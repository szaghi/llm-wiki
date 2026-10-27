---
type: Source
title: "Alauzet et al. (2022) — Periodic adjoints and anisotropic mesh adaptation in rotating frame for high-fidelity RANS turbomachinery applications"
description: "Builds a metric-based anisotropic mesh-adaptation workflow for steady RANS turbomachinery on unstructured tetrahedral meshes, with periodic discrete adjoints, rotating-frame functionals and shape-preserving periodic remeshing, and shows mesh-converged LS89 and NASA Rotor 37 predictions with Spalart–Allmaras closure."
resource: "doi:10.1016/j.jcp.2021.110814"
source_kind: paper
authors: [Alauzet F., Frazza L., Papadogiannis D.]
year: 2022
venue: "J. Comput. Phys. 450:110814"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Alauzet_Periodic_adjoints_and_anisotropic_mesh_adaptation_in_rotatin.pdf"
tags: [mesh-adaptation, rans, turbomachinery, spalart-allmaras, numerical-dissipation]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Alauzet et al. (2022) control the discretization error of steady RANS
turbomachinery computations by
[metric-based anisotropic mesh adaptation](/methods/mesh-adaptation.md) on
fully unstructured, purely tetrahedral meshes. The flow solver (Wolf, INRIA)
is vertex-centred and mixes second-order finite volumes (HLLC, MUSCL
"β-scheme" reconstruction with limiters, whose choice "directly affects the
[numerical dissipation](/properties/numerical-dissipation.md)") for
convection with P1 Galerkin finite elements for the viscous terms. Time
stepping is implicit pseudo-transient continuation. The closure is the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) without $f_{t2}$
(SA-noft2), with QCR2000 for Rotor 37, entering the mean flow through the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
($\mu\to\mu+\mu_t$, $\lambda\to\lambda+\lambda_t$, $Pr_t=0.9$).

The contributions are numerical: strong periodicity in the flow and the
discrete-adjoint solvers through one layer of ghost elements; exact
differentiation of the rotating-frame terms and boundary conditions; the
discrete adjoints of five turbomachinery functionals, with the chain rule
from the rotating to the absolute frame; a four-step periodic remeshing that
keeps the domain shape, with the metric rotated as $R\mathcal MR^T$; and a
mesh-convergence loop that traces a compressor characteristic to stall. Two
error estimates drive adaptation: a feature-based multiscale $L^4$ estimate
of the Mach number and a goal-oriented adjoint-weighted estimate from which
the turbulence equation is omitted.

On the LS89 turbine vane and NASA Rotor 37 the adapted solutions converge to
the same functionals whatever the initial mesh and the estimate, with one
exception for LS89; goal-oriented adaptation converges earlier. The adapted
meshes reach $y^+\approx1$ without prismatic or hexahedral layers, the
opposite design choice from hand-built
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md).
Against structured [elsA](/software/elsa.md) RANS on 3M–32M cells the adapted
solutions predict higher pressure ratio and efficiency and keep the tip and
induced vortices that the globally refined structured meshes dissipate. The
paper proposes comparing SA with the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) once discretization
error is removed (future work). Turbulence modelling is not the subject; the
paper is peripheral to the bundle's closure topics.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 450:110814, available
online 9 November 2021), 65 pages, all read. Page-1 title, authors and DOI
match the metadata above. No identity problem. Equation, section, figure
and reference numbers on this page are those of this version.

# Key claims

1. Unstructured, purely tetrahedral, anisotropically adapted meshes give high-fidelity, mesh-converged RANS turbomachinery predictions with no prismatic or hexahedral boundary-layer meshes (§1, §9). **Shown**
2. The mesh-adaptive solution converges to the same solution whatever the initial mesh and the error estimate (feature-based or goal-oriented) (§1; §8.1.3, Fig. 18; §8.2.4). Exception stated for LS89 at the lowest pressure ratio: "the feature-based approach gives a different answer from the goal-oriented one" (§8.1.3). **Shown**
3. Exact differentiation of all implicit terms (convective, viscous, source, boundary conditions) "greatly improves the flow solver convergence"; only the MUSCL part is not differentiated, because it would raise the matrix pattern from about twenty to about a hundred entries per row in 3D (§4.2, footnote 1). **Stated**
4. Without exact differentiation of the inhomogeneous Dirichlet condition $\boldsymbol u=-\boldsymbol\Omega_{\mathrm{rot}}\times\boldsymbol r$ on fixed walls in the rotating frame, the residual stalls even with limiters frozen after iteration 800, and the pressure ratio oscillates and drops (Rotor 37, initial mesh) (§4.2.3, Fig. 2). **Shown**
5. Breadth-first-search renumbering is more effective than Hilbert space-filling-curve renumbering for implicit convergence; Hilbert ordering is better for cache misses (§4.2). **Stated**
6. Symmetric Gauss–Seidel (SGS) relaxation of the implicit linear system: at most $k_{max}$ iterations (usually 20), stopped when the relative linear residual drops by a factor 0.01 (§4.2.4). **Stated**
7. The RANS discrete-adjoint system has no mass matrix (infinite CFL) and is much stiffer than the flow system, the more so on finer adapted meshes. GMRES preconditioned by LU-SGS reduced the residual by only 3–5 orders after 10 000 iterations with a Krylov space of 1 000; GMRES preconditioned by 20–40 SGS passes converges with Krylov spaces up to 200, by twelve orders (§5.3). **Shown**
8. The adjoint is discontinuous at Dirichlet boundaries; for error estimation it is replaced there by a quadratic least-squares extrapolation from the interior (§5.2). **Stated**
9. The optimal $L^p$ continuous metric (Eq. 34) and its interpolation error (Eq. 35) are cited from earlier work; the paper uses $L^4$ of the Mach number following Park & Balan's finding of faster boundary-layer adaptation in RANS (§6.1). **Stated**
10. The goal-oriented error is bounded by an adjoint-weighted sum of $L^1$ interpolation errors of the conservative variables, with the 3D weights given explicitly (Eq. 38 and following, §6.2). **Derived** (from cited work)
11. The turbulence equation is omitted from the goal-oriented estimate; turbulence enters only through $\mu_t$ and $\lambda_t$ (Remarks 5.1, 6.1). **Stated**
12. Periodic remeshing takes four steps (remesh, migrate, remesh, migrate back), keeps the original domain, and needs a remesher that handles non-manifold geometry; 5 element layers are migrated, and with $N_l$ layers at least $2N_l$ layers must span the narrowest periodic width (§7.2). **Stated**
13. For rotation periodicity the metric is transported as $\bar{\mathcal M}=R\mathcal MR^T$ (§7.2). **Derived**
14. Without adaptation of the periodic surfaces, interior refinement leaves them too coarse, causing "inversion of the local anisotropy", instabilities, unphysical results and solver breakdown (§7.3, Figs. 8–10). **Shown** (qualitatively)
15. Periodic-remeshing CPU time grows linearly with mesh size, with a factor-2 overhead over non-periodic adaptation and an average speed of 33 000 elements per second (serial). Example at 9.8M vertices / 61.1M elements: remeshing 31m28 and 30m30, migrations 3m01 and 2m38 (§7.4, Table 1). **Shown**
16. A complexity counts as converged when mass flow, pressure ratio and temperature ratio vary by less than 1% over three consecutive adaptations; complexity doubles at each outer iteration; in practice 4 adaptations per complexity are needed (§3, §8.1.2, §8.2.3). **Stated**/**Shown**
17. On coarse adapted meshes (complexities "40 000 and 80 000") simulations diverge at $P_{ratio}\approx1.175$, which motivates Algorithm 2 (restart of each higher pressure ratio from the previous one at fixed complexity). Goal-oriented adaptation reaches $P_{ratio}=1.280$ with 720 000 vertices, feature-based needs 1 400 000 (§3, §8.2.4). **Shown**
18. Rotor 37: mesh convergence is quick (a few hundred thousand vertices) from choke to near-peak efficiency ($P_{ratio}\approx1.2$) and harder towards stall; the total-temperature ratio converges at all points with about half a million vertices (§8.2.4, Figs. 22–25). **Shown**
19. Goal-oriented adaptation on the total-pressure ratio converges earlier than feature-based adaptation, towards the same values. Against the finest goal-oriented reference: at MFR/MFR* = 1.00 the goal-oriented gap is below 0.1% after 0.5M vertices (feature-based 0.2–0.5%); at 0.98 it is 0.5% at 1M vertices and below 0.2% above (feature-based below 0.2% on 5M); at 0.93 all are within 0.5% (§8.2.4, Fig. 32). **Shown**
20. Table 2 (5M-vertex adapted meshes against 7M-cell elsA), choke MFR / pressure ratio / efficiency: feature-based 20.58 / 1.904 / 0.861, peak efficiency 2.058 / 0.874 at MFR/MFR* 0.993, near stall 2.141 / 0.854; goal-oriented 20.66 / 1.909 / 0.865, peak 2.062 / 0.877, near stall 2.144 / 0.857; elsA 20.71 / 1.965 / 0.855, peak 2.046 / 0.860, near stall 2.130 / 0.830 (Table 2). **Shown**
21. Total-pressure-ratio and total-temperature-ratio characteristics lie above the experiment, "not in accordance with the literature" that "generally shows curves below the data"; the authors attribute this mainly to simulating the cold instead of the hot geometry (§8.2.4). **Shown**/**Stated** (cause not tested)
22. The predicted isentropic efficiency is "a lot higher" than literature and elsA results, below experiment at high mass flow and matching it near stall; the authors attribute the gap to a "lack of resolution of the non-adapted meshes" (§8.2.4). **Shown**/**Stated**
23. Radial profiles at 5M vertices agree in shape with experiment and, near the endwalls, better than elsA; refining elsA moves it towards the adapted solution, attributed to better-resolved secondary flows (§8.2.4, Fig. 31). **Shown**
24. Globally refined structured elsA meshes dissipate the induced tip vortex and weaken the tip-leakage vortex downstream; the adapted meshes keep both (§8.2.5, Figs. 42–43). **Shown**
25. Feature-based adaptation gives $y^+=1$ before the shock on the coarsest adapted mesh (360 354 vertices) and $y^+\approx2$ in the detached boundary layer after it, the same as on the finest mesh (2 820 611 vertices): adaptation converges in the boundary layer without over-refining (§8.2.5, Fig. 40). **Shown**
26. Near stall (93% of choke mass flow) the hub-corner separation barely changes while the tip separation and leakage area grow; the authors infer that stall originates near the tip, and relate the slower mesh convergence to the more isotropic flow there (§8.2.5, Fig. 41). **Shown**/**Stated**
27. On the 10M-vertex (61 486 015 tetrahedra) goal-oriented mesh at $\beta=1.2$ the mean anisotropic ratio is 112 and the mean anisotropic quotient 9 892, i.e. "almost four order of magnitudes" fewer elements than an isotropic adapted mesh; the element-volume ratio max/min is about $10^9$ (§8.2.6, Table 3). **Shown**
28. Transition is not modelled for Rotor 37 because LES shows transition almost immediately at the leading edge, triggered by the leading-edge shocks (§8.2). **Stated** (from cited LES)
29. Once discretization error is removed, turbulence models can be compared without mesh contamination (SA against Menter SST $k$-$\omega$); extensions to URANS, higher order, DES and LES are planned (§9). **Stated**

# Printed slips

- **Sign of the SA destruction term (Eq. 13, p. 7).** Eq. 9 prints the destruction as $-c_{w1}f_w\rho(\tilde\nu/d)^2$; the last row of the source vector Eq. 13 prints $\frac{c_{b2}\rho}{\sigma}\|\nabla\tilde\nu\|^2+\rho c_{b1}\tilde S\tilde\nu+c_{w1}f_w\rho\big(\frac{\tilde\nu}{d}\big)^2$, with a plus sign.
- **$c_{w1}$ (§2.3).** Printed $c_{w1}=c_{b1}/\kappa+(1+c_{b2})/\sigma$;
  [Cato et al. (2023)](/sources/cato-2023.md) (§II A) print
  $c_{b1}/\kappa^2$ with the same constants, and the log-layer balance of
  the printed SA equation requires $\kappa^2$ (see the
  [Spalart–Allmaras page](/methods/spalart-allmaras-model.md))
  *(compiler check, not in the sources)*.
- **Number of complexities (§8.1.2).** "seven complexities" for LS89, while the printed list has eight values, $\{4\,000,\dots,512\,000\}$, and so does the vertex list.
- **Rotor 37 low complexities (§8.2.4).** "for very low complexities (40 000 and 80 000), the simulations start to diverge"; the Rotor 37 complexity list of §8.2.3 starts at 160 000.
- **Pressure ratio 1.305 (Table 2).** The goal-oriented "Wolf Stall" row prints a CFD P ratio of 1.305; the largest $\beta$ in the lists of §8.2.3 and §8.2.4 is 1.300.
- **Algorithm step (§3).** "The convergence criteria of step 1(f)"; in Algorithm 1, step 1(f) is "Compute adjoint state" and the convergence check is step 1(g).
- **Duplicated paragraph (§6.1, p. 24).** The opening paragraph ("The most natural and straightforward approach…") and the optimal metric appear twice; Eqs. 32 and 34 are identical.
- **Fig. 17 left/right.** The caption puts feature-based left and goal-oriented right; the text of §8.1.3 says "goal-oriented mesh adaptation based on the loss coefficient functional (left pictures) and … feature-based approach (right pictures)".
- **Fig. 42 left/right (§8.2.5).** The text says "feature-based on the right and goal-oriented on the left", the reverse of the order stated in the paper's other captions.
- **Viscosity units.** $\mu_{ref}=1.716\times10^{-5}$ "Pa.s−1" (LS89) and "1.789 × 10−5 Pa.s−1 kg m−1 s−1" (Rotor 37).
- **LS89 inlet total pressure.** The experimental conditions give $p_t^{in}=1.87\times10^5$ Pa, the simulation reference state $1.828\times10^5$ Pa; the paper does not explain the difference.
- **Software name (§8.2.2).** "Autrogrid" for Autogrid.
- **Table 2, elsA MFR/MFR\*** *(compiler check, not in the sources)*. Dividing the printed elsA mass flows by the printed elsA choke mass flow 20.71 gives $20.46/20.71=0.988$, $19.20/20.71=0.927$ and $18.86/20.71=0.911$, against printed 0.980, 0.935 and 0.925. The adapted-mesh rows agree with the same division within 0.002
(feature-based) and 0.001 (goal-oriented).
- **Anisotropic ratio (§8.2.6, p. 52)** *(compiler check, not in the sources)*. The paper prints ratio $=\sqrt{\min_i\lambda_i/\max_i\lambda_i}=\max_ih_i/\min_ih_i$. With the metric sizes $h_i=\lambda_i^{-1/2}$, $\max_ih_i/\min_ih_i=\sqrt{\max_i\lambda_i/\min_i\lambda_i}$; the printed square root is inverted (it is $\le1$, while the reported mean ratio is 112).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf u=(u,v,w)$, $p$, $E$, $T$ | $\rho$, $u_i$, $p$, $E$, $T$ | RANS mean fields; the paper marks no averaging; $E$ is per unit mass |
| $\mu$, $\lambda$ | $\mu$, (thermal conductivity) | Sutherland, $S_u=110$; $Pr=0.72$ |
| $\mu_t$, $\lambda_t$ | $\mu_t$, (turbulent conductivity) | $Pr_t=\mu_tC_p/\lambda_t=0.9$ |
| $\mathcal T=(\mu+\mu_t)\tau$, $\tau=\nabla\otimes\mathbf u+{}^t\nabla\otimes\mathbf u-\tfrac23\nabla\cdot\mathbf u\,\mathbb I$ | $\sigma_{ij}+2\mu_tS^d_{ij}$, $\tau=2S^d$ | **collision:** the source's $\tau$ is twice the deviatoric strain rate, not the SGS stress $\tau_{ij}$ |
| $\tau_{QCR}$ | (QCR2000 correction) | defined in Spalart (2000), not reproduced |
| $\tilde\nu$, $\tilde S$, $\chi$, $d$ | $\tilde\nu$, (SA modified vorticity), $\chi$, $d$ | agree; $\tilde S$ built on $\|\nabla\times\mathbf u\|$ |
| $\sigma$, $c_{b1}$, $c_{b2}$, $\kappa$, $c_{w1}$, $c_{w2}$, $c_{w3}$, $c_{v1}$ | same names | printed values $2/3$, 0.1355, 0.622, 0.41, $c_{w1}$ printed as $c_{b1}/\kappa+(1+c_{b2})/\sigma$, 0.3, 2, 7.1; $f_{t1}=f_{t2}=0$ |
| "dissipation", "diffusion" (Eq. 9) | (SA diffusion terms) | the paper labels the conservative term "dissipation" and the $c_{b2}$ term "diffusion" |
| $\boldsymbol\Omega=\omega\mathbf e_\Omega$ | $\Omega_{\mathrm{rot}}$ | **collision:** not the rotation-rate tensor $\Omega_{ij}$; the source's $\omega$ is neither $\omega$ (§4) nor vorticity |
| $\omega$ (§2.5) | (loss coefficient) | **collision:** same letter as the rotation speed in the source and as the registry's specific dissipation rate |
| $W$, $W^*$, $\Pi_h$ | (conservative state, discrete adjoint, P1 interpolation) | $W$ includes $\rho\tilde\nu$ |
| $h$ | $h$ | smallest element height around a vertex (time step) |
| $\mathcal M$, $\mathcal C$, $\mathcal N$, $H_u$ | (metric field, complexity, target complexity, sensor Hessian) | $\mathcal C\approx\frac{\sqrt2}{12}n_t$ |
| $p$ in $L^p$, $d$ | (norm exponent, here 4; space dimension) | **collision:** not the pressure or the wall distance |
| $\alpha$ | (complexity growth factor, 2) | **collision:** not the DG blending factor; also $\mathbf x\cdot\mathbf e_\Omega$ in §2.2 |
| $\beta$, $P_{ratio}$ | (outlet static to inlet total pressure ratio) | **collision:** not the field-inversion $\beta(\boldsymbol x)$ |
| $\lambda_i$, $h_i$ (§8.2.6) | (metric eigenvalues, sizes) | not the conductivity |
| $y^+$ | $y^+$ | first-cell height in wall units, an outcome of adaptation |
| "a priori" (error estimate) | — | numerical-analysis sense, not [a priori testing](/definitions/a-priori-and-a-posteriori-testing.md) |

# Reference list

76 printed references, numbered style [1]–[76], ordered alphabetically by
first author. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works are keyed in printed order (Alauzet 2010 [1], [5];
Alauzet 2016 [2], [6]; Loseille 2011 [42], [43]; Loseille 2013 [47], [48]).
[68] Spalart (2000) is printed "Strategies for turbulence modelling and
simulations" and is the same work as the existing `spalart-2000` entry;
[69] Spalart & Allmaras (1992) is the existing `spalart-1992`. [15] and [74]
(J. Turbomach.) print no pages; [38] Van Leer is printed with year 1972. No
printed duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunks 5–6. This source is cited on:

- [NASA Rotor 37](/benchmarks/nasa-rotor-37.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Boundary-layer-conforming grids for wall-modelled LES](/methods/boundary-layer-conforming-grid.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [elsA](/software/elsa.md)
