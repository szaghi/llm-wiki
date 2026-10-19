---
type: Method
title: "Embedded Runge–Kutta pairs and the FSAL property"
description: "An embedded pair adds a second weight vector to a Runge–Kutta tableau so that the difference of two solutions of orders p and p-hat estimates the local error at no extra stage cost; FSAL, design criteria, SSP and low-storage pairs, Rosenbrock pairs."
status: established
aliases: [embedded pair, embedded method, Runge–Kutta pair, p(p-hat) pair, FSAL, first same as last, local extrapolation]
tags: [runge-kutta, step-size-control, explicit, ssp, embedded-pair]
timestamp: 2026-10-19T12:00:00Z
---

# Embedded Runge–Kutta pairs and the FSAL property

An **embedded pair** is an $s$-stage [Runge–Kutta method](/definitions/runge-kutta-method.md)
$(A,b,c)$ together with a second weight vector $\hat b$ that reuses the same stage
values $Y_i$:

$$\begin{aligned}
y_{n+1}&=y_n+h\sum_{i=1}^s b_if(t_n+c_ih,Y_i),\\
\hat y_{n+1}&=y_n+h\sum_{i=1}^s \hat b_if(t_n+c_ih,Y_i)\;\bigl[+\,h\,\hat b_{s+1}f(t_{n+1},y_{n+1})\bigr].
\end{aligned}$$

The main method has order $p$, the embedded method order $\hat p$, usually $\hat p=p-1$, and
the pair is written $p(\hat p)$. The difference $y_{n+1}-\hat y_{n+1}$ estimates the local
error and drives [step-size control](/methods/step-size-control.md); because $A$ is shared,
the estimate costs no additional stage (Fekete et al. 2022, §1–2; Ranocha et al. 2022, §2,
Eqs. (2.2)–(2.4); Reynolds et al. 2023, §2.1, Eq. (4)). The bracketed term is present only in a
**FSAL** pair (below).

## Local extrapolation

When the solution is advanced with the higher-order $y_{n+1}$ and $\hat y_{n+1}$ serves only
as the estimator, the pair is used in **local extrapolation** mode. The new pairs of
[Fekete et al. (2022)](/sources/fekete-2022.md) (§1, read as the 2018 arXiv preprint by
Conde, Fekete and Shadid) and of [Ranocha et al. (2022)](/sources/ranocha-2022.md) (§2) all
assume it, and [Reynolds et al. (2023)](/sources/reynolds-2023.md) describe the
[ARKODE](/software/arkode.md) tables the same way, with embeddings "usually of order
$p-1$" (§2.1). Several classical pairs advance the *lower* order instead: Fekete et al.
list RKF23, Fehlberg12, Ceschino24 (second order advanced, fourth-order estimator) and
Fehlberg45 (fourth order advanced, fifth-order estimator) among their baselines (§3.1).

The estimate is the local error of the embedded method, not of the advanced solution:
$y_{n+1}-\hat y_{n+1}=O(h^{\hat p+1})$, which is why controller exponents use
$\hat p+1$ (or $\min(p,\hat p)+1$; see [step-size control](/methods/step-size-control.md)).

## FSAL (first same as last)

In a FSAL pair the embedded solution also uses the derivative at the new point,
$\hat b_{s+1}f(t_{n+1},y_{n+1})$. If the step is accepted, that evaluation is the first stage
of the next step, so the estimator is free; only after a rejection is it wasted
(Ranocha et al. 2022, §2, Eq. (2.3)). Equivalently, the pair is an $(s+1)$-stage method with
$\tilde A=\begin{pmatrix}A&0\\ b^\top&0\end{pmatrix}$ and $\tilde c=(c;1)$ (their Remark 2.1).
Naming conventions follow this accounting: in the Kennedy–Carpenter–Lewis convention adopted by
Ranocha et al., NAME$p(\hat p)s$F counts $s$ as the **effective** number of right-hand-side
evaluations per step, one less than the stage count for FSAL (Remark 3.1); BS3(2)3F, the
Bogacki–Shampine pair, has four stages. Fekete et al., by contrast, count Bogacki–Shampine 3(2)
as four stages and do not exploit FSAL in their work measure (§3.1), which penalizes that
baseline in their comparisons.

Ranocha et al. find FSAL pairs "often more efficient" than non-FSAL ones, especially at loose
tolerances, and recommend their new FSAL low-storage pairs for stability-limited hyperbolic
problems (§6.2).

## Design criteria for the embedded weights

The sources agree that a usable embedding needs more than order $\hat p$:

- **Non-defectiveness.** Fekete et al. require the embedded method to violate *every*
  order-$p$ condition; a defective embedding has vanishing order-$p$ error coefficients, so the
  Kennedy–Carpenter–Lewis ratio $C^{(p+1)}$ diverges and the estimate is meaningless
  (§2, property (ii), Remark 2).
- **Error measures.** Both Fekete et al. (§2) and Ranocha et al. (Suppl. Table 1) score pairs
  with the Kennedy–Carpenter–Lewis quantities: the principal error norm of the embedded method,
  the ratios $B$ and $C$ (targets near 1), and the largest coefficient $D$.
- **Stability of the estimator.** Ranocha et al. design embedded methods whose stability region
  *contains* that of the main method, as for BS3(2)3F; they attribute the poor showing of the
  Kennedy–Carpenter–Lewis 2R pairs partly to embedded regions smaller than the main one in
  places (§5.5.4, Fig. 5). Fekete et al. likewise favour embeddings with large stability regions
  (e.g. $\hat b=\tfrac14\mathbf 1$ for SSPRK(4,3), "significantly larger stability region",
  §2.2).
- **Step-size-control stability.** The pair and its controller form a dynamical system; Ranocha
  et al. impose step-size-control stability along the boundary of the main method's stability
  region as an a priori design constraint (§4, §6; see
  [step-size control](/methods/step-size-control.md)).
- **Moderate coefficients and rational values** when possible (Fekete et al. §2, property (iii);
  Ranocha et al. §6).

## Embedded pairs for SSP methods

Optimal [SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md) are
usually run at a fixed CFL-limited step. Fekete et al. (2022) construct embedded weights for
them, asking that the embedded method keep the SSP coefficient $\mathcal C$ of the main method
when possible. Since a positive SSP coefficient forces nonnegative weights, any SSP embedding
satisfies $0\le\hat b\le\mathbf 1$ componentwise (§2, after Eq. (11)). Their families (§2.1–2.3):

| Main method ($\mathcal C$) | Embedded weights $\hat b$ | Remarks |
|---|---|---|
| SSPRK$(s,2)$ ($s-1$) | $\bigl(\tfrac1{s-1},\dots,\tfrac1{s-1},0\bigr)$ or $\bigl(\tfrac{s+1}{s^2},\tfrac1s,\dots,\tfrac1s,\tfrac{s-1}{s^2}\bigr)$ | both first order with SSP coefficient $s-1$; the second preferred |
| SSPRK(4,3) ($2$) | $\bigl(\tfrac14,\tfrac14,\tfrac14,\tfrac14\bigr)$ | supersedes $(\tfrac13,\tfrac13,\tfrac13,0)$ |
| SSPRK$(n^2,3)$, $n\ge3$ ($n^2-n$) | $\tfrac1{n^2}\mathbf 1$ | no embedding with the full $\mathcal C$ found; positive SSP coefficient kept |
| SSPRK(10,4) ($6$) | eight rational third-order vectors | non-defective embedding impossible |

For SSPRK(10,4) non-defectiveness is impossible because one fourth-order condition,
$b^\top\bigl(\tfrac{c^3}{3!}-\tfrac{Ac^2}{2!}\bigr)=0$, holds for every weight vector given that
$A$ (§2.3). Fekete et al. recommend SSPRK(4,2) and SSPRK(6,2) with the second first-order
embedding, SSPRK(4,3) with $\tfrac14\mathbf 1$, four of the eight SSPRK(10,4) embeddings, and
their numerically optimized SSPRK(3,2) and SSPRK(3,3) pairs (§4).

The SSPRK(4,3) pair with $\hat b=\tfrac14\mathbf 1$ appears identically in Ranocha et al. (2022)
as SSP3(2)4[3S\*$_+$], with tableau $c=(0,\tfrac12,1,\tfrac12)$, $b=(\tfrac16,\tfrac16,\tfrac16,\tfrac12)$
(Appendix A, Eq. (A.1)): two sources, the same pair. It has the largest real stability
interval per stage of all methods Ranocha et al. compare (5.15, i.e. 1.29 per stage; Suppl.
Table 1) and is about 50% cheaper than BS3(2)3F at loose and medium tolerances on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (3438 versus 5256 right-hand-side
evaluations), but its cost grows sharply at tight tolerances, and its estimator "does not seem
to be reliable enough" to make tolerance choice robust (§5.5.2, Table 4).

## Optimized low-storage pairs

Ranocha et al. (2022) build FSAL and non-FSAL pairs RK3(2)5, RK4(3)9 and RK5(4)10 in the
3S\*$_+$ [low-storage](/methods/low-storage-runge-kutta.md) class, taking as main methods
stability-optimized schemes (see [optimal stability polynomials](/methods/optimal-stability-polynomial.md))
that had no estimator and designing $\hat b$ (and $\hat b_{s+1}$) for step-size-control
stability, error measures, an embedded stability region containing the main one, and moderate
coefficients (§6, Appendix B). The new third-order pairs are up to 18% cheaper than BS3(2)3F,
in line with their larger real stability interval per stage (0.99 versus 0.84); the fourth- and
fifth-order ones beat the corresponding Kennedy–Carpenter–Lewis pairs by up to 25% and 35%
(§6.2). Among general-purpose pairs, BS3(2)3F is about 50% more efficient than the fifth-order
BS5(4)7F and DP5(4)6F when the step is stability-limited (§5.5.1, Table 3).

## Pairs in software

[ARKODE](/software/arkode.md) ships explicit pairs of orders 2, 3, 4, 5, 6 and 8 (defaults
Heun–Euler, Bogacki–Shampine, Zonneveld and Cash–Karp for orders 2–5), additive IMEX pairs
of orders 3, 4, 5 with embeddings 2, 3, 4, and DIRK pairs of orders 2–5 with embeddings 1–4; a
user table without embedding disables adaptivity (Reynolds et al. 2023, §2.1–2.2). The
optimized pairs of Ranocha et al. are available in
[DifferentialEquations.jl](/software/differentialequations-jl.md) (§6).

## Embedded Rosenbrock pairs

The same mechanism serves [Rosenbrock–Wanner methods](/methods/rosenbrock-wanner-method.md).
[Steinebach (2023)](/sources/steinebach-2023.md) shows two ways an embedding can fail: for
$y'=\cos t$ the main and embedded errors of Rodas5 coincide exactly, so the controller sees a
zero estimate (§1, p. 4); and the embedded method of Rodas5 is not A-stable, which "may cause
stepsize reductions" for eigenvalues near the imaginary axis (Fig. 1). [Rodas5P](/methods/rodas5p.md)
uses a stiffly accurate, A-stable 7-stage embedded method of order 4 (§3, Fig. 2).

## Qualifications

- Fekete et al. print the SSP coefficients and error measures of their new pairs nowhere in
  the paper; they defer them to a GitHub draft (their ref. [3]), and the coefficients of their
  numerically optimized embeddings are not printed (§2).
- Fekete et al. impose SSP conditions on the embedded method, although under local
  extrapolation only the main method's SSP property bears on the strong stability of
  $y_{n+1}$; the paper does not say why the embedded SSP coefficient matters *(compiler note,
  not in the sources)*.
- Fekete et al. print the Dormand–Prince pair as using "six function evaluations" (§3.1) and as
  "seven-stage" (§3.2.2); both are consistent with a seven-stage FSAL pair counted with and
  without the reused stage *(compiler check)*.
- **Suitability of the SSP embeddings for adaptive control: a qualification, not a
  contradiction.** Fekete et al. (2022) recommend their SSPRK(10,4) and SSPRK(4,3) pairs
  for adaptive control with a PID controller, on the evidence of work–precision tests at
  tolerances $10^{-2}$–$10^{-7}$ (§3.2.2, §4); they do not examine step-size-control
  stability. Ranocha et al. (2022, §5) report that for SSP4(3)10[3S\*$_+$] (SSPRK(10,4) with
  "the embedded method of Conde et al.") step-size-control stability "could not be achieved
  with any PID controller" they tested, and therefore leave that pair out of their
  comparisons; they do not say which of the eight SSPRK(10,4) embeddings they used. For
  SSPRK(4,3) with $\hat b=\tfrac14\mathbf 1$, the same embedding, Ranocha et al. find the
  pair often the most efficient, with an error estimator that is not reliable at tight
  tolerances (§5.5.2); Fekete et al. themselves report it costing more than Bogacki–Shampine
  at tighter tolerances. The nine-stage SSP3(2)9 pair that Ranocha et al. find unstable under
  control is not one Fekete et al. recommend. The two papers therefore speak about different
  properties (efficiency on non-stiff tests versus controller stability on stability-limited
  problems), and they would conflict only if Ranocha et al.'s SSPRK(10,4) embedding is one
  Fekete et al. recommend. What would decide it: the spectral radius of the step-size-control
  Jacobian along the stability boundary for each recommended embedding with Fekete et al.'s
  PID gains. *(Recorded as an Open contradiction by the drafter; reclassified by the chunk-1
  deep lint after checking Ranocha et al. §5 on the PDF.)*

# Citations

- [Fekete et al. (2022)](/sources/fekete-2022.md) — §1–2 (Eqs. (8)–(14), Remarks 1–2), §2.1–2.3 (embedded families), §3.1 (baseline pairs, work measure), §3.2.2, §4.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2 (Eqs. (2.2)–(2.4), Remark 2.1), Remark 3.1, §4, §5.5.1–5.5.4 (Tables 3–4, Fig. 5), §6, Appendix A–B, Suppl. Table 1.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.1–2.2 (ERKStep and ARKStep tables).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Rodas5 estimator failures, Fig. 1), §3 (Rodas5P embedded method, Fig. 2).
