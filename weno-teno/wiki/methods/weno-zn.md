---
type: Method
title: "WENO-ZN schemes"
description: "WENO-ZN weights replace the WENO-Z global indicator by the square of the (2r−2)th undivided difference over the whole stencil, of order Δx^(4r−4), and the constant 1 by an adaptive function of the two extreme indicators; at order 2r−1 they keep the design order up to (2r−4)th-order critical points."
status: established
aliases: [WENO-ZN, WENO5-ZN, WENO7-ZN, WENO9-ZN]
tags: [weno, reconstruction, finite-difference]
timestamp: 2026-10-21T12:00:00Z
---

# WENO-ZN schemes

WENO-ZN is a modification of the [WENO-Z](/methods/weno-z.md) weights aimed at
[accuracy at critical points](/properties/critical-point-accuracy.md). The fifth-order scheme is
due to Shen, Zhang, Li & Peng (an arXiv preprint of 2020, as recalled by Li et al. 2022, §3.1); Li
et al. (2022) generalize it to every odd order $2r-1$, $r\ge3$, and work out $r=4$ and $r=5$. With
the linear weights $d_k$ and the Jiang–Shu [smoothness indicators](/definitions/smoothness-indicator.md)
$\beta_k$ of [WENO-JS](/methods/weno-js-reconstruction.md),

$$\alpha_k=d_k\Big[\Theta+\Big(\frac{\tau_{4r-4}}{\beta_k+\epsilon}\Big)^q\Big],\qquad
\tau_{4r-4}=\big[\Delta^{2r-2}f_i\big]^2,\qquad
\Theta=C_\Theta\Big(\frac{\beta_0+\beta_{r-1}-|\beta_0-\beta_{r-1}|+\epsilon}{|\beta_0-\beta_{r-1}|+\epsilon}\Big)^2,$$

(Li et al. 2022, Eqs. (27)–(29)), where $\Delta^{m}f_i$ (page-local) is the $m$th undivided
difference centred at $x_i$ over the global stencil $f_{i-r+1},\dots,f_{i+r-1}$, and $\Theta$ and
$C_\Theta$ (page-local) are the paper's adaptive function $\theta$ and constant $C$. The
normalization is that of WENO-Z.

## The two ingredients

**A global indicator of maximal order.** WENO-Z builds $\tau$ from the local $\beta_k$; WENO-ZN
uses the highest undivided difference the global stencil supports (Eqs. (30)–(32)):

$$\begin{aligned}
\tau_8&=(f_{i-2}-4f_{i-1}+6f_i-4f_{i+1}+f_{i+2})^2,\\
\tau_{12}&=(f_{i-3}-6f_{i-2}+15f_{i-1}-20f_i+15f_{i+1}-6f_{i+2}+f_{i+3})^2,\\
\tau_{16}&=(f_{i-4}-8f_{i-3}+28f_{i-2}-56f_{i-1}+70f_i-56f_{i+1}+28f_{i+2}-8f_{i+3}+f_{i+4})^2,
\end{aligned}$$

so that $\tau_{4r-4}=O(\Delta x^{4r-4})$ in smooth regions, against WENO-Z's $\tau_{2r-1}$
($\tau_7=O(\Delta x^6)$ by Li et al.'s Eq. (17)) and $O(\Delta x^{2r+2})$ for the optimal-order indicator of Fan's WENO-Z$\eta$
(§3.3). The same squared undivided difference is the quantity $d_1$ of the OWENO scheme of Baeza et
al. (Eq. (19), recalled in §2).

**An adaptive constant.** Since $\beta_0+\beta_{r-1}-|\beta_0-\beta_{r-1}|=2\min(\beta_0,\beta_{r-1})$,
$\Theta$ is large when the two extreme stencils have nearly equal indicators (smooth global stencil:
weights pulled to $d_k$) and small when one of them is crossed by a discontinuity, in which case the
relative weights are governed by $(\tau/(\beta_k+\epsilon))^q$ and the ENO behaviour of the
$\beta_k$ is recovered. $C_\Theta=10$ comes from the fifth-order paper (§3.1); Li et al. argue that
it raises the contribution of less-smooth stencils "in a reasonable region" and improves
high-frequency waves on coarse grids. On the test function of Eq. (33) (a jump at $x=0$), Fig. 1
shows $\Theta\sim10^{10}$–$10^{15}$ in smooth parts and $\tau_{12}\sim\tau_7\gg\Theta$ at the jump.

## Accuracy at critical points

Li et al. (2022, §3.3, Table 5) count, from the ratio $\tau_{4r-4}/\beta_k$ alone, the order $n$ in
$\alpha_k=d_k+O(\Delta x^n)$ at an $m$th-order critical point (where $f'=\dots=f^{(m)}=0$):
$n=q\,[(4r-4)-(2+2m)]$. For $r=3$: $n=4$ ($q=1$) or 8 ($q=2$) at the first order, 2 or 4 at the second
and 0 at the third; for $r=4$ it is positive up to the fourth order, for $r=5$ up to the sixth. Hence the
claim: the $(2r-1)$th-order WENO-ZN improves accuracy at critical points up to order $2r-4$, while
WENO-Z$\eta$ reaches only order $r-1$.

Convergence on $f(x)=x^ke^x$ at $x=0$, a $(k-1)$th-order critical point, $\Delta x$ from
$1.25\times10^{-2}$ to $1.56\times10^{-3}$ (Tables 6–8):

| scheme | critical point | observed orders |
|---|---|---|
| WENO5-ZN | 1st / 2nd / 3rd | 4.99–5.00 / 4.82–5.97 / 1.38–2.81 |
| WENO7-ZN | 2nd / 3rd / 4th | 6.99–7.00 / 6.99–7.00 / 7.43–7.91 |
| WENO9-ZN | 3rd / 4th / 5th / 6th | 8.99–9.00 / 8.99–9.00 / 9.00 / 7.04, 7.07, 9.09 |

The corresponding WENO-Z orders drop to 2.11–2.32 (WENO5-Z, second order), 3.24–3.55 (WENO7-Z,
third order) and 3.11–3.84 (WENO9-Z, fourth order). WENO5-ZN does not improve at a third-order
critical point, where it is worse than WENO5-JS (3.39–3.72).

## Other properties

- **ENO behaviour** (§3.3(2)): $S_0$ and $S_{r-1}$ cover the global stencil without overlap, so a
  discontinuity in the global stencil falls in one of them, $\Theta\ll1$, and the weights rank the
  stencils by $\beta_k$. This is a heuristic argument, not a theorem
  ([ENO property](/definitions/eno-property.md)).
- **Spectral properties**: in the approximate dispersion relation of Pirozzoli, WENO5-ZN and
  WENO7-ZN keep lower dissipation and dispersion errors than WENO-JS and WENO-Z over a large range of
  medium wavenumbers (Fig. 2; [approximate dispersion
  relation](/definitions/approximate-dispersion-relation.md)).
- **Shock-capturing tests** at seventh order (FD, global Lax–Friedrichs splitting with local
  characteristic fields, TVD-RK3, CFL 0.5): Lax ($N_x=200$), [Shu–Osher](/benchmarks/shu-osher-problem.md)
  ($N_x=200$), [interacting blast waves](/benchmarks/woodward-colella-blast-wave.md) ($N_x=400$),
  [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) ($120\times480$),
  [shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) ($200\times100$),
  [forward-facing step](/benchmarks/forward-facing-step.md) ($600\times200$) and the inviscid
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($64^3$, $128^3$): WENO7-ZN is less
  dissipative than WENO7-JS and WENO7-Z, with no reported spurious oscillations (§4.2–4.5). Ninth-order
  results are said to give "similar conclusions" but are not shown.
- **Positioning.** Li et al. exclude WENO-Z$\eta$ and the WENO-Z of Don & Borges with
  $\epsilon=\Delta x^m$ from the comparison because they "cannot keep the ENO property well"; they
  object to $\epsilon=\Delta x^m$ that $\beta_k$ and $\Delta x$ have different dimensions, so the
  solution depends on the nondimensionalization (§4.1; [scale
  invariance](/properties/scale-invariance.md)). Neither scheme is run in the paper. OWENO, which
  claims optimal order at critical points of any order, is recalled but not compared.

## Qualifications

- **The order count ignores $\Theta$.** Table 5 derives $n$ from $(\tau/\beta_k)^q$ although the
  weight is $d_k[\Theta+(\tau/\beta_k)^q]$. *(Compiler check, not in the sources.)* $\Theta$ is the
  same for every $k$, so
  $\omega_k-d_k=d_k(Z_k-\bar Z)/(\Theta+\bar Z)$ with (page-local) $Z_k=(\tau/(\beta_k+\epsilon))^q$ and
  $\bar Z=\sum_ld_lZ_l$: wherever $\Theta\gtrsim1$ the deviation is at most of the order the table
  gives, so Table 5 is a lower bound on the weight accuracy, not a prediction of the observed order.
  This reconciles the WENO9-ZN orders 7.04–9.09 at the sixth-order critical point (predicted $n=2$
  or 4) with the analysis; the paper instead asserts plain agreement with Tables 4–5.
- The values of $C_\Theta$ for $r\ge4$, and the $q$ and $\epsilon$ used in §4, are not stated; nor is
  the quantity whose error Tables 6–8 measure.
- The footnote of Table 5 says the leading constants are independent of $k$, but the $r=3$ and $r=4$
  rows print $k$-dependent constants, as Table 4 does ($C_0=C_3\ne C_1=C_2$).
- The regularization $\epsilon$ inside $\Theta$ is added to a quantity with the dimension of $\beta$,
  so the dimensional objection Li et al. raise against $\epsilon=\Delta x^m$ applies in part to
  $\Theta$ as well; the paper does not discuss it.

# Citations

- [Li et al. (2022b)](/sources/li-2022-b.md) — §2, Eqs. (12)–(23); §3, Eqs. (24)–(32), Tables 4–5, Figs. 1–2; §4, Tables 6–8, Figs. 3–11.
