---
type: Definition
title: "Stiffness"
description: "Stiffness names problems on which ordinary explicit methods need steps far below the scale of the solution sought; the sources define it relative to the step (Curtiss–Hirschfelder 1952), by fast decaying or oscillatory eigenmodes, by implicit versus explicit Euler, and by a small parameter or scaled eigenvalues of a semi-discretization."
status: established
aliases: [stiff equation, stiff problem, stiff system, stiff ODE, stiffness parameter]
tags: [stiff, stability, implicit, explicit]
timestamp: 2026-10-29T18:13:00Z
---

# Stiffness

A differential equation is **stiff** when ordinary explicit methods can integrate it only with
steps much smaller than the variation of the solution of interest requires, while suitable
implicit (or exponential) methods can take steps set by that solution alone. The sources do
not share one formal definition. They give a step-relative definition for a scalar model
equation ([Curtiss & Hirschfelder (1952)](/sources/curtiss-1952.md)), a
spectral description by fast decaying transients
([Dahlquist (1963)](/sources/dahlquist-1963.md)) or fast oscillations
([Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md)), an operational test (implicit
against explicit Euler, Hochbruck & Ostermann 2010), and, for method-of-lines systems, scaled
eigenvalues per term and a stiffness parameter
([Kennedy & Carpenter (2003)](/sources/kennedy-2003.md)). Stiffness is the setting of
[A-stability](/properties/a-stability.md), of the [BDF](/methods/backward-differentiation-formula.md)
family, of [order reduction](/definitions/order-reduction.md) and of
[B-convergence](/definitions/b-convergence.md).

## The step-relative definition of Curtiss and Hirschfelder

Curtiss & Hirschfelder (1952) name the class: equations arising in chemical kinetics,
electrical circuit theory and missile guidance are "exceedingly difficult to solve by ordinary
numerical procedures", and "the differential equations to which this method applies are called
'stiff'" (Introduction, p. 235). In registry notation ($x\to t$, $\Delta x\to h$; $G$ and $a$
page-local) they consider the scalar equation

$$y'=\frac{y-G(t)}{a(t,y)},$$

whose right-hand side has the root $y=G(t)$ for each $t$. With $h$ "the desired resolution of
[$t$] or the interval which will be used in the numerical integration", the equation is stiff if

$$\Big\lvert\frac{a(t,y)}{h}\Big\rvert\ll1$$

and $G$ is well behaved, i.e. varies "considerably more slowly" than $\exp(t/a(t,G(t)))$ (§1,
Eqs. (1)–(2)). The definition is relative to the step one wants to use and is stated for this
scalar form only. *(Compiler check, not in the sources: for $a$ independent of $y$ the equation is linear,
$y'=\lambda(y-G)$ with $\lambda=1/a$, so $\lvert a/h\rvert\ll1$ reads $\lvert h\lambda\rvert\gg1$.)*

The structure of the solutions (§1, Eqs. (3)–(7), Figs. 1–2):

- **A smooth special solution.** If $a$ is small there is a solution $Y$ (page-local) close to
  $G$, obtained by successive approximation, $Y=\sum_{k\ge0}\big(a\,\tfrac{d}{dt}\big)^kG$ when
  $a$ does not depend on $y$.
- **Exponential departure.** Near $Y$ every other solution behaves like
  $y-Y=C\exp\big(\int dt/a(t,Y(t))\big)$ ($C$ page-local), so the family of solutions "horns
  out" about $Y$ in one direction of integration and converges onto it in the other.
- **Failure of ordinary methods.** With ordinary methods "small errors are rapidly magnified if
  the equations are integrated in the direction such that the family of solutions horn out,
  whereas the numerical solutions oscillate violently about $Y(x)$" in the opposite direction
  (§2, pp. 237–238).

Their remedy, "forward interpolation", is the origin of the
[backward differentiation formulas](/methods/backward-differentiation-formula.md): it converges
onto $Y$ from any starting value and in either direction of integration (§2–3, Figs. 3–4, on
$y'=5(y-t^2)$, i.e. $G=t^2$, $a=\tfrac15$, with $Y=t^2+0.4t+0.08$ as printed in the captions).
Systems are reduced to this case: "in any particular region, the differential equations can be
uncoupled by introducing suitable linear combinations of the original dependent variables"; the
stiff uncoupled equations are integrated by the new method and the others "by the more usual
procedures" (Introduction). The motivating example is the rate of formation of free radicals,
created and destroyed so fast that their production nearly balances their depletion (the
"pseudo-stationary state"), an approximation that is "not sufficiently accurate" for fast
reactions in flames or detonations (Introduction).

## Fast decaying transients

Dahlquist (1963, §1, p. 29) motivates [A-stability](/properties/a-stability.md) with the
long-time integration of a linear system $y'=Ly+u(t)$ ($u$ page-local) "where some of the
eigenvalues of [$L$] have large modulus but negative real part". The solution is
$y=w(t)+e^{tL}c$ with $w$ (page-local) often slowly varying; once the components of $e^{tL}c$
along those eigenvectors "have lost their importance in the physical system, one would like to
proceed with a step $h$, determined only by the behaviour of [$w$] and independent of the norm"
of $L$. Nonlinear problems of this type occur "in many fields, such as control engineering or
chemical engineering" (citing Hamming). The paper never uses the word "stiff". It calls
A-stability "an extreme formulation of the wishes in such situations" and notes that "in most
applications A-stability is not a necessary property".

Hochbruck & Ostermann (2010, §1, p. 210) describe the same class as problems whose Jacobian
"possesses eigenvalues with large negative real parts", typified by semilinear parabolic
problems and their spatial discretizations.

## The implicit-versus-explicit-Euler test

For that class, Hochbruck & Ostermann (2010, §1, p. 210) state "the usual definition of
stiffness": a differential equation is stiff "whenever the implicit Euler method works
(tremendously) better than the explicit Euler method". They give the reason as linear
stability: all available explicit integrators, "with the exception of Runge–Kutta–Chebyshev
methods", have a relatively small stability domain in the left half-plane, so they "require
unrealistically small step sizes" (see [stabilized explicit methods](/methods/stabilized-explicit-runge-kutta.md)).

## Highly oscillatory stiffness

Hochbruck & Ostermann (2010, §1, p. 210) treat a second class: highly oscillatory problems with
purely imaginary eigenvalues of large modulus. Explicit methods again lack stability, but here
implicit Euler "does not perform well either": its step is limited by accuracy, because "the
method tends to resolve all the oscillations in the solution". Hochbruck & Ostermann build
[exponential integrators](/methods/exponential-integrators.md) for both classes from the exact
propagator of a linearization. They recall that "in the early days of stiff problems" the
matrix exponential was replaced by rational (Padé) approximations, which gave implicit and
semi-implicit Runge–Kutta methods, [Rosenbrock methods and W-methods](/methods/rosenbrock-wanner-method.md)
(§1, p. 211).

## Stiffness in method-of-lines systems

Kennedy & Carpenter (2003, §1) linearize a semi-discretized convection–diffusion–reaction system
as $y'=(L^{\mathrm C}+L^{\mathrm D}+L^{\mathrm R})y$ (page-local operators for convection,
diffusion and reaction) and read stiffness off the scaled eigenvalues of each term:

- convection contributes predominantly imaginary scaled eigenvalues, diffusion predominantly
  real ones, and reaction mostly real ones that "may give rise to relatively large scaled
  eigenvalues";
- stable integration needs the stability domain to contain all of them, and accuracy needs the
  step no larger than the fastest relevant physical process;
- the difficulty arises when "stable integration ... can only proceed at a time scale
  substantially faster than any physically relevant time scale", which "may render a numerical
  method unacceptably inefficient"; it "may occur in regions of intense grid clustering or while
  using stiff chemistry", or from interface boundary conditions of multidomain formulations.

Their remedy is to change the method rather than the equations: an
[IMEX additive Runge–Kutta method](/methods/imex-runge-kutta.md) treats the stiff term
implicitly and the rest explicitly ([Kennedy–Carpenter ARK methods](/methods/kennedy-carpenter-ark-methods.md)).
In their tests stiffness is a parameter: $\varepsilon^{-1}=k_2/k_3$, a ratio of reaction rates,
with $\varepsilon=1$ the largest stiffness that explicit time advancement still integrates stably
(§7.4). They estimate $\varepsilon\approx10^{-7}$ for hydrocarbon flames with heptane–air
mechanisms integrated at the convective limit (time scales of about 1 fs against 10 ns; §8.1).
On singularly perturbed test problems the limit $\varepsilon\to0$ is an index-1
[differential-algebraic equation](/definitions/differential-algebraic-equation.md) (Kaps'
problem, §7.1); [Farrell et al. (2021)](/sources/farrell-2021.md) (§2.1) call DAEs "infinitely
stiff".

**Stiffness leakage.** Kennedy & Carpenter (2003, §8.1) require of an IMEX scheme that "the
stiffness remains truely separable. If this were not the case then stiffness would leak out of
the stiff terms and stiffen the nonstiff terms", seen as a loss of stability or a forced step
reduction of the explicit part. They measure it by the largest stable CFL number as $\varepsilon$
decreases and call it catastrophic when the step must shrink "in direct proportion to the
increase in reaction rate stiffness" (Tables 8–13).

## Consequences recorded by the sources

- **Order measured uniformly in the stiffness.** Hochbruck & Ostermann (2010, §1, p. 212) use
  the *stiff order*: a global error bound $Ch^p$ on finite intervals with $C$ depending on the
  interval and the problem class "but neither on the stiffness nor on the step size $h$"; the
  classical order "is always an upper bound to the stiff order". See
  [order reduction](/definitions/order-reduction.md) and
  [B-convergence](/definitions/b-convergence.md). Kennedy & Carpenter (2003, §8.3) observe the
  loss of order of IMEX Runge–Kutta methods at intermediate stiffness, $\varepsilon\approx h$.
- **Stability requirements.** A-stability and its variants are the linear-stability answer
  ([A-stability](/properties/a-stability.md)); A-stable linear multistep methods have order at
  most 2 ([Dahlquist's order barrier](/results/dahlquist-second-barrier.md)).
- **Method choice by spectrum.** Kennedy & Carpenter (2003, §1) state that SBDF methods, which
  use BDF for the implicit part, "may be quite effective for equations whose stiff terms give
  rise to predominately real eigenvalues"; Hochbruck & Ostermann's oscillatory class is the case
  in which damping implicit methods lose accuracy.

## Qualifications

- **No common definition.** The step-relative condition of Curtiss & Hirschfelder (1952), the
  method comparison quoted by Hochbruck & Ostermann (2010) as "the usual definition" (without a
  citation), and the spectral and efficiency descriptions of Dahlquist (1963) and Kennedy &
  Carpenter (2003) are different formulations, not competing values of one quantity. Curtiss &
  Hirschfelder state theirs for one scalar equation and cover systems only by local uncoupling,
  without formulas.
- **Direction of integration.** Curtiss & Hirschfelder apply their method in both directions:
  Fig. 3 integrates in the direction in which the solutions "horn out" ($a/h=\tfrac15$), Fig. 4
  in "the direction of convergence of the manifold of solutions" ($a/h=-\tfrac15$) (§2, p. 240).
- **Stiffness parameters are problem-specific.** Kennedy & Carpenter's $\varepsilon$ is measured
  relative to a baseline mechanism; the registry $\varepsilon$ denotes such a parameter page by
  page.

# Citations

- [Curtiss & Hirschfelder (1952)](/sources/curtiss-1952.md) — Introduction (term, applications, systems by uncoupling, pseudo-stationary state); §1 (Eqs. (1)–(7), Figs. 1–2); §2 (behaviour of ordinary methods, pp. 237–238); §2–3 (Figs. 3–4).
- [Dahlquist (1963)](/sources/dahlquist-1963.md) — §1, p. 29 (transient motivation of A-stability, "extreme formulation").
- [Hochbruck & Ostermann (2010)](/sources/hochbruck-2010.md) — §1, pp. 210–212 (two classes of stiff problems, "usual definition", oscillatory case, Padé history, stiff order).
- [Kennedy & Carpenter (2003)](/sources/kennedy-2003.md) — read as NASA/TM-2001-211038: §1 (scaled eigenvalues, inefficiency, SBDF remark), §7.1, §7.4 (stiffness parameter), §8.1 (stiffness leakage, Tables 8–13, flame estimate), §8.3.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.1 (DAEs "infinitely stiff").
