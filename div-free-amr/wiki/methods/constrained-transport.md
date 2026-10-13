---
type: Method
title: "Constrained transport (CT)"
description: "Evolves face magnetic fluxes from once-computed edge EMFs so the discrete divergence of the field is conserved identically."
status: established
aliases: [CT]
tags: [constrained-transport, staggered, mhd, induction-equation]
timestamp: 2026-10-13T00:00:00Z
---

# Constrained transport (CT)

A finite-difference formulation of the ideal-MHD induction equation
$\partial_t \mathbf{B} = \nabla \times (\mathbf{V} \times \mathbf{B})$ that
maintains the [exact discrete divergence](/properties/exact-discrete-divergence.md)
of the magnetic field to machine roundoff, introduced by
[Evans & Hawley (1988)](/sources/evans-hawley-1988.md).

**Earlier history, as Balsara & Spicer give it.**
[Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md) §1 trace the
staggered, Stokes-theorem-based field transport further back. It "was first
proposed by Yee" for electromagnetic fields
([Yee scheme](/methods/yee-scheme.md)). Brecht et al. (1981) combined it
with a nonlinear FCT limiter in global magnetosphere MHD. Evans and Hawley
then "applied the hybrid scheme utilized by Brecht et al. to an artificial
viscosity based scheme, coining the term 'constrained transport'";
DeVore applied it to FCT at about the same time. In this account Evans &
Hawley named the method and carried it into their scheme; they did not
originate the staggered update. The Brecht et al. and DeVore papers are not
ingested.

## Construction

1. **Integral form, flux as the variable.** The induction equation is placed
   in integral form: the rate of change of magnetic flux $\Phi_S$ through a
   (possibly moving) cell face equals minus the total EMF circulated around
   the face boundary. Fluxes through [staggered](/definitions/staggered-grid.md)
   cell faces — elements of $V_h^2$ — are the fundamental evolved quantities;
   the face field $B_h$ is the area-averaged flux.
2. **Edge EMFs, computed once.** Each cell edge carries one EMF value
   $E_h \in V_h^1$, obtained by any suitable transport approximation (donor
   cell, van Leer monotonic, PPM, …). Every edge EMF is *calculated once* and
   enters the two adjacent face updates it borders with opposite signs.

   **PPM as a transport approximation.** The advection scheme of the PPM
   paper is a conservative transport scheme of exactly this kind. That
   paper is pure hydrodynamics and applies it to no magnetic field or EMF
   ([Colella & Woodward (1984)](/sources/colella-woodward-1984.md), §1;
   [PPM](/methods/ppm.md)).
3. **Update.** In registry terms the scheme is
   $$\partial_t B_h = -\,C_h E_h,$$
   so the divergence is stationary by the complex identity:
   $$\partial_t\,(D_h B_h) = -\,D_h C_h E_h = 0 .$$
   (Evans & Hawley state this as the once-per-edge/twice-per-face sign
   cancellation of their eqs. 4.7/4.13; the identity $D_h C_h = 0$ is the
   compiled form — see the
   [source's notation map](/sources/evans-hawley-1988.md).)

## Properties

* **Transport-scheme agnostic:** no restriction on the order of accuracy of
  the EMF reconstruction; the constraint mechanism is the topology of the
  edge-face assembly, not the interpolant
  [Evans & Hawley (1988)](/sources/evans-hawley-1988.md).
* **Coordinate- and metric-independent:** with the magnetic vector density
  absorbing the metric, the same scheme runs in curvilinear coordinates and
  general-relativistic (3+1) spacetimes unchanged.
* **Moving/adaptive meshes:** the flux-integral form accounts for zone motion
  (grid velocity enters the net transport velocity), which Evans & Hawley
  argue admits adaptive meshes naturally — provided the remap is built from
  the flux-update form; naive differencing of the convective form destroys
  the constraint.
* **Preserves changes only:** initial data must satisfy $D_h B_h = 0$
  (e.g. via edge-differenced vector potential, their eq. 4.17); inflow
  boundaries can inject divergence — monitor a global diagnostic.
* **One-derivative Lorentz force:** compared with evolving the vector
  potential, CT computes currents from a single difference of the evolved
  field, avoiding the anomalous current oscillations produced by second
  differences of monotonically-advected quantities.
* **Embedded boundaries:** on a Cartesian mesh cut by a non-conforming
  wall or material interface, extrapolated ghost fields are not solenoidal,
  but they reach the active faces only through $E_h$. The invariant
  therefore survives in the active domain, while magnetic flux through the
  boundary is not conserved. A two-material interface keeps one global
  $B_h$ with fraction-weighted edge EMFs; one field per side would create
  monopoles
  ([embedded-boundary CT](/methods/embedded-boundary-constrained-transport.md);
  [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md)).

## High-order extension

The scheme's divergence guarantee is a statement about cell/face *averages*;
above second order it survives only if the reconstruction of point values is
itself [divergence-free](/methods/divergence-free-reconstruction.md), and
the corner EMF becomes a genuinely two-dimensional four-state upwind flux
rather than an average —
[Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), who
build a third-order ENO-based CT scheme on these two ingredients.
Their 2004 formalization,
[upwind constrained transport](/methods/upwind-constrained-transport.md),
says where the exact invariant lives on point values. The evolved primary
data are deconvolved face variables, whose point-value divergence is
preserved to machine precision. The point values that feed the fluxes are
recovered by an implicit inversion, so their divergence is exact only to the
inversion's precision ($10^{-7}$–$10^{-6}$ maxima at third order)
([Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md),
Appendix A). High-order CT on point values therefore holds the invariant on
a variable that the fluxes never see directly.

**A second-order CT step caps a high-order code.** With fifth-order
finite-difference WENO fluxes, the second-order CT of Ryu et al. (1998)
gives second-order convergence on 3D linear and circularly polarized
Alfvén waves. [Seo & Ryu (2023)](/sources/seo-2023.md) restore fifth order with a high-order staggered CT:
* the edge "advective fluxes" ($E_h$) are assembled from WENO-reconstructed
  magnetic fluxes, interpolated to edges at fourth order, and corrected to
  edge point values;
* faces are updated by fourth- or sixth-order central differences of those
  edge values (CT4, CT6);
* the cell-centred field is a sixth-order interpolation of the faces.

Both CT4 and CT6 converge at fifth order, at almost the same cost as the
second-order step. The paper states that the divergence is preserved "up
to the numerical truncation error"; its rotor diagnostic saturates there.
*Compiler reading:* each face update is a difference, along one axis, of
a single-valued edge array, and the divergence is evaluated with the
matching one-axis differences. Differences along different axes commute on
a tensor-product grid, so the update preserves that divergence identically,
as in [exact discrete divergence](/properties/exact-discrete-divergence.md).
The paper's "truncation" wording therefore probably refers to the
saturation level of its diagnostic rather than to a defect of the identity;
the text alone does not settle it.

**The base scheme.** The fifth-order FD-WENO is the point-value flux form
of Jiang & Shu, which contains no MHD and no divergence control; HOW-MHD's
local Lax–Friedrichs splitting is its own choice, since Jiang & Shu test
only global splitting ([Jiang & Shu (1996)](/sources/jiang-shu-1996.md),
§§2, 4; [WENO reconstruction](/methods/weno.md)).

**Origin of local splitting.** Local Lax–Friedrichs splitting in the point-value flux framework is ENO-LLF of [Shu & Osher (1989)](/sources/shu-osher-1989.md) (Alg. 2.2, eq. 2.12; systems eqs. 4.3–4.4). What is HOW-MHD's own is its use inside Jiang–Shu WENO, which Jiang & Shu allow in words but do not test ([WENO reconstruction](/methods/weno.md)).

## Shock-capturing combinations and the collocated recast

CT as introduced is a finite-difference discretization; it was subsequently
combined with conservative Godunov-type base schemes by supplying the edge
EMF from base-scheme data — the field-CT / flux-CT / transport-flux-CT family
([Flux-CT and the Godunov CT variants](/methods/flux-ct.md);
[Tóth (2000)](/sources/toth-2000.md) §4).

**The field-CT primary sources.**
[Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md) and
[Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md) derive the
Godunov combination from the integral form. The face average of each
field component changes by the space–time averages of $E_h$ along the
edges of its face, an exact statement on averages, so the net face flux
of every cell is unchanged (JCP eqs. 18–24; ApJ eqs. 17–23). Their stated
reason that conservation and the constraint can hold together is
structural: the conservation law of each field component has no
derivative along that component, so eight conservation laws and the
constraint fit one set of eight difference equations (JCP §2, ApJ §2).
* They do not call the scheme CT. In their account Evans–Hawley CT, as
  used by Stone & Norman, satisfies the constraint exactly "although the
  conservation laws are satisfied to the accuracy of the algorithms" (JCP
  §1); theirs is claimed to conserve all eight quantities exactly as well.
* The fluid may be split, the field may not: it "should be updated in an
  unsplit manner in order to exactly maintain the divergence-free
  constraint" (ApJ p. 320).
* No divergence value is printed; exactness of the face invariant is
  stated for all runs. The EMF construction is on
  [flux-CT](/methods/flux-ct.md).
* **Does exactness matter if conservation holds?** On a Mach-15
  shock–cloud problem the same conservative scheme with and without the
  field update gives solutions "not significantly different", differing in
  small scales where the uncontrolled run has its largest net cell flux
  (ApJ §3, Figs. 12–18). The authors leave the question open ("unable to
  and do not intend to fully answer" it, JCP §5). One problem, visual
  comparison only.

**The flux-CT primary source.**
[Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md) motivate the
combination by a duality: the magnetic components of a Godunov scheme's
face fluxes are upwinded electric-field values, so the edge EMF can be
assembled from them directly. On a rotor, a low-$\beta$ blast and an
oblique Alfvén wave they find the staggered scheme as robust and accurate
as a cell-centred Godunov scheme with divergence cleaning. The same
cell-centred scheme without cleaning fails on the rotor, with undivided
divergence-to-field ratios of $\pm0.66$ (§3, Fig. 3e). No divergence
measure of the CT runs is reported.

**The transport-flux primary source.**
[Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md) put CT into a
second-order Harten-TVD code, contemporary with Dai & Woodward and before
Balsara & Spicer. In their account earlier CT codes were
artificial-viscosity based, and staggering was "unnatural" for
Riemann-solver schemes until Dai & Woodward (1998) (§1).
* $B_h \in V_h^2$ on faces is the evolved field; the cell-centred field is
  the two-face average, recomputed each step (eqs. 3–4).
* $E_h$ at each edge is averaged from two TVD fluxes per direction, each
  the central average of the advective product plus the full seven-wave
  TVD dissipation of the field component (eqs. 6–7, 15).
* The face update $B_h^{n+1} = B_h^n - \Delta t\, C_h E_h$ (eqs. 16–17)
  gives an exactly zero net face flux per cell at $n+1$ if it was zero at
  $n$ (eq. 18).
* No projection and no source term are used. Dropping the code's earlier
  Poisson cleaning made it about 20% faster
  ([projection](/methods/projection-method.md)).
* No divergence value is reported in any test; exactness rests on eq. 18.

Details of the EMF are on [flux-CT](/methods/flux-ct.md). This is the
second-order CT step that [Seo & Ryu (2023)](/sources/seo-2023.md) find
caps a fifth-order WENO code (above).

[Tóth (2000)](/sources/toth-2000.md) further proves that these CT variants
are algebraically *identical* to pure finite-volume schemes on the
cell-centered field, conserving a corner-centered divergence
$D_h^{\mathrm{k}} B_h$ exactly —
[CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md).
The constraint mechanism of this family is therefore not staggering per se
but the symmetrized, once-per-edge assembly of the EMF; the staggered and
collocated formulations are two representations of one scheme, each exact in
its own divergence stencil.

**Unstaggered CT via the potential.** A second collocated line evolves a
collocated potential and replaces the predicted field with its central
curl, which holds $D_h^{\mathrm{c}} B_h = 0$. It runs from Tóth and Rossmanith
at second order to fourth order in
[Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md). See
[vector-potential evolution](/methods/vector-potential-evolution.md).

# Examples

Evans & Hawley calibrate CT against three vector-potential codes on Cartesian
square-wave advection, radial accretion onto a Schwarzschild hole, closed
field-loop infall, and accretion-disk formation; the divergence diagnostic
holds at $\sim 10^{-15}$ (double precision) through all runs.
In [Tóth (2000)](/sources/toth-2000.md)'s ten-problem shock-capturing
comparison, flux-CT ranks among the three most accurate and reliable schemes.
In production, CT runs on tree-based (octree) AMR in RAMSES-MHD with
2D-Riemann edge EMFs ([Fromang et al. (2006)](/sources/fromang-2006.md)),
in fourth-order ADER-WENO finite volume for special-relativistic MHD with
edge fields from a multidimensional (MuSIC) Riemann solver
([Balsara & Kim (2016)](/sources/balsara-kim-2016.md); no divergence
diagnostic is reported there),
and in Athena via unsplit CTU with the upwind-biased $\mathcal{E}^c$ EMF
([Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md)) — where
dimensional splitting is ruled out on principle (the constraint couples
all field components, so they must update together), and the scheme
reduces exactly to its 1D form for grid-aligned flow. The Athena code paper
([Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md)) documents the implementation, the second unsplit option VL+CT, and
two cautions: 1D tests cannot reveal divergence errors, since there the
normal field is simply constant, and the face-centred discretization is
argued to be the consistent one because it conserves the flux, the
cell-integrated monopole density, of every cell.

**The integrator.** Athena's unsplit CTU is Colella's [corner transport upwind](/methods/corner-transport-upwind.md) ([Colella (1990)](/sources/colella-1990.md)), a pure-hydrodynamics integrator with no divergence property of its own.

# Citations

1. [Evans & Hawley (1988)](/sources/evans-hawley-1988.md), §II–V.
2. [Tóth (2000)](/sources/toth-2000.md), §4, §7.
3. [Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md), §3–4.
4. [Fromang et al. (2006)](/sources/fromang-2006.md), §2.
5. [Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), §§3–4.
6. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.1, 2.3, Appendix A.
7. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §§1, 3, 6.
8. [Jones, McNally & Reynolds (2026)](/sources/jones-2026.md), §§4, 8.
9. [Seo & Ryu (2023)](/sources/seo-2023.md), §§1, 2.3, 3.1–3.2, 3.6.
10. [Stone, Gardiner, Teuben, Hawley & Simon (2008)](/sources/stone-2008.md), §§1, 3, 5–6, 8.
11. [Balsara & Kim (2016)](/sources/balsara-kim-2016.md), §§1, 4.
12. [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), §§1, 3, Fig. 3.
13. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §§1–2, eqs. 3–18.
14. [Colella & Woodward (1984)](/sources/colella-woodward-1984.md), §1.
15. [Jiang & Shu (1996)](/sources/jiang-shu-1996.md), §§2, 4.
16. [Dai & Woodward (1998, JCP)](/sources/dai-woodward-1998.md), §§1–3.2, 5, eqs. 18–28, 52.
17. [Dai & Woodward (1998, ApJ)](/sources/dai-woodward-1998-b.md), §§1–3, eqs. 15–27, Figs. 12–18.
18. [Shu & Osher (1989)](/sources/shu-osher-1989.md), Alg. 2.2, eqs. 2.12, 4.3–4.4.
19. [Colella (1990)](/sources/colella-1990.md), §6.
