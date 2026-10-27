---
type: Source
title: "Yang & Ma (2022) — Hybrid RANS/LES study of tip leakage vortex instability and turbulence characteristics of a transonic turbine cascade"
description: "SST-based DES of a transonic high-pressure turbine cascade with tip clearance in ANSYS CFX: tip-leakage-vortex wandering and a spiral-type breakdown, vorticity budgets, POD of the wandering velocity, Reynolds stresses and anisotropy maps along the vortex, with URANS for comparison."
resource: "doi:10.1016/j.ast.2022.107758"
source_kind: paper
authors: [Yang Y., Ma H.]
year: 2022
venue: "Aerosp. Sci. Technol. 128:107758"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Aerospace_Science_and_Technology_Yang_Hybrid_RANSLES_study_of_tip_leakage_vortex_instability_and_t.pdf"
tags: [des, k-omega, turbomachinery, tip-leakage-vortex, anisotropy]
timestamp: 2026-10-26T16:21:00Z
---

# Summary

Yang & Ma (2022) apply an off-the-shelf
[detached-eddy simulation](/methods/detached-eddy-simulation.md) to one
passage of a transonic high-pressure turbine rotor cascade. The case is a
SNECMA profile tested by Arts et al., with a flat-tip clearance of $0.07c$
and an exit isentropic Mach number of 0.95
([turbine cascades](/benchmarks/turbine-cascade.md)). The model is the
[SST](/methods/k-omega-sst-model.md)-based DES of ANSYS CFX, with the $F_2$
shielding of the destruction term, $C_{DES}=0.61$ and $\Delta=\max_i\Delta_i$.
The paper calls it DES, DES-type, hybrid DES and DDES. Convection uses a
blend of central and second-order upwind fluxes whose local blending factor
$\sigma_b$ is near zero in LES regions
([numerical dissipation](/properties/numerical-dissipation.md)). The
authors judge mesh adequacy from this factor and from $-5/3$ spectra on a
single grid, arguing that comparing grids "cannot" do it for a DES-type
method ([hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

DES and URANS both match the measured mid-span isentropic Mach number
except near the suction-side shock. DES resolves more small-scale
structure and sharper shocks. URANS, with a
[Boussinesq](/definitions/boussinesq-hypothesis.md) Reynolds stress,
over-predicts the pitchwise–streamwise shear stress along the tip-leakage
vortex (TLV) and dissipates the wake early. The TLV wanders inside the
passage at a single frequency of about 2200 Hz. Near the trailing edge it
breaks down, a breakdown the authors attribute to the adverse pressure
gradient raised by the shocks. They call it a "spiral-type" breakdown seen
for the first time in a transonic turbine. A vorticity budget, a triple
decomposition with snapshot POD of the wandering velocity, Reynolds
stresses along the trajectory and Lumley anisotropy maps complete the
study. The maps go from one-component near the core upstream, toward
two-component downstream, to near-isotropic behind the trailing edge. All
results come from one simulation; no LES or DNS reference is used.

# Version read

Version of record (Elsevier, received 19 April 2022, online 19 July 2022);
13 pages, all read, with the equation pages checked visually. Page 1
matches Crossref.

# Key claims

1. The SST-DES switches from RANS to LES where $L_t=\sqrt k/(\beta^*\omega)$ exceeds $C_{DES}\Delta$, by replacing the destruction term of the $k$ equation; $C_{DES}=0.61$, $\Delta=\max_i\Delta_i$ (§2.1, Eqs. 2–4). **Stated** (after Strelets)
2. ANSYS CFX replaces $F_{DES}$ by $F_{DES\text{-}CFX}=\max\big(\frac{L_t}{C_{DES}\Delta}(1-F_2),1\big)$ to prevent grid-induced separation and modelled-stress depletion (§2.1, Eq. 5). **Stated**
3. Grid: structured O4H mesh $169\times155\times404$, "about 13 million" hexahedral cells, first cell $10^{-6}$ m ($y^+\approx1$), expansion ratio 1.05, 69 spanwise layers in the tip gap (§2.3). **Stated**
4. Time step $10^{-6}$ s, about 450 steps per wake-shedding period and 2100 per flow-through; dual time stepping with 10 pseudo-steps, three-level multigrid, residuals below $10^{-6}$ (§2.3, §3.1). **Stated**
5. Statistics: 0.004 s of settling, then 0.002 s sampled as 2000 snapshots (§3.1). **Stated**
6. Mesh adequacy for a DES-type method "cannot be conducted by just comparing flow parameters among different mesh amounts"; instead $\sigma_b$ is near zero in the TLV and wake at 90% span (LES mode) and near one near walls and in irrotational regions (§3.1, Fig. 4). **Shown** (single grid)
7. Velocity spectra at three monitor points show an inertial range with a $-5/3$ slope, a peak at 2200 Hz and harmonics tied to TLV instability (§3.1, Fig. 5). **Shown**
8. DES and URANS ($k$-$\omega$ and SST) both agree with the measured mid-span isentropic Mach number, except on the rear suction side, attributed to under-predicted shocks (§3.1, Fig. 6). **Shown**
9. DES resolves more small-scale vortical structure near the tip, and the wake-shedding layer persists longer, owing to lower numerical dissipation (§3.2, Fig. 7). **Shown** (qualitative)
10. URANS over-predicts the Reynolds shear stress in the pitchwise–streamwise plane along the TLV and misses the trailing-edge mixing; the DES stress is large mainly near the trailing edge (§3.2, Fig. 8). **Shown** (resolved DES stress against Boussinesq URANS stress)
11. DES captures the shocks more sharply, including pressure waves on both sides of the trailing edge; the URANS wake dissipates early "due to a higher eddy viscosity" (§3.2, Fig. 9). **Shown** (qualitative)
12. The TLV starts at about $0.2c$, strengthens downstream, keeps a supersonic core and stays continuous beyond the trailing edge (§4.1, Fig. 10). **Shown**
13. A "spiral-type" breakdown appears downstream of the shock near the trailing edge, "which cannot be found in the previous RANS literature", "distinguished firstly in a transonic turbine environment" (Abstract, §4.1, Fig. 10, §5). **Shown** (iso-surface visualization)
14. The breakdown is attributed to the adverse pressure gradient from passage expansion and vortex rotation, raised by the shocks; with a 5% span gap the TLV is strong and its breakdown "relatively weak" (§4.1). **Stated**
15. Upstream of the breakdown the spectra show one characteristic frequency, about 2200 Hz, attributed to wandering; downstream four frequencies, 730, 1460, 2200 and 4400 Hz, "almost harmonic" to it (§4.1, Fig. 11). **Shown**
16. Vorticity budget on the 0.95-span plane: the stretching–tilting term $(\boldsymbol\omega\cdot\nabla)\boldsymbol u$ (the source's "convection term") dominates the TLV transport; dilatation, baroclinic and viscous-diffusion terms are weaker (§4.2, Fig. 12). **Shown** (see Printed slips for the closing sentence of §4.2)
17. The TLV wanders spanwise and pitchwise, with patterns varying downstream and asymmetric about the mean core (20 slices from $0.4c$ to $1.2c$; Q criterion and vortex-ellipse fitting) (§4.3, Fig. 13). **Shown**
18. The TLV trajectory moves away from the suction surface and the endwall; radius and circulation grow downstream, dip at the throat and fall behind the trailing edge (§4.3, Fig. 14). **Shown**
19. The wandering amplitude grows monotonically up to the trailing edge, rises sharply near it and decreases downstream; the wandering frequencies become more complex downstream (§4.3, Figs. 15–16). **Shown**
20. The leading POD mode of the wandering velocity has non-zero transverse components at the core, which drive the wandering; its streamwise component is near zero at the core, so streamwise wandering is small; the perturbation grows downstream (§4.4, Fig. 17). **Shown**
21. The turbulent kinetic energy and all six Reynolds stresses are near zero along the TLV upstream of $z/c=0.8$ (source axial coordinate), rise downstream, dip near the throat and rise sharply at the trailing edge through the shocks (§4.5, Fig. 18). **Shown**
22. The shock-induced adverse pressure gradient sharply raises the normal Reynolds stresses near the core, which stretch the TLV and are "responsible for the vortex breakdown" (Abstract, §4.5, §5). **Stated** (interpretation of Fig. 18)
23. The streamwise normal stress is the smallest normal stress; the spanwise–pitchwise shear stress is much larger than the other shear stresses; the shear stresses follow the wandering amplitude (§4.5). **Shown**
24. Lumley maps of instantaneous TLV cores on four slices: one-component near the core upstream, toward two-component downstream, and gradually isotropic behind the trailing edge (§4.6, Fig. 19). **Shown**
25. RANS/URANS eddy-viscosity models erase small-scale unsteadiness through their large eddy viscosity and, being isotropic, ignore anisotropy (§1). **Stated**
26. The authors find only one earlier hybrid RANS/LES (DDES) study of turbine tip leakage (§1). **Stated**

The stresses compared (Eqs. 8–9), translated to the registry's kinematic
positive convention with $\langle\cdot\rangle$ the time average: DES uses
the resolved stress $R_{ij}=\langle u_i'u_j'\rangle$ only (modelled part not
added), URANS the Boussinesq form
$\rho R_{ij}=\tfrac23\rho k\delta_{ij}-2\mu_t\langle S_{ij}\rangle+\tfrac23\mu_t\partial_k\langle u_k\rangle\delta_{ij}$.
The anisotropy map uses $b_{ij}$ of the registry and the invariants
$\eta_b^2=b_{ij}b_{ji}/6$, $\xi_b^3=b_{ik}b_{kj}b_{ji}/6$ (Eqs. 13–15).

# Printed slips

- §4.2 states that the convection term plays "a dominant role" and the other three terms are "relatively weak", but closes "the viscous diffusion effect dominates the evolution of leakage vorticity"; the Abstract says the convection term dominates.
- §4.6 cites "the non-linear Lumley triangle method [31]" and "Lumley et al. [31]"; ref. [31] is Strelets (2001), and no Lumley work is in the list.
- §2.1: "Strelts et al. [31]" for a single-author reference.
- §4.6 places the two-component vertex at "$(-1/6, 1/6)$" in the "coordinate system $(\eta,\xi)$"; Eqs. (14)–(15) with eigenvalues $(1/6,1/6,-1/3)$ give $\eta_b=1/6$, $\xi_b=-1/6$, so the pair is $(\xi_b,\eta_b)$ *(compiler check, not in the sources)*. The same sentence calls this state "asymmetric".
- The text says DES, DES-type and hybrid DES; the Fig. 7 caption and the subscript of Eq. (8) say DDES; the Nomenclature lists both.
- $169\times155\times404=10.58\times10^6$, against "about 13 million hexahedral cells"; the 69-layer tip-gap block is not counted separately in the text *(compiler check, not in the sources)*.
- Typos: "Naiver-Stokes", "Gird Induced Separation", "Shear Stress Transportation", "balde", "a highly accuracy", "chocked".
- Fig. 18 caption names only kinetic energy and normal stresses; the text also reads shear stresses off it.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y$, $z$; $u_1$, $u_2$, $u_3$ | (spanwise, pitchwise, axial coordinates and velocities, kept page-local) | **collision:** the registry's $x$ is streamwise and $y$ wall-normal |
| $\overline{u}$, $u_i'$ | $\langle u\rangle$, $u_i'$ | **collision:** overbar is a time average, not the LES filter |
| $\tau_{ij}=-\rho\overline{u_i'u_j'}$ | $-\rho R_{ij}$ | **collision:** opposite sign and dynamic; not the SGS $\tau_{ij}$ |
| $k$ | $k$ | modelled in Eqs. 1–5, resolved in Eq. 13 |
| $\omega$, $\vec\omega$ | $\omega$, $\omega_i$ | specific dissipation rate; vorticity |
| $\beta^*$, $\sigma_k$, $F_2$ | $\beta^*$, $\sigma_k$, $F_2$ | values not printed |
| $L_t$, $C_{DES}$, $\Delta$, $F_{DES}$ | same | $\Delta=\max_i\Delta_i$ |
| $\sigma$ (Eq. 6) | $\sigma_b$ | upwind fraction of the blended convective flux (§11) |
| $S_{ij}$, $\Omega_{ij}$, $Q$ | $S_{ij}$, $\Omega_{ij}$, (Q criterion) | |
| $\nu_t$, $\nu_m$ | $\nu_t$, $\nu$ | |
| $\tilde{\boldsymbol u}$, $\hat{\boldsymbol u}$ | (coherent wandering velocity; wandering-corrected velocity, page-local) | **collision:** neither a Favre nor a test filter |
| $b_{ij}$, $\lambda_n$ | $b_{ij}$, (its eigenvalues) | |
| $\eta$, $\xi$ | $\eta_b$, $\xi_b$ (Lumley invariants, page-local) | **collision** with $\eta$ (Kolmogorov length) and $\xi$ (reference coordinate) |
| $c$, $h$, $p$ | (chord 71.812 mm, blade height 100 mm, pitch, page-local) | **collision:** $h$ element size, $p$ pressure |

# Reference list

35 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year pairs (Wheeler 2013, [5] and [16]; Tian 2017, [20] and [21]) are
keyed in printed order. [1] is an ASME paper printed with a volume
"78897"; [29] (Arts et al. 1998) prints no venue; [35] prints no pages. No
printed duplicates; all items parsed.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
