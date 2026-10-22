---
type: Benchmark
title: "Sod and Lax shock tubes"
description: "The two most often run one-dimensional Euler Riemann problems with exact solutions, Sod's mild tube and Lax's stronger one, run by most sources as the first check of shock and contact capturing; records each source's placement, grid and final time and the printed variants."
status: established
aliases: [Sod problem, Sod shock tube, Lax problem, Lax shock tube, Riemann problem of Lax]
tags: [benchmark, weno, teno, riemann-solver]
timestamp: 2026-10-21T12:00:00Z
---

# Sod and Lax shock tubes

Both are one-dimensional Riemann problems of the Euler equations with
$\gamma=1.4$: two constant states separated by a diaphragm at the
middle of the tube. Each has an exact solution containing a shock and
a contact discontinuity, so the benchmark checks whether a scheme
captures both sharply and without oscillation, before harder problems
are attempted. Lax's data start with a moving left state;
[Huang et al. (2026)](/sources/huang-2026.md) §6.3 describe the problem
as testing a strong shock and contact.

## Sod

$(\rho,v,p)=(1,0,1)$ on the left half of $[0,1]$ and $(0.125,0,0.1)$ on
the right half.

| Source | Grid | Final time | Notes |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.3 | 96 points | 0.2 | exact Riemann reference; [TENO-AA](/methods/adaptive-teno.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.3 | 100 | 0.2 | exact reference; [TENO-THINC](/methods/teno-thinc.md) |
| [Ye et al. (2022)](/sources/ye-2022.md) §4.3, Eq. (43) | 200 | 0.2 | mirrored: $(0.125,0,0.1)$ on the left, $(1,0,1)$ on the right; [AFTENO](/methods/afteno.md) |
| [Deng (2023)](/sources/deng-2023.md) App. A.4 | 200 cells | 0.25 | [ROUND](/methods/round-scheme.md), NewWENO |
| [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) §3.5.3, §5.6 | 100 | 0.1 | [Active Flux](/methods/active-flux.md); states and $\gamma$ not printed |

Abgrall & Barsukow run Sod with three Active Flux variants: sixth order
at CFL 0.25 (Fig. 19); a fifth-order point setup with a third-order
evolution operator at CFL 0.5 (Fig. 24); and seventh order at CFL 0.01
on a periodic tube with discontinuities at $x=1/3$ and $x=2/3$ (Fig. 28),
which doubles the problem so that periodic boundaries can be used.

## Lax

$(\rho,v,p)=(0.445,\ 0.698,\ 3.528)$ on the left and $(0.5,\ 0,\ 0.571)$
on the right. Two placements coexist.

| Source | Domain | Grid | Final time | Notes |
|---|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.3 | $[0,1]$ | 96 | 0.14 | right pressure printed $0.5710$ |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.3 | $[0,1]$ | 100 | 0.14 | same |
| [Deng (2023)](/sources/deng-2023.md) App. A.5 | $[0,1]$ | 200 cells | 0.16 | |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.3 | $[0,1]$ | 200 cells | 0.15 (text) / 0.16 (Fig. 8) | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md) |
| [Li et al. (2022)](/sources/li-2022-b.md) §4.3.1, Eq. (39) | $[-5,5]$ | 200 | 1.3 | zero-gradient BCs, CFL 0.5; reference fifth-order WENO-Z with 4000 points |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.2.4, Eq. (16) | $[-5,5]$ | 101 | 1.3 | CFL 0.5 |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.6 | $[-5,5]$ | 256 cells | 1.3 | outflow; data scaled by $\lambda\in\{1,0.01,100\}$ |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.3 | specifications deferred to an earlier paper | | | affine-invariant weights, data scaled |

The $[-5,5]$ placement at $t=1.3$ corresponds to the $[0,1]$ placement
at $t=0.13$ under the scaling $x\mapsto(x+5)/10$, $t\mapsto t/10$
*(compiler check, not in the sources)*; the $[0,1]$ runs stop later,
at $0.14$ to $0.16$, so the two families compare slightly different
wave positions.

## Findings across sources

**Contact resolution separates the schemes.** On Sod all schemes agree
with the exact solution, and differences lie at the contact: AFTENO best
and AFWENO-Z better than AFWENO-JS (Ye et al., Fig. 3); TENO-THINC
shocks as sharp as WENO5-Z and TENO5, contacts better resolved (Takagi
et al., Figs. 4–5, also for Lax). On Lax, WENO-ZN reduces the
dissipation near the shock (Li et al., Fig. 4); WENO-Z+M improves shock
and contact markedly over WENO-Z and WENO-Z+, is less oscillatory than
WENO-IS-I, while ninth-order WENO-Z9 is less dissipative but more
oscillatory (Luo & Wu, Fig. 12). Deng finds NewWENO less dissipative
than WENO-P on both tubes (Fig. 15).

**Scale invariance.** Scaling the Lax data by a factor $\lambda$
(page-local symbol) exposes schemes
whose weights depend on the magnitude of the data: OEDG is exactly
scale-invariant, whereas the earlier OFDG smears at $\lambda=100$,
oscillates at $\lambda=0.01$ and undershoots near the shock even at
$\lambda=1$ (Peng et al., Fig. 3). Wang & Don find affine-invariant Z-
and D-type weights essentially identical and non-oscillatory on Lax and
the "123" problem (Fig. 7). Deng recalls, from an earlier study, that
WENO-Z with $\epsilon=10^{-12}$ and WENO-JS with $\epsilon=10^{-6}$
oscillate on Sod scaled by $\lambda=10^{-7}$ (§1). See [scale invariance](/properties/scale-invariance.md).

## Qualifications

- Luo & Wu print the left Lax pressure as $0.3528$ (Eq. (16)), where
  Fu (2021), Takagi et al., Li et al., Deng, Huang et al. and Peng et
  al. print $3.528$; the paper's text does not show
  which value was run.
- Huang et al. give $t=0.15$ in the text and $t=0.16$ in the caption of
  Fig. 8.
- Wang & Don's figure of the unscaled tubes includes the Lax problem,
  although their §3.2.3 text list omits it.
- Li et al. compute the Lax reference with fifth-order WENO-Z, the
  other references of the paper with seventh order.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.3 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.3, Figs. 4–5.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.3, Eq. (43), Fig. 3.
- [Deng (2023)](/sources/deng-2023.md) — §1; App. A.4–A.5, Fig. 15.
- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §3.5.3 and §5.6, Figs. 19, 24, 28 (author preprint).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.3, Fig. 8.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.3.1, Eq. (39), Fig. 4.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.2.4, Eq. (16), Fig. 12.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.6, Fig. 3 (arXiv v1).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.3, Fig. 7.
