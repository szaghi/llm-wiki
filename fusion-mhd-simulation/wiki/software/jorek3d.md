---
type: Software
title: "JOREK3D"
description: "Stellarator extension of JOREK: a reduced MHD model built on the vacuum-field potential, an analytic Dommaschk representation of that field, and flux-surface-aligned Bézier grids whose geometry varies toroidally, initialized from GVEC and benchmarked against CASTOR3D on Wendelstein 7-A tearing (within 13.2 % in a β scan, 26.2 % in an η scan) and ballooning modes (within 6.4 %)."
status: established
aliases: [JOREK stellarator extension]
tags: [code, stellarator, reduced-mhd, finite-elements, spectral, equilibrium, tearing, ballooning, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# JOREK3D

JOREK3D is the version of [JOREK](/software/jorek.md) that runs
stellarator geometry. It implements the
[stellarator reduced MHD](/methods/stellarator-reduced-mhd.md) model of
Nikulsin et al. (2019, 2021) and generalizes the JOREK grid to a toroidally
varying geometry ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
Abstract, §I). [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) (§4.1) list
it among the 2021–2024 JOREK developments, next to a "virtual current" model
that approximates a stellarator in axisymmetric geometry, and record linear
benchmarks for classical stellarators and in the tokamak limit.
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§2.15, §3.8) list
stellarator reduced and full MHD and 3D grids with GVEC import as planned
work.

## Physics model

* **Field ansatz.** $\mathbf B=\nabla\chi+\nabla\psi\times\nabla\chi$, where
  $\chi$ is the magnetic scalar potential of the vacuum (coil) field and
  $\psi$ is the field-line-bending potential that becomes the poloidal flux
  per radian in the tokamak limit $\chi=F_0\phi$. The velocity is
  $\mathbf v\propto\nabla u\times\nabla\chi/|\nabla\chi|^2$, perpendicular to
  $\nabla\chi$, with $u$ a stream function that reduces to the tokamak one;
  the parallel velocity is set to zero in this paper (Nikulsin et al. 2022,
  §II, Eqs. 1–4).
* **Equations.** Vorticity (momentum projected with
  $\nabla\chi\cdot\nabla\times(|\nabla\chi|^{-2}\,\cdot\,)$), density,
  pressure and flux equations, with the current along $\nabla\chi$ and the
  vorticity kept as separate finite-element unknowns to avoid second
  derivatives in the weak form; viscosity, hyperviscosity and
  hyper-resistivity are added after the projection (§II, Eq. 3).
* **Equilibrium compatibility.** For the ordering parameter
  $\lambda_{\mathrm o}=L_\perp/L_\parallel$, a full-MHD equilibrium leaves a
  residual force in the reduced equations at $O(\lambda_{\mathrm o}^4)$,
  against $O(\lambda_{\mathrm o}^2)$ leading terms, even at zero $\beta$
  (§II, Eqs. 8–12). In the tokamak limit the model reduces to the JOREK
  tokamak model (§II).
* **Self-adjointness.** The linearized ideal reduced operator is self-adjoint,
  so ideal perturbations have real $\omega^2$ (App. B).

## Discretization and numerics

* **Vacuum field.** $\chi$ is represented analytically by
  [Dommaschk potentials](/methods/dommaschk-potentials.md), so $\nabla^2\chi=0$
  and $\nabla\cdot\mathbf B=0$ hold to machine precision (see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
  A finite-element $\chi$ would make the advective terms discontinuous,
  because the elements are only $G^1$ (§II, §III). The coefficients are fitted
  from the EXTENDER_P vacuum field by Legendre and Fourier projections that
  give triangular linear systems; for W7-A at $\beta=2.3\times10^{-3}\,\%$ the
  fit error is minimal (about $5\times10^{-11}$) at nine poloidal modes and
  rises (about $10^{-7}$ at twelve) by overfitting (§III, Fig. 1).
* **Grid.** Bicubic $G^1$ Bézier elements in the poloidal plane (see
  [Bézier–Hermite finite elements](/methods/bezier-finite-elements.md)) whose
  $(R,Z)$ control points now carry their own toroidal Fourier expansion. The
  geometry and the physics fields have separate harmonic counts and
  periodicities, so a full-torus physics run can sit on a five-periodic
  geometry. The grid is flux-surface aligned from GVEC; toroidal integrals
  are sums over 40 poloidal planes (App. A, Eqs. A1–A2).
* **Initial and boundary conditions.** The initial current along $\nabla\chi$
  comes from the GVEC field, $\Delta^*\psi_0$ is solved for $\psi_0$, and the
  non-homogeneous Dirichlet value of $\psi$ on the boundary comes from
  $\mathbf n\cdot\mathbf B=0$, solved by a Fourier–Galerkin method that
  excludes the $m=0$ kernel. The boundary is a perfectly conducting fixed wall
  (§IV, Eqs. 32–35).
* **Time stepping.** Linearized implicit steps; runs start with implicit Euler
  to damp the initial transient, then switch to Crank–Nicolson. An iterative
  solver is used; at low $\eta$ it needed hyper-resistivity to converge. The
  preconditioner is not specified (§V–VI, footnote 38). See
  [implicit time integration](/methods/implicit-time-integration.md).
* **Not ported.** The higher-continuity $G^n$ basis is not in JOREK3D (§II).
  No core counts, run times or GPU use are reported.

## Coupled codes

GVEC (fixed-boundary 3D equilibrium, B-spline radial basis, VMEC-like energy
minimization), NEMEC (initial equilibrium), EXTENDER_P (vacuum field), a
Python implementation of the Dommaschk fit, and CASTOR3D as the linear
full-MHD reference (Nikulsin et al. 2022, §I, §III, §VI). See
[three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
and [VMEC](/software/vmec.md). Hoelzl et al. (2024) (§4.1) report that
saturated external modes from VMEC-based studies and JOREK agree
qualitatively when the dominant $n$ is the same, but magnetic-energy spectra
and topology can differ through coupling to internal modes and non-ideal
effects.

## Verification on Wendelstein 7-A

Rotating-ellipse W7-A-like equilibria with five field periods, $R=1.99$ m,
toroidal flux 0.08 Wb and total toroidal current 17.5 kA (Nikulsin et al.
2022, §V, Eqs. 36–37).

* **Equilibrium preservation.** Four stable equilibria up to
  $\beta=0.022\,\%$, run five-periodically for about 7 ms, keep the magnetic
  axis fixed (offset from GVEC below about $10^{-4}$ m) and reproduce the GVEC
  flux surfaces before and after the run. An initial kinetic-energy transient
  of about $10^{-7}$ J decays to about $2\times10^{-11}$ J within about 0.02 ms
  (§V, Figs. 4–6).
* **Tearing mode $(m,n)=(2,1)$.** At $\eta=1.938\times10^{-6}\,\Omega$ m and
  $\beta=2.3\times10^{-5}$, $2.3\times10^{-4}$, $2.3\times10^{-3}\,\%$ the
  maximum deviation from CASTOR3D is 13.2 %; in the resistivity scan at
  $\beta=2.3\times10^{-5}\,\%$ ($\eta$ from $1.938\times10^{-7}$ to
  $1.938\times10^{-5}\,\Omega$ m) it is 26.2 % at the highest $\eta$
  (§VI, Fig. 8). Nonlinearly, the $n=1$ family ($n=1,4,6,9$) grows by
  toroidal-geometry coupling, $n=1$ drives $n=2$ at about 2 ms, the mode
  saturates at 3–3.5 ms, and a secondary $(3,2)$ island chain appears
  (Figs. 9–10). See [tearing mode](/definitions/tearing-mode.md).
* **Ballooning modes.** At $\beta=0.11\,\%$ and $0.21\,\%$ with $n=0,5,10$,
  the maximum deviation from CASTOR3D is 6.4 %, the other three cases below
  3 % (§VII, Fig. 12). See [ballooning mode](/definitions/ballooning-mode.md).
* **Convergence.** Halving $\Delta t$ or hyperviscosity, or doubling
  resolution, harmonics or planes, changes the growth rate by less than 1.5 %
  (§VI).

## Limitations

* The parallel velocity is dropped, which the authors hold responsible for
  the larger tearing deviation (§VI).
* With $N_{\mathrm{tor}}=5$, field lines drift off flux surfaces and
  anisotropic transport is not properly modelled (§VI).
* Validity at $\beta\sim3$–5 % "remains to be seen", and the model family
  "cannot accurately reproduce kink modes at higher β" (§VIII). The claim
  that it can already handle W7-X and LHD carries no evidence in the paper
  (§VIII).
* Version caveat: a Publisher's Note (Phys. Plasmas 29:099902) postdates the
  arXiv v3 read for this page.

## Contradictions

* **JOREK3D versus CASTOR3D growth rates.** *Open (qualified).*
  Nikulsin et al. (2022) report JOREK3D growth rates systematically above
  CASTOR3D: up to 13.2 % in the $\beta$ scan and 26.2 % in the $\eta$ scan
  for the $(2,1)$ tearing mode (§VI, Fig. 8), and up to 6.4 % for ballooning
  modes (§VII, Fig. 12). They attribute the tearing gap to the neglect of
  $v_\parallel$, which is large in the resistive layer that widens with
  $\eta$ (an analogy is the overestimate of quasi-interchange growth rates by
  $\sqrt{1+2q^2}$, $q$ at the mode surface, without $v_\parallel$), and most of the ballooning gap to
  spectral blocking: adding $n=15$ lowers the JOREK3D $n=10$ growth rate by
  5–6 % but changes CASTOR3D's by less than 0.003 %. The attribution is the
  authors'; a JOREK3D run with $v_\parallel$ retained would test the first
  explanation.

# Citations

1. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §§I–VIII, App. A–B, Figs. 1, 4–12.
2. [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §4.1.
3. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.15, §3.8.
