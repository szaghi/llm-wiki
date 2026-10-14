---
type: Definition
title: "Wave equation"
description: "The model hyperbolic equation, laplacian of u equals u_tt over c squared: derived for the small transverse vibrations of a string, its one-dimensional general solution is two counter-propagating waves of fixed shape along the characteristics x - ct and x + ct, in three dimensions plane waves along any unit vector, and in bounded domains separated normal modes."
status: established
aliases: [one-dimensional wave equation, d'Alembert equation]
tags: [model-equation, hyperbolic, characteristics]
timestamp: 2026-10-14T00:00:00Z
---

# Wave equation

$$\nabla^2 u = \frac{1}{c^2}\,\partial_t^2 u$$
describes the displacement $u(\mathbf x, t)$ of a vibrating string,
membrane, solid, gas or liquid, and field components in electromagnetic
waves; $c$ is the speed of propagation
([Riley et al. (2006)](/sources/riley-2006.md), eq. 20.1, p. 676). It is
[hyperbolic](/definitions/second-order-pde-classification.md).
[Arfken et al. (2013)](/sources/arfken-2013.md) call it "the prototype
hyperbolic PDE" and list it, with the Klein–Gordon, telegraphy and elastic
wave equations, among the most frequent PDEs of physics (§9.1, p. 403;
§9.6, p. 435).

**Derivation (string).** For small transverse displacements of a uniform
string under uniform tension, the net vertical force on an element is the
tension times the difference of slopes. Newton's second law then gives
$\partial_x^2 u = c^{-2}\partial_t^2 u$, with $c^2$ the tension divided by
the mass per unit length (pp. 676–677). The approximations are small angles
($\sin\theta \approx \tan\theta$) and element mass equal to (line density)
$\times\,\Delta x$. An external force per unit length enters as a source
term; the membrane is the two-dimensional analogue (p. 677).

## One dimension

The characteristics are $x \mp ct = \text{const}$
([characteristic curves](/definitions/characteristic-curve.md), p. 704),
and the general solution is
$$u(x,t) = F(x - ct) + G(x + ct)$$
(eq. 20.23, p. 690; [general solution of constant-coefficient
second-order equations](/methods/constant-coefficient-second-order-general-solution.md)).
$F(x - ct)$ is a waveform of constant shape travelling in $+x$ at speed $c$,
and $G(x + ct)$ one travelling in $-x$ (§20.4, p. 693). Equal $F = G =
C_1\cos kx$ superpose to the standing wave
$2C_1\cos(kct)\cos kx$, with nodes where
$\cos kx = 0$ (p. 693; the book keeps a phase constant). Cauchy data on $t = 0$ give
[d'Alembert's formula](/results/dalembert-formula.md).

Arfken et al. state the same general solution from the two characteristic
families (§9.6, eq. 9.90, p. 435). They stress that $F$ and $G$ "need not
be sinusoidal or periodic, but may be entirely irregular", and need not be
related to each other. Their standing wave is
$\sin(x - ct) + \sin(x + ct) = 2\sin x\cos ct$, whose nodes are fixed while
those of a travelling wave move at $\pm c$ (p. 435). Separation of
variables yields standing waves, but "the totality of the solution set
from the separated variables has the same content as the traveling-wave
solutions": $\sin x\cos ct \pm \cos x\sin ct = \sin(x \pm ct)$
(pp. 435–436).

## Three dimensions

$u = F(\hat{\mathbf n}\cdot\mathbf x - ct) + G(\hat{\mathbf n}\cdot\mathbf x + ct)$
solves the equation for any unit vector $\hat{\mathbf n}$, the direction
of propagation (eq. 20.33, p. 695). This is plane waves only; the book
does not give a general solution for arbitrary data in three dimensions.
Separation in Cartesian coordinates gives the plane wave
$\exp[i(\mathbf k\cdot\mathbf x - \omega t)]$ with $\omega = c|\mathbf k|$,
a special case of eq. 20.33 (§21.1, eqs. 21.6–21.8, p. 716).

## Separated solutions and modes

Writing $u = U(\mathbf x)\mathcal T(t)$ with separation constant $k^2$
gives the [Helmholtz equation](/definitions/helmholtz-equation.md) $\nabla^2 U + k^2U = 0$ and
$\mathcal T = c_1e^{i\omega t} + c_2e^{-i\omega t}$, $\omega = kc$
(eqs. 21.52–21.54, p. 737; [separation of variables](/methods/separation-of-variables.md)).
For a circular membrane of radius $R_0$ clamped at its rim, the modes are
$J_n(kr)(c_1\cos n\phi + c_2\sin n\phi)e^{\pm i\omega t}$ with
$J_n(kR_0) = 0$. The four lowest frequencies are
$\omega R_0/c \approx 2.40, 3.83, 5.14, 5.52$, the second and third
two-fold degenerate (pp. 739–740, Fig. 21.8). In spherical polars the
radial zeros are not equally spaced (except for $\ell = 0$), so there is
no precise wavelength (p. 741).

## Appropriate data

Cauchy data on an open boundary (Table 20.1, p. 705; [boundary data by
equation type](/results/boundary-data-by-equation-type.md)); e.g. a
semi-infinite string whose end is moved in a prescribed way is
hyperbolic, open, Cauchy (Exercise 20.23(d), answer p. 712).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.1.1 (pp. 676–677),
  §20.3.3 (pp. 689–690), §20.4 (pp. 693–695), §20.6.2 (p. 704), §21.1
  (pp. 714–716), §21.3.2 (pp. 737–741).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §9.1 (p. 403), §9.3
  (p. 411), §9.6 (pp. 435–436).
