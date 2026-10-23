---
type: Software
title: "FLEXI"
description: "FLEXI is the open-source (GNU GPL v3.0) DGSEM framework of Krais et al. for hyperbolic–parabolic conservation laws on curved hexahedra; Mossier et al. extend its a priori finite-volume subcell shock capturing to p-adaptation, Schwarz et al. compare entropy-stable Gauss–Lobatto and Gauss collocation in it for turbulent LES, and other authors position it."
status: established
aliases: [Flexi, os-FLEXI, hp-FLEXI]
tags: [software, dg, limiting]
timestamp: 2026-10-23T15:06:00Z
---

# FLEXI

FLEXI is an open-source framework for the [DGSEM](/methods/dgsem.md) on
curved hexahedral meshes, distributed under the GNU GPL v3.0 at
www.flexi-project.org, with the Krais et al. framework paper as its
reference ([Mossier, Beck & Munz (2022)](/sources/mossier-2022.md), p. 1
footnote and §1). It is a 3D code: the 1D and 2D runs of Mossier et al.
use one element layer in the other directions, and their degree-of-freedom
counts are 3D counts, e.g. $216=6^3$ per element for $N=5$ (§8).

## Discretization as reported

As Mossier et al. describe the open-source baseline (§3, §4, §6):

- **DGSEM on Legendre–Gauss nodes.** The solution and the flux are
  tensor-product Lagrange interpolants of degree $N$ at the Gauss nodes,
  which also serve as quadrature (collocation), on elements mapped from
  $[-1,1]^3$; the transformed law is
  $J\partial_tu+\nabla_\xi\cdot\tilde f=0$ with contravariant fluxes
  $\tilde f^{(d)}=Ja^{(d)}\cdot f$ (Eqs. (5)–(13)). This is the Gauss
  variant of the DGSEM, not the LGL variant of most
  [Trixi.jl](/software/trixi-jl.md) and [FLUXO](/software/fluxo.md) runs
  of the bundle; Schwarz et al. (2025) run both node sets in FLEXI (below).
- **Time stepping.** An explicit four-stage Runge–Kutta method, with the
  step $\Delta t=\nu\,\alpha_{\mathrm{RK}}(N)\,\Delta x/\big((2N+1)a\big)$
  (CFL number $\nu$, maximum signal speed $a$, page-local Runge–Kutta
  factor $\alpha_{\mathrm{RK}}$; Eq. (18)).
- **Shock capturing.** The a priori finite-volume subcell scheme of
  Sonntag and Munz, as recalled: a troubled element is switched as a whole
  to a second-order TVD finite-volume scheme (piecewise-linear
  reconstruction with the minmod limiter) on $N+1$ equidistant subcells
  per direction, so that DG and finite-volume elements have the same
  number of degrees of freedom and share one array (§4, §6;
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
- **Data structures.** Static arrays of size variables × elements ×
  $(N+1)^d$ for volume data and variables × sides × $(N+1)^{d-1}$ for
  face data, which suit tensor operations and a fixed global degree
  (§6).

Mossier et al. deliberately do not use a split-form (de-aliased) DG
volume term, to isolate the stabilizing effect of the subcells (§9).

## The p-adaptive extension

Mossier et al. extend FLEXI ("hp-FLEXI" against "os-FLEXI", §8.3) with an
element-local degree $N\in[N_{\min},N_{\max}]$, finite-volume subcells of
any number $N_{\mathrm{FV}}$ per direction (page-local) and a modal-decay
indicator that drives both decisions; the method is on
[h- and hp-adaptation](/methods/hp-adaptation.md). To keep the static
arrays, every element carries storage for every degree and for the
subcells, and metric terms are precomputed for all of them, so nothing is
reallocated at run time (§6, §7.1). The single-core cost per degree of
freedom and time step (their performance index, wall time × cores per
DOF per time step) is nearly that of the open-source code for $N>4$ and
about 15 % higher at $N=2$ with a uniform degree, at most about 15 %
higher for a half–half split of degrees and up to 80 % higher for a
checkerboard, on an Intel Xeon Gold 6140 with GNU 8.3.0 and -O3 (§8.3,
Fig. 7). Memory grows by about 20 % (p-adaptive) and a factor of 4 with
$N_{\mathrm{FV}}=2N_{\max}+1$ (double Mach reflection: 4.9, 5.9 and 19.0
GB; Table 3). Load balancing for parallel runs is "work in progress"
(§9). Free streams are preserved on a curved mesh mixing DG elements of
degrees 2 and 7 with finite-volume elements, with $L^2$ errors from
$7.8\times10^{-16}$ to $3.4\times10^{-15}$ (§8.1, Table 1) ([free-stream preservation](/properties/free-stream-preservation.md)).

## Entropy-stable collocation on both node sets

[Schwarz et al. (2025)](/sources/schwarz-2025.md) (arXiv v1 read)
implement in FLEXI the entropy-stable [DGSEM](/methods/dgsem.md) on
Legendre–Gauss–Lobatto nodes (ESDGSEM-GL: diagonal-norm
[summation-by-parts](/operators/summation-by-parts-operator.md) operator and
[flux differencing](/methods/flux-differencing.md)) and on Legendre–Gauss
nodes (ESDGSEM-G: Chan's hybridized generalized SBP operator with
[entropy projection](/methods/entropy-projection.md) of the face states),
and compare them on compressible turbulence (§3, Eqs. (20)–(25); GALÆXI is
cited as a companion code). Their FLEXI configuration (§3.1–3.5):

- metric terms in Kopriva's conservative curl form, so that the discrete
  metric identities hold ([free-stream preservation](/properties/free-stream-preservation.md));
- [BR1 lifting](/methods/bassi-rebay-viscous-discretization.md) of the
  primitive-variable gradients for the viscous fluxes;
- the [Roe flux](/methods/roe-riemann-solver.md) with the Harten–Hyman
  entropy fix at interfaces ([Lax–Friedrichs](/methods/lax-friedrichs-flux.md)
  for the low-Mach Taylor–Green vortex) and Chandrashekar's
  entropy-conservative and kinetic-energy-preserving volume flux
  ([entropy-conservative fluxes](/methods/entropy-conservative-flux.md));
- Carpenter & Kennedy's explicit low-storage five-stage fourth-order
  Runge–Kutta method at CFL 0.9;
- for the supersonic Taylor–Green vortex only, convex blending of the DG
  volume operator with a second-order TVD finite-volume subcell operator on
  the nodes, driven by a modal indicator on $\rho p$ with blending bounds
  $(0.01,0.04)$ ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
  This differs from Mossier et al.'s element-wise switch above.

Both node sets reach order $N+1$ on a manufactured solution on curved
meshes, Gauss–Lobatto being less accurate at equal resolution (§4.1). At
fixed $N$ the Gauss variant costs about twice as much, which the authors
attribute to the entropy projection and the additional surface fluxes:
27 890 against 62 080 CPU hours for the compressible diffuser LES (§4.4).
Because Gauss–Lobatto needs $N=7$ where Gauss reaches comparable accuracy at
$N=5$, with a smaller time step at higher $N$, they conclude that Gauss
collocation is the more efficient choice per accuracy (§4.3–4.4, §5); no
CPU time is printed for the Gauss–Lobatto run at $N=7$. The accuracy
comparisons are on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
and a three-dimensional diffuser LES.

## Relation to other DGSEM codes

[Ranocha et al. (2023)](/sources/ranocha-2023.md) state that the
performance techniques of their Trixi.jl and FLUXO study, among them
precomputation, compile-time options and SIMD-friendly volume terms, "can
be applied successfully to other (open or closed source) DG codes such as
FLEXI" (§1). They do not test FLEXI. Their performance index is the time
per right-hand-side evaluation per node (Def. 4.1), while Mossier et al.'s
is wall time per degree of freedom and time step; the two numbers are not
comparable *(compiler check, not in the sources)*.

[Deng, Jiang & Yan (2025)](/sources/deng-2025.md) cite FLEXI (Krais et al.)
among the hard-switching a priori DG/finite-volume subcell methods and
group Mossier et al.'s approach with those that project DG data onto
equidistant subcells, which they argue changes the data structure, breaks
compactness and adds cost and load imbalance, against their own non-uniform
subcells sized by the Gauss weights (§1, §3.2). Their double-Mach-reflection
troubled-element distributions are "comparable" to Mossier et al.'s (§4.5).
These are characterizations by other authors, not measurements of FLEXI.

## Qualifications

- What FLEXI contains is reported here through the sources that use or
  name it; none describes the code systematically. Mossier et al. and
  Schwarz et al. extend or configure it and cite the framework paper
  (Krais et al.); Ranocha et al. and Deng et al. only name it.
- Schwarz et al.'s efficiency conclusion is inferred from accuracy at
  different $N$ and the time-step argument, not from a measured cost of the
  Gauss–Lobatto run at $N=7$; their cost ratio (2.23 for the diffuser) is a
  single-code measurement *(compiler check, not in the sources:
  $62\,080/27\,890=2.23$)*.
- The degree counts per element in Mossier et al. count nodes, not
  nodes × variables *(compiler check, not in the sources: $216=(N+1)^3$
  for $N=5$)*.

# Citations

- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — p. 1, §1, §3 Eqs. (5)–(18), §4, §6, §7.1, §8.1, §8.3 Fig. 7, §8.6 Table 3, §9.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §1, Def. 4.1.
- [Schwarz et al. (2025)](/sources/schwarz-2025.md) — arXiv v1: §3.1–3.5, Eqs. (9)–(26); §4.1–4.4, Table 1; §5.
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §1, §3.2, §4.5.
