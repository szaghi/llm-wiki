---
type: Method
title: "Semi-implicit all-Mach schemes"
description: "Semi-implicit all-Mach schemes split the Euler or MHD equations into explicitly treated material waves and implicitly treated acoustic (and, in one MHD scheme, magnetic) waves, so the time step follows the flow speed; the page compares splittings by hyperbolicity, asymptotic consistency and contact preservation, and implicit parts solved by one linear pressure equation or Picard iteration."
status: established
aliases: [all-Mach scheme, all-speed semi-implicit scheme, low-Mach semi-implicit scheme, SI-IMEX WENO, S4T3, all sonic Mach MHD scheme, AP WENO-CT, pressure-based semi-implicit MHD, flux-vector-splitting semi-implicit scheme]
tags: [asymptotic-preserving, imex, semi-implicit, all-mach, finite-difference, weno, characteristic, low-dissipation, mhd]
timestamp: 2026-10-24T05:57:00Z
---

# Semi-implicit all-Mach schemes

An **all-Mach** (all-speed) scheme for the compressible Euler equations stays stable and
accurate from shocked compressible flow down to the incompressible limit. In the
non-dimensional equations with reference Mach number $\varepsilon$ (page-local; not the
WENO regularization $\epsilon$), the acoustic eigenvalues $v\cdot n\pm c/\varepsilon$ along a unit normal $n$ force
an explicit step $\Delta t=O(\varepsilon\Delta x)$, and upwind numerical viscosity grows like
$\varepsilon^{-1}$ ([Boscarino et al. (2022)](/sources/boscarino-2022.md), §2). A
**semi-implicit** scheme treats the material waves explicitly and the acoustic waves
implicitly, so that the step is set by the material speed. The scheme of this page is the
one of Boscarino et al., which combines a pressure splitting, a linearized equation of state,
a partitioned [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) integrator and fifth-order
finite-difference WENO.

## Scaled equations and the low-Mach limit

As recalled by Boscarino et al. (§2, Eqs. (2.1)–(2.8)), the scaled full Euler system is

$$\partial_t\rho+\nabla\cdot(\rho v)=0,\qquad
\partial_t(\rho v)+\nabla\cdot(\rho v\otimes v)+\frac1{\varepsilon^2}\nabla p=0,\qquad
\partial_tE+\nabla\cdot\big((E+p)v\big)=0,\qquad
E=\frac{p}{\gamma-1}+\frac{\varepsilon^2}2\rho\lvert v\rvert^2 ,$$

with $c=\sqrt{\gamma p/\rho}$ the sound speed multiplied by $\varepsilon$. The expansion
$p=p_0+\varepsilon^2p_2+\dots$, $v=v_0+\varepsilon v_1+\dots$ gives, with no-slip or periodic
boundaries, $p_0$ constant in space and time, $\nabla\cdot v_0=0$ and the incompressible Euler
equations with hydrodynamic pressure $p_2$, which solves
$-\nabla\cdot\big(\rho_0^{-1}\nabla p_2\big)=\nabla\cdot\big((v_0\cdot\nabla)v_0\big)$.
Initial data are **well prepared** when $p(0,x)=p_0+\varepsilon^2p_2(0,x)+\dots$ with $p_0$
constant and $v(0,x)=v_0(x)+O(\varepsilon)$ with $\nabla\cdot v_0=0$; otherwise an initial
layer of width $O(\varepsilon)$ in time appears (Eq. (2.9)).

## Flux splitting

The flux is split as $f=f_E+f_{SI}$ (page-local, Eqs. (3.10)–(3.11)), the subscripts $E$ and
$I$ marking explicitly and implicitly treated values:

$$f_E=\begin{pmatrix}(\rho v)_E\\ \dfrac{(\rho v)_E\otimes(\rho v)_E}{\rho_E}+\alpha_{\mathrm s}p_E\mathbb I\\ 0\end{pmatrix},\qquad
f_{SI}=\begin{pmatrix}0\\ \dfrac{1-\alpha_{\mathrm s}\varepsilon^2}{\varepsilon^2}p_I\mathbb I\\ \dfrac{E_E+p_E}{\rho_I}(\rho v)_I\end{pmatrix},$$

with splitting parameter $\alpha_{\mathrm s}$ (page-local) **fixed**: $\alpha_{\mathrm s}=1$ for
$\varepsilon<1$, so that the explicit part keeps a hyperbolic structure with a much smaller
sound speed, and $\alpha_{\mathrm s}=1/\varepsilon^2$ for $\varepsilon\ge1$, where the implicit
pressure term vanishes and the update becomes explicit. Boscarino et al. state two
differences from Cordier, Degond and Kumbaro, whose splitting parameter depends on
$\varepsilon$: the fixed $\alpha_{\mathrm s}$, and the implicit density $\rho_I$ in the energy
flux, which they say gives "a better asymptotic preserving property" (§3.1).

**Linearized equation of state** (Eq. (3.12)). The kinetic energy is always evaluated
explicitly, $E_I=\frac{p_I}{\gamma-1}+\varepsilon^2\frac{\lvert(\rho v)_E\rvert^2}{2\rho_E}$, so
the implicit stage is linear in $p_I$. With the pressure perturbation
$p_2=(p_I-\bar p_E)/\varepsilon^2$ (page-local; $\bar p_E$ the spatial mean of $p_E$, after
Park and Munz), $\varepsilon^{-2}\nabla p_I=\nabla p_2$ (Eqs. (3.13)–(3.14)).

## First-order scheme

The first-order step (§3.1, Eqs. (3.15)–(3.19)) is

$$\begin{aligned}
&\frac{\rho^{n+1}-\rho^n}{\Delta t}+\nabla\cdot(\rho v)^n=0,\\
&\frac{(\rho v)^{n+1}-(\rho v)^n}{\Delta t}+\nabla\cdot\Big(\frac{(\rho v)^n\otimes(\rho v)^n}{\rho^n}+p^n\mathbb I\Big)+\frac{1-\varepsilon^2}{\varepsilon^2}\nabla p^{n+1}=0,\\
&\frac{E^{n+1}-E^n}{\Delta t}+\nabla\cdot\big(\bar H^n(\rho v)^{n+1}\big)=0,\qquad \bar H^n=\frac{E^n+p^n}{\rho^{n+1}},
\end{aligned}$$

with $\bar H$ page-local (not the registry's specific enthalpy $H$). It is solved in four
steps: $\rho^{n+1}$ explicitly; $(\rho v)^{n+1}=(\rho v)^*-\Delta t\frac{1-\varepsilon^2}{\varepsilon^2}\nabla p^{n+1}$
with an explicit predictor $(\rho v)^*$; substitution into the energy equation and the
equation of state, which gives the **linear elliptic equation**

$$\frac{\varepsilon^2}{\gamma-1}p_2^{n+1}-\Delta t^2(1-\varepsilon^2)\nabla\cdot\big(\bar H^n\nabla p_2^{n+1}\big)=E^{**}$$

with $E^{**}$ explicit; then the momentum and energy updates. This step is the type-A IMEX
tableau of first order applied to the partitioned system (Remark 3.1).

## High order in time and space

**Time.** High order comes from the partitioned semi-implicit IMEX Runge–Kutta form with the
stiffly accurate type-A tableaux SI-IMEX(4,4,3) and SI-IMEX(3,3,2)
([IMEX Runge–Kutta](/methods/imex-runge-kutta.md)); each implicit stage $i$ needs one linear
elliptic equation of the same form, with $\Delta t$ replaced by $\mathsf a_{ii}\Delta t$
(page-local diagonal coefficient), and $u^{n+1}$ is the last stage (Eqs. (3.33)–(3.40)).
Type A is required because with a zero first diagonal entry the first stage has no pressure
equation (§3.2.2).

**Space** (§3.3). Conservative [finite differences](/definitions/conservative-finite-difference-scheme.md)
on a uniform Cartesian grid:

- $\nabla\cdot f_E$ by fifth-order [WENO](/methods/weno-js-reconstruction.md) on a global
  [Lax–Friedrichs splitting](/methods/lax-friedrichs-flux.md) with the Mach-dependent speed
  $a_\varepsilon=\max\big(\lvert v_1\rvert+\lvert v_2\rvert+\min(1,1/\varepsilon)\,c\big)$
  (page-local, Eq. (3.32)), which excludes the fast acoustic speed for $\varepsilon<1$, in the
  local [characteristic](/methods/characteristic-decomposition.md) fields of the Euler system
  **with $\varepsilon=1$**;
- $\nabla\cdot f_{SI}$ by component-wise fifth-order WENO, described as "with zero numerical
  diffusion" (§1, §5.6);
- the second-order operator $\nabla\cdot(\bar H\nabla p_2)$ by a fourth-order compact central
  difference.

The resulting scheme S4T3 is called fourth order in space (because of the compact elliptic
operator) and third order in time; S2T2 pairs SI-IMEX(3,3,2) with a second-order TVB
reconstruction ($M=1$ in the source's notation). The step is $\Delta t=\nu\Delta x/a_\varepsilon$
with $\nu=0.25$ in all tests, independent of the acoustic speed for $\varepsilon<1$ (§5).

## Asymptotic properties

- **Asymptotic preservation** (Thm. 4.1). For well-prepared data at $t^n$, inserting the
  expansion into the first-order scheme gives $\nabla p_0^{n+1}=0$ at $O(\varepsilon^{-2})$ and,
  at $O(1)$, $\frac{p_0^{n+1}-p_0^n}{\Delta t}+\gamma p_0^n\nabla\cdot v_0^{n+1}=0$; integrating
  over the domain (no-slip or periodic) gives $p_0^{n+1}=p_0^n$ and $\nabla\cdot v_0^{n+1}=0$
  **exactly**, so the limit is a consistent scheme for incompressible Euler, with a discrete
  pressure-Poisson equation (§4.1). The exact cancellation rests on $\rho^{n+1}$ in $\bar H^n$:
  with $\rho^n$, as in Cordier, Degond and Kumbaro, the leading-order divergence is
  $O(\Delta t)$ (Remark 4.2). See [asymptotic preservation](/properties/asymptotic-preservation.md).
- **Asymptotic accuracy** (Def. 4.3, Prop. 4.4). A semi-implicit scheme is asymptotically
  accurate if it keeps its temporal order on the limit system; an order-$r_{\mathrm{RK}}$
  SI-IMEX-RK scheme with stiffly accurate implicit part, on well-prepared data, gives a
  constant limit pressure, $\nabla\cdot v^1\to0$ and the incompressible solution up to
  $O(\Delta t^{r_{\mathrm{RK}}+1})$ after one step. Proof by induction over stages; stage 1 is
  the first-order analysis with $\Delta t\to\mathsf a_{11}\Delta t$, which needs
  $\mathsf a_{11}\ne0$. Both results are formal and time-semi-discrete (space continuous).

## Evidence

All tests with $\gamma=1.4$ (§5):

- smooth 1D colliding pulses at $\varepsilon=10/11$: $L^1$ pressure errors from
  $1.62\times10^{-2}$ ($N_x=40$) to $1.34\times10^{-6}$ ($N_x=320$), orders 4.02, 4.82, 4.72,
  "between 4 and 5, due to the dominance of spatial errors" (Table 5.1); at $\varepsilon=1/11$
  on 22 points S4T3 is closer to the reference than S2T2 (Fig. 5.1);
- 2D smooth test at $t=0.02$: about fourth order at $\varepsilon=1$, fifth order at
  $\varepsilon=10^{-6}$ (5.34, 5.22), order reduction at intermediate $\varepsilon$ (0.91 at
  $\varepsilon=10^{-2}$ on the last refinement; sweep over $[10^{-6},1]$ in Fig. 5.3);
- [Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md) at $\varepsilon=1$, 50 points,
  without observable oscillations (Fig. 5.2);
- [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md), configurations 3
  (modified) and 5, $400^2$, $\varepsilon=1$: characteristic-wise WENO on $f_E$ is needed;
  component-wise WENO everywhere, or no splitting ($\alpha_{\mathrm s}=0$), oscillates in the
  middle region (Ex. 5.4, Figs. 5.4–5.5);
- [Gresho vortex](/benchmarks/gresho-vortex.md) at $\varepsilon=10^{-1},10^{-2},10^{-6}$ on
  $100^2$ and $200^2$: shape and kinetic energy well kept over two periods, S4T3 better than
  S2T2 on the coarse grid (Ex. 5.5, Fig. 5.6);
- double shear layer and [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) at
  $\varepsilon=10^{-6}$: the $L^\infty$ divergence error grows in time and jumps when fine
  structures are no longer resolved (Ex. 5.6, Fig. 5.7).

## Linear IMEX finite volumes: what a splitting must satisfy

[Allegrini & Vignal (2025)](/sources/allegrini-2025.md) (HAL author manuscript) build a
first- and second-order IMEX finite-volume scheme for the full Euler equations in a different
scaling: the pressure gradient carries $1/\varepsilon_{\mathrm A}$ and
$E=\frac{p}{\gamma-1}+\frac{\varepsilon_{\mathrm A}}2\rho\lvert v\rvert^2$, with
$M^2=\varepsilon_{\mathrm A}/\gamma$ (page-local $\varepsilon_{\mathrm A}$, so
$\varepsilon_{\mathrm A}=\gamma\varepsilon^2$ in the notation above) and the unscaled
$c^2=\gamma p/\rho$, the physical sound speed being $c/\sqrt{\varepsilon_{\mathrm A}}$ (§1, Eq. (1)).
They name three properties a splitting $f=f_{\mathrm e}+f_{\mathrm i}$ (page-local, explicit and
implicit parts) should have (§2): (i) real eigenvalues of both Jacobians, those of the explicit
one bounded in $\varepsilon_{\mathrm A}$; (ii) asymptotic consistency; (iii) preservation of
constant contact discontinuities ([stationary contact preservation](/properties/stationary-contact-preservation.md)).
The energy equation must carry the enthalpy flux implicitly, or the pressure-wave operator
forces $\Delta t=O(\sqrt{\varepsilon_{\mathrm A}}\,\Delta x)$ (§2.1). They compare (Lemmas 1–3):

- the **Toro–Vázquez splitting** ([flux vector splitting](/methods/flux-vector-splitting.md)),
  $f_{\mathrm e}=(\rho v,\ \rho v\otimes v,\ \kappa_{\mathrm A}v)$,
  $f_{\mathrm i}=(0,\ p\,\mathbb I/\varepsilon_{\mathrm A},\ h_{\mathrm v}v)$ with the rescaled
  kinetic energy $\kappa_{\mathrm A}=\varepsilon_{\mathrm A}\rho\lvert v\rvert^2/2$ and the enthalpy per
  unit volume $h_{\mathrm v}=\gamma p/(\gamma-1)$ (page-local), satisfies all three, with explicit
  eigenvalues $0,v,v$ and implicit ones $0$, $v/2\pm\sqrt{v^2/4+c^2/\varepsilon_{\mathrm A}}$ in 1D, and
  is consistent for non-well-prepared data (Lemma 1, (ii) by citation of Boscheri et al.); moving a
  fraction $\beta_{\mathrm A}\in[0,1)$ (page-local) of $h_{\mathrm v}v$ to the explicit part gives
  $\nabla\cdot v^{n+1}=\frac{\beta_{\mathrm A}}{\beta_{\mathrm A}-1}\nabla\cdot v^n$ in the limit, so
  $\beta_{\mathrm A}=0$ is "the only choice" consistent for non-well-prepared data (Remark 2.2);
- the **Cordier–Degond–Kumbaro** splitting is multi-step through $p^n$, so (i) is meaningless and
  (ii)–(iii) hold up to $O(\Delta t)$ (§2.2), in agreement with Boscarino et al.'s finding above
  that $\rho^n$ in the energy flux leaves an $O(\Delta t)$ divergence;
- the non-conservative splitting of Dimarco, Loubère and Vignal satisfies (i) but is consistent
  only up to $O(\Delta t)$ and does not preserve contacts; its one-step conservative variant has
  complex explicit eigenvalues for $\gamma<3$ (Lemma 2);
- a **Lagrange-projection-type** splitting, $f_{\mathrm e}=(\rho v,\rho v\otimes v,Ev)$,
  $f_{\mathrm i}=(0,p\,\mathbb I/\varepsilon_{\mathrm A},pv)$, separates transport from pressure waves
  and satisfies (i) and (iii), and (ii) iff the initial velocity is well prepared (Lemma 3).

**Linearization without Picard iteration** (§3.1, Eq. (13)). Boscheri et al.'s reformulated
semi-discretization is non-linear in the enthalpy and needs a Picard iteration; Allegrini &
Vignal evaluate the enthalpy and the kinetic energy of the elliptic pressure equation on the
explicitly convected state $u^{n+1,\mathrm{ex}}$, so that $\rho^{n+1}$, $p^{n+1}$, $\rho v^{n+1}$ and
$E^{n+1}$ follow in sequence from one linear elliptic solve on a three-point stencil. The energy
must be updated from the energy equation, not from the equation of state, or the Sod
intermediate states are wrong (Fig. 1). The price (Lemma 4) is consistency only for
well-prepared initial **energy**, $E(x,0)=E^0+\varepsilon_{\mathrm A}\bar E(x)$; putting
$h^{n+1,\mathrm{ex}}$ in the energy update would restore consistency for arbitrary data but is
rejected as less diffusive and oscillatory in some tests (Remark 3.2).

**Fluxes and stability** (§3.2–3.4). The explicit part takes a [Rusanov flux](/methods/lax-friedrichs-flux.md)
with coefficient $\tfrac12\max(\lvert v_i\rvert,\lvert v_{i+1}\rvert)$, the implicit part centred
fluxes ("L2 AP" scheme); the "L∞ AP" scheme adds a second implicit solve, an upwinding of the
whole state with coefficient $\tfrac12\max\lvert\lambda_{\mathrm i}\rvert$,
$\lvert\lambda_{\mathrm i}\rvert=\lvert v\rvert/2+\sqrt{v^2/4+c^2/\varepsilon_{\mathrm A}}$, which degrades
consistency to $O(\Delta t)$ (Remark 5.2). A 1D linearized Fourier analysis, finished by
plotting root moduli over $M_\varepsilon\in(0,25]$ and $\gamma\in[1,10]$ or $[1,5]$, gives $L^2$
stability under $\gamma\lvert v\rvert\Delta t=\Delta x$ (L2 AP) and $\lvert v\rvert\Delta t=\Delta x$
(L∞ AP and the non-linear L2 AP variant) (Lemmas 5–7). The time step is thus set by the
flow speed alone. Second order uses [ARS(2,2,2)](/methods/imex-runge-kutta.md) with
minmod MUSCL on the explicit flux only, and a convex blend with the first-order scheme gives a
first-order TVD variant ([total variation diminishing](/definitions/total-variation-diminishing.md)).

**Evidence** (§3.4, §4). On Sod and Lax (200 and 500 cells) the linear schemes match the
non-linear ones up to extra smearing at the Lax contact that vanishes on refinement; a contact
with a density ratio of $10^5$ keeps velocity and pressure constant "up to an error of
$10^{-5}$"; on interacting Riemann problems at $\varepsilon_{\mathrm A}=1,10^{-1},10^{-2}$ all
first-order AP schemes oscillate on coarse meshes unless the CFL number is reduced, the L2
versions more, so the L∞ scheme is kept as the first-order one; on the
[Gresho vortex](/benchmarks/gresho-vortex.md) ($M_p=10^{-1}$ to $10^{-3}$, $80^2$) the second-order
scheme keeps a Mach-independent local Mach field without pressure oscillations, its
kinetic-energy loss coming "mostly" from the limiter (0.9825 unlimited against 0.92 with minmod
on $40^2$); a double shear layer at $\varepsilon_{\mathrm A}$ down to $10^{-6}$ matches the
incompressible solution.

## A weakly compressible finite-element relative

[Zampa & Dumbser (2025)](/sources/zampa-2025.md) (§3.1, Eqs. (4)–(6); arXiv v1) apply the same
explicit-convection, implicit-pressure split to weakly compressible **isentropic** flow with
compatible finite elements (momentum in Raviart–Thomas, density and pressure discontinuous),
with Newton iterations on the equation of state and a non-conservative entropy equation; the
time step $\Delta t=C_{\mathrm{CFL}}h/((2r+1)\max(\lVert v\rVert_\infty,1))$ ($r$ the polynomial
degree, $C_{\mathrm{CFL}}=0.25$) does not contain the sound speed (§4). Theorem 3.2 proves that
with constant density and $1/c^2=0$ the Newton iteration converges in one step to an H(div)
incompressible Navier–Stokes scheme ([asymptotic preservation](/properties/asymptotic-preservation.md)).
The scheme is first order in time, IMEX Runge–Kutta being named as the route to higher order,
and the authors restrict it to Mach numbers from zero to about one because the entropy
equation replaces the energy equation (§3.2.2, §5).

## Explicit low-Mach flux corrections, for contrast

Allegrini & Vignal (§1) recall that explicit schemes, besides $\Delta t=O(\sqrt{\varepsilon_{\mathrm A}})$,
are not asymptotically consistent without flux corrections. [MFC](/software/mfc.md) 5.0
([Wilfong et al. (2026)](/sources/wilfong-2026.md), §4.2.4, Fig. 14) keeps an explicit solver and
implements two such corrections of HLLC, the Thornber et al. velocity reconstruction and the
anti-dissipation pressure correction of Chen et al.; on the Gresho vortex at reference Mach
numbers $10^{-1}$ to $10^{-4}$ standard HLLC loses accuracy, both corrections preserve the flow "to
visual accuracy" ([HLL-family solvers](/methods/hll-riemann-solvers.md)). The time step remains
acoustic.

## Extension to ideal MHD

[Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) carry the scheme over to the ideal MHD
equations at all sonic Mach numbers $\varepsilon\in[0,O(1)]$, with the Alfvén Mach number set
to one (§2.2): the momentum flux carries $(p/\varepsilon^2+\tfrac12\lvert B\rvert^2)\mathbb I-B\otimes B$
and the energy is $E=\frac{p}{\gamma-1}+\frac{\varepsilon^2}2\big(\rho\lvert v\rvert^2+\lvert B\rvert^2\big)$.
They combine it with constrained transport through a vector potential (Weyl gauge, after
Christlieb, Rossmanith and Tang): the induction equation is replaced by
$\partial_t\mathcal A+(\nabla\times\mathcal A)\times v=0$ for the potential $\mathcal A$ (registry §10),
and $B=\nabla\times\mathcal A$, so $\nabla\cdot B=0$ holds identically (§2.4,
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).

**Splitting** (§3.2). The right-hand side is partitioned into four parts: an explicit
convective–magnetic flux (mass and momentum, with the pressure $p$ itself, not
$p/\varepsilon^2$), the explicit constrained-transport term, an explicit energy flux carrying the
$\varepsilon^2$ magnetic contributions, and the implicit acoustic flux, which carries
$(1-\varepsilon^2)p_2$ in the momentum and the linearized enthalpy flux
$\frac{E_E+p_E}{\rho_I}(\rho v)_I$ in the energy, with $p_2=(p_I-\bar p_E)/\varepsilon^2$ as above.
With the kinetic and magnetic energy evaluated explicitly, each implicit stage again reduces
to one linear elliptic equation,
$$\frac{\varepsilon^2}{\gamma-1}p_2-(1-\varepsilon^2)\Delta t^2\mathsf a_{ii}^2\,\nabla\cdot\big(\bar H\nabla p_2\big)=E^{\circ\circ}$$
(Eq. (3.18); $E^{\circ\circ}$ explicit). The switch $\alpha_{\mathrm s}=1$ for $\varepsilon<1$,
$1/\varepsilon^2$ for $\varepsilon\ge1$ is that of Boscarino et al. (§3.1). The time stepper is the
third-order stiffly accurate SI-IMEX Runge–Kutta of Boscarino et al. and Huang, Xing and
Xiong (tableau not reprinted).

**Space** (§3.3). Fifth-order finite-difference WENO, characteristic-wise on the explicit
convective–magnetic flux and component-wise on the other two fluxes; the
vector-potential equation is a Hamilton–Jacobi equation discretized with Jiang–Peng WENO and
a Lax–Friedrichs Hamiltonian; $B=\nabla\times\mathcal A$ and the elliptic operator use
fourth-order central differences. The [characteristic decomposition](/methods/characteristic-decomposition.md)
uses the MHD eigenvectors **at $\varepsilon=1$**, because for small $\varepsilon$ the true ones "will make
such a spectral characteristic decomposition to be unstable" (stated, no analysis).

**Capped viscosity.** The global [Lax–Friedrichs](/methods/lax-friedrichs-flux.md) speed and
the time step use the fast magnetosonic speed built from the capped sound speed
$\hat c=\min(1/\varepsilon,1)\sqrt{\gamma p/\rho}$ (Eq. (3.12)), so both are independent of
$\varepsilon$ for $\varepsilon<1$. The explicit reference schemes of the paper (WENO with SSP-RK3,
with and without constrained transport) use the same cap, which the authors say "leads to
much better results" (§5).

**Evidence** (§5, CFL 0.25). Fifth order on the 1D and 2D circularly polarized
[Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md) at $\varepsilon=1$, with $B$ only
fourth order in 2D because of the central-difference curl (Tables 5.1, 5.3); order loss at
$\varepsilon=10^{-2}$ ([asymptotic preservation](/properties/asymptotic-preservation.md)); the
[Brio–Wu-type shock tube](/benchmarks/brio-wu-shock-tube.md), the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) and the
[MHD blast wave](/benchmarks/mhd-blast-wave.md) (maximum discrete divergence
$2.87\times10^{-11}$ at $\varepsilon=0.9$); field-loop advection on $256\times128$ with CPU times
(s) for the semi-implicit and the explicit constrained-transport scheme of 7634.880 vs
4736.466 at $\varepsilon=0.5$, 5687.467 vs 19719.964 at $\varepsilon=0.1$ and 8015.959 vs 38666.192
at $\varepsilon=0.05$ (Table 5.5; hardware and linear solver not stated). The explicit scheme is
cheaper at $\varepsilon=0.5$; the semi-implicit one is about 3.5 and 4.8 times faster at the two
smaller Mach numbers *(compiler check, not in the sources: ratios of the printed times)*, and its own cost is not monotone in $\varepsilon$, which the paper does
not explain.

## Cell-centred MHD with implicit magnetic terms

[Dematté et al. (2024)](/sources/dematte-2024.md) build a different, pressure-based
semi-implicit finite-volume scheme for ideal and visco-resistive MHD in which **all**
magnetic-field terms of the pressure part are implicit, so that the time step is set by the
fluid velocity alone, also in magnetically dominated flows (target: disruption events in
magnetic-confinement fusion). They contrast it with the scheme of Dumbser et al. (2019), which
keeps the magnetic terms explicit and is therefore limited by the Alfvén speed (§1). *(compiler
check, not in the sources: the same holds for the Chen–Wu–Xiong scheme above, whose capped
fast magnetosonic speed still contains the Alfvén speed.)*

**Flux-vector splitting** (§2.1, Eq. (15), the MHD splitting of Balsara, Montecinos and Toro
closest to Toro–Vázquez). With $u=(\rho,\rho v,E,B)$ and, in the $x$ direction, the specific
enthalpy $h=e+p/\rho$ (page-local), $f=f^{\mathrm a}+f^{\mathrm p}$ with

$$f^{\mathrm a}=v_1\big(\rho,\ \rho v_1,\ \rho v_2,\ \rho v_3,\ \kappa,\ 0,\ B_2,\ B_3\big),\qquad
f^{\mathrm p}=\big(0,\ p+\tfrac12\lvert B\rvert^2-B_1^2,\ -B_1B_2,\ -B_1B_3,\ v_1(\rho h+\lvert B\rvert^2)-B_1(v\cdot B),\ 0,\ -v_2B_1,\ -v_3B_1\big)$$

(page-local $f^{\mathrm a}$, $f^{\mathrm p}$; $\kappa$ the kinetic energy, registry §6). The advective
sub-system has eigenvalues $0$ and $v_1$ only; the "pressure" sub-system, which carries the gas
pressure, the magnetic pressure and the non-advective induction terms, has the eigenvalues
$0,0,\mp\lvert B_1\rvert/\sqrt\rho$ and $\tfrac12\big[v_1\mp\sqrt{v_1^2+4\big(c^2+(\gamma-1)(B_2^2+B_3^2)/\rho\big)}\big]$
(Eqs. (17), (19)), so it is always subsonic. The authors note that these fast analogues need not
bracket the true fast magnetosonic speeds, as for Toro–Vázquez in gas dynamics (§2.1).
*(compiler check, not in the sources: $f^{\mathrm a}+f^{\mathrm p}$ is the ideal-MHD flux with total
energy $E=\rho e+\kappa+\tfrac12\lvert B\rvert^2$.)*

**Explicit advective step** (§3.1, Eqs. (21)–(24)). First-order or second-order
[MUSCL–Hancock](/methods/muscl-hancock.md) (van Leer limiter) interface states and a
[Rusanov flux](/methods/lax-friedrichs-flux.md) with $a=\max(\lvert v_1^-\rvert,\lvert v_1^+\rvert)$, so
the dissipation scales with the flow speed only; the step is
$\Delta t=\nu/(\max\lvert\lambda_x\rvert/\Delta x+\max\lvert\lambda_y\rvert/\Delta y)$ with the advective
eigenvalues, $\nu=0.8$ unless stated, and a magnetosonic step for the first step when the initial
velocity is zero or small. The density is final after this step.

**Implicit pressure sub-system by nested Picard iterations** (§3.2, Fig. 1; after Fambri and
Boscheri–Tavelli for the magnetic and viscous parts, Dumbser–Casulli for the pressure). A main
loop ($N_{\mathrm r}$ iterations, page-local) contains a magnetic loop ($N_{\mathrm q}$) that solves a linear system for a
non-solenoidal predictor of $B$ with a provisional momentum and the pressure frozen, quadratic
terms linearized between Picard iterates, and a pressure loop ($N_{\mathrm s}$) that solves a linear system
for $p$ with $B$ frozen, from the energy equation with mean-centred implicit fluxes and a
momentum-weighted face enthalpy (Eqs. (26)–(37)). With the ideal-gas law each pressure iteration
is linear. All systems are solved by matrix-free GMRES (tolerance $10^{-15}$) without
preconditioner, the Picard tolerance is $10^{-12}$ (Eq. (38)), and $N_{\mathrm r}=N_{\mathrm q}=N_{\mathrm s}=2$ in all tests. The
predicted field is corrected inside every magnetic iteration either by a staggered adaptation of
Gardiner–Stone constrained transport, whose corner electric field includes the implicit pressure
flux, or by an unstaggered adaptation of Rossmanith's vector-potential method; both keep
$\nabla\cdot B$ at machine precision (§3.3, Fig. 8;
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md),
[constrained transport](/methods/constrained-transport.md)). Viscous, resistive and heat-flux
terms enter the same implicit loops (§3.4), so the step stays velocity-based in
visco-resistive-dominated flows.

**Evidence** ($\gamma=5/3$; §4):

- four 1D MHD Riemann problems on 1000 cells, including the
  [Brio–Wu tube](/benchmarks/brio-wu-shock-tube.md): with the purely advective step RP3 and RP4 are
  less accurate than with an Alfvénic step, so the step size is also an accuracy choice (§4.1.1);
- second order in space on a smooth [MHD vortex](/benchmarks/magnetized-vortex.md) with fixed
  $\Delta t=0.01$: $L_2(\rho)$ orders 1.573 to 1.998 from $16^2$ to $512^2$ (Table 2), and a
  stationary vortex kept to $t=1000$ on $200^2$ cells;
- rotor, [Orszag–Tang](/benchmarks/orszag-tang-vortex.md) and [blast wave](/benchmarks/mhd-blast-wave.md);
- low-Mach [field loop](/benchmarks/field-loop-advection.md) ($M\approx0.006$): 960 time steps and
  2930 s against 240427 steps and 85340 s for an explicit second-order MUSCL–HLLEM–CT scheme
  (§4.2.1); advected θ-pinch: 1150 against 117546 steps, 104 s against 4240 s, with the
  semi-implicit error and wall time essentially independent of the axial field from 1 to 32
  (§4.2.3); hardware not stated;
- shear layer and current sheet in 23 steps, visco-resistive
  [Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) with helicity errors comparable
  to an explicit divergence-free Godunov scheme, and an MHD
  [lid-driven cavity](/benchmarks/lid-driven-cavity.md) against Fambri et al., plus a new
  accelerating-lid cavity from very low Mach to $M\simeq2$ and back (§4.3–4.4);
- GMRES needs fewer than ten iterations per step on Orszag–Tang and Kelvin–Helmholtz and about
  one hundred for the pressure system of the field loop (§4.5).

## Qualifications

- **Different meanings of "all Mach".** Boscarino et al. prove asymptotic preservation and asymptotic
  accuracy (formal, time-semi-discrete); Dematté et al. mean a velocity-based time step and
  flow-speed-scaled dissipation, give no asymptotic analysis, state that there is "no rigorous
  proof" of stability under the advective CFL condition (§2.1), and leave higher order in time
  to future IMEX Runge–Kutta work (§4.1.2, §5).
- Dematté et al. print the explicit advective update (Eq. (21)) and the semi-discrete energy
  equation (Eq. (34)) with the sign of the flux divergence reversed, against their Eqs. (16),
  (26) and (35); the face-field updates of the staggered constrained transport (Eq. (39)) with
  both signs reversed with respect to Faraday's law with their electric field $\mathcal E_z=v_2B_1-v_1B_2$ ($\mathcal E$ registry §10, as on [constrained transport](/methods/constrained-transport.md)); and the
  vector-potential field (Eqs. (49), (51)) with $B_2=+\partial_x\mathcal A$ where $B=\nabla\times(\mathcal A\hat z)$
  gives $-\partial_x\mathcal A$, so that the printed field would not satisfy their own discrete divergence
  condition (50). *(compiler check, not in the sources: each of these follows from the paper's
  own definitions; divergence preservation (40) holds for either sign of (39).)*
- **Stability lemmas finished numerically.** Allegrini & Vignal's Lemmas 5–7 reduce the
  amplification factor to a quadratic whose roots are plotted over the parameter ranges, the
  maximum modulus being 1; the closing step invokes a matrix norm with
  $\lVert B\rVert\le r(B)$ for the amplification matrix $B$ and its spectral radius $r(B)$
  (page-local). *(compiler check, not in the sources: such a norm does not exist for every
  matrix: for the Jordan block $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $r(B)=1$ while
  $\lVert B^n\rVert$ grows like $n$, so no induced norm has $\lVert B\rVert\le1$; it exists when the
  eigenvalues of modulus $r(B)$ are semisimple, which the paper does not check.)* The lemmas are
  therefore numerical evidence of stability over the plotted ranges, not complete proofs.
- **Further meanings of "all Mach".** Zampa & Dumbser prove asymptotic preservation for constant
  density only and restrict their scheme to Mach numbers up to about one; Allegrini & Vignal
  run shocked problems at $\varepsilon_{\mathrm A}=1$ and prove consistency for well-prepared
  energy (linear scheme) or arbitrary data (semi-discrete Toro–Vázquez splitting).
- Allegrini & Vignal's printed slips (HAL v1): the 2D explicit flux of Remark 4 has mass flux
  $u$ in place of $\rho u$; Eqs. (15e), (19d)–(19e) carry stray tildes on $p^{n+1}$; the
  centred part of the MUSCL flux, Eq. (26), is divided by $2\Delta x$ against 2 in Eq. (15f);
  Eq. (28) calls the L∞ AP scheme "(13)", which is the L2 semi-discretization; and the time-step
  ratio of the L∞ AP scheme to the explicit one is said to exceed "the expected gain
  $\sqrt\varepsilon$", although $\sqrt\varepsilon<1$ for the tested $\varepsilon<1$, so a ratio
  above it need not be a gain.
- The scheme is not uniformly accurate in $\varepsilon$: asymptotic accuracy covers only
  $\varepsilon\to0$, and order is lost at intermediate Mach numbers (Table 5.2, Fig. 5.3),
  which the paper observes without explanation.
- For incompressible or weakly compressible flow without initial discontinuities the authors
  state that high-order **linear** reconstruction would preserve the divergence and resolve
  structures better than WENO (Ex. 5.6); only the divergence comparison with a fourth-order
  central difference is shown.
- A semi-implicit kinetic-energy splitting of Boscheri and Pareschi "may produce slightly
  better error in some test cases"; results not reported (Remark 3.2).
- The SI-IMEX(4,4,3) explicit tableau fails one third-order coupling condition as printed
  ([IMEX Runge–Kutta](/methods/imex-runge-kutta.md), compiler check); the paper's tests do
  not isolate temporal order.
- Printed slips. The elliptic operator in Eqs. (3.37)–(3.38) is printed without its
  divergence dot, against Eqs. (3.18) and (3.35). In Table 5.2 the $\varepsilon=1$, $N=32$
  error is printed $4.64\times10^{-3}$ next to $2.82\times10^{-5}$ at $N=64$ and the order
  4.05; the middle branch of the Gresho pressure (Eq. (5.9)) is printed
  $2(r/R)^2-4(2r/R+\log(r/R))+6$. *(compiler check, not in the sources:
  $\log_2(4.64\times10^{-3}/2.82\times10^{-5})=7.36$, while $4.64\times10^{-4}$ would give 4.04;
  the radial balance $p_2'(r)=v_\theta^2/r$ with $\rho=1$, $v_\theta=2(1-r/R)$ and $p_2(R)=0$
  gives $2(r/R)^2-4(2r/R-\log(r/R))+6$, which is continuous at $r=R/2$ with the printed inner
  branch $2(r/R)^2+2-\log16$, whereas the printed middle branch is not.)*

# Citations

- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — §2.2–2.4, §3.1–3.4 (Eqs. (3.1)–(3.18)), §4, §5 (Tables 5.1–5.5) (arXiv v1).
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §§1–2 (Eqs. (2.1)–(2.9)), §3.1 (Eqs. (3.10)–(3.19), Remark 3.1), §3.2 (Eqs. (3.25)–(3.40), Remark 3.2), §3.3 (Eq. (3.32)), §4 (Thm. 4.1, Remark 4.2, Def. 4.3, Prop. 4.4), §5 (Tables 5.1–5.2, Figs. 5.1–5.7) (arXiv v2).
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §1, §2.1 (Eqs. (14)–(19)), §3.1 (Eqs. (21)–(24)), §3.2 (Eqs. (25)–(38), Fig. 1), §3.3 (Eqs. (39)–(51)), §3.4, §4 (Tables 1–2, Figs. 2–22).
- [Allegrini & Vignal (2025)](/sources/allegrini-2025.md) — §1 (Eqs. (1)–(5)), §2 (Eqs. (6)–(12), Lemmas 1–3, Remarks 2.1–2.2), §3 (Eqs. (13)–(23), Lemmas 4–7, Remarks 3.1–5.2), §3.4, §4 (Eqs. (24)–(28), Lemma 8, Figs. 1–16) (HAL author manuscript).
- [Zampa & Dumbser (2025)](/sources/zampa-2025.md) — §3.1 (Eqs. (4)–(6)), §3.2.2, Thm. 3.2, §4, §5 (arXiv v1).
- [Wilfong et al. (2026)](/sources/wilfong-2026.md) — §4.2.4, Fig. 14: explicit low-Mach HLLC corrections in MFC 5.0.
