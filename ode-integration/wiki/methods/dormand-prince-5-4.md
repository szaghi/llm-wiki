---
type: Method
title: "Dormand–Prince 5(4) pair"
description: "The seven-stage explicit embedded Runge–Kutta pair RK5(4)7M of Dormand and Prince (1980): a fifth-order formula advanced by local extrapolation, a fourth-order estimator, and a last stage reused as the next first stage, with its construction, coefficients, error and stability data, its siblings 7S and 6M, and its later uses."
status: established
aliases: [RK5(4)7M, DP5(4)6F, DOPRI5, DOPRI5(4), DOPRI54, DP5, Dormand–Prince pair, dopri5]
tags: [runge-kutta, explicit, embedded-pair, step-size-control, order-conditions]
timestamp: 2026-10-29T18:13:00Z
---

# Dormand–Prince 5(4) pair

The **Dormand–Prince 5(4) pair** is the explicit [embedded pair](/methods/embedded-runge-kutta-pair.md)
RK5(4)7M of [Dormand & Prince (1980)](/sources/dormand-1980.md): seven stages, a fifth-order
formula that advances the solution and a fourth-order formula that only estimates the error
(local extrapolation), and a seventh stage evaluated at the new point that is the first stage
of the next step. After the first step it costs six evaluations of $f$ per accepted step and
one more after each rejection (§2). The paper designs it as one member of a family whose free
parameters are chosen to make the sixth-order error terms of the fifth-order formula small;
two siblings, RK5(4)7S (larger stability regions) and the six-stage RK5(4)6M, come from the same
family (§3). Later sources call the pair DP5(4)6F, DOPRI5 or DP5.

## Notation and naming

This page writes the pair in registry notation: $b$ are the fifth-order (advanced) weights,
$\hat b$ the fourth-order (embedded) weights, $\hat p=4$. Dormand & Prince put the hat on the
*higher*-order quantities, the reverse convention; they work with the autonomous form
$y'=f(y)$ and with stage increments that include the factor $h$ (§1). Their name RK5(4)7M reads:
advanced order 5, estimator order 4, seven stages counting the reused one, "M" for the
minimum-truncation-error member (the letters M and S are not defined in the paper; the reading
comes from its text). The Kennedy–Carpenter–Lewis convention used by
[Ranocha et al. (2022)](/sources/ranocha-2022.md) counts effective evaluations and appends F
for the reused stage, giving DP5(4)6F; both names denote the same tableau (Table 2 of Dormand &
Prince).

## Construction

The family has seven stages with the reuse built in (Eq. (2.1)): $c_7=1$ and $a_{7j}=b_j$ for
$j\le6$, $b_7=0$, so the fifth-order formula uses six stages and the fourth-order formula all
seven. Dormand & Prince describe this as the converse of the "common practice that the higher
order formula uses more stages than the lower order formula" (§1). They credit the reuse device
to Fehlberg (1972) and to their 1978 paper and do not use the word FSAL.

The 25 [order conditions](/results/runge-kutta-order-conditions.md) of the pair (17 for order 5
on six stages, 8 for order 4 on seven) are reduced by simplifying assumptions (§2, Eqs.
(2.2)–(2.3)):

- $\sum_ib_ia_{ij}=b_j(1-c_j)$ for $j=1,\dots,6$, the $D(1)$ form for the fifth-order weights;
- $b_2=\hat b_2=0$;
- $\sum_ja_{ij}c_j=\tfrac12c_i^2$ and $\sum_ja_{ij}c_j^2=\tfrac13c_i^3$ for $i=3,\dots,6$, the
  $C(3)$ relations on those rows.

Three of these are dependent, and 11 independent equations remain, solved in closed form. The
assumptions force $c_6=1$; with $c_3,c_4,c_5$ free,

$$b_3=\frac{3-5(c_4+c_5)+10c_4c_5}{60c_3(1-c_3)(c_3-c_4)(c_3-c_5)},\qquad
b_6=\frac{12-15(c_3+c_4+c_5)+20(c_3c_4+c_4c_5+c_5c_3)-30c_3c_4c_5}{60(1-c_3)(1-c_4)(1-c_5)},$$

$b_4$ and $b_5$ by cyclic exchange of $c_3,c_4,c_5$ in the formula for $b_3$ (Eq. (2.6)), and
$c_2=\tfrac23c_3$, $a_{32}=\tfrac34c_3$, $a_{42}=3c_4^2(3c_3-2c_4)/(4c_3^2)$,
$a_{43}=c_4^2(c_4-c_3)/c_3^2$; the remaining entries of $A$ follow in sequence (§2). The
fourth-order weights then solve a linear system "given a value for" the seventh weight
$\hat b_7$, "which is arbitrary": the embedding is a one-parameter family for fixed $(A,c)$, and
$\hat b_7$ "tunes" the error estimate (§2–3). Four parameters remain: $c_3$, $c_4$, $c_5$ and
$\hat b_7$ (§3). [Belardo et al. (2026)](/sources/belardo-2026.md) (§3–4) recover the same
one-parameter order-4 family as the one-dimensional kernel of the order-4 condition matrix;
see [embedded pairs](/methods/embedded-runge-kutta-pair.md).

## Choice of the free parameters

Dormand & Prince choose $c_3,c_4,c_5$ to make small the 2-norm of the 20 sixth-order error
coefficients of the fifth-order formula, the principal error norm $\mathcal E_6$ of the
order-conditions page up to the sign of each term. Under the simplifying assumptions the 20
coefficients are fixed multiples of four of them, which they give in closed form in
$c_3,c_4,c_5$ (Eq. (3.1)). They also ask for moderate coefficients, $\lvert c_i\rvert\le1$ and
"reasonably distinct" $c_i$, because large $a_{ij}$ and $b_i$ are "unsatisfactory with regard to
rounding error" (§3). The minimum-error choice is $c_3=\tfrac3{10}$, $c_4=\tfrac45$,
$c_5=\tfrac89$, $\hat b_7=\tfrac1{40}$, with norm $3.99\times10^{-4}$, "about 8 times" smaller
than the $3.36\times10^{-3}$ of Fehlberg's RKF4, the pair that "practical results" favoured in
local-extrapolation mode (p. 23). [Biswas et al. (2025)](/sources/biswas-2025.md) list
$3.991\times10^{-4}$ for Dormand–Prince 5 in their table of principal error norms (Table 3.2; see
[explicit methods of high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)).

## Coefficients of RK5(4)7M

From Dormand & Prince (1980, Table 2), in registry convention ($b$ fifth order, $\hat b$ fourth
order):

| $c_i$ | $a_{i1}$ | $a_{i2}$ | $a_{i3}$ | $a_{i4}$ | $a_{i5}$ | $a_{i6}$ | $b_i$ | $\hat b_i$ |
|---|---|---|---|---|---|---|---|---|
| $0$ | | | | | | | $\tfrac{35}{384}$ | $\tfrac{5179}{57600}$ |
| $\tfrac15$ | $\tfrac15$ | | | | | | $0$ | $0$ |
| $\tfrac3{10}$ | $\tfrac3{40}$ | $\tfrac9{40}$ | | | | | $\tfrac{500}{1113}$ | $\tfrac{7571}{16695}$ |
| $\tfrac45$ | $\tfrac{44}{45}$ | $-\tfrac{56}{15}$ | $\tfrac{32}9$ | | | | $\tfrac{125}{192}$ | $\tfrac{393}{640}$ |
| $\tfrac89$ | $\tfrac{19372}{6561}$ | $-\tfrac{25360}{2187}$ | $\tfrac{64448}{6561}$ | $-\tfrac{212}{729}$ | | | $-\tfrac{2187}{6784}$ | $-\tfrac{92097}{339200}$ |
| $1$ | $\tfrac{9017}{3168}$ | $-\tfrac{355}{33}$ | $\tfrac{46732}{5247}$ | $\tfrac{49}{176}$ | $-\tfrac{5103}{18656}$ | | $\tfrac{11}{84}$ | $\tfrac{187}{2100}$ |
| $1$ | $\tfrac{35}{384}$ | $0$ | $\tfrac{500}{1113}$ | $\tfrac{125}{192}$ | $-\tfrac{2187}{6784}$ | $\tfrac{11}{84}$ | $0$ | $\tfrac1{40}$ |

The last row of $A$ equals $b^\top$, which is the reuse of the seventh stage.

## Stability

The stability polynomials of the family are (§3, Eqs. (3.2)–(3.3))

$$P(z)=\sum_{j=0}^5\frac{z^j}{j!}+d\,z^6,\qquad
\hat P(z)=\sum_{j=0}^4\frac{z^j}{j!}+e\,z^5+f\,z^6+g\,z^7,$$

with $d=c_4(2-5c_3)/240$ and, for RK5(4)7M, $d=\tfrac1{600}$, $e=\tfrac{1097}{120000}$,
$f=\tfrac{161}{120000}$, $g=\tfrac1{24000}$ ($d,e,f,g$ page-local; p. 23). Dormand & Prince want
the regions of both formulas enlarged, because "an absolute stability failure on the lower order
formula could cause severe problems in step size control", against Alt's argument that the
embedded formula's stability does not matter under local extrapolation (pp. 23–24); see
[stability function](/definitions/stability-function.md). Following Lawson, who showed that
$d=\tfrac1{1280}$ enlarges the region, they build the high-stability sibling below. A choice
$d=\tfrac1{1275}$ gives two further pairs, rejected for their large coefficients (p. 24). Along
the one-parameter family of order-4 embeddings, Belardo et al. (2026, Fig. 3) print an
embedding with a wider real stability interval than the standard one; under local extrapolation
it changes the estimator, not the advanced solution.

## The siblings RK5(4)7S and RK5(4)6M

- **RK5(4)7S** (Table 3) favours stability: $c_3=\tfrac13$, $c_4=\tfrac59$, $c_5=\tfrac23$, error
  norm $1.81\times10^{-3}$. The best $\hat b_7$ for comparable regions of the two formulas was
  $\tfrac1{150}$, but "this results in a poorly 'tuned' formulae pair and a compromised choice is"
  $\hat b_7=-\tfrac1{50}$ (p. 24). Tableau: $c=(0,\tfrac29,\tfrac13,\tfrac59,\tfrac23,1,1)$; rows
  of $A$: $(\tfrac29)$, $(\tfrac1{12},\tfrac14)$, $(\tfrac{55}{324},-\tfrac{25}{108},\tfrac{50}{81})$,
  $(\tfrac{83}{330},-\tfrac{13}{22},\tfrac{61}{66},\tfrac9{110})$,
  $(-\tfrac{19}{28},\tfrac94,\tfrac17,-\tfrac{27}7,\tfrac{22}7)$, and $b^\top$;
  $b=(\tfrac{19}{200},0,\tfrac35,-\tfrac{243}{400},\tfrac{33}{40},\tfrac7{80},0)$,
  $\hat b=(\tfrac{431}{5000},0,\tfrac{333}{500},-\tfrac{7857}{10000},\tfrac{957}{1000},\tfrac{193}{2000},-\tfrac1{50})$.
  For a moderately stiff system the step is then limited by stability, and RK5(4)7S "will permit
  a substantial reduction in computing time *provided* only a modest global error is required.
  If high accuracy is needed the RK5(4)7S offers no advantage" (§4).
- **RK5(4)6M** (Table 4) takes $\hat b_7=0$, so the seventh stage is not needed and the pair has
  six stages and no reuse. The two weight vectors then coincide unless a $4\times4$ matrix built
  from $c_3,c_4,c_5$ and the second column of $A$ is nonsingular; it is singular iff
  $c_4=c_3/\bigl(2(5c_3^2-4c_3+1)\bigr)$, and that singular case is taken, with $\hat b_6=\tfrac1{20}$
  as the tuning parameter (p. 24). With $c_3=\tfrac3{10}$, $c_5=\tfrac23$: $c=(0,\tfrac15,\tfrac3{10},\tfrac35,\tfrac23,1)$;
  rows of $A$: $(\tfrac15)$, $(\tfrac3{40},\tfrac9{40})$, $(\tfrac3{10},-\tfrac9{10},\tfrac65)$,
  $(\tfrac{226}{729},-\tfrac{25}{27},\tfrac{880}{729},\tfrac{55}{729})$,
  $(-\tfrac{181}{270},\tfrac52,-\tfrac{266}{297},-\tfrac{91}{27},\tfrac{189}{55})$;
  $b=(\tfrac{19}{216},0,\tfrac{1000}{2079},-\tfrac{125}{216},\tfrac{81}{88},\tfrac5{56})$,
  $\hat b=(\tfrac{31}{540},0,\tfrac{190}{297},-\tfrac{145}{108},\tfrac{351}{220},\tfrac1{20})$.
  Its error norm is $1.23\times10^{-3}$ and it "is sixth order for quadrature problems" (p. 24).
  The paper ties sixth order on $y'=f(t)$ to the vanishing of the bushy sixth-order coefficient
  (p. 22); its closed form (3.1) gives, at $c_3=\tfrac3{10}$, $c_4=\tfrac35$, $c_5=\tfrac23$,
  $[0.2-\tfrac23\cdot0.3]/7200=0$ *(compiler check, not in the sources)*.

All the 1980 pairs are built to avoid a failure the authors find in high-order pairs of
Fehlberg ($p>5$) and in their own 1978 pairs: on quadrature problems $y'=f(t)$ both formulas
give the same value and the error estimate vanishes (p. 22).

## Numerical evidence in the founding paper

The tests use the DETEST set of Hull et al. over seven tolerances $10^{-3-r}$, $r=0,\dots,6$,
modified to record the maximum global error, with function calls (rejected steps included) as
the cost measure (§4). Totals of Table 5:

| Pair | function calls | steps | max. error | fraction deceived | fraction badly deceived |
|---|---|---|---|---|---|
| RKF4 (5(4) mode) | 226208 | 36363 | 12.4 | 0.005 | 0.000 |
| RK5(4)7M | 209305 | 33126 | 9.7 | 0.008 | 0.000 |
| RK5(4)6M | 267324 | 43394 | 1.2 | 0.000 | 0.000 |
| RK5(4)7S | 186229 | 29158 | 15.2 | 0.027 | 0.001 |

By the criteria of Hull et al. the authors find the two minimum-error pairs, 7M and 6M, "more
efficient than the RKF4" (§4). On problem A3, $y'=y\cos t$, RK5(4)7M needs about 800 evaluations
for a maximum absolute global error of $10^{-6}$ against 1450 for RKF4 (§4(a)); on the two-body
problem D5 with eccentricity 0.9, "a severe test for the step-size control procedure", RK5(4)7M
is again the most efficient (§4(b), Fig. 3; see [Kepler problem](/benchmarks/kepler-problem.md)).
Their conclusion is that the seventh evaluation "permits lower truncation terms at a penalty of
the loss of one extra evaluation when a step rejection occurs but this seems to be worthwhile"
(§5).

## In later sources

- **Controllers.** Gustafsson's PI34 controller was designed for DP5(4)6F; Ranocha et al. (2022)
  recommend $(\beta_1,\beta_2,\beta_3)=(0.70,-0.40,0)$ for it and find an optimized controller
  not significantly better than PI34 (§5.5.1, Table 11). Dormand & Prince print the elementary
  error-per-step and error-per-unit-step controllers with safety factor 0.9 (§1); see
  [step-size control](/methods/step-size-control.md).
- **Efficiency when stability-limited.** On the
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at tolerance $10^{-5}$, DP5(4)6F
  needs 8014 right-hand-side evaluations against 5256 for BS3(2)3F (Ranocha et al. 2022,
  §5.5.1, Table 3). The fourth-order SSP pairs of [Fekete et al. (2022)](/sources/fekete-2022.md)
  beat Dormand–Prince 5(4) on their hyperbolic tests for tolerances $\ge10^{-4}$ (§3.2.2); Fekete et al. print it
  as using "six function evaluations" and as "seven-stage", the two counts of the reused stage.
- **Weights for fixed stages.** [Nüßlein et al. (2021)](/sources/nusslein-2021.md) (Table 1)
  count free weight directions of the Dormand–Prince RK5(4)7 stages, 6, 5, 3, 1, 0 for orders
  1–5, in agreement with Belardo et al.'s kernel dimensions; they use it in their
  [adaptive-weight methods](/methods/adaptive-weight-runge-kutta.md).
- **Order reduction.** Like other explicit methods of weak stage order 1, Dormand–Prince drops to
  order 2 on linear advection with time-dependent forcing ([Biswas et al. 2025](/sources/biswas-2025.md),
  §5, Fig. 5.1; see [weak stage order](/definitions/weak-stage-order.md)).
- **Relaxation.** DOPRI5 is one of the base methods of the multiple-relaxation experiments of
  [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) on the
  [Kepler problem](/benchmarks/kepler-problem.md), and DP5 is one of the two pairs on which
  [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) test their FSAL-preserving relaxation
  (see [embedded pairs](/methods/embedded-runge-kutta-pair.md)).
- **Reference solver.** [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) (§5.3.2) take the
  reference solution of their perturbed [Kepler problem](/benchmarks/kepler-problem.md) from
  SciPy's dopri5 dense output at $\mathrm{rtol}=\mathrm{atol}=10^{-16}$.

## Qualifications

- The registry and Dormand & Prince use opposite hat conventions; every coefficient above is
  translated, and quotations from the paper keep its own wording.
- Dormand & Prince derive the stability-oriented design of RK5(4)7S from Lawson's condition
  $d=\tfrac1{1280}$, $c_4=3/(16(2-5c_3))$ (p. 23), and print $c_4=\tfrac59$ with $c_3=\tfrac13$ in
  Table 3. The paper's printed reference numbers and figure axes contain slips recorded on the
  [Source page](/sources/dormand-1980.md).
- The DETEST results are aggregate counts over 25 non-stiff problems; the paper does not define
  the efficiency criteria of Hull et al. that it applies.

# Citations

- [Dormand & Prince (1980)](/sources/dormand-1980.md) — §1 (Eq. (1.6), naming, local extrapolation), §2 (Eqs. (2.1)–(2.6)), §3 (Eqs. (3.1)–(3.3), Tables 2–4), §4 (Table 5, Figs. 2–3), §5.
- [Belardo et al. (2026)](/sources/belardo-2026.md) — §3–4, Fig. 3 (one-parameter order-4 family, alternative embedding).
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5.5.1 (Table 3), Table 11 (naming DP5(4)6F, controller).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — Table 3.2 (principal error norm), §5 (Fig. 5.1, order reduction).
- [Fekete et al. (2022)](/sources/fekete-2022.md) — §3.1, §3.2.2 (baseline, evaluation counts).
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §4.1, Table 1; arXiv v2.
- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §5.3.1–5.3.2.
- [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) — §3 (Fig. 1).
