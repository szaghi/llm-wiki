---
type: Definition
title: "B-series, composition and substitution laws"
description: "A B-series is a formal expansion over rooted trees of elementary differentials weighted by a coefficient map; Runge–Kutta steps and exact flows are B-series, composition of methods is the Butcher product over ordered subtrees, and substitution of a modified vector field is the law over edge partitions that underlies backward error analysis."
status: established
aliases: [Butcher series, B-series method, Butcher group, composition law, substitution law, NB-series, P-series]
tags: [runge-kutta, order-conditions, geometric-integration]
timestamp: 2026-10-20T16:00:00Z
---

# B-series, composition and substitution laws

For an autonomous ODE $y'=f(y)$, a **B-series** with coefficient map
$a:T\cup\{\varnothing\}\to\mathbb R$ is the formal series

$$B(a,y)=a(\varnothing)\,y+\sum_{\tau\in T}\frac{h^{\lvert\tau\rvert}}{\sigma(\tau)}\,a(\tau)\,F(\tau)(y),$$

summed over all rooted trees $\tau$, with $\lvert\tau\rvert$ the number of
vertices, $\sigma(\tau)$ the symmetry and $F(\tau)$ the elementary
differential ([Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md), Eq. (9),
after Butcher and Hairer–Wanner). A series with $a(\varnothing)=1$ represents a
one-step map $y_{n+1}=B(a,y_n)$; one with $a(\varnothing)=0$ represents a
vector field $y'=h^{-1}B(a,y)$ (§2.1, Eq. (10)). Other normalizations of the
$h^{\lvert\tau\rvert}/\sigma(\tau)$ factor exist; this page follows the source.

## Trees and elementary differentials

A rooted tree is written $\tau=[\tau_1,\dots,\tau_m]$, the root joined to the
roots of $\tau_1,\dots,\tau_m$; $\bullet$ is the single vertex. The recursions
are (Ketcheson & Ranocha (2023), Eqs. (5), (11)–(12)):

$$\begin{aligned}
F(\bullet)(y)&=f(y), & F(\tau)(y)&=f^{(m)}(y)\big(F(\tau_1)(y),\dots,F(\tau_m)(y)\big),\\
\gamma(\bullet)&=1, & \gamma(\tau)&=\lvert\tau\rvert\,\gamma(\tau_1)\cdots\gamma(\tau_m),\\
\sigma(\bullet)&=1, & \sigma(\tau)&=\sigma(\tau_1)\cdots\sigma(\tau_m)\,\mu_1!\mu_2!\cdots,
\end{aligned}$$

with $\mu_k$ the multiplicities of identical subtrees. For example the tree
with root, one child and two grandchildren has $F(\tau)=f'f''(f,f)$,
$\sigma=2$, $\gamma=12$ (Table 1). There are 1, 1, 2, 4 trees with 1–4
vertices. RootedTrees.jl stores a tree as its canonical level sequence, the
lexicographically largest depth-first list of vertex depths, generated in
constant time per tree by the Beyer–Hedetniemi algorithm (Def. 1.1, §4.1).

## The two basic series

* **Exact flow.** $y(t+h)=B(e,y(t))$ with $e(\varnothing)=1$,
  $e(\tau)=1/\gamma(\tau)$ (Eqs. (19)–(20)).
* **Runge–Kutta step.** $y_{n+1}=B(\Phi,y_n)$ with $\Phi(\varnothing)=1$ and
  $\Phi(\tau)$ the elementary weight $\sum_jb_j\Phi_j(\tau)$ (Eqs. (13)–(16)).

Equating the two to $\lvert\tau\rvert\le p$ gives the
[order conditions](/results/runge-kutta-order-conditions.md).

**Internal weights as vectors.** [Zhang (2024)](/sources/zhang-2024.md) (§2,
§3.2, Eqs. (5)–(6)) writes the order conditions as
$b^\top\Phi_\cdot(\tau)=1/\gamma(\tau)$, with the vector
$\Phi_\cdot(\tau)=(\Phi_j(\tau))_{j=1}^s$ of Butcher's derivative weights
(assuming $c=A\mathbf 1$). Every tree is generated from $\bullet$ by
*extension* $[\tau]$ (graft onto a new root) and the *rooted sum*
$\tau_1\#\tau_2$ (merge the roots), and the weight vectors follow the same
recursion:

$$\Phi_\cdot(\bullet)=\mathbf 1,\qquad\Phi_\cdot([\tau])=A\,\Phi_\cdot(\tau),\qquad\Phi_\cdot(\tau_1\#\tau_2)=\Phi_\cdot(\tau_1)\odot\Phi_\cdot(\tau_2),$$

with $\odot$ the componentwise product (page-local). An *instruction table*
lists, for each tree of a set, either $\bullet$, an extension of an earlier
tree, or a rooted sum of two earlier trees; it needs exactly one row per tree
and lets all weight vectors of the trees with at most $p$ vertices be computed
in one linear pass that reuses shared subtrees (Def. 5, Table 1, Algorithm 1).
There are $\lvert T_{10}\rvert=1205$ trees with at most 10 vertices
(1, 1, 2, 4, 9, 20, 48, 115, 286, 719 by order). RungeKuttaToolKit orders trees
in reverse lexicographic order of canonical level sequences, which puts bushy
trees last where Butcher's ordering puts them first (Remark 4).

**Map and flow coefficients.** [de León et al. (2025)](/sources/deleon-2025.md)
(§1.2, Eqs. (1)–(3)) distinguish the *map* coefficients $u(\tau)$, the
elementary weights of $y_{n+1}=B(u,y_n)$, from the *flow* coefficients
$v(\tau)$ of the modified vector field $h^{-1}B(v,\cdot)$ that the method
integrates exactly (page-local names); the substitution law below relates
them order by order (Eq. (9), computed with BSeries.jl and SymPy). Methods whose
step is a B-series are **B-series methods**; besides RK methods the sources
treat the average vector field (AVF) method
$y_{n+1}=y_n+h\int_0^1f(\xi y_{n+1}+(1-\xi)y_n)\,d\xi$, whose coefficients
(page-local $a_{\mathrm{AVF}}$) are $a_{\mathrm{AVF}}(\bullet)=1$ and
$a_{\mathrm{AVF}}([\tau_1,\dots,\tau_m])=a_{\mathrm{AVF}}(\tau_1)\cdots a_{\mathrm{AVF}}(\tau_m)/(m+1)$
(§3.2, Eqs. (48)–(50)). BSeries.jl also computes B-series of
Rosenbrock–Wanner methods (§1).

## Composition law

Applying the method with coefficients $a$ and then the method with
coefficients $b$ gives a B-series,

$$B\big(b,B(a,y)\big)=B(a\cdot b,y),\qquad (a\cdot b)(\varnothing)=b(\varnothing),\qquad (a\cdot b)(\tau)=\sum_{s}a(\tau\setminus s)\,b(s_\tau),$$

the sum running over the **ordered subtrees** $s$ of $\tau$: connected vertex
sets containing the root, the empty set included; $s_\tau$ is the tree they
form and $\tau\setminus s$ the forest left after removing them, on which $a$
acts as the product over its trees (Ketcheson & Ranocha (2023), Eqs.
(21)–(23), Def. 2.1, in the formulation of Chartier–Hairer–Vilmart; a tree
with 5 vertices in their Table 3 has 11 ordered subtrees). Rescaling the step to
$\mu h$ (page-local scalar $\mu$) replaces $a(\tau)$ by $\mu^{\lvert\tau\rvert}a(\tau)$. Under this product the RK
methods form a group, the Butcher group (§2.3).

The composition law decides whether a sequence of steps raises the order: two
second-order explicit two-stage methods compose to order exactly two, while
Butcher's main method of order 4 with order-3 starting and finishing methods
composes to order 5 (§2.3.1–2.3.2); see
[processing and effective order](/methods/processing-and-effective-order.md).

## Substitution law

If the vector field $hf$ in a B-series with coefficients $a$ is replaced by a
vector field that is itself a B-series $B(b,\cdot)$ with $b(\varnothing)=0$,
the result is again a B-series,

$$B(b\star a,y):=B\big(a,y\big)\big|_{hf\to B(b,\cdot)},\qquad (b\star a)(\varnothing)=a(\varnothing),\qquad (b\star a)(\tau)=\sum_{p}b(\tau\setminus p)\,a(p_\tau),$$

summed over the $2^{\lvert\tau\rvert-1}$ **partitions** $p$ of $\tau$ (subsets
of its edges): $\tau\setminus p$ is the forest obtained by cutting edges and
$p_\tau$ the **skeleton**, the tree obtained by contracting each tree of the
forest to a vertex (Ketcheson & Ranocha (2023), Eq. (26), Def. 2.2, Table 2,
after Chartier–Hairer–Vilmart Thm. 3.2). Because
$(b\star e)(\tau)=b(\tau)+$ terms in trees of fewer vertices, equations of the
form $b\star e=a$ or $b\star a=e$ are solved tree by tree; this is how
[backward error analysis](/methods/backward-error-analysis.md) computes
modified equations and modifying integrators.

## Energy-preserving B-series

For a Hamiltonian system $y'=\mathcal J\nabla H(y)$ with constant
skew-symmetric $\mathcal J$ (page-local), a B-series vector field preserves $H$
to order $q$ iff it is a combination, over trees $\lvert\tau\rvert\le q$ and
leaves $\ell$ of $\tau$, of $F(\tau)+(-1)^mF(\tau^*(\ell))$, with $m$ the
root-to-leaf distance and $\tau^*(\ell)$ the *energy-preserving conjugate*:
the parent of $\ell$ becomes the root and $\ell$ is reattached to the old root
(page-local $m$, $\ell$;
Celledoni, McLachlan, Owren & Quispel 2010, Thms. 2–3, as quoted by
de León et al. (2025), Theorem 1, Eq. (5), §2.1). Bushy trees and tall
trees with an even number of vertices cannot appear; conjugacy partitions the
trees of each order into classes, one condition per class (Examples 1–3). This
characterization yields the
[pseudo-energy-preserving methods](/methods/pseudo-energy-preserving-runge-kutta.md).

## Generalizations

Additive and partitioned methods for $y'=\sum_\nu f^{[\nu]}$ are expanded over
**colored** rooted trees: a vertex of color $\nu$ contributes $f^{[\nu]}$ to
the elementary differential and the tableau of part $\nu$ to the elementary
weight (N-trees and NB-series of Araújo–Murua–Sanz-Serna, P-trees and
P-series of Hairer, as recalled by Ketcheson & Ranocha (2023), §3.1). Additive
RK methods include partitioned RK methods, and Störmer–Verlet is an additive
RK method with two parts (§3.1.2, Eq. (46)).

**Linearly implicit multistep methods.** [Glandon et al. (2022)](/sources/glandon-2022.md)
(§3.2) use B-series to derive the order conditions of
[linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md), whose
steps contain a Jacobian times a combination of past values. They extend the index set
to $T\cup\{\varnothing\}\cup\{\tau_\circ\}$:

- $F(\varnothing)(y)=y$, and $\tau_\circ$ (page-local) is a single "fat" node with
  $F(\tau_\circ)(y)=Jy$. This term appears in the numerical solution but not in the exact one
  (Eq. (3.9)).
- **Exact solution.** At $t+ch$ the coefficients are $e_c(\varnothing)=1$,
  $e_c(\tau_\circ)=0$ and $e_c(\tau)=c^{\lvert\tau\rvert}/\gamma(\tau)$. The derivative series
  has $\lvert\tau\rvert c^{\lvert\tau\rvert-1}/\gamma(\tau)$ ($e_c$ page-local; Eqs. (3.11a)–(3.11b)).
- **Multiplication by $J$** acts on coefficients as $(Ja)(\tau_\circ)=a(\varnothing)$ and
  $(Ja)([u])=a(u)$ for a tree $u$, i.e. the root has exactly one subtree. All other values are
  zero (Eq. (3.11c), after Butcher).

Every past value and right-hand side of a multistep step is such a series about a common point,
with the step fractions as the $c$'s. Matching the series gives the conditions (Eqs. (3.13)–(3.17)).
Unlike Runge–Kutta conditions, they depend only on $\lvert\tau\rvert$ and on whether the root
has one child or several (§3.2). The exact-Jacobian method therefore needs $2p$ conditions,
against $2p+1$ for its W-variant, which they derive by Taylor expansion (Thm. 3.3, Thm. 3.7,
Remark 3.8). Glandon et al. call B-series "the gold standard approach" to the order conditions of
one-step methods such as Runge–Kutta, Rosenbrock and exponential schemes (§3.2); their
construction carries it over to a multistep method.

**Exponential integrators: the φ-series.** [Dallerit & Tokman (2025)](/sources/dallerit-2025.md)
(§2–3) expand exponential methods for $y'=f(y)$ in B-series with the normalisation above,
with $J_n=f'(y_n)$ and the remainder $r_n(y)=f(y)-f(y_n)-J_n(y-y_n)$ (page-local). Their tools
are the following:

- **Tree partition.** $T_S$ holds the trees with exactly one branch at the root, and
  $T_M=T\setminus T_S$ holds $\bullet$ and the trees with at least two (page-local). Every tree
  of $T_S$ is uniquely $[\tau]_k$, the $k$-fold rooting of some $\tau\in T_M$, and
  $F([\tau]_k)(y_n)=J_n^kF(\tau)(y_n)$ (Lemma 1). The trees of $T_S$ are exactly the
  elementary differentials that a stiff Jacobian amplifies.
- **B-series of the remainder** (Thm. 4). For a point $Y=B(z,y_n)$ with $z(\varnothing)=1$
  (page-local $z$), $h\,r_n(Y)$ is a B-series whose coefficients vanish on $\varnothing$,
  $\bullet$ and $T_S$, and equal $\prod_iz(\tau_i)$ on $\tau=[\tau_1,\dots,\tau_m]\in T_M\setminus\{\bullet\}$.
  Subtracting $hJ_n(Y-y_n)$ removes exactly the $T_S$ coefficients.
- **φ-series of the exact flow** (Thm. 5). Inserting the remainder series into the
  variation-of-constants formula gives
  $y(t_n+h)=y_n+h\phi_1(hJ_n)f(y_n)+\sum_{k\ge3}\phi_k(hJ_n)G_k$. Here $G_k$ (page-local) is
  the B-series supported on the trees of $T_M$ with $k$ vertices, with coefficient
  $k!/\gamma(\tau)$.

Matching these series defines the φ-order conditions of
[stiff order conditions of exponential Runge–Kutta methods](/results/exponential-runge-kutta-stiff-order-conditions.md).
There, φ-order $p$ is shown equivalent to matching the exact B-series on all trees up to
order $p$ and on all $[\tau]_k$ with $\lvert\tau\rvert\le p$ (Thm. 7). The $J$-multiplication
rule is the same one Glandon et al. use for the fat node above *(compiler remark, not in the
sources)*.

Splitting and composition methods built from exact sub-flows are analysed
instead with Lie series: the Baker–Campbell–Hausdorff formula in a Lyndon
basis of the free Lie algebra, words and the shuffle algebra of iterated
integrals, or the word series of Murua–Sanz-Serna, which
[Blanes et al. (2024)](/sources/blanes-2024.md) (§2.2–2.5) present as the
equivalent route for those methods; compositions of a basic method are also
described by trees (§2.5). See
[splitting order conditions](/results/splitting-order-conditions.md).

## Software

[BSeries.jl](/software/bseries-jl.md), built on RootedTrees.jl, computes
truncated B-series of RK, additive RK and ROW methods, composition and
substitution, modified equations and modifying integrators, symbolically or
for a given ODE. Summing the modified-equation coefficients of the explicit
midpoint method to order 9 took about 53 ms against 3.7 s in the Python
package pybs on one Intel Core i7-8700K, a factor of about 70 (Ketcheson &
Ranocha (2023), §4). The same Hopf-algebra structure underlies
renormalization in quantum field theory (§5).

Zhang (2024, §3) evaluates and differentiates the sum of squared order-condition
residuals with instruction tables and bespoke reverse-mode automatic
differentiation in RungeKuttaToolKit. On one thread of an Intel i9-11900KF,
tree enumeration by the Beyer–Hedetniemi successor is 16.3–170.4 times faster
than Mathematica and NodePy for $p=1,\dots,15$, and residual evaluation for
$s=16$, $p\le12$ is on average 47.7 times faster than NodePy and 4.5 times
faster than compiled Mathematica (Figs. 1–2). RootedTrees.jl uses the same
enumeration algorithm with "extremely similar performance" (Remark 5).

## Qualifications

* The order of the factors in the composition product is not uniform in the
  literature. The registry and Ketcheson & Ranocha (2023, Eq. (21)) put the
  first-applied map on the left.
* Ketcheson & Ranocha (2023) define $\tau\setminus p$ as the forest left when
  the edges of $p$ are removed (Def. 2.2), while their Algorithms 1–3 encode
  kept edges as 1 and removed edges as 0; which edges constitute $p$ is
  therefore ambiguous in the paper. The formula above is unaffected if
  $p$ is read as the set of cut edges. Their Algorithm 1 also loops over
  binary sequences of length $\lvert\tau\rvert$ for a tree with
  $\lvert\tau\rvert-1$ edges.

# Citations

- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §2.1–2.4, Eqs. (5), (9)–(26), Defs. 1.1, 2.1, 2.2, Tables 1–3 (trees, B-series, composition and substitution); §3.1–3.2 (colored trees, AVF); §4 (implementation, timings).
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §2.2–2.5 (Lie-series, word and tree descriptions for splitting and composition methods).
- [de León et al. (2025)](/sources/deleon-2025.md) — §1.2 (Eqs. (1)–(3), map and flow), §2 (Theorem 1, Eq. (5)), §2.1 (energy-preserving conjugate, Examples 1–3), §2.3 (Eq. (9)).
- [Zhang (2024)](/sources/zhang-2024.md) — §2 (Proposition 1), §3.1–3.3 (Eqs. (5)–(6), Def. 5, Table 1, Algorithm 1, Remarks 4–5, Figs. 1–2).
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §3.2 (Eqs. (3.9)–(3.17), fat-node tree, Jacobian-times-B-series rule), Thms. 3.3, 3.7, Remark 3.8.
- [Dallerit & Tokman (2025)](/sources/dallerit-2025.md) — §2 (Lemma 1, Defs. 1–3, Thms. 2–3), §3 (Thms. 4–5, $T_S$/$T_M$ partition, φ-series), §5.1 (Thm. 7).
