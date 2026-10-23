---
type: Benchmark
title: "Magnetized (MHD) vortex"
description: "Smooth exact equilibrium vortices of ideal and relativistic MHD, in which centrifugal force, magnetic tension and pressure balance radially, advected or held static on a periodic box as convergence-order tests: Balsara's iso-density vortex, a relativistic iso-enthalpy vortex, and the near-vacuum vortex used to test positivity-preserving DG."
status: established
aliases: [MHD vortex, magnetized vortex, iso-density vortex, iso-enthalpy vortex, near-vacuum magnetized vortex, Balsara vortex]
tags: [benchmark, mhd, relativistic, positivity]
timestamp: 2026-10-23T23:45:00Z
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
v&=v_0+(-y,\,x)\,k\,e^{q(1-R^2)},\qquad
B=(-y,\,x)\,\mu\,e^{q(1-R^2)}+B_3\,e_z,\\
p+\frac{B_3^2}{2}&=1+\frac{1}{4q}\Big[\mu^2(1-2qR^2)-fk^2\Big]e^{2q(1-R^2)},
\end{aligned}
$$

with $R=\sqrt{x^2+y^2}$, $k=\mu=1/(2\pi)$ (printed "$1/2\pi$"), $q=1$,
$f=\rho=1$, the right-hand side split equally into thermal and
magnetic parts ($p$ and $B_3^2/2$ each half of it), $v_0=(1,1)$, one
period $t=10$; error $\varepsilon_1(B_1)$ in $L^1$ ($k$, $\mu$, $q$, $f$,
$v_0$ page-local). Differentiating the printed pressure reproduces the
balance above term by term, so the data are an exact equilibrium
*(compiler check, not in the sources)*.

**Iso-enthalpy relativistic vortex (new in Berta et al.).** The same
profiles with $f=w=5$, the constant enthalpy density $\rho h$
(page-local), $B_3=0$, zero radial electric field, a static vortex
($v_0=0$), $\gamma=5/3$ and $\rho=w-5p/2$ from the equation of state,
which stays positive for this choice of $w$; run to $t=10$
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

**Positivity-filtered DG near vacuum.** Dzanic & Witherden's nodal
DG / flux reconstruction with positivity-preserving
[entropy filtering](/methods/entropy-filtering.md) converges at
2.89, 3.80, 4.62 and 5.23 for $\mathbb P_2$–$\mathbb P_5$ on $20^2$ to
$67^2$ elements, "on the order of $p$ to $p+1$" ($\mathbb P_2$:
$2.29\times10^{-4}$ to $6.92\times10^{-6}$; $\mathbb P_5$:
$4.04\times10^{-7}$ to $6.51\times10^{-10}$; Table 1), with the filter
"essentially negligible for smooth solutions" (Table 2). Their
$\mathbb P_2$ errors are "marginally lower" than those of Wu & Shu's
positivity-preserving DG, which they compare against.

## Qualifications

- Berta et al.'s observed orders exceed four on every grid pair except
  the first WENO-Z one, up to 4.84, for a scheme they call fourth order
  whose interface interpolation they call fifth-order accurate; the
  paper does not comment on the rates above four.
- As printed, Berta et al.'s relativistic balance, Eq. (46), carries a
  factor $W$ (the Lorentz factor) in the centrifugal term, while the
  solution they give, Eqs. (44)–(45) with constant $f=w$, balances the
  same term without it; at the largest vortex speed of these data,
  $v_\phi\approx0.186$ at $R=1/\sqrt2$, $W\approx1.018$, so the two
  differ by up to about 2 % of that term *(compiler check, not in the
  sources)*. The paper does not resolve which of the two equations is
  meant.
- Dzanic & Witherden's run is short ($t=0.05$, a translation of
  $0.05\sqrt2$), and their error is measured against the translated
  exact solution.
- Berta et al. are read as the arXiv v4 preprint, Dzanic & Witherden
  as arXiv v2.

# Citations

- [Berta et al. (2024)](/sources/berta-2024.md) — §5.2, Eqs. (43)–(46), Table 1, Fig. 4 (arXiv v4).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.1, Eqs. (38)–(41), Tables 1–2 (arXiv v2).
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §5.1.1 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — Exs. 6.1, 6.7 (arXiv v1).
