---
type: Source
title: "Couch, Carlson, Pajkos, O'Shea, Dubey & Klosterman (2021) — Towards performance portability in the Spark astrophysical MHD solver in the Flash-X simulation framework"
description: "Performance-portability paper for Flash-X's Spark MHD solver (fifth-order WENO, HLLD, SSP-RK, cell-centred divergence control): pencil data layout, key-dictionary program synthesis for CPU/GPU, and AMR flux registers holding Runge-Kutta stage combinations."
resource: "doi:10.1016/j.parco.2021.102830"
source_kind: paper
authors: [Couch S.M., Carlson J., Pajkos M., O'Shea B.W., Dubey A., Klosterman T.]
year: 2021
venue: "Parallel Comput. 108:102830"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2021-ParCo-Couch-101016jparco2021102830.pdf"
tags: [production-code, amr, performance-portability, gpu, refluxing, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Spark is the MHD solver of Flash-X, written for core-collapse supernova
simulations in the ExaStar project. It uses:
* fifth-order WENO reconstruction of primitive variables, with Borges
  smoothness indicators;
* HLLD fluxes;
* an unsplit update with second- or third-order SSP Runge–Kutta;
* AMR through Paramesh or AMReX.

The abstract describes "an efficient cell-centered approach to satisfying
the divergence-free condition". **The paper does not say which method**,
and the bundle does not infer it; Spark's algorithm is in a companion
paper, cited as in press. The paper's subject is performance portability:
cache-friendly pencil layouts, and a key-dictionary program-synthesis tool
that assembles CPU and GPU variants from shared code fragments.

For this bundle the relevant content is the AMR flux register under
multistage integration, merged into [refluxing](/methods/refluxing.md).
This paper is in tier C of the ingestion list (context: codes). The user
asked for it to be added.

# Key claims

1. **Algorithm outline.** Reconstruct, solve Riemann problems dimension by
   dimension, then update unsplit with flux divergences. This is repeated
   at each Runge–Kutta stage.
2. **AMR fluxes.** Coarse–fine fluxes must be reconciled. In AMReX, a flux
   register between each pair of levels can store a linear combination of
   the Runge–Kutta stage fluxes, with the correction applied at the end of
   the step. Paramesh advances all levels at once and needs a different
   correction path.
3. **Cost against CT.** On a single-block 3D magnetized shock tube, Spark
   is nearly four times faster than Flash's unsplit staggered-mesh CT
   solver, although Spark takes two RK stages per step. The authors
   caution that RK's tighter time-step limit makes whole-application
   comparisons unreliable. PLM instead of WENO doubles speed.
4. **Portability.** Program synthesis from keyed fragments avoids
   duplicating the solver per platform. The paper reports CPU
   single-thread and OpenMP scaling and a GPU port of the flux step.

# Notation map

| Couch et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U$, $\mathbf F_i$ | conserved state, fluxes | |
| flux register | refluxing register at a coarse–fine interface | |
| USM | unsplit staggered-mesh CT (Lee 2013) | holds $D_h^{\mathrm{f}} B_h = 0$ |

# Pages created or updated

* Updated [Refluxing](/methods/refluxing.md): flux registers under multistage Runge–Kutta, with a compiler reading on stage coupling.

# Citations

1. `~/papers/mosaic/div-free-amr/2021-ParCo-Couch-101016jparco2021102830.pdf` (doi:10.1016/j.parco.2021.102830): text extraction, all pages including the reference list (22 entries). Performance figures were read from their captions and the text only.
