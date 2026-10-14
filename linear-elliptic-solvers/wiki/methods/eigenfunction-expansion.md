---
type: Method
title: "Eigenfunction expansion"
description: "Solution of L u = f, or of the shifted problem L u - mu w u = f, for a Hermitian operator by expanding u in its orthonormal eigenfunctions, which yields the Green's function as the bilinear series sum phi_n(x) conj(phi_n(x'))/(lambda_n - mu) and the solvability condition when mu is an eigenvalue."
status: established
aliases: [superposition of eigenfunctions, spectral method for BVPs, bilinear expansion, eigenfunction series]
tags: [operator-theory, greens-function, eigenproblem]
timestamp: 2026-10-14T00:00:00Z
---

# Eigenfunction expansion

**Method.** Let $\mathcal L$ be [Hermitian](/definitions/hermitian-operator.md)
under the boundary conditions of the problem, with orthonormal
eigenfunctions $\mathcal L\phi_n=\lambda_nw\phi_n$. To solve
$\mathcal Lu=f$ under the same conditions, expand $u=\sum_nc_n\phi_n$
(completeness, assumed); linearity removes all derivatives,
$f=\sum_nc_n\lambda_nw\phi_n$, and orthogonality gives
$$c_n=\frac{1}{\lambda_n}\int_a^b\bar\phi_n(x')f(x')\,\mathrm dx'\quad\text{(eqs. 17.44–17.49, normalised form)}$$
([Riley et al. (2006)](/sources/riley-2006.md), §17.5, pp. 569–570).
Interchanging sum and integral (assumed),
$$u(x)=\int_a^bG(x,x')f(x')\,\mathrm dx',\qquad G(x,x')=\sum_n\frac{\phi_n(x)\bar\phi_n(x')}{\lambda_n}\quad\text{(eqs. 17.50–17.51)},$$
so $G(x,x')=\overline{G(x',x)}$ (eq. 17.52). $G$ depends only on
$\mathcal L$ and its boundary conditions and serves every right-hand side;
it coincides with the [Green's function](/definitions/greens-function.md)
defined by $\mathcal LG=\delta(x-x')$. A zero eigenvalue makes the series
undefined; the book does not discuss that case for $\mu=0$.

[Arfken et al. (2013)](/sources/arfken-2013.md) derive the same series for
unit weight by expanding $G(x,x')=\sum_{n,m}g_{nm}\phi_n(x)\bar\phi_m(x')$
together with the closure relation for $\delta(x-x')$, which forces
$g_{nm}=\delta_{nm}/\lambda_n$ (§10.1, eqs. 10.10–10.14, pp. 449–450). They
too set aside a zero eigenvalue ("we shall not pursue that special case"),
judge the series of "dubious value as a computational tool", and value it
for exhibiting the symmetry $G(x,x')=\overline{G(x',x)}$ (eq. 10.15) — in
agreement with Riley's "cumbersome". Their exercise 10.1.10 (statement,
p. 458) has the reader recover the closed form $x(1-x')$, $x<x'$, of the
Dirichlet Green's function of $-\mathrm d^2/\mathrm dx^2$ on $[0,1]$ from
$\frac{2}{\pi^2}\sum_n\frac{\sin n\pi x\,\sin n\pi x'}{n^2}$.

**Example** (pp. 570–571). $u''+\tfrac14u=f$, $u(0)=u(\pi)=0$:
$\phi_n=\sqrt{2/\pi}\sin nx$, $\lambda_n=\tfrac14-n^2$, and
$G(x,x')=\frac{2}{\pi}\sum_n\frac{\sin nx\,\sin nx'}{1/4-n^2}$; for
$f=x/2$ the series reproduces $2x-2\pi\sin(x/2)$.

## Shifted problem

For $\mathcal Lu-\mu wu=f$ with fixed $\mu$ (§17.6, eq. 17.53), the same
steps give
$$c_n=\frac{\langle\phi_n,f\rangle}{\lambda_n-\mu},\qquad G(x,x')=\sum_n\frac{\phi_n(x)\bar\phi_n(x')}{\lambda_n-\mu}.$$
If $\mu=\lambda_n$, $G$ is infinite and no solution exists unless
$\int_a^b\bar\phi_nf\,\mathrm dx=0$ (p. 573) — the book states this
necessary condition but not what the solution set is when it holds.
Arfken et al. give the same shifted series in two and three dimensions,
"well-defined only if the parameter [$\mu$] is not equal to any of the
eigenvalues", and say nothing of the resonant case (§10.2,
eqs. 10.38–10.39, pp. 460–461). For a
continuous spectrum the sum becomes an integral over the spectral parameter
(p. 573).

**PDEs.** The same construction gives
$G(\mathbf r,\mathbf r')=\sum_n\phi_n(\mathbf r)\bar\phi_n(\mathbf r')/\lambda_n$
for a Hermitian partial differential operator (eq. 21.79, §21.5.1), which
Riley et al. call "very cumbersome" for PDEs and do not pursue (p. 753);
Arfken et al. list it among the general properties of Hermitian problems in
two and three dimensions (§10.2, item 3, p. 459; eq. 10.37, p. 460).

**Coefficients and truncation** (Arfken et al., §5.1). The coefficients
$c_n=\langle\phi_n,f\rangle$ are those of the orthogonal projection, so a
truncated expansion is the best weighted mean-square approximation with
that many terms (exercise 5.1.4, p. 267). Convergence can be slow: for
the sine expansion of $x^2(\pi-x)$ on $[0,\pi]$ the book reports the first
four coefficients and calls the convergence "not very fast" (Example 5.1.3,
p. 259), and a square wave is reproduced only in the mean,
with deviations at its discontinuities (Example 5.1.6, pp. 262–264).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17.5 (pp. 569–571), §17.6
  (pp. 572–573), §21.5.1 (p. 753).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §5.1 (pp. 258–267),
  §10.1 (pp. 449–450, 458), §10.2 (pp. 459–461).
