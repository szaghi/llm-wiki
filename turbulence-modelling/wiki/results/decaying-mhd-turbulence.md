---
type: Result
title: "Decaying MHD turbulence and its invariants"
description: "Decaying MHD turbulence is a selective decay whose power laws follow from the conserved quantity that constrains it and from a reconnection-controlled decay time (Schekochihin 2022, §12); decaying runs also serve as code tests and as probes of the Hall effect, as in the Orszag–Tang decay with and without the Hall term."
status: established
aliases: [selective decay, Orszag–Tang vortex, Orszag-Tang decay, decaying Hall MHD, Saffman invariant, Hosking invariant, Saffman helicity invariant, Loitsyansky invariant, reconnection-controlled decay, inverse transfer]
tags: [mhd, astrophysics, plasma, isotropic-turbulence, reconnection]
timestamp: 2026-10-28T07:08:00Z
---

# Decaying MHD turbulence and its invariants

Freely decaying MHD turbulence loses energy while some other quantity is
conserved better than the energy; the decay laws — power laws in time of the
mean kinetic and magnetic energies and of the energy-containing scale — are
fixed by that constraint and by the decay rate. This **selective decay**
(the review cites Taylor 1974 and, for hydrodynamics, Kolmogorov 1941) is
the organizing idea of §12 of [Schekochihin
(2022)](/sources/schekochihin-2022.md), which reviews the classical laws,
replaces the ideal decay time by a **reconnection-controlled** one (citing
Zhou et al. 2019 and Hosking & Schekochihin 2021), and derives
the non-helical laws from the **Hosking invariant**.

Notation (page-local): $\langle u^2\rangle$ and $\langle b^2\rangle$ are the
mean kinetic and magnetic energies (field in velocity units, no mean field),
$U$ and $b$ the corresponding rms amplitudes, $L$ the energy-containing
scale, $\boldsymbol A$ the vector potential, $H_m=\boldsymbol A\cdot\boldsymbol B$
and $H_c=\boldsymbol u\cdot\boldsymbol B$ the helicity and cross-helicity
densities of the registry.

## Classical selective-decay laws

- **2D MHD, anastrophy.** The mean square of the out-of-plane vector
  potential $A_z$ obeys $d\langle A_z^2\rangle/dt=-2\eta_m\langle b^2\rangle\to0$
  as $\eta_m\to0$ (Eq. 12.2). With $\langle A_z^2\rangle\sim b^2L^2$ and an
  ideal decay rate $U\sim b$, Hatori's (1984) laws, which the review cites, follow:
  $\langle b^2\rangle\sim\langle u^2\rangle\propto t^{-1}$, $L\propto t^{1/2}$
  (Eq. 12.4), confirmed by Biskamp & Welter (1989).
- **3D helical MHD.** Magnetic helicity decays as
  $d\langle H_m\rangle/dt=-2\eta_m\langle\boldsymbol B\cdot\boldsymbol J\rangle$,
  which vanishes like $\eta_m^{1/2}$ (Eq. 12.5; $\boldsymbol J$ the current,
  page-local). With $\langle H_m\rangle\sim b^2L$, the ideal laws are
  $\langle b^2\rangle\propto t^{-2/3}$, $L\propto t^{2/3}$ (Eq. 12.7; the review cites Hatori
  1984 and Son 1999). Simulations of Biskamp & Müller (1999, 2000)
  instead show $\langle b^2\rangle\propto t^{-1/2}$, $\langle u^2\rangle\propto t^{-1}$,
  $L\propto t^{1/2}$ (Eq. 12.8).

## Reconnection-controlled decay

Schekochihin (2022, §12.2) adopts the argument of Zhou et al. (2019, 2021) that
the assumption of ideal dynamics, $U\sim b$, is "flawed": the
energy-containing structures decay on a reconnection time
$\tau_{\mathrm{rec}}\sim\epsilon_{\mathrm{rec}}^{-1}L/b$, where the
dimensionless reconnection rate $\epsilon_{\mathrm{rec}}$ (page-local) is
Sweet–Parker-like, $\epsilon_{\mathrm{rec}}^{-1}=(1+Pm)^{1/2}S_{L}^{1/2}$ with
$S_L=bL/(\eta_m\sqrt{1+Pm})$, until $S_L$ exceeds the plasmoid threshold
$\sim10^4$, beyond which it saturates at the fast plasmoid rate
$\sim10^{-2}(1+Pm)^{-1/2}$ (Eq. 12.9; see [tearing-mediated MHD
turbulence](/results/tearing-mediated-mhd-turbulence.md)). Then

$$\frac{d\langle b^2\rangle}{dt}\sim-\epsilon_{\mathrm{rec}}\frac{b^3}{L},\qquad \langle u^2\rangle\sim\epsilon_{\mathrm{rec}}\langle b^2\rangle$$

(Eqs. 12.10–12.11): the flows are the reconnection outflows, and the turbulence
is magnetically dominated. The 2D laws (12.4) are unchanged, but helical
Sweet–Parker decay gives $\langle b^2\rangle\propto t^{-4/7}$,
$L\propto t^{4/7}$, $\langle u^2\rangle\propto t^{-5/7}$ (Eqs. 12.12–12.13).
Hyper-resistivity changes the reconnection rate and hence the laws, which is
the test the review cites from Hosking & Schekochihin (2021): their 2D run at
$4608^2$ uses equal hyperviscosity and hyperresistivity of order $n=4$ in
the source's indexing (Fig. 25 caption, §12.2.1).

## Saffman-type invariants

For a density $\psi$ obeying a conservation law
$\partial_t\psi+\nabla\cdot\boldsymbol\Gamma=$ (dissipation) with
$\langle\psi\rangle=0$ (Eq. 12.17), Schekochihin (2022, §12.4.1) defines the
generalized Saffman invariant (page-local $I_\psi$)

$$I_\psi=\lim_{V\to\infty}\frac{1}{V}\left(\int_V\psi\,d^3r\right)^2=\int d^3l\,\langle\psi(\boldsymbol r)\psi(\boldsymbol r+\boldsymbol l)\rangle$$

(Eqs. 12.18–12.20), conserved when correlations decay faster than $l^{-3}$
(Eq. 12.21). It is the coefficient of the large-scale spectrum,
$E_\psi(k)=I_\psi k^2/(2\pi^2)+J_\psi k^4+\dots$ with
$J_\psi=-\tfrac13\int d^3l\,l^2\langle\psi\psi\rangle$ (Eq. 12.32; "permanence
of large scales"). Instances:

| $\psi$ | Invariant | Scaling constraint | Decay laws |
|---|---|---|---|
| $\boldsymbol u$ (hydrodynamics) | Saffman $I_u$ | $U^2L^3=$ const | $\langle u^2\rangle\propto t^{-6/5}$, $L\propto t^{2/5}$ (Eq. 12.22) |
| — (hydrodynamics) | Loitsyansky $\int d^3l\,l^2\langle\boldsymbol u\cdot\boldsymbol u'\rangle$ | $U^2L^5=$ const | $t^{-10/7}$, $L\propto t^{2/7}$, Kolmogorov (1941) (Eqs. 12.23–12.24) |
| $H_m$ | Hosking $I_H$ | $b^4L^5=$ const | below |
| $H_c$ | Saffman cross-helicity $I_X$ | $U^2b^2L^3=$ const | below |

**Hosking invariant (non-helical decay).** With $b^4L^5=$ const and
reconnection-controlled decay, Hosking & Schekochihin (2021), cited by the
review (§12.4.2), obtain for magnetically dominated non-helical turbulence (Eqs. 12.26–12.27)

$$\begin{aligned}
&\text{fast reconnection:}\quad \langle b^2\rangle\propto t^{-10/9},\quad L\propto t^{4/9};\\
&\text{Sweet–Parker:}\quad \langle b^2\rangle\propto t^{-20/17},\quad L\propto t^{8/17},\quad \langle u^2\rangle\propto t^{-19/17}.
\end{aligned}$$

*(Compiler check, not in the sources: with $b\propto L^{-5/4}$ and
$d\langle b^2\rangle/dt\sim-\epsilon_{\mathrm{rec}}b^3/L$ at constant
$\epsilon_{\mathrm{rec}}$, $\langle b^2\rangle\propto t^{x}$ and
$L\propto t^{-2x/5}$ give $x-1=3x/2+2x/5$, i.e. $x=-10/9$.)* Conservation of
$I_H$ over volumes $(2R)^3$ is tested in $512^3$ simulations (Figs. 26–27), and
simulations with varying hyperdissipation order discriminate these laws from
Campanelli's (2004) alternative, which the review reports as ruled out
(§12.2.3, §12.3, §12.4.2). The review notes that $t^{-10/9}$ and $t^{-20/17}$ differ from the
widely reported $\langle b^2\rangle\propto t^{-1}$, $L\propto t^{1/2}$, but
are numerically hard to distinguish from them.

**Saffman cross-helicity invariant.** $I_X$ together with magnetic helicity
gives $U\propto b^2$ and recovers the Biskamp–Müller laws (12.8) exactly
(Eq. 12.29), which the review reinterprets as a transient decay constrained
by $I_X$ (§12.4.3, Eqs. 12.28–12.31). The review cites a kinetic-helicity analogue
from Levich & Tsinober (1983).

## Self-similar spectra and inverse transfer

The Olesen rescaling, which the review cites (§12.2.3), $\boldsymbol r\to a\boldsymbol r$,
$t\to a^{1-h_O}t$, $\boldsymbol u\to a^{h_O}\boldsymbol u$,
$\boldsymbol B\to a^{h_O}\boldsymbol B$, $\nu\to a^{1+h_O}\nu$,
$\eta_m\to a^{1+h_O}\eta_m$ (Eq. 12.14; $h_O$ page-local) gives
$\langle u^2\rangle\propto\langle b^2\rangle\propto t^{2h_O/(1-h_O)}$ and
$L\propto t^{1/(1-h_O)}$ (Eq. 12.15). With Campanelli's more general
rescaling $\boldsymbol B\to a^{m_O}\boldsymbol B$ ($m_O$ page-local; $m_O=-1/2$
with helicity, $m_O=h_O$ without), the self-similar spectra are
$E(k,t)=k^{-1-2m_O}f(kt^{1/(1-h_O)})$ (Eq. 12.35), and the
decay laws (12.7), (12.29) and (12.26) correspond to
$(m_O,h_O)=(-1/2,-1/2)$, $(-1/2,-1)$ and $(-5/4,-5/4)$ (§12.5.2); the
Sweet–Parker cases are not self-similar. The review concludes that
dissipation coefficients need not be invariant under the rescaling,
against Campanelli's argument (§12.2.3). In all decay regimes the $k^4$
coefficient of the magnetic spectrum grows, $J_B\sim b^2L^5$, which is the
review's account of **inverse transfer** without helicity (§12.5,
Eq. 12.33).

In a driven setting, [Dahlin et al. (2022)](/sources/dahlin-2022.md) (§1–§2)
cite helicity condensation (Antiochos 2013), which builds on the inverse
cascade of magnetic helicity of the works they also cite (Berger & Field
1984, Berger 1984, Finn & Antonsen 1985, Biskamp 1993): reconnection between the fields twisted by
neighbouring photospheric cells of the same rotation sense removes the twist
between them and moves twist flux to ever larger scales, until it accumulates at the boundary of the flux
system. Their [STITCH model](/methods/stitch-helicity-condensation-model.md)
parametrizes the outcome of that inverse transfer as a boundary source term
in driven runs; the paper states no decay law.

## Decaying RMHD and imbalanced decay

With a strong mean field (§12.6), the review cites Zhou et al. (2020), who find
$b_\perp L_\perp\sim$ const, hence $\langle b_\perp^2\rangle\propto t^{-1}$,
$L_\perp\propto t^{1/2}$, and by [critical
balance](/properties/critical-balance.md) $L_\parallel\propto t$
(Eqs. 12.38–12.40); the review justifies $b_\perp L_\perp\sim$ const with
$I_X$ (Eq. 12.41). Its new §12.6.2 extends the Olesen symmetry with a
separate parallel rescaling (Eq. 12.42), derives self-similar 2D spectra
(Eqs. 12.43–12.47) and conjectures a **parallel Saffman invariant**
$I_\parallel=\int dl_\parallel\,\boldsymbol b_\perp(r_\parallel)\cdot\boldsymbol b_\perp(r_\parallel+l_\parallel)\sim b_\perp^2L_\parallel$
(Eq. 12.48; $I_\parallel$ page-local). Imbalanced decay,
$d(Z^\pm)^2/dt\sim-Z^\mp(Z^\pm)^2/L$, conserves $Z^+-Z^-$ and drives the
system towards Elsasser states (§12.7, Eqs. 12.49–12.50, citing Dobrowolny et al. 1980
and Maron & Goldreich 2001), where $Z^\pm$ are the rms Elsasser
amplitudes of [reduced MHD](/definitions/reduced-mhd.md).

## Decay as a diagnostic problem

Decay also matters where it is not the object of study. [Ferrand et al.
(2022)](/sources/ferrand-2022.md) evaluate [exact
laws](/results/turbulence-exact-laws.md) of compressible Hall MHD on
$1024^3$ DNS of free decay (no forcing, initial random-phase modes at
$1\le k\le3$, $Re=Rm\simeq3\times10^3$), where the stationarity behind the
inertial-range law fails (§3, §5):

- The energy decay rates from linear fits over the analysis windows are
  $\approx0.047$ with a mean field $B_0=2$ and $\approx0.087$ without, in
  code units, and the inertial-range cascade rate roughly matches them (§3.1,
  §4).
- With $B_0=2$, kinetic plus magnetic energy oscillates in step with the
  internal energy, an exchange the authors attribute to waves (§3.1, Fig. 1;
  see [compressible MHD turbulence](/results/compressible-mhd-turbulence.md)).
- In the general (non-stationary) form of the laws, the time derivative of
  the two-point energy correlator acts as a scale-dependent energy
  reservoir that replaces large-scale forcing and is shared between cascade
  and dissipation; the authors conclude that the stationary inertial-range
  law still holds in decaying turbulence (§5–§6).

These runs analyse one window near the peak of dissipation each (§3.1,
§3.3) and report no decay exponents to compare with the selective-decay
laws above.

## Orszag–Tang decay, with and without the Hall term

[Foldes et al. (2023)](/sources/foldes-2023.md) use freely decaying
turbulence started from the three-dimensional **Orszag–Tang** vortex
(the authors cite Orszag & Tang 1979), "often considered as a prototypical flow
to study freely evolving MHD turbulence", first to validate a [lattice
Boltzmann](/methods/lattice-boltzmann-method.md) MHD code against the
pseudo-spectral code [GHOST](/software/ghost.md), then to study decaying
Hall MHD (§4.4, §5). The field is in Alfvén units ($\mu_0^{1/2}$ absorbed
into $\boldsymbol B$, so the Lorentz force is $\boldsymbol J\times\boldsymbol B$
with $\boldsymbol J=\nabla\times\boldsymbol B$), and the initial condition in
a periodic box of side $2\pi$ is

$$\boldsymbol u(\boldsymbol x,0)=U_0\,[-2\sin y,\;2\sin x,\;0],\qquad \boldsymbol B(\boldsymbol x,0)=B_{\mathrm{OT}}\,[-2\sin2y+\sin z,\;2\sin x+\sin z,\;\sin x+\sin y],$$

with amplitudes $U_0=1$ and $B_{\mathrm{OT}}=0.8$ (§4.4; $B_{\mathrm{OT}}$ registry §11, the paper's $B_0$; $U_0$ is also the reference velocity and $L_0$ the reference length). There is no mean field; the authors note that
the configuration is isotropic and does not contain the anisotropy a
background field would impose (§7). The runs are model-free
[DNS](/definitions/direct-numerical-simulation.md) with $Pm=1$.

**Energy budget.** The diagnostic is the shell-cumulative balance
$\partial_t\sum_{|k'|<k}E(k')=-S(k)-D(k)$, where $S(k)$ is the nonlinear
transfer through the wavenumber $k$ (advection, Lorentz force and induction
terms) and $D(k)=\sum_{|k'|<k}\bigl(\nu k'^2|\boldsymbol u_{\boldsymbol k'}|^2+\eta_mk'^2|\boldsymbol B_{\boldsymbol k'}|^2\bigr)$
the cumulative dissipation (Eqs. 4.10–4.12; $S$ and $D$ page-local,
$\boldsymbol u_{\boldsymbol k'}$, $\boldsymbol B_{\boldsymbol k'}$ the Fourier coefficients); the pressure contribution is
neglected as negligible (§4.4, Fig. 12).

**MHD decay ($N_x=512$ points per direction).** At $M=0.025$ the Reynolds number based on the rms
velocity and the integral scale reaches $Re\simeq1600$ at the peak of
dissipation. The mean magnetic dissipation, proportional to
$\langle|\boldsymbol J|^2\rangle$, and the kinetic and magnetic energies are
followed to $t\approx12$; the code comparison is summarized on
[GHOST](/software/ghost.md) (Figs. 10–12).

**Hall-MHD decay.** The Hall term enters the induction equation as
$\partial_t\boldsymbol B=\nabla\times[(\boldsymbol u-\alpha_H\boldsymbol J)\times\boldsymbol B]+\eta_m\nabla^2\boldsymbol B$
(Eq. 2.9), derived from a two-fluid model with isothermal, massless electrons; $\alpha_H=1/(en)$ is the Hall parameter and its
dimensionless form $\epsilon_H=L_H/L_0$ the ratio of the Hall length to the
reference length, equal to the ion inertial length $d_i$ over $L_0$ when
$U_0$ equals the Alfvén speed (Eqs. 3.32, 3.37–3.38; $\alpha_H$, $\epsilon_H$,
$d_i$ registry §11, $L_H$ page-local). The runs (Table 2; $Pm=1$, box $2\pi$; $Re$ at the
peak of magnetic dissipation, times in units of $L_0/U_0$):

| Run | $N_x$ | $M$ (initial) | $Re$ | $\epsilon_H$ | $t_{\mathrm{tot}}$ | $t_{\mathrm{peak}}$ |
|---|---|---|---|---|---|---|
| I | 512 | $7.0\times10^{-4}$ | 4400 | 0.0025 | 48.2 | 31.8 |
| II | 512 | $1.0\times10^{-4}$ | 5240 | 0.01 | 35.8 | 33.6 |
| III | 512 | $0.625\times10^{-4}$ | 7150 | 0.025 | 29.6 | 26.5 |
| IV | 768 | $0.6\times10^{-4}$ | 6000 | 0.015 | 36.6 | 32.0 |

The Mach numbers are set by the whistler time-step bound of the explicit
scheme (Table 2 caption, §3.4; see [GHOST](/software/ghost.md)).
Findings (§5):

- **Faster onset.** "Increasing the intensity of the Hall effect produces a
  faster development of turbulence", attributed to whistler and Hall-drift
  waves that propagate faster than Alfvén waves (the authors cite Huba 2003),
  and said to be consistent with the magnetic-dissipation histories of
  Fig. 13.
- **Spectral break.** Increasing $\epsilon_H$ moves the Hall scale to larger
  scales and shortens the $k^{-5/3}$ range of both the kinetic and the
  magnetic spectrum (Fig. 16). Beyond the Hall wavenumber the magnetic
  spectrum develops, as $\epsilon_H$ grows, a power law that the authors
  call "in perfect agreement" with the $k^{-2.73}$ sub-ion slope of
  solar-wind spectra (the authors cite Kiyani et al. 2015; Figs. 14, 16).
- **Small-scale structure.** In run IV the current density and the
  vorticity show current sheets, Kelvin–Helmholtz instabilities and
  vortices, which the authors call the disordered structures characteristic
  of the Hall effect (the authors cite Miura & Araki 2014; Fig. 15).

Ferrand et al. (2022, §4) measure a different quantity in compressible
Hall-MHD decay: the Hall part of the cascade rate of the [exact
laws](/results/turbulence-exact-laws.md) never dominates the MHD part below
the ion scale in their runs, which they attribute to a Hall effect too weak,
dissipation stopping the cascade first, and they recommend hyperviscosity.
Foldes et al. report the slope of magnetic spectra (Figs. 14, 16), Ferrand
et al. the Hall and MHD components of the cascade rate (§4, Figs. 3, 7), in
different set-ups (Orszag–Tang decay without mean field against random-phase
initial modes at initial sonic Mach numbers 0.25–0.5).

## Qualifications

- **Printed inconsistency, §12.5.2, p. 96 of arXiv v3.** The text states that
  the spectral peak scales as $E_{\max}\propto t^{(1+2m)/(1-h)}$ (source
  symbols; $m_O$, $h_O$ here) and that this
  is "$\propto t^{-1/2}$ for the non-helical one (figure 28b)". *(Compiler
  check, not in the sources: with the non-helical fast-reconnection pair
  $(m_O,h_O)=(-5/4,-5/4)$ listed in the preceding paragraph for Eq. 12.26, the formula
  gives $t^{-2/3}$; $t^{-1/2}$ corresponds to $m_O=h_O=-1$, i.e. the 2D-like
  laws $\langle b^2\rangle\propto t^{-1}$, $L\propto t^{1/2}$.)* The text does
  not say which pair it means; the figure it cites is not read here.
- **Section reference, §12.2.1, p. 83.** The text says the assumption of ideal
  dynamics "in § 12.4 was flawed"; the $U\sim b$ assumption is made in
  §12.1.1 (Eq. 12.4), and §12.4 is the Saffman-invariant section.
- **Hall-MHD Orszag–Tang runs (Foldes et al. 2023, arXiv v2).** The
  $k^{-2.73}$ agreement is shown by overlaying a reference slope on the
  spectra (Figs. 14, 16); no fitted exponent or fit range is reported, the
  Reynolds numbers are 4400–7150, and the same paper states (§6) that
  observed solar-wind sub-ion slopes range from about $-4$ to $-2$. The §5
  text and the Fig. 13 caption speak of "three" runs while Table 2 lists
  four; the wall-clock times 10, 55 and 69 h are given for "the three runs".
  The printed peak times of the three $512^3$ runs (Table 2), 31.8, 33.6
  and 26.5 for $\epsilon_H=0.0025$, 0.01 and 0.025, are not monotone in
  $\epsilon_H$, and the runs also differ in $M$ and $Re$; the paper supports
  the "faster development" statement with Fig. 13 (§5).
- Disagreements the review cites and does not resolve: Brandenburg et
  al. (2019) and Banerjee & Jedamzik (2004) prefer the ideal helical law
  (12.7) (§12.2.1); Christensson et al. (2005) argue for $L\propto t^{1/2}$ along
  Campanelli's lines (§12.3, footnote 60).

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §12 (Eqs. 12.1–12.50): §12.1.1–§12.1.2, §12.2.1–§12.2.3, §12.3, §12.4.1–§12.4.3, §12.5, §12.5.2, §12.6, §12.6.2, §12.7; Figs. 25–29 cited only as locations of the evidence the text describes.
- [Ferrand et al. (2022)](/sources/ferrand-2022.md) — §3.1, Figs. 1–2; §4; §5–§6 (decay in compressible Hall-MHD DNS, non-stationary exact laws; Hall cascade component below the ion scale).
- [Dahlin et al. (2022)](/sources/dahlin-2022.md) — §1–§2 (helicity condensation as inverse helicity transfer, cited).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §2.1, Eq. (2.9); §3.3, Eqs. (3.32), (3.37)–(3.38); §4.4, Eqs. (4.10)–(4.12), Figs. 10–12; §5, Table 2, Figs. 13–16; §6; §7 (Orszag–Tang decay in MHD and Hall MHD).
