---
type: Source
title: "Bader & Zhu (2025) — AFiD-MHD: A finite difference method for magnetohydrodynamic flows"
description: "Code paper extending the staggered second-order finite-difference solver AFiD to incompressible Boussinesq MHD in a plane layer, with three exact discrete treatments of the solenoidal constraint: a staggered projection cleaning, a Lagrange-multiplier projection and a Coulomb-gauge vector potential."
resource: "doi:10.1016/j.jcp.2024.113658"
source_kind: paper
authors: [Bader S.H., Zhu X.]
year: 2025
venue: "J. Comput. Phys. 523:113658"
local_file: "/home/stefano/papers/mosaic/weno-teno/2025_Crossref_Journal_of_Computational_Physics_Bader_AFiD-MHD_A_finite_difference_method_for_magnetohydrodynamic.pdf"
tags: [mhd, finite-difference, software, performance]
timestamp: 2026-10-23T15:06:00Z
---

# Summary

The paper extends AFiD, a pencil-decomposed second-order staggered finite-difference
code for wall-bounded incompressible convection, to incompressible Boussinesq MHD in a
plane layer: rotating plane-layer dynamos and quasi-static magnetoconvection. It is
peripheral to this bundle. There is no shock capturing, nonlinear reconstruction or
compressible flux; its contact with the bundle is the discrete
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

Velocity and magnetic field (or vector potential) components sit at face centres, and
the grid is stretched in the wall-normal direction through a coordinate map. Time
integration is the fractional-step three-substep Runge–Kutta of Rai & Moin, with
Crank–Nicolson for the wall-normal diffusion only. The paper calls it "third-order
RK" and does not present it as a strong-stability-preserving scheme (compare
[SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)). Poisson problems are
solved by FFT in the periodic directions and a tridiagonal solve in the wall-normal
one.

Three treatments of $\nabla\cdot B=0$ are implemented. SDCM-Stag is a
Brackbill–Barnes projection cleaning whose Laplacian is the composition of the same
discrete divergence and gradient used elsewhere, so the cleaned field is divergence
free to round-off and the odd–even decoupling of the collocated version is avoided. A
Lagrange-multiplier projection adds a pseudo-pressure to the induction equation. A
vector-potential form $B=\nabla\times\mathcal A$ with Coulomb gauge has a
discrete divergence that cancels identically.

Evidence is numerical: temporal convergence of $B_1$ (fitted order 2.74 for both
projections), $\max\lvert\nabla\cdot B\rvert$ near $10^{-15}$ against $10^{-5}$
without cleaning, closed energy budgets, agreement of Nusselt and Reynolds numbers
with Stellmach & Hansen (2004) and Yan et al., and strong scaling on $2048^3$ points
to 6000 cores.

# Version read

Version of record (Elsevier typeset, open access; received 17 May 2024, accepted 3
December 2024, online 6 December 2024), 21 pages, all read; pp. 6, 7, 8, 13 and 14
read on the page images, where the text extraction drops the calligraphic operator
letters. Page 1 matches Crossref (title, two authors, venue, DOI). Numbering cited
here is that of this version.

# Key claims

Registry notation: the source's $\mathbf u$, $\mathbf b$, $\mathbf a$ are $v$, $B$,
$\mathcal A$; its vertical (wall-normal) coordinate $x$ is $x_1$, with periodic
$x_2,x_3$. Page-local: $\mathsf G$, $\mathsf D$, $\mathsf L$ the discrete gradient,
divergence and Laplacian (source $\mathcal G$, $\mathcal D$, $\mathcal L$); $\psi_B$
the cleaning potential (source $\psi$); $g_x$ the grid metric; $\mathrm{Ra}$, $\mathrm{Pm}$,
$\mathrm{Ek}$, $Q$ the Rayleigh, magnetic Prandtl, Ekman and Chandrasekhar numbers.

1. Velocity, magnetic field and vector potential are discretized on a staggered grid by a conservative second-order centred finite-difference scheme, after Verzicco & Orlandi and AFiD (§3.1, Abstract). **Stated**
2. Wall-normal stretching is handled by a map with metric $g_x=\delta x/\delta\tilde x$, keeping $\mathcal O(\Delta\tilde x^2)$ first and second derivatives (Eqs. (3a)–(3c)); differences taken directly on a non-uniform grid "result in the loss of accuracy of one order" (§3.1). **Stated**
3. Wall ghost values use linear extrapolation ($f_G=-f_{3/2}$ Dirichlet, $f_G=f_{3/2}$ Neumann), justified by the absence of shocks in Boussinesq problems (§3.1, Eqs. (4a)–(4b)). **Stated**
4. Time stepping is the fractional-step RK3 with $\gamma=[8/15,5/12,3/4]$, $\rho=[0,-17/60,-5/12]$ and "$\alpha=\gamma+\rho=[4/15,1/15,1/6]$"; convection, Lorentz, Coriolis and horizontal viscous terms are explicit, the wall-normal viscous term Crank–Nicolson (§3.2, Eqs. (5)–(9)). **Stated** (see Printed slips)
5. Implicit horizontal diffusion "becomes unnecessary at large Rayleigh numbers"; dropping it leaves the Poisson solve as the only global communication (§3.2, §4). **Stated**
6. The collocated SDCM stencil (Eq. (13)) couples each cell only with every other cell and is prone to odd–even (checkerboard) decoupling; the adjacent-cell fix is not exact (§3.3.1). **Stated** (cited)
7. SDCM-Stag (Eq. (14)): with $\psi_B$ at cell centres and $B$ on faces, the Laplacian is $\mathsf D\mathsf G$ with the same $\mathsf D$ that measures $\nabla\cdot B$, so the cleaned field $B+\mathsf G\psi_B$ has zero discrete divergence and no checkerboard instability (§3.3.1, Fig. 4b). **Derived**
8. For the projection methods the Lorentz force and the induction term are written in divergence form, with the $(\nabla\cdot B)B$ term neglected and $\lvert B\rvert^2/2$ absorbed into the modified pressure (Eqs. (10a)–(10b)). **Derived**
9. Perfectly conducting walls give $\partial_1\psi_B=0$ (Eq. (22)); pseudo-vacuum walls would need a second-derivative condition, and "a slight error" in the $\psi_B$ boundary condition "may result in the large" $\nabla\cdot B$ "errors near the boundaries" (§3.3.3). **Stated**
10. With the Coulomb gauge $\nabla\cdot\mathcal A=0$ enforced by an extra projection, the term $\nabla(\nabla\cdot\mathcal A)$ of the current is dropped, avoiding cross-derivative stencils (§3.3.4). **Stated**
11. The vertex divergence (Eq. (25)) of the edge-centred $B=\nabla\times\mathcal A$ (Eqs. (26a)–(26c)) is a sum of twelve terms that "cancel each other in pairs", so it vanishes to round-off (Eq. (27)). **Derived**
12. The Alfvén time-step limit is $\Delta t\le(\mathrm{CFL})_A\min\big(\sum_d\lvert B_d\rvert/\Delta x_d\big)^{-1}$ (Eq. (29)); explicit horizontal magnetic diffusion gives $\Delta t\sim\mathcal O(\mathrm{Rm}\,\delta_h^2)$, $\mathrm{Rm}=\mathrm{Pm}\sqrt{\mathrm{Ra}/\mathrm{Pr}}$, $\delta_h$ the horizontal spacing (Eq. (30), §4). **Stated** / **Derived**
13. Strong scaling on $2048^3$ points up to 6000 cores has least-squares slope $-0.87$; the three cleaning variants cost about one extra Poisson solve each and are "expected to be practically similar" (§4, Fig. 5). **Shown** / **Stated**
14. Temporal convergence of the $L^2$ error of $B_1$ ($128^3$, reference $\Delta t=10^{-4}$, test steps $n\times10^{-3}$, $n=1,2,4,8$): fitted order 2.74 for both SDCM-Stag and the Lagrange-multiplier projection, with identical errors; the authors call 2.74 "very close to the order of the base scheme (third-order RK)" and conclude that the projection hardly affects the order, in line with Tóth (§5.1, Fig. 6). **Shown** (the paper itself calls Crank–Nicolson "second-order accurate", §3.2)
15. SDCM-Stag is preferred because the Lagrange multiplier is pressure-like and "suffers from the same fate of reduced order of accuracy as hydrodynamic pressure does" (§5.1, citing Brown et al.). **Stated** (the accuracy of the multiplier is not measured)
16. From a random non-solenoidal field ($\max\lvert\nabla\cdot B\rvert=\mathcal O(1)$), SDCM-Stag reduces $\max\lvert\nabla\cdot B\rvert$ "by 15 orders of magnitude, down to the machine zero"; without cleaning it settles near $10^{-5}$ (§5.1, Fig. 7). **Shown**
17. The total energy budget closes (residual two to three orders below the leading terms), and the three Nusselt estimates oscillate about a common mean for both projections (Figs. 8–9). **Shown**
18. Dynamo statistics agree with Stellmach & Hansen, e.g. case 1 $\mathrm{Nu}=1.74$ (1.71), $\mathrm{Re}=44.8$ (44.2), $E_{\mathrm{mag}}/E_{\mathrm{kin}}=0.61$ (0.62) (Table 1). **Shown**
19. Vector-potential runs with pseudo-vacuum walls keep $\nabla\cdot B$ near machine zero and give Nusselt numbers within 1–2 % of Yan et al. (Figs. 12–13). **Shown**
20. Quasi-static magnetoconvection at $Q=10^6$ gives Nusselt numbers within 0.44, 0.34 and 0.09 % of Yan et al. at $\mathrm{Ra}=1.1\times10^7$, $4\times10^8$, $10^9$ (Table 2); near onset the number of critical wavelengths "match reasonably well" linear theory (Fig. 16). **Shown**

# Printed slips

- §3.2: "$\alpha=\gamma+\rho=[4/15,1/15,1/6]$". *(Compiler check, not in the sources: from the printed $\gamma$ and $\rho$, $\gamma+\rho=[8/15,2/15,1/3]$; the printed values are $(\gamma+\rho)/2$, so the formula or the values are mis-stated.)*
- Eq. (32): $\partial_t\langle\lvert B\rvert^2/2\rangle_V=-\langle(j\times B)\cdot v\rangle_V$ is printed without the Ohmic term, although the next line defines $\langle\epsilon_\eta\rangle_V$ and Eq. (33), the sum of (31) and (32), contains $-\langle\epsilon_\eta\rangle_V$ (checked on the page image, p. 13).
- Eq. (17): the diffusion term is printed $-\frac1{\mathrm{Pm}}\sqrt{\mathrm{Pr}/\mathrm{Ra}}\nabla^2B$. *(Compiler check, not in the sources: for solenoidal $B$, $\nabla\times j=\nabla\times\nabla\times B=-\nabla^2B$, so Eq. (1c) gives $+\frac1{\mathrm{Pm}}\sqrt{\mathrm{Pr}/\mathrm{Ra}}\nabla^2B$.)*
- Thermal dissipation: §5.1 defines $\langle\epsilon_\kappa\rangle_V=\sqrt{\mathrm{Pr}/\mathrm{Ra}}\langle\lvert\nabla\theta\rvert^2\rangle_V$, §5.2 $(1/\sqrt{\mathrm{Ra}\,\mathrm{Pr}})\langle\lvert\nabla\theta\rvert^2\rangle_V$. *(Compiler check, not in the sources: the diffusivity of Eq. (1b) is $1/\sqrt{\mathrm{Ra}\,\mathrm{Pr}}$, so the §5.2 form is the consistent one.)*
- Table 1, case 1: $\mathrm{Re}_m=112.2$ with $\mathrm{Re}=44.8$, $\mathrm{Pm}=2.5$. *(Compiler check, not in the sources: if $\mathrm{Re}_m=\mathrm{Pm}\,\mathrm{Re}$, which the definition is not printed for but the other rows satisfy, $2.5\times44.8=112.0$.)*
- Typos: "located ot the cell-centers" (§3.3.1), "two types are BCs" (§3.3.3), "Lagragian" (Fig. 9 caption), "in a n alternative" (§6), "bouyancy" (§3.1).
- Not printed: the aspect ratio of the dynamo cases of Table 1.

# Notation map

| Bader & Zhu | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u$, $\mathbf b$, $\mathbf j=\nabla\times\mathbf b$ | $v$, $B$, current (local) | incompressible Boussinesq, dimensionless |
| $\mathbf a$, $\Pi_a$ | $\mathcal A$ (§10), gauge scalar (local) | **collision** with the THINC $\mathcal A$ |
| $x$ (vertical); $y$, $z$ | $x_1$; $x_2$, $x_3$ | wall-normal is $x$ |
| $p$, $\phi$ | modified pressure and its increment | absorbs $\lvert B\rvert^2/2$ |
| $\psi$ | $\psi_B$ (local) | **collision** with the entropy potential $\psi$ |
| $p_b$, $\phi_b$ | Lagrange multiplier and increment (local) | |
| $V$ | electric potential (local) | |
| $\theta$ | temperature (local) | **collision** with the Zhang–Shu $\theta$ |
| $\mathcal G$, $\mathcal D$, $\mathcal L$, $\mathcal L_x$ | $\mathsf G$, $\mathsf D$, $\mathsf L$ (local) | **collision** of $\mathcal G$, $\mathcal L$ with the global flux and the semi-discrete operator |
| $\tilde x$, $g_x$ | computational coordinate, metric (local) | |
| $\gamma$, $\rho$, $\alpha$ (RK3 coefficients) | substep coefficients (local) | **collision** with $\gamma$, $\rho$, $\alpha$ |
| $\epsilon_\nu$, $\epsilon_\eta$, $\epsilon_\kappa$ | viscous, Ohmic, thermal dissipation (local) | |
| $Ra$, $Pr$, $Pm$, $Ek$, $Q$, $Rm$, $Re_m$ | dimensionless groups (local) | $\mathrm{Pr}$ as in the registry |
| $(CFL)_A$, $\mathbf v_A=\mathbf b$ | Alfvén CFL number, Alfvén velocity | not the registry $\nu$ |
| $E_{mag}/E_{kin}$, $Nu$, $Re$ | $E_{\mathrm{mag}}/E_{\mathrm{kin}}$, $\mathrm{Nu}$, $\mathrm{Re}$ (local) | magnetic-to-kinetic energy ratio, Nusselt and Reynolds numbers; $E_{\mathrm{mag}}$ is not the total energy $E$ |
| PC, PV | perfectly conducting, pseudo-vacuum walls | |

# Reference list

The paper prints 57 references, numbered [1]–[57]. The list is merged complete into
the [bibliography](/bibliography.md), with `citedby` including `bader-2025`.
Same-author same-year works are suffixed in printed order (three Zhu et al. 2018 and
two Bader & Zhu 2023 items, one of them a conference abstract). The classical
divergence-control references (Brackbill & Barnes, Evans & Hawley, Powell et al.,
Tóth, Dedner et al., Balsara & Kim) are matched to the existing entries by
volume and page. Ref. [31] is a book chapter printed without editors or publisher and
ref. [11] without pages; no item is unparseable.

# Pages created or updated

Chunk 9 (2026-10-23). This source is cited on:

* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
