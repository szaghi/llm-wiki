---
type: Source
title: "Husson et al. (2024) — A comprehensive framework for robust hybrid RANS/LES simulations of wall-bounded flows in LBM"
description: "Transposes ZDES mode 2 (2020) on the Spalart–Allmaras model to a D3Q19 HRR lattice Boltzmann solver with a linearized-wall-law immersed boundary, and shows that its shielding keeps attached boundary layers in RANS on isotropic grids where DDES fails, on a flat plate, a backward-facing step and a three-element airfoil."
resource: "doi:10.1016/j.jcp.2024.112814"
source_kind: paper
authors: [Husson J., Terracol M., Deck S., Le Garrec T.]
year: 2024
venue: "J. Comput. Phys. 502:112814"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Computational_Physics_Husson_A_comprehensive_framework_for_robust_hybrid_RANSLES_simulati.pdf"
tags: [hybrid-rans-les, des, lattice-boltzmann, immersed-boundary, wall-model, spalart-allmaras]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Husson et al. (2024) combine a [lattice Boltzmann](/methods/lattice-boltzmann-method.md)
solver with zonal [detached-eddy simulation](/methods/detached-eddy-simulation.md)
(ZDES) mode 2 (2020) of Deck & Renard, built on the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md), and call the
result ZDES-LBM. Lattice Boltzmann methods need isotropic Cartesian grids,
which at high Reynolds number are very fine in the streamwise and spanwise
directions relative to the boundary-layer thickness ($\Delta\approx0.01\delta$).
On such grids the shielding of DES-type models fails: modelled-stress
depletion (MSD), wrong skin friction and grid-induced separation
([hybrid RANS/LES](/definitions/hybrid-rans-les.md)). ZDES mode 2 (2020) adds
a wake-layer shielding function and a detached-flow inhibition function to
the DDES function $f_d$, plus boolean switches that boost eddy-viscosity
destruction in grey areas. The question is whether these gradient sensors,
calibrated on finite-volume Navier–Stokes solvers, survive lattice Boltzmann
numerics.

The framework runs in a development branch of [ProLB](/software/prolb.md):
D3Q19 hybrid recursive regularized BGK collision; the SA equation solved by
finite differences and fed into the relaxation time; a sharp-interface
direct-forcing [immersed boundary](/methods/immersed-boundary-method.md) with
fluid-side forcing nodes; and the analytical SA
[wall law](/definitions/law-of-the-wall.md) of Allmaras & Johnson,
linearized below the interpolation distance $2.5h$ as a
[RANS wall function](/methods/rans-wall-function.md), an analytical
[equilibrium](/methods/equilibrium-wall-model.md) law. The authors place it
beside [wall-modelled LES](/methods/wall-modelled-les.md) in lattice
Boltzmann, which needs [inflow turbulence](/methods/inflow-turbulence-generation.md),
and state, citing earlier work, that lattice Boltzmann LES mostly uses
[Smagorinsky](/methods/smagorinsky-model.md)-type models or the collision
operator as an [implicit](/definitions/implicit-les.md) model; the PowerFLOW
hybrid rests on an RNG [k-ε model](/methods/k-epsilon-model.md).

On the zero-pressure-gradient flat plate
([turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md),
$Re_L=5\times10^6$) ZDES-LBM reproduces RANS-LBM exactly, also with
$C_{\mathrm{DES}}=0$ and on an inclined plate, while DDES in lattice Boltzmann
suffers severe MSD. On the [backward-facing step](/benchmarks/backward-facing-step.md)
($Re_h=40\,000$) ZDES-LBM matches the wall-resolved ZDES-NS of Deck & Renard
in shielding, eddy-viscosity destruction, vorticity thickness and profiles.
On the LEISA2 three-element airfoil ($Re_c\approx1.23\times10^6$, 77 million
nodes) attached layers stay RANS and $C_p$ agrees with the experiment; a
slight delay of the slat shear-layer instability is attributed to grid and
wall model, not to the hybrid model.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 502 (2024) 112814;
received 21 April 2023, accepted 26 January 2024), 23 pages, all read;
pp. 4–9 checked visually for the equations. Page 1 matches Crossref (title,
four authors, venue, DOI).

# Key claims

Notation: $f_q$, $\boldsymbol c_q$, $w_q$, $\tau_{\mathrm{LB}}$ lattice
distributions, velocities, weights and relaxation time; $l_{\mathrm{hyb}}$
hybrid length; $f_P$, $f_{P2}$, $f_R$ ZDES shielding, second shielding and
inhibition functions; $c_0$ physical sound speed (page-local; Notation map).

1. On the isotropic grids of high-Reynolds-number lattice Boltzmann runs, DES-type methods almost systematically trigger MSD and delay the formation of instabilities, which makes them prohibitive for attached boundary layers (§1, citing [29]). **Stated**
2. ZDES mode 2 (2020) is "the only fully-detailed «automatic» formulation in the open literature providing an appropriate solution to the RANS shielding of the whole attached turbulent boundary layer thickness"; the SBES/SDES shielding and the PowerFLOW VLES switching ($k$-$\varepsilon$ RNG based) are undisclosed (§1). **Stated**
3. The D3Q19 HRR-BGK scheme recovers the weakly compressible Navier–Stokes equations to second order with $\rho=p/c_0^2$ and $\tau_{\mathrm{LB}}=(\nu+\nu_t)/c_0^2+\Delta t/2$: the eddy viscosity enters only through the relaxation time (§2.1, Eq. 15). **Stated**
4. The HRR blending constant is 0.98, as in [95] (§2.1). **Stated**
5. The hybrid length is $l_{\mathrm{hyb}}=d-f_P\max(0,d-C_{\mathrm{DES}}\Delta)$ with $C_{\mathrm{DES}}=0.65$; the choice of cell-size estimate is "not significant" on isotropic grids (§2.2, Eq. 24). **Stated**
6. DDES shielding alone ($f_P=f_d$) protects only the layer below the log region; it is insufficient on fine meshes or under adverse pressure gradient and triggers MSD (§2.2, citing [53,83]). **Stated**
7. ZDES mode 2 (2020) uses $f_P=f_d\big(1-(1-f_{P2})f_R\big)$ (Eq. 25), with $f_{P2}=\frac{f_d(2.5r_d)}{f_d(r_d)}f_d(\mathcal G_{\tilde\nu})$, $\mathcal G_{\tilde\nu}=\frac{25}{\sqrt{\partial_ju_i\partial_ju_i}\,\kappa d}\max\big(0,-\nu\,\partial\chi/\partial n\big)$ (Eq. 27), and $f_R$ ramping from 1 to 0 as the detached-flow sensor $\mathcal G_\Omega$ goes from 0.03 to 0.04 (Eq. 28); $f_R=1$ where $\lvert\boldsymbol\omega\rvert<0.8\sqrt{\partial_ju_i\partial_ju_i}$ (§2.2). **Stated**
8. In LES zones $f_{v1}=1$, $f_{v2}=0$, $f_w=1$; boolean switches with thresholds 0.8 and 0.2 on $f_d$ and $1-(1-f_{P2})f_R$ blend the RANS and LES damping functions, and a factor 100 on $f_w$ boosts eddy-viscosity destruction in grey areas (§2.2, Eqs. 29–35). **Stated**
9. "A priori no evidence" says the shielding keeps its efficiency in lattice Boltzmann, because $\nu_t$ recalibrates the relaxation time, slower destruction could delay instabilities, and factor-2 grid transitions can spuriously activate $f_{P2}$ or $f_R$ (§2.2). **Stated**
10. Typical DES-type methods give insufficient protection when $\Delta x\le0.3\delta$; $\Delta x\approx0.01\delta$ is also Menter's estimated threshold of the SDES shielding [74] (§4.1.2). **Stated**
11. Flat plate: ZDES-LBM and RANS-LBM give "identical" $C_f$ and superimposed velocity and $\nu_t/\nu$ profiles at $x/L=1$, with $\Delta x\approx0.01\delta$ at mid-plate (§4.1.2, Fig. 4). **Shown**
12. Flat plate with $C_{\mathrm{DES}}=0$ gives "exactly the same result" (§4.1.2). **Shown** (stated, no separate figure)
13. DDES (2006) on the same plate suffers severe MSD: the layer tends to laminar while the wall law still imposes a turbulent profile, and $C_f$ oscillates ("unexploitable") (§4.1.2, Fig. 5). **Shown**
14. On the inclined plate the staircased forcing nodes and non-aligned wall normal make the wall-normal sensors harder to evaluate, yet ZDES still shields the layer like RANS (§4.1.2, Fig. 5). **Shown**
15. Backward-facing step: the a priori shielding field built from RANS-LBM is very consistent with that of ZDES-NS despite different numerics and grids (§4.2.2, Fig. 7). **Shown**
16. Backward-facing step: early 2D Kelvin–Helmholtz instabilities are stronger in ZDES-NS; vorticity-thickness growth agrees; eddy viscosity is destroyed quickly in both, and "no further delay in the formation of instabilities is introduced with ZDES-LBM than the ZDES-NS" (§4.2.2, Figs. 8–10). **Shown**
17. Backward-facing step: mean velocity profiles at four stations agree very well with ZDES-NS; streamwise RMS shows a "fair common tendency"; near-wall differences at station 1 are attributed to the wall model imposing a zero-pressure-gradient profile in the recirculation (§4.2.2, Fig. 11). **Shown**
18. Isotropy makes the lattice grid locally much finer than the Navier–Stokes grid: $\Delta z_{\mathrm{NS}}\approx10\Delta z_{\mathrm{LBM}}$ for $0\le x/h\le1$; 61 000 against 5000 points in the plane $x=0$; 44.7 million against 3.9 million nodes in total (§4.2, Table 1). **Shown**
19. Three-element airfoil: slat and flap boundary layers stay RANS and the eddy viscosity is destroyed quickly near trailing edges; the flap separation is not grid-induced (§4.3.2, Fig. 13). **Shown**
20. Three-element airfoil: mean $C_p$ of ZDES-LBM and RANS-LBM agrees very well with the experiment (§4.3.2, Fig. 14). **Shown**
21. The flap suction-side topology differs (mild separation in ZDES-LBM, thin in the wall-resolved LES, massive in PIV) and the pressure taps do not match the PIV, which the authors take as a sign that several topologies occurred in the experiment, consistent with Arnott et al. on another airfoil, as they cite (§4.3.2, Figs. 14–15). **Stated**
22. The slat shear layer shows a small delay of instability ($k_{2D}$ overpredicted in the mixing layer, underpredicted near the cusp), attributed not to the model since "the exact same phenomenon" occurs in wall-modelled lattice Boltzmann LES without RANS eddy viscosity [95] (§4.3.2, Figs. 17–18). **Shown** (attribution **Stated**)
23. Slat spectra agree with the wall-resolved LES below about 10 kHz ($St\approx10$); the drop above at points $S_4$, $S_5$ is due to local grid resolution (§4.3.2, Fig. 19). **Shown**
24. ZDES mode 2 (2020) with a linearized-wall-law immersed boundary in lattice Boltzmann handles flows with attached and separated regions and is a "fair alternative" to Navier–Stokes methods and to wall-modelled LES in lattice Boltzmann, especially for aeroacoustics (§5). **Stated**
25. The SA analytical wall law and its linearization rest on the equilibrium hypothesis, so discrepancies are expected near separation and in recirculation (§3). **Stated**

# Printed slips

- **Eq. 10** sums $\sum_{i=1}^{19}$, while the D3Q19 index runs $0\le i\le18$ (Eqs. 2–3).
- **Eq. 13** prints the first-order term as $\frac1{c_s^2}\xi_{i,\alpha}\rho u_{i,\alpha}$, with the lattice index on the velocity.
- **Eq. 43:** the analytical wall-normal gradient is the fraction $\frac{c_{v1}^3+(\kappa y^+_{IP})^3}{c_{v1}^3+(\kappa y^+_{IP})^3(1+\kappa y^+_{IP})}$ times $u_{\tau,F}$, which has the units of a velocity, not of a velocity gradient; with $\chi=\kappa y^+$ (Eq. 42) and $f_{v1}=\chi^3/(\chi^3+c_{v1}^3)$ (Eq. 19), $\nu_t=\nu\chi f_{v1}$ (Eq. 18), the fraction is $1/(1+\chi f_{v1})$, the $du^+/dy^+$ of a layer of constant total stress $(\nu+\nu_t)\,\partial u_t/\partial n=u_\tau^2$, and the dimensional gradient then carries $u_\tau^2/\nu$ *(compiler check, not in the sources)*.
- **Eq. 17** adds $\nu_t(\cdot)$, without density, to $-\frac23\rho k\delta_{ij}$ *(compiler check, not in the sources)*.
- **Eq. 41:** the $y$ in $u_{t,IP}y/\nu$ is not defined.
- **p. 12:** "the LBM grid resolution is finer than the LBM one" (one should read NS).
- **WRLES size:** "$2.6\cdot10^9$ nodes" (p. 15) and "$2700\cdot10^6$ nodes" (p. 18).
- "modeled-stressed depletion" (abstract); "ZDES mode (2020)" (conclusion).
- **Fig. 19:** the Strouhal number uses $u_0$, the step's velocity symbol, for the airfoil.
- **SA constants:** $c_{w2}$ and $c_{w3}$ are not printed (Eq. 23).
- **Reference list:** ref. [83] prints "R. Radespiel" twice; ref. [9] (first author "B.M. Duda") sits between Bhatnagar and Bouchard in the alphabetical list.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f_i$, $\boldsymbol\xi_i$, $\omega_i$ | $f_q$, $\boldsymbol c_q$, $w_q$ | $\omega_i$ **collides** with the vorticity |
| $\tau$ (relaxation time) | $\tau_{\mathrm{LB}}$ | **collision** with the SGS stress |
| $\Omega(f)$, $\Omega_i$ | page-local (collision operator) | **collision** with the rotation-rate tensor |
| $c_s=1/\sqrt3$, $c_0$ | page-local | lattice and physical sound speeds |
| $\mathcal H^{(n)}$, $a^{(0)}_n$, $a^{(1)}_n$ | page-local | Hermite polynomials and coefficients |
| $\sigma$ (HRR) | $\sigma_{\mathrm{HRR}}$ (page-local) | 0.98; **collision** with the SA diffusion constant $\sigma=2/3$ |
| $\sigma^\nu_{ij}$ | $\sigma_{ij}/\rho$ | kinematic viscous stress (deviatoric factor printed $\tfrac13$) |
| $\sigma^R_{ij}$ | $-R_{ij}$ (modelled) | **sign:** a Boussinesq stress $\nu_t(\cdot)-\tfrac23\rho k\delta_{ij}$ |
| $\chi$ | $\chi=\tilde\nu/\nu$ | transported directly |
| $S$, $\tilde S$ | $\lvert\Omega\rvert$ (vorticity magnitude), $\tilde S$ (SA modified vorticity) | $S$ **collides** with the strain rate |
| $\boldsymbol\Omega$, $\lVert\boldsymbol\Omega\rVert$ | $\boldsymbol\omega$, $\lvert\boldsymbol\omega\rvert$ | vorticity vector |
| $d_w$, $d$ | $d$ | wall distance |
| $\ell$ | $l_{\mathrm{hyb}}$ | hybrid length scale ($l_{\mathrm{RANS}}=d$) |
| $\Delta$ (Eq. 20) | $\nabla^2$ | Laplacian; elsewhere $\Delta$ is the cell-size estimate |
| $\Delta x$, $\Delta y$ | $h$ | lattice spacing, isotropic |
| $C_{DES}$, $f_d$, $r_d$ | $C_{\mathrm{DES}}$, $f_d$, $r_d$ | |
| $f_P$, $f_{P2}$, $f_R$, $\mathcal G_{\tilde\nu}$, $\mathcal G_\Omega$, test$_\Delta$, test$_w$ | $f_P$, $f_{P2}$, $f_R$, $\mathcal G_{\tilde\nu}$, $\mathcal G_\Omega$ (registry §11); test$_\Delta$, test$_w$ page-local | ZDES mode 2 (2020) functions, sensors and switches |
| $y_c$, $r_{lin}$, $d_{IP}$ | $y_c$, $r_{\mathrm{lin}}$ (page-local), $d_{\mathrm{IP}}$ (registry §11) | linearization distance, $y_c/d$, $2.5h$ |
| $B$, $a_k$, $b_k$, $c_k$ (Eq. 37) | page-local | SA wall-law constants; $B=5.0333908790505579$ **differs** from the registry's log-law intercept $B$ |
| $u_t$, $u_n$ | page-local | wall-tangential and normal velocity |
| $k_{2D}$, $\delta_\omega$, $Q^*$ | page-local | 2D resolved energy, vorticity thickness, normalized Q |
| $Re_L$, $Re_h$, $Re_c$; $Ma$ | $Re$ with subscripts; $M$ | |

# Reference list

121 printed references in numbered Elsevier style; merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [67]
(Maeyama et al. 2022, Comput. Fluids 233:105249, lattice Boltzmann wall
modelling) is a different work from the ingested
[Maeyama et al. (2022)](/sources/maeyama-2022.md) and is keyed `maeyama-2022-c`.
Ref. [49] is a bare URL of ProLB (keyed with a corporate author and the
citing year); ref. [76] prints a truncated title; ref. [22] prints the issue
"(2022)" before the year 2014; ref. [68] is an arXiv preprint
(arXiv:1505.06900); ref. [74] is a technical report. Same-author same-year
works take suffixes in printed order (Deck 2014, Degrigny 2021, Kang 2011).
No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [ProLB](/software/prolb.md)
