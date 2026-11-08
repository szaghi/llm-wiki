# Update log

## 2026-11-08

**Chunk 2 ingested (night protocol, D32).** Sources: tseng-2003,
mittal-2005, uhlmann-2005, colella-2006, ghias-2007, taira-2007,
mittal-2008, tan-2010, chaudhuri-2011, burman-2015 (20 of 57).

- Concept pages created (6): methods/ghost-cell-method,
  definitions/fresh-cell-problem, methods/immersed-boundary-projection-method,
  methods/inverse-lax-wendroff, methods/cutfem,
  benchmarks/shock-obstacle-interaction.
- Concept pages updated (15): definitions/immersed-boundary-method (formal
  continuous/discrete forcing dichotomy, grid scaling, later families),
  definitions/sharp-and-diffuse-interface, definitions/small-cell-problem,
  operators/regularized-delta-function, operators/spreading-and-interpolation,
  methods/direct-forcing (Lagrangian direct forcing), methods/feedback-forcing,
  methods/volume-penalization, methods/classical-immersed-boundary-method,
  methods/cut-cell-method (formally consistent EB), methods/redistribution
  (hybrid update), methods/ghost-fluid-method, properties/discrete-conservation
  (accuracy–conservation trade-off), results/first-order-accuracy-of-regularized-delta-forcing,
  benchmarks/flow-past-circular-cylinder, benchmarks/flow-past-sphere.
- Registry extended: rigid-body velocity $\mathbf u_c$, $\boldsymbol\omega_c$,
  $\mathbf x_c$; ghost-cell points $\mathbf x_{BI}$, $\mathbf x_{IP}$, $\Delta l$;
  classification symbols $\mathbf f_b$, $[L]$, $[L']$.
- Source pages created (10); audit lists of all 20 Source pages regenerated.
- Bibliography: 609 entries (from 312), all ten lists from Crossref deposits;
  `bib_merge.py` FLAGS 0 after 18 aliases (same key, different works:
  verzicco-2000-b, verzicco-1996-b, liu-1998-b, quirk-1994-b, beyer-1992-b,
  lee-2003-b, mittal-1999-b, mittal-2002-c, fedkiw-2002-b, iaccarino-2003-b,
  peskin-1972-b for the thesis, the swapped Mittal 1997 pair, GetFEM++/LifeV)
  and 12 verified silences; same-key venue check clean.
- Deep lint (compiler self-audit of the 21 touched concept pages): paper
  symbols translated (Taira's $q$ → $\mathbf u$, his pressure $\phi$ → $\mathbf p$),
  section references without a printed heading replaced by part names
  (Mittal & Iaccarino 2005), Colella's redistribution formula marked as
  reconstructed from the prose; no contradiction opened.

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
