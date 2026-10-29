---
type: Method
title: "Lagrangian relaxation towards equilibrium (LaRTE) wall model"
description: "A wall-stress model that transports the friction-velocity vector along wall trajectories and relaxes it towards the equilibrium stress with the inertial time of the fluid layer below the matching height, optionally adding a laminar Stokes-layer stress driven by fast pressure-gradient fluctuations."
status: established
aliases: [LaRTE, LaRTE wall model, relaxation-towards-equilibrium wall model, quasi-equilibrium wall model]
tags: [wall-model, wmles, boundary-layer]
timestamp: 2026-10-29T10:04:00Z
---

# Lagrangian relaxation towards equilibrium (LaRTE) wall model

The LaRTE model of [Fowler et al. (2022)](/sources/fowler-2022.md) is a
wall-stress model for [wall-modelled LES](/methods/wall-modelled-les.md) in
which the friction-velocity vector $\boldsymbol u_\tau(x,z,t)$ on the wall is a
prognostic field, governed by a two-dimensional transport equation. Along
wall trajectories it relaxes towards the total forcing of the layer between
the wall and the matching height $h_{\mathrm{wm}}$ (stress at $h_{\mathrm{wm}}$
plus pressure-gradient force), with a relaxation time equal to the inertia of
that layer. The classical [equilibrium wall model](/methods/equilibrium-wall-model.md)
is its limit of zero relaxation time. A second, separate component models the
fast, laminar Stokes-layer response of the viscous sublayer to pressure-gradient
fluctuations. Throughout, stresses are kinematic (divided by $\rho$) and the
flow is incompressible over smooth planar walls.

## Quasi-equilibrium ansatz

Following Chung & Pullin (2009) and the integral wall model of Yang et al.
(2015), as Fowler et al. cite them, the wall-parallel velocity of the layer
$0\le y\le h_{\mathrm{wm}}$, filtered horizontally at the LES scale and
implicitly in time, is written as (Eq. 2.1)

$$\boldsymbol u_s(x,y,z,t)=\boldsymbol u_\tau(x,z,t)\,f(y^+),\qquad y^+=\frac{yu_\tau}{\nu},\qquad \boldsymbol\tau_w=u_\tau\boldsymbol u_\tau ,$$

with $f$ the [law of the wall](/definitions/law-of-the-wall.md), $u_\tau=|\boldsymbol u_\tau|$
and $\boldsymbol s=\boldsymbol u_\tau/u_\tau$ the stress direction (page-local
symbols $\boldsymbol u_s$, $f$, $\boldsymbol s$). The slow time scale implied by
the filter is not prescribed; it emerges from the derivation.

## Derivation and the LaRTE equation

The ansatz is substituted in the wall-parallel unsteady RANS
(thin-boundary-layer) momentum equation with eddy viscosity $\nu_t$ and a
pressure independent of $y$, and the equation is integrated from the wall to
$h_{\mathrm{wm}}$ (§2, App. A). Two integral lengths appear, the cell
displacement and momentum thicknesses (Eqs. 2.8, 2.13; page-local)

$$\delta^*_h=\int_0^{h_{\mathrm{wm}}}\left(1-\frac{f(y^+)}{f(h^+_{\mathrm{wm}})}\right)dy,\qquad \theta_h=\int_0^{h_{\mathrm{wm}}}\frac{f(y^+)}{f(h^+_{\mathrm{wm}})}\left(1-\frac{f(y^+)}{f(h^+_{\mathrm{wm}})}\right)dy .$$

The time derivative yields $\partial\boldsymbol u_\tau/\partial t$ by the chain
rule; after continuity, the horizontal and vertical advection terms combine
into an advection of $\boldsymbol u_\tau$ (the $\partial u_\tau/\partial s$
parts cancel exactly, App. A). The result is the LaRTE equation (Eq. 2.14)

$$\frac{\partial\boldsymbol u_\tau}{\partial t}+\boldsymbol V_\tau\cdot\nabla_h\boldsymbol u_\tau=\frac1{T_s}\left[\frac1{u_\tau}\left(-h_{\mathrm{wm}}\nabla_hp+\boldsymbol\tau_h\right)-\boldsymbol u_\tau\right]+u_\tau\frac{\delta^*_h}{h_{\mathrm{wm}}}\frac{\partial\boldsymbol s}{\partial t}+\frac{\nabla_h\cdot\boldsymbol D_\tau}{h_{\mathrm{wm}}f(h^+_{\mathrm{wm}})},$$

with $p$ the kinematic pressure, $\boldsymbol\tau_h=(\nu+\nu_t)\partial\boldsymbol u_s/\partial y$
the total stress at $h_{\mathrm{wm}}$, $\boldsymbol D_\tau$ a wall-normal-integrated
horizontal diffusive flux (App. B, neglected in all simulations), and

$$T_s=f(h^+_{\mathrm{wm}})\,\frac{h_{\mathrm{wm}}}{u_\tau},\qquad \boldsymbol V_\tau=\left(1-\frac{\delta^*_h}{h_{\mathrm{wm}}}-\frac{\theta_h}{h_{\mathrm{wm}}}\right)f(h^+_{\mathrm{wm}})\,\boldsymbol u_\tau$$

(Eqs. 2.15, 2.12; page-local $T_s$, $\boldsymbol V_\tau$, $\nabla_h$ the
wall-parallel gradient). The authors state the derivation "does not require
additional ad hoc assumptions" beyond the ansatz.

**Meaning of $T_s$.** Fowler et al. (§2.1) state that $T_s$ is proportional
to the fluid volume per unit wall area below $h_{\mathrm{wm}}$, that is, the
inertia of the layer: it delays the
wall stress behind the stress at $h_{\mathrm{wm}}$; a higher matching point
lengthens the delay and a larger $u_\tau$ shortens it (§2.1). For one stress
component without pressure gradient the wall stress itself relaxes with time
$T_s/2$, $d_s\tau_{wx}/dt=(2/T_s)(\tau_{hx}-\tau_{wx})$ with
$d_s/dt=\partial_t+\boldsymbol V_\tau\cdot\nabla_h$ (Eq. 2.18), and Fowler et
al. identify $T_s/2$ with the time scale of Chung & Pullin (2009).

**Equilibrium limit.** For $T_s\to0$ the bracket must vanish: the wall stress
equals the total forcing at $h_{\mathrm{wm}}$, which is the equilibrium wall
model, justified only under full time-scale separation (§2.2).

## Closure of the forcing

The authors place the closure at $h_{\mathrm{wm}}$, where the LES velocity is
known, not at the wall. The forcing is the full-equilibrium fit of Meneveau
(2020) aligned with the LES velocity (Eqs. 2.19–2.21):
$\boldsymbol\tau_h-h_{\mathrm{wm}}\nabla_hP=(Re^{\mathrm{pres}}_{\tau h}\nu/h_{\mathrm{wm}})^2\hat{\boldsymbol e}_u$,
where $Re^{\mathrm{pres}}_{\tau h}$ is the fitted
$\langle u_\tau\rangle h_{\mathrm{wm}}/\nu$ (page-local) and $P$ the slow
(equilibrium) part of the pressure. The function $f$ and the thicknesses are
evaluated from fits with errors below 1 % ($f$, for $y^+>5$) and 0.5 %
($\delta^*_h$, $\theta_h$, over $10^{-1}\le h^+_{\mathrm{wm}}\le10^5$); the
cell shape factor tends to 3 for a linear profile (App. C).

## Time-scale split of the pressure gradient

The LES pressure gradient at $h_{\mathrm{wm}}$ is split by one-sided
exponential time filters $\langle\cdot\rangle_T$ (filter of time scale $T$,
page-local) into three bands (§4.1, Eqs. 4.1–4.5):

- equilibrium, $\nabla_hP=\nabla_h\langle p\rangle_{3T_s}$, the input of the
  equilibrium fit (results "appear to be quite insensitive" to the factor 3);
- band-pass, $\nabla_h\langle p\rangle_{t_\nu}-\nabla_h\langle p\rangle_{3T_s}$,
  the pressure term of the LaRTE equation;
- high-pass, $\nabla_hp-\nabla_h\langle p\rangle_{t_\nu}$, the input of the
  laminar model, with $t_\nu=(l_s^+)^2\nu/u_\tau^2$, $l_s^+\approx12$
  (page-local).

The band between $t_\nu$ and $T_s$ — the response of near-wall turbulence
above the viscous sublayer, as in turbulence scrambling or drag reduction by
spanwise wall oscillation — is not modelled (§4.1, §6).

## Laminar Stokes-layer (non-equilibrium) stress

The high-pass pressure gradient drives a laminar response of the viscous
sublayer, $\partial_t\boldsymbol u_l=-\nabla_hp''+\nu\partial^2_y\boldsymbol u_l$,
with no slip at the wall and zero initial perturbation (Eq. 3.1; page-local
$p''$ the high-pass pressure, $\boldsymbol u_l$ the laminar velocity). Its
solution is a generalized Stokes first problem, and the wall stress is the
convolution (Eq. 3.5)

$$\boldsymbol\tau''_w(t)=\sqrt{\frac\nu\pi}\int_{t_0}^t\left(-\nabla_hp''\right)(t')\,(t-t')^{-1/2}\,dt' ,$$

a Caputo fractional derivative of order 1/2 of the free-stream velocity that
the high-pass gradient induces (Eqs. 3.6–3.7). It scales as $\nu^{1/2}$ and
"vanishes in the limit of infinite Reynolds number" (§5.1). The total wall
condition is $\boldsymbol\tau_w=u_\tau\boldsymbol u_\tau+\boldsymbol\tau''_w$.
The convolution is evaluated by the sum-of-exponentials method of Jiang et al.
(2017): with time step $4\times10^{-4}$, tolerance $10^{-9}$ and horizon 1, 48
exponentials suffice, with $O(N_{\exp})$ storage instead of the
$O(N_T)$ storage and $O(N_T^2)$ work of direct summation (§4.3); against the L1
method the root-mean difference normalized by $u_{\tau0}^2$ is below 0.021
(streamwise) and 0.011 (spanwise) (App. D).

## Discretization

Forward Euler with a semi-Lagrangian derivative: $\boldsymbol u_\tau$ at the new
time is the value at the upstream point $\boldsymbol x-\boldsymbol V_\tau\delta t$
plus $\delta t$ times the right-hand side there, with first-order bilinear
interpolation (Eqs. 4.6–4.7), following the Lagrangian dynamic SGS model of
Meneveau, Lund & Cabot (1996). The numerical diffusion of the low-order
interpolation stands in for the neglected horizontal diffusion (§4.2).

## Evidence

- **A priori** (§2.3, Fig. 2): on channel DNS at $Re_\tau=1000$ (Johns Hopkins
  database, horizontal Gaussian filter of $196$ wall units,
  $0\le y^+\le h^+_{\mathrm{wm}}\approx34$), exponential time filtering at $T_s$
  "almost completely collapses" the profiles onto the law of the wall when
  normalized by the local friction velocity; no filter, or a filter at
  $h_{\mathrm{wm}}/u_\tau$, does not.
- **Stationary channel** in [LESGO](/software/lesgo.md) (§5.1, Figs. 4–10):
  $Re_\tau=10^3$ to $5\times10^5$ on one $128\times30\times48$ grid,
  $h_{\mathrm{wm}}=\delta/30$. Mean profiles are "nearly indistinguishable" from
  the equilibrium model. The mean relaxation time is
  $T_su_\tau/\delta\approx0.45$ at $Re_\tau=1000$, and LaRTE filters out almost
  all $u_\tau$ fluctuations faster than $T_s$. The predicted wall-stress PDFs
  peak correctly but are much narrower than filtered DNS; the laminar part
  widens them, streamwise fluctuations stay under-predicted. The Lagrangian
  form gives less streamwise elongation of wall-stress structures than an
  Eulerian form, with the caveat that no reference distribution exists.
- **Sudden spanwise pressure gradient** (§5.2, Figs. 12–14): a channel at
  $Re_{\tau0}=1000$ subjected to a spanwise gradient ten times the streamwise
  one. For $0\le tu_{\tau0}/\delta\le0.05$ the spanwise wall stress follows the
  laminar Stokes-layer solution, carried by the non-equilibrium component, and
  LaRTE takes over later; the composite model agrees with DNS better than the
  equilibrium model, whose response is linear in time. Without the band-pass
  term the response lags by $O(T_s)$; without the high-pass term it misses the
  $\sqrt t$ trend. It misses the small initial dip of the streamwise stress (an
  error below 1–2 % of $u_{\tau0}$, attributed to a three-dimensional
  scrambling mechanism).

## Relation to other models

- Against the integral wall model of Yang et al. (2015), as Fowler et al.
  describe it: that model's time filter, about $h_{\mathrm{wm}}/(\kappa u_\tau)$,
  is shorter than $T_s$ by the factor $\kappa f(h^+_{\mathrm{wm}})$ and was
  tuned, while $T_s$ follows from momentum balance without tunable parameters
  (§2.1, §2.3); LaRTE also avoids that model's slope discontinuity in the buffer
  layer.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) (§I) cite Fowler et al.
  (2022), alongside the reviews of the field, for recent LES wall-modelling
  work; in the same code they list the integral, slip and
  POD-inspired wall models (§II.A). LaRTE is the relaxation-based member of the
  family surveyed on the [wall-modelled LES](/methods/wall-modelled-les.md) page.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§3) cite Fowler et al.
  (2022), with Yang et al. (2017), for the benefit of time-averaging the
  wall-model input, and adopt the simplest version of the idea: an
  exponential moving average of the sampled LES velocity with a fixed time
  constant of $0.0025\,\delta/u_\tau$, ahead of an algebraic
  [equilibrium wall model](/methods/equilibrium-wall-model.md). LaRTE's
  $T_s$, $T_su_\tau/\delta\approx0.45$ at $Re_\tau=1000$ in Fowler et al.'s
  channel, is about 180 times that constant *(compiler check, not in the
  sources)*. Gillyns et al. use their filter to keep the model from
  diverging (§5).
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) (§I) cite Fowler et al.
  (2022) twice: as evidence that the equilibrium model's "ability to
  accurately capture strong non-equilibrium effects in certain flow scenarios
  can be limited", and, with the integral, non-equilibrium and slip wall
  models, among recent models that "seek improvements by incorporating a
  lower level of simplifications". Their own route to the same deficiency is
  a learned model ([machine-learning wall models](/methods/machine-learning-wall-model.md)),
  which they test only in equilibrium channel flow; neither paper compares
  the two approaches.
- [Hu et al. (2024)](/sources/hu-2024.md) (§1) list Fowler et al. (2022) as
  the Lagrangian-relaxation entry of their taxonomy of wall-stress models,
  between the integral non-equilibrium model of Yang et al. and the dynamic
  slip conditions; their grid-convergence study uses only an algebraic
  [equilibrium wall model](/methods/equilibrium-wall-model.md) and does not
  test LaRTE.

## Qualifications

- Fowler et al. print Eq. (3.6) with a leading minus sign,
  $\boldsymbol\tau''_w=-\sqrt{\nu/\pi}\,\Gamma(1/2)D_t^{1/2}(\boldsymbol u''_\infty)$.
  With their Caputo definition (3.7) and their free-stream velocity (3.2),
  $\sqrt{\nu/\pi}\,\Gamma(1/2)D_t^{1/2}(\boldsymbol u''_\infty)$ equals the
  right-hand side of (3.5) with a plus sign, so the printed minus is
  inconsistent with (3.2), (3.5) and (3.7) *(compiler check, not in the
  sources)*.
- §4.2 writes $\boldsymbol u_\tau(x,y,t)$ for the $\boldsymbol u_\tau(x,z,t)$ of
  Eq. (2.1); §2.3 gives $h^+_{\mathrm{wm}}\approx34$ and Table 1 gives 33 for
  $Re_\tau=1000$.
- The sources of this bundle offer no second test of LaRTE; its evidence is
  that of its authors. Gillyns et al. (2022), Vadrot et al. (2023a) and
  Hu et al. (2024) cite it but do not implement it.

# Citations

- [Fowler et al. (2022)](/sources/fowler-2022.md) — §2, Eqs. (2.1)–(2.21); §3, Eqs. (3.1)–(3.7); §4, Eqs. (4.1)–(4.15); §5, Figs. 2–16; Apps. A–E.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I; §II.A.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §3, Eq. (4); §5.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §I (arXiv v3).
- [Hu et al. (2024)](/sources/hu-2024.md) — §1 (taxonomy of wall-stress models; passing mention).
