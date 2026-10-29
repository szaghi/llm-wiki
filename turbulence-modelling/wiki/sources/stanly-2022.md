---
type: Source
title: "Stanly et al. (2022) — Large-Eddy Simulation of a wind turbine using a Filtered Actuator Line Model"
description: "Implements the filtered actuator line model (a subfilter correction of the velocity sampled at the actuator points) in the compressible implicit-LES code MIRACLES with a per-blade MPI gather–broadcast algorithm; on the NREL Phase VI rotor with a twice-optimal kernel it predicts power within 1% against 13% for the baseline actuator line."
resource: "doi:10.1016/j.jweia.2021.104868"
source_kind: paper
authors: [Stanly R., Martínez-Tossas L.A., Frankel S.H., Delorme Y.]
year: 2022
venue: "J. Wind Eng. Ind. Aerodyn. 222:104868"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Wind_Engineering_and_Industrial_Aerodynamics_Stanly_Large-Eddy_Simulation_of_a_wind_turbine_using_a_Filtered_Act.pdf"
tags: [actuator-line, wind-energy, implicit-les, numerical-dissipation, mpi]
timestamp: 2026-10-29T10:05:00Z
---

# Summary

Stanly et al. (2022) implement the filtered
[actuator line model](/methods/actuator-line-model.md) (F-ALM) of
Martínez-Tossas & Meneveau (2019) in MIRACLES, the authors' high-order
compressible [implicit LES](/definitions/implicit-les.md) code: fourth-order
summation-by-parts finite differences, an eighth-order artificial-dissipation
operator as the only closure (the code's
[numerical dissipation](/properties/numerical-dissipation.md)), fourth-order
Runge–Kutta and analytically stretched grids. The actuator line replaces each
blade by a rotating line of points that apply tabulated lift and drag,
spread onto the grid by an isotropic Gaussian kernel of width
$\epsilon_{\mathrm G}$. The optimal width $\epsilon_{\mathrm G}\approx0.25c$
together with $\epsilon_{\mathrm G}/h\gtrsim2.8$ forces fine grids; wider
kernels give thicker, weaker tip vortices, too little induced velocity, and
overpredicted torque and power. F-ALM corrects the velocity sampled at each
actuator point by the difference between the induced velocities of the
optimal and of the LES kernel, computed from filtered lifting-line theory as
a line integral over the whole blade.

The paper's own contribution is the implementation and its parallelization:
since the correction at one point depends on every point of the line, and the
rank owning a point changes as the blade rotates, one MPI communicator per
blade gathers the line data on its rank 0, solves the integral there and
broadcasts the corrections. The serial code reproduces the stronger tip
downwash of the reference translating-wing case. On the NREL Phase VI
two-bladed rotor (sequence H, $U_\infty=7$ m/s), with a twice-optimal kernel
$\epsilon_{\mathrm G}/c=0.5$ on the same grid, the flow fields of ALM and
F-ALM are indistinguishable, F-ALM predicts stronger induced velocity at the
tip and root and lower tangential force there, and the power is 6.06 kW
(experiment 6.0 kW, ALM 6.778 kW) at 1% extra cost per step. The
introduction surveys actuator lines in [lattice Boltzmann](/methods/lattice-boltzmann-method.md)
solvers and blade-resolved [immersed boundary](/methods/immersed-boundary-method.md)
alternatives; the wake reference (Ravensbergen et al. 2020) uses an actuator
line in a [variational multiscale](/methods/variational-multiscale-method.md)
framework. The rotor material is wind-energy aerodynamics: the paper adds no
turbulence closure to [large-eddy simulation](/definitions/large-eddy-simulation.md).

# Version read

Version of record (J. Wind Eng. Ind. Aerodyn. 222:104868, Elsevier; received
30 May 2021, accepted 1 December 2021, online 7 February 2022), 14 pages, all
read; pages 4, 5 and 8 (Eqs. 15–21, Algorithm 2, Table 3) also checked
visually. Page-1 title, four authors and DOI match the metadata. No identity
problem. Numbering on this page is that of this version.

# Key claims

The Gaussian kernel width is written $\epsilon_{\mathrm G}$ and the
grid spacing $h$ (page-local and registry; the source's $\epsilon$ and
$\Delta$), the rotor radius $R_{\mathrm r}$ and the rotor angular velocity
$\Omega_{\mathrm{rot}}$.

1. "A grid spacing ($\Delta$) of $\Delta\approx\epsilon/2.8$ ... or higher is preferred" (in page notation $h\approx\epsilon_{\mathrm G}/2.8$, the "higher" referring to the ratio $\epsilon_{\mathrm G}/h$, as the Fig. 3 caption's "usually 2.8 or higher is preferred" for $\epsilon/\Delta$ reads) so that the force is spread over more than two points without oscillation; with the optimal $\epsilon_{\mathrm G}=0.25c$ this forces very fine grids (§3). **Stated**
2. Coarser kernels ($\epsilon_{\mathrm G}/c>0.25$ with $\epsilon_{\mathrm G}/h\approx2.8$) predict downstream wakes well but overpredict blade torque and power, "sometimes even exceeding the Betz limit" (§3.1, citing Stevens et al. 2018 and Martínez-Tossas & Meneveau 2019). **Stated**
3. Mechanism: a wider kernel gives thicker, weaker tip vortices, a lower induced velocity, a changed effective angle of attack, and overpredicted torque and power, most at the tip and where $C_L$ or chord varies strongly (§3.1, Fig. 2). **Stated**
4. Earlier tip corrections (Shen et al. 2005; Jha et al. 2014; Zhong et al. 2019; Forsting et al. 2019, 2020) are "mostly based on empirical corrections or fits"; F-ALM is a "well-derived subgrid-scale model" and "a more theoretically consistent version" of the Dağ & Sørensen (2020) model (§1, §3.2). **Stated**
5. F-ALM corrects the sampled velocity by $\Delta u_y=u_y(z_i;\epsilon_{\mathrm G}^{\mathrm{opt}})-u_y(z_i;\epsilon_{\mathrm G}^{\mathrm{LES}})$ from the line integral of Eq. (21); lift is applied perpendicular and drag parallel to the corrected velocity (§3.2, Eqs. 19–21). **Stated** (derived in Martínez-Tossas & Meneveau 2019)
6. F-ALM leaves the shape of the projected tip vortex in the LES field unchanged and corrects only the velocity "felt" by the actuator points (§3.2). **Stated**
7. The serial F-ALM reproduces the trend and peak magnitudes of the spanwise downwash of Martínez-Tossas & Meneveau (2019) on the translating wing ($44^3$ points, $\epsilon_{\mathrm G}^{\mathrm{LES}}/c=2$, 200 actuator points), with a stronger downwash than ALM at the tips (§4.2, Fig. 6, Table 1). **Shown**
8. The small differences from that reference are attributed to running implicit LES on a grid built with the explicit-LES criterion $\epsilon_{\mathrm G}/h=2.8$ (§4.2). **Stated**
9. Point-to-point messaging is "not feasible" for F-ALM because each point depends on the whole line and the owning rank changes with rotation; one communicator per blade (`MPI_COMM_SPLIT`) with `MPI_GATHER`, a computation on rank 0 and `MPI_BCAST` solves it, and the same approach applies to other non-local actuator lines (Jha & Schmitz 2018; Dağ & Sørensen 2020) (§4.3, Algorithm 3, Figs. 7–8). **Stated** (testing deferred to Stanly 2020)
10. NREL Phase VI: both models use $\epsilon_{\mathrm G}/c=0.5$ on the same "15-million-point" grid with average $\epsilon_{\mathrm G}/h=3.6$, on 729 CPUs (§5, §5.1, Table 3). **Shown** (set-up)
11. Grid study (Richardson extrapolation, ASME 2008) on 3,466,008, 6,993,756 and 13,002,444 points gives power 6.675, 6.557 and 6.778 kW and a GCI of 6% on the fine grid (Table 5). **Shown**; *(compiler check, not in the sources)* the fine-grid power, 6.778 kW, equals the ALM power of Table 6; the paper does not say which model the grid study used.
12. The coarse grid violates $\epsilon_{\mathrm G}/h>2$ ($\epsilon_{\mathrm G}/h=1.85$) but shows no spurious fluctuations and a smooth source term (§5.2). **Shown** (asserted from the run)
13. Fifty actuator points per line suffice; results did not change beyond that number (§5.2). **Stated**
14. The time step $0.001R_{\mathrm r}/U_{\mathrm{ref}}=1.32\times10^{-4}$ s is "about one order of magnitude smaller" than in typical wind-turbine simulations, as the compressible code requires; smaller steps changed no key parameter (§5.1, §5.2). **Stated**
15. Averaging over more than one flow-through time (after two of transient) did not change the averages, attributed to the non-turbulent inflow (§5.2). **Stated**
16. Instantaneous Q-criterion structures and instantaneous and mean wakes show "no noticeable difference" between ALM and F-ALM; the source-term change is confined to tip and root and is not "seen" in the flow unless the grid is fine enough (§5.3.1, Figs. 12–14). **Shown**
17. An actuator-line tower disturbs the tip vortices less than a no-slip tower because the stagnation pressure in front of it is lower (§2.3, §5.3.1, citing Churchfield et al. 2015). **Stated**
18. The wake $2R_{\mathrm r}$ downstream agrees in trend with Ravensbergen et al. (2020); deficit differences behind tower, nacelle and lower rotor and between mid-span and tip are attributed to the missing nacelle and the actuator-line tower (§5.3.1, Fig. 15). **Shown**
19. F-ALM predicts a stronger time-averaged downwash at the blade than ALM, most at tip and root (§5.3.2, Fig. 16). **Shown**
20. F-ALM lowers the tangential force that ALM overpredicts, most at root and tip; both overshoot near the root, attributed to three-dimensional rotational effects missing from two-dimensional airfoil tables (§5.3.2, Fig. 17). **Shown**
21. Power (Table 6): experiment 6.0 kW, ALM 6.778 kW (12.96% over), F-ALM 6.06 kW (1% over) (§5.3.2). **Shown**
22. Average time per step on 8 cores: 3.0098 s (ALM) and 3.039 s (F-ALM), about 1% extra (§5.3.3, Table 7). **Shown**
23. Because F-ALM allows coarser grids, it is judged "more suitable for LES simulations having explicit subgrid-scale models (Ciri et al., 2018), rather than the currently used implicit LES" (§6). **Stated**

# Printed slips

- **Table 3 (p. 8):** the value cells of "Total grid points $n_x\times n_y\times n_z$" and of the two "$dx\times dy\times dz$" rows are empty; the "$dx\times dy\times dz$" row is printed twice.
- **Grid size:** the text prints "15 million points" (§5, §5.1) and Table 5 prints 13,002,444 points for the fine grid used for the ALM and F-ALM runs. *(compiler check, not in the sources)* Table 3's $25\times25\times33$ points per CPU on 729 CPUs give 15,035,625.
- **Table 5 refinement ratios:** printed 1.26 and 1.44. *(compiler check, not in the sources)* The edge lengths give $0.0276/0.0219=1.26$ and $0.0219/0.0152=1.44$; the point counts give $(6{,}993{,}756/3{,}466{,}008)^{1/3}=1.26$ but $(13{,}002{,}444/6{,}993{,}756)^{1/3}=1.23$.
- **Table 5 $\epsilon/\Delta$:** printed 1.85, 2.33, 3.60. *(compiler check, not in the sources)* With the printed $\epsilon=0.5C_{mean}$, $C_{mean}=0.1095R$ and edge lengths 0.0276R, 0.0219R, 0.0152R the ratios are 1.98, 2.50, 3.60.
- **Tip-speed ratio (Table 2):** printed TSR 5.35 with $U_\infty=7$ m/s and $U_{ref}=37.86$ m/s. *(compiler check, not in the sources)* $37.86/7=5.41$; 71.9 RPM and $R=5.029$ m give $\Omega R=37.87$ m/s, consistent with $U_{ref}$.
- **Mean chord (Table 2):** printed "$C_{mean}=0.5475$ m $\equiv0.1095R$" with $R=5.029$ m. *(compiler check, not in the sources)* $0.5475/5.029=0.1089$.
- **Table 1:** the $C_L$ entry of the translating wing (NACA 64A17, $\alpha=6°$) reads "See Fig. 11 and Table 4", which are the NREL Phase VI S809 data.
- **Eq. (21) and Algorithm 2, step 6:** the left side is $u_y(z_i;\epsilon_k)$, the kernel in the integrand is $\epsilon_i^2$, and the Algorithm writes $u_y^{n*}(z_i;\epsilon_i)$.
- **Symbol $\gamma$:** the grid-stretching parameter in Eqs. (4)–(7) and the twist in Eq. (12), defined there as "Sum of the local twist angle and twist of the blade"; Table 2 lists "Blade pitch, in addition to the twist".
- **Algorithms 1 (step 7) and 2 (step 8):** labelled "Compute local angle of attack", they give the flow angle $\phi$ of Eq. (11).
- **Reference list:** Kleusberg et al. 2017a and 2017b are printed identically (authors, title, J. Phys. Conf. Ser. 854, 012025, DOI); "Ciri et al. 2020" (Energies) is printed with volume 10, issue 6 and DOI 10.3390/en10060821. Fig. 9 caption ends "..".

# Notation map

| Stanly et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\epsilon$, $\epsilon^{LES}$, $\epsilon^{opt}$ | $\epsilon_{\mathrm G}$, $\epsilon_{\mathrm G}^{\mathrm{LES}}$, $\epsilon_{\mathrm G}^{\mathrm{opt}}$ | Gaussian kernel (spreading) width (registry §11); **collision** with the dissipation rate $\varepsilon$ |
| $\Delta$, $dx$ | $h$ | grid spacing, not a filter width |
| $\eta_\epsilon(d)$ | $g_\epsilon(d)$ | page-local Gaussian regularization kernel; **collision** with the Kolmogorov length $\eta$ |
| $\mathbf f_\epsilon(\mathbf x)$, $N_{blades}$ | $\boldsymbol f_{\mathrm{ALM}}(\boldsymbol x)$, $N_{\mathrm b}$ | page-local regularized load per unit volume; number of blades |
| $\phi$, $\alpha$ (Eqs. 11–12) | $\phi_{\mathrm f}$, $\alpha_{\mathrm a}$ | page-local flow angle and angle of attack; **collision** with the registry $\alpha$ |
| $\gamma$ (Eq. 12) | $\gamma_{\mathrm t}$ | page-local twist plus pitch; **collision** with the ratio of specific heats |
| $\gamma$, $\chi$, $\psi$ (Eqs. 2–7) | (grid-stretching parameters) | page-local; **collision** with $\gamma$, the SA $\chi$ and the $k$-$\sqrt kL$ $\psi$ |
| $\Omega$ | $\Omega_{\mathrm{rot}}$ | rotor angular velocity |
| $R$ | $R_{\mathrm r}$ | rotor radius |
| $M_{Tip}$ | $M_{\mathrm{tip}}$ | tip Mach number |
| $C_L$, $C_D$ | $C_L$, $C_D$ | airfoil lift and drag coefficients, agree |
| $\tilde{\mathbf u}(\mathbf x_i)$ | (LES velocity sampled at actuator point $i$) | the tilde is **not** a Favre filter |
| $\hat{\mathbf u}(\mathbf x_i)$ | $\boldsymbol u_{\mathrm{corr}}(\boldsymbol x_i)$ | page-local F-ALM corrected velocity; the hat is **not** a test filter |
| $u_y$, $\Delta u_y$, $G(z_j)$ | $u_y$, $\Delta u_y$, $\Gamma_U(z_j)$ | page-local induced velocity, subfilter velocity correction, $\tfrac12cU_\infty^2c_L$ |
| $AD$ | (artificial-dissipation term) | the implicit-LES closure |
| $Q$ | (Q-criterion) | dimensional, 35 m²s⁻² |
| TSR, NTU | (tip-speed ratio, flow-through time) | page-local |

# Reference list

105 printed references, alphabetical author–year (Elsevier Harvard). The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Same-author same-year works take suffixes in printed
order; the two identically printed Kleusberg et al. (2017a, b) references are
recorded as printed (see Printed slips). Several items lack page or article
numbers (Jha et al. 2014; Shen et al. 2005; Zhong et al. 2019; Rullaud et al.
2018); all are parseable.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Actuator line and actuator disk models](/methods/actuator-line-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Variational multiscale method](/methods/variational-multiscale-method.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
