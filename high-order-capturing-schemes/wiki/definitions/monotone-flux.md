---
type: Definition
title: "Monotone numerical flux"
description: "A two-argument interface flux that is Lipschitz, nondecreasing in its left and nonincreasing in its right argument, and consistent; the first-order building block that high-order capturing schemes evaluate on reconstructed states."
status: established
aliases: [monotone flux, E-flux building block]
tags: [numerical-flux, riemann-solver, definition]
timestamp: 2026-10-08T00:00:00Z
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
  $\tfrac12\left[f(a) + f(b) - \beta(b - a)\right]$ with $\beta$ the
  maximum of $\vert f'\vert$ between $a$ and $b$; with a global constant
  $\alpha$ in place of $\beta$, the Lax–Friedrichs flux.

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

# Citations

1. [Shu (1998)](/sources/shu-1998.md), §§2.3.1–2.3.2.
2. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §2.
3. [Harten et al. (1987)](/sources/harten-1987.md), §§4, 7.
4. [Shu & Osher (1989)](/sources/shu-1989.md), §II.
5. [Zhang & Shu (2010)](/sources/zhang-2010.md), §1, Remark 2.4.
6. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4.
