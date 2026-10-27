---
type: Result
title: "Tearing-mediated MHD turbulence"
description: "Below a disruption scale proportional to Rm^-4/7, aligned sheets of MHD turbulence are torn faster than they cascade; the resulting recursive, tearing-mediated cascade has a k_perp^-11/5 envelope and ends at a Kolmogorov-scaled dissipation cutoff (Schekochihin 2022, after Mallet et al. and Loureiro & Boldyrev)."
status: hypothesis
aliases: [tearing disruption, disruption scale, reconnection-mediated turbulence, sub-inertial range, tearing instability, plasmoid instability]
tags: [mhd, plasma, astrophysics, reconnection, dns]
timestamp: 2026-10-27T15:50:00Z
---

# Tearing-mediated MHD turbulence

The [aligned cascade](/properties/dynamic-alignment.md) of strong MHD
turbulence produces sheet-like structures whose aspect ratio
$\xi/\lambda\sim1/\sin\theta_\lambda$ grows towards small scales. Such sheets
are unstable to the **tearing instability**, and below a **disruption scale**
$\lambda_D$ (page-local symbol) the fastest tearing mode grows faster than the
structure is cascaded. [Schekochihin (2022)](/sources/schekochihin-2022.md)
(§7) presents, in the form it cites from Mallet et al. (2017) and with
Loureiro & Boldyrev (2017) as the parallel derivation (crediting an earlier
formal version to Carbone et al. 1990), the result that the
cascade below $\lambda_D$ is a recursive sequence of tearing disruptions with
a $k_\perp^{-11/5}$ spectral envelope, ending at a Kolmogorov-scaled
dissipation cutoff. The page carries `status: hypothesis`: the review ranks
the tearing-mediated range among the "hotly debated" parts of the theory
(§8.2), and the numerical evidence it cites is partly a conference abstract.

## The tearing instability (background)

Schekochihin (2022, App. D.1–D.3) gives a "quick and dirty" derivation in the
Strauss form of [reduced MHD](/definitions/reduced-mhd.md), citing
Furth, Killeen & Rosenbluth (1963), Coppi et al. (1976) and Porcelli (1987).
For a sheet of width $\lambda$ with reversing field of Alfvén speed $v_{Ay}$
(page-local), define the width-based Lundquist number
$S_{L,\lambda}=v_{Ay}\lambda/\eta_m$ and $Pm=\nu/\eta_m$. With the tearing
stability index $\Delta'$ (page-local) scaling as
$\Delta'\lambda\sim(k_y\lambda)^{-n}$ ($n=1$ for Harris-like profiles, $n=2$
for $\tanh$/$\cosh^{-2}$ or sinusoidal ones; Eq. D20), the fastest-growing
(Coppi) mode has, for $n=1$ (Eq. D32),

$$k_*\lambda\sim S_{L,\lambda}^{-1/4}(1+Pm)^{1/8},\qquad \gamma_{\mathrm t}\sim\frac{v_{Ay}}{\lambda}\,S_{L,\lambda}^{-1/2}(1+Pm)^{-1/4},$$

with $\gamma_{\mathrm t}$ the tearing growth rate (page-local; the source
writes $\gamma$) and inner-layer width $\delta_{\mathrm{in}}/\lambda\sim k_*\lambda$
(Eq. D33). The FKR branch ($k_y\gg k_*$) has
$\gamma_{\mathrm t}\lambda/v_{Ay}\sim S_{L,\lambda}^{-3/5}(k_y\lambda)^{-2/5}$
and the Coppi branch ($k_y\ll k_*$)
$\gamma_{\mathrm t}\lambda/v_{Ay}\sim S_{L,\lambda}^{-1/3}(1+Pm)^{-1/3}(k_y\lambda)^{2/3}$
(Eqs. D34, D36); for general $n$,
$\gamma_{\mathrm t}\lambda/v_{Ay}\sim S_{L,\lambda}^{-(n+1)/(3n+1)}(1+Pm)^{-n/(3n+1)}$
(Eq. D40). The fastest mode fits in a sheet of length $\xi$ if
$\xi/\lambda\gtrsim S_{L,\lambda}^{1/4}(1+Pm)^{-1/8}$ (Eq. D37).

## Disruption scale

In the turbulence, $v_{Ay}\sim\delta Z_\lambda$, and disruption occurs where
$\gamma_{\mathrm t}\tau_{\mathrm{nl}}\sim1$. With the aligned scalings of
[dynamic alignment](/properties/dynamic-alignment.md), Schekochihin (2022,
§7.1) obtains

$$\lambda_D\sim\lambda_{CB}\,Rm^{-4/7}(1+Pm)^{-2/7}$$

(Eq. 7.2), with $\lambda_{CB}$ the critical-balance scale and
$Rm\sim(\varepsilon/\eta_m)(L_\parallel/v_A)^2$ the magnetic Reynolds number
based on $\lambda_{CB}$ (Eq. 6.23). $\lambda_D$ lies above the Boldyrev
dissipation cutoff, and so matters, when
$[Rm/(1+Pm)^{10}]^{2/21}\gg1$ (Eq. 7.3). A disrupted sheet breaks into
$N\sim Rm^{1/14}(1+Pm)^{2/7}$ islands (Eq. 7.6; page-local $N$, not the
polynomial degree). The review cites two views of what disruption does and
says they agree on the spectrum (§7.1, Eqs. 7.7–7.8, 7.23–7.24): islands grow until
the sheet collapses into flux ropes of aspect ratio
$\sim Rm^{-1/14}(1+Pm)^{3/14}$ (X-point collapse, after Uzdensky & Loureiro
2016; Mallet et al. 2017), or alignment is not lost abruptly because the
tearing angle matches $\sin\theta_{\lambda_D}$ (Boldyrev & Loureiro 2017).

## The recursive cascade

Below a disruption the structures have alignment reset to order unity and
Kolmogorov-like amplitudes, $\delta Z_{\lambda_n^-}\sim(\varepsilon\lambda_n)^{1/3}$
(Eq. 7.10), then realign and are disrupted again. The disruption scales obey
$\lambda_{n+1}\sim S_{L,\lambda_n}^{-4/7}(1+Pm)^{-2/7}\lambda_n$ with
$S_{L,\lambda_n}\sim Rm(\lambda_n/\lambda_{CB})^{4/3}$ (Eqs. 7.9, 7.11), so
that (Eq. 7.12)

$$\frac{\lambda_n}{\lambda_{CB}}\sim\left[Rm^{-4/7}(1+Pm)^{-2/7}\right]^{\frac{21}{16}\left[1-(5/21)^n\right]}\ \longrightarrow\ Rm^{-3/4}(1+Pm)^{-3/8}.$$

Just above each disruption, $\tau_{\mathrm{nl}}^{-1}\sim\gamma_{\mathrm t}$
gives $\delta Z_{\lambda_n^+}\sim\varepsilon^{2/5}\eta_m^{-1/5}(1+Pm)^{1/10}\lambda_n^{3/5}$
(Eq. 7.14). The spectrum is bracketed by the two families (Eq. 7.15):

$$\varepsilon^{2/3}k_\perp^{-5/3}\ \lesssim\ E(k_\perp)\ \lesssim\ \varepsilon^{4/5}\eta_m^{-2/5}(1+Pm)^{1/5}k_\perp^{-11/5},$$

and the review takes the $-11/5$ upper envelope as the expected effective
slope (after Mallet et al. 2017 and Boldyrev & Loureiro 2017). The envelopes
meet at $\lambda_\infty\sim\eta_m^{3/4}\varepsilon^{-1/4}(1+Pm)^{-3/8}$
(Eq. 7.16). Through the range the alignment increases again below each
$\lambda_n$ (Eqs. 7.20–7.21), the parallel coherence length lies between
$v_A\varepsilon^{-1/3}\lambda_n^{2/3}$ and
$v_A\varepsilon^{-1/5}\eta_m^{-2/5}(1+Pm)^{1/5}\lambda_n^{6/5}$ (Eq. 7.22),
the turbulence becomes less anisotropic, and the $k_\parallel^{-2}$ spectrum
of [critical balance](/properties/critical-balance.md) continues. The 2D
spectrum in this range has CB exponent $6/5$ and the exponents of App. C,
Eq. C24.

## Restoration of the Kolmogorov cutoff

The dissipation cutoff of the tearing-mediated range is Kolmogorov-scaled
(Eq. 7.19):

$$\lambda_{\mathrm d}^{\mathrm K}\sim\lambda_{CB}\left[\frac{Rm}{1+Pm}\right]^{-3/4}\sim\frac{(\nu+\eta_m)^{3/4}}{\varepsilon^{1/4}}$$

(page-local symbol). This is the review's resolution of the alignment dispute
(§1, §7.2.2): Beresnyak's numerical evidence for a Kolmogorov-scaled
dissipation scale and Boldyrev's aligned $-3/2$ inertial range are "both
right, in a sense".

## Resolution requirements

From these scalings the review derives rough Reynolds-number thresholds for
numerical confirmation (§7.2.2, §7.3), with "the smallest large number" taken
as 3: $\lambda_D$ exceeds the Boldyrev cutoff by a factor 3 only at
$Rm\gtrsim10^5$, and exceeds the Kolmogorov cutoff by a factor 3 at
$Rm\gtrsim10^3$ for $Pm\sim1$. *(Compiler check, not in the sources: the
ratios are $Rm^{2/21}$ and $Rm^{5/28}$ at $Pm\sim1$, and $3^{21/2}\approx1.0\times10^5$,
$3^{28/5}\approx4.7\times10^2$.)* A fast-reconnection-mediated range inside
the aligned cascade would need
$Rm\gtrsim\epsilon_{\mathrm{rec}}^{-7}(1+Pm)^{-1/2}\sim10^{14}(1+Pm)^3$
(Eq. 7.26), with $\epsilon_{\mathrm{rec}}\sim10^{-2}(1+Pm)^{-1/2}$ the
dimensionless fast reconnection rate (page-local); fast reconnection takes
over where $\sin\theta_\lambda\lesssim\epsilon_{\mathrm{rec}}$ (Eq. 7.25).

## Numerical evidence cited

Schekochihin (2022, §7.3, Fig. 15) cites Dong et al. (2018), whose 2D
simulation at $Rm=10^6$ on a $64{,}000^2$ grid shows a $k_\perp^{-11/5}$
spectrum below a break at the disruption scale, and Dong et al. (2021, an APS
DPP abstract) for a 3D "sub-inertial range" with slope $-11/5$ and break
scaling as $Rm^{-4/7}$ at $Rm>10^5$. It cites Huang et al. (2017), who find
disruption at a ratio of growth rate to shear rate of "a few" rather than
$\approx1$, depending on noise (footnote 103). Simulations of
reconnection-driven turbulence report various slopes: steeper than $-2$
(Bárta et al. 2011; Huang & Bhattacharjee 2016), $-11/5$ (Tenerani & Velli
2020), $-12/5$ (Loureiro & Boldyrev 2020), all cited by the review (§7.4.3,
App. D.6.3).

## Reconnection primer: Sweet–Parker, plasmoids, fast reconnection

The review's App. D (as background, with the author's modifications)
supplies the reconnection results the turbulence theory uses:

- **Sweet–Parker** (the review cites Sweet 1958, Parker 1957, and Park et
  al. 1984 for the large-$Pm$ form): sheet aspect ratio
  $\delta_{\mathrm{SP}}/\ell\sim(1+Pm)^{1/4}S_{L,\ell}^{-1/2}$ for a sheet of
  length $\ell$ ($\delta_{\mathrm{SP}}$, $\ell$ page-local), outflow speed
  $v_{Ay}/\sqrt{1+Pm}$ (Eqs. D47–D51).
- **Plasmoid instability** (the review cites Loureiro et al. 2007): a
  Sweet–Parker sheet is tearing-unstable with a growth rate increasing with
  its Lundquist number (Eq. D52); the critical outflow-based Lundquist number
  is $S_{L,c}\sim10^4$ (Eq. D53, page-local).
- **Ideal tearing** (the review cites Pucci & Velli 2014): the critical aspect
  ratio at which tearing becomes "ideal" is
  $\xi/\lambda\sim S_{L,\lambda}^{1/2}(1+Pm)^{1/4}$, equivalently
  $S_{L,\xi}^{1/3}(1+Pm)^{1/6}$ with the length-based Lundquist number, so
  Sweet–Parker sheets (aspect ratio $S_{L,\xi}^{1/2}$) never form above
  $S_{L,\xi}\sim10^5$–$10^6$ (Eqs. D57–D59, citing Huang et al. 2017).
- **Recursive tearing.** The author's "embedding" modification of the
  Shibata & Tanuma (2001) scheme gives a $k_\perp^{-4}$ island spectrum,
  energetically negligible next to $k_\perp^{-11/5}$ (Eqs. D68–D74).
- **Fast plasmoid reconnection** (the review cites Uzdensky et al. 2010):
  dimensionless reconnection rate $\sim S_{L,c}^{-1/2}\sim10^{-2}(1+Pm)^{-1/2}$,
  independent of the global Lundquist number (Eq. D81); plasmoid
  flux and width distributions both fall off as the inverse square of the
  flux and of the width (Eq. D86, after Loureiro et al. 2012); a
  plasmoid chain has a $k^{-2}$ spectrum (Eqs. D89–D94).
- **Stochastic reconnection** (the review cites Lazarian & Vishniac 1999
  and Eyink et al. 2011) via Richardson diffusion of field lines (Eqs. D97–D113); the
  review argues that it is compatible with alignment (see [dynamic
  alignment](/properties/dynamic-alignment.md)).

## Qualifications

- **Printed slip, Eq. (7.17), p. 46 of arXiv v3.** The tearing-cascade cutoff
  is printed as
  "$\lambda_\eta\sim\varepsilon^{-3/4}\eta^{3/4}(1+\mathrm{Pm})^{3/2}\sim\lambda_{CB}\mathrm{Rm}^{-3/4}(1+\mathrm{Pm})^{3/2}$"
  (source notation, $\eta$ the magnetic diffusivity). *(Compiler check, not
  in the sources:* with Eqs. 4.3 and 6.23,
  $\lambda_{CB}Rm^{-3/4}=\varepsilon^{-1/4}\eta_m^{3/4}$, and
  $\varepsilon^{-3/4}\eta_m^{3/4}$ does not have the dimension of a length;
  the exponent of $\varepsilon$ must be $-1/4$, as in Eqs. 6.11, 7.16 and
  7.19.)
- **Label mismatch, §7.2.2, p. 46.** The text calls the condition of Eq.
  (7.18) the one for "the range $[\lambda_D,\lambda^K_\eta]$" to be
  non-empty, but Eq. (7.18) uses the tearing-cascade cutoff defined in Eq.
  (7.17); the Kolmogorov cutoff $\lambda^K_\eta$ is introduced only in Eq.
  (7.19).
- Mallet et al. (2017) and Boldyrev & Loureiro (2017) differ on the physical
  nature of disruption but, as the review reports, agree on the $-11/5$
  envelope (§7.1).
- The review (footnote 105) cites Kowal et al. (2020), who attribute reconnection-layer turbulence to
  Kelvin–Helmholtz rather than tearing, but with a reconnecting field ten
  times the guide field, outside the RMHD regime.
- The same disruption mechanism reappears in the subviscous range at large
  $Pm$ (§11; see [critical balance](/properties/critical-balance.md)) and in
  the folds of the [small-scale dynamo](/results/small-scale-dynamo.md)
  (§13.3), and controls the decay rate of [decaying MHD
  turbulence](/results/decaying-mhd-turbulence.md) (§12).

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §1; §7 (Eqs. 7.1–7.27), §7.1, §7.2.2, §7.3, §7.4.3; §8.2; App. C (Eq. C24); App. D.1–D.7 (Eqs. D2–D116); footnotes 103, 105.
