---
type: Result
title: "Kinetic thermal ions confine LHD pressure-driven activity to the periphery"
description: "In high-beta inward-shifted LHD equilibria, conventional MHD (MIPS) predicts a core collapse by peripheral resistive ballooning modes at moderate Lundquist number and by a resonant (3,2) ideal interchange at high Lundquist number, whereas MEGA with drift-kinetic thermal ions lowers the growth rates through the poloidal precession of helically trapped ions and keeps the nonlinear activity peripheral with the central pressure maintained at S = 10^7, as observed; energetic ions up to 0.8 % beta lower the linear growth rate without changing saturation."
status: established
aliases: [LHD high-beta kinetic stabilization, KTI stabilization of LHD, trapped-ion precession stabilization]
tags: [stellarator, hybrid-kinetic, ballooning, mhd, particles, energetic-particles]
timestamp: 2026-10-16T20:00:00Z
---

# Kinetic thermal ions confine LHD pressure-driven activity to the periphery

LHD experiments sustain volume-averaged $\beta\approx5\,\%$ in
inward-shifted configurations without significant MHD activity, whereas
fixed-boundary linear MHD predicts strong instability; free-boundary ideal
MHD, nonlinear MHD, two-fluid and equilibrium-flow models had not
reconciled the two ([Sato & Todo (2026)](/sources/sato-2026.md),
Introduction). Sato & Todo review their MHD study (Sato et al. 2017) and
three kinetic-thermal-ion studies (Sato & Todo 2019, 2020, 2021), none of
them ingested, and add new runs with energetic ions. Their conclusion is
that the missing physics is the kinetic response of thermal ions, not a
further fluid effect. This page records the result as the review states
it; figures reproduced from the earlier papers are cited by their number
in the review.

## Setup

* **Equilibria.** [HINT](/software/hint.md) equilibria, without the
  nested-surface assumption, with $p=p_0(1-\psi_{t,N})$ and
  $\beta_0=7.5\,\%$ and $9.2\,\%$; a stochastic region outside the last
  closed surface; a Mercier-stable core (magnetic well from the Shafranov
  shift) and a Mercier-unstable outer region (magnetic hill) (p. 3, Fig. 1;
  see [interchange modes](/definitions/interchange-mode.md)).
* **Models.** [MIPS](/software/mips.md) for conventional single-fluid
  visco-resistive MHD; [MEGA](/software/mega.md) with drift-kinetic
  $\delta f$ thermal ions ([kinetic thermal ions](/methods/kinetic-thermal-ions.md)).
  The MEGA KTI model does not reduce to MHD when the kinetic ions are
  switched off, because density and parallel velocity are moments of the
  ion distribution; hence the use of two codes (p. 2). No ion diamagnetic
  term and no finite-Larmor-radius effects (FLR is available in MEGA but
  switched off "to isolate the dominant stabilization mechanism") (p. 2).
* **Lundquist number.** $S=\mu_0R_0^2/(\eta\tau_A)$ with
  $\tau_A=R_0/v_A$; simulations span $10^4\le S\le10^7$. The experimental
  value, converted to this definition, is stated as
  $2\times10^7\lesssim S\lesssim5\times10^7$, "of the same order" as the
  highest simulated value; the conversion factor is not given (p. 3).
* **Dissipation and resolution.** $\nu=\kappa=10^{-7}v_AR_0$ in the
  earlier studies, anisotropic $\kappa_\perp=10^{-7}$ and
  $\kappa_\parallel=10^{-3}v_AR_0$ in the 2021 study (diffusivities,
  normalized); MIPS $256\times640\times256$ and MEGA $128\times640\times128$
  points in $(R,\phi,Z)$ with about $6.7\times10^8$ thermal-ion markers
  (p. 3).

## Conventional MHD: core collapse

* **Moderate $S$.** For $10^4\le S\le10^6$ the most unstable modes are
  resistive [ballooning modes](/definitions/ballooning-mode.md) of
  "2D type", weakly coupled toroidally within the ten-period
  [mode families](/definitions/toroidal-mode-family.md), so that the
  toroidal mode number identifies an eigenmode (p. 4). At $S=10^5$ they
  start in the periphery, dominant $n=12,13$ ($\beta_0=7.5\,\%$) and
  $n=11,10$ ($\beta_0=9.2\,\%$); their nonlinear interaction generates
  low-$n$ modes such as $n=1$ that reach the core, and the quadratic
  coupling of the $n=1$ velocity and pressure perturbations builds a
  $(m,n)=(0,0)$ pressure drop that collapses the core, by
  $t\approx147\tau_A$ at $\beta_0=7.5\,\%$ (pp. 4–5, Figs. 2–3).
* **High $S$.** For $S>10^6$ a resonant $(3,2)$ ideal interchange mode on
  the $\iota=2/3$ surface dominates, extends toward the core and collapses
  it, by $t=3326\tau_A$ at $S=10^7$ (p. 5, Fig. 7). The authors contrast it
  with the non-resonant $m=n>1$ interchange of a tokamak sawtooth-like
  crash (Jardin et al. 2020, as cited).

## Kinetic thermal ions: linear stabilization

Growth rates read from Fig. 4 (after Sato & Todo 2021), in units of
$\tau_A^{-1}$:

| $S$ | MHD | MHD mode | KTI |
|---|---|---|---|
| $10^4$ | $\approx0.11$ | resistive ballooning | $\approx0.11$ |
| $10^6$ | $\approx0.015$ | resistive ballooning | $\approx0.004$ |
| $2\times10^6$–$10^7$ | $\approx0.009$–$0.01$ | $(3,2)$ interchange | down to $\approx5\times10^{-4}$ at $10^7$ |

The figure's guide lines scale as $S^{-1/3}$ for MHD resistive ballooning
and $S^{-1}$ for KTI (pp. 6–7). The mechanism the authors give:

* **Poloidal precession of helically trapped ions.** Ions deeply trapped
  in the helical ripples precess both toroidally and poloidally in LHD
  (only toroidally in a tokamak). For perturbations of short poloidal
  wavelength, fast precession carries them across positive and negative
  fluctuations, which "effectively average out the perturbations" and
  weaken the perpendicular ion-pressure response (pp. 6–7, Fig. 5).
* **Selective suppression of $\delta p_{\perp i}$.** For an $n=6$
  ballooning mode, $\delta p_{\perp i}$ peaks at about 5 % and
  $\delta p_{\parallel i}$ at about 15 % of the dominant $m=8$ harmonic of
  $\delta p_e$, trapped ions dominating $\delta p_{\perp i}$ (p. 7, Fig. 6).
  The text puts this case at $S=10^5$, the Fig. 5 and 6 captions at
  $S=10^6$ (recorded on the Source page).
* **Criterion $\gamma$ against $\omega_{\mathrm d}$.** With $\omega_{\mathrm d}$ (registry §11)
  the precession frequency of a typical trapped ion relative to the mode
  phase, and a nearly purely growing mode, stabilization is weak while
  $\omega_{\mathrm d}<\gamma$ ($S\sim10^4$, $\omega_{\mathrm d}\tau_A\approx0.07$–$0.09$) and
  strong once $\gamma$ falls below $\omega_{\mathrm d}$ as $S$ rises. The ideal
  $(3,2)$ interchange has $\gamma<\omega_{\mathrm d}$ ($\omega_{\mathrm d}\tau_A\approx0.03$)
  and is stabilized, after which "the resistive interchange mode remains
  the dominant unstable mode" (p. 7, Fig. 4).

## Kinetic thermal ions: nonlinear outcome

* At $S=10^5$ the slightly lower KTI growth rate does not prevent the
  degradation of the central pressure; both models lose it (pp. 7–8).
* At $S=10^7$ MHD collapses the core (Fig. 7), whereas with KTIs the
  activity stays in the periphery up to $t=84\,811\tau_A$ and the central
  pressure is maintained (Fig. 8), "better agreement with experimental
  observations" (pp. 7–8).
* In the saturated KTI state the $(0,0)$ perturbation of $p_{\perp i}$ is
  "significantly suppressed" relative to $p_e$ and $p_{\parallel i}$; the
  KTI $(0,0)$ pressure profile stays close to the initial one, while the
  MHD profile at $t=3326\tau_A$ is flattened inside a radial label of
  about 0.6 (the label is not defined in the source) (p. 8, Fig. 9).

## Energetic ions (new in the review)

At $S=10^7$, $\beta_0=7.5\,\%$, with Maxwellian 100 keV energetic ions
(p. 8, Figs. 10–12):

* the linear growth rate of the $n=2$ interchange decreases with $\beta_h$,
  from about $4.9\times10^{-4}$ at $\beta_h=0$ to about $3.6\times10^{-4}$
  at $\beta_h=0.8\,\%$ (figure reading, axis units not printed),
  attributed to the lower bulk-pressure drive at fixed total pressure, as
  Pinon et al. (2018, as cited) also found;
* the energetic-ion perpendicular pressure response is negligible,
  "likely due to" an energetic-ion precession frequency far above $\gamma$;
* $n=2$ saturates at nearly the same level, the weakly unstable $(1,1)$
  interchange then grows and dominates in both cases, and the saturated
  $(0,0)$ total-pressure profiles at $\beta_h=0$ and $0.8\,\%$ do not differ
  significantly. Re-destabilization above a threshold $\beta_h$ (Pinon et
  al. 2018) is not explored (p. 9).

## Scope and caveats

* **Generality claimed.** The authors trace the stabilization to the
  deviation of particle orbits from field lines (finite orbit width), "may
  become particularly important in plasmas near the beta limit, where
  instabilities grow slowly", and conclude that "the conventional MHD model
  may be insufficient" for beta-limit assessment (Summary, p. 10).
* **Core density collapse.** The core density collapse observed in LHD has
  been linked to fast ideal-ballooning-type modes with possibly
  $\gamma>\omega_{\mathrm d}$, where the kinetic stabilization is weaker; the absence
  of collapse in the KTI runs "does not rule out CDC-related mechanisms"
  (p. 8).
* **Missing physics.** No ion or electron diamagnetic effects and no FLR;
  FLR "may quantitatively modify growth rates but are not expected to
  alter the primary stabilization mechanism" (p. 2, stated, not tested).
* **Not a code-to-code result.** No benchmark or convergence study is
  reported in the review; the nonlinear KTI run took 2048 SX-Aurora vector
  engines for about 164 h (p. 3).

## Relation to other results

* **Tokamak counterpart.** For $n=3$ infernal modes in a tokamak, kinetic
  thermal ions in MEGA likewise lower slow growth rates and suppress the
  resistive beta collapse, but through a phase shift of the ion-pressure
  response rather than an amplitude reduction
  ([Sato et al. (2024)](/sources/sato-2024.md), §3–4; see
  [infernal mode](/definitions/infernal-mode.md)). The two papers, by the
  same group, state this difference of mechanism between geometries.
* **W7-AS.** [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) obtain
  mild, edge-confined pressure-driven activity in W7-AS within reduced MHD
  at low resistivity. The contrast with the LHD MHD collapse is discussed,
  as a compiler's observation, on [soft β limit](/definitions/soft-beta-limit.md).

## Contradictions

None stated within the bundle. The review's claim that conventional MHD
fails for LHD is directed at MHD studies it cites (Nakajima et al.
2004/2006; Miura & Nakajima 2010; Sato et al. 2017), none ingested.

# Citations

* [Sato & Todo (2026)](/sources/sato-2026.md) — the whole result: equilibria, MHD collapse, linear and nonlinear KTI stabilization, the $\gamma$–$\omega_{\mathrm d}$ criterion, energetic ions, caveats.
* [Sato et al. (2024)](/sources/sato-2024.md) — tokamak infernal-mode counterpart.
* [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — W7-AS reduced-MHD contrast.
