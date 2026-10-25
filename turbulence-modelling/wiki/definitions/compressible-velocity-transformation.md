---
type: Definition
title: "Compressible velocity transformations"
description: "Maps that turn the mean velocity of a variable-property compressible wall layer into the incompressible law of the wall — van Driest, Trettel–Larsson, data-driven and total-stress-based — with semi-local scaling, temperature–velocity relations, and their assessment on DNS of channels and supersonic to hypersonic boundary layers."
status: established
aliases: [velocity transformation, compressible law of the wall, total-stress-based transformation, van Driest transformation, Trettel–Larsson transformation, semi-local scaling, generalized Reynolds analogy]
tags: [compressible, boundary-layer, wall-model, hypersonic]
timestamp: 2026-10-25T16:48:00Z
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
  semi-local units $y^*$ (Yang & Lv 2018, as recalled, §3).
- **Data-driven** transformation of Volpiani et al. (2020), used by Kumar &
  Larsson (2022) in the same inverse procedure (as recalled, §2.3).
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
  recalled).

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
  $Re_\tau^*\lesssim200$ (Griffin et al. 2021, as recalled, §3), which accounts
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

# Citations

- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1; §2.1, Eqs. (2.1)–(2.2); §2.2, Eqs. (2.3)–(2.5); §3, Figs. 1–7; §5.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §4, Eqs. (4.1)–(4.4), Table 3, Figs. 8–9.
- [Huang et al. (2022)](/sources/huang-2022.md) — §4.1, Eqs. (4.1)–(4.5), Figs. 10–11; §4.3.1, Table 5, Fig. 15.
