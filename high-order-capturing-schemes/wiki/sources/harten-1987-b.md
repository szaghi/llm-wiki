---
type: Source
title: "Harten & Osher (1987) — Uniformly high-order accurate nonoscillatory schemes. I"
description: "Paper I of the ENO series: defines nonoscillatory schemes (the number of local extrema does not increase), reduces their design to a reconstruction problem, and builds the second-order UNO2 scheme, whose slope is the minmod of the one-sided derivatives of a nonoscillatory piecewise-parabolic interpolant, O(h^2)-accurate at extrema; nonlinear scalar scheme, formal extension to systems, and 1D tests against a TVD scheme that differs only in the slope."
resource: "doi:10.1137/0724022"
source_kind: paper
authors: [Harten A., Osher S.]
year: 1987
venue: "SIAM J. Numer. Anal. 24:279–309"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1987-SINUM-Harten-1011370724022.pdf"
tags: [eno, uno, reconstruction, tvd, muscl, critical-points]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The first paper of the series that leads to ENO. It defines a
*nonoscillatory* scheme: the solution operator does not increase the
**number of local extrema** (§1), a weaker requirement than
[TVD](/properties/total-variation-diminishing.md). With the design
principle reconstruct–evolve–average (§2), cell averaging is
nonoscillatory and exact evolution is TVD, so the scheme is
nonoscillatory if the reconstruction has no more local extrema than the
data. The reconstruction is piecewise linear, as in MUSCL, with slopes
taken as the minmod of the one-sided derivatives of a nonoscillatory
piecewise-parabolic interpolant, which picks in each interval the less
oscillatory of two candidate parabolas by a minmod of second differences
(§§3–4). These slopes are $O(h^2)$-accurate everywhere, extrema included,
where minmod-MUSCL slopes are $O(h)$; the resulting **UNO2** scheme stays
second order at extrema, at the price of the TVD property (the TV can grow
by a bounded amount, eq. 5.5b). Uniform TV boundedness is left unproved.
The nonlinear scalar scheme (§6) is proved uniformly second order,
extrema and sonic points included; §7 compares UNO2 with a TVD2 scheme
that differs only in its slopes, on advection, Burgers and Sod's problem.

# Key claims

1. **Nonoscillatory schemes** (§1, p. 280). The solution operator "is only
   required to diminish the number of local extrema in the numerical
   solution" ("diminishing" meaning "nonincreasing"). Every essentially
   3-point TVD scheme that is an average of monotone Riemann solvers has
   the property (citing Osher & Tadmor). Unlike TVD, such a scheme may
   "occasionally accentuate a local extremum"; it is monotonicity
   preserving. Uniform TV boundedness follows once the maximum norm is
   uniformly bounded.
2. **TVD degeneracy quantified** (§1, p. 280). High-order TVD schemes
   "necessarily degenerate into first-order accuracy" at local extrema;
   the cumulative global error is $O(h)$ in $L_\infty$, $O(h^{3/2})$ in
   $L_2$ and $O(h^2)$ in $L_1$, "(see [17])", a reference absent from the
   printed list. Footnote 1 (p. 282): TVD schemes, "no matter how they are
   constructed", lose accuracy at extrema.
3. **Series programme** (§1, p. 280): "In a sequence of papers, of which
   the present paper is the first, we show how to construct nonoscillatory
   schemes that are uniformly high-order accurate … In this first paper we
   describe a second-order accurate scheme of this type." The paper states
   **no order limit** for nonoscillatory schemes.
4. **Design reduces to approximation** (§2, eqs. 2.1–2.3). Reconstruct,
   solve exactly, average; hence "the design of nonoscillatory high-order
   accurate schemes essentially boils down to a problem on the level of
   approximation of functions" (p. 281).
5. **Accuracy of cell averages** (eqs. 2.9–2.10). Second order means
   $O(h^3)$ local error in the cell averages; for higher orders the
   cell-average and pointwise definitions differ, "not only conceptual but
   of practical importance as well" (p. 283).
6. **Nonoscillatory piecewise-parabolic interpolant** (§3, eqs. 3.1–3.4).
   On $[x_i, x_{i+1}]$ the parabola through $u_i$, $u_{i+1}$ takes as its
   second difference $\operatorname{minmod}(\Delta^2 u_{i-1}, \Delta^2 u_i)$:
   of the two candidate parabolas, on $\{x_{i-1}, x_i, x_{i+1}\}$ and
   $\{x_i, x_{i+1}, x_{i+2}\}$, it takes the one that "deviates the least
   from the line connecting" the two points. Error $O(h^3)$, one-sided
   derivatives $O(h^2)$ where $u$ is smooth (3.1c). Two candidates sharing
   $\{x_i, x_{i+1}\}$, chosen by the smaller second difference: a
   one-step precursor of the ENO stencil choice (reader's reading).
7. **The interpolant is nonoscillatory** (pp. 285–286). It has no more
   local extrema than the data; an interior extremum in an interval occurs
   iff the limited second difference exceeds twice the first difference
   (3.5); its TV exceeds $\sum_i\vert\Delta^1 u_i\vert$ by at most a quarter
   of the limited second differences on the intervals with an interior
   extremum (3.8c), and tends to $TV(u)$ for piecewise-smooth data (3.9).
8. **The UNO2 reconstruction** (§4, eqs. 4.2, 4.8). Piecewise linear,
   $\mathcal P_i = \bar u_i + \hat u^{(1)}_i\zeta$, with
   $$\hat u^{(1)}_i = \operatorname{minmod}\left(\Delta^1\bar u_i - \tfrac12\operatorname{minmod}(\delta^2\bar u_i, \delta^2\bar u_{i+1}),\ \Delta^1\bar u_{i-1} + \tfrac12\operatorname{minmod}(\delta^2\bar u_{i-1}, \delta^2\bar u_i)\right)$$
   (4.8b, 7.1c, 7.3, in registry symbols): $h$ times the minmod of the two
   one-sided derivatives of the interpolant of the cell averages. The slope
   approximates $\partial_x u$ to $O(h^2)$, "true also at local extrema
   points" (4.4b, p. 287); the reconstruction is monotone in an interval
   iff the interpolant is (4.7b); $TV$ of the reconstruction is at least
   $TV$ of the interpolant (4.16).
9. **Why TVD schemes lose order** (§2, p. 282). Their slopes approximate
   $\partial_x u$ only to $O(h)$, and the loss at extrema "is due to lack of
   smoothness of the coefficient in the $O(h)$ term at these points".
   "Unfortunately there is a price to pay for this extra accuracy, namely
   the loss of the TVD property."
10. **Constant coefficients** (§5, eqs. 5.3–5.12). Exact evolution plus
    averaging, $\vert\nu\vert \le 1$. Nonoscillatory and second order; TV
    growth per step bounded by (5.5b), "clearly … overly pessimistic";
    monotone data stay monotone and mesh extrema are damped (5.8–5.9); at
    an interior extremum of the interpolant the new value follows the
    interpolant and may leave the data range by a bounded amount (5.10),
    "the essential difference between the present scheme and the
    'second-order' TVD schemes". In "rather rare" instances two modified
    TV norms also grew. Max-norm and TV boundedness are not proved, for
    "lack of theoretical tools to analyze pointwise regularity" (p. 291).
11. **Nonlinear scalar scheme** (§6, eqs. 6.4–6.7). The reconstruction is
    transported along piecewise-linear approximate characteristics whose
    speeds are the interface Roe speeds $\hat a_{i+1/2}$, after Harten's
    "to appear" paper; that approximate solution is conservative and TVD,
    so the scheme is nonoscillatory. The flux (6.7b) is upwind by the sign
    of $\hat a_{i+1/2}$ with a slope correction scaled by
    $1/[1 + \frac{\Delta t}{h}(\hat a_{i+1/2} - \hat a_{i-1/2})]$ (6.7c).
    Entropy is explicitly ignored ("we ignore entropy considerations",
    p. 292).
12. **Uniform second order** (eqs. 6.8–6.10). The flux error is $O(h^2)$
    with a smooth coefficient, so the scheme is second order "wherever
    $u(x,t)$ is smooth, including local extrema and sonic ($f' = 0$) points"
    (p. 294).
13. **CFL** (§6 Remark 2, eqs. 6.12–6.13). Halving the time step to keep the
    approximate solution single valued "is completely unnecessary"; the
    scheme stays nonoscillatory under $\Delta t\max_i\vert\hat a_{i+1/2}\vert < h$.
14. **Variants** (Remarks 3–4; §7, eqs. 7.9–7.10). Nonuniform and moving
    meshes; a random-choice variant; FNO2/FVD2 with the flux at the
    time midpoint, nonoscillatory only for constant coefficients; ANO2,
    initialized with exact cell averages, recovers point values by
    differentiating the interpolant of the primitive
    $\mathcal U(x_{i+1/2})$ (7.10b–d).
15. **Systems** (§7, eqs. 7.12–7.15). A "formal extension" with a Roe
    average and field-by-field slopes in local characteristic variables; no
    artificial compression; the contact smears "like $n^{1/3}$, as
    expected" (p. 308).

# Tests

All 1D on $[-1, 1]$ with $N$ intervals; scalar data initialized pointwise
except ANO2.

1. **Approximation of $\sin\pi x$** (Table 1, Fig. 1). The interpolant is
   $O(h^3)$, both reconstructions $O(h^2)$; UNO2's error is "about a
   $\frac13$" of TVD2's. At $N = 80$, $L_\infty$: interpolant
   $3.104\times10^{-5}$, UNO2 $7.710\times10^{-4}$, TVD2
   $2.308\times10^{-3}$; $L_1$: $2.617\times10^{-5}$,
   $3.351\times10^{-4}$, $9.787\times10^{-4}$.
2. **Linear advection of $\sin\pi x$** (eq. 7.6, Table 2, Fig. 2).
   Periodic, $t = 2$, $\Delta t/h = 0.8$, $N = 20$–$160$. UNO2 second order
   in $L_\infty$ and $L_1$; TVD2 "second-order accurate in $L_1$ but only
   first-order accurate in $L_\infty$". At $N = 160$: UNO2 $L_\infty$
   $9.201\times10^{-5}$, $L_1$ $1.172\times10^{-4}$; TVD2 $L_\infty$
   $5.975\times10^{-3}$, $L_1$ $1.528\times10^{-3}$. The TVD degeneracy
   "adversely affects the accuracy everywhere".
3. **Discontinuous three-piece profile** (eq. 7.7, Figs. 3–5).
   $-x\sin(3\pi x^2/2)$ on $(-1, -\tfrac13)$, $\vert\sin 2\pi x\vert$ on
   $\vert x\vert < \tfrac13$, $2x - 1 - \tfrac16\sin 3\pi x$ on
   $(\tfrac13, 1)$, period 2; advection to $t = 2$ at $N = 40$, periodic
   and with inflow at $x = -1$. TVD2 shows "the damping effect" at extrema;
   the boundary treatment "does not seem to have degraded the performance
   of either scheme". Not the bundle's
   [composite advection profile](/benchmarks/composite-advection-profile.md).
4. **Burgers, smooth** (eq. 7.8, Table 3(a)). $u_0 = \sin\pi x$, periodic,
   CFL 0.5, $t = 0.15$ (shocks form at $1/\pi$). At $N = 160$: UNO2
   $L_\infty$ $3.985\times10^{-4}$, $L_1$ $1.965\times10^{-4}$; TVD2
   $1.837\times10^{-3}$, $3.621\times10^{-4}$. FNO2 (Table 3(b)):
   $1.251\times10^{-4}$, $5.270\times10^{-5}$; FVD2 "about the same as
   TVD2". ANO2 (Table 3(c)): $4.597\times10^{-4}$, $2.079\times10^{-4}$.
5. **Burgers, shock** (Figs. 6(a)–(d)). $u_0 = 2 + \sin\pi(x + 1)$,
   $t = 0.35$, $N = 20$; all four schemes nonoscillatory.
6. **Sod's problem** (eq. 7.11, Figs. 7–9). $\gamma = 1.4$, conserved data
   $(1, 0, 2.5) \mid (0.125, 0, 0.25)$; $N$, time and CFL not printed. Both
   schemes nonoscillatory, UNO2 "somewhat 'crisper'"
   ([Sod shock tube](/benchmarks/sod-shock-tube.md)).

# Notation map

| Harten & Osher (1987) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v^n_j$; $\bar u^n_j$ | $\bar u_i$ | numerical and exact cell averages; one registry symbol |
| $h$, $\tau$, $\lambda = \tau/h$ | $h$, $\Delta t$, $\Delta t/h$ | **collision**: $\lambda^{(p)}$ |
| $\mu = \lambda a$ | $\nu$ (signed) | **collision**: diffusion coefficient $\mu$ |
| $\hat f_{j+1/2}$ | $\hat f_{i+1/2}$ | |
| $E_h$ | words (solution operator) | |
| $m(x, y)$ | $\operatorname{minmod}$ | |
| $d_{j+1/2}u$ | $\Delta^1 u_j$ | |
| $D_j u$ | $\delta^2\bar u_j$ (averages), $\Delta^2 u_{j-1}$ (points) | |
| $D_{j+1/2}u$ | $\operatorname{minmod}(\delta^2\bar u_j, \delta^2\bar u_{j+1})$ | |
| $Q(x;u)$, $q_{i+1/2}$ | words (nonoscillatory piecewise-parabolic interpolant) | **collision**: weight power $q$, $q_k$ |
| $L(x;\bar u)$ | $\mathcal P_i$ with $K = 1$ | |
| $S_j$; $S^\pm_j$ | $\hat u^{(1)}_i$; words (one-sided slopes) | **collision**: $S$, $S_L$, $S_R$, $S_k$ |
| $\bar a_{j+1/2}$ | $\hat a_{i+1/2}$ | |
| $M$, $M_n$ | words (intervals with an interior extremum) | **collision**: TVB $M$ |
| $\gamma_{j-1/2}$, $\sigma_{j-1/2}$, $\theta^n_j$ | words | **collisions**: $\gamma$, $\sigma$, $\theta$ |
| $V^n_{j+1/2}$ | $\mathcal U(x_{i+1/2})$ | |
| $R^k_{j+1/2}$, $\bar a^k_{j+1/2}$ | $r^{(p)}$, $\hat a_{i+1/2}$ of field $p$ | |
| $\rho$, $m$, $E$, $P$ | $\rho$, $\rho v_x$, $E$, $p$ | **collision**: $P$ big-stencil polynomial, $m$ system size |

# Pages created or updated

* Updated [Essentially non-oscillatory (ENO property)](/definitions/essentially-non-oscillatory.md) (batch-18 block: the nonoscillatory rung at its source; no order limit stated there).
* Updated [ENO reconstruction and schemes](/methods/eno-reconstruction.md) (batch-18 block: UNO2, the two-candidate interpolant as precursor, the tests).
* Updated [Tsai et al. (2012)](/sources/tsai-2012.md), item 4, and a set-up row on [Burgers shock formation](/benchmarks/burgers-shock-formation.md).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1987-SINUM-Harten-1011370724022.pdf`.
   * **Version read.** The publisher's version (SIAM scan, 31 pages =
     pp. 279–309, "Downloaded 11/05/12" banner); received May 1, 1985,
     revised version accepted April 12, 1986. The bibliography's note on a
     report version (MRC Technical Summary Report 2823, May 1985) is not
     mentioned by the paper; the received date is consistent with it.
   * **Identity.** doi:10.1137/0724022, checked on Crossref: "Uniformly
     High-Order Accurate Nonoscillatory Schemes. I", SIAM J. Numer. Anal.
     24(2):279–309, April 1987, authors Harten and Osher, reference count
     16.
   * **How it was read.** The OCR layer garbles every equation; every
     equation, table and the reference list were read from page renders
     (110 dpi; reference [10] at 300 dpi).
   * **Recorded as printed** (reader's reading).
     - [17] is cited for the global-error rates (p. 280) but the printed
       list ends at [16]; the work is unidentified.
     - The year of [10] is damaged ("19?4"), read as 1984.
     - "Figures 3(a) and 3(b)" for the advection test of Fig. 2 (p. 297);
       "initial data given by (7.2)" for (7.7) (p. 299); "Riemann problem
       (7.1b)" for (7.11) (p. 308); "$\phi(x)$" for the function of (7.7).
     - The approximate solution of §6 is taken from Harten's "to appear"
       paper; its derivation is not in this one.
   * **Reference list:** 16 printed entries, all merged. Harten's "to
     appear" "On second-order accurate Godunov-type schemes" is
     `harten-1982`; Harten & Hyman (J. Comput. Phys. 50:235) is
     `harten-1983-c`; Jameson & Lax (MAE Report 1650) is `jameson-1984-b`;
     Chakravarthy & Osher, AIAA 85-0363, "A new class of high accuracy TVD
     schemes", is `chakravarthy-1985-b`; Osher & Chakravarthy, "Very high
     order accurate TVD schemes" (ICASE Report 84-44), is `osher-1986`;
     Osher & Tadmor (Math. Comp., submitted) is `osher-1988-b`; Osher's
     "Convergence of generalized MUSCL schemes", printed as both a NASA
     report and SIAM J. Numer. Anal. 22:947, is `osher-1985`; [10] is
     `osher-1984`. Bibliography: 3380 entries.
