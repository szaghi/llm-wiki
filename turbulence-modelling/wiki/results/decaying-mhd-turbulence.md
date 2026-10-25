---
type: Result
title: "Decaying MHD turbulence and its invariants"
description: "Decaying MHD turbulence is a selective decay whose power laws follow from the conserved quantity that constrains it (anastrophy, magnetic helicity, Saffman-type invariants such as the Hosking invariant) and from a reconnection-controlled decay time, as reviewed and extended by Schekochihin (2022, §12)."
status: established
aliases: [selective decay, Saffman invariant, Hosking invariant, Saffman helicity invariant, Loitsyansky invariant, reconnection-controlled decay, inverse transfer]
tags: [mhd, astrophysics, plasma, decaying-turbulence, reconnection]
timestamp: 2026-10-25T13:42:00Z
---

# Decaying MHD turbulence and its invariants

Freely decaying MHD turbulence loses energy while some other quantity is
conserved better than the energy; the decay laws — power laws in time of the
mean kinetic and magnetic energies and of the energy-containing scale — are
fixed by that constraint and by the decay rate. This **selective decay**
(recalled from Taylor 1974 and, for hydrodynamics, from Kolmogorov 1941) is
the organizing idea of §12 of [Schekochihin
(2022)](/sources/schekochihin-2022.md), which reviews the classical laws,
replaces the ideal decay time by a **reconnection-controlled** one (after
Zhou et al. 2019 and Hosking & Schekochihin 2021, as recalled), and derives
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
  ideal decay rate $U\sim b$, Hatori's (1984) laws follow (as recalled):
  $\langle b^2\rangle\sim\langle u^2\rangle\propto t^{-1}$, $L\propto t^{1/2}$
  (Eq. 12.4), confirmed by Biskamp & Welter (1989).
- **3D helical MHD.** Magnetic helicity decays as
  $d\langle H_m\rangle/dt=-2\eta_m\langle\boldsymbol B\cdot\boldsymbol J\rangle$,
  which vanishes like $\eta_m^{1/2}$ (Eq. 12.5; $\boldsymbol J$ the current,
  page-local). With $\langle H_m\rangle\sim b^2L$, the ideal laws are
  $\langle b^2\rangle\propto t^{-2/3}$, $L\propto t^{2/3}$ (Eq. 12.7; Hatori
  1984, Son 1999, as recalled). Simulations of Biskamp & Müller (1999, 2000)
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
the test used by Hosking & Schekochihin (2021), as recalled: their 2D run at
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
reconnection-controlled decay, Hosking & Schekochihin (2021), as reviewed,
obtain for magnetically dominated non-helical turbulence (Eqs. 12.26–12.27)

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
by $I_X$ (§12.4.3, Eqs. 12.28–12.31). A kinetic-helicity analogue is recalled from
Levich & Tsinober (1983).

## Self-similar spectra and inverse transfer

The Olesen rescaling (as recalled, §12.2.3) $\boldsymbol r\to a\boldsymbol r$,
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

## Decaying RMHD and imbalanced decay

With a strong mean field (§12.6), Zhou et al. (2020), as recalled, find
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
system towards Elsasser states (§12.7, Eqs. 12.49–12.50; Dobrowolny et al. 1980,
Maron & Goldreich 2001, as recalled), where $Z^\pm$ are the rms Elsasser
amplitudes of [reduced MHD](/definitions/reduced-mhd.md).

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
  §12.1.1 (Eq. 12.4), and §12.4 is the Saffman-invariant section — an
  evident mix-up of the section with the equation number.
- Disagreements recalled by the review and not resolved by it: Brandenburg et
  al. (2019) and Banerjee & Jedamzik (2004) prefer the ideal helical law
  (12.7) (§12.2.1); Christensson et al. (2005) argue for $L\propto t^{1/2}$ along
  Campanelli's lines (§12.3, footnote 60).

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §12 (Eqs. 12.1–12.50): §12.1.1–§12.1.2, §12.2.1–§12.2.3, §12.3, §12.4.1–§12.4.3, §12.5, §12.5.2, §12.6, §12.6.2, §12.7; Figs. 25–29 cited only as locations of the evidence the text describes.
