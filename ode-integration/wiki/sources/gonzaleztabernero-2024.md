---
type: Source
title: "González-Tabernero et al. (2024) — Boundary Treatment for High-Order IMEX Runge–Kutta Local Discontinuous Galerkin Schemes for Multidimensional Nonlinear Parabolic PDEs"
description: "Computes the boundary values of internal IMEX Runge–Kutta stages from the stage equations, the PDE and Lax–Wendroff conversion of time into space derivatives, for any IMEX tableau; this removes the order reduction from time-dependent Dirichlet data in LDG convection–diffusion–reaction tests at orders 3 and 4."
resource: "doi:10.1137/23m1612184"
source_kind: paper
authors: [González-Tabernero V., López-Salas J.G., Castro-Díaz M.J., García-Rodríguez J.A.]
year: 2024
venue: "SIAM J. Sci. Comput. 46:A3282-A3304"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_SIAM_Journal_on_Scientific_Computing_González-Tabernero_Boundary_Treatment_for_High-Order_IMEX_RungeKutta_Local_Disc.pdf"
tags: [imex, order-reduction, method-of-lines, runge-kutta]
timestamp: 2026-10-19T13:16:00Z
---

# Summary

The paper treats [order reduction](/definitions/order-reduction.md) of IMEX
Runge–Kutta time integration combined with a local discontinuous Galerkin (LDG)
discretization. The model problems are scalar convection–diffusion–reaction
equations on Cartesian domains with **time-dependent Dirichlet data**. Convection and
reaction are explicit and linear diffusion implicit, so the step restriction is
$h=\mathcal O(\Delta x)$. Imposing the boundary data naively at the stage times
creates numerical boundary layers and lowers the observed order to about 2 in the
maximum norm.

The contribution is a [boundary treatment for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
that computes the boundary value of every internal stage from the stage equation
itself:
- the diffusive term at the boundary is replaced through the PDE by the time
  derivative of the boundary data minus the explicit part;
- the stage equations are differentiated in $x$ to obtain the boundary derivative at
  each stage (Theorem 3.5, valid for any IMEX tableau);
- Taylor expansion in time and a Lax–Wendroff (Cauchy–Kovalevskaya) procedure turn
  time derivatives into space derivatives;
- these are approximated from the LDG polynomial, with finite differences across
  neighbouring cells for the highest derivative.

Algorithms 4.1–4.3 need only the two tableaux. They extend the
Wang–Zhang–Shu treatment (one third-order scheme, 1D linear) to nonlinear convection,
source terms, order 4 and 2D.

The tests are a 1D and a 2D linear convective heat equation and a 1D viscous
[Burgers equation](/benchmarks/burgers-equation.md) with source. They use a
third-order four-stage IMEX scheme and Kennedy–Carpenter ARK4(3)6L[2]SA. Without
the treatment the maximum-norm order is about 2 (about 2.25 in $L^2$, 2.5 in
$L^1$); with it the design order 3 or 4 is recovered in all three norms at
negligible extra cost. Space and time are refined together, and no convergence
theorem for the treated scheme is proved.

# Version read

Version of record (SIAM typeset, open access under CC BY 4.0), pp. A3282–A3304,
23 pages, all read; pp. A3290–A3302 were read visually because text extraction
scrambles the displayed equations. Title, authors, pages and DOI on page 1 match
Crossref. The supplementary sections SM1–SM3 (stage-by-stage derivations for §5) are
not in the file and were not read.

# Key claims

1. Imposing $u=\omega(t_n+c_ih)$ at the internal IMEX stages produces numerical boundary layers and order reduction (§1, Fig. 1; §2.2 citing [14]). **Stated** (and **Shown** in §5)
2. Diffusion-dominated problems force $h=\mathcal O(\Delta x^2)$ on explicit schemes; IMEX with implicit diffusion gives $h=\mathcal O(\Delta x)$ (§1). **Stated**
3. To the authors' knowledge, Wang–Zhang–Shu (2018) and Zhao–Huang (2020) are the only prior boundary treatments for IMEX schemes (§1). **Stated**
4. The novelties with respect to Wang–Zhang–Shu are the nonlinear case, source terms, orders above three, multidimensional problems and a general procedure for arbitrary IMEX LDG methods, claimed as the first of its kind (§1). **Stated**
5. Proposition 3.1: for $H$ of class $C^2$, $H(z(x,t+h),t+h)=H(z(x,t),t)+\mathcal O(h)$ for $z=u,u_x$, extendable to any order by more Taylor terms (§3, Remark 3.2). **Proved**
6. For the third-order scheme, the first-stage boundary value is $u^{n,1}=u_n+\gamma_{\mathrm I}h\big(f^{\mathrm E,n,0}+\partial_t\omega(t_n+c_1h)-f^{\mathrm E,n,1}\big)$, with $u_x^{n,1}$ from a first-order Taylor shift, which "ensures a third-order time approximation" (§3.1, Eqs. (3.4)–(3.5)). **Derived**
7. For a $p$th-order scheme only $p-1$ time derivatives of $u_n$ are needed when the stage value inside the explicit part is replaced by its Taylor expansion, because that part is multiplied by $h$ (§3.1, Eq. (3.6)). **Derived**
8. Remark 3.4: the boundary spatial derivatives multiply $h^2$, so for order $p$ they need accuracy $\mathcal O(\Delta x^{p-2})$ with $h=\mathcal O(\Delta x)$; $\hat u_x$ and $\hat u_{xx}$ come from the local LDG polynomial, but $\hat u_{xxx}$ must be rebuilt from neighbouring cells. **Derived**
9. Theorem 3.5 gives $u_x^{n,i}$ at any stage of any IMEX scheme in terms of $u_x^{n,1}$, the tableaux and Taylor-shifted derivatives of the explicit and implicit parts (§3.2). **Proved** (algebraic identity plus Taylor expansion)
10. Remark 3.6: a $p$th-order IMEX scheme needs a $(p-2)$th-order approximation of the spatial derivative; for $p\le3$ a first-order approximation suffices and the correction sums of Theorem 3.5 vanish. **Derived**
11. Algorithms 4.1–4.3 automate the treatment for any IMEX scheme given its tableaux; Algorithm 4.2 evaluates the explicit terms at their own stage times and Taylor-shifts the implicit derivative only from the preceding stage (§4). **Stated**
12. Algorithm 4.2 extends directly to structured multidimensional meshes (Algorithm 4.3) (§4). **Stated** (used in §5.3)
13. Solving the nonlinear boundary equation directly and Taylor-expanding the stage value give no substantial difference, nor do Algorithms 4.1 and 4.2 (§5). **Stated** (no table)
14. 1D linear convective heat equation, third order, CFL 0.25, $N=5\ldots640$: without treatment the orders tend to 2.52, 2.25, 2.00 in $L^1$, $L^2$, $L^\infty$; with it to 2.97, 2.99, 2.98, with $L^\infty$ error $1.44\times10^{-11}$ against $5.64\times10^{-9}$ (Table 1). **Shown**
15. Without treatment the pointwise error peaks at the boundaries (about $1.1\times10^{-5}$ at $t=h$, $N=160$); with it the peaks vanish (Fig. 4). **Shown**
16. 1D viscous Burgers with source, third order, CFL 0.4: without treatment 2.65, 2.26, 1.98; with it 3.01, 3.00, 3.00 (Table 2). **Shown**
17. 2D linear convective heat equation, third order, CFL 0.2, $N=M=5\ldots80$: without treatment about 2.53, 2.26, 1.96; with it 3.00, 2.99, 3.00 (Table 3). **Shown**
18. 1D linear convective heat equation, fourth order with ARK4(3)6L[2]SA, CFL 0.25, $N=5\ldots160$: without treatment 2.50, 2.26, 2.02; with it 3.98, 3.98, 3.95, with $L^\infty$ error $4.48\times10^{-14}$ against $3.24\times10^{-11}$ (Table 4). **Shown**
19. The fourth-order case needs one more Taylor term and third to fifth spatial derivatives at the boundary, the higher ones from first-order finite differences, and a second-order $u_{xxx}$ where it appears outside the Taylor expansion (§5.4, footnote 1). **Stated**
20. The extra cost of the treatment is negligible (work–precision diagrams, C++, Intel Core i7-1365U) (§5.5, Fig. 6). **Shown**
21. At equal CPU time the treated runs reach lower $L^2$ and $L^\infty$ errors than untreated ones; the untreated fourth-order curve lies close to the treated third-order curve (Fig. 6). **Shown**
22. The strategy applies to stiff sources treated implicitly and to explicit Runge–Kutta schemes as a special case (§1, §6). **Stated** (not tested)
23. The technique is independent of the spatial discretization (abstract, §1). **Stated**
24. Order reduction also affects ordinary (non-IMEX) Runge–Kutta methods (§1, citing [16, 18, 25]). **Stated**

# Printed slips

- §3.3, display after (3.10): "$\beta_3u_t^{n,3}$" uses an undefined $\beta_3$ (for $\gamma$), and the $\xi^{n,1}$ coefficient "$-(\alpha_2+\beta_2-1)$" should be $-(\alpha_2+\beta_1-1)$, as Eq. (3.11) carries.
- Algorithm 4.2 step 5 and Algorithm 4.3: "$\ldots+\tau\sum_{j=0}^{i-1}a_{ij}\hat\psi_x^{n,j}+a_{ii}\psi_x^{n,i}$" lacks the factor $\tau$ on the last term (compare Algorithm 4.1 and Theorem 3.5).
- §5.3: the exact solution is printed "$De^{-t}\sin(x+Ct)\cos(y+Ct)$" in the text and without $D$ in the Table 3 caption (they coincide for $D=1$).
- Proposition 3.1: "$H:\Omega\times[0,T]\to\Omega$"; the codomain cannot be the spatial domain.
- §1: citation list "[22, 23, 22, 25]" repeats [22].
- "Cauchy–Kovaléskya" (§1) and "Cauchy–Kovalévskaya" (§3) for Kovalevskaya.
- Fig. 6 caption: "the same data of Table 4", while §5.5 names Tables 1 and 4 and the markers run to $N=640$; the right panel prints "$L^*$ error".
- Remark 3.6 writes $\bar H(t^{n,j},t^{n,0})$, reversing the argument order of Theorem 3.5.
- §2.2: "$t^{n,1}=t+\gamma\tau$" uses $t$ for $t^n$.
- Table 3: the lower block header prints "$N$" where the upper prints "$N,M$".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau$ | $h$ | step size; the source's $h$ is the reaction term |
| $u_t=\xi(u,t)+\psi(u,t)$ | $y'=f^{\mathrm E}+f^{\mathrm I}$ | explicit (convection + source) and implicit (diffusion) parts |
| $\xi^{n,j}$, $\psi^{n,j}$ | $f^{\mathrm E,n,j}$, $f^{\mathrm I,n,j}$ (page-local) | stage evaluations; **$\xi$ also** denotes reference coordinates in §2.1 and the registry $B(\xi)$ argument |
| $\tilde A$, $\tilde b$; $A$, $b$ | $A^{\mathrm E}$, $b^{\mathrm E}$; $A^{\mathrm I}$, $b^{\mathrm I}$ | stage index from 0, $(s+1)\times(s+1)$ arrays; shared $c$ |
| $u^{n,i}$, $u^{n,0}=u^n$ | $Y_i$ ($Y_0=y_n$) | stage values; $s$ counts the stages after stage 0 |
| $t^{n,i}=t^n+c_i\tau$ | $t_n+c_ih$ | stage times |
| $\gamma$, $\alpha_1$, $\alpha_2$, $\beta_1$, $\beta_2$ | $\gamma_{\mathrm I}$ (page-local), others kept | third-order scheme coefficients; **collide** with the registry $\gamma$, $\alpha_{ij}$, $\beta_j$ |
| $\omega(x,t)$, $u_t^{n,i}$ | kept | Dirichlet data and its time derivative at $t_n+c_ih$ |
| $\hat u$, $\hat u_x$, … | kept | LDG solution and its derivatives; the hat does **not** mean embedded |
| $p$ | $p$ | order (combined space–time) |
| $k$ | kept | LDG degree **and** Taylor truncation index (overloaded); **collides** with the LMM step count |
| $C$, $D$, CFL | kept | convection speed, diffusion coefficient, $h/\Delta x$ |

# Reference list

The paper prints 29 references in numbered SIAM style ([1]–[29]) without DOIs. The
list is merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Same-key works take suffixes in printed order for Cockburn 1989 and
Zhao 2020; the two Wang 2016 items follow the keys already in the bibliography,
[22] `wang-2016-c` and [23] `wang-2016`. [8] (Cockburn 1998), [14] (Lubich &
Ostermann 1995) and [25] (Wang, Zhang & Shu 2018, the prior boundary treatment)
are `cockburn-1998-b`, `lubich-1995-b` and `wang-2018-b`, because the bibliography
already held other works under the plain keys. [4] is a book chapter whose editors are recorded in a note. [2]
(Calvo–de Frutos–Novo) is the source of the third-order IMEX scheme and [12]
(Kennedy–Carpenter 2003) of ARK4(3)6L[2]SA. No printed duplicates and no
unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Order reduction](/definitions/order-reduction.md)
