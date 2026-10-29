// Parts of the production build (scripts/build.mjs), shared by the build script, the site config and the theme
// (browser code: no Node imports here; the file-system helpers are in parts-node.mjs).
//
// The site is built as one part for the documentation and the bundle list ("main") and one part per bundle
// ("<slug>"). A bundle whose pages exceed SPLIT_MB is built as three parts instead, one per page group
// ("<slug>/sources", "<slug>/bibliography", "<slug>/pages"): the heap of one Vite build grows with the pages it
// bundles, and the largest bundles outgrew the CI runner as single parts.

export const SPLIT_MB = 6
export const GROUPS = ['sources', 'bibliography', 'pages']

// page group of a path inside a bundle (`sources/x`, `bibliography`, `bibliography.md`, `methods/y`, ``)
export function groupOf(rest) {
  if (rest.startsWith('sources/')) return 'sources'
  if (/^bibliography(\.(md|html))?([#?]|$)/.test(rest)) return 'bibliography'
  return 'pages'
}

// part of a site path (with or without the leading slash, after the base); `split` lists the split bundles
export function partOf(path, split) {
  const m = path.match(/^\/?bundles\/([^/]+)\/(.*)$/)
  if (!m) return 'main'
  return split.includes(m[1]) ? `${m[1]}/${groupOf(m[2])}` : m[1]
}
