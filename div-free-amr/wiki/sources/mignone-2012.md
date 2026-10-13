---
type: Source
title: "Mignone et al. (2012) — The PLUTO code for adaptive mesh computations in astrophysical fluid dynamics"
description: "PLUTO-Chombo AMR for MHD/RMHD: cell-centered CTU with GLM cleaning, so the magnetic field needs no AMR machinery beyond standard conservative interpolation and refluxing."
resource: "doi:10.1088/0067-0049/198/1/7"
source_kind: paper
authors: [Mignone A., Zanni C., Tzeferacos P., van Straalen B., Colella P., Bodo G.]
year: 2012
venue: "Astrophys. J. Suppl. Ser. 198:7"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2012-ApJS-Mignone-1010880067004919817.pdf"
tags: [glm, amr, ctu, collocation, production-code, relativistic, mhd]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

The AMR release of PLUTO (classical and special-relativistic MHD) on the
Chombo block-structured infrastructure: conservative finite volume,
**everything cell-centered**, unsplit CTU with PPM/WENO/linear tracing
(including a characteristic-decomposition-free variant), and the
solenoidal condition enforced by
[mixed GLM cleaning](/methods/glm-divergence-cleaning.md). Level
coupling is the *standard* conservative trio — coarse-to-fine conservative
interpolation for ghosts and new cells, fine-to-coarse averaging,
[refluxing](/methods/refluxing.md) at synchronization — applied uniformly
to all conserved variables, magnetic field included. Novelties beyond
MHD-AMR: unsplit non-ideal terms (viscosity, resistivity, anisotropic
conduction) and stiff point-local sources exploiting time adaptivity.

# Key claims

1. **The collocated+GLM payoff realized on AMR**: because $\mathbf{B}$ is
   a cell-centered conserved variable and the constraint is *controlled*
   (not held) by the cleaning field, the magnetic field requires **no
   dedicated AMR transfer operators** — no face restriction, no $P_D$, no
   EMF correction; the hydro AMR machinery is the whole story. This is
   the production cash-out of the architectural argument in
   [Mignone & Tzeferacos (2010)](/sources/mignone-tzeferacos-2010.md).
2. **Subcycled hierarchy discipline**: per-level $\Delta t^\ell$, average
   down + reflux at synchronization (their eqs. 45–49, Figs. 1, 5) — the
   Berger–Colella pattern, refinement ratio 2 typical.
3. **Scheme flexibility as a feature**: reconstruction (linear/PPM/WENO)
   and Riemann solvers interchangeable over the same AMR substrate,
   RMHD included — breadth that staggered-CT AMR implementations must
   engineer per-scheme.

# Notation map

| Mignone et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| cell-centered $\mathbf{B}$, $\psi$ | $B_h$ cell-collocated, $\psi_h$ | conserved-variable treatment |
| conservative interpolation (45) | $P$ (plain, conservative) | ghosts + new cells |
| averaging (47) + refluxing (48–49) | $R$ + flux correction | all variables uniformly |

# Pages created or updated

* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md) (AMR realization: no dedicated magnetic transfer operators).

# Citations

1. `~/papers/mosaic/div-free-amr/2012-ApJS-Mignone-1010880067004919817.pdf` (doi:10.1088/0067-0049/198/1/7) — text extraction, 31 pp.
