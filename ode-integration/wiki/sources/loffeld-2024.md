---
type: Source
title: "Loffeld et al. (2024) — Performance of explicit and IMEX MRI multirate methods on complex reactive flow problems within modern parallel adaptive structured grid frameworks"
description: "Performance study in SUNDIALS/ARKODE: explicit MRI methods beat spectral and multirate spectral deferred correction on a 3D methane flame, and IMEX-MRI-GARK methods beat single-rate ARK-IMEX on a stiff-diffusion reacting problem in AMReX, with multigrid-preconditioned implicit stages and gains compounding with AMR."
resource: "doi:10.1177/10943420241227914"
source_kind: paper
authors: [Loffeld J.J., Nonaka A., Reynolds D.R., Gardner D.J., Woodward C.S.]
year: 2024
venue: "Int. J. High Perform. Comput. Appl. 38:263-281"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_The_International_Journal_of_High_Performance_Computing_Appl_Loffeld_Performance_of_explicit_and_IMEX_MRI_multirate_methods_on_co.pdf"
tags: [multirate, imex, hpc, software, implicit-stage-solvers, cfd]
timestamp: 2026-10-19T19:14:00Z
---

# Summary

The paper is a performance study: it introduces no integrator and proves
nothing. It compares
[multirate infinitesimal (MRI) methods](/methods/multirate-infinitesimal-methods.md)
implemented in the MRIStep module of [ARKODE](/software/arkode.md) against spectral
[deferred correction](/methods/deferred-correction.md) (SDC), multirate SDC
(MRSDC) and single-rate ARK-IMEX, on two reacting-flow problems discretized on
block-structured grids (BoxLib and AMReX), on LLNL's Quartz cluster with pure MPI.

Problem 1 is the 3D premixed methane flame of Emmett et al. (2014): reacting
compressible Navier–Stokes with GRI-Mech 3.0 (53 species, 325 reactions),
eighth-order compact finite differences, $32^3$ cells. Chemistry is the fast part
and transport the slow part. An explicit third-order MRI method with the
Knoth–Wolke slow method (an MIS-type scheme) and fast explicit methods of orders
2–5 is compared with fourth-order SDC, MRSDC-338 and MRSDC-352 at constant steps.
The MRI methods reach their asymptotic regime at larger steps and give smaller
error per wall-clock second except at the smallest steps, where MRSDC-352 is
comparable; MRSDC converges non-monotonically and MRSDC-338 stagnates near
$2\times10^{-6}$. At $H=6.25\times10^{-8}$ s the MRI runs take 173–274 s against
376 s and 833 s for the MRSDC methods, because they need fewer slow and fast
evaluations.

Problem 2 is an advection–diffusion–reaction model for the mass fractions with
diffusion artificially stiffened by a factor 1000, $128^3$ cells, 512 ranks, split
three ways: chemistry fast, advection slow explicit, diffusion slow implicit.
[IMEX-MRI-GARK](/methods/imex-mri-gark.md) 3b and 4 with ten fast steps per slow
step beat the single-rate fourth-order ARK-IMEX of Kennedy & Carpenter (2003).
The [implicit stages](/methods/implicit-stage-solvers.md) use Newton with
matrix-free GMRES; AMReX geometric multigrid preconditioning pays off from 128
cells per side and becomes critical at 256 with stiffer diffusion. A two-level
AMR test shows multirate and spatial refinement gains compounding (about 18×).
Classical [splittings](/methods/operator-splitting.md) are discussed as the
order-limited alternative.

# Version read

The file is the arXiv preprint arXiv:2211.03293v1 [math.NA], 7 November 2022, in
the SAGE template with placeholder header "Journal Title XX(X):1–14" and the
placeholder DOI "10.1177/ToBeAssigned", 14 pages, all read; figures and tables
were checked visually. It is not the version of record (IJHPCA 38:263–281);
differences could not be checked, and page, equation and table numbers cited
here are those of the preprint. Title and authors match Crossref.

# Key claims

1. Single-rate implicit methods can be prohibitively expensive for multiscale problems because of large monolithic algebraic solves; single-rate explicit methods can be infeasible because the fastest process sets the stability limit (§1). **Stated**
2. Classical splitting (Lie–Trotter, Strang–Marchuk) with subcycling is limited to orders 1 and 2 and can lack stability and accuracy; higher-order splittings typically need backward-in-time substeps (§2). **Stated**
3. Lie–Trotter and Strang–Marchuk can be viewed as infinitesimal formulations with zero forcing, giving $O(H)$ and $O(H^2)$ accuracy (§2.1). **Stated**
4. MIS methods treat $f^{\{\mathrm s\}}$ explicitly and reach $O(H^3)$; MRI-GARK treats it explicitly or solve-decoupled implicitly, up to $O(H^4)$; IMEX-MRI-GARK splits $f^{\{\mathrm s\}}=f^{\mathrm I}+f^{\mathrm E}$, up to $O(H^4)$ (§2.1). **Stated**
5. Implicit infinitesimal methods allow implicit dependence on $Y_i$ only at stages with $\Delta c_i=0$ ("solve-decoupled"): stages alternate between a diagonally implicit slow solve and a modified fast problem (§2.1). **Stated**
6. MRI methods are "currently" limited to fourth order, while SDC has "ostensibly no upper bound" on its order (§2.2). **Stated**
7. SDC iterates over the step, so its cost tends to exceed that of MRI methods of the same order, which pass through their stages "in one shot" (§2.2). **Stated**, then **Shown** in §5
8. Each SDC sweep with forward or backward Euler raises the order by one, up to the quadrature order (§2.2). **Stated** (Dutt et al. 2000)
9. MRSDC-XYZ has $X+(X-1)(Z-1)+(X-1)(Y-2)Z$ fine nodes (§2.2). **Stated** (consistent with Fig. 1)
10. On the methane flame the largest stable steps are: SDC $\le6.25\times10^{-8}$ s, MRSDC-338 $2.0\times10^{-6}$, MRSDC-352 $2.5\times10^{-7}$, MRI-2(8) $5.0\times10^{-7}$, MRI-3(4) $1.0\times10^{-6}$, MRI-4(8) $5.0\times10^{-7}$, MRI-5(4) $2.5\times10^{-7}$ s; the single-rate $O(10^{-8})$ limit agrees with the eigenvalues of the chemistry Jacobian (§5.2, Table 1). **Shown**
11. After "exhaustive testing" the best multirate ratios are MRI-2(8), MRI-3(4), MRI-4(8), MRI-5(4) (fast order, $m$ fast steps per slow step) (§5.1). **Shown**
12. MRSDC converges "highly non-monotonic[ally]" despite its theoretical fourth order: MRSDC-338 rates 2.72, 3.28, 2.51, 2.07, 1.69, 0.77, 0.08, its error stalling near $2\times10^{-6}$; MRSDC-352 rates 7.17, 4.02, 8.98, 1.24; smaller steps or more iterations might cure it (§5.2, Fig. 3, Table 1). **Shown**
13. MRI-4 and MRI-5 are asymptotically third order, limited by the slow method, but their slopes exceed four where the reactions dominate the error; MRI-2 is asymptotically second order but its slope is at least three over the tested range (§5.2). **Shown**
14. The MRI methods reach their asymptotic range at larger steps than MRSDC (§5.2). **Shown**
15. Rates are very similar in $L_2$ and $L_\infty$ and insensitive to the solution component (§5.2). **Shown** (asserted; other norms not printed)
16. MRSDC has a significant advantage over single-rate SDC, confirming Emmett et al. (2014) (Fig. 4). **Shown**
17. MRI methods generally give smaller error at given wall-clock time than the SDC methods; at the smallest steps MRSDC-352 with four iterations is comparable (Fig. 4). **Shown**
18. At $H=6.25\times10^{-8}$ s (32 steps), slow/fast evaluations, runtime and density error: MRSDC-338 129/7169, 833 s, $3.62\times10^{-6}$; MRSDC-352 257/2049, 376 s, $2.12\times10^{-6}$; MRI-2(8) 97/993, 176 s, $9.06\times10^{-7}$; MRI-3(4) 97/929, 173 s, $4.31\times10^{-6}$; MRI-4(8) 97/1857, 274 s, $4.61\times10^{-7}$; MRI-5(4) 97/1345, 216 s, $1.15\times10^{-6}$ (Table 2). **Shown**
19. On the stiff-diffusion AMReX problem the IMEX-MRI methods have a "significant performance advantage" over single-rate ARK-IMEX, and a ratio $m=10$ was the best of those tried (§6.2, Fig. 5). **Shown**
20. The multirate methods needed tighter algebraic-solver tolerances than ARK-IMEX at the same coarse step, attributed to their higher accuracy at those steps (§6.2, Tables 3–4). **Shown** (cause **Stated** as "seems to be")
21. Solver tolerances were chosen by sweeping $10^{-1}$ to $10^{-15}$ and taking the loosest one that changes the H2 and H mass-fraction errors by less than a factor 0.01; used as absolute tolerance in the WRMS norm (nonlinear) and 2-norm (linear), with safety factors 0.1 and 0.05 and at most 10 nonlinear and 100 linear iterations (§6.1). **Shown** (procedure)
22. IMEX-MRI3-10 over 8 steps, unpreconditioned, at 32/64/128/256 cells per side on 8/64/512/4096 ranks: 35.6/46.5/69.0/129.1 s, 48/48/48/72 nonlinear and 119/142/209/1150 linear iterations; the cost grows slowly because evaluating the diffusion coefficients, not the linear solve, dominates (Table 5). **Shown**
23. With AMReX MLABecLaplacian multigrid preconditioning: 45.92/64.45/66.63/112.1 s and 48/48/48/60 linear iterations; preconditioning is a net loss at 32 and 64 cells per side and a gain from 128 (Table 6). **Shown**
24. With diffusion scaled by $10^4$: unpreconditioned 40.9/64.6/102.8/853.6 s with 241/439/875/4796 linear iterations (Table 7), preconditioned 48.0/68.8/82.3/145.8 s with 48/48/48/72 (Table 8): preconditioning becomes critical at 256 cells per side. **Shown**
25. Two-level AMR compounds with multirate: wall times (units not printed) ARK-IMEX 8582 (one level), 2363 (two levels); IMEX-MRI4-10 1507 and 478; effective resolution $256^3$, fine level about 5 % of the volume (§6.3, Table 9). **Shown**
26. In this AMR test the steps are set by the accuracy of chemistry and diffusion, not by a CFL limit; all levels share the same steps, without level subcycling (§6.3). **Stated**
27. The MRI methods "match the accuracy of SDC and MRSDC methods while giving higher efficiency in most accuracy regimes", and multirate beats single-rate on block-structured mesh problems (§7). **Shown** (summary of §§5–6)
28. Adaptive step control would further improve multirate efficiency and remove manual step tuning; work in progress (§7). **Stated**

# Printed slips

- Eq. (4), p. 5: "$f^S(t_p.y_p^k)$", "$f^F(t_q.y_q^k)$", and in the text "$f^F(t_{q+1}.y^k_{q+1})$": periods for commas.
- Eq. (4) has $S_S^{k,q}$; the next sentence calls it "$S_C^{k,q}$".
- Eq. (9), p. 5, prints the advection term "$+\nabla\cdot(Y_k\mathbf u)$", Eq. (5b) has $-\nabla\cdot(\rho Y_k\mathbf u)$, and §3.2 repeats $f^E=\nabla\cdot(Y_k\mathbf u)$.
- Eq. (9) has the reaction term $\dot\omega_kW_k/\rho$; §3.2, p. 6, writes "$f^F=\dot\omega_k\rho W_k$".
- Table 1: MRI-3(4) at $H=5.0\times10^{-7}$ prints rate 4.48, but $\log_2(5.50\times10^{-3}/2.17\times10^{-4})=4.66$; MRI-2(8) at $H=6.25\times10^{-8}$ prints 5.89, but $\log_2(4.07\times10^{-5}/9.06\times10^{-7})=5.49$.
- Table 3, p. 10: ARK-IMEX steps $1.0\times10^{-7}$, $5.0\times10^{-8}$, $2.5\times10^{-9}$, $1.25\times10^{-9}$, $6.25\times10^{-10}$; the factor-20 jump breaks the halving pattern. §6.1 calls the reference step $10^{-10}$ "an order of magnitude smaller than the smallest fast step size", which the printed $6.25\times10^{-10}$ contradicts.
- §3.2 says MRI3 needs "four evaluations of $f^S$" per slow step, while Table 2 counts 97 slow evaluations over 32 steps ($3\cdot32+1$).
- §3.2 describes MRSDC-352 with four iterations only; Fig. 4 also plots "MRSDC352 (2 iters)".
- §5.2: "The error for the MRI approaches is comparable to or smaller than the SDC approaches"; Table 2's MRI-3(4) error $4.31\times10^{-6}$ exceeds both MRSDC errors.
- §5.1 "where is P the order"; §4.1 labels two items "(d)"; the reference to Schlegel (2011) prints "Halle-Wittenbergk".
- Table 9 prints no time unit; the model is said to hold "velocity, density, pressure and diffusion coefficients constant", but §6.1 computes the diffusion coefficients from the state (not updated within the solves).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y\in\mathbb R^N$ | $y\in\mathbb R^d$ | state |
| $f^F$, $f^S$ | $f^{\{\mathrm f\}}$, $f^{\{\mathrm s\}}$ | fast and slow parts, non-autonomous |
| $f^I$, $f^E$ | $f^{\mathrm I}$, $f^{\mathrm E}$ | slow implicit and explicit parts |
| $H$, $h$ | $H$, $h$ | slow and fast steps, agree |
| $s$, $c_i$, $Y_i$, $\Delta c_i$ | $s$, $c_i$, $Y_i$, $\Delta c_i$ | stages, abscissae, stage values, abscissa increments, agree |
| $T_i$, $v(\theta)$, $r_i(\theta)$ | — | stage times, fast solution, forcing polynomial (coefficients not printed); page-local |
| MRI-$P$($k$) | — | Knoth–Wolke slow method with fast explicit method of order $P$ and $m=k$ fast steps per slow step |
| IMEX-MRI3-10, IMEX-MRI4-10 | — | IMEX-MRI-GARK3b and 4 with $m=10$ |
| MRSDC-XYZ | — | $X$ coarse nodes, a $Y$-node fine quadrature applied $Z$ times per coarse subinterval |
| $t_p$, $t_q$, $H_q$ | $t_{n,m}$ | coarse and fine SDC nodes and fine spacing; **collision**: $H_q$ is not the macro step |
| $k$ (superscript) | — | SDC iteration index; **collision**: also species index and the fast-step count of MRI-$P$($k$) |
| $Y_k$ | — | mass fraction of species $k$; **collision** with the stage values $Y_i$ |
| $\eta$, $\lambda$ | — | shear viscosity and thermal conductivity; **collision** with the registry entropy $\eta$ and eigenvalue $\lambda$ |
| $\alpha$, $\beta$, $\phi$, $R$ (Eq. 10) | — | coefficients, unknown and right side of the multigrid operator $(\alpha I-\nabla\cdot\beta\nabla)\phi=R$ |
| "order" | $p$ | empirical rate $\log_2$ of error ratios under step halving |

# Reference list

The paper prints 52 references in author–year (SAGE) style, alphabetical. The
list is merged complete into the [bibliography](/bibliography.md), with
`citedby` this slug. Reynolds et al. (2022), the ARKODE paper, is printed as an
arXiv DOI with no venue and enters as a preprint entry, `reynolds-2022-c`, distinct from the
ingested [Reynolds et al. (2023)](/sources/reynolds-2023.md); Zhang et al. (2020),
AMReX, is printed "To appear"; xSDK (2020) is a web page; Frenklach et al. (1995)
(GRI-Mech) and Kee et al. (1998) (PREMIX) are a report and a user manual; Huang et
al. (2020) has an article number and no volume; Wartha et al. (2020) has no
volume or pages; Chen et al. (2009) is printed with "et al.". All items parsed.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [ARKODE](/software/arkode.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [IMEX multirate infinitesimal GARK methods](/methods/imex-mri-gark.md)
* [Multirate infinitesimal methods (MIS, MRI-GARK)](/methods/multirate-infinitesimal-methods.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
