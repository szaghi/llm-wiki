---
type: Method
title: "Semi-implicit all-Mach schemes"
description: "Semi-implicit all-Mach schemes split the scaled Euler or ideal MHD equations into explicit material (and magnetic) waves and implicit acoustic waves, so the time step no longer shrinks with the Mach number; with a linearized equation of state each implicit stage is one linear elliptic equation for the pressure, and the scheme is asymptotic preserving in the incompressible limit."
status: established
aliases: [all-Mach scheme, all-speed semi-implicit scheme, low-Mach semi-implicit scheme, SI-IMEX WENO, S4T3, all sonic Mach MHD scheme, AP WENO-CT]
tags: [asymptotic-preserving, imex, semi-implicit, all-mach, finite-difference, weno, characteristic, low-dissipation, mhd]
timestamp: 2026-10-23T16:00:00Z
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

## Extension to ideal MHD

[Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) carry the scheme over to the ideal MHD
equations at all sonic Mach numbers $\varepsilon\in[0,O(1)]$, with the Alfvén Mach number set
to one (§2.2): the momentum flux carries $(p/\varepsilon^2+\tfrac12\lvert B\rvert^2)\mathbb I-B\otimes B$
and the energy is $E=\frac{p}{\gamma-1}+\frac{\varepsilon^2}2\big(\rho\lvert v\rvert^2+\lvert B\rvert^2\big)$.
They combine it with constrained transport through a vector potential (Weyl gauge, after
Christlieb, Rossmanith and Tang): the induction equation is replaced by
$\partial_t\mathcal A+(\nabla\times\mathcal A)\times v=0$ for the page-local potential $\mathcal A$,
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

## Qualifications

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
