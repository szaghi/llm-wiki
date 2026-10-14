---
type: Result
title: "Boundary data by equation type"
description: "Stated without proof: a hyperbolic equation takes Cauchy data on an open boundary, a parabolic one Dirichlet or Neumann data on an open boundary, an elliptic one Dirichlet or Neumann data on a closed boundary (possibly at infinity), these pairings giving a unique (sometimes up to a constant) and well-defined solution."
status: established
aliases: [Table 20.1, appropriate boundary conditions, well-posed boundary data]
tags: [well-posedness, boundary-conditions, classification]
timestamp: 2026-10-13T00:00:00Z
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

**Examples** (Exercise 20.23, answers p. 712): an isolated conducting bar
with an initial temperature is parabolic, open, with Dirichlet initial data
and Neumann $\partial_xu = 0$ at the ends. Concentric cylinders with
prescribed voltage are elliptic, closed, Dirichlet; with prescribed charge,
elliptic, closed, Neumann. A semi-infinite string whose end is moved in a
prescribed way is hyperbolic, open, Cauchy.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.6.2 (pp. 704–705),
  Table 20.1, Exercise 20.23 (pp. 710, 712), §21.5.2 (p. 754).
