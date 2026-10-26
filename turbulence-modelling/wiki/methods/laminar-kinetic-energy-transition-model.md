---
type: Method
title: "Laminar kinetic energy transition models"
description: "RANS transition closures that transport the energy of pre-transitional laminar fluctuations and transfer it to the turbulent kinetic energy at transition; the concept and lineage, the multi-mode reformulation of Pacciani et al. coupled to SST with its production, intermittency, pressure-gradient and separation terms and constants, and its validation on flat plates, turbine cascades and an airfoil."
status: established
aliases: [LKE model, laminar kinetic energy model, k-kL-ω, k-kl-ω, three-equation transition model, LKE-SST]
tags: [rans, transition, eddy-viscosity, turbomachinery, separated-flow, boundary-layer]
timestamp: 2026-10-26T10:25:00Z
---

# Laminar kinetic energy transition models

A laminar-kinetic-energy (LKE) model adds to a two-equation RANS closure a
transport equation for $k_\ell$ (page-local), the kinetic energy of the
non-turbulent fluctuations that grow in a laminar boundary layer before
transition (Klebanoff streaks, Tollmien–Schlichting waves). Transition is
modelled as a transfer term $\mathcal R$ (page-local) that moves energy
from $k_\ell$ to the turbulent kinetic energy $k$, leaving the total
fluctuation energy $k_\ell+k$ unchanged. As recalled by Pacciani et al.
(2025), the concept goes back to Mayle & Schulz (1997) and was used for
transition-sensitive closures by Walters & Leylek (2004), Walters &
Cokljat (2008) and Lardeau et al. (2007); a variant of Lopez & Walters
(2016) replaces $k_\ell$ by the wall-normal fluctuation energy
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

$$\frac{Dk_\ell}{Dt}=P_\ell-\mathcal R-D_\ell+\partial_j(\nu\,\partial_jk_\ell),\qquad D_\ell=2\nu\frac{k_\ell}{d^2},\qquad P_\ell=c_1\ell_s\sqrt{k_\ell}\,\lvert S\rvert^2,$$

with the Mayle–Schulz dissipation $D_\ell$, a production after Lardeau et
al. whose length $\ell_s$ (page-local) is the vorticity thickness of the
separated shear layer, a non-local quantity meant to model
Kelvin–Helmholtz growth, and the transfer, after Walters & Leylek,

$$\mathcal R=c_3f_tk_\ell\omega,\qquad f_t=1-e^{-\psi/c_4},\qquad \psi=\max\Big(\frac{\sqrt k\,d}{\nu}-c_5,0\Big),$$

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

## The multi-mode reformulation

Pacciani et al. (2025) rebuild the model as a "base framework" whose few
closure functions are candidates for gene-expression-programming training
(§1, §4). The changes, all built on local quantities:

**Production with a local length scale and the large-scale turbulence.**
With $U$ the local velocity magnitude (page-local) and the shear-sheltering
split of Jacobs & Durbin and Walters & Cokljat,

$$f_{SS}=e^{-(c_{SS}\nu\lvert\Omega\rvert/k)^2},\quad k_{T,s}=f_{SS}k,\quad k_{T,l}=k-k_{T,s},\quad c_{SS}=2,$$

$$P_\ell=c_1\Big(\frac{\lvert\Omega\rvert d^2}{U}\Big)\lvert S\rvert^2\sqrt{k_{T,l}}$$

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

$$\gamma=\frac{k_{T,s}}{k_\ell+k_{T,s}},$$

which multiplies the [SST](/methods/k-omega-sst-model.md) production as in
intermittency models (Eqs. 14–18):

$$\begin{aligned}
\frac{Dk_\ell}{Dt}&=(1-\gamma)P_\ell-\mathcal R-D_\ell+\partial_j(\nu\,\partial_jk_\ell),\\
\frac{Dk}{Dt}&=\gamma P_k+\mathcal R-\max(\gamma,0.1)\,\beta^*k\omega+\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_k}\Big)\partial_jk\Big],
\end{aligned}$$

with the $\omega$-equation and the eddy viscosity of standard SST (limiter
$\mu_t=\rho a_1k/\max(a_1\omega,F_2\lvert S\rvert)$, App. A Eq. A14). The
factor $(1-\gamma)$ drives $k_\ell$ and $\mathcal R$ to zero after transition:
$\mathcal R$ controls the onset, and once turbulent production starts the
intermittency controls the gradual rise of $k$ (§4.2). Using $k_{T,s}$
rather than $k$ in $\gamma$ avoids $\gamma\to1$ in accelerating laminar
layers where $k_\ell$ is smaller than the free-stream $k$ diffused into the
layer (§4.2). This $\gamma$ is algebraic and differs in definition from
the transported or algebraic intermittencies of the local-correlation
models. The authors state that the coupling works with any two-equation
model (§4.2).

**Laminar fluctuation diffusivity.** A viscosity
$\mu_\ell=c_{\mu,\ell}f_{\mu,\ell}\,\rho\,(\lvert\Omega\rvert d^2/U)\sqrt{k_\ell}$
(page-local), with a function $f_{\mu,\ell}$ of $R_T$ meant to keep it out of
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

$$P_\ell=c_1\Big(\frac{\lvert\Omega\rvert d^2}{U}\Big)\lvert S\rvert^2\sqrt{k_{T,l}}+f_{sep}P_{sep},\qquad P_{sep}=\max(c_{sep}\mu-\mu_t,0)\lvert S\rvert^2,\qquad \mathcal R=c_3(f_t+3c_{sep}f_{sep})k_\ell\omega,$$

$$f_{sep}=1-\exp\Big[-\max\Big(\frac{Re_v}{R_{cr}}-1,0\Big)\Big],\quad Re_v=\frac{\lvert S\rvert d^2}{\nu},\quad R_{cr}=800\max[\min(2r,8),1],\quad r=\frac{\lvert S\rvert d}{U}$$

(page-local symbols; the source calls $Re_v$ the vorticity Reynolds number
although it is built on the strain). $P_{sep}$ is borrowed from Menter et
al. (2015); its $\max(c_{sep}\mu-\mu_t,0)$ form is "self-destructing" in
turbulent flow and prevents spurious growth in wakes. The boosted transfer
targets the overlong bubbles that a delayed turbulence-model response
produces in many closures (§4.5); $f_{sep}$ "has no ambition of generality"
and is a training candidate.

**Constants.** Calibrated on the ERCOFTAC T3 plates (Table 2):

| $c_1$ | $c_3$ | $c_4$ | $c_5$ | $c_{\mu,\ell}$ | $c_{sep}$ | $c_{SS}$ |
|---|---|---|---|---|---|---|
| 0.02 | 0.02 | 8 | 24 | 0.03 | 10 | 2 |

$k_\ell=0$ at the inlet and on walls (App. A). The model uses local
quantities only but is not Galilean invariant, through $U$ in its length
scale and through $f_{PG}$ (§4.1, §4.4).

## Calibration and validation

All runs are steady two-dimensional RANS in the in-house TRAF code
(density-based, artificial compressibility for incompressible cases, a
formally third-order TVD scheme on Roe's flux) (§2).

**Flat plates.** On the [ERCOFTAC T3 plates](/benchmarks/ercoftac-t3-flat-plate.md)
(T3A, T3B, T3A–, Schubauer–Klebanoff, T3C1–T3C5; $288\times128$ cells, the
plate leading edge excluded):

- $c_1$ and $c_5$ compete: a larger $c_1$ raises $k_\ell$ and smooths the
  rise of $\gamma$, so $c_5$ must decrease to keep the onset; $c_1=0.02$
  with $c_5=24$ matches the T3A total fluctuation profiles up to
  $Re_x\simeq2.0\times10^5$ (§5.1.1, Figs. 2–3);
- lower $c_3$ does not start transition reliably and higher values make it
  too rapid; $c_{\mu,\ell}$ barely acts at zero and adverse pressure gradient
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

## Coupling to other host models

Liu et al. (2024) recall the $k$-$k_L$-$\omega$ LKE model of Walters &
Cokljat as calibrated on a $k$-$\omega$ closure "with numerous trigger
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

## Qualifications

- Pacciani et al. print $f_{\mu,\ell}=1-e^{R_T^{2.5}}$ with a positive exponent
  in both Eq. 19 and Eq. A13. For $R_T>0$ this is negative and unbounded,
  which contradicts the text's description of a damping function that keeps
  $\mu_\ell$ out of the viscous sublayer *(compiler check, not in the
  sources)*; the form is therefore left unwritten above.
- Their Appendix Eq. A2 writes the untilded $P_k$, $D_k$ in the $k$-equation,
  while Eq. A11 defines the intermittency-modified terms and Eq. 16 uses
  them; the equation above follows Eqs. 16 and 18.
- $f_{PG}$ and Thwaites' parameter as printed are dimensionless only if $p$
  is the kinematic pressure *(compiler check, not in the sources)*.
- "Turbulent Reynolds number" names both $k/(\nu\omega)$ (§3.1, §4.3) and the
  viscosity ratio $\nu_t/\nu$ (§5.1).
- The S809 statements here and the natural-transition onset at
  $6^\circ$–$7^\circ$ against about $5^\circ$ measured that Menter et al.
  (2022) report for their intermittency models (see
  [local-correlation-based transition models](/methods/local-correlation-based-transition-model.md))
  use different metrics and models; they are not compared on this page.

# Citations

- [Pacciani et al. (2025)](/sources/pacciani-2025.md) — §1, §2, §3.1–3.2 Eqs. 1–9 Fig. 1, §4.1–4.5 Eqs. 10–27, §5.1 Figs. 2–13 Tables 2–3 Eqs. 28–29, §6.1–6.3 Figs. 15–25, §7, App. A Eqs. A2, A11, A13, A14.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §5.
