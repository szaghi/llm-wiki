---
type: Definition
title: "B-series, composition and substitution laws"
description: "A B-series is a formal expansion over rooted trees of elementary differentials weighted by a coefficient map; Runge–Kutta steps and exact flows are B-series, composition of methods is the Butcher product over ordered subtrees, and substitution of a modified vector field is the law over edge partitions that underlies backward error analysis."
status: established
aliases: [Butcher series, B-series method, Butcher group, composition law, substitution law, NB-series, P-series]
tags: [runge-kutta, order-conditions, geometric-integration]
timestamp: 2026-10-19T12:00:00Z
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
[order conditions](/results/runge-kutta-order-conditions.md). Methods whose
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
$\mu h$ replaces $a(\tau)$ by $\mu^{\lvert\tau\rvert}a(\tau)$. Under this product the RK
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

## Generalizations

Additive and partitioned methods for $y'=\sum_\nu f^{[\nu]}$ are expanded over
**colored** rooted trees: a vertex of color $\nu$ contributes $f^{[\nu]}$ to
the elementary differential and the tableau of part $\nu$ to the elementary
weight (N-trees and NB-series of Araújo–Murua–Sanz-Serna, P-trees and
P-series of Hairer, as recalled by Ketcheson & Ranocha (2023), §3.1). Additive
RK methods include partitioned RK methods, and Störmer–Verlet is an additive
RK method with two parts (§3.1.2, Eq. (46)).

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
