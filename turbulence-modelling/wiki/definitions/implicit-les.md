---
type: Definition
title: "Implicit large-eddy simulation"
description: "Implicit LES drops the explicit subgrid model and lets the discretization's own dissipation and filtering act as the closure; the sources use the term in at least three senses and report where it works, where it fails, and what it misses."
status: established
aliases: [ILES, iLES, implicitly filtered LES, no-model LES, under-resolved DNS, URDNS, MILES]
tags: [les, implicit-les, numerical-dissipation, sgs-model, dg]
timestamp: 2026-10-27T21:12:00Z
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
   (numerical) dissipation details"
   (see [shock-generated turbulence](/results/shock-generated-turbulence.md)).
   [Delassaux et al. (2023)](/sources/delassaux-2023.md) (§4.1) define
   implicit LES in this sense, as "use of the truncation error of high order
   numerical scheme to mimic a sub-grid model". [Zhao et al. (2023a)](/sources/zhao-2023.md)
   (§1) date the idea to Boris et al. (1992, cited), and recall MILES
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

   Further no-model runs:

   - **Gas-kinetic iLES against four explicit models.**
     [Zhao et al. (2021)](/sources/zhao-2021-c.md) (§I, §III, §VI) run
     wall-resolved channel flow with the
     [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
     (fifth-order WENO with linear weights normal to the face) either with no
     model ("iLES") or with the [Vreman](/methods/vreman-model.md),
     clipped [dynamic Smagorinsky](/methods/dynamic-procedure.md),
     [WALE](/methods/wale-model.md) or dynamic Clark
     ([gradient](/methods/gradient-model.md)) model entering the kinetic
     solver through an enlarged relaxation time. They state, citing
     Bazilevs et al. and Kokkinakis & Drikakis, that implicit LES "can
     overcome the problem of over-dissipation that arises in explicit LES
     models" (§I); results below.
   - **Gas-kinetic iLES.** [Cao et al. (2024)](/sources/cao-2024.md) (§1)
     run their curvilinear
     [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
     as "iLES": "the built-in numerical dissipation acts as the
     subgrid-scale (SGS) dissipation, thus no explicit SGS model is
     utilized".
   - **Supersonic Taylor–Green vortex.**
     [Chapelier et al. (2024)](/sources/chapelier-2024.md) (§IV.A) run
     seven high-order codes on the supersonic
     [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($Re=1600$,
     $M_0=1.25$) without a subgrid model. They assume that at this low
     Reynolds number "the inherent dissipative properties" of the schemes
     mimic the subgrid dissipation on the coarse grids.
   - **Supersonic isothermal turbulence.**
     [Cernetic et al. (2024)](/sources/cernetic-2024.md) (§2–5) drive
     supersonic isothermal turbulence with a GPU modal
     discontinuous-Galerkin code. The code uses a Legendre total-degree
     basis, not the nodal DGSEM. There is no explicit viscosity or subgrid
     model; the dissipation is numerical plus a von Neumann–Richtmyer
     [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
     at compressions.
   - **Compressor cascade.** [Klose et al. (2025)](/sources/klose-2025.md)
     (§2) choose "the implicit (no-model) LES approach … such that
     dissipation is added implicitly via the numerical dissipation of the
     Riemann solver". The setting is a transonic
     [compressor cascade](/benchmarks/compressor-cascade.md) at
     $Re=1.35\times10^6$. The code is the DGSEM of
     [TRACE](/software/trace.md) ($N=3$, Chandrashekar entropy-conserving
     split form with its Riemann solver, BR1) with
     [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).
   - **GPU DGSEM.** [Kurz et al. (2025)](/sources/kurz-2025.md) run all
     scale-resolving cases of the GPU code [GALÆXI](/software/galaexi.md)
     without an explicit model. The cases are a supersonic Taylor–Green
     vortex and a wall-resolved
     [NASA Rotor 37](/benchmarks/nasa-rotor-37.md) cascade. The
     kinetic-energy-preserving split form and the DG/finite-volume blending
     are the only dissipation. The paper calls the Rotor 37 run
     "wall-resolved LES" and does not use the term implicit LES (§2.2–2.3,
     §6).
   - **Mixed-stress finite elements, transitional airfoil.**
     [Lederer et al. (2026)](/sources/lederer-2026.md) (§3, §3.1) call
     "ILES" their exactly divergence-free hybrid mixed-stress method with
     the upwind jump term as the only dissipation, which acts on the
     high-order part of the solution (citing Moura et al.). They exclude
     explicit SGS models "due to their inferior performance compared to
     ILES in a DG framework for wall-bounded flow problems", citing their
     2023 study and Fernandez et al.
   - **Coarse DGSEM baseline.** [Ranjbar et al. (2026)](/sources/ranjbar-2026.md)
     (§III) run "coarse DNS", the unmodelled DGSEM of
     [HORSES3D](/software/horses3d.md) on the coarse meshes, as the
     baseline of their filter.
   - **Shock/boundary-layer interaction in DGSEM.** [Gao et al. (2022)](/sources/gao-2022.md)
     (§1, §3.1) run a wall-resolved LES of an oblique shock reflection at
     Mach 2 in [FLEXI](/software/flexi.md) with no subgrid model,
     relying "solely" on the dissipation of the interface Riemann solver
     (split-form DGSEM, $N=6$), an approach they call "widely tested and
     accepted within the DG community". Shocks are captured by
     [finite-volume subcells](/methods/subcell-finite-volume-shock-capturing.md)
     switched by a [shock sensor](/definitions/shock-sensor.md) evaluated
     on a spanwise-averaged field, so that the extra dissipation stays out
     of the turbulent boundary layer.
   - **Supersonic twin jets, MILES.** [Ahn et al. (2023)](/sources/ahn-2023.md)
     (§III) run "an implicit LES approach (or monotonically integrated
     large-eddy simulation, MILES)" of over-expanded twin square jets in
     the unstructured finite-volume code EDGE: "no explicit sub-grid-scale
     (SGS) model is implemented … the physical dissipation originated by
     small-scale eddies is implicitly considered by taking the advantage
     of truncation errors". The scheme is second-order central with a
     modified Jameson second/fourth-difference
     [artificial dissipation](/methods/artificial-viscosity-shock-capturing.md)
     switched by a Ducros-type dilatation sensor, applied once per time
     step at the end of the first Runge–Kutta stage.
   - **Shock-capturing schemes run without a model.**
     [Liang & Fu (2024)](/sources/liang-2024.md) (§1, §4.10–4.12) motivate
     their hybrid TENO scheme by "under-resolved large eddy simulations
     (LES) deployed on coarse meshes" and run the Taylor–Green vortex and
     decaying compressible isotropic turbulence with no subgrid model (see
     [WENO schemes](/methods/weno-scheme.md)); [Takagi et al. (2022)](/sources/takagi-2022.md)
     (§1, §5) give the same motivation for a TENO–THINC hybrid but test
     turbulence only with the inviscid Taylor–Green vortex, deferring
     turbulent flows to a later paper.
   - **Workshop case.** The SD7003 wing case (C3.3) of the first High-Order
     CFD Workshop, summarized by [Wang et al. (2013)](/sources/wang-2013.md)
     (§4.13), asks for "implicit LES approaches for handling, in a seamless
     fashion, the mixed laminar, transitional, and turbulent flow regions"
     at $Re_c=60\,000$, $M=0.1$, $\alpha=4^\circ$ and $8^\circ$ (see
     [laminar separation bubble](/definitions/laminar-separation-bubble.md));
     the paper shows no results for it. Its survey reports high-order
     methods as "routinely chosen for LES and DNS of turbulent flows" (§2).
   - **Future extension.** [Liu et al. (2022b)](/sources/liu-2022-g.md)
     (§4) state that their laminar
     [flux-reconstruction](/methods/flux-reconstruction.md)
     fluid–structure solver "can be directly extended into an ILES one" at
     moderately high Reynolds number.
   - **Lattice Boltzmann.** [Husson et al. (2024)](/sources/husson-2024.md)
     (§1) list, beside eddy-viscosity models, implicit LES "where the
     collision operator acts as a subgrid scale model" as an option of
     [lattice-Boltzmann](/methods/lattice-boltzmann-method.md) LES (citing
     Nishimura et al.).
   - **Shock–turbulence interaction in OpenFOAM.**
     [Cheng et al. (2023)](/sources/cheng-2023-b.md) (§1, §2.2) run a
     second-order finite-volume solver (AUSM+-up flux, compact TVD
     reconstruction of primitive variables) as implicit LES: the subgrid
     stress "can be modeled implicitly by the inherent numerical
     dissipation from the shock-capturing schemes". They argue, citing
     Garnier et al., that explicit subgrid models are "not suited to
     shock-vortex and shock-turbulence problems", because they cannot
     account for the intermodal energy transfer among acoustic, entropy
     and vorticity modes and usually miss the conversion of kinetic to
     internal energy across shocks, and they set three requirements on the
     scheme: oscillation-free capture of shocks and shear layers, low
     dissipation for the resolved scales, and stabilization of the
     subgrid scales by the scheme's dissipation (§1). Their reconstruction
     and its dissipation parameters are on
     [numerical dissipation](/properties/numerical-dissipation.md); results
     below.
   - **Dense gas.** [Zhang et al. (2022d)](/sources/zhang-2022-h.md) (§I)
     cite implicit LES of dense-gas flows (Hoarau et al.) as one LES
     family, against which they set an explicit deconvolution closure of
     the real-gas subgrid terms.
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
   number (iSGET) as the energy-transfer part of a hybrid model; Vicente
   Cruz & Lamballais (2023, §1) and Beck & Kurz (2023, §III C) cite MILES
   as the origin of the idea. [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md)
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
   positivity-preserving entropy filter of Dzanic & Witherden (cited). Filtering adds local numerical dissipation to the dissipation
   on which ILES relies as a subgrid model (citing Edoh et al.); the
   Riemann solver contributes too: Rusanov on wall faces, HLLC or Roe
   inside. The filter and solver comparisons are on the
   [subcell finite-volume shock-capturing](/methods/subcell-finite-volume-shock-capturing.md)
   and [numerical dissipation](/properties/numerical-dissipation.md) pages.
   Kurz et al. (2025, §2.3) recall, citing Beck & Kurz, that the
   Hennemann-type DG/finite-volume blending of
   [GALÆXI](/software/galaexi.md) "has also been demonstrated to yield a
   sensible turbulence model if tuned correctly", the RL-Blend idea above.

   **Artificial-dissipation operator on summation-by-parts differences.**
   [Stanly et al. (2022)](/sources/stanly-2022.md) (§2.1, Eq. 1) run the
   compressible code MIRACLES as implicit LES: fourth-order
   summation-by-parts finite differences, fourth-order Runge–Kutta and,
   as the only closure, an eighth-order artificial-dissipation operator
   (Mattsson et al., as cited) with a fourth-order boundary closure, on
   analytically stretched grids. Their application is the
   [actuator-line model](/methods/actuator-line-model.md) of a wind
   turbine; they attribute small differences from an explicit-LES
   reference partly to running their implicit LES on a grid built with
   the explicit-LES criterion (§4.2), and judge their filtered actuator
   line, which allows coarse grids, "more suitable" for LES with explicit
   subgrid models than for implicit LES (§6).

   **Spectral vanishing viscosity under a wall model.**
   [Huang et al. (2022c)](/sources/huang-2022-c.md) (§II B, Eq. 13) run
   SVV implicit LES of the incompressible equations in
   [Nektar++](/software/nektar-plus-plus.md): spectral/hp elements with
   the SVV term $\nu_{\mathrm{svv}}\sum_i\partial_i[\mathcal Q\otimes\partial_i\boldsymbol u]$
   (page-local $\nu_{\mathrm{svv}}$ the dissipation strength, $\mathcal Q$
   the kernel acting on the high modes) as the only regularization; they
   cite the "DG kernel" of Moura et al., calibrated so that continuous
   Galerkin plus SVV mimics upwind DG, but do not state the kernel,
   $\nu_{\mathrm{svv}}$ or cut-off of their own runs (see
   [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)).
   Since an implicit LES has no model coefficient to adjust, they state
   that eddy-viscosity wall-model corrections (dynamic eddy viscosity of
   Cabot & Moin; the Smagorinsky-coefficient constraint of Wu & Meyers)
   are "not applicable", and they couple an algebraic equilibrium wall
   model through a Neumann wall-stress condition that brings no eddy
   viscosity into the equations (§I, §II C; results below and on
   [wall-modelled LES](/methods/wall-modelled-les.md)).

   **Dissipative interpolation and regularization filters.**
   [Caban et al. (2026)](/sources/caban-2026.md) (§3.2, §5) classify as
   ILES two no-model variants of their half-staggered compact-difference
   code: dissipative compact interpolation between velocity and pressure
   nodes (orders 4 to 10), whose induced filter is the square of the
   interpolation transfer function, and spectral (error-free)
   interpolation plus an explicit regularization filter applied to the
   velocity after every time step. That filter is an eighth-order compact
   filter composed with its van Cittert approximate inverse truncated at $N_{\mathrm{AD}}=2$,
   which acts mainly on the smallest scales and is equivalent to the
   relaxation term of the approximate deconvolution model (§3.1, Eq. 17;
   see [scale-similarity models](/methods/scale-similarity-model.md)).
   The derivative-induced filter alone, with spectral interpolation and no
   regularization, is not enough (below); the induced filters are on
   [large-eddy simulation](/definitions/large-eddy-simulation.md).

   **Explicit modal filtering.** Ranjbar et al. (2026, §I, pp. 3–4) present
   low-pass filtering of the DGSEM modes, restricted to elements where the
   local Kolmogorov length is below the grid spacing, as "an alternative
   or complement to subgrid-scale modeling" that "mimics the effects of"
   spectral vanishing viscosity without its extra flux. The method and its
   results are on [explicit modal filtering](/methods/explicit-modal-filtering.md).

   **Relaxation filtering of central differences.** [Volpiani (2024)](/sources/volpiani-2024.md)
   (§1, §2.2.2, §5) stabilizes sixth-order central finite differences by a
   selective (relaxation) filter applied to the conservative variables at
   every step, with no subgrid model, and calls the result implicit LES;
   the filter, optimized for low dissipation at long waves, is the
   designed numerical regularization, and the alternative stabilization
   by kinetic-energy-preserving split forms, which adds no dissipation,
   fails as an implicit LES on coarse grids (below; the filter and its
   coefficients are on [explicit modal filtering](/methods/explicit-modal-filtering.md)).

   **HOPU, second version.** Lederer et al. (2026, §2.3, §3.2) reuse the
   [HOPU method](/methods/high-order-projection-based-upwind-method.md)
   with a Chorin-type projection time integrator instead of the earlier
   IMEX Runge–Kutta scheme, and with other settings of the adaptive
   projection order (thresholds, reversion to standard upwinding, update
   every tenth step); the two settings are versions of the method, listed
   on the HOPU page.
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
   [Reddy et al. (2026)](/sources/reddy-2026.md) (§1, §2.1) take this
   position with explicit closures. Their continuous spectral-element LES
   is implicitly (grid-)filtered, the quadrature-point values being the
   filtered quantities. It carries explicit eddy-viscosity models,
   including the
   [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md).
   They call implicit LES in the sense of usage 1 "very different" from
   their approach.
   [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) (§1, §2.3)
   name the two senses apart: "implicitly filtered LES (iLES)", where the
   numerical dissipation performs the filtering and an explicit SGS model
   is added, against "implicit LES (ILES)", where the truncation error is
   the SGS model. Their "iLES" is usage 3, whereas Kurz et al. (2023) and
   Cao et al. (2024) use "iLES" for no-model runs (usage 1); the
   abbreviation alone does not identify the sense. They add that a scheme
   stable without upwind dissipation lets SGS models "function as
   intended without dissipation interference from upwinding" (§1).
   [Wu & Lele (2026)](/sources/wu-2026.md) (§1, §3.3) state the
   usage-3 premise for supervised learning: the filter of a running LES
   "is implicit and is a product of both the grid and the numerical
   method" (citing Sagaut), and the subgrid-stress statistics depend on
   that filter, so a network trained on one explicit filter (usually a box)
   meets a distribution shift a posteriori. Their remedy is to train on
   several filter shapes rather than to match a solver's filter; see
   [neural-network SGS models](/methods/neural-network-sgs-model.md) and,
   for the opposing design of matching the discretization,
   [discretization-consistent closure](/definitions/discretization-consistent-closure.md).
   [Jakhar et al. (2026)](/sources/jakhar-2026.md) (p. 6) note that
   weather and climate models often operate in implicit-LES regimes and
   propose their closed-form gradient closure there as a diagnostic target
   for interscale transfers, or as an add-on "when an explicit
   representation of backscatter is desired" (see
   [energy backscatter](/definitions/energy-backscatter.md)).

Usages 1 and 2 concern the closure (none, or numerical); usage 3 concerns
the filter. A page or claim about "ILES" should say which.

Volpiani (2024, §1, §5) crosses the two axes explicitly: filtering is
implicit (embedded in the scheme, with unknown size and shape) or explicit
(a filter applied to the discrete solution, with known shape and width),
and LES is implicit (no subgrid model) or explicit (a model). The
relaxation-filtered runs are thus implicit LES that are "explicitly
filtered with a well-defined filter function", while the split-form runs
without filter are implicitly filtered. [Valencia et al. (2026)](/sources/valencia-2026.md)
(§I, §V A) emulate the implicit filter of a centred finite-volume scheme
by a top-hat filter of the grid width in their a priori protocol, and find
that explicitly filtered spectra at a filter-to-grid ratio of one
"essentially overlap" the implicit-LES spectrum: explicit filtering does
not move the grid cutoff, it only damps energy below it (Fig. 3).
[Pan & Zhang (2023)](/sources/pan-2023.md) (§II.D, §III.A) describe the
same LES of a centrifugal impeller as using the
[dynamic Smagorinsky–Lilly model](/methods/dynamic-procedure.md) and as
"the implicit filtered LES approach" of ANSYS-Fluent, citing a work on
implicit LES (Hahn & Drikakis); the paper does not say in which sense
the phrase is meant.

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
  numerically converged in what the authors call the standard condition,
  $\Delta x=\Delta$ (Vicente Cruz & Lamballais
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
  comparable to coarse DNS (Poggie et al.; Ritos et al., cited). They
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
- **Gas-kinetic iLES of channel flow, against explicit models.** Zhao et
  al. (2021, §V, Tables V–VII, Figs. 2–19) compare the realized friction
  Reynolds number. At nominal $Re_\tau=180$ ($96^3$) they find DNS 178.12,
  iLES 177.89, Vreman 174.99, dynamic Smagorinsky 175.47, WALE 172.57,
  dynamic Clark 172.06. At nominal 395 on $96^3$ the values are DNS 392.24,
  iLES 360.35, Vreman 351.36, dynamic Smagorinsky 359.54, dynamic Clark
  351.35, and on $128^3$ iLES 376.33 against 370.13, 375.22 and 369.57.
  "For all cases, the resolved $Re_\tau$ value for iLES is higher than
  those given by the LES schemes" (§V), and iLES is generally closest to
  DNS in mean velocity, r.m.s. fluctuations and $Q$-criterion structures;
  spectra show no visible difference between methods (§V.C). iLES is also
  cheapest per step (0.520 s against 0.534–0.624 s on
  $64\times96\times64$, 16 cores, Table III). The authors attribute the
  outcome to the scheme's numerical dissipation already sufficing as
  subgrid dissipation, so that an explicit model over-dissipates, lowers
  the wall velocity gradient and $u_\tau$, and degrades the profiles
  (Abstract, §VI); no dissipation budget is measured. They conclude that in
  their high-order finite-volume approach iLES is "more suitable than
  traditional LES models" (§VI). Their iLES value at nominal $Re_\tau=395$
  on $96^3$, 360.35, is also the value Zhao et al. (2023a, above; the same
  four authors) print for their fifth-order non-compact run on that grid.
- **Jump penalties against explicit models.** On the Taylor–Green vortex
  at $Re=1600$, $M=0.1$ ($32^3$ elements, $N=3$), unpenalized DG diverges;
  solution and gradient jump penalties above $\tau_s>1.9$ and
  $\tau_g>6.3\times10^{-4}$ (penalty parameters, registry §11, defined on
  the [jump-penalty](/methods/jump-penalty-stabilization.md) page) remove a
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
- **Gas-kinetic iLES of a supersonic channel and a compressible hill.**
  Cao et al. (2024, §3.3–3.4, Tables 4–6, Figs. 5–16).
  - **Channel at $M=1.5$, $Re=3000$ (isothermal walls).** iLES on $128^3$
    gives $Re_\tau=211$, against 213 for their own $160^3$ run labelled
    DNS and 222 and 218 for the reference DNS of Coleman et al. and
    Morinishi et al. (cited by Cao et al.). The non-dimensional wall heat flux is
    −0.047 against −0.049 and −0.048.
  - **Sensitivities in the channel.** Halving the streamwise box "almost
    does not affect" the wall statistics but visibly changes the rms density
    and temperature. Keeping the native unit Prandtl number of the BGK model
    "changes the mean density, temperature and Ma number profiles greatly",
    and $Re_\tau$ rises to 221.
  - **Compressible periodic hill ($Re_b=2800$).** On $10^6$ to
    $1.6\times10^7$ cells the separation and reattachment points are
    0.23/5.18, 0.20/5.15 and 0.24/5.52, against 0.21/5.41 from DNS (Table 6).
  - **The authors' conclusion.** "Coarse grids is enough for iLES" in
    low-Reynolds-number separated flow. The tabulated reattachment points
    (5.18, 5.15, 5.52 from coarse to fine) do not converge monotonically
    *(compiler check, not in the sources)*.
- **Supersonic Taylor–Green vortex, seven codes.** Chapelier et al. (2024,
  §IV.A, Figs. 5–7) find the large-scale kinetic energy captured by all
  solvers from $128^3$ degrees of freedom, and "most turbulent dynamics"
  from $256^3$. On coarser grids "high-order schemes are still able to
  capture a significant part of the small-scale dynamics", and the
  discontinuous finite-element schemes (modal DG, spectral difference,
  DGSEM) "seem to be efficient in that respect".
- **High-order DG against finite volume in supersonic turbulence.**
  Cernetic et al. (2024, §5–6, Figs. 5, 8, 10–11) compare modal DG with a
  second-order finite-volume scheme at equal cell count.
  - **Subsonic Mach numbers.** DG extends the resolved spectral range
    markedly.
  - **Supersonic Mach numbers.** The advantage "nearly disappears".
  - **Sonic scale at $M=3.2$.** Second-order DG at $1024^3$ resolves the
    sonic scale. DG at $512^3$ "does nearly as well as" finite volume at
    $1024^3$, and finite volume at $512^3$ shows no trace of it.
  - **Bottleneck.** Lower numerical dissipation also gives DG a more
    pronounced [bottleneck](/definitions/bottleneck-effect.md).
- **Regularized compact differences, transitional Taylor–Green vortex.**
  Caban et al. (2026, §5.3–5.4, Tables 4–9) run LES on $64^3$ at $Re=1600$
  (DNS on $256^3$ and $384^3$) and rank by the time-integrated relative
  error of the kinetic energy up to $t=20$.
  - **ILES.** With the regularization filter, or with tenth-order
    dissipative interpolation, the error is $2.23\times10^{-2}$, about half
    the best eddy-viscosity result (Vreman with the regularization filter,
    $4.33\times10^{-2}$; Smagorinsky $4.76\times10^{-2}$, both at
    $\Delta=2h$). With sixth- or tenth-order derivatives and the
    regularization filter, ILES is stable and more accurate than the ALDM
    implicit LES of Hickel et al. (cited) (§5.3.1, Fig. 19).
  - **Explicit models on top.** Eddy-viscosity models combined with the
    dissipative interpolation or the regularization filter are stable but
    worse than ILES: the total dissipation is too large (§5.3.1, Fig. 20).
  - **Overall ranking.** Layton–Lewandowski model with the regularization
    filter (best $2.03\times10^{-2}$, "10% lower" than the best ILES)
    $\lesssim$ ILES $<$ best approximate deconvolution model
    ($\approx2.3\times10^{-2}$) $<$ eddy-viscosity models (§5.4, §6). The
    deconvolution model "requires some level of numerical dissipation" to
    stay stable (§5.4.2). The authors limit the ranking to this Reynolds
    number and grid.
- **Entropy-stable flux reconstruction, free-shear turbulence.** Brillon &
  Nadarajah (2026) run nonlinearly stable
  [flux reconstruction](/methods/flux-reconstruction.md) (split form,
  entropy-conserving two-point flux, no upwinding, no over-integration).
  - **Stability.** It is stable on every under-resolved Taylor–Green grid
    ($Re=1600$, 96$^3$ to 24$^3$ degrees of freedom, $N=5$ and 7) without
    added dissipation, and at $96^3$ ($N=5$) the dissipation rate follows
    the DNS up to its peak (§3.1.2, Fig. 8).
  - **Explicit models.** Smagorinsky, shear-improved, high-pass-filtered
    and dynamic variants marginally raise the dissipation rate, lower the
    peak enstrophy and remove energy at the smallest resolved scales,
    where the no-model run already has a deficit; "the SGS models
    considered in this work are not recommended for the LES of
    transitional turbulent free-shear flows using NSFR" (§3.1.8, Fig. 19).
  - **Decaying grid turbulence.** At $128^3$ degrees of freedom ($N=3$)
    the Comte-Bellot–Corrsin spectra agree with experiment and the
    kinetic-energy error at the last station is 1.36%, against 29.81%
    (finite differences, $64^3$) and 15.55% and 29.75% (CPR, $78^3$ and
    $126^3$), lower errors the authors expect to be "partially due" to more
    unique degrees of freedom and to oversampled spectra (§3.2, Table 6).
- **Transitional airfoil.** On the [Eppler 387](/benchmarks/eppler-387-airfoil.md)
  airfoil ($Re=10^5$ at $10^\circ$, $3\times10^5$ at $4^\circ$; $k=3$
  elements, the paper's $k$ being the polynomial degree $N$), ILES and HOPU
  give essentially the same pressure distribution, lift, drag and
  separation-bubble positions, e.g. lift 1.274 and 1.271 against 1.200
  measured at $10^\circ$ on the coarsest mesh. In the turbulent boundary
  layer HOPU overpredicts the mean velocity and turbulent kinetic energy
  less for $n^+>10$ ($n$ the wall distance), and on the coarsest mesh does
  "almost as well as" ILES on the finest (Lederer et al. 2026, §4.1–4.2,
  Table 2, Figs. 7–9). The finest ILES mesh predicts transition well
  against experiment, which the authors credit to the low dissipation of
  the method (§5).

- **Relaxation-filtered central differences, Taylor–Green vortex.**
  Volpiani (2024, §5, Figs. 6–10, 15–18) finds the filtered implicit LES
  the best of all the paper's runs at $Re=1600$: it predicts the kinetic-energy
  dissipation rate $-d\mathcal K/dt$ ($\mathcal K$ the volume-averaged kinetic energy, page-local) well on $64^3$ to $512^3$ while
  under-predicting the enstrophy-based rate on coarse grids, which the author reads
  as under-resolved structures whose energy drain the filter carries; with
  the new optimized filter on $128^3$ it agrees with the DNS of Dairay et
  al. (2017, cited) at $Re=2500$, 5000 and 10000. "Regardless of the model, the
  best result is achieved for the implicit LES with RF with the optimized
  filter and no SGS model": Smagorinsky, multiscale Smagorinsky and
  dynamic models on split forms do worse, and the author concludes that
  implicit and explicit LES are both viable "as long as dissipation is
  carefully tuned and guided by the physics", implicit LES being faster
  (§6).
- **Shock-capturing hybrids, Taylor–Green vortex and isotropic
  turbulence.** Liang & Fu (2024, §4.11–4.12, Figs. 19–21) report that
  their TENO-S scheme without a model agrees with DNS in the dissipation
  rate of the viscous Taylor–Green vortex at $Re=100$–3000 on $64^3$ and
  $Re=5000$, 10000 on $128^3$, and in decaying compressible isotropic
  turbulence ($M_t=0.6$, $Re_\lambda=100$, $64^3$ against filtered
  $256^3$ DNS), "significantly better" than WENO-CU6, TENO6 and TENO8,
  whose dissipation it reduces by switching to a non-dissipative split
  form in smooth cells.
- **Shock/boundary-layer interaction in DGSEM.** Gao et al. (2022,
  §5.3.1) place separation at $16.7\delta_r$ and reattachment at
  $19.5\delta_r$ against $17.6\delta_r$ and $19.3\delta_r$ in a reference
  LES, and see the skin-friction plateau that, per that reference, appears
  only at sufficient resolution, on a much coarser grid ($N=6$, about
  93 million degrees of freedom); see
  [shock–turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- **Supersonic jets.** The MILES of Ahn et al. (2023, §IV D, Fig. 22,
  Table II) reproduces the far-field overall sound pressure level and the
  screech frequency (7928 Hz against 8172 Hz measured) through a
  [Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
  surface, and its velocity spectra follow the $-5/3$ slope "for about one
  order of magnitude", which the authors take as sufficient resolution
  (§IV C 1, Fig. 12).
- **Shock-capturing scheme with one dissipation knob.** [Deng et al. (2022)](/sources/deng-2022.md)
  add to their polynomial/THINC boundary-variation-diminishing finite-volume
  schemes a stage that blends the two face values with a parameter
  $\lambda_{\mathrm{AD}}$ (page-local): $\lambda_{\mathrm{AD}}=1$ is the
  upwind-biased scheme of order $n+1$, $\lambda_{\mathrm{AD}}=0.5$ the
  non-dissipative central scheme of order $n+2$ (§3.2). In ILES of decaying
  compressible isotropic turbulence with eddy shocklets ($M_t=0.6$,
  Taylor-scale Reynolds number 100) on $64^3$ with
  $\lambda_{\mathrm{AD}}=0.75$, every order gives a velocity spectrum at
  four eddy-turnover times closer to the $256^3$ DNS than ninth-order
  WENO-M ILES, and the tenth-order variant is close to the DNS; lowering
  $\lambda_{\mathrm{AD}}$ improves the spectrum further, and on $128^3$ both
  0.75 and 0.5 converge to the DNS (§4.15, Figs. 23–25). The authors
  recommend $\lambda_{\mathrm{AD}}=0.5$ for DNS and explicit LES and a
  larger value as the ILES dissipation, which "is believed to work" in
  place of a subgrid model (Remark 2); see
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
- **Compact interpolation instead of explicit.** [Ma et al. (2022)](/sources/ma-2022.md)
  replace the explicit fifth-order nonlinear interpolation of the weighted
  compact nonlinear scheme (WCNS) by a seventh-order nonlinear tri-diagonal
  compact interpolation on the same five-point stencil (WCNS-T, §2.2). With
  no subgrid model, WCNS-T follows the DNS dissipation rate of the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) in peak height
  and transition time, and gives better near-wake profiles and wake spectra
  of the [circular cylinder](/benchmarks/circular-cylinder-wake.md) at
  $Re_D=3900$ and better wall pressure on the T106A
  [turbine cascade](/benchmarks/turbine-cascade.md) than the explicit
  version (§3.1–3.3, Figs. 5–12). The authors conclude that WCNS "is not
  over-dissipative anymore for ILES" (§4); no error norms are given for the
  ILES cases.
- **Filter as the only model.** [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md)
  call their unfiltered flux-reconstruction runs ILES and their runs with an
  optimized [explicit modal filter](/methods/explicit-modal-filtering.md)
  "LES"; in a channel at $Re_\tau=395$ with 3/8 of the DNS degrees of
  freedom the unfiltered runs are stable at $N=3$ and $4$, and the $N=5$
  run is stable only with the filter (§5.1). On a stalled NACA0020 at
  $Re_c=20\,000$, unfiltered ILES and filtered LES give $C_L=0.639$, $0.651$
  and $C_D=0.353$, $0.357$ against 0.64 and 0.35 in DNS (§5.2, Table 3).
- **Lattice Boltzmann without a model.** [Simonis et al. (2022)](/sources/simonis-2022.md)
  conjecture that under-resolved multiple-relaxation-time lattice Boltzmann
  simulation "already acts as an implicit LES": in the Taylor–Green vortex
  at $Re=3000$ on $64^3$ the dissipation not accounted for by the enstrophy,
  $\epsilon_{\mathrm{mod}}=\epsilon_{\mathrm{tot}}-\epsilon_{\mathrm{res}}$ in
  their notation, is about half of the total, and its share decreases with
  refinement at the same magnitude with and without their explicit temporal
  closure (§3.3.2, §3.4, Figs. 7, 9); see the
  [lattice Boltzmann method](/methods/lattice-boltzmann-method.md). The
  "model" share includes every dissipation not captured by the enstrophy,
  compressibility effects of the weakly compressible scheme included
  (§3.4, where the compressibility defect is named the main cause of an
  error plateau).
- **Implicit against explicit LES on the same grid, with the dissipation
  budget.** [Cao et al. (2022b)](/sources/cao-2022-c.md) ask why their
  implicit LES with a fourth-order finite-volume
  [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) had beaten
  explicit eddy-viscosity LES in earlier compressible periodic-hill runs
  (§I). On the compressible
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at Mach 0.1,
  $Re=1600$, $256^3$ cells, against $1024^3$ DNS, the explicit models enter
  the kinetic solver through an enlarged collision time
  $\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$, with the cell as
  implicit filter: static [Smagorinsky](/methods/smagorinsky-model.md)
  ($C_s=0.1$), [Vreman](/methods/vreman-model.md) ($C_v=2.5C_s^2=0.025$,
  page-local $C_v$) and the [dynamic procedure](/methods/dynamic-procedure.md)
  with a top-hat test filter of twice the width and a domain-averaged
  coefficient (§III, Eqs. 7–13). Kinetic energy and its total decay rate
  are insensitive to the choice; the enstrophy-based and solenoidal
  dissipations are closest to DNS with implicit LES, and the dynamic model
  is the best explicit one (§IV A, Figs. 1–3). Writing the discrete
  equation with a numerical subgrid stress $\tau^{\mathrm{num}}_{ij}$ beside the
  modelled one, after Moser et al. (Eq. 20), they estimate the total
  subgrid dissipation as $-\mathrm dE_k/\mathrm dt$ minus the physical
  dissipation (Eq. 22): modelled and numerical parts together for explicit
  LES, numerical only for implicit LES. The static models give about twice
  the implicit value at $t=2.5$–10 and the dynamic model lies between,
  its domain-averaged coefficient being always positive in this flow
  (§IV C, Table II). The authors conclude that the scheme's dissipation is
  a built-in subgrid dissipation sufficient for this low-Reynolds-number
  flow, that the added eddy viscosity "pollutes" the resolved vorticity,
  and that explicit LES should not be "a holy grail" on under-resolved
  grids without considering the numerics (§IV C, §V). On $128^3$ and
  $384^3$ the ranking holds; static explicit LES on $384^3$ only matches
  implicit LES on $256^3$ (App. B, Figs. 9–12). The decomposition is on
  [numerical dissipation](/properties/numerical-dissipation.md), the a
  priori comparison on
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
- **Low-order TVD-type reconstruction, transonic cavity.** Cheng et al.
  (2023, §3.6, Figs. 9–14) run their compact-stencil implicit LES on the
  Mach 0.8 deep cavity of Forestier et al. ($Re=8.6\times10^5$ on the
  cavity length $L$, 10.36 million cells, smallest $L/120$, 60 shedding
  cycles). The mean velocities of all their schemes agree with the
  experiment and are mostly comparable to a fifth-order implicit LES of
  Thornber & Drikakis on its own grid; the classical TVD limiters (van
  Leer, MUSCL) underestimate the Reynolds stresses "due to numerical
  dissipation", the fifth-order reference "tends to slightly
  overestimate" them and overestimates the fluctuating energy near the
  upstream wall, and the lower-dissipation reconstructions come closest
  to the measured peak there. The grids differ between the two
  computations, which the authors note ("may benefit from the finer grid
  size"); no cost is reported.
- **Wall-modelled SVV implicit LES of channel flow.** Huang et al.
  (2022c, §III, Table I, Figs. 3–9) run turbulent channel flow at
  $Re_\tau=550$, 950 and 2000 on one mesh of $12\times6\times10$ hexahedra
  with "polynomial order $N_p=7$" as printed, matching height at the top of
  the first element, $0.224\delta$. The mean velocity is "almost not
  distinguishable" from DNS at $Re_\tau=550$ and over-predicted by at most
  2% and 5.4% at 950 and 2000; the r.m.s. fluctuations and the Reynolds
  shear stress agree away from the wall but show a "parabolic" error near
  the matching interface. At $Re_\tau=550$ the computation is reported up
  to seven times cheaper than wall-resolved SVV implicit LES with the same
  outer mesh (no timing data). At similar resolution a mesh with fewer,
  higher-order elements gives better fluctuations than one with more,
  lower-order elements (§III E).

## Evidence: when it fails

- **Split forms without dissipation.** Volpiani (2024, §5, Figs. 11–13)
  finds that kinetic-energy-preserving split forms without a model are
  "extremely noisy" on $64^3$ and $128^3$ in the Taylor–Green vortex at
  $Re=1600$: aliased energy builds up at high wavenumber for every split
  form and contaminates even low wavenumbers, so the split forms are
  "unsuited to perform implicit large-eddy simulations" (Abstract); a
  weak relaxation filter ($\chi_f=0.01$, the filter strength of registry
  §11, see [explicit modal filtering](/methods/explicit-modal-filtering.md)) removes
  the pile-up (Fig. 18).
- **Near-nozzle shear layers.** In the jet MILES of Ahn et al. (2023,
  §IV B, Figs. 6–10) both runs give much higher turbulent kinetic energy
  than PIV at one and two nozzle heights downstream and slightly over-predict the
  shock-cell strength; boundary-layer tripping inside the nozzle reduces
  but does not remove the excess (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
  The nozzle wall is not resolved ($y^+$ 10–20, no wall model).

- **Applicability plateau.** At $48^3$ degrees of freedom ($6^3$ elements,
  $N=7$), where only about 0.9% of the dissipation is resolved, DG ILES
  piles energy up at mid wavenumbers and drops sharply near the cutoff;
  changing the Riemann solver (Roe, Lax–Friedrichs, low-dissipation Roe) or
  adding a Smagorinsky or small–small VMS model on top does not help.
  Flad & Gassner (2017, §1) conclude that roughly 40% of the total
  dissipation must be resolved for de-aliased upwind DG ILES to work, a
  threshold drawn from two resolutions of one case. The remedy they
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
  split-form DG at $48^3$, stable but without a model. Inviscid runs of
  the non-dissipative second-order kinetic-energy- and entropy-preserving
  central scheme of [Kuya et al. (2018)](/sources/kuya-2018.md) (§5,
  Taylor–Green vortex on $64^3$, isotropic turbulence on $32^3$) are used
  by the paper as stability tests at infinite Reynolds number, with no
  model; they show which split forms stay bounded with no dissipation at
  all (see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)). Agrawal et al. (2022,
  §VII.C) see $k^2$ equipartition in a no-model run of HIT at
  $Re_\lambda\to\infty$. [Kim et al. (2024)](/sources/kim-2024.md) (§2.1,
  Table 3, App. C) state that their second-order central,
  kinetic-energy-conserving scheme has no numerical dissipation: no-model
  LES of the [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
  is stable but inaccurate (recirculation length $L_r/D=1.25$ against 1.56
  from DNS at $Re_D=3900$; $L_r$ registry §11) and diverges on very coarse
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
  with earlier stabilized-method studies (cited). On the fine mesh
  the residual, and so the stabilization, matters less. The implicit model
  of this scheme therefore depends on $\Delta t$ through the stabilization
  parameter (§2.4, Eq. 10; §4.2). At $Re_h=10\,600$ and
  37 000 the velocity is reasonable but the Reynolds stresses are
  over-predicted, more so at 37 000 (§4.4).
- **Aliasing.** On the periodic hill at $Re_h=10\,595$ with 64×64×32
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
  reattachment length ($x_R$, registry §11) $x_R/H=7.60$ (+16.7% against the experimental 6.51),
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
  aliasing following Gassner et al. (cited), and in a 2D compressible
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
- **Modal relaxation filter in wall-modelled spectral-element LES.**
  [Mukha et al. (2025)](/sources/mukha-2025.md) (§III.C, Fig. 8) follow
  Gillyns et al. in using Nek5000's high-pass relaxation filter as an
  implicit subgrid model. They filter two modes with strength 100.
  - In channel flow at $Re_\tau\approx8000$ ($N=7$) the filter gives
    stronger near-wall oscillations and over-predicts $\langle u'u'\rangle$.
  - The wall stress computed from the mean wall gradient then misses the
    modelled one by −84.85%.
  - The authors conclude that filtering alone "does not introduce enough
    damping to avoid the contamination of the solution with numerical
    artifacts". Explicit models stabilize better (see
    [Vreman model](/methods/vreman-model.md) and
    [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)).
- **Pile-up with dissipation-free central schemes.** On the supersonic
  Taylor–Green vortex at $64^3$, the central finite-difference codes
  without dissipation (kinetic-energy- and entropy-preserving, or compact
  with a high-order filter) predict the kinetic energy very accurately up
  to $t\approx12$. Their levels are slightly too high afterwards, which the
  authors explain by a small-scale energy pile-up at the cutoff "and the
  lack of an SGS closure" (Chapelier et al. 2024, §IV.A, Fig. 5).
- **Under-resolved shock buffet.** In the compressor-cascade LES of Klose
  et al. (2025, §6–7, Table 2) the coarse-grid solutions "should be
  considered under-resolved". The shock-oscillation amplitude grows from
  0.172 to 0.231 chords when the resolution is refined at fixed span. The
  authors "assume that the increased numerical dissipation of the URANS
  and, to a lesser extent, the coarser LES, damps out flow structures that
  are driving the larger shock oscillations". Shocklets in the coarse run
  also appear more diffused.
- **Derivative-induced filtering is not a closure.** In the laminar
  Taylor–Green vortex the effective Reynolds number from the energy decay
  stays at about the physical one with spectral interpolation, so the
  derivative-induced filtering removes no energy, whereas dissipative
  interpolation or the regularization filter lower it, fourth-order
  interpolation "several times" (Caban et al. 2026, §5.1, Figs. 10–11). In
  the transitional case on $64^3$, spectral interpolation without a model
  is unstable near $t=3.5$, the time at which Hickel et al.'s no-model run
  fails, and near $t=10$ on $256^3$; Smagorinsky and Vreman at
  $\Delta=2h$ do not stabilize it (§5.3.1, Fig. 18). With second-order
  derivatives and the regularization filter the ILES is unstable
  ($\varepsilon<0$ for $t=5.5$–7), which the authors attribute to the
  second-derivative filter damping the viscous dissipation; fourth-order
  instead of tenth-order interpolation raises the ILES error by an order
  of magnitude, to $2.84\times10^{-1}$ (Table 4).
- **Over-predicted energy on coarse DGSEM.** Without filtering, the coarse
  DGSEM runs of Ranjbar et al. (2026, §III.A–C, Figs. 3, 13–15)
  over-predict the kinetic energy of decaying isotropic turbulence,
  over- and then under-predict the Taylor–Green dissipation rate, and
  over-predict all r.m.s. velocities in channel flow at $Re_\tau=395$,
  with non-zero wall fluctuations from the weakly imposed boundary
  condition.
- **Not de-aliased.** Strong-form DG without over-integration fails in the
  transitional phase of the Taylor–Green vortex ($t^*\approx6$, $64^3$,
  $N=7$): "a linearly stable scheme can be unstable in the absence of
  over-integration" (Brillon & Nadarajah 2026, §3.1.3, Fig. 11). A
  high-pass-filtered shear-improved Smagorinsky model stabilizes the
  non-de-aliased $N=5$ scheme but gives inaccurate dissipation and
  spectra, whereas the over-integrated scheme follows the DNS (§3.1.8,
  Fig. 20).
- **Explicit WCNS interpolation.** Ma et al. (2022, §1, §2.2) recall,
  citing Ishiko & Shimada and Matsukawa, that the dissipation of the
  original weighted compact nonlinear scheme "imitates" a strongly
  dissipative subgrid model, so that WCNS-based ILES is ineffective, and
  trace it to the explicit interpolation step. On the T106A cascade even
  its *linear* version captures the leading-edge separation that the
  nonlinear version misses (§3.3, Fig. 12).
- **Linearly unstable continuity equation.** [Svärd (2022)](/sources/svard-2022.md)
  (§3, §5.2) recalls that entropy-conservative and kinetic-energy-preserving
  split fluxes are not locally linearly stable, and shows on a 2-D
  Kelvin–Helmholtz instability that numerical errors amplified by such
  schemes "trip" spurious roll-ups. With physical viscosity
  $\mu=\kappa=10^{-4}$, the box mean of the density changes by 4.1% from
  $128^2$ to $512^2$ with Chandrashekar's flux against 1.8% with the
  author's stabilized flux (Tables 1, 3); without viscosity the box means
  are not on a convergent path up to $1024^2$ (Table 2). "What may look
  like turbulent features in under-resolved simulations may be unphysical
  numerical errors amplified by the scheme"; the most detailed solutions
  are the least accurate (§5.2.1).
- **Hyperviscosity-stabilized pseudospectral runs.** In the
  subgrid-model comparison of [Wang et al. (2022)](/sources/wang-2022-j.md),
  the implicit-LES baseline of forced isotropic turbulence ($128^3$,
  pseudospectral, filtered-DNS reference at $Re_\lambda\approx250$) needs
  an artificially adjusted hyperviscosity to keep its spectrum near DNS:
  "Otherwise, the ILES always diverges in the simulation" (§IV, no
  divergence shown); its strain-rate PDFs are wider than filtered DNS and
  peak at the wrong place (Figs. 3–4). In a weakly compressible temporal
  mixing layer (eighth-order finite differences, $64\times128\times128$)
  the implicit LES matches the momentum thickness but cannot recover the
  filtered energy spectrum and over-predicts the kinetic energy, where
  the explicit models do better (§V, Figs. 9–12; see
  [temporal mixing layer](/benchmarks/temporal-mixing-layer.md)). The
  dissipation mechanism of the mixing-layer run is not described.

## A DNS that is an implicit LES for some modes

[Beattie et al. (2025)](/sources/beattie-2025.md) (§6, App. D, §9.1) apply
the no-model diagnosis to compressible "DNS" that set only a shear
viscosity. In their finite-volume MHD runs at rms Mach number about 1
(FLASH, $Re=1000$), the compressible velocity modes have no physical
dissipation when the [bulk viscosity](/definitions/bulk-viscosity.md) is
zero. Their decay is then "governed completely by numerical dissipation",
set by the flux discretization, the Riemann solver and the resolution
(§1).

- **Pile-up.** The compressible modes pile up at high wavenumbers in a
  [bottleneck](/definitions/bottleneck-effect.md).
- **No convergence.** The ratio of compressible to solenoidal spectra
  should "grow unbounded" with resolution, "exactly what one expects for an
  ILES" (App. D).
- **The authors' conclusion (§9.1).** Without bulk viscosity "the grid
  controls the dissipation of the compressible modes". This turns "what is
  usually considered a direct numerical simulation (DNS) into an implicit
  large eddy simulation for the compressible modes". They hold that a
  compressible DNS needs a bulk viscosity comparable to the shear one.
- **Resolution evidence (App. D).** With bulk viscosity ten times the shear
  viscosity, their run converges on all scales at $512^3$. With equal
  viscosities the bulk-viscous scale is not resolved even at $1024^3$.

See [direct numerical simulation](/definitions/direct-numerical-simulation.md)
and [compressible MHD turbulence](/results/compressible-mhd-turbulence.md).

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

## Numerical diffusion as a combustion closure (inline)

[Cuenot et al. (2022)](/sources/cuenot-2022.md) (§1, §6) separate their
[thickened flame model](/methods/thickened-flame-model.md), which they call
"totally different from pdf-based or viscosity-based (ILES) methods", from
implicit LES. On coarse grids numerical diffusion thickens a diffusion
flame and raises its consumption rate (printed as up to +65% at a flame
resolution of two cells in laminar counterflow, §4; their Table 2 value
$F=2.575$ corresponds to +60.5% by their Eq. 14 *(compiler check, not in
the sources)*, see
[numerical dissipation](/properties/numerical-dissipation.md)), and their proposed
correction divides the diffusivities by $F_{\mathrm{LES}}=F_{\mathrm{num}}F_{\mathrm{sgs}}$,
a numerical factor times a subgrid one. $F_{\mathrm{LES}}\approx1$ means
that "numerical diffusion compensates subgrid effects", which they offer
as the reason why LES with and without a subgrid combustion model gave
similar results in an earlier study (Breda et al., cited; §6). The
correction is a proposal: $F_{\mathrm{sgs}}$ is not modelled and no
turbulent flame is computed.

## Residual-based stabilization as the closure (inline)

In stabilized finite elements the implicit closure is a set of
residual-driven terms rather than a truncation error.
[Chen et al. (2022)](/sources/chen-2022-g.md) (§1, §7) classify
residual-based [variational multiscale](/methods/variational-multiscale-method.md)
LES as an implicit LES whose small-scale model is "an addition of purely
dissipative numerical terms and no eddy viscosity is introduced", and
budget the dissipation of each term in a channel at $Re_\tau=180$; one
cross-stress term turns out to add energy on average, and reversing its
sign improves the outer-layer mean velocity on their coarse mesh (§5–6).
They hold that, being residual-based, this closure keeps numerical
consistency and full convergence rate, "whereas, e.g. the convergence rate
of the classical LES is limited to $O(h^{4/3})$ due to the artificial
viscosity effects" (§1, citing Bazilevs et al. and Hughes et al.).
Prieto Saavedra et al. (2024), above, use the SUPG/PSPG truncation of the
same closure.

## Weak entropy solutions as an a posteriori filter (inline)

[Svärd (2022)](/sources/svard-2022.md) gives implicit LES a rationale
different from the truncation-error-as-filter one. The author distinguishes
three senses (§2.2): fixed-width LES, whose grid-converged solution solves
the filtered equations; "vanishing LES" with $\Delta\propto h$; and ILES.
Only the last two converge, if at all, to a DNS, and "there are no strong
reasons to assume" that they do without the a priori estimates a
convergence theory needs. Instead, a scheme that converges weakly to a
weak entropy solution makes integrals against a fixed test function
converge, $(\Phi,U_h)\to\int\phi u\,dx$, before point values do: local
averages over a fixed support are LES-like quantities filtered *a
posteriori*, and the larger the support the coarser the grid on which
they converge (§2.3, Eq. 9). Accuracy is judged by refining until the
functional of interest stops changing.

From the estimates of the compressible Navier–Stokes–Fourier system the
author conjectures five necessary conditions on such a scheme (§3):
conservation form; [entropy stability](/properties/entropy-conservation.md);
at least the diffusion of a [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
flux; positive density; and a linearly stable (non-anti-diffusive)
continuity equation; a temperature-dependent conductivity
$\kappa\propto1+T^2$ is also required. The proposed finite-volume flux adds
an artificial diffusion $\lambda^\rho_{i+1/2}=\lvert\bar u\rvert/2+\lvert\Delta u\rvert/4$
(page-local; arithmetic mean and jump of the face states) to the mass flux
of Chandrashekar's entropy-conservative flux only, and reuses that mass
flux in the momentum and energy fluxes; Proposition 4.1 states that it
satisfies the five conditions (§4, Eqs. 20–23). The author also argues that
upwind dissipation, $\nu_t\sim h\lvert u\rvert$, corresponds to a turbulent
cell Reynolds number of order one and "can not be ruled out" as a subgrid
model (§3.1). On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $Re=1600$ the scheme, first order in its viscous terms and with forward
Euler stepping, reaches peak dissipation 0.0116 on $64^3$ (Table 5), which
the author calls the same peak as that of a second-order scheme on $129^3$
quoted from earlier work ($\approx0.0115$, §5.3).

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
  explicit SGS modelling "cannot be evidenced", and invert the
  justification of ILES: explicit models such as Smagorinsky's "should be
  seen as an ersatz of regularization". Beck & Kurz (2023, §V A) reach a
  related conclusion from the other side: no reference model is best for
  all discretizations, so closure and discretization must be designed
  together.
- [Goc et al. (2021)](/sources/goc-2021.md) (§2.3), who run explicit SGS
  models, state that low-dissipation numerics are essential because
  numerical dissipation is "extremely detrimental" for coarse LES (Mittal &
  Moin 1997, cited): the opposite design choice to usage 2.

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
- Cao et al. (2024, §3.3) label a $160^3$ run of the same gas-kinetic
  scheme "DNS" and a $128^3$ run "iLES". Beattie et al. (2025) call a run
  labelled DNS an implicit LES for the modes it does not dissipate
  physically (above).
- Chapelier et al. (2024, §IV.A, §V) treat their coarse runs as implicit
  LES on the assumption that numerical dissipation mimics subgrid
  dissipation at $Re=1600$. Their synthesis of a "low impact" of shock
  capturing on the turbulent scales (§V) stands next to their per-code
  remark (§IV.A) that the "strong shock capturing strategy" of SD3D "is
  probably hindering to some extent the development of small scales on the
  finer grids".
- The version read for Cao et al. (2024) is the 2021 arXiv preprint, and
  for Reddy et al. (2026) a 2021 preprint; their versions of record may
  differ. Brillon & Nadarajah (2026, arXiv v1 of 2024), Lederer et al.
  (2026, arXiv v1 of 2024), Ranjbar et al. (2026, arXiv v1), Jakhar et al.
  (2026, arXiv v3) and Wu & Lele (2026, arXiv v2) are also cited in the
  versions read.
- Brillon & Nadarajah (2026, §3.1.8) find explicit eddy-viscosity models
  unhelpful on dissipation-free entropy-stable flux reconstruction at
  $96^3$ degrees of freedom, while Flad & Gassner (2017, §4) propose a
  dissipation-free kinetic-energy-preserving DG baseline plus an explicit
  Smagorinsky model for decaying isotropic turbulence at $48^3$. Flows,
  resolutions and schemes differ, and Brillon & Nadarajah limit their
  verdict to transitional free-shear flow, so no contradiction is
  recorded.
- Zhao et al. (2021) state in the abstract and conclusions that iLES is
  superior for the Reynolds stress, while their §V.B reports for
  $Re_\tau=180$ that "for the Reynolds stress, the results for D-model
  [dynamic Smagorinsky] match better with DNS, followed by iLES"; the iLES
  advantage in Reynolds stress holds at $Re_\tau=395$ only. Their
  explanation for the dynamic Smagorinsky model being the best explicit
  model reads "the numerical dissipation in this model is relatively small
  as a result of the dynamic coefficient" (§V.B; §VI). The Vreman constant
  differs between the Reynolds numbers (0.01 at 180, best of a scan;
  0.07 at 395, after Vreman; §IV), and no WALE results are shown at 395
  although §IV gives its constant for that case.
- Caban et al. (2026, §5.3.1) attribute the stability of Hickel et al.'s
  Smagorinsky run to its larger constant ($C_s=0.18$ against their 0.1),
  a hypothesis supported only by their $\Delta=4h$ run giving similar
  discrepancies.
- Svärd (2022) announces in the abstract "a turbulent Rayleigh-Taylor
  problem" as the third test; the paper runs a Taylor–Green vortex. In §5.3
  the reference peak dissipation is printed "close to 0.0013", against
  0.0086–0.0136 in the author's own Table 5 and "$\approx0.0115$" for the
  quoted second-order scheme.
- Simonis et al. (2022, Eq. 25) print the enstrophy-based dissipation as
  $\epsilon_{\mathrm{res}}=2\pi\nu\zeta$ with $\zeta$ the volume average of
  $\lvert\nabla\times\boldsymbol u\rvert^2$ (Eq. 23); for incompressible
  periodic flow the paper's own definitions give $-dk/dt=\nu\zeta$, without
  the factor $2\pi$ *(compiler check, not in the sources)*. Whether the
  factor enters their computed $\epsilon_{\mathrm{mod}}$ is not determinable
  from the paper.
- Hamedi & Vermeire (2022) optimize their filters on the inviscid
  Taylor–Green vortex and apply them unchanged to the other cases (§3.4,
  §4–5); Deng et al. (2022) vary $\lambda_{\mathrm{AD}}$ in their isotropic
  ILES and compare each value with the DNS spectrum (§4.15).
- **Cao et al. (2022b): "two times" and one flow.** The static explicit
  models give "approximately two times" the implicit total subgrid
  dissipation; Table II gives ratios of 1.9, 2.5 and 2.1 (Smagorinsky) at
  $t=2.5$, 5 and 10 but about 14 at $t=15$ (Vreman: 1.7, 2.3, 1.9, 10)
  *(compiler check, not in the sources)*. The conclusion that explicit
  modelled dissipation is not required is drawn from one flow (Mach 0.1,
  $Re=1600$) and one fourth-order scheme; the authors defer higher Mach
  numbers, where shocklets make the numerical dissipation depend on the
  shock-capturing scheme (§V).
- **Huang et al. (2022c): what "$N_p=7$" means.** The printed spacings
  ($\Delta x\simeq0.087\delta$, $\Delta z\simeq0.052\delta$,
  $\Delta y_1\simeq0.037\delta$) equal the element sizes divided by
  $N_p-1=6$, not by 7 *(compiler check, not in the sources)*. The paper attributes the near-interface error to the wall
  gradient increasing "the eddy viscosity" (§III B), although its SVV
  equations (Eq. 13) contain no eddy viscosity.
- **Cheng et al. (2023)** state that their reconstructions satisfy the
  TVD condition without proof (§2.2), and report no time integrator,
  time step or cost; the deep-cavity comparison with fifth-order implicit
  LES is at different resolutions.

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
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv v1: §1; §3.3, Tables 4–5, Figs. 5–9; §3.4, Table 6, Figs. 10–16.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL accepted manuscript: §III.B; §IV.A, Figs. 5–7; §V.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — arXiv v2: §2–3.1; §5, Fig. 5; §6, Figs. 8, 10–11.
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2; §3; §6, Table 2; §7.1.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §2.2–2.3; §5.2; §6.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.A, Eq. (4); §III.C, Fig. 8.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §1; §2.1.
- [Beattie et al. (2025)](/sources/beattie-2025.md) — arXiv v4: §1; §6.1–6.2, Fig. 9; §9.1; App. D.
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.1, Eq. (17); §3.2; §5.1, Figs. 10–11; §5.3.1, Table 4, Figs. 18–20; §5.4, Tables 5–9; §6.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv v1: §1; §2.3; §3.1.2, Fig. 8; §3.1.3, Fig. 11; §3.1.8, Figs. 19–20; §3.2, Table 6.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv v1: §2.3; §3–3.2; §4.1–4.2, Table 2, Figs. 7–9; §5.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §I, pp. 3–4; §III.A–C, Figs. 3, 13–15.
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1; §3.3.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: p. 6.
- [Gao et al. (2022)](/sources/gao-2022.md) — §1; §3.1–3.2; §5.3.1.
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III, Eqs. (1)–(6); §IV B, Figs. 6–10; §IV C 1, Fig. 12; §IV D, Fig. 22, Table II.
- [Liang & Fu (2024)](/sources/liang-2024.md) — §1; §4.10–4.12, Figs. 17–21.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §4.10; §5.
- [Husson et al. (2024)](/sources/husson-2024.md) — §1.
- [Volpiani (2024)](/sources/volpiani-2024.md) — Abstract; §1; §2.2.2; §5, Figs. 6–18; §6.
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §I; §V A, Fig. 3.
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.D; §III.A.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — Abstract; §I; §III; §IV; §V, Tables III, V–VII, Figs. 2–19; §V.B; §V.C; §VI.
- [Wang et al. (2013)](/sources/wang-2013.md) — §2; §4.13 (case C3.3).
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §4.
- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §1; §4; §6.
- [Kuya et al. (2018)](/sources/kuya-2018.md) — §5.
- [Deng et al. (2022)](/sources/deng-2022.md) — §1; §3.2, Remarks 1–2; §4.15, Figs. 23–25.
- [Ma et al. (2022)](/sources/ma-2022.md) — §1; §2.2; §3.1–3.3, Figs. 5–12; §4.
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §1; §3.4; §4; §5.1; §5.2, Table 3.
- [Simonis et al. (2022)](/sources/simonis-2022.md) — Eqs. (23)–(26); §3.3.2, Fig. 7; §3.4, Fig. 9.
- [Svärd (2022)](/sources/svard-2022.md) — Abstract; §2.2–2.3, Eq. (9); §3–3.1; §4, Eqs. (20)–(23), Prop. 4.1; §5.2–5.2.1, Tables 1–3; §5.3, Table 5.
- [Chen et al. (2022)](/sources/chen-2022-g.md) — §1; §5–6; §7.
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §I; §III, Eqs. 7–13 (explicit models in the kinetic solver); §IV A, Figs. 1–3; §IV C, Eqs. 19–22, Table II, Fig. 8 (numerical and modelled subgrid dissipation); §V; App. B, Figs. 9–12.
- [Cheng et al. (2023)](/sources/cheng-2023-b.md) — §1 (explicit models unsuited to shock–turbulence, citing Garnier et al.); §2.2; §3.6, Figs. 9–14 (deep cavity); §4.
- [Stanly et al. (2022)](/sources/stanly-2022.md) — §2.1, Eq. 1 (SBP differences plus artificial dissipation as implicit LES); §4.2; §6.
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I (eddy-viscosity wall-model corrections inapplicable to implicit LES); §II B–C, Eqs. 8–13, 20 (SVV implicit LES, Neumann wall-stress coupling); §III A–E, Table I, Figs. 3–9.
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §IV, Figs. 2–4 (hyperviscosity-stabilized implicit LES of isotropic turbulence); §V, Figs. 9–12 (mixing layer).
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §I (dense-gas implicit LES cited, in passing).
