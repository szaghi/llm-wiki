---
type: Definition
title: "Sturm–Liouville problem"
description: "Second-order eigenproblem -(p u')' + q u = lambda w u with real coefficients, Hermitian on [a,b] under boundary conditions that make [conj(u_i) p u_j']_a^b vanish; the integrating factor that brings any second-order linear equation to this form, natural intervals where p vanishes, and the classical equations in Sturm–Liouville form."
status: established
aliases: [Sturm-Liouville equation, Sturm-Liouville operator, SL problem, natural interval, self-adjoint ODE, weight function]
tags: [operator-theory, eigenproblem, ode]
timestamp: 2026-10-14T00:00:00Z
---

# Sturm–Liouville problem

**Definition.** The Sturm–Liouville equation with real $p$, $q$, $w$ is
$$\mathcal Lu\equiv-(pu')'+qu=\lambda wu$$
([Riley et al. (2006)](/sources/riley-2006.md), §17.4, eqs. 17.32–17.35,
p. 564). Riley et al. write $-(pu')'-qu$, so their $q$ is the registry's
$-q$; they also note that sign conventions vary, some authors putting
$-\lambda w u$ in eq. 17.32.

*Qualification (sign and form), [Arfken et al. (2013)](/sources/arfken-2013.md).*
Arfken et al. start from a general second-order operator in an
unweighted eigenproblem $\mathcal Lu=\lambda u$ (eqs. 8.7–8.8, p. 384),
call it self-adjoint in the differential-equation sense when the
coefficient of $u'$ is the derivative of the coefficient of $u''$, so that
it can be written as the derivative of (coefficient times $u'$) plus a
multiple of $u$, with a plus sign (eqs. 8.9–8.11), and introduce the weight
only when that condition fails (below). Their general form therefore fixes
no sign: in registry symbols their coefficient of $u''$ is $-p$ (times
$w$ after weighting) and their zeroth-order coefficient is $q$; the
correspondence is spelled out in the source's notation map. In their examples they write the
minus sign explicitly — Legendre $-(1-x^2)u''+2xu'=\lambda u$ (eq. 8.23),
Hermite $-u''+2xu'=\lambda u$ (eq. 8.27), $-\mathrm d^2/\mathrm dx^2$ for
the string (eq. 8.2) — which is the registry sign with non-negative
eigenvalues. Their Green's-function chapter uses $(pu')'+qu$ (eq. 10.5), the
registry form with $p\to-p$.

**Hermiticity.** $\mathcal L$ is self-adjoint, and
[Hermitian](/definitions/hermitian-operator.md) on $[a,b]$ provided any two
eigenfunctions satisfy
$$\left[\bar u_i\,p\,u_j'\right]_{x=a}^{x=b}=0\quad\text{(eqs. 17.36–17.37)},$$
proved by two integrations by parts (§17.4.1, p. 565). Arfken et al.
derive the general form for any two admissible functions $u$, $v$,
$$\int_a^b\bar v\,\mathcal Lu\,\mathrm dx-\int_a^b\overline{\mathcal Lv}\,u\,\mathrm dx=-\left[p\left(\bar v\,u'-\bar v'\,u\right)\right]_a^b$$
(eq. 8.12, p. 385, in registry sign), and specialise it to eigenfunctions,
$(\lambda_u-\lambda_v)\langle v,u\rangle$ equal to the same boundary term
(eq. 8.13). The condition is met
by, e.g., $u(a)=u(b)=0$; $u(a)=u'(b)=0$; $p(a)=p(b)=0$; Arfken et al. add
Neumann conditions $u'(a)=u'(b)=0$ and periodicity, where
$\bar vpu'$ takes equal values at $a$ and $b$ (p. 385). One condition must
be specified at each end of the range. Where $p(a)=p(b)=0$, $[a,b]$ is a
**natural interval**: $\mathcal L$ is Hermitian there for any eigenfunctions
regular at the endpoints. Arfken et al. reach the same conclusion for
Legendre's operator, whose leading coefficient vanishes at $\pm1$, with
non-singularity at the endpoints acting as the boundary condition (§8.3,
pp. 389–390); for Hermite's operator on $(-\infty,\infty)$ the condition is
a finite weighted norm (pp. 390–391). In both cases the eigenvalues follow
from requiring the power-series solution to terminate.

**Reduction to Sturm–Liouville form** (§17.4.2). Any
$pu''+p_1u'-qu+\lambda wu=0$ (eq. 17.38, first-order coefficient $p_1$)
becomes Sturm–Liouville form on multiplication by
$$\Psi(x)=\exp\left(\int^x\frac{p_1(t)-p'(t)}{p(t)}\,\mathrm dt\right)\quad\text{(eq. 17.39)},$$
giving $-(\Psi pu')'+\Psi qu=\lambda\Psi wu$, with weight $\Psi w$ still
non-negative (eq. 17.40).

Arfken et al. reach the same factor from the other side. For an
unweighted problem, i.e. the general equation above with $w\equiv1$,
$pu''+p_1u'-qu+\lambda u=0$, they multiply by
$$w(x)=\frac{1}{p(x)}\exp\left(\int^x\frac{p_1(t)}{p(t)}\,\mathrm dt\right)\quad\text{(eq. 8.15, p. 385, in registry symbols; the book's form differs by the constant factor $-1$)},$$
which makes the operator self-adjoint in form and Hermitian under the
weighted scalar product $\langle\cdot,\cdot\rangle_w$ when the boundary
terms vanish (eqs. 8.16–8.20, p. 386). Since
$\int(p_1-p')/p=\int p_1/p-\ln p$, this $w$ is exactly $\Psi$: the
integrating factor of one book is the weight function of the other.
Their summary (p. 386): a formally self-adjoint operator is Hermitian under
the unweighted scalar product with boundary terms removed; otherwise it is
Hermitian under the scalar product weighted by eq. 8.15.

**Classical cases** (table 17.1, p. 566; natural intervals p. 567).
Legendre, associated Legendre and Chebyshev on $[-1,1]$; Laguerre and
associated Laguerre on $[0,\infty]$; Hermite on $[-\infty,\infty]$; simple
harmonic with periodic interval of length $2\pi$; hypergeometric on
$[0,1]$ under parameter conditions derived in an example (pp. 567–568).
Bessel's equation fits only after rescaling the variable, and then the
eigenvalue enters the argument of the solution (eqs. 17.41–17.42). Arfken
et al. obtain the weights and intervals of the polynomial cases by
eq. 8.15: Laguerre $\mathrm e^{-x}$ on $[0,\infty)$ (Example 8.2.1,
p. 387), Hermite $\mathrm e^{-x^2}$ on $(-\infty,\infty)$, Chebyshev
$(1-x^2)^{-1/2}$ and Legendre $1$ on $[-1,1]$ (exercises 8.2.1–8.2.4,
statements, p. 387) — the intervals of Riley's table.

Riley's variational treatment of Sturm–Liouville eigenvalues (ch. 22)
is outside the scope read; Arfken et al.'s
[variation method](/methods/variation-method.md) (§8.4) bounds the lowest
eigenvalue of a Hermitian operator from above.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17.4 (pp. 564–568).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §8.1 (pp. 381–384),
  §8.2 (pp. 384–388), §8.3 (pp. 389–391).
