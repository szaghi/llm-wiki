---
type: Result
title: "Equivalence of DeC and ADER"
description: "Modern ADER is a deferred-correction scheme with low-order operator Dy − r(y_n), and DeC is an ADER-type Galerkin scheme with characteristic-function test functions; via Abgrall's contraction lemma, ADER with M+1 time nodes and K iterations has order min(M+1, K)."
status: established
aliases: [ADER is DeC, DeC–ADER equivalence, ADER–DeC convergence theorem]
tags: [deferred-correction, ader, order-conditions]
timestamp: 2026-10-20T06:18:00Z
---

# Equivalence of DeC and ADER

[Han Veiga et al. (2021)](/sources/hanveiga-2021.md) show that two iterative,
arbitrarily high-order one-step methods are the same algorithm read in two ways, once
both are restricted to the semi-discrete ODE $y'=f(y)$. The methods are modern
[ADER](/methods/ader-time-integration.md) (a Galerkin-in-time predictor solved by Picard
iteration) and [deferred correction](/methods/deferred-correction.md) in Abgrall's
$\mathcal L^1/\mathcal L^2$ form. Their Conclusion 4.2: "ADER is equivalent to DeC and
vice versa, up to few details. The major difference … is the choice of the test functions
and the resulting iteration matrix." The equivalence transfers DeC's convergence argument
to ADER and yields an order theorem for ADER (Thm. 4.5).

Notation as on the [ADER](/methods/ader-time-integration.md) and
[DeC](/methods/deferred-correction.md) pages ($\mathcal D$, $\mathbf r$, $\ell_m$,
$\omega_{mr}$, $c_m$ page-local there; $\mathsf M$ and $K$ from the registry), with
$f=-F$ relative to the source.

## ADER is DeC (§4.1)

Choose the operators

$$\mathcal L^2(\mathbf Y)=\mathcal D\mathbf Y-\mathbf r(\mathbf Y),\qquad
\mathcal L^1(\mathbf Y)=\mathcal D\mathbf Y-\mathbf r(y_n,\dots,y_n)\qquad\text{(24)},$$

where $\mathcal L^1$ evaluates the right-hand side at the constant initial state. The
DeC update
$\mathcal L^1(\mathbf Y^{(k)})=\mathcal L^1(\mathbf Y^{(k-1)})-\mathcal L^2(\mathbf Y^{(k-1)})$
then reduces to $\mathcal D\mathbf Y^{(k)}=\mathbf r(\mathbf Y^{(k-1)})$, which is exactly
the ADER Picard iteration. The choice of $\mathcal L^1$ is "not really unique". It is made
so that $\mathcal L^1-\mathcal L^2$ is Lipschitz with a constant $O(h)$. The analysis uses
the normalized pair

$$\mathcal L^1(\mathbf Y)=\mathbf Y-\mathcal D^{-1}\mathbf r(y_n,\dots,y_n),\qquad
\mathcal L^2(\mathbf Y)=\mathbf Y-\mathcal D^{-1}\mathbf r(\mathbf Y)\qquad\text{(25)/(30)}.$$

## DeC is ADER (§4.2)

Line $m$ of DeC's high-order operator,
$Y_m-Y_0=h\sum_r\omega_{mr}f(Y_r)$, is a Galerkin weak form in time with the
characteristic function $\psi_m=\chi_{[t_{n,0},t_{n,m}]}$ as test function:

$$\int_{t_n}^{t_{n+1}}\psi_m\,y'\,dt=\int_{t_n}^{t_{n+1}}\psi_m\,f(y)\,dt\qquad\text{(29)},$$

with $f$ replaced by its Lagrange interpolant on the subnodes. ADER uses the same weak
form with $\psi_m=\ell_m$ and integrates by parts in time. DeC cannot do so, because its
test functions are discontinuous. The two methods therefore differ only in the test
functions, and hence in the iteration matrix: $\mathcal D$ for ADER, the identity with
interpolation weights for DeC.

## Order of ADER (§4.3)

Abgrall's DeC proposition needs three conditions:
(C.1) $\mathcal L^1$ is coercive;
(C.2) $\mathcal L^1-\mathcal L^2$ is Lipschitz with constant proportional to $h$;
(C.3) $\mathcal L^2=0$ has a unique solution $\mathbf Y^*$.
For the ADER operators (30):

- **Proposition 4.3.** For states with equal initial value,
  $\lVert\mathcal L^1(\mathbf Y)-\mathcal L^1(\mathbf Z)\rVert=\lVert\mathbf Y-\mathbf Z\rVert$:
  coercive with constant 1.
- **Proposition 4.4.** The difference
  $(\mathcal L^1-\mathcal L^2)(\mathbf Y)-(\mathcal L^1-\mathcal L^2)(\mathbf Z)=\mathcal D^{-1}\big(\mathbf r(\mathbf Y)-\mathbf r(\mathbf Z)\big)$
  is bounded by $h\,C_{\mathcal D}C_{\mathbf r}\lVert\mathbf Y-\mathbf Z\rVert$. Here
  $C_{\mathbf r}$ comes from bounded basis functions and weights and a Lipschitz $f$, and
  $C_{\mathcal D}$ bounds $\lVert\mathcal D^{-1}\rVert$ independently of $h$ (page-local
  constants; the source's $C_r$, $C_M$, product $\beta$).
- (C.3) is assumed, not proved.

**Theorem 4.5 (convergence of ADER–DeC).** With operators (30) in the DeC algorithm, ADER
with $\mathsf M+1$ time nodes and $K$ iterations has order of accuracy
$\min(\mathsf M+1,K)$. With $C_{\mathrm L}=C_{\mathcal D}C_{\mathbf r}$,

$$\lVert\mathbf Y^{(K)}-\mathbf Y^{\mathrm{ex}}\rVert\le C^*\Big(h^{\mathsf M+1}+(C_{\mathrm L}h)^K\Big),$$

because each iteration contracts the distance to $\mathbf Y^*$ by $C_{\mathrm L}h$ (eqs.
(34)–(36)), and $\lVert\mathbf Y^*-\mathbf Y^{\mathrm{ex}}\rVert=O(h^{\mathsf M+1})$.
Han Veiga et al. present this as extending Jackson's result to the nonlinear setting. Jackson
showed that for linear homogeneous systems a finite number of iterations suffices. Here the
number of iterations equals the desired order. In practice $K=\mathsf M+1$ is used, the same
count as DeC.

## Consequences stated or shown in the source

- Explicit ADER and explicit DeC have identical linear stability regions for every node
  family tested (§5.1, Fig. 2). This is consistent with both being polynomial methods of degree
  $K$ and order $K$ in $z=h\lambda$ (compiler check on the
  [DeC page](/methods/deferred-correction.md)). For the DeC side the check is now a theorem:
  every bDeC method of order $K$, and its interpolating variants, has
  $R(z)=\sum_{j\le K}z^j/j!$ for any subnodes ([Micalizzi & Torlo 2024](/sources/micalizzi-2024.md),
  Thm. 6.1). The DeC of Han Veiga et al., with forward Euler from $t_n$ in $\mathcal L^1$, is
  the bDeC member of the family of Micalizzi & Torlo *(compiler remark, not in the sources)*.
- The equivalence carries over to the stiff variants. Implicit ADER is DeC with a
  Newton-type $\mathcal L^1$ that couples $\mathcal D$ and the source Jacobian. IMDeC is DeC
  with a node-wise linearized $\mathcal L^1$ (§4.4).
- Both methods are, for fixed $K$, Runge–Kutta methods (Remark 3.2 for DeC). The
  equivalence also covers residual-distribution, space–time DG and spectral-difference
  versions written out in §4.5.

## The converged implicit predictor

[Popov (2024)](/sources/popov-2024.md) (Introduction) restates the conclusion of Han Veiga et
al. that explicit ADER is a special interpretation of DeC, and that DeC competes with ADER and
is easier to implement. His own solver iterates the Gauss–Legendre predictor to convergence
(Picard or Newton), so the DeC iteration count plays no role: the step is the fixed point
$\mathbf Y^*$ of (C.3), an implicit Runge–Kutta method (see
[ADER](/methods/ader-time-integration.md)). Two consequences for the equivalence
*(compiler checks, not in the sources)*:

- **End-of-step value.** Han Veiga et al. extrapolate the predictor to $t_{n+1}$; Popov
  integrates $f$ with the Gauss weights. Summing the rows of $\mathcal D\mathbf Y=\mathbf r(\mathbf Y)$,
  with $\sum_m\ell_m\equiv1$, gives $\sum_l\ell_l(1)Y_l=y_n+h\sum_lw_lf(Y_l)$ at the fixed
  point, so the two updates agree for the converged predictor and differ only after finitely
  many iterations.
- **Order of the fixed point.** Popov's fitted nodal orders $2\mathsf M+1$ with
  $\mathsf M+1$ Gauss–Legendre nodes, up to $\mathsf M=60$ (Tables 1–6), are numerical
  evidence that the converged predictor exceeds the $\mathsf M+1$ of Theorem 4.5, in line
  with the sharpness qualification below.

## Qualifications

- **Local versus global order.** Theorem 4.5 bounds the error of one step started from
  exact data. The paper does not argue the passage to global order explicitly. The standard
  DeC argument (local error $O(h^{K+1})$, global $O(h^K)$) is consistent with the claim
  *(compiler note)*.
- **Sharpness.** $\mathsf M+1$ is the order of the converged predictor only for nodes without
  quadrature superconvergence. With Gauss–Lobatto or Gauss–Legendre nodes the converged
  problem has higher order, so $\min(\mathsf M+1,K)$ is a lower bound (see
  [deferred correction](/methods/deferred-correction.md), Qualifications). The source itself
  says the order "depends on the used quadrature rule" (§2). Popov's (2024) fitted nodal
  order $2\mathsf M+1$ for the converged Gauss–Legendre predictor supports this.
- **Printed slips** (arXiv v3). The proof of Proposition 4.3 cites definition (24), but the
  identity holds for the normalized (30), which §4.3 adopts. With (24) the difference is
  $\mathcal D(\mathbf Y-\mathbf Z)$. Eq. (34) writes the coercivity constant as a factor
  where its inverse is meant (harmless, the constant is 1). Eq. (28) prints $\ell_m$ for
  $\ell_r$ inside the sum over $r$.

# Citations

- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §3 (Prop. 3.1); §4.1 (eqs. (24)–(25), Remark 4.1); §4.2 (eqs. (26)–(29), Conclusion 4.2); §4.3 (C.1–C.3, Props. 4.3–4.4, Thm. 4.5, eqs. (30)–(36)); §4.4; §5.1 (Fig. 2); §6.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — Thm. 6.1 (stability function of bDeC); §3 (bDeC as the forward-Euler DeC).
- [Popov (2024)](/sources/popov-2024.md) — Introduction (DeC and ADER); §1.1 (Eqs. (11)–(13)); §2.1 (Tables 1–6).
