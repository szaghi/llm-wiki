---
type: Method
title: "Mapped WENO"
description: "Mapped WENO (WENO-M, Henrick, Aslam & Powers) passes the Jiang–Shu weights through a mapping that fixes the linear weights, restoring the fifth-order condition at first-order critical points but not where f'' also vanishes, at a higher CPU time than WENO-JS and WENO-Z in Borges et al.'s timings; another source maps second-order TVD weights for a third-order WENO."
status: established
aliases: [WENO-M, mapped weights, Henrick mapping, mapping-function-free WENO-M]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-30T08:09:00Z
---

# Mapped WENO

Mapped WENO (WENO-M) of Henrick, Aslam & Powers corrects the [WENO-JS](/methods/weno-js-reconstruction.md)
weights $\omega_k$ through a mapping function $g(\omega)$ (Luo & Wu 2021, §1: "a mapping function to
correct the WENO-JS weights"; Deng 2023, §1: "modifies the non-linear weights through a mapping
function"; Takagi et al. 2022, §1: "remapping the WENO5-JS nonlinear weights"). Shu (2009a, §2.3.5)
describes it as "another choice of the nonlinear weights, based on the same smoothness indicators ... to
enhance accuracy in smooth regions, especially at smooth extrema".

## The mapping

[Borges et al. (2008)](/sources/borges-2008.md) (§2, Eq. (24)) print the mapping, after Henrick et al., and
Chamarthi (2023b, §3, Eqs. (47)–(48)) prints it again, applied to the weights of the seventh-order WCNS7M
comparator ([WCNS](/methods/weighted-compact-nonlinear-scheme.md); citing Henrick et al. and Jin et al.).
In registry notation, with $d_k$ the linear weights,

$$g_k(\omega)=\frac{\omega\big(d_k+d_k^2-3d_k\omega+\omega^2\big)}{d_k^2+(1-2d_k)\omega},$$

and the mapped weights are used in place of $\omega_k$. Borges et al. list its properties: $g_k$ is
non-decreasing with $0\le g_k\le1$, $g_k(0)=0$, $g_k(1)=1$; $g_k(d_k)=d_k$ and $g_k'(d_k)=g_k''(d_k)=0$; hence
$g_k(\omega)=d_k+O(\Delta x^6)$ when $\omega=d_k+O(\Delta x^2)$. Chamarthi states that the mapping
"efficiently recovers the formal order of accuracy of the scheme", and prints the denominator with a minus,
$d_k^2-(1-2d_k)\omega$, against the plus of Borges et al. *(Compiler check, not in the sources: with the
printed minus $g_k(d_k)=d_k(1-d_k)/(3d_k-1)$, e.g. $-\tfrac{63}{3904}$ for $d_k=\tfrac1{64}$, so that form
would not fix the linear weights.)*

## A third-order mapping of TVD weights

[Komissarov & Phillips (2024)](/sources/komissarov-2024.md) (§3.3, App. A, Eqs. (A1)–(A23);
arXiv v3) build a third-order WENO interpolation of point values for their relativistic MHD
code by mapping second-order TVD weights instead of Jiang–Shu weights, and present it as
analogous to Henrick et al.'s mapped WENO5. The two linear interpolants
$P_-=u_i+(u_i-u_{i-1})(x-x_i)/\Delta x$ and $P_+=u_i+(u_{i+1}-u_i)(x-x_i)/\Delta x$ are combined with
Falle's TVD weights

$$w_-=\frac{\beta_+}{\beta_-+\beta_+},\qquad w_+=\frac{\beta_-}{\beta_-+\beta_+},$$

which favour the smaller gradient (page-local $w_\pm$, $\beta_\pm$; the indicators are on the
[smoothness indicators](/definitions/smoothness-indicator.md) page). The combination equals the
three-point quadratic at $x_{i+1/2}$ for $(w_-,w_+)=(\tfrac14,\tfrac34)$ and at $x_{i-1/2}$ for
$(\tfrac34,\tfrac14)$, so the linear weights are $\tfrac14$ and $\tfrac34$. A mapping must send
$w_+=\tfrac12$ (smooth data) to these values and leave $w_+\to0$ or $1$ unchanged; with the flat
polynomial $g_n(x)=1-(1-2x)^n$, $n\ge2$ (page-local; Fig. A1 uses $n=4$), the weight at $x_{i+1/2}$ is

$$w^{\mathrm r}_+=\begin{cases}\tfrac34\,g_n(w_+),&0\le w_+\le\tfrac12,\\ 1-\tfrac14\,g_n(1-w_+),&\tfrac12<w_+\le1,\end{cases}\qquad w^{\mathrm r}_-=1-w^{\mathrm r}_+,$$

and the weight at $x_{i-1/2}$ has $\tfrac14$ and $\tfrac34$ exchanged. *(Compiler check, not in the
sources: $\tfrac14P_-+\tfrac34P_+$ at $x_{i+1/2}$ is $(-u_{i-1}+6u_i+3u_{i+1})/8$, the quadratic
interpolant; both branches give $\tfrac34$ at $w_+=\tfrac12$, and $1-g_n(w_+)=(1-2w_+)^n$, so a
deviation $\delta$ of $w_+$ from $\tfrac12$ becomes a deviation $O(\delta^n)$ of the mapped weight.)*
The scheme converges at third order on a high-magnetization Alfvén wave ($L_1(B_2)$ orders 3.5,
3.1, 3.0, 3.1; Table 1); no test isolates critical points
([critical-point accuracy](/properties/critical-point-accuracy.md)). The authors cite the WENO3 of
Ha et al. as an alternative whose "test results look impressive, but the approach is not
intuitive and hard to comprehend" (§3.3), a judgement without comparison.

## What the sources record

- **Purpose: critical points.** WENO-M was designed because WENO-JS fails to recover the optimal
  order at critical points (Deng 2023, §1; Fu 2021, §1; Takagi et al. 2022, §1; Balsara et al. 2024,
  §I). Li et al. (2022b, §2) recall that it satisfies the fifth-order condition at first-order
  critical points ([critical-point accuracy](/properties/critical-point-accuracy.md)). Borges et al.
  (2008, §2, after Eq. (24)) add that the mapping does not improve the order when $f''$ also vanishes:
  then $\beta_k=D(1+O(1))$, $\omega_k=d_k+O(1)$, and the scheme is second order like WENO-JS. Wang et al.
  (2021, §1) describe it as one of "two important variants" for "achieving optimal order near critical
  points", whose "nonlinear weights are pushed smoothly to the optimal values by a regularization
  process", the other being [WENO-Z](/methods/weno-z.md). Deng (2023,
  §1) adds that Henrick et al. also pointed out the sensitivity of WENO schemes to the regularization
  $\epsilon$. Hiejima (2022, §1) recalls it as "adjusting the weights to smoothly move the optimal
  values and meet the fifth-order accuracy".
- **Why it helps on shocks.** Borges et al. (2008, Remark 1) state that, "distinctly from" Henrick et
  al., they "do not credit" the better shock results of WENO-M to its order at critical points "but to the
  smaller dissipation that results from the assignment of larger weights to discontinuous stencils";
  next to a jump, WENO-M raises those weights slightly over WENO-JS's $10^{-8}$, and WENO-Z to about
  $10^{-4}$ (Fig. 3). They run WENO-M with $\epsilon=10^{-40}$ (Remark 2, §5) and find WENO-Z
  "equivalent" to it on composite advection and on the Richtmyer–Meshkov instability, slightly sharper on
  blast waves (§5).
- **Cost.** Borges et al. (2008, Tables 5–6) time it in one code on one machine: 1.87 s per Runge–Kutta step
  against 1.47 s for WENO-JS and 1.39 s for WENO-Z on the $400^2$ shock–vortex interaction, and similar ratios at
  $800^2$ and on the Richtmyer–Meshkov run *(compiler check, not in the sources: $1.87/1.47=1.27$,
  $1.87/1.39=1.35$)*; the cost question between WENO-Z and WENO-M is recorded on the
  [WENO-Z](/methods/weno-z.md) page. Luo & Wu (2021, §1) state that the mapping functions "dramatically" increase the
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
- **Recalled in passing** by Hong, Ye & Ye (2022, §1), Li, Chen & Ren (2022a, §1) and Liang et al.
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
  mapping belong to Henrick et al., which is not ingested; Borges et al. (2008) recall the mapping and its
  properties from it. Chamarthi's print of the mapping carries the opposite sign in the denominator. The
  third-order mapping of Komissarov & Phillips acts on TVD weights and is a different map.

# Citations

- [Borges et al. (2008)](/sources/borges-2008.md) — §2, Eq. (24), Remarks 1–2; §3, Fig. 3; §5, Tables 5–6.
- [Shu (2009a)](/sources/shu-2009.md) — §2.3.5.
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
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §1.
- [Liang et al. (2022)](/sources/liang-2022.md) — §1.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §3, Eqs. (43)–(48): the printed mapping in WCNS7M.
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §1.
- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — §3.3; §4.1, Table 1; App. A, Eqs. (A1)–(A23), Fig. A1: mapped TVD weights for third-order WENO (arXiv v3).
