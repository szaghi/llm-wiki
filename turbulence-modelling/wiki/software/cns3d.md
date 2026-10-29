---
type: Software
title: "CNS3D"
description: "CNS3D is the block-structured Godunov-type finite-volume code of Kokkinakis and Drikakis for compressible flow, with WENO reconstruction up to eleventh order and SSP Runge–Kutta time stepping; this page records its numerics, its low-Mach velocity corrections including NEHA, and its implicit-LES uses in a low-Mach channel and a shock/boundary-layer interaction."
status: established
aliases: [CNS3D, Compressible Navier–Stokes Solver in 3D]
tags: [software, implicit-les, compressible, numerical-dissipation, dns]
timestamp: 2026-10-29T05:08:00Z
---

# CNS3D

**CNS3D** ("Compressible Navier–Stokes Solver in three-dimensional (3D)")
is the in-house code of Kokkinakis, Drikakis and co-workers (University of
Nicosia). As described by [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md),
§III–§III A, it solves the Euler or Navier–Stokes equations by the
finite-volume Godunov-type (upwind) method on block-structured grids, with
several approximate Riemann solvers, in modern Fortran (Fortran 2018); it
includes "high-resolution methods of up to 11th order of accuracy in space
and 4th order of accuracy in time" and is used for RANS, implicit LES and
DNS. The bundle holds two papers that run the code,
[Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) and Kokkinakis &
Drikakis (2025b).

In the turbulent runs of both papers the code is used as
[implicit LES](/definitions/implicit-les.md): Kokkinakis & Drikakis
(2025b, §III) write that ILES "relies on FV discretization, Godunov-type
(upwind) methods, and the computational grid to remove the small scales",
the unresolved scales being modelled by the nonlinear dissipation of the
convective scheme; Kokkinakis et al. (2023) call the same approach
"coarse-grained simulation" (see
[numerical dissipation](/properties/numerical-dissipation.md)).

## Numerics

As printed in the two papers (Kokkinakis & Drikakis 2025b, §III A–C;
Kokkinakis et al. 2023, §III):

- **Reconstruction** of the primitive variables $(\rho,\boldsymbol u,p)$
  at cell interfaces by
  one-dimensional swept unidirectional stencils (dimension by dimension);
  the authors reject characteristic variables as more expensive and cite
  Zanotti & Dumbser against conservative ones (2025b, §III B).
- **WENO** up to eleventh order: an augmented eleventh-order scheme in
  Kokkinakis et al. (2023), a ninth-order scheme (W9) in Kokkinakis &
  Drikakis (2025b). Formulas and variants are on
  [WENO and hybrid schemes](/methods/weno-scheme.md).
- **Riemann solver**: HLLC of Toro, Spruce & Speares; in 2025b within the
  adaptive non-iterative Riemann solver (ANRS) of Toro, which replaces the
  primitive-variable star-pressure estimate by a two-rarefaction or
  two-shock estimate when the pressure ratio $p_{\max}/p_{\min}$ exceeds
  2 and the primitive-variable estimate falls outside
  $[p_{\min},p_{\max}]$ (§III C).
- **Time**: the five-stage fourth-order optimal strong-stability-preserving
  Runge–Kutta scheme of Spiteri & Ruuth (2025b, §III A); the
  2023 paper prints a five-stage SSP Runge–Kutta.
- **Inflow**: digital-filter synthetic turbulence for the boundary layer
  of Kokkinakis et al. (2023) (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

**The ninth-order WENO of 2025b** (§III B, Eqs. 5–15) adds four steps
around the Jiang–Shu weights: each stencil is normalized so that its
maximum is 1 and its minimum positive, which the authors find prevents
negative smoothness indicators and lowers dissipation; a relative
total-variation test switches to the linear weights when the ratio of the
largest to the smallest stencil total variation is below 2 and the
largest is below $0.2(r-1)$ ($r$ the stencil length, page-local; Taylor et
al. used 5 for the first threshold, "too high" here); the weights are
mapped (WENO-M, in the form of Feng et al.); and the order is reduced
stepwise W9→W7→W5→W3→MUSCL where the reconstructed face value of
density or pressure differs from the adjacent cell value by more than 70%
of that value (Eq. 15), a test "never met" in their quasi-incompressible
channel.

## Low-Mach velocity corrections

Kokkinakis & Drikakis (2025b, §IV–§V, Table I) compare corrections applied
after reconstruction and before the Riemann solver, which blend the left
and right reconstructed velocities $\boldsymbol u_L$, $\boldsymbol u_R$
toward their average with a factor $z=\min\big(1,\max(M_L,M_R)\big)$
(Thornber et al.'s "LM"; $M_L$, $M_R$ the local Mach numbers of the two
states). Density and pressure are left unchanged and the total energy is
recomputed with the limited velocities. The variants differ by which
velocity component is limited and which Mach number enters $z$:

| Variant | limited velocity | Mach number in $z$ |
|---|---|---|
| LM of Thornber et al. (as run by the authors in 2015) | normal and tangential | velocity magnitude |
| LM | normal and tangential | face-normal, $M_\perp=\lvert\boldsymbol u\cdot\boldsymbol n\rvert/c$ |
| LMn (Simmonds et al.) | normal | $M_\perp$ |
| LMt | tangential | tangential $M_\parallel$ |
| LMtn | tangential | $M_\perp$ |
| NEHA | normal and tangential | $M_\perp$ for the normal, $M_\parallel$ for the tangential part |

NEHA (Numerical Enhancement for Hyposonic Accuracy) is their
contribution: on hexahedral cells the normal velocity at one face is a
tangential velocity at the faces of the other directions, and separate
factors make the limiting consistent across the faces of an element
(§V, Fig. 3). The motivation is the dilemma they state: very-high-order
WENO is nearly central in smooth regions, so the original LM "makes the
overall numerical scheme excessively dispersive" (citing their 2015
work), yet without it even W9 fails at Mach numbers of order 0.01 on
coarse meshes (citing Tsoutsanis et al. 2015) (§I). The corrections, as
dissipation fixes, are discussed on
[numerical dissipation](/properties/numerical-dissipation.md) and
[WENO](/methods/weno-scheme.md).

**Channel results** (§VI–§VIII, Table II). Implicit LES of a weakly
compressible [channel](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau\simeq395$ and bulk Mach number 0.2, adiabatic walls, $64^3$ cells
(first cell centre at $y^+=1.5$) and $128^3$ for W9 alone, against the
DNS of Moser, Kim & Mansour ($Re_\tau=392.24$). Mean friction Reynolds
numbers (time r.m.s. in brackets): W9 $64^3$ 372.5 (4); LM with the
velocity-magnitude Mach number 367 (2.91); LM 402.2 (2.9); LMn 383 (3.3);
LMt 372 (3.5); LMtn 371.1 (3.2); NEHA 392 (2.96); W9 $128^3$ 391 (2.6).
The authors state that NEHA on $64^3$ brings $Re_\tau$ and the mean
velocity within 1% of the DNS against about 5.7% for W9 alone, removes
the "fuzzy" dispersed vortices that LM produces near mid-height, gives
skewness and flatness of $u'$ closest to the DNS near the wall, and is
more accurate than W9 on $128^3$ for $y^+<40$ (§VII–§VIII, Figs. 6–10).
LMt alone barely changes $Re_\tau$, but adding it to LMn moves it from 383
to 392. NEHA costs less than 10% over W9 with HLLC, LM about 5% (§VIII;
no timing table or hardware).

## Implicit LES of shock/boundary-layer interactions over deformed panels

Kokkinakis et al. (2023) run CNS3D with HLLC, the eleventh-order WENO and
digital-filter inflow on the Mach 1.94 oblique-shock interaction of the
AFRL Research Cell 19 over a planar panel and six static buckled shapes;
a four-mesh study selects 9.4 million cells ($\Delta x^+=717$,
$\Delta z^+=634$, $y^+=4.8$), and the wall-pressure mean and r.m.s.
change by about 10% with the deformation (§III–§IV; see
[shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

## Qualifications

- **The viscous-stress coefficient.** Both papers write
  $\boldsymbol\tau=\lambda_{\mathrm v}(\nabla\cdot\boldsymbol u)\mathbf I+\mu[\nabla\otimes\boldsymbol u+(\nabla\otimes\boldsymbol u)^{\mathsf T}]$
  ($\lambda_{\mathrm v}$ page-local). Kokkinakis et al. (2023, §III A)
  print $\lambda_{\mathrm v}=-4\mu/3$, "bulk viscosity … according to
  Stokes' hypothesis"; Kokkinakis & Drikakis (2025b, Eq. 4) print
  $\lambda_{\mathrm v}=-2\mu/3$, "the second viscosity coefficient the
  Stokes hypothesis gives". The Source page of Kokkinakis et al. (2023)
  lists its value under printed slips, with the trace of the printed
  tensor, $(3\lambda_{\mathrm v}+2\mu)\nabla\cdot\boldsymbol u$
  *(compiler check, not in the sources)*; that paper does not say which
  value the code uses. See [bulk viscosity](/definitions/bulk-viscosity.md).
- **Printed slips (Kokkinakis & Drikakis 2025b).** As printed,
  $\boldsymbol u^{LM}_L=(\boldsymbol u_s-\boldsymbol u_u)/2$ with
  $\boldsymbol u_s=\boldsymbol u_L+\boldsymbol u_R$ and
  $\boldsymbol u_u=z(\boldsymbol u_L-\boldsymbol u_R)$ (Eqs. 21–23), which
  gives $\boldsymbol u^{LM}_L=\tfrac12[(1-z)\boldsymbol u_L+(1+z)\boldsymbol u_R]$,
  so that $z=1$ swaps the two states instead of restoring them; the same
  sign pattern recurs in Eqs. 28–29, 31–32 and 35–36 *(compiler check, not
  in the sources)*. The mapped-weight formula (Eq. 11) prints
  $(\Omega+C)^{K+1}$ in the numerator, with which the stated choice
  $A=1$, $K=2$ does not leave the linear weight $C$ unchanged
  *(compiler check, not in the sources)*. The text gives $L_x=6\pi\delta$,
  the schematic of Fig. 5 $2\pi$; the averaging time is printed
  "$900\,u_b/\delta$", "just over 21 flow-throughs" based on $L_x$ and
  $u_b$, while a time of $900\,\delta/u_b$ over a flow-through time
  $6\pi\delta/u_b$ gives $900/(6\pi)\approx47.7$ *(compiler check, not in
  the sources)*; the
  initial noise is printed as 5% and as $s=10\%$; Eqs. (38) and (41) put a
  wall at $y=0$, Eqs. (43)–(44) the mid-height.
- **Evidence.** The variants are compared on one case (the channel) and
  one grid ($64^3$); NEHA is not run on $128^3$ (§VI–§VIII, Table II). The
  difference between LMn and NEHA, $392-383=9$, is three times the printed
  r.m.s. of about 3 *(compiler check, not in the sources)*.

# Citations

- [Kokkinakis & Drikakis (2025b)](/sources/kokkinakis-2025-b.md) — §I (low-Mach dilemma); §III–§III A (CNS3D: Fortran 2018, FV Godunov, orders, RANS/ILES/DNS, SSP-RK); §III B, Eqs. (5)–(15) (normalized RLTV mapped W9, order reduction); §III C, Eqs. (16)–(20) (HLLC with ANRS); §IV–§V, Eqs. (21)–(36), Table I, Fig. 3 (LM, LMn, LMt, LMtn, NEHA); §VI–§VIII, Table II, Figs. 4–10 (channel ILES, cost).
- [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) — §III (CNS3D with HLLC, eleventh-order WENO, SSP Runge–Kutta, digital-filter inflow, coarse-grained simulation); §III B–§IV (mesh study, panel-deformation results).
