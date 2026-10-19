import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import PageMeta from './components/PageMeta.vue'
import PageGraph from './components/PageGraph.vue'
import BundleMap from './components/BundleMap.vue'
import BundleCards from './components/BundleCards.vue'
import 'katex/dist/katex.min.css'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      // the OKF frontmatter of a wiki page (type, status, tags, source identity) above its body
      'doc-before': () => h(PageMeta),
    }),
  enhanceApp({ app, router, siteData }) {
    app.component('PageGraph', PageGraph)
    app.component('BundleMap', BundleMap)
    app.component('BundleCards', BundleCards)
    // The production site is built in parts (the documentation, then one part per bundle; see
    // scripts/build.mjs), and the client router of a part knows only that part's pages. A link into
    // another part must load the page in full.
    const scope = siteData.value.themeConfig.buildScope
    if (typeof window === 'undefined' || !scope || scope === 'all') return
    const base = siteData.value.base
    const partOf = (href: string) => {
      const path = new URL(href, window.location.href).pathname.slice(base.length)
      return path.match(/^bundles\/([^/]+)\//)?.[1] ?? 'main'
    }
    // History steps need no hook: within one document the history holds only this part's pages, and an
    // entry of another document is loaded by the browser. The current page is never redirected: it may
    // be the 404 page the server sent for another part's missing page, which would then reload forever.
    router.onBeforeRouteChange = (href) => {
      const target = new URL(href, window.location.href)
      if (partOf(href) === scope || target.pathname === window.location.pathname) return
      window.location.assign(href)
      return false
    }
  },
} satisfies Theme
