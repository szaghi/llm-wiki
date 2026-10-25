---
type: Property
title: "Critical balance and the anisotropic MHD cascade"
description: "Critical balance equates the linear Alfvén time and the nonlinear time at every scale of strong MHD turbulence; it fixes the parallel spectrum k_par^-2, the anisotropy l_par ~ lambda^(2/3) of Goldreich–Sridhar, the weak-to-strong transition scale, and frames imbalance and residual energy."
status: established
aliases: [CB, Goldreich–Sridhar theory, GS95, strong MHD turbulence, weak MHD turbulence, imbalanced MHD turbulence, residual energy]
tags: [mhd, astrophysics, plasma, anisotropy, energy-cascade]
timestamp: 2026-10-25T13:29:00Z
---

# Critical balance and the anisotropic MHD cascade

**Critical balance (CB)** is the conjecture that in strong MHD turbulence with
a mean field the linear (Alfvén) propagation time along the local field and
the nonlinear interaction time across it are comparable at every scale,

$$\tau_A\sim\frac{l_\parallel}{v_A}\ \sim\ \tau_{\mathrm{nl}},$$

where $\lambda$ is the perpendicular scale of a fluctuation and $l_\parallel$
its coherence length along the **local** field. As recalled by
[Schekochihin (2022)](/sources/schekochihin-2022.md) (§2.3), it is due to
Goldreich & Sridhar (1995, 1997), anticipated by Higdon (1984), and the
review calls its consequence for the parallel spectrum "the least
controversial" result of the field (§5). CB is stated here for the
[reduced-MHD](/definitions/reduced-mhd.md) system; the perpendicular spectrum
it predicts is modified by [dynamic
alignment](/properties/dynamic-alignment.md) and, at small scales, by
[tearing](/results/tearing-mediated-mhd-turbulence.md).

## From K41 to Goldreich–Sridhar

Schekochihin (2022, §2) recalls three dimensional theories, with $\varepsilon$
the energy flux (equal to the dissipation rate in a steady state) and
$\delta u_\lambda$ the velocity increment at scale $\lambda$:

| Theory (as recalled) | Assumptions | Scalings |
|---|---|---|
| Kolmogorov (1941) | constant flux, $\tau_{\mathrm{nl}}\sim\lambda/\delta u_\lambda$ | $\delta u_\lambda\sim(\varepsilon\lambda)^{1/3}$, $E(k)\sim\varepsilon^{2/3}k^{-5/3}$ (Eqs. 2.1–2.2) |
| Iroshnikov (1963), Kraichnan (1965) | cascade time $\tau_{\mathrm{nl}}^2/\tau_A$, isotropy | $\delta u_\lambda\sim(\varepsilon v_A\lambda)^{1/4}$, $E(k)\sim(\varepsilon v_A)^{1/2}k^{-3/2}$ (Eq. 2.5) |
| Goldreich & Sridhar (1995) | cascade time $\sim\tau_A\sim\tau_{\mathrm{nl}}$ (CB) | $E(k_\perp)\sim\varepsilon^{2/3}k_\perp^{-5/3}$, $l_\parallel\sim v_A\varepsilon^{-1/3}\lambda^{2/3}$ (Eqs. 2.6–2.11) |

The review judges the isotropy of the Iroshnikov–Kraichnan argument
"illogical": the field it invokes to make interactions weak is precisely what
makes the cascade anisotropic. Under CB the perpendicular cascade is
Kolmogorov-like, and $l_\parallel\propto\lambda^{2/3}$ means eddies become
more elongated along the field as $\lambda$ decreases (scale-dependent
anisotropy).

## Why critical balance: causality and the weak-turbulence limit

Two justifications are given (§4–§5, recalled from Boldyrev 2005 and Nazarenko
& Schekochihin 2011):

- **Causality.** Information propagates along the field at $v_A$, so no
  structure can stay coherent over a length longer than
  $l_\parallel\sim v_A\tau_{\mathrm{nl}}$; fluctuations with
  $\tau_A\gg\tau_{\mathrm{nl}}$ break up into shorter ones.
- **Weak turbulence becomes strong.** If $\tau_A\ll\tau_{\mathrm{nl}}$ at the
  outer scale (weak turbulence, WT), three-wave interactions require one of
  the three modes to have $k_\parallel=0$ (resonance $q_\parallel=k_\parallel$,
  $p_\parallel=0$, Eq. 4.2), so WT cascades only in $k_\perp$ at fixed
  $k_\parallel$. The random-walk estimate
  $\tau_c\sim\tau_{\mathrm{nl}}^2/\tau_A$ (Eq. 4.5; recalled from Ng &
  Bhattacharjee 1997 and Goldreich & Sridhar 1997) gives the balanced WT
  spectrum
  $$E(k_\perp)\sim\left(\frac{\varepsilon}{\tau_A}\right)^{1/2}k_\perp^{-2}$$
  (Eq. 4.7; confirmed numerically by Perez & Boldyrev 2008 and Boldyrev &
  Perez 2009, as recalled). The nonlinearity grows towards small $\lambda$
  until CB is reached at the **critical-balance scale** (page-local symbol)
  $$\lambda_{CB}\sim\varepsilon^{1/2}\left(\frac{L_\parallel}{v_A}\right)^{3/2}$$
  (Eqs. 4.3, 4.8), with $L_\parallel$ the parallel outer scale — "the only
  dimensionally correct" scale built from $\varepsilon$ and $L_\parallel/v_A$,
  consistently with the RMHD rescaling symmetry. The review concludes that WT
  is asymptotically "irrelevant": it is a transient range above
  $\lambda_{CB}$, and the transition was first captured numerically by
  Meyrand et al. (2016), as recalled (Fig. 3).

### Weak turbulence: the $k_\parallel=0$ condensate

Because every WT interaction scatters a wave off a zero-frequency
$k_\parallel=0$ mode, Schekochihin (2022, §4.4, App. A) argues that the
standard WT kinetic equation (Galtier et al. 2000, derived in App. A.2 under
the random-phase approximation) is "at best incomplete and at worst wrong":
the $k_\parallel=0$ "2D condensate" is forced by pairs of counter-propagating
waves, builds up even when unforced, and is itself strongly turbulent and
critically balanced. In the review's unpublished weak RMHD runs (Yousef &
Schekochihin 2009) the unforced condensate has a spectrum close to
$k_\perp^0$, against the $k_\perp^{-1}$ predicted by the author's own earlier
theory (Schekochihin et al. 2012), which the review says "fails
quantitatively". For broad-band forcing, the review derives (App. A.4,
Eqs. A25–A30, new there and with the conjecture that the condensate is
unaligned) a condensate spectrum
$E_{0,2D}\sim(\varepsilon L_\parallel v_A)^{1/2}k_\perp^{-2}$, which recovers
the $k_\perp^{-2}$ WT exponent ("spectral continuity"). Imbalanced WT is
harder still: the standard closure cannot accommodate
$\varepsilon^+\gg\varepsilon^-$, and its power-law solutions only satisfy
$\mu^++\mu^-_0=-4$ for the exponents of waves and condensate (Eqs. 4.9,
A23), with non-universal prefactors.

## The parallel spectrum

With CB, the energy of a fluctuation is transferred in one Alfvén time, so
$(\delta Z^\pm_{l_\parallel})^2/(l_\parallel/v_A)\sim\varepsilon^\pm$ and
(Eq. 5.1)

$$\delta Z^\pm_{l_\parallel}\sim\left(\frac{\varepsilon^\pm l_\parallel}{v_A}\right)^{1/2},\qquad E^\pm(k_\parallel)\sim\frac{\varepsilon^\pm}{v_A}\,k_\parallel^{-2}.$$

This scaling uses only $\varepsilon^\pm$ and $l_\parallel/v_A$ — the
combination the [RMHD rescaling symmetry](/definitions/reduced-mhd.md)
allows — and it is independent of the perpendicular theory, which is why it
survives alignment and tearing. An equivalent Lagrangian-frequency form,
$E^\pm(\omega_f)\sim\varepsilon^\pm\omega_f^{-2}$ with
$\omega_f=k_\parallel v_A$ (page-local frequency symbol), is recalled from
Beresnyak (2015) (Eq. 5.2). Cited evidence: $\approx k_\parallel^{-1.9}$ in
Beresnyak (2015) and $k_\parallel^{-2}$ for the magnetic field in Meyrand et
al. (2019) (§5.2, footnote 11).

### Measuring along the local field

Scale-dependent anisotropy is visible only when increments are taken along
the **local** field. Measured along the global mean field, the parallel
increments are swamped by perpendicular decorrelation, because a field line
wanders by $\Delta l_\perp\sim\lambda\,\delta b_{L_\perp}/\delta b_\lambda\gg\lambda$
(Eq. 5.8). The method recalled in §5.3 (Cho & Vishniac 2000; Chen et al.
2011, and later work) uses the local field
$\boldsymbol B_{\mathrm{loc}}=\boldsymbol B_0+[\boldsymbol b_\perp(\boldsymbol r+\boldsymbol l)+\boldsymbol b_\perp(\boldsymbol r)]/2$
and conditions structure functions on the angle between the separation
$\boldsymbol l$ and $\boldsymbol B_{\mathrm{loc}}$ (Eqs. 5.6–5.12); it was
extended to the three directions $l_\parallel$, $\xi$, $\lambda$ of
[dynamic alignment](/properties/dynamic-alignment.md). The review quotes a
second-order exponent of 1 along the local field and between $2/3$ and $1/2$
across it in the solar wind, closer to $1/2$ in simulations (§5.3).

### Two-dimensional spectrum

Schekochihin (2022, App. C, partly after Schekochihin et al. 2016) derives the
2D spectrum $E_{2D}(k_\perp,k_\parallel)$ of critically balanced turbulence
with the CB line $k_\parallel\sim k_\perp^{1/2}$ (aligned case):

$$E_{2D}\sim\begin{cases}k_\parallel^{-6}\,k_\perp, & k_\parallel\gtrsim k_\perp^{1/2},\\ k_\parallel^{0}\,k_\perp^{-2}, & k_\parallel\lesssim k_\perp^{1/2},\end{cases}$$

(Eq. C23). The flat $k_\parallel$ spectrum below the CB line is "the Fourier
signature of causality" (white noise along the field), not evidence of
quasi-2D motions; the review calls the opposite reading — that CB implies a
$k_\parallel$ spectrum peaked at the CB line — a fallacy that "has made it
into a number of published texts" (App. C.1). The large-scale $k_\perp^{1}$
part is a thermal (equipartition) range maintained against turbulent
diffusion (Eqs. C14–C19). The $k_\parallel^{-6}$ exponent is reported as
confirmed by Squire et al. (2022) (footnote 96).

## Imbalanced turbulence

When $\varepsilon^+\ne\varepsilon^-$, Schekochihin (2022, §9.2) summarizes the
numerical facts (Beresnyak & Lazarian 2008, 2009; the unpublished Mallet &
Schekochihin 2011 runs; Meyrand & Squire 2020, private communication): the
stronger field has the steeper perpendicular spectrum; the energy ratio grows
at least like $(\varepsilon^+/\varepsilon^-)^2$ (Eq. 9.1); the stronger
field has the shorter parallel coherence length; the weaker field's parallel
spectrum is robustly $k_\parallel^{-2}$. Recalled theories:

- **Lithwick, Goldreich & Sridhar (2007):** both fields share the weaker
  field's correlation time, giving
  $\delta Z^+_\lambda/\delta Z^-_\lambda\sim\varepsilon^+/\varepsilon^-$ and
  equal spectral slopes (Eqs. 9.2–9.3); its parallel-scale predictions
  (9.5–9.6) are inconsistent with the cited numerics.
- **Perez & Boldyrev (2009):**
  $\delta Z^+_\lambda/\delta Z^-_\lambda\sim(\varepsilon^+/\varepsilon^-)^{1/2}$
  (Eq. 9.4), which the review reports as contradicted by Beresnyak & Lazarian
  (2010).

The review's **new theory** (§9.6) has two "semi-local" cascades: the stronger
field is cascaded locally in $\lambda$ by the weaker one, while the weaker
field is cascaded locally in $l_\parallel$ but non-locally in $\lambda$, by
stronger-field fluctuations at a larger $\lambda'$ with the same parallel
coherence length (Eqs. 9.9–9.15). It yields
$\delta Z^+_\lambda/\delta Z^-_\lambda\sim(\varepsilon^+/\varepsilon^-)(\lambda/L_\perp)^{\alpha_i}$
(Eq. 9.17; $\alpha_i$ page-local for the source's $\alpha$) and the weaker
field's $k_\parallel^{-2}$ spectrum. Requiring both dissipation scales to be
"pinned" together fixes $\alpha_i$ (Eq. 9.26) as a ratio
$\ln(\varepsilon^+/\varepsilon^-)/\ln Re_{\mathrm{eff}}$ times an order-unity
factor, so $\alpha_i\to0$ as the Reynolds number grows: asymptotically the two
spectra are parallel, with logarithmic finite-Reynolds-number steepening of
the stronger field. The limits $\alpha_i=0$ recover Goldreich–Sridhar
(unaligned) and the aligned theory of §6.4. Parker Solar Probe data with an
Elsasser energy ratio $\approx15$ and the same $k^{-3/2}$ slope for both
fields (Chen et al. 2020, as recalled) "may be damning" for theories or
simulations that predict different slopes (§9).

## Residual energy

The residual energy
$E_{\mathrm{res}}$, the spectrum of $\langle|\boldsymbol u_\perp|^2\rangle-\langle|\boldsymbol b_\perp|^2\rangle$
(see [reduced MHD](/definitions/reduced-mhd.md)), is observed to be negative
(magnetic excess) with a spectrum close to $k_\perp^{-2}$ in the solar wind
(Chen et al. 2013, as recalled), while Beresnyak (2014) finds
$k_\perp^{-1.7}$ carrying a fraction $\approx0.15$ of the energy (§10). The
review rejects the older EDQNM explanation (Pouquet et al. 1976; Grappin et
al. 1982, 1983; Müller & Grappin 2005) as "necessarily wrong because
IK-based": under CB it would give $E_{\mathrm{res}}\sim E$ (Eq. 10.1). Its
own account (§10.4, heuristic): Elsasser alignment implies non-zero residual
energy (App. B, Eq. B5); shear layers ($\delta u>\delta b$) are
Kelvin–Helmholtz unstable while current sheets are stabilized by the field;
the RMHD nonlinearity drives $\langle\varpi^+\varpi^-\rangle<0$ (Elsasser
vorticities, page-local); and the most intense structures, current sheets,
are step functions with a $k_\perp^{-2}$ spectrum. An RMHD-consistent
$k_\perp^{-2}$ residual spectrum requires the intermittency exponent of
[dynamic alignment](/properties/dynamic-alignment.md) to take the value
$-1/4$ in the general form (Eq. 10.3), so the review classes it as an
intermittency effect. In weak turbulence the condensate carries a negative
residual energy comparable to its energy (App. A.5, after Wang et al. 2011).

## Below the viscous scale at large $Pm$

For $Pm=\nu/\eta_m\gg1$, Schekochihin (2022, §11; updating Cho et al. 2002,
2003 and Lazarian et al. 2004, as recalled) finds no parallel cascade in the
subviscous range: the magnetic spectrum is $E_b\propto k_\perp^{-1}$
(Eq. 11.5), interpreted as sharp repeated stripes, and the velocity spectrum,
set by a balance of viscous and tension forces with a flat tension spectrum,
is $E_u\propto k_\perp^{-4}$ (Eq. 11.9). Tearing can disrupt the stripes when
$Pm\gtrsim Re^{1/9}$ (Eqs. 11.10–11.17), giving yet another
Kolmogorov-scaled cutoff $\sim(\nu^3/\varepsilon_m)^{1/4}$, where
$\varepsilon_m$ (page-local) is the flux surviving into the subviscous
magnetic cascade.

## Scope

The review advocates CB as a universal principle for turbulence carrying
waves — kinetic plasma turbulence, stratified and rotating flows (§8.2) —
and quotes kinetic-Alfvén-wave slopes of $-7/3$ (CB, as recalled from Cho &
Lazarian 2004 and Schekochihin et al. 2009) against $-8/3$ (Boldyrev & Perez
2012) (§14). In its own robustness ranking, CB and the parallel cascade are
"quite safe", while alignment and the tearing-mediated range are "hotly
debated" (§8.2).

## Qualifications

- All relations are order-of-magnitude ("twiddle") estimates; the review
  stresses that the theory is order-unity inaccurate.
- The perpendicular exponent $-5/3$ of Goldreich–Sridhar is not the review's
  conclusion: it argues for an aligned $-3/2$ range (see [dynamic
  alignment](/properties/dynamic-alignment.md)) ending in a tearing-mediated
  range. The asymptotic perpendicular spectrum is recorded by the review as
  disputed (Beresnyak versus Boldyrev and coauthors, as recalled, §6–§7).
- The review discusses no turbulence closure (RANS, LES or subgrid model);
  its content bears on closure modelling only through cascade phenomenology
  and numerical-resolution arguments.

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §2 (Eqs. 2.1–2.11); §4 (Eqs. 4.2–4.13), §4.4; §5 (Eqs. 5.1–5.12), §5.2, §5.3; §8.2; §9 (Eqs. 9.1–9.28), §9.2, §9.6; §10 (Eqs. 10.1–10.4), §10.4; §11 (Eqs. 11.1–11.17); §14; App. A.2–A.5 (Eqs. A15, A23, A25–A41); App. C (Eqs. C3–C29).
