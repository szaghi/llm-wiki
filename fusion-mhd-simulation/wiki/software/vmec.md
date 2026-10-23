---
type: Software
title: "VMEC"
description: "Variational moments equilibrium code: 3D ideal-MHD inverse equilibria with nested surfaces, Fourier series in the angles and radial finite differences, found by minimizing the MHD energy with a second-order Richardson iteration and multigrid radial continuation; first-order accurate in radius and inaccurate near the axis, it is the standard equilibrium source of the stellarator and EP codes in the cited sources."
status: established
aliases: [variational moments equilibrium code, NEMEC]
tags: [equilibrium, stellarator, spectral, finite-differences]
timestamp: 2026-10-16T18:35:00Z
---

# VMEC

VMEC computes fixed-boundary 3D ideal-MHD equilibria with nested flux
surfaces by an inverse representation: the cylindrical coordinates of the
flux surfaces are the unknowns ([Panici et al. (2023)](/sources/panici-2023.md),
§3.1). It cannot represent islands (§2). See
[three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md).
NEMEC, a VMEC variant, supplies the initial equilibrium of the JOREK3D
workflow ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §I).

## Representation and solver

All from Panici et al. (2023), §3.1, unless cited otherwise.
* Coordinates: the normalized toroidal flux $\psi_{t,N}$ as radial label, a
  poloidal angle equal to the straight-field-line angle minus a stream
  function $\lambda$, and the cylindrical toroidal angle over one field period
  (Eq. 3.1).
* $R$, $Z$ and $\lambda$ are Fourier series in the two angles on discrete flux
  surfaces; stellarator symmetry removes half the coefficients; $\lambda$ is
  chosen to minimize the spectral width $M(2,2)$ (Hirshman–Breslau) (Eqs.
  3.2–3.3). $\lambda$ lives on a radial half-mesh (App. A).
* Radial derivatives are first-order finite differences between neighbouring
  surfaces (§3.1).
* The MHD energy $\int(B^2/2\mu_0+p/(\Gamma-1))\,\mathrm dV$ is minimized; the
  steepest-descent flow is replaced by a second-order Richardson scheme with a
  damping time set by the least-damped eigenmode (Eqs. 1.3, 3.13–3.15).
* Inputs: $p$, either $\iota$ or the net toroidal current, and the boundary
  shape; a force tolerance FTOL; multigrid radial continuation over a sequence
  of surface counts (NS_ARRAY) (§3.1).

## Accuracy

From Panici et al. (2023), with a force-residual metric normalized by the
volume average of $|\nabla p|$ that the authors compute from VMEC's Fourier
output (§4, App. A):
* First-order radial convergence on a D-shaped tokamak (fit slope $-1.02$),
  normalized error about 0.03 at 1024 surfaces, above the $10^{-4}$ threshold
  that [DESC](/software/desc.md) meets (§5.2, §5.4, Fig. 7).
* Fourier coefficients divided by $s^{m}$ ($s=\sqrt{\psi_{t,N}}$) diverge, up to
  about $10^{10}$, toward the axis, "evidence of possibly unphysical modes"
  (§5.1, Fig. 4); the W7-X force error rises to about $10^2$ at the axis
  (§5.3, Fig. 11).
* Edge force-error spikes sit at the radial nodes of a coarse grid of the
  multigrid sequence; tighter FTOL or higher angular resolution does not remove
  them (§4.1, App. B).
* Error stops decreasing beyond 1024 surfaces and stagnates at $M=N=20$ in
  angle (App. C); FTOL below $10^{-14}$ took more than 24 h (App. B).
* Mercier stability deviates from near-axis theory inside $s\approx0.25$ even
  at 801 surfaces, dominated by the geodesic-curvature term (§5.4, Fig. 15).
* VMEC's near-axis inaccuracy "has been found to cause issues when conducting
  ideal MHD stability analyses near the axis" (A.H. Glasser, personal
  communication, quoted in §5.4).

## Use by other codes in the cited sources

* **GMEC**: VMEC equilibria converted to Boozer coordinates (Hirshman's
  transformation) supply the ideal-ballooning benchmark (800 radial surfaces)
  ([Jiang et al. (2024)](/sources/jiang-2024.md), §VI C, §IX A, App. C) and the
  ITPA TAE and DIII-D RSAE cases; the $n=3$ TAE on a VMEC equilibrium gives
  almost the same result as on the analytic one
  ([Liu et al. (2024)](/sources/liu-2024.md), §II D, §III B–D). See
  [GMEC](/software/gmec.md).
* **M3D-C1**: a zero-pressure VMEC equilibrium for the first quasi-axisymmetric
  bootstrap case; the quasi-symmetry error computed from M3D-C1 output
  "closely resembles" VMEC's, while SFINCS's is lower by a factor of about 2–3
  in the figure, not discussed in the text
  ([Saxena et al. (2025)](/sources/saxena-2025.md), §3.2–3.3, Fig. 8). See
  [M3D-C1](/software/m3d-c1.md). For W7-X, a fixed-boundary VMEC map defines
  the M3D-C1 domain and initial state; VMEC is re-run on the profiles of a
  saturated one-period M3D-C1 run to obtain an equilibrium the dissipative
  model sustains ([Zhou et al. (2023)](/sources/zhou-2023.md), §III).
* **JOREK**: comparisons of VMEC-based saturated external modes with nonlinear
  JOREK runs agree qualitatively when the dominant $n$ is the same, but the
  magnetic-energy spectrum and topology can differ through coupling to
  internal modes and non-ideal effects
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.1). See
  [JOREK3D](/software/jorek3d.md). JOREK3D imports free-boundary VMEC
  reconstructions of W7-AS as fixed-boundary initial states up to 10 kPa
  central pressure; a 14 kPa case with strong Shafranov shift could not be
  imported accurately, and a VMEC equilibrium extended into vacuum exposes
  an external $(7,5)$ mode
  ([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.2, §4.1).
* **MIPS and MEGA, LHD.** VMEC re-solves the equilibrium inside the last
  closed surface of a [HINT](/software/hint.md) equilibrium, which has a
  stochastic region outside it that VMEC cannot represent; the $\iota$ and
  pressure profiles agree with HINT's. The VMEC solution provides the
  Boozer coordinates (via NEWBOZ) onto which the cylindrical simulation
  data are interpolated for Fourier analysis, and the Mercier evaluation
  ([Sato & Todo (2026)](/sources/sato-2026.md), p. 3, Fig. 1; see
  [interchange modes](/definitions/interchange-mode.md)).
* **JOREK3D** uses GVEC, described as VMEC-like energy minimization with a
  B-spline radial basis, for its grid and initial state (Nikulsin et al. 2022,
  §I, §IV).

## Limitations

Nested surfaces only; first-order radial accuracy; poor near-axis behaviour
of the Fourier coefficients and of derived quantities that need high radial
derivatives (Panici et al. 2023, §2, §5). The authors' VMEC error averages
exclude $\psi_{t,N}<0.1$ and $>0.99$, which they note makes VMEC look more
accurate (§4).

# Citations

1. [Panici et al. (2023)](/sources/panici-2023.md) — §§2–5, App. A–C, Figs. 4, 7, 11, 15.
2. [Jiang et al. (2024)](/sources/jiang-2024.md) — §VI C, §IX A, App. C.
3. [Liu et al. (2024)](/sources/liu-2024.md) — §II D, §III B–D.
4. [Saxena et al. (2025)](/sources/saxena-2025.md) — §3.2–3.3, Fig. 8.
5. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §I, §IV.
6. [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §4.1.
7. [Zhou et al. (2023)](/sources/zhou-2023.md) — §III.
8. [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §3.2, §4.1.
9. [Sato & Todo (2026)](/sources/sato-2026.md) — p. 3, Fig. 1.
