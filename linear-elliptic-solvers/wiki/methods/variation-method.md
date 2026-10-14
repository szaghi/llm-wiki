---
type: Method
title: "Variation method"
description: "Upper bound and approximation of the smallest eigenvalue of a Hermitian operator: the Rayleigh quotient of any admissible function is a weighted mean of the eigenvalues, so minimising it over a parametrised trial family bounds lambda_min from above, with equality only at an eigenfunction."
status: established
aliases: [variational method, variation principle, Rayleigh-Ritz bound, Rayleigh quotient minimisation, expectation-value bound]
tags: [eigenproblem, operator-theory, variational]
timestamp: 2026-10-14T00:00:00Z
---

# Variation method

**Bound.** Let $\mathcal L$ be [Hermitian](/definitions/hermitian-operator.md)
with orthonormal eigenfunctions $\phi_n$, eigenvalues $\lambda_n$, and a
finite smallest eigenvalue $\lambda_{\min}$. For any admissible $u\neq0$,
expanded as $u=\sum_nc_n\phi_n$,
$$R_{\mathcal L}(u)=\frac{\langle u,\mathcal Lu\rangle}{\langle u,u\rangle}=\frac{\sum_n\lvert c_n\rvert^2\lambda_n}{\sum_n\lvert c_n\rvert^2}\ \ge\ \lambda_{\min},$$
with equality only if $u$ is an eigenfunction of $\lambda_{\min}$
([Arfken et al. (2013)](/sources/arfken-2013.md), §6.4, eqs. 6.28–6.31,
p. 316; restated for operators in §8.4, p. 395, and §8.5, item 11,
p. 399). The book stresses that the bound holds without knowing or
computing the expansion: it needs only Hermiticity and the completeness of
the eigenfunctions, which the book assumes (p. 395).

**Method** (§8.4, pp. 395–396). Choose a trial family $\tilde u$ depending
on parameters, compute $R_{\mathcal L}(\tilde u)$, and minimise over the
parameters. The minimum is the best upper bound to $\lambda_{\min}$ the
family allows; its quality depends on how closely the family can
approximate the eigenfunction, and it is exact if the family contains it.
The book calls the method "at the heart of some of the most powerful
methods" for large quantum eigenproblems and cites a variational helium
calculation accurate to about 40 digits (Schwartz 2006) (p. 397); its
worked examples are one- and two-electron atoms (Example 8.4.1), outside
this bundle's scope.

**Accuracy.** For a Hermitian matrix with distinct eigenvalues, an
approximate eigenvector with small components along the other
eigenvectors gives an error in the Rayleigh quotient of the order of their
squares
(exercise 6.5.18, statement only, p. 327, stated for the largest
eigenvalue, from below).

**Relation to the matrix case.** For a matrix the quotient is
$R_A(\mathbf x)$ of the [quadratic and Hermitian forms](/definitions/quadratic-and-hermitian-forms.md)
page: [Riley et al. (2006)](/sources/riley-2006.md) prove that it is
stationary exactly at eigenvectors, where it equals the eigenvalue
(§8.17.1, pp. 290–291) — in the compiler's reading, the reason a
first-order error in $\mathbf x$ produces only a second-order error in
$R_A$. Arfken et al. add the bound
$\lambda_{\min}\le R_A\le\lambda_{\max}$. Neither source in the scope read
treats the Ritz projection onto a finite trial subspace (a matrix
eigenproblem whose eigenvalues bound several eigenvalues at once) or
higher eigenvalues; Riley's variational chapter (ch. 22) is outside the
scope read.

For a [Sturm–Liouville](/definitions/sturm-liouville-problem.md) operator
the quotient is $\langle u,\mathcal Lu\rangle/\langle u,u\rangle_w$ with
the weight in the denominator, since $\mathcal L\phi_n=\lambda_nw\phi_n$;
*this weighted form is the compiler's transcription to the registry
convention (status: hypothesis)* — Arfken et al. state the bound for an
operator Hermitian under its own scalar product, with the weight already
absorbed.

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §6.4 (p. 316), exercise
  6.5.18 (p. 327), §8.4 (pp. 395–397), §8.5 (p. 399).
* [Riley et al. (2006)](/sources/riley-2006.md), §8.17.1 (pp. 290–291).
