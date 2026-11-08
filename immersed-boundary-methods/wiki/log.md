# Update log

## 2026-11-08

**Chunk 1 ingested (night protocol, D32): the founding papers.** Sources:
peskin-1972, goldstein-1993, leveque-1994, pember-1995, fedkiw-1999,
ye-1999, angot-1999, fadlun-2000, kim-2001, peskin-2002 (10 of 57).

- Bundle scaffolded: `bundle.toml`, `CLAUDE.md`, `raw/`, `wiki/index.md`,
  `wiki/log.md`, `wiki/notation.md`.
- Registry created from chunk 1 (domain, fluid, Lagrangian description,
  coupling operators, forcing and penalization, cut cells, interfaces and
  level sets); conventions fixed: normal out of the body, $\varphi$ for the
  delta kernel because $\phi$ is the level set, $\kappa$ for the volume
  fraction, $\mathbf q$ for conserved variables, order of accuracy $r$.
- Concept pages created (18): definitions/immersed-boundary-method,
  definitions/sharp-and-diffuse-interface, definitions/small-cell-problem,
  operators/regularized-delta-function, operators/spreading-and-interpolation,
  methods/classical-immersed-boundary-method, methods/feedback-forcing,
  methods/direct-forcing, methods/volume-penalization,
  methods/immersed-interface-method, methods/ghost-fluid-method,
  methods/cut-cell-method, methods/redistribution,
  results/first-order-accuracy-of-regularized-delta-forcing,
  results/convergence-of-volume-penalization,
  properties/discrete-conservation, benchmarks/flow-past-circular-cylinder,
  benchmarks/flow-past-sphere.
- Source pages created (10), one per source above.
- Bibliography: 312 entries from the ten reference lists (six from Crossref
  deposits, four transcribed from the printed lists: goldstein-1993 and
  pember-1995 through OCR, angot-1999, peskin-2002); `bib_merge.py` FLAGS 0
  after 2 aliases and 11 verified silences; undated in-press citations keyed
  by the citing paper's year.
- Deep lint (compiler self-audit of the 18 concept pages against the
  registry): section references the OCR texts cannot support replaced by
  part names; paper-native symbols removed (Ye's $\phi$ → $w$, Pember's
  update formula described in words because the OCR does not show it);
  no contradiction opened.
