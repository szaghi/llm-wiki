---
type: Method
title: "Non-equilibrium wall models"
description: "Wall-stress models of wall-modelled LES that keep unsteadiness, convection or pressure gradient in the inner layer: the thin-boundary-layer equations and the reduced eddy viscosity that avoids double counting, pressure-gradient scalings, the integral bound on equilibrium validity, the integral and wall-model-integrated forms, their evidence against equilibrium models and their cost."
status: established
aliases: [NEQWM, non-equilibrium wall model, nonequilibrium wall model, TBLE wall model, thin-boundary-layer-equation wall model, two-layer zonal wall model, integral wall model, wall-model integrated LES, integrated wall model]
tags: [wall-model, wmles, boundary-layer, separated-flow]
timestamp: 2026-10-29T10:04:00Z
---

# Non-equilibrium wall models

A non-equilibrium wall model is a wall-stress boundary condition of
[wall-modelled LES](/methods/wall-modelled-les.md) whose inner-layer model
keeps some of the terms that the [equilibrium wall model](/methods/equilibrium-wall-model.md)
drops: the time derivative, the wall-parallel convection and the
pressure gradient of the thin-boundary-layer equations. In the review of
[Bose & Park (2018)](/sources/bose-2018.md) (§2.1) the equilibrium model is
the special case of the thin-boundary-layer-equation (TBLE) model in which
only the wall-normal diffusion of momentum is retained, so that the total
stress is constant across the modelled layer; the non-equilibrium forms
restore the rest, at a cost and with a consistency problem of their own
(below). [Heinz (2020)](/sources/heinz-2020.md) (§3.1, Eq. 21) draws the same
hierarchy. Other routes to non-equilibrium effects in this bundle have their
own pages: the relaxation equation of the
[LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
and the pressure-gradient, separation and spanwise-forcing classes of the
[building-block-flow wall model](/methods/building-block-flow-wall-model.md).

Page-local notation: $U_i(x,y,z,t)$, $i=1,3$, the wall-parallel velocity of
the inner-layer (wall-model) solution between the wall and the matching
height $h_{\mathrm{wm}}$; $U_{\mathrm{LES},i}$ the LES velocity at
$h_{\mathrm{wm}}$ (the source's $y^*$); $\nu_t$ the inner-layer eddy
viscosity; $U_\infty$ the free-stream velocity at the edge.

## The thin-boundary-layer equations

Bose & Park (2018, §2.1, Eqs. 4–5) write the incompressible inner-layer
model as

$$\frac{\partial U_i}{\partial t}+\frac{\partial(U_iU_j)}{\partial x_j}+\frac1\rho\frac{\partial p}{\partial x_i}=\frac{\partial}{\partial y}\left[(\nu+\nu_t)\frac{\partial U_i}{\partial y}\right],\qquad i=1,3,$$

with $U_i=0$ at the wall and $U_i=U_{\mathrm{LES},i}$ at $h_{\mathrm{wm}}$, a
pressure independent of $y$ (taken from the LES), the wall-normal velocity
from continuity, and $\tau_{w,i}=\mu\,\partial U_i/\partial y$ at the wall.
Dropping the left-hand side leaves the equilibrium stress balance. In
compressible flow mass and energy conservation are no longer trivial, and
the compressible extensions (Kawai & Larsson 2013; Park & Moin 2014, as
cited) solve the full compressible Navier–Stokes equations in the
wall-model domain.

Heinz (2020, §3.1, Eq. 21) writes the same balance as
$2\,\partial[(\nu+\nu_t)S_{i2}]/\partial y=DU_i/Dt+\partial(p/\rho+2k/3)/\partial x_i\equiv F_i$
($i=1,3$; the isotropic part of the modelled stress is carried with the
pressure) and distinguishes three uses: the PDE form, solved on an extra grid
between the wall and $h_{\mathrm{wm}}$ with the LES velocity there as
boundary condition; the ODE form, in which $F_i$ is evaluated from the LES
solution; and $F_i=0$, the equilibrium model. In the thin layer
$2S_{i2}=\partial U_i/\partial y$ for $i=1,3$, so the two printed forms are
the same equation *(compiler check, not in the sources)*.

[Lv et al. (2021)](/sources/lv-2021.md) (§I) describe the full model as the
three-dimensional RANS equations solved in the wall layer, after Park & Moin
(2014) and Lozano-Durán et al. (2020) as they cite them.
[Zangeneh (2021)](/sources/zangeneh-2021.md) (§II.B, Fig. 1) uses a
two-layer form inside an SST-IDDES: an inner RANS layer on an
auxiliary grid refined in the wall-normal direction and embedded in the
coarse outer LES mesh, forced at each step by the instantaneous LES
velocity, density and temperature at the matching point and returning $\tau_w$
and the wall heat flux as Neumann conditions; following Kawai & Larsson, as
cited, the matching point is not the first off-wall LES node (see
[detached-eddy simulation](/methods/detached-eddy-simulation.md) for IDDES).

## Double counting: reducing the inner-layer eddy viscosity

Once convection is kept, the unsteady inner-layer solution resolves part of
the Reynolds stress, and a full mixing-length eddy viscosity counts it twice,
which over-predicts the skin friction. Bose & Park (2018, §2.1, Eqs. 9–10)
review three corrections.

- **Reduced von Kármán constant** (Wang & Moin 2002, as cited): matching
  the stress at $h_{\mathrm{wm}}$ to the unresolved (SGS) stress of the LES
  gives a model constant
  $$\kappa_{\mathrm{wm}}=\frac{\nu_{\mathrm{sgs}}(h_{\mathrm{wm}})/\nu}{h^+_{\mathrm{wm}}\left[1-e^{-h^+_{\mathrm{wm}}/A^+}\right]^2},$$
  with $\nu_{\mathrm{sgs}}$ the LES eddy viscosity (page-local). Bose & Park
  print the numerator as $\nu_{\mathrm{sgs}}(h_{\mathrm{wm}})$, without the
  factor $1/\nu$ (Qualifications); it is restored here from their mixing
  length (Eq. 6) in wall units with the squared van Driest factor of Eq. (9),
  $\nu_t/\nu=\kappa y^+(1-e^{-y^+/A^+})^2$, since $\kappa$ is dimensionless
  *(compiler check, not in the sources)*.
- **Linear blending** (Kawai & Larsson 2013, as cited): they showed the
  constant above to be potentially inaccurate at high Reynolds number,
  argued that $\kappa$ need not be uniform in $y$ — as the wall-parallel
  spacings grow in wall units the inner grid cannot carry resolved stress, so
  $\kappa$ should return to its nominal value towards the wall — and blend
  the nominal value with the reduced one linearly, with an $O(1)$
  prescribed coefficient ("linear $\kappa(y)$").
- **Dynamic correction** (Park & Moin 2014, as cited): the coefficient of
  the blending was found flow- and mesh-dependent, and is replaced by
  $$\mu_t^{\mathrm{wm}}(y)=\mu_t^{\mathrm{neq}}(y)+\rho\frac{R^{\mathrm{res}}_{ij}S^d_{ij}}{2S^d_{ij}S^d_{ij}}(y),\qquad \mu_t^{\mathrm{neq}}=\rho(\kappa y)^2\lvert S\rvert D(y),$$
  with $R^{\mathrm{res}}_{ij}$ the Reynolds stress resolved by the
  inner-layer solution, $S^d_{ij}$ its deviatoric mean strain and $D(y)$ a
  damping function (page-local $\mu_t^{\mathrm{wm}}$, $\mu_t^{\mathrm{neq}}$,
  $D$); the second term removes the eddy viscosity of the resolved
  inner-layer turbulence. Heinz (2020, §3.1) writes the same correction as
  $\nu_t=\nu_{t,\mathrm{tot}}-\nu_{t,\mathrm{res}}$ and lists the prescribed
  total viscosity among the three design parameters of WMLES, with the
  exchange location (a fraction of an unknown boundary-layer thickness) and
  the mesh distribution.

## Pressure gradient without convection

Bose & Park (2018, §2.1, Eq. 11) cite wall laws scaled with a
pressure-gradient velocity (Manhart et al. 2008; Duprat et al. 2011; Maheu
et al. 2012; after Simpson 1983, as cited),
$u_p=\lvert\nu\rho^{-1}\partial\langle p\rangle/\partial x\rvert^{1/3}$ and
$u_{\tau p}=\sqrt{u_\tau^2+u_p^2}$, with the mixed wall distance
$yu_{\tau p}/\nu$ (page-local symbols). They predict better than the
equilibrium form, but Hickel et al. (2012), as cited, argue that keeping
the pressure gradient without the convective and unsteady terms is
inconsistent with the outer momentum equation, whose Bernoulli limit balances
the two; Bose & Park temper this, saying that the mixed scaling of Duprat et
al. may still improve the wall stress. The same velocity scale $u_p$ appears in
the adverse-pressure-gradient analysis of [Knopp (2022)](/sources/knopp-2022.md), on the
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
page.

**An idealized pressure-gradient wall condition.** [Zhou & Bae (2024)](/sources/zhou-2024-b.md)
(§2.2.2, Eqs. 3–9) keep exactly this term, and only it, in an idealized
wall condition built to isolate the SGS model from the wall model on the
[Gaussian bump](/benchmarks/gaussian-bump.md). From the thin-boundary-layer
equations without unsteadiness and convection, integrated across the first
off-wall cell (centre at $y=h_{\mathrm{wm}}$, velocity $u_{\mathrm c}$ there),
the no-slip wall carries an effective wall eddy viscosity
$\nu_{t,w}$ calibrated by a running time average (breve; $\nu_{t,w}$ and
$\breve u_{\mathrm c}$ as in registry §11; the source writes an
overbar) so that the mean stress equals the DNS value
$\tau^{\mathrm{DNS}}_w$:
$$\breve\nu_{t,w}\approx\frac{\tau^{\mathrm{DNS}}_w+\tfrac12h_{\mathrm{wm}}\,\breve{(\partial_xp)}}{\rho\,\breve u_{\mathrm c}/h_{\mathrm{wm}}}-\nu,\qquad
\tau_{w,i}=\rho\nu\left(1+\frac{\breve\nu_{t,w}}{\nu}\right)\frac{\partial u_i}{\partial y}\bigg|_w-\frac{h_{\mathrm{wm}}}{2}\frac{\partial p}{\partial x_i},\quad i=1,3,$$
with $\nu_{t,w}$ clipped at zero to avoid abnormally large stresses at
separation and reattachment (clipping occurs only for $0<x/L<0.7$, below
13% of the time on average; $L$ the bump width). Dropping the pressure term
gives their equilibrium counterpart (see the
[equilibrium wall model](/methods/equilibrium-wall-model.md)). The two are
"idealized equilibrium and non-equilibrium wall models tailored to the
present flow configuration", not predictive models, since they consume the
DNS mean wall stress. *(Compiler check, not in the sources: integrating
$\rho(\nu+\nu_{t,w})\partial u/\partial y=\tau_w+y\,\partial p/\partial x$
from the wall to $h_{\mathrm{wm}}$ gives
$\rho(\nu+\nu_{t,w})u_{\mathrm c}/h_{\mathrm{wm}}=\tau_w+\tfrac12h_{\mathrm{wm}}\partial p/\partial x$,
consistent with the printed forms.)*

**An explicit pressure-gradient wall function on immersed boundaries.**
[Yan et al. (2024)](/sources/yan-2024.md) (§I, §II C, Eqs. 22–31) call their
model an explicit non-equilibrium model (NEM) although it keeps, of the
thin-boundary-layer source $\partial_tU+\rho^{-1}\partial_xp+\partial_y(UV)$
(their Eq. 22b, in the wall-tangential and wall-normal directions of a
curved body), only the pressure gradient; their introduction defines the
equilibrium model (EM) by the diffusion term alone and the NEM by the
added pressure gradient and convection (§I). Integrating
$\partial_y[(\nu+\nu_t)\partial_yU]=\rho^{-1}\partial_xp$ from the wall to
the probe height $h_{\mathrm{wm}}$, about three grid spacings off a
diffused-interface [immersed boundary](/methods/immersed-boundary-method.md),
gives the velocity gradient there,
$$\left.\frac{\partial U}{\partial y}\right|_{h_{\mathrm{wm}}}=\frac{\tau_w+h_{\mathrm{wm}}\,\partial p/\partial x}{\rho(\nu+\nu_t)},\qquad \frac{\nu_t}{\nu}=\kappa y^+\left(1-e^{-y^+/19}\right)^2,\ \kappa=0.41$$
(Eqs. 23–24; $x$ here the local tangential direction), and the wall stress
comes explicitly from a power law, Werner–Wengle in zero or favourable
gradient and the adverse-pressure-gradient power law of Wilhelm et al. (as
cited) with a separation indicator in adverse gradient (formulas on the
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
page). The gradient serves only to extrapolate the probe velocity to a slip
target at the wall (see [slip-wall models](/methods/slip-wall-model.md)).
Their Table I classifies seven earlier wall-modelled diffused-interface
methods, two of which solve the boundary-layer equation by finite
differences, and they present theirs as the first use of explicit
non-equilibrium wall functions on a diffused interface, these having been
applied only to sharp interfaces before (§I). Side by side: Bose & Park
(2018, §2.1; above) cite Hickel et al. (2012) arguing that keeping the
pressure gradient without the convective and unsteady terms is inconsistent
with the outer momentum equation; Yan et al. keep only the pressure
gradient and do not discuss that argument.

**A generalized wall function applied in two steps (flux reconstruction).**
[Gao et al. (2025b)](/sources/gao-2025-b.md) (§II C2–C3, Fig. 1, Eqs.
29–32) keep the pressure gradient, and only it, through the generalized
wall function of Shih, Povinelli & Liu (2003), which splits the
tangential velocity into a wall-stress part $U_1$ and a pressure-gradient
part $U_2$ with the scales $u_\tau$, $u_p$ and $u_c=u_\tau+u_p$ (the law,
its profile functions $f_1$, $f_2$ and the symbols are on the
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
page). To avoid iterating for $u_\tau/u_c$ they apply it in two steps at
each wall flux point of a high-order
[flux reconstruction](/methods/flux-reconstruction.md) solver, with
$\boldsymbol U_t$ the tangential velocity at the first solution point
inside the wall-adjacent element and $p_w$ the wall pressure:

1. $u_\tau$ from the equilibrium law of Allmaras, Johnson & Spalart,
   inverted explicitly by a piecewise fit (see the
   [equilibrium wall model](/methods/equilibrium-wall-model.md));
2. $u_p$ from the wall-pressure gradient and $U_2$ from $f_2$;
3. the wall-stress part
   $U_1=\Bigl|\,\lvert\boldsymbol U_t\rvert-\dfrac{\boldsymbol U_t\cdot\partial p_w/\partial x_i}{\lvert\boldsymbol U_t\cdot\partial p_w/\partial x_i\rvert}\,U_2\Bigr|$
   (Eq. 30), from which $u_\tau$ is recomputed with the same fit;
4. the corrected wall stress, as printed (Eq. 31),
   $$\tau_{w,i}=\left(\frac{U_{t,i}}{u_c}-\frac{\nu}{\rho}\frac{\partial p_w/\partial x_i}{u_c^3}f_2(y_p^+)\right)\frac{u_c}{u_\tau f_1(y^+_\tau)}\,\rho u_\tau^2,$$
   imposed as the wall-normal viscous flux, $\boldsymbol n\cdot\hat{\boldsymbol F}^v=-\boldsymbol\tau_w$
   (Eq. 32), with no slip kept at the wall.

In the procedure $u_\tau$ comes from the inverse of the Allmaras et al.
law and the profile $f_1$ of Eq. (31) from Shih et al.'s fit. On the
[periodic hill](/benchmarks/periodic-hill.md) at $Re=10\,595$ (the paper does not state the reference length and velocity; Mesh 1,
$32\times12\times16$ elements; Mesh 2, $48\times24\times24$; quadratic
27-node hexahedra; polynomial degree $N=2$–4; Vreman SGS model) the mean
streamwise velocity at the hill top shows a minor discrepancy for $N=2$
and "excellent agreement" for $N=4$, the skin friction approaches the DNS
of Krank et al. (as cited) as $N$ increases, separation and reattachment
agree with the references, and the $L_2$ errors of the mean velocity and
the Reynolds stress at ten stations against the PIV of Rapp & Manhart (as
cited) decrease with $N$ and with mesh refinement (§III B1, Figs. 8–13).
At $Re=37\,000$ ($N=3$, Mesh 1) the mean velocity agrees with experiment
and with the LES of Gloerfelt & Cinnella (as cited, $512\times256\times256$
points) except a slight deviation of the wall-normal velocity in the
recirculation, and the shear-layer intensities are over-estimated, as in
that LES (§III B2, Figs. 14–15). The authors call their meshes
"significantly coarser than those employed by other researchers", too
coarse at the crest to resolve the boundary layer (§III B, Table I). The
hill runs use only the generalized law, so they carry no
equilibrium-against-non-equilibrium comparison. Side by side with
Hickel et al.'s argument cited by Bose & Park (above): Gao et al. keep the
pressure gradient without the convective and unsteady terms and do not
discuss that argument.

[Gao et al. (2025)](/sources/gao-2025.md) (§I.A, Eq. 1) print the
thin-boundary-layer equations after Cabot & Moin (as cited), with the
equilibrium model dropping all terms but the wall-normal diffusion,
and run only the equilibrium form; adding pressure-gradient source terms
to their wall-model equations is named as future work (§IV; see
[slip-wall models](/methods/slip-wall-model.md)).

## When is equilibrium enough? An integral bound

Bose & Park (2018, §2.1, Eqs. 7–8) give their own von Kármán integral
analysis, "similar to" Hoffmann & Benocci (1995) as they cite it. Integrating
the streamwise TBLE from the wall to $h_{\mathrm{wm}}$ with continuity and the
inviscid outer equation gives

$$u_\tau^2=\frac{\tau(h_{\mathrm{wm}})}{\rho}+\frac{\partial}{\partial t}\int_0^{h_{\mathrm{wm}}}(U_\infty-U)\,dy+\frac{\partial U_\infty}{\partial x}\int_0^{h_{\mathrm{wm}}}(U_\infty-U)\,dy+\frac{\partial}{\partial x}\int_0^{h_{\mathrm{wm}}}U(U_\infty-U)\,dy+(U_\infty-U)\,V\Big|_{h_{\mathrm{wm}}},$$

with $\tau$ the total shear stress and $V$ the wall-normal velocity
(page-local); as $h_{\mathrm{wm}}\to\delta$ the first and last terms vanish
and the von Kármán momentum integral is recovered. With $U\le U_\infty$ the
integrand of the pressure-gradient term is at most $U_\infty$, so its ratio
to $\tau_w$ is bounded by the Clauser pressure-gradient parameter times
$h_{\mathrm{wm}}/\delta^*$ (Eq. 8); in the notation of the adverse-pressure-gradient page,
$\lvert\cdot\rvert\le\lvert\beta_{RC}\rvert\,h_{\mathrm{wm}}/\delta^*$ with
$\beta_{RC}=(\delta^*/\tau_w)\,dP/dx$ *(compiler check, not in the sources:
the source writes the bound with the Clauser parameter, which it does not
define explicitly, and the sign is discussed under Qualifications)*. Two consequences
are drawn: the pressure-gradient effect on the modelled stress can be made
negligible by keeping $h_{\mathrm{wm}}/\delta^*$ small — "the outer LES
captures the pressure gradient" — and the matching height for which the
equilibrium model is valid may depend on the pressure-gradient parameter,
unlike fixed-fraction recommendations such as $h_{\mathrm{wm}}\approx0.1$–$0.2\delta$
(Larsson et al. 2016, as cited). The argument fails near separation, where
$\tau_w\to0$. [Goc et al. (2021)](/sources/goc-2021.md) (§2.2) cite this
bound to justify their equilibrium model (see
[equilibrium wall model](/methods/equilibrium-wall-model.md)).

From wall-law data rather than a momentum balance, Knopp (2022) finds that
the log layer ends at a height that falls with the inner-scaled pressure
gradient, below $0.08\delta$ for $\Delta p_s^+>0.015$ and $\beta_{RC}>12$ (see the
adverse-pressure-gradient page).

## Integral wall model

The integral wall model of Yang et al. (2015) is cited by two sources.
Bose & Park (2018, §2.1, Eq. 12) give its profile, linear in the viscous
sublayer and, in the overlap region,

$$\frac{\langle u\rangle}{u_\tau}=B_{\mathrm I}+\frac1\kappa\ln\frac{y}{h_{\mathrm{wm}}}+A_{\mathrm I}\frac{y}{h_{\mathrm{wm}}},$$

($A_{\mathrm I}$, $B_{\mathrm I}$ page-local, the source's $A$, $B$), with 11
coefficients fixed by boundary conditions, continuity and the vertically
integrated (von Kármán) momentum equation: algebraic cost with
non-equilibrium effects, extended to roughness drag and to immersed
boundaries. Lv et al. (2021, §I, §II B 4) describe it as a set of nonlinear
algebraic equations "whose derivation is long", solved outside the LES, at a
cost usually below 5 % of the LES (as they cite it). The relation of its
time filter and buffer-layer slope to LaRTE is on the
[LaRTE](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
page.

## Wall-model-integrated LES

Lv et al. (2021) remove the wall-model solver altogether. They locate three
problems in its being outside the LES, "the root of many issues in WMLESs"
(§I, Fig. 2): cost and coding effort; an ambiguous LES solution in the
wall-adjacent cell — reconstructing it with the scheme's polynomials and the
modelled wall gradient gives, for a linear reconstruction,
$U_w=U_{\mathrm{LES}}-\tau_wh_{\mathrm{wm}}/(\rho\nu)$, a negative wall velocity, while
taking the wall-model profile leaves a discontinuity at the first off-wall
point; and conflict with high-order schemes, to which they attribute the
oscillations of the discontinuous Galerkin (DG) WMLES of Frère et al. (2017),
as cited.

**Reconstruction in a law-of-the-wall basis** (§II A, Eqs. 1–6). In the
wall-adjacent cell the wall-parallel velocity $u_t(y)$ (page-local) is
reconstructed in a basis in which one monomial is replaced by the log law,

$$u_t=a_w\phi_w+a_1y+a_0,\qquad \phi_w(y)=\frac1\kappa\ln\frac{y+y_0}{y_0},\qquad \frac{\tau_w}{\rho}=a_w^2+\nu a_1,$$

with $\kappa=0.41$, $y_0$ a viscous or roughness length and $a_w$ identified
with $u_\tau$ (page-local $u_t$, $a_0$, $a_1$, $a_w$, $\phi_w$, $y_0$). The
LES solver computes all coefficients from the filtered Navier–Stokes
equations, convection and pressure gradient included, and the wall flux
follows from them "no different from computing a flux on an internal cell's
surface": there is no matching height, no wall-model grid and no external
solver. A purely linear basis would give $\tau_w/\rho=\nu a_1$, which
under-estimates the stress when the wall layer is not resolved; when it is
resolved, $\phi_w$ degenerates to a linear term. For an order-$p$ scheme
the general basis is $\{y^i,\ i=0,\dots,p-2;\ \text{log term}\}$ (Eq. 8),
read as a Taylor expansion about the log law in which only the log term and
$y$ carry wall stress, since $dy^i/dy=0$ at the wall for $i\ge2$; for their
third-order scheme ("P3", whose wall-parallel factors are quadratic, Eq. 11;
polynomial degree $N=2$ in the registry's sense *(compiler check, not in the
sources)*) the basis is $\{1,y,\phi_w\}$. The authors state that the
integral wall model "truncates at $p=3$", so that with this basis "[one] is
practically applying the integral wall model — but without an algebraic
solver outside the LES" (§II B 3), and that the linear coefficient absorbs the
non-equilibrium effects. The inspiration is the von Kármán–Pohlhausen
polynomial profile, $u_t/U_\infty=\sum_{i=1}^4\beta_i(y/\delta)^i$ (Eq. 7,
page-local $\beta_i$). Two wall-parallel components and the
wall-parallel quadratic factors of the P3 scheme give the stress components
of Eqs. (9)–(12), e.g. $\tau_{w,x}/\rho=\sqrt{a_w'^2+a_w''^2}\,a_w'+\nu a_1'$
(primes for the $x$ and $z$ components).

They distinguish the method from two DG predecessors (§II B 2): Frère et al.
(2017) solved the polynomial coefficients in the LES but took the wall flux
from the log law; Lv, Yang, Park & Ihme (2021, Comput. Fluids, as cited)
*added* a log basis without removing a polynomial one, so its coefficient
had to be solved outside the LES; here a basis is *replaced*. The dynamic slip
wall of Bose and co-workers is credited as "the first attempt" to remove
"RANS legacies" from WMLES but said to have "numerical difficulty in some
codes" (§II B 1; see [wall-modelled LES](/methods/wall-modelled-les.md)).

**Implementation and tests** (§III–IV). The solver is SUPES, a DG solver
extended with a piecewise-parabolic finite-volume scheme so that only the
wall-adjacent cells use the DG variational form; local Lax–Friedrichs
convective flux, symmetric interior-penalty viscous flux, third-order
Runge–Kutta, [Vreman](/methods/vreman-model.md) SGS model with $Pr_t=0.9$,
and a strongly imposed isothermal no-slip wall state whose viscous momentum
flux is set from the stress above.

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md) on uniform
  grids without near-wall refinement (Table I): $Re_\tau=2000$ on $32^3$,
  $64^3$ and $128^3$ ($y_1^+=125$, 63, 31, with $y_1$ the first-cell height,
  page-local), $Re_\tau=180$ on $64\times128\times64$ ($y_1^+=2.81$, wall
  resolved) and $Re_\tau=50\,000$ on $64^3$ ($y_1^+=1.6\times10^3$). The mean
  velocity "follows the DNS data closely, irrespective of the grid
  resolution" at $Re_\tau=2000$, and the log law is recovered at all three
  Reynolds numbers; the rms velocities and the shear stress approach DNS
  under refinement (Figs. 5–6, 11). When the wall layer is resolved the
  linear term "would take over" and the profile follows DNS into the viscous
  sublayer and buffer layer (Fig. 12). The log coefficient $a_w'$ tracks the
  first-cell velocity, and the linear coefficient $a_1'$ correlates, in a
  joint PDF, with the non-equilibrium measure
  $\mathcal N_x=\boldsymbol u\cdot\nabla u+\rho^{-1}\partial p/\partial x$ at
  the first off-wall point (page-local $\mathcal N_x$) on all three grids
  (Figs. 7–10).
- [Periodic hill](/benchmarks/periodic-hill.md) at $Re_h=10\,595$ (§IV B 2,
  Table II): the integrated model on $64\times32\times32$ (Hill-C) and $64^3$
  (Hill-R) cells against the equilibrium model of Kawai & Larsson (2012), as
  cited, on $64^3$ (Hill-Equil). Grid resolution "has a more notable impact
  on the results than the wall model": Hill-C is worse, because the coarse
  grid does not capture the pressure force (Fig. 16), as Xu et al. found
  when pressure is the dominant momentum sink (as cited). For the skin
  friction, "the acid test for a wall model", neither model captures $C_f$
  between $x/H\approx0$ and 2, but Hill-R gives "considerable more accurate
  estimates" than Hill-Equil on the leeside and near the crest (Fig. 17; $C_f$
  printed as $\tau_w/(2\rho U_b^2)$).

Bose & Park (2018, §4.3) write of the hill that slip, equilibrium and
non-equilibrium models agree favourably with DNS, the last slightly better
near separation, and that "the differences may be due more to" the
outer-LES numerics than to the wall models.

The hill also serves as a reference outside wall modelling.
[Li et al. (2022)](/sources/li-2022-k.md) (§III B, Figs. 7–11) compare a
Reynolds-stress-model-based dynamic IDDES on $160\times115\times60$ cells
(first cell at $\Delta y^+<1$) with the experiment of Breuer et al. and with
the DNS, wall-resolved LES and WMLES of Balakumar, Park & Pierce, as cited;
that WMLES ($128\times128\times72$, second-order central differences,
dynamic Smagorinsky) uses the non-equilibrium wall model of Park & Moin.
Near the lower wall at $x/h=4$ both hybrid variants agree with the WMLES
rather than with the DNS, wall-resolved LES and experiment, and the
near-wall resolved stresses of the dynamic variant fall in the band of the
references and close to the WMLES (see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)). The
comparison involves no wall model of their own.

## Evidence against equilibrium models

| Flow | Finding | Source |
|---|---|---|
| [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md), inflow $Re_\tau\approx2000$ | full non-equilibrium TBLE outperforms equilibrium models in the bubble and the recovery (Avdis et al. 2009; Park 2017, as cited) | Bose & Park (2018, §4.3) |
| [Periodic hill](/benchmarks/periodic-hill.md), $Re_h=10\,595$ | non-equilibrium slightly better near separation; differences possibly from outer numerics | Bose & Park (2018, §4.3) |
| Periodic hill, $Re_h=10\,595$ | integrated model better $C_f$ on the leeside and near the crest than the equilibrium model; grid matters more | Lv et al. (2021, §IV B 2) |
| Mach 1.7 oblique [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md) | the non-equilibrium model with linear $\kappa(y)$ of Kawai & Larsson (2013), as cited: skin friction and mean velocity "agree well" with the experiment of Souverein et al. (2010) and the reverse-flow probability is "well captured"; Fig. 6b also shows a non-equilibrium model with constant $\kappa=0.4$ (Balaras et al. 1996) | Bose & Park (2018, §4.4, Fig. 6b) |
| H-type transitional boundary layer | the non-equilibrium model of Park & Moin (2014), with the wall model switched off by a transition sensor upstream, predicts the transition location well (Fig. 6a) | Bose & Park (2018, §4.1) |
| Aérospatiale-A airfoil, $Re_c=2.1\times10^6$ | algebraic, equilibrium and Kawai–Larsson non-equilibrium models disagree on the trailing-edge separation, "highlighting" the sensitivity of mild adverse-gradient separation to wall-model details | Bose & Park (2018, §4.3) |
| Bachalo–Johnson transonic bump | WM-LES with equilibrium and non-equilibrium models (Iyer et al., as compiled) cannot match both the shock and the reattachment $C_f$ maxima by choosing the exchange location (first or third point) | Heinz (2020, §5.3, Table 5, Fig. 14) |
| Mach 2.28 oblique shock/boundary-layer interaction, $8^\circ$ deflection | equilibrium ODE model coupled with no slip kept: negative $C_f$ in the bubble, but interaction length $L_{\mathrm{int}}/\delta_r=7.0$–5.0 (coarse to fine; nominal impingement to reflected-shock foot over the inflow 99 % thickness; $L_{\mathrm{int}}$, $\delta_r$ registry §11) against 3.3 wall-resolved and 4.18 experimental; oversizing attributed to the wall model and to SGS plus shock-capturing dissipation; non-equilibrium improvements named as future work | [De Vanna et al. (2022)](/sources/devanna-2022.md) (§4.6, §5) |
| Mach 7.2, $8^\circ$ compression ramp | equilibrium ODE model: early pressure rise on the coarse grid, minimum $C_f$ above DNS; the imbalance between tangential pressure gradient and convection, which the equilibrium model omits, named as a possible cause (not tested) | [van Noordt et al. (2022)](/sources/vannoordt-2022.md) (§3.4) |
| [Gaussian bump](/benchmarks/gaussian-bump.md), $Re_L=2\times10^6$, idealized conditions fed by the DNS mean wall stress | the pressure-gradient condition "notably improves" the bubble measured from $C_f$ for the eddy-viscosity SGS models, but changes the bubble measured from the first-cell velocity little; the SGS model and the mesh still largely set the separation length, and the wall condition has "a negligible impact on the convergence behavior"; Iyer & Malik (as cited) found a non-equilibrium model only marginally better than an equilibrium one on the same bump | [Zhou & Bae (2024)](/sources/zhou-2024-b.md) (§1, §3.2, Figs. 13–16) |
| [Circular cylinder](/benchmarks/circular-cylinder-wake.md), $Re_D=3.9\times10^3$ and $1.4\times10^5$; [square cylinder](/benchmarks/square-cylinder-flow.md), $Re_D=2.2\times10^4$; sixth-order compact finite differences with implicit spectral vanishing viscosity, diffused-interface immersed boundary | the pressure-gradient wall function captures separation, shear-layer transition, shedding and the multiscale wake at $Re_D=3.9\times10^3$, the variant without pressure gradient (Werner–Wengle only) does not (Fig. 7); bulk values at $3.9\times10^3$ $C_D=1.02$, $C_{L,\mathrm{rms}}=0.113$, $L_r/D=1.42$, $St=0.229$; at $1.4\times10^5$ $L_r/D=0.98$ against LES 0.42–0.62 and experiment 0.44, attributed to flow sensitivity, eddy-viscosity models and the simplified boundary-layer equation; favourable-gradient wall stress under-predicted (Werner–Wengle); on the square cylinder the leading- and trailing-edge bubbles of wall-resolved LES are missed | [Yan et al. (2024)](/sources/yan-2024.md) (§III A–B, Tables II–IV, Figs. 7, 9) |
| Three-dimensional boundary layers (bent square duct; rotating free stream; sudden spanwise pressure gradient) | integral and PDE non-equilibrium models "considerably less sensitive" to the matching location than the ODE equilibrium model (Hu et al. 2023, as cited); in their own LES the algebraic equilibrium model converges to a wall stress that depends on $h_{\mathrm{wm}}$ and is more accurate for small $h_{\mathrm{wm}}$, which they attribute to its unidirectional-flow assumption; on the hump, Park (2017, as cited) found the non-equilibrium model mostly converged on the medium grid, the equilibrium model more slowly and less monotonically | [Hu et al. (2024)](/sources/hu-2024.md) (§1, §6.1, §7) |

Heinz (2020, §5.2, Table 3, Figs. 10–11) compiles WM-LES reattachment
lengths on the hump of 1.035–1.105 against the experimental 1.10, and finds
the double-peak skin-friction structure missed by WM-LES and DES. The
evidence of both reviews is compiled from published work. Hu et al. (2024, §7) recommend wall models with low
sensitivity to the matching location when $h_{\mathrm{wm}}$ is held fixed
during grid refinement, the property they cite for non-equilibrium models.

**Why some sources stay with equilibrium.** De Vanna et al. (2022, §1)
call non-equilibrium wall modelling in LES "still an open problem": the
models they survey (Cabot & Moin, Wang & Moin, Kawai & Asada, Park & Moin,
Suga et al., Zebiri et al., Mettu & Subbareddy, as cited) require
"significant technical complexity and a non-trivial computing cost", are
"frequently invasive at the implementation level" and carry numerous
fitted parameters. They keep an equilibrium ODE model and move the
non-equilibrium burden to the coupling: no slip is retained and the
modelled stress enters through an augmented wall viscosity, which lets the
LES reverse the wall shear in a separation bubble (see the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[wall-modelled LES](/methods/wall-modelled-les.md) pages). [Huang et al. (2022c)](/sources/huang-2022-c.md)
(§I, §II C, §IV) give the same trade-off for a spectral/hp implicit LES:
non-equilibrium (PDE, two-layer) models such as that of Balaras et al.
(1996), as cited, capture adverse pressure gradient and separation but
need a separate near-wall grid, while the algebraic equilibrium model is
"considerably cheaper" though it "cannot completely and correctly solve the
problem of the transfer mechanism of the wall attached vortex in the inner
layer"; they choose the algebraic model, restrict their study to
equilibrium channel flow and leave non-equilibrium flows to future work
(see [wall-modelled LES](/methods/wall-modelled-les.md)). Van Noordt et al. (2022,
§2.5) use the HyWall library, which supports non-equilibrium models through
data at the surface-triangle centroids, but run only its equilibrium model.

**Equilibrium models on a strongly non-equilibrium aircraft flow.** In the
HLPW-4 wall-modelled LES focus group on the
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) configuration
summarized by [Kiris et al. (2023)](/sources/kiris-2023.md) (§II.5,
Table 2), "all groups utilized equilibrium models with adiabatic thermal
conditions" with the exception of one (Table 2 lists no wall model for the
Euler submission W-030). The exception (W-032, PowerFLOW, a
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) code) used a
proprietary "pressure-aware" formulation listed as a non-equilibrium wall
model; no formula is printed. The authors call the ODE-versus-algebraic
variants of the equilibrium model "of no consequence for the present flow".
They suggest that a larger source of discrepancy may be whether the wall
stress is applied at nodes or at cell centres. For the use of equilibrium
modelling in "strongly nonequilibrium flows such as the one being studied
here" they refer to the reviews of Bose & Park (2018) and Larsson et al.
(2016). The workshop does not isolate the effect of the non-equilibrium
model: the remaining load scatter at high angle of attack is attributed to
grid resolution and to the predicted onset of inboard stall (see
[wall-modelled LES](/methods/wall-modelled-les.md)).

## Cost

Bose & Park (2018, §3) put the full non-equilibrium TBLE at about twice the
cost of the baseline LES without wall model, and note that load imbalance
at large processor counts can matter more. Lv et al. (2021, §I, §II B 4),
citing implementation studies for grids of $O(10^6$–$10^7)$ points on up to
256 cores, give 100–150 % overhead for the non-equilibrium model ("$\sim$100 %"
in §I and §V), 30–40 % for the ODE equilibrium model and usually below 5 %
for the integral and algebraic models, and claim "exactly 0 cost" for the
integrated model, whose scalability is "solely determined by the LES
solver"; no timing of the integrated model is shown. On the equilibrium page,
[Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) cite 10–30 % for the ODE model.
Yan et al. (2024, §III A–B, Table V), whose explicit model needs no
inner grid, report 15.04 h of wall clock per $10^5$ steps on 96 cores for
the cylinder at $Re_D=3.9\times10^3$ with the sixth-order scheme and
implicit SVV, against 18.16 h for a second-order scheme with the
[Smagorinsky model](/methods/smagorinsky-model.md) on the same mesh, and
13.2 core-hours per shedding cycle on the square cylinder against about
1058 and 676 h inferred for two wall-resolved LES (as they cite them); the
wall model's own share of the cost is not separated. Gao et al. (2025b,
§III B) time 100 steps of the hill on one core (Mesh 1, 6144 elements,
1024 at the wall): 135.6 s without wall model, 143.8 s with the
equilibrium law and 152.7 s with the two-step generalized law (+6 % and
+12.5 % as printed), which they attribute to the absence of iterations.

## Qualifications

- **Outer relation of Bose & Park (2018).** The text before their Eq. (7)
  prints $\rho^{-1}dp/dx=U_\infty\,dU_\infty/dx$; the steady Euler equation
  gives $\rho^{-1}dp/dx=-U_\infty\,dU_\infty/dx$, and their Eq. (7), which
  also contains the unsteady term, follows from integrating the TBLE with
  the negative sign, so the slip is confined to the inline relation. With
  $dP/dx=-\rho U_\infty dU_\infty/dx$ the middle member of their Eq. (8)
  equals $-\beta_{RC}h_{\mathrm{wm}}/\delta^*$; since the paper does not
  define its Clauser parameter, the bound is stated above in magnitude
  *(compiler check, not in the sources)*.
- Bose & Park (2018) print the reduced constant (their Eq. 9) as
  $\kappa_{\mathrm{wm}}=\nu_{\mathrm{sgs}}(h_{\mathrm{wm}})/\{h^+_{\mathrm{wm}}[1-\exp(-h^+_{\mathrm{wm}}/A^+)]^2\}$,
  which has the dimensions of a kinematic viscosity, without the
  factor $1/\nu$ (above), and write the equilibrium eddy viscosity with a
  damping $D(y)$ multiplying $\kappa u_\tau y$ without saying that it is the
  squared van Driest factor of Eq. (9).
- **Printed items of Lv et al. (2021).** Eq. (3) writes the log basis with
  $\ln\big((y+y_0)/y_0\big)$, Eq. (8) with $\ln\big((y-y_0)/y_0\big)$, which is
  undefined between the wall and $y_0$. Their stress $a_w^2$ follows from
  identifying $a_w$ with $u_\tau$, not from the wall gradient of the basis,
  $\nu\,\partial(a_w\phi_w)/\partial y|_{y=0}=\nu a_w/(\kappa y_0)$; the two agree
  only for $y_0=\nu/(\kappa u_\tau)$, and the paper does not say how $y_0$ is
  set *(compiler check, not in the sources)*. Table II gives Hill-Equil the
  grid of Hill-R ($64^3$) but the first-cell range of Hill-C
  ($\Delta_1/H=0.063$–0.094, against 0.031–0.047 for Hill-R), without comment.
  The discussion of Fig. 15 states that "Hill-C and Hill-Equil capture the
  mean flow very well" and, two sentences later, that "Hill-C … is noticeably
  worse" and "does not do very well in capturing the mean flow". §IV B 1
  refers to "Sec. III" for the argument of Sec. II. The coefficient $a_1'$ is
  normalized by $u_\tau^2/h$ in the Fig. 8 caption and by
  $u_\tau h_{\mathrm{wm}}/h^2$ on the Fig. 9 axis ($h$ the channel half-height),
  although the framework has no matching height.
- The equivalence of the $\{1,y,\phi_w\}$ basis with the integral wall model
  and the zero cost are asserted by Lv et al., not demonstrated against the
  integral model or by timings.
- **Printed items of Yan et al. (2024).** The paragraph after their
  Eq. (32) cites "Eq. (32)" for the velocity gradient, which is Eq. (23),
  and says that the target velocity influences the forcing "in Eq. (3)",
  which appears in Eq. (4); the Fig. 2 caption and §II C call the velocity
  gradient $\partial U/\partial y$ a "pressure gradient". The van Driest
  constant 19 is printed without comment.
- **Printed items of Gao et al. (2025b).** Solving their Eq. (28) for
  $\tau_{w,i}$ gives the second term of Eq. (31) multiplied by $u_p/u_c$,
  a factor that the printed Eq. (31) and Fig. 1 (step 7) omit; Eq. (28)
  writes $f_1(y^+)$ where Eq. (31) writes $f_1(Y^+_\tau)$ in the source's
  symbols *(compiler check, not in the sources)*. $152.7/135.6=1.126$, so
  the printed "12.5 %" is 12.6 % to one decimal *(compiler check, not in
  the sources)*. The $Re=37\,000$ run is printed as "a mesh of only
  128 × 48 × 60 points"; Mesh 1 with $N+1=4$ points per direction gives
  $128\times48\times64$, as the paper's own count $96\times36\times48$ for
  $N=2$ does with 3 *(compiler check, not in the sources)*. Which hybrid
  wall-flux weight is used in each case, how $\partial p_w/\partial x_i$
  is evaluated and whether the input is filtered in time are not stated.
- Lv et al.'s own reference [24], the DG wall-model method of Lv, Yang,
  Park & Ihme (2021), is a different work from the Physics of Fluids paper
  read here.

# Citations

- [Bose & Park (2018)](/sources/bose-2018.md) — §2.1, Eqs. (4)–(12), Fig. 6; §3; §4.1, Fig. 6a; §4.3; §4.4, Fig. 6b.
- [Lv et al. (2021)](/sources/lv-2021.md) — §I, Fig. 2; §II A–C, Eqs. (1)–(12); §III; §IV B 1, Figs. 5–12, Table I; §IV B 2, Figs. 15–17, Table II; §V.
- [Heinz (2020)](/sources/heinz-2020.md) — §3.1, Eq. (21); §5.2, Table 3, Figs. 10–11; §5.3, Table 5, Fig. 14.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §II.B, Fig. 1.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.2.
- [Knopp (2022)](/sources/knopp-2022.md) — §2.4 (pressure-gradient velocity scale); §5.2.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §IV.D.
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §1; §4.6; §5.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §2.5; §3.4.
- [Li et al. (2022)](/sources/li-2022-k.md) — §III B, Table I, Figs. 7–11 (periodic-hill WMLES reference with the Park–Moin model).
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I; §II C; §IV.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §II.5, Table 2 (equilibrium models in HLPW-4; the pressure-aware model of W-032).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §1; §2.2.2, Eqs. (3)–(9); §3.2, Figs. 13–16; §4.
- [Hu et al. (2024)](/sources/hu-2024.md) — §1 (taxonomy; matching-location sensitivity, Hu et al. 2023 and Park 2017 as cited); §6.1; §7.
- [Yan et al. (2024)](/sources/yan-2024.md) — §I, Table I; §II C, Eqs. (22)–(32), Fig. 2; §III A–B, Tables II–V, Figs. 7, 9.
- [Gao et al. (2025b)](/sources/gao-2025-b.md) — §II C2–C3, Eqs. (28)–(32), Fig. 1 (two-step generalized wall function); §III B, Table I (timings); §III B1–B2, Figs. 8–15 (periodic hill).
- [Gao et al. (2025)](/sources/gao-2025.md) — §I.A, Eq. (1) (TBLE, cited); §IV (pressure-gradient extension as future work).
