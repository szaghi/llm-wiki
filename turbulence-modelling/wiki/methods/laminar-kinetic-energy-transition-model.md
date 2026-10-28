---
type: Method
title: "Laminar kinetic energy transition models"
description: "RANS transition closures that transport the energy of pre-transitional laminar fluctuations and transfer it to the turbulent kinetic energy at transition; the multi-mode reformulation of Pacciani et al. coupled to SST, the Walters–Cokljat model with correlation-based compressible thresholds of Ghidoni & Noventa, and their validation."
status: established
aliases: [LKE model, laminar kinetic energy model, k-kL-ω, k-kl-ω, three-equation transition model, LKE-SST]
tags: [rans, transition, eddy-viscosity, turbomachinery, separated-flow, boundary-layer]
timestamp: 2026-10-28T07:04:00Z
---

# Laminar kinetic energy transition models

A laminar-kinetic-energy (LKE) model adds to a two-equation RANS closure a
transport equation for $k_L$ (registry §11), the kinetic energy of the
non-turbulent fluctuations that grow in a laminar boundary layer before
transition (Klebanoff streaks, Tollmien–Schlichting waves). Transition is
modelled as a transfer term $\mathcal R$ (page-local) that moves energy
from $k_L$ to the turbulent kinetic energy $k$, leaving the total
fluctuation energy $k_L+k$ unchanged. Pacciani et al. (2025) trace the
concept to Mayle & Schulz (1997) and cite its use for
transition-sensitive closures by Walters & Leylek (2004), Walters &
Cokljat (2008) and Lardeau et al. (2007); a variant of Lopez & Walters
(2016) replaces $k_L$ by the wall-normal fluctuation energy
([Pacciani et al. (2025)](/sources/pacciani-2025.md), §1, §3.1). The
family sits beside the
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
which carry an intermittency instead of a fluctuation energy.

## The baseline model of Pacciani et al.

The authors' earlier model (Pacciani et al. 2011–2012), built for
separated-flow transition in low-pressure-turbine cascades, reads, with
$d$ the wall distance (the source's $y$) and $\lvert S\rvert$ the mean
strain magnitude (normalization not printed by the source)
(§3.1, Eqs. 1–9):

$$\frac{Dk_L}{Dt}=P_L-\mathcal R-D_L+\partial_j(\nu\,\partial_jk_L),\qquad D_L=2\nu\frac{k_L}{d^2},\qquad P_L=c_1\ell_s\sqrt{k_L}\,\lvert S\rvert^2,$$

with the Mayle–Schulz dissipation $D_L$, a production after Lardeau et
al. whose length $\ell_s$ (page-local) is the vorticity thickness of the
separated shear layer, a non-local quantity meant to model
Kelvin–Helmholtz growth, and the transfer, after Walters & Leylek,

$$\mathcal R=c_3f_tk_L\omega,\qquad f_t=1-e^{-\psi/c_4},\qquad \psi=\max\Big(\frac{\sqrt k\,d}{\nu}-c_5,0\Big),$$

so transition starts where the wall-distance Reynolds number
$\sqrt k\,d/\nu$ (the registry's $R_y$) reaches $c_5$. The $k$-equation of
the Wilcox $k$-$\omega$ model receives $+\mathcal R$, and its eddy viscosity
is damped by Wilcox's low-Reynolds function of $R_T=k/(\nu\omega)$
(page-local), which keeps the flow laminar before transition.

The authors list four weaknesses (§3.2): the vorticity thickness is
non-local; there is no bypass-transition term; the constant threshold
$c_5$ should depend on pressure gradient and free-stream turbulence; and
the coupling through the damping function is poor. On T3A the baseline
coupling gives an "erratic" skin friction, a non-physical sequence of
relaminarizations and retransitions, because the damping prevents the
transfer term from igniting the turbulence model; rational and exponential
damping forms did not fix it (§4.2, Fig. 1). The reformulation was also
motivated by Fang et al. (2024), whose multi-objective machine-learnt
corrections of the production and transfer found opposite trends for
separated-flow and bypass transition (§1, §3.2; see
[symbolic-regression closures](/methods/symbolic-regression-closure.md)).

**Requirements from wake-passing flows.** Sandberg & Michelassi (2022)
describe the LKE model of Pacciani et al. (2014), built for separated-flow
transition under incoming wakes, through the two requirements it was
designed to meet: on the wake-induced path no laminar kinetic energy is
created, transition being triggered by the wake velocity deficit (the
"negative jet") and the wake turbulence; between wakes, $k_L$ develops to
model the instabilities of the laminar layer. They report "realistic"
predictions for high-lift low-pressure-turbine cascades with incoming
wakes, and cite the $k$-$\overline{v^2}$-$\omega$ model of Lopez &
Walters (2016), which transports the wall-normal fluctuation to model the
growth of Klebanoff distortions driven by the wall-normal free-stream
component, as an alternative that predicted the separation bubble of a
low-Reynolds-number turbine accurately (citing Akolekar et al. 2018)
([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md), §3.3.3; see
[laminar separation bubble](/definitions/laminar-separation-bubble.md) and
[turbine cascades](/benchmarks/turbine-cascade.md)). The review does not
print the model's equations.

## The multi-mode reformulation

Pacciani et al. (2025) rebuild the model as a "base framework" whose few
closure functions are candidates for gene-expression-programming training
(§1, §4). The changes, all built on local quantities:

**Production with a local length scale and the large-scale turbulence.**
With $U$ the local velocity magnitude (page-local) and the shear-sheltering
split of Jacobs & Durbin and Walters & Cokljat,

$$f_{SS}=e^{-(c_{SS}\nu\lvert\Omega\rvert/k)^2},\quad k_{T,s}=f_{SS}k,\quad k_{T,l}=k-k_{T,s},\quad c_{SS}=2,$$

$$P_L=c_1\Big(\frac{\lvert\Omega\rvert d^2}{U}\Big)\lvert S\rvert^2\sqrt{k_{T,l}}$$

(Eqs. 10–13; $f_{SS}$, $k_{T,s}$, $k_{T,l}$, $c_{SS}$ page-local). The length
scale $\lvert\Omega\rvert d^2/U$ is taken from machine-learnt expressions of
Akolekar et al.; its wall-normal maximum is roughly proportional to the
momentum thickness and sits at about half the boundary-layer thickness in
attached layers and on the outer shear layer of laminar separation
bubbles, a behaviour checked on Falkner–Skan profiles but not shown
(§4.1). The velocity scale $\sqrt{k_{T,l}}$ makes the model respond to
free-stream turbulence, on the "established physical fact and common
assumption" that large-scale free-stream fluctuations drive pre-transitional
growth while small scales feed turbulence (§4.1).

**Intermittency coupling to SST.** The damping-function coupling is
replaced by an algebraic intermittency

$$\gamma=\frac{k_{T,s}}{k_L+k_{T,s}},$$

which multiplies the [SST](/methods/k-omega-sst-model.md) production as in
intermittency models (Eqs. 14–18):

$$\begin{aligned}
\frac{Dk_L}{Dt}&=(1-\gamma)P_L-\mathcal R-D_L+\partial_j(\nu\,\partial_jk_L),\\
\frac{Dk}{Dt}&=\gamma P_k+\mathcal R-\max(\gamma,0.1)\,\beta^*k\omega+\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_k}\Big)\partial_jk\Big],
\end{aligned}$$

with the $\omega$-equation and the eddy viscosity of SST (limiter
$\mu_t=\rho a_1k/\max(a_1\omega,F_2\lvert S\rvert)$, App. A Eq. A14). The
factor $(1-\gamma)$ drives $k_L$ and $\mathcal R$ to zero after transition:
$\mathcal R$ controls the onset, and once turbulent production starts the
intermittency controls the gradual rise of $k$ (§4.2). Using $k_{T,s}$
rather than $k$ in $\gamma$ avoids $\gamma\to1$ in accelerating laminar
layers where $k_L$ is smaller than the free-stream $k$ diffused into the
layer (§4.2). This $\gamma$ is algebraic and differs in definition from
the transported or algebraic intermittencies of the local-correlation
models. The authors state that the coupling works with any two-equation
model (§4.2).

**Laminar fluctuation diffusivity.** A viscosity
$\mu_L=c_{\mu,L}f_{\mu,L}\,\rho\,(\lvert\Omega\rvert d^2/U)\sqrt{k_L}$
(page-local), with a function $f_{\mu,L}$ of $R_T$ meant to keep it out of
the viscous sublayer, is added to the eddy viscosity in the diffusive
fluxes of momentum and energy (§4.3, Eq. 19).

**Pressure-gradient-dependent onset.** Beside Menter's local parameter
$\lambda_{\theta l}=-7.57\times10^{-3}\,[\nabla(\boldsymbol u\cdot\boldsymbol n)\cdot\boldsymbol n]\,d^2/\nu+0.0128$,
which is Galilean invariant but may need extra logic at corners between
walls, the authors introduce (§4.4, Eqs. 20–22; $s$ the streamwise
coordinate, $p$ the pressure, page-local symbols)

$$f_{PG}=\frac{d}{\nu\lvert S\rvert}\frac{\partial p}{\partial s},$$

local but not Galilean invariant, to give data-driven training a second
pressure-gradient input. The "proof of concept" thresholds are linear
(§5.1.3, Eqs. 28–29):

$$c_5(f_{PG})=\begin{cases}24,&f_{PG}\le0\\24-2f_{PG},&f_{PG}>0\end{cases}\qquad
c_5(\lambda'_{\theta l})=\begin{cases}24,&\lambda'_{\theta l}\ge0\\24+5.5\lambda'_{\theta l},&\lambda'_{\theta l}<0\end{cases}$$

with $\lambda'_{\theta l}$ Menter's parameter without its constants; Eq. 28
is used in all validation runs, and a dependence on free-stream turbulence
is left to future work.

**Separated-flow terms.** A separation switch replaces the non-local
vorticity thickness (§4.5, Eqs. 23–27):

$$P_L=c_1\Big(\frac{\lvert\Omega\rvert d^2}{U}\Big)\lvert S\rvert^2\sqrt{k_{T,l}}+f_{sep}P_{sep},\qquad P_{sep}=\max(c_{sep}\mu-\mu_t,0)\lvert S\rvert^2,\qquad \mathcal R=c_3(f_t+3c_{sep}f_{sep})k_L\omega,$$

$$f_{sep}=1-\exp\Big[-\max\Big(\frac{Re_v}{R_{cr}}-1,0\Big)\Big],\quad Re_v=\frac{\lvert S\rvert d^2}{\nu},\quad R_{cr}=800\max[\min(2r,8),1],\quad r=\frac{\lvert S\rvert d}{U}$$

(page-local symbols; the source calls $Re_v$ the vorticity Reynolds number
although it is built on the strain). $P_{sep}$ is borrowed from Menter et
al. (2015); its $\max(c_{sep}\mu-\mu_t,0)$ form is "self-destructing" in
turbulent flow and prevents spurious growth in wakes. The boosted transfer
targets the overlong bubbles that a delayed turbulence-model response
produces in many closures (§4.5); $f_{sep}$ "has no ambition of generality"
and is a training candidate.

**Constants.** Calibrated on the ERCOFTAC T3 plates (Table 2):

| $c_1$ | $c_3$ | $c_4$ | $c_5$ | $c_{\mu,L}$ | $c_{sep}$ | $c_{SS}$ |
|---|---|---|---|---|---|---|
| 0.02 | 0.02 | 8 | 24 | 0.03 | 10 | 2 |

$k_L=0$ at the inlet and on walls (App. A). The model uses local
quantities only but is not Galilean invariant, through $U$ in its length
scale and through $f_{PG}$ (§4.1, §4.4).

## Calibration and validation

All runs are steady two-dimensional RANS in the in-house TRAF code
(density-based, artificial compressibility for incompressible cases, a
formally third-order TVD scheme on Roe's flux) (§2).

**Flat plates.** On the [ERCOFTAC T3 plates](/benchmarks/ercoftac-t3-flat-plate.md)
(T3A, T3B, T3A–, Schubauer–Klebanoff, T3C1–T3C5; $288\times128$ cells, the
plate leading edge excluded):

- $c_1$ and $c_5$ compete: a larger $c_1$ raises $k_L$ and smooths the
  rise of $\gamma$, so $c_5$ must decrease to keep the onset; $c_1=0.02$
  with $c_5=24$ matches the T3A total fluctuation profiles up to
  $Re_x\simeq2.0\times10^5$ (§5.1.1, Figs. 2–3);
- lower $c_3$ does not start transition reliably and higher values make it
  too rapid; $c_{\mu,L}$ barely acts at zero and adverse pressure gradient
  but shapes the transitional $C_f$ ramp in favourable gradient, where
  0.03 then agrees "very well" with $\gamma$-$Re_\theta$ (§5.1.1–5.1.2,
  Fig. 10);
- medium ($289\times129$) and fine ($541\times221$) grids coincide on T3A–
  (Table 3, Fig. 8);
- on the low-$Tu$ plates (T3A–, Schubauer–Klebanoff), with no
  natural-transition term, the transition path is "definitely too steep",
  as with $\gamma$-$Re_\theta$ (§5.1.1, Figs. 7–8);
- with constant $c_5$ the adverse-gradient plates T3C2–T3C4 transition
  significantly late; both pressure-gradient thresholds correct the onset
  almost identically on T3C2, but the transition region stays too short;
  on T3C4 a small separation forms but $P_{sep}$ never activates because the
  pressure-gradient threshold triggers transition first (§5.1.3, Figs.
  11–13);
- on T3B and T3C1 the onset is right but the laminar $C_f$ is off,
  attributed to the missing leading edge (Figs. 6, 9).

**Turbine cascades.** On the transonic VKI LS89 vane (bypass transition,
heat transfer; $Re_{2,is}\simeq6\times10^5$ and $2\times10^6$, $Tu=1$–$6\%$),
with the inlet length scale tuned per case to the leading-edge heat
transfer, the suction-side onset is "reasonably well predicted" at the lower
Reynolds number and "in very good agreement" with the measurements at the
higher one, and at $Tu=6\%$ and high Reynolds number pressure-side transition appears
near $s/s_{tot}\approx0.4$ as measured; transition develops too quickly
(§6.1, Figs. 15–16). On the high-lift T106C and T108 cascades
($Re_{2,is}=0.8$–$1.6\times10^5$, $Tu=0.8\%$) the model reproduces the bursting
of the [laminar separation bubble](/definitions/laminar-separation-bubble.md)
into an open separation at the lowest Reynolds number on T106C, with
transition too early and an underestimated loss there, closed bubbles at the
higher Reynolds numbers, and short bubbles on the front-loaded T108, with
loss and lapse rate matched; $f_{sep}$ switches on at the separation point
near 80% axial chord on T106C (§6.2, Figs. 18–23). Results are "quite
insensitive" to $c_{sep}$ between 10 and 100; above 100 the post-reattachment
pressure recovery is too steep and below 10 unsteady transition paths can
appear (§6.2). See [turbine cascades](/benchmarks/turbine-cascade.md).

**Wind-turbine airfoil.** On the S809 airfoil ($Re=2\times10^6$, $Tu=0.2\%$,
twenty incidences in $0^\circ$–$12^\circ$) the trends are reproduced:
separation-induced transition on both sides up to about $5.5^\circ$, a rapid
upstream shift of the suction-side onset above $5^\circ$, and onset near the
leading edge above $9^\circ$; the predicted transition is slightly upstream of
the measurements at all angles (§6.3, Figs. 24–25).

Overall, the onset is predicted with "engineering accuracy", comparable to
$\gamma$-$Re_\theta$, transition lengths are consistently too short, and
separated-flow predictions reach the accuracy of the baseline model built
for them (§7).

## The Walters–Cokljat model with correlation-based thresholds

Ghidoni & Noventa (2026) start from the three-equation
$k_L$-$k$-$\omega$ model of Walters & Leylek (2004) and Walters & Cokljat
(2008), in the form of Lorini et al. (2021) with further corrections, and
replace the case-dependent thresholds of its two transfer terms by
critical momentum-thickness Reynolds numbers from the empirical onset
correlations of the intermittency models
([Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md), §II–§III). Symbols
in this section (page-local unless registry §11 lists them:
$\tilde\omega_\ell$, $k_L$, $R_{\mathrm{TRG}}$, $c_\theta$, $\gamma_A$,
$\gamma_B$, $\lambda_{\theta l}$, $Tu_l$): $\tilde\omega_\ell=\ln\omega$ the transported
variable (as on the [Wilcox page](/methods/k-omega-model.md)),
$k_{\mathrm{tot}}=k_L+k$, $k_{T,s}$ and $k_{T,l}$ the small- and large-scale
parts of $k$ (as above), $\ell_T=\sqrt k/\omega$ and
$\ell_{\mathrm{eff}}=\min(C_\lambda d,\ell_T)$ the turbulent and wall-limited
length scales (the source's $\lambda_T$, $\lambda_{\mathrm{eff}}$),
$R_{\mathrm{TRG}}$ the second transfer term, $c_\theta$, PGC and
$\lambda_{\theta l}$ the scale factor, pressure-gradient correction and
pressure-gradient parameter below, $M_e$ the boundary-layer-edge Mach number.

**Structure.** The compressible model transports $k_L$, $k$ and
$\tilde\omega_\ell$; the energy equation receives the opposite of the net
sources of both kinetic energies (§II, p. 3):

$$\begin{aligned}
\frac{D(\rho k)}{Dt}&=\nabla\cdot\Big[\Big(\mu+\frac{\rho\alpha_T}{\sigma_k}\Big)\nabla k\Big]+\rho\big(P_k+\mathcal R+R_{\mathrm{TRG}}-D_k\big),\\
\frac{D(\rho k_L)}{Dt}&=\nabla\cdot(\mu\nabla k_L)+\rho\big(P_{k_L}-\mathcal R-R_{\mathrm{TRG}}-D_{k_L}\big),
\end{aligned}$$

with $\alpha_T$ (page-local) an effective turbulent diffusivity, the
dissipations $D_k=k\omega+2\nu k/d^2$ and $D_{k_L}=2\nu k_L/d^2$ (Eq. 13),
which replace the anisotropic terms of Walters & Cokljat "for robustness",
"even more important for high-order solvers", and productions computed
from the full small- and large-scale Boussinesq stresses, which the
authors prefer to the incompressible approximation $\nu_{T,s}\lvert S\rvert^2$
of Walters & Cokljat. The small-scale eddy viscosity is
$\nu_{T,s}=f_\nu f_{\mathrm{INT}}C_\mu\sqrt{k_{T,s}}\,\ell_{\mathrm{eff}}$ with
$k_{T,s}=f_{SS}f_Wk$, the shear-sheltering function
$f_{SS}=\exp[-(C_{SS}\nu\lvert\Omega\rvert/k)^2]$, the realizable
$C_\mu=1/(A_0+A_S\lvert S\rvert/\omega)$ and the onset function
$f_{\mathrm{INT}}=\min\big(k/(C_{\mathrm{INT}}k_{\mathrm{tot}}),1\big)$; the
large-scale viscosity adds a natural-transition part built on a threshold
of $d^2\lvert\Omega\rvert/\nu$ (Eqs. 1–12). The shear-sheltering split is the
one Pacciani et al. use above, with $C_{SS}=1.7$ here against $c_{SS}=2$
there. Positivity is handled by clipping $k_L$ and $k$ at zero in the
source terms only, which "allows the solution to oscillate" (§II).

**The original transfer terms and their thresholds.**

$$\mathcal R=C_R\beta_R\frac{k_L\lvert\Omega\rvert}{f_W},\quad \beta_R=1-e^{-\phi_R/A_R},\quad \phi_R=\max\Big(\frac{k}{\nu\lvert\Omega\rvert}-C_{R,\mathrm{crit}},0\Big),$$

$$R_{\mathrm{TRG}}=C_{R,\mathrm{TRG}}\beta_{\mathrm{TRG}}k_L\lvert\Omega\rvert,\quad \beta_{\mathrm{TRG}}=1-e^{-\phi_{\mathrm{TRG}}/A_{\mathrm{TRG}}},\quad \phi_{\mathrm{TRG}}=\max\Big(\frac{d^2\lvert\Omega\rvert}{\nu}-\frac{C_{\mathrm{TRG,crit}}}{f_{\mathrm{TRG,crit}}},0\Big)$$

(Eqs. 19–25; $C_{R,\mathrm{crit}}=1.75$). The thresholds compare the
Reynolds numbers $k/(\nu\lvert\Omega\rvert)$ and $d^2\lvert\Omega\rvert/\nu$
with model constants that need case-by-case recalibration (§I). The
authors rename the two terms of the literature, "bypass" and "natural",
to "main" and "triggering" (TRG), because all of them act in natural
transition: $R_{\mathrm{TRG}}$ acts only in natural-mode cases,
upstream of $\mathcal R$, raising the local turbulence intensity until the
main term triggers (pp. 3, 7).

**The proposed thresholds.** Both thresholds are rewritten on a local
estimate of the momentum-thickness Reynolds number (Eqs. 21, 26):

$$\phi_R=\max\Big(\frac{d^2\lvert\Omega\rvert}{\nu\,c_\theta}-Re_{\theta c},0\Big),\qquad
\phi_{\mathrm{TRG}}=\max\Big(\frac{d^2\lvert\Omega\rvert}{\nu\,c_\theta}-Re_{\theta c,\mathrm{TRG}},0\Big),$$

with $c_\theta$ the ratio of $d^2\lvert\Omega\rvert/\nu$ to $Re_\theta$,
$c_\theta\simeq2.197$ in incompressible flow, and $f_{\mathrm{TRG,crit}}$
dropped. The critical values come from the Langtry–Menter correlation of
the [local-correlation-based models](/methods/local-correlation-based-transition-model.md),
evaluated with the local turbulence intensity
$Tu_l=(\tfrac23k)^{1/2}/\lvert\boldsymbol u\rvert$ (limited to $Tu_l>0.1$):
its natural-transition branch ($Tu_l\le1.3$) feeds $R_{\mathrm{TRG}}$
and its bypass branch ($Tu_l>1.3$) feeds $\mathcal R$ (§II, Eq. 27):

$$Re^*_{\theta c}=\begin{cases}1173.51-589.428\,Tu_l+0.2196\,Tu_l^{-2},&Tu_l\le1.3,\\ 331.50\,(Tu_l-0.5658)^{-0.671},&Tu_l>1.3,\end{cases}$$

the operator between the first two terms being missing in print (see
Qualifications). Corrections for pressure gradient and compressibility then
multiply both branches (§III, Eqs. 28–33):

$$Re_{\theta c}=Re^*_{\theta c}\,\mathrm{PGC}\,(1+M_e^2),\qquad
\mathrm{PGC}=\begin{cases}1+(12.986\lambda_{\theta l}+123.66\lambda_{\theta l}^2+405.689\lambda_{\theta l}^3)\,e^{-(Tu_l/1.5)^{1.5}},&\lambda_{\theta l}\le0,\\ 1+0.275\,(1-e^{-35\lambda_{\theta l}})\,e^{-Tu_l/0.5},&\lambda_{\theta l}>0,\end{cases}$$

with $\lambda_{\theta l}=(\theta^2/\nu)\,\partial_s\lvert\boldsymbol u\rvert$ along
the local streamline, limited to $(-1,1)$, and $\theta$ recovered from the
same local estimate, $\theta=(d^2\lvert\Omega\rvert/\nu)\,c_\theta^{-1}\,\nu_\infty/u_\infty$.
PGC lowers $Re_{\theta c}$ in adverse and raises it in favourable pressure
gradient. In compressible flow $c_\theta$ is the zero-pressure-gradient part
of the Mach- and wall-temperature-dependent fit of Liu et al. (2022), whose
pressure-gradient part is dropped because Crivellini et al. found the
first term dominant and to avoid an iterative solve for $\theta$ (§III).
Citing Huang et al., the authors note that the ratio $c_\theta$ ranges
from 2.2 to 8.4 for $0.2<M_e<10$ and is reduced by wall cooling (§II). The
edge Mach number, temperature and velocity come from isentropic relations
with free-stream data and the local pressure. The model uses no non-local
integration, which is why the authors still call it local although
free-stream values enter the corrections and the boundary conditions
(§II–§III). They require each correlation to be used with the same
turbulence intensity, local or free-stream, as its calibration, and so
adopt none of the free-stream-based supersonic correlations (§III).

**Constants** (Table I): $A_0=2.04$, $A_S=2.12$, $A_\nu=5.20$, $A_R=0.2$,
$A_{\mathrm{TRG}}=1000$, $A_{TS}=200$, $C_{R,\mathrm{crit}}=1.75$, $C_{NC}=0.1$,
$C_{\mathrm{TRG,crit}}=1600$, $C_{\mathrm{INT}}=0.95$, $C_{R,\mathrm{TRG}}=0.013$,
$C_{l1}=3.4\times10^{-6}$, $C_{l2}=2.58\times10^{-12}$, $C_R=0.14$,
$C_{\alpha,\theta}=0.03$, $C_{SS}=1.7$, $C_{\tau,l}=4360$, $C_{\omega1}=0.44$,
$C_{\omega2}=0.92$, $C_{\omega3}=0.3$, $C_{\omega R}=1.5$, $C_\lambda=2.075$,
$C^*_\mu=0.09$, $Pr_t=0.85$, $\sigma_k=1$, $\sigma_\omega=1.17$, $C_{k1}=10$,
$C_{k2}=6$, $C_{SI}=1150$ (all page-local names of the source).

**Onset measures.** Transition onset is the location of the average of
$C_f$ over the transition region, start and end at the $C_f$ minimum and
maximum (after Jacobs & Durbin), or from $C_p$ where the experiment used
it. For comparison with intermittency-based measurements the authors
propose $\gamma_B=(k-k_{\min})/(k_{\max}-k_{\min})$ along the plate, beside
$\gamma_A=k/k_{\mathrm{tot}}$, each set to 0.5 at onset ($\gamma_A$,
$\gamma_B$ registry §11, not a transported intermittency; §IV, Eq. 34).

**Discretization.** The model runs in a modal discontinuous Galerkin RANS
solver with primitive logarithmic variables ($\ln p$, $\ln T$,
$\tilde\omega_\ell$), BR2 viscous fluxes, an exact Riemann solver,
residual-based artificial-viscosity shock capturing and linearized backward
Euler with pseudo-transient continuation, at polynomial degree $N=4$
with $y_1^+=1$; every degree is started from the converged lower one
(Appendix; see
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)).

### Validation

All from Ghidoni & Noventa (2026), §IV–§V:

- **ERCOFTAC T3A, T3B, T3A–** ([ERCOFTAC T3 plates](/benchmarks/ercoftac-t3-flat-plate.md)):
  $C_f$-distribution errors 3.38%, 15.81% and 7.67%; onset errors 8.22%
  (T3A) and 22.22% (T3B). On T3B the start of transition agrees but the end
  lies downstream ($1.59$ against $1.22\times10^5$ in $Re_x$), which the
  authors attribute to the $Re_\theta$ threshold in $\phi_R$, which "avoids
  the influence of $k$ and limits the transfer"; the original model gives
  a shorter region and a higher $C_f$ peak (Figs. 4–5). For T3A– they use
  $Tu_\infty=0.48\%$ instead of the experimental 0.9%, for which the
  Coupland and Abu-Ghannam & Shaw onsets differ by 137.62% (Fig. 6). The
  T3A $C_f$ error converges from 3.89% at $N=1$ to 3.38% at $N=4$ on 4000
  elements (Fig. 7).
- **Adverse pressure gradient** (T3C2–T3C5): $C_f$ errors 7.56%, 4.61%,
  12.67%, 5.89%; without PGC the T3C2 onset error rises from 2.98% to
  18.65% and the $C_f$ error to 31.81% (Fig. 8). The T3C4 bubble is on the
  [laminar-separation-bubble page](/definitions/laminar-separation-bubble.md).
- **Natural transition**: Schubauer–Klebanoff onset error 8.34% and
  Schubauer–Skramstad onset errors 3.00%–6.01% at $Tu_\infty=0.1$–$0.34\%$
  (Table IV), with the TRG terms acting upstream of the main ones; on T3A
  they are zero (Figs. 10–11).
- **Free-stream length scale and intensity**: a sweep of the free-stream
  length scale moves transition downstream with increasing scale, but the
  model "seems to fail" the twofold effect found by Fransson & Shahinfar,
  as the original model does according to Yin et al.; on 42
  Fransson–Shahinfar cases the onset error is 18%–23% with the $C_f$-based
  onset and 5%–9% with $\gamma_B$ (Fig. 14). Lowering $Tu_\infty$ tenfold
  moves the onset monotonically, without the slope reversals reported for
  Lorini et al. and Bulgarini et al. (Fig. 15).
- **Heated plates** (Blair): zero-pressure-gradient $C_f$ errors 1.94%–14.51%;
  in favourable pressure gradient 14.89%–24.87%, with transition regions
  shorter than measured (Figs. 17–20).
- **Supersonic plates**: on the Mach 2.25 DNS of Pirozzoli et al. the
  onset error is 6.96% and the $C_f$ error 10.91%; without the
  compressibility correction of the correlation they are 32.40% and
  39.70%, and without both corrections 46.78% and 64.42% (Fig. 23); on the
  Mach 3.5 plates of Chen et al. onset errors are 1.56%–4.23%, all models
  underestimating the transitional $C_f$ overshoot (Table IX).
- **Airfoils**: on the S809, NFL(1)-0416 and transonic NLR-7301 onset
  errors are mostly below 5%–10%, the largest being 28.12% (NFL upper side
  at high incidence) and 81.16% (NLR-7301 where the shock dominates
  transition) (Figs. 25, 27, 29). Large far-field elements produce negative
  $k_L$ or $k$; clipped to zero, a zero $k$ prevents triggering, and a
  plain $k$-$\ln\omega$ model is less sensitive to this (§V).

## Coupling to other host models

Liu et al. (2024, Introduction) describe the $k$-$k_L$-$\omega$ LKE model of
Walters & Cokljat as calibrated on a $k$-$\omega$ closure "with numerous trigger
functions and empirical coefficients", hard to couple to a
[Reynolds-stress model](/methods/reynolds-stress-model.md), and prefer
Menter's intermittency model for that purpose
([Liu et al. (2024)](/sources/liu-2024.md), Introduction). Pacciani et al.
couple their model to Wilcox $k$-$\omega$ as well: on T3A it gives the same
onset as with SST, a quicker transition and a different turbulent $C_f$, so
the constants "should be retouched" per host model; with Wilcox's model the
LS89 leading-edge heat transfer stayed below the measurements (§5.1.1,
Fig. 5, §6.1). Morsbach et al. (2024), whose SST and Reynolds-stress RANS
with $\gamma$-$Re_\theta$ miss the separation-induced transition of a
low-pressure turbine at midspan, suggest that tuned transition models or
LKE models may be needed ([Morsbach et al. (2024)](/sources/morsbach-2024.md),
§5).

## Data-driven corrections

Sandberg & Zhao (2022) list the laminar-kinetic-energy line (Mayle &
Schulz 1997; Pacciani & Marconcini 2011, cited) among the transport
models a machine-learnt transition closure can build on, and review one
such correction: CFD-driven, multi-expression and multi-objective
gene-expression training of corrections to a laminar-kinetic-energy model
for low-pressure turbines, with non-dimensional $\Pi$-group features
(Akolekar et al. 2021), in which every candidate model is run in RANS and
scored on the mean flow ([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md),
§3.4, §4.3; see [model-consistent training](/methods/model-consistent-training.md)
and [symbolic-regression closures](/methods/symbolic-regression-closure.md)).
Their verdict on data-driven transition modelling as a whole is that it
is "still far from mature" (§4.3); the field-inversion corrections of
intermittency models they cite are on the
[correlation-based page](/methods/local-correlation-based-transition-model.md).

## Qualifications

- Pacciani et al. print $f_{\mu,L}=1-e^{R_T^{2.5}}$ with a positive exponent
  in both Eq. 19 and Eq. A13. For $R_T>0$ this is negative and unbounded,
  which contradicts the text's description of a damping function that keeps
  $\mu_L$ out of the viscous sublayer *(compiler check, not in the
  sources)*; the form is therefore left unwritten above.
- Their Appendix Eq. A2 writes the untilded $P_k$, $D_k$ in the $k$-equation,
  while Eq. A11 defines the intermittency-modified terms and Eq. 16 uses
  them; the equation above follows Eqs. 16 and 18.
- $f_{PG}$ and Thwaites' parameter as printed are dimensionless only if $p$
  is the kinematic pressure *(compiler check, not in the sources)*.
- "Turbulent Reynolds number" names both $k/(\nu\omega)$ (§3.1, §4.3) and the
  viscosity ratio $\nu_t/\nu$ (§5.1).
- Ghidoni & Noventa (2026) print the first branch of Eq. 27 as
  "$1173.51\ 589.428Tu+0.2196/Tu^2$", without the operator; the form above
  takes the minus sign that Vandenhoeck et al. (2022) print for the same
  Langtry–Menter correlation, whose PGC function they also print in the
  same form ([Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md),
  §1.2, Eqs. 33–34) *(compiler check, not in the sources)*.
- Ghidoni & Noventa list in Table I a constant $C_k=1000$ that no equation
  uses, while $C_{TS,\mathrm{crit}}$ of their Eq. 11 has no value; they give
  T3A $Tu_\infty=3.3\%$ in Table II and 2.3% in §IV A; their Table VII
  (Blair B6–B15) prints $(\mu_t/\mu)_\infty=1.2$ for every case and
  $Tu_\infty$ = 2, 8, 34, 67 and 100%, the values of the $(\mu_t/\mu)_\infty$
  row of their Table VI (B1–B5); and the B7 and B13 errors "without" the
  pressure-gradient correction repeat the values with it.
- Their onset errors do not all follow one formula: the relative
  difference of the printed $Re_{x,tr}$ reproduces Tables IV and IX and
  the T3A and T3B values (within the rounding of the printed $Re_{x,tr}$),
  but gives 9.7% for Schubauer–Klebanoff (printed 8.34%) and 2.6% for
  Blair B1 (1.66%) *(compiler check, not in the sources)*.
- The log-$\omega$ notation of Ghidoni & Noventa writes $\tilde\omega$ in
  $D_k$ and in the $\omega$-equation sources (Eqs. 13–15) where elsewhere
  $\omega$ is recovered as $e^{\tilde\omega}$, and shows no extra term from
  the logarithmic transformation; the structure above writes $\omega$.
- The S809 statements here and the natural-transition onset at
  $6^\circ$–$7^\circ$ against about $5^\circ$ measured that Menter et al.
  (2022) report for their intermittency models (see
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md))
  use different metrics and models; they are not compared on this page.

# Citations

- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §1, §2, §3.1–3.2 Eqs. 1–9 Fig. 1, §4.1–4.5 Eqs. 10–27, §5.1 Figs. 2–13 Tables 2–3 Eqs. 28–29, §6.1–6.3 Figs. 15–25, §7, App. A Eqs. A2, A11, A13, A14.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §5.
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — §I, §II Eqs. 1–27, §III Eqs. 28–33, §IV A–C Tables I–IX Figs. 4–23, Eq. 34, §V Figs. 25–29, Appendix.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — §1.2, Eqs. 33–34.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §3.3.3.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.4, §4.3.
