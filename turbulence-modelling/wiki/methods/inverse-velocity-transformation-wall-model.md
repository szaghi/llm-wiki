---
type: Method
title: "Inverse-velocity-transformation wall model"
description: "A one-ODE wall-stress model for compressible wall-modelled LES with heat transfer: the incompressible mixing-length solution is mapped to compressible profiles by the inverse total-stress-based velocity transformation, and temperature follows from a matching-anchored Reynolds analogy, with a priori and a posteriori accuracy and cost."
status: established
aliases: [compressible wall model based on an inverse velocity transformation, Griffin–Fu–Moin wall model, inverse-transformation wall model]
tags: [wall-model, wmles, compressible, hypersonic, boundary-layer]
timestamp: 2026-10-25T13:44:00Z
---

# Inverse-velocity-transformation wall model

The wall model of [Griffin et al. (2023)](/sources/griffin-2023.md) computes
the wall shear stress $\tau_w$ and wall heat flux $q_w$ of a compressible
turbulent boundary layer from the mean state at one matching height
$h_{\mathrm{wm}}$ in the inner layer and at the boundary-layer edge. It differs
from the classical compressible [equilibrium wall model](/methods/equilibrium-wall-model.md)
in exactly two respects (§2): (i) instead of a compressible momentum ODE, it
solves only the constant-property (incompressible) mixing-length ODE and maps
its strain rate to the compressible one through the inverse of the
total-stress-based [compressible velocity transformation](/definitions/compressible-velocity-transformation.md);
(ii) instead of a constant-$Pr_t$ energy ODE, it closes the temperature with an
algebraic temperature–velocity relation from the generalized Reynolds analogy.
One ODE replaces two coupled boundary-value problems. Page-local notation as
on the transformation page: $U$, $T$ Favre-averaged velocity and temperature,
$\rho^+=\langle\rho\rangle/\rho_w$, $\mu^+=\langle\mu\rangle/\mu_w$, subscripts
$w$, $e$, $m$ for wall, edge and matching height.

## Motivation

Griffin et al. (2023, §1) state two defects of the classical model, Eqs.
(1.1)–(1.3) on the equilibrium-wall-model page:

- **Robustness**: two coupled nonlinear boundary-value problems can be
  difficult to converge with strong heat transfer (Fu et al. 2021, as
  recalled).
- **Accuracy**: its damping function implicitly embeds the van Driest
  transformation, and its energy equation a constant $Pr_t=0.9$; both degrade
  with wall heat transfer (§3, §5).

## Algorithm

Inputs: $U_m$, $T_m$, $\langle\rho\rangle_m$ at $h_{\mathrm{wm}}$; $U_e$, $T_e$ at
the edge (located by the method of Griffin, Fu & Moin 2021, as recalled); the
wall temperature; an ideal gas, a viscosity law and constant pressure across
the inner layer (§2.3).

1. Integrate the constant-property mixing-length equation (with $\kappa=0.41$,
   $A^+=17$, evaluated at $Re_\tau^*$ instead of $Re_\tau$) once analytically
   and solve for the strain rate; this is the incompressible strain $S_t^+$
   of the transformation.
2. Substitute $S_t^+$ into the inverse transformation (Eq. 2.2),

   $$\frac{dU^+}{dy^*}=\left[\frac1{\mu^+S_t^+}-\frac1{\mu^+}+\sqrt{\rho^+}\left(1+\frac{y^+}{2\rho^+}\frac{d\rho^+}{dy^+}-\frac{y^+}{\mu^+}\frac{d\mu^+}{dy^+}\right)\right]^{-1},$$

   an initial-value problem integrated from the wall.
3. At each integration step, sub-iterate the velocity increment so that the
   temperature obeys the matching-anchored relation (Eq. 2.5)

   $$T=T_w+s\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_m}\right)+\left(\frac{U}{U_m}\right)^2(T_m-T_w),\qquad T_r=T_e+\frac{rU_e^2}{2c_p},$$

   with $s=1.14$, $r=Pr^{1/3}$, and update density and viscosity.
4. Shoot on $\tau_w$ until the integrated velocity matches $U_m$ at
   $h_{\mathrm{wm}}$. The heat flux follows algebraically,
   $q_w=s\,\tau_wc_p(T_w-T_r)/U_e$.

Anchoring the quadratic $T(U)$ at the matching point rather than at the edge
(as Zhang et al. 2014 do, as recalled) enforces the exact matching temperature.
The model outputs the mean profiles $U(y)$, $T(y)$ as well as $\tau_w$, $q_w$;
Griffin et al. (§5) suggest it also as a boundary condition for outer LES or
RANS, for inflow generation and as a base flow for perturbation methods.

## A priori evaluation

Matching data are taken from DNS at $h_{\mathrm{wm}}=0.3\delta$ (§3). Over 48
cases — isothermal-wall channels, supersonic pipes and diabatic supersonic and
hypersonic boundary layers, edge Mach number 0.77–11, $Re_\tau^*=170$–$5700$ —
the model has significantly smaller wall-stress and heat-flux errors than the
classical model, the reduction growing with the dimensionless heat transfer
$-B_q$, $B_q=q_w/(c_pT_w\rho_wu_\tau)$ (page-local) (Fig. 5). Velocity and
temperature profiles agree with DNS "significantly better" in every case shown
(Figs. 1–4), including a cooled-wall boundary layer at $M_e=11.46$,
$Re_\tau^*=5677$. In channels the semi-local damping models of Yang & Lv (2018)
and Chen et al. (2022) perform as well; in diabatic boundary layers the present
model improves the log slope of the velocity over them (Fig. 7).
Reynolds-number-dependent $\kappa$ and $A^+$ fitted to incompressible DNS change
little (Fig. 6).

## A posteriori evaluation

WMLES in [CharLES](/software/charles.md) (§4): nine isothermal-wall channels
matching the DNS of Trettel & Larsson (2016) at $M_b=0.7$–$4.0$,
$Re_\tau=319$–$1842$ ($Re_\tau^*=195$–$591$), $-B_q$ up to 0.19; 12 points per
half-height, $h_{\mathrm{wm}}=0.3\delta$; dynamic SGS model accounting only for
variable properties.

- Mean velocity and temperature are significantly more accurate than with the
  classical model in all cases (Figs. 8–9).
- The classical model's $\tau_w$ and $q_w$ errors grow with $-B_q$; the present
  model's are small and independent of heat flux (Fig. 10).
- **Fixed matching height, refined grid** ($M_b=3.0$, $Re_\tau^*=590$; 9, 18,
  36 points per half-height, $2\times10^4$ to $1.3\times10^6$ cells against
  $6.4\times10^8$ for the DNS): both models are only weakly grid-dependent; the
  classical model's log-intercept error persists, so its dominant error is the
  wall model (Fig. 13).
- **Matching height moving with the grid** ($h_{\mathrm{wm}}=0.3\delta$,
  $0.15\delta$, $0.075\delta$ for 12, 24, 48 points): the present model stays
  accurate at $Re_\tau^*=590$ and 200; the classical model converges
  non-monotonically at $Re_\tau^*=200$, because its relative error peaks in the
  buffer and early log layer, which $h^*_{\mathrm{wm}}$ enters (Figs. 14–15).
- Resolved fluctuations improve with the better mean but stay over-predicted,
  attributed partly to the wall-blocking effect of stress-based wall models
  and partly to numerical and SGS errors at this resolution; turbulent Mach
  numbers near 0.3 point to dilatational-dissipation modelling (§4,
  Figs. 11–12).

**Cost.** Between 7 % faster and 32 % slower than the classical model,
depending on Reynolds number, matching height and Mach number, with an
unoptimized implementation and no load balancing (§4).

## Limits stated by the authors

The accuracy is bounded by that of the forward transformation (documented
error at $Re_\tau^*\lesssim200$) and of the temperature–velocity relation; the
model ties $q_w$ algebraically to $\tau_w$ through the Reynolds analogy;
validation in complex flows is pending (§3, §5). Intermediate versions appear
in a CTR brief of the same title (Griffin, Fu & Moin 2022) and in Griffin's
thesis; Kumar & Larsson (2022) apply the same inverse procedure with a
data-driven transformation (§2.3, as recalled).

## Qualifications

- §4.1 states that $h_{\mathrm{wm}}=0.3\delta$, $0.15\delta$, $0.075\delta$ with
  12, 24, 48 points per half-height "corresponds to $y_m=4\Delta$". On a uniform
  grid of spacing $\delta/12$, $\delta/24$, $\delta/48$ each of these is
  $3.6$ grid spacings *(compiler check, not in the sources)*. The paper
  defines $\Delta$ as "the wall-normal grid spacing near the wall" (§4.1) but
  does not give its value on the hexagonally close-packed mesh.
- The printed Eq. (1.2) of the classical model and the "4.1" for $\kappa$ in §3
  are discussed on the [law of the wall](/definitions/law-of-the-wall.md) page.

# Citations

- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1, Eqs. (1.1)–(1.3); §2, Eqs. (2.1)–(2.5); §3, Eqs. (3.1)–(3.2), Figs. 1–7; §4, Table 1, Figs. 8–15; §5.
