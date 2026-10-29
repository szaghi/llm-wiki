---
type: Source
title: "Carlsson et al. (2023) — Investigation of low-dissipation low-dispersion schemes for incompressible and compressible flows in scale-resolving simulations"
description: "Extends the second-order low-dissipation low-dispersion (LD2) scheme of an unstructured node-based finite-volume solver to shocked compressible flow (LD2C: density and sound-speed extrapolation, Ducros-weighted shock sensor) and tests it in decaying isotropic turbulence, IDDES of subsonic and supersonic channels, and DDES of a supersonic base flow."
resource: "doi:10.1016/j.compfluid.2022.105741"
source_kind: paper
authors: [Carlsson M., Davidson L., Peng S.H., Arvidson S.]
year: 2023
venue: "Comput. Fluids 251:105741"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computers_amp_Fluids_Carlsson_Investigation_of_low-dissipation_low-dispersion_schemes_for.pdf"
tags: [numerical-dissipation, hybrid-rans-les, des, compressible, log-layer-mismatch]
timestamp: 2026-10-29T10:03:00Z
---

# Summary

Carlsson et al. (2023) study the convective scheme of the node-based
unstructured finite-volume solver M-Edge in
[hybrid RANS/LES](/definitions/hybrid-rans-les.md). The flux is Kok's
skew-symmetric energy-preserving central flux
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
which brings no dissipation of its own, plus a Jameson–Schmidt–Turkel matrix
dissipation. The [low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
LD2 of Löwe et al. extrapolates velocity and pressure to the faces with
gradients weighted by $a=1/3$ (fourth order on structured meshes) and
lowers the fourth-difference coefficient $\kappa^{(4)}$ far below its RANS
values. The authors' LD2C extends it to shocks: density and speed of sound are
extrapolated too, and second-difference dissipation ($\kappa^{(2)}=5$) is kept,
switched by a Jameson pressure sensor multiplied by the Ducros
dilatation–vorticity ratio, with $\kappa^{(4)}=1/512$.

The Sod shock tube fixes the shock parameters. In decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) with
SA- and SST-based LES, LD2 gives the measured spectra without recalibrating
$C_{DES}$, whereas the reference RANS-type scheme ($\kappa^{(4)}=1/128$) is far
too dissipative. In SST-IDDES of [channel flow](/benchmarks/turbulent-channel-flow.md)
at $M_b=0.15$ ($Re_\tau$ up to 18 000) and $M_b=1.5$, LD2 and LD2C remove
most of the [log-layer mismatch](/definitions/log-layer-mismatch.md) that the
reference scheme shows, so the mismatch there is traced to
[numerical dissipation](/properties/numerical-dissipation.md). The supersonic
profiles are compared after the Trettel–Larsson
[velocity transformation](/definitions/compressible-velocity-transformation.md).
In [SA](/methods/spalart-allmaras-model.md)-based
[DDES](/methods/detached-eddy-simulation.md) of the Herrin–Dutton supersonic
base flow with the shear-layer-adapted length scale, LD2C unlocks the
Kelvin–Helmholtz instability of the separated shear layer much earlier and
improves reattachment and shear stress. The base pressure stays wavy and too
low, as in earlier ZDES and DDES studies. The underlying RANS models are SA and
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md); the channel runs use the
[wall-modelled LES](/methods/wall-modelled-les.md) branch of IDDES. The paper
argues that the dissipation added by the scheme should ideally be minimal so
that dissipation comes from the subgrid model (compare
[implicit LES](/definitions/implicit-les.md)).

# Version read

Version of record (Elsevier, open access CC BY; received 24 April 2022,
accepted 21 November 2022, online 23 November 2022), downloaded from the
Chalmers repository, which prepends a one-page cover sheet: 15 PDF pages, the
14 article pages all read. Page-1 title, authors, venue and DOI match the
metadata above. The cover sheet prints the third author as "Shia-Hui, P."
(surname and forename swapped); the article prints "Shia-Hui Peng". Section,
equation, table and figure numbers on this page are those of this version.

# Key claims

Page-local symbols: $a$ is the face-extrapolation parameter (the source's $\alpha$), $\kappa^{(2)}$, $\kappa^{(4)}$ the second- and fourth-difference dissipation coefficients, $\Psi_i$ the Jameson pressure sensor, $\Phi_i$ the Ducros factor.

1. M-Edge discretizes convection with Kok's central skew-symmetric energy-preserving flux plus a JST matrix dissipation, needed for stability on hybrid grids because the Kok flux provides no numerical dissipation (§2, Eq. 2). **Stated**
2. LD2 extrapolates velocity and pressure to the faces with Green–Gauss nodal gradients weighted by $a$ (Eq. 4); for compressible flow with shocks the authors also extrapolate density and speed of sound (Eq. 5), which Löwe et al. had judged a small effect and not tested beyond subsonic cases (§2.1). **Stated** (Eq. 5 is the contribution)
3. $a=1/3$ gives a fourth-order approximation of the derivative, "the theoretically highest order for any $\alpha$", and $a=0$ the second-order central scheme (§2.3, Fig. 1b). **Stated** (derivation not shown)
4. Löwe et al. found $a=0.36$ and $0.4$ better than $1/3$ on a coarse grid but more dispersive on finer grids and recommended 0.36; Fig. 1 shows small differences between 0.36 and $1/3$, and earlier LES (Carlsson et al. 2020) found little practical difference among $a>0$, so $1/3$ is used (§2.3). **Stated**/**Shown** (semi-discrete analysis)
5. Typical RANS values $\kappa^{(4)}\in[1/128,1/64]$ "will severely dissipate resolved turbulence"; LES of decaying grid turbulence and channel flow indicate $1/512$ to $1/1024$ for scale-resolving simulation (§2.2.1). **Stated** (cited [8,28,11]); **Shown** for decaying turbulence in §4.2
6. Eigenvalue scaling of the fourth-difference coefficient with exponent 0.3 adds dissipation in the stretching direction of highly stretched cells; a Harten entropy fix keeps the eigenvalues above 30% of the spectral radius (§2.2.1, Eqs. 6–7). **Stated**
7. Turkel low-Mach preconditioning replaces the speed of sound by an artificial one controlled by $\min[\max(M^2,KM_\infty^2),1]$, with $K$ typically 1–4 in M-Edge RANS (§2.2.2, Eqs. 9–11). **Stated**
8. The Jameson pressure sensor (Eq. 13) drives the scheme to first order at shocks; its cap of 0.5 limits it to first-order upwind behaviour (§2.2.3, Eqs. 12, 8, 6). **Stated**
9. The Ducros factor $\Phi_i=(\nabla\cdot\boldsymbol u)^2/[(\nabla\cdot\boldsymbol u)^2+|\nabla\times\boldsymbol u|^2+\epsilon]$ alone cannot separate shocks from small dilatations and activates wherever vorticity is negligible; the product $\Psi_i\Phi_i$ (Eq. 15) distinguishes shocks from compressible turbulence (§2.2.3, Eq. 14, cited [18]). **Stated**
10. Sod shock tube: extrapolating $p$ and $u$ (LD2) reduces the oscillation peak at the shock but not at the contact discontinuity; adding $\rho$ and $c$ extrapolation (LD2C) with $\kappa^{(2)}=5$ removes the oscillations upstream of the shock and significantly mitigates the contact-discontinuity peak; $\kappa^{(2)}=5$ is adopted (§4.1, Fig. 2). **Shown**
11. With the Ducros-weighted sensor the Sod results of LD2C are similar to those with the pressure sensor (not shown) (§4.1). **Stated**
12. Decaying isotropic turbulence: the reference scheme ($\kappa^{(4)}=1/128$, $a=0$) gives too steep a decay of the spectrum at high wavenumbers on all three grids ($32^3$, $64^3$, $128^3$); LD2 with $\kappa^{(4)}=1/512$ or $1/1024$ matches the experimental spectra, $1/512$ being only slightly more dissipative (§4.2, Fig. 3). **Shown**
13. LD2 with $\kappa^{(4)}=1/512$ gives the correct decay without recalibrating the standard constants $C_{DES}=0.65$ (SA) and $C_{DES,k\text{-}\varepsilon}=0.61$ (SST); $C_{DES,k\text{-}\omega}=0.78$ gives nearly identical results (not shown) (§4.2). **Shown** (SA, SST $k$-$\varepsilon$ branch)
14. Subsonic channel ($M_b=0.15$, SST-IDDES, wall-modelled grids): LD2 and LD2C agree excellently with DNS for the mean velocity and the total stresses at $Re_\tau=395$, including the $R_{11}$ peak; SA results are very similar (not shown) (§4.3, Fig. 4a,d). **Shown**
15. Activating $\kappa^{(2)}=5$ with LD2 in the low-speed channel shows that the shock-capturing term switches off automatically (§4.3, Fig. 4). **Shown**
16. At $Re_\tau=2400$ and 18 000, LD2 and LD2C leave only a small log-layer mismatch at the RANS–LES interface ($y^+\approx200$ and $\approx2000$), while the reference scheme shows a significant mismatch at all Reynolds numbers, correct in the RANS part and failing "as soon as the model switches to LES due to adding to much numerical dissipation" (§4.3, Fig. 4b,c). **Shown**
17. The van Driest transformation (Eq. 25) is inaccurate for non-adiabatic walls [45,51,52]; the Trettel–Larsson transformation (Eq. 26) is adopted (§4.3). **Stated**
18. Supersonic channel ($M_b=1.5$, isothermal walls): LD2 and LD2C velocity profiles agree well with the DNS of Modesti and Pirozzoli at $Re_\tau=500$ and 1015 and collapse onto Reichardt's law; the $Re_\tau=5000$ case, without DNS, is judged by its agreement with the law; the reference scheme overestimates the velocity in the LES region (§4.3, Fig. 5). **Shown**
19. The supersonic Reynolds stresses are captured less well than the subsonic ones on the same meshing strategy, the $R_{11}$ peak being underpredicted; refining $x$ and $z$ (CMP-1015F) improves the buffer-layer velocity and the stress peak (§4.3, Figs. 5d, 6). **Shown**
20. Earlier base-flow studies (cited): SA-DES with $\Delta_{\max}$ (DESider) gave good base pressure but overestimated recirculation and underpredicted early shear-layer stresses, attributed to excessive $\nu_t$; ZDES (Simon et al.) with the cube-root length and $C_{DES}=0.55$ matched recirculation length and shear stress but overpredicted backflow, with a wavy, too low base pressure; SA-DDES with the shear-layer-adapted length (Guseva et al.) accelerated the instability without a flat base pressure (§4.4). **Stated**
21. In decaying turbulence the shear-layer-adapted length gives the same spectra as $\Delta_{\max}$ with the same constant (§4.4, referring to Fig. 3). **Stated**
22. With the shear-layer-adapted length, the onset of resolved turbulence in the initial shear layer is governed mainly by the numerical dissipation and the grid: the reference scheme strongly delays resolved structures and shows azimuthally coherent Kelvin–Helmholtz rollers, LD2C unlocks the instability and accelerates transition to three-dimensional turbulence, and LD2C on the coarse grid G1 resolves small scales comparably to the reference scheme on the fine grid G3 (§4.4, Fig. 9). **Shown**
23. Base pressure: the experiment is flat around $C_p=-0.102$; the reference scheme is flat on all grids but its mean differs strongly between G1 and G2/G3; LD2C shows radial variations and generally underpredicts it, with a smaller grid dependence (§4.4, Fig. 10a). **Shown**
24. Reattachment: reference scheme $x/R\approx4.0$ (G1) and $\approx3.0$ (G2, G3); LD2C $x/R\approx2.7$ (G2, G3); experiment 2.67. LD2C overpredicts the reverse flow, which explains the low base pressure, and underpredicts the radial size of the bubble (§4.4, Fig. 10b–d). **Shown**
25. LD2C agrees much better with the measured turbulent shear stress at $x/R=1.57$; the reference scheme greatly overpredicts it at $x/R=2.52$, which LD2C mitigates (§4.4, Fig. 10e,f). **Shown**
26. "Improved numerics in the initial shear layer does not produce a better prediction of the base pressure profile"; the wavy pattern agrees with Simon et al. (ZDES, much finer grid) and Guseva et al. (blended centred/upwind-biased scheme, grid like G2) (§4.4). **Shown**/**Stated**
27. Including vorticity in the shock sensor (Ducros) improves the resolved shear stress and contributes to grey-area mitigation in the initial shear layer, compared with the Jameson sensor (§5). **Shown** (base flow; the comparison is reference scheme against LD2C, which also differ in $\kappa^{(4)}$ and $a$)
28. In decaying turbulence the numerical dissipation of the convection term dominates the decay of turbulent kinetic energy; it is controlled by the low-Mach preconditioning and by $\kappa^{(4)}$ "in the range of 1/512 or smaller" (§5). **Shown**

# Printed slips

- **§5:** "The low-dissipative low-dispersive scheme (LD2) by Löwe et al. [28]"; elsewhere LD2 is Löwe et al. [10], and [28] is Probst et al.
- **Eq. (19)** writes the constant $C_{dw}$; the text below gives "$C_w=0.15$".
- **§4.3:** "$y^+\approx2000$ for $Re_\tau=18\,000$ as shown in Fig. 4(b)"; Fig. 4(b) is the $Re_\tau=2400$ case and $Re_\tau=18\,000$ is Fig. 4(c).
- **§4.3:** "Fig. 5 presents ... the total stresses for CMP-5000", while the Fig. 5(d) caption reads "Total stresses, CMP-1015"; the text says the stresses in Fig. 6(b) are not captured as well "for the LD2 and LD2C schemes", while Fig. 6 shows LD2C only.
- **§4.4** refers to the "Ducros sensor in Eq. (14)", **§4.1** to the "Ducros sensor (Eq. (15))"; Eq. (14) is the factor, Eq. (15) the sensor used.
- **Range of $\kappa^{(4)}$:** "$1/512$ to $1/1024$" (§2.2.1) against "in the range of 1/512 or smaller" (§5).
- **Conclusions on stresses:** §5 claims excellent resolved-stress predictions for $Re_\tau=395$, 2400 and 18 000; stresses are shown for $Re_\tau=395$ only (Fig. 4d).
- **Names:** "Simone et al." (§4.4) against "Simon F" in refs. [55,56]; "Corssin" (§4.2) against "Corrsin" in ref. [42].
- **Jameson sensor credit:** the introduction cites [9] (Jameson 1991), §2.2.3 cites [31] (Jameson, Schmidt & Turkel 1981).
- **Eq. (26)** is printed with the square root over the whole product $\frac{\bar\mu}{\bar\mu_w}\frac{\mathrm dy_T^+}{\mathrm dy^+}$; recorded as printed.
- **References [28] and [35]** print identical author lists (Probst, Knopp, Francois, Grabe, Landa, Radespiel) and nearly identical titles ("streamwise sortex" in [28], "streamwise vortex" in [35]) with different venues, years and DOIs (AIAA J. 2016, doi:10.2514/1.J054957; AIAA SciTech 2019, doi:10.2514/6.2019-0331), while the text uses [28] for the incompressible LD2 parameters and the channel time step. The bibliography resolution followed the DOI of [28] on Crossref: Probst, Löwe, Reuß, Knopp & Kessler, AIAA J. 54:2972–2987 (2016), an LD2 paper, so [28] prints the authors and title of [35] by mistake; it is entry `probst-2016`, and [35] is `probst-2019`.
- **Reference typography:** [43] garbled author list ("Yan J. CM, Thiele F."); [25] "Harten A. J."; [1] venue "Advanced in DNS/LES"; [37] (Aupoix & Spalart 2003, roughness extensions) is cited as the SA model itself.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q_i=(\rho,\rho u,\rho v,\rho w,\rho E)$ | (conservative variables at node $i$) | $E$ per unit mass here; **collision:** the registry's $E$ is per unit volume |
| $\tilde F_{ij}$; $\overline{(\cdot)}$, $\widetilde{(\cdot)}$ in Eq. (3) | (Kok face flux and face averages) | **collision:** not the LES filter, not the Favre filter |
| $\alpha$, $\alpha_u,\alpha_p,\alpha_\rho,\alpha_c$ | $a$ (page-local; $\alpha_{\mathrm{ema}}$ is the filter weight on the equilibrium wall model) | **collision:** the registry's $\alpha$ is the DG/FV blending factor |
| $\kappa^{(2)}$, $\kappa^{(4)}$ | $\kappa^{(2)}$, $\kappa^{(4)}$ (registry §11) | **collision:** not the von Kármán constant $\kappa$ |
| $\varepsilon^{(2)}_{ij}$, $\varepsilon^{(4)}$ | (dissipation coefficients, page-local) | **collision:** not the dissipation rate $\varepsilon$ |
| $p$ (exponent 0.3) | (eigenvalue-scaling exponent) | **collision:** not the pressure |
| $C_L$, $C_R$, $c$ | (speed of sound) | **collision:** $C_L$ is not the lift coefficient |
| $\beta$, $K$, $M$ | (preconditioning parameter, its coefficient), $M$ (local Mach) | **collision:** $\beta$ is not the field-inversion correction |
| $\Psi_i$, $\Phi_i$, $\epsilon=10^{-30}$ | $\Psi_i$, $\Phi_i$ (registry §11); $\epsilon$ page-local | **collision:** $\Psi$ also denotes the DDES low-Reynolds correction (Eq. 17) |
| $\Delta$, $\Delta_{\max}$ | $\Delta$ | $\Delta_{\max}$ = largest edge of the dual control volume in M-Edge |
| $\Delta_{SLA}=\tilde\Delta_\omega F_{KH}(\langle VTM\rangle)$ | $\Delta_{\mathrm{SLA}}=\Delta_\omega F_{KH}(\langle VTM\rangle)$ (page-local, as on the DES page) | **collision:** the tilde and angle brackets are not Favre filter or Reynolds average |
| $C_{DES}$, $f_d$, $\tilde f_d$, $f_e$, $C_{dw}$, $d_w$, $\Delta_{wn}$ | ($C_{DES}$, DDES and IDDES functions), $d$ (wall distance) | |
| $\mu_t$ | $\mu_t$ | agrees |
| $\bar u$, $\overline{u_i'u_j'}^+$ | $\langle u\rangle$, $R_{ij}^+$ | **collision:** overbar = Reynolds average; kinematic, positive trace |
| $\tilde u^+$ | $\langle u\rangle_\rho^+$ | Favre-averaged velocity in wall units |
| $u^+_{vD}$, $u^+_T$, $y^+_T$ | (van Driest and Trettel–Larsson velocities), $y^*$ | $y^+_T$ is the semi-local wall distance |
| $Re_b$, $M_b$, $Re_\tau$, $u_\tau$, $\delta$ | $Re_b$, $M_b$, $Re_\tau$, $u_\tau$, $\delta$ | based on the half-height and wall viscosity; agree |
| $M_g$, $U_0$ | (grid mesh size, tunnel speed of the decaying-turbulence experiment) | **collision:** $M_g$ is not a Mach number |
| $M_t$ | $M_t$ | 0.1, agrees |
| $R$, $Re_R$ | $R$ (page-local base radius, as on the [base-flow page](/benchmarks/supersonic-axisymmetric-base-flow.md)), $Re$ based on $R$ | **collision:** $R$ is not a Reynolds stress |
| $C_p$ | $C_p$ | agrees |

# Reference list

57 printed references, numbered style ([1]–[57]), with DOIs for most. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [4] prints no venue; [43], [25] and [1] carry the
printed defects listed above; [28] and [35] are the near-duplicate pair
described under Printed slips, resolved by DOI to `probst-2016` and
`probst-2019`. No cited key equals an ingested Source; the
cited Carlsson et al. (2020) is the authors' AIAA SciTech precursor, a
different work.

# Pages created or updated

Chunk 3 (2026-10-26), cited further in chunks 4, 8, 16. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Supersonic axisymmetric base flow](/benchmarks/supersonic-axisymmetric-base-flow.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
