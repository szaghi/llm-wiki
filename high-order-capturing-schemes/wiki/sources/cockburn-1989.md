---
type: Source
title: "Cockburn & Shu (1989) — TVB Runge-Kutta Local Projection Discontinuous Galerkin Finite Element Method for Conservation Laws II: General Framework"
description: "Part II of the RKDG series: the 1D scalar framework for any degree K (moments, monotone flux, MUSCL-type mean equation), the local projection limiter on the two face deviations with Shu's TVB correction and a rule for M, rebuilding of the higher moments, TVD Runge–Kutta time stepping, proofs of TVDM/TVBM, TVB and subsequence convergence, entropy variants, linear stability for K = 1, 2, inflow/outflow boundaries, and third-order Burgers and nonconvex tests."
resource: "doi:10.1090/S0025-5718-1989-0983311-4"
source_kind: paper
authors: [Cockburn B., Shu C.-W.]
year: 1989
venue: "Math. Comp. 52:411–435"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1989-MathComp-Cockburn-101090S0025-5718-1989-0983311-4.pdf"
tags: [dg, rkdg, limiter, tvb, convergence, boundary-treatment]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Part II of the RKDG series sets out the general framework of the explicit
discontinuous Galerkin method for the 1D scalar conservation law, for any
polynomial degree $K$; systems and multi-D are deferred. The solution is a
polynomial of degree $K$ in each cell, discontinuous at interfaces, tested
against the same space; the undefined interface flux is replaced by a
[monotone flux](/definitions/monotone-flux.md) (eqs. 2.2–2.10). Stability
comes from a **local projection limiter** that modifies only the two
deviations of the interface values from the cell mean, by a minmod against
the neighbouring mean differences (eqs. 2.21–2.23); Shu's TVB correction
(eq. 2.24) leaves it inactive below a threshold $Mh^2$, and Lemma 2.2 fixes
$M$ from a bound on $\vert\partial_{xx}u\vert$ (eq. 2.25). Time stepping is
the Shu–Osher TVD Runge–Kutta method (eqs. 2.32–2.34). The paper proves
TVDM/TVBM of the means, TVB of the whole solution, convergence of a
subsequence, entropy-convergent variants, and linear stability under
$\nu \le 1/(2K+1)$ for $K = 1, 2$, and gives inflow/outflow boundary
treatments with TVBM (§3). Third-order runs ($K = 2$, RK3) on Burgers'
equation and on two nonconvex fluxes close the paper (§4). Merged into
[RKDG](/methods/rkdg.md).

# Key claims

1. **Space and degrees of freedom** (§2, eqs. 2.2–2.6). The space is
   piecewise $P^K$ with jumps at interfaces, not a subspace of $H^1$, so
   the semidiscrete scheme is explicit, unlike streamline diffusion. The
   basis is the unscaled Legendre basis $1$, $x - x_i$,
   $(x - x_i)^2 - h_i^2/12$, …, i.e. $h_i^l P_l(\zeta)$; the moments are
   normalized so that the zeroth is $\bar u_i$.
2. **Weak form and flux** (eqs. 2.7–2.10). After integration by parts the
   interface value of $f$ is undefined: "It is this freedom which gives us
   a chance to adopt the successful finite difference nonoscillatory
   methodology" (p. 415). It is replaced by $\hat f(u^-_{i+1/2}, u^+_{i+1/2})$,
   Lipschitz, consistent and monotone. The mean equation is
   $\frac{d}{dt}\bar u_i = -\frac1h(\hat f_{i+1/2} - \hat f_{i-1/2})$
   (2.10a); the higher moments add a volume integral of $f(\mathcal P_i)$
   (2.10b,c).
3. **The mean equation is MUSCL-type** (eqs. 2.11–2.14). With the face
   deviations $u^-_{i+1/2} - \bar u_i$ and $\bar u_i - u^+_{i-1/2}$, the
   mean update is a scheme that "resembles a MUSCL type finite difference
   scheme considered by Osher" (2.14).
4. **Lemma 2.1 (TVDM)** (eqs. 2.16–2.20). If the ratios of the
   differences of the face deviations to $\Delta^1\bar u_i$ lie in
   $[-\theta, 1]$ (here $\theta \ge 0$ is the lemma's own parameter, not the
   registry's limiter $\theta$), the semidiscrete mean scheme is TVD, and
   its forward-Euler version is TVD when $\Delta t/h$ times the sum of the
   Lipschitz constants of $\hat f$ in its two arguments is at most
   $1/(1+\theta)$ (2.17). Proof by Harten's incremental form, after
   Osher. TVDM means total variation diminishing in the means.
5. **Local projection limiter** (eqs. 2.21–2.23), for $\theta = 1$:
   $u^-_{i+1/2} - \bar u_i \leftarrow \operatorname{minmod}(u^-_{i+1/2} - \bar u_i,\ \Delta^1\bar u_i,\ \Delta^1\bar u_{i-1})$,
   and likewise $\bar u_i - u^+_{i-1/2}$; the interface values are rebuilt
   from the limited deviations. In smooth monotone regions the deviations
   are about half the mean differences, so the limiter is inactive away
   from critical points; at critical points the accuracy degenerates to
   first order "like in any other TVD scheme" (p. 418).
6. **TVB correction** (eq. 2.24), "the idea of Shu": $\operatorname{minmod}$
   is replaced by $\operatorname{minmod}_M$ with threshold $Mh^2$.
7. **Lemma 2.2: the choice of $M$** (eq. 2.25, read from the page image).
   With $M = \tfrac23\max\vert\partial_{xx}u\vert$ (2.25a), or a cell
   value (2.25b) that "is very small except near critical points", the
   limiter does not affect the accuracy wherever $u \in C^2$ with that
   bound on $\vert\partial_{xx}u\vert$. "In practice, we should choose" the
   bound as the maximum of $\vert\partial_{xx}u\vert$ of the initial data
   over a neighbourhood of its smooth critical points (p. 418).
8. **Lemma 2.3 (TVBM).** Lemma 2.1 holds with $\operatorname{minmod}_M$
   and TVD replaced by TVB (proof referred to Shu).
9. **Higher moments after limiting** (eqs. 2.26–2.27). For $K = 1, 2$ the
   two limited deviations determine the new moments: for $K = 2$,
   $\hat u^{(1)}_i$ is their sum and $\hat u^{(2)}_i$ three times their
   difference (compiler's conversion of eqs. 2.5–2.6b, 2.26b to the
   registry's Legendre moments). For $K \ge 3$ the recipe is not unique;
   one keeps the moments of degree $\ge 3$ unless $\hat u^{(1)}_i$ or
   $\hat u^{(2)}_i$ changed, in which case they are set to zero and those
   two are rebuilt as for $K = 2$. A bound on every moment by the smaller mean
   difference plus $O(h^2)$ (2.27) carries TVBM of the means to the whole
   solution.
10. **Fluxes** (Remark 2.4, eq. 2.28). Engquist–Osher, Godunov,
    Lax–Friedrichs with a global $\alpha$, local Lax–Friedrichs with
    $\alpha_{i+1/2}$, and Roe with entropy fix (2.28e), which is "an
    E-flux, which is a generalization of monotone fluxes". For convex $f$
    they suggest local Lax–Friedrichs or Roe with entropy fix.
11. **Quadrature** (Remark 2.6). The volume integral must be approximated
    with error $O(h^{2K+2})$ for every moment: Simpson suffices for
    $K = 1$, three-point Gauss is needed for $K = 2$; Gauss–Lobatto is
    preferred because the interface fluxes can be reused.
12. **Entropy** (Lemmas 2.8–2.9, eqs. 2.29–2.30). An extra minmod argument
    of size $Ch^\alpha$ (constants "must be tuned for each individual
    problem", p. 421) makes the scheme converge to the entropy solution;
    for convex $f$ Osher's condition (2.30) gives one entropy inequality but
    affects smooth-region accuracy. Neither is used in practice; they
    "always observed convergence to the correct entropy solution" (p. 421).
13. **Time discretization** (eqs. 2.31–2.34). Shu–Osher TVD Runge–Kutta,
    TVD/TVB under $\Delta t \le \Delta t_{\mathrm{FE}}\min a_{ik}/\vert b_{ik}\vert$
    (2.33). RK2: $a_{10} = b_{10} = 1$, $a_{20} = a_{21} = b_{21} = \tfrac12$,
    $b_{20} = 0$, stage times $0, 1$. RK3: $a_{10} = b_{10} = 1$,
    $a_{20} = \tfrac34$, $a_{21} = b_{21} = \tfrac14$, $b_{20} = 0$,
    $a_{30} = \tfrac13$, $a_{32} = b_{32} = \tfrac23$, $b_{30} = a_{31} = b_{31} = 0$,
    stage times $0, 1, \tfrac12$; both with CFL coefficient 1 (2.34).
    "For $r \le 4$, (2.32) can be made $r$th-order accurate" ($r$ the
    number of stages).
14. **Linear stability** (Lemma 2.10, eq. 2.35). The unlimited scheme is
    linearly stable under $\nu \le 1/(2K+1)$ for $K = 1, 2$; the $K = 1$
    proof is referred to earlier papers (part I among them), the $K = 2$ proof "is more
    technical, and is thus omitted", and "We do not know whether (2.35) is
    the correct CFL condition for linear stability when $k \ge 3$." The
    condition is stated as sufficient; no sharpness claim. The
    forward-Euler version is linearly unstable at any fixed CFL number.
15. **Proposition 2.11.** (i) Linear stability under (2.35), $K = 1, 2$;
    (ii) with the minmod limiter: order $K + 1$ except near critical
    points, TVDM and TVB under (2.17) with $\theta = 1$, a convergent
    subsequence; (iii) with $\operatorname{minmod}_M$ and (2.25): uniformly
    of order $K + 1$ where $u \in C^2$ with the bound, TVBM and TVB, a
    convergent subsequence; (iv) with (2.30): convergence to the entropy
    solution for convex $f$; (v) with (2.29) as well: all entropy
    conditions. Order is "in the sense of local truncation error".
    "In practice, we suggest using the schemes in (iii)."
16. **Boundaries** (§3, eqs. 3.1–3.8, Prop. 3.1). Outflow: the boundary
    interface value is taken from inside and the deviations are limited
    against $\Delta^1\bar u_0$ only. Inflow: $u^-_{-1/2} = g(t)$ and the
    deviation is limited also against $2(\bar u_0 - g(t))$, the factor 2
    "chosen for accuracy considerations". TVBM and TVB under (2.17) with
    $\theta = 1$ (outflow) or $2$ (inflow); the boundary data add at most
    their own variation plus $O(h)$ to the TV (3.7). The compact, moment-based
    stencil makes the boundary treatment simpler than wide-stencil FD TVB.
17. **Position in the series** (§§1, 5). Higher order "by more moments in a
    cell rather than using neighboring cells"; Chavent–Salzano explicit DG
    is linearly unstable at fixed CFL; the Chavent–Cockburn $P^0P^1$ scheme
    is first order in time; part I is second order with TVD RK2, linearly
    stable for CFL $\le \tfrac13$, TVBM.

# Tests

All in §4: $K = 2$ with RK3 (2.34b), limiter (2.21)–(2.24) with the cell
value (2.25b), no entropy-enforcing limiter, Roe flux with entropy fix.
**Not printed:** the CFL number, the bound on $\vert\partial_{xx}u\vert$
(hence $M$), the quadrature. Figures plot one point per cell.

1. **Burgers, periodic** (Example 1, eq. 4.1).
   $u_0 = \tfrac14 + \tfrac12\sin\pi x$; figures on $[-1, 1]$ (period 2
   implied; the domain is not stated in the text); smooth until
   $t = 2/\pi$, with a sonic point. Table 1 ($t = 0.3$; $h = 1/10, 1/20, 1/40$):
   $L^1$ errors 7.10, 0.94, 0.12 ($\times10^{-5}$), orders 2.92, 2.97;
   $L^\infty$ 4.80, 0.66, 0.09 ($\times10^{-5}$), orders 2.86, 2.87.
   Table 2 ($h = 1/40$, points at least 0.1 from the shock): $L^\infty$
   $0.13\times10^{-4}$ ($t = 2/\pi$), $0.61\times10^{-6}$ ($t = 1.1$);
   $L^1$ $0.11\times10^{-5}$, $0.14\times10^{-6}$. Claim: uniformly high
   order in smooth regions "including at critical and sonic points"; sharp
   shocks without oscillation (Figs. 1–4)
   ([Burgers shock formation](/benchmarks/burgers-shock-formation.md)).
2. **Burgers, inflow/outflow** (Example 2, eqs. 4.2–4.3). Same data on
   $-1 < x < 1$, inflow data from the exact periodic solution. Table 3
   ($t = 0.3$): $L^1$ 6.82, 0.92, 0.12 ($\times10^{-5}$), orders 2.90,
   2.94; $L^\infty$ 3.82, 0.56, 0.09, orders 2.77, 2.78. Table 4
   ($h = 1/40$, band 0.1): $L^\infty$ $0.15\times10^{-4}$, $0.65\times10^{-6}$;
   $L^1$ $0.11\times10^{-5}$, $0.13\times10^{-6}$. A shifted variant
   ($\sin\pi(x + 0.2)$, inflow from the exact solution at $-0.8$) sends a
   shock out through the inflow boundary before $t = 1.1$; stable
   (Figs. 7–8).
3. **Nonconvex fluxes** (Example 3). $f(u) = \tfrac14(u^2 - 1)(u^2 - 4)$
   (eq. 4.4) with Riemann data $2 \mid -2$ at $t = 1$ and $-3 \mid 3$ at
   $t = 0.04$; Buckley–Leverett $f(u) = 4u^2/(4u^2 + (1-u)^2)$ (eq. 4.5),
   $u = 1$ on $[-\tfrac12, 0]$, 0 elsewhere, $t = 0.4$; $h = 1/20$, $1/40$.
   "In all cases, we see convergence with good resolution to the entropy
   solutions." Graphical only.

# Notation map

| Cockburn & Shu (1989) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$, $I_j$ | $i$, $I_i$ | |
| $\Delta x_j$; $h = \sup_j\Delta x_j$ | $h_i$; $h$ | the paper's $h$ is the largest spacing |
| $k$, $P^k(I_j)$, $V_h^k$ | $K$, $P^K$ | |
| $v_l^{(j)}$ | $h_i^l P_l(\zeta)$ | checked for $l \le 2$ |
| $u_j^{(l)}$ (eq. 2.5) | $\hat u^{(l)}_i$ up to scaling: $\hat u^{(1)}_i = 12u^{(1)}_j$, $\hat u^{(2)}_i = 180u^{(2)}_j$; $u^{(0)}_j = \bar u_i$ | compiler's conversion |
| $u^h$ | $\mathcal P_i$ | |
| $h(\cdot,\cdot)$, $h_{j+1/2}$ | $\hat f(a, b)$, $\hat f_{i+1/2}$ | **collision**: the paper's $h$ is also the spacing |
| $h_1$, $-h_2$ | words (Lipschitz constants of $\hat f$) | |
| $\tilde u_j$, $\tilde{\tilde u}_j$ | $u^-_{i+1/2} - \bar u_i$, $\bar u_i - u^+_{i-1/2}$ | |
| $\Delta_+$, $\Delta_-$ | $\Delta^1 w_i$, $\Delta^1 w_{i-1}$ | |
| $m$, $\tilde m$, $M$ | $\operatorname{minmod}$, $\operatorname{minmod}_M$, $M$ | |
| $M_2$ | words (bound on $\vert\partial_{xx}u\vert$) | not registered |
| $\theta$ (Lemma 2.1) | words | **collision**: limiter $\theta$ |
| $\lambda = \Delta t/h$ | $\Delta t/h$; $\nu$ with $\max\vert f'\vert$ | **collision**: eigenvalues $\lambda^{(p)}$ |
| $\alpha$ (2.28c); $\beta$ (2.28d) | $\alpha$; $\alpha_{i+1/2}$ | **collision**: $\beta$ with $\beta_k$ |
| $C$, $\alpha$ in $Ch^\alpha$ (2.29) | words | **collision**: $\alpha$ |
| $V(u) = u^2/2$ | $U(u)$ | |
| $L_h(u^h, t)$; $\tilde L_h$ | $\mathcal L(t, u)$; $\tilde{\mathcal L}$ | |
| $r$ (stages) | $s$ | **collision**: $r$ |
| $\alpha_{il}$, $\beta_{il}$, $d_l$ | $a_{ik}$, $b_{ik}$, $\mathsf c_i$ | |
| $\lambda_0$ | $\Delta t_{\mathrm{FE}}/h$ | |
| $g(t)$ | $g(t)$ | |
| $TV$ | $TV$ | |

# Pages created or updated

* Updated [Runge–Kutta discontinuous Galerkin method (RKDG)](/methods/rkdg.md) (batch-18 block: the 1D framework, the limiter on the face deviations, Lemma 2.2, rebuilding the moments, Lemma 2.10 and Prop. 2.11, boundaries, the third-order Burgers tables).
* Updated [Monotone numerical flux](/definitions/monotone-flux.md) (batch-18 block: Roe with entropy fix classed as an E-flux).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (batch-18 block: one bullet on the E-flux classification).
* Updated item 3 of [Cockburn & Shu (1998)](/sources/cockburn-1998.md) (the cited Proposition 2.1 is part IV's) and a set-up row on [Burgers shock formation](/benchmarks/burgers-shock-formation.md).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1989-MathComp-Cockburn-101090S0025-5718-1989-0983311-4.pdf`.
   * **Version read.** The publisher's version (AMS typesetting, 25 PDF
     pages = pp. 411–435), received February 23, 1988; not a preprint.
   * **Identity.** doi:10.1090/S0025-5718-1989-0983311-4 (from the archive
     filename), checked on Crossref: "TVB Runge-Kutta local projection
     discontinuous Galerkin finite element method for conservation laws.
     II. General framework", Math. Comp. 52(186):411–435, 1989, authors
     Cockburn and Shu, reference count 28; agrees with page 1.
   * **How it was read.** Text layer for prose; every equation used here,
     the figures, tables and the reference list checked on page images
     (pp. 414–435).
   * **Recorded as printed** (reader's reading).
     - §4 prints neither the CFL number nor the bound that fixes $M$, nor
       the quadrature rule.
     - Example 1 does not state its domain; the figures span $[-1, 1]$.
     - The $K = 2$ proof of Lemma 2.10 is omitted by the authors; the
       proofs of Lemmas 2.3 and 2.8 are referred to Shu and to Cockburn.
   * **Reference list:** 28 entries, all merged. Part I, printed as IMA
     Preprint 388, is `cockburn-1991` (RAIRO M2AN 25:337); Chavent &
     Cockburn's IMA preprint is `chavent-1989` (M2AN 23:565). The printed
     order swaps two pairs of keys: Harten & Osher (SIAM J. Numer. Anal.
     24:279) is `harten-1987-b` and Harten, Engquist, Osher & Chakravarthy
     `harten-1987`; Shu (SIAM J. Sci. Stat. Comput. 9:1073) is `shu-1988-b`
     and Shu & Osher (J. Comput. Phys. 77:439) `shu-1988`. One printed entry
     covers van Leer's parts II and V (`vanleer-1974`), one Hughes' four
     parts (`hughes-1986`), one three Cockburn preprints (`cockburn-1986`).
     Johnson's undated preprint takes the citing date (`johnson-1989`). This
     list supplies the title of `osher-1985`, "Convergence of generalized
     MUSCL schemes". Bibliography: 3380 entries.
