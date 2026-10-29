// File-system helpers of the build parts (parts.mjs), for the site config and the build script only.

import { readdirSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { GROUPS, SPLIT_MB, groupOf } from './parts.mjs'

function markdownBytes(dir) {
  let total = 0
  for (const name of readdirSync(dir)) {
    const path = join(dir, name)
    if (statSync(path).isDirectory()) total += markdownBytes(path)
    else if (name.endsWith('.md')) total += statSync(path).size
  }
  return total
}

// the bundles of `slugs` (pages generated under `bundlesDir`) that are built as page groups
export function splitBundles(bundlesDir, slugs) {
  return slugs.filter((s) => markdownBytes(join(bundlesDir, s)) > SPLIT_MB * 1024 * 1024)
}

// srcExclude patterns (relative to the docs root) that leave only the pages of `group` in bundle `slug`
export function excludeOtherGroups(bundlesDir, slug, group) {
  return readdirSync(join(bundlesDir, slug))
    .filter((name) => groupOf(statSync(join(bundlesDir, slug, name)).isDirectory() ? `${name}/` : name) !== group)
    .map((name) => (statSync(join(bundlesDir, slug, name)).isDirectory() ? `bundles/${slug}/${name}/**` : `bundles/${slug}/${name}`))
}

// the page groups present in bundle `slug` (a part with no pages is not built)
export function groupsOf(bundlesDir, slug) {
  const names = readdirSync(join(bundlesDir, slug))
  return GROUPS.filter((g) => names.some((name) => groupOf(statSync(join(bundlesDir, slug, name)).isDirectory() ? `${name}/` : name) === g))
}
