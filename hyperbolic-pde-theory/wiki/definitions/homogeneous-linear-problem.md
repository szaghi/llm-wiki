---
type: Definition
title: "Homogeneous equations and homogeneous problems"
description: "A linear equation is homogeneous when every multiple of a solution is a solution, a problem when its boundary conditions share the property; the general solution of an inhomogeneous linear problem is any particular solution plus the general solution of the homogeneous problem, and inhomogeneity can be moved between the boundary data and the equation."
status: established
aliases: [homogeneous boundary conditions, superposition principle, complementary function and particular integral]
tags: [linearity, superposition, boundary-conditions]
timestamp: 2026-10-14T00:00:00Z
---

# Homogeneous equations and homogeneous problems

**Definitions** ([Riley et al. (2006)](/sources/riley-2006.md), §20.3.2,
p. 685). An equation is **homogeneous** if the fact that $u$ is a solution
implies that $C_1u$ is one for every constant $C_1$. A **problem**
(equation plus boundary conditions) is homogeneous if in addition the
boundary conditions satisfied by $u$ are satisfied by $C_1u$; such
conditions are *homogeneous boundary conditions*. The first-order equation
$b_1\partial_x u + b_2\partial_y u + c_0u = \psi$ is homogeneous only
if $\psi = 0$; the condition $u(1,y) = 2y + 1$ is not homogeneous, while
$u = 0$ on a curve is.

The book restricts itself to linear equations, for which a homogeneous
equation is one with $\psi = 0$ and solutions superpose: any linear
combination of solutions is a solution (§20.3.2; §21.2, eq. 21.16). The
boundary conditions do not superpose unless they are homogeneous (p. 685).

[Arfken et al. (2013)](/sources/arfken-2013.md) define a linear PDE as
$\mathcal Lu = \psi$ with $\mathcal L$ a linear differential operator,
homogeneous if $\psi = 0$, and they state the superposition principle for
homogeneous linear PDEs (§9.1, pp. 401–402). This agrees with Riley et al.
for linear equations. Linearity is a property of the operator, not of its
coefficients: $p(x)\,\mathrm d/\mathrm dx + q(x)$ is linear whatever $p$
and $q$ are (§7.1, p. 330).

**Qualification: two definitions of a homogeneous ODE.** Arfken et al. call
an ODE homogeneous "if the dependent variable … occurs to the same power in
all its terms" (§7.1, p. 330). Riley et al.'s definition is invariance
under $u \to C_1u$. For linear equations both reduce to $\psi = 0$; for
nonlinear ones, terms of a common degree in $u$ and its derivatives are a
sufficient condition for that invariance (compiler's remark). Arfken et al.
also flag a third, unrelated usage: a first-order ODE "homogeneous in $x$
and $y$", in which the combined power of $x$ and $y$ is the same in every
term ([first-order ODE methods](/methods/first-order-ode-solution-methods.md);
§7.2, p. 334).

## Structure of the solution

The general solution of an inhomogeneous linear problem is the sum of any
particular solution and the general solution of the corresponding
homogeneous problem (p. 685–686). Concretely, for
$\partial_x u - x\,\partial_y u + c_0u = \psi$ ($c_0$ constant) with $u(0,y) = g(y)$ the
solution is $u = v + u_h$, with $v$ any solution of the full problem and $u_h$
the general solution of the homogeneous equation with $u_h(0,y) = 0$; if the
data suffice, $u_h \equiv 0$ (eqs. 20.16–20.17, p. 686). Arfken et al.
state the same structure for linear ODEs: for a first-order linear ODE the
general solution is a particular solution plus the general homogeneous
solution, and two solutions of the inhomogeneous equation differ by a
solution of the homogeneous one (§7.2, eqs. 7.16–7.17, p. 337); for second
order, $y = c_1y_1 + c_2y_2 + y_p$ (eq. 7.26, p. 346). Alternatively one
first writes the general solution of the inhomogeneous equation and then
fits the data (p. 686). The book adds that the particular solution must
not already be contained in the homogeneous general solution, as for ODEs
(p. 686). The statement is made for first-order equations and asserted to
hold for linear PDEs of higher order (p. 687). The ODE form is
$y = y_c + y_p$ ([structure of linear ODE solutions](/results/linear-ode-solution-structure.md)).

## Moving the inhomogeneity

A change of dependent variable converts inhomogeneous boundary conditions
into an inhomogeneous equation with homogeneous conditions, or back
(§21.5, p. 752):

* **ODEs.** For $n$ conditions, set $v = y - y_b(x)$ with $y_b$ a polynomial of
  degree $n - 1$ that satisfies them, e.g. the straight line through
  the two prescribed end values of a two-point problem
  (§15.2.5, pp. 515–516).
* **PDEs.** For a bar held at $u(0,t) = 0$ with a constant heat flux into
  the end $x = L$, write $u = v(x,t) + u_s(x)$ with $u_s$ the linear
  steady-state profile; $v$ then satisfies the diffusion equation with
  conditions that are homogeneous in $x$ and a modified initial condition,
  and is found by [separation of variables](/methods/separation-of-variables.md)
  (§21.2, pp. 723–724).

A Green's function solves the homogeneous-boundary problem directly; the
representation formula of [Green's functions for PDEs](/methods/greens-functions-for-pdes.md)
also handles inhomogeneous boundary data (§21.5.2).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §20.3.2 (pp. 685–687),
  §21.2 (pp. 717–724), §15.2.5 (pp. 515–516), §21.5 (p. 752).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §7.1 (p. 330), §7.2
  (pp. 334, 337), §7.5 (p. 346), §9.1 (pp. 401–402).
