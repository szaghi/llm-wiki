---
type: Software
title: "PLUTO (astrophysical gas-dynamics and MHD code)"
description: "Multi-physics finite-volume and finite-difference code for classical and relativistic MHD in which two high-order capturing schemes of this corpus are implemented: cell-centred finite-difference GLM-MHD with WENO+3 and LimO3 (third order) and WENO-Z and MP5 (fifth order), and fourth-order finite volume with pointwise reconstruction and upwind constrained transport."
status: established
aliases: [PLUTO, PLUTO-AMR]
tags: [software, mhd, finite-volume, finite-difference, constrained-transport]
timestamp: 2026-10-13T00:00:00Z
---

# PLUTO

The sources here use PLUTO as the host code of the schemes they present.
They do not describe the code itself.
* **Finite-difference GLM-MHD.** Third- and fifth-order conservative
  finite differences with all variables cell-centred and
  [GLM cleaning](/methods/hyperbolic-divergence-cleaning.md). Four
  reconstructions (WENO+3, LimO3, WENO-Z, MP5) are compared under a global
  Lax–Friedrichs splitting in characteristic fields
  ([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §§3–4).
* **Fourth-order finite volume** for classical and special relativistic
  MHD. Point values come from averages by the $\frac{h^2}{24}$
  correction, MP5 or WENO-Z interpolate them to faces, and one Riemann
  problem per face is solved. Upwind constrained transport has a
  fourth-order edge correction, and a discontinuity detector drives order
  reduction ([Berta et al. (2024)](/sources/berta-2024.md), §§3–5;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md);
  [constrained transport](/methods/constrained-transport.md)).
* Its adaptive version, PLUTO-AMR, is listed among the method-of-lines
  Runge–Kutta AMR codes ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §3;
  [high-order AMR](/methods/high-order-amr.md)).

**Later uses (batch 7).**
* PLUTO hosts the second-order CTU-GLM, CTU-EGLM, eight-wave and CTU-CT
  schemes compared in [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md) (§4). It sets the GLM damping length
  to the finest cell, so under AMR the damping time changes with the
  finest level ([Tomida et al. (2026)](/sources/tomida-2026.md), §2.3.3).

# Citations

1. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §§3–4 (arXiv v2).
2. [Berta et al. (2024)](/sources/berta-2024.md), §§3–5 (arXiv v4).
3. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §3.
4. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §4.
5. [Tomida et al. (2026)](/sources/tomida-2026.md), §2.3.3.
