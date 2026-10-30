---
type: Method
title: "Godunov scheme"
description: "Godunov's first-order scheme replaces the data by cell averages, solves the Riemann problem at every interface exactly for one step and averages back; the page gives the reconstruct–evolve–average form, the scalar Godunov flux, its Roe replacement, van Leer's Lagrangean reading, and the evidence that second-order extensions beat it."
status: established
aliases: [Godunov's method, Godunov's scheme, Godunov flux, first-order Godunov scheme, Godunov-type scheme, reconstruct–evolve–average]
tags: [finite-volume, riemann-solver, numerical-flux, reconstruction]
timestamp: 2026-10-30T08:44:00Z
---

# Godunov scheme

**Godunov's scheme** is the first-order finite-volume scheme in which the data of each
step are the cell averages $\bar u_i$, taken as constant in each cell $I_i$; the
Riemann problem at every interface is solved exactly over one step, and the result is
averaged back onto the cells. Written in flux form,

$$\bar u^{n+1}_i=\bar u^n_i-\frac{\Delta t}{\Delta x}\Big(h^{\mathrm G}(\bar u^n_i,\bar u^n_{i+1})-h^{\mathrm G}(\bar u^n_{i-1},\bar u^n_i)\Big),$$

with the **Godunov flux** $h^{\mathrm G}(u^-,u^+)=f\big(u^{\mathrm{RP}}(0;u^-,u^+)\big)$, the
physical flux of the self-similar Riemann solution $u^{\mathrm{RP}}(x/t;u^-,u^+)$ at $x/t=0$
(page-local symbols; [Harten et al. (1987a)](/sources/harten-1987.md), §4, Eqs. (4.4)–(4.5)).
The founding sources of the bundle treat it as the base of every higher-order
Godunov-type scheme: [MUSCL](/methods/muscl-hancock.md) replaces the constants by
linear functions ([van Leer (1979)](/sources/vanleer-1979.md)), and
[ENO reconstruction](/methods/eno-reconstruction.md) by polynomials of degree $r-1$
(Harten et al. 1987a).

## Reconstruct, evolve, average

Harten et al. (1987a) (§1, Eqs. (1.10)–(1.14)) write every scheme of their hierarchy as
the composition of three operators: a reconstruction $\mathsf R(\cdot;\bar u)$ of a
function from cell averages, the exact solution operator $\mathsf S(\Delta t)$ of the
conservation law over one step, and the cell-averaging operator $\mathsf A_{\Delta x}$
(page-local names for the source's $R$, $E$, $A_h$):

$$\bar u^{n+1}=\mathsf A_{\Delta x}\,\mathsf S(\Delta t)\,\mathsf R(\cdot;\bar u^n).$$

With piecewise-constant $\mathsf R$ this "is exactly Godunov's scheme" (Eq. (1.11)); with
piecewise-linear $\mathsf R=\bar u_i+s_i(x-x_i)$, $s_i=\partial_xu(x_i)+O(\Delta x)$, it is
the second-order extension of van Leer and others (Eq. (1.12)). The flux form follows
from integrating the exact evolution over $I_i\times[t^n,t^{n+1}]$, with the
time-averaged interface flux as numerical flux (Eqs. (1.5)–(1.6)). In the scalar case $\mathsf S$ and
$\mathsf A_{\Delta x}$ do not increase the total variation, so
$TV(\bar u^{n+1})\le TV(\mathsf R(\cdot;\bar u^n))$ (Eq. (1.20)), and Godunov's scheme,
whose reconstruction satisfies $TV(\mathsf R(\cdot;\bar u))\le TV(\bar u)$, is
[total variation diminishing](/definitions/total-variation-diminishing.md) (Eqs.
(1.21a,b)).

## The scalar Godunov flux

For a scalar law, Harten et al. (1987a) (§4, Eq. (4.6a), after Osher) evaluate the
Godunov flux without constructing the Riemann fan:

$$h^{\mathrm G}(u^-,u^+)=\begin{cases}\min_{u^-\le u\le u^+}f(u),&u^-\le u^+,\\
\max_{u^+\le u\le u^-}f(u),&u^->u^+,\end{cases}$$

and write the convex case with the sonic point (Eq. (4.6b)).
[Liu et al. (1994)](/sources/liu-1994.md) (§2, Eq. (2.5)) and
[Shu (2009a)](/sources/shu-2009.md) (§3.1) print the same formula as one of their
[monotone fluxes](/definitions/monotone-scheme.md). For systems the exact flux needs an
iterative Riemann solver; Harten et al. (1987a) cite iterative algorithms for the Euler
equations (§6) and replace it by the
[Roe flux](/methods/roe-riemann-solver.md),

$$h^{\mathrm{Roe}}(u^-,u^+)=\tfrac12\big[f(u^-)+f(u^+)-\lvert\bar a(u^-,u^+)\rvert(u^+-u^-)\big],\qquad
\bar a(u^-,u^+)=\frac{f(u^+)-f(u^-)}{u^+-u^-},$$

which equals $f(u^-)$ when $\bar a>0$ and $f(u^+)$ otherwise (scalar form, Eq. (4.21);
page-local $\bar a$ the Rankine–Hugoniot speed). It admits a stationary expansion shock
where $\bar a=0$ and "should not be used" at a sonic rarefaction without an entropy
correction (§4, §7 A2). [Harten (1983a)](/sources/harten-1983.md) (§8, Eq. (8.5)) calls the
first-order scheme with this flux the "first order accurate Godunov-type scheme of Roe".

**The Riemann solver as a pointer.** In a higher-order scheme the role of the Riemann
solver shrinks: in Harten et al.'s ENO schemes it only selects which of the two one-sided
Taylor expansions is valid at the interface, so the Roe flux can replace the exact one
without loss of order (§4, pp. 252–253), and "the importance of the Riemann solver
decreases with increasing order" (§7 A2, p. 274; argued from their figures).

## Upwind differencing and the first-order barrier

For a three-point scheme written with Harten's numerical-viscosity function $\mathfrak Q$ (page-local, the source's $Q$) of the
local Courant number (see [Harten's TVD scheme](/methods/harten-tvd-scheme.md)), the
choice $\mathfrak Q(\nu)=\lvert\nu\rvert$ gives the update

$$u^{n+1}_i=u^n_i-\min(\nu_{i+1/2},0)\,(u^n_{i+1}-u^n_i)-\max(\nu_{i-1/2},0)\,(u^n_i-u^n_{i-1}),$$

with $\nu_{i+1/2}=\frac{\Delta t}{\Delta x}\bar a(u_i,u_{i+1})$ the signed local Courant number
(page-local); Harten (1983a) (§5, Eq. (5.1), Lemma 5.1) calls it a generalization of the
upstream differencing of Courant, Isaacson and Rees, the least dissipative
total-variation-nonincreasing scheme of three-point form, with the monotonicity property
under $\frac{\Delta t}{\Delta x}\max\lvert f'(u)\rvert\le1$. Van Leer (1979) (App. B, p. 134)
states, citing the fourth paper of the series, that Godunov's scheme "boils down to" the
Courant–Isaacson–Rees scheme for the Riemann invariants, as the scheme with averaged slopes
boils down to Fromm's second-order scheme.

Godunov's scheme is first order. Harten (1983a) (§2, Eq. (2.8)) relays, citing Godunov,
that a linear scheme is monotonicity preserving only if all its coefficients are
nonnegative, so a linear scheme that keeps monotone data monotone is first order; the
higher-order schemes of the founding sources are therefore nonlinear
([monotone schemes](/definitions/monotone-scheme.md)).

## Godunov's Lagrangean scheme as van Leer's starting point

[Van Leer (1979)](/sources/vanleer-1979.md) builds MUSCL as a "second-order sequel" to
Godunov's first-order **Lagrangean** scheme for ideal compressible flow, written in the
mass coordinate (Abstract, §1, §2):

- Godunov's scheme represents specific volume, velocity and total energy as uniform in
  each slab; with linear distributions instead, and all slopes set to zero, van Leer's
  scheme reduces to Godunov's, which "accounts for the first-order accuracy of Godunov's
  scheme" (§2.2, p. 107; §3.3, p. 118);
- in smooth flow on a uniform grid the interface jumps of Godunov's scheme are
  $O(\Delta\zeta)$, those of the linear distributions $O(\Delta\zeta^2)$, so in the second-order
  scheme the acoustic estimate of the resolved pressure suffices in the smooth part of the
  flow (§2.3, p. 110; $\Delta\zeta$ the mass-coordinate cell size, page-local);
- the resolved pressure $p^*$ comes from exact wave relations solved iteratively ([exact Riemann solver](/methods/exact-riemann-solver.md)); Godunov's
  chord iteration gains a factor of the order of the interface jump per cycle, the tangent
  iteration suggested by P. J. Bedijn its square (§2.3, App. A, Eqs. (A1)–(A3)), with a
  pressure floor for cavitation;
- Godunov's Euler version integrates the Euler equations directly in one step; van Leer's
  method uses a Lagrangean step plus a separate remap
  ([conservative remapping](/methods/conservative-remapping.md); §3.2, §5).

## Evidence

- **Mach 3 step, Godunov against MUSCL.** Van Leer (1979) (§4, Figs. 8 and 11; runs by
  P. R. Woodward) realize Godunov's method in the MUSCL code by zeroing all slopes. On the
  [forward-facing step](/benchmarks/forward-facing-step.md) Godunov's method on an
  $80\times30$ grid ($H/\Delta y=30$, $H$ the tunnel entrance height) is "mimicked" by MUSCL
  on $30\times10$; Godunov's method "even when programmed efficiently, will not run more
  than twice as fast as MUSCL", which the author calls "a dramatic increase in efficiency"
  and, in §1, "at least an order of magnitude" in 2D. The comparison is visual, on pressure
  contours; no error norm is printed.
- **Shock tube, first order against second order.** On Harten (1983a)'s first Riemann
  problem (140 cells, 100 steps, CFL 0.95) the first-order Roe scheme smears shock and
  contact, while the second-order total-variation-nonincreasing ULT1 scheme captures them
  sharply without the oscillations of Lax–Wendroff (§8 I, Figs. 2a–c;
  [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)).
- **Expansion shocks.** On the Mach 3 step Harten (1983a) (§8 III) reports that ULT1, whose
  viscosity vanishes at zero Courant number, shows part of the sonic line at the corner
  turning into an expansion shock, as do the Godunov results of Woodward and Colella that
  the paper cites.
- **First-order ENO.** Harten et al. (1987a) run their ENO hierarchy from $r=1$, the
  Godunov-type member: on smooth periodic Burgers data its $L_1$ rate is 0.99 at
  $J=64\to128$ (Tables IA–IB), and with the crude entropy correction of the Roe flux its
  shock on a nonconvex Riemann problem lags the correct one by 8 cells, against 3 and 1
  for $r=2$ and $r=4$ (§7 A2, Figs. 6, 8;
  [nonconvex scalar Riemann problems](/benchmarks/nonconvex-scalar-riemann-problem.md)).

## Qualifications

- Van Leer's efficiency factor rests on comparing contour plots at matched appearance,
  with timings on one machine (IBM 370/158); it is not a measured error at equal cost.
- Harten et al.'s statement on the declining role of the Riemann solver is an argument
  from figures, not a theorem; the paper itself uses the Roe flux without entropy
  correction in all Euler runs (§7 B).
- "Godunov-type scheme" is used in the sources for any flux-form scheme built on
  (approximate) Riemann solutions; Harten (1983a) applies it to Roe's first-order scheme,
  Harten et al. (1987a) to their whole hierarchy.

# Citations

- [Harten et al. (1987a)](/sources/harten-1987.md) — §1 (Eqs. (1.5)–(1.14), (1.20)–(1.21)), §4 (Eqs. (4.4)–(4.6), (4.21), pp. 252–253), §6, §7 A1–A2 (Tables IA–IB, Figs. 6, 8), §7 B.
- [Van Leer (1979)](/sources/vanleer-1979.md) — Abstract, §1, §2.2–2.3, §3.2–3.3, §4 (Figs. 8, 11), §5, App. A (Eqs. (A1)–(A3)), App. B.
- [Harten (1983a)](/sources/harten-1983.md) — §2 (Eq. (2.8)), §5 (Eq. (5.1), Lemma 5.1), §8 (Eq. (8.5), Figs. 2a–c, §8 III) (NYU report DOE/ER/03077-175, 1982).
- [Liu et al. (1994)](/sources/liu-1994.md) — §2, Eq. (2.5): scalar Godunov flux.
- [Shu (2009a)](/sources/shu-2009.md) — §3.1: scalar Godunov flux among monotone fluxes.
