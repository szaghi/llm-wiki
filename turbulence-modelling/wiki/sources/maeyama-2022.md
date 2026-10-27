---
type: Source
title: "Maeyama et al. (2022) — Multi-scale turbulence simulation suggesting improvement of electron heated plasma confinement"
description: "Multi-scale gyrokinetic simulations of a burning-plasma-like tokamak flux tube at electron temperature above ion temperature show that ion-scale trapped-electron-mode and electron-scale ETG turbulence suppress each other, reducing the electron heat flux from 33.63 to 5.66 gyro-Bohm units and upshifting the critical temperature ratio of TEM-dominated transport."
resource: "doi:10.1038/s41467-022-30852-0"
source_kind: paper
authors: [Maeyama S., Watanabe T.H., Nakata M., Nunami M., Asahi Y., Ishizawa A.]
year: 2022
venue: "Nat. Commun. 13:3166"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Nature_Communications_Maeyama_Multi-scale_turbulence_simulation_suggesting_improvement_of.pdf"
tags: [plasma, dns, energy-cascade]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Maeyama et al. (2022) study the
[cross-scale interaction](/results/cross-scale-interaction.md) of
ion-scale and electron-scale micro-turbulence in a tokamak plasma with
electron temperature above ion temperature ($T_e/T_i>1$), the regime of
electron-heated ITER phases and alpha-heated burning plasmas. Conventional
turbulent-transport modelling of fusion plasmas treats the two scales
separately and is tuned to ion-scale transport, so it misses their
coupling. The authors run multi-scale simulations with
the delta-$f$ electromagnetic gyrokinetic code GKV (local flux tube,
Fourier spectral in the perpendicular plane) on Fugaku, resolving from the
electron to the ion gyroradius with four species (electrons, deuterium,
tritium, helium ash). The paper does not call them
[direct numerical simulation](/definitions/direct-numerical-simulation.md);
they resolve both scale ranges, while the comparison runs truncate the
spectrum to one of them (Methods).

The ion-scale instability is the trapped electron mode (TEM), the
electron-scale one the toroidal electron-temperature-gradient (ETG) mode.
At $T_e/T_i=3$ the multi-scale run gives an electron heat flux of
$5.66\,Q_{gB}$ against $33.63\,Q_{gB}$ in the ion-scale-only run, and the
fuel and ash fluxes are also lower (0.24 against 1.11 and 0.02 against
0.09 $Q_{gB}$). Three diagnostics locate the
mechanism: tracer-particle trajectories show ETG fluctuations disturbing
the electrons in precession-drift resonance with the TEM; the
velocity-space heat flux puts the transport on those resonant trapped
electrons; and a nonlinear entropy-transfer analysis with triad and
subspace transfer functions shows electron-scale coupling damping
low-$k_y$ TEMs and ion-scale eddies damping ETG modes, without strong
zonal flows. A $T_e/T_i$ scan from 1 to 4 shows the reduction in an
intermediate range and an upshift of the critical temperature ratio for
TEM-dominated flux from about 2 (ion-scale run) to about 3 (multi-scale
run), which the authors liken to the Dimits shift. Their message for transport
modelling is that scale-separated models lack cross-scale interactions
(Abstract).

# Version read

Version of record (Nat. Commun. 13:3166, open access CC BY 4.0; received
27 September 2021, accepted 23 May 2022, published 7 June 2022), 8 pages,
all read (equations and subspace definitions of pp. 4–7 read visually).
Page 1 matches the Crossref metadata. The Supplementary Information
(Supplementary Figs. 1–2) is not in the file and was not read.

# Key claims

1. Conventional turbulent-transport modelling of fusion plasmas lacks cross-scale interactions; it was designed to reproduce ion-scale transport under the scale-separation assumption (Abstract; Introduction, p. 2). **Stated**
2. Linear analysis at the run parameters: the most unstable TEM is at $k_y=0.25\,\rho_{ti}^{-1}$ with $\omega_r=1.50\,v_{ti}/R_0$, $\gamma_{\mathrm{lin}}=0.145\,v_{ti}/R_0$; the most unstable ETG mode at $k_y=4.5\,\rho_{ti}^{-1}$ with $\omega_r=24.3\,v_{ti}/R_0$, $\gamma_{\mathrm{lin}}=1.16\,v_{ti}/R_0$ (Results, Fig. 1). **Shown**
3. TEM and ETG have similar toroidal phase velocities, printed as $(\omega_r/k_{\mathrm{tor}})_{\mathrm{TEM}}=42.7\,v_{ti}\rho_{ti}/R_0$ and $(\omega_r/k_{\mathrm{tor}})_{\mathrm{ETG}}=45.1\,v_{ti}\rho_{ti}/R_0$, with $k_{\mathrm{tor}}=\epsilon_ak_y/q_s$ (Results, p. 2). **Shown** (see Printed slips)
4. The TEM precession-drift resonance $v_{\mathrm{pre}}=\omega_r/k_{\mathrm{tor}}$, with $v_{\mathrm{pre}}\sim m_ev^2q_s/(2erB_0)$ for deeply trapped electrons, is met at particle speed $v=1.9\,v_{te}$ (Results, p. 2). **Derived**
5. Tracer particles: a resonant electron ($v=2v_{te}$, $v_{\mathrm{pre}}=47.3\,v_{ti}\rho_{ti}/R_0$) feels the TEM poloidal electric field over a toroidal path $yq_s/(\epsilon_a\rho_{ti})<400$ and drifts radially; an off-resonant one ($v=2.5v_{te}$, $v_{\mathrm{pre}}=73.9\,v_{ti}\rho_{ti}/R_0$) has no net radial displacement; small-scale ETG fields disturb the resonant trajectory and produce a secular displacement beyond $yq_s/(\epsilon_a\rho_{ti})>700$ (Fig. 2, $162.4<tv_{ti}/R_0<179.4$). **Shown**
6. The velocity-space-resolved electron energy flux shows that trapped electrons in precession-drift resonance carry the turbulent heat transport (Fig. 3c, averaged over $100<tv_{ti}/R_0<200$ at $\theta=0$). **Shown**
7. Small-scale ETG eddies coexist with large-scale TEM fluctuations in the nonlinear state; no strong zonal flows appear in the multi-scale run (Fig. 3a,b). **Shown**
8. Heat fluxes at $T_e/T_i=3$: multi-scale $Q_e=5.66\,Q_{gB}$, $Q_D+Q_T=0.24\,Q_{gB}$, $Q_{He}=0.02\,Q_{gB}$; single ion-scale TEM run $Q_e=33.63\,Q_{gB}$, $Q_D+Q_T=1.11\,Q_{gB}$, $Q_{He}=0.09\,Q_{gB}$; the reduction is attributed to suppression of the TEM by ETG turbulence (Results, p. 3, Fig. 4). **Shown**
9. The low-$k_y$ TEM part of the flux spectrum is reduced in the multi-scale run relative to the ion-scale-only run; the high-$k_y$ ETG peaks of the multi-scale and electron-scale-only spectra coincide (Fig. 4). **Shown**
10. In the electron-scale-only run, ETG turbulence first saturates at higher transport, then ETG-driven zonal flows suppress it after $tv_{ti}/R_0\ge50$ ("not shown"); in the multi-scale run no significant zonal flow appears, so ETG is suppressed by cross-scale interactions instead (p. 3). **Stated** (data not shown)
11. Shearing by TEM eddies, not necessarily zonal flows, can suppress ETG turbulence, in contrast with earlier work [34] that attributed the suppression to TEM-driven zonal flows (p. 3). **Shown** (absence of zonal flows plus entropy transfer)
12. Entropy transfer: the electron-scale/electron-scale coupling $\mathcal T_{\boldsymbol k}^{\mathcal K_e,\mathcal K_e}<0$ at $k_y\rho_{ti}<0.5$, directly confirming the damping of TEMs by ETG turbulence (Fig. 5a). **Shown**
13. By the subspace detailed balance $\mathcal T_{\boldsymbol k\in\mathcal K_i}^{\mathcal K_e,\mathcal K_e}+2\mathcal T_{\boldsymbol k\in\mathcal K_e}^{\mathcal K_i,\mathcal K_e}=0$, the TEM damping implies entropy transfer from low-$k_y$ TEMs to high-$k_y$ modes; the net gain through ion-scale coupling appears at finite $k_x$ ($k_y\rho_{ti}\sim4$, $k_x\rho_{ti}>1$), not at the ETG peaks ($k_x\rho_{ti}\sim0$), and these modes feed still higher-$k_\perp$ fluctuations ($\mathcal T^{\mathcal K_e,\mathcal K_e}>0$ at $k_y\rho_{ti}>7$, not shown) that collisions damp (pp. 4–5, Fig. 5b). **Shown**
14. The ion-scale/electron-scale coupling is negative on the ETG peak ($\mathcal T_{\boldsymbol k}^{\mathcal K_i,\mathcal K_e}<0$ at $k_y\rho_{ti}\sim4$, $k_x\rho_{ti}\sim0$), confirming suppression of ETG by ion-scale turbulence (p. 5). **Shown**
15. The reduction of TEM transport by ETG contrasts with multi-scale ITG/ETG simulations [2] and resembles the suppression of microtearing modes by ETG [5] (p. 4). **Stated**
16. $T_e/T_i$ scan from 1 to 4 (Fig. 6): at $T_e/T_i=1$ ETG is highly unstable and multi-scale transport agrees with the electron-scale-only result; with rising $T_e/T_i$ ETG is stabilized and TEM destabilized; at $T_e/T_i=4$ TEM dominates even in the multi-scale run. The electron-scale run at $T_e/T_i=4$ and the ion-scale runs at $T_e/T_i=1,2$ have no unstable modes and decay. **Shown**
17. Suppression of near-marginal TEM by ETG upshifts the critical temperature ratio for an increase of TEM-dominated flux from $T_e/T_i\sim2$ (ion-scale) to $\sim3$ (multi-scale), analogous to the Dimits upshift of the critical ion temperature gradient by zonal flows [38] (p. 5). **Shown**
18. The ETG contribution survives over $1<T_e/T_i<3$, whereas it may have been thought non-negligible only for $T_e\sim T_i$ with large enough electron temperature [8] (p. 5). **Shown**
19. A reactor-relevant ratio is $1<T_e/T_i<2$ (ITER profile modelling, DIII-D high-$T_e$ discharge [37]); the central $T_e/T_i$ of ITER PFPO-1 can exceed 3 with electron-cyclotron heating [15] (pp. 2, 5–6). **Stated**
20. Across the authors' multi-scale studies, large-scale turbulence tends to suppress small-scale turbulence (ITG/ETG, MTM/ETG, TEM/ETG) and small-scale turbulence tends to destroy large-scale structures (zonal flows, MTM current sheets, TEM drift resonance), a "mutual conjunction" beyond a single-scale injection–cascade–dissipation picture (Discussion). **Stated**
21. Interactions of energetic alpha particles with TEM/ETG are expected to be weak because the propagation directions are opposite [42]; alpha particles are left out of the simulations (Discussion). **Stated**
22. GKV scales to 12,288 Fugaku nodes at 3.1 PFLOPS, 7.5% of theoretical peak, with 83.7% parallel efficiency (Methods). **Stated**
23. Doubling the $|k_y\rho_{ti}|$ boundary between the ion and electron subspaces from 1 to 2 changes the entropy-transfer analysis in no qualitative way (Methods). **Stated** (not shown)

The run set-up (Methods): circular $s$-$\alpha$ geometry with $\alpha=0$,
$\epsilon_a=0.18$, $q_s=1.42$, $\hat s=0.8$; $n_D=n_T=0.45n_e$,
$n_{He}=0.05n_e$; $R_0/L_n=3$ for all species, $R_0/L_{Te}=9.342$,
$R_0/L_{Ti}=1$; $\beta_p=0.05\%$, $\nu_*=0.05$; box
$0\le x/\rho_{ti}<125$, $0\le y/\rho_{ti}<40\pi$; grids
$(N_x,N_y,N_z,N_{v\parallel},N_\mu)=(2048,2048,40,64,16)$ at $T_e/T_i=1$ and
$(1024,1024,40,64,16)$ at $T_e/T_i\ge2$; Fourier spectral in $x,y$ with
2/3 de-aliasing. The single ion-scale runs truncate at
$k_{x,\max}=4\rho_{ti}^{-1}$, $k_{y,\max}=\rho_{ti}^{-1}$, the single
electron-scale runs start at $k_{\min}=0.5\rho_{ti}^{-1}$. No experimental
validation is given.

# Printed slips

- **Subspace label (Methods, p. 7).** "the ion-scale $\Omega_i=\{\mathbf k\,|-4<k_x\rho_{ti}<4,-1<k_y\rho_{ti}<1\}$ and electron-scale $\Omega_i=\{\mathbf k\,|$ the others$\}$": the second set, the electron-scale subspace, is labelled $\Omega_i$; everywhere else it is $\Omega_e$.
- **Typo (p. 5).** "characterised by a peak of energy specrum".
- **Phase velocities (Results, p. 2)** *(compiler check, not in the sources)*. With the printed $k_{\mathrm{tor}}=\epsilon_ak_y/q_s$, $\epsilon_a=0.18$, $q_s=1.42$, the printed TEM values $\omega_r=1.50$, $k_y=0.25$ give $\omega_r/k_{\mathrm{tor}}=1.50\times1.42/(0.18\times0.25)=47.3$, not the printed 42.7; the ETG values $\omega_r=24.3$, $k_y=4.5$ give $24.3\times1.42/(0.18\times4.5)=42.6$, not the printed 45.1 (units $v_{ti}\rho_{ti}/R_0$). The printed 42.7 does agree with the resonance claim: with $v_{\mathrm{pre}}\propto v^2$ and the printed $v_{\mathrm{pre}}(2v_{te})=47.3$, $v_{\mathrm{pre}}(1.9v_{te})=47.3\times0.95^2=42.7$. The paper does not say how the phase velocities were computed.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\gamma$ | $\gamma_{\mathrm{lin}}$ (page-local linear growth rate) | **collision:** registry $\gamma$ is the ratio of specific heats |
| $\omega_r$ | $\omega_r$ (page-local real frequency) | **collision** with the specific dissipation rate $\omega$; the subscript keeps it apart |
| $\varepsilon_r=r/R_0$ | $\epsilon_a$ (page-local inverse aspect ratio) | **collision** with the dissipation rate $\varepsilon$ |
| $\beta=\mu_0n_eT_D/B_0^2$ | $\beta_p$ | plasma beta, 0.05% |
| $\lambda$ ($\lambda^2=\varepsilon_0B_0^2/(m_in_e)$) | $\lambda_{De}$ (page-local normalized Debye length) | **collision** with the Taylor microscale and the MHD perpendicular scale $\lambda$ |
| $\Omega_i$, $\Omega_e$ | $\mathcal K_i$, $\mathcal K_e$ (page-local ion- and electron-scale wavenumber subspaces) | **collision** with the rotation-rate tensor $\Omega_{ij}$ |
| $J_{\mathbf k}^{\mathbf p,\mathbf q}$, $J_{\mathbf k}^{\Omega_s,\Omega_{s'}}$ | $\mathcal T_{\boldsymbol k}^{\boldsymbol p,\boldsymbol q}$, $\mathcal T_{\boldsymbol k}^{\mathcal K_s,\mathcal K_{s'}}$ (page-local triad and subspace entropy-transfer functions) | positive = entropy gain of mode $\boldsymbol k$ |
| $\mu$ | $\mu_m$ (page-local magnetic moment) | **collision** with the dynamic viscosity $\mu$ |
| $\langle\cdot\rangle_\theta$; $\langle\cdot\rangle$ on $\phi$ | (flux-surface average; gyrophase average) | neither is a Reynolds average |
| $x,y,z$ | (field-aligned flux-tube coordinates, $z=\theta$) | not the registry's streamwise, wall-normal, spanwise axes |
| $k_x,k_y,k_\perp,k_{\mathrm{tor}}$ | (radial, binormal, perpendicular, toroidal wavenumbers) | $k_{\mathrm{tor}}=\epsilon_ak_y/q_s$ |
| $q$, $\hat s$ | $q_s$, $\hat s$ (page-local safety factor, magnetic shear) | |
| $\rho_{ti}$, $v_{ti}$, $\rho_{te}$, $v_{te}$ | (ion and electron thermal gyroradius and speed) | thermal-speed convention not printed |
| $T_e$, $T_i$ | (electron and ion temperatures) | $T$ in the registry is the fluid temperature |
| $Q_e$, $Q_{gB}=n_eT_ec_a\rho_a^2/R_0^2$ | (electron heat flux, gyro-Bohm unit) | |
| $\nu_*$ | (normalized collisionality) | not a viscosity |
| $f_s$, $g_{e\mathbf k}$, $F_{eM}$ | (perturbed distribution, its non-adiabatic part, Maxwellian) | |
| $\phi$, $A_\parallel$, $\chi_{\mathbf k}$ | (electrostatic potential, parallel vector potential, generalized potential) | |

# Reference list

51 printed references, numbered (Nature style), titles printed for all. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [51] is the authors' code and data deposit for
this paper (GitHub and Zenodo DOI 10.5281/zenodo.6541253); it is a
different work from the article and is kept as its own `@misc` entry,
`maeyama-2022-b`. Same-author same-year pairs take suffixes in printed
order (`maeyama-2015`/`-b`, `maeyama-2017`/`-b`). Ref. [22] is the
existing entry `schekochihin-2009`. No printed duplicates or unparseable
items.

# Pages created or updated

Chunk 3 (2026-10-26). This source is cited on:

- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Cross-scale interaction in plasma turbulence](/results/cross-scale-interaction.md)
