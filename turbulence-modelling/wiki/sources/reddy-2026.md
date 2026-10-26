---
type: Source
title: "Reddy et al. (2026) — Comparison of Sub-Grid Scale Models for Large-Eddy Simulation Using a High-Order Spectral Element Approximation of the Compressible Navier-Stokes Equations at Low Mach Number"
description: "Compares Smagorinsky, Vreman and residual-based dynamic SGS models, with element-wise and node-wise coefficients, in a continuous-Galerkin spectral-element atmospheric solver on tracer transport, 2D Burgers, the Taylor–Green vortex and the Straka density current; nodal residual-based models are judged best overall."
resource: "doi:10.4208/cicp.oa-2025-0351"
source_kind: paper
authors: [Reddy S., Tissaoui Y., Alves F.A.V.d.B., Giraldo F.X., Marras S.]
year: 2026
venue: "Commun. Comput. Phys. 40:701–732"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Communications_in_Computational_Physics_Reddy_Comparison_of_Sub-Grid_Scale_Models_for_Large-Eddy_Simulatio.pdf"
tags: [sgs-model, les, spectral-element, residual-based, atmospheric-flows, taylor-green-vortex]
timestamp: 2026-10-26T15:49:00Z
---

# Summary

Reddy et al. (2026) compare explicit eddy-viscosity subgrid closures for
[LES](/definitions/large-eddy-simulation.md) of low-Mach compressible
atmospheric flows. They run them in NUMA, an atmospheric model on a
[continuous-Galerkin spectral-element](/methods/spectral-element-method.md)
discretization with LGL collocation, a diagonal mass matrix, direct stiffness
summation and $N=4$. Filtering is implicit (grid filter) with
$\Delta=\min(\Delta x,\Delta y,\Delta z)/(N+1)$. The closures are the
[Smagorinsky model](/methods/smagorinsky-model.md) ($C_s=0.14$, 0.21 for
Burgers), the [Vreman model](/methods/vreman-model.md) (constant
$\approx2.5C_s^2$) and two forms of the
[residual-based dynamic SGS model](/methods/residual-based-dynamic-sgs-model.md).
That model takes its eddy diffusivity from the residual of the filtered
inviscid equations, capped by an upwind-like maximum. R-DSGS keeps the time
derivative in the residual; T-DSGS, the variant named here, drops it. Each
DSGS form is run with one coefficient per element (E) or with a coefficient
varying node by node inside the element (N). The nodal form is the paper's
stated departure from element-constant practice.

Four tests are run: slotted-cylinder tracers in a reversing deformational
flow, a 2D inviscid Burgers system, the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) on $32^3$ elements,
and the Straka density current at 50, 25 and 12.5 m. All closures keep
discontinuities sharp. Smagorinsky and Vreman produce Gibbs oscillations, and
Vreman diverges at $t=0.7$ s in the Burgers test, while DSGS, with one
coefficient per equation, stays stable. The elemental DSGS is the most
diffusive. The nodal R-DSGS conserves kinetic energy best before vortex
breakdown. All dissipation rates peak near $t^*\approx8$, against about 9
in the DNS of Brachet et al. Smagorinsky and Vreman resolve Kelvin–Helmholtz
rotors on coarser grids. The spectra show $k^{-5/3}$ ranges (and $k^{-3}$ in
2D). The authors favour nodal R-DSGS. They call spectral elements ideal for the
comparison for their "lack of inherent
[numerical dissipation](/properties/numerical-dissipation.md)". They
distinguish their explicit-closure approach from
[implicit LES](/definitions/implicit-les.md) and its
[DG](/methods/discontinuous-galerkin-spectral-element-method.md) practice.
They call the Taylor–Green case
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md). All
tests are [a posteriori](/definitions/a-priori-and-a-posteriori-testing.md).

# Version read

A preprint dated "March 4, 2021" on page 1 and in every running header ("A
PREPRINT - MARCH 4, 2021"), with no arXiv or HAL stamp, 26 pages, all read
(pages 1–8, 10 and 13–18 also visually). It is about five years older than
the version of record (32 pages, DOI with "oa-2025-0351"); claims and numbers
here are those of the 2021 preprint and the published text can differ.
**Author order:** read row by row, the preprint's two-column author block puts
Marras fourth and Giraldo fifth; Crossref has Giraldo before Marras, and the
frontmatter follows Crossref. The Supplementary Material (tracer figures of
Case 4) is referred to but not in the file.

# Key claims

1. Element-based Galerkin SGS models in the literature assume a constant eddy diffusion within each element even for high-order elements; the nodal variant lets it vary within the element (§1, p. 2). **Stated** (contribution; used in §§5–8)
2. A spectral-element discretization is "ideal" for comparing SGS models "due to the lack of inherent numerical dissipation present" (§1, p. 2). **Stated**
3. DSGS: $\nu_t=\min(\nu_{\max},\nu_{\mathrm{res}})$, $\nu_{\mathrm{res}}=C\Delta^2\,\lVert \mathcal R(\tilde{\boldsymbol u})\rVert_\infty/\lVert\tilde{\boldsymbol u}-\langle\tilde{\boldsymbol u}\rangle_\Omega\rVert_{\infty,\Omega}$ with $C=1$; the scalar diffusivities are built alike and scaled by $Pr/(\gamma-1)$ with an artificial $Pr=0.7$ (§3.3, Eqs. 11–14). **Stated** (construction of Nazarov & Hoffman 2013, applied)
4. The dissipation is proportional to the residual, which scales as $\Delta^{-1}$ at discontinuities and is small in smooth regions; the cap $\nu_{\max}$ "is equivalent to a stable upwind scheme in regions with sharp discontinuities" (§3.3, p. 5). **Stated**
5. The time derivatives in the residuals are first-order backward differences; a second-order approximation made no significant difference (§3.3, p. 5). **Stated** (not shown)
6. Elemental coefficients, the maximum over the element's LGL points, are more dissipative than nodal ones (§3.3, p. 6; Cases 1–4). **Shown**
7. Case 1 (tracer): Smagorinsky keeps the discontinuity but errs by 0.12 kg/kg at the global minimum and 0.15 kg/kg at the maximum; Vreman by about 0.05 kg/kg at both (§5.2, Fig. 2). **Shown**
8. Case 1: elemental T-DSGS gives the most diffused interface and the smallest extremum errors; Vreman and nodal R-DSGS balance interface sharpness and overshoot best (§5.2, Figs. 2–3). **Shown**
9. R-DSGS is less diffusive than T-DSGS because "the magnitude of the residual is typically smaller than the unsteadiness of the flow" (§5.2, §9). **Stated**
10. Case 2 (Burgers): Smagorinsky and Vreman ($C_s=0.21$) oscillate near and away from discontinuities; Vreman diverges at $t=0.7$ s; DSGS, with one coefficient per equation, damps the oscillations and stays stable to $t=1$ s (§6.2, Figs. 4–6). **Shown**
11. Case 2: nodal R-DSGS gives the least dissipated non-oscillatory solution, elemental T-DSGS the most dissipated (§6.2, Fig. 6). **Shown**
12. Case 2: the Vreman divergence is attributed to its single coefficient for both equations, which DSGS avoids by decoupling them (§6.2, p. 11). **Stated** (no single-coefficient DSGS control)
13. Case 3 (Taylor–Green): the elemental T-DSGS and R-DSGS are the most dissipative of the six variants in all four integral quantities (§7.2, p. 14, Fig. 7). **Shown**
14. Case 3: nodal R-DSGS conserves kinetic energy best early ($t^*<12$) but has dissipated more by $t^*\approx24$; Vreman conserves more energy than Smagorinsky overall, Smagorinsky dissipating more between $t^*\approx28$ and 40 (§7.2, Fig. 7a). **Shown**
15. Case 3: all models peak in dissipation rate at $t^*\approx8$, in "good agreement" with Brachet et al. (peak at $t^*\approx9$) and the LES of Rafei et al.; the R-DSGS models have the highest peak (§7.2, Fig. 7b). **Shown**
16. Case 3: all models show an inflection near $t^*\approx5$ in dissipation rate and effective viscosity, read as the breakdown of the vortex tubes (§7.2). **Shown** (interpretation **Stated**)
17. Case 3: nodal DSGS gives the largest enstrophy, Smagorinsky, Vreman and elemental DSGS the lowest; magnitudes agree with Shu et al., Drikakis et al. and Rafei et al. (§7.2, Fig. 7c). **Shown**
18. Case 3: all spectra peak at $k\approx3$ (the imprint of the initial condition) and follow $k^{-5/3}$ for $k<32$ (§7.2, Fig. 8). **Shown**
19. Case 4 (density current): Kelvin–Helmholtz rotors appear at $\Delta x=50$ m with Smagorinsky and Vreman, at 25 and 12.5 m with DSGS; nodal DSGS resolves rotors on coarser grids than elemental DSGS (§8.2, Fig. 10). **Shown**
20. Case 4: Smagorinsky and Vreman give similar enstrophy, consistently above DSGS; all models, and a constant viscosity of 75 m$^2$s$^{-1}$, follow the same trend until $t=300$ s (§8.2, Fig. 9a–c). **Shown**
21. Case 4: spectra over $x\in[5000,15000]$ m, $z\in[0,4000]$ m (made periodic by Errico's detrending) follow $k^{-5/3}$ at low $k$ and Kraichnan's $k^{-3}$ at high $k$ (§8.2, Fig. 9d–f). **Shown**
22. Case 4: front locations at $t=900$ s lie in [14600, 15040] m at 50 m (literature [14400, 15030] m), [14900, 15120] m at 25 m and [15075, 15160] m at 12.5 m; the front advances with refinement for every model except Smagorinsky (15034, 15117, 15091 m) (§8.2, Table 2). **Shown**
23. Case 4: Smagorinsky and Vreman give the largest tracer over- and undershoots (negative concentrations), which elemental DSGS damps (§8.2; figures in the Supplementary Material, not in the file). **Shown** (by reference)
24. Vreman's model "has not been previously studied within the spectral element framework or in the context of atmospheric flows" to the authors' knowledge (§3.2, p. 4). **Stated**
25. Only two earlier works analysed the density current within an LES framework (§8.1, p. 17). **Stated**
26. Conclusions: Smagorinsky, Vreman and R-DSGS capture sharp discontinuities; Smagorinsky and Vreman show Gibbs oscillations that DSGS damps; DSGS is the more robust stabilization; Smagorinsky and Vreman resolve rotors at much lower resolution; nodal R-DSGS best preserves kinetic energy; all show the Kolmogorov–Kraichnan spectrum (§9). **Shown** (summary)

The filtered momentum equation and closures (Eqs. 3–7, 10), translated: with $\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$,
$$\frac{\partial\tilde u_i}{\partial t}+\tilde u_j\frac{\partial\tilde u_i}{\partial x_j}+\frac1{\bar\rho}\frac{\partial\bar p}{\partial x_i}=-\frac1{\bar\rho}\frac{\partial\tau_{ij}}{\partial x_j}-g\delta_{i3},\qquad\tau_{ij}=-2\nu_tS_{ij}\ \text{(as printed: full tensor, no }\bar\rho\text{)},$$
and the momentum residual $\mathcal R(\tilde u_i)$ is the left-hand side plus $g\delta_{i3}$ (R-DSGS), or the same without $\partial\tilde u_i/\partial t$ (T-DSGS). The cap (Eq. 11) is $\nu_{\max}=0.5\,\Delta\,\big\lVert\,\lvert\tilde{\boldsymbol u}\rvert+\sqrt{\gamma\bar p/\bar\rho}\,\big\rVert_\infty$. Smagorinsky (Eq. 8): $\nu_t=(C_s\Delta)^2\lvert S\rvert$.

# Printed slips

- Title "Compressible Navier-Stokes Equations", while §2 solves "the time-dependent compressible Euler equations" and no molecular viscosity appears.
- §3.1: "the rate of strain tensor $S_{ij}=(\partial_ju_i+\partial_iu_j)$", without the $\tfrac12$ of the definition on p. 4.
- Table 1: $\bar\Delta=(\Delta x\Delta y\Delta z)^{1/3}/N$, while the width used (§3.4) and $a_{1,2}$ in the same table divide by $N+1$.
- Eq. 14a calls $\mu$ a "dynamic viscosity", but it has kinematic units ($\nu_{\max}=0.5\Delta\times$ a velocity; constant runs quoted as "$\mu=75$ m$^2$s$^{-1}$"); Eq. 4, $\tau^{SGS}_{ij}=-2\mu S_{ij}$, omits the $\bar\rho$ of the definition of $\tau^{SGS}_{ij}$.
- Eq. 12 has an outer "max" on a scalar ratio that Eqs. 13a–b omit; §3.3 lists Eqs. 11, 12 and 13a for the elemental norm but not 13b, used in Case 1.
- Fig. 9 caption: "Evolution with time of the turbulent energy dissipation rate" for panels (a)–(c), which plot enstrophy (§8.2 "evolution of enstrophy"); §8.2 says "Figures 9a - Fig. 9c show the evolution of enstrophy and the kinetic energy spectrum", the spectra being 9d–f.
- §8.2: "comparing Figs. 10l and 10n", which show different models at different resolutions (T-DSGS:E at 12.5 m, R-DSGS:N at 25 m).
- §9: "Although the Smagorinsky model is able to preserve stability until t = 0.7 s, it did result in severe oscillations", whereas §6.2 says "the Smagorinsky model does not diverge" and shows it at $t=1.0$ s; 0.7 s is the Vreman divergence time.
- Abstract: "The Smagorinsky and Vreman models are better able to resolve the finer flow structures in shear flows"; §9 has nodal R-DSGS "resolve[s] finer flow structures (Case 4)" and §8.2 "the R-DSGS models produce the least diffused rotor structures".
- §7.2: "elemental T-DSGS and R-DSGS models are the most dissipative of the six", then "The dissipation rate of the R-DSGS models is consistently higher than the remaining models".
- §9 calls R-DSGS and T-DSGS "two newly developed models", while §3.3 attributes DSGS to Nazarov & Hoffman (2013).
- References: [5] and [48] are the same Favre (1983) paper, [10] and [52] the same Deardorff (1970) paper (first pages 453 and 452); [25] prints "M. J. Brazell, M. Brazell".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $G_{\bar\Delta}$, $\bar\Delta$ | $\bar\phi$, $G$, $\Delta$ | implicit grid filter; footnote 1 makes bar and tilde both "grid-resolved" |
| $\tilde\phi=\overline{\rho\phi}/\bar\rho$ | $\tilde\phi$ | Favre filter, agrees |
| $\hat\cdot$ | $\langle\cdot\rangle_\Omega$ (space average over the domain, page-local) | **collision:** not a test filter |
| $\tau^{SGS}_{ij}$ | $\tau_{ij}$ (compressible form) | positive convention, agrees; closure on the full tensor, not $\tau^d_{ij}$ |
| $S_{ij}$, $\sqrt{2S_{ij}^2}$ | $S_{ij}$, $\lvert S\rvert$ | §3.1 prose drops the $\tfrac12$ |
| $\mu$, $\nu_t$ | $\nu_t$ | the source's $\mu$ is kinematic |
| $\mu_{\max}$, $\mu_{res}$ | $\nu_{\max}$, $\nu_{\mathrm{res}}$ (page-local) | |
| $\kappa$, $\alpha$ | $\kappa_\vartheta$, $\alpha_q$ (SGS diffusivities of potential temperature and tracer, page-local, as on the [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md) page) | **collision:** bare $\kappa$ is the von Kármán constant and bare $\alpha$ the blending factor in the registry |
| $\Theta^{SGS}_j$, $Q^{SGS}_j$ | (SGS fluxes of potential temperature and tracer) | |
| $\theta$, $q$ | $\vartheta$, $q$ (potential temperature, tracer concentration, page-local) | **collision:** $\theta$ is the momentum thickness in the registry |
| $R(\cdot)$, $C$ | $\mathcal R(\cdot)$ (residual of the filtered inviscid equation, page-local), $C$ (DSGS scaling, $C=1$) | |
| $\mathrm{Pr}$ | $Pr$ (artificial, 0.7) | |
| $C_s$, $c$, $\beta_{ij}$, $B_\beta$, $\Delta_k$ | $C_s$, Vreman constant, Vreman tensor and invariant, $\Delta_k$ | |
| $N$ | $N$ | $N=4$ |
| $\Delta x$, $\Delta y$, $\Delta z$ | $h_x/N$, $h_y/N$, $h_z/N$ ("effective resolution") or $h_x$, $h_y$, $h_z$ (element sizes, page-local) | the printed resolutions of Cases 1–3 equal the element size over $N$ *(compiler check, not in the sources)*; the filter width $\min(\Delta x,\Delta y,\Delta z)/(N+1)$ is written with the element sizes on the concept pages |
| $\chi_i$, $\omega_i$, $\psi_i$, $\mathcal P_N$ | $\xi_i$, $w_i$, (Lagrange basis), (Legendre polynomial) | **collision:** $\omega_i$ is the vorticity in the registry |
| $E$, $E^*$, $\varepsilon$, $\langle\omega^2\rangle$, $\nu_{eff}$ | $K$ (volume-averaged kinetic energy), normalized, $\varepsilon$, enstrophy, (effective viscosity, $\varepsilon=\nu_{\mathrm{eff}}\langle\omega^2\rangle$) | **collision:** $E$ is total energy in the registry |
| $k$ | Taylor–Green wavenumber (1 m$^{-1}$) and spectral wavenumber | |
| $t^*=ku_0t$, $Re=u_0/k\nu$ | (Taylor–Green time and Reynolds number) | no $\nu$ is defined for the Euler runs |
| $\rho_R$, $\theta_R$, $p_R$ | (hydrostatic reference state) | |

# Reference list

86 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Two printed
duplicates: [5]/[48] (Favre 1983) and [10]/[52] (Deardorff 1970). Marras et
al. (2021, "In review") is kept as its own pre-publication entry. Several
items print no volume or pages ([4], [55], [56], [68], [84]).

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Residual-based dynamic subgrid-scale model](/methods/residual-based-dynamic-sgs-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Vreman model](/methods/vreman-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
