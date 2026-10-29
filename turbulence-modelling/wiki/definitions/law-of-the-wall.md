---
type: Definition
title: "Law of the wall"
description: "The inner-layer mean-velocity profile of wall-bounded turbulence — viscous sublayer, buffer layer and logarithmic layer in wall units — with the constants, composite fits and damping functions the sources use, its compressible, displaced (canopy) and outer-layer (defect-law) extensions, and its role as the target every wall model and data-driven RANS correction must reproduce."
status: established
aliases: [logarithmic law, log law, law-of-the-wall profile, inner-layer profile]
tags: [boundary-layer, wall-model, wmles, rans]
timestamp: 2026-10-29T16:21:00Z
---

# Law of the wall

The law of the wall states that, in the inner layer of a smooth-wall turbulent
flow in equilibrium, the mean velocity scaled by the friction velocity is a
universal function of the wall distance in viscous units,
$u^+=f(y^+)$, with $u^+=\langle u\rangle/u_\tau$, $y^+=y/\delta_\nu$,
$u_\tau=\sqrt{\tau_w/\rho_w}$ and $\delta_\nu=\nu_w/u_\tau$ (let $f$ denote this
universal profile, page-local). Its two asymptotes are the viscous sublayer,
$u^+=y^+$, and the logarithmic layer,

$$u^+=\frac1\kappa\ln y^++B ,$$

joined through a buffer layer. Every wall model of this bundle is a way of
inverting $f$ (or an ODE whose solution is $f$) to obtain $\tau_w$ from a
velocity sampled away from the wall; see the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

## Constants used by the sources

The sources do not agree on one pair $(\kappa,B)$; each states its own values,
and the choice is part of the model.

| Source | $\kappa$ | $B$ | Other constants | Use |
|---|---|---|---|---|
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), Eq. (1) | 0.41 | 5.2 | quadratic branch below $y^+=23$ | algebraic wall model in [CharLES](/software/charles.md) |
| [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), Eq. (1) | 0.4 | 5 | | algebraic wall model in [LESGO](/software/lesgo.md); reference for log-layer mismatch |
| [Fowler et al. (2022)](/sources/fowler-2022.md), App. C | 0.4 | 4.95 | $\kappa_2=9.753$, $\beta=1.903$ (fit) | composite fit (C1); their Fig. 4 log law uses $B=5.0$ |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §1 | 0.41 | — | $A^+=17$ | mixing length with van Driest damping |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.D | 0.38 (DNS value at $Re_\tau=4200$) | — | | reference slope for the log-layer error of WMLES |
| [Gillyns et al. (2022)](/sources/gillyns-2022.md), §3, Eq. (3) | 0.38 | 4.1 | Reichardt profile; Österlund et al. values, as they cite them | algebraic wall model in a spectral-element code |
| [Bae & Koumoutsakos (2022)](/sources/bae-2022.md), Eq. (3), Fig. 2 | 0.41 | 5.2 | | reference log law of the reinforcement-learning wall models |
| [Cao et al. (2022)](/sources/cao-2022.md), Eq. (8) | 0.40 | 5.5 | "for the low Reynolds number turbulent channel flow" | estimate of $u_\tau$ for a channel DNS at $Re_\tau=180$ |
| [Knopp (2022)](/sources/knopp-2022.md), §4, Eq. (26) | 0.41 | 5.0 | with Coles' wake, after Coles & Hirst | fit of boundary-layer thickness in adverse pressure gradient |
| [Cogo et al. (2022)](/sources/cogo-2022.md), Fig. 8 | 0.41 | 5.2 | | reference for transformed compressible profiles |
| [Kim et al. (2022)](/sources/kim-2022.md), Fig. 12 | 0.41 | 5.2 | | reference line for the mean velocity of LES with learned SGS models at $Re_\tau=180$–720 |
| [Dang et al. (2022)](/sources/dang-2022.md), Fig. 17 legend | $1/2.44$ | 5.1 | | reference for van Driest-transformed DNS profiles upstream of a Mach 2.9 ramp |
| [Cai et al. (2022)](/sources/cai-2022.md), Eq. (26) | not printed | $\kappa^{-1}\ln E$, $E=11.27$ | blend constants 10.71 and 1.526 | log law written $u^+=\kappa^{-1}\ln(Ey^+)$; explicit equilibrium wall model in a lattice Boltzmann solver |
| [Blind et al. (2023)](/sources/blind-2023.md), §3.3 | not printed | not printed | Spalding's law | algebraic wall model in [FLEXI](/software/flexi.md) |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), Figs. 4–5 | not printed | not printed | Reichardt's law | reference profile for IDDES of channel flow |
| [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §3.2, Eq. (3.1) | 0.41 | 5.2 | quadratic branch below $y^+=23$ | equilibrium baseline of the [building-block-flow wall model](/methods/building-block-flow-wall-model.md), sampled at the second grid point |
| [Lewis et al. (2023)](/sources/lewis-2023.md), §3.2.2 | not printed | not printed | linear for $y^+<11$, logarithmic above | wall law of fan-stage WMLES in AVBP |
| [Kang et al. (2023)](/sources/kang-2023.md), figures | 0.41 | 5.2 | | reference line for LES of channel flow at $Re_\tau=180$ and 395 with learned SGS models |
| [Wang et al. (2023b)](/sources/wang-2023-b.md), Eq. (10) | 0.40 | 5.5 | "for the low Reynolds number turbulent channel flow" | reference for van Driest-transformed compressible channel DNS |
| [Zhao et al. (2023a)](/sources/zhao-2023.md), Eqs. (25)–(26) | 0.40 | 5.5 | "selected for the low-Reynolds-number turbulent channel flow" | sets the viscosity of a channel at a target $Re_\tau$ |
| [Zhao et al. (2021)](/sources/zhao-2021-c.md), §IV, Eqs. (25)–(26) | 0.40 | 5.5 | centreline form $U_c^+=2.5\ln y_c^++5.5$ | sets the viscosity of a gas-kinetic LES channel at $Re_\tau=180$ and 395, the procedure of Zhao et al. (2023a) below |
| [Bose & Park (2018)](/sources/bose-2018.md), §2.1, Eq. (3) | $\approx0.41$ "for ZPG layers"; 0.4 in a non-equilibrium model of their Fig. 6b | not printed | Spalding and Werner–Wengle composites, a pressure-gradient variant, Monin–Obukhov similarity for stratified flow (as cited) | algebraic wall-stress model of their WMLES review |
| [Heinz (2020)](/sources/heinz-2020.md), §2.3, Eqs. (9)–(11) | 0.43 implied by the $k$-$\varepsilon$ constants 1.44, 1.92, 1.3; 0.41 by the $k$-$\omega$ and SAS constants | — | log-layer values of $k$, $\varepsilon$, $\nu_t$ | consistency condition of RANS model constants (below) |
| [Lv et al. (2021)](/sources/lv-2021.md), §II A, Eq. (3); Fig. 11 | 0.41 | 5.2 (Fig. 11) | basis $\kappa^{-1}\ln\big((y+y_0)/y_0\big)$ | the log law as a basis function of the wall-adjacent cell (below) |
| [Zangeneh (2021)](/sources/zangeneh-2021.md), Fig. 6 | 0.41 | 5.2 | | reference for the van Driest-scaled velocity of WMLES of a supersonic plate |
| [Vadrot et al. (2023a)](/sources/vadrot-2023.md), §II.B.1, Eq. (1); §II.B.3 | $\approx0.4$ (0.4 in the states and figures) | $\approx5$ | | algebraic wall model and reference log law of reinforcement-learning wall models in LESGO |
| [Constant et al. (2024)](/sources/constant-2024.md), §3.2, Eq. (8) | 0.41 | not printed | Musker's law (form not printed); van Driest damping $1-e^{-y^+/19}$ in the target-point eddy viscosity | wall function at immersed-boundary target points in RANS |
| [Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §2.2, Eqs. (12)–(15) | $\approx0.41$ | $\kappa^{-1}\ln E$, $E\approx7.9$ | blend constants $s=86.58$, $p=0.7894$ | explicit equilibrium wall model in a lattice Boltzmann solver |
| [Chen et al. (2024)](/sources/chen-2024.md), §2.3, Eqs. (2.7), (2.10) | 0.40 | — | $A^+=26$ divided by the square root of the local total shear stress in wall units; Johnson–King reference damping with 17 | mixing length of the algebraic [Baldwin–Lomax model](/methods/baldwin-lomax-model.md) (a RANS closure, not an LES wall model) |
| [Mukha et al. (2025)](/sources/mukha-2025.md), §III.A, App. A | 0.387 | 4.2 | Spalding's law (formula not printed); values from the channel DNS of Yamamoto & Tsuji at $Re_\tau\approx8000$, as cited | algebraic wall model of spectral-element WMLES of channel flow in [Nek5000](/software/nek5000.md) |
| Mukha et al. (2025), §IV.A; App. A | 0.41 | 5.2 (§IV.A) or 5.5 (App. A) | Spalding's law | the same model for a zero-pressure-gradient flat-plate boundary layer (see Qualifications) |
| [Lohrer & Fröhlich (2025)](/sources/lohrer-2025.md), §5.2, Eqs. (5.7)–(5.8) | 0.41 (0.38 when fitted) | 5.5 | roughness function $\Delta U^+_{\mathrm{vo}}=15.4$ (17.4 with fitted $\kappa$); $B$ after Nezu & Nakagawa (1993), as cited | displaced log law above a submerged flexible canopy (below) |
| [Oulghelou et al. (2025)](/sources/oulghelou-2025.md), Figs. 4, 11 | 0.41 | 5.2 | | reference log law for blended data-driven RANS corrections in channel and flat-plate flow |
| [Wu et al. (2025)](/sources/wu-2025.md), §2.1, Eq. (3) | 0.41 | — | | log-layer calibration constraint of the $k$-$\omega$ SST $\omega$ equation (below) |
| [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §5.2.1, Eqs. (93)–(94) | 0.39 | — | $A^+=26$ in the mixing length, $\nu_t=l^2\lvert\partial u/\partial y\rvert$ | mixing-length model used to verify a high-order HDG RANS solver in channel flow; their flat-plate profile is compared with Coles' law (§5.3) |
| [Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §3.3, Eqs. (12)–(13); §4 | $\sim0.41$ | 5 | power law $u^+=8.3\,(y^+)^{1/7}$ above $y^+=11.81$; Spalding's law for comparison | explicit [RANS wall function](/methods/rans-wall-function.md) in a high-order DG solver (below) |
| [Lederer et al. (2026)](/sources/lederer-2026.md), §4.2 | 0.41 | 5.2 | log layer quoted as $40<y^+<200$; constants "experimentally fitted for mild adverse pressure gradients" | reference for implicit DG LES of the transitional [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md) |
| [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md), §4.1, Eq. (4.1) | 0.41 | — | van Driest profile, $A^+=26$ | volume-filtered to model the wall slip of immersed-boundary WMLES (below) |
| [Aiello et al. (2026)](/sources/aiello-2026.md), §4.1, Fig. 1 | 0.41 | 6.0 (fitted) | in $y^*$, log region from $y^*\ge40$ | Trettel–Larsson-transformed DNS of a thermally perfect CO$_2$ channel at $Re_\tau^*=160$–190 |
| [Nuca et al. (2025)](/sources/nuca-2025.md), §V.B, Table V | 0.387 | 4.21 | "high-Re" set after Yamamoto & Tsuji, as cited; the corresponding $C$ and $A^+$ are not printed | fixed-parameter explicit approximations of the Spalding, Reichardt and ODE wall models (below) |
| Nuca et al. (2025), §V.B, Table VI | 0.4 (Spalding, Reichardt); 0.41 (ODE) | 5.5 | $C=7.8$ (Reichardt); $A^+=17$ (ODE), "essentially a standard choice" | "classical" set of the same approximations |
| Nuca et al. (2025), §V.A, Table II | 0.38–0.42 | 4.2–5.5 | $C\in[6.8,7.7]$, $A^+\in[15,19]$ | parameter ranges over which the global explicit approximations are fitted |
| [Husson et al. (2024)](/sources/husson-2024.md), §3.1, Eq. (37) | not printed ($1/0.41$ from the coefficients, see below) | 5.0334 | Allmaras–Johnson composite law, nine printed constants | wall law of RANS and zonal DES on a lattice Boltzmann immersed boundary |
| [Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §3.2 | 0.41 | 5.5 | log layer quoted as $30<y^+<200$ | reference for $k$-$\tau$ RANS of pipe flow at $Re_\tau=1142$ |
| [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §IV.A, Figs. 12–13 | 0.41 | 5 | | reference profile for laminar-kinetic-energy transition RANS of the ERCOFTAC plates |
| [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md), §4.1, Fig. 9 | not printed | not printed | Spalding's law, as cited | reference for high-order flux-reconstruction RANS of the Wieghardt plate |
| [Huang et al. (2022b)](/sources/huang-2022-d.md), §2.4.3, Eq. (52) | not printed | not printed | Reichardt-type profile with damping lengths 11 and $1/0.33$ | manufactured boundary-layer profile for testing a high-order reconstruction |
| [Zhang et al. (2022)](/sources/zhang-2022-b.md), §3, Fig. 3 caption | 0.41 | 5.2 | | reference for transformed mean velocities of cooled-wall boundary-layer DNS at $M_\infty=0.5$–8 (below) |
| [Tonicello et al. (2022)](/sources/tonicello-2022.md), Fig. 5 | 0.41 | 5.25 | | reference for the van Driest velocity of the Mach 2.91 incoming boundary layer of a ramp DNS |
| [De Vanna et al. (2022)](/sources/devanna-2022.md), §2.2, Eq. (6); [van Noordt et al. (2022)](/sources/vannoordt-2022.md), §2.5, Eq. (35) | 0.41 | — | $A^+=17$ in semi-local $y^*$ | mixing length of a compressible ODE [equilibrium wall model](/methods/equilibrium-wall-model.md) |
| [Devenport & Lowe (2022)](/sources/devenport-2022.md), §2.1, Eq. (2.25) | "often" 0.41; 0.38–0.39 reported for zero-pressure-gradient boundary layers; 0.384 (Monkewitz et al., as cited) | 5.0; 4.17 with $\kappa=0.384$ | roughness function, Coles wake $\Pi\approx0.51$ (below) | review of incompressible boundary-layer physics |
| [Huang et al. (2022c)](/sources/huang-2022-c.md), §II C, Eqs. (14), (17) | 0.41 | 5.2 | Reichardt's law with $D=9.8$, $E=1/11$, $F=1/3$ (below) | algebraic wall model of a spectral/hp implicit LES in [Nektar++](/software/nektar-plus-plus.md) |
| [Zhang et al. (2022e)](/sources/zhang-2022-i.md), §II A, Eq. (3) | not printed | — | rough-wall form $\kappa^{-1}\ln(y/y_{0,\mathrm r})$, roughness length $y_{0,\mathrm r}$ (registry §11; $0.004$ mm in the matched wind tunnel) | wall stress of atmospheric LES over hills in [LESGO](/software/lesgo.md) |
| [Mo et al. (2023)](/sources/mo-2023.md), §II B, Eqs. (9)–(10) | 0.41 | 5.1 | sublayer $u^+=y^+$ for $y^+<6$ | reference for van Driest-transformed DNS of Mach 2.25, 2.9 and 7.25 flat plates |
| [Shi & Yan (2023)](/sources/shi-2023.md), Fig. 9 | 0.41 | 5.0 | | reference for the van Driest velocity of the Mach 2.9 incoming layer of a ramp implicit LES |
| [Gao et al. (2023)](/sources/gao-2023.md), §5.2, Fig. 18 | not printed | not printed | sublayer matched for $y^+\le5$, log law for $30\le y^+\le100$ | reference "derived from incompressible flow" for a Mach 2 DG implicit LES |
| [Yu et al. (2023)](/sources/yu-2023.md), §4.1, Eq. (4.1) | $1/2.55$ | 5 | reference-station buffer layer below $y^+=30$; cosine wake with a coefficient linear in $Re_\tau$ (below) | composite canonical profile in van Driest form after a shock interaction |
| [Maeyama & Kawai (2023)](/sources/maeyama-2023.md), §2.3, Eqs. (2.19)–(2.20) | 0.41 | — | $A^+=17$, $Pr_{t}=0.9$ in the wall model | mixing length of the compressible ODE [equilibrium wall model](/methods/equilibrium-wall-model.md) of a Mach 2.28 WMLES |
| [Zhang et al. (2022c)](/sources/zhang-2022-g.md), §II C, Fig. 6a | not printed | 5.7 (measured) | van Driest-transformed DNS profile on a cold wall | log-law intercept of the inflow layer of a Mach 6 ramp DNS, "higher than" incompressible, attributed to the wall temperature |
| [Hu et al. (2024)](/sources/hu-2024.md), §2; §4, Eq. (5) | 0.41 | 5.2 | quadratic branch below $y^+=23$; log layer placed "between about $y^+=30$ and $y/\delta=0.3$" | algebraic wall model of a WMLES grid-convergence study in CharLES |
| [Zhou & Bae (2024)](/sources/zhou-2024-b.md), §2.3, Fig. 3 | 0.41 | 5.2 | | check of the precursor flat-plate LES that feeds the [Gaussian bump](/benchmarks/gaussian-bump.md) inflow ($Re_\tau\approx620$) |
| [Kang & Lee (2024)](/sources/kang-2024.md), §III, Eq. (16), Fig. 4b | $1/2.44$ | 5.0 | "$\log$" printed without base | van Driest-transformed DNS profile of the Mach 2.9 incoming layer of a $24^\circ$ ramp, $Re_\theta=2400$ |
| [Tang et al. (2024)](/sources/tang-2024.md), §2.3, Fig. 11a | $1/2.44$ | 5.5 | linear law for $y^+<4$, log law over $y^+=30$–200 | van Driest-transformed DNS profile of the Mach 5 cold-wall ($T_w/T_r=0.5$) incoming layer of a $30^\circ$ ramp |
| [Zhang et al. (2024b)](/sources/zhang-2024-b.md), §3.1, Eq. (3.2), Fig. 5a | $1/2.44$ | 5.6–6.0 (measured), against 5.1 incompressible | intercept more sensitive than slope to the wall temperature | van Driest-transformed DNS of Mach 6 boundary layers at $T_w/T_r=0.50$, 0.75, 1.0 (below) |
| [Wang & Xu (2024)](/sources/wang-2024-h.md), §4.2, Fig. 8 | 0.41 | 5.2 | | target of the Griffin–Fu–Moin transformed profile of a reacting Mach 2.33 boundary layer |
| [Wei et al. (2023)](/sources/wei-2023.md), §III B, Fig. 10 legend | $1/2.5$ | 5.4 | | target of the van Driest-transformed velocity of a wall-resolved LES of a Mach 2.44 boundary layer |
| [Yan et al. (2024)](/sources/yan-2024.md), §II C, Eqs. (24)–(28) | 0.41 | — | Werner–Wengle power law $u^+=8.3\,(y^+)^{1/7}$ above $y^+=11.81$; van Driest damping $(1-e^{-y^+/19})^2$ in the mixing length; pressure-gradient correction in adverse gradient | explicit wall function of a wall-modelled diffused-interface immersed boundary (below) |
| [Wang et al. (2024d)](/sources/wang-2024-k.md), §II D, Eq. (22) | 0.41 | — | van Driest damping $(1-e^{-y^+/A^+})^2$ with $A^+=19.0$; Musker's profile as plotted reference (not in the reference list) | integrated equilibrium wall model of immersed-boundary lattice Boltzmann WMLES |
| [Xiao et al. (2025)](/sources/xiao-2025.md), §2.1, Eq. (10) | 0.41 | 5.2 | log law only, solved by Newton–Raphson | algebraic wall-stress model of [CaLES](/software/cales.md) at $h_{\mathrm{wm}}=0.1\delta$ |
| [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md), §2.4, Eqs. (19)–(23) | 0.42 | 5.2 | linear law below $y^+=11.0$, logarithmic above | wall function in the reconstruction of a sharp-interface curvilinear immersed boundary (below) |
| [De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.3, Eq. (27), Fig. 9 | not printed | 5.2 (Fig. 9 legend) | defect-law constant 0.2 for $y^+>30$ | reference for an implicit LES of channel flow at $Re_\tau=200$ (below) |
| [Guo & Wang (2025)](/sources/guo-2025.md), Eq. (18) | not printed | not printed | Spalding's law to the cubic term | OpenFOAM wall function of SST-based DDES (below) |
| [Wang et al. (2024c)](/sources/wang-2024-j.md), Fig. 1 legend | $1/2.44$ | 5.2 | printed "5.2 + 2.44 log($y^+$)", base not printed | reference for the van Driest velocity of LES and hybrid RANS/LES of a Mach 2 boundary layer |
| [Alberti et al. (2025b)](/sources/alberti-2025-c.md), captions of Figs. 1, 9, 11 | not printed | 5.5 | "compound law of the wall" $u^+=y^+$ and the log law | reference for entropy-stable DG implicit LES of channel flow at $Re_\tau=180$–590 |
| [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), §5.3 | 0.41 | 5 | sublayer $u^+=y^+$; the same letter $k$ is the thermal conductivity in their Eq. (8) and the von Kármán constant in Eqs. (10)–(12) | validation of isogeometric DG Spalart–Allmaras RANS of a flat plate at $M=0.2$, $Re=1.1\times10^7$ (below) |
| [Gao et al. (2025)](/sources/gao-2025.md), Figs. 5, 8, 14 | 0.41 | 5.2 | $A^+=17$ and $\kappa=0.41$ in the wall-model mixing length (Eq. 10) | reference for slip-velocity WMLES of channel ($Re_\tau=576$–5100) and flat-plate flow |
| [Launder & Spalding (1974)](/sources/launder-1974.md), §2.1, Eq. (2.1-12); §2.3-1; Fig. 3.3a | not printed | $\kappa^{-1}\ln E$, $E\approx9.0$ for a smooth wall, a function of roughness | van Driest $A^+=26.0$ (smooth wall) in the thermal wall function; Fig. 3.3a draws $u^+=5.5\log_{10}y^++5.45$ | log law written $u^+=\kappa^{-1}\ln(Ey^+)$; the standard [RANS wall functions](/methods/rans-wall-function.md) (below) |
| [Spalart & Allmaras (1992)](/sources/spalart-1992.md), App. (p. 21) | 0.41 | not printed | $c_{v1}=7.1$ chosen for the log-law intercept | log-layer calibration of the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) (below) |
| [Gao et al. (2025b)](/sources/gao-2025-b.md), §II C1, Eq. (17); App. A, Table III | not printed | 3.0333909 (see Qualifications) | Allmaras–Johnson–Spalart composite law, eight further constants; Shih et al.'s piecewise $f_1$ with its log branch $\kappa^{-1}\ln y^++C$ above $y^+=140$, $\kappa$ and $C$ not printed | explicitly inverted equilibrium wall model of a flux-reconstruction WMLES (below) |

Zhao et al. (2023a) attribute $\kappa=0.40$, $B=5.5$ to the channel DNS of
Kim et al. (1987), as they cite it; Wang et al. (2023b) give the same values
with the same wording. Zhao et al. (2021, §IV) use the same values and the same
reverse procedure in an earlier paper of the same group. Zhao et al. (2023a, §5.2, Eqs. 25–26) use the law in the reverse
direction: with the centreline velocity $U_c=1$ and the target centreline
value $y_c^+=Re_\tau=180$, they set $U_c^+=2.5\ln y_c^++5.5$,
$u_\tau=U_c/U_c^+$ and the viscosity $\mu=\rho u_\tau\delta/Re_\tau$ ($\delta$ the
channel half-height, the source's $H$; $U_c$, $U_c^+$, $y_c^+$ page-local); the realized $Re_\tau$ then follows
from the simulation. Dang et al.'s slope $1/2.44$ is $\kappa\approx0.410$, and Cai et al.'s $E=11.27$
corresponds to $B=\kappa^{-1}\ln E\approx2.42/\kappa$, about 5.9 for
$\kappa=0.41$ *(compiler check, not in the sources)*.

Griffin et al. (2023, §3) test Reynolds-number-dependent constants fitted to
the incompressible channel DNS of Lee & Moser (as they cite it): at
$Re_\tau=\{182,543,1000,1990,5190\}$, $\kappa=\{0.400,0.408,0.400,0.391,0.391\}$
and $A^+=\{18.2,17.4,17.0,16.5,16.5\}$. The fitted values improve their
compressible wall model only modestly at $Re_\tau^*=190$ and not at all at
$Re_\tau^*=590$, so they keep $\kappa=0.41$, $A^+=17$. Gillyns et al. (2022,
§3) likewise note that more recent values after Lee & Moser are
$\kappa\simeq0.383$, $B\simeq4.25$, but keep 0.38 and 4.1; the effect of the
choice on $u_\tau$ is not assessed.

Launder & Spalding (1974) print no value of $\kappa$; the reference line of
their Fig. 3.3a, $u^+=5.5\log_{10}y^++5.45$, corresponds to $\kappa=\ln10/5.5=0.419$
and $B=5.45$, and with that $\kappa$ their smooth-wall $E\approx9.0$ gives
$B=\kappa^{-1}\ln E\approx5.25$ *(compiler check, not in the sources)*.

Vadrot et al. (2023a, §II.B.3) note that empirical values of $\kappa$ range
over 0.36–0.44 (as they cite it), which matters for their learned wall model
because its first state is built from the chosen $\kappa=0.4$ (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).
Mozaffari et al. (2024) write the log law as $u^+=\kappa^{-1}\ln(Ey^+)$, as
Cai et al. (2022) do, but with $E\approx7.9$ against 11.27 (see
Contradictions); with $\kappa=0.41$ for both (Cai et al. print no value of
$\kappa$) these correspond to $B\approx5.0$ and $B\approx5.9$
*(compiler check, not in the sources)*.

[Nuca et al. (2025)](/sources/nuca-2025.md) (§III) state that $\kappa$ and
$B$ are subject to low-Reynolds-number effects and that their high-Reynolds-number
values are "not settled upon" (as they cite it), so an approximation of a
wall model must keep them as inputs rather than freeze them; their two fixed
sets and their fitting ranges are in the table. Their high-Re intercept,
4.21, and the 4.2 of Mukha et al. (2025) are both taken from Yamamoto &
Tsuji as cited, and differ only in the printed rounding. Husson et al.
(2024, §3.1) print no $\kappa$ with their composite law; its two
logarithmic terms give the slope $2(c_1-c_2)=2.439=1/0.410$ and, with the
argument order discussed under Qualifications, the intercept $5.0334$
equals the printed additive constant ($c_1$, $c_2$ the law's constants,
page-local) *(compiler check, not in the sources)*.

**Universality in a boundary-layer review.** [Devenport & Lowe (2022)](/sources/devenport-2022.md)
(§2.1, Eqs. 2.22–2.26) call Rotta's derivation of the log law, independence
of viscosity in the overlap of inner and outer regions, "the most general",
since it assumes nothing about the outer flow, and state that the
universality of $\kappa$ is open: values of 0.38–0.39 are reported for
zero-pressure-gradient boundary layers, and the review classes pipes and
channels as favourable-pressure-gradient flows. The practical consequence is
small at moderate $y^+$: with Monkewitz et al.'s $\kappa=0.384$, $B=4.17$,
as cited, $u^+$ differs from that with $\kappa=0.41$, $B=5.0$ by only 0.4 %
and 1.4 % at $y^+=100$ and 1000 (16.16 against 16.23 and 22.16 against 21.85
*(compiler check, not in the sources)*). The review writes the log law
equivalently as $u^+=\kappa^{-1}\ln(y/k_o)$ with the hydrodynamic roughness
length $k_o=\nu e^{-\kappa B}/u_\tau$, $k_o^+\approx0.129$ for $\kappa=0.41$,
$B=5.0$ (page-local $k_o$; $e^{-0.41\times5}=0.129$ *(compiler check, not in
the sources)*), and places the inner region in the bottom 10–20 % of the
layer.

**Intercepts of hypersonic cold-wall layers.** [Zhang et al. (2024b)](/sources/zhang-2024-b.md)
(§3.1, Fig. 5a) find that the van Driest-transformed DNS profiles of Mach 6
boundary layers keep the slope $2.44$ but have intercepts 5.6–6.0, above the
incompressible 5.1; the intercept is more sensitive than the slope to the
wall temperature, colder walls leave $u^+_{\mathrm{VD}}=y^+$ closer to the
wall, and they conclude that the transformation "is more applicable to the
adiabatic wall". They set this beside intercepts of 5.2–6.0 at Mach 5
(Duan et al. 2010) and 5.9 at Mach 7.2 (Priebe & Martín 2021), as they cite
them, and attribute the high values to the transformation's validity only
at moderate Mach number. The Mach 5 cold-wall DNS of [Tang et al. (2024)](/sources/tang-2024.md)
(§2.3) uses the reference intercept 5.5 and reports a deviation up to 3 %
from Duan et al. (2010) only in the wake (see
[compressible velocity transformation](/definitions/compressible-velocity-transformation.md)).

Aiello et al. (2026, §4.1) attribute their large fitted intercept,
$B=6.0$, to the low transformed friction Reynolds number of their DNS
($Re_\tau^*=160$–190), consistent, they state, with low-Reynolds-number
incompressible flow and earlier supersonic channel DNS (see
[compressible velocity transformation](/definitions/compressible-velocity-transformation.md)).
Lederer et al. (2026, §4.2) take $\kappa=0.41$, $B=5.2$ as constants fitted
for mild adverse pressure gradients and compare the profiles of their
implicit LES in the turbulent part of the airfoil boundary layer, where all
runs follow $u^+=y^+$ for $y^+<5$ and differ from one another above
$y^+=10$ (Fig. 7; see
[high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md)).

How much the constants matter is quantified by Lozano-Durán et al. (2022,
§IV.C, Eq. 12): a 10 % error in $\kappa$ or in $B$ produces about 6 % or 3 %
error in $u_\tau$, less than a 10 % error in the LES velocity at the matching
point; their fuselage WMLES errors saturate at about 2 %, which they attribute
to a 3 % deviation in $\kappa$ (§V.C) (details on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page). Vadrot et
al. (2023a, §III.B) quote a comparable sensitivity, after Yang et al. (2019)
as they cite it: a 2.5 % uncertainty in $\kappa$ gives about a 5 % error in
the predicted wall stress, that is about one to two wall units of
[log-layer mismatch](/definitions/log-layer-mismatch.md).

## Composite profiles across the buffer layer

A wall model sampled in the buffer layer needs a single smooth $f(y^+)$.

- **Piecewise algebraic profile** (Lozano-Durán et al. 2022, Eq. 1):
  $u^+=y^++a_1(y^+)^2$ for $y^+<23$ and the log law otherwise, with $a_1$
  fixed by $C^1$ continuity at $y^+=23$ (value not printed).
- **Smooth fit of the full-equilibrium solution** (Fowler et al. 2022, Eqs.
  C1–C2), fitted to the numerical solution of the mixing-length equilibrium
  ODE with van Driest damping:

  $$f(y^+)=\left[\frac1\kappa\ln(\kappa_2+y^+)+B\right]\left[1+\left(\frac{y^+}{\kappa_1}\right)^{-\beta}\right]^{-1/\beta},\qquad \kappa_1=\frac1\kappa\ln\kappa_2+B,$$

  with $\kappa=0.4$, $B=4.95$, $\kappa_2=9.753$, $\beta=1.903$ (here $\beta$
  is the fit exponent, page-local). The choice of $\kappa_1$ makes
  $f\to y^+$ in the viscous sublayer. The fit error is below 1 % for $y^+>5$
  and below 2.25 % for $0\le y^+\le5$. Fowler et al. reject Reichardt's (1951)
  profile, as they cite it, because its error exceeds 3 % near $y^+\sim10$.
- **Reichardt's profile** (Gillyns et al. 2022, Eq. 3, as in Frère et al.
  2017, as they cite it):

  $$u^+=\frac1\kappa\ln(1+\kappa y^+)+\left(B-\frac1\kappa\ln\kappa\right)\left(1-e^{-y^+/11}-\frac{y^+}{11}e^{-y^+/3}\right),$$

  with $\kappa=0.38$, $B=4.1$, inverted for $u_\tau$ in their equilibrium
  wall model (the source writes $C$ for $B$). Fowler et al. (2022) reject this
  profile for its error near $y^+\sim10$ (above); Gillyns et al. sample it at
  $y^+\ge63$, where the choice is not tested against an alternative.
  Nuca et al. (2025, §III, Eqs. 3, 6) print the same law with an additive
  constant $C$ and damping lengths $B_1=11$, $B_2=3$ (page-local), and derive
  $C=B-\kappa^{-1}\ln\kappa$ from the limit $y^+\to\infty$, which is the
  coefficient Gillyns et al. write; dropping the damping terms leaves
  $\kappa^{-1}\ln(1+\kappa y^+)$, the profile of the undamped equilibrium ODE
  (below). With $\kappa=0.4$, $B=5.5$ the relation gives $C=7.79$, the
  printed classical 7.8, and with the high-Re set $\kappa=0.387$, $B=4.21$ it
  gives $C=6.66$ *(compiler check, not in the sources)*.
  Huang et al. (2022c, §II C, Eq. 17) print the law with the damping
  rates as inverse lengths, $u^+=\kappa^{-1}\ln(1+\kappa y^+)+D\big(1-e^{-Ey^+}-Ey^+e^{-Fy^+}\big)$,
  with $D=9.8$, $E=1/11$, $F=1/3$, $\kappa=0.41$ (page-local $D$, $E$,
  $F$; $D$ is the $C$ above), as a profile that connects the linear, buffer
  and log regions, and use it as an alternative to their log law with
  $B=5.2$ in a wall model sampled at $0.224\delta$ at $Re_\tau=550$; they find only slight
  differences and explain them by the matching point lying in the log
  region "where both of the two laws coincide" (§III C, Fig. 7). With the
  printed constants the two laws do not coincide there (see Qualifications).
- **Blended profile with an explicit inverse** (Cai et al. 2022, §II.C.1,
  Eqs. 24–26, after the authors' earlier work as they cite it). The forward
  profile blends the two asymptotes with hyperbolic tangents,

  $$u^+=\left[1-\tanh\frac{y^+}{10.71}\right]^{1.526}y^++\left[\tanh\frac{y^+}{10.71}\right]^{1.526}\frac1\kappa\ln(Ey^+),\qquad E=11.27,$$

  and a separately fitted inverse gives $y^+$ directly from the local Reynolds
  number $Re_y=U y/\nu$ (registry §11; $U$ the wall-tangential velocity at
  distance $y$, page-local),

  $$y^+=\left[1-\tanh\frac{Re_y}{180.8}\right]^{0.789}Re_y^{1/2}+\left[\tanh\frac{Re_y}{180.8}\right]^{0.789}\frac{e^{W(\kappa ERe_y)}}{E},$$

  with $W$ the Lambert function, $W(x)=\ln\big(x/W(x)\big)$, "expanded
  explicitly into series" (series not printed), so that
  $u_\tau=y^+\nu/y$ needs no Newton iteration. Each branch of the inverse is
  the exact inverse of the matching branch of the forward profile — the
  viscous branch from $Re_y=(y^+)^2$, the log branch from
  $\kappa ERe_y=Ey^+\ln(Ey^+)$, i.e. $\ln(Ey^+)=W(\kappa ERe_y)$ — while the
  two blending functions differ, so the pair is consistent only
  asymptotically; its buffer-layer accuracy is not shown in the source
  *(compiler check, not in the sources)*. See the
  [equilibrium wall model](/methods/equilibrium-wall-model.md).
- **The same explicit inverse with other constants** (Mozaffari et al.
  2024, §2.2, Eqs. 9–15, after Cai & Sagaut as they cite it): the viscous
  branch $y^+=\sqrt{Re_y}$, the log branch $y^+=E^{-1}e^{W(\kappa ERe_y)}$ and
  the unified inverse

  $$y^+(Re_y)=\left[1-\tanh\frac{Re_y}{s}\right]^pRe_y^{1/2}+\left[\tanh\frac{Re_y}{s}\right]^p\frac{e^{W(\kappa ERe_y)}}{E},\qquad u^+=\frac{Re_y}{y^+},$$

  with $s=86.58$, $p=0.7894$, $\kappa\approx0.41$, $E\approx7.9$ ($s$, $p$
  page-local); the exponent $p$ applies to the bracketed blending functions,
  as in the form of Cai et al. (2022) above (manuscript p. 5, Eq. 15, checked
  visually). No pressure-gradient term. See Contradictions for the
  comparison with Cai et al. (2022).
- **An explicit forward law $u^+(Re_y)$, re-fitted, with buffer-layer
  corrections** (Nuca et al. 2025, §III–IV, Eqs. 5, 9–10, 24). Nuca et al.
  write "model 2" of Cai & Sagaut (2021), as they cite it, directly for
  $u^+$,

  $$u^+_{\mathrm{CS}}=\left(e^{-Re_y/s}\right)^p\sqrt{Re_y}+\frac{\left(1-e^{-Re_y/s}\right)^p}{\kappa}\,W\!\left(\kappa e^{\kappa B}Re_y\right),$$

  with exponential, not hyperbolic-tangent, blending functions, and treat
  $p$ and $s$ as free coefficients to be optimized rather than as Cai &
  Sagaut's values (for $\kappa=0.41$, $B=5.525$, Fig. 3 uses $p=1.2411$,
  $s=117.3629$; the optimization bounds of Table III span $p=1.22$–1.29,
  $s=76$–378). The log branch is the same as in the inverses above: from
  $Re_y=u^+y^+$ and $u^+=\kappa^{-1}\ln y^++B$, $\kappa u^+=W(\kappa e^{\kappa B}Re_y)$,
  and with $E=e^{\kappa B}$ this is $\ln(Ey^+)=W(\kappa ERe_y)$ of Cai et
  al. (2022) *(compiler check, not in the sources)*. Their premise is that
  Spalding's law, Reichardt's law, the van Driest equilibrium ODE and this
  explicit law coincide in the linear and logarithmic regions once their
  constants match, so only a buffer-layer perturbation $\Delta u^+$, a sum of
  one to three Gaussian bumps in $\log_{10}Re_y$, has to be fitted to turn
  the explicit law into an approximation of any of the three (§IV, Fig. 3).
  The fits, their printed accuracy (below 1 % for coefficients linear in
  $\kappa$ and in $B$, $C$ or $A^+$; below 0.05 % for fixed constants) and
  the checks of the printed coefficients are on the
  [equilibrium wall model](/methods/equilibrium-wall-model.md) page.
- **Musker's law** (Constant et al. 2024, §3.2, Eq. 6, after Musker as
  cited): an equilibrium profile fitting viscous, buffer and log layers,
  $u_A=u_\tau f(y_A^+)$ at an immersed-boundary target point $A$, with
  $u_\tau$ from Newton–Raphson at the image point and assumed constant along
  the wall normal; the formula is not printed. Their Fig. 7 compares it with
  Spalding's law and a body-fitted flat-plate RANS profile. The eddy
  viscosity at the target points is $\nu_t=\kappa u_\tau y\,[1-e^{-y^+/19}]$
  with $\kappa=0.41$ (Eq. 8), stated "valid in the log layer and down to the
  wall", and inverted for the Spalart–Allmaras variable $\tilde\nu$; the
  damping enters to the first power and with the constant 19, unlike the
  squared $A^+=17$ form of Griffin et al. (2023).
- **Linear/log switch** (Lewis et al. 2023, §3.2.2, after Schmitt et
  al. as cited): a linear law $u^+=y^+$ for $y^+<11$ and a logarithmic law
  otherwise; the constants are not printed.
- **Spalding's law** is the algebraic wall model of Blind et al. (2023,
  §3.3), solved by Newton's method in every Runge–Kutta stage; the formula
  and its constants are not printed. Mukha et al. (2025, §II.C.1) use it in
  the same role in a continuous spectral-element code and, without printing
  the formula, measure its accuracy against reference profiles (App. A,
  Figs. 18–21). In channel flow at $Re_\tau\approx8000$, with the constants
  $\kappa=0.387$, $B=4.2$ taken from the same DNS, the law reproduces the
  DNS velocity in the log region within 0.2 %, and the wall stress it
  returns from the exact DNS velocity is within $\pm0.2$ % for matching
  heights $0.05\le h_{\mathrm{wm}}/\delta\lesssim0.25$ ($-0.04$ % at
  $h_{\mathrm{wm}}=0.2\delta$ in §III.B.3, "about 0.05 %" in App. A). With
  $\kappa=0.41$ and reference flat-plate profiles the stress error
  is about $\pm1$ %, an order of magnitude larger; the law reaches its
  logarithmic limit only near $y^+\approx150$, which at low Reynolds numbers
  lies near the wake region, and where the error crosses zero depends on
  whether wall-resolved LES or DNS supplies the reference profile (App. A,
  Figs. 20–21). Constant et al. (2024, Fig. 7) compare Spalding's law with
  Musker's law (above). Ghidoni et al. (2026, §3.3, Eq. 12) print the law,
  up to the quadratic term, as
  $y^+=u^++e^{-\kappa B}\big(e^{\kappa u^+}-1-\kappa u^+-(\kappa u^+)^2/2!\big)$
  with $\kappa\sim0.41$, $B=5$, and use it as the implicit reference against
  which their explicit power law (next item) is timed. Nuca et al. (2025,
  §III, Eq. 2) print it with the cubic term as well,

  $$y^+=u^++e^{-\kappa B}\left(e^{\kappa u^+}-1-\kappa u^+-\tfrac12(\kappa u^+)^2-\tfrac16(\kappa u^+)^3\right),$$

  explicit in $y^+$, so that obtaining $\tau_w$ requires Newton iteration;
  they report that this iteration "would often sporadically diverge" in
  complex-flow WMLES (see [equilibrium wall model](/methods/equilibrium-wall-model.md)).
  [Guo & Wang (2025)](/sources/guo-2025.md) (Eq. 18) print the same
  cubic-term form as the law behind the OpenFOAM wall function
  `nutUSpaldingWallFunction` of their SST-based DDES, with $\kappa$ and $B$
  not printed (see [RANS wall function](/methods/rans-wall-function.md)).
- **The Spalart–Allmaras analytical law** (Husson et al. 2024, §3.1, Eq. 37,
  after Allmaras & Johnson as cited), a composite of two logarithms and two
  arctangents,

  $$u^+=B+c_1\ln\!\big[(y^++a_1)^2+b_1^2\big]-c_2\ln\!\big[(y^++a_2)^2+b_2^2\big]-c_3\,\theta_1-c_4\,\theta_2,$$

  with $\theta_k$ an arctangent of $(y^++a_k)/b_k$ (see Qualifications for
  the printed argument order) and nine constants printed to sixteen digits
  ($B=5.0333908790505579$, $a_1=8.148221580024245$,
  $a_2=-6.9287093849022945$, $b_1=7.4600876082527945$,
  $b_2=7.468145790401841$, $c_1=2.5496773539754747$,
  $c_2=1.3301651588535228$, $c_3=3.599459109332379$,
  $c_4=3.6397531868684494$; $a_k$, $b_k$, $c_k$, $\theta_k$ page-local).
  The authors choose it because its buffer layer is consistent with the
  [Spalart–Allmaras model](/methods/spalart-allmaras-model.md); below a
  cut-off height they replace it by its tangent line (Tamaki et al., as
  cited), so that the wall-normal gradient is constant and resolvable on a
  coarse mesh. Formulas of the linearization and of its eddy viscosity are
  on the [RANS wall function](/methods/rans-wall-function.md) page.
  [Gao et al. (2025b)](/sources/gao-2025-b.md) (§II C1, Eq. 17) print the
  same law, attributed to Allmaras, Johnson & Spalart (2012) as cited,
  with the arctangents written $\tan^{-1}(y^++a_k,b_k)$ and the constants
  to eight digits: $a_1$, $a_2$, $b_1$, $b_2$, $c_1$–$c_4$ agree with
  Husson et al.'s to the printed digits, while the additive constant is
  printed $B=3.0333909$ against Husson et al.'s $5.0333908790505579$ (see
  Qualifications). Gao et al. do not invert the law iteratively: they
  write $Re_y=y^+u^+=F(y^+)$ and fit the inverse $y^+=F^{-1}(Re_y)$ in five
  explicit branches (formulas on the
  [equilibrium wall model](/methods/equilibrium-wall-model.md) page).
- **Power law with a closed-form inverse** (Ghidoni et al. 2026, §3.3,
  Eqs. 13–15, after Wilhelm et al. as cited): $u^+=y^+$ for
  $y^+\le y^+_{\mathrm{vs}}=11.81$ and $u^+=8.3\,(y^+)^{1/7}$ above, which is continuous
  at $y^+_{\mathrm{vs}}$ ($8.3\times11.81^{1/7}=11.81$ *(compiler check, not in the
  sources)*). Each branch inverts explicitly for $u_\tau$ given the velocity
  at a distance $y$, and the two friction velocities are blended as
  $(u_{\tau,\mathrm{vis}}^4+u_{\tau,\log}^4)^{1/4}$ after Menter et al. (as
  cited), so no Newton iteration is needed; the law assumes zero pressure
  gradient. Formulas, cost and accuracy are on the
  [RANS wall function](/methods/rans-wall-function.md) page.
  The same Werner–Wengle constants ($8.3$, $1/7$, $y^+_{\mathrm{vs}}=11.81$) appear in
  the LES wall model of [Yan et al. (2024)](/sources/yan-2024.md) (§II C,
  Eqs. 26–27), inverted explicitly for $u_\tau$ branch by branch without
  blending, and extended by an adverse-pressure-gradient correction (see
  the [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).
  Yan et al. state that the power law cannot supply the velocity gradient
  at the probe, because its derivative is discontinuous at $y^+_{\mathrm{vs}}$, and take
  the gradient from a boundary-layer equation instead (see
  [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).
- **Linear/log switch inside an immersed-boundary reconstruction**
  ([Akbarzadeh & Borazjani 2025](/sources/akbarzadeh-2025.md), §2.4,
  Eqs. 19–24). The friction velocity is found iteratively from the log law
  ($\kappa=0.42$, $B=5.2$) at a fluid point $c$ on the wall normal, and the
  tangential velocity at the boundary node $b$ between wall and $c$ follows
  from $u^+_b=y^+_b$ for $y^+_b<11.0$ and the log law above. The second
  branch of Eq. (23) is printed with $y^+_c$ in place of $y^+_b$ (see
  Qualifications). The authors state that the law "works properly when the
  flow is attached and the boundary layer is turbulent", not in separated
  or transitional flow (§2.4).
- **Mixing length with van Driest damping**, the differential form behind
  the fit of Fowler et al.: the eddy viscosity is $\nu_t=\kappa y\,u_\tau(1-e^{-y^+/A^+})^2$,
  and integrating the constant-stress equation gives $f$ (Griffin et al.
  2023, Eq. 1.2, in its incompressible form; see Qualifications for the
  printed form). Rickard & Kasbaoui (2026, §4.1, Eq. 4.1) write the van
  Driest profile in closed integral form,

  $$u^+(y^+)=\int_0^{y^+}\frac{2\,d\eta'}{1+\sqrt{1+4\big[\kappa\eta'\big(1-e^{-\eta'/A^+}\big)\big]^2}},\qquad\kappa=0.41,\ A^+=26$$

  ($\eta'$ the integration variable, page-local). The integrand is the
  root of the constant-stress balance $(1+\nu_t^+)\,du^+/dy^+=1$ with the
  mixing length $l^+=\kappa y^+(1-e^{-y^+/A^+})$ and
  $\nu_t=l^2\lvert\partial u/\partial y\rvert$, the form with the damping
  inside the squared length; it is not the profile of Griffin et al.'s
  eddy viscosity, which is linear in $u_\tau$ and gives
  $du^+/dy^+=1/\big(1+\kappa y^+(1-e^{-y^+/A^+})^2\big)$ *(compiler check,
  not in the sources)*. Nuca et al. (2025, §III, Eq. 4) integrate exactly
  that equilibrium ODE, $u^+=\int_0^{y^+}d\eta'/\big(1+\kappa\eta'(1-e^{-\eta'/A^+})^2\big)$,
  with $\kappa=0.41$, $A^+=17$ after Kawai & Larsson (as cited; Cabot used
  $A^+=19$, as they cite it), and note that without damping it integrates to
  $\kappa^{-1}\ln(1+\kappa y^+)$, while with damping no closed form links the
  intercept $B$ to $A^+$, so $B$ is evaluated pointwise as
  $u^+(\hat y^+)-\kappa^{-1}\ln\hat y^+$ at some $\hat y^+\gg30$ (Eqs. 1, 8;
  $\hat y^+$ page-local). Elzaabalawy et al. (2023,
  §5.2.1, Eqs. 93–94) use the mixing length $l=0.39\,y\,(1-e^{-y^+/26})$ with
  $\nu_t=l^2\lvert\partial u/\partial y\rvert$ ($l$ page-local) as an
  algebraic RANS model for verifying a high-order solver: without the
  singular wall value of $\omega$, their mean velocity converges at the
  optimal order (Fig. 16).

## Generalizations carried by the sources

- **Extent of the constant-stress layer.** The log law follows from a
  layer of constant total stress, and [Bose & Park (2018)](/sources/bose-2018.md)
  (§2.1, Fig. 3) state how far it extends: experimental and numerical data
  show a constant-stress layer for $y^+\lesssim100$ that then departs
  linearly in $y/\delta$, close to the fit $\tau/\tau_w=1-0.6\,y/\delta$ of
  Spalart (1988), as cited, with $0.95<\tau/\tau_w<1$ for $y/\delta\lesssim0.03$
  at high enough Reynolds number (zero-pressure-gradient data of DeGraaff &
  Eaton and Klebanoff at $Re_\theta=5200$–31 000, as cited). They read the
  inner-layer solution of a wall model as an ensemble of many eddies, valid
  only for cells larger than a minimal channel (see
  [equilibrium wall model](/methods/equilibrium-wall-model.md)), and cite
  rough-wall forms with a downward shift $\Delta U^+=f(k^+)$ of the log law
  ($k^+$ the roughness height in wall units, page-local; §4.1).
- **Rough walls.** Devenport & Lowe (2022, §2.1, Eqs. 2.27–2.29) write
  the rough-wall law as $u^+=\kappa^{-1}\ln(y/k_s)+B+3.5=\kappa^{-1}\ln y^++B-\Delta U^+$
  with $\Delta U^+=\kappa^{-1}\ln k_s^+-3.5$ ($k_s$ the equivalent
  sand-grain roughness, registry §11; this is the downward shift that Bose &
  Park cite above) and $k_o\approx0.031k_s$ in the fully rough regime,
  commonly $k_s^+\gtrsim50$; for dense roughness the origin of $y$ is
  Jackson's level at which the mean drag acts. Outside a roughness layer of
  about five roughness heights, rough-wall turbulence agrees with smooth-wall
  turbulence scaled on $u_\tau$ (Townsend's wall similarity), seen for
  $y/\delta\gtrsim0.15$ when $\delta/k_g\gtrsim50$ ($k_g$ the geometric
  height), though Mehdi et al., as cited, argue it is unlikely below the
  height of maximum shear stress, of order $\sqrt{Re_\tau}$ in wall units
  (§2.2). Atmospheric LES uses the fully rough form with a roughness length
  in the wall stress: [Zhang et al. (2022e)](/sources/zhang-2022-i.md)
  (§II A, Eq. 3) impose
  $\tau_w=\rho\big(\kappa/\ln(y/y_{0,\mathrm r})\big)^2U^2$ with a test-filtered
  velocity magnitude $U$ at the first grid point (details on the
  [equilibrium wall model](/methods/equilibrium-wall-model.md) page).
- **Outer layer: wake and defect laws in a review.** Devenport & Lowe
  (2022, §2.1, Eqs. 2.30–2.34) give the von Kármán defect law
  $(U_e-\langle u\rangle)/u_\tau=g(y/\delta)$, Coles' composite
  $u^+=\kappa^{-1}\ln(y/k_o)+(\Pi/\kappa)W(y/\delta)$ with
  $W=2\sin^2(\pi y/2\delta)$ and a wake factor $\Pi$ typically 0.51, believed
  to reach an asymptote at high Reynolds number, and the Zagarola–Smits
  outer velocity scale $U_e\delta^*/\delta$, accurate in high-$Re$ pipes and
  collapsing smooth- and rough-wall and mildly pressure-gradient layers
  (page-local $U_e$, $g$, $W$, $\Pi$, the last not the SGS flux). An adverse
  gradient lowers the log region and a favourable one raises it (see the
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).
- **A composite canonical profile as a reference after a shock.**
  [Yu et al. (2023)](/sources/yu-2023.md) (§4.1, Eq. 4.1) need a canonical
  mean velocity to measure the defect left by a separated oblique-shock
  interaction at Mach 2.28. In van Driest form (see
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md))
  they take the reference station's own profile below $y^+=30$,
  $2.55\ln y^++5$ above it up to $y/\delta=0.3$, the same log law plus
  $2.55\,b_{\mathrm{wk}}\big(\cos(0.3\pi)-\cos(\pi y/\delta)\big)$ for
  $0.3<y/\delta<1$, and the constant edge value
  $2.55\ln\delta^++5+2.55\,b_{\mathrm{wk}}(\cos(0.3\pi)+1)$ beyond. Here
  $b_{\mathrm{wk}}$ (registry §11, the source's $\beta$) is a wake coefficient
  fitted linearly in $Re_\tau$, $b_{\mathrm{wk}}=0.0005Re_\tau-0.411$, from the
  reference station and the last station, where recovery is postulated.
  The log law is called "standard" after Pirozzoli & Bernardini (2011, as
  cited). The four branches are continuous at $y/\delta=0.3$ and 1, and the
  slope 2.55 corresponds to $\kappa\approx0.392$ *(compiler check, not in
  the sources)*. The log-law intercept serves as a recovery indicator: just
  downstream of the interaction it is "much lower than 5.0" with a raised
  wake and an inflection near $y/\delta\approx0.3$, and it returns to 5.0
  at $13.3\delta_r$ downstream of impingement (§3, Fig. 5). The defect is
  used in the [skin-friction decomposition](/definitions/skin-friction-decomposition.md).
- **Defect law as an LES check.** [De Cosmo et al. (2025)](/sources/decosmo-2025.md)
  (§3.3, Eq. 27, Figs. 8–9) validate an implicit LES of channel flow at
  $Re_\tau=200$ with the velocity-defect law
  $(u(h)-\langle u\rangle)/u_\tau=-\kappa^{-1}\log(y/h)+B_1$, $B_1=0.2$,
  "expected to follow a log-law for $y^+>30$" ($h$ the channel
  half-height, $u(h)$ the centreline velocity, $B_1$ page-local; $\kappa$
  not printed): the computed defect agrees with the DNS and departs from
  the law at low $y/h$, and the inner profile, compared with the log law
  with $B=5.2$, is over-predicted by 2 % at $y^+=100$, which the authors
  relate to excess dissipation and an under-predicted wall stress (see
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).
- **Magnetohydrodynamic channels.** [Fang et al. (2025)](/sources/fang-2025.md)
  (§3.4, Figs. 12–13) find the mean velocity of their channel DNS at
  $Re_\tau=150$ in agreement with the law of the wall without a magnetic
  field, and report that a wall-normal magnetic field lifts the log layer,
  "as in drag-reducing flows", increasingly with the Hartmann number, until
  the flow relaminarizes at Hartmann number 8; their log layer lies slightly
  above the reference DNS data in wall units and agrees in bulk scaling
  (see [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).
- **Three-dimensional boundary layers.** The review's §5.3 (Eq. 5.11)
  presents van den Berg's three-dimensional law of the wall, with
  pressure-gradient and wall-stress-rotation terms added to both velocity
  components, as "perhaps the leading theoretical development", while noting
  that it relies on alignment of stress and strain, which three-dimensional
  boundary layers violate (see
  [turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).
- **The log law as a basis function.** [Lv et al. (2021)](/sources/lv-2021.md)
  (§II A, Eqs. 3–6) put the law of the wall into the discretization: in the
  wall-adjacent cell of a high-order LES one monomial of the reconstruction
  basis is replaced by $\kappa^{-1}\ln\big((y+y_0)/y_0\big)$ ($y_0$ a viscous
  or roughness length, page-local), whose coefficient is identified with
  $u_\tau$; the remaining polynomial terms carry the departures from the law
  (details on [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).
  Their WMLES recovers $\kappa^{-1}\ln y^++B$ ($\kappa=0.41$, $B=5.2$) in
  channel flow at $Re_\tau=180$, 2000 and 50 000 (§IV B 1, Fig. 11).
- **Rotating channels.** The supervised wall model HYK19 analysed by Vadrot
  et al. (2023b, §II.B.2, Eq. 5) learns the departure of the LES velocity from
  an empirical profile $g(y^+,l^+_\Omega)$ that equals $\kappa^{-1}\ln y^+$
  without rotation and switches to a linear-plus-log form beyond
  $y^+=l^+_\Omega/\kappa$, with $l_\Omega=u_\tau/(2\Omega_{\mathrm{rot}})$ the
  rotation length (page-local). Without rotation the network therefore
  predicts a wall-distance-dependent intercept in place of $B$.
- **Compressible flows.** With variable density and viscosity the profile
  holds only after a [compressible velocity transformation](/definitions/compressible-velocity-transformation.md);
  Griffin et al. (2023, §3) report, citing Yang & Lv, that the classical van
  Driest damping is consistent with the van Driest transformation and its
  semi-local version (written in $y^*$) with the Trettel–Larsson one.
  [Chen et al. (2024)](/sources/chen-2024.md) (§3.1, Eqs. 3.1–3.2) derive
  the same equivalence for the inner layer of the algebraic
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md): a mixing length
  $\kappa y[1-e^{-y^*/A^+}]$ ($\kappa=0.40$) with semi-local damping is the
  mixing-length relation written for the Trettel–Larsson velocity. Their
  DNS diagnostic of the semi-local eddy viscosity, compared with the
  Johnson–King inner scaling $\kappa y^*[1-e^{-y^*/17}]^2$, collapses up to
  the buffer layer but falls below it in the log region of diabatic
  boundary layers, and follows it more closely with the Griffin–Fu–Moin
  transformation (§3.1, Fig. 3). [Zhang et al. (2022)](/sources/zhang-2022-b.md)
  (§3, Fig. 3) show the same dependence on the transformation in DNS of
  zero-pressure-gradient boundary layers at $M_\infty=0.5$, 2 and 8 with
  $T_w/T_r$ down to 0.25: of the van Driest, Trettel–Larsson,
  quasi-equilibrium and total-stress-based transformations, only the last
  brings the cooled and adiabatic profiles onto $u^+=y^+$ and the log law
  with $\kappa=0.41$, $B=5.2$ together.
- **Outer (defect) layer.** Chen et al. (2024, §3.2, Eqs. 3.9–3.12) use
  Clauser's defect law $u_e^+-u^+=g(y/\Delta_{RC})$ with the Rotta–Clauser
  thickness $\Delta_{RC}=u_e^+\delta^*$ (page-local $u_e^+$, $g$,
  $\Delta_{RC}$); for the incompressible zero-pressure-gradient layer they
  take, from Monkewitz et al. (2007) as they cite it, the outer maximum 5.55
  of $y\,\partial u^+/\partial y$ at $y/\Delta_{RC}=0.155$. For compressible
  layers the van Driest-transformed defect collapses better, with outer
  velocity scale $u_\tau/\sqrt{\langle\rho\rangle/\rho_w}$, after Smits &
  Dussauge as they cite it (Eq. 3.12, Fig. 5); this is the basis of their
  outer-layer correction (see
  [compressible velocity transformation](/definitions/compressible-velocity-transformation.md)).
- **Adverse pressure gradients.** [Knopp (2022)](/sources/knopp-2022.md)
  finds the log law robust in adverse-pressure-gradient boundary layers but
  confined below $y^+_{\log,\max}=1.78\,Re_\tau^{1/2}(\Delta p_s^+)^{-1/5}$, with
  $\Delta p_s^+=\nu\rho^{-1}u_\tau^{-3}dP/ds$ the inner-scaled pressure
  gradient, and a half-power law above it (Eq. 35; $\Delta p_s^+$ registry §11); the
  log layer then ends below $0.11\delta$ for $\Delta p_s^+>0.005$ and a
  Rotta–Clauser parameter above 4.5 (§5.2). Details on
  the [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
  page. Gillyns et al. (2022, §1) place the validity of the law of the wall
  at $y/\delta\lesssim0.15$ and expect an algebraic wall model to fail once
  Coles' wake reaches the matching point near separation.
- **Pressure gradients in wall models.** The equilibrium fit of Meneveau (2020), as used by
  Fowler et al. (2022, Algorithm 1), returns $\langle u_\tau\rangle h_{\mathrm{wm}}/\nu$
  as a function of $U_{\mathrm{LES}}h_{\mathrm{wm}}/\nu$ and a dimensionless
  wall-parallel pressure gradient, and returns zero friction (separation) for
  strong adverse gradients.

- **Hypersonic cold walls.** [Huang et al. (2022)](/sources/huang-2022.md)
  (§4.1, Eq. 4.5, Fig. 11) test logarithmic behaviour with the diagnostic
  function $y^+\,du^+/dy^+$ applied to the transformed velocity: it is nearly
  constant for $y^+\approx40$–100 in their Mach 2.5 and 4.9 quasi-adiabatic
  boundary layers at $Re_\tau=1172$, but their Mach 10.9 boundary layer with
  $T_w/T_r=0.20$ shows no wide constant region up to that $Re_\tau$, which they
  attribute to reduced scale separation from strong wall cooling. Above the
  log region the mean velocity follows a power law
  $\langle u\rangle/U_\infty=(y/\delta_\infty)^{1/n_{pl}}$ over
  $0.2\lesssim y/\delta\lesssim0.6$ with $n_{pl}=5$–8, and the van Driest
  velocity over $0.2\lesssim y/\delta\lesssim0.9$ with $n_{pl}=5$ (Eqs.
  4.6–4.7; page-local $n_{pl}$, $\delta_\infty$ the height where the mean
  velocity first reaches $U_\infty$).
- **Vegetated (canopy) walls: the displaced log law.** Over a submerged
  canopy of flexible blades in open-channel flow,
  [Lohrer & Fröhlich (2025)](/sources/lohrer-2025.md) (§5.2, Eqs. 5.6–5.8),
  after Nepf (2012) as they cite it, write the mean velocity above the
  canopy as

  $$\frac{\langle u\rangle}{u_{\tau,\mathrm{vo}}}=\frac1\kappa\ln\frac{y-y_{\mathrm{vo}}}{\nu/u_{\tau,\mathrm{vo}}}+B-\Delta U^+_{\mathrm{vo}},$$

  with $y_{\mathrm{vo}}$ the displacement height (virtual origin),
  $u_{\tau,\mathrm{vo}}$ the friction velocity built from the total shear
  stress at $y_{\mathrm{vo}}$ and $\Delta U^+_{\mathrm{vo}}$ a roughness
  function (all page-local; the viscous length $\nu/u_{\tau,\mathrm{vo}}$
  "plays the same role as the roughness length in rough-wall boundary
  layers"). A fit over $2.5h_c\le y\le0.8H$ ($h_c=0.20H$ the mean hull height of
  the reconfigured canopy, $H$ the water depth, page-local) with $\kappa=0.41$, $B=5.5$ gives
  $y_{\mathrm{vo}}=0.18H$, $\Delta U^+_{\mathrm{vo}}=15.4$ and
  $u_{\tau,\mathrm{vo}}=0.16U$; fitting $\kappa$ as well gives $\kappa=0.38$,
  $y_{\mathrm{vo}}=0.13H$ and $\Delta U^+_{\mathrm{vo}}=17.4$, so the
  displacement height is sensitive to the assumed $\kappa$. Below the canopy,
  scaled with the bed friction velocity, $u^+=y^+$ holds only up to
  $y^+\approx2$. The flow is a fluid–structure-interaction problem resolved by
  LES with an immersed boundary, not a wall-modelled flow.
- **Volume-filtered law of the wall: the wall slip.** Filtering the flow
  with a compact kernel of support width $\Delta_f$ (registry §11) that is
  truncated at the wall but not rescaled leaves a non-zero filtered velocity
  at the wall, the slip. Rickard & Kasbaoui (2026, §4.1, Eqs. 4.2–4.5) obtain
  a model of the mean slip by filtering the van Driest profile above; for
  $\Delta_f^+\gg1$ it tends to $\varphi_{f,w}^{-1}(2\kappa)^{-1}\ln(\Delta_f^+/2)$,
  with $\varphi_{f,w}$ the fluid volume fraction at the wall (1/2 at a planar
  wall; registry §11 $\varphi_f$ evaluated at the wall), and a fitted correction makes it accurate within 1 %
  for $\Delta_f^+\ge100$. The slip grows logarithmically with the filter
  width, $6.93u_\tau$ at $\Delta_f^+=50$ and $13.5u_\tau$ at $\Delta_f^+=300$
  in filtered channel DNS at $Re_\tau=5200$ (§3.2); see
  [wall-modelled LES](/methods/wall-modelled-les.md).
- **Low-Reynolds pipe flow in RANS.** [Launder & Spalding (1974)](/sources/launder-1974.md)
  (§3.3, Figs. 3.3a,b) report that the measured pipe-flow profile at
  $Re=6000$ (bulk velocity and diameter; data of Kudva & Sesonske as
  cited) lies above the high-Reynolds log law and that the Jones–Launder
  low-Reynolds $k$-$\varepsilon$ model integrated to the wall reproduces the
  departure, whereas near-wall formulae independent of Reynolds number,
  tuned for $Re>20\,000$, over-predict the friction factor at low $Re$ (see
  [$k$-$\varepsilon$ models](/methods/k-epsilon-model.md)).
- **Low Reynolds number.** [Kim et al. (2022)](/sources/kim-2022.md) (§III D,
  Fig. 12) state, citing the channel DNS of Moser, Kim & Mansour, that the
  DNS mean velocity at $Re_\tau=180$ deviates slightly from the log law in the
  logarithmic region, and use this non-universality to explain why an SGS
  model trained by reinforcement learning at $Re_\tau=180$ under-estimates the
  buffer-layer slope at $Re_\tau=360$, while one trained at 360 over-estimates
  the mean velocity at 180 (see
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md)):
  "the non-universal characteristic of $Re_\tau=180$ affects the
  generalization performance of the DRL model".
- **Separated regions.** Cai et al. (2022, §II.C.2) state that equilibrium
  and non-equilibrium wall models assume quasi-parallel near-wall flow and
  that their use under separation is "physically not appropriate", but that
  the small wall stress there keeps the model in the low-$y^+$ range "where
  linear profile applies", and cite three studies finding the flow not very
  sensitive to the wall model in the recirculation zone.
- **Universality claimed for learned models.** Bae & Koumoutsakos (2022,
  Discussion) state, citing the literature, that all flows with inner–outer
  scale separation exhibit a log law, and take this as the reason a state
  space built on the local log-law slope and intercept can extend to
  roughness, stratification and compressibility (not shown).

- **RANS on DG grids.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md)
  (§5.1, Fig. 5-2) report that the velocity profile of their interior-penalty
  DG solver with the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
  on a turbulent flat plate ($M=0.2$, $Re_L=1.12\times10^7$, first-cell
  $y^+=1$) agrees with a reference profile they cite in the log layer.
  [Lodares et al. (2022)](/sources/lodares-2022.md) (§7.3, Fig. 8a) compare
  the $u^+(y^+)$ profile of their entropy-stable DG Spalart–Allmaras RANS on
  the coarsest flat-plate mesh of the NASA Turbulence Modeling Resource
  ($M=0.2$, $Re=5\times10^6$, profile at $x=0.97008$, $N=4$, 7, 10) with the
  viscous sublayer, the log law and a fine-grid FUN3D solution, "in good
  agreement". [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md)
  (§4.1, Figs. 9–10) find the velocity profiles of their flux-reconstruction
  $k$-$\omega$ SST solution of the Wieghardt plate in agreement with
  experiment and Spalding's law, coinciding across orders, on meshes whose
  first element reaches $y_1^+\simeq25$ without wall function (see
  [RANS wall function](/methods/rans-wall-function.md)).
  [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md) (§5.3, Figs.
  13–14) find the skin friction and velocity profile of their
  [isogeometric](/methods/isogeometric-analysis.md) DG Spalart–Allmaras
  solution of a flat plate ($M=0.2$, $Re=1.1\times10^7$, 8800 elements,
  $y_1^+<1$, $N=4$) in "perfect" agreement with $u^+=y^+$, the log law with
  $\kappa=0.41$, $B=5$ and the data of Wieghardt & Tillmann (as cited);
  with the mesh adapted from $y_1^+=100$ down to about 1 they report about
  60 % fewer degrees of freedom and computing time than a reference mesh
  (see [mesh adaptation](/methods/mesh-adaptation.md)).
- **Pipe flow and transitional plates in RANS.** [Tomboulides et al. (2025)](/sources/tomboulides-2025.md)
  (§3.2, Fig. 5) find their [$k$-$\tau$](/methods/k-tau-model.md) and
  regularized $k$-$\omega$ pipe-flow profiles at $Re_\tau=1142$ in excellent
  agreement with DNS in the viscous sublayer ($y^+<5$) and with the log law
  ($\kappa=0.41$, $B=5.5$) for $30<y^+<200$, with minor RANS–DNS
  differences there and "expected deviations" in the outer layer.
  [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) (§IV.A,
  Figs. 12–13) use $u^+=y^+$ and the log law with $\kappa=0.41$, $B=5$ as
  reference for the turbulent part of the transitional ERCOFTAC plate
  boundary layers computed with their
  [laminar-kinetic-energy transition model](/methods/laminar-kinetic-energy-transition-model.md),
  with which all their velocity profiles agree.
- **Compressible channel.** Wang et al. (2023b, §4.2, Eqs. 10–11, Fig. 11)
  compare the van Driest-transformed mean velocity of their gas-kinetic DNS of
  a channel at bulk $M_b=0.8$ and bulk Reynolds number 3000 (isothermal walls)
  with the incompressible log law; see the
  [compressible velocity transformation](/definitions/compressible-velocity-transformation.md).

## The law of the wall as a constraint

Vadrot et al. (2023b, §V) make preservation of the law of the wall the minimum
requirement of any learned wall model: a model must reproduce the log law in
channel flow at all Reynolds numbers, seen and unseen, before it is credited
with improvements elsewhere (see [machine-learning wall models](/methods/machine-learning-wall-model.md)).
Their a priori test of the ZHY21/ZYZY22 networks feeds a law of the wall built
by stitching the $Re_\tau=5200$ DNS wall layer to $u^+=\kappa^{-1}\ln y^++B$ at
$y^+=100$ (§IV.B). The mean-velocity departure from the log law is the
[log-layer mismatch](/definitions/log-layer-mismatch.md).
Bae & Koumoutsakos (2022, Methods, Eq. 3) build the states of their
log-law-based reinforcement-learning wall model from the instantaneous local
slope and intercept of the log law at the matching height, so that the agent
learns to raise or lower $\tau_w$ according to whether the local state lies
above or below $u^+=0.41^{-1}\ln y^++5.2$ (Fig. 2); see
[machine-learning wall models](/methods/machine-learning-wall-model.md).
Vadrot et al. (2023a, §V) state the same position for their own
reinforcement-learning model: recovering the log law is "an essential
step", since "if a model cannot capture the log law, it would be hard for it
to capture other flow phenomena"; their model, trained at $Re_\tau=10^4$,
recovers $u^+=0.4^{-1}\ln y^++5$ in half-channel WMLES up to
$Re_\tau=10^{10}$ whenever the matching height lies in the log layer, while
at $Re_\tau=180$ its profile lies above the DNS (§III.A, Fig. 6).

**Data-driven RANS corrections.** Two sources make the same point for
learned corrections of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md):
a correction trained on separated flows breaks the log law unless it is
kept out of the attached boundary layer.
[Wu et al. (2025)](/sources/wu-2025.md) (§2.1, Eqs. 3–4) cite Wilcox for
the log-layer calibration of the $\omega$ equation,

$$\beta_\omega-\beta^*\gamma_\omega=\kappa^2\sqrt{\beta^*}\,\sigma_\omega,\qquad\kappa=0.41,$$

with $\gamma_\omega$, $\beta_\omega$ the production and destruction
coefficients of the $\omega$ equation (registry §11; the source's $\gamma$
and $\theta$), a "necessary condition for accurate resolution of the log
layer". A [field-inversion](/methods/field-inversion-machine-learning.md)
multiplier $\beta(\boldsymbol x)$ on the destruction term turns the
left-hand side into $\beta(\boldsymbol x)\beta_\omega-\beta^*\gamma_\omega$,
so the constraint holds only where $\beta=1$. Their conditioned inversion
switches the multiplier off inside the boundary layer with the DDES shielding
function; on a zero-pressure-gradient flat plate at $Re_L=10^7$ the
conditioned symbolic model keeps $\beta=1$ there and matches SST and the
viscous and log layers, while the unconditioned one gives $\beta\approx1.06$
in the boundary layer, an "erroneous log layer", a thicker boundary layer
and an over-predicted $C_f$ (§4.5, Figs. 47–48).
[Oulghelou et al. (2025)](/sources/oulghelou-2025.md) (§4.2.1, Table 3)
quantify the same effect for sparse symbolic corrections in channel flow at
$Re_\tau=1000$: the mean absolute error of $u^+$ is 0.44 for the baseline
SST, 2.41 for a correction trained on separated flows and 8.97 for one
trained on a near-sonic jet, which strongly lowers the eddy viscosity; their
locally weighted blend of the three gives the baseline's 0.44, with a
weight of the baseline close to one across the channel. On the unseen flat
plate the blend's error is 0.7 against 0.42 for SST and 6.27 for the jet
correction, although the jet correction receives a significant weight in
the log region, which the authors read as weight shifts there having "little
impact on the overall accuracy" (§5.1.1, Table 9, Fig. 11). See
[turbulence-model aggregation](/methods/turbulence-model-aggregation.md).

**Calibrating RANS constants on the log layer.** [Heinz (2020)](/sources/heinz-2020.md)
(§2.3, Eqs. 8–11) writes the log-layer solution of two-equation models,
$\partial\langle u\rangle/\partial y=u_\tau/(\kappa y)$, $k=u_\tau^2/C_\mu^{1/2}$,
$\varepsilon=u_\tau^3/(\kappa y)$ and $\nu_t=\kappa yu_\tau$, and the conditions
it imposes on the constants: $\kappa^2=C_\mu^{1/2}\sigma_\varepsilon(C_{\varepsilon2}-C_{\varepsilon1})$
for the [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md), which with
$C_{\varepsilon1}=1.44$, $C_{\varepsilon2}=1.92$, $\sigma_\varepsilon=1.3$
requires "a relatively high value" $\kappa=0.43$, and
$\kappa^2=C_\mu^{1/2}\sigma_\omega(C_{\omega2}/C_\mu-C_{\omega1})$ for the
[$k$-$\omega$ model](/methods/k-omega-model.md), which with the constants of
Bredberg et al. as cited, $(C_{\omega1},C_{\omega2},C_\mu,\sigma_\omega)=(0.49,0.072,0.09,1.8)$,
gives $\kappa=0.41$ ($C_{\omega1}$, $C_{\omega2}$ page-local; the
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md) constants
also give 0.41, §3.4, Eq. 33). Heinz's $k$-$\omega$ condition is the constraint of Wu
et al. above with $C_{\omega2}=\beta_\omega$, $C_{\omega1}=\gamma_\omega$,
$C_\mu=\beta^*$ and Heinz's $\sigma_\omega$ the
reciprocal of theirs; with Heinz's constants,
$0.3\times1.8\times(0.8-0.49)=0.167$ and $\sqrt{0.167}=0.409$ *(compiler check,
not in the sources)*.

The same log-layer solution is how the founding papers fix their
constants. Launder & Spalding (1974, §2.1, Eqs. 2.1-10–2.1-13) insert the
log law and $\nu_t=C_\mu k^{1/2}L$ ($L$ a length scale proportional to $y$,
page-local) into the equation of a generic length-scale variable
$k^m/L^n$ with uniform $k$, which gives
$n^2/\sigma_t+C_1C_\mu^{1/2}/\kappa^2-C_2C_\mu^{1/2}/\kappa^2=0$ ($\sigma_t$
the variable's Prandtl number, $C_1$, $C_2$ its production and destruction
constants, page-local); for $\varepsilon$ ($n=1$) it is Heinz's
$k$-$\varepsilon$ condition *(compiler check, not in the sources)*, and they use it to reject the $kL$ and
$k/L^2$ variables, which would need $\sigma_t=-0.8$ and 2.9 (details on the
[$k$-$\varepsilon$ page](/methods/k-epsilon-model.md)). In their wall
functions the log law is reproduced "identically" when the shear stress is
uniform and generation balances dissipation, since then
$\tau/\rho=C_\mu^{1/2}k$ (§2.3-1; see
[RANS wall functions](/methods/rans-wall-function.md)).
[Spalart & Allmaras (1992)](/sources/spalart-1992.md) (pp. 5–8) build the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) on the same
solution: with $\lvert\Omega\rvert=u_\tau/(\kappa d)$ and $\nu_t=u_\tau\kappa d$
($\lvert\Omega\rvert$ the vorticity magnitude the model uses, $d$ the wall
distance), the balance of
production, diffusion and destruction requires
$c_{w1}=c_{b1}/\kappa^2+(1+c_{b2})/\sigma$, a constant "not negotiable" (p.
6); in units of the production the ideal near-wall budget has diffusion
$\kappa^2(1+c_{b2})/(\sigma c_{b1})\approx3$ and destruction $\approx-4$, a
balance not maintained far into the layer, so that $\nu_t$ departs from
$\kappa yu_\tau$ while a log layer still forms (p. 7, Fig. 6). The damping
function $f_{v1}$ and the modified vorticity are built so that the working
variable equals $\kappa yu_\tau$ and the modified vorticity $u_\tau/(\kappa y)$
"all the way to $d=0$", which the authors find to be a stable numerical
solution from a wide range of initial conditions; they prefer
$c_{v1}=7.1$ to Mellor & Herring's 6.9, which they believe yields a low
log-law intercept, and found no case where the choice of $f_{v1}$ mattered
(p. 8). An alternative $f_{v1}$ compatible with van Driest damping
($A^+=26$) is given (p. 8). The flat-plate calibration then fixes $c_{w2}=0.3$
from $C_f=0.00262$ at $Re_\theta=10^4$ (p. 6; see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)). With
the printed constants $c_{b1}=0.1355$, $c_{b2}=0.622$, $\sigma=2/3$ and
$\kappa=0.41$, $c_{w1}=0.806+2.433=3.239$ and the diffusion ratio is
$0.1681\times2.433/0.1355=3.02$ *(compiler check, not in the sources)*.

**A diagnostic of logarithmic behaviour.** The premultiplied gradient
$y^+\,du^+/dy^+$ is constant, equal to $1/\kappa$, in a log layer: Huang et
al. (2022, Eq. 4.5) use it on transformed hypersonic profiles (above), and
Mukha et al. (2025, §III.B.2, Fig. 3) use $\kappa y^+\,du^+/dy^+$, equal to
one in a log layer, to expose the jumps of the velocity derivative at the
element boundaries of their spectral-element WMLES (see
[log-layer mismatch](/definitions/log-layer-mismatch.md)).

The friction velocity is also the first quantity a near-wall LES must get
right without a wall model: [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§7.2–7.4) report $u_\tau$ errors in pipe flow at $Re_\tau=1000$ of $+15.3$ %
(no model), $+9.6$ % (Smagorinsky with van Driest damping) and $-1.8$ %
(implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md))
on a uniform mesh with $\Delta x^+=\Delta y^+\approx9$.

## Qualifications

- The constants are source choices, not measurements of this bundle; the
  table records them and no value is preferred here.
- Mozaffari et al. (2024) print for Cai & Sagaut (2021), their ref. [8], a
  DOI identical to the one they print for Wilhelm et al. (2021), ref. [63];
  one of the two DOIs is a slip.
- **Printed viscosity of Zhao et al. (2023a).** For $Re_\tau=180$ they print
  $\mu=2.83\times10^{-4}$ (§5.2). With their Eqs. (25)–(26), $\rho=1$, $\delta=1$
  and $U_c=1$: $U_c^+=2.5\ln180+5.5\approx18.48$, $u_\tau\approx0.0541$ and
  $\mu\approx3.01\times10^{-4}$ *(compiler check, not in the sources)*; the
  printed value is not reproduced. Zhao et al. (2021, §IV) print the same
  $\mu=2.83\times10^{-4}$ with the same Eqs. (25)–(26); their Table V,
  however, gives resolved $U_\tau/Re_\tau=0.0535/177.8889\approx3.008\times10^{-4}$
  and $0.0526/174.9860\approx3.006\times10^{-4}$, consistent with
  $3.01\times10^{-4}$, not with the printed value, while their
  $\mu=1.24\times10^{-4}$ at $Re_\tau=395$ is reproduced by the same
  procedure ($1.238\times10^{-4}$) *(compiler check, not in the sources)*.
- Griffin et al. (2023) print Eq. (1.2) as
  $\mu_t=\kappa y\langle\rho\rangle\sqrt{\tau_w/\langle\rho\rangle}\,(1-\exp(y^+/A^+))^2$,
  without the minus sign in the exponent; their own text describes a damping
  function that tends to the undamped mixing length away from the wall, which
  holds only for $(1-e^{-y^+/A^+})^2$. In §3 they print "$\kappa$ … 4.1" for
  the 0.41 stated in §1 and at the end of §3.
- **Intercept of Mukha et al. (2025) for the boundary layer.** §IV.A
  prints "here with $\kappa=0.41$ and $B=5.2$" for the flat-plate WMLES, and
  App. A prints "$\kappa=0.41$ and $B=5.5$" for the accuracy analysis of the
  same law on the same flow; which value the simulations used cannot be
  told from the arXiv v1 read.
- **Argument order of the arctangents of Husson et al. (2024).** They define
  $\mathrm{atan2}(y,x)$ as the principal argument of $x+iy$ and print the
  terms as $\mathrm{atan2}(y^++a_k,b_k)$, the argument of $b_k+i(y^++a_k)$.
  Evaluated so, the law gives $u^+(0)\approx10.84$ and a log-law intercept
  near $-6.3$; with the arguments exchanged, the argument of
  $(y^++a_k)+ib_k$, it gives $u^+(0)=0$ to machine precision, $u^+\approx1.00$
  at $y^+=1$, the slope $1/0.41$ and the intercept 5.033 at $y^+=10^5$
  *(compiler check, not in the sources)*. The printed order is therefore
  inconsistent with the printed definition; the exchanged order is the one
  that yields a wall law.
- **Additive constant of the composite law of Gao et al. (2025b).** With
  their printed constants and the arctangent as the argument of
  $(y^++a_k)+ib_k$ (the order that yields a wall law above), their
  $B=3.0333909$ gives $u^+(0)=-2.000$ and $u^+(1)=-1.000$, while
  $B=5.0333909$ gives 0.000 and 1.000. Their own fitted inverse returns
  $y^+=65.1$ at $Re_y=1000$; the law gives $Re_y=y^+u^+=996$ at that height
  with $B=5.0333909$ (the additive constant of Husson et al. 2024 to the
  printed digits) and 865 with the printed 3.0333909 *(compiler check, not
  in the sources)*.
- **Printed truncations of Spalding's law.** Ghidoni et al. (2026, Eq. 12)
  print the series up to the quadratic term, Nuca et al. (2025, Eq. 2) up to
  the cubic term; both call it Spalding's law. The difference is recorded
  without a test of which form either code uses beyond the printed one.
- **Printed slips of Nuca et al. (2025).** The text gives $\kappa$ "from 0.38
  to 0.41" for the global fits, Table II up to 0.42 (0.40 for Reichardt);
  the relation for $B$ appears twice, as Eqs. (1) and (8), written with
  $\log$ and $\ln$. The high-Re constants give $C=6.66$, outside the range
  $C\in[6.8,7.7]$ over which the global Reichardt approximation is fitted,
  so its use with the high-Re set in the channel test is an extrapolation
  that the paper does not mention *(compiler check, not in the sources)*.
- **Printed slips of Huang et al. (2022b)** (§2.4.3). The friction velocity
  of their manufactured profile is printed as
  $\sqrt{\rho_0u_0^2C_f/\rho}=\sqrt{a\rho_0u_0^2x^b/(2\rho)}$ with the fit
  $C_f=ax^b$, the two forms differing by the factor 1/2 under the root; with
  $\tau_w=\tfrac12\rho_0u_0^2C_f$ the second is the consistent one *(compiler
  check, not in the sources)*. The fit is said to be of the data "shown in
  Fig. 8", which is Fig. 9; the profile's $\kappa$ and additive constant are
  not printed, and the cited Reichardt (1951) is attached in the text to the
  LU-SGS solver instead.
- **Reichardt's law of Huang et al. (2022c) against their log law.** For
  large $y^+$ their Eq. (17) tends to $\kappa^{-1}\ln y^++D+\kappa^{-1}\ln\kappa$,
  an intercept of $9.8+\ln(0.41)/0.41\approx7.63$ against $B=5.2$ of their
  Eq. (14); at $y^+=0.224\times550\approx123$, their matching point at $Re_\tau=550$, Eq. (17)
  gives $u^+\approx19.4$ and Eq. (14) $u^+\approx16.9$, a gap of about 2.5
  *(compiler check, not in the sources)*. The printed constants thus do not
  support the statement that the two laws coincide in the log region.
- **Clauser–Rotta thickness of Devenport & Lowe (2022).** Eq. (2.33)
  prints $\int_0^\delta(U_e-\langle u\rangle)/u_\tau\,dy=\delta^*\sqrt{C_f/2}$.
  Since $\int_0^\delta(U_e-\langle u\rangle)dy=U_e\delta^*$ and
  $U_e/u_\tau=\sqrt{2/C_f}$, the integral equals $\delta^*\sqrt{2/C_f}$
  *(compiler check, not in the sources)*, the $u_e^+\delta^*$ of Chen et al.
  (2024) above.
- **Printed branch of Akbarzadeh & Borazjani (2025).** Their Eq. (23)
  prints the logarithmic branch at the boundary node as
  $\kappa^{-1}\ln(y^+_c)+B$, the value at the fluid point $c$, while the
  linear branch and the switch are written in $y^+_b$; Eq. (24) then uses
  this $u^+_b$ for the boundary node.
- Oulghelou et al. (2025) and Wu et al. (2025) write the steady
  incompressible RANS equations and solve them in OpenFOAM (Wu et al. also run CFL3D for a
  compressible airfoil case); their log-law statements concern RANS
  profiles, not LES.

## Contradictions

- **Constants of the explicit inverse wall law of Cai & Sagaut (2021).**
  [Cai et al. (2022)](/sources/cai-2022.md) (§II.C.1, Eqs. 24–26) present
  the tanh-blended explicit inverse $y^+(Re_y)$ as the model "proposed in
  Refs. 23 and 29" (ref. 29 is Cai & Sagaut 2021) and print the blend scale
  180.8, the exponent 0.789 and, in the companion forward profile, $E=11.27$.
  [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) (§2.2, Eqs. 12–15,
  lines 160–164) give the same functional form "in the form [8]" (ref. [8]
  is Cai & Sagaut 2021) with $s=86.58$, $p=0.7894$ and $E\approx7.9$,
  $\kappa\approx0.41$. Cai is a co-author of both and both run in ProLB;
  neither paper says that its constants recalibrate the cited model, so the
  two sources disagree on the constants of the same attributed law (the
  blend scales differ by a factor of about two and the log branches through
  $E$). Cai & Sagaut (2021) is not ingested. [Nuca et al. (2025)](/sources/nuca-2025.md)
  (§III, Eq. 5) print a third form attributed to "model 2" of Cai & Sagaut
  (2021), a forward law $u^+(Re_y)$ blended with powers of
  $e^{-Re_y/s}$ instead of $\tanh$, and say that they re-optimize $p$ and
  $s$; their constants therefore do not bear on the disagreement, but the
  functional form they attribute differs from that of the other two, so the
  ingested sources do not fix the form either. *Open.*

# Citations

- [Fowler et al. (2022)](/sources/fowler-2022.md) — App. C, Eqs. (C1)–(C2), Fig. 17; Algorithm 1; Fig. 4.
- [Devenport & Lowe (2022)](/sources/devenport-2022.md) — §2.1, Eqs. (2.22)–(2.34); §2.2; §5.3, Eq. (5.11).
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §II C, Eqs. (14), (17); §III C, Fig. 7.
- [Zhang et al. (2022e)](/sources/zhang-2022-i.md) — §II A, Eq. (3).
- [Zhang et al. (2022c)](/sources/zhang-2022-g.md) — §II C, Eq. (2), Fig. 6a.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §IV.C, Eq. (12); §V.C.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1, Eq. (1.2); §3, Fig. 6.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II.B, Eqs. (1)–(6); §IV.B; §V.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D, Fig. 8.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.2–7.4, Figs. 25–27.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1; §3, Eq. (3).
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Eq. (3); Fig. 2; Discussion; Methods.
- [Knopp (2022)](/sources/knopp-2022.md) — §4, Eq. (26); §5–6, Eq. (35).
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1, Eqs. (4.5)–(4.7), Figs. 11–12.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.3, Eq. (8).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4, Fig. 8.
- [Kim et al. (2022)](/sources/kim-2022.md) — §III D, Fig. 12.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.C.1, Eqs. (24)–(26); §II.C.2.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.3.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Figs. 4–5.
- [Dang et al. (2022)](/sources/dang-2022.md) — §5.1, Fig. 17.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.2, Eq. (3.1).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.2 (HAL accepted manuscript).
- [Kang et al. (2023)](/sources/kang-2023.md) — channel-flow mean-velocity figures (§3).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2, Eqs. (10)–(11), Fig. 11 (arXiv v1).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.2, Eqs. (25)–(26) (arXiv v1).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.1, Fig. 5-2.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.B.1, Eq. (1); §II.B.3; §III.A–III.B, Fig. 6; §V (arXiv v3).
- [Constant et al. (2024)](/sources/constant-2024.md) — §3.2, Eqs. (6)–(8), Fig. 7 (HAL author manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.2, Eqs. (9)–(15); ref. [8] (HAL accepted manuscript).
- [Chen et al. (2024)](/sources/chen-2024.md) — §2.3, Eqs. (2.7)–(2.10); §3.1, Eqs. (3.1)–(3.4), Fig. 3; §3.2, Eqs. (3.9)–(3.12), Fig. 5.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §II.C.1; §III.A; §III.B.2–III.B.3, Fig. 3; §IV.A; App. A, Figs. 18–21 (arXiv v1).
- [Lohrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §5.2, Eqs. (5.6)–(5.8).
- [Oulghelou et al. (2025)](/sources/oulghelou-2025.md) — §4.2.1, Table 3, Fig. 4; §5.1.1, Table 9, Fig. 11 (arXiv v2).
- [Wu et al. (2025)](/sources/wu-2025.md) — §2.1, Eqs. (3)–(4); §4.5, Figs. 47–48 (authors' manuscript).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §5.2.1, Eqs. (93)–(94), Fig. 16; §5.3.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §3.3, Eqs. (12)–(15); §4.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — §4.2, Fig. 7 (arXiv v1).
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §3.2, Fig. 6; §4.1, Eqs. (4.1)–(4.5), Fig. 11.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §4.1, Fig. 1.
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I; §III, Eqs. (1)–(8); §IV, Eqs. (9)–(10), (24), Fig. 3; §V.A–V.B, Tables II–VI.
- [Husson et al. (2024)](/sources/husson-2024.md) — §3.1, Eqs. (36)–(38).
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §3.2, Fig. 5.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §IV.A, Figs. 12–13.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §4.1, Figs. 9–10.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §7.3, Fig. 8.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §IV, Eqs. (24)–(26), Table V.
- [Bose & Park (2018)](/sources/bose-2018.md) — §2.1, Eqs. (3), (6), Fig. 3; §4.1.
- [Heinz (2020)](/sources/heinz-2020.md) — §2.3, Eqs. (8)–(11); §3.4, Eq. (33).
- [Lv et al. (2021)](/sources/lv-2021.md) — §II A, Eqs. (3)–(6); §IV B 1, Fig. 11.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §III.A.1, Fig. 6.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.4.3, Eq. (52), Fig. 9.
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §3, Fig. 3.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — Fig. 5.
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §2.2, Eq. (6).
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §2.5, Eq. (35).
- [Mo et al. (2023)](/sources/mo-2023.md) — §II B, Eqs. (9)–(10).
- [Shi & Yan (2023)](/sources/shi-2023.md) — §IV.B, Fig. 9.
- [Gao et al. (2023)](/sources/gao-2023.md) — §5.2, Fig. 18.
- [Yu et al. (2023)](/sources/yu-2023.md) — §3, Fig. 5; §4.1, Eq. (4.1).
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §2.3, Eqs. (2.19)–(2.20).
- [Hu et al. (2024)](/sources/hu-2024.md) — §2; §4, Eq. (5).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.3, Fig. 3.
- [Kang & Lee (2024)](/sources/kang-2024.md) — §III, Eq. (16), Fig. 4b.
- [Tang et al. (2024)](/sources/tang-2024.md) — §2.3, Eq. (2.6), Fig. 11a.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §3.1, Eqs. (3.1)–(3.2), Fig. 5a.
- [Wang & Xu (2024)](/sources/wang-2024-h.md) — §4.2, Fig. 8.
- [Wei et al. (2023)](/sources/wei-2023.md) — §III B, Fig. 10.
- [Yan et al. (2024)](/sources/yan-2024.md) — §II C, Eqs. (24)–(28).
- [Wang et al. (2024d)](/sources/wang-2024-k.md) — §II D, Eq. (22); Figs. 2, 5.
- [Xiao et al. (2025)](/sources/xiao-2025.md) — §2.1, Eq. (10).
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §2.4, Eqs. (19)–(24).
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §3.3, Eq. (27), Figs. 8–9.
- [Guo & Wang (2025)](/sources/guo-2025.md) — Eq. (18) (Spalding's law in the OpenFOAM wall function).
- [Fang et al. (2025)](/sources/fang-2025.md) — §3.4, Figs. 12–13 (log layer lifted by a wall-normal magnetic field).
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — Fig. 1 (reference log law; passing).
- [Alberti et al. (2025b)](/sources/alberti-2025-c.md) — captions of Figs. 1, 9, 11 (compound law of the wall, $B=5.5$; reference only).
- [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md) — §5.3, Figs. 13–14 (flat-plate RANS against the log law, $\kappa=0.41$, $B=5$).
- [Gao et al. (2025)](/sources/gao-2025.md) — §II.B, Eq. (10); Figs. 5, 8, 14 (reference log law).
- [Gao et al. (2025b)](/sources/gao-2025-b.md) — §II C1, Eqs. (17)–(18) (Allmaras–Johnson–Spalart composite law); App. A, Table III.
- [Launder & Spalding (1974)](/sources/launder-1974.md) — §2.1, Eqs. (2.1-10)–(2.1-13); §2.3-1; §3.3, Figs. 3.3a–b (log-law constants of the standard wall functions, log-layer constraint on the length-scale equation, low-Reynolds pipe flow).
- [Spalart & Allmaras (1992)](/sources/spalart-1992.md) — pp. 5–8, Fig. 6; App. (p. 21) (log-layer calibration of $c_{w1}$, near-wall budget, $f_{v1}$ and $c_{v1}=7.1$).
