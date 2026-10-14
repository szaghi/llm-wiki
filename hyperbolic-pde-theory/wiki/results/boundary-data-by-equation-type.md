---
type: Result
title: "Boundary data by equation type"
description: "Stated without proof in both textbooks: a hyperbolic equation takes Cauchy data on an open boundary, a parabolic one Dirichlet or Neumann data on an open boundary, an elliptic one Dirichlet or Neumann data on a closed boundary (possibly at infinity), these pairings giving a unique (sometimes up to a constant), well-defined and, in Arfken's table, stable solution; the other pairings are insufficient, too restrictive, non-unique or unstable."
status: established
aliases: [Table 20.1, Table 9.1, appropriate boundary conditions, well-posed boundary data]
tags: [well-posedness, boundary-conditions, classification]
timestamp: 2026-10-14T00:00:00Z
---

# Boundary data by equation type

| Equation type | Boundary | Conditions |
|---|---|---|
| hyperbolic | open | Cauchy |
| parabolic | open | Dirichlet or Neumann |
| elliptic | closed | Dirichlet or Neumann |

([Riley et al. (2006)](/sources/riley-2006.md), Table 20.1, p. 705; types
per [classification](/definitions/second-order-pde-classification.md),
conditions per [boundary condition types](/definitions/boundary-condition-types.md).)

**What is claimed.** These pairings are the appropriate ones "in that they
give a solution that is unique, sometimes to within a constant, and is well
defined". Appropriateness depends on the equation type and on whether the
region is bounded by a closed or an open curve or surface. Part of a closed
boundary may be at infinity (p. 705).

**Status of the claim.** The book states the table without proof: "It may
be shown that the appropriate boundary-condition and equation-type
pairings are as given in table 20.1". It calls the general considerations
"complex" and refers the reader to Morse and Feshbach (1953), chap. 6
(p. 705; see the [bibliography](/bibliography.md)). The only part proved in
the chapters read is the elliptic row for Poisson's equation, through the
[uniqueness theorem](/results/uniqueness-theorem-poisson.md). The book's
notion of "appropriate" is uniqueness and well-definedness. Continuous
dependence on the data (Hadamard well-posedness) is not mentioned.

**Caveats stated with it.** Cauchy data on a hyperbolic data curve that
meets a characteristic more than once can overdetermine the problem
(p. 705; [characteristic curves](/definitions/characteristic-curve.md)).
Dirichlet and Neumann data together on a closed boundary overdetermine
Poisson's equation (p. 754).

## Arfken et al.'s Table 9.1

[Arfken et al. (2013)](/sources/arfken-2013.md) tabulate every pairing, not
only the appropriate ones, for the model equations in two variables:
Laplace or Poisson in $(x,y)$, wave and diffusion in $(x,t)$ (§9.3,
Table 9.1, p. 412).

| Conditions | Boundary | Elliptic | Hyperbolic | Parabolic |
|---|---|---|---|---|
| Cauchy | open | unphysical results (instability) | **unique, stable solution** | too restrictive |
| Cauchy | closed | too restrictive | too restrictive | too restrictive |
| Dirichlet | open | insufficient | insufficient | **unique, stable solution in one direction** |
| Dirichlet | closed | **unique, stable solution** | solution not unique | too restrictive |
| Neumann | open | insufficient | insufficient | **unique, stable solution in one direction** |
| Neumann | closed | **unique, stable solution** | solution not unique | too restrictive |

**Agreement.** The bold cells are exactly Riley et al.'s three rows. Both
books state the table without proof. Both send the reader to Morse and
Feshbach, Chapter 6: Arfken et al. call an exact analysis "complicated and
beyond the scope of the present text" (p. 412).

**Qualifications.**

* *Stability.* Arfken et al.'s table qualifies the appropriate pairings as
  "stable" and marks Cauchy data for an elliptic equation as giving
  "unphysical results (instability)". This is the continuous-dependence
  requirement that Riley et al. do not mention (see above). Arfken et al.
  give no definition of stability and no example of the instability.
* *One direction.* For the parabolic equation the solution is unique and
  stable "in one direction" (in time), a restriction absent from Riley's
  row.
* *Scope.* Table 9.1 "oversimplifies the situation". The Helmholtz equation
  $\nabla^2u \pm k^2u = 0$ with Dirichlet data on a closed boundary "has
  solution(s) … only for certain values of its parameter $k$", an
  eigenvalue problem (p. 413). For the plus sign this agrees with
  everything in Riley et al. For the minus sign it collides with Riley et
  al.'s uniqueness result for $\nabla^2u - k^2u = 0$ (see the
  [uniqueness theorem](/results/uniqueness-theorem-poisson.md)); the
  conflict is recorded, open, under `Contradictions` on the
  [Helmholtz equation](/definitions/helmholtz-equation.md) page.
* *Overdetermination.* Arfken et al. derive the inconsistency of Cauchy
  data for Poisson's equation from the table itself: Dirichlet and Neumann
  data each determine a solution, so prescribing both "could lead to an
  inconsistency" (pp. 412–413). This agrees with Riley et al. (p. 754).

**Examples** (Riley et al., Exercise 20.23, answers p. 712): an isolated conducting bar
with an initial temperature is parabolic, open, with Dirichlet initial data
and Neumann $\partial_xu = 0$ at the ends. Concentric cylinders with
prescribed voltage are elliptic, closed, Dirichlet; with prescribed charge,
elliptic, closed, Neumann. A semi-infinite string whose end is moved in a
prescribed way is hyperbolic, open, Cauchy.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.6.2 (pp. 704–705),
  Table 20.1, Exercise 20.23 (pp. 710, 712), §21.5.2 (p. 754).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.3 (pp. 411–413),
  Table 9.1.
