---
type: Result
title: "Negative-coefficient barrier for splitting methods"
description: "Every splitting or composition method with real coefficients and order at least 3 has at least one negative $a_j$ and at least one negative $b_j$, so some sub-flow runs backward in time; the page gives the proof, the consequences for parabolic and irreversible problems, and the three escapes (commutator flows, complex coefficients, processing or effective order)."
status: established
aliases: [order barrier for splitting, Sheng–Suzuki theorem, Goldman–Kaper barrier, backward-step barrier]
tags: [splitting, order-conditions, stability, geometric-integration]
timestamp: 2026-10-19T07:44:00Z
---

# Negative-coefficient barrier for splitting methods

**Theorem** (Sheng 1989, Suzuki 1991, Goldman & Kaper 1996, as recalled by
[Blanes et al. 2024](/sources/blanes-2024.md), §2.6). Let

$$\psi_h=\varphi^{[1]}_{a_{s+1}h}\circ\varphi^{[2]}_{b_sh}\circ\varphi^{[1]}_{a_sh}\circ\dots\circ\varphi^{[2]}_{b_1h}\circ\varphi^{[1]}_{a_1h}$$

be a [splitting method](/methods/operator-splitting.md) with **real** coefficients, built
only from the flows of $f^{[1]}$ and $f^{[2]}$. If $\psi_h$ has order $p\ge3$, then at least
one $a_j$ is negative **and** at least one $b_j$ is negative. The same holds for
[compositions](/methods/composition-methods.md) $\chi_{\gamma_sh}\circ\dots\circ\chi_{\gamma_1h}$
of a basic map with real weights: order $\ge3$ forces a negative $\gamma_j$.

So every real splitting beyond second order integrates some part backward in time, and
Strang splitting is the highest-order method of this class whose sub-steps all move
forward.

## Proof (Blanes & Casas 2005, as given in §2.6)

Write the splitting as the composition of a first-order map $\chi_h=\varphi^{[2]}_h\circ\varphi^{[1]}_h$
and its adjoint with weights $\alpha_1,\dots,\alpha_{2s}$ (page-local), so that
$b_j=\alpha_{2j-1}+\alpha_{2j}$ and $a_{j+1}=\alpha_{2j}+\alpha_{2j+1}$
([composition methods](/methods/composition-methods.md), Eq. 2.18). Order 3 requires,
among the [order conditions](/results/splitting-order-conditions.md), $\sum_j\alpha_j=1$ and
the vanishing of the cubic polynomial (Eq. 2.56)

$$\sum_{j}\alpha_j^3=\sum_j\big(\alpha_{2j-1}^3+\alpha_{2j}^3\big)=0 .$$

The weights are not all zero, so one pair has $\alpha_{2j-1}^3+\alpha_{2j}^3<0$, and
$x^3+y^3<0\Rightarrow x+y<0$ gives $b_j<0$. Regrouping the same sum as
$\alpha_1^3+\sum_j(\alpha_{2j}^3+\alpha_{2j+1}^3)$ gives a negative $a_j$ in the same way.
(The source's regrouped sum is printed with summation index $i$ but summand in $j$, p. 50;
a typographic slip.) For a composition of a symmetric second-order map the order-3
condition is $\sum_j\gamma_j^3=0$ with $\sum_j\gamma_j=1$, which forces a negative weight
directly. Since the RKN order conditions coincide with the general ones up to order 3, the
barrier also binds [RKN splittings](/methods/composition-methods.md) (§2.6).

## Consequences

- **Parabolic and irreversible problems.** A negative step of a diffusion sub-flow is
  ill-posed. For $y'=(L_1+L_2)y$ with $L_1,L_2$ generating $C_0$ semigroups (page-local
  $L_i$), an order-$p$ splitting with all $a_j,b_j\ge0$ converges with order $p$ under
  regularity assumptions (Eq. 6.44, as recalled from Hansen & Ostermann 2009), but the
  barrier caps such methods at $p=2$ (§6.4). Blanes et al. conclude that splitting is no
  longer appropriate for diffusion beyond order 2 except with complex coefficients or
  commutators (§6.2, §6.4).
- **Step-size restriction.** In imaginary-time propagation of a Schrödinger operator (a
  parabolic problem), a method with negative coefficients suffers a step restriction
  proportional to $\Delta x^2$, while positive-coefficient methods are insensitive to the
  mesh (§6.4, Fig. 6.1, $256$ and $512$ grid points).
- **Path-integral Monte Carlo** requires positive $a_j$, so the barrier is binding there
  (§9).
- **Multi-product expansions** $\sum_ic_i(\cdot)$ of positive-weight compositions: each
  composition is at most second order and some $c_i<0$ (§9.1, as recalled from Sheng 1989).
- A related barrier holds outside splitting: Runge–Kutta and multistep methods that
  preserve positivity unconditionally are at most first order (§9.2.1, as recalled from
  Bolley & Crouzeix 1978); see [positivity preservation](/properties/positivity-preservation.md).

## Escapes

1. **Commutator flows.** Adding the flow of a double commutator (in the RKN case a
   "modified potential" built from $\nabla V$) removes the obstruction: the
   Koseleff–Chin fourth-order scheme, which the source calls all-positive, has splitting
   coefficients $a_1=\tfrac16$, $b_1=\tfrac12$, $a_2=\tfrac13$ and commutator coefficient
   $d_2=-\tfrac1{72}$ (§3.2). The escape is
   limited: sixth order with positive coefficients in general again needs negative ones
   (Chin 2005), except for special potentials (a processed sixth-order method for cubic
   potentials, Blanes et al. 2023) (§3.2). For parabolic problems the double commutator
   route is Kieri's (2015) (§6.4).
2. **Complex coefficients** with positive real part avoid backward steps in the real
   direction and give the classical order on analytic semigroups (§6.4, §7); see
   [complex-coefficient splitting](/methods/complex-coefficient-splitting.md).
3. **Effective order.** The barrier concerns classical order. Positive-coefficient kernels
   can reach higher *effective* order by [processing](/methods/processing-and-effective-order.md):
   the Takahashi–Imada action of path-integral Monte Carlo has effective order 4 (§9,
   as recalled).

## Qualifications

- The theorem is stated for real splitting and composition methods without commutator
  flows; Blanes et al. are careful to exclude both commutators (§3.2) and complex
  coefficients (§7). A statement of the barrier "for all splitting methods" is too broad.
- Reynolds et al. phrase the alternative to first-order splitting as higher-order variants
  that "introduce complex arithmetic or backward integration"
  ([Reynolds et al. 2023](/sources/reynolds-2023.md), §1), which covers escapes 2 and the
  barrier itself but not escape 1.

# Citations

- [Blanes et al. (2024)](/sources/blanes-2024.md) — §2.6 (theorem and proof, Eq. 2.56), §3.2 (modified potentials), §6.2–6.4 (parabolic problems, Eq. 6.44, Fig. 6.1), §7 (complex coefficients), §9.1–9.2 (multi-product expansions, positivity), §9 (path-integral Monte Carlo).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1 (higher-order splitting needs complex arithmetic or backward integration).
