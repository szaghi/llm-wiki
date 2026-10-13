---
type: Method
title: "Constrained transport for high-order capturing schemes (MHD)"
description: "Keeping the magnetic field discretely divergence-free alongside a high-order capturing scheme: the unstaggered vector-potential variant (evolve A on the cell mesh, set B as its discrete curl), Yee-staggered variants (face fields updated by edge electric fields from a multidimensional Riemann solver, from upwind CT, or from high-order staggered differences of WENO fluxes), and the related projection and trace-projection treatments."
status: established
aliases: [CT, unstaggered constrained transport, vector-potential constrained transport, Yee mesh, divergence-preserving update, upwind constrained transport, UCT, high-order CT]
tags: [mhd, divergence-free, constrained-transport, involution]
timestamp: 2026-10-13T00:00:00Z
---

# Constrained transport for high-order capturing schemes

$\nabla\cdot\mathbf B = 0$ is an involution: preserved by the exact
evolution, but discretizations of the transport equation alone
accumulate divergence errors. These produce an unphysical force along
$\mathbf B$ and often crash the code. The options are the eight-wave
method, projection, hyperbolic divergence cleaning and constrained
transport ([Christlieb et al. (2016)](/sources/christlieb-2016.md), §1;
[Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §1).
Several constrained-transport designs appear in this corpus, unstaggered
and staggered. The alternatives are [hyperbolic (GLM) cleaning](/methods/hyperbolic-divergence-cleaning.md),
used with cell-centred finite differences and on adaptive meshes,
projection (the earliest), and a projection of reconstructed interface
traces (below). The curl analogue is the
[curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md).

## Unstaggered, vector potential

([Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md),
§§2–6, the original FD-WENO scheme, after Helzel, Rossmanith and Taetz;
[Christlieb et al. (2016)](/sources/christlieb-2016.md), §§2, 4, its
single-step sequel.) Faraday's law with ideal Ohm's law gives
$\partial_t\mathbf A + (\nabla\times\mathbf A)\times\mathbf v = -\nabla\psi$;
the Weyl gauge $\psi = 0$ is stable. $\mathbf A$ lives on the same
mesh as the conserved variables. Each step, or each Runge–Kutta stage,
updates the MHD variables (including a provisional $\mathbf B$), updates
$\mathbf A$, and overwrites $\mathbf B$ with the discrete curl of
$\mathbf A$. The fourth-order central curl is exactly divergence-free for
the matching central divergence, because the central operators commute
(2014, §6). Optionally the energy is corrected so the pressure is
unchanged, which sacrifices energy conservation. The 2014 scheme never
applies this correction; the 2016 scheme does, where its positivity
limiter acts.
* *Why Hamilton–Jacobi WENO.* WENO applied to differences of $\mathbf A$
  measures the smoothness of $\nabla\mathbf A$, that is of $\mathbf B$, so
  it controls oscillations in the physical field (2014, §5.1, Fig. 1).
* In 2D only $A_z$ is needed:
  $\partial_t A_z + v_x\partial_x A_z + v_y\partial_y A_z = 0$, a strongly
  hyperbolic Hamilton–Jacobi equation. Treated with HJ technology
  (Lax–Friedrichs Hamiltonian, WENO5 one-sided derivatives), it gives
  $\mathbf B$ with non-oscillatory derivatives; the curl is fourth-order
  central.
* In 3D the $\mathbf A$ system is only weakly hyperbolic and needs
  artificial resistivity: each component gets upwind dissipation in only
  two of the three directions (2014, eqs. 5.16–5.19). A
  smoothness-indicator-gated term of size $O(h^6)$ in smooth regions and
  $O(h)$ at kinks controls field oscillations. Its coefficient is
  between 0.02 and 0.2 (0.1 in the runs) with the 10-stage SSP-RK(10,4) at
  CFL 3.0 (2014, §5.3), and about 0.01 in the single-step 2016 scheme. The
  weak hyperbolicity is an artifact of freezing the velocity, since full
  MHD stays strongly hyperbolic (Helzel et al., cited in 2014, §2.2).
* Without CT the rotated shock tube develops unphysical oscillations
  ([grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md)).
  The [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) run crashes
  at $t = 1.67$ with the 2016 scheme and reaches negative pressure at about
  $t = 4.0$ with the 2014 base scheme. With CT the 2014 scheme runs to
  $t = 30$ (§7.3).

## Yee-staggered, multidimensional Riemann solver

([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–4.)
Every divergence-preserving sub-system has the induction form
$\partial_t\mathbf B + \nabla\times\boldsymbol{\mathcal E} = 0$, with
anti-symmetric fluxes, and Stokes' theorem forces a Yee-type
collocation: face averages $\bar B_x$, $\bar B_y$, $\bar B_z$ updated by
edge averages of $\boldsymbol{\mathcal E}$,
$$\partial_t \bar B_{x;i+1/2,j,k} = -\frac{1}{h_y h_z}\left(h_z\,\bar{\mathcal E}_{z;i+1/2,j+1/2,k} - h_z\,\bar{\mathcal E}_{z;i+1/2,j-1/2,k} + h_y\,\bar{\mathcal E}_{y;i+1/2,j,k-1/2} - h_y\,\bar{\mathcal E}_{y;i+1/2,j,k+1/2}\right),$$
and cyclically (eqs. 3–5, checked on the page image). This preserves the discrete divergence exactly. Edge
fields need upwinding in both transverse directions, which is the role
of the multidimensional Riemann solver. In its 2D LLF limit (signal
speed $S$),
$$\mathcal E^{**}_z = \tfrac14\left(\mathcal E_{z,RU} + \mathcal E_{z,LU} + \mathcal E_{z,LD} + \mathcal E_{z,RD}\right) + \tfrac{S}{2}\left[B_{x,D} - B_{x,U} + B_{y,R} - B_{y,L}\right]$$
(eq. 12, checked on the page image). The four corner fields come from
2D WENO interpolation of cell-centred $\mathcal E_z$, and the jumps from
2D WENO reconstruction of the face fields evaluated at the edge. The
dissipation is thus proportional only to transverse jumps of the
normal field and vanishes as they converge. The HLL version (eqs.
16–20) adds a supersonic limit through a nine-case conditional; it is
preferred for strongly supersonic MHD.

**Mixed FD–FV scheme.** All cell-centred variables follow
[AFD-WENO](/methods/alternative-finite-difference-weno.md); only the
face fields are FV-updated. A pointwise 1D WENO interpolation along each
edge converts point values of $\mathcal E$ to edge averages. No
divergence-free volumetric reconstruction is built, which keeps the
cost low; high-order divergence-preserving AMR remains available. The
same algorithm, unchanged, solves electrodynamics, MHD and relativistic
MHD at orders up to 9.

**Relativistic MHD** ([Balsara & Kim (2016)](/sources/balsara-2016-b.md), §4).
A multidimensional solver built from HLLC/HLLEM pieces works at the
vertices, keeping linear sub-structure of the entropy and Alfvén waves in
the strongly interacting state. The edge field is
$\mathcal E_z = \tfrac12\left(-(f^{**}_x)_7 + (f^{**}_y)_6\right)$, the
mean of two multidimensionally upwinded numerical fluxes. Such solvers
remove any need to double the dissipation in the electric field, as the
earlier HLL-based scheme did (§1; Balsara et al. 2009, below;
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).

**Comparison.** The vector-potential route needs no staggering, which
eases embedding in AMR, but it breaks energy conservation where the
positivity fix acts. The staggered route conserves exactly except in
rare cells, where the first-order PCP fallback adds an energy source
([positivity preservation](/properties/positivity-preserving.md)).

## Staggered, divergence-free reconstruction

([Balsara (2004)](/sources/balsara-2004.md), §§2–3, second order;
[Balsara (2009b)](/sources/balsara-2009-b.md), RK-WENO to fourth order;
[Balsara et al. (2009)](/sources/balsara-2009.md), §§2.3, 4.1, with
[ADER](/methods/ader.md) one-step time stepping;
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md).)
At second order, each face gets four Riemann problems, at points next to
its four edges. Each edge electric field is built from the one-sided
fluxes of the four faces at that single point, which the author stresses
is not a spatial average (Balsara 2004, eqs. 2.10–2.12). With one Riemann
problem per face plus averaging, the pressure of a low-β blast is not
evolved properly (§7.3). The face-normal field
components and their facial moments are WENO-limited within each face.
Imposing $\nabla\cdot\mathbf B = 0$ then fixes a polynomial field
inside the whole zone that is divergence-free to all orders. Some of its
coefficients (for example the cubic terms in a third-order scheme) exist
only because of the constraint. They take part in fluxes and Riemann
problems but not in the time evolution. The face averages are updated
from space–time averages of the edge electric fields, which come from
1D Riemann solutions at the face points nearest each edge, averaged
over the four faces meeting there. With HLL fluxes, doubling the
dissipation bracket when $S_L < 0 < S_R$ gives enough upwinding for the
electric field. The authors attribute the positive pressure in their
low-β [blast problems](/benchmarks/mhd-blast-wave.md) to using this
reconstruction for the zone-centred field
([positivity preservation](/properties/positivity-preserving.md)).

**Hyperbolic divergence cleaning (GLM).** On the space–time adaptive
meshes of [high-order AMR](/methods/high-order-amr.md), the MHD system is
augmented with a scalar that transports divergence errors out of the
domain at a cleaning speed (Dedner et al.; details on
[hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)). A staggered field is not
used ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4; [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2). The rotor then shows none of the spurious
density and magnetic-pressure oscillations reported for Godunov schemes
without divergence treatment ([Dumbser et al. (2013)](/sources/dumbser-2013.md), §4; [MHD rotor](/benchmarks/mhd-rotor.md)).

## Projection (Brackbill–Barnes)

([Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.) After each WENO
update, solve the Poisson equation $\nabla^2\Phi + \nabla\cdot\mathbf B = 0$
(by relaxation) and replace $\mathbf B$ with $\mathbf B + \nabla\Phi$,
which is divergence-free. The paper does not say whether this is done per
Runge–Kutta stage or per step, nor which discrete divergence and gradient
are used. The divergence errors of a high-order scheme are small in
smooth regions but first order across discontinuities. Powell's
eight-wave system is used only for its eigenvectors, without its source
term ([characteristic decomposition](/methods/characteristic-decomposition.md)).
* **Divergence control decides stability.** Without the projection the
  [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) reaches
  negative pressure and fails at $t \approx 3.9$ (eight-wave
  eigensystem) or $t \approx 2.5$ (seven-wave). With it, both run to
  $t = 8$ and agree (§3.4). This parallels the crash without CT reported
  above.
* The rotated [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)
  shows spurious oscillations near the slow rarefaction without the
  projection (§3.1).

## Yee-staggered, upwind CT at fourth order

([Berta et al. (2024)](/sources/berta-2024.md), §4; arXiv v4.) Inside
the [fourth-order finite-volume](/methods/fourth-order-finite-volume.md)
scheme, the edge electric field is the upwind-CT combination of
Londrillo and Del Zanna, generalized by Mignone and Del Zanna. It takes
the transverse velocities and normal fields reconstructed from face
centres to the edge, and the flux and diffusion coefficients of the 1D
Riemann solver (eq. 39), with no multidimensional Riemann solver. A
second difference along the edge, divided by 24, turns the edge-centre
value into the edge average (eq. 40). Coefficients are given for HLL,
HLLC, HLLD and GFORCE, with a new GFORCE average for relativistic MHD
(Appendix B). Beyond a moderate magnetization in 3D blasts the scheme
needs a Balsara–Spicer energy correction (§5.7).

## Staggered finite-difference CT from WENO fluxes

([Seo & Ryu (2023)](/sources/seo-2023.md), §2.4; [HOW-MHD](/software/how-mhd.md).)
With finite-difference WENO, face point values of the normal field are
updated by staggered differences of edge fields of fourth order
(coefficients $\tfrac98$, $-\tfrac1{24}$) or sixth order ($\tfrac{75}{64}$,
$-\tfrac{25}{384}$, $\tfrac{3}{640}$) (eq. 27).
* The edge fields come from the upwinded parts of the 1D WENO fluxes of
  the induction equation along the two transverse directions, plus
  fourth-order interpolated cross terms (eqs. 12–21).
* A plain difference of these fields is not enough, since each combines
  fluxes reconstructed in different directions. They are corrected by
  $\frac{1}{24}$ second differences in the two transverse directions
  (eq. 23).
* The zone-centred field comes from sixth-order interpolation. With
  fourth-order interpolation the scheme converges only at fourth order
  (eq. 30).
* The discrete divergence stays at round-off. On 3D linear waves the
  scheme converges at fifth order with either staggered difference,
  against second order with the original second-order CT
  ([circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)).
  On shock problems the CT order makes no visible difference.

## Projection of reconstructed traces

([Ding & Wu (2024)](/sources/ding-2024.md), §2.3; arXiv v1.) A
cell-local, unstaggered alternative for finite-volume WENO, which
returns only point values at face quadrature nodes. The discrete
divergence is defined from each cell's own interior traces, by quadrature
of the normal components around the cell (eq. 9). The traces of $B_x$ and
$B_y$ are then shifted by cell-wise constants $\mp A^{\mathrm{DDF}}_x$,
$\mp A^{\mathrm{DDF}}_y$ that make this divergence zero. The shift is the
minimum-norm correction (Prop. 2.3), it is $O(h^k)$ for a $k$-th-order
reconstruction, so the order is kept (Thm. 2.7), and it needs no
polynomial and no Poisson solve. It is the key to a provable positivity
result ([positivity preservation](/properties/positivity-preserving.md)).
The paper does not show what happens to a discrete divergence of the
evolved cell averages.

**Later evidence (batch 7).**
* *Same-code comparisons.* At second order in PLUTO, GLM and CT give equal
  normal-field errors on 2D and 3D oblique shock tubes, and the eight-wave
  scheme gives wrong jumps. On a 3D blast at plasma beta $2\times10^{-4}$,
  CT "failed even with a minmod limiter" while EGLM ran
  ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §§4.3, 4.7). In Athena++, CT is the least
  diffusive and the more robust of the two, and the only one free of the
  leakage and time-step artifacts of cleaning ([Tomida et al. (2026)](/sources/tomida-2026.md), §5;
  [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
* *CT's weak point at low β.* When the cell-centred field is a linear
  average of face fields, the thermal-energy error on a circularly
  polarized Alfvén wave at plasma beta $1.98\times10^{-4}$ reaches about
  30%, as large as plain GLM's ([Tomida et al. (2026)](/sources/tomida-2026.md), App. B.3). This is the
  same deficiency the divergence-free reconstruction section credits for
  positive pressures in low-β blasts.
* *Each scheme's own divergence.* In FLASH the staggered USM solver keeps
  its face divergence at machine precision, while its cell-centred central
  divergence is not zero and is comparable to that of the GLM scheme
  ([Derigs et al. (2018)](/sources/derigs-2018.md), §5.3). This is direct evidence for the scoped reading
  recorded under Contradictions: exactness belongs to a stated discrete
  divergence.
* *The 2001 starting point.* The first divergence-free AMR scheme on a
  Yee mesh still takes edge fields as the Balsara–Spicer average of four
  face fluxes; evaluating them without spatial averaging is the 2004
  change. It argues for staggered over zone-centred CT because the latter's
  control volumes do not tile the mesh, align with refinement patches or
  nest for multigrid ([Balsara (2001)](/sources/balsara-2001.md), §§II–III;
  [divergence-free reconstruction](/methods/divergence-free-reconstruction.md)).

**Later uses (batch 11): the Balsara–Spicer origin.**
([Balsara & Spicer (1999)](/sources/balsara-1999.md), §§1–4.) The scheme
that the batch-7 paragraph and Berta et al. refer to.
* *Flux–electric-field duality.* With
  $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$, the induction rows
  of the directional fluxes are electric-field components: component 7 of
  the $x$-flux is $-\mathcal E_z$ and component 6 of the $y$-flux is
  $\mathcal E_z$, and cyclically (eq. 6; components counted in
  $(\rho, \rho\mathbf v, E, \mathbf B)$, as for $(f^{**}_x)_7$ above).
  So the upwinded, time-centred Godunov fluxes at face centres already
  carry upwinded electric fields.
* *Edge field.* Each edge field is the arithmetic mean of the four face
  fluxes around the edge (eqs. 7–9),
  $$\bar{\mathcal E}^{n+1/2}_{z;i+1/2,j+1/2,k} = \tfrac14\left[(\hat f_y)_{6;i,j+1/2,k} + (\hat f_y)_{6;i+1,j+1/2,k} - (\hat f_x)_{7;i+1/2,j,k} - (\hat f_x)_{7;i+1/2,j+1,k}\right],$$
  called the most compact second-order edge representation on a uniform
  mesh. The paper claims the averaging adds no significant numerical
  diffusion, because $\boldsymbol{\mathcal E}$ is not an evolved quantity
  (p. 276); this is asserted, not measured. The later HLL constructions
  above, which evaluate edge fields without spatial averaging or double the
  dissipation bracket (Balsara 2004; Balsara et al. 2009), and the
  multidimensional Riemann solvers react to this averaged baseline. Their
  statements concern specific HLL constructions, so this is recorded as
  context, not as a contradiction.
* *Face update.* The discrete Stokes law of the Yee section above, applied
  over one step with the time-centred edge fields (eqs. 13–15), keeps the
  face-flux divergence at round-off. This is the Yee side of the closed
  contradiction below; the paper does not claim staggering is necessary.
* *Dual storage and the energy correction.* The zone-centred field is
  also evolved by the Godunov scheme; optionally the magnetic energy of
  that field is replaced, inside $E$, by that of the face fields averaged
  to the zone centre (eq. 16). This costs energy conservation at the level
  of the discretization error and is meant for very low β. It is the
  "Balsara–Spicer energy correction" of Berta et al.
* *An early multidimensional upwinding.* A variant (§2.2) weights the two
  flux pairs by the share of each direction in the local pressure jump,
  where pressure-jump and compression switches detect a strong shock, and
  uses $\tfrac12$ each elsewhere. It targets standing grid-aligned
  magnetosonic shocks, but gave results "practically identical" to the
  basic scheme on every test shown.
* *Time stepping.* Edge fields are accumulated over dimensional sweeps of
  a second-order TVD scheme, but the method does not depend on sweeping:
  an unsplit scheme uses one step, and Shu–Osher multi-stage schemes apply
  the average at every stage. Above second order the average must change,
  and finite volume needs a Simpson-rule edge integral (p. 278).
* *Evidence.* Without CT or cleaning, the zone-centred scheme forms
  divergence errors at the edge of the [MHD rotor](/benchmarks/mhd-rotor.md),
  while on the strong [blast](/benchmarks/mhd-blast-wave.md) it stays
  "very similar". With upwinded fluxes the staggered scheme is as robust as
  the zone-centred scheme with cleaning, against the earlier view, which
  the authors trace to artificial-viscosity schemes (§§3.2, 4).
  Projection is called fast with multigrid or FFT but not adaptable to all
  boundary conditions and zonings (§1).

**Later uses (batch 15).** *The Brackbill–Barnes note*
([Brackbill & Barnes (1980)](/sources/brackbill-1980.md), pp. 426–430).
* *The parallel force.* The introduction's "unphysical force along
  $\mathbf B$" is this note's argument. With a nonzero discrete divergence,
  the conservative magnetic force, the divergence of the Maxwell stress,
  has a dot product $\vert\mathbf B\vert^2\,\nabla\cdot\mathbf B$ with
  $\mathbf B$ (eq. 8). Its effect relative to the flow grows as the flow
  slows against the Alfvén speed. In the note's only test, a uniform
  plasma at beta $1.3\times10^{-8}$ in a uniform field, an implicit 2D
  Lagrangian code with conservative momentum develops flow along
  $\mathbf B$ that "eventually inverts cells and terminates the
  calculation" (Fig. 1).
* *What the note says about projection.* The page heading "Projection
  (Brackbill–Barnes)" follows the usage of later sources. The note states
  the continuous projection, $\nabla^2\Phi + \nabla\cdot\mathbf B = 0$ and
  $\mathbf B \leftarrow \mathbf B + \nabla\Phi$, with the registry's sign
  convention, in one sentence (p. 428), together with formulating MHD "in
  terms of fluxes for which $\nabla\cdot\mathbf B = 0$ automatically". It
  gives no discrete divergence, gradient or Laplacian, no solver, no
  boundary condition and no projection run; the remark above that Jiang
  and Wu leave the discrete operators open applies to the note as well.
  Relaxation, multigrid, FFT, cost and boundary adaptability are not
  discussed in it: those statements are Jiang and Wu's and Balsara and
  Spicer's.
* *The remedy it proposes instead.* Difference the momentum equation in
  nonconservative ($(\nabla\times\mathbf B)\times\mathbf B$) form, and keep the induction
  equation (without the $\mathbf v(\nabla\cdot\mathbf B)$ term) and the
  energy equation in conservation form. Energy and magnetic flux are then
  conserved, momentum only to truncation error, and the parallel force
  vanishes for any divergence (eqs. 9–10). In the same test the mesh stays
  undistorted after 300 transit times, with a kinetic energy "only 1/4000"
  of the conservative run's (Fig. 2). The note judges exact conservation
  form "imperative only for high-speed flows" with shocks (p. 427). This is
  a non-conservative treatment, not a projection; calling projection "the
  earliest" option is a statement about naming, not about what this note
  tested.

## Contradictions

* *Robustness of CT against cleaning:* recorded as open on the
  [GLM cleaning page](/methods/hyperbolic-divergence-cleaning.md)
  (Mignone & Tzeferacos 2010 against Tomida et al. 2026).

**Does exact divergence preservation require a staggered (Yee) mesh?**
*Closed by human fiat (2026-10-08).*
* [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §1: keeping the
  magnetic field divergence-free "requires the use of a staggered,
  Yee-type mesh"; "any divergence-free formulation of MHD requires the
  use of a Yee-type mesh". [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md),
  §§1–4, derive the Yee collocation from Stokes' theorem.
* [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md),
  §§1, 6, and [Christlieb et al. (2016)](/sources/christlieb-2016.md):
  unstaggered CT keeps the central discrete divergence of the cell-centred
  field exactly zero, and Tóth showed that staggering is unnecessary.
* *Compiler's note on scope, not a resolution:* the two sides use
  different discrete divergences, a face-flux (Stokes) one and a central
  difference of point values. Each scheme keeps its own exactly zero.
  Whether the claims conflict depends on which divergence "divergence-free"
  means, which neither side states in that form.
* **Closed by human fiat (2026-10-08): both claims hold, each for its own
  discrete divergence.** The Yee requirement is right for the face-flux
  (Stokes) divergence; unstaggered CT is right for the central divergence
  of cell-centred values. Both designs are kept as valid alternatives.
  *Fiat closure — `status: hypothesis` attribution: the closure is the
  human's judgment, not a source superseding a source; a later source can
  reopen it.*

# Citations

1. [Christlieb et al. (2016)](/sources/christlieb-2016.md), §§1, 2, 4, 6.
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–5 (eq. 12 read from the page image).
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §§2.3, 4.1, 7.
4. [Dumbser et al. (2013)](/sources/dumbser-2013.md), §4.
5. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §6.2.
6. [Jiang & Wu (1999)](/sources/jiang-1999.md), §§1, 3.1, 3.4.
7. [Christlieb, Rossmanith & Tang (2014)](/sources/christlieb-2014.md), §§1–7 (arXiv v2).
8. [Balsara (2004)](/sources/balsara-2004.md), §§1–3, 7.3.
9. [Balsara (2009b)](/sources/balsara-2009-b.md), §§2–3 (author manuscript).
10. [Balsara & Kim (2016)](/sources/balsara-2016-b.md), §§1, 4.
11. [Berta et al. (2024)](/sources/berta-2024.md), §§4, 5.7, Appendix B (arXiv v4).
12. [Seo & Ryu (2023)](/sources/seo-2023.md), §§2.4, 3.
13. [Ding & Wu (2024)](/sources/ding-2024.md), §2.3 (arXiv v1).
14. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §§4.3, 4.7.
15. [Tomida et al. (2026)](/sources/tomida-2026.md), §5, App. B.3.
16. [Derigs et al. (2018)](/sources/derigs-2018.md), §5.3.
17. [Balsara (2001)](/sources/balsara-2001.md), §§II–III.
18. [Balsara & Spicer (1999)](/sources/balsara-1999.md), §§1–4 (eqs. 7–9, 13–15, 17–26 read from the page images).
19. [Brackbill & Barnes (1980)](/sources/brackbill-1980.md), pp. 426–430, Figs. 1–2 (read from page images).
