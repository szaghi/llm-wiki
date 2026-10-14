---
type: Definition
title: "Helmholtz equation"
description: "The equation laplacian of U plus k^2 U equals zero, the spatial part left when time is separated from the wave or diffusion equation (Laplace's equation for k = 0); it separates in Cartesian, cylindrical and spherical coordinates (plane waves, Bessel and spherical Bessel radial factors), and with homogeneous Dirichlet data on a closed boundary it is an eigenvalue problem with nontrivial solutions only for discrete k^2."
status: established
aliases: [Helmholtz PDE, reduced wave equation, time-independent diffusion equation, modified Helmholtz equation]
tags: [model-equation, elliptic, separation-of-variables, eigenvalue-problem]
timestamp: 2026-10-14T00:00:00Z
---

# Helmholtz equation

$$\nabla^2U + k^2U = 0$$
is the equation for the spatial factor $U(\mathbf x)$ left when the time
dependence is separated from the [wave equation](/definitions/wave-equation.md),
$u = U(\mathbf x)\mathcal T(t)$ with $\mathcal T \propto e^{\pm i\omega t}$
and $k = \omega/c$ ([Riley et al. (2006)](/sources/riley-2006.md), eqs.
21.52–21.54, p. 737), or from the [diffusion equation](/definitions/diffusion-equation.md),
with a time factor that decays exponentially
([Arfken et al. (2013)](/sources/arfken-2013.md), §9.7, eq. 9.104, p. 439).
For $k = 0$ it is [Laplace's equation](/definitions/laplace-and-poisson-equations.md).
Its principal part is the Laplacian, so it is elliptic (classification by
the principal part, [classification](/definitions/second-order-pde-classification.md)).

Arfken et al. list "Helmholtz and time-independent diffusion equations,
$\nabla^2\psi \pm k^2\psi = 0$" among the most frequent PDEs of physics:
elastic waves, acoustics, electromagnetic waves, nuclear reactors (§9.1,
p. 402). The minus sign (the *modified* Helmholtz equation, a name neither
book uses) they treat as "a somewhat peculiar case" of the plus sign with
imaginary $k$ (p. 428). Riley et al. call $\nabla^2u - k^2u = 0$ the
Klein–Gordon form (Exercise 20.25, p. 711), while Arfken et al. reserve
"Klein–Gordon" for the four-dimensional equation (p. 403): a difference of
naming only.

## Separated solutions

Both books separate it in three coordinate systems ([separation of
variables](/methods/separation-of-variables.md)):

* **Cartesian:** products of exponentials or sines and cosines with
  $k_x^2 + k_y^2 + k_z^2 = k^2$, the plane waves
  $e^{i\mathbf k\cdot\mathbf x}$ (Riley et al., eqs. 21.6–21.8, p. 716;
  Arfken et al., eqs. 9.29–9.41, pp. 415–417).
* **Cylindrical:** the radial factor solves Bessel's equation (Riley et
  al., eq. 21.55, pp. 738–739; Arfken et al., eqs. 9.53–9.65,
  pp. 421–422).
* **Spherical:** the angular factors are the same as for Laplace's
  equation, and the radial factor is $j_\ell(kr)$ or $y_\ell(kr)$, i.e.
  $r^{-1/2}J_{\ell+1/2}(kr)$ and its partner (Riley et al., eqs.
  21.56–21.57, pp. 740–741; Arfken et al., eqs. 9.80–9.86, pp. 426–428). For the minus
  sign the radial factors are the modified spherical Bessel functions
  (Arfken et al., p. 428).

The separation survives when $k^2$ is replaced by a sum of one-variable
functions adapted to the coordinates, and for $k^2 = k^2(r)$ in spherical
coordinates the angular factors do not change (Arfken et al., pp. 417,
422, 426; e.g. the hydrogen atom and the three-dimensional oscillator,
p. 428).

## Eigenvalue problem

With $U = 0$ on a closed boundary, nontrivial solutions exist only for
particular values of $k^2$; finding them "is an eigenvalue problem and is
important for physics" (Arfken et al., §9.3, p. 413). Worked cases:

* a circular membrane clamped at radius $R_0$: $J_n(kR_0) = 0$, lowest
  frequencies $\omega R_0/c \approx 2.40, 3.83, 5.14, 5.52$ (Riley et al.,
  pp. 739–740; see [wave equation](/definitions/wave-equation.md));
* a rectangular box: $k^2 = \pi^2(n_1^2/L_x^2 + n_2^2/L_y^2 + n_3^2/L_z^2)$
  for positive integers $n_1$, $n_2$, $n_3$, a discrete spectrum (Arfken et al., Example
  9.4.2, eqs. 9.48–9.52, pp. 419–420, written for the Schrödinger equation
  $-\tfrac12\nabla^2U = \lambda U$, so $k^2 = 2\lambda$);
* a closed cylinder of radius $R_0$ and length $L$: lowest eigenvalue of
  $-\nabla^2$ equal to $(2.4048/R_0)^2 + \pi^2/L^2$ (Arfken et al., Example
  9.4.3, pp. 422–424).

This is why Arfken et al. call their Table 9.1 of boundary data an
oversimplification: the Helmholtz equation with Dirichlet data on a closed
boundary does not always have a unique solution (p. 413; see
[boundary data by equation type](/results/boundary-data-by-equation-type.md)).

## Contradictions

* **Open — does $\nabla^2U - k^2U = 0$ have Dirichlet eigenvalues?**
  Arfken et al. state that "the Helmholtz PDE, $\nabla^2\psi \pm k^2\psi = 0$,
  … has solution(s) for Dirichlet conditions on a closed boundary only for
  certain values of its parameter $k$", an eigenvalue problem
  ([Arfken et al. (2013)](/sources/arfken-2013.md), §9.3, p. 413). Read as
  a statement about nontrivial solutions with homogeneous data, it
  includes the minus sign. Riley et al. prove, for
  $\nabla^2u - k^2u = 0$ with Dirichlet or Neumann data, that the
  difference $v$ of two solutions satisfies
  $\int|\nabla v|^2\,\mathrm dV + k^2\int|v|^2\,\mathrm dV = 0$, so $v = 0$
  for every real $k \ne 0$ ([Riley et al. (2006)](/sources/riley-2006.md),
  Exercise 20.25, p. 711, hint p. 712; [uniqueness
  theorem](/results/uniqueness-theorem-poisson.md)). The homogeneous
  minus-sign problem then has no nontrivial solution for any real $k$, so
  there is no discrete set of exceptional values. The claims are
  incompatible for the minus sign; they agree for the plus sign. The
  compiler reads Arfken's "$\pm$" as loose wording meant for the plus sign.
  That reading is a hypothesis; the entry stays open until a source
  settles it or the human closes it.

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), Exercise 20.25
  (pp. 711–712), §21.1 (p. 716), §21.3.2 (pp. 737–741).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.1 (pp. 402–403),
  §9.3 (p. 413), §9.4 (pp. 415–428), §9.7 (p. 439).
