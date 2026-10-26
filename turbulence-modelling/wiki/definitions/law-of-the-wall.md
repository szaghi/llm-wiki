---
type: Definition
title: "Law of the wall"
description: "The inner-layer mean-velocity profile of wall-bounded turbulence — viscous sublayer, buffer layer and logarithmic layer in wall units — with the constants, composite fits and damping functions the sources use, its compressible and outer-layer (defect-law) extensions, and its role as the target every wall model must reproduce."
status: established
aliases: [logarithmic law, log law, law-of-the-wall profile, inner-layer profile]
tags: [boundary-layer, wall-model, wmles, rans]
timestamp: 2026-10-26T10:26:00Z
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
| [Kim et al. (2022)](/sources/kim-2022.md), Fig. 12 | 0.41 | 5.2 | | reference line for the mean velocity of LES with learned SGS models at $Re_\tau=180$–720 |
| [Dang et al. (2022)](/sources/dang-2022.md), Fig. 17 legend | $1/2.44$ | 5.1 | | reference for van Driest-transformed DNS profiles upstream of a Mach 2.9 ramp |
| [Cai et al. (2022)](/sources/cai-2022.md), Eq. (26) | not printed | $\kappa^{-1}\ln E$, $E=11.27$ | blend constants 10.71 and 1.526 | log law written $u^+=\kappa^{-1}\ln(Ey^+)$; explicit equilibrium wall model in a lattice Boltzmann solver |
| [Blind et al. (2023)](/sources/blind-2023.md), §3.3 | not printed | not printed | Spalding's law | algebraic wall model in [FLEXI](/software/flexi.md) |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), Figs. 4–5 | not printed | not printed | Reichardt's law | reference profile for IDDES of channel flow |
| [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §3.2, Eq. (3.1) | 0.41 | 5.2 | quadratic branch below $y^+=23$ | equilibrium baseline of the [building-block-flow wall model](/methods/building-block-flow-wall-model.md), sampled at the second grid point |
| [Lewis et al. (2023)](/sources/lewis-2023.md), §3.2.2 | not printed | not printed | linear for $y^+<11$, logarithmic above | wall law of fan-stage WMLES in AVBP |
| [Kang et al. (2023)](/sources/kang-2023.md), figures | 0.41 | 5.2 | | reference line for LES of channel flow at $Re_\tau=180$ and 395 with learned SGS models |
| [Wang et al. (2023b)](/sources/wang-2023-b.md), Eq. (10) | 0.40 | 5.5 | "for the low Reynolds number turbulent channel flow" | reference for van Driest-transformed compressible channel DNS |
| [Zhao et al. (2023a)](/sources/zhao-2023.md), Eqs. (25)–(26) | 0.40 | 5.5 | "selected for the low-Reynolds-number turbulent channel flow" | sets the viscosity of a channel at a target $Re_\tau$ |
| [Vadrot et al. (2023a)](/sources/vadrot-2023.md), §II.B.1, Eq. (1); §II.B.3 | $\approx0.4$ (0.4 in the states and figures) | $\approx5$ | | algebraic wall model and reference log law of reinforcement-learning wall models in LESGO |
| [Constant et al. (2024)](/sources/constant-2024.md), §3.2, Eq. (8) | 0.41 | not printed | Musker's law (form not printed); van Driest damping $1-e^{-y^+/19}$ in the target-point eddy viscosity | wall function at immersed-boundary target points in RANS |
| [Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §2.2, Eqs. (12)–(15) | $\approx0.41$ | $\kappa^{-1}\ln E$, $E\approx7.9$ | blend constants $s=86.58$, $p=0.7894$ | explicit equilibrium wall model in a lattice Boltzmann solver |
| [Chen et al. (2024)](/sources/chen-2024.md), §2.3, Eqs. (2.7), (2.10) | 0.40 | — | $A^+=26$ divided by the square root of the local total shear stress in wall units; Johnson–King reference damping with 17 | mixing length of the algebraic [Baldwin–Lomax model](/methods/baldwin-lomax-model.md) (a RANS closure, not an LES wall model) |

Zhao et al. (2023a) attribute $\kappa=0.40$, $B=5.5$ to the channel DNS of
Kim et al. (1987), as they cite it; Wang et al. (2023b) give the same values
with the same wording. Zhao et al. (2023a, §5.2, Eqs. 25–26) use the law in the reverse
direction: with the centreline velocity $U_c=1$ and the target centreline
value $y_c^+=Re_\tau=180$, they set $U_c^+=2.5\ln y_c^++5.5$,
$u_\tau=U_c/U_c^+$ and the viscosity $\mu=\rho u_\tau\delta/Re_\tau$ ($\delta$ the
channel half-height, the source's $H$; $U_c$, $U_c^+$, $y_c^+$ page-local); the realized $Re_\tau$ then follows
from the simulation. Dang et al.'s slope $1/2.44$ is $\kappa\approx0.410$, and Cai et al.'s $E=11.27$
corresponds to $B=\kappa^{-1}\ln E\approx2.42/\kappa$, about 5.9 for
$\kappa=0.41$ *(compiler check, not in the sources)*.

Griffin et al. (2023, §3) test Reynolds-number-dependent constants fitted to
the incompressible channel DNS of Lee & Moser (as recalled by them): at
$Re_\tau=\{182,543,1000,1990,5190\}$, $\kappa=\{0.400,0.408,0.400,0.391,0.391\}$
and $A^+=\{18.2,17.4,17.0,16.5,16.5\}$. The fitted values improve their
compressible wall model only modestly at $Re_\tau^*=190$ and not at all at
$Re_\tau^*=590$, so they keep $\kappa=0.41$, $A^+=17$. Gillyns et al. (2022,
§3) likewise note that more recent values after Lee & Moser are
$\kappa\simeq0.383$, $B\simeq4.25$, but keep 0.38 and 4.1; the effect of the
choice on $u_\tau$ is not assessed.

Vadrot et al. (2023a, §II.B.3) note that empirical values of $\kappa$ range
over 0.36–0.44 (as they cite it), which matters for their learned wall model
because its first state is built from the chosen $\kappa=0.4$ (see
[machine-learning wall models](/methods/machine-learning-wall-model.md)).
Mozaffari et al. (2024) write the log law as $u^+=\kappa^{-1}\ln(Ey^+)$, as
Cai et al. (2022) do, but with $E\approx7.9$ against 11.27 (see
Contradictions); with $\kappa=0.41$ for both (Cai et al. print no value of
$\kappa$) these correspond to $B\approx5.0$ and $B\approx5.9$
*(compiler check, not in the sources)*.

How much the constants matter is quantified by Lozano-Durán et al. (2022,
§IV.C, Eq. 12): a 10 % error in $\kappa$ or in $B$ produces about 6 % or 3 %
error in $u_\tau$, less than a 10 % error in the LES velocity at the matching
point; their fuselage WMLES errors saturate at about 2 %, which they attribute
to a 3 % deviation in $\kappa$ (§V.C). The constants therefore set an accuracy
floor of wall-modelled LES that grid refinement does not remove (details on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page). Vadrot et
al. (2023a, §III.B) quote a comparable sensitivity, after Yang et al. (2019)
as they cite it: a 2.5 % uncertainty in $\kappa$ gives about a 5 % error in
the predicted wall stress, that is about one to two wall units of
[log-layer mismatch](/definitions/log-layer-mismatch.md).

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
- **Blended profile with an explicit inverse** (Cai et al. 2022, §II.C.1,
  Eqs. 24–26, after the authors' earlier work as they cite it). The forward
  profile blends the two asymptotes with hyperbolic tangents,

  $$u^+=\left[1-\tanh\frac{y^+}{10.71}\right]^{1.526}y^++\left[\tanh\frac{y^+}{10.71}\right]^{1.526}\frac1\kappa\ln(Ey^+),\qquad E=11.27,$$

  and a separately fitted inverse gives $y^+$ directly from the local Reynolds
  number $Re_y=U y/\nu$ ($U$ the wall-tangential velocity at distance $y$;
  page-local),

  $$y^+=\left[1-\tanh\frac{Re_y}{180.8}\right]^{0.789}Re_y^{1/2}+\left[\tanh\frac{Re_y}{180.8}\right]^{0.789}\frac{e^{W(\kappa ERe_y)}}{E},$$

  with $W$ the Lambert function, $W(x)=\ln\big(x/W(x)\big)$, "expanded
  explicitly into series" (series not printed), so that
  $u_\tau=y^+\nu/y$ needs no Newton iteration. Each branch of the inverse is
  the exact inverse of the matching branch of the forward profile — the
  viscous branch from $Re_y=(y^+)^2$, the log branch from
  $\kappa ERe_y=Ey^+\ln(Ey^+)$, i.e. $\ln(Ey^+)=W(\kappa ERe_y)$ — while the
  two blending functions differ, so the pair is consistent only
  asymptotically; its buffer-layer accuracy is not shown in the source
  *(compiler check, not in the sources)*. See the
  [equilibrium wall model](/methods/equilibrium-wall-model.md).
- **The same explicit inverse with other constants** (Mozaffari et al.
  2024, §2.2, Eqs. 9–15, after Cai & Sagaut as they cite it): the viscous
  branch $y^+=\sqrt{Re_y}$, the log branch $y^+=E^{-1}e^{W(\kappa ERe_y)}$ and
  the unified inverse

  $$y^+(Re_y)=\left[1-\tanh\frac{Re_y}{s}\right]^pRe_y^{1/2}+\left[\tanh\frac{Re_y}{s}\right]^p\frac{e^{W(\kappa ERe_y)}}{E},\qquad u^+=\frac{Re_y}{y^+},$$

  with $s=86.58$, $p=0.7894$, $\kappa\approx0.41$, $E\approx7.9$ ($s$, $p$
  page-local); the exponent $p$ applies to the bracketed blending functions,
  as in the form of Cai et al. (2022) above (manuscript p. 5, Eq. 15, checked
  visually). No pressure-gradient term. See Contradictions for the
  comparison with Cai et al. (2022).
- **Musker's law** (Constant et al. 2024, §3.2, Eq. 6, after Musker as
  cited): an equilibrium profile fitting viscous, buffer and log layers,
  $u_A=u_\tau f(y_A^+)$ at an immersed-boundary target point $A$, with
  $u_\tau$ from Newton–Raphson at the image point and assumed constant along
  the wall normal; the formula is not printed. Their Fig. 7 compares it with
  Spalding's law and a body-fitted flat-plate RANS profile. The eddy
  viscosity at the target points is $\nu_t=\kappa u_\tau y\,[1-e^{-y^+/19}]$
  with $\kappa=0.41$ (Eq. 8), stated "valid in the log layer and down to the
  wall", and inverted for the Spalart–Allmaras variable $\tilde\nu$; the
  damping enters to the first power and with the constant 19, unlike the
  squared $A^+=17$ form of Griffin et al. (2023).
- **Linear/log switch** (Lewis et al. 2023, §3.2.2, after Schmitt et
  al. as cited): a linear law $u^+=y^+$ for $y^+<11$ and a logarithmic law
  otherwise; the constants are not printed.
- **Spalding's law** is the algebraic wall model of Blind et al. (2023,
  §3.3), solved by Newton's method in every Runge–Kutta stage; the formula
  and its constants are not printed.
- **Mixing length with van Driest damping**, the differential form behind
  the fit of Fowler et al.: the eddy viscosity is $\nu_t=\kappa y\,u_\tau(1-e^{-y^+/A^+})^2$,
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
  [Chen et al. (2024)](/sources/chen-2024.md) (§3.1, Eqs. 3.1–3.2) derive
  the same equivalence for the inner layer of the algebraic
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md): a mixing length
  $\kappa y[1-e^{-y^*/A^+}]$ ($\kappa=0.40$) with semi-local damping is the
  mixing-length relation written for the Trettel–Larsson velocity. Their
  DNS diagnostic of the semi-local eddy viscosity, compared with the
  Johnson–King inner scaling $\kappa y^*[1-e^{-y^*/17}]^2$, collapses up to
  the buffer layer but falls below it in the log region of diabatic
  boundary layers, and follows it more closely with the Griffin–Fu–Moin
  transformation (§3.1, Fig. 3).
- **Outer (defect) layer.** Chen et al. (2024, §3.2, Eqs. 3.9–3.12) use
  Clauser's defect law $u_e^+-u^+=g(y/\Delta_{RC})$ with the Rotta–Clauser
  thickness $\Delta_{RC}=u_e^+\delta^*$ (page-local $u_e^+$, $g$,
  $\Delta_{RC}$); for the incompressible zero-pressure-gradient layer they
  take, from Monkewitz et al. (2007) as they cite it, the outer maximum 5.55
  of $y\,\partial u^+/\partial y$ at $y/\Delta_{RC}=0.155$. For compressible
  layers the van Driest-transformed defect collapses better, with outer
  velocity scale $u_\tau/\sqrt{\langle\rho\rangle/\rho_w}$, after Smits &
  Dussauge as they cite it (Eq. 3.12, Fig. 5); this is the basis of their
  outer-layer correction (see
  [compressible velocity transformation](/definitions/compressible-velocity-transformation.md)).
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
- **Low Reynolds number.** [Kim et al. (2022)](/sources/kim-2022.md) (§III D,
  Fig. 12) recall, citing the channel DNS of Moser, Kim & Mansour, that the
  DNS mean velocity at $Re_\tau=180$ deviates slightly from the log law in the
  logarithmic region, and use this non-universality to explain why an SGS
  model trained by reinforcement learning at $Re_\tau=180$ under-estimates the
  buffer-layer slope at $Re_\tau=360$, while one trained at 360 over-estimates
  the mean velocity at 180 (see
  [reinforcement-learning closures](/methods/reinforcement-learning-closure.md)):
  "the non-universal characteristic of $Re_\tau=180$ affects the
  generalization performance of the DRL model".
- **Separated regions.** Cai et al. (2022, §II.C.2) state that equilibrium
  and non-equilibrium wall models assume quasi-parallel near-wall flow and
  that their use under separation is "physically not appropriate", but that
  the small wall stress there keeps the model in the low-$y^+$ range "where
  linear profile applies", and recall three studies finding the flow not very
  sensitive to the wall model in the recirculation zone.
- **Universality claimed for learned models.** Bae & Koumoutsakos (2022,
  Discussion) state, citing the literature, that all flows with inner–outer
  scale separation exhibit a log law, and take this as the reason a state
  space built on the local log-law slope and intercept can extend to
  roughness, stratification and compressibility (not shown).

- **RANS on DG grids.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md)
  (§5.1, Fig. 5-2) report that the velocity profile of their interior-penalty
  DG solver with the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
  on a turbulent flat plate ($M=0.2$, $Re_L=1.12\times10^7$, first-cell
  $y^+=1$) agrees with a reference profile they cite in the log layer.
- **Compressible channel.** Wang et al. (2023b, §4.2, Eqs. 10–11, Fig. 11)
  compare the van Driest-transformed mean velocity of their gas-kinetic DNS of
  a channel at bulk $M_b=0.8$ and bulk Reynolds number 3000 (isothermal walls)
  with the incompressible log law; see the
  [compressible velocity transformation](/definitions/compressible-velocity-transformation.md).

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
Vadrot et al. (2023a, §V) state the same position for their own
reinforcement-learning model: recovering the log law is "an essential
step", since "if a model cannot capture the log law, it would be hard for it
to capture other flow phenomena"; their model, trained at $Re_\tau=10^4$,
recovers $u^+=0.4^{-1}\ln y^++5$ in half-channel WMLES up to
$Re_\tau=10^{10}$ whenever the matching height lies in the log layer, while
at $Re_\tau=180$ its profile lies above the DNS (§III.A, Fig. 6).

The friction velocity is also the first quantity a near-wall LES must get
right without a wall model: [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§7.2–7.4) report $u_\tau$ errors in pipe flow at $Re_\tau=1000$ of $+15.3$ %
(no model), $+9.6$ % (Smagorinsky with van Driest damping) and $-1.8$ %
(implicit [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md))
on a uniform mesh with $\Delta x^+=\Delta y^+\approx9$.

## Qualifications

- The constants are source choices, not measurements of this bundle; the
  table records them and no value is preferred here.
- Mozaffari et al. (2024) print for Cai & Sagaut (2021), their ref. [8], a
  DOI identical to the one they print for Wilhelm et al. (2021), ref. [63];
  one of the two DOIs is a slip.
- **Printed viscosity of Zhao et al. (2023a).** For $Re_\tau=180$ they print
  $\mu=2.83\times10^{-4}$ (§5.2). With their Eqs. (25)–(26), $\rho=1$, $\delta=1$
  and $U_c=1$: $U_c^+=2.5\ln180+5.5\approx18.48$, $u_\tau\approx0.0541$ and
  $\mu\approx3.01\times10^{-4}$ *(compiler check, not in the sources)*; the
  printed value is not reproduced.
- Griffin et al. (2023) print Eq. (1.2) as
  $\mu_t=\kappa y\langle\rho\rangle\sqrt{\tau_w/\langle\rho\rangle}\,(1-\exp(y^+/A^+))^2$,
  without the minus sign in the exponent; their own text describes a damping
  function that tends to the undamped mixing length away from the wall, which
  holds only for $(1-e^{-y^+/A^+})^2$. In §3 they print "$\kappa$ … 4.1" for
  the 0.41 stated in §1 and at the end of §3.

## Contradictions

- **Constants of the explicit inverse wall law of Cai & Sagaut (2021).**
  [Cai et al. (2022)](/sources/cai-2022.md) (§II.C.1, Eqs. 24–26) present
  the tanh-blended explicit inverse $y^+(Re_y)$ as the model "proposed in
  Refs. 23 and 29" (ref. 29 is Cai & Sagaut 2021) and print the blend scale
  180.8, the exponent 0.789 and, in the companion forward profile, $E=11.27$.
  [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) (§2.2, Eqs. 12–15,
  lines 160–164) give the same functional form "in the form [8]" (ref. [8]
  is Cai & Sagaut 2021) with $s=86.58$, $p=0.7894$ and $E\approx7.9$,
  $\kappa\approx0.41$. Cai is a co-author of both and both run in ProLB;
  neither paper says that its constants recalibrate the cited model, so the
  two sources disagree on the constants of the same attributed law (the
  blend scales differ by a factor of about two and the log branches through
  $E$). Cai & Sagaut (2021) is not ingested. *Open.*

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
- [Kim et al. (2022)](/sources/kim-2022.md) — §III D, Fig. 12.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.C.1, Eqs. (24)–(26); §II.C.2.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.3.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Figs. 4–5.
- [Dang et al. (2022)](/sources/dang-2022.md) — §5.1, Fig. 17.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.2, Eq. (3.1).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.2 (HAL accepted manuscript).
- [Kang et al. (2023)](/sources/kang-2023.md) — channel-flow mean-velocity figures (§3).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2, Eqs. (10)–(11), Fig. 11 (arXiv v1).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.2, Eqs. (25)–(26) (arXiv v1).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.1, Fig. 5-2.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.B.1, Eq. (1); §II.B.3; §III.A–III.B, Fig. 6; §V (arXiv v3).
- [Constant et al. (2024)](/sources/constant-2024.md) — §3.2, Eqs. (6)–(8), Fig. 7 (HAL author manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.2, Eqs. (9)–(15); ref. [8] (HAL accepted manuscript).
- [Chen et al. (2024)](/sources/chen-2024.md) — §2.3, Eqs. (2.7)–(2.10); §3.1, Eqs. (3.1)–(3.4), Fig. 3; §3.2, Eqs. (3.9)–(3.12), Fig. 5.
