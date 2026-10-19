---
type: Source
title: "Southworth et al. (2022) — Fast Solution of Fully Implicit Runge–Kutta and Discontinuous Galerkin in Time for Numerical PDEs, Part II: Nonlinearities and DAEs"
description: "Extends a real-Schur, block-triangular preconditioning framework for fully implicit Runge–Kutta stage systems to nonlinear PDEs and DAEs, with Newton-like stage-Jacobian approximations, a condition-number bound for the 2x2 blocks, and MFEM tests against SDIRK."
resource: "doi:10.1137/21m1390438"
source_kind: paper
authors: [Southworth B.S., Krzysik O.A., Pazner W.]
year: 2022
venue: "SIAM J. Sci. Comput. 44:A636-A663"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_SIAM_Journal_on_Scientific_Computing_Southworth_Fast_Solution_of_Fully_Implicit_Runge--Kutta_and_Discontinuo.pdf"
tags: [runge-kutta, implicit, implicit-stage-solvers, preconditioning, dae, method-of-lines]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

Fully implicit collocation methods (Gauss, Radau IIA, Lobatto IIIC; see
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md))
reach order $p=2s$ and [stage order](/definitions/stage-order.md) $q=s$. That
avoids the [order reduction](/definitions/order-reduction.md), the stage-order-1
limit and the symplectic-order limits of
[DIRK methods](/methods/diagonally-implicit-runge-kutta.md) (see
[symplecticity](/properties/symplecticity.md)). In practice these methods are
rarely used for large PDE problems because the coupled $sd\times sd$ stage system
is hard to solve. This paper is Part II of a pair. It extends the authors'
linear-PDE preconditioning framework to nonlinear PDEs, where each stage has its
own Jacobian $L_i$, and to [differential-algebraic equations](/definitions/differential-algebraic-equation.md).

The stage system is rewritten through the real Schur decomposition of $A^{-1}$.
The decomposition is not new (it comes from the RADAU code); the contribution
is the robust preconditioning built on it. When the $L_i$ differ, the
conjugated stage-Jacobian operator has zero-sum off-diagonal couplings. Four
block-upper-triangular approximations of it (simplified Newton and Newton-like
(1)–(3)) reduce each Newton step to a block back substitution over $1\times1$
and $2\times2$ blocks. Each $2\times2$ block is solved by GMRES with a block
lower-triangular preconditioner whose Schur-complement shift is
$\gamma_{\mathrm S}=\eta+\beta^2/\eta$. Only backward-Euler-type operators
$\gamma M-hL$ are inverted. The paper proves a condition-number bound
$2+\beta^2/\eta^2$ for unequal stage Jacobians, which requires an extra
hypothesis, and gives the DAE extension through $4\times4$ blocks.
These results feed the page on [solving implicit stage equations](/methods/implicit-stage-solvers.md).

The numerical tests use MFEM. On the [isentropic vortex](/benchmarks/isentropic-vortex.md),
orders 2–7 are observed. The other tests are an $\mathrm{Re}=40\,000$ NACA0012
compressible Navier–Stokes flow and an index-1 vorticity–streamfunction double
shear layer. Fourth-order Gauss needs roughly half the preconditioner
applications of SDIRK4 at equal step size. Gauss and Radau IIA methods of
orders 7–10 cost about as much as SDIRK4 on the double shear layer. The paper
also points to [Irksome](/software/irksome.md) as a concurrent IRK
implementation, and notes that A-stability with an irreducible, invertible $A$
puts every eigenvalue of $A$ in the right half plane
([A-stability](/properties/a-stability.md)).

# Version read

The file is the arXiv preprint arXiv:2101.01776v3 [math.NA] (5 Oct 2021; the
title page is dated 7 October 2021), 30 pages, single column with arXiv
pagination. It is not the SIAM version of record. Its title is printed in
sentence case and it gives no DOI; otherwise it matches the published identity.
The author order (Southworth, Krzysik, Pazner) matches Crossref. Part I of the
pair (arXiv:2101.00512, with De Sterck as a fourth author) is not in the
archive; Theorem 1 is restated from it without proof. Equation, table and
section numbers on this page are those of arXiv v3.

# Key claims

Notation: $h$ is the step, $\bar L_i:=hM^{-1}L_i$ is the scaled stage
linearization, $\eta\pm i\beta$ are the eigenvalues of $A^{-1}$, $W(\cdot)$ is
the field of values and $\kappa(\cdot)$ is the 2-norm condition number (see the
notation map).

1. For stiff PDEs, the accuracy of Runge–Kutta methods observed in practice can be limited to about $\min\{p,q+1\}$. For index-2 DAEs the order is formally limited to $q$ (§2.1, citing HW-II and Kennedy–Carpenter). **Stated**
2. DIRK methods have maximum order $p=s$ or $p=s+1$ "with reasonable stability properties" and stage order $q=1$ ($q=2$ for ESDIRK with one explicit stage). Fully implicit RK methods reach $p=2s$, $q=s$ (§2.1). **Stated**
3. A-stable linear multistep methods have order at most two. Neither LMMs nor explicit RK methods can be symplectic in general for non-separable problems. Symplectic DIRK methods are limited to order 4, and the known ones above order 2 have negative diagonal entries of $A$ (§2.1). **Stated**
4. If an RK method is A-stable and irreducible and $A$ is invertible (DIRK, Gauss, Radau IIA and Lobatto IIIC qualify), then every eigenvalue of $A$ has positive real part (Assumption 1, §2.2). **Stated**
5. $\lVert e^{tL}\rVert\le1$ for all $t\ge0$ if and only if $W(L)\le0$ (the motivation for Assumption 2; §2.2, citing Trefethen–Embree Thm 17.1). **Stated**
6. Under simplified Newton ($L_i=L$), the real Schur form $A^{-1}=Q_0R_0Q_0^\top$ turns the stage system into a block upper triangular one. Its $1\times1$ blocks are $\eta I-\bar L$, and its $2\times2$ blocks belong to the complex-conjugate pairs (eq. (9)). The Schur reduction itself comes from RADAU; the contribution is the robust preconditioning (Remark 3). **Derived**
7. In the conjugated operator $\hat P=(Q_0^\top\otimes I)\operatorname{diag}(\bar L_i)(Q_0\otimes I)$, the weights satisfy $\sum_i(d_{k,\ell})_i=\delta_{k\ell}$. Hence $\hat P=I\otimes\bar L$ when all the $\bar L_i$ coincide (§3.2). **Derived**
8. For 2-stage Gauss, $\hat P$ is exactly block diagonal, so true Newton needs no approximation. For 2-stage Radau IIA, $\hat P$ has weights $\{0.985,0.015\},\{0.121,-0.121\};\{0.121,-0.121\},\{0.015,0.985\}$ (eq. (13)). **Derived**
9. Newton-like(3) is an exact Newton iteration for 2-stage methods (§3.2, item 3). **Derived**
10. Theorem 1 (restated from Part I, Th. 5): with $\gamma_{\mathrm S}=(\eta^2+\beta^2)/\delta$, the bound is $\kappa(\mathcal P_{\delta,\gamma_{\mathrm S}})\le\frac1{2\eta}\big(\delta+\frac{\eta^2+\beta^2}{\delta}\big)$. It is tight over all $\bar L$ with $W(\bar L)\le0$, and this $\gamma_{\mathrm S}$ minimizes the worst case (eqs. (21)–(22)). **Stated** (proof in Part I)
11. Corollary 1: for $\bar L_1=\bar L_2$, the shift $\gamma_{\mathrm S}=\eta+\beta^2/\eta$ is optimal and $\kappa(P_{\gamma_{\mathrm S}})\le1+\frac{\beta^2}{2\eta^2}$, tight (eqs. (23)–(24)). **Proved**
12. Bounds on $\kappa(P_{\gamma_{\mathrm S}})$ (Table 1) range from 1.00 to 3.44 over Gauss, Radau IIA and Lobatto IIIC with 2–5 stages. Examples: Gauss 2-stage 1.17; Radau IIA 2-stage 1.25; Lobatto IIIC 5-stage 1.00/3.44/1.19. **Derived**
13. Remark 4: for symmetric negative semidefinite $\bar L$, the tight bound at $\gamma_{\mathrm S}$ is $\kappa\le\frac12\big(1+\sqrt{1+\beta^2/\eta^2}\big)$. For skew-symmetric $\bar L$ the bound equals (24). **Stated**
14. Theorem 2: suppose $\eta>0$, $W(\bar L_1)\le0$, $W(\bar L_2)\le0$ and $\langle\bar L_1w,\bar L_2w\rangle\ge0$ for all $w$. Then $\kappa(P_{\gamma_{\mathrm S}})\le2+\beta^2/\eta^2$ (eq. (25), App. A). The authors do not believe the last hypothesis is necessary, but could not prove the bound without it. **Proved**
15. For a $2\times2$ block operator with a block-triangular preconditioner, GMRES convergence is determined by GMRES on the preconditioned Schur complement. With the exact Schur complement, GMRES converges in two iterations (§4). **Stated**
16. Isentropic Euler vortex (degree-4 DG, 532 triangles), observed orders at the finest refinement: Gauss 2/4/6 → 2.07/4.07/5.99; Radau IIA 3/5/7 → 2.90/4.91/6.28; Lobatto IIIC 2/4/6 → 1.88/3.67/5.83 (Table 2). **Shown**
17. Euler vortex at $h=2\times10^{-2}$, preconditioner applications: SDIRK 1/2/3/4 → 20/26/45/59; Gauss 2/4/6/8/10 → 15/36/103/162/169; Radau 3/5/7/9 → 44/121/168/205; Lobatto 2/4/6/8 → 66/225/210/292 (Table 3). **Shown**
18. The shift $\gamma_{\mathrm S}=\eta+\beta^2/\eta$ lowers the mean Krylov iterations per $2\times2$ system compared with the naive $\gamma_{\mathrm S}=\eta$ (Gauss 10: 14.9 → 7.6; Lobatto 8: 35.2 → 11.2; Radau 9: 20.6 → 9.3), even though $\bar L_1\ne\bar L_2$ (Table 4). **Shown**
19. NACA0012 ($\mathrm{Re}=40\,000$, angle of attack 30°, Mach 0.1, degree-3 CDG, 3154 triangles, $h=5\times10^{-2}$), preconditioner applications: SDIRK 1/2/3/4 → 173/200/359/481; Gauss 2/4/6/8/10 → 128/244/557/732/830; Radau 3/5/7/9 → 314/728/926/1061; Lobatto 2/6/8 → 454/1670/1995 (Table 5). **Shown**
20. NACA solver comparison (Fig. 2). Gauss 4 runtimes for solvers 0/1/2/3 are 33.8/21.7/21.6/21.6 s; Radau 3 runtimes are 47.1/33.3/35.2/25.4 s. Better Jacobian approximations run faster despite their higher cost per iteration. The effect is problem-dependent: simplified Newton can win for small $h$ (§7.1.2). **Shown**
21. Double shear layer ($\mathrm{Re}=10$, degree 3, $h=10^{-2}$, 288 cores), preconditioner applications with formulation (41): SDIRK 1/2/3/4 → 127/141/322/365; Gauss 2/4/6/8/10 → 78/161/218/287/333; Radau 3/5/7/9 → 237/232/299/490; Lobatto 2/4/6/8 → 217/234/311/375 (Table 6). **Shown**
22. The block-triangular reordering (42) needs many more iterations than the coupled formulation (41) in all cases (Table 6). **Shown**
23. Linear iteration counts are nearly equal for Newton-like methods 1, 2 and 3 on the double shear layer (data not shown). **Stated**
24. At $\mathrm{Re}=25\,000$: SDIRK 1/2/3/4 → 41/72/113/177; Gauss → 37/75/118/163/194; Radau → 81/123/165/206; Lobatto → 91/130/173/220 (Table 7). **Shown**
25. Double-shear-layer accuracy ($\mathrm{Re}=100$, $t\in[0,10]$, $h\in\{0.4,0.2,0.1\}$), final rates: Gauss 4/6/8 → 3.99/6.61/6.63; Radau 5/7/9 → 4.94/6.91/1.96; Lobatto 4/6/8 → 3.92/5.91/6.30. The reduced high-order rates are attributed to the nonlinear tolerance $10^{-11}$ (Table 8). **Shown**
26. Low-order Gauss "consistently requires about half the preconditioner applications" of standard SDIRK schemes, and Gauss and Radau IIA of orders 7–10 cost about as much as SDIRK4 on the double shear layer (§8). **Shown**, in part: the comparison is at equal order and equal $h$, not at equal accuracy, and the ratio is 0.61 in Table 3.

# Printed slips

- §7.1.2 and the Table 5 caption give $\delta t=5\times10^{-2}$, but the Figure 2 caption reads "NACA test case with $\delta t=2\times10^{-2}$".
- Table 5 lists Lobatto orders 2, 6 and 8 only, while Table 3 lists 2, 4, 6 and 8.
- §7.2: the reference solution is computed by "explicit 6th-order SDIRK integration". SDIRK is not explicit.
- §3.2 says "extract the real Schur decomposition as in Section 3.2" inside §3.2 itself (§3.1 is meant). §7.1.1 refers to itself ("in Section 7.1.1 we study") where Table 4 is meant.
- Isentropic vortex (p. 17): the $v$ component is printed with $-\frac{\epsilon((x-x_0)-\bar ut)}{2\pi r_c}$, whereas the standard rotating vortex has $+(x-x_0)$. This is likely a sign slip.
- Double shear layer initial condition: the $y>\pi$ branch lacks a closing parenthesis, and the parameters $\delta$ and $\rho$ are never given values ($\rho$ also clashes with density).
- Remark 4: "spectrum of $\hat L$ becomes dense in $[0,\infty)$" for symmetric negative semidefinite $\hat L$. Such a spectrum lies in $(-\infty,0]$.
- The abstract says "in all cases" 4th-order Gauss needs "roughly half" the SDIRK preconditioner applications. The tables give 36/59 = 0.61 (Table 3), 244/481, 161/365 and 75/177.
- Table 2 claims "the expected rates of convergence are observed", but Lobatto 2 has a first rate of 1.13 and Lobatto 4 has rates of 3.53 and 3.67.
- Typos: "Dalhquist" (§2.2), "equtions" (§7.1), "left left-hand term" (§7.2).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Mu'=\mathcal N(u,t)$ | $My'=f(t,y)$ | method-of-lines system with mass matrix $M$ (agrees) |
| $\delta t$ | $h$ | step size; the source's $h$ is the mesh spacing in §7.2 |
| $A_0=\{a_{ij}\}$, $b_0$, $c_0$ | $A$, $b$, $c$ | the subscript 0 frees $A$ for other uses |
| $k_i$ | $k_i=f(t_n+c_ih,Y_i)$ | **stage derivatives**, the unknowns of the solver; kept as $k_i$ where the solver acts on them |
| $L_i$, $L$ | $J$ at stage $i$ ($L$ in the linear case) | Newton or Picard linearization of stage $i$, fixed per block row |
| $\hat L_i:=\delta tM^{-1}L_i$ | $\bar L_i:=hM^{-1}L_i$ | **hat renamed**: in the registry the hat marks embedded quantities |
| $Q_0$, $R_0$ | $Q_0$, $R_0$ | real Schur factors, $A^{-1}=Q_0R_0Q_0^\top$ |
| $\eta\pm i\beta$, $\phi$ | same | eigenvalue pair of $A^{-1}$ and the off-diagonal entry of its $2\times2$ Schur block; $\phi$ (no subscript) is page-local, **not** the registry $\phi_k$ |
| $\gamma$, $\gamma_*$ | $\gamma_{\mathrm S}$ | **collision**: registry $\gamma$ is tree density or Rosenbrock diagonal; the source also uses $\gamma=1.4$ for the adiabatic index |
| $W(L)$ | $W(L)$ | field of values; $W(L)\le0$ means it lies in the closed left half plane |
| $\kappa(\cdot)$ | $\kappa(\cdot)$ | 2-norm condition number |
| $P_\gamma$, $\mathcal P_{\delta,\gamma}$ | $P_{\gamma_{\mathrm S}}$, $\mathcal P_{\delta,\gamma_{\mathrm S}}$ | preconditioned Schur-complement operators; $\delta>0$ is a free shift of Part I, Thm 1 (page-local) |
| $p$, $q$ | $p$, $q$ | order and stage order (agrees); the source's $p$ is also the DG degree in §7 |
| "Gauss $n$", "Radau $n$", "Lobatto $n$", "SDIRK $n$" | labelled by order | Gauss $2s$, Radau IIA $2s-1$, Lobatto IIIC $2s-2$ |
| $u,w$; $\mathcal G$; $\ell_i$ | differential and algebraic variables; constraint; algebraic stage derivatives | DAE, §6; **$\ell_i$ collides with the registry micro-step index $\ell$** and is page-local |
| $A$ (§7.2) | — | **collision**: the $H^1$ Laplacian, not the Butcher matrix |

# Reference list

The paper prints 51 references in numbered SIAM style ([1]–[51], alphabetical).
The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` this slug. No DOIs are printed. The preprints [12], [22], [37], [41]
and [46] (Part I) are kept as their own entries. Some items are printed
irregularly and were entered as printed: [25] Lesaint–Raviart appears as
"Lasaint"; [26] gives the author as "J. V. Lent"; [18] and [19] give the names
as "J. J. B. D. Swart" and "P. J. v. d. Houwen"; [50] has pages "557–557"; [45]
has "p. drw050"; [15] and [17] (Hairer–Wanner) have no publisher; [24] is a
technical report with no institution; [2] (MFEM) has no volume or pages.

# Pages created or updated

Chunk 1 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Irksome](/software/irksome.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Order reduction](/definitions/order-reduction.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stage order](/definitions/stage-order.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
