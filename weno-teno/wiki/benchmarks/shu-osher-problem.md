---
type: Benchmark
title: "Shu–Osher shock–entropy-wave problem"
description: "One-dimensional Euler benchmark of a Mach 3 shock running into a sinusoidal density (entropy) wave, with its Titarev–Toro high-frequency variant; the bundle's most widely run test of how well a shock-capturing scheme resolves the short waves generated behind a shock without oscillating at the shocklets."
status: established
aliases: [Shu–Osher problem, shock–density wave interaction, shock–entropy wave interaction, Titarev–Toro problem]
tags: [benchmark, low-dissipation, weno, teno]
timestamp: 2026-10-21T12:00:00Z
---

# Shu–Osher shock–entropy-wave problem

A Mach 3 shock moves to the right into gas at rest whose density
carries a small sinusoidal perturbation at uniform pressure, i.e. an
entropy wave. Passing through the shock, the wave is compressed into a
band of short, steep density oscillations, followed by weak shocklets.
A dissipative scheme damps the short waves; an oscillatory one creates
spurious waves near the shocklets. The problem is the most widely run
one-dimensional resolution test in the bundle: twelve sources run it or
a variant (one of them a review reproducing earlier figures), in four
placements of one set of data, plus a high-frequency variant attributed
to Titarev & Toro.

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
| $[-5,5]$ | $x=-4$ | $1+0.2\sin(5x)$ | 1.8 | [Li et al. (2022)](/sources/li-2022-b.md) §4.3.2; [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.2; [Wang et al. (2023)](/sources/wang-2023-b.md) Example 2; [Takagi et al. (2022)](/sources/takagi-2022.md) §4.4; [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.8 (domain not stated) |
| $[0,10]$ | $x=1$ | $1+0.2\sin(5(x-5))$ | 1.8 | [Fu (2021)](/sources/fu-2021.md) §5.4 |
| $[0,10]$ | $x=1$ | $1+0.2\sin(5x)$ as printed | 1.8 | [Ye et al. (2022)](/sources/ye-2022.md) §4.4 |
| $[0,1]$ | $x=0.1$ | $1+0.2\sin(50x-25)$ | 0.18 | [Deng (2023)](/sources/deng-2023.md) App. A.6; [Huang et al. (2026)](/sources/huang-2026.md) §6.4 |

The $[0,1]$ placement is the $[-5,5]$ one under $x\mapsto(x+5)/10$,
$t\mapsto t/10$ (velocities unchanged), since
$\sin(5x')=\sin(50x-25)$ for $x'=10x-5$ *(compiler check, not in the
sources)*. The $[0,10]$ placement of Fu (2021) is the shift $x\mapsto x+5$.
Ye et al. print $\sin(5x)$ without the shift, which changes the phase
of the incoming wave relative to the shock *(compiler check, not in the
sources)*.

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

## Findings across sources

**Short-wave resolution.** Every source reads the amplitude of the
post-shock short waves as the measure of dissipation, and every new
scheme improves on its baseline: TENO-AA over WENO-CU6 in amplitude and
phase (Fu 2021, Fig. 4); WENO-ZN over WENO-JS and WENO-Z (Li et al.,
Fig. 5); WENO-Z+M better than WENO-Z+ at the discontinuity and better
than WENO-IS-I and WENO-Z9 on the high-frequency waves (Luo & Wu, Fig.
10); the adaptive-diffusion flux reducing dissipation behind the shock
(Wang et al., Fig. 2); AFTENO and TENO best on the entropy-wave
amplitude (Ye et al., Fig. 4); TENO-THINC similar to TENO5 and slightly
better than WENO5-Z, with a negligible CFL effect (Takagi et al., Figs.
6–7); WENO3-NN "significantly smeared out" against ROUND and LD-ROUND,
LD-ROUND best (Huang et al., Fig. 9). Fu (2023) reports that TCNS6
beats seventh- and ninth-order WCNS-Z on this problem.

**Oscillations at shocklets.** Fu (2021) reports density and velocity
oscillations of WENO-CU6 near the shocklets, which TENO-AA avoids.

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
Riemann solver, and WENO5-Z-FV.

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
state above *(compiler check, not in the sources; recomputed
2026-10-21)*.

## Related variants

- [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 2, called
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
- The resolution claims are visual comparisons of zoomed density
  profiles; no source reports an error norm against its reference.

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
