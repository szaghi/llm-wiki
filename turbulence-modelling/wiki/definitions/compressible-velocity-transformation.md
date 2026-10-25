---
type: Definition
title: "Compressible velocity transformations"
description: "Maps that turn the mean velocity of a variable-property compressible wall layer into the incompressible law of the wall — van Driest, Trettel–Larsson, data-driven and total-stress-based — with semi-local scaling, the generalized Reynolds analogy for temperature, and the sources' ranking of the transformations."
status: established
aliases: [velocity transformation, compressible law of the wall, total-stress-based transformation, van Driest transformation, Trettel–Larsson transformation, semi-local scaling, generalized Reynolds analogy]
tags: [compressible, boundary-layer, wall-model, hypersonic]
timestamp: 2026-10-25T13:34:00Z
---

# Compressible velocity transformations

A compressible velocity transformation maps the Favre-averaged mean velocity
$U(y)$ of a compressible wall-bounded flow with variable density and viscosity
onto an equivalent incompressible profile that obeys the incompressible
[law of the wall](/definitions/law-of-the-wall.md). Once such a map is known,
the incompressible inner-layer physics — and any incompressible wall model —
can be carried to compressible flows with heat transfer. All content here is
from [Griffin et al. (2023)](/sources/griffin-2023.md), who invert one such
map to build the
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md);
the forward transformations are recalled by them. Page-local notation:
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

The ranking is that of one group of authors on their own transformation; the
bundle has no independent comparison yet. Griffin et al. (§1) also recall that
Iyer & Malik (2019) found the classical (van Driest-consistent) scaling more
accurate for adiabatic walls, while Yang & Lv (2018) and Fu, Bose & Moin (2022)
found semi-local damping better for cold walls.

## Qualifications

- The forward transformations of van Driest, Trettel–Larsson and Volpiani et
  al. are not written out in the source read; they enter here only through
  Griffin et al.'s account.
- The GRA with fixed $s=1.14$ and $r=Pr^{1/3}$ is validated, in the works
  Griffin et al. cite, for channels, pipes and boundary layers with and without
  heat transfer; Griffin et al. (§5) state that complex flows (for example
  blunt-body boundary layers behind curved shocks) remain untested.

# Citations

- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1; §2.1, Eqs. (2.1)–(2.2); §2.2, Eqs. (2.3)–(2.5); §3, Figs. 1–7; §5.
