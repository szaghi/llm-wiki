---
type: Method
title: "Local-correlation-based transition models"
description: "RANS laminar–turbulent transition models that evaluate an empirical onset correlation with local variables and switch on the turbulence model through an intermittency; the γ-Reθ, one-equation γ and algebraic γ-alg-SST members, the hysteresis of transition location and its harmonic-averaging remedy, and mesh requirements."
status: established
aliases: [LCTM, local correlation-based transition modelling, γ-Reθ model, gamma-Re-theta, γ-SST, one-equation γ model, γ-alg-SST, algebraic LCTM model, algebraic intermittency model]
tags: [rans, transition, eddy-viscosity, boundary-layer, separated-flow]
timestamp: 2026-10-25T13:42:00Z
---

# Local-correlation-based transition models

Local-correlation-based transition modelling (LCTM) predicts laminar–turbulent
transition inside a RANS solver with local variables only. An empirical
correlation gives a critical momentum-thickness Reynolds number $Re_{\theta c}$
as a function of the local turbulence intensity and pressure gradient; a
vorticity Reynolds number, a local surrogate of $Re_\theta$, measures the
state of the boundary layer; where their ratio reaches about one, an
intermittency $\gamma$ switches on the production of the host turbulence
model ([$k$-$\omega$ SST](/methods/k-omega-sst-model.md) or GEKO in Menter et
al. (2022); Spalart–Allmaras in the SA-based variants they list). The
family covers natural, bypass and separation-induced transition. Menter et
al. (2022) present its lineage and an algebraic member, γ-alg-SST, that
needs no transport equation
([Menter et al. (2022)](/sources/menter-2022.md)).

## Family and lineage

As recalled by Menter et al. (2022, §1):

- a one-equation intermittency model (Menter et al. 2002), calibrated on
  free-stream turbulence only;
- the γ-Reθ model (Langtry et al. 2004; Menter et al. 2006; Langtry &
  Menter 2009), "arguably the first fully functional and locally formulated
  RANS transition model": one equation for $\gamma$ and one for the onset
  correlation;
- the one-equation γ model, γ-SST (Menter et al. 2015), which replaces the
  $Re_\theta$ equation by a local formulation with a pressure-gradient
  indicator built from the gradient of the wall-normal velocity;
- the algebraic γ-alg-SST of Menter et al. (2022).

Outside the family the same review lists $e^N$ methods, which exclude bypass
transition at high turbulence intensity, the amplification-factor transport
model, laminar-kinetic-energy models, non-local correlation models,
Spalart–Allmaras-based LCTM variants and other algebraic models (Kubacki et
al.; Cakmakcioglu et al. with SA; Sandhu & Ghosh). Transition occurs
approximately at $250<Re_\theta<1200$, depending on $Tu$ and pressure gradient
(§2.1). The authors justify an algebraic model by the observation that
transport transition models are dominated by their source terms and settle
quickly to a source equilibrium downstream of the inlet, convection and
diffusion playing a minor but not negligible role (§1).

## The algebraic γ-alg-SST model

The symbols $Re_V$, $\Omega_V$, $\mathrm{Rat}$, $Tu_l$, $\lambda_{\theta l}$,
$FPG$, $k_h$, $\gamma_b$, $\Phi_{1,2,3}$, $F_{RV}$ and the named coefficients
below are page-local transcriptions of the source's; $\gamma$ is the
intermittency (registry, transition pages only). Equations from Menter et
al. (2022), §2, Eqs. 1–22.

**Vorticity Reynolds number** (Eq. 1):
$$Re_V=\frac{\Omega_Vd^2}{2.2\,\nu},\qquad\Omega_V=\max(\lvert S\rvert,\lvert\Omega\rvert,0.1\,\omega).$$
$Re_V$ is bell-shaped across a laminar boundary layer; the factor 2.2 makes
its maximum equal $Re_\theta$ in zero pressure gradient, and the $0.1\omega$
floor gives $\gamma=1$ in the free stream.

**Intermittency** (Eqs. 2–3, 5):
$$\gamma=\tanh(\mathrm{Rat}^2),\qquad\mathrm{Rat}=\frac{\max(Re_V,60)}{Re_{\theta c}},\qquad P_k\to\gamma P_k .$$
$\gamma$ multiplies only the production of $k$; earlier LCTM models also made
the destruction depend on $\gamma$.

**Onset correlation and local indicators** (Eqs. 4, 8–11):
$$Re_{\theta c}=\min\Big(CTu_{\mathrm{crit}}\frac{ReC_{C1}}{Tu_l^{\,ReC_{C2}}},\ ReC_{\max}\Big)\,FPG(\lambda_{\theta l}),$$
$$Tu_l=100\,\min\Big(\frac{\sqrt{2k_h/3}}{\omega d},1\Big),\qquad
\lambda_{\theta l}=-0.1111\,\frac{dV}{dn}\frac{d^2}{\nu}+0.1875\in[-10,10],\qquad
\frac{dV}{dn}=\nabla(\boldsymbol n\cdot\boldsymbol u)\cdot\boldsymbol n,$$
$$FPG=\begin{cases}\min\big[\max\big(1-CFPG\cdot\max(\lambda_{\theta l},0),\,0.25\big),\,4\big],&\lambda_{\theta l}\ge0,\\
\min\big[\max\big(1-CAPG\cdot\min(\lambda_{\theta l},0),\,0.25\big),\,4\big],&\lambda_{\theta l}<0,\end{cases}$$
with $\boldsymbol n$ the wall-normal direction. The starting assumption is
$Re_{\theta c}\approx CTu_{\mathrm{crit}}/Tu$. The pressure-gradient indicator
uses only the wall-normal derivative of the wall-normal velocity, which
makes the model Galilean invariant.

**Harmonic averaging of $k$** (Eq. 12): $k_h=n\big/\sum_{i=1}^n k_i^{-1}$ over
the cell and its face neighbours. $Tu_l$ must measure the pre-transitional,
upstream level; once production switches on the local $k$ rises, and the
harmonic mean weights the small upwind values (§2.3).

**Bubble term** (Eqs. 13–18): $\gamma\to\gamma+\gamma_b$ with
$$\gamma_b=\min(C_{b1}\gamma\Phi_1\Phi_2\Phi_3,\ 3.0),\quad
\Phi_1=\frac{\max(\nu-\tfrac12\nu_t,0)}{0.2\nu+\nu_t},\quad
\Phi_2=\min\Big[\Big(\frac{Re_{V,H}}{300}\Big)^2,1\Big],\quad
\Phi_3=\min[\max(\mathrm{Rat}-C_{b2},0),5],$$
$$Re_{V,H}=\min(Re_V,1000)\frac{\min(\lvert S\rvert,\lvert\Omega\rvert)}{\max(\lvert S\rvert,\lvert\Omega\rvert,0.1\omega)}.$$
$\gamma$ may thus exceed one, up to four, inside laminar separation bubbles,
an "obviously unphysical enhancement" that compensates the slow response
of the two-equation model. $\Phi_1$ switches the term off once $\nu_t>2\nu$
and $\Phi_3$ acts only where $\gamma\approx1$ already, so the term accelerates
transition but does not start it.

**Coefficient blending** (Eqs. 19–22): bypass transition happens at low
$Re_V$ and natural transition at high $Re_V$, so each correlation coefficient
blends a "High" and a "Low" value,
$X=X_{\mathrm{High}}(1-F_{RV})+X_{\mathrm{Low}}F_{RV}$, with
$F_{RV}=2R/(1+R)$, $R=\min[(Re_V/RV_{\mathrm{switch}})^2,1]$.

| $CTu_{\mathrm{High}}$ | $CTu_{\mathrm{Low}}$ | $CFPG_{\mathrm{High}}$ | $CFPG_{\mathrm{Low}}$ | $CAPG_{\mathrm{High}}$ | $CAPG_{\mathrm{Low}}$ | $ReC_{C1}$ | $ReC_{C2}$ | $ReC_{\max}$ | $RV_{\mathrm{switch}}$ | $C_{b1}$ | $C_{b2}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.06 | 2.25 | 0.6 | 1.0 | −0.5 | −0.5 | 210 | 1.0 | 1000 | 1000 | 0.5 | 2.5 |

(Table 1.) The authors say twelve coefficients are more than the shown cases
need; they are exposed for user tuning, the "rubber-band" philosophy of
GEKO, against the few-coefficient emphasis of Juntasaro et al. (§2.5).
They also show that the tripping indicator $k/(\lvert S\rvert\nu)$ of Juntasaro
et al. is, with $\omega\sim\lvert S\rvert$, proportional to $Re_V\,Tu_l^2$, so that
model reads as an LCTM with $Re_{\theta c}\sim Tu_l^{-2}$ (Eqs. 23–24).

## Hysteresis of the transition location

Menter et al. (2022) call *hysteresis* the dependence of the converged
transition location on the initial condition, laminar or fully turbulent.
With the local cell $k$ in $Tu_l$, the Schubauer–Klebanoff natural-transition
plate ($Tu=0.03\%$) converges to different solutions from the two starts; the
turbulent front can get "locked". The harmonic mean $k_h$ removes the
multiplicity (§2.3, Fig. 2). The same defect appears in the one-equation γ
model in Ansys Fluent, a cell-centred finite-volume code, but not in Ansys
CFX, a mixed finite-volume/finite-element code where the model was
developed; harmonic averaging is now standard in the Fluent γ model
(Fig. 3). The authors report the same multiplicity for the algebraic models
of Kubacki et al. and Sandhu & Ghosh, with the caveat that those models are
not intended for that limit, and recommend a laminar-against-turbulent start
test as a standard procedure for every new transition model (§1, §5).

## Validation

In Ansys Fluent R21, cross-checked against the NTS code, γ-alg-SST is
compared with γ-Reθ-SST, γ-SST and experiment (§3):

- **Limiter of 60.** On T3A, without the floor on $Re_V$ in $\mathrm{Rat}$ the
  skin friction is underpredicted after transition and the velocity
  profile departs from the log law; with it $\gamma=1$ reaches deep into the
  sublayer (§2.2, Fig. 1).
- **Flat plates.** On the zero-pressure-gradient ERCOFTAC T3 cases the
  transition location agrees with the transport models and experiment; on
  the T3C pressure-gradient cases bypass transition comes earlier than with
  the transport models (Figs. 8–9).
- **Separation bubbles.** The model captures the reduction of bubble size with
  Reynolds number on the Volino–Hultgren plate but tends to underpredict
  it; without the bubble term the Eppler 387 bubble at $Re=10^5$ is far too
  large and lift drops at $4^\circ$–$8^\circ$ (Figs. 4–5, 10). γ-SST
  overpredicts bubble size at low $Re$ on Eppler 387 and Pak-B, which the
  authors read as a deficiency of that model's bubble terms (Figs. 16–19,
  24).
- **Natural-laminar-flow airfoils.** On NLF(1)-0416F the upper-surface
  transition location agrees with experiment from $\alpha=-12^\circ$ to
  $+2^\circ$, where γ-Reθ-SST falls outside the experimental range; on S809
  natural transition starts at $6^\circ$ against $7^\circ$ for the transport
  models and about $5^\circ$ in experiment (Figs. 13–15, 20–22).

Accuracy is overall of the same quality as the transport models; the
algebraic model predicts earlier natural transition and smaller bubbles.

## Mesh requirements

The algebraic model is "clearly less forgiving" of streamwise resolution:
on T3A the transport models stay reasonable at a streamwise step of
$10\delta$, while γ-alg-SST deviates from $2\delta$ (§4, Fig. 26). Recommended
meshes: $y^+\le1$ in the transition region, a wall-normal expansion ratio
of at most 1.15 (ratios above 1.2 to be avoided), a streamwise step not much
larger than $\delta$; wall-function meshes are unsuitable (§4, Figs. 26–28).

## Qualifications

- *Compiler check, not in the sources:* with the Table 1 values
  ($CFPG>0$, $CAPG<0$) both branches of the printed $FPG$ give values at or
  below one, so the upper cap 4 is never reached and both signs of
  $\lambda_{\theta l}$ lower $Re_{\theta c}$. Menter et al. neither plot $FPG$
  nor discuss its range, so whether the sign mapping or a coefficient sign
  differs from the printed one cannot be settled from the paper.
- Menter et al. print slips: Eq. 22 carries a stray "1"
  ($CAPG_{\mathrm{High}}(1-F_{RV1}1)$) where Eqs. 20–21 have $(1-F_{RV1})$; the
  §3.3 heading names NLF(1)-0416F twice where the section treats 0416F and
  0414F; the Volino–Hultgren intensities are $0.2\%$ and $7\%$ in the text but
  0.2% and 2.5% in Table 2; and §4 says of γ-alg-SST both that its transition
  location "stays unaffected" for larger $y^+$ and that it "moves upstream"
  above $y^+_{\max}=6$.
- The hysteresis of the Kubacki and Sandhu–Ghosh models is stated, not
  shown in this paper.

# Citations

- [Menter et al. (2022)](/sources/menter-2022.md) — §1, §2 Eqs. 1–24 and Table 1, §2.3 Figs. 2–3, §3 Figs. 1, 4–24, §4 Figs. 25–28, §5.
