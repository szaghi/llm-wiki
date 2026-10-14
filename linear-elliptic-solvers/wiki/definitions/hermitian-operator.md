---
type: Definition
title: "Adjoint and Hermitian differential operators"
description: "Formal adjoint of a linear differential operator by integration by parts, self-adjoint versus Hermitian (boundary terms vanish under the imposed conditions), the PDE version, and the properties of a Hermitian operator: real eigenvalues, orthogonal and real-choosable eigenfunctions, completeness and the closure relation."
status: established
aliases: [adjoint operator, self-adjoint operator, Hermitian operator, closure relation, completeness relation, eigenfunction]
tags: [operator-theory, eigenproblem, function-space]
timestamp: 2026-10-14T00:00:00Z
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

*Qualification (terminology), [Arfken et al. (2013)](/sources/arfken-2013.md).*
Arfken et al. use "self-adjoint" in two senses. For an abstract operator on
a Hilbert space they define the adjoint by
$\langle f,\mathcal Ag\rangle=\langle\mathcal A^{\mathsf H}f,g\rangle$ for
all $f$, $g$ of the space and call $\mathcal A$ "self-adjoint, or
equivalently, Hermitian" when $\mathcal A^{\mathsf H}=\mathcal A$ (§5.3,
eqs. 5.47–5.48, p. 277) — Riley's *Hermitian*, the boundary conditions
entering through the space. For a second-order differential expression,
"self-adjoint in the differential-equation sense" is the formal condition
alone, which they call "weaker than the corresponding concept for
operators in our Hilbert spaces, due to the lack of a requirement on the
boundary terms" (§8.2, p. 385) — Riley's *self-adjoint*. The two books
therefore draw the same distinction under different words; neither uses
the functional-analytic one. Arfken et al. stress that Hermiticity depends
on the scalar product and the interval: $-\mathrm i\,\mathrm d/\mathrm dx$ is
Hermitian on the square-integrable functions on the whole line but not on $[-1,1]$, where the boundary
terms survive, and $x\,\mathrm d/\mathrm dx$ has adjoint
$-\mathrm d/\mathrm dx\,x$ on the whole line (Examples 5.3.2–5.3.3,
p. 278).

**Matrix representation** (Arfken et al., §§5.3–5.4, pp. 279–284). In an
orthonormal basis the matrix of $\mathcal A^{\mathsf H}$ is the conjugate
transpose of the matrix of $\mathcal A$ (eq. 5.60), so a Hermitian operator
is represented by a Hermitian matrix (eq. 5.62), and
$\langle u,\mathcal Au\rangle=\mathbf x^{\mathsf H}A\mathbf x$ is real.
The product of two Hermitian operators is Hermitian iff they commute
(p. 286).

**PDE version.** A partial differential operator is Hermitian on $\Omega$
if $\int_\Omega\bar\phi\,\mathcal L\psi\,\mathrm dV=\overline{\int_\Omega\bar\psi\,\mathcal L\phi\,\mathrm dV}$
for all $\phi$, $\psi$ obeying the homogeneous boundary conditions (§21.5.1,
p. 753). Arfken et al. give the self-adjoint form
$\nabla\cdot(p\nabla u)+qu$ with real $p$, $q$ (in registry sign
$-\nabla\cdot(p\nabla u)+qu$), Hermitian when the boundary conditions
make $\langle\phi,\mathcal L\psi\rangle=\langle\mathcal L\phi,\psi\rangle$,
e.g. Dirichlet conditions with unit weight (eq. 10.33, p. 460; exercise
10.2.2, p. 466).

## Properties (§17.3, pp. 561–564)

1. **Real eigenvalues:** from eq. 17.16 applied to two eigenfunctions,
   $(\bar\lambda_i-\lambda_j)\int_a^b\bar\phi_i\phi_jw\,\mathrm dx=0$
   (eq. 17.23); $i=j$ gives $\lambda_i$ real.
2. **Orthogonality:** eigenfunctions of distinct eigenvalues are orthogonal
   with weight $w$ (eq. 17.24); a degenerate eigenspace is orthogonalised by
   [Gram–Schmidt](/methods/gram-schmidt-orthogonalisation.md), and
   normalisation gives $\langle\phi_m,\phi_n\rangle_w=\delta_{mn}$ (eq. 17.27).
   Arfken et al. prove properties 1 and 2 for Hermitian matrices by the
   same two-line argument (eqs. 6.17–6.21, pp. 310–311) and transfer them
   to any Hermitian operator through its matrix representation (p. 311,
   summary §8.5, p. 398).
3. **Completeness:** the eigenfunctions form a complete basis, so
   $u=\sum_nc_n\phi_n$ converges to $u$ in the sense that the sum can be made
   "arbitrarily close" (eq. 17.17). Stated without proof, with a reference to
   Courant & Hilbert (1953) (footnote, p. 560). The closure relation follows:
   $$w(x')\sum_n\phi_n(x)\bar\phi_n(x')=\delta(x-x'),$$
   and $w(x')$ may be replaced by $w(x)$ (eqs. 17.28–17.29). For a
   continuous spectrum the sum becomes an integral. Arfken et al. state
   completeness as flatly — "A Hermitian operator on a Hilbert space has a
   complete set of eigenfunctions" (§8.5, item 3, p. 398; also p. 311) —
   and cite the same Courant & Hilbert (vol. 1, ch. 6, §3) for the proof
   (footnote, p. 262). Their closure relation is written for unit weight,
   $\sum_n\phi_n(x)\bar\phi_n(x')=\delta(x-x')$, valid for $x$, $x'$
   inside the interval and meaningful only under an integral; its
   convergence is not uniform at $x=x'$ (eqs. 5.25–5.30, pp. 263–265).
   *Compiler's note (status: hypothesis):* neither book states the
   hypotheses under which an eigenbasis exists; as written, the statement
   fails for operators with continuous spectrum, which Riley et al. at
   least acknowledge.
4. **Real eigenfunctions:** $\phi$ and $\bar\phi$ belong to the same (real)
   eigenvalue, so $\phi+\bar\phi$ or $\mathrm i(\bar\phi-\phi)$ is a real
   eigenfunction; recombination is needed only for degenerate eigenvalues
   (§17.3.4).

The matrix counterpart is the
[spectral theorem](/results/spectral-theorem-normal-matrices.md); the
lower bound $\langle u,\mathcal Lu\rangle\ge\lambda_{\min}\lVert u\rVert^2$
that a Hermitian operator with a finite smallest eigenvalue obeys is the
basis of the [variation method](/methods/variation-method.md). The
main family of Hermitian operators is the
[Sturm–Liouville operator](/definitions/sturm-liouville-problem.md); the
properties above underlie the
[eigenfunction expansion](/methods/eigenfunction-expansion.md) of the
[Green's function](/definitions/greens-function.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17 intro (pp. 554–556),
  §§17.2–17.3 (pp. 559–564), §21.5.1 (p. 753).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §5.1 (pp. 262–265),
  §§5.3–5.4 (pp. 275–286), §6.3 (pp. 310–311), §8.2 (p. 385), §8.5
  (p. 398), §10.2 (p. 460).
