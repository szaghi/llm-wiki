# Update log

## 2026-11-08

**Chunk 5 ingested (night protocol, D33).** Sources: wang-2024,
dzanic-2024, ma-2024, kim-2025, liao-2025, chen-2025, wang-2025, bach-2025,
hu-2026, kirilov-2026 (48 of 56).

- Concept page created (1): methods/reinforcement-learning-meshing.
- Concept pages updated (8): methods/moving-mesh-pde (tokamak MHD),
  methods/conservative-metric-evaluation (multi-resolution, linear streams,
  mimetic metrics), properties/free-stream-preservation (stronger
  requirements), properties/geometric-conservation-law (Runge–Kutta),
  methods/neural-network-mesh-generation (attention and Fourier features),
  methods/high-order-mesh-curving (review classification, third-party
  meshes), software/nekmesh, definitions/high-order-mesh-validity.
- Source pages created (10); audit lists regenerated, no older list changed.
- Bibliography: 1710 entries (from 1338), FLAGS 0. wang-2025-c (a grid
  stitching paper) separated from the ingested key; two anonymous 2018
  Chinese papers printed in swapped order resolved by title; the ECCOMAS
  paper turner-2016-b and the ADIGMA book kroll-2010-b merged across title
  variants. The hu-2026 deposit contains garbled entries (e.g. titles
  "forum", "fluid dynamics conference"); they are kept as deposited.

**Chunk 4 ingested (night protocol, D33).** Sources: han-2022,
barrera-2023, rochery-2023, peng-2023, su-2023, camier-2023, su-2023-b,
chen-2023, green-2024 (38 of 56). Archive file 036, named after Galbraith et
al.'s HLPW-4/GMGW-3 summary, holds the Allmaras–Johnson–Spalart note on the
Spalart–Allmaras model and is not ingested (left to the human); a title-word
check of all 56 files finds no further mismatch.

- Concept page created (1): software/nekmesh.
- Concept pages updated (6): methods/conservative-metric-evaluation (three
  upwind routes), methods/target-matrix-optimization (GPUs, implicit
  geometries), methods/high-order-mesh-curving (linear-programming
  correction, cavity remeshing, production tools),
  definitions/high-order-mesh-validity, methods/neural-network-mesh-generation
  (coarse-mesh data), definitions/boundary-fitted-coordinate-system
  (mapped-mesh AMR).
- Registry extended: level-set function $\sigma$ and penalty weight
  $w_\sigma$.
- Source pages created (9); audit lists regenerated, no older list changed.
- Bibliography: 1338 entries (from 1045), FLAGS 0. chen-2023's deposit
  lists the paper itself (reference 36), not entered; camier-2022 (a 2022
  citation without venue) kept distinct from the ingested camier-2023; the
  two Liao 2015 papers resolved by DOI; rochery-2023-b (the author's thesis)
  separated from the ingested key; turner-2016 cited with two venues (the
  DOI-bearing Procedia Eng. 163:340 and a misprinted 82:127) kept as one.

**Chunk 3 ingested (night protocol, D33).** Sources: dobrev-2019,
dobrev-2020, yu-2020, dobrev-2022, assonitis-2022, elaouad-2022, chen-2022,
cicchino-2022, nikl-2022 (29 of 56). Archive file 025, named after
Pietroni et al.'s hex-mesh survey, holds the VTK file-format manual and is
not ingested (left to the human).

- Concept pages created (4): methods/target-matrix-optimization,
  methods/shock-fitting, methods/neural-network-mesh-generation,
  methods/anisotropic-mesh-adaptation.
- Concept pages updated (5): methods/conservative-metric-evaluation (WENO
  on the solution, MHD potential, flux-reconstruction curl forms),
  properties/free-stream-preservation (stability on curved elements),
  definitions/boundary-fitted-coordinate-system (curvilinear Lagrangian
  meshes), definitions/mesh-quality-metric, methods/moving-mesh-pde.
- Source pages created (9); audit lists regenerated, knupp-2001 changed.
- Bibliography: 1045 entries (from 678), FLAGS 0. cerveny-2018 (a 2018
  citation without venue) kept distinct from the SISC paper cerveny-2019;
  cicchino-2022-b separated from the ingested key; kolev-2009-b normalized.

**Chunk 2 ingested (night protocol, D33).** Sources: visbal-2002,
tang-2003, kopriva-2006, nonomura-2010, deng-2011, xie-2013, deng-2013,
johnen-2013, toulorge-2013, zhu-2019 (20 of 56).

- Concept pages created (3): methods/conservative-metric-evaluation,
  definitions/high-order-mesh-validity, methods/high-order-mesh-curving.
- Concept pages updated (6): properties/free-stream-preservation (3-D,
  error forms, surface conservation law), properties/geometric-conservation-law
  (time metrics from the GCL), methods/moving-mesh-pde (conservative
  interpolation), results/grid-induced-truncation-error (filters, randomized
  grids), definitions/mesh-quality-metric (curved elements),
  definitions/boundary-fitted-coordinate-system (unstructured curvilinear
  meshes).
- Registry extended: flux and metric operators $\delta_i$,
  $\delta^{\mathrm o}_i$, $\delta^{\mathrm{in}}_i$; interpolation $\mathcal I_k$;
  straight-sided Jacobian $J_0$ and distortion $\mathcal D$.
- Source pages created (10); audit lists regenerated, thomas-1979 changed.
- Bibliography: 678 entries (from 470), FLAGS 0. **Chunk-1 record
  repaired:** three ingested keys held other works cited by thompson-1982
  (thomas-1979 a boundary-condition report, steger-1979 an FSI report,
  steger-1980 the aileron-buzz paper); they were rekeyed (thomas-1979-b,
  steger-1979-c, steger-1980-e), the ingested JCP note moved to steger-1979,
  and thomas-1980 (same DOI as the ingested paper, deposit year 1980) to
  thomas-1979. A check that every ingested key holds its own work now runs
  after each merge. Three keys normalized (karniadakis-2004,
  zienkiewicz-1983, zienkiewicz-2000).
- Deep lint (self-audit of the 9 touched pages): canonical notation; the
  inverse-Jacobian convention of visbal-2002 translated on its Source page.

**Chunk 1 ingested; bundle founded (night protocol, D33).** Sources:
winslow-1966, gordon-1973, thompson-1974, thomas-1979, steger-1979,
steger-1980, brackbill-1982, thompson-1982, huang-1994, knupp-2001
(10 of 56).

- Bundle scaffolded: `bundle.toml`, bundle law (`CLAUDE.md`),
  `INGESTION-ISSUES.md`, `raw/`, and the wiki root (`index.md`, `log.md`,
  `notation.md`); DECISIONS D33.
- Registry seeded from chunk 1: physical and curvilinear coordinates, the
  mapping and its Jacobian, base vectors, metric tensor, metric terms and
  identities, moving-grid symbols and the geometric conservation law,
  transfinite-interpolation projectors, control functions, variational
  functionals, monitor function and relaxation time, element and target
  Jacobians and the condition number, and flow symbols.
- Concept pages created (11): definitions/boundary-fitted-coordinate-system
  (hub), definitions/equidistribution-principle, definitions/mesh-quality-metric,
  methods/transfinite-interpolation, methods/elliptic-grid-generation,
  methods/hyperbolic-grid-generation, methods/variational-grid-generation,
  methods/moving-mesh-pde, properties/geometric-conservation-law,
  properties/free-stream-preservation, results/grid-induced-truncation-error.
- Source pages created (10), with audit lists.
- Bibliography: 470 entries, FLAGS 0. Cited-DOI metadata fetched from
  Crossref for DOI-only deposits. Resolution: autoresolve (DOI or title to
  the family key, fragment keys reserved) plus hand corrections:
  brackbill-1982 kept distinct from thompson-1982's pre-publication
  citation brackbill-1981, thompson-1977-c (NASA CR-2729) separated from
  the TOMCAT paper thompson-1977, huang-1994-b (Huang & Sloan) separated
  from the ingested huang-1994, noh-1964 cited at two pages of one chapter;
  six keys normalized from deposited author strings (anderson-1983-b,
  madsen-1984, white-1979, george-1998, zienkiewicz-1969,
  zienkiewicz-1971-b).
- Deep lint (self-audit of the 11 pages): canonical notation only; section
  numbers cited only where printed; claims checked against the text layers.
