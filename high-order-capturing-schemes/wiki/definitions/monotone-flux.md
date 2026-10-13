---
type: Definition
title: "Monotone numerical flux"
description: "A two-argument interface flux that is Lipschitz, nondecreasing in its left and nonincreasing in its right argument, and consistent; the first-order building block that high-order capturing schemes evaluate on reconstructed states."
status: established
aliases: [monotone flux, E-flux building block]
tags: [numerical-flux, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Monotone numerical flux

A two-argument flux $\hat f(a, b)$ is **monotone** if it is Lipschitz in
both arguments, nondecreasing in $a$ and nonincreasing in $b$, and
consistent, $\hat f(a, a) = f(a)$ ([Shu (1998)](/sources/shu-1998.md),
§2.3.1). With piecewise constant data it gives a first-order monotone
scheme; with reconstructed interface states $u^\mp_{i+1/2}$ it is the
building block of high-order schemes.

**Examples**, from least to most dissipative
([Shu (1998)](/sources/shu-1998.md);
[Liu, Osher & Chan (1994)](/sources/liu-1994.md), eqs. 2.4–2.6):
* **Godunov**: $\min_{a\le u\le b} f(u)$ if $a \le b$,
  $\max_{b\le u\le a} f(u)$ if $a > b$ — the exact Riemann flux in the
  scalar case;
* **Engquist–Osher**: $\int_0^a \max(f'(s),0)\,ds + \int_0^b \min(f'(s),0)\,ds + f(0)$;
* **Roe with entropy fix**: $f(a)$ if $f' \ge 0$ between $a$ and $b$,
  $f(b)$ if $f' \le 0$ there, local Lax–Friedrichs otherwise;
* **local Lax–Friedrichs**:
  $\tfrac12\left[f(a) + f(b) - \alpha_{i+1/2}(b - a)\right]$ with
  $\alpha_{i+1/2}$ the maximum of $\vert f'\vert$ between $a$ and $b$; with
  a global constant $\alpha$ in place of $\alpha_{i+1/2}$, the
  Lax–Friedrichs flux.

**Order dependence.** The choice matters much at first and second order
and little at high order. Shu shows fourth-order ENO with Godunov and
with Lax–Friedrichs fluxes behaving alike on a Burgers shock, whereas
the first-order versions differ visibly, and therefore recommends the
cheap Lax–Friedrichs flux ([Shu (1998)](/sources/shu-1998.md), Fig. 2.2).
[Harten et al. (1987)](/sources/harten-1987.md) reach the same
conclusion from the structure of the scheme: for $r > 1$ the smooth
polynomial variation inside a cell exceeds the interface jumps, so the
Riemann solver acts mainly as a *pointer* to the valid side, and the
time evolution of the smooth part matters more. With a crude entropy
correction the computed shocks lag by 8, 3 and 1 cells at orders 1, 2
and 4. [Shu & Osher (1989)](/sources/shu-1989.md) find upwind building
blocks slightly sharper than Lax–Friedrichs at high order, the gap being
much smaller than at first order.

**Relation to flux splitting.** For any smooth splitting $f = f^+ + f^-$
with $df^+/du \ge 0 \ge df^-/du$, $\hat f(a,b) = f^+(a) + f^-(b)$ is
monotone; the converse fails (Godunov)
([conservative finite difference](/methods/conservative-finite-difference.md)).

**Positivity of first-order fluxes (batch 3).** Beyond monotonicity
for scalar laws, a first-order flux for Euler can keep the admissible
set: Godunov, Lax–Friedrichs (under $\nu \le 1$), Boltzmann-type, HLL,
and HLLC with Batten et al.'s wave speeds. These are the building
blocks of every high-order positivity-preserving scheme
([positivity preservation](/properties/positivity-preserving.md);
[Zhang & Shu (2010)](/sources/zhang-2010.md), §1;
[Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4). Richer Riemann
solvers used at high order are compared in
[approximate Riemann solvers](/methods/approximate-riemann-solvers.md).

**Later uses (batch 14).**

**Origin of "monotone".** [Godunov (1959)](/sources/godunov-1959.md)
(Ch. I §§1–2) asks a scheme to behave qualitatively like the exact
solution and keep monotone data monotone. For a linear two-level scheme
this holds iff all its coefficients are nonnegative; with coefficients
summing to 1 the scheme is also max-norm stable. Godunov's "monotone" is
the property later called monotonicity preserving
([Harten (1983)](/sources/harten-1983.md), §2), which for linear schemes
coincides with the monotone scheme of this page
([Godunov's order barrier](/results/godunov-order-barrier.md)).

**The Godunov flux formula.** The scalar $\min$/$\max$ form in the
examples above is not in Godunov (1959), which treats linear equations
and Lagrangian gas dynamics only; the bundle's attribution to Shu (1998)
and Liu, Osher & Chan (1994) stands as the source of that statement
([Godunov's method](/methods/godunov-method.md)).

**Monotone schemes** ([Harten (1983)](/sources/harten-1983.md), §2,
pp. 360–361). A scheme is monotone when each new value is a
nondecreasing function of every old value it depends on. Such schemes
are $l_1$-contractive and hence TVD (Theorem 2.1, citing Crandall &
Majda), and they are "necessarily first order accurate": their modified
equation carries a diffusion coefficient that is nonnegative and not
identically zero (eq. 2.7). They converge, and the limit satisfies
Oleinik's entropy condition, which identifies it uniquely (citing
Crandall & Majda and Harten, Hyman & Lax)
([TVD](/properties/total-variation-diminishing.md)).

**Upwinding without an entropy fix** (§5). The least dissipative member
of Harten's three-point TVD family, numerical viscosity
$\Theta_{i+1/2} = \vert\hat a_{i+1/2}\vert$ (Roe-type upstream
differencing), keeps a stationary discontinuity with equal fluxes on
both sides "regardless of whether or not it satisfies the entropy
condition", because its viscosity vanishes at zero Courant number.
Harten's fix replaces $\vert\hat a_{i+1/2}\vert$ near zero by a smooth
parabolic floor (parameter 0.1 on genuinely nonlinear fields, 0 on
linearly degenerate ones). He also remarks that Godunov's scheme
"actually exhibits a surprisingly poor entropy enforcement" (p. 374).
This is a different device from the "Roe with entropy fix" flux above,
which switches to local Lax–Friedrichs.

# Citations

1. [Shu (1998)](/sources/shu-1998.md), §§2.3.1–2.3.2.
2. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §2.
3. [Harten et al. (1987)](/sources/harten-1987.md), §§4, 7.
4. [Shu & Osher (1989)](/sources/shu-1989.md), §II.
5. [Zhang & Shu (2010)](/sources/zhang-2010.md), §1, Remark 2.4.
6. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4.
7. [Godunov (1959)](/sources/godunov-1959.md), Ch. I §§1–2 (reader's translation of the Russian original).
8. [Harten (1983)](/sources/harten-1983.md), §§2, 5.
