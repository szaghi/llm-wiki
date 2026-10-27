---
type: Software
title: "COOLFluiD"
description: "COOLFluiD is an open-source C++ component-based multi-physics platform; this page records the implicit high-order flux-reconstruction RANS solver built in it for the log-ω SST and Langtry–Menter transition models, with its semi-analytical Jacobian, source-term linearization, wall treatment, verification and per-degree-of-freedom cost scaling."
status: established
aliases: [COOLFluiD platform, Computational Object-Oriented Library for Fluid Dynamics]
tags: [software, flux-reconstruction, rans, transition]
timestamp: 2026-10-27T05:46:00Z
---

# COOLFluiD

**COOLFluiD** is an open-source, component-based multi-physics platform
written in C++. [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md)
(KU Leuven, von Karman Institute, ESA/ESTEC), §3.1, Fig. 4, list its
discretizations as finite volume, residual distribution, finite element,
spectral finite difference and
[flux reconstruction](/methods/flux-reconstruction.md) (FR), with interfaces
to the PETSc and Trilinos linear-algebra libraries and physics modules for
aerothermochemistry, MHD and multi-fluid flows, Monte Carlo radiation and
$r$-adaptation. It is the only bundle source on the code. Their paper adds
to it a high-order, fully implicit FR solver for compressible RANS with
laminar–turbulent transition. The authors call it, to their knowledge, the first FR
solver for RANS with transition, earlier FR-RANS work having been limited
to the [Spalart–Allmaras](/methods/spalart-allmaras-model.md) and Wilcox
[$k$-$\omega$](/methods/k-omega-model.md) models (Abstract, §1).

## The FR-RANS modules

Vandenhoeck et al. (2022, §3.1) add two kinds of modules on top of the
core FR solver of earlier group work:

- **physics modules** for RANS with the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
  in its 2003 form and with the Langtry–Menter
  [local-correlation-based transition model](/methods/local-correlation-based-transition-model.md)
  (SST-2003-LM2009), inheriting from the Navier–Stokes module;
- an **FR-RANS numerical module** holding the boundary conditions and the
  source terms of these models.

**Logarithmic $\omega$.** The SST model is rewritten to transport
$\ln\omega$ instead of $\omega$, an idea the authors take from Bassi et al.
(2005, as recalled) for discontinuous Galerkin with the Wilcox model and
extend to SST-2003, which adds a transformed cross-diffusion term and a
term in $(\nu+\sigma_\omega\nu_t)\lvert\nabla\ln\omega\rvert^2$ from the
diffusion (§1.1, Eqs. 5, 17–18). They report that with the original
variable the steep near-wall rise of $\omega$ made the high-order solver
unstable and did not keep $\omega$ positive, and that $\ln\omega$, whose
near-wall distribution is much smoother, removes the instability and
guarantees $\omega>0$ (§1.1; no figure). The formulation and constants are
on the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) page.

**Numerics** (§2, §3.2, Eqs. 47–63): FR in Huynh's form on tensor-product
elements with $(N+1)^d$ Gauss–Legendre solution points, the
Vincent–Castonguay–Jameson–Huynh (VCJH) correction functions (the
spectral-difference member $c_{SD}$ by default), BR2 for the diffusive
interface flux and AUSM$^+$-up for the convective one; backward Euler in
time, linearized by Newton's method, the linear system solved by GMRES in
PETSc, with the time step set by a user CFL number.

## Implicit Jacobian

**Semi-analytical FR Jacobian** (the authors' contribution, §3.2.2,
Eqs. 66–87). The FR operator is differentiated analytically, and only the
derivatives of the physical flux with respect to the state and its
gradient are taken by finite differences, which the authors justify by
their small cost compared with the FR part. The Jacobian splits into six
terms: element and face contributions, each with respect to the state and
to the gradient, the face ones split into interface and extrapolated
discontinuous parts (Eq. 87). Because the corrected gradient couples an
element with its $2d$ face neighbours, the gradient at one solution point
depends on $3d(N+1)$ states (page-local count, the source's $N_{s,q}$). A
fully numerical (finite-difference) Jacobian is costly and does not scale
with order, since the whole FR procedure must be repeated for every
perturbed variable (§3.2.1, Eqs. 64–65, perturbation $10^{-7}$ relative to
the local or free-stream value).

**Source-term Jacobian** (§3.2.3, Figs. 6–7). On the ERCOFTAC T3A plate at
$N=2$, with the CFL raised exponentially from 10 to 1250, the authors
compare a full analytical source Jacobian (limiters ignored, blending
functions frozen), the approximate treatment of Merci et al. (as recalled:
only the negative part implicit, with or without a source-based time-step
limit), a **decoupled** treatment (no derivatives with respect to the
mean-flow variables, SST and transition blocks separated), a diagonal one,
none, and a fully numerical Jacobian. All analytical variants run at CFL
1250, while without a source Jacobian the CFL had to be cut to 500. The
fully numerical Jacobian stagnates, the negative-part schemes first speed
up convergence and then stagnate, full and diagonal perform alike, and the
decoupled treatment converges slightly faster and is retained. They
find, in agreement with Merci et al., that the source-based time-step limit
is less severe than the convective/diffusive one. At $N=2$ and CFL 1250 a
residual level of $-13$ (as printed) takes about
700–1000 iterations, and $N=4$ at CFL 200 started from the $N=3$ solution
about 500.

## Boundary conditions

Boundary values are imposed by ghost states at the boundary flux points
(§3.3, Eqs. 88–90). At a no-slip wall $k=0$, zero normal gradients of the
intermittency and of the transported onset Reynolds number, and
$\ln\omega=\ln\big(60\nu/(\beta_1d_1^2)\big)$, where $d_1$ is the wall
distance of the first solution point: the exact wall value would be
infinite, so the wall value depends on order and mesh. At the inlet $k$
follows from $Tu_\infty$ and $\omega$ from the free-stream viscosity ratio,
with values adjusted for the decay between inlet and leading edge. The wall
distance $d$ inside the models is the distance from a solution point to the
nearest wall flux point projected on the wall normal, which the authors
call inexact (an Eikonal solve would be better) but adequate for flat
plates (§1.1).

## Verification

- **Wieghardt flat plate** (§4.1, Figs. 9–10; see
  [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)):
  $Re_L=1.03\times10^7$, SST only, $N=0$–4 on a 784-element mesh
  (first-element $y_1^+\simeq10$) and $N=5$–6 on a 392-element mesh
  ($y_1^+\simeq25$). Higher orders converge to one solution, agreeing with
  experiment, Spalding's [law of the wall](/definitions/law-of-the-wall.md)
  and a DG reference at $N=2$ on 8800 elements; the $N=4$ $C_f$ is
  considerably closer to experiment than the lower orders and the DG
  reference. The authors state that accurate results at $y_1^+\simeq25$
  without [wall functions](/methods/rans-wall-function.md) exceed what
  state-of-the-art second-order finite-volume solvers achieve without
  them; no finite-volume run is shown.
- **ERCOFTAC T3A, T3B, T3A$-$** (§4.2, Figs. 12–16; see
  [ERCOFTAC T3 plates](/benchmarks/ercoftac-t3-flat-plate.md)): one
  143-element mesh, $N=0$–5 (6 for T3A). $N=0$ shows no transition, the two
  highest orders coincide, T3A and T3A$-$ match the Langtry–Menter
  finite-volume reference on about 39,000 elements, and T3B lies closer to
  experiment than that reference. T3A $C_f$ at $N=5$ is nearly identical
  for the VCJH parameters $c_{SD}$, $c_{DG}$ and $c_{g2}$ (Fig. 14).

## Cost scaling with order

Vandenhoeck et al. (2022, §4.3) argue that on tensor elements each of the
$O(N^d)$ solution points of an element couples to $O(N)$ others, so the
implicit FR Jacobian costs $O(N^{d+1})$ per element, and with diffusive
fluxes each entry costs an extra $O(N)$ through the corrected gradient:
the wall time per degree of freedom can at best grow as $O(N^2)$,
independent of dimension. Single-thread timings (Intel Core i7-9700K,
3.6 GHz, 16 GB) of wall time per degree of freedom per iteration follow
this scaling, slightly worse at the higher orders, and adding the two
transition equations raises the wall time without changing its order
(Fig. 17).

## Planned extensions

GPU porting, three-dimensional transitional cases and the $\gamma$-$\alpha$
transition model for high-speed flows with shock capturing (§5).

## Qualifications

- Vandenhoeck et al. print "$_fu^n_j$ and $_fu^n_j$" between Eqs. (82) and
  (83), where the second is the current-element value $_fu^c_j$ of their
  Eq. (82); and in §3.2.2 they write the derivatives of $F^D$ where, by
  context, those of the interface flux $F^I$ are meant.
- They give the free-stream turbulence intensity of the Wieghardt plate as
  "$10^{-2}$" (§4.1), having defined $Tu_\infty$ in percent (§3.3.2), so the
  unit of that value is ambiguous.
- The letter $P$ denotes both the production of $k$ and the polynomial
  degree in the source; on this page the degree is $N$.

# Citations

- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — Abstract, §1 (priority claim); §1.1, Eqs. (1)–(20), Table 1 (log-$\omega$ SST, wall distance); §2, Eqs. (47)–(61) (FR); §3.1, Fig. 4 (COOLFluiD, new modules); §3.2, Eqs. (62)–(87), Figs. 5–7 (implicit scheme, numerical and semi-analytical Jacobians, source-term Jacobians); §3.3, Eqs. (88)–(90) (boundary conditions); §4.1–4.2, Figs. 9–16 (Wieghardt plate, T3 cases); §4.3, Fig. 17 (cost scaling); §5.
