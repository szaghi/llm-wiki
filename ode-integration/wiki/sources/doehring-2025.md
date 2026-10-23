---
type: Source
title: "Doehring et al. (2025) — Fourth-Order Paired-Explicit Runge-Kutta Methods"
description: "Extends paired explicit Runge–Kutta (P-ERK) families to fourth order by sharing the last three subdiagonal entries across members so that the partitioned coupling condition holds by construction, optimizes the constrained stability polynomials with an arbitrary-precision SOCP, and cuts runtime by 1.35–3.86 against optimized standalone methods in Trixi.jl."
resource: "doi:10.1007/s44207-025-00005-4"
source_kind: paper
authors: [Doehring D., Christmann L., Schlottke-Lakemper M., Gassner G.J., Torrilhon M.]
year: 2025
venue: "Comput. Sci. Eng. 2:1"
local_file: "/home/stefano/papers/mosaic/ode-integration/2025_Crossref_Computational_Science_and_Engineering_Doehring_Fourth-order_paired-explicit_Runge-Kutta_methods.pdf"
tags: [runge-kutta, explicit, multirate, order-conditions, stability, method-of-lines]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

[Paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md)
(P-ERK) methods are partitioned explicit Runge–Kutta methods: each
partition of a method-of-lines system, grouped by cell size or wave
speed, uses a member with its own number $e$ of active stages and its own
optimized stability polynomial, while all members share $c$ and $b$. This
gives a multirate effect with one global step $h$ and no change to the
spatial code. Second- and third-order families existed; this paper builds
the fourth-order one.

With shared $c$ and $b$ the partitioned
[order conditions](/results/runge-kutta-order-conditions.md) reduce to the
classical ones up to order 3, but order 4 adds the coupling condition
$b^\top A^{\{r_1\}}A^{\{r_2\}}c=1/24$ for all member pairs. Keeping the P-ERK
sparsity (first column and subdiagonal of $A$, only $b_{s-1},b_s$ nonzero),
the authors satisfy it by sharing the last three subdiagonal entries across
members. The result is a one-parameter family with $b_{s-1}=b_s=1/2$ and
$c_{s-1},c_s$ the two-point Gauss nodes; a fourth-order P-ERK needs at
least five stages, and each member keeps only $e-5$ free coefficients. The
stability polynomial is reparametrized linearly in products of subdiagonal
entries, so the Ketcheson–Ahmadia
[convex optimization](/methods/optimal-stability-polynomial.md) still
applies; the constrained optimum reaches about 85 % ($e=6$) to 96.5 %
($e=16$) of the unconstrained fourth-order step. The free abscissa is set
to 1 to reduce [internal error amplification](/definitions/internal-stability.md),
which grows exponentially with $e$.

DGSEM tests in Trixi.jl check linear stability of a two-level scheme,
error parity with standalone members, round-off-level conservation and
fourth-order convergence on the [isentropic vortex](/benchmarks/isentropic-vortex.md)
and on Lotka–Volterra. On 3D linearized Euler, an AMR isentropic vortex,
the laminar SD7003 airfoil and a coupled Euler–acoustic vortex pair,
multirate P-ERK cuts runtime by 1.35–3.86 and right-hand-side
evaluations by 1.38–4.26 against optimized standalone fourth-order
methods. Runtime gains stay below the evaluation gains because the code is
memory-bound and partitioning loses data locality.

# Version read

The file is an authors' preprint dated 10 August 2024 (page-1 footer
"Preprint submitted to – … August 10, 2024", elsarticle layout), 39 pages,
all read; it is neither the version of record nor the Research Square
posting (doi:10.21203/rs.3.rs-5259801/v1, which the archive's Crossref
lookup returned and which carries a Research Square header and a later
date). No arXiv identifier is printed; the compiler's identification with
arXiv:2408.05470v1 is unverified. The Code Availability section promises a
reproducibility repository "in a later version of this article". Title and
authors match the version of record (Comput. Sci. Eng. 2:1, 2025); its
differences from this preprint are unknown. Equation, table and section
numbers cited here are those of the preprint.

# Key claims

1. For partitioned Runge–Kutta methods with shared abscissae $c$ and weights $b$, the order conditions for $p=1,2,3$ reduce to the classical ones, with $b^\top A^{\{r\}}c=1/6$ required for every member $r$ separately (§2.1, Eq. 2.3). **Stated**
2. At $p=4$, even with shared $c$ and $b$, the coupling conditions $b^\top A^{\{r_1\}}A^{\{r_2\}}c=1/24$ for all $r_1,r_2$ arise (Eq. 2.4d), besides the per-member conditions (2.4a–c) (§2.1). **Stated**
3. Linear stability of a partitioned method cannot in general be inferred from the members' stability functions (matrix-valued stability function, Eq. 2.12); in practice absolute stability of each member for its own spectrum is "observed" to suffice (§2.2). **Stated** (checked on one example in §5.1, **Shown**)
4. Internal consistency $\sum_{j=1}^{i-1}a^{\{r\}}_{ij}=c_i$ for all $i,r$ (Eq. 2.13) is equivalent to stage order one of every member and is required to avoid spurious oscillations at partition interfaces (§2.3). **Stated**
5. Equal weights across partitions (Eq. 2.14) guarantee conservation of linear invariants for equation-based partitioning; for flux-based partitioning this can be relaxed (§2.4). **Stated**
6. An SSP partitioned method needs every member to be SSP, and its nonlinearly stable step is $h=\min_r\mathcal C_r\,h_{\mathrm{FE}}$ (Eq. 2.15), which makes SSP-capable partitioned methods "in many cases ineffective" (§2.5). **Stated**
7. The maximum stable step of optimized explicit methods grows asymptotically linearly in $e$ for hyperbolic spectra, so a $2e$-evaluation method on cells of size $\Delta x/2$ allows the same $h$ as an $e$-evaluation method on cells of size $\Delta x$; this is what makes P-ERK effective, and it fails for diffusion-dominated spectra, where RKC-type methods are needed (§3.1, Eqs. 3.2–3.4). **Stated**
8. Second- and third-order P-ERK are low-storage (two stages stored), have constant per-stage cost and sparse $A$, $b$ that simplify computing $a_{ij}$ from an optimized polynomial (§3.1). **Stated**
9. With $b=(0,\dots,0,b_{s-1},b_s)$ and the P-ERK sparsity (3.7), the coupling condition reduces to Eq. 3.8; sharing $a_{s-2,s-3}$, $a_{s-1,s-2}$, $a_{s,s-1}$ across members satisfies it by construction, leaving nine unknowns for eight conditions (A.1), a one-parameter family given to double precision in Eq. 3.9 with $c_{s-3}$ free (§3.2). **Derived** (compiler check, not in the sources: Eq. 3.9 satisfies (A.1a–c, e–h) and the corrected (A.1d))
10. A fourth-order P-ERK of this form needs at least 5 stages: $c_{s-3}\ne0$ is required for $a_{s-2,s-3}$ to be finite, and for $s=4$, $c_{s-3}=c_1=0$. Second- and third-order P-ERK can be built with 2 and 3 stages (§3.2). **Derived**
11. The stability polynomial does not depend on $c_{s-3}$, because $a_{i,1}=c_i-a_{i,i-1}$; $c_{s-3}$ is chosen to minimize internal error amplification, and the optimum on $[0,1]$ is $c_{s-3}=1$ (§3.2). **Shown** (not tabulated)
12. A fourth-order P-ERK family is a "classic–partitioned–classic" method: stages 1–2 are shared (internal consistency), stages $3,\dots,s-4$ are partitioned, and stages $s-3,\dots,s$ are shared (§3.3, Eq. 3.10). **Derived**
13. For $e=5$, $P(z)=\sum_{j=0}^4 z^j/j!+k_1z^5$ with $k_1=0.001055026310046423$, independent of $c_{s-3}$ (Eq. 4.4). **Derived**
14. For $e$ active stages, $P$ is affine-linear in $\gamma^{(e)}_j=\prod_{i=1}^{j}a_{e-3-i+1}$, $j=1,\dots,e-5$ (Eqs. 4.7–4.8, with $a_i:=a_{i,i-1}$), so the stability constraint is a second-order cone constraint and the Ketcheson–Ahmadia bisection with a convex inner solve applies. Only $e-5=e-p-1$ coefficients are free, against $e-p$ at orders 2 and 3 (§4.2, App. C). **Derived**
15. Optimizing the free monomial coefficients and then fitting the $e-5$ Butcher entries by least squares gives "significantly inferior results" to optimizing $\gamma^{(e)}$ directly (§4.2). **Stated** (no data shown)
16. Loss of optimality (isentropic-vortex spectrum, DGSEM degree 3, HLLC, $8\times8$ grid): the constrained step is about 85 % of the unconstrained one at $e=6$ and 96.5 % at $e=16$, for $e=5,\dots,16$; both grow linearly in $e$ (§4.3, Figs. 1–2). **Shown**
17. The maximum internal amplification factor $\widetilde{\mathcal M}$ (Eq. 4.14) grows exponentially with $e$, between the reference slopes $O(2^e)$ and $O(\exp e)$ for $e=5,\dots,18$ (Fig. 3). For $e=18$, linearly increasing $c_i=i/(e-4)$ gives $\widetilde{\mathcal M}=1.35809\cdot10^6$ and CFL 0.87; constant $c_i=1$ gives $5.34877\cdot10^5$ and CFL 0.90 (§4.4, Table 1). **Shown**
18. Constant $c_i=1$ is preferred: it puts maximum weight on the least-perturbed first stage and reduces the risk of negative $a_{i,1}$ (downwinding) (§4.4). **Stated** (heuristic)
19. Two-level P-ERK$_{4;\{10,16\}}$ on 1D advection with 2:1 refinement: the fully discrete matrix has spectral radius 1 to machine precision, confirmed by runs to $t_f=100$ (7672 steps) (§5.1, Fig. 4). **Shown**
20. The isentropic vortex on a 3-level AMR mesh with $e=\{6,10,16\}$ gives density errors of the combined scheme equal to those of the standalone members to 4–5 digits ($L^1\approx3.632\cdot10^{-7}$, $L^\infty\approx1.1497\cdot10^{-5}$), so there is no interface error growth (§5.2, Table 2). **Shown**
21. Conservation errors of P-ERK$_{4;\{6,10,16\}}$ are $O(10^{-13})$–$O(10^{-12})$, on par with Ketcheson's SSP$_{4;10}$, and come from round-off only (§5.3, Table 3). **Shown**
22. Isentropic-vortex convergence with DGSEM degree 6 and $e=\{5,9,15\}$: $L^1$ observed order 3.99 from CFL 1 to 1/2, then 1.71 as the spatial error dominates at CFL 1/4; $L^\infty$ 4.95, then 4.43 (Table 4). **Shown**
23. Lotka–Volterra with $e=\{5,9\}$: fourth-order convergence from $h=1/8$ to $2^{-13}$; the maximum-norm error (the source's $e_\infty$) flattens at $O(10^{-11})$ because the reference quadrature is inaccurate, while the averaged error ($\bar e$) converges at fourth order almost to $O(10^{-15})$ (§5.4.2, Fig. 6). **Shown**
24. Implementing P-ERK in a method-of-lines code needs only restricting element, interface, boundary and mortar loops to a partition's index set; interfaces and mortars belong to the partition of the smaller element (§6.1, Listings 1–2). **Shown** (code listing)
25. 3D linearized Euler with sound speed $10-9d(x)$, $64^3$ elements, DGSEM degree 3, above $10^8$ DOF, ten members $e=5,\dots,15$. Runtime/RHS-evaluation ratios against multirate P-ERK: standalone P-ERK$_{4;15}$ 1.41/1.75; NDB$_{4;14}$ 1.60/1.80; PKD$_{4;18}$ 2.56/2.82; CK$_{4;5}$ 2.57/2.57; RK$_{4;4}$ 3.86/3.42 (Table 5). Only about 50 % of the theoretical speedup is realized because Trixi.jl is memory-bound and partitioning loses data locality (§6.2). **Shown** (hardware not stated)
26. Isentropic vortex on 4-level AMR with $e=\{5,7,11,19\}$. Runtime/RHS ratios: P-ERK$_{4;19}$ 1.20/1.38; NDB$_{4;14}$ 1.50/1.82; TD$_{4;8}$ 1.52/1.71; RDPK$_{4;9}$ 1.40/1.63; RK$_{4;4}$ 1.79/2.08 (§6.3, Table 6). **Shown**
27. SD7003 airfoil (Ma 0.2, $\mathrm{Re}=10^4$, $\alpha=4^\circ$, 7605 quadrilaterals, degree 3) with $e=\{5,6,7,8,10,12,14\}$. Runtime/RHS ratios: P-ERK$_{4;12}$ 1.35/2.05; NDB$_{4;14}$ 1.77/2.01; TD$_{4;8}$ 1.71/1.90; KCL$_{4;9}$ 2.82/3.10; RK$_{4;4}$ 2.28/2.33 (Table 7). Time-averaged $C_L=0.3827$, $C_D=0.04995$ against P-ERK order 2: 0.3841/0.04990, order 3: 0.3848/0.04910, and literature values 0.3755/0.04978 and 0.3719/0.04940 (§6.4, Table 8). **Shown**
28. Co-rotating vortex pair (Euler + acoustic perturbation equations, degree 3, Rusanov flux) with families $e=\{5,6,8,13\}$ and $e=\{5,6,9,14\}$. Runtime/RHS ratios: standalone P-ERK$_{4;13}$/P-ERK$_{4;14}$ 1.61/1.87; NDB$_{4;14}$ 1.82/2.20; TD$_{4;8}$ 2.65/3.02; CFR$_{4;6}$ 3.86/4.26; RK$_{4;4}$ 4.77/4.52 (§6.5, Table 9). **Shown**
29. Conclusion: against optimized standalone methods from OrdinaryDiffEq.jl, RHS evaluations drop by factors of 2–3 and runtimes by "40% to 280%"; against RK4 by more than a factor of 4 (§7). **Shown** (summarizing Tables 5–9)
30. Shared final stages improve nonlinear stability: a second-order P-ERK$_{\{8,16\}}$ with 6 shared final stages (first 8 monomial coefficients equal) has much smaller interface oscillations after one step of $h\approx0.14067$ on 1D upwind finite-volume advection, at the cost of an optimal step of about 64.3 % of the unconstrained one (App. B, Fig. B.13). **Shown**

# Printed slips

- (A.1d) prints $1/6=b_{S-1}a^{(r)}_{S-1,S-2}c_{S-1}+b_Sa^{(r)}_{S,S-1}c_S$. Since $(Ac)_i=a_{i,i-1}c_{i-1}$, it should read $b_{s-1}a_{s-1,s-2}c_{s-2}+b_sa_{s,s-1}c_{s-1}$; with Eq. 3.9 the corrected form gives 0.1666667, the printed one 0.2589.
- Eq. 4.6b, $z^8$ coefficient: printed $\frac{k_1}{c_4}a_3a_4a_5c_2$; the other terms and the general form (4.7) give $\frac{k_1}{c_{8-3}}=\frac{k_1}{c_5}$.
- (C.2b) $b_m=\sum_{j=0}^{p}z_m^j/j!+k_1z^5$: the last term lacks the subscript $m$, and $p$ stands for 4.
- (C.8): $\tilde\gamma\in\mathbb R^{S-4}$ but $d\in\mathbb R^{E-4}$ (mixed $S$ and $E$, in the source's notation).
- §3.1, after Eq. 3.5: says stages $K^{(1)}_2,K^{(1)}_3$ do not influence $U_{n+1}$; by tableau 3.5, $K^{(1)}_4$ does not either, and the next sentence says "the second to fourth stage". The same passage refers to "the Butcher tableaus (3.7)", which appear later.
- §4.3: "approximately 85% of the maximum admissible timestep $\Delta t$ of the two-coefficient P-ERK stability polynomial"; the reference is the unconstrained polynomial, not a P-ERK one.
- §6.4: "runtime savings between 35% for the standalone P-ERK scheme and 71% for TD$_{4;8}$", while Table 7 has NDB$_{4;14}$ at 1.77 and KCL$_{4;9}$ at 2.82. "Multirate P-ERK require at most roughly half the scalar RHS evaluations" is contradicted by TD$_{4;8}$ at 1.90. "used also in Section 6.5" for TD$_{4;8}$, introduced in §6.3.
- Table 7 caption: "SD70003 airfoil".
- §6.4: averages "over the $[30t_c,35t_c]$ interval" while $t_c$ is defined as the nondimensional time itself.
- App. B cites [65] ("Many-stage optimal stabilized Runge-Kutta methods…") for the investigation of P-ERK nonlinear stability, which §2.5 attributes to [43].
- §6.2: the domain is "the cube $\Omega=[0,1]^3$", but Fig. 7a shows "the subdomain $[0,1]^3\subset\Omega$". Unresolved.
- §2 calls the partitioned system "the ODE system (2.2)"; it is (2.1).
- §7: "40% to 280%" runtime reduction is not meaningful above 100 %; it stands for runtime ratios up to 3.86.
- References: [36] prints the Hairer–Wanner authors reversed; [23] prints "E. Hairer, G. Wanner, S. P. Nørsett" with the DOI of the 2008 printing; [51] prints year 2013 with a 2012 DOI; [26] prints a DOI as "arXiv:10.1137/0733019"; [2] prints "S. H. Nasab"; [7] and [25] print no volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U'=F(t,U)$, $U_n$ | $y'=f(t,y)$, $y_n$ | |
| $\Delta t$ | $h$ | step size; **collision**: the source's $h$ is the minimum cell size, here $\Delta x$ |
| $S$ | $s$ | number of stages |
| $E$ | $e$ | number of active stages (degree of the member's polynomial); page-local, not in the registry; as on the [P-ERK](/methods/paired-explicit-runge-kutta.md) page |
| $K_i^{(r)}$ | $f(t_n+c_ih,Y_i)$ on partition $r$ | the source uses stage derivatives |
| $R$, $r$, $A^{(r)}$ | number of partitions, $r$, $A^{\{r\}}$ | GARK-style partition superscript |
| $b$, $c$, $C=\mathrm{diag}(c)$ | $b$, $c$, $\mathrm{diag}(c)$ | agree |
| $a_i:=a_{i,i-1}$ | $a_{i,i-1}$ | §4.2 shorthand |
| $p$ | $p$ | classical order; also the linear order of $P_{p;E}$ |
| $P_{p;E}(z)$, $\alpha_j$ | $P(z)$, $\theta_j$ | stability polynomial and its monomial coefficients |
| $k_1$, $k_2$ | — | constants from Eq. 3.9; page-local |
| $\gamma^{(E)}_j$ | — | products of subdiagonal entries (Eq. 4.8); page-local; **collision** with the registry tree density $\gamma$ |
| $J$, $\lambda_m$ | $J$, $\lambda$ | agree |
| $S_{4;E}$ | $\mathcal S$ | region of absolute stability; same letter as the stage count in the source |
| $Q_i(z)$, $\widetilde M$ | —, $\widetilde{\mathcal M}$ | internal stability polynomials and maximum internal amplification factor; **collision**: $M$ is the registry mass matrix |
| $c^{SSP}_r$ | $\mathcal C_r$ | SSP coefficient of member $r$ |
| $\Delta t_{\mathrm{Forward\ Euler}}$ | $h_{\mathrm{FE}}$ | |
| CFL, $\nu$ | $\nu$, — | the source's $\nu$ is the maximum characteristic speed, $h\le\mathrm{CFL}/\nu$; **collision** with the registry Courant number $\nu$ |
| $k$ | — | DG polynomial degree; also a summation index in Eq. 4.7 |
| $\tau/\tau^\star$ | — | runtime relative to multirate P-ERK |

# Reference list

The paper prints 100 references in numbered style ([1]–[100]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. No printed duplicates. Ref. [2] prints the first author as
"S. H. Nasab" (the ingested
[Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md)); [80]
is the ingested [Ranocha et al. (2022)](/sources/ranocha-2022.md), while
[59] (Trixi.jl, JuliaCon 2022) is `ranocha-2022-b`; [65] is the ingested
[Doehring et al. (2024)](/sources/doehring-2024.md) and [43] a different
Doehring 2024 work (`doehring-2024-b`); [36] and [23] print the
Hairer–Wanner(–Nørsett) books with irregular author order ([36] is merged
into `hairer-1996`); [51] (Ketcheson–Ahmadia) prints year 2013 with a
2012 DOI and is merged into `ketcheson-2012`; [26] prints a DOI as an arXiv identifier; [99] Boost and several
others are software. All items parsed.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Paired explicit Runge–Kutta (P-ERK) methods](/methods/paired-explicit-runge-kutta.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Trixi.jl](/software/trixi-jl.md)
