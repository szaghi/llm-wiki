---
type: Method
title: "Mapped WENO"
description: "Mapped WENO (WENO-M, Henrick, Aslam & Powers) passes the Jiang–Shu nonlinear weights through a mapping function that fixes the linear weights, restoring the fifth-order condition at first-order critical points at a higher cost than WENO-JS; one source prints the mapping, inside a seventh-order WCNS."
status: established
aliases: [WENO-M, mapped weights, Henrick mapping, mapping-function-free WENO-M]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-23T12:00:00Z
---

# Mapped WENO

Mapped WENO (WENO-M) of Henrick, Aslam & Powers corrects the [WENO-JS](/methods/weno-js-reconstruction.md)
weights $\omega_k$ through a mapping function $g(\omega)$ (Luo & Wu 2021, §1: "a mapping function to
correct the WENO-JS weights"; Deng 2023, §1: "modifies the non-linear weights through a mapping
function"; Takagi et al. 2022, §1: "remapping the WENO5-JS nonlinear weights").

## The mapping

Chamarthi (2023b, §3, Eqs. (47)–(48)) is the only ingested source that prints the mapping, applied to the
weights of the seventh-order WCNS7M comparator ([WCNS](/methods/weighted-compact-nonlinear-scheme.md);
citing Henrick et al. and Jin et al.). In registry notation, with $d_k$ the linear weights,

$$g_k(\omega)=\frac{\omega\big(d_k+d_k^2-3d_k\omega+\omega^2\big)}{d_k^2+(1-2d_k)\omega},$$

and the mapped weights are used in place of $\omega_k$; the author states that the mapping "efficiently
recovers the formal order of accuracy of the scheme". Chamarthi prints the denominator with a minus,
$d_k^2-(1-2d_k)\omega$. *(Compiler check, not in the sources: with the plus sign
$g_k(0)=0$, $g_k(d_k)=d_k$ and $g_k(1)=1$; with the printed minus $g_k(d_k)=d_k(1-d_k)/(3d_k-1)$, e.g.
$-\tfrac{63}{3904}$ for $d_k=\tfrac1{64}$, so the printed map would not fix the linear weights on which the
recovery of order rests.)*

## What the sources record

- **Purpose: critical points.** WENO-M was designed because WENO-JS fails to recover the optimal
  order at critical points (Deng 2023, §1; Fu 2021, §1; Takagi et al. 2022, §1; Balsara et al. 2024,
  §I). Li et al. (2022, §2) recall that it satisfies the fifth-order condition at first-order
  critical points ([critical-point accuracy](/properties/critical-point-accuracy.md)). Wang et al.
  (2021, §1) describe it as one of "two important variants" for "achieving optimal order near critical
  points", whose "nonlinear weights are pushed smoothly to the optimal values by a regularization
  process", the other being [WENO-Z](/methods/weno-z.md). Deng (2023,
  §1) adds that Henrick et al. also pointed out the sensitivity of WENO schemes to the regularization
  $\epsilon$. Hiejima (2022, §1) recalls it as "adjusting the weights to smoothly move the optimal
  values and meet the fifth-order accuracy".
- **Cost.** Luo & Wu (2021, §1) state that the mapping functions "dramatically" increase the
  computational expense, and recall Hong's mapping-function-free WENO-M, which uses a pre-discrete
  mapping to reduce that cost. Wan & Xia (2022, §1) put the extra CPU time of WENO-M at "about 20%"
  (stated, without a measurement). Deng (2023, §1) and Luo & Wu (2021, §1) recall that
  [WENO-Z](/methods/weno-z.md) is more accurate than WENO-JS and cheaper than WENO-M, and Deng
  (2023, §4.3) that WENO-Z3 gives sharper solutions than mapped WENO.
- **Resolution.** Luo & Wu (2021, §1) recall that WENO-M "achieves significantly better results than
  WENO-JS for both discontinuities and smooth structures"; Fu (2023, §2.3) that WENO-M and WENO-Z
  "show better spectral resolution" than WENO-JS.
- **Comparisons.** In Fu's review (2023, §5.2, Fig. 18, reproduced from earlier work) TENO5 captures
  the cellular structure of a two-dimensional self-sustained detonation on coarse meshes better than
  WENO5-JS and WENO-M, and WENO5-JS gives incorrect cellular structures
  ([targeted ENO](/methods/targeted-eno.md)).

- **As a comparator.** Jeong, Yang & Yoon (2022, §5) run WENO-M against their sixth-order RBF-based
  WENO without printing the mapping: on linear advection of $\sin^2(2\pi x)$ at $N_x=640$ WENO-M and
  [WENO-Z](/methods/weno-z.md) give the same $L^\infty$ error, $1.96\times10^{-8}$, against
  $1.62\times10^{-7}$ for WENO-JS (Table 1), and WENO-M costs 42.28 s against 40.30 s for WENO-JS and
  40.51 s for WENO-Z in MATLAB (Table 3) ([RBF-based WENO](/methods/rbf-weno.md)).
- **Recalled in passing** by Hong, Ye & Ye (2022, §1), Li, Chen & Ren (2022, §1) and Liang et al.
  (2022, §1) as the first remedy for the critical-point defect, and by Zhou et al. (2023, §1) for its lower
  dissipation at critical points.

- **In codes.** Bryngelson et al. (2021, §4.1) cite Henrick, Aslam & Powers among the WENO
  references of the MFC solver, but do not state whether MFC uses mapped weights
  ([MFC](/software/mfc.md)).

## Place in the family

Mapped weights, WENO-Z and its descendants ([WENO-Z+](/methods/weno-z-plus.md),
[WENO-ZN](/methods/weno-zn.md)) all act only on the nonlinear weights of the same candidate
stencils. Fu (2023, §1) groups WENO-M and WENO-Z as the improvements for the order-degeneration
problem, distinct from the strategies that target dissipation (freezing the nonlinear adaptation,
raising the weights of non-smooth stencils, hybridization, spectral optimization).

## Qualifications

- The page records only what the ingested sources state about WENO-M; the proofs and the analysis of the
  mapping belong to Henrick et al., which is not ingested. The mapping is printed once, in a comparator
  scheme and with a sign slip; it is recorded above with the sign that fixes $d_k$.

# Citations

- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §1.
- [Deng (2023)](/sources/deng-2023.md) — §1; §4.3.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §2.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1.
- [Fu (2021)](/sources/fu-2021.md) — §1.
- [Fu (2023)](/sources/fu-2023.md) — §1; §2.3; §5.2, Fig. 18.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Wang et al. (2021)](/sources/wang-2021.md) — §1.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.1.
- [Hiejima (2022)](/sources/hiejima-2022.md) — §1.
- [Jeong, Yang & Yoon (2022)](/sources/jeong-2022.md) — §5, Tables 1–3.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §1.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1.
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §1.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §3, Eqs. (43)–(48): the printed mapping in WCNS7M.
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §1.
