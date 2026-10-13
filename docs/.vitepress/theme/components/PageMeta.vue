<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'

const { frontmatter } = useData()
const fm = computed(() => frontmatter.value)

// the resource of a Source page as a link: doi:, arXiv: and plain URLs
const resource = computed(() => {
  const r = String(fm.value.resource ?? '').trim()
  if (!r) return null
  if (r.startsWith('doi:')) return { text: r, href: `https://doi.org/${r.slice(4)}` }
  if (/^arxiv:/i.test(r)) return { text: r, href: `https://arxiv.org/abs/${r.slice(6)}` }
  if (/^https?:\/\//.test(r)) return { text: r, href: r }
  return { text: r, href: null }
})

const authors = computed(() => (Array.isArray(fm.value.authors) ? fm.value.authors.join(', ') : ''))
const bundleHome = computed(() => withBase(`/bundles/${fm.value.bundle}/`))
</script>

<template>
  <div v-if="fm.bundle" class="okf-meta">
    <div class="okf-meta-row">
      <a class="okf-bundle" :href="bundleHome">{{ fm.bundleTitle }}</a>
      <span v-if="fm.type" class="okf-badge okf-type">{{ fm.type }}</span>
      <span
        v-if="fm.status"
        class="okf-badge"
        :class="fm.status === 'hypothesis' ? 'okf-hypothesis' : 'okf-established'"
        :title="
          fm.status === 'hypothesis'
            ? 'A claim a published source could still overturn: not literature fact.'
            : 'A published, peer-reviewed result.'
        "
        >{{ fm.status }}</span
      >
      <span v-for="tag in fm.tags || []" :key="tag" class="okf-tag">#{{ tag }}</span>
    </div>
    <div v-if="fm.type === 'Source'" class="okf-source">
      <span v-if="authors">{{ authors }}</span>
      <span v-if="fm.year"> ({{ fm.year }})</span>
      <span v-if="fm.venue">, <em>{{ fm.venue }}</em></span>
      <span v-if="resource">
        ·
        <a v-if="resource.href" :href="resource.href" target="_blank" rel="noopener">{{ resource.text }}</a>
        <span v-else>{{ resource.text }}</span>
      </span>
      <span v-if="fm.local_file" class="okf-local" title="The compiler's local copy; source files are not distributed with the wiki."
        > · local copy not distributed</span
      >
    </div>
    <p v-if="fm.description && fm.type" class="okf-description">{{ fm.description }}</p>
  </div>
</template>
