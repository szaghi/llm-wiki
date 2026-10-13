// One colour per OKF page type, shared by the page graph and its legend.
export const TYPE_COLORS: Record<string, string> = {
  Definition: '#8e6bd8',
  Method: '#2f80ed',
  Operator: '#00a3a3',
  Result: '#e2574c',
  Property: '#e5a000',
  Benchmark: '#27ae60',
  Software: '#c2549d',
  Concept: '#7f8c8d',
  Source: '#9aa5b1',
}

export function typeColor(type: string): string {
  return TYPE_COLORS[type] ?? '#7f8c8d'
}

// One colour per bundle on the bundle map, assigned in registry order.
export const BUNDLE_COLORS = ['#2f80ed', '#e2574c', '#27ae60', '#8e6bd8', '#e5a000', '#00a3a3', '#c2549d']
