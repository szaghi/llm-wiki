---
type: Method
title: "Multi-resolution WENO"
description: "Multi-resolution WENO combines polynomials on nested central stencils, down to a one-point base, with any positive linear weights; the page records the Zhu–Shu hierarchy to ninth order, ghost candidates, the Wang et al. variant, scale-invariant MR-AWENO, WCNS, learned, shock-detector (MR-WENO-SD), hybrid, moving-mesh, Hermite, entropy-stable and steady-state uses."
status: established
aliases: [multi-resolution WENO, multiresolution WENO, MR-WENO, WENO-MR, WENOZS5, New WENO5, WENOMR, Zhu–Shu WENO, MRWENO, MR-AWENO, MR-AWENO-Si, WCNS-MR, MR-WCNS, hybrid MR-WCNS, GMR-WENO, ghost multi-resolution WENO, MMR-WENO, HMR-WENO, MR-WENO-SD, WCNS3-MR]
tags: [weno, cweno, reconstruction, finite-difference]
timestamp: 2026-10-23T20:37:00Z
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
reprinted by Li, Duan & Tang (2022c, App. A).

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

## Multi-resolution interpolation for A-WENO (MR-AWENO) and its scale-invariant form

Li, Li, Don & Wang (2023a, §2.1) recall the MR-AWENO interpolation of Wang, Zhu, Yang & Zhao (2021) for the
[alternative formulation](/methods/alternative-weno.md): point-value Lagrange interpolants of degree 0, 2,
4 on $T_1$, $T_2$, $T_3$ (Eqs. (12)–(15)), e.g. the interface values
$f_i$, $-\tfrac18f_{i-1}+\tfrac34f_i+\tfrac38f_{i+1}$ and
$\tfrac3{128}f_{i-2}-\tfrac5{32}f_{i-1}+\tfrac{45}{64}f_i+\tfrac{15}{32}f_{i+1}-\tfrac5{128}f_{i+2}$; linear weights
$(1,10,100)/111$; the Legendre-form indicators of the [smoothness indicators](/definitions/smoothness-indicator.md)
page with $\beta_1=\min\big((f_{i-1}-f_i)^2,(f_i-f_{i+1})^2\big)$; the global indicator of Step 4 above;
$\epsilon=10^{-6}$; and the interface value of Step 5 (Eqs. (16)–(25)). *(Compiler check, not in the sources:
up to point values in place of cell averages, the hierarchy, the global indicator and the interface value
coincide with Steps 1–5 above; the CMAME paper of Wang, Zhu, Yang & Zhao is not the ingested Comput. Fluids
paper of Wang et al. 2021.)*

**Not scale-invariant.** Li et al. (2023a) prove that the operator commutes with $f\mapsto\sigma f$ iff its
weights are invariant, iff the unnormalized weights scale by a $k$-independent factor (Theorems 1–2),
and that the MR-AWENO weights fail this for every $\sigma\ne0,\pm1$ (Theorem 3, on data with $\tau\ne0$),
which they trace to the different scalings of $\beta_k$, $\tau$ and $\epsilon$ (§2.3); on the Lax problem scaled by $10^{-7}$ the
scheme oscillates (Fig. 1) ([scale invariance](/properties/scale-invariance.md)).

**MR-AWENO-Si.** The fix has two parts (§2.3): the global indicator is replaced by the squared fifth
undivided difference $\tau^*$ on $T_3\cup\{x_{i+3}\}$ (Eq. (42)), and $\epsilon$ by $\epsilon\,\mathsf m^2$
with the descaler $\mathsf m=\tfrac15\sum_{T_3}|f_j|+10^{-100}$ of [affine-invariant WENO](/methods/affine-invariant-weno.md)
(Eqs. (43)–(44)); Theorem 4 proves scale invariance. In quadruple precision the scale-invariance error is
at round-off for $\sigma\in[10^{-19},10^{19}]$ on sine, ReLU and Heaviside data, while MR-AWENO's vanishes
only at $\sigma=1$ (§2.4, Fig. 3). The two parts act differently: on the scaled Lax problem $\tau^*$ alone
removes the oscillations at $\sigma=1$ but not at $10^{-7}$ (§2.5, Fig. 4,
[ENO property](/definitions/eno-property.md)), so the improvement at $\sigma=1$, where MR-AWENO
already oscillates on the Einfeldt, Sod and Lax problems at $N_x=200$ (§3.2, Fig. 5), comes from $\tau^*$.
Both schemes are fifth order on a 1-D density wave ($L^1$ $6.44\times10^{-11}$ at 320 points, Table 1) and
the [isentropic vortex](/benchmarks/isentropic-vortex.md) (Table 2); MR-AWENO-Si is sharper on
[double Mach reflection](/benchmarks/double-mach-reflection.md) ($1600\times400$), and both run with a
positivity-preserving limiter on [Sedov](/benchmarks/sedov-blast-wave.md) and the Mach 2000
[jet](/benchmarks/high-mach-astrophysical-jet.md) (§3). Scale invariance is what makes the
characteristic-wise scheme well-balanced for the Euler equations with gravity (§4;
[well-balancing](/properties/well-balancing.md)).

## Multi-resolution interpolation in a WCNS, up to the boundary

Qin, Chen, Lin & Deng (2023, §2.1–2.2) use the hierarchy as the interpolation of a fifth-order staggered
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) ("WCNS-MR", after Zhang, Wang & Zhang and Zhu & Shu). The
three point-value candidates at $x_{i+1/2}$ are those of MR-AWENO above, the linear weights
$(1,10,100)/111$, the global indicator that of Step 4 with $\epsilon=10^{-10}$, and the interface value the
simplified combination of Wang et al. (2021), Step 5, which they call more efficient than Zhang et al.'s
(Eqs. (6)–(12)). Two changes are new:

- **Scaled indicators.** $\beta_2$, $\beta_3$ are sums of squared derivatives of $P_2$, $P_3$ at the solution
  point, the $n$th derivative weighted by $\lambda_{\mathrm s}^{n-1}$ (page-local; $\lambda_{\mathrm s}=2$ adopted),
  and $\beta_1$ is the minimum of the squared one-sided divided differences times $\Delta x$
  (Eqs. (13)–(22); [smoothness indicators](/definitions/smoothness-indicator.md)).
- **One-sided hierarchies at the boundary.** At the first and last two flux points the nested stencils become
  one-sided, $T_2$ and $T_3$ including the boundary value $u_{1/2}$ on the left and extrapolating to
  $x_{N+1/2}$ on the right, on the non-uniform "conservative solution points" that make the scheme globally
  conservative; the coefficients are tabulated to 17 digits (Tables 2–9;
  [shock-capturing boundary closure](/methods/shock-capturing-boundary-closure.md)). The authors take the idea from
  a nonlinear spectral difference scheme of Lin, Chen & Deng (§1).

The hierarchy accommodates the truncated stencils because its linear weights need not reproduce a target linear
scheme: the same weights $(1,10,100)/111$ are kept at every point, while only the interpolation coefficients
change. The scheme is fifth order with the closures active (linear advection order 5.01 at $N=320$, Burgers
5.16, 1-D Euler 5.01; Tables 10–12). On the single-domain Lax problem with $\lambda_{\mathrm s}=1$ it is more
oscillatory than characteristic-wise WENO-JS and Zhu & Shu's WENO-MR with the simplified $\beta_1$ of Wang
et al. (2021), which the authors attribute to the wide difference stencil of WCNS; $\lambda_{\mathrm s}=2$
removes the oscillations (§3.4.2, Fig. 6).

## Third-order WCNS hierarchy (WCNS3-MR) and a learned weight

[Fan et al. (2025b)](/sources/fan-2025-b.md) (§2.2, Eqs. (10)–(18)) write the third-order member of the
WCNS hierarchy in the modified form of Qin et al. above, on point values of a staggered grid: $T_1=\{x_i\}$
with $P_1=u_i$ and $T_2=\{x_{i-1},x_i,x_{i+1}\}$ with
$P_2(x_{i+1/2})=-\tfrac18u_{i-1}+\tfrac34u_i+\tfrac38u_{i+1}$; linear weights $d_m=b_{\mathrm{MR}}^{m-1}/\sum_lb_{\mathrm{MR}}^{l-1}$
with a base $b_{\mathrm{MR}}>0$ (page-local), $10$ by default, i.e. $(\tfrac1{11},\tfrac{10}{11})$; $\beta_1$ the
minimum of the two squared one-sided differences and $\beta_2$ Qin et al.'s derivative sum with the
amplifying parameter $\lambda_{\mathrm s}\ge1$; the squared global indicator $\tau_{\mathrm{MR}}=\lvert\beta_2-\beta_1\rvert^2$
(page-local) in Z-type weights with exponent 1 and $\epsilon=10^{-10}$; and the interface value of Step 5.
They record two trade-offs (Remarks 1–2): a larger base gives higher resolution but poorer shock
capturing, a smaller one suppresses oscillations at a cost in resolution, and no single base suits the
whole domain; a larger $\lambda_{\mathrm s}$ improves shock capturing "without sacrificing the design accuracy", a
statement they attribute to Qin et al. and do not test.

Their contribution is to rewrite the two-level combination as a combination of the candidates
themselves, $\omega_1P_1+\omega_2P_2$ with
$\omega_1=\omega^{\mathrm p}_1-\omega^{\mathrm p}_2d_1/d_2$, $\omega_2=\omega^{\mathrm p}_2/d_2$ (Eqs. (19)–(20); $\omega^{\mathrm p}_m$ the
weights of the hierarchical form, page-local), whose optimal weights are $(0,1)$: third order then needs
only $\omega_1=O(\Delta x^2)$, a target that a network with softmax output can meet as a half-line
condition. The network that predicts these weights (WCNS3-MR-NN) and its accuracy to $N=10240$ are on
[learned WENO weights](/methods/learned-weno-weights.md).

## Simplified multi-resolution WCNS interpolation (Wang et al. 2023c)

Wang, Zhu, Wang & Zhao (2023c, §3, Steps 2.1–2.5, Eqs. (3.10)–(3.24)) transpose the hierarchy to the
node-to-midpoint interpolation of an explicit fifth-order
[WCNS](/methods/weighted-compact-nonlinear-scheme.md), simplifying the MR-WCNS of Zhang, Wang & Zhang:

- point-value interpolants of degree 4, 2 and 0 on $T_3$, $T_2$, $T_1$, with midpoint values
  $\tfrac1{128}(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2})$, $\tfrac18(-u_{i-1}+6u_i+3u_{i+1})$ and
  $u_i$ (their stencils are numbered from the largest, $S_1$ five points);
- the CWENO decomposition of the largest polynomial, valid for any linear weights with nonzero
  top weight (Eqs. (3.17)–(3.18); [CWENO](/methods/cweno.md));
- Jiang–Shu indicators for the quartic and the parabola, the latter
  $\tfrac{13}{12}(u_{i-1}-2u_i+u_{i+1})^2+\tfrac14(u_{i+1}-u_{i-1})^2$, and the parameter-free
  $\beta_1=\min\big((u_{i-1}-u_i)^2,(u_i-u_{i+1})^2\big)$ for the constant, which they set against the
  parameter-dependent indicator of Zhang et al. ([smoothness indicators](/definitions/smoothness-indicator.md));
- the global indicator and weights of Step 4 above with $\epsilon=10^{-6}$, default linear weights
  $(1,10,100)/111$ from the smallest to the largest stencil.

*(Compiler check, not in the sources: these interpolants, indicators, global indicator and weights are
those of the MR-AWENO interpolation of the previous section, so Li et al.'s (2023a) Theorem 3 applies and the
interpolation is not scale-invariant.)*

The paper claims that its scheme reaches fifth order with all three tested weight sets,
$(1,10,100)/111$, $(\tfrac13,\tfrac13,\tfrac13)$ and $(100,10,1)/111$ in this page's order, while the
MR-WCNS of Zhang et al. reaches it only with the first, because its pre-defined linear weights "have
a negative impact on the smoothness indicators" (Remark 2, Example 4.1). This is the WCNS counterpart
of the claim of Wang et al. (2021) against the original scheme above, by an overlapping author group.
With the default weights, all schemes are fifth order on 1-D and 2-D Euler and Navier–Stokes density
waves, with errors about one order below WENO-JS ($L^1$ $1.10\times10^{-11}$ against $1.93\times10^{-10}$
at 320 points; Tables 4.1–4.4). A parameter-free linear/nonlinear switch makes the scheme cheaper
than WENO-JS in most runs ([hybrid schemes](/methods/hybrid-weno.md)). On the shock tests (Shu–Osher,
blast waves, double Mach reflection, shock–bubble, Richtmyer–Meshkov, Rayleigh–Taylor, a viscous
shock–mixing layer and the viscous shock tube) both MR-WCNS variants resolve more structure than
WENO-JS, with symmetry errors between $10^{-14}$ and $10^{-7}$ on the symmetric problems (§4;
[symmetry preservation](/properties/symmetry-preservation.md)).

## Hierarchical WCNS-MR as a comparator (Chen & Deng 2023)

Chen & Deng (2023, §2, Eqs. (19)–(24)) use a modified WCNS-MR as comparator of their
[exponential weights](/methods/exponential-nonlinear-weights.md): the equivalent-polynomial form of
the original scheme (the "Indicators that depend on the linear weights" section), with level-wise
weights $(\tfrac1{11},\tfrac{10}{11})$ and $(\tfrac1{111},\tfrac{10}{111},\tfrac{100}{111})$, and weights
$d_{m}\big(1+(\tau/(\tilde\beta_m+\epsilon))^2\big)$ with $\tau=|\tilde\beta_3-\tilde\beta_2|$ and
$\epsilon=10^{-40}$ (page-local $\tilde\beta_m$ the indicators of the nested interpolants). They state
that these differ "slightly" from the published scheme, to reduce oscillations. It is the most
dissipative of their four weightings in the approximate dispersion relation, drops to third order at
a first-order critical point, and costs about 2.5 times WCNS-JS (273.04 s against 110.06 s on Sod at
$N_x=1000$; §3, §4.1–4.2, Table 1; [accuracy at critical points](/properties/critical-point-accuracy.md)).

## Two levels on moving quadrilaterals (Gu et al. 2023)

Gu, Li, Cheng & Shu (2023, §2.4) use a third-order two-level hierarchy in a finite-volume scheme that
remaps cell averages by solving $\partial_tu=0$ on a moving mesh
([conservative remapping](/methods/conservative-remapping.md)):

- $T_1$ the cell itself with $P_1=\bar u_{i,j}$, and $T_2$ the $3\times3$ block with a quadratic fitted
  by constrained least squares, exact on the cell's own average;
- $P_2$ replaced by $P_2/d_2-(d_1/d_2)P_1$, linear weights $(\tfrac1{11},\tfrac{10}{11})$ "as a good
  balance": a larger top weight improves smooth accuracy but may oscillate;
- an area-scaled Jiang–Shu indicator for the quadratic and, for the constant,
  $\beta_1=\min\{\mathsf z_1+\mathsf z_2,\mathsf z_2+\mathsf z_3,\mathsf z_3+\mathsf z_4,\mathsf z_4+\mathsf z_1\}$ with $\mathsf z_l$ the four
  squared differences to the face neighbours (page-local $\mathsf z_l$; the source's $\zeta$), after Zhu & Shu, because $\beta_1=0$
  "does lead to more smearing" at strong shocks and contacts;
- weights $d_m\big(1+(\tau/(\beta_m+\epsilon))^2\big)$, $\tau=|\beta_2-\beta_1|$, $\epsilon=10^{-3}$.

The authors find the hierarchy "particularly suitable" for moving meshes because the linear weights
do not depend on the cell geometry and need not be recomputed as the cells deform. Without limiter
the remap converges at $L^1$ orders 2.7–3.6 on smoothly moving meshes, 3.5–4.2 on random ones and
2.5–3.4 on a mesh whose nodes travel more than one cell, and nearly the same with a
[Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md) on density and internal energy
(Tables 3.1–3.3), without oscillations at discontinuities (§3.2). *(Compiler check, not in the
sources: this is the third-order hierarchy with a first-order base polynomial whose loss of order
Balsara et al. report below; on the $20^2$–$320^2$ meshes of Tables 3.1–3.3 no $L^1$ order falls
below 2.48.)*

## The hierarchy up to ninth order (Zuo & Zhu 2024a, 2024b)

Zuo & Zhu (2024a, §2.1, Eqs. (2.8)–(2.19); 2024b, §2.1, Eqs. (2.8)–(2.14)) recall the finite-difference
Zhu–Shu scheme at orders 3, 5, 7, 9 as the nonlinear part of their hybrid schemes:

- nested central stencils $T_1,\dots,T_5$ of 1, 3, 5, 7, 9 points (their $T_r=\{I_{i-r},\dots,I_{i+r}\}$,
  $r=0,\dots,4$), degree-$2(m-1)$ polynomials in the monomial basis about $x_i$, and the CWENO rewriting
  level by level, $\tilde P_m=P_m/d_{m,m}-\sum_{l<m}(d_{l,m}/d_{m,m})\tilde P_l$ with level-wise linear weights
  $d_{l,m}\propto10^{l-1}$ (page-local double index: stencil $l$, level $m$);
- Jiang–Shu indicators on the rewritten polynomials, and a "special" base indicator that Zuo & Zhu
  (2024a, Eqs. (2.12)–(2.16)) print: with $\zeta_{\mathrm L}=(f_i-f_{i-1})^2$, $\zeta_{\mathrm R}=(f_{i+1}-f_i)^2$,
  unnormalized weights 10 and 1 given to the smaller and the larger of the two (Eq. (2.13)), and WENO-Z-type factors
  $1+|\zeta_{\mathrm L}-\zeta_{\mathrm R}|^{m_\zeta}/(\zeta+\epsilon)$, $\beta_1$ is the square of the weighted mean of
  the two one-sided differences, with "$m_\zeta=1,2,3,4$" not assigned to the orders (page-local
  $\zeta_{\mathrm L},\zeta_{\mathrm R},m_\zeta$);
- WENO-Z-type weights $d_{l,m}\big(1+\tau_m/(\epsilon+\beta_l)\big)$, $\epsilon=10^{-10}$, with a global
  indicator whose power grows with the level,
  $$\tau_m=\Big(\frac1{m-1}\sum_{l<m}|\beta_m-\beta_l|\Big)^{m-1}$$
  (page-local, their $\ell_2=m-1$; [WENO-Z](/methods/weno-z.md)). *(Compiler check, not in the sources: the
  ratio $\tau_m/(\epsilon+\beta_l)$ is then of degree $2(m-1)-2$ in the data, 0 at third order, 2 at fifth,
  4 at seventh, 6 at ninth, so only the third-order weights are scale-invariant, and only for $\epsilon=0$;
  [scale invariance](/properties/scale-invariance.md).)*

In their accuracy tables the original fifth-order scheme converges erratically on the 2-D Euler density
wave, $L^1$ orders 2.52, 7.58, 5.98, 8.66, 5.55 from $10^2$ to $60^2$, printed identically in both papers
(2024a, Table 3.3; 2024b, Table 3.3), and on the 3-D wave (4.73, 5.69, 7.60, 5.00, 4.98 in $L^1$, 2024b,
Table 3.4), while their hybrid versions, which use the linear upwind scheme in smooth cells, give clean
orders 4.89–5.00 with smaller errors on coarse grids; at seventh and ninth order the two coincide to the
printed digits on fine grids. The authors do not comment on the erratic orders. The hybrid switches, a
parameter-free extreme-point detector in the target cell, save 63–79 % (2024a) and 22–75 % (2024b) of the
CPU time ([hybrid schemes](/methods/hybrid-weno.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Ghost multi-resolution WENO (Zhang & Zhu 2024)

Zhang & Zhu (2024) build the lower levels of the hierarchy without lower stencils. For order
$k\in\{3,5,7\}$ one polynomial $P^{(k)}_1$ of degree $k-1$ matches the cell averages on the $k$-cell central
stencil and is written in the Legendre basis of the target cell, $\xi=(x-x_i)/\Delta x$,
$L_0=1$, $L_1=\xi$, $L_2=\xi^2-\tfrac1{12}$, $L_3=\xi^3-\tfrac3{20}\xi$, $L_4=\xi^4-\tfrac3{14}\xi^2+\tfrac3{560}$,
$L_5=\xi^5-\tfrac5{18}\xi^3+\tfrac5{336}\xi$, $L_6=\xi^6-\tfrac{15}{44}\xi^4+\tfrac5{176}\xi^2-\tfrac5{14784}$,
$P^{(k)}_1=\bar u_i+\sum_{r=1}^{k-1}A^{(k)}_rL_r$ (page-local $L_r$, $A^{(k)}_r$; Eqs. (2.4)–(2.25)). The
"ghost" candidates $P^{(k)}_\ell$, $\ell=2,\dots,k$, are its $L^2(I_i)$ projections on degree $k-\ell$, obtained by
dropping the top Legendre modes, so there are $k$ candidates of every degree from $k-1$ down to 0, all with
the cell average $\bar u_i$ (Remark 1); they "could not be constructed by directly utilizing the information
defined on real spatial stencils" (§1). The fifth-order coefficients $A^{(5)}_r$ are those of $\mathsf b_r$ in the
recipe of Wang et al. above. *(Compiler check, not in the sources: the two sets of printed coefficients agree
term by term.)* The candidates are combined in the CWENO form, with any positive linear weights (used:
$10{:}5{:}1$, $100{:}25{:}10{:}5{:}1$, $1000{:}125{:}100{:}25{:}10{:}5{:}1$ from the top polynomial down),
Jiang–Shu indicators written as sums of squares of Legendre coefficients, and
$$\alpha_r=d_r\Big(1+\frac{\tau_k}{\epsilon+\beta_r}\Big),\qquad
\tau_k=\Big(\frac1{k-1}\sum_{l=2}^k|\beta_1-\beta_l|\Big)^{(k-1)/2},\qquad\epsilon=10^{-6}$$
(page-local $\tau_k$; Eqs. (2.26)–(2.30)), in finite-difference form (Lax–Friedrichs splitting) and in
finite-volume form (dimension by dimension, Gauss points on faces) with TVD-RK3 at CFL 0.6 and
$\Delta t\sim\Delta x^{k/3}$ in the accuracy tests.

The fifth- and seventh-order errors equal those of the original multi-resolution WENO to the printed digits
on [Burgers](/benchmarks/burgers-equation-tests.md) and Euler [density waves](/benchmarks/density-wave-advection.md)
(e.g. $L^1$ $2.27\times10^{-8}$ for both at 200 points, Table 3.2), the third-order ones are about half
($1.27\times10^{-5}$ against $2.25\times10^{-5}$), with observed third-order $L^1$ rates up to 4.53 and
$L^\infty$ rates 2.25–3.37 on the meshes used (Tables 3.2–3.9). The CPU ratio to the original scheme is
1:1.23 to 1:2.18 in finite differences and 1:1.27 to 1:2.25 in finite volumes on the shock tests (Table 3.1;
Intel Core i5-8265U, Visual Fortran), and figures show better resolution on
[Shu–Osher](/benchmarks/shu-osher-problem.md), Titarev–Toro, [blast waves](/benchmarks/woodward-colella-blast-wave.md)
and [double Mach reflection](/benchmarks/double-mach-reflection.md), with both schemes running the
[Sedov problem](/benchmarks/sedov-blast-wave.md) and a [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
The authors claim "the first time that only one central spatial stencil is utilized in designing high-order
finite difference and finite volume WENO schemes" (Abstract). *(Compiler check, not in the sources: the CWENO and WENO-ZQ reconstructions of the
bundle ([CWENO](/methods/cweno.md)) also centre on one large stencil, but their low-order candidates live on
real substencils, so the new element is the projected candidates.)*

**Two-stencil variant on triangles.** Lin & Zhu (2024) keep only the one-cell stencil and the top stencil of
the triangular Zhu–Shu hierarchy and adapt the two linear weights cell by cell; the scheme is recorded on the
[CWENO](/methods/cweno.md) page. Fan & Wu (2024) use a nested quintic–cubic–linear Hermite hierarchy with
arbitrary linear weights in their OE-HWENO ([Hermite WENO](/methods/hermite-weno.md)).

## Weights from a shock detector: MR-WENO-SD (Ren et al. 2025)

[Ren et al. (2025)](/sources/ren-2025.md) (§5.1.1, Eqs. (41)–(49)) use the fifth-order finite-volume
hierarchy (degrees 0, 2, 4 on $T_1$, $T_2$, $T_3$, after Zhu & Shu, Cui & Zhu and Wang et al. 2021) with
the indicators of Step 3, $\beta_1=\min\big((\bar u_i-\bar u_{i-1})^2,(\bar u_i-\bar u_{i+1})^2\big)$, the global
indicator of Step 4 and Z-type weights, and write the result as weights $\omega^{\mathrm P}_m$ (page-local) on
the three polynomials themselves. Their [matrix stability analysis](/methods/matrix-stability-analysis.md)
of the [carbuncle](/definitions/carbuncle-phenomenon.md) on a planar Mach 20 normal shock examines these
weights inside the numerical shock structure, where every candidate but the constant contains the jump:

- with the level-wise weights $10^m$ the polynomial weights at the face next to the shock are
  $(0.21940,0.22749,0.55311)$ (constant, quadratic, quartic), and the steady shock shows a "subtle"
  non-carbuncle anomaly (Table 4, Fig. 32a);
- with equal level-wise weights they become $(0.85337,0.08849,0.05815)$ and the normal shock is stable,
  but the residual of the blunt-body problem does not reach machine zero (Table 5, Figs. 32b, 33–34).

The authors recall from the multi-resolution literature that the linear weights of the hierarchy are not unique and that
larger weights on the higher-degree polynomials sharpen shocks (§5.1.1); in their Table 5 it is the choice that gives the
constant the largest weight at the shock that is stable. **MR-WENO-SD** sets the polynomial weights directly from a pressure-jump shock
detector of the faces, page-local
$$f_{\mathrm{SD},i+1/2}=\Big(1-\exp\Big(-\max(M_i,M_{i+1})\,\frac{\lvert p_i-p_{i+1}\rvert}{p_i+p_{i+1}}\Big)\Big)^4,$$
the exponent 4 "to ensure spatial accuracy": with $\bar w_0$ the maximum of $f_{\mathrm{SD}}$ over the four transverse
faces of the two cells, $\bar w_1=\max(f_{\mathrm{SD},i-1/2},f_{\mathrm{SD},i+1/2})$ and $\bar w_2=\max(f_{\mathrm{SD},i-3/2},f_{\mathrm{SD},i+3/2})$
(page-local),
$$\omega^{\mathrm P}_1=\max(\bar w_0,\bar w_1),\qquad\omega^{\mathrm P}_2=\big(1-\omega^{\mathrm P}_1\big)\bar w_2,\qquad\omega^{\mathrm P}_3=\big(1-\omega^{\mathrm P}_1\big)(1-\bar w_2),$$
so that a shock on the adjacent faces (or on the transverse faces) selects the constant, a shock two faces
away the quadratic, and otherwise the quartic; the weights sum to one by construction (Eqs. (47)–(49)).
No smoothness indicator enters. At the same face as above the weights are
$(0.99999999,\,1.98\times10^{-14},\,1.27\times10^{-8})$ (Table 6). The scheme is paired with an HLLC/HLL
flux blended by the same detector ([HLL-family solvers](/methods/hll-riemann-solvers.md)), and is also used
for the in-cell Gauss-point values of the two-point face quadrature (§5.2.3).

*Evidence* (§5.2). Fifth order on a 1D density wave, $L_1$ orders 4.9055–5.0290 and $L_\infty$ orders
4.8084–4.9973 for 10 to 320 cells (Table 7); all eigenvalues of the analysed $50\times25$ normal shock in the
left half-plane (Fig. 35); stable runs where WENO with HLLC is unstable on the inviscid Mach 20 cylinder
(Figs. 36–37), the double Mach reflection, the Sedov blast at $960\times960$ (Fig. 40) and a viscous Mach 8.1
cylinder, whose stagnation heat flux is within 0.81% of the Fay–Riddell value (Figs. 41–42). *(Compiler
check, not in the sources: the accuracy test has $p\equiv1$, so $f_{\mathrm{SD}}\equiv0$ and the reconstruction there
is the linear quartic; the fifth order of Table 7 does not exercise the detector-based weighting, whose effect
on smooth flows with pressure variation is not tested.)*

## Hermite and moment-based hierarchy

Li, Shu & Qiu (2022d, §2.1, Eqs. (2.9)–(2.24)) build a sixth-order finite-volume hierarchy on the
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
in the slopes ([TVD limiters](/definitions/total-variation-diminishing.md)). Wang et al. (2021) and Li,
Shu & Qiu (2022d) use one-point base polynomials at fifth and sixth order, with $\beta_1$ built from
one-sided differences; their tests show the design orders, so the third-order defect of Balsara et
al. is not contradicted at those orders.

## Linear weights and robustness

The sources agree that the linear weights do not affect smooth-region accuracy but do affect shocks:
- a larger weight on the largest stencil gives sharper discontinuities but "tends to oscillate"
  (Wang et al. 2021, §3.1.1 Step 3; Li, Duan & Tang 2022c, App. A step 3; Li, Shu & Qiu 2022d, Remark 1,
  where larger weights on higher-degree polynomials make "the more unstable the scheme becomes", and
  §1, where the gap between linear weights "cannot be too large");
- on the Sedov, double-rarefaction and Leblanc problems Wang et al. (2021, Example 5.5) state that
  their weight ratio "is so large that it cannot directly and robustly solve such extreme problems"
  and revert to the weights of the original scheme; no positivity limiter is used
  ([Sedov blast wave](/benchmarks/sedov-blast-wave.md),
  [double rarefaction](/benchmarks/double-rarefaction-problem.md),
  [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md));
- Li, Duan & Tang (2022c, §5) use $(1,10,100)/111$ by default and $(0.95,0.045,0.005)$ in three
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
- **Entropy-stable dissipation.** Li, Duan & Tang (2022c, §3.4, Eq. (3.21)) reconstruct the jump of
  scaled entropy variables in a TeCNO-type entropy-stable flux with this fifth-order scheme
  ([TeCNO schemes](/methods/tecno-scheme.md),
  [adaptive moving mesh](/methods/adaptive-moving-mesh.md)). Against the same scheme with WENO-JS,
  it "better capture[s] the localized structures" (Remark 3.2); the printed timings (Tables 5.1–5.2)
  are 2m56s vs 2m37s, 2m50s vs 2m38s, 13m53s vs 13m52s and 3m21s vs 3m3s, i.e. 0.1–12 % more
  *(compiler check, not in the sources: ratios of the printed timings)*.

**Steady states.** Wan & Xia (2022, §2.4, Eqs. (2.31)–(2.45)) reprint the finite-difference Zhu–Shu
scheme ("MRWENO"), with the original equivalent polynomials, linear weights $1,10,100$ (normalized) and
a weighted base indicator built from the two one-sided differences, as a comparator for steady Euler
problems: its residue stalls at about $10^{-3.5}$ on the $400^2$ plate problems, does not converge on a 3-D plate, and on
the [forward-facing step](/benchmarks/forward-facing-step.md) it converges only with the Lax–Friedrichs
speed enlarged by 10 % (Examples 4.5, 4.7–4.8, 4.15; [hybrid schemes](/methods/hybrid-weno.md)). Their
§1 credits it with "lovely convergence" but oscillations near discontinuities, where it behaves almost
like a linear scheme.

**On triangles.** Ji, Liang & Fu (2022, §5.8) state, by comparison with the published figure, that their
unstructured fifth-order TENO at $h\approx1/200$ resolves double Mach reflection comparably to Zhu & Shu's
triangular multi-resolution WENO5 at $h\approx1/320$; the codes and fluxes differ. Balsara, Samantaray &
Subramanian (2023, §6.3) name the Zhu–Shu scheme as an efficient alternative for prolongation.

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
- Li, Duan & Tang (2022c, App. A) phrase the algorithm "for the given cell average values"; applied
  to finite-difference point values it rests on the reading that Wang et al. (2021, §3.1.1) state,
  point values interpreted, as in FD-WENO, as cell averages of the primitive function.
- The claim against the original multi-resolution WENO is made by Wang et al. with Zhu, a co-author
  of the original; Balsara et al.'s third-order fix is likewise made by a group including Shu.
  Neither is an independent test, and the original Zhu–Shu paper is not ingested.
- *(Compiler check, not in the sources.)* Li et al.'s ratio (Eq. (41)),
  $\alpha_k[\sigma f]/\alpha_k[f]=1+(\sigma^2-1)\frac{\tau}{\tau+\beta_k+\epsilon}\big(1+\frac{\epsilon}{\beta_k+\epsilon/\sigma^2}\big)$,
  is exact for $\beta_k$ quadratic and $\tau$ quartic in the data, and depends on $k$ even for $\epsilon=0$.
- Li et al. (2023a, §5.2) call the polytropic accuracy result "super-convergence behavior like the spectral
  method": the printed order 12.55 comes from a well-balanced error of $7.49\times10^{-4}$ at $N=32$,
  after which the errors equal those of the non-well-balanced scheme (Table 6). On the vortex at $160^2$
  the MR-AWENO-Si error is $3.09\times10^{-6}$ against $1.05\times10^{-7}$ for MR-AWENO (Table 2).
- Balsara et al. (2024, Table III) contain an unexplained rate of 12.06 for ninth-order
  multi-resolution WENO.
- Wang et al. (2023c) show the failure of Zhang et al.'s MR-WCNS with the two non-default weight sets
  only in CPU-versus-error figures (Figs. 4.1–4.4), with no tabulated errors; no bundle source states the
  contrary.
- Wang et al. (2023c, Eq. (3.20)) print the explicit quartic indicator without the cross term
  $-3495756\,u_iu_{i+1}$ (prefactor $\tfrac1{60480}$). *(Compiler check, not in the sources: the integral
  definition gives this term, mirror image of the printed $-3495756\,u_{i-1}u_i$, and without it the
  printed form does not vanish on constant data.)*

- Zhang & Zhu (2024, Eq. (2.27)) print the indicator sum up to "$l=2(r-1)$", which in their indexing, where
  $P^{(k)}_r$ has degree $k-r$, is empty for the top polynomial; it is MR-WENO's increasing-degree count. Their
  claim that accuracy decreases "gradually" to first order near strong discontinuities (§1, §4) is not tested.
  *(Compiler check, not in the sources: every ghost candidate except the constant is a truncation of the
  polynomial on the whole stencil, so all of them see a discontinuity anywhere in the stencil, and the
  non-oscillatory fallback is to the constant.)* Tables 3.8–3.9 label both column groups "MR-WENO"; the left
  ones carry the smaller third-order errors that the text attributes to the ghost schemes. Zuo & Zhu (2024a) and (2024b) sum the global indicator up to $\ell_2$ and to
  $\ell_2-1$, the same quantity since the extra term vanishes.

# Citations

- [Wang et al. (2021)](/sources/wang-2021.md) — §1; §3.1.1, Steps 1–7, Eqs. (3.2)–(3.28), Remark 2; §4, Fig. 4.1; §5.1, Tables 5.1–5.6, Figs. 5.1–5.6; Examples 5.4–5.13; §5.4, Table 5.8; §6.
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — §3.4, Eq. (3.21), Remark 3.2; §5, Tables 5.1–5.2; App. A.
- [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md) — §1; §2.1, Eqs. (2.9)–(2.24), Remark 1; §2.2, Eqs. (2.42)–(2.56).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I; §VII.a–b, Tables I, III; App. D, Eqs. (D.7)–(D.10).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §1.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1.
- [Li, Li, Don & Wang (2023a)](/sources/li-2023.md) — §1; §2.1–2.5, Eqs. (12)–(46), Theorems 1–4, Figs. 1–4; §3, Tables 1–2, Figs. 5–8; §4; §5, Table 6.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §1; §2.4, Eqs. (2.31)–(2.45); §4, Examples 4.5, 4.7–4.8, 4.15.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.8.
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §6.3.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §1; §3, Steps 2.1–2.5, Eqs. (3.10)–(3.24), Remark 2; §4, Example 4.1, Tables 4.1–4.4, Figs. 4.1–4.4; §5, Table 5.1.
- [Chen & Deng (2023)](/sources/chen-2023.md) — §2, Eqs. (19)–(24); §3, Fig. 1; §4.1–4.2, Table 1.
- [Gu et al. (2023)](/sources/gu-2023.md) — §1; §2.4; §3.1–3.2, Tables 3.1–3.3.
- [Qin, Chen, Lin & Deng (2023)](/sources/qin-2023.md) — §1; §2.1, Eqs. (6)–(22); §2.2, Tables 2–9; §3, Tables 10–12, Fig. 6.
- [Zuo & Zhu (2024a)](/sources/zuo-2024.md) — §2.1, Eqs. (2.8)–(2.19); §3, Tables 3.1–3.4.
- [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) — §2.1, Eqs. (2.8)–(2.14); §3, Tables 3.1–3.4.
- [Zhang & Zhu (2024)](/sources/zhang-2024-c.md) — Abstract; §1; §2.1–2.2, Eqs. (2.4)–(2.36), Remark 1; §3, Tables 3.1–3.9, Examples 3.1–3.10; §4.
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §1; §2.
- [Fan & Wu (2024)](/sources/fan-2024.md) — §2.2.1, App. A (arXiv v1).
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §2.2, Eqs. (10)–(18), Remarks 1–2; §3, Eqs. (19)–(21): third-order WCNS3-MR and its candidate-weight form.
- [Ren et al. (2025)](/sources/ren-2025.md) — §5.1.1, Eqs. (41)–(49), Tables 4–6, Figs. 32–34; §5.2, Table 7, Figs. 35–42: weights inside the numerical shock structure, MR-WENO-SD.
