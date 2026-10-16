---
type: Software
title: "JOREK3D"
description: "Stellarator extension of JOREK: a reduced MHD model built on the vacuum-field potential (Dommaschk or, since 2024, finite-element), parallel flow, and flux-surface-aligned Bézier grids whose geometry varies toroidally, initialized from GVEC or VMEC and benchmarked against CASTOR3D on Wendelstein 7-A tearing and ballooning modes (within 6.4–26.2 %) and on W7-AS tearing (about 3 %) and interchange modes (within 10 %), then applied to the W7-AS soft β limit."
status: established
aliases: [JOREK stellarator extension]
tags: [stellarator, reduced-mhd, finite-elements, spectral, equilibrium, tearing, ballooning, verification]
timestamp: 2026-10-16T23:45:00Z
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
  §II, Eqs. 1–4). [Ramasamy et al. (2024)](/sources/ramasamy-2024.md)
  (§2.1–2.3) add a parallel flow along $\mathbf B$ with its own momentum
  equation and write the equations in conservative form; the artificial
  parallel diffusivity is then dropped. A two-temperature variant exists
  but is not used (§2). See
  [stellarator reduced MHD](/methods/stellarator-reduced-mhd.md).
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
  Ramasamy et al. (2024) (§2.2) replace it "in all simulations" by a
  finite-element $\chi$ from a Poisson problem, citing numerical
  difficulties of the Dommaschk fit for highly shaped devices; the ideal
  wall then reduces to $\psi$ constant on the boundary (see
  *Contradictions* on [Dommaschk potentials](/methods/dommaschk-potentials.md)).
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
  preconditioner is not specified (§V–VI, footnote 38). Ramasamy et al.
  (2024) (§2.4) use the mode-group preconditioner that couples adjacent
  harmonics of the same [toroidal mode family](/definitions/toroidal-mode-family.md)
  and call it important for making the runs "computationally manageable";
  coupling stays strong in the second and third sidebands of optimized
  configurations. See
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
effects. Ramasamy et al. (2024) (§2.2, §3.2, §4.1) import GVEC and
free-boundary VMEC equilibria of W7-AS, run as fixed-boundary cases; force
balance is "not guaranteed" to survive the change of ansatz, a
single-field-period run relaxes the imbalance first, and a 14 kPa
equilibrium with strong Shafranov shift could not be imported accurately.
A VMEC equilibrium extended into a vacuum region exposes an external
$(7,5)$ mode.

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

## Verification and application on W7-AS

All from [Ramasamy et al. (2024)](/sources/ramasamy-2024.md); version read
is the submitted arXiv v1.

* **$(2,1)$ tearing mode.** Approximate GVEC W7-AS equilibrium (vacuum
  $\iota\approx0.34$ plus an ohmic current giving an $\iota=0.5$ surface),
  no parallel flow, $\eta$ from about $6\times10^{-7}$ to
  $2\times10^{-5}\ \Omega$ m with all visco-resistive coefficients scaled
  together: maximum deviation from [CASTOR3D](/software/castor3d.md) about
  3 %, eigenfunctions in "very good agreement" (§3.1, Fig. 2, Table 1).
  Nonlinearly the $n\equiv\pm1\pmod5$ family leads and the
  $n\equiv\pm2$ family is driven at saturation; the $(2,1)$ island is
  visible at 4.18 ms (Fig. 3; see [tearing mode](/definitions/tearing-mode.md)).
* **Interchange modes** in a low-shear five-period $l=2$ stellarator with
  $\iota$ crossing $2/3$: agreement at $\Gamma=0$ without parallel flow and
  within 10 % for $n=2$–15 at $\Gamma=5/3$ only with parallel flow (§3.2,
  Figs. 5, 7; see [interchange modes](/definitions/interchange-mode.md)).
  The internal benchmark stops at $\beta=0.86\,\%$ because an external
  $(7,5)$ mode interferes; a free-boundary stellarator version is needed
  for it (§3.2).
* **Soft β limit.** β scans from fixed-boundary VMEC reconstructions of
  W7-AS shot #51751 reproduce mild, resistive pressure-driven activity
  whose rate of β rise converges only with toroidal mode numbers up to
  about 50 (§4; see [soft β limit](/definitions/soft-beta-limit.md)).
* Resolutions: $64\times64$ elements with $n\le40$ (tearing),
  $71\times96$ with $n=0,5,\dots,30$ (interchange), $46\times64$ to
  $65\times91$ with $n\le60$ (β scans); HPC systems are named but no
  costs are reported (Tables 1–3, Acknowledgements).

## Limitations

* The parallel velocity is dropped in the 2022 version, which its authors
  hold responsible for the larger tearing deviation (§VI); it is restored
  in the 2024 version (Ramasamy et al. 2024, §2.1).
* No free boundary for stellarators, which blocks external-mode
  benchmarks and limits the W7-AS β-limit study (Ramasamy et al. 2024,
  §3.2, §4.5).
* With $N_{\mathrm{tor}}=5$, field lines drift off flux surfaces and
  anisotropic transport is not properly modelled (§VI).
* Validity at $\beta\sim3$–5 % "remains to be seen", and the model family
  "cannot accurately reproduce kink modes at higher β" (§VIII). The claim
  that it can already handle W7-X and LHD carries no evidence in the paper
  (§VIII).
* Version caveat: a Publisher's Note (Phys. Plasmas 29:099902) postdates the
  arXiv v3 read for this page.

## Contradictions

* **JOREK3D versus CASTOR3D growth rates.** *Open (qualified); the cause of the gap was kept Open by human decision (2026-10-16).*
  Nikulsin et al. (2022) report JOREK3D growth rates systematically above
  CASTOR3D: up to 13.2 % in the $\beta$ scan and 26.2 % in the $\eta$ scan
  for the $(2,1)$ tearing mode (§VI, Fig. 8), and up to 6.4 % for ballooning
  modes (§VII, Fig. 12). They attribute the tearing gap to the neglect of
  $v_\parallel$, which is large in the resistive layer that widens with
  $\eta$ (an analogy is the overestimate of quasi-interchange growth rates by
  $\sqrt{1+2q^2}$, $q$ at the mode surface, without $v_\parallel$), and most of the ballooning gap to
  spectral blocking: adding $n=15$ lowers the JOREK3D $n=10$ growth rate by
  5–6 % but changes CASTOR3D's by less than 0.003 %. The attribution is the
  authors'.
  [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§3.1), with
  Nikulsin and Ramasamy among the authors of both papers, re-attribute the
  tearing mismatch: "the helical mode coupling was not correctly resolved
  in the initial study, due to the use of insufficient poloidal resolution
  in CASTOR3D. At higher poloidal resolution, the level of agreement for
  this simpler case is similar" to their 3 %. No figure or number is given
  for the re-run W7-A case. This is an explicit later statement by the
  original authors that contradicts the 2022 attribution but does not show
  the evidence; it stays open until the human decides whether it
  supersedes. The same 2024 paper shows that, for interchange modes,
  neglecting the parallel flow does make JOREK3D too stable at finite
  compressibility (§3.2), so the 2022 mechanism is real in another case,
  with the opposite sign of the error to the 2022 tearing gap.

# Citations

1. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §§I–VIII, App. A–B, Figs. 1, 4–12.
2. [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §4.1.
3. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.15, §3.8.
4. [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §§2–4, Figs. 2–13, Tables 1–3.
