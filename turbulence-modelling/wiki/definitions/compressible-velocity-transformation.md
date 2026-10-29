---
type: Definition
title: "Compressible velocity transformations"
description: "Maps that turn the mean velocity of a variable-property compressible wall layer into the incompressible law of the wall — van Driest, Trettel–Larsson, data-driven and total-stress-based — with semi-local scaling, temperature–velocity relations, their assessment on DNS of channels and supersonic to hypersonic boundary layers, and their use as validation yardsticks."
status: established
aliases: [velocity transformation, compressible law of the wall, total-stress-based transformation, van Driest transformation, Trettel–Larsson transformation, semi-local scaling, generalized Reynolds analogy]
tags: [compressible, boundary-layer, wall-model, hypersonic]
timestamp: 2026-10-29T07:38:00Z
---

# Compressible velocity transformations

A compressible velocity transformation maps the Favre-averaged mean velocity
$U(y)$ of a compressible wall-bounded flow with variable density and viscosity
onto an equivalent incompressible profile that obeys the incompressible
[law of the wall](/definitions/law-of-the-wall.md). Once such a map is known,
the incompressible inner-layer physics — and any incompressible wall model —
can be carried to compressible flows with heat transfer. [Griffin et al. (2023)](/sources/griffin-2023.md) invert one such
map to build the
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md);
[Cogo et al. (2022)](/sources/cogo-2022.md) and [Huang et al. (2022)](/sources/huang-2022.md)
write the forward transformations out and assess them on their own DNS of
zero-pressure-gradient boundary layers at Mach 2 to 10.9 (see
[direct numerical simulation](/definitions/direct-numerical-simulation.md)). Page-local notation:
$U$ and $T$ the Favre-averaged velocity and temperature, $\rho^+=\langle\rho\rangle/\rho_w$
and $\mu^+=\langle\mu\rangle/\mu_w$, subscripts $w$, $e$, $m$ for wall,
boundary-layer edge and matching height.

## Semi-local scaling

Semi-local units replace the wall density and viscosity by their local mean
values (Griffin et al. 2023, §3, cite Coleman, Kim & Moser 1995 and Huang,
Coleman & Bradshaw 1995): $u_\tau^*=\sqrt{\tau_w/\langle\rho\rangle(y)}$ and
$y^*=y\,u_\tau^*\langle\rho\rangle/\langle\mu\rangle$, so that
$y^*=y^+\sqrt{\rho^+}/\mu^+$. The semi-local friction Reynolds number
$Re_\tau^*=\langle\rho\rangle_e u_\tau^*\delta/\langle\mu\rangle_e$ (with
$u_\tau^*$ evaluated at the edge or centreline) is invariant under the
transformation, so the incompressible constants are taken at $Re_\tau^*$ in
place of $Re_\tau$ (§2.1).

Semi-local scaling also organizes statistics other than the mean velocity.
In six DNS of zero-pressure-gradient boundary layers at $M_\infty=0.5$, 2
and 8 on quasi-adiabatic and cooled walls, [Zhang et al. (2022)](/sources/zhang-2022-b.md)
find that it collapses the peak positions of the Reynolds stresses (§3,
Fig. 4), the peaks of the pressure-fluctuation intensity at about $y^*=30$
(§5, Fig. 13) and the near-wall streak spacing at about 100 in semi-local
units for all cases (§4).

In RANS, [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) (§1.1,
§2.2, Eqs. 1, 7–8) use the semi-local friction Reynolds number in the form
$Re_\tau^*=Re_\tau\sqrt{\rho^+}/\mu^+$ (after Huang et al. and Patel et al.,
as cited) to characterize variable-property channels. They replace $y^+$
by $y^*=y^+\sqrt{\rho^+}/\mu^+$ in the damping functions of the
Myong–Kasagi [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md),
following Otero Rodriguez et al. (as cited). They also state that the
velocity transformation of Patel et al. "is equivalent to the one
proposed by Trettel and Larsson" (§1.1). In their learned correction
(see [field inversion and machine learning](/methods/field-inversion-machine-learning.md))
$y^*$ ranks above $\rho^+$ and $\mu^+$ as an input feature, which they
read as the property variation being already contained in $y^*$ (§5, §6).

**The local friction Reynolds number as a profile.** [Wang & Xu (2024)](/sources/wang-2024-h.md)
(§4.2, Eq. 4.2) use the same quantity of Patel, Boersma & Pecnik (2016, as
cited) as a function of wall distance,
$Re_\tau^*(y)=\sqrt{\langle\rho\rangle/\rho_w}\,(\mu_w/\langle\mu\rangle)\,Re_\tau$,
whose prefactor measures how far the local density and viscosity depart from
their wall values. In the DNS of a Mach 2.33 boundary layer with a sonic
cold hydrogen film ($Re_\tau\approx1000$, adiabatic wall), with and without
combustion, the downstream Reynolds stresses settle below the canonical
adiabatic profiles of Pirozzoli & Bernardini (2011, as cited) at the same
$Re_\tau$, mainly in the outer region; the authors attribute the deficit to a
prefactor below that of a canonical profile, because the mean temperature is
non-monotonic across the cold layer. Upstream, hydrogen depletion raises the
density and $Re_\tau^*$; downstream, heat release raises the wall temperature
and lowers $Re_\tau^*$ (§4.2, Figs. 10–11). Their reading is that $Re_\tau$
and the thermal wall condition label a canonical profile only if the density
and viscosity distributions are canonical. The canonical comparison profile
is built from the Pirozzoli & Bernardini density with $T\propto1/\rho$ and
$\mu\propto T^{2/3}$ (§4.2).

**Semi-local scaling of the turbulent-kinetic-energy budget.** On Mach 6
boundary layers at $T_w/T_r=0.50$, 0.75 and 1.0 ($Re_\tau=675$, 411, 293),
[Zhang et al. (2024b)](/sources/zhang-2024-b.md) (§3.1, Eqs. 3.7–3.14,
Fig. 7) scale the Favre budget terms by $\langle\rho\rangle u_\tau^{*3}$ over
the semi-local viscous length and plot them against $y^*$; the budgets agree
with the Mach 5 DNS of Duan et al. (2010, case M5T5, as cited) and sum to
balance, which they read as confirming semi-local scaling in hypersonic
boundary layers.

**Semi-local scaling with the subgrid viscosity.** In wall-modelled LES the
near-wall region carries a large SGS eddy viscosity. [Maeyama & Kawai (2023)](/sources/maeyama-2023.md)
(§5.4, Eqs. 5.3–5.5) therefore add it to the molecular viscosity in the
semi-local viscous length,

$$\delta^{*,\mathrm{sgs}}_\nu=\frac{\langle\nu\rangle+\nu_t}{u_\tau^*}=\frac{\langle\mu\rangle+\mu_t}{\langle\rho\rangle u_\tau^*},$$

with $\nu_t$ the SGS eddy viscosity at height $y$ and
$\delta^{*,\mathrm{sgs}}_\nu$ registry §11, against $\delta_\nu=\nu_w/u_\tau$
and the semi-local $\langle\nu\rangle/u_\tau^*$. They measure the spanwise
length of the near-wall streak-like structures of a Mach 2.28 WMLES from
the spanwise correlation of $u$ near $y^+\approx15$, or at the first grid
point. In wall units or in semi-local units this length grows almost
linearly with $Re_\tau$ from 700 to 14 000. Scaled by
$\delta^{*,\mathrm{sgs}}_\nu$ it collapses to $O(100)$, the order of the
DNS streak spacing in wall units, on every grid, scheme and SGS model they
tried (App. C–D, Figs. 17b, 28, 32). They conclude that "the diffusion
introduced by the SGS eddy viscosity dominantly determines the spanwise
length scale" of these numerical structures (see
[wall-modelled LES](/methods/wall-modelled-les.md)). The exact definition of
the length taken from the correlation is not printed.

## General form

Cogo et al. (2022, §4, Eq. 4.1, Table 3), citing Modesti & Pirozzoli (2016),
write every transformation as a stretching of the wall
distance and of the velocity,

$$y_I^+=\int_0^{y^+}f_I\,dy^+,\qquad U_I^+=\int_0^{U^+}g_I\,dU^+ ,$$

with (page-local $f_I$, $g_I$; the source writes $R$, $M$ for $\rho^+$,
$\mu^+$):

| Transformation | $f_I$ | $g_I$ |
|---|---|---|
| van Driest | $1$ | $\sqrt{\rho^+}$ |
| Trettel–Larsson | $\dfrac{d}{dy^+}\left(\dfrac{y^+\sqrt{\rho^+}}{\mu^+}\right)$ | $\mu^+\dfrac{d}{dy^+}\left(\dfrac{y^+\sqrt{\rho^+}}{\mu^+}\right)$ |
| Volpiani et al. | $\sqrt{\rho^+}/(\mu^+)^{3/2}$ | $\sqrt{\rho^+}/\sqrt{\mu^+}$ |

The Trettel–Larsson wall distance is thus the semi-local $y^*$. Huang et al.
(2022, Eqs. 4.1–4.3) print the same three forms with $y$ wall-normal
translated from their $z$.

## The transformations

- **Van Driest (1951).** The classical transformation; it is implied by the
  classical mixing length with van Driest damping written in wall units
  $y^+$ (Griffin et al. 2023, §3, citing Yang & Lv 2018).
- **Trettel–Larsson (2016).** Implied by the same damping written in
  semi-local units $y^*$ (Griffin et al., §3, citing Yang & Lv 2018).
  [Chen et al. (2024)](/sources/chen-2024.md) (§3.1, Eqs. 3.1–3.2) derive
  the same equivalence for the inner eddy viscosity of the semi-local
  [Baldwin–Lomax model](/methods/baldwin-lomax-model.md): written with the
  density-weighted Reynolds shear stress (Morkovin scaling), its mixing-length
  relation is the incompressible one in the variables $y^*$ and $U^+_{TL}$
  (the Trettel–Larsson velocity, page-local). Their DNS diagnostic of the
  semi-local eddy viscosity built on $U^+_{TL}$ falls below the incompressible
  curve in the log region, especially in diabatic boundary layers (§3.1,
  Fig. 3a), which motivates their switch to the total-stress-based
  transformation below.
- **Data-driven** transformation of Volpiani et al. (2020), used by Kumar &
  Larsson (2022) in the same inverse procedure (Griffin et al., §2.3, cite both).
- **Total-stress-based** transformation of Griffin, Fu & Moin (2021), which
  maps the compressible mean strain rate to the incompressible
  non-dimensional strain rate $S_t^+$ at the same $Re_\tau^*$ (Eq. 2.1):

  $$S_t^+=\frac{S_{eq}^+}{1+S_{eq}^+-S_{TL}^+},\qquad S_{eq}^+=\frac1{\mu^+}\frac{dU^+}{dy^*},\qquad S_{TL}^+=\mu^+\frac{dU^+}{dy^+},$$

  with $U^+=U/u_\tau$ (page-local $S_t^+$, $S_{eq}^+$, $S_{TL}^+$). The
  viscous-region scaling follows Trettel & Larsson (2016) and Patel, Boersma &
  Pecnik (2016); the log region follows a modified version of the
  turbulence-equilibrium argument of Zhang et al. (2012). $S_{TL}^+$ equals the
  viscous stress and reduces to the incompressible strain rate when
  $\mu^+=1$. The transformation assumes a constant-stress layer in the buffer
  region, which Griffin et al. (2021) found harmless in equilibrium flows and
  Bai, Griffin & Fu (2022) under moderate pressure gradients (as Griffin et
  al., §2.1, cite them).

  **Total-stress form.** Cogo et al. (2022, Eq. 4.2) write the same
  transformation as a total-stress balance,
  $\tau/\tau_w=S_t^+\left(\tau_v^+/S_{TL}^++\tau_R^+/S_{eq}^+\right)$, with
  $\tau_v^+$, $\tau_R^+$ the viscous and Reynolds shear stresses scaled by
  $\tau_w$, and define $S_{TL}^+$ and $S_{eq}^+$ as $y^*$-derivatives of the
  Trettel–Larsson- and equilibrium-transformed velocities rather than through
  $\mu^+$ and $U^+$ as above. With $\tau/\tau_w=1$ and $\tau_v^+=S_{TL}^+$ their
  form reduces algebraically to Eq. (2.1), and the Trettel–Larsson $y^*$-slope
  $g_I/f_I\cdot dU^+/dy^+=\mu^+dU^+/dy^+$ equals the $S_{TL}^+$ above
  *(compiler check, not in the sources)*. Cogo et al. report that the
  constant-stress version ($\tau/\tau_w\approx1$) deviates by no more than
  0.3 % from the full one on their data (§4). Huang et al. (2022, Eq. 4.4)
  print the definitions above.

- **Intrinsic-compressibility correction (HLPP).** Chen et al. (2024,
  App. B, Eq. B1) also test the transformation of Hasan et al. (2023b, as
  cited),

  $$U^+_{HLPP}=\int_0^{U^+}\frac{1+\kappa y^*D^i}{1+\kappa y^*D^c}\,\mu^+\frac{dy^*}{dy^+}\,dU^+,\qquad D^c=\left[1-e^{-y^*/(17+19.3M_\tau)}\right]^2,$$

  with $D^i$ the same damping with 17 alone and $M_\tau$ the friction Mach
  number (page-local $D^i$, $D^c$, $M_\tau$); its damping depends on Mach
  number, which Chen et al. (§1, §3.1) present as questioning Morkovin's
  hypothesis (see [Morkovin hypothesis](/definitions/morkovin-hypothesis.md)).

## Inversion

Because (2.1) is algebraic, it can be solved for the compressible velocity
gradient given $S_t^+$ and the property profiles (Eq. 2.2):

$$\frac{dU^+}{dy^*}=\left[\frac1{\mu^+S_t^+}-\frac1{\mu^+}+\sqrt{\rho^+}\left(1+\frac{y^+}{2\rho^+}\frac{d\rho^+}{dy^+}-\frac{y^+}{\mu^+}\frac{d\mu^+}{dy^+}\right)\right]^{-1}.$$

Substituting $S_{eq}^+$ and $S_{TL}^+$ in (2.1), with
$dy^*/dy^+=(\sqrt{\rho^+}/\mu^+)\left(1+\frac{y^+}{2\rho^+}\frac{d\rho^+}{dy^+}-\frac{y^+}{\mu^+}\frac{d\mu^+}{dy^+}\right)$
from $y^*=y^+\sqrt{\rho^+}/\mu^+$, and solving for $dU^+/dy^*$ reproduces (2.2)
exactly *(compiler check, not in the sources)*.

## Temperature: the generalized Reynolds analogy

A velocity transformation needs the density and viscosity profiles, hence the
temperature. Griffin et al. (2023, §2.2) cite the Walz (modified
Crocco–Busemann) relation with recovery factor $r=Pr^{1/3}$, accurate for
adiabatic walls but degraded by heat transfer, and its recasting by Zhang et
al. (2014) as the generalized Reynolds analogy (GRA), with Reynolds-analogy
factor $s_{\mathrm{RA}}=1.14$ (Eq. 2.3; page-local $r$; $s_{\mathrm{RA}}$ registry §11):

$$T=T_w+s_{\mathrm{RA}}\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_e}\right)+\left(\frac{U}{U_e}\right)^2(T_e-T_w),\qquad T_r=T_e+\frac{rU_e^2}{2c_p}.$$

It is equivalently a quadratic $T=b_0+b_1U+b_2U^2/2$ (Eq. 2.4) with $b_0=T_w$,
$b_1$ the wall slope from the Reynolds analogy and $b_2$ fixed by the edge
temperature. Griffin et al. fix $b_2$ instead by the matching-height
temperature $T_m$ at velocity $U_m$ (Eq. 2.5),

$$T=T_w+s_{\mathrm{RA}}\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_m}\right)+\left(\frac{U}{U_m}\right)^2(T_m-T_w),$$

which ties the wall heat flux to the wall stress, $q_w=s_{\mathrm{RA}}\tau_wc_p(T_w-T_r)/U_e$.
They judge the constant-$Pr_t$ energy equation of the classical model less
accurate than the GRA (citing Zhang et al. 2014).

Chen et al. (2024, §3.3, Eqs. 3.16–3.17) write the same quadratic with
the constant $C_{\mathrm{DM}}=0.8259$ of Duan & Martín (2011), recast as $s_{\mathrm{RA}}\,Pr$ with
$s_{\mathrm{RA}}=1.14$ after Zhang et al. (2014) as they cite them, and use the
matching-anchored form below $y^*_{mT}=100$ inside an algebraic RANS model;
they do not re-examine the relation against their DNS (details on the
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
page). Their motivation is the turbulent Prandtl number: in cold-wall
boundary layers the DNS value of $Pr_t$ is non-monotonic and becomes
negative or singular near the temperature peak, where the mean temperature
gradient and the turbulent heat flux change sign, and is below 0.5 between
that point and the wall in the three cold-wall cases shown, so a constant $Pr_t=0.9$ over-predicts the peak
temperature and no monotone wall-distance formula can follow it (§3.3,
Fig. 6; see the [Morkovin hypothesis](/definitions/morkovin-hypothesis.md)
page for $Pr_t$).

[Mo et al. (2023)](/sources/mo-2023.md) (§II B, Eqs. 11–13) print the GRA
of Zhang et al. (2013, as cited) in the form
$T/T_e=T_w/T_e+\big((T_r-T_w)/T_e\big)f(U/U_e)+\big((T_e-T_r)/T_e\big)(U/U_e)^2$
with $f(\xi)=(1-s_{\mathrm{RA}}\,Pr)\xi^2+s_{\mathrm{RA}}\,Pr\,\xi$, $s_{\mathrm{RA}}=1.16$ and $Pr=0.72$, giving
$f=0.165\xi^2+0.835\xi$. Expanded, this is the first relation above
term by term, with $s_{\mathrm{RA}}=1.16$ in place of Griffin et al.'s 1.14 *(compiler
check, not in the sources)*. Their DNS reproduces it at Mach 2.25 (isothermal
wall), 2.9 (adiabatic) and 7.25 (cold wall, $T_w=562$ K), and they
differentiate it to obtain a temperature-fluctuation law for a hypersonic
inflow (see [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)).

## Ranking by the sources

Griffin et al. (2023, §3, Fig. 7) compare wall models that embed different
transformations, a priori on DNS of channels, pipes and diabatic boundary
layers:

- In channels, the Trettel–Larsson and total-stress-based transformations
  both outperform van Driest: the classical model (van Driest-consistent)
  fails, while the semi-local models of Yang & Lv (2018) and Chen et al. (2022)
  and the total-stress-based model all perform well.
- In cooled and heated boundary layers, the classical model is least
  accurate; the total-stress-based model improves the log slope of the velocity
  (substantially for the cooled wall at $M_e=11.46$, slightly for the heated
  wall at $M_e=4.327$), and the temperature only slightly.
- The total-stress-based transformation has a documented error at
  $Re_\tau^*\lesssim200$ (Griffin et al. 2023, §3, citing Griffin et al. 2021), which accounts
  for the residual mismatch of their low-$Re_\tau^*$ cases.

Three independent DNS studies of boundary layers extend the comparison:

- **Cogo et al. (2022, §4, Fig. 8)**: four zero-pressure-gradient boundary
  layers on a cold isothermal wall, $T_w/T_r=0.76$, at $M_\infty=2$ and 5.86,
  $Re_\tau\approx450$ and 2000. Van Driest and Trettel–Larsson leave a
  log-law intercept mismatch, largest for the hypersonic cases and for
  Trettel–Larsson; Volpiani et al. and the total-stress-based transformation
  give "an excellent collapse through the whole boundary layer" for all four
  cases and differ only in the wake, where the total-stress-based one
  collapses the two Mach 5.86 cases better; "the database cannot decide"
  between them.
- **Huang et al. (2022, §4.1, Figs. 10–11)**: boundary layers at Mach 2.5
  (adiabatic), 4.9 ($T_w/T_r=0.91$) and 10.9 ($T_w/T_r=0.20$) up to
  $Re_\tau\approx1200$, plus the earlier cases of Zhang et al. (2018) at Mach 2.5–13.6. Trettel–Larsson
  collapses the viscous and buffer layers of all cases but leaves a scatter of
  the log-law intercept between flow conditions, also at matched
  $Re_\tau^*$, whereas it collapses isothermal cold-wall channels almost
  perfectly (citing Trettel & Larsson 2016 and Yao & Hussain 2020);
  they suggest a stronger effect of cooling on the turbulent/viscous stress
  balance in external boundary layers. Volpiani et al. and the
  total-stress-based transformation collapse both viscous and log layers, the
  latter best across the inner layer, judged by the diagnostic
  $y\,dU_I^+/dy$; Huang et al. call the success of the data-driven
  transformation "not unexpected" since it was fitted on non-adiabatic
  boundary-layer data.
- **Zhang et al. (2022, §3, Fig. 3)**: six spatially developing
  zero-pressure-gradient boundary layers at $M_\infty=0.5$, 2 and 8, each
  quasi-adiabatic ($T_w/T_r=1$) and cooled ($T_w/T_r=0.25$ at Mach 0.5, 0.5
  at Mach 2 and 8), compared at $Re_\tau\approx650$ (DNS in
  [STREAmS](/software/streams.md)). Van Driest fails for the cooled cases;
  Trettel–Larsson collapses the viscous sublayer but is "less successful" in
  the log region; the quasi-equilibrium transformation of Griffin et al.
  (based on Zhang et al. 2012, as they cite it; the $S_{eq}^+$ scaling above)
  gives a common slope but different additive constants; the
  total-stress-based transformation agrees well with the wall law and with
  the log law $\kappa=0.41$, $B=5.2$ for adiabatic and cooled cases alike.
  The comparison holds $Re_\tau$ fixed, so the semi-local $Re_\tau^*$ ranges
  from 96 to 20 696 across the six cases (Table 3); the authors call the
  choice of similarity parameter "a matter of controversy" (§2).

Cogo et al., Huang et al. and Zhang et al. (2022) each report the
total-stress-based transformation collapsing their boundary layers; Huang
et al. and Zhang et al. report Trettel–Larsson less successful in the log
layer of their cooled boundary layers, and Huang et al. cite its near-perfect
collapse of cold-wall channels. Cogo et al. state that their database
"cannot decide" between the total-stress-based and Volpiani et al.'s
transformations, while Huang et al. find the former best across the inner
layer. Griffin et al. (§1) also cite
Iyer & Malik (2019), who found the classical (van Driest-consistent) scaling
more accurate for adiabatic walls, and Yang & Lv (2018) and Fu, Bose & Moin
(2022), who found semi-local damping better for cold walls.

A third DNS-based comparison, over twelve published zero-pressure-gradient
boundary layers at $M_\infty=2$–13.64 and $T_w/T_r=0.18$–1.9 (Chen et al.
2024, App. B, Fig. 16), gives mean absolute errors of 2.2 % for the
total-stress-based and 2.4 % for the HLPP transformation; the authors note
that their error measure differs from that of Hasan et al. Built into their
algebraic RANS model, the two give comparable a posteriori errors (velocity
0.7 % against 0.6 % in log-inner coordinates). They also cite reports
that the total-stress-based transformation can degrade for
supercritical or non-air-like flows (§1).

**Outer layer.** The transformations above are designed for the region at
and below the log layer (Chen et al. 2024, §3.1). For the outer layer Chen et
al. (§3.2, Eqs. 3.11–3.12, Figs. 4–5) use the van Driest transformation in
defect form, after Smits & Dussauge (2006) and Pirozzoli & Bernardini (2011)
as they cite them: the diagnostic $y\,dU^+_{VD}/dy=\sqrt{\rho^+}\,y\,dU^+/dy$
collapses the outer peaks of cold-wall layers better than the untransformed
one, which implies an outer velocity scale $u_\tau/\sqrt{\rho^+}$, and the
outer eddy viscosity normalized with a van Driest displacement thickness
varies as little across the cases as the classical normalization. The
authors call the van Driest outer scaling of diabatic layers "somewhat
insufficiently examined" and raise error cancellation in the integral
thickness as a possible reason for its success (§3.2).

## Transformations as a validation yardstick

Further sources use a transformation not to rank transformations but to
judge, initialize or close a simulation.

- **Hybrid RANS/LES of supersonic channels.** [Carlsson et al. (2023)](/sources/carlsson-2023.md)
  (§4.3, Eqs. 24–26) state, citing three earlier studies, that the van Driest
  transformation, $u^+_{\mathrm{vD}}=\int_0^{u^+}\sqrt{\langle\rho\rangle/\rho_w}\,du^+$
  with Reynolds stresses scaled by $\langle\rho\rangle/\rho_w$ (Eq. 25), "is
  inaccurate for non-adiabatic walls", and adopt the Trettel–Larsson
  transformation, whose wall distance $y_T^+=\langle\rho\rangle(\tau_w/\langle\rho\rangle)^{1/2}y/\langle\mu\rangle$
  is the semi-local $y^*$ above. In SST-IDDES of isothermal-wall channels at
  $M_b=1.5$, $Re_\tau=500$, 1015 and 5000, the transformed profiles of their
  low-dissipation schemes agree with the DNS of Modesti & Pirozzoli (as they
  cite it) at the two lower Reynolds numbers and collapse onto Reichardt's
  incompressible law; at $Re_\tau=5000$, where no DNS exists, agreement with
  that law is taken as the accuracy criterion. The more dissipative reference
  scheme over-predicts the transformed velocity in the LES region (Fig. 5;
  see [log-layer mismatch](/definitions/log-layer-mismatch.md) and the
  [low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)).
  Carlsson et al. do not compare the two transformations on their own data;
  the choice rests on the studies they cite.
- **LES against DNS of hypersonic boundary layers.** [Helm & Martín (2022)](/sources/helm-2022.md)
  (Sec. III B, Fig. 3, Tables I–II) compare van Driest-transformed profiles
  of their LES with DNS at $M_e=2.9$ ($T_w/T_r=1.1$), 7.2 (0.52) and 9.0
  (0.33): all three agree within 3 %. The Mach 3 LES shows a slightly lower
  log-law intercept than the DNS, which they attribute to a mild forcing of
  the DNS mean flow by its rescaling length, judging the LES "the more
  accurate solution"; the Mach 10 LES overshoots the logarithmic layer of the
  DNS because it under-predicts the skin friction, by less than 5 %. In the
  upstream boundary layer of their Mach 7.2, 33° ramp the van Driest profiles
  with and without the scale-similar part of the SGS model are identical
  (Sec. IV F, Fig. 31).
- **High-order DG implicit LES of a supersonic boundary layer.**
  [Gao et al. (2022)](/sources/gao-2022.md) (§5.2, Figs. 16–17) validate the
  undisturbed Mach 2 boundary layer upstream of their oblique
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  ($Re_{\theta_0}=1628$, adiabatic wall, [FLEXI](/software/flexi.md) at
  $N=6$, no SGS model; see [implicit LES](/definitions/implicit-les.md))
  against the DNS of Wenzel et al. (as cited) one $\delta_r$ downstream of
  their forcing zone ($\delta_r$ the reference boundary-layer thickness,
  registry §11): the van Driest-transformed mean velocity is "in good
  agreement", and so are the density-scaled Reynolds stresses (see
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md); the scaling
  formula is not printed). For the skin friction they apply the van Driest
  II transformation and compare the transformed $C_f$ against the transformed
  momentum-thickness Reynolds number with the incompressible correlation
  $C_{f,i}=0.024\,Re_{\theta,i}^{-0.25}$ (subscript $i$ the transformed
  value, page-local), "as Wenzel et al. and Pirozzoli and Bernardini did";
  the LES approaches both the DNS and the correlation quickly after the
  forcing zone. Gao et al. do not discuss the choice of van Driest over the
  alternatives above; their wall is adiabatic, the case for which Iyer &
  Malik, cited by Griffin et al. (§1; above), found the classical
  scaling the more accurate.
- **DNS code validation.** [Dang et al. (2022)](/sources/dang-2022.md) (§5.1,
  Fig. 17) validate the GPU code [OpenCFD-SCU](/software/opencfd-scu.md) on
  the Mach 2.9, 24° compression ramp with van Driest-transformed mean
  profiles against the DNS of Martín and co-workers, reporting "good
  agreement".
- **GPU DNS and floating-point precision.** [Wang et al. (2023b)](/sources/wang-2023-b.md)
  (§4.2, Eqs. 10–11, Fig. 11) apply the van Driest transformation,
  $u^+_{\mathrm{vD}}=\int_0^{u^+}\sqrt{\langle\rho\rangle/\rho_w}\,du^+$ (the source writes $\langle U\rangle^+_{VD}$ and $\langle\rho_w\rangle$),
  to their multi-GPU gas-kinetic DNS of a channel at bulk Mach number 0.8 and
  bulk Reynolds number 3000 with isothermal walls ($\mu\propto T^{0.7}$,
  $Pr=0.7$), and compare it with the incompressible log law with
  $\kappa=0.40$, $B=5.5$, stating that the transformed velocity is expected to
  satisfy it; single- and double-precision runs are plotted together, and the
  fine-grid results "agree well" with the compressible channel DNS of Fu et al.
  as they cite it (Fig. 13). The paper does not discuss the choice of the van
  Driest transformation over the alternatives above; see
  [high-order gas-kinetic schemes](/methods/high-order-gas-kinetic-scheme.md).
- **Implicit LES of a supersonic channel.** [Cao et al. (2024)](/sources/cao-2024.md)
  (§3.3, Fig. 8) apply the same van Driest transformation, which they
  state is "expected to satisfy the incompressible log law", to implicit LES
  with the curvilinear high-order gas-kinetic scheme of an isothermal-wall
  channel at bulk $M_b=1.5$ and bulk Reynolds number 3000 ($\mu\propto T^{0.7}$,
  $Pr=0.70$). On $128^3$ cells (first point at $\Delta y^+=0.50$,
  $\Delta x^+=21.18$, $\Delta z^+=7.06$) the transformed mean velocity is "in
  reasonable agreement" with the DNS of Coleman et al. and of Morinishi et
  al. (as they cite them), and a constrained LES on a coarser grid, as
  they list it, "also performs very well" (Fig. 8; Table 4). Their wall
  statistics, $Re_\tau=211$ against 222 and 218 in the two DNS and
  $B_q=-0.047$ against $-0.049$ and $-0.048$ (Table 5; $B_q$ the heat-flux
  parameter), are close; with the native BGK value $Pr=1$ the mean density
  and temperature profiles change "greatly" and $Re_\tau$ rises to 221, and
  the authors conclude that the Prandtl number must be corrected to the
  target value (§3.3, Table 5, Fig. 7). As in Wang et al. (2023b), the
  choice of the van Driest transformation is not discussed; the wall is
  isothermal with a non-zero heat flux ($B_q=-0.047$), the case for which
  Carlsson et al. (above), citing earlier studies, call van Driest
  inaccurate. See [implicit LES](/definitions/implicit-les.md).
- **DNS of a thermally perfect gas: the transformation as a scheme
  discriminator.** [Aiello et al. (2026)](/sources/aiello-2026.md) (§2.2,
  §4.1–4.2, Fig. 1, Table 3) run DNS of isothermal-wall channels of CO$_2$,
  modelled as a thermally perfect gas ($c_v(T)$ from NASA polynomials), at
  bulk Mach numbers based on the wall sound speed of 3, 4 and 5
  ($Re_\tau\approx470$, 630 and 800, $Re_\tau^*$ between 160 and 190 with
  centreline properties) in [STREAmS](/software/streams.md), and compare
  convective discretizations that differ in
  [entropy conservation](/properties/entropy-conservation.md) and in the
  pressure term, all [kinetic-energy preserving](/properties/kinetic-energy-preservation.md).
  With the Trettel–Larsson transformation every profile collapses on
  $U^+_{TL}=y^*$ in the viscous sublayer regardless of scheme and Mach
  number, and a narrow log region appears for $y^*\ge40$, fitted with
  $\kappa=0.41$ and $B=6.0$ on the entropy-conservative results; the authors
  attribute the large intercept to the low $Re_\tau^*$, consistent with
  low-Reynolds-number incompressible flow and earlier supersonic channel DNS
  of calorically perfect gas (§4.1). As the Mach number grows, the
  non-entropy-conservative KEEP scheme over-predicts the transformed
  velocity in the log region: its max-norm relative difference to the
  entropy-conservative EC-TP scheme is 0.23 %, 1.05 % and 1.98 % at Mach 3,
  4 and 5, against 0.57 %, 0.23 % and 0.78 % for the entropy-conservative
  scheme of Gouasmi et al. with a different pressure term, and 0.55 % for
  Ranocha's scheme (Mach 5 only). The transformation leaves these
  differences almost unchanged (relative differences of the untransformed
  and transformed velocity nearly equal; §4.2, Table 3). EC-TP is the
  reference by construction; there is no external DNS. See
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md).

- **Equivalent incompressible Reynolds numbers for implicit DG LES.**
  [Alberti et al. (2025b)](/sources/alberti-2025-c.md) (§III A, Eq. 39,
  Fig. 8) print the Trettel–Larsson pair in the form
  $y^*=(\langle\rho\rangle/\langle\mu\rangle)\sqrt{\tau_w/\langle\rho\rangle}\,y$,
  $U^+_{TL}=\int_0^{u^+}\sqrt{\langle\rho\rangle/\rho_w}\,\big[1+\tfrac12\,(y/\langle\rho\rangle)\,d\langle\rho\rangle/dy-(y/\langle\mu\rangle)\,d\langle\mu\rangle/dy\big]\,du^+$
  (averages over time and wall-parallel planes; they report Favre averages
  and state no significant difference from Reynolds averages, as cited),
  and use it to pair their isothermal-wall channels with incompressible
  ones and to choose grids for a modal entropy-stable DG
  [implicit LES](/definitions/implicit-les.md) (see
  [entropy conservation](/properties/entropy-conservation.md)). Under the
  transformation the cases $M_b=1.5$, $Re_\tau=222$ and $M_b=3$,
  $Re_\tau=450$ collapse on the incompressible DNS at $Re_\tau=180$ of Moser,
  Kim & Mansour (as cited), $M_b=1.5$, $Re_\tau=1000$ corresponds to
  $Re_\tau=590$ and $Re_\tau=500$ to about 350 (Fig. 8). On these
  "moderately under-resolved" grids (polynomial degree $N=8$ or 9, DNS-to-DG
  degree-of-freedom ratios 33–199) the untransformed mean velocity,
  Reynolds stresses and temperature agree with the compressible DNS of
  Modesti & Pirozzoli and of Coleman, Kim & Moser (as cited), except at
  $M_b=3$, where the profiles depart from the former beyond $y^+\approx45$
  in velocity and after the first cell in temperature, which the authors
  attribute to its Sutherland viscosity against the power law of the
  latter (§III A 2, Figs. 2–5). The transformation is used without a
  comparison against the alternatives above.
- **Wall-modelled hybrid LES of a supersonic plate.** [Zangeneh (2021)](/sources/zangeneh-2021.md)
  (§III.A.1, Fig. 6) plots the van Driest-scaled mean velocity of an SST-IDDES
  used as wall-modelled LES of a zero-pressure-gradient boundary layer at
  $M=1.69$, $Re_\theta=50\,000$ (adiabatic wall, Fig. 4) against the
  incompressible log law $\ln(y^+)/0.41+5.2$ and the experiment of Souverein
  et al. (as cited). The baseline has the right slope but a higher intercept,
  read as too low a skin friction, i.e. a
  [log-layer mismatch](/definitions/log-layer-mismatch.md), and the
  random-forest-corrected run follows the experiment over $30<y^+<3000$ (see
  [machine-learning wall models](/methods/machine-learning-wall-model.md)).
  The choice of transformation is not discussed.
- **LES with a one-equation SGS model.** [Qi et al. (2022)](/sources/qi-2022-b.md)
  compare all mean velocities in van Driest form,
  $u^+_{\mathrm{vD}}=\int_0^{u^+}\sqrt{\langle\rho\rangle/\rho_w}\,du^+$: in
  channels at Mach 1.5 (three LES grids) and Mach 3.0 their
  quasi-dynamic $k_{\mathrm{sgs}}$-equation model keeps the transformed log
  region closest to the DNS as the grid coarsens (Figs. 5, 12), and in a
  Mach 2.25 transitional flat-plate boundary layer it reproduces the van
  Driest profile at $x/L=8.8$ on all three grids (Figs. 16–17; see the
  [dynamic procedure](/methods/dynamic-procedure.md)).
- **DNS validation of shock/boundary-layer interactions.** [Tonicello et al. (2022)](/sources/tonicello-2022.md)
  (Fig. 5a) validate the incoming Mach 2.91 boundary layer of their
  [spectral-difference](/methods/spectral-difference-method.md) DNS of a 24°
  ramp with the van Driest velocity against $u^+=y^+$ and
  $u^+=\ln(y^+)/0.41+5.25$ and earlier DNS; [Yu et al. (2022)](/sources/yu-2022-e.md)
  (§2, Eq. 2.4a, Fig. 2) validate the Mach 2.28 incoming layer of their
  oblique interaction with the van Driest velocity against the Mach 2 DNS of
  Pirozzoli & Bernardini (as cited) at $Re_\tau\approx200$. Both walls are
  at or near the recovery temperature (see
  [shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
  A cold-wall counterpart is the Mach 6 swept-ramp DNS of
  [Zhang et al. (2022c)](/sources/zhang-2022-g.md) (§II C, Eq. 2,
  Fig. 6a; [OpenCFD-SCU](/software/opencfd-scu.md)), whose wall is at
  294 K against a printed recovery temperature of 585 K
  ($T_w/T_r\approx0.50$ *(compiler check, not in the sources)*). The van
  Driest velocity $\int_0^{u^+}\sqrt{\langle\rho\rangle/\rho_w}\,du^+$ of the
  incoming layer ($\delta=8.61$ mm, shape factor 9.30 at the reference
  station) follows the linear and logarithmic laws with a log-law intercept
  of 5.7, which the authors call higher than the incompressible value and
  attribute to the wall temperature. They do not test another
  transformation. On cooled walls Cogo et al. (above) report a log-law
  intercept mismatch of van Driest, Zhang et al. (2022, above) report that
  van Driest fails for their cooled cases, and Carlsson et al. call van
  Driest inaccurate for non-adiabatic walls.
- **Further incoming layers of shock interactions.** [Shi & Yan (2023)](/sources/shi-2023.md)
  (§IV.B, Eq. 29, Figs. 8–9) validate the Mach 2.9 incoming layer of a 24°
  ramp computed by flux-reconstruction implicit LES ($T_w=307$ K
  isothermal) with the closed Crocco–Busemann-based form of the van Driest
  velocity,
  $$U_{\mathrm{vD}}=\frac{U_\infty}{a_{\mathrm{vD}}}\left[\sin^{-1}\!\left(\frac{2a_{\mathrm{vD}}^2U/U_\infty-b_{\mathrm{vD}}}{Q_{\mathrm{vD}}}\right)+\sin^{-1}\!\frac{b_{\mathrm{vD}}}{Q_{\mathrm{vD}}}\right],$$
  $a_{\mathrm{vD}}=\big(\tfrac{\gamma-1}2M_\infty^2T_\infty/T_w\big)^{1/2}$,
  $b_{\mathrm{vD}}=T_{aw}/T_w-1$, $Q_{\mathrm{vD}}=\sqrt{b_{\mathrm{vD}}^2+4a_{\mathrm{vD}}^2}$
  ($T_{aw}$ the adiabatic-wall temperature; all page-local). The profile is
  converged on three grids and lies between two reference DNS, with the
  log law $\ln(y^+)/0.41+5.0$. [Gao et al. (2023)](/sources/gao-2023.md)
  (§5.2, Fig. 18) validate the shock-free Mach 2 layer of their DG implicit
  LES with the van Driest velocity against the DNS of Wenzel et al. (as
  cited): it follows the sublayer for $y^+\le5$ and the log law for
  $30\le y^+\le100$. The van Driest II transformed $C_f$ approaches the DNS
  and the correlation $0.024Re_\theta^{-0.25}$ (transformed quantities)
  soon after the forcing zone (Fig. 19). [Yu et al. (2023)](/sources/yu-2023.md)
  (§3, §4.1, Eq. 3.1) use the van Driest transform of an adiabatic-like
  Mach 2.28 layer ($T_w=1.92T_\infty$, the recovery temperature) in both
  directions. Forward, they show that just behind an oblique-shock
  interaction the log-law intercept falls well below 5.0 and returns to
  5.0 about $13\delta_r$ downstream of impingement. Inverted, they map a
  composite canonical profile back to physical velocity to extract a
  mixing-layer defect (see [skin-friction decomposition](/definitions/skin-friction-decomposition.md)).
- **Hypersonic inflow DNS.** [Mo et al. (2023)](/sources/mo-2023.md)
  (Eqs. 9–10; Figs. 9, 13) check their Mach 2.25, 2.9 and 7.25 flat
  plates with $dU^+_{\mathrm{vD}}=\sqrt{\langle\rho\rangle/\rho_w}\,dU^+$
  against $U^+_{\mathrm{vD}}=y^+$ ($y^+<6$) and $\ln(y^+)/0.41+5.1$. The
  Mach 7.25 cold-wall case ($T_w=562$ K, $T_e=64.4$ K) agrees with the
  experiment it reproduces at $\delta=9.5$ mm. No other transformation is
  tested.
- **Wall-modelled and learned-SGS LES.** [Maeyama & Kawai (2023)](/sources/maeyama-2023.md)
  (§4.1, Eq. 4.1, Fig. 4) compare WMLES and DNS of an adiabatic Mach 2.28
  layer through the van Driest velocity: they agree above the matching
  height at $Re_\tau\approx700$–2300. [Xu et al. (2023)](/sources/xu-2023.md)
  (§4.1, Eq. 4.1, Fig. 13a) compare their a posteriori LES of an
  isothermal-wall Mach 1.5 channel with filtered DNS through the van Driest
  velocity. In the log region their neural-network SGS model is "fully
  consistent" with the filtered DNS. The Vreman, dynamic Smagorinsky and
  WALE models give a larger transformed velocity and the no-model LES a
  slightly lower one, which they read as too much and too little SGS
  dissipation (see [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).
- **Hybrid RANS/LES against wall-resolved LES.** [Wang et al. (2024c)](/sources/wang-2024-j.md)
  (§III.B, Fig. 1) judge their wall-resolved LES of an adiabatic Mach 2
  flat-plate layer ($Re_{\delta_0}\approx13\,500$) on three grids, and the
  Spalart–Allmaras-based DES, DDES and scale-adaptive runs on the coarsest,
  by the van Driest-transformed mean velocity against the DNS of Pirozzoli
  et al. (as cited) and a log law printed in the figure legend as
  "5.2 + 2.44 log($y^+$)"; the finest LES agrees with the DNS, and the DES
  and DDES profiles show a [log-layer mismatch](/definitions/log-layer-mismatch.md).
  Reynolds stresses are density-scaled with $\langle\rho\rangle/\rho_w$.
- **Inside equilibrium wall models.** [De Vanna et al. (2022)](/sources/devanna-2022.md)
  (§2.2, Eq. 6) and [van Noordt et al. (2022)](/sources/vannoordt-2022.md)
  (§2.5, Eq. 35) write the van Driest damping of the mixing-length eddy
  viscosity of their compressible ODE
  [equilibrium wall model](/methods/equilibrium-wall-model.md) in the
  semi-local $y^*$ with $A^+=17$, $\kappa=0.41$, i.e. the Trettel–Larsson
  choice in the sense of Yang & Lv cited above. Van Noordt et al. (§1)
  call the choice of coordinate transformation "critical" and cite Iyer &
  Malik, who found results sensitive to the damping
  parameter and a semi-empirical scaling to "perform slightly better" than
  the Trettel–Larsson form used by Yang & Lv, while Chen et al. found the
  Trettel–Larsson form good for heat transfer; they keep Trettel–Larsson. De
  Vanna et al. (§4.1) also initialize their LES from a van Driest-transformed
  Musker profile.
- **Incoming layers of shock interactions and hypersonic DNS.** Five further DNS
  and LES validate their incoming boundary layer by the van Driest
  transformation. [Kang & Lee (2024)](/sources/kang-2024.md)
  (§III, Eq. 16, Fig. 4b): Mach 2.9, $Re_\theta=2400$, linear law in the
  sublayer and $5.0+2.44\log y^+$ in the log region, with the Morkovin-scaled
  intensities matching incompressible and compressible DNS.
  [Tang et al. (2024)](/sources/tang-2024.md) (§2.3, Eq. 2.6, Fig. 11a):
  Mach 5, $T_w/T_r=0.5$, linear for $y^+<4$, $2.44\ln y^++5.5$ for
  $y^+=30$–200, deviation from Duan et al. (2010, as cited) up to 3 % in the
  wake, attributed to Reynolds number and turbulence generation.
  [Yu et al. (2023b)](/sources/yu-2023-b.md) (§II, Eq. 8, Fig. 1): Mach 5,
  $T_w=0.75T_r$, linear for $y^+\lesssim5$ and logarithmic for $y^+=30$–60.
  [Wei et al. (2023)](/sources/wei-2023.md) (§III B, Eqs. 35–36, Figs.
  10–11): in a wall-resolved LES of a Mach 2.44 layer with synthetic-eddy
  inflow the transformed profile approaches the log law after
  $x/\delta=7$ and converges at $x/\delta=14$, and the density-scaled
  Reynolds stresses $\sqrt{\langle\rho\rangle/\rho_w}\,(R_{ii})^{1/2}/u_\tau$ (no
  sum) agree with experiments. [Zhang et al. (2024b)](/sources/zhang-2024-b.md)
  (§3.1, Fig. 5a): Mach 6 at three wall temperatures, slope 2.44 kept but
  intercepts 5.6–6.0, colder walls leaving the linear law closer to the
  wall; they conclude that the transformation "is more applicable to the
  adiabatic wall" (see [law of the wall](/definitions/law-of-the-wall.md)).
- **A reacting boundary layer.** In [Wang & Xu (2024)](/sources/wang-2024-h.md)
  (§4.2, Fig. 8) the van Driest profile of the hydrogen-film layer matches
  the canonical Mach 2, $Re_\tau=1000$ profile up to $y/\delta\approx0.3$ and
  falls below it in the outer layer, while the Griffin–Fu–Moin
  (total-stress-based) transformation against $y^*$ matches the linear and
  log laws ($\kappa=0.41$, $B=5.2$); the untransformed inner profile already
  matches well because the near-wall density varies slowly (adiabatic wall
  and a hydrogen-rich near-wall layer).

## Assessments of the temperature–velocity relation

Cogo et al. (2022, §4, Fig. 9) compare Walz's relation with the generalized
relation of Zhang et al. (2014), which they parametrize by a generalized
recovery factor $r_g=2c_p(T_w-T_\infty)/U_\infty^2-2Pr\,q_w/(U_\infty\tau_w)$ in
place of the analogy factor $s_{\mathrm{RA}}$ above (page-local $r_g$; a different
parametrization of the same relation). Zhang et al.'s relation is more
accurate at both Reynolds numbers; Walz stays within 3 % of the DNS, which
they attribute to wall cooling too mild to stress it. Huang et al. (2022,
§4.3.1, Table 5, Fig. 15) compare five quadratic relations
(Crocco–Busemann, Walz, Huang et al. 1993, Duan & Martin 2011, Zhang et al.
2014): all agree at Mach 2.5, while at Mach 10.9 with $T_w/T_r=0.20$ only Duan
& Martin and Zhang et al. fit the DNS, Duan & Martin being "significantly
simpler". Zhang et al. (2022, §3, Eqs. 3.1–3.2, Fig. 5) find the same split
on their six cases: Walz is accurate for the quasi-adiabatic walls and
deviates for the cooled ones, while the generalized relation of Zhang et al.
(2014), written with the generalized recovery factor $r_g$ as by Cogo et al.,
fits both. [Zhang et al. (2024b)](/sources/zhang-2024-b.md) (§3.1,
Eqs. 3.4–3.6, Fig. 6) repeat the comparison at Mach 6 for
$T_w/T_r=0.50$, 0.75 and 1.0: the Duan & Martin (2011) relation (constant
$C_{\mathrm{DM}}=0.8259$, with $1-C_{\mathrm{DM}}=0.1741$ on the quadratic
term) and the generalized relation of Zhang et al. (2014) match the DNS,
while Walz's relation deviates more as $T_w$ departs from $T_r$, and near the
edge even at $T_w/T_r=1.0$ because of the total-temperature overshoot (a
maximum of $1.02$ times the free-stream total temperature). Both
non-adiabatic relations reduce to Walz's for adiabatic walls.
[Tang et al. (2024)](/sources/tang-2024.md) (§2.3, Eqs. 2.7–2.8,
Fig. 11b), at Mach 5 with $T_w/T_r=0.5$, find Walz's relation close with a
slight mid-layer deviation, which they attribute to the cold wall violating
its assumption $Pr_t=1$, and the generalized relation, written with $r_g$,
in good agreement. The strong Reynolds analogies that relate the fluctuations are on
the [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md) page.

## Qualifications

- The forward transformations of van Driest, Trettel–Larsson and Volpiani et
  al. are not written out by Griffin et al. (2023); the forms above are those
  of Cogo et al. (2022) and Huang et al. (2022).
- Huang et al. (2022) print Eq. (4.4) with upper limit $u^+$ and differential
  $dz^*$, a velocity as the upper limit of an integral over the semi-local
  wall distance. Their §4.1
  quotes $Re_\tau^*=2626$, 9178 and 6213 at $Re_\tau=1172$ where their Table 4
  gives 2761, 9114 and 6149.
- Cogo et al. (2022) and Zhang et al. (2022, Table 3) evaluate their
  semi-local friction Reynolds number with free-stream properties, Huang et
  al. (2022) and Griffin et al. (2023) with boundary-layer edge or centreline
  properties.
- Zhang et al. (2022) call the generalized relation of Zhang et al. (2014)
  the "generalized Reynolds analogy" in the text (§3) and the "modified
  strong Reynolds analogy" in the caption of their Fig. 5.
- The GRA with fixed $s_{\mathrm{RA}}=1.14$ and $r=Pr^{1/3}$ is validated, in the works
  Griffin et al. cite, for channels, pipes and boundary layers with and without
  heat transfer; Griffin et al. (§5) state that complex flows (for example
  blunt-body boundary layers behind curved shocks) remain untested.
- **Printed form of Trettel–Larsson.** Carlsson et al. (2023) print Eq. (26)
  as $u_T^+=\int_0^{u^+}\sqrt{(\langle\mu\rangle/\mu_w)\,dy_T^+/dy^+}\,du^+$,
  with the square root over the whole product, whereas Cogo et al. (2022) and
  Huang et al. (2022) write the velocity stretching of the same
  transformation without a square root, $g_I=\mu^+dy^*/dy^+$ (table above).
  Both printed forms are recorded here without deciding between them.
  [Aiello et al. (2026)](/sources/aiello-2026.md) (§2.2) print a third
  form,
  $U^+_{TL}=\int_0^{U^+}\sqrt{\rho^+}\left(1+\frac{y}{2\langle\rho\rangle}\frac{d\langle\rho\rangle}{dy}-\frac{y}{\langle\mu\rangle}\frac{d\langle\mu\rangle}{dy}\right)dU^+$,
  without square root over the bracket; expanding
  $g_I=\mu^+\,d(y^+\sqrt{\rho^+}/\mu^+)/dy^+$ of the table gives exactly this
  integrand, so Aiello et al. agree with Cogo et al. and Huang et al.
  *(compiler check, not in the sources)*.
  [Alberti et al. (2025b)](/sources/alberti-2025-c.md) (Eq. 39) print the
  same integrand as Aiello et al., with $\sqrt{\langle\rho\rangle/\rho_w}$
  outside the bracket and no square root over it.
- Alberti et al. (2025b) state in §III A that the case $M_b=3$,
  "$Re=450$" corresponds to "an incompressible simulation at $Re=140$",
  while Fig. 8 and its discussion pair it with the incompressible
  $Re_\tau=180$; the captions of their Figs. 6–7 call the same $M_b=3$ case
  "incompressible".
- Aiello et al. (2026) evaluate $Re_\tau^*$ with centreline density and
  viscosity. Their Fig. 1 caption writes the log law in $y^+$ where the text
  writes it in $y^*$ (§4.1).
- Cao et al. (2024) print the bulk velocity and density as integrals over
  $[-\delta,\delta]$ without the factor $1/(2\delta)$ (§3.3), and their
  printed wall-unit spacings imply $Re_\tau\approx216$ where Table 5 gives
  211 ($\Delta x^+=4\pi Re_\tau/128=21.18$ with the $4\pi\delta$ box and 128
  cells gives $Re_\tau=215.7$, and $\Delta z^+=7.06$ with the $\tfrac43\pi\delta$ span gives 215.8) *(compiler
  check, not in the sources)*. Locators refer to the arXiv v1 preprint read (2021, five authors;
  the Journal of Scientific Computing version lists four).
- Zhang et al. (2024b, Eq. 3.6) define the generalized recovery temperature
  with the plain recovery factor $r$ and then define $r_g$, which is not used
  in any printed formula; Yu et al. (2023b, Eq. 8) print the van Driest
  integral with upper limit $\tilde u^+$ and a prefactor $1/u_\tau$, so that
  as printed the right-hand side has the dimension of an inverse velocity
  *(compiler check, not in the sources)*.
- Wang & Xu (2024, §4.2) place $Re_\tau=1067$ and 1051 at $x/h_0=125$ and
  150 ($h_0$ the hydrogen-stream height, page-local), where their Table 2
  gives these values at 100 and 125 (1044 at 150).
- Helm & Martín (2022, Sec. III B) write "The much shorter rescaling length
  of the DNS (29δ compared to 7δ for the LES)": as printed, the length called
  shorter is the larger number.

# Citations

- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1; §2.1, Eqs. (2.1)–(2.2); §2.2, Eqs. (2.3)–(2.5); §3, Figs. 1–7; §5.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4, Eqs. (4.1)–(4.4), Table 3, Figs. 8–9.
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1, Eqs. (4.1)–(4.5), Figs. 10–11; §4.3.1, Table 5, Fig. 15.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Eqs. (24)–(26), Table 2, Fig. 5.
- [Helm & Martín (2022)](/sources/helm-2022.md) — Sec. III B, Tables I–II, Fig. 3; Sec. IV F, Fig. 31.
- [Dang et al. (2022)](/sources/dang-2022.md) — §5.1, Fig. 17.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4.2, Eqs. (10)–(11), Figs. 11, 13 (arXiv v1).
- [Cao et al. (2024)](/sources/cao-2024.md) — §3.3, Tables 4–5, Figs. 7–8 (arXiv v1).
- [Chen et al. (2024)](/sources/chen-2024.md) — §1; §3.1, Eqs. (3.1)–(3.7), Fig. 3; §3.2, Eqs. (3.11)–(3.14), Figs. 4–5; §3.3, Eqs. (3.15)–(3.17), Fig. 6; App. B, Eq. (B1), Fig. 16.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §2.2; §4.1, Fig. 1; §4.2, Table 3.
- [Gao et al. (2022)](/sources/gao-2022.md) — §5.2, Figs. 16–17.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §III.A.1, Figs. 4, 6.
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §2; §3, Eqs. (3.1)–(3.2), Table 3, Figs. 3–5; §4; §5, Fig. 13.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §4, Figs. 5, 12, 16–17.
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — Fig. 5a.
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §2, Eq. (2.4a), Fig. 2.
- [Zhang et al. (2022c)](/sources/zhang-2022-g.md) — §II B, Table II; §II C, Eq. (2), Fig. 6a.
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §2.2, Eq. (6); §4.1.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §1; §2.5, Eq. (35).
- [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) — §1.1, Eq. (1); §2.2, Eqs. (7)–(8); §5–6 (semi-local $Re_\tau^*$ and $y^*$ in RANS damping; Patel and Trettel–Larsson equivalence as stated).
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §4.1, Eq. (4.1), Fig. 4; §5.4, Eqs. (5.3)–(5.5), Fig. 17; Apps. C–D, Figs. 28, 32.
- [Mo et al. (2023)](/sources/mo-2023.md) — §II B, Eqs. (9)–(13); Figs. 9, 13.
- [Shi & Yan (2023)](/sources/shi-2023.md) — §IV.B, Eq. (29), Table III, Figs. 8–9.
- [Gao et al. (2023)](/sources/gao-2023.md) — §5.2, Figs. 18–19.
- [Yu et al. (2023)](/sources/yu-2023.md) — §3, Eq. (3.1), Fig. 5; §4.1, Eq. (4.1).
- [Xu et al. (2023)](/sources/xu-2023.md) — §4.1, Eq. (4.1), Fig. 13a.
- [Wang & Xu (2024)](/sources/wang-2024-h.md) — §2.3; §4.2, Eq. (4.2), Figs. 8, 10–11; Table 2.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §3.1, Eqs. (3.1)–(3.14), Figs. 5–7.
- [Tang et al. (2024)](/sources/tang-2024.md) — §2.3, Eqs. (2.6)–(2.8), Fig. 11.
- [Kang & Lee (2024)](/sources/kang-2024.md) — §III, Eq. (16), Figs. 4–5.
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §II, Eq. (8), Fig. 1.
- [Wei et al. (2023)](/sources/wei-2023.md) — §III B, Eqs. (35)–(36), Figs. 10–11.
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §III.B, Figs. 1–2 (van Driest velocity as the yardstick of LES and hybrid runs; passing).
- [Alberti et al. (2025b)](/sources/alberti-2025-c.md) — §III A, Eq. (39), Fig. 8 (Trettel–Larsson pairing with incompressible channels); §III A 2, Figs. 2–7.
