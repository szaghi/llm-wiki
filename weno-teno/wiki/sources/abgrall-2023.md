---
type: Source
title: "Abgrall & Barsukow (2023) — Extensions of Active Flux to arbitrary order of accuracy"
description: "Three routes to arbitrary-order Active Flux in one dimension (larger finite-difference stencils, extra interior point values, extra moments), each with linear stability analysis, transonic upwinding and order-reducing limiting, plus a proof that even orders are impossible with symmetric interior points."
resource: "doi:10.1051/m2an/2023004"
source_kind: paper
authors: [Abgrall R., Barsukow W.]
year: 2023
venue: "ESAIM Math. Model. Numer. Anal. 57:991-1027"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_ESAIM_Mathematical_Modelling_and_Numerical_Analysis_Abgrall_Extensions_of_Active_Flux_to_arbitrary_order_of_accuracy.pdf"
tags: [active-flux, finite-volume, finite-difference, limiting, benchmark]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

[Active Flux](/methods/active-flux.md) (AF) solves $\partial_tu+\partial_xf(u)=0$ with two kinds of
degrees of freedom: cell averages $\bar u_i$ and point values $u_{i+1/2}$ at the interfaces. The two
neighbouring cells share each interface value, so the reconstruction is globally continuous
($C^0$). The averages are updated conservatively with the interface values as fluxes. The point
values are updated independently, with upwinding and without a Riemann solver. All earlier AF
methods were at most third order, since they use one parabola per cell.

The paper gives three extensions to arbitrary order in one dimension:

- **Variant A, larger stencils.** The interface values follow the method of lines, with new
  mixed finite-difference formulas FD1–FD7c that combine point values and averages. Each formula
  has one free parameter, tuned for stability with
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) RK3. Upwinding splits the Jacobian.
- **Variant B, interior point values.** $k$ point values are added inside each cell. The
  reconstruction is in $\mathbb P^{k+2}$ and the scheme stays characteristics-based. A theorem
  shows that even orders are impossible when the interior points are symmetric about the cell
  centre.
- **Variant C, higher moments.** Moments are added as degrees of freedom, and the point values
  are updated by compact "moment differences".

Each variant gets a transonic-upwinding fix and an order-reducing limiter, whose last fallback is a
monotone power-law reconstruction. Linear stability is checked by a von Neumann analysis with the
Schur–Cohn–Miller criterion. The tests are convergence studies for advection and Burgers, a
transonic Burgers Gaussian, and the [Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md). No
variant is best in every respect.

In passing, the paper:

- recalls that an AF analogue of the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
  was shown by Abgrall (2020) (§1);
- recalls that AF for linear acoustics on Cartesian grids is vorticity preserving and low-Mach
  compliant (§2.1), while a multi-dimensional Godunov method with the exact acoustic Riemann
  solver is neither (§1);
- notes that the [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) cannot
  respect prescribed interface values (§2.2);
- mentions Riemann solvers only as what AF avoids.

# Version read

The file is the authors' preprint: pdfTeX, PDF created 2022-09-25, with no journal typesetting and
no ESAIM header. It runs to 40 pages: main text pp. 1–37, references pp. 37–39 and Appendix A
pp. 39–40. The preprint uses its own page numbers 1–40, so the journal pagination 991–1027 does
not appear. All section, equation, table and figure numbers cited here are the preprint's. Page 1
matches the published title and authors (Abgrall, Zurich; Barsukow, CNRS/Bordeaux), so there is no
identity issue.

# Key claims

1. Traditional AF with a parabolic reconstruction (one $\mathbb P^2$ polynomial per cell) is at
   most third order. Before this paper only third-order AF methods had been proposed. (§2, §2.1,
   §7) **Stated**
2. The semi-discrete AF of Abgrall (2020) (midpoint value via Simpson's rule, half-spacing finite
   difference, RK time integration) is stable up to $\nu=0.77$. (§2.1, after (17), App. A)
   **Stated**
3. The original van Leer AF for linear advection, with exact parabolic evolution and Simpson flux
   quadrature (eqs. (23)–(24)), is stable up to $\nu=1$. (§2.1) **Stated**
4. Recalled from Barsukow (2021): for monotone data, the parabola through $u_{i\pm1/2}$ with
   average $\bar u_i$ is monotone iff
   $(u_{i+1/2}-\bar u_i)/(\bar u_i-u_{i-1/2})\in[\tfrac12,2]$. (Thm. 2.1, eq. (26)) **Stated**
5. The switched reconstruction (power law 1, power law 2 or parabola) is continuous as a function
   of $\bar u_i$. The power laws reduce to the parabola at ratio $2$ and $1/2$ respectively.
   (Thm. 2.2, eqs. (29)–(30)) **Stated**
6. Every AF limiter in the literature limits only the point-value update. The finite-volume step
   (31) stays unlimited, which does not rule out oscillations. Limiting it is left as future work.
   (§2.2) **Stated**
7. Early AF versions fail on transonic Burgers data ($2$ / $-1$). The wrong upwind estimate keeps
   all point values stationary while the middle-cell average grows without bound. The cause is
   that a continuous reconstruction can steepen into a shock within one step. (§2.3,
   eqs. (32)–(35), Figs. 2–3) **Derived**
8. For an AF method of order $n$ it is enough to approximate the derivative to order $n-1$.
   (§3.1, after (49)) **Stated**
9. The mixed formulas FD1–FD7c each have one free parameter. With the parameter optimized for
   SSP-RK3, the maximal CFL numbers are:
   - FD1: 1 ($a_2\in[1,2]$);
   - FD3a: 0.7985 ($a_3\simeq1.7723$); FD3b: 1 ($a_3\in[1/2,1.1]$); FD3c: 0.45 ($a_3\simeq3.5$);
   - FD4a: 0.675 ($a_4\simeq1.6$); FD4b: 0.855 ($a_4\simeq1.5$);
   - FD5a: 0.7 ($a_5\simeq1.88$); FD5b: 0.713 ($a_5\simeq1/4$); FD5c: 0.56 ($a_5\simeq2.3$);
   - FD6: 0.73 ($a_6\simeq0.68$);
   - FD7a: 0.657 ($a_7\simeq4/3$); FD7c: 0.62 ($a_7\simeq1.9$).

   (Tables 1–2, Figs. 4–15) **Shown**
10. FD1 is first order for general $a_2$ and second order for $a_2=4$. (Table 1 caption)
    **Stated**
11. For FD5b, RK5 raises the maximal CFL number only slightly above its RK3 value. (§3.2,
    Figs. 11–12) **Shown**
12. Beyond third order, writing the cell average through interface and midpoint values (as in
    Abgrall 2020) becomes non-local, because it needs a linear system. The paper therefore uses the
    general mixed form (37). (§3.1, eqs. (50)–(52)) **Derived**
13. On transonic upwinding for variant A:
    - the paper's modified transonic upwinding (53) degrades accuracy at sonic points, whereas the
      original Barsukow (2021) modification keeps third order;
    - averages such as $(u_{i-1/2}+2u_{i+1/2}+u_{i+3/2})/4$ proved unsatisfactory;
    - for systems, evaluating the Jacobian at $u^n_{i+1/2}$ works well.

    (§3.3) **Stated**
14. The power-law derivatives (55)–(58) are first-order nonlinear fallback differences. They are
    used only when all of the following hold: the stencil values are monotone, all higher-order
    formulas violate monotonicity, (26) is violated, and the exponent lies in $[1/50,50]$. (§3.4)
    **Stated**
15. Variant A attains its theoretical orders 3–7:
    - on linear advection (Gaussian, RK3, CFL $10^{-2}$, $t=0.1$);
    - on Burgers before shock formation (CFL $10^{-3}$, $t=0.01$).

    Free parameters close to the stability limit make the order hard to observe. Among stencils of
    equal order, the choice changes the error constant. (§3.5.1–3.5.2, Figs. 16, 18) **Shown**
16. With limiting and transonic upwinding, variant A captures the transonic Burgers Gaussian without
    artifacts (100 cells, CFL 0.4). Its sixth-order version runs Sod (100 points, CFL 0.25).
    (§3.5.2–3.5.3, Figs. 17, 19) **Shown**
17. With $k$ interior point values, the reconstruction is in $\mathbb P^{k+2}$ and stays globally
    $C^0$. The order is $k+3$, with $k+2$ degrees of freedom per cell on average. (§4, §4.1)
    **Stated**
18. Theorem 4.1 reduces the mixed point/average interpolation problem to pointwise interpolation:
    $p=p_1+p_2\,(\Delta x\,\bar y-\int p_1)/\int p_2$, which is unique when $\int p_2\ne0$.
    (Thm. 4.1, eq. (71)) **Proved**
19. Take $n-1$ interpolation points symmetric about the cell centre, with $n-1$ odd. Then
    $\int p_2=0$ and no reconstruction exists, so even-order variant-B methods are impossible with
    symmetric interior points. Placing the points asymmetrically makes even orders possible.
    (Thm. 4.2, §4.1) **Proved** (the asymmetric case is **Stated**)
20. Variant B of fifth order is stable for every CFL number in $(0,1]$ under two conditions: the
    leap-frog-type integrator with correct upwind-cell selection (95)–(96), and interior points
    near the interfaces, $\xi_1=-\xi_2\gtrsim0.4$. The authors know no simple reason why. Inside
    the stable range, the point location has no visible influence on the results. (§4.2,
    Fig. 20) **Shown**
21. Variant B converges at fifth and seventh order:
    - on linear advection (CFL 0.5, exact evolution, Gauss–Lobatto in time with $M=4$ and $M=5$
      points, $t=0.01$);
    - on Burgers before shock formation.

    (§4.5.1–4.5.2, Figs. 21, 23) **Shown**
22. For the Euler equations, variant B uses the approximate evolution operator of Barsukow (2021),
    which is formally only third order. The authors liken this to combining RK3 with spatially
    high-order methods. (§4.5.3, Fig. 24) **Stated**
23. The moment equations (100) are exact up to the quadrature of $\int x^{p-1}f(u)\,dx$. For a
    linear flux they close as (103), so the accuracy of variant C depends only on the point-value
    update. (§5.1) **Derived**
24. The moment differences are unique for every order. The coefficients of the even moments and of
    the point values sum to zero. (§5.2, eq. (113)) **Derived**
25. Variant C with RK3 is stable up to CFL 0.13 (MD5) and 0.066 (MD7). Experiments suggest
    CFL $<0.17$ for MD5 with RK5 and CFL $\le0.1$ for MD7 with RK7. (§5.3) **Shown**
26. Variant C converges at the design orders for advection and Burgers (CFL $10^{-4}$, RK3). With
    limiting and transonic upwinding, it resolves the transonic Burgers shock without sonic-point
    artifacts (CFL 0.01). Its seventh-order version runs Sod (CFL 0.01). (§5.6, Figs. 25–28)
    **Shown**
27. Roe's (2021) Hermite-type extension stores interface derivatives up to order $s$:
    - it gives a $\mathbb P^{2s+2}$, $C^s$ reconstruction with $s+2$ degrees of freedom per cell
      and order $\le2s+3$;
    - spatial derivatives cannot raise the order of the time quadrature of the flux;
    - its fifth-order version appears stable up to CFL 1.

    (§6) **Stated**
28. Comparing the variants:
    - B has the best stability;
    - C keeps a compact stencil but has the smallest CFL numbers;
    - A and C apply directly to any hyperbolic system without a Riemann solver;
    - no variant outperforms the others in all respects.

    (§7) **Stated**
29. Abgrall (2020) proved the Lax–Wendroff-type convergence theorem for AF. AF for linear acoustics
    on Cartesian grids is vorticity preserving and low-Mach compliant. A truly multidimensional
    Godunov method with the exact acoustic Riemann solver has neither property. (§1, §2.1)
    **Stated**

# Printed slips

- **Eq. (51).** The preprint prints
  $\bar q_i=(-4q_{i-1,\mathrm{mid}}+34q_{i-1/2}+144q_{i,\mathrm{mid}}+34q_{i+1/2}-q_{i+1,\mathrm{mid}})/180$.
  The coefficients sum to $207/180\ne1$ and are not symmetric. The five-point rule for the cell
  average on nodes $x_i+\{-1,-\tfrac12,0,\tfrac12,1\}\Delta x$ has weights $(-1,34,114,34,-1)/180$.
  *(compiler check, not in the sources: solved the moment equations up to degree 4 symbolically)*
- **Eq. (52).** The preprint prints $(-4q_{i-3/2}+189q_{i-1/2}+704q_{i,\mathrm{mid}}+189q_{i+1/2}-q_{i+3/2})/1080$.
  The coefficients sum to $1077/1080$. The correct weights on nodes
  $\{\pm\tfrac32,\pm\tfrac12,0\}\Delta x$ are $(-1,189,704,189,-1)/1080$, so the leading $-4$ is
  wrong. *(compiler check, not in the sources: same symbolic solve)*
- **Eqs. (55)–(56).** The two interface derivatives are attached to the wrong power law or the wrong
  end:
  - the derivative of power law 1 at $+\Delta x/2$ is
    $\frac1{\Delta x}(q_{i+1/2}-q_{i-1/2})\frac{q_{i+1/2}-\bar q_i}{\bar q_i-q_{i-1/2}}$, which the
    preprint prints as (56) with the label "power-law 2";
  - the derivative of power law 2 at $-\Delta x/2$ is the expression printed as (55), with the
    label "power-law 1".

  $D_1$ (57) is consistent with power law 1 at $+\Delta x/2$. *(compiler check, not in the
  sources: differentiated (27)–(28) symbolically)*
- **§3.5.1.** "FD1 ($a_4=4$)" should be $a_2=4$, as in the Table 1 caption and §3.4.
- **Eq. (63).** The energy equation is printed as $\partial_te+\partial_x(\rho v)=0$; the energy
  flux should be $(e+p)v$.
- **Thm. 4.1.** Conditions (68)–(69) are written with $p(x_j)$ where $p_1(x_j)$, $p_2(x_j)$ and
  $p_2(x_0)$ are meant, and the proof's (73) writes "$p_{recon}$".
- **Thm. 4.2.** The non-existence is stated for "(68)–(69)" but concerns (70). The proof opens with
  "Take $n$ to be even", where $N$ is meant.
- **§5 vs Def. 5.1.** In the §5 introduction $k$ counts the moments including the average. In
  Def. 5.1 the moments run over $p=0,\dots,k$.
- **Eq. (111).** The preprint claims $\mathcal O(\Delta x^N)$ for the moment difference of an
  $N$th-order method. MD5 is exact for degree $\le4$ but not 5, so the error is
  $\mathcal O(\Delta x^{N-1})$, consistent with the rule of §3.1. *(compiler check, not in the
  sources: applied MD5 (114) to monomials of degree 0–6 with the moments (97))*
- **Eqs. (16)–(17).** Misplaced parentheses ("$q_{i+1,\mathrm{midpoint}(t)}$",
  "$q_{i+1/2-k}t$").
- **Def. A.1.** "$f'$ … derivative of $f$ with respect to $x$": the variable is $z$.
- **§3.2.** "Figures 6–15" should be Figures 4–15.

# Notation map

| Abgrall & Barsukow | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $f(q)$ | $u$, $f(u)$ | conserved variables, flux |
| $\bar q_i^n$ (also $q_i^{(0)}$) | $\bar u_i^n$ | cell average |
| $q^n_{i+1/2}$ | $u^n_{i+1/2}$ | a single shared interface value, not a pair $u^\pm_{i+1/2}$; AF needs no Riemann solver |
| $q_{\mathrm{recon},i}$ | $u^{\mathrm{rec}}_i$ (local) | in-cell continuous reconstruction |
| $P^k$ | $\mathbb P^k$ | polynomial space |
| $\lambda=c\Delta t/\Delta x$ | $\nu$ | CFL number; the source's $\lambda_\ell$ in (49) are eigenvalues $\lambda_l$ |
| $c$ | $a$ (advection speed) | **collision**: the registry's $c$ is the sound speed |
| $f'=R\,\mathrm{diag}(\lambda)R^{-1}$, $f'^\pm$ | $A=R\,\mathrm{diag}(\lambda_l)L$, $A^\pm$ | |
| $R(\cdot)$ (point-value residual) | $\mathcal R$ (local) | **collision** with the eigenvector matrix $R$ |
| $D$, $D^*$ | $D$, $D^*$ (local) | mixed difference and its mirror; not the DG differentiation matrix $D$ |
| $a_2,\dots,a_7$ | $\mathsf a$ (local) | free parameter of the formulas FD1–FD7c |
| $b^{(0)}_j$, $b_{j+1/2}$ | kept (local) | coefficients of the mixed formula (37) |
| $\tilde q_{i+1/2}$ | $\check u_{i+1/2}$ (local) | state at which the upwind Jacobian is evaluated; registry $\tilde u_{i+1/2}$ is the normalized face value |
| $\omega_\ell$ | — | **collision**: time-quadrature (Simpson / Gauss–Lobatto) weights, not the WENO weights $\omega_k$ |
| $r=(q_{i+1/2}-\bar q_i)/(\bar q_i-q_{i-1/2})$ | $\mathsf r_i$ (local) | monotonicity ratio; not the registry's $r$ or TVD slope ratio $r_i$ |
| $N$ | order $n$ (local) | **collision**: the registry's $N$ is the DG degree |
| $k$ | $k$ | number of interior points (§4) or the highest moment index (§5), local |
| $q_i^{(p)}$, $A_p$ | $u^{(\ell)}_i$, $\mathcal N_\ell$ (local) | normalized moments; the source's $p$ also denotes the pressure |
| $p$, $p_1$, $p_2$, $\bar y$ (Thms. 4.1–4.2) | kept (local) | interpolating polynomials and prescribed average |
| $s$ (§6) | $s$ (local) | highest interface derivative stored by Roe's extension; not the entropy |
| $\xi_j$ | $\xi_j$ (local) | interior point locations in units of $\Delta x$, not LGL nodes |
| $\rho,v,p,e,\gamma$ | $\rho,v,p,E,\gamma$ | the source's $e$ is the total energy, the registry's $E$ |

# Reference list

The paper prints 23 references in alphanumeric-label style ([Abg20], [Bar21], …), ordered
alphabetically. The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` set to `abgrall-2023`. All items parse. Notes on individual items:

- [Abg20] is an arXiv preprint;
- [BB20] is printed as "submitted, 2020";
- [Sch17] and [Sch18] are two parts of Schur's work and are kept as distinct entries;
- [BK22] has no pages.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–3 (2026-10-22). This source is cited on:

* [Active Flux](/methods/active-flux.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
