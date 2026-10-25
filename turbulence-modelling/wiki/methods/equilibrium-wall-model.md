---
type: Method
title: "Equilibrium wall model"
description: "The wall-stress model of wall-modelled LES that assumes a locally constant-stress, equilibrium inner layer: its ODE and algebraic forms, constants, matching heights, compressible extension, error propagation from LES input and model constants, cost, and the regimes where the sources show it fails."
status: established
aliases: [EQWM, EWM, wall-stress model, equilibrium wall-stress model, ODE wall model, algebraic wall model]
tags: [wall-model, wmles, boundary-layer, rans]
timestamp: 2026-10-25T13:44:00Z
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
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) and
[Griffin et al. (2023)](/sources/griffin-2023.md). It is the boundary
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
  code ([CharLES](/software/charles.md)).
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
| Agrawal et al. (2022, §VII.D, §VIII) | staggered finite differences (channel); CharLES (bump) | second off-wall point, first point at $y^+\sim100$ (channel); first point (bump) | dynamic coefficients averaged; SGS-stress wall condition $d\tau_{ij}/dy=0$ |
| Fowler et al. (2022, §5.1) | [LESGO](/software/lesgo.md) | first grid point, $h_{\mathrm{wm}}=\Delta y/2=\delta/30$ | the "2Δ spatial filter" of Bou-Zeid et al. (2005) on $U_{\mathrm{LES}}$ (Fowler's $\Delta$ is $h_{\mathrm{wm}}$) |
| Vadrot et al. (2023b, §II.B.1) | LESGO | first point, $\Delta y/2$ | sharp filter of twice the grid spacing |
| Griffin et al. (2023, §4) | CharLES | $0.3\delta$ (12 points per half-height) | none stated |
| Goc et al. (2021, §2.2) | CharLES, Alya | not quantified (deferred to Lehmkuhl et al. 2018) | — |

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

Goc et al. (2021, §2.2) recall the complementary bound of Bose & Park (2018):
the equilibrium-model wall-stress error is bounded by the resolution of the
matching location relative to the displacement or momentum thickness, even with
pressure gradients, because the outer LES resolves the non-equilibrium effects.

## Cost

Vadrot et al. (2023b, §IV.D) count 5 operations per evaluation for the
algebraic log-law model (a multiplication, two divisions, a logarithm, a
square), recall that the ODE-based model adds 10–30 % overhead to an LES, and
measure the ODE model at about four times the cost of the
reinforcement-learning wall model BK22 (one cluster, no hardware detail).
Griffin et al. (2023, §4) report that their one-ODE
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
costs between 7 % less and 32 % more than the classical two-ODE compressible
model.

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
  matching height.
- **Separation and corners.** In the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
  the mean-velocity error reaches about 15 % in the wing–body juncture and
  about 100 % in the separated trailing-edge corner (Lozano-Durán et al. 2022,
  §V.B), which the authors partly attribute to internal (log-law) errors.
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
- [Krais et al. (2021)](/sources/krais-2021.md) (§2.2.3, §7.3) list a wall-stress
  model after Larsson et al. and Kawai & Larsson in [FLEXI](/software/flexi.md)
  and use it with the Vreman SGS model in a zonal LES of an open cavity at
  $N=7$ with a wall-adjacent spacing of $y^+=15$; no equations or matching
  height are printed.

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §2.2, Eq. (2.6), Fig. 2.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §IV.C, Eq. (12), Fig. 8; §V.B–V.C.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D; §VIII.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §1; §2.2, Eqs. (2.19)–(2.21), Algorithm 1; §5.1–5.2, Fig. 12.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §II.B.1, Eqs. (1)–(2), Table II; §III.A; §IV.D.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1, Eqs. (1.1)–(1.3); §3–4, Figs. 5, 10, 13.
- [Krais et al. (2021)](/sources/krais-2021.md) — §2.2.3; §7.3.
