---
type: Software
title: "OpenFOAM (overset)"
description: "The open-source finite-volume library OpenFOAM as used with overset meshes in the sources: a cell-centred pressure-correction solver with overset interpolation, whose lower/upper/diagonal matrix storage cannot hold the dense row of an implicit global conservation constraint."
status: established
aliases: [OpenFOAM overset]
tags: [software, finite-volume, incompressible, overset-grid]
timestamp: 2026-11-02T15:27:00Z
---

# OpenFOAM (overset)

OpenFOAM is an open-source C++ finite-volume library. Two sources run overset computations in it; neither names the version or the overset module.

- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) implement their implicit global mass-conservation constraint for the pressure equation ([conservative overset interface](/methods/conservative-overset-interface.md)) in an OpenFOAM pressure-correction solver with inverse-distance, polynomial and RBF [interpolation](/methods/inter-grid-interpolation.md). The constraint row couples one flux-balance cell to all receptors of all meshes; OpenFOAM's lower/upper/diagonal addressing cannot store it, so the system is assembled in compressed row storage and solved with BiCGStab from the external ITSOL library (§3). The dense row leaves the iteration count essentially unchanged (Table 4).
- [Wang et al. (2021)](/sources/wang-2021.md) run a rotating propeller grid inside a stationary background with PISO, second-order upwind convection and second-order backward time stepping, recomputing the interpolation coefficients every $1^\circ$ of rotation with 8-point trilinear interpolation ([moving overset grids](/methods/moving-overset-grid.md)).

- [Devlin et al. (2023)](/sources/devlin-2023.md) implement their interpolation-free DFVF-overset scheme as a preprocessing utility for OpenFOAM (foam-extend 4.1), which lets existing finite-volume solvers run on overset grids monolithically ([interpolation-free overset coupling](/methods/interpolation-free-overset-coupling.md), Conclusions).

# Citations

- [Chandar & Sitaraman (2022)](/sources/chandar-2022.md) — §3, §3.7.7, Table 4.
- [Wang et al. (2021)](/sources/wang-2021.md) — §2, Eq. (10).
- [Devlin et al. (2023)](/sources/devlin-2023.md) — Conclusions.
