---
type: Benchmark
title: "Shu–Osher shock–entropy-wave problem"
description: "One-dimensional Euler benchmark of a Mach 3 shock running into a sinusoidal density (entropy) wave, with its Titarev–Toro high-frequency variant; the bundle's most widely run test of how well a shock-capturing scheme resolves the short waves generated behind a shock without oscillating at the shocklets."
status: established
aliases: [Shu–Osher problem, shock–density wave interaction, shock–entropy wave interaction, Titarev–Toro problem]
tags: [benchmark, low-dissipation, weno, teno]
timestamp: 2026-10-23T11:06:00Z
---

# Shu–Osher shock–entropy-wave problem

A Mach 3 shock moves to the right into gas at rest whose density
carries a small sinusoidal perturbation at uniform pressure, i.e. an
entropy wave. Passing through the shock, the wave is compressed into a
band of short, steep density oscillations, followed by weak shocklets.
A dissipative scheme damps the short waves; an oscillatory one creates
spurious waves near the shocklets. The problem is the most widely run
one-dimensional resolution test in the bundle: forty-six sources run it
or a variant (one of them a review reproducing earlier figures), in six
placements of one set of data, plus a high-frequency variant attributed
to Titarev & Toro, a Mach 10 variant, two-medium variants and a radial
two-dimensional extension.

## Common data and its placements

With $\gamma=1.4$, the post-shock state of a Mach 3 shock moving into
$(\rho,v,p)=(1,0,1)$ is

$$
(\rho,v,p)_{\mathrm L}=\Big(\tfrac{27}{7},\ \tfrac{4\sqrt{35}}{9},\ \tfrac{31}{3}\Big)
\approx(3.857143,\ 2.629369,\ 10.333333),
$$

as printed in exact form by [Li et al. (2022b)](/sources/li-2022-b.md)
Eq. (40) and [Ye et al. (2022)](/sources/ye-2022.md) Eq. (44), and in
decimals by the others (Rankine–Hugoniot with $M=3$ reproduces these
values *(compiler check, not in the sources)*). The pre-shock state is
$(1+0.2\sin(5x),\,0,\,1)$ in the coordinates of $[-5,5]$, and the run
ends at $t=1.8$.

| Placement | Shock position | Perturbation | Final time | Sources |
|---|---|---|---|---|
| $[-5,5]$ | $x=-4$ | $1+0.2\sin(5x)$ | 1.8 | [Li et al. (2022b)](/sources/li-2022-b.md) §4.3.2; [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.2; [Wang et al. (2023b)](/sources/wang-2023-b.md) Example 2; [Takagi et al. (2022)](/sources/takagi-2022.md) §4.4; [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.8 (domain not stated); [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.6; [Pazner (2021)](/sources/pazner-2021.md) §5.2.2; [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) §4.3, Eq. (42); [Wang et al. (2021)](/sources/wang-2021.md) Example 5.4a; [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.2.2; [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) §5.1.2; [Hiejima (2022)](/sources/hiejima-2022.md) §3.3, Eq. (28); [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.3.2; [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.4; [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.5; [Zhou et al. (2023)](/sources/zhou-2023.md) §5.2, Eq. (37); [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 8; [Wang et al. (2023c)](/sources/wang-2023-c.md) Example 4.3; [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) §8.2 (interface printed at $x=4$, see Qualifications); [Liu et al. (2023b)](/sources/liu-2023-b.md) §5.2 (strip $[-5,5]\times[-0.1,0.1]$ on triangles); [Jiang et al. (2024)](/sources/jiang-2024.md) §5.1.1 (Lagrangian particles); [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.5 (strip $[-5,5]\times[-0.166,0.166]$ on triangles); [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) Ex. 3.5; [Naudet & Zahr (2024)](/sources/naudet-2024.md) §5.3.2 (to $T=2$, supersonic inlet at $x=-5$, solid wall at $x=5$) |
| $[-4.5,4.5]\times[0,1]$ | $x=-4$ | $1+0.2\sin(5x)$ | 1.8 | [Maltsev et al. (2023)](/sources/maltsev-2023.md) §3.3 (strip on triangles, periodic in $y$) |
| $[0,10]$ | $x=1$ | $1+0.2\sin(5(x-5))$ | 1.8 | [Fu (2021)](/sources/fu-2021.md) §5.4; [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.5; [Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.5 (two-dimensional strip on triangles); [Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.4, Eq. (41) (likewise) |
| $[0,10]$ | $x=1$ | $1+0.2\sin(5x)$ as printed | 1.8 | [Ye et al. (2022)](/sources/ye-2022.md) §4.4; [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.4, Eq. (33); [Li, Chen & Ren (2022)](/sources/li-2022.md) §4.2; [Liang et al. (2022)](/sources/liang-2022.md) §4.4; [Qin et al. (2023)](/sources/qin-2023.md) §3.4.3; [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.3 |
| $[-5,5]$ | $x=-4$ | $1+0.2\sin(5(x-5))$ as printed | 1.8 | [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.11; [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.5 |
| $[0,1]$ | $x=0.1$ | $1+0.2\sin(50x-25)$ | 0.18 | [Deng (2023)](/sources/deng-2023.md) App. A.6; [Huang et al. (2026)](/sources/huang-2026.md) §6.4 |
| $[-1,1]$ | $x=-0.8$ | $1+0.2\sin(5\pi x)$ | 0.36; not stated | [Sousa & Scalo (2022)](/sources/sousa-2022.md) §5.1 ($\gamma$ not printed); [Kolluru et al. (2024)](/sources/kolluru-2024.md) §3.4, Eq. (9e) (amplitude 0.2, wavenumber $5\pi$, supersonic inflow at $x=-1$, non-reflecting outflow at $x=1$; arXiv v2) |
| $[-5,5]$ | $x=-4$ | $1+0.2\sin(5\pi x)$ as printed | 1.8 | [Tang (2024)](/sources/tang-2024.md) §4.3, Eq. (29) |

The $[0,1]$ placement is the $[-5,5]$ one under $x\mapsto(x+5)/10$,
$t\mapsto t/10$ (velocities unchanged), since
$\sin(5x')=\sin(50x-25)$ for $x'=10x-5$ *(compiler check, not in the
sources)*. The $[0,10]$ placement of Fu (2021), Huang, Liang & Fu and Ji, Liang & Fu is the
shift $x\mapsto x+5$. Ye et al., Bezgin et al., Li, Chen & Ren and
Liang et al. (and Qin et al., Zhao et al.) print $\sin(5x)$ without the shift, which
changes the phase of the incoming wave relative to the shock *(compiler
check, not in the sources)*; the two Chamarthi papers print the shifted
perturbation $\sin(5(x-5))$ on the unshifted domain $[-5,5]$, the
opposite mismatch. Both mismatches shift the phase by $25$ rad, which is
$25-8\pi\approx-0.13$ rad modulo $2\pi$, so the incoming wave is moved by
about $0.03$ in $x$, a small fraction of its wavelength
$2\pi/5\approx1.26$ *(compiler check, not in the sources)*. Sousa & Scalo's placement contracts
$[-5,5]$ by a factor 5: the shock position $-0.8$ and the final time
$0.36=1.8/5$ follow the contraction, but the contracted perturbation
would be $\sin(25x)$, while they print $\sin(5\pi x)$ (as do Kolluru et
al. on the same placement), a wavenumber
$5\pi\approx15.7$ instead of 25, i.e. five wavelengths on the tube
instead of about eight *(compiler check, not in the sources)*. Their run
is therefore a related problem with a longer incoming wave, not a
rescaling of the common data. Their left state is the same Mach 3
post-shock state of Rankine–Hugoniot with $\gamma=1.4$ *(compiler
check, not in the sources)*. Tang prints the same perturbation
$\sin(5\pi x)$ on the uncontracted $[-5,5]$,
with the common shock position and final time: a wavenumber $\pi$ times
the common one, about 22 wavelengths ahead of the shock and about 8
cells per wavelength on the 200 cells *(compiler check, not in the
sources)*. The text does not say whether this is what was run or a
slip for $\sin(5x)$.

### Grids and references

| Source | Points | Reference | Scheme compared |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) | 200 | WENO5-JS, 2000 | [TENO-AA](/methods/adaptive-teno.md) vs [WENO-CU6](/methods/weno-cu6.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) | 200 | WENO5-JS, 2000 | [TENO-THINC](/methods/teno-thinc.md) vs WENO5-Z, TENO5; CFL 0.4 vs 0.6 |
| [Ye et al. (2022)](/sources/ye-2022.md) | 200 | WENO5-JS, 2000 | [AFTENO](/methods/afteno.md), TENO, AFWENO |
| [Li et al. (2022b)](/sources/li-2022-b.md) | 200 | WENO7-Z, 4000 | [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) | 201, CFL 0.5 | WENO-Z, 20001 | [WENO-Z+M](/methods/weno-z-plus.md) vs WENO-Z+, WENO-IS-I, WENO-Z9 |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) | 200 | OLD scheme, $\Delta x=1/160$ | [A-WENO](/methods/alternative-weno.md) with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) |
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
| [Zhou et al. (2023)](/sources/zhou-2023.md) | 200, CFL 0.4, HLLC, TVD-RK3 | WENO5, 4000 | six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) with minimum dispersion and adaptive dissipation (WCNS-SA) vs WCNS-LD and ONL6 on the same stencil |
| [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) App. A.2 | 200, extrapolation boundaries; data "provided by Jiang and Shu", final time printed $t/t_0=1.3$ | 2000-point run | [WENO-Z](/methods/weno-z.md)3/5/7, TENO5, [TENO-A5](/methods/adaptive-teno.md) in [URANOS](/software/uranos.md) |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) | 300 | — | [gradient-based](/methods/gradient-based-reconstruction.md) MEG6, MIG4 vs TENO5 (arXiv v2) |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) | 200 | MP5, 2000 | MEG7 vs seventh-order mapped WCNS7M (arXiv v1) |
| [Qin et al. (2023)](/sources/qin-2023.md) | two blocks: 250 on $[0,5)$, 500 on $[5,10]$ | single-domain WCNS-MR, 6000 | multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md) with [shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md) at the block interface |
| [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) | 100 elements, static $N=5$ or $p$-adaptive $N\in[2,5]$ | second-order FV, fine mesh | [$p$-adaptive DG](/methods/hp-adaptation.md) with FV subcells, $N_{\mathrm{FV}}=6$ or 11 |
| [Zhong et al. (2023)](/sources/zhong-2023.md) | 200, CFL 0.5 | WENO-JS, 10000 | fifth-order FV IMWENO-P (mirror-symmetric smoothness indicators) vs WENO-JS, WENO-Z, WENO-NS, WENO-P, MWENO-P |
| [Wang et al. (2023c)](/sources/wang-2023-c.md) | 400, CFL 0.6 | WENO-JS, 20000 | hybrid multi-resolution [WCNS](/methods/weighted-compact-nonlinear-scheme.md) vs MR-WCNS, WENO-JS |
| [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) | 200, CFL 0.4 and 0.8; non-reflecting ends | — | eighth-order compact [gas-kinetic scheme](/methods/gas-kinetic-scheme.md) vs the authors' earlier compact scheme at CFL 0.4 (arXiv v1) |
| [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) | $N=3$, $N_{\mathrm{el}}=64,128$ elements, CFL 0.5 | fifth-order WENO, 25000 cells | entropy-stable DGSEM with positivity-only elementwise blending, bound relaxation $\zeta_{\mathrm r}=0.1,0.5$ (their $\zeta$; arXiv v2) |
| [Liu et al. (2023b)](/sources/liu-2023-b.md) | triangles, $h=1/40$ | — | implicit fourth-order [RBF differential-quadrature](/methods/rbf-differential-quadrature.md) FV and LSFD-FV with the PEEB limiter (tolerance $100h^{1.5}$) vs a second-order FV scheme |
| [Ji, Liang & Fu (2023)](/sources/ji-2023.md) | 200 cells ("triangular mesh with $h\approx1/20$") | 1D WENO5-JS, 2000 | dual-stencil-selection TENO4-D–TENO7-D vs CWENO6/7, HLL, SSP-RK3 at CFL 0.4 |
| [Tang (2024)](/sources/tang-2024.md) | 200, CFL 0.5, global LF splitting | WENO-JS, 4000 | [TENO-AZ](/methods/adaptive-teno.md) vs TENO-Z, TENO-A, TENO-LAD |
| [Jiang et al. (2024)](/sources/jiang-2024.md) | particle spacing $\Delta x_0=0.01$, serial CPU | WENO-Z, 5000 | Lagrangian weighted-least-squares particles with WENO-Z-type pair states (LWLS-WENO-Z) |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) | triangles, $301\times11$ vertices, CFL 0.6 | FD WENO5, 2000 | ALW-MR-WENO-3/4/5 vs [MR-WENO](/methods/multi-resolution-weno.md) |
| [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) | 300 points or cells, CFL 0.6 | WENO-JS5, 2000 | GMR-WENO3/5/7 vs MR-WENO, finite differences and finite volumes |
| [Kolluru et al. (2024)](/sources/kolluru-2024.md) | Chebyshev with a mapping, $N_x=615$ | HyPar characteristic WENO5, 8000 | spectral relaxation with Fejér–Korovkin and de la Vallée-Poussin kernels ([artificial and spectral viscosity](/methods/artificial-viscosity.md)) |
| [Naudet & Zahr (2024)](/sources/naudet-2024.md) | five space-time slabs, 20 spatial elements, quadratic simplices, then refinement | second-order FV (superbee), over $5\times10^4$ cells, adaptive RK4 | space-time [implicit shock tracking](/methods/implicit-shock-tracking.md) (HOIST) |
| [Maltsev et al. (2023)](/sources/maltsev-2023.md) | triangles, $h=0.070$, about 13,000 elements | 1D WENO5, 10,000 points | hybrid DG–FV(CWENOZ) of orders 3–5 with MOOD$^{\mathrm R}$ (limited and extended bounds) and the shock detector ($C_k=1.5$), vs pure FV |

## Findings across sources

**Short-wave resolution.** The sources read the amplitude of the
post-shock short waves as the measure of dissipation, and each new
scheme below improves on its baseline: TENO-AA over WENO-CU6 in amplitude and
phase (Fu 2021, Fig. 4); WENO-ZN over WENO-JS and WENO-Z (Li et al.,
Fig. 5); WENO-Z+M better than WENO-Z+ at the discontinuity and better
than WENO-IS-I and WENO-Z9 on the high-frequency waves (Luo & Wu, Fig.
10); the adaptive-diffusion flux reducing dissipation behind the shock
(Wang et al. 2023b, Fig. 2); AFTENO and TENO best on the entropy-wave
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
TENO5/6 better than CWENO5/6 of the same order (§5.5, Figs. 8–10);
their sequel finds TENO6-D and TENO7-D "much better" than CWENO6 and
CWENO7 on the high-wavenumber waves, and, by comparison with a figure
of another paper, similar to fourth- and fifth-order WENO-AO on the
finer $h=1/40$ (Ji, Liang & Fu 2023, §4.4, Figs. 7–8). Their times are
173.12 s (CWENO6), 211.01 s (CWENO7), 164.26 s (TENO6-D) and 196.57 s
(TENO7-D), "approximately the same", hardware not stated (Table 6).
Tang finds the TENO-AZ comparable to TENO-LAD and better than TENO-A
and TENO-Z (§4.3, Fig. 7), at 0.95 of TENO-Z's CPU time, against 1.15
for TENO-A and 1.35 for TENO-LAD (Table 5, average of 1000 runs). Jiang
et al.'s Lagrangian particle method captures the problem close to the
WENO-Z reference on 5000 points (§5.1.1, Fig. 6), although its observed
order on smooth data is only about 2.2–2.35 (see
[density-wave advection](/benchmarks/density-wave-advection.md)).
Mossier, Beck & Munz find their $p$-adaptive DG closer to the
reference behind the shock than the static $N=5$ run, with a mean of
70.8 degrees of freedom per element against 216 (§8.5, Figs. 10–11).

Chamarthi (2023b) finds MEG7 resolving the density extrema better than
WCNS7M (Fig. 7).

Zhong et al. find the highest resolution with IMWENO-P (Fig. 7), and
Wang et al. (2023c) both multi-resolution WCNS ahead of WENO-JS, with
their hybrid at 0.89 of WENO-JS's CPU time against 1.50 for the
original MR-WCNS (Fig. 4.5, Table 5.1). Zhao et al. use the problem for
the time step: their compact gas-kinetic scheme runs at CFL 0.8 as well
as 0.4, while their earlier compact scheme is shown at 0.4 (Fig. 6).
On triangles, Liu et al. (2023b) find their fourth-order schemes with
the PEEB limiter capturing the smooth extrema, the second-order scheme
more diffusive (Fig. 6).

**Switching in hybrid DG–FV.** Maltsev et al. find that at third order
the hybrid improves markedly on pure FV, while at higher order the pure
FV scheme agrees better with the reference than the hybrid with
sensitive indicators, because the solver falls back to FV more often;
the NAD criterion of MOOD flags erratically, the shock detector only the
shock region (§3.3, Figs. 8–9). Lin, Chan & Tomas's limited DG solutions
are close to the reference, with oscillations near the shocks reduced
by the larger relaxation factor $\zeta_{\mathrm r}$ (§8.2, Figs. 5–6).

Zhou et al. find WCNS-LD and WCNS-SA resolving the post-shock waves,
ONL6 damping them "considerably", and WCNS-LD overshooting in velocity
and pressure near the shocklets (§5.2, Fig. 11). De Vanna et al. (2023b)
find all five shock-capturing schemes of URANOS representing the flow
accurately, the waves adhering to the reference progressively as the
order rises and from WENO to TENO (App. A.2, Fig. 12).

**A shock through a block interface.** Qin et al. split the domain at
$x=5$ into two blocks with a 2:1 jump of spacing and pass the shock
through the interface with their one-sided nonlinear closures: the
transition is smooth at $t=1.0$ and $1.8$ against the single-domain
reference (Fig. 9). With unscaled smoothness indicators ($\lambda=1$ in
their notation) "the shock fails to cross the interface", as stated
without a figure; their scaled indicators ($\lambda=2$) are used
throughout. The interface costs nothing measurable: 376.14 s on one zone
against 375.44 s on two at 10000 points, serial on an AMD Ryzen7-5800H
(Table 13).

**Multi-resolution WENO of the Zhu group.** Lin & Zhu's two-stencil
ALW-MR-WENO on triangles gives results comparable to MR-WENO of the
same order (Case 3.5, Fig. 3.6); Zhang & Zhu state that their
single-stencil GMR-WENO "perform better" than MR-WENO on the
post-shock waves (Ex. 3.5, Figs. 3.9–3.10). Both judgements are visual.

**Spectral shock capturing.** Kolluru et al.'s spectral relaxation
needs a high-order kernel here: with the positive, low-order
Fejér–Korovkin kernel (parameters $(0.95,0.97)$) it "does not converge to
the correct solution" and loses the entropy-wave oscillations, while
the de la Vallée-Poussin kernel with $(1.14,0.95)$ resolves both the
shock and the fine structure (§3.4, Fig. 16). On their Burgers and
shock-tube tests, by contrast, the Fejér–Korovkin kernel gives the
oscillation-free solutions and the de la Vallée-Poussin kernel bounded
oscillations (see [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
and [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).

**Shock tracking with an error norm.** Naudet & Zahr track the main
shock in a first pass (five slabs, 160 quadratic space-time simplices in
the first slab, stopped at optimality tolerance $10^{-8}$ or 200 SQP
iterations), then refine uniformly and remove the known upstream region
(3184 to 1500 elements), and a final pass with adaptive refinement and
shock boundary conditions resolves the formation of the shocklets and
the post-shock oscillations (§5.3.2, Figs. 19–20). Against the fine
finite-volume reference at $T=2$ the relative $L^2$ error is
$3.97\times10^{-4}$ (Fig. 21).

**Order without weights does not resolve the waves.** Hiejima's WCNS
with Jiang–Shu weights shows "no difference based on the accuracy"
between interpolation orders 5 and 11 and fails to capture the small
post-shock waves, which Hiejima attributes to the dissipation of the JS
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

The two Chamarthi papers print $(1.515695,0.523346,1.805)$ for
$0\le x<0.5$ and $(1+0.1\sin(20\pi(x-5)),0,1)$ for $0.5\le x\le10$, on
$[0,10]$, 1000 points, $t=5$: the Titarev–Toro data shifted by 5
*(compiler check, not in the sources)*. [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 9 print
$(1.515695,\ 0.5233346,\ 1.80500)$ for $x<-4.5$ and
$(1+0.1\sin(20\pi x),0,1)$ ahead on $[-5,5]$, $t=5$, 900 cells,
reference WENO-JS on 10000: IMWENO-P gives the highest resolution, and
WENO-P "falsely amplifies the smooth waves in front of and closely
behind the main shock wave" (Fig. 8), the defect that Luo & Wu report
for WENO-Z+ below. Their velocity
$0.5233346$ has one digit more than the $0.523346$ of the other sources
and of the Rankine–Hugoniot state at $M=1.3$ *(compiler check, not in
the sources)*.

The Chamarthi papers'
figure axes span about $-4$ to $4$ (Chamarthi 2023a, Fig. 16) and $-5$ to
$5$ (Chamarthi 2023b, Fig. 8), so printed data and plotted domain
disagree. Chamarthi (2023a) finds TENO5 "severely" under-resolving the
fluctuations, which MEG6 and MIG4 resolve; Chamarthi (2023b) finds MEG7
resolving them better than WCNS7M.

[Zhang & Zhu (2024)](/sources/zhang-2024-c.md) Ex. 3.8 run the same
data ($(1.515695,0.523346,1.80500)$ for $-5\le x<-4.5$) to $t=5$ on 2000
points or cells against WENO-JS5 on 20000, and state that GMR-WENO
"perform better" than MR-WENO (Fig. 3.15). They call the density
"ten times bigger than the density of the standard
shock/turbulence problem"; the printed data have half the amplitude
(0.1 against 0.2) and the wavenumber $20\pi$ against 5, a ratio
$20\pi/5\approx12.6$ *(compiler check, not in the sources)*.

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

## Mach 10 variant

[Peyvan et al. (2023)](/sources/peyvan-2023.md) §4.2 (arXiv v1) print a
"modified Shu–Osher" problem with a Mach 10 shock:
$(\rho,v,p)=(3.857143,\ 9.76153,\ 116.5)$ for $x\le-4$ and
$(1+0.2\sin5x,\,0,\,1)$ for $x>-4$ on $[-5,5]$, $\gamma=1.4$, $t=0.7$
(shock at $x=4.27$), 170 elements of degree $P=3$,
$\Delta t=9.9964\times10^{-5}$, reference DGSEM on 3000 elements. Their
entropy-stable DGSEM with flux blending resolves the dip at $x=2.82$
and the valley at $x=3.265$, which spectral-difference and filtered
[flux reconstruction](/methods/flux-reconstruction.md) miss (Fig. 2);
they note that the adaptive [entropy filter](/methods/entropy-filtering.md)
has a problem-dependent threshold ($10^{-4}$) that must be tuned.

The printed left state is not a single Mach 10 shock *(compiler check,
not in the sources)*. Rankine–Hugoniot for $M=10$ into $(1,0,1)$ with
$\gamma=1.4$ gives $p=(2\gamma M^2-(\gamma-1))/(\gamma+1)=116.5$ and
$v=M\sqrt\gamma\,(1-1/\rho)=9.76153$ with
$\rho=(\gamma+1)M^2/((\gamma-1)M^2+2)=240/42=5.714286$; the printed
velocity and pressure are these Mach 10 values, while the printed
density $3.857143$ is the Mach 3 density $27/7$ of the common data
above, as printed in exact form by Li et al. (2022b) and Ye et al. and
in decimals by the other sources of this page. The paper does not say
which state was run. Its Fig. 2 caption gives a pressure ratio of 100
against the printed $116.5$.

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
not in the sources)*, so the printed velocity is inconsistent with the
printed density and pressure.

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
- **Two-dimensional shock–entropy wave.** Chamarthi (2023a) Ex. 4.6 and
  Chamarthi (2023b) Ex. 3.7 run an oblique version on
  $[-5,5]\times[-1,1]$: the Mach 3 post-shock state
  $(\rho,v_1,p)=(3.857143,2.629369,10.3333)$ for $x<-4$ and
  $(1+0.2\sin(10x\cos\theta+10y\sin\theta),0,1)$ ahead, $\theta=\pi/6$,
  $400\times80$ points ($\Delta x=1/40$), $t=1.8$, against MP5
  (Chamarthi 2023a) or MIG4 (Chamarthi 2023b) on $1600\times320$.
  Chamarthi (2023a) finds MIG4 resolving the high-frequency waves best
  and TENO5 oscillating, which "may indicate insufficient dissipation"
  (Fig. 9); Chamarthi (2023b) finds MEG7 less dissipative and less
  dispersive than WCNS7M, and uses a shock-stable HLLC flux to avoid a
  carbuncle seen with the author's earlier scheme (Fig. 10; see
  [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md)).
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
- Chamarthi (2023a) prints no reference for the 300-point run of the 1D
  problem; both Chamarthi papers are read as arXiv preprints.
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
- Lin, Chan & Tomas print the post-shock state for "$x<4.0$" on
  $[-5,5]$ with inflow at $x=-5$; a shock moving at the
  Rankine–Hugoniot speed $3.857143\cdot2.629369/2.857143\approx3.55$
  from $x=4$ would leave the domain by $t\approx0.28$, long before
  $T=1.8$, so the interface is at $x=-4$ as in every other source
  *(compiler check, not in the sources)*.
- Maltsev et al.'s strip $[-4.5,4.5]$ starts half a unit to the right
  of the $[-5,5]$ placement; with the shock at $x=-4$ the post-shock
  region is shorter, the incoming wave is the same *(compiler check, not
  in the sources)*.
- Ji, Liang & Fu (2023) state "200 uniformly distributed mesh cells"
  in the text and "a uniformly distributed triangular mesh with
  $h\approx1/20$" in the captions, without the number of triangles of
  the strip.
- Naudet & Zahr call the problem a "Mach $M=3$ shock" and run it to
  $T=2$, which they call "larger than often seen in the literature";
  their §5.3.2 says that extruding 20 spatial elements and splitting the
  quadrilaterals gives "160 quadratic space-time simplices", whereas the
  four-triangle split of their Remark 9, which matches their other
  one-dimensional cases (6 to 24, 8 to 32 elements), gives 80 *(compiler
  check, not in the sources)*.
- Kolluru et al.'s figure caption calls it the "Osher–Shu problem".
- Hiejima runs the one-dimensional problem in a three-dimensional
  code on $N_x\times21\times21$ points and prints the post-shock pressure
  as $31/3$.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.4, Figs. 4–5 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.4, Figs. 6–7.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.4–4.5, Eqs. (44)–(45), Figs. 4–5.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §4.3.2, Eq. (40), Fig. 5.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §2.3; §5.2.2–5.2.3, Eqs. (14)–(15), Figs. 10–11.
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4, Example 2, Fig. 2.
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
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Exs. 4.6, 4.11, 4.12, Figs. 9, 16 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Exs. 3.5, 3.7, Figs. 7, 8, 10 (arXiv v1).
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.4.3–3.4.4, Table 13, Fig. 9.
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.2, Eq. (37), Fig. 11.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — App. A.2, Fig. 12.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.3, Exs. 8–9, Figs. 7–8.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — Example 4.3, Fig. 4.5, Table 5.1.
- [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) — §4.3, Fig. 6 (arXiv v1).
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — §8.2, Eq. (64), Figs. 5–6 (arXiv v2).
- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §5.2, Eq. (46), Fig. 6.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §3.3, Figs. 8–9.
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §4.2, Eq. (93), Fig. 2 (arXiv v1).
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.4, Eq. (41), Figs. 7–8, Table 6.
- [Tang (2024)](/sources/tang-2024.md) — §4.3, Eq. (29), Fig. 7, Table 5.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §5.1.1, Fig. 6.
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3, Case 3.5, Fig. 3.6.
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — Ex. 3.5, Ex. 3.8, Figs. 3.9–3.10, 3.15.
- [Kolluru et al. (2024)](/sources/kolluru-2024.md) — §3.4, Eq. (9e), Fig. 16, App. B (arXiv v2).
- [Naudet & Zahr (2024)](/sources/naudet-2024.md) — §5.3.2, Figs. 19–21.
