---
type: Source
title: "Banks et al. (2016) — An added-mass partition algorithm for fluid–structure interactions of compressible fluids and nonlinear solids"
description: "Extends the added-mass partitioned (AMP) fluid–structure algorithm to compressible fluids coupled with nonlinear hyperelastic solids, with interface states from a fluid–solid Riemann problem as impedance-weighted averages, both domains discretized on deforming composite overlapping grids regenerated every step with Ogen in Overture."
resource: "doi:10.1016/j.jcp.2015.10.043"
source_kind: paper
authors: [Banks J.W., Henshaw W.D., Kapila A.K., Schwendeman D.W.]
year: 2016
venue: "J. Comput. Phys. 305:1037-1064"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2016_Crossref_Journal_of_Computational_Physics_Banks_An_added-mass_partition_algorithm_for_fluidstructure_interac.pdf"
tags: [composite-grid, moving-grid, compressible, shock-capturing, fsi]
timestamp: 2026-11-02T14:53:00Z
---

# Summary

Banks, Henshaw, Kapila and Schwendeman extend their added-mass partitioned (AMP) algorithm, which
coupled an inviscid compressible fluid with a linearly elastic solid, to nonlinear hyperelastic
solids (Saint Venant–Kirchhoff and neo-Hookean) undergoing large rotations and displacements. The
paper is a [fluid–structure interaction](/methods/fluid-structure-interaction-on-overset-grids.md)
paper; overlapping grids are its discretization ingredient, not its contribution.

The fluid (Euler equations) is solved on moving mapped grids by a second-order Godunov scheme with a
Roe solver, the [shock-capturing](/methods/shock-capturing-on-overset-grids.md) scheme of the
group's earlier moving-grid work. The solid is solved in Lagrangian reference coordinates as a
first-order system for displacement, velocity and nominal stress by a new second-order
characteristic upwind scheme. Both domains live on
[composite overlapping grids](/definitions/composite-overlapping-grid.md). The component grids next
to the fluid–solid interface deform with it: after each step a hyperbolic grid generator
regenerates them, and Ogen recomputes the [domain connectivity](/definitions/domain-connectivity.md)
([hole cutting](/methods/hole-cutting.md) and receptor points), all within
[Overture](/software/overture.md). These "deforming composite grids" are a case of
[moving overset grids](/methods/moving-overset-grid.md).

The central result is a linearized fluid–solid Riemann problem in the interface-normal direction.
It gives the interface normal velocity and traction as impedance-weighted averages of the predicted
fluid and solid states. A simplified projection replaces the effective solid impedance with the
linear p-wave impedance. Unlike the traditional partitioned (Dirichlet–Neumann) scheme, the AMP
scheme stays stable for light solids, where added-mass effects are large. The traditional scheme is
unstable for the medium and light solids of the rotating-disk test.

Verification uses a manufactured solution on an elastic piston (the
[twilight-zone](/methods/twilight-zone-flow.md) technique, here called the method of analytic
solutions) and a rotating elastic disk compared with a fine 1-D reference; both give second-order
rates. Demonstrations: a Mach-1.3 planar shock hitting a light elliptical solid, and a light
flexible beam bent by a Mach-1.1-driven cross flow. The introduction cites
[store separation](/benchmarks/store-separation.md) as the early application of overlapping grids
to rigid moving bodies. The paper does not state the [inter-grid
interpolation](/methods/inter-grid-interpolation.md) width or order; it defers to earlier papers.

# Version read

The Elsevier typeset version of record, J. Comput. Phys. 305 (2016) pp. 1037–1064, 28 pages, all
read; the text layer is clean, and pages 7–8, 11–13 and 26 were checked visually. Page 1 matches
Crossref in title, author order and DOI. Section and equation numbers below are those of this
version.

# Key claims

1. The AMP algorithm, with either the full or the simplified interface projection, is stable even
   for light solids, where added-mass effects are large. (Abstract, §5.2, §8) **Shown**
2. The fluid–solid Riemann problem gives the interface states as impedance-weighted averages of the
   fluid and solid states, of the same form as for linear solids. (Abstract, §3.2, Eq. (28))
   **Derived**
3. Full AMP projection: with fluid impedance $z=\rho_0a_0$, effective solid impedance $\bar z$
   and coupling coefficient $\bar k$ (Eq. (27)), predicted fluid and (rotated, scaled) solid
   normal velocities $v$, $\bar v$ and normal tractions $\tau$, $\bar\tau$, and solid tangential
   traction $\bar\tau_t$,
   $v^I=\dfrac{\bar z\bar v+zv}{\bar z+z}+\dfrac{\tau-\bar\tau}{\bar z+z}+\dfrac{\bar k\bar\tau_t}{\bar z+z}$,
   with the analogous traction formula. (§3.2, Eqs. (26)–(28)) **Derived**
4. The simplified projection drops $\bar\tau_t$ (zero to truncation-error level, because a zero
   tangential traction is enforced each step) and replaces $\bar z$ by the linear p-wave impedance
   $\bar\rho\bar c_{\mathrm p}$, $\bar c_{\mathrm p}=\sqrt{(\bar\lambda+2\bar\mu)/\bar\rho}$, which is justified
   when the deformation gradient is a small perturbation of a rotation. (§3.2, Eq. (29)) **Derived**
5. Both projections have the same formal order, being linear combinations of the interface
   conditions with different weights; the simplified one is cheaper and in all tests no less
   stable. (§3.2) **Stated** (order), **Shown** (stability)
6. Unlike the one-sided Riemann problem of Farhat et al. (a traditional partitioned treatment), the
   AMP projection is two-sided; for very light solids the interface position and velocity are set
   by the fluid. (§1) **Stated**
7. The interface projection imposes no time-step restriction; $\Delta t$ is the minimum of the fluid
   and solid steps. (§4.2) **Stated**
8. The 2-D solid system has eight eigenvalues, four wave speeds and four zeros (the tangential
   stresses and the two displacement components). Upwinding does not damp the zero-speed
   components, which can produce weak instabilities at grid overlaps; fourth-order dissipation
   cures them. (§4.2, Eqs. (38)–(40)) **Stated**
9. The fourth-order dissipation adds $O(\Delta r_m^4/\Delta t)=O(\Delta r_m^3)$, below the
   second-order truncation error; its coefficient is typically $1/2$. (§4.2) **Derived**
10. A stress–strain relaxation term adds $O(\Delta r_m^4/\Delta t)$ for an $O(1)$ coefficient,
    reduces stress errors and, with the conservative momentum equation, mitigates the
    non-conservative form of the stress equation in shock impacts. (§1, §4.2) **Stated**
11. The solid scheme and the whole fluid–structure scheme on deforming composite grids are
    free-stream preserving. (§4.2) **Stated**
12. The time step comes from an elliptical approximation of the absolute-stability region with
    semi-axes $2$ (real) and $1$ (imaginary), giving a quadratic bound (Eq. (45)) and
    $\Delta t_{\max}=(-b+\sqrt{b^2-4ac})/(2a)$, times a safety factor of about 0.9. (§4.2,
    Eqs. (44)–(45)) **Derived**
13. Elastic piston, manufactured solution (SVK, $\bar\lambda=\bar\mu=\bar\rho=0.1$): max-norm rates
    at $t=0.5$ are 1.95 ($\rho$), 2.01 and 2.10 (fluid velocity components), 1.87 ($T$), 1.91
    (displacement), 2.00 (solid velocity) and 2.02 (stress). (Fig. 8) **Shown**
14. Rotating disk, heavy solid (density parameter 10): rates 2.01, 2.02, 2.03, 2.01, 2.39, 2.20,
    2.48, identical for the simplified and full projections; the traditional partitioned scheme
    gives 2.00, 2.00, 2.01, 2.00, 2.38, 2.19, 2.48. (Fig. 12) **Shown**
15. Rotating disk, medium solid (parameter 1): rates 1.89, 1.89, 1.90, 1.89, 2.39, 2.20, 2.49 for
    both projections; the traditional partitioned scheme is unstable. (Fig. 13) **Shown**
16. Rotating disk, light solid (parameter 0.1): rates 1.94, 1.65, 1.49, 2.35, 2.36, 2.13, 2.45 for
    both projections; the traditional scheme is unstable; the error ratios approach 4 under
    refinement; the case approaches an inviscid fluid with a free surface. (Fig. 14, §5.2)
    **Shown**
17. The difference between the simplified and full projections is negligible in every problem
    considered. (§5.2, §6, Fig. 19) **Shown**
18. Shock–ellipse: the linear-elastic model, which assumes small displacement gradients, is
    unsuitable for large rotations; the linear-elastic solid barely rotates, while the neo-Hookean
    and rigid solids translate and rotate markedly. (Figs. 16–17) **Shown**
19. Elastic solids delay the bow-shock formation relative to the rigid body by the elastic-wave
    transit time and radiate many low-amplitude fluid waves. (Fig. 16, §6) **Shown**
20. The finest ellipse grid has about 2.2 million points, only about 8,800 on the two curvilinear
    grids; the cost is dominated by the static Cartesian grids. (§6) **Stated**
21. Beam in cross flow: the heaviest beam deflects horizontally by about 40% of its length; the
    lightest bends over by $t=5$ and starts to recover by $t=7$; the centrelines on the two finest
    grids agree. (Figs. 22–23, §7) **Shown**
22. Interface ghost values are set with the existing moving slip-wall (fluid) and moving
    traction-wall (solid) compatibility conditions rather than special interface conditions,
    with the interface values from the projection; this eases embedding the projection in
    existing partitioned solvers. (§4.3) **Stated**
23. Overlapping grids were recognized early as useful for rigid moving bodies such as store
    separation, and have been applied to electromagnetics and solid mechanics. (§1) **Stated**

# Printed slips

- **Post-shock state, §6:** "the corresponding state behind the shock is [1.516, 0.5233, 0,
  1.191]" for a Mach-1.3 shock into $[\rho,u,v,p]=[1,0,0,1]$, $\gamma=1.4$. The normal-shock
  relations give $\rho=1.516$ and $u=0.5233$, but $p=1.805$; the printed 1.191 is the temperature
  ratio $p/\rho$. The analogous Mach-1.1 state of §7, $[1.1691,0.1591,0,0.8893]$, satisfies the
  relations *(compiler check, not in the sources)*.
- **§6:** "a static rectangular grid $R_s$ for the domain $[-2.75,.75]\times[1.75,1.75]$", a
  zero-width interval in $x_2$.
- **§5.1:** the piston is "computed on the composite grid $\mathcal G^{(j)}_{ep}$ for
  $j=2,\dots,5$", with spacing $1/(10j)$, while the table rows are $h=1/20,1/40,1/80,1/160$,
  i.e. $j=2,4,8,16$.
- **Fig. 14 caption:** "computed using the AMP scheme medium solid, δ = 0.1"; the table is the
  light-solid case.
- **Conclusions:** "neo-Hookean (NE)" and then "NH" in the same paragraph.
- **Fig. 5 caption:** the fluid mapping is printed "$\bar x=g(r,t)$"; the text reserves the bar for
  solid reference coordinates.
- **Eq. (16)** writes the tangent as $\bar\tau_0$; the text defines $\bar t_0$.
- "Piola–Kirchoff" (§2); ref. [33] journal printed "AIAA J. Aircr.".

# Notation map

| Banks et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal G$, $G_g$, $g=1,\dots,\mathcal N$ | $\mathcal G$, $G_k$, $k=1,\dots,n_g$ | one composite grid per fluid or solid domain |
| $x=g(r,t)$; $\bar x=\bar g(\bar r)$ | $\mathbf x=\mathbf d_k(\mathbf r,t)$; static solid mapping | **$g$ is the grid index and the mapping in the source** |
| $J_g=\det(\partial x/\partial r)$ | $\mathcal J=\det(\partial\mathbf x/\partial\mathbf r)$ (page-local, as on [moving overset grids](/methods/moving-overset-grid.md)) | **not the registry $J$** (Pulliam–Steger, inverse volume) |
| $\dot g$ | $\mathbf u_g$ | grid velocity |
| $\Delta\bar r_\alpha$, $\mathbf i$, $e_\alpha$ | $\Delta r_m$, $\mathbf i$, unit index vector | direction index $\alpha\to m$ |
| $\rho$, $v$, $p$, $\gamma$ | $\rho$, $\mathbf u$, $p$, $\gamma$ | fluid |
| $\rho E$ | $E$ | **the source's $E$ is per unit mass** |
| $q$, $f_{ij}$ | $\mathbf q$, $\mathbf F$ | |
| $\bar u$, $\bar v$, $\bar P$, $\bar F$ | solid displacement, velocity, nominal stress, deformation gradient | page-local, bars mark solid quantities; **$\bar u$ is a displacement, not the registry velocity $\mathbf u$** |
| $\bar\lambda$, $\bar\mu$, $\bar\rho$ | Lamé constants, solid reference density | page-local; $\bar\mu$ is not a viscosity |
| $z_0=\rho_0a_0$ | $z$ | fluid acoustic impedance; $a_0$ the speed of sound |
| $\hat z_0$, $\hat k$, $\hat z_{p,0}$, $\hat z_{s,0}$, $\vartheta$ | $\bar z$, $\bar k$, $\bar z_{\mathrm p}$, $\bar z_{\mathrm s}$, $\theta_{\mathrm p}$ | effective solid impedance, coupling coefficient, scaled p- and s-wave impedances, angle of the p-eigenvector; page-local, as on [fluid–structure interaction](/methods/fluid-structure-interaction-on-overset-grids.md) |
| $\bar z_p=\bar\rho\bar c_p$ | $\bar\rho\bar c_{\mathrm p}$ | linear p-wave impedance, written out |
| $v_1$, $\hat v_1$; $w_1$, $\hat w_1$, $\hat w_2$ | $v$, $\bar v$; $\tau$, $\bar\tau$, $\bar\tau_t$ | normal velocity and normal/tangential traction, bar on the solid side; predicted values carry no subscript, superscript $I$ the interface; **$v$ here is not the registry's $y$-velocity** |
| $\delta$ | $\delta_\rho$ (page-local) | density parameter, fluid density $\gamma/\delta_\rho$; **the registry $\delta$ is the Yin–Yang buffer angle** |
| $E^{(q)}_j$, $r$, $\zeta_q$ | $\lVert e\rVert_\infty$, error ratio, $\sigma$ | **the source's $q$ is a solution component, not the interpolation width** |
| $T=p/\rho$ | $T$ (up to the gas constant) | |
| method of analytic solutions | twilight-zone flow | |
| DCG, AMP, TP, FSR | deforming composite grids, added-mass partitioned, traditional partitioned, fluid–solid Riemann | |

# Reference list

44 printed references, numbered `[1]`–`[44]`. All 44 are merged complete into the
[bibliography](/bibliography.md) with `citedby` banks-2016; no reference prints a DOI. Ref. [6] is
an arXiv preprint "submitted for publication" and is its own entry. Same-key suffixes follow
publication order: refs. [4] and [5] (Parts I and II of one FSI analysis, Part II published first)
are `banks-2014-b` and `banks-2014`; refs. [8] and [28] are `henshaw-2006` (moving overlapping
grids with AMR) and `henshaw-2006-b` (Maxwell); refs. [38] and [44] are `henshaw-1998` (Ogen
report) and `henshaw-1998-b` (Mappings report). AIAA papers are entered as technical reports, and
the LLNL reports as reports.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Wing–pylon–store separation and related moving-body cases](/benchmarks/store-separation.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [High-order discretizations on overlapping grids](/methods/high-order-overset-discretization.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Moving overset grids](/methods/moving-overset-grid.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
- [Twilight-zone flow (manufactured solutions)](/methods/twilight-zone-flow.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)
