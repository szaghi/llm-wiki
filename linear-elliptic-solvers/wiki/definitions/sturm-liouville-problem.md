---
type: Definition
title: "Sturm–Liouville problem"
description: "Second-order eigenproblem -(p u')' + q u = lambda w u with real coefficients, Hermitian on [a,b] under boundary conditions that make [conj(u_i) p u_j']_a^b vanish; the integrating factor that brings any second-order linear equation to this form, natural intervals where p vanishes, and the classical equations in Sturm–Liouville form."
status: established
aliases: [Sturm-Liouville equation, Sturm-Liouville operator, SL problem, natural interval]
tags: [operator-theory, eigenproblem, ode]
timestamp: 2026-10-13T00:00:00Z
---

# Sturm–Liouville problem

**Definition.** The Sturm–Liouville equation with real $p$, $q$, $w$ is
$$\mathcal Lu\equiv-(pu')'+qu=\lambda wu$$
([Riley et al. (2006)](/sources/riley-2006.md), §17.4, eqs. 17.32–17.35,
p. 564). Riley et al. write $-(pu')'-qu$, so their $q$ is the registry's
$-q$; they also note that sign conventions vary, some authors putting
$-\lambda w u$ in eq. 17.32.

**Hermiticity.** $\mathcal L$ is self-adjoint, and
[Hermitian](/definitions/hermitian-operator.md) on $[a,b]$ provided any two
eigenfunctions satisfy
$$\left[\bar u_i\,p\,u_j'\right]_{x=a}^{x=b}=0\quad\text{(eqs. 17.36–17.37)},$$
proved by two integrations by parts (§17.4.1, p. 565). The condition is met
by, e.g., $u(a)=u(b)=0$; $u(a)=u'(b)=0$; $p(a)=p(b)=0$. One condition must
be specified at each end of the range. Where $p(a)=p(b)=0$, $[a,b]$ is a
**natural interval**: $\mathcal L$ is Hermitian there for any eigenfunctions
regular at the endpoints.

**Reduction to Sturm–Liouville form** (§17.4.2). Any
$pu''+p_1u'-qu+\lambda wu=0$ (eq. 17.38, first-order coefficient $p_1$)
becomes Sturm–Liouville form on multiplication by
$$\Psi(x)=\exp\left(\int^x\frac{p_1(t)-p'(t)}{p(t)}\,\mathrm dt\right)\quad\text{(eq. 17.39)},$$
giving $-(\Psi pu')'+\Psi qu=\lambda\Psi wu$, with weight $\Psi w$ still
non-negative (eq. 17.40).

**Classical cases** (table 17.1, p. 566; natural intervals p. 567).
Legendre, associated Legendre and Chebyshev on $[-1,1]$; Laguerre and
associated Laguerre on $[0,\infty]$; Hermite on $[-\infty,\infty]$; simple
harmonic with periodic interval of length $2\pi$; hypergeometric on
$[0,1]$ under parameter conditions derived in an example (pp. 567–568).
Bessel's equation fits only after rescaling the variable, and then the
eigenvalue enters the argument of the solution (eqs. 17.41–17.42).

The book's variational treatment of Sturm–Liouville eigenvalues (ch. 22)
is outside the scope read.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §17.4 (pp. 564–568).
