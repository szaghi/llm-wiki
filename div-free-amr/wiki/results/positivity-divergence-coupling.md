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
* **A finite-volume, point-value version**
  ([Ding & Wu (2024)](/sources/ding-2024.md)). Standard FV-WENO returns interface point
  values, not polynomials, so a locally divergence-free basis is not
  available. The paper replaces it with a **projection of the
  reconstructed traces**.
  * In each cell, the normal-field traces on the cell's own faces are
    shifted by the minimal-norm correction that zeroes their
    face-quadrature divergence. That cell-*local*, $D_h^{\mathrm{f}}$-type
    divergence of the cell's own traces then vanishes exactly.
  * The correction is an orthogonal projection, $P^2 = P$, and it keeps
    the reconstruction's order (Theorem 2.7).
  * A new, symmetric source term built from the face jumps of $B_n$,
    evaluated at the averaged face state, handles the inter-cell part.
    The authors report it allows a milder CFL than the Wu–Shu versions.
  * With a point-value positivity limiter this is provably positive
    (Theorem 2.1) with LF fluxes. Removing any of the three ingredients
    voids the proof.
  * The condition is enforced on the reconstruction at every stage; it is
    not an invariant of evolved data. The cell averages $\bar B_h$ are not
    held to any discrete divergence.

Taken together, the results give a trade-off rather than a free
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
* **An early observation of the coupling.** A fifth-order WENO
  finite-difference scheme with Lax–Friedrichs flux splitting loses
  pressure positivity on Orszag–Tang without divergence control, and runs
  stably with a projection ([Jiang & Wu (1999)](/sources/jiang-1999.md)).
  *Compiler reading:* this is the failure the theorem predicts for LF-type
  schemes. It is not covered by the theorem, which is proved for
  finite-volume and DG schemes, and the projection holds a divergence on a
  stencil the paper does not specify.
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
  alone does not supply positivity. The same holds at fourth order: in
  [Berta et al. (2024)](/sources/berta-2024.md) the Balsara–Spicer case and an RMHD blast
  needed the second-order energy correction. Felker & Stone's blast at
  three times their magnetization was the strongest case the scheme could
  run without it.
  [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md) report the same
  limit for their exact-CT base scheme: it loses thermal-energy positivity
  in strongly shocked low-$\beta$ flows.
* **Restoring the constraint can itself break positivity.** In
  potential-based CT the field is overwritten by the curl of the potential
  after each step, which changes the magnetic energy. [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md) keep the pressure
  instead, adjusting the total energy, whenever their positivity limiter is
  on. That costs exact energy conservation; the measured error stays below
  1% except on the coarsest meshes, grows linearly in time and falls with
  refinement. The limiter was required for the rotor, both blasts and the 3D
  cloud–shock at $256^3$.
  Without CT, Orszag–Tang crashes at $t = 1.67$.
* **The same repair for a staggered high-order scheme.** In
  [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), a first-order zone update is hybridized with the high-order one,
  zone by zone, until every zone is admissible. Averaging the exact face
  fields to the zone centre can still break admissibility in rare zones.
  These are repaired by borrowing thermal energy from a neighbour, or, if
  none can lend, by a low-order energy source.
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

## Contradictions

**Is the first-order LF update positivity-preserving for admissible data
in more than one dimension?**

* [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md) build their limiter on this claim, conjectured by Cheng et al.
  (2013): admissible data and CFL $\le 0.5$ give an admissible LF update.
  They state it is unproven, verified only on random states, and that
  their limiter assumes it.
* [Wu (2018)](/sources/wu-2018.md), Theorem 4.1: for every CFL number and
  every viscosity multiple there are admissible 2D data whose LF update
  leaves $\mathcal{G}$. Wu presents this as the refutation of exactly that
  conjecture.

**Closed by explicit supersession** (Wu 2018 addresses the conjecture
directly). The limiter therefore guarantees positivity only when its
low-order LF update does, which by Statement 2 requires a discrete
divergence-free condition. *Compiler reading:* Christlieb et al.'s field is
the fourth-order central curl of the potential. It is annihilated by the
matching fourth-order central divergence, but not by the second-order
$D_h^{\mathrm{c}}$ that the first-order theorem uses, so the sufficient
condition is not met by construction. Their runs did not fail; this is a
gap in the guarantee, not an observed failure.

**Is the first-order HLL/LLF zone update positivity-preserving in more
than one dimension?** (open)

* [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md) state that a first-order zone-centred MHD update with HLL or LLF face
  fluxes "will indeed be PCP, as was first proved by Gurski" (2004), and
  build their low-order fallback on it. They do not cite Wu (2018).
* [Wu (2018)](/sources/wu-2018.md) proves that for the LF scheme in 2D,
  admissible data alone do not suffice, at any CFL and viscosity; a
  discrete divergence-free condition on the scheme's own stencil is
  needed. [Wu & Shu (2019)](/sources/wu-shu-2019.md) extend this to HLL.

**Scoped reading (compiled, open).** The cited Gurski proof is not ingested;
as far as the citing text shows, it concerns a one-dimensional Riemann
solver. The multi-dimensional statement then needs Wu's condition. The
zone-centred field here is the average of exactly divergence-free face
fields, which in general does not make the collocated central divergence of
the averages vanish, so the condition is not met by construction. The
scheme's practical guarantee does not depend on the disputed claim, since
any zone that fails is repaired by the energy borrowing or source. What
remains unsettled is whether the low-order fallback is positive by itself.

# Citations

1. [Wu (2018)](/sources/wu-2018.md), Theorems 2.11, 2.15, 3.1, 4.1, 4.3, 4.5–4.7, 4.10, Remarks 4.4, 4.8–4.9, §5.2, Appendix B.
2. [Wu & Shu (2018)](/sources/wu-shu-2018.md), Theorems 3.1, 3.4, Remarks 3.3, 3.6, §5, Appendix A.
3. [Wu & Shu (2019)](/sources/wu-shu-2019.md), Theorems 2.1–2.2, 4.1–4.3, Corollary 4.1, Remarks 4.1, 4.3, Proposition A.1.
4. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §6.4.
5. [Ding & Wu (2024)](/sources/ding-2024.md), Theorems 2.1, 2.6–2.7, §§2.3, 4.
6. [Berta et al. (2024)](/sources/berta-2024.md), §5.7.
7. [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md), §8.
8. [Jiang & Wu (1999)](/sources/jiang-1999.md), §3.4.
9. [Christlieb, Feng, Seal & Tang (2016)](/sources/christlieb-2016.md), §§2, 5, 6.7, Claim 1.
10. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §5.
