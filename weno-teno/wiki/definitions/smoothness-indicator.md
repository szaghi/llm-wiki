---
type: Definition
title: "Smoothness indicators"
description: "A smoothness indicator β_k is a quadratic functional of the data on candidate stencil S_k, O(Δx²) on smooth data and O(1) across a jump; the Jiang–Shu form underlies WENO, TENO, CWENO and Hermite-WENO weights, with variants for one-point bases, L¹-type and symmetric forms, Hermite data, multi-dimensional and time stencils, global indicators and pairwise tests; the term also names unrelated sensors."
status: established
aliases: [smoothness indicator, local smoothness indicator, LSI, IS_k, Jiang–Shu indicator, global smoothness indicator, oscillation indicator, reference smoothness indicator, symmetry-preserving indicators, L1-type indicators, IMWENO-P, WENO-NS]
tags: [reconstruction, weno, teno, cweno]
timestamp: 2026-10-23T20:37:00Z
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

The form used by nearly every source of the bundle is that of Jiang & Shu (Li et al. 2022b, Eq. (7);
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
(Fu 2021, Eq. (28); Takagi et al. 2022, Eq. (10); Ye et al. 2022, Eq. (5); Hong et al. 2022,
Eq. (16); Liang et al. 2022, Eq. (12); Huang, Liang & Fu 2023, Eq. (16)). On the compact two-point
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
by $\tfrac{13}{12}$ instead of 1.)* Hiejima applies it to substencils of 3 to $(K+3)/2$ points, $K$ the size of the full stencil.
Chen & Deng (2023, Eqs. (14)–(16)) use the same form for the three-point candidates of a fifth-order
WCNS interpolation and print its expansions (Eqs. (28)–(30), cited to Borges et al.):
$\beta_{0,2}=f'^2\Delta x^2+\big(f''^2-\tfrac23f'f'''\big)\Delta x^4\pm\big(\tfrac12f'f^{(4)}-2f''f'''\big)\Delta x^5+O(\Delta x^6)$,
$\beta_1=f'^2\Delta x^2+\big(f''^2+\tfrac13f'f'''\big)\Delta x^4+O(\Delta x^6)$, the expansions of Wan & Xia
below with $\tfrac{13}{12}$ replaced by 1
([exponential weights](/methods/exponential-nonlinear-weights.md)). For finite-volume WENO, Zhong et
al. (2023, Eqs. (8)–(9)) recall two indicators built from the same two squares: WENO-$\eta$ of Fan et
al., $\tfrac14(\cdot)^2+(\cdot)^2$, which coincides with this form, and the WENO-ZS indicators of
Zhang & Shu for steady states, which keep only the first-difference square.

**Wider stencils.** Ye et al. (2022, Eq. (5)) give the four-point indicators of TENO7, e.g. for
$\{i,\dots,i+3\}$

$$\beta=\tfrac1{36}(-11f_i+18f_{i+1}-9f_{i+2}+2f_{i+3})^2+\tfrac{13}{12}(2f_i-5f_{i+1}+4f_{i+2}-f_{i+3})^2+\tfrac{781}{720}(-f_i+3f_{i+1}-3f_{i+2}+f_{i+3})^2 .$$

Fu (2021, Eq. (28)) prints the six-, eight- and ten-point indicators of TENO-AA as rational quadratic
forms (prefactors $1/120960$, $1/62270208000$, $1/8002967132160000$); the six-point one is the
indicator $\beta_6$ that Ye et al. (2022, Eq. (29)) attribute to [WENO-CU6](/methods/weno-cu6.md).
*(Compiler check, not in the sources: the four-point form above and the six-point $\beta_6$ of Ye et
al. were recomputed from the integral definition and agree exactly.)*
Hong, Ye & Ye (2022, Eq. (19)) print the five-point indicator of $\{i,\dots,i+4\}$ used by
eight-point TENO as five quadratic terms with prefactors $\tfrac1{144}$, $\tfrac{13}{1728}$,
$\tfrac{781}{2880}$, a cross term $-\tfrac1{4320}$ and $\tfrac{32803}{30240}$, and the eight-point
global indicator $\tau_8$ as a quadratic form in $f_{i-3},\dots,f_{i+4}$ with prefactor
$1/62270208000$ (Eq. (20)); they name these wide indicators as the main cost of TENO8 (§1, §3.2;
[targeted ENO](/methods/targeted-eno.md)). Li, Chen & Ren (2022a, Eqs. (43)–(44)), following
[WENO-CU6](/methods/weno-cu6.md), replace the indicator of the fully downwind three-point stencil by
the six-point $\beta_6$, because a downwind stencil weighted like the upwind ones "may cause the
instability" ([MDCD schemes](/methods/mdcd-scheme.md)).
Zhang, Jiang, Qin, Qu & Yan (2024b, Eqs. (11), (16)) print the same rule for WENO-CU6 and the four-point
indicator of the TENO6 stencil $\{i,\dots,i+3\}$ in expanded form,
$\tfrac1{240}\big[f_i(2107f_i-9402f_{i+1}+7042f_{i+2}-1854f_{i+3})+f_{i+1}(11003f_{i+1}-17246f_{i+2}+4642f_{i+3})+f_{i+2}(7043f_{i+2}-3882f_{i+3})+547f_{i+3}^2\big]$;
for their scale-adaptive TENO6-SA they replace it by the mean of this four-point indicator and the six-point
$\beta_6$ (Eq. (36); [scale sensors](/definitions/scale-sensor.md)). *(Compiler check, not in the sources: the expanded
form equals Ye et al.'s three-square form above identically.)*

**Legendre form.** Li et al. (2022b, Eqs. (8)–(11)), after Balsara et al., expand the candidate in
the rescaled Legendre basis $1,\ X,\ X^2-\tfrac1{12},\ X^3-\tfrac3{20}X$ on
$[-\tfrac12,\tfrac12]$ (page-local $X=(x-x_i)/\Delta x$; the registry keeps $\xi_j$ for DG nodes) with modal coefficients $p^{[l]}_k$; for $r=4$

$$\beta_k=\Big(p^{[1]}_k+\tfrac{1}{10}p^{[3]}_k\Big)^2+\tfrac{13}{3}\big(p^{[2]}_k\big)^2+\tfrac{781}{20}\big(p^{[3]}_k\big)^2 .$$

*(Compiler check, not in the sources: this equals the Jiang–Shu integral exactly.)* Balsara et al. (2024, §I) stress that
indicators written as sums of perfect squares cost few operations, which they credit with improving
the speed and stability of high-order FD-WENO; they extend the closed forms to finite volumes.
For the quartic on a five-point central stencil, with the further basis function
$X^4-\tfrac3{14}X^2+\tfrac3{560}$ and modal coefficients $p^{[l]}$ (written $\mathsf a_l$, $\mathsf b_l$ on the
multi-resolution WENO page), Wang et al. (2021, Eq. (3.11))
and Li, Duan & Tang (2022c, Eq. (A.2)) print

$$\beta=\Big(p^{[1]}+\tfrac1{10}p^{[3]}\Big)^2+\tfrac{13}{3}\Big(p^{[2]}+\tfrac{123}{455}p^{[4]}\Big)^2+\tfrac{781}{20}\big(p^{[3]}\big)^2+\tfrac{1421461}{2275}\big(p^{[4]}\big)^2,$$

and $\beta=(p^{[1]})^2+\tfrac{13}{3}(p^{[2]})^2$ for the parabola on three points; these are the
indicators of [multi-resolution WENO](/methods/multi-resolution-weno.md). *(Compiler check, not in
the sources: the quartic form equals the Jiang–Shu integral exactly.)*

Balsara, Samantaray & Subramanian (2023, §3, Eqs. (14)–(30)) give the same closed forms for a
different object: one-dimensional **interpolation of facial values** of a face-collocated vector field
at the zone faces $x=\pm\tfrac12,\pm\tfrac32,\dots$ (reference units), used to prolong divergence-constrained fields
([divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md)). For candidates
$p^{[0]}+p^{[1]}X+p^{[2]}(X^2-\tfrac1{12})+\dots$ on $r=3,4,5$ faces the indicators are
$(p^{[1]})^2+\tfrac{13}{3}(p^{[2]})^2$, the $r=4$ form above, and the quartic form above (Eqs. (17),
(23), (30)), i.e. the Jiang–Shu integral, independent of whether the candidate matches cell averages
or point values. They state that finite-volume indicators on Cartesian meshes also reduce to sums of
perfect squares in a Legendre basis, which "has never been documented in the literature before"
(§1, §10); the derivation is in an online supplement that is not part of the paper read.

**Other forms recalled.** Li et al. (2022b, Eq. (6)) recall the earlier Liu–Osher–Chan indicator, a
sum of squared undivided differences of all orders below $r$. Fu (2023, §2.2) notes that improved
indicators developed for WENO can be used in TENO unchanged.

**Interpolation polynomials.** For the point-value interpolation of a WCNS, Zhou, Ding, Huang & Luo (2023,
Eqs. (15)–(17)) integrate the derivatives of the interpolation polynomials over $[x_{i-1/2},x_{i+1/2}]$, which
gives the classical fifth-order $\beta_0,\beta_1,\beta_2$ unchanged, and the six-point indicator of the
downwind candidate, after Hu et al. and Liu et al., printed in full with denominator 232243200 (Eq. (17));
$\tau_6=|\beta_3-\tfrac18(\beta_0+6\beta_1+\beta_2)|$ (Eq. (18), their $\beta_3$ the six-point indicator). They
attribute the non-monotone growth of the nonlinear dissipation with wavenumber to "the first derivative term in
the smoothness indicator", citing earlier work (§4.2).

**Scaled derivative sums at the solution point.** Qin, Chen, Lin & Deng (2023, Eqs. (13)–(20)) evaluate the
derivatives of the nested interpolants $P_2$ (three points) and $P_3$ (five points) of a multi-resolution WCNS
at the solution point $x_i$ instead of integrating over a cell, and weight them by a free factor
$\lambda_{\mathrm s}>0$ (page-local):

$$\beta_2=\sum_{n=1}^2\big(\lambda_{\mathrm s}^{n-1}\Delta x^n\partial_x^nP_2(x_i)\big)^2,\qquad
\beta_3=\sum_{n=1}^4\big(\lambda_{\mathrm s}^{n-1}\Delta x^n\partial_x^nP_3(x_i)\big)^2,$$

with $\Delta x^n\partial_x^nP_3(x_i)$ the five-point central differences
$\tfrac1{12}u_{i-2}-\tfrac23u_{i-1}+\tfrac23u_{i+1}-\tfrac1{12}u_{i+2}$, $-\tfrac1{12}u_{i-2}+\tfrac43u_{i-1}-\tfrac52u_i+\tfrac43u_{i+1}-\tfrac1{12}u_{i+2}$,
$-\tfrac12u_{i-2}+u_{i-1}-u_{i+1}+\tfrac12u_{i+2}$ and $u_{i-2}-4u_{i-1}+6u_i-4u_{i+1}+u_{i+2}$ on a uniform grid, the
$\mathsf D_1,\dots,\mathsf D_4$ of the five-point [scale sensor](/definitions/scale-sensor.md) of Huang, Liang & Fu. $\lambda_{\mathrm s}=2$
multiplies the squared $n$th-derivative terms by $1,4,16,64$. The authors state that it suppresses the
oscillations of $\lambda_{\mathrm s}=1$ on the Lax problem and lets slow shocks cross block interfaces; their
convergence tables give equal or nearly equal fine-grid errors for both values, larger coarse-grid errors with
$\lambda_{\mathrm s}=2$, and no analysis of the choice (Tables 10–12;
[shock-capturing boundary closure](/methods/shock-capturing-boundary-closure.md)). Near boundaries the same
formulas are applied with coefficients for the non-uniform points (Tables 4–5, 8–9).

**Explicit quartic form.** Wang, Zhu, Wang & Zhao (2023c, Eq. (3.20)) print the Jiang–Shu indicator of
the five-point point-value quartic of a multi-resolution WCNS interpolation as a quadratic form with
prefactor $\tfrac1{60480}$ (diagonal coefficients 82364, 1228889, 2695779, 1228889, 82364); see the
Qualifications for a missing term.

**Stencils that do not contain the target cell.** For the eight-point discontinuity indicator of TENO-S, Liang & Fu
(2024b, §3.1, Eq. (31)) evaluate the Jiang–Shu integral over the target cell $[x_{i-1/2},x_{i+1/2}]$ for three-point
stencils lying beside it, i.e. for extrapolated quadratics, e.g. on $\{i+1,i+2,i+3\}$
$$\beta=\tfrac13\big|10f_{i+3}^2-49f_{i+2}f_{i+3}+29f_{i+1}f_{i+3}+61f_{i+2}^2-73f_{i+1}f_{i+2}+22f_{i+1}^2\big|,$$
with analogous forms on $\{i-3,i-2,i-1\}$ and $\{i+2,i+3,i+4\}$; equal stencil sizes keep the cost low
([hybrid schemes](/methods/hybrid-weno.md)). *(Compiler check, not in the sources: integrating the squared first and
second derivatives of the quadratic matching $f_{i+1},f_{i+2},f_{i+3}$ as cell averages over the target cell reproduces this
form exactly.)* The same paper prints the four- and five-point indicators of eight-point TENO (prefactors $\tfrac1{240}$ and
$\tfrac1{5040}$) and recalls $\tau_8=\big|\beta_8-\tfrac16(\beta_{1,3}+\beta_{2,3}+4\beta_{0,3})\big|=O(\Delta x^6)$ in the TENO
labelling (Eqs. (14)–(16); page-local $\beta_{k,r}$, stencil $k$ of width $r$).

**Finite-volume TENO5.** Huang & Fu (2024, §2, Eqs. (9)–(11)) recall the three-point indicators in the central-first
labelling, the five-point indicator $\beta_{3,5}$ as a quadratic form in $\bar u_{i-2},\dots,\bar u_{i+2}$ with prefactor
$\tfrac1{5040}$ (diagonal coefficients 6908, 104963, 231153, 104963, 6908), and the global indicator
$\tau_K=\big|\beta_{3,5}-\tfrac16(\beta_{1,3}+\beta_{2,3}+4\beta_{0,3})\big|=O(\Delta x^6)$ with $K=5$, after Fu et al.: the
TENO full-stencil form of [targeted ENO](/methods/targeted-eno.md), not the registry's WENO-Z $\tau_5=|\beta_0-\beta_2|$.

**Finite-volume five-point indicator with two-point candidates.** For the finite-volume
[converged ENO](/methods/converged-eno.md) scheme, Liang & Fu (2026, §3.2.2, Eqs. (18)–(19)) print the Jiang–Shu
indicator of the quartic on $\bar u_{i-2},\dots,\bar u_{i+2}$ (their $\beta_0$, the large stencil) as
$$\begin{aligned}\beta_0={}&\tfrac1{15600}(11\bar u_{i+2}-174\bar u_{i+1}+326\bar u_i-174\bar u_{i-1}+11\bar u_{i-2})^2+\tfrac{781}{2880}(\bar u_{i+2}-2\bar u_{i+1}+2\bar u_{i-1}-\bar u_{i-2})^2\\&+\tfrac{1421461}{1310400}(\bar u_{i+2}-4\bar u_{i+1}+6\bar u_i-4\bar u_{i-1}+\bar u_{i-2})^2+\tfrac1{144}(\bar u_{i+2}-8\bar u_{i+1}+8\bar u_{i-1}-\bar u_{i-2})^2,\end{aligned}$$
the form [Ren et al. (2025)](/sources/ren-2025.md) (§5.1.1, Eq. (45)) print for the quartic of their multi-resolution WENO, with squared
differences $(\bar u_{i-1}-\bar u_i)^2$ and $(\bar u_i-\bar u_{i+1})^2$ for the two two-point stencils, and the global indicator
$\tau_{\mathrm C}=\lvert2\beta_0-(\beta_1+\beta_2)\rvert$ (page-local; their stencil numbering, $0$ the large stencil). Their Taylor expansions
(Eqs. (22)–(23)) give $\beta_0=u'^2\Delta x^2+\tfrac{13}{12}u''^2\Delta x^4+O(\Delta x^6)$,
$\beta_{1,2}=u'^2\Delta x^2\mp u'u''\Delta x^3+(\tfrac14u''^2+\tfrac13u'u''')\Delta x^4+O(\Delta x^5)$ and
$\tau_{\mathrm C}=\big\lvert(\tfrac23u'u'''-\tfrac53u''^2)\Delta x^4+O(\Delta x^6)\big\rvert$, so that $\tau_{\mathrm C}$ cancels the common
$u'^2\Delta x^2$ and has more contrast between smooth and non-smooth data than the $\beta_k$, whose leading term depends
on $u'$ alone; they use $\tau_{\mathrm C}$ in their noise filter for that reason. *(Compiler check, not in the sources: the printed
$\beta_k$ expansions are those of point values $u(x_j)$ in place of the cell averages; with cell averages the
$\Delta x^4$ coefficients become $\tfrac{13}{12}u''^2+\tfrac1{12}u'u'''$ for $\beta_0$ and
$\tfrac14u''^2+\tfrac5{12}u'u'''$ for $\beta_{1,2}$. The $\Delta x^4$ term of $\tau_{\mathrm C}$ is the same in both settings,
so the argument for $\tau_{\mathrm C}$ is unaffected; its $\Delta x^6$ term differs.)*

## $L^1$-type and symmetric indicators (the WENO-NS line)

**As network inputs.** Nogueira et al. (2024, §3.1, Eqs. (12)–(14)) feed their learned WENO5 weights with the
absolute-value analogues of the Jiang–Shu indicators, page-local
$\beta^{\mathrm{abs}}_0=\tfrac{13}{12}|f_{i-2}-2f_{i-1}+f_i|+\tfrac14|f_{i-2}-4f_{i-1}+3f_i|$ and its two shifts, divided by
their maximum; with the squared $\beta_k$ the network trained "less accurately" (stated, no data). The max-normalization
maps machine-zero data such as $(10^{-16},10^{-15},10^{-16})$ to $(0.1,1,0.1)$, which "may correspond with a non-smooth situation", so a plateau
detector bypasses the network there ([learned WENO weights](/methods/learned-weno-weights.md)).

Zhong, Wang, Qiu & Gao (2023, §2–3) review fifth-order finite-volume indicators built from the
undivided differences of Ha et al. (page-local $\mathsf L_{n,k}$),
$\mathsf L_{1,k}=(1-k)\bar u_{i-2+k}+(2k-3)\bar u_{i-1+k}+(2-k)\bar u_{i+k}$ and
$\mathsf L_{2,k}=\bar u_{i-2+k}-2\bar u_{i-1+k}+\bar u_{i+k}$, on the three candidate stencils
$k=0,1,2$ (so $\mathsf L_{1,0}=\bar u_{i-2}-3\bar u_{i-1}+2\bar u_i$, $\mathsf L_{1,1}=\mathsf L_{1,2}=\bar u_{i+1}-\bar u_i$):

- **WENO-NS** (Ha et al.): $\beta_k=\xi_{\mathrm{NS}}|\mathsf L_{1,k}|+|\mathsf L_{2,k}|$, an $L^1$-type indicator with a
  tunable $\xi_{\mathrm{NS}}$ (0.1 for advection, 0.4 for Euler recommended; page-local);
- **WENO-P** (Kim et al.): $\beta_1$ and $\beta_2$ multiplied by $1+\delta_{\mathrm P}$ and $1-\delta_{\mathrm P}$, a second
  tunable parameter (page-local $\delta_{\mathrm P}$), with global indicator $(\beta_0-\beta_2)^2$;
- **MWENO-P** (Rathan & Naga Raju): the WENO-P indicators with global indicator
  $|\mathsf L_{2,0}+\mathsf L_{2,2}-\mathsf L_{2,1}|^2$ (Eqs. (12)–(18), as recalled).

**Symmetry-preserving property.** Zhong et al. (§3.1, Eqs. (19)–(20), Table 1) call a set of indicators
symmetry-preserving when, inside each squared term, the coefficient of $\bar u_{i-n}$ in $\beta_k$ equals
$\pm$ that of $\bar u_{i+n}$ in $\beta_{2-k}$, $n=0,1,2$: $\beta_2$ is the mirror image of $\beta_0$ about
the centre cell and $\beta_1$ is its own mirror image. The Jiang–Shu, WENO-Z, mapped, WENO-ZS and
WENO-$\eta$ indicators have it; those of WENO-NS, WENO-P and MWENO-P do not *(compiler check, not in the
sources: $\mathsf L_{1,0}$ is not the mirror image of $\mathsf L_{1,2}=\bar u_{i+1}-\bar u_i$)*. This is a
property of indicator coefficients, distinct from the symmetry of solutions on the
[symmetry preservation](/properties/symmetry-preservation.md) page; their own Rayleigh–Taylor run
still breaks solution symmetry (Fig. 13).

**IMWENO-P** (§3.2, Eqs. (21)–(26)). With $\xi_{\mathrm{NS}}=\Delta x$, the cell width,

$$\begin{aligned}
\beta^{\mathrm{IMP}}_0&=4\Delta x(\bar u_{i-2}-3\bar u_{i-1}+2\bar u_i)^2+(\bar u_{i-2}-2\bar u_{i-1}+\bar u_i)^2,\\
\beta^{\mathrm{IMP}}_1&=\Delta x(\bar u_{i-1}-\bar u_{i+1})^2+(\bar u_{i-1}-2\bar u_i+\bar u_{i+1})^2,\\
\beta^{\mathrm{IMP}}_2&=4\Delta x(2\bar u_i-3\bar u_{i+1}+\bar u_{i+2})^2+(\bar u_i-2\bar u_{i+1}+\bar u_{i+2})^2,
\end{aligned}$$

which are symmetry-preserving (Lemma 1, proof omitted) *(compiler check, not in the sources: the
coefficients are mirror images as stated)*, and the global indicator is the squared undivided fourth
difference

$$\tau^{\mathrm{IMP}}=\big(\bar u_{i-2}-4\bar u_{i-1}+6\bar u_i-4\bar u_{i+1}+\bar u_{i+2}\big)^2=\Delta x^8\big(f^{(4)}\big)^2+O(\Delta x^9)$$

(page-local $\beta^{\mathrm{IMP}}_k$, $\tau^{\mathrm{IMP}}$, the source's $\bar\beta_s$, $\bar\zeta$; Eqs. (23)–(24), (29)), in Z-type weights
$d_k\big(1+(\tau^{\mathrm{IMP}}/(\beta^{\mathrm{IMP}}_k+\epsilon))^q\big)$ with $q=1$, $\epsilon=10^{-40}$. Because of the
factor $\Delta x$, $\beta^{\mathrm{IMP}}_k=4(f')^2\Delta x^3+O(\Delta x^4)$ on smooth monotone data, not $O(\Delta x^2)$ (Eq. (30)). On
non-uniform meshes $\xi_{\mathrm{NS}}$ is the smallest of the five local widths (Example 17). The orders at
critical points are on [accuracy at critical points](/properties/critical-point-accuracy.md). On a
low-density, low-internal-energy Riemann problem WENO-NS, WENO-P and MWENO-P produce negative pressure
and fail, while IMWENO-P, WENO-JS, WENO-Z, WENO-$\eta$ and WENO-ZS run; the authors state that this is
"not enough to link the symmetry-preserving property with the positivity-preserving property"
(Example 10; [double rarefaction](/benchmarks/double-rarefaction-problem.md)). *(Compiler check, not in the
sources: the fourth difference in $\tau^{\mathrm{IMP}}$ is the one whose square, times $\tfrac{13}{12}$,
leads $\tau^{\mathrm{ref}}_5$ below, and the $\mathsf D_4$ of the five-point
[scale sensor](/definitions/scale-sensor.md).)*

## Indicators of one- and two-point candidates

The Jiang–Shu form vanishes identically on a constant candidate, so schemes whose hierarchy starts
from one point need another base indicator:

- Wang et al. (2021, Eq. (3.12)) and Li, Duan & Tang (2022c, App. A) take
  $\beta=\min\big((f_i-f_{i-1})^2,(f_{i+1}-f_i)^2\big)$, which, in Li, Duan & Tang's words, "avoids
  the zero value" of the Jiang–Shu form on the constant;
- Li, Shu & Qiu (2022d, Eqs. (2.14)–(2.20)) combine the two one-sided linear polynomials with WENO-Z
  weights and take the Jiang–Shu indicator of the combination,
  $\beta=\big(\omega_{\mathrm L}(\bar u_i-\bar u_{i-1})+\omega_{\mathrm R}(\bar u_{i+1}-\bar u_i)\big)^2$
  (page-local $\omega_{\mathrm{L,R}}$), and in 2-D four L-shaped linear polynomials
  (Eqs. (2.49)–(2.55)).

- Wang, Zhu, Wang & Zhao (2023c, Eq. (3.22)) take the same minimum of squared differences for the
  constant of their multi-resolution WCNS interpolation, and call it simpler and parameter-free
  compared with the indicator of the earlier MR-WCNS;
- Fan et al. (2025b, §2.2, Eqs. (13)–(15)) take the same minimum for the one-point stencil of the third-order
  multi-resolution WCNS (WCNS3-MR) in the modified form of Qin et al., and for the three-point stencil
  $\beta=\sum_{n=1}^2\big(\lambda_{\mathrm s}^{n-1}\partial_x^nP(x_i)\big)^2$ with the amplifying parameter $\lambda_{\mathrm s}\ge1$ of
  Qin et al. below ($\lambda_{\mathrm s}=1$ and $50$ in the two training targets of their network); their global indicator is
  the square $\lvert\beta_2-\beta_1\rvert^2$ of the difference, not the difference
  ([learned WENO weights](/methods/learned-weno-weights.md)). Fan et al. print the derivatives without the factor
  $\Delta x^n$ that Qin, Chen, Lin & Deng (2023, Eqs. (13)–(20)) print, so that, unless the derivatives are meant in
  index space, their $\beta_2$ and their undivided $\beta_1$ scale differently with $\Delta x$ *(compiler check, not in the sources)*;
- in two dimensions, on the $3\times3$ block of a moving-mesh remap, Gu, Li, Cheng & Shu (2023, §2.4)
  take the minimum of the four sums of two adjacent squared face-neighbour differences, after Zhu & Shu,
  because $\beta=0$ on the constant "does lead to more smearing" at strong shocks
  ([multi-resolution WENO](/methods/multi-resolution-weno.md)).

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
it is not the WENO-Z $\tau_5=|\beta_0-\beta_2|$ of the registry). *(Compiler check, not in the sources: the closed form
was recomputed from the integral; it agrees.)*

**Floored two-point indicators.** For the third-order interpolation of their relativistic MHD
code, [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) (App. A, Eqs. (A3)–(A10);
arXiv v3) start from Falle's TVD indicators $(u_i-u_{i-1})^2$ and $(u_{i+1}-u_i)^2$, "the same as
in Jiang & Shu (1996) for a 3rd-order WENO", and add a scale-aware floor,
$\beta_\pm=(u_i-u_{i\pm1})^2+U^2/n_{\mathrm{sm}}^2+\epsilon$, $U$ the largest $\lvert u\rvert$ on the
three points, $n_{\mathrm{sm}}=10$, $\epsilon=10^{-25}$ (page-local), so that critical points are
not taken for shocks ([critical-point accuracy](/properties/critical-point-accuracy.md),
[mapped WENO](/methods/mapped-weno.md)). *(Compiler check, not in the sources: the floor scales
like the squared differences under $u\mapsto\sigma u$, so the weights are scale-invariant up to
$\epsilon$, but $U$ changes when a constant is added, so they are not affine-invariant.)*

**Wider stencils for sensors.** Zheng, Shu & Qiu (2021, §2.2.4) evaluate Jiang–Shu indicators with
derivatives up to fifth order over $[x_i,x_{i+1}]$, not over a cell, for the quintic on
$\{x_{i-2},\dots,x_{i+3}\}$ and the four quadratics on its three-point substencils; the quintic's
indicator is printed as a sum of five squares with prefactors $1$, $\tfrac{13}{3}$, $\tfrac{781}{20}$,
$\tfrac{1421461}{2275}$ and $\tfrac{21520059541}{1377684}$. Their WENO-Z-like combination of these
indicators is a discontinuity indicator, not a weight
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Behaviour in smooth regions

For $r=4$, Li et al. (2022b, Eq. (16)) give
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

For $r=3$, Wan & Xia (2022, Eqs. (2.18)–(2.20)) print, in the Jiang–Shu labelling,
$$\begin{aligned}\beta_{0,2}&=f'^2\Delta x^2+\big(\tfrac{13}{12}f''^2-\tfrac23f'f'''\big)\Delta x^4\mp\big(\tfrac{13}{6}f''f'''-\tfrac12f'f^{(4)}\big)\Delta x^5+O(\Delta x^6),\\
\beta_1&=f'^2\Delta x^2+\big(\tfrac{13}{12}f''^2+\tfrac13f'f'''\big)\Delta x^4+O(\Delta x^6),\end{aligned}$$
which gives $\tau_5=|\beta_0-\beta_2|=O(\Delta x^5)$ and, with the mean $\tfrac13\sum_k\beta_k=O(\Delta x^2)$,
their smoothness detector $\tau_5/(\epsilon+\tfrac13\sum_k\beta_k)$ ([hybrid schemes](/methods/hybrid-weno.md)).

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

Chen & Fu (2024, §4.2, Eqs. (15)–(20)) apply the Jiang–Shu form to the whole nodal polynomial of a
spectral-difference cell, $\beta_i=\sum_{l=1}^{N}\Delta x^{2l-1}\int_{I_i}(\partial^l_xu_h)^2dx$, and in 2-D
direction by direction, $\beta^x_{i,j}=\sum_{l=1}^{N}\Delta x^{2l-2}\iint_{I_{i,j}}(\partial^l_xu_h)^2\,dx\,dy$ ($N$ the
polynomial degree, $N+1$ solution points per direction; the source's $N$ counts the points). Three consecutive cells form a TENO-type troubled-cell test with
$\gamma_k=(\beta_k+\epsilon)^{-q}$, $q=6$, normalized and cut at $10^{-5}$ (1-D) or $5\times10^{-4}$ (2-D), with
$\epsilon=10^{-4}$ (1-D) and $10^{-3}$ (2-D): a very small $\epsilon$ such as $10^{-12}$ is "not good" because
high-wavenumber noise of extremely low amplitude would be flagged, and the larger 2-D value is argued from the
$(N+1)^2$ basis functions of degree up to $2N$ of a nodal 2-D polynomial
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)). The same paper's Hermite candidates use
the Jiang–Shu form over the target cell (Eq. (56); [Hermite WENO](/methods/hermite-weno.md)).

## Multi-dimensional, derivative and time indicators

- **Reference space.** On unstructured meshes Tsoutsanis et al. (2021, Eqs. (33)–(35)) integrate all
  derivatives of orders 1 to $r$ of candidate $s$ over the reference element, so that
  $\beta_s=\sum_k\sum_lc^s_k\,\mathcal O_{kl}\,c^s_l$ is a quadratic form in the polynomial
  coefficients $c^s_k$ with a precomputed "oscillation indicator" matrix $\mathcal O_{kl}$
  (page-local symbols); no mesh-size factor is printed ([CWENO](/methods/cweno.md)).
  Ji, Liang & Fu (2022, Eq. (17)) use the same reference-space form, summed over derivative orders 1
  to the polynomial degree, for the candidates of their unstructured TENO; the measure is then
  $\gamma_k=(\beta_k+\epsilon)^{-6}$, $\epsilon=10^{-12}$, without the global indicator of Cartesian TENO,
  which "can be applied" but is left out to save cost (§3.2;
  [targeted ENO](/methods/targeted-eno.md)).
  Ji, Liang & Fu (2023, Eq. (26)) keep the reference-space form, printed without mesh-size factor, for both their
  dual-cut-off TENO ($\gamma_k=(\beta_k+\epsilon)^{-6}$, $\epsilon=10^{-12}$) and their CWENO comparator (exponent 4,
  $\epsilon=10^{-14}$) at orders 4 to 7 (§3.1.2, §3.2.2).
  Maltsev et al. (2023, Eqs. (26)–(28)) use the same quadratic form, integrated over the target cell in
  physical space with a volume-normalized Taylor basis shared with their modal DG, for the CWENOZ
  limiter of a hybrid DG–finite-volume scheme ([CWENO](/methods/cweno.md)).
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
- **Cartesian 2-D.** Li, Shu & Qiu (2022d, Eq. (2.48)) scale each derivative of order $|\alpha|$ by
  $|I_{i,j}|^{|\alpha|-1}$; Zheng, Cai, Qiu & Qiu (2022, Eq. (12)) by
  $\Delta x^{l_1}\Delta y^{l_2}$ for $\partial_x^{l_1}\partial_y^{l_2}$, summed up to the degree of the
  candidate.
- **DG cells and limiter candidates.** Huang & Fu (2024, §4.3, Eq. (32)) apply the one-dimensional Jiang–Shu form,
  derivatives 1 and 2, to the $\mathbb P^2$ DG polynomial of each of the three cells $I_{i-1},I_i,I_{i+1}$ on its own
  cell; with $\gamma_n=(\beta_n+10^{-3})^{-6}$ normalized over the three cells, cell $i$ is troubled when its own share
  falls below $10^{-4}$ ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)). The same form on the target
  cell measures the candidates of their TENO limiter (Eq. (41); [WENO limiters for DG](/methods/weno-limiter-dg.md)). In
  2-D (Eq. (59)) the terms are scaled by $|I_{ij}|^{2k-1}$, $|I_{ij}|$ the cell area, and the indicators of the
  second-order modes include first-derivative terms, which differs from the HWENO limiter "for better robustness" (no
  ablation shown). *(Compiler check, not in the sources: with an area raised to $2k-1$ the $k=1$ and $k=2$ terms carry
  different powers of length, whereas the $|I|^{|\alpha|-1}$ scaling of Li, Shu & Qiu and Chen & Wu above makes every term
  scale like the squared data; the absolute $10^{-3}$ in the troubled-cell measure also makes it depend on the amplitude of
  the data.)*
- **The same DG indicator printed twice.** Huang et al. (2025a, §3.1, Eq. (11)) state that they reuse the indicator of
  Huang & Fu (2024) unchanged, but print the integral of the three polynomials $p_{i-1},p_i,p_{i+1}$ over the target
  cell $I_i$ for all three, whereas Huang & Fu (2024, Eq. (32)) integrate each polynomial over its own cell. *(Compiler
  check, not in the sources: for a quadratic the second-derivative term is the same on either cell, but the
  first-derivative term of a neighbour polynomial differs, so the two prints define different indicators.)* Which one is
  implemented neither paper settles. Huang et al. (2025a, §3.2.1) use the same form again, with $\epsilon=10^{-10}$
  instead of $10^{-3}$, inside their [TENO-THINC](/methods/teno-thinc.md) limiter, the smaller value "also" acting "as a
  cutoff of the smoothness measurements".
- **Derivative reconstruction.** When the reconstructed quantity is a derivative, Fan, Zhang & Qiu
  (2021, App. A, Eqs. (A.1), (A.3)) sum only derivative orders 2 and 3 of the Hermite candidates, i.e.
  the variation of the candidate's derivative.
- **Hermite data in finite differences.** For the quartic of the finite-difference Hermite WENO,
  fitted to three point fluxes and two derivative fluxes, Fan, Zhao, Xiong & Qiu (2023, §2.1, Step II)
  print the Jiang–Shu indicator as a sum of four squares in the combinations
  $f_{i-1}-f_{i+1}$, $(h_{i-1}+h_{i+1})\Delta x$, $f_{i-1}-2f_i+f_{i+1}$ and $(h_{i-1}-h_{i+1})\Delta x$
  (page-local $h_j$ the derivative fluxes), with prefactors $\tfrac1{16}$, $\tfrac{781}{320}$,
  $\tfrac1{3900}$, $\tfrac{1421461}{36400}$, and squared differences for the two linear candidates
  ([Hermite WENO](/methods/hermite-weno.md)).
- **Hermite data in finite volumes.** For the quartic of the moment-based HWENO-U, fitted to
  three cell averages and the first moments of the two neighbours, Fan et al. (2025a, §2.1,
  Eqs. (2.8)–(2.9)) print, with $p_0=\sum_l\mathsf c_l\xi^l$, $\xi=(x-x_i)/\Delta x$ (page-local
  coefficients),
  $\beta_0=(\mathsf c_1+\tfrac14\mathsf c_4)^2+\tfrac{13}3(\mathsf c_2+\tfrac{63}{130}\mathsf c_4)^2+\tfrac{781}{20}\mathsf c_3^2+\tfrac{1421461}{2275}\mathsf c_4^2$,
  and squared slopes for the two linear candidates. *(Compiler check, not in the sources: the
  Jiang–Shu integral of the quartic gives $(\mathsf c_1+\tfrac14\mathsf c_3)^2$ as first square, the
  other three terms as printed; the prefactors $1,\tfrac{13}3,\tfrac{781}{20},\tfrac{1421461}{2275}$ are
  those of the quartic indicator of Wang et al. (2021) and Li, Duan & Tang (2022c) above.)* Their weights normalize the indicators by
  the stencil's mean absolute average for [scale invariance](/properties/scale-invariance.md)
  ([Hermite WENO](/methods/hermite-weno.md)).
- **Central candidates.** In third-order [CWENO](/methods/cweno.md), Puppo et al. (2023, Eq. (9))
  compute the central indicator from the coefficients of the optimal parabola
  $\mathsf a+\mathsf b(x-x_i)+\mathsf c(x-x_i)^2$, not from the central polynomial, and the one-sided
  ones as squared differences. For implicit schemes they compute all indicators on a first-order
  predictor, which makes the reconstruction linear in the unknowns ([Quinpi](/methods/quinpi.md)).
- **Time.** Puppo et al. (2023, Eq. (27)) extend the Jiang–Shu form to the time direction:
  $\sum_{\ell=1}^3\Delta t^{2\ell-1}\int_{t^n}^{t^{n+1}}\big(\tfrac{d^\ell}{dt^\ell}P_t\big)^2dt$ on
  the cubic continuous extension $P_t$ of a DIRK step (page-local), plus squared differences of
  neighbouring stage values, to blend the high-order step with a first-order predictor.

## Global indicators and pairwise tests

Several sources build the global indicator not from differences of the $\beta_k$ but directly from
the data, or test stencils pairwise:

- **Undivided-difference global indicators.** Li, Li, Don & Wang (2023a, Eq. (42)) replace the global
  indicator of the multi-resolution A-WENO scheme, $\big(\tfrac12(|\beta_2-\beta_0|+|\beta_2-\beta_1|)\big)^2$
  on nested central stencils (Eq. (23)), by the squared fifth undivided difference on the six-point
  stencil,
  $$\tau^*=\big(-f_{i-2}+5f_{i-1}-10f_i+10f_{i+1}-5f_{i+2}+f_{i+3}\big)^2,$$
  which is $O(\Delta x^{10})$ for smooth data and makes the scheme more upwind when a jump sits at
  $x_{i+3}$ ([multi-resolution WENO](/methods/multi-resolution-weno.md)); its base indicator for the
  constant candidate is $\min\big((f_{i-1}-f_i)^2,(f_i-f_{i+1})^2\big)$, as in Wang et al. (2021).
  Huang, Liang & Fu (2023, Eq. (32)) use, for TENO5-A, a "sixth-order" five-point $\tau_5$ printed as a
  quadratic form with prefactor $1/5040$ instead of $|\beta_1-\beta_2|$ in the TENO labelling.
  *(Compiler check, not in the sources: the printed form vanishes on samples of polynomials of degree 0
  to 2 but not on cubics, and on samples of $\sin(x_0+j\Delta x)$ it falls by a factor of about 64 per
  halving of $\Delta x$, i.e. it is $O(\Delta x^6)$.)*
- **Pairwise relative difference.** Hong et al. (2022, Eqs. (22)–(26)) accept a three-point extension
  stencil of TENO-M only if
  $|\beta^*_{(a,b)}-\beta^*_{(b,a)}|/\big(\max(\beta^*_{(a,b)},\beta^*_{(b,a)})+\epsilon\big)<C_s$, $C_s=0.8$,
  where $\beta^*_{(a,b)}$ (page-local) is the three-point Jiang–Shu-type indicator of stencil $a$ with the
  derivatives taken at the node it shares with the accepted neighbour $b$; no $\tau$ and no normalization
  enter ([targeted ENO](/methods/targeted-eno.md)). *(Compiler check, not in the sources: the ratio is
  below 1 for non-negative indicators, so $C_s=1$ accepts every extension and $C_s=0$ none, the limits
  that the paper's spectral analysis associates with the linear scheme and with TENO5.)*
- **Generalized undivided differences.** Jeong, Yang & Yoon (2022, §4, Eqs. (29)–(38)) build indicators
  from difference operators that are exact on $\{e^{-\nu_kx},e^{\nu_kx},x^2\}$ (three points) or
  $\{e^{-\nu x},e^{\nu x},x^2,x^3,x^4\}$ (five points), page-local fitted exponents $\nu_k$, $\nu$:
  $\beta_k=(\theta_{\mathrm G}|\nabla^1_kf|+|\nabla^2_kf|)^2$ and $\tau_{\mathrm G}=|\nabla^4f|^2$ (page-local
  operators $\nabla^\alpha_k$, mixing parameter $\theta_{\mathrm G}$, global indicator $\tau_{\mathrm G}$, as on
  [RBF-based WENO](/methods/rbf-weno.md)). With fitted exponents each difference
  gains one order (Lemmas 4.1, 4.3, 4.4), and as $\nu\to0$ the classical undivided differences
  $(1,-3,2)$, $(-1,1)$, $(1,-2,1)$ and $(1,-4,6,-4,1)$ return
  ([RBF-based WENO](/methods/rbf-weno.md)).

- **Pairwise agreement of squared indicators.** Liang & Fu (2026, §3.3, Eqs. (27)–(28)) detect discontinuities for
  mesh adaptation from the indicators already computed by the reconstruction. With $b_k=\beta_k^2$ (page-local),
  $$\Delta\beta_{kl}=\frac{2b_kb_l+\epsilon}{b_k^2+b_l^2+\epsilon}\in(0,1],\qquad
  \chi_{\mathrm d}=\min(\Delta\beta_{01},\Delta\beta_{02},\Delta\beta_{12}),\qquad\epsilon=10^{-8}$$
  (page-local $\Delta\beta_{kl}$ and detection variable $\chi_{\mathrm d}$, the source's $\chi$, not the registry's $\chi_k$):
  $\Delta\beta_{kl}\approx1$ when the two indicators agree and $\approx0$ when one stencil crosses a jump, the bound
  following from $2b_kb_l\le b_k^2+b_l^2$. Squaring the indicators is meant to give "strong scale separation". On four
  static profiles with $400$ points, among them the Jiang–Shu composite profile, $\chi_{\mathrm d}$ falls at the
  discontinuities and non-smooth regions (Fig. 3); its use is on [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
- **Compact gas-kinetic stencils.** In the WENO-AO-type reconstruction of compact gas-kinetic schemes,
  Zhao, Ji, Shyy & Xu (2023, §3.4, Eqs. (31)–(32)) form the WENO-Z reference value from the sub-stencil
  indicators, $|3(\beta_1-\beta_2)+(\beta_3-\beta_2)|$ for their eighth-order 1-D stencils and
  $\tfrac13\sum|2\beta_0-\beta_k-\beta_l|$ over the three pairs on triangles, and replace the indicator
  of the large stencil by the maximum of the small ones to save cost ([WENO-AO](/methods/weno-ao.md)).
  The minimum and maximum indicators of the cells on each side of a face are reused to limit the
  third- and fourth-order time-derivative terms of their two-stage time stepping (Eq. (27)).

- **TENO measures without a global indicator.** Several sources print the TENO measure as
  $\gamma_k=(\beta_k+\epsilon)^{-q}$, $q=6$, without the constant $C$ and the global indicator of the registry form:
  Chen & Chen (2026, §2.3.1, Eq. (19), $\epsilon=10^{-40}$) for the five-point finite-difference TENO5 they take from
  Fu, Hu & Adams; Liang et al. (2025, §3.3.3, Eq. (22), $\epsilon=10^{-12}$) on unstructured meshes, as Ji, Liang & Fu above;
  Huang et al. (2025a, Eqs. (12), (15)) on DG polynomials ([targeted ENO](/methods/targeted-eno.md)). Liang & Fu (2026,
  Eq. (17)) keep the form $(1+\tau_{\mathrm C}/(\beta_k+\epsilon))^6$ with the $\tau_{\mathrm C}$ above.

## Indicators of blended reconstructions

Wan & Xia (2022, Eq. (3.9)) give the indicator of a fixed linear combination of the quartic
and the two linear candidates of a CWENO-type reconstruction in closed form, from the quartic's
indicator and two differences, with an absolute value against round-off, and bound the indicator of a
blend $P=W_1P^{\mathrm L}+W_2P^{\mathrm N}$ of a linear and a nonlinear reconstruction by
$2(W_1^2\beta^{\mathrm L}+W_2^2\beta^{\mathrm N})$, using $(A+B)^2\le2(A^2+B^2)$ (page-local
$P^{\mathrm L}$, $P^{\mathrm N}$, $W_{1,2}$; Eqs. (3.10)–(3.13); [hybrid schemes](/methods/hybrid-weno.md)).

## Other meanings of the term

Several sources use "smoothness indicator" for quantities of a different kind:

- Basile et al. (2022, §4.2, Eqs. (36)–(37)), after Mavriplis, call the decay rate $\varrho_K$ of a
  least-squares fit $\mathcal N_n\simeq Ce^{-\varrho_Kn}$ to the per-degree norms $\mathcal N_n$ of a DG element's modal
  coefficients, $n\ge1$, a smoothness indicator (page-local symbols); $\varrho_K>1$ means smooth and selects
  $p$-enrichment, otherwise $h$-refinement. It grows with smoothness, the opposite sense of $\beta_k$,
  and is computable only for degree $\ge2$ ([h- and hp-adaptation](/methods/hp-adaptation.md)).
- **First-order measures for detection.** Two TENO sources prefer low-order measures to the high-order indicators for
  telling discontinuities from fluctuations. Chen & Chen (2026, §2.3.2, Eqs. (23)–(25)) drive the TENO cut-off by the
  discontinuity indicator of Ren et al.,
  $\mathfrak r_i=\big(\lvert2\Delta f_{i+1/2}\Delta f_{i-1/2}\rvert+\epsilon_{\mathrm r}\big)/\big((\Delta f_{i+1/2})^2+(\Delta f_{i-1/2})^2+\epsilon_{\mathrm r}\big)$,
  $\Delta f_{i+1/2}=f_{i+1}-f_i$, $\epsilon_{\mathrm r}=\tfrac{0.9C_{\mathrm r}}{1-0.9C_{\mathrm r}}\,10^{-6}$, $C_{\mathrm r}=0.24$ (page-local
  $\mathfrak r_i$, $\epsilon_{\mathrm r}$, $C_{\mathrm r}$; the $\sigma_i$, $\epsilon_\sigma$, $C_r$ of [adaptive TENO](/methods/adaptive-teno.md), renamed here
  because this page uses $\sigma$ for a scaling), a "low-order undivided difference" that they argue detects
  discontinuities better than high-order undivided differences ([adaptive TENO](/methods/adaptive-teno.md)). Liang et al.
  (2025, §1, §3.3.4) call the high-order undivided differences of WENO/TENO indicators "over-sensitive" to both
  high-wavenumber fluctuations and discontinuities, citing Ren et al. for first-order measures being "more sensitive to
  discontinuities than to high-wavenumber fluctuations", and build their unstructured troubled-cell indicator from the
  variance of relative first-order cell-average jumps ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
  Both keep the high-order $\beta_k$ inside the TENO weights. *(Compiler check, not in the sources: $\mathfrak r_i$ has the
  structure of Liang & Fu (2026)'s $\Delta\beta_{kl}$ above, applied to two one-sided differences instead of two squared
  indicators.)*
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
- Hiejima (2022, Eq. (14)) writes the sum over $n=1,\dots,(K-1)/2$ (Hiejima's $r-1$) for every substencil, though the
  difference operators exist only up to one less than the substencil size (blank in the paper's Tables 1, 3,
  5); the sum runs over the available orders.
- Hong et al. (2022, Eq. (19)) print the last coefficient of the first square of the five-point
  indicator as "$-3f$" without subscript; it multiplies $f_{i+4}$. They print $\tau_8$ (Eq. (20))
  without the absolute value of their definition (Eq. (10)).
- Qin et al. (2023) take $\beta_1=\min(\delta_0^2,\delta_1^2)$ with the one-sided divided differences times $\Delta x$
  (Eq. (22)), the form of Wang et al. (2021) extended to non-uniform points; they print the first member of
  Eq. (22) without the factor $\Delta x$ that the last member carries.
- Chamarthi (2023b, Eq. (46)) prints the WCNS7M indicator as $\sum_n\big(\sum_lc_{n,k,l}u_{i+k+l-5}\big)$ without the
  square of the inner sum and without its coefficients.
- Li, Chen & Ren (2022a, Eq. (44)) print the $f_{i-2}^2$ coefficient of $\beta_6$ as 271799 against
  271779 in Ye et al. (2022); see [MDCD schemes](/methods/mdcd-scheme.md).
- Fan et al. (2023, §2.2) print the indicator of the point-value Hermite quartic of their derivative
  limiter in the same four combinations as above. *(Compiler check, not in the sources: for $u=x^3$
  sampled at $-1,0,1$ with exact derivatives, $\Delta x=1$, the quartic is $x^3$ and the integral
  definition gives $\tfrac9{80}+3+36=39.1125$, the printed form 39.06; both agree on linear and
  quadratic data, so the printed coefficients are not the Jiang–Shu indicator of the stated
  quartic.)*
- Wan & Xia (2022, end of §3.1) conclude $\beta^{\mathrm C}\le2\big(\beta^{\mathrm A}+K\min_k\beta_k\big)$
  from $\beta^{\mathrm C}\le2Q\beta^{\mathrm N}$ (page-local symbols of the
  [hybrid schemes](/methods/hybrid-weno.md) page). *(Compiler check, not in the sources: the step needs
  $\beta^{\mathrm N}\le\beta^{\mathrm A}$, whereas their argument uses $\beta^{\mathrm A}\le\beta^{\mathrm N}$;
  the bound holds only with the factor $\beta^{\mathrm N}/\beta^{\mathrm A}$ kept.)*
- Wang et al. (2023c, Eq. (3.20)) omit the cross term $-3495756\,u_iu_{i+1}$ of the quartic indicator.
  *(Compiler check, not in the sources: the integral definition gives it, mirror image of the printed
  $-3495756\,u_{i-1}u_i$; the other fourteen coefficients agree, and without it the printed form does not
  vanish on constants, its coefficients summing to 3495756.)*
- Zhong et al. (2023, Eq. (14)) print the WENO-NS global indicator as
  $\tfrac12\big(|\beta_0-\beta_2|^2+g(\mathsf L_{1,1})\big)^2$ with $g(x)=x^3/(1+x^3)$; the bundle has no
  source by Ha et al. to check it against.
- Balsara et al. (2023, §1) credit the perfect-square form for finite-difference WENO to their ref. [5],
  a divergence-free MHD paper; §6.3 and §10 credit the WENO-AO paper, their ref. [6].

# Citations

- [Li et al. (2022b)](/sources/li-2022-b.md) — §2, Eqs. (6)–(11), (16), Table 3.
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
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — App. A, Eq. (A.2).
- [Li, Shu & Qiu (2022d)](/sources/li-2022-d.md) — §2.1, Eqs. (2.13)–(2.20); §2.2, Eqs. (2.48)–(2.55).
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
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §1; §2.2, Eqs. (9)–(10), (16)–(20); §3.3, Eqs. (22)–(26).
- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §3.1, Eqs. (43)–(45).
- [Balsara, Samantaray & Subramanian (2023)](/sources/balsara-2023.md) — §1; §3, Eqs. (14)–(30); §6.3; §10.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §2.3, Eq. (17); §3.2, Eq. (23).
- [Qin, Chen, Lin & Deng (2023)](/sources/qin-2023.md) — §2.1, Eqs. (13)–(22); §3, Tables 10–12, Fig. 6.
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §2.3, Eqs. (15)–(18); §4.2.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §3, Eq. (46).
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — §2.1, Step II, Eq. (2.4); §2.2.
- [Li, Li, Don & Wang (2023a)](/sources/li-2023.md) — §2.1.1, Eqs. (17)–(23); §2.3, Eq. (42).
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §2, Eqs. (10), (16); §3.2, Eq. (32).
- [Jeong, Yang & Yoon (2022)](/sources/jeong-2022.md) — §4, Eqs. (29)–(38), Lemmas 4.1–4.4; App., Eqs. (54)–(55).
- [Wan & Xia (2022)](/sources/wan-2022.md) — §2.2, Eqs. (2.14)–(2.20); §3, Eqs. (3.8)–(3.13).
- [Liang et al. (2022)](/sources/liang-2022.md) — §2.2, Eqs. (11)–(12).
- [Chen & Deng (2023)](/sources/chen-2023.md) — §2, Eqs. (14)–(16); §3, Eqs. (28)–(30).
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §2, Eqs. (7)–(18); §3.1–3.2, Eqs. (19)–(26), Table 1, Lemma 1; §3.3, Eqs. (27)–(30); §4, Examples 10, 11, 17.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §3, Eqs. (3.19)–(3.22).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.2.2, Eqs. (26)–(28).
- [Gu et al. (2023)](/sources/gu-2023.md) — §2.4, Eq. (2.6).
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §2.2, Eqs. (13)–(16); §3.1, Eqs. (31)–(34).
- [Huang & Fu (2024)](/sources/huang-2024.md) — §2, Eqs. (9)–(11); §4.3, Eq. (32); §4.4, Eq. (41); §5.2, Eq. (59).
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §3.1.2, Eqs. (25)–(26); §3.2.2, Eq. (29).
- [Nogueira et al. (2024)](/sources/nogueira-2024.md) — §3.1, Eqs. (12)–(14).
- [Zhao et al. (2023)](/sources/zhao-2023.md) — §3.3, Eq. (27); §3.4, Eqs. (28)–(32).
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §2.4–2.5, Eqs. (11), (16); §5.1, Eq. (36).
- [Chen & Fu (2024)](/sources/chen-2024.md) — §4.2, Eqs. (15)–(20); §5.4.1, Eq. (56).
- [Fan et al. (2025a)](/sources/fan-2025.md) — §2.1, Eqs. (2.8)–(2.11); §2.2, Eqs. (2.19)–(2.22).
- [Komissarov & Phillips (2024)](/sources/komissarov-2024.md) — App. A, Eqs. (A3)–(A10) (arXiv v3).
- [Liang & Fu (2026)](/sources/liang-2026.md) — §3.2.2, Eqs. (17)–(19); §3.2.3, Eqs. (22)–(23); §3.3, Eqs. (27)–(28), Fig. 3: five-point FV indicator, $\tau_{\mathrm C}=\lvert2\beta_0-(\beta_1+\beta_2)\rvert$ and its expansion, pairwise detection variable.
- [Ren et al. (2025)](/sources/ren-2025.md) — §5.1.1, Eq. (45): quartic indicator of multi-resolution WENO.
- [Fan et al. (2025b)](/sources/fan-2025-b.md) — §2.2, Eqs. (13)–(17): WCNS3-MR indicators with amplifying parameter.
- [Huang et al. (2025a)](/sources/huang-2025.md) — §3.1, Eqs. (11)–(14); §3.2.1, Eqs. (15)–(17): DG-polynomial indicator over the target cell.
- [Chen & Chen (2026)](/sources/chen-2026.md) — §2.3.1, Eqs. (19)–(20); §2.3.2, Eqs. (23)–(25): TENO measure without $\tau$, Ren et al.'s first-order indicator.
- [Liang et al. (2025)](/sources/liang-2025.md) — §1, §3.3.3–3.3.4, Eq. (22): over-sensitivity of high-order differences, unstructured TENO measure.
