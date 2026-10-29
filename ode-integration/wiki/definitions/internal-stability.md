---
type: Definition
title: "Internal stability of explicit Runge–Kutta methods"
description: "Internal stability is the stability of perturbations introduced at the stages, by round-off or inexact evaluations, as they propagate through the remaining stages of one step; measured by internal stability polynomials and an amplification factor, it depends on the realization and limits many-stage and low-precision methods; for DIRK-type stages it is a stage-wise stability function at the stiff limit."
status: established
aliases: [internal stability polynomials, internal amplification factor, maximum internal amplification factor, round-off propagation within a step, stage-wise stability]
tags: [stability, explicit, runge-kutta, round-off]
timestamp: 2026-10-29T18:13:00Z
---

# Internal stability of explicit Runge–Kutta methods

A Runge–Kutta step is computed stage by stage, and every stage carries an error of
its own: round-off, a low-precision evaluation, an inexact solve. **Internal
stability** is the property that such stage perturbations are not amplified as they
propagate through the later stages of the same step, the notion of van der Houwen and
Sommeijer recalled by [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) (§3,
Lemma 3.1) and by [Doehring et al. (2024)](/sources/doehring-2024.md) (§9.1). The
[stability function](/definitions/stability-function.md) $R(z)$ describes only the
unperturbed map $y_n\mapsto y_{n+1}$; two realizations of the same $R$ can differ by
many orders of magnitude in internal stability. The issue is negligible for methods
with a few stages and becomes the limiting factor for stabilized and stability-optimized
methods with tens or hundreds of stages, and for methods run in reduced precision.

## Perturbed stages and internal stability polynomials

Perturb each stage and the update by $e_i$ (page-local):

$$\tilde Y_i=\tilde y_n+h\sum_ja_{ij}f(\tilde Y_j)+e_i,\qquad \tilde y_{n+1}=\tilde y_n+h\sum_ib_if(\tilde Y_i)+e_{s+1}.$$

For a linear problem $y'=\lambda y$, with $z=h\lambda$, as recalled from Ketcheson,
Lóczi & Parsani by [Doehring et al. (2025)](/sources/doehring-2025.md) (§4.4, Eqs.
(4.11)–(4.13)),

$$\lVert\tilde y_{n+1}-y(t_{n+1})\rVert\le\lVert\tilde y_n-y(t_n)\rVert+\sum_{i=1}^{s+1}\lvert Q_i(z)\rvert\,\lVert e_i\rVert+\mathcal O(h^{p+1}),\qquad Q(z)=z\,b^\top(I-zA)^{-1},$$

with $Q_i$ the **internal stability polynomials** (page-local symbol; $Q_{s+1}=1$ for
the update). For explicit methods $e_1=0$, since the first stage is $\tilde y_n$
itself. In modified Shu–Osher form
$Y_k=v_ky_n+\sum_{l<k}(\alpha_{kl}Y_l+h\beta_{kl}f(Y_l))$, $k=1,\dots,s+1$,
$y_{n+1}=Y_{s+1}$, the same polynomials are
$Q(z)=(\alpha_{s+1}+z\beta_{s+1})(I-\alpha-z\beta)^{-1}$ with $\alpha$, $\beta$ the
first $s$ rows and $\alpha_{s+1}$, $\beta_{s+1}$ the last (Doehring et al. 2024,
§9.1, Eqs. (9.9)–(9.11)).

For three-term recurrence methods the analogous objects are the stage polynomials of
the recurrence. In Runge–Kutta–Chebyshev methods the stage $j$ has stability
polynomial $P_j(z)=\mathsf a_j+\mathsf b_jT_j(\omega_0+\omega_1z)$ (page-local: $T_j$ the
Chebyshev polynomial of the first kind, $\mathsf a_j$, $\mathsf b_j$, $\omega_0$, $\omega_1$ the
RKC constants of the stabilized-methods page; Croci & Rosilho de Souza 2022, Lemma 3.1);
in the monotonic RKC method of [Faleichik & Moisa (2026)](/sources/faleichik-2026.md)
every stage polynomial satisfies $0\le\tilde P_j(z)<1$ for real $z$ in the whole
monotonicity interval, which the authors name
as the method's internal stability (§2, Eq. (13)). See
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md).
The vector $(I-zA)^{-1}\mathbf 1$ that gives the stage values of the linear test
problem, called the internal stability function in multirate analysis, is a related
but different object ([Roberts et al. 2021](/sources/roberts-2021.md), §3.4).

## Internal stability of diagonally implicit stages

For implicit methods the word names a stage-wise stability function at the stiff limit.
[Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) (§3.1.2, Eq. (30), after Verwer)
define for a DIRK-type implicit tableau the **internal stability function of stage $n$**,

$$R^{(n)}_{\mathrm{int}}(z)=\frac{\det\bigl(I-zA_{[n]}+z\mathbf 1a_{[n]}^\top\bigr)}{\det\bigl(I-zA_{[n]}\bigr)},$$

with $A_{[n]}$ the leading $n\times n$ block of $A$ and $a_{[n]}=(a_{n1},\dots,a_{nn})^\top$ its
$n$-th row (page-local symbols; the paper writes calligraphic $\mathcal A$, $\mathcal B$),
i.e. the stability function of the $n$-stage method whose weights are row $n$ of $A$. On
$y'=\lambda y$ it is the factor $Y_n=R^{(n)}_{\mathrm{int}}(z)y_n$, the $n$-th component of
the vector $(I-zA)^{-1}\mathbf 1$ above *(compiler check, not in the sources: for lower-triangular
$A$, $Y_n=\bigl(1+za_{[n]}^\top(I-zA_{[n]})^{-1}\mathbf 1\bigr)y_n$, and this factor equals the
determinant ratio)*. The quantity of concern is $R^{(n)}_{\mathrm{int}}(-\infty)$, the
amplification of stage $n$ for infinitely stiff components:

- SDIRKs have $R^{(n)}_{\mathrm{int}}(-\infty)=0$ at every stage; ESDIRKs, with $a_{11}=0$,
  generally do not (§3.1.2). Pairs with a zero-padded implicit tableau (Ascher et al., Calvo
  et al.) have $R^{(n)}_{\mathrm{int}}(-\infty)=0$ at every stage, at the price of stage order 1
  because $a_{21}\neq a_{22}$ (§8.1).
- The ESDIRKs of the [Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md)
  have values of modulus at most 1 (e.g. $+1,-1,-0.806$ for ARK3(2)4L[2]SA), while
  Griepentrog's three- and four-stage methods reach $-2.464$ at stage 3 and $-4.909$ at
  stage 4 (Tables 10, 12).
- Griepentrog's methods break on a stiff reacting-shock problem with nonequilibrium initial
  data (largest stable Courant number 0.37 and 0.44 at $\varepsilon=10^0$, 0.0 at
  $\varepsilon=10^{-8}$, Table 9). Kennedy & Carpenter point to the final-stage values of
  Table 10 and write: "If internal stability of the implicit method is a principal contributor
  to the breakdown of these methods, it is not surprising that the zero padded A matrices found
  in the methods of Ascher et al. and Calvo et al. do not leak stiffness badly" (§8.1); see [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md).
- A zero first column of the implicit tableau means that the initial value of an algebraic
  variable is not propagated through the stages, which helps on Kreiss's problem (§3.1.2).

## Amplification factor and the round-off test

Doehring et al. measure internal stability by a variant of Ketcheson–Lóczi–Parsani's
maximum internal amplification factor,

$$\widetilde{\mathcal M}=\max_{z}\sum_{i\ge2}\lvert Q_i(z)\rvert$$

(page-local), the maximum taken over the region of absolute stability (Doehring et
al. 2024, Eq. (9.12)) or over the scaled eigenvalues of the semi-discretization
(Doehring et al. 2025, Eq. (4.14)). In double precision the round-off contribution
per step is about $\widetilde{\mathcal M}\cdot10^{-15}$; internal stability limits the
step when this is comparable with the truncation error $h^{p+1}$ (Doehring et al.
2024, §9.1). Their tests on DG semi-discretizations:

- third-order methods with 26, 52 and 104 stages on 1D advection run at the full
  scaled step with $\widetilde{\mathcal M}\cdot10^{-15}=3.6\times10^{-12}$,
  $1.5\times10^{-9}$, $5.4\times10^{-5}$, below $h^4=1.1\times10^{-5}$,
  $1.7\times10^{-4}$, $2.8\times10^{-3}$ (§10.1.1, Table 3);
- on 2D linearized Euler a 128-stage second-order method is unstable at the full
  step, with $\widetilde{\mathcal M}\cdot10^{-15}\approx7.6\times10^{-2}$ above
  $h^3$, and needs CFL 0.81; the authors attribute this to internal stability
  (§10.1.2, Table 4);
- for the fourth-order [P-ERK](/methods/paired-explicit-runge-kutta.md) members
  $\widetilde{\mathcal M}$ grows exponentially with the number $e$ of active stages
  (page-local), between the reference slopes $\mathcal O(2^e)$ and $\mathcal O(\exp e)$ for
  $e=5,\dots,18$ (Doehring et al. 2025, §4.4, Fig. 3).

"Internal stability … seems to be the major difficulty in realizing the maximum
timestep" of many-stage methods (Doehring et al. 2024, §9).

## The realization decides

Internal stability is reduced without changing $R(z)$ by choosing the tableau or
the order of the factors:

- **Ordering and grouping of factors.** Doehring et al. (2024, §9.2–9.3, Table 2)
  write a degree-104 polynomial as a product of forward Euler steps and two-stage
  submethods. Minimizing $\lVert\beta\rVert_1$ of each submethod, allowing negative
  $\beta$, and grouping the near-imaginary roots of $(P-1)/z$ with those of largest
  real-part magnitude (a generalized Lebedev idea) lowers $\widetilde{\mathcal M}$
  from $2.39\times10^{22}$ (no grouping, $\beta\ge0$) to $1.63\times10^{9}$ (grouping,
  $\beta\in\mathbb R$). Full minimization over all coefficients is judged infeasible.
- **Free abscissae.** In fourth-order P-ERK the stability polynomial does not depend
  on the free abscissa $c_{s-3}$; with 18 active stages, linearly increasing $c_i$
  give $\widetilde{\mathcal M}=1.36\times10^6$ and a usable CFL of 0.87, constant
  $c_i=1$ give $5.35\times10^5$ and 0.90 (Doehring et al. 2025, §4.4, Table 1). The
  constant choice puts the largest weight on the least-perturbed first stage.
- **Delta form.** Croci & Rosilho de Souza (2022, §2.2) write RKC in increment form
  because it accumulates smaller rounding errors.

## Internal stability in reduced precision

When most stages are evaluated in low precision with unit roundoff $u$ (page-local),
the stage perturbations are of size $u$ rather than $10^{-16}$, and internal stability
decides whether the method is usable. Croci & Rosilho de Souza (2022) prove for
mixed-precision RKC, under an internal-stability assumption on the computed
increments (Assumption 3.2) and a symmetric nonpositive definite Jacobian, one-step
error recursions whose constants depend neither on $s$ nor on the stiffness
(Thms. 3.4–3.5). Their worst-case bound for the rounding errors themselves (Thm. 3.6,
Eqs. (71)–(81)) contains a factor $2(1+Chu)^{s-1}\le2\exp(2\bar Cs^2u)$
(page-local constants $C$, which grows with the spectral radius, and $\bar C$) and
guarantees boundedness only for $s^2u=\mathcal O(1)$, about $s\lesssim16$ in
bfloat16. In their experiments the methods stay stable up to $s=512$, "more robust than
our theory predicts" (§5.2.3). They contrast this with the earlier rounding analysis of
Verwer et al., which assumed independent stage perturbations and found a stability
constant $1+Cs^2u$ independent of $h$, against $1+Cs^2uh$ for their order-preserving
scheme (§3.6). See
[mixed-precision Runge–Kutta methods](/methods/mixed-precision-runge-kutta.md).

## Stage values on low-dissipation semi-discretizations

[Kemm (2024)](/sources/kemm-2024.md) raises a different, informal stage-stability
argument. For low-Mach finite-volume schemes the semi-discrete spectrum reaches the
imaginary axis and forward Euler is unstable. Every explicit Runge–Kutta step begins with
a forward-Euler substep (the second stage, $Y_2=y_n+ha_{21}f(y_n)$, in this bundle's
indexing), and Kemm argues that this "unstable first stage value" spoils the step on
nonlinear (limited) problems even when the stability polynomial covers the spectrum,
whereas Adams–Bashforth methods, which have no internal stages, are not affected (§1,
§3.1, §5). His evidence is numerical: on a perturbed uniform flow at Mach $1/20$ with a
second-order limited scheme, Heun's RK3 shows no improvement over RK2 while AB3 keeps the
perturbation from growing (Fig. 4); with first order in space, i.e. without the limiter,
RK3 behaves as linear theory predicts (Fig. 5); on Richtmyer–Meshkov flow RK3 shows
instabilities in the extremely-low-Mach region where AB3 does not (Fig. 12). He proposes
that future general linear and predictor–corrector methods be designed with stable stage
values (§5).

The argument is not the internal-stability measure of this page: no internal stability
polynomials or amplification factors are computed, and the sources above find internal
amplification negligible for methods with few stages, so the mechanism Kemm proposes for
three-stage methods remains a hypothesis of that source *(compiler remark, not in the sources)*. See also
[linear multistep methods](/methods/linear-multistep-method.md).

## Qualifications

- **Definitions differ.** Doehring et al. (2024) take the maximum of
  $\widetilde{\mathcal M}$ over the stability region and sum over $i=2,\dots,s+1$,
  including the perturbation of the update; Doehring et al. (2025) take it over the
  scaled spectrum and sum over $i=2,\dots,s$; both start at $i=2$ and both call it a variant of the factor of
  Ketcheson, Lóczi & Parsani, whose original definition is not given in the sources.
- **Attribution of step limits.** Doehring et al. (2024, §10.2) attribute the step
  reductions on nonlinear problems (CFL 0.28–0.79) to the zero SSP coefficient of
  their methods, not to internal stability, because there
  $\widetilde{\mathcal M}\cdot10^{-15}$ lies orders of magnitude below $h^3$; the
  evidence is indirect (comparison with an SSP method of a different family and
  total-variation growth).
- **Printed slips.** Doehring et al. (2024, p. 24) print $h^3\approx9.29\times10^{-4}$
  for the 128-stage case where their own data give $9.3\times10^{-5}$; the conclusion
  (round-off above truncation) holds either way. Their Eq. (9.10) mixes the summation
  index.
- Stability-optimized many-stage methods of earlier work were published without an
  internal-stability analysis ([Hedayati Nasab et al. 2021](/sources/hedayatinasab-2021.md),
  as noted on [optimal stability polynomials](/methods/optimal-stability-polynomial.md)).

# Citations

- [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) — §2.2, §3 (Lemma 3.1, Assumption 3.2, Thms. 3.4–3.6, Eqs. 71–81), §3.6, §5.2.3.
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §9, §9.1–9.3 (Eqs. 9.9–9.12, Table 2), §10.1.1–10.1.2 (Tables 3–4), §10.2.
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §4.4 (Eqs. 4.11–4.14, Fig. 3, Table 1).
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §2 (Eq. 13, internal stability by construction).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §3.4 (stage-value internal stability function, contrast).
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — internal stability not analysed for 16-stage methods.
- [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) — NASA/TM-2001-211038: §3.1.2 (Eq. (30)), §8.1 (Tables 9–10, 12).
- [Kemm (2024)](/sources/kemm-2024.md) — §1, §3.1, §4.1, §4.4, §5, Figs. 4–5, 12 ("unstable first stage value" thesis).
