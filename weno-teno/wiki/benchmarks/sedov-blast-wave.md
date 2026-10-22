---
type: Benchmark
title: "Sedov blast wave"
description: "Point-explosion benchmark in which the energy of one cell drives a strong shock into cold gas of near-zero pressure, in one dimension and in a two-dimensional corner, with an exact similarity solution; a robustness test of positivity preservation at pressure ratios near 10^20, with a gas–liquid variant."
status: established
aliases: [Sedov problem, Sedov–Taylor blast wave, point explosion, Sedov blast]
tags: [benchmark, positivity, bound-preserving, weno]
timestamp: 2026-10-22T12:00:00Z
---

# Sedov blast wave

A finite energy is deposited in a single cell of a gas at rest whose
internal energy elsewhere is $10^{-12}$ per unit volume. A strong
shock (planar in 1D, cylindrical in the 2D corner version) runs outwards, and behind it the density
falls towards zero at the centre, so the solution combines a shock of
enormous strength with a near-vacuum core. The problem has a
self-similar exact solution, which two of the one-dimensional sources
use as reference (Fan et al., Li, Shu & Qiu). Pressure is a tiny difference of large energies near the
centre, so a high-order scheme without a
[positivity](/properties/bound-preservation.md) safeguard tends to
produce negative pressure; the sources use the test as a robustness
check and read resolution from the height of the density peak behind
the shock.

## One-dimensional version

The common data, written in $(\rho,v,E)$: $(1,0,10^{-12})$ on $[-2,2]$
except the centre cell, where $E=3200000/\Delta x$, so that the
deposited energy is $3.2\times10^6$ whatever the grid; inlet/outlet
boundaries; $t=0.001$. On 400 cells ($\Delta x=0.01$) the centre cell
holds $E=3.2\times10^8$, $3.2\times10^{20}$ times the ambient value
*(compiler check, not in the sources)*.

| Source | Cells | Reference | Scheme |
|---|---|---|---|
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.4 | 400 | exact solution | positivity-preserving hybrid [HWENO](/methods/hermite-weno.md), Euler and Navier–Stokes ($\mathrm{Re}=1000$) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.8 | 400 | exact solution | moment-based multi-resolution HWENO, with and without modified first moments |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.5a | 400 | WENO-JS5, 6400 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR), WENO-AO5, WENO-JS5 |

Wang et al. attribute the setup to Zhang & Shu (2012). Li, Shu & Qiu
print the deposited cell as "the centre cell" and plot density,
velocity, pressure and the troubled cells (Fig. 3.6).

## Two-dimensional corner version

The blast is placed in the lower-left corner cell of $[0,1.1]^2$ with
reflecting (symmetry) left and bottom boundaries and outflow elsewhere,
$\rho=1$, $v=0$, on $160\times160$ cells ($\Delta x=\Delta y=1.1/160$).

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.6: $E=10^{-12}$
  except the corner cell, where $E=0.244816/(\Delta x\Delta y)$; $t=1$;
  30 density contours from 0.95 to 5 (Fig. 4.6).
- [Fu (2021)](/sources/fu-2021.md) §5.7.2: pressure $4\times10^{-13}$
  except the corner cell, where $p=9.79264\times10^{4}/(\Delta x\Delta y)$;
  $t=10^{-3}$; $\gamma$ not printed; [TENO-AA](/methods/adaptive-teno.md)
  with LLF splitting and the
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md).

The two setups are one problem under the similarity scaling of the
blast *(compiler check, not in the sources)*. With $\gamma=1.4$,
$p=(\gamma-1)E$ turns Fan et al.'s ambient $E=10^{-12}$ into Fu's
$p=4\times10^{-13}$ and their corner energy into
$p=0.0979264/(\Delta x\Delta y)$, which is $10^{-6}$ times Fu's corner
pressure. Fu's run thus deposits $10^6$ times the energy and stops at
$10^{-3}$ times the time. A cylindrical blast of energy $E_0$ per unit length (page-local; the
corner run is a quarter of it) in gas of density $\rho$ has, by
dimensional analysis, a radius $R\propto(E_0t^2/\rho)^{1/4}$, and
$E_0t^2$ is the same in both runs, so the shock reaches the same radius; velocities are $10^3$ times larger in
Fu's run and its ambient pressure is relatively $10^6$ times smaller,
both immaterial for a strong blast. Fu's printed factor $\times10^4$ is
therefore consistent with a rescaled run, not evidence of a misprint.

## Gas–liquid version

[Wong et al. (2021)](/sources/wong-2021.md) §6.4 run a planar
multi-material Sedov problem in the
[five-equation model](/definitions/five-equation-model.md): water
($\gamma=6.12$, stiffening pressure $3.43\times10^8$ Pa) with partial
density 1000 kg m$^{-3}$ and pressure $-3.0\times10^7$ Pa fills
$[0,4]$ m, except the centre cell, which holds air with partial density
1 kg m$^{-3}$ and pressure $1.28\times10^6/\Delta x$ Pa; 401 points,
$t=10^{-3}$ s, reference 4001 points. The negative water pressure is
admissible because the
[stiffened-gas](/definitions/stiffened-gas-equation-of-state.md)
condition requires only $p$ plus the stiffening pressure to be positive.
Both first-order HLLC and their positivity-preserving
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) are free of
spurious oscillations, and the WCNS gives much sharper shocks
(Figs. 9–10).

## Findings across sources

**A positivity safeguard is the price of running the test.** Fan et al.
state that the earlier hybrid HWENO of Zhao, Chen & Qiu blows up on
both Sedov problems from loss of positivity (no figure shown); their
scaling limiter is triggered in 3.00 % of the cells in 1D and 1.09 % in
2D, identically for the hybrid and non-hybrid positivity-preserving
schemes (Table 4.2). Fu computes the corner blast, like all his
extreme cases, with the positivity-preserving flux limiter and reports
it stable (§5.7). Wang et al. use no
positivity limiter: the ratio of the linear weights "used in this
paper" is "so large" that the scheme cannot run the extreme problems
robustly, and they switch to the weights of the original
multi-resolution scheme (Example 5.5); which weights the paper uses
elsewhere is ambiguous as printed (see
[multi-resolution WENO](/methods/multi-resolution-weno.md)).

**Resolution of the density peak.** Wang et al. find WENO-JS5 and both
multi-resolution schemes similar, and all worse than WENO-AO5 near the
peak; they conjecture that near strong shocks of large pressure ratio
their algorithm reduces quickly to first order (Fig. 5.9). Li, Shu &
Qiu find their modified HWENO "much better" resolved than the unmodified
one (comment p. 31).

**Troubled cells and cost.** In Fan et al.'s hybrid scheme the
nonlinear reconstruction is applied only in troubled cells: 11.92 %
(Navier–Stokes) and 14.50 % (Euler) of the cells in 1D, 13.82 % and
14.62 % in 2D, concentrated in a band behind the shock. The hybrid
saves 68.86 % (Euler) and 69.02 % (Navier–Stokes) of the CPU time of
the non-hybrid scheme in 1D, 62.64 % and 63.64 % in 2D, hardware not
stated (Table 4.2).

## Qualifications

- Fu (2021) prints the corner-cell condition as "$x\le\Delta x$ and
  $x\le\Delta y$"; the second inequality must read $y\le\Delta y$.
- The 1D sources print no $\gamma$ for the problem; Fan et al. use
  $\gamma=1.4$ throughout their paper.

# Citations

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; Ex. 4.4, Ex. 4.6, Fig. 4.6, Table 4.2.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.8, Fig. 3.6; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.5a, Fig. 5.9.
- [Fu (2021)](/sources/fu-2021.md) — §5.7.2, Eq. (44) (arXiv v1).
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.4, Table 7, Figs. 9–10 (arXiv v1).
