---
type: Benchmark
title: "Double rarefaction (123) problem"
description: "One-dimensional Euler Riemann problem of two gases receding from each other, whose two rarefactions leave a near-vacuum (Toro-type 123 data), a vacuum point or a vacuum region at the centre; a positivity and internal-energy robustness test for capturing schemes with and without positivity limiters and a shock-tracking DG method; two-phase variants test bound preservation and cavitation."
status: established
aliases: [123 problem, receding flow, double rarefaction, double rarefaction with vacuum, water cavitation tube, two-phase expansion tube]
tags: [benchmark, positivity, bound-preserving, riemann-solver]
timestamp: 2026-10-23T19:51:00Z
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
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.2 | $(7,\mp1,0.2)$, Navier–Stokes $\mathrm{Re}=1000$; inflow left, outflow right | $[-1,1]$ | 400 points | 0.6 |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.6 | $(7,\mp1,0.2)$, outflow | $[-1,1]$ | 400 cells | 0.6 |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.2, "Einfeldt problem" | $(1,\mp2,0.4)$ | $[-5,5]$ | 200 cells | 1 |
| [Tang (2024)](/sources/tang-2024.md) §4.3, Eq. (30) | $(1,\mp2,0.4)$, split at $x=0$ | $[-5,5]$ | 200 cells, reference WENO-JS on 4000 | 1.0 |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.2, Eq. (31) | $(1,\mp2,0.4)$ | $[0,1]$ (stated for their Sod tube) | 200 cells | 0.15 |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 10, "low density and low internal energy" | $(1,\mp2,0.4)$, transmissive | $[0,1]$ | 300 cells; 30 cells | 0.15; 0.0295 |
| [Fan et al. (2025a)](/sources/fan-2025.md) Ex. 3.8 | $(7,\mp1,0.2)$, outflow | $(-1,1)$ | 400 cells | 0.6 |
| [Fan et al. (2025b)](/sources/fan-2025-b.md) §4.3.1, Eq. (46), "123 problem" | $(1,\mp2,0.4)$, split at $x=0$ | $[-5,5]$ | 400 points | 1 |
| [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) Ex. D.2 | $(7,\mp1,0.2)$ | $[0,1]$ | 400 cells, CFL 0.4 (0.1 for the van Leer–Hänel splitting) | 0.3 |
| [Abgrall et al. (2026)](/sources/abgrall-2026.md) Ex. 8, "1-2-3" | $(1,\mp2,0.4)$, $\gamma=5/3$ | $[0,1]$ | 400 cells, SSP-RK3, CFL 0.2 | 0.15 |
| [Fu (2021)](/sources/fu-2021.md) §5.7.1, Eq. (42) | $(1,\mp2,0.1)$, split at $x=0.5$; $\gamma$ not printed | $[0,1]$ | 400 points, exact reference | 0.1 |

The three data sets fall in the three regimes of the vacuum criterion
*(compiler check, not in the sources)*:

- $(1,\mp2,0.4)$: $c=0.748$, $2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)=7.48>4$,
  no vacuum; $p_{\mathrm m}=0.00189$, $\rho_{\mathrm m}=0.0219$. With
  Abgrall et al.'s $\gamma=5/3$ the same data give $c=0.816$, a
  criterion value $4.90>4$, and a much deeper middle state,
  $p_{\mathrm m}=8.3\times10^{-5}$, $\rho_{\mathrm m}=6.2\times10^{-3}$.
- $(7,\mp1,0.2)$: $c=0.2$, $2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)=2=2v_0$,
  the critical case, in which the two rarefaction tails meet in a
  single vacuum point; Wang et al. call it "double rarefaction with
  vacuum".
- $(1,\mp2,0.1)$: $c=0.374$, $2(c_{\mathrm L}+c_{\mathrm R})/(\gamma-1)=3.74<4$,
  a vacuum interval opens between the rarefactions. Fu prints no
  $\gamma$ for this problem; with $\gamma=5/3$, the value of Fu's Le Blanc
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

A two-phase relative: [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md)
Ex. 4.3 run the receding flow in the five-equation (Kapila) model with
a material interface at the centre: phase densities
$(\rho_1,\rho_2)=(2,2)$, $p=0.2$, $v=\mp1$, volume fraction
$\phi_1=1-10^{-10}$ on the left and $10^{-10}$ on the right, $\gamma_1=1.4$
and $\gamma_2=4.4$, on $[-1,1]$ with 200 cells and outflow boundaries,
$\mathbb P^2$, to $t=0.4$. For a Riemann problem between two ideal gases
the two-rarefaction solution keeps a non-vacuum middle state when
$2c_{\mathrm L}/(\gamma_{\mathrm L}-1)+2c_{\mathrm R}/(\gamma_{\mathrm R}-1)>2v_0$;
here $1.871+0.390=2.26>2$, a near-vacuum case like the 123 data
*(compiler check, not in the sources)*.

## Findings across sources

**Positivity limiters are triggered.** Fan, Zhang & Qiu's (2021)
positivity-preserving hybrid [HWENO](/methods/hermite-weno.md) computes the critical case
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
keeps positivity on RP3 (§7.2, Figs. 3–4); Renac's Theorem 6.1 proves
positive cell averages under a CFL condition with factor
$1/(2N(N+1))$, while the runs use a practical time-step bound of 0.4
(§6.2, §7).

Fan, Zhang & Qiu (2022) run the critical case with the compressible
Navier–Stokes equations at $\mathrm{Re}=1000$ and their
[positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md)
with a finite-difference WENO convection; their results are comparable
to the positivity-preserving DG of Zhang, and WENO-ZQ5 is better than
WENO-JS5 and WENO-JS7 in the zoomed low-density centre (Fig. 5.1, which
also maps where the limiter acts in space and time). They state that
without the positivity flux and limiter all three WENO schemes blow up
on this test, without showing the failed runs (§5). Fan, Zhao, Xiong &
Qiu instead run their finite-difference HWENO with restricted
derivatives (HWENO-R) and WENO-ZQ on the same data **without**
positivity limiters, and both complete (Ex. 3.6). Fan et al. (2025a) do
the same with their moment-based HWENO with unified stencils (HWENO-U),
HWENO-M and WENO-ZQ: all three run without positivity limiters
(Fig. 12), while their 1D Sedov problem needs them.

**Bound-preserving point–average updates.** Abgrall et al. (2026) run
the 123 data at $\gamma=5/3$ with their bound-preserving
[PAMPA scheme](/methods/pampa-scheme.md), which enforces positive
density and internal energy on cell averages and point values through
a [geometric quasilinearization](/methods/geometric-quasilinearization.md)
of the admissible set; the solution is non-oscillatory, with a
near-vacuum centre (Fig. 9). They state that their bound-preserving
technique cures the non-physical solutions that the Jacobian splitting
of the point-value update can give for the Euler equations, observed
by [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) and by others (§2).

Duan, Barsukow & Klingenberg run the critical vacuum-point data with
their generalized [Active Flux](/methods/active-flux.md) method, whose
point values are updated by Jacobian splitting or by one of three
[flux vector splittings](/methods/flux-vector-splitting.md) (local
Lax–Friedrichs, Steger–Warming, van Leer–Hänel): every variant fails
without their bound-preserving limiting, convex limiting of the cell
averages plus a scaling limiter of the point values, and runs with it
(Ex. D.2, arXiv v3).

**Learned weights at strong rarefactions.** Fan et al. (2025b) run the
no-vacuum 123 data with their learned third-order
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) (WCNS3-MR-NN),
WCNS3-JS and WCNS3-MR, and present the completed run, with the Leblanc
tube, as the evidence of robustness at strong rarefactions (§4.3.1,
Fig. 11); no positivity limiter is mentioned for these runs.

**Two-phase bound preservation.** Yan, Abgrall & Wu's bound-preserving
[OEDG](/methods/oedg.md) scheme keeps density and internal energy
positive and the volume fraction in $[0,1]$ on their two-phase receding
flow (Fig. 5); without the bound-preserving limiter the computation can
terminate on negative density or pressure, which they state without a
figure. See [bound preservation](/properties/bound-preservation.md).


**Scale invariance and spurious oscillations.** Li, Li, Don & Wang run
the no-vacuum data under the name of Einfeldt and find that the
multi-resolution [alternative WENO](/methods/alternative-weno.md)
MR-AWENO of Wang, Zhu, Yang & Zhao produces spurious oscillations near
the rarefactions already on the unscaled data, while their
scale-invariant MR-AWENO-Si is essentially non-oscillatory (§3.2,
Fig. 5); see [scale invariance](/properties/scale-invariance.md).

**Adaptive TENO cut-offs.** Tang runs the Li, Li, Don & Wang data
with fifth-order finite-difference TENO schemes, global Lax–Friedrichs
splitting and TVD-RK3 at CFL 0.5; no positivity limiter is mentioned. The
adaptive-cut-off TENO-A of Fu, Hu & Adams "produces a trend directly
opposite to that of the trusted reference solution" around the centre,
while Tang's TENO-AZ, whose cut-off is $\min(10^{-5},\lvert\beta_0+\beta_2-2\beta_1\rvert)$,
performs comparably to TENO-LAD and better than TENO-A and TENO-Z, the
difference being most evident on this test among the paper's one-dimensional
problems (§4.3, Fig. 8; see [adaptive TENO](/methods/adaptive-teno.md)).
Tang's CPU-time ratios to TENO-Z, averaged over 1000 runs, are 0.96
(TENO-AZ), 1.06 (TENO-A) and 1.38 (TENO-LAD) (Table 5).

**Smoothness indicators and failure without a limiter.** Zhong et
al. run the no-vacuum data with eight fifth-order finite-volume WENO
schemes, SSP-RK3, global Lax–Friedrichs flux and characteristic
decomposition, without a positivity limiter (Figs. 9–12). WENO-NS,
WENO-P and MWENO-P, whose $L^1$-type smoothness indicators are not
mirror-symmetric, "fail to finish the simulation" on 300 cells and
produce negative pressure on 30 cells by $t=0.0295$; WENO-JS, WENO-Z,
WENO-η, WENO-ZS and their symmetric IMWENO-P complete it. They state
that this "is not enough to link the symmetry-preserving property with
the positivity-preserving property". Their symmetry error of the
solution is smallest for IMWENO-P over $0.041<t<0.093$ and afterwards
at the level of WENO-JS, WENO-Z and WENO-η, much below WENO-ZS (see
[symmetry preservation](/properties/symmetry-preservation.md) and
[smoothness indicator](/definitions/smoothness-indicator.md)).

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

**Cost.** Fan, Zhang & Qiu's (2021) hybridization saves 59.05 % ($\mathrm{Re}=\infty$)
and 67.34 % ($\mathrm{Re}=1000$) of the CPU time of the non-hybrid
scheme (Table 4.2).

**Scale invariance.** [Wang & Don (2022)](/sources/wang-2022-b.md)
§3.2.3 run the 123 problem, with specifications deferred to an earlier
paper, and find affine-invariant Z- and D-type weights essentially
identical and non-oscillatory (Fig. 7); see
[scale invariance](/properties/scale-invariance.md).

## Two-phase variant: water cavitation tube

[Wakimura et al. (2024)](/sources/wakimura-2024.md) (§4.1, Eq. (46),
after Pelanti & Shyue) run the same receding-flow configuration for
liquid water with a little vapour, in the six-equation two-phase model
with stiffened-gas water (their Table 1; see
[five- and six-equation models](/definitions/five-equation-model.md) and
[stiffened gas](/definitions/stiffened-gas-equation-of-state.md)). On
$x\in[0,1]$ m with outflow boundaries, the liquid volume fraction is
$\phi_1=0.99$, the phase densities $\rho_1=1150$ and
$\rho_2=0.63$ kg m$^{-3}$, $p=10^5$ Pa and $T_1=T_2=354.728$ K on both
sides, and the velocity is $-\lvert v_0\rvert$ for $x<0.5$ m and
$+\lvert v_0\rvert$ for $x>0.5$ m. Two cases: $\lvert v_0\rvert=2$ m s$^{-1}$
on 500 cells to $t=3.2$ ms, and $\lvert v_0\rvert=500$ m s$^{-1}$ on 5000
cells to $t=0.58$ ms, CFL 0.5. The pressure drop in the expansion
creates vapour; four variants of the relaxation (mechanical only, plus
thermal, plus chemical, i.e. phase change) are compared. The authors
obtain the temperature from the liquid density by the isothermal
condition; the stiffened-gas law with their Table 1 parameters at
$p=10^5$ Pa and $T=354.728$ K gives back $\rho_1\approx1150.0$ and
$\rho_2\approx0.630$ kg m$^{-3}$ *(compiler check, not in the sources)*.

The test serves their low-dissipation
[BVD](/definitions/boundary-variation-diminishing.md) schemes, which
choose per cell between MUSCL and [THINC](/methods/thinc-reconstruction.md)
reconstructions of different steepness. MUSCL and the adaptive THINC
scheme give generally similar solutions, with mass-fraction differences
between MUSCL-THINC-BVD and MUSCL of at most $1.49\times10^{-6}$ ($2$ m
s$^{-1}$) and $6.00\times10^{-5}$ ($500$ m s$^{-1}$), in general agreement
with Pelanti & Shyue (Figs. 1–2). For the strong case the steep THINC
is admitted in the selection only where $\nabla\cdot v<0$ (compression),
"to address the strong rarefaction waves"; no result without this
condition is shown (§4.1).

## Qualifications

- Fan, Zhang & Qiu (2021) caption Fig. 4.3 "$\mathrm{Re}=\infty$ (right) and 1000
  (left)", the reverse of their convention in the other figures.
- Fu prints the data on $0\le x<0.5$ and $0.5\le x\le1$ (Eq. (42)) but
  no $\gamma$ for this problem.
- Fan, Zhang & Qiu (2022) caption Fig. 5.1 "Double Rarefraction
  problem" and print inflow on the left for data whose left gas moves
  out of the domain.
- Wakimura et al.'s §4.1 text calls the density 1150 kg m$^{-3}$ "the gas
  density $\rho_2$", while their Eq. (46) and the liquid phase 1 assign
  it to $\rho_1$.
- Luo et al.'s claim that no other method avoids overheating is
  attributed to Liou and not tested in the paper.
- Abgrall et al. (2026) set $\gamma=5/3$ for this example only by a
  general statement of their §4.2 ("$\gamma=1.4$, except for Example 4
  where $\gamma=3$, and Example 8 where $\gamma=5/3$"), so their run is a
  deeper near-vacuum than the $\gamma=1.4$ runs of the same data.

# Citations

- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §IV.C, Figs. 18–21 (author manuscript).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; Ex. 4.3, Fig. 4.3, Table 4.2.
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.5b, Fig. 5.10.
- [Fu (2021)](/sources/fu-2021.md) — §5.7.1 (arXiv v1).
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Example 5.2, Fig. 5.1.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.6.
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §3.2, Fig. 5.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.2, Eq. (31), Figs. 10, 26; App. A.6, Table 4.
- [Renac (2021)](/sources/renac-2021.md) — §7.2, RP3, Figs. 3–4 (arXiv v3).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.3, Fig. 7.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.3, Ex. 10, Figs. 9–12.
- [Tang (2024)](/sources/tang-2024.md) — §4.3, Eq. (30), Fig. 8, Table 5.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §3.2.3–3.2.4, §4.1, Eq. (46), Table 1, Figs. 1–2.
- [Fan et al. (2025a)](/sources/fan-2025.md) — Ex. 3.8, Fig. 12.
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §2, §3.4, §4.2, Ex. 8, Fig. 9.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Ex. 4.3, Fig. 5.
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §4, Ex. D.2 (arXiv v3).
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §4.3.1, Eq. (46), Fig. 11.
