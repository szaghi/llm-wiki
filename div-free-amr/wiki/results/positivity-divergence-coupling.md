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
3. **The first-order LF scheme keeps that condition, on Cartesian
   meshes.** With the global LF flux the max-norm of
   $D_h^{\mathrm{c}}\bar B_h$ never grows, and it stays exactly zero if it starts
   at zero. The first-order 2D LF scheme is therefore provably
   positivity-preserving. On general meshes, and with HLL-type fluxes, the
   DDF condition generalizes to a wave-speed-weighted face divergence, and
   the conservative scheme no longer preserves it, so it is not
   positivity-preserving in general
   ([Wu & Shu (2019)](/sources/wu-shu-2019.md), eq. 4.9, Corollary 4.1).
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
extension in its Appendix B. It is scoped to conservative schemes; see the
non-conservative escape below.

## The non-conservative escape

The coupling is a statement about **conservative** schemes.
[Wu & Shu (2018)](/sources/wu-shu-2018.md) prove positivity *without* any discrete
divergence-free condition by discretizing Godunov's symmetrizable form,
which carries the [eight-wave](/methods/eight-wave.md) source term
$-(\nabla\cdot B)\,S(U)$.
* **First order.** The LF scheme gains the penalty term
  $-\Delta t\,(D_h^{\mathrm{c}}\bar B_h)\,S(\bar U)$. It is positivity-preserving
  under a CFL-type condition corrected by $\max |B|/\sqrt\rho$, whatever
  $D_h^{\mathrm{c}}\bar B_h$ is.
* **High order.**
  * DG in a *locally* divergence-free polynomial space gives zero
    divergence inside each cell.
  * Penalty terms built from the jumps of the normal field at each face
    control the divergence across faces.
  * With a positivity limiter and SSP time stepping, the scheme is
    provably positivity-preserving. The time-step factor $\theta$ stays
    close to 1 in the tests.
* **The PDE-level motive.**
  * The conservative side remains evidence, not proof (Wu & Shu 2018,
    Appendix A): its exact smooth solution can lose pressure positivity
    when $\nabla\cdot B \ne 0$.
  * The symmetrizable side is now a theorem: any $C^1$ solution keeps
    $\rho > 0$ and $p > 0$ whatever $\nabla\cdot B$ is, because density
    and pressure obey $D_t\rho = -\rho\nabla\cdot v$ and
    $D_t p = -\gamma p\nabla\cdot v$ along particle paths. The same holds
    for Janhunen's system ([Wu & Shu (2019)](/sources/wu-shu-2019.md), Proposition A.1).
* **General meshes and HLL fluxes**
  ([Wu & Shu (2019)](/sources/wu-shu-2019.md), Theorems 4.1, 4.2).
  * The escape extends to HLL-type fluxes on arbitrary polytopal meshes in
    any dimension.
  * The penalty is discretized *upwind*, with the HLL wave speeds, through a
    wave-speed-weighted face divergence. It reduces to the Cartesian LF
    divergence for symmetric speeds.
  * Explicit wave-speed bounds replace the Davis or Einfeldt estimates,
    which are not guaranteed positivity-preserving.
* **The price is conservation**, and the authors state it: "there is still
  a conflict" between the source term and conservation.

Taken together, the two results give a trade-off rather than a free
choice. An LF-type scheme gets provable positivity either by holding a
discrete divergence on its own stencil, or by giving up exact conservation
through the source term.

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
* **Exactness on the staggered stencil is not positivity either.** On
  the $\beta \approx 2.5\cdot10^{-4}$ blast, *no* CT scheme stayed positive
  without the Balsara–Spicer energy correction, even with a minmod limiter.
  This covers six EMF variants, all with an exactly held
  $D_h^{\mathrm{f}}B_h = 0$ ([Mignone & Del Zanna (2021)](/sources/mignone-2021.md) §6.4,
  footnote 2). These are Godunov–Roe schemes, not LF-type, so the theorem
  above does not apply to them; the observation only shows that exactness
  alone does not supply positivity.
* **Controlled-class schemes carry no guarantee.**
  [GLM](/methods/glm-divergence-cleaning.md) and other cleaning methods
  hold no discrete divergence exactly, so this result gives them no
  positivity guarantee. *Compiler reading:* this is consistent with the
  record of [Zaghi (2026)](/sources/zaghi-2026.md), where the mixed GLM
  fails the low-$\beta$ blast. It does not explain that failure, because
  the scheme there is not LF-type, and the record does not isolate the
  cause.
* **Scope.**
  * The conservative-scheme statements are proved for LF on uniform
    Cartesian meshes (Wu 2018). They are generalized to HLL-type fluxes on
    polytopal meshes by Wu & Shu (2019).
  * The non-conservative escape holds on the same general meshes.
  * Numerics exist only in 1D and on 2D rectangles.
  * No source addresses AMR interfaces. *Compiler reading:* if the
    coarse cell at a 2:1 seam is read as a polygon with a hanging vertex,
    the seam is a polytopal configuration that the general-mesh theorems
    formally cover. No source tests it.

# Citations

1. [Wu (2018)](/sources/wu-2018.md), Theorems 2.11, 2.15, 3.1, 4.1, 4.3, 4.5–4.7, 4.10, Remarks 4.4, 4.8–4.9, §5.2, Appendix B.
2. [Wu & Shu (2018)](/sources/wu-shu-2018.md), Theorems 3.1, 3.4, Remarks 3.3, 3.6, §5, Appendix A.
3. [Wu & Shu (2019)](/sources/wu-shu-2019.md), Theorems 2.1–2.2, 4.1–4.3, Corollary 4.1, Remarks 4.1, 4.3, Proposition A.1.
4. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §6.4.
