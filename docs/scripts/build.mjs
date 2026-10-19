// Build the documentation site in parts and merge them into .vitepress/dist.
//
// One Vite build of every page needs a heap that grows with the whole corpus (it outgrew the 16 GB CI
// runner in October 2026). The site is therefore built as one part for the documentation and the bundle
// list (DOCS_SCOPE=main) and one part per bundle (DOCS_SCOPE=<slug>), each with the same base, so links
// and asset URLs are those of a single site. The parts are merged afterwards: page files never collide,
// assets are content-hashed, and the few unhashed files (404.html, vp-icons.css) are the main part's.
// The theme sends links that leave a part to a full page load (.vitepress/theme/index.ts).
//
// Usage: node scripts/build.mjs   (after tools/site_sync.py; npm run docs:build does both)

import { spawnSync } from 'node:child_process'
import { cpSync, existsSync, mkdirSync, readFileSync, readdirSync, rmSync, statSync } from 'node:fs'
import { join } from 'node:path'

const HEAP_MB = process.env.DOCS_HEAP_MB || '8192'
const parts = join('.vitepress', 'parts')
const dist = join('.vitepress', 'dist')
const generated = JSON.parse(readFileSync(join('.vitepress', 'generated', 'bundles.json'), 'utf-8'))
const slugs = generated.nav.map((n) => n.link.split('/')[2])

function build(scope) {
  const outDir = join(parts, scope)
  const started = Date.now()
  const run = spawnSync(
    process.execPath,
    [`--max-old-space-size=${HEAP_MB}`, join('node_modules', 'vitepress', 'bin', 'vitepress.js'), 'build'],
    { stdio: 'inherit', env: { ...process.env, DOCS_SCOPE: scope, DOCS_OUT: outDir } },
  )
  if (run.status !== 0) {
    console.error(`build of part "${scope}" failed (exit ${run.status ?? run.signal})`)
    process.exit(1)
  }
  console.log(`part "${scope}" built in ${((Date.now() - started) / 1000).toFixed(0)} s`)
  return outDir
}

// copy src into dst without replacing what is already there
function merge(src, dst) {
  for (const name of readdirSync(src)) {
    const from = join(src, name)
    const to = join(dst, name)
    if (statSync(from).isDirectory()) {
      mkdirSync(to, { recursive: true })
      merge(from, to)
    } else if (!existsSync(to)) {
      cpSync(from, to)
    }
  }
}

rmSync(parts, { recursive: true, force: true })
rmSync(dist, { recursive: true, force: true })
mkdirSync(dist, { recursive: true })
merge(build('main'), dist)
for (const slug of slugs) {
  const out = build(slug)
  merge(join(out, 'bundles', slug), join(dist, 'bundles', slug))
  merge(join(out, 'assets'), join(dist, 'assets'))
}
rmSync(parts, { recursive: true, force: true })
console.log(`site merged into ${dist}: 1 + ${slugs.length} parts`)
