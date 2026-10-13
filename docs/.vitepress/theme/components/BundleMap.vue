<script setup lang="ts">
// The bundle map: bundles as nodes, edges weighted by what two bundles share (cited works, ingested
// sources, concepts with the same name or alias). Data: public/data/bundles.json (tools/site_sync.py).
// The overlaps are computed at build time: bundle content itself never links across bundles (D12).
import { computed, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import { BUNDLE_COLORS } from './palette'

interface Page {
  title: string
  url: string
}
interface Bundle {
  slug: string
  title: string
  sources: number
  concepts: number
}
interface Overlap {
  a: string
  b: string
  sharedWorks: number
  sharedSources: { a: Page; b: Page }[]
  sharedConcepts: { a: Page; b: Page; names: string[]; samePage: boolean }[]
}

const bundles = ref<Bundle[]>([])
const overlaps = ref<Overlap[]>([])
const selected = ref(0)
const W = 720
const H = 440

onMounted(async () => {
  const res = await fetch(withBase('/data/bundles.json'))
  const data = await res.json()
  bundles.value = data.bundles
  overlaps.value = data.overlaps
  // open on the pair that shares the most
  let best = 0
  data.overlaps.forEach((o: Overlap, i: number) => {
    if (o.sharedWorks > data.overlaps[best].sharedWorks) best = i
  })
  selected.value = best
})

const layout = computed(() => {
  const n = bundles.value.length
  const r = n > 1 ? Math.min(W, H) * 0.32 : 0
  const max = Math.max(1, ...bundles.value.map((b) => b.sources + b.concepts))
  const pos: Record<string, { x: number; y: number; r: number; color: string; b: Bundle }> = {}
  bundles.value.forEach((b, i) => {
    const t = -Math.PI / 2 + (2 * Math.PI * i) / Math.max(n, 1)
    pos[b.slug] = {
      x: W / 2 + r * Math.cos(t) * 1.25,
      y: H / 2 + r * Math.sin(t),
      r: 26 + 30 * Math.sqrt((b.sources + b.concepts) / max),
      color: BUNDLE_COLORS[i % BUNDLE_COLORS.length],
      b,
    }
  })
  return pos
})

// an edge label sits beside the edge's midpoint, pushed away from the centre of the map so labels never cross
function label(o: Overlap) {
  const a = layout.value[o.a]
  const b = layout.value[o.b]
  if (!a || !b) return { x: 0, y: 0, anchor: 'middle' }
  const mx = (a.x + b.x) / 2
  const my = (a.y + b.y) / 2
  const dx = mx - W / 2
  const dy = my - H / 2
  const n = Math.hypot(dx, dy) || 1
  const x = mx + (dx / n) * 34
  const y = my + (dy / n) * 34
  return { x, y, anchor: dx / n > 0.3 ? 'start' : dx / n < -0.3 ? 'end' : 'middle' }
}

const maxWorks = computed(() => Math.max(1, ...overlaps.value.map((o) => o.sharedWorks)))
const current = computed(() => overlaps.value[selected.value])
const plural = (n: number, word: string) => `${n} ${word}${n === 1 ? '' : 's'}`
const titleOf = (slug: string) => bundles.value.find((b) => b.slug === slug)?.title ?? slug
const href = (url: string) => withBase(url)
</script>

<template>
  <div class="bm">
    <svg :viewBox="`0 0 ${W} ${H}`" role="img" aria-label="Map of the bundles and what they share">
      <g v-for="(o, i) in overlaps" :key="o.a + o.b" class="bm-edge" :class="{ on: i === selected }" @click="selected = i">
        <line
          :x1="layout[o.a]?.x"
          :y1="layout[o.a]?.y"
          :x2="layout[o.b]?.x"
          :y2="layout[o.b]?.y"
          :stroke-width="2 + 14 * Math.sqrt(o.sharedWorks / maxWorks)"
        />
        <text :x="label(o).x" :y="label(o).y" :text-anchor="label(o).anchor">
          <tspan :x="label(o).x" dy="0">{{ o.sharedWorks }} shared works</tspan>
          <tspan :x="label(o).x" dy="15">{{ plural(o.sharedSources.length, 'source') }} · {{ plural(o.sharedConcepts.length, 'concept') }}</tspan>
        </text>
      </g>
      <a v-for="(p, slug) in layout" :key="slug" :href="href(`/bundles/${slug}/`)" class="bm-node">
        <circle :cx="p.x" :cy="p.y" :r="p.r" :fill="p.color" />
        <text :x="p.x" :y="p.y + p.r + 18" text-anchor="middle" class="bm-title">{{ p.b.title }}</text>
        <text :x="p.x" :y="p.y + 5" text-anchor="middle" class="bm-count">{{ p.b.sources }} · {{ p.b.concepts }}</text>
      </a>
    </svg>
    <p class="bm-legend">
      Circle size: sources + concept pages (the numbers inside, in that order). Edge width: cited works the two
      bundles share. Click a bundle to open it, an edge to list what the two bundles share.
    </p>

    <div v-if="current" class="bm-detail">
      <h3>{{ titleOf(current.a) }} ↔ {{ titleOf(current.b) }}</h3>
      <p>
        <strong>{{ current.sharedWorks }}</strong> works are cited by both bundles (matched by DOI, else by title and
        year).
      </p>
      <template v-if="current.sharedSources.length">
        <h4>Sources ingested in both ({{ current.sharedSources.length }})</h4>
        <p class="bm-note">The same paper, compiled twice: each bundle reads it for its own domain.</p>
        <table>
          <thead>
            <tr>
              <th>{{ titleOf(current.a) }}</th>
              <th>{{ titleOf(current.b) }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="s in current.sharedSources" :key="s.a.url">
              <td><a :href="href(s.a.url)">{{ s.a.title }}</a></td>
              <td><a :href="href(s.b.url)">{{ s.b.title }}</a></td>
            </tr>
          </tbody>
        </table>
      </template>
      <template v-if="current.sharedConcepts.length">
        <h4>Related concepts ({{ current.sharedConcepts.length }})</h4>
        <p class="bm-note">
          Pages with the same file name, or sharing a title or alias. Same-name pages describe one subject from two
          domains; an alias match can be looser: the shared name is shown so you can judge it.
        </p>
        <table>
          <thead>
            <tr>
              <th>{{ titleOf(current.a) }}</th>
              <th>{{ titleOf(current.b) }}</th>
              <th>Matched on</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="c in current.sharedConcepts" :key="c.a.url + c.b.url">
              <td><a :href="href(c.a.url)">{{ c.a.title }}</a></td>
              <td><a :href="href(c.b.url)">{{ c.b.title }}</a></td>
              <td>{{ c.samePage ? 'same page name' : c.names.join(', ') }}</td>
            </tr>
          </tbody>
        </table>
      </template>
    </div>
  </div>
</template>
