---
type: Source
title: "Elzaabalawy et al. (2023) — Assessment of solving the RANS equations with two-equation eddy-viscosity models using high-order accurate discretization"
description: "Hybridizable discontinuous Galerkin discretization of incompressible RANS with the Wilcox 1998, TNT, BSL and SST k-ω models up to Re = 10^9: 1/ω interpolation, wall-element removal, mean-preserving limiters and segregated coupling, verified by manufactured solutions and against a second-order finite-volume code."
resource: "doi:10.1016/j.jcp.2023.112059"
source_kind: paper
authors: [Elzaabalawy H., Deng G., Eça L., Visonneau M.]
year: 2023
venue: "J. Comput. Phys. 483:112059"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Elzaabalawy_Assessment_of_solving_the_RANS_equations_with_two-equation_e.pdf"
tags: [k-omega, rans, dg, high-order, verification, k-omega-sst]
timestamp: 2026-10-26T20:47:00Z
---

# Summary

Elzaabalawy et al. (2023) discretize the steady incompressible RANS
equations with a hybridizable discontinuous Galerkin (HDG) method, aiming at
Reynolds numbers up to $10^9$. The closures are four two-equation
[$k$-$\omega$ models](/methods/k-omega-model.md) with a
[Boussinesq](/definitions/boussinesq-hypothesis.md) eddy viscosity: Wilcox
(1998), Kok's TNT, and Menter's BSL and [SST](/methods/k-omega-sst-model.md).
The mean-flow solver is the authors' pointwise divergence-free, energy-stable
HDG. The motivation is that thin attached boundary layers at industrial
Reynolds numbers keep RANS and [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
indispensable, whatever the progress of [wall-modelled LES](/methods/wall-modelled-les.md)
and its [grid requirements](/results/les-grid-point-requirements.md).

Four obstacles are named: stiffness, positivity of $k$ and $\omega$, steep
gradients ($\omega\to\infty$ at the wall), and min/max functions that break
smoothness inside elements. The remedies follow. $\omega$-dependent terms are
evaluated through the interpolant of $1/\omega$, which is smooth near the
wall, and $\nabla\omega$ as $-\omega^2\nabla(1/\omega)$. Wall-touching
elements are removed from the $\omega$ problem, which instead takes the
near-wall solution $6\nu/(\beta y^2)$ as Dirichlet data. A mean-preserving
Zhang–Shu limiter acts on $k$ and $1/\omega$. The SST eddy viscosity is
fitted by polynomial regression, and the coupling is segregated and
under-relaxed. Unlike the SA-based DG work reviewed in the introduction
([Spalart–Allmaras](/methods/spalart-allmaras-model.md)), the paper solves
for $\omega$ directly.

[Manufactured solutions](/methods/method-of-manufactured-solutions.md) give
optimal rates and calibrate the HDG stabilization. In
[channel flow](/benchmarks/turbulent-channel-flow.md) at $Re=2\times10^6$ and
$2\times10^8$, fourth-order HDG beats second-order finite volumes at equal
degrees of freedom, but the $\omega$ wall singularity degrades convergence on
fine grids. The [flat plate](/benchmarks/turbulent-boundary-layer.md) and the
[NACA 0012](/benchmarks/naca-0012-airfoil.md) show oscillations of $k$ and
$\omega$ at the boundary-layer edge and in the wake, a consequence of low
[numerical dissipation](/properties/numerical-dissipation.md). A 26-grid
comparison with ReFRESCO shows far smaller numerical error per degree of
freedom for HDG. SST is dropped for robustness. The outlook names a $k$-$kl$
model and coarse-mesh [transition modelling](/methods/local-correlation-based-transition-model.md),
and recalls why wall-resolved [$k$-$\varepsilon$](/methods/k-epsilon-model.md)
models are stiff. The plate profile is compared with Coles'
[law of the wall](/definitions/law-of-the-wall.md).

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 483 (2023) 112059;
received 27 December 2021, accepted 6 March 2023), 36 pages, all read, with
pp. 5–13 and 17–18 checked visually. Page 1 agrees with Crossref.

# Key claims

1. High-order schemes applied only to WMLES are not enough for industrial flows: thin attached boundary layers at $Re$ up to $10^9$ and the Spalart estimate that WMLES of a full wing will not be possible before 2045 keep RANS and hybrid RANS/LES indispensable; "it is unrealistic to discard RANS equations if one wishes to extend high-order accurate schemes to industrial applications" (§1, Fig. 1). **Stated**
2. Four challenges of high-order DG RANS: stiff non-linear equations; positivity of turbulence quantities (absolute values destroy polynomial continuity); large gradients, with $\omega$ infinite at the wall and steep at the boundary-layer edge, where low-order schemes are stabilized by their dissipation; min/max functions creating discontinuities inside elements (§1). **Stated**
3. The $k$-$\ln\omega$ form gives a smoother variable but a non-conservative non-linear term "problematic for DG methods to treat it implicitly"; the paper solves for $\omega$ directly (§1). **Stated**
4. Since $k_h/\omega_h$ is not a polynomial of degree $N$, the eddy viscosity carries an aliasing error; evaluating $\nu_t=|\mathsf N(1/\omega_h)|\,|\mathsf Nk_h|$ through the interpolant of $1/\omega$ "is used effectively to damp the oscillations of $\omega$ near the wall", whereas interpolating $\omega$ directly oscillates and goes negative (§3.1.1, Fig. 2). **Shown** (one-element illustration)
5. The production limiter $\min(\nu_t|S|^2,15\beta^*\omega k)$ (Eq. 55) uses 15 instead of Menter's 10, "because the lower value activates the limiter in boundary-layer regions"; the constant was 20 in Menter [30] and 10 in [31] (§3.1.1). **Stated**
6. Elements with a node (simplices: a vertex) on the wall are removed from the $\omega$ problem, and $\omega=6\nu/(\beta y^2)$, valid for $y^+<3$, is imposed on the new boundary (Eq. 57); a large wall value of $\omega$, as in [16], "is not stable for high-order approximations when directly using $\omega$" (§3.1.2, Fig. 3). **Stated**
7. $\nabla\omega_h=-\big(1/\mathsf N(1/\omega_h)\big)^2\,\mathsf N_x(1/\omega_h)$ preserves the sign and value of $\nabla\omega$ near the wall, so the TNT cross-diffusion switch does not flip between 0 and 0.5 through spurious sign changes (Eqs. 69–70, §3.1.2). **Derived**
8. The SST eddy viscosity is only $C^0$ inside elements; it is evaluated at quadrature points and fitted by a degree-$N$ polynomial; because the derivative of the fit was unstable, diffusion terms are put in weak form for BSL and SST (§3.2.1). **Stated**
9. A segregated fixed-point coupling (exterior, RANS and turbulence loops) is chosen because the turbulence equations are much stiffer than the mean-flow ones; under-relaxation $r_{ui}=0.4$, $r_{ug}=0.5$, $r_{kj}=r_{\omega j}=0.5$, $r_{kg}=r_{\omega g}=0.7$; the divergence-free constraint holds at every iteration (§4.1, Eqs. 76–87). **Stated**
10. A mean-preserving scaling limiter on $k$ and on $1/\omega$ (Eqs. 88–92) removes negative values while keeping the cell average and the high-order accuracy, citing Zhang & Shu [34, 35] (§4.2). **Stated**
11. Manufactured solution at $Re=10^7$, $N=3$ triangles: velocity error rates 4.62, 3.79, 3.82 and pressure rates 2.84, 2.94, 2.97, about $N+1$ and $N$; the $k$ and $\omega$ equations alone are also optimal (§5.1, Table 1). **Shown**
12. With the HDG stabilization $\tau_{\mathrm{HDG}}=Re/\ell_{\mathrm{HDG}}$ the error is smallest for $\ell_{\mathrm{HDG}}\approx10^2$ at $Re=10^5$, $10^7$ and $10^9$, supporting the proportionality of $\tau_{\mathrm{HDG}}$ to $Re$ proposed in [26] (§5.1, Figs. 4–6). **Shown**
13. Channel (Wilcox 1998, $N=3$) at $Re=2\times10^6$ (60 degrees of freedom in $y$) and $2\times10^8$ (120): fourth-order HDG predicts velocity, $k$ and $\omega$ near the wall better than second-order finite volumes at the same $y^+$ and degrees of freedom; HDG needs a lower $y^+$ as $Re$ grows to capture $\nabla\omega$ (§5.2, Figs. 7–12). **Shown**
14. Refinement from 30 to 300 elements in $y$: rates about $N+1$ from 30 to 150 cells, deteriorating on finer grids because the $\omega$ wall singularity makes the global rate "first-order accurate at most", as for second-order finite volumes (Eça et al. [38]) (§5.2.1, Table 2, Figs. 13–14). **Shown**
15. Skin friction from the HDG auxiliary variable $\mathsf E_h$ (degree $N$) converges at order $N+1$ and is closer to the exact value than that from $\nabla\boldsymbol u_h$ (degree $N-1$, order $N$); with the exact value $1.2373476\times10^{-3}$ from the imposed pressure gradient, the text gives errors of 1.0% to 0.025% ($\mathsf E_h$) and 6.4% to 0.13% ($\boldsymbol u_h$) from coarsest to finest grid (§5.2.1, Table 3, Fig. 15). **Shown** (Table 3 differs: see Printed slips)
16. With an algebraic mixing-length model, free of the $\omega$ singularity, the mean velocity converges at the optimal order $N+1$ (§5.2.1, Eqs. 93–94, Fig. 16). **Shown**
17. Flat plate (TNT, inlet $\nu_t/\nu=0.1$): the HDG velocity profile is very close to Coles' law; skin friction is about 2% above ISIS-CFD SST, attributed to the leading-edge singularity and the lower dissipation of the finer HDG leading-edge mesh (§5.3, Figs. 18–20). **Shown**
18. $k$ and $\omega$ oscillate at the boundary-layer edge; BSL and SST are less robust than TNT and Wilcox 1998 at low inlet eddy viscosity; raising the inlet viscosity ratio to 100 is "one of the simplest remedies"; HDG-SST at ratio 100 over-predicts skin friction by 1.6% against ISIS-CFD (§5.3, Figs. 21–23). **Shown**
19. "The robustness of the SST model in the high-order framework is questionable due to the polynomial regression that is used to approximate the C0 continuous eddy viscosity. Thus, it is excluded for further study in this work." (§5.3). **Stated**
20. Wilcox 1998 is very sensitive to the inlet condition; TNT and BSL do better; the raised inlet eddy viscosity over-predicts skin friction (§5.3, Figs. 24–27). **Shown**
21. Flat-plate skin-friction verification (TNT, grids $228\times72$ to $380\times120$): observed order 1.84 from $\boldsymbol u_h$ and 3.33 from $\mathsf E_h$, extrapolated $2.919602\times10^{-3}$ and $2.918802\times10^{-3}$; the sub-optimal orders are attributed to the edge singularities of $C_f$ and to the oscillations at the boundary-layer edge (§5.3, Table 4). **Shown**
22. NACA 0012 at $Re_c=6\times10^6$, $0^\circ$, inlet ratio 6: skin friction above the reference SST solution [39], $C_p$ slightly below it but closer to Ladson's experiment; $\omega$ oscillates in the wake, and at lower inlet ratios the oscillations "obstruct the convergence of the solver", "one of the drawbacks of using high-order methods while using the $k-\omega$ model" (§5.4, Figs. 28–36). **Shown**
23. HDG ($N=3$, 6 grids, 228,000–1,313,280 degrees of freedom) against ReFRESCO finite volumes (26 grids, 15,680–5,242,880 cells), flat plate $Re=10^7$, TNT: the extrapolated $C_D$ agree; at equal degrees of freedom the HDG numerical error is "significantly smaller", for integral, surface and local quantities (§6, Figs. 37–45). **Shown**
24. HDG data from $\boldsymbol u_h$ show "noise" in grid convergence, possibly from the aliasing used to damp $\omega$ and from incomplete iterative convergence; at $x=0.75L$ no reliable fit is possible (§6). **Shown**
25. Robustness is strongly mesh-dependent: stable on fine meshes with $y^+<3$ at the wall and $x^+<3$ around the leading and trailing edges; coarse elements at inlet, outlet or boundary-layer edge can destroy convergence; models less sensitive to inlet turbulence, such as SST, are recommended, but the $C^0$ SST eddy viscosity is undesirable (§7). **Stated**
26. The $k$-$kl$ model is proposed for high-order methods ($kl=0$ at the wall; it uses second velocity derivatives, available elementwise in DG), with a "negative $k$-$kl$" variant like negative SA; the low dissipation of high-order schemes makes local-correlation transition modelling feasible on coarser meshes (§7). **Stated**

The model form, translated (Eqs. 1–5, 38–39, 44): with kinematic mean
quantities,
$$-R_{ij}+2\nu S_{ij}=2(\nu+\nu_t)S_{ij}-\tfrac23k\delta_{ij},\qquad \nu_t=k/\omega\ \ (\text{except SST}),$$
$$\nabla\cdot\big(k\boldsymbol u-(\nu+\sigma_k\nu_t)\nabla k\big)+\beta^*\omega k=\nu_t|S|^2,\qquad \nabla\cdot\big(\omega\boldsymbol u-(\nu+\sigma_\omega\nu_t)\nabla\omega\big)+\beta\omega^2=\alpha|S|^2+\frac{F_\omega}{\omega}\nabla k\cdot\nabla\omega .$$
Constants: Wilcox 1998 $\sigma_k=0.5$, $\beta^*=0.09$, $\sigma_\omega=0.5$,
$\beta=0.072$, $\alpha=13/25$, $F_\omega=0$; TNT $\sigma_k=2/3$, $\beta^*=0.09$,
$\sigma_\omega=0.5$, $\beta=0.075$, $\alpha=\beta/\beta^*-\sigma_\omega\kappa^2/\sqrt{\beta^*}$,
$F_\omega=0$ or $0.5$ by the sign of $\nabla k\cdot\nabla\omega$; BSL/SST as
printed in §3.2 (Menter 2003, $\beta_1$ see Printed slips), SST
$\nu_t=a_1k/\max(a_1\omega,F_2|S|)$ with $a_1=0.43$ as printed.

# Printed slips

- §3.2 prints $\beta_1=0.75$ among the BSL/SST constants. The paper's own relation $\alpha=\beta/\beta^*-\sigma_\omega\kappa^2/\sqrt{\beta^*}$, stated for TNT with $\kappa=0.41$ and $\beta^*=0.09$, gives the printed $\alpha_1=5/9$ for $\beta_1=0.075$ ($0.553$) and the printed $\alpha_2=0.44$ for $\beta_2=0.0828$, $\sigma_{\omega2}=0.856$ ($0.440$), but 8.05 for $\beta_1=0.75$ *(compiler check, not in the sources)*.
- §4.2: "where $\epsilon=1^{-12}$".
- Table 3: the percentage errors do not match the tabulated values and the printed exact value $1.2373476\times10^{-3}$; recomputed, the $\boldsymbol u_h$ column runs 6.44% (coarsest) to 0.135% (finest), as the text says, against the printed 7.004% and 0.471%, and the $\mathsf E_h$ column runs 1.06% to 0.003%, against the printed 1.088% and 0.025% *(compiler check, not in the sources)*. The Table 3 values equal half the $C_f$ of Table 2 (e.g. $2.474698\times10^{-3}/2=1.237349\times10^{-3}$), which the paper does not say *(compiler check, not in the sources)*.
- Eq. (11) writes $\nu_c\mathbf E$ where the rest of the paper has $\nu_e$.
- Eqs. (65)–(66): "$a_\omega(k_h,\phi_h)$", "$d_\omega(k_h,\psi_h)$" and "$e_k(\mathbf q_h,\psi_h)$" in the $\omega$ equation, defined elsewhere with $\omega_h$ and $e_\omega$.
- Eq. (97), the rescue fit: "$\phi_i=\phi_o+\alpha_1r_i+\alpha_1r_i^2$", the same coefficient twice.
- Table 4 caption: "Re = ×10^7"; Fig. 33 caption: "Re = 6.6 × 10^6" against $6\times10^6$ elsewhere.
- The stabilization length scale is "set from 50L to 200L" (§2.1, §3.1.2) and "from 50 to 200" (§3.1.1).
- §3.2: $\rho$ appears in $CD_{k\omega}$ and $arg_1$ of a kinematic incompressible formulation.
- §1: "Peter et al. implemented the SA with HDG", for ref. [15], Peters & Evans.
- Citations whose reference entries carry unrelated titles: the "K-S correlation [40]" for skin friction cites an entry titled "The Kolmogorov-Smirnov test for goodness of fit" (Massey 1951); the ISIS-CFD solver "[41]" cites an entry titled "… the isis cfd code for fire simulation"; "Ph. Spalart in [5]" cites a book listed under Durbin (2021).
- Typos: "expect the SST model", "the STT and BSL" (§3.1), "relativity large gradients", "finner meshes", "matrix from".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $p$ (time averages) | $\langle u_i\rangle$, $\langle p\rangle$ | $p$ absorbs $\tfrac23k$ |
| $\bar\tau_{ij}=2\nu_eS_{ij}-\tfrac23k\delta_{ij}$ | $-R_{ij}+2\nu S_{ij}$ | **collision:** negative convention, includes the viscous stress; the overbar is not the LES filter |
| $\nu_e$, $\nu_{th}$, $\nu_{eh}$ | $\nu+\nu_t$, $\nu_t$ (discrete) | |
| $\mathbf E$ | $2S_{ij}$ | HDG auxiliary variable, factor two |
| $P=2S_{ij}S_{ij}$ | $\lvert S\rvert^2$ | production $\nu_t\lvert S\rvert^2$ |
| $S$ (Eq. 71) | $\lvert S\rvert$ | not defined in the source |
| $\zeta$, $\zeta_1$, $\zeta_2$ | $\alpha$, $\alpha_1$, $\alpha_2$ | production coefficient of the $\omega$ equation |
| $F_\omega$ | $F_\omega$ (page-local) | cross-diffusion coefficient; not the PANS ratio $f_\omega$ |
| $\sigma_k$, $\sigma_\omega$, $\beta^*$, $\beta$, $\kappa$, $F_1$, $F_2$, $a_1$, $CD_{k\omega}$ | same | |
| $y_{wall}$, $y^+_{elem}$, $x^+$ | $y$, (wall units of the second element), (streamwise wall unit) | |
| $m$, $m_{int}$ | $N$, (quadrature order) | $m=3$, fourth order |
| $\mathbf N$, $\mathbf N_x$ | $\mathsf N$, $\mathsf N_x$ (page-local) | **collision:** interpolation and differentiation matrices, not the degree $N$ |
| $\bar\omega_h=1/\mathbf N(1/\omega_h)$; $\bar k$, $\bar\omega$ (§4.2) | (page-local) | **collision:** overbar is a harmonic interpolant or a cell average |
| $\tau$, $\tau_k$, $\tau_\omega$; $\ell$, $\ell_k$, $\ell_\omega$ | $\tau_{\mathrm{HDG}}$, $\ell_{\mathrm{HDG}}$ (page-local) | **collision:** stabilization, not a stress |
| $\hat{\mathbf u}_h$, $\hat p_h$, $\hat k_h$, $\hat\omega_h$ | (face traces, page-local) | **collision:** hat is not a test filter |
| $\theta_k$, $\theta_{1/\omega}$, $\epsilon$ | (limiter factors and floor, page-local) | |
| $l=0.39y(1-e^{-y^+/26})$ | $\ell_m$ (mixing length, page-local) | $A^+=26$ |
| $c_f$, $C_D$, $C_p$ | $C_f$, $C_D$, $C_p$ | |
| $r_i$, $\phi_o$, $\alpha$, $p$ (Eqs. 95–97) | (grid ratio, extrapolated value, error constant, observed order) | **collision:** $\alpha$, $p$ |
| $Re$ | $Re$ | free-stream velocity with plate length, chord or channel half-height |

# Reference list

46 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. No printed
duplicates. [24] and [26] are printed as "submitted for publication" (2020)
and are kept as pre-publication entries; [7] is a PhD thesis; [43] an
internal IST report; [39] the NASA Turbulence Modeling Resource web page
(2020); [5] (Durbin 2021) has no publisher; [2] (Slotnick et al.) has no
venue. Same-author same-year works take suffixes in printed order (Eça
2010, 2012; Zhang 2010; Elzaabalawy 2020).

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Method of manufactured solutions](/methods/method-of-manufactured-solutions.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
