---
type: Benchmark
title: "Double rarefaction (123) problem"
description: "One-dimensional Euler Riemann problem of two gases receding from each other, whose two rarefactions leave a near-vacuum (Toro-type 123 data), a vacuum point or a vacuum region at the centre; a positivity and internal-energy robustness test, run by capturing schemes with positivity limiters and by a shock-tracking DG method."
status: established
aliases: [123 problem, receding flow, double rarefaction, double rarefaction with vacuum]
tags: [benchmark, positivity, bound-preserving, riemann-solver]
timestamp: 2026-10-22T20:00:00Z
---

# Double rarefaction (123) problem

Two states of equal density and pressure move apart with opposite
velocities $\mp v_0$ (page-local symbol). Two rarefactions run outwards
and leave between them a region of low density and pressure. Whether
that region is a near-vacuum, a single vacuum point or a vacuum
interval depends on the data: for an ideal gas the two-rarefaction
solution produces a vacuum exactly when
$2v_0\ge2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)$, with
$c_{\mathrm L}$, $c_{\mathrm R}$ the sound speeds of the two states, and
otherwise has the middle state
$c_{\mathrm m}=c-\tfrac{\gamma-1}{2}v_0$,
$p_{\mathrm m}=p\,(c_{\mathrm m}/c)^{2\gamma/(\gamma-1)}$ for symmetric data
(page-local symbols; *compiler check, not in the sources*, from the
Riemann invariants). Density and pressure near zero make the problem a
test of [positivity](/properties/bound-preservation.md), and the
internal energy at the centre, a ratio of two vanishing quantities, is
where schemes go wrong.

## Setups

All with $\gamma=1.4$ unless stated; states $(\rho,v,p)$ on the left and
right of the centre.

| Source | Data | Domain | Grid | Final time |
|---|---|---|---|---|
| [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) §IV.C | $(1,\mp2,0.4)$ | $(-0.5,0.5)$ | 16 space–time quadrilaterals, $\mathbb P^2$ | 0.15 |
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.3 | $(7,\mp1,0.2)$ | $[-1,1]$ | 200 cells, exact reference | 0.6 |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.5b | $(7,\mp1,0.2)$ | $[-1,1]$ | 400 points, reference from Zhang & Shu | 0.6 |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.2, Eq. (31) | $(1,\mp2,0.4)$ | $[0,1]$ (stated for their Sod tube) | 200 cells | 0.15 |
| [Fu (2021)](/sources/fu-2021.md) §5.7.1, Eq. (42) | $(1,\mp2,0.1)$, split at $x=0.5$; $\gamma$ not printed | $[0,1]$ | 400 points, exact reference | 0.1 |

The three data sets fall in the three regimes of the vacuum criterion
*(compiler check, not in the sources)*:

- $(1,\mp2,0.4)$: $c=0.748$, $2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)=7.48>4$,
  no vacuum; $p_{\mathrm m}=0.00189$, $\rho_{\mathrm m}=0.0219$.
- $(7,\mp1,0.2)$: $c=0.2$, $2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)=2=2v_0$,
  the critical case, in which the two rarefaction tails meet in a
  single vacuum point; Wang et al. call it "double rarefaction with
  vacuum".
- $(1,\mp2,0.1)$: $c=0.374$, $2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)=3.74<4$,
  a vacuum interval opens between the rarefactions. Fu prints no
  $\gamma$ for this problem; with $\gamma=5/3$, the value of his Le Blanc
  problem, $c=0.408$ and the criterion gives $2.45<4$, the same regime.

Luo et al. call their problem the "receding flow" or 123 problem and
pose it, after Liou, as an open problem of overheating: an anomalous
internal energy at the centre produced by Eulerian, Lagrangian and ALE
methods alike.

A multicomponent relative: [Renac (2021)](/sources/renac-2021.md)
§7.2 "RP3" is a near-vacuum double rarefaction of the
[two-component Euler equations](/definitions/multicomponent-euler-equations.md),
$(Y_1,\rho,v,p)=(0.2,\ 0.99988,\ -1.99931,\ 0.4)$ and
$(0.5,\ 0.99988,\ 1.99931,\ 0.4)$ with $Y_1$ the mass fraction of
component 1, $\gamma_1=1.5$, $\gamma_2=1.3$, unit heat capacities,
$t=0.15$, entropy-stable DGSEM with $N=3$ on 100 cells.

## Findings across sources

**Positivity limiters are triggered.** Fan et al.'s positivity-preserving
hybrid [HWENO](/methods/hermite-weno.md) computes the critical case
robustly; its scaling limiter acts in 10.00 % of the cells, the largest
share among their tests, and 11.30 % ($\mathrm{Re}=1000$) and 19.57 %
($\mathrm{Re}=\infty$) of the cells are troubled; they state that the
earlier hybrid HWENO of Zhao, Chen & Qiu blows up here from loss of
positivity (Fig. 4.3, Table 4.2). Fu computes the vacuum case stably
with LLF splitting and the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
(§5.7). Wang et al.'s [multi-resolution WENO](/methods/multi-resolution-weno.md),
with no positivity limiter, is run with the linear weights of the
original scheme, because the ratio of the weights "used in this paper"
is too large for the extreme problems (Example 5.5, Fig. 5.10). Renac's DGSEM with a [Zhang–Shu-type limiter](/methods/zhang-shu-scaling-limiter.md)
keeps positivity on RP3 (§7.2, Figs. 3–4); his Theorem 6.1 proves
positive cell averages under a CFL condition with factor
$1/(2N(N+1))$, while the runs use a practical time-step bound of 0.4
(§6.2, §7).

**Accuracy between the rarefactions.** Bezgin et al. run the
no-vacuum data without a positivity limiter and rank the schemes by the
summed $L_1$ error of $\rho$, $v$ and $p$: their three-point learned
[WENO3-NN2](/methods/learned-weno-weights.md) gives
$1.967\times10^{-2}$, below WENO5-Z ($2.282\times10^{-2}$), WENO5-JS
($2.393\times10^{-2}$) and WENO3-JS ($2.540\times10^{-2}$) (App. A.6,
Table 4); it is the only one of their tests on which WENO5-Z is not
best. They note that WENO3-NN has a slightly larger error between the
rarefactions (App. A.6, Figs. 10, 26), so the lower norm comes from
elsewhere in the profile *(compiler check, not in the sources)*. They
also state that WENO3-NN handles the strong rarefactions "without
introducing invalid pressure values" (§4.2, Fig. 10).

**Tracking the rarefactions.** Luo, Absillis & Nourgaliev's
[moving DG with interface condition enforcement](/methods/implicit-shock-tracking.md)
removes the initial discontinuity by collapsing the two space–time
cells next to it; before their removal those cells have zero volume and
negative density, which does not stop the solver. After removal the
density, velocity, pressure and internal energy agree with the exact
solution "without overheating", which they say no other numerical
method achieves "to the best of our knowledge" (Figs. 18–21); the
evidence is figures, without error norms, and no capturing scheme is
run for comparison.

**Cost.** Fan et al.'s hybridization saves 59.05 % ($\mathrm{Re}=\infty$)
and 67.34 % ($\mathrm{Re}=1000$) of the CPU time of the non-hybrid
scheme (Table 4.2).

**Scale invariance.** [Wang & Don (2022)](/sources/wang-2022-b.md)
§3.2.3 run the 123 problem, with specifications deferred to an earlier
paper, and find affine-invariant Z- and D-type weights essentially
identical and non-oscillatory (Fig. 7); see
[scale invariance](/properties/scale-invariance.md).

## Qualifications

- Fan et al. caption Fig. 4.3 "$\mathrm{Re}=\infty$ (right) and 1000
  (left)", the reverse of their convention in the other figures.
- Fu prints the data on $0\le x<0.5$ and $0.5\le x\le1$ (Eq. (42)) but
  no $\gamma$ for this problem.
- Luo et al.'s claim that no other method avoids overheating is
  attributed to Liou and not tested in the paper.

# Citations

- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §IV.C, Figs. 18–21 (author manuscript).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; Ex. 4.3, Fig. 4.3, Table 4.2.
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.5b, Fig. 5.10.
- [Fu (2021)](/sources/fu-2021.md) — §5.7.1 (arXiv v1).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.2, Eq. (31), Figs. 10, 26; App. A.6, Table 4.
- [Renac (2021)](/sources/renac-2021.md) — §7.2, RP3, Figs. 3–4 (arXiv v3).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.3, Fig. 7.
