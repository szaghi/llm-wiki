---
type: Method
title: "Inverse-velocity-transformation wall model"
description: "A one-ODE wall-stress model for compressible wall-modelled LES with heat transfer: the incompressible mixing-length solution is mapped to compressible profiles by the inverse total-stress-based velocity transformation, and temperature follows from a matching-anchored Reynolds analogy, with a priori and a posteriori accuracy and cost."
status: established
aliases: [compressible wall model based on an inverse velocity transformation, Griffin–Fu–Moin wall model, inverse-transformation wall model]
tags: [wall-model, wmles, compressible, hypersonic, boundary-layer]
timestamp: 2026-10-28T07:07:00Z
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
  difficult to converge with strong heat transfer (Griffin et al. cite Fu
  et al. 2021).
- **Accuracy**: its damping function implicitly embeds the van Driest
  transformation, and its energy equation a constant $Pr_t=0.9$; both degrade
  with wall heat transfer (§3, §5).

## Algorithm

Inputs: $U_m$, $T_m$, $\langle\rho\rangle_m$ at $h_{\mathrm{wm}}$; $U_e$, $T_e$ at
the edge (located by the method of Griffin, Fu & Moin 2021, which Griffin et al. cite); the
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

   $$T=T_w+s_{\mathrm{RA}}\,Pr\,(T_r-T_w)\frac{U}{U_e}\left(1-\frac{U}{U_m}\right)+\left(\frac{U}{U_m}\right)^2(T_m-T_w),\qquad T_r=T_e+\frac{rU_e^2}{2c_p},$$

   with the Reynolds-analogy factor $s_{\mathrm{RA}}=1.14$ (registry §11), the
   recovery factor $r=Pr^{1/3}$ (page-local), and update density and viscosity.
4. Shoot on $\tau_w$ until the integrated velocity matches $U_m$ at
   $h_{\mathrm{wm}}$. The heat flux follows algebraically,
   $q_w=s_{\mathrm{RA}}\,\tau_wc_p(T_w-T_r)/U_e$.

Anchoring the quadratic $T(U)$ at the matching point rather than at the edge
(as Zhang et al. 2014 do, whom Griffin et al. cite) enforces the exact matching temperature.
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

## Transfer to an algebraic RANS closure

[Chen et al. (2024)](/sources/chen-2024.md) carry the two ingredients of this
model from WMLES into the algebraic RANS eddy viscosity of a whole
compressible boundary layer, the [Baldwin–Lomax model](/methods/baldwin-lomax-model.md);
they call the result a "wall model", but it supplies no wall stress to an LES
(§1). They state that the Griffin et al. model outperforms the classical ODE
wall model and cite it as the origin of both steps (§1, §3.3):

- **Velocity.** The inner-layer mixing length is rewritten for the
  Griffin–Fu–Moin transformed velocity instead of the Trettel–Larsson one
  that the semi-local Baldwin–Lomax model implies; the semi-local eddy
  viscosity diagnosed from DNS with this transformation scatters less and
  follows the incompressible curve more closely in the log region than with
  the Trettel–Larsson one (§3.1, Eqs. 3.5–3.7, Fig. 3).
- **Temperature.** The energy equation with constant $Pr_t=0.9$ is solved
  only above a matching height $y^*_{mT}=100$; below it the temperature is
  overwritten by the same matching-anchored quadratic relation as Eq. (2.5)
  above, with $C_{\mathrm{DM}}=0.8259$ (written $s_{\mathrm{RA}}Pr$ with $s_{\mathrm{RA}}=1.14$ after Zhang et al.
  2014, as cited) and the matching values sampled at $y_{mT}$ (Eq. 3.17,
  "following Griffin et al. 2023"). The results change little for
  $y^*_{mT}=50$–150 (App. A, Fig. 15).

Against twelve DNS of zero-pressure-gradient boundary layers at
$M_\infty=2$–13.64 and $T_w/T_r=0.18$–1.9, the combination lowers the mean
temperature error in outer coordinates from 8.8 % to 3.4 % and the velocity
error from 2.5 % to 1.3 % relative to the baseline semi-local model, and the
turbulent Prandtl number implied a posteriori reproduces the near-wall
singularity of the DNS (§4, Figs. 7, 13). For highly cooled walls
($T_w/T_r\le0.5$) the velocity transformation alone is insufficient and the
temperature–velocity relation is required (§4, Fig. 11); Griffin et al.
(2023, §1) had judged the constant-$Pr_t$ energy equation of the classical
model less accurate than the generalized Reynolds analogy. The evidence is for attached thin layers; Chen
et al. expect a smaller gain in channels and pipes, where the Trettel–Larsson
transformation is accurate and $Pr_t$ has no near-wall singularity (§5.1).

## Limits stated by the authors

The accuracy is bounded by that of the forward transformation (documented
error at $Re_\tau^*\lesssim200$) and of the temperature–velocity relation; the
model ties $q_w$ algebraically to $\tau_w$ through the Reynolds analogy;
validation in complex flows is pending (§3, §5). Intermediate versions appear
in a CTR brief of the same title (Griffin, Fu & Moin 2022) and in Griffin's
thesis; Kumar & Larsson (2022) apply the same inverse procedure with a
data-driven transformation (Griffin et al., §2.3, cite both).

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
- [Chen et al. (2024)](/sources/chen-2024.md) — §1; §3.1, Eqs. (3.5)–(3.7), Fig. 3; §3.3, Eqs. (3.16)–(3.17); §4, Figs. 7, 11, 13; §5.1; App. A, Fig. 15.
