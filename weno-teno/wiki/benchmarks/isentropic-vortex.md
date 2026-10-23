---
type: Benchmark
title: "Isentropic vortex"
description: "Smooth exact solution of the Euler equations, an isentropic vortex advected by a uniform stream (or held steady) on a periodic box; used for design-order convergence studies, which expose the time-step scaling and multidimensional quadrature high orders need, and, with an amplified vortex strength, as a stress test of entropy-conservative fluxes."
status: established
aliases: [isentropic vortex advection, isentropic vortex evolution, vortex convection, steady isentropic vortex]
tags: [benchmark, weno, dg, entropy-stable, finite-volume]
timestamp: 2026-10-23T23:50:00Z
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
[Duan & Tang (2022)](/sources/duan-2022.md)), and a magnetized
relative an ideal-MHD test ([Dao & Nazarov (2022)](/sources/dao-2022.md)).
With a near-vacuum core it becomes a positivity test
([Fan et al. (2023)](/sources/fan-2023.md)). Run for a hundred vortex
widths on a coarse grid, it is also a long-time robustness test of
kinetic-energy-preserving central schemes
([Edoh (2022)](/sources/edoh-2022.md)) and of the choice of energy
equation ([De Michele & Coppola (2023a)](/sources/demichele-2023.md)),
and on a randomly distorted grid a test of free-stream-preserving
metrics ([Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md)).
With a second species rolled up by the vortex and the velocity reversed
at half time it measures the irreversibility added at species interfaces
([Trojak & Dzanic (2024)](/sources/trojak-2024.md)).

## Setup

Let $T=p/\rho$ be the temperature, $\mathcal E$ the vortex strength
and $r$ the distance from the vortex centre (page-local symbols). The
form printed by [Wang et al. (2023b)](/sources/wang-2023-b.md) Example 3
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
| [Wang et al. (2023b)](/sources/wang-2023-b.md) Example 3 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=T_0=1$ | $t=1$; $L^2$ error of $\rho$ on $\Delta x=1/2,\dots,1/64$ |
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
| [Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.3, Eq. (3.1) | $[-5,15]^2$, centre $(5,5)$, periodic | 10.0828 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=0.01$; $L^1$ errors and CPU time, $20^2$ to $640^2$, with and without positivity-preserving limiters |
| [Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.2 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=10$; $L_\infty$ errors on triangles, $h\approx0.1$ to $0.01$ |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.4 | $[0,10]^2$, centre $(5,5)$, exact boundary values | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=1$; $160^2$ to $640^2$ |
| [Wan & Xia (2022)](/sources/wan-2022.md) Ex. 4.3 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=0.2$, $\Delta t\approx\Delta x^{5/3}$; $L^1$, $L^\infty$ errors, $10^2$ to $320^2$ |
| [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) §5.2.1 | $[-10,10]^2$, periodic | 2.5 (printed strength 5 in their normalization) | $\rho_0=p_0=1$, stream $(1,\sqrt2/2)$ or $(1,\sqrt3/2)$, see Qualifications | $t=5$ convergence, CFL 1; $t=200$ on $200^2$ |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.3 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=T_0=1$, stream $(1,1)$ | $T=10$; errors on $25^2$ to $200^2$ (printed "252–2002"); time-step law not stated |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.1 | $[-5,5]^2$, centre at the origin, periodic | 5 | $T_0=1$, stream $(1,1)$ | $t=10$; $L_2$ density error, $25^2$ to $200^2$, CFL 0.2 |
| [De Michele & Coppola (2023a)](/sources/demichele-2023.md) §5.1, Eqs. (79)–(81) | unit square, centre $(0.5,0.5)$, periodic | vortex Mach number $M_{\mathrm v}=0.5$, radius $r_{\mathrm v}=1/15$ | $\rho_\infty=1$, $u_\infty=1$, $M_\infty=0.5$ | robustness: $40^2$ to $t=5$, and $30^2$ to $T=50$ at CFL 0.01, 0.1, 0.5 |
| [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) §8.1.2, Eq. (47) | $[0,16]^2$, centre $(8,8)$, periodic; grid randomized by 20 % in the central region | $C/(U_\infty R)=0.02$ | $\rho=1$, $M=0.1$, advection speed 1 | one period, $t=16$; $64\times64$ |
| [Funada & Imamura (2023)](/sources/funada-2023.md) §3.1 | $[-6,18]\times[-12,12]$, centre at the origin, periodic in $x$, Riemann boundaries in $y$ | $\kappa_{\mathrm v}=0.02$ (page-local) | $\rho=1$, $M_\infty=0.1$, stream along $x$ | $L_\infty$ error of $v_2$ when the vortex reaches $x=8$; $\Delta x=0.375$, $0.1875$, $0.09375$; RK4 |
| [Zaghi et al. (2023)](/sources/zaghi-2023.md) Appendix, Eqs. (A.1)–(A.6) | periodic cube of side 10 m, centre $(2,5,5)$ m, 3D | vortex Mach number $M_{\mathrm v}=0.1$, radius 0.5 m | $\rho_0=1.226$ kg m$^{-3}$, $p_0=101325$ Pa, free-stream Mach 0.1 along $x$ | period 0.29 s; AMR performance test, WENO3, 4768 blocks, about 2.4M cells |
| [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) §8.2.1 | $[0,20]\times[0,10]$, centre $(9,5)$, periodic | $\beta=8.5$ in their form, see below | $\rho_0=p_0=1$, stream $(1,0)$ | $T=2$; $L^2$ errors, $N=1$–$4$, $K_{1D}=2$–$32$ ($2K_{1D}\times K_{1D}$ elements, page-local), quadrilaterals (CFL 0.9) and triangles (CFL 0.5) |
| [Lin & Chan (2024)](/sources/lin-2024.md) §4.2 | $[0,20]\times[0,10]$, $2K_{1D}\times K_{1D}$ elements, periodic | 5.0 in their normalization (analytic solution of §8.2.1 of their earlier paper) | not restated | $T=1$; relative $L^2$ error over $\rho,\rho v_1,\rho v_2,E$ (LGL quadrature), $N=1$–$4$, $K_{1D}=5$–$80$ |
| [Liu et al. (2023b)](/sources/liu-2023-b.md) §5.1.2, Eqs. (43)–(45) | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=2$; $L_\infty$, $L_1$ density errors on uniform triangles, 800 to 12800 points; with and without the PEEB limiter |
| [Maltsev et al. (2023)](/sources/maltsev-2023.md) §3.1 | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=10$; $e_{L^2}$, $e_{L^\infty}$ on triangular, hybrid and uniform meshes, 16–128 edges per side ($P_2$, $P_3$), 8–64 ($P_4$); CFL 0.5 |
| [Cernetic et al. (2023)](/sources/cernetic-2023.md) §5.1, Eqs. (48)–(51) | $[-5,5]^2$, centre at the origin, periodic | 5 | no stream; specific internal energy $1$ at infinity, see below | $t=10$; density $L_1$, degree 0 to 7, exponential in the degree |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.1 | $[-20,30]^2$, centre $(5,5)$, wall boundaries | 5 | $\rho_0=p_0=1$, no stream | $t=1$; $L_2$ errors of $\rho$, $p$, $P_1$–$P_3$ on polygons |
| [Tang (2024)](/sources/tang-2024.md) §4.4.1, Eq. (33) | $[0,10]^2$, centre $(5,5)$, periodic | 5 | $\rho_0=p_0=1$, stream $(1,1)$ | $t=100$, $\Delta x=0.2$; density along $y=5$ |
| [Trojak & Dzanic (2024)](/sources/trojak-2024.md) §5.1.2, Eqs. (37a)–(37f) | $[-10,10]^2$, two species, periodic | Gaussian width $R_{\mathrm v}=1.5$, strength $S_{\mathrm v}=13.5$ | Mach 0.4, stream $(0,1)$, species fraction $\tfrac12\sin(\pi y/10)+\tfrac12$ | to $t=20$, velocity reversed, to $t=40$; $\mathbb P_4$, $20^2$–$80^2$ |
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
zero entropy perturbation, as do Ji, Liang & Fu, Li, Li, Don & Wang and
Wan & Xia with $\mathcal E=5$ on $[0,10]^2$, and Fan et al. with
$\mathcal E=10.0828$. Abgrall & Nassajian Mojarrad write
$\rho=\big[1-\frac{(\gamma-1)\beta_{\mathrm v}^2}{32\gamma\pi^2}e^{1-r^2}\big]^{1/(\gamma-1)}$
and velocity perturbation
$\frac{\beta_{\mathrm v}}{4\pi}e^{(1-r^2)/2}(-\bar y,\bar x)$ with
$\beta_{\mathrm v}=5$ (page-local symbol), $p=\rho^\gamma$: the
table's form with $\mathcal E=\beta_{\mathrm v}/2=2.5$ and $T_0=1$
*(compiler check, not in the sources)*, half the strength
$\mathcal E=5$ of most rows of the table. They choose the stream so that the vortex centre never
crosses grid points.

Chamarthi (2023a) prints
$\rho=\big[1-\frac{(\gamma-1)\mathcal E^2}{8\gamma\pi^2}e^{1-r^2}\big]^{1/(\gamma-1)}$,
$p=\rho^\gamma$ and the table's velocity with $\mathcal E=5$; Chamarthi
(2023b) the table's temperature and velocity. De Michele & Coppola write
$v_1/u_\infty=1-\frac{M_{\mathrm v}}{M_\infty}\frac{\bar y}{r_{\mathrm v}}e^{(1-\hat r^2)/2}$,
$v_2/u_\infty=\frac{M_{\mathrm v}}{M_\infty}\frac{\bar x}{r_{\mathrm v}}e^{(1-\hat r^2)/2}$,
$T/T_\infty=(p/p_\infty)^{(\gamma-1)/\gamma}=(\rho/\rho_\infty)^{\gamma-1}=1-\frac{\gamma-1}2M_{\mathrm v}^2e^{1-\hat r^2}$,
$\hat r=r/r_{\mathrm v}$, $p=\rho^\gamma/(\gamma M_\infty^2)$
($M_{\mathrm v}$, $r_{\mathrm v}$, $\hat r$ page-local): the table's form in
units of the vortex radius, with stream $(1,0)$. Chandravamsi et al.
use a different profile with uniform density, hence not isentropic
*(compiler check, not in the sources)*,
$v_1=1-\frac{C\bar y}{U_\infty R}e^{-r^2/2}$,
$p=1-\gamma M^2\frac{C^2}{U_\infty^2R^2}e^{-r^2}$ ($C$, $R$, $U_\infty$
page-local), and print $v_2=\frac{C\bar x}{U_\infty R^2}e^{-r^2/2}$ with
$R^2$ in place of the $R$ of $v_1$.
Funada & Imamura (after Kawai & Lele) also keep the density uniform:
$v_1=M_\infty\big(1-\kappa_{\mathrm v}\bar y\,e^{-r^2/2}\big)$,
$v_2=M_\infty\kappa_{\mathrm v}\bar x\,e^{-r^2/2}$,
$p=\frac1\gamma-\frac12\kappa_{\mathrm v}^2M_\infty^2\rho\,e^{-r^2}$.
Zaghi et al. print a dimensional three-dimensional vortex after Poinsot
& Lele with $p=p_0(\rho/\rho_0)^\gamma$; their printed $v_2$ carries
$\bar y$ like $v_1$, and their density exponent does not give radial
equilibrium with the printed velocity (see the
[Source page](/sources/zaghi-2023.md), Printed slips).

Liu et al. (2023b) (after Hu & Shu) and Maltsev et al. (after Balsara
& Shu) print the table's form with $\mathcal E=5$, $T=p/\rho$ and unit
background. Lin, Chan & Tomas print
$\rho=\big[1-\frac1{8\gamma\pi^2}\,\tfrac12(\gamma-1)\big(\beta e^{1-r^2}\big)^2\big]^{1/(\gamma-1)}$,
$v=(1,0)+\frac\beta{2\pi}e^{1-r^2}(-\bar y,\ \bar x)$, $p=\rho^\gamma$
($\beta$ page-local), with $e^{1-r^2}$ where the table has
$e^{(1-r^2)/2}$ in the velocity. Writing $r=r'/\sqrt2$ turns it into
the table's form in the coordinate $r'$ with
$\mathcal E=\beta\sqrt{e/2}\approx1.166\,\beta$, i.e. a vortex
$1/\sqrt2$ times narrower and of strength $\mathcal E\approx9.91$ for
$\beta=8.5$ *(compiler check, not in the sources)*. They state that most
experiments in the literature choose $\beta=5$, with minimum density 0.36, and that $\beta=8.5$ gives a minimum
density $2.145\times10^{-3}$; their printed formula gives 0.3617 and
$2.145\times10^{-4}$ at the centre with $\gamma=1.4$ *(compiler check,
not in the sources)*.

Gaburro et al. write the table's form with $\mathcal E=5$ and unit
background through $\delta T$, $\delta\rho=(1+\delta T)^{1/(\gamma-1)}-1$,
$\delta p=(1+\delta T)^{\gamma/(\gamma-1)}-1$, but with no stream; their
section title says "moving" while the text calls the vortex "a
stationary equilibrium". Tang prints
$\rho=[1-\frac{(\gamma-1)\mathcal E^2}{8\gamma\pi^2}e^{1-r^2}]^{1/(\gamma-1)}$,
$p=\rho^\gamma$ and the table's velocity with $\mathcal E=5$; the final
time $t=100$ is ten periods of the stream $(1,1)$ on $[0,10]^2$
*(compiler check, not in the sources)*. Cernetic et al. (after Yee et
al.) print the steady vortex through the specific internal energy,
$\mathrm e=1-\frac{\mathcal E^2}{8\gamma\pi^2}e^{1-r^2}$, $\rho=[(\gamma-1)\mathrm e]^{1/(\gamma-1)}$
($\mathrm e$ page-local), with the table's velocity perturbation and no
stream: this is the table's form with $T_0=\gamma-1=0.4$ and
$\rho_0=0.4^{2.5}\approx0.101$, which satisfies the radial balance
because the isentropic balance does not depend on $T_0$ *(compiler check,
not in the sources)*. Trojak & Dzanic's profile is that of the two
Dzanic papers below ($S_{\mathrm v}=13.5$, $R_{\mathrm v}=1.5$, $M=0.4$,
stream $(0,1)$), written per species with $\gamma_0=\gamma_1=1.4$ but
different heat capacities ($c_p=1.4$, $c_v=1$ and $c_p=2.8$, $c_v=2$).

**Near-vacuum strength.** With $\mathcal E=10.0828$ and unit
background the centre temperature is
$1-\frac{(\gamma-1)\mathcal E^2}{8\gamma\pi^2}e=2.28\times10^{-6}$,
the density $7.83\times10^{-15}$ and the pressure $1.78\times10^{-20}$
*(compiler check, not in the sources)*: Fan et al. print the minima
$7.8\times10^{-15}$ and $1.7\times10^{-20}$, the same strength as Chen &
Wu's relativistic case below.

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
is a narrower vortex. Edoh does not print $\gamma$; with $\gamma=1.4$ the
background is $p_\infty=114285.7$ Pa, $c_\infty=400$ m s$^{-1}$, Mach 0.5,
the centre temperature drops by $21.4\,\%$ and the minimum density is
$0.5479$ kg m$^{-3}$, the value Edoh prints *(compiler check, not in the
sources)*, which supports $\gamma=1.4$.

### MHD version

[Dao & Nazarov (2022)](/sources/dao-2022.md) §5.1.1 run the smooth
ideal-MHD vortex of Wu & Shu, as they cite it, on $[-10,10]^2$,
periodic, $\gamma=5/3$, to $t=0.05$: background
$(\rho,v,p,B)=(1,(1,1),p_0,(0.1,0.1))$ with
$\delta v=\frac{\mu_{\mathrm v}}{\pi\sqrt2}e^{(1-r^2)/2}(-\bar y,\bar x)$,
$\delta B=\frac{\mu_{\mathrm v}}{2\pi}e^{(1-r^2)/2}(-\bar y,\bar x)$,
$\delta p=-\frac{\mu_{\mathrm v}^2(1+r^2)e^{1-r^2}}{8\pi^2}$,
$\mu_{\mathrm v}=5.389489439$ (page-local symbol). They print $p_0=0$,
which makes the pressure negative everywhere; the printed
$\mu_{\mathrm v}$ gives $\delta p=-1.0000$ to ten digits at the centre,
so a background $p_0=1$ would leave a centre pressure of about
$5\times10^{-12}$ *(compiler check, not in the sources)*. On continuous
$\mathbb P_1$–$\mathbb P_3$ elements with their residual-based
[artificial viscosity](/methods/artificial-viscosity.md) the
viscous and Galerkin solutions have nearly the same errors; $\mathbb P_3$
reaches about fourth order in $L^1$ (rates 3.81, 3.96, 3.71 for the
velocity), $\mathbb P_2$ only second, which they call a known
suboptimality of continuous Galerkin (Table 1, Fig. 1). Their rates are
computed from the degrees of freedom, not from a mesh halving.

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.1, Eqs.
(38)–(41) (arXiv v2) run what they cite as the near-vacuum magnetized
vortex of Christlieb et al., with the same constant
$\mu_{\mathrm v}=5.38948938512$: on $[-10,10]^2$, periodic, $\gamma=5/3$,
$\rho=1$, $v=(1,1)+\delta v_{\mathrm v}(-y,x)$, $B=\delta B_{\mathrm v}(-y,x)$,
$p=1+\delta p$, with printed
$\delta v_{\mathrm v}=\frac{\mu_{\mathrm v}}{\sqrt{2\pi}}\varphi$,
$\delta B_{\mathrm v}=\frac{\mu_{\mathrm v}}{2\pi}\varphi$,
$\delta p=-\frac{\mu_{\mathrm v}^2(1+r^2)}{8\pi^2}\varphi^2$,
$\varphi=e^{1-r^2}$ (page-local), to $t=0.05$ with $\Delta t=10^{-4}$,
error of $B$ in $L^1$ against the translated solution. They state a
minimum pressure of about $2\times10^{-8}$; with the printed $\varphi^2$
the centre pressure is $1-\mu_{\mathrm v}^2e^2/(8\pi^2)\approx-1.72$,
and the stated minimum follows with $\varphi$ in place of $\varphi^2$
($1-\mu_{\mathrm v}^2e/(8\pi^2)=2.0\times10^{-8}$) *(compiler check, not
in the sources)*, so one exponent is misprinted. On $20^2$ to $67^2$
quadrilaterals their positivity-preserving
[entropy filter](/methods/entropy-filtering.md) in nodal DG gives rates
2.89, 3.80, 4.62, 5.23 for $\mathbb P_2$–$\mathbb P_5$ ($\mathbb P_2$:
$2.29\times10^{-4}$ to $6.92\times10^{-6}$; $\mathbb P_5$:
$4.04\times10^{-7}$ to $6.51\times10^{-10}$), with the filter strength
$1-f$ at most $1.08\times10^{-4}$, i.e. negligible activity (Tables
1–2).

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

Wan & Xia run the same refined time step $\Delta t\approx\Delta x^{5/3}$
for their [hybrid WENO](/methods/hybrid-weno.md) WENO-H against the
linear upwind scheme UW5, CWENOZ and MRWENO. They state that all
schemes reach fifth order; the printed WENO-H orders are irregular,
3.45 ($L^1$) and 2.42 ($L^\infty$) at $80^2$, then 6.71 and 8.19 at
$160^2$, with 4.62–4.67 for all schemes at $320^2$, and the WENO-H
$L^1$ error at $80^2$, $2.22\times10^{-4}$, is 3.5 times that of UW5,
$6.33\times10^{-5}$ (Ex. 4.3, Table 4.2); recomputing
$\log_2(2.42\times10^{-3}/2.22\times10^{-4})=3.45$ and
$\log_2(2.22\times10^{-4}/2.12\times10^{-6})=6.71$ reproduces the
printed orders *(compiler check, not in the sources)*, so the
irregularity is in the printed errors, not in the rate computation.

**Scale invariance costs accuracy on coarse grids.** Li, Li, Don & Wang
compare their scale-invariant multi-resolution
[A-WENO](/methods/alternative-weno.md) (MR-AWENO-Si) with MR-AWENO:
both reach fifth order once the vortex is resolved, with identical
errors from $320^2$ on ($3.31\times10^{-9}$ to $1.04\times10^{-10}$), but at
$160^2$ the scale-invariant scheme's error is $3.09\times10^{-6}$
against $1.05\times10^{-7}$, about 30 times larger, and its printed
first order of 9.87 is the drop from that coarse error (§3.4, Table 2);
$\log_2(3.09\times10^{-6}/3.31\times10^{-9})=9.87$ *(compiler check, not in
the sources)*. See [scale invariance](/properties/scale-invariance.md).

**Unstructured TENO.** Ji, Liang & Fu verify the design order of their
finite-volume TENO3–6 on triangles in $L_\infty$, with the numbers
shown only in a figure (§5.2, Fig. 2); see
[TENO](/methods/targeted-eno.md) and [UCNS3D](/software/ucns3d.md).

**Positivity limiters on a near-vacuum vortex.** Fan et al. run the
$\mathcal E=10.0828$ vortex with their finite-difference
[Hermite WENO](/methods/hermite-weno.md) HWENO-R, HWENO-L and WENO-ZQ,
with (WL) and without (WO) the [positivity-preserving flux
limiter](/methods/positivity-preserving-flux-limiter.md), to $t=0.01$.
All three reach fifth order either way (HWENO-R $L^1$ errors
$1.24\times10^{-3}$ at $20^2$ to $1.34\times10^{-11}$ at $640^2$,
orders 3.23, 4.32, 7.11, 6.64, 5.16), but the WO runs print negative
minima on coarse meshes, $p_{\min}=-1.90\times10^{-3}$ for HWENO-R on
$40^2$ and $-1.55$ for HWENO-L on $20^2$, $\rho_{\min}=-1.92\times10^{-4}$
for WENO-ZQ on $40^2$, and still run to the end (Table 3.3). On
meshes from $320^2$ the CPU ratio HWENO-R/WENO-ZQ is 1.823 (WO) and
1.609 (WL) at about 1/5.5 of the error, so they call HWENO-R more
efficient (Ex. 3.3, Fig. 3.3). See [bound
preservation](/properties/bound-preservation.md).

**CFL above one with kinetic schemes.** Abgrall & Nassajian Mojarrad
run their arbitrary-order [discrete kinetic relaxation
scheme](/methods/discrete-kinetic-relaxation-scheme.md) with
[deferred-correction](/methods/deferred-correction.md) time stepping
(four-wave model, fourth order in space and time) at CFL 1, measured
on the kinetic speeds: the $t=5$ convergence curves approach fourth
order (Fig. 6), and on $200^2$ to $t=200$, about twenty crossings, the
pressure error stays in $[-4.2\times10^{-3},1.6\times10^{-3}]$ (Fig. 7);
with five iterations CFL 1.2 reaches $t=200$, while they could not run
above CFL 1.3 (Remark 1, §4).

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
gives $\Delta t\propto\Delta x$ (Eq. 40). Wang et al.'s CFL
$\Delta x^{2/3}$ and Li et al.'s
$\Delta t=C_{\mathrm{CFL}}(\min\Delta\xi_k)^{5/3}$ (Li et al., §5) realize
the same balance for fifth order with a third-order integrator
*(compiler check, not in the sources)*. See
[SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md).

**Exponential convergence of modal DG.** Cernetic et al.'s GPU DG code
([TENET](/software/tenet.md)) converges as $L_1\propto N_x^{-(N+1)}$ for
degrees $N=0$ to 7, with fitted orders slightly above design except at
$N=0$, and at fixed $N_x$ the error falls exponentially with the degree;
an edge effect of the periodic box floors $L_1$ at about $10^{-11}$
(§5.1, Fig. 5). Error and initial projection use $N+2$ Gauss points per
direction. See [discontinuous Galerkin](/methods/discontinuous-galerkin.md).

**Primitive-variable DG with a posteriori limiting.** Gaburro et al.'s
[ADER](/methods/ader-scheme.md)-DG in primitive variables on polygonal
meshes, with the subcell limiter never activated, gives $L_2$ density
errors $1.28\times10^{-1}$ to $9.86\times10^{-3}$ for $P_1$ (orders 2.3,
2.4, 2.2), $4.43\times10^{-2}$ to $2.06\times10^{-3}$ for $P_2$ (2.6,
2.9, 2.7) and $3.55\times10^{-2}$ to $2.73\times10^{-3}$ for $P_3$ (3.3,
3.6, 3.8), with similar pressure errors, which they call the expected
orders, "up to fourth order" (§5.1.1, Table 1).

**Long-time resolution of adaptive TENO.** On Tang's coarse grid
($\Delta x=0.2$) after ten periods the adaptive-cut-off TENO-AZ density
along $y=5$ is closer to the exact one than that of TENO-Z, TENO-A and
TENO-LAD (§4.4.1, Fig. 10; see [adaptive TENO](/methods/adaptive-teno.md));
it costs 0.98–1.01 of TENO-Z's time per step on $100\times100$ (Table 6).

**Interface dissipation of a multi-species entropy filter.** Trojak &
Dzanic run their positivity-preserving
[entropy filter](/methods/entropy-filtering.md) for two-species DG at
$\mathbb P_4$ to $t=20$, reverse the velocity and run to $t=40$, so that
a reversible scheme would return the initial species field; there is
no exact multi-species solution, and the irreversibility is their error
proxy. With their pressure-jump entropy switch the species roll-up is
well resolved on $40^2$ and converges towards $80^2$; with the entropy
constraint enforced everywhere, the $80^2$ run is on the level of the
$20^2$ run with the switch (§5.1.2, Figs. 1–4).

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

**Fourth order of RBF differential-quadrature finite volumes.** Liu
et al. (2023b) find their implicit
[RBF differential-quadrature](/methods/rbf-differential-quadrature.md)
finite volumes, LSFD-FV and k-exact FV all at fourth order in
$L_\infty$ and $L_1$ of density on the four triangular meshes, with
IRBFDQ-FV the most accurate and the cheapest at equal error (no
numbers in the text); switching on their PEEB limiter changes the
errors only slightly (§5.1.2, Figs. 3–5).

**Positivity-only limiting of entropy-stable DG.** On Lin, Chan &
Tomas's strengthened vortex, unlimited entropy-stable DG fails "due to
large jumps in the density and pressure"; with elementwise blending
under bounds relaxed by $\zeta_{\mathrm r}=0.1$ and $0.5$ (their $\zeta$) the solutions converge with
asymptotic rates between $N+\tfrac12$ and $N+1$, which they call
optimal, e.g. $N=4$ on quadrilaterals $1.915\times10^{-4}$ at $K_{1D}=32$
with last rates 6.30 ($\zeta_{\mathrm r}=0.1$) and 5.21 ($\zeta_{\mathrm r}=0.5$), and
$3.248\times10^{-4}$ (rate 4.85) on triangles (Tables 6–9). The
quadrilateral $N=4$, $K_{1D}=32$ error is identical for both $\zeta_{\mathrm r}$, as
limiting is inactive there. See
[convex limiting](/methods/convex-limiting.md).

**Entropy limiting that keeps high order.** Lin & Chan (2024) use the
vortex, at a strength for which no positivity limiting is needed and
with the convex-constraint factors set to 1, to compare entropy
limiters for [subcell-limited DGSEM](/methods/subcell-finite-volume-limiting.md).
Their limiter, which enforces a semi-discrete cell entropy inequality by
solving a small linear program for the subcell limiting factors, shows
"an asymptotic convergence rate between $O(h^{N+1/2})$ and $O(h^{N+1})$"
(Table 1; last printed rates 1.84, 2.74, 4.28, 4.36 for $N=1$–4). The
local minimum-entropy-principle limiter gives at most first order (last
rates 0.86, 0.93, 0.90, 0.95; Table 2), and its relaxed form at most
second (1.52, 1.21, 1.49, 1.31; Table 3), for every $N$. High order of
their limiter is shown numerically only, not proved (§4.2). See
[entropy stability](/properties/entropy-stability.md).

**Troubled-cell switching in hybrid DG–FV.** Maltsev et al. find pure
DG close to design order, while CWENOZ finite volumes of the same
polynomial order reach it only on finer meshes (quadrilateral $P_4$:
DG $e_{L^2}$ $2.97\times10^{-4}$ to $1.14\times10^{-9}$ from 8 to 64
edges, FV $7.64\times10^{-2}$ to $7.20\times10^{-4}$); their MOOD-type
switch flags cells in the vortex core, from 26–46 % of the cells on the
coarsest meshes to 0.08–0.16 % on the finest $P_2$ and $P_3$ meshes
(0.35–0.72 % for $P_4$ on 64 edges), and the hybrid then costs 1.26–1.56
times pure DG on the coarsest and 1.01–1.06 times on the finest meshes
(Table 1, Fig. 4). See
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

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
the divergence form is unstable within five widths and Edoh's rotational
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

**Primitive-variable state reconstruction caps the order at two.**
Chamarthi (2023a) finds every scheme the author runs, the fourth-order
[gradient-based](/methods/gradient-based-reconstruction.md) MEG6 and
MIG4 and TENO5 alike, only second order on the vortex, with nearly
equal errors on $200^2$ ($4.10\times10^{-5}$ for all), although on
linear advection MIG4 and MEG6 are fourth and TENO5 fifth order (Tables
2–3). Chamarthi attributes this to reconstructing primitive variables and
evaluating the flux of the reconstructed states, after Zhang, Zhang &
Shu, and states that other published schemes (BVD, P4T2, Fu's
finite-volume TENO) share it without having computed their order.
Chamarthi (2023b) removes the limitation by blending, interface by
interface, a reconstruction of the point fluxes with the flux of the
limited state through a density-based detector; the seventh-order MEG7
then reaches $L_2$ rates 5.25, 6.03, 6.59 (conservative variables) and
5.13, 6.00, 6.68 (primitive) on $50^2$, $100^2$, $200^2$, against 4.71,
6.35, 6.24 for the seventh-order mapped WCNS7M, with errors about
$1.0\times10^{-8}$–$1.5\times10^{-8}$ on $200^2$ (Table 1). Chamarthi calls this
seventh-order accuracy; the observed rates stay below seven on these
grids.

**Energy equation and long-time robustness.** De Michele & Coppola run
central, non-dissipative schemes with kinetic-energy-preserving mass and
momentum fluxes and fifteen discretizations of an energy-like equation
(total energy, internal energy, pressure, total enthalpy, sound speed,
entropy). On $40^2$ with eighth-order central derivatives, RK4 at CFL
0.01, the linear invariants are preserved to round-off and the entropy,
internal and kinetic energy drift differently by formulation (Figs.
1–5). On $30^2$ with fourth-order derivatives to $T=50$, the
internal-energy forms $(\rho e)$ and $(\rho e)_{\mathrm{PEP}}$ and the
KGP-split sound-speed and entropy forms never blow up at CFL 0.01, 0.1
or 0.5, while the total-energy and total-enthalpy forms blow up between
$t=21$ and $47$ except $(\rho E)_{\mathrm{PEP}}$ and $(\rho H)_{H+\hat p}$
at CFL 0.5 (Table 3). See [kinetic energy preservation](/properties/kinetic-energy-preservation.md),
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
and [split convective forms](/methods/split-convective-forms.md).

**Free-stream preservation on distorted grids.** Chandravamsi et al.
advect the vortex for one period through a $64\times64$ grid whose
central region is randomized by 20 % (maximum included angle about
$160^\circ$): with their [free-stream-preserving](/properties/free-stream-preservation.md)
metrics the MEG6 and MIG4 schemes keep the vortex and its swirl-velocity
profile, while non-preserving metrics give an unphysical solution at
$t=16$ (§8.1.2, Fig. 8).

**Order of a flux-reconstruction solver without walls.** Funada &
Imamura use their weak vortex to show that their
[flux reconstruction](/methods/flux-reconstruction.md) on hierarchical
Cartesian grids reaches order $k$ for $k=2,3,4$ in the $L_\infty$
error of $v_2$ before they test immersed walls (§3.1, Fig. 10; see
[flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)).

**Adaptive mesh refinement.** Zaghi et al. advect their vortex through
the block-octree [adaptive mesh](/methods/adaptive-mesh-refinement.md)
of [ADAM](/software/adam.md) (maximum level 5, finest spacing 0.0625,
refinement on the enthalpy gradient). The smearing they observe comes
from the dissipation of WENO3, the level jumps "seem to not pollute the
solution", and the strong scaling up to 16 GPUs is comparable with that
of their shock-diffraction runs (Appendix, Figs. A.17–A.18).

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

- Fan et al. print the temperature perturbation as
  $+\frac{(\gamma-1)\mathcal E^2}{8\gamma\pi^2}e^{1-r^2}$ (Eq. (3.1)); with the
  plus sign the centre temperature would be about 2, and only the minus
  sign of Ji, Liang & Fu, Li, Li, Don & Wang and Wan & Xia gives their
  printed minima *(compiler check, not in the sources)*.
- Abgrall & Nassajian Mojarrad print $v_2=\frac{\sqrt2}2+\dots$ in the
  initial data and $v_{2,\infty}=\sqrt3/2$ for the free stream that
  moves the centre; one of the two is a slip. They do not state the
  relaxation parameter or kinetic speeds used.
- Dao & Nazarov label the second error block of the $\mathbb P_2$ and
  $\mathbb P_3$ panels of Table 1 "$u$", where the caption and the
  $\mathbb P_1$ panel indicate $B$.
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
  $\delta T/T_\infty=0.001$. With $\gamma=1.4$ the printed temperature
  perturbation is $0.02895\,e^{2(1-r^2)}T_\infty$, which equals
  $0.001\,T_\infty$ at $r=1.64$, a diameter of about 3.3 m; 2.1 m
  corresponds to a threshold of about 0.024, both computed with the
  unprinted $\gamma=1.4$ *(compiler check, not in the sources)*. The threshold or the
  diameter is misprinted, or the diameter is defined otherwise.
- De Michele & Coppola print $\Delta t=1.8\times10^{-4}$ at CFL 0.01 on
  $h=1/40$ without a CFL definition; neither $\mathrm{CFL}\,h/(\lvert u\rvert+c)$
  ($8.3\times10^{-5}$) nor $\mathrm{CFL}\,h/u_\infty$ ($2.5\times10^{-4}$)
  reproduces it *(compiler check, not in the sources)*. They also print
  $T_\infty=720M_{\mathrm v}r_{\mathrm v}$, a value used nowhere else.
  Their remark that higher resolution can lower the blow-up time
  compares runs that differ in both grid and order ($40^2$ eighth order,
  $30^2$ fourth order).
- Maltsev et al. state that the simulation runs "for 10 periods" with
  errors at "final time $t=10$"; with stream $(1,1)$ on the periodic
  $[0,10]^2$ one period is $t=10$ *(compiler check, not in the
  sources)*. Their Table 1 prints a DG $L^\infty$ order of 6.69 for
  quadrilateral $P_4$ at 32 edges, where
  $\log_2(6.99\times10^{-5}/5.63\times10^{-7})=6.96$ *(compiler check,
  not in the sources)*.
- Lin, Chan & Tomas are read as arXiv v2.
- Lin & Chan (2024) print in Table 1, $N=2$, the rate 1.11 at
  $K_{1D}=20$ and 2.74 at $K_{1D}=80$, where the printed errors give
  $\log_2(1.785\times10^{-1}/4.126\times10^{-2})=2.11$ and
  $\log_2(6.714\times10^{-3}/1.210\times10^{-3})=2.47$ *(compiler check,
  not in the sources)*. With 2.47, and with the last rates 4.28 for
  $N=3$ (above $N+1$) and 4.36 for $N=4$ (below $N+\tfrac12$), not all
  rates lie in the band $[N+\tfrac12,N+1]$ that their text states
  *(compiler check, not in the sources)*.
- Gaburro et al.'s last $P_3$ orders, 3.8 ($\rho$) and 3.6 ($p$), are
  3.53 and 3.40 when recomputed from the printed errors and the printed
  $h=1.15$ and $0.92$; rounding $h$ to two digits moves them to at most
  3.69 and 3.56, which covers the printed 3.6 for $p$ but not the 3.8 for
  $\rho$ *(compiler check, not in the sources)*. They do not define
  $r$, and are read as arXiv v1.
- Tang prints "$r=\bar x^2+\bar y$" in Eq. (33), where the formulas need
  $r^2=\bar x^2+\bar y^2$.
- Cernetic et al. (arXiv v2, accepted) label curves by the polynomial
  degree in their figures but call $p=n+1$ the order in §2.3, so their
  "$p$" alternates between order and degree; the ranges above are given
  in degrees. Trojak & Dzanic are read as arXiv v1.
- Chamarthi (2023a) and (2023b) are read as arXiv preprints, Chandravamsi
  et al. and De Michele & Coppola (2023a) as arXiv v1.
- Yu & Hesthaven's DG solution and Du et al.'s unlimited DG are the
  baselines of their tests; the sub-design orders above are those of
  the baselines, not of the shock-capturing devices.

# Citations

- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4, Example 3, Table 1.
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
- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — §4, Remark 1; §5.2.1, Figs. 6–7.
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §5.1.1, Table 1, Fig. 1 (arXiv v1).
- [Fan et al. (2023)](/sources/fan-2023.md) — Ex. 3.3, Eq. (3.1), Table 3.3, Fig. 3.3.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.2, Fig. 2 (preprint).
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §3.4, Table 2.
- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.3, Table 4.2.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.3, Tables 2–3 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.1, Table 1 (arXiv v1).
- [De Michele & Coppola (2023a)](/sources/demichele-2023.md) — §5.1, Eqs. (79)–(81), Table 3, Figs. 1–5 (arXiv v1).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §8.1.2, Eq. (47), Fig. 8 (arXiv v1).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.1, Eqs. (38)–(41), Tables 1–2 (arXiv v2).
- [Funada & Imamura (2023)](/sources/funada-2023.md) — §3.1, Fig. 10.
- [Zaghi et al. (2023)](/sources/zaghi-2023.md) — Appendix, Eqs. (A.1)–(A.6), Figs. A.16–A.18.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.2.1, Tables 6–9 (arXiv v2).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §4.2, Eq. (60), Tables 1–3.
- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §5.1.2, Eqs. (43)–(45), Figs. 3–5.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §3.1, Table 1, Fig. 4.
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — §5.1, Eqs. (48)–(51), Fig. 5 (arXiv v2).
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.1.1, Table 1 (arXiv v1).
- [Tang (2024)](/sources/tang-2024.md) — §4.4.1, Eq. (33), Fig. 10, Table 6.
- [Trojak & Dzanic (2024)](/sources/trojak-2024.md) — §5.1.2, Eqs. (37a)–(37f), Figs. 1–4 (arXiv v1).
