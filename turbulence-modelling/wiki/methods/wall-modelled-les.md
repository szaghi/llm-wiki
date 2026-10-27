---
type: Method
title: "Wall-modelled large-eddy simulation"
description: "LES that resolves the outer-layer eddies and replaces the near-wall viscous region by a wall-stress model: its definition and cost advantage, the grid-dependent error scaling of mean quantities, the dominance of SGS-model errors, non-monotonic grid convergence, the insufficiency of wall-mesh criteria, grid adaptation, immersed-boundary coupling and wall-slip models, and demonstrations on aircraft, fan stages and separated flows."
status: established
aliases: [WMLES, wall-modeled LES, wall-stress-modelled LES, LES with approximate boundary conditions, IBMLES, immersed boundary-modelled LES]
tags: [wmles, les, wall-model, boundary-layer, separated-flow]
timestamp: 2026-10-27T06:13:00Z
---

# Wall-modelled large-eddy simulation

Wall-modelled LES (WMLES) is [large-eddy simulation](/definitions/large-eddy-simulation.md)
whose grid resolves eddies that scale with the boundary-layer thickness
$\delta$ but not the viscous near-wall region; the no-slip condition is
replaced by a wall-stress (Neumann) boundary condition computed by a wall model
from the LES state at a matching height $h_{\mathrm{wm}}$
([Goc et al. 2021](/sources/goc-2021.md), §2.2;
[Lozano-Durán et al. 2022](/sources/lozanoduran-2022.md), §II.A). Its
point is cost: the grid count no longer depends on the viscous length near the
wall (see [grid-point requirements](/results/les-grid-point-requirements.md)).
In the classification of Larsson et al. (2016), recalled by
[Fowler et al. (2022)](/sources/fowler-2022.md) (§1) and
[Haering et al. (2022)](/sources/haering-2022.md) (§II), wall-stress models,
where the LES extends to the wall, are distinct from
[hybrid RANS/LES](/definitions/hybrid-rans-les.md), where a RANS region covers
the inner layer. This page covers the wall-stress kind.
The vocabulary is not uniform across the sources: [Delassaux et al. (2023)](/sources/delassaux-2023.md)
(§4.1) describe WMLES as using "a RANS model only in the innermost part of the
wall boundary layer and then switch to a LES model", i.e. the hybrid kind in
the classification above, and name separately "wall-function LES" (WFLES),
which resolves the boundary layer with a number of cells independent of the
Reynolds number and puts the first node at $y^+>30$, as they cite it.
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Introduction) draw the same
line between hybrid LES/RANS and "wall-flux" modelling, and subdivide the
latter into models based on the law of the wall, on the full unsteady
three-dimensional RANS equations, and on wall-normal diffusion only (ODEs),
plus the coefficient-free dynamic slip model. The modelled region is the inner
layer up to about 10 % of $\delta$ ([Hoy & Bermejo-Moreno 2022](/sources/hoy-2022.md),
§1, as they cite it) or $y/\delta\lesssim0.15$ ([Gillyns et al. 2022](/sources/gillyns-2022.md),
§1), the outer region being driven by the pressure gradient and by the stress
propagated from the wall. [Husson et al. (2024)](/sources/husson-2024.md)
(§1) give the same figure for lattice Boltzmann solvers, where WMLES models
"roughly the first ten percent of the boundary layer" with the law of the
wall alone or with a RANS eddy viscosity blended into the LES, and where it
is "preponderant" but "still raises open questions" about generating inflow
fluctuations, which the unresolved near-wall events can no longer produce
(see [inflow turbulence generation](/methods/inflow-turbulence-generation.md)),
and about the RANS–LES interface; in hybrid RANS/LES, they note, the outer
layer of attached boundary layers is RANS as well, so no fluctuations need
to be generated.

## Wall models

| Model | Idea | Page |
|---|---|---|
| Equilibrium (ODE or algebraic) | constant-stress inner layer, law of the wall inverted at $h_{\mathrm{wm}}$ | [equilibrium wall model](/methods/equilibrium-wall-model.md) |
| LaRTE | transport equation for the friction-velocity vector, relaxing towards equilibrium with the inertia of the layer below $h_{\mathrm{wm}}$; optional laminar Stokes-layer stress | [LaRTE wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md) |
| Inverse velocity transformation | incompressible ODE mapped to compressible profiles plus an algebraic temperature–velocity relation | [inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md) |
| Learned (supervised or reinforcement learning) | network maps LES state to $\tau_w$ or to its update | [machine-learning wall models](/methods/machine-learning-wall-model.md) |
| Building-block flow | classifier over seven canonical flows blends per-flow learned predictions of $\tau_w$, with a confidence score | [building-block-flow wall model](/methods/building-block-flow-wall-model.md) |
| Wall slip (volume filtering) | the filtered velocity at the wall is modelled by a filtered van Driest profile or a slip length; the stress follows | section below |

**Not every "wall model" is a WMLES wall model.** [Chen et al. (2024)](/sources/chen-2024.md)
call their compressible [Baldwin–Lomax model](/methods/baldwin-lomax-model.md)
an "algebraic wall model", but it is an algebraic RANS eddy viscosity for
the whole boundary layer, solved with the boundary-layer equations; it
supplies no wall stress to an LES. It borrows ingredients from WMLES work:
the semi-local damping of mixing-length wall models and the
velocity-transformation and temperature–velocity combination of the
[inverse-velocity-transformation wall model](/methods/inverse-velocity-transformation-wall-model.md)
(§1, §2.3, §3.3). [Constant et al. (2024)](/sources/constant-2024.md) use an
equilibrium wall function as the near-wall closure of steady RANS on an
[immersed boundary](/methods/immersed-boundary-method.md), with no LES
region; they name a hybrid RANS/LES extension as future work (§7).
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md) (§3.3) borrow the WMLES
choice of sampling point, away from the wall inside the first element, for
a steady RANS [wall function](/methods/rans-wall-function.md).

[Cai et al. (2022)](/sources/cai-2022.md) (§I, §II.C.1) put the motivation
in the same terms: without a wall model the no-slip condition requires grids
refined "to the limit of DNS" in both wall-parallel and wall-normal
directions near the wall.

**How the stress reaches the LES.** Gillyns et al. (2022, §2) prescribe
$\tau_w$ as a stress boundary condition (Nek5000's `sh` condition), which
requires the stress formulation of the momentum equations. Bae & Koumoutsakos (2022, Methods, Eq. 10) keep
no slip and impose the stress through a wall eddy viscosity chosen so that the
resolved wall gradient gives the modelled stress, a choice they call better
against [log-layer mismatch](/definitions/log-layer-mismatch.md).

**Weak Neumann against viscosity-based imposition.**
[Mukha et al. (2025)](/sources/mukha-2025.md) (§II.C.2–II.C.4, Eqs. 7–14)
analyse the two routes in a continuous Galerkin spectral-element code
([Nek5000](/software/nek5000.md), polynomial degree $N=7$). Integrating the
weak form of the stress divergence by parts gives, for a test function $v_i$
and the total (viscous plus subgrid) kinematic stress $\sigma^{\mathrm t}_{ij}$
with wall traction $t_i=\sigma^{\mathrm t}_{ij}n_j$ (page-local symbols),

$$\int_\Omega\frac{\partial v_i}{\partial x_j}\sigma^{\mathrm t}_{ij}\,dV=\int_{\partial\Omega}\big[v_it_{w,i}+(t_jn_j)\,v_in_i\big]\,dA,\qquad t_{w,i}=t_i-(t_jn_j)n_i .$$

The second term vanishes because non-penetration is enforced strongly; the
first vanishes for no slip (test functions zero at the wall) and, for a
Neumann condition, is where the modelled stress enters, as a natural
boundary term. Two consequences follow.

- *Neumann (weak).* The wall stress computed from the mean velocity gradient
  at the wall, $\tau_w^{\mathrm{wall}}$, equals the modelled one,
  $\tau_w^{\mathrm{wm}}$, only asymptotically under refinement. In channel
  flow at $Re_\tau\approx8000$ on meshes of 2, 4 and 8 elements per $\delta$
  the errors of $\tau_w^{\mathrm{wm}}$ are 0.71 %, 0.76 % and $-0.54$ %, those
  of $\tau_w^{\mathrm{wall}}$ 12.58 %, 10.86 % and 8.07 %, and those of the
  stress implied by the driving pressure gradient, $\tau_w^{\nabla p}$,
  1.95 %, 0.96 % and $-3.84$ % (Table II; superscripts page-local).
  $\tau_w^{\mathrm{wall}}$ "should essentially be disregarded":
  $\tau_w^{\mathrm{wm}}$ sets the slope of the linear Reynolds shear-stress
  profile, and the gap between $\tau_w^{\nabla p}$ and $\tau_w^{\mathrm{wm}}$
  measures the global momentum imbalance of the discretization (§III.B.2).
  The authors call the issue "unique to the finite element method". Duan &
  Wang (2024, §4) also impose the wall condition weakly, at the wall flux
  points of a flux-reconstruction scheme, and report no comparison of the
  two stresses.
- *Viscosity-based (strong).* No slip is kept and the subgrid viscosity at
  the wall is set so that the resolved gradient carries the modelled stress,
  $\nu_t|_w=\tau_w^{\mathrm{wm}}/\big(\rho\sqrt{(\partial u/\partial y)_w^2+(\partial w/\partial y)_w^2}\big)-\nu$
  (Eq. 14 in registry notation, $\tau_w$ dynamic: at a no-slip wall the
  source's strain components, printed without the factor $\tfrac12$, reduce
  to the wall-normal derivatives *(compiler check, not in the sources)*). This is the condition
  of Bae & Koumoutsakos (2022) above; Mukha et al. recall its long use in
  OpenFOAM, its use to blend wall-resolved and wall-modelled regions by
  setting the wall viscosity to zero where the inner layer is resolved, and
  a finite-difference comparison by Bae & Lozano-Durán that found it
  somewhat more accurate than the Neumann condition (as they cite it). A
  scalar viscosity cannot set the direction of the stress, so with spanwise
  strain the streamwise stress is under-predicted even for an exact
  magnitude (§II.C.4). In the spectral-element channel it fails:
  $\tau_w^{\mathrm{wm}}=\tau_w^{\mathrm{wall}}$ by construction (errors
  $-0.91$ %, $-0.85$ %, $-2.26$ %), but $\tau_w^{\nabla p}$ is off by 38.05 %,
  25.73 % and 15.65 %, the mean velocity is strongly under-predicted for
  $y^+\lesssim2500$ and over-predicted in the core, all Reynolds stresses are
  over-predicted, and at fixed $Re_\tau$ the stress is strongly
  under-predicted; the authors attribute this to strong violation of
  momentum conservation and judge the attempt "largely unsuccessful"
  (§III.D, Table IV, Figs. 9–10; §V).

The continuous discretization conserves mass globally when the velocity is
locally divergence-free, but not momentum, because velocity derivatives jump
across element boundaries; the jumps are negligible at wall-resolved
resolution and significant at WMLES resolution (§II.B). The peaks at
element boundaries that the jumps leave in their Reynolds-stress profiles
are "similar to the results in Gillyns et al." (§III.C), who report the same
spikes in the same code (below).

On non-body-fitted Cartesian grids the stress reaches the LES through an
[immersed boundary](/methods/immersed-boundary-method.md): Cai et al. (2022,
§II.C.1, Fig. 1b) invert the wall model at the fluid points next to the
boundary, interpolate the friction velocity (not the velocity) to the
boundary points, set the tangential velocity there from $u_\tau u^+(y^+)$,
compute gradients by weighted least squares and correct the wall-normal
gradient of the tangential velocity, which is "highly underestimated
regardless of the accuracy of the gradient schemes", by a discrete wall-law
gradient. They recall that immersed boundaries coupled to wall models give
spurious oscillations of wall pressure and skin friction and over-estimate
the mean skin friction, because the wall distance of near-wall nodes varies
along a steep, under-resolved profile.

**Near-wall stress constraint (constrained LES).** Because the immersed
boundary is not conservative, the total near-wall Reynolds stress is not
maintained and turbulence development is delayed; Cai et al. (2022,
§II.C.1, Eq. 27, from the authors' earlier work and the constrained LES of
Chen et al. and Verma et al., as they cite them) therefore augment the eddy
viscosity "several grid points from wall" with the resolved stress:

$$\nu_t^{\mathrm{hyb}}=\frac{2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle+R^{\mathrm{res}}_{ij}\langle\tilde S_{ij}\rangle}{2\langle\tilde S_{ij}\rangle\langle\tilde S_{ij}\rangle},\qquad \frac{\nu_t^{\mathrm{RANS}}}{\nu}=\kappa y^+\left(1-e^{-y^+/19}\right)^2,$$

with $R^{\mathrm{res}}_{ij}=\langle\tilde u_i\tilde u_j\rangle-\langle\tilde u_i\rangle\langle\tilde u_j\rangle$
the resolved Reynolds stress, $\langle\cdot\rangle$ a time average and $\tilde{\ }$
the Favre filter of their weakly compressible lattice Boltzmann formulation
(page-local $\nu_t^{\mathrm{hyb}}$, $\nu_t^{\mathrm{RANS}}$, $R^{\mathrm{res}}_{ij}$).
Contracting the condition $R^{\mathrm{res}}_{ij}-2\nu_t^{\mathrm{hyb}}\langle\tilde S_{ij}\rangle=-2\nu_t^{\mathrm{RANS}}\langle\tilde S_{ij}\rangle$
with $\langle\tilde S_{ij}\rangle$ gives exactly this formula: the total
(resolved plus modelled) stress, projected on the mean strain, equals the
mixing-length RANS stress *(compiler check, not in the sources)*. The authors
state that $\nu_t^{\mathrm{hyb}}$ tends to the RANS viscosity in attached and
to the SGS viscosity in separated boundary layers, which makes the method a
form of [hybrid RANS/LES](/definitions/hybrid-rans-les.md) near the wall;
how the return to the SGS viscosity is enforced is not printed. The SGS model
is the [Vreman model](/methods/vreman-model.md) with $C_s\approx0.1$ in
$\nu_t=2.5C_s^2\Delta^2\sqrt{B_\beta/A_\beta}$ (§II.A).

Fowler et al. (2022, §1) and [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md)
(§I, §II.A) also recall zonal two-layer models on a separate RANS mesh (whose
cost can approach wall-resolved LES), the integral wall model of Yang et al.
(2015), the dynamic slip wall model of Bose & Moin (2014) and Bae et al. (2019),
and a POD-inspired model; none of these is formulated in those sources. The
slip approach is formulated by Rickard & Kasbaoui (2026), next section.

## Wall-slip models with volume filtering

[Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) derive a wall model
for [immersed-boundary](/methods/immersed-boundary-method.md) LES from the
filtering itself, which they name immersed boundary-modelled LES (IBMLES).
The incompressible equations are convolved with a compact, symmetric kernel
of support width $\Delta_f$ that is truncated by the fluid indicator and,
unlike the treatment of Bose & Moin (2014) as they recall it, not rescaled
near the wall; the deficit is carried by the fluid volume fraction
$\varphi_f$ (1/2 at a planar wall), and filtered quantities extend
$\Delta_f/2$ into the solid (§2.1; page-local $\Delta_f$, $\varphi_f$,
$\varphi_{f,w}$ its wall value). Exact commutation identities turn the wall
terms into an immersed-boundary body force and leave, besides the SGS
stress, a closed "residual viscous stress" that is linear in the slip at the
wall (§2.2–2.3, Eqs. 2.17–2.27). The only unclosed wall quantity is the
filtered velocity at the wall, the slip
$\boldsymbol u_{\mathrm{slip}}=\bar{\boldsymbol u}|_w-\boldsymbol u_w$, and
the wall stress follows from it (Eq. 2.25), so "modelling the wall slip is
in essence a turbulence wall model"; no slip holds only in the DNS limit
$\Delta_f^+<1$ (§2.3).

**A priori magnitudes** (§3, filtered channel DNS of Lee & Moser at
$Re_\tau=5200$, $\Delta_f^+=50$–300, four kernels): the mean streamwise
slip is $6.93u_\tau$ at $\Delta_f^+=50$ and $13.5u_\tau$ at 300, growing
logarithmically; wall-normal and spanwise mean slips are negligible;
streamwise slip fluctuations are about $1.5u_\tau$ at all widths and carry
the near-wall streaks at small $\Delta_f$ and outer-layer structures at
large $\Delta_f$. The residual viscous stress exceeds the filtered viscous
stress at every width tested, and the peak SGS shear stress grows from 0.24
to 0.57 $\tau_w$ (Figs. 6–10).

**Two closures** (§4–5):

- *Van Driest slip model*: the volume-filtered van Driest profile (see
  [law of the wall](/definitions/law-of-the-wall.md)), with a fitted
  approximation
  $\langle u_{\mathrm{slip}}\rangle/u_\tau=\varphi_{f,w}^{-1}\big[(2\kappa)^{-1}\ln(\Delta_f^+/2)+a_0+b_0(\Delta_f^+)^{-n_0}\big]$,
  $\kappa=0.41$, within 1 % of the exact filtered profile for
  $\Delta_f^+\ge100$; across kernels $a_0=0.81\pm0.21$, $b_0=-67.5\pm4.5$,
  $n_0=0.92\pm0.03$ (Eqs. 4.2–4.5, 7.1, Table 1; page-local constants).
- *Slip-length model*: the commutation identity gives
  $\boldsymbol u_{\mathrm{slip}}=\mathrm{diag}(\boldsymbol\ell)\,\partial\bar{\boldsymbol u}/\partial n|_w$
  with slip lengths $\boldsymbol\ell=\varphi_{f,w}(\boldsymbol\Lambda-1)/(\partial\varphi_f/\partial n)|_w$,
  $\boldsymbol\Lambda$ the ratio of the filtered wall gradient to the
  gradient of the filtered velocity, which tends to one as
  $\Delta_f\to0$ and so recovers no slip (Eqs. 4.13, 4.24). The fit
  $\Lambda_x=1+0.251\,(\Delta_f^+)^{0.5385}$ gives
  $\ell_x^+=0.0798\,(\Delta_f^+)^{1.5385}$ for the cosine kernel, roughly
  $\ell_x^+\approx0.08(\Delta_f^+)^{1.5}$ for all four kernels; the
  wall-normal and spanwise ratios are set to one (Eqs. 4.25–4.27, 7.3).
  The derivation holds for curved (with curvature resolved by $\Delta_f$)
  and moving walls, which the authors say the Taylor-series argument of
  Bose & Moin does not.

A dynamic slip length from the Germano identity, with a separate length per
direction and an explicit positive root instead of a least-squares fit, is
derived but not tested (§6; see [dynamic procedure](/methods/dynamic-procedure.md)).
There are no a posteriori runs: the constants come from one Reynolds number,
and rough, deforming or strongly separated walls are outside the stated
scope (§4.2, §7). Existing SGS models, such as dynamic Smagorinsky, are
expected to close the SGS stress (§7). The authors note, after Verzicco (as
cited), that immersed boundaries on non-uniform grids produce spurious
stress oscillations that corrupt the near-wall eddy viscosity (§1).

## The wall-model solve: robustness and cost

At every wall node and time step the wall model samples the LES at
$h_{\mathrm{wm}}$, computes $\tau_w$ and returns it as a boundary
condition, the three steps that [Nuca et al. (2025)](/sources/nuca-2025.md)
(§I) take from Larsson et al. and Bose & Park (as cited). For the
algebraic and ODE wall laws they treat, the second step is an iterative
inversion (Newton or fixed point), and Nuca et al. (§I–II)
report that it fails "sporadically" in complex geometries: the Newton
solver of Spalding's law diverges when the sampled velocity fluctuates
strongly or when the law is applied where it does not hold, as in
transition regions, and particularly when $h_{\mathrm{wm}}$ lies above the
first off-wall node. Channel flow and zero-pressure-gradient plates, on
which much of the wall-model literature rests, "are suitable for testing the model's accuracy but not
its robustness" (§II). Their remedy is an explicit approximation of the
law, used directly or as initial guess; on WMLES of the Aérospatiale
A-airfoil near stall (OpenFOAM, [sigma model](/methods/sigma-model.md),
18.7 M cells, 10–12 cells across the boundary layer, "at the lower limit"
of acceptable WMLES resolution) it caps the Newton count at 3 instead of
10–11 and the ODE fixed-point count at 6 instead of the 100-iteration cap,
and the wall model takes about 2 % of the run time with algebraic laws and
11.9 % with the integrated ODE model (§VI, App. B; details on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page).

## Error scaling: WMLES as a convergence study

Lozano-Durán et al. (2022, §IV.A) argue that WMLES is intrinsically
grid-dependent — "the grid size is an explicit variable of the governing
equations" — and must be assessed by convergence studies. Following
Lozano-Durán & Bae, as they recall it, they posit for a mean quantity $q$
the relative error (page-local symbols $e_q$, $b_q$, $a_q$)

$$e_q=\frac{\lVert\langle q_{\mathrm{exp}}\rangle-\langle q\rangle\rVert}{\lVert\langle q_{\mathrm{exp}}\rangle\rVert}=b_q\left(\frac\Delta\delta\right)^{a_q},$$

with $\Delta$ the local isotropic grid size, which is also the implicit filter
width. Their results:

- **Wall pressure** is an outer-layer, inviscid quantity: under the
  thin-boundary-layer approximation the wall pressure equals the inviscid
  pressure, so $b_p\ll1$ and $a_p\approx0$ (Eq. 10). $C_p$ errors stay below
  5 % on all their grids, even with 0–1 points per $\delta$, and a free-slip
  run without SGS model gives nearly the same $C_p$ (§V.E, Figs. 20–21).
- **Mean velocity** scales with $a_u=0$ when $\Delta/\delta$ lies in the
  shear-dominated range and $a_u=1$ in the inertial range (Eq. 11). In
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at
  $Re_\tau=4200$ ([CharLES](/software/charles.md), dynamic Smagorinsky,
  equilibrium wall model, $\Delta/\delta=1/3,1/5,1/10$) they find
  $e_u\approx0.08\,\Delta/\delta$, with the same linear trend from a staggered
  finite-difference solver (§IV.B, Fig. 7b). The difference between DNS and an
  inviscid solution, about 15 %, bounds the mean-velocity error of even a poor
  WMLES of canonical flows.
- **Corners.** Near a second wall the error is controlled by the local shear
  length $u_\tau/|\mathrm dU/\mathrm dy|$, so $e_u\sim\Delta/d$ with $d$ the
  distance to the nearest wall (§IV.B).
- **Resolved stresses** are under-predicted where the subgrid share is large,
  since the experimental stress is approximately the resolved plus the mean
  SGS stress; turbulence-intensity errors scale as $(\Delta/\delta)^{2/3}$ with
  10–30 % values (§V.B, recalled from Lozano-Durán & Bae).

On the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) the
mean-velocity error is 3–8 % on the fuselage with $b_u\approx0.14$ (above the
channel value because of upstream error propagation), about 15 % in the
wing–body juncture with $a_u\approx0.4$, and about 100 % in the separated
trailing-edge corner with $a_u\approx0.6$ (§V.B, Fig. 15). Errors generated at
an under-resolved leading edge travel downstream over a recovery length of
about $300\delta_0$; a [boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md)
lowers $b_u$ but not $a_u$ (§V.C).

The error of the wall model itself splits into external (LES velocity at the
matching point) and internal (model constants) parts, analysed on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) page.
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) separate the two a
posteriori, by replacing the SGS model with an "exact-for-the-mean"
correction that forces the mean LES profile onto DNS (§2.5, §4.1). Across
laminar and turbulent boundary layers, pipe and Poiseuille–Couette flows, a
three-dimensional channel, the NASA CRM-HL and the
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md), their learned
[building-block-flow wall model](/methods/building-block-flow-wall-model.md)
reduces the internal error markedly, but the total error is set by the
external error of the SGS model at the matching location; they conclude that
further WMLES gains require better SGS models, not only better wall models
(§4.7, §5(4), §6). Internal errors, they add, can keep WMLES from converging
to DNS until the grid is DNS-like (§4.1).

## Agreement on what converges first

Three sources agree that outer, pressure-dominated quantities converge at much
coarser grids than near-wall and separated quantities. Lozano-Durán et al.
(2022) find $C_p$ insensitive to resolution and the separation bubble about
15 % smaller than the oil-film measurement (§V.F). Goc et al. (2021, §3) predict
$C_{L,\max}$ of the [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
within five lift counts at about ten points across the trailing-edge boundary
layer, while drag errors persist at the finest free-air grids (§3.2) and the
flap separation bubble collapses on the finest in-tunnel grid (§3.3).
[Agrawal et al. (2022)](/sources/agrawal-2022.md) (§VIII.B) note that the
suction peak of the Gaussian bump is primarily inviscid and is predicted by a
free-slip run, whereas separation needs the finest grid (first cell at
$y^+\sim30$ upstream). On a transonic airfoil [Blind et al. (2023)](/sources/blind-2023.md)
(§4, Fig. 13) find the same order on a sequence of adapted grids: $c_p$
converges fastest, the skin friction after the second adaptation and the
boundary-layer thickness $\delta_{99}$, the most sensitive quantity, only on
the fourth grid. On the Ahmed body Cai et al. (2022, §IV) find that the
wall-modelled flow separates on the slant only on the finer of two grids
($\Delta x_{\min}/H=4.5\times10^{-3}$ against $9.0\times10^{-3}$), and that
grid resolution affects drag more with the wall model than with no-slip
imposed on the slant, because the flow topology changes between the grids.

## Grid convergence can be non-monotonic

- **Channel.** Lozano-Durán et al. (2022, App. B, Figs. 23–24) find the
  mean-velocity error departs from $e_u\sim\Delta$ around
  $\Delta/\delta\approx0.03$–$0.05$ in both CharLES and a staggered
  finite-difference solver, and recovers the linear trend below 0.03. Runs
  without SGS model and with the exact DNS mean wall stress show a qualitative
  change at a critical $\Delta_c/\delta\approx0.03$–$0.05$: noisy structure
  above it, near-wall streaks below it. The authors "still lack a satisfactory
  explanation of the phenomenon and … a robust remedy".
- **Separated flows.** On the spanwise-periodic Gaussian bump
  ($Re_L=2\times10^6$), dynamic Smagorinsky and Vreman separate on the coarse
  grid, lose the separation on the medium grid and recover it on the fine grid,
  while the [dynamic tensor-coefficient model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  converges monotonically towards the quasi-DNS $C_f$ (Agrawal et al. 2022,
  §VIII.A, Fig. 13). Agrawal et al. recall similar non-monotonic behaviour in
  high-lift aircraft simulations. Goc et al. (2021, §3.3) report that the
  flap separation bubble seen experimentally and on their coarse and medium
  in-tunnel grids is suppressed on the finest one, recall a similar collapse
  under refinement by Iyer & Malik (2021) for a Gaussian bump, and leave cause
  and remedy open.
- **Pipe flow.** Lozano-Durán & Bae (2023, §4.4, Fig. 10) observe
  non-monotonic grid convergence in pipe flow at $Re_\tau\approx40\,000$ on
  grids $\Delta/R=1/5$ to $1/40$ ($R$ the radius), with both the equilibrium
  and the building-block-flow wall model and dynamic Smagorinsky; total
  errors are 4–12 %.

## Wall-mesh criteria are necessary, not sufficient

[Lewis et al. (2023)](/sources/lewis-2023.md) (§3.3, Table 5) recall, from
Piomelli (2014) and Wagner et al. (2007) as they cite them, wall-mesh
requirements in wall units (streamwise, spanwise and wall-normal cell
sizes $\Delta x^+$, $\Delta z^+$, $\Delta y^+$; the source's $s^+$, $r^+$, $n^+$):
$\Delta x^+=50$–150, $\Delta z^+=10$–40, $\Delta y^+=1$ with 3–5 points below
$y^+=10$ for wall-resolved LES, and $\Delta x^+=100$–600, $\Delta z^+=100$–300,
$\Delta y^+=30$–150 for WMLES. Two WMLES of the ACAT1 fan–outlet-guide-vane
stage at approach in AVBP (Lax–Wendroff scheme,
[WALE](/methods/wale-model.md) SGS model, linear/log wall law; LES1 with 95 M
cells and 8 prism layers, LES2 with 210 M cells, 14 prism layers and about
1.5 times finer blade and vane surface meshes) are both stated to meet them
(§3.3). Yet LES1 shows a large separation at about 65 % of the stator chord
over almost the whole vane span, with a radial vortex at 60 % chord, which
disappears in LES2 through the wall-mesh refinement; the authors conclude
that "wall laws should be used with caution since wall-mesh requirements for
WMLES are actually quite broad", that two compliant WMLES "may exhibit
significant discrepancies", and that even WMLES able to predict large
detachments "might fail to accurately predict the exact detachment and
reattachment points" (§4.2.1–4.2.2, Figs. 13, 17). LES2 also improves the
interstage wake profiles and spectra (§4.3). See the
[ACAT1 fan stage](/benchmarks/acat1-fan-stage.md). These criteria are
stated in wall units; the
[boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md)
sizes cells by the boundary-layer thickness instead.

## Interaction with the SGS model

The wall model and the SGS model ([large-eddy simulation](/definitions/large-eddy-simulation.md)) act on the
same under-resolved first cells.

- Both dynamic models of Agrawal et al. (2022, §VII.D) under-predict the SGS
  stress there; the [dynamic procedure](/methods/dynamic-procedure.md) needed
  clipping at the second off-wall point at $Re_\tau=4200$, the tensor-coefficient
  model none, and the log-region slope error relative to $\kappa=0.38$ fell
  from 7 % to 5 % (Figs. 8–10). They impose $d\tau_{ij}/dy=0$ at the wall for
  the SGS stress, because resolved stresses do not vanish at the wall of a
  coarse WMLES.
- Fowler et al. (2022, §5.1) attribute the WMLES–DNS differences in
  $\langle u'u'\rangle$ (under-predicted) and $\langle w'w'\rangle$
  (over-predicted) near the wall to grid and SGS model, because two different
  wall models give the same statistics.
- Vadrot et al. (2023b, App. B) find little effect of replacing the
  anisotropic minimum-dissipation SGS model by a Lagrangian scale-dependent
  dynamic model at $Re_\tau=5200$, for the equilibrium and the learned models
  alike.
- [Krais et al. (2021)](/sources/krais-2021.md) (§7.3) report that the Vreman
  model "helps to reduce artificial pressure fluctuations caused by the
  wall-model" in a high-order DG zonal LES of an open cavity.
- [Griffin et al. (2023)](/sources/griffin-2023.md) (§4) recall that
  stress-based wall models over-predict near-wall resolved fluctuations through
  a wall-blocking effect (Bae et al. 2018).
- [Implicit LES](/definitions/implicit-les.md) without wall model is not a
  substitute at WMLES resolution: implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  predicts $u_\tau$ in pipe flow at $Re_\tau=2000$ within about 1.9 % at
  $\Delta x^+=9$ but under-predicts it by more than 12 % at $\Delta x^+=18$, and the authors
  conclude it "cannot be used alone in the context of WMLES"
  ([Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md), §7.4).
- **No wall model inside a jet nozzle.** [Ahn et al. (2023)](/sources/ahn-2023.md)
  (§III) run [implicit LES](/definitions/implicit-les.md) of twin square
  supersonic jets with the nozzle interior meshed at a first cell of
  $h_n/320$ ($h_n$ the nozzle exit height, page-local), $y^+=10$–20, and no wall
  model, accepting that "the grid resolution is insufficient to resolve the
  viscous sub-layer but allows us to convect forced velocity fluctuations";
  the fluctuations come from a geometric trip in the convergent section
  (see [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
  They cite wall models, with and without surface roughness, as the
  alternative. Even with tripping the turbulent kinetic energy near the lip
  stays above the PIV values, though less than without it (§IV.B).
- **"Wall model" for DG implicit LES.** [Lederer et al. (2023)](/sources/lederer-2023.md)
  (§6) write that their adaptive
  [high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md),
  which lowers the excessive near-wall upwind dissipation of under-resolved DG
  implicit LES, "can be interpreted as a wall model approach for standard DG
  ILES". The method models no wall stress and uses no matching height; their
  channel runs at $Re_\tau=392.24$ tabulate near-wall resolutions of 3.00 to
  13.64 wall units (§4, Table 1). The term is used
  here in a sense different from the wall-stress models of this page.
- **A learned closure in place of a wall model.** [Sirignano & MacArt (2023)](/sources/sirignano-2023.md)
  (§4.3) run LES of bluff bodies at $Re_0=1000$–2000 whose mesh does not
  resolve within $y^+=10$, with no wall model, and find that an
  adjoint-trained neural-network closure of all unclosed terms gives better
  near-wall mean profiles than the AMD, dynamic Smagorinsky and no-model LES;
  see [machine-learning wall models](/methods/machine-learning-wall-model.md).

- **Discretization dependence of the guidelines.** Gillyns et al. (2022, §1)
  state that WMLES guidelines derived for finite differences (Larsson et al.)
  or discontinuous Galerkin (Frère et al.) "cannot be used as such" in a
  spectral element code, because "the modelled region is highly sensitive to
  the discretization method". In their continuous spectral-element LES
  (polynomial degree 7, approximate-deconvolution SGS model) the velocity is
  continuous across elements but its gradient is not, which produces
  Gibbs-like spikes in the fluctuation statistics at element interfaces on
  coarse meshes; they use the spikes as a reference-free mesh-quality
  indicator and name them the main drawback of the approach (§2, §8). Their
  mean velocity stays within 1.1 % (normalized RMS) of DNS even inside the
  under-resolved first element, which they attribute, without a same-mesh
  comparison, to the spectral element method (§7, §10).

- **SGS model as stabilizer in a continuous spectral-element code.**
  Mukha et al. (2025, §II.D, §III.C, Figs. 6–8) compare on their finest
  channel mesh the [Vreman model](/methods/vreman-model.md) (single constant
  $2.5C_s^2$ with $C_s=0.16$), the sigma model ($C_\sigma=1.35$, page-local;
  near-wall viscosity $\propto y^3$, as for [WALE](/methods/wale-model.md))
  and Nek5000's high-pass relaxation filter as implicit SGS model (two modes,
  weight 100), with the SGS length scale set for the whole element by its
  largest GLL spacing and $\nu_t$ not forced to zero at the wall. All three
  give an accurate $\tau_w^{\mathrm{wm}}$ and no
  [log-layer mismatch](/definitions/log-layer-mismatch.md), but less
  near-wall dissipation gives a more oscillatory solution: the error of
  $\tau_w^{\mathrm{wall}}$ is 8.07 % with Vreman, $-25.72$ % with the sigma
  model and $-84.85$ % with the filter, and the filter alone "does not
  introduce enough damping" and over-predicts $\langle u'u'\rangle$. Jumps of
  the velocity derivative at element boundaries become spikes of $\nu_t$,
  "just numerical artifacts"; ensuring derivative continuity is called "a
  missing component in the current WMLES methodology". Vreman shows no
  visible near-wall decrease of $\nu_t$ although its asymptote is linear in
  $y$, so "how fast the model transitions towards the asymptote" matters.
  Against reports that WALE and sigma over-predict the wall stress in
  channel WMLES (Blanchard et al., as cited) they conclude that accuracy is
  "a strong function of the combination of the boundary conditions, SGS
  model and numerical method"; Vreman "could, perhaps, be preferred due to
  smoother derivatives" and is used for their boundary-layer runs.
- **High-order schemes need added dissipation at WMLES resolution.**
  [Duan & Wang (2024)](/sources/duan-2024.md) state that high-order implicit
  LES "often runs into robustness and accuracy issues" in WMLES because the
  schemes carry little dissipation (§1). Their flux-reconstruction
  ([flux reconstruction](/methods/flux-reconstruction.md)) WMLES of channel
  flow at $Re_\tau=5200$ on $60\times16\times40$ elements (element sizes
  $\Delta x^+=1088$, $\Delta y^+=650$, $\Delta z^+=544$) was not stable without
  an SGS model (§5.4). Stabilization by solution limiting works, but in an
  earlier fourth-order WMLES they show (Fig. 2, from earlier work as
  cited), too little limiting
  over-predicts the wall friction and under-predicts the velocity and too
  much does the reverse, which they call "very ad hoc" (§1, Fig. 2; §5.4).
  With explicit eddy-viscosity models, element-wise constant $\nu_t$ and
  zero interface SGS flux, they recalibrate the filter width instead of the
  constant: the [Vreman model](/methods/vreman-model.md) with
  $\Delta=V^{1/3}/\sqrt{N+1}$ ($V$ the element volume, page-local) gives the
  best mean velocity at every degree $N=2$–5 and at $Re_\tau=544$, while the
  [WALE model](/methods/wale-model.md) is best with $\Delta=V^{1/3}$ at
  $N=2$–4 and with $V^{1/3}/\sqrt{N+1}$ at $N=5$, a reversal they call
  unexpected (§3, §5.4, Figs. 11–15). They recommend Vreman with
  $V^{1/3}/\sqrt{N+1}$ for high-order WMLES (§6); the comparisons are visual,
  without tabulated errors. In wall-resolved LES at $Re_\tau=180$ implicit LES
  agrees very well with the DNS, the Smagorinsky model performs very poorly
  at every width, and WALE and Vreman agree well only with the two smaller
  widths (§5.3, Figs. 9–10), so the recommendation is specific to
  wall-modelled resolution.
- **Learned SGS models under a wall model.** [Wu & Lele (2026)](/sources/wu-2026.md)
  (§6.2, Figs. 15–20) run their [neural-network SGS models](/methods/neural-network-sgs-model.md),
  trained on filtered isotropic and channel DNS, in WMLES of channel flow at
  $Re_\tau=1000$ ($128\times96\times32$ points, $\Delta=16$ DNS spacings,
  Fourier wall-parallel and sixth-order staggered wall-normal schemes, the
  wall model of Bou-Zeid et al. as cited) without retraining. The network
  trained on box-filtered data with complex inputs "completely fails" with
  unphysical spectra and over-predicts the Reynolds stresses, notably
  $R_{11}$ and $R_{33}$ (their wall-normal direction is $z$), and static
  [Smagorinsky](/methods/smagorinsky-model.md) ($C=0.18$) piles up energy at
  high wavenumbers, while the [sigma model](/methods/sigma-model.md)
  ($C=1.3$) and the network trained on two filter shapes reproduce the
  spectra; the latter's mean velocity "lines up very well" with filtered DNS
  and its stresses are "oftentimes" the most accurate, even against sigma.
  The SGS model, not the wall model, separates success from failure here.
- **Element-based matching.** Duan & Wang (2024, §4, Fig. 4) place the
  exchange location of their equilibrium model on the interface between the
  first and second elements off the wall and take the data from the second
  element, because the scales in the first element are always
  under-resolved; a near-wall element aspect ratio of one is desirable.
  Gillyns et al. (2022) sample at the same height, the top node of the first
  element, where their continuous spectral-element velocity is single-valued;
  in the discontinuous flux-reconstruction solution the interface carries two
  values, and Duan & Wang choose the outer one *(compiler check, not in the
  sources)*.

Low numerical dissipation is a precondition: Goc et al. (2021, §2.3) call
[numerical dissipation](/properties/numerical-dissipation.md) "extremely
detrimental" for coarse LES and use kinetic-energy- and entropy-preserving
schemes ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
[Carlsson et al. (2023)](/sources/carlsson-2023.md) (§4.3, Fig. 4) show the
consequence in the WMLES branch of IDDES: on channel grids built to WMLES
practice up to $Re_\tau=18\,000$, a central scheme with the artificial
dissipation of RANS practice produces a significant
[log-layer mismatch](/definitions/log-layer-mismatch.md), which their
[low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
reduces to a small one at the RANS–LES interface.

## Grid adaptation for WMLES

[Blind et al. (2023)](/sources/blind-2023.md) adapt the residual-based grid
adaptation of Toosi & Larsson to the DG spectral element code
[FLEXI](/software/flexi.md) (details on [mesh adaptation](/methods/mesh-adaptation.md))
and apply it to WMLES. Left alone, the residual estimator sees the strongest
under-resolution next to the wall and refines there; but "severe
underresolution in that region is a choice and not an error", so the target
spacing of every cell between the wall and $h_{\mathrm{wm}}$ is reset, in all
three directions, to its value at $h_{\mathrm{wm}}$ (a rule credited to Toosi,
personal communication; §3.3). With the Vreman constant raised to 0.11
("previous experience" in the code), Spalding's law and $h_{\mathrm{wm}}=0.1h$
in channel flow at $Re_\tau=2000$, the mean velocity agrees with DNS above
$h_{\mathrm{wm}}$ on the fourth grid ($l=3$) and the Reynolds stresses on the
fifth, $\langle u'u'\rangle$ not exactly, which they attribute to WMLES rather
than to the adaptation (Figs. 10–11). On the adapted grids the matching point
can sit in the second off-wall cell. The WMLES of a transonic NACA 64A-110
airfoil ($M=0.72$, $Re_c=9.3\times10^5$, $h_{\mathrm{wm}}=0.0134c$) starts from
six elements per chord and reaches the wall-resolved reference in $c_p$,
$\tau_w$ and $\delta_{99}$ within four grids (§4).

## Demonstrations

- **High-lift aircraft** (Goc et al. 2021): JAXA Standard Model at
  $Re_c=1.96\times10^6$, $M_\infty=0.172$, $Re_\tau\approx5000$; Vreman (free
  air) or dynamic Smagorinsky (in tunnel) with the equilibrium wall model; 32 M
  Voronoi cells give the lift curve and $C_{L,\max}$; wind-tunnel walls and
  nacelle are needed for the inboard separation and the pitching-moment
  kickback. A medium-grid run costs about $40\times10^3$ core-hours (21 h on
  2000 CPU cores, 48 min on 96 V100 GPUs), comparable to a steady RANS run of
  the workshop; the authors judge WMLES of high-lift aircraft "on the threshold
  of readiness for industrial use" (§4–5).
- **Wing–body juncture** (Lozano-Durán et al. 2022): the juncture flow at
  $Re=2.4\times10^6$ on the crank chord, eight grids from 6 M to 174 M cells,
  13–398 thousand core-hours.
- **Smooth-body separation** (Agrawal et al. 2022, §VIII): the Boeing Gaussian
  bump, spanwise-periodic ($Re_L=2\times10^6$, against quasi-DNS) and 3D
  ($Re_L=3.41\times10^6$, against experiment); on the finest grid both dynamic
  models predict the bubble and the counter-rotating vortex pair, while
  Vreman misses separation in 3D.
- **Non-equilibrium channel** (Fowler et al. 2022, §5.2): sudden spanwise
  pressure gradient at $Re_{\tau0}=1000$.
- **Compressible channels** (Griffin et al. 2023, §4): $M_b=0.7$–$4$,
  $Re_\tau=320$–$1800$, 12 points per half-height.
- **Spectral-element channel** (Gillyns et al. 2022, §5–9): algebraic
  equilibrium model in Nek5000 against the DNS of Lee & Moser at
  $Re_\tau=1000$ and 5200; mean-velocity errors below 1 % and fluctuation
  errors up to about 9 % (normalized RMS), with five wall-normal elements per
  half-height judged acceptable and four "not sufficiently resolved" at
  $Re_\tau=1000$ (§8), the same four-element mesh being called "a fair
  compromise between accuracy and computational cost" in §9.
- **Shock/boundary-layer interaction over a flexible panel** (Hoy &
  Bermejo-Moreno 2022): Mach 3 impinging shock, unit Reynolds number
  $49.4\times10^6$ m$^{-1}$, $\delta_0=4$ mm, coupled to a finite-element
  structural solver; finite-volume WMLES with the
  [Vreman model](/methods/vreman-model.md), the Kawai–Larsson equilibrium
  model at $h_{\mathrm{wm}}=0.1\delta_0$, a hybrid ENO/central scheme and
  digital-filter inflow, on about 20 M (spanwise-periodic, $5\delta_0$) and
  200 M (full span, $50\delta_0$) cells. WMLES is what makes the experimental
  Reynolds number, span and duration affordable (§1, §3). Panel flexibility
  moves separation about $3\delta_0$ upstream and lengthens the separation by
  about 60 % ($L_{sep}/\delta_0\approx7.8\to12.6$; §4.3). The authors rest the
  validity of the equilibrium model in this strongly separated flow on earlier
  work (Bermejo-Moreno et al. 2014, as they cite it), not on a test here.
  For comparison, [Gao et al. (2022)](/sources/gao-2022.md) (§5, Tables
  1–2) resolve the wall in a Mach 2 oblique interaction ($Re_{\theta_0}=1628$)
  with high-order DG implicit LES at $N=6$: $\Delta y^+_{\min}=1.6$,
  $\Delta x^+=30$, $\Delta z^+=16$ at the reference station, about 93 M
  degrees of freedom on 16 384 cores and about 196 600 CPU hours for the
  interaction run; they name WMLES as where "the main emphasis of the
  efficiency improvement" of such simulations should go (§6), without
  running one. See [shock–turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
- **Bluff body with massive separation on an immersed boundary** (Cai et al.
  2022, §III–IV): Ahmed body with 35° slant, $Re_H=7.68\times10^5$, lattice
  Boltzmann solver ProLB with the Vreman model, explicit equilibrium wall
  model and the constrained-LES near-wall viscosity, octree grids of 13.6 M
  and 40.3 M cells, Mach number raised from 0.12 to 0.24 to enlarge the time
  step. Wall model everywhere ("wall-law") is compared with no-slip imposed
  in advance on slant and base. Drag coefficients (near-field/far-field,
  Table III): wall-law fine 0.2347/0.2380, coarse 0.2742/0.2912; no-slip
  fine 0.2553/0.2588, coarse 0.2548/0.2486; against experiments of 0.279
  (Meile et al., same $Re_H$) and 0.26 (Ahmed et al., $Re_H=1.2\times10^6$),
  and body-fitted computations of Guilmineau et al. of 0.2999 ($k$-$\omega$
  SST), 0.2603 (EARSM), 0.3156 (DES) and 0.3452 (IDDES), as they list them.
  The authors judge the fine wall-law case better overall by its velocity
  profiles and closer to Meile et al. than the body-fitted IDDES.
- **The same bluff body with SST-based hybrids** ([Mozaffari et al. 2024](/sources/mozaffari-2024.md),
  §3.3, Table 3): ProLB again, $35^\circ$ and $25^\circ$ slants at the same
  $Re_H$, 45.8 M nodes with finest cells of 1.3 mm (the finest cell of Cai
  et al.'s fine grid, $4.5\times10^{-3}H$ with $H=288$ mm, is also 1.3 mm
  *(compiler check, not in the sources)*), but with
  [SST-IDDES](/methods/detached-eddy-simulation.md) or continuous eddy
  simulation (see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)) in place
  of Vreman LES with the constrained-LES viscosity. With the explicit
  equilibrium wall model on the body neither hybrid separates on the slant
  at either angle (drag 0.2878 IDDES and 0.2738 CES at $35^\circ$); with a
  zero-velocity condition at $y^+\gg1$ the IDDES reproduces the $35^\circ$
  wake topology and drag (0.2819, against 0.2580–0.32 in the experiments
  they list), while at $25^\circ$ it separates late without reattachment
  ($y^+\approx100$–150 on the slant). The authors attribute the attached
  wall-model solution to the missing pressure-gradient term (see the
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)).
  Cai et al. (2022) had stated that, without their near-wall stress
  enhancement, "the flow stays attached even by refining the grid";
  Mozaffari et al., whose hybrids do not use that constrained-LES
  viscosity, give the missing pressure-gradient term, not the near-wall
  stress, as the cause of their attached solution. They conclude that SST-based hybrids "can
  be an alternative for the wall-modeled LES in the LBM framework" and that
  IDDES with the no-slip condition "could recover the WMLES solution" of
  Cai et al. at lower cost, without cost figures (HAL manuscript lines
  413–418, 510–515).
- **Learned wall model up to $Re_\tau=10^{10}$** ([Vadrot et al. 2023a](/sources/vadrot-2023.md),
  §III): half-channel WMLES in [LESGO](/software/lesgo.md) on a uniform
  $48^3$ grid at eleven $Re_\tau$ from 180 to $10^{10}$, with a
  reinforcement-learning wall model trained only at $10^4$; at this
  resolution neither the inner peak ($y^+\approx15$) nor the outer peak
  ($y^+\approx3\sqrt{Re_\tau}$) of the streamwise velocity variance is
  resolved, by any of the wall models tested (§III.A, Fig. 7), and the SGS
  model used is not stated (§II.A). See
  [machine-learning wall models](/methods/machine-learning-wall-model.md).
- **Transonic airfoil on adapted DG grids** (Blind et al. 2023, §4): see
  the section above; 222 426 elements on the last grid, about half of what a mesh
  of the same spacings without spanwise mortar zones would need.
- **IDDES channel flow** (Carlsson et al. 2023, §4.3, Table 2): SST-IDDES at
  $M_b=0.15$ ($Re_\tau=395$, 2400, 18 000) and $M_b=1.5$ (500, 1015, 5000),
  $64\times64$ points in the wall-parallel plane, first node at $y^+\approx0.5$.
- **High-lift aircraft and juncture with a learned wall model**
  (Lozano-Durán & Bae 2023, §4.7–4.8): NASA CRM-HL at
  $Re=5.49\times10^6$ (mean aerodynamic chord), $M_\infty=0.20$, 30 M
  points with 0–20 points per boundary-layer thickness, at 7° and 19°, and the
  Juncture Flow on a boundary-layer-conforming grid with 5 points per
  $\delta$; the building-block-flow model gives moderate gains over the
  equilibrium model, especially near stall and most clearly in pitching
  moment.
- **Fan stage** (Lewis et al. 2023): see the section on wall-mesh criteria;
  the WMLES wall-pressure fluctuations feed Ffowcs Williams–Hawkings and
  Goldstein acoustic analogies for broadband noise (§5).
- **Automotive, as cited by Delassaux et al.** Delassaux et al. (2023, §1) recall a GPU
  wall-function LES of the notchback DrivAer car by Menter et al. on 250 M
  and 500 M cells, with drag errors of 24 counts (SBES), 10 counts (250 M LES)
  and 2 counts (500 M LES, 1 %), and the GPU cost figures of Goc et al.
  (2021); their own full-scale car study uses
  [detached-eddy simulation](/methods/detached-eddy-simulation.md).
- **Spectral-element channel and boundary layer at higher Reynolds number**
  (Mukha et al. 2025, §III–IV): Spalding's law, Neumann condition and Vreman
  model in Nek5000 at $N=7$. Channel flow at $Re_\tau\approx8000$ against
  the DNS of Yamamoto & Tsuji (as cited) on $8\delta\times2\delta\times6\delta$
  with 2, 4 and 8 elements per $\delta$: the mean velocity is within 1 % for
  $y>0.1\delta$ on all three meshes, with no gain from the middle to the
  finest; second-order statistics over-predict $\langle u'u'\rangle$ and
  under-predict $\langle v'v'\rangle$, $\langle w'w'\rangle$ near the wall
  and improve strongly only on the finest, from which they require "at
  least 4 elements across the boundary layer in all three spatial
  directions" (§III.B.1, Figs. 1–2; §IV.A); Gillyns et al. (2022, §8),
  at $Re_\tau=1000$, call five wall-normal elements per half-height
  "acceptable" and four "not sufficiently resolved". A zero-pressure-gradient flat-plate boundary
  layer from $Re_\theta=790$ to about 6000 (inflow from a precursor
  simulation) gives $C_f$ within 2 % of a wall-resolved LES on the finest
  mesh and Reynolds stresses "on par with" published WMLES; its mean
  velocity improves with spanwise refinement although the outer scales are
  already resolved, which they note "would violate" the premise of WMLES
  being independent of inner-scale resolution (§IV.B, Figs. 13–17). They
  quote, for comparison, the 10–30 % velocity and 5–15 % wall-stress
  deviations of Lozano-Durán & Bae (2023) on coarser meshes, matching that
  source's own §4.3 (see [building-block-flow wall model](/methods/building-block-flow-wall-model.md)).
  Mesh details are on the [grid-point requirements](/results/les-grid-point-requirements.md)
  page.
- **WMLES as the reference of a hybrid in a lattice Boltzmann solver**
  (Husson et al. 2024, §4.3.2, §5). On the LEISA2 three-element airfoil
  ($Re_c\approx1.23\times10^6$, 77 M nodes) their zonal-DES lattice
  Boltzmann computation shows a small delay in the formation of the slat
  shear-layer instabilities; they state that it is not due to the hybrid
  model, because "the exact same phenomenon" was observed in a lattice
  Boltzmann WMLES of the same airfoil without RANS eddy viscosity by Soni et
  al. (as cited), and that capturing it would require a finer mesh (§4.3.2).
  They present the hybrid as a
  "fair alternative" to WMLES in lattice Boltzmann solvers, especially for
  aeroacoustics (see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
- **Airfoil near stall as a robustness test** (Nuca et al. 2025, §II, §VI,
  App. B): Aérospatiale A-airfoil, OpenFOAM with the libWallModelledLES
  library, sigma SGS model, wall model on the whole suction side; accuracy
  against experiment is deliberately not a goal, and statistics cover one
  convective time. See the robustness section above.
- **Learned wall models** (Bae & Koumoutsakos 2022): channel flow from
  $Re_\tau=5200$ to $10^6$ at $\Delta x=\Delta z=0.05\delta$, and a zero-pressure-gradient
  flat-plate boundary layer at $Re_\theta=1000$–7000; see
  [machine-learning wall models](/methods/machine-learning-wall-model.md).

## Qualifications

- Haering et al. (2022, §V.B) estimate a WMLES of the [periodic hill](/benchmarks/periodic-hill.md)
  at about 12 M cells (structured) or 1.6 M (streamwise-varying grid), using
  spacings of at most 8 %, 2 % and 5 % of $\delta$; both exceed the 0.9 M cells
  of their fine [active model split](/methods/active-model-split.md) grid. The
  estimate is theirs; no WMLES of the hill is run.
- **WMLES against zonal DES for turbomachinery.** [François et al. (2022)](/sources/francois-2022.md)
  (§4.1) choose [zonal detached-eddy simulation](/methods/detached-eddy-simulation.md)
  for a fan–outlet-guide-vane stage, keeping RANS in the boundary layers
  ($\Delta y^+\le1$ at the wall, 380 M cells), and state that the 0.5 mm
  free-shear cell size needed for the fan wakes "would require a larger
  number of cells in the whole mesh with a WMLES approach". The claim is not
  backed by a cost comparison in the source; they recall WMLES of fan stages
  by others.
- Locators of Lozano-Durán et al. (2022) refer to the arXiv v1 preprint read, not the AIAA Journal version.
- **WMLES against RANS for thin attached layers.** [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md)
  (§1, Fig. 1) argue for high-order RANS rather than high-order WMLES on
  industrial geometries: boundary layers of ships and submarines reach
  $Re\sim10^9$, and over a full-size wing $\delta$ grows from about 1 mm at
  the leading edge to tens of centimetres at the trailing edge, which LES,
  needing near-isotropic cells, must follow with sub-millimetre spacings.
  They endorse Spalart's view, as they cite it, that accurate "pure" WMLES
  of such a wing will not be possible before 2045, and call WMLES of a thin
  attached boundary layer "a fantastic waste of resources"; they point to
  hybrid RANS/LES for separated regions. Their reference [5] for Spalart is
  listed as a book by Durbin (2021).
- Locators of Wu & Lele (2026) refer to the arXiv v2 preprint read.
- **Printed inconsistencies of Rickard & Kasbaoui (2026).** The Fig. 6
  caption gives the streamwise slip fluctuations as "approximately 10 % or
  less" of the mean slip, while their $1.5u_\tau$ against $6.93u_\tau$ at
  $\Delta_f^+=50$ is about 22 % *(compiler check, not in the sources)*; §4.1
  states the fitted slip formula is accurate for $\Delta_f^+\ge50$, against
  $\ge100$ in Fig. 11(b) and Eqs. (5.4), (7.1).
- **Drag of the Ahmed body.** Against Meile et al.'s 0.279, the fine-grid
  wall-law drag of Cai et al. (2022, Table III) is closer than the
  body-fitted IDDES (0.3452) but farther than their fine no-slip case
  (0.2553) and their coarse wall-law case (0.2742), which does not separate
  on the slant, so drag alone does not rank the cases in the authors' order
  *(compiler check, not in the sources)*. The authors' judgement rests on the
  velocity profiles (§IV, Figs. 8–9).
- Blind et al. (2023, Table 4) list the friction Reynolds number computed in
  the wall-modelled $Re_\tau=2000$ channel as 627.91, 872.29, 1241.07,
  1220.01 and 1555.60 on the five grids, without comment; they judge
  convergence on the profiles. The table is captioned "wall-modeled
  $Re_\tau=550$ channel", while its spacings (333.33 $=2000/6$ at $l=0$)
  belong to $Re_\tau=2000$ *(compiler check, not in the sources)*.
- **Lewis et al.'s compliance.** Lewis et al. (2023, §3.3) state that both
  fan-stage meshes are "consistent with the wall requirements for
  wall-modelled LES", but their Table 6 gives mean first-cell sizes
  $\Delta y^+=25$ (LES1) and 17 (LES2), and mean wall-parallel sizes
  $\Delta x^+,\Delta z^+=80$ and 64, below the lower bounds of the WMLES ranges
  of their Table 5 ($\Delta y^+=30$–150, $\Delta x^+=100$–600,
  $\Delta z^+=100$–300); the maxima (66, 64; 300, 195) lie inside. The paper does not
  say whether the ranges are meant as upper limits only.
- Locators of Mukha et al. (2025) refer to the arXiv v1 preprint read
  (two authors; the Physics of Fluids version lists three). Their Fig. 10
  legend labels the meshes M0–M2 where text and Table IV use M1–M3.
- Locators of Blind et al. (2023) refer to the arXiv v1 preprint read
  (titled "Grid-Adaptation for Wall-Modeled Large Eddy Simulation Using
  Unstructured High-Order Methods"), not the Computers & Fluids version.

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §1–5, Figs. 5–14, Tables 1–2.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II–V, Eqs. (8)–(12), Figs. 7, 15–24; App. B.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VII.D, §VIII, Figs. 8–19.
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §1; §5.1–5.2.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I; §II.A; App. B.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1; §4.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II; §V.B.
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.4, Fig. 28.
- [Krais et al. (2021)](/sources/krais-2021.md) — §7.3, Fig. 27.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Introduction; Methods, Eq. (10); Figs. 3–5.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1–2; §5–10, Tables 1–3.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §1; §3; §4.3.
- [François et al. (2022)](/sources/francois-2022.md) — §1; §4.1.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §II.A; §II.C.1, Eq. (27), Fig. 1(b); §II.C.2; §III, Table II; §IV, Figs. 8–9, Table III.
- [Blind et al. (2023)](/sources/blind-2023.md) — §3.3, Table 4, Figs. 9–11; §4, Table 6, Fig. 13.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.3, Table 2, Fig. 4.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.5; §4.1–4.8, Figs. 10, 15, 18, Table 1; §5(4); §6.
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2–3.3, Tables 5–6; §4.2–4.3, Figs. 13, 17; §5.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §1; §4.1 (HAL author manuscript).
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §4, Table 1; §6 (arXiv v1).
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §4.3, Fig. 10; §7.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §1, Fig. 2; §3, Eqs. (26)–(30); §4, Fig. 4; §5.3–5.4, Figs. 9–15; §6.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.A; §III.A, Figs. 6–7 (arXiv v3).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §3.3, Figs. 16–24, Table 3; conclusions (HAL accepted manuscript, lines 413–418, 510–515).
- [Chen et al. (2024)](/sources/chen-2024.md) — §1; §2.3; §3.3.
- [Constant et al. (2024)](/sources/constant-2024.md) — §7 (HAL author manuscript).
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §II.B–II.D, Eqs. (7)–(14); §III.B–III.D, Tables II–IV, Figs. 1–10; §IV, Figs. 12–17; §V (arXiv v1).
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §1; §2.1–2.3, Eqs. (2.6)–(2.27); §3, Figs. 6–10; §4.1–4.2, Eqs. (4.2)–(4.27), Figs. 11–13; §5, Tables 1–2; §6; §7.
- [Wu & Lele (2026)](/sources/wu-2026.md) — §2.2; §6.2, Figs. 15–20 (arXiv v2).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1, Fig. 1.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §3.3.
- [Nuca et al. (2025)](/sources/nuca-2025.md) — §I–II, Fig. 2; §VI, Tables VII–VIII; App. B.
- [Husson et al. (2024)](/sources/husson-2024.md) — §1; §4.3.2; §5.
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III; §IV.B.
- [Gao et al. (2022)](/sources/gao-2022.md) — §5, Tables 1–2; §6.
