<script setup lang="ts">
// Interactive page graph of one bundle: every page a node, every wiki link an edge.
// Data: public/data/<bundle>.graph.json, written by tools/site_sync.py.
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useRouter, withBase } from 'vitepress'
import { TYPE_COLORS, typeColor } from './palette'

const props = defineProps<{ bundle: string }>()
const router = useRouter()

interface GNode {
  id: string
  title: string
  type: string
  status: string
  url: string
  degree?: number
  x?: number
  y?: number
  fx?: number | null
  fy?: number | null
}
interface GLink {
  source: string | GNode
  target: string | GNode
}

const svgEl = ref<SVGSVGElement | null>(null)
const title = ref('')
const nodes = ref<GNode[]>([])
const links = ref<GLink[]>([])
const query = ref('')
const hidden = ref<Set<string>>(new Set(['Source']))
const hover = ref<GNode | null>(null)
const error = ref('')

const types = computed(() => {
  const count: Record<string, number> = {}
  for (const n of nodes.value) count[n.type] = (count[n.type] ?? 0) + 1
  return Object.keys(TYPE_COLORS)
    .filter((t) => count[t])
    .map((t) => ({ type: t, count: count[t] }))
})

let stop: (() => void) | null = null
let applyQuery: () => void = () => {}

function toggle(type: string) {
  const next = new Set(hidden.value)
  if (next.has(type)) next.delete(type)
  else next.add(type)
  hidden.value = next
}

async function draw() {
  stop?.()
  const d3 = await import('d3')
  const svg = d3.select(svgEl.value!)
  svg.selectAll('*').remove()
  const width = svgEl.value!.clientWidth || 900
  const height = svgEl.value!.clientHeight || 640

  const shown = nodes.value.filter((n) => !hidden.value.has(n.type)).map((n) => ({ ...n }))
  const ids = new Set(shown.map((n) => n.id))
  const edges = links.value
    .map((l) => ({ source: l.source as string, target: l.target as string }))
    .filter((l) => ids.has(l.source) && ids.has(l.target))
  const degree: Record<string, number> = {}
  const neighbours = new Map<string, Set<string>>()
  for (const e of edges) {
    degree[e.source] = (degree[e.source] ?? 0) + 1
    degree[e.target] = (degree[e.target] ?? 0) + 1
    if (!neighbours.has(e.source)) neighbours.set(e.source, new Set())
    if (!neighbours.has(e.target)) neighbours.set(e.target, new Set())
    neighbours.get(e.source)!.add(e.target)
    neighbours.get(e.target)!.add(e.source)
  }
  for (const n of shown) n.degree = degree[n.id] ?? 0

  const root = svg.append('g')
  svg.call(
    d3
      .zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.2, 6])
      .on('zoom', (ev) => root.attr('transform', ev.transform)),
  )

  const sim = d3
    .forceSimulation(shown as any)
    .force('link', d3.forceLink(edges as any).id((d: any) => d.id).distance(55).strength(0.25))
    .force('charge', d3.forceManyBody().strength(-110))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('x', d3.forceX(width / 2).strength(0.04))
    .force('y', d3.forceY(height / 2).strength(0.06))
    .force('collide', d3.forceCollide().radius((d: any) => 5 + Math.sqrt(d.degree)))

  const link = root.append('g').attr('class', 'pg-links').selectAll('line').data(edges).join('line')

  const node = root
    .append('g')
    .selectAll('circle')
    .data(shown)
    .join('circle')
    .attr('class', (d) => 'pg-node' + (d.status === 'hypothesis' ? ' pg-hypothesis' : ''))
    .attr('r', (d) => 4 + Math.sqrt(d.degree ?? 0) * 1.6)
    .attr('fill', (d) => typeColor(d.type))
    .on('mouseenter', (_, d) => {
      hover.value = d
      const near = neighbours.get(d.id) ?? new Set()
      node.classed('pg-dim', (n) => n.id !== d.id && !near.has(n.id))
      link.classed('pg-dim', (l: any) => l.source.id !== d.id && l.target.id !== d.id)
    })
    .on('mouseleave', () => {
      hover.value = null
      applyQuery()
    })
    .on('click', (_, d) => router.go(withBase(d.url)))
    .call(
      d3
        .drag<SVGCircleElement, GNode>()
        .on('start', (ev, d) => {
          if (!ev.active) sim.alphaTarget(0.3).restart()
          d.fx = d.x
          d.fy = d.y
        })
        .on('drag', (ev, d) => {
          d.fx = ev.x
          d.fy = ev.y
        })
        .on('end', (ev, d) => {
          if (!ev.active) sim.alphaTarget(0)
          d.fx = null
          d.fy = null
        }) as any,
    )

  const label = root
    .append('g')
    .selectAll('text')
    .data(shown.filter((n) => (n.degree ?? 0) >= 12))
    .join('text')
    .attr('class', 'pg-label')
    .text((d) => (d.title.length > 34 ? d.title.slice(0, 32) + '…' : d.title))

  sim.on('tick', () => {
    link
      .attr('x1', (d: any) => d.source.x)
      .attr('y1', (d: any) => d.source.y)
      .attr('x2', (d: any) => d.target.x)
      .attr('y2', (d: any) => d.target.y)
    node.attr('cx', (d) => d.x!).attr('cy', (d) => d.y!)
    label.attr('x', (d) => d.x! + 8).attr('y', (d) => d.y! + 4)
  })

  applyQuery = () => {
    const q = query.value.trim().toLowerCase()
    node.classed('pg-dim', (n) => !!q && !n.title.toLowerCase().includes(q))
    node.classed('pg-match', (n) => !!q && n.title.toLowerCase().includes(q))
    link.classed('pg-dim', !!q)
  }
  applyQuery()
  stop = () => sim.stop()
}

watch(query, () => applyQuery())
watch(hidden, () => draw())

onMounted(async () => {
  try {
    const res = await fetch(withBase(`/data/${props.bundle}.graph.json`))
    const data = await res.json()
    title.value = data.title
    nodes.value = data.nodes
    links.value = data.links
    await draw()
  } catch {
    error.value = `Graph data not found for ${props.bundle}: run tools/site_sync.py.`
  }
})
onBeforeUnmount(() => stop?.())
</script>

<template>
  <div class="pg">
    <div class="pg-head">
      <h1>{{ title }}: page graph</h1>
      <p>
        Every page of the bundle is a node and every wiki link an edge. Bigger nodes are linked more often; a dashed
        outline marks a <em>hypothesis</em> page. Hover to see a page's neighbours, click to open it, scroll to zoom,
        drag to move. Sources are hidden at first: turn them on to see which papers each concept rests on.
      </p>
      <div class="pg-controls">
        <input v-model="query" type="search" placeholder="Highlight pages by title…" aria-label="Highlight pages by title" />
        <button
          v-for="t in types"
          :key="t.type"
          class="pg-chip"
          :class="{ off: hidden.has(t.type) }"
          :style="{ '--chip': typeColor(t.type) }"
          @click="toggle(t.type)"
        >
          {{ t.type }} ({{ t.count }})
        </button>
      </div>
    </div>
    <p v-if="error" class="pg-error">{{ error }}</p>
    <div class="pg-canvas">
      <svg ref="svgEl" role="img" :aria-label="`Page graph of ${title}`"></svg>
      <div v-if="hover" class="pg-tip">
        <strong>{{ hover.title }}</strong>
        <span>{{ hover.type }}<template v-if="hover.status"> · {{ hover.status }}</template> · {{ hover.degree }} links</span>
      </div>
    </div>
  </div>
</template>
