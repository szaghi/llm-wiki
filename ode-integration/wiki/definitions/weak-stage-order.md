---
type: Definition
title: "Weak stage order"
description: "The weak stage order $q_{\\mathrm w}$ of a Runge–Kutta method is the largest $q$ with $b^\\top A^j\\tau^{(k)}=0$ for all $j<s$ and $k\\le q$: the weights are orthogonal to the $A$-invariant space of the stage-order residuals. It removes order reduction on linear problems and, unlike stage order, is reachable by DIRK and explicit methods."
status: established
aliases: [WSO, parabolic order conditions, pseudostage order, BPR-consistency]
tags: [runge-kutta, order-conditions, order-reduction, stiff]
timestamp: 2026-10-19T07:44:00Z
---

# Weak stage order

Let $(A,b,c)$ be an $s$-stage [Runge–Kutta method](/definitions/runge-kutta-method.md)
with $c=A\mathbf 1$, and let $\tau^{(k)}=Ac^{k-1}-c^k/k$ be its $k$-th stage-order
residual (so $\tau^{(1)}=0$). The **weak stage order** $q_{\mathrm w}$ is the largest
integer $q$ for which

$$b^\top A^j\tau^{(k)}=0,\qquad 0\le j\le s-1,\quad 1\le k\le q,$$

and $q_{\mathrm w}=\infty$ if this holds for every $q$
([Biswas et al. 2024](/sources/biswas-2024.md), Def. 1.1, where the set of
conditions is called $S(q)$; [Biswas et al. 2023](/sources/biswas-2023.md),
Def. 3.1; [Biswas et al. 2025](/sources/biswas-2025.md), §1.3). It is a relaxation of
[stage order](/definitions/stage-order.md): stage order $q$ asks the residuals
themselves to vanish, weak stage order only asks them to be invisible to the
weights after any number of multiplications by $A$. Hence $q\le q_{\mathrm w}$ for
every method (Biswas et al. 2024, §1, §2.2). Its purpose is to suppress
[order reduction](/definitions/order-reduction.md) for stiff linear problems in
method classes that cannot have high stage order: diagonally implicit methods have
$q\le2$ and explicit ones $q\le1$, yet both can have high $q_{\mathrm w}$.

## Equivalent formulations

Let $\mathcal K_m$ be the smallest $A$-invariant subspace containing
$\tau^{(1)},\dots,\tau^{(m)}$, i.e. the span of $A^j\tau^{(k)}$, $0\le j\le s-1$,
$1\le k\le m$, and $\mathcal Y$ the smallest $A^\top$-invariant subspace containing
$b$, the span of $(A^\top)^jb$, $0\le j\le s-1$. The following are equivalent
statements of $q_{\mathrm w}\ge q$:

1. $b\perp\mathcal K_q$ (Biswas et al. 2023, Def. 3.1).
2. There is an $A$-invariant subspace $V$ containing $\tau^{(1)},\dots,\tau^{(q)}$ with
   $b^\top v=0$ for all $v\in V$ (Biswas et al. 2023, Def. 3.2, stated equivalent to 1).
3. $\mathcal Y\perp\mathcal K_q$; consequently $\dim\mathcal Y+\dim\mathcal K_q\le s$
   (Biswas et al. 2024, Lemma 3.4, Eq. (14)). This orthogonality of two invariant
   subspaces is the starting point of every
   [weak-stage-order barrier](/results/weak-stage-order-barriers.md).
4. $b^\top(I-zA)^{-1}\tau^{(k)}=0$ for all $z\in\mathbb C$ and $1\le k\le q$
   (Biswas et al. 2025, Eq. (1.3), as recalled from Ketcheson, Seibold, Shirokoff and
   Zhou 2020, Thm. 2). The Neumann coefficients of this rational function are
   $b^\top A^j\tau^{(k)}$, and by Cayley–Hamilton powers $j\ge s$ are combinations
   of lower ones *(compiler check, not in the sources)*.

For an explicit method $A$ is nilpotent and the conditions are simply
$b^\top A^j\tau^{(k)}=0$ for all $j\ge0$ (Biswas et al. 2025, §1.3).

In the same language, a method has stage order $q$ iff $\dim\mathcal K_q=0<\dim\mathcal K_{q+1}$
(Biswas et al. 2024, §3.1). Weak stage order replaces "$\mathcal K_q=\{0\}$" by
"$\mathcal K_q$ is orthogonal to $b$".

## Why it removes order reduction

On the [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
$y'=\lambda(y-g(t))+g'(t)$, with $z=h\lambda$, the local error of a Runge–Kutta step
is (Biswas et al. 2024, Eq. (9))

$$-\sum_{k\ge1}\frac{h^k}{(k-1)!}\,W_k(z)\,g^{(k)}(t_n)+\mathcal O(h^{p+1}),\qquad W_k(z):=z\,b^\top(I-zA)^{-1}\tau^{(k)},$$

where $g$ is the smooth exact solution and $W_k$ is page-local. For $|z|$ large the
expansion of $(I-zA)^{-1}$ produces $b^\top A^{-j}\tau^{(k)}$, $j\ge1$, with negative powers
of $A$, which the classical order conditions do not annihilate; this is the
mechanism of order reduction (Biswas et al. 2023, §2, Eqs. (8)–(14)). Weak stage
order $q_{\mathrm w}$ makes $W_k\equiv0$ for $k\le q_{\mathrm w}$, so the local
error is $\mathcal O(h^{q_{\mathrm w}+1})$ uniformly in $z$. Biswas et al. (2024,
§2.2) call it the least restrictive condition guaranteeing $W_k\equiv0$, and Biswas
et al. (2023, §3) "the most general criterion" for this, both citing Ketcheson et
al. (2020). Biswas et al. (2024, §2.3) add that the conditions, originally derived
only for SDIRK methods, are necessary for any Runge–Kutta method to avoid order
reduction on this problem.

**Relation to the Ostermann–Roche condition.** Ostermann and Roche's condition,
as recalled by Biswas et al. (2024, Eq. (11)) and Biswas et al. (2023, Eq. (29)),
is

$$\frac{k\,b^\top(I-zA)^{-1}\tau^{(k)}}{R(z)-1}\equiv0,\qquad 1\le k\le r,$$

with $r$ page-local. Under technical assumptions it yields the rate
$\min\{p,\,r+2+\bar\nu\}$ for linear parabolic problems, $\bar\nu$ a page-local
problem-dependent number (Biswas et al. 2024, §2.3). Biswas et al. (2023, §6) say
this condition is "(essentially) implied" by weak stage order $r$. Convention
difference: Biswas et al. (2023) name the Ostermann–Roche function $W_k$, Biswas et
al. (2024) reserve $W_k$ for $z\,b^\top(I-zA)^{-1}\tau^{(k)}$ and write the
Ostermann–Roche one with a tilde; this page follows Biswas et al. (2024).

Biswas et al. (2024, §2.2) further state that the convergence theorems of
Alonso-Mallo and Palencia for linear problems generated by a $C_0$-semigroup,
formulated with stage order, use only the weak-stage-order conditions in their
proofs, so that weak stage order is relevant for wave-type problems too; the
reinterpretation is asserted, not re-proved. They also recall Montijano's necessary
condition $b^\top A^{-1}c^j=1$, $0\le j\le r$, for order-$r$ convergence on the
Prothero–Robinson problem.

## History and names

The conditions predate the name; Biswas et al. (2024, §1; 2025, §1.3) recall:

- Scholz derived them for SDIRK and Rosenbrock methods, with order barriers.
- Ostermann and Roche introduced them as the *parabolic order conditions* of
  [Rosenbrock](/methods/rosenbrock-wanner-method.md) and Runge–Kutta methods,
  with fractional convergence orders.
- Skvortsov called the property *pseudostage order* and built DIRK and explicit
  methods with $q_{\mathrm w}=2,3$.
- Rang called it *BPR-consistency*.
- Rosales et al. and Ketcheson et al. (2020) coined *weak stage order* and built
  DIRK schemes through the **eigenvector criterion**: each $\tau^{(k)}$ an
  eigenvector of $A$. This criterion caps invertible-$A$ DIRK schemes at
  $q_{\mathrm w}\le3$ ([barriers](/results/weak-stage-order-barriers.md)).
- Roberts and Sandu extended the notion to
  [GARK methods](/methods/generalized-additive-runge-kutta.md).

The Rosenbrock analogue is Scholz's pair of Prothero–Robinson conditions
$C_2(H)=C_3(H)=0$, which [Steinebach (2023)](/sources/steinebach-2023.md), §2,
imposes on [Rodas5P](/methods/rodas5p.md); Steinebach notes, citing Ostermann and
Roche, that the same conditions arise for semi-discretized parabolic problems.

## Interaction with the order conditions

Weak stage order makes some classical [order conditions](/results/runge-kutta-order-conditions.md)
redundant. Writing the Butcher-form residuals page-locally as
$\varrho_{i,k}=b^\top A^{i-k}c^k-k!/(i+1)!$, Biswas et al. (2023, §3) show

$$b^\top A^j\tau^{(k)}=\varrho_{j+k,\,k-1}-\tfrac1k\,\varrho_{j+k,\,k},$$

so with $q_{\mathrm w}=p$ or $p-1$ exactly $(p-1)(p-2)/2$ order conditions drop out:
1 of 4 for $p=3$, 3 of 8 for $p=4$, 6 of 17 for $p=5$ (Table 2). In the other
direction, Biswas et al. (2025, Eq. (3.2)) state, without proof, that
$q_{\mathrm w}\ge p-1$ together with the quadrature conditions $b^\top c^{j-1}=1/j$,
$j\le p$, implies all "palm-tree" conditions
$b^\top A^kc^j=1/\big((k+j+1)\cdots(j+1)\big)$, $0\le j+k\le p-1$; for $p\le3$
every order condition is of that kind.

Weak stage order also constrains the [stability function](/definitions/stability-function.md):
$\deg N,\deg D\le\dim\mathcal Y\le s-\dim\mathcal K_{q_{\mathrm w}}$ for
$R=N/D$ (Biswas et al. 2024, Thm. 3.8, Lemma 3.4). For explicit methods it forces
the highest $q_{\mathrm w}-1$ coefficients of the stability polynomial to vanish, the
dual of order $p$ fixing the first $p+1$ (Biswas et al. 2025, §7).

## Which methods have it

- **Generic methods.** Almost all irreducible schemes not designed for it have
  $\dim\mathcal Y=s$, hence $\mathcal K_{q_{\mathrm w}}=\{0\}$ and weak stage order
  equal to stage order; the exceptions noted are explicit methods with a zero first
  subdiagonal entry, such as the eighth-order Prince–Dormand method and some
  fifth-order SSP methods of Ruuth and Spiteri (Biswas et al. 2024, §3.1).
- **Explicit methods.** Explicit Euler has $q_{\mathrm w}=\infty$; any explicit
  method with $p>1$ has $\tau^{(2)}\neq0$; SSPRK3, classical RK4 and Dormand–Prince 5
  have $q_{\mathrm w}=1$ (Biswas et al. 2025, §1.3, §2.1, Table 3.2). Explicit
  methods of every $q_{\mathrm w}$ exist:
  [explicit Runge–Kutta methods with high weak stage order](/methods/explicit-runge-kutta-high-weak-stage-order.md).
- **Diagonally implicit methods.** Despite stage order $\le2$,
  [DIRK schemes](/methods/diagonally-implicit-runge-kutta.md) with
  $q_{\mathrm w}=4,5$ have been constructed:
  [DIRK schemes with high weak stage order](/methods/dirk-high-weak-stage-order.md).
- **Gauss methods** attain the general bound of Biswas et al. (2024, Ex. 7.4); see
  [fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md).

## Qualifications

- **Linear problems only.** The guarantee holds for linear problems; Biswas et al.
  (2024) state it for "time-independent operators" in the abstract and §8, but §1.1
  says "linear (possibly time-dependent)". This page records only the
  time-independent case as established. Biswas et al. (2023, §7.1) find order
  reduction practically removed for a slowly varying diffusion coefficient
  ($\cos(0.1t+0.2)$) and not removed for a rapidly varying one
  ($1+0.5\cos(30t+0.1)$).
- **Nonlinear problems.** High weak stage order gives third-order convergence on
  viscous Burgers (Biswas et al. 2023, §7.2, methods of order 4–5) and on inviscid
  Burgers (Biswas et al. 2025, §5.2), versus second order for $q_{\mathrm w}=1$; on
  Van der Pol with $\mu=500$ it does not remove order reduction (Biswas et al. 2023,
  §7.3). No nonlinear theory exists in these sources.
- **Derivatives of the solution.** On initial-boundary-value problems
  $q_{\mathrm w}=p-1$ recovers order $p$ in the solution but can lose order in its
  spatial derivative; $q_{\mathrm w}=p$ fixes both (Biswas et al. 2023, §6;
  Biswas et al. 2025, §5.1).
- Biswas et al. (2025, §3) state that high-$q_{\mathrm w}$ methods "typically"
  converge at $\min(p,q_{\mathrm w}+1)$ on linear PDEs and $\min(p,q_{\mathrm w})$ on
  ODEs; both are empirical statements there.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — §2 Eqs. (5)–(14); §3 Defs. 3.1–3.2, Tables 1–2; §6 Eq. (29); §7.
- [Biswas et al. (2024)](/sources/biswas-2024.md) — §1, Def. 1.1; §2.2–2.3 Eqs. (9), (11); §3.1 Lemma 3.4; Thm. 3.8.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1.3 Eq. (1.3); §2.1; Eq. (3.2); Table 3.2; §5; §7.
- [Steinebach (2023)](/sources/steinebach-2023.md) — §2, Scholz's conditions (2.5)–(2.13).
