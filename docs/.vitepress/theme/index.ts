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
  enhanceApp({ app }) {
    app.component('PageGraph', PageGraph)
    app.component('BundleMap', BundleMap)
    app.component('BundleCards', BundleCards)
  },
} satisfies Theme
