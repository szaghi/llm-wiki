---
type: Method
title: "Energy-stable WENO (ESWENO) with summation-by-parts boundary closures"
description: "WENO finite differences recast as a summation-by-parts operator plus a design-order artificial dissipation that makes the nonlinear scheme provably L2-stable for linear hyperbolic systems, with boundary closures on non-uniform flux points that keep WENO stencil biasing up to the boundary."
status: established
aliases: [ESWENO, energy stable WENO, SBP-WENO, summation-by-parts WENO, ESWENO3-4-3, ESWENO2-4-2]
tags: [weno, finite-difference, boundary-treatment, stability, summation-by-parts, nonlinear-weights]
timestamp: 2026-10-08T00:00:00Z
---

# Energy-stable WENO (ESWENO) with summation-by-parts boundary closures

**Motivation** ([Fisher et al. (2011)](/sources/fisher-2011.md), §1).
Conventional WENO has no energy estimate: the symmetric part of its
nonlinear operator can have eigenvalues in the right half-plane. Near
boundaries it uses ad hoc closures. Discarding stencils that leave the
domain cuts local accuracy from $2p$ to $p + 1$, ghost points tie the
closure to particular boundary conditions, and Shen et al.'s wall
treatment drops a fifth-order scheme to fourth. Most implementations rely on low-order
closures for robustness. A boundary closure must be inward-biased,
stable and accurate *for every combination of candidate stencils* the
weights can select.

**Summation by parts (SBP).** A derivative operator
$\mathsf D = \mathsf P^{-1}\mathsf Q$ with $\mathsf P$ symmetric positive
definite (the norm) and $\mathsf Q + \mathsf Q^{\mathsf T}$ zero except
at the two corner entries mimics integration by parts. With boundary
data imposed weakly by a penalty term (SAT), the energy
$u^{\mathsf T}\mathsf P u$ is bounded, which is $L^2$ stability. Two kinds of
norm matter.
* *Diagonal* norms also give stability proofs for variable coefficients
  and some nonlinear forms. Their boundary stencils are limited to order
  $p$, so a $2p$-order interior gives global order $p + 1$.
* *Block* norms admit boundary order $2p - 1$, which keeps global order
  $2p$ ([Fisher et al. (2011)](/sources/fisher-2011.md), §§2.1, 3.1).

**Construction** (Yamaleev and Carpenter's periodic ESWENO, extended
to finite domains by [Fisher et al. (2011)](/sources/fisher-2011.md), §§2–4).
1. **Target.** A non-dissipative fourth-order central SBP operator.
2. **Dual grid.** The target is recast in WENO form, with solution
   points $x_j$ and flux points between them. Near each boundary the
   flux points must be *non-uniform*. Their positions are fixed by the
   norm $\mathsf P$ (Lemma 1), which is what lets SBP, accuracy and stencil
   biasing hold together.
3. **Biasing.** Three two-point candidate fluxes (L, C, R; plus LL, RR
   near diagonal-norm boundaries) are combined with WENO-Z-type
   weights (eqs. 13, 19, checked on the page image):
   $$\tilde\omega_k = d_k\left(1 + \frac{\tau}{\varepsilon + \beta_k}\right),\quad \beta_{\mathrm L} = (f_j - f_{j-1})^2,\ \beta_{\mathrm C} = (f_{j+1} - f_j)^2,\ \beta_{\mathrm R} = (f_{j+2} - f_{j+1})^2,\quad \tau = \left(-f_{j-1} + 3f_j - 3f_{j+1} + f_{j+2}\right)^2.$$
   Here $\tau$ is the squared third undivided difference, which is
   one-sided toward the interior next to the boundaries. As in
   [WENO-Z](/methods/weno-z.md), the weights tend to $d_k$ quickly.
   A modified downwind indicator keeps the downwind weight below the
   others. Indicators use the characteristic solution variables rather
   than fluxes, which was found best in practice.
4. **Energy stabilization.** Decompose the WENO operator's symmetric
   part into the SBP dissipation form: $\mathsf P^{-1}$ times a sum of
   diagonal matrices sandwiched between powers of the difference
   operator. Its diagonal entries can be negative, so a smooth, design-order
   artificial-dissipation term of the same form is added to make each
   entry non-negative. The resulting ESWENO operator satisfies an $L^2$
   energy estimate for constant-coefficient linear systems.

**Accuracy conditions** ([Fisher et al. (2011)](/sources/fisher-2011.md), §5;
eqs. 41–42, checked on the page images). Fourth order holds if
$\omega_k - d_k = O(h^3)$. When $f' \neq 0$, $\beta_k = (f'h)^2 + O(h^3)$
and $\tau = O(h^6)$, so $\omega_k - d_k = O(h^4)$. At a critical point
with any number of vanishing derivatives the bound used is
$\tau/(\varepsilon + \beta_k) \le \tau/\varepsilon$, which needs
$$O(h^3) \le \varepsilon \le O(h^2).$$
With only $\varepsilon > 0$ imposed, the order can drop from four to
two (Remark, §5.2). The implementation recipe instead sets
$\varepsilon = \max\left(\Vert f_0\Vert, \Vert f'_0\Vert\right)h^4$
with $h = 1/N$ (eq. 75, read from the page image), which lies below
the lower end of that range. The paper does not reconcile the two, and
its accuracy tests do not isolate a critical point. This is recorded
here as an unresolved internal tension of the source, not as a
contradiction between sources. Compare $\varepsilon \sim h^2$ for
WENO-Z ([accuracy at critical points](/properties/accuracy-at-critical-points.md)).

**Evidence** ([Fisher et al. (2011)](/sources/fisher-2011.md), §6).
* For a convected square wave, plain WENO with the new closures has
  eigenvalues in the right half-plane, and the stabilization moves them
  to the left.
* Design order is reached: three for the diagonal-norm ESWENO2-4-2 and
  four for the block-norm ESWENO3-4-3. This holds on linear advection,
  subsonic and transonic quasi-1D nozzles, and the 2D
  [isentropic vortex](/benchmarks/isentropic-vortex.md) with SAT
  boundaries.
* A square wave crossing in and out of the domain stays sharp and
  non-oscillatory.
* The diagonal-norm closure diverges without the stabilization, and
  the block-norm one survives without it. The authors conclude it
  should always be included.
* A reacting supersonic hydrogen–air mixing layer shows
  Kelvin–Helmholtz roll-up with shocks, with no extra filtering.

**Later uses (batch 6).** The weights of Yamaleev and Carpenter's
*third-order* energy-stable scheme, without its stabilizing dissipation,
improve third-order WENO ("WENO+3"):
$\tilde\omega_k = d_k\left(1 + \tau/(\varepsilon + \beta_k)\right)$ with
$\tau = (\delta^2 f_i)^2$ and $\varepsilon = h^2$, quoted as required to avoid
accuracy loss at critical points
([Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §3.2.1).
A point-value version, with linear weights $\tfrac34, \tfrac14$, serves
fourth-order finite volume ([Berta et al. (2024)](/sources/berta-2024.md), §3.2).
Both sit at the $O(h^2)$ end of the window above.

# Citations

1. [Fisher et al. (2011)](/sources/fisher-2011.md), §§1–7 and Appendices A–B (eqs. 13, 19, 41–42, 73–75 read from the page images).
2. [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-2010.md), §3.2.1 (arXiv v2).
3. [Berta et al. (2024)](/sources/berta-2024.md), §3.2 (arXiv v4).
