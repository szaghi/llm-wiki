---
type: Benchmark
title: "Shu–Osher shock–entropy-wave problem"
description: "One-dimensional Euler benchmark of a Mach 3 shock running into a sinusoidal density (entropy) wave, with its Titarev–Toro high-frequency variant; the bundle's most widely run test of how well a shock-capturing scheme resolves the short waves generated behind a shock without oscillating at the shocklets."
status: established
aliases: [Shu–Osher problem, shock–density wave interaction, shock–entropy wave interaction, Titarev–Toro problem]
tags: [benchmark, low-dissipation, weno, teno]
timestamp: 2026-10-23T10:00:00Z
---

# Shu–Osher shock–entropy-wave problem

A Mach 3 shock moves to the right into gas at rest whose density
carries a small sinusoidal perturbation at uniform pressure, i.e. an
entropy wave. Passing through the shock, the wave is compressed into a
band of short, steep density oscillations, followed by weak shocklets.
A dissipative scheme damps the short waves; an oscillatory one creates
spurious waves near the shocklets. The problem is the most widely run
one-dimensional resolution test in the bundle: thirty-two sources run it
or a variant (one of them a review reproducing earlier figures), in five
placements of one set of data, plus a high-frequency variant attributed
to Titarev & Toro, two-medium variants and a radial two-dimensional
extension.

## Common data and its placements

With $\gamma=1.4$, the post-shock state of a Mach 3 shock moving into
$(\rho,v,p)=(1,0,1)$ is

$$
(\rho,v,p)_{\mathrm L}=\Big(\tfrac{27}{7},\ \tfrac{4\sqrt{35}}{9},\ \tfrac{31}{3}\Big)
\approx(3.857143,\ 2.629369,\ 10.333333),
$$

as printed in exact form by [Li et al. (2022)](/sources/li-2022-b.md)
Eq. (40) and [Ye et al. (2022)](/sources/ye-2022.md) Eq. (44), and in
decimals by the others (Rankine–Hugoniot with $M=3$ reproduces these
values *(compiler check, not in the sources)*). The pre-shock state is
$(1+0.2\sin(5x),\,0,\,1)$ in the coordinates of $[-5,5]$, and the run
ends at $t=1.8$.

| Placement | Shock position | Perturbation | Final time | Sources |
|---|---|---|---|---|
| $[-5,5]$ | $x=-4$ | $1+0.2\sin(5x)$ | 1.8 | [Li et al. (2022)](/sources/li-2022-b.md) §4.3.2; [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.2; [Wang et al. (2023)](/sources/wang-2023-b.md) Example 2; [Takagi et al. (2022)](/sources/takagi-2022.md) §4.4; [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.8 (domain not stated); [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.6; [Pazner (2021)](/sources/pazner-2021.md) §5.2.2; [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.3, Eq. (42); [Wang et al. (2021)](/sources/wang-2021.md) Example 5.4a; [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.2.2; [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.2; [Hiejima (2022)](/sources/hiejima-2022.md) §3.3, Eq. (28); [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.3.2; [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.4; [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.5 |
| $[0,10]$ | $x=1$ | $1+0.2\sin(5(x-5))$ | 1.8 | [Fu (2021)](/sources/fu-2021.md) §5.4; [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.5; [Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.5 (two-dimensional strip on triangles) |
| $[0,10]$ | $x=1$ | $1+0.2\sin(5x)$ as printed | 1.8 | [Ye et al. (2022)](/sources/ye-2022.md) §4.4; [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.4, Eq. (33); [Li, Chen & Ren (2022)](/sources/li-2022.md) §4.2; [Liang et al. (2022)](/sources/liang-2022.md) §4.4 |
| $[0,1]$ | $x=0.1$ | $1+0.2\sin(50x-25)$ | 0.18 | [Deng (2023)](/sources/deng-2023.md) App. A.6; [Huang et al. (2026)](/sources/huang-2026.md) §6.4 |
| $[-1,1]$ | $x=-0.8$ | $1+0.2\sin(5\pi x)$ | 0.36 | [Sousa & Scalo (2022)](/sources/sousa-2022.md) §5.1 ($\gamma$ not printed) |

The $[0,1]$ placement is the $[-5,5]$ one under $x\mapsto(x+5)/10$,
$t\mapsto t/10$ (velocities unchanged), since
$\sin(5x')=\sin(50x-25)$ for $x'=10x-5$ *(compiler check, not in the
sources)*. The $[0,10]$ placement of Fu (2021), Huang, Liang & Fu and Ji, Liang & Fu is the
shift $x\mapsto x+5$. Ye et al., Bezgin et al., Li, Chen & Ren and
Liang et al. print $\sin(5x)$ without the shift, which
changes the phase of the incoming wave relative to the shock *(compiler
check, not in the sources)*. Sousa & Scalo's placement contracts
$[-5,5]$ by a factor 5: the shock position $-0.8$ and the final time
$0.36=1.8/5$ follow the contraction, but the contracted perturbation
would be $\sin(25x)$, while they print $\sin(5\pi x)$, a wavenumber
$5\pi\approx15.7$ instead of 25, i.e. five wavelengths on the tube
instead of about eight *(compiler check, not in the sources)*. Their run
is therefore a related problem with a longer incoming wave, not a
rescaling of the common data. Their left state is the same Mach 3
post-shock state of Rankine–Hugoniot with $\gamma=1.4$ *(compiler
check, not in the sources)*.

### Grids and references

| Source | Points | Reference | Scheme compared |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) | 200 | WENO5-JS, 2000 | [TENO-AA](/methods/adaptive-teno.md) vs [WENO-CU6](/methods/weno-cu6.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) | 200 | WENO5-JS, 2000 | [TENO-THINC](/methods/teno-thinc.md) vs WENO5-Z, TENO5; CFL 0.4 vs 0.6 |
| [Ye et al. (2022)](/sources/ye-2022.md) | 200 | WENO5-JS, 2000 | [AFTENO](/methods/afteno.md), TENO, AFWENO |
| [Li et al. (2022)](/sources/li-2022-b.md) | 200 | WENO7-Z, 4000 | [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) | 201, CFL 0.5 | WENO-Z, 20001 | [WENO-Z+M](/methods/weno-z-plus.md) vs WENO-Z+, WENO-IS-I, WENO-Z9 |
| [Wang et al. (2023)](/sources/wang-2023-b.md) | 200 | OLD scheme, $\Delta x=1/160$ | [A-WENO](/methods/alternative-weno.md) with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) | 400, $\mathbb P^3$ | LLF, 300,000 | [OEDG](/methods/oedg.md), data scaled by $\lambda\in\{1,0.01,100\}$ |
| [Deng (2023)](/sources/deng-2023.md) | 400 | — | [ROUND](/methods/round-scheme.md), NewWENO |
| [Huang et al. (2026)](/sources/huang-2026.md) | 400 | WENO5-JS, 2000 | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md) |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.3 | specifications deferred to an earlier paper | — | [affine-invariant WENO-Z/D](/methods/affine-invariant-weno.md) |
| [Fu (2023)](/sources/fu-2023.md) §3.7 | review: TCNS6 vs seventh- and ninth-order WCNS-Z | — | — |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) | 400 cells, CFL 0.6 | FD WENO5, 8000 | moment-based [multi-resolution HWENO](/methods/hermite-weno.md) with modified first moments (HWENO6-M5-I) vs HWENO6 |
| [Pazner (2021)](/sources/pazner-2021.md) | 512 DOFs, $N=0,1,3,7$ ($N=7$ on 64 elements) | $N=0$, 20,000 elements | sparse IDP DG with subcell [convex limiting](/methods/convex-limiting.md) |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) | 200 | same scheme, 2000 | ninth-order central scheme with adaptive [artificial dissipation](/methods/artificial-viscosity.md), with and without the Bhagatwala–Lele factor in its shock sensor |
| [Wang et al. (2021)](/sources/wang-2021.md) | 200, CFL 0.6 | WENO-JS5, 20,000 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5) vs the original multi-resolution WENO5, [WENO-AO](/methods/weno-ao.md)(5,3) and WENO-JS5 |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) | 400, 800, CFL 0.6 | — | [WENO3-NN](/methods/learned-weno-weights.md) vs WENO3-JS, WENO3-Z, WENO3-N, WENO5-JS, WENO5-Z |
| [Hiejima (2022)](/sources/hiejima-2022.md) | 201, 401 ($\times21\times21$), RK4 at CFL 0.8 | WCNS-JS fifth order, 2000 | [WCNS](/methods/weighted-compact-nonlinear-scheme.md) with JS and TENO-type weights, interpolation orders 5–11 |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) | $\mathbb P_4$, 100 elements | exact-Godunov solver, highly resolved | [artificial viscosity](/methods/artificial-viscosity.md) from the temporal residual, $c_\mu=5$ |
| [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) | $\mathbb P_3$, 100 and 200 elements | exact-Godunov solver, highly resolved | flux reconstruction with [entropy filtering](/methods/entropy-filtering.md) |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) | 200 elements; fixed-DOF series across degrees | — | nodal DG with ANN-predicted artificial viscosity |
| [Sousa & Scalo (2022)](/sources/sousa-2022.md) | grid series, $\delta t=10^{-5}$ | same scheme (quasi-spectral viscosity), 4096 | [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md) vs localized artificial diffusion |
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) | 200, zero-gradient boundaries | WENO-JS, 2000 | TENO-M6 and TENO-M8 ([TENO](/methods/targeted-eno.md) with stencil extension) vs TENO6, TENO8, [WENO-CU6](/methods/weno-cu6.md), WENO-JS, WENO7, WENO9 |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) | 200, CFL 0.4 | WENO5-JS, 2000 | five-point TENO with a new [scale sensor](/definitions/scale-sensor.md) vs [TENO5-A](/methods/adaptive-teno.md), TENO5, WENO5-Z |
| [Li, Chen & Ren (2022)](/sources/li-2022.md) | 200, low-storage RK4 at CFL 0.6 | WENO-Z, 2000 | MDAD-HY ([MDCD](/methods/mdcd-scheme.md)-type hybrid with adaptive dissipation) vs MDCD-HY, TENO-HY, WENO-Z |
| [Liang et al. (2022)](/sources/liang-2022.md) | 200, CFL 0.4 | WENO5-JS, 2000 | low-dissipation discontinuity-resolving TENO ([TENO-THINC](/methods/teno-thinc.md) family) vs TENO5-THINC, TENO5, WENO5-Z |
| [Ji, Liang & Fu (2022)](/sources/ji-2022.md) | 18,282 triangles, $h\approx1/20$ | 1D FD WENO5-JS, 2000 | unstructured finite-volume TENO3–6 vs [CWENO](/methods/cweno.md)5/6 |
| [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) | 100 elements, static $N=5$ or $p$-adaptive $N\in[2,5]$ | second-order FV, fine mesh | [$p$-adaptive DG](/methods/hp-adaptation.md) with FV subcells, $N_{\mathrm{FV}}=6$ or 11 |

## Findings across sources

**Short-wave resolution.** The sources read the amplitude of the
post-shock short waves as the measure of dissipation, and each new
scheme below improves on its baseline: TENO-AA over WENO-CU6 in amplitude and
phase (Fu 2021, Fig. 4); WENO-ZN over WENO-JS and WENO-Z (Li et al.,
Fig. 5); WENO-Z+M better than WENO-Z+ at the discontinuity and better
than WENO-IS-I and WENO-Z9 on the high-frequency waves (Luo & Wu, Fig.
10); the adaptive-diffusion flux reducing dissipation behind the shock
(Wang et al. 2023, Fig. 2); AFTENO and TENO best on the entropy-wave
amplitude (Ye et al., Fig. 4); TENO-THINC similar to TENO5 and slightly
better than WENO5-Z, with a negligible CFL effect (Takagi et al., Figs.
6–7); WENO3-NN "significantly smeared out" against ROUND and LD-ROUND,
LD-ROUND best (Huang et al., Fig. 9). Fu (2023) reports that TCNS6
beats seventh- and ninth-order WCNS-Z on this problem. Li, Shu & Qiu
find that modifying the first moments in troubled cells gives "much
better resolutions" than the unmodified HWENO6 (Fig. 3.4, comment
p. 31). At fixed 512 degrees of freedom Pazner resolves the smooth
post-shock structures better with higher polynomial degree, while some
peak clipping of the post-shock oscillations remains (Fig. 8). Wang et
al. (2021) rank their New WENO5 above the original multi-resolution
WENO5 and WENO-JS5, with WENO-AO(5,3) best, at nearly equal cost (0.2184 s
and 283 steps against 0.2028 s for WENO-JS5, 0.2340 s for WENO-AO5 and
0.2808 s for the original scheme; Fig. 5.7). Bezgin et al.'s three-point
WENO3-NN on 400 points is comparable to WENO3-JS on 800 and approaches
WENO5-JS on 800, with WENO5-Z best overall (§4.4, Fig. 12). Among the
TENO variants, Hong, Ye & Ye find TENO6, TENO-M6 and WENO-CU6 resolving
the entropy waves alike and much better than WENO-JS, and TENO8 and
TENO-M8 markedly better than WENO7 and WENO9 (§5.4, Fig. 12); Huang,
Liang & Fu find TENO5-A and their scale-sensor scheme better than
WENO5-Z and TENO5 on the high-wavenumber fluctuations, their scheme
best preserving the velocity amplitude on $x\in[4.3,5.6]$ (§4.5,
Fig. 8); Liang et al. find their scheme similar to TENO5-THINC and
slightly better than WENO5-Z and TENO5 on shocklets and short waves
(§4.4, Fig. 10); Li, Chen & Ren find MDAD-HY resolving the crests and
troughs best (§4.2, Fig. 15). On unstructured triangles Ji, Liang &
Fu find the entropy waves better resolved with increasing order, and
TENO5/6 better than CWENO5/6 of the same order (§5.5, Figs. 8–10).
Mossier, Beck & Munz find their $p$-adaptive DG closer to the
reference behind the shock than the static $N=5$ run, with a mean of
70.8 degrees of freedom per element against 216 (§8.5, Figs. 10–11).

**Order without weights does not resolve the waves.** Hiejima's WCNS
with Jiang–Shu weights shows "no difference based on the accuracy"
between interpolation orders 5 and 11 and fails to capture the small
post-shock waves, which he attributes to the dissipation of the JS
weights; with TENO-type weights the waves are resolved, the eleventh
order matching the ninth, and on 401 points the results are "very
similar to the exact solution" (§3.3, Figs. 4–5).

**Element methods and shock-capturing devices.** Dzanic, Trojak &
Witherden find good agreement with the reference at $\mathbb P_4$ on
100 elements; their residual-based indicator separates the shocks from
the oscillatory density field, with a magnitude roughly proportional to
the shock strength (§5.2.2, Fig. 5). Yu & Hesthaven report sharp,
oscillation-free shocks on 200 elements; at a fixed number of DOFs the
accuracy decreases with the polynomial degree on coarse meshes, which
they attribute to the network underestimating smoothness on coarse
meshes, while the degrees nearly coincide on finer meshes (§5.3.2,
Figs. 9–11), the opposite of Pazner's fixed-DOF trend with convex
limiting. Dzanic & Witherden run $\mathbb P_3$ on 100 and 200 elements
against the same kind of reference (§5.1.2). Sousa & Scalo find
quasi-spectral viscosity and localized artificial diffusion recovering
the trailing density oscillations alike, the former with a sharper
shock, especially in velocity, and monotone convergence from very
coarse grids (§5.1, Fig. 5).

**Entropy waves under scalar artificial dissipation.** Sciacovelli et
al. find pressure and velocity in agreement with the reference, with
bounded oscillations near the shock, but density and entropy more
strongly damped behind the shock; they attribute this to their scalar
(spectral-radius) dissipation acting equally on acoustic and entropic
fields. The Bhagatwala–Lele dilatation factor of their sensor strongly
improves the entropy-wave resolution by suppressing spurious activation
of Jameson's pressure sensor; it makes no appreciable difference on the
[shock tubes](/benchmarks/sod-and-lax-shock-tubes.md) (§4.3, Fig. 4).

**Oscillations at shocklets.** Fu (2021) reports density and velocity
oscillations of WENO-CU6 near the shocklets, which TENO-AA avoids;
Hong, Ye & Ye likewise see WENO-CU6 overshoot near the valleys (§5.4).
Huang, Liang & Fu report slight overshoots of TENO5-A around $x=3.25$,
which they attribute to Ren's sensor misjudging critical points (§4.5,
Fig. 8).

**Discontinuity detectors over time.** Li, Chen & Ren plot the time
history of their hybrid scheme's detector: only their new detector
separates the entropy-wave fluctuations from the shocklets throughout
the run (§4.2, Fig. 16); see [troubled-cell
indicators](/definitions/troubled-cell-indicator.md).

**Parameter sensitivity on triangles.** Ji, Liang & Fu sweep the CWENO
central-stencil linear weight $d'_K\in\{10^3,10^4,10^7,10^{15}\}$
(page-local symbol): larger values resolve the waves better but, they
state, lose robustness (not shown here; the double Mach reflection
"typically fails"), so they fix $10^4$ for all orders (§2.4, §5.5,
Fig. 11).

**Scale invariance.** Peng, Sun & Wu multiply the data by a factor
$\lambda\in\{1,0.01,100\}$ (page-local symbol); OEDG is exactly scale-invariant and
oscillation-free, while the earlier OFDG oscillates or smears depending
on $\lambda$ (Fig. 5). Wang & Don run the problem with affine-invariant
weights and $\epsilon=10^{-12}$ and find the Z- and D-type weights
essentially identical and non-oscillatory (Fig. 7). See
[scale invariance](/properties/scale-invariance.md).

## Titarev–Toro variant

A weaker shock enters a high-frequency, low-amplitude wave:
$(\rho,v,p)=(1.515695,\ 0.523346,\ 1.805)$ behind the shock and
$(1+0.1\sin(20\pi x),\,0,\,1)$ ahead of it, shock at $x=-4.5$ on
$[-5,5]$, $t=5$. [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.3 use
1001 points, CFL 0.5, reference WENO-Z with 20001 points;
[Fu (2021)](/sources/fu-2021.md) §5.4 use the shifted placement on
$[0,10]$, 1000 points, CFL 0.1, reference WENO5-JS with 5000 points;
[Fu (2023)](/sources/fu-2023.md) Fig. 9 reproduces 1000-point runs of
finite-volume TENO5, the low-dissipation TENO5-LFV with a switched
Riemann solver, and WENO5-Z-FV. [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md)
§5.3, Eq. (5.3), run it with second-order MUSCL and a second-order TVD
Runge–Kutta stepper on 1000 cells, CFL 0.9, $t=5$, comparing
[HLL-family](/methods/hll-riemann-solvers.md) solvers: HLLE is highly
damped, their RHLLEM-LD more accurate on the high-frequency wave
(Fig. 5.3). They print the perturbation as $\sin(20x)$ and call the
shock Mach 1.1; see the shared printed variant below.

The variant separates negative from positive dissipation. Luo & Wu
show that WENO-Z+ resolves the high-frequency waves somewhat better
than WENO-Z+M but **amplifies** the smooth waves ahead of and behind
the shock, a signature of negative nonlinear dissipation; WENO-Z+M is
free of it and much better than WENO-Z9 (Fig. 11). They recall that
the original WENO-Z+ chose the factor of its extra weight term,
$\Delta x^{2/3}$, on this test, as a compromise between magnified waves
with $\Delta x^{1/2}$ and attenuated ones with $\Delta x$ (§2.3); see
[WENO-Z+](/methods/weno-z-plus.md).

The Rankine–Hugoniot conditions for $M=1.3$ into $(1,0,1)$, $\gamma=1.4$,
give $(\rho,v,p)=(1.515695,\ 0.523346,\ 1.805)$, and for $M=3$ the exact
state above *(compiler check, not in the sources)*.

## Two-medium variant

[Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 3 keep the
$[-5,5]$ data but give the pre-shock gas $\gamma=1.666666$, the
post-shock gas $\gamma=1.4$, so that a material interface starts at
$x=-4$ together with the shock; $N=300$, reference $N=2000$, $T=1.8$.
Their conservative two-medium finite-difference scheme (alternative-flux
[A-WENO](/methods/alternative-weno.md) on primitive variables, a
[level set](/methods/level-set-method.md) and an interface flux) and a
conservative-variable WENO-JS scheme are "nearly the same", and
comparable to an earlier DG computation with more degrees of freedom
(Fig. 7). With different $\gamma$ on the two sides the initial jump is
a two-material Riemann problem, not a single shock: the printed left
state is the Rankine–Hugoniot state of a Mach 3 shock only for
$\gamma=1.4$ on both sides *(compiler check, not in the sources)*.

[Bai & Li (2022)](/sources/bai-2022.md) §3.1.5, Eq. (35), run a
second two-medium version in a two-dimensional strip
$[-5,5]\times[0,1]$: the Mach 3 post-shock state with $\gamma=1.4$
for $x\le-4$ and $(1+0.2\sin5x,\ 0,\ 1)$ with $\gamma=1.89$ ahead, to
$t=1.8$, with their sharp-interface ghost-fluid cut-cell DG and a WENO
limiter; reference $\mathbb P^2$ on 2000 elements. At 200 elements the
accuracy grows with the degree ($\mathbb P^0$, $\mathbb P^1$,
$\mathbb P^3$); at equal DOFs (800 $\mathbb P^0$, 400 $\mathbb P^1$, 200
$\mathbb P^3$ elements) $\mathbb P^1$ and $\mathbb P^3$ agree except near
the material interface and beat $\mathbb P^0$ (Fig. 14). The remark on
Zheng et al.'s initial jump applies here as well.

## Radial extension

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) §4
(p. 23, arXiv v4) run a cylindrical version on triangles: the Mach 3
post-shock density $3.857143$ and pressure $10.\bar3$ for $r\le1$
with a radial velocity, $(1+0.5\sin(5r),0,0,1)$ for $1<r<4$ and the
constant $(1+0.5\sin20,0,0,1)$ for $r\ge4$, to $t=1.8$, with
deferred-correction residual distribution and their
[entropy correction term](/methods/entropy-correction-term.md)
(Fig. 6). The perturbation amplitude is $0.5$, not $0.2$. The radial
velocity is printed as $\sqrt{2.629\rho_0}\,x/r$, $\sqrt{2.629\rho_0}\,y/r$;
the Rankine–Hugoniot speed consistent with their own density and
pressure is $2.629369$, which the printed root does not give for
$\rho_0=1$ ($1.621$) or $\rho_0=3.857143$ ($3.184$) *(compiler check,
not in the sources)*, so the printed velocity is a slip whose intended
value the paper does not show.

## Related variants

- **Shared printed variant ($\sin(20x)$, "Mach 1.1").**
  [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 2, called
  "shock–entropy wave (Shu–Osher)", print the post-shock state
  $(1.51695,\ 0.523346,\ 1.805)$ for $x<-4.5$ and
  $(1+0.1\sin(20x),0,1)$ ahead, on $[-5,5]$, $t=5$, $\Delta x=1/80$,
  reference $\Delta x=1/400$, attribute it to Shu & Osher and call it a
  Mach 1.1 shock. Luo & Wu (Eq. (15)) and Fu (2021) (Eq. (36)) print the
  same problem with density $1.515695$ and perturbation
  $\sin(20\pi x)$, so Chertock et al.'s $1.51695$ is a dropped digit and
  their $\sin(20x)$ a different wavenumber. Their state is that of a
  Mach 1.3 shock, not 1.1: Rankine–Hugoniot at $M=1.1$ gives
  $(1.1691,\ 0.1882,\ 1.245)$ *(compiler check, not in the sources)*. Their LCD central-upwind scheme is
  "substantially more accurate" than the earlier one on $x\in[0,3]$
  (Fig. 5.2).
  [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.3, Eq. (5.3), print
  the same pair: the full-digit post-shock state
  $(1.515695,\ 0.523346,\ 1.805)$ for $-5\le x\le-4.5$,
  $(1+0.1\sin(20x),0,1)$ ahead, and "a right-traveling shock wave with
  Mach 1.1", attributing the problem to Titarev & Toro. Two sources thus
  share the $\sin(20x)$ data and the Mach 1.1 label against Luo & Wu's and
  Fu's $\sin(20\pi x)$; the printed state is the Mach 1.3 state in all
  four (Rankine–Hugoniot at $M=1.3$ gives
  $(1.515695,\ 0.523346,\ 1.805)$, at $M=1.1$
  $(1.169082,\ 0.188239,\ 1.245)$ *(compiler check, not in the
  sources)*). The two wavenumbers are different problems: ahead of the
  shock $\sin(20x)$ has about 30 wavelengths on $[-4.5,5]$ and about 31
  cells per wavelength on Hu et al.'s 1000 cells, $\sin(20\pi x)$ has 95
  wavelengths and 10 cells per wavelength *(compiler check, not in the
  sources)*. Neither source can decide which wavenumber Titarev & Toro
  used; only a reading of their paper would.
- [Ye et al. (2022)](/sources/ye-2022.md) §4.5, after an earlier
  study, add a long, small-amplitude shock–entropy-wave test: the Mach 3
  post-shock state on $0\le x<0.5$ and
  $(\exp(-\varepsilon_{\mathrm s}\sin(k(x-19.5))),0,1)$ on $0.5\le x<20$ with
  $\varepsilon_{\mathrm s}=0.01$, $k=-13$ (page-local symbols), $N=1500$,
  $t=5$, reference WENO-JS with $N=10000$. They find the weight
  exponent $q=2$ better than $q=6$ on it (Fig. 5).

## Qualifications

- Takagi et al. print the data on $-5\le x\le5$ but write "the
  computational domain is $[0,10]$" (§4.4).
- Peng, Sun & Wu do not state the domain of their run.
- Li, Shu & Qiu print $\gamma$ only for their double Mach reflection,
  not for this problem; Sciacovelli et al. print the post-shock
  pressure as $10.33333$.
- The resolution claims are visual comparisons of zoomed density
  profiles; no source reports an error norm against its reference.
- Ji, Liang & Fu print the domain of their strip as
  $[0,2]\times[0,10]$ while the data are defined for $0\le x\le10$, the
  factors written with $x$ second (§5.5).
- Hong, Ye & Ye and Huang, Liang & Fu call the shock "Mach 3"; Li, Chen &
  Ren and Liang et al. do not state boundary conditions.
- Hiejima runs the one-dimensional problem in a three-dimensional
  code on $N_x\times21\times21$ points and prints the post-shock pressure
  as $31/3$.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.4, Figs. 4–5 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.4, Figs. 6–7.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.4–4.5, Eqs. (44)–(45), Figs. 4–5.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.3.2, Eq. (40), Fig. 5.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §2.3; §5.2.2–5.2.3, Eqs. (14)–(15), Figs. 10–11.
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 2, Fig. 2.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.8, Fig. 5 (arXiv v1).
- [Deng (2023)](/sources/deng-2023.md) — App. A.6, Figs. 15c, 22, 32.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.4, Fig. 9.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.3, Fig. 7.
- [Fu (2023)](/sources/fu-2023.md) — §3.6, Fig. 9; §3.7.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.1, Ex. 2, Fig. 5.2 (arXiv v2).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — Ex. 3.6, Fig. 3.4; comment p. 31 (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — §5.2.2, Fig. 8 (arXiv v1).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §4.3, Eq. (42), Fig. 4 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.4a, Fig. 5.7.
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 3, Fig. 7.
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.4, Eq. (33), Fig. 12.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §3.3, Eq. (28), Figs. 4–5.
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.2.2, Fig. 5 (arXiv v2).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.2 (arXiv v3).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.3.2, Figs. 9–11.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §5.1, Fig. 5 (arXiv v2).
- [Bai & Li (2022)](/sources/bai-2022.md) — §3.1.5, Eq. (35), Fig. 14.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §4, p. 23, Fig. 6 (arXiv v4).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.4, Fig. 12.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.3, Eq. (5.3), Fig. 5.3.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.5, Fig. 8 (arXiv v1).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §2.4, §5.5, Figs. 8–11 (preprint).
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.2, Figs. 15–16.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.4, Fig. 10.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §8.5, Figs. 10–11.
