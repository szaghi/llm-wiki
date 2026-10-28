---
type: Result
title: "Cross-scale interaction in plasma turbulence"
description: "In magnetized fusion plasmas, ion-scale and electron-scale micro-turbulence interact across scales; multi-scale gyrokinetic simulation at electron-to-ion temperature ratio 3 shows mutual suppression of trapped-electron and electron-temperature-gradient turbulence, reducing the electron heat flux from 33.63 to 5.66 gyro-Bohm units against an ion-scale-only simulation."
status: established
aliases: [multi-scale plasma turbulence, cross-scale coupling, TEM/ETG interaction, ion-scale/electron-scale interaction, scale separation assumption]
tags: [plasma, dns, energy-cascade]
timestamp: 2026-10-28T07:05:00Z
---

# Cross-scale interaction in plasma turbulence

Turbulence in a magnetized fusion plasma is driven by micro-instabilities at
two widely separated scales: ion-scale modes at the ion gyroradius and
electron-scale modes at the much smaller electron gyroradius. **Cross-scale interaction** is the
nonlinear coupling between the two. [Maeyama et al.
(2022)](/sources/maeyama-2022.md) note that conventional turbulent-transport
modelling treats the two separately — a **scale-separation assumption** —
and is designed to reproduce ion-scale transport, so it lacks these
interactions (Abstract, Introduction). They show by multi-scale gyrokinetic
simulation that in a plasma with electron temperature above the
ion temperature, the regime of electron-heated phases of ITER and of
alpha-heated burning plasma, the interaction reduces the electron heat
flux ($5.66$ against $33.63\,Q_{gB}$ at $T_e/T_i=3$), and conclude that cross-scale interactions must be taken
into account in burning-plasma predictions (Discussion).

Page-local notation: $T_e$, $T_i$ are the electron and ion temperatures
(deuterium, tritium and helium share $T_i$); $\rho_{ti}$ and $v_{ti}$ the ion
thermal gyroradius and speed (subscripted; never the density); $R_0$ the
major radius; $k_x$, $k_y$ the radial and binormal wavenumbers of the flux
tube and $k_\perp$ their magnitude; $\omega_r$ and $\gamma_{\mathrm{lin}}$
the real frequency and linear growth rate; $Q_e$ the electron heat flux and
$Q_{gB}$ the gyro-Bohm unit; TEM is the trapped electron mode (ion scale),
ETG the electron temperature gradient mode (electron scale).

## Simulation

Maeyama et al. (2022, Methods) solve the delta-$f$ electromagnetic
gyrokinetic Vlasov–Poisson–Ampère equations in five-dimensional phase space
with the open-source code GKV in a local flux tube (field-aligned
coordinates, periodic in the perpendicular plane "along with homogeneous
turbulence in fluids", Fourier spectral there with 2/3 dealiasing). Four
species (electrons, deuterium, tritium, helium ash), circular $s$-$\alpha$
geometry with inverse aspect ratio 0.18, safety factor 1.42 and magnetic
shear 0.8, normalized gradients $R_0/L_n=3$, $R_0/L_{Te}=9.342$,
$R_0/L_{Ti}=1$ ($L_n$, $L_T$ gradient lengths, page-local), plasma beta
0.05% and normalized collisionality 0.05. The multi-scale grid,
$(N_x,N_y,N_z,N_{v_\parallel},N_\mu)=(1024,1024,40,64,16)$ for
$T_e/T_i\ge2$ and $(2048,2048,40,64,16)$ for $T_e/T_i=1$, resolves
$0.05\le k_{x,y}\rho_{ti}\le16.95$ (33.9 for $T_e/T_i=1$). Comparison runs
truncate the spectrum: single ion-scale runs keep $k_x\rho_{ti}\le4$,
$k_y\rho_{ti}\le1$; single electron-scale runs keep
$k_{x,y}\rho_{ti}\ge0.5$. The authors report that GKV scales to 12,288 nodes
of the Fugaku supercomputer at 3.1 PFLOPS, 7.5% of peak, with 83.7% parallel
efficiency (Methods; no data shown). The paper does not use the term
[DNS](/definitions/direct-numerical-simulation.md); the entropy injected by
the gradients balances "the collisional dissipation in a steady state"
(Methods, p. 7).

## Mutual suppression at $T_e/T_i=3$

- **Linear drives** (Results, Fig. 1). The most unstable TEM is at
  $k_y\rho_{ti}=0.25$ with $\omega_r=1.50$ and
  $\gamma_{\mathrm{lin}}=0.145$, the most unstable ETG at $k_y\rho_{ti}=4.5$
  with $\omega_r=24.3$ and $\gamma_{\mathrm{lin}}=1.16$, in units of
  $v_{ti}/R_0$. The authors state that the two have similar toroidal phase
  velocities (see Qualifications).
- **Heat fluxes** (Results, Fig. 4):

  | Simulation | $Q_e/Q_{gB}$ | $(Q_D+Q_T)/Q_{gB}$ | $Q_{He}/Q_{gB}$ |
  |---|---|---|---|
  | multi-scale TEM/ETG | 5.66 | 0.24 | 0.02 |
  | single ion-scale TEM | 33.63 | 1.11 | 0.09 |

  The low-$k_y$ TEM part of the flux spectrum is reduced in the multi-scale
  run, while its high-$k_y$ ETG peak coincides with that of the
  electron-scale-only run. Small ETG eddies coexist with the large TEM
  fluctuations, and no strong zonal flows appear.
- **Small scales disturb large-scale transport.** Tracer electrons followed
  in the simulated $E\times B$ field show that a trapped electron in
  toroidal-precession resonance with the TEM drifts radially, an
  off-resonant one does not, and the ETG fluctuations disturb the resonant
  trajectory (Fig. 2); velocity-space-resolved fluxes localize the
  transport on the resonant trapped electrons (Fig. 3c).
- **Large scales suppress small-scale turbulence.** In the electron-scale-only
  run, ETG-driven zonal flows suppress transport after
  $tv_{ti}/R_0\ge50$ (stated, not shown); in the multi-scale run there are
  no significant zonal flows, so the authors attribute ETG suppression to
  shearing by TEM eddies themselves — in contrast to the earlier work they cite
  (Asahi et al. 2014), which attributes it to TEM-driven zonal flows (Results).

## Entropy-transfer diagnosis

The interaction is quantified with gyrokinetic nonlinear entropy transfer
(after the authors' earlier work, which they cite). For a triad
$\boldsymbol k+\boldsymbol p+\boldsymbol q=0$ the transfer function
$\mathcal T_{\boldsymbol k}^{\boldsymbol p,\boldsymbol q}$ (page-local; the
source writes $J$) is the entropy gained by mode $\boldsymbol k$ through the
quadratic $E\times B$ nonlinearity, positive for gain (Eq. 4), and it obeys
the detailed balance

$$\mathcal T_{\boldsymbol k}^{\boldsymbol p,\boldsymbol q}+\mathcal T_{\boldsymbol p}^{\boldsymbol q,\boldsymbol k}+\mathcal T_{\boldsymbol q}^{\boldsymbol k,\boldsymbol p}=0,$$

which "ensures entropy conservation" (Methods, p. 7).
Summing over the ion-scale wavenumber subspace
$\mathcal K_i=\{\boldsymbol k:|k_x\rho_{ti}|<4,\ |k_y\rho_{ti}|<1\}$ and its
complement $\mathcal K_e$ (page-local; the source writes $\Omega_i$,
$\Omega_e$) gives subspace transfers
$\mathcal T_{\boldsymbol k}^{\mathcal K_s,\mathcal K_{s'}}$ with the balance
$\mathcal T_{\boldsymbol k\in\mathcal K_i}^{\mathcal K_e,\mathcal K_e}+2\mathcal T_{\boldsymbol k\in\mathcal K_e}^{\mathcal K_i,\mathcal K_e}=0$
(Eq. 5, Methods). Findings (pp. 4–5, Fig. 5):

- $\mathcal T^{\mathcal K_e,\mathcal K_e}<0$ at $k_y\rho_{ti}<0.5$: electron-scale
  coupling directly damps the TEMs.
- By the balance, that entropy goes to high-$k_y$ modes, but the net gain
  through ion-scale coupling appears at finite $k_x$
  ($k_y\rho_{ti}\sim4$, $k_x\rho_{ti}>1$), not on the ETG peaks
  ($k_x\rho_{ti}\sim0$); those modes feed still higher $k_\perp$
  ($\mathcal T^{\mathcal K_e,\mathcal K_e}>0$ at $k_y\rho_{ti}>7$, not
  shown), eventually damped by collisions.
- $\mathcal T^{\mathcal K_i,\mathcal K_e}<0$ on the ETG peak: ion-scale
  turbulence suppresses ETG.

Doubling the subspace boundary in $|k_y\rho_{ti}|$ from 1 to 2 gives no
qualitative difference (Methods, not shown).

## Dependence on the temperature ratio

A scan $1\le T_e/T_i\le4$ (Fig. 6): at $T_e/T_i=1$ ETG is strongly unstable
and the multi-scale transport matches the electron-scale-only result; raising
$T_e/T_i$ stabilizes ETG and destabilizes TEM, and at $T_e/T_i=4$ TEM
dominates even in the multi-scale run. Suppression of the near-marginal TEM
by ETG upshifts the temperature ratio at which TEM-dominated flux rises from
$T_e/T_i\sim2$ (ion-scale run) to $\sim3$ (multi-scale run), which the
authors liken to the Dimits upshift of the critical ion temperature gradient
by zonal flows (ref. [38], which they cite). The ETG contribution survives over
$1<T_e/T_i<3$, a wider range than previously thought (Results, p. 5). The
authors place reactor-relevant ratios at $1<T_e/T_i<2$ and note that ITER's
first pre-fusion plasma operation can exceed 3 with electron cyclotron
heating (pp. 2, 5–6).

## A generic pattern

From their own multi-scale studies (ITG/ETG, microtearing/ETG, TEM/ETG),
Maeyama et al. (2022, Discussion) draw a synthesis: large-scale turbulence
tends to suppress small-scale turbulence, while small-scale turbulence tends
to destroy large-scale structures (zonal flows, current sheets, resonances),
a "mutual conjunction" beyond the single-scale picture of injection, cascade
and dissipation. They note that TEM reduction by ETG contrasts with the
earlier ITG/ETG multi-scale results but resembles the suppression of
microtearing modes by ETG reported in the work they cite, and that alpha particles, excluded
here, are expected to interact weakly because they propagate in the opposite
direction.

## Qualifications

- **One configuration.** The evidence is one flux-tube configuration with a
  temperature scan, compared with the authors' own single-scale runs; there
  is no experimental validation. The authors cite Alcator C-Mod work (ref. [3],
  Howard et al., titled "Enhanced heat loss due to cross-scale coupling")
  and state that they study the regime
  $T_e>T_i$, $R_0/L_{Te}>R_0/L_{Ti}$, "which has not yet been analysed in
  existing devices" (Methods, p. 6).
- **Printed phase velocities.** The text gives toroidal phase velocities
  $\omega_r/k_{\mathrm{tor}}=42.7$ (TEM) and $45.1$ (ETG) in units of
  $v_{ti}\rho_{ti}/R_0$, with $k_{\mathrm{tor}}=\epsilon_ak_y/q_s$
  ($\epsilon_a=0.18$ the inverse aspect ratio, $q_s=1.42$ the safety factor,
  page-local). *(Compiler check, not in the sources: the printed most-unstable
  values give $1.50\times1.42/(0.18\times0.25)=47.3$ for TEM and
  $24.3\times1.42/(0.18\times4.5)=42.6$ for ETG; the printed 42.7 equals the
  precession velocity at $v=1.9v_{te}$ ($v_{te}$ the electron thermal speed) obtained by scaling the printed
  $47.3$ at $2v_{te}$ by $(1.9/2)^2$, with the printed $v_{\mathrm{pre}}\propto v^2$ of deeply trapped electrons (Results, p. 2). The paper does not say at which
  wavenumbers the phase velocities were taken.)*
- **Printed slip** (Methods, p. 7). The electron-scale subspace is printed
  "$\Omega_i=\{\mathbf k\,|$ the others$\}$"; it is $\Omega_e$, as used
  everywhere else.
- The paper calls the subspace detailed balance an "energy conservation
  relation" (Results, p. 4) and the subspace transfer "the energy gain or
  loss" (Methods, p. 7), while it states that the triad balance "ensures
  entropy conservation" (Methods, p. 7).

# Citations

- [Maeyama et al. (2022)](/sources/maeyama-2022.md) — Abstract; Introduction; Results, pp. 2–5, Figs. 1–6; Discussion; Methods, Eqs. (1)–(5), pp. 6–7.
