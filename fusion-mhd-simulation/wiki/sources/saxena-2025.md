---
type: Source
title: "Saxena et al. (2025) — Bootstrap current modeling in M3D-C1"
description: "Adds Sauter and Redl bootstrap-current closures to M3D-C1 as a non-inductive current in Ohm's law, extended to quasi-symmetric stellarators through the Landreman isomorphism and evaluated on temperature isotherms as proxy flux surfaces; verifies it against XGCa, NEO and SFINCS for a tokamak and two quasi-axisymmetric stellarators and applies it to nonlinear quasi-axisymmetric stellarator simulations."
resource: "doi:10.1017/S0022377825100834"
source_kind: paper
authors: [Saxena S., Ferraro N.M., Martin M.F., Wright A.]
year: 2025
venue: "J. Plasma Phys. 91:E141"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Journal_of_Plasma_Physics_Saxena_Bootstrap_current_modeling_in_M3D-C1.pdf"
tags: [bootstrap-current, stellarator, tokamak, extended-mhd, full-mhd, equilibrium, finite-elements, verification, code]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper adds a self-consistent bootstrap-current source to the
extended-MHD code [M3D-C1](/software/m3d-c1.md), for tokamaks and for
quasi-symmetric stellarators. The bootstrap current enters as the
non-inductive current $\mathbf J_x$ of a modified Ohm's law,
$\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_x)$, which
is equivalent to an electron force that removes $\mathbf J_x$ from the
electron–ion friction, so that the current relaxes resistively toward
$\mathbf J_x$. $\mathbf J_x$ is purely parallel, with
$\mathbf J_x\cdot\mathbf B/B^2$ a surface function fixed by the surface
average $\langle\mathbf J_x\cdot\mathbf B\rangle$, which comes from
analytic fits: Sauter et al. (1999) or the revised fit of Redl et al.
(2021). For quasi-symmetric stellarators the isomorphism of Landreman,
Buller & Drevlak (2022) maps these fits to fields whose strength depends
on the flux label and one helical angle (the "Sauter–Redl–Landreman"
formula). Because M3D-C1 does not assume flux surfaces, the
surface-averaged geometric quantities are computed outside the code with
Fusion-IO on isotherms of $T_e$ used as proxy surfaces, read in and
re-extrapolated to the mesh every time step, while the closure
coefficients are evaluated locally every step. On the tokamak CIRC1 case
(Hager & Chang 2016) the result agrees with XGCa, NEO and SFINCS to
0.04–2.2% at the profile peak; for two quasi-axisymmetric (QA)
stellarators it closely matches SFINCS and the standalone Redl formula.
Nonlinear QA runs at $\langle\beta\rangle=2.5\%$ show that the model
sustains the toroidal current against resistive decay and slows the
breakup of edge surfaces, while instability growth still increases with
resistivity, supporting Wright & Ferraro (2024a). An M3D-C1 → SFINCS
workflow to estimate the error away from quasi-symmetry is outlined, not
demonstrated.

# Key claims

1. **Bootstrap as a non-inductive current** (§2, Eq. 2.1). The modified
   Ohm's law is equivalent to an electron force $-\eta n_ee\mathbf J_x$
   that removes the share of $\mathbf J_x$ from the electron–ion
   friction; "collisional drag will cause the current density to decay
   towards $\mathbf J_x$", and $\mu_0\mathbf J=\nabla\times\mathbf B$
   evolves on the resistive time scale. Derived/Stated.
2. **No net force** (§2). For an internal force such as the bootstrap
   drive an equal and opposite force acts on the ions, so no net force
   enters MHD force balance. Stated.
3. **Parallel, divergence-free $\mathbf J_x$** (§2, Eq. 2.2). This
   requires $\mathbf J_x\cdot\mathbf B/B^2$ to be a surface function,
   hence $\mathbf J_x=\dfrac{\langle\mathbf J_x\cdot\mathbf B\rangle}{\langle B^2\rangle}\mathbf B$.
   Derived.
4. **Fit validity** (§1). Sauter is less accurate at electron
   collisionality above 1, limiting it near the edge; Redl, fitted to NEO,
   holds over a broader range; both are fitted only to axisymmetric
   geometry. Stated, attributed to Koh et al. (2012), Landreman & Ernst
   (2012), Redl et al. (2021).
5. **Isotherms as flux surfaces** (§2). With $\kappa_\parallel\gg\kappa_\perp$,
   $T_e$ isotherms coincide with magnetic surfaces when these exist and the
   dynamics are slow; without surfaces they relate to quadratic-flux-
   minimizing surfaces (Dewar, Hudson & Price 1994). Stated.
6. **Tokamak CIRC1 verification** (§3.1, Fig. 1b). At the peak
   ($\psi_N\approx0.89$, inverse aspect ratio 0.63, electron
   collisionality 0.92): M3D-C1 Sauter vs NEO Sauter 2.18%; M3D-C1
   (Sauter by context) vs XGCa 0.04%; M3D-C1 Redl vs XGCa 2.12% and vs
   SFINCS 1.01%. Shown. Acceptance criterion: "agreement within a few
   percent at the profile peak is generally considered acceptable"; "no
   single code serves as a definitive reference".
7. **QA verification** (§3.2, Fig. 4). M3D-C1's Redl-plus-isomorphism
   profile is "in close agreement" with SFINCS and with the Redl-formula
   calculation of Landreman et al. (2022); remaining differences are
   ascribed to numerics or isotherm–surface misalignment, "although the
   exact sources remain unclear". Shown.
8. **Current sustained** (§3.3, Fig. 5). In nonlinear QA_Case2 with
   resistivity multiplier $10^4$ the toroidal current decays without
   bootstrap and is maintained with it; the plasma remains MHD-unstable in
   both. Shown.
9. **Slower surface breakup** (§3.3, Fig. 6). With bootstrap the edge
   chaotic region at $t=250\tau_A$ is "significantly smaller". Shown.
10. **Resistivity raises growth even with bootstrap** (§3.3, Fig. 7).
    Kinetic energy grows faster with larger resistivity multiplier (1, 10,
    $10^3$, $10^4$) with bootstrap on or off, so the Wright & Ferraro
    (2024a) result is not an artefact of spurious resistive decay of the
    bootstrap-driven current. Shown.
11. **Quasi-symmetry maintained** (§3.3, Fig. 8). The two-term
    quasi-symmetry error evaluated on isotherm surfaces "closely resembles"
    [VMEC](/software/vmec.md)'s and does not change significantly over
    $0<t<250\tau_A$; later the isotherm surfaces are ill-defined and the
    analysis stops. Shown.
12. **Validity and outlook** (§2, §4, Abstract). The Sauter–Redl–Landreman
    model is valid only in quasi-symmetric geometry; its error can be
    assessed post hoc by running SFINCS and NEO 3D on M3D-C1 output, which
    "lays groundwork" for coupled modelling. Stated; no error
    quantification shown.
13. **Time independence** (§4). All these closures (and NEO 3D, SFINCS)
    are steady-state, so they miss a time-dependent neoclassical response
    on Alfvénic time scales (e.g. kinks), which "is not expected to play a
    significant role in such phenomena anyway"; in stochastic regions
    parallel transport along chaotic field lines dominates. Stated.

# Models and numerics

* **Code** (§2, App. C). M3D-C1 (Jardin et al. 2012): extended MHD with a
  split-implicit time scheme allowing steps beyond the Alfvénic scale,
  high-order $C^1$ finite elements on an axisymmetric mesh (element family
  not named here), stellarator capability through non-axisymmetric domain
  geometry (Zhou et al. 2021). SI units with $\mu_0$ explicit.
* **Single-fluid equations** (App. C):
  $$\begin{aligned}
  &\partial_tn+\nabla\cdot(n\mathbf v)=0,\qquad nm_i(\partial_t\mathbf v+\mathbf v\cdot\nabla\mathbf v)=\mathbf J\times\mathbf B-\nabla p-\nabla\cdot(\text{viscous stress})+(\text{external force}),\\
  &\partial_tp+\mathbf v\cdot\nabla p+\Gamma p\nabla\cdot\mathbf v=(\Gamma-1)\big[\eta\mathbf J\cdot(\mathbf J-\mathbf J_x)-\nabla\cdot(\text{heat flux})-(\text{viscous heating})+(\text{heat source})\big],\\
  &\partial_t\mathbf B=\nabla\times[\mathbf v\times\mathbf B-\eta(\mathbf J-\mathbf J_x)],\qquad \mu_0\mathbf J=\nabla\times\mathbf B,
  \end{aligned}$$
  with $\Gamma=5/3$, a heat flux of anisotropic conduction
  ($\kappa_\perp$, $\kappa_\parallel$; sign as printed, see below), and a
  viscous stress of perpendicular, gyro- and parallel ion viscosity, the
  electron viscosity implemented as hyper-resistivity. The bootstrap term
  also modifies the Ohmic heating to $\eta\mathbf J\cdot(\mathbf J-\mathbf J_x)$.
* **Tokamak closures** (App. A). Sauter (Eq. A1) and Redl (Eq. A2) give
  $\langle\mathbf J_x\cdot\mathbf B\rangle$ as $-F(\psi)$ times a sum of
  logarithmic $\psi$-derivatives of pressure (Sauter) or density (Redl)
  and of $T_e$, $T_i$, weighted by $p$, $p_e$, $p_i$ and by the
  dimensionless Sauter/Redl coefficients (functions of the trapped
  fraction, collisionality and $Z_{\mathrm{eff}}$; fits not reproduced).
  Auxiliary definitions: trapped fraction (Eq. A3, a pitch-angle integral
  of the surface average of the square root of one minus pitch times $B$),
  electron and ion collisionalities (Eq. A4) and Coulomb logarithms
  (Eq. A5), with $T$ in eV and $n$ in m⁻³.
* **Stellarator closure** (§2, Eq. 2.3; App. B). For quasi-symmetry with
  helicity $N$ (field strength a function of the flux label and the Boozer
  angle combination $\theta-N\zeta$), the Landreman isomorphism replaces
  $F$ by the Boozer poloidal-current function plus $N$ times the toroidal-
  current function (both times $\mu_0/2\pi$), the $\psi$ derivative by a
  $\psi_t$ derivative divided by $(\iota-N)$ (with
  $\partial_{\psi_t}=\iota\,\partial_\psi$, Eq. B1), the connection-length
  factor $qR$ by its helical analogue, and the inverse aspect ratio by
  $(B_{\max}-B_{\min})/(B_{\max}+B_{\min})$ (Eq. B2). QA has $N=0$.
* **Surface-quantity pipeline** (§2). Fusion-IO builds approximate magnetic
  coordinates from M3D-C1 output on $T_e$ isotherms labelled by
  $1-T_e/T_{e,\max}$ (analogous to $\psi_{t,N}$), and computes the surface
  averages (Boozer current functions, label, trapped fraction, inverse
  aspect ratio, $qR$) and $\iota$ as the ratio of poloidal to toroidal
  flux derivatives with respect to the label. They are read in at the
  start, extrapolated to the mesh, and re-extrapolated each step from the
  evolving isotherm label; the closure coefficients are evaluated locally
  each step. The normalized label avoids recomputation when the profile
  changes amplitude but not shape. Whether the external averages are ever
  recomputed during a run is not stated.
* **Resistivity** (Eq. 3.2): $\eta=2.74\ \Omega\,\mathrm m\times(\text{multiplier})\times T_e^{-3/2}$,
  multiplier $\in\{1,10,10^3,10^4\}$; units of $T_e$ not stated.
* **Nonlinear set-up** (§3.3). QA_Case2 from SIMSOPT (Landreman et al.
  2022), domain bounded by the LCFS; viscosity $\nu=3.65\times10^{-4}$
  kg m⁻¹ s⁻¹; $\kappa_\perp=2.18\times10^{-20}$ m⁻¹ s⁻¹ as printed;
  $\kappa_\parallel$ not given; semi-structured grid with 36 toroidal
  planes and $1.88\times10^5$ 3D elements; times in $\tau_A$, never given
  in seconds. No linear solver, preconditioner, parallelism, GPU or cost
  information.

# Tests and results

* **Tokamak CIRC1** (Hager & Chang 2016; §3.1, Fig. 1). Circular
  cross-section, inverse aspect ratio 0.84 at the boundary (mean minor
  radius over centroid radius), tanh pedestals over $\psi_N=0.7$–1
  ($n\approx2.5$–$4.5\times10^{19}$ m⁻³, $T$ up to about 400 eV). Peak
  $\langle\mathbf J\cdot\mathbf B\rangle/B_0\approx1.4\times10^5$ A m⁻² at
  $\psi_N\approx0.89$ (read from Fig. 1b).

  | Comparison at the peak | Difference |
  |---|---|
  | M3D-C1 Sauter vs NEO Sauter | 2.18% |
  | M3D-C1 (Sauter by context) vs XGCa | 0.04% |
  | M3D-C1 Redl vs XGCa | 2.12% |
  | M3D-C1 Redl vs SFINCS | 1.01% |

* **QA stellarators** (§3.2, Fig. 4). Minor radius 1.70 m, volume-averaged
  $B=5.86$ T, $n=n_0(1-\psi_{t,N}^5)$, $T=T_0(1-\psi_{t,N})$.
  QA_Case1: pure H, $n_0=4.13\times10^{20}$ m⁻³, $T_0=12$ keV, on a
  zero-pressure VMEC equilibrium (bootstrap not self-consistent with it).
  QA_Case2: $n_{e,0}=2.38\times10^{20}$ m⁻³, $T_{e,0}=9.45$ keV, optimized
  for $\langle\beta\rangle=2.5\%$ with self-consistent bootstrap.
  $\langle\mathbf J\cdot\mathbf B\rangle$ is negative, minimum about
  $-7.5$ (Case1) and $-2.7$ MA T m⁻² (Case2) near $\psi_{t,N}\approx0.5$;
  M3D-C1 sits roughly 5–10% deeper than SFINCS and Redl over mid-radius by
  eye; no percentage quoted.
* **Nonlinear QA_Case2** (§3.3). Four resistivity multipliers, bootstrap
  on and off.
  * Fig. 5 (multiplier $10^4$): at $250\tau_A$ the toroidal-current
    profile drifts from its initial form for $\psi_{t,N}>0.55$ without
    bootstrap, stays close with it.
  * Fig. 6: Poincaré sections at 0, 50, 150, 250, 350 $\tau_A$; without
    bootstrap the edge is chaotic by 150 and mostly chaotic by 250; with
    bootstrap more surfaces survive at 150–250; both largely stochastic by
    350.
  * Fig. 7: kinetic energy to $800\tau_A$; multipliers 1 and 10 nearly
    coincide, $10^3$ faster, $10^4$ fastest (saturating about
    $5\times10^{-2}$ near $380\tau_A$); on/off curves close for each.
  * Fig. 8: the quasi-symmetry error rises from about $10^{-5}$ to
    $10^{-3}$ across $\psi_{t,N}$; M3D-C1 at 0 and $250\tau_A$ matches
    VMEC closely; SFINCS at $t=0$ is lower by about 2–3×, uncommented.

# Notation map

| Saxena et al. (2025) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf E$, $\mathbf v$, $\mathbf B$, $\mathbf J=\nabla\times\mathbf B/\mu_0$ | same | SI |
| $\eta$, $\eta_{norm}$, $\eta_0$ | $\eta$; words (2.74 Ω m; resistivity multiplier) | |
| $\mathbf J_x$, $J_\parallel$ | $\mathbf J_x$; words | |
| $\mathbf F^e_x$ | words (equivalent electron force) | **collision** with $F$ |
| $\langle\cdot\rangle$ | surface average (words; not yet in registry) | on $T_e$ isotherms |
| $\psi$, $\psi_t$ ($\Psi_p=2\pi\psi$, $\Psi_t=2\pi\psi_t$) | $\psi$, $\psi_t$ | per radian |
| $\psi_N$, $\psi_{t_N}$/$\Psi_{t_N}$ | $\psi_N$, $\psi_{t,N}$ | |
| $\hat T_e=1-T_e/T_e^{max}$ | words (isotherm label) | |
| $F(\psi)$ | $F$ | |
| $G$, $I$, $\tilde G=G+NI$ | words (Boozer current functions) | **collision:** native $I$ vs $I_p$ |
| $\iota$, $q$ | $\iota$, $q$ | |
| $N$, $M$ | words (toroidal and poloidal helicity of the symmetry) | **collision risk:** not $N_{\mathrm{fp}}$; registry $m$, $n$ are mode numbers |
| $\theta$, $\zeta$ | $\theta$, $\zeta$ | Boozer angles |
| $L_{31}$, $L_{32}$, $L_{34}$, $\alpha$ | words (Sauter/Redl coefficients) | |
| $f_t$ | words (trapped fraction) | **collision risk** with $f_s$ |
| $\lambda$ (Eq. A3) | words (pitch variable) | **collision risk** with $\lambda_{\mathrm o}$ |
| $\epsilon$/$\varepsilon$ | words (inverse aspect ratio) | **collision** with $\varepsilon_0$ |
| $qR$ | words (connection-length factor) | |
| $\nu^*_e$, $\nu^*_i$ | words (collisionalities) | **collision:** registry $\nu$ is viscosity |
| $\Lambda_e$, $\Lambda_{ii}$ | words (Coulomb logarithms) | printed without $\ln$ |
| $Z$ | $Z$ (ion charge), $Z_{\mathrm{eff}}$ | |
| $p,p_e,p_i$; $n,n_e,n_i$; $T_e,T_i$ | same | eV, m⁻³ |
| $\boldsymbol\Pi$, $\mathbf F$, $Q$ | words (viscous stress, external force, heat source) | registry lacks a viscous-stress symbol |
| $\mathbf q$ | words (heat flux) | **collision** with safety factor $q$ |
| $\Gamma$ | $\Gamma$ | 5/3 |
| $\kappa_\perp$, $\kappa_\parallel$ | same | density × diffusivity units |
| $\nu$ | $\nu$ | viscosity, kg m⁻¹ s⁻¹ |
| $F_{QS}$ | words (two-term quasi-symmetry error) | |
| $\tau_A$ | $\tau_A$ | not given in seconds |
| $J_y$ | $J_\phi$ (words: toroidal current density) | Fig. 5 label |
| $(R,\phi,Z)$ | $(R,Z,\phi)$ | $\phi$ orientation not stated |

# Pages created or updated

Chunk 1 (2026-10-16) created every page of the bundle; chunk 2 (2026-10-16) extended many. This source is cited on:

* [Bootstrap current and its MHD implementation](/definitions/bootstrap-current.md)
* [Edge-localized mode (ELM) and ELM-free regimes](/definitions/edge-localized-mode.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [M3D-C1](/software/m3d-c1.md)
* [NIMROD](/software/nimrod.md)
* [Quasi-symmetry](/definitions/quasi-symmetry.md)
* [Single-fluid visco-resistive MHD model](/methods/visco-resistive-mhd-model.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [VMEC](/software/vmec.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2025_Crossref_Journal_of_Plasma_Physics_Saxena_Bootstrap_current_modeling_in_M3D-C1.pdf`.
   * **Version.** Publisher version of record (Cambridge University Press,
     open access CC BY), 16 pages. Received 8 Jul 2025, accepted 22 Aug
     2025, online 17 Oct 2025.
   * **Identity.** doi:10.1017/S0022377825100834, checked on Crossref: J.
     Plasma Phys. 91(5), article E141, issued 2025-10; four authors as
     printed (PPPL; Thea Energy; Univ. Wisconsin–Madison); reference count
     49.
   * **How read.** Full text including Appendices A–C; equations
     transcribed from the extracted text; the reader notes do not list
     rendered-page checks. Plot values are approximate readings.
   * **Recorded as printed.**
     * The abstract attributes the isomorphism to "Landreman et al. (2022
       Phys. Rev. Lett. vol. 128, pp. 035001)", which is Landreman & Paul
       (2022), "Magnetic fields with precise quasisymmetry"; the
       isomorphism is Landreman, Buller & Drevlak (2022), Phys. Plasmas
       29:082501. In the body "Landreman et al. (2022)" is ambiguous
       between the two.
     * Sign: the tokamak forms (A1, A2) carry $-F$, the stellarator form
       (2.3) carries $+$(Boozer function)$/(\iota-N)$; with $N=0$ and
       Eq. B1, (2.3) becomes $+F\partial_\psi(\cdots)$, opposite to A2,
       yet App. B says it "recovers the result of Redl et al. (2021)". The
       density term also differs in form (separate electron and ion
       logarithmic derivatives vs a single one), equivalent only for
       $n_e\propto n_i$. No orientation convention for $\psi$, $\psi_t$ is
       stated (compiler's check of the printed equations).
     * Eq. A5 prints the Coulomb logarithms as $\Lambda=31.3-\ln(\cdots)$
       although these are $\ln\Lambda$ (Sauter form) and Eq. A4 takes
       their logarithm again.
     * Eq. A4b uses $n_e$ in the ion collisionality where Sauter (1999)
       uses $n_i$ (not verified against Sauter here).
     * Eq. C5: the perpendicular heat flux has a $+$ sign and the full
       gradient, against the Fourier form $-\kappa_\perp\nabla_\perp T$.
     * App. C labels both the gyroviscosity and the parallel viscosity
       with the same symbol ($\boldsymbol\Pi_i^\wedge$) in the text.
     * $\kappa_\perp=2.18\times10^{-20}$ m⁻¹ s⁻¹ (§3.3) is implausibly
       small at $n\sim10^{20}$ m⁻³ (exponent-sign typo likely); not
       verifiable.
     * The resistivity scale 2.74 Ω m cannot be checked against Spitzer
       since the unit of $T_e$ is unstated.
     * Fig. 1 legend ("NEO-3D", "NEO-2D: Sauter") vs text ("NEO code's
       Sauter model"); the 0.04% XGCa comparison does not name the M3D-C1
       model.
     * Fig. 4 axis "⟨J.B⟩ [MAT m⁻²]"; "beyond t > 250" without units.
     * §1: "(Schlutt et al. Schlutt et al., 2012, 2013; …)"; NIMSTELL
       cited as "Carl & Brian 2021" (given and family names swapped).
     * Fig. 7: by eye the bootstrap-on curve at multiplier $10^4$ reaches
       $10^{-2}$ slightly earlier (about $330\tau_A$) than bootstrap-off,
       which sits awkwardly with the Fig. 6 statement that bootstrap slows
       surface breakup; uncommented (low-confidence reading).
     * The abstract and §4 call the SFINCS workflow "presented", but no
       procedure or result away from quasi-symmetry is shown.
   * **Reference list.** 49 printed entries (= Crossref count), merged into
     the bibliography under `saxena-2025`. Jardin et al. 2012 is printed
     twice as 2012a and 2012b (same Comput. Sci. Discov. work; 2012b with
     "globle") and is the single entry `jardin-2012`; the J. Comput. Phys.
     review is `jardin-2012-b`; the Sauter et al. erratum (2002) is
     `sauter-2002-b`. Nikulsin 2022 (JOREK3D, "Team, JOREK" printed as an
     author) is the ingested `nikulsin-2022`. Other printed defects: Dewar
     et al. 1994 as "Phys. Rev. A 194, 49–56" (Phys. Lett. A); Belli &
     Candy "2011" in PPCF vol. 54 (2012); Paul et al. 2020 with garbled
     author order; Landreman 2019 without venue; Hirshman & Whitson 1983
     cites the ORNL report (ORNL/TM-8861), not Phys. Fluids 26:3553;
     Monticello 1993 (an IAEA meeting summary) cited for CQL3D; Futatani
     et al. 2021 with team names merged into the author list; Lyons 2015
     "solvera".
