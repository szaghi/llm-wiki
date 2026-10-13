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

**Later uses (batch 16).**

**The Lax–Friedrichs scheme as printed** ([Lax (1954)](/sources/lax-1954.md),
§1, p. 163). Lax replaces the flux derivative by a centred difference
and the time derivative by the new value minus the **average of the two
neighbours**, on a staggered lattice where each time level uses every
other point:
$$u^{n+1}_i = \tfrac12\left(u^n_{i+1} + u^n_{i-1}\right) - \frac{\Delta t}{2h}\left(f(u^n_{i+1}) - f(u^n_{i-1})\right).$$
In conservative form this is the global Lax–Friedrichs flux of the
examples above with $\alpha = h/\Delta t$ (reader's algebra; Lax does not
write a numerical flux), so the condition $\alpha \ge \max\vert f'\vert$
is the CFL condition $\max\vert f'\vert\,\Delta t/h \le 1$. Without the
average (forward time, centred space) the scheme is "unconditionally
unstable" (footnote 5). The scheme is the forward-time, centred-space
discretization of $\partial_t u + \partial_x f(u) = \mu\,\partial_{xx}u$
with $\mu = h^2/(2\Delta t)$ (p. 165). Lax names as the novelty "the use
of the conservation form … and, to a lesser extent, the particular way
of differencing" (p. 159).

**A positive-coefficient argument before Godunov** (Lax (1954), §5,
eqs. 11–13). For a scalar law, the difference of two solutions' discrete
primitives (partial sums) obeys a recursion with positive coefficients
summing to one when $\vert f'\vert\,\Delta t/h$ "should not exceed one",
hence a maximum principle in a weak (integrated) norm; with genuine
nonlinearity Lax proves $L^1$ compactness of the solution set. This
predates Godunov's (1959) monotonicity argument quoted above, but it is
stated for the primitive and the weak norm, not as monotonicity of the
scheme in $u$.

**Why the conservation form** (Lax (1954), §3, pp. 186–187). For
$\partial_t u + u^2\partial_x u = 0$ a non-conservative one-sided scheme with
step data converges to a discontinuity moving at about 0.388, against the
weak-solution speed 0.333. If a conservative scheme converges boundedly
a.e., its limit is a weak solution (pp. 163–164; a strong limit is
required). Lax conjectures, without proof, that his scheme forms
compression shocks but no rarefaction shocks (pp. 183–185).

**Upwinding and stationary shocks** ([Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md),
§2, eqs. 2.2–2.3, 2.12). Courant–Isaacson–Rees upwinding is monotone
under $\vert f'\vert\,\Delta t/h \le 1$; its modified-equation viscosity
$\tfrac12 h\vert f'\vert\left(1 - \vert f'\vert\,\Delta t/h\right)$
vanishes at zero speed, which "will allow perfectly resolved stationary
shocks but may also result in admitting entropy violating
discontinuities", the same mechanism as Harten's §5 above. In general, a
three-point conservative scheme resolves an admissible stationary shock
exactly iff its dissipation vanishes for equal-flux states joined by an
admissible jump, and it must not vanish for an inadmissible one (2.12).

**Later uses (batch 18).**

**Roe with entropy fix: an E-flux at its DG source** ([Cockburn & Shu (1989)](/sources/cockburn-1989.md),
Remark 2.4, eq. 2.28). The fluxes the RKDG framework admits are listed as
Engquist–Osher, Godunov, Lax–Friedrichs with a global $\alpha$, local
Lax–Friedrichs with $\alpha_{i+1/2}$ (the maximum of $\vert f'\vert$
between the two arguments), and Roe with entropy fix (2.28e). The last is
called "an E-flux, which is a generalization of monotone fluxes", not a
monotone flux; the examples above place it among the monotone fluxes
following Shu (1998) and Liu, Osher & Chan (1994). A qualification of
that list: Cockburn and Shu assert only the E-flux property for it, while
their framework is stated for a Lipschitz, consistent, monotone flux
(§2, eqs. 2.7–2.10). For convex $f$ they suggest
local Lax–Friedrichs or Roe with entropy fix ([RKDG](/methods/rkdg.md)).

# Citations

1. [Shu (1998)](/sources/shu-1998.md), §§2.3.1–2.3.2.
2. [Liu, Osher & Chan (1994)](/sources/liu-1994.md), §2.
3. [Harten et al. (1987)](/sources/harten-1987.md), §§4, 7.
4. [Shu & Osher (1989)](/sources/shu-1989.md), §II.
5. [Zhang & Shu (2010)](/sources/zhang-2010.md), §1, Remark 2.4.
6. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4.
7. [Godunov (1959)](/sources/godunov-1959.md), Ch. I §§1–2 (reader's translation of the Russian original).
8. [Harten (1983)](/sources/harten-1983.md), §§2, 5.
9. [Lax (1954)](/sources/lax-1954.md), §§1, 3, 5, pp. 159–165, 183–191.
10. [Harten, Lax & van Leer (1983)](/sources/harten-1983-d.md), §2, eqs. 2.2–2.3, 2.12.
11. [Cockburn & Shu (1989)](/sources/cockburn-1989.md), Remark 2.4, eq. 2.28.
