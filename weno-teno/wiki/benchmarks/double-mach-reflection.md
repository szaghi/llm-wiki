---
type: Benchmark
title: "Double Mach reflection"
description: "Two-dimensional Euler benchmark in which a Mach 10 shock at 60° to a reflecting wall forms a double Mach stem, slip line and wall jet; used to rank the numerical dissipation of shock-capturing schemes by the Kelvin–Helmholtz roll-up along the slip line."
status: established
aliases: [DMR, double Mach reflection of a strong shock, Woodward–Colella double Mach reflection]
tags: [benchmark, low-dissipation, weno, teno, dg]
timestamp: 2026-10-22T00:00:00Z
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
source that runs it. Thirteen sources of the bundle run it; most cite
Woodward & Colella (1984) for it, while Peng, Sun & Wu cite no source
for the setup.

## Setup

Common data, as printed by
[Fu (2021)](/sources/fu-2021.md) §5.5.1,
[Takagi et al. (2022)](/sources/takagi-2022.md) §4.6,
[Ye et al. (2022)](/sources/ye-2022.md) §4.8 and
[Huang et al. (2026)](/sources/huang-2026.md) §6.7, Eq. (6.9), in
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
[Wang et al. 2023](/sources/wang-2023-b.md), Example 4, and
[Balsara et al. 2024](/sources/balsara-2024.md) §IX.h; Peng, Sun & Wu,
Ex. 5.17, write it as post-shock data on $0\le x\le\tfrac16+(1+20t)/\sqrt3$
of the upper boundary). [Pazner (2021)](/sources/pazner-2021.md) §5.7
states the same boundary set: post-shock state on the left and on
$[0,1/6]$ of the bottom, slip wall on $[1/6,4]$, exact shock motion on
the top, outflow on the right, pre-shock $\rho=1.4$, $p=1$.

[Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.17 and
[Wang et al. (2023)](/sources/wang-2023-b.md) Example 4 write the same
geometry as $x<\tfrac16+y/\sqrt3$ with post-shock state
$(8,\ 8.25\cos\tfrac\pi6,\ -8.25\sin\tfrac\pi6,\ 116.5)$. The line
$y=1.732(x-0.1667)$ is the same front to the printed digits, and the
velocity components agree ($8.25\cos30^\circ=7.145$,
$8.25\sin30^\circ=4.125$). The two groups differ in the post-shock
pressure, $116.5$ versus $116.8333$. The Rankine–Hugoniot conditions
for a Mach 10 shock entering $(\rho,p)=(1.4,1)$ with $\gamma=1.4$
(sound speed $c=1$, shock speed $10$) give
$\rho=1.4\cdot\frac{(\gamma+1)M^2}{(\gamma-1)M^2+2}=1.4\cdot\frac{240}{42}=8$,
a post-shock speed $10\,(1-1.4/8)=8.25$ and
$p=1+\tfrac{2\gamma}{\gamma+1}(M^2-1)=1+\tfrac76\cdot99=116.5$
*(compiler check, not in the sources; recomputed 2026-10-21)*, so
$116.5$ is the Rankine–Hugoniot post-shock pressure and $116.8333$ is
$1/3$ (about 0.29 %) higher; Fu (2021), Takagi et al., Ye et al. and
Huang et al. print it without comment. It is a setup difference, not a
contradiction: no source compares the two. The shock's horizontal
speed $10/\sin60^\circ=20/\sqrt3$ matches Peng et al.'s upper-boundary
formula *(compiler check, not in the sources)*.

Wording differs in one more place: Ye et al. call the shock "at 30°"
starting at $x=1/6$ and [Deng (2023)](/sources/deng-2023.md) App. A.11
speak of "a 30° ramp", whereas Fu, Takagi et al., Huang et al., Peng et
al. and [Balsara et al. (2024)](/sources/balsara-2024.md) §IX.h speak of a
$60^\circ$ incidence. The printed data are the same; a shock normal to
the flow meets a $30^\circ$ ramp at $60^\circ$, so the two angles
describe one configuration *(compiler check, not in the sources)*.

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
| [Wang et al. (2023)](/sources/wang-2023-b.md) Example 4 | [A-WENO](/methods/alternative-weno.md) with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) | $\Delta x=\Delta y=1/480$ | NEW vs OLD flux |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.17 | [OEDG](/methods/oedg.md), $\mathbb P^3$ | $h=1/240$ | no positivity limiter mentioned |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §IX.h | [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md), seventh order, HLL-based (Fig. 18 caption) | $[0,4]\times[0,1]$ (plotted $[0,3]\times[0,1]$), $1920\times480$ | CFL 0.4; fifth order "similar" |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.9 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md), sixth order, HLLC, modified first moments (HWENO6-M5-I) | $[0,4]\times[0,1]$, $1600\times400$ | CFL 0.6; 30 contours 1.5–22.7 |
| [Pazner (2021)](/sources/pazner-2021.md) §5.7 | sparse IDP DG, $N=3$, subcell [convex limiting](/methods/convex-limiting.md) | $[0,4]\times[0,1]$, $2400\times600$ elements | $t=0.275$ (caption); 30 equispaced contours |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.7 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR) vs WENO-JS5, WENO-AO5 | $[0,3]\times[0,1]$, $1200\times400$ | CFL 0.6 |

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
and TENO6 at $512\times128$. Wang et al. (2023) find the new
adaptive-diffusion flux resolves the wall-jet roll-up, the triple point
and the slip-line instabilities "much better" (Figs. 3–4). Huang et al.
find WENO3-NN, WENO5-JS and ROUND comparable and LD-ROUND richer
(Fig. 12); Deng reports that ROUND resolves the second contact on
$h=1/300$, "comparable and even better" than WENO-JS5 on a coarser mesh
(Figs. 25, 36). Balsara et al. resolve Mach-stem instabilities at seventh
order on $1920\times480$ (Fig. 18). Pazner reads the Kelvin–Helmholtz
roll-ups near the triple point of his $N=3$ DG run as a sign of low
dissipation (Fig. 13). Wang et al. (2021) find both multi-resolution
schemes resolving the roll-up better than WENO-JS5 (Fig. 5.13).

**Robustness and stability margin.** The strong shock is also a
robustness test. Luo & Wu must lower the CFL number to 0.1 for every
scheme because their ninth-order reference WENO-Z9 does not run at
larger values (§5.3.3). Huang et al. replace HLLC by HLL to avoid the
[carbuncle](/definitions/carbuncle-phenomenon.md) at the Mach stem
(§6.7). Peng et al. run third- and fourth-order OEDG without any
positivity limiter being mentioned; they say only that their results
agree with earlier computations. Li, Shu & Qiu report that the
unmodified sixth-order HWENO "will blow up without modification" on
this problem, and show only the run with modified first moments; they
recall that the original Hermite WENO schemes are "not stable enough"
for it, because the first derivatives grow large near discontinuities
(§1, Ex. 3.9, Fig. 3.7).

**Cost.** Takagi et al. report cost per step (Table 3, hardware not
stated): WENO5-Z 696 / 2802 ms, TENO5 810 / 3255 ms, TENO-THINC 946 /
3810 ms, TENO6 867 / 3330 ms at $512\times128$ / $1024\times256$, i.e.
TENO-THINC costs 16.8 % (17.1 %) more than TENO5.

**Unstructured meshes.** Fu (2023) reproduces finite-volume TENO6 on
triangular meshes of 151,850 to 752,708 cells (Fig. 11).

## Qualifications

- The roll-up criterion is qualitative. No source gives an error
  norm; claims of superiority rest on contour plots, often against
  figures of other papers (Fu 2021 compares with
  figures of another work; Ye et al. with literature grids; Deng's
  comparison cites a WENO-JS5 result "in [65]", a reference on an
  improved third-order WENO-Z scheme).
- Fu (2023) prints "$t=2.0$" in the caption of Fig. 8, and Takagi et
  al. print "$t=2.0$" in the caption of Fig. 10 while their §4.6 text
  says $t=0.2$; the final time of the problem is $0.2$ in every source
  that states it in the text.
- Deng and Wang et al. (2021) compute on $[0,3]\times[0,1]$, the
  others on $[0,4]\times[0,1]$ (Balsara et al. compute on $[0,4]$ and
  plot $[0,3]$).
- Pazner's Fig. 13 caption gives $t=0.275$, later than the $t=0.2$ of
  the other sources; the run is therefore at a later stage of the
  roll-up.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.5.1, Figs. 7–8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.6, Table 3, Fig. 10.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.8, Eq. (48), Fig. 9.
- [Fu (2023)](/sources/fu-2023.md) — Figs. 8 and 11 (reproduced).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.3, Fig. 15.
- [Deng (2023)](/sources/deng-2023.md) — App. A.11, Figs. 25, 36.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.7, Eq. (6.9), Fig. 12.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 4, Figs. 3–4.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.17, Fig. 13 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.h, Fig. 18.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1; Ex. 3.9, Fig. 3.7 (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.7, Fig. 13 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.7, Fig. 5.13.
