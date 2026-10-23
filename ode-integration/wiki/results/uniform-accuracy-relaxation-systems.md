---
type: Result
title: "Uniform accuracy of IMEX schemes for hyperbolic relaxation systems"
description: "For linear hyperbolic relaxation systems with Fourier–Galerkin space discretization, certain IMEX Runge–Kutta schemes of orders 2 and 3 and IMEX-BDF schemes of orders 1 to 4 converge with error constants independent of the relaxation time ε, so they keep their order in the intermediate regime where IMEX schemes usually lose it."
status: established
aliases: [uniform accuracy in ε, uniformly accurate IMEX, uniform-in-ε convergence, no order reduction in the intermediate regime, uniform stability of IMEX-BDF, uniform accuracy of IMEX-RK]
tags: [asymptotic-preserving, imex, order-reduction, stability, stiff]
timestamp: 2026-10-20T06:18:00Z
---

# Uniform accuracy of IMEX schemes for hyperbolic relaxation systems

A scheme for a problem with relaxation time $\varepsilon$ is **uniformly accurate of
order $p$** if its global error obeys $\lVert e_n\rVert\le C\,h^p$ for $nh\le T$ with $C$
independent of $\varepsilon$ (and of the spatial resolution): the order holds in the
kinetic regime $\varepsilon=O(1)$, in the limit $\varepsilon\to0$, and in the
intermediate regime between them. This is stronger than the
[asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) property, which
concerns only the two ends: the triangle-inequality argument recalled by
[Jin (2022)](/sources/jin-2022.md) (§1, eqs. (1.1)–(1.6)) turns AP into uniform
convergence at a reduced rate (stated on the AP page), not at the order of the scheme.
[Hu & Shu (2025)](/sources/hu-2025.md) (IMEX Runge–Kutta) and
[Ma et al. (2026)](/sources/ma-2026.md) (IMEX-BDF) prove uniform accuracy at full order
for linear hyperbolic relaxation systems; Jin (2022, §6.1) cites the earlier IMEX-BDF
result of Hu & Shu (2021) as "a rigorous uniform accuracy proof of AP schemes for linear
problems". Both papers state the contrast with AP explicitly (Hu & Shu, §1 and App. 7.3).

## Common setting

Both results concern linear constant-coefficient systems on a periodic interval (the
[linear hyperbolic relaxation system](/benchmarks/hyperbolic-relaxation-system.md)), with
a Fourier–Galerkin discretization keeping wavenumbers $\lvert k\rvert\le N$ (page-local
$N$), and share four hypotheses:

1. **A parabolic-type step restriction** $h\le c_{\mathrm{CFL}}/N^2$, from the inverse
   inequality $\lVert\partial_x\phi\rVert\le N\lVert\phi\rVert$ used to absorb the
   explicit convection term in the energy estimate (Hu & Shu 2025, Thm. 3.4, Eq. (2.16);
   Ma et al. 2026, Thm. 3.1, ineq. (3.2)).
2. **Prepared data.** Hu & Shu call data "consistent up to order $q$" (page-local $q$, a
   data index, not the stage order) when they lie in $H^q$ and the scheme starts after the
   initial layer, of length $q\,\varepsilon\log(1/\varepsilon)$ (§4 before Thm. 4.3). Ma et al. admit either
   well-prepared data (time derivatives bounded uniformly in $\varepsilon$, "Type 1") or a
   start after a layer of length $O(\varepsilon\log(1/\varepsilon))$ ("Type 2") (§3.2).
3. **Uniform regularity of the exact solution** after the layer: time and space
   derivatives bounded uniformly in $\varepsilon$, the relaxing component of size
   $O(\varepsilon)$ (Hu & Shu 2025, Lemma 2.1, cited; Ma et al. 2026, Thm. 3.2, proved
   for every structurally stable system).
4. **An energy estimate with a multiplier.** The scheme is tested against a combination
   of stage or step values chosen so that the stiff term gives a nonnegative, coercive
   quadratic form; the error equation is then estimated the same way.

Error bounds are stated for squared norms, so $C(h^4+N^{-8})$ means second order in $h$
(Hu & Shu 2025, Eq. (4.3)).

## IMEX Runge–Kutta (Hu & Shu 2025)

The system is $\partial_tu+\partial_x(\kappa u+w)=0$,
$\partial_tw+\partial_x((1-\kappa^2)u-\kappa w)=-\frac1\varepsilon w$, with
$\lvert\kappa\rvert<1$ (page-local; their $b$), convection explicit and relaxation implicit,
integrated by a pair with explicit tableau $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$
and lower-triangular implicit tableau $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$
(§2, Eqs. (2.6)–(2.11)). The hypotheses on the pair are:

- **type CK**: $A^{\mathrm I}=\begin{pmatrix}0&0\\ \hat a&\hat A\end{pmatrix}$ with $\hat A$
  invertible ($\hat a\in\mathbb R^{s-1}$, $\hat A$ page-local); type ARS is the case
  $\hat a=0$, $b^{\mathrm I}_1=0$ (Eq. (2.9));
- **implicitly stiffly accurate (ISA)**: $a^{\mathrm I}_{sj}=b^{\mathrm I}_j$; *globally*
  stiffly accurate (GSA) adds $a^{\mathrm E}_{sj}=b^{\mathrm E}_j$ (footnote 1);
- **condition (A)**: the null vector of $A^{\mathrm I}$ has zero last component,
  equivalently $\hat e^\top\hat A^{-1}\hat a=0$ with $\hat e$ the last unit vector of
  $\mathbb R^{s-1}$ (page-local); automatic for type ARS (§4, Remark 4.2). As
  $\varepsilon\to0$ it projects the last stage onto equilibrium. For a stiffly accurate
  type-CK tableau this is the same expression as the condition $R_\infty=0$ that
  Boscarino–Russo impose for L-stability, as quoted by
  [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) (Eq. (68))
  *(compiler observation, not in the sources)*.

**Theorem (uniform stability, Thm. 3.4).** For a type-CK, ISA pair admitting an
$s\times s$ multiplier matrix $\Pi$ (page-local; zero first column) such that
$\Pi A^{\mathrm I}+(\Pi A^{\mathrm I})^\top$ and $\Pi_*+\Pi_*^\top$ are positive
semidefinite of rank $s-1$ (conditions (M1)–(M2); $\Pi_*$ a fixed shift of $\Pi$, Eq.
(3.3)), and $h\le\min(c_{\mathrm{CFL}}/N^2,c)$, the fully discrete solution satisfies
$(1-\kappa^2)\lVert U^n\rVert^2+\lVert W^n\rVert^2\le C\big((1-\kappa^2)\lVert u_{\mathrm{in}}\rVert^2+\lVert w_{\mathrm{in}}\rVert^2\big)$
for $nh\le T$, with $c,C$ independent of $\varepsilon$, $N$, $h$ (Eq. (3.7)). The method
is the [energy method](/methods/runge-kutta-energy-method.md) with the stage equations
multiplied by $\Pi$; Proposition 7.1 shows that each condition forces one zero eigenvalue,
so both can be checked numerically by eigenvalues.

**Theorem (uniform second order, Thm. 4.3).** Add the second-order conditions,
$c^{\mathrm E}=c^{\mathrm I}$, condition (A) and data consistent to order 6: then
$(1-\kappa^2)\lVert U^n_e\rVert^2+\lVert W^n_e\rVert^2\le C(h^4+N^{-8})$ uniformly in
$\varepsilon$.

**Theorem (uniform third order, Thm. 5.1).** Add the third-order conditions, the stage
conditions
$\frac12c_i^2=\sum_ja^{\mathrm E}_{ij}c_j=\sum_ja^{\mathrm I}_{ij}c_j$ for $i=3,\dots,s$
(stage order 2 on every stage but the second; Eq. (5.1)), the **vanishing coefficient
condition** $b^{\mathrm E}_2=0$, $a^{\mathrm I}_{i2}=0$ for $i\ge3$ (Eq. (5.2)), and data
consistent to order 8: the bound becomes $C(h^6+N^{-12})$.

**Why Runge–Kutta is harder.** For IMEX-BDF the order equals the stage order and uniform
accuracy follows from uniform stability; a second-order IMEX-RK pair may have stages of
[stage order](/definitions/stage-order.md) 1 (Remark 4.4). The stage truncation errors are
$O(h^2)$ and the step error $O(h^3)$ uniformly in $\varepsilon$ (Lemma 4.5), but a naive
estimate gives only $C(h^4+h^2\theta^2/(1+\theta)^2)$ with $\theta=h/\varepsilon$
(page-local), i.e. first order in the intermediate regime (Eq. (4.40), Remark 4.8). The
proof absorbs the stage errors into auxiliary error vectors (once for order 2, twice for
order 3), which leaves one stiff residual; componentwise bounds
$(I+\theta A^{\mathrm I})^{-1}=O(1)$, $A^{\mathrm I}(I+\theta A^{\mathrm I})^{-1}=O(1/(1+\theta))$
and, under (A), $O(1/(1+\theta)^2)$ in the last row (Lemma 4.6), plus the coercive term from
(M1), close a bootstrap argument (Eqs. (4.41)–(4.49)). The vanishing coefficient condition
makes the low-order second stage drop out of the stiff residual (Lemma 5.3).

**Which schemes qualify** (§3–§5, App. 7.2). ARS(2,2,2), ARS(4,4,3) and BHR(5,5,3)* satisfy
Thm. 4.3 (exact $\Pi$ for the ARS schemes, a numerically verified $\Pi$ with second-smallest
eigenvalue above 0.01 for BHR(5,5,3)*). Only BHR(5,5,3)* satisfies Thm. 5.1; ARS(4,4,3) does
not, which the authors say answers "rigorously" why it is only uniformly second order (§1,
§6). It fails both the stage conditions (5.1), e.g. $\sum_ja^{\mathrm I}_{3j}c_j=\frac5{12}\ne\frac29=\frac12c_3^2$,
and the vanishing coefficient condition, $b^{\mathrm E}_2=\frac74$, $a^{\mathrm I}_{32}=\frac16$
*(compiler check on the tableau of App. 7.2)*. BHR(5,5,3)* is the Boscarino–Russo scheme
BHR(5,5,3) with $c_4=1.5$ instead of $c_4\approx2.3402$: for the original the authors could
not find a $\Pi$ (Remark 7.2). It is type CK, ISA, not GSA, with
$\gamma\approx0.435866521508460$ and $c=(0,2\gamma,2\gamma,1.5,1)$; the full tableau is
printed in App. 7.2.

**Numerical evidence** (§6, Fig. 1): $\kappa=0.6$, $N=40$, $\varepsilon$ from 1 to
$10^{-7}$, $h=\frac{8}{N^2}2^{-k}$, $k=1,\dots,5$, $T=2$, data evolved exactly through the
initial layer. The maximum over $\varepsilon$ of the error decays with slope 2 for
ARS(2,2,2), 3 for BHR(5,5,3)*, and 2 for ARS(4,4,3), whose error peaks near
$\varepsilon\approx10^{-4}$–$10^{-3}$ and is third order at both ends; see
[order reduction](/definitions/order-reduction.md).

**AP without GSA.** Appendix 7.3 (Def. 7.3, Thm. 7.4) shows formally, for the nonlinear
system with equilibrium flux $F(u)$ (page-local; Hu & Shu write $f$) and initial data in
equilibrium to $O(\varepsilon)$, that a type-CK ISA pair is AP in the strong sense
(the limit scheme keeps order $p$; "asymptotically accurate") if it is GSA (recalled from
Dimarco–Pareschi; ARS(2,2,2) and ARS(4,4,3) qualify), or, new, if it satisfies (A) together with
$\sum_j(b^{\mathrm E}_j-a^{\mathrm E}_{sj})=0$ (order 2) and
$\sum_j(b^{\mathrm E}_j-a^{\mathrm E}_{sj})c^{\mathrm E}_j=0$ (order 3). BHR(5,5,3)* is in
the second class.

## IMEX-BDF (Ma et al. 2026)

Ma et al. treat $U_t+\mathcal AU_x=\frac1\varepsilon\mathcal QU$ (page-local constant
matrices) under Yong's **structural stability condition**: $\mathcal Q$ similar to
$\mathrm{diag}(0,\hat S)$ with $\hat S$ invertible, a symmetrizer $\mathcal A_0$ with
$\mathcal A_0\mathcal A$ symmetric, and a dissipative coupling inequality, plus the extra
assumption that $\mathcal A_{02}\hat S$ is symmetric (§2.1). The scheme is the $k$-step
IMEX-BDF method with the convection term extrapolated explicitly and the relaxation
implicit at the new level,
$\sum_{j=0}^k\alpha_jU^{n+j}+h\sum_{j=0}^{k-1}\gamma_j\mathcal AU^{n+j}_x=\beta\frac h\varepsilon\mathcal QU^{n+k}$
(Eq. (2.2); page-local $\gamma_j$, $\beta$; see
[IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md)).

**Theorems 3.1, 3.3 and Corollary 3.1.** For $k=1,2,3,4$, periodic boundaries and
$h\le c_{\mathrm{CFL}}/N^2$, the scheme is uniformly stable,
$\lVert U^n_N\rVert^2\le C\sum_{i<k}\big(\lVert U^i_N\rVert^2+\frac h\varepsilon\lVert W^i_N\rVert^2\big)$
($W$ the relaxing components), and uniformly accurate,
$\lVert U(t_n)-U^n_N\rVert^2\le C(h^{2k}+e_{\mathrm{init}})$, with $C$ independent of
$\varepsilon$, $N$, $h$. If the solution is smooth enough at the start time,
$\lVert U(t_n)-U^n_N\rVert^2\le C(h^{2k}+N^{-4k})$. The proof uses the
[Nevanlinna–Odeh multipliers](/methods/multiplier-energy-technique.md) of the BDF pair
(Lemma 2.1, recalled from Akrivis–Katsoprinakis and Hu & Shu 2021): testing with
$U^{n+k}-\sum_j\mu_jU^{n+k-j}$ telescopes a positive-definite
[G-norm](/properties/g-stability.md) and turns the implicit relaxation into a nonnegative
telescoping form in $W$. The limit $k\le4$ is the availability of these multiplier
identities. The local truncation error is $O(h^{k+1})$ uniformly in $\varepsilon$ because
the stiff term is evaluated at $t_{n+k}$ with the weight $\beta$ that matches the BDF
derivative approximation, so its contribution cancels exactly (Lemma 3.1).

**Numerical evidence** (§4, Tables 4.1–4.3): $N=100$, $k=2,3,4$, $\varepsilon=10^{-7},\dots,1$
on the linearized Aw–Rascle–Zhang traffic model, the linearized
[Broadwell model](/benchmarks/broadwell-model.md) and a linearized Grad moment system:
observed orders 2.00–2.07, 2.99–3.02 and 3.76–4.00 in every regime, with slight dips
(1.89–2.02, 2.90–2.95) at $\varepsilon=10^{-3}$ on the traffic model. For $k=3,4$ the data
carry $O(\varepsilon)$ and $O(\varepsilon^2)$ corrections; starting values come from
ARS(2,2,2) or ARS(4,4,3) at step $h/500$.

## Qualifications

- **Scope.** Both results are for linear, constant-coefficient, periodic one-dimensional
  problems with a spectral space discretization. The nonlinear AP statements of Hu & Shu
  (App. 7.3) are formal.
- **Step restriction.** The restriction $h\le c_{\mathrm{CFL}}/N^2$ is an artifact of the
  energy proof, a parabolic scaling for a hyperbolic problem, not a sharp condition: the
  tests of Ma et al. run with $hN^2$ up to 50 and $c_{\mathrm{CFL}}$ is never specified.
  Neither paper proves uniform stability under the convective CFL condition $h=O(1/N)$
  that IMEX schemes are expected to satisfy.
- **Sufficient, not necessary.** Thm. 5.1 does not cover BHR(5,5,3) as published, which
  Boscarino and Russo observed to be uniformly third order numerically; the failure is of
  the multiplier construction, not a counterexample (Hu & Shu 2025, Remark 7.2).
- **"IMEX-RK degrade as $\varepsilon\to0$."** Ma et al. (2026, §1) write that "many IMEX-RK
  schemes suffer from accuracy degeneration when $\varepsilon$ goes to zero", as motivation
  for IMEX-BDF. Hu & Shu (2025, Thms. 4.3, 5.1) prove uniform second and third order for a
  class of IMEX-RK pairs on the same problem class, and their ARS(4,4,3) data show the loss
  in the intermediate regime, not as $\varepsilon\to0$. The two statements are compatible
  (Ma et al. say "many", not "all", and cite the Hu & Shu preprint for IMEX-RK); the claim
  is recorded as an imprecise generalization, not as a contradiction.
- **Extra hypothesis.** Theorem 3.1 of Ma et al. is stated "under the structural stability
  condition"; the symmetry of $\mathcal A_{02}\hat S$ is assumed in the preamble and is
  needed.
- **Hidden hypothesis in Lemma 4.6 of Hu & Shu.** The Neumann-series argument divides by
  $1+\theta a^{\mathrm I}_{ii}$, which needs $a^{\mathrm I}_{ii}>0$ for $i\ge2$; type CK only
  requires $\hat A$ invertible. All schemes considered satisfy it.
- **Printed slips.** In Ma et al., Table 4.2 (Broadwell, second order) prints the
  $h=2.5\times10^{-3}$ errors with exponent $10^{-5}$ where the neighbouring entries and the
  printed orders require $10^{-4}$; the second truncation bound in the proof of Lemma 3.1
  lacks a factor $h$ on $\sum_j\gamma_j\partial_xu^{n+j}$. Neither affects the results.
  Hu & Shu measure the error in $(u,v)$ while the theorems bound $(u,w)$; the norms are
  equivalent.

# Citations

- [Hu & Shu (2025)](/sources/hu-2025.md) — §1; §2 (Eqs. (2.6)–(2.11), Lemma 2.1); §3 (Eq. (3.3), Thm. 3.4, Remark 3.3); §4 (Thm. 4.3, Remarks 4.2, 4.4, 4.8, Lemmas 4.5–4.6, Eqs. (4.40)–(4.49)); §5 (Thm. 5.1, Lemma 5.3); §6 (Fig. 1); §7.1–7.3 (Prop. 7.1, Remark 7.2, Def. 7.3, Thm. 7.4); arXiv v1.
- [Ma et al. (2026)](/sources/ma-2026.md) — §1; §2.1–2.2 (Eq. (2.2), Lemma 2.1); §3 (Thms. 3.1–3.3, Lemma 3.1, Cor. 3.1); §4 (Tables 4.1–4.3); arXiv v1.
- [Jin (2022)](/sources/jin-2022.md) — §1 (eqs. (1.1)–(1.6)); §6.1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3.1, Eq. (68) (the $R_\infty=0$ condition, for comparison with condition (A)); HAL v2.
