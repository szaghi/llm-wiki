---
type: Definition
title: "Monotone schemes and monotone numerical fluxes"
description: "A monotone scheme is nondecreasing in each argument of its update; Harten proves monotone implies total variation nonincreasing implies monotonicity preserving, and monotone schemes are first order; high-order WENO and ENO schemes keep monotonicity only in the two-point flux that joins the reconstructed states, whose definition, examples and smoothness caveats the page collects."
status: established
aliases: [monotone scheme, monotone flux, monotone numerical flux, E-flux, monotonicity preserving scheme, Godunov's theorem]
tags: [numerical-flux, limiting, riemann-solver, finite-volume]
timestamp: 2026-10-30T08:09:00Z
---

# Monotone schemes and monotone numerical fluxes

An explicit $(2k+1)$-point scheme $u^{n+1}_i=H(u^n_{i-k},\dots,u^n_{i+k})$ for a scalar
conservation law is **monotone** if $H$ is a nondecreasing function of each of its
$2k+1$ arguments ([Harten (1983a)](/sources/harten-1983.md), §2, Eq. (2.3a); page-local
$H$). A two-point numerical flux $h(u^-,u^+)$ is **monotone** if it is nondecreasing in
its first and nonincreasing in its second argument, "$h(\uparrow,\downarrow)$", consistent,
$h(u,u)=f(u)$, and Lipschitz in both arguments ([Shu (2009a)](/sources/shu-2009.md), §3.1;
[Liu et al. (1994)](/sources/liu-1994.md), §2). The first notion classifies whole
schemes and is tied to first order; the second is the building block that every
high-order [WENO](/methods/weno-js-reconstruction.md) and
[ENO](/methods/eno-reconstruction.md) scheme of the bundle evaluates at its reconstructed
interface states.

## Monotone, TVNI, monotonicity preserving

Harten (1983a) (§2) sets three nested properties of a scalar scheme $u^{n+1}=\mathcal H(u^n)$
(page-local solution operator $\mathcal H$), modelled on the **monotonicity property** of
entropy solutions, which create no new local extrema, do not decrease local minima or
increase local maxima, and hence have nonincreasing total variation (Eq. (2.2)):

- **total variation nonincreasing (TVNI)**: $TV(\mathcal Hu)\le TV(u)$,
  $TV(u)=\sum_i\lvert u_{i+1}-u_i\rvert$ (Eq. (2.4)), the property later called
  [TVD](/definitions/total-variation-diminishing.md);
- **monotonicity preserving**: $\mathcal H$ maps monotone mesh functions to monotone ones;
- **monotone**: $H$ nondecreasing in each argument.

**Theorem 2.1** (Harten 1983a): a monotone scheme is TVNI, and a TVNI scheme is
monotonicity preserving. Part (i) uses the $\ell_1$ contraction
$\lVert\mathcal Hu-\mathcal Hw\rVert_{\ell_1}\le\lVert u-w\rVert_{\ell_1}$ of monotone schemes
(Eq. (2.6a)) with $w_i=u_{i+1}$, credited in the text to B. Keyfitz in the paper's
reference [8] (Harten, Hyman and Lax); part (ii) is by contradiction.
[Harten et al. (1987a)](/sources/harten-1987.md) (§1, Eq. (1.13)) use the same mechanism
for the exact evolution and cell averaging of their
[reconstruct–evolve–average](/methods/godunov-scheme.md) schemes: both operators are
monotone in the scalar case, so a step cannot increase the total variation of the
reconstruction.

## Monotone schemes are first order

Harten (1983a) (§2, Eq. (2.7)) recalls, citing Harten, Hyman and Lax, that a monotone
scheme approximates the viscous modified equation

$$\partial_tu+\partial_xf(u)=\Delta t\,\partial_x\big[\beta_{\mathrm H}(u)\,\partial_xu\big],\qquad
\beta_{\mathrm H}=\frac12\Big(\frac{\Delta x}{\Delta t}\Big)^2\Big[\sum_{\ell=-k}^{k}\ell^2\,\frac{\partial H}{\partial u_{i+\ell}}(u,\dots,u)-\Big(\frac{\Delta t}{\Delta x}\Big)^2f'(u)^2\Big],$$

with $\beta_{\mathrm H}\ge0$ and $\beta_{\mathrm H}\not\equiv0$ (page-local $\beta_{\mathrm H}$, not a
smoothness indicator), so it is necessarily first order. For linear schemes
$u^{n+1}_i=\sum_\ell c_\ell u^n_{i+\ell}$ the hierarchy collapses: such a scheme is
monotonicity preserving iff all $c_\ell\ge0$ (Harten, citing Godunov), so every linear
TVNI scheme is monotone and first order, while nonlinear second-order TVNI schemes are not
excluded (Eq. (2.8)). That gap is where [Harten's TVD scheme](/methods/harten-tvd-scheme.md)
lives. [Harten et al. (1987a)](/sources/harten-1987.md) (§2) take the next step: TVD
schemes are "necessarily only first-order accurate at local extrema", and a strictly
non-oscillatory scheme (no increase in the number of extrema) is limited to second order
(citing their paper II), which is why ENO replaces both by the
[ENO property](/definitions/eno-property.md).

## Monotone two-point fluxes

The founding WENO and ENO papers keep monotonicity in the flux only. The finite-volume
scheme of Liu et al. (1994) (§2, Eqs. (2.7a,b)) and Shu (2009a) (§3.1, Eq. (3.4)) is

$$\frac{d}{dt}\bar u_i=-\frac1{\Delta x}\Big[h\big(u^-_{i+1/2},u^+_{i+1/2}\big)-h\big(u^-_{i-1/2},u^+_{i-1/2}\big)\Big],$$

with $u^\pm_{i+1/2}$ the reconstructed interface values and $h$ a monotone flux. The
examples printed:

| flux | formula | source |
|---|---|---|
| Godunov | $\min_{u^-\le u\le u^+}f(u)$ if $u^-\le u^+$; $\max_{u^+\le u\le u^-}f(u)$ if $u^->u^+$ | Liu et al., Eq. (2.5); Shu, §3.1; Harten et al. (1987a), Eq. (4.6a), after Osher |
| Lax–Friedrichs | $h^{\mathrm{LF}}$ with $a=\max_u\lvert f'(u)\rvert$ | Shu, §3.1; local form with $a$ the maximum over $[\min(u^\pm),\max(u^\pm)]$ in Liu et al., Eq. (2.6b) |
| Engquist–Osher | $f(0)+\int_0^{u^-}\max(f'(v),0)\,dv+\int_0^{u^+}\min(f'(v),0)\,dv$ | Liu et al., Eq. (2.4); Shu, §3.1 |
| Roe with entropy fix | $f(u^-)$ if $f'\ge0$ on $[\min(u^\pm),\max(u^\pm)]$, $f(u^+)$ if $f'\le0$ there, local Lax–Friedrichs otherwise | Liu et al., Eq. (2.6a) |

See [Godunov scheme](/methods/godunov-scheme.md),
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) and
[Roe solver](/methods/roe-riemann-solver.md). The plain Roe flux
$\tfrac12[f(u^-)+f(u^+)-\lvert\bar a\rvert(u^+-u^-)]$, with $\bar a$ the Rankine–Hugoniot speed,
admits a stationary expansion shock, so Harten et al. (1987a) (§4, §7 A2, Eq. (7.8))
correct it with $\max(\lvert\bar a\rvert,\epsilon_{\mathrm R})$, $\epsilon_{\mathrm R}=0.1\,\Delta x/\Delta t$ in
their tests (page-local $\epsilon_{\mathrm R}$), and $\epsilon_{\mathrm R}=\Delta x/\Delta t$ gives
Lax's first-order scheme.

**Flux splitting.** Any splitting $f=f^++f^-$ with $\frac{d}{du}f^+\ge0$,
$\frac{d}{du}f^-\le0$ gives the monotone flux $h(u^-,u^+)=f^+(u^-)+f^-(u^+)$ (Shu 2009a,
§3.2, Eqs. (3.10)–(3.11)). The finite-difference WENO scheme reconstructs $f^+$ and $f^-$
separately and therefore "can only use monotone fluxes which correspond to smooth flux
splitting" (§3.2); [Jiang & Shu (1996)](/sources/jiang-1996.md) (§2, Eqs. (2.4)–(2.6))
use the global Lax–Friedrichs splitting $f^\pm=\tfrac12(f\pm au)$ and a Roe splitting with
entropy fix, and need the smoothness of the global splitting for their convergence argument,
which requires the WENO operator to be infinitely differentiable (§6, Eq. (6.1)). See
[flux vector splitting](/methods/flux-vector-splitting.md) and
[conservative finite-difference schemes](/definitions/conservative-finite-difference-scheme.md).

**E-fluxes.** [Shu & Osher (1988)](/sources/shu-1988.md) (§III, Eqs. (3.20)–(3.21)) let
"any monotone or E-flux" replace the Lax–Friedrichs building block of their
finite-difference ENO scheme through the flux increments $f_{i+1}-h_{i+1/2}$ and
$h_{i+1/2}-f_i$, and note that the accuracy needs the building block to be smooth to the
order of the scheme, while most E-fluxes (Godunov, Engquist–Osher, Roe with entropy fix)
are not smooth at sonic points.

## Qualifications

- With a high-order reconstruction the scheme as a whole is no longer monotone; the
  monotone flux supplies upwinding and, at first order, the classical convergence theory.
  Shu & Osher (1988) (§III, p. 20) use that theory as the yardstick: they call a capped
  non-conservative variant of their scheme "essentially conservative" because, as they
  state, it keeps the conclusion of the
  [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md), the entropy condition and every
  convergence property of first-order monotone schemes.
- "Monotone" in [Shu (2009a)](/sources/shu-2009.md) (§2.1, p. 86) also means a monotone
  interpolant: for a step function, the candidate and full-stencil interpolants of
  fifth-order WENO are monotone in the jump cell, so their convex combination is; that is
  a property of the reconstruction, not of the scheme in the sense above.
- Harten (1983a) prints the attribution of the $\ell_1$ contraction to "B. Keyfitz in [8]",
  while reference [8] of the report is Harten, Hyman and Lax; the page records the
  attribution as printed.

# Citations

- [Harten (1983a)](/sources/harten-1983.md) — §2 (Eqs. (2.2)–(2.8), Theorem 2.1) (NYU report DOE/ER/03077-175, March 1982).
- [Harten et al. (1987a)](/sources/harten-1987.md) — §1 (Eq. (1.13)), §2, §4 (Eqs. (4.6a), (4.21)), §7 A2 (Eq. (7.8)).
- [Shu (2009a)](/sources/shu-2009.md) — §2.1 (p. 86), §3.1 (Eq. (3.4)), §3.2 (Eqs. (3.10)–(3.11)).
- [Liu et al. (1994)](/sources/liu-1994.md) — §2 (Eqs. (2.4)–(2.7b)).
- [Jiang & Shu (1996)](/sources/jiang-1996.md) — §2 (Eqs. (2.4)–(2.6)), §6 (Eq. (6.1)) (author preprint).
- [Shu & Osher (1988)](/sources/shu-1988.md) — §III (Eqs. (3.20)–(3.21), p. 20) (ICASE Report 87-33).
