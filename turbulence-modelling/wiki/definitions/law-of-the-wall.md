---
type: Definition
title: "Law of the wall"
description: "The inner-layer mean-velocity profile of wall-bounded turbulence — viscous sublayer, buffer layer and logarithmic layer in wall units — with the constants, composite fits and damping functions the sources use, and its role as the target every wall model must reproduce."
status: established
aliases: [logarithmic law, log law, law-of-the-wall profile, inner-layer profile]
tags: [boundary-layer, wall-model, wmles, rans]
timestamp: 2026-10-25T19:43:00Z
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
| [Gillyns et al. (2022)](/sources/gillyns-2022.md), §3, Eq. (3) | 0.38 | 4.1 | Reichardt profile; Österlund et al. values, as recalled | algebraic wall model in a spectral-element code |
| [Bae & Koumoutsakos (2022)](/sources/bae-2022.md), Eq. (3), Fig. 2 | 0.41 | 5.2 | | reference log law of the reinforcement-learning wall models |
| [Cao et al. (2022)](/sources/cao-2022.md), Eq. (8) | 0.40 | 5.5 | "for the low Reynolds number turbulent channel flow" | estimate of $u_\tau$ for a channel DNS at $Re_\tau=180$ |
| [Knopp (2022)](/sources/knopp-2022.md), §4, Eq. (26) | 0.41 | 5.0 | with Coles' wake, after Coles & Hirst | fit of boundary-layer thickness in adverse pressure gradient |
| [Cogo et al. (2022)](/sources/cogo-2022.md), Fig. 8 | 0.41 | 5.2 | | reference for transformed compressible profiles |

Griffin et al. (2023, §3) test Reynolds-number-dependent constants fitted to
the incompressible channel DNS of Lee & Moser (as recalled by them): at
$Re_\tau=\{182,543,1000,1990,5190\}$, $\kappa=\{0.400,0.408,0.400,0.391,0.391\}$
and $A^+=\{18.2,17.4,17.0,16.5,16.5\}$. The fitted values improve their
compressible wall model only modestly at $Re_\tau^*=190$ and not at all at
$Re_\tau^*=590$, so they keep $\kappa=0.41$, $A^+=17$. Gillyns et al. (2022,
§3) likewise note that more recent values after Lee & Moser are
$\kappa\simeq0.383$, $B\simeq4.25$, but keep 0.38 and 4.1; the effect of the
choice on $u_\tau$ is not assessed.

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
- **Reichardt's profile** (Gillyns et al. 2022, Eq. 3, as in Frère et al.
  2017, as recalled):

  $$u^+=\frac1\kappa\ln(1+\kappa y^+)+\left(B-\frac1\kappa\ln\kappa\right)\left(1-e^{-y^+/11}-\frac{y^+}{11}e^{-y^+/3}\right),$$

  with $\kappa=0.38$, $B=4.1$, inverted for $u_\tau$ in their equilibrium
  wall model (the source writes $C$ for $B$). Fowler et al. (2022) reject this
  profile for its error near $y^+\sim10$ (above); Gillyns et al. sample it at
  $y^+\ge63$, where the choice is not tested against an alternative.
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
- **Adverse pressure gradients.** [Knopp (2022)](/sources/knopp-2022.md)
  finds the log law robust in adverse-pressure-gradient boundary layers but
  confined below $y^+_{\log,\max}=1.78\,Re_\tau^{1/2}(\Delta p_s^+)^{-1/5}$, with
  $\Delta p_s^+=\nu\rho^{-1}u_\tau^{-3}dP/ds$ the inner-scaled pressure
  gradient, and a half-power law above it (Eq. 35; page-local symbols); the
  log layer then ends below $0.11\delta$ for $\Delta p_s^+>0.005$ and a
  Rotta–Clauser parameter above 4.5 (§5.2). Details on
  the [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
  page. Gillyns et al. (2022, §1) place the validity of the law of the wall
  at $y/\delta\lesssim0.15$ and expect an algebraic wall model to fail once
  Coles' wake reaches the matching point near separation.
- **Pressure gradients in wall models.** The equilibrium fit of Meneveau (2020), as used by
  Fowler et al. (2022, Algorithm 1), returns $\langle u_\tau\rangle h_{\mathrm{wm}}/\nu$
  as a function of $U_{\mathrm{LES}}h_{\mathrm{wm}}/\nu$ and a dimensionless
  wall-parallel pressure gradient, and returns zero friction (separation) for
  strong adverse gradients.

- **Hypersonic cold walls.** [Huang et al. (2022)](/sources/huang-2022.md)
  (§4.1, Eq. 4.5, Fig. 11) test logarithmic behaviour with the diagnostic
  function $y^+\,du^+/dy^+$ applied to the transformed velocity: it is nearly
  constant for $y^+\approx40$–100 in their Mach 2.5 and 4.9 quasi-adiabatic
  boundary layers at $Re_\tau=1172$, but their Mach 10.9 boundary layer with
  $T_w/T_r=0.20$ shows no wide constant region up to that $Re_\tau$, which they
  attribute to reduced scale separation from strong wall cooling. Above the
  log region the mean velocity follows a power law
  $\langle u\rangle/U_\infty=(y/\delta_\infty)^{1/n_{pl}}$ over
  $0.2\lesssim y/\delta\lesssim0.6$ with $n_{pl}=5$–8, and the van Driest
  velocity over $0.2\lesssim y/\delta\lesssim0.9$ with $n_{pl}=5$ (Eqs.
  4.6–4.7; page-local $n_{pl}$, $\delta_\infty$ the height where the mean
  velocity first reaches $U_\infty$).
- **Universality claimed for learned models.** Bae & Koumoutsakos (2022,
  Discussion) state, citing the literature, that all flows with inner–outer
  scale separation exhibit a log law, and take this as the reason a state
  space built on the local log-law slope and intercept can extend to
  roughness, stratification and compressibility (not shown).

## The law of the wall as a constraint

Vadrot et al. (2023b, §V) make preservation of the law of the wall the minimum
requirement of any learned wall model: a model must reproduce the log law in
channel flow at all Reynolds numbers, seen and unseen, before it is credited
with improvements elsewhere (see [machine-learning wall models](/methods/machine-learning-wall-model.md)).
Their a priori test of the ZHY21/ZYZY22 networks feeds a law of the wall built
by stitching the $Re_\tau=5200$ DNS wall layer to $u^+=\kappa^{-1}\ln y^++B$ at
$y^+=100$ (§IV.B). The mean-velocity departure from the log law is the
[log-layer mismatch](/definitions/log-layer-mismatch.md).
Bae & Koumoutsakos (2022, Methods, Eq. 3) build the states of their
log-law-based reinforcement-learning wall model from the instantaneous local
slope and intercept of the log law at the matching height, so that the agent
learns to raise or lower $\tau_w$ according to whether the local state lies
above or below $u^+=0.41^{-1}\ln y^++5.2$ (Fig. 2); see
[machine-learning wall models](/methods/machine-learning-wall-model.md).

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
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1; §3, Eq. (3).
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Eq. (3); Fig. 2; Discussion; Methods.
- [Knopp (2022)](/sources/knopp-2022.md) — §4, Eq. (26); §5–6, Eq. (35).
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1, Eqs. (4.5)–(4.7), Figs. 11–12.
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.3, Eq. (8).
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4, Fig. 8.
