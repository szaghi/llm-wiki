---
type: Source
title: "Henshaw (1994) — A fourth-order accurate method for the incompressible Navier–Stokes equations on overlapping grids"
description: "Fourth-order finite-difference method of lines for incompressible Navier–Stokes on curvilinear overlapping grids: velocity–pressure form with the divergence-free boundary condition, ghost-point numerical boundary conditions, quartic Lagrange interpolation with two interpolation lines, divergence damping, and twilight-zone and exact-solution convergence tests in 2-D and 3-D (code CGINS)."
resource: "doi:10.1006/jcph.1994.1114"
source_kind: paper
authors: [Henshaw W.D.]
year: 1994
venue: "J. Comput. Phys. 113:13-25"
local_file: "/home/stefano/papers/mosaic/overset-chimera/1994_Crossref_Journal_of_Computational_Physics_Henshaw_A_Fourth-Order_Accurate_Method_for_the_Incompressible_Navier.pdf"
tags: [composite-grid, incompressible, high-order, finite-difference, interpolation]
timestamp: 2026-11-02T11:28:00Z
---

# Summary

Henshaw presents a method of lines for the time-dependent incompressible
Navier–Stokes equations on curvilinear
[composite overlapping grids](/definitions/composite-overlapping-grid.md) in
two and three dimensions, fourth-order accurate in space. This is the
founding high-order case of
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md).
The equations are solved in velocity–pressure form: momentum equations for
$\mathbf u$ coupled to a pressure Poisson equation. The paper argues that
the right extra boundary condition is $\nabla\cdot\mathbf u=0$ on
$\partial\Omega$. With it, the velocity–pressure form is equivalent to the
velocity–divergence form, and the normal momentum equation on the boundary
becomes a *numerical* boundary condition that gives a Neumann condition for
$p$. Fourth-order centred differences need two ghost lines. They are filled
by applying the momentum and pressure equations on the boundary, setting the
normal derivative of the divergence to zero, and extrapolating on the second
ghost line. Edges and vertices of 3-D grids get their own Taylor-series
treatment.

The velocity is advanced explicitly, and a pressure equation is solved at
each stage. Its singular discrete system is handled by a bordered system
with a compatibility multiplier of size $O(h^4)$. A divergence-damping term
is added to the pressure equation. Component grids are coupled by quartic
($q=5$, $5\times5\times5$) Lagrange
[inter-grid interpolation](/methods/inter-grid-interpolation.md) in the
donor's parameter coordinates, with two lines of interpolation points
([point classification](/definitions/point-classification.md)). This is the
width that the [interpolation-order requirement](/results/interpolation-order-requirement.md)
of Chesshire and Henshaw prescribes for fourth order. The timings separate
[explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md).

Fourth-order convergence is shown with [twilight-zone](/methods/twilight-zone-flow.md)
solutions on a square, a rotated square, a disc, a cube and a two-grid
spherical shell, and with Wannier's exact Stokes flow past a cylinder near a
moving wall. The divergence converges at rates 4.2–5.8. Demonstrations are
the [flow past a cylinder](/benchmarks/flow-past-circular-cylinder.md) at
$Re=100$ and the flow past a sphere in a channel. The code is CGINS, built on
grids from [CMPGRD](/software/cmpgrd.md).

# Version read

Version of record (Academic Press typeset), J. Comput. Phys. 113, 13–25
(1994), 13 pages. The scan is image-only, so all pages were read visually
and the equations checked on 300 dpi crops. The page-1 title and single
author match Crossref. The scan prints no DOI. The paper's own reference
[13] (Henshaw, IBM report RC 19361, 1994) is a different work with the same
author and year (see the reference list). Equation, table and page numbers
are those of the journal.

# Key claims

Registry notation: the source's $\nabla_4$, $\nabla_4\cdot$, $\Delta_4$ are
$\nabla_p$, $\nabla_p\cdot$, $\nabla^2_p$ with $p=4$; its Lagrange basis
$q_i(s)$ is $L_j(s)$; its $\mathbf r^I$ is $\mathbf r'$; its unit normal,
inward in §5.1.2, is the outward $\mathbf n$; its discrete divergence
$\delta_i$, its forcing $\mathcal D_i$ and the compatibility multiplier
$\alpha$ are written $\vartheta_{\mathbf i}$, $\mathcal T_{\mathbf i}$ and
$\varsigma$ here (page-local, as on
[incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)).

1. The scheme is fourth-order accurate in space on curvilinear overlapping grids in 2-D and 3-D, and its time accuracy is that of the chosen time stepper (abstract, §1). **Stated** (space order **Shown** in §5)
2. The natural extra boundary condition for the pressure equation is $\nabla\cdot\mathbf u=0$ on $\partial\Omega$. With it the velocity–pressure formulation (2) is equivalent to the velocity–divergence formulation (1) for smooth solutions (§1.2). **Stated** ("it is not hard to show"; no proof given)
3. If the extra condition is instead the normal component of the momentum equation, (2) is **not** equivalent to (1), since nothing then prevents a nonzero divergence inside the domain. That condition alone gives an under-determined system (citing Strikwerda) (§1.2). **Stated**
4. Essentially all methods impose $\nabla\cdot\mathbf u=0$ on the boundary, implicitly or explicitly. On staggered grids it occurs naturally, and Karniadakis et al. impose it by writing $\nabla^2\mathbf u=\nabla(\nabla\cdot\mathbf u)-\nabla\times(\nabla\times\mathbf u)$ and setting $\nabla(\nabla\cdot\mathbf u)=0$ (§1.2). **Stated**
5. Numerical boundary conditions: the momentum and pressure equations are applied on the boundary and $\partial_n(\nabla\cdot\mathbf u)=0$ is imposed; pressure and tangential velocity are extrapolated on the second ghost line (Eq. 3, §2). In 3-D this gives 12 equations for the 12 unknowns $(\mathbf U_{\mathbf i},P_{\mathbf i})$ at a boundary point and its two ghost points (§2). **Derived**
6. A second-order version exists that needs no extra numerical boundary conditions (§1.1). **Stated**
7. Pressure extrapolated in time, $P^*$, can be used in the tangential momentum boundary condition without affecting accuracy or stability, "from the theory" of the companion paper [18] (§3, Step 2). **Stated**
8. The discrete pressure system $\mathsf A\mathbf p=\mathbf b$ is normally singular. The bordered system (11) is nonsingular, and its multiplier $\varsigma=\mathbf l^T\mathbf b/\mathbf l^T\mathbf 1$ ($\mathbf l$ the left null vector) measures the violation of discrete compatibility and is expected to be $O(h^4)$ (Eqs. 11–14, §3). **Derived**
9. Inter-grid interpolation is quartic tensor-product Lagrange interpolation, $u^k_{\mathbf i}=\sum_{j_1,j_2,j_3=0}^{4}L_{j_1}(s_1)L_{j_2}(s_2)L_{j_3}(s_3)\,u^{k'}_{\mathbf i'+\mathbf j}$ on a $5\times5\times5$ stencil ($q=5$) in the donor's parameter coordinates, with $s_m=(r'_m-r_m(\mathbf i',k'))/\Delta r_m$ and $\mathbf i'$ the stencil corner. Fourth-order discretizations use two lines of interpolation points, an order chosen as in Chesshire and Henshaw (§4.1, §5.1). **Stated**
10. At a 3-D boundary edge, $\partial_{r_m}(\nabla\cdot\mathbf u)=0$ for $m=1,2$ and a diagonal sixth-difference extrapolation of the edge-parallel velocity fix the four ghost values outside the edge. At a vertex, a Taylor formula containing only tangential second derivatives gives the eight ghost values (Eqs. 15–17, §4.2). **Derived**
11. On a grid orthogonal to the boundary, the tangential and the normal ghost velocities decouple point by point, so no large system is solved. On non-orthogonal grids the solve is iterated in correction mode and converges quickly unless the grid is very skewed (§4.3). **Derived**/**Stated**
12. The discrete divergence $\vartheta_{\mathbf i}=\nabla_4\cdot\mathbf U_{\mathbf i}$ obeys a convection–diffusion equation forced by an $O(h^4)$ term $\mathcal T_{\mathbf i}$, with $\vartheta_{\mathbf i}=0$ and $D_{4n}\vartheta_{\mathbf i}=0$ on the boundary. Interpolation conditions also act as sources of divergence (§4.4). **Derived**
13. Adding $-C_d\nu\mathcal V_{\mathbf i}\vartheta_{\mathbf i}$, with $\mathcal V_{\mathbf i}=\sum_m\Delta x_{m,\mathbf i}^{-2}$, to the pressure equation adds linear damping $-C_d\nu\mathcal V_{\mathbf i}\vartheta_{\mathbf i}$ to the divergence equation. It reduces the discrete divergence but cannot make it zero; usually $C_d=1$ (§4.4, §5.1). **Derived** (no comparison with $C_d=0$ shown)
14. Initial data are projected: $\mathbf u_0=\mathbf u_I+\nabla\phi$ with $\nabla^2\phi=-\nabla\cdot\mathbf u_I$ and $\mathbf n\cdot\nabla\phi=0$. The discrete projection does not make the discrete divergence exactly zero, and for non-smooth data smoothing and projection alternate until the divergence stops decreasing (§4.5). **Stated**
15. Twilight zone on a square ($\nu=0.05$, $t=1$): errors in $\mathbf u$ of $1.2\times10^{-3}$, $2.5\times10^{-4}$, $7.9\times10^{-5}$ on $20^2$, $30^2$, $40^2$ grids; $\sigma=3.9$ for $\mathbf u$, $4.0$ for $p$, $5.6$ for $\nabla\cdot\mathbf u$ (Table I). **Shown**
16. Square rotated by $45^\circ$, same solution: $\sigma=4.2$, $3.5$, $5.8$ for $\mathbf u$, $p$, $\nabla\cdot\mathbf u$ (Table II). **Shown**
17. Disc of radius 1 on an overlapping grid ($35\times35\cup55\times11$ and $69\times69\cup109\times21$): $\sigma=4.0$, $4.0$, $4.3$ (Table III, Fig. 1). **Shown**
18. Stokes flow past a cylinder near a moving wall, against Wannier's exact solution, on $(27^2)\cup(9\times43)$ and $(53^2)\cup(17\times85)$: error in $\mathbf u$ from $7.3\times10^{-4}$ to $5.6\times10^{-5}$, $\sigma=3.7$; maximum divergence from $8.5\times10^{-3}$ to $3.8\times10^{-4}$, $\sigma=4.5$ (Table IV, Fig. 2). **Shown**
19. Flow past a cylinder at $Re=100$: the Kármán vortex street appears only after $t\approx40$, and the ratio of maximum divergence to maximum vorticity stays below about $3\times10^{-3}$ (§5.1.2, Figs. 3–5). **Shown**
20. Cylinder timings (IBM RS/6000-530, 14,581 points): 1.5 s/step, of which the pressure solve takes 27%, explicit interpolation 2%, the second-order Adams predictor–corrector 43% and the boundary conditions 7% (Table V). **Shown**
21. Twilight zone on a cube ($20^3$, $30^3$): $\sigma=4.3$, $4.4$, $5.4$ (Table VI). **Shown**
22. Spherical shell of radii $1/2$ and $1$ covered by two component grids (top and bottom halves), $t=0.5$: $\sigma=4.0$, $4.2$, $4.2$ (Table VII). **Shown**
23. Sphere in a channel on three grids, $(35^3)\cup(25^2\times9)\cup(25^2\times9)$, $\nu=0.05$: 45.0 s/step, with the GMRES pressure solve taking 42%, implicit interpolation 17%, the Adams predictor–corrector 28% and the boundary conditions 9%. The 10,728 interpolation points, a high fraction of all points, explain the interpolation cost (Table VIII, Fig. 6). **Shown**
24. Overlapping grids avoid coordinate singularities (a sphere covered by two or more patches has no poles) and the metric discontinuities of multiblock patched grids, which makes high-order accuracy easier to obtain (§1.2). **Stated**
25. The pressure equation can be solved by direct sparse, iterative sparse (biconjugate gradient squared, GMRES) or multigrid solvers (§3). **Stated**

# Printed slips

- §2 (p. 16): the second-derivative operator is printed $D_{4r_mr_m}\mathbf U_{\mathbf i}:=(-E^2_{+m}+16E_{+m}-30+16E_{-m}-E^2_{-m})\mathbf U_{\mathbf i}/(24(\Delta r_m)^2)$. Applied to $u=r^2$ it returns $1$ instead of $2$, so the denominator must be $12(\Delta r_m)^2$ *(compiler check, not in the sources)*.
- Eq. (17) (p. 19): $\mathbf u(-r_1,-r_2,r_3)=2\mathbf u(0,0,r_3)-\mathbf u(r_1,r_2,r_3)+\tfrac12r_1^2\mathbf u_{r_1r_1}+r_1r_2\mathbf u_{r_1r_2}+\tfrac12r_2^2\mathbf u_{r_2r_2}+O(\lvert r_1\rvert^4+\lvert r_2\rvert^4)$. Adding the Taylor expansions of $\mathbf u(\pm r_1,\pm r_2,r_3)$ gives twice these second-order coefficients, $r_1^2\mathbf u_{r_1r_1}+2r_1r_2\mathbf u_{r_1r_2}+r_2^2\mathbf u_{r_2r_2}$ *(compiler check, not in the sources)*. The vertex formula on the same page has the full coefficients. The text also says "Taylor series about (0, 0, 0)" while (17) expands about $(0,0,r_3)$.
- Eq. (7) (p. 17): the viscous term is printed $-\nu\nabla_4\mathbf U_i(t)$; the same condition on pp. 16 and 19 has $-\nu\Delta_4\mathbf U_i$.
- Eq. (3) (p. 14): the momentum line is printed "$\mathbf u_t+(\mathbf u\cdot\nabla)\mathbf u+\nabla p=\nu\Delta\mathbf u+\mathbf f\ =0$", with two equals signs.
- Wannier solution (p. 23): $k_1=x^2+(s+y)^2$ and $k_2=x^2+(s-y)^2$ use lowercase $s$, while $S=\sqrt{D^2-R^2}$ is defined and used elsewhere. $D$ denotes both the wall distance and the constant $D=-U$ in the same parameter list.
- Sphere case: §5.2 (p. 24) gives "a total of 47,550 active grid points"; Table VIII (p. 25) gives "Total number of grid points = 17,550".
- Table I: the printed pressure rate is $\sigma=4.0$, while a least-squares fit of the printed errors ($4.1\times10^{-3}$, $6.8\times10^{-4}$, $2.1\times10^{-4}$) against $h=1/N$ gives 4.3; the same fit reproduces the printed velocity (3.9) and divergence (5.6) rates *(compiler check, not in the sources)*. The fitting details are not stated, so this is an unexplained discrepancy, not a corrected value.
- Typos: "non-cocentric", "convergece", "this regions" (p. 22).

# Notation map

| Henshaw (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $G_k$, $k=1..n_g$; $\mathbf d_k(\mathbf r)$; $\mathbf r=(r_1,r_2,r_3)$ | $G_k$, $n_g$; $\mathbf x=\mathbf d_k(\mathbf r)$; $\mathbf r$ | agree |
| $i=(i_1,i_2,i_3)$ | $\mathbf i$ | |
| $n_{m,a,k}$, $n_{m,b,k}$ | page-local (boundary indices) | arrays extend two lines beyond |
| $\Delta r_m=1/(n_{m,b}-n_{m,a})$ | $\Delta r_m$ | |
| $\mathbf U_i$, $P_i$ | $\mathbf U_{\mathbf i}$, $P_{\mathbf i}$ (discrete $\mathbf u$, $p$) | |
| $E_{\pm m}$, $D_{\pm m}$ (undivided) | $E_{\pm m}$; undivided differences said so | |
| $D_{4r_m}$, $D_{4x_m}$, $D_{4n}$ | fourth-order difference operators, page-local | |
| $\nabla_4$, $\nabla_4\cdot$, $\Delta_4$ | $\nabla_p$, $\nabla_p\cdot$, $\nabla^2_p$, $p=4$ | |
| $\partial r_m/\partial x_n$ | $\partial r_m/\partial x_n$ | from CMPGRD |
| $\mathbf n$ (inward in §5.1.2) | $\mathbf n$ outward | **sign convention differs** |
| $\mathbf t_\mu$, $\mathbf u_B$, $P^*$ | page-local | |
| $\mathbf r^I$, $i_2$ (stencil corner), $s_m$ | $\mathbf r'$, corner of $\mathcal S_{\mathbf i}$, $s_m$ | |
| $q_i(s)$ | $L_j(s)$ | **collision**: registry $q$ is the interpolation width (here $q=5$) |
| $A$, $\mathbf P$, $\mathbf F$, $\mathbf r=[1,\dots,1]^T$, $\mathbf l$, $\alpha$, $\beta$ (Eq. 11) | $\mathsf A$, $\mathbf p$, $\mathbf b$, $\mathbf 1$, $\mathbf l$, $\varsigma$, $\beta$ page-local | **collisions**: $\mathbf r$ is the parameter coordinate, $\alpha$ the weights |
| $\alpha$ (Eq. 6, substep coefficient) | page-local | |
| $\delta_i$, $\mathcal D_i$, $C_d$, $\mathcal V_i$ | $\vartheta_{\mathbf i}$, $\mathcal T_{\mathbf i}$, $C_d$, $\mathcal V_{\mathbf i}$ page-local | **collisions**: registry $\delta$ is the Yin–Yang buffer angle, $\mathcal D_k$ the discretization points |
| $f$ (twilight-zone frequency) | page-local | **collision** with the forcing $\mathbf f$ |
| $\sigma$ | $\sigma$ | agree |
| $S,k_1,k_2,G,A,B,C,D,F,U,R$ | page-local (Wannier) | $G$ collides with grid symbols, $D$ is overloaded |
| $R_0$, $R_1$ | $r_{\mathrm{in}}$, $r_{\mathrm{out}}$ | spherical shell |

# Reference list

The paper prints 29 numbered references, almost all without titles, merged
complete into the [bibliography](/bibliography.md) with `citedby` including
this slug. Refs. [13], [14], [15] (Henshaw, IBM reports RC 19361, 19360,
19359, 1994) and [18] (Henshaw, Kreiss and Reyna, Comput. Fluids 23, 1994)
are other works by the same author and year. They are keyed
`henshaw-1994-b` to `henshaw-1994-e`, so that the plain key `henshaw-1994`
is this JCP paper. Ref. [21] (Kiris et al., "to appear") is kept as its own
pre-publication entry. Ref. [4] is a private communication (Brown, 1987).
Ref. [10] has no page printed. Ref. [12] (Harlow and Welch) is printed with
the venue "J. Comput. Phys. 8, 2182 (1965)" and recorded as printed; its
venue has not been checked on Crossref. There are no printed duplicates.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Patched (zonal) grids](/definitions/patched-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Incompressible flow on overlapping grids](/methods/incompressible-flow-on-overset-grids.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [CMPGRD and its solver suite (CGINS, CGNVT, CGES, CGMG, DSK)](/software/cmpgrd.md)
