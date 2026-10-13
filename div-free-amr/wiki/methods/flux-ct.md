---
type: Method
title: "Flux-CT and the Godunov CT variants"
description: "Constrained transport driven by a shock-capturing base scheme: corner EMFs assembled from upwind fluxes (flux-CT) or interpolated fields (field-CT)."
status: established
aliases: [flux-interpolated CT, field-interpolated CT, transport-flux-CT]
tags: [constrained-transport, godunov, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Flux-CT and the Godunov CT variants

The family of schemes combining [constrained transport](/methods/constrained-transport.md)
with conservative shock-capturing (Godunov-type) base schemes: the corner/edge
EMF $E_h$ is assembled from base-scheme data, then the staggered field is
updated by the standard CT circulation, preserving $D_h^{\mathrm{f}} B_h$
([notation](/notation.md)) to roundoff. The variants, as catalogued by
[Tóth (2000)](/sources/toth-2000.md) §4 (primary sources ingested for flux-CT,
[Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), and for
transport-flux-CT, [Ryu et al. (1998)](/sources/ryu-1998.md); field-CT not
yet ingested):

* **Field-interpolated CT** (Dai & Woodward): interpolate cell-centered
  $\mathbf{v}$ and $\mathbf{B}$ (two time levels, four cells) to the corner
  and form $E_h = -\bar{\mathbf{v}}\times\bar{\mathbf{B}}$ there.
* **Flux-interpolated CT** (Balsara & Spicer): average the four
  appropriately-signed upwind magnetic-field fluxes of the base scheme
  adjacent to the corner,
  $$E_h\big|_{j+\frac12,k+\frac12} = \tfrac14\left(-f^{x,*}_{j+\frac12,k} - f^{x,*}_{j+\frac12,k+1} + f^{y,*}_{j,k+\frac12} + f^{y,*}_{j+1,k+\frac12}\right),$$
  inheriting the base scheme's upwinding in the EMF.
* **Transport-flux-interpolated CT** (Ryu, Miniati, Jones & Frank): as
  flux-CT but averaging only the *transport part* of the upwind fluxes, with
  weight $\tfrac12$; coincides with the base scheme for 1D slab-symmetric
  problems.

**Flux-CT in its primary source**
([Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md) §2.1). The face
field $B_h \in V_h^2$ is an area-weighted face average and $E_h \in V_h^1$
sits at edge centres. The magnetic components of the Godunov face fluxes
are electric-field values (their eqs. 4–6), so the formula above is their
eq. 9, the plain average $\mathcal{E}^\circ$; eqs. 7–8 give the other two
edge orientations in 3D. The fluxes are second order and time-centred at
$t^{n+1/2}$. Faces are then updated by a discrete Stokes theorem with edge
lengths and face areas (eqs. 13–15), in registry form
$B_h^{n+1} = B_h^n - \Delta t\, C_h E_h^{n+1/2}$.
* **Two cell-centred fields.** Each step starts by interpolating $B_h$ to
  cell centres. The base scheme then advances that cell-centred field with
  its own fluxes (eqs. 10–12), giving $B_h^{*}$, which at the end of the
  step differs from the cell average of the new $B_h$ by discretization
  error. An optional step replaces the magnetic energy of $B_h^{*}$ in the
  total energy by that of the face average (eq. 16), for pressure
  positivity at low $\beta$
  ([positivity–divergence coupling](/results/positivity-divergence-coupling.md)).
* **Scope as printed.** Eqs. 7–9 hold for uniform zoning; on varying zone
  sizes "the averaging should be viewed as a reconstruction step". An
  unsplit base scheme accumulates all edge contributions at once; a
  multi-stage scheme applies eqs. 7–9 at every stage. Above second order
  eqs. 7–9 must change, and finite-volume schemes also need a higher-order
  edge quadrature in eqs. 13–15, left to later work (pp. 275–278).

**The shock-switched variant** (Balsara & Spicer §2.2, eqs. 17–26). Two
switches are evaluated on the four cells around an edge: summed pressure
jumps above half the minimum pressure, and a velocity divergence more
negative than a tenth of a fast-speed bound. Where both fire, $E_h$ is a convex combination of the
average of the two $x$-face fluxes and the average of the two $y$-face
fluxes, weighted by the share of the $x$ pressure jump in the summed jumps.
Elsewhere the weight is $\tfrac12$ and eq. 9 is recovered. The target is
standing magnetosonic shocks aligned with the grid. On all the paper's
tests, which have moving shocks, the variant is "practically identical" to
the basic scheme, and no standing-shock test is shown. These are the
"shock-sensing switches" that
[Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) credit with
restoring the upwind bias.

**Transport-flux CT in its primary source**
([Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md) §2, eqs. 3–18).
The scheme puts the staggered field into an existing second-order
Harten-TVD code, replacing its explicit Poisson cleaning.
* **Placement.** $B_h \in V_h^2$ on faces is the evolved field. The
  cell-centred field fed to the TVD step is the two-face average (eqs.
  3–4), recomputed from the faces every step rather than advanced
  separately (contrast the two cell-centred fields of Balsara & Spicer
  above).
* **The "transport part".** On an $x$-face the flux used for the EMF is the
  central average of the advective product, the transverse field times the
  normal velocity, plus the full seven-wave TVD dissipation of that field
  component; the $y$-face analogue uses the other product (eqs. 6–7). The
  other term of the induction flux "causes no problems" and is left out
  (p. 246).
* **Edge EMF.** $E_h$ at each edge is the plain average of the two such
  fluxes in each direction, hence the weight $\tfrac12$ (eq. 15), "a
  simple arithmetic average, which still keeps second-order accuracy".
* **Update and invariant.** Faces are updated by
  $B_h^{n+1} = B_h^n - \Delta t\, C_h E_h$ (eqs. 16–17), so the net face
  flux of every cell is zero at $n+1$ "if it is zero at step $n$" (eq. 18):
  $D_h^{\mathrm f}$ is preserved, not imposed. The field update is unsplit
  and follows Strang-split fluid sweeps. No projection or source term is
  used, and no divergence value is reported in any test.
* **1D reduction, as claimed.** On grid-aligned 1D problems the 2D code
  reproduces the 1D code exactly; "with Dai & Woodward's (1998) advective
  fluxes, that is not necessarily true" (pp. 246–247). The authors call the
  class "method of characteristics, constrained transport" (MoCCT, §4).

*Compiler reading:* the halved viscosity that
[Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) find (below) is
derived for the four-flux average of Balsara & Spicer. Ryu et al. average
two transport fluxes per direction and assert exact 1D reduction without
analysing the dissipation, so the two statements concern different
constructions and do not conflict on their face. Likewise, Tóth's report
that transport-flux-CT needs limiter changes to run some 2D tests concerns
the variant as run inside his comparison; the original Harten-TVD code ran
its own 2D tests (diagonal shock tubes, Orszag–Tang, clouds, a jet) with no
limiter change reported. Different implementations and tests, so a
qualification, not a contradiction.

## Properties

* Constraint mechanism identical to CT: once-per-edge EMF, two-face use with
  opposite signs.
* Each variant is exactly a pure finite-volume scheme on the cell-centered
  field — see [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md);
  the price of divergence preservation is flux averaging over a wider stencil
  than the base scheme.
* In [Tóth (2000)](/sources/toth-2000.md)'s ten-problem comparison, flux-CT is
  among the three most accurate and reliable schemes; field-CT is the least
  accurate CT variant; transport-flux-CT fails to run some 2D tests without
  limiter changes.

The averaging step is the family's acknowledged weak point and was later
superseded twice over: by genuinely two-dimensional four-state upwind EMFs
([Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md)), and
by direct evaluation of the EMF at zone edges from the multidimensional
Riemann data, with second/third-order unsplit time integration
([Balsara (2004)](/sources/balsara-2004.md) §2 — resolving his "Issue 4").
A later step in the same line takes the edge field from the vertex fluxes
of a genuinely two-dimensional (MuSIC) Riemann solver: the edge value of
$E_h$ is the mean of the sign-reversed seventh component of the $x$ vertex
flux and the sixth component of the $y$ vertex flux, in
special-relativistic MHD. Its authors claim this removes any need to double
the dissipation of the electric field and avoids Gardiner and Stone's
objections. No test in that paper checks the claim
([Balsara & Kim (2016)](/sources/balsara-kim-2016.md) §§1, 4.2).

**Why plain averaging fails, quantified.**
[Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md) §§2.3–3.2 make
the coupling exact and the defect measurable.
* **The coupling.** Defining the cell-centered field as the mean of its two
  faces forces the finite-volume flux of each cell-centered component to
  equal the average of the two adjacent corner EMFs. The CT EMF is the
  corrector of the Riemann flux, not a separate quantity.
* **The defect.** Under that coupling the arithmetic four-face average
  reproduces the 1D flux of a grid-aligned flow with its numerical viscosity
  **halved**, so the scheme no longer reduces to its own 1D solver.
* **The remedy.** Treat the corner EMF as an integration from the face
  centers with an estimated derivative. Every such choice reduces exactly
  to the 1D solver; the choices differ only in multidimensional
  dissipation:
  * $\mathcal{E}^\alpha$, Lax–Friedrichs: diffusive;
  * $\mathcal{E}^\circ$, not upwinded: oscillatory. At first order it equals
    the [upwind-CT](/methods/upwind-constrained-transport.md) EMF;
  * $\mathcal{E}^c$, upwinded by the sign of the mass flux, so independent
    of the Riemann solver: the choice carried into the 3D
    [Athena scheme](/sources/gardiner-stone-2008.md).

**The dissipation of the average: a qualification.** Balsara & Spicer
(p. 276) state that, since $E_h$ "is not a quantity that we evolve in
time", interpolating the fluxes "does not introduce any significant level
of numerical diffusion in the time evolution of the magnetic field". No
analysis or test supports the statement. Gardiner & Stone find the
opposite defect in the same average: the numerical viscosity of a
grid-aligned flow is halved, which is too little dissipation, not too much.
The two statements point in opposite directions and are not incompatible.
Balsara & Spicer's own §2.2 switches act precisely on grid-aligned shocks,
the case where the halving matters, and changed nothing on their
moving-shock tests. Likewise, "inheriting the base scheme's upwinding"
above is Balsara & Spicer's own description ("properly upwinded fluxes");
Gardiner & Stone show that the average does not reduce to the 1D upwind
flux.

**The second-order ceiling of $\mathcal{E}^c$**
([Felker & Stone (2018)](/sources/felker-2018.md) §4). Three of the four limits are
replaceable: the second-order Taylor estimate of the corner EMF, the
midpoint face EMFs, and the face-average definition of the cell field. The
fourth is structural. The upwinded slopes difference a 1D Riemann flux
against a cell-centered reference $E$, so only a dimensionally split
approximation of the corner Riemann fan is captured, and that difference
caps the order at two. A fourth-order CT therefore has to change
construction, to [upwind CT](/methods/upwind-constrained-transport.md),
rather than raise the order of $\mathcal{E}^c$. The authors also note that
later literature has misidentified $\mathcal{E}^\circ$ as the final GS05
scheme.

**A comparison of the averaging family**
([Mignone & Del Zanna (2021)](/sources/mignone-2021.md)). The paper renames the 2D EMF
recipes: arithmetic averaging, "CT-Contact" (the $\mathcal{E}^c$ above),
and "CT-Flux" (the dissipative terms doubled, as used by Minoshima et al.
in high-order FD). It compares them with UCT schemes under one base scheme.
* **Arithmetic averaging fails.** It has too little dissipation: a
  checkerboard instability in the 3D field loop, and pressure fixes on
  Orszag–Tang. With a third-order Roe base scheme on Orszag–Tang, both
  arithmetic averaging and CT-Flux failed outright.
* **The other two are viable.** CT-Contact and CT-Flux are "an efficient
  and valid option, although not strictly compliant with the UCT
  formalism". The authors agree with Felker & Stone that CT-Contact is at
  most second order, and call its contact-mode selection rule empirically
  supported only.
* **Their dissipation is inherited.** On a Harris-sheet equilibrium,
  CT-Contact reconnects early with a Roe base solver but stays nearly ideal
  with HLLD. Roe diffusion carries pressure and field jumps into the EMF;
  HLLD diffusion carries field jumps only. UCT-HLLD behaves the same with
  either solver.
* **Conclusion:** "the choice of the emf averaging scheme is as crucial as
  the choice of the interface Riemann solver".

**The monopole objection.**
[Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md) §2.4
argue that a second weakness sits outside the EMF. These variants evolve
staggered data but feed *cell-centered averages* into the momentum and
energy fluxes. The orthogonality defect of the Lorentz force is then
governed by $D_h^{\mathrm{c}}$ of the averaged field, not by the exactly
held staggered divergence, and that residual is $O(1)$ wherever the field's
parallel derivative jumps. Numerical monopoles therefore arise despite exact
CT. The two views do not conflict:
* Tóth's equivalence says *which* divergence these schemes hold
  ($D_h^{\mathrm{k}}$);
* Londrillo & Del Zanna say *which* divergence the momentum flux sees,
  which is a different stencil.

Their remedy, [upwind constrained transport](/methods/upwind-constrained-transport.md),
puts the staggered components into every flux.

# Citations

1. [Tóth (2000)](/sources/toth-2000.md), §4.2–4.4, §6–7, Table IX.
2. [Balsara (2004)](/sources/balsara-2004.md), §2.
3. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.2.1, 2.4, Table 3.
4. [Gardiner & Stone (2005)](/sources/gardiner-stone-2005.md), §§2.3, 3.2, 3.3.
5. [Felker & Stone (2018)](/sources/felker-2018.md), §4, Appendix A.
6. [Mignone & Del Zanna (2021)](/sources/mignone-2021.md), §§3, 6.
7. [Balsara & Kim (2016)](/sources/balsara-kim-2016.md), §§1, 4.2.
8. [Balsara & Spicer (1999)](/sources/balsara-spicer-1999.md), §§2.1–2.2, eqs. 4–26, pp. 275–280.
9. [Ryu, Miniati, Jones & Frank (1998)](/sources/ryu-1998.md), §§1–2, 4, eqs. 3–18.
