---
type: Method
title: "Equilibrium wall model"
description: "The wall-stress model of wall-modelled LES that assumes a locally constant-stress, equilibrium inner layer: its ODE and algebraic forms, constants, matching heights, compressible extension, error propagation from LES input and model constants, cost, and the regimes where the sources show it fails."
status: established
aliases: [EQWM, EWM, wall-stress model, equilibrium wall-stress model, ODE wall model, algebraic wall model]
tags: [wall-model, wmles, boundary-layer, rans]
timestamp: 2026-10-28T11:51:00Z
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
[Blind et al. (2023)](/sources/blind-2023.md),
[Duan & Wang (2024)](/sources/duan-2024.md) and
[Mozaffari et al. (2024)](/sources/mozaffari-2024.md) (with hybrid RANS/LES
rather than LES), [Mukha et al. (2025)](/sources/mukha-2025.md),
[Nuca et al. (2025)](/sources/nuca-2025.md), who reformulate the
Spalding, Reichardt and ODE forms as explicit laws, the compressible ODE
models of [De Vanna et al. (2022)](/sources/devanna-2022.md) and
[van Noordt et al. (2022)](/sources/vannoordt-2022.md) in shock/boundary-layer
interactions, and the wall law of the
fan-stage WMLES of [Lewis et al. (2023)](/sources/lewis-2023.md); it is the comparison
baseline of the learned models of [Bae & Koumoutsakos (2022)](/sources/bae-2022.md)
and of the [building-block-flow wall model](/methods/building-block-flow-wall-model.md)
of [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) and of the
reinforcement-learning model of [Vadrot et al. (2023a)](/sources/vadrot-2023.md). It is the boundary
condition that defines [wall-modelled LES](/methods/wall-modelled-les.md). The review of [Bose & Park (2018)](/sources/bose-2018.md) (§2.1)
places it as the special case of the thin-boundary-layer-equation model in
which only the wall-normal diffusion is kept, and [Heinz (2020)](/sources/heinz-2020.md)
(§3.1) as the case $F_i=0$ of the same equation; the models that keep the
dropped terms are on the [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
page, where [Lv et al. (2021)](/sources/lv-2021.md) use the model of Kawai &
Larsson (2012), as cited, as the baseline of their integrated wall model.
The same equilibrium wall function also closes steady RANS at coarse
near-wall resolution: [Constant et al. (2024)](/sources/constant-2024.md)
use it with the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
on an [immersed boundary](/methods/immersed-boundary-method.md), and
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md) with the $k$-$\omega$
model in a high-order DG solver, borrowing the WMLES practice of sampling
away from the wall and the constant-stress hypothesis (see
[RANS wall function](/methods/rans-wall-function.md)).
[Husson et al. (2024)](/sources/husson-2024.md) (§3.1–3.2) impose the
Spalart–Allmaras analytical wall law, linearized below the interpolation
point, through a lattice Boltzmann immersed boundary in RANS and in the RANS
zone of [zonal DES](/methods/detached-eddy-simulation.md), on the stated
equilibrium hypothesis (formulas on the RANS wall function page).
[Wu & Lele (2026)](/sources/wu-2026.md) (§2.2, §6.2) run their wall-modelled
channel LES with "a classic wall model" identical to that of Bou-Zeid et al.
(2005), as cited, without printing its form, so that it is an equilibrium
model is not stated in the source.
[Hu et al. (2024)](/sources/hu-2024.md) use the algebraic form in their
grid-convergence study of WMLES (below), and [Zhou & Bae (2024)](/sources/zhou-2024-b.md)
use an equilibrium stress-balance model in the precursor LES that feeds
their [Gaussian bump](/benchmarks/gaussian-bump.md) and an idealized
equilibrium wall condition on the bump itself (below).

**History.** In the account of [Kim & Leonard (2024)](/sources/kim-2024-b.md)
(§2.5, §3.1), the first channel LES already replaced no slip by a wall
condition built on the log law: Deardorff (1970) with 6,720 grid points and
Schumann (1975) with up to 65 K grid volumes, both "special wall boundary
conditions" as Kim & Leonard put it, whereas Moin et al. (1978) were the
first to compute the wall region explicitly. The same review closes (§5)
with wall-modelled LES as a design tool for high-lift aircraft (Goc et al.
2021). **A stochastic alternative.** The review of One-Dimensional
Turbulence by [Chen et al. (2024b)](/sources/chen-2024-c.md) (§3.3,
Fig. 13) sets the wall-stress model beside ODT used as a near-wall LES
closure (Schmidt et al. 2003; Freire & Chamecki 2021, as cited): the ODT
region is an embedded near-wall mesh like that of the wall-stress approach,
but the transport there comes from stochastic eddy events rather than
gradient diffusion (see [one-dimensional turbulence](/methods/one-dimensional-turbulence.md)).

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
Moin 2000 as they cite it). The problem is iterative because $\mu_t$ depends
on $\tau_w$. Goc et al. (2021, Eq. 2.6) write the same balance as
$d\big(\mu\,dU/dy-\langle\rho u''v''\rangle\big)/dy=0$ with the Reynolds shear
stress closed by a mixing-length eddy viscosity (constants not printed), and obtain the
wall heat flux $q_w$ from an analogous energy-equation approximation. Agrawal et
al. (2022, §VII.D) use the Cabot–Moin form, a boundary-value problem solved
for given matching height and LES velocity.

Bose & Park (2018, §2.1, Eq. 6) write the same closure as
$\mu_t=\rho\kappa u_\tau y\,D(y)$ with a damping function $D$ (van Driest,
for example; page-local) and $\kappa\approx0.41$ for zero-pressure-gradient
layers, after Wang & Moin (2002) as cited: the solution is a layer
of constant total stress, $d\tau/dy=0$, that reproduces the linear sublayer
and the log law. They read it as a steady RANS solution of the inner layer,
i.e. as an ensemble of many eddies (after Piomelli & Balaras 2002, as
cited), which presupposes wall-adjacent cells larger than a minimal
channel, $\Delta x^+\gtrsim300$, $\Delta z^+\gtrsim100$, with experimental
support for $\Delta^+\gtrsim1800$ (Nakayama et al. 2004, as cited). Data
support the constant-stress premise only close to the wall:
$0.95<\tau/\tau_w<1$ for $y/\delta\lesssim0.03$ at high enough Reynolds number
(§2.1, Fig. 3; see [law of the wall](/definitions/law-of-the-wall.md)).

**Compressible extension.** For compressible flow with heat transfer the
momentum ODE is coupled with a total-energy ODE,

$$\frac{d}{dy}\left[(\mu+\mu_t)U\frac{dU}{dy}+c_p\left(\frac{\mu}{Pr}+\frac{\mu_t}{Pr_t}\right)\frac{dT}{dy}\right]=0,$$

with $Pr_t=0.9$, an ideal gas, a viscosity law and constant pressure across the
inner layer; the boundary conditions are the wall temperature and the matching
temperature (Griffin et al. 2023, Eq. 1.3, after Larsson et al. 2016 as they
cite it). Two coupled nonlinear boundary-value problems must then be iterated.
Hoy & Bermejo-Moreno (2022, §3) use the compressible equilibrium model of
Kawai & Larsson (2012), with a mixing-length eddy viscosity, solved on a
separate one-dimensional grid from the wall to $h_{\mathrm{wm}}$, with the
instantaneous LES velocity, pressure and temperature at $h_{\mathrm{wm}}$ as
top condition and an adiabatic no-slip wall; equations and constants are not
printed. [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) (§2.3,
Eqs. 2.17–2.20) print the Kawai–Larsson pair as the total-energy form above,
with the wall-parallel velocity magnitude and the mixing length
$\mu_t=\kappa\rho y\sqrt{\tau_w/\rho}\,[1-\exp(-y^+/A^+)]^2$, where
$\sqrt{\tau_w/\rho}$ is "the velocity scale with varying density".
Constants are $\kappa=0.41$, $A^+=17$ and $Pr_t=0.9$. The wall is adiabatic
no slip, and the instantaneous LES velocity and temperature are imposed at
$h_{\mathrm{wm}}$. The ODEs are solved on a stretched 39-point grid that
resolves the viscous sublayer, and $\tau_w$ and $q_w$ return to the LES as
flux boundary conditions. They place $h_{\mathrm{wm}}$ at the 10th LES grid
point "to avoid the large discretization error and the resultant log-layer
mismatch", following Kawai & Larsson (2012).

De Vanna et al. (2022, §2.2, Eqs. 6a–b) and van Noordt et al. (2022, §2.5,
Eqs. 34, 37) print the same pair in the split form

$$\frac{d}{dy}\left[(\mu+\mu_t)\frac{dU}{dy}\right]=0,\qquad\frac{d}{dy}\left[c_p\left(\frac{\mu}{Pr}+\frac{\mu_t}{Pr_t}\right)\frac{dT}{dy}\right]=-\frac{d}{dy}\left[(\mu+\mu_t)U\frac{dU}{dy}\right],$$

which is the total-energy equation above with the work term moved to the
right-hand side. Both close $\mu_t$ with a mixing length whose van Driest
damping is written in the semi-local wall distance $y^*$, with
$\kappa=0.41$, $A^+=17$: De Vanna et al. as $\mu_t=\kappa\rho u_\tau y\,[1-e^{-y^*/A^+}]^2$
with $\rho=p_{\mathrm{LES}}/(RT)$ and $Pr_t=0.9$, van Noordt et al. as
$\mu_t=\kappa\mu y^*\,[1-e^{-y^*/A^+}]^2$ ($Pr_t$ not printed). With
$y^*=y\sqrt{\langle\rho\rangle\tau_w}/\langle\mu\rangle$, $\mu y^*=\langle\rho\rangle y\sqrt{\tau_w/\langle\rho\rangle}$,
so the second form is Griffin et al.'s eddy viscosity with the damping in
$y^*$ in place of $y^+$ *(compiler check, not in the sources)*; De Vanna et
al. do not say which $u_\tau$ enters their form. Both describe the equilibrium
assumption as a balance of convection and pressure gradient (De Vanna et al.
§1, §2.2; van Noordt et al. Eq. 33, with $v=w=0$, no spanwise, streamwise or
temporal derivatives and $\partial(\rho uu)/\partial x=-\partial p/\partial x$),
the wording of Goc et al. above. The semi-local damping is the
Trettel–Larsson choice (see
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).

**How the stress reaches the LES.** Most sources of this page replace no
slip by the modelled $\tau_w$ (and $q_w$). Van Noordt et al. (§2.4–2.6) apply
$\tau_w$ and $q_w$ explicitly as the viscous fluxes at the intersections of
grid lines with an [immersed boundary](/methods/immersed-boundary-method.md),
contrasting this with the dynamic slip condition of Bose & Moin (as cited;
see [slip-wall models](/methods/slip-wall-model.md)). De Vanna et al.
(§2.2, Eqs. 7a–b) keep no slip and the thermal wall condition and instead
augment the wall viscosity and conductivity, $\tau_w=(\mu_w+\mu^w_{\mathrm{sgs}})\,\partial u_\parallel/\partial y$
and $q_w=(\lambda_w+\lambda^w_{\mathrm{sgs}})\,\partial T/\partial y$
with the resolved wall gradients ($u_\parallel$ the wall-parallel velocity,
$\lambda$ the conductivity, $\mu^w_{\mathrm{sgs}}$, $\lambda^w_{\mathrm{sgs}}$
the wall SGS increments; page-local), the viscosity-augmentation form that
Bae & Koumoutsakos (2022) also use (see
[log-layer mismatch](/definitions/log-layer-mismatch.md)); details on the
[wall-modelled LES](/methods/wall-modelled-les.md) page.

## Algebraic forms

When the ODE solution is replaced by its closed-form profile, the model is the
inversion of a [law of the wall](/definitions/law-of-the-wall.md) for
$u_\tau$ at $y^+_{\mathrm{wm}}=h_{\mathrm{wm}}u_\tau/\nu$.

- **Review of the algebraic family** (Bose & Park 2018, §2.1, Eq. 3): the
  log law $U_{\mathrm{LES}}=u_\tau[\kappa^{-1}\ln(h_{\mathrm{wm}}u_\tau/\nu)+B]$,
  a nonlinear equation for $u_\tau$, assumed valid locally and
  instantaneously with no penetration (Deardorff 1970; Schumann 1975;
  Grötzbach 1987, as cited); the composites of Spalding (1961) and Werner &
  Wengle (1993) that cover sublayer and buffer layer; the pressure-gradient
  term of Manhart et al. (2008); and Monin–Obukhov similarity for stratified
  atmospheric LES. The Werner–Wengle model is the wall model of the
  cruise NASA Common Research Model WMLES they cite (Lehmkuhl et al. 2016;
  §4.3).

- **Log law only** (Vadrot et al. 2023b, Eqs. 1–2, after Moeng):
  $\tau_w=\rho\left[\kappa U_{\mathrm{LES}}/\ln(h_{\mathrm{wm}}/y_0)\right]^2$
  with $y_0=\nu e^{-\kappa B}/u_\tau$, $\kappa\approx0.4$, $B\approx5$
  (let $y_0$ denote this viscous length, page-local); implicit in $u_\tau$, so
  solved iteratively. Vadrot et al. (2023a, §II.B.1, Eqs. 1–2) print the
  same model as the baseline of their reinforcement-learning study, with
  $h_{\mathrm{wm}}=\Delta y/2$ and the LES velocity filtered after Yang et
  al. (2017) as cited.
- **Piecewise profile** (Lozano-Durán et al. 2022, Eq. 1): $u^+=y^++a_1(y^+)^2$
  for $y^+<23$, $\kappa^{-1}\ln y^++B$ otherwise, $\kappa=0.41$, $B=5.2$, $a_1$
  from $C^1$ continuity; walls adiabatic. Agrawal et al. (2022, §VIII) use an
  algebraic $C^1$-continuous profile in its compressible formulation in the same
  code ([CharLES](/software/charles.md)). Lozano-Durán & Bae (2023, §3.2,
  Eq. 3.1) print the same profile and constants, attributed to Deardorff
  (1970) and Piomelli et al. (1989) as they cite them, with adiabatic walls
  and the LES velocity taken at the second grid point off the wall.
  [Hu et al. (2024)](/sources/hu-2024.md) (§4, Eq. 5) print it again in
  CharLES, with $a_1$ "calculated to ensure $C^1$ continuity at $y^+=23$"
  (value not printed), the model returning only the magnitude of the wall
  stress, aligned with the LES velocity at $h_{\mathrm{wm}}$ (§6.1); they
  choose it because it "obviates the need for meshing or discretization for
  the wall model".
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
  printed. Mukha et al. (2025, §II.C.1, §IV.A) use the same law in the
  continuous spectral-element code [Nek5000](/software/nek5000.md), with
  $\kappa=0.387$, $B=4.2$ for channel flow at $Re_\tau\approx8000$ and
  $\kappa=0.41$ with $B=5.2$ (§IV.A) or 5.5 (App. A), a printed
  inconsistency, for a flat-plate boundary layer; the stress is aligned with the sampled wall-parallel velocity, and
  the matching height can be set per wall node, the velocity there being
  obtained by spectral interpolation inside the element that contains it.
  Their accuracy analysis of the law itself is on the
  [law of the wall](/definitions/law-of-the-wall.md) page.
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
  arguable" (as they cite it). [Mozaffari et al. (2024)](/sources/mozaffari-2024.md)
  (§2.2, Eqs. 9–15) use the same explicit form in the same code with other
  printed constants ($s=86.58$, $p=0.7894$, $E\approx7.9$, $\kappa\approx0.41$;
  both papers attribute the form and their constants to Cai & Sagaut 2021,
  a disagreement recorded under Contradictions on the
  [law of the wall](/definitions/law-of-the-wall.md) page): the
  tangential velocity at a reference point placed one local grid size along
  the wall normal gives $u_\tau$, and the wall law sets the tangential
  velocity and the turbulence quantities of the first off-wall node. They
  ignore pressure-gradient effects knowingly, citing Cai et al. (2022) for
  the claim that in fully separated flows the model operates at low $y^+$,
  comparable to a linear reconstruction (§2.2). Nuca et al. (2025, Eq. 5)
  use an explicit law attributed to the same reference, written forward as
  $u^+(Re_y)$ with exponential blending, and re-optimize its two blend
  constants for each model and constant set (next item).
- **Explicit approximations of the Spalding, Reichardt and ODE models**
  (Nuca et al. 2025, §III–V, Eqs. 9–24, Tables I–VI). The three models are
  written as functions of the local Reynolds number
  $Re_y=U_{\mathrm{LES}}h_{\mathrm{wm}}/\nu$, computable from the sampled
  data, so that $\tau_w=\rho(U_{\mathrm{LES}}/u^+)^2$ follows with no
  iteration. The approximant is the explicit law above plus a buffer-layer
  correction,

  $$u^+(Re_y)\simeq u^+_{\mathrm{CS}}(Re_y)+\sum_{i=1}^{N_b}a_i\,e^{-b_i(\log_{10}Re_y-c_i)^2},\qquad N_b\in\{1,2,3\},$$

  with amplitudes $a_i$, widths $b_i>0$ and centres $c_i$ (page-local; the
  minus sign is the corrected reading of the printed Eq. 10, see
  Qualifications). The $3N_b+2$ coefficients, including the blend
  constants of $u^+_{\mathrm{CS}}$, minimize the 2-norm of the pointwise
  relative error on a log-uniform grid of the model's native variable,
  mapped to $Re_y$, by simplicial-homology global optimization (Eqs. 17–21).
  Two families result:
  - *Global* models ($N_b=1$): on a $20\times20$ grid of
    $(\kappa,B)$ for Spalding, $(\kappa,C)$ for Reichardt (with its damping
    lengths 11 and 3 fixed) and $(\kappa,A^+)$ for the ODE model (ranges on
    the [law of the wall](/definitions/law-of-the-wall.md) page), the optimal
    coefficients are regressed linearly on the two parameters (Eqs. 22–23,
    Table IV), giving one closed form for each model valid over the whole
    range, with error below 1 % for $Re_y$ from $10^{-4}$ to $10^6$
    (0.8 % in the conclusions), the Reichardt map including an extrapolation
    to $\kappa>0.4$ (§V.A, Figs. 4–6).
  - *Fixed-parameter* models ($N_b=3$, eleven coefficients each, Tables
    V–VI) for a high-Re set, $\kappa=0.387$, $B=4.21$, and a classical set
    ($\kappa=0.4$, $B=5.5$, $C=7.8$; $\kappa=0.41$, $A^+=17$ for the ODE),
    with printed errors below 0.05 % (§V.B, Fig. 7); see Qualifications
    for a check of the printed coefficients.

  The target of 1 % is argued from the models themselves, which are "not
  accurate" in the buffer layer, and from the about 1 % maximum error of
  the explicit approximation of an ODE model by Meneveau (2020), as they
  cite it, whose work treats roughness and pressure gradient and is called
  complementary (§I, §IV). The Lambert function is evaluated explicitly by
  one refinement of the initial guess of Iacono & Boyd (as cited), with at
  most 0.02 % error (App. A, Eqs. A1–A3). The explicit law can replace the
  model or seed its iteration; results are under "Robustness of the
  iterative inversion" below. The approach is stated to extend to any model
  coupling the linear and logarithmic laws in one dimension and to thermal
  wall layers, not shown.
- **Musker's law with RANS variables** (Constant et al. 2024, §3.2,
  Eqs. 6–11): at each immersed-boundary target point $A$ below the
  modelling height, $u_\tau$ from Newton–Raphson on Musker's law at the
  image point $B$ (assumed constant along the normal), tangential velocity
  $u_\tau f(y_A^+)$, normal velocity linear to zero at the wall, the
  Spalart–Allmaras variable from $\nu_t=\kappa u_\tau y\,[1-e^{-y^+/19}]$
  ($\kappa=0.41$; a quartic in $\tilde\nu$ solved by Ferrari's method),
  Crocco–Busemann temperature for adiabatic walls, and pressure equal to the
  image-point pressure. The quartic is exactly $\nu_t=\tilde\nu f_{v1}$ of the
  Spalart–Allmaras model solved for $\tilde\nu$ *(compiler check, not in the
  sources)*.
- **Explicit power law** (Ghidoni et al. 2026, §3.3, Eqs. 13–17, after
  Wilhelm et al. as cited), in RANS: $u^+=y^+$ below $y^+=11.81$ and
  $u^+=8.3\,(y^+)^{1/7}$ above, each branch inverted in closed form for
  $u_\tau$ and the two blended as $(u_{\tau,\mathrm{vis}}^4+u_{\tau,\log}^4)^{1/4}$
  (Menter et al., as cited); a second velocity scale built from $k$ keeps
  $\tau_w$ non-zero at separation. Formulas on the
  [RANS wall function](/methods/rans-wall-function.md) page.
- **Unprinted law of the wall in a high-order code** (Duan & Wang 2024,
  §4): the model takes the wall-parallel velocity, density and viscosity at
  the exchange point, "solves a nonlinear equation to obtain $u_\tau$" from
  the law of the wall (formula deferred to the authors' earlier papers, as
  cited) and imposes $\tau_w=\rho u_\tau^2$ weakly at the wall flux points of
  a [flux-reconstruction](/methods/flux-reconstruction.md) scheme.
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
- **Log law and Reichardt's law in a spectral/hp implicit LES**
  ([Huang et al. 2022c](/sources/huang-2022-c.md), §II C, Eqs. 14, 17,
  20): the wall-parallel velocity at the matching height, evaluated with
  the element's high-order expansion, is inserted in the log law with
  $\kappa=0.41$, $B=5.2$ (after Grötzbach 1987, as cited), $u_\tau$ is found
  by Newton–Raphson and $\tau_w=\rho u_\tau^2$ is imposed as a Neumann
  condition on the wall-parallel velocity, with no penetration and zero
  spanwise velocity at the wall; no eddy viscosity enters at the interface.
  Reichardt's composite law with $D=9.8$, $E=1/11$, $F=1/3$ (page-local
  constants; formula on the [law of the wall](/definitions/law-of-the-wall.md)
  page) is the alternative; at $Re_\tau=550$ the two give "only slightly"
  different statistics (§III C, Fig. 7). The paper also recalls the ODE
  form with the mixing-length viscosity $\kappa u_\tau y[1-e^{-y^+/A^+}]^2$
  ($A^+$ not printed; Eqs. 1–5) but does not use it.
- **Rough-wall log law in atmospheric LES**
  ([Zhang et al. 2022e](/sources/zhang-2022-i.md), §II A, Eq. 3; the
  source writes $z$ wall-normal, translated here): the wall stress
  $\tau_{i2}\rvert_w=-\big(\kappa/\ln(y/y_{0,\mathrm r})\big)^2\sqrt{\hat{\bar u}_1^2+\hat{\bar u}_3^2}\;\hat{\bar u}_i$,
  $i=1,3$, with $y_{0,\mathrm r}$ the aerodynamic roughness length
  (page-local, distinct from the viscous length $y_0$ above) and the hat a
  local average at twice the filter width, applied at the first grid point
  of [LESGO](/software/lesgo.md) and on the immersed terrain of a
  two-dimensional hill ($\kappa$ not printed). It is the classical
  equilibrium condition of atmospheric LES; the paper uses it as a fixed
  ingredient.

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
| Gillyns et al. (2022, §3, §5, §7) | Nek5000, spectral elements of degree 7 | top node of the first element, $y/\delta=0.063$–0.15 ($y^+=63$–153) at $Re_\tau=1000$; $y^+=260$, 520 at $Re_\tau=5200$ | exponential moving average in time, $\bar U_n=\bar U_{n-1}+\alpha_{\mathrm{ema}}(U_n-\bar U_{n-1})$, $\alpha_{\mathrm{ema}}=\Delta t/(C_t+\Delta t)$, $C_t=0.0025\,\delta/u_\tau$ (about five time steps) |
| Hoy & Bermejo-Moreno (2022, §3) | unstructured finite volume | $0.1\delta_0$, four uniform cells below | none stated |
| Blind et al. (2023, §3.3, §4) | FLEXI, DG spectral elements of degree 5, residual-adapted grids | channel: $0.1h$ ($h^+_{\mathrm{wm}}=200$ at $Re_\tau=2000$), in the first or, on the finest adapted grid, the second cell; airfoil: $0.0134c$, about 10 % of the mean $\delta_{99}$, chosen by the exchange-location algorithm of Kahraman & Larsson on wall-resolved reference data | none stated |
| Cai et al. (2022, §II.C.1) | ProLB lattice Boltzmann, octree Cartesian grid, [immersed boundary](/methods/immersed-boundary-method.md) | first fluid points next to the boundary; $u_\tau$ (not the velocity) interpolated to the boundary points, e.g. by inverse distance weighting | none stated |
| Bae & Koumoutsakos (2022, Methods) | staggered finite differences | $0.1\delta$ in the correlation analysis (Figs. 6–7) | formulation not printed ("RANS-based", coefficients "tuned for this particular case") |
| Vadrot et al. (2023a, §II.B.1) | LESGO, uniform $48^3$ half channel | first point, $\Delta y/2$ | filtered, after Yang et al. (2017) as cited |
| Duan & Wang (2024, §4, Fig. 4) | hpMusic, flux reconstruction of degree $N=2$–5 | interface between the first and second elements, $h_{\mathrm{wm}}$ equal to the first element height; data from the second element | element-wise constant SGS viscosity (no wall-model filtering stated) |
| Mozaffari et al. (2024, §2.2) | ProLB lattice Boltzmann, octree Cartesian grid, immersed boundary | reference point one local grid size along the normal from each boundary node | none stated |
| Mukha et al. (2025, §II.C.1, §III–IV) | Nek5000, continuous spectral elements of degree 7 | channel: $0.2\delta$, inside the first element on meshes of 2 and 4 elements per $\delta$ and in the second on 8, for elements of equal height *(compiler check, not in the sources)*; boundary layer: $0.2\delta_{99}(x)$, $\delta_{99}$ from a power-law estimate | none by default; exponential moving average of 5–500 time steps tested (channel), 10 time steps (boundary layer) |
| Nuca et al. (2025, §II, §VI, App. B) | OpenFOAM with the libWallModelledLES library, structured C-grid of 18.7 M cells, 10–12 cells across the boundary layer | airfoil: not printed; a priori channel test: $0.05\delta$, "the center of the second off-wall cell" of a notional WMLES grid | channel: LES velocity averaged over a cube of side $\delta/30$ around the sampling point; airfoil: none stated |
| Ghidoni et al. (2026, §3.3, Fig. 1, Alg. 1), RANS | modal DG, $N\le6$, body-fitted | internal quadrature point of the wall element farthest from the wall (nearest the opposite face), first-element heights $y_1^+=1$–320 | steady RANS, no filtering |
| De Vanna et al. (2022, §2.2, §3.2) | URANOS, uniform finite-difference grids | chosen dynamically from the local wall resolution, "sufficiently far from the wall and in an adequately resolved flow zone" (details deferred to their earlier work, as cited); model active only where $\Delta x^+_w<40$, $\Delta y^+_w<3$, $\Delta z^+_w<15$ (resolved $\tau_w$) is violated | none stated |
| van Noordt et al. (2022, §2.6, §3.1, §3.4) | CHAMPS, Cartesian octree, immersed boundary | far point of a ray from each surface-triangle centroid at a fixed outer-unit distance: about $0.05\delta$, varied over 3–4 minimum grid spacings (channel); $0.11\delta_r$ (ramp) | none stated; insensitive to the exchange distance (channel) |
| Huang et al. (2022c, §II C, §III A, §III D) | [Nektar++](/software/nektar-plus-plus.md), spectral/hp elements, "polynomial order $N_p=7$" as printed, $12\times6\times10$ elements | top of the first wall-adjacent element, $0.224\delta$ (about $y^+=123$, 213 and 448 at $Re_\tau=550$, 950, 2000 *(compiler check, not in the sources)*); "first layer grid" where $y^+>30$ | instantaneous by default; exponential moving average $\bar u^n=a u^n+(1-a)\bar u^{n-1}$, $a=0.01$, tested |
| Zhang et al. (2022e, §II A) | LESGO, uniform $192\times64\times97$, immersed terrain | first grid point | local average at $2\Delta$ (test filter) |
| Maeyama & Kawai (2023, §2.3, Table 1) | in-house sixth-order compact differences, eighth-order filter, stretched in $y$ | 10th grid point, $h^+_{\mathrm{wm}}\approx54$, 101, 191, 357, 677, 1287 at $Re_\tau\approx700$–14 000 (all in the log region) | instantaneous LES velocity and temperature |
| HLPW-4 participants, [Kiris et al. (2023)](/sources/kiris-2023.md) (Table 2, §II.5) | nine codes on the CRM high-lift configuration (structured overset, Voronoi, unstructured, Cartesian immersed boundary, $N=2$ flux reconstruction) | from the first off-wall point ($0.5\Delta$ in CharLES, $1\Delta$ in FUN3D) to the fourth off-wall cell ($3.5\Delta$); between the first and second elements in hpMusic | not stated; nodal (W-020, W-034, W-050) against cell-centred (W-021, W-031, W-047) application of the wall stress named as "perhaps a large source of discrepancy", the model variants being "of no consequence" |
| Constant et al. (2024, §3.1, §4.2), RANS | FastS finite volume, octree Cartesian grid, immersed boundary | modelling height $H_{\mathrm{mod}}$ from a flat-plate estimate of a target $y^+$ (50–500), then lowered locally after a first converged run (see below) | steady RANS, no filtering |
| Hu et al. (2024, §4–5, Tables 1–2) | CharLES, isotropic grids | fixed in outer units, $h_{\mathrm{wm}}=0.1\delta$, $0.2\delta$ (channels) and $0.05$–$0.15\delta$ (rotating free stream), always at a cell centre, while the grid is refined from $\Delta/h_{\mathrm{wm}}=2$ to about 0.12 | none stated |
| Zhou & Bae (2024, §2.2–2.3) | unstructured incompressible finite volume (You, Ham & Moin, as cited), isotropic and $4{:}1{:}2$ cells | idealized wall conditions on the bump: first off-wall cell centre; precursor flat-plate LES: equilibrium stress-balance model | running time average of the first-cell velocity with time scale $0.3L/U_\infty$, then $6L/U_\infty$ ($L$ the bump width), to calibrate the wall eddy viscosity |

Gillyns et al. (2022, §5) find that without the moving average ($C_t=0$) the
model diverges, "most likely due to the Gibbs phenomenon at the element
boundary", that $C_t=0.0025\,\delta/u_\tau$ gives the same statistics as
$C_t=2\,\delta/u_\tau$ with a much shorter settling time, and that the same
value is near optimal at $Re_\tau=5200$; spanwise element-wise averaging gave
no gain (page-local symbols $\bar U_n$, $\alpha_{\mathrm{ema}}$, $C_t$). "The law of the
wall is quite robust to the input quantity, yet it still requires a minimal
time averaging". The matching height barely matters while it stays below
$0.15\delta$: errors grow slightly from the lowest to the highest first
element, so a first element ending near $y^+\simeq150$ "is not necessarily
the best choice" (§7, Table 1).

Mukha et al. (2025, §II.C.1, Eqs. 5–6) apply the same exponential filter in
the same code: their weight $\Delta t/(\Delta t+\Delta t_{\mathrm{avg}})$ is
$\alpha_{\mathrm{ema}}$ with $C_t=\Delta t_{\mathrm{avg}}$ *(compiler check, not in the
sources)*. Their study separates a priori from a posteriori effects
(§III.B.3, Tables II–III, Figs. 4–5):

- **A priori**, feeding the wall model with the simulation's mean velocity
  at $h_{\mathrm{wm}}$ (the limit of infinite averaging) changes the
  mean-stress error from 0.71 %, 0.76 % and $-0.54$ % to 0.06 %, 0.2 % and
  $-1.07$ % on their three channel meshes; fluctuations of the input shift
  the stress error towards over-prediction (after Hultmark et al., as they
  cite it). With recorded probe data, most of the reduction is obtained by
  $\Delta t_{\mathrm{avg}}=50\Delta t=0.01\,\delta/u_\tau$, where the mean
  stress magnitude and the magnitude of the mean stress begin to coincide,
  i.e. where the spanwise velocity is averaged out; this lies in the
  inertial range of the temporal spectrum of $u'$ at $h_{\mathrm{wm}}$, far
  below the diffusion time $h_{\mathrm{wm}}/(\kappa u_\tau)\approx0.51\,\delta/u_\tau$
  that others recommend (as they cite it). The temporal stability of the
  direction of the modelled stress is proposed as a criterion for choosing
  $\Delta t_{\mathrm{avg}}$ automatically.
- **A posteriori**, runs with $\Delta t_{\mathrm{avg}}=5$, 10, 50 and
  $500\Delta t$ show "no systematic accuracy gain", because the velocity at
  the sampling point itself changes with $\Delta t_{\mathrm{avg}}$, which
  violates the a priori assumption. For algebraic models they conclude that
  $h_{\mathrm{wm}}$ matters more than $\Delta t_{\mathrm{avg}}$, "at odds
  with" Yang et al., as they cite them; for non-equilibrium RANS-based wall
  models averaging may matter more. Running without averaging, they did not
  see the divergence reported by Gillyns et al. (see Qualifications).

A third high-order code reports the same insensitivity as Mukha et al.
Huang et al. (2022c, §III D, Eqs. 21–22, Fig. 8) compare, in an implicit LES
of channel flow at $Re_\tau=550$, the instantaneous matching velocity with
an exponential moving average of weight $a=0.01$ (page-local; a time
constant of 99 time steps by the identity $a=\alpha_{\mathrm{ema}}$ above *(compiler
check, not in the sources)*): the results differ only marginally and both
agree with DNS, so they recommend the instantaneous velocity, which "speeds
up computation", in agreement with Frère et al.'s DG LES as they cite it.

The choice is tied to [log-layer mismatch](/definitions/log-layer-mismatch.md):
matching away from the wall or filtering the input are the remedies the
sources cite, and Lozano-Durán et al. (2022) and Agrawal et al. (2022)
report first-point matching on Voronoi grids without them.

**Modelling height chosen from the solution (RANS on an immersed
boundary).** Constant et al. (2024) set the height below which grid points
are modelled from a flat-plate skin-friction correlation and a user target
$y^+$ (§3.1, Eq. 5). At strong incidence this estimate fails near the
leading edge: on the NACA 0012 at $15^\circ$ the image-point $y^+$ there
exceeds a target of 300 by close to 300 % (§4.1, Fig. 10), so the wall
function is applied where the boundary layer is thin and not in
equilibrium. Their remedy converts modelled points back into computed ones
after a first converged run wherever the $y^+$ one layer below already
exceeds the target, a static single-pass update with a warm restart that
lowers the maximum suction-side image-point $y^+$ from 435 to 243 for a
target of 100 (§4.2, §6.1, Fig. 18). Details on the
[immersed boundary method](/methods/immersed-boundary-method.md) page.

## Robustness of the iterative inversion

Implicit laws need an iterative solve at every wall point and time step,
and the solve can fail. Nuca et al. (2025, §I–II) report from their own
work and from users of the libWallModelledLES library that the Newton
solver for Spalding's law "would often sporadically diverge" in WMLES of
complex geometries, particularly when the sampling height exceeds the first
off-wall node; they name large fluctuations of the sampled velocity, which
make the previous-step initial guess poor, and application of the model
where it is not physically valid, such as transition regions. On the
Aérospatiale A-airfoil near stall (configuration of Tamaki & Kawai, as
cited; wall model on the whole suction side) the Newton count of an
instantaneous snapshot rises to 5 in the transition region (Fig. 2).
Robustness "is not an issue" in channel flow or zero-pressure-gradient
plates, where equilibrium models are consistent with the physics, so the
canonical tests of most of the wall-model literature probe accuracy, not
robustness (§II). The remedies they list (sampling the near-wall cell
during initial transients, averaging the input, derivative-free solvers)
complicate the set-up and guarantee nothing (§II). The ODE model does not
diverge in this way but needs a one-dimensional mesh or adaptive quadrature
per wall node and a fixed-point iteration (§I).

Their explicit approximations (above) remove the iteration when used
directly, which they call "unconditionally stable" (by construction: there
is nothing to converge), or seed it in place of the previous-step stress.
Mean/maximum iteration counts (Tables VII–VIII):

| Model | Channel, previous step | Channel, high-Re explicit guess | Airfoil, previous step | Airfoil, high-Re explicit guess |
|---|---|---|---|---|
| Reichardt (Newton) | 1.95 / 3 | 1.79 / 2 | 2.88 / 11 | 2.93 / 3 |
| Spalding (Newton) | 1.95 / 3 | 1.52 / 2 | 2.95 / 10 | 2.95 / 3 |
| ODE (fixed point) | 3.27 / 6 | 1.03 / 2 | 1.37 / 100 | 1.00 / 6 |

The channel test is a priori: a stored wall-resolved LES signal at
$Re_\tau\approx1000$ (OpenFOAM, as cited), relative tolerance $10^{-4}$,
in which the explicit laws reproduce the iterated $\tau_w$ within 0.07 %
(high-Re constants) and 0.7 % (global); the global $N_b=1$ guess gives
1.91/2, 1.95/2 and 3.9/4. The airfoil test is a posteriori, averaged over
one convective time $c/U_\infty$ after about $13c/U_\infty$ of
initialization; 100 is the iteration cap of the ODE model, which therefore
failed to converge to its tolerance ($10^{-3}$) at some steps, and the
explicit Spalding stress differs from the iterated one by at most 0.06 %
over a wider $Re_y$ range than in the channel (§VI, Figs. 8–9). For the
algebraic laws the guess barely changes the mean count, because Newton
converges quadratically; in the laminar region $x/c<0.08$ the
previous-step guess is better, the flow there being steady (§VI). Accuracy
against experiment is not assessed; the reference is the original model.

## Pressure across the modelled layer

Constant et al. (2024, §1, lines 44–47) state that most recent
immersed-boundary work for high-Reynolds-number flow assumes a constant
wall-normal pressure across the whole turbulent boundary layer, and their own
wall function sets the target-point and wall pressures equal to the
image-point pressure (Griffin et al. 2023 likewise state constant pressure
across the inner layer for their compressible ODE). Constant et al. (§5)
show that this assumption, not the field solution, corrupts the
near-field pressure drag at strong incidence when the modelled layer is
thick: on the NACA 0012 at $15^\circ$ the zeroth-order extrapolation
$p_w=p_B$ misplaces the suction peak and gives a 94 % drag error against a
wall-resolved body-fitted reference, which local lowering of the modelling
height reduces to 47 %, and a second-order Taylor reconstruction of the
wall pressure from a second layer of image points (placed at the modelling
height plus $2\sqrt{d}\,h$, $d$ the space dimension and $h$ the near-wall
cell size, page-local) to 17 % (Table 3; $C_L$ error 2.6 %). The
reconstruction is applied only in post-processing; the authors justify this
by a mesh study in which refining at fixed target $y^+$ barely changes the
error although the distance over which the assumption acts falls by four
(§5.1, Figs. 12–13). On the NASA CRM high-lift configuration at
$17.05^\circ$ the same steps take the drag error from 9.1 % to 1.5 % and the
lift error from 13 % to 8.4 % against a body-fitted reference (§6.3,
Table 9). They agree with Cai et al. (2021, as cited) that far-field
integration gives a better pressure drag than near-field integration, but
attribute the near-field error to the wall-pressure reconstruction rather
than to the field (§5.1).

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

Mukha et al. (2025, §III.B.3, App. A, Fig. 19) observe the linear
propagation directly for Spalding's law with relative input errors of about
1–2 %: the mean-stress error is about twice the velocity-input error, and its
slope against the input error is twice that of the $u_\tau$ error. Since
$\tau_w=\rho_wu_\tau^2$, a relative error $e$ in $u_\tau$ gives $2e+e^2$ in
$\tau_w$, which accounts for the factor two between the stress and $u_\tau$
errors *(compiler check, not in the sources)*.

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

Goc et al. (2021, §2.2) cite the complementary bound of Bose & Park (2018):
the equilibrium-model wall-stress error is bounded by the resolution of the
matching location relative to the displacement or momentum thickness, even with
pressure gradients, because the outer LES resolves the non-equilibrium effects. The bound itself (Bose & Park 2018, §2.1, Eqs. 7–8) comes from
integrating the boundary-layer momentum equation up to $h_{\mathrm{wm}}$: the
pressure-gradient contribution to $\tau_w$ is at most the Clauser parameter
times $h_{\mathrm{wm}}/\delta^*$, so it can be made negligible by a low matching
height, but the height needed may depend on the pressure-gradient parameter
rather than being a fixed fraction of $\delta$, and the argument fails near
separation, where $\tau_w\to0$ (derivation and sign convention on the
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) page).

## Wall-stress fluctuations

Bae & Koumoutsakos (2022, p. 8, Figs. 6–7) point out that in a deterministic
wall model such as the equilibrium model the modelled wall stress is
perfectly correlated with the LES velocity at the sampling location, whereas
DNS gives a correlation of about 0.3, as they cite it; their log-law-based
reinforcement-learning model reproduces about 0.3 at $h_{\mathrm{wm}}=0.1\delta$
(see [machine-learning wall models](/methods/machine-learning-wall-model.md)).

Vadrot et al. (2023a, §III.B, Fig. 10) find that the wall-stress
fluctuations of all their models, the equilibrium model included, decrease
with increasing $Re_\tau$, and explain it with the algebraic form: the
fluctuation of $\tau_w$ scales as $1/(\ln h^+_{\mathrm{wm}}+B)$ times the
fluctuation of the input velocity, which falls as $h^+_{\mathrm{wm}}$ grows
(Eq. 12, a heuristic argument). Their printed Eq. (12) differs from their
Eq. (2) (see Qualifications).

## Cost

Vadrot et al. (2023b, §IV.D) count 5 operations per evaluation for the
algebraic log-law model (a multiplication, two divisions, a logarithm, a
square), cite earlier work for the statement that the ODE-based model adds 10–30 % overhead to an LES, and
measure the ODE model at about four times the cost of the
reinforcement-learning wall model BK22 (one cluster, no hardware detail).
Lv et al. (2021, §I, §II B 4) quote, for the ODE form on grids of
$O(10^6$–$10^7)$ points scaled up to 256 cores, an overhead of 30–40 %, and
for algebraic equilibrium models usually not more than 5 %, as they cite
earlier implementation studies.
Griffin et al. (2023, §4) report that their one-ODE
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
costs between 7 % less and 32 % more than the classical two-ODE compressible
model. Lozano-Durán & Bae (2023, §2.6) report that their learned
building-block-flow model makes a CharLES WMLES 1.1–1.3 times as expensive as
the algebraic equilibrium model. In RANS, Ghidoni et al. (2026, §4.1,
Table 2) measure the gain of an explicit over an implicit law: with the
first element at $y_1^+=320$ the computing time falls on average by 68.96 %
with the explicit power law and by 63.73 % with the Newton-iterated
Spalding law, against the wall-resolved run, over degrees $N=1$–6. In
WMLES, Nuca et al. (2025, §VI) measure the wall-modelling share of the run
time of their airfoil case at about 2 % with the Newton-iterated algebraic
laws, 1.8 % with the explicit Spalding law (the difference called not
statistically significant), 1.9 % with the explicit ODE approximation and
11.9 % with the integrated ODE model; all explicit laws perform the same
operations with different coefficients and cost the same (Shaheen III, no
further hardware detail).

## Limits shown by the sources

- **Correct statistics, numerical near-wall structures.** In Mach 2.28
  boundary layers at $Re_\tau\approx700$–14 000, [Maeyama & Kawai (2023)](/sources/maeyama-2023.md)
  find that with the Kawai–Larsson model the mean velocity, Reynolds shear
  stress and turbulent-kinetic-energy budget match the DNS above
  $h_{\mathrm{wm}}$. The total shear stress stays near $\tau_w$ even below
  it, with oscillations (§4.1–4.3, Figs. 4–5, 7). They read the accuracy
  through the inner-layer stress balance of Kawai & Larsson,
  $\tau_w\approx\langle\mu\,du/dy\rangle+\langle\mu_t\,du/dy\rangle-\langle\rho u''v''\rangle$
  (Eqs. 1.1, 4.2), which does not constrain the normal stresses. Below
  $h_{\mathrm{wm}}$ the LES grows streak-like ejection–sweep pairs with
  about 8 grid points per spanwise wavelength. They are wider than the
  physical streaks, and their width is set by the SGS eddy viscosity (§5;
  see [wall-modelled LES](/methods/wall-modelled-les.md)). The streamwise
  stress in the log region and the outer spectral peak do not grow with
  $Re_\tau$ as in the DNS (§6).
- **Variants on a high-lift aircraft.** In the HLPW-4 focus group summarized
  by Kiris et al. (2023, §II.5), "with the exception of one participant
  (W-032, who used a proprietary pressure-aware formulation), all groups
  utilized equilibrium models with adiabatic thermal conditions" (Table 2
  lists no wall model, "Not applicable", for the Euler submission W-030),
  on a flow the authors call strongly nonequilibrium. They judge the ODE-versus-algebraic variants "of no
  consequence for the present flow" (see
  [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).
- **Separation in the review.** Bose & Park (2018, §2.1) state that neither
  presumed profiles nor eddy-viscosity closures handle separation reliably:
  $u_\tau\to0$ there, and with it the mixing-length eddy viscosity. Earlier
  studies imposed no slip in regions known to separate (Bodart et al. 2013)
  or at corners (Cabot 1996), as cited, and the treatment of separation
  points "remains a theoretical challenge".
- **Secondary flows and compression corners.** Supersonic-duct WMLES with an
  equilibrium model over-predict the secondary corner flow and the corner
  shear stress (Vane et al. 2014), which suggests that the locally
  one-dimensional equilibrium approximation is inadequate for secondary
  flows, and a compression ramp shows a delayed initial pressure rise
  (Dawson et al. 2013), as cited by Bose & Park (2018, §4.4).
- **Laminar and transitional regions** in the review: equilibrium-type wall
  models must be switched off upstream of transition; the sensor of Bodart &
  Larsson (2012), as cited, suppresses the modelled turbulent stress where
  the velocity fluctuation at the top of the wall-model layer relative to
  $u_\tau$ falls below a threshold, and transition locations are then well
  predicted (Bose & Park 2018, §4.1).
- **Periodic hill.** Against the integrated wall model of Lv et al. (2021,
  §IV B 2, Fig. 17), the equilibrium model (Kawai & Larsson 2012, as cited)
  gives the less accurate skin friction on the leeside and near the crest at
  $Re_h=10\,595$; neither captures $C_f$ between $x/H\approx0$ and 2, and the
  grid matters more than the wall model (see
  [periodic hill](/benchmarks/periodic-hill.md)).
- **Strong wall heat transfer.** The classical compressible model is hard to
  converge (Griffin et al. 2023, §1, citing Fu et al. 2021), and its
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
  separated flows on earlier work (Bermejo-Moreno et al. 2014, as they cite it,
  §1).
- **Shock-induced separation with no slip kept.** De Vanna et al. (2022,
  §4.4–4.6, Figs. 5–7) apply the compressible ODE model through the
  viscosity-augmentation coupling to the oblique interaction at
  $M_\infty=2.28$, deflection $8^\circ$, $Re_\tau=700$ at the inflow. Because
  no slip is retained, the mean skin friction becomes negative in the
  bubble, which they present as a capability "mainly ruled out in classical
  equilibrium wall-modeling formulations"; but the interaction length
  $L_{\mathrm{int}}/\delta_r$ ($L_{\mathrm{int}}$ from the nominal impingement
  to the reflected-shock foot, $\delta_r$ the inflow 99 % thickness,
  page-local) is 7.0, 5.2 and 5.0 on the coarse, medium and fine
  grids against 3.3 for a wall-resolved LES and 4.18 in experiment (§4.6),
  and the reverse flow is "gentle" where the wall-resolved LES separates
  clearly. They attribute the oversizing to the wall model and to SGS plus
  shock-capturing dissipation that "laminarize" the bubble at low
  resolution, and contrast it with Gross et al. (as cited), who found
  separation "strongly under-predict[ed]" with a standard equilibrium model
  (§1). The wall-model activation sensor drops from above 0.95 in the
  attached layers to about 0.65 in the bubble, where small wall gradients
  make the wall more often treated as resolved (Fig. 6b).
- **Hypersonic compression ramp.** Van Noordt et al. (2022, §3.4, Figs.
  26–27) find, for a Mach 7.2, $8^\circ$ ramp against DNS, the surface
  pressure captured on the fine grid but an early pressure rise and too much
  instantaneous separation on the coarse one, a minimum $C_f$ notably above
  the DNS and a post-shock adjustment length of about $4\delta_r$ on the
  coarse mesh; as a possible cause they name the imbalance between the
  tangential pressure gradient and the convective terms that the
  equilibrium model does not capture. They also warn that in hypersonic flow
  a sampling point can lie beyond a thin shock layer and over-predict the
  viscous fluxes (§2.5).
- **Transitional hypersonic layers.** Van Noordt et al. (2022, §3.2, Eq.
  58) switch off the wall-model eddy viscosity where the sensor
  $\hat\rho\hat k/(\hat\mu\lvert\hat S\rvert)$ of Mettu & Subbareddy (as
  cited; $\hat k$ a test-filtered subfilter energy, the filter not defined
  in the paper) falls below $5/3$, a threshold tuned to the reference
  transition location of a Mach 6 flat plate, so the transition location is
  imposed rather than predicted; laminar surface quantities are not
  accurately predicted by the wall model and the heat transfer is sensitive
  to the numerical dissipation added at the immersed boundary (§3.2, §4).
  This is the role of the Bodart–Larsson sensor described above.
- **Massive separation on a bluff body.** Cai et al. (2022, §II.C.2, §IV)
  apply the explicit equilibrium model on the whole Ahmed body (a generic car
  body) with a 35° slant ($Re_H=7.68\times10^5$, $H$ the body height), including
  the front where they acknowledge pressure-gradient effects, arguing that
  the wall stress in the recirculation is small, that the model then acts in
  the linear range and that the flow is insensitive to it there (as they cite it).
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
- **Thin leading-edge boundary layers at strong incidence (RANS).**
  Constant et al. (2024, §6.1, Figs. 19–21) find that over the first 10 % of
  chord of the NACA 0012 at $15^\circ$ ($M=0.15$, $Re_c=6\times10^6$) the
  velocity profile cannot be represented by the equilibrium wall function,
  which holds once the log region is established downstream, and that the
  leading-edge error is carried downstream to the trailing-edge eddy
  viscosity. A residual drag error of about 20 % remains after both
  corrections; they relate it to the test-case sensitivity reported by
  others (as cited) and state that removing it would need the wall model
  applied only in the viscous sublayer at the leading edge (§6.1), with a
  non-equilibrium model as future work (§7).
- **Suppressed separation in hybrid RANS/LES.** Mozaffari et al. (2024,
  §3.3) apply the explicit model on the Ahmed body with SST-IDDES and
  continuous eddy simulation in a lattice Boltzmann solver: no separation
  appears on the $35^\circ$ slant, against a fully detached reference flow,
  while a zero-velocity condition at $y^+\gg1$ separates. They relate the
  attachment to the absence of a pressure-gradient term and conclude that
  under high adverse pressure gradient and mild separation "these wall
  models may introduce some error", proposing an APG-aware model as next
  step (§3.3, §4, lines 465–470, 550–557; see
  [wall-modelled LES](/methods/wall-modelled-les.md) for the comparison with
  Cai et al. 2022, whose Vreman LES with an enhanced near-wall stress does
  separate on the fine grid). For the NACA 0012 they also
  report that the equilibrium model under strong adverse pressure gradient
  degrades the surface forces (§3.2).
- **Strong adverse pressure gradient and recirculation (RANS, DG).**
  Ghidoni et al. (2026, §4.2–4.3, Figs. 8, 10) find their zero-pressure-gradient
  power law accurate for first-element heights up to $y_1^+=320$ on a flat
  plate and in weak adverse gradient, but degrading for $y_1^+>80$ near the
  end of the strong-gradient region of the DM2/DM3 plates and, at $N=6$, for
  $y_1^+>10$ in the recirculation of a backward-facing step, where the law
  of the wall gives wrong $u_\tau$ (details on the
  [RANS wall function](/methods/rans-wall-function.md) page).
- **Recirculation behind a step and in a slat cove (RANS and zonal DES on
  an immersed boundary).** Husson et al. (2024, §3.1) state that their
  immersed-boundary treatment and the linearized Spalart–Allmaras law both
  rest on the equilibrium hypothesis, so "significant discrepancies are to
  be expected" near separation and in recirculation; they cite work showing that
  non-equilibrium analytical laws and ODE models on embedded grids extend
  the validity, the latter at higher cost and with possible instability on
  non-body-fitted grids (as cited). In their results the near-wall
  differences at the first station of a [backward-facing step](/benchmarks/backward-facing-step.md)
  are attributed to the wall law imposing a zero-pressure-gradient profile
  in the recirculation, and the slightly too large slat recirculation of a
  three-element airfoil partly to the wall model (§4.2.2, §4.3.2; see
  [RANS wall function](/methods/rans-wall-function.md)).
- **Recirculating hill wake (atmospheric LES).** Zhang et al. (2022e,
  §III A, Fig. 4b) under-predict the streamwise turbulence intensity in the
  lower wake at the downwind foot of a steep two-dimensional hill (slope
  0.4, separated flow) against the wind-tunnel data of Cao & Tamura, and
  attribute it to the classical log-law wall model in recirculating flow,
  as Yang et al. (2015) reported, as cited; the attribution is not tested
  against another wall model.
- **Near-interface stresses with a Neumann coupling.** In the channel
  runs of Huang et al. (2022c, §III B, Figs. 4–6) the mean velocity agrees
  with DNS (at most 2 % and 5.4 % over-prediction at $Re_\tau=950$ and 2000),
  but the rms fluctuations and the Reynolds shear stress show a
  "parabolic" error around the matching interface, which they attribute to
  the high wall-normal velocity gradient that the Neumann condition
  creates at the wall and call common to wall-modelled approaches; they
  cite Bae & Lozano-Durán for the view that a Dirichlet condition with
  eddy-viscosity augmentation may do better near the wall, not tested (see
  [wall-modelled LES](/methods/wall-modelled-les.md)). They state that the
  algebraic model suits equilibrium layers only (§I, §IV).
- **Equilibrium as a limit.** Fowler et al. (2022, §2.2) derive the classical
  model as the limit $T_s\to0$ of their relaxation equation (page-local $T_s$,
  the relaxation time of the fluid layer below $h_{\mathrm{wm}}$); applying the
  equilibrium stress instantaneously is justified only under full time-scale
  separation.

**Relation to the slip wall.** Bose & Park (2018, §2.3) state that the
dynamic slip-wall condition, derived without any assumption on the velocity
profile or equilibrium, can be shown equivalent to an equilibrium wall-stress
model in its resulting stress (Yang et al. 2016, as cited); see
[wall-modelled LES](/methods/wall-modelled-les.md).

**Thermal equilibrium.** The same assumptions applied to the total-energy
equation with constant properties, $q_{\mathrm{turb}}\approx-\lambda_t\,\partial T/\partial y$
and $\lambda_t=\mu_tc_p/Pr_t$ (Rannie 1956, as cited), give the strong
Reynolds analogy $C_h=C_f/2$ in the absence of strong viscous heating, while
the work terms carry the inner-layer viscous heating and the near-wall
temperature peak (Bose & Park 2018, §2.5, Eq. 17; $q_{\mathrm{turb}}$,
$\lambda_t$ page-local, $C_h$ the Stanton number as on the Morkovin page). The analogy fails near
separation, where the skin friction vanishes but the heat transfer does not
(see [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)).

**Grid convergence fixed by the matching height.** On a channel at
$Re_\tau=1000$, Spalart's boundary layer under a rotating free stream
($Re_l=767$, page-local) and a channel at $Re_\tau=934$ with a sudden
spanwise pressure gradient, [Hu et al. (2024)](/sources/hu-2024.md)
(§6.1–6.2, Figs. 3–12) find that the mean wall stress, the mean velocity
above $h_{\mathrm{wm}}$ and the mean flow direction computed with the
algebraic model converge at coarser grids for larger $h_{\mathrm{wm}}$, with
onset near $\Delta/h_{\mathrm{wm}}\approx0.3$–$0.4$, while the streamwise
r.m.s. velocity converges much more slowly and without clear
$h_{\mathrm{wm}}$ dependence (see [wall-modelled LES](/methods/wall-modelled-les.md)).
In the three-dimensional layers the converged wall-stress magnitude is
more sensitive to $h_{\mathrm{wm}}$ than in the channel and more accurate for
smaller $h_{\mathrm{wm}}$, which they attribute to the model's assumption of
unidirectional flow in the wall-modelled region; "grid-converged WMLES is
not necessarily accurate" (§3, §6.1, §7).

**An idealized equilibrium condition.** [Zhou & Bae (2024)](/sources/zhou-2024-b.md)
(§2.2.2, Eqs. 3–7) derive from the thin-boundary-layer equations without
unsteadiness, convection and pressure gradient the first-cell balance
$\tau_{w,i}\approx\rho(\nu+\nu_{t,w})u_{{\mathrm c},i}/h_{\mathrm{wm}}$ ($i=1,3$;
$u_{\mathrm c}$ the first-cell-centre velocity, $\nu_{t,w}$ an effective
wall eddy viscosity, page-local), calibrate
$\nu_{t,w}\approx\tau^{\mathrm{DNS}}_w/(\rho\,\breve u_{\mathrm c}/h_{\mathrm{wm}})-\nu$
against the DNS mean wall stress ($\breve u_{\mathrm c}$ a running time
average of the first-cell velocity, page-local; the source writes it with
an overbar), and apply
$\tau_{w,i}=\rho(\nu+\nu_{t,w})\,\partial u_i/\partial y|_w$
through a Dirichlet (no-slip) condition, with $\nu_{t,w}\ge0$. On the
Gaussian bump its first-cell velocities resemble those of a Neumann
condition imposing the DNS mean stress directly, while for the
mixed-similarity model and the Vreman model with $c=0.025$ it moves
reattachment downstream and lengthens the bubble; the SGS model and the
mesh decide the separation more than the wall condition does (§3.2,
Figs. 14–16). The
pressure-gradient variant is on the
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) page.

In equilibrium flows the model is adequate: Fowler et al. (2022, §5.1) find
equilibrium-model and LaRTE channel statistics "nearly indistinguishable" for
$Re_\tau=10^3$ to $5\times10^5$, and Vadrot et al. (2023b, §III.A) find the
algebraic model captures the log law whenever $h_{\mathrm{wm}}$ lies in the log
layer (at $Re_\tau=180$, with the matching point in the viscous layer, its
profile lies above the DNS).

## Qualifications

- **One coefficient for two matching conditions.** With the printed
  $\kappa=0.41$, $B=5.2$ and junction at $y^+=23$, the piecewise profile
  $y^++a_1(y^+)^2$ / $\kappa^{-1}\ln y^++B$ cannot be both continuous and
  $C^1$ by tuning $a_1$ alone: slope matching gives $a_1\approx-0.0194$ and
  $u^+(23)\approx12.72$ against $12.85$ on the log branch, value matching
  gives $a_1\approx-0.0192$ with a slope mismatch *(compiler check, not in
  the sources; applies to the form as printed by Hu et al. 2024, Lozano-Durán
  et al. 2022 and Lozano-Durán & Bae 2023, none of whom prints $a_1$)*.
- The printed Eq. (1.2) of Griffin et al. (2023) lacks the minus sign in the
  exponent of the damping function (see the [law of the wall](/definitions/law-of-the-wall.md)
  page); the form above is the one their text describes.
- Goc et al. (2021) cite "Choi and Moin (1994)" for the WMLES grid-point
  scaling in §4, while the same section attributes it to Choi & Moin (2012);
  their reference list gives the 1994 work as "Effects of the computational
  time step on numerical solutions of turbulent flow".
- [Basile et al. (2023)](/sources/basile-2023.md) (§4.2.3) state that the
  LES of the PPRIME jet by Brès et al. uses an equilibrium wall model inside
  the nozzle, which allows elements much larger than $y^+=1$, and note that
  dof comparisons with such a computation are not like-for-like.
- [Krais et al. (2021)](/sources/krais-2021.md) (§2.2.3, §7.3) list a wall-stress
  model after Larsson et al. and Kawai & Larsson in [FLEXI](/software/flexi.md)
  and use it with the Vreman SGS model in a zonal LES of an open cavity at
  $N=7$ with a wall-adjacent spacing of $y^+=15$; no equations or matching
  height are printed.
- **Printed Eq. (12) of Vadrot et al. (2023a).** Presented as a rewriting
  of their Eq. (2), it reads
  $\tau_w=\rho\,\kappa U_{\mathrm{LES}}/(\ln h^+_{\mathrm{wm}}+B)$, without
  the square. With their $y_0=\nu e^{-\kappa B}/u_\tau$,
  $\ln(h_{\mathrm{wm}}/y_0)=\ln h^+_{\mathrm{wm}}+\kappa B$, so Eq. (2) gives
  $\tau_w=\rho[\kappa U_{\mathrm{LES}}/(\ln h^+_{\mathrm{wm}}+\kappa B)]^2$
  *(compiler check, not in the sources)*. The text after it prints an
  unbalanced "$1/(\ln(h^+_{wm}+B)$".
- Constant et al. (2024, §3.1) define the flat-plate first-cell height as the
  height "for which $y^+=0$"; their Eq. (5) is the height at which $y^+=1$
  *(compiler check, not in the sources)*.
- Cai et al. (2022) never print the value of $\kappa$ used in their
  explicit model; the blend constants (180.8 and 0.789 for the inverse,
  10.71 and 1.526 for the forward profile) and $E=11.27$ are printed.
- Mukha et al. (2025) print their filter, Eq. (5), with the same symbol for
  the averaged and the instantaneous input on both sides; the reading above
  (instantaneous sample on the right) is the only one consistent with their
  weight $\epsilon$ *(compiler check, not in the sources)*. They print $t_{\mathrm{diff}}\approx0.51\,\delta/u_\tau$,
  where $0.2/0.387=0.517$ rounds to 0.52 *(compiler check, not in the
  sources)*. Their locators refer to the arXiv v1 preprint read, whose author
  list (Mukha, Schlatter) lacks the third author of the Physics of Fluids
  version.
- **Time averaging of the wall-model input in Nek5000: two set-ups.**
  [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§5) report that their
  algebraic wall model diverges without the moving average ($C_t=0$),
  "most likely due to the Gibbs phenomenon at the element boundary", and
  conclude that the law of the wall "still requires a minimal time
  averaging" (channel at $Re_\tau=1000$ and 5200, Reichardt's law sampled at
  the top node of the first element, $h_{\mathrm{wm}}=0.05\delta$–$0.15\delta$,
  with Nek5000's approximate-deconvolution model, a high-pass relaxation
  filter of weight 10, as SGS treatment).
  [Mukha et al. (2025)](/sources/mukha-2025.md) (§II.C.1, §III.B.3) run their
  own implementation in the same code with Spalding's law at
  $h_{\mathrm{wm}}=0.2\delta$ and no averaging by default, on channel flow at
  $Re_\tau\approx8000$ with the Vreman model, and state that they did not
  see this divergence; their a posteriori averaging study finds no
  systematic gain. They tie the difference to the set-up (§III.C): Gillyns
  et al. filter only the highest mode with weight 10, settings Mukha et al.
  find "more suitable for DNS", and the reported divergence "indicates the
  need for stronger filtering"; when they test the filter as SGS model they
  filter two modes with weight 100. Each statement concerns its own set-up
  (wall law, sampling height, Reynolds number, SGS treatment), so the two
  are not in conflict.
- **Sign of the bump exponent of Nuca et al. (2025).** Eq. (10) (checked
  on the page image) prints the correction as
  $\xi_i\,e^{\sigma_i(\log_{10}Re_y-\mu_i)^2}$ with no minus sign (the
  source's $\xi_i$, $\sigma_i$, $\mu_i$ are $a_i$, $b_i$, $c_i$ above),
  while every printed $\sigma_i$ is positive and the text requires bumps
  that decay away from their centre. Evaluated as printed, the global
  Spalding model of Table IV diverges; with the minus sign its maximum
  relative error over the fitted $Re_y$ range is 0.82 % at $\kappa=0.4$,
  $B=5.5$ and 0.63 % at $\kappa=0.387$, $B=4.21$, consistent with the
  printed bound of 1 % *(compiler check, not in the sources)*. The form
  above uses the minus sign.
- **Fixed-parameter coefficients of Nuca et al. (2025) not reproduced.**
  With the minus sign, $\log_{10}$ in the bumps and the four-decimal
  coefficients of Tables V–VI, the maximum relative error against
  Spalding's law (cubic form) and Reichardt's law (damping lengths 11 and 3,
  $C=B-\kappa^{-1}\ln\kappa$) is about 1.5 % and 0.5 % for the high-Re set
  and 1.8 % and 1.0 % for the classical set, and against the ODE model of
  the classical set ($\kappa=0.41$, $A^+=17$, $B$ from Eq. 1 at
  $y^+=10^5$) about 0.5 %, against the printed bound of
  0.05 %; rounding to four decimals cannot account for errors of order 1 %.
  Tables V–VI are therefore not reproduced by a computation from the
  printed tables *(compiler check, not in the sources)*; whether Eq. (10)
  or the tables differ further from what was run cannot be told from the
  paper.
- Huang et al. (2022c) print the wall condition, Eq. (20) (and Eq. 22),
  as $\partial u/\partial y\rvert_w=\tau_w/(\rho v)$ and $v_t\rvert_w=0$,
  with the italic $v$ of the wall-normal velocity in the same line; a
  velocity gradient requires the kinematic viscosity there
  *(compiler check, not in the sources)*. They write the wall stress
  $\tau_u$ in the text and $\tau_w$ in Eq. (20).
- **Other printed items of Nuca et al. (2025).** The Fig. 7 caption puts
  the high-Re models on top and the classical ones below, while the panel
  labels say the reverse; §V calls the global model's regression "10
  coefficients" where Table IV prints 15 numbers per model (10 slopes and
  5 intercepts); the channel test uses a relative tolerance of $10^{-4}$
  and the airfoil test $10^{-3}$, without comment; Fig. 2 shows at most 5
  Newton iterations in one snapshot, Table VIII a maximum of 10 over the
  run, which are compatible.

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
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.B.1, Eqs. (1)–(2); §III.B, Eq. (12), Fig. 10 (arXiv v3).
- [Duan & Wang (2024)](/sources/duan-2024.md) — §4, Fig. 4.
- [Constant et al. (2024)](/sources/constant-2024.md) — §1; §3.1–3.2, Eqs. (5)–(11); §4.1–4.2, Figs. 10–11; §5.1–5.2, Figs. 12–15; §6.1, Figs. 18–25, Table 3; §6.3, Table 9; §7 (HAL author manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.2, Eqs. (9)–(15); §3.2; §3.3, Figs. 16–20 (HAL accepted manuscript).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §II.C.1, Eqs. (5)–(6); §III.A; §III.B.3, Tables II–III, Figs. 4–5; §III.C; §IV.A; App. A, Fig. 19 (arXiv v1).
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §3.3, Eqs. (12)–(17), Fig. 1, Alg. 1; §4.1, Table 2; §4.2–4.3, Figs. 8, 10.
- [Wu & Lele (2026)](/sources/wu-2026.md) — §2.2; §6.2 (arXiv v2).
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I–II, Fig. 2; §III–IV, Eqs. (1)–(24), Table I, Fig. 3; §V.A–V.B, Tables II–VI, Figs. 4–7; §VI, Tables VII–VIII, Figs. 8–9; §VII; App. A, Eqs. (A1)–(A3); App. B.
- [Husson et al. (2024)](/sources/husson-2024.md) — §3.1–3.2; §4.2.2; §4.3.2.
- [Bose & Park (2018)](/sources/bose-2018.md) — §2.1, Eqs. (3), (6)–(8), Fig. 3; §2.3; §2.5, Eq. (17); §4.1; §4.3; §4.4.
- [Heinz (2020)](/sources/heinz-2020.md) — §3.1, Eq. (21).
- [Lv et al. (2021)](/sources/lv-2021.md) — §I; §II B 4; §IV B 2, Fig. 17.
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §1; §2.2, Eqs. (6)–(7); §3.2, Eq. (9); §4.4–4.6, Figs. 5–7.
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I, Eqs. (1)–(5); §II C, Eqs. (14), (17), (20); §III A, Table I; §III B, Figs. 4–6; §III C, Fig. 7; §III D, Eqs. (21)–(22), Fig. 8; §IV.
- [Zhang et al. (2022e)](/sources/zhang-2022-i.md) — §II A, Eq. (3); §III A, Fig. 4b.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §2.4–2.6, Eqs. (33)–(37); §3.1, Fig. 13; §3.2, Eq. (58); §3.4, Figs. 26–27; §4.
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §1; §2.3, Eqs. (2.17)–(2.20); §4.1–4.3, Eqs. (1.1), (4.2), Figs. 4–5, 7; §5; §6; Table 1.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §II.5, Table 2.
- [Hu et al. (2024)](/sources/hu-2024.md) — §1; §3; §4, Eq. (5); §5, Tables 1–2; §6.1–6.2, Figs. 3–12; §7.
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.2.2, Eqs. (3)–(7); §2.3; §3.2, Figs. 13–16.
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.5; §3.1; §5 (log-law wall conditions of the first channel LES; historical).
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §3.3, Fig. 13 (ODT near-wall closure set beside the wall-stress model; passing).
