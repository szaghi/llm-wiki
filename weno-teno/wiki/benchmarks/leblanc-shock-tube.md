---
type: Benchmark
title: "Leblanc shock tube"
description: "One-dimensional Euler Riemann problem with pressure ratio 10^9 and density ratio 10^3 or 2×10^3, printed in two inequivalent versions under one name, plus a rescaled copy and a gamma = 1.4 variant of the first; a near-vacuum robustness test for positivity limiters, DG blending and ALE remapping, judged against fine or exact references."
status: established
aliases: [LeBlanc problem, Le Blanc shock tube, LeBlanc shock tube]
tags: [benchmark, positivity, bound-preserving, low-dissipation]
timestamp: 2026-10-23T23:00:00Z
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

**Rescaled copy on $[0,1]$.** [Lin, Chan & Tomas (2023)](/sources/lin-2023.md)
§8.1.1 (arXiv v2) print, on $[0,1]$ with the jump at $x_0=0.33$ and
$\gamma=5/3$, the left state $(\rho,v,p)=(1,0,(\gamma-1)\,0.1)$ and the
right state $(10^{-3},0,(\gamma-1)10^{-10})$, Dirichlet exterior states,
$T=2/3$, and the exact solution with $p^*=0.515577927650970\times10^{-3}$,
$v^*=0.621838671391735$ and the two star densities
$5.40793353493162\times10^{-2}$ and $3.99999806043000\times10^{-3}$.
These are Fu's states, and dividing $x$ and $t$ by 9 maps $[0,9]$,
$x=3$, $t=6$ onto $[0,1]$, $x=1/3$, $t=2/3$, since the Euler equations
are invariant under a common scaling of space and time; the printed
jump $0.33$ is $1/3$ rounded *(compiler check, not in the sources)*.

**Variant with $\gamma=1.4$.** [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md)
§3.5.4 print Deng's internal energies, $(\rho,v_1,v_2,e)$ equal to
$(1,0,0,0.1)$ on $0\le x<3$ and $(0.001,0,0,10^{-7})$ on $3\le x<9$ of
$[0,9]\times[0,1]$, but with $\gamma=1.4$, fixed left and right
boundaries, reflective walls elsewhere, $t=6$. With $p=(\gamma-1)\rho e$
the pressures are $0.04$ and $4\times10^{-11}$: the pressure and density
ratios are unchanged, but the sound speeds and wave positions differ
from the $\gamma=5/3$ version *(compiler check, not in the sources)*.

## Version on $[-10,10]$, $\gamma=1.4$

| Source | Left, $x<0$ | Right | Grid | Final time |
|---|---|---|---|---|
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.5 | $(\rho,v,p)=(2,\ 0,\ 10^9)$ | $(0.001,\ 0,\ 1)$ | 3200 cells, logarithmic plots | $10^{-4}$ |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.5c | same | same | 6400 points | $10^{-4}$ |
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.4 | same, Navier–Stokes $\mathrm{Re}=1000$ | same | 3200 points | $10^{-3}$ as printed |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.7 | same | same | 6400 cells | $10^{-4}$ |
| [Peyvan et al. (2023)](/sources/peyvan-2023.md) §4.1 | same, $\gamma=1.4$ | same | 1000 elements, $P=3$ (4000 solution points) | $10^{-4}$ |

Fan, Zhang & Qiu (2021) use inlet/outlet boundaries, Fan, Zhang & Qiu
(2022) inflow/outflow and Fan, Zhao, Xiong & Qiu outflow ones. The
pressure ratio is again
$10^9$, the density ratio $2\times10^3$; with a different $\gamma$ and
different states this is a different problem from the first version,
not a rescaling of it *(compiler check, not in the sources)*. Wang et
al. describe the density and pressure ratios as $O(10^3)$ and
$O(10^9)$.

Peyvan et al. use a fixed $\Delta t=2.0893\times10^{-8}$ and cite the
problem as the "Leblanc Sod problem".

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

**Positivity-only blending of entropy-stable DG.** Lin, Chan & Tomas
measure $L^1$ errors against the exact solution, for $N=2$ and $5$ on
$N_{\mathrm{el}}=50$–$800$ elements (page-local count) at CFL 0.5, of their sparse low-order
positivity-preserving scheme and of entropy-stable DG blended
elementwise with it under bounds relaxed by $\zeta_{\mathrm r}=0.1$ and $0.5$ (their $\zeta$)
(Table 1, Figs. 2–3). At $N_{\mathrm{el}}=800$ the limited $N=5$ errors are
$6.333\times10^{-4}$ ($\zeta_{\mathrm r}=0.1$) and $5.889\times10^{-4}$ ($\zeta_{\mathrm r}=0.5$),
against $2.868\times10^{-2}$ for the low-order scheme. They state that
"all strategies are first order accurate, which is optimal for this test
case"; the printed low-order rates are 0.35–0.69 and the $N=2$ limited
rates reach 1.07 and 1.05 at the finest pair. The low-order solutions for
$N=2$ and $N=5$ at 600 degrees of freedom nearly coincide, which they
attribute to the sparsified low-order operator. See
[convex limiting](/methods/convex-limiting.md) and
[DGSEM](/methods/dgsem.md).

**Element methods for hypersonic flows.** Peyvan et al. compare
entropy-stable [DGSEM](/methods/dgsem.md) with high/low-order flux
blending (maximum blending $\alpha_{\max}=0.5$, Chandrashekar
entropy-conservative volume flux) against spectral-difference (SD) and
[flux-reconstruction](/methods/flux-reconstruction.md) schemes, both
with the adaptive [entropy filter](/methods/entropy-filtering.md):
ES-DGSEM smears the contact more than FR and SD but has the smallest
oscillations; SD has the largest oscillations and undershoots, which
they attribute to its degree-$P+1$ flux polynomial (Fig. 1). They also
state that, "according to our experience", artificial viscosity cannot
stabilize a high-order spectral method for shocks of high pressure
ratio; no run is shown.

**ALE with positivity-preserving remapping.** Gu et al. run the
$\gamma=1.4$ variant with an indirect ALE method: the third-order
positivity-preserving ENO Lagrangian scheme of Cheng & Shu, rezoning
and their positivity-preserving multi-resolution WENO
[conservative remapping](/methods/conservative-remapping.md) every 20
steps, without moving the nodes at the shock and contact fronts
(Fig. 19). On $2100\times2$ and $4200\times2$ cells the finer mesh
agrees better with the exact solution in the shape and position of the
contact and the shock.

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
- The two versions and the two relatives (Lin, Chan & Tomas's rescaled
  copy, Gu et al.'s $\gamma=1.4$ variant) give four sets of wave
  positions; only the rescaled copy is equivalent to a printed version.
- Evidence is visual against fine-grid or exact references, except Lin,
  Chan & Tomas's $L^1$ errors against the exact solution.
- Peyvan et al. write that "the pressure ratio is $10^9$ and the
  density ratio is $10^5$" (§4.1 and Fig. 1 caption); their printed
  densities $2$ and $0.001$ give a ratio of $2\times10^3$, as in the
  other sources of this version *(compiler check, not in the sources)*.
  They are read in the arXiv v1 preprint.
- Gu et al. print the left state with five components,
  $(1,0,0,0,0.1)$, for the four variables $(\rho,v_1,v_2,e)$; the right
  state has four. The values used above drop the extra zero.
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
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.1.1, Eq. (61), Table 1, Figs. 2–3 (arXiv v2).
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §4.1, Fig. 1 (arXiv v1).
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §3.5.4, Fig. 19.
