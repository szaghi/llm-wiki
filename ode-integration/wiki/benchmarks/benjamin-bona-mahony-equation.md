---
type: Benchmark
title: "Benjamin–Bona–Mahony equation"
description: "The BBM equation u_t + u_x + u u_x − u_txx = 0 with periodic solitary-wave solutions and linear, quadratic and cubic invariants; its semidiscretizations test invariant preservation by Gauss–Legendre, relaxation and pseudo-energy-preserving methods."
status: established
aliases: [BBM equation, BBM solitary wave, regularized long-wave equation]
tags: [structure-preserving, geometric-integration, verification]
timestamp: 2026-10-20T06:18:00Z
---

# Benjamin–Bona–Mahony equation

The Benjamin–Bona–Mahony (BBM) equation on a periodic interval is

$$\partial_tu+\partial_xu+u\,\partial_xu-\partial_t\partial_x^2u=0,\qquad\text{i.e.}\qquad(I-\partial_x^2)\,\partial_tu+\partial_x\Big(\frac{u^2}2+u\Big)=0$$

([Farrell et al. (2021)](/sources/farrell-2021.md), §4.4.2;
[Bleecke & Ranocha (2026)](/sources/bleecke-2026.md), Eq. (19);
[de León et al. (2025)](/sources/deleon-2025.md), Eq. (25)). The
operator $I-\partial_x^2$ on the time derivative makes the semi-discrete system
non-stiff in the usual sense but couples all unknowns through a mass-matrix
solve. Its solitary waves travel without change of shape, so the exact
solution is known for all time.

## Solitary wave

With speed $c_\star>1$ (page-local),

$$u(t,x)=A_\star\operatorname{sech}^2\big(K_\star(x-c_\star t)\big),\qquad A_\star=3(c_\star-1),\quad K_\star=\tfrac12\sqrt{1-1/c_\star},$$

(Bleecke & Ranocha (2026), Eqs. (20)–(21); de León et al. (2025),
§4.1.4), both with $c_\star=1.2$. Farrell et al. (2021, §4.4.2) write
$u(x,0)=\frac{3c^2}{1-c^2}\operatorname{sech}^2\big(\tfrac12(cx+\delta)\big)$
with $c=\tfrac12$ (page-local $c$, $\delta$), speed $1/(1-c^2)=\tfrac43$;
this is the same family with $c_\star=\tfrac43$, $A_\star=1$,
$K_\star=\tfrac14$ *(compiler check, not in the sources)*.

## Invariants

The equation conserves the mass $\int u$, the quadratic invariant
$\int(u^2+(\partial_xu)^2)$ and a cubic one, which for the Hamiltonian form
$\partial_tu=-(I-\partial_x^2)^{-1}\partial_x\,\delta\mathcal H/\delta u$ is
$\mathcal H=\int(\tfrac12u^2+\tfrac16u^3)$ (page-local $\mathcal H$; de León
et al. (2025), Eq. (28); Farrell et al. (2021), Eqs. (26)–(28)).
Semidiscretizations are chosen to keep some of them:

* Fourier collocation conserving a discrete
  $\tfrac12\int(u^2+(\partial_xu)^2)$ (Bleecke & Ranocha (2026), Eq. (22), after
  Ranocha et al., via SummationByPartsOperators.jl and FFTW.jl);
* the conservative Fourier semidiscretization
  $u_t+(I-D_2)^{-1}D_1(\tfrac12u^2+u)=0$ (page-local $D_1$, $D_2$, Fourier
  differentiation matrices), which conserves discrete mass and the discrete
  Hamiltonian (de León et al. (2025), Eq. (27), after Linders et al.);
* $P^1$ Galerkin on $[0,100]$, $\Delta x=0.1$, in Irksome (Farrell et al.
  (2021)).

## Uses in the sources

* **Gauss–Legendre methods** (Farrell et al. (2021), §4.4.2, Table 2): to
  $T=18$, one- and two-stage Gauss–Legendre conserve the linear and quadratic
  invariants to $O(10^{-15})$, while the cubic one drifts to 0.9948969 and
  0.9999990 of its initial value. Implicit midpoint gives about 0.15% relative
  $L^2$ error at $h=\Delta x$ and over 10% at $h=10\Delta x$; two-stage
  Gauss–Legendre at $h=10\Delta x$ gives 0.14%. See
  [symplecticity](/properties/symplecticity.md).
* **Relaxation with FSAL pairs** (Bleecke & Ranocha (2026), §3, Fig. 1): BS3
  and DP5 in four variants; FSAL-R and R-FSAL reach the naive relaxation
  accuracy at the baseline's right-hand-side count. See
  [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md).
* **Pseudo-energy-preserving methods** (de León et al. (2025),
  §4.1.4, Fig. 3): on $[-90,90]$, PEP(4,2,5) has smaller long-time errors than
  explicit midpoint with $h_0=0.05$ to $t=10^3$. See
  [pseudo-energy-preserving RK](/methods/pseudo-energy-preserving-runge-kutta.md).

## Qualifications

* Bleecke & Ranocha (2026, Eq. (21)) print the domain $[0,2]$ with
  $c_\star=1.2$, for which $1/K_\star\approx4.9$ exceeds the period: the
  solitary wave would not be near-periodic there. de León et al. (2025)
  use the same wave on $[-90,90]$. The printed domain is probably a slip
  *(compiler check, not in the sources; the domain actually run is not recoverable from
  the paper)*. Bleecke & Ranocha print
  no mode count, final time or tolerances.
* Farrell et al. (2021, Eq. (28)) print the cubic invariant as
  $\int((\partial_xu)^2+\tfrac13u^3)$. This equals
  $\int(u^2+(\partial_xu)^2)+2\mathcal H-2\int u^2$ and so is conserved only if
  $\int u^2$ is, which BBM does not guarantee; the printed form is likely a
  slip for a multiple of $\mathcal H$ *(compiler check, not in the sources)*.
  Their Table 2 drift values may have been computed with either form.
* Farrell et al. spell the name "Benjamin-Bona-Mahoney" in Eq. (25).

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §2.2.3 (Eq. (25)), §4.4.2 (Eqs. (26)–(28), Fig. 6, Table 2).
- [Bleecke & Ranocha (2026)](/sources/bleecke-2026.md) — §3 (Eqs. (19)–(22), Fig. 1).
- [de León et al. (2025)](/sources/deleon-2025.md) — §4.1.4 (Eqs. (25)–(28), Fig. 3).
