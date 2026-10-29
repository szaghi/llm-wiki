---
type: Method
title: "Strong-stability-preserving (SSP) Runge–Kutta methods"
description: "A Runge–Kutta method is SSP with coefficient $\\mathcal C$ when it preserves every convex-functional bound that forward Euler preserves for $h\\le h_{\\mathrm{FE}}$, under $h\\le\\mathcal C h_{\\mathrm{FE}}$; the page gives the origin as TVD time discretizations, the characterization, downwind operators, order and coefficient barriers, the optimal explicit methods, SSP multistep methods, embedded pairs and the multiderivative and IMEX extensions."
status: established
aliases: [SSP Runge–Kutta, SSPRK, SSPERK, TVD Runge–Kutta, Runge–Kutta type TVD time discretization, monotonicity-preserving Runge–Kutta, contractivity-preserving Runge–Kutta]
tags: [ssp, runge-kutta, stability, explicit, structure-preserving]
timestamp: 2026-10-29T18:13:00Z
---

# Strong-stability-preserving (SSP) Runge–Kutta methods

A [Runge–Kutta method](/definitions/runge-kutta-method.md) is *strong stability
preserving* (SSP) if it inherits, under a step-size restriction, any bound that the
forward Euler method satisfies for the same right-hand side. The hypothesis is the
**forward Euler condition**: for a convex functional $\lVert\cdot\rVert$ (a norm, a
semi-norm, total variation, or the positivity indicator),

$$\lVert y+hf(y)\rVert\le\lVert y\rVert\qquad\text{for all }y\text{ and }0\le h\le h_{\mathrm{FE}}.$$

The method is SSP with **SSP coefficient** $\mathcal C>0$ if, under this hypothesis,
$\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ whenever $h\le\mathcal Ch_{\mathrm{FE}}$
(Conde, Fekete & Shadid, [Fekete et al. 2022](/sources/fekete-2022.md), §1.1, Eq. (6);
[Gottlieb et al. 2022](/sources/gottlieb-2022.md), §1, Eq. (2)). The property is
nonlinear and independent of any linearization: it holds for every $f$ satisfying the
hypothesis. The effective SSP coefficient $\mathcal C_{\mathrm{eff}}=\mathcal C/s$
normalizes by the stage count (registry convention). Gottlieb, Shu & Tadmor use an
"effective CFL coefficient" with a different normalization, $\mathcal C\cdot\frac4{4+i}$
for a four-stage method with $i$ evaluations of the downwind operator, which compares the
method with an ideal one without them
([Gottlieb et al. 2001](/sources/gottlieb-2001.md), §4.1).

**Origin.** [Shu & Osher (1988)](/sources/shu-1988.md) (§II) present the methods as
"Runge–Kutta type TVD time discretizations" for the
[total variation](/definitions/total-variation-diminishing.md):
if the forward Euler step is TVD under a CFL restriction $\nu\le\nu_0$, a method written as
a convex combination of forward Euler steps is TVD under $\nu\le\nu_0\min\alpha_{ij}/\lvert\beta_{ij}\rvert$
(Prop. 2.1, Eq. (2.13)); Gottlieb et al. (2001, §2.2, Lemmas 2.1–2.2) recall this result
from them. Their Remark 2.1 already replaces the total variation by any
convex nonnegative functional on a Banach space of grid functions. The name *strong
stability preserving* is due to Gottlieb et al. (2001, abstract, §1), who renamed the
"TVD time discretizations" of Shu–Osher, Shu and Gottlieb–Shu because the argument uses
only convexity; they call the factor $\mathcal C$ the **CFL coefficient** (§2.1, Eq. (2.6)).

SSP is a different notion from the [strong stability](/properties/strong-stability.md)
of a method on a linear seminegative problem: see *Relation to strong stability* below.

## Characterization

**Shu–Osher form.** A method written as
$Y_i=\sum_{j<i}\bigl(\alpha_{ij}Y_j+h\beta_{ij}f(Y_j)\bigr)$ (with $Y_1=y_n$,
$\sum_j\alpha_{ij}=1$, all $\alpha_{ij},\beta_{ij}\ge0$) is a convex combination of
forward Euler steps of size $h\beta_{ij}/\alpha_{ij}$, so it is SSP with
$\mathcal C\ge\min_{ij}\alpha_{ij}/\beta_{ij}$ (Gottlieb et al. 2022, §1; Fekete et
al. 2022, §1.1). Fekete et al. call the convex decomposition "a sufficient and
necessary condition"; see *Qualifications*.

The form is printed by Shu & Osher (1988, §II, Eqs. (2.10)–(2.12)). Starting from an
explicit method in stage-value form, $Y_i=y_n+h\sum_{j<i}a_{ij}f(Y_j)$ for $i=2,\dots,s+1$
with $Y_{s+1}=y_{n+1}$ and $a_{s+1,j}=b_j$, any choice of $\alpha_{ij}\ge0$ with
$\sum_j\alpha_{ij}=1$ gives the equivalent form with
$\beta_{ij}=a_{ij}-\sum_{l=j+1}^{i-1}a_{lj}\alpha_{il}$ (their 0-based indices shifted by one), so the
representation is not unique (p. 9). Shu & Osher require only $\alpha_{ij}\ge0$:
a negative $\beta_{ij}$ is allowed if $f$ is replaced in that term by the downwind
operator $\tilde L$ (see *Downwind operators* below), and the bound becomes
$\min\alpha_{ij}/\lvert\beta_{ij}\rvert$ (Prop. 2.1). Gottlieb et al. (2001, §2.2, Lemmas
2.1–2.2, Eqs. (2.9)–(2.13)) restate both cases, writing "In [Shu–Osher], a general
$m$-stage Runge–Kutta method … is written in the form"; neither paper calls it the
Shu–Osher form, and both give it as a sufficient condition. Shu & Osher add that "most
classical Runge–Kutta methods lead to small CFL numbers in (2.13) as well as negative
$\beta_{ik}$'s", so they design methods directly in this form (p. 10).

**Kraaijevanger's characterization.** With the $(s+1)\times(s+1)$ matrix
$\tilde A=\begin{pmatrix}A&0\\b^\top&0\end{pmatrix}$ (page-local),

$$\mathcal C(A,b)=\sup\Bigl\{r\ge0:\ (I+r\tilde A)^{-1}\text{ exists},\ \tilde A(I+r\tilde A)^{-1}\ge0,\ r\tilde A(I+r\tilde A)^{-1}\mathbf 1\le\mathbf 1\Bigr\},$$

inequalities componentwise, as recalled by Fekete et al. (2022, §1.1, Thm. 1, Eqs.
(7a)–(7b), from Gottlieb–Ketcheson–Shu, Thm. 3.2). A positive SSP coefficient requires
$A\ge0$ and $b\ge0$ (Fekete et al. 2022, Thm. 2); for an irreducible method Biswas et
al. recall the sharper requirement $A\ge0$, $b>0$ (Kraaijevanger, Thm. 4.2;
[Biswas et al. 2025](/sources/biswas-2025.md), proof of Cor. 2.8).
[Ketcheson (2019)](/sources/ketcheson-2019.md) (§3.2, Eq. (22)) defines $\mathcal C(A,b)$ as
the radius of absolute monotonicity of the method, the largest $r\ge0$ with
$A(I+rA)^{-1}\ge0$, $(I+rA)^{-1}\mathbf 1\ge0$, $b^\top(I+rA)^{-1}\ge0$ and $R(-r)\ge0$,
citing Ferracina–Spijker.

**Stage and weight halves.** In the resolvent form used by Kuzmin et al. (2022, §3.1.1,
Eqs. (36)–(37)), with $X=(I+rA)^{-1}$, an explicit method is SSP with coefficient $r$ when
the stage conditions $AX\ge0$, $AX\mathbf 1\le\mathbf 1$ and the weight conditions
$b^\top X\ge0$, $b^\top X\mathbf 1\le1$ hold entrywise. Kuzmin et al. call a method
**internal SSP** when only the stage half holds: all stages then preserve the forward Euler
bound for $h\le rh_{\mathrm{FE}}$, but the update need not. Euler-based
[extrapolation methods](/methods/extrapolation-methods.md) are internal SSP at any order,
which is why their final update is limited separately (§3.1.2; see
[bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)).
[Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) (§7, Eq. (32)) use
the same stage conditions for implicit methods ("methods with SSP stages"): the stages are
bound preserving for $h\le rh_{\mathrm{FE}}$, conditions "more relaxed than those required
for the full method to be SSP"; backward Euler extrapolation satisfies them for every
$r$, so its stages are unconditionally bound preserving (§7.1).

**Linear SSP coefficient.** On linear problems only the
[stability polynomial](/definitions/stability-function.md) matters, and the relevant
quantity is the *radius of absolute monotonicity* (threshold factor) of $R$: the
largest $r$ such that $R$ and all its derivatives are nonnegative on $(-r,0]$ (Fekete
et al. 2022, §1.1, Def. 4). It can exceed the nonlinear $\mathcal C$, and it can be
positive when $\mathcal C=0$ (Biswas et al. 2025, after Cor. 2.8).

Gottlieb et al. (2001, §3.1, Prop. 3.2, Eqs. (3.1)–(3.2)) give the linear case of every
order: $s-1$ forward Euler stages followed by a convex combination,
$y_{n+1}=\sum_{k=0}^{s-2}\alpha_{s,k}(I+hL)^ky_n+\alpha_{s,s-1}(I+hL)^sy_n$ with
$\alpha_{1,0}=1$, $\alpha_{s,k}=\frac1k\alpha_{s-1,k-1}$ ($k=1,\dots,s-2$),
$\alpha_{s,s-1}=\frac1{s!}$ and $\alpha_{s,0}=1-\sum_{k\ge1}\alpha_{s,k}$ (page-local
indexing of their $\alpha_{m,k}$; all nonnegative), is of order $s$ on linear problems and
SSP with coefficient 1. Since the $s$-stage, order-$s$ linear Runge–Kutta polynomial is unique,
they conclude that "this unique $m$-stage, $m$th-order linear Runge–Kutta method is SSP under
CFL coefficient $c=1$": the degree-$s$ Taylor polynomial of $e^{z}$ has a convex form with
coefficient 1 for every $s$. Examples (Eqs. (3.4)–(3.5)):

$$\sum_{k=0}^3\frac{z^k}{k!}=\frac13+\frac12(1+z)+\frac16(1+z)^3,\qquad
\sum_{k=0}^4\frac{z^k}{k!}=\frac38+\frac13(1+z)+\frac14(1+z)^2+\frac1{24}(1+z)^4.$$

Their Table 3.1 lists the coefficients up to $s=8$. For nonlinear $f$ the same scheme is
SSP with coefficient 1 but "no longer $m$th-order accurate" (§3.1). They do not use the term
"absolute monotonicity".

## Barriers

- **Explicit order barrier.** No explicit Runge–Kutta method of order $p\ge5$ has
  $\mathcal C>0$, as recalled by Fekete et al. (2022, §1.1),
  [Babbar et al. (2022)](/sources/babbar-2022.md) (§1, Ruuth–Spiteri),
  [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) (§1, §3.1.1) and
  [Ciallella et al. (2022)](/sources/ciallella-2022.md) (Remark 3.1); the last two add the
  order-6 barrier for implicit SSP Runge–Kutta methods, and Kuzmin et al. that backward
  Euler is the only method SSP for arbitrarily large steps. The five-stage "fifth-order"
  SSPRK55 that Babbar et al. use is fifth order only on linear autonomous problems (§8).
  [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) (§1) recall the
  orders 4 and 6 and add that existing high-order implicit SSP methods "are not
  A-stable", which imposes severe step restrictions on stiff diffusion.
- **Stages equal to order: $\mathcal C\le1$.** Among $s$-stage, order-$s$ methods in
  Shu–Osher form with all $\alpha_{ij},\beta_{ij}\ge0$ the largest coefficient is
  $\mathcal C=1$; the proof already works in the linear case (Gottlieb et al. 2001, §3.1,
  Prop. 3.1). The bound holds only when the stage count equals the order: Gottlieb et al.
  recall an $s$-stage first-order method of Shu (1988, SIAM J. Sci. Statist. Comput.) with
  $\mathcal C=s$, for steady-state computations.
- **Four stages, fourth order.** Every four-stage fourth-order method in Shu–Osher form
  with nonzero coefficient (2.13) has at least one $\beta_{ij}<0$, so it needs the downwind
  operator (Gottlieb et al. 2001, §4.1, Prop. 4.2, recalled from Gottlieb–Shu). Shu & Osher
  (1988, §II, pp. 12–13) had stated only that "Extensive searching seems to indicate that we
  cannot avoid negative constants $\beta_{ik}$ this time", for four stages, with seven
  order equations in sixteen unknowns. Gottlieb et al. (2001) do not state the order-5
  barrier recalled above.
- **Implicit methods have bounded $\mathcal C$.** Implicit Runge–Kutta, multistep and
  general linear methods have finite SSP coefficients, "usually bounded by twice the
  number of stages for a Runge–Kutta method"; implicit methods that preserve the
  forward Euler condition for every $h>0$ cannot exist beyond first order (backward
  Euler is the exception at order 1), as recalled by Gottlieb et al. (2022, §1 and App.
  A, restating Gottlieb–Shu–Tadmor). The same barrier for positivity is the
  Bolley–Crouzeix result recalled on
  [positivity preservation](/properties/positivity-preservation.md).
  Gottlieb et al. (2001, §6, Props. 6.2–6.3) state the barrier for implicit methods
  without explicit terms, under the **backward** Euler hypothesis (unconditional strong
  stability of $y_{n+1}=y_n+hf(y_{n+1})$, Eq. (6.8)): an implicit Runge–Kutta method of
  the form $Y_i=\sum_{k<i}\alpha_{ik}Y_k+h\beta_if(Y_i)$, $\alpha_{ik}\ge0$ (their (6.7):
  one implicit evaluation per stage, no explicit $f$ terms, with $\tilde L$ for
  $\beta_i<0$), or an implicit multistep method with only the implicit term (6.16), cannot
  have all $\alpha\ge0$ at order $\ge2$. They add that with explicit terms SSP methods are
  obtained "under restrictions on $\Delta t$ similar to explicit methods" (§6.2–6.3). A
  second-order example of form (6.3) has $\alpha_{2,1}=\frac1{2\beta_1(1-\beta_1)}\in[4,\infty)\cup(-\infty,0)$,
  so no member is SSP (Eq. (6.4)).
- **Many stages do not bring SSP for free.** Stability polynomials optimized for
  hyperbolic spectra and realized as products of forward Euler steps and two-stage
  submethods have $\mathcal C=\min\alpha_{ij}/\beta_{ij}=0$, because the final row has
  $\alpha_{s+1,s}=0$, $\beta_{s+1,s}=1$; negative $\beta$, used to reduce
  [internal error amplification](/definitions/internal-stability.md), would need
  downwind treatment ([Doehring et al. 2024](/sources/doehring-2024.md), §9.4, Eq.
  (9.14)). On Burgers with a source and on the isentropic vortex their 28–120-stage
  methods need 28–79% of the linearly stable step and increase the total variation,
  while Ketcheson's third-order SSP method with $s=225=n^2$ stages, of similar internal
  amplification, keeps it constant; the authors attribute the reductions to the
  missing SSP property, and leave many-stage SSP methods of this kind open (§10.2,
  Tables 5–6). The optimal second-order disk polynomial
  $\frac{s-1}s(1+\frac z{s-1})^s+\frac1s$ is, by contrast, a composition of forward
  Euler steps and SSP with optimal coefficient, as recalled there (§3.1.2).
- **Partitioned methods.** A partitioned Runge–Kutta method is SSP only if every
  member is, with $h\le\min_q\mathcal C^{\{q\}}h_{\mathrm{FE}}$ over the members'
  coefficients (page-local $\mathcal C^{\{q\}}$), which makes SSP partitioned methods
  "in many cases ineffective" ([Doehring et al. 2025](/sources/doehring-2025.md),
  §2.5, Eq. (2.15)); see
  [paired explicit Runge–Kutta methods](/methods/paired-explicit-runge-kutta.md).
- **Weak stage order.** An explicit method with $A\ge0$, $b\ge0$ has either
  [weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}=1$, or $p\le1$
  and $q_{\mathrm w}=\infty$; hence every explicit method with $p\ge2$ and
  $q_{\mathrm w}\ge2$ has $\mathcal C=0$ (Biswas et al. 2025, §2, Thm. 2.7, Cor. 2.8).
  Such methods can still have a positive *linear* SSP coefficient: the families
  (3,2,2), (4,3,2) and (5,3,3) of
  [explicit methods with high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md)
  have linear SSP coefficient 1 (Biswas et al. 2025, §3.1.2–3.1.4). Avoiding
  [order reduction](/definitions/order-reduction.md) this way and preserving
  nonlinear strong stability are therefore mutually exclusive for explicit methods.

## Optimal explicit SSP methods

SSPERK$(s,p)$ denotes the explicit $s$-stage, order-$p$ method with the largest
$\mathcal C$ (Fekete et al. 2022, §2). The families used across the sources:

| Method | $\mathcal C$ | Structure | Source |
|---|---|---|---|
| SSPERK$(s,2)$ (Ruuth–Spiteri; $s=2$ Gottlieb–Shu) | $s-1$ | $a_{ij}=\frac1{s-1}$ for $j<i$, $c_i=\frac{i-1}{s-1}$, $b_j=\frac1s$ | Fekete et al. 2022, §2.1, Table 1 |
| SSPERK$(n^2,3)$, $n\ge2$ (Kraaijevanger; Ketcheson) | $n^2-n=s-\sqrt s$ | entries $\frac1{n(n-1)}$ except a $\frac{n(n-1)}2\times(2n-1)$ block of $\frac1{n(2n-1)}$ | Fekete et al. 2022, §2.2, Eqs. (15)–(16) |
| SSPERK$(4,3)$ (the $n=2$ case) | 2 | $c=(0,\frac12,1,\frac12)$, rows $(\frac12)$, $(\frac12,\frac12)$, $(\frac16,\frac16,\frac16)$, $b=(\frac16,\frac16,\frac16,\frac12)$ | Fekete et al. 2022, §2.2; [Ranocha et al. 2022](/sources/ranocha-2022.md), App. A, Eq. (A.1) |
| SSPERK$(10,4)$ (Ketcheson) | 6 | rows 2–5: $\frac16$ in all previous columns; rows 6–10: $\frac1{15}$ in columns 1–5, $\frac16$ in columns $6,\dots,i-1$; $b=\frac1{10}\mathbf 1$; low-storage | Fekete et al. 2022, §2.3 |

The effective coefficients are $\mathcal C_{\mathrm{eff}}=(s-1)/s$, $1-1/n$ and $0.6$
respectively *(compiler check, not in the sources)*.

**The founding methods.** Shu & Osher (1988, §II) derive the two-stage second-order family
(Eq. (2.14), free $\beta_{21}$ and $\alpha_{32}$ in registry indexing) and pick

$$Y_2=y_n+hf(y_n),\qquad y_{n+1}=\tfrac12y_n+\tfrac12Y_2+\tfrac12hf(Y_2),$$

with CFL coefficient 1, as "optimal (considering CFL restriction (2.13) and whether
$\tilde L$ appears)" ("It can be verified"; no proof printed), and identify it with Heun's
or the modified Euler method (Eqs. (2.15)–(2.16)). From the five-parameter third-order
family (2.17), "extensive searching" gives the preferred method

$$Y_2=y_n+hf(y_n),\quad Y_3=\tfrac34y_n+\tfrac14Y_2+\tfrac14hf(Y_2),\quad
y_{n+1}=\tfrac13y_n+\tfrac23Y_3+\tfrac23hf(Y_3),$$

with CFL coefficient 1 and no $\tilde L$ (Eqs. (2.18)–(2.19)); this is the SSPRK(3,3) of the
table above, for which Ketcheson (2019, §4) cites Shu & Osher. Shu &
Osher could not identify it with any classical third-order method, and the classical
third-order methods they took from Lambert lead to negative $\beta$ and small CFL numbers
(p. 12). Gottlieb et al. (2001, §4.1, Prop. 4.1, Eqs. (4.1)–(4.2)) print the same two
methods as optimal among $s$-stage, order-$s$ methods with $\beta_{ij}\ge0$, citing
Gottlieb–Shu for the proof. At fourth order Shu & Osher rewrite classical RK4 with two
$\tilde L$ evaluations and CFL coefficient $\frac23$ (Eq. (2.20)), raise it to $\frac{137}{200}$
with another choice of the third stage (Eq. (2.21)), and give a second fourth-order method
with coefficient $0.87$ (Eq. (2.22)); Gottlieb et al. (2001, Eq. (4.3)) give a four-stage
fourth-order method with coefficient $0.936$ and two $\tilde L$ evaluations (effective
coefficient $0.624$ in their normalization) and "do not claim" it optimal. Shu & Osher
(1988, Eq. (2.23)) also print a six-stage scheme with CFL coefficient $\frac7{30}$ that they
present as a fifth-order method from Lambert's book (p. 143); as printed in the version read,
its Butcher form gives $b^\top Ac=\frac8{45}$ instead of $\frac16$ *(compiler check, not in
the sources)*, see the [Source page](/sources/shu-1988.md).

**Other explicit classes.** Gottlieb et al. (2001, §4.2) print a third-order SSP method in
the two-register Williamson form with CFL coefficient 0.32 and report that a low-storage
method with negative $\beta$ "cannot be made SSP", because $\tilde L$ destroys the low-storage
property; see [low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md). In the
two-step two-stage hybrid family (§4.3, Eqs. (4.5)–(4.7)) the best third-order member found
has CFL coefficient $\approx0.473$, and no fourth-order member has all $\alpha\ge0$ (Prop.
4.3). The three-stage third-order
Shu–Osher method SSPRK(3,3) is the common baseline in the numerical comparisons of
Ranocha et al. (2022, §5) and Biswas et al. (2025, Table 3.2); among the classical
methods compared by Biswas et al., it, RK4 and Dormand–Prince all have
$q_{\mathrm w}=1$. Irksome ships an SSP tableau among its explicit methods
([Farrell et al. 2021](/sources/farrell-2021.md), §3.2).

Linear-stability measures go with these methods. Ranocha et al. report that the
four-stage third-order method has real stability interval 5.15, i.e. 1.29 per
right-hand-side evaluation, the largest scaled value of all pairs they compare, against
0.84 for SSPRK(3,3) and for Bogacki–Shampine 3(2) (Ranocha et al. 2022, Suppl. Table 1).
It can be implemented in three registers (Ranocha et al. 2022, App. A, Eq. (A.2)); see
[low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md). On linear
spectra of DG with subcell shock capturing, its stability region loses about 5% of
the admissible CFL number relative to plain DG, against more than 20% for
Bogacki–Shampine 3(2) and the five-stage pair of Ranocha et al.
([Ranocha et al. 2025](/sources/ranocha-2025.md), §4.1, Fig. 3). The second-order
two-stage SSP method of Shu and Osher is the base of the second-order multirate scheme
MRK2 of Constantinescu and Sandu, which [Kang & Constantinescu (2022)](/sources/kang-2022.md)
use and extend to several levels (§2.3, Table 1).

## SSP linear multistep methods

The same convexity argument applies to explicit multistep methods written as
$y_{n+1}=\sum_{r=1}^k\bigl(\bar\alpha_ry_{n+1-r}+h\bar\beta_rf(y_{n+1-r})\bigr)$ with
$\bar\alpha_r\ge0$, $\sum_r\bar\alpha_r=1$ (page-local backward-indexed coefficients; the
[registry form](/methods/linear-multistep-method.md) uses forward indices): it is SSP with
coefficient $\min_r\bar\alpha_r/\lvert\bar\beta_r\rvert$, with $\tilde L$ for negative
$\bar\beta_r$ (Gottlieb et al. 2001, §2.3, Lemma 2.3, Eq. (2.15), recalled from Shu (1988,
SIAM J. Sci. Statist. Comput.)). Gottlieb et al. prove (§5):

- no $k$-step method of order $k$ ($k\ge2$) with all $\bar\beta_r\ge0$ is SSP, and no
  $k$-step SSP method has order $k+1$ (Prop. 5.1);
- the optimal coefficients are $\frac12$ for two-step second-order methods, $\frac12$ for
  three-step second-order and $\frac13$ for four-step third-order methods with all
  $\bar\beta_r\ge0$ (Props. 5.2–5.4); the three-step and four-step optima are
  $y_{n+1}=\frac34y_n+\frac14y_{n-2}+\frac32hf(y_n)$ and
  $y_{n+1}=\frac{16}{27}y_n+\frac{11}{27}y_{n-3}+\frac{16}9hf(y_n)+\frac49hf(y_{n-3})$
  (Table 5.1, schemes 2 and 6, both attributed to Shu 1988, SIAM);
- more steps raise the coefficient: Table 5.1 lists 15 methods of orders 2–5, e.g.
  $\frac23$ for four-step second order and $0.567$ for six-step third order;
- five-step fourth-order methods with all coefficients nonnegative exist, with coefficient
  at most $\frac3{88}\approx0.034$ and $0.021$ found by search, which the authors say
  "disproves the belief that SSP schemes of order four or higher must have negative
  $\beta$" while being "probably too small … to be of much practical use".

They compare efficiency per right-hand-side evaluation: the three-step second-order method
with coefficient $\frac12$ and one evaluation per step has "the same efficiency" as the
two-stage method with coefficient 1, at more storage (Prop. 5.3), and likewise the four-step
third-order method against SSPRK(3,3). Shu & Osher (1988, §II, p. 7) give the reasons they
moved from multi-level TVD discretizations to Runge–Kutta methods: a multistep method must be
started by another method of the same order and must store all levels.

## Relaxation and the SSP coefficient

Scaling the weights of a method by the relaxation parameter of
[relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md) keeps the SSP property
over a range: for $0\le\gamma\le\gamma_*=-1/(R(-\mathcal C)-1)\ge1$ the method $(A,\gamma b)$
has $\mathcal C(A,\gamma b)\ge\mathcal C(A,b)$ (Ketcheson 2019, §3.2, Lemma 8, Thm. 9). Table 1
of the same paper gives $\gamma_*=2$ for SSPRK(2,2), $s/(s-1)$ for SSPRK$(s,2)$, $\frac32$ for
SSPRK(3,3), 1 for SSPRK(4,3), SSPRK(5,3) and SSPRK(9,3), 1.312 for SSPRK(5,4) and
$\frac{25}{24}$ for SSPRK(10,4); for all of them direct computation gives
$\mathcal C(A,\gamma b)=\mathcal C(A,b)$ on $[0,\gamma_*]$ and a smaller coefficient beyond.

## Embedded pairs and adaptive steps

Optimal SSP methods are usually run at a fixed CFL-limited step. Fekete et al. (2022)
construct [embedded pairs](/methods/embedded-runge-kutta-pair.md) that share $A$ with
the SSP method (no extra stage) and advance with the SSP solution (local
extrapolation). Design targets: embedded order $p-1$; non-defective (violating every
order-$p$ condition, otherwise the error estimate degenerates); rational coefficients;
and, if possible, an embedded SSP coefficient equal to $\mathcal C$ (§2, Eqs.
(9)–(11)). Results:

- SSPERK$(s,2)$: $\tilde b_1=[\frac1{s-1},\dots,\frac1{s-1},0]$ and
  $\tilde b_2=[\frac{s+1}{s^2},\frac1s,\dots,\frac1s,\frac{s-1}{s^2}]$, both with
  embedded SSP coefficient $s-1$; $\tilde b_2$ is preferred (§2.1).
- SSPERK$(4,3)$: $\tilde b_2=\frac14\mathbf 1$ supersedes the earlier
  $[\frac13,\frac13,\frac13,0]$ by a larger stability region; for SSPERK$(n^2,3)$,
  $n\ge3$, $\tilde b=\frac1{n^2}\mathbf 1$, and no embedding with SSP coefficient
  $n^2-n$ was found (§2.2).
- SSPERK$(10,4)$: no non-defective embedding exists, because one fourth-order
  condition, $b^\top(\frac{c^3}{3!}-\frac{Ac^2}{2!})=0$, holds for every weight vector
  on this $A$; eight rational third-order embeddings are listed, none with SSP
  coefficient 6 (§2.3).

With a PID controller these pairs reach the requested tolerance where classical
second-order pairs do not, cost 30–40% more than Bogacki–Shampine 3(2) at third order,
and beat Dormand–Prince 5(4) on hyperbolic problems for $\mathrm{tol}\ge10^{-4}$ at
fourth order (Fekete et al. 2022, §3.2.2). Ranocha et al. (2022, §5.5.2, Table 4) find
the four-stage third-order pair with $\hat b=\frac14\mathbf 1$ about 50% cheaper than
SSPRK(3,3) or Bogacki–Shampine 3(2) at loose and medium tolerances on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), nearly 50% faster than
Bogacki–Shampine 3(2) on the NASA juncture flow and the most efficient method on the
Imperial Front Wing at spatial degree 2 (§7.2–7.3, Tables 8–9), but its cost grows
sharply at tight tolerances. In a later study of error-based control for
compressible DG, the same pair with the Conde–Fekete–Shadid embedding is usually the
most efficient of four pairs for low-Mach, positivity-critical and strongly
shock-captured problems: 16% fewer right-hand-side evaluations than the five-stage
pair of Ranocha et al. on the Orszag–Tang vortex, and the fewest on both
Kelvin–Helmholtz tests (5478 and 6618 evaluations), one of which cannot be run with
CFL-based control at all; because its coefficients are optimized for $\mathcal C$
and not for the truncation error, it enters the accuracy-limited regime at looser
tolerances than the others (Ranocha et al. 2025, §3, §4.2, §6, §8, Tables 1, 4–5). Step-size control is on [step-size control](/methods/step-size-control.md).

## Beyond Runge–Kutta: downwind, multiderivative, IMEX

- **Downwind operators.** The downwind operator $\tilde L$ is a second approximation of
  the same spatial operator for which the backward-in-time Euler step $y-h\tilde L(y)$ is
  strongly stable under the same bound $h\le h_{\mathrm{FE}}$. It is introduced by Shu &
  Osher (1988, §II, Eqs. (2.8)–(2.9), Prop. 2.1), who credit the trick to Shu's 1986 report
  on multi-level TVD time discretizations; their example for $u_t=u_x$ pairs the forward
  difference $(u_{j+1}-u_j)/\Delta x$ for $f$ with the backward difference
  $(u_j-u_{j-1})/\Delta x$ for $\tilde L$, both TVD for $h/\Delta x\le1$. Gottlieb et al.
  (2001, §2.2, Lemma 2.2) restate it: for conservation laws $\tilde L$ comes from
  $u_t=f(u)_x$, "the only difference is the change of upwind direction", $\tilde L$ costs as
  much as $f$, and when both are needed at the same stage cost and storage for that stage
  double, so "we would like to avoid negative $\beta_{i,k}$ as much as possible". Shu &
  Osher's design goal is the fewest negative $\beta$ (p. 10). With $\tilde L$
  satisfying $\lVert y-h\tilde L(y)\rVert\le\lVert y\rVert$ for $h\le h_{\mathrm{FE}}$, Ketcheson
  built unconditionally SSP implicit methods of order 2, as recalled by Gottlieb et al.
  (2022, §1, Eq. (3)). Gottlieb et al. (2001, Prop. 6.2) state that in their implicit form
  (6.7), with $\tilde L$ for negative $\beta_i$, no method of order $\ge2$ has all
  $\alpha\ge0$; no ingested source says whether Ketcheson's methods are of that form.
- **Two-derivative methods.** Explicit SSP two-derivative methods use a second
  derivative condition $\lVert y+h^2\dot f(y)\rVert\le\lVert y\rVert$ or a Taylor
  series condition $\lVert y+hf(y)+\frac12h^2\dot f(y)\rVert\le\lVert y\rVert$, as
  recalled by Gottlieb et al. (2022, §1, Eqs. (4)–(5)); under either, no implicit
  two-derivative method of order 2 is unconditionally SSP (App. A). Under their new
  *backward derivative condition* Gottlieb et al. obtain unconditionally SSP implicit
  methods of orders 2, 3 and 4; see
  [multiderivative Runge–Kutta methods](/methods/multiderivative-runge-kutta.md).
- **IMEX.** For $f=f^{\mathrm E}+f^{\mathrm I}$, ordinary
  [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) methods do not remove the step
  restriction caused by $f^{\mathrm I}$ for general convex functionals (Gottlieb et
  al. 2022, §3, recalling Higueras and Conde et al.); the multiderivative IMEX methods
  of the same paper are SSP for $h\le rh_{\mathrm{FE}}$ with $r$ the SSP coefficient of
  the explicit part alone (Thm. 2).

## SSP explicit parts in IMEX and low-Mach practice

- **Explicit parts of IMEX pairs.** Several IMEX pairs pair an SSP explicit method with an
  L-stable or stiffly accurate implicit one: SSP-LDIRK2(3,3,2) (SSP second-order explicit
  part), SSP-LDIRK3(3,3,2) and SSP3(4,3,3) (SSPRK(3,3) explicit part), used for radiation
  hydrodynamics and for high-Mach flows
  ([Southworth et al. 2024](/sources/southworth-2024.md), §5.1;
  [Boscheri & Pareschi 2021](/sources/boscheri-2021.md), §3.4.1, Eqs. (79), (81)); the
  tableaux are on [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
  No SSP coefficient of a pair is stated in these sources, and the step restriction of the
  stiff part is not lifted (see *Beyond Runge–Kutta* above). Southworth et al. also compare
  with an operator split whose hydrodynamics uses third-order TVD Runge–Kutta (§5).
- **Implicit high order is not $L^\infty$-stable.** Boscheri & Pareschi (2021, §3.6) state
  that high-order implicit schemes "are not $L^\infty$ stable but only $L^2$ stable", so
  their semi-implicit scheme can produce bounded over- and undershoots at strong shocks when
  the explicit CFL condition is violated, which they control with an a-priori flattener that
  blends a first-order and the high-order solution. [Orlando & Bonaventura (2025)](/sources/orlando-2025.md)
  (§3) recall that implicit methods of order above one cannot be unconditionally TVD and that
  this holds for IMEX methods too. Both are consequences of the unconditional-SSP barrier
  above.
- **Explicit relaxation splitting.** [Toh et al. (2026)](/sources/toh-2026.md) (§3) use
  SSP-RK2 (Heun) for the explicit fluxes of extended MHD with an implicit relaxation step at
  every sub-stage, and suggest the Shu–Osher SSPRK(3,3) as a replacement; the coupling to the
  split relaxation step limits the scheme to first order in time in the stiff regime (§3.5;
  see [operator splitting](/methods/operator-splitting.md)).
- **When forward Euler is unstable.** [Kemm (2024)](/sources/kemm-2024.md) (§3.1–3.2) argues
  that SSP theory, for Runge–Kutta and for multistep methods, "hinges on the stability of the
  explicit Euler scheme" and is therefore "not applicable" to low-Mach finite-volume
  solvers whose acoustic dissipation scales with the flow speed: their semi-discrete spectra
  approach the imaginary axis, where forward Euler is unstable. Among explicit methods with
  the minimal number of stages only the third- and fourth-order ones have stability regions
  containing the required hull (§3.3, Fig. 2); in his tests with a nonlinear limiter
  third-order Adams–Bashforth outperforms a three-stage third-order Runge–Kutta method, which
  he attributes to the forward Euler first stage of every explicit Runge–Kutta step. See
  [linear multistep methods](/methods/linear-multistep-method.md).
- **Reference solutions.** SSPRK(3,3) provides the explicit reference runs of Orlando &
  Bonaventura (2025, §5.2–5.3) and Orlando et al. (2025b, §4.3) for low-Mach IMEX tests.

## SSPRK(3,3) as a building block of coupled and asynchronous schemes

The tableau of SSPRK(3,3) is $c=(0,1,\tfrac12)$, $a_{21}=1$,
$a_{31}=a_{32}=\tfrac14$, $b=(\tfrac16,\tfrac16,\tfrac23)$
([Unfer (2021)](/sources/unfer-2021.md), Eq. (106)), the Butcher form that Shu & Osher
(1988, Eq. (2.19)) print beside their Shu–Osher form (2.18). They point out that stage $i$
needs only $f$ of the previous stage, "so there is no need to store the previous
$L(u^{(k)})$, lowering the storage requirement significantly" (p. 12). Three sources use it
inside a larger time-stepping construction; in none of them is the SSP property of the
whole scheme proved.

- **Positivity inside a splitting.** [Liu & Zhang (2023)](/sources/liu-2023.md) (§2.1,
  §3.1, Eq. (5)) advance the Euler half-steps of a Strang splitting of compressible
  Navier–Stokes with SSPRK(3,3) in Shu–Osher form and a Zhang–Shu positivity limiter at
  every stage: positivity of density and internal energy follows from the convex
  combination of forward Euler steps, each positive under the Gauss–Lobatto CFL bound
  $\frac{h}{\Delta x}\max\lvert\text{wave speed}\rvert\le\frac12\hat\omega$ with
  page-local Gauss–Lobatto weight factor $\hat\omega$ (Eq. (17), cited). This is the
  forward-Euler argument of this page applied to the positivity functional; the viscous
  half of the splitting is implicit and first order, so the full scheme is at most first
  order in time (§1.4) and no temporal convergence is reported. See
  [positivity preservation](/properties/positivity-preservation.md) and
  [operator splitting](/methods/operator-splitting.md).
- **Asynchronous local time stepping.** Unfer (2021, §3.5) builds a third-order
  *asynchronous* Runge–Kutta method ARK3 (the acronym does not mean additive RK here) in
  which every finite-volume cell has its own step. The stage states become parabolic
  extrapolations in time and the conservative states cubic polynomials whose derivatives
  are assembled from face fluxes at three face times; with a global step the scheme
  reverts to SSPRK(3,3) (§3.5.2). A
  formal truncation analysis gives $O(\Delta x^3)$ in smooth regions (§3.5.3). The author
  states: "There is no claim at this point that the SSP property holds for the ARK3
  method"; strong shocks need a fallback to first-order states and per-stage recall of
  cells whose local step dropped (§3.5.2, App. B). On a Mach 10 double Mach reflection
  ARK3 runs 1.98 times faster than synchronous SSPRK(3,3) and shows more slip-line
  roll-ups (§4.5); see [local time stepping](/methods/local-time-stepping.md) and
  [double Mach reflection](/benchmarks/double-mach-reflection.md).
- **Stagewise interface coupling.** [Pulicani et al. (2026)](/sources/pulicani-2026.md)
  (§4.3, Eqs. (54)–(55)) advance an ALE finite-volume fluid with SSPRK(3,3), which they
  state "exhibits a greater stability" than forward Euler with MUSCL, and couple it to an
  implicit [Newmark](/methods/newmark-method.md) structure by solving a Lagrange-multiplier
  interface problem at each of the three stages, with the mid-stage structure velocity
  interpolated linearly. The coupled scheme converges at about second order at fixed CFL
  ($2.087$ in time, $2.064$ in space on a smooth piston problem; $1.41$ for the fluid in a
  coupled piston–rod test), so the third order of the Runge–Kutta method is not observed
  (§5.2–5.3).

## SSP as a proof device beyond Runge–Kutta

The Shu–Osher convex-combination argument transfers any property of a single forward
Euler step to the whole method. [Bassenne et al. (2021)](/sources/bassenne-2021.md)
(§3.1, Lemmas 3.3–3.4, Thm. 3.2) use it for explicit Runge–Kutta methods applied to a
first-order TASE-preconditioned linear problem: one forward Euler step of the
preconditioned problem is the $\theta$-method with $\theta$ equal to the TASE
parameter $\alpha$, unconditionally stable iff $\alpha\ge\frac12$, and a method with
nonnegative Shu–Osher coefficients is then unconditionally stable if
$\alpha\ge\frac12\max\beta_{ij}/\alpha_{ij}$; for linear SSP methods up to order four
this gives $\alpha\ge\frac12$. For four-stage fourth-order methods this uses a linear
SSP realization of the same polynomial, valid for linear constant-coefficient problems
only, since no four-stage fourth-order explicit method has a positive SSP coefficient
without downwinding (Gottlieb et al. 2001, Prop. 4.2, recalled above). See [TASE operators](/methods/tase-operators.md).

## SSP methods as bases of positivity-preserving schemes

- **Positivity under $h\le\mathcal Ch_{\mathrm{FE}}$.** If forward Euler keeps a problem
  nonnegative for $h\le h_{\mathrm{FE}}$, every SSP method does for $h\le\mathcal Ch_{\mathrm{FE}}$
  ([Nüßlein et al. 2021](/sources/nusslein-2021.md), §1). Beyond that bound SSPRK(3,3) can
  produce negative values even on a linear two-species exchange (their Example I, §2.1), and
  the [adaptive-weight](/methods/adaptive-weight-runge-kutta.md) remedy has room at full
  order only in many-stage methods: SSPRK(10,4) keeps four free weight directions at order 4,
  classical RK4 none (Table 1).
- **Positivity limiters.** With a Zhang–Shu limiter on a WENO5 reconstruction forward Euler
  is positive for CFL numbers up to $\tfrac1{12}$, and SSPRK(5,4) up to about
  $1.508\cdot\tfrac1{12}$ (Ciallella et al. 2022, Remark 3.1). Kuzmin et al. (2022) combine
  their GMC flux limiter with SSP54 (Kraaijevanger; Spiteri–Ruuth), whose Shu–Osher
  coefficients they print (App. A.1), as the SSP reference against non-SSP methods of order
  5 and 6 (§5).
- **Patankar schemes on SSP bases.** MPRK(2,2,1) modifies SSPRK(2,2) (Heun), the new
  MPRK(3,2) uses the SSPRK(3,3) abscissae and weights, the semi-implicit SI-RK2 and SI-RK3 put
  Patankar weights into the Shu–Osher forms of SSPRK(2,2) and SSPRK(3,3), and MPRKSO(4,3)
  uses optimal SSP coefficients ([Torlo et al. 2022](/sources/torlo-2022.md), §2, App. A).
  The SSP-MPRK family of Huang and coauthors is cited by [Izzo et al. (2025)](/sources/izzo-2025.md)
  (§1); the second- and third-order multistep Patankar schemes they reproduce come from
  explicit SSP multistep methods (§2): $y_n=\tfrac34y_{n-1}+\tfrac14y_{n-3}+\tfrac32hf(y_{n-1})$
  (Izzo et al. print the coefficient $\tfrac32$ on $f(y_{n-2})$, a slip; see the Patankar page) and $y_n=\tfrac{16}{27}y_{n-1}+\tfrac{11}{27}y_{n-4}+\tfrac{16}9hf(y_{n-1})+\tfrac49hf(y_{n-4})$.
  Gottlieb et al. (2001, Table 5.1) print them as schemes 2 and 6, with
  $\bar\beta=(\frac32,0,0)$ for the first, attribute both to Shu (1988, SIAM) and prove them
  optimal (Props. 5.3–5.4; see *SSP linear multistep methods* above).
  [Zhu et al. (2024)](/sources/zhu-2024.md) print exactly these two Gottlieb–Shu–Tadmor
  methods as convex combinations of forward Euler steps (Eqs. (2.5)–(2.6)) and obtain
  positivity of their Patankar versions with explicit convection under
  $h\le\tfrac12h_{\mathrm{FE}}$ and $\tfrac13h_{\mathrm{FE}}$, the SSP coefficients of the
  bases (§3.3). See [modified Patankar methods](/methods/modified-patankar-methods.md).
- **Deferred correction.** Ciallella et al. (2022, §6.6) state that arbitrary-order
  [deferred correction](/methods/deferred-correction.md) cannot be written as a convex
  combination of explicit Euler steps, so explicit DeC with a positivity limiter has no
  positivity proof even under the limiter CFL bound (§6.6, no proof given and no order named).
  The same paper recalls that explicit SSP Runge–Kutta methods are at most fourth order
  (Remark 3.1). Since explicit DeC methods are explicit Runge–Kutta methods, those of order $\ge5$
  cannot have a positive SSP coefficient *(compiler remark, not in the sources)*; for orders
  up to 4 no ingested source settles the question. [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md)
  (§1, §3.1) cite Liu, Shu and Zhang's study of the SSP property of deferred correction only as
  the origin of bDeC and of the α-family, without reporting its SSP findings.
- **Reference integrators.** SSP methods remain the default explicit baseline:
  SSPRK$(N+1,N+1)$ for $N=1,2$ and SSPRK54 in Lax–Wendroff flux reconstruction comparisons
  (Babbar et al. 2022, §8), and the third-order Shu–Osher method and the four-stage
  fourth-order Spiteri–Ruuth method for DG references in multiderivative tests
  ([Chouchoulis et al. 2022](/sources/chouchoulis-2022.md), §6.3), where SSP multiderivative
  methods are named as future work.

## Limits of the SSP route: limiting and entropy

- **Limiting instead of convex decomposition.**
  [Ern & Guermond (2022)](/sources/ern-2022.md) obtain invariant-domain preservation for
  any explicit method by limiting each stage against a low-order Euler step from the
  previous stage; the step bound depends on the abscissae only, so methods with
  $\mathcal C=0$, such as the explicit midpoint rule, become admissible at the full
  per-stage step, and fifth order is reachable (§2.4, §4.5; see
  [invariant-domain preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md)).
  Their **efficiency ratio** (largest admissible step over $s\,h_{\mathrm{FE}}$, bounded
  below by $1/(s\Delta c_{\max})$ with page-local $\Delta c_{\max}$ the largest gap between
  an abscissa and the closest earlier one not above it) coincides with $\mathcal C_{\mathrm{eff}}$ for SSPRK(2,2) and
  SSPRK(3,3) but not in general: they give about 0.51 for Kraaijevanger's SSPRK(5,4),
  whose $\mathcal C\approx1.508$ gives $\mathcal C_{\mathrm{eff}}\approx0.30$ *(compiler check, not in the sources)*. The two numbers measure different constructions and must not be compared. The
  IMEX version (Part II, [Ern & Guermond 2023](/sources/ern-2023.md)) needs no positivity
  of the Butcher coefficients either.
- **SSP-RK3 and entropy stability of RKDG.** [Wei & Shu (2026)](/sources/wei-2026.md)
  prove a fully discrete cell square-entropy inequality for explicit third-order RKDG on
  Burgers' equation for the three-stage family with $c_3=1$ and positive weights, which
  contains Kutta's method and **excludes SSP-RK3** ($c_3=\tfrac12$); they recall from their
  companion paper that RKDG with $P^2$ elements and a class of third-order methods
  including SSP-RK3 is not $L^2$ stable on Burgers under $h\sim\Delta x$ (§1). Here the
  SSP property is not the one that decides; see
  [fully discrete cell entropy inequality](/results/fully-discrete-cell-entropy-inequality.md).

## Relation to strong stability

SSP assumes the forward Euler condition and then asks nothing of the operator.
[Strong stability](/properties/strong-stability.md) in the sense of Sun and coauthors
asks for $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ in an inner-product norm for the
linear problem $y'=Ly$ with $\langle Lv,v\rangle\le0$, and makes no forward Euler
assumption. The two meet when $L$ is *coercive*: then forward Euler is contractive for
small $h$, and Gottlieb–Shu–Tadmor showed through the SSP formulation that every linear
Runge–Kutta method is strongly stable, as recalled by
[Sun & Shu (2021)](/sources/sun-2021.md) (§1). Gottlieb et al. (2001, §3.2) define the
coercivity constant
$\eta_{\mathrm c}(t)=\inf_{\lVert v\rVert=1}-\mathrm{Re}\langle L(t)v,v\rangle/\lVert L(t)v\rVert^2>0$
(page-local; their Assumption 3.1), show that forward Euler is contractive iff $h\le2\eta_{\mathrm c}$,
and state that their aim is strong stability of "the general $m$-stage, $m$th-order accurate
Runge–Kutta scheme" under that bound, with "our uniform $C_s=2$" against the constant
$\frac1{31}$ of Levy–Tadmor for RK4. The printed proof treats classical RK4 for time-dependent
$L(t)$ with $\lVert L(t)-L(t')\rVert\le K\lvert t-t'\rvert/\eta_{\mathrm c}(t)$: the frozen-coefficient
polynomial has norm at most 1 by its convex form (Prop. 3.2), and the bound is
$\lVert y_n\rVert\le e^{3Kt_n}\lVert y_0\rVert$ under $h_n\le2\eta_{\mathrm c}(t_n)$ (Prop. 3.3). Sun, Wei & Wu note that the
truncated-Taylor polynomials of explicit linear Runge–Kutta methods have SSP form
([Sun et al. 2022](/sources/sun-2022.md), §1). For merely seminegative $L$ (a skew
operator from a wave-type semi-discretization, for instance) forward Euler itself
increases the norm, the hypothesis fails for every $h>0$, and SSP and contractivity
arguments "may not be generally applied" (Sun et al. 2022, §1). That regime is handled
by the [energy method](/methods/runge-kutta-energy-method.md).

## Qualifications

- **"Necessary and sufficient."** Fekete et al. (2022, §1.1) call the Shu–Osher convex
  decomposition "a sufficient and necessary condition for the SSP property".
  Necessity holds for the optimal coefficient through the canonical Shu–Osher form
  (the Kraaijevanger characterization above); an arbitrary decomposition can
  underestimate $\mathcal C$. Shu & Osher (1988, p. 9) note that the decomposition is
  not unique, and Gottlieb et al. (2001, Lemma 2.1) give it as a sufficient condition only.
- **"Optimal" in the founding papers.** Shu & Osher (1988, pp. 11–12) call the second-order
  method "optimal" ("It can be verified") and the third-order one "preferred" after
  "extensive searching"; the optimality statements are in Gottlieb et al. (2001, Prop. 4.1),
  for $s$-stage, order-$s$ methods with $\beta_{ij}\ge0$, recalled from Gottlieb–Shu.
- **Several space dimensions.** Shu & Osher (1988, §III, p. 22; §IV, Example 3) run the
  methods on dimension-by-dimension semi-discretizations with the one-dimensional CFL numbers
  "shrunk by a factor $(d)^{-1}$" in $d$ dimensions; one-dimensional CFL numbers "led to
  instability–overflow" in their two-dimensional advection test.
- **The $2s$ bound.** Gottlieb et al. (2022, §1) attribute the "twice the number of
  stages" bound for implicit SSP Runge–Kutta methods to Ketcheson's downwind paper;
  the cited paper is not ingested, so the bound is recorded here as recalled, not as
  the result of that reference.
- **Unconditional SSP.** Gottlieb et al. (2022, §1) state without qualifier that
  implicit methods preserving the forward Euler condition for every $h$ "cannot
  exist"; their own Appendix A makes clear that the barrier is for order greater than
  one.
- **"Implicit SSP methods are at most first order."** Ern & Guermond (2022, §1.2, §2.4)
  write this, citing Gottlieb–Shu–Tadmor (Prop. 6.2). Gottlieb et al. (2001, §6.2, Prop.
  6.2) state that implicit Runge–Kutta methods of their form (6.7), with only implicit terms
  and $\alpha_{ik}\ge0$, cannot have order $\ge2$, so none is unconditionally SSP beyond first
  order, and that SSP methods exist under step restrictions once explicit terms are admitted.
  Kuzmin et al. (2022, §1) and Ciallella et al. (2022, Remark 3.1) recall that implicit SSP
  methods with a finite coefficient exist up to order 6, and Quezada de Luna & Ketcheson
  (2022, §1) put the implicit barrier at order 6.
- **Embedded SSP coefficient.** Fekete et al. impose SSP conditions on the embedded
  weights, but with local extrapolation the advanced solution is the main method's,
  so the embedded coefficient does not affect the strong stability of $y_{n+1}$; the
  paper does not discuss why it matters.
- **Controllability of SSP pairs.** Ranocha et al. (2022, §5) could not make
  SSPERK$(10,4)$ with the embedded method of Conde, Fekete & Shadid step-size-control
  stable with any PID controller they tested, nor the nine-stage third-order method,
  and they judge the estimator of the four-stage third-order pair unreliable at tight
  tolerances; Fekete et al. (2022, §4) recommend the SSPERK$(10,4)$ pairs
  $\tilde b_1,\tilde b_3,\tilde b_5,\tilde b_8$ on the strength of work-precision tests
  that do not examine step-size-control stability. Which of the eight embeddings
  Ranocha et al. used is not stated, and the test problems differ (WENO
  finite-volume versus entropy-stable spectral elements), so this is recorded as a
  partial disagreement, not a contradiction.
- The SSP coefficients and error measures of the new pairs of Fekete et al. are not
  printed in the version read (arXiv v1); they are deferred to a repository.
- **"Only $L^2$ stable."** Boscheri & Pareschi (2021, §3.6) credit to Gottlieb, Shu &
  Tadmor the statement that high-order implicit schemes "are not $L^\infty$ stable but only
  $L^2$ stable". Gottlieb et al. (2001, §6) state Props. 6.2–6.3 for unconditional strong
  stability in any norm or convex functional, for the forms (6.7) and (6.16), and add that SSP
  methods with explicit terms exist under step restrictions (§6.2–6.3); the words "only $L^2$
  stable" do not appear there. Their explicit-Euler-stage pair SP(1,1,1) is called "stiffly accurate
  and stability preserving" without an SSP coefficient.
- **Deferred correction and SSP.** Ciallella et al.'s (2022, §6.6) statement that
  arbitrary-order DeC is not a convex combination of Euler steps sits beside the
  Liu–Shu–Zhang study of SSP deferred correction that both they and Micalizzi & Torlo
  (2024) cite, but no ingested source reports what that study finds, so there is no
  contradiction; by the explicit SSP order barrier the statement certainly holds from order 5
  *(compiler remark, see above)*. Babbar et al. (2022, §9) write that "there is no four stage SSPRK method",
  meaning that no four-stage fourth-order explicit method has a positive SSP coefficient.
- **Kemm's "unstable first stage" thesis.** Kemm's explanation of the Runge–Kutta failures
  is heuristic: the linear stability of a Runge–Kutta step depends only on its stability
  polynomial, his first-order-in-space tests behave as linear theory predicts, and the
  amplification of internal stage perturbations is measured by
  [internal stability](/definitions/internal-stability.md), not by the stability of the
  first stage alone *(compiler remark, not in the sources)*. His claim that SSP theory does not
  apply is correct as a statement about its hypothesis, not a counterexample to it.

# Citations

- [Shu & Osher (1988)](/sources/shu-1988.md) — §II (Eqs. (2.8)–(2.23), Prop. 2.1, Remark 2.1, pp. 7, 9–14), §III p. 22, §IV Example 3; read as ICASE Report 87-33.
- [Gottlieb et al. (2001)](/sources/gottlieb-2001.md) — §1, §2.1–2.3 (Lemmas 2.1–2.3), §3.1 (Props. 3.1–3.2, Eqs. (3.1)–(3.5), Table 3.1), §3.2 (Prop. 3.3), §4.1–4.3 (Props. 4.1–4.3, Eqs. (4.1)–(4.7)), §5 (Props. 5.1–5.4, Table 5.1), §6 (Props. 6.2–6.3, Eqs. (6.3)–(6.16)).
- [Ketcheson (2019)](/sources/ketcheson-2019.md) — §3.2 (Eq. (22), Lemma 8, Thm. 9, Table 1); arXiv v1.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — §1.1 (Eq. 6, Thms. 1–2, Def. 4, order barrier), §2 (Eqs. 9–11), §2.1–2.3 (SSPERK$(s,2)$, $(n^2,3)$, $(10,4)$ and embeddings), §3.2.2, §4.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §1 (Eqs. 2–5, SSP coefficient of implicit methods), §3 and Thm. 2 (IMEX), App. A (unconditional-SSP barrier).
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §2, Thm. 2.7, Cor. 2.8; §3.1.2–3.1.4 (linear SSP coefficient 1); Table 3.2.
- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5, §5.5.2, Table 4, §7.2–7.3, App. A (Eqs. A.1–A.2), Suppl. Table 1.
- [Sun & Shu (2021)](/sources/sun-2021.md) — §1 (coercive operators, contractivity).
- [Sun et al. (2022)](/sources/sun-2022.md) — §1 (SSP versus noncoercive problems; Taylor polynomials in SSP form).
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §3.2 (SSP tableau in Irksome).
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §3.1.2, §9.4 (Eq. 9.14), §10.2 (Tables 5–6).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §2.5 (Eq. 2.15).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §3, §4.1 (Fig. 3), §4.2 (Table 1), §6 (Tables 4–5), §8.
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — §3.1 (Lemmas 3.3–3.4, Thm. 3.2).
- [Kang & Constantinescu (2022)](/sources/kang-2022.md) — §2.3 (Table 1; MRK2 base method).
- [Kemm (2024)](/sources/kemm-2024.md) — §1, §3.1–3.3 (Figs. 1–2).
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.4.1 (Eqs. (78)–(81)), §3.6 (Eqs. (104)–(105)); arXiv v1.
- [Toh et al. (2026)](/sources/toh-2026.md) — §3, §3.5.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §5, §5.1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §3, §5.2–5.3; HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §4.3; arXiv v5.
- [Unfer (2021)](/sources/unfer-2021.md) — §3.5 (Eq. (106)), §3.5.2–3.5.3, App. B, §4.5.
- [Liu & Zhang (2023)](/sources/liu-2023.md) — §1.4, §2.1, §3.1 (Eqs. (5), (17)).
- [Pulicani et al. (2026)](/sources/pulicani-2026.md) — §4.3 (Eqs. (54)–(55)), §5.2–5.3.
- [Kuzmin et al. (2022)](/sources/kuzmin-2022.md) — §1, §3.1.1–3.1.2 (Eqs. (35)–(37)), §5, App. A.1; arXiv v2.
- [Nüßlein et al. (2021)](/sources/nusslein-2021.md) — §1, §2.1, §4.1 (Table 1); arXiv v2.
- [Torlo et al. (2022)](/sources/torlo-2022.md) — §2, App. A; arXiv v5.
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — Remark 3.1, §6.6; arXiv v3.
- [Babbar et al. (2022)](/sources/babbar-2022.md) — §1, §8, §9; arXiv v1.
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §6.3; arXiv v1.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — §1, §3.1; arXiv v4.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §1, §2; arXiv v1.
- [Ern & Guermond (2022)](/sources/ern-2022.md) — §1.2, §2.4, §4.1, §4.5; HAL v2.
- [Ern & Guermond (2023)](/sources/ern-2023.md) — §3.3 (Eq. (63)); HAL v1.
- [Wei & Shu (2026)](/sources/wei-2026.md) — §1, §2 (Eq. (12)); author manuscript.
- [Quezada de Luna & Ketcheson (2022)](/sources/quezadadeluna-2022.md) — §1, §7 (Eq. (32)), §7.1, §9; arXiv v1.
- [Zhu et al. (2024)](/sources/zhu-2024.md) — §2.2 (Eqs. (2.5)–(2.6)), §3.3; arXiv v1.
