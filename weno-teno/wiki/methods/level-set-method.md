---
type: Method
title: "Level-set and ghost-fluid interface methods"
description: "Interface methods that locate a material interface by the zero contour of a signed-distance level-set function: its transport and reinitialization, the ghost-fluid family and its loss of conservation, a conservative sharp-interface finite-difference scheme with cell merging and flux blending, and the coupling of a level set with a conservative phase field."
status: established
aliases: [level set, level-set function, ghost fluid method, GFM, sharp-interface method, conservative sharp-interface scheme]
tags: [interface-capturing, multiphase, finite-difference, weno, limiting]
timestamp: 2026-10-22T12:00:00Z
---

# Level-set and ghost-fluid interface methods

A level-set method represents a material interface as the zero contour
of a function $\Phi(x,t)$ (page-local symbol), kept close to the signed
distance from the interface ($\lvert\nabla\Phi\rvert=1$), negative in
one fluid and positive in the other. The function is transported with
the interface and periodically reinitialized to a distance function;
it supplies the interface position, its normal $\nabla\Phi/\lvert\nabla\Phi\rvert$
and its curvature. In this bundle it appears in two roles: as the
interface tracker of a sharp-interface, two-fluid, conservative
finite-difference scheme for compressible gas–gas and gas–water flows
([Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md)), and as the
geometric companion of a mass-conserving phase field in a weakly
compressible gas–liquid solver
([Matsushita & Aoki (2021)](/sources/matsushita-2021.md)). The
alternative, capturing the interface as a diffuse mixture region, is
the [five-equation model](/definitions/five-equation-model.md).

## Transport and reinitialization

**Transport.** Zheng et al. evolve $\Phi$ by the normal-speed form
$\partial_t\Phi+V_n\lvert\nabla\Phi\rvert=0$, with the normal speed
$V_n$ obtained from interface Riemann problems and extended off the
interface by $\partial_\tau q+\mathrm{sign}(\Phi)\frac{\nabla\Phi}{\lvert\nabla\Phi\rvert}\cdot\nabla q=0$
in pseudo-time $\tau$. They discretize it with a Godunov-type
Hamiltonian and one-sided WENO approximations of
$\partial_x\Phi$ (and $\partial_y\Phi$) after Jiang & Peng, with
$\Phi$ stored at half nodes (1D) or cell corners (2D) (§2.2, Eqs.
21–22; §3, Eqs. 41–42). Matsushita & Aoki advect
$\partial_t\Phi=-v\cdot\nabla\Phi$ with third-order Hamilton–Jacobi WENO
every step (Eq. 16).

**Reinitialization.** Both sources restore the distance property by
solving to pseudo-steady state

$$
\partial_\tau\Phi+S(\Phi)\big(\lvert\nabla\Phi\rvert-1\big)=0,
$$

with $S$ a sign function: $\mathrm{sign}(\Phi_0)$ of the initial
contour, with TVD Runge–Kutta in pseudo-time, $\Delta\tau=0.1\min(\Delta x,\Delta y)$,
every 100 steps in 2D (Zheng et al. §3.1.5); or the smoothed sign
$S(\Phi)=\Phi/\sqrt{\Phi^2+\lvert\nabla\Phi\rvert^2\Delta x^2}$ with 20
iterations every several dozen steps (Matsushita & Aoki §2.2, Eq. 15).

**Geometry.** Zheng et al. cut each cell by the straight segment
between the zero crossings of $\Phi$ on its edges and compute the
volume fraction of each fluid in five generic configurations (§3.1.1).
Matsushita & Aoki compute the curvature (page-local symbol)
$\kappa_{\mathrm c}=-\nabla\cdot(\nabla\Phi/\lvert\nabla\Phi\rvert)$ for a
density-scaled continuum surface force (Eqs. 19–20), and detect where
the level set has lost its distance property in thin films by the
quality (page-local) $Q=\lvert1-\lvert\nabla\Phi\rvert\rvert$: where $Q>0.05$ the
curvature is replaced by that of the face neighbour with smallest $Q$
(§3.4, Eqs. 39–41). They also use $\Phi$ to drive interface-adapted
mesh refinement: a tree leaf is refined when its smallest
$\lvert\Phi\rvert$ is below the diagonal length of its children
(§3.5, Eq. 47).

## Ghost-fluid methods and conservation

Zheng et al. group the ghost-fluid method (GFM) with its isobaric fix,
the modified GFM, the real GFM, interface-treatment methods and
path-conservative schemes as interface *tracking* methods that are not
conservative, "so convergence to weak solutions is not assured" (the
motivation is the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md));
conservative schemes, conversely, "tend to give oscillatory results if
no special care is taken" (§1). On a strong shock hitting a gas–gas
interface ($(\rho,v,p,\gamma)=(0.3856,27.0784,100,5/3)$ against
$(1,0,1,1.4)$), a finite-difference WENO-based original GFM places the
shock front and the interface wrongly, while their conservative scheme
does not (§4, Ex. 4, Fig. 8). They also argue against diffuse-interface
capturing, whose smeared interface carries mixture states
"inconsistent with what is really happening in physics" (§1).

## A conservative sharp-interface finite-difference scheme

Zheng et al. build a fifth-order conservative scheme in which each fluid
keeps its own nodal values and the level set says which fluid a node
belongs to (§2–3):

1. **Computational variable.** Away from the interface it is the nodal
   value of the local fluid; in the interface cell it is the
   volume-weighted combination of the two fluids' values. It is updated
   by one conservative flux difference per stage
   ([conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)).
2. **High-order flux.** The [alternative WENO](/methods/alternative-weno.md)
   flux: a Lax–Friedrichs flux on WENO-interpolated left and right
   states plus the central corrections in $\Delta x^2\partial_x^2f$ and
   $\Delta x^4\partial_x^4f$. The WENO interpolation acts on the
   primitive variables $(\rho,v,p)$ in the local characteristic fields
   of the primitive quasilinear system (see
   [characteristic decomposition](/methods/characteristic-decomposition.md)),
   with stencils that take the nodal values of the fluid in which the
   flux is evaluated.
3. **Cell merging and a low-order interface flux.** Near the interface
   two cells are merged so that no fluid occupies a small cut cell. On
   each fluid's part of the merged stencil a low-order flux comes from
   an ALE-type space–time integral whose interface contribution is the
   flux $(0,p,vp)$ of an interface Riemann problem (in 2D with the
   interface normal); the first component vanishes, so each fluid's mass
   is conserved (Eqs. 7–14; 2D Eqs. 32–36).
4. **Blending by a discontinuity indicator.** With a smooth indicator
   $\varphi_{\mathrm D}\in[0,1]$ (page-local symbol), the flux near the
   interface is $\hat f^{\mathrm L}+\varphi_{\mathrm D}(\hat f^{\mathrm H}-\hat f^{\mathrm L})$,
   $\varphi_{\mathrm D}$ also multiplies the central corrections of the
   high-order flux, and the updated mixed-cell value is redistributed to
   the two fluids with the same weight (Eqs. 6, 15–20). The indicator is
   built like a WENO-Z global indicator from Jiang–Shu
   [smoothness indicators](/definitions/smoothness-indicator.md) of a
   six-point quintic and four three-point quadratics on $[x_i,x_{i+1}]$:
   $\tau$ is the mean squared difference between the large-stencil
   indicator and each small one, and
   $\varphi_{\mathrm D}=\big(1+\tfrac14\sum_k\tau/(\beta_k+\epsilon)\big)^{-2}$.
   Zheng et al. prove $\varphi_{\mathrm D}=1+O(\Delta x^6)$ on smooth
   data and $\varphi_{\mathrm D}=O(\Delta x^4)$ when the large stencil
   contains a discontinuity (Appendix B); see
   [troubled-cell indicators](/definitions/troubled-cell-indicator.md).
5. **Accuracy budget.** Propositions 2.1–2.3 show that the blended
   scheme keeps fifth order if $\varphi_{\mathrm D}=1+O(\Delta x^5)$ and
   $\Delta t=O(\Delta x^m)$ with $m\le2$ ($m$ page-local), because the
   low-order interface flux is recovered by dividing an update by
   $\Delta t/\Delta x$ and is only $O(\Delta x^{2-m})$ accurate.

Evidence (§4): fifth order on Burgers-reducible artificial-interface
tests in 1D ($L_1$ density error $1.05\times10^{-5}$ to
$1.07\times10^{-8}$ for $N_x=80$ to $320$, final rate 5.14) and 2D
(final rate 5.06), sixth-order convergence of the indicator itself
(rate 5.98); on a 1D moving contact the velocity and pressure deviations
are about $10^{-11}$–$10^{-10}$, against about $10^{-4}$–$10^{-3}$ for
a conservative-variable WENO-JS scheme, and round-off on a 2D pure
interface; on gas–water Riemann problems WENO-JS produces a spurious
jump at the interface where the new scheme does not (see
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)).
Stages of the third-order SSP Runge–Kutta method are assembled from
$t^n$ with accumulated fluxes, so that the final update is a single
conservative flux difference (§2.2.5–2.2.6).

## Level set coupled with a conservative phase field

Matsushita & Aoki capture the interface by the conservative phase-field
(conservative Allen–Cahn) equation of Chiu & Lin for the liquid volume
fraction $\phi_{\mathrm l}\in[0,1]$ (page-local), solved in finite-volume
flux form so that total mass is conserved, and use the level set only
for geometry (§2.2, Eqs. 9–14):

$$
\partial_t\phi_{\mathrm l}+\nabla\cdot(v\phi_{\mathrm l})
=\delta_b\,M_{\mathrm{pf}}\Big\{\ell\,\nabla\cdot\nabla\phi_{\mathrm l}
-\nabla\cdot\Big[\phi_{\mathrm l}(1-\phi_{\mathrm l})\frac{\nabla\Phi}{\lvert\nabla\Phi\rvert}\Big]\Big\},
$$

with mobility $M_{\mathrm{pf}}$, interface-width parameter $\ell$ and a
band indicator $\delta_b=1$ for $\lvert\Phi\rvert<5\delta$, $0$
otherwise, $\delta=3\Delta x$ the interface thickness (page-local
symbols). Replacing the phase-field normal by the level-set normal
improves the geometry and reduces the compression of $\phi_{\mathrm l}$
by the weakly compressible velocity field. The level set is rebuilt
from the phase field before each reinitialization by inverting the
equilibrium profile $\phi_{\mathrm l}=\tfrac12\big(1+\tanh(\Phi/(2\ell))\big)$,
i.e. $\Phi=\ell\ln\big(\phi_{\mathrm l}/(1-\phi_{\mathrm l})\big)$
(Eqs. 10, 14). The advective flux uses third-order MUSCL with minmod.
The total-mass error is $O(10^{-16})$ on uniform and adaptive grids,
while the volume of each phase is not conserved (gas-area error within
1.5 % in the text, see Qualifications); on the Rider–Kothe single-vortex
test the interface error converges at roughly second order (rates
2.06, 1.40, 2.29, 2.04 on $32^2$ to $512^2$; Appendix 8.4, Table 4).

## Qualifications

- The two sources solve different problems. Zheng et al. solve the
  compressible Euler equations with physical equations of state and a
  sharp interface; Matsushita & Aoki solve a weakly compressible,
  isothermal model of low-Mach gas–liquid flow, $\partial_tp=-\rho c_{\mathrm a}^2\nabla\cdot v$
  with an artificial sound speed $c_{\mathrm a}$ equal in both phases
  (page-local), whose solutions converge to incompressible ones at
  about second order in the Mach number (§2.1; Appendix 8.3). Their
  level set does not enter any compressible-flow flux.
- Zheng et al.'s indicator proof assumes that the
  [smoothness indicators](/definitions/smoothness-indicator.md) are
  $O(\Delta x^2)$, i.e. a non-vanishing first derivative, and does not
  discuss critical points or the value of $\epsilon$ in the indicator,
  which the paper does not print (only $\epsilon=10^{-6}$ for the WENO
  weights); see [accuracy at critical points](/properties/critical-point-accuracy.md).
- The accuracy budget ties the interface flux to the time step: the
  middle interface flux is $O(\Delta x^{2-m})$ accurate (Appendix A),
  so time steps smaller than $O(\Delta x^2)$ degrade it; the accuracy
  tests use $\Delta t=O(\Delta x^{5/3})$.
- Zheng et al. print the reinitialization stopping rule as
  "$e_1<\Delta\tau\Delta x\Delta y$ or $k\le20$", which as a stopping
  rule is inverted (an iteration cap would read $k\ge20$; *compiler
  check, not in the sources*), and in Appendix A reuse the volume-fraction symbol for
  interface lengths.
- Matsushita & Aoki state that the gas-area error of their rising-bubble
  Case B stays "within 1.5%", while their Fig. 37 spans at most
  0.16 %; the text and the figure disagree by a factor of about ten.
- The scheme of Zheng et al. is conservative for the computational
  variable and for each fluid's mass; momentum in Matsushita & Aoki's
  non-conservative velocity form is "not exactly satisfied" (§3.1).

# Citations

- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §1; §2.1–2.3, Eqs. (1)–(27); §3, Eqs. (28)–(42); §4, Ex. 1–11, Tables 2–4, Figs. 6, 8, 11–15; Appendices A–B.
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §2.1–2.2, Eqs. (8)–(20); §3.2, §3.4–3.5, Eqs. (32)–(35), (39)–(41), (47); §5.1; Appendices 8.1, 8.3, 8.4.
