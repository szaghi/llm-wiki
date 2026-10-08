---
type: Result
title: "Positivity–divergence coupling"
description: "For conservative Lax-Friedrichs-type MHD schemes in 2D and 3D, provable positivity of density and pressure requires a discrete divergence-free condition on the scheme's own interface fields; admissible cell data alone are not enough."
status: established
aliases: [PP-DDF coupling, positivity requires discrete divergence-free]
tags: [positivity, divergence-constraint, mhd, admissibility, lax-friedrichs]
timestamp: 2026-10-08T00:00:00Z
---

# Positivity–divergence coupling

**Statement.** Let a conservative finite-volume or DG scheme for ideal MHD
use the Lax–Friedrichs flux on a uniform Cartesian mesh. A scheme is
*positivity-preserving* if its cell averages stay in the admissible set
$\mathcal{G}$ ([notation](/notation.md)). In more than one dimension:

1. **Admissibility alone fails.** For every viscosity multiple and every
   CFL number there are admissible data whose first-order LF update leaves
   $\mathcal{G}$. The counterexample violates the
   divergence condition only slightly, at low pressure.
2. **Divergence-free data suffice.** If the data are admissible and satisfy
   the discrete divergence-free condition, the update stays in
   $\mathcal{G}$ under $\sum_\ell \alpha_\ell^{\mathrm{LF}}\Delta t/\Delta x_\ell \le 1$.
   This needs the generalized viscosity bound of the theorem, not the
   standard spectral radius. For the first-order scheme the condition is
   the collocated central divergence of the cell averages,
   $D_h^{\mathrm{c}}\bar B_h = 0$.
3. **The first-order LF scheme keeps that condition.** The max-norm of
   $D_h^{\mathrm{c}}\bar B_h$ never grows, and it stays exactly zero if it
   starts at zero. The first-order 2D LF scheme is therefore provably
   positivity-preserving.
4. **High order.** For FV and DG schemes, the sufficient conditions are:
   * the reconstructed states are admissible at Gauss–Lobatto points, which
     a scaling limiter enforces;
   * the divergence built from Gauss quadrature of the averaged interface
     normal fields vanishes, which is a face-flux divergence of
     $D_h^{\mathrm{f}}$ type.
   
   A globally divergence-free polynomial field satisfies the second
   condition by Green's theorem. A merely *locally* divergence-free field
   does not. The scaling limiter can destroy global divergence-freeness,
   and how to enforce both conditions at once is left open.
5. **Quantitative form.** When the divergence condition fails, the new
   internal energy is bounded below by
   $-\Delta t\,(\bar v\cdot\bar B)\,D_h B_h$. Negative pressure is
   therefore most likely where $|v\cdot B|$ and the divergence error are
   both large.

Proved by [Wu (2018)](/sources/wu-2018.md) in 1D and 2D, with the 3D
extension in its Appendix B.

## Why it matters for this bundle

* **It is a second reason for the constraint.** The classical case for
  $D_h B_h = 0$ is the anomalous parallel force
  ([exact discrete divergence](/properties/exact-discrete-divergence.md)).
  This result adds a theorem: without a discrete divergence-free condition,
  no LF-type scheme can guarantee positive pressure, however much viscosity
  it adds.
* **The stencil matters again.** The condition is tied to the flux form the
  scheme actually uses: a collocated central divergence at first order, a
  quadrature face divergence at high order. A field held exactly
  solenoidal in some other stencil does not qualify automatically. The
  same scheme-relative reading applies as for
  [exact discrete divergence](/properties/exact-discrete-divergence.md).
* **Controlled-class schemes carry no guarantee.**
  [GLM](/methods/glm-divergence-cleaning.md) and other cleaning methods
  hold no discrete divergence exactly, so this result gives them no
  positivity guarantee. *Compiler reading:* this is consistent with the
  record of [Zaghi (2026)](/sources/zaghi-2026.md), where the mixed GLM
  fails the low-$\beta$ blast. It does not explain that failure, because
  the scheme there is not LF-type, and the record does not isolate the
  cause.
* **Scope.** Uniform Cartesian meshes and the LF flux only. Extensions to
  less dissipative fluxes and to non-uniform or unstructured meshes are
  announced, not proved here. The behavior across AMR interfaces is
  unaddressed.

# Citations

1. [Wu (2018)](/sources/wu-2018.md), Theorems 2.11, 2.15, 3.1, 4.1, 4.3, 4.5–4.7, 4.10, Remarks 4.4, 4.8–4.9, §5.2, Appendix B.
