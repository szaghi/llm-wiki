---
type: Source
title: "Zhao et al. (2023b) — Turbulence simulations with an improved interior penalty discontinuous Galerkin method and SST k-ω model"
description: "Couples an interior penalty discontinuous Galerkin discretization of the compressible RANS equations, with a jump-based lifting term that avoids the viscous homogeneity tensor, to a first-order finite-volume k-ω SST model with a dilatational compressibility correction, validated from laminar verification cases to a Mach 2.92 cavity–ramp flow."
resource: "doi:10.1016/j.compfluid.2023.105967"
source_kind: paper
authors: [Zhao M., Wei T., Hao S., Ding Q., Liu W., Li X., Liu Z.]
year: 2023
venue: "Comput. Fluids 263:105967"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computers_amp_Fluids_Zhao_Turbulence_simulations_with_an_improved_interior_penalty_dis.pdf"
tags: [rans, dg, compressible, eddy-viscosity]
timestamp: 2026-10-26T07:38:00Z
---

# Summary

Zhao et al. (2023b) solve the compressible Reynolds-averaged equations with
an interior penalty discontinuous Galerkin (IPDG) method closed by the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md), with and without the
compressibility correction of Suzen & Hoffmann. The "improved IPDG" of the
authors' earlier work replaces the penalty term, which contains the
fourth-order homogeneity tensor (the Jacobian of the viscous flux with respect
to the solution gradient), by a lifting quantity: the viscous flux evaluated
with the interface jump in place of the gradient. The tensor is therefore
never formed. The mean-flow equations are discretized at high order, while the
two SST equations are discretized by a first-order cell-centred finite-volume
scheme on the same mesh, for stability and positivity of the turbulence
variables. The eddy viscosity of the [Boussinesq closure](/definitions/boussinesq-hypothesis.md)
is passed to the mean flow as a piecewise constant. Time integration is BDF2
with Newton–Krylov iterations, and shocks are stabilized by Hartmann's
flux-divergence artificial viscosity.

The solver reaches close to its design orders on an isentropic vortex and
Couette flow and matches the Blasius and lid-driven-cavity references. A
zero-pressure-gradient [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)
at $M=0.2$ agrees with references in the [log layer](/definitions/law-of-the-wall.md).
NACA 0012 runs at $M=0.15$ (0° and 10°) and transonic $M=0.804$ follow.
The transonic shock ends slightly behind the measured position, which the
authors attribute to an overestimated [shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
In the Settles cavity–ramp flow at $M=2.92$, the uncorrected model gives
excess eddy viscosity and a too-wide shear layer; the corrected model
reproduces the measured shear-layer velocity profiles. The paper performs no
scale-resolving computation. Its introduction reviews DG for
[implicit LES](/definitions/implicit-les.md), with the
[numerical dissipation](/properties/numerical-dissipation.md) of the DG order
and of the Riemann solver, DG [DES](/methods/detached-eddy-simulation.md) and
DG [Spalart–Allmaras](/methods/spalart-allmaras-model.md) positivity fixes,
within the [discontinuous Galerkin family](/methods/discontinuous-galerkin-spectral-element-method.md).

# Version read

Version of record (Elsevier typeset; received 25 January 2023, revised 25
April 2023, accepted 7 June 2023), 14 pages, all read; the equations of pp.
3–4 were read visually because the text layer garbles them. Page 1 matches
the metadata (title, seven authors in the same order, venue, article number,
DOI).

# Key claims

1. The standard IPDG viscous penalty needs the fourth-order homogeneity tensor $\partial F^\nu/\partial\nabla U$, "difficult to calculate"; the lifting quantity $L=-F^\nu(U,[U])$, which uses the linearity of the viscous flux in its gradient argument, removes it and gives the weak form Eq. 3-7 (§1, §3.1, Eqs. 3-1–3-7). **Derived** (from the authors' earlier work, ref. [34])
2. The mean flow is discretized by IPDG and the SST equations by first-order finite volumes in a "hybrid framework of DG and FVM … to pursue numerical stability and positivity"; turbulence quantities are piecewise constant per element and the velocity gradients are $L^2$-projected onto the finite-volume space (§1, §3.2; idea attributed to Burgess & Mavriplis, ref. [22]). **Stated**
3. The convective flux is local Lax–Friedrichs with $\lambda_{\max}=|\boldsymbol u\cdot\boldsymbol n|+c$ (Eq. 3-8); the viscous flux is the average of the two viscous fluxes plus the penalty $C_{IP}(N^2/h_f)L\cdot\boldsymbol n$, $C_{IP}$ "a sufficiently large constant" whose value is not printed (Eq. 3-9). **Stated**
4. Shocks are stabilized by the artificial viscosity $\nu_s=C_\varepsilon h^{2-\beta_s}|-\nabla\cdot(F^c-F^\nu)|$ of Hartmann (ref. [40]) (Eq. 3-10), which concentrates around the shock in the transonic case (§3.1, §5.3, Fig. 5-12). **Shown** (qualitative)
5. SST closure as printed: $\mu_t=\min[\rho k/\omega;\ \rho a_1k/(\Omega F_2)]$ with $a_1=0.31$ and $\Omega=|S_{ij}|$ (a strain-based limiter; the normalization of the magnitude is not printed), with $F_1$, $F_2$ and the cross-diffusion floor $10^{-20}$; the other coefficient values are not printed (§2, Eqs. 2-2–2-4). **Stated**
6. Compressibility correction (Suzen & Hoffmann, ref. [39]): the $k$ dissipation becomes $[1+\alpha_1M_t^2(1-F_1)]\beta^*\rho k\omega$, a matching term enters the $\omega$ equation, and a pressure-dilatation model $-\alpha_2\tau_{ij}\partial_ju_iM_t^2+\alpha_3\rho\beta^*k\omega M_t^2$ is added, all through $(1-F_1)$, with $\alpha_1=1.0$, $\alpha_2=0.4$, $\alpha_3=0.2$ (§2, Eq. 2-5). **Stated**
7. The wall value $\omega_w=10\cdot6\nu/(\beta y^2)$ is imposed "according to [17]"; the constant $C_w$ "should be adjusted to the numerical discretization scheme": 2.5 in ref. [41], 0.3 in Bassi et al. (ref. [17]), "reset to 0.01" here (§3.2). **Stated**
8. Time integration is second-order BDF with Newton iterations and GMRES (§3.2). **Stated**
9. Isentropic vortex: entropy $L^2$ errors on four meshes give orders 1.58, 2.12, 2.25 (DG(2)), 1.69, 3.14, 2.80 (DG(3)) and 3.39, 3.87, 4.14 (DG(4)); the methods "could reach the design accuracy for most of the cases, especially when the mesh resolution is fine enough" (§4.1, Table 4-1). **Shown**
10. Couette flow: density $L^2$ errors give orders 1.97, 1.70 (IPDG(2)), 3.02, 2.86 (IPDG(3)) and 4.11, 4.26 (IPDG(4)); the loss on the finest mesh of IPDG(2) is attributed to "temporal errors" (§4.2, Table 4-2). **Shown** (attribution **Stated**)
11. The laminar flat plate at $M=0.5$ matches the Blasius velocity profiles and skin friction, including near the leading edge (§4.3, Figs. 4-4, 4-5). **Shown**
12. Lid-driven cavity at $Re=1000$ on $40\times40$ elements: the difference from Ghia et al. decreases with order; IPDG(1) "could be regarded as a finite volume method" and IPDG(4) coincides with the reference near the walls (§4.4, Figs. 4-6, 4-7). **Shown**
13. Turbulent flat plate ($M=0.2$, $Re=1.12\times10^7$ on the plate length, first cell at $y^+=1$): the velocity profile agrees with ref. [46] in the log layer and the turbulent kinetic energy with ref. [45] (§5.1, Fig. 5-2). **Shown**
14. NACA 0012 at $M=0.15$, $Re_c\approx6\times10^6$, 0°: IPDG(1)–(3) pressure coefficients coincide with Ladson's experiment on 5883 elements; IPDG(2) is retained; meshes of 6834, 8844 and 10854 elements show grid independence of $C_p$ (§5.2, Fig. 5-4). **Shown**
15. At 10° the $C_p$ agrees with experiment; differences from the SUPG Spalart–Allmaras results of ref. [48] at the upper-surface leading edge "might be interpreted by the turbulence model"; mean-flow and turbulence residuals decrease steadily (§5.2, Fig. 5-6). **Shown**
16. Force coefficients: $C_L=0.00$, $C_D=0.0084$ at 0° and $C_L=0.93$, $C_D=0.011$ at 10°, against 0.00, 0.0083, 1.05, 0.012 (McCroskey, ref. [49]); the 10° discrepancy is "probably" attributed to the RANS assumption (§5.2, Table 5-1). **Shown**. The 10° lift is 11.4% below the reference *(compiler check, not in the sources)*.
17. Transonic NACA 0012 ($M=0.804$, $Re=4.09\times10^6$, 0.05°, IPDG(2), 8954 cells): the shock sits at $x\approx0.47$ with upper and lower extrema consistent with ONERA data, but "the ending position of the shock wave slightly lags behind", attributed to an overestimated shock-wave/boundary-layer interaction (§5.3, Figs. 5-9–5-11). **Shown**
18. Settles cavity–ramp at $M=2.92$: without the correction "the original model produces excessive turbulent viscosity and in fact the solution is dissipative", widening the shear layer and the shock and expansion regions; with it, the velocity profiles at three shear-layer stations agree with Settles et al. and without it they "obviously deviate" (§5.4, Figs. 5-14, 5-15). **Shown**
19. "To our knowledge, there has been rarely any DG attempt introducing a compressibility correction within the RANS turbulence model" (§2). **Stated**
20. From the cited literature: DG is "spectrally compatible with a subgrid-scale model" (ref. [24]); raising the DG order increases dissipation at the largest wavenumbers and narrows its range, so DG suits ILES, and the Riemann solver strongly influences DG ILES (ref. [25]); Roe was more robust than Lax–Friedrichs in an inviscid Taylor–Green ILES (ref. [26]); viscous penalty fluxes can replace the stabilizing effect of nonlinear fluxes (ref. [27]) (§1). **Stated** (cited)
21. In DG RANS, Bassi et al. solved for $\log\omega$, Crivellini et al. modified the Spalart–Allmaras source and diffusion terms only where the working variable or closure functions become negative, and ref. [20] used an always-positive auxiliary variable (§1). **Stated** (cited)

# Printed slips

- **Viscosities of the two SST forms.** Eq. 2-2 writes $(\mu_L+\sigma_k\mu_T)$; Eq. 2-5 writes $(\mu+\sigma_k\mu_t)$ while §2 defines $\mu=\mu_L+\mu_T$, so Eq. 2-5 read literally counts the eddy viscosity twice.
- **Undefined symbols.** $\upsilon_t$ (last term of the $\omega$ equation in Eq. 2-5) and $M_t$ are not defined.
- **Wall value of $\omega$ (§3.2).** "$\omega_w=10\frac{6\nu}{\beta y^2}$" carries a fixed factor 10 and no $C_w$, yet "$C_w=\sqrt{\frac{50^2}{10}\frac{\beta}{6}}$ should be adjusted" and is "reset to 0.01"; the formula through which $C_w$ enters is not printed.
- **Jump (§3.1).** $[U]$ is called "the difference across the element edge" but defined as $\frac12(U^+-U^-)\otimes n$.
- **Order definition (§4.1).** "the numerical order is defined as the logarithm of the numerical error"; the printed orders are base-2 logarithms of successive error ratios *(compiler check, not in the sources)*. §4.1 calls Table 4-1 the "L2 error of entropy", its caption only "L2 error".
- **Citation (§1).** "the numerical studies by Fortin et al [30]" are cited among DG DES studies, while ref. [30] is printed as "A very high order discontinuous Galerkin method for the numerical solution of stiff DDEs".
- **Symbol reuse.** $\Omega$ is the strain magnitude in Eq. 2-4 and the element domain in Eqs. 3-3–3-7; $\beta$ is an SST coefficient and the artificial-viscosity exponent; $\varepsilon$ is the vortex strength in §4.1.
- **Reference list.** Ref. [9] "Comput. Methods Appl. Mech. English"; ref. [45] "AIAA Journal 1999;99(0745):1–19"; ref. [25] first author "Wiart C C" and last author "Winckelmanset G" (the text says "Carton de Wiart et al."); ref. [33] pages "15-00418-15-00418".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U=[\rho,\rho u,\rho v,\rho w,\rho E]$ | (conservative variables, page-local) | Reynolds-averaged; the averaging (Reynolds or Favre) is not stated |
| $\vec q=(u,v,w)$ | $\boldsymbol u$ | |
| $F^c$, $F^\nu$, $\hat F^c$, $\hat F^\nu$ | (convective and viscous fluxes), $f^*$ (interface numerical fluxes) | $F^\nu$ printed with a leading minus |
| $\mu_L$, $\mu_T$, $\mu_t$ | $\mu$, $\mu_t$ | molecular and eddy viscosity |
| $\upsilon_t$ | (undefined in the source; the symbol resembles $\nu_t$) | Eq. 2-5 only |
| $\tau_{ij}$ | (total Boussinesq stress, sign not printed) | **collision:** not the SGS stress $\tau_{ij}$ |
| $\Omega=\lvert S_{ij}\rvert$ | $\lvert S\rvert$ | **collision:** not the rotation rate; normalization not printed; also the element domain |
| $k$, $\omega$, $F_1$, $F_2$, $\beta^*$, $\sigma_k$, $\sigma_\omega$, $d$ | same | agree |
| $\beta$ (SST) | $\beta$ (SST destruction coefficient) | values not printed |
| $a_1$, $CD_{k\omega}$, $\sigma_{\omega2}$ | SST limiter constant (0.31), cross-diffusion term, its coefficient | |
| $M_t$, $\overline{p''d''}$, $\alpha_1,\alpha_2,\alpha_3$ | $M_t$, (modelled pressure dilatation), (correction constants 1.0, 0.4, 0.2) | **collision:** the double prime is not a Favre fluctuation here |
| $g$, $\Theta$, $L$, $T$, $\psi$ | (homogeneity tensor, viscous-flux auxiliary variable, jump-based lifting quantity, tensor and scalar test functions; page-local) | |
| $\hat U=\frac12(U^++U^-)$ | $\{\!\{U\}\!\}$ | **collision:** hat is an interface average, not a test filter |
| $[U]=\frac12(U^+-U^-)\otimes n$ | (half-jump times normal) | |
| $p$ (Eq. 3-9) | $N$ | polynomial order in the penalty; **collision:** not the pressure |
| DG($n$), IPDG($n$) | order of accuracy $n$ | "Second-order DG(2)"; the relation to $N$ is not printed |
| $h_f$, $h_e$ | $h$ (face scale, element size) | |
| $C_{IP}$ | (penalty factor) | value not printed |
| $\nu_s$, $C_\varepsilon$, $\beta$ (Eq. 3-10) | (artificial viscosity and its constants; exponent written $\beta_s$ on this page) | **collision** with the SST $\beta$ |
| $\omega_w$, $C_w$, $y$ | (wall value of $\omega$, its constant), $y$ (first-cell wall distance) | |
| $\varepsilon$ (§4.1) | (vortex strength) | **collision:** not the dissipation rate |
| $Re_L$, $Re$ | $Re$ on the plate length or chord | |
| $C_L$, $C_D$, $C_p$ | same | |

# Reference list

53 printed references, numbered [1]–[53]. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. DOIs are
printed only for refs. [30] and [31]. Ref. [25] is keyed under Carton de
Wiart, as the text names the author, although the list prints "Wiart C C".
Same-author same-year works take suffixes in printed order (Bassi 1997, refs.
[6], [7]; Hartmann 2006, refs. [10], [13], [40]). Refs. [8], [11] and [33]
print irregular venue, volume or page fields and are recorded as printed;
refs. [41], [47], [49], [50] are reports. No printed duplicates.

# Pages created or updated

Chunk 4 (2026-10-26), cited further in chunk 5. This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
