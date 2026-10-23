---
type: Source
title: "Dawes (2021) — Some properties of the Runge-Kutta-Legendre super-time-stepping explicit methods"
description: "Reinterprets the Runge–Kutta–Legendre super-time-stepping recurrence as forward-Euler steps plus linear extrapolation, gives a simplified algorithm, and shows that with Dirichlet boundaries the RKL schemes lose monotonicity and positivity near the boundary at diffusion numbers far below the forward-Euler limit, with mesh-coarsening remedies and heat-equation tests."
resource: "doi:10.1016/j.compfluid.2020.104762"
source_kind: paper
authors: [Dawes A.S.]
year: 2021
venue: "Comput. Fluids 214:104762"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Computers_amp_Fluids_Dawes_Some_properties_of_the_Runge-Kutta-Legendre_super-time-stepp.pdf"
tags: [stabilized, runge-kutta, explicit, positivity, method-of-lines, stability]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper analyses the Runge–Kutta–Legendre (RKL1, RKL2)
super-time-stepping schemes of Meyer, Balsara and Aslam, a family of
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md),
on the linear heat equation semi-discretized by a cell-centred finite-volume
scheme in 1D. Its [stability polynomial](/definitions/stability-function.md)
is $P(z)=\mathsf a_s+\mathsf b_s\mathcal P_s(1+w_1z)$ with $\mathcal P_s$ the
Legendre polynomial of degree $s$, so one super step is
$h=w_1^{-1}h_{\mathrm e}$ with $h_{\mathrm e}$ the forward-Euler step:
$w_1^{-1}=s(s+1)/2$ for RKL1 and $(s-1)(s+2)/4$ for RKL2.

There are three contributions. First, a reinterpretation: the Legendre
three-term recurrence is a sequence of forward-Euler steps of size
$h_{\mathrm e}$ alternated with linear extrapolation in time; for RKL2 the
stage values are also a linear interpolation back to $t_n+c_jh$. A
"simplified algorithm" runs the pure recurrence and forms
$y_{n+1}=\mathsf a_sy_n+\mathsf b_sV_s$ at the end. Second, a
[positivity](/properties/positivity-preservation.md) analysis of the
one-step matrix $P(hL)$, entry by entry, closed form for $s\le4$ and
numerically beyond. With Neumann or periodic boundaries all entries are
non-negative under the forward-Euler condition $d_{\mathrm e}\le1/2$
($d_{\mathrm e}=\kappa h_{\mathrm e}/\Delta x^2$). With Dirichlet boundaries
entries near the boundary turn negative for all schemes except the 1-stage
RKL1 (FTCS) and the 2-stage RKL2, and the critical $d_{\mathrm e}^*$ falls
quickly with $s$. Up to $s-1$ cells per boundary may change sign. Two
fixed-mesh remedies are proposed: refinement or coarsening of the boundary
cells. Third, heat-front and heat-pulse tests against analytic solutions:
RKL is much cheaper than FTCS for smooth data, but on a compact pulse a
large $s$ inverts the peak and truncates the base. Fewer stages with more
outer cycles repair this. The recommendation is empirical: try several
stage numbers and study the sensitivity.

# Version read

Version of record (Elsevier typeset, Comput. Fluids 214 (2021) 104762),
23 pages, DOI printed on page 1; title, venue, volume and article number
match Crossref. Received 10 March 2020, available online 10 October 2020.
Pages 2–7 and 11–21 were read visually because extraction garbled the
equations, tables and the appendix formulas. No identity problem.

# Key claims

Registry notation: $h$ the super step (the source's $\Delta\tau_{sts}$),
$h_{\mathrm e}=w_1h$ the forward-Euler step ($\Delta\tau_e$), $s$ the stage
number (the source's "steps"), $L$ the semi-discrete Laplacian, $\kappa$ the
diffusivity, $\Delta x$ the mesh width and $d_{\mathrm e}=\kappa
h_{\mathrm e}/\Delta x^2$ (the source's $\beta_e$). $\mathcal P_j$ is the
Legendre polynomial and $\mathsf a_j$, $\mathsf b_j$ are the RKL stage
constants (not Butcher coefficients).

1. The RKL $s$-stage schemes are built from forward-Euler steps combined
   with linear extrapolation; RKL2 also uses linear interpolation (abstract,
   §4, §5, §9). **Derived** (the extrapolation weight equals the
   recurrence coefficient $(2j-1)/j$, Eq. (12)).
2. A simplified algorithm runs $V_j=\frac{2j-1}{j}XV_{j-1}-\frac{j-1}{j}V_{j-2}$,
   $X=I+w_1hL$, and sets $y_{n+1}=\mathsf a_sV_0+\mathsf b_sV_s$, computing the
   stages $Y_j$ only when the operator must be updated (§4, p. 2).
   **Derived**
3. For nonlinear systems the RKL recurrence "is not satisfied as it assumes
   the operator $\mathbb X$ remains the same on both sides of the
   expression" (§4). **Stated**
4. RKL1: $\mathsf b_j=1$, $w_1=2/(s(s+1))$, $h=\frac{s(s+1)}{2}h_{\mathrm e}$.
   RKL2: $w_1=4/((s-1)(s+2))$, $h=\frac{(s-1)(s+2)}{4}h_{\mathrm e}$
   (Eqs. (9), (10)). **Stated** (from Meyer et al.)
5. The condition on $h_{\mathrm e}$ (all entries of $X$ non-negative) is the
   same for all RKL schemes; only the condition on $h$ changes with $s$
   (§5, §6.1). **Stated**
6. For linear problems each scheme has an equivalent direct form in which
   forward-Euler data from $t_n$ to $t_n+sh_{\mathrm e}$ are scaled and
   summed; "the process of extrapolation and interpolation are hidden"
   (§5, Appendix A, Eq. (A.2)). **Derived**
7. Meyer et al. found the RKL schemes monotone (Convex Monotone Property)
   for $s<64$, but their analysis "did not include boundary conditions"
   (§5). **Stated** (citation)
8. With Neumann (zero-flux) and periodic boundaries all entries of $P(hL)$
   are non-negative for $d_{\mathrm e}\le1/2$ and the schemes are monotone
   (§6.2, §6.3, §7.2, Figs. 13–24, Appendix D). **Shown** (closed forms for
   $s\le4$, numerics beyond)
9. With Dirichlet boundaries (ghost-centre closure, $d_{\mathrm e}\le1/2$)
   the schemes are non-monotone near the boundary; only the 1-stage RKL1
   (FTCS) and the 2-stage RKL2 guarantee $P(hL)y_n\ge0$ (§6.1, §7.1).
   **Shown**
10. Critical $d_{\mathrm e}^*$ (Dirichlet, uniform mesh): RKL1 $s=2$:
    $\frac1{15}(6-\sqrt6)\approx0.24$; $s=3$: $\frac1{35}(10-\sqrt{30})\approx0.13$;
    $s=4$: $\frac1{210}(70-5\sqrt{10}-\sqrt{950+140\sqrt{10}})\approx0.08$;
    RKL2 $s=3$: $\frac1{35}(15-\sqrt{15})\approx0.32$; $s=4$:
    $\frac1{21}(7-\sqrt7)$, printed "$\sim0.18$" (see Printed slips)
    (§6.1.2–6.1.3). **Proved** (roots of closed-form polynomials)
11. Dirichlet non-monotone region for RKL1: left-boundary entries with
    $i+j\le s$ and right-boundary entries with $i+j+s\ge2(N+1)$, so $s-1$
    cells per boundary; RKL2 the same minus the corner entries (§7.1,
    Fig. 25). **Shown**
12. With some negative entries, non-negativity of the update holds iff
    $\sum_ja^+_{ij}y_{n,j}\ge\sum_ja^-_{ij}y_{n,j}$ for all $i$ (Eq. (23)),
    so it is data-dependent. **Derived**
13. Strategy 1 (local refinement): for 2-stage RKL1 on $100e^{-100x}$,
    $y_{n+1,1}\ge0$ is independent of $\Delta x$ for $d_{\mathrm e}\le
    d_{\mathrm e}^*$, and holds only for some resolutions above it (§6.1.5,
    Eq. (24), Fig. 8). **Shown**
14. Strategy 2 (coarsen the boundary cells by $g_c$): the grouped cells
    needed for $s=2..10$ are RKL1 4, 5, 7, 12, 17, 26, 50, 85, 205 and RKL2
    1, 5, 7, 9, 17, 26, 35, 85, 196 (§6.1.6, Table 3); accuracy is visibly
    lost (Fig. 12). **Shown** (numerical for $s\ge4$)
15. Coarsened-mesh non-negativity needs $d_{\mathrm e}\le
    g_c^2(1+g_c)/(1+3g_c)$, $d_{\mathrm e}\le(1+g_c)/(3+g_c)$ and
    $d_{\mathrm e}\le1/2$, the last dominating as $g_c$ grows (Eq. (30)).
    **Derived**
16. The face-based Dirichlet closure (Eq. (18)) needs $d_{\mathrm e}\le1/3$;
    the ghost-centre closure (Eq. (19)) needs $d_{\mathrm e}\le1/2$ and is
    adopted (§6.1). **Derived**
17. In a recursively built scheme the critical $d_{\mathrm e}^*$ differ from
    stage to stage and decrease; strategy 1 must use the lowest, while
    grouping sized for the final stage also covers earlier stages (§7.1).
    **Stated**
18. Monotone heat front ($N=1000$, $d_{\mathrm e}=9/20$, Neumann): 300-stage
    RKL1 agrees well with the analytic solution, FTCS is "much better" but
    needs over 150 times more applications of $X$ (45150 vs 300); 500-stage
    RKL1 has diverged; 700-stage RKL2 is significantly better (§8.1,
    Figs. 26–28). **Shown**
19. Diffused heat pulse: 100-stage RKL1 and FTCS agree with the analytic
    solution; 300-stage RKL1 has diverged; 425-stage RKL2 is much closer
    (§8.2, Figs. 29–31). **Shown**
20. Compact heat pulse, test A (support $[0.49,0.51]$), 10-stage RKL1, one
    cycle: the base is less diffused and the central peak inverted; Neumann
    and Dirichlet give no visible difference; recursive and direct forms
    agree (§8.3, Figs. 32–33). **Shown**
21. One RKL1 step spreads the base only $s$ cells each way, whereas FTCS
    over the same time spreads $s(s+1)/2$; "the extrapolation cannot fill
    in for the missing data" (§8.3). **Shown**
22. 2-stage RKL1 with 19 outer cycles (or 4-stage with 6) for the same end
    time restores the correct behaviour with fewer applications of $X$
    than FTCS (55) (§8.3, Fig. 34). **Shown**
23. Test B (support $[0.39,0.61]$): 10-stage RKL1 is good, 100-stage RKL1
    distorted, and 10-stage RKL1 with 92 cycles overlays FTCS and the
    analytic solution with over 5 times fewer applications of $X$ (§8.3,
    Figs. 35–38). **Shown**
24. RKL2: 15 stages over-extend the peak with kinks (test A), 160 stages
    show the same on test B; 30 stages with 28 cycles overlay the analytic
    and 2-stage results with over 15 times fewer applications of $X$ than
    the 2-stage method (§8.3, Figs. 39–41). **Shown**
25. The effective-stencil differences $a_{i+1,j}-a_{ij}$ (Eq. (40)) of
    10-stage RKL1 and 15-stage RKL2 are noisy and partly negative, so more
    than one extremum can arise; the 15-stage RKL2 central entry
    ($\approx0.52$ vs $\approx0.055$ analytic) explains the overestimated
    peak (§8.3.1, Figs. 42–44). **Shown**
26. "From the results the lower the number the steps used the better the
    outcome. For general applications the universal approach is to try
    different numbers of steps and study any sensitivities" (§8.3, §9).
    **Stated**
27. The same reinterpretations "can also be applied to the RKC methods"
    (§5, §9). **Stated** (not shown)

# Printed slips

- §6.1.3, 4-stage RKL2 Dirichlet: "$\beta_e^*\le\frac1{21}(7-\sqrt7)\sim0.18$".
  $(7-\sqrt7)/21=0.2073$, the correct smallest root of
  $a_{1,2}\propto2-18d+49d^2-42d^3$ *(compiler symbolic and numerical
  check, not in the sources)*; the decimal is wrong, the closed form right.
- (D.8), 3-stage RKL1 Dirichlet: "$a_{i,i+1}=6\beta_e(1-5\beta_e+\frac{35\beta_e^2}{36})$"
  should have $\frac{35\beta_e^2}{6}$; and "$a_{i,i+2}=\frac{5\beta_e^2}{4}(1-2\beta_e)$"
  should be $\frac{15\beta_e^2}{2}(1-2\beta_e)$, as printed correctly in
  (D.9)–(D.10).
- (D.18), 3-stage RKL2 Neumann: "$\frac{5\beta_e}{8}(4-15\beta_e+15\beta_{sts}^2)$"
  has $\beta_{sts}$ where $\beta_e$ is meant.
- (D.20), 4-stage RKL2 Dirichlet: "$a_{i,i+1}=\frac{9\beta_e}{2}(\dots)$"
  should be $\frac{9\beta_e}{4}(\dots)$; sign and root unaffected.
- Eqs. (35), (36): "$u=T_0[1-\cos(\pi x)]e^{-\nu\pi^2t}/2$" (and the
  $2\pi x$ analogue) does not solve the heat equation; the figures
  correspond to $\frac{T_0}{2}[1-\cos(\pi x)e^{-\nu\pi^2t}]$.
- §3: "an $s$-order shifted Legendre polynomial", where "order" means degree.
- §6.1.6.2: "second order accuracy only offers a small reduction in the
  number of combined cells" matches Table 3 only partly (fewer cells for
  $s=2,5,8,10$, equal otherwise).
- Typos: "2nd dd." (ref. [2]), "Mon Not R Astrom Soc" (ref. [11]), "feed
  back" for "fed back", "Table's 1 and 2", "forth row", "Gegenbauger";
  refs. [11], [12] print the first author "Meyer DM", ref. [14] "Meyer CD".

*(Compiler checks, not in the sources.)* All verifications are against the printed matrices (symbolic
recomputation of $P(hL)$); the appendix (E) asymmetric entries were not
re-verified.

# Notation map

| Dawes (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta\tau$ | $h$ | generic step; **the source's $h$ is the mesh width** |
| $\Delta\tau_{sts}$ | $h$ | super step of one RKL cycle |
| $\Delta\tau_e$ | $h_{\mathrm e}=w_1h$ | forward-Euler (FTCS) step; page-local, not the SSP bound $h_{\mathrm{FE}}$ |
| **$h$, $h_i$** | $\Delta x$ | **mesh width; collides with the step $h$** |
| $s$ "steps" | $s$ | number of stages (one application of $X$ each) |
| $du/dt=\mathbb Au$, $\mathbb D$ | $y'=Ly$, $L$ | linear semi-discrete operator |
| $\mathbf u^n$ | $y_n$ | |
| $\mathbf z=\mathbb D\Delta\tau$ | $z=h\lambda$ (matrix $hL$) | |
| $E(\mathbf z)$, $E_s$, $E_j$ ("the exponential") | $P(z)$, internal stage polynomials | stability polynomial of an explicit method |
| **$P_j$** | $\mathcal P_j$ | **Legendre polynomial; collides with the stability polynomial $P(z)$** |
| $\mathbb X=w_0\mathbb I+w_1\mathbf z$ | $X=I+w_1hL$ | $w_0=1$ for RKL; one application of $X$ is one FTCS step |
| **$a_j$, $b_j$** | $\mathsf a_j$, $\mathsf b_j$ | **RKL stage constants; collide with Butcher $A$, $b$** |
| $c_j$ | $c_j$ | effective stage abscissae, $c_s=1$; agrees |
| $A_j,B_j,C_j,D_j$ | — | recurrence coefficients (Eq. (11)) |
| $\mathbf Y_j$ | $Y_j$ | stage values; agrees |
| $V_j=P_j(\mathbb X)V_0$ | $V_j=\mathcal P_j(X)y_n$ | pure-recurrence vectors |
| **$\nu$** | $\kappa$ | **diffusivity; collides with the Courant number $\nu$** |
| **$\beta_e$, $\beta_{sts}$** | $d_{\mathrm e}$, $d$ | mesh Fourier numbers; **$\beta$ collides with Shu–Osher $\beta_{ij}$** |
| $\Omega$ | — | bound on $\beta_e$ (1/2); the tests run at $\Omega=9/20$ |
| $\beta_e^*$ | $d_{\mathrm e}^*$ | critical diffusion number (Dirichlet) |
| $\mathbb M_{D1},\mathbb M_{D2},\mathbb M_N,\mathbb M_P$ | — | scaled Laplacians (Dirichlet, coarsened Dirichlet, Neumann, periodic) |
| $a_{i,j}$, $a^\pm_{i,j}$ | — | entries of the one-step matrix and their positive/negative parts |
| $g_c$ | — | boundary-cell coarsening factor |
| $N_O$ | — | number of outer cycles |
| **$T$, $T^n$** | — | **temperature; $T^n$ in Eq. (1) is a power, not a time level; collides with the tree set $T$** |
| "monotone" | — | all entries of the one-step matrix non-negative (linear) |

# Reference list

The paper prints 15 references in numbered Vancouver-like style. All are
merged complete into the [bibliography](/bibliography.md) with `citedby`
dawes-2021. Ref. [3] is a conference poster, ref. [6] an M.Sc. thesis,
ref. [8] (Hypre) is undated with a corporate author and keyed by the
citing year; ref. [14] is printed in press ("J Comput Phys 2020;October",
no volume). Refs. [11], [12] print Meyer's initials "DM". No printed
duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping](/methods/stabilized-explicit-runge-kutta.md)
