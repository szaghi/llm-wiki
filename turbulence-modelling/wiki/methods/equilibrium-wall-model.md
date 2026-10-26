---
type: Method
title: "Equilibrium wall model"
description: "The wall-stress model of wall-modelled LES that assumes a locally constant-stress, equilibrium inner layer: its ODE and algebraic forms, constants, matching heights, compressible extension, error propagation from LES input and model constants, cost, and the regimes where the sources show it fails."
status: established
aliases: [EQWM, EWM, wall-stress model, equilibrium wall-stress model, ODE wall model, algebraic wall model]
tags: [wall-model, wmles, boundary-layer, rans]
timestamp: 2026-10-26T07:39:00Z
---

# Equilibrium wall model

The equilibrium wall model replaces the no-slip condition of an LES by a
wall-stress boundary condition. The LES velocity $U_{\mathrm{LES}}$ sampled at a
matching height $h_{\mathrm{wm}}$ is the outer boundary condition of a
one-dimensional, steady model of the inner layer, and the wall shear stress
$\tau_w$ that this model returns is fed back to the LES as a Neumann-type
momentum flux. "Equilibrium" names the assumption that, below $h_{\mathrm{wm}}$,
convection, pressure gradient and time dependence balance or vanish, so the
total shear stress is constant across the layer. It is the baseline model of
every wall-modelled source of this bundle:
[Goc et al. (2021)](/sources/goc-2021.md),
[Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md),
[Agrawal et al. (2022)](/sources/agrawal-2022.md),
[Fowler et al. (2022)](/sources/fowler-2022.md),
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md),
[Griffin et al. (2023)](/sources/griffin-2023.md),
[Gillyns et al. (2022)](/sources/gillyns-2022.md) and
[Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md),
[Cai et al. (2022)](/sources/cai-2022.md) and
[Blind et al. (2023)](/sources/blind-2023.md), and the wall law of the
fan-stage WMLES of [Lewis et al. (2023)](/sources/lewis-2023.md); it is the comparison
baseline of the learned models of [Bae & Koumoutsakos (2022)](/sources/bae-2022.md)
and of the [building-block-flow wall model](/methods/building-block-flow-wall-model.md)
of [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md). It is the boundary
condition that defines [wall-modelled LES](/methods/wall-modelled-les.md).

## Assumptions

Goc et al. (2021, §2.2) state the assumptions explicitly: the thin-boundary-layer
equations hold; the pressure gradient and the streamwise convection balance
locally and drop out; and the LES resolution is coarse compared with viscous
scales, so the near-wall cell is statistically stationary. Momentum then
reduces to a constant-stress layer.

## Differential (ODE) form

With $y$ the wall-normal distance and $U(y)$ the wall-parallel mean velocity in
the inner layer (page-local),

$$\frac{d}{dy}\left[(\mu+\mu_t)\frac{dU}{dy}\right]=0,\qquad U(0)=0,\qquad U(h_{\mathrm{wm}})=U_{\mathrm{LES}},$$

and $\tau_w=\mu_w(dU/dy)_w$. The eddy viscosity is a Prandtl mixing length
with van Driest damping,

$$\mu_t=\kappa y\,\langle\rho\rangle\sqrt{\tau_w/\langle\rho\rangle}\,\left(1-e^{-y^+/A^+}\right)^2,$$

with $\kappa=0.41$, $A^+=17$ (Griffin et al. 2023, Eqs. 1.1–1.2, after Cabot &
Moin 2000 as they recall it). The problem is iterative because $\mu_t$ depends
on $\tau_w$. Goc et al. (2021, Eq. 2.6) write the same balance as
$d\big(\mu\,dU/dy-\langle\rho u''v''\rangle\big)/dy=0$ with the Reynolds shear
stress closed by a mixing-length eddy viscosity (constants not printed), and obtain the
wall heat flux $q_w$ from an analogous energy-equation approximation. Agrawal et
al. (2022, §VII.D) use the Cabot–Moin form, a boundary-value problem solved
for given matching height and LES velocity.

**Compressible extension.** For compressible flow with heat transfer the
momentum ODE is coupled with a total-energy ODE,

$$\frac{d}{dy}\left[(\mu+\mu_t)U\frac{dU}{dy}+c_p\left(\frac{\mu}{Pr}+\frac{\mu_t}{Pr_t}\right)\frac{dT}{dy}\right]=0,$$

with $Pr_t=0.9$, an ideal gas, a viscosity law and constant pressure across the
inner layer; the boundary conditions are the wall temperature and the matching
temperature (Griffin et al. 2023, Eq. 1.3, after Larsson et al. 2016 as they
recall it). Two coupled nonlinear boundary-value problems must then be iterated.
Hoy & Bermejo-Moreno (2022, §3) use the compressible equilibrium model of
Kawai & Larsson (2012), with a mixing-length eddy viscosity, solved on a
separate one-dimensional grid from the wall to $h_{\mathrm{wm}}$, with the
instantaneous LES velocity, pressure and temperature at $h_{\mathrm{wm}}$ as
top condition and an adiabatic no-slip wall; equations and constants are not
printed.

## Algebraic forms

When the ODE solution is replaced by its closed-form profile, the model is the
inversion of a [law of the wall](/definitions/law-of-the-wall.md) for
$u_\tau$ at $y^+_{\mathrm{wm}}=h_{\mathrm{wm}}u_\tau/\nu$.

- **Log law only** (Vadrot et al. 2023b, Eqs. 1–2, after Moeng):
  $\tau_w=\rho\left[\kappa U_{\mathrm{LES}}/\ln(h_{\mathrm{wm}}/y_0)\right]^2$
  with $y_0=\nu e^{-\kappa B}/u_\tau$, $\kappa\approx0.4$, $B\approx5$
  (let $y_0$ denote this viscous length, page-local); implicit in $u_\tau$, so
  solved iteratively.
- **Piecewise profile** (Lozano-Durán et al. 2022, Eq. 1): $u^+=y^++a_1(y^+)^2$
  for $y^+<23$, $\kappa^{-1}\ln y^++B$ otherwise, $\kappa=0.41$, $B=5.2$, $a_1$
  from $C^1$ continuity; walls adiabatic. Agrawal et al. (2022, §VIII) use an
  algebraic $C^1$-continuous profile in its compressible formulation in the same
  code ([CharLES](/software/charles.md)). Lozano-Durán & Bae (2023, §3.2,
  Eq. 3.1) print the same profile and constants, attributed to Deardorff
  (1970) and Piomelli et al. (1989) as they cite them, with adiabatic walls
  and the LES velocity taken at the second grid point off the wall.
- **Linear/log switch** (Lewis et al. 2023, §3.2.2): in the compressible
  solver AVBP, a wall law "inducing a no-slip condition at the walls" (after
  Nicoud et al., as cited) that is linear for $y^+<11$ and logarithmic
  otherwise (after Schmitt et al., as cited); constants and matching location
  are not printed.
- **Reichardt profile** (Gillyns et al. 2022, §3–4, Eqs. 3, 5): the
  streamwise LES velocity at the top node of the first spectral element is
  inserted in Reichardt's composite law (see
  [law of the wall](/definitions/law-of-the-wall.md); $\kappa=0.38$,
  $B=4.1$), and the root $u_\tau$ is found by an iterative method from two
  initial guesses (algorithm not named): seven iterations on average to
  machine precision, 0.4 % of the cost of a time step, so that the look-up
  tables of earlier implementations are judged unnecessary (hardware not
  given). Sampling inside the wall-adjacent element keeps the model
  element-local and avoids inter-process communication; smooth walls, no
  pressure-gradient term.
- **Spalding's law** (Blind et al. 2023, §3.3): an algebraic wall model in
  the DG spectral element code [FLEXI](/software/flexi.md), solved by
  Newton's method in every Runge–Kutta stage; formula and constants not
  printed.
- **Explicit inversion** (Cai et al. 2022, §II.C.1, Eqs. 24–26, from the
  authors' earlier work as they cite it): a fitted closed-form inverse
  $y^+(Re_y)$ of a tanh-blended viscous/log profile, with the Lambert $W$
  function for the log branch, gives $u_\tau=y^+\nu/y$ from the wall-tangential
  velocity at distance $y$ without iteration (formulas on the
  [law of the wall](/definitions/law-of-the-wall.md) page). The authors
  contrast it with the Newton iteration of the "traditional logarithmic wall
  model" and credit it with eliminating unnecessary iterations and enhancing
  stability; because it is cheap, it can be inverted at all fluid points
  next to an immersed boundary (no cost figures). Only the equilibrium model
  is used because a proper implementation of non-equilibrium terms is "still
  arguable" (as they cite it).
- **Fitted equilibrium solution with pressure gradient** (Meneveau 2020, as
  used by Fowler et al. 2022, Eqs. 2.19–2.20, Algorithm 1): a fit returns
  $\langle u_\tau\rangle h_{\mathrm{wm}}/\nu$ from
  $Re_{\mathrm{wm}}=U_{\mathrm{LES}}h_{\mathrm{wm}}/\nu$ and the dimensionless
  pressure gradient
  $\psi_p=\rho^{-1}(\nabla_hP\cdot\hat{\boldsymbol e}_u)h_{\mathrm{wm}}^3/\nu^2$
  (page-local symbols), valid for smooth walls, $0<Re_{\mathrm{wm}}<10^7$,
  $|\psi_p|<2\times10^7$; for adverse gradients below a threshold
  $Re_{\mathrm{wm}}$ the fit returns zero friction (separation). Without
  pressure gradient this is the baseline EQWM of Fowler et al. (§5.1).

## Matching height and input treatment

| Source | Code / grid | $h_{\mathrm{wm}}$ | Input treatment |
|---|---|---|---|
| Lozano-Durán et al. (2022, §II.B) | CharLES, isotropic Voronoi | first off-wall cell centre | none |
| Lozano-Durán & Bae (2023, §3.2) | CharLES, isotropic Voronoi | second grid point off the wall | none stated |
| Lewis et al. (2023, §3.2.2, §3.3) | AVBP, prisms at walls, tetrahedra elsewhere | not stated; mean wall-normal first-cell size $\Delta y^+=25$ and 17, maxima 66 and 64, on two meshes (Table 6) | none stated |
| Agrawal et al. (2022, §VII.D, §VIII) | staggered finite differences (channel); CharLES (bump) | second off-wall point, first point at $y^+\sim100$ (channel); first point (bump) | dynamic coefficients averaged; SGS-stress wall condition $d\tau_{ij}/dy=0$ |
| Fowler et al. (2022, §5.1) | [LESGO](/software/lesgo.md) | first grid point, $h_{\mathrm{wm}}=\Delta y/2=\delta/30$ | the "2Δ spatial filter" of Bou-Zeid et al. (2005) on $U_{\mathrm{LES}}$ (Fowler's $\Delta$ is $h_{\mathrm{wm}}$) |
| Vadrot et al. (2023b, §II.B.1) | LESGO | first point, $\Delta y/2$ | sharp filter of twice the grid spacing |
| Griffin et al. (2023, §4) | CharLES | $0.3\delta$ (12 points per half-height) | none stated |
| Goc et al. (2021, §2.2) | CharLES, Alya | not quantified (deferred to Lehmkuhl et al. 2018) | — |
| Gillyns et al. (2022, §3, §5, §7) | Nek5000, spectral elements of degree 7 | top node of the first element, $y/\delta=0.063$–0.15 ($y^+=63$–153) at $Re_\tau=1000$; $y^+=260$, 520 at $Re_\tau=5200$ | exponential moving average in time, $\bar U_n=\bar U_{n-1}+\alpha_e(U_n-\bar U_{n-1})$, $\alpha_e=\Delta t/(C_t+\Delta t)$, $C_t=0.0025\,\delta/u_\tau$ (about five time steps) |
| Hoy & Bermejo-Moreno (2022, §3) | unstructured finite volume | $0.1\delta_0$, four uniform cells below | none stated |
| Blind et al. (2023, §3.3, §4) | FLEXI, DG spectral elements of degree 5, residual-adapted grids | channel: $0.1h$ ($h^+_{\mathrm{wm}}=200$ at $Re_\tau=2000$), in the first or, on the finest adapted grid, the second cell; airfoil: $0.0134c$, about 10 % of the mean $\delta_{99}$, chosen by the exchange-location algorithm of Kahraman & Larsson on wall-resolved reference data | none stated |
| Cai et al. (2022, §II.C.1) | ProLB lattice Boltzmann, octree Cartesian grid, [immersed boundary](/methods/immersed-boundary-method.md) | first fluid points next to the boundary; $u_\tau$ (not the velocity) interpolated to the boundary points, e.g. by inverse distance weighting | none stated |
| Bae & Koumoutsakos (2022, Methods) | staggered finite differences | $0.1\delta$ in the correlation analysis (Figs. 6–7) | formulation not printed ("RANS-based", coefficients "tuned for this particular case") |

Gillyns et al. (2022, §5) find that without the moving average ($C_t=0$) the
model diverges, "most likely due to the Gibbs phenomenon at the element
boundary", that $C_t=0.0025\,\delta/u_\tau$ gives the same statistics as
$C_t=2\,\delta/u_\tau$ with a much shorter settling time, and that the same
value is near optimal at $Re_\tau=5200$; spanwise element-wise averaging gave
no gain (page-local symbols $\bar U_n$, $\alpha_e$, $C_t$). "The law of the
wall is quite robust to the input quantity, yet it still requires a minimal
time averaging". The matching height barely matters while it stays below
$0.15\delta$: errors grow slightly from the lowest to the highest first
element, so a first element ending near $y^+\simeq150$ "is not necessarily
the best choice" (§7, Table 1).

The choice is tied to [log-layer mismatch](/definitions/log-layer-mismatch.md):
matching away from the wall or filtering the input are the recalled remedies,
and first-point matching on Voronoi grids is reported to work without them.

## Error propagation: external against internal errors

Lozano-Durán et al. (2022, §IV.C, Eq. 12) propagate errors through the log-law
model with the matching point in the log layer. Writing every quantity as
$q=q_{\mathrm{exact}}(1+e_q)$ (page-local relative error $e_q$),

$$e_{U}=\frac{1+e_{u_\tau}}{1+e_\kappa}\left(1+\frac{\ln(1+e_{u_\tau})+\kappa B\,(e_\kappa+e_B+e_\kappa e_B)}{\kappa\phi}\right)-1,\qquad \phi=\frac1\kappa\ln Re_{h}+B,$$

with $Re_h=u_\tau h_{\mathrm{wm}}/\nu$ and the constants at their exact values in
$\phi$ (page-local symbols). Two error classes follow:

- **External errors**, in the LES velocity at the matching point, exist even
  for an exact model and propagate about linearly, $e_{u_\tau}\propto e_U$,
  with weak sensitivity to $Re_h$.
- **Internal errors**, in the model constants or from a failing log law
  (pressure gradient, roughness, separation), set a floor: $e_\kappa=10\%$
  gives $e_{u_\tau}\approx6\%$ and $e_B=10\%$ gives about 3 %, both smaller
  than the 10 % that a 10 % external error gives. "Wall models are more
  resilient to internal errors than to external errors"; but internal errors
  mean WMLES may not converge to DNS until the grid reaches wall resolution.
  Errors of the two kinds can also cancel and give a fortuitously good $u_\tau$.

Lozano-Durán & Bae (2023, §4) measure both classes a posteriori by
replacing the SGS model with an "exact-for-the-mean" correction that removes
the external error (see the [building-block-flow wall model](/methods/building-block-flow-wall-model.md)).
The internal error of the equilibrium model is above 20 % in a laminar
Blasius boundary layer, about 2 % in a zero-pressure-gradient turbulent
boundary layer at $Re_\theta=800$–2000, below 5 % in pipe flow at
$Re_\tau\approx40\,000$ even on the coarsest grid (§4.2–4.4); on the
upstream fuselage of the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
both it and the learned model stay below 2 % error (§4.8, Table 1). The two classes cancel in practice: with dynamic
Smagorinsky or Vreman the laminar mean velocity stays within 5 % despite the
internal error, and in adverse pressure gradient and separation the
equilibrium model has the smaller total error "for the wrong reasons", under-predicting
$\tau_w$ while the near-wall mean velocity is over-predicted (§4.2, §4.5,
Fig. 11). The authors also attribute its better lift at low incidence on the NASA
CRM-HL to such cancellation ("it has been reported", with no citation,
§4.7).

Goc et al. (2021, §2.2) recall the complementary bound of Bose & Park (2018):
the equilibrium-model wall-stress error is bounded by the resolution of the
matching location relative to the displacement or momentum thickness, even with
pressure gradients, because the outer LES resolves the non-equilibrium effects.

## Wall-stress fluctuations

Bae & Koumoutsakos (2022, p. 8, Figs. 6–7) point out that in a deterministic
wall model such as the equilibrium model the modelled wall stress is
perfectly correlated with the LES velocity at the sampling location, whereas
DNS gives a correlation of about 0.3, as they recall; their log-law-based
reinforcement-learning model reproduces about 0.3 at $h_{\mathrm{wm}}=0.1\delta$
(see [machine-learning wall models](/methods/machine-learning-wall-model.md)).

## Cost

Vadrot et al. (2023b, §IV.D) count 5 operations per evaluation for the
algebraic log-law model (a multiplication, two divisions, a logarithm, a
square), recall that the ODE-based model adds 10–30 % overhead to an LES, and
measure the ODE model at about four times the cost of the
reinforcement-learning wall model BK22 (one cluster, no hardware detail).
Griffin et al. (2023, §4) report that their one-ODE
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
costs between 7 % less and 32 % more than the classical two-ODE compressible
model. Lozano-Durán & Bae (2023, §2.6) report that their learned
building-block-flow model makes a CharLES WMLES 1.1–1.3 times as expensive as
the algebraic equilibrium model.

## Limits shown by the sources

- **Strong wall heat transfer.** The classical compressible model is hard to
  converge (Fu et al. 2021, as recalled by Griffin et al. 2023, §1), and its
  wall-stress and heat-flux errors grow with the cooling parameter $-B_q$,
  both a priori on 48 DNS cases and a posteriori in nine channels at
  $M_b=0.7$–$4$; its log-intercept error persists under grid refinement, so
  the wall model, not numerical or SGS error, dominates (Griffin et al. 2023,
  §3–4, Figs. 5, 10, 13). Griffin et al. trace this to the van Driest-consistent
  damping and the constant $Pr_t$.
- **Fast non-equilibrium forcing.** After a sudden spanwise pressure gradient
  the equilibrium model responds linearly in time, while DNS shows the
  $\sqrt t$ growth of a laminar Stokes layer (Fowler et al. 2022, §5.2,
  Fig. 12); the [LaRTE model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
  recovers it. Fowler et al. note that their EQWM is closer to the DNS than
  that of Lozano-Durán et al. (2020), attributing the difference to a smaller
  matching height. In a channel at $Re_\tau=700$ with a sudden spanwise
  pressure gradient 80 times the streamwise one, Lozano-Durán & Bae (2023,
  §4.6, Fig. 13) find that the algebraic model misses the mild drop of the
  streamwise wall stress and, by construction, the angle between the
  wall stress and the velocity at the first off-wall point, which their
  learned model predicts.
- **Laminar regions.** Inverted in a laminar Blasius boundary layer, the
  log-law model has an internal error above 20 % (Lozano-Durán & Bae 2023,
  §4.2, Fig. 8); the learned model of the same authors has no
  transition mechanism either (§5(1)).
- **Separation and corners.** In the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
  the mean-velocity error reaches about 15 % in the wing–body juncture and
  about 100 % in the separated trailing-edge corner (Lozano-Durán et al. 2022,
  §V.B), which the authors partly attribute to internal (log-law) errors.
- **Shock-induced separation.** Hoy & Bermejo-Moreno (2022) apply the model
  to a Mach 3 impinging shock/boundary-layer interaction with a separation
  length of 8–13 $\delta_0$, resting its validity in such non-equilibrium
  separated flows on earlier work (Bermejo-Moreno et al. 2014, as recalled,
  §1).
- **Massive separation on a bluff body.** Cai et al. (2022, §II.C.2, §IV)
  apply the explicit equilibrium model on the whole Ahmed body (a generic car
  body) with a 35° slant ($Re_H=7.68\times10^5$, $H$ the body height), including
  the front where they acknowledge pressure-gradient effects, arguing that
  the wall stress in the recirculation is small, that the model then acts in
  the linear range and that the flow is insensitive to it there (as recalled).
  On their coarse grid this "wall-law" case does not separate on the slant,
  which they attribute to the assumed alignment of wall stress and tangential
  velocity at the boundary points and to too little near-wall turbulent
  stress; on the fine grid it separates massively and, by their velocity
  profiles, "outperforms" a case with no-slip imposed in advance on slant and
  base. With the wall stress applied through an
  [immersed boundary](/methods/immersed-boundary-method.md), they state that
  flow separation required enhancing the near-wall Reynolds stress (the
  constrained-LES viscosity on the [wall-modelled LES](/methods/wall-modelled-les.md)
  page): "Without this enhancement, the flow stays attached even by refining
  the grid" (no run without it is shown in the paper).
- **Adverse pressure gradient.** The log law that the algebraic forms invert
  ends below $0.11\delta$ once the inner-scaled pressure gradient exceeds
  0.005 and the Rotta–Clauser parameter 4.5, and below $0.08\delta$ beyond
  0.015 and 12 ([Knopp 2022](/sources/knopp-2022.md), §5.2); see the
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
  Knopp's paper targets RANS wall functions, not WMLES. By the second bound
  a matching height of $0.1\delta$ lies above the log layer; by Knopp's
  Eq. (35) it does so once the inner-scaled pressure gradient exceeds about
  0.057 at $Re_\tau=1000$ and 0.0057 at $Re_\tau=2500$ *(compiler check, not in
  the sources)*. Gillyns et al. (2022, §1) expect
  their algebraic model to fail once Coles' wake reaches the matching point.
- **Equilibrium as a limit.** Fowler et al. (2022, §2.2) derive the classical
  model as the limit $T_s\to0$ of their relaxation equation (page-local $T_s$,
  the relaxation time of the fluid layer below $h_{\mathrm{wm}}$); applying the
  equilibrium stress instantaneously is justified only under full time-scale
  separation.

In equilibrium flows the model is adequate: Fowler et al. (2022, §5.1) find
equilibrium-model and LaRTE channel statistics "nearly indistinguishable" for
$Re_\tau=10^3$ to $5\times10^5$, and Vadrot et al. (2023b, §III.A) find the
algebraic model captures the log law whenever $h_{\mathrm{wm}}$ lies in the log
layer (at $Re_\tau=180$, with the matching point in the viscous layer, its
profile lies above the DNS).

## Qualifications

- The printed Eq. (1.2) of Griffin et al. (2023) lacks the minus sign in the
  exponent of the damping function (see the [law of the wall](/definitions/law-of-the-wall.md)
  page); the form above is the one their text describes.
- Goc et al. (2021) cite "Choi and Moin (1994)" for the WMLES grid-point
  scaling in §4, while the same section attributes it to Choi & Moin (2012);
  their reference list gives the 1994 work as "Effects of the computational
  time step on numerical solutions of turbulent flow".
- [Basile et al. (2023)](/sources/basile-2023.md) (§4.2.3) recall that the
  LES of the PPRIME jet by Brès et al. uses an equilibrium wall model inside
  the nozzle, which allows elements much larger than $y^+=1$, and note that
  dof comparisons with such a computation are not like-for-like.
- [Krais et al. (2021)](/sources/krais-2021.md) (§2.2.3, §7.3) list a wall-stress
  model after Larsson et al. and Kawai & Larsson in [FLEXI](/software/flexi.md)
  and use it with the Vreman SGS model in a zonal LES of an open cavity at
  $N=7$ with a wall-adjacent spacing of $y^+=15$; no equations or matching
  height are printed.
- Cai et al. (2022) never print the value of $\kappa$ used in their
  explicit model; the blend constants (180.8 and 0.789 for the inverse,
  10.71 and 1.526 for the forward profile) and $E=11.27$ are printed.

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §2.2, Eq. (2.6), Fig. 2.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §IV.C, Eq. (12), Fig. 8; §V.B–V.C.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D; §VIII.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §1; §2.2, Eqs. (2.19)–(2.21), Algorithm 1; §5.1–5.2, Fig. 12.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II.B.1, Eqs. (1)–(2), Table II; §III.A; §IV.D.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1, Eqs. (1.1)–(1.3); §3–4, Figs. 5, 10, 13.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.3.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1; §3–5, Eqs. (3)–(5); §7, Table 1.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §1; §3; §4.3.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — p. 8, Figs. 6–7; Methods.
- [Knopp (2022)](/sources/knopp-2022.md) — §5.2.
- [Basile et al. (2023)](/sources/basile-2023.md) — §4.2.3.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.C.1, Eqs. (24)–(26), Fig. 1(b); §II.C.2; §IV, Table III.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.3; §4.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.6; §3.2, Eq. (3.1); §4.2–4.8, Figs. 8–13.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.2; §3.3, Table 6.
