---
type: Definition
title: "Smoothness indicators"
description: "A smoothness indicator β_k is a quadratic functional of the data on candidate stencil S_k, O(Δx²) on smooth data and O(1) across a jump; the Jiang–Shu form underlies WENO, TENO, CWENO and Hermite-WENO weights, with variants for one-point bases, multi-dimensional and time stencils; the term also names unrelated sensors."
status: established
aliases: [smoothness indicator, local smoothness indicator, LSI, IS_k, Jiang–Shu indicator, global smoothness indicator, oscillation indicator, reference smoothness indicator]
tags: [reconstruction, weno, teno, cweno]
timestamp: 2026-10-22T20:00:00Z
---

# Smoothness indicators

A smoothness indicator $\beta_k$ measures how far the data on a candidate stencil $S_k$ are from
smooth. It enters the nonlinear weights of [WENO](/methods/weno-js-reconstruction.md) as
$\alpha_k\propto d_k/(\beta_k+\epsilon)^q$ and the scale-separated measure $\gamma_k$ of
[TENO](/methods/targeted-eno.md). Its defining behaviour: on smooth data $\beta_k=O(\Delta x^2)$ (all
$\beta_k$ sharing their leading term), while a stencil crossed by a discontinuity has
$\beta_k=O(1)$, so its weight is driven towards zero (the
[ENO property](/definitions/eno-property.md)).

## Jiang–Shu form

The form used by nearly every source of the bundle is that of Jiang & Shu (Li et al. 2022, Eq. (7);
Wang & Don 2022, Eq. (8); Fu 2023, Eq. (7); Fu 2021, Eq. (12); Takagi et al. 2022, Eq. (9)): with
$\hat f_k(x)$ the degree-$(r_k-1)$ candidate polynomial of $S_k$ on cell $I_i$,

$$\beta_k=\sum_{j=1}^{r_k-1}\Delta x^{2j-1}\int_{x_{i-1/2}}^{x_{i+1/2}}\Big(\frac{d^j\hat f_k}{dx^j}\Big)^2dx .$$

It is a sum of scaled squared $L^2$ norms of all derivatives of the candidate, hence a quadratic form
in the stencil values. For the three-point stencils of fifth-order WENO, in the Jiang–Shu labelling
($S_0$ most upwind; Luo & Wu 2021, Eq. (5)):

$$\begin{aligned}
\beta_0&=\tfrac{13}{12}(f_{i-2}-2f_{i-1}+f_i)^2+\tfrac14(f_{i-2}-4f_{i-1}+3f_i)^2,\\
\beta_1&=\tfrac{13}{12}(f_{i-1}-2f_i+f_{i+1})^2+\tfrac14(f_{i-1}-f_{i+1})^2,\\
\beta_2&=\tfrac{13}{12}(f_i-2f_{i+1}+f_{i+2})^2+\tfrac14(3f_i-4f_{i+1}+f_{i+2})^2 .
\end{aligned}$$

The same three expressions appear in TENO papers under the central-first labelling
(Fu 2021, Eq. (28); Takagi et al. 2022, Eq. (10); Ye et al. 2022, Eq. (5)). On the compact two-point
stencils of third-order WENO they reduce to $\beta_0=(\bar u_{i-1}-\bar u_i)^2$,
$\beta_1=(\bar u_i-\bar u_{i+1})^2$ (Deng 2023, Eq. (4.22); Huang et al. 2026, Eq. (3.4); Bezgin,
Schmidt & Adams 2022, Eq. (10)). For the point-value *interpolation* of the alternative formulation,
Chu, Kurganov & Na (2022, Eqs. (3.6)–(3.7)) use the same three fifth-order expressions, and reuse them
unchanged for the interpolation to the quarter points $x_{i\mp1/4}$, where only the linear weights
change ([alternative WENO](/methods/alternative-weno.md)).

**Difference-operator form.** In WCNS interpolation, Hiejima (2022, Eq. (14)), after Deng & Zhang,
sums the unweighted squares of the scaled finite-difference derivatives of the candidate,
$\beta_k=\sum_n\big[\mathsf D^n_k\big]^2$, over the derivative orders the substencil supports, where
$\mathsf D^n_k$ is the difference approximation of $\Delta x^n\partial_x^nu$ at $x_i$ on $S_k$
(page-local, as on the source page; $u$ one primitive variable, interpolated componentwise). On
$\{i-1,i,i+1\}$ it is $\big[\tfrac12(u_{i+1}-u_{i-1})\big]^2+(u_{i-1}-2u_i+u_{i+1})^2$. *(Compiler check, not in the
sources: the Jiang–Shu $\beta_1$ above is the same expression with the second-difference square weighted
by $\tfrac{13}{12}$ instead of 1.)* Hiejima applies it to substencils of 3 to $(K+3)/2$ points, $K$ the size of his full stencil.

**Wider stencils.** Ye et al. (2022, Eq. (5)) give the four-point indicators of TENO7, e.g. for
$\{i,\dots,i+3\}$

$$\beta=\tfrac1{36}(-11f_i+18f_{i+1}-9f_{i+2}+2f_{i+3})^2+\tfrac{13}{12}(2f_i-5f_{i+1}+4f_{i+2}-f_{i+3})^2+\tfrac{781}{720}(-f_i+3f_{i+1}-3f_{i+2}+f_{i+3})^2 .$$

Fu (2021, Eq. (28)) prints the six-, eight- and ten-point indicators of TENO-AA as rational quadratic
forms (prefactors $1/120960$, $1/62270208000$, $1/8002967132160000$); the six-point one is the
indicator $\beta_6$ that Ye et al. (2022, Eq. (29)) attribute to [WENO-CU6](/methods/weno-cu6.md).
*(Compiler check, not in the sources: the four-point form above and the six-point $\beta_6$ of Ye et
al. were recomputed from the integral definition and agree exactly.)*

**Legendre form.** Li et al. (2022, Eqs. (8)–(11)), after Balsara et al., expand the candidate in
the rescaled Legendre basis $1,\ X,\ X^2-\tfrac1{12},\ X^3-\tfrac3{20}X$ on
$[-\tfrac12,\tfrac12]$ (page-local $X=(x-x_i)/\Delta x$; the registry keeps $\xi_j$ for DG nodes) with modal coefficients $p^{[l]}_k$; for $r=4$

$$\beta_k=\Big(p^{[1]}_k+\tfrac{1}{10}p^{[3]}_k\Big)^2+\tfrac{13}{3}\big(p^{[2]}_k\big)^2+\tfrac{781}{20}\big(p^{[3]}_k\big)^2 .$$

*(Compiler check: this equals the Jiang–Shu integral exactly.)* Balsara et al. (2024, §I) stress that
indicators written as sums of perfect squares cost few operations, which they credit with improving
the speed and stability of high-order FD-WENO; they extend the closed forms to finite volumes.
For the quartic on a five-point central stencil, with the further basis function
$X^4-\tfrac3{14}X^2+\tfrac3{560}$ and modal coefficients $p^{[l]}$ (written $\mathsf a_l$, $\mathsf b_l$ on the
multi-resolution WENO page), Wang et al. (2021, Eq. (3.11))
and Li, Duan & Tang (2022, Eq. (A.2)) print

$$\beta=\Big(p^{[1]}+\tfrac1{10}p^{[3]}\Big)^2+\tfrac{13}{3}\Big(p^{[2]}+\tfrac{123}{455}p^{[4]}\Big)^2+\tfrac{781}{20}\big(p^{[3]}\big)^2+\tfrac{1421461}{2275}\big(p^{[4]}\big)^2,$$

and $\beta=(p^{[1]})^2+\tfrac{13}{3}(p^{[2]})^2$ for the parabola on three points; these are the
indicators of [multi-resolution WENO](/methods/multi-resolution-weno.md). *(Compiler check, not in
the sources: the quartic form equals the Jiang–Shu integral exactly.)*

**Other forms recalled.** Li et al. (2022, Eq. (6)) recall the earlier Liu–Osher–Chan indicator, a
sum of squared undivided differences of all orders below $r$. Fu (2023, §2.2) notes that improved
indicators developed for WENO can be used in TENO unchanged.

## Indicators of one- and two-point candidates

The Jiang–Shu form vanishes identically on a constant candidate, so schemes whose hierarchy starts
from one point need another base indicator:

- Wang et al. (2021, Eq. (3.12)) and Li, Duan & Tang (2022, App. A) take
  $\beta=\min\big((f_i-f_{i-1})^2,(f_{i+1}-f_i)^2\big)$, which, in Li, Duan & Tang's words, "avoids
  the zero value" of the Jiang–Shu form on the constant;
- Li, Shu & Qiu (2022, Eqs. (2.14)–(2.20)) combine the two one-sided linear polynomials with WENO-Z
  weights and take the Jiang–Shu indicator of the combination,
  $\beta=\big(\omega_{\mathrm L}(\bar u_i-\bar u_{i-1})+\omega_{\mathrm R}(\bar u_{i+1}-\bar u_i)\big)^2$
  (page-local $\omega_{\mathrm{L,R}}$), and in 2-D four L-shaped linear polynomials
  (Eqs. (2.49)–(2.55)).

Wang et al. (2021, §3.1.1, Remark 2) argue that indicators computed on the original Zhu–Shu
"equivalent polynomials", which contain the linear weights, "misjudge" smoothness for some weight
choices and cost accuracy; their indicators act on the candidate polynomials themselves.

On two-point stencils the indicator is the squared difference. Wong, Angel, Barad & Kiris (2021,
Eqs. (94)–(99)) use $(u_i-u_{i+1})^2$ and $(u_{i-1}-u_i)^2$ for the two-point stencils of their
incremental-stencil interpolation, the Jiang–Shu three-point indicators for the others, and an extra
three-point indicator on $\{i-1,i,i+1\}$ that enters only the weights of the two-point stencils. Their
global indicator, taken from TENO (Eqs. (100)–(101)), keeps only the third and fourth derivatives of
the five-point interpolant $\tilde u^{(5)}$:

$$\tau^{\mathrm{ref}}_5=\sum_{l=3}^4\int\Delta x^{2l-1}\big(\partial_x^l\tilde u^{(5)}\big)^2dx
=\tfrac{13}{12}(u_{i+2}-4u_{i+1}+6u_i-4u_{i-1}+u_{i-2})^2+\tfrac14(u_{i+2}-2u_{i+1}+2u_{i-1}-u_{i-2})^2,$$

with $\tau^{\mathrm{ref}}_5=(u_i''')^2\Delta x^6+O(\Delta x^8)$ (App. B, Eq. (B.20)) (page-local symbol;
it is not the WENO-Z $\tau_5=|\beta_0-\beta_2|$ of the registry). *(Compiler check: the closed form
was recomputed from the integral; it agrees.)*

**Wider stencils for sensors.** Zheng, Shu & Qiu (2021, §2.2.4) evaluate Jiang–Shu indicators with
derivatives up to fifth order over $[x_i,x_{i+1}]$, not over a cell, for the quintic on
$\{x_{i-2},\dots,x_{i+3}\}$ and the four quadratics on its three-point substencils; the quintic's
indicator is printed as a sum of five squares with prefactors $1$, $\tfrac{13}{3}$, $\tfrac{781}{20}$,
$\tfrac{1421461}{2275}$ and $\tfrac{21520059541}{1377684}$. Their WENO-Z-like combination of these
indicators is a discontinuity indicator, not a weight
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Behaviour in smooth regions

For $r=4$, Li et al. (2022, Eq. (16)) give
$\beta_k=f'^2\Delta x^2+\tfrac{13}{12}f''^2\Delta x^4+a_kf'f^{(4)}\Delta x^5+\dots$ with $k$-dependent
$a_k$; Ye et al. (2022, Eqs. (25), (30)) give the fifth- and sixth-order expansions. The leading term
is common to all stencils, which is what allows global indicators $\tau$ built from differences of
$\beta_k$ to be of higher order: $\tau_5=|\beta_0-\beta_2|=O(\Delta x^5)$ for
[WENO-Z](/methods/weno-z.md), $\tau_6=\big|\beta_6-\tfrac16(\beta_0+\beta_2+4\beta_1)\big|=O(\Delta x^6)$
for WENO-CU6 and sixth-order TENO (Ye et al. 2022, Eqs. (28), (39), translated here to the Jiang–Shu
labelling). At an $m$th-order
critical point the leading term drops to $O(\Delta x^{2m+2})$, and the ratios $\tau/\beta_k$ that
control the weights lose orders ([critical-point accuracy](/properties/critical-point-accuracy.md);
[WENO-ZN](/methods/weno-zn.md) replaces $\tau$ by an undivided difference for that reason).

Scaling: $\beta_k[\sigma f+\mu]=\sigma^2\beta_k[f]$ for constants $\sigma$, $\mu$ (page-local; Wang
& Don 2022, Eq. (18)). This quadratic scaling against an absolute $\epsilon$ is the source of the
scale dependence of classical weights ([scale invariance](/properties/scale-invariance.md)).

## Indicators on element methods

Kuzmin & Vedral (2023, Eq. (10)) use, for a polynomial $v$ on a finite element $K_e$ in $d$
dimensions, the scaled Sobolev seminorm

$$\|v\|_e=\Big(\sum_{1\le|\mathbf k|\le N}h_e^{2|\mathbf k|-d}\int_{K_e}|D^{\mathbf k}v|^2dx\Big)^{1/2},$$

over all derivatives of order 1 to the polynomial degree $N$ (page-local: multi-indices $\mathbf k$,
local mesh size $h_e$).
Their Hermite-WENO candidates are weighted with $\beta_l=\|u_{h,l}\|_e^{q}$ (page-local seminorm
exponent $q\ge1$, not the weight exponent), generalizing the Jiang–Shu ($q=2$, 1-D) and Friedrich
($q=1$, 2-D) indicators; the same seminorm of the difference
between the finite element solution and its WENO reconstruction defines their smoothness sensor
([Hermite WENO](/methods/hermite-weno.md),
[WENO-stabilized continuous Galerkin](/methods/weno-stabilized-continuous-galerkin.md),
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)). Because only derivatives enter,
the cell-average correction of the candidates does not affect the indicator (Remark 3).

## Multi-dimensional, derivative and time indicators

- **Reference space.** On unstructured meshes Tsoutsanis et al. (2021, Eqs. (33)–(35)) integrate all
  derivatives of orders 1 to $r$ of candidate $s$ over the reference element, so that
  $\beta_s=\sum_k\sum_lc^s_k\,\mathcal O_{kl}\,c^s_l$ is a quadratic form in the polynomial
  coefficients $c^s_k$ with a precomputed "oscillation indicator" matrix $\mathcal O_{kl}$
  (page-local symbols); no mesh-size factor is printed ([CWENO](/methods/cweno.md)).
- **Triangles.** In the Zhu–Qiu reconstruction on triangles, Chen & Wu (2022, §3.2.1, Eq. (33))
  scale the derivatives of order $|\alpha|$ of the quadratic by $|K|^{|\alpha|-1}$ and the linear
  candidates without factor (as in Hu–Shu), and form the global indicator
  $\tau=\tfrac14\sum_{\ell=1}^4|\beta_0-\beta_\ell|=O(|K|^{3/2})$ from the quadratic's and the four
  linear candidates' indicators (citing Zhu & Qiu; their $\tau^2$ is Zhu & Qiu's $\tau$). In the
  simple WENO limiter for DG, Du, Shu & Zhong (2022, Eq. (3.6)) use
  $\beta=\sum_{1\le|\ell|\le N}|K_0|^{|\ell|-1}\int_{K_0}\big(\tfrac{1}{|\ell|!}\partial^{\ell}p\big)^2d\mathbf x$ for a
  degree-$N$ polynomial $p$ on the target triangle $K_0$ (page-local multi-index $\ell$), with the
  factor $1/|\ell|!$ that the one-dimensional form lacks
  ([WENO limiters for DG](/methods/weno-limiter-dg.md)).
- **Vertex gradients.** In a second-order unstructured finite-volume scheme, Chen, Zhang, Liu & Chen
  (2022, §5, Eq. (25)) measure the smoothness of each vertex gradient direction by direction,
  $(\partial_xu_a)^2|K|$ and $(\partial_yu_a)^2|K|$ (page-local: $u_a$ the
  least-squares vertex value, $|K|$ the cell area), which scales as $h^2|\nabla u|^2$ like a
  $\beta_k$; the weights are WENO-JS-type with exponent 2 and an unscaled
  $\epsilon=10^{-3}$ ([gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)).
- **Cartesian 2-D.** Li, Shu & Qiu (2022, Eq. (2.48)) scale each derivative of order $|\alpha|$ by
  $|I_{i,j}|^{|\alpha|-1}$; Zheng, Cai, Qiu & Qiu (2022, Eq. (12)) by
  $\Delta x^{l_1}\Delta y^{l_2}$ for $\partial_x^{l_1}\partial_y^{l_2}$, summed up to the degree of the
  candidate.
- **Derivative reconstruction.** When the reconstructed quantity is a derivative, Fan, Zhang & Qiu
  (2021, App. A, Eqs. (A.1), (A.3)) sum only derivative orders 2 and 3 of the Hermite candidates, i.e.
  the variation of the candidate's derivative.
- **Central candidates.** In third-order [CWENO](/methods/cweno.md), Puppo et al. (2023, Eq. (9))
  compute the central indicator from the coefficients of the optimal parabola
  $\mathsf a+\mathsf b(x-x_i)+\mathsf c(x-x_i)^2$, not from the central polynomial, and the one-sided
  ones as squared differences. For implicit schemes they compute all indicators on a first-order
  predictor, which makes the reconstruction linear in the unknowns ([Quinpi](/methods/quinpi.md)).
- **Time.** Puppo et al. (2023, Eq. (27)) extend the Jiang–Shu form to the time direction:
  $\sum_{\ell=1}^3\Delta t^{2\ell-1}\int_{t^n}^{t^{n+1}}\big(\tfrac{d^\ell}{dt^\ell}P_t\big)^2dt$ on
  the cubic continuous extension $P_t$ of a DIRK step (page-local), plus squared differences of
  neighbouring stage values, to blend the high-order step with a first-order predictor.

## Other meanings of the term

Several sources use "smoothness indicator" for quantities of a different kind:

- Basile et al. (2022, §4.2, Eqs. (36)–(37)), after Mavriplis, call the decay rate $\varrho_K$ of a
  least-squares fit $\mathcal N_n\simeq Ce^{-\varrho_Kn}$ to the per-degree norms $\mathcal N_n$ of a DG element's modal
  coefficients, $n\ge1$, a smoothness indicator (page-local symbols); $\varrho_K>1$ means smooth and selects
  $p$-enrichment, otherwise $h$-refinement. It grows with smoothness, the opposite sense of $\beta_k$,
  and is computable only for degree $\ge2$ ([h- and hp-adaptation](/methods/hp-adaptation.md)).
- Matsushita & Aoki (2021, §3.1, Eq. (27)) call the slope ratio of a minmod-limited blend of third-order
  WENO with first-order upwinding a "smoothness indicator"; it is the TVD ratio $r_i$ of the registry
  ([TVD limiters](/definitions/total-variation-diminishing.md),
  [hybrid schemes](/methods/hybrid-weno.md)).

- Yu & Hesthaven (2022, §4.1, Eqs. (4.1)–(4.2)), after Klöckner, Warburton & Hesthaven, use the
  algebraic decay rate $\mathfrak a_K$ of the modal coefficients of a DG element,
  $|\hat q_m|\simeq c\,m^{-\mathfrak a_K}$ (page-local, as on the [artificial viscosity](/methods/artificial-viscosity.md) page; their $\tau$, unrelated to the WENO-Z
  $\tau$), with the Fourier analogy $\mathfrak a_K=1$ for a jump, 2 for a kink ($C^0$ but not $C^1$), 3 for $C^1$ but
  not $C^2$ (their Eq. (4.2)); the least-squares estimate is replaced by a neural-network prediction from 11
  normalized point values, and $\mathfrak a_K$ sets an artificial viscosity
  ([artificial viscosity](/methods/artificial-viscosity.md),
  [troubled-cell indicators](/definitions/troubled-cell-indicator.md)). It also grows with smoothness.
- Bezgin et al. (2022, §3.2, Eq. (22)) use a "resolvedness indicator"
  $\varsigma=\dfrac{|\bar u_{i-1}-2\bar u_i+\bar u_{i+1}|}{|\bar u_i-\bar u_{i-1}|+|\bar u_{i+1}-\bar u_i|+\epsilon}\in[0,1]$
  (page-local, as on the learned-weights page; their $\gamma$), derived from the ratio of the second- to the first-order Taylor term,
  only in the training loss of WENO3-NN, to weight the reconstruction error against the deviation
  from the linear weights ([learned WENO weights](/methods/learned-weno-weights.md)).
  *(Compiler check, not in the sources: $\varsigma=1$ exactly when the two one-sided
  differences have opposite signs or one vanishes, i.e. at every discrete extremum of the averages,
  smooth or not.)*

## Qualifications

- Fu (2023, §3.8) recalls Don et al.'s attribution of symmetry breaking in low-dissipation schemes to
  round-off in unstable forms of low-order indicators, and their compact rewriting; Fleischmann et al.
  instead remove floating-point inconsistencies ([symmetry preservation](/properties/symmetry-preservation.md)).
- Deng (2023, Eq. (4.21)) and Huang et al. (2026, Eq. (3.3)) print the two third-order indicators as
  $IS_0$ and $\beta_1$; both are the Jiang–Shu $\beta$ of the two-point stencils.
- Fu (2021, Eq. (11)) uses the indicator without the TENO reference constant,
  $\gamma_k=(\beta_k+\epsilon)^{-q}$ with $q=7$; this is a choice of weight, not of indicator.
- Puppo et al. (2023, Eq. (9)) print the central CWENO3 indicator as
  $\mathsf b^2\Delta x^2+\tfrac{52}{3}\mathsf c^2\Delta x^4$. *(Compiler check, not in the sources:
  their own definition (8) applied to the parabola gives $\tfrac{13}{3}\mathsf c^2\Delta x^4$, which is
  the $\tfrac{13}{12}(\bar u_{i-1}-2\bar u_i+\bar u_{i+1})^2$ of the Jiang–Shu $\beta_1$ printed by Luo &
  Wu 2021, Eq. (5); the printed factor is four times larger.)*
- Zheng, Cai, Qiu & Qiu (2022, Eq. (12)) print the indicator sums over $l_1+l_2\le3$ (and $\le1$),
  which includes the zeroth derivative, the squared polynomial itself; every other source sums from
  first-order derivatives. *(Compiler check, not in the sources: a zeroth-order term makes the
  indicator change when a constant is added to the data.)* The paper does not comment.
- Wong et al. (2021) do not print the value of $\epsilon$ in their weights.
- Bezgin et al. (2022, Eq. (9)) print the general indicator with the sum starting at the zeroth
  derivative and the integrand not squared; their own two-point values (Eq. (10)) are those of the
  squared first derivative, the Jiang–Shu form above. Chu et al. (2022, Eq. (3.6)) print both limits
  of the integral as $x_{j+1/2}$; their explicit forms (3.7) are the Jiang–Shu ones.
- Hiejima (2022, Eq. (14)) writes the sum over $n=1,\dots,(K-1)/2$ (his $r-1$) for every substencil, though the
  difference operators exist only up to one less than the substencil size (blank in his Tables 1, 3,
  5); the sum runs over the available orders.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §2, Eqs. (6)–(11), (16), Table 3.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §2.1, Eq. (5).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §2.1, Eq. (8); §2.3, Eq. (18).
- [Ye et al. (2022)](/sources/ye-2022.md) — §2.1, Eq. (5); §3, Eqs. (18), (25), (28)–(30), (33)–(39).
- [Fu (2021)](/sources/fu-2021.md) — §3.2, Eqs. (11)–(12); §4.2, Eq. (28).
- [Fu (2023)](/sources/fu-2023.md) — §2.2, Eq. (7); §3.8.
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §2.2, Eqs. (9)–(10).
- [Deng (2023)](/sources/deng-2023.md) — §4.3, Eqs. (4.21)–(4.22).
- [Huang et al. (2026)](/sources/huang-2026.md) — §3.1, Eqs. (3.3)–(3.4).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §I.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — Eqs. (9)–(10), Remark 1; §5, Eq. (11), Remark 3.
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.1.1, Eqs. (3.10)–(3.12), (3.23)–(3.28), Remark 2.
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — App. A, Eq. (A.2).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §2.1, Eqs. (2.13)–(2.20); §2.2, Eqs. (2.48)–(2.55).
- [Wong et al. (2021)](/sources/wong-2021.md) — §4.3, Eqs. (91)–(101); App. B, Eq. (B.20).
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2.2.4; App. B.
- [Zheng, Cai, Qiu & Qiu (2022)](/sources/zheng-2022.md) — §2.2, Eqs. (12)–(13).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §3.2.1, Eqs. (33)–(35).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — App. A, Eqs. (A.1), (A.3).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §3.1, Eqs. (8)–(9); §3.3.3, Eq. (27).
- [Basile et al. (2022)](/sources/basile-2022.md) — §4.2, Eqs. (36)–(37).
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.1, Eqs. (26)–(27).
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §2, Eqs. (9)–(10); §3.2, Eqs. (20)–(22).
- [Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md) — §5, Eqs. (25)–(26).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §3.2.1, Eqs. (32)–(34).
- [Chu, Kurganov & Na (2022)](/sources/chu-2022.md) — §3, Eqs. (3.6)–(3.7); §4.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §3.1, Eq. (3.6).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.4, Eq. (14); Tables 1, 3, 5.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §4.1, Eqs. (4.1)–(4.3).
