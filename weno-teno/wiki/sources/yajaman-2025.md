---
type: Source
title: "Yajaman et al. (2025) — A new polynomial reconstruction scheme AENO-C for ADER methods to very-high orders of accuracy"
description: "AENO-C averages, coefficient by coefficient, the ENO polynomial and the centred-stencil polynomial with a new symmetric joining function, and is tested in one-dimensional ADER finite-volume schemes of orders 2 to 10 against ENO, AENO and WENO for accuracy, robustness and cost."
resource: "doi:10.1016/j.compfluid.2025.106777"
source_kind: paper
authors: [Yajaman S., Toro E.F., Demattè R.]
year: 2025
venue: "Comput. Fluids 301:106777"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Computers_amp_Fluids_Yajaman_A_new_polynomial_reconstruction_scheme_AENO-C_for_ADER_metho.pdf"
tags: [reconstruction, finite-volume, weno, very-high-order]
timestamp: 2026-10-23T15:06:00Z
---

# Summary

Yajaman et al. (2025) propose AENO-C ("AENO-centred"), a one-dimensional nonlinear
polynomial reconstruction for [ADER](/methods/ader-scheme.md) finite-volume schemes, built on
the [AENO reconstruction](/methods/aeno-reconstruction.md) of Toro et al. AENO writes the two
degree-$m$ polynomials on the stencils that contain the degree-$(m-1)$ ENO stencil in Taylor
form about $x_i$. Each coefficient is averaged with a weight given by a *joining function* of the
ratio of the coefficient magnitudes; the constant term is fixed by conservation of the cell
average. The paper makes two changes. A new joining function,
$\mathcal J(\mathsf s)=e^{-\mathsf s^{\mathsf p}}-e^{-1/\mathsf s^{\mathsf p}}$, gives exactly
$\mathcal J(0)=1$ and is antisymmetric under inversion, so the average no longer depends
on which polynomial is called left or right. And AENO-C averages the degree-$m$ ENO polynomial
with the polynomial on the centred stencil (for odd $m$ the almost-centred stencil closer to the
ENO stencil). Only two stencils are used, against $m+1$ for WENO, and the result is a closed-form
polynomial that can be evaluated anywhere in the cell.

The reconstruction feeds the Toro–Titarev solver of the
[generalized Riemann problem](/methods/generalized-riemann-problem.md), based on the
Cauchy–Kovalevskaya procedure, for orders 2 to 10. It is compared with ENO, AENO and Jiang–Shu
WENO on linear advection (a $\sin^4(\pi x)$ convergence test, a long-time square wave and the
[Jiang–Shu composite wave](/benchmarks/jiang-shu-composite-advection.md) over 1000 periods), on
[Burgers' equation](/benchmarks/burgers-equation-tests.md) with source terms, and on the Euler
equations: [density-wave advection](/benchmarks/density-wave-advection.md), a modified
[Sod tube](/benchmarks/sod-and-lax-shock-tubes.md) with a sonic rarefaction, the left half of the
[Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md) and the Toro–Titarev
variant of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md). AENO-C removes most of
AENO's order loss and reaches design order except at order 4. It stays non-oscillatory where
WENO oscillates, or fails at orders 7–10 on the Woodward–Colella half problem, and its
reconstruction is cheaper than WENO's. At order 10 the Cauchy–Kovalevskaya procedure takes
85.2 % of the run time.

# Version read

Version of record (Elsevier, open access), 25 pages, all read: received 22 March 2025, revised
16 July 2025, accepted 28 July 2025, available online 5 August 2025. Title, authors, venue and
DOI on page 1 match the Crossref record. Numbering cited on this page is that of the version of
record.

# Key claims

Registry notation (see the Notation map). Page-local: $m$ the polynomial degree of the
reconstruction (an ADER scheme of order $m+1$); $\mathsf c^{\mathrm L}_k$, $\mathsf c^{\mathrm R}_k$ the Taylor coefficients about
$x_i$ of the two candidate polynomials and $\tilde{\mathsf c}_k$ the averaged ones; $\mathcal J(\mathsf s)$ the
joining function, $\mathsf p$ its exponent, $\epsilon_{\mathrm J}$ the parameter of the
original one; ADER-$n$ the scheme of order $n$.

1. The original joining function $\mathcal J(\mathsf s)=(1-\mathsf s)/\sqrt{\epsilon_{\mathrm J}^2+(1-\mathsf s)^2}$ (Eq. 40) gives $\mathcal J(0)<1$ for every $\epsilon_{\mathrm J}>0$, so when $\mathsf c^{\mathrm L}_k=0\ne \mathsf c^{\mathrm R}_k$ the right coefficient keeps some weight: "an unintended bias" (§2.3, §3). **Derived**
2. With $\tilde{\mathsf c}_k=\tfrac12(1+\mathcal J(\mathsf s))\mathsf c^{\mathrm L}_k+\tfrac12(1-\mathcal J(\mathsf s))\mathsf c^{\mathrm R}_k$ and $\mathsf s=\lvert \mathsf c^{\mathrm L}_k\rvert/\lvert \mathsf c^{\mathrm R}_k\rvert$, the average is independent of the left/right labelling iff $\mathcal J(1/\mathsf s)=-\mathcal J(\mathsf s)$, which (40) does not satisfy (§3, Eqs. 43–45). **Derived**
3. The new family $\mathcal J(\mathsf s)=e^{-\mathsf s^{\mathsf p}}-e^{-1/\mathsf s^{\mathsf p}}$ (Eq. 46) satisfies $\mathcal J(1/\mathsf s)=-\mathcal J(\mathsf s)$, $\mathcal J(0)=1$, $\mathcal J(1)=0$, $\mathcal J\to-1$ as $\mathsf s\to\infty$, and varies rapidly between 1 and $-1$ (§3). **Derived**
4. Decreasing $\mathsf p$ acts like increasing $\epsilon_{\mathrm J}$; $\mathsf p=2$ approximates (40) with $\epsilon_{\mathrm J}^2=0.5$ on qualitative inspection (§3, §5.1, Fig. 6). **Stated**
5. In AENO, replacing (40) ($\epsilon_{\mathrm J}^2=0.5$) by (46) ($\mathsf p=2$) visibly reduces numerical diffusion and improves symmetry on the square wave at orders 7–10 (100 cells, $t=2000$) (§5.1, Fig. 8). **Shown**
6. AENO-C results on the square wave are similar for $\mathsf p=1,2,5$, somewhat more sensitive at orders 5 and 6 (§5.2, Fig. 9). **Shown**
7. AENO-C with $\mathsf p=1$ produced negative densities or pressures on the left-half Woodward–Colella problem, while $\mathsf p=2$ works; $\mathsf p=2$ is used throughout as "an excellent compromise" (§5.2). **Stated** (the other $\mathsf p$ runs are not shown)
8. No theoretical justification of the choice of $\mathsf p$ is given; it is left to future work (§5.2). **Stated**
9. ADER with AENO ($\epsilon_{\mathrm J}^2=0.5$) does not reach design order on the $\sin^4(\pi x)$ test at orders 4 and 5; at order 5 convergence is lost on the finest mesh ($L_1$ order $-0.63$ from 200 to 400 cells) (§6, Table 1). **Shown**
10. On the same test AENO also loses convergence on the finest mesh at orders 6 and 7 ($L_1$ orders $-3.25$ and $-0.25$, 200 → 400 cells; Table A.8), while §6 calls AENO's performance from sixth to tenth order "quite satisfactory". **Shown** (table) / **Stated** (text)
11. ADER-AENO-C reaches the theoretical order in $L_1$ and $L_2$ at all orders 2–10 except order 4 (still sub-optimal, $L_1$ order 2.78 at 400 cells), and nearly so in $L_\infty$ (§6, Table 2). **Shown**
12. In convergence rates AENO-C outperforms ENO and AENO and is outperformed only by WENO, whose degree-$m$ polynomial has spatial accuracy $2m+1$ (§6). **Shown**
13. WENO superconverges on coarse meshes, where spatial accuracy dominates temporal accuracy (e.g. ADER-10 $L_1$ order 14.13 from 32 to 64 cells; Table A.7). **Shown** (explanation **Stated**)
14. Efficiency (CPU time to $L_1=10^{-8}$, $\sin^4$ test, $t=100$): AENO-C is the most efficient of the four methods at all orders except 3 and 4, where WENO is; AENO's CPU time is anomalously high at orders 4 and 5 because the extrapolated data do not converge (§6, Fig. 10). **Shown**
15. On the Jiang–Shu composite wave to $t=2000$ (1000 periods, 222 223 steps, 200 cells), AENO-C keeps all four shapes without overshoots at orders 5–10, while WENO is prone to spurious oscillations near discontinuities and steep gradients (§6, Fig. 11). **Shown**
16. On Burgers' equation with source $\beta u^2$, ADER-AENO-C reaches the expected order at essentially all orders 2–10 in all norms (§7.1, Table 3). **Shown**
17. On the accelerating-shock generalized Riemann problem for Burgers' equation with source $e^{-u}$, ADER-9-AENO-C (800 cells, CFL 0.95) reproduces Fig. 10 of Demattè et al. (2019) (§7.1, Fig. 12). **Shown**
18. ENO-type reconstructions give a closed-form polynomial usable anywhere in the cell, an advantage over WENO for the space–time quadrature of source terms, since WENO linear weights at generic Gauss points are not trivial (§7.1). **Stated**
19. On the Euler density wave (66), ADER-AENO-C reaches the expected order at all orders 2–10 except order 4 (§7.2, Table 4). **Shown**
20. Euler efficiency (to $L_1=10^{-8}$, $t=10$): ENO is the least efficient; AENO-C beats AENO at every order and is almost as efficient as WENO up to order 7, less efficient beyond; the authors attribute this to the Cauchy–Kovalevskaya procedure (§7.2, Fig. 13). **Shown** (cause **Stated**, examined in §8)
21. Modified Sod (sonic rarefaction), orders 7–10: ADER-AENO oscillates significantly near the rarefaction tail, ADER-AENO-C does not; at orders 9 and 10 "the tail of the rarefaction appears slightly disconnected", which a CFL of about 0.75–0.8 cures (§7.2, Fig. 14). **Shown**
22. The full Woodward–Colella problem gives negative pressures with the high-order schemes, AENO-C included (near $t\approx0.028$, at the shock collision), so only its left half is run (§7.2). **Stated**
23. Left-half Woodward–Colella (200 cells, CFL 0.9, $t=0.012$): WENO at orders 5–6 oscillates strongly at the contact, WENO at orders 7–10 fails with negative pressures or densities for every CFL tried in $[0.2,0.9]$, AENO-C shows no visible spurious oscillations or relevant over- and undershoots (§7.2, Fig. 15). **Shown**
24. On the same problem sixth-order ADER-AENO-C is nearly twice as efficient as sixth-order ADER-WENO to reach $L_1=0.01$ (§7.2, Fig. 16). **Shown**
25. Toro–Titarev shock–turbulence interaction: AENO-C at orders 5–10 on 1000 cells captures the flow and the upstream acoustic disturbance, approaching the reference (WENO5 with RK3, 50 000 cells) as the order increases (§7.2, Figs. 17–18). **Shown**
26. Profiling (density wave, 200 cells, CFL 0.9, $t=5$, serial, one CPU): AENO-C reconstruction costs a fraction of WENO's at every order, order-10 AENO-C (4.36 s) less than order-7 WENO (16.02 s); the Cauchy–Kovalevskaya procedure takes 37 %, 59.6 %, 74.1 % and 85.2 % of the AENO-C run time at orders 7, 8, 9, 10, the reconstruction under 7 % at order 10 (§8, Table 5; hardware not stated). **Shown**
27. Generalized-Riemann-problem solvers that avoid the Cauchy–Kovalevskaya procedure (ADER-DET, ADER-TR) are therefore desirable at very high order (§8, §9). **Stated**
28. "To the best of our knowledge, this is the first study to investigate the Euler equations using non-linear ADER schemes of order 8 or higher" (§9). **Stated**
29. AENO-C shows occasional undershoots near discontinuities (e.g. order 6, Figs. 9 and 11) absent from AENO, attributed to retaining too much centred-stencil information; they decrease with resolution, and a WENO-type average of the two stencils is suggested as a remedy (§5.2, §9). **Shown** (cause and remedy **Stated**)
30. A dimension-by-dimension extension on Cartesian meshes is possible; extending the stencil selection to unstructured grids is "non-trivial and unclear" (§9). **Stated**

Also stated (§2.2): in the authors' experience the Dumbser–Käser WENO used in earlier ADER and
AENO work degrades beyond sixth order, so Jiang–Shu WENO with $q=2$ is used.

*(Compiler check, not in the sources.)* The properties of claim 3 follow by substitution:
$\mathcal J(1/\mathsf s)=e^{-\mathsf s^{-\mathsf p}}-e^{-\mathsf s^{\mathsf p}}=-\mathcal J(\mathsf s)$, and
$\mathcal J(1)=e^{-1}-e^{-1}=0$. The Table 5 percentages are consistent with the printed
times (e.g. $55.23/64.8=85.2\%$, $4.36/64.8=6.7\%$).

# Printed slips

- §2.2 calls the polynomial reconstructed on the extended stencil of $2m+1$ cells "the higher-degree polynomial of degree $2m+1$". *(Compiler check, not in the sources:)* $2m+1$ cell averages determine a polynomial of degree $2m$, of accuracy $2m+1$, as §6 states.
- Eq. (42): $\tilde a_0=\bar q_j-\frac1{\Delta x}\sum_{k=1}^{n}\dots$ for the cell $I_i$, with $j$ for $i$ and upper limit $n$ where the degree is $m$ in Eqs. (37)–(39); Eqs. (50)–(52) also use $n$.
- §2.3: "rapidly approaches 1 as $s\to0$ and $-1$ and $s\to\infty$" ("and" for "as").
- §7.2 announces convergence "on a sequence of five meshes" for test (66); the caption of Table 4 says four, and four meshes (16–128 cells) are printed.
- Efficiency on advection: §6 says AENO-C is the most efficient "except for the third and fourth orders", §7.2 recalls "the advection equation where AENO-C was more efficient than WENO at all orders except the fourth-order".
- Onset of the efficiency loss on Euler: §7.2 "Beyond the seventh-order", §8 "above the eighth-order".
- ADER-TR is cited as [10] (Demattè et al. 2019) in §8 and as [21] (Demattè 2017, Master's thesis) in §9.
- §6 calls AENO "quite satisfactory" from sixth to tenth order, while Table A.8 shows divergence on the finest mesh at ADER-6 ($L_1$ order $-3.25$, $L_\infty$ $-5.44$) and ADER-7 ($-0.25$).
- Captions: Table 3 "ADER with AENO-C with for Burgers' equation", Tables B.9 and B.10 "ADER with ENO with for", "ADER with WENO with for"; Fig. 11 calls the Jiang–Shu test "the Shu linear advection test".
- §7.2, Eq. (70): the Toro–Titarev test is called "a right-moving Mach 1.1 shock", with post-shock state $(\rho,v,p)=(1.515695,0.523346,1.805)$ running into $(1,0,1)$, $\gamma=1.4$. *(Compiler check, not in the sources: the Rankine–Hugoniot relations give $(1.169082,0.188239,1.245)$ for Mach 1.1 and $(1.515695,0.523346,1.805)$ for Mach 1.3; the printed state is that of a Mach 1.3 shock.)* [Chu et al. (2025a)](/sources/chu-2025.md) print the same state, with the density 1.51695, and also call it Mach 1.1.
- Eq. (66) writes $\partial_x\mathbf f(\mathbf u)$ where Eq. (61) uses $\mathbf f(\mathbf q)$.

# Notation map

| Yajaman et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf Q$, $\mathbf F(\mathbf Q)$, $\mathbf S(\mathbf Q)$ | $u$, $f(u)$, $S(u)$ | balance law |
| $\mathbf Q^n_i$ | $\bar u^n_i$ | cell average |
| $\mathbf F_{i+1/2}$, $\mathbf S_i$ | $\hat f_{i+1/2}$, averaged source (local) | time-averaged flux, space–time-averaged source |
| $\mathbf P_i(x)$, $m$ | reconstruction polynomial, degree $m$ (local) | ADER order $m+1$; $m$ is not the number of equations |
| $\mathbf J_{i+1/2}(t)$, $\mathbf G^{(k)}$, $\mathbf H^{(k)}$ | interface state, derivative Riemann solutions, Cauchy–Kovalevskaya functionals (local) | |
| $\mathbf A$ | $A$ | flux Jacobian |
| $\omega_k,\tau_k$; $\sigma_l,\xi_l$ | Gauss weights and points in time and space (local) | not WENO weights; $\xi_l$ not DG nodes |
| $\mathcal E_i$, $S^{(i)}_s$ | extended stencil, candidate stencil $S_k$ | source labels stencils by their left-most cell $s$ |
| $p^{(i)}_s$ | $u^{(k)}$ | candidate polynomial |
| $\lambda_s$ | $d_k$ | linear weights; **collision** with the eigenvalues $\lambda_l$ |
| $\beta_s$ | $\beta_k$ | Jiang–Shu form |
| $\alpha_s$, $\omega_s$, $\epsilon$ | $\alpha_k$, $\omega_k$, $\epsilon$ | agree |
| $r=2$ | $q=2$ | weight exponent; **collision**: registry $r$ is the stencil width |
| $a_{k,L}$, $a_{k,R}$, $a_{k,ENO}$, $a_{k,CENT}$, $\tilde a_k$ | $\mathsf c^{\mathrm L}_k$, $\mathsf c^{\mathrm R}_k$ (local Taylor coefficients; for AENO-C, L = ENO and R = centred), $\tilde{\mathsf c}_k$ | as on [AENO reconstruction](/methods/aeno-reconstruction.md) |
| $\omega(s)$ | $\mathcal J(\mathsf s)$ (local) | joining function; **collision** with the weights $\omega_k$ |
| $s$, TOL | $\mathsf s$ coefficient ratio, guard $10^{-6}$ (local) | $s$ is not the entropy |
| $\epsilon$ (AENO), $p$ | $\epsilon_{\mathrm J}$, $\mathsf p$ (local) | **collision** of $p$ with the pressure |
| $\rho$, $u$, $p$, $E$, $\epsilon$, $\gamma$ | $\rho$, $v$, $p$, $E$, $e$, $\gamma$ | $u$ velocity, $\epsilon$ specific internal energy |
| $C_{CFL}$ | $\nu$ | CFL number |
| $M$ | $N_x$ | number of cells; also the number of temporal Gauss points in Eq. (20) |
| $T_{out}$ | output time $t$ | |

# Reference list

The paper prints 28 references, numbered [1]–[28]. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `yajaman-2025`. Ref. [13] (Toro's
forthcoming book, "to appear", 2025) is kept as a pre-publication entry; ref. [21] is a 2017
Master's thesis; ref. [3] (ENO III) is printed as the 1997 J. Comput. Phys. reprint; ref. [15]
(AENO) is keyed by its printed year 2021. No item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23). This source is cited on:

* [ADER schemes](/methods/ader-scheme.md)
* [AENO and AENO-C reconstruction](/methods/aeno-reconstruction.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Generalized Riemann problem (GRP) solvers](/methods/generalized-riemann-problem.md)
* [Jiang–Shu composite-wave advection](/benchmarks/jiang-shu-composite-advection.md)
* [Low-dissipation central-upwind schemes](/methods/low-dissipation-central-upwind-scheme.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
