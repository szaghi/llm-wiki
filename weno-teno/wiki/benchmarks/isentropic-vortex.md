---
type: Benchmark
title: "Isentropic vortex"
description: "Smooth exact solution of the Euler equations, an isentropic vortex advected by a uniform stream (or held steady) on a periodic box; used for design-order convergence studies, which expose the time-step scaling and multidimensional quadrature high orders need, and, with an amplified vortex strength, as a stress test of entropy-conservative fluxes."
status: established
aliases: [isentropic vortex advection, isentropic vortex evolution, vortex convection, steady isentropic vortex]
tags: [benchmark, weno, dg, entropy-stable, finite-volume]
timestamp: 2026-10-22T20:00:00Z
---

# Isentropic vortex

The isentropic vortex is a smooth, exact, time-dependent solution of the
compressible Euler equations: a vortex with Gaussian-type velocity and
temperature perturbations, at constant specific entropy $s$, superposed
on a uniform stream $(v_1,v_2)=(1,1)$ on a periodic square. Since the
exact solution is the initial data translated along the diagonal, the
error after any number of periods is measurable; Wang et al. and
Balsara et al. use it as their two-dimensional order-of-accuracy check
for the Euler equations, and Ranocha et al. call it "a widely used
benchmark problem" with an analytical solution. Without the stream the
vortex is steady, and the error is the deviation from the initial data
([Bryngelson et al. (2021)](/sources/bryngelson-2021.md)); a rotated
copy gives a three-dimensional test
([Li, Duan & Tang (2022)](/sources/li-2022-c.md)), and Lorentz-boosted
versions give relativistic and relativistic-MHD tests
([Chen & Wu (2022)](/sources/chen-2022-b.md),
[Duan & Tang (2022)](/sources/duan-2022.md)). Run for a hundred vortex
widths on a coarse grid, it is also a long-time robustness test of
kinetic-energy-preserving central schemes
([Edoh (2022)](/sources/edoh-2022.md)).

## Setup

Let $T=p/\rho$ be the temperature, $\mathcal E$ the vortex strength
and $r$ the distance from the vortex centre (page-local symbols). The
form printed by [Wang et al. (2023)](/sources/wang-2023-b.md) Example 3
and, in three dimensions, by
[Ranocha et al. (2023)](/sources/ranocha-2023.md) §4.1, Eq. (4.1) is,
in two dimensions,

$$
\begin{aligned}
T&=T_0-\frac{(\gamma-1)\mathcal E^2}{8\gamma\pi^2}\,e^{\,1-r^2},\qquad
\rho=\rho_0\Big(\frac{T}{T_0}\Big)^{1/(\gamma-1)},\qquad p=\rho T,\\
(v_1,v_2)&=(1,1)+\frac{\mathcal E}{2\pi}\,e^{(1-r^2)/2}\,(-\bar y,\ \bar x),
\end{aligned}
$$

with $(\bar x,\bar y)$ the position relative to the centre and
$\gamma=1.4$. The sources differ in normalization and strength:

| Source | Domain | $\mathcal E$ | Background | Final time / use |
|---|---|---|---|---|
| [Wang et al. (2023)](/sources/wang-2023-b.md) Example 3 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=T_0=1$ | $t=1$; $L^2$ error of $\rho$ on $\Delta x=1/2,\dots,1/64$ |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §VII.a | square periodic box; $[-10,10]^2$ and doubled time for orders 7 and 9 | not restated | not restated | design order, $64^2$ to $512^2$ |
| [Ranocha et al. (2023)](/sources/ranocha-2023.md) §4.1 | $[-5,5]^d$, $d=2,3$, periodic | 20 | $\rho_0=1$, $p_0=10$, $v_0=(1,1,0)$ | timing only, 8 elements per direction |
| [Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.1 | $[-10,10]^2$, centre $(-2,-2)$, periodic | 5 | $\rho_0=1$, temperature 1 with $c_v=1$, stream $(1,1)$ | $t=4$; $\ell^1$, $\ell^\infty$ errors of $\rho$, $N_x=40$ to $320$, moving mesh |
| Li, Duan & Tang (2022) Ex. 5.5 | $[-10,10]^3$, 2D vortex rotated onto the domain diagonal | 5 | as Ex. 5.1 | $t=0.1$; $N_x=40$ to $320$ |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.1 | $[-10,10]^2$ (enlarged from $[-5,5]^2$), periodic | amplitude not printed | $\rho_0=1$, $p_0=1/\gamma$, stream of Mach $\sqrt{2/\gamma}$ at $45°$ | one cycle; $100^2$ to $500^2$, CFL 0.6 down to 0.00625 |
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.4 | steady vortex, no stream; setup deferred to an earlier MFC paper | not printed | not printed | $\lVert\rho(1)-\rho(0)\rVert_\infty$, $1/N\in[10^{-3},10^{-1}]$ |
| [Chen et al. (2022)](/sources/chen-2022.md) §6.3, Eq. (32) | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=2$; density error on triangles with boundary spacing $h=0.4$ to $0.05$ (1966 to 122,204 cells); HLLC, four-stage RK, $\Delta t=0.002$ |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Exs. 4.2, 4.8 | $[0,14]^2$, centre $(7,7)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=0.2$; density errors, $h=14/10$ to $14/160$ (triangles) and point clouds |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.1.2 | $[-10,10]^2$, centre $(-5,-5)$ | 5 | $\rho_0=T_0=1$, stream $(1,1)$ | $t=10$; $L^2$, $L^\infty$ errors, $N_g=40$ to 640 triangles per direction |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.2.3, Eq. (45) | $[-10,10]^2$, periodic quadrilaterals | Gaussian of width $R_{\mathrm v}=1.5$, strength $S_{\mathrm v}=13.5$ | Mach 0.4, stream $(0,1)$ | one convective period; $L^2$ density error, $N=20$ to 67 |
| [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.3 | as Dzanic, Trojak & Witherden | as above | as above | one pass; $L^2$ error with $(2p)^2$ Gauss–Legendre points per element, $N=20$ to 67; cost on a V100 |
| [Edoh (2022)](/sources/edoh-2022.md) §4.1, Eqs. (27)–(28) | periodic, dimensional | 4 (dimensionless factor of $\sqrt{R_{\mathrm g}T_\infty}$), Gaussian exponent factor $\phi_{\mathrm v}=1$ | $\rho_\infty=1$ kg m$^{-3}$, $\rho v_{1,\infty}=200$ kg m$^{-2}$s$^{-1}$, $\rho e_{o,\infty}=305714.3$ | 100 vortex widths; 60 points per direction; density error, kinetic energy, entropy |

Wang et al. print $\rho=\big(1-\frac{25(\gamma-1)}{8\gamma\pi^2}e^{1-r^2}\big)^{1/(\gamma-1)}$,
which is the table's form with $\mathcal E=5$, $T_0=1$. Balsara et al.
take the setup of Pao & Salas as described in Balsara & Shu, without
restating its parameters. Wang et al. take theirs from three earlier
papers, Ranocha et al. cite Shu.

The other normalizations reduce to the same vortex *(compiler check, not
in the sources)*. Li et al. write $p=(\gamma-1)\rho T$ with $c_v=1$, so
their temperature perturbation $-\mathcal E^2e^{1-r^2}/(8\gamma\pi^2)$
is the table's $T$-perturbation divided by $\gamma-1$; their velocity
perturbation turns the other way, $\propto(\bar y,-\bar x)$.
Sciacovelli et al. write the perturbations through a Gaussian
$\Omega=A_\Omega e^{-r^2/2}$ with an amplitude $A_\Omega$ they do not print (page-local symbols), $\delta v=\Omega(-\bar y,\bar x)$,
$\rho=(1-\tfrac{\gamma-1}2\Omega^2)^{1/(\gamma-1)}$ and
$p=\rho^\gamma/\gamma$; this is the table's form with
$\mathcal E=2\pi A_\Omega e^{-1/2}$ and $T_0=1/\gamma$, i.e. unit background
sound speed. Sciacovelli et al. enlarge the domain to $[-10,10]^2$ "to
reduce artificial shear layers at boundaries", and Li et al.,
Yu & Hesthaven, the two Dzanic papers and Balsara et al. (orders 7
and 9) use the same box. Chen et al. (2022), Du et al. and Yu &
Hesthaven print the table's form with $\mathcal E=5$ and unit
background; Du et al. write it through $\delta T$ with $T=p/\rho$ and
zero entropy perturbation.

Two sources use other profiles. Dzanic, Trojak & Witherden and Dzanic &
Witherden write the perturbation through
$\varphi_{\mathrm v}(r)=\exp\big((1-r^2)/(2R_{\mathrm v}^2)\big)$, velocity
$(V_x,V_y)+\frac{S_{\mathrm v}}{2\pi R_{\mathrm v}}\varphi_{\mathrm v}\,(\bar y,-\bar x)$
and pressure
$\frac1{\gamma M^2}\big(1-\frac{S_{\mathrm v}^2M^2(\gamma-1)}{8\pi^2}\varphi_{\mathrm v}^2\big)^{\gamma/(\gamma-1)}$,
with $S_{\mathrm v}=13.5$, $R_{\mathrm v}=1.5$, $M=0.4$,
$(V_x,V_y)=(0,1)$ (page-local symbols $\varphi_{\mathrm v}$, $S_{\mathrm v}$,
$R_{\mathrm v}$, $V_x$, $V_y$): a wider Gaussian at a fixed background
Mach number. Edoh writes a dimensional vortex with
velocity perturbation
$\sqrt{R_{\mathrm g}T_\infty}\,\frac{\mathcal E}{2\pi}e^{\phi_{\mathrm v}(1-r^2)}(-\bar y,\bar x)$
and temperature perturbation
$-T_\infty\frac{\mathcal E^2(\gamma-1)}{16\phi_{\mathrm v}\gamma\pi^2}e^{2\phi_{\mathrm v}(1-r^2)}$,
$\mathcal E=4$, $\phi_{\mathrm v}=1$, isentropic pressure
($R_{\mathrm g}$ the gas constant and $\phi_{\mathrm v}$ the exponent
factor, page-local symbols); with $\phi_{\mathrm v}=\tfrac12$ it is the table's
form scaled by $\sqrt{R_{\mathrm g}T_\infty}$, so $\phi_{\mathrm v}=1$
is a narrower vortex. He does not print $\gamma$; with $\gamma=1.4$ his
background is $p_\infty=114285.7$ Pa, $c_\infty=400$ m s$^{-1}$, Mach 0.5,
the centre temperature drops by $21.4\,\%$ and the minimum density is
$0.5479$ kg m$^{-3}$, the value he prints *(compiler check, not in the
sources)*, which supports $\gamma=1.4$.

### Relativistic versions

[Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.1 (arXiv v1) move a
[relativistic](/definitions/relativistic-hydrodynamics.md) isentropic
vortex along $(-1,-1)$ with speed $w=0.5\sqrt2$ on $[-5,5]^2$:
$\rho=(1-\alpha_{\mathrm r}e^{1-r^2})^{1/(\gamma-1)}$, $p=\rho^\gamma$,
$\alpha_{\mathrm r}=\frac{(\gamma-1)/\gamma}{8\pi^2}\mathcal E^2$
(page-local symbols for the source's vortex parameters), with
Lorentz-boosted coordinates and velocities, on five triangular meshes
of 932 to 238,592 cells. With $\mathcal E=5$ no limiter is
needed and the $\ell^1$ and $\ell^2$ density orders reach 2.9971 and
3.0015 (Table 1). With $\mathcal E=10.0828$ the minimum
pressure is $1.78\times10^{-20}$ and density $7.8\times10^{-15}$; the
physical-constraint-preserving limiter is required, acts on 1.502 % of
the cells on the coarsest mesh and on none on the finest, and the
orders reach 3.05 and 3.07 (Table 2). Duan & Tang (2022) Ex. 6.1 run a
relativistic-MHD vortex, $\rho=(1-\sigma_{\mathrm r}e^{1-r^2})^{1/(\gamma-1)}$,
$\sigma_{\mathrm r}=0.2$, magnetic amplitude $B_0=0.05$, $\gamma=5/3$,
moving with $(-0.5,-0.5)$ on $[-5,5]^2$ to $t=4$, on prescribed and
adaptive moving meshes (arXiv v1), and its three-dimensional
counterpart on $[-5,5]^2\times[-25,25]$ to $t=0.1$ (Ex. 6.7).

## Uses in the sources

**Design-order verification.** Balsara et al. use it to show that
their [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md)
reaches design order for conservation laws with
[WENO-AO](/methods/weno-ao.md) and multi-resolution WENO weights of
orders 3, 5, 7 and 9, LLF flux, CFL 0.3. Density $L_1$ rates at the
finest grid: WENO-AO-3 2.59 ($512^2$), AO-(5,3) 4.97, AO-(7,3) 6.93
($L_1$ error $5.18406\times10^{-10}$ at $512^2$), AO-(9,3) 8.78
($1.01355\times10^{-10}$ at $384^2$); multi-resolution WENO 2.74, 4.68,
6.93, 8.78 (Table I). The domain and the final time are doubled for
orders 7 and 9.

**Fifth-order A-WENO with the time-step tied to the grid.** Wang et
al. run their [A-WENO](/methods/alternative-weno.md) schemes with the
adaptive-diffusion central-upwind flux (NEW) and the earlier central flux
(OLD) with CFL number $\Delta x^{2/3}$. Then $\Delta t\propto\Delta x^{5/3}$
and the third-order SSP-RK error scales like $\Delta x^5$, the spatial
design order *(compiler check, not in the sources)*. Both reach fifth
order, with irregular rates: OLD 3.27, 2.39, 6.38, 4.99, 6.20; NEW
3.24, 2.36, 6.37, 4.98, 6.22. The $L^2$ density errors at
$\Delta x=1/64$ are $3.45\times10^{-9}$ (OLD) and $3.62\times10^{-9}$
(NEW); the NEW errors are slightly larger on every grid (Table 1).

**Ninth order and the time-integration error.** Sciacovelli et al. run
a ninth-order central-difference scheme with Jameson-type adaptive
[artificial dissipation](/methods/artificial-viscosity.md) and the
third-order TVD Runge–Kutta method of Gottlieb & Shu. At constant CFL
the observed order wanders between 3 and 9: a ninth-order range appears
only for CFL $\le0.2$, and ninth order holds over the whole range
$100^2$–$500^2$ only at CFL $1.25\times10^{-2}$ and
$6.25\times10^{-3}$ (§4.1, Fig. 2). They explain the behaviour by the
error balance: keeping the ratio of temporal to spatial error fixed
needs $\Delta t\propto\Delta x^{9/3}=\Delta x^3$, whereas a constant CFL
gives $\Delta t\propto\Delta x$ (Eq. 40). The same balance is what
Wang et al.'s CFL $\Delta x^{2/3}$ and Li et al.'s
$\Delta t=C_{\mathrm{CFL}}(\min\Delta\xi_k)^{5/3}$ (Li et al., §5) realize
for fifth order with a third-order integrator: across the sources, a
convergence study above third order with SSP-RK3 is only meaningful
with a refined time step or a small CFL. See
[SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md).

**Second order on unstructured triangles.** Chen et al. (2022)
use the vortex to check that their nonlinear vertex weighting of
[unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md)
does not degrade second order: every method is about second order
except node-averaging Green–Gauss with inverse-distance weights, whose
last order is 0.86; the vertex-based method gives $3.29\times10^{-3}$,
$5.98\times10^{-4}$, $1.34\times10^{-4}$, $3.59\times10^{-5}$ (orders
2.46, 2.16, 1.90), and with the nonlinear weighting $4.02\times10^{-3}$,
$6.12\times10^{-4}$, then the same values, so the weighting costs
accuracy only on the coarse meshes (§6.3, Table 1).

**Limiters and artificial viscosity must leave the order intact.**
Du et al. deliberately lower the KXRCF threshold ($C_k=10^{-4}$ on
triangles, $10^{-3}$ on point clouds) so that many smooth cells are
flagged; both the original and their improved
[simple WENO limiter](/methods/weno-limiter-dg.md) keep the order and
error magnitude of the unlimited DG, the improved one saving between
0.13 % and 35.60 % of the CPU time on triangles (Tables 4.4–4.6) and
up to 57.82 % on point clouds (Tables 4.14–4.16). Yu & Hesthaven's
ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md)
fires only on the coarsest grid ($N_g=40$), giving inflated apparent
orders on the first refinement ($P^4$: 10.2 in $L^2$), and is identical
to the inviscid DG afterwards (Table 3). Dzanic, Trojak & Witherden's
residual-based viscosity gives $L^2$ density rates that "met or
exceeded" $p+1$: 3.30, 4.93, 5.53, 7.44, 7.79, 8.74 for
$\mathbb P_2$–$\mathbb P_7$, with maximum viscosity components falling
from $O(10^{-7})$ at $N=20$ to $O(10^{-9})$ at $N=40$ for $\mathbb P_7$
(§5.2.3, Table 2). Dzanic & Witherden's
[entropy filter](/methods/entropy-filtering.md) gives rates
"generally in the range of $p$ to $p+1$", 2.59, 4.00, 4.27, 6.73, 6.10,
8.13 (Table 5), and costs 1.1, 1.7 and 2.0 % more time-to-solution for
5, 10 and 20 bisection iterations ($N=40$, $\mathbb P_3$, V100, five
flow-throughs; §5.1.3). The unlimited schemes themselves fall below
$N+1$ on some of these runs: Du et al.'s unlimited $P^2$ DG has $L^2$
orders 2.64–2.70 on triangles (Table 4.5) and $P^1$ $L^\infty$ orders
about 1.6 on point clouds (Table 4.11), and Yu & Hesthaven's inviscid
$P^2$ about 2.1–2.2 (Table 3); neither paper comments on it.

**Long-time robustness of kinetic-energy-preserving splittings.** Edoh
runs a sixth-order compact central scheme (CD06) on 60 points per
direction, about six across the vortex, with RK4 at
$\Delta t=1.74\times10^{-4}$ s for 100 vortex widths. Without filtering
the divergence form is unstable within five widths and his rotational
form within fifteen, while the Feiereisen and Kennedy–Gruber splittings
survive 100 widths with noise; with solution filtering all are stable
and the rotational form has the lowest density error. After 100 widths
the minimum density is $0.5479$ exact, $0.5069$ Feiereisen, $0.4490$
Kennedy–Gruber and $0.6261$ rotational form (§4.1, Figs. 1–2). See
[split convective forms](/methods/split-convective-forms.md) and
[kinetic energy preservation](/properties/kinetic-energy-preservation.md).

**Moving meshes and entropy.** Li et al. advect the vortex on an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) (monitor built
from $\lvert\nabla\rho\rvert$ and $\lvert\Delta\rho\rvert$) with
entropy-stable fluxes whose dissipation uses
[multi-resolution WENO](/methods/multi-resolution-weno.md) and reach
fifth order in $\ell^1$ and $\ell^\infty$ at $t=4$ (Ex. 5.1, Fig. 5.2),
and the expected fifth order in three dimensions at $t=0.1$ (Ex. 5.5,
Fig. 5.6). The same runs check [entropy stability](/properties/entropy-stability.md):
the total entropy stays almost constant with the
[entropy-conservative flux](/methods/entropy-conservative-flux.md) and
decays with the entropy-stable one, to about $-4.2\times10^{-6}$ at
$t=4$ on $160^2$ in 2D and to about $-1\times10^{-7}$ by $t=0.1$ in 3D.
Duan & Tang reach sixth order with their entropy-conservative scheme on
a prescribed moving mesh and fifth order with the entropy-stable one on
an adaptive mesh, for the relativistic-MHD vortex in two and three
dimensions, the entropy flat in the former and decaying in the latter
(Exs. 6.1, 6.7, Figs. 6.3–6.4, 6.13).

**Multidimensional finite-volume quadrature.** Bryngelson et al. use
the steady vortex to verify the finite-volume WENO5 scheme of
[MFC](/software/mfc.md): the $L^\infty$ density error converges at
second order when face fluxes are evaluated at face midpoints and at
fifth order with a $2\times2$ Gauss rule on each face, so "the
4th-order-accurate cell averaging we employ is required to achieve
5th-order accuracy associated with the WENO reconstructions" in
multiple dimensions (§5.4, Fig. 5a).

**Implementation stress test.** Ranocha et al. raise the strength to
$\mathcal E=20$ "to make sure that all possible paths in the logarithmic
mean are followed" in the [entropy-conservative fluxes](/methods/entropy-conservative-flux.md)
of [flux-differencing DG](/methods/flux-differencing.md). They report
no errors: the vortex is used to time
[Trixi.jl](/software/trixi-jl.md) against [FLUXO](/software/fluxo.md)
(Trixi.jl: 50 steps of a 9-stage fourth-order RK with error-based step
control; FLUXO: 90 steps of a 5-stage fourth-order RK; the same number
of right-hand-side evaluations) and in single-element microbenchmarks.
Precomputing $\ln\rho$ and $\ln p$ speeds the volume terms up by about
10 % on this vortex, against 25–55 % on sinusoidal and 60–75 % on random
data, because near-constant states take the Taylor branch of the
logarithmic mean (§7.2, Fig. 6).

## Qualifications

- Wang et al. print "$r=(x-5)^2+(y-5)^2$" while the formulas use
  $e^{1-r^2}$; the formulas are consistent only with
  $r^2=(x-5)^2+(y-5)^2$, i.e. with $r$ the distance from the centre as
  Ranocha et al. define it.
- The irregular rate sequence of Wang et al. (2.36–2.39 on the third
  refinement) is printed without comment.
- Ranocha et al. report timings only; their strengthened vortex
  carries no accuracy result.
- Bryngelson et al. call the $2\times2$ Gauss rule fourth-order accurate
  and observe fifth order. A face-average error of order
  $\Delta x^4$ bounds the formal order of the scheme at four *(compiler
  check, not in the sources)*; the paper does not comment on the
  observed slope of five. They also print the Gauss points as
  $y_j+(2l+1)\Delta y_j/(2\sqrt3)$, $l=1,2$, which lie outside the face;
  the two-point Gauss points are $y_j\pm\Delta y_j/(2\sqrt3)$.
- Bryngelson et al.'s vortex is steady, so it tests the spatial operator
  without transport across the grid; it is not the advected benchmark
  of the other sources.
- Sciacovelli et al. do not print the amplitude $A_\Omega$, so their
  error levels cannot be reproduced from the paper; their scheme is a
  central scheme with artificial dissipation, not a WENO scheme.
- Du et al.'s final time $t=0.2$ moves the vortex only 0.2 units along
  each axis, a short test of the advection.
- Chen & Wu state $t=1$ in the text and $t=0.15$ in the captions of
  Tables 1–2. They state $\gamma=5/3$ as the default and no other value
  for Ex. 4.1, but with $\gamma=5/3$ and $\mathcal E=10.0828$,
  $1-\alpha_{\mathrm r}e=-0.40<0$ and the density is undefined at the
  centre, whereas $\gamma=1.4$ gives $1-\alpha_{\mathrm r}e=2.28\times10^{-6}$,
  $\rho_{\min}=7.83\times10^{-15}$ and $p_{\min}=1.78\times10^{-20}$,
  the printed minima *(compiler check, not in the sources)*; the strong
  case was therefore run with $\gamma=1.4$, as their Ex. 4.10 states for
  the same vortex.
- Dzanic & Witherden print the density as $p^{1/\gamma}$ with $p$
  undefined; if $p$ is the printed pressure, the far-field density is
  $(1/(\gamma M^2))^{1/\gamma}\neq1$, and the isentropic density
  consistent with it would be $(\gamma M^2p)^{1/\gamma}$ *(compiler check,
  not in the sources)*.
- Edoh calls the vortex diameter "approximately 2.1 [m]", identified by
  $\delta T/T_\infty=0.001$. With $\gamma=1.4$ his printed temperature
  perturbation is $0.02895\,e^{2(1-r^2)}T_\infty$, which equals
  $0.001\,T_\infty$ at $r=1.64$, a diameter of about 3.3 m; 2.1 m
  corresponds to a threshold of about 0.024, both computed with the
  unprinted $\gamma=1.4$ *(compiler check, not in the sources)*. The threshold or the
  diameter is misprinted, or the diameter is defined otherwise.
- Yu & Hesthaven's DG solution and Du et al.'s unlimited DG are the
  baselines of their tests; the sub-design orders above are those of
  the baselines, not of the shock-capturing devices.

# Citations

- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 3, Table 1.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VII.a, Table I.
- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §4.1, Eq. (4.1); §7.2, Fig. 6 (arXiv v2).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §5, Eq. (5.1), Ex. 5.1, Fig. 5.2; Ex. 5.5, Fig. 5.6 (arXiv v1).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §4.1, Eqs. (37)–(40), Fig. 2 (arXiv v1).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.1, Eqs. (29)–(30); §5.4, Fig. 5a (arXiv v1).
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.3, Eq. (32), Table 1.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — Exs. 4.2, 4.8, Tables 4.4–4.6, 4.11, 4.14–4.16.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.1.2, Table 3.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.2.3, Eq. (45), Table 2 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.3, Eq. (29), Table 5 (arXiv v3).
- [Edoh (2022)](/sources/edoh-2022.md) — §4.1, Eqs. (27)–(28), Figs. 1–2.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.1, Tables 1–2 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — Exs. 6.1, 6.7, Figs. 6.3–6.4, 6.13 (arXiv v1).
