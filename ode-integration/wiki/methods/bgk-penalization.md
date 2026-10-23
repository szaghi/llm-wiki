---
type: Method
title: "BGK penalization"
description: "Asymptotic-preserving time stepping for stiff kinetic collision operators: subtract a BGK relaxation term β(M−F)/ε, treat it implicitly and the remainder explicitly, so that conservation makes the implicit step explicit; it is AP after an initial transient, and the successive-penalty variant reaches the limit in one step."
status: established
aliases: [penalization method, Filbet–Jin penalization, BGK penalty, successive penalization]
tags: [asymptotic-preserving, imex, kinetic, stiff]
timestamp: 2026-10-19T07:44:00Z
---

# BGK penalization

BGK penalization is a time-integration device for kinetic equations whose collision
operator is stiff (scaled by $1/\varepsilon$, $\varepsilon$ the Knudsen number) and too
complicated to treat implicitly. The method subtracts a simple linear relaxation operator
of BGK type with a constant rate $\beta$. The subtracted copy is treated implicitly. The
remainder, the full collision operator minus the penalty, is treated explicitly. Because
the BGK operator conserves mass, momentum and energy, the implicit step can be carried out
explicitly. The scheme is [asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md)
in the limit to the compressible Euler equations
([Jin 2022](/sources/jin-2022.md), §5.1, reviewing Filbet & Jin 2010).

**Page-local notation.** $F(t,x,v)$ is the particle distribution (the sources' $f$,
renamed to keep $f$ for the vector field). $Q(F)$ is the collision operator, with
gain–loss split $Q(F)=Q^+(F)-F\,Q^-(F)$. $\mathcal M=\mathcal M[F]$ is the local
Maxwellian with the same density, velocity and temperature as $F$.
$\mathbf m(v)=(1,v,\lvert v\rvert^2/2)^\top$ are the collision invariants. $\beta>0$ is
the penalization constant. Time levels are subscripts, $F_n\approx F(t_n)$.

## Penalized equation and scheme

The Boltzmann equation $\partial_tF+v\cdot\nabla_xF=\frac1\varepsilon Q(F)$ is rewritten
exactly as

$$\partial_tF+v\cdot\nabla_xF=\underbrace{\frac{Q(F)-\beta(\mathcal M-F)}{\varepsilon}}_{\text{less stiff: explicit}}+\underbrace{\frac{\beta(\mathcal M-F)}{\varepsilon}}_{\text{stiff: implicit}}$$

(Jin 2022, eq. (5.1)). The constant $\beta$ approximates the Fréchet derivative of $Q$
around $\mathcal M$. In practice $\beta=\sup_v\lvert Q^-(F)\rvert$, and it may vary in time
and space (Yan & Jin 2013, as recalled by Jin). The first-order IMEX discretization is

$$\frac{F_{n+1}-F_n}{h}+v\cdot\nabla_xF_n=\frac{Q(F_n)-\beta(\mathcal M_n-F_n)}{\varepsilon}+\frac{\beta(\mathcal M_{n+1}-F_{n+1})}{\varepsilon}\qquad\text{(5.2)}.$$

**Explicit implementation.** Multiplying by $\mathbf m(v)$ and integrating in $v$
cancels both collision terms, because $Q$ and the BGK operator conserve the collision
invariants. This leaves an explicit update of the moments,

$$\frac{1}{h}\int\mathbf m(v)\,(F_{n+1}-F_n)\,dv+\nabla_x\cdot\int\mathbf m(v)\,v\,F_n\,dv=0\qquad\text{(5.3)},$$

which gives density, velocity and temperature at $t_{n+1}$, hence $\mathcal M_{n+1}$.
Equation (5.2) is then linear in $F_{n+1}$ and is solved pointwise. This is the
Coron–Perthame (1991) device of "inverting the implicit BGK term explicitly" (Jin 2022,
§5.1). No Newton iteration and no inversion of $Q$ are required.

Solving (5.2) for $F_{n+1}$ gives *(compiler algebra, not in the sources)*

$$F_{n+1}=\frac{\varepsilon}{\varepsilon+\beta h}\Big[F_n-h\,v\cdot\nabla_xF_n+\frac{h}{\varepsilon}\big(Q(F_n)-\beta(\mathcal M_n-F_n)\big)\Big]+\frac{\beta h}{\varepsilon+\beta h}\,\mathcal M_{n+1}.$$

As $\varepsilon\to0$ at fixed $h$, the first term tends to
$\big(Q(F_n)-\beta(\mathcal M_n-F_n)\big)/\beta$, which vanishes only if $F_n$ is already
near equilibrium. This is why the AP property below holds only after a transient.

## Asymptotic property

The Euler limit requires $F_n=\mathcal M_n$ for all $n$ as $\varepsilon\to0$ with $h$ and
$\Delta x$ fixed. Filbet & Jin (2010), as recalled by Jin (2022, §5.1), show formally
that $F_n=\mathcal M_n+O(\varepsilon)$ implies $F_{n+1}=\mathcal M_{n+1}+O(\varepsilon)$.
Numerically, whatever the initial datum, $F_n=\mathcal M_n+O(\varepsilon)$ holds for every
$n$ beyond some $N$ (eq. (5.4)). The scheme is therefore consistent with the compressible
Euler equations "after an initial transient time". With well-prepared data the transient
is absent. The moment update (5.3) is then a kinetic scheme for the Euler equations.

**Successive penalization** (Yan & Jin 2013; Jin 2022, Remark 5.1) splits the penalty
into two half-strength implicit steps,

$$\begin{aligned}
\frac{F^*-F_n}{h}+v\cdot\nabla_xF_n&=\frac{Q(F_n)-\beta(\mathcal M_n-F_n)}{\varepsilon}+\frac{\beta(\mathcal M^*-F^*)}{2\varepsilon},\\
\frac{F_{n+1}-F^*}{h}&=\frac{\beta(\mathcal M_{n+1}-F_{n+1})}{2\varepsilon},
\end{aligned}$$

and is AP in one time step. This removes the initial-layer restriction.

## The general idea and its uses

The principle is to penalize a complicated stiff operator by a simpler one that can be
inverted, often linear, and treat only the simple one implicitly (Jin 2022, §5.1). Jin
lists these instances:

- Fokker–Planck–Landau collisions are penalized by the linear Fokker–Planck operator
  $\nabla_v\cdot\big(\mathcal M\nabla_v(F/\mathcal M)\big)$ (Jin & Yan 2011). An explicit
  Fokker–Planck–Landau step would need $h=O(\varepsilon(\Delta v)^2)$, with $\Delta v$ the
  velocity mesh.
- Quantum Boltzmann (Filbet, Hu & Jin 2012), quantum Fokker–Planck–Landau (Hu, Jin & Yan
  2012) and multi-species Boltzmann (Jin & Li 2013).
- BGK penalization inside a [micro–macro decomposition](/methods/micro-macro-decomposition.md),
  which avoids inverting the linearized collision operator (Gamba, Jin & Liu 2019).
- The unified gas-kinetic scheme of Liu, Xu, Sun & Cai (2016) ends with a similar linear
  combination of Boltzmann and BGK operators.

The motivation is the explicit stiffness restriction $h=O(\varepsilon)$ for the Boltzmann
collision term (Jin 2022, §5.1).

## Exponential reformulation with the same penalty

The same penalty supports an exponential, integrating-factor formulation
(Dimarco & Pareschi 2011; Jin 2022, §5.2). For the space-homogeneous equation
$\partial_tF=\frac1\varepsilon Q(F)$, where $\mathcal M$ is constant in time,

$$\partial_t\Big[(F-\mathcal M)\,e^{\beta t/\varepsilon}\Big]=\frac{Q(F)-\beta(\mathcal M-F)}{\varepsilon}\,e^{\beta t/\varepsilon}\qquad\text{(5.7)},$$

an exact reformulation. The factor $e^{-\beta t/\varepsilon}$ "removes the stiffness and
numerically forces the convergence between $F$ and $\mathcal M$". Here $\beta$ is chosen
as the smallest value that keeps $F$ positive. Jin states that the construction extends to
all explicit Runge–Kutta methods, which are "not only of high order but also satisfy the AP
property automatically". The space-inhomogeneous version of Li & Pareschi (2014) evolves
the Maxwellian within the step through the moment equations (eqs. (5.8)–(5.10)). It is said
to preserve positivity, high-order accuracy and "strong AP properties". See
[exponential integrators](/methods/exponential-integrators.md) and
[positivity preservation](/properties/positivity-preservation.md).

## Qualifications

- **Order.** The penalization scheme displayed by Jin (2022) is first-order IMEX (forward
  and backward Euler). Higher-order IMEX versions are cited, not displayed. The high-order
  statement for the exponential version concerns fixed $\varepsilon$. Jin does not claim
  order uniform in $\varepsilon$ (see
  [asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md), Qualifications).
- **Printed slips in Jin (2022).** Eq. (5.1) labels the second brace "stiff, explicit", but
  (5.2) evaluates that term at $t_{n+1}$. The intended label is "stiff, implicit", implemented
  explicitly. In (5.8) a symbol $P$ appears without definition (presumably the gain-type
  part $Q+\beta F$).
- **"Strong AP".** Jin uses the phrase for the Li–Pareschi scheme (§5.2) without defining
  it. By contrast with the "after an initial transient" behaviour of (5.2), it presumably
  means AP without well-prepared data. That reading is the compiler's, not the source's.

# Citations

- [Jin (2022)](/sources/jin-2022.md) — §5.1 (eqs. (5.1)–(5.5), Remark 5.1), §5.2 (eqs. (5.6)–(5.10)), §5.3 (Gamba–Jin–Liu), p. 449 (design goals).
