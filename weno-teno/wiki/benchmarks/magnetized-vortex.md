---
type: Benchmark
title: "Magnetized (MHD) vortex"
description: "Smooth exact equilibrium vortices of ideal and relativistic MHD, in which centrifugal force, magnetic tension and pressure balance radially, advected or held static as convergence-order tests: Balsara's iso-density vortex, a relativistic iso-enthalpy vortex, a 3D low-Mach vortex run up to tenth order, near-vacuum vortices for positivity, and a resistive charged vortex."
status: established
aliases: [MHD vortex, magnetized vortex, iso-density vortex, iso-enthalpy vortex, near-vacuum magnetized vortex, Balsara vortex]
tags: [benchmark, mhd, relativistic, positivity]
timestamp: 2026-10-24T06:00:00Z
---

# Magnetized (MHD) vortex

The MHD counterpart of the [isentropic vortex](/benchmarks/isentropic-vortex.md)
is a cylindrical equilibrium in which the azimuthal velocity $v_\phi$ and
the azimuthal field $B_\phi$ (page-local cylindrical components, radius
$R$) both decay like a Gaussian and the pressure balances them,

$$
\frac{d}{dR}\Big(p+\frac{B_3^2}{2}\Big)=\frac{\rho v_\phi^2}{R}-\frac{1}{2R^2}\frac{d}{dR}\big(R^2B_\phi^2\big),
$$

in units without $4\pi$ ([Berta et al. (2024)](/sources/berta-2024.md)
Eq. (43)). Superposed on a uniform translation on a periodic box, the
solution returns to its initial state after one period, so the error
against the initial data measures the order of the scheme on smooth MHD
flow, including the magnetic field. The sources use two families: a
vortex of constant density with order-one pressure, and a near-vacuum
vortex whose pressure almost vanishes at the centre, which adds a
positivity test.

## Setups

**Iso-density vortex (Balsara; Mignone; Dumbser, as cited).** Berta et
al. §5.2, Eqs. (44)–(45): on $[-5,5]^2$, periodic, $\rho=1$,

$$
\begin{aligned}
v&=v_0+(-y,\,x)\,k_{\mathrm v}\,e^{q_{\mathrm v}(1-R^2)},\qquad
B=(-y,\,x)\,\mu\,e^{q_{\mathrm v}(1-R^2)}+B_3\,e_z,\\
p+\frac{B_3^2}{2}&=1+\frac{1}{4q_{\mathrm v}}\Big[\mu^2(1-2q_{\mathrm v}R^2)-fk_{\mathrm v}^2\Big]e^{2q_{\mathrm v}(1-R^2)},
\end{aligned}
$$

with $R=\sqrt{x^2+y^2}$, $k_{\mathrm v}=\mu=1/(2\pi)$ (printed "$1/2\pi$"), $q_{\mathrm v}=1$,
$f=\rho=1$, the right-hand side split equally into thermal and
magnetic parts ($p$ and $B_3^2/2$ each half of it), $v_0=(1,1)$, one
period $t=10$; error $\varepsilon_1(B_1)$ in $L^1$ ($k_{\mathrm v}$, $\mu$, $q_{\mathrm v}$, $f$,
$v_0$ page-local; the sources' $k$, $q$). Differentiating the printed pressure reproduces the
balance above term by term, so the data are an exact equilibrium
*(compiler check, not in the sources)*.

**Dumbser et al.'s vortex, unshifted ([Dematté et al. 2024](/sources/dematte-2024.md)).**
Dematté et al. §4.1.2 take "the same" setup as Dumbser et al. (2019) on the
periodic box $[0,10]^2$, $\rho=1$, with the profiles of Berta et al.
at $q_{\mathrm v}=\tfrac12$, centred at $(5,5)$ and without mean flow:
$v=k_{\mathrm v}\,e^{\frac12(1-R^2)}(5-y,\,x-5)$, $B=\mu\,e^{\frac12(1-R^2)}(5-y,\,x-5)$,
$k_{\mathrm v}=\mu=1/(2\pi)$ (their $\varepsilon/(2\pi)$ with $\varepsilon=1$); the
exact solution is the initial state. In these symbols the pressure is
printed as $p=1+\tfrac12\mu^2(1-R^2)e^{(1-R^2)}-\tfrac12\tilde k_{\mathrm v}^2e^{\frac12(1-R^2)}$,
with a symbol $\tilde k_{\mathrm v}$ (their $\tilde\varepsilon/(2\pi)$) that is not
defined. *(Compiler check, not in the sources.)* With $k_{\mathrm v}=\mu$ and $\rho=1$
the velocity equals the field, so the state is stationary iff
$p+\tfrac12\lvert B\rvert^2$ is constant; this holds when the last term is
$-\tfrac12k_{\mathrm v}^2e^{(1-R^2)}$ and fails with the printed exponent
$e^{\frac12(1-R^2)}$; the magnetic term is correct as printed. The run
ends at $t=1$ with a fixed $\Delta t=0.01$, error in $L_2$ against the
initial state (Eq. (65)). In §4.1.3 the same vortex, centred at the
origin on the periodic $[-10,10]^2$ with $200^2$ cells, is run to
$t=1000$ with a velocity-based CFL number of $0.45$ to test the
preservation of a steady state over long times.

**Three-dimensional vortex at low Mach number ([Teissier et al. 2024](/sources/teissier-2024.md)).**
Teissier et al. §4.1, Eq. (66) (arXiv v2) use the Balsara profiles in a
triply periodic $[-5,5]^3$, with the Gaussian of the full 3D radius
$r=\sqrt{x^2+y^2+z^2}$: $\rho=1$, $v=(1,1,2)+(-y,x,0)\,k_{\mathrm v}\,e^{q_{\mathrm v}(1-r^2)}$,
$B=(-y,x,0)\,\mu\,e^{q_{\mathrm v}(1-r^2)}$,
$p=p_0+\frac1{4q_{\mathrm v}}\big[\mu^2\big(1-2q_{\mathrm v}(r^2-z^2)\big)-k_{\mathrm v}^2\rho\big]e^{2q_{\mathrm v}(1-r^2)}$,
with $k_{\mathrm v}=\mu=1/(2\pi)$, $q_{\mathrm v}=1.75$ and $p_0=360$, chosen higher than in the
earlier versions so that the advection speed is about a tenth of the
sound speed; $\gamma$ is not stated. One period ends at $t=10$, and the
error $\delta_2$ is the root mean square over all cells of the
differences of all eight conserved variables against $t=0$ (Eq. (67)).
They also record the fraction $E_{\mathrm{loss}}$ of the fluctuating
kinetic plus magnetic energy lost in one period (Eq. (69)). *Compiler
check, not in the sources:* with $k_{\mathrm v}=\mu$ and $\rho=1$,
$p+\tfrac12\lvert B\rvert^2=p_0$ everywhere, so the 3D data are an
exact equilibrium despite the $z$-dependence of the Gaussian.

**Iso-enthalpy relativistic vortex (new in Berta et al.).** The same
profiles with $f=w_{\mathrm h}=5$, the constant relativistic enthalpy density $w_{\mathrm h}=\rho h$, $B_3=0$, zero radial electric field, a static vortex
($v_0=0$), $\gamma=5/3$ and $\rho=w_{\mathrm h}-5p/2$ from the equation of state,
which stays positive for this choice of $w_{\mathrm h}$; run to $t=10$
(see [relativistic hydrodynamics and MHD](/definitions/relativistic-hydrodynamics.md)).

**Near-vacuum vortex (Christlieb et al., as cited).**
[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.1, Eqs.
(38)–(41): on $[-10,10]^2$, periodic, $\gamma=5/3$, $\rho=1$,
$v=(1,1)+\delta v_{\mathrm v}(-y,x)$, $B=\delta B_{\mathrm v}(-y,x)$,
$p=1+\delta p$ with Gaussian amplitudes set by $\mu_{\mathrm v}=5.38948938512$
(page-local), chosen to bring the central pressure to about
$2\times10^{-8}$; $t=0.05$ with $\Delta t=10^{-4}$; $L^1$ error of
$(B_1,B_2)$ against the solution translated with velocity $(1,1)$,
9th-order Gauss–Legendre quadrature. The printed exponents are
inconsistent with the stated minimum pressure, as recorded on the
[isentropic vortex](/benchmarks/isentropic-vortex.md) page.

[Ding & Wu (2024a)](/sources/ding-2024.md) Ex. 4.1 (arXiv v1) print the
vortex "with low pressure" of Christlieb et al. and Wu & Shu, as they
cite it, explicitly: on $[-10,10]^2$, periodic, $\gamma=5/3$, $\rho=1$,
$v=(1,1,0)+\frac{\mu_{\mathrm v}}{\sqrt2\pi}e^{\frac12(1-r^2)}(-y,x,0)$,
$B=\frac{\mu_{\mathrm v}}{2\pi}e^{\frac12(1-r^2)}(-y,x,0)$,
$p=1-\frac{\mu_{\mathrm v}^2(1+r^2)}{8\pi^2}e^{1-r^2}$ with
$\mu_{\mathrm v}=5.389489439$, to $t=0.05$ on $N_x^2$ cells,
$N_x=20,\dots,1280$; they state a lowest pressure of about
$5.3\times10^{-12}$. The centre value $1-\mu_{\mathrm v}^2e/(8\pi^2)$ is
$5.34\times10^{-12}$ with their $\mu_{\mathrm v}$, and $2.0\times10^{-8}$ with
Dzanic & Witherden's $5.38948938512$: the two sources' last digits of
$\mu_{\mathrm v}$ set the near-vacuum depth *(compiler check, not in the
sources)*.

**Stationary charged vortex of resistive relativistic MHD.**
[Mignone et al. (2024)](/sources/mignone-2024.md) §4.2, Eq. (60): an
exact equilibrium of resistive relativistic MHD that does not depend on
the resistivity $\eta_{\mathrm m}$, with radial electric field
$\mathcal E_r=\frac{q_0}2\frac{r}{r^2+1}$ (page-local $\mathcal E$, the
electric field of the registry's MHD row; no vortex strength $\mathcal E$
on this page), axial field
$B_3=\sqrt{(r^2+1)^2-q_0^2/4}\,/(r^2+1)$, azimuthal velocity
$v_\phi=-\frac{q_0}2\,r/\sqrt{(r^2+1)^2-q_0^2/4}$, charge density
$\mathfrak q=q_0/(r^2+1)^2$ and the pressure of their Eq. (60), with
$q_0=0.7$, $p_0=0.1$, $\rho=1$ (page-local $q_0$, $\mathfrak q$, $p_0$),
on $[-10,10]^2$ with the boundaries held at the equilibrium, to $t=5$,
cuts on $256^2$. The charge is the divergence of the electric field:
$\frac1r\frac{d}{dr}(r\mathcal E_r)=q_0/(r^2+1)^2$ *(compiler check,
not in the sources)*.

**Balsara's vortex in a long run ([Liu et al. 2025c](/sources/liu-2025-c.md)).**
Liu et al. (2025c) Ex. 5.1 take Shu's hydrodynamic vortex extended to MHD
by Balsara, in the setup of Li & Shu, as they cite it, without reprinting
the data; $\gamma=5/3$, $N_x=N_y=32,64,128,256$, run to $T=20$, where the
exact solution is the initial state, $L^2$ errors.

The same page records two further magnetized vortices: the Wu–Shu-type
vortex of [Dao & Nazarov (2022)](/sources/dao-2022.md) and the
relativistic-MHD vortex of [Duan & Tang (2022)](/sources/duan-2022.md),
in two and three dimensions.

## Runs and findings

**Fourth-order finite volumes with constrained transport.** Berta et
al.'s scheme (pointwise [MP5](/methods/monotonicity-preserving-limiter.md)
or pointwise [WENO-Z](/methods/weno-z.md) reconstruction, upwind
constrained transport, SSPRK(5,4)) gives, for $N_x=32,64,128,256,512$
(Table 1):

| $\varepsilon_1(B_1)$ | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|
| MHD, MP5 | 9.99E-04 | 6.09E-05 (4.04) | 2.35E-06 (4.70) | 1.06E-07 (4.47) | 5.76E-09 (4.20) |
| MHD, WENO-Z | 9.01E-04 | 6.00E-05 (3.91) | 2.37E-06 (4.66) | 1.06E-07 (4.48) | 5.76E-09 (4.20) |
| RMHD, MP5 | 3.93E-04 | 1.70E-05 (4.53) | 6.09E-07 (4.80) | 2.34E-08 (4.71) | 1.05E-09 (4.47) |
| RMHD, WENO-Z | 3.11E-04 | 1.83E-05 (4.09) | 6.41E-07 (4.84) | 2.36E-08 (4.77) | 1.05E-09 (4.49) |

(observed orders in parentheses). The fourth-order profiles overlap the
exact solution almost perfectly at $N_x=128$, while the second-order
LINEAR scheme does not reach that accuracy even at 512 and clips the
relativistic profile markedly (Fig. 4). Against the fifth-order
finite-difference scheme of Mignone the errors are "very similar" for
$N_x\lesssim128$, the finite-difference scheme converging faster; they
note that it needs $\Delta t\sim\Delta x^{5/3}$ with its third-order
Runge–Kutta to keep fifth order.

**Semi-implicit all-Mach finite volumes.** Dematté et al.'s cell-centred
[semi-implicit scheme](/methods/semi-implicit-all-mach-scheme.md), with
unlimited MUSCL–Hancock reconstruction of the advective sub-system and
the fixed $\Delta t=0.01$, converges at second order in space (Table 2):

| $N_x=N_y$ | 16 | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|---|
| $L_2(\rho)$ | 2.436E-02 | 8.186E-03 (1.573) | 2.264E-03 (1.854) | 5.794E-04 (1.966) | 1.457E-04 (1.992) | 3.647E-05 (1.998) |
| $L_2(E)$ | 2.878E-02 | 7.505E-03 (1.939) | 1.863E-03 (2.010) | 4.647E-04 (2.003) | 1.161E-04 (2.001) | 2.903E-05 (2.000) |

with similar orders for $v_1$ and $B_1$, which the authors call second order
of accuracy in space; these are orders at a fixed small step, and higher
order in time is left to future IMEX work (§4.1.2). In the
long-time run both of their constrained-transport variants (staggered,
and unstaggered from a vector potential) keep the stationary vortex to
$t=1000$ (§4.1.3, Figs. 4–5).

**Orders up to ten with point-value fluxes.** Teissier et al.'s
finite-volume solvers S2–S10 (WENO face reconstruction of order 3 to 11,
conversion of face averages to point values and back, LLF fluxes,
constrained transport, SSP multistep–multistage time integration of
matching order) give (Table 2):

| scheme | $\delta_2$ at $64^3$ | $\delta_2$ at $192^3$ | EOC$_2$ at $192^3$ | $E_{\mathrm{loss}}$ at $192^3$ |
|---|---|---|---|---|
| S2 | 8.5E-03 | 5.7E-03 | 0.657 | 0.79 |
| S4 | 3.9E-03 | 7.5E-05 | 4.46 | 9.0E-03 |
| S6 | 8.7E-04 | 1.4E-06 | 6.12 | 7.7E-05 |
| S8 | 1.4E-04 | 2.1E-08 | 7.87 | 9.6E-07 |
| S10 | 2.9E-05 | 5.0E-10 | 9.74 | 1.1E-08 |
| S8 without point values (S8P) | 1.4E-04 | 2.9E-06 | 1.99 | 1.1E-06 |
| S8 with a second-order time integrator (S8T) | 1.4E-04 | 2.7E-07 | 2.12 | 9.0E-07 |

S4–S10 reach their design orders. Without the passage through point
values the order falls to two, confirming that identifying a face
average with the face-centre value costs $O(\Delta x^2)$ (Eq. (36));
S8P keeps an energy loss close to S8's, which the authors read as a sign
of dispersive rather than dissipative error. S2 loses $99\%$ of the
fluctuating energy at $64^3$ ($60\%$ at $256^3$), which they ascribe to
the LLF dissipation at low Mach number, proportional to the fast speed
times the interface jump; raising the order shrinks the jump and acts as
an alternative to low-Mach Riemann-solver fixes (§4.1; see
[numerical dissipation](/definitions/numerical-dissipation.md)). The
WENO weights use the exponent $q=1$ (not the vortex parameter $q_{\mathrm v}$) and
$\epsilon=10^{-12}$, because the "typical choice" $q=2$ with $\epsilon=10^{-6}$ "leads to a worse convergence for schemes
of order strictly greater than 4" (§4.1, no table). With the cost per
step relative to S2 (Table 3), the authors argue that S6 at $96^3$
matches the energy loss of S4 at $192^3$ at a fraction of the cost, "a
factor of order 10" (§4.1).

**Positivity-filtered DG near vacuum.** Dzanic & Witherden's nodal
DG / flux reconstruction with positivity-preserving
[entropy filtering](/methods/entropy-filtering.md) converges at
2.89, 3.80, 4.62 and 5.23 for $\mathbb P^2$–$\mathbb P^5$ on $20^2$ to
$67^2$ elements, between $N$ and $N+1$ (their "on the order of $p$ to $p+1$") ($\mathbb P^2$:
$2.29\times10^{-4}$ to $6.92\times10^{-6}$; $\mathbb P^5$:
$4.04\times10^{-7}$ to $6.51\times10^{-10}$; Table 1), with the filter
"essentially negligible for smooth solutions" (Table 2). Their
$\mathbb P^2$ errors are "marginally lower" than those of Wu & Shu's
positivity-preserving DG, which they compare against.

**Positivity with a discrete divergence-free projection.** Ding & Wu
(2024a)'s positivity-preserving finite volumes, which project the
interface point values of $B$ onto a discretely divergence-free set and
add a Godunov–Powell-type source, keep their design order with the
positivity limiter active: the second-order scheme reaches orders
2.42–2.59 on the finest grids and the fifth-order one ([WENO-Z](/methods/weno-z.md),
characteristic, four-point Gauss–Lobatto face quadrature) 4.80–5.05 at
$N_x=1280$, with $l^1$ errors $2.50\times10^{-11}$ ($v_2$),
$1.61\times10^{-11}$ ($B_1$) and $2.04\times10^{-11}$ ($p$) (Table 4.1);
the authors conclude that neither the projection nor the limiter
degrades the accuracy. See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
and [geometric quasilinearization](/methods/geometric-quasilinearization.md).

**Fourth order in resistive relativistic MHD.** On the charged vortex
Mignone et al. (2024)'s fourth-order finite-volume scheme, run in
[PLUTO](/software/pluto.md) with IMEX time stepping, reduces the charge
error "by two orders of magnitude" against the second-order scheme of
their Paper I; the
SSP(4,3,3) and ARK4 integrators "yield nearly identical results", but
ARK4 becomes unstable for $\eta_{\mathrm m}\lesssim10^{-4}$. The pressure converges
at fourth order with both integrators, against second order for Paper I
(§4.2, Fig. 3).

**Globally divergence-free entropy-stable nodal DG.** Liu et al.
(2025c)'s nodal DG on $k+2$ Gauss–Lobatto points, whose cells carry
$\mathbb Q^{k+1}$ fields and whose faces carry degree-$k$ normal fields
(their $k$; registry $N=k+1$), with a least-squares reconstruction of a
nodally divergence-free $B$, reaches on the finest pair the $L^2$ orders
2.48 ($\rho$), 2.29 ($\rho v_1$), 2.57 ($B_1$), 2.35 (total energy) for
$k=1$; 3.09, 3.03, 2.91, 3.05 for $k=2$; and 4.47, 4.21, 4.00, 4.33 for
$k=3$ (Table 1, no limiter, SSP-RK of ten stages and fourth order, CFL
0.45). The authors read this as the "designed accuracy"; it matches the
$(k+1)$-th-order truncation error they state for $k+2$ Gauss–Lobatto
points (§3.1), one order below the registry's design order $N+1=k+2$ for
DG of degree $N=k+1$. On $64^2$ and $128^2$ with $k=2$, both their scheme and the
entropy-stable nodal DG of Liu, Shu & Zhang (2018), as they cite it,
leave a total-energy conservation error "at the same level" (the
reconstruction step corrects the energy to keep the pressure), while
only the divergence-free variant keeps the conservation error of $B$ at
machine accuracy (Fig. 2). See
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
and [entropy stability](/properties/entropy-stability.md).

## Qualifications

- Berta et al.'s observed orders exceed four on every grid pair except
  the first WENO-Z one, up to 4.84, for a scheme they call fourth order
  whose interface interpolation they call fifth-order accurate; the
  paper does not comment on the rates above four.
- As printed, Berta et al.'s relativistic balance, Eq. (46), carries a
  factor $W$ (the Lorentz factor) in the centrifugal term, while the
  solution they give, Eqs. (44)–(45) with constant $f=w_{\mathrm h}$, balances the
  same term without it; at the largest vortex speed of these data,
  $v_\phi\approx0.186$ at $R=1/\sqrt2$, $W\approx1.018$, so the two
  differ by up to about 2 % of that term *(compiler check, not in the
  sources)*. The paper does not say which of the two equations is
  correct.
- Dematté et al.'s Table 2 orders are spatial, with $\Delta t$ fixed
  (§4.1.2).
- Teissier et al. are read as arXiv:2306.09856v2, titled "High-order
  finite-volume integration schemes for subsonic magnetohydrodynamics"
  with two of the three authors of the published article; their
  efficiency argument is restricted to smooth subsonic flows (§1, §5).
- Dzanic & Witherden's run is short ($t=0.05$, a translation of
  $0.05\sqrt2$), and their error is measured against the translated
  exact solution.
- Mignone et al. (2024) give the ARK4 stability threshold as
  $\eta_{\mathrm m}\lesssim10^{-4}$ here, report its failure at $\eta_{\mathrm m}=10^{-6}$ on
  their rotor and call SSP more robust for $\eta_{\mathrm m}\lesssim10^{-5}$ in their
  summary. Their Fig. 3 caption gives the charge cuts at $t=3$ and
  "pressure" maps where the panels read $t=2$ and $\rho$.
- Berta et al. are read as the arXiv v4 preprint, Dzanic & Witherden
  as arXiv v2, Ding & Wu (2024a) as arXiv v1; Mignone et al. (2024) as
  the version of record deposited on HAL.

# Citations

- [Berta et al. (2024)](/sources/berta-2024.md) — §5.2, Eqs. (43)–(46), Table 1, Fig. 4 (arXiv v4).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.1, Eqs. (38)–(41), Tables 1–2 (arXiv v2).
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §5.1.1 (arXiv v1).
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §4.1.2–4.1.3, Eq. (65), Table 2, Figs. 4–5.
- [Teissier et al. (2024)](/sources/teissier-2024.md) — §4.1, Eqs. (36), (66)–(69), Tables 2–3 (arXiv v2).
- [Duan & Tang (2022)](/sources/duan-2022.md) — Exs. 6.1, 6.7 (arXiv v1).
- [Ding & Wu (2024a)](/sources/ding-2024.md) — Ex. 4.1, Table 4.1 (arXiv v1).
- [Mignone et al. (2024)](/sources/mignone-2024.md) — §4.2, Eq. (60), Fig. 3.
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §3.1, Ex. 5.1, Table 1, Fig. 2.
