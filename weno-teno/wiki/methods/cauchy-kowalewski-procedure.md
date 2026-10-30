---
type: Method
title: "Cauchy–Kowalewski procedure"
description: "The Cauchy–Kowalewski (Lax–Wendroff) procedure expands the solution in time and replaces every time derivative by spatial derivatives through repeated use of the PDE; the page gives Harten et al.'s ENO flux built on it, its Euler form, its role in generalized Riemann problems and ADER, its cost at high order, and the case made for Runge–Kutta instead."
status: established
aliases: [Cauchy–Kovalevskaya procedure, Cauchy-Kowalewski procedure, Lax–Wendroff procedure, Lax–Wendroff-type time discretization, local space–time Taylor expansion, Cauchy–Kowalewski predictor]
tags: [finite-volume, reconstruction, numerical-flux, riemann-solver, finite-difference]
timestamp: 2026-10-30T08:40:00Z
---

# Cauchy–Kowalewski procedure

The **Cauchy–Kowalewski procedure** (spelled Cauchy–Kovalevskaya by the later sources) turns a
spatial reconstruction into a space–time one: the solution is expanded in a Taylor series in time,
and every time derivative is rewritten as a function of spatial derivatives by differentiating the
PDE $\partial_tu=-\partial_xf(u)$ repeatedly. [Shu (2009a)](/sources/shu-2009.md) (§3.1, after Eq. (3.5))
calls the same idea the **Lax–Wendroff procedure**, "which performs a Taylor expansion in time and
converts all time derivatives to spatial derivatives by repeatedly using the PDE, and finally
discretizes all the spatial derivatives to the correct order of accuracy", and offers it as the
alternative to [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) time stepping, citing ADER and
Lax–Wendroff-type finite-difference WENO schemes. The result is a one-step scheme: the fluxes are
integrated in time over $[t^n,t^{n+1}]$ by quadrature on the expansion.

## The ENO flux of Harten et al.

[Harten et al. (1987a)](/sources/harten-1987.md) (§4, Eqs. (4.11)–(4.14)) use the procedure to approximate
the "solution in the small" of their reconstruct–evolve–average schemes
([ENO reconstruction](/methods/eno-reconstruction.md), [Godunov scheme](/methods/godunov-scheme.md)).
In cell $i$ the spatial derivatives at $(x_i,t^n)$ are those of the reconstruction polynomial of
degree $r-1$, and zero from order $r$ on (Eq. (4.11a)); the mixed derivatives come from the PDE
(Eq. (4.11c)), for a scalar law

$$\partial_tu=-f'(u)\,\partial_xu,\qquad \partial_x\partial_tu=-\big[f''(u)(\partial_xu)^2+f'(u)\,\partial_x^2u\big],$$

and so on up to $\partial_t^3u$. The local expansion (page-local $\tilde u_i$, time measured from $t^n$)

$$\tilde u_i(x,t)=\sum_{l=0}^{r-1}\sum_{k=0}^{l}\frac{\partial^lu}{\partial x^k\partial t^{l-k}}(x_i,t^n)\,\frac{(x-x_i)^k}{k!}\,\frac{t^{l-k}}{(l-k)!}\qquad(4.12a)$$

satisfies $\tilde u_i=u+O(\Delta x^r)$ (Eq. (4.12c)). The numerical flux combines the expansions of the
two neighbouring cells, evaluated at the interface at the nodes $t_q$ of a time quadrature with
weights $\mathsf w^t_q$ (page-local; the source's $\beta_k\tau$, $\alpha_k$), by a two-point Riemann flux:

$$\hat f_{i+1/2}=\sum_q\mathsf w^t_q\,h\big(\tilde u_i(x_{i+1/2},t_q),\ \tilde u_{i+1}(x_{i+1/2},t_q)\big)\qquad(4.14b),$$

with the [exact Riemann flux](/methods/exact-riemann-solver.md) or the
[Roe flux](/methods/roe-riemann-solver.md) as $h$. The authors derive that this flux is $r$th order
accurate in their cell-average sense when the quadrature has order $r$ (Eqs. (4.15)–(4.16)), and that
for constant-coefficient advection it equals the exact flux of the abstract scheme, the update
reducing to the reconstruction shifted along the characteristic (Eqs. (4.17)–(4.19)); the procedure
is then equivalent to tracing the characteristic through $(x_{i+1/2},t)$.

**Euler equations.** For gas dynamics Harten et al. (§6, Eqs. (6.4)–(6.7)) apply the procedure to the
variables $(\rho,\rho v,p,v)$: the spatial derivatives of $v$ and $p$ come from $\rho v$ and
$p=(\gamma-1)(E-\tfrac12v\,\rho v)$, the time derivatives from
$\partial_t\rho+\partial_x(\rho v)=0$, $\partial_t(\rho v)+\partial_x(v\,\rho v)+\partial_xp=0$ and the pressure
equation, and a recursion (6.6a–f) reaches $\partial_t^3$ of all four variables. They print the pressure
equation as $\partial_tp+v\,\partial_xp+\gamma p\,\partial_xu=0$ with $u$ the state vector, while the recursion
(6.6a) uses $\gamma p\,\partial_xv$.

**Characteristic variant.** Their scalar characteristic-method flux (§7 C1, Eqs. (7.14)–(7.17)) solves
$\tilde u(x_0+\bar a(x_0)t,t)=\mathsf R(x_0)$ by Newton iteration, with $\mathsf R$ the reconstruction and
$\bar a$ an interpolant of the Rankine–Hugoniot speeds of its interface jumps (both page-local), and evaluates $f$ at the quadrature
nodes; the authors call it "computationally equivalent" to the Cauchy–Kowalewski flux (4.14), "slightly
more accurate", and the version "with which the development started".

**Weight of the time expansion.** In their experiments for $r>1$ the Cauchy–Kowalewski step is "in
general, more important than the Riemann solver", whose role shrinks to a pointer selecting the
valid one-sided expansion (§4, pp. 252–253; §7 A2, p. 274).

## In generalized Riemann problems and ADER

- **Toro–Titarev solver.** As recalled by [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md)
  (§2.1, Eqs. (6)–(15)), the interface state of a
  [generalized Riemann problem](/methods/generalized-riemann-problem.md) is a Taylor polynomial in time
  whose leading term solves a classical Riemann problem; the Cauchy–Kovalevskaya procedure writes
  each time derivative as a function of spatial derivatives, source terms included,
  $\partial_t^{(k)}u=\mathsf H^{(k)}(u,\partial_xu,\dots,\partial_x^{(k)}u)$ (Eq. (10); $\mathsf H^{(k)}$ page-local), and
  the spatial derivatives at the interface come from linearized derivative Riemann problems. The
  source average of [ADER finite volumes](/methods/ader-scheme.md) uses a cell-local space–time
  expansion obtained the same way (Eqs. (18)–(20)).
- **Cost at very high order.** Profiling an Euler density wave (200 cells, CFL 0.9, $t=5$, one CPU),
  Yajaman et al. find that the Cauchy–Kovalevskaya procedure takes 37 %, 59.6 %, 74.1 % and 85.2 % of
  the run time of their AENO-C scheme at orders 7, 8, 9 and 10, the reconstruction less than 7 % at
  order 10 (§8, Table 5). They attribute to it the lower efficiency of AENO-C against WENO beyond
  order 7 (§7.2, Fig. 13) and conclude that solvers avoiding the procedure, ADER-DET and ADER-TR as
  they cite them, are desirable at very high order (§8–§9;
  [AENO reconstruction](/methods/aeno-reconstruction.md),
  [density-wave advection](/benchmarks/density-wave-advection.md)).
- **One-step second order with a source.** [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) (§3.2.2,
  Eqs. (67)–(70)) evaluate the Godunov–Powell source of their MHD scheme at $t^n+\Delta t/2$ with a
  first-order Cauchy–Kowalewski predictor
  $\partial_tu=-A\,\partial_xu-A^{(2)}\partial_yu-(\nabla\cdot B)\,S_{\mathrm P}(u)$, $S_{\mathrm P}$ the Powell vector
  (page-local), and their HLL-GRP flux uses $\partial_t\tilde u=-A\,\partial_xu$ in the region of the fan
  (Eqs. (65)–(66); [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- **Characteristic time derivatives.** [Van Leer (1979)](/sources/vanleer-1979.md) (§2.3, Eqs. (64)–(66))
  obtains the first time derivatives of the resolved interface state from the characteristic
  equations on both sides of the contact, not by differentiating the conservation laws, and advances
  the interface values half a step with them ([MUSCL](/methods/muscl-hancock.md)).

## The case for Runge–Kutta instead

[Shu & Osher (1988)](/sources/shu-1988.md) (§I(1), pp. 4–5) replace the Lax–Wendroff-type time
discretization of the ENO schemes by method-of-lines Runge–Kutta steppers, stating that the former is
complicated to program in several space dimensions and with forcing terms, that TVD or TVB is hard to
prove for it, and that only second-order-in-time TVD or TVB schemes of this type exist. Harten et al.
(1987a, §7 C2), citing the Runge–Kutta experiments of their ref. [2], already called the semi-discrete
form easier to program but less efficient and more storage-demanding than the fully discrete one,
with no spurious oscillations for CFL $\le0.5$ and oscillations beyond. Strang-type dimensional
splitting, they add, is only second order in time and "therefore unsuitable" for their higher-order
schemes in two dimensions (§7 C4).

## Qualifications

- The order statements of Harten et al. are formal truncation-error derivations; they state that the
  accumulation of error is not analysed rigorously.
- The cost shares of Yajaman et al. are for one problem, one code and one machine (hardware not
  named), and include the GRP linear solves together with the expansion.
- Shu (2009a) only names the Lax–Wendroff procedure and cites its uses; it prints no scheme of this
  type.

# Citations

- [Harten et al. (1987a)](/sources/harten-1987.md) — §4 (Eqs. (4.11)–(4.19), pp. 252–253), §6 (Eqs. (6.4)–(6.7)), §7 A2 (p. 274), §7 C1 (Eqs. (7.14)–(7.17)), §7 C2, §7 C4.
- [Shu (2009a)](/sources/shu-2009.md) — §3.1, after Eq. (3.5).
- [Shu & Osher (1988)](/sources/shu-1988.md) — §I(1), pp. 4–5 (ICASE Report 87-33).
- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §2.1 (Eqs. (6)–(20)), §7.2 (Fig. 13), §8 (Table 5), §9.
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §3.2.1–§3.2.2, Eqs. (65)–(70).
- [Van Leer (1979)](/sources/vanleer-1979.md) — §2.3, Eqs. (64)–(66).
