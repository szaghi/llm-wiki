---
type: Source
title: "Rismondo et al. (2025) — Wind turbine noise generation and propagation through large eddy simulation and acoustic analogy"
description: "Couples a wall-resolved WALE LES of a model three-blade wind turbine in OpenFOAM with the advective Ffowcs Williams–Hawkings equation, separating tonal and trailing-edge surface noise from low-frequency wake quadrupole noise, describing the wake in three regions and explaining near-field decay with a stochastic rotpole model."
resource: "doi:10.1017/jfm.2025.10709"
source_kind: paper
authors: [Rismondo G., Petris G., Cianferra M., Armenio V.]
year: 2025
venue: "J. Fluid Mech. 1024:A33"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Fluid_Mechanics_Rismondo_Wind_turbine_noise_generation_and_propagation_through_large.pdf"
tags: [les, aeroacoustics, eddy-viscosity, software, separated-flow]
timestamp: 2026-10-26T15:52:00Z
---

# Summary

Rismondo et al. (2025) characterize the aerodynamic noise of a model-scale,
three-blade horizontal-axis wind turbine ($D=0.18$ m, $Re_D=9.6\times10^4$, tip
speed ratio 4.7, tip Mach number about 0.11) by a hybrid approach. A
geometry-resolved, wall-resolved incompressible [LES](/definitions/large-eddy-simulation.md)
in [OpenFOAM](/software/openfoam.md) (PISO, multiple reference frame, about 144
million cells, first cell below $y^+=1$) closed with the [WALE model](/methods/wale-model.md)
supplies the flow. The advective form of the [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
then gives the acoustic pressure at virtual microphones, split into linear
(thickness and loading, surface integrals over the turbine) and nonlinear
(quadrupole, volume integrals over a cylinder containing the wake to $x/D=7$)
parts. The paper's fit to the bundle is peripheral (aeroacoustics and wind
energy); it applies LES with an existing closure and proposes none, and no grid-convergence
study is reported.

The thrust and power coefficients are within 11.25% and 8.5% of the experiment.
The wake has a near region to about $1D$, an intermediate region to about $7D$,
where tip-vortex instabilities lead to leap-frogging and grouping, and a far
region of homogenized turbulence; unlike a marine propeller, no significant hub
vortex forms. Surface pressure fluctuations produce tonal noise at the blade
passing frequency and high-frequency broadband trailing-edge noise. The wake
produces low-frequency broadband noise, significant only below four times the
rotation frequency, which dominates the near field; the linear part dominates
the far field. In the rotor plane the near-field linear term decays as $r^{-4}$,
the $r^{-(n+1)}$ law of Ianniello's rotpole model for $n=3$ rotating sources. A
stochastic extension of that model shows that random pressure fluctuations
shorten the steep near-field decay. Other rotor-wake LES cited in the paper use
[immersed boundaries](/methods/immersed-boundary-method.md), and full-turbine
acoustics have been computed with delayed [detached-eddy simulation](/methods/detached-eddy-simulation.md).

# Version read

Version of record (J. Fluid Mech., Cambridge University Press, open access CC
BY 4.0; received 24 April 2025, revised 29 July 2025, accepted 1 September
2025), 43 pages (A33-1 to A33-43), all read; Eqs. (2.2)–(2.7) checked visually.
Page 1 matches Crossref; no identity problem. Locators are the journal's
sections, equations, figures and tables.

# Key claims

Page-local symbols: $f_T$ rotation frequency (blade passing frequency $3f_T$);
$c_0$ speed of sound; $M_0=U_\infty/c_0$; $p'$ acoustic pressure; $C_T$,
$C_P$ thrust and power coefficients; $K_\lambda$ observer distance over the
blade-passing wavelength; $\mathcal S=\partial_i\partial_j(u_iu_j)$ the
kinematic Lighthill source.

1. The flow is solved as filtered incompressible Navier–Stokes in a multiple reference frame with Coriolis and centrifugal terms, closed with WALE (Ducros, Nicoud & Poinsot 1998), in OpenFOAM with PISO, second-order backward time stepping and second-order central (linear Gauss) space discretization (§2.1, Eqs. 2.1–2.2). **Stated**
2. The time step $1.0\times10^{-6}$ s gives a maximum Courant number about 10 in a few cells near the blade tips and an average of order 0.017 (§2.1). **Stated**
3. Initialization by a potential solver, then RANS, then LES; statistics over 10 revolutions, collected after 31 revolutions (§2.1). **Stated**
4. Mesh: about 144 million hexa-dominant cells, about $5\times10^5$ surface elements, 28 prism-like layers with first-cell height $y/D\approx4.4\times10^{-5}$, $y^+<1$ except $O(1)$ at the trailing edge of the outer radii, chordwise and spanwise spacings below 15 wall units and about 5 at the tip and trailing edge (§2.3, Figs. 3–5). **Stated**
5. Validation: $C_T=0.71$ (LES) against 0.80 (experiment), $C_P=0.183$ against 0.20; errors 11.25% and 8.5%, attributed to the absent mast, the wind-tunnel blockage (4.7%) and the floor boundary layer of the experiment (§3, Table 2). **Shown**
6. Resolved load fluctuations are broadband up to $100f_T$ (§3, Fig. 7). **Shown**
7. The SGS eddy-viscosity ratio $\nu_t/\nu$ lies mostly in 0–10, peaking in the tip-vortex core and thin wake vortices, which the authors take as indicating high resolution (§3, Fig. 8c). **Shown**
8. The wake has a near region to about $1.0D$ (synchronized tip and root vortices, trailing-edge vortex sheet), an intermediate region to about $7D$ (loss of coherence, kinetic-energy increase at outer radii) and a far region with homogenized kinetic energy over the disk (§3.1, Figs. 9–10). **Shown**
9. Tip-vortex destabilization proceeds by short-wave then long-wave instability, then mutual inductance, leap-frogging and vortex grouping, consistent with Posa et al. (2021), Lignarolo et al. (2015) and Felli et al. (2011) (§3.1.2, Figs. 12–14). **Shown**
10. Unlike an isolated marine propeller, the wind-turbine hub vortex is insignificant and no hub–tip vortex interaction occurs; the near wake is dominated by the tip-vortex system (§3.1.1). **Shown**
11. Blade pressure fluctuations are larger on the downwind than the upwind side, largest at the trailing edge towards the tip and weaker at the tip itself (§4.1, Fig. 16). **Shown**
12. Large r.m.s. of $\mathcal S$ occurs in coherent regions (tip and root vortices, trailing-edge sheet) and, unlike marine propellers, persists at outer rather than inner radii (§4.1, Fig. 17). **Shown**
13. Neglecting retarded-time delays is valid below $30f_T$ for the linear terms and $3.85f_T$ for the nonlinear terms at the nearest microphone, from the maximum-frequency-parameter criterion of Cianferra et al. (2019a) with delays computed by bisection of the retarded-time equation (§4.2, Eqs. 4.3–4.5, Tables 3–4). **Derived**
14. Retarded times are not computed, justified by the nonlinear terms being significant only below $4f_T$ (§4.2). **Stated**
15. The linear part dominates for $f\ge3f_T$; the lowest frequencies are dominated by the nonlinear terms at the near-field microphones ($r/D=1$) (§4.2, Fig. 18). **Shown**
16. The linear spectrum peaks at $f=3f_T$ plus a high-frequency broadband part; the nonlinear spectrum shows blade-passing peaks near the rotor that are smoothed into low-frequency broadband noise downstream, tied to vortex instability and loss of synchronization (§4.2, Fig. 18). **Shown**
17. An increased nonlinear level at $f>20f_T$ at $x/D=1$ and 2, in a range where time delays may matter, is likened to the Kelvin–Helmholtz quadrupole noise of Wolf et al. (2012) and Turner & Kim (2022) (§4.2). **Shown** (with the caveat stated)
18. Among the three volume terms, the $1/R^{*3}$ term (seventh term of Eq. 2.3) dominates at the near microphones (§4.2, Fig. 19f). **Shown**
19. The linear noise comes mainly from the middle blade region ($0.2<r/D<0.45$); trailing-edge pressure fluctuations are the main surface source (§4.2, Fig. 20). **Shown**
20. The nonlinear noise comes from the outer volume ($0.45<r/D<0.9$, tip vortex); the inner volume (root vortices) is negligible everywhere (§4.2, Fig. 21). **Shown**
21. For nonlinear noise at a near-field microphone the dominant contribution comes from the wake region directly beneath it, so the whole wake must be included (§4.2, Fig. 22). **Shown**
22. Directivity: the linear part is a dipole with lobes along the flow, the nonlinear part an asymmetric quadrupole (downstream lobe dominant) in the near field that becomes symmetric with distance; the total at $2D$ ($K_\lambda\approx0.22$) is a non-symmetric dipole, at $100D$ a nearly symmetric dipole (§4.3, Fig. 24). **Shown**
23. In the rotor plane both terms decay as $r^{-1}$ in the far field, the linear dominant; in the near field both decay roughly as $r^{-4}$; the transition is around $4D$ (§4.3, Fig. 25a). **Shown**
24. The near-field $r^{-4}$ linear decay agrees with the $r^{-(n+1)}$ law of the rotpole model (Ianniello 2016) for $n=3$ rotating sources, i.e. destructive kinematic auto-interaction (§4.3; abstract). **Shown** (consistency with theory)
25. Along a line at $r/D=1$ parallel to the axis, out of the wake, the linear term decays as $r^{-1}$; the nonlinear term dominates up to $9D$, peaks at $4.5D$ and then decays as $r^{-1}$; beyond $10D$ the total follows $r^{-1}$ (§4.3, Fig. 25b). **Shown**
26. Stochastic tri-rotpole (contribution): with pressure fluctuation levels of 0.01 and 0.1 of the mean source pressure, the transition from the steep near-field decay ($r^{-4}$ radial, $r^{-7}$ streamwise for the deterministic model) to the asymptotic decay occurs earlier; pressure fluctuations reduce or remove the destructive kinematic auto-interaction (§4.3, Eq. 4.6, Figs. 26–27). **Shown**
27. By Mach similarity the results represent a medium-size turbine of about 100 m diameter rotating with a period of about 8 s (§2.3, §5). **Stated**
28. Volume (quadrupole) terms may matter near the source ($K_\lambda<1$) at this rotational Mach number (§5). **Shown**

The FWH Lighthill tensor is approximated as $T^{\mathrm L}_{ij}=\rho u_iu_j$ (low
Mach number, negligible viscous effects); the integration surface is the
impermeable turbine surface and the volume a cylinder of radius $0.9D$ from
$x/D=-0.5$ to 7 (results stated to be independent of radii 0.7–0.9, not shown).

# Printed slips

- **Eq. (2.2):** the centrifugal term is printed $\epsilon_{ijk}\omega_j(\epsilon_{ijk}\omega_ir_j)$, repeating each index more than twice.
- **Eq. (3.6) text:** "S and W are the symmetric and deviatoric parts of the velocity gradient tensor"; the rotation part $W$ is the antisymmetric part.
- **§3:** "the blockage coefficient of our simulation ($A_d/C=0.005$ %)"; with a domain of radius $7D$ the ratio is $1/196\approx0.0051$, i.e. 0.51% *(compiler check, not in the sources)*.
- **Fig. 15:** the caption gives $x/D=7.0$, 7.5; the text (§3.1.3) says 7.0, 8.0.
- **§3.1.1** discusses the state "at $x=0.6D$" with reference to Fig. 11, whose planes are at $x/D=0.05$, 0.2, 0.4, 0.8.
- **§4.1** says Eq. (2.3) "contains seven terms"; the Fig. 19 caption speaks of "the six terms composing the FWH equation".
- **§4.2:** "significant in the lower frequency range only ($f<4.0f/f_T$)"; §5 prints $f<4f_T$.
- **Eq. (4.3)** defines "$MFP=1/(\Delta_{del}f_{max})=1$", then uses the "criterion MFP > 1".
- **Tip Mach number:** $\sim0.11$ in §2.3, $\sim0.10$ in the abstract and §5; $K_\lambda$ at $2D$ is 0.22 in §4.3 and 0.21 on Fig. 24(c).
- **§5** names the experiment "Gambuzza & Ganapathisubramani (2021)", while §2.3 and §3 use Gambuzza et al. (2023) for the same turbine and data.
- **§4.3:** $M_{rl}=\boldsymbol v_l\cdot\boldsymbol r_l/c_0$ with the unnormalized $\boldsymbol r_l$; "rotopole" for rotpole.
- **§2.2:** the loading tensor is printed $L_{ij}=(p-p_0)\delta_{ij}+\sigma_{ij}$ and the Lighthill tensor $T_{ij}=\dots-\sigma_{ij}$, opposite signs on the same viscous stress; both derive from the momentum flux, so both signs cannot hold, and the $T_{ij}$ sign is the one that matches the momentum equation *(compiler check, not in the sources)*.
- **Reference list:** Gaurier et al. (2015) author list garbled ("DI FELICE, E., F, COSTANZO, M."); Debruijn et al. (1984) page field garbled; Posa, Broglia & Felli (2022a) title begins "A acoustic signature".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline u_i$, $\overline p$ | $\bar u_i$, $\bar p$ | filtered inertial-frame velocity and kinematic pressure; no filter definition printed |
| $\tau_{ij}$, entering as $+\partial_j\tau_{ij}$ | $-\tau_{ij}$ | **sign:** the source adds $+\partial_j\tau_{ij}$ to the momentum equation, so for Eq. (2.2) to hold its $\tau_{ij}$ is the negative of the registry's; the definition is not printed |
| $\nu_T$ | $\nu_t$ | WALE eddy viscosity; constant and filter width not printed |
| $\omega_j$ (frame), $\Omega$ (turbine) | $\Omega_{\mathrm{rot}}$ | $417.17$ rad/s; **collision** with the vorticity $\omega_i$ and the specific dissipation rate |
| $S$, $W$ (Eq. 3.6) | $S_{ij}$, $\Omega_{ij}$ | Q criterion |
| $S=\partial^2u_iu_j/\partial x_i\partial x_j$ | $\mathcal S$ | page-local; **collision** with the strain rate and the Lundquist number $S_L$ |
| $S$, $V$ (Eq. 2.3) | page-local | FWH integration surface and volume |
| $T_{ij}$ | $T^{\mathrm L}_{ij}$ | Lighthill tensor; **collision** with the integrity basis $T^{(n)}$ and temperature |
| $L_{ij}=(p-p_0)\delta_{ij}+\sigma_{ij}$ | $\ell_{ij}$ (page-local, as on the [FW-H page](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)) | loading tensor; **collision** with the Leonard stress $L_{ij}$ |
| $Q_i=\rho v_i$ | page-local | thickness source ($v_i$ surface velocity); $Q$ is also the torque and the Q criterion |
| $\hat p$ | $p'$ | acoustic pressure; **collision** with the test-filter hat (the hat also marks phase averages) |
| $\beta=\sqrt{1-M_0^2}$; $\beta$ (Table 1) | $\beta_M$ (page-local); blade twist page-local | Prandtl–Glauert factor; **collision** with the field-inversion $\beta$ |
| $R^*$, $\tilde R_i$, $\tilde R^*_i$, $\hat R_{ij}$ | $R^*$, $r_i$, $r^*_i$, $\Lambda_{ij}$ (page-local) | advective radiation distance and vectors, Eqs. (2.4)–(2.7); tildes are not Favre filters |
| $y$, $[\cdot]_\tau$, $U_\infty$ (Eq. 2.3) | $\boldsymbol s$, $[\cdot]_{t_e}$, $U_0$ (page-local) | source point, evaluation at emission time, uniform stream |
| $c_0$, $M_0$, $M_{tip}$ | page-local | $c_0=330$ m/s, $M_0\approx0.02$ |
| $C_T$, $C_P$, $C_p$ | page-local, $C_p$ | **collision:** the power coefficient $C_P$ differs from the pressure coefficient $C_p$ only by case |
| $\lambda=c_0/3f_T$, $K_\lambda$ | page-local | blade-passing wavelength; **collision** with the Taylor microscale |
| $x_b,y_b,z_b$, $y_b^+$ | $y^+$ | blade-local coordinates; $u_\tau$ estimated from a flat-plate $C_f$ correlation |
| $n$, $N$ | $n$ (page-local) | number of blades / rotating sources; the source's $N$ **collides** with the polynomial degree |

# Reference list

77 printed references in JFM author–year style, no DOIs printed; merged complete
into the [bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works keyed in printed order: Cianferra et al. (2019a/b), Posa
(2022) and Posa et al. (2022a/b), whose text labels do not coincide with the key
suffixes, and Sherry et al. (2013a/b). Partially garbled entries recorded as
printed: Gaurier et al. (2015) author list and Debruijn et al. (1984) page
field. Items without venue: van der Borg & Vink (1994), Mikkelsen (2004),
Wagner, Bareiss & Guidati (1996, book without publisher), Farassat (2007,
"Tech. Rep.").

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [WALE model](/methods/wale-model.md)
- [OpenFOAM](/software/openfoam.md)
