---
type: Method
title: "Wall functions for RANS"
description: "The near-wall closure of RANS that imposes a law of the wall at the first grid points instead of resolving the viscous sublayer: wall-stress inversion, turbulence-variable boundary values, an explicit power-law wall function for high-order DG, its accuracy and cost up to a first-element height of 320 wall units, and its failure in strong adverse pressure gradient and recirculation."
status: established
aliases: [wall function, WF, adaptive wall function, two-velocity-scale wall function, explicit wall function, RANS wall law]
tags: [rans, wall-model, boundary-layer, dg]
timestamp: 2026-10-27T10:59:00Z
---

# Wall functions for RANS

A wall function closes a Reynolds-averaged computation without resolving the
viscous sublayer and the buffer layer. The first grid points (or the first
element) lie at a wall distance where a
[law of the wall](/definitions/law-of-the-wall.md) $u^+=f(y^+)$ is assumed to
hold. The wall shear stress $\tau_w$ is obtained by inverting that law with
the mean tangential velocity sampled away from the wall, and the turbulence
variables next to the wall ($k$, $\omega$, or the Spalart–Allmaras $\tilde\nu$)
are set to their sublayer or log-layer values. The inversion is the one of the
[equilibrium wall model](/methods/equilibrium-wall-model.md) of
[wall-modelled LES](/methods/wall-modelled-les.md); the difference is the
host: a steady or unsteady RANS solution of the mean flow, with no resolved
eddies above the matching point. Page-local notation: $y_1$ the height of the
first element or cell, $y_1^+=y_1u_\tau/\nu_w$ (the height, not the centroid,
in [Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §1); $U_t$ the
tangential velocity at the sampling (feeding) point; $\beta_\omega$ the
destruction coefficient of the $\omega$ equation (registry §11; the sources'
$\beta$, $\beta_1$).

## Why wall functions are used

- **Stiffness of near-wall damping.** [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md)
  (§1) state that wall-resolved $k$-$\varepsilon$ models need ad hoc damping
  functions that increase stiffness, "for this reason, wall function
  approaches are usually employed" with the
  [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md); the
  [$k$-$\omega$ model](/methods/k-omega-model.md) integrates to the wall
  without damping, but $\omega\to\infty$ there and "usually requires very
  fine meshes".
- **Near-wall resolution of high-order RANS.** Ghidoni et al. (2026, §1)
  quote the first-cell height of wall-resolved RANS as $y_1^+\sim1$ for
  finite volumes and $y_1^+\sim10$ for discontinuous Galerkin (DG) methods, a
  rule of thumb they state rather than demonstrate; wall functions relax
  it, lower the element aspect ratio and cut the cost. They state that the
  only earlier wall-function implementation in a DG solver is that of
  Tiberga et al. for the $k$-$\varepsilon$ model (as cited).
- **Immersed boundaries and adapted meshes.** On non-body-fitted Cartesian
  grids the first fluid points cannot be placed at $y^+\approx1$ without
  octree refinement to the wall; [Constant et al. (2024)](/sources/constant-2024.md)
  impose a wall function at the target points of a Spalart–Allmaras
  [immersed boundary method](/methods/immersed-boundary-method.md) (§3), and
  [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) set $k$ and $\omega$
  by wall functions at the boundary nodes of a lattice Boltzmann solver
  (§2.2). [Husson et al. (2024)](/sources/husson-2024.md) (§1, §3.1) state
  that the isotropic Cartesian grids of lattice Boltzmann solvers make wall
  resolution prohibitive at high Reynolds number, so that an immersed
  boundary with a wall model "has become a standard choice"; theirs carries
  a Spalart–Allmaras law into RANS and the RANS zone of zonal DES (below).
  [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) (App. A,
  Fig. 32) run the RANS part of their aircraft-wake study, with a
  differential [Reynolds-stress model](/methods/reynolds-stress-model.md), on
  an anisotropically adapted mesh of about 110 M cells whose ten prism layers
  use wall functions with $y^+\approx80$ on the wing (see
  [mesh adaptation](/methods/mesh-adaptation.md)).

## Wall stress from an inverted law

**Implicit laws.** The log law, Reichardt's and Spalding's composite laws
must be inverted for $u_\tau$ by Newton iteration at every wall point; in a
high-order DG solver at every wall quadrature point, so the cost grows with
the polynomial degree $N$ (Ghidoni et al. 2026, §1, §3.3). Their reference
implicit law is Spalding's, printed (Eq. 12) as

$$y^+=u^++e^{-\kappa B}\left(e^{\kappa u^+}-1-\kappa u^+-\frac{(\kappa u^+)^2}{2!}\right),\qquad \kappa\sim0.41,\ B=5 .$$

Constant et al. (2024, §3.2) invert Musker's law by Newton–Raphson at an
image point; details on the [equilibrium wall model](/methods/equilibrium-wall-model.md)
page.

**An explicit power law.** Ghidoni et al. (2026, §3.3, Eqs. 13–15) replace
the implicit law by the power law of Wilhelm et al. (as cited), with
page-local constants $A_{\mathrm{pl}}=8.3$, $m_{\mathrm{pl}}=1/7$ and
$y_c^+=11.81$ ("non-dimensional height of the viscous sublayer"):

$$u^+=\begin{cases}y^+, & y^+\le y_c^+,\\ A_{\mathrm{pl}}\,(y^+)^{m_{\mathrm{pl}}}, & y^+>y_c^+,\end{cases}$$

which inverts in closed form,

$$u_{\tau,\mathrm{vis}}=\sqrt{\frac{\nu U_t}{y}},\qquad u_{\tau,\log}=\left(\frac{U_t}{A_{\mathrm{pl}}}\right)^{\frac1{1+m_{\mathrm{pl}}}}y^{-\frac{m_{\mathrm{pl}}}{1+m_{\mathrm{pl}}}}\nu^{\frac{m_{\mathrm{pl}}}{1+m_{\mathrm{pl}}}},$$

and the two branches are blended without a switch, after Menter et al. (as
cited), as $u_\tau=\left(u_{\tau,\mathrm{vis}}^4+u_{\tau,\log}^4\right)^{1/4}$.
The power law is continuous at $y_c^+$, since $8.3\times11.81^{1/7}=11.81$,
and the log branch is the exact inverse of $U_t/u_\tau=A_{\mathrm{pl}}(yu_\tau/\nu)^{m_{\mathrm{pl}}}$
*(compiler check, not in the sources)*. Despite assuming a zero pressure
gradient, the law "remains accurate even with moderate pressure gradients"
(§1), as the weak-APG test below shows.

**Defined at separation: a second velocity scale.** Where $U_t\to0$ the
inverted $u_\tau$ vanishes. Ghidoni et al. (§3.3, Eqs. 16–17) adopt the
two-velocity-scale approach of Ignat et al. (as cited), with
$u^*=\beta_\omega^{1/4}\sqrt{\max(0,k)}$ (the constant of the $\omega$
equation as printed), but because $\max(0,k)$ can be zero on low orders and
coarse meshes they replace Ignat et al.'s $\tau_w=\rho_wu^*u_\tau$ by

$$\tau_w=\rho_w\max(u^*,u_\tau)\,u_\tau .$$

**Feeding point and imposition.** The law is sampled at the internal
quadrature point of the wall-adjacent element farthest from the wall (nearest
the face opposite the wall), "following what is often proposed for WMLES",
under the constant-stress hypothesis that the stress there approximates
$\tau_w$; the choice keeps the sampled flow resolved, limits the dependence on
$N$ and keeps all computations element-local (§3.3, Fig. 1, Alg. 1). The
no-slip condition is replaced by the slip condition $\boldsymbol u\cdot\boldsymbol n=0$,
and in the wall viscous flux the tangential part of the traction is replaced
by $-\tau_w\boldsymbol t$, $\boldsymbol t$ the unit vector of the tangential
velocity (Eq. 19). The authors call it an "adaptive" wall function: nothing
requires the first element to lie in the log layer.

**A linearized law on an immersed boundary.** Husson et al. (2024,
§3.1–3.2, Eqs. 37–43) use the analytical law of the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) (Allmaras &
Johnson, as cited; formula and constants on the
[law of the wall](/definitions/law-of-the-wall.md) page), chosen because its
buffer layer is consistent with the model, in a lattice Boltzmann solver
([ProLB](/software/prolb.md)) with a sharp-interface direct-forcing
[immersed boundary](/methods/immersed-boundary-method.md) whose forcing nodes
lie on the fluid side. On coarse grids the near-wall gradients of the law are
"too steep to be well captured by the mesh", which causes oscillations and
a wrong skin friction; removing nodes below a threshold, as others do
(as cited), leaves too few nodes in thin inner layers. They therefore
linearize the law below a cut-off height $y_c$ (after Tamaki et al., as
cited),

$$u^+(y^+)=u^+(y_c^+)-(y_c^+-y^+)\,\frac{du^+}{dy^+}\Big|_{y_c^+},$$

so that the wall-normal gradient is constant and resolvable by finite
differences, and offset the momentum imbalance by a constant eddy viscosity
below $y_c$, replacing the damping function of the Spalart–Allmaras
eddy viscosity there by $f'_{v1}=r_{\mathrm{lin}}(\chi r_{\mathrm{lin}})^3/\big(c_{v1}^3+(\chi r_{\mathrm{lin}})^3\big)$,
$r_{\mathrm{lin}}=y_c/d$ ($\chi=\tilde\nu/\nu$; $y_c$, $r_{\mathrm{lin}}$
page-local). With the linear wall value $\chi=\kappa y^+$ this gives
$\nu_t/\nu=\chi f'_{v1}=\kappa y_c^+f_{v1}(\kappa y_c^+)$ at every $d<y_c$,
the value at the cut-off *(compiler check, not in the sources)*. The cut-off
is the interpolation-point distance, $y_c=d_{\mathrm{IP}}=2.5\Delta y$, fixed
"to limit local scheme staggering". At each forcing node: interpolate
density and velocity at the interpolation point by weighted least squares
from eight nodes; invert the law there by Newton–Raphson for $u_\tau$; set
the tangential velocity from the linearized law, the density equal to the
interpolated one, $\chi_F=\kappa y_F^+$ and the normal velocity by linear
extrapolation; overwrite the wall-normal velocity gradient, in the wall
frame, by an analytical value; and rebuild all distributions from the
equilibrium and first-order non-equilibrium parts (§3.2, steps 1–5). The
grids are coarse in wall units: $\Delta y^+\approx30$ on a flat plate,
15 at a backward-facing step and about 40 on the main element of a
three-element airfoil (§4). The authors cite earlier successes of the
linearization and state its limit: it rests, like the immersed-boundary
treatment, on the equilibrium hypothesis, so discrepancies are expected
near separation and in recirculation (§3.1).

**The same linearization on a moving Cartesian grid.** [Sugaya & Imamura (2021)](/sources/sugaya-2021.md)
(§2.2, Eqs. 10–15, Table 1) extend the immersed-boundary wall function of
Tamaki et al. (2017), as cited, to Cartesian grids that move rigidly with a
pitching airfoil or a rotor blade, for RANS and DDES with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) in the
compressible solver UTCart. Wall conditions are imposed at the face centres
between fluid cells and cells cut by the body; an image point lies on the
wall normal through each face centre at $d_{\mathrm{IP}}=2\Delta x$ from the
wall, located once at the start because the grid moves with the body, and
its values are interpolated linearly with the gradient of the containing
cell. The normal velocity varies linearly between the image point and the
wall velocity, and the tangential velocity is extrapolated with the slope of
the Spalart–Allmaras wall law $u^+=f_{\mathrm{wall}}(y^+)$ (formula not
printed; page-local $f_{\mathrm{wall}}$) at the image point,

$$u_{t,\mathrm{FC}}=u_{t,\mathrm{IP}}-u_\tau\,\frac{\partial f_{\mathrm{wall}}}{\partial y^+}\Big|_{y^+_{\mathrm{IP}}}\left(y^+_{\mathrm{IP}}-y^+_{\mathrm{FC}}\right),$$

with $u_\tau$ from Newton–Raphson on
$u_\tau f_{\mathrm{wall}}(y^+_{\mathrm{IP}})=u_{t,\mathrm{IP}}-V_{t,\mathrm{wall}}$,
$V_{t,\mathrm{wall}}$ the tangential wall speed (subscripts FC and IP for
face centre and image point, page-local); the original condition is
recovered for a wall at rest. Temperature is extrapolated linearly, and the
face-centre pressure is taken from the fluid cell next to the face instead of
the image point, a modification credited with "a small improvement" in
simple tests that are not shown. In the frame of the wall,
$u_{t,\mathrm{IP}}-V_{t,\mathrm{wall}}=u_\tau f_{\mathrm{wall}}(y^+_{\mathrm{IP}})$,
so the face-centre value lies on the tangent line of the wall law at the
image point *(compiler check, not in the sources)*. Because the grid moves with
the body, the boundary layer stays in the same cells and no cell changes
from solid to fluid, so the "fresh-cell" pressure oscillations of moving
immersed boundaries on fixed grids do not arise (§1, §2.2); the authors call
the combination of immersed boundaries, wall functions and moving grids on
Cartesian grids "the first study" of its kind (§1). The image-point heights
are $y^+_{\mathrm{IP}}\approx230$ at mid-chord on a steady NACA 0012 at
$Re=6\times10^6$, about 100 on the pitching NACA 0012 of AGARD Case 3 and up
to about 500 on the coarser of two [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md)
grids; they rely on earlier work, as
cited, for the statement that immersed boundaries with wall functions agree
with body-fitted grids for surface pressure "when $y^+$ is approximately 500
or less" (§3.1). On the steady airfoil the stationary and moving-grid runs
give density residuals equal to machine zero and pressure, skin friction,
velocity and eddy-viscosity profiles that agree with a body-fitted
Spalart–Allmaras reference (FaSTAR), and on the pitching airfoil the
lift hysteresis is reproduced and the pitching moment differs from the
experiment by about 0.005, "almost the same" as the body-fitted FUN3D
results, which the authors offer as indirect
evidence that the non-conservation of the immersed boundary does not spoil
the unsteady loads (§3.1–3.2; see [NACA 0012](/benchmarks/naca-0012-airfoil.md) and
[immersed boundary methods](/methods/immersed-boundary-method.md)).

## Turbulence variables next to the wall

The sources set $k$ and $\omega$ from the asymptotic solutions of the
$k$-$\omega$ equations in the sublayer and in the log layer:

| Source | Sublayer | Log layer | Combination |
|---|---|---|---|
| Ghidoni et al. (2026, Eq. 18), DG, wall boundary condition | $\omega_{\mathrm{vis}}=6\nu_w/(\beta_\omega y^2)$ | $\omega_{\log}=\max(u^*,u_\tau)/(\sqrt{\beta_\omega}\,\kappa y)$ | $\omega=\sqrt{\omega_{\mathrm{vis}}^2+\omega_{\log}^2}$; $\boldsymbol n\cdot\nabla k=0$ |
| Mozaffari et al. (2024, Eqs. 22–25), lattice Boltzmann, boundary nodes | $k=C_ku_\tau^2(y^+)^{3.23}$, $\omega_{\mathrm{vis}}=6\nu/(\beta_\omega y^2)$ | $k=u_\tau^2/\sqrt{C_\mu}$, $\omega_{\log}=u_\tau/(\sqrt{C_\mu}\,\kappa y)$ | switch at $y^+=11.06$ (Kalitzin et al., as cited); optional blend $\phi\,\omega_{b2}+(1-\phi)\omega_{b1}$, $\phi=\tanh\big((y^+/10)^4\big)$, $\omega_{b1}=\omega_{\mathrm{vis}}+\omega_{\log}$, $\omega_{b2}=(\omega_{\mathrm{vis}}^{1.2}+\omega_{\log}^{1.2})^{1/1.2}$ (Knopp et al., as cited) |

Mozaffari et al. print the $\omega$ values in wall units,
$6u_\tau^2/(\nu\beta_\omega y^{+2})$ and $u_\tau^2/(\nu\sqrt{C_\mu}\kappa y^+)$,
which equal the forms above; the values of $C_k$, $C_\mu$ and
$\beta_\omega$ are not printed, and whether the blend is used in their runs
is not stated. Ghidoni et al. modify $\omega_{\log}$ with
$\max(u^*,u_\tau)$ "to account for possible null $u^*$" (§3.3).

The sublayer exponent of $k$ follows from the model constants:
Elzaabalawy et al. (2023, §3.1.2, Eq. 58) print the viscous-sublayer
solution $k^+=C_k(y^+)^{p_k}$ with $p_k=\tfrac12+\sqrt{\tfrac14+6\beta^*/\beta_\omega}$
and $C_k$ between 0.0025 and 0.0032 depending on the $k$-$\omega$ version
(after Eça & Hoekstra, as cited). With $\beta^*=0.09$ and $\beta_\omega=0.075$
this gives $p_k=3.23$, the exponent of Mozaffari et al.; with Wilcox's 1998
value $\beta_\omega=0.072$ it gives 3.28 and with Ghidoni et al.'s 0.0708 it
gives 3.31 *(compiler check, not in the sources)*.

On an immersed boundary the turbulence variable is the
Spalart–Allmaras $\tilde\nu$: Constant et al. (2024, §3.2, Eq. 8) set it at
the target points from the mixing-length viscosity
$\nu_t=\kappa u_\tau y\,[1-e^{-y^+/19}]$ (see
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md)); Husson et al.
(2024, Eq. 42) set it at the forcing nodes as $\chi_F=\kappa y_F^+$, the
linear log-layer value that the Spalart–Allmaras damping function is built
to reproduce down to the wall (§2.2).

## Accuracy and cost in a high-order DG solver

Ghidoni et al. (2026) test the explicit wall function with the Wilcox
2006 $k$-$\omega$ model in logarithmic form in a modal DG solver
(BR2 lifting, $N\le6$, implicit pseudo-transient continuation), on meshes
with $y_1^+\in\{1,5,10,20,40,80,160,320\}$ obtained by removing wall layers
from a $y_1^+=1$ mesh while keeping the outer resolution (§4).

- **Zero-pressure-gradient flat plate** (Wieghardt, $Re=11.1\times10^6$ on
  the plate length, $M_\infty=0.096$; §4.1, Table 1). Against the
  wall-resolved $y_1^+=1$, $N=6$ solution the skin-friction error is below
  1 % from $N=3$ up to $y_1^+=10$. At $y_1^+=20$ it is not monotone in $N$
  (7.714 %, 0.043 %, 0.409 % at $N=1$–3, 5.514 % at $N=6$), which the authors
  attribute to feeding points in the buffer layer, where the law blends its
  two branches. At $y_1^+=40$ it is 3.833 % at $N=3$ and 0.162 % at $N=6$;
  for $y_1^+=80$, 160 and 320 it stays below 3 % from $N=3$ on. Convergence in
  $N$ is not ideal because the feeding point moves away from the wall as $N$
  grows (§4.1, §5).
- **Cost** (Table 2). The computing time falls, against the $y_1^+=1$ run
  without wall function, by 29.76, 34.14, 45.85, 59.54 and 68.96 % on average
  over $N=1$–6 for $y_1^+=20$, 40, 80, 160 and 320, with a maximum of 71.77 %
  ($N=3$, $y_1^+=320$). At $y_1^+=320$ the explicit law saves 68.96 % on
  average against 63.73 % for the iterative Spalding law.
- **Weak adverse pressure gradient** (Samuel & Joubert, $Re=5.95\times10^6$,
  $M_\infty=0.07$, Rotta–Clauser parameter 1.5–4.5; §4.2, Figs. 6–7). Skin
  friction agrees for every $y_1^+$ and $N$, but every mesh needs one degree
  more than in zero pressure gradient; at $N=6$ a discrepancy appears for
  $y_1^+>20$, mostly on the first part of the plate.
- **Strong adverse pressure gradient** (DLR/UniBw DM2 and DM3 plates of
  Knopp et al., $Re=3.4$ and $5.2\times10^7$, Rotta–Clauser parameter 25–45;
  §4.2, Fig. 8). Agreement deteriorates for $y_1^+>80$; at $N=6$ the
  skin-friction difference grows for $y_1^+=160$ and 320 near the end of the
  pressure-gradient region, $0.8<x/L<0.85$, because the power law refers to
  zero-pressure-gradient layers only. See the
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
- **Recirculation** ([backward-facing step](/benchmarks/backward-facing-step.md)
  of Driver & Seegmiller, $Re_H=36\,000$, $M_\infty=0.128$, $y_1^+\le80$;
  §4.3, Figs. 10–11). Pressure, skin friction, velocity and turbulence
  intensity agree for all $y_1^+$ and $N$ except the $N=6$ skin friction in
  the recirculation for $y_1^+>10$, where the law of the wall, valid only for
  developed turbulent boundary layers, returns wrong $u_\tau$; the
  under-predicted $c_f$ affects only the sublayer velocity, so the velocity
  and turbulence-intensity profiles still agree.
- **Airfoil** ([NACA 0012](/benchmarks/naca-0012-airfoil.md),
  $Re_c=6\times10^6$, $M=0.15$, $-15^\circ$ to $15^\circ$; §4.4,
  Figs. 13–14). Lift and drag agree for all $y_1^+$ and $N$; at $N=6$ the
  skin friction departs for $y_1^+>80$ near the leading edge, and at
  $y_1^+=320$ its peak is under-predicted with recovery from $x/c=0.15$, with
  negligible effect on lift and drag. At $15^\circ$ incipient separation
  appears from $x/c=0.72$, reattaching at the trailing edge.

The authors conclude that accuracy is preserved up to $y_1^+=320$ "with a
drastic computing time reduction" (Abstract, §5); their own strong-APG and
step results confine the statement to near-equilibrium boundary layers.

## The same airfoil with an immersed-boundary wall function

Constant et al. (2024) run the NACA 0012 at the same $Re_c=6\times10^6$ and
$M=0.15$ with a Spalart–Allmaras immersed-boundary wall function and find,
at $15^\circ$, that over the first 10 % of chord the boundary layer cannot be
represented by the wall function, and that a drag error of almost 20 % remains
after their corrections (§6.1; details on the
[equilibrium wall model](/methods/equilibrium-wall-model.md) and
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
pages). The two results concern different couplings: a feeding point inside
the first element of a body-fitted DG mesh, compared with the $y_1^+=1$
solution, against an immersed boundary with a modelling height set from a
target $y^+$ and a reconstructed wall pressure, compared with a body-fitted
wall-resolved reference. They are not two answers to one question.

## Pressure-gradient-aware laws

[Knopp (2022)](/sources/knopp-2022.md) (§1) builds an empirical log-law and
half-power-law description of adverse-pressure-gradient boundary layers with
the stated aim of improving RANS models and wall functions; the paper
implements no wall function. The correlations and their bounds are on the
[wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
page. Mozaffari et al. (2024) report "primary findings", without data, that
the adverse-pressure-gradient extension of Wilhelm et al. improves their
hybrid Ahmed-body results (lines 553–557); Ghidoni et al. (2026, §5) list
strong adverse pressure gradients, transonic and supersonic flow, unsteady
flow and hybrid RANS/LES as future work.

## The linearized law in separated flow

Husson et al. (2024, §4) assess the linearized law only inside their
hybrid computations (see [detached-eddy simulation](/methods/detached-eddy-simulation.md)).
On the zero-pressure-gradient flat plate of the NASA Turbulence Modeling
Resource ($Re_L=5\times10^6$, $M=0.2$, $\Delta y^+\approx30$) the RANS and
zonal-DES skin frictions are "identical" (§4.1.2). Behind the A3C
[backward-facing step](/benchmarks/backward-facing-step.md)
($Re_h=40\,000$, $\Delta y^+=15$ at the step, 44.7 M nodes) the mean
profiles agree with a wall-resolved body-fitted Navier–Stokes zonal DES on
3.9 M points, except near the wall at the first station, which the authors
attribute to the wall law imposing a zero-pressure-gradient profile in the
recirculation (§4.2.2, Fig. 11). On the LEISA2 three-element airfoil the
slat recirculation is slightly larger than in a wall-resolved LES and the
experiment, "partly" because of the wall model (§4.3.2, Fig. 18). The same
limit appears in the DG results of Ghidoni et al. (2026) above: the law of
the wall returns a wrong $u_\tau$ in recirculation.

## Wall-resolved alternatives in high-order RANS

Five high-order sources resolve the wall instead, and say what it takes:

- Ghidoni et al. (2026, §3, Eq. 4) impose, without wall function,
  $k_w=0$ and $\omega_w=6\nu_w/\big(\beta_\omega(a_Ny_1)^2\big)$ with
  $a_N=\exp\big(-\sum_{n=1}^N1/n\big)$ (page-local; the source's $\alpha^l$), an
  effective distance that shrinks with the degree $N$.
- Elzaabalawy et al. (2023, §3.1.2, Eq. 57, Fig. 3) remove every element
  touching the wall from the $\omega$ problem and impose the sublayer
  solution $\omega=6\nu/(\beta_\omega y^2)$, valid for $y^+<3$, on the new
  boundary, because a large wall value of $\omega$ "is not stable for
  high-order approximations"; robustness needs $y^+<3$ at the wall (§7).
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) transport
  $\ln\omega$ in a flux-reconstruction $k$-$\omega$ SST solver (see
  [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)) and impose at a
  no-slip wall the ghost value $\ln\big(60\mu/(\rho\beta_\omega d_1^2)\big)$,
  with $d_1$ the wall distance of the first solution point, because the
  theoretical distance zero would give an infinite value (§3.3.1, Eq. 88);
  the wall value thus depends on order and mesh. On the Wieghardt plate
  their high-order solutions are accurate with a first element at
  $y_1^+\simeq25$ "without wall functions", which they state is larger than
  what second-order finite-volume solvers without wall-extended functions
  allow (Abstract, §4.1, Fig. 10); no finite-volume comparison is shown.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) replace $\omega$
  by its inverse, the time scale of the [$k$-$\tau$ model](/methods/k-tau-model.md),
  whose wall condition is simply zero and whose source terms stay bounded,
  against the $\omega\sim y^{-2}$ singularity that an arbitrarily large
  wall value of $\omega$ handles in finite-volume codes but that leaves
  persistent oscillations and grid sensitivity in high-order codes (§1–2).
  In their spectral-element channel at $Re_\tau\approx5200$ the solution is
  insensitive to the first-point height, $y^+=1.7$ to 0.25 for polynomial
  degrees 3 to 9 (§3.1). Their finite-volume comparison runs set
  $\omega_w=6\nu/(\beta_\omega y^2)$ through OpenFOAM's `omegaWallFunction`
  at $y^+\sim1$ (§3.1); $k$-$\tau$ wall functions are reported in earlier
  work, as they cite it, and left to future application (§4).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) resolve the wall in a
  fourth-order finite-volume Spalart–Allmaras solver with $\rho\tilde\nu=0$
  at the wall and first cells at $y^+\approx0.5$–1 (§2.1, §3.1), and treat
  the cost of the resulting stretched cells in the reconstruction instead
  (see [boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)).

## Qualifications

- **Printed statements of Ghidoni et al. (2026) against their Table 1.**
  §4.1 states that at $y_1^+=1$ "already for $\mathbb P^1$ … the error is
  below 0.5 %", while Table 1 gives 1.970 % (0.416 % at $N=2$); §4.1 and §5
  state an error below 3 % "from $\mathbb P^3$" at $y_1^+=40$, while Table 1
  gives 3.833 % ($<3$ % from $N=4$); §4.1 places the minimum at $y_1^+=20$
  at $N=3$ "approximately 0.5 %", while the table's minimum is 0.043 % at
  $N=2$; and the claim that the time saving grows with $N$ on a fixed mesh is
  not monotone in Table 2 (71.77 % at $N=3$ against 66.84 % at $N=4$ for
  $y_1^+=320$). The Table 1 caption places the error "at $x/L=0.923$"
  while Eq. (20) defines a distribution average over 1000 wall points; the
  $y_1^+=1$ errors for $N=1$–3 are reproduced as pointwise relative errors
  of $c_f$ at $x/L=0.923$ against the $N=6$ value
  ($|2.479-2.431|/2.431=1.97$ %) *(compiler check, not in the sources)*.
- Ghidoni et al. print the turbulent stress with the negative convention
  ($\tau_{ij}=2\mu_t S^d_{ij}-\tfrac23\rho k\delta_{ij}$) and call it the
  total stress in the text, with the names of the turbulent and total
  stresses swapped relative to their formulas (§2).
- Ghidoni et al.'s Rotta–Clauser parameter (their $\beta_{RH}$) is
  $\delta^*/(\rho_wu_\tau^2)\,\partial p/\partial x$, the $\beta_{RC}$ of the
  adverse-pressure-gradient page.
- Mozaffari et al. (2024) reuse the symbol $\omega_{\log}$ on the left side
  of their blend (Eq. 24) for the blended value.
- **Analytical wall gradient of Husson et al. (2024).** Eq. (43) sets the
  wall-normal gradient of the tangential velocity at the forcing node to
  $u_{\tau,F}\,\big(c_{v1}^3+(\kappa y^+_{\mathrm{IP}})^3\big)/\big(c_{v1}^3+(\kappa y^+_{\mathrm{IP}})^3(1+\kappa y^+_{\mathrm{IP}})\big)$,
  "consistent with Equation (37)". The fraction is exactly $du^+/dy^+$ of
  the constant-stress layer with the Spalart–Allmaras eddy viscosity and
  $\chi=\kappa y^+$, since $(1+\chi f_{v1})\,du^+/dy^+=1$ gives
  $(c_{v1}^3+\chi^3)/(c_{v1}^3+\chi^3+\chi^4)$; the dimensional gradient is
  then $(u_\tau^2/\nu)\,du^+/dy^+$, so the printed prefactor $u_{\tau,F}$
  lacks a factor $u_\tau/\nu$, and the fraction is evaluated at the
  interpolation point while the left side is at the forcing node
  *(compiler check, not in the sources)*. In Eq. (41), the Newton update for
  $y^+$, the wall distance $y$ in $u_{t,\mathrm{IP}}y/\nu$ is not defined
  (the inversion is performed at the interpolation point, at distance
  $d_{\mathrm{IP}}$).

# Citations

- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1; §2; §3, Eq. (4); §3.3, Eqs. (12)–(19), Fig. 1, Alg. 1; §4.1, Tables 1–2; §4.2, Figs. 6–8; §4.3, Figs. 10–11; §4.4, Figs. 13–14; §5.
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1; §3.1.2, Eqs. (57)–(58), Fig. 3; §7.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.2, Eqs. (22)–(25); lines 553–557 (HAL accepted manuscript).
- [Constant et al. (2024)](/sources/constant-2024.md) — §3.2, Eqs. (6)–(8); §6.1 (HAL author manuscript).
- [Knopp (2022)](/sources/knopp-2022.md) — §1.
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — App. A, Fig. 32.
- [Husson et al. (2024)](/sources/husson-2024.md) — §1; §2.2; §3.1, Eqs. (36)–(39); §3.2, Eqs. (40)–(43); §4.1.2; §4.2.2, Fig. 11; §4.3.2, Fig. 18.
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — Abstract; §3.3.1, Eq. (88); §4.1, Figs. 9–10.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §1–2; §3.1, Table 1; §4.
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §2.1; §3.1.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §1; §2.2, Eqs. (10)–(15), Table 1; §3.1–3.2, Figs. 4–13; §4.
