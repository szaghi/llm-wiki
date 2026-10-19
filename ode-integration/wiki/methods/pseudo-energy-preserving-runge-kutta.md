---
type: Method
title: "Pseudo-energy-preserving explicit Runge–Kutta methods"
description: "A Runge–Kutta method of classical order p is pseudo-energy-preserving of order q ≥ p when its one-step energy error on every canonical Hamiltonian system is O(h^(q+1)); the conditions follow from energy-preserving B-series of the modified equation, and explicit methods up to q = 6 exist."
status: established
aliases: [PEP method, PEP order, pseudo-energy-preserving method, PEP(s,p,q)]
tags: [runge-kutta, explicit, structure-preserving, geometric-integration, order-conditions, hamiltonian]
timestamp: 2026-10-19T20:00:00Z
---

# Pseudo-energy-preserving explicit Runge–Kutta methods

For a Hamiltonian system $y'=\mathcal J\nabla H(y)$ with a constant,
non-singular, skew-symmetric matrix $\mathcal J$ (page-local; the source calls
such systems "canonical"), a Runge–Kutta method of classical order $p$ is
**pseudo-energy-preserving (PEP) of order $(p,q)$** if

$$H(y_{n+1})=H(y_n)+O(h^{q+1})$$

for every such system, with $q\ge p$; it is **energy preserving** if
$H(y_{n+1})=H(y_n)$ exactly ([de León et al. (2025)](/sources/deleon-2025.md),
Defs. 1–2, §2). No Runge–Kutta method is energy preserving for all Hamiltonian
systems (Celledoni et al. 2009, as recalled in §1), so PEP methods aim at a
small energy error instead. They are the energy analogue of the
**pseudo-symplectic** methods of Aubry & Chartier (1998), explicit methods
that satisfy the symplecticity conditions (equivalently, preservation of
quadratic invariants) to an order $q>p$ (§1.1; see
[symplecticity](/properties/symplecticity.md)). A method is written
PEP$(s,p,q)$ with $s$ stages.

## Characterization through the modified equation

The derivation works on the
[modified equation](/methods/backward-error-analysis.md)
$y'=h^{-1}B(v,y)$ of the method, whose coefficients $v(\tau)$ the source calls
the "flow" coefficients, as opposed to the "map" coefficients $u(\tau)$, the
elementary weights of $y_{n+1}=B(u,y_n)$ (page-local names $u$, $v$; de León et al. (2025), Eqs. (1)–(3)). A method is PEP of order $q$ if its
modified equation is energy preserving to order $q$.

**Theorem 1** (Celledoni, McLachlan, Owren & Quispel 2010, Thms. 2–3, as
quoted). A B-series vector field for a canonical Hamiltonian system preserves
energy to order $q$ iff it can be written, up to $O(h^{q+1})$, as a linear
combination over trees $\lvert\tau\rvert\le q$ and leaves $\ell$ of $\tau$ of
$F(\tau)+(-1)^{m}F(\tau^*(\ell))$, where $m$ is the distance from the root
to $\ell$ and $\tau^*(\ell)$ the **energy-preserving conjugate** of $\tau$ with
respect to $\ell$ (Eq. (5)). The conjugate is obtained by making the parent of
$\ell$ the new root and reattaching $\ell$ as a child of the old root (§2.1,
page-local $m$, $\ell$). The condition is necessary and sufficient (Remark 1).

Consequences (Examples 1–3): bushy trees, all leaves on the root, cannot
appear ($\tau^*=\tau$ with $m=1$); tall trees with an even number of vertices
cannot appear; tall trees with an odd number of vertices and "self-conjugate"
trees carry free coefficients. Conjugacy partitions the trees of each order
into classes, and each class gives exactly one linear condition on $v$. Up to
order 5 the classes have one or two trees; from order 6 there are triplets
whose three equations are dependent and give one constraint (Eq. (8)).

## Order conditions

In Butcher bracket notation the conditions on the modified equation are
(de León et al. (2025), §2.2): order 2, $v([\bullet])=0$ (classical
order 2); order 3, $v([\bullet,\bullet])=0$, weaker than classical order 3,
which also needs $v([[\bullet]])=0$; order 4, three more; order 5, four more;
order 6, eleven more. The substitution law (computed with
[BSeries.jl](/software/bseries-jl.md) and SymPy, §2.3) turns them into
conditions on the tableau. Assuming $c=A\mathbf 1$ and classical order 2:

$$\begin{aligned}
&\text{PEP order 3:}\quad b^\top c^2=\tfrac13,\\
&\text{PEP order 4:}\quad b^\top A^2c=b^\top Ac-\tfrac18,\qquad b^\top\operatorname{diag}(c)Ac-\tfrac12b^\top Ac^2=\tfrac1{12},\qquad b^\top c^3=\tfrac14,\\
&\text{PEP order 5:}\quad b^\top\operatorname{diag}(c)A^2c+\tfrac12b^\top A^2c^2=b^\top A^2c+\tfrac12b^\top Ac^2-\tfrac12b^\top Ac+\tfrac1{24},\\
&\qquad 2\,b^\top A\operatorname{diag}(c)Ac-b^\top(Ac)^2=b^\top A^2c+b^\top Ac^2-b^\top Ac+\tfrac1{24},\\
&\qquad b^\top\operatorname{diag}(c^2)Ac-\tfrac13b^\top Ac^3=\tfrac1{12},\qquad b^\top c^4=\tfrac15,
\end{aligned}$$

with powers of vectors componentwise (Eqs. (14)–(16), rewritten in matrix
form). The order-6 conditions are given only on the elementary weights
(Eq. (13), one of them quadratic in the weights). Cumulative counts:

| order | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| PEP conditions | 1 | 2 | 3 | 6 | 10 | 21 |
| pseudo-symplectic conditions | 1 | 2 | 3 | 6 | 12 | 28 |

(Table 4.) PEP order 2 equals classical order 2, so every consistent method
with $q\ge2$ has $p\ge2$ (§2.3). Compared with the classical
[order conditions](/results/runge-kutta-order-conditions.md), the PEP
conditions drop every condition that only moves the solution along the energy
surface.

## Methods

* **PEP(2,2,3).** In the two-stage family $c=(0,\alpha_\star)$,
  $b=(1-\tfrac1{2\alpha_\star},\tfrac1{2\alpha_\star})$ (page-local parameter),
  $q=3$ holds only for $\alpha_\star=\tfrac23$, i.e. $b=(\tfrac14,\tfrac34)$,
  Ralston's method (§3, citing Celledoni et al.); $\alpha_\star=\tfrac12$ is the
  explicit midpoint method.
* **PEP(3,2,4)**, the unique three-stage second-order method with $q=4$:
  $c=(0,\tfrac13,\tfrac56)$, $a_{21}=\tfrac13$, $a_{31}=-\tfrac5{48}$,
  $a_{32}=\tfrac{15}{16}$, $b=(\tfrac1{10},\tfrac12,\tfrac25)$ (§3). It has
  $b^\top Ac=\tfrac18\ne\tfrac16$, so $p=2$ *(source's reader check)*.
* **PEP(4,2,5)** with rational coefficients (Eq. (31)); **PEP(5,2,6)**,
  **PEP(6,3,6)**, **PEP(7,4,6)** and **PEP(7,5,6)** in floating point
  (Tables 9–12). Several have negative weights; PEP(6,3,6) has
  $c_5\approx0.015$, $c_6\approx0.043$ and PEP(7,4,6) a negative abscissa.
* **Largest $q$ found** for $s$ stages and order $p$ (Table 5): $(2,2)\to3$;
  $(3,2)\to4$, $(3,3)\to3$; $(4,2)\to5$, $(4,3)\to4$, $(4,4)\to4$;
  $(5,2)\to6$, $(5,3)\to5$, $(5,4)\to5$. For $p=2$, $q=s+1$; except for
  $s=p=2$, raising $q$ above $p$ costs extra stages.

The search minimized the norm of the leading truncation-error coefficients
with MATLAB fmincon through RK-Opt, from "many thousands" of random starts per
$(s,p,q)$; it is local and non-convex, and stopped at $s=5$ because the
optimizer "struggles greatly" beyond (§3).

## Numerical behaviour

Comparisons use equal work per unit time: step $h=sh_0$ with a common advance
per stage $h_0$ (Eq. (18)).

* **Exponential entropy system** $y_1'=-e^{y_2}$, $y_2'=e^{y_1}$, $T=160$:
  PEP(6,3,6) converges at order 3 in the solution and about 5.96 in the
  energy before round-off; PEP(7,4,6) shows energy rates up to 8.13 before
  round-off, "roughly consistent with the theory" (Tables 6–7). The problem
  comes from the relaxation literature.
* **Undamped Duffing oscillator** started just inside the homoclinic orbit:
  the largest step keeping the orbit in the right half-plane is $0.004$ for
  explicit midpoint and $0.152$ for PEP(5,2,6) (§4.1.2).
* **Hénon–Heiles**: PEP methods conserve energy markedly better than
  pseudo-symplectic methods of matching order to $t=10^3$ (Fig. 2).
* **[BBM](/benchmarks/benjamin-bona-mahony-equation.md) solitary wave** with a
  conservative Fourier semidiscretization: PEP(4,2,5) has smaller long-time
  errors than explicit midpoint to $t=10^3$ (Fig. 3).
* **Non-canonical systems.** On a nonlinear oscillator and Lotka–Volterra,
  Theorem 1 does not apply; the energy rate of PEP(6,3,6) falls to the
  classical order (3.05, Table 8), yet higher PEP order still gives smaller
  long-time errors and longer linear error growth (§4.2, Figs. 4–8).

PEP and pseudo-symplectic methods behave alike in most tests (§4).

## Relation to exact preservation

Exact alternatives listed by the source (§1): the average vector field method
and continuous-stage Runge–Kutta methods (implicit), discrete gradients,
projection (oblique projection along the step keeps linear invariants), and
[relaxation](/methods/relaxation-runge-kutta.md), which makes explicit
methods conserve one chosen functional exactly. PEP methods need no solve and
no modified step, at the price of an energy error of order $h^q$ over bounded
time. See [entropy stability](/properties/entropy-stability.md).

## Qualifications

* "PEP order" is a one-step (local) energy-error order. Over a fixed interval
  it gives a global energy error $O(h^q)$, which is what the convergence tables
  measure.
* Table 5 records the largest $q$ the local search found; optimality is not
  proved.
* Linear error growth for PEP methods is motivated by results for exactly
  conservative methods (cited) and observed over moderately long times, not
  proved; growth becomes superlinear later (Fig. 4a).
* **Printed slips** (arXiv v2 read; source's reader checks): in Eq. (31) the
  abscissae $c_3$ and $c_4$ of PEP(4,2,5) are swapped (row sums give
  $c_3=\tfrac{37}{63}$, $c_4=\tfrac{19}{20}$; with $c=A\mathbf 1$ the method
  satisfies all conditions to order 5 in exact arithmetic); two constants of
  the map–flow relations Eq. (9) are wrong ($\tfrac7{12}$ and $\tfrac16$ where
  the exact flow requires $\tfrac1{12}$ and $\tfrac18$), while the downstream
  conditions (11) and (15) are right; the second order-5 condition prints
  $\sum b_i(a_{ij}c_j)^2$ for $\sum_ib_i(\sum_ja_{ij}c_j)^2$; the
  experimental-order formula Eq. (21) has a sign error; PEP(7,5,6) has two
  weights of size $10^{-13}$, effectively zero, and is not tested.

# Citations

- [de León et al. (2025)](/sources/deleon-2025.md) — §1 (exact alternatives, Celledoni et al. impossibility), §1.1 (pseudo-symplectic methods), §2 (Defs. 1–2, Theorem 1, Eqs. (1)–(5), Remark 1), §2.1–2.4 (Examples 1–3, Eqs. (8)–(16), Table 4), §3 (Eq. (17), PEP(3,2,4), Table 5), §4 (Eq. (18), Tables 6–8, Figs. 1–8), App. (Eq. (31), Tables 9–12).
