---
type: Definition
title: "Law of the wall"
description: "The inner-layer mean-velocity profile of wall-bounded turbulence — viscous sublayer, buffer layer and logarithmic layer in wall units — with the constants, composite fits and damping functions the sources use, and its role as the target every wall model must reproduce."
status: established
aliases: [logarithmic law, log law, law-of-the-wall profile, inner-layer profile]
tags: [boundary-layer, wall-model, wmles, rans]
timestamp: 2026-10-25T13:30:00Z
---

# Law of the wall

The law of the wall states that, in the inner layer of a smooth-wall turbulent
flow in equilibrium, the mean velocity scaled by the friction velocity is a
universal function of the wall distance in viscous units,
$u^+=f(y^+)$, with $u^+=\langle u\rangle/u_\tau$, $y^+=y/\delta_\nu$,
$u_\tau=\sqrt{\tau_w/\rho_w}$ and $\delta_\nu=\nu_w/u_\tau$ (let $f$ denote this
universal profile, page-local). Its two asymptotes are the viscous sublayer,
$u^+=y^+$, and the logarithmic layer,

$$u^+=\frac1\kappa\ln y^++B ,$$

joined through a buffer layer. Every wall model of this bundle is a way of
inverting $f$ (or an ODE whose solution is $f$) to obtain $\tau_w$ from a
velocity sampled away from the wall; see the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md).

## Constants used by the sources

The sources do not agree on one pair $(\kappa,B)$; each states its own values,
and the choice is part of the model.

| Source | $\kappa$ | $B$ | Other constants | Use |
|---|---|---|---|---|
| [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), Eq. (1) | 0.41 | 5.2 | quadratic branch below $y^+=23$ | algebraic wall model in [CharLES](/software/charles.md) |
| [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), Eq. (1) | 0.4 | 5 | | algebraic wall model in [LESGO](/software/lesgo.md); reference for log-layer mismatch |
| [Fowler et al. (2022)](/sources/fowler-2022.md), App. C | 0.4 | 4.95 | $\kappa_2=9.753$, $\beta=1.903$ (fit) | composite fit (C1); their Fig. 4 log law uses $B=5.0$ |
| [Griffin et al. (2023)](/sources/griffin-2023.md), §1 | 0.41 | — | $A^+=17$ | mixing length with van Driest damping |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.D | 0.38 (DNS value at $Re_\tau=4200$) | — | | reference slope for the log-layer error of WMLES |

Griffin et al. (2023, §3) test Reynolds-number-dependent constants fitted to
the incompressible channel DNS of Lee & Moser (as recalled by them): at
$Re_\tau=\{182,543,1000,1990,5190\}$, $\kappa=\{0.400,0.408,0.400,0.391,0.391\}$
and $A^+=\{18.2,17.4,17.0,16.5,16.5\}$. The fitted values improve their
compressible wall model only modestly at $Re_\tau^*=190$ and not at all at
$Re_\tau^*=590$, so they keep $\kappa=0.41$, $A^+=17$.

How much the constants matter is quantified by Lozano-Durán et al. (2022,
§IV.C, Eq. 12): a 10 % error in $\kappa$ or in $B$ produces about 6 % or 3 %
error in $u_\tau$, less than a 10 % error in the LES velocity at the matching
point; their fuselage WMLES errors saturate at about 2 %, which they attribute
to a 3 % deviation in $\kappa$ (§V.C). The constants therefore set an accuracy
floor of wall-modelled LES that grid refinement does not remove (details on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page).

## Composite profiles across the buffer layer

A wall model sampled in the buffer layer needs a single smooth $f(y^+)$.

- **Piecewise algebraic profile** (Lozano-Durán et al. 2022, Eq. 1):
  $u^+=y^++a_1(y^+)^2$ for $y^+<23$ and the log law otherwise, with $a_1$
  fixed by $C^1$ continuity at $y^+=23$ (value not printed).
- **Smooth fit of the full-equilibrium solution** (Fowler et al. 2022, Eqs.
  C1–C2), fitted to the numerical solution of the mixing-length equilibrium
  ODE with van Driest damping:

  $$f(y^+)=\left[\frac1\kappa\ln(\kappa_2+y^+)+B\right]\left[1+\left(\frac{y^+}{\kappa_1}\right)^{-\beta}\right]^{-1/\beta},\qquad \kappa_1=\frac1\kappa\ln\kappa_2+B,$$

  with $\kappa=0.4$, $B=4.95$, $\kappa_2=9.753$, $\beta=1.903$ (here $\beta$
  is the fit exponent, page-local). The choice of $\kappa_1$ makes
  $f\to y^+$ in the viscous sublayer. The fit error is below 1 % for $y^+>5$
  and below 2.25 % for $0\le y^+\le5$. Fowler et al. reject Reichardt's (1951)
  profile, as they recall it, because its error exceeds 3 % near $y^+\sim10$.
- **Mixing length with van Driest damping**, the differential form behind
  both fits: the eddy viscosity is $\nu_t=\kappa y\,u_\tau(1-e^{-y^+/A^+})^2$,
  and integrating the constant-stress equation gives $f$ (Griffin et al.
  2023, Eq. 1.2, in its incompressible form; see Qualifications for the
  printed form).

## Generalizations carried by the sources

- **Rotating channels.** The supervised wall model HYK19 analysed by Vadrot
  et al. (2023b, §II.B.2, Eq. 5) learns the departure of the LES velocity from
  an empirical profile $g(y^+,l^+_\Omega)$ that equals $\kappa^{-1}\ln y^+$
  without rotation and switches to a linear-plus-log form beyond
  $y^+=l^+_\Omega/\kappa$, with $l_\Omega=u_\tau/(2\Omega_{\mathrm{rot}})$ the
  rotation length (page-local). Without rotation the network therefore
  predicts a wall-distance-dependent intercept in place of $B$.
- **Compressible flows.** With variable density and viscosity the profile
  holds only after a [compressible velocity transformation](/definitions/compressible-velocity-transformation.md);
  Griffin et al. (2023, §3) report, citing Yang & Lv, that the classical van
  Driest damping is consistent with the van Driest transformation and its
  semi-local version (written in $y^*$) with the Trettel–Larsson one.
- **Pressure gradients.** The equilibrium fit of Meneveau (2020), as used by
  Fowler et al. (2022, Algorithm 1), returns $\langle u_\tau\rangle h_{\mathrm{wm}}/\nu$
  as a function of $U_{\mathrm{LES}}h_{\mathrm{wm}}/\nu$ and a dimensionless
  wall-parallel pressure gradient, and returns zero friction (separation) for
  strong adverse gradients.

## The law of the wall as a constraint

Vadrot et al. (2023b, §V) make preservation of the law of the wall the minimum
requirement of any learned wall model: a model must reproduce the log law in
channel flow at all Reynolds numbers, seen and unseen, before it is credited
with improvements elsewhere (see [machine-learning wall models](/methods/machine-learning-wall-model.md)).
Their a priori test of the ZHY21/ZYZY22 networks feeds a law of the wall built
by stitching the $Re_\tau=5200$ DNS wall layer to $u^+=\kappa^{-1}\ln y^++B$ at
$y^+=100$ (§IV.B). The mean-velocity departure from the log law is the
[log-layer mismatch](/definitions/log-layer-mismatch.md).

The friction velocity is also the first quantity a near-wall LES must get
right without a wall model: [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§7.2–7.4) report $u_\tau$ errors in pipe flow at $Re_\tau=1000$ of $+15.3$ %
(no model), $+9.6$ % (Smagorinsky with van Driest damping) and $-1.8$ %
(implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md))
on a uniform mesh with $\Delta x^+=\Delta y^+\approx9$.

## Qualifications

- The constants are source choices, not measurements of this bundle; the
  table records them and no value is preferred here.
- Griffin et al. (2023) print Eq. (1.2) as
  $\mu_t=\kappa y\langle\rho\rangle\sqrt{\tau_w/\langle\rho\rangle}\,(1-\exp(y^+/A^+))^2$,
  without the minus sign in the exponent; their own text describes a damping
  function that tends to the undamped mixing length away from the wall, which
  holds only for $(1-e^{-y^+/A^+})^2$. In §3 they print "$\kappa$ … 4.1" for
  the 0.41 stated in §1 and at the end of §3.

# Citations

- [Fowler et al. (2022)](/sources/fowler-2022.md) — App. C, Eqs. (C1)–(C2), Fig. 17; Algorithm 1; Fig. 4.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §IV.C, Eq. (12); §V.C.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1, Eq. (1.2); §3, Fig. 6.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II.B, Eqs. (1)–(6); §IV.B; §V.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D, Fig. 8.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.2–7.4, Figs. 25–27.
