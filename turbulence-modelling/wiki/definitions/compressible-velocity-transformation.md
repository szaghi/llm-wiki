---
type: Definition
title: "Compressible velocity transformations"
description: "Maps that turn the mean velocity of a variable-property compressible wall layer into the incompressible law of the wall — van Driest, Trettel–Larsson, data-driven and total-stress-based — with semi-local scaling, temperature–velocity relations, their assessment on DNS of channels and supersonic to hypersonic boundary layers, and their use as validation yardsticks."
status: established
aliases: [velocity transformation, compressible law of the wall, total-stress-based transformation, van Driest transformation, Trettel–Larsson transformation, semi-local scaling, generalized Reynolds analogy]
tags: [compressible, boundary-layer, wall-model, hypersonic]
timestamp: 2026-10-26T20:49:00Z
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
values (Coleman, Kim & Moser 1995; Huang, Coleman & Bradshaw 1995, as recalled
by Griffin et al. 2023, §3): $u_\tau^*=\sqrt{\tau_w/\langle\rho\rangle(y)}$ and
$y^*=y\,u_\tau^*\langle\rho\rangle/\langle\mu\rangle$, so that
$y^*=y^+\sqrt{\rho^+}/\mu^+$. The semi-local friction Reynolds number
$Re_\tau^*=\langle\rho\rangle_e u_\tau^*\delta/\langle\mu\rangle_e$ (with
$u_\tau^*$ evaluated at the edge or centreline) is invariant under the
transformation, so the incompressible constants are taken at $Re_\tau^*$ in
place of $Re_\tau$ (§2.1).

## General form

Cogo et al. (2022, §4, Eq. 4.1, Table 3), after Modesti & Pirozzoli (2016) as
they recall it, write every transformation as a stretching of the wall
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
  $y^+$ (Yang & Lv 2018, as recalled by Griffin et al. 2023, §3).
- **Trettel–Larsson (2016).** Implied by the same damping written in
  semi-local units $y^*$ (Yang & Lv 2018, as recalled by Griffin et al., §3).
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
  Larsson (2022) in the same inverse procedure (as recalled by Griffin et al., §2.3).
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
  Bai, Griffin & Fu (2022) under moderate pressure gradients (§2.1, as
  recalled by Griffin et al.).

  **Convention difference.** Cogo et al. (2022, Eq. 4.2) write the same
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
temperature. Griffin et al. (2023, §2.2) recall the Walz (modified
Crocco–Busemann) relation with recovery factor $r=Pr^{1/3}$, accurate for
adiabatic walls but degraded by heat transfer, and its recasting by Zhang et
al. (2014) as the generalized Reynolds analogy (GRA), with Reynolds-analogy
factor $s=1.14$ (Eq. 2.3; page-local $r$, $s$):

$$T=T_w+s\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_e}\right)+\left(\frac{U}{U_e}\right)^2(T_e-T_w),\qquad T_r=T_e+\frac{rU_e^2}{2c_p}.$$

It is equivalently a quadratic $T=b_0+b_1U+b_2U^2/2$ (Eq. 2.4) with $b_0=T_w$,
$b_1$ the wall slope from the Reynolds analogy and $b_2$ fixed by the edge
temperature. Griffin et al. fix $b_2$ instead by the matching-height
temperature $T_m$ at velocity $U_m$ (Eq. 2.5),

$$T=T_w+s\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_m}\right)+\left(\frac{U}{U_m}\right)^2(T_m-T_w),$$

which ties the wall heat flux to the wall stress, $q_w=s\,\tau_wc_p(T_w-T_r)/U_e$.
They judge the constant-$Pr_t$ energy equation of the classical model less
accurate than the GRA (citing Zhang et al. 2014).

Chen et al. (2024, §3.3, Eqs. 3.16–3.17) write the same quadratic with
the constant $C_T=0.8259$ of Duan & Martín (2011), recast as $s\,Pr$ with
$s=1.14$ after Zhang et al. (2014) as they cite them, and use the
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
  $Re_\tau^*\lesssim200$ (Griffin et al. 2021, as recalled by Griffin et al. 2023, §3), which accounts
  for the residual mismatch of their low-$Re_\tau^*$ cases.

Two independent DNS studies of boundary layers extend the comparison:

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
  perfectly (as they recall Trettel & Larsson 2016 and Yao & Hussain 2020);
  they suggest a stronger effect of cooling on the turbulent/viscous stress
  balance in external boundary layers. Volpiani et al. and the
  total-stress-based transformation collapse both viscous and log layers, the
  latter best across the inner layer, judged by the diagnostic
  $y\,dU_I^+/dy$; Huang et al. call the success of the data-driven
  transformation "not unexpected" since it was fitted on non-adiabatic
  boundary-layer data.

The sources thus agree that the total-stress-based transformation collapses
compressible wall layers at least as well as any alternative, and that
Trettel–Larsson succeeds in channels but not in the log layer of cooled
boundary layers; Griffin et al.'s ranking of their own transformation is no
longer the only evidence. Cogo et al. and Huang et al. differ only in
emphasis on whether Volpiani et al.'s transformation can be told apart. Griffin et al. (§1) also recall that
Iyer & Malik (2019) found the classical (van Driest-consistent) scaling more
accurate for adiabatic walls, while Yang & Lv (2018) and Fu, Bose & Moin (2022)
found semi-local damping better for cold walls.

A third DNS-based comparison, over twelve published zero-pressure-gradient
boundary layers at $M_\infty=2$–13.64 and $T_w/T_r=0.18$–1.9 (Chen et al.
2024, App. B, Fig. 16), gives mean absolute errors of 2.2 % for the
total-stress-based and 2.4 % for the HLPP transformation; the authors note
that their error measure differs from that of Hasan et al. Built into their
algebraic RANS model, the two give comparable a posteriori errors (velocity
0.7 % against 0.6 % in log-inner coordinates). They also recall reports, as
cited, that the total-stress-based transformation can degrade for
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

Six further sources use a transformation not to rank transformations but to
judge a simulation.

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
  choice of the van Driest transformation is not discussed, although the
  wall is isothermal with a non-zero heat flux ($B_q=-0.047$); Carlsson et al. (above) call it
  inaccurate for non-adiabatic walls on the strength of the studies they
  cite. See [implicit LES](/definitions/implicit-les.md).
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

## Assessments of the temperature–velocity relation

Cogo et al. (2022, §4, Fig. 9) compare Walz's relation with the generalized
relation of Zhang et al. (2014), which they parametrize by a generalized
recovery factor $r_g=2c_p(T_w-T_\infty)/U_\infty^2-2Pr\,q_w/(U_\infty\tau_w)$ in
place of the analogy factor $s$ above (page-local $r_g$; a different
parametrization of the same relation). Zhang et al.'s relation is more
accurate at both Reynolds numbers; Walz stays within 3 % of the DNS, which
they attribute to wall cooling too mild to stress it. Huang et al. (2022,
§4.3.1, Table 5, Fig. 15) compare five quadratic relations
(Crocco–Busemann, Walz, Huang et al. 1993, Duan & Martin 2011, Zhang et al.
2014): all agree at Mach 2.5, while at Mach 10.9 with $T_w/T_r=0.20$ only Duan
& Martin and Zhang et al. fit the DNS, Duan & Martin being "significantly
simpler". The strong Reynolds analogies that relate the fluctuations are on
the [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md) page.

## Qualifications

- The forward transformations of van Driest, Trettel–Larsson and Volpiani et
  al. are not written out by Griffin et al. (2023); the forms above are those
  of Cogo et al. (2022) and Huang et al. (2022).
- Huang et al. (2022) print Eq. (4.4) with upper limit $u^+$ and differential
  $dz^*$; the integration variable is the semi-local wall distance and the
  upper limit should be the corresponding wall-distance value. Their §4.1
  quotes $Re_\tau^*=2626$, 9178 and 6213 at $Re_\tau=1172$ where their Table 4
  gives 2761, 9114 and 6149.
- Cogo et al. (2022) evaluate their semi-local friction Reynolds number with
  free-stream properties, Huang et al. (2022) and Griffin et al. (2023) with
  boundary-layer edge or centreline properties.
- The GRA with fixed $s=1.14$ and $r=Pr^{1/3}$ is validated, in the works
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
- Aiello et al. (2026) evaluate $Re_\tau^*$ with centreline density and
  viscosity. Their Fig. 1 caption writes the log law in $y^+$ where the text
  writes it in $y^*$ (§4.1).
- Cao et al. (2024) print the bulk velocity and density as integrals over
  $[-\delta,\delta]$ without the factor $1/(2\delta)$ (§3.3), and their
  printed wall-unit spacings imply $Re_\tau\approx216$ where Table 5 gives
  211 ($\Delta x^+=4\pi Re_\tau/128=21.18$ with the $4\pi\delta$ box and 128
  cells gives $Re_\tau=215.7$, and $\Delta z^+=7.06$ gives 215.8) *(compiler
  check, not in the sources)*. Locators refer to the arXiv v1 preprint read (2021, five authors;
  the Journal of Scientific Computing version lists four).
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
