---
type: Source
title: "Zhang et al. (2024) — Complicated flow in tip flow field of a compressor tandem cascade using delayed detached eddy simulation"
description: "Spalart–Allmaras delayed detached-eddy simulation in OpenFOAM of the tip-clearance flow of a tandem compressor cascade derived from the NACA 65-K48 cascade, validated on the clearance-free cascade; the tandem lowers total-pressure loss by about 20% and forms a second, counter-rotating tip leakage vortex."
resource: "doi:10.1016/j.cja.2024.03.044"
source_kind: paper
authors: [Zhang B., Mao X., Liu B., Wang H., Yang Z.]
year: 2024
venue: "Chin. J. Aeronaut. 37(8):63–78"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Chinese_Journal_of_Aeronautics_ZHANG_Complicated_flow_in_tip_flow_field_of_a_compressor_tandem_ca.pdf"
tags: [des, hybrid-rans-les, spalart-allmaras, turbomachinery, separated-flow]
timestamp: 2026-10-29T07:41:00Z
---

# Summary

Zhang et al. (2024) use [delayed detached-eddy simulation](/methods/detached-eddy-simulation.md)
built on the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md) to
study the tip region of a linear tandem
[compressor cascade](/benchmarks/compressor-cascade.md) with tip clearance,
against a single-row datum with the same clearance. The datum is the NACA
65-K48 cascade (inlet $M_{\mathrm{in}}=0.67$, $Re_c=5.6\times10^5$, chord 40 mm),
lengthened to an aspect ratio of 1.3 with a clearance of 1% of span; the
tandem keeps the overall chord and camber with equal front and rear blades,
percent pitch 0.9 and zero axial overlap. The solver is
[OpenFOAM](/software/openfoam.md) (second-order central convection,
second-order backward time, $\Delta t=10^{-6}$ s) on a half-span domain of
about 6.65 million cells.

The paper uses DDES as a tool: it is presented as the affordable
alternative to URANS for anisotropic unsteady tip flows (see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)), with RANS defects
attributed to its "isotropic hypothesis" (cited, see the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). No model
is developed and no URANS or LES comparison is run. Validation is on the
clearance-free K48 cascade only: the extent and onset of the hub corner
separation and the spanwise loss and outlet angle agree with the
experiments of Hergt et al., with the corner loss slightly under-predicted.

For the clearance cases, the tandem lowers the front-blade tip load, moves
the load peak from about 20% to about 30% axial chord, reduces the
mass-averaged total-pressure loss at the measurement plane by about 20.05%,
and produces a second tip leakage vortex, counter-rotating, from about 60%
axial chord in the rear-blade passage. Endwall pressure spectra peak at a
reduced frequency of about 1.18 (datum) and 1.10 (tandem). Vortices are
identified with the $\Omega$-criterion and the axial-slice topology checked
against Kang's singular-point rule.

# Version read

Version of record (Elsevier, open access CC BY-NC-ND; received 15 June 2023,
online 1 April 2024), 16 pages, all read, the equation pages checked
visually. Page 1 matches Crossref; no identity problem.

# Key claims

1. The tandem cascade, designed from the NACA 65-K48 datum with the same overall chord and camber, percent pitch 0.9 and zero axial overlap (following refs. 12, 30), performs better than the datum "under the premise that the diffusion ability and flow turning are no less" (§2.1, Table 2). **Stated**
2. DDES (Spalart et al. 2006, ref. 28) resolves "the possible nonphysical artifacts that may occur in the shear layer during the transition from RANS to LES by modifying the length scale parameter" (§2.3). **Stated**
3. Grid: 57 spanwise nodes in the tip region (2% of blade height), 33 inside the clearance; in wall units $\Delta z^+<80$ (spanwise), $\Delta y^+<0.5$ (normal to the blade) and $\Delta x^+<130$ (streamwise) over the whole axial range; about 6.65 M cells (tandem) and 5.9 M (datum) (§2.2, Fig. 3). **Stated**
4. $\Delta t=10^{-6}$ s gives about 180 samples per feature period of the passage flow, at a mean Courant number of 0.65 (§2.3). **Stated**
5. On the clearance-free K48 cascade the predicted range and onset of corner separation, reverse flow and endwall cross flow agree with oil-flow visualization (Fig. 5); the computed high-loss corner area is "slightly smaller" than measured and the endwall loss "slightly higher", while spanwise loss and outlet angle agree well, including the high-loss boundary at about 15% span (§2.4, Figs. 6–7). **Shown**
6. The DDES accuracy for tip leakage flow is taken from ref. 24 (Liu, Zhong & Lu 2019) and not re-verified for the clearance case (§2.4). **Stated**
7. Statistics are collected over about 90 feature periods after periodic or quasi-periodic convergence of pressure and mass flow (§3). **Stated**
8. The tandem shows two tip leakage vortex trajectories in the rear-blade passage: the first from about 20% axial chord (as in the datum), the second from about 60% axial chord, formed by the interaction of leakage flow, gap jet and endwall secondary flow (§3.1, Fig. 8). **Shown**
9. The mass-averaged total-pressure loss coefficient at 143% axial chord is reduced by about 20.05% in the tandem; over- and under-deflection near the tip are "effectively controlled" (§3.1, Fig. 10). **Shown**
10. At 98% span the maximum tandem load decreases and its peak moves from about 20% to about 30% axial chord; the suction-side pressure plateau near the datum trailing edge disappears; the same trend holds at 90% span (§3.1, Figs. 12–13). **Shown**
11. The standard deviation of endwall static pressure and the resolved kinetic energy at 98% span are significantly reduced in the tandem, but the local fluctuation intensity near 110% axial chord is larger (§3.2, Figs. 14–15). **Shown**
12. At three endwall points the dominant reduced frequency $fC_e/V_1$ is about 1.18 (datum) and 1.10 (tandem), the same at all points; the text lists secondary datum components 1.46, 2.16 and 9.63, and for the tandem 2.16 plus 16.43 at the point near the front-blade trailing edge (§3.2, Fig. 16). **Shown**
13. In the datum, ultra-high-frequency fluctuations linked to separation exist in the passage, downstream and at mid-span; in the tandem only in the front-blade passage tip flow (§3.2). **Shown**
14. "There is no essential change in the frequency-domain features of the unsteady fluctuations in the blade tip flow field" between datum and tandem (§3.2, Conclusion 3). **Shown**
15. The second leakage vortex rotates opposite to the first; the gap jet "compresses and rubs" the front-blade leakage flow to form it near the rear-blade leading edge (§3.1–3.2, Fig. 18). **Shown**
16. The $\Omega$-criterion iso-surface $\Omega_{\mathrm L}=0.52$ identifies the horseshoe, leakage, tip separation, passage, trailing-edge shedding, hairpin and induced vortices; tip separation and trailing-edge vortices are smaller and passage and first leakage vortices weaker in the tandem (§3.2, Fig. 19). **Shown**
17. Singular-point counts on axial slices at 30, 50, 80, 110 and 143% axial chord satisfy Kang's rule $(\sum N-\sum S)+\tfrac12(\sum N'-\sum S')=0$ (Eq. 15) for both cascades (Tables 3–4, Fig. 22). **Shown**
18. The total number of singular points first rises then falls downstream: datum peak 20 at the trailing edge, tandem maximum 26 at 90% axial chord (§3.3, Fig. 22). **Shown**
19. The tip secondary vortex of the datum does not occur in the tandem, because of the large lateral velocity of the rear-blade leakage flow and the second leakage vortex near the suction side (§3.3). **Shown**
20. RANS has "inherent defects in predicting the strong anisotropic and unsteady characteristics" because its models are "based on the isotropic hypothesis" (§1, citing Tucker 2013, ref. 21). **Stated**

The model as printed, in registry notation ($\tilde\nu$ for the printed
$\upsilon_t$, $\kappa=0.41$, $S$ "the scalar norm of the deformation
tensor", $\sigma$ "a turbulent Prandtl number"; $c_{w1}$, $\sigma$ and the
form of $f_w$ are not printed):

$$\frac{D\tilde\nu}{Dt}=c_{b1}S\tilde\nu+\frac1\sigma\Big[\nabla(\tilde\nu\cdot\nabla\tilde\nu)+c_{b2}(\nabla\tilde\nu)^2\Big]-c_{w1}f_w\Big(\frac{\tilde\nu}{d}\Big)^2,\qquad r=\frac{\tilde\nu}{S\kappa^2d^2},$$

with $c_{b1}=0.1355$, $c_{b2}=0.622$ (Eqs. 1–2); the diffusion term is
transcribed as printed, $\nabla(\upsilon_t\cdot\nabla\upsilon_t)$, without the
molecular viscosity.
The DDES length (Eqs. 3–8):

$$r_d=\frac{\tilde\nu+\nu}{\sqrt{\partial_ju_i\,\partial_iu_j}\;\kappa^2d^2},\qquad f_d=1-\tanh\big[(8r_d)^3\big],\qquad d_{\mathrm{DDES}}=d-f_d\max\big(0,\,d-C_{\mathrm{DES}}\Delta\big),$$

with $\Delta=\max(\Delta x,\Delta y,\Delta z)$ and $C_{\mathrm{DES}}=0.65$,
"calibrated by the decay of isotropic turbulence"; the norm is printed
$\sqrt{V_{i,j}V_{j,i}}$, called the "traditional" representation of $S$.

# Printed slips

- §2.3: "The DDES method adds the molecular visibility ($\upsilon$)".
- §3.2 (Fig. 18 description): "The leakage flow streamlines of the FR and RB" for the front blade (FB).
- Table 1 uses $s$ for both the blade pitch (22 mm) and the tip clearance (0.52 mm).
- §2.2 calls the $y$ direction "normal-to-blade" for $\Delta y^+$ and "pitchwise" for $\Delta y/C_e$ in the next sentence.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\upsilon_t$ ("kinematic eddy viscosity") | $\tilde\nu$ | the SA working variable, printed without tilde |
| $\upsilon$ | $\nu$ | |
| $k=0.41$ | $\kappa$ | **collision** with $k$ (TKE) |
| $S$; $\sqrt{V_{i,j}V_{j,i}}$ | (SA strain norm, page-local); $\sqrt{\partial_ju_i\partial_iu_j}$ | **collision:** not $\lvert S\rvert$; $S$ also counts saddle points |
| $\sigma$, $c_{b1}$, $c_{b2}$, $c_{w1}$, $f_w$, $r$ | as in the registry (SA constants and functions) | |
| $r_d$, $f_d$, $C_{DES}$, $\Delta$ | $r_d$, $f_d$, $C_{\mathrm{DES}}$, $\Delta$ (registry §11 and the DES page) | $\Delta$ the maximum cell size |
| $\tilde d$ | $d_{\mathrm{DDES}}$ (registry §11) | **collision:** the tilde is not a Favre filter |
| $x$ (spanwise), $y$ (normal to blade), $z$ (streamwise) | $z$, $y$, $x$ | **collision:** $\Delta x^+$, $\Delta z^+$ swap |
| $Ma_1$, $Re$ | $M_{\mathrm{in}}$ (page-local), $Re_c$ | inlet Mach number (not the pre-shock $M_1$ of registry §11); chord-based Reynolds number |
| $\omega$ (loss coefficient, Eq. 9) | (total-pressure loss coefficient, page-local) | **collision** with $\omega$ |
| $C_p$ (Eq. 10) | $C_p$ | based on inlet total minus static pressure |
| $k_{res}$, $V'$ | $k_{\mathrm{res}}$, resolved fluctuation | time average over snapshots |
| $\Omega$ (Eq. 14), $A$, $B$, $\varepsilon$ | $\Omega_{\mathrm L}$ (Omega vortex criterion, page-local), symmetric and antisymmetric velocity-gradient parts, small number | **collision** with $\Omega_{ij}$ and $\varepsilon$ |
| $F_C^+=fC_e/V_1$ | $St$ based on $C_e$ and inlet speed | |
| $C_e$, $C_{ea}$, $h$, $s$, $t$ | (equivalent and axial chord, blade height, pitch, lateral offset, page-local) | |
| $N$, $S$, $N'$, $S'$, $N_{sp}$ | (nodes, saddles, half-nodes, half-saddles, total, page-local) | |

# Reference list

38 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. No two printed
references share first author and year. Two printed keys collide with slugs
of different works (ref. 7, Tang & Liu, Chin. J. Aeronaut. 35(11):1–17; ref.
16, Liu B.J. et al., Chin. J. Aeronaut. 35(4):165–175) and are keyed `tang-2022-b` and `liu-2022-p`. Ref.
32 (Spalart & Allmaras 1992) is an AIAA paper. All items parsed.

# Pages created or updated

Chunk 13 (2026-10-28), cited further in chunk 15. This source is cited on:

- [Compressor cascades](/benchmarks/compressor-cascade.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Vortex identification criteria](/definitions/vortex-identification-criterion.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [OpenFOAM](/software/openfoam.md)
