---
type: Definition
title: "Fishbone instability"
description: "Energetic-particle-modified n = 1 internal kink that acquires a finite real frequency through resonance with trapped energetic particles; benchmarked linearly by M3D-C1-K against M3D-K and NIMROD, and, in its non-resonant form at q_min slightly above 1, shown to be raised in frequency, reduced in growth and partly stabilized by thermal-ion Landau damping."
status: established
aliases: [fishbone, fishbone mode, energetic-particle-driven internal kink, non-resonant fishbone]
tags: [energetic-particles, hybrid-kinetic, kink, tokamak]
timestamp: 2026-10-16T20:00:00Z
---

# Fishbone instability

The fishbone is the $n=1$ internal kink modified by energetic particles
(EPs). Without EPs the $m/n=1/1$ mode is an ideal or
[resistive internal kink](/definitions/resistive-internal-kink.md) with zero
real frequency. As the EP share of the pressure grows, the mode changes
character. It acquires a finite real frequency $\omega$, and its growth is
driven by resonance with trapped EPs
([Liu et al. (2022)](/sources/liu-2022.md), §6.1).

## The linear transition from kink to fishbone

The M3D-C1-K benchmark follows the setup of Fu et al. (2006) for M3D-K, also
used by Kim et al. (2008) for NIMROD
([Liu et al. (2022)](/sources/liu-2022.md), §6.1):

- **Geometry and plasma.** Circular tokamak with $R_0=1$ m,
  $a=0.361925$ m, $B=1$ T and hydrogen at uniform
  $n_i=2.489\times10^{20}$ m$^{-3}$. The pressure is
  $p=p_0\exp(-\psi_N/0.25)$ with $p_0=16335$ Pa, which gives a central
  $\beta=8\%$.
- **Safety factor.** $q_0=0.6$, so the $q=1$ surface lies inside the plasma.
- **EPs.** The EP density has the same shape as $p$. The distribution is an
  isotropic slowing-down $f_0\propto H(v_0-v)/(v^3+v_c^3)$ ($v$ the particle speed, $H$ the Heaviside step) with
  $v_0=3.9\times10^6$ m/s and $v_c=0.58v_0$. The EP mass is reduced to
  $0.11m_{\mathrm H}$ to match $\rho_L/a=0.0125$.
- **Physics options.** No FLR. Markers are loaded on the local $\psi$, not
  the orbit-averaged $\psi$ of Fu et al.

The scan holds the total pressure fixed and raises the EP share
$\beta_h/\beta$ from 0 to 0.75 (Fig. 3):

- the mode changes from an ideal kink at $\beta_h/\beta=0$ to a fishbone
  with finite real frequency;
- $\gamma\tau_A$ falls from about 0.025 to a minimum of about 0.021 near
  $\beta_h/\beta=0.25$, then rises to about 0.028 at 0.75;
- $\omega\tau_A$ rises roughly linearly with $\beta_h/\beta$, to about 0.030
  at 0.75 (values read off the plot; $\tau_A$ is not defined in the paper).

The non-adiabatic EP response $\delta p_{\perp h}-\delta p_{\parallel h}$ is
localized on the low-field side. The paper reads this as evidence of
trapped-particle resonance, and the mode structure is "consistent with" the
NIMROD result (§6.1, Fig. 4). Pressure coupling and current coupling give
nearly identical $\gamma$ and $\omega$ (Fig. 3; see
[pressure and current coupling](/methods/pressure-and-current-coupling.md)).

## Non-resonant fishbones and thermal-ion Landau damping

When $q_{\min}$ lies slightly above 1, the $m/n=1/1$ mode has no $q=1$
surface. In MHD alone it is the so-called non-resonant kink, whose growth
rate depends strongly on $\beta$, "similar to pressure-driven modes"; with
EPs it becomes a non-resonant fishbone
([Liu et al. (2022b)](/sources/liu-2022-b.md), §4, Fig. 10).
Liu et al. scan $q_{\min}$ in M3D-C1-K for a DIII-D hybrid equilibrium
(#125476, $q_{\min}$ varied by adding a constant to $F^2$ at fixed $p$ and
toroidal current) and an NSTX equilibrium (#134020, $q_{\min}$ varied by
the plasma current at almost fixed $\beta$), each in three models: MHD
only, EPs only, and EPs plus [kinetic thermal ions](/methods/kinetic-thermal-ions.md)
(§§4–5, Figs. 5, 13). Growth rates in DIII-D are in units of
$\tau_A^{-1}$, which the paper does not define; values are figure readings.

- **MHD only.** The DIII-D $n=1$ kink is unstable for $q_{\min}<1.06$
  ($\gamma\tau_A\approx0.026$ at $q_{\min}=1.00$). In NSTX the threshold is
  higher, near 1.24, "thanks to the larger β".
- **EPs only.** The growth rate falls and the real frequency rises with
  $q_{\min}$ (fishbone-like branch). Above $q_{\min}\approx1.1$ in DIII-D
  ($\approx1.2$ in NSTX) a weakly unstable EP-driven mode with much higher
  frequency remains, which the authors call **BAE-like** (beta-induced
  Alfvén eigenmode-like).
- **EPs plus kinetic thermal ions.** Fishbone frequencies increase, growth
  rates decrease (DIII-D $\gamma\tau_A\approx0.013$ at $q_{\min}=1.00$, about
  half the EP-only value), the mode is stable for $q_{\min}>1.06$ in DIII-D
  and $>1.22$ in NSTX, and the BAE-like branch is stabilized. The estimate
  $\omega/k_\parallel\approx0.2$–$1.15\,v_{th,i}$ for
  $q_{\min}=1.04$–1.15, with $k_\parallel\approx(n-m/q_{\min})/R$, places
  both branches in the range of ion Landau damping (Eq. 4.2). The authors
  conclude that kinetic-MHD simulations of non-resonant fishbones without
  kinetic thermal ions risk "false positive results" and should be
  revisited (§§4, 7).
- **$\beta$ dependence.** At fixed $q_{\min}=1.04$ the MHD-only growth rate
  rises from 0 at $\beta/\beta_{\mathrm{exp}}=0.8$ to
  $\gamma\tau_A\approx0.021$ at 1.2; with kinetic ions the $\beta$
  dependence weakens and the frequency is almost independent of $\beta$
  (Fig. 10).
- **Which particles drive.** In NSTX the frequency rise with kinetic thermal
  ions is attributed to the isotropic thermal ions supplying a large trapped
  population, which the co-passing-dominated NUBEAM EPs lack, while the
  growth falls "because of Landau damping" (§5). This qualifies the
  trapped-EP drive of the benchmark case above: in this case trapped
  *thermal* ions contribute. The paper does not separate the drive and
  damping roles by a power-transfer analysis (recorded on the Source page).
- **Comparison with experiment.** The simulated DIII-D fishbone-like
  frequency at $q_{\min}=1.04$ is 6.13 kHz, called "consistent" with the
  measured 18 kHz lab-frame frequency and about 21 kHz rotation; the
  arithmetic plasma-frame difference is about 3 kHz and the Doppler sign
  convention is not stated (§4; recorded on the Source page). In NSTX the
  $m=1$ mode is marginally unstable for $1.1<q_{\min}<1.2$ with kinetic
  thermal ions, close to the observed plasma-frame frequency below 5 kHz (§5).

## Nonlinear studies

JOREK's full-$f$ EP model, coupled through anisotropic pressure, has so far
been verified only linearly. Nonlinear applications "to fishbone
instabilities and other phenomena" are listed as in progress
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.2). Liu et al. name
long-time nonlinear EP physics as the intended use of M3D-C1-K, including
"kink/tearing with EPs" ([Liu et al. (2022)](/sources/liu-2022.md), §7).
That intended use has a first instance: a nonlinear M3D-C1-K run of the
NSTX non-resonant fishbone at $q_{\min}=1.12$ with kinetic thermal and fast
ions (8 toroidal planes, $16\times10^6$ markers, Perlmutter A100 GPUs)
([Liu et al. (2022b)](/sources/liu-2022-b.md), §6, Figs. 15–16). The $n=1$
mode saturates at about 0.5 ms with peak $\delta B/B\approx1.5\times10^{-2}$;
$n=0$ is excited by mode coupling and keeps growing after saturation; the
magnetic axis shifts; $(1,1)$ and $(2,1)$ islands form, "consistent with
the experimental observation". The core EP density drops by only about 5%:
the gradient survives because the Landau-damped mode "requires a finite
radial gradient to excite".

## Code-to-code spread

M3D-C1-K's growth rates agree with M3D-K and NIMROD over the whole scan.
Its real frequency does not at large $\beta_h/\beta$. The paper states the
exception ("except for the mode real frequency at large
$\beta_h/\beta_{total}$"). Read off Fig. 3b, M3D-C1-K's $\omega\tau_A$ is
15–20% below the other two codes at $\beta_h/\beta=0.5$–0.75: about 0.022
against 0.026–0.028 at 0.5, and about 0.030 against 0.035–0.036 at 0.75
([Liu et al. (2022)](/sources/liu-2022.md), §6.1). The paper does not
attribute the gap. The one setup difference it records is the local-$\psi$
loading of markers in place of Fu et al.'s orbit-averaged $\psi$. Repeating
the scan with orbit-averaged loading would test that candidate.

## Contradictions

**Growth rate of the BAE-like branch at large $q_{\min}$ (DIII-D, EPs
only).** Open.
[Liu et al. (2022b)](/sources/liu-2022-b.md) (§4, Fig. 5) find
frequencies and growth rates "close to the NIMROD results in Brennan et al.
(2012)", as cited, "except that the growth rate for $q_{\min}>1.1$ keeps
dropping to zero as $q_{\min}$ increases, whereas in Brennan et al. (2012)
the growth rate is almost a constant for large $q_{\min}$". The M3D-C1-K
side is shown ($\gamma\tau_A\approx0.0013$ at 1.10, about 0.0005 at 1.15);
the NIMROD side is known only as restated, since Brennan et al. (2012) is
not ingested and no NIMROD curve is plotted. No cause is offered. Candidate
differences to test: the equilibrium $q$-scan method, the EP distribution
model and the treatment of continuum damping; a rerun of both codes on one
equilibrium sequence would settle it.

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): the linear kink-to-fishbone benchmark against M3D-K and NIMROD.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md): nonlinear JOREK fishbone studies in progress.
- [Liu et al. (2022b)](/sources/liu-2022-b.md): non-resonant fishbones in DIII-D and NSTX, the BAE-like branch, thermal-ion Landau damping, the first nonlinear M3D-C1-K fishbone, the disagreement with NIMROD.
