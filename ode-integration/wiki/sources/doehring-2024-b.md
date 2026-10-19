---
type: Source
title: "Doehring et al. (2024b) — Multirate Time-Integration based on Dynamic ODE Partitioning through Adaptively Refined Meshes for Compressible Fluid Dynamics"
description: "Applies paired explicit Runge–Kutta families to method-of-lines systems partitioned dynamically by quad/octree mesh refinement in Trixi.jl, shows that the families are never SSP and lose monotonicity at member interfaces, estimates spectrum boundaries by shifted Arnoldi, and reports speedups up to 2.4 over standalone schemes."
resource: "doi:10.1016/j.jcp.2024.113223"
source_kind: paper
authors: [Doehring D., Schlottke-Lakemper M., Gassner G.J., Torrilhon M.]
year: 2024
venue: "J. Comput. Phys. 514:113223"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Computational_Physics_Doehring_Multirate_time-integration_based_on_dynamic_ODE_partitioning.pdf"
tags: [multirate, runge-kutta, explicit, ssp, stability, method-of-lines]
timestamp: 2026-10-20T05:00:00Z
---

# Summary

The paper applies the second-order (Vermeire 2019) and third-order (Hedayati
Nasab & Vermeire 2022)
[paired explicit Runge–Kutta (P-ERK)](/methods/paired-explicit-runge-kutta.md)
families to method-of-lines systems **partitioned dynamically** by quad/octree
adaptive mesh refinement of a DGSEM discretization in
[Trixi.jl](/software/trixi-jl.md). Each cell is assigned by its minimum edge
length to a member of the family (shared $c$ and $b$, different numbers of active
stages $e_q$), and the assignment is recomputed after every mesh change. The
spatial code changes only in restricting its loops to index sets. The scheme is a
form of [local time stepping](/methods/local-time-stepping.md) without
interpolation or flux exchange.

After recalling partitioned Runge–Kutta theory, the paper analyses nonlinear
stability. Zero weights make every family non-SSP (see
[SSP methods](/methods/strong-stability-preserving-runge-kutta.md)). On
first-order upwind finite volumes for linear advection, the one-step matrix is
linearly stable but has negative entries at the interface between members, so
monotonicity is lost even on a uniform mesh. The relative total-variation
increase after one step grows with the refinement ratio, the step, the mesh
coarseness and the stage-count difference between members. The third-order
family is rebuilt on the Shu–Osher SSPRK(3,3) instead of an archetype with a
downwinding coefficient $-1$. For the
[optimal stability polynomials](/methods/optimal-stability-polynomial.md) the
paper estimates the spectrum boundary of large Jacobians by shifted Arnoldi
around the scaled convex hull of a coarse-mesh spectrum.

Conservation and convergence are validated on the
[isentropic vortex](/benchmarks/isentropic-vortex.md) with AMR. Three-member
third-order families are benchmarked against standalone optimized P-ERK, SSPRK33
and four optimized methods from OrdinaryDiffEq.jl on a shear layer, a
visco-resistive Orszag–Tang vortex, the 3D
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), the
[Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md), a
Rayleigh–Taylor instability and an MHD rotor. Speedups reach 2.4 (viscous) and
1.8 (inviscid); partitioning costs under 5 % of runtime and 7–34 % more memory.
Inviscid problems need a reduced CFL number (70 % for Kelvin–Helmholtz), and more
than three members do not pay.

# Version read

The file is the arXiv preprint arXiv:2403.05144v2 [math.NA], 27 June 2024
(footer: "Preprint submitted to Journal of Computational Physics, June 28,
2024"), 47 pages: main text pp. 1–37, Appendices A–B pp. 38–40, references
pp. 40–47, all read. It is not the version of record (JCP 514:113223); numbers
cited here are those of arXiv v2. Title and authors match Crossref. This is a
different paper from the ingested
[Doehring et al. (2024)](/sources/doehring-2024.md) on many-stage stabilized
methods, which it cites as ref. [64] in its arXiv form.

# Key claims

1. P-ERK schemes are partitioned Runge–Kutta methods; with shared $c$ and $b$ the partitioned order conditions for $p=1,2,3$ reduce to the classical ones with $b^\top A^{\{q\}}c=\frac16$ for every $q$; coupling conditions between the $A^{\{q\}}$ first appear at $p=4$ (§2.1, Eq. (2.3)). **Stated** (cited)
2. Linear stability of the partitioned scheme cannot in general be inferred from the members' stability polynomials (matrix-valued stability function (2.10)); in practice absolute stability of each member on its own spectrum suffices (§2.2). **Stated** (observed, cited)
3. Internal consistency, $\sum_ja^{\{q\}}_{ij}=c_i$ for all $i,q$, equals stage order one of all members and is needed to avoid spurious oscillations at partition interfaces (§2.3, Eq. (2.11)). **Stated** (cited)
4. Identical weights across partitions guarantee conservation of linear invariants for equation-based partitioning (§2.4, Eq. (2.12)). **Stated** (cited)
5. A partitioned method is SSP only if every member is, with step $h=\min_q\mathcal C_q h_{\mathrm{FE}}$ (§2.5, Eq. (2.13)). **Stated** (cited)
6. P-ERK families are never SSP: zero entries of the shared $b$ violate $b>0$ for the highest-stage member and all reduced members; the only possible exception is a base method whose evaluated stages coincide with the nonzero weights (§3.2). **Derived**
7. For first-order upwind finite volumes for $u_t+u_x=0$ on a uniform mesh of 64 cells with $e_q=16$ in $[-0.5,0.5]$ and 8 elsewhere, at the largest stable step $h=0.21875$, the one-step matrix $D$ has spectral radius below 1 but negative entries in rows 17–24, producing oscillations behind the upwind interface at $x=-0.5$ after one step; none appear at $x=0.5$ (§3.2.2–3.2.3, Figs. 2–3). **Shown**
8. The row sums of $D$ equal one (conservation) and the scheme converges at second order asymptotically despite the monotonicity loss (§3.2.3). **Shown**
9. The stage-evaluation pattern matters: "alternating" (3.12) and "early shared" (3.13) tableaux with the same polynomial $P_{2;4}$ give different one-step results; alternating gives the strongest oscillations, early shared the largest errors at the fine–coarse interface (§3.2.4, Fig. 4). **Shown**
10. On non-uniform meshes with refinement ratio $\alpha$ in $[-0.5,0.5]$ and $e$ chosen to keep the step, the relative total-variation increase after one step rises from $-0.03$ at $\alpha=1.125$ ($e=9$) to 26.0 at $\alpha=2$ ($e=16$) (Table 1). **Shown**
11. At $\alpha=2$ the total-variation increase falls with the step (26.0 at CFL 1.0, 4.04 at 0.8, 0.28 at 0.6, $-0.01$ at 0.4; Table 2), with base resolution (26.0 at 64 cells, 0.01 at 4096; Table 3), and with the stage counts ($\le0$ for $e_1=2,3,4$ with $e_2=2e_1$, 26.0 for $e_1=8$; Table 4). **Shown**
12. Since the cell averages themselves are corrupted, conventional (MUSCL-type, positivity) limiters cannot repair the monotonicity loss; flux or stage limiting would be needed (§3.2.5). **Stated**
13. Earlier oscillation-free P-ERK results are explained by small neighbour refinement ratios (SD7003 mesh average $\bar\alpha\approx1.15$), stage-count differences $\le4$, diffusive equations, and, in a random-member convergence test, the step reduction forced by the smallest member (§3.2.6). **Derived** / **Stated**
14. The third-order family uses the Shu–Osher SSPRK(3,3) ($c=(0,1,\frac12)$, $b=(\frac16,\frac16,\frac23)$) as base instead of the archetype with $a_{31}=-1$, whose negative entry downwinds the fluxes of the first stage; using the first stage in the final update costs no extra storage, and each stage still costs two scalar–vector multiplications and one vector addition (§3.3, Eqs. (3.15)–(3.16)). **Stated**
15. With linear free abscissae and positivity constraints on $a_{i,i-1}$ and $a_{i1}=c_i-a_{i,i-1}$, positive Butcher coefficients were found for every optimized polynomial of the paper, though not guaranteed in general (§3.3, §4.3.2). **Shown**
16. Spectrum-boundary estimation: full spectrum of a reduced-resolution semi-discretization, its densified convex hull scaled by the mesh ratio, then shifted Arnoldi (ARPACK) around each hull point on the sparse full Jacobian. For a Kelvin–Helmholtz DGSEM case the reduced $1024\times1024$ eigendecomposition takes 0.4 s, the full $16384\times16384$ one over 11 minutes, and 20 shifted Arnoldi runs about 30 s in total for 930 eigenvalues that capture the shape (§4.1, Fig. 5). **Shown**
17. The Ketcheson–Ahmadia optimizer handles monomial-basis polynomials up to degree about 16 and up to about 2000 eigenvalue constraints in under a minute; degrees above 100 need the root-based approach of [Doehring et al. (2024)](/sources/doehring-2024.md) (§4.2). **Stated**
18. With refinement ratio 2 the stage counts would have to double per level, $e_q=e_1\cdot\{1,2,4,8,\dots\}$; since the monotonicity loss grows with the stage-count difference, only few-member families are used (§4.2). **Derived**
19. Second-order coefficients follow sequentially from the optimized monomial coefficients, $a_{s-i}=\frac{\theta_{3+i}}{c_{s-i-1}}\prod_{j=0}^{i-1}\frac1{a_{s-j}}$ with $a_i:=a_{i,i-1}$; third order needs a nonlinear solve (trust region, random starts) with the constraint $\frac16=b_sa_s+b_{s-1}a_{s-1}$ (§4.3, Eqs. (4.4)–(4.7)). **Derived**
20. On the isentropic vortex with two AMR levels the families P-ERK$_{2;\{3,6,12\}}$ and P-ERK$_{3;\{4,8,16\}}$ give density errors of the size of each standalone member ($L^1/\lvert\Omega\rvert$: $2.09\cdot10^{-5}$ against $1.74$–$1.77\cdot10^{-5}$ at $p=2$; $3.73\cdot10^{-7}$ against $4.05\cdot10^{-7}$ at $p=3$), and orders 2 and 3 are observed until the spatial error dominates, with no order reduction at interfaces (§5, Table 5, Fig. 6). **Shown**
21. Conservation errors of P-ERK$_{3;\{4,8,16\}}$ match SSPRK33 (mass $3.94\cdot10^{-13}$ against $7.82\cdot10^{-13}$, energy $1.06\cdot10^{-12}$ against $3.64\cdot10^{-12}$) (Table 6). **Shown**
22. Partitioning overhead is 2.5 % (shear layer), 1.0 % (Orszag–Tang), 0.3 % (Taylor–Green), 0.4 % (Kelvin–Helmholtz), 4.4 % (Rayleigh–Taylor, p4est mesh needing edge lengths) and 0.8 % (rotor) of runtime; memory overhead 20 %, 28 %, 7 %, 23 %, 34 %, 11 % (§7). **Shown**
23. No extra MPI communication is needed relative to a standard Runge–Kutta method (§6.3). **Stated** (no distributed runs shown)
24. Three-member families with relative CFL numbers $\{1,2,4\}$ are the most efficient in every example; more members need CFL reduction (§7). **Shown** (data for more members not tabulated)
25. Hyperbolic–parabolic problems run at the CFL number of the standalone optimized P-ERK; inviscid ones need reduction: 70 % for Kelvin–Helmholtz, 96 % for Rayleigh–Taylor, "not significantly reduced" for the rotor (§7.1, §7.2). **Shown**
26. Shear layer: P-ERK$_{3;\{3,4,7\}}$ is fastest; runtime ratios against it are 1.468 (P-ERK$_{3;7}$), 2.356 (SSPRK33), 1.412 (DGLDD3;7), 1.854 (PKD3S3;5), 2.171 (RDPKFSAL3;5), 2.350 (CKLLS3;4); the standalone P-ERK needs 76.2 % more evaluations but is only 46.8 % slower, because Trixi.jl is memory-bound and partitioning loses data locality (Table 7, §7.1.1). **Shown**
27. Orszag–Tang: ratios 1.248 (P-ERK$_{3;6}$), 2.005 (SSPRK33), 1.575, 1.717, 1.649; the family is 1.718 times slower than a hypothetical optimal family (Table 8). Taylor–Green: P-ERK$_{3;6}$ only 1.068 slower, since most cells are refined (Table 9). **Shown**
28. Kelvin–Helmholtz: P-ERK$_{3;\{4,6,11\}}$ is fastest; ratios 1.311 (P-ERK$_{3;11}$), 1.426 (SSPRK33), 1.169 (DGLDD3;7), 1.866, 1.659; DGLDD3;7 beats the standalone optimized P-ERK, attributed to its low dissipation and dispersion, and runtime is not proportional to the evaluation count because P-ERK triggers subcell shock capturing on more cells (Table 10, §7.2.1). **Shown**
29. Rayleigh–Taylor: ratios 1.126 (P-ERK$_{3;4}$), 1.205 (SSPRK33), 1.751, 1.402, 1.292, with AMR fixed costs about 23 % of runtime (Table 11); MHD rotor: 1.097, 1.492, 1.148, 1.195, 1.192 (Table 12). **Shown**
30. On a smoothly refined structured mesh (Euler, no shock capturing) second-order families keep the stage-normalized CFL number at 0.93–0.97, and the speedup over SSPRK33 grows from 1.26 ($e_{\max}=4$) to 2.45 ($e_{\max}=16$): P-ERK works without stabilization when mesh and method discontinuities do not coincide (App. A, Table A.13). **Shown**
31. The speedup per step increase matches Hedayati Nasab & Vermeire (about 4.3 for an 8× step against SSPRK33; here 2.356 for a 4× step) (§7.1.1–7.1.2). **Derived** (comparison)

# Printed slips

- Eq. (3.4), row 6 of $A^{(2)}$: entries printed "$5/10-a^{(2)}_{6,4}$ … $a^{(2)}_{6,4}$" where the subdiagonal structure requires $a^{(2)}_{6,5}$ (p. 8).
- Eq. (4.4): the last term is printed "$c_{S-E+2}z^{S-E+2}\prod_{i=S-E+3}^Sa_i$"; the power must be $z^E$.
- Eq. (4.6): the last term "$c_2b_Sa_S\prod_{j=1}^{i}a_{S-j}z^S$" uses the summation index $i$ outside the sum.
- §3.2.3: the intermediate state "$U_n+\Delta t\sum_{i=1}^S\sum_{r=1}^Rb_i^{(r)}K_i^{(r)}$ (cf. (2.2b))"; (2.2b) has $a^{(r)}_{i,j}$.
- §3.2.5: "$N^{(1)}=64$ to $N^{(1)}=4095$" against 4096 in Table 3, and "cell size $\Delta x^{(1)}=64$" where $2/64$ is meant.
- Table 5 caption "from $\Delta x^{(1)}=10/64$ to $\Delta x^{(3)}=2/256$" against $h=10/256$ in §5.
- The stage-count difference "grows exponentially" with the levels (§3.2.6, §4.2) but "scales quadratically with the number of levels" (App. A, p. 40).
- The Fig. 4 caption speaks of "two different 6-12 P-ERK schemes", while three patterns are plotted.
- §7.2.1: the optimality ratio $\kappa=92.4\,\%$ (Table 10) implies 1.082, but the text says the family is "1.035 of the optimal one"; the other cases are consistent.
- Tables 7, 8, 9 and 11 captions write "$S=\{\dots\}$" for the stage-evaluation sets $E=\{\dots\}$.
- App. B, p. 40: the rotor taper $f(r)=\frac{r_1-r}{r_1}$ gives $f(r_0)\approx0.13$; the usual taper $\frac{r_1-r}{r_1-r_0}$ gives $f(r_0)=1$.
- Conclusions give "1.8" for the inviscid speedup; Table 10's largest is 1.866.
- Ref. [37] prints "G. Wanner, E. Hairer" and "volume 375"; ref. [47] prints year 2013 with a DOI encoding 2012.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U'=F(t,U)$, $U_n$ | $y'=f(t,y)$, $y_n$ | semi-discrete system |
| $U^{(r)}$, $F^{(r)}$ | $y^{\{q\}}$, $f^{\{q\}}$ | partition $r$; registry partition index $q$ |
| $R$ | — | number of partitions (family members); **collision** with the stability function $R(z)$ |
| $L$ | — | number of AMR levels; **collision** with the registry linear operator $L$, which the source also uses for the upwind matrix (3.7b) |
| $S$, $\Delta t$ | $s$, $h$ | stages, step |
| $E$, $E^{(r)}$, $\Delta E$ | $e$, $e_q$, — | active stages (degree of the member's polynomial), as on the P-ERK page; stage-count difference |
| $K_i^{(r)}$ | $f^{\{q\}}(Y_i)$ | stage derivatives translated to stage values |
| $A^{(r)}$, $a^{(r)}_{i,j}$, $a_i$ | $A^{\{q\}}$, $a^{\{q\}}_{ij}$, $a_{i,i-1}$ | member Butcher matrices |
| $b$, $c$ | $b$, $c$ | shared weights and abscissae, agree |
| $P_{p;E}(z)$ | $P(z)$ | stability polynomial of order $p$, degree $e$ |
| $\alpha_i$ | $\theta_i$ | monomial coefficients beyond order $p$; **collision** with the refinement ratio $\alpha$ |
| $P(Z)$, $I^{(r)}$ | — | matrix-valued stability function and mask matrices of the partitioned test equation |
| $J$, $\sigma$, $\tilde\sigma$ | $J$, — | Jacobian; full and reduced spectra; **collision**: $\sigma$ is the registry tree symmetry |
| $\tilde\mu_k$, $\mu_k$ | — | convex-hull points and Arnoldi shifts |
| $c^{SSP}_r$, $\Delta t_{FE}$ | $\mathcal C_q$, $h_{\mathrm{FE}}$ | SSP coefficient (radius of absolute monotonicity), forward-Euler step |
| $D$, $e_{TV}$ | — | one-step matrix and relative total-variation increase |
| $\beta$, $\rho_i$, $k$, $N_D$ | — | local characteristic time (3.1), directional spectral radius, DG degree, dimension |
| CFL | — | factor of the step bound $h\le\mathrm{CFL}\cdot\beta$, not the Courant number $\nu$ |
| $\kappa$ | — | optimality ratio $\tau_{Opt}/\tau$; also a shear-layer parameter |
| P-ERK$_{p;\{E^{(1)},\dots,E^{(R)}\}}$ | — | family label |

# Reference list

The paper prints 100 references in numbered style ([1]–[100]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` this
slug. [2] prints the first author as "S. H. Nasab" and is the bundle's
[Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md); [64] is the
arXiv preprint (arXiv:2402.12140) of the ingested
[Doehring et al. (2024)](/sources/doehring-2024.md) and stays a separate preprint
entry, `doehring-2024-e`; [27] is the paper's own reproducibility repository
(2024), keyed `doehring-2024-d` so that it collides with neither ingested
Doehring 2024 slug;
[30] (Griepentrog 1978) has no volume; [79] has no pages; [29] and [31] print
their DOI also as a spurious "arXiv:" field; [66] is an arXiv preprint; [37] and
[47] carry the slips listed above. All items parsed.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [Local time stepping](/methods/local-time-stepping.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Paired explicit Runge–Kutta (P-ERK) methods](/methods/paired-explicit-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Trixi.jl](/software/trixi-jl.md)
