<script setup lang="ts">
// The bundle list: one card per bundle with its derived statistics (tools/bundles.py via site_sync.py).
import { onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import { BUNDLE_COLORS } from './palette'

interface Bundle {
  slug: string
  title: string
  summary: string
  sources: number
  concepts: number
  by_type: Record<string, number>
  hypotheses: number
  contested: number
  cited_works: number
  frontier: number
  updated: string
}

const bundles = ref<Bundle[]>([])
onMounted(async () => {
  const res = await fetch(withBase('/data/bundles.json'))
  bundles.value = (await res.json()).bundles
})
const href = (url: string) => withBase(url)
</script>

<template>
  <div class="bc-grid">
    <article v-for="(b, i) in bundles" :key="b.slug" class="bc-card" :style="{ '--bundle': BUNDLE_COLORS[i % BUNDLE_COLORS.length] }">
      <h3>
        <a :href="href(`/bundles/${b.slug}/`)">{{ b.title }}</a>
      </h3>
      <code class="bc-slug">{{ b.slug }}</code>
      <p>{{ b.summary }}</p>
      <dl>
        <div><dt>Sources</dt><dd>{{ b.sources }}</dd></div>
        <div><dt>Concept pages</dt><dd>{{ b.concepts }}</dd></div>
        <div><dt>Cited works</dt><dd>{{ b.cited_works }}</dd></div>
        <div title="Cited by an ingested source but not ingested: the derived ingestion frontier">
          <dt>Frontier</dt><dd>{{ b.frontier }}</dd>
        </div>
        <div title="Concept pages with a Contradictions section"><dt>Contested pages</dt><dd>{{ b.contested }}</dd></div>
        <div title="Concept pages with status: hypothesis"><dt>Hypotheses</dt><dd>{{ b.hypotheses }}</dd></div>
      </dl>
      <p class="bc-links">
        <a :href="href(`/bundles/${b.slug}/`)">Reading guide</a> ·
        <a :href="href(`/bundles/${b.slug}/graph`)">Page graph</a> ·
        <a :href="href(`/bundles/${b.slug}/notation`)">Notation</a> ·
        <a :href="href(`/bundles/${b.slug}/bibliography`)">Bibliography</a>
        <span class="bc-updated">updated {{ b.updated }}</span>
      </p>
    </article>
  </div>
</template>
