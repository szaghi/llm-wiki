---
type: Method
title: "Three-dimensional inverse equilibrium solvers"
description: "Codes that compute 3D ideal-MHD equilibria with nested flux surfaces by solving for the positions R, Z of the surfaces as functions of flux coordinates: VMEC (Fourier in angle, radial finite differences, energy descent), DESC (global Fourier–Zernike pseudospectral, Newton-type solve of the force residual) and GVEC (B-spline radial basis, energy minimization); they supply initial states and grids to nonlinear MHD and hybrid codes."
status: established
aliases: [inverse equilibrium, 3D equilibrium codes, VMEC-type solvers, fixed-boundary 3D equilibrium]
tags: [equilibrium, stellarator, spectral, verification]
timestamp: 2026-10-16T12:00:00Z
---

# Three-dimensional inverse equilibrium solvers

An inverse equilibrium solver does not solve for the flux as a function of
position, as the [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
does in axisymmetry. It solves for the position of the flux surfaces as a
function of flux coordinates. The unknowns are $R(s,\theta,\phi)$,
$Z(s,\theta,\phi)$ and a periodic angle stream function that relates the
computational poloidal angle $\theta$ to the straight-field-line angle
$\theta^*$. The solution satisfies ideal MHD force balance

$$\mathbf J\times\mathbf B=\nabla p,\qquad \mu_0\mathbf J=\nabla\times\mathbf B,\qquad \nabla\cdot\mathbf B=0,$$

or, equivalently, is a stationary point of the energy
$W=\int_V\big(B^2/2\mu_0+p/(\Gamma-1)\big)\,dV$. The field is written in
contravariant form,

$$\mathbf B=\nabla\psi_t\times\nabla\theta^*+\nabla\phi\times\nabla\psi,\qquad \iota=\frac{d\psi}{d\psi_t},$$

which is divergence-free identically
([Panici et al. (2023)](/sources/panici-2023.md), Eqs. 1.1–1.3, 3.4, 3.22,
A9a; see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
Here $\psi_t$ and $\psi$ are the toroidal and poloidal fluxes per radian;
the source's own symbols for them, and its $2\pi$ conventions, are
translated on its Source page. The inputs of the fixed-boundary problem are
$p$, either $\iota$ or the net toroidal current, and the boundary shape.
These codes assume nested flux surfaces with $p$ constant on them and
cannot represent magnetic islands (same source, §2).

## The codes

* **VMEC** expands $R$, $Z$ and the angle stream function in Fourier
  series in $(\theta,\phi)$ on discrete radial surfaces, labelled by the
  normalized toroidal flux $\psi_{t,N}$, with first-order radial finite
  differences. It minimizes $W$ by steepest descent accelerated as a
  second-order Richardson iteration, uses the angle stream function to
  minimize the spectral width (Hirshman–Breslau), and refines radially by
  multigrid continuation ([Panici et al. (2023)](/sources/panici-2023.md),
  §3.1, Eqs. 3.1–3.15). See [VMEC](/software/vmec.md).
* **DESC** expands $R$, $Z$ and the angle stream function in a global
  Fourier–Zernike basis in $(s,\theta,\phi)$ with $s=\sqrt{\psi_{t,N}}$,
  evaluates the volume-weighted force residual at collocation nodes and
  drives it to zero with Newton-type (Levenberg–Marquardt) iterations,
  implemented in Python with JAX. The Zernike radial polynomials satisfy the
  near-axis analyticity condition by construction: the coefficient of
  poloidal harmonic $m$ behaves as $s^{m}$ times a power series in $s^2$
  (Lewis & Bellan 1990). The version compared uses a VMEC-like poloidal
  angle; the original DESC paper (Dudt & Kolemen 2020) used $\theta^*$
  ([Panici et al. (2023)](/sources/panici-2023.md), §3.2, Eqs. 3.16–3.28).
  See [DESC](/software/desc.md).
* **GVEC** is a fixed-boundary 3D equilibrium solver that follows VMEC's
  ideas (nested surfaces, minimization of the MHD energy) but uses
  non-uniform B-splines of arbitrary order in the radial direction, which
  gives a smooth representation of equilibrium quantities
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §I).

## Accuracy: the DESC–VMEC comparison

[Panici et al. (2023)](/sources/panici-2023.md) compare the two codes with
a common metric: the magnitude of $\mathbf J\times\mathbf B-\nabla p$,
averaged over a flux surface or the volume and normalized by the
volume-averaged $|\nabla p|$. VMEC's value is reconstructed from its
Fourier output (§4, App. A).

* **Radial convergence.** On an axisymmetric D-shaped case (β about 3%),
  VMEC converges at first order in the number of radial surfaces (log-log
  slope $-1.02$); DESC converges exponentially in the radial resolution,
  error $\approx\exp(-0.61L)$, from about $5\times10^{-5}$ at $L=16$ to
  $4\times10^{-7}$ at $L=24$ (§5.2, Figs. 7–8).
* **Near the axis.** VMEC Fourier coefficients divided by $s^m$ diverge
  toward the axis, by up to about $10^{10}$ for high $|m|+|n|$, and VMEC's
  force error on W7-X ($\beta\approx2\%$) rises to about $10^2$ at the axis,
  against about $5\times10^{-2}$–$10^{-1}$ at mid-radius; DESC's error is
  flat down to the axis (§5.1, §5.3, Figs. 4, 11).
* **Cost.** At equal runtime on the same CPU, DESC's error is generally an
  order of magnitude lower on W7-X (§5.3.2, Fig. 12). DESC runtimes do not
  fall below about 2 min because of just-in-time compilation.
* **Stability input.** On a quasi-helically symmetric case (aspect ratio
  about 20), DESC's Mercier criterion matches near-axis asymptotic formulae
  down to the axis, while VMEC deviates near the axis even with 801
  surfaces, the deviation being dominated by the geodesic-curvature term
  that needs high-order radial derivatives (§5.4, Figs. 15–16; see
  [quasi-symmetry](/definitions/quasi-symmetry.md)).
* **Unchanged quantities.** Flux-surface shapes and the spectral width
  agree between the codes (§5.1, Figs. 5, 9–10). VMEC's force-error spikes
  near the edge sit at the radial nodes of a coarser multigrid level and do
  not disappear with a tighter tolerance or higher angular resolution
  (§4.1, App. B).

The comparison averages VMEC only over $0.1\le\psi_{t,N}\le0.99$ and DESC
over the full volume, which the authors say "could make the VMEC
calculations appear to have lower error" (§4).

## Use by nonlinear and hybrid codes

* **JOREK3D** builds its flux-surface-aligned, toroidally varying grid
  from a GVEC equilibrium and derives the initial reduced-MHD current from
  it; the full-MHD equilibrium leaves a small residual force in the
  reduced model ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md),
  §I, §IV; see [reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)).
* **JOREK3D, W7-AS.** Free-boundary VMEC reconstructions of W7-AS shot
  #51751 (central pressures 1–14 kPa, pressure scaled linearly) serve as
  fixed-boundary initial states; force balance is "not guaranteed" to
  survive the change to the reduced ansatz, and the 14 kPa case, with a
  strong Shafranov shift, could not be represented accurately and was
  dropped. A GVEC equilibrium leaves a force imbalance that a
  single-field-period run relaxes before the full-torus run. A VMEC
  equilibrium extended into a vacuum region exposes an external $(7,5)$
  mode that a boundary at the last closed surface suppresses
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §2.2, §3.1–3.2,
  §4.1; see [soft β limit](/definitions/soft-beta-limit.md)).
* **M3D-C1, W7-X.** A fixed-boundary VMEC equilibrium supplies both the
  non-axisymmetric domain, through the map $R(\psi_{t,N},\theta,\phi)$,
  $Z(\psi_{t,N},\theta,\phi)$, which does not evolve, and the initial
  $\mathbf B$ and $p$. Because an ideal equilibrium need not be sustained by
  a dissipative, sourced model on transport time scales, the equilibrium
  is made self-consistent in two passes: VMEC, a one-field-period M3D-C1
  run to saturation, VMEC rebuilt from the saturated $\iota$ and $p$, and
  a second M3D-C1 check in which $\iota$ and $T_e$ "barely evolve" and
  only small island chains form
  ([Zhou et al. (2023)](/sources/zhou-2023.md), §III, Fig. 2; see
  [sawtooth crash](/definitions/sawtooth-crash.md)).
* **GMEC** reads VMEC equilibria (transformed to Boozer coordinates
  following Hirshman) or DESC equilibria, the latter providing
  "high-precision derivatives". Its ideal-ballooning benchmark uses a VMEC
  equilibrium with 800 radial points and its tearing benchmark a DESC
  equilibrium of a circular $R=10$ m plasma
  ([Jiang et al. (2024)](/sources/jiang-2024.md), §VI C, §IX, App. C–D; see
  [GMEC](/software/gmec.md) and
  [field-aligned coordinates](/methods/field-aligned-coordinates.md)).
  GMEC's TAE results with a VMEC equilibrium are "almost the same" as with
  the analytic one ([Liu et al. (2024)](/sources/liu-2024.md), §III B).
* **M3D-C1** runs quasi-axisymmetric stellarators from a zero-pressure
  VMEC equilibrium and from a SIMSOPT-optimized one, and its quasi-symmetry
  error at $t=0$ and $t=250\tau_A$
  "closely resembles" VMEC's ([Saxena et al. (2025)](/sources/saxena-2025.md),
  §3.2–3.3, Fig. 8).
* **JOREK** saturated external modes agree qualitatively with VMEC
  free-boundary equilibria with the same dominant $n$, with differences in
  energy spectrum and topology from coupling to internal modes and non-ideal
  effects ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.1).

# Citations

* [Panici et al. (2023)](/sources/panici-2023.md) — formulation of VMEC and DESC and their accuracy comparison.
* [Jiang et al. (2024)](/sources/jiang-2024.md) — VMEC and DESC as inputs to a field-aligned MHD code.
* [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — GVEC and its use for JOREK3D grids.
* [Saxena et al. (2025)](/sources/saxena-2025.md) — VMEC equilibria for M3D-C1 stellarator runs.
* [Liu et al. (2024)](/sources/liu-2024.md) — VMEC equilibrium for TAE benchmarks.
* [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — VMEC–JOREK comparison of external modes.
* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — VMEC and GVEC equilibria imported into JOREK3D.
* [Zhou et al. (2023)](/sources/zhou-2023.md) — self-consistent VMEC–M3D-C1 initialization for W7-X.
