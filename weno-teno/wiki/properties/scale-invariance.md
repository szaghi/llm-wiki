---
type: Property
title: "Scale and affine invariance"
description: "A reconstruction or limiter is scale-invariant when it commutes with multiplication of the data by a constant, and affine-invariant when it also commutes with adding a constant; classical WENO weights have neither property because ε is absolute, and the sources reach it by normalised variables, relative ε, or globally normalised damping."
status: established
aliases: [scale-invariant, affine-invariant, Ai-property, Si-property, homogeneity of a reconstruction, normalisable scheme, homogeneity of the evolution operator]
tags: [reconstruction, weno, limiting, dg]
timestamp: 2026-10-23T23:55:00Z
---

# Scale and affine invariance

Let $\mathsf R$ be a reconstruction operator that maps stencil data to an interface value (or a
limiter that maps a solution to a limited one; page-local, since the registry's $R$ is the
right-eigenvector matrix). With page-local constants $\sigma\ne0$ and $\mu$:

- $\mathsf R$ is **scale-invariant** if $\mathsf R[\sigma f]=\sigma\mathsf R[f]$ (Deng 2023, Definition 7; the "Si-property"
  of Wang & Don 2022, Definition 4);
- $\mathsf R$ is **affine-invariant** if $\mathsf R[\sigma f+\mu]=\sigma\mathsf R[f]+\mu$ (the "Ai-property" of Wang & Don
  2022, Definition 2, Eq. (3)).

Wang & Don (2022, §1) motivate the affine case with data that are affine images of other fields:
the momentum flux $\rho v^2+p$ is affine in $v^2$ where $\rho$ and $p$ are locally constant, and the
shallow-water still-water flux is affine in the bottom elevation. Peng, Sun & Wu (2024, §1.2) add a
dimensional argument: a damping coefficient that enters an exponential must be dimensionless.
Consistent linear reconstructions reproduce constants and are therefore affine invariant (Deng 2023,
§3.1, states that every consistent linear operator is normalisable); the property is lost through the
nonlinear parts (weights, indicators, damping coefficients) when these contain dimensional constants.

## Terminology across the sources

The sources that use the word differ. Wang & Don (2022) separate scale invariance ($\mu=0$)
from affine invariance. Deng (2023) defines scale invariance as homogeneity only, and so do Chen & Wu
(2022, Lemma 3.1), for whom it is the homogeneity of degree one of reconstruction, limiter and scheme. Peng, Sun & Wu
(2024, Theorem 2.6) call "scale-invariant" what Wang & Don call affine invariant:
$\mathcal S(\sigma u_h+\mu)=\sigma\mathcal S(u_h)+\mu$ for their oscillation-eliminating step
$\mathcal S$ (page-local name). Fan & Wu (2024, Definition 1; arXiv v1 read) do the same for the Hermite
WENO setting: an operator is "scale-invariant" if it commutes with
$A_{\sigma,\mu}:(\bar u_j,\bar u^{(1)}_j)\mapsto(\sigma\bar u_j+\mu,\sigma\bar u^{(1)}_j)$ for all $\sigma\ne0$,
$\mu\in\mathbb R$ (page-local $A_{\sigma,\mu}$; the first moment $\bar u^{(1)}_j$ is not shifted), which is
affine invariance in the terms of this page. This page uses Wang & Don's split. Li, Li, Don & Wang (2023a, Definition 1)
follow Wang & Don's scale invariance, $\mathsf R[\sigma f]=\sigma\mathsf R[f]$ for every real $\sigma$, negative
values included, i.e. homogeneity of degree one.

## How classical weights fail

In Jiang–Shu and WENO-Z weights the [smoothness indicators](/definitions/smoothness-indicator.md)
scale as $\beta_k[\sigma f+\mu]=\sigma^2\beta_k[f]$ while $\epsilon$ does not, so the weights
depend on $\sigma$ (Wang & Don 2022, Eq. (18)).

- Deng (2023, App. A.2, Fig. 13) measures the scale-invariance error
  $\max_x|\mathsf R[\sigma\bar u]/\sigma-\mathsf R[\sigma_0\bar u]/\sigma_0|$ with $\sigma_0=10^{20}$ on $N_x=320$
  cells: WENO-JS3 with $\epsilon=10^{-6}$ depends clearly on $\sigma$; with $\epsilon=10^{-40}$ the
  error grows for $\sigma<10^{-10}$; WENO-Z3 and WENO-P3 with $\epsilon=10^{-40}$ show errors too. Deng
  also recalls Don et al. (2022): WENO-Z with $\epsilon=10^{-12}$ and WENO-JS with $\epsilon=10^{-6}$
  oscillate on Sod's problem scaled by $10^{-7}$.
- Wang & Don (2022, §3.2) show that a scale-invariant but not affine-invariant scheme still fails:
  for data $10^{-7}f+1$, the Si descaler is dominated by the offset, $\epsilon$ swamps the
  $\beta_k$, and the weights collapse to the linear weights, destroying the
  [ENO property](/definitions/eno-property.md).
- Chen & Wu (2022, Remark 3.3) show a failure that a scaled $\epsilon$ alone does not cure: in the
  Zhu–Qiu weights $d_\ell\big(1+\tau^2/(\beta_\ell+\epsilon)\big)$ on triangles, $\tau^2$ scales as
  $\sigma^4$ and $\beta_\ell+\epsilon$ as $\sigma^2$, so the ratio is of degree 2 in the data even
  with $\epsilon\propto\sigma^2$ ([CWENO](/methods/cweno.md), [WENO-Z](/methods/weno-z.md), whose
  table of Z-type weights records the same degree count).
- Li et al. (2022b, §4.1) object to the WENO-Z variant with $\epsilon=\Delta x^m$ of Don & Borges
  that $\beta_k$ and $\Delta x$ have different dimensions, so the solution depends on the reference
  values used to nondimensionalize the problem.

- **Exponential weights.** Chen & Deng (2023, §5) describe their weights
  $d_k\exp(-\beta_k^{\lambda_{\mathrm E}}/\lambda_{\mathrm E})$ as built "without using any dimensional
  scales": they use stencil data only, with no $\Delta x$-dependent $\epsilon$ and no global quantity
  ([exponential weights](/methods/exponential-nonlinear-weights.md)). *(Compiler check, not in the
  sources: the weights are still not scale-invariant. For $\lambda_{\mathrm E}=1$,
  $\omega_k/\omega_l=(d_k/d_l)e^{-(\beta_k-\beta_l)}$ and $\beta_k\mapsto\sigma^2\beta_k$ under
  $f\mapsto\sigma f$, so the ratio depends on $\sigma$; the exponent's argument
  $\tau_5/(\min_k\beta_k+\epsilon)^{0.8}$ scales as $\sigma^{0.4}$, and the constants 3, 0.8, $10^{-6}$ act
  on data in absolute units. Translation by $\mu$ leaves the $\beta_k$ unchanged, so the defect is one of
  scaling only.)*
- **Indicators that carry the cell width.** Zhong et al. (2023, Eq. (21)) fix the parameter of their
  $L^1$-derived indicators to $\xi_{\mathrm{NS}}=\Delta x$, which gives
  $\beta^{\mathrm{IMP}}_k=c_k\Delta x\,(\text{first difference})^2+(\text{second difference})^2$ with $c_k=4,1,4$
  (page-local $\xi_{\mathrm{NS}}$, $\beta^{\mathrm{IMP}}_k$, $c_k$)
  ([smoothness indicators](/definitions/smoothness-indicator.md)). *(Compiler check, not in the sources:
  under $f\mapsto\sigma f$ both terms and the global indicator scale by $\sigma^2$, so the weights are
  scale-invariant up to $\epsilon=10^{-40}$; but $\Delta x$ is a length and the differences are undivided, so the
  balance of the two terms, and the weights, change with the unit of length, which classical Jiang–Shu
  indicators of undivided differences do not.)* The paper does not discuss invariance.
- **High powers of the global indicator.** The unstructured CWENOZ weights of Maltsev et al. (2023,
  Eqs. (22)–(23)) raise the mean indicator difference to the fourth power against an exponent 1 on the
  ratio, a ratio of degree 6 in the data *(compiler check, not in the sources; see the homogeneity count
  on [WENO-Z](/methods/weno-z.md))*.

## A criterion for WENO-type operators

Li, Li, Don & Wang (2023a, §2.3) turn the reduction to the weights into necessary and sufficient
conditions for an operator $\mathsf R[f]=\sum_k\omega_k[f]P^{(k)}[f]$ with linear candidates:
**Theorem 1**, $\mathsf R$ is scale-invariant iff $\omega_k[\sigma f]=\omega_k[f]$ for all $k$;
**Theorem 2**, for $\epsilon>0$ this holds iff $\alpha_k[\sigma f]=C\,\alpha_k[f]$ with $C$ independent of
$k$. They name WCNS, TENO, Hermite WENO, WENO-Z+M, unstructured finite-volume WENO with unequal
substencils and approximations of high-order derivatives as schemes the criterion can check.
**Theorem 3** applies it: the multi-resolution A-WENO operator of Wang, Zhu, Yang & Zhao is not
scale-invariant for any $\sigma\ne0,\pm1$, proved on data with nonzero global indicator, because the ratio
$\alpha_k[\sigma f]/\alpha_k[f]$ depends on $k$, which they trace to the different scalings of $\beta_k$, $\tau$
and $\epsilon$ *(compiler check, not in the sources: $\tau$ is quartic and $\beta_k$ quadratic in the data, so the
dependence on $k$ persists even for $\epsilon=0$)* ([multi-resolution WENO](/methods/multi-resolution-weno.md)).
With a squared undivided-difference global indicator and $\epsilon\,\mathsf m^2$, $\mathsf m$ the mean of
$|f_j|$ (the Si descaler), **Theorem 4** proves invariance; the measured error
$\max|\mathsf R[\sigma f]/\sigma-\mathsf R[f]|$, floored at machine epsilon, is at round-off in quadruple
precision for $\sigma\in[10^{-19},10^{19}]$ on sine, ReLU and Heaviside data, while the original operator's
error vanishes only at $\sigma=1$ (§2.4, Fig. 3). On the Lax problem scaled by $10^{-7}$ the original scheme
oscillates even with $\epsilon=10^{-40}$ (Fig. 1).

## Routes to invariance

**Relative sensitivity parameter.** Replace $\epsilon$ by $\epsilon\,\mathsf m^2[f]$ with
$\mathsf m$ the mean absolute value of the stencil data (Si-WENO, Don et al. 2022, as recalled) or
its mean absolute deviation (Ai-WENO); Wang & Don (2022, Theorems 1–2) prove the Ai-property for
Z-, D- and JS-type weights ([affine-invariant WENO](/methods/affine-invariant-weno.md)). The same
paper shows the practical payoff: shallow-water still water preserved to roundoff without the
"WENO linearization technique" ([well-balancing](/properties/well-balancing.md)). Li et al. (2023a, §4, Theorem 5)
obtain the analogous payoff for the Euler equations with gravity: in a characteristic-wise
[A-WENO](/methods/alternative-weno.md) scheme the equilibrium characteristic variables are the
equilibrium pressure times an interface constant, so a scale-invariant interpolation (an affine-invariant
one is not needed) keeps hydrostatic states to round-off in double and quadruple precision.

**Data-scaled $\epsilon$ with matching powers.** Chen & Wu (2022, §3.2.1, Eq. (32), Lemma 3.1) make
the Zhu–Qiu weights homogeneous by squaring the denominator and scaling the regularization with the
data and the mesh,
$$\alpha_\ell=d_\ell\Big(1+\frac{\tau^2}{(\beta_\ell+\epsilon)^2}\Big),\qquad \epsilon=|K_0|\max_{K\in N_0}\bar u_K^2,$$
so that $\beta_\ell$, $\tau$ and $\epsilon$ all scale by $\sigma^2$ ($|K_0|$ the cell area, $N_0$ the
large stencil); third order is kept (Remark 3.3). The motivation is physical: the special-relativistic
Euler equations are invariant under $u\mapsto\sigma u$, so the exact evolution satisfies
$\frac1\sigma S_t(\sigma u_0)=S_t(u_0)$ (Prop. 2.1; page-local evolution operators $S_t$, $S_h$), and with the HLL flux and a two-step scaling
limiter that are homogeneous too (up to their $10^{-13}$ floors), the one-step scheme satisfies
$\frac1\sigma S_h(\sigma u)=S_h(u)$ (Theorem 3.2;
[relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)). On a Riemann problem
scaled by $10^{-2}$ and $10^{-4}$ the scaled solution matches the unscaled one to
$O(10^{-12})$–$O(10^{-13})$, against $O(10^{-1})$ and $O(10^{-2})$ with overshoots for the original
weights; on a multi-scale four-state problem the original weights undershoot at the contacts and the
new ones do not (Examples 4.4–4.5, Figs. 6–9). *(Compiler check, not in the sources: adding a
constant to the data changes $\max\bar u_K^2$, so these weights are scale- but not affine-invariant,
and $\epsilon\to0$ when all data on the stencil are near zero, as characteristic variables can be.)*

**Squared denominators in Hermite WENO.** Cai, Qiu & Wu (2024, §3.1.2, Eq. (3.8), Remark 3.2; arXiv v1 read) take the
same step for the moment-based [Hermite WENO](/methods/hermite-weno.md) of a physical-constraint-preserving scheme for
special-relativistic hydrodynamics, crediting Chen & Wu for the idea:
$$\alpha_n=d_n\Big(1+\frac{\tau^2}{\beta_n^2+\epsilon}\Big),\qquad \tau=\tfrac12\big(|\beta_0-\beta_1|+|\beta_0-\beta_2|\big),$$
(page-local $\tau$, not the registry's $\tau_5$), and state that the weights "remain unchanged" when the zeroth and first moments are multiplied by any $\sigma\ne0$. The
first-moment limiter of troubled cells uses $d_n\big(1+\tau_\ell^2\Delta x/(\beta_{\ell,n}^2+\epsilon)\big)$ (page-local).
*(Compiler check, not in the sources: $\tau^2$ and $\beta_n^2$ both scale as $\sigma^4$, so the ratio has degree 0 in the
data, and the weights are invariant up to $\epsilon$, whose value the paper does not print and which is not scaled with the
data as in Chen & Wu; the extra $\Delta x$ in the limiter weights makes them change with the unit of length, as for the
indicators of Zhong et al. above.)* In the same scheme the characteristic projection uses rescaled eigenvector pairs
$(cr,l/c)$ with $c=\sqrt{|l|/|r|}$, which the authors find necessary to avoid oscillations on an ultra-relativistic 2-D
Riemann problem (Remark 3.3, Example 5.7); it is a fix of the arbitrary eigenvector scaling that Peng et al. identify below
as a threat to invariance ([characteristic decomposition](/methods/characteristic-decomposition.md)).

**Normalised variables.** In a compact three-cell stencil, a reconstruction that depends on the
data only through the normalized cell average $\tilde u_i=(\bar u_i-\bar u_{i-1})/(\bar u_{i+1}-\bar u_{i-1})$
is called *normalisable*, $\tilde u_{i+1/2}=\mathcal R(\tilde u_i)$, and Deng (2023, Proposition 2) proves
it scale-invariant:
$u^-_{i+1/2}=(\bar u_{i+1}-\bar u_{i-1})\mathcal R(\tilde u_i)+\bar u_{i-1}$. *(Compiler check, not
in the sources: $\tilde u_i$ is unchanged by $\bar u\mapsto\sigma\bar u+\mu$, so the same formula
gives affine invariance as well.)* Consistent linear schemes are normalisable; WENO3-JS, WENO-Z3 and
WENO-P3 are not (§4.3). Proposition 6: a WENO3 operator whose weight depends only on $\tilde u_i$ is
normalisable, hence scale-invariant. Deng's NewWENO (Eq. (6.6)),
$\omega_0=\tfrac13+\tfrac23\big(1+\gamma_0\tilde u_i^{2}\big)^{-2}-\tfrac13\big(1+\gamma_0(1-\tilde u_i)^2\big)^{-2}$
with page-local $\gamma_0=25$ (the paper's $\gamma$, $m=1$, $n=2$), has a scale-invariance error near
machine precision for scaling factors in $[10^{-19},10^{19}]$ (Fig. 13). The
[ROUND schemes](/methods/round-scheme.md) are designed directly as functions $\mathcal R(\tilde u_i)$ on
the [normalised-variable diagram](/definitions/normalised-variable-diagram.md) and are scale-invariant
by construction (Deng 2023, §7; Huang et al. 2026, §2.2). Huang et al. (2026, §3.4) sample the
learned WENO3-NN on this diagram by *assuming* it is scale-independent; its input layer normalizes
differences by $\max(|\bar u_i-\bar u_{i-1}|,|\bar u_{i+1}-\bar u_i|,\epsilon)$, which the paper calls
"Galilean invariance" ([learned WENO weights](/methods/learned-weno-weights.md)). Bezgin, Schmidt &
Adams (2022, §3.2, Eqs. (14)–(15)), who designed that layer, state that the features are invariant
under adding a constant and, up to $\epsilon$, under scaling, so the whole weight function is.
*(Compiler check, not in the sources: the features depend only on the ratio of the two one-sided
differences, i.e. on $\tilde u_i$, so up to $\epsilon$ WENO3-NN is normalisable and affine-invariant.)*

**Globally normalized damping in DG.** Peng, Sun & Wu (2024, Eq. (2.6)) normalize the damping
coefficient of the [OEDG](/methods/oedg.md) step by $\|u_h-\mathrm{avg}(u_h)\|_{L^\infty(\Omega)}$ and
multiply it by a local wave-speed estimate. The coefficient is then invariant under
$u_h\mapsto\sigma u_h+\mu$, which gives affine invariance of the step (Theorem 2.6) and *evolution
invariance*: for $u_t+\lambda f(u)_x=0$ (page-local constant $\lambda$) at fixed CFL number the results after $n$ steps do not depend
on $\lambda>0$ (Theorem 2.10). The damping of the earlier oscillation-free DG scales as $|\sigma|$ and
carries no wave speed; it smears the Lax and Shu–Osher problems scaled by 100 and oscillates when
they are scaled by 0.01, while OEDG gives identical results for factors 1, 0.01 and 100 (Remark 2.8;
Ex. 5.6, 5.8). A locally normalized coefficient (Eq. (2.14)) is proposed, but no mesh-independent
constant for it has been found (Remark 2.9). Peng et al. also note that a characteristic
decomposition can destroy invariance, because eigenvectors are defined up to an arbitrary scaling
(Remark 2.12, Ex. 5.7; [characteristic decomposition](/methods/characteristic-decomposition.md)).

**A dimensionless transformation of the stencil data.** Fan & Wu (2024, §2.2.4, Definitions 2–3,
Theorem 5) make a nonlinear reconstruction invariant from outside instead of changing its weights, the
route of Wang & Don and Deng above. On the stencil $\Lambda_i$ of cell $i$ they map the moments to
$$\hat u_j=\frac{\bar u_j-u_{\mathrm{ave}}}{u_{\max}-u_{\min}+\epsilon_{\mathrm m}},\qquad
\hat u^{(1)}_j=\frac{\bar u^{(1)}_j}{u_{\max}-u_{\min}+\epsilon_{\mathrm m}},$$
with $u_{\mathrm{ave}}$, $u_{\max}$, $u_{\min}$ the mean, maximum and minimum of the $\bar u_j$ on $\Lambda_i$ and
$\epsilon_{\mathrm m}=10^{-15}$ (page-local symbols), apply the [Hermite WENO](/methods/hermite-weno.md) operator
$\mathcal H$ to the mapped data, and map back, $\mathcal H_{\mathcal D}=\mathcal D_u^{-1}\mathcal H\mathcal D$ with
$\mathcal D_u^{-1}\hat u_h=(u_{\max}-u_{\min}+\epsilon_{\mathrm m})\hat u_h+u_{\mathrm{ave}}$ (Eqs. (2.30)–(2.33)).
Theorem 5 proves $\mathcal H_{\mathcal D}$ affine-invariant when $\epsilon_{\mathrm m}$ is "treated as machine zero";
the paper states that $\mathcal D$ "can render any nonlinear reconstruction operator" (WENO, HWENO)
invariant, and proves it for HWENO only. *(Compiler check, not in the sources: for $\sigma<0$ the range is
$|\sigma|(u_{\max}-u_{\min})$ and the mapped data change sign; invariance then also needs $\mathcal H$ to be odd,
$\mathcal H[-f]=-\mathcal H[f]$, which holds for weights that depend on the data only through quadratic
indicators.)*

**Normalized damping in Hermite WENO.** The oscillation-eliminating step of Fan & Wu's OE-HWENO carries the
[OEDG](/methods/oedg.md) normalization over: its damping coefficient is a sum of value and derivative jumps
divided by $\max_i|\bar u_i-u_\Omega|$, $u_\Omega$ the global mean (page-local), so $F_{\mathrm{OE}}$ commutes
with $A_{\sigma,\mu}$ (Theorem 4). With homogeneous fluxes the whole solution operator is homogeneous of degree
one (Theorem 6), and for $u_t+\lambda f(u)_x=0$ at fixed CFL number the results do not depend on $\lambda>0$
(evolution invariance, Theorem 7), because the damping factor depends on the product of the wave speed and
$\Delta t$. The tests show the payoff against the oscillation-free OF-HWENO of Zhao & Qiu, whose damping
terms and HWENO operator the authors call not scale-invariant (§2.2.4): on a Lighthill–Whitham–Richards
traffic problem written in three equivalent unit systems (hours and km, minutes and km, minutes and m)
OE-HWENO gives consistent results while OF-HWENO smears in one and oscillates and shifts the discontinuity
in another (Ex. 3, Fig. 3.1); on the Lax problem scaled by $\sigma\in\{10^{-7},1,10^7\}$ OE-HWENO is
invariant while OF-HWENO smears at $10^7$ and oscillates at $10^{-7}$ (Ex. 4, Fig. 3.2); on a 2-D Riemann
problem scaled by 100 OF-HWENO "excessively smears" (Ex. 9, Fig. 3.8).

## Qualifications

- Fan & Wu (2024, Definition 4) print the 2-D transformation with
  $u_{\mathrm{ave}}=\frac1{\#\Lambda_{i,j}}\sum|\bar u_\kappa|$, with absolute values that the 1-D Eq. (2.31) does not
  have, and state the 2-D invariance proof as "similar to Theorem 5". *(Compiler check, not in the sources:
  with the absolute values the shift part fails for sign-changing data, since
  $|\sigma\bar u+\mu|\ne\sigma|\bar u|+\mu$ in general; the 1-D form is the consistent one.)* *(Compiler check, not in the sources: like that of OEDG,
  the OE damping is normalized by a global range, so its strength in one region depends on the data elsewhere.)*
- **Invariance and accuracy can conflict.** *(Compiler check, not in the sources.)* In smooth
  regions $\tilde u_i=\tfrac12+O(\Delta x)$ (Deng 2023, Lemma 1), and a weight that depends on
  $\tilde u_i$ alone tends to its value at $\tfrac12$, not to the linear weight. For NewWENO,
  $\omega_0(\tfrac12)=857/2523\approx0.3397$ against $d_0=\tfrac13$, an $O(1)$ defect, so the
  operator is second-order with an error constant close to the third-order scheme rather than
  uniformly third order. Deng states the accuracy condition $\omega_k-d_k=O(\Delta x^2)$ (§4.3) but
  reports only error-versus-$N$ plots, no observed orders.
- In OEDG the global $L^\infty$ normalization couples the damping strength to the global solution
  range; multi-scale data in one domain are not tested.
- The nonlinear vertex weighting of Chen, Zhang, Liu & Chen (2022, Eqs. (24)–(26)), a second-order
  unstructured scheme, uses squared pressure differences and squared gradients against a fixed
  $\epsilon=10^{-3}$, and so depends on the units of the data *(compiler check, not in the sources)*
  ([gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)).
- The Ai-WENO theorems assume a zero floor in the descaler; the floors used in practice make
  invariance approximate for very small $|\sigma|$.

# Citations

- [Wang & Don (2022)](/sources/wang-2022-b.md) — §1, Defs. 1–4; §2.2–2.4, Eqs. (9)–(18), Theorem 1; §3.1–3.3; App. A.
- [Deng (2023)](/sources/deng-2023.md) — §1; §2.2–2.3, Lemma 1, Def. 7, Prop. 2; §4.3; §6.2, Prop. 6, Eq. (6.6); App. A.2, Fig. 13.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — §1; §2, Eqs. (2.6), (2.13)–(2.14), Theorems 2.6, 2.10, Remarks 2.8–2.12; Ex. 5.6–5.8.
- [Huang et al. (2026)](/sources/huang-2026.md) — §2.2; §3.2, Eq. (3.10); §3.4.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §4.1.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §2, Eqs. (13)–(14), Prop. 2.1; §3.2.1, Eqs. (32)–(34), Lemma 3.1, Remark 3.3; §3.6, Theorem 3.2; Examples 4.4–4.5.
- [Bezgin, Schmidt & Adams (2022)](/sources/bezgin-2022.md) — §3.2, Eqs. (14)–(15).
- [Chen, Zhang, Liu & Chen (2022)](/sources/chen-2022.md) — §5, Eqs. (24)–(26).
- [Chen & Deng (2023)](/sources/chen-2023.md) — §1; §3, Eqs. (26)–(34); §5.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §3.2, Eqs. (21)–(26).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.2.2, Eqs. (22)–(23).
- [Li, Li, Don & Wang (2023a)](/sources/li-2023.md) — §1, Def. 1; §2.3–2.5, Eqs. (36)–(46), Theorems 1–4, Figs. 1, 3–4; §4.2, Theorem 5.
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — §3.1.2–3.1.3, Eq. (3.8), Remarks 3.2–3.3; Example 5.7 (arXiv v1).
- [Fan & Wu (2024)](/sources/fan-2024.md) — §2.2.4–2.2.5, Defs. 1–3, Eqs. (2.30)–(2.33), Theorems 4–7; §2.3, Def. 4; Examples 3, 4, 9, Figs. 3.1, 3.2, 3.8 (arXiv v1).
