---
type: Benchmark
title: "Double Mach reflection"
description: "Two-dimensional Euler benchmark in which a Mach 10 shock at 60° to a reflecting wall forms a double Mach stem, slip line and wall jet; used to rank the numerical dissipation of shock-capturing schemes by the Kelvin–Helmholtz roll-up along the slip line."
status: established
aliases: [DMR, double Mach reflection of a strong shock, Woodward–Colella double Mach reflection]
tags: [benchmark, low-dissipation, weno, teno, dg]
timestamp: 2026-10-23T23:55:00Z
---

# Double Mach reflection

A planar shock of Mach number $M=10$ moves into quiescent ideal gas
($\gamma=1.4$) and meets a reflecting wall at an incidence that makes
the shock front an angle of $60^\circ$ with the wall. Balsara et al. describe it as the similarity solution of
a wedge put in a supersonic flow, and Deng as a Mach 10 shock on a
$30^\circ$ ramp; the problem is computed with the wedge face as the
lower boundary, so that the shock is inclined. The reflection is a double
Mach reflection: two triple points, a primary and a secondary Mach stem,
a slip line from the primary triple point and a wall jet. The slip line
is Kelvin–Helmholtz unstable, and the amount of roll-up a scheme
resolves on a given grid is the visual gauge of its
[numerical dissipation](/definitions/numerical-dissipation.md) in every
source that runs it. Forty-five sources of the bundle run it,
forty-one in the Woodward–Colella form (one of them on a randomly
distorted curvilinear grid) and four in a variant (two
wedges in the physical frame on unstructured meshes, a relativistic
version, a dimensional ramp with an immersed boundary); most cite Woodward & Colella (1984)
for it, while Peng, Sun & Wu cite no source for the setup. A Mach 10
reflection-and-diffraction relative over a backward step is recorded
under Variants.

## Setup

Common data, as printed by
[Fu (2021)](/sources/fu-2021.md) §5.5.1,
[Takagi et al. (2022)](/sources/takagi-2022.md) §4.6,
[Ye et al. (2022)](/sources/ye-2022.md) §4.8 and
[Huang et al. (2026)](/sources/huang-2026.md) §6.7, Eq. (6.9), and
likewise by [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.6,
[Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.8,
[Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.5, Eq. (42) and
[Liang et al. (2022)](/sources/liang-2022.md) §4.5, in
$(\rho,v_1,v_2,p)$:

$$
(\rho,v_1,v_2,p)(x,y,0)=\begin{cases}
(8,\ 7.145,\ -4.125,\ 116.8333), & y\ge 1.732\,(x-0.1667),\\
(1.4,\ 0,\ 0,\ 1), & \text{otherwise},
\end{cases}
$$

on $[0,4]\times[0,1]$ to $t=0.2$. The lower boundary carries the
post-shock state on $0\le x\le 1/6$ and is a reflecting wall on
$1/6\le x\le 4$; left inflow, right outflow; the upper boundary
follows the exact motion of the oblique shock (stated explicitly by
[Wang et al. 2023b](/sources/wang-2023-b.md), Example 4, and
[Balsara et al. 2024](/sources/balsara-2024.md) §IX.h; Peng, Sun & Wu,
Ex. 5.17, write it as post-shock data on $0\le x\le\tfrac16+(1+20t)/\sqrt3$
of the upper boundary). [Pazner (2021)](/sources/pazner-2021.md) §5.7
states the same boundary set: post-shock state on the left and on
$[0,1/6]$ of the bottom, slip wall on $[1/6,4]$, exact shock motion on
the top, outflow on the right, pre-shock $\rho=1.4$, $p=1$.

[Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.17 and
[Wang et al. (2023b)](/sources/wang-2023-b.md) Example 4 and
[Zhou et al. (2023)](/sources/zhou-2023.md) §5.5, Eq. (40) and
[Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 15, Eq. (49) write the same
geometry as $x<\tfrac16+y/\sqrt3$ with post-shock state
$(8,\ 8.25\cos\tfrac\pi6,\ -8.25\sin\tfrac\pi6,\ 116.5)$, and
[Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.4,
[Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.8 and
[Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) §8.1.3
print the same state for $x<1/6+y/\tan60^\circ$, pre-shock $(1.4,0,0,1)$;
Chandravamsi et al. state the boundaries as post-shock on the left,
zero gradient on the right, post-shock on $[0,1/6]$ and reflecting wall
on $[1/6,3]$ of the bottom, time-dependent top. The same
post-shock pressure $116.5$ is printed by
[Bezgin et al. (2022)](/sources/bezgin-2022.md) Eq. (37), as
$(8,7.145,-4.125,116.5)$ above $y=1.732(x-0.1667)$;
[Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.3, as
$(\rho,p,v_1,v_2)=(8,116.5,8.25\cos30^\circ,-8.25\sin30^\circ)$ with
the shock through $(1/6,0)$ at $60^\circ$ to the $x$-axis;
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.4, as
$(8,7.14471,-4.125,116.5)$ for $x<1/6+\tan(30^\circ)\,y$, with the
upper boundary moving as $x\le1/6+\tan(30^\circ)\,y+\frac{10}{\cos30^\circ}t$;
[Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.6 and
[Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.5, as
$(8,8.25\cos\theta,-8.25\sin\theta,116.5)$ for $x<\tfrac16+y/\sqrt3$
with $\theta=\pi/6$ (Hong, Ye & Ye call $\theta$ the angle between the
shock and the $y$-axis); [Li, Chen & Ren (2022)](/sources/li-2022.md)
§4.3.1, as $(8.0,7.1447,-4.125,116.5)$ for $x\le\tfrac16+\sqrt3y/3$;
[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.6, as
$(8.0,\,8.25\cos30^\circ,\,-8.25\sin30^\circ,\,0,\,116.5)$ with a third
velocity component, for $x\le x_0+\sqrt{1/3}\,y$; and
[Hiejima (2022)](/sources/hiejima-2022.md) §3.4, Eq. (29), as
$(8.0,\ 8.25\sin\theta,\ -8.25\cos\theta,\ 116.5)$ with
$\theta=60^\circ$ the angle of the shock to the $x$-axis and the upper
boundary at $x_s=10t/\sin\theta+1/6+1/\tan\theta$.
Zhong et al. impose the post-shock state on the left boundary and on
$[0,1/6]$ of the bottom, a reflective wall on $[1/6,4]$, outflow on the
right and, on the top, the post-shock state for $x<s(t)=\tfrac16+(1+20t)/\sqrt3$.
[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) §8.4 (arXiv v2) print
the same post-shock and pre-shock states on $[0,3.5]\times[0,1]$, with
the front written as the zero line of $y-\sqrt3x+\sqrt3/6$, a reflective
wall on $[1/6,3.5]$ of the bottom and exterior states moving with
$s(t)=\frac{1+\sqrt3/6}{\sqrt3}+\frac{10}{\cos(\pi/6)}t$, which is the
same top-boundary law as Zhong et al.'s, since
$\frac{1+\sqrt3/6}{\sqrt3}=\frac16+\frac1{\sqrt3}$ and
$\frac{10}{\cos(\pi/6)}=\frac{20}{\sqrt3}$ *(compiler check, not in the
sources)*. [Maltsev et al. (2023)](/sources/maltsev-2023.md) §3.4 give
the Mach 10 shock starting at $x=1/6$, pre-shock $\rho=1.4$, $p=1$, on
$[0,4]\times[0,1]$ to $t=0.2$, and [Wang et al. (2023c)](/sources/wang-2023-c.md)
Example 4.5 the domain $[0,4]\times[0,1]$ and $t=0.2$, deferring the
rest of the description to the literature.
[Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.4 give the geometry
($[0,4]\times[0,1]$, wall from $x=1/6$, Mach 10 shock at $60^\circ$,
$t=0.2$) without printing the states. The line
$y=1.732(x-0.1667)$ is the same front to the printed digits, and the
velocity components agree ($8.25\cos30^\circ=8.25\sin60^\circ=7.145$,
$8.25\sin30^\circ=8.25\cos60^\circ=4.125$). The two groups differ in the post-shock
pressure, $116.5$ versus $116.8333$. The Rankine–Hugoniot conditions
for a Mach 10 shock entering $(\rho,p)=(1.4,1)$ with $\gamma=1.4$
(sound speed $c=1$, shock speed $10$) give
$\rho=1.4\cdot\frac{(\gamma+1)M^2}{(\gamma-1)M^2+2}=1.4\cdot\frac{240}{42}=8$,
a post-shock speed $\frac{2c}{\gamma+1}\big(M-\frac1M\big)=8.25$ and
$p=1+\tfrac{2\gamma}{\gamma+1}(M^2-1)=1+\tfrac76\cdot99=116.5$
*(compiler check, not in the sources)*, so
$116.5$ is the Rankine–Hugoniot post-shock pressure and $116.8333$ is
$1/3$ (about 0.29 %) higher; Fu (2021), Takagi et al., Ye et al. and
Huang et al., Huang, Liang & Fu, Ji, Liang & Fu (2022, 2023) and
Liang et al. print it without comment. It is a setup difference, not a
contradiction: no source compares the two. The shock's horizontal
speed $10/\sin60^\circ=10/\cos30^\circ=20/\sqrt3$ matches the
upper-boundary formulas of Peng et al., Dzanic & Witherden and Hiejima
*(compiler check, not in the sources)*.

[Tang (2024)](/sources/tang-2024.md) §4.4.4, Eq. (36) prints, under
the heading $(\rho,v_1,v_2,p)$, the states $(8,\ 57.1597,\ -33.0012,\ 563.544)$
for $y<\sqrt3(x-1/6)$ and $(1.4,0,0,2.5)$ otherwise on $[0,4]\times[0,1]$.
These are the conservative variables $(\rho,\rho v_1,\rho v_2,E)$ of the
Woodward–Colella states: $E=1/(\gamma-1)=2.5$ for $p=1$ at rest, and the
post-shock $8\cdot8.25\cos30^\circ=57.158$, $-8\cdot8.25\sin30^\circ=-33.0$
and $116.5/0.4+\tfrac12\cdot8\cdot8.25^2=563.5$ match the printed values
to about $10^{-4}$ relative *(compiler check, not in the sources)*.
The inequality $y<\sqrt3(x-1/6)$ assigns the post-shock state to the
region below the front, the opposite side to the other sources' $y\ge1.732(x-0.1667)$,
which is the gas at rest ahead of the shock on the wall side; the
text does not otherwise state which side carries the post-shock state.

[Lesur et al. (2023)](/sources/lesur-2023.md) §4.1 take "Colella &
Woodward (1984) initial conditions" without printing them, and
[Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.8 give the Mach 10 shock
at $x=1/6$ and $60^\circ$ on $[0,4]\times[0,1]$ to $t=0.2$.

Wording differs in one more place: Ye et al. call the shock "at 30°"
starting at $x=1/6$, [Deng (2023)](/sources/deng-2023.md) App. A.11
speak of "a 30° ramp", Dzanic & Witherden and Mossier, Beck & Munz of
a "30° ramp" and Hiejima
of a shock "reflected by an inclined plane of 30°", whereas Fu, Takagi
et al., Huang et al., Peng et al., Du et al., Yu & Hesthaven and
[Balsara et al. (2024)](/sources/balsara-2024.md) §IX.h speak of a
$60^\circ$ incidence, and Maltsev et al. of a "ramp inclined by
$\alpha=60^\circ$". The printed data are the same; a shock normal to
the flow meets a $30^\circ$ ramp at $60^\circ$, so the two angles
describe one configuration *(compiler check, not in the sources)*.

### Variants

- **Wedge in the physical frame, unstructured mesh.**
  [Chen et al. (2022)](/sources/chen-2022.md) §6.5 compute the
  original wedge geometry instead of the rotated one: a Mach 10 shock
  at $x=0$ moves into $(\rho,v_1,v_2,p)=(1.4,0,0,1)$, the post-shock
  state "from the Rankine–Hugoniot relations", on
  $[-0.5,2.5]\times[0,2.5]$ containing a slip-wall wedge that starts
  at $x=0$; post-shock state on the left, supersonic outlet on the
  right; 576,910 triangles, van Leer flux-vector splitting, four-stage
  Runge–Kutta, $\Delta t=2.5\times10^{-5}$, $t=0.2$, 48 density
  contours 2–24. The wedge angle is not stated in the text.
  [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.7 (arXiv v1)
  likewise compute in physical coordinates, as in an earlier work they
  cite: the unstructured polygon with vertices $(-2,0)$, $(0,0)$,
  $(3,\sqrt3)$, $(3,2)$, $(-2,2)$, a ramp of angle $\pi/6$ starting at
  the origin, and a Mach 10 shock along $x$ with
  $(\rho,v_1,v_2,p)=(8,8.25,0,116.5)$ for $x\le0$ and $(\gamma,0,0,1)$
  for $x>0$, $t=0.2$.
- **Relativistic double Mach reflection.**
  [Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.8 (arXiv v1) run
  the special-relativistic version, also without rotation, on the wedge
  domain with vertices $(-0.1,0)$, $(0,0)$, $(2.7,0.9\sqrt2)$,
  $(2.7,2)$, $(-0.1,2)$, $h=1/240$ triangles, $\gamma=1.4$: a shock at
  $x=0$ with speed $0.4984$, post-shock primitive state
  $(\rho,v_1,v_2,p)=(8.564,0.4247,-0.4247,0.3808)$ and pre-shock state
  $(1.4,0,0,0.0025)$, $t=4$. See
  [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
  for the system.
- **Dimensional ramp with an immersed boundary.**
  [Wang et al. (2022a)](/sources/wang-2022.md) §3.4 represent a
  $36^\circ$ ramp by an
  [immersed boundary](/methods/immersed-boundary-method.md) on a
  Cartesian grid: air at 300 K, $p_0=2$ kPa, $\rho_0=0.02312$
  kg m$^{-3}$, $c_0=348.04$ m s$^{-1}$; a Mach 4.5 shock starting at
  $(0,0)$ with post-shock $\rho_s=0.11123$ kg m$^{-3}$ and
  $p_s=46.917$ kPa; domain $[-5,70]\times[0,60]$ mm, $6000\times4800$
  cells ($12.5\,\mu$m), $t=40\,\mu$s, constant inflow on the left,
  slip wall on the bottom, outflow elsewhere; experiment of Ben-Dor &
  Glass for comparison. Their printed post-shock normal velocity is
  discussed under Qualifications.
- **Reflection and diffraction over a backward step.**
  [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Ex. 5.8 and
  [Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.12 run the Mach 10
  oblique shock of the Woodward–Colella data over a wall that ends at
  $x=1$ and drops to $y=-1$, so that the reflected structure then
  diffracts round the corner; Fan, Zhang & Qiu state that the reflection
  part is "exactly the same as" the double Mach reflection, and run it
  for the Navier–Stokes equations at $\mathrm{Re}=1000$ and for Euler.
  The problem is recorded on [shock diffraction](/benchmarks/shock-diffraction.md).

## Runs in the sources

| Source | Scheme family | Domain / grid | Notes |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.5.1 | [very-high-order TENO](/methods/adaptive-teno.md) (TENO8-AA, TENO10-AA) vs [WENO-CU6](/methods/weno-cu6.md) | $[0,4]\times[0,1]$; TENO $512\times128$, $800\times200$; WENO-CU6 $512\times128$, $1024\times256$ | 43 density contours 1.887–20.9 |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.6 | [TENO-THINC](/methods/teno-thinc.md) vs WENO5-Z, TENO5, TENO6 | $512\times128$, $1024\times256$ | cost table; CFL and $\epsilon$ sensitivity |
| [Ye et al. (2022)](/sources/ye-2022.md) §4.8 | [AFTENO](/methods/afteno.md) and AFWENO | $1024\times256$ ($h=1/256$) | zoom $[2,3]\times[0,0.8]$ |
| [Fu (2023)](/sources/fu-2023.md) Figs. 8, 11 | TENO review, reproduced figures | $512\times128$; TENO6 on 151,850 / 369,794 / 752,708 triangles | 43 contours 1.887–20.9, zoom $x\in[2,3]$ |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.3 | [WENO-Z+M](/methods/weno-z-plus.md) vs WENO-Z, WENO-Z+, WENO-IS-I, WENO-Z9 | $961\times241$ | CFL 0.1 for all runs; setup referred to its ref. [17]; 50 contours 2–22 |
| [Deng (2023)](/sources/deng-2023.md) App. A.11 | [ROUND](/methods/round-scheme.md) | $[0,3]\times[0,1]$, $h=1/300$ | tests second contact and roll-up |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.7 | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md), WENO5-JS | $\Delta x=\Delta y=1/400$ | HLL solver "to mitigate carbuncle"; 30 contours 1.4–22.4 |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) Example 4 | [A-WENO](/methods/alternative-weno.md) with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) | $\Delta x=\Delta y=1/480$ | NEW vs OLD flux |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.17 | [OEDG](/methods/oedg.md), $\mathbb P^3$ | $h=1/240$ | no positivity limiter mentioned |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §IX.h | [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md), seventh order, HLL-based (Fig. 18 caption) | $[0,4]\times[0,1]$ (plotted $[0,3]\times[0,1]$), $1920\times480$ | CFL 0.4; fifth order "similar" |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.9 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md), sixth order, HLLC, modified first moments (HWENO6-M5-I) | $[0,4]\times[0,1]$, $1600\times400$ | CFL 0.6; 30 contours 1.5–22.7 |
| [Pazner (2021)](/sources/pazner-2021.md) §5.7 | sparse IDP DG, $N=3$, subcell [convex limiting](/methods/convex-limiting.md) | $[0,4]\times[0,1]$, $2400\times600$ elements | $t=0.275$ (caption); 30 equispaced contours |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.7 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR) vs WENO-JS5, WENO-AO5 | $[0,3]\times[0,1]$, $1200\times400$ | CFL 0.6 |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.6 | [WENO3-NN](/methods/learned-weno-weights.md) vs WENO3-JS, WENO3-Z, WENO3-N, WENO5-JS; finite volume, LLF, characteristic | $1024\times256$ | plotted $[2,3]\times[0,1]$, 40 contours 1.85–21.5; cost test (3700 steps) |
| [Hiejima (2022)](/sources/hiejima-2022.md) §3.4 | [WCNS](/methods/weighted-compact-nonlinear-scheme.md) with JS weights (WCNS-JS) and TENO-type weights (WCNS-T), interpolation orders 5–11, AUSMDV, RK4 at CFL 0.8 | $1024\times256\times5$, $2048\times512\times5$ (three-dimensional code) | 43 contours 1.887–20.9; zoom $2\le x\le3$ |
| [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.4 | flux reconstruction, $\mathbb P_3$, with [entropy filtering](/methods/entropy-filtering.md) (arXiv v3) | $[0,4]\times[0,1]$, $2400\times600$ elements | HLLC |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Exs. 4.3, 4.9 | RKDG $P^1$, $P^2$ with the improved [simple WENO limiter](/methods/weno-limiter-dg.md) vs the original one | triangles $h=1/200$; point clouds of 400,000 ($P^1$) and 800,000 ($P^2$) points | KXRCF threshold $C_k=0.01$; 30 contours 1.1–22 (triangles), 29 contours 1.3–23 (point clouds) |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.4 | nodal DG on triangles with ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md), $P^2$–$P^4$ | $[0,4]\times[0,1]$, $h=1/204$ | fixed-DOF comparison $P^2$ (1,259,712 DOFs) vs $P^4$ (1,248,480 DOFs) |
| [Chen et al. (2022)](/sources/chen-2022.md) §6.5 | second-order cell-centred FV with [vertex-based gradient reconstruction](/methods/unstructured-gradient-reconstruction.md) (VWLSQ with nonlinear weighting) vs WLSQ with the MLP-pw limiter | wedge, 576,910 triangles | variant above |
| [Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.8 | third-order FV WENO on triangles, physical-constraint-preserving limiter, HLL | wedge, $h=1/240$ | relativistic variant above |
| [Wang et al. (2022a)](/sources/wang-2022.md) §3.4 | ghost-cell [immersed boundary](/methods/immersed-boundary-method.md) (baseline, BCGCM, HBCGCM) vs a cut-cell method, MUSCL–Hancock | $6000\times4800$; error study on $1500\times1200$ | dimensional variant above |
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.6 | TENO-M6/M8 ([TENO](/methods/targeted-eno.md) with stencil extension) vs TENO6/8, WENO-JS, [WENO-CU6](/methods/weno-cu6.md), WENO7, WENO9; van Leer flux | $960\times240$ | zoom $[2,3]\times[0,1]$; cost table |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.6 | five-point TENO with a new [scale sensor](/definitions/scale-sensor.md) vs [TENO5-A](/methods/adaptive-teno.md), TENO5, WENO5-Z | $1024\times256$; timing at $512\times128$ | 43 contours 1.887–20.9 (arXiv v1) |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.5 | [TENO-THINC](/methods/teno-thinc.md)-family scheme vs TENO5-THINC, TENO5, TENO6, TENO8, WENO5-Z | $360\times90$, $512\times128$, $1024\times256$ | CFL 0.2, 0.4, 0.6 at $512\times128$; 43 contours 1.887–20.9 |
| [Li, Chen & Ren (2022)](/sources/li-2022.md) §4.3.1 | MDAD-HY ([MDCD](/methods/mdcd-scheme.md)-type hybrid with adaptive dissipation) vs MDCD-HY, TENO-HY | $800\times200$ | detector maps |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.5 | scale-invariant multi-resolution [A-WENO](/methods/alternative-weno.md) (MR-AWENO-Si) vs MR-AWENO | $1600\times400$ | TVD-RK3, CFL 0.45 |
| [Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.8 | finite-difference [Hermite WENO](/methods/hermite-weno.md) HWENO-R vs HWENO-L, WENO-ZQ | $1600\times400$ | 30 contours 1.5–22.7 |
| [Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.8 | unstructured finite-volume TENO3–6 vs WENO5/6 and [CWENO](/methods/cweno.md)5/6, HLL | 151,850, 369,794 ($h\approx1/200$), 752,708 ($h\approx1/280$) triangles | 43 contours 1.887–20.9; cost table (preprint) |
| [Lesur et al. (2023)](/sources/lesur-2023.md) §4.1 | [IDEFIX](/software/idefix.md), second-order Godunov: RK2 + linear + HLL or HLLC; RK3 + LimO3 + HLLC; RK3 + PPM + Roe | $1920\times480$ | data not printed (arXiv v1) |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.5 | six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS-SA vs WCNS-LD and ONL6; HLLC with Xie et al.'s pressure control against shock instability, TVD-RK3, CFL 0.5 | $[0,4]\times[0,1]$, $960\times240$ | post-shock bottom for $x<1/6$, reflective beyond, time-dependent top; $t=0.2$ |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.4 | [gradient-based reconstruction](/methods/gradient-based-reconstruction.md) with [MP limiter](/methods/monotonicity-preserving-limiter.md) (MEG6, MIG4) vs TENO5; HLLC, CFL 0.2 | $[0,3]\times[0,1]$, $768\times256$ | arXiv v2 |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.8 | seventh-order gradient-based MEG7 (conservative and primitive variables) vs seventh-order mapped explicit [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS7M; shock-stable HLLC | $[0,4]\times[0,1]$, $1024\times256$ | reference HOUCS6 on about $4096\times1024$; cost table (arXiv v1) |
| [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) §8.1.3 | MEG6, MIG4 on generalized curvilinear grids with [free-stream-preserving](/properties/free-stream-preservation.md) metrics vs non-preserving metrics; WENO-Z on a uniform grid | $[0,3]\times[0,1]$, $768\times256$, interior nodes displaced randomly by up to 50 % of the spacing | OpenACC GPU timing case, 3 M cells (arXiv v1) |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 15 | fifth-order FV IMWENO-P (mirror-symmetric smoothness indicators) vs WENO-JS, WENO-Z, WENO-NS, WENO-P, MWENO-P; global LF, SSP-RK3, CFL 0.5 | $[0,4]\times[0,1]$, $1440\times360$ | zoom around the Mach stems |
| [Wang et al. (2023c)](/sources/wang-2023-c.md) Example 4.5 | hybrid multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md) vs MR-WCNS and WENO-JS; LF flux, TVD-RK3, CFL 0.6 | $[0,4]\times[0,1]$, plotted $[0,3]\times[0,1]$, $960\times240$ | 30 contours 1.5–22.7; marked-point map |
| [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) §8.4 | entropy-stable [DGSEM](/methods/dgsem.md), $N=3$, elementwise blending with a sparse low-order positivity-preserving scheme, bound relaxation $\zeta_{\mathrm r}=0.1$ (their $\zeta$; with and without shock-capturing blending) and $\zeta_{\mathrm r}=0.5$ | $[0,3.5]\times[0,1]$, $875\times250$ quadrilaterals | $\mathrm{Re}=\infty$ (arXiv v2) |
| [Maltsev et al. (2023)](/sources/maltsev-2023.md) §3.4 | hybrid DG($P_3$)–FV(CWENOZ4) in [UCNS3D](/software/ucns3d.md), a priori [troubled-cell](/definitions/troubled-cell-indicator.md) switch: shock detector, MOOD$^{\mathrm O}$, MOOD$^{\mathrm R}$, extended bounds; CFL 0.5 | about 150,000 triangles, $h=1/125$ | — |
| [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.6 | [$p$-adaptive DG](/methods/hp-adaptation.md) $N\in[2,5]$ with [FV subcells](/methods/subcell-finite-volume-limiting.md) ($N_{\mathrm{FV}}=6$ or 11) vs static $N=5$; HLLE; [FLEXI](/software/flexi.md) | $240\times60\times1$ elements ($h=1/60$), periodic in $z$ | $t=0.28$; pressure indicator |
| [Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.5 | unstructured finite-volume TENO4-D–TENO7-D (dual stencil selection) vs [CWENO](/methods/cweno.md)6/7, HLL, SSP-RK3 at CFL 0.4; [UCNS3D](/software/ucns3d.md) | 151,850 ($h\approx1/125$), 369,794 ($h\approx1/200$), 752,708 ($h\approx1/280$) triangles | 43 contours of $\ln\rho$ in $[1,3]$; cost table |
| [Tang (2024)](/sources/tang-2024.md) §4.4.4 | [TENO-AZ](/methods/adaptive-teno.md) (adaptive cut-off) vs TENO-Z, TENO-A, TENO-LAD; finite difference, global LF splitting, TVD-RK3 at CFL 0.5 | $960\times240$ | 30 contours in $[2,20]$; cost table |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.8 | finite-volume ALW-MR-WENO-3/4/5 on triangles (two stencils, adaptive linear weights) vs [MR-WENO](/methods/multi-resolution-weno.md); characteristic-wise, CFL 0.6 | $[0,4]\times[0,1]$, 708,576 triangles (392,693 points), boundary mesh size 1/320 | 30 contours 1.5–21.5; Mach-stem close-up; cost table |
| [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) Ex. 3.9 | ghost multi-resolution GMR-WENO3/5/7, finite difference and finite volume, vs MR-WENO | $[0,3]\times[0,1]$, $1200\times400$ | 30 contours 1.5–22.7; cost table |
| [Zuo & Zhu (2024a)](/sources/zuo-2024.md) Ex. 3.6 | [hybrid](/methods/hybrid-weno.md) MMR-WENO5/7/9 (MR-WENO in troubled cells, linear upwind elsewhere) vs MR-WENO; CFL 0.6, TVD-RK3 | $[0,4]\times[0,1]$, plotted $[0,3]\times[0,1]$ "on $1200\times400$ grid points" | 30 contours 1.5–22.7; troubled-cell map; cost table |
| [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) Ex. 3.5 | hybrid HMR-WENO5/7/9 (bisection-based extremum indicator) vs MR-WENO; CFL 0.6, TVD-RK3 | $[0,4]\times[0,1]$, $1200\times400$, plotted $[0,3]\times[0,1]$ | 30 contours 1.5–22.7; troubled-cell map; cost table |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.7 | quasi-conservative [ADER](/methods/ader-scheme.md)-DG in primitive variables with a posteriori [subcell FV limiter](/methods/mood-a-posteriori-limiting.md), conservative correction in shock cells, $P_2$ | physical-frame wedge, polygonal mesh $h=1/220$ | variant above (arXiv v1) |

## What the benchmark measures

**Slip-line roll-up as a dissipation gauge.** Every source uses the
roll-up of the primary slip line and the mushroom structure of the wall
jet as the visual measure of resolution. Fu (2021) reports that TENO8-AA
and TENO10-AA at $512\times128$ resolve "much more small-scale vortical
structures than WENO-CU6 with a resolution of $1024\times256$" and calls
the result the best among low-dissipation schemes at similar
resolutions (§5.5.1, Figs. 7–8). Ye et al. find AFWENO-JS the most and
AFTENO the least dissipative, with AFTENO at $h=1/256$ "very close" to
fifth-order WENO-JS at $h=1/960$ and ninth-order WENO-JS at $h=1/480$
from earlier literature (§4.8, Fig. 9). Takagi et al. and Fu (2023)
(Fig. 8) show TENO-THINC sharpening the slip line over WENO5-Z, TENO5
and TENO6 at $512\times128$. Wang et al. (2023b) find the new
adaptive-diffusion flux resolves the wall-jet roll-up, the triple point
and the slip-line instabilities "much better" (Figs. 3–4). Huang et al.
find WENO3-NN, WENO5-JS and ROUND comparable and LD-ROUND richer
(Fig. 12); Bezgin et al. likewise find WENO3-NN resolving finer
structures than WENO3-JS, WENO3-Z and WENO3-N and close to WENO5-JS
(§4.6, Fig. 14). Deng reports that ROUND resolves the second contact on
$h=1/300$, "comparable and even better" than WENO-JS5 on a coarser mesh
(Figs. 25, 36). Balsara et al. resolve Mach-stem instabilities at seventh
order on $1920\times480$ (Fig. 18). Pazner reads the Kelvin–Helmholtz
roll-ups near the triple point of the author's $N=3$ DG run as a sign of low
dissipation (Fig. 13); Dzanic & Witherden find sub-element shock
resolution with the roll-up kept, the filter acting mainly at the shock
fronts (Fig. 4). Wang et al. (2021) find both multi-resolution
schemes resolving the roll-up better than WENO-JS5 (Fig. 5.13).

The TENO family of the newer sources agrees in kind. Hong, Ye & Ye find
TENO and TENO-M resolving the slip-line structures equally well, far
better than the WENO schemes, with WENO9 oscillating near the Mach stem
(§5.6, Fig. 14). Liang et al. call their scheme "significantly better"
than WENO5-Z, TENO5 and TENO5-THINC at $360\times90$ and $512\times128$,
"and even better than" TENO6 and TENO8, and state that it
"substantially outperforms all other schemes in the literature" around
the Mach stems and the wall jet, a claim resting on contour plots
(Figs. 11–12); at $1024\times256$ it suppresses small disturbances that
TENO5-THINC produces near the oblique shock (Figs. 13–14), and the
result is "not very sensitive" to CFL 0.2–0.6 (Fig. 15). Huang, Liang &
Fu find TENO5 better than WENO5-Z, both excessively dissipative, and
their scale-sensor scheme resolving the richest structures in
$[2,3]\times[0,0.9]$ with much less noise behind the incident shock
than TENO5-A (§4.6, Figs. 9–10). Li, Chen & Ren find MDAD-HY giving the
finest slip-line structures, its detector flagging only vortex edges,
not their interiors, unlike MDCD-HY and TENO-HY (§4.3.1, Figs. 19–20).
Li, Li, Don & Wang find the large structures alike and the slip-line
small scales "much better resolved" by the scale-invariant scheme
(§3.5, Fig. 7). Ji, Liang & Fu rank equal-order schemes on triangles:
TENO least dissipative, then WENO, then CWENO, with more small scales
at higher order and no spurious oscillations (§5.8, Figs. 21–25); by
reference to other papers' figures they state that TENO5 captures the
Mach-stem roll-up better than WENO5-AO at twice its mesh size and at
$h\approx1/200$ matches multi-resolution WENO5 at $h\approx1/320$.
Lesur et al. use the problem to show the sensitivity of the wall jet to
the dissipation of a second-order code: LimO3 and PPM, its least
diffusive options, give a more vigorous jet with the beginning of
Kelvin–Helmholtz rolls (§4.1, Fig. 3).

The gradient-based schemes of the Chamarthi papers are ranked the same
way. Chamarthi (2023a) finds MIG4 resolving the slip-line roll-ups
better than MEG6 and TENO5, and TENO5 oscillating near the Mach stem
(Fig. 7). In Chamarthi (2023b) MEG7 with conservative variables
resolves the slip-line vortices better than WCNS7M, while MEG7 with
primitive variables shows no slip-line vortices but a better-resolved
wall jet, primitive reconstruction being "slightly more dissipative"
here (Fig. 11). Chandravamsi et al. find WENO-Z resolving the shear
layer less well than MEG6 and MIG4 on the uniform grid (Fig. 9f).
Zhou et al. find WCNS-SA giving clearer vortex cores along the slip
line than WCNS-LD and ONL6, similar to the hybrid weighted compact
scheme CCSSR-HW6 of their ref. [40] on $1920\times480$ (§5.5, Fig. 15).

Zhong et al. find the global structure alike for all six fifth-order
schemes and rank them by the small vortices along the slip line:
WENO-JS the most dissipative, then WENO-Z, while IMWENO-P, WENO-NS,
WENO-P and MWENO-P capture more vortices, IMWENO-P with the highest
resolution (Fig. 20). Wang et al. (2023c) find both multi-resolution
WCNS schemes better than WENO-JS on the same grid in the zoom around the
Mach stems, and their hybrid switch marks the shock structures
(Figs. 4.7–4.8); their hybrid costs 0.87 of WENO-JS's CPU time here,
the original MR-WCNS 1.92 (Table 5.1).

The unstructured TENO and adaptive-TENO sources of chunk 7 read the
figure the same way. Ji, Liang & Fu (2023) find that higher-order TENO-D
resolves more small scales in the blow-up region while keeping the
shocks sharp, and that at equal order TENO-D shows "much lower
numerical dissipation" than CWENO (§4.5, Figs. 9–14); by reference to a
figure of another paper they call TENO-D at $h\approx1/200$
"significantly better" than fifth-order WENO-AO at $h\approx1/400$.
Tang finds that the adaptive-cut-off TENO-AZ resolves finer vortices
than TENO-Z and TENO-LAD, while TENO-A gives more vortices but
significantly more noise (§4.4.4). Gaburro et al.'s primitive-variable
ADER-DG uses the conservative update only in the shock-triggered
subcells, so most of the domain stays in primitive variables, and the
small-scale roll-up of the shear layer is visible at $P_2$ on
$h=1/220$ (§5.1.7, Fig. 6; see
[local conservation](/results/local-conservation-flux-form.md)).

The multi-resolution WENO papers of the Zhu group compare new
schemes with MR-WENO of the same order and find them alike or better.
Lin & Zhu's two-stencil ALW-MR-WENO on triangles and MR-WENO "can
provide good resolution" and give similar results (Case 3.8, Figs.
3.11–3.14). Zhang & Zhu state that GMR-WENO "resolve two Mach stems well
than" MR-WENO on $1200\times400$ (Ex. 3.9, Figs. 3.16–3.17). Zuo & Zhu's (2024a, 2024b)
hybrids show "more sophisticated flow structures" in the blow-up around
the Mach stems than MR-WENO (2024a, Ex. 3.6, Figs. 3.8–3.9; 2024b,
Ex. 3.5, Figs. 3.6–3.7), and in 2024a the MMR-WENO indicator is called
"more accurate than" the SHUS-WENO indicator of Wang et al. in
identifying the flow features, judged from troubled-cell maps (Fig.
3.10). All four judgements are visual.

**Order does not buy roll-up by itself.** Hiejima's WCNS-JS shows no
Kelvin–Helmholtz roll-up along the slip line at fifth order, and its
seventh, ninth and eleventh orders look like its fifth; WCNS-T shows
ripples at fifth order, a wavy slip line with small scales in the
rolled-up vortex at seventh and more waves at ninth order, and at
$2048\times512$ the small scales grow with order up to the end of the
wall jet (§3.4, Figs. 7–9). At eleventh order on $1024\times256$ the
slip line shows no waves, which Hiejima attributes, with a "probably",
to the first-order interpolation the code falls back to where reconstructed density or
pressure turn negative. Yu & Hesthaven find the roll-up more noticeable
at higher DG degree on one mesh, but at comparable degrees of freedom
($P^2$ against $P^4$) the shock thickness is comparable and the contacts
are slightly sharper for $P^2$ (§5.4.4, Figs. 18–20). The meshes of
that comparison are not printed; on uniform quadrilaterals split into
two triangles the DOF counts correspond to $h=1/162$ for $P^2$ and
$h=1/102$ for $P^4$ *(compiler check, not in the sources)*. For the
immersed-boundary variant, Wang et al. (2022) recall that the numerical
scheme is "generally thought" to influence the roll-up more than the
boundary treatment; on $6000\times4800$ their four boundary methods put
the discontinuities in the same place and differ in the wall jet, where
the improved ghost-cell method produces smaller-scale vortices and a
smoother field than the cut-cell method (§3.4, Figs. 14–15).

**Robustness and stability margin.** The strong shock is also a
robustness test. Luo & Wu must lower the CFL number to 0.1 for every
scheme because their ninth-order reference WENO-Z9 does not run at
larger values (§5.3.3). Huang et al. replace HLLC by HLL to avoid the
[carbuncle](/definitions/carbuncle-phenomenon.md) at the Mach stem
(§6.7). Chen et al. (2022) report kinked Mach stems with the weighted
least-squares gradients and the MLP-pw limiter, most strongly with the
vertex stencil, and none with their nonlinear vertex weighting on the
same stencil; since the flux (van Leer) is the same for all runs, they
attribute the kinks to the reconstruction and limiter, not to the flux
(§6.5, Fig. 22). Bezgin et al. see a slightly more pronounced
post-shock instability behind the incident shock with WENO3-NN than
with WENO3-N or WENO5-JS (§4.6). Hiejima needs a first-order fallback
where interpolated $\rho$ or $p$ is negative, "due to the difficulty of
calculating this problem using a high-order accuracy interpolation due
to the strong shock wave" (§3.4). Peng et al. run third- and
fourth-order OEDG without any
positivity limiter being mentioned; they say only that their results
agree with earlier computations. Li, Shu & Qiu report that the
unmodified sixth-order HWENO "will blow up without modification" on
this problem, and show only the run with modified first moments; they
recall that the original Hermite WENO schemes are "not stable enough"
for it, because the first derivatives grow large near discontinuities
(§1, Ex. 3.9, Fig. 3.7). In the relativistic variant Chen & Wu's
physical-constraint-preserving limiter acts on one or two cells in the
first three steps only (Ex. 4.8). Ji, Liang & Fu report that
equal-order WENO5 and WENO6 on triangles "typically fail" without the
extended-bounds limiter of an earlier work, which they describe as
helping to preserve positivity, whereas TENO and CWENO run at all three
resolutions (§5.8, Figs. 24–25); they also state that CWENO with a large
central linear weight "typically fails" here, which fixes their choice
of that weight (§2.4).

**Positivity-only limiting of entropy-stable DG.** Lin, Chan & Tomas
run the problem robustly with elementwise blending that enforces only
positivity of density and internal energy, not local bounds or a
minimum entropy principle; the fine-scale vortical structure is
resolved, which "suggests that the proposed limiting strategy does not
introduce excessive numerical dissipation" (Fig. 9), while oscillations
remain near the shocks and are reduced by the larger relaxation factor
$\zeta_{\mathrm r}=0.5$ or by adding the shock-capturing blending (Figs. 10–11); see
[convex limiting](/methods/convex-limiting.md) and
[entropy stability](/properties/entropy-stability.md).

**Switch sensitivity in hybrid DG–FV.** Maltsev et al. find that only
the less sensitive MOOD$^{\mathrm R}$ switch resolves the slipstream
roll-up; the shock detector and MOOD$^{\mathrm O}$ flag larger regions
and diffuse it. A curved Mach stem appears with every indicator, which
they attribute to the [carbuncle](/definitions/carbuncle-phenomenon.md)
sensitivity of the flux and to shock–grid misalignment on triangles;
reconstructing primitive instead of conserved variables reduces it,
shown for the shock detector (§3.4, Figs. 10–11).

**Distorted curvilinear grids.** Chandravamsi et al. run the problem
on a $768\times256$ grid whose interior nodes are displaced randomly by
up to 50 % of the spacing (maximum included angle close to $200^\circ$).
With free-stream-preserving metrics the solution is unaffected by the
distortion; with non-preserving metrics rough patches appear, smaller
for MIG4 than for MEG6 (§8.1.3, Fig. 9).

**Limiters on unstructured meshes.** Du et al. find the improved
simple WENO limiter as good as the original at $P^1$ and better at
$P^2$, with "better control" of oscillations and a better-resolved
double Mach region on triangles (Ex. 4.3, Figs. 4.3–4.4); on point
clouds the $P^2$ Mach stem is better resolved with the improved limiter,
and they state that the original limiter needed $1{,}664{,}000$ points
in their earlier work for the resolution they reach with $800{,}000$
(Ex. 4.9, Figs. 4.14–4.15).

**$p$-adaptation.** Mossier, Beck & Munz run their $p$-adaptive DG
with FV subcells at a mean of 35 (adaptive) and 54 (hp, with refined
subcells) degrees of freedom per element against 216 for static $N=5$,
with wall times of 15,578, 3856 and 6569 s, speedups of about 4 and
2.4, memory 4.9, 5.9 and 19.0 GB, and 4695, 4726 and 4765 time steps,
so the larger subcell count $N_{\mathrm{FV}}=2N+1$ does not shrink the
step (§8.6, Table 3). The ratios $15{,}578/3856=4.04$ and
$15{,}578/6569=2.37$ match their "a factor 4" and "almost a factor 2.5"
*(compiler check, not in the sources)*.

**Cost.** Takagi et al. report cost per step (Table 3, hardware not
stated): WENO5-Z 696 / 2802 ms, TENO5 810 / 3255 ms, TENO-THINC 946 /
3810 ms, TENO6 867 / 3330 ms at $512\times128$ / $1024\times256$, i.e.
TENO-THINC costs 16.8 % (17.1 %) more than TENO5. Bezgin et al. time
the $1024\times256$ run for 3700 steps in JAX on a GPU, in ns per cell
and step: WENO3-JS 389, WENO3-Z 396, WENO3-N 411, WENO3-NN1 1676 (4.31
times WENO3-JS), WENO3-NN2 1743 (4.48 times), WENO5-JS 561 (1.44 times),
with unoptimized networks (§4.9, Table 2). Du et al. measure the CPU
time saved by the improved limiter: 12.34 % ($P^1$) and 17.88 %
($P^2$) on triangles (Table 4.7), 36.11 % and 54.92 % on point clouds,
the latter with 10 and 30 MPI processes respectively (Table 4.17).
Hong, Ye & Ye time 1000 steps on $960\times240$ (Fortran, Intel Core
i9-10980XE): TENO6 1747.42 s, TENO-M6 1406.65 s, WENO-JS 1252.31 s,
WENO-CU6 1489.53 s, TENO8 2277.26 s, TENO-M8 1588.62 s, WENO7 1398.94 s,
WENO9 1577.73 s (Table 4). They recall from an earlier TENO paper that
the eight-point TENO took "nearly 70%" more time than WENO-CU6 on a
$1024\times256$ run; their own table gives $2277.26/1489.53=1.53$,
about 53 % *(compiler check, not in the sources)*, with different codes,
grids and hardware. Ji, Liang & Fu report a reconstruction time per
iteration and element rising from $1.36\times10^{-6}$ s (TENO3) to
$2.24\times10^{-6}$ s (TENO6) on 369,794 triangles, "roughly 65%", with
TENO5 and CWENO5 at $1.96$ and $1.98\times10^{-6}$ s (Intel Xeon
E5-2690, 8 MPI ranks × 7 OpenMP threads; §5.10, Table 7).

Ji, Liang & Fu (2023) time the $h\approx1/125$ run at 2517.38 s
(CWENO6), 3050.80 s (CWENO7), 2694.45 s (TENO6-D) and 3126.84 s
(TENO7-D), "approximately the same", hardware not stated (Table 7); the
TENO-D/CWENO ratios are 1.070 and 1.025 here against 0.949 and 0.932 on
their Shu–Osher run *(compiler check, not in the sources)*. Tang
times one step at $t=\mathrm{CFL}\cdot\Delta x$, averaged over 100 runs
on an Intel i7-9700, over seven two-dimensional problems including
this one: TENO-AZ costs 0.98–1.01 of TENO-Z, TENO-A 1.33–1.44 and
TENO-LAD 1.11–1.18 (Table 6).

Chamarthi (2023b, Table 2) times the $1024\times256$ run at 1806 s
(MEG7-prim), 1946 s (MEG7-cons) and 2493 s (WCNS7M), hardware not
stated. Chandravamsi et al. time it on one GPU against one Xeon Gold
5115 core: MEG6 speedups of 57.5, 100.4 and 153.14 on an A6000, a V100
and an A100 (Table 5); on this inviscid case WENO-Z is the fastest of
their three schemes because it needs no gradients (§9.1).

The Zhu-group papers all report savings against MR-WENO. Lin & Zhu
(Table 3.1, hardware not stated): 660330.33 s for MR-WENO-4 against
611079.93 s for ALW-MR-WENO-4, and 713307.99 s against 451954.05 s at
fifth order. Zhang & Zhu (Table 3.1, Intel Core i5-8265U, Visual
Fortran): 22286.90 s for MR-WENO7-FD against 10285.53 s for GMR-WENO7-FD
(1:2.17) and 115220.18 s against 71880.31 s in finite volumes (1:1.60).
Zuo & Zhu (2024a, Table 3.1, hardware not stated): MMR/MR time ratios
31.1 %, 28.4 % and 24.9 % at orders 5, 7, 9. Zuo & Zhu (2024b, Table
3.1, a Lenovo XiaoXinAir 14 laptop): MR-WENO 9509.17, 17058.2 and
26535.5 s against HMR-WENO 3088.51, 5905.18 and 11658.7 s.

**Unstructured meshes.** Fu (2023) reproduces finite-volume TENO6 on
triangular meshes of 151,850 to 752,708 cells (Fig. 11). Chen et al.
(2022), Chen & Wu (2022), Du et al., Yu & Hesthaven, Maltsev et al. and
Lin & Zhu also compute on triangles, and Du et al. on polygonal cells built from point clouds.

**Error norms.** Wang et al. (2022) are the only source that measures
an error: density errors on $1500\times1200$ against the baseline
ghost-cell solution on $6000\times4800$, with the hybrid ghost-cell
method lowest of four in all norms ($L^1$ error total /
boundary region $2.3\times10^{-4}$ / $5.0\times10^{-4}$, against
$4.2\times10^{-4}$ / $2.1\times10^{-3}$ for the cut-cell method;
§3.4, Table 2). The reference is one of the compared methods on a finer
grid, not an exact solution.

## Qualifications

- The roll-up criterion is qualitative. Except for Wang et al.
  (2022), no source gives an error
  norm; claims of superiority rest on contour plots, often against
  figures of other papers (Fu 2021 compares with
  figures of another work; Ye et al. with literature grids; Deng's
  comparison cites a WENO-JS5 result "in [65]", a reference on an
  improved third-order WENO-Z scheme).
- Fu (2023) prints "$t=2.0$" in the caption of Fig. 8, and Takagi et
  al. print "$t=2.0$" in the caption of Fig. 10 while their §4.6 text
  says $t=0.2$; the final time of the problem is $0.2$ in every source
  that states it in the text.
- Liang et al. print "$t=2.0$" in the captions of Figs. 11–14 while
  their §4.5 text says $t=0.2$, the same caption slip as Fu (2023) and
  Takagi et al.; Ji, Liang & Fu time their run "at $t=2$" (§5.10)
  against the $t=0.2$ of their §5.8.
- Chamarthi (2023a) applies the reflecting wall on
  "$0.1667<x\le4.0$" of a domain $[0,3]\times[0,1]$ (arXiv v2).
- Chamarthi (2023a) finds TENO5 oscillating near the Mach stem, as the author's
  text says WENO figures of the literature do; the TENO sources above
  report no such oscillation for their TENO5 runs. The runs differ in
  reconstructed variables (primitive in Chamarthi), flux and grid, and
  no source compares them, so this is recorded as a difference of
  findings, not as a contradiction.
- Mossier, Beck & Munz stop at $t=0.28$, like Pazner a later stage of
  the roll-up.
- Deng; Wang et al. (2021); Chamarthi (2023a), Chandravamsi et al. and
  Zhang & Zhu compute on $[0,3]\times[0,1]$, Lin, Chan & Tomas on
  $[0,3.5]\times[0,1]$, the others on $[0,4]\times[0,1]$ (Balsara et al.
  and Wang et al. (2023c) compute on $[0,4]$ and plot $[0,3]$).
- Pazner's Fig. 13 caption gives $t=0.275$, later than the $t=0.2$ of
  the other sources; the run is therefore at a later stage of the
  roll-up.
- Hiejima's text calls condition (A) the post-shock state and imposes
  "post-shock condition (A)" at the inflow and on $0\le x\le1/6$ of the
  bottom, but Eq. (29) gives (A) the values $(1.4,0,0,0,1.0)$, the gas
  at rest ahead of the shock, and (B) the compressed state
  $(8.0,\dots,116.5)$. The values are the Woodward–Colella ones: the
  state $(1.4,1)$ has sound speed 1, consistent with the
  upper-boundary speed $10/\sin\theta$ of a Mach 10 shock, and the
  Rankine–Hugoniot relations map it to $(8,8.25,116.5)$ (see Setup)
  *(compiler check, not in the sources)*. The labels (A)/(B) in the
  text and in Fig. 6 are swapped against Eq. (29).
- Dzanic & Witherden print "no-slip adiabatic wall" conditions on the
  bottom for $x\ge1/6$ in an inviscid computation (§5.1.4); a no-slip
  condition cannot be imposed on the Euler equations, and the paper
  itself replaces no-slip by slip for the hyperbolic step (§4.1). The
  reflecting wall of the other sources is what the setup requires.
- Wang et al. (2022) print the post-shock normal velocity as
  $u_{n,s}=1566.2$ m s$^{-1}$. With their $c_0=348.04$ m s$^{-1}$,
  $4.5\,c_0=1566.2$ m s$^{-1}$ is the shock speed; the Rankine–Hugoniot
  gas velocity behind a Mach 4.5 shock is
  $\frac{2c_0}{\gamma+1}\big(M-\frac1M\big)\approx1240.7$ m s$^{-1}$,
  while their density ratio $0.11123/0.02312=4.811$ and pressure ratio
  $46.917/2=23.458$ agree with the Rankine–Hugoniot values $4.812$ and $23.458$
  *(compiler check, not in the sources)*. Only the printed velocity is
  inconsistent; which value the code used cannot be read from the paper.
- Chen & Wu's relativistic post-shock state has $v_2=-0.4247$ for a
  shock at $x=0$ moving in $+x$. With $\gamma=1.4$, the state
  $(8.564,0.4247,0,0.3808)$ satisfies the relativistic
  Rankine–Hugoniot conditions against $(1.4,0,0,0.0025)$ at shock speed
  $0.4984$ to the four printed digits (residuals below $10^{-3}$),
  whereas the printed state with $v_2=-0.4247$ leaves residuals of
  order $10^{-1}$ *(compiler check, not in the sources)*. The
  $v_2$ entry is therefore inconsistent with the stated shock; the
  paper's figure cannot decide which data were run.
- Zuo & Zhu (2024a) state the domain $[0,4]\times[0,1]$ and show
  contours of $[0,3]\times[0,1]$ "on $1200\times400$ grid points",
  without saying whether the 1200 points cover $[0,4]$ (spacings $1/300$
  and $1/400$) or $[0,3]$. Both Zuo & Zhu papers (2024a, 2024b) defer the setup to the
  literature, as does Lin & Zhu's Case 3.8 apart from the geometry.
- Yu & Hesthaven print no initial states; their run is listed as a
  Woodward–Colella run on their own citation of the setup.
- Tang's states are conservative variables printed under a primitive
  heading (see Setup), and the caption of Tang's Fig. 13 reads "implosion
  problem" while §4.4.4 uses Fig. 13 for this run.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.5.1, Figs. 7–8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.6, Table 3, Fig. 10.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.8, Eq. (48), Fig. 9.
- [Fu (2023)](/sources/fu-2023.md) — Figs. 8 and 11 (reproduced).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.3, Fig. 15.
- [Deng (2023)](/sources/deng-2023.md) — App. A.11, Figs. 25, 36.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.7, Eq. (6.9), Fig. 12.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4, Example 4, Figs. 3–4.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.17, Fig. 13 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.h, Fig. 18.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1; Ex. 3.9, Fig. 3.7 (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.7, Fig. 13 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.7, Fig. 5.13.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.6, Eq. (37), Fig. 14; §4.9, Table 2.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §3.4, Eq. (29), Figs. 6–9.
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.4, Fig. 4 (arXiv v3).
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — Exs. 4.3, 4.9, Figs. 4.2–4.4, 4.13–4.15, Tables 4.7, 4.17.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.4, Figs. 18–20.
- [Chen et al. (2022)](/sources/chen-2022.md) — §6.5, Figs. 21–22.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.8, Fig. 12 (arXiv v1).
- [Wang et al. (2022a)](/sources/wang-2022.md) — §3.4, Table 2, Figs. 14–15.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — Example 5.8, Fig. 5.7.
- [Fan et al. (2023)](/sources/fan-2023.md) — Ex. 3.8; Ex. 3.12.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1; §5.6, Fig. 14; Table 4.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.6, Figs. 9–10 (arXiv v1).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §2.4; §5.8, Figs. 21–25; §5.10, Table 7 (preprint).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.1, Fig. 3 (arXiv v1).
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.3.1, Figs. 19–20.
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §3.5, Fig. 7.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.5, Figs. 11–15.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §8.6, Table 3.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.4, Fig. 7 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.8, Fig. 11, Table 2 (arXiv v1).
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §8.1.3, Fig. 9; §9.1, Table 5 (arXiv v1).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.5, Eq. (40), Fig. 15.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.4, Ex. 15, Eq. (49), Fig. 20.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — Example 4.5, Figs. 4.7–4.8, Table 5.1.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.4, Figs. 9–11 (arXiv v2).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §3.4, Figs. 10–11.
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.5, Eq. (42), Figs. 9–14, Table 7.
- [Tang (2024)](/sources/tang-2024.md) — §4.4.4, Eq. (36), Fig. 13; §4.4.8, Table 6.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.1.7, Fig. 6 (arXiv v1).
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3, Case 3.8, Figs. 3.11–3.14, Table 3.1.
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — §3, Ex. 3.9, Figs. 3.16–3.17, Table 3.1.
- [Zuo & Zhu (2024a)](/sources/zuo-2024.md) — Ex. 3.6, Figs. 3.8–3.10, Table 3.1.
- [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) — Ex. 3.5, Figs. 3.6–3.8, Table 3.1.
