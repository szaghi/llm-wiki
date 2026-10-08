---
type: Method
title: "Approximate Riemann solvers as building blocks of capturing schemes"
description: "The interface fluxes used by FV and alternative-FD WENO schemes in this corpus: Lax–Friedrichs/Rusanov, Roe, HLL and HLLC (with positivity-preserving wave speeds), HLLI/LLFI, the Riemann-solver-free MUSTA flux, and multidimensional HLL/LLF solvers for edge electric fields."
status: established
aliases: [Riemann solver, HLLC, HLL, MUSTA, FORCE, HLLI, Rusanov flux]
tags: [riemann-solver, numerical-flux, finite-volume, positivity]
timestamp: 2026-10-08T00:00:00Z
---

# Approximate Riemann solvers as building blocks

A capturing scheme evaluates $\hat f(u^-_{i+1/2}, u^+_{i+1/2})$ at each
interface. At first order this is a [monotone flux](/definitions/monotone-flux.md)
or an E-flux; at high order its choice still sets contact and shear
resolution and robustness. Finite-volume WENO and
[AFD-WENO](/methods/alternative-finite-difference-weno.md) accept any
solver. Classical FD-WENO needs a smooth flux splitting and so is
restricted to Lax–Friedrichs or Roe-type fluxes
([Balsara et al. (2025)](/sources/balsara-2025.md), §I).

* **Lax–Friedrichs / Rusanov / LLF**: centred average plus dissipation
  $\alpha$. It is robust and positivity-preserving for Euler under
  $\nu \le 1$ ([positivity preservation](/properties/positivity-preserving.md)),
  but it does not open the Riemann fan, so contacts smear.
  Titarev and Toro's WENO-HLLC and WENO-MUSTA are about twice as
  accurate on the same mesh as the Rusanov-based FV-WENO of Shi, Hu and
  Shu ([Titarev & Toro (2004)](/sources/titarev-2004.md), §5.1–5.2).
* **HLLC** (Toro, Spruce & Speares): a three-wave model with speeds
  $S_L \le S_M \le S_R$ and two star states. It contains all waves of the
  Euler Riemann fan, uses no linearization, and works for low density
  and sonic points without fixes ([Titarev & Toro (2004)](/sources/titarev-2004.md), §4.1).
  With the wave speeds of Batten et al. it resolves isolated shocks and
  contacts exactly. The star states stay in $\mathcal{G}$, so the
  first-order scheme is positivity-preserving under
  $\Delta t\,\Vert\vert u\vert + c\Vert_\infty/h \le 1$
  ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4, Remark 1). Being
  less dissipative, it can leave oscillations in velocity and internal
  energy near vacuum, where Lax–Friedrichs is cleaner (Examples 6, 8).
* **MUSTA** (Toro): opens the Riemann fan numerically by evolving the
  two-cell data with a first-order predictor flux — FORCE, whose
  viscosity is half the Lax–Friedrichs one — for $k$ stages
  ($k = 2$–$3$ approaches the exact Godunov flux; $k = 2$ is used). It
  needs no eigenstructure, so it suits systems whose characteristic
  information is unknown, at a cost comparable to approximate Riemann
  solvers. HLLC resolves slip lines better than MUSTA in the
  [double Mach reflection](/benchmarks/double-mach-reflection.md)
  ([Titarev & Toro (2004)](/sources/titarev-2004.md), §§4.2, 5.3).
* **Roe** for MHD shock tubes and **HLLC** for Euler in GP-WENO
  ([Reyes et al. (2018)](/sources/reyes-2018.md), §5).
* **HLLI / LLFI** (Dumbser–Balsara): HLL-type solvers that resolve
  intermediate (linearly degenerate) waves, used throughout AFD-WENO.
  A solver that keeps stationary contacts makes the whole AFD scheme do
  so, which helps well-balancing ([Balsara et al. (2025)](/sources/balsara-2025.md), §II).
* **Multidimensional HLL / LLF** solvers at mesh edges, for the
  electric field of the induction equation; they reduce to the 1D
  solver for one-dimensional variation
  ([constrained transport](/methods/constrained-transport.md);
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §3).

In 3D FV-WENO the flux integral over a face is approximated by a tensor
Gauss rule, so a Riemann solve is needed at each face Gauss point
([finite-volume reconstruction](/methods/finite-volume-reconstruction.md);
[Titarev & Toro (2004)](/sources/titarev-2004.md), §2).

**In one-step schemes (batch 4).**
* *Space–time averaged fluxes.* Freezing the HLL signal speeds at the
  face's space–time barycentre makes the flux linear in the
  predictor's states and fluxes, which are then averaged exactly
  instead of solving Riemann problems at every quadrature point
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §4.1; [ADER](/methods/ader.md)).
* *Linearized vs HLL for MHD.* In the decay of torsional Alfvén waves,
  a linearized MHD Riemann solver is much less dissipative than HLL.
  The gap narrows as the order rises, because better reconstruction
  shrinks the interface jumps, so cheaper solvers become acceptable at
  high order ([Balsara et al. (2009)](/sources/balsara-2009.md), §7.2).
* *Rusanov and Osher-type fluxes* (the path-integral flux of Dumbser and
  Toro, evaluated with Gauss–Legendre quadrature) serve the ADER-WENO
  and ADER-DG schemes on adaptive meshes ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.1; [Dumbser et al. (2014)](/sources/dumbser-2014.md), §2.3;
  [Zanotti et al. (2015)](/sources/zanotti-2015.md), §3.2).
* *Linear systems* use the exact Riemann solver,
  $\tfrac12\left(A + \vert A\vert\right)u^- + \tfrac12\left(A - \vert A\vert\right)u^+$,
  with $A$ the Jacobian along the face normal and
  $\vert A\vert = R\vert\Lambda\vert L$
  ([Dumbser & Käser (2007)](/sources/dumbser-2007.md), eqs. 30–31).

# Citations

1. [Titarev & Toro (2004)](/sources/titarev-2004.md), §§2, 4, 5.
2. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §§2.4, 3.
3. [Reyes et al. (2018)](/sources/reyes-2018.md), §5.
4. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §§I–II.
5. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §3.
6. [Balsara et al. (2009)](/sources/balsara-2009.md), §§4.1, 7.2.
7. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §2.1.
8. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §2.3.
9. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §3.2.
10. [Dumbser & Käser (2007)](/sources/dumbser-2007.md), §3.1.
