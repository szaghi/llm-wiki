---
type: Result
title: "Weak wave turbulence (magneto-capillary waves)"
description: "Weak wave turbulence describes cascades of weakly nonlinear waves through resonant interactions, with Kolmogorov–Zakharov spectra scaling as the square root of the flux for three-wave systems; the page covers weak Alfvén-wave turbulence and its critique, and its magneto-capillary analogue on a ferrofluid surface."
status: established
aliases: [weak turbulence, wave turbulence, WT, Kolmogorov–Zakharov spectrum, KZ spectrum, weak Alfvén-wave turbulence, magneto-capillary wave turbulence, MHD wave turbulence]
tags: [mhd, plasma, dns, anisotropy]
timestamp: 2026-10-27T15:51:00Z
---

# Weak wave turbulence (magneto-capillary waves)

**Weak (wave) turbulence** (WT) is the statistical regime of a field of
weakly nonlinear waves whose nonlinear interaction time $\tau_{\mathrm{nl}}$ is
much longer than the linear wave period, so that energy is exchanged only
among resonant wave sets (triads for quadratic nonlinearities) and the
spectrum obeys a kinetic equation whose stationary power-law solutions are
the **Kolmogorov–Zakharov (KZ) spectra**. The bundle meets it in two
settings: weak Alfvén-wave turbulence of [reduced
MHD](/definitions/reduced-mhd.md), which [Schekochihin
(2022)](/sources/schekochihin-2022.md) treats as a transient range on the way
to [critically balanced](/properties/critical-balance.md) strong turbulence,
and the surface waves of a magnetic liquid in a horizontal field, simulated by
[Kochurin et al. (2022)](/sources/kochurin-2022.md) as an analogue of
anisotropic Alfvén-wave turbulence.

## Ingredients

Stated by Kochurin et al. (2022, pp. 1, 5) and, for MHD, by Schekochihin
(2022, §4, App. A):

- **Time-scale separation** $\tau_{\mathrm{nl}}\gg$ the linear period at all
  scales; Kochurin et al. report checking it in their runs (Supplemental
  Material, not read here).
- **Resonant three-wave interactions.** For Alfvén waves of RMHD, the
  resonance conditions $\boldsymbol p+\boldsymbol q=\boldsymbol k$ with
  counter-propagating waves force one member of every triad to have
  $k_\parallel=0$, so energy moves only in $k_\perp$ at fixed $k_\parallel$
  (Schekochihin 2022, Eq. 4.2; the transfer is "frozen in the field
  direction", in the words of Kochurin et al. 2022, who cite Shebalin et al. 1983).
- **Flux scaling.** For a three-wave system, the spectral amplitude scales as
  the square root of the energy flux; Kochurin et al. (p. 5) cite this
  $\varepsilon_s^{1/2}$ dependence ($\varepsilon_s$ the energy flux, defined
  below) as the signature of three-wave interactions.
- **Kinetic equation.** The WT kinetic equation for RMHD of Galtier et
  al. (2000), derived in Schekochihin (2022, App. A.2, Eq. A15) under the
  random-phase approximation; its power-law steady states satisfy
  $\mu^++\mu^-_0=-4$ for the exponents of the wave and $k_\parallel=0$
  spectra (Eq. A23; $\mu^\pm$ page-local).

## Weak Alfvén-wave turbulence

The random-walk estimate $\tau_c\sim\tau_{\mathrm{nl}}^2/\tau_A$ gives the
balanced spectrum (Schekochihin 2022, Eqs. 4.5–4.7)

$$E(k_\perp)\sim\left(\frac{\varepsilon}{\tau_A}\right)^{1/2}k_\perp^{-2},$$

and the nonlinearity grows towards small scales until critical balance is
reached at $\lambda_{CB}\sim\varepsilon^{1/2}(L_\parallel/v_A)^{3/2}$; the
details, including the strongly turbulent $k_\parallel=0$ "condensate", are on
[critical balance](/properties/critical-balance.md). Kochurin et al. (2022,
Eq. 3) quote the corresponding kinetic-equation result for the elevation-like
spectrum of anisotropic shear-Alfvén waves ($k_\perp\gg k_\parallel$),

$$\mathcal S^m(k)=C_m\,\varepsilon_s^{1/2}v_A^{-3/2}k_\perp^{-3},\qquad C_m=1.467,\qquad E^m(k)=v_A^2k\,\mathcal S^m(k),$$

with the constant taken from Galtier (2021) and the remark that "a
$\sqrt{2\pi}$ factor was missing" in Galtier et al. (2000)
($\mathcal S^m$, $\varepsilon_s$ page-local, defined below). *(Compiler
check, not in the sources: $E^m=v_A^2k\mathcal S^m\propto C_m\varepsilon_s^{1/2}v_A^{1/2}k_\perp^{-2}$,
the $k_\perp^{-2}$ exponent and $(\varepsilon v_A)^{1/2}$ dependence of the
estimate above.)*

**Standing of the theory.** Schekochihin (2022, §4.4, App. A) judges WT
asymptotically "irrelevant" — a transient range above $\lambda_{CB}$ — and the
kinetic equation of Galtier et al. (2000) "at best incomplete and at worst wrong", because
the $k_\parallel=0$ condensate through which all interactions pass is itself
strongly turbulent and violates the random-phase approximation. Kochurin et
al. (2022) quote the weak-turbulence prediction as derived and "confirmed
recently numerically" (p. 1, citing Meyrand et al.) and use it as the
reference for their spectra; they do not discuss the condensate critique,
and list "the critical balance separating weak turbulence from strong
turbulence" among open questions (Conclusion, p. 5). Their model is a
ferrofluid without free charge or current (p. 2), whose capillary waves
propagate across the field, unlike Alfvén waves in a plasma (p. 4). On
the exponent the two agree: Schekochihin (2022, Eq. 4.7) also gives
$k_\perp^{-2}$ for the balanced WT energy spectrum and reports it confirmed
numerically (§4, citing Perez & Boldyrev 2008).

## Magneto-capillary waves on a ferrofluid

Page-local notation for this section: $\varsigma(x,y,t)$ is the surface
elevation and $\psi$ the surface velocity potential; $B$ is the external
horizontal field, along $x$; $k_x$ ($k_\parallel$) and $k_y$ ($k_\perp$) are
the wavenumbers along and across it, $k=|\boldsymbol k|$; $\sigma_s$ is the
surface tension, $\rho$ the liquid density, $\mu_r$ the relative magnetic
permeability, $\mu_{\mathrm{eff}}=\mu_0(\mu_r+1)/(\mu_r-1)^2$; $\mathcal S(k)$
is the elevation power spectrum (squared modulus of the Fourier transform of
$\varsigma$); $\varepsilon_s$ is the energy flux per unit area and density
(the source writes $P$).

**Linear waves.** For an ideal ferrofluid of infinite depth, gravity
neglected, Kochurin et al. (2022, Eq. 1, citing Melcher 1961) write

$$\omega^2(\boldsymbol k)=\frac{B^2}{\mu_{\mathrm{eff}}\rho}k_x^2+\frac{\sigma_s}{\rho}k^3,\qquad v_A^2=\frac{B^2}{\mu_{\mathrm{eff}}\rho},$$

where $v_A$ is the speed of the dispersionless magnetic surface wave along
$B$, "analogous to Alfvén velocity" — on this page only, not the registry's
plasma $v_A$. Without field the waves are isotropic capillary waves with the
KZ spectra (Eq. 2, from Zakharov & Filonenko 1967)

$$\mathcal S^c(k)=C_{KZ}\,\varepsilon_s^{1/2}\left(\frac{\sigma_s}{\rho}\right)^{-3/4}k^{-15/4},\qquad \mathcal S^c(\omega)\sim\omega^{-17/6},$$

which the authors describe as well confirmed experimentally and
numerically. For $B\ne0$ no WT prediction existed, only dimensional
analysis (p. 2).

**Model and numerics** (pp. 2–3). Hamiltonian boundary-motion equations for
$\varsigma$ and $\psi$ of an ideal, irrotational, incompressible ferrofluid
with no free charge or current, truncated at quadratic nonlinearity (Eqs.
4–5; derivation in the Supplemental Material), with the nondimensional field
parameter $V_A^2=v_A^2[\rho/(g\sigma_s)]^{1/2}$ ($g$ gravity, used only for
scaling) and the magnetic Atwood number $A_\mu=(\mu_r-1)/(\mu_r+1)=0.5$
($\mu_r=3$). Dissipation is a hyperviscous operator
$-\nu_h(k-k_d)^2$ for $k\ge k_d$ (page-local $\nu_h=10$, $k_d=150$), and
harmonics above $k_a=212$ are zeroed every step, which the authors interpret
as "superviscosity". Isotropic pumping acts at $k\in[1,6]$, peaked at
$k=3$. Pseudo-spectral discretization with $1024^2$ harmonics in a $2\pi\times2\pi$
box, explicit fourth-order Runge–Kutta, $dt=5\times10^{-5}$; runs at
$V_A^2=0,25,100,300$, statistically stationary after $t\approx50$, run to
$t=500$; mean steepness 0.16, almost independent of $B$. The authors note
that surface waves collapse under an infinitely strong horizontal field for
finite $\mu_r$, so viscosity and surface tension are needed to regularize
the simulation. What the title calls "direct numerical simulation" solves
this truncated Hamiltonian model with hyperviscosity, not the Navier–Stokes
equations (compare [DNS](/definitions/direct-numerical-simulation.md));
"three-dimensional" refers to the liquid, while the computed field
$\varsigma(x,y)$ is two-dimensional.

**Results** (pp. 3–5, Figs. 1–4):

- **Isotropic to anisotropic.** As $V_A^2$ rises from 0 to 300 the surface
  relief turns from isotropic to almost unidirectional, waves propagating
  mainly across $B$ (Fig. 1); the authors attribute this to the stabilizing
  effect of a horizontal field, whose lines pierce the interface for waves
  along $B$.
- **Dispersion.** The space–time spectra show the nonlinear dispersion
  relation becoming dispersionless along the field, $\omega=V_Ak_x$
  (Fig. 2a–c), and a bound-wave branch $\omega=k_y^{3/2}/2^{1/2}$ across it
  (Fig. 2d–f); the constant-frequency sections at $\omega=600$ go from an
  isotropic ring to a perpendicular-dominated distribution (Fig. 2g–h).
- **Spectra.** At $B=0$, $\mathcal S(k)\propto k^{-15/4}$ and
  $\mathcal S(\omega)\propto\omega^{-17/6}$ as in KZ theory. At
  $V_A^2=300$ the spectrum is carried by perpendicular transfer —
  $\mathcal S(k_x)$ is "more than one order of magnitude smaller" than
  $\mathcal S(k_y)$ — and (Eqs. 6–7)
  $$\mathcal S(k)\approx\mathcal S(k_y)=C_1\,\varepsilon_s^{1/2}v_A^{-3/2}k_y^{-3},\qquad \mathcal S(\omega)=C_2\left(\frac{\sigma_s}{\rho}\right)^{2/3}\varepsilon_s^{1/2}v_A^{-3/2}\omega^{-7/3},$$
  with fitted $C_1=1.7$ and $C_2=1.34$ (page-local; the source writes $C$,
  $C'$). The prefactors scale as $\varepsilon_s^{1/2}$ at fixed $V_A$ and as
  $V_A^{-3/2}$ at fixed $\varepsilon_s\approx2.7\times10^{-3}$ "for high
  enough $V_A$" (Fig. 4 insets). Mapping one spectrum onto the other through
  the capillary branch gives $C_2=2C_1/3$; the fitted ratio
  $2C_1/(3C_2)=0.85$ is "as expected close to 1".
- **Agreement with Alfvén WT.** The $k_\perp^{-3}$ law and its
  $\varepsilon_s^{1/2}v_A^{-3/2}$ prefactor coincide with the shear-Alfvén
  WT prediction above, and $C_1=1.7$ is "close to" $C_m=1.467$. A
  phenomenological model (strong field $V_Ak_x\gg k_y^{3/2}$, anisotropy
  $k_y\gg k_x$; all magnetic potential energy transferred into capillary
  kinetic energy) gives the same scaling (pp. 2–3; details in the
  Supplemental Material).
- **Locality.** Bicoherence (Supplemental Material) shows three-wave
  interactions mainly across $B$, with triads of comparable wavenumbers,
  "suggesting that wave interactions are local" — unlike the nonlocal
  interactions and flat spectrum predicted for 2D MHD weak turbulence by
  Tronko et al. (2013), whom they cite (p. 5).

**Different physics, same scaling.** The authors stress that in a plasma no
wave propagates across the field and magnetic energy reaches the
perpendicular direction by shearing, whereas here capillary waves propagate
across the field and receive the magnetic energy: different mechanisms
giving the same spectral law (p. 4). They propose the analogy as
quantitative, and expect similar effects in electrohydrodynamics of
non-conducting liquids under strong electric fields; an experiment would need
a ferrofluid of high susceptibility, but such fluids are "at least ten times"
as viscous as water, which would suppress wave interactions (Conclusion).

## Qualifications

- **Evidence.** The time-scale separation, bicoherence and triad locality
  are shown only in the Supplemental Material, which is not part of the file
  read. The magneto-capillary scalings are fits to four field strengths and
  two parameter series, without an experimental counterpart.
- **Printed slip** (arXiv v1, Fig. 4 caption). The caption converts the
  wavenumber spectra to frequency "using $\omega\sim k^{-3/2}$". *(Compiler
  check, not in the sources: the capillary branch of Eq. 1 gives
  $\omega\propto k^{3/2}$, and only that sign maps $k^{-15/4}$ to
  $\omega^{-17/6}$ and $k^{-3}$ to $\omega^{-7/3}$, since
  $\mathcal S(\omega)=\mathcal S(k)\,dk/d\omega\propto k^{-15/4}k^{-1/2}=k^{-17/4}=\omega^{-17/6}$;
  the Fig. 2 caption correctly writes $\omega=k_y^{3/2}$.)* Eq. (3) prints the
  energy spectrum with a lowercase $v_a$ where $v_A$ is defined.
- **Not a closure.** Neither source proposes a turbulence closure.

# Citations

- [Kochurin et al. (2022)](/sources/kochurin-2022.md) — pp. 1–2, Eqs. (1)–(3); Model equations, Eqs. (4)–(5), p. 2; Phenomenological analysis, pp. 2–3; Anisotropic regime and Wave interactions, pp. 3–5, Figs. 1–4, Eqs. (6)–(7); Conclusion.
- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §4, Eqs. (4.2)–(4.8); §4.4; App. A.2, Eqs. (A15), (A23).
