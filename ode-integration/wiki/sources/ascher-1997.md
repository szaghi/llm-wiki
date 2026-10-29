---
type: Source
title: "Ascher et al. (1997) — Implicit-explicit Runge–Kutta methods for time-dependent partial differential equations"
description: "Constructs the Ascher–Ruuth–Spiteri IMEX Runge–Kutta pairs: an s-stage DIRK padded with a zero first row and column is coupled to an explicit method on shared abscissae; eight named (s,σ,p) pairs, a von Neumann test-equation stability study and advection–diffusion and multigrid experiments."
resource: "doi:10.1016/S0168-9274(97)00056-1"
source_kind: paper
authors: [Ascher U.M., Ruuth S.J., Spiteri R.J.]
year: 1997
venue: "Appl. Numer. Math. 25(2-3):151-167"
local_file: "/home/stefano/papers/mosaic/ode-integration/1997_Crossref_Applied_Numerical_Mathematics_Ascher_Implicit-explicit_Runge-Kutta_methods_for_time-dependent_par.pdf"
tags: [imex, additive, diagonally-implicit, stability, stiff, convection-diffusion]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

The paper constructs the implicit–explicit Runge–Kutta pairs now named after
its authors. The motivation is the authors' earlier finding that
[IMEX linear multistep schemes](/methods/imex-linear-multistep-methods.md)
restrict the step on convection–diffusion problems unless diffusion
dominates and a BDF-based scheme (SBDF) is used. For $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$,
with convection explicit and diffusion implicit, an $s$-stage
[DIRK](/methods/diagonally-implicit-runge-kutta.md) is padded with a zero
first row and column and coupled to an explicit method on the same
abscissae, so that one step alternates one implicit solve in $f^{\mathrm I}$ with one
evaluation of $f^{\mathrm E}$ ([IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)).
Two sub-families are singled out: equal weights ($b^{\mathrm E}=b^{\mathrm I}$), and a
[stiffly accurate](/properties/stiff-accuracy.md) implicit part whose last
row equals the weights, with the step result equal to the last stage.
Schemes are named $(s,\sigma,p)$: implicit stages, explicit stages, combined
order. Eight are printed: (1,1,1), (1,2,1), (1,2,2), (2,3,3), (2,3,2), (2,2,2),
(3,4,3) and (4,4,3).

[Linear stability](/definitions/stability-function.md) is studied on the
scalar test equation $y'=i\beta y+\alpha y$, which the paper takes from a
[von Neumann analysis](/definitions/von-neumann-stability-analysis.md) of
centred advection–diffusion. The second sub-family has no step restriction as
$\alpha\to-\infty$; the first keeps one, typically $h\beta<1$. Experiments on a
variable-coefficient advection–diffusion equation
([linear advection](/benchmarks/linear-advection-equation.md)), the viscous
[Burgers equation](/benchmarks/burgers-equation.md) and a 2D viscous
Burgers system with one multigrid solve per stage
([implicit stage solvers](/methods/implicit-stage-solvers.md)) support the
picture. The (1,2,2) pair applied to a separable Hamiltonian is shown to
coincide with leap-frog/Verlet ([symplecticity](/properties/symplecticity.md)).
The paper has no theorems: evidence is order-condition derivation (not
printed in full), test-equation analysis and experiments.

# Version read

Version of record (Elsevier typeset), pp. 151–167, 17 pages, all read;
every page with tableaux or tables was read visually because the text layer
garbles them. Title, authors, venue and year on page 1 match Crossref; the
printed PII matches the DOI. No received or accepted dates are printed.
Numbering cited here is that of the journal.

# Key claims

1. IMEX linear multistep schemes "tend to have undesirable time-step restrictions when applied to convection-diffusion problems, unless diffusion strongly dominates and an appropriate BDF-based scheme is selected" (Abstract; §1, citing Ascher, Ruuth & Wetton 1995). **Stated**
2. A dissipative IMEX multistep scheme for the hyperbolic term needs "order (or more accurately, backward steps) at least 3"; the stability region of explicit Runge–Kutta schemes "actually increases slightly when three- and four-stage schemes are contemplated" (§1). **Stated**
3. Since "the effective order of DIRK schemes drops to 1 for very stiff ODEs" (§1, citing Hairer & Wanner), the Runge–Kutta pairs are not expected to compete with SBDF when $f^{\mathrm I}$ is dominant and very stiff ([order reduction](/definitions/order-reduction.md)). **Stated**
4. The IMEX schemes are partitioned Runge–Kutta schemes for $y=v+w$ (Eq. 1.3) and "can also be seen as a particular class of splitting methods" (§1; [operator splitting](/methods/operator-splitting.md)). **Stated**
5. Scheme (2.1): an $s$-stage DIRK $(A^{\mathrm I},b^{\mathrm I},c)$ for $f^{\mathrm I}$, padded with a zero first row and column, and an explicit $(s+1)$-stage tableau with abscissae $(0,c)$ for $f^{\mathrm E}$; the shared abscissae "simplif[y] significantly the form of the order conditions … due to coupling" (§2). **Stated**
6. Sub-family (2): if the last explicit weight vanishes and the implicit weights equal the last implicit row and the explicit weights the last explicit row (Eq. 2.3), the implicit scheme is stiffly accurate with $c_s=1$ and the step result is the last stage (Eq. 2.4) (§2). **Derived**
7. With the Jacobian of $f^{\mathrm I}$ frozen at the step start, the stage matrix $I-ha^{\mathrm I}_{ii}\partial f^{\mathrm I}/\partial y$ is the same for all stages iff $a^{\mathrm I}_{ii}$ is constant; all recommended schemes are SDIRK "since there were sufficient excess degrees of freedom" (§2). **Stated**
8. (1,2,2), explicit midpoint with implicit midpoint, is second order; it "performs usually comparably to the unreasonably popular CNAB … and has better symmetry properties" (§2.3). **Stated**
9. On a separable Hamiltonian with $f^{\mathrm E}=(H_p,0)^\top$, $f^{\mathrm I}=(0,-H_q)^\top$, (1,2,2) is explicit, "can also be shown to be symplectic", and is identical to leap-frog/Verlet (§2.3, Example 2). **Derived** (identity), **Stated** (symplecticity)
10. The implicit part of (2,3,3), $\gamma=(3+\sqrt3)/6$, is "the two-stage, third-order DIRK scheme with the best damping properties" (§2.4, citing Hairer, Nørsett & Wanner, p. 207), with $R(z)\to1-\sqrt3\approx-0.7321$ as $z\to-\infty$; the pair is third order (§2.4). **Stated**
11. In (2,3,2), with $\gamma=(2-\sqrt2)/2$, the free explicit coefficient $\delta=-2\sqrt2/3$ matches the exponential to third order in the explicit stability function; the pair is second order (§2.5). (2,2,2) uses the same DIRK with $\delta=1-1/(2\gamma)$ and satisfies (2.3) (§2.6). **Derived**
12. In (3,4,3) the third-order conditions leave a two-parameter family in $a^{\mathrm E}_{42},a^{\mathrm E}_{43}$ (closed-form expressions for $a^{\mathrm E}_{31},a^{\mathrm E}_{32},a^{\mathrm E}_{41}$, §2.7); matching the exponential to fourth order gives "the same (desirable) stability region as all four-stage, fourth-order ERK schemes", with printed values $a^{\mathrm E}_{42}=a^{\mathrm E}_{43}=0.5529291479$, $a^{\mathrm E}_{31}=0.3212788860$, $a^{\mathrm E}_{32}=0.3966543747$, $a^{\mathrm E}_{41}=-0.105858296$; the DIRK has $\gamma=0.4358665215$, the middle root of $6x^3-18x^2+9x-1=0$ (§2.7). **Derived**
13. "No pair consisting of a three-stage, L-stable DIRK and a four-stage ERK satisfying (2.3) with a combined third-order accuracy could be found"; (4,4,3) uses a four-stage third-order L-stable DIRK with diagonal $\tfrac12$ and the free choices $c_1=c_3=\tfrac12$, $b^{\mathrm I}_4=\tfrac12$, $a^{\mathrm E}_{43}=\tfrac12$ (§2.8). **Stated** (search result)
14. On the test equation, (1,1,1) is unconditionally unstable on the imaginary axis and unconditionally stable with decay as $h\alpha\to-\infty$; (1,2,1) satisfies $\lvert y_n\rvert^2\le(1-(h\beta)^2+(h\beta)^4)\lvert y_{n-1}\rvert^2$ on the imaginary axis, stable iff $h\beta\le1$, and keeps this restriction as $h\alpha\to-\infty$ (§3). **Derived**
15. The sub-family (1) schemes (1,2,1), (1,2,2), (2,3,3), (2,3,2), (3,4,3) keep a step restriction as $\alpha\to-\infty$, "typically $k\beta<1$"; the sub-family (2) schemes (1,1,1), (2,2,2), (4,4,3) have none, like SBDF; (3,4,3) "suggests a potential advantage, in terms of allowable time steps, over a large range of parameter values" (§3, Figs. 1–2). **Shown**
16. Advection–diffusion $y_t+\sin(2\pi x)y_x=\nu y_{xx}$, large viscosity ($h=1.8\Delta x_0$, $\Delta x_0=1/63$): (3,4,3) and the (2.3) schemes allow the largest stable steps; on refining $\Delta x$ at fixed $h$ only the (2.3) schemes remain stable at $\Delta x_0/8$; at $h=5.4\Delta x_0$, (3,4,3) "is more accurate and stable in this example than the popular CNAB scheme with one-third the step size" (§4.1.1, Figs. 3–4). **Shown**
17. Small viscosity ($\Delta x=1/81$, $h=1.8\Delta x$, $0.001\le\nu\le0.01$): the errors of the third-order schemes and (2,3,2) are "always smaller than those arising for the two-step IMEX schemes considered in [2] even though twice the time step is applied" (§4.1.2, Fig. 5). **Shown**
18. Viscous Burgers gives "qualitatively similar results"; small $\nu$ needs upwinding (§4.2). **Stated** (no data printed)
19. 2D viscous Burgers system with multigrid V(1,1) cycles per stage (Table 1): strongly damping L-stable schemes need the fewest fine-grid iterations for large viscosity; weakly damping schemes need more because "lingering high-frequency modes necessitate more work on the finest grid", most visibly (1,2,2) (3.13, 3.29, 3.68 for $\nu=0.03,0.04,0.05$) (§5). **Shown**

# Printed slips

- §3, (1,1,1): "On the imaginary axis, $|u_n|\le(1+y^2)|u_{n-1}|$"; with $x=0$ the printed amplification factor $1+iy$ gives $\lvert u_n\rvert^2=(1+y^2)\lvert u_{n-1}\rvert^2$, so the printed bound holds but is not the modulus *(compiler check, not in the sources)*. The (1,2,1) inequality $|u_n|^2\le(1-y^2+y^4)|u_{n-1}|^2$ holds with equality: $\lvert1+iy(1+iy)\rvert^2=1-y^2+y^4$ *(compiler check, not in the sources)*.
- §2.4: "$R(\infty)=1-\sqrt3$" denotes the limit $z\to-\infty$.
- §5: Table 1 is introduced as "the average number of fine-grid iterations at each time step", while the discussion reads it per stage ("more than three iterations were required per stage when $\nu\ge0.03$").
- Footnote 4 (p. 160): "W. Hunsdorfer"; ref. [16] prints "W. Hundsdorfer".
- Ref. [5]: "M. Crouziex"; ref. [6]: "Seminarbereicht".
- The mesh Reynolds number $R=ah/\nu$ (footnote 5) and the stability function $R(z)$ share a letter.
- Example 1 assigns $f=(0,-H_q)^{\rm T}$, $g=(H_p,0)^{\rm T}$, Example 2 the opposite split of the same Hamiltonian.

# Notation map

| Ascher et al. (1997) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\dot u=f(u)+g(u)$ | $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$ | **the source's $f$ is the explicit part only**, not the full right-hand side |
| $k$ | $h$ | time step |
| $h$, $h_0$ | $\Delta x$, $\Delta x_0$ | **collision**: the source's $h$ is the mesh width |
| $t_{n-1}\to t_n$ | $t_{n-1}\to t_n$ | the step ends at index $n$ |
| $A=(a_{ij}),b,c$ | $A^{\mathrm I},b^{\mathrm I},c$ | unpadded $s$-stage DIRK |
| $\tilde A,\tilde b,\tilde c$ | padded $A^{\mathrm I},b^{\mathrm I},c$ | zero first row and column |
| $\hat A,\hat b,\hat c$ | $A^{\mathrm E},b^{\mathrm E},c^{\mathrm E}$ | **collision: the source's hat is the explicit tableau, the registry's hat is the embedded method**; $\hat c=\tilde c$ |
| $u_i$ | $Y_i$ | implicit stage $i=1,\dots,s$; explicit row $i+1$ pairs with it |
| $K_i$, $\hat K_i$ | $f^{\mathrm I}(Y_i)$, $f^{\mathrm E}(\cdot)$ | stage derivatives; $\hat K_1=f^{\mathrm E}(y_{n-1})$, $\hat K_{i+1}=f^{\mathrm E}(Y_i)$ |
| $s$, $\sigma$, $(s,\sigma,p)$ | $s$, — , — | implicit stages, explicit stages evaluated ($\sigma=s+1$ in sub-family (1), $\sigma=s$ in sub-family (2)), combined order |
| $\gamma$, $\delta$ | $\gamma$, $\delta$ (page-local) | DIRK diagonal and free explicit coefficient, values per scheme |
| $\alpha$, $\beta$; $x=k\alpha$, $y=k\beta$ | $\alpha$, $\beta$ (page-local); $h\alpha$, $h\beta$ | test equation $y'=i\beta y+\alpha y$; **$y$ collides with the solution** and is written $h\beta$ here |
| $R(z)$ | $R(z)$ | stability function; $R(\infty)$ is the limit $z\to-\infty$ |
| $g_u$ | $\partial f^{\mathrm I}/\partial y$ | |
| $\nu$ | $\nu$ (page-local) | viscosity; **collides with the registry's Courant number** |
| $v,w$, $\hat f,\hat g$ | — | partitioned form (1.3); this hat is neither explicit nor embedded |

# Reference list

The paper prints 16 references in numbered style ([1]–[16]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. Refs. [3], [7], [8] are books; ref. [6] is a seminar report
(Humboldt-Universität Berlin, 1978); ref. [13] a proceedings item without
pages. Spelling slips of refs. [5] and [6] are listed above. No DOIs are
printed; no printed duplicates; all items parsed.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Boundary conditions for Runge–Kutta stages](/methods/runge-kutta-stage-boundary-treatment.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [IMEX linear multistep and IMEX-BDF methods](/methods/imex-linear-multistep-methods.md)
* [Kennedy–Carpenter additive Runge–Kutta methods (ARK3, ARK4, ARK5)](/methods/kennedy-carpenter-ark-methods.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Order reduction](/definitions/order-reduction.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
