---
type: Definition
title: "Implicit large-eddy simulation"
description: "Implicit LES drops the explicit subgrid model and lets the discretization's own dissipation and filtering act as the closure; the sources use the term in at least three senses and report where it works, where it fails, and what it misses."
status: established
aliases: [ILES, iLES, implicitly filtered LES, no-model LES, under-resolved DNS, URDNS, MILES]
tags: [les, implicit-les, numerical-dissipation, sgs-model, dg]
timestamp: 2026-10-26T10:27:00Z
---

# Implicit large-eddy simulation

**Implicit LES (ILES)** solves the unfiltered Navier–Stokes equations on a
mesh too coarse to resolve the dissipative scales, with no explicit
subgrid-scale term: the [numerical dissipation](/properties/numerical-dissipation.md)
and the truncation of the discretization play the role of
$-\partial_j\tau_{ij}$ in the [filtered equations](/definitions/large-eddy-simulation.md).
In the form of [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§2.1, Eqs. 8–9), the LES equation with closure operator
$M_i=-\partial_j\tau_{ij}$ becomes formally identical to the Navier–Stokes
equation when $M_i$ is dropped, and the filter is whatever the numerics
apply. The sources agree on this core but use the name for different
things, and they disagree on how much of the subgrid physics the numerics
can carry.

## Three usages

1. **No-model LES.** The discretization is used as is and its truncation
   error is the only closure. [Dzanic et al. (2022)](/sources/dzanic-2022.md)
   (§1) equate ILES with under-resolved DNS (URDNS); [Lozano-Durán et al.
   (2022)](/sources/lozanoduran-2022.md) (App. B) run channel WMLES "without
   an explicit SGS model, i.e., the numerical truncation errors act as the
   SGS model". [Flad & Gassner (2017)](/sources/flad-2017.md) (§1, §3.1)
   describe the standard DG practice: no model, polynomial de-aliasing for
   stability, and the interface Riemann solver as the only source of
   subgrid dissipation. [Prakash et al. (2022)](/sources/prakash-2022.md)
   (§III.B) call their no-model runs, in which only the SUPG/PSPG/grad-div
   stabilization of a finite-element scheme acts, an "implicit SGS model".
   In the [PANS](/methods/partially-averaged-navier-stokes.md) study of
   [Pereira et al. (2021)](/sources/pereira-2021.md) (§II, §IV) the
   $f_k=0$ run has no closure and the finite-volume code no artificial
   viscosity; the authors use it as their reference solution, "resolving
   all flow scales", while noting that the initial interface perturbations
   are not fully resolved on that grid. Astrophysical MHD runs use
   the same no-model setting: [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md)
   (§2) set the physical resistivity to zero in their RAMSES runs, so that
   "all diffusive effects in our simulations are of numerical nature" (the
   paper does not use the term implicit LES), and [Liu et al. (2022)](/sources/liu-2022.md)
   (§1) let dissipation be "provided by local truncation errors".
   [Placco et al. (2023)](/sources/placco-2023.md) (§2) simulate the
   supersonic wake of a Mars entry capsule with no explicit SGS model,
   "using instead the numerical dissipation given by the numerical
   discretisation as artificial viscosity acting at small scales": the
   fifth-order WENO convective scheme of the GPU code
   [STREAmS](/software/streams.md) (see [WENO schemes](/methods/weno-scheme.md)).
   [Davidovits et al. (2022)](/sources/davidovits-2022.md) (§II A) run
   shock-generated turbulence in an arbitrary Lagrangian–Eulerian
   radiation-hydrodynamics code with artificial viscosity for shocks and
   no physical viscosity or SGS model; they say the runs "should not be
   regarded as direct numerical simulation" but are "in the spirit of
   implicit large eddy simulations" (citing Sagaut), and analyse only
   large-scale averages, "expected to be least influenced by the
   (numerical) dissipation details\"
   (see [shock-generated turbulence](/results/shock-generated-turbulence.md)).
   [Delassaux et al. (2023)](/sources/delassaux-2023.md) (§4.1) define
   implicit LES in this sense, as "use of the truncation error of high order
   numerical scheme to mimic a sub-grid model". [Zhao et al. (2023a)](/sources/zhao-2023.md)
   (§1) date the idea to Boris et al. (1992, as recalled), and recall MILES
   and residual-based variational multiscale modelling as relatives; their
   high-order [gas-kinetic](/methods/high-order-gas-kinetic-scheme.md) ILES
   has molecular viscosity only, and they state that numerical dissipation
   "can overcome the problem of over-dissipation that arises in explicit LES
   models". [Morsbach et al. (2024)](/sources/morsbach-2024.md) (§2) run a
   wall-resolved ILES of the T161 low-pressure-turbine cascade with the
   sixth-order DGSEM of TRACE ($N=5$, Roe interface flux, Kennedy–Gruber
   kinetic-energy-preserving split form, BR1 viscous flux without penalty)
   and use it as the reference for RANS closures. [Sirignano & MacArt (2023)](/sources/sirignano-2023.md)
   (§3.2) and [Kurz et al. (2023)](/sources/kurz-2023.md) (§3.3, "iLES")
   use no-model LES as a baseline for learned closures.
   [Wang et al. (2023c)](/sources/wang-2023-c.md) (§II.A) recall the
   usage: $\tau_{ij}$ is neglected, numerical dissipation is "entirely
   responsible" for the subgrid energy transfer, the solution depends on
   grid and numerics, and extra numerical viscosity is often needed.
   [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) (§1)
   define ILES as "often referred to in the literature as under resolved
   DNS", with no subgrid model; in their stabilized finite-element solver
   the added dissipation is the SUPG/PSPG term, a stabilization parameter
   times the strong residual of the momentum equation (below). The 3D
   solar-flare MHD run of [Ruan et al. (2023)](/sources/ruan-2023.md) (§2)
   resolves its turbulence with the HLL Riemann solver and slope limiters
   of MPI-AMRVAC and no subgrid model; the paper does not use the term
   implicit LES and does not discuss numerical dissipation or resolution
   convergence.
2. **Designed numerical regularization.** The numerical dissipation is
   built to act as a model. Vicente Cruz & Lamballais (2023, §5.1) use the
   [implicit spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
   a viscous-term discretization tuned to dissipate near the mesh cutoff;
   [Beck & Kurz (2023)](/sources/beck-2023.md) (§III C, §V) distinguish
   such "true" implicit modelling from "no-model LES" (NoMo) and
   reinterpret the per-element blending factor $\alpha$ of a hybrid
   [DG/finite-volume subcell scheme](/methods/subcell-finite-volume-shock-capturing.md)
   as an implicit SGS model whose value a reinforcement-learning policy
   chooses (RL-Blend); [Haering et al. (2022)](/sources/haering-2022.md)
   (App. C) use an upwinding weight driven by a subgrid cell Reynolds
   number (iSGET) as the energy-transfer part of a hybrid model; MILES is
   recalled as the origin of the idea by Vicente Cruz & Lamballais (2023,
   §1) and Beck & Kurz (2023, §III C). [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md)
   (§1) describe implicit LES as benefiting "from the scheme's numerical
   dissipation", against explicit LES which models the small scales; their
   own SVV-filtered Smagorinsky viscosity sits between the two.
   [Ferrer et al. (2023)](/sources/ferrer-2023.md) (§4.1) list three
   implicit-LES options of the [HORSES3D](/software/horses3d.md) DG code:
   dissipative Riemann solvers, an interior-penalty parameter raised above
   its coercivity minimum in the viscous discretization, and energy-stable
   split forms combined with
   [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md).
   They state that DG dissipation and dispersion errors are confined to
   high wavenumbers, so that the numerical dissipation acts "primarily on
   under-resolved scales", making DG "very suitable for ILES" (citing
   earlier studies). [Zhao et al. (2023b)](/sources/zhao-2023-b.md) (§1),
   in a RANS paper, recall the same literature: raising the DG order
   increases the dissipation at the largest wavenumbers while narrowing the
   range where it acts, and the choice of Riemann solver strongly
   influences DG ILES.
   [Kou et al. (2023)](/sources/kou-2023.md) (Abstract, §1, §2.2) study two
   of these face penalties in HORSES3D, on the solution jump (an increased
   interior-penalty parameter) and on the gradient jump, and state that
   [jump-penalty stabilization](/methods/jump-penalty-stabilization.md)
   "acts as an implicit subgrid model". [Slaughter et al. (2023)](/sources/slaughter-2023.md)
   (§3, §3.1) stabilize a Fourier spectral/hp element ILES in
   [Nektar++](/software/nektar-plus-plus.md) with gradient-jump penalisation
   in the plane and spectral vanishing viscosity in the span. They call the
   stabilisations "somewhat analogous to a sub-grid scale model" whose
   dissipation is "a pure characteristic of the numerical scheme", and state
   the ILES assumption as "the SGS stresses are of the order of magnitude as
   the truncation error of the discretisation". [Lederer et al. (2023)](/sources/lederer-2023.md)
   (§3.2–3.3) take the upwind jump term of an exactly divergence-free hybrid
   mixed finite-element method as the only dissipation, and then restrict
   it to the high-order part of the jump: the
   [HOPU method](/methods/high-order-projection-based-upwind-method.md).
   [Wang (2024)](/sources/wang-2024-b.md) (§2.3–2.4) runs
   [flux-reconstruction](/methods/flux-reconstruction.md) ILES of turbine
   cascades with no subgrid model, relying on the built-in dissipation of
   the scheme, and adds local solution filtering for robustness: an
   exponential modal filter applied only in elements whose Persson–Peraire
   smoothness indicator exceeds a threshold (local modal filter), or the
   positivity-preserving entropy filter of Dzanic & Witherden (as
   recalled). Filtering adds local numerical dissipation to the dissipation
   on which ILES relies as a subgrid model (citing Edoh et al.); the
   Riemann solver contributes too: Rusanov on wall faces, HLLC or Roe
   inside. The filter and solver comparisons are on the
   [subcell finite-volume shock-capturing](/methods/subcell-finite-volume-shock-capturing.md)
   and [numerical dissipation](/properties/numerical-dissipation.md) pages.
3. **Implicitly filtered LES.** The filter is the one induced by grid and
   discrete operator, whatever closure is added. Beck & Kurz (2023, §I)
   use the term in this sense: the filter width and shape are
   inhomogeneous, possibly nonlinear and unknown a priori, and the closure
   must be [discretization-consistent](/definitions/discretization-consistent-closure.md).
   [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) (§1) define
   implicit LES even more broadly, as any LES that uses the DNS equations
   in their original form with a closure added "regardless of whether the
   filter is known explicitly or not".
   [Krais et al. (2021)](/sources/krais-2021.md) (§2.2.3) state that LES in
   FLEXI uses implicitly filtered equations, with the implicit closure
   through the numerical flux recommended for well-resolved LES and
   explicit eddy-viscosity models available.
   Kurz et al. (2023, §1, §3.3) state the consequence for learning: in DG
   the induced filter is an element-local $L^2$ projection coupled through
   the numerical fluxes, a filter with "typically non-linear kernel", so
   the exact closure terms cannot be computed even from DNS and supervised
   learning of closures for implicitly filtered LES is "from our
   perspective, ill-posed"; reinforcement learning puts the filter in the
   training loop. [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
   (§2.5) generate wall-model training data in the target solver for the
   same reason: in implicitly filtered LES the subgrid tensor does not
   coincide with the stress obtained by filtering Navier–Stokes. Sirignano &
   MacArt (2023, §3.1) box-filter and downsample DNS, with the filter width
   equal to the local LES spacing, and treat the result as an implicitly
   filtered LES solution.
   [Duan & Wang (2024)](/sources/duan-2024.md) (§3) state that projecting a
   solution onto the piecewise-polynomial space is a space-filtering
   operation, so flux reconstruction without a subgrid model is ILES, and
   adding a model adds dissipative fluxes.

Usages 1 and 2 concern the closure (none, or numerical); usage 3 concerns
the filter. A page or claim about "ILES" should say which.

## What the closure terms are

Beck & Kurz (2023, §I, Eqs. 2–5) split the unclosed terms of implicitly
filtered LES into a commutation error, the classical subfilter term and a
discretization term (the "computational subgrid stress"). For
$\Delta\approx h$ the third can exceed the second, and for nonlinear schemes
it cannot be computed a priori. In this view ILES is the limit in which the
explicit closure is zero and the discretization term is the whole model.
The trained RL-Quad Smagorinsky coefficient of Beck & Kurz (§V B, Fig. 11)
peaks at the DG element centre and vanishes at the faces, which the authors
read as compensating the face-concentrated DG dissipation (an
interpretation they flag as needing further work).

## Evidence: when it works

- **High-order DG with enough resolution.** Flad & Gassner (2017, §1,
  Fig. 1a) obtain excellent spectra for decaying homogeneous isotropic
  turbulence (DHIT, $Re_\lambda$ from about 162 to 97) with DG ILES at
  $144^3$ degrees of freedom ($18^3$ elements, $N=7$), where about 43% of
  the dissipation is resolved at a 3-points-per-wavelength cutoff.
  Krais et al. (2021, §7.1) run a wall-resolved ILES of a NACA 64418
  airfoil at $Re_c=10^6$, $M=0.2$ with split-form DG and the Pirozzoli
  kinetic-energy-preserving flux ($N=7$, about 117 million degrees of
  freedom per variable); $C_p$ agrees with XFoil except near the suction-side
  trailing edge, where the LES separates (XFoil is the only reference).
- **Low order DG.** In forced HIT at $Re_\lambda\approx180$ with 24 or 36
  degrees of freedom per direction, NoMo is the best baseline for $N=3$,
  better than static and dynamic Smagorinsky and not reached by the RL
  models; its reward falls as $N$ grows to 5 and 8 (Beck & Kurz 2023, §V A,
  Fig. 8).
- **Designed SVV.** Implicit SVV beats constant-coefficient Smagorinsky in
  Taylor–Green-vortex spectra and dissipation at $Re=40\,000$ and is
  numerically converged at standard resolution (Vicente Cruz & Lamballais
  2023, §6.4). In pipe flow at $Re_\tau=1000$ with
  $\Delta x^+=\Delta y^+\approx9$ it predicts $u_\tau$ within 1.8%, against
  +9.6% for Smagorinsky with van Driest damping and +15.3% for no model
  (§7.2–7.4); the authors call this an "augmented wall-resolving" property.

- **High-order gas-kinetic scheme, Taylor–Green vortex.** [Cao et al. (2022)](/sources/cao-2022.md)
  (§3.1, Figs. 2–5) run the Taylor–Green vortex at $Re=1600$, $M_0=0.1$
  with a fifth-order WENO gas-kinetic scheme on $128^3$ to $1024^3$ cells,
  and estimate the numerical dissipation as the kinetic-energy decay rate
  minus the resolved solenoidal, bulk and pressure–dilatation dissipation.
  The numerical part decreases with refinement and is significant on the
  coarse grids. The authors state that because the decay rate "is well
  predicted at all grid levels", "the filtering due to the coarse mesh
  correctly mimics the physical dissipation from the unresolved scale
  dynamics", which "validates the usage of high-order numerical methods for
  the implicit large-eddy simulations"; the same section reports "a large
  discrepancy" in the peak dissipation rate on $128^3$ and $256^3$, and
  kinetic energy matching the reference on all grids except $128^3$. See
  [high-order gas-kinetic schemes](/methods/high-order-gas-kinetic-scheme.md).
- **DG airfoil polars.** In HORSES3D, ILES of the NACA 0012 at
  $Re_c=10^6$ on 18 000 hexahedra with $N=4$ (2.2 million degrees of
  freedom) gives lift against angle of attack and a drag polar in "very
  good agreement with the experimental data" (Ferrer et al. 2023, §4.1,
  Fig. 7, adapted from the group's earlier paper); the experiment is not
  named in this paper.
- **Supersonic capsule wake.** Placco et al. (2023, §2–5) justify their
  WENO-based ILES by turbulent-boundary-layer studies that found it
  comparable to coarse DNS (Poggie et al.; Ritos et al., as recalled). They
  run a $2048\times672\times672$ grid with an
  [immersed boundary](/methods/immersed-boundary-method.md) at
  $M_\infty=2$, $Re=10^6$ based on the capsule diameter, and report wake
  topology, drag, lift and Strouhal numbers, with no comparison with
  reference data, no grid-convergence study and no wall-unit resolution.
- **Resolution check, shock-driven turbulence.** Davidovits et al. (2022,
  §II A) rerun a subset of their 2D cases at double resolution in each
  direction and state that the scalings of the averaged quantities do not
  change; for one example case the analysis-region averages change by
  0.6% to 2.9%, depending on the quantity.
- **Jet reference.** Among the reference simulations of the PPRIME round
  jet, the finest hp-adapted hybrid RANS/LES of [Basile et al. (2023)](/sources/basile-2023.md)
  (§4.2.3, Fig. 9, Table 1) agrees on the centreline with the RANS-profile
  plus ILES of Shur et al. (23 million cells, high-order finite volume);
  both overestimate the potential-core length, and Basile et al. list ILES,
  with the missing nozzle–jet feedback loop, among the candidate causes
  given by Shur et al., without settling between them.

- **Gas-kinetic ILES of channel flow.** Zhao et al. (2023a, §5, Tables
  8–9, Figs. 3–15) run the Taylor–Green vortex at $Re=1600$ on $256^3$ and
  channel flow at nominal $Re_\tau=180$ ($64\times96\times64$) and 395
  ($96^3$) with fifth- and seventh-order, non-compact and compact
  reconstructions. Higher order or the compact stencil brings the realized
  $Re_\tau$ closer to DNS (at 395: 360.35 for fifth order non-compact,
  377.05–380.45 for the others, against 392.24) and improves mean velocity,
  r.m.s. fluctuations and spectra; the fifth-order compact scheme "can
  almost achieve the accuracy of the 7th-order non-compact scheme".
- **Jump penalties against explicit models.** On the Taylor–Green vortex
  at $Re=1600$, $M=0.1$ ($32^3$ elements, $N=3$), unpenalized DG diverges;
  solution and gradient jump penalties above $\tau_s>1.9$ and
  $\tau_g>6.3\times10^{-4}$ (page-local penalty parameters, defined on the
  [jump-penalty](/methods/jump-penalty-stabilization.md) page) remove a
  spurious second peak of the dissipation rate, and both are "clearly
  superior" to [Smagorinsky](/methods/smagorinsky-model.md) and
  [Vreman](/methods/vreman-model.md) models adapted to DG (Kou et al. 2023,
  §4.2, Figs. 10–12). The paper gives no constants or filter width for the
  explicit models.
- **Explicit model on top of DG ILES.** In channel flow at
  $Re_\tau=392.24$, a projection-based variational multiscale model with
  the [WALE](/methods/wale-model.md) eddy viscosity gives about the same
  statistics as ILES at the finer resolutions and slightly worse ones at
  the coarsest (Lederer et al. 2023, §4.1, Fig. 1). The authors conclude
  that the explicit model "can harm the implicit dissipation mechanism"
  (§6). HOPU lowers the bulk-Reynolds-number error of the $N=3$ runs to
  0.6–1.0%, against 1.1–13.4% for ILES and 2.7–16.3% for the VMS model
  (Table 2), an error measure the authors call rough.

- **High-order flux reconstruction, well resolved.** Duan & Wang (2024,
  §5.1–5.3, Figs. 5–10) find ILES better than explicit
  [Smagorinsky](/methods/smagorinsky-model.md), [WALE](/methods/wale-model.md)
  and [Vreman](/methods/vreman-model.md) models whenever the flow is well
  resolved: on the viscous Taylor–Green vortex at $Re=1600$ ($64^3$
  elements, $N=4$) the ILES enstrophy is "almost on top of" the DNS, and in
  the wall-resolved channel at $Re_\tau=180$ ($N=3$, per-degree-of-freedom
  spacings $\Delta x^+=\Delta z^+=5.7$, $\Delta y^+=0.68$) it "agrees very
  well" with DNS; the subgrid models add much more dissipation than the
  Riemann solver of the scheme (§5.1). This confirms, in the authors'
  words, earlier findings that subgrid models are detrimental in
  high-order wall-resolved LES (§1, §6).
- **Stabilized finite elements, periodic hill.** Prieto Saavedra et al.
  (2024, §4.1–4.3, Figs. 4–12) run the
  [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=5600$ in the
  continuous-Galerkin code Lethe ($Q_1$–$Q_1$ SUPG/PSPG, BDF2) on 0.25 to 4
  million cells (1.1 to 16 million degrees of freedom), against 12.4
  million cells for the reference explicit LES. Mean velocity and Reynolds
  stresses agree well with Rapp's experiment and Breuer et al.'s LES; the
  reattachment approaches the measured $x/h=4.83$ with refinement,
  non-monotonically, and on the fine mesh all time steps but the largest
  give similar results even at a Courant number of about 2.8 (Table 5).
  The authors conclude that ILES needs no calibration of a subgrid model
  and can reduce mesh size and degrees of freedom (§5); no cost comparison
  at equal accuracy is given, and the fine runs cost up to 188 000
  core-hours (App. C).
- **Flux-reconstruction turbine cascades.** With the local modal filter,
  the Taylor–Green vortex at $Re=1600$ and 5000 ($64^3$, $N=3$) shows no
  visible change of dissipation rate or spectrum against the unfiltered
  run and DNS, at 5.5% overhead; the T106C cascade at $Re=80\,000$ ($N=3$,
  7.9 million degrees of freedom per equation) matches the measured
  isentropic Mach number; on the LS89 vane at $Re=1.13\times10^6$ the heat
  transfer coefficient converges towards experiment with $N$ and spanwise
  refinement, and a spanwise spacing $z^+\approx45$–60 suffices for its
  mean (Wang 2024, §4.1–4.3, Figs. 2–3, 8, 13–14; see
  [turbine cascades](/benchmarks/turbine-cascade.md)).

## Evidence: when it fails

- **Applicability plateau.** At $48^3$ degrees of freedom ($6^3$ elements,
  $N=7$), where only about 0.9% of the dissipation is resolved, DG ILES
  piles energy up at mid wavenumbers and drops sharply near the cutoff;
  changing the Riemann solver (Roe, Lax–Friedrichs, low-dissipation Roe) or
  adding a Smagorinsky or small–small VMS model on top does not help.
  Flad & Gassner (2017, §1) conclude that roughly 40% of the total
  dissipation must be resolved for de-aliased upwind DG ILES to work, a
  threshold inferred from two resolutions of one case. The remedy they
  propose is a dissipation-free [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
  split-form baseline plus an explicit [Smagorinsky model](/methods/smagorinsky-model.md)
  (§4).
- **Missing plateau of the spectral eddy viscosity.** The a priori
  [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) of the
  Taylor–Green vortex has a nonzero low-wavenumber plateau (about 12, 2 and
  0.2 times $\nu$ at the three LES resolutions), which carries up to 24%,
  16% and 6% of the total dissipation through scales below $k_c/4$; scale-
  selective ILES vanishes there. Vicente Cruz & Lamballais (2023, §6.4,
  Figs. 16–18) call this "a fundamental limitation of any implicit LES",
  "making somewhat inconsistent the concept of implicit LES except when the
  mesh is close to DNS". Flad & Gassner (2017, §3.1) give the same
  explanation for the DG failure: interface dissipation is concentrated at
  the highest wavenumbers and lacks the Kraichnan plateau.
- **Bottleneck.** The scale-selective SVV dissipation produces a soft
  pile-up below $k_c/2$, a spurious defiltering that Vicente Cruz &
  Lamballais (2023, §6.4) call the main drawback of their implicit model;
  adding Smagorinsky ($C_s=0.18$) removes it but does not improve the total
  dissipation (§6.5).
- **No dissipation at all.** With kinetic-energy-conserving convection,
  no-model LES thermalizes towards a $k^2$ equipartition spectrum and,
  during the Taylor–Green breakdown, dramatically overestimates the total
  dissipation (Vicente Cruz & Lamballais 2023, §6.2); Flad & Gassner (2017,
  §3, Fig. 4) obtain the same $k^2$ spectrum from the dissipation-free
  split-form DG at $48^3$, stable but without a model. Agrawal et al. (2022,
  §VII.C) see $k^2$ equipartition in a no-model run of HIT at
  $Re_\lambda\to\infty$. [Kim et al. (2024)](/sources/kim-2024.md) (§2.1,
  Table 3, App. C) state that their second-order central,
  kinetic-energy-conserving scheme has no numerical dissipation: no-model
  LES of the [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
  is stable but inaccurate (recirculation length $L_r/D=1.25$ against 1.56
  from DNS at $Re_D=3900$; $L_r$ page-local) and diverges on very coarse
  grids.
- **Under-resolved wall-modelled LES at high order.** Duan & Wang (2024,
  §1, §5.4) state that high-order ILES in severely under-resolved LES, wall
  modelled above all, "often runs into robustness and accuracy issues due
  to the low dissipation embedded in these methods"; their wall-modelled
  channel at $Re_\tau=5200$ ($60\times16\times40$ elements, element sizes
  $\Delta x^+=1088$, $\Delta y^+=650$, $\Delta z^+=544$) is not stable
  without a model. The alternative, solution limiting, makes the result
  depend on the amount of limiting (their Fig. 2), which they call ad hoc;
  they recommend an explicit Vreman model instead. In decaying isotropic
  turbulence ($32^3$ cells, $N=2$–5) the ILES spectra differ most from
  experiment at high wavenumbers (§5.2, Fig. 8).
- **Dissipation tied to the time step.** In the stabilized finite-element
  ILES of Prieto Saavedra et al. (2024, §4.2, Table 5, Figs. 6–8) the
  stabilization parameter contains $1/\Delta t$, so its dissipation falls
  as the time step falls. On the coarse mesh (0.25 million cells) halving
  $\Delta t$ three times, from 0.1 to 0.0125, moves the reattachment from
  $x/h=4.73$ to 5.37 and degrades the Reynolds stresses in the bulk;
  the authors explain this by the shrinking stabilization, consistently
  with earlier stabilized-method studies (as recalled). On the fine mesh
  the residual, and so the stabilization, matters less. The implicit model
  of this scheme therefore depends on $\Delta t$ through the stabilization
  parameter (§2.4, Eq. 10; §4.2). At $Re_h=10\,600$ and
  37 000 the velocity is reasonable but the Reynolds stresses are
  over-predicted, more so at 37 000 (§4.4).
- **Aliasing.** On the periodic hill at $Re_b=10\,595$ with 64×64×32
  degrees of freedom, fourth-order URDNS shows large spurious oscillations
  in the $\langle v'v'\rangle$ and $\langle u'v'\rangle$ profiles that the
  authors attribute to aliasing, absent when the
  [PANS](/methods/partially-averaged-navier-stokes.md) eddy viscosity is
  added (Dzanic et al. 2022, §3.1, Fig. 5); the paper reports no
  de-aliased run.
- **Coarse grids with high-aspect-ratio cells.** On the coarse grid of a
  [backward-facing step](/benchmarks/backward-facing-step.md) (10 nodes per
  step height, $\Delta x/\Delta y\sim100$ in the shear layer), a no-model run
  of [Abe (2021)](/sources/abe-2021.md) (App. B, Table IV, Fig. 14) gives a
  reattachment length (page-local $x_R$) $x_R/H=7.60$ (+16.7% against the experimental 6.51),
  against 7.19 with the author's stabilized mixed model; on the fine and
  medium grids the explicit-model LES gives 6.54 and 6.67 (Table II). Citing
  the author's earlier work, Abe states that "as the grid resolution
  becomes coarser, the performance of the ILES suddenly decreases", so a
  high-quality SGS model is preferable on coarse grids, and that ILES "does
  not always account for the detailed dynamics of small-scale turbulent
  structures" (§I).
- **Stabilized finite elements at infinite Reynolds number.** In forced
  isotropic turbulence with $\nu=10^{-12}$ on $32^3$–$128^3$ trilinear
  elements, the no-model run shows a large energy pile-up at the highest
  resolved wavenumbers, as does the unclipped gradient model (Prakash et
  al. 2022, §III.B.1, Fig. 4). The authors state, from numerical experiments
  not shown, that the numerical dissipation of the stabilization is
  "significantly smaller" than the SGS dissipation of every explicit model.
- **Rayleigh–Taylor mixing.** Pereira et al. (2021, §I, Fig. 1) survey
  growth rates of [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md):
  DNS values vary little, ILES values span a broad range, which they
  attribute, beyond initial conditions, to modelling assumptions such as an
  inviscid fluid or one- and two-dimensional flow.
- **Pile-up in DG at moderate order.** In forced HIT at
  $Re_\lambda\approx180$ with $N=5$ and 7 (24 to 48 degrees of freedom per
  direction), no-model DG LES "exhibits a buildup of energy in the
  upper wavenumbers due to lacking dissipation"; static Smagorinsky ($C_s=0.17$) is over-dissipative, a
  learned element-wise Smagorinsky coefficient matches the DNS spectrum
  "almost perfectly", and the dynamic model does about as well except at
  24 degrees of freedom (Kurz et al. 2023, §4.2, Fig. 6). This agrees with the
  reward of no-model LES falling from $N=3$ to $N=5$ and 8 in Beck & Kurz
  (2023) above.
- **Unpenalized DG.** Kou et al. (2023) see standard DG diverge in the
  Taylor–Green vortex ($32^3$ elements, $N=3$), which they relate to
  aliasing following Gassner et al. (as recalled), and in a 2D compressible
  Kelvin–Helmholtz instability ($Re=10^4$, $M=0.5$, $64^2$ elements, $N=3$)
  at $t/t_c\simeq4$; only the solution penalty completes the
  Kelvin–Helmholtz run (§4.2–4.3).
- **Separated bluff-body flow.** For rectangular prisms in confined
  cross-flow ($Re_0=1000$–2000, LES on $1/64$ or $1/512$ of the DNS points),
  no-model LES underperforms the learned closures in all cases; it
  underpredicts the drag coefficient (e.g. 1.88 against 2.45 for filtered
  DNS at aspect ratio 1) and gives "incorrectly large" resolved Reynolds
  stresses in the boundary layers (Sirignano & MacArt 2023, §4.1–4.2,
  Table 2, Figs. 8–9).
- **Excess near-wall upwind dissipation.** In highly under-resolved DG
  ILES the velocity jumps, and so the upwind dissipation, are larger near
  the wall than in the outer flow, more than stability needs (Lederer et
  al. 2023, §3.3, Figs. 2–3, 10); HOPU targets this.
- **Still over-dissipative at fifth order.** Measured by the residual of
  the kinetic-energy budget, the numerical dissipation of the fifth-order
  gas-kinetic ILES of the Taylor–Green vortex falls with order and with the
  compact stencil; "the 5th-order scheme for ILES is still over-dissipative"
  (Zhao et al. 2023a, §5.1, Fig. 7). All their channel spectra show "an
  unnatural leveling-off of the energy spectrum near the cutoff
  wavenumber", attributed to the resolution (§5.2.3).
- **Wall-modelled resolution.** Implicit SVV alone underestimates $u_\tau$
  by more than 12% at $Re_\tau=2000$ with $\Delta x^+=18$ (Vicente Cruz &
  Lamballais 2023, §7.4), so it "cannot be used alone in the context of
  WMLES".

## Flux reconstruction and PANS (inline)

Dzanic et al. (2022, §2.2–2.3) compare URDNS with
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
in the flux-reconstruction scheme of Huynh (PyFR), at equal degrees of
freedom with second-order ($\mathbb P_1$) and fourth-order ($\mathbb P_3$)
solution polynomials. Going to fourth order improves first-order statistics
of URDNS and PANS about equally, but second-order statistics (periodic hill)
and the shedding and Kelvin–Helmholtz spectral peaks of the circular
cylinder at $Re_D=3900$ (at $x/D=7$) much more for PANS than for URDNS
(§3.2, Figs. 11–13). The authors attribute the difference to the lower
numerical dissipation of the high-order scheme, which lets resolved small
scales respond to the model.

## Numerical dissipation as an effective Reynolds number

When the numerics are the only dissipation, the grid fixes an effective
Reynolds number. Liu et al. (2022, §1) recall that a turbulent dynamo needs a
dissipation scale at least about 30 times smaller than the injection scale
(critical Reynolds number about 30–60), and with truncation-error
dissipation turn this into a resolution of at least 30 pc for a 1 kpc thick
disc and about 3 pc for a 100 pc disc; they replace the unresolved dynamo by
a [subgrid model](/methods/subgrid-turbulent-dynamo-model.md).
Martin-Alvarez et al. (2022, §1, §3.2) argue that multi-level adaptive
refinement introduces one numerical viscous and resistive scale per level,
and compare dynamo growth rates with reference scalings drawn against the
finest cell size (Fig. 7), the numerical viscosity being assumed
proportional to the cell size; see
[numerical dissipation](/properties/numerical-dissipation.md) and
[small-scale dynamo](/results/small-scale-dynamo.md). Pereira et al. (2021,
§IV.3.1, Eqs. 22–23) define an effective viscosity $\nu+\nu_t+\nu_n$ with
$\nu_n$ the numerical viscosity, which they do not compute.

## Explicit models that act like implicit ones

[Saini et al. (2023)](/sources/saini-2023.md) (Abstract, §5–6) measure, as
the residual of the discrete resolved-energy budget, how much dissipation
the numerics add beside an explicit closure: the [WALE](/methods/wale-model.md)
model in a second-order finite-volume code and
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) in
a fifth-order continuous-Galerkin code. Numerical dissipation is 60–90% of
the total numerical-plus-model dissipation (Abstract); the authors say this "challenges the usual
assumption in LES practice that all or most of the required subgrid
dissipation is imparted by the SGS model". Details on
[numerical dissipation](/properties/numerical-dissipation.md).

## Qualifications

- The plateau threshold of Flad & Gassner (2017) and the plateau-dissipation
  shares of Vicente Cruz & Lamballais (2023) come from one canonical flow
  each (DHIT, Taylor–Green vortex) and different schemes (DG, sixth-order
  compact differences); neither is a general bound.
- Krais et al. (2021) validate their ILES airfoil only against XFoil.
- Vicente Cruz & Lamballais (2023, §8) conclude that for
  $\Delta_{\mathrm{LES}}/\Delta x_{\mathrm{DNS}}\lesssim5$ the usefulness of
  explicit SGS modelling "cannot be evidenced", and invert the usual
  justification of ILES: explicit models such as Smagorinsky's "should be
  seen as an ersatz of regularization". Beck & Kurz (2023, §V A) reach a
  related conclusion from the other side: no reference model is best for
  all discretizations, so closure and discretization must be designed
  together.
- [Goc et al. (2021)](/sources/goc-2021.md) (§2.3), who run explicit SGS
  models, state that low-dissipation numerics are essential because
  numerical dissipation is "extremely detrimental" for coarse LES (Mittal &
  Moin 1997, as recalled): the opposite design choice to usage 2.

- Ferrer et al. (2023, §4.1) call DG "very suitable for ILES" because its
  numerical dissipation is confined to high wavenumbers, and give no
  resolution condition; Flad & Gassner (2017), whom they cite, find that
  the same high-wavenumber concentration makes de-aliased DG ILES fail
  when the cutoff lies in the inertial range (above). Ferrer et al.
  state no resolution condition and the paper reports no coarse-resolution
  test, so the two statements are not recorded as a contradiction.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) (§2.3) take the
  position opposite to usage 2 for their hybrid RANS/LES: "if one assumes
  that the added dissipation to the simulation should be only due to the
  SGS scales", the scheme's fourth-order artificial dissipation should be
  as low as possible, although "some amount of numerical dissipation is
  often needed" for convergence (see
  [numerical dissipation](/properties/numerical-dissipation.md)).
- Lederer et al. (2023, §4.1, §5.1, §6) and Abe (2021, §I, App. B) reach
  opposite recommendations about explicit models on coarse grids. In DG
  ILES of channel flow and the periodic hill, a WALE-based VMS model gives
  about the same statistics as no model, slightly worse ones on the
  coarsest channel grids, and "can harm the implicit dissipation
  mechanism"; Abe, on the coarse high-aspect-ratio grid of a
  backward-facing step (above), finds that "the performance of the ILES
  suddenly decreases" and favours a high-quality SGS model on coarse
  grids. The schemes, models and flows differ, so the two are not
  recorded as a contradiction. Duan & Wang (2024) find both verdicts in
  one flux-reconstruction code, split by resolution: ILES is best when the
  flow is well resolved (Taylor–Green vortex, wall-resolved channel) and
  fails in the wall-modelled channel, where an explicit model is needed
  (§5–6).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) (§4.2, §5), after
  comparing single and double precision in DNS of channel flow with a
  GPU gas-kinetic code, state that single precision "may not be safe" for
  DNS of time-evolving turbulence but "may be used" for LES and RANS; the
  paper runs no LES or RANS case.
- In the LES modelling-residual estimator that drives the
  [mesh adaptation](/methods/mesh-adaptation.md) of
  [Blind et al. (2023)](/sources/blind-2023.md) (§2.2), the subgrid terms
  are zero for implicit LES, so the estimate contains only the resolved
  terms.
- Abe (2021) and Cao et al. (2022) reach opposite verdicts on implicit LES
  from different settings: a second-order finite-volume code on a coarse,
  strongly anisotropic grid in a separated shear layer, with a local
  measure (reattachment length), against a fifth-order gas-kinetic scheme
  on uniform grids of $128^3$ and finer in the Taylor–Green vortex, with a
  global measure (kinetic-energy decay rate). Neither tests the other's
  configuration, so the two are not recorded as a contradiction. Cao et
  al.'s verdict also sits beside their own report of a large peak-dissipation
  discrepancy on the two coarsest grids.

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, Figs. 1–3; §3, Fig. 4; §3.1; §4.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I, Eqs. (2)–(5); §III C, Eq. (16); §V A–C, Figs. 8, 11–14.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1; §2.2–2.3; §3.1, Fig. 5; §3.2, Figs. 11–13.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1, Eqs. (8)–(9); §5.1; §6.2–6.5, Figs. 16–18; §7.2–7.4; §8.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.1, Fig. 24.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §1.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V D; App. C, Eqs. (C1)–(C2).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — App. B.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.3 (low-dissipation numerics as a requirement of coarse LES).
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.C, Fig. 6.
- [Abe (2021)](/sources/abe-2021.md) — §I; App. B, Tables II, IV, Fig. 14.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B, §III.B.1, Fig. 4.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.1, Figs. 2–5.
- [Basile et al. (2023)](/sources/basile-2023.md) — §4.2.3, Fig. 9, Table 1.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §I, Fig. 1; §II; §IV; §IV.3.1, Eqs. (22)–(23).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §1.
- [Liu et al. (2022)](/sources/liu-2022.md) — §1.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1; §2; §3.2.
- [Placco et al. (2023)](/sources/placco-2023.md) — §2; §3; §4–5.
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §II A.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1, Fig. 7.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2.3.
- [Blind et al. (2023)](/sources/blind-2023.md) — §2.2.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §1; §5.1, Figs. 3–7; §5.2, Tables 8–9, Figs. 8–15.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2.
- [Kou et al. (2023)](/sources/kou-2023.md) — Abstract; §1; §2.2; §4.2, Figs. 10–12; §4.3.
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §3; §3.1.
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.2–3.3, Figs. 2–3, 10; §4.1, Fig. 1, Table 2; §6.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §1; §3.3; §4.2, Fig. 6.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.5.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §3.1–3.2; §4.1–4.2, Table 2, Figs. 8–9.
- [Saini et al. (2023)](/sources/saini-2023.md) — Abstract; §5; §6.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2; §5.
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §1.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §1; §2.4; §4.1–4.4, Tables 4–5, Figs. 4–16; §5; App. C.
- [Ruan et al. (2023)](/sources/ruan-2023.md) — §2.
- [Wang (2024)](/sources/wang-2024-b.md) — §2.3–2.4; §4.1–4.3, Figs. 2–3, 8, 13–14.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §1, Fig. 2; §3; §5.1–5.4, Figs. 5–15; §6.
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1; Table 3; App. C.
