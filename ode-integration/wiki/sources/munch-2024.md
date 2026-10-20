---
type: Source
title: "Munch et al. (2024) — Stage-Parallel Fully Implicit Runge–Kutta Implementations with Optimal Multilevel Preconditioners at the Scaling Limit"
description: "Implements stage-parallel Radau IIA solvers with matrix-free multigrid in deal.II: an LU-based real preconditioner and the exact complex diagonalization decouple the stages onto process subgroups, a performance model bounds the speed-up by $s$, and runs to 147,456 processes show gains below 10k unknowns per process."
resource: "doi:10.1137/22m1503270"
source_kind: paper
authors: [Munch P., Dravins I., Kronbichler M., Neytcheva M.]
year: 2024
venue: "SIAM J. Sci. Comput. 46:S71-S96"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_SIAM_Journal_on_Scientific_Computing_Munch_Stage-Parallel_Fully_Implicit_RungeKutta_Implementations_wit.pdf"
tags: [runge-kutta, implicit, implicit-stage-solvers, preconditioning, hpc]
timestamp: 2026-10-20T01:00:00Z
---

# Summary

The paper studies parallelism across the stages of Radau IIA
[fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) methods (order
$2s-1$) for the linear finite-element system $M\dot u+K_{\mathrm S}u=g(t)$. The goal
is a faster integrator once the spatial solver has hit its strong-scaling limit. The
stage system is multiplied by $A^{-1}\otimes I$ to the form
$(A^{-1}\otimes M+hI_s\otimes K_{\mathrm S})\mathbf k=\text{rhs}$ and solved by
GMRES.

Two decoupling preconditioners are used (see
[implicit stage solvers](/methods/implicit-stage-solvers.md)):
- the Axelsson–Neytcheva preconditioner: write $A^{-1}=\mathsf L\mathsf U$ with unit
  upper-triangular $\mathsf U$, keep $\mathsf L$ and diagonalize it, which gives $s$
  real blocks $\tilde\lambda_iM+hK_{\mathrm S}$;
- Butcher's exact complex diagonalization of $A^{-1}$, which gives $\lceil s/2\rceil$
  complex blocks, solved with PRESB or with multigrid on the $2\times2$ real form.

Each block is approximately inverted by one V-cycle of matrix-free geometric multigrid
(deal.II), and the blocks are assigned to concurrent process subgroups. The
implementation contributions are:
- a stage × partition process grid with row and column communicators;
- a Cannon-like ring algorithm for the stage-coupling products $(D\otimes I)u$;
- a shared-memory variant;
- a batched mode that treats all stages as a multivector.

A performance model predicts that at the scaling limit the sequential cost scales
with the sum of block iterations and the stage-parallel cost with their maximum, so
the speed-up is at most $s$. On SuperMUC-NG (3D heat equation, up to 147,456
processes, $s\le9$) stage parallelism wins clearly below 10k unknowns per process
and loses about 20 % above 100k. The complex variant has about half the speed-up,
but its per-block iteration counts do not grow with $s$, so both stage-parallel
variants reach similar minimal times. Batching gives only 5–25 % because deal.II's
intergrid transfer serializes per stage. No accuracy results are reported.

# Version read

arXiv:2209.06700v1 [math.NA], 14 Sep 2022, title-page date "15th June, 2022";
25 pages, all read (pp. 4, 5, 7, 8, 9, 19, 20, 21 also visually). It is not the
SIAM version of record (S71–S96, issue 2024, online 2023). Page 1 prints the same
title in sentence case with an ASCII hyphen; authors match Crossref. Section,
equation, table and figure numbers on this page are those of arXiv v1.

# Key claims

1. Radau IIA with $s$ stages has order $2s-1$ (§2). **Stated**
2. After left multiplication by $A^{-1}\otimes I$, the stage system of a Runge–Kutta method for $M\dot u+K_{\mathrm S}u=g$ reads $(A^{-1}\otimes M+hI_s\otimes K_{\mathrm S})\mathbf k=(A^{-1}\otimes I)\bar g+(A^{-1}\otimes K_{\mathrm S})(\mathbf 1\otimes u_0)$ (Eq. (1), §2). **Derived** (sign slip in the $K_{\mathrm S}u_0$ term; see Printed slips)
3. With $A^{-1}=S\Lambda S^{-1}$ (Butcher), the system decouples into blocks $\lambda_iM+hK_{\mathrm S}$; for Radau IIA $\Lambda$ has $\lfloor s/2\rfloor$ complex-conjugate pairs plus one real eigenvalue for odd $s$ (Eq. (2), §2). **Stated**
4. The real Schur form gives a real block-triangular factorization with $2\times2$ diagonal blocks $\begin{bmatrix}\operatorname{Re}\lambda_i&\alpha\\-(\operatorname{Im}\lambda_i)^2/\alpha&\operatorname{Re}\lambda_i\end{bmatrix}$ for an arbitrary constant $\alpha$ (§2). **Stated**
5. Axelsson–Neytcheva write $A^{-1}=\mathsf L\mathsf U$ with $\mathsf U$ unit upper triangular, so all eigenvalues of $\mathsf L^{-1}A^{-1}$ equal one, and build the preconditioner from $\mathsf L$ (§2). **Stated** (eigenvalue analysis deferred to [6])
6. The spectral decomposition of $\mathsf L$ is always real, so $s$ real blocks $\tilde\lambda_iM+hK_{\mathrm S}$ can be solved independently, against $\lceil s/2\rceil$ blocks in the complex case (§2, Eq. (3)). **Stated**
7. The parallel building blocks are the stage-local "generalized vector scaling" $(I_s\otimes C)u$ and the stage-coupling "generalized matrix-vector product" $(D\otimes I)u$, $D\in\mathbb R^{s\times s}$ (Eqs. (4)–(5)). **Derived**
8. $(D\otimes I)u$ is computed by a circular, Cannon-like algorithm with MPI_Sendrecv_replace on the row communicator; unlike Cannon's algorithm $D$ is replicated and the operands are tensors (§3.3, Eq. (6)). **Derived**
9. The preconditioner times are $T_{\mathrm{IRK}}(N)=2T_S(N)+\sum_qT_{B_q}(N)$ and $T_{\mathrm{SPIRK}}(N)=2T'_S(N)+\max_qT_{B_q}(N/s)$ for $N$ processes, so the speed-up is at most $\sum_qT_{B_q}/\max_qT_{B_q}\le s$, and stage parallelism pays off only at the scaling limit with comparable block times (§4, Eqs. (7)–(8)). **Derived**
10. At the scaling limit $T_{\mathrm{IRK}}\sim\sum_qN^{\mathrm{IT}}_q$ and $T_{\mathrm{SPIRK}}\sim\max_qN^{\mathrm{IT}}_q$, so iteration counts bound the speed-up (§4). **Derived**
11. Idealized stage-parallel speed-ups for $s=8$ are ×1.06, ×1.42, ×3.98 across the process range: a few percent far from the scaling limit, approaching $s$ at it (Fig. 1b). **Shown**
12. On 16 nodes (768 processes), FE degree 1, $s=4$: sequential solves on 4× the processes reach speed-up 3.7 for large problems but collapse for small ones; the stage-parallel solver exceeds 3 over large ranges, maximum 3.6 (§5.1, Fig. 5). **Shown**
13. In the time breakdown ($s=4$, 768 processes) the sequential solver spends 75 % in block preconditioners and 1 % in basis changes at refinement level 8; at level 6 preconditioning is 90 % (sequential) and 77 % (stage-parallel) of the total, and stage parallelism cuts it by a factor of 3.1 (§5.1, Fig. 6). **Shown**
14. Higher FE degree raises throughput and seems to raise the stage-parallel speed-up; larger $s$ lowers throughput more than the extra work explains, because outer GMRES iterations grow with $s$, while the achievable speed-up rises with $s$ (§5.1, Fig. 7). **Shown**
15. GMRES iterations per step (degree 1, level 8) are 5.0, 7.0, 9.9, 11.9 for $s=2,4,6,8$; sequential V-cycles 12.0, 32.0, 65.3, 103.1 against 6.0, 8.0, 10.9, 12.9 per process group for the stage-parallel solver, a factor 8 fewer at $s=8$ (§5.1, Table 2). **Shown**
16. Row-major process layout favours the stage-coupling product, column-major favours multigrid, and padded row-major with MPI shared memory reads all stages directly; shared memory helps in a few cases but not overall, because the basis change is not the bottleneck (§5.2, Figs. 8–9). **Shown**
17. In strong scaling from 1 to 3,072 nodes (48 to 147,456 processes), FE degrees 1 and 4, $s=2,4,9$, the stage-parallel solver reaches lower time to solution at the scaling limit and the sequential one is more efficient far from it (§5.3, Figs. 10–12). **Shown**
18. Below 10k unknowns per process (about half a million per node) the stage-parallel solver is clearly faster; between 10k and 100k the picture is split; above 100k the sequential solver is consistently about 20 % faster (§5.3, Fig. 13). **Shown**
19. A four-stage method runs in less than 0.05 s per time step; far from the scaling limit the stage-parallel solver has 13 % lower throughput on average (§7). **Shown**
20. Batched execution ($s=8$, 16 nodes, Chebyshev–Jacobi coarse solver) gives only 5–25 % speed-up because deal.II's intergrid transfer is serialized per stage; GMRES iterations are not hurt by Chebyshev coefficients from the largest eigenvalue over all blocks; a preliminary single-vector multigrid batching reaches up to 5.7 (§5.4, Fig. 14, Table 2). **Shown**
21. Batching needs every multigrid component to support multivectors (Chebyshev–Jacobi does, AMG typically does not); it saves memory and could favour deformed meshes, which are not studied (§3.4, §5.4). **Stated**
22. The exact complex diagonalization solves $\lceil s/2\rceil$ blocks $(\operatorname{Re}\lambda_iM+hK_{\mathrm S})+i\operatorname{Im}\lambda_iM$ independently, each with its own GMRES, and needs only two basis changes per step (§6, Eqs. (9)–(10)). **Derived**
23. PRESB preconditions the $2\times2$ real form, with one V-cycle for the inner inverse and two sequential V-cycles per application (§6, Eq. (11)). **Stated**
24. For the complex variant, per-block iterations are essentially independent of $s$ (PRESB 5.0–6.2, multigrid 7.0–9.3 for $s=2$–$8$), while the sequential complex solver grows from 6.0 to 23.1 (PRESB) and 7.0 to 31.3 (multigrid) (§6, Table 2). **Shown**
25. The complex stage-parallel speed-up over the sequential complex solver is about half that of the real stage-parallel preconditioner, but the two stage-parallel variants reach similar minimal times for $s\le8$ (§6, §7, Figs. 16–17). **Shown**
26. PRESB beats multigrid on the $2\times2$ system in time because it needs fewer GMRES iterations; scalability is comparable and multigrid needs fewer V-cycles in total (§6, Fig. 18). **Shown**
27. The blocks of Southworth et al. (Part I) are quadratic in $hM^{-1}K_{\mathrm S}$ and their algorithm is "inherently stage-serial", so the stage-parallel algorithms do not apply there (§6). **Stated**
28. The stage-uncoupled block-Jacobi of Pazner & Persson is stage-parallel; the present preconditioner is stage-coupled through the basis changes at a similar cost, because basis changes are cheap (§2). **Stated** / **Shown** (Fig. 6)
29. Running at the scaling limit presumes ample hardware; far from it, stage-parallel and parallel-in-time methods may lose to organizational overhead (§1). **Stated**

# Printed slips

- §2, stage system: the right-hand side is printed $K u_0+g(t_0+c_i\tau)$ and $\bar g+(I_Q\otimes K)(e_Q\otimes u_0)$; for $M\dot u+Ku=g$ the term is $g-Ku_0$. The sign propagates into Eqs. (1) and (2).
- §2, list item 3: "$(\lambda_iM+\tau\otimes K)$", a stray $\otimes$.
- §2 and Fig. 4: "$A_q^{-1}$" and "$I_q$" in lower case.
- §3.2: "$v_2=D_{11}u_1+D_{21}u_2+\cdots+D_{2Q}u_Q$" for $D_{21}u_1+D_{22}u_2+\cdots$.
- Eq. (6), first sum, last row: "$D_{Q1}u_Q$" for $D_{Q1}u_1$.
- §6, block form of (6): "$D_{11}u_1+D_{11}u_2$" for $D_{11}u_1+D_{12}u_2$.
- Eq. (10): lower-right block "$K_i$" for $K'_i$.
- §5.1: "786 processes (16 compute nodes)"; 16 × 48 = 768, as used elsewhere.
- §4: "$T_\square(N)\approx T_\square(1)/N$" prints a placeholder box.
- Typos: "Pazner and Person", "GRMES", "adn", "implementation of of"; ref. [6] "arbritary", ref. [10] "R. Spech", ref. [30] "H. D. Sterck", ref. [32] "G. Wanner and E. Hairer … vol. 375".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Q$ | $s$ | number of stages |
| $\tau$ | $h$ | step size |
| $A_Q$, $b_Q$, $c_Q$ | $A$, $b$, $c$ | Butcher tableau |
| $k$, $k_i$ | $\mathbf k$, $k_i=f(t_n+c_ih,Y_i)$ | **stage derivatives**, the solver's unknowns; the source's $k$ is also the FE degree |
| $e_Q$ | $\mathbf 1$ | vector of ones |
| $M$ | $M$ | mass matrix (agrees) |
| $K$ | $K_{\mathrm S}$ (page-local) | stiffness matrix; **collides** with the registry iteration count $K$ |
| $n$ | $d$ (dimension) or $n$ (step) | **overloaded** in the source |
| $S$, $\Lambda$, $\lambda_i$ | kept | eigen-decomposition of $A^{-1}$ (not of $A$); reused after Eq. (3) for $\mathsf L$ |
| $L$, $U$ | $\mathsf L$, $\mathsf U$ | LU factors of $A^{-1}$; **$L$ collides** with the registry linear operator and with the source's refinement level $L$ |
| $\tilde S$, $\tilde\Lambda$, $\tilde\lambda_i$ | kept | real eigen-decomposition of $\mathsf L$ |
| $K'_i$, $M'_i$ | kept | $\operatorname{Re}\lambda_iM+hK_{\mathrm S}$ and $\operatorname{Im}\lambda_iM$ |
| $\alpha$ | kept | arbitrary real-Schur constant; **not** the registry $\alpha_{ij}$ |
| $N$, $B$, $T_\square$, $N^{\mathrm{IT}}_q$ | kept | processes, spatial partitions, times, iteration counts |
| IRK, SPIRK | kept | sequential and stage-parallel solver labels |

# Reference list

The paper prints 32 references in numbered style ([1]–[32], alphabetical). The
list is merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. [15] is Irksome (the ingested source `farrell-2021`) and [29] is
Southworth et al. Part II (the ingested source `southworth-2022`). [30] is the
published Part I, `southworth-2022-b`, kept distinct from its arXiv preprint
entry `southworth-2021`. [32] is printed "G. Wanner and E. Hairer … vol. 375"
for the Hairer–Wanner book and is merged into `hairer-1996`. [2] (Adams 2003)
is `adams-2003-b`, because the bibliography already held a different work under
the plain key. [13] (Cannon 1969) has no document kind and [26] no venue. No
printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [Irksome](/software/irksome.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
