---
type: Method
title: "Embedded Runge–Kutta pairs and the FSAL property"
description: "An embedded pair adds a second weight vector to a Runge–Kutta tableau so that the difference of two solutions of orders p and p-hat estimates the local error at no extra stage cost; local extrapolation and higher-order embeddings, FSAL and relaxation, the affine family of all embeddings (null rules), design criteria, SSP, low-storage, paired and Rosenbrock pairs."
status: established
aliases: [embedded pair, embedded method, Runge–Kutta pair, p(p-hat) pair, FSAL, first same as last, local extrapolation, null rule, nested Runge–Kutta methods]
tags: [runge-kutta, step-size-control, explicit, ssp, embedded-pair]
timestamp: 2026-10-20T16:00:00Z
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
Eqs. (2.2)–(2.4); Reynolds et al. 2023, §2.1, Eq. (4); Ranocha et al. 2025, §2, Eq. (2.2);
Vermeire 2023, §2.1). The bracketed term is present only in a **FSAL** pair (below).

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

**Higher-order embedding in implicit pairs.** [Pan et al. (2022)](/sources/pan-2022.md)
(§2.1.2, Eqs. (10)–(15), App. A) advance the lower order on purpose: Kværnø's ESDIRK pairs
2(3), 3(4) and 4(5) are one tableau with $S+1$ stages whose row $S$ is the main method and
row $S+1$ the embedded one, $b_i=a_{Si}$, $\hat b_i=a_{S+1,i}$, both
[stiffly accurate](/properties/stiff-accuracy.md), so $y_{n+1}=Y_S$ and $\hat y_{n+1}=Y_{S+1}$.
The difference then estimates the local error of the advanced solution, $O(h^{p+1})$. The
price is one extra implicit stage, about $1/(S-1)$ of the step's implicit work ($S=3,4,6$),
which the authors judge worthwhile because the estimate is more accurate than a
lower-order one and needs no problem-dependent calibration (§2.4); the claim is not tested
against a lower-order embedding. The estimate drives their balance of temporal against
spatial error on [step-size control](/methods/step-size-control.md). The tableaux are on
[DIRK methods](/methods/diagonally-implicit-runge-kutta.md).

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
problems (§6.2). [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) attribute the FSAL
technique to Dormand and Prince (§1).

### FSAL and relaxation

A [relaxation Runge–Kutta method](/methods/relaxation-runge-kutta.md) continues from
$y^{\gamma}_{n+1}=y_n+\gamma_n(y_{n+1}-y_n)$, so the first stage of the next step is
$f(y^{\gamma}_{n+1})$, not the FSAL value $f(y_{n+1})$. Relaxing accepted steps on top of an
unchanged FSAL pair, as in OrdinaryDiffEq.jl and SUNDIALS, therefore costs one extra evaluation
per step, an efficiency loss reported earlier by Al Jahdali et al. and Rogowski et al. (as
recalled by Bleecke & Ranocha 2026, §1). Bleecke & Ranocha (2026, §2) remove it by the linear
structure of the relaxation update. Let $p$ be the order of the main method and $g$ any $C^2$
function.

- **FSAL-R** (relax after the accept/reject decision). The next first stage is approximated by
  $f(y_n)+\gamma_n\bigl(f(y_{n+1})-f(y_n)\bigr)$, a combination of values already computed
  ($y_n$ the current, already relaxed, solution). Lemma 1:
  $g(y^{\gamma}_{n+1})=g(y_n)+\gamma_n\bigl(g(y_{n+1})-g(y_n)\bigr)+O(h^{p+1})$, which follows
  from $\gamma_n=1+O(h^{p-1})$. Theorem 1: the local errors of main and embedded solution stay
  $O(h^{p+1})$ and $O(h^{p})$, because the first-stage error enters multiplied by $h$.
- **R-FSAL** (relax before the error estimate). One evaluation $f(y^{\gamma}_{n+1})$ is made and
  serves as the next first stage; the FSAL value needed by $\hat y_{n+1}$ is approximated by
  $f(y_n)+\gamma_n^{-1}\bigl(f(y^{\gamma}_{n+1})-f(y_n)\bigr)$ (Lemma 2, error $O(h^{p+1})$). The
  estimate compares $y^{\gamma}_{n+1}$ with a relaxed embedded solution
  $\hat y^{\gamma}_{n+1}=y_n+\gamma_nh\bigl(\sum_i\hat b_if(t_n+c_ih,Y_i)+\hat b_{s+1}\,[\text{approximated FSAL value}]\bigr)$,
  both read at $t_n+\gamma_nh$; Theorem 2 gives a local error $O(h^{p})$ for it.

On the [BBM equation](/benchmarks/benjamin-bona-mahony-equation.md) with BS3(2) and the
Dormand–Prince 5(4) pair, both variants match the accuracy of the naive combination at
essentially the evaluation count of the unrelaxed method, "roughly 25%" more accurate than
the baseline at equal work (§3, Fig. 1). The authors see no clear winner for conservative
problems, recommend FSAL-R for general-purpose libraries and R-FSAL for dissipative problems,
whose entropy estimates FSAL-R cannot use directly (§4).

## The family of all embeddings: null rules

For fixed $(A,c)$ the order conditions are linear in the weights: collecting the conditions up
to order $p$ gives a matrix $G_p(A,c)$ with one row per tree and one column per stage,
and $G_p\,b=r_p$ with $r_p$ the vector of $1/\gamma(\tau)$ ($G_p$,
$r_p$ page-local). [Belardo et al. (2026)](/sources/belardo-2026.md) draw the consequence
(§2–3, Eqs. (1)–(2)):

- the difference $b-\hat b$ of two nested weight vectors lies in $\ker G_p$ for the
  lower of the two orders; borrowing Lyness's quadrature term, they call a nonzero element of
  $\ker G_p$ a **null rule of order $p$**;
- *every* weight vector of order $\ge p$ that reuses the stages of $(A,b,c)$ is $b+Z_pk$, with $Z_p$
  an orthonormal basis of $\ker G_p$ and $k$ free ($Z_p$, $k$ page-local; Belardo et al. write $\boldsymbol\Phi_p$ for $G_p$); an embedding of
  order $p$ exists iff $G_p$ lacks full column rank.

Their examples (§3–4):

| Main method | kernel dimensions found | consequence |
|---|---|---|
| explicit midpoint ($s=2$) | $\dim\ker G_1=1$; $G_2$ full rank | only first-order embeddings |
| classical RK4 | $G_4$, $G_3$ full rank; $\dim\ker G_2=2$ | no embedding of order 3 or 4 |
| Dormand–Prince 5(4) ($s=7$) | $\dim\ker G_4=1$, $\dim\ker G_3=3$ | the standard $\hat b$ is one member of a one-parameter order-4 family |
| (5,3,3) method of Biswas et al. (2025) | $\dim\ker G_3=1$, $\dim\ker G_2=3$ | one order-3 family, three order-2 directions |
| Bogacki–Shampine 3(2) | $\dim\ker G_2=2$ | two-parameter family of estimators |

The RK4 row restates, as full rank of $G_3$, the classical result that a four-stage
fourth-order explicit method cannot be nested with an order-3 embedding, which they cite from
Hairer–Nørsett–Wanner; the rank is asserted, not proved (§3). Along the Dormand–Prince family
they print a new order-4 embedding with a wider real stability interval than the standard one
(Fig. 3), positive-weight order-2 embeddings for RK4 and for the (5,3,3) method of
[Biswas et al. (2025)](/sources/biswas-2025.md) (Figs. 2, 5; see
[explicit methods of high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)),
and first-order embeddings of the midpoint rule. They also propose such lower-order formulas
with larger stability intervals for stiffness detection, without demonstrating it (§1). The free
parameter is chosen by the real stability interval of the embedded formula, with the caveat that
this alone does not decide the quality of the estimator (§3 Remarks; see the next section).

## Stage values as embedded solutions

An internal stage value can itself serve as the embedded solution when its abscissa is 1 and
it is accurate enough.

- In the 2N-storage (5,3) method (5,3)$_4$ of [Bazavov (2026)](/sources/bazavov-2026.md),
  stage 5 has $c_5=1$ and satisfies $\sum_ja_{5j}=1$, $\sum_ja_{5j}c_j=\tfrac12$, so it is a
  second-order solution, and the method carries a 3(2) pair with no extra evaluation (§9,
  Table 10; see [low-storage methods](/methods/low-storage-runge-kutta.md)).
- In the monotonic Runge–Kutta–Chebyshev methods of [Faleichik & Moisa (2026)](/sources/faleichik-2026.md),
  the stability function of stage $Y_{s-1}$ equals $R_s'$ and $c_{s-1}=1$, so $Y_{s-1}$ is a
  stable first-order approximation at $t_n+h$. Its error constant depends on $s$, so it would
  need a normalization to avoid rejections when the stage count changes, and the authors use a
  Taylor-type estimate instead (§2, Eq. (19); §4; see
  [step-size control](/methods/step-size-control.md)).

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
- **Stability interval of the estimator is not efficiency.** Belardo et al. (2026) select
  embeddings by the real stability interval of the embedded formula, but their own test on the
  Bogacki–Shampine family shows the limit of that criterion: on a stiff scalar problem the
  estimator with the fewest accepted steps (804 against 906 for the standard one at stiffness
  50) has a *smaller* real stability interval (2.41 against 3.15), and the one with the largest
  interval (3.18) needs 1488 steps (§4, Tables 2–3; see
  [step-size control](/methods/step-size-control.md)). The paper itself warns that the interval
  alone cannot decide the choice (§3).
- **An estimator that fails first, by design.** Vermeire (2023) takes the opposite choice to
  Ranocha et al.: in the embedded [paired explicit methods](/methods/paired-explicit-runge-kutta.md)
  the embedded stability region is optimized to be *slightly smaller* than the main one, so
  that the estimate grows just before the main method becomes unstable and the controller
  tracks the stability limit (§3–4). The two choices serve different goals (a reliable accuracy
  estimate versus a stability-limit detector) and are not incompatible claims.
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
[Ranocha et al. (2025)](/sources/ranocha-2025.md) confirm the pattern on further
compressible-flow problems: the pair is usually the most efficient for lower-Mach flows,
positivity-critical problems and strong shock capturing, its stability region loses only about
5% to shock-capturing spectra against more than 20% for BS3(2)3F and RDPK3(2)5F, and it enters
the accuracy-limited regime at looser tolerances because it is optimized for the SSP coefficient,
not for the principal truncation error (§3, §4.1, §8).

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

Ranocha et al. (2025) call the third- and fourth-order FSAL pairs RDPK3(2)5F[3S\*$_+$] and
RDPK4(3)9F[3S\*$_+$] (§2.5). On compressible-flow problems RDPK3(2)5F is the more robust and
RDPK4(3)9F the more efficient at strict tolerances; the nine-stage pair crashed at tolerance
$10^{-4}$ on a Kelvin–Helmholtz instability and needed $10^{-5}$ or $10^{-6}$, which the
authors attribute to its larger stage count, "making it more difficult to adapt quickly to
changing conditions" (§6, §8; interpretation, not tested). [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md)
use BS3(2), SSP3(2)4[3S\*$_+$], RK3(2)5F[3S\*$_+$], the Bogacki–Shampine 5(4) pair and a
sixth-order Verner pair as the error-controlled schemes of their relaxation study (§2.1).

## Embedded paired explicit pairs

[Vermeire (2023)](/sources/vermeire-2023.md) adds embedded estimators to the second-order
[paired explicit Runge–Kutta (P-ERK)](/methods/paired-explicit-runge-kutta.md) families, in which
all members share $s$, $c$ with $c_i=\frac{i-1}{2(s-1)}$ and $b=(0,\dots,0,1)$ but evaluate only
$e$ stages ("active stages"; page-local $e$) (§3, Eqs. (15)–(20)). A member with $e$ active stages gets a
first-order embedding with $e-1$ active stages: $\hat b_s=0$, $\hat b_i=0$ on the inactive
stages, $\hat b_1=1-\sum_{i=2}^{s-1}\hat b_i$. Both the $e-2$ free subdiagonal entries of $A$ and
the $e-2$ free entries of $\hat b$ follow from prescribed optimized
[stability polynomials](/methods/optimal-stability-polynomial.md) sequentially, with no
nonlinear solve. For flux-reconstruction DG of degrees 1–8 and $e=3,\dots,16$, the ratio of the
embedded to the main maximal stable Courant number rises from about 60% at few stages to about
93% at $e=16$ (§4, Table 1, Fig. 2). Because $\hat b$ differs between members, the embedded
solution of a mixed family is not conservative, which the author accepts since it never
advances the solution (§3). Embedded pairs for the third-order P-ERK are left open, because base
and embedded methods must then satisfy more order conditions (§7).

## Embedded weights in positivity-preserving steps

- **Candidates for weight adaptation.** In the
  [adaptive-weight Runge–Kutta methods](/methods/adaptive-weight-runge-kutta.md) of
  [Nüßlein et al. (2021)](/sources/nusslein-2021.md) the embedded weights play two roles:
  their difference to $b$ gives the truncation estimate, and they are candidate vectors whose
  convex combinations with $b$ keep the update nonnegative (convex adaptation, §3.2). The
  local error of an adapted step is estimated by the embedded estimate plus the weight
  perturbation $\lVert h\sum_i(\tilde b_i-b_i)f(t_n+c_ih,Y_i)\rVert$ (page-local adapted
  weights $\tilde b$; §4.2, Eqs. (4.1)–(4.2)). Their count of free weight directions agrees
  with the null-rule analysis above: classical RK4 has none at order 3 (Table 1).
- **Estimates around a corrector.** For the Patankar predictor–corrector of
  [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) the embedded estimate is formed
  from the uncorrected SDIRK predictor, so the controller is unaffected by the correction;
  a more conservative variant adds the size of the correction (Remarks 3.20–3.21). The
  embedded method "only provides truncation error estimates and does not need to be
  positive" (§4.2). See [modified Patankar methods](/methods/modified-patankar-methods.md).

## Embedded estimates without a second weight vector

The embedded idea, two solutions of consecutive orders from shared work, is used outside
Runge–Kutta tableaux.

- **Single-stage Taylor methods.** [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md)
  (§5.2, Eqs. (63)–(65), Algorithms 1, 3) obtain an embedded solution for Lax–Wendroff flux
  reconstruction by truncating the Taylor series of the time-averaged flux one term earlier
  and dropping the interface terms in both updates, so no extra communication is needed.
  The estimate feeds the PID controller and weighted RMS norm of Ranocha et al. with the
  parameters tuned for BS3(2)3F and costs about 4%; that the difference is a local error
  estimate of the stated order is asserted, not proved
  *(compiler remark on §5.2, not in the source)*. See
  [step-size control](/methods/step-size-control.md).
- **Spectral deferred correction.** [Saupe et al. (2025)](/sources/saupe-2025.md) (§2.2,
  Algorithm 1) use the last two sweeps of SDC, of orders $k_{\max}$ and $k_{\max}-1$, as an
  embedded pair with an elementary controller and local extrapolation; with this and a
  residual-based variant, at least one adaptive parallel SDC variant is faster than the
  embedded pairs ESDIRK5(3) and ARK5(4) of Kennedy and Carpenter on each of their test
  problems, the pairs winning only on Schrödinger at low accuracy (§4.2, Fig. 10). See
  [deferred correction](/methods/deferred-correction.md).

Standard pairs also serve as reference solvers: SciPy's RK23 (Bogacki–Shampine), RK45
(Dormand–Prince) and DOP853 in [Popov (2024)](/sources/popov-2024.md) (§2.3), and the
Dormand–Prince 5(4) pair in Saupe et al. (2025, §4).

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

- **Printed slip in Nurkhametova et al. (2026).** The embedded weights printed for the
  SDIRK32 pair of Kennedy and Carpenter sum to about 0.379, so the printed $\hat b$ is not
  even consistent; the main weights satisfy the order-3 conditions *(compiler check of the
  printed tableau, §4.2.2, PDF p. 28)*. The SDIRK43 embedding satisfies the quadrature conditions to
  order 3 only, as an order-3 embedding should.
- Fekete et al. print the SSP coefficients and error measures of their new pairs nowhere in
  the paper; they defer them to a GitHub draft (their ref. [3]), and the coefficients of their
  numerically optimized embeddings are not printed (§2).
- Fekete et al. impose SSP conditions on the embedded method, although under local
  extrapolation only the main method's SSP property bears on the strong stability of
  $y_{n+1}$; the paper does not say why the embedded SSP coefficient matters *(compiler note,
  not in the sources)*.
- Fekete et al. print the Dormand–Prince pair as using "six function evaluations" (§3.1) and as
  "seven-stage" (§3.2.2); both are consistent with a seven-stage FSAL pair counted with and
  without the reused stage *(compiler check, not in the source)*.
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
- **The new Dormand–Prince embedding is not a more stable integrator.** Under local
  extrapolation the Dormand–Prince pair advances the fifth-order solution, so the wider real
  stability interval of the order-4 embedding printed by Belardo et al. (2026, Fig. 3) changes
  the estimator, not the stability of the integration. The paper does not say which solution is
  propagated for that pair, nor compare error constants, on which Dormand and Prince chose
  their embedding *(compiler note, not in the sources)*.
- Belardo et al. (2026) print several values that their own formulas do not reproduce, as
  checked on the Source page: the midpoint embedding's maximal real stability interval is
  given as "7" at $k=1$, while the one-parameter family gives $1/\alpha$ with
  $\alpha=\tfrac12(1-k/\sqrt2)$, i.e. 6.83 at $k=1$ and a supremum of 8 at $k\approx1.061$;
  the visible weights of the second RK4 embedding (Fig. 2b, partly hidden by Fig. 2c) violate
  the order-2 conditions; and the positive-weight (5,3,3) embedding said to sit where the
  interval is maximal has an interval of about 2.28, below the base method's 2.51 (§4;
  *compiler checks of Figs. 1, 2b and 5a*). Their basis $Z_p$ is not unique for kernel dimension $\ge2$, so "null rule
  #$j$" and the scale of $k$ depend on the basis computed.
- The Bogacki–Shampine estimator comparison of Belardo et al. (2026) selects the best
  estimator a posteriori on the problem it is evaluated on, with the exact solution, and the
  selected estimator differs between the two stiffness values (Tables 2–3).
- Vermeire (2023, Table 1) prints equal main and embedded stable Courant numbers for degree 1
  at $e=15$ (3.22) and $e=16$ (3.43), against the text's statement that the embedded value is
  always slightly smaller; the degree-1 pattern $\hat\nu_{\max}(e)=\nu_{\max}(e-1)$ stated in §4 would
  give 3.00 and 3.22 ($\nu_{\max}$, $\hat\nu_{\max}$ the main and embedded maximal stable
  Courant numbers). In the example
  tableau (Eq. (21)) the printed $\hat b_1$ omits $\hat b_6$.

# Citations

- [Fekete et al. (2022)](/sources/fekete-2022.md) — §1–2 (Eqs. (8)–(14), Remarks 1–2), §2.1–2.3 (embedded families), §3.1 (baseline pairs, work measure), §3.2.2, §4.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §2 (Eqs. (2.2)–(2.4), Remark 2.1), Remark 3.1, §4, §5.5.1–5.5.4 (Tables 3–4, Fig. 5), §6, Appendix A–B, Suppl. Table 1.
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §2.1–2.2 (ERKStep and ARKStep tables).
- [Steinebach (2023)](/sources/steinebach-2023.md) — §1 (Rodas5 estimator failures, Fig. 1), §3 (Rodas5P embedded method, Fig. 2).
- [Belardo et al. (2026)](/sources/belardo-2026.md) — §1–3 (null rules, Eqs. (1)–(2), Table 1, Remarks), §4 (Figs. 1–5, Tables 2–3).
- [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) — §1 (Eqs. (4)–(7), naive FSAL with relaxation), §2.1 (Lemma 1, Theorem 1), §2.2 (Lemma 2, Eq. (17), Theorem 2), §3 (Fig. 1), §4.
- [Vermeire (2023)](/sources/vermeire-2023.md) — §2.1–2.2, §3 (Eqs. (15)–(21)), §4 (Table 1, Figs. 1–2), §7.
- [Bazavov (2026)](/sources/bazavov-2026.md) — §9, Table 10 (free embedded 3(2) pair).
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §2 (Eq. (19)), §4.
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §2 (Eq. (2.2)), §2.5, §3, §4.1, §6, §8.
- [Al Jahdali et al. (2022)](/sources/aljahdali-2022.md) — §2.1 (error-controlled pairs).
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §3.2, §4.1 (Table 1), §4.2 (Eqs. (4.1)–(4.2)); arXiv v2.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — Remarks 3.20–3.21, §4.2.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §5.1–5.2 (Eqs. (61)–(65), Algorithms 1, 3), §6.3; arXiv v4.
- [Saupe et al. (2025)](/sources/saupe-2025.md) — §2.2 (Eqs. (14)–(15), Algorithm 1), §4.2 (Fig. 10); arXiv v2.
- [Popov (2024)](/sources/popov-2024.md) — §2.3 (reference solvers); arXiv v1.
- [Pan et al. (2022)](/sources/pan-2022.md) — §2.1.2 (Eqs. (10)–(15)), §2.4, App. A (Tables A1–A4).
