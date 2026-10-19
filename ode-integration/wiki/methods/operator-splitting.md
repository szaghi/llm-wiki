---
type: Method
title: "Operator splitting: Lie–Trotter, Strang and dimensional splitting"
description: "Splitting methods advance $y'=f^{[1]}(y)+f^{[2]}(y)$ by composing the flows of the parts: Lie–Trotter is first order, Strang second order and symmetric; the page covers their error constants, conjugacy, linear stability, PDE (ADI, LOD, Peaceman–Rachford) forms, boundary order reduction and multirate and asymptotic-preserving uses."
status: established
aliases: [splitting method, Lie splitting, Godunov splitting, Strang–Marchuk splitting, Störmer–Verlet, leapfrog, split-step Fourier, time-splitting spectral method, ADI, LOD, fractional step method]
tags: [splitting, geometric-integration, order-reduction, multirate, asymptotic-preserving]
timestamp: 2026-10-19T12:00:00Z
---

# Operator splitting: Lie–Trotter, Strang and dimensional splitting

A splitting method for $y'=f(y)$ with $f=f^{[1]}+f^{[2]}$ (or more parts) replaces the
exact flow $\varphi_h$ by a composition of the flows $\varphi^{[i]}_{\theta h}$ of the
parts, each of which is assumed cheap, or exactly solvable, or treatable by its own
specialised solver. The general $s$-stage scheme is

$$\psi_h=\varphi^{[1]}_{a_{s+1}h}\circ\varphi^{[2]}_{b_sh}\circ\varphi^{[1]}_{a_sh}\circ\dots\circ\varphi^{[2]}_{b_1h}\circ\varphi^{[1]}_{a_1h},\qquad \sum_{j=1}^{s+1}a_j=\sum_{j=1}^{s}b_j=1,$$

with the consistency condition on the right
([Blanes et al. 2024](/sources/blanes-2024.md), §2.2: scheme Eqs. 1.10, 2.17; consistency
Eq. 2.22). When the last
$\varphi^{[1]}$ of a step merges with the first of the next step the scheme is FSAL.
The two basic members, Lie–Trotter and Strang, are the subject of this page; higher order
by composition is on [composition methods](/methods/composition-methods.md), the order
theory on [splitting order conditions](/results/splitting-order-conditions.md).

## Lie–Trotter and Strang

Throughout this page, in the linear case $y'=Ly$ with $L=L_1+L_2$ (page-local: $L_i$ the
linear operator of $f^{[i]}$), the flows are matrix exponentials.

**Lie–Trotter** is $\chi_h=\varphi^{[2]}_h\circ\varphi^{[1]}_h$, linearly
$y_{n+1}=e^{hL_2}e^{hL_1}y_n$. It is first order with local error
$\tfrac12h^2[L_1,L_2]+O(h^3)$; its adjoint is $\chi^*_h=\varphi^{[1]}_h\circ\varphi^{[2]}_h$
(Blanes et al. 2024, §1.1, Eqs. 1.5–1.6, 1.11). The underlying limit
$e^{t(L_1+L_2)}=\lim_n(e^{tL_2/n}e^{tL_1/n})^n$ is the Lie product formula. Blanes et al.
(§1.9) dispute its attribution to Lie: Lie's 1888 work is "clearly not from 1875" and the
formula does not evidently appear in it; the 1950s sources are Butler & Friedman (1955) and
Golden (1957), with Trotter (1959) for self-adjoint operators. They adopt the name
"Lie–Trotter"; the scheme is also called Godunov splitting in the hyperbolic-PDE literature.

**Strang** splitting is

$$S_h=\varphi^{[1]}_{h/2}\circ\varphi^{[2]}_h\circ\varphi^{[1]}_{h/2}=\chi_{h/2}\circ\chi^*_{h/2},$$

(page-local symbol $S_h$ for the Strang map). It is second order and time-symmetric,
$S_h=S_h^*$. Its local error in the linear case is

$$e^{h(L_1+L_2)}-e^{hL_1/2}e^{hL_2}e^{hL_1/2}=\frac{h^3}{24}\Big([L_1,[L_1,L_2]]+2[L_2,[L_1,L_2]]\Big)+O(h^4),$$

from the symmetric Baker–Campbell–Hausdorff formula
$\log(e^{hL_1/2}e^{hL_2}e^{hL_1/2})=h(L_1+L_2)-\tfrac{h^3}{24}[L_1,[L_1,L_2]]-\tfrac{h^3}{12}[L_2,[L_1,L_2]]+O(h^5)$
(Blanes et al. 2024, §1.1, Eqs. 1.8–1.9; §2.1.1). For nonlinear flows the same
expansions hold with Lie derivatives in place of $L_i$, but the exponentials of Lie
operators appear in the **reverse order** relative to the composition of maps (Eq. 1.15).
For $m>2$ parts the symmetric form nests: $\varphi^{[1]}_{h/2}\circ\varphi^{[2]}_{h/2}\circ\dots\circ\varphi^{[m]}_h\circ\dots\circ\varphi^{[2]}_{h/2}\circ\varphi^{[1]}_{h/2}$.

**Conjugacy.** Strang is conjugate to Lie–Trotter:
$S_h=\varphi^{[1]}_{-h/2}\circ\chi^*_h\circ\varphi^{[1]}_{h/2}$, so $n$ Strang steps equal $n$ Lie–Trotter steps plus an
initial and a final half-flow; Lie–Trotter has *effective* order 2 (Blanes et al. 2024,
§1.3, Eq. 1.18). This is the simplest instance of
[processing](/methods/processing-and-effective-order.md).

**Names.** On separable Hamiltonians $T(p)+V(q)$ Lie–Trotter gives the symplectic Euler
methods and Strang gives Störmer–Verlet (VTV or TVT); Strang is also leapfrog (wave
equations), the Wisdom–Holman map (Jacobi-coordinate splitting of planetary $N$-body
problems) and the split-step Fourier method (Schrödinger equations) (Blanes et al. 2024,
§1.4–1.6). Störmer–Verlet preserves linear first integrals and quadratic ones of the form
$p^\top Cq$ (§1.4). Ketcheson & Ranocha write Störmer–Verlet as an additive Runge–Kutta
method with tableaux $A^{\{1\}}=\begin{pmatrix}0&0\\1/2&1/2\end{pmatrix}$,
$A^{\{2\}}=\begin{pmatrix}1/2&0\\1/2&0\end{pmatrix}$, $b^{\{1\}}=b^{\{2\}}=(\tfrac12,\tfrac12)$,
explicit despite the implicit-looking coefficients because each part acts on the other
variable only, and find no odd powers of $h$ in its modified equation through $h^7$
([Ketcheson & Ranocha 2023](/sources/ketcheson-2023.md), §3.1.2, Eqs. 45–46).

## Geometric properties

A splitting of a Hamiltonian into Hamiltonian parts is a composition of symplectic maps,
hence [symplectic](/properties/symplecticity.md). By
[backward error analysis](/methods/backward-error-analysis.md) the modified vector field
of a splitting stays in the Lie algebra generated by the parts, so an order-$p$ splitting
of a Hamiltonian system on a compact set conserves a modified Hamiltonian and gives
$H(y_n)=H(y_0)+O(h^p)$ (page-local: $H$ the Hamiltonian here, not the macro step of the
multirate section below) for $nh\le e^{h_0/(2h)}$, with at most linear global-error growth
for integrable systems, whereas non-symplectic methods give energy drift $O(th^p)$ and
quadratic error growth (Blanes et al. 2024, §4.4, Eq. 4.16, as recalled from Hairer et al.
2006, Moan 2004, Calvo & Hairer 1995). Variable step sizes destroy these long-time
properties because the modified equation depends on $h$; time transformations are the
remedy (§4.4, §9.10).

## Linear stability on the harmonic oscillator

The linear stability model for splittings is not the Dahlquist equation but the
oscillator $q''=-\omega^2q$ (page-local $\omega$), split into kinetic and potential parts.
The one-step matrix $\tilde M$ has unit determinant, and the method is stable when its
half-trace $\tfrac12\operatorname{tr}\tilde M$, a polynomial in $h\omega$ called the
*stability polynomial* of the splitting, has modulus below 1; this is a different object
from the [stability function](/definitions/stability-function.md) $R(z)$ of a Runge–Kutta
method. For Störmer–Verlet the half-trace is $1-(h\omega)^2/2$ and the stability interval
is $0<h\omega<2$, i.e. $h<2/\omega_{\max}$ for a linear system. $k$ concatenated
Störmer–Verlet steps have interval $(0,2k)$, the **longest possible for any $k$-stage
splitting** (Blanes et al. 2024, §4.2, as recalled from Bou-Rabee & Sanz-Serna 2018). For
$q''=-q-\varepsilon q$ the concatenated rotation–kick Strang integrators have strictly larger
stability regions than any other $k$-stage rotation/kick splitting (§4.2, from Casas,
Sanz-Serna & Shaw 2023).

## PDE splittings as compositions of Euler steps

Blanes et al. (2024, §6.1, Eqs. 6.2–6.12) write the classical fractional-step schemes as
compositions of explicit and implicit Euler sub-steps on $f^{[1]}$, $f^{[2]}$:

| Scheme | Linear form | Order and remarks |
|---|---|---|
| Marchuk–Yanenko | $(I-hL_2)^{-1}(I-hL_1)^{-1}$ | 1; the $[0/1]$ Padé approximant inside Lie–Trotter |
| Yanenko's Crank–Nicolson | $[1/1]$ Padé inside Lie–Trotter | 1, but conjugate to a symmetric second-order composition, which explains its good behaviour |
| Peaceman–Rachford | $(I-\tfrac h2L_2)^{-1}(I+\tfrac h2L_1)(I-\tfrac h2L_1)^{-1}(I+\tfrac h2L_2)$ | 2; symmetric; the only symmetric second-order Euler composition that captures steady states exactly |
| Douglas–Rachford | splitting in an enlarged space | 1; more robust for non-smooth operators and steady states (as recalled from Glowinski et al. 2016) |

**Dimensional splitting (LOD/ADI).** For the 2D heat equation on an $N_x\times N_x$ grid
(page-local $N_x$) the semi-discrete operator splits as $L_1=I\otimes B$,
$L_2=B\otimes I$ (page-local $B$: the $N_x\times N_x$ matrix of one-dimensional second differences), and each sub-step is a
set of independent 1D problems; sources are handled by a symmetric composition with
explicit and implicit source sub-steps, which keeps second order (Blanes et al. 2024,
§6.1, Eq. 6.13). Lie–Trotter ("Godunov") and Strang splittings of convection–diffusion
and of KdV are recalled with their convergence analyses (§6.1).

**IMEX as splitting.** The one-step IMEX Euler method is the composition of an explicit
Euler step on the non-stiff part and an implicit Euler step on the stiff part, and many
second-order [IMEX schemes](/methods/imex-runge-kutta.md) have the symmetric form
(implicit half step)∘(explicit method)∘(explicit half step). A splitting variant of
IMEX Crank–Nicolson leap-frog halves the implicit work, and the IMEX trapezoidal
Runge–Kutta method is a Strang splitting of a doubled system (Blanes et al. 2024, §6.2,
Eqs. 6.14–6.21).

## Order reduction from boundary conditions

Boundary conditions hold for $f$ but not for the sub-operators. For reaction–diffusion
with Dirichlet or Neumann conditions this causes
[order reduction](/definitions/order-reduction.md), for Strang "one in the infinity norm"
(Blanes et al. 2024, §6.1, as recalled from Hansen & Ostermann 2009 and Hundsdorfer &
Verwer 2003). Remedies are boundary correction functions (Einkemmer & Ostermann) and
boundary-only corrections (Alonso-Mallo et al.). A related defect: ordinary splitting
does not reproduce the steady states of $f$ (§1.8); Peaceman–Rachford and balanced
splitting (Speth et al. 2013) do.

## Diffusion beyond second order

For parabolic $y'=(L_1+L_2)y$ with $L_1,L_2$ generating $C_0$ semigroups, an order-$p$
splitting with all $a_j,b_j\ge0$ retains order $p$ (Blanes et al. 2024, §6.4, Eq. 6.44, as
recalled from Hansen & Ostermann 2009), but real coefficients of order $p\ge3$ are never
all positive (the [negative-coefficient barrier](/results/negative-coefficient-barrier.md)),
so with real positive coefficients splitting of diffusion stops at order 2. Order is
regained with commutator flows (Kieri 2015) or with
[complex coefficients](/methods/complex-coefficient-splitting.md). Reynolds et al. likewise
describe first-order operator splitting as long used for stiff–non-stiff coupling, with
higher-order variants that "introduce complex arithmetic or backward integration"
([Reynolds et al. 2023](/sources/reynolds-2023.md), §1), as the motivation for
[IMEX additive Runge–Kutta](/methods/imex-runge-kutta.md) methods in
[ARKODE](/software/arkode.md).

## Splitting in multirate integration

Before IMEX multirate infinitesimal methods, the only multirate schemes treating the slow
scale IMEX and the fast scale "infinitesimally" (by an inner solver) were splittings
([Chinomona & Reynolds 2021](/sources/chinomona-2021.md), §1, Eqs. 1.3–1.4), for
$f=f^{\mathrm I}+f^{\mathrm E}+f^{\{\mathrm f\}}$ and macro step $H$:

- **Lie–Trotter:** explicit Euler on $f^{\mathrm E}$, implicit Euler on $f^{\mathrm I}$,
  then the fast problem $v'=f^{\{\mathrm f\}}(t,v)$ over $[t_n,t_n+H]$;
- **Strang–Marchuk:** half steps of explicit Heun on $f^{\mathrm E}$ and of the implicit
  trapezoidal rule on $f^{\mathrm I}$, a full fast solve in the middle, then the mirrored
  half steps.

On a multirate Kværnø–Prothero–Robinson problem their measured orders are 0.99 and 1.98;
on a stiff [brusselator](/benchmarks/brusselator.md) 0.91 and 1.92 (201 points), and they
are less efficient than [IMEX-MRI-GARK](/methods/imex-mri-gark.md) and implicit
MRI-GARK at every accuracy shown (Chinomona & Reynolds 2021, §5, Figs. 2–3). Roberts
et al. identify their decoupled [multirate backward Euler](/methods/multirate-gark.md),
for even ratio $m$, with subcycled Strang splitting
$(\varphi^{\{\mathrm f\}}_h)^{m/2}\circ\varphi^{\{\mathrm s\}}_H\circ(\varphi^{\{\mathrm f\}}_h)^{m/2}$
in which each flow is replaced by one backward Euler step
([Roberts et al. 2021](/sources/roberts-2021.md), §5.1).

## Splitting and asymptotic preservation

When every sub-flow is integrated exactly, a splitting can inherit the
[asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) property in time.
For the semiclassical Schrödinger equation
$i\varepsilon\partial_tu=-\tfrac{\varepsilon^2}2\partial_{xx}u+V(x)u$, the time-splitting
spectral method solves the free part exactly in Fourier space and the potential part
exactly by $u\mapsto e^{-iV(x)h/\varepsilon}u$; the only time error is the splitting error,
first order (Lie) or second order (Strang) at fixed $\varepsilon$
([Jin 2022](/sources/jin-2022.md), §3.1, Eqs. 3.2–3.3). For the wave function itself the
error bound
$G_m\frac{T}{h}\big(\tfrac{\Delta x}{\varepsilon}\big)^m+\frac{CTh}{\varepsilon}$ requires
$h=o(\varepsilon)$ and $\Delta x=o(\varepsilon)$ (Thm 3.1, as recalled from Bao, Jin &
Markowich 2002). The splitting is, however, equivalent to a splitting of the Wigner
equation whose $\varepsilon\to0$ limit at fixed $h$ is the splitting of the classical
Liouville equation, so $h=O(1)$ with $\Delta x=o(\varepsilon)$ gives correct observables
(§3.3, Eqs. 3.7–3.10; rigorous uniform estimates are recalled from Golse, Jin & Paul 2021
and Lasser & Lubich 2020). Crank–Nicolson with $h=10^{-4}$ fails to capture the weak limit
on the same problem at $\varepsilon=10^{-3}$, while Strang splitting with $h\gg\varepsilon$
captures it (Example 3.3, Fig. 3.1). The same mechanism makes the splitting of the
Schrödinger–Liouville–Ehrenfest system AP in time (§3.4, Thm 3.4); large steps do not in
general give correct observables for the nonlinear Schrödinger equation (§3.4, as
recalled from Bao, Jin & Markowich 2003). Splittings into a stiff implicit relaxation step
and an explicit transport step underlie several kinetic AP schemes (§5.4.1, §6.5; see
[micro–macro decomposition](/methods/micro-macro-decomposition.md) and
[BGK penalization](/methods/bgk-penalization.md)).

## Qualifications

- "Order" of a splitting for PDEs means consistency on a fixed spatial grid; for unbounded
  operators the formal expansions need rigorous remainder estimates (Blanes et al. 2024,
  footnote 5 and §2.4, citing Thalhammer 2008). For the pseudo-spectral Schrödinger
  equation with smooth periodic $V$, Strang has global error $\le C\,h^2\lVert u_0\rVert_{H^2}$
  in $L^2$ independently of the number of grid points (§6.3, Eqs. 6.23–6.25).
- The reduction "one order in the infinity norm" is quoted by Blanes et al. without its
  norm and regularity hypotheses; the reduction depends on the norm.
- Roberts et al. (2021, §5.1) write the multirate-backward-Euler/Strang identity with
  remainder $O(H^2)$, looser than the $O(H^3)$ local error of Strang splitting itself; the
  source does not explain it. It matches the local error of replacing each flow by one
  backward Euler step *(compiler inference, not in the sources)*.
- Reynolds et al.'s remark (higher-order splitting needs complex arithmetic or backward
  integration) omits the third route recorded by Blanes et al.: commutator (modified
  potential) flows, which give fourth order with positive coefficients (see
  [composition methods](/methods/composition-methods.md)).

# Citations

- [Blanes et al. (2024)](/sources/blanes-2024.md) — §1.1–1.9 (Lie–Trotter, Strang, conjugacy, names, history), §2.2 (general scheme), §4.2 (linear stability), §4.4 (long-time behaviour), §6.1–6.4 (PDE schemes, LOD/ADI, IMEX as splitting, boundary order reduction, parabolic problems).
- [Jin (2022)](/sources/jin-2022.md) — §3.1–3.4 (time-splitting spectral method, AP in time, Thm 3.1, Example 3.3, Thm 3.4), §5.4.1, §6.5.
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §1, Eqs. 1.3–1.4 (multirate Lie–Trotter and Strang–Marchuk), §5 (measured orders and efficiency).
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §5.1 (decoupled multirate backward Euler as subcycled Strang splitting).
- [Reynolds et al. (2023)](/sources/reynolds-2023.md) — §1 (operator splitting as precursor of IMEX methods).
- [Ketcheson & Ranocha (2023)](/sources/ketcheson-2023.md) — §3.1.2, Eqs. 45–46 (Störmer–Verlet as an additive Runge–Kutta method).
