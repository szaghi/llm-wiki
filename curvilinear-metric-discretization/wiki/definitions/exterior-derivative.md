---
type: Definition
title: "Exterior derivative"
description: "The operator d mapping p-forms to (p+1)-forms, defined by linearity, the Leibniz rule d(fα) = df∧α + f dα, the antiderivation rule d(α∧β) = dα∧β + (−1)^p α∧dβ, d(dα) = 0 and df = ∂_k f dx^k; in three dimensions it generates gradient, curl and divergence, and d∘d = 0 contains curl grad = 0 and div curl = 0."
status: established
aliases: [exterior differentiation, d operator, Cartan derivative, Poincare lemma, d squared equals zero, nilpotency of d]
symbol: "$d$"
tags: [differential-forms, exterior-calculus, operators, identities]
timestamp: 2026-10-14T00:00:00Z
---

# Exterior derivative

**Axioms** ([Arfken et al. (2013)](/sources/arfken-2013.md), §4.6,
eq. (4.85), pp. 238–239). For a $p$-form $\alpha$, a $p'$-form $\beta$ and a
function (0-form) $\phi$:

$$\begin{aligned}
d(\alpha+\beta)&=d\alpha+d\beta\quad(p=p'),\qquad d(\phi\alpha)=d\phi\wedge\alpha+\phi\,d\alpha,\\
d(\alpha\wedge\beta)&=d\alpha\wedge\beta+(-1)^p\,\alpha\wedge d\beta,\qquad d(d\alpha)=0,\qquad d\phi=\frac{\partial\phi}{\partial x^k}\,dx^k .
\end{aligned}$$

The basis 1-forms $dx^i$ are the exterior derivatives of the coordinate
functions $x^i$, and $d$ of any $dx^i$ is zero. The book treats the rules as
axioms, checks that the sign $(-1)^p$ is required for consistency
(Example 4.6.1, p. 239), and calls the antiderivation rule's sign
"antisymmetry-motivated".

* **$d(d\alpha)=0$.** It is an independent axiom (without it nothing reduces
  $d(dx^i)$), and it is consistent with the others because mixed second
  derivatives of a sufficiently differentiable function do not depend on the
  order of differentiation; shown explicitly for $d(d\phi)$ in two dimensions
  (p. 240). The book calls this axiom "Poincaré's lemma" (p. 239).
* **Degree raising.** $d$ maps a $p$-form to a $(p+1)$-form, so the result of
  differentiating stays a form; the book contrasts this with tensor calculus,
  where differentiating the components of a tensor with position-dependent
  transformation coefficients does not give a tensor and the
  [covariant derivative](/definitions/covariant-derivative.md) is needed
  (p. 235).

## The vector operators (Cartesian, three dimensions)

From the axioms (eqs. (4.86)–(4.90), p. 240):

$$\begin{aligned}
d\phi&=(\nabla\phi)_1\,dx^1+(\nabla\phi)_2\,dx^2+(\nabla\phi)_3\,dx^3,\\
d(v_k\,dx^k)&=(\nabla\times\mathbf v)_1\,dx^2\wedge dx^3+(\nabla\times\mathbf v)_2\,dx^3\wedge dx^1+(\nabla\times\mathbf v)_3\,dx^1\wedge dx^2,\\
d(b_1\,dx^2\wedge dx^3+b_2\,dx^3\wedge dx^1+b_3\,dx^1\wedge dx^2)&=(\nabla\cdot\mathbf b)\,dx^1\wedge dx^2\wedge dx^3 .
\end{aligned}$$

With the [Hodge star](/definitions/hodge-star.md) the last two become the
1-form of the curl and the 0-form $\nabla\cdot\mathbf b$. "Application of the
$d$ operator directly generates all the differential operators of
traditional vector analysis" ([gradient](/definitions/gradient.md),
[curl](/definitions/curl.md), [divergence](/definitions/divergence.md)).

**Identities from $d\circ d=0$** (eqs. (4.91)–(4.92), p. 241): taking the
1-form $d\phi$ in the curl formula gives $\nabla\times(\nabla\phi)=\mathbf 0$;
taking the 2-form $d(v_k\,dx^k)$ in the divergence formula gives
$\nabla\cdot(\nabla\times\mathbf v)=0$. These are "merely the first members
of hierarchies of identities" in more dimensions and other metrics
([vector operator identities](/results/vector-operator-identities.md)).
The continuity equation of electromagnetic charge follows the same way in
Minkowski space, because the source 3-form is $d$ of a form and so has zero
exterior derivative (eq. (4.98), p. 243).

## Exact and closed forms

A form with $\alpha=d\phi$ is **exact**; then $d\alpha=0$, i.e. $\alpha$ is
**closed** (exercise 4.7.3 defines both for 1-forms in the plane; eqs.
(4.100)–(4.101), p. 244). See [differential form](/definitions/differential-form.md)
and, for the vector-calculus counterpart in a simply connected region, the
[conservative vector field](/definitions/conservative-vector-field.md).
Integrated, $d$ obeys [Stokes' theorem for differential forms](/results/generalized-stokes-theorem.md).

*Terminology note (compiler's remark).* Arfken names $d(d\alpha)=0$
"Poincaré's lemma". The same name is widely used in the literature for a
different statement, the converse direction that a closed form is exact on a
contractible (e.g. star-shaped) region. No source of this bundle states that
converse yet; a page citing "Poincaré lemma" must say which statement is
meant.

*Compiler's remark.* $d$ uses no metric: the derivatives above are the same
expressions in every coordinate system once the $dx^i$ are replaced by
$d\xi^i$ and the components by the components of the form in $\xi$. This is
why its discrete counterpart (a signed incidence matrix acting on cochains)
needs no metric terms; the source does not discuss discretization.

# Citations

* [Arfken et al. (2013)](/sources/arfken-2013.md), §4.5, p. 235; §4.6, pp. 238–243; §4.7, p. 244; exercise 4.7.3, p. 248.
