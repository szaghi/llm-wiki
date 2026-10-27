---
type: Method
title: "Baldwin–Lomax algebraic model and its compressible recalibration"
description: "The two-layer algebraic RANS eddy viscosity of Baldwin and Lomax, a mixing length with van Driest damping under a Clauser–Klebanoff outer layer, in its semilocal form, and Chen et al.'s compressible modification by the Griffin–Fu–Moin and van Driest transformations and a two-layer temperature relation, tested on twelve high-speed boundary layers."
status: established
aliases: [Baldwin–Lomax model, BL model, BL-local, BL-GFM-VD-TV, Cebeci–Smith model, algebraic eddy-viscosity model, zero-equation model, algebraic wall model]
tags: [rans, eddy-viscosity, compressible, hypersonic, boundary-layer]
timestamp: 2026-10-26T20:48:00Z
---

# Baldwin–Lomax algebraic model and its compressible recalibration

The Baldwin–Lomax (BL) model is a zero-equation RANS closure: a
[Boussinesq](/definitions/boussinesq-hypothesis.md) eddy viscosity computed
algebraically from the local mean flow, with an inner branch (a mixing
length with van Driest damping) and an outer branch (a Clauser-type
viscosity with Klebanoff intermittency), switched at the height where the
two branches cross. Chen et al. (2024) recalibrate its semilocal form for
supersonic and hypersonic zero-pressure-gradient boundary layers with
"established" mean-flow scalings and no newly fitted coefficients
([Chen et al. (2024)](/sources/chen-2024.md)). Their title calls the model
an "algebraic wall model"; it supplies the eddy viscosity across the whole
boundary layer, solved by boundary-layer marching (§2.2), not a wall stress
for [wall-modelled LES](/methods/wall-modelled-les.md), although it borrows
ingredients from that literature.

On this page all flow quantities are means: $U$ and $T$ the Favre-averaged
streamwise velocity and temperature (page-local; the source's $\tilde U$,
$\tilde T$), $\rho$ the Reynolds-averaged density, $\mu$ the viscosity at
$T$; $U_e$ the edge velocity, subscript $w$ wall values, superscript $+$
wall units and $(\cdot)^*$ the registry's semilocal scaling, with
$y^*=y/\delta_\nu^*$, $\delta_\nu^*=\mu/(\rho u_\tau^*)$.

## The baseline model

Chen et al. start from "BL-local", the semilocal BL form of Gupta et al.
and Cheatwood & Thompson used in the LAURA code (§2.3, Eqs. 2.6–2.10). In
the thin-layer limit the vorticity magnitude is $\lvert\partial_yU\rvert$:

$$\mu_t=\begin{cases}\mu_{t,i},&y\le y_{m\mu},\\ \mu_{t,o},&y>y_{m\mu},\end{cases}\qquad
\mu_{t,i}=\rho\,l_{\mathrm{mix}}^2\lvert\partial_yU\rvert,\qquad l_{\mathrm{mix}}=\kappa y\big[1-e^{-y^*/A^+}\big],\qquad A^+=\frac{26}{\sqrt{\lvert\tau^+\rvert}},$$

with $\kappa=0.40$, $y_{m\mu}$ the crossing height of the two branches and
$\tau^+$ the local total shear stress over $\tau_w$ (page-local symbols
$l_{\mathrm{mix}}$, $y_{m\mu}$, $\tau^+$). Two features differ from the
original model: the damping uses $y^*$ instead of $y^+$, as in several
wall-modelled-LES works, and $A^+$ depends on the local total shear (§2.3).

The outer branch descends from Clauser's $\nu_{t,\max}=\alpha U_e\delta^*$,
with $\delta^*$ the kinematic displacement thickness, which gives the
Cebeci–Smith model $\mu_{t,o}=\rho\nu_{t,\max}F_{\mathrm{Kleb}}$; Baldwin &
Lomax replace $U_e\delta^*$ by $C_{cp}y_{\max}F_{\max}$:

$$\mu_{t,o}=\rho\,\alpha C_{cp}\,y_{\max}F_{\max}F_{\mathrm{Kleb}},\qquad
F_{\max}=\frac1\kappa\max_y\big(l_{\mathrm{mix}}\lvert\partial_yU\rvert\big),\qquad
F_{\mathrm{Kleb}}=\Big[1+5.5\Big(C_{\mathrm{Kleb}}\frac{y}{y_{\max}}\Big)^6\Big]^{-1},$$

with $y_{\max}$ the location of the maximum and the original constants
$\alpha=0.0168$, $C_{cp}=1.6$, $C_{\mathrm{Kleb}}=0.3$, kept (the wake limiter
for free shear is inactive). The turbulent heat flux uses an eddy
conductivity $c_p\mu_t/Pr_t$ with constant $Pr_t=0.9$ (§2.3). Gupta et al.
proposed Mach-dependent constants, which the authors do not adopt (§2.3).

**Diagnosis.** On the incompressible boundary layer of Schlatter & Örlü
at $Re_\theta=2540$ the branches cross at $y^+_{m\mu}=152$
($0.18\delta_{99}$); on the hypersonic cold-wall case M8Tw048R20 at $y^*_{m\mu}=67$
($0.09\delta_{99}$), so the outer eddy viscosity is too low and the region
$67<y^*\lesssim300$ is not governed by the log scaling (§2.3, Fig. 2).
BL-local reproduces the mean velocity of adiabatic layers but degrades
with heat transfer, and its temperature departs from DNS even for
adiabatic walls (§1).

## The compressible modification

The authors impose three principles: the incompressible model is not
altered, only well-established relations are used with no coefficient fitted
by the authors, and the change is as simple as possible (§1). All variants
reduce to the original model for incompressible constant-property flow
(§3.4).

**Inner layer: from the TL to the GFM transformation.** Writing the
mixing-length relation in semilocal form, the authors show that BL-local's
inner eddy viscosity is equivalent to applying the Trettel–Larsson (TL)
[velocity transformation](/definitions/compressible-velocity-transformation.md)
inside a van Driest-damped mixing length (§3.1, Eqs. 3.1–3.2):

$$-\rho^+\langle u''^+v''^+\rangle_\rho=\Big\lvert\frac{\partial U^+_{TL}}{\partial y^*}\Big\rvert^2\kappa^2y^{*2}\big[1-e^{-y^*/A^+}\big]^2 .$$

The DNS semilocal eddy viscosity built on TL collapses on the incompressible
curve $\kappa y^*[1-e^{-y^*/17}]^2$ (Johnson & King's scaling in semilocal
form) within and below the buffer layer but falls below it in the log
region, especially for diabatic layers (Fig. 3a). Built on the total-stress
Griffin–Fu–Moin (GFM) transformation it scatters less below $y^*\approx70$
and follows the curve further into the log region (Fig. 3b). The model
therefore replaces $U^+_{TL}$ by $U^+_{GFM}$ in the mixing-length relation
and recovers $\mu_{t,i}$ through the ratio of the two transformation kernels
(Eqs. 3.5–3.7).

**Outer layer: van Driest scaling.** The Cebeci–Smith alternative
$\nu_{t,\max}=\alpha_2u_\tau\delta_{99}$ ($\alpha_2=0.06$–$0.075$) is less robust
than $\alpha U_e\delta^*$ once compressible cases are included, its DNS value
varying by more than a factor two among diabatic cases (§3.2, Fig. 4). From
the large-Reynolds-number defect profile of Monkewitz et al., whose outer
maximum of $y\,\partial_yU^+$ is 5.55 at $0.155$ of the Rotta–Clauser
thickness, the BL replacement of $U_e\delta^*$ by $C_{cp}y_{\max}F_{\max}$ is
justified with the constant $1/(0.155\times5.55)$, "namely $C_{cp}$, though not
exactly the same value" (Eq. 3.10). The van Driest-transformed diagnostic
$\sqrt{\rho^+}\,y\,\partial_yU^+$ collapses the outer peaks of the DNS better
than the untransformed one (Eq. 3.12, Fig. 5). The modified outer branch is

$$F_{VD,\max}=\frac1\kappa\max_y\big(\sqrt\rho\,l_{\mathrm{mix}}\lvert\partial_yU\rvert\big),\qquad
\mu_{t,o}=\sqrt\rho\;\alpha C_{cp}\,y_{VD,\max}F_{VD,\max}F_{\mathrm{Kleb}}(y/y_{VD,\max}),$$

so that $\mu_{t,o}\sim\rho^{1/2}F_{\mathrm{Kleb}}$ and $\nu_{t,o}\sim\rho^{-1/2}F_{\mathrm{Kleb}}$,
a compromise between modelling $\nu_{t,\max}$ and $\mu_{t,\max}$; the constants
are unchanged and $y_{VD,\max}/\delta_{99}$ lies within 0.6–0.8 for most cases
(§3.2, Eqs. 3.13–3.14, Fig. 5f).

**Temperature: a two-layer formulation.** The turbulent Prandtl number from
DNS is 0.7–1.1 above the buffer layer, but near the temperature peak of
cold-wall layers the temperature gradient and the turbulent heat flux change
sign, so $Pr_t$ becomes negative or singular and is below 0.5 between the
singular point and the wall; monotone wall-distance formulae such as
$Pr_t=1-0.25y/\delta_{99}$ cannot represent this, and a constant 0.9
over-predicts the peak temperature (§3.3, Fig. 6; see
[Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)).
The model therefore solves the energy equation with constant $Pr_t$ only
above $y^*_{mT}=100$ and imposes below it the quadratic
temperature–velocity relation of Duan & Martín and Zhang et al., anchored
at the matching height (Eq. 3.17):

$$T=T_w+C_T(T_r-T_w)\Big(1-\frac{U}{U_m}\Big)\frac{U}{U_\delta}+(T_m-T_w)\Big(\frac{U}{U_m}\Big)^2,\qquad y<y_{mT},$$

with $C_T=0.8259$, $T_r$ the recovery temperature (recovery factor
$Pr^{1/3}$), subscripts $m$ and $\delta$ the matching height and the edge
(page-local symbols). The matched form follows the wall model of Griffin et
al. (2023) (see
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)).
Results change little for $y^*_{mT}$ between 50 and 150 (App. A, Fig. 15);
the relation is invalid in laminar flow, so the computation must start in
the turbulent regime.

The variants are BL-local, BL-GFM-VD (both transformations, constant
$Pr_t$), BL-GFM-VD-TV (plus the two-layer temperature) and BL-HLPP-VD-TV with
the transformation of Hasan et al. in place of GFM (§3.4, App. B).

## Solution method

The models are solved as boundary-layer equations ($\partial_yp=0$) by
streamwise marching in Mangler–Levy–Lees coordinates: third-order finite
differences in the marching direction, Chebyshev collocation with 241 points
across the layer, Newton iteration to $10^{-9}$, first-order Newton
convergence because the max and intersection operations make $\mu_t$
non-smooth (§2.2). A solution at a target station takes "minutes on a
desktop computer". The solver agrees with full Navier–Stokes BL results of
Hendrickson et al. at Mach 6 and with the authors' shock-capturing RANS at
Mach 14 (App. A, Fig. 14).

## Evidence

Twelve compressible zero-pressure-gradient DNS datasets (Pirozzoli &
Bernardini; Zhang, Duan & Choudhari; Volpiani et al.), $M_\infty$ 2 to 13.64,
$T_w/T_r$ 0.18 to 1.9, $Re_\tau$ 100 to 1113, plus Schlatter & Örlü's
incompressible layers, are the reference (Table 1; see
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)). With
relative errors integrated in a logarithmic inner coordinate and in a linear
outer coordinate up to $1.1\delta_{99}$ (Eq. 4.1), the averages over all cases
from BL-local to BL-GFM-VD-TV are (§4, Fig. 13):

| error | velocity, log coordinate | velocity, linear | temperature, log | temperature, linear |
|---|---|---|---|---|
| BL-local | 1.2% | 2.5% | 1.4% | 8.8% |
| BL-GFM-VD-TV | 0.7% | 1.3% | 0.4% | 3.4% |

- BL-local keeps the velocity error below 1.0% (log) and 1.6% (linear) for
  the adiabatic cases but exceeds 3% (linear) for the four hypersonic ones,
  and its temperature error exceeds 10% for the five hypersonic diabatic
  cases and 20% for a heated case (Fig. 13).
- On M8Tw048R20 the modified model raises the crossing height to
  $y^*_{m\mu}=242$ ($0.24\delta_{99}$) and its implied $Pr_t$ reproduces the DNS
  singular point near $y^*\approx8$ (§4, Fig. 7). On M6Tw025R11 the crossing
  height rises from 80 to 224 and both models under-predict $u_\tau$; it is the
  only case whose log-coordinate velocity error does not improve (Figs. 8,
  13).
- For heated and moderately cooled walls ($T_w/T_r>0.5$) the transformations
  alone already improve the temperature; for highly cooled walls
  ($T_w/T_r\le0.5$) "modifying only $\mu_t$ is insufficient" and the
  temperature relation is required (§4, Fig. 11). The temperature error of
  BL-GFM-VD lies between the other two models in every case (Fig. 13b).
- Wall quantities: the skin-friction coefficient ($\times10^3$) moves from
  2.07 to 2.13 against 2.31 (M2.5, adiabatic), 0.85 to 0.97 against 1.00
  (M6, $T_w/T_r=0.76$), 0.66 to 0.76 against 0.77 (M8) and 0.35 to 0.39
  against 0.40 (M14), but from 1.55 to 1.52 against 1.70 at M6 with
  $T_w/T_r=0.25$ (Table 2).
- The HLPP variant gives comparable errors (0.6%, 1.3%, 0.4%, 3.5%), and the
  two transformations have mean errors of 2.2% (GFM) and 2.4% (HLPP) over
  all cases (App. B, Fig. 16).

The authors claim that close agreement of the temperature with DNS in most
cases "has not been realized before" (§5.2), against earlier BL work of
Hendrickson et al. that improved the inner scaling with velocity
transformations but left temperature deviations for cold walls (§1).

## Qualifications

- The modifications assume attached thin-layer flow
  ($\lvert\partial_yU\rvert$ for the vorticity), so the modified model is less
  general than the baseline; pressure gradients and separation are future
  work, and the authors expect smaller gains in channels and pipes, where
  TL is accurate and $Pr_t$ has no near-wall singularity (§5.1).
- The use of the van Driest transformation in the outer layer of diabatic
  layers is admitted to be "somewhat insufficiently examined" (§3.2).
- Favre and Reynolds averages are treated as interchangeable when the RANS
  results are compared with mostly Reynolds-averaged DNS (§2.1); high-enthalpy
  effects are ignored even at Mach 14.
- The justification of $C_{cp}$ gives $1/(0.155\times5.55)\approx1.16$ against
  the model's 1.6 *(compiler check, not in the sources)*; the authors flag
  the mismatch themselves ("not exactly the same value").
- Chen et al. state that the denominator $\sqrt{\rho_w}$ is "moved out" of
  $F_{VD,\max}$ to combine with other factors, while Eq. 3.14 divides by the
  local $\sqrt\rho$; the step is not derived in the paper. On p. A7-10 the
  range "$0.09<y_{m\mu}/\delta_{99}\lesssim0.27$" should read $y/\delta_{99}$
  for the stated region.

# Citations

- [Chen et al. (2024)](/sources/chen-2024.md) — §1, §2.1–2.3 Eqs. 2.1–2.10 Fig. 2, §3.1–3.4 Eqs. 3.1–3.17 Figs. 3–6, §4 Eq. 4.1 Figs. 7–13 Tables 1–2, §5.1–5.2, App. A Figs. 14–15, App. B Fig. 16.
