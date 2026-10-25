---
type: Method
title: "Local-correlation-based transition models"
description: "RANS laminar–turbulent transition models that evaluate an empirical onset correlation with local variables and switch on the turbulence model through an intermittency; the γ-Reθ model, its calibrations and separation-induced correction, the one-equation γ and algebraic γ-alg-SST members, hysteresis, very-low-Reynolds airfoils and mesh requirements."
status: established
aliases: [LCTM, γ-Reθ-SST, separation-induced transition correction, Suluksna–Juntasaro calibration, Langtry–Menter calibration, local correlation-based transition modelling, γ-Reθ model, gamma-Re-theta, γ-SST, one-equation γ model, γ-alg-SST, algebraic LCTM model, algebraic intermittency model]
tags: [rans, transition, eddy-viscosity, boundary-layer, separated-flow]
timestamp: 2026-10-25T19:45:00Z
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

## The $\gamma$-$Re_\theta$ model and its separation-induced correction

Carreño Ruiz & D'Ambrosio (2022) print the two-equation $\gamma$-$Re_\theta$
model coupled to [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) as
implemented in STAR-CCM+ 14.06 (Menter et al. 2006; Langtry 2006; Langtry &
Menter 2009, as recalled), and test it on airfoils at very low Reynolds
number ([Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md),
§2, Eqs. 1–20). Page-local symbols: $\mathcal R_{\theta t}$ the transported
onset Reynolds number (the source writes it with an overbar, which the
registry reserves for the LES filter), $Re_{\theta t}$ its correlation value,
$\gamma_{\mathrm{eff}}$, $\gamma_{\mathrm{sep}}$, $s_1$, $R_T$, $\lambda_\theta$
and the functions $F$ as named in the source; $Re_V$ is the vorticity
Reynolds number of the previous section, which the source does not define
by formula.

**Transport equations** (Eqs. 7–11):

$$\begin{aligned}
\rho\frac{D\gamma}{Dt}&=\nabla\cdot\Big[\Big(\mu+\frac{\mu_t}{\sigma_\gamma}\Big)\nabla\gamma\Big]+F_{\mathrm{length}}c_{a1}\rho\lvert S\rvert\big[\gamma F_{\mathrm{onset}}\big]^{1/2}(1-c_{e1}\gamma)-c_{a2}\rho\lvert\Omega\rvert\gamma F_{\mathrm{turb}}(c_{e2}\gamma-1),\\
\rho\frac{D\mathcal R_{\theta t}}{Dt}&=\nabla\cdot\big[\sigma_{\theta t}(\mu+\mu_t)\nabla\mathcal R_{\theta t}\big]+c_{\theta t}\frac{\rho}{t}\big(Re_{\theta t}-\mathcal R_{\theta t}\big)(1-F_{\theta t}),
\end{aligned}$$

with $F_{\mathrm{onset}}$ triggering production, $F_{\mathrm{turb}}$ preventing
relaminarization, $t$ a time scale and $F_{\theta t}$ a blending function that
switches the $\mathcal R_{\theta t}$ source off inside the boundary layer, so
that the free-stream correlation value diffuses into it. The model is
therefore "semi-local": a free-stream edge must be defined. The source prints $S$
and $W$ in the production and destruction of $\gamma$ without defining
them; the page writes them as the strain-rate and vorticity magnitudes
$\lvert S\rvert$, $\lvert\Omega\rvert$, an identification the source does not
state *(compiler check, not in the sources)*. The
constants $c_{a1},c_{a2},c_{e1},c_{e2},c_{\theta t},\sigma_\gamma,\sigma_{\theta t}$
are those of Menter et al. (2006), not printed. The effective intermittency
$\gamma_{\mathrm{eff}}=\max(\gamma,\gamma_{\mathrm{sep}})$ scales both production
and destruction of $k$ (see the SST page), unlike the production-only
coupling of γ-alg-SST above.

**Onset correlation** (both calibrations, Eqs. 18–20), with $Tu$ in percent
and Thwaites' parameter $\lambda_\theta=(\theta^2/\nu)\,dU/ds$, $\theta$
estimated locally from $Re_{\theta t}$ so that the correlation is solved
iteratively:

$$Re_{\theta t}=\begin{cases}\big(1173-589.428\,Tu+0.2196\,Tu^{-2}\big)F(\lambda_\theta),&Tu<1.3,\\331.5\,(Tu-0.5658)^{-0.671}F(\lambda_\theta),&Tu>1.3,\end{cases}$$

$$F(\lambda_\theta)=\begin{cases}1-\big(-12.986\lambda_\theta-123.66\lambda_\theta^2-405.689\lambda_\theta^3\big)e^{-(Tu/1.5)^{1.5}},&\lambda_\theta<0,\\1+0.275\big(1-e^{-35\lambda_\theta}\big)e^{-Tu/0.5},&\lambda_\theta>0.\end{cases}$$

**Two calibrations** of the critical Reynolds number $Re_{\theta c}$ and the
transition length $F_{\mathrm{length}}$ (§2.1, Eqs. 12–17):

- *Suluksna–Juntasaro* (the STAR-CCM+ default, no pressure-gradient
  correction, $F(\lambda_\theta)=1$):
  $Re_{\theta c}=\min(\mathcal R_{\theta t},\,0.615\mathcal R_{\theta t}+61.5)$,
  $F_{\mathrm{length}}=\min\big(300,\,e^{7.168-0.01173\mathcal R_{\theta t}}+0.5\big)$;
- *Langtry–Menter (2009)*: piecewise polynomials in $\mathcal R_{\theta t}$
  (coefficients not printed), with
  $F_{\mathrm{length}}$ blended towards 40 near the wall by
  $F_{\mathrm{sublayer}}=\exp\big[-\big(\omega d^2/(200\nu)\big)^2\big]$.

**Separation-induced transition.** Langtry (2006) found reattachment
predicted downstream of experiment at low $Tu$, attributed to too little
production of $k$ in the separated shear layer; the correction lets the
intermittency exceed one (§2). Two forms are in use (Eqs. 5–6):

$$\gamma_{\mathrm{sep}}=\min\Big(s_1\max\Big[0,\frac{Re_V}{a\,Re_{\theta c}}-1\Big]e^{-(R_T/b)^4},\;c\Big)F_{\theta t},$$

with $(a,b,c)=(3.235,20,2)$ in the *updated* form (STAR-CCM+ since 2021.2)
and $(2.193,15,5)$ in the *older* one (up to 2021.1); $s_1=2$ by default and
$R_T$ the viscosity ratio of the damping (not defined in the source). The
threshold 3.235 is the ratio $Re_V/Re_{\theta c}$ at shape factor 3.5, taken
as separation, and 2.193 the maximum of $Re_V/Re_{\theta c}$ in a Blasius
profile. Like the bubble term of γ-alg-SST, the correction works by an
intermittency above one: with the older form $\gamma_{\mathrm{eff}}$ exceeds 3
in separated regions (§3.5, Fig. 7).

## Very-low-Reynolds airfoils and laminar separation bubbles

Carreño Ruiz & D'Ambrosio (2022) run 2D compressible RANS and URANS
(Roe flux, second order, polyhedral mesh with a prism layer at $y^+<1$ and
gradient-based adaptive refinement, $Tu=0.03\%$, $\mu_t/\mu=1$) on the SD7003,
Ishii and Eppler 387 airfoils at $Re=2.3\times10^4$–$2\times10^5$, where
transition is induced by laminar separation bubbles. They take the
transition location as the point where the skin friction starts to drop
(§3.5). On SD7003 at $Re=60{,}000$, $\alpha=4^\circ$, against the implicit LES
of Galbraith & Visbal (Tables 5, 8, 10):

| Setting | $x_{\mathrm{sep}}/c$ | $x_{\mathrm{tr}}/c$ | $x_{\mathrm{re}}/c$ | $C_L$ | $C_D$ |
|---|---|---|---|---|---|
| Langtry–Menter, older $\gamma_{\mathrm{sep}}$ | 0.202 | 0.518 | 0.660 | 0.600 | 0.0221 |
| Langtry–Menter, updated $\gamma_{\mathrm{sep}}$ | 0.185 | 0.535 | 0.769 | 0.603 | 0.0259 |
| Suluksna–Juntasaro, $s_1=2$ | 0.184 | 0.530 | 0.743 | 0.600 | 0.0257 |
| Suluksna–Juntasaro, $s_1=6$ | 0.202 | 0.536 | 0.680 | 0.593 | 0.0228 |
| Langtry–Menter with $F(\lambda_\theta)=1$ | 0.184 | 0.544 | 0.767 | 0.597 | 0.0264 |
| LES (Galbraith & Visbal) | 0.23 | 0.55 | 0.65 | 0.59 | 0.021 |

The authors conclude (§3.5, §4, §7):

- the Langtry–Menter calibration performs "significantly better" than the
  default one at $s_1=2$; at $\alpha=8^\circ$ the default does not reattach;
- the older correction beats the updated one: lowering the cap from 5 to 2
  reduces the production of $k$ and "considerably delays reattachment" —
  the opposite of the direction of the developers' update;
- with $F(\lambda_\theta)=1$ the Langtry–Menter correlation behaves like the
  default calibration, and the default with $s_1=6$ reproduces its forces
  while placing transition closer to the LES; the pressure-gradient
  correction and the separation correction "play a similar role", the former
  possibly double-counting pressure-gradient effects (after Malan et al.);
- no single $s_1$ fits all incidences (a low value is needed at $6^\circ$, a
  high one at $11^\circ$); they propose a second parameter in
  $\gamma_{\mathrm{sep}}$ to control bubble position and length separately;
- the model gives too little skin friction after reattachment (leading to
  early stall) and too early transition at $6^\circ$–$8^\circ$; at
  $Re=30{,}000$, $\alpha=8^\circ$ neither calibration reattaches while the LES
  reattaches at $x/c=0.53$ (Table 7); accuracy improves with Reynolds number,
  with "excellent" agreement with experiment at $Re=2\times10^5$ (§6.1);
- unsteady RANS is needed at low incidence, where trailing-edge vortex
  shedding raises the mean lift by 22.8% (SD7003, $Re=23{,}000$,
  $\alpha=2^\circ$; §5, Table 11), and near bubble bursting;
- on the more cambered Eppler 387 at $Re=60{,}000$ the 2D results agree with
  2D Navier–Stokes but not with 3D data, which the authors attribute to
  three-dimensional flow (§6.3).

They also recommend not exceeding $Tu=0.1\%$ and not using $Tu$ as a tuning
parameter (§3.4). Menter et al. (2022) report a related tendency of the
transport model γ-SST to overpredict bubble size at low Reynolds number on
Eppler 387 (see Validation); the two papers test different models.

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
- Carreño Ruiz & D'Ambrosio attribute the two $\gamma_{\mathrm{sep}}$ forms
  inconsistently: §2 places the 3.235 form in Menter et al. (2006) and the
  2.193 form in a first version by Langtry et al. (2006), while §3.5 says the
  2.193 form was introduced by Menter et al. (2004) and updated by Langtry &
  Menter (2009). The page names the forms by their STAR-CCM+ versions only.
- The same paper says $\gamma_{\mathrm{eff}}$ "well above 3" makes production
  "over 300% larger" than in natural or bypass transition; since production
  scales with $\gamma_{\mathrm{eff}}$, 300% larger needs $\gamma_{\mathrm{eff}}>4$
  *(compiler check, not in the sources)*. Its grid study (Table 3, medium
  grid: 0.181, 0.741, 0.6020, 0.02585) is close to the Suluksna–Juntasaro
  row of Table 5 (0.184, 0.743, 0.600, 0.0257) and differs from the
  Langtry–Menter one (0.202, 0.660, 0.600, 0.0221); the calibration used for the
  grid study is not stated. The text refers to the $\mathcal R_{\theta t}$
  transport equation as Eq. 11, which is its production term (the equation
  is Eq. 10).

# Citations

- [Menter et al. (2022)](/sources/menter-2022.md) — §1, §2 Eqs. 1–24 and Table 1, §2.3 Figs. 2–3, §3 Figs. 1, 4–24, §4 Figs. 25–28, §5.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §1, §2 Eqs. 1–20, §3.4 Table 4, §3.5 Tables 5–9 Fig. 7, §4 Table 10 Fig. 8, §5 Table 11, §6.1–6.3, §7.
