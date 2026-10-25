---
type: Result
title: "Small-scale turbulent dynamo"
description: "The small-scale (fluctuation) dynamo amplifies magnetic fields in folds at the resistive scale; Schekochihin (2022) argues that in saturation the folds are torn, setting the reversal scale at L Rm^-1/3 and seeding a local, critically balanced RMHD-like cascade below it."
status: hypothesis
aliases: [fluctuation dynamo, turbulent dynamo, saturated dynamo, tearing-limited dynamo, reconnection-limited dynamo]
tags: [dynamo, mhd, astrophysics, reconnection, dns]
timestamp: 2026-10-25T13:42:00Z
---

# Small-scale turbulent dynamo

The **small-scale (fluctuation) dynamo** is the exponential amplification of
a weak magnetic field by a turbulent flow without a mean field, at scales
smaller than the outer scale of the flow, followed by a nonlinear stage and a
saturated state of statistically steady MHD turbulence. [Schekochihin
(2022)](/sources/schekochihin-2022.md) (§13) reviews the classical picture
(as recalled from Batchelor 1950, Biermann & Schlüter 1951, Kazantsev 1968,
and the author's own earlier work, Schekochihin et al. 2002, 2004) and
proposes a **tearing-limited** theory of the saturated state: the folded
fields are disrupted by tearing, which sets their reversal scale and seeds a
local cascade that resembles the [tearing-mediated
turbulence](/results/tearing-mediated-mhd-turbulence.md) of the
strong-mean-field case. The page carries `status: hypothesis`: the author
presents the theory as new, supported by "tentative evidence", and leaves
open the central question of the saturated state (§13.3.4).

Page-local notation: $\ell$ is the scale of the stretching motions, $L$ the
outer scale, $\delta u_\ell$ the velocity increment at $\ell$,
$Rm_\ell=\delta u_\ell\ell/\eta_m$ and $Rm_L$ the magnetic Reynolds numbers
at $\ell$ and $L$, $Re_{\mathrm{eff},\ell}=\delta u_\ell\ell/(\nu+\eta_m)$,
$b_\lambda$ the amplitude (velocity units) of a field reversing across a
fold of width $\lambda$, $\varepsilon$ the energy flux of the turbulence.

## Kinematic stage and the onset of tearing

In the kinematic regime the field is organized in folds — long in the
direction of the field, reversing across a resistive width
$\lambda\sim\ell\,Rm_\ell^{-1/2}$ (Eq. 13.2, as recalled). Treating a fold
as a current sheet, the review (§13.3.1) applies the tearing growth rate of a
reversing field,

$$\gamma_{\mathrm t}\sim b_\lambda^{1/2}\lambda^{-3/2}\eta_m^{1/2}(1+Pm)^{-1/4}$$

(Eq. 13.3; page-local $\gamma_{\mathrm t}$), and finds that tearing outpaces
the resistive evolution of the fold once
$b_\lambda\sim\delta u_\ell\,Re_{\mathrm{eff},\ell}^{-1/2}$ (Eq. 13.4), i.e.
already when the field is far weaker than the flow. Hence the review's
statement that "a nonlinear dynamo is also a reconnecting dynamo".

## Self-similar nonlinear stage

Recalled from Schekochihin et al. (2002), Cho et al. (2009) and Beresnyak
(2012) (§13.3.2): once the field is strong enough to suppress the stretching
motions at scale $\ell$, the dynamo proceeds at the scale where
$\delta u_{\ell(t)}\sim b_\lambda(t)$ (Eq. 13.5), so

$$b_\lambda\sim(\varepsilon t)^{1/2},\qquad \ell(t)\sim\varepsilon^{1/2}t^{3/2}$$

(Eq. 13.6): magnetic energy grows linearly in time. The fraction of the
energy flux going into the field is quoted as 0.04–0.07 (Cho et al. 2009;
Beresnyak 2012), with $3/38$ from Xu & Lazarian (2016), all as recalled.

## Saturation: tearing-limited folds

When $\ell$ reaches the outer scale, the fold-reversal scale is set by
tearing (Eq. 13.7, condition 13.8) and not by Ohmic diffusion
(§13.3.3):

$$\lambda_R\sim L\,Rm_L^{-1/3}(1+Pm)^{-1/6}$$

(Eq. 13.9; $\lambda_R$ page-local), instead of the $L\,Rm_L^{-1/2}$ of the
author's earlier view. A torn fold of length $L$ yields
$N\sim Rm_L^{1/6}(1+Pm)^{1/3}$ islands (Eq. 13.10; page-local $N$). The flux
ropes so produced have amplitude given by Eq. (13.11) and a critically
balanced parallel length
$l_\parallel\sim L\,Rm_L^{-2/9}(1+Pm)^{-1/9}$ (Eq. 13.12), with the
outer-scale velocity playing the role of the Alfvén speed and the fold field
the role of a local mean field. The resulting cascade is a [critically
balanced](/properties/critical-balance.md) [RMHD](/definitions/reduced-mhd.md)
cascade with $\lambda_R$ in the role of the critical-balance scale and the
small ordering parameter

$$\frac{\delta u_{\lambda_R}}{\delta u_L}\sim\frac{\lambda_R}{l_\parallel}\sim Rm_L^{-1/9}(1+Pm)^{-1/18}\ll1$$

(Eq. 13.13). This cascade is [aligned](/properties/dynamic-alignment.md),
then disrupted by tearing at (Eq. 13.15)

$$\lambda_D\sim L\,Rm_L^{-41/63}(1+Pm)^{-41/126},$$

below which it has the $k^{-11/5}$ envelope of the tearing-mediated range,
and it ends at the Kolmogorov scale $\sim L\,Re_{\mathrm{eff},L}^{-3/4}$
(Eq. 13.16; $\lambda_D$ page-local). The review's conclusion is that
"universality is regained at small scales": even without a mean field, MHD
turbulence "manages to turn itself into RMHD (Alfvénic) turbulence, at least
in local patches", with statistics isotropic overall because the local mean
field fluctuates (§13.3.3, citing Beresnyak & Lazarian 2009 and St-Onge et
al. 2020 for the latter).

## Numerical evidence cited

- **Folds become current sheets.** The review cites its own unpublished
  simulations (Iskakov & Schekochihin 2008: $512^3$, $Pm=1$, $Re=1360$ with
  $Re=u_{\mathrm{rms}}/(\nu k_0)$, $k_0=2\pi$, Fig. 31) showing inflow–outflow
  patterns around field reversals and corrugated folds with plasmoid-like
  structures, and Beresnyak (2012, unpublished: $1024^3$, $Pm=10$,
  $Re\approx500$, Fig. 32) with the same features; none of these appear in
  the "Stokes" regime $Re\sim1$, $Pm\gg1$, where the saturated field stays
  smoothly folded at the resistive scale (§13.2, footnote 74).
- **Spectra.** In saturated-dynamo simulations the kinetic-energy spectrum
  steepens at large scales (an empirical $k^{-7/3}$) and becomes shallower,
  $\approx k^{-4/3}$, at small scales (Grete et al. 2021, as recalled), with
  magnetic-to-kinetic transfer via tension at small scales — consistent with
  reconnection in folds driving flows (§13.2, Fig. 33).
- **Tests of the tearing-limited theory.** Galishnikova et al. (2022, up to
  $2240^3$), designed to test the fold-tearing scenario, "appear to offer some
  tentative evidence" for the disruption of folds by tearing, for the scaling
  of the reversal scale with $Rm^{-1/3}$, and for a steeper-than-Kolmogorov
  spectrum ($\propto k^{-2}$ "or thereabouts") below $\lambda_R$ (§13.3.4).

## Saturation scenarios above $\lambda_R$

The theory does not say whether magnetic energy stays at $\lambda_R$ or moves
to the outer scale — "the central question of small-scale-dynamo theory"
(§13.3.4). Section 13.4 catalogues speculations, "not necessarily all
mutually exclusive":

- multiscale folds with $b_\lambda\propto\lambda^{3/5}$, i.e. a $k^{-11/5}$
  magnetic spectrum (Eq. 13.17, §13.4.1);
- a $k^{-1}$ magnetic spectrum above $\lambda_R$ (Eq. 13.18, after Yousef et
  al. 2007) and a velocity cascade depleted by dynamo losses,
  $E\propto k^{-(5+2\sigma_d)/3}$ when the rate of transfer into the folds
  times the cascade time is a constant $\sigma_d$ (Eqs. 13.19–13.20,
  page-local $\sigma_d$; §13.4.2);
- **magnetoelastic turbulence**: a tangled field acts as an elastic medium
  with isotropic waves $\omega_f^2=k^2v_A^2$, $v_A^2=\langle b^2\rangle/3$
  (page-local $\omega_f$), and a weak, isotropic
  Iroshnikov–Kraichnan-like cascade $E(k)\sim(\varepsilon v_A)^{1/2}k^{-3/2}$
  (Eqs. 13.21–13.26, §13.4.3), with a polymer analogy;
- a fast-reconnection-limited dynamo with reversal scale
  $\sim\epsilon_{\mathrm{rec}}\ell$ if $Rm_\ell\gtrsim10^6(1+Pm)$
  (Eqs. 13.27–13.29, §13.4.4);
- the Xu & Lazarian (2016) scheme, which the review critiques: its spectral
  "overturning" at constant energy is not seen in $Pm\gg1$, $Re\sim1$ runs
  (§13.4.5);
- Subramanian's (1999) model with an effective resistivity
  $\eta_m+\tau\langle b^2\rangle$ and a reversal scale $L\,Rm_c^{-1/2}$,
  $Rm_c\sim10$–$100$ (Eqs. 13.30–13.32, §13.4.6; $\tau$, $Rm_c$ page-local);
- inverse magnetic-energy transfer via sporadic decay (Eqs. 13.33–13.35,
  §13.4.7) and a local shear dynamo (§13.4.8).

The decay of the saturated state, once forcing stops, is the subject of
[decaying MHD turbulence](/results/decaying-mhd-turbulence.md).

## Qualifications

- **Printed sign, §13.3.4, p. 111 of arXiv v3** (checked on the rendered
  page). The text reports Galishnikova et al. (2022) as supporting "the
  $\lambda_R\propto\mathrm{Rm}^{1/3}$ scaling of the field-reversal scale",
  and footnote 79 gives their version as
  "$\lambda_R\propto\mathrm{Rm}^{3/10}\mathrm{Pm}^{1/5}$", both with positive
  exponents; Eq. (13.9), p. 109, prints
  $\lambda_R\sim L\,Rm_L^{-1/3}(1+Pm)^{-1/6}$, a scale that decreases with
  $Rm$. The review does not say why the signs differ. Footnote 79 adds that
  Galishnikova et al. compare with tearing of a sinusoidal profile ($n=2$ in
  App. D.1.5) rather than the Harris-like $n=1$ of the main text.
  *(Compiler check, not in the sources: repeating the balance of Eq. 13.7,
  $\gamma_{\mathrm t}\sim\delta u_L/L$ with $b_\lambda\sim\delta u_L$, with the
  general-$n$ growth rate of Eq. D40 at $n=2$,
  $\gamma_{\mathrm t}\lambda/b_\lambda\sim S_{L,\lambda}^{-3/7}(1+Pm)^{-2/7}$,
  gives $\lambda_R\sim L\,Rm_L^{-3/10}(1+Pm)^{-1/5}$: the magnitudes of the
  footnote's exponents with negative signs, as in Eq. 13.9.)*
- The review records the competing view (Haugen et al. 2003, 2004; Beresnyak
  2012; Xu & Lazarian 2016, as recalled) that the saturated state is
  non-asymptotic and would become Kolmogorov-like with scale-by-scale
  equipartition at higher resolution (§13.2); Grete et al. (2021) and Bian &
  Aluie (2019) disagree on magnetic control of the small-scale cascade, as
  recalled. These are disagreements among un-ingested works reported by the
  review, not a bundle contradiction.
- The theory revises the author's earlier result (Schekochihin et al. 2002,
  2004) that the reversal scale is resistive, $L\,Rm^{-1/2}$.

# Citations

- [Schekochihin (2022)](/sources/schekochihin-2022.md) — §13 (Eqs. 13.2–13.35): §13.1, §13.2, §13.3.1–§13.3.4, §13.4.1–§13.4.8; footnotes 74, 79.
