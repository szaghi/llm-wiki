---
type: Source
title: "Korving et al. (2023) — Development of the neutral model in the nonlinear MHD code JOREK: Application to E × B drifts in ITER PFPO-1 plasmas"
description: "Derives a conservative plasma–atomic-neutral source model and implements it in JOREK as fluid and Monte Carlo kinetic neutrals, benchmarks both against SOLPS-ITER fuelling scans of ITER PFPO-1, and shows that poloidal E × B drifts drive early inner-target detachment and the dynamic formation of a high-field-side high-density region."
resource: "doi:10.1063/5.0135318"
source_kind: paper
authors: [Korving S.Q., Huijsmans G.T.A., Park J.-S., Loarte A., JOREK Team]
year: 2023
venue: "Phys. Plasmas 30:042509"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/0000_manual_no_journal_Unknown_10106350135318title.pdf"
tags: [neutrals, particles, edge, divertor, reduced-mhd, full-mhd, tokamak, verification]
timestamp: 2026-10-16T18:35:00Z
---

# Summary

The paper adds atomic-neutral physics to the nonlinear MHD code
[JOREK](/software/jorek.md) so that divertor and scrape-off-layer
conditions can be simulated together with the MHD. It first derives a
three-fluid (ion, electron, atomic-neutral) source model for
electron-impact ionization and effective radiative recombination with
OpenADAS rate coefficients, conservative in particles, momentum and energy
in both the Eulerian and the non-Eulerian "JOREK form", and reduces it to
JOREK's assumptions ($m_e\to0$, $n_e=n_i$, a single temperature
$T=T_e+T_i$). The reduced model is implemented twice: as a fluid neutral
model with a spatially constant diffusivity (after Fil et al. 2015), and
as a new kinetic neutral model in JOREK's particle framework, in which
Monte Carlo superparticles pushed with the Boris scheme undergo
ionization, charge exchange, line radiation and recombination, are
recycled and sputtered at the wall with TRIM/Eckstein data, and are
projected onto the Bézier–Fourier basis by a regularized $L^2$ projection
as explicit sources once per fluid step. Against SOLPS-ITER fuelling
scans of the ITER PFPO-1 H-mode (1.85 T, 5 MA, 20 MW), with JOREK reduced
to frozen fields and no drifts, kinetic neutrals reproduce the total
divertor heat load to within 10% for upstream separatrix densities
$1$–$2\times10^{19}$ m⁻³, detach at about 10% higher density, less
sharply, and give peak heat fluxes about twice as high; the authors
attribute the differences to the missing molecules and the
one-temperature model. The fluid neutral model gives only qualitative
agreement. With poloidal $\mathbf E\times\mathbf B$ drifts switched on
(standard reduced MHD with $\psi$ and $u$ evolved), the in–out asymmetry
grows, the inner target detaches earlier, and a phase-like transition
near $2.2$–$2.4\times10^{19}$ m⁻³ marks the dynamic formation of a
high-field-side high-density (HFSHD) region trapped in an HFS
$\mathbf E\times\mathbf B$ vortex near the X-point, which appears only
with drifts.

# Key claims

1. **Conservative three-fluid source model** (§III, Eqs. 13–17;
   Appendix A1–A6). The ionization/recombination source terms conserve
   particles, momentum and energy in both the Eulerian and the JOREK form.
   Derived.
2. **Reduced two-fluid sources and radiation correction** (§III,
   Eqs. 18–21). With $\rho=m_in_i$, $m_e\to0$, equal ion and neutral
   masses and $n_e=n_i$, the sources reduce to Eqs. 19–21; the
   recombination electron-energy loss is folded into
   $P_{\mathrm{rad}}$, which equals $n_en_i$ times the ADAS
   recombination-plus-bremsstrahlung power coefficient minus the
   recombination rate coefficient times the ionization potential. Derived.
   The $(\mathbf v_{\mathrm N}-\mathbf v_i)^2$ terms "purely arise due to
   the JOREK form" (Appendix). Stated.
3. **Kinetic recombination is conservative by construction** (§IV D 4,
   Eq. 31). Recombination neutrals are created per element per fluid step
   from the fluid-computed recombination loss, which "ensures mass and
   energy conservation". Stated/Derived.
4. **Projection matrix factorized once** (§IV A, Eqs. 22–23). The
   left-hand side of the moment projection depends only on the element
   geometry and "needs to be factorized only once"; the regularization
   (Laplacian and bi-Laplacian smoothing, separately tunable for $n=0$
   and $n>0$ and for parallel and perpendicular directions) reduces
   Monte Carlo noise. Stated.
5. **Pulsed wall injection is harmless** (§IV B). Reflection and
   sputtering superparticles injected once per fluid step "do not result
   in oscillating or pulsed solutions". Stated.
6. **Explicit coupling order** (§IV C). Particle moments enter
   explicitly but multiply implicit MHD terms "to maintain the highest
   order accuracy"; when kinetic particles dominate the order may drop;
   (semi-)implicit coupling is future work. Stated.
7. **Fluid neutrals are insufficient** (§V B, Fig. 3). With constant
   neutral diffusivity $\approx2\times10^2$ m² s⁻¹ (tuned to the SOLPS
   neutral decay) the power ranges and the sheath- to conduction-limited
   transition are reproduced, but the model is "not sufficient to provide
   the correct plasma mechanics"; JOREK upstream density at given
   fuelling is lower than SOLPS-ITER's. Shown.
8. **Kinetic neutrals vs SOLPS-ITER, power** (§V C, Fig. 4; §IX). Total
   divertor power agrees up to $n_{e,\mathrm{up}}\approx2\times10^{19}$
   m⁻³ ("difference <10%"); in–out balance slightly more symmetric;
   detachment at about 10% higher $n_{e,\mathrm{up}}$, less sharp, with a
   weaker density saturation from $n_{e,\mathrm{up}}\simeq2.4\times10^{19}$
   m⁻³. Shown.
9. **Peak heat flux about 2× SOLPS-ITER** (§V C, Fig. 5). In the
   conduction-limited regime JOREK peak target heat fluxes are
   "approximately twice as high", with a similar slope versus
   $n_{e,\mathrm{up}}$; inner and outer peaks converge at high density.
   Shown. Cause (one-temperature model, missing molecules and
   neutral–neutral collisions) Stated without test.
10. **Cost** (§V D). On 4 nodes × 36 cores, kinetic neutrals with $10^6$
    particles and $\Delta t_{\mathrm{kin}}=2\times10^{-8}$ s run as fast as
    the fluid model and "scale almost ideally" with node count; a steady
    state costs 9000–10000 core-hours (60–70 h wall clock). Stated; no
    scaling data shown.
11. **Conservation errors** (§V F, Fig. 6, Eq. 32). Recombination gives a
    mean relative momentum error $\sim10^{-4}$ and energy error
    $\sim10^{-3}$; the global steady-state power balance closes to
    $10^{-3}$–$10^{-2}$ depending on $\Delta t$ and particle count; BDF2
    "does not conserve energy exactly". Shown.
12. **Drifts move power outward and detach the inner target** (§VI A,
    Fig. 7). With $\mathbf E\times\mathbf B$ drifts more power reaches the
    outer target, and the inner target detaches (target $T_e<5$ eV) by
    $n_{e,\mathrm{up}}\approx2\times10^{19}$ m⁻³, far earlier than without
    drifts. Shown.
13. **Mechanism: private-flux-region flow** (§VI A, §VI C, Figs. 11, 18).
    The $\mathbf E\times\mathbf B$ flow from the outer to the inner target
    through the private flux region reduces the inner-target power. Shown
    (2D flows), interpreted.
14. **HFSHD region** (§VI D, §VIII D, Figs. 11, 18–20). Three
    $\mathbf E\times\mathbf B$ vortices form near the X-point (LFS, HFS,
    private region); when the HFS vortex dominates (ratio of
    $\mathbf E\times\mathbf B$ to remaining poloidal flow $\gtrsim1$) it
    traps density and forms the HFSHD region, which is "not a passive
    structure" and changes the flows of the whole SOL. Shown.
15. **Phase-like transition only with drifts** (§VIII A, Fig. 15). Over
    about 6 ms near $n_{e,\mathrm{up}}\approx2.4\times10^{19}$ m⁻³ the
    upstream density stagnates, drops and recovers at constant power,
    coinciding with HFSHD formation; it occurs "only with drifts". Shown.
16. **HFSHD without high power or impurities** (§VIII B). Unlike
    SOLPS-ITER drift runs at high power with impurities (Kaveeva 2020,
    Rozhansky 2021), here the HFSHD region is driven by drifts and
    main-plasma flow alone. Shown for this scenario.
17. **Full inner detachment implies HFSHD** (§VIII C). In the 20 MW
    scenario full inner-target detachment always comes with HFSHD
    formation. Shown (one scenario).
18. **Dynamic vs steady-state trajectories** (§VII A, Fig. 12). In a gas
    puff ramp the divertor power falls about twice as fast with
    $n_{e,\mathrm{up}}$ as along the sequence of steady states; 50% of the
    density change occurs within 5 ms of the puff; at least 40 ms must be
    simulated to reach steady state. Shown.
19. **Diamagnetic drift unimportant for HFSHD** (§VIII D 1, §IX), because
    the region has low pressure. Stated.
20. **ITER $Q=10$** (§VIII D 3). At 100 MW neutrals alone will not detach
    the plasma; Ne seeding is needed. Stated.

# Models and numerics

* **Full MHD** (§II A, normalized units with $\mu_0$ and $k_B$ absent; SI
  form here):
  $$\begin{aligned}
  \partial_t\mathbf A&=-\mathbf E-\nabla\Phi,\qquad \mathbf B=F\nabla\phi+\nabla\times\mathbf A,\qquad \mu_0\mathbf J=\nabla\times\mathbf B,\\
  \rho\,\partial_t\mathbf v&=-\rho\mathbf v\cdot\nabla\mathbf v-\nabla p+\mathbf J\times\mathbf B-\nabla\cdot\mathsf\Pi+\mathbf S_{\mathbf v},\\
  \partial_t\rho&=-\nabla\cdot(\rho\mathbf v)+\nabla\cdot(D_\perp\nabla_\perp\rho+D_\parallel\nabla_\parallel\rho)+S_\rho,\\
  \partial_tp&=-\mathbf v\cdot\nabla p-\Gamma p\nabla\cdot\mathbf v+\nabla\cdot(\kappa_\perp\nabla_\perp T+\kappa_\parallel\nabla_\parallel T)+(\Gamma-1)\big[\text{viscous heating}+(\mathbf E+\mathbf v\times\mathbf B)\cdot\mathbf J\big]+S_p,\\
  \mathbf E&=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_x)+(\text{diamagnetic term, off in this paper}).
  \end{aligned}$$
  with $\mathsf\Pi$ the viscous stress tensor (printed $-\underline{\boldsymbol\tau}$).
* **Reduced MHD** (§II B, the ansatz of [Hoelzl et al. (2021)](/sources/hoelzl-2021.md)):
  $\mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi$,
  $\mathbf v=-R\nabla u\times\mathbf e_\phi+v_\parallel\mathbf b$, with
  $u=\Phi/F_0$ (the $\mathbf E\times\mathbf B$ velocity is the first term;
  the ion diamagnetic term of Eq. 7 is not used). Variables $\psi$, $u$,
  $j$, $\varpi$, $\rho$, $T=T_e+T_i$, $v_\parallel$, plus the neutral mass
  density for fluid neutrals. Momentum is projected on $\mathbf B$ and on
  the $\mathbf E\times\mathbf B$ test direction (Eq. 9). Visco-resistive,
  one temperature, $p=n(T_e+T_i)$.
* **Driftless benchmark reduction.** The evolution of $\psi$, $j$, $u$,
  $\varpi$ is removed: frozen field, no $\mathbf E\times\mathbf B$ flow.
* **Plasma–neutral sources** (§III). Ionization rate
  $n_{\mathrm N}n_e\langle\sigma v\rangle_{\mathrm{ion}}$ and
  recombination rate $n_en_i\langle\sigma v\rangle_{\mathrm{rec}}$, both
  OpenADAS effective coefficients of $(n_e,T_e)$. Ionization transfers
  the neutral's mass, momentum, thermal and kinetic energy to the ions and
  removes the ionization potential from the electrons; recombination
  transfers ion (and electron) mass, momentum and energy to the neutrals,
  the remainder going to photons. The plasma is optically thin. Charge
  exchange appears only in the kinetic model; there are no molecules and
  no neutral–neutral collisions.
* **Kinetic neutral model** (§IV). Superparticles (weights
  $5\times10^{13}$–$5\times10^{14}$ atoms, $10^6$–$10^7$ particles) pushed
  by the full-orbit Boris scheme of the kinetic-ion framework (van Vugt
  2019; see [particle pushers](/methods/particle-pushers.md)), tracked in
  $(R,Z,\phi)$ and in local element coordinates.
  * Ionization: probability per kinetic step
    $1-\exp(-n_e\langle\sigma v\rangle_{\mathrm{ion}}\Delta t_{\mathrm{kin}})$
    applied as a weight reduction (see Recorded as printed for the
    printed form).
  * Charge exchange: same probability form; the new neutral velocity is
    drawn from a Maxwellian of temperature $T_e$ shifted by the plasma
    flow; momentum and kinetic-energy differences go to the plasma.
  * Line radiation from the ADAS line-power coefficient.
  * Recombination: per element per fluid step, at least one new
    superparticle carrying the recombined mass and momentum, placed
    uniformly in the element and the toroidal sector.
  * Wall: reflection vs thermal desorption from the TRIM database (via
    EIRENE), sputtering from Eckstein yields, injected once per fluid
    step.
  * Moment projection: weak $L^2$ projection of the particle mass,
    momentum and energy sources onto the Bézier × Fourier basis, with the
    contributions accumulated every kinetic step for conservation and the
    mass matrix (optionally regularized by Laplacian and bi-Laplacian
    terms) factorized once; sources enter the fluid as
    $\partial_t\rho=S_\rho$, $\rho\partial_t\mathbf v=\mathbf S_{\mathbf v}-\mathbf vS_\rho$
    and an energy source corrected for the kinetic energy (Eq. 25).
* **Fluid neutral model.** Fil et al. (2015): one extra density
  equation, diffusive transport with constant diffusivity
  ($\approx2\times10^2$ m² s⁻¹ here).
* **Discretization.** Bicubic Bézier elements ($G^1$; see
  [Bézier finite elements](/methods/bezier-finite-elements.md)) in the
  poloidal plane, toroidal Fourier series, iso-parametric flux-aligned
  grid from a Grad–Shafranov solve extended to the first wall (dome and
  sub-dome not gridded). Near the strike points 0.74 mm along and 8.1 mm
  across the field (Fig. 2); about 1 mm along the field is required.
* **Time integration.** Fully implicit; Gear/BDF2 used (Crank–Nicolson
  available). Fluid $\Delta t=2.246\times10^{-6}$ s (§V F), kinetic
  $\Delta t_{\mathrm{kin}}=2\times10^{-8}$ s (§V D); quasi-steady states
  after 11–55 ms simulated, at least 40 ms in the dynamic study, some runs
  to 150 ms.
* **Boundary conditions** (§V E). Dirichlet $\psi$ from the equilibrium;
  $u=\varpi=0$ (grounded wall); Neumann for $\rho$; magnetized Bohm sheath
  conditions, $v_\parallel=c_s$ and a sheath heat-transmission factor $\delta_{\mathrm{sh}}$ on
  the parallel heat flux.
* **Transport.** $D_\perp=0.3$ m² s⁻¹, perpendicular ion and electron
  heat diffusivities 1.0 m² s⁻¹, Braginskii parallel conduction.
* **Hardware.** 4 nodes × 36 cores (Marconi-Fusion, ITER SDCC); no GPU.

# Tests and results

* **Scenario.** ITER PFPO-1 H-mode, $B_T=1.85$ T, $I_p=5$ MA, 20 MW
  heating, no impurities, divertor gas puff, pumping at the private-region
  boundary. The SOLPS-ITER reference (Park et al. 2021) has molecules, two
  temperatures, a separate EIRENE grid and the dome; JOREK includes the
  core but not the sub-dome.
* **Fluid neutrals vs SOLPS-ITER** (Fig. 3): same power ranges; lower
  upstream density at given fuelling (attributed to the ad hoc initial
  density profile); discrepancies below $1.5\times10^{19}$ m⁻³;
  "reasonable agreement" given the model's simplicity.
* **Kinetic neutrals vs SOLPS-ITER** (Figs. 4–5): total power within 10%
  to $\approx2\times10^{19}$ m⁻³; detachment about 10% later in density;
  peak heat flux about 2× higher in the conduction-limited regime; at low
  density the inner-target peak is higher in JOREK, unexplained.
* **Power balance** (Fig. 6, Eq. 32): relative error $10^{-3}$–$10^{-2}$
  in a high-recycling attached case.
* **Drifts vs no drifts** (Figs. 7–10): inner-target rollover at about
  $1.8\times10^{19}$ and outer at about $2.15\times10^{19}$ m⁻³ with
  drifts, roughly symmetric without; double-peaked ion-flux profiles
  without drifts, flattened with; outer-target peak flux counter-intuitively
  rises up to $1.5\times10^{19}$ m⁻³; two distinct solutions at nearly
  equal density (2.28 and $2.3\times10^{19}$ m⁻³) at HFSHD formation.
* **Dynamics** (Fig. 12): 8.3 MW power drop in the first 5 ms after the
  puff while $n_{e,\mathrm{up}}$ goes from 1 to $1.5\times10^{19}$ m⁻³; a
  further 1.3 MW over 36.6 ms; saturation after 30–40 ms.
* **HFSHD formation** (Fig. 19): slow density build-up at the wall, a
  front moving toward the X-point building up to about $10^{21}$ m⁻³ (printed
  "$10\times10^{20}$"), then a jump to a stable position that shifts with
  fuelling; formation time 10–20 ms (§IX).
* **Detached-case ionization** (Fig. 21): inner strike point
  $T_e\approx1$ eV, outer $\approx10$ eV (outer not detached); ionization
  concentrated at the edge of the HFSHD region.

# Notation map

| Korving et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf A$, $\Phi$, $\mathbf B$, $\mathbf J=\nabla\times\mathbf B$ | $\mathbf A$, $\Phi$, $\mathbf B$, $\mu_0\mathbf J=\nabla\times\mathbf B$ | JOREK normalized units, $\mu_0=1$, $k_B$ absent |
| $F$, $F_0$ | $F$, $F_0$ | |
| $\psi$ ($\mathbf B=\frac{F_0}{R}\mathbf e_\phi+\frac1R\nabla\psi\times\mathbf e_\phi$) | $\psi$ | per radian, no $2\pi$ |
| $u=\Phi/F_0$ | $u$ | |
| $j$, $w$ | $j$, $\varpi$ | **collision risk:** native $w$ (vorticity) vs registry $w_p$ (marker weight) |
| $v_\parallel$ ($\mathbf v_\parallel=v_\parallel\mathbf B$) | $\hat v_\parallel=v_\parallel/B$ | **collision:** native $v_\parallel$ is per unit $B$; registry $v_\parallel=\mathbf v\cdot\mathbf b$ |
| $\rho$, $p$, $T$ | $\rho$, $p$, $T=T_e+T_i$ | one-temperature model |
| $\gamma$ | $\Gamma$ | **collision:** registry $\gamma$ is a growth rate |
| $\underline{\boldsymbol\tau}$, $\underline{\mathbf D}$, $\underline{\boldsymbol\kappa}$ | $-\mathsf\Pi$ (viscous stress); $D_\perp,D_\parallel$; $\kappa_\perp,\kappa_\parallel$ | sign: native $+\nabla\cdot\underline{\boldsymbol\tau}$ |
| $\mathbf J_*$ | $\mathbf J_x$ | source current in Ohm's law |
| $\delta^*$ | words (diamagnetic coefficient) | unused here |
| $\tilde S_\rho$, $\tilde{\mathbf S}_v$, $\tilde S_p$; $S_\rho$, $\mathbf S_v$, $S_E$ | $S_\rho$, $\mathbf S_{\mathbf v}$, $S_p$; words for the energy source | JOREK-form vs conservative-form sources |
| $n_n$, $m_n$, $\mathbf v_n$, $\rho_n$ | $n_{\mathrm N}$, $m_i$, $\mathbf v_{\mathrm N}$, $\rho_{\mathrm N}=m_in_{\mathrm N}$ | ion and electron velocities $\mathbf v_i$, $\mathbf v_e$ written by species subscript |
| $\Gamma^{ion}_\alpha$, $\Gamma^{rec}_\alpha$ | $\mathcal R_{\mathrm{ion}}=n_{\mathrm N}n_e\langle\sigma v\rangle_{\mathrm{ion}}$, $\mathcal R_{\mathrm{rec}}=n_en_i\langle\sigma v\rangle_{\mathrm{rec}}$ | **collision:** registry $\Gamma$ is the ratio of specific heats |
| $S_{ion}$, $S_{rec}$, $S_{CX}$, $S_{PLT}$ | $\langle\sigma v\rangle_{\mathrm{ion}}$, $\langle\sigma v\rangle_{\mathrm{rec}}$, $\langle\sigma v\rangle_{\mathrm{cx}}$, words | **collision:** registry $S$ is the Lundquist number and $S_\rho$ etc. are sources |
| $L_{PRB}$, $P_{PRB}$, $P_{rad}$ | $L_{\mathrm{rad}}$ (recombination + bremsstrahlung part); words; $P_{\mathrm{rad}}$ | ADAS recombination + bremsstrahlung power |
| $\phi_{ion}$ | $\varepsilon_{\mathrm{ion}}$ (ionization potential) | **collision:** registry $\phi$ is the toroidal angle |
| $E_\alpha$ | words (species total energy density) | **collision** with $\mathbf E$ |
| $w_n$ | $w_p$ | superparticle weight (atoms) |
| $\mathcal P_{ion}$, $\mathcal P_{CX}$ | words (reaction probabilities per kinetic step) | |
| $\lambda$, $\zeta$ | words (regularization coefficients) | **collision:** registry $\zeta$ is a flux-coordinate toroidal angle, $\lambda_{\mathrm o}$ an ordering parameter |
| $(s,t,\phi)$ | words (local element coordinates) | **collision:** registry $s$ is a radial flux label |
| $H_{ij}$, $H_{\phi,k}$, $v^*$ | words (Bézier and Fourier basis, test function) | |
| $\Delta t_{fluid}$, $\Delta t_{kinetic}$ | $\Delta t$, $\Delta t_{\mathrm{kin}}$ | |
| $n_{upstream}$ | $n_{e,\mathrm{up}}$ | outer-midplane separatrix electron density |
| $q_{pk,\perp}$ | words (peak target heat flux) | **collision** with safety factor $q$ |
| $\gamma_{sheath}$ | $\delta_{\mathrm{sh}}$ (sheath heat-transmission factor) | **collision** with growth rate $\gamma$ |
| $E\times B_{factor}$ | words | ratio of $\mathbf E\times\mathbf B$ to remaining poloidal flow |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunks 2 and 3 (2026-10-16) extended many. This source is cited on:

* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [Fluid neutral models and plasma–neutral atomic sources](/methods/fluid-neutral-models.md)
* [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)
* [High-field-side high-density region](/results/high-field-side-high-density-region.md)
* [Hybrid kinetic-MHD models](/methods/hybrid-kinetic-mhd.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [JOREK](/software/jorek.md)
* [Kinetic (Monte Carlo) neutral model coupled to MHD](/methods/kinetic-neutral-model.md)
* [Operator splitting and Newton–Krylov treatment of atomic-physics sources](/methods/operator-splitting-of-atomic-sources.md)
* [Particle pushers: Boris, slow-manifold Boris, guiding-centre and gyrokinetic](/methods/particle-pushers.md)
* [Particle-to-finite-element moment projection](/methods/particle-to-mesh-projection.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Sheath (Bohm) boundary conditions](/methods/sheath-boundary-conditions.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/0000_manual_no_journal_Unknown_10106350135318title.pdf`.
   * **Version.** Publisher version of record (AIP, CC BY 4.0) with an
     AIP cover page; 25 PDF pages = cover + article pp. 042509-1 to
     042509-24. Submitted 18 Nov 2022, accepted 10 Mar 2023, online 5 Apr
     2023; Special Collection "2023 Early Career Collection". The filename
     carries no metadata.
   * **Identity.** doi:10.1063/5.0135318, checked on Crossref: Phys.
     Plasmas 30(4), article 042509, issued 2023-04; authors Korving,
     Huijsmans, Park, Loarte and the group author JOREK Team (footnote b
     points to Hoelzl et al., Nucl. Fusion 61:065001); reference count 56.
   * **How read.** Full text, including the Appendix. Equations
     transcribed from the extracted text; the reader notes do not list
     which equations were re-checked on rendered pages. Plot values are
     approximate readings.
   * **Recorded as printed.**
     * Time step: §V F gives a fluid step of $2.246\times10^{-6}$ s, and
       Figs. 12, 15 and 17 give 100 steps = 0.2246 ms (consistent); the
       Fig. 13 and Fig. 14 captions give "4000 fluid time steps
       (0.8984 ms)", i.e. $2.246\times10^{-7}$ s per step. Both cannot
       hold.
     * Fig. 13 and Fig. 14 captions label the bottom row "with drifts";
       per the text it is the no-drift case.
     * §VII C refers to "the lower row in Fig. 13" for heat flux in the
       ion-flux discussion of Fig. 14.
     * Eq. 21, electron energy: printed
       $-(\Gamma-1)\big(\text{ionization loss}-P_{\mathrm{rad}}\big)$ in
       translation, which makes the radiation term a heating, against
       Eq. 18 and the text; the inner sign should be $+$ (compiler's
       check of the printed sign).
     * Eqs. 26–27: the surviving weight after ionization is printed as
       $w_p$ times the ionization probability, while the ionized weight is
       $w_p$ times one minus that probability; relative to the definition
       of the probability the two are swapped. The rule is also
       conditioned on a uniform random number below the probability while
       still reducing the weight, which mixes analog and weight-reduction
       Monte Carlo.
     * Eq. 29: the charge-exchange momentum and energy sources lack the
       particle mass; the CX neutral is sampled with $T_e$, not $T_i$.
     * Eq. 14: the electron momentum left-hand side is printed with the
       ion velocity.
     * Eq. 7: "$\mathbf A\cdot\mathbf e_\phi=\psi\nabla\phi$" equates a
       scalar and a vector ($\mathbf A=\psi\nabla\phi$ meant).
     * Eq. 8: the induction weak form is printed as a projection of
       $\partial_t\mathbf A$ on $\mathbf B$; a projection on $\nabla\phi$
       is presumably meant.
     * Eq. 23: the right-hand-side integral sign is missing.
     * Appendix after A5: "$v_u^2$" for $v_i^2$.
     * Field: "1.8T/5MA" in the abstract, $B_T=1.85$ T in §V.
     * Transition density quoted as $2$–$2.2\times10^{19}$ (§VI A),
       2.28–$2.3\times10^{19}$ (§VI B), $2.4\times10^{19}$ (§VIII A, C,
       Fig. 15) and $2.2\times10^{19}$ m⁻³ (§IX); different runs
       (steady-state vs puff ramps), but the conclusion quotes one number.
     * Wall data: "TRIM-code database" (§IV B, citing the EIRENE website)
       vs "SDTRIM coefficients" (conclusion).
     * "Scales almost ideally" (§V D) without scaling data.
     * Fig. 16 caption: central electron density $1.2\times10^{19}$ m⁻³,
       implausibly low next to edge values of about $2\times10^{19}$ m⁻³;
       not verifiable.
     * Abstract: "neoclassical flows" are said to be included; in this
       paper diamagnetic and neoclassical flows are off.
     * Typos: "Crank–Nicholson", "Eularian", "difissivity", "Gears".
   * **Reference list.** 56 printed entries (= Crossref count), merged
     into the bibliography under `korving-2023`; no DOIs are printed. The
     JOREK Team footnote repeats ref. 1 (`hoelzl-2021`, the ingested
     [Hoelzl et al. (2021)](/sources/hoelzl-2021.md); its title printed
     "fusion plasma") and is not a separate entry. Refs. 14 and 15 are two
     van Vugt 2019 works (`vanvugt-2019`, `vanvugt-2019-b`); the EIRENE
     website (ref. 45, no author) is `eirene-2019`; the ADAS manual
     (ref. 40) is a web resource. Ref. 3 (Du et al., Fusion Eng. Des.) is
     printed vol. 61 with year 2014; ref. 27 (Meier et al., PPCF 58:125012)
     is printed with the title of ref. 28 (Sytova et al. 2019), a copy
     error; ref. 47 has "Braginksii" and "Martınex-Gomez".
