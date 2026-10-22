---
type: Method
title: "Multi-resolution WENO"
description: "Multi-resolution WENO combines polynomials on nested central stencils of increasing size, down to a one-point base, with any positive linear weights; the page records the Zhu–Shu hierarchy, the fifth-order finite-difference variant of Wang et al. with weight-free indicators, its Hermite and entropy-stable uses, costs, and the third-order fix of Balsara et al."
status: established
aliases: [multi-resolution WENO, multiresolution WENO, MR-WENO, WENO-MR, WENOZS5, New WENO5, WENOMR, Zhu–Shu WENO]
tags: [weno, cweno, reconstruction, finite-difference]
timestamp: 2026-10-22T20:00:00Z
---

# Multi-resolution WENO

**Multi-resolution WENO** (Zhu & Shu 2018, as recalled by Wang et al. 2021, §1, §3.1.1, and Balsara
et al. 2024, §I) builds candidate polynomials on a hierarchy of **nested, central** stencils whose
sizes grow from one point to the full stencil, instead of on the shifted equal-size stencils of
[WENO-JS](/methods/weno-js-reconstruction.md). The candidates are combined in the
[CWENO](/methods/cweno.md) manner, so that the linear weights need not reproduce a target linear
scheme and "can set as any" positive numbers summing to one (Wang et al. 2021, §1). Where smoothness is
lost, the reconstruction falls back level by level, down to the first-order base polynomial. Wang et
al. (2021, §1) state that these schemes were "the first time to use a series of unequal-sized spatial
stencils for the reconstruction process"; Balsara et al. (2024, §I) list them, with
[WENO-AO](/methods/weno-ao.md) and WENO-ZQ, among the stability-oriented descendants of CWENO.

On this page $T_m$ denotes the $m$th nested stencil, $P_m$ its polynomial, $d_m$, $\beta_m$,
$\omega_m$ its linear weight, indicator and nonlinear weight, with $m=1$ the smallest (page-local
index, increasing with stencil size, unlike the registry's $S_0$ = most upwind).

## Fifth-order finite-difference recipe

Wang, Zhu, Tian, Yang & Zhao (2021, §3.1.1, Steps 1–7) give the fifth-order scheme for the positive
Lax–Friedrichs split flux $f^+$ of the [conservative finite-difference
scheme](/definitions/conservative-finite-difference-scheme.md), whose point values are read, as in
FD-WENO, as cell averages of the primitive function.

1. **Stencils and polynomials.** $T_1=\{x_i\}$, $T_2=\{x_{i-1},x_i,x_{i+1}\}$,
   $T_3=\{x_{i-2},\dots,x_{i+2}\}$; $P_m$ of degree $2m-2$ matches the cell averages on $T_m$. In the
   local Legendre basis of Balsara et al. 2016 (page-local $X=(x-x_i)/\Delta x$, $\phi_0=1$,
   $\phi_1=X$, $\phi_2=X^2-\tfrac1{12}$, $\phi_3=X^3-\tfrac3{20}X$, $\phi_4=X^4-\tfrac3{14}X^2+\tfrac3{560}$),
   $P_1=f^+_i$, $P_2=\sum_{l\le2}\mathsf a_l\phi_l$, $P_3=\sum_{l\le4}\mathsf b_l\phi_l$ with
   (page-local coefficients; Eq. (3.9))
   $$\begin{aligned}
   \mathsf a_1&=\tfrac12(f_{i+1}-f_{i-1}),\qquad \mathsf a_2=\tfrac12(f_{i-1}-2f_i+f_{i+1}),\\
   \mathsf b_1&=\tfrac1{120}(11f_{i-2}-82f_{i-1}+82f_{i+1}-11f_{i+2}),\quad
   \mathsf b_2=\tfrac1{56}(-3f_{i-2}+40f_{i-1}-74f_i+40f_{i+1}-3f_{i+2}),\\
   \mathsf b_3&=\tfrac1{12}(-f_{i-2}+2f_{i-1}-2f_{i+1}+f_{i+2}),\quad
   \mathsf b_4=\tfrac1{24}(f_{i-2}-4f_{i-1}+6f_i-4f_{i+1}+f_{i+2}),
   \end{aligned}$$
   and $\mathsf a_0=\mathsf b_0=f_i$ (superscript $+$ dropped). *(Compiler check, not in the sources:
   all coefficients were recomputed by solving the cell-average conditions; they agree.)*
2. **Linear weights.** Any positive $d_1,d_2,d_3$ with sum 1; recommended $d=(1,10,100)/111$
   (Step 3).
3. **Indicators** ([smoothness indicators](/definitions/smoothness-indicator.md)). Jiang–Shu form on
   $P_2$, $P_3$, written as sums of squares (Eq. (3.11)),
   $$\beta_2=\mathsf a_1^2+\tfrac{13}{3}\mathsf a_2^2,\qquad
   \beta_3=\big(\mathsf b_1+\tfrac1{10}\mathsf b_3\big)^2+\tfrac{13}{3}\big(\mathsf b_2+\tfrac{123}{455}\mathsf b_4\big)^2+\tfrac{781}{20}\mathsf b_3^2+\tfrac{1421461}{2275}\mathsf b_4^2,$$
   and, for the constant $P_1$, $\beta_1=\min\big((f_i-f_{i-1})^2,(f_{i+1}-f_i)^2\big)$ (Eq. (3.12)).
4. **Weights.** WENO-Z type with exponent 1 on the ratio and a squared global indicator (Eq. (3.17)),
   $$\tau=\Big(\frac{|\beta_3-\beta_1|+|\beta_3-\beta_2|}{2}\Big)^2,\qquad
   \alpha_m=d_m\Big(1+\frac{\tau}{\epsilon+\beta_m}\Big),\qquad \epsilon=10^{-10}$$
   ($\tau$ page-local; not the WENO-Z $\tau_5$ of the registry).
5. **Interface value** (Eq. (3.21)),
   $$\hat f^+_{i+1/2}=\omega_1P_1+\omega_2P_2+\omega_3\Big[\frac1{d_3}P_3-\frac{d_1}{d_3}P_1-\frac{d_2}{d_3}P_2\Big]\Big|_{x_{i+1/2}},$$
   which returns $P_3(x_{i+1/2})$, the fifth-order upwind flux, when $\omega_m=d_m$; $\hat f^-$ by
   mirror symmetry and $\hat f=\hat f^++\hat f^-$. The reconstruction is done in local characteristic
   fields ([characteristic decomposition](/methods/characteristic-decomposition.md)).

The same algorithm, phrased in the Legendre basis and applied to scaled entropy variables, is
reprinted by Li, Duan & Tang (2022, App. A).

## Accuracy argument

Wang et al. (2021, Eqs. (3.13)–(3.20)) expand all indicators: each equals $(f')^2\Delta x^2+O(\Delta x^3)$;
$|\beta_3-\beta_1|=O(\Delta x^3)$ if $f'\ne0$ and $O(\Delta x^4)$ if $f'=0$, $f''\ne0$;
$|\beta_3-\beta_2|=O(\Delta x^4)$ or $O(\Delta x^6)$. Hence $\tau=O(\Delta x^6)$ or $O(\Delta x^8)$ and
$\omega_m=d_m+O(\Delta x^4)$ in smooth regions, including first-order critical points
([accuracy at critical points](/properties/critical-point-accuracy.md)). There is no formal theorem.
*(Compiler check, not in the sources: writing the interface value as
$\frac{\omega_3}{d_3}P_3+\sum_{m=1,2}\big(\omega_m-\tfrac{d_m}{d_3}\omega_3\big)P_m$, the coefficients
of $P_1$, $P_2$ are $O(\Delta x^4)$ and multiply errors $O(\Delta x)$ and $O(\Delta x^3)$, so the value
error stays $O(\Delta x^5)$.)*

## Indicators that depend on the linear weights

In the original scheme (as recalled by Wang et al. 2021, Remark 2, Eqs. (3.23)–(3.28)) the indicators
are computed on "equivalent polynomials"
$$\tilde P_1=P_1,\qquad \tilde P_m=\frac1{d_{m,m}}P_m-\sum_{l=1}^{m-1}\frac{d_{l,m}}{d_{m,m}}\tilde P_l,\qquad \sum_{l=1}^md_{l,m}=1,$$
(page-local level-wise weights $d_{l,m}$) that contain the linear weights, and $\beta_1$ is a weighted
blend of the two one-sided squared differences. Wang et al. argue that these indicators "misjudge" the
smoothness of $P_2$, $P_3$ for some weight choices, "resulting in only first-order accuracy for the
smooth problems" (§3.1.1, p. 5), and show the original scheme (WENOZS5) missing fifth order with their
third weight set and failing to converge on their 3-D viscous test (§5.1, Figs. 5.2–5.6). Their scheme
reaches fifth order with $(0.95,0.049,0.001)$, $(1/3,1/3,1/3)$ and $(0.001,0.049,0.95)$ (§5.1). The
decoupling of indicators from linear weights is the paper's main contribution.

## Hermite and moment-based hierarchy

Li, Shu & Qiu (2022, §2.1, Eqs. (2.9)–(2.24)) build a sixth-order finite-volume hierarchy on the
compact three-cell stencil from cell averages and first moments
([Hermite WENO](/methods/hermite-weno.md)): $P_1,\dots,P_4$ of degree 0, 2, 3, 5, the constant from
$\bar u_i$ alone and the others from the averages of $I_{i-1},I_i,I_{i+1}$ and zero, one or three
first moments $\bar u^{(1)}$ (page-local, defined on the Hermite WENO page). They keep the Zhu–Shu equivalent
polynomials, with unnormalized linear weights $10^{l-1}$ at every level, which gives
$$\tilde P_2=\tfrac{11}{10}P_2-\tfrac1{10}P_1,\quad \tilde P_3=\tfrac{111}{100}P_3-\tfrac{11}{100}P_2,\quad \tilde P_4=\tfrac{1111}{1000}P_4-\tfrac{111}{1000}P_3,$$
and indicators on $\tilde P_m$. The base indicator is not zero: two linear polynomials on
$\{I_{i-1},I_i\}$ and $\{I_i,I_{i+1}\}$ are combined with WENO-Z weights and
$\beta_1=\big(\omega_{\mathrm L}(\bar u_i-\bar u_{i-1})+\omega_{\mathrm R}(\bar u_{i+1}-\bar u_i)\big)^2$
(page-local $\omega_{\mathrm{L,R}}$; in 2-D four L-shaped triples, Eqs. (2.49)–(2.55)). The weights are
$\alpha_m=d_m\big(1+\tau/(\beta_m+\epsilon)\big)$ with
$\tau=\big(\tfrac13\sum_{l=1}^3|\beta_4-\beta_l|\big)^2$, $\epsilon=10^{-10}$ (Eqs. (2.21)–(2.22)), and
the reconstruction is the convex combination $\sum_m\omega_m\tilde P_m$ (Eq. (2.23)).

## Fixes at low and high order

Balsara et al. (2024, §VII.a, App. D) found that the published **third-order** multi-resolution WENO
"got less than second order accuracy" on somewhat large meshes, because it jumps from third to first
order. Their fix replaces the first-order base polynomial by a limited linear one,
$\bar u_i+\mathrm{MC}_\theta(\bar u_{i+1}-\bar u_i,\bar u_i-\bar u_{i-1})$ or the van Albada form
(Eqs. (D.7)–(D.10)), with
$$\mathrm{MC}_\theta(a,b)=\tfrac12\big(\mathrm{sgn}\,a+\mathrm{sgn}\,b\big)\min\big(\tfrac12|a+b|,\theta|a|,\theta|b|\big),\ 1\le\theta\le2,\qquad
\mathrm{vA}_\epsilon(a,b)=\frac{(b^2+\epsilon)a+(a^2+\epsilon)b}{a^2+b^2+2\epsilon},$$
($\theta$ the MC parameter, page-local, not the Zhang–Shu factor of the registry; $a$, $b$ here are
slopes, page-local); the van Albada form is suggested for implicit problems because it is continuous
in the slopes ([TVD limiters](/definitions/total-variation-diminishing.md)). Wang et al. (2021) and Li
et al. (2022) use one-point base polynomials at fifth and sixth order, with $\beta_1$ built from
one-sided differences; their tests show the design orders, so the third-order defect of Balsara et
al. is not contradicted at those orders.

## Linear weights and robustness

The sources agree that the linear weights do not affect smooth-region accuracy but do affect shocks:
- a larger weight on the largest stencil gives sharper discontinuities but "tends to oscillate"
  (Wang et al. 2021, §3.1.1 Step 3; Li, Duan & Tang 2022, App. A step 3; Li, Shu & Qiu 2022, Remark 1,
  where larger weights on higher-degree polynomials make "the more unstable the scheme becomes", and
  §1, where the gap between linear weights "cannot be too large");
- on the Sedov, double-rarefaction and Leblanc problems Wang et al. (2021, Example 5.5) state that
  their weight ratio "is so large that it cannot directly and robustly solve such extreme problems"
  and revert to the weights of the original scheme; no positivity limiter is used
  ([Sedov blast wave](/benchmarks/sedov-blast-wave.md),
  [double rarefaction](/benchmarks/double-rarefaction-problem.md),
  [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md));
- Li, Duan & Tang (2022, §5) use $(1,10,100)/111$ by default and $(0.95,0.045,0.005)$ in three
  examples.

Chen & Wu (2022, §1) place the hierarchy in the line of reconstructions whose linear weights "can
also be chosen arbitrarily": after the Zhu–Qiu combination of one high-degree polynomial with several
linear ones, which extends easily to triangles and tetrahedra, "the multi-resolution WENO schemes
with similar linear weights were proposed" ([CWENO](/methods/cweno.md)). Du, Shu & Zhong (2022, §1)
recall compact DG limiters built on the multi-resolution procedure, which "appear to be quite robust
for RKDG methods of various orders" ([WENO limiters for DG](/methods/weno-limiter-dg.md)).

## Performance

- **Smooth accuracy.** On a 1-D Euler density wave at 320 points, Wang et al. (2021, Table 5.1) give
  $L_1$ errors $2.93\times10^{-11}$ for their scheme and for the linear Upwind5 scheme,
  $3.26\times10^{-11}$ for WENOZS5, $1.93\times10^{-10}$ for WENO-JS5. Balsara et al. (2024, Table I)
  report $L_1$ density rates 2.74, 4.68, 6.93, 8.78 for multi-resolution WENO of orders 3, 5, 7, 9 on
  the 2-D Euler [isentropic vortex](/benchmarks/isentropic-vortex.md) in their
  [fluctuation-form FD-WENO](/methods/fluctuation-form-fd-weno.md).
- **Cost.** At 320 points (1-D Euler) Upwind5 takes 0.9217 s, WENO-JS5 1.5809 s, WENOZS5 3.0171 s,
  the new scheme 1.9766 s (Wang et al. 2021, Table 5.1); in 3-D at $100^3$, 14526 s, 22054 s and
  15170 s for WENO-JS5, WENOZS5 and the new scheme (Table 5.5). Over the 2-D and 3-D shock tests the
  cost relative to WENO-JS5 is 1.09–1.60 for the new scheme, 1.40–1.83 for WENOZS5 and 1.29–1.80 for
  WENO-AO(5,3) (Table 5.8). Wang et al. (§6) add that on unstructured meshes three sub-stencils
  suffice for orders above three, where classical unstructured WENO "needs more than nine
  sub-stencils" (stated, not shown).
- **Resolution.** The multi-resolution schemes capture more roll-up than WENO-JS5 on the
  [two-dimensional Riemann problem](/benchmarks/two-dimensional-riemann-problems.md),
  [double Mach reflection](/benchmarks/double-mach-reflection.md),
  [forward-facing step](/benchmarks/forward-facing-step.md) and
  [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md), and the new scheme
  "performs best among the four considered WENO schemes" on the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (Wang et al. 2021, Examples 5.6–5.9,
  5.13). WENO-AO(5,3) is better near the Sedov peak and on the
  [Shu–Osher problem](/benchmarks/shu-osher-problem.md) (Examples 5.4–5.5), where Wang et al.
  suggest that their algorithm "is rapidly reduced to the first order accuracy" at strong shocks.
  The approximate dispersion relation of the multi-resolution schemes is better than WENO-JS5 (§4,
  Fig. 4.1; [approximate dispersion relation](/definitions/approximate-dispersion-relation.md)).
- **Entropy-stable dissipation.** Li, Duan & Tang (2022, §3.4, Eq. (3.21)) reconstruct the jump of
  scaled entropy variables in a TeCNO-type entropy-stable flux with this fifth-order scheme
  ([TeCNO schemes](/methods/tecno-scheme.md),
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md)). Against the same scheme with WENO-JS,
  it "better capture[s] the localized structures" (Remark 3.2); the printed timings (Tables 5.1–5.2)
  are 2m56s vs 2m37s, 2m50s vs 2m38s, 13m53s vs 13m52s and 3m21s vs 3m3s, i.e. 0.1–12 % more
  *(compiler check, not in the sources: ratios of the printed timings)*.

## Qualifications

- **Which weights were used.** Wang et al. (2021) recommend $(1,10,100)/111$ "for all examples in
  this paper" (§3.1.1 Step 3), but §5 defines "New WENO5" as the first weight type
  $(0.95,0.049,0.001)$, and Example 5.5 says that "the linear weight here is the same as the original
  method" because their own ratio is too large, although §5 gives the original method's weights as
  $(1,10,100)/111$. The weights behind the shock results are therefore ambiguous. Their §3.1.1 and §5.1
  also describe the failure case of the original scheme in opposite terms (small vs large weight on
  the five-point stencil).
- Wang et al. (2021, §5.4) write that their scheme costs "9%–30%" more than WENO-JS5, but Table 5.8
  gives up to 1.60 (Example 5.10); "about 0.7 times" WENOZS5 is the lower end of the table's
  0.70–0.87.
- *(Compiler check, not in the sources.)* The $\Delta x^4$ bracket printed for $|\beta_3-\beta_1|$ in
  Wang et al. (2021, Eq. (3.18)) is the $\Delta x^4$ term of $(f_i-f_{i-1})^2$ itself; the difference of
  their Eqs. (3.13) and (3.16) gives $\tfrac56(f'')^2-\tfrac13f'f'''$. The order conclusions are
  unaffected.
- Li, Duan & Tang (2022, App. A) phrase the algorithm "for the given cell average values"; applied
  to finite-difference point values it rests on the reading that Wang et al. (2021, §3.1.1) state,
  point values interpreted, as in FD-WENO, as cell averages of the primitive function.
- The claim against the original multi-resolution WENO is made by Wang et al. with Zhu, a co-author
  of the original; Balsara et al.'s third-order fix is likewise made by a group including Shu.
  Neither is an independent test, and the original Zhu–Shu paper is not ingested.
- Balsara et al. (2024, Table III) contain an unexplained rate of 12.06 for ninth-order
  multi-resolution WENO.

# Citations

- [Wang et al. (2021)](/sources/wang-2021.md) — §1; §3.1.1, Steps 1–7, Eqs. (3.2)–(3.28), Remark 2; §4, Fig. 4.1; §5.1, Tables 5.1–5.6, Figs. 5.1–5.6; Examples 5.4–5.13; §5.4, Table 5.8; §6.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §3.4, Eq. (3.21), Remark 3.2; §5, Tables 5.1–5.2; App. A.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1; §2.1, Eqs. (2.9)–(2.24), Remark 1; §2.2, Eqs. (2.42)–(2.56).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; §VII.a–b, Tables I, III; App. D, Eqs. (D.7)–(D.10).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §1.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1.
