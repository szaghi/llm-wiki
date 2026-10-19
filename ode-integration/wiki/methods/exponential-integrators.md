---
type: Method
title: "Exponential integrators and φ-functions"
description: "Exponential integrators treat a stiff linear part exactly through its exponential and the φ-functions; the page records the φ-function conventions, the exponential structure of multirate infinitesimal methods with an exact fast solve, the exponential reformulation of stiff kinetic relaxation, and Magnus and commutator-free quasi-Magnus methods for linear non-autonomous problems."
status: established
aliases: [phi-functions, exponential Runge–Kutta, ExpRK, exponential Rosenbrock, EPIRK, integrating factor method, Magnus integrator, commutator-free quasi-Magnus, CFQM, exponential midpoint rule]
tags: [exponential, stiff, kinetic, asymptotic-preserving, multirate]
timestamp: 2026-10-19T12:00:00Z
---

# Exponential integrators and φ-functions

An exponential integrator advances a problem with a stiff linear part, typically the
semilinear form $y'=Ly+N(t,y)$ (page-local $N$: the non-stiff remainder), by evaluating
the exponential $e^{hL}$ and related functions of $hL$ exactly, so that the stiffness of $L$
imposes no step-size restriction. The functions involved are the **φ-functions**

$$\phi_0(z)=e^z,\qquad \phi_k(z)=\int_0^1e^{(1-\theta)z}\frac{\theta^{k-1}}{(k-1)!}\,d\theta\quad(k\ge1),$$

which satisfy $\phi_k(0)=1/k!$ and $\phi_{k+1}(z)=\big(\phi_k(z)-1/k!\big)/z$; they arise
from the variation-of-constants formula
$y(t_n+h)=e^{hL}y_n+h\int_0^1e^{(1-\theta)hL}N\big(t_n+\theta h,y(t_n+\theta h)\big)\,d\theta$
when $N$ is replaced by a polynomial in $\theta$ *(compiler statement of the standard
background; the sources use the formula without stating it in this form)*. Exponential
Runge–Kutta, exponential Rosenbrock and EPIRK methods are named by Chinomona & Reynolds,
alongside IMEX additive Runge–Kutta methods and general linear methods, as the main
families for problems that couple stiff and non-stiff processes
([Chinomona & Reynolds 2021](/sources/chinomona-2021.md), §1). The ingested sources
develop three uses of the idea, below; none of them develops exponential Runge–Kutta
order theory itself.

## Convention for φ-functions

Chinomona & Reynolds (2021, §3) define $\varphi_k(z)=\int_0^1e^{z(1-t)}t^{k-1}\,dt$ without
the factor $1/(k-1)!$, with the recursion $\varphi_{k+1}(z)=(k\varphi_k(z)-1)/z$. Their
functions are $(k-1)!\,\phi_k$ in the registry normalisation above; the two recursions are
equivalent. This is a convention difference, not a disagreement.

## Multirate infinitesimal methods as exponential integrators

In a [multirate infinitesimal method](/methods/multirate-infinitesimal-methods.md) each
slow stage is reached by solving a modified fast problem whose forcing is a polynomial in
time built from slow stage values. If the fast part is linear and solved exactly, every
stage is an exponential-integrator stage. Chinomona & Reynolds (2021, §3, Eqs. 3.1–3.3)
use this to obtain the linear stability function of
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) methods on
$y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$ (page-local
eigenvalues of the fast, slow-explicit and slow-implicit parts;
$z^{\{\cdot\}}=H\lambda^{\{\cdot\}}$ with macro step $H$). With page-local $\Delta c_i$ the
stage increments of the slow abscissae and $\omega^{(k)}_{ij}$, $\gamma^{(k)}_{ij}$ the
entries of the registry's explicit and implicit coupling matrices $\Omega^{(k)}$,
$\Gamma^{(k)}$ (the source writes $\omega^{\{k\}}_{ij}$, $\gamma^{\{k\}}_{ij}$), variation of constants gives,
in registry normalisation,

$$\begin{aligned}
Y_i&=e^{\Delta c_iz^{\{\mathrm f\}}}Y_{i-1}+z^{\mathrm E}\sum_{j<i}\eta_{ij}Y_j+z^{\mathrm I}\sum_{j\le i}\mu_{ij}Y_j,\\
\eta_{ij}&=\sum_k\omega^{(k)}_{ij}\,k!\,\phi_{k+1}\big(\Delta c_iz^{\{\mathrm f\}}\big),\qquad
\mu_{ij}=\sum_k\gamma^{(k)}_{ij}\,k!\,\phi_{k+1}\big(\Delta c_iz^{\{\mathrm f\}}\big)
\end{aligned}$$

(page-local $\eta_{ij},\mu_{ij}$; the source writes $\varphi_{k+1}$ without the $k!$). The
stability function $R(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})$ is the last component
of the solution of this lower-triangular linear system with $Y_1=1$ (Eq. 3.3), and
defines the joint stability region of
[multirate linear stability](/definitions/multirate-linear-stability.md).

## Exponential reformulation of stiff kinetic relaxation

For the space-homogeneous kinetic equation $\partial_tF=\varepsilon^{-1}Q(F)$ (page-local,
as on [BGK penalization](/methods/bgk-penalization.md): $F$ the distribution function, $Q$
the collision operator, $\mathcal M$ its local equilibrium, which is constant in time in the
homogeneous case, and $\beta>0$ a penalization constant), Dimarco & Pareschi (2011) rewrite
the equation exactly as

$$\partial_t\Big[(F-\mathcal M)e^{\beta t/\varepsilon}\Big]=\frac{Q(F)-\beta(\mathcal M-F)}{\varepsilon}\,e^{\beta t/\varepsilon},$$

as recalled by [Jin (2022)](/sources/jin-2022.md) (§5.2, Eq. 5.7). The factor
$e^{-\beta t/\varepsilon}$ "removes the stiffness and numerically forces the convergence
between $F$ and $\mathcal M$"; applying any explicit Runge–Kutta method to the transformed
variable gives schemes that are "not only of high order but also satisfy the AP property
automatically", and $\beta$ is chosen as the smallest value that preserves the positivity of
$F$ (p. 451). Li & Pareschi (2014) extend it to the inhomogeneous equation, with the
Maxwellian evolving inside the step through its moments (Eqs. 5.8–5.10), and claim
positivity, high-order accuracy and "strong AP properties" (p. 452). The penalization by
$\beta(\mathcal M-F)$ is the same device as in [BGK penalization](/methods/bgk-penalization.md);
see also [asymptotic-preserving schemes](/definitions/asymptotic-preserving-scheme.md) and
[positivity preservation](/properties/positivity-preservation.md). Hu & Shu (2019) give a
second-order AP and positivity-preserving exponential Runge–Kutta method for relaxation
systems (as recalled by Jin 2022, §6.1). Structurally this is an integrating-factor
(Lawson-type) transformation with the scalar linear part $-\beta/\varepsilon$ *(compiler
classification, not in the source)*.

## Magnus and commutator-free quasi-Magnus methods

For linear non-autonomous problems $y'=L(t)y$ the exact solution is
$y(t_n+h)=e^{\Upsilon(h)}y_n$, with $\Upsilon$ a series of iterated integrals of nested
commutators (the Magnus expansion). Truncating it and using two-point Gauss quadrature
$c_{1,2}=\tfrac12\mp\tfrac{\sqrt3}6$ gives the fourth-order Magnus integrator

$$y_{n+1}=\exp\Big(\tfrac h2(L_1+L_2)+\tfrac{\sqrt3}{12}h^2[L_2,L_1]\Big)y_n,\qquad L_j=L(t_n+c_jh)$$

([Blanes et al. 2024](/sources/blanes-2024.md), §6.3, Eqs. 6.32–6.33; page-local $L_j$ and
$\Upsilon$, the source's $\Omega$, renamed because $\Omega^{(k)}$ is the registry's MRI coupling
matrix used above). For the Schrödinger equation with a smooth time-dependent potential, Magnus
integrators keep their full order uniformly in the space discretization (as recalled from
Hochbruck & Lubich 2003). Their drawback is the cost of the commutators, acute in two and
three space dimensions. **Commutator-free quasi-Magnus (CFQM)** methods, "a different class
of exponential integrators", replace the single exponential by a product
$y_{n+1}=e^{hB_J}\cdots e^{hB_1}y_n$ of exponentials of linear combinations
$B_j=\sum_ka_{jk}L(t_n+c_kh)$ (page-local $B_j$, $a_{jk}$, $c_k$). Examples are the
exponential midpoint rule $y_{n+1}=e^{hL(t_n+h/2)}y_n$ (order 2, Eq. 6.34) and the
fourth-order method with $c_{1,2}=\tfrac12\mp\tfrac{\sqrt3}6$,
$a_{11}=a_{22}=\tfrac14+\tfrac{\sqrt3}6$, $a_{12}=a_{21}=\tfrac14-\tfrac{\sqrt3}6$,
$y_{n+1}=e^{hB_2}e^{hB_1}y_n$ (Eq. 6.35). CFQM methods are unconditionally stable with
full order under low regularity; schemes up to order 6 and 8 exist (§6.3, as recalled
from Blanes et al. 2017, 2018, 2021 and Alvermann & Fehske 2011).

## Exact linear flows inside splittings

[Operator splitting](/methods/operator-splitting.md) uses exact exponentials of a linear
part in another way: the split-step Fourier and time-splitting spectral methods solve the
free Schrödinger flow exactly in Fourier space (Jin 2022, §3.1; Blanes et al. 2024, §1.6),
and rotation–kick splittings integrate the quadratic part of a Hamiltonian exactly
(Blanes et al. 2024, §4.2, §5). Jin (2022, §3.3) shows that exact sub-flows are what lets
the time-splitting spectral method stay asymptotic-preserving in time for semiclassical
observables.

## Qualifications

- Jin's claim that explicit Runge–Kutta methods on the exponential reformulation are "of
  high order" refers to order at fixed $\varepsilon$; uniform-in-$\varepsilon$ high order is
  not claimed in the source (Jin 2022, §5.2).
- The function $P$ in the inhomogeneous reformulation (Jin 2022, Eq. 5.8) is used without
  definition in the source (printed slip).

# Citations

- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §1 (ExpRK, ExpRB, EPIRK as method families), §3, Eqs. 3.1–3.3 (exact fast solve, φ-functions, stability function; unnormalised convention).
- [Jin (2022)](/sources/jin-2022.md) — §5.2, Eqs. 5.6–5.10 (exponential reformulation of kinetic relaxation, Dimarco & Pareschi 2011, Li & Pareschi 2014), §6.1 (Hu & Shu 2019), §3.1–3.3 (exact sub-flows in time splitting).
- [Blanes et al. (2024)](/sources/blanes-2024.md) — §6.3, Eqs. 6.32–6.35 (Magnus and CFQM integrators), §1.6, §4.2, §5 (exact linear flows in splittings).
