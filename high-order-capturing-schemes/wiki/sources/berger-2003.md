---
type: Source
title: "Berger et al. (2003) — h-box methods for the approximation of hyperbolic conservation laws on irregular grids"
description: "Systematic study of h-box finite-volume methods on grids with cells much smaller than a reference length h: interface fluxes of a small cell come from Riemann problems between states averaged over boxes of length h, so the step follows h; linear-interpolation h-box values with a second-order correction built on h give a proved second-order scheme for 1D advection with one small cell (supraconvergence), observed second order on irregular 1D grids and a 2D nonuniform tensor grid, a transonic-rarefaction defect cured by Lax–Friedrichs fluxes; no cut cells and no embedded boundary."
resource: "doi:10.1137/S0036142902405394"
source_kind: paper
authors: [Berger M.J., Helzel C., LeVeque R.J.]
year: 2003
venue: "SIAM J. Numer. Anal. 41:893–918"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2003-SINUM-Berger-101137S0036142902405394.pdf"
tags: [small-cell-problem, irregular-grid, wave-propagation, boundary-treatment]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper studies **h-box methods**: finite-volume schemes on grids that
contain cells much smaller than a reference length $h$. The fluxes at the
interfaces of a small cell come from Riemann problems between *h-box
values*, states averaged over boxes of length $h$ next to each interface,
so the time step is set by $h$ ($\nu \le 1$ with $\nu$ computed on $h$)
and not by the smallest cell (§§1, 3). The base scheme is LeVeque's
high-resolution wave-propagation algorithm (clawpack). The definition of
the h-box values decides accuracy: averaging the piecewise-constant data
gives an inconsistent but first-order ("supraconvergent") scheme
(Prop. 1), while linear interpolation with weight $2\kappa/(1+\kappa)$,
plus a second-order correction that uses $h$ rather than the small-cell
size, is second order for advection on a grid with one small cell
(Prop. 2), GKS-stable for $0 < \nu \le 1$ (Appendix A, shown
numerically). The h-box values are generalized to completely irregular
1D grids, second order is observed there for advection and smooth Euler
flow, a transonic-rarefaction defect with Godunov and Roe fluxes is cured
by Lax–Friedrichs fluxes (§6), and a 2D h-box method with modified
transverse propagation is stable for $\nu \le 1$ and second order on a 2D
nonuniform tensor grid (§7). **The paper treats grids with small cells,
not embedded boundaries:** its 2D tests have thin rows and columns of
cells, no cut cells, and §8 states that "So far there is no Cartesian
grid embedded boundary method that leads to a second order accurate
approximation at boundary cells", announcing an h-box embedded-boundary
scheme as forthcoming work.

# Key claims

The small cell $k$ has length $\kappa_k h$, $0 < \kappa_k \le 1$ (the
paper's $\alpha$); in 1D this is the cut-cell volume fraction of the
registry.

1. **Principle** (§§1, 3, Fig. 1, p. 896). At each interface of a small
   cell the scheme defines a left and a right state representing the data
   over a box of length $h$. This restores the domain of dependence of a
   regular cell, "a necessary stability condition", and replaces the
   time-step restriction (2.5), which has the cell length in the
   denominator, by one with $h$ ("CFL$_h$", p. 895).
2. **Base scheme** (§2, eqs. 2.1–2.5). First-order wave propagation: the
   update uses fluctuations, sums of waves times the negative or positive
   parts of their speeds, from a Riemann solver at each interface; the
   second-order correction on an irregular grid (2.4) uses the mean of the
   two adjacent cell lengths and limited waves; stable for $\nu \le 1$
   computed on each cell (2.5).
3. **h-box values by averaging piecewise constants** (§3.1, eq. 3.1), as
   used by Berger & LeVeque and Forrer & Jeltsch: the value inside the box
   that covers the small cell is $\kappa_k\bar u_k + (1-\kappa_k)\bar u_{k\pm1}$.
   For advection with positive speed $a$ the small-cell update becomes
   $\bar u^{n+1}_k = \bar u^n_k - \frac{a\Delta t}{h}(\bar u^n_k - \bar u^n_{k-1})$
   (3.2): the small denominator disappears. Its truncation error in cell
   $k$ is $\frac{a}{2}(\kappa_k - 1)\partial_x u + O(\Delta t, h)$,
   inconsistent unless $\kappa_k = 1$ (p. 897).
4. **Proposition 1** (p. 897). Scheme (3.2) is nevertheless first-order
   accurate for smooth advection solutions (proof by a Wendroff–White
   modified grid function plus stability for $\nu \le 1$).
5. **Consistent h-box values by linear interpolation** (p. 898, eq. 3.3).
   Consistency forces the interpolation weight $2\kappa_k/(1+\kappa_k)$:
   $$u^{\mathrm{hb}}_{k-1/2} = \frac{2\kappa_k\bar u_k + (1-\kappa_k)\bar u_{k+1}}{1+\kappa_k},\qquad u^{\mathrm{hb}}_{k+1/2} = \frac{2\kappa_k\bar u_k + (1-\kappa_k)\bar u_{k-1}}{1+\kappa_k}$$
   for the two values seen from inside the small cell (written here with a
   page-local superscript; the outer values are the neighbour averages).
   The advection update (3.4) divides the difference by $h(1+\kappa_k)/2$;
   it is first order, exact for linear functions and consistent in the
   neighbours too (p. 899). The formula was first given by Berger &
   LeVeque (1990), "not further investigated there". Equivalently: the
   h-box averages of a piecewise-linear reconstruction (3.9)–(3.10).
6. **System update** (eq. 3.6). The small-cell update uses fluctuations
   from Riemann problems between h-box values plus the physical fluxes of
   the two inner h-box values, and reduces to the regular scheme for
   $\kappa_k = 1$.
7. **The second-order correction must use $h$** (§3.2). The natural
   analogue (3.7) of (2.4), with $(1+\kappa_k)h/2$, has truncation error
   $O(h^2, \Delta t^2)$, but "numerical tests showed that such an approach
   is not stable for time steps satisfying CFL$_h\le1$" (p. 900). The
   adopted correction (3.8) uses $1 - \frac{\Delta t}{h}|s|$ for each wave
   speed $s$ of the h-box Riemann problems. Its truncation error in cell
   $k$ has non-cancelling first-order terms.
8. **Proposition 2** (p. 900). Scheme (3.4) with (3.8), unlimited, is
   second-order accurate for smooth advection solutions on a grid with
   one small cell, in that cell and in its neighbours, hence globally
   (p. 901). Stability: Appendix A.
9. **Limiting** (§3.3). Wave limiters at small-cell interfaces compare
   with waves from two further h-boxes at distance $h$ (two extra Riemann
   problems per small-cell interface, Fig. 3); limited slopes inside the
   h-box construction use the van Leer limiter, capped at the unlimited
   slope "because only those values lead to a second order approximation
   in smooth regions" (p. 902).
10. **TVD and monotonicity** (§4). Stability comes from flux differences of
    size $O(\kappa_k h)$ across the small cell. Stern proved first-order
    h-box methods TVD for advection; $TV(u^{n+1}) \le TV(u^n)$ for
    $\nu \le 1$ under condition (4.1), always true for (3.1) and true for
    (3.4) with a TVD slope limiter, with more than one small cell too. The
    (3.1) scheme is monotone for advection, the (3.3) scheme is not;
    neither is monotone for Burgers (p. 903)
    ([TVD](/properties/total-variation-diminishing.md)).
11. **Completely irregular 1D grids** (§5, eqs. 5.1–5.3, Fig. 4). An h-box
    may cover more than two cells; its value is an average of a
    piecewise-linear reconstruction, with slopes needed only in the partly
    covered end cells. **Proposition 3:** the first-order upwind h-box
    scheme with (5.3) is first order on irregular grids (proof only in the
    preprint, Berger et al. 2002). With (3.8), second order is observed
    (Fig. 5).
12. **Transonic rarefactions** (§6). h-box methods give unphysical
    oscillations at sonic points where standard Godunov schemes do not:
    Burgers with the exact Godunov flux (Fig. 9a), Euler with Roe and the
    standard entropy fix (Fig. 10). A Lax–Friedrichs flux between h-box
    values, with dissipation coefficient $h/(2\Delta t)$, removes them
    (Figs. 9b, 11). The preprint proves a discrete entropy inequality for
    the Godunov-flux h-box method away from sonic points, which can fail at
    a sonic point; a less dissipative entropy fix is future work.
13. **2D h-box** (§7). Unsplit, on the multidimensional wave-propagation
    algorithm. The normal-direction update (7.2) built on (3.6) is stable
    for $\nu \le \tfrac12$; with second-order corrections in $x$ and $y$
    (7.3) and modified transverse propagation (geometric fractions of the
    fluctuations; the physical-flux terms of (7.2) folded into the
    fluctuations first, Fig. 12) it is stable for $\nu \le 1$ (p. 912).
14. **Conclusions** (§8, p. 915). "The definition of the h-box values is
    important in order to construct accurate schemes"; "So far there is no
    Cartesian grid embedded boundary method that leads to a second order
    accurate approximation at boundary cells"; an h-box embedded-boundary
    scheme is "forthcoming work".
15. **Appendix A (GKS stability).** Lax–Wendroff on each side of one small
    cell, linear interpolation as boundary condition. A maximum-principle
    argument plus a *numerical* evaluation of the root function on the
    unit circle for $0 \le \kappa \le 1$, $0 < \nu \le 1$ (Fig. 16) shows
    stability; "we can show only analytically that $f(z)\le1$ for
    $\lambda>0.5$" ($\lambda = \nu$ here). Quadratic interpolation with the
    same three-point interpolant for both sides reduces the region to
    $\nu < 0.5$; an upwind-biased one keeps $\nu \le 1$ (p. 917).
16. **No grid smoothness needed** (§§1–2). Some Lax–Wendroff versions on
    nonuniform grids are second order only if the ratio of adjacent cell
    lengths is $1 + O(h)$ (Wendroff–White, Pike), and Morton showed
    large-time-step high-resolution methods second order on nonuniform
    grids only for smoothly varying grids; the h-box method "does not
    require this smoothness assumption" (pp. 894, 896).

# Tests

1. **1D advection, irregular grids** (§5.1, Figs. 5–6). $u_0 = \sin(2\pi x)$
   on $[0,1]$, periodic, $t = 0.75$, plots at $h = 0.04$.
   Linear-interpolation h-box with (3.8): observed orders 2.03 and 2.01
   (Fig. 5b; the figure does not say which norm each is). Piecewise-constant
   h-box with (3.8): 1.00 and 1.02 (Fig. 6b). Accuracy "compares well" with
   the standard irregular-grid scheme at much larger time steps.
2. **Example 5.1, smooth Euler on an irregular grid** (§5.2, Fig. 7,
   Table 5.1). Cells between $h/10$ and $h$ on $[0,1]$, reflecting walls,
   $\rho = 1 + 0.4\sin(\pi/2 + \pi x)$, $v = 0.25 - (x - 0.5)^2$, $p = 1$,
   $\gamma = 1.4$; $L^1$ density error against a fine regular-grid
   reference. Unlimited orders ($h$ = 0.01→0.005): 1.94, 1.89, 1.91, 1.80,
   1.67 at $t$ = 0.2, 0.4, 0.6, 0.8, 1; (0.02→0.01): 1.92, 1.86, 1.87,
   1.73, 1.72. Minmod-limited (0.01→0.005): 1.80, 1.63, 1.30, 1.33, 1.62;
   (0.02→0.01): 1.57, 1.62, 1.51, 1.46, 1.70. Example value: unlimited,
   $h = 0.005$, $t = 0.2$: 7.7282d-6.
3. **Example 5.2, colliding flows** (§5.2, Fig. 8). $\rho = 1$, $p = 1$,
   $v = \pm1$ meeting at $x = 0.5$, $\gamma = 1.05$, $t = 0.5$; irregular
   cells smaller than $h = 0.01$ on the left half, regular on the right;
   $\nu \approx 0.9$. Limited: no spurious oscillations, but the shock in
   the irregular part is more smeared than its mirror ("a jump in the
   conserved quantities can influence several h-box values"); unlimited:
   oscillations (Fig. 8b).
4. **Transonic rarefaction, Burgers** (§6, Fig. 9). $u = -0.5 \mid 0.5$ at
   $x = 0.5$, irregular grid, first order: the exact Godunov flux
   oscillates at the sonic point, Lax–Friedrichs does not.
5. **Transonic rarefaction, Euler** (§6, Figs. 10–11).
   $(\rho, v, p) = (1, 0.75, 1)$ for $x \le 0.3$ and $(0.125, 0, 0.1)$
   beyond, $\gamma = 1.4$, $t = 0.2$: first-order Roe with the standard
   entropy fix oscillates near the sonic point (Fig. 10b), Lax–Friedrichs
   does not (Fig. 11). The data are those of the modified Sod problem
   ([Sod shock tube](/benchmarks/sod-shock-tube.md)); the paper does not
   name it.
6. **Example 7.1, 2D advection** (§7, Fig. 13). $\partial_t u + \partial_x u + \partial_y u = 0$,
   $u_0 = \sin(2\pi x)\cos(2\pi y)$ on $[0,1]^2$, periodic; two rows and
   two columns of cells of width $0.1h$ and $0.9h$, the rest $h\times h$;
   $t = 1$, $\nu \approx 0.9$ on $h$. h-box orders 2.19 and 2.09
   (Fig. 13d); standard irregular-grid clawpack at $\nu \approx 0.9$ on the
   small cells: 2.00 and 2.00 (Fig. 13c). The h-box error is "slightly
   smaller", attributed to numerical viscosity: the standard scheme runs at
   $\nu \le 0.1$ away from the small cells.
7. **2D Euler Riemann problem** (§7, Fig. 14). The four-shock
   configuration of Schulz-Rinne, Collins & Glaz
   ([two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)),
   with 10 rows and 10 columns of widths between $0.1h$ and $0.9h$,
   $h = 0.005$, $t = 0.8$, MC limiter: matches the uniform-grid solution
   except at the unstable contact lines (qualitative).

# Notation map

| Berger et al. (2003) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $Q^n_i$ | $u$, $\bar u^n_i$ | lower case for exact grid functions, capitals for numerics (p. 897) |
| $f(q)$, $g(q)$ | $f(u)$; $\mathbf f$ | 2D fluxes (7.1) |
| $\Delta x_i$, $\Delta y_j$ | $h_i$; $h_x$, $h_y$ per cell | |
| $h$ | $h$ | reference (regular) cell length |
| $\alpha$, $\alpha_i$ ($\Delta x_i = \alpha_i h$) | $\kappa_i$ | **collision**: $\alpha$ is the Lax–Friedrichs speed; in 1D the small-cell fraction is the cut-cell volume fraction |
| $\lambda$ (interpolation weight, §3.1) | words | **collision** with the eigenvalues $\lambda^{(p)}$ |
| $\lambda = \Delta t/h$ (Appendix A) | $\nu$ | unit speed, so it is the Courant number |
| CFL, CFL$_h$ | $\nu$ on $h_i$; $\nu$ on $h$ | |
| $Q^L_{i+1/2}$, $Q^R_{i+1/2}$; $Q^{LL}$, $Q^{RR}$ | page-local $u^{\mathrm{hb}}$, or words (h-box values) | **collision risk**: $u^\pm_{i+1/2}$ are reconstructed point values; h-box values are box averages of length $h$ |
| $\mathcal W^p_{i+1/2}$, $s^p_{i+1/2}$, $M_w$ | words (waves, wave speeds, number of waves) | $s^p = \lambda^{(p)}$ of the Roe matrix with a Roe solver; $s$ is the RK stage count |
| $\mathcal A^\pm\Delta Q$, $\mathcal B^\pm\mathcal A^\pm\Delta Q$ | words (fluctuations, transverse fluctuations) | |
| $\tilde F^2$, $\hat F^2$, $\hat G^2$ | words (second-order correction fluxes) | |
| $\phi(\theta)$, $\theta_i$ (van Leer limiter and ratio) | words | **collision**: PPM $\phi_i$, limiter $\theta$ |
| $\sigma_i$ (slopes) | words | **collision**: Hu–Adams–Shu $\sigma$ |
| $\rho,\sigma,\kappa,\tau,z,\eta$ (Appendix A) | words | **collisions** with density, $\sigma$, $\kappa$, $\tau$, $\eta$ |
| $\rho$, $u$, $p$, $E$, $\gamma$ | $\rho$, $v$, $p$, $E$, $\gamma$ | Euler |

# Pages created or updated

* Updated [Cut-cell (embedded-boundary) finite volume](/methods/cut-cell-finite-volume.md)
  (batch-18 block: the h-box principle and what this paper proves; the
  "second order at cut cells" attribution qualified; a supraconvergence
  bullet added to the Open flux-redistribution entry, which stays Open).
* Updated [Berger & Giuliani (2021)](/sources/berger-2021.md): a
  qualification of key claim 1 ("h-box (second order …)").

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2003-SINUM-Berger-101137S0036142902405394.pdf`.
   * **Version read.** The SIAM version of record ("Downloaded 12/02/14"
     stamp), 26 pages. Received 10 April 2002; revised version accepted
     1 November 2002; published electronically 22 May 2003. The preprint
     (Conservation-law preprint server 2002-022, the paper's ref. [2]) was
     not read; the proof of Proposition 3 and the entropy analysis are only
     there.
   * **Identity.** doi:10.1137/S0036142902405394, checked on Crossref:
     "H-Box Methods for the Approximation of Hyperbolic Conservation Laws
     on Irregular Grids", SIAM J. Numer. Anal. 41(3):893–918, 2003,
     authors Berger, Helzel, LeVeque; agrees with page 1. The bibliography
     entry spells the third author "Leveque"; page 1 prints "LeVeque".
   * **How it was read.** Text extraction of all sections; eqs. 2.3–2.5,
     3.1–3.10, the limited h-box values and 7.2–7.3 checked on rendered
     pages (pp. 895, 899, 900, 902, 910). Orders in Figs. 5, 6 and 13 read
     from the figure labels. Not reproduced: the transverse-update
     coefficients of Fig. 12(b) (text layer only).
   * **Recorded as printed.**
     - Eq. 7.3 prints "+" before the $y$ second-order correction term, where
       the $x$ term has "−" (p. 910, checked on the page image); apparently
       a misprint, not corrected.
     - Figs. 5b, 6b and 13c–d print two orders without saying which norm
       is which.
     - Refs. [3] and [5] both print pp. 305–311.
     - Appendix A's stability is numerical for $0 < \nu \le 1$ and
       analytical only for $\nu > 0.5$, as the paper says.
   * **Reference list:** 31 entries, all merged. The paper's own 2002
     preprint is `berger-2002`, kept separate ("the conservation-law
     preprint (2002-022) of berger-2003 itself, printed in its own
     reference list; kept as a separate entry"). Quirk (1994), Comput.
     Fluids 23:125, lands on `quirk-1994-c`. Same-key homonyms were
     resolved by venue: Berger (1985) Math. Comp. 45:301 is
     `berger-1985-b`, Berger & LeVeque AIAA-89-1930 `berger-1989-b`, the
     rotated difference scheme AIAA CP-91-1602 `berger-1991-b`, LeVeque
     SIAM J. Numer. Anal. 33:627 `leveque-1996-b`; the Uppsala proceedings
     of Berger & LeVeque is `berger-1990-b`, and their "Stable boundary
     conditions for Cartesian grid calculations" (Comput. Syst. Engin.
     1:305) lands on `berger-1990`, the ICASE 90-37 report of the same
     title. clawpack prints no year: `leveque-2003` ("no year printed in
     the citing reference; year is the citing paper's year, a
     placeholder"). Bibliography: 3380 entries.
