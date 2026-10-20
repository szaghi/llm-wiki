---
type: Source
title: "Babbar et al. (2022) — Lax-Wendroff flux reconstruction method for hyperbolic conservation laws"
description: "Builds an arbitrary-order single-step Lax–Wendroff time discretization inside flux reconstruction, computing the time-average flux Jacobian-free, and adds a dissipation model and face-flux construction that raise the Fourier CFL limit and restore optimal order on nonlinear problems."
resource: "doi:10.1016/j.jcp.2022.111423"
source_kind: paper
authors: [Babbar A., Kenettinkara S.K., Chandrashekar P.]
year: 2022
venue: "J. Comput. Phys. 467:111423"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Computational_Physics_Babbar_Lax-Wendroff_flux_reconstruction_method_for_hyperbolic_conse.pdf"
tags: [lax-wendroff, explicit, stability, hyperbolic-conservation-laws, ssp]
timestamp: 2026-10-20T10:00:00Z
---

# Summary

The paper builds a single-step, explicit, arbitrary-order
[Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md)
(LWFR) scheme for hyperbolic conservation laws $u_t+g(u)_x=0$ ($g$ the physical flux, source $f$). It is an
alternative to method-of-lines Runge–Kutta flux reconstruction (RKFR). A
Taylor expansion in time of order $N+1$, with time derivatives traded for
space derivatives through the PDE (Cauchy–Kovalevskaya), gives the update
$u^{n+1}=u^n-h\,\partial_xG$. Here $G$ is the truncated Taylor
approximation of the time-average flux over $[t_n,t_{n+1}]$. Flux
reconstruction is applied to $G$ instead of $g$. The time derivatives of $g$
are computed Jacobian-free by the approximate Lax–Wendroff procedure of
Zorío, Baeza and Mulet, which takes centred finite differences in time of
$g$ at Taylor-extrapolated states. The formulas are written out for orders
2 to 5.

The contributions are in the numerical flux. Dissipation model D2 evaluates
the dissipative jump with the time-average solution instead of $u^n$. It is
exactly upwind for constant linear advection and raises the Fourier-stable
CFL number by factors of 1.40 to 2.15. The face construction EA
(extrapolate, then average) avoids the half-order loss that the face
construction AE shows at odd $N$ on nonlinear problems. The CFL numbers come
from a [von Neumann stability analysis](/definitions/von-neumann-stability-analysis.md)
of the fully discrete scheme in 1-D and 2-D.

The paper compares LWFR with [SSP Runge–Kutta](/methods/strong-stability-preserving-runge-kutta.md)
FR. It cites the order barriers of explicit Runge–Kutta methods as the
motivation for a single-step scheme, and it places LW next to
[ADER](/methods/ader-time-integration.md). With inflow boundaries, LW imposes
a time-averaged boundary flux, which avoids the
[Runge–Kutta stage boundary](/methods/runge-kutta-stage-boundary-treatment.md)
issue. Tests run up to fifth order on [linear advection](/benchmarks/linear-advection-equation.md),
[Burgers](/benchmarks/burgers-equation.md), Buckley–Leverett, 1-D Euler
(including the [Sod shock tube](/benchmarks/sod-shock-tube.md)), the
[isentropic vortex](/benchmarks/isentropic-vortex.md) and the
[double Mach reflection](/benchmarks/double-mach-reflection.md). LW-D2
matches RKFR accuracy on nonlinear problems. On the vortex it is 1.1 to 1.7
times faster than RKFR in wall-clock time.

# Version read

arXiv:2207.02954v1 [math.NA], stamped 6 July 2022, running header "July 8,
2022", 54 pages, all read. This is the arXiv preprint, not the JCP version
of record (467:111423), although the archive filename says
"Crossref_Journal_of_Computational_Physics". Title and authors match the
published version. The file prints no DOI. Section, equation, table and
figure numbers on this page are those of arXiv v1.

# Key claims

Registry notation: $h$ is the time step (source $\Delta t$), $\nu$ the
Courant number (source $\sigma$). The PDE unknown $u$, the physical flux
$g(u)$ (source $f$), the polynomial degree $N$, the time-average flux $G$
(source $F$) and solution $U$, as on
[Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md), and the FR matrices $D$, $D_1$, $V_L$, $V_R$, $b_L$, $b_R$ are
page-local (see Notation map).

1. LW with the Taylor expansion truncated at $O(h^{N+1})$ and degree-$N$ FR
   in space gives a single-step scheme of order $N+1$ in space and time. The
   update (5) is the same at every order; only the time-average flux
   $G=\sum_{m=0}^N\frac{h^m}{(m+1)!}\partial_t^mg$ changes (§4, Eqs.
   (2)–(5)). **Derived**
2. The LWFR update is conservative: summing (5) with the quadrature weights
   gives $\int_{\Omega_e}u_h^{n+1}=\int_{\Omega_e}u_h^n-h[G_{e+1/2}-G_{e-1/2}]$
   (§4.1, Eq. (6)). **Proved** (short argument)
3. The approximate LW procedure needs only flux evaluations, no Jacobian or
   higher tensors; $\partial_t^mg$ must be approximated to $O(h^{N+1-m})$
   (§4.4). **Stated** (accuracy of the difference formulas asserted, citing
   [82, 8])
4. Explicit approximate-LW formulas are given for $N=1,2,3,4$ (§4.4.1–4.4.4):
   3-point centred differences for $N\le2$, 5-point for $N=3,4$. **Stated**
5. Dissipation model D1 (jump in $u^n$, as in [47]) is not upwind even for
   constant linear advection. D2 (jump in the time-average solution $U$)
   reduces to the exact upwind flux for $u_t+au_x=0$ (§5, Remark 1).
   **Derived**
6. For $g=a(x)u$, D2 is not exactly upwind because of interpolation errors;
   an upwind flux (10) written with the time-average flux only is defined
   instead (Remark 1, Eqs. (9)–(10)). **Derived**
7. D2 costs no more than D1, since $U$ is accumulated during the LW procedure
   (§5). **Stated**
8. 1-D Fourier CFL numbers (Table 1) for $N=1,2,3,4$. Radau correction: D1
   0.226, 0.117, 0.072, 0.049; D2 0.333, 0.170, 0.103, 0.069 (ratios 1.47,
   1.45, 1.43, 1.40). $g_2$ correction: D1 0.465, 0.204, 0.116, 0.060; D2
   1.000, 0.333, 0.170, 0.103 (ratios 2.15, 1.63, 1.47, 1.72) (§6, Table 1).
   **Shown** (eigenvalue sampling, about three decimals)
9. LWFR with Radau correction is identical to (LW-)DG, and its D2 CFL numbers
   agree with those of ADER-DG [19, 26] (§6). **Stated**
10. The Fourier CFL numbers are sharp: linear advection blows up for slightly
    larger steps (§6). **Shown** (statement of an experiment, no figure)
11. AE and EA coincide when solution points lie on the faces (GLL points) and
    for constant-coefficient advection; they differ for variable
    coefficients and nonlinear fluxes (Remark 3). **Derived**
12. LWFR with GL points and Radau correction equals the LW direct flux
    reconstruction scheme on the $N+3$ points $\{0,\xi_0,\dots,\xi_N,1\}$:
    $b_L$, $b_R$ and $D_1$ coincide (§4.3, Appendix C). **Proved**
13. Constant linear advection: RKFR has slightly smaller errors and slower
    error growth than LWFR, attributed to the superconvergence of RKDG [29].
    The superconvergent LWDG of [29] is not pursued because it couples more
    neighbours (§8.1.1, Figs. 3–4). **Shown**
14. At $N=4$ with periodic boundaries a mild linear instability appears for
    LW-D1, LW-D2, SSPRK55 and SSPRK54 at the LW-D1 CFL. The relative $L^2$
    norm grows linearly with slopes about 6.177e-10 (LW-D1), 5.415e-10
    (LW-D2), 2.862e-13 and 1.908e-13 (SSPRK54, SSPRK55). The authors say a
    similar instability seems present in ADER-DG and was studied for RKDG in
    [78] (§8.1.1, Fig. 5d). **Shown**
15. With inflow Dirichlet data, RK at its own stable CFL has slightly larger
    errors at $N=3,4$ than LW, possibly from the Dirichlet treatment inside
    RK stages [9]. LW imposes the boundary flux as the time average
    $\frac1h\int_{t_n}^{t_{n+1}}g(u_b(t))\,dt$ (boundary data $u_b$, source $g$) by $(N+1)$-point Gauss
    quadrature (§8.1.1, Fig. 6b, Remark 4). **Shown**
16. Variable advection $a(x)=x^2$: AE has larger errors than RK at odd $N$;
    EA is as accurate as RK at all $N$; the RK advantage of the
    constant-coefficient case disappears (§8.2, Figs. 16–17). **Shown**
17. 1-D Burgers, $u_0=0.2\sin x$: AE at odd $N$ converges at about
    $O(\Delta x^{N+1/2})$, EA at $O(\Delta x^{N+1})$ for all $N$. With AE only
    the global Lax–Friedrichs flux gives optimal rates. AE errors concentrate
    near sonic points $g'(u)=0$; "the reason for this behaviour is not known
    at present". Without sonic points AE is optimal (§8.3, Figs. 19–20).
    **Shown**
18. Radau correction gives clearly smaller errors than $g_2$ (Figs. 2, 19).
    $g_2$ fails on Shu–Osher at $N=1$ with the Table 1 CFL (pressure
    positivity) and needs CFL 0.44. The authors recommend Radau, GL points
    and EA (§9.7, §13). **Shown**
19. Bound and positivity preservation with the Zhang–Shu scaling limiter is
    not proved for LW. On Buckley–Leverett the bounds hold at the Fourier CFL
    for $N=4$ and need CFL 0.079 for $N=3$ (§8.4). **Shown**
20. LW calls the a-posteriori limiter (TVD/TVB, positivity) once per time
    step, RK once per stage (§7, Algorithms 1–2). **Stated**
21. HLLC and Roe fluxes resolve a stationary contact exactly in the LW scheme;
    Rusanov, LF and HLL smear it over two cells (§9.6, Fig. 28a). HLL, HLLC
    and Roe resolve the blast-wave density peak better than Rusanov; global
    LF does worse (Fig. 27). **Shown**
22. 2-D: the stability region in $(\nu_1,\nu_2)$ is $|\nu_1|+|\nu_2|\le\mathrm{CFL}$
    except at $N=1$, with D2 CFL numbers 0.259, 0.166, 0.101, 0.067 (Radau)
    and 0.511, 0.348, 0.178, 0.108 ($g_2$) for $N=1,\dots,4$ (Appendix B,
    Eq. (26), Table 2, Figs. 44–45). The step is reduced for oblique flow
    because 1-D face fluxes do not couple diagonal neighbours. **Shown**
23. Isentropic vortex: wall-clock time scales as (number of cells)$^{1.5}$.
    WCT(LW-D1)/WCT(LW-D2) is 1.4–1.5 for $N>1$, consistent with the Table 1
    CFL ratios. WCT(RK)/WCT(LW-D2) is about 1.1, 1.4, 1.7 for $N=1,2,3$ and
    about 1.2 at $N=4$, with RK at its own optimal CFL [26] (§12.1, Figs.
    37–40). No hardware is reported. **Shown**
24. Double Mach reflection, $N=2$, $960\times240$: LWFR-D2-EA and RKFR give
    similar resolution; the RK/LW-D2 WCT ratio lies between about 1.1 and 1.6
    depending on $N$ and grid (Figs. 41–43). **Shown**
25. Order barriers motivate LW: RK needs at least $p$ stages and more than
    $p$ at high order; no 5-stage RK has order 5 for nonlinear problems
    (Butcher [7], ch. 32); no SSPRK of order five has positive coefficients
    [54] (§1, §8, §9). **Stated**

# Printed slips

- §5.2 EA, degree $N=4$ (p. 12):
  "$u^{\pm2}_\alpha=V_\alpha^\top(u\pm2u^{(1)}+\frac{2^2}{2!}u^{(2)}\pm\frac{2^3}{3!}u^{(3)}+\frac{2^3}{3!}u^{(3)})$".
  The last term repeats $\frac{2^3}{3!}u^{(3)}$; by §4.4.4 it should be
  $\frac{2^4}{4!}u^{(4)}$.
- Fig. 19 caption: "(b) Radau vs g2, EA scheme, (c) LW-EA vs RK"; the text
  (§8.3) and the panel titles have (b) LW-EA vs RK and (c) Radau vs $g_2$.
- Fig. 34 caption: "No limiter is used in (b), (c) and TVB limiter (M = 100)
  is used in (d), (e)"; the text says (34b), (34d) are unlimited and (34c),
  (34e) use TVB, and the panels show (b), (c) LWFR and (d), (e) RKFR.
- Lax problem: text (§9.3) "using 100 cells"; Fig. 24 caption "on a mesh of
  200 cells".
- Fig. 8 caption "160 dofs"; text (§8.1.1) "using 200 dofs in each case".
- Figure 38 duplicates Figure 37 (same caption, apparently the same plots).
- §9, p. 27: "there is no four stage SSPRK method". The barrier is that no
  four-stage, fourth-order explicit SSP Runge–Kutta method with positive
  SSP coefficient exists.
- Introduction: "Qui and Shu [48]" (Qiu); "Safian et al. [55]" (the
  reference is Safjan and Oden); "compressible flaws". Ref. [16] prints the
  page range "411–411"; ref. [54] has no volume or pages.
- §1 roadmap omits Section 12 (2-D Euler results).

# Notation map

| Babbar et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t_n$, superscript $n$ | $h$, $t_n$, index $n$ | |
| $\sigma=a\Delta t/\Delta x$; $\sigma_1,\sigma_2$ | $\nu$; $\nu_1,\nu_2$ | Courant number; **$\sigma$ collides with the tree symmetry $\sigma(\tau)$** |
| $\Delta x_e$ | $\Delta x$ | element width, element index $e$ |
| $u_t+f(u)_x=0$ | $u_t+g(u)_x=0$ (page-local) | PDE unknown and physical flux, renamed as on the concept page: **the registry $f$ is the right-hand side $f(t,y)$**; the inflow data $g(t)$ is written $u_b(t)$ |
| $N$ | — | polynomial degree; order $N+1$ in space and time |
| $\xi\in[0,1]$, $\xi_j$, $w_j$, $\ell_j$ | — | reference coordinate on $[0,1]$, GL/GLL solution points, weights, Lagrange basis |
| $D$, $D_1$, $\tilde D$ | — | differentiation, corrected differentiation and direct-flux-reconstruction matrices; **$D$ is not Butcher's $D(\zeta)$** |
| $V_L$, $V_R$ | — | interpolation vectors to $\xi=0,1$ (printed "Vandermonde matrices") |
| $g_L$, $g_R$; $b_L$, $b_R$ | — | Radau or $g_2$ correction functions; their derivatives at solution points; **$b_L,b_R$ are not Runge–Kutta weights** |
| $F$, $G$ | $G$, $G^y$ (page-local) | time-average flux $\sum_{m=0}^N\frac{h^m}{(m+1)!}\partial_t^mg$ and its $y$-flux; renamed as on the concept page: **the registry $F(\tau)$ is the elementary differential** |
| $U$ | — | time-average solution $\sum_{m=0}^N\frac{h^m}{(m+1)!}\partial_t^mu$ |
| $u^{(m)}$, $f^{(m)}$ | $u^{(m)}=h^m\partial_t^mu$, $g^{(m)}=h^m\partial_t^mg$ | scaled time derivatives |
| D1, D2 | — | dissipation in $u^n$ / in $U$ |
| AE, EA | — | average-then-extrapolate / extrapolate-then-average face fluxes |
| $\lambda_{e+1/2}$ | — | dissipation wave speed; **not the Dahlquist eigenvalue $\lambda$** |
| **$T$** | — | $\sum_{m=0}^N(-\nu D)^m/(m+1)!$, time-average operator for advection; **collides with the set of trees $T$** |
| $H(\sigma,\kappa)$, $\kappa=k\Delta x$ | — | Fourier amplification matrix, nondimensional wave number |
| $M$ | — | TVB parameter; **collides with the mass matrix $M$** |
| SSPRK55, SSPRK54, RK65 | — | Gottlieb–Shu–Tadmor 5-stage (fifth order on linear autonomous problems only), Spiteri–Ruuth $(5,4)$, Tsitouras $(6,5)$ |

# Reference list

The paper prints 83 references in numbered, alphabetical style, with
leftover "bibtex: Key" tokens after many entries (ignored). All are merged
complete into the [bibliography](/bibliography.md) with `citedby`
babbar-2022. Refs. [14], [17], [18] and [74] print their authors as a ditto
dash, resolved to the preceding entry's authors. Ref. [34] (Huynh 2007)
prints no venue beyond "Miami, FL, June 2007, AIAA"; ref. [54] (Ruuth &
Spiteri 2002) has no volume or pages; ref. [7] prints "July 2016". Same-key
pairs take suffixes in printed order ([10], [11]; [15], [16]; [19], [20];
[73], [74]). No DOIs are printed.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Multiderivative Runge–Kutta methods and the backward derivative condition](/methods/multiderivative-runge-kutta.md)
* [Sod shock tube](/benchmarks/sod-shock-tube.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Trixi.jl](/software/trixi-jl.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
