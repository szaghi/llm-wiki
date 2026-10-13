---
type: Method
title: "Constrained transport"
description: "Staggered discretization of the induction equation: face-area-averaged magnetic field updated from edge-centred EMFs, which keeps the discrete divergence of each cell at its initial value to round-off; production codes build the edge EMFs from the face Godunov fluxes (Gardiner–Stone upwind construction or Balsara–Spicer averaging) and, on AMR, add area-weighted restriction, divergence-free prolongation and an EMF correction at coarse–fine edges."
status: established
aliases: [CT, upwind constrained transport, staggered-mesh constrained transport, face-centred constrained transport, MHD-CT]
tags: [mhd, constrained-transport, amr, conservation, gpu]
timestamp: 2026-10-13T00:00:00Z
---

# Constrained transport

Constrained transport (CT) evolves $\mathbf B$ from the induction equation
$\partial_t\mathbf B + \nabla\times\boldsymbol{\mathcal E} = 0$, $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$,
on a staggered mesh. Four codes in this bundle use it:
[Athena](/software/athena.md), [Athena++](/software/athena-plus-plus.md),
[Enzo](/software/enzo.md) (its MHD-CT solver) and [GAMER](/software/gamer.md).
[PLUTO](/software/pluto.md) has CT on static grids but not in its AMR
version (below).

## Staggering and what is preserved

* $\rho$, $\rho\mathbf v$ and $E$ are cell-centred volume averages. Each
  component of $\mathbf B$ is an area average on the faces normal to it.
  The EMF components are time- and line-averaged on cell edges
  ([Stone et al. (2008)](/sources/stone-2008.md), §3, eqs. 16–24;
  [Zhang et al. (2018)](/sources/zhang-2018.md), §3.1, eqs. 10–15, Fig. 1;
  [Bryan et al. (2014)](/sources/bryan-2014.md), §4.3).
* The CT difference equations keep the cell-volume-averaged divergence of
  the face field exactly at zero. Equivalently, they conserve the magnetic
  flux through each cell (Stone et al. 2008, §3, eq. 25). Zhang et al.
  write it as $(\nabla\cdot\mathbf B)^{n+1}_{i,j,k} = (\nabla\cdot\mathbf B)^{n}_{i,j,k}$ (eq. 16).
  Bryan et al. state machine-precision preservation and add that
  monopoles from other sources, such as ill-posed initial conditions,
  persist (§4.3).
* The cell-centred field used by the Riemann solvers is the arithmetic
  mean of the two face values (Stone et al. 2008, eqs. 26–28; Bryan et
  al. 2014, §4.3). Enzo's update has four steps: Riemann problem with the
  cell-centred field, edge EMF from the fluxes, curl update of the face
  field, re-averaging to the cell centre (Bryan et al. 2014, §4.3).
* The staggered field makes the ghost zone one cell wider than for pure
  hydrodynamics in GAMER (Zhang et al. 2018, §3.1).
* Stated cost of the design: face-centred CT "complicates the
  implementation of the algorithm, and the interface to AMR drivers"
  (Stone et al. 2008, §3.2).

## Edge EMFs from face fluxes

The Godunov fluxes of the induction equation give EMFs at face centres;
CT needs them on edges.
* **Upwind-gradient construction (Gardiner & Stone 2005).**
  [Stone et al. (2008)](/sources/stone-2008.md) (§5.3, eqs. 79–81) set
  the edge EMF to the arithmetic mean of the four adjacent face-centred
  EMFs plus, in each transverse direction, $h/8$ times the difference of
  two EMF derivatives taken on either side of the edge. Each derivative
  is a one-sided difference to a cell-centre reference EMF computed from
  the cell-centred $\mathbf v$ and $\mathbf B$, e.g.
  $$\left(\partial_y\mathcal E_z\right)_{i,j-1/4} = \frac{2\left(\mathcal E_{z,i,j} - \mathcal E_{z,i,j-1/2}\right)}{h}\qquad\text{(eq. 81)},$$
  and is upwinded by the sign of the contact (mass-flux) velocity at the
  face, with the mean of both sides when that velocity is zero (eq. 80).
  The paper allows different cell sizes per direction. "Simple arithmetic
  averaging does not work for the unsplit integrators adopted here"
  (§5, citing Gardiner & Stone 2005).
* [Athena++](/software/athena-plus-plus.md) uses the upwind CT of
  Gardiner & Stone (2005, 2008) and does not restate the recipe
  ([Stone et al. (2020)](/sources/stone-2020.md), §3.1).
* [Enzo](/software/enzo.md)'s MHD-CT offers the first-order EMF method of
  Balsara & Spicer (1999) and the second-order methods of Gardiner &
  Stone (2005), without naming which Gardiner–Stone variant is used
  ([Bryan et al. (2014)](/sources/bryan-2014.md), §4.3).
* [GAMER](/software/gamer.md) evaluates the edge EMF "from the electric
  field at the cell interface ... together with the magnetic field at the
  cell interface and the velocity at the cell center"; it names no
  variant and does not cite Gardiner & Stone
  ([Zhang et al. (2018)](/sources/zhang-2018.md), §3.2, CTU step 3).
* **Order.** Athena++'s default CT is second order, so the overall error
  stays $\mathcal O(h^2)$ even with PPM reconstruction; a fully
  fourth-order scheme is deferred to Felker & Stone (2018)
  (Stone et al. 2020, §3.2.1).

Inside an [unsplit integrator](/methods/unsplit-godunov-integrators.md)
the edge EMFs are built twice per step. In 2D CTU+CT the in-plane face
fields are first advanced by $\Delta t/2$ with CT for the corrector
states, then the corner EMFs are rebuilt from the second Riemann solve
(Stone et al. 2008, §5.1, steps 3–7, eqs. 74–75; Zhang et al. 2018,
§3.2).

## CT on adaptive meshes

Face- and edge-centred data need their own inter-level operators.
* **Restriction.** Face fields are area-weighted averages of the fine
  faces (Stone et al. 2020, §2.1.5, eq. 3; Zhang et al. 2018, §3.3). In
  Enzo's projection the averaging weight is $r_{\mathrm{ref}}^{-(d-1)}$
  for face-centred and $r_{\mathrm{ref}}^{-1}$ for edge-centred data
  (Bryan et al. 2014, §3.3, eq. 26).
* **Prolongation.** Athena++ uses the divergence-preserving prolongation
  of Tóth & Roe (2002), extended to nonuniform and curvilinear meshes "in
  finite-area fashion", and does not overwrite fine faces that already
  exist (Stone et al. 2020, §2.1.5). Enzo and GAMER use Balsara (2001).
  Enzo interpolates all three face components together and uses the old
  fine field where present (Bryan et al. 2014, §4.3). GAMER's 2D
  illustration interpolates the fine faces lying on coarse faces
  piecewise linearly with the coarse face average preserved, then fixes
  the interior faces with two quadratic polynomials whose 10 coefficients
  come from 7 independent face-matching equations and 3 from requiring
  zero divergence (Zhang et al. 2018, §3.3, Fig. 2, eq. 17).
* **EMF correction.** On an edge shared by coarse and fine blocks,
  Athena++ replaces the coarse EMF so that the coarse EMF times the coarse
  edge length equals the sum of the fine EMFs times their lengths; fine
  edges without a coarse counterpart are unused, and on shared edges the
  fine EMFs are averaged first (Stone et al. 2020, §2.1.4, eq. 1,
  Figs. 7–8). GAMER corrects the coarse face field with the EMF
  differences on coarse–fine "interedges" (Zhang et al. 2018, §3.3).
  Enzo projects the electric field, not $\mathbf B$, from fine to coarse
  and re-updates the parent field with it (Bryan et al. 2014, §4.3,
  citing Balsara & Spicer 1999 and Collins et al. 2010).
* **Shared edges without refinement.** Athena++ also replaces EMFs on
  edges shared by same-level `MeshBlock`s with their arithmetic mean:
  round-off, nondeterministic MPI ordering and non-ANSI optimizations
  otherwise create divergence errors "that CT never removes"
  (Stone et al. 2020, §2.1.4, §2.1.1). The polar boundary likewise
  averages EMFs on radial edges touching the pole (§2.3).
* **Avoiding CT under AMR.** PLUTO's AMR version uses
  [GLM cleaning](/methods/glm-divergence-cleaning.md) only. The stated
  reason is the care the staggered field needs in prolongation and
  restriction at fine–coarse interfaces
  ([Mignone et al. (2012)](/sources/mignone-2012.md), §1, §3, §7).
* In general relativity Athena++ keeps the same CT discretization with
  $\alpha_{\mathrm L}\sqrt{\det\gamma_{ij}}$-weighted lengths, areas and volumes (Stone et al. 2020, §4).

## Evidence

* **[Field-loop advection](/benchmarks/field-loop-advection.md).** Athena,
  2D, 256×128, PLM, Roe: the loop shape is "preserved extremely well";
  with uniform $v_z \ne 0$, $B_z$ stays zero to round-off. In 3D the
  axial component of an inclined loop stays zero to truncation error
  (Stone et al. 2008, §8.4, Fig. 21; §8.6, Fig. 34). Athena++ advects a
  loop through the pole of a spherical-polar grid with the structure
  "well preserved" (Stone et al. 2020, §3.5.2, Fig. 29).
* **[Linear waves](/benchmarks/linear-wave-convergence.md).** CT codes
  converge at second order in all MHD wave families, on oblique 3D grids
  (Stone et al. 2008, §8.6, Fig. 32; Zhang et al. 2018, §5.1(i), Fig. 4)
  and with AMR (Stone et al. 2020, §3.4.1, Fig. 19).
* **ABC field relaxation (GAMER, AMR).** Total energy is conserved to
  machine precision and magnetic helicity to better than 98 % over
  32 crossing times (Zhang et al. 2018, §5.1(v)).
* **[Orszag–Tang](/benchmarks/orszag-tang-vortex.md).** Enzo's CT and
  Dedner solvers give "approximately equal effective resolution"; the
  resolution is not printed (Bryan et al. 2014, §11.2.10, Fig. 14).
* **[MHD blast](/benchmarks/mhd-blast-wave.md).** Athena calls CTU+CT
  "robust for low-β flows" after isothermal runs at plasma beta $\beta_{\mathrm p} = 0.02$
  (Stone et al. 2008, §8.4, Figs. 28–30).

## Later uses (batch 3)

Five more codes use CT: [Cholla](/software/cholla.md),
[IDEFIX](/software/idefix.md), [AthenaK](/software/athenak.md),
[gPLUTO](/software/gpluto.md) (CT or GLM) and
[GRaM-X](/software/gram-x.md) (vector potential on edges).

* **Cholla** ([Caddy & Schneider (2024)](/sources/caddy-2024.md)). Face
  $\mathbf B$ advanced inside the VL+CT integrator; the cell-centred field
  is the arithmetic mean of the two face values (eq. 13), recomputed every
  time it is needed and never stored, because "Cholla is generally limited
  instead by GPU memory" (§2.2.1, §2.3.1). The edge EMF is the mean of the
  four adjacent face values plus derivative terms formed between face
  values and a cell-centre reference
  $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ (eqs. 15–18,
  Fig. 1, "based on Figure 5 of Stone et al. 2008"). The derivatives are
  upwinded by the sign of the face-normal velocity, with the mean of both
  sides otherwise (eq. 16); whether that velocity is the contact
  (mass-flux) velocity of Stone et al. (2008) is not stated. The code
  advances $\mathbf B$ with the electric field rather than the magnetic flux
  with the EMF, which the paper says differ only by factors of unit length
  (§2.2.4). Recorded as printed: eq. 15 adds the two derivative terms in
  each direction and eq. 17 writes its example derivative as face value
  minus reference, the opposite arrangement to Stone et al. (2008), eq. 81,
  above; only one derivative is printed, so whether this is a sign
  convention or a misprint cannot be decided from the text. Stated reasons
  for CT on GPUs: "its overall accuracy, because the algorithm pairs well
  with static structured grids, and because the computational efficiency
  of GPUs is a good match to the algebraic complexity of CT" (§1).
* **IDEFIX** ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.4). Face
  $\mathbf B$ by CT after Evans & Hawley (1988). Edge EMFs from the face
  Riemann fluxes (arithmetic average, or the two Gardiner–Stone 2005 upwind
  variants, the paper's $\mathcal E^\circ$ and $\mathcal E^c$, $\mathcal E^c$ being the default and "similar to
  Athena") or from 2D Riemann solvers at edges (Londrillo & Del Zanna 2004;
  2D HLL and HLLD after Mignone & Del Zanna 2021), selectable at run time.
  The Hall-effect EMF uses the arithmetic average of the fluxes; adding Hall
  to the upwind variant "led to numerical instabilities" (§2.5). This
  qualifies, without contradicting, Stone et al.'s (2008) statement that
  simple averaging "does not work" for their unsplit integrators: IDEFIX
  uses it, with no instability reported, under a method-of-lines
  integrator and the diffusive HLL solver.
* **Vector-potential formulation** (IDEFIX, §2.4, eqs. 7–8). Optionally the
  edge-centred vector potential is advanced by minus the edge EMF and
  $\mathbf B$ is its discrete curl: "mathematically equivalent to the
  original CT algorithm", but round-off no longer accumulates in
  $\nabla\cdot\mathbf B$. Costs: memory for the potential, initial
  conditions coded as a potential, and possible overflow of the potential
  under a large-scale constant EMF, removed by a periodic gauge
  transformation.
* **Round-off growth.** IDEFIX states that with plain CT the divergence
  grows by round-off as the square root of the number of cycles with
  explicit Runge–Kutta, and linearly with Runge–Kutta–Legendre
  [super-time-stepping](/methods/super-time-stepping.md), "potentially
  significant" over billions of steps; it recommends the vector potential
  when super-time-stepping is used on a parabolic MHD term (§2.4, §2.8).
  The growth law is asserted, not shown in a figure. This qualifies "to
  round-off" in the opening section, and matches Athena++'s reason for
  averaging EMFs on shared edges (errors "that CT never removes", above).
* **AthenaK** ([Stone et al. (2026)](/sources/stone-2026.md), §3).
  Face-area-averaged $\mathbf B$, Evans–Hawley CT with the upwinded
  electric fields of Gardiner & Stone (2005, 2008); "the staggered mesh
  version of CT is critical for some problems." How the coarse–fine EMF
  correction is implemented on the device is not described.
* **gPLUTO** ([Rossazza et al. (2026)](/sources/rossazza-2026.md)). CT "in
  the more recent formulation by" Mignone & Del Zanna (2021), the upwind
  "UCT HLLD" average, with Londrillo & Del Zanna (2004) as an origin
  (§2.1, §4.1). The strong-scaling runs switch to
  [GLM cleaning](/methods/glm-divergence-cleaning.md) "because this
  algorithm requires less device memory than the constrained transport
  method", to fit a slightly larger grid; no memory figures are given
  (§4.1).
* **GRaM-X** ([Shankar et al. (2023)](/sources/shankar-2023.md), §III B).
  The vector potential sits on cell edges of AMReX's staggered layout,
  which is said to keep $\nabla\cdot\mathbf B$ zero to round-off "in
  particular near mesh refinement interfaces". The EMF construction, gauge
  and prolongation are not described, and no divergence measurement is
  reported.

Evidence added in batch 3:
* **[Field-loop advection](/benchmarks/field-loop-advection.md), Cholla.**
  Tilted spherical loop in 3D: the maximum divergence stays at about
  $10^{-17}$–$10^{-15}$, "near round off", for the whole run, and the
  zero-field exterior stays near zero (Caddy & Schneider 2024, §3.1.3,
  Fig. 4).
* **[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), IDEFIX.**
  $\vert\nabla\cdot\mathbf B\vert \ll 10^{-12}$ in all runs
  (Lesur et al. 2023, §4.2).
* **[Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
  Cholla.** Second order with VL+CT in 3D (Caddy & Schneider 2024,
  §3.1.2, Fig. 3). gPLUTO runs the same test with CT for weak scaling only,
  without accuracy diagnostics (Rossazza et al. 2026, §4.2).

## Later uses (batch 4)

**Production GRMHD.** The nine codes of the
[EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md) all
"preserve the divergence of the magnetic field to machine precision"
([Porth et al. (2019)](/sources/porth-2019.md), §6), with five
induction schemes (Table 1, §3, §4.1):
* upwind constrained transport (UCT) of Del Zanna et al. (2007): BHAC,
  ECHO (UCT after Londrillo & Del Zanna 2000, 2004);
* staggered upwind CT after Gardiner & Stone (2005):
  [Athena++](/software/athena-plus-plus.md), [H-AMR](/software/h-amr.md);
* staggered CT of Fragile et al. (2012): Cosmos++;
* cell-centred Flux-CT of Tóth (2000): iharm3D, KORAL, and HARM-Noble with
  PPM-reconstructed edge EMFs (Noble et al. 2009);
* vector-potential evolution: IllinoisGRMHD, which reduces to staggered
  Flux-CT on uniform grids and "enables any interpolation scheme to be used
  at AMR refinement boundaries" (§4.1.8).

Athena++ in GR uses the magnetic fluxes at the pole to help build the
edge EMFs of its polar boundary (§4.1.1), as in the polar-boundary EMF
averaging above.

**Arithmetic EMF averaging in production** (App. A). KORAL, following
Gammie et al. (2003), keeps a cell-centred field and averages EMFs
arithmetically (the paper's "ACT"); H-AMR and Athena++ use staggered UCT
after Gardiner & Stone (2005). "In contrast to ACT methods, the UCT scheme
reproduces the correct solution for plane-parallel grid-aligned fields,
however the amount of dissipation of the scheme is effectively doubled."
This is offered as one reason why KORAL's PLM runs stay closer to its PPM
runs; the doubled dissipation is stated, not isolated in a dedicated test.
It qualifies, without contradicting, Stone et al.'s (2008) statement that
simple averaging "does not work" for their unsplit (CTU) integrators: the
averaging codes here use other second-order integrators (KORAL's is
"2nd order", iharm3D's a method-of-lines predictor–corrector), as IDEFIX
does with a method of lines (batch 3, above).

**Staggered fields and floors** (§4.1.2). BHAC with staggered fields needed
floors 10 times higher than with centred fields, because interpolating the
staggered field to cell centres "introduces an additional error"; see
[density and pressure floors](/methods/numerical-floors.md).

## Later uses (batch 6)

[Gardiner & Stone (2005)](/sources/gardiner-2005.md) (arXiv v1 read; 2D
only) is the primary source of the upwind CT that Athena, Athena++,
AthenaK, H-AMR and the IDEFIX default use.

* **Why CT is the representation.** Keeping $\nabla\cdot\mathbf B = 0$
  "in an integral sense" is called "as fundamental as ... the conservation
  of mass in a finite volume method"; cell-centred CT (Tóth 2000) keeps a
  divergence on "a different (larger) stencil" (§2.2). Directional
  splitting is rejected because split updates of the cell-centred field
  "will not generally satisfy the divergence free constraint between
  directional sweeps" (§2.1).
* **Finite-volume–CT consistency** (§2.3, eqs. 21–24). With the cell-centred
  field defined as the mean of the two face values (eqs. 19–20, as in the
  Staggering section above), keeping that definition at $t^{n+1}$ forces
  the finite-volume flux of each transverse cell-centred component to be
  the mean of the two corner EMFs on that face: the $B_x$ component of the
  $y$-flux at face $(i, j+1/2)$ is
  $\tfrac12(\mathcal E_{z,i-1/2,j+1/2} + \mathcal E_{z,i+1/2,j+1/2})$, and
  the $B_y$ component of the $x$-flux at face $(i+1/2, j)$ is
  $-\tfrac12(\mathcal E_{z,i+1/2,j-1/2} + \mathcal E_{z,i+1/2,j+1/2})$.
  The Godunov fluxes of those components are replaced by these averages,
  "regardless of the details of the CT algorithm".
* **Why plain averaging fails** (§3.2.1, eqs. 34–38). With the corner EMF
  equal to the mean of the four face EMFs, a plane-parallel grid-aligned
  flow gives a scheme whose "numerical viscosity is reduced by a factor of
  2", which "does not reduce to the underlying integration algorithm"; "the
  stability of this approach is questionable", for "the lack of a
  directional bias". This is an argument from the discrete equations, not a
  failing run: the paper shows none. It is the reasoning behind Stone et
  al.'s (2008) "does not work" above, and it leaves room for the IDEFIX and
  KORAL uses of averaging recorded in batches 3 and 4, under other
  integrators. Porth et al.'s statement that upwind CT has "effectively
  doubled" dissipation relative to averaging (batch 4) is the same factor
  2 seen from the other side: Gardiner & Stone call the average deficient,
  Porth et al. call upwind CT more dissipative. Gardiner & Stone read
  Balsara & Spicer (1999) as built on this average, with shock-sensor
  weights restoring a directional bias.
* **The upwind construction in the original** (§3.2.2, eqs. 42–51). The
  corner EMF is the mean of the four face EMFs plus $h/8$ times
  differences of EMF derivatives at the quarter points on either side of
  the corner (eq. 42), each a one-sided difference between a face EMF and
  a cell-centre reference EMF. Eq. 46 writes the quarter point on the $+x$
  side of the cell centre as face minus centre,
  $$\left(\partial_x\mathcal E_z\right)_{i+1/4,j} = \frac{2\left(\mathcal E_{z,i+1/2,j} - \mathcal E_{z,i,j}\right)}{h},$$
  where Stone et al. (2008), eq. 81 (above), write the quarter point on the
  $-y$ side as centre minus face; both are the difference in the direction
  of increasing coordinate, so they agree. For the Cholla note in batch 3
  (Caddy & Schneider, eq. 17, face value minus reference): that arrangement
  is the original's for a quarter point on the $+$ side of the centre, so it
  need not be a misprint; which quarter point eq. 17 refers to is still not
  stated, so the note stays undecided.
* **Three variants** (§3.2.2). A Lax–Friedrichs flux of the differentiated
  induction equation with a maximum wave speed (eq. 49); its zero-speed
  limit $\mathcal E_z^\circ$, equal to doubling the viscous part of the
  plain average (eqs. 39–40), "not an upwinded approximation", and for a
  first-order Godunov scheme identical to the CT of Londrillo & Del Zanna
  (2004); and $\mathcal E_z^c$ (eq. 51), each derivative taken from the
  upwind cell by the sign of the face-normal (mass-flux) velocity, the
  mean when it vanishes, usable with "any approximate or exact Riemann
  solver". All three reduce exactly to the 1D scheme for plane-parallel
  grid-aligned flow and "differ only in their numerical viscosity for
  multidimensional problems". On the first-order field loop the
  Lax–Friedrichs variant shows "unacceptable" diffusion of a stationary
  loop, $\mathcal E_z^\circ$ oscillates on the advected loop, and
  $\mathcal E_z^c$ does neither (§3.3.1); on a standing Alfvén wave the
  Lax–Friedrichs variant dissipates about twice as fast (§3.3.2).
  $\mathcal E_z^c$ is used for all second-order tests. These are the $\mathcal E^\circ$ and
  $\mathcal E^c$ that IDEFIX offers (batch 3). Because the cell-size factors cancel, the
  construction is stated to apply to corner-reconstruction schemes
  (Balsara), wave-propagation and central schemes as well (§6).
* **Inside CTU.** The predictor advances the face normal fields by
  $\Delta t/2$ with CT, so $\nabla\cdot\mathbf B = 0$ holds at
  $t^{n+1/2}$ too, and the corrector EMF uses a reference EMF built from
  the half-step state (§4.1.1, eqs. 69–70; §4.2, eqs. 74–78), as in the
  2D CTU+CT steps recorded above from Stone et al. (2008).
* **Evidence: grid-scale oscillations are not divergence errors** (§5.3,
  Fig. 10). In a shock tube rotated by $\tan^{-1}2$ on $256\times128$
  cells, the cell-centred field component along the wavevector oscillates
  by "roughly 10%" near the fast shocks; the Lax–Friedrichs variant does
  not reduce it, and averaged over macro-cells of $2\times1$ cells it is
  constant to round-off. The authors read the oscillation as grid-scale
  transverse variation of the discrete solution, not a CT defect.
* **Evidence: field loop.** The loop's magnetic energy decays smoothly
  (fit in [field-loop advection](/benchmarks/field-loop-advection.md)),
  and with uniform $v_z$ the out-of-plane field stays at round-off with
  "an incoherent structure", which the paper attributes to placing the
  $v_z\,\partial_xB_x$ term in the transverse correction rather than the
  characteristic step (§4.1.2; asserted, no figure).
* **Scope.** The paper is 2D only; the 3D extension is deferred (§6), so
  the 3D statements above rest on Stone et al. (2008) and later sources.

## Later uses (batch 7)

[Evans & Hawley (1988)](/sources/evans-1988.md) is the origin of the
method, cited for it by IDEFIX and AthenaK above. Its tests are
kinematic only: the field does not act on the flow, and the Lorentz force
"is left to a later paper" (§I).

* **Integral form** (§IIc, eqs. 2.9–2.12; §IVc, eqs. 4.10–4.13). The
  scheme evolves the magnetic flux through each face of a staggered cell.
  Each face flux changes by the EMFs on its four edges, a
  finite-difference Stokes theorem (after Schnack & Killeen 1980); each
  edge EMF is the **line integral** along the edge of the EMF component
  parallel to it (eq. 4.11). The face field is the flux over the face
  area, "the face area averaged flux" (eq. 4.6), as in the Staggering
  section above.
* **Why the divergence is preserved** (§IVc, p. 665). Summed over the six
  faces of a cell, the total flux "continues to vanish if it did
  originally, even though the cell position and shape may change",
  because "each EMF edge contribution appears in the full sum exactly
  twice with opposing signs"; each edge EMF is "calculated *once* even
  though each contribution is used in two separate evolution equations",
  as face fluxes conserve mass. This cancellation is the whole argument;
  there is no separate proof. The discrete divergence is the
  finite-difference Gauss theorem over the cell (eqs. 4.7–4.9).
* **The initial-value qualification in the original** (§IVc, p. 666). "The
  CT scheme only guarantees that field evolution *changes* are divergence
  free. If the initial magnetic field fails to satisfy the constraint, it
  will continue to do so." Badly posed inflow/outflow boundaries "can lead
  to subtle inflow of nondivergence-free magnetic field", so a global
  constraint measure should be monitored. This is the primary-source form
  of Bryan et al.'s point about ill-posed initial conditions (Staggering
  section).
* **Coordinates and moving meshes** (§II, eqs. 2.4–2.8). Written for the
  vector density $\sqrt{\det\gamma_{ij}}\,B^i$ with contravariant
  velocities, the induction equation has a "Cartesian" form in any
  coordinates and in general relativity, the shift entering only through
  the net velocity. The paper's "adaptive mesh" is **one moving,
  stretching grid** (a grid velocity in the net velocity, eqs. 2.10–2.12,
  4.20), not a hierarchy of refined grids: the restriction, prolongation
  and EMF correction of the AMR section above have no counterpart in it.
  The moving-grid update is written for field times zone width at both
  time levels; a straightforward differencing of the moving-surface
  equation "would be disastrous to constraint satisfaction" (§IVd).
* **Layout relative to the hydrodynamics** (§IVa–b, eq. 4.4, Figs. 1–2).
  The field components sit on the faces of a CT control volume "centered
  on $(i,j,k)$" (Fig. 2), which in the paper's indices is a hydro-zone
  corner; the velocities and momenta of the host code are face-centred on
  the hydro zones at half-integer time levels (Fig. 1), a staggered
  finite-difference layout rather than the cell-centred volume averages of
  the Staggering section. Per Fig. 1, $B^x$ (the figure's label $\mathcal B^x$)
  sits at the paper's $(i+\tfrac12, j)$ together with $v^y$ (label $V^y$),
  and $B^y$ (label $\mathcal B^y$) at $(i, j+\tfrac12)$ together with
  $v^x$ (label $V^x$), so each field component is tangential to
  the hydro-zone face it lies on and the 2D edge EMF falls at a
  hydro-zone centre (eq. 4.18). The later layout (field normal to the
  hydro-zone faces, EMFs on hydro-zone edges; Stone et al. 2008 above) is
  then a different placement of the same flux–EMF structure.
* **The original EMF is not built from Godunov fluxes** (§IVd,
  eqs. 4.18–4.24). In 2D axisymmetric spherical-polar coordinates each
  transverse field component is interpolated to the edge upwind along the
  velocity component it is paired with, with a van Leer limited slope and
  time centring, and multiplied by an equal-weight average of the
  velocity. Both the "transport" and the "shear" term must be upwinded:
  "These terms must be differenced in a consistent manner." Donor cell is
  "not recommended"; PPM is a named alternative. No Riemann solver or
  characteristic decomposition enters, consistent with the kinematic
  scope. The face-flux EMFs of the "Edge EMFs from face fluxes" section
  (Gardiner–Stone, Balsara–Spicer) are a later construction.
* **Edge-centred vector potential** (eqs. 4.14–4.17, 4.25). The face flux
  is the circulation of the vector potential around the face, so the
  potential sits on the EMF edges and its discrete curl satisfies the
  discrete divergence exactly. The paper uses it for divergence-free
  initial and boundary fields and states that CT "is related to a
  particular numerical approach for advecting the vector potential". This
  is the primary source behind IDEFIX's "mathematically equivalent to the
  original CT algorithm" (batch 3).
* **Why not the vector potential** (§III; §Va–d). The current needs two
  derivatives of the potential; at sharp features monotonic schemes change
  their weights abruptly and give "anomalous current, or force,
  reversals". In square-wave advection CT gives two clean current peaks,
  the monotonic and Wilson vector-potential codes "decidedly nonmonotonic
  currents" that change sign; in the accretion tests the vector-potential
  currents carry extra extrema "on the scale of $2\Delta x$". The price
  stated: "Accurate CT calculations may therefore require slightly greater
  resolution to maintain the same sharpness in the magnetic field"
  (§Vc).
* **The measured round-off floor** (§Vb, §Vd, eq. 5.6, Fig. 6). A
  normalized global divergence diagnostic starts at about $10^{-15}$;
  round-off "accumulates, but at a problem specific rate", to $10^{-10}$
  by the end of one calculation and $10^{-13}$ in another, and stays at
  $10^{-15}$–$10^{-14}$ when only the field is evolved in "double
  precision" (baseline precision not stated). No growth law is given. It
  is the earliest measured instance in this bundle of "to round-off" as a
  drifting floor, which the IDEFIX growth law (batch 3) states for its
  integrators.
* **Scope claims** (abstract, §I, §IVd). Any coordinates, any order of the
  transport scheme, 3D as well as 2D, nonideal MHD "Since Stoke's theorem
  still applies". Only 2D axisymmetric and 2D Cartesian kinematic runs
  are shown; 3D and nonideal MHD are asserted, not tested. The
  hydrodynamics is that of the host code of Hawley, Smarr & Wilson
  (1984b), to which the paper defers every hydrodynamic detail.

## Later uses (batch 9)

* **3D EMFs in the Gardiner–Stone scheme** ([Gardiner & Stone (2008)](/sources/gardiner-2008.md), §4). No new 3D EMF is defined: the contact-upwinded $\mathcal E^c$ of 2005 is reused in both 3D CTU variants. CT is framed as predictor (Godunov electric fields) and corrector (CT electric fields). At $t^{n+1/2}$ the cell-centre reference EMF uses face-averaged $\mathbf B$ and $\rho$, $\rho\mathbf v$ from a conservative $\Delta t/2$ update with the first fluxes (eq. 48). This agrees with the attributions of Athena++ and AthenaK to "Gardiner & Stone (2005, 2008)" above.
* **A cleaning paper's case against CT** ([Dedner et al. (2002)](/sources/dedner-2002.md), §1, p. 646): CT schemes are "restricted to structured grids and require large stencils", and "the underlying base scheme is only partially used". This is the authors' position, stated without a test.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §3, §5.1, §5.3, §8.4, §8.6.
2. [Stone et al. (2020)](/sources/stone-2020.md), §2.1.1, §2.1.4–2.1.5, §2.3, §3.1, §3.2.1, §3.4.1, §3.5.2, §4.
3. [Bryan et al. (2014)](/sources/bryan-2014.md), §3.3, §4.3, §11.2.10 (arXiv v1).
4. [Zhang et al. (2018)](/sources/zhang-2018.md), §3.1–3.3, §5.1 (arXiv v4).
5. [Mignone et al. (2012)](/sources/mignone-2012.md), §1, §3, §7.
6. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §1, §2.2.1, §2.2.4, §2.3.1, §3.1.2–§3.1.3 (arXiv v2).
7. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.4, §2.5, §2.8, §4.2 (arXiv v1).
8. [Stone et al. (2026)](/sources/stone-2026.md), §3 (arXiv v1).
9. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.1, §4.1–§4.2 (arXiv v1).
10. [Shankar et al. (2023)](/sources/shankar-2023.md), §III B (arXiv v2).
11. [Porth et al. (2019)](/sources/porth-2019.md), §3, §4.1, §4.1.1–§4.1.2, §4.1.8, §6, Table 1, App. A (arXiv v2).
12. [Gardiner & Stone (2005)](/sources/gardiner-2005.md), §§2.1–2.3, 3.2.1–3.2.2, 3.3.1–3.3.2, 4.1–4.2, 5.3, 6, eqs. 19–24, 34–51, 69–78 (arXiv v1).
13. [Evans & Hawley (1988)](/sources/evans-1988.md), §§I–VI, eqs. 2.4–2.12, 4.4–4.25, 5.6, Figs. 1–6.
14. [Gardiner & Stone (2008)](/sources/gardiner-2008.md), §4, eq. 48.
15. [Dedner et al. (2002)](/sources/dedner-2002.md), §1.
