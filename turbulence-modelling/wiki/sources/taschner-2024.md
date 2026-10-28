---
type: Source
title: "Taschner et al. (2024) — A new coupling of a GPU-resident large-eddy simulation code with a multiphysics wind turbine simulation tool"
description: "Couples the GPU-resident anelastic Smagorinsky LES code GRASP to the OpenFAST turbine tool through actuator line and filtered actuator line models; cross-verifies the NREL 5-MW rotor against four LES codes, and shows the filtered model reduces but does not remove the kernel-width dependence of rotor loads."
resource: "doi:10.1002/we.2844"
source_kind: paper
authors: [Taschner E., Folkersma M., Martínez-Tossas L.A., Verzijlbergh R., van Wingerden J.-W.]
year: 2024
venue: "Wind Energy 27:1152–1172"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Wind_Energy_Taschner_A_new_coupling_of_a_GPUresident_largeeddy_simulation_code_wi.pdf"
tags: [les, wind-energy, gpu, sgs-model, software]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Taschner et al. (2024) couple GRASP, a GPU-resident atmospheric
[LES](/definitions/large-eddy-simulation.md) code (anelastic,
[Smagorinsky](/methods/smagorinsky-model.md) closure with $C_s=0.16$,
second-order central differences on a staggered grid, third-order
Runge–Kutta, FFT pressure solver), to the turbine tool OpenFAST
(aerodynamics, structural dynamics, control) through a new C++ plugin,
AspFAST. Rotor forces enter the LES through the
[actuator line model](/methods/actuator-line-model.md), with point forces
spread by a Gaussian kernel of width $\epsilon_{\mathrm G}$, and optionally
through the filtered actuator line correction of Martínez-Tossas & Meneveau,
written here in vector form for a rotating blade. The motivation is
wind-farm control research that needs flow and turbine dynamics together on
GPU hardware.

Three cases verify the coupling. On the NREL 5-MW turbine in uniform laminar
inflow, blade loads and the near wake agree with four reference LES codes
(including [LESGO](/software/lesgo.md)); the far wake has lower Reynolds
stresses and a slightly asymmetric vertical profile, which the authors
attribute to a coarser kernel resolution ($\epsilon_{\mathrm G}/\Delta x\approx3.39$
against about 5, limited by one 40 GB GPU) and to the missing zero-shear
bottom boundary. The order of wake transition across codes is discussed
through the [numerical dissipation](/properties/numerical-dissipation.md)
of pseudo-spectral and second-order schemes. On a translating wing the
filtered model makes the lift independent of the kernel width up to sixteen
times the optimal width $0.25c$, but needs 300 actuator points. On the rotor
it lowers $C_P$ from 0.569 to 0.514 and the thrust coefficient from 0.838 to
0.805 at $\epsilon_{\mathrm G}/D=0.079$, and roughly halves the kernel-width
sensitivity, without full independence; in laminar inflow it delays wake
transition. Two-way coupling is about ten times slower than standalone LES.
An [immersed-boundary](/methods/immersed-boundary-method.md) representation
of tower and nacelle is named as an option only.

# Version read

Version of record (Wiley, open access CC BY-NC-ND, special-issue paper;
received 16 September 2022, accepted 2 June 2023, online 2023, issue 2024),
21 pages, all read, the equation pages and Algorithm 1 checked visually.
Page 1 prints the third author as Luis A. Martínez-Tossas; the Crossref
record splits the name as "A Martínez-Tossas L." (a metadata artefact).

# Key claims

1. The GRASP–OpenFAST coupling through the actuator line gives blade loads and near-wake results consistent with four reference LES codes (LESGO, SOWFA, SP-Wind, EllipSys3D); deviations appear in the far wake (Abstract, §4.1, Figs. 2–6). **Shown**
2. The filtered actuator line reduces the lift and power overprediction of the actuator line on coarse grids (Abstract, §4.2–4.3, Fig. 9, Table 4). **Shown**
3. The optimal kernel width is about 25% of the local chord, which implies grids too fine for wind farms (§1, citing ref. 21). **Stated**
4. A kernel wider than optimal underestimates the induced velocity, giving larger angles of attack and overpredicted torque and power (§2.3, citing refs. 21, 25). **Stated**
5. GRASP solves the anelastic filtered equations with the Smagorinsky closure $\tau_{ij}=-2\rho_b(C_s\Delta)^2|\bar S|\bar S_{ij}$, $\Delta=(\Delta_x\Delta_y\Delta_z)^{1/3}$, on an Arakawa C-grid with second-order central advection, third-order Runge–Kutta and an FFT pressure solver (§2.1, Eqs. 1–4). **Stated**
6. The point force is spread by the isotropic Gaussian $\eta_\epsilon=\epsilon_{\mathrm G}^{-3}\pi^{-3/2}\exp(-|\boldsymbol x-\boldsymbol x^k|^2/\epsilon_{\mathrm G}^2)$ (Eqs. 10–11), evaluated only where it exceeds 0.1% of its centre value (§2.3; App. B). **Stated**
7. OpenFAST uses $N_F$ force points and $N_V$ velocity points per blade, in general $N_F\neq N_V$, $N_V$ set by the blade stations (§2.3). **Stated**
8. In the cross-verification GRASP reaches only $\epsilon_{\mathrm G}/\Delta x\approx3.39$ against about 5 in the references, which "most likely" explains its smaller axial blade velocities; refined tests on smaller domains move GRASP toward the references (§4.1; tests not shown in detail). **Shown**
9. Outflow fringe forcing affects wake recovery and the transition location; the domain is lengthened from $24D$ to $53.25D$ (§3.1, §4.1). **Shown**
10. Wake transition is earliest in SP-Wind ($x/D\approx5.5$), then EllipSys3D and LESGO; SOWFA and GRASP transition furthest downstream, at $x/D\approx10$ (§4.1, Fig. 6). **Shown**
11. Pseudo-spectral horizontal discretization (LESGO, SP-Wind) gives earlier transition and faster wake recovery than second-order finite differences (§4.1, citing ref. 53). **Stated**
12. GRASP's staggered grid should improve accuracy over SOWFA's collocated grid (citing ref. 56), but the coarser resolution cancels the gain; GRASP's Reynolds stresses are smaller throughout the wake (§4.1). **Shown**
13. GRASP's far-wake vertical velocity profile at $x/D=15$ is slightly asymmetric; the missing zero-shear bottom condition is the authors' hypothesis, to be tested (§4.1, Fig. 3). **Shown**
14. Wing: the filtered correction is converged at $\epsilon_{\mathrm G}/\Delta x=4$ for $\epsilon_{\mathrm G}/c=1,2,4$, in line with convergence for $\epsilon_{\mathrm G}/\Delta x>2.8$ found earlier (§4.2, Fig. 8, citing ref. 25). **Shown**
15. Wing: the filtered-model lift is independent of the kernel width even 16 times the optimum and matches the actuator line with $\epsilon_{\mathrm G}=0.25c$ (§4.2, Fig. 9). **Shown**
16. The filtered model rests on the numerically computed spanwise lift gradient; $N_F=300$ was needed on the wing, and actuator points clustered at the tips are suggested (§4.2). **Shown**
17. Rotor: toward the tip the ratio of optimal to resolved induced velocity reaches about 12 (§4.3, Fig. 11). **Shown**
18. Rotor: the optimal induced velocity changes sign at $r/R\approx0.16$ (no lift on the circular root sections, upwash from shed vorticity at the strong lift gradient) (§4.3). **Shown**
19. Rotor: the filtered model lowers the angle of attack for $r/R>0.75$, and with it lift, tangential and normal forces, power and thrust (§4.3, Fig. 12). **Shown**
20. At $\epsilon_{\mathrm G}/D=0.079$, $C_P=0.569$ (actuator line) and 0.514 (filtered), thrust coefficient 0.838 and 0.805; going to $\epsilon_{\mathrm G}/D=0.11$ raises $C_P$ by 3.51% and 1.56% and the thrust coefficient by 1.31% and 0.50% (Table 4). **Shown**
21. On coarse rotor grids the filtered model reduces but does not remove the dependence on $\epsilon_{\mathrm G}$ and $\Delta x$, consistent with Blaylock et al. at $\epsilon_{\mathrm G}/\Delta x=2$; a larger $\epsilon_{\mathrm G}/\Delta x$ is expected to help (§4.3). **Shown**
22. The lower normal loading of the filtered model reduces induction and shear-layer steepness and delays laminar–turbulent wake transition for both widths; the conclusion holds for laminar inflow only (§4.3, Fig. 13). **Shown**
23. The treatment of tip blade data (zero-chord interpolation or extrapolation) changes the tip lift and is a source of inter-code deviation (§3.1, §4.1, §4.3). **Shown**
24. Standalone LES is about one order of magnitude faster than two-way coupling for medium and large cases, one-way coupling about twice as fast as two-way; the A100 node beats an RTX 3090 on all cases both hold (App. B, Fig. B1). **Shown**
25. The filtered correction itself costs little; the overhead comes from the larger $N_F$: $N_F=163$ with the filtered model lowers steps per wall-clock second by about 25% against $N_F=55$ with the actuator line (App. B). **Shown**
26. Rotor at $\epsilon_{\mathrm G}/D=0.11$: $N_F=55$ misses the tip lift drop, its magnitude needs at least $N_F=163$, full convergence about 300; $C_P$ and thrust differences between $N_F=55$ and 307 are about 1.8% and 0.7% (filtered) against 0.014% and 0.011% (actuator line) (App. C, Fig. C2). **Shown**
27. $\epsilon_{\mathrm G}/\Delta x>2$ avoids numerical oscillations (citing ref. 19), and $\epsilon_{\mathrm G}/\Delta x=5$ was found necessary for fully converged results (citing ref. 55) (§3.3). **Stated**

The filtered correction (Eqs. 12–20) in the notation of the
[actuator line](/methods/actuator-line-model.md) page, with
$\boldsymbol\Gamma_U$ (page-local, there written $\Gamma_U$) the force
component perpendicular to the estimated unperturbed velocity
$\boldsymbol U_\infty$ per unit span and density (Eq. 14), $\Delta\boldsymbol\Gamma_U$
its central spanwise difference (Eqs. 15–17), and $f_u=0.1$ an
under-relaxation factor:

$$\boldsymbol u_{\mathrm{ind}}(\boldsymbol x^k;\epsilon_{\mathrm G})\approx-\sum_{l=1}^{N_F}\frac{\Delta\boldsymbol\Gamma_U(\boldsymbol x^l)}{|\boldsymbol U_\infty(\boldsymbol x^l)|\,4\pi\,(\boldsymbol x^k-\boldsymbol x^l)}\Big(1-e^{-|\boldsymbol x^k-\boldsymbol x^l|^2/\epsilon_{\mathrm G}^2}\Big),$$

$$\Delta\boldsymbol u^n_{\mathrm{ind}}=f_u\big[\boldsymbol u^n_{\mathrm{ind}}(\epsilon^{\mathrm{opt}}_{\mathrm G})-\boldsymbol u^n_{\mathrm{ind}}(\epsilon^{\mathrm{LES}}_{\mathrm G})\big]+(1-f_u)\big[\boldsymbol u^{n-1}_{\mathrm{ind}}(\epsilon^{\mathrm{opt}}_{\mathrm G})-\boldsymbol u^{n-1}_{\mathrm{ind}}(\epsilon^{\mathrm{LES}}_{\mathrm G})\big],$$

added to the sampled velocity at the force points (Eq. 20); the projection
keeps the coarse kernel. The distance in the denominator is printed as the
vector difference $(x^k_i-x^l_i)$.

# Printed slips

- Eq. 17 prints "$k=N_F$: $\Delta G^{n-1}_i(x^1_i)=-G^{n-1}_i(x^{N_F}_i)$": the left-hand argument is $x^1_i$, the index of the $k=1$ case (Eq. 15).
- App. B says that for "the simulation from Section 3.1 (red square in Figure B1) … the $\epsilon/\Delta x$ ratio is equal to five rather than two"; Table 1 and §4.1 give $\epsilon/\Delta x=3.39$ for that case.
- The Table 3 caption repeats "Parameter settings for the ALM cross-verification case", the caption of Table 1; Table 3 holds the case of §3.3.
- App. B states that App. C concludes "at least $N_F=150$ is required"; App. C prints "at least $N_F=163$ points".
- §4.3 prints "a grid resolution of $\epsilon/\Delta x=3$", Table 3 "≈3".
- Spellings as printed: "Smagorinski" (§3.2), "Grasp" (§2.1), "OpenFast" (§3.2, Algorithm 1); Fig. B1 labels the RTX 3090 "GTX".
- Ref. 46 DOI printed "doi:10.1175/MWRD-14-00293.1".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde u_i$ | $\bar u_i$ | **collision:** the tilde is the LES filter, not a Favre filter |
| $\rho_b(x_3)$, $\rho'$, $b$ | (anelastic reference density, density deviation, buoyancy, page-local) | $x_3$ vertical |
| $\tilde p'$, $\langle\cdot\rangle$ | (pressure deviation from the horizontal mean, page-local) | **collision:** $\langle\cdot\rangle$ is the horizontal mean |
| $\tau_{ij}=-2\rho_bK_m\tilde S_{ij}$ | $\tau_{ij}=-2\rho_b\nu_t\bar S_{ij}$ | eddy-viscosity form; no trace or deviatoric statement printed |
| $K_m$ | $\nu_t$ | |
| $\sqrt{2\tilde S_{ij}\tilde S_{ij}}$, $C_s$, $\Delta$ | $\lvert\bar S\rvert$, $C_s$, $\Delta$ | agree |
| $f_c$, $u^g_j$, $f^{WT}_i$, $f^{Fringe}_i$ | (Coriolis parameter, geostrophic wind, turbine force, fringe force, page-local) | |
| $\alpha(x,y,z)$, $\eta$ (fringe) | (fringe weight and factor, page-local) | **collision** with $\alpha$ (angle of attack, blending factor) and $\eta$ (Kolmogorov length) |
| $\epsilon$, $\epsilon^{LES}$, $\epsilon^{Opt}$, $\eta_\epsilon$ | $\epsilon_{\mathrm G}$, $\epsilon^{\mathrm{LES}}_{\mathrm G}$, $\epsilon^{\mathrm{opt}}_{\mathrm G}$ (registry §11) | **collision** with $\varepsilon$ |
| $G_i=\tfrac12cC_LU_{j,\infty}U_{j,\infty}$ (vector) | $\boldsymbol\Gamma_U$ (page-local, as on the actuator-line page) | |
| $u_{i,ind}$, $\hat u_i$ | $\boldsymbol u_{\mathrm{ind}}$, $\boldsymbol u_{\mathrm{corr}}$ | **collision:** the hat is not a test filter |
| $x^k_i$, $x^q_i$, $N_F$, $N_V$ | (force and velocity actuator points and their numbers, page-local) | |
| $U_{Rel}$, $\phi$, $\alpha$, $\gamma$, $\Omega$ | (relative speed, inflow angle, angle of attack, twist plus pitch, rotor speed, page-local) | **collision** with $\gamma$ and $\Omega_{ij}$ |
| $C_P$, $C_T$ | $C_P$ (power coefficient, page-local), $C_{\mathrm{Th}}$ (registry §11) | **collision:** $C_P$ is not the pressure coefficient $C_p$ |
| $\overline{u'_xu'_x}$ | $R_{11}$ (time average) | the overbar is a time average here |
| $D$, $R$, $S$, $c$ | $D$, $R_{\mathrm r}$ (registry §11), (wing span, chord, page-local) | **collision:** $S$ is not the strain rate |

# Reference list

57 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. 26 (Stanly
et al. 2022) is the ingested [stanly-2022](/sources/stanly-2022.md). The two
Schalkwijk 2015 works (refs. 40, 46) are keyed in printed order. Ref. 24 is
an arXiv preprint and its own entry; ref. 49 (OpenFAST on GitHub) is undated;
ref. 8 prints the journal name and DOI of the discussion paper with the volume
and pages of the final paper, recorded as printed. All items parsed.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Actuator line and actuator disk models](/methods/actuator-line-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [LESGO](/software/lesgo.md)
