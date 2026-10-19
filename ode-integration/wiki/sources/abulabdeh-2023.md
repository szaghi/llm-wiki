---
type: Source
title: "Abu-Labdeh et al. (2023) — Monolithic multigrid for implicit Runge–Kutta discretizations of incompressible fluid flow"
description: "Monolithic geometric multigrid with an additive Vanka relaxation whose patches hold all Runge–Kutta stages, inside Newton–FGMRES, solves Gauss, Radau IIA and Lobatto IIIC stage systems for Stokes, Navier–Stokes and MHD index-2 DAEs with bounded iteration counts to 640 cores."
resource: "doi:10.1016/j.jcp.2023.111961"
source_kind: paper
authors: [Abu-Labdeh R., MacLachlan S., Farrell P.E.]
year: 2023
venue: "J. Comput. Phys. 478:111961"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Journal_of_Computational_Physics_Abu-Labdeh_Monolithic_multigrid_for_implicit_RungeKutta_discretizations.pdf"
tags: [runge-kutta, implicit, implicit-stage-solvers, preconditioning, dae, cfd]
timestamp: 2026-10-20T01:00:00Z
---

# Summary

The paper builds monolithic geometric multigrid preconditioners for the stage systems
of [fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) methods
(Gauss, Radau IIA, Lobatto IIIC, $s=2,3$). It applies them to time-dependent Stokes,
incompressible Navier–Stokes and visco-resistive incompressible MHD. The spatial
discretizations are mixed finite elements: Taylor–Hood, plus Nédélec and a Lagrange
multiplier for MHD. They are index-2
[differential-algebraic equations](/definitions/differential-algebraic-equation.md),
so the authors argue that accuracy is limited by stage order. This favours fully
implicit methods over DIRK methods, at the price of a stage system
$(I_s\otimes\mathcal M+hA\otimes\mathcal K)\mathbf k=\mathbf F$ that couples all stages.

The solver (see [implicit stage solvers](/methods/implicit-stage-solvers.md)) is
Newton–Krylov–multigrid:
- inexact Newton (Eisenstat–Walker), started from the previous step's stages;
- FGMRES as outer Krylov method;
- one geometric multigrid cycle with stage-wise interpolation $I_s\otimes P$,
  rediscretized coarse operators and a direct coarse solve;
- an additive Vanka relaxation whose vertex patches contain **all stages** of the
  patch unknowns, accelerated by Chebyshev or GMRES.

The block structure needs no Schur complement of the stage-coupled system. The code
uses Firedrake with [Irksome](/software/irksome.md), PETSc and PCPATCH.

On 2D Stokes the iteration counts stay bounded (9–26 per step) under joint mesh and
step refinement, and Radau IIA(2) reaches the accuracy of a three-stage L-stable DIRK
in about 60 % of the wall time on one-eighth of the cores. On 2D Navier–Stokes
[flow past a cylinder](/benchmarks/flow-past-cylinder.md) (up to 46.6M unknowns on
640 cores), Radau IIA and Lobatto IIIC reproduce the reference drag and lift.
Gauss(3) gives oscillatory forces, which the authors attribute to its lack of
L-stability. MHD island coalescence and a 3D MHD lid-driven cavity give fewer than
about 10 linear iterations per step, except under-resolved runs. All evidence is
numerical.

# Version read

arXiv:2202.07381v2 [math.NA], 25 Feb 2023, footer "Preprint submitted to Elsevier,
February 28, 2023", with the title footnote still reading "Submitted to the editors
DATE."; 44 pages, all read (pp. 9, 24, 28 also checked visually). It is not the JCP
version of record. Title and authors on page 1 match Crossref. Section, equation,
table and figure numbers on this page are those of arXiv v2.

# Key claims

1. No linear multistep method of order greater than 2 is A-stable (the second Dahlquist barrier), which motivates Runge–Kutta methods for higher order (§2, citing [43]). **Stated**
2. An explicit Runge–Kutta method has order $p\le s$, and $p>5$ needs at least $p+1$ stages; implicit methods reach order $2s$ (§2, citing [45, §324]). **Stated**
3. For index-2 DAEs the order of a Runge–Kutta method is limited by its stage order (§2, §3.1, citing [43, §VII.4]). **Stated**
4. DIRK stage order is "typically limited to 1", ESDIRK stage order is limited to 2, and fully implicit stage order "can be as large as the number of stages", which makes fully implicit methods the choice for DAEs (§2). **Stated**
5. Gauss, Radau IIA and Lobatto IIIC are fully implicit "with stage order equal to the number of stages": Gauss of order $2s$ (A- but not L-stable), Radau IIA of order $2s-1$ and Lobatto IIIC of order $2s-2$ (both A- and L-stable) (§5). **Stated** (the stage-order claim is wrong for Lobatto IIIC, whose stage order is $s-1$; see the [fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md) page)
6. The time-dependent Stokes system with constraint $-\nabla\cdot u=0$ is an index-2 DAE (§3.1). **Derived** (informal differentiation count)
7. A Runge–Kutta method applied to the Taylor–Hood Stokes DAE gives the stage system $\Big(I_s\otimes\begin{bmatrix}M&0\\0&0\end{bmatrix}+hA\otimes\begin{bmatrix}K_{\mathrm S}&B_{\mathrm S}\\B_{\mathrm S}^\top&0\end{bmatrix}\Big)\mathbf k=\mathbf F$, with pressure advanced by its own stage derivatives (Eq. (3), §3.1). **Derived**
8. An additive Vanka relaxation whose patches contain all stage unknowns, inside multigrid with stage-wise interpolation $I_s\otimes P$, is a robust and scalable monolithic preconditioner for Runge–Kutta saddle-point systems, and avoids approximating method-dependent Schur complements (§4, §4.2, §6). **Shown**
9. FGMRES is preferred to right-preconditioned GMRES: it trades vector storage for one fewer preconditioner application and allows GMRES inside the relaxation (§4). **Stated**
10. For finite elements, rediscretization equals Galerkin coarsening when compatible quadrature is used (§4.1). **Stated**
11. On 2D Stokes, average linear iterations per step stay between 8.70 and 25.97 for refinement levels 5–7 (1.1M to 19M unknowns per stage) across Gauss, Radau IIA and Lobatto IIIC with 2 and 3 stages, with the tolerance falling 8× per level (Table 1). **Shown**
12. Velocity errors converge at least at second order for all three families when $h$ is halved with each mesh refinement: Gauss 2.5, Radau IIA 3.0, Lobatto IIIC 2.0 for two stages, 2.4–3.1 for three; Gauss errors are much larger than Radau IIA and Lobatto IIIC errors (Tables 1–2). **Shown**
13. Wall-time weak scaling grows about 3.5× per level against an ideal 2×, attributed to iteration growth, memory-bandwidth saturation and a communication-dominated coarse solve (§5.1). **Shown**
14. With fixed $h=0.5/2^8$, spatial refinement alone makes the velocity error stagnate (e.g. Radau IIA(2): $3.380\times10^{-6}\to3.119\times10^{-6}\to3.101\times10^{-6}$), so refining $h$ with the mesh pays off even for high-order integrators (Table 3, §5.1). **Shown**
15. The L-stable DIRK methods of Pareschi–Russo (2 stages, order 2) and Alexander (3 stages, order 3) beat their stage-order-1 guarantees but are much less efficient than Radau IIA: DIRK(3) at level 6 matches Radau IIA(2) at level 5, which needs about 60 % of the wall time on one-eighth of the cores (Table 4 against Table 1, §5.1). **Shown**
16. On flow past a cylinder (Re 100, $h=1/400$, $T_f=8$), Radau IIA and Lobatto IIIC with 2 and 3 stages give maximum drag 2.95 and maximum lift 0.48 at every level 3–6, in agreement with the reference data (Table 6, Fig. 3). **Shown**
17. On the cylinder problem, average Newton iterations per step are 1.35–2.70 and linear iterations 1.61–8.19, with 0.03–0.19 min per step on up to 640 cores and 46,566,816 unknowns (Tables 5–6). **Shown**
18. Gauss(3) on the cylinder problem gives "highly oscillatory" drag and lift even with a stricter tolerance; the authors hypothesize that its lack of L-stability is the cause, since stiff modes with $R(z)$ close to $-1$ decay slowly and oscillate (§5.2, Fig. 4). **Shown** (phenomenon) / **Stated** (cause)
19. On MHD island coalescence with Lobatto IIIC(2), Re $=$ Re$_m\in\{5000,10000,20000\}$ (2.7M–42.7M unknowns per stage, 40–640 cores), the reconnection rates behave as expected and the linear iterations stay below about 10 per step, slightly above BDF2 with the same discretization (§5.3, Figs. 5–7). **Shown**
20. For island coalescence the Alfvén CFL number is about 6 throughout, and the fluid CFL number exceeds 1 at the largest Re, with histories "identical" to the BDF2 case (Fig. 8). **Shown**
21. On the 3D MHD lid-driven cavity with Lobatto IIIC(2), average linear iterations are 4.20–8.34 and Newton iterations 2.16–3.52, except 31.55 and 17.59 linear iterations for under-resolved Re $=1000$ runs (Table 7). **Shown**
22. GMRES-accelerated Vanka beats Chebyshev at high Re; at Re $=$ Re$_m=1$ Chebyshev is "significantly better" and the GMRES-accelerated relaxation sometimes fails (§5.4). **Shown** (partly not tabulated)
23. A Chebyshev interval $[\lambda_{\max}/4,\lambda_{\max}]$ is a practical heuristic in 2D with factor-2 coarsening; the intervals actually used were hand-tuned (§5.1–5.3). **Stated**
24. No rigorous stopping tolerances guarantee discretization-level accuracy for these systems, so hand-tuned tolerances are used (§5). **Stated**

# Printed slips

- §5.3: "Re = Rem : 5000, 1000 and 20000"; the figures and the rest of the text use 10000.
- Captions of Figs. 6, 7 and 8 print "LobattoIIC(2)".
- §4: "we choose to use FMGRES" for FGMRES.
- §5.2 says Fig. 4 shows Gauss(3) "with ℓ = 3"; the caption reads "ℓ = 4".
- Table 2 against Table 1: recomputing the Gauss(3) rates gives velocity 2.31 (printed 2.4) and pressure −2.20 (printed −2.3).
- Table 4, DIRK(2): the velocity error rises from $2.480\times10^{-5}$ (ℓ = 5) to $6.198\times10^{-5}$ (ℓ = 6) and then falls to $1.546\times10^{-5}$ (ℓ = 7), without comment.
- p. 9: the final pressure update prints $\vec k_j^{p}$ for $\vec k_j^{(p)}$.
- §3.1 and §3.3: $H^1_0(\Omega)=\{v\in H^1(\Omega):\mathbf u=0$ on $\partial\Omega\}$ uses $u$ for $v$.
- §3.3, weak form (7): the viscous term is printed $-\frac{2}{Re}(\varepsilon(u):\varepsilon(v))$; integration by parts gives a plus sign.
- §3.2: the stage equation uses $K$ without the viscosity $\mu$ of Eq. (5).
- Ref. [43] prints "G. Wanner, E. Hairer" and "Vol. 375" for the Hairer–Wanner book.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $r$ | $s$ | number of stages |
| $\Delta t$ | $h$ | constant step |
| $u'(t)=f(u(t),t)$ | $y'=f(t,y)$ | argument order differs |
| $k_i$, $\vec k_i^{(u)}$, $\vec k_i^{(p)}$; $\vec k$ | $k_i=f(t_n+c_ih,Y_i)$; stacked $\mathbf k$ | **stage derivatives**, the solver's unknowns |
| $\vec u_i^n$, $\vec p_i^n$ | $Y_i$ (and the algebraic stage $W_i$) | stage values |
| $a_{ij}$, $A$, $b_j$, $c_i$ | $A$, $b$, $c$ | agree |
| $r(z)$, $z=\lambda\Delta t$ | $R(z)$, $z=h\lambda$ | **$r$ collides** with the source's own stage count; stability domain printed with strict $\lvert r\rvert<1$ |
| $p$ | $p$ | order; **also the pressure** in the source |
| $q$ | $q$ | stage order, defined in the source as $\min\{q,p\}$ |
| $M$ | $M$ | velocity mass matrix (agrees) |
| $K$, $B$ | $K_{\mathrm S}$, $B_{\mathrm S}$ (page-local) | stiffness and weak gradient; **collide** with the registry iteration count $K$ and simplifying assumption $B(\xi)$ |
| $B$, $\gamma$ (MHD) | kept | magnetic field and Lagrange multiplier; **$\gamma$ collides** with the registry $\gamma$ |
| $J$ | kept | Jacobian of the stage system (not the ODE Jacobian alone) |
| $\eta_\ell$ | kept | Eisenstat–Walker forcing term; **not** the registry entropy $\eta$ |
| $\ell$ | kept | refinement level and Newton index; **collides** with the registry micro-step index |
| $P$, $R_i$, $S_i$, $\omega$ | kept | interpolation, patch restriction, patch set, relaxation weight |

# Reference list

The paper prints 69 references in numbered Elsevier style ([1]–[69]). The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this slug.
[40] is Irksome, the ingested source `farrell-2021`; the other two Farrell 2021
items are `farrell-2021-b` ([27], Reynolds-robust Scott–Vogelius preconditioner)
and `farrell-2021-c` ([53], PCPATCH). [43] is printed with author order
"Wanner, Hairer" and a spurious "Vol. 375" and is merged into `hairer-1996`.
Several keys take suffixes because the bibliography already held a different
work under the plain key: [4] `scott-1985-b`, [9] `hu-2017-b`, [10] `hu-2019-b`,
[52] `farrell-2020-b`. [57] is an authorless Zenodo software archive and [59] a
Wikipedia page. The preprints [28], [30] and [38] are kept as their own entries;
[38] (arXiv:2101.01776) is `southworth-2021-b`, the preprint of the ingested
[Southworth et al. (2022)](/sources/southworth-2022.md), and [30] its Part I
preprint `southworth-2021`. No printed duplicates and no unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Flow past a cylinder (Schäfer–Turek)](/benchmarks/flow-past-cylinder.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Irksome](/software/irksome.md)
* [Order reduction](/definitions/order-reduction.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
