---
type: Definition
title: "Zero-stability"
description: "A linear multistep method is zero-stable when the roots of its first generating polynomial satisfy the root condition; with variable steps the condition becomes uniform boundedness of products of stability matrices, which holds only under step-ratio restrictions, sharp at 1 + sqrt 2 for variable-step BDF2."
status: established
aliases: [root condition, D-stability, stability at the origin, variable-step zero-stability]
tags: [linear-multistep, stability, step-size-control]
timestamp: 2026-10-19T13:16:00Z
---

# Zero-stability

A [linear multistep method](/methods/linear-multistep-method.md) with first generating
polynomial $\varrho(\zeta)=\sum_{j=0}^k\alpha_j\zeta^j$ is **zero-stable** if every root of
$\varrho$ lies in the closed unit disc and the roots on the unit circle are simple (the *root
condition*; [Glandon et al. (2022)](/sources/glandon-2022.md), §4, as recalled from
Hairer–Nørsett–Wanner). It is the stability of the method for $h\to0$, i.e. for $z=h\lambda=0$.
It does not involve $\sigma$ or the problem's stiffness.
[Akrivis et al. (2024)](/sources/akrivis-2024.md) (§1.3) use it as "zero-stability (hence ODE
stability under a Lipschitz condition)". By Dahlquist's equivalence theorem, a consistent
multistep method converges on Lipschitz problems iff it is zero-stable; one-step methods have
$\varrho(\zeta)=\zeta-1$ and are always zero-stable *(compiler remarks, not stated in the
sources)*.

## Matrix form

Write the method as a one-step recursion for the history vector
$(y_{n+k-1},\dots,y_n)$. For the scalar test equation the step is then multiplication by a
$k\times k$ companion matrix of the characteristic polynomial. At $z=0$ that matrix is the
companion matrix of $\varrho$, and the root condition is equivalent to bounded powers of it.
Glandon et al. (2022, Eq. (4.5)) write this stability matrix for their linearly implicit
methods; at $z=0$ it reduces to multistep zero-stability (§4.1).

## Variable steps

With variable steps the coefficients $\alpha_j$ depend on the step ratios $r_n=h_n/h_{n-1}$.
Each step then multiplies by a different matrix, and zero-stability means that all products of
these matrices are bounded uniformly. Spectral radii of the factors do not decide this: the
spectrum of a product cannot be inferred from them (Glandon et al. 2022, §4.1, citing the
literature on non-uniform grids). The facts the sources state or prove:

- **Smooth grids.** Zero-stability is preserved on grids with $r_n=1+O(h_{\max})$, as
  recalled by Glandon et al. (2022, §4.1) from Söderlind et al.
- **Sufficient norm condition.** If some fixed norm of every admissible stability matrix is at
  most one, all products are bounded. Glandon et al. (2022, Remark 5.6) recall this route from
  Butcher–Heard for BDF2 and BDF3. They report that their two-step Limm-W method satisfies it in
  a weighted 1-norm for all real $z<0$ and all ratios in about $[0.1,1.57]$; the bounds are
  computed, not proved.
- **Ratio and variation bounds.** As recalled by Glandon et al. (2022, Remark 5.7) from
  Ostermann, Thalhammer and Kirlinger, the products are bounded when the ratios are bounded in
  terms of the method's damping at infinity and their variation is controlled.
- **Ratio-invariant $\varrho$.** The Limm and Limm-W methods of Glandon et al. (2022, §4.1, §6)
  have $\alpha_j$ that do not depend on the step ratios, so they are zero-stable on every grid.
- **Variable-step BDF2.** Zero-stability holds for $r_n<1+\sqrt2\approx2.414$, and this bound is
  sharp (Akrivis et al. 2024, §1.3, as recalled from Crouzeix–Lisbona, Grigorieff and
  Hairer–Nørsett–Wanner). The ratio bound of their two-multiplier energy technique,
  $r^\star(\mu_1,\mu_2)$ (the source's $\delta$, $\eta$ are $\mu_1$, $\mu_2$), attains its supremum $1+\sqrt2$ at $(\mu_1,\mu_2)=(1,0)$, i.e. it
  recovers the zero-stability bound (footnote 1, p. 9).

## Zero-stability is not parabolic stability

Zero-stability gives stability for nonstiff ODEs. Stiff and parabolic problems need estimates
uniform in the stiffness, and for variable-step BDF2 these have been proved only under smaller
ratio bounds, for example $r_n\le1.9398$ for the energy estimate of Akrivis et al. (2024,
Thm. 1.1). The bounds bound different quantities; see
[variable-step BDF2 stability](/results/variable-step-bdf2-stability.md).

## Related notions

- **Damping at infinity.** Glandon et al. (2022) require the stability matrix to be strictly
  stable at both $z=0$ and $z=\infty$ (Assumption 5.2). For their two-step Limm, the matrix at
  $z\to-\infty$ has spectral radius at most one iff the step ratio is at least $1/3$ (§4.1).
  See [linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).
- **Stability region.** The stability region of a multistep method is the set of $z$ where the
  roots of $\varrho-z\sigma$ satisfy the root condition (Glandon et al. 2022, Eq. (4.3)); see
  [A-stability](/properties/a-stability.md).

# Citations

- [Glandon et al. (2022)](/sources/glandon-2022.md) — §4 (root condition, Eqs. (4.3), (4.5)), §4.1 (variable-step products, two-step Limm at infinity), Assumption 5.2, Remarks 5.6–5.7, §6.
- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1.3 (zero-stability bound $1+\sqrt2$, sharp), footnote 1 (p. 9), Thm. 1.1.
