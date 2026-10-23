---
type: Source
title: "Howell et al. (2022) — Growing neoclassical tearing modes seeded via transient-induced-multimode interactions"
description: "NIMROD simulations with heuristic neoclassical stress closures in which a transient boundary magnetic perturbation seeds a 2/1 neoclassical tearing mode in a DIII-D ITER-baseline equilibrium; a toroidal Fourier power-transfer analysis shows that three-wave coupling among core modes drives the slow-growth phase before MRE-like robust growth at 3.4 Wb/s."
resource: "doi:10.1063/5.0076253"
source_kind: paper
authors: [Howell E.C., King J.R., Kruger S.E., Callen J.D., La Haye R.J., Wilcox R.S.]
year: 2022
venue: "Phys. Plasmas 29:022507"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Physics_of_Plasmas_Howell_Growing_neoclassical_tearing_modes_seeded_via_transient-indu.pdf"
tags: [mhd, tearing, bootstrap-current, tokamak]
timestamp: 2026-10-16T18:35:00Z
---

# Summary

The paper reports nonlinear [NIMROD](/software/nimrod.md) simulations in
which a 2/1 neoclassical tearing mode (NTM) is seeded in a classically
stable, kinetically reconstructed DIII-D ITER Baseline Scenario (IBS)
equilibrium (shot 174446 at 3390 ms, $\beta_N\sim1.8$, $q_{95}\sim3.4$) with
reconstructed toroidal and poloidal flows. Two model developments make this
possible. Heuristic neoclassical stress closures (Gianakon et al. 2002) add
a poloidal-flow-damping ion force to the momentum equation and an electron
force to Ohm's law; the electron force produces the
[bootstrap-current](/definitions/bootstrap-current.md) drive without an
imposed source current. A transient $n=1$, broad-$m$ magnetic perturbation
(MP), imposed as a normal field at the computational boundary with a
compact-support bump envelope, generates the seed island. After a 1 ms
pulse the 2/1 helical flux decays, grows slowly (about 1.5–8 ms) and then
grows "robustly", linearly in time at about 3.4 Wb/s, against 3.3 Wb/s from
a modified Rutherford equation (MRE) analysis. The pulse also excites a
time-ordered sequence of core modes (6/5, 5/4, 4/3, 3/2) whose islands
overlap into a stochastic core that flattens the pressure. A generalization
of the cylindrical Ho–Craddock toroidal-Fourier energy-transfer analysis to
shaped toroidal equilibria shows that during the slow phase a sequence of
three-wave couplings among the core modes (first $n=5,6$, later $n=2,3$)
puts power into $n=1$ and sustains the 2/1 growth until the island reaches
a critical width; quasi-linear flattening is not the main driver. In the
experiment the same two-phase growth follows successive ELMs, but the core
modes evolve over about 100 ms, not a few ms. The authors propose MP-scan
simulations as a test of an equilibrium's resilience to NTMs.

# Key claims

1. **Two enabling developments** (Abstract, §II). NIMROD's NTM capability
   rests on heuristic neoclassical ion and electron stress closures and on
   transient MPs applied at the boundary. Stated (implementation, not
   separately verified).
2. **Closure content** (§II A, Eqs. 8–10). The closures "model the
   neoclassical bootstrap current, neoclassical ion poloidal flow damping,
   and the neoclassical ion polarization current enhancement" from fluid
   variables only; subtracting the equilibrium flow and current keeps the
   equilibrium "against decay". Stated.
3. **Closure validity** (§II A). The ion closure assumes the ion velocity
   equals $\mathbf v$ (valid to $O(m_e/m_i)$); the electron closure assumes
   the electron poloidal velocity is $-\mathbf J\cdot\mathbf e_\theta/(n_ee)$
   and holds for strong ion poloidal-flow damping; both assume
   $Z_{\mathrm{eff}}=1$. Derived/Stated.
4. **Pulse envelope** (§II B, Eq. 12). A bump function with compact support
   and continuous derivatives of all orders, peaking at $t=t_w+t_o$, is
   "numerically advantageous". Derived.
5. **Phase modulation** (§II B, Eq. 11). Linear theory (Fitzpatrick &
   Hender 1991) predicts weakest flow screening when the applied field is
   nearly in phase with the rotating resonant mode, motivating a modulation
   $e^{i\omega_{\mathrm{mp}}t}$. Attributed.
6. **Coil spectrum** (§II B, Fig. 1). A four-coil cross that would give pure
   $m=2$ in a cylinder gives a broad poloidal spectrum in shaped geometry;
   coil positions and pitches are tuned with vacuum-response calculations to
   raise the 2/1 helical flux relative to 3/1 and 4/1, and only the $n=1$
   component is applied. Stated.
7. **Experiment** (§III A, Fig. 2). ELMs at 3335 and 3363 ms are followed by
   a small, slowly growing $n=1$ signal; the ELM at 3396 ms triggers a
   robustly growing 2/1 NTM. Shown (experimental data).
8. **Modified core profile** (§III A, Fig. 3). $q_0$ is raised above 1 to
   stabilize the 1/1 internal kink and avoid sawteeth; this lowers the
   near-axis shear and changes core-mode stability while $q$ near $q=2$ is
   preserved. Stated.
9. **Pedestal flow shear** (§III A, Fig. 4 caption) stabilizes
   peeling–ballooning modes, i.e. suppresses ELMs in the simulation. Stated.
10. **Parameters** (§III A, Table I). Simulated parameters at the 2/1
    surface are "within a factor of 2 or 6" of experiment; the ratio of
    electron damping rate to (collision rate + damping rate) is 0.55
    against 0.43 in experiment. Shown (but see Recorded as printed).
11. **Phases of 2/1 growth** (§III B, Fig. 5A). Rise and decay with the
    pulse, decay until about 1.5 ms, slow growth to about 8 ms, then robust
    growth. Shown.
12. **NTM signature** (§III B). Linear-in-time helical-flux growth "is
    indicative of an NTM"; classical (Rutherford) tearing grows
    quadratically in time. Attributed (refs. [3], [7]).
13. **MRE agreement** (§III B, Fig. 5A). Robust growth about 3.4 Wb/s
    against 3.3 Wb/s from an MRE analysis with the simulated parameters
    (ref. [30], in preparation), indicating "standard NTM growth". Shown;
    the MRE number is computed elsewhere.
14. **Edge responses** (§III B, Figs. 5B, 6A). 3/1 and 4/1 respond strongly
    because their surfaces lie near the boundary where screening is weak;
    the 3/1 decays over several ms. Shown.
15. **Core-mode sequence** (§III B, Fig. 5B). From about 4 ms: 6/5, then
    5/4 and 4/3, then 3/2; when 3/2 is large the 2/1 enters robust growth;
    each earlier mode peaks and decays as the next grows. Shown.
16. **Stochastic core** (§III B, Fig. 7). Overlapping islands form a
    stochastic region that spreads outward toward the 2/1 island; 2/1
    island width 2–3 cm at 3 ms and 5 cm at 15 ms; surfaces outside $q=2$
    stay closed. Shown.
17. **Quasi-linear drive** (§III B, Fig. 8). Core flattening by the
    stochastic field and anisotropic conduction steepens the gradient at the
    edge of the stochastic region and raises the drive. Shown.
18. **Power-transfer analysis** (§IV, App. A). Generalizes Ho & Craddock
    (1991) to axisymmetric shaped toroidal equilibria; it gives "no insight
    into the poloidal mode spectrum". Derived.
19. **Large linear power ≠ instability** (§IV, Fig. 10B–C). For $n=2,3$ the
    total power is a small imbalance of large terms; the linear power is
    large and positive although linear NIMROD runs are stable. Shown.
20. **Negative dissipative power enables tearing** (§IV, App. A). Resistive
    and neoclassical-electron powers are negative; they enable growth by
    changing the mode structure so that it draws more energy from the
    equilibrium. Stated (interpretation).
21. **Saturation of $n=2,3$** (§IV, Fig. 10). Quasi-linear flattening mostly
    causes $n=2$ saturation and decay from about 8 ms; for $n=3$, nonlinear
    plus dissipative powers make up 45% of the outgoing power late in the
    run. Shown.
22. **3/1 → 2/1 transfer** (§IV). From 3 to 5 ms the net $n=1$ power is
    about zero while 3/1 decays and 2/1 grows; the transfer is "inferred"
    and the diagnostic "cannot directly quantify" it. Stated (inference).
23. **Nonlinear drive of $n=1$** (§IV, Fig. 10A). From 5 to 10 ms nonlinear
    and linear powers contribute "roughly equally", the onset coinciding with
    the growth of higher-$n$ core modes. Shown.
24. **Robust phase** (§IV, Fig. 11). At 15.5 ms linear and Poynting-flux
    powers largely cancel; their sum is localized at $q=2$ ($s=0.69$); the
    Poynting flux carries about 80% of the injected energy inward. Shown.
25. **Three-wave 5 + 6 → 1** (§IV, Fig. 12). At 5 ms the $n=1$ nonlinear
    power peaks at $s=0.31$ near $q=6/5$; peak nonlinear powers $-0.086$
    ($n=5$), $-0.046$ ($n=6$) and $+0.063$ MW m⁻³ ($n=1$), the residual
    going to $n=2,4$. Shown.
26. **Later couplings** (§IV, Fig. 13). At 8.39 ms the $n=1$ nonlinear
    power is broad ($s\approx0.3$–0.65), peaking inside $q=4/3$ and at
    $q=5/3$ (from $n=3$) and near $q=3/2$ (from $n=2$). Shown.
27. **Main conclusion** (§IV, §V). Seeding is "a sequence of 3-wave coupling
    interactions that evolve in time", not a single one. Shown
    (interpretation of Claims 25–26).
28. **Sensitivity** (§V, runs not shown). Larger electron damping: the pulse
    alone triggers robust 2/1 growth, followed by an inverse sequence 3/2,
    4/3, 5/4; smaller damping: return to quiescence; half amplitude or
    shorter pulse: similar sequence. Stated.
29. **Comparison with experiment** (§V). Both show core modes (4/3, 3/2)
    before the 2/1 and two-phase 2/1 growth; experimental core modes evolve
    over about 100 ms and exist before the triggering ELM, simulated ones over
    a few ms; attributed partly to enhanced resistivity and modified core
    profiles. Stated.
30. **Against $\Delta'$-based resilience** (§V). The MRE analysis of ref.
    [30] finds the classical $\Delta'$ term negligible in this plasma;
    seeding needs a finite MP; MP-scan simulations for a seeding threshold
    are proposed as a resilience metric. Stated.
31. **ELM surrogate** (§I). ELMs come from moderate-$n$ peeling–ballooning
    modes whose $n$ and $n+1$ ($\sim6$–8) interact to give $n=1$ (ref. [23]);
    the MP stands in for ELM seeding. Attributed.

# Models and numerics

* **Code.** NIMROD (Sovinec et al. 2004). Discretization, time advance,
  linear solvers, resolution and cost are not described; harmonics up to at
  least $n=6$ appear (Figs. 5, 9, 12). Runs at NERSC. SI units, $\mu_0$
  explicit.
* **Governing equations** (§II A, Eqs. 1–7, single fluid, $n_e=n_i$,
  $Z_{\mathrm{eff}}=1$, diamagnetic flow neglected), with
  $D/Dt=\partial_t+\mathbf v\cdot\nabla$:
  $$\begin{aligned}
  \frac{Dn_e}{Dt}&=-n_e\nabla\cdot\mathbf v+D\nabla^2n_e,\\
  \rho\frac{D\mathbf v}{Dt}&=\mathbf J\times\mathbf B-\nabla p-\nabla\cdot\mathsf\Pi_i,\\
  \tfrac32n_e\frac{DT_s}{Dt}&=-p_s\nabla\cdot\mathbf v-\nabla\cdot\mathbf q_s,\\
  \partial_t\mathbf B&=-\nabla\times\mathbf E+D_B\nabla\nabla\cdot\mathbf B,\\
  \mathbf E&=-\mathbf v\times\mathbf B+\eta\mathbf J-\frac{1}{n_ee}\nabla\cdot\mathsf\Pi_e,\qquad \mu_0\mathbf J=\nabla\times\mathbf B.
  \end{aligned}$$
  $D$ is an artificial isotropic particle diffusivity; $D_B$ a
  divergence-cleaning diffusivity (see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md));
  $\mathsf\Pi_i$ holds classical (form not given) and neoclassical ion
  stress, $\mathsf\Pi_e$ only neoclassical electron stress; $\mathbf q_s$ is
  the species heat flux, anisotropic with
  $(\kappa_\parallel/\kappa_\perp)^{1/4}=100$. Resistivity Spitzer-like,
  $\eta=\eta_0T_e^{-3/2}$; damping rates uniform; $\eta$ and the damping
  rates are "artificially enhanced for numerical convenience".
  ($\mathsf\Pi_s$ is the registry stress tensor; $\mathbf q_s$, $D_B$ are
  page-local; see Notation map.)
* **Heuristic neoclassical closures** (§II A, Eqs. 8–10, after Gianakon et
  al. 2002), with subscript 0 for the equilibrium, $\mathbf e_\theta$ a
  poloidal basis vector parallel to the equilibrium poloidal field and
  $\tau_{\mathrm{nc},s}^{-1}$ the poloidal-flow damping rate of species $s$:
  $$\nabla\cdot\mathsf\Pi_i=\tau_{\mathrm{nc},i}^{-1}n_em_i\langle B_0^2\rangle\frac{(\mathbf v-\mathbf v_0)\cdot\mathbf e_\theta}{(\mathbf B_0\cdot\mathbf e_\theta)^2}\mathbf e_\theta,\qquad
  \nabla\cdot\mathsf\Pi_e=-\tau_{\mathrm{nc},e}^{-1}\frac{m_e}{e}\langle B_0^2\rangle\frac{(\mathbf J-\mathbf J_0)\cdot\mathbf e_\theta}{(\mathbf B_0\cdot\mathbf e_\theta)^2}\mathbf e_\theta,$$
  special cases of the species form
  $\tau_{\mathrm{nc},s}^{-1}n_sm_s\langle B_0^2\rangle(\mathbf v_s\cdot\mathbf e_\theta)\mathbf e_\theta/(\mathbf B_0\cdot\mathbf e_\theta)^2$.
  $\langle B_0^2\rangle$ is computed once from the initial equilibrium; the
  normalization of $\mathbf e_\theta$ cancels. The electron force in Ohm's
  law produces the bootstrap drive; no $\mathbf J_x$ is imposed. This is a
  third implementation class beside the imposed $\mathbf J_x$ of M3D-C1 and
  JOREK described in [Saxena et al. (2025)](/sources/saxena-2025.md) and
  [Hoelzl et al. (2024)](/sources/hoelzl-2024.md).
* **Seed by transient boundary MP** (§II B, Eqs. 11–12):
  $$\mathbf n\cdot\mathbf B(\mathbf x,t)=\mathbf n\cdot\mathbf B_{\mathrm{mp}}(\mathbf x)\,\mathrm{env}(t)\,e^{i\omega_{\mathrm{mp}}t},\qquad
  \mathrm{env}(t)=\begin{cases}E_0\exp\!\big(-1/(1-\tau^2)\big)&|\tau|\le1\\0&\text{otherwise}\end{cases},\quad \tau=\frac{t-t_o-t_w}{t_w},$$
  with $\mathbf B_{\mathrm{mp}}$ the vacuum field of six toroidal sets of
  four poloidally arranged circular coils with alternating currents,
  Fourier-filtered to $n=1$. Pulse 1 ms; $E_0$, $\omega_{\mathrm{mp}}$, $t_o$
  not given. Motivated by transient forced reconnection (Hahm & Kulsrud
  1985; Beidler et al. 2018).
* **Equilibrium** (§III A). Kinetic EFIT (OMFIT) from data just before the
  3396 ms ELM, constrained by fast-ion pressure and computed bootstrap
  current, with 1 ms CER flows; fast ions and impurities are not in the MHD
  model. Flow $\mathbf v_0=K(s)\mathbf B_0+\omega_E(s)R^2\nabla\phi$ (Eq. 13).
  $T_i$ is derived from $p=n_e(T_e+T_i)$ and differs from the reconstructed
  $T_i$; called minor because $T_i$ enters no transport coefficient.
* **Boundary.** The reconstructed separatrix; the MP is the normal field
  imposed there. Wall type and other BCs not stated.
* **Diagnostics.** Helical flux (Eqs. 14–15)
  $\Psi_{m/n}=\oint\!\oint\mathcal J\,\delta\mathbf B\cdot\nabla s\;e^{i(n\phi-m\theta)}\,d\theta\,d\phi$,
  $\mathcal J^{-1}=\nabla s\cdot(\nabla\theta\times\nabla\phi)$, independent
  of the radial label; SURFMN conversion $0.544$ G per mWb for 2/1. Island
  width (Eq. 16) $w=\frac{4}{2\pi}\sqrt{\frac{q}{q'}\frac{|\Psi_{m/n}|}{m}}$,
  $q'$ the derivative with respect to the equilibrium poloidal flux; for 2/1,
  $w[\mathrm{cm}]=1.54\sqrt{|\Psi_{2/1}|[\mathrm{mWb}]}$.
* **Toroidal Fourier power-transfer analysis** (App. A, Eqs. A1–A31). Fields
  expanded as $\sum_{n=-n_{\max}}^{n_{\max}}(\cdot)_n(R,Z)e^{-in\phi}$;
  harmonic energy densities $\rho_0|\mathbf v_n|^2$ and
  $|\mathbf B_n|^2/\mu_0$ for $n\ne0$ (factor 2 from $\pm n$), internal
  energy zero for $n\ne0$ because $p$ (not $n_e$, $T$) is expanded; density
  perturbations neglected in the kinetic energy. Magnetic power from
  Poynting's theorem per harmonic,
  $\mu_0^{-1}\partial_t\mathbf B_n\cdot\mathbf B_n^*=-\nabla\cdot(\mathbf E_n\times\mathbf B_n^*)/\mu_0-\mathbf E_n\cdot\mathbf J_n^*$,
  with $\mathbf E$ from Ohm's law; kinetic power from the momentum equation.
  Terms grouped (each plus complex conjugate) as advective, linear (products
  of equilibrium and harmonic-$n$ fields, plus $-\nabla p_n\cdot\mathbf v_n^*$),
  quasi-linear (the same with the $n=0$ perturbations), nonlinear (products
  of perturbations with all $n=0$ parts excluded), dissipative
  ($-\eta|\mathbf J_n|^2$ plus the neoclassical stress powers) and Poynting
  flux. Volume-integrated power $P_n$ (A30) and flux-surface-averaged power
  density (A31).
* **Linear runs** find $n=2$ and $n=3$ stable (§IV).

# Tests and results

* **Case.** DIII-D IBS 174446 at 3390 ms, ITER-similar shape, ELMing
  H-mode, $q=2$ at $s=0.69$.
* **Table I** (at the 2/1 surface, simulation / experiment):

  | Quantity | Simulation | Experiment |
  |---|---|---|
  | Lundquist number $S$ | $2.5\times10^6$ | $7.9\times10^6$ |
  | Prandtl number | 23 | 11 |
  | $(\kappa_\parallel/\kappa_\perp)^{1/4}$ | 100 | 260 |
  | $\tau_{\mathrm{nc},e}^{-1}$ | $8\times10^5$ s⁻¹ | $1.3\times10^5$ s⁻¹ |
  | $\tau_{\mathrm{nc},i}^{-1}$ | $1\times10^3$ s⁻¹ | $1.4\times10^3$ s⁻¹ |
  | $\tau_{\mathrm{nc},e}^{-1}/(\tau_{ei}^{-1}+\tau_{\mathrm{nc},e}^{-1})$ | 0.55 | 0.43 |

* **2/1 helical flux** (Fig. 5A; figure readings): pulse spike about
  5–6 mWb; slow phase at about 4–5 mWb to about 8 ms; robust growth
  3.4 Wb/s (MRE 3.3 Wb/s); about 28 mWb at about 16 ms.
* **Other helicities** (Fig. 5B; readings): 3/1 peak near 40 mWb during the
  pulse; 4/3 near 27 mWb at about 6 ms; 3/2 near 34 mWb at about 8 ms.
* **Islands** (Fig. 7): 2/1 width 2–3 cm (3 ms), 5 cm (15 ms); stochastic
  core inside $q=2$ at 15 ms.
* **Mode energies** (Fig. 9): $n=1$ slow growth 3–8 ms, delayed relative to
  the 2/1 flux by the 3/1 decay; $n>3$ energies much smaller (narrower
  radial extent).
* **Powers**: Claims 19–26; Fig. 10 (volume powers), Figs. 11–13
  (flux-surface-averaged profiles at 15.5, 5.0, 8.39 ms).
* No code-to-code comparison; the experimental comparison is qualitative
  ("the goal of this study isn't to reproduce the experiment", §V).

# Notation map

| Howell et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $n$ (density), $n_\alpha$ | $n_e=n_i$, $n_s$ | **collision:** native $n$ is also the toroidal mode number |
| $n$, $m$ (mode numbers) | $n$, $m$ | |
| $\rho$ (Eq. 2), $\rho_0$ | $\rho$, $\rho_0$ | mass density |
| $\rho$ (Eqs. 14, 15, A5) | $s$ | **collision:** radial flux coordinate; registry forbids $\rho$ as a radial label |
| $\rho_N$ | $s$ | "normalized toroidal flux"; whether square-rooted not stated |
| $\Theta$ | $\theta$ | flux-aligned poloidal angle, type not stated |
| $\phi$, $\Phi$ (Eq. 15) | $\phi$ | **collision:** native $\Phi$ (an angle) vs registry electrostatic potential |
| $\mathcal J$ | $\mathcal J$ (page-local) | Jacobian of $(s,\theta,\phi)$ |
| $\vec v$, $\vec v_\alpha$ | $\mathbf v$, $\mathbf v_s$ (page-local) | |
| $p$, $p_\alpha$, $T_\alpha$ | $p$, $p_s$, $T_s$ | |
| $\vec q_\alpha$ | $\mathbf q_s$ (page-local) | **collision risk** with safety factor $q$ |
| $\alpha$ (species) | $s$ | |
| $D_n$ | $D$ (page-local, isotropic) | registry has only $D_\parallel$, $D_\perp$ |
| $\kappa_B$ | $D_B$ (page-local) | **collision:** registry $\kappa$ is heat conductivity |
| $\chi_\parallel$, $\chi_\perp$ | $\kappa_\parallel$, $\kappa_\perp$ | thermal diffusivities |
| $\vec B$, $\vec E$, $\vec J$, $\mu_0$ | $\mathbf B$, $\mathbf E$, $\mathbf J$, $\mu_0$ | SI |
| $\eta$, $\eta_0$ | $\eta$, $\eta_0$ | Spitzer-like profile |
| $\nu_{ei}=\eta ne^2/m_e$ | $\tau_{ei}^{-1}$ (page-local) | **collision:** registry $\nu$ is viscosity |
| $\vec{\vec\pi}_i$, $\vec{\vec\pi}_e$, $\vec{\vec\Pi}$ | $\mathsf\Pi_i$, $\mathsf\Pi_e$ | registry $\mathsf\Pi_s$ |
| $\mu_\alpha$ ($\mu_i$, $\mu_e$) | $\tau_{\mathrm{nc},s}^{-1}$ (page-local) | **collision:** registry $\mu$ is the magnetic moment |
| $m_i$, $m_e$, $e$, $Z_{eff}$ | $m_i$, $m_e$, $e$, $Z_{\mathrm{eff}}$ | |
| $\langle\ldots\rangle$ | $\langle\cdot\rangle$ | flux-surface average |
| subscript "eq" | subscript 0 | equilibrium |
| $\vec e_\Theta$ | $\mathbf e_\theta$ (page-local) | $\propto$ equilibrium poloidal field |
| $\hat n$ | $\mathbf n$ | boundary normal |
| $\vec B_{mp}$, $\mathrm{Env}$, $E_0$, $\tau$, $t_w$, $t_o$ | $\mathbf B_{\mathrm{mp}}$, $\mathrm{env}$, $E_0$, $\tau$, $t_w$, $t_o$ (page-local) | **collision risk:** $E_0$ is an amplitude, not a field |
| $\Omega$ (MP modulation) | $\omega_{\mathrm{mp}}$ | **collision:** registry $\Omega_s$ is a cyclotron frequency |
| $K$, $\Omega_E$ | $K$, $\omega_E$ (page-local) | poloidal-flow coefficient; toroidal angular rotation |
| $\psi_{m,n}$ | $\Psi_{m/n}$ | **collision:** registry $\psi$ is poloidal flux per radian |
| $\tilde B$, $\tilde f$, $\tilde J_0$ etc. | $\delta\mathbf B$, $\delta(\cdot)$ | |
| $w$ | $w$ | island width |
| $q$, $q'$, $q_0$, $q_{95}$, $\Delta'$ | same | $2\pi$ convention of the flux in $q'$ not stated |
| $\beta_n$ | $\beta_N$ | |
| $E_{kin}$, $E_{mag}$, $E_{int}$, $E_n$ | $W_{\mathrm{kin}}^{(n)}$, $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{th}}$ | **collision risk** with $\mathbf E$ |
| $e_{kin,n}$, $e_{mag,n}$, $P_n$, $\langle Q_n\rangle$, $V'$ | words / page-local | |
| $\Gamma$ | $\Gamma$ | |

Sign conventions: Fig. 7A labels rational surfaces with negative $q$
(NIMROD orientation) while the text uses $|q|$; $\phi$ orientation not
stated; $e^{-in\phi}$ (A7–A9) vs $e^{i(n\phi-m\theta)}$ (Eq. 14).

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below; chunk 3 extended some. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [JOREK](/software/jorek.md)
* [Modified Rutherford equation](/definitions/modified-rutherford-equation.md)
* [Neoclassical tearing mode](/definitions/neoclassical-tearing-mode.md)
* [NIMROD](/software/nimrod.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Resonant magnetic perturbations and plasma response](/definitions/resonant-magnetic-perturbation.md)
* [Sawtooth crash and Kadomtsev reconnection](/definitions/sawtooth-crash.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2022_Crossref_Physics_of_Plasmas_Howell_Growing_neoclassical_tearing_modes_seeded_via_transient-indu.pdf`.
   * **Version.** arXiv:2110.12068v1 [physics.plasm-ph], 22 Oct 2021
     (preprint dated 26 Oct 2021), 18 pages; not the publisher version.
     Section, equation and figure numbers are those of the preprint; the
     published numbering was not checked.
   * **Identity.** doi:10.1063/5.0076253, checked on Crossref by title: Phys.
     Plasmas 29(2), article 022507, published 2022-02-01; six authors as on
     page 1.
   * **How read.** Full text; Eqs. 1–7 and 8–10 checked on the rendered
     pages 2–3; App. A read from the extracted text; plot values are the
     reader's approximate readings.
   * **Recorded as printed.**
     * Phases: the Abstract and §V say two phases, §III B says "three
       distinct phases" and describes four stages (pulse, decay to 1.5 ms,
       slow growth, robust growth).
     * Slow-phase windows differ: 2/1 flux 1.5–8 ms (§III B, §IV); $n=1$
       energy 3–8 ms (§IV); Fig. 10 caption "5 ms to 10 ms"; robust
       transition "around 10 ms" (§IV).
     * Eq. A30 prints $2\pi\int\rho\oint d\Theta\,\mathcal J\,\frac{d}{dt}e_n$;
       the radial measure is missing ($\int d\rho$, cf. Eq. A5).
     * App. A cites "the kinetic energy in Eq. (A11)"; the kinetic energy is
       Eq. A10, A11 the magnetic energy.
     * Sign of the ion stress: Eq. 2 has $-\nabla\cdot\mathsf\Pi_i$, Eqs. A23
       and A28 write $+\nabla\cdot\mathsf\Pi$ dotted with
       $\mathbf v_n^*$; with Eq. 8 as printed this would make the
       "dissipative" power positive (compiler's check; the paper does not
       state the sign used in the diagnostic).
     * "$\mu_i\gg1$" (§II A) compares a rate in s⁻¹ with 1; the reference
       frequency is missing.
     * Eq. 3 prints $\nabla\cdot v$ and Eq. 5 prints $E$ without vector
       arrows; Eq. 15 uses $\Phi$ for the toroidal angle.
     * Island width "in units of flux" (Eq. 16) is converted to cm without
       a stated flux-to-length factor.
     * "Within a factor of 2 or 6" (§III A): Table I ratios are $S$ 3.2×,
       Prandtl 2.1×, $(\kappa_\parallel/\kappa_\perp)^{1/4}$ 2.6× (so the
       anisotropy itself differs by about 46×), electron damping 6.2×, ion
       damping 1.4× (compiler's check).
     * Fig. 12 caption: $q=1.17$ and $1.2$ where the text says 7/6 and 6/5
       (consistent up to rounding).
     * The Abstract cites La Haye et al. as "Proceedings IAEA FEC 2020";
       ref. [29] reads "Submitted to Nucl. Fusion (2021)".
     * The 3.3 Wb/s MRE value and the negligible-$\Delta'$ argument rest on
       ref. [30], "In preperation (2021)".
     * Typos: "derrived", "denisty", "preformed", "most interacting case",
       "a island", "such has flattening", "an a applied MP".
   * **Reference list.** 39 printed entries, merged into the bibliography
     under `howell-2022`. Hu Q. et al., Nucl. Fusion 59:016005 (printed
     2018), is `hu-2018-c` (`hu-2018` and `hu-2018-b` are other works).
     Ref. [4], printed "R. Carrera", is Carreras, Hazeltine &
     Kotschenreuther, Phys. Fluids 29:899 (1986), kept under the printed
     spelling `carrera-1986` for the closing `--dupes` sweep. Existing keys
     reused: `chang-1995`, `rutherford-1973`, `held-2015`, `gianakon-2002`,
     `meshcheriakov-2019`, `kim-2020`, `sovinec-2004`, `lao-1985` (printed
     "H. S. John" is St John). Printed defects: author lists ending
     "… and" in [1], [17], [18], [19], [21]; [2] "R. J. L. Haye" (La Haye)
     with year 2016 for the 2017 volume 57; [18] "E. D. la Luna"; [5] has no
     title; [29], [30] unpublished; no titles printed except in [3].
