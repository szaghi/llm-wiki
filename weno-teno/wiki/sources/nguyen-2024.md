---
type: Source
title: "Nguyen et al. (2024) — Optimal transport for mesh adaptivity and shock capturing of compressible flows"
description: "Steady high-order HDG solver for compressible flows with shocks that alternates adaptive artificial-viscosity regularization (Helmholtz viscosity field, parameters reduced by homotopy under positivity and modal-smoothness constraints) with r-adaptive meshes from optimal transport, solving the Monge–Ampère equation by fixed-point HDG."
resource: "doi:10.1016/j.jcp.2024.113005"
source_kind: paper
authors: [Nguyen N.C., Van Heyningen R.L., Vila-Pérez J., Peraire J.]
year: 2024
venue: "J. Comput. Phys. 508:113005"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Nguyen_Optimal_transport_for_mesh_adaptivity_and_shock_capturing_of.pdf"
tags: [artificial-viscosity, moving-mesh, dg, shock-capturing, hypersonic, unstructured-mesh]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper combines two earlier ingredients of the same group in one solver for
steady compressible Euler and Navier–Stokes flows with shocks.

The first is adaptive viscosity regularization, a form of
[artificial viscosity](/methods/artificial-viscosity.md). The conservation law gets
a Laplacian artificial flux $\lambda_1\nabla\cdot(\mu(\eta)\nabla u)$. The viscosity
shape $\eta$ solves a Helmholtz equation whose source is the clipped negative
velocity divergence. The amplitude $\lambda_1$ and thickness $\lambda_2$ are lowered
by homotopy continuation as long as density and pressure stay positive and a modal
smoothness measure stays bounded. Positivity is thus an acceptance test, not a
limiter (contrast [bound preservation](/properties/bound-preservation.md)), and the
modal measure is a Persson–Peraire-type
[indicator](/definitions/troubled-cell-indicator.md) used as a constraint.

The second is r-adaptivity by optimal transport, which belongs with
[adaptive moving meshes](/methods/adaptive-moving-mesh.md). The mesh map is the
gradient of a convex potential that solves the Monge–Ampère equation with the second
boundary-value condition under equidistribution. The mesh density is a
Helmholtz-smoothed indicator built from the velocity divergence or the density
gradient. The Monge–Ampère equation is solved by a fixed-point hybridizable DG
(HDG) method, extended here to a mesh density given by piecewise polynomials on the
current mesh. Nodes move without new points or new connectivity. On polygonal
domains, boundary nodes may slide across faces and are then snapped to the corners.

The flow is discretized by HDG, a [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
variant, and the Helmholtz problems by continuous Galerkin, on isoparametric
elements of degree 4 (degree 3 in one case). The tests are all 2D: a
[supersonic bump channel](/benchmarks/supersonic-bump-channel.md), a transonic
[NACA 0012](/benchmarks/naca0012-airfoil.md), a double ramp at $M_\infty=3.6$, and
[hypersonic cylinders](/benchmarks/flow-past-circular-cylinder.md): inviscid at
$M_\infty=7$, an Edney type IV interaction at $M_\infty=8.03$, and viscous at
$M_\infty=17.6$. Sharp, oscillation-free solutions appear within two or three
adaptations, and only the adapted mesh reproduces the reference heat-transfer
coefficient. No error norms, orders, timings or iteration counts are given. Implicit
shock tracking ([HOIST, MDG-ICE](/methods/implicit-shock-tracking.md)) is reviewed
as an alternative.

# Version read

arXiv:2310.01196v1 [math.NA], 2 October 2023 (side stamp; footer "Preprint submitted
to arXiv, October 3, 2023"), 42 pages, all read; the equations of pp. 5–6 and 11–13
were checked on the page images. This is not the JCP version of record. Title and
author list match the published article. Section, equation and figure numbers on
this page are those of arXiv v1.

# Key claims

Registry notation where it applies. Page-local: $\eta$ the Helmholtz viscosity field
(not an entropy) and $\bar\eta=\eta/\lVert\eta\rVert_\infty$; $\lambda_1,\lambda_2$
the regularization amplitude and thickness; $\ell=h_{\min}$; $\phi_{\mathrm{MA}}$
the Monge–Ampère potential; $\varrho$, $\varrho'$ the source and target (mesh)
densities; $N=k$ the polynomial degree (see the Notation map).

1. Limiters (flux, slope, WENO-type) "pose implementation difficulties for implicit time integration schemes and high-order methods on complex geometries", so the paper uses artificial viscosity (§1). **Stated**
2. The group's earlier shock-aligned meshes, built by replicating shock curves along streamlines, are "not practical for complex geometries and shock patterns"; optimal transport replaces them (§1). **Stated**
3. The regularized system is $\nabla\cdot F(u,\nabla u)-\lambda_1\nabla\cdot\big(\mu(\eta)\nabla u\big)=0$, $\eta-\lambda_2^2\nabla\cdot(\ell^2\nabla\eta)-s(u,\nabla u)=0$, with $\eta=0$ on walls, $\ell=h_{\min}$; $\lambda_1$ sets the amplitude and $\lambda_2$ the thickness of the artificial viscosity (§2.2, Eqs. 5–7). **Stated** (method from earlier work)
4. The smoothed ramp $\mu(\bar\eta)$ of Eq. (8), with threshold $\bar\eta_T=0.2$, gives an artificial viscosity $\lambda_1\mu$ with $\mu\in[0,1-\bar\eta_T]$; $\bar\eta_T=0.2$ "is a sensible choice" (§2.2). **Stated**
5. The shock strength is $-\nabla\cdot v$, clipped smoothly at $s_{\max}=0.5\lVert\nabla\cdot v\rVert_\infty$ taken from the previous homotopy iterate (§2.2, Eqs. 9–11). **Stated**
6. The parameters solve $\min\lambda_1\lambda_2$ over $\lambda_1>0$, $\lambda_2\ge1$, $u$, $\eta$, subject to the discrete equations and $u\in\mathcal C$; the amount of artificial viscosity is "proportional to $\lambda_1\lambda_2$" (§2.2, Eq. 12). **Stated**
7. $\mathcal C$ requires $\rho>0$, $p>0$ and $\sigma(\lambda)\le C_0\sigma(\lambda_0)$ with $C_0=5$. Here $\sigma$ is the maximum, over the shock elements $\{K:\int_K\bar\eta\ge\bar\eta_T\lvert K\rvert\}$, of $\int_K\lvert\xi/\xi^*-1\rvert\,dx/\lvert K\rvert$, where $\xi$ is the density, the pressure or the local Mach number and $\xi^*$ its truncation to degree $N-1$ (§2.3, Eqs. 13–17). **Stated**
8. Homotopy: $\lambda_{n,1}=\zeta^{n-1}\lambda_{n-1,1}$, $\lambda_{n,2}=1+\zeta^{n-1}(\lambda_{n-1,2}-1)$, $\zeta\in(0,1)$, repeated until a constraint fails; the last admissible iterate is kept. $\lambda_{0,2}=1.5$ on uniform meshes, $5$ on shock-adapted ones (§2.4). **Stated**
9. The flow equations are discretized by HDG and the Helmholtz equations by continuous Galerkin, to obtain a continuous viscosity field (§2.5). **Stated**
10. By Brenier's theorem the optimal-transport problem has a unique optimal map, the gradient of a convex potential unique up to a constant, which gives the Monge–Ampère equation with the second boundary-value condition (§3.1, Eqs. 18–22). **Stated** (cited)
11. Equidistribution makes the source density the constant $\theta=\int_{\Omega'}\varrho'\,dx'/\lvert\Omega\rvert$ and gives $\varrho'(\nabla\phi_{\mathrm{MA}})\det(D^2\phi_{\mathrm{MA}})=\theta$, with $c(\nabla\phi_{\mathrm{MA}})=0$ on $\partial\Omega$ and $\int_\Omega\phi_{\mathrm{MA}}=0$ (§3.2, Eq. 23). **Derived**
12. The mesh density solves $\varrho'-\nabla\cdot(\ell^2\nabla\varrho')=b$ with $b=\sqrt{1+\beta_{\mathrm{OT}}\,s}$ (velocity divergence, Eq. 25) or $b=\sqrt{1+\beta_{\mathrm{OT}}\,g(\lvert\nabla\rho\rvert)}$ (density gradient, Eq. 26). The smoothing is needed for the Monge–Ampère discretization to converge (§3.3). **Stated**
13. The fixed-point HDG Monge–Ampère solver is extended to a mesh density given by piecewise polynomials on the current mesh. This needs the inverse of the isoparametric map, nonlinear for $N>1$, computed by Newton's method at every quadrature point (§3.4, Eqs. 27–34). **Derived**
14. The nodes are moved without new points or changed connectivity; the values of the new positions at duplicate DG nodes are averaged (§3.5, Algorithm 1, step 4). **Stated**
15. The homotopy runs only on the final adapted mesh, which "will considerably reduce the number of times we solve the compressible Euler/Navier-Stokes equations" (§3.5). **Stated** (no counts)
16. On the six-segment double-ramp boundary, enforcing the boundary condition face by face detaches the mesh at the corners (Fig. 5); "whether this phenomenon is a result of the HDG discretization or the formulation of Monge-Ampère on this domain remains to be determined". The fix lets boundary nodes slide between faces and then moves the vertex nearest each corner onto it (§4.2, Figs. 5–6). **Shown** (qualitative)
17. Because the map is the gradient of a scalar potential, the positions of chosen nodes cannot be fixed explicitly (§4.2). **Stated**
18. NACA 0012 ($M_\infty=0.8$, angle of attack $1.5^\circ$): the pressure-coefficient profiles converge fast, the second and third adapted meshes give very similar profiles, and the third is "very sharp at the shocks, yet there is no oscillation and overshoot" (§4.1, Figs. 2–4). **Shown**
19. Double ramp ($M_\infty=3.6$, degree 3, 909 elements): the Mach-number oscillations of the initial mesh disappear on the adapted mesh, and the shocks and the contact are sharper. The density-gradient indicator with $\beta_{\mathrm{OT}}=1$ refines along the contact, "which would be missed with the sensor based off the divergence of the velocity" (§4.2, Figs. 7–8). **Shown**
20. Inviscid cylinder ($M_\infty=7$, 900 quadrilaterals of degree 4): the mesh-density amplitude grows with adaptation, the artificial viscosity shrinks in amplitude and width, the profiles on $y=0$ converge (second and third meshes close), and the final mesh shows no oscillation or overshoot (§4.3, Figs. 9–12). **Shown**
21. Type IV shock–shock interaction ($M_\infty=8.03$, 2400 quadrilaterals of degree 4, two adaptations): the second adapted mesh resolves the impinging supersonic jet, the jet bow shock, expansions and shear layers that the initial mesh with the same element count misses, and its surface-pressure peak is higher and closer to the Wieting–Holden data (§4.4, Figs. 13–16). **Shown**
22. Viscous cylinder ($M_\infty=17.6$, $\mathrm{Re}=376{,}000$, $T_\infty=200$ K, isothermal wall at 500 K, 1500 quadrilaterals of degree 4, one adaptation): the pressure coefficient barely changes, but the heat-transfer coefficient is too low on the initial mesh and "agrees very well" with Gnoffo & White's LAURA results on the adapted one (§4.5, Figs. 17–22). **Shown**
23. The density-gradient indicator is "more effective" than the velocity-divergence one for flows with boundary layers, shear layers and expansion waves (§5). **Shown** (qualitatively, §§4.2–4.5)
24. Degree 4 is used from the start, without initialization from lower degrees (§4). **Stated**
25. Optimal transport also yields shock-aligned snapshots for stable reduced-order models (§5). **Stated** (cited)

*(Compiler check, not in the sources.)* The 2D Monge–Ampère system (29) writes
$\nabla\cdot q=f(H,q)=\sqrt{H_{11}^2+H_{22}^2+H_{12}^2+H_{21}^2+2\theta/\varrho'(q)}$.
For a symmetric Hessian, $(H_{11}+H_{22})^2=H_{11}^2+H_{22}^2+H_{12}^2+H_{21}^2+2\det H$,
and $\det H=\theta/\varrho'$ by Eq. (23), so $f$ is the positive root of
$(\Delta\phi_{\mathrm{MA}})^2$, consistent with convexity.

# Printed slips

- §2.4, homotopy update *(compiler check, not in the sources)*: with $\lambda_{n,1}=\zeta^{n-1}\lambda_{n-1,1}$ the first step ($n=1$) does not reduce $\lambda_1$, and the cumulative factor is $\zeta^{n(n-1)/2}$. The version of record was not checked.
- §2.2: "$\mu(\eta)$ vanish to zero when $\bar\eta\le\bar\eta_T$". *(Compiler check, not in the sources:)* Eq. (8) gives $\mu(\bar\eta_T)=\tfrac12-\arctan(100)/\pi=3.18\times10^{-3}$ and $\mu(0)=2.5\times10^{-6}$ for $\bar\eta_T=0.2$, so $\mu$ is small but not zero below the threshold, and $\mu(1)=0.80000006$ slightly exceeds $1-\bar\eta_T$.
- Eq. (6) is announced as "homogeneous Neumann boundary conditions" but contains the Dirichlet condition $\eta=0$ on the wall.
- Eq. (21) reads "$\nabla u(x)\in\partial\Omega',\ \forall x\in\Omega$"; Eq. (22) has $x\in\partial\Omega$.
- "$\Omega\in\mathbb R^d$", "$\Omega'\in\mathbb R^d$" (§2.1, §3.1) for $\subset$.
- §3.1 states the convexity of the Brenier potential as "$\Delta u(x)>0$", which is necessary but not equivalent to convexity for $d\ge2$.
- Eq. (32): the previous iterate is $q^{\ell-1}$ in the text and $q^{l-1}$ in the formula; the HDG spaces carry the degree as superscript $p$ in (30) and $k$ in (33)–(34).
- §4.4: "Boundary conditions are the same as those for the test case presented in Subsection 4.2"; §4.2 is the double ramp, §4.3 the inviscid cylinder.
- §5: "transonic, supersonic and supersonic flows", for "hypersonic" (cf. the abstract).
- Typos: "phenonema", "Monge-Amper̀e" (§4.2), "Navier-Sokes" (§2.2), "contraints" (§2.3), "reserach" (§5), "freastream" (§2.1), "freemstream" (§4.4); references "Reno, Neveda" [17], "Reston, Virigina" [16].
- Reference list: [16] and [61] print the same work (Nguyen & Peraire, AIAA 2011-3060), and so do [71] and [72] (Gnoffo & White, AIAA 2004-2371, [71] with "doi:doi:"). [39] dates Computers & Fluids vol. 98 to 2013, while [19] and [52] date the same volume to 2014.
- Not printed: $\gamma$, $\mathrm{Pr}$, $\zeta$, $\lambda_{0,1}$, $\beta_{\mathrm{OT}}$ (except for the double ramp), the smooth form of the clipping $g$, the stopping tolerance of Algorithm 1.

# Notation map

| Nguyen et al. 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$ (§2) | $u$ | conserved variables $(\rho,\rho v,E)$; the source writes $\rho E$ for $E$ |
| $u$ (§3) | $\phi_{\mathrm{MA}}$ (local) | **collision**: the same letter is the Monge–Ampère potential |
| $F$, $f_j$ | $f^{(j)}$ | physical flux; **collision**: $f_j$ is also the heat flux in (4) and $f(H,q)$ the Monge–Ampère right-hand side in (29) |
| $G=\mu(\eta)\nabla u$ | artificial flux (local) | **collision** with the admissible set $G$; $G$ is also an HDG test function in (34) |
| $\eta$, $\bar\eta$, $\bar\eta_T$ | viscosity field, normalized, threshold (local) | **collision** with the entropy $\eta$ |
| $\lambda=(\lambda_1,\lambda_2)$ | regularization amplitude and thickness (local) | **collision** with the eigenvalues $\lambda_l$ |
| $\mu(\eta)$ | smoothed ramp (local) | not the affine translation $\mu$; $\mu$ is also the HDG trace test function |
| $S=-\nabla\cdot v$, $s$, $s_{\max}$ | shock strength, clipped source (local) | **collision** with the source term $S(u)$ and the entropy $s$ |
| $\xi$, $\xi^*$ | sensor scalar and its degree-$(N-1)$ truncation (local) | **collision** with the reference nodes $\xi_j$; $\xi$ is also the reference coordinate in (27)–(28) |
| $\sigma$, $\sigma_K$, $C_0$ | modal smoothness measure (local) | not the affine scaling $\sigma$ |
| $\zeta$ | homotopy factor (local) | not the characteristic variables $\zeta$ |
| $k$ (also $p$ in (30)) | $N$ | polynomial degree of solution and geometry |
| $\varrho$, $\varrho'$ | source and target densities | $\varrho'$ is the mesh density, not the fluid density $\rho$ |
| $\phi=\nabla u$ | $\nabla\phi_{\mathrm{MA}}$ | optimal map |
| $\theta$ | equidistribution constant (local) | **collision** with the Zhang–Shu factor $\theta$ |
| $c(x)$ | boundary level-set function (local) | **collision** with the sound speed $c$ |
| $b$, $\beta$ | resolution indicator, $\beta_{\mathrm{OT}}$ (local) | not $\beta_k$ |
| $H$, $q$ | Hessian and gradient of the potential (local) | **collision** with the enthalpy $H$ and the weight exponent $q$; $q$ gives the new node positions |
| $\hat q_h$, $\hat u_h$, $\tau$ | HDG flux, trace, stabilization | **collision** with the WENO-Z indicator $\tau$ |
| $\mathcal T_h$, $\mathcal T_h^{\mathrm{shock}}$, $\mathcal T_h^*$ | mesh, shock elements, adapted mesh | |
| $M_\infty$, $Re$, $Pr$, $\gamma$ | $M_\infty$, $\mathrm{Re}$, $\mathrm{Pr}$, $\gamma$ | agree |
| $H=E+p/\rho$ (§2.1) | $H$ | specific total enthalpy; agrees |

# Reference list

The paper prints 75 references, numbered [1]–[75] in order of citation. The list is
merged complete into the [bibliography](/bibliography.md), with `citedby` including
`nguyen-2024`. Two printed duplicate pairs, [16]=[61] (Nguyen & Peraire, AIAA
2011-3060) and [71]=[72] (Gnoffo & White, AIAA 2004-2371), are each one work. [47]
(arXiv:2306.05296) and [74] (Van Heyningen et al. 2023, no venue) are preprints.
Cited Bai & Fidkowski 2022 (AIAA J.) and Nguyen, Terrana & Peraire 2022 (AIAA J.) are
different works from the ingested `bai-2022` and `nguyen-2022` and are keyed apart.
Same-author same-year works take suffixes in printed order (Nguyen 2023
[46]/[47]/[57]/[75], Kercher 2021 [44]/[45], Fernández 2018 [23]/[49]). No item is
unparseable.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunk 9 (2026-10-23). This source is cited on:

* [Adaptive moving mesh finite differences](/methods/adaptive-moving-mesh.md)
* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [NACA 0012 airfoil](/benchmarks/naca0012-airfoil.md)
* [Supersonic flow over a circular-arc bump](/benchmarks/supersonic-bump-channel.md)
