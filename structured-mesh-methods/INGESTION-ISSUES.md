# Ingestion issues — structured-mesh-methods

Reviewer's digest, one section per chunk, newest first: contradictions
opened (the normative record is the `## Contradictions` section of the
named page), printed inconsistencies, identity and metadata problems,
bundle-fit suggestions, and questions left to the human. Not part of the
OKF wiki; maintained by the compiler at every chunk.

## Chunk 3 — 2019–2022: mesh optimization, curved-element stability, shock fitting, ML meshing (2026-11-08)

Sources (9): dobrev-2019, dobrev-2020, yu-2020, dobrev-2022, assonitis-2022,
elaouad-2022, chen-2022, cicchino-2022, nikl-2022. 29 of 56 ingested, 18
concept pages plus the registry, 1045 bibliography entries.

### Decisions for the human

1. **Archive file 025 is not the paper.**
   `2022_Crossref_ACM_Transactions_on_Graphics_Pietroni_Hex-Mesh_Generation_and_Processing_A_Survey.pdf`
   contains the VTK "File Formats" manual (19 pages), not Pietroni et al.,
   ACM Trans. Graph. 42(2) (2023). Not ingested. Replace the file with the
   survey (it would then be ingested in a later chunk) or remove it.
2. **Versions read.** dobrev-2019 (arXiv:1807.09807v1), dobrev-2020
   (arXiv:2001.11536v1), yu-2020 (arXiv:2001.04091v1), dobrev-2022
   (arXiv:2010.02166v1), nikl-2022 (arXiv:2110.11669v3), cicchino-2022
   (preprint submitted to JCP), assonitis-2022 and elaouad-2022 (HAL
   deposits); chen-2022 is the version of record.

### Contradictions

None opened.

### Bundle fit

- yu-2020 and nikl-2022 (MHD, constrained transport, de Rham spaces) touch
  `div-free-amr` and `fusion-mhd-simulation`; assonitis-2022 (shock
  fitting with cell blanking) touches `overset-grid-methods`; read here in
  this bundle's notation (D12).

## Chunk 2 — 2002–2019: metric identities, free-stream preservation, curved high-order meshes (2026-11-08)

Sources (10): visbal-2002, tang-2003, kopriva-2006, nonomura-2010, deng-2011,
xie-2013, deng-2013, johnen-2013, toulorge-2013, zhu-2019. 20 of 56
ingested, 14 concept pages plus the registry, 678 bibliography entries.

### Decisions for the human

1. **Versions read.** toulorge-2013 (preprint submitted to JCP), zhu-2019
   (arXiv:1811.06325v1); the others are versions of record.
2. **Bibliography repair of chunk 1.** Three ingested keys (thomas-1979,
   steger-1979, steger-1980) held other works of the same author and year
   cited by thompson-1982; they were rekeyed in this chunk (see the log).
   The chunk-1 commit therefore carries those wrong identities until the
   chunk-2 commit corrects them.
3. **Same-paper years.** thompson-1982's deposit dates Thomas & Lombard
   1980 (AIAA J. 17 is 1979); merged into thomas-1979 on DOI.

### Contradictions

None opened.

### Bundle fit

- visbal-2002, kopriva-2006, nonomura-2010, deng-2011, deng-2013, zhu-2019
  (metric identities, free-stream preservation) touch
  `curvilinear-metric-discretization`; nonomura-2010 and zhu-2019 (WENO,
  WCNS) touch `weno-teno`; read here in this bundle's notation (D12).

## Chunk 1 — 1966–2001: the founding papers (2026-11-08)

Sources (10): winslow-1966, gordon-1973, thompson-1974, thomas-1979,
steger-1979, steger-1980, brackbill-1982, thompson-1982, huang-1994,
knupp-2001. 10 of 56 ingested, 11 concept pages plus the registry.

### Decisions for the human

1. **Bundle name.** `structured-mesh-methods`, after the archive folder; the
   archive also holds unstructured high-order curvilinear meshing, mesh
   optimization and machine-learning meshing, all in scope (D33).
2. **Reading depth.** thompson-1982 (108 pages) is read in scope: Sections A,
   B, O and P in full, the rest by structure; its 346 deposited references
   are merged complete.
3. **Notation choices.** Time is $t$ in both frames and $\tau$ is reserved for
   the relaxation time of moving mesh PDEs; the Winslow coefficients are
   written as metric components ($g_{22}$, $g_{12}$, $g_{11}$).

### Contradictions

None opened.

### Identity and metadata

- Crossref misspells or truncates authors: thompson-1974 (C. Mastin →
  C.W. Mastin), thompson-1982 ("Wayne Mastin C." → C.W. Mastin),
  steger-1979 and brackbill-1982 (initials completed from page 1).
- thompson-1974 prints Winslow (1966) as J. Comp. Phys. **2** (1966), 149;
  the paper is in volume 1 (printed slip).

### Bundle fit

- thomas-1979 (geometric conservation law) and the conservative-metric part
  of thompson-1982 touch `curvilinear-metric-discretization`; read here in
  this bundle's notation (D12).
