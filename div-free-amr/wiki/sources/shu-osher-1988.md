---
type: Source
title: "Shu & Osher (1988) — Efficient Implementation of Essentially Non-Oscillatory Shock Capturing Schemes"
description: "The origin of TVD (strong-stability-preserving) Runge–Kutta time stepping in the convex Shu–Osher form, with the optimal second- and third-order schemes at CFL coefficient 1, and of the point-value flux ENO scheme built on Lax–Friedrichs flux splitting; scalar tests only, no divergence content."
resource: "doi:10.1016/0021-9991(88)90177-5"
source_kind: paper
authors: [Shu C.-W., Osher S.]
year: 1988
venue: "J. Comput. Phys. 77:439-471"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1988-JCP-Shu-1010160021-99918890177-5.pdf"
tags: [eno, tvd, finite-difference, high-order, shock-capturing, lax-friedrichs, time-integration]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Read as ICASE Report 87-33 (NASA CR-178304, May 1987), the report form
of the JCP article; equation, table and page numbers below are the
report's. The paper gives two simplifications for high-order
non-oscillatory schemes, aimed at multidimensional problems and forcing
terms.

**(i) TVD Runge–Kutta time discretization (§II).** An explicit
Runge–Kutta method is rewritten so that each stage is a convex
combination of forward-Euler steps (eq. 2.12). If the forward-Euler step
of the spatial operator is TVD (or TVB) under a CFL restriction, the
whole scheme is TVD under a reduced restriction (Proposition 2.1,
eq. 2.13). Negative step weights are handled by a downwinded operator.
The optimal second-order scheme (eq. 2.15) and the third-order scheme
(eq. 2.18) both have CFL coefficient 1; the third-order one is the scheme
later called SSP-RK3. Fourth- and fifth-order schemes need the downwinded
operator. This is compiled in
[SSP Runge–Kutta methods](/methods/ssp-runge-kutta.md).

**(ii) ENO from point values of the flux (§III).** A conservative
finite-difference scheme on point values, not cell averages: global
Lax–Friedrichs flux splitting, ENO adaptive-stencil Newton interpolation
of each split flux, upwind-started, plus fixed Taylor correction terms
that make the conservative difference of order $2m$. There are optional
TVB caps, general E-flux building blocks, a dimension-by-dimension
multidimensional extension and a field-by-field characteristic extension
to systems. §IV has preliminary scalar tests.

**The paper contains no divergence constraint.** It treats scalar
conservation laws only: no MHD, no $\nabla\cdot\mathbf B$, no
incompressibility, and no system is computed. The bundle's MHD sources
take from it the SSP-RK3 integrator and the point-value flux-difference
framework under FD-ENO/WENO ([WENO reconstruction](/methods/weno.md)).

# Key claims

1. **Setting** (§I, eqs. 1.1–1.7). Conservative scheme
   $u_j^{n+1} = u_j^n - \lambda(\hat f_{j+\frac12} - \hat f_{j-\frac12})$,
   $\lambda = \Delta t/\Delta x$ (1.3), consistent flux (1.4);
   $TV(u) = \sum_j |u_{j+1} - u_j|$ (1.5); TVD means
   $TV(u^{n+1}) \le TV(u^n)$ (1.6); TVB means $TV(u^n) \le B$ for
   $0 \le n\Delta t \le T$ (1.7). Local truncation error
   $O(\Delta x^{r+1})$ is called $r$-th order (p. 3).
2. **TVD time discretization** (§II, eqs. 2.1–2.6). Forward-Euler
   operator $T(u) = (I + \Delta t L)(u)$ (2.1) with
   $L(u) = \mathcal L(u) + O(\Delta x^r)$ (2.2); the time discretization
   is TVD if $TV(S(u)) \le TV(T(u))$ (2.5), so that a TVD/TVB Euler step
   gives a TVD/TVB scheme (2.6a/b).
3. **Downwind operator** (eqs. 2.7–2.9). If $T$ is TVD for
   $\lambda \le \lambda_0$ (2.7), $\tilde T(u) = (I - \Delta t\tilde L)(u)$
   (2.8), with $\tilde L(u) = \mathcal L(u) + O(\Delta x^r)$ (2.9), is
   required to be TVD under the same restriction: an approximation to the
   backward-in-time problem. For $u_t = u_x$, $L$ is the forward and
   $\tilde L$ the backward difference (p. 8).
4. **Convex form** (eqs. 2.10–2.12, p. 9). The explicit RK method (2.10)
   is rewritten as
   $$u^{(i)} = \sum_{k=0}^{i-1}\left[\alpha_{ik}u^{(k)} + \beta_{ik}\Delta t\,L(u^{(k)})\right],\qquad \alpha_{ik} \ge 0,\quad \sum_k \alpha_{ik} = 1,$$
   with $\beta_{ik} = c_{ik} - \sum_{\ell=k+1}^{i-1} c_{\ell k}\alpha_{i\ell}$;
   the time-dependent form (2.11) evaluates sources at
   $t^{(0)} + d_k\Delta t$, $d_k = \sum_{\ell<k} c_{k\ell}$.
5. **Proposition 2.1** (p. 10). Scheme (2.12) is TVD under
   $$\lambda \le \lambda_0 \min_{i,k} \frac{\alpha_{ik}}{|\beta_{ik}|}\qquad(2.13)$$
   provided $L$ is replaced by $\tilde L$ wherever $\beta_{ik} < 0$.
   **Remark 2.1:** $TV$ may be replaced by any convex functional $G \ge 0$
   on a Banach space, giving $G(u^m) \le G(u^0)$. This is the
   strong-stability-preserving property, stated here without that name.
6. **Second order** (eqs. 2.14–2.16). Accuracy conditions (2.14):
   $\alpha_{20} = 1 - \alpha_{21}$,
   $\beta_{20} = 1 - \frac{1}{2\beta_{10}} - \alpha_{21}\beta_{10}$,
   $\beta_{21} = \frac{1}{2\beta_{10}}$. Optimal scheme (2.15):
   $u^{(1)} = u^{(0)} + \Delta t L(u^{(0)})$,
   $u^{(2)} = \frac12 u^{(0)} + \frac12 u^{(1)} + \frac12\Delta t L(u^{(1)})$,
   CFL coefficient 1; it is Heun's (modified Euler) method (2.16).
7. **Third order** (eqs. 2.17–2.19). With $\alpha_{21}, \alpha_{30},
   \alpha_{31}, \beta_{10}$ free and
   $P = \beta_{20} + \alpha_{21}\beta_{10} + \beta_{21}$, the conditions
   (2.17) fix the $\beta$'s. "Extensive searching" gives (2.18):
   $$\begin{aligned} u^{(1)} &= u^{(0)} + \Delta t\,L(u^{(0)})\\ u^{(2)} &= \tfrac34 u^{(0)} + \tfrac14 u^{(1)} + \tfrac14\Delta t\,L(u^{(1)})\\ u^{(3)} &= \tfrac13 u^{(0)} + \tfrac23 u^{(2)} + \tfrac23\Delta t\,L(u^{(2)}) \end{aligned}$$
   CFL coefficient 1, no $\tilde L$, and each stage needs only
   $L(u^{(i-1)})$, which saves storage. Its Butcher-type form (2.19) is
   $u^{(3)} = u^{(0)} + \frac16\Delta t L(u^{(0)}) + \frac16\Delta t L(u^{(1)}) + \frac23\Delta t L(u^{(2)})$;
   the authors "have been unable to identify (2.19) with any of the
   classical third order RK methods", whose forms in Lambert give negative
   $\beta_{ik}$ and small CFL (p. 12).
8. **Fourth order** (eqs. 2.20–2.22). Seven equations in 16 unknowns;
   "Extensive searching seems to indicate that we cannot avoid negative"
   $\beta_{ik}$ (stated, not proved). Classical RK4 in form (2.12) is
   (2.20), CFL coefficient $2/3$, with $\tilde L(u^{(0)})$ and
   $\tilde L(u^{(1)})$. A re-weighted last stage (2.21) gives $137/200$;
   another scheme (2.22) gives 0.87, again with $\tilde L$ at the first two
   stages.
9. **Fifth order** (eq. 2.23). Lambert's fifth-order method in form
   (2.12): CFL coefficient $7/30$, with $\tilde L$ at $u^{(0)}$,
   $u^{(1)}$, $u^{(3)}$.
10. **Lax–Friedrichs building block** (§III, eqs. 3.1–3.4).
    $f^\pm(u) = \frac12(f(u) \pm \alpha u)$ with a constant
    $\alpha \ge \max|f'(u)|$ (3.1), $f^{+\prime} \ge 0$,
    $f^{-\prime} \le 0$ (3.2), $f^+ + f^- = f$ (3.3); LF flux
    $\hat f_{j+\frac12} = f_j^+ + f_{j+1}^-$ (3.4). This is **global** LF:
    one constant $\alpha$.
11. **Flux ENO by derivative corrections** (eqs. 3.5–3.9). The accuracy
    condition
    $$\hat f_{j+\frac12} = f_{j+\frac12} + \sum_{k=1}^{m-1} a_{2k}\Delta x^{2k}\left(\frac{\partial^{2k} f}{\partial x^{2k}}\right)_{j+\frac12} + O(\Delta x^{2m+1})\qquad(3.5)$$
    gives order $2m$, with $a_2 = -\frac1{24}$, $a_4 = \frac{7}{5760}$.
    Each split flux is interpolated by $p_j^\pm$, of degree $2m$ on $2m+1$
    points (3.8), and
    $\hat f^\pm_{j+\frac12} = p_j^\pm(x_{j+\frac12}) + \sum_k a_{2k}\Delta x^{2k}(d^{2k}p_j^\pm/dx^{2k})(x_{j+\frac12})$
    (3.9). The report does **not** introduce the implicit function whose
    cell averages are the point fluxes (the "flux primitive"); that form is
    Lemma 2.1 of [Shu & Osher (1989)](/sources/shu-osher-1989.md).
12. **ENO stencil selection** (eqs. 3.10–3.15). The stencil of $f^+$
    starts at $j$ (3.10), that of $f^-$ at $j+1$ (3.15): an upwind start.
    At level $n$ the left and right $n$-th divided differences are
    compared and the one of smaller modulus taken, extending the stencil
    on that side (3.11–3.13); Newton form (3.14).
13. **Remark 3.1** (pp. 17–18). First order recovers LF. Second order is
    "similar to the usual minmod second order TVD scheme", with minmod
    replaced by "the value closer to zero", and is TVD. For linear
    $u_t + au_x = 0$ the scheme is equivalent to the cell-average ENO of
    Harten et al. up to stencil choice.
14. **TVB cap** (eqs. 3.16–3.17). Capping the divided differences of
    order $n \ge 2$ by $M^{(n)}$ (3.16a) or $M^{(n)}\Delta x^{n-2}$ (3.16b)
    makes the flux a TVD second-order flux plus a correction bounded by
    $M\Delta x^2$ (3.17), hence TVB. Numerically there is "no essential
    difference" with or without the cap.
15. **Abandoned non-conservative variant** (eqs. 3.18–3.19). Updating by
    the derivative of the interpolant at $x_j$ is "essentially
    conservative" with the cap. Without it, a fifth-order run on a moving
    Burgers shock ($u_L = 2$, $u_R = -1$) puts the shock in the **wrong
    location**; with it the location is right but the shock is severely
    smeared (pp. 20–21).
16. **General E-flux building blocks** (eqs. 3.20–3.21). The LF flux is
    $C^\infty$, so accuracy holds everywhere. Godunov, Engquist–Osher and
    entropy-fixed Roe fluxes are not smooth at sonic points and lose
    accuracy there unless smoothed (pp. 21–22). No Roe-type (RF) ENO
    scheme is built in this report.
17. **Multidimensions and systems** (§III, pp. 22–23). Multi-D: the 1D
    procedure is applied to each flux derivative, and the RK CFL is
    "shrunk by a factor $(d)^{-1}$". Systems: $\alpha$ becomes a matrix
    $T(\bar u)\,\mathrm{diag}(\bar\lambda_i)\,T^{-1}(\bar u)$ at a frozen
    state $\bar u$, with $\bar\lambda_i \ge |\lambda_i(u)|$, and the split
    fluxes are interpolated field by field with the eigenvectors at $u_j$,
    then recombined. No system is computed; Euler work is "currently under
    way".

# Tests

All scalar; errors printed as "4.2-3" $= 4.2\times10^{-3}$. "$p$-$p$-LF-ENO"
is order $p$ in time and space with the LF building block; 3-3 uses
(2.18)/(2.19), 4-4 uses (2.20).

1. **1D Burgers** (§IV Ex. 1, eq. 4.1).
   $u_0 = \frac14 + \frac12\sin\pi x$ on $[-1,1]$, periodic, smooth until
   $t = 2/\pi$. CFL 0.8 (3-3) and 0.6 (4-4). Table 1 ($t = 0.3$,
   $\Delta x = 1/10, 1/20, 1/40$):
   * $L_\infty$ 3-3: 2.6-3, 2.3-4 (order 3.50), 3.1-5 (2.89); 4-4: 2.1-3,
     1.1-4 (4.25), 5.4-5 (4.35).
   * $L_1$ 3-3: 7.2-4, 5.7-5 (3.66), 6.5-6 (3.13); 4-4: 5.3-4, 2.5-5
     (4.41), 9.2-7 (4.76).

   Near the shock at $t = 2/\pi$ and $t = 1.1$ ($\Delta x = 1/40$): a
   one-point transition without oscillations (Figs. 1–12). Table 2
   (errors at distance $\ge 0.1$ from the shock, $\Delta x = 1/40$),
   3-3/4-4: $L_\infty$ 8.7-4/1.5-4 at $t = 2/\pi$, 1.6-4/1.6-5 at
   $t = 1.1$; $L_1$ 3.5-5/8.6-6 and 6.7-6/1.4-6.
2. **2D Burgers** (Ex. 2, eq. 4.2). $u_0 = \frac14 + \frac12\sin(\pi(x+y)/2)$
   on $[-2,2]^2$, dimension by dimension, CFL half the 1D value: 0.4 (3-3),
   0.3 (4-4). Table 3 ($t = 0.3$, $\Delta x = \Delta y = 1/5, 1/10, 1/20$):
   $L_\infty$ 3-3 2.7-3, 2.3-4 (3.55), 3.2-5 (2.85); 4-4 2.1-3, 1.1-4
   (4.21), 5.6-6 (4.36); $L_1$ 3-3 1.4-3, 1.1-4 (3.67), 1.3-5 (3.08); 4-4
   2.7-4, 1.3-5 (4.40), 4.5-7 (4.80). Table 4 (smooth region, $1/20$):
   $L_\infty$ 9.9-4/1.5-4 ($t = 2/\pi$), 1.6-4/1.7-5 ($t = 1.1$); $L_1$
   7.9-5/4.8-6 and 1.5-5/7.7-7. Same behaviour as in 1D.
3. **2D linear advection of a rotated square** (Ex. 3, eq. 4.3).
   $u_t + u_x + u_y = 0$ on $[-1,1]^2$, indicator of a unit square rotated
   by $\pi/4$, $\Delta x = 1/10$, $t = 16$ (8 periods; Figs. 13–20). Stable
   at half the 1D CFL; the 1D CFL "led to instability-overflow". Fourth
   order resolves the jumps better than third; over- and undershoots are
   "negligible".
4. **Nonconvex fluxes** (Ex. 4, eqs. 4.4–4.5).
   $f = \frac14(u^2-1)(u^2-4)$ with $u_L = 2$, $u_R = -2$ and with
   $u_L = -3$, $u_R = 3$: convergence to the entropy solution (Figs.
   21–32). Buckley–Leverett: 3-3-LF-ENO smears more than 3-3-EO-ENO
   (Figs. 33–38). The entropy condition is observed, not proved.

No Euler system, no MHD and no shock–entropy-wave test; that test is in
[Shu & Osher (1989)](/sources/shu-osher-1989.md).

# Notation map

| Shu & Osher (1988) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_j^n$ | $w_j$, time level $n$ | point value; **collision:** $u_h$ is the velocity field |
| $\Delta x$ | $h$ | grid spacing |
| $\Delta t$ | $\Delta t$ | |
| $\lambda = \Delta t/\Delta x$, $\lambda_0$ | words: CFL number, forward-Euler CFL limit | **collision:** $\lambda_k$ is a characteristic speed |
| $\lambda_i(u)$, $\bar\lambda_i$ | $\lambda_k$ | eigenvalues (§III systems) |
| $\mathcal L$, $L$, $\tilde L$ | words: spatial operator, its discretization, the downwinded discretization | not registered |
| $T$, $\tilde T$, $S$ | words: forward-Euler step, downwinded Euler step, full RK step | **internal collision:** $T(\bar u)$ is also the eigenvector matrix |
| $\alpha_{ik}$, $\beta_{ik}$, $c_{ik}$, $d_k$ | words: convex stage weights, forward-Euler step weights | **collision:** $\beta$ plasma beta, $\alpha^{\mathrm{LF}}$; $d_k$ linear WENO weight |
| $\alpha$ (eq. 3.1) | $\alpha^{\mathrm{LF}}$ | one global constant |
| $f^\pm$, $\hat f_{j+\frac12}$ | words: split fluxes, numerical flux | used on [WENO](/methods/weno.md) without registration |
| $TV(u)$ | words: total variation | not registered |
| $r$ (order) | words | **collision:** refinement ratio $r$ |
| $2m+1$ (interpolation points), $m$ | $k_{\mathrm s}$ for the point count | **internal collision:** $m$ is also the system size in §I; registry $m(E)$ is the SFC index |
| $a_{2k}$ | words: Taylor correction coefficients | |
| $M$, $M^{(n)}$ | words: TVB cap constants | |

# Pages created or updated

* Created [SSP Runge–Kutta methods](/methods/ssp-runge-kutta.md):
  convex form, Proposition 2.1, the second- and third-order schemes, the
  downwinded operator, fourth and fifth order.
* Updated [WENO reconstruction](/methods/weno.md): origin of the
  point-value flux form (Taylor corrections here, flux primitive in 1989),
  origin of the time integrator, the TVD status of classical RK4.
* Updated [Total variation diminishing (TVD)](/properties/total-variation-diminishing.md).
* Updated Source pages of [Jiang & Shu (1996)](/sources/jiang-shu-1996.md) and
  [Mignone, Tzeferacos & Bodo (2010)](/sources/mignone-tzeferacos-bodo-2010.md).

# Citations

1. `~/papers/mosaic/div-free-amr/1988-JCP-Shu-1010160021-99918890177-5.pdf`
   (copied from a sibling archive, D17).
   * **Version read.** Not the journal article: the file is NASA
     Contractor Report 178304 / ICASE Report No. 87-33, *Efficient
     Implementation of Essentially Non-Oscillatory Shock Capturing
     Schemes*, Chi-Wang Shu (IMA, University of Minnesota) and Stanley
     Osher (UCLA), contract NAS1-18107, May 1987: 34 numbered text pages
     and 38 figure pages. Every equation, table and page number on this
     page is the report's; their agreement with the JCP text is not
     verified.
   * **Identity.** doi:10.1016/0021-9991(88)90177-5, checked on Crossref:
     "Efficient implementation of essentially non-oscillatory
     shock-capturing schemes", Shu & Osher, J. Comput. Phys. 77(2):439–471,
     issued August 1988. Title and authors match the report.
   * **How it was read.** A scan with a good text layer for prose but
     almost no display equations; every equation was read from page
     renders.
   * **Recorded as printed.**
     * Table 1, 4-4-LF-ENO $L_\infty$ at $\Delta x = 1/40$ is printed
       "5.4-5", while the printed order 4.35 implies about 5.4-6 (reader's
       reading); not corrected.
     * The fifth-order coefficients (2.23) and the full coefficients of
       (2.22) were read on the page but not transcribed; only the CFL
       coefficients ($7/30$, $0.87$) and the $\tilde L$ stages are
       recorded.
     * The figures (38 pages) are qualitative and were not inspected in
       detail.
   * **Reference list.** 17 entries, all merged. Harten & Osher's MRC
     report is `harten-osher-1987`; the Saint-Etienne proceedings are the
     new `harten-1986-b`; Osher & Chakravarthy, SIAM J. Numer. Anal.
     21:955, is the new `osher-1984-b`. Bibliography key renamed
     `shu-1988` → `shu-osher-1988`; its DOI was corrected to
     10.1016/0021-9991(88)90177-5 (the stored string lacked the hyphen and
     does not resolve on Crossref). The bibliography holds 3779 entries
     after this batch.
