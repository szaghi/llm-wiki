---
type: Benchmark
title: "Leblanc shock tube"
description: "One-dimensional Euler Riemann problem with a pressure ratio of 10^9 and a density ratio of 10^3 or 2×10^3, printed in two inequivalent versions under one name; a robustness test of near-vacuum, extreme-ratio shock tubes in which positivity limiters and low dissipation are judged against a fine reference."
status: established
aliases: [LeBlanc problem, Le Blanc shock tube, LeBlanc shock tube]
tags: [benchmark, positivity, bound-preserving, low-dissipation]
timestamp: 2026-10-23T16:00:00Z
---

# Leblanc shock tube

A Riemann problem of the Euler equations whose left state carries a
pressure nine orders of magnitude above the right one, with the right
density about three orders below the left. The solution is a strong
rarefaction to the left and a very strong shock and contact to the
right (the left gas is at rest at the higher pressure); the extreme
ratios make it a robustness test, and resolution is judged visually
against an exact or fine-grid reference. Two inequivalent problems go
by the name.

## Version on $[0,9]$, $\gamma=5/3$

| Source | Left, $x<3$ | Right | Grid | Final time |
|---|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.7.1 | $(\rho,v,p)=(1,\ 0,\ \tfrac23\times10^{-1})$ | $(10^{-3},\ 0,\ \tfrac23\times10^{-10})$ | 800 points; reference WENO5-JS, 4000 | 6 |
| [Deng (2023)](/sources/deng-2023.md) App. A.8 | $(\rho,v,e)=(1,\ 0,\ 0.1)$ | $(0.001,\ 0,\ 10^{-7})$ | 200 cells | 6 |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.10 | $(\rho,v,p)=(1,\ 0,\ \tfrac23\times10^{-1})$ on $0<x<3$ | $(10^{-3},\ 0,\ \tfrac23\times10^{-10})$ on $3<x<9$ | 900 points; exact Riemann solver | 6 |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.3 | same | same | 900 points; exact | 6 |

Deng prints the specific internal energy $e$. With
$p=(\gamma-1)\rho e$ and $\gamma=5/3$, Deng's states are
$p=\tfrac23\times0.1$ and $p=\tfrac23\times0.001\times10^{-7}=\tfrac23\times10^{-10}$,
Fu's states exactly *(compiler check, not in the sources)*. The
pressure ratio is $10^9$ and the density ratio $10^3$.

## Version on $[-10,10]$, $\gamma=1.4$

| Source | Left, $x<0$ | Right | Grid | Final time |
|---|---|---|---|---|
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.5 | $(\rho,v,p)=(2,\ 0,\ 10^9)$ | $(0.001,\ 0,\ 1)$ | 3200 cells, logarithmic plots | $10^{-4}$ |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.5c | same | same | 6400 points | $10^{-4}$ |
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.4 | same, Navier–Stokes $\mathrm{Re}=1000$ | same | 3200 points | $10^{-3}$ as printed |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.7 | same | same | 6400 cells | $10^{-4}$ |

Fan, Zhang & Qiu (2021) use inlet/outlet boundaries, Fan, Zhang & Qiu
(2022) inflow/outflow and Fan, Zhao, Xiong & Qiu outflow ones. The
pressure ratio is again
$10^9$, the density ratio $2\times10^3$; with a different $\gamma$ and
different states this is a different problem from the first version,
not a rescaling of it *(compiler check, not in the sources)*. Wang et
al. describe the density and pressure ratios as $O(10^3)$ and
$O(10^9)$.

## Findings across sources

**Robustness needs a positivity safeguard.** Fu runs the very-high-order
[TENO-AA](/methods/adaptive-teno.md) on this problem with LLF splitting
and the [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md),
like all the paper's extreme cases, and reports it stable (§5.7). Fan, Zhang &
Qiu's (2021) positivity-preserving hybrid [HWENO](/methods/hermite-weno.md) triggers
its scaling limiter in only 0.25 % of the cells and flags 0.97 %
($\mathrm{Re}=1000$) and 1.35 % ($\mathrm{Re}=\infty$) as troubled; they
state that the earlier hybrid HWENO of Zhao, Chen & Qiu blows up on it
from loss of positivity (§1, §4). Wang et al. run their
[multi-resolution WENO](/methods/multi-resolution-weno.md) without a
positivity limiter; they state that the ratio of the linear weights
"used in this paper" is too large for the extreme problems and use
those of the original multi-resolution scheme instead (Example 5.5,
Fig. 5.11); which weights the paper uses elsewhere is ambiguous as
printed.

Fan, Zhang & Qiu (2022) compute it with their
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md)
and scaling limiter at $\mathrm{Re}=1000$; WENO-ZQ5 "produces more
oscillation possibly due to its wider stencil" than WENO-JS5 and
WENO-JS7 (Fig. 5.3), and without the positivity treatment all three
schemes blow up, as stated (§5). Fan, Zhao, Xiong & Qiu's finite-difference
[HWENO](/methods/hermite-weno.md) with restricted derivatives (HWENO-R)
runs it **without** positivity limiters, while the HWENO-L scheme of
Zhang & Zhao, whose flux reconstruction uses the unrestricted
derivative, "cannot simulate" it even with them (§1, Ex. 3.7). They
also state that the other finite-difference HWENO schemes cannot
simulate the problem directly, which is shown only for HWENO-L.

**Low dissipation.** Deng finds low-dissipation
[ROUND](/methods/round-scheme.md) "much less dissipative and less
oscillatory" than WENO-JS5 on 200 cells (Fig. 34).

**Discontinuity position at $x=8$.** The two Chamarthi papers use the
problem to compare gradient-based reconstructions with other
low-dissipation schemes. In Chamarthi (2023a) TENO5 oscillates in density
with larger amplitude, which Chamarthi matches with Fig. 19 of Li, Fu & Adams,
where an MP filter is applied to TENO8-A; MIG4
([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
with an [MP limiter](/methods/monotonicity-preserving-limiter.md))
captures the velocity discontinuity at $x=8$ within one cell (Fig. 14).
In Chamarthi (2023b) the seventh-order mapped WCNS7M is slightly more
dissipative and MEG7 places the discontinuity at $x=8$ closer to the
exact solution (Fig. 4). In the same example of Chamarthi (2023b), MEG7
with conservative variables needs the Zhang–Shu positivity step on the
1D Sedov problem (Fig. 5).

**Cost of hybridization.** Fan, Zhang & Qiu (2021) record their largest
CPU saving
here: the hybrid scheme saves 88.59 % ($\mathrm{Re}=\infty$) and
89.64 % ($\mathrm{Re}=1000$) of the time of the non-hybrid one, because
almost no cells are troubled (Table 4.2).

## Qualifications

- The two versions share a name and the pressure ratio only; results
  on one say nothing directly about the other.
- Evidence is visual against fine-grid or exact references; no source
  reports an error norm.
- Fan, Zhang & Qiu (2022) print $T=0.001$, ten times the $10^{-4}$ of
  the other three sources of this version. The head of the left
  rarefaction moves at $c=\sqrt{1.4\times10^9/2}\approx2.65\times10^4$,
  so it travels about 2.6 by $t=10^{-4}$ but about 26 by $t=10^{-3}$,
  beyond the left end of $[-10,10]$ *(compiler check, not in the
  sources)*; the printed time is either a slip or a run in which the
  rarefaction leaves through the boundary.
- Deng states neither the CFL number nor the Runge–Kutta variant.
- Chamarthi (2023a) and (2023b) are read as arXiv preprints; both run at
  CFL 0.2.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.7.1 (arXiv v1).
- [Deng (2023)](/sources/deng-2023.md) — App. A.8, Fig. 34.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; Ex. 4.5, Fig. 4.5, Table 4.2.
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.5c, Fig. 5.11.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Example 5.4, Fig. 5.3.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — §1, Ex. 3.7.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.10, Fig. 14 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.3, Fig. 4 (arXiv v1).
