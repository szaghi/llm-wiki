---
type: Definition
title: "Adjoint and Hermitian differential operators"
description: "Formal adjoint of a linear differential operator by integration by parts, self-adjoint versus Hermitian (boundary terms vanish under the imposed conditions), the PDE version, and the properties of a Hermitian operator: real eigenvalues, orthogonal and real-choosable eigenfunctions, completeness and the closure relation."
status: established
aliases: [adjoint operator, self-adjoint operator, Hermitian operator, closure relation, completeness relation, eigenfunction]
tags: [operator-theory, eigenproblem, function-space]
timestamp: 2026-10-13T00:00:00Z
---

# Adjoint and Hermitian differential operators

**Eigenfunctions.** For a linear differential operator $\mathcal L$ on
$[a,b]$ with imposed boundary conditions, $\phi$ is an eigenfunction with
eigenvalue $\lambda$ with respect to the weight $w$ if
$\mathcal L\phi=\lambda w\phi$, $w$ real and of one sign on $[a,b]$, taken
non-negative ([Riley et al. (2006)](/sources/riley-2006.md), §17 intro,
eqs. 17.2, 17.5, p. 555).

**Adjoint.** The adjoint $\mathcal L^{*}$ is defined by
$$\int_a^b\bar f\,(\mathcal Lg)\,\mathrm dx=\int_a^b\overline{(\mathcal L^{*}f)}\,g\,\mathrm dx+\text{boundary terms}\quad\text{(eq. 17.15)},$$
obtained by repeated integration by parts. $\mathcal L$ is **self-adjoint**
if $\mathcal L^{*}=\mathcal L$, and **Hermitian** on $[a,b]$ if in addition
the boundary terms vanish for the admitted functions, so that
$$\int_a^b\bar f\,(\mathcal Lg)\,\mathrm dx=\int_a^b\overline{(\mathcal Lf)}\,g\,\mathrm dx\quad\text{(eq. 17.16)}$$
(§17.2, pp. 559–560). Example: $\mathrm d^2/\mathrm dx^2$ is self-adjoint,
and Hermitian on $[a,b]$ when $[\bar f g']_a^b=[\bar f' g]_a^b$.

**Terminology warning.** This usage is the book's: "self-adjoint" means
formally self-adjoint, and "Hermitian" adds the boundary conditions. In
functional-analytic usage "self-adjoint" is the stronger notion (domain
equality) and the book's "Hermitian" corresponds to symmetric. Later
sources must be mapped with care.

**PDE version.** A partial differential operator is Hermitian on $\Omega$
if $\int_\Omega\bar\phi\,\mathcal L\psi\,\mathrm dV=\overline{\int_\Omega\bar\psi\,\mathcal L\phi\,\mathrm dV}$
for all $\phi$, $\psi$ obeying the homogeneous boundary conditions (§21.5.1,
p. 753).

## Properties (§17.3, pp. 561–564)

1. **Real eigenvalues:** from eq. 17.16 applied to two eigenfunctions,
   $(\bar\lambda_i-\lambda_j)\int_a^b\bar\phi_i\phi_jw\,\mathrm dx=0$
   (eq. 17.23); $i=j$ gives $\lambda_i$ real.
2. **Orthogonality:** eigenfunctions of distinct eigenvalues are orthogonal
   with weight $w$ (eq. 17.24); a degenerate eigenspace is orthogonalised by
   [Gram–Schmidt](/methods/gram-schmidt-orthogonalisation.md), and
   normalisation gives $\langle\phi_m,\phi_n\rangle_w=\delta_{mn}$ (eq. 17.27).
3. **Completeness:** the eigenfunctions form a complete basis, so
   $u=\sum_nc_n\phi_n$ converges to $u$ in the sense that the sum can be made
   "arbitrarily close" (eq. 17.17). Stated without proof, with a reference to
   Courant & Hilbert (1953) (footnote, p. 560). The closure relation follows:
   $$w(x')\sum_n\phi_n(x)\bar\phi_n(x')=\delta(x-x'),$$
   and $w(x')$ may be replaced by $w(x)$ (eqs. 17.28–17.29). For a
   continuous spectrum the sum becomes an integral.
4. **Real eigenfunctions:** $\phi$ and $\bar\phi$ belong to the same (real)
   eigenvalue, so $\phi+\bar\phi$ or $\mathrm i(\bar\phi-\phi)$ is a real
   eigenfunction; recombination is needed only for degenerate eigenvalues
   (§17.3.4).

The matrix counterpart is the
[spectral theorem](/results/spectral-theorem-normal-matrices.md). The
main family of Hermitian operators is the
[Sturm–Liouville operator](/definitions/sturm-liouville-problem.md); the
properties above underlie the
[eigenfunction expansion](/methods/eigenfunction-expansion.md) of the
[Green's function](/definitions/greens-function.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17 intro (pp. 554–556),
  §§17.2–17.3 (pp. 559–564), §21.5.1 (p. 753).
