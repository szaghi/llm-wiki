---
type: Source
title: "Dahlin et al. (2022) — STITCH: A Subgrid-scale Model for Energy Buildup in the Solar Corona"
description: "Implements in a full-MHD adaptive-mesh code the STITCH term, a parametrized boundary source in the induction equation that stands for unresolved helicity condensation, gives a discretely divergence-free face-flux discretization, and reproduces a resolved filament-channel eruption at one fifteenth of the cost."
resource: "doi:10.3847/1538-4357/ac9e5a"
source_kind: paper
authors: [Dahlin J.T., DeVore C.R., Antiochos S.K.]
year: 2022
venue: "Astrophys. J. 941:79"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_The_Astrophysical_Journal_Dahlin_STITCH_A_Subgrid-scale_Model_for_Energy_Buildup_in_the_Solar.pdf"
tags: [mhd, astrophysics, sgs-model, mesh-adaptation, reconnection]
timestamp: 2026-10-26T05:06:00Z
---

# Summary

Dahlin et al. (2022) implement and test
[STITCH](/methods/stitch-helicity-condensation-model.md) (STatistical
InjecTion of Condensed Helicity) for MHD simulations of the solar corona.
The physics it abstracts is helicity condensation (Antiochos 2013).
Same-sense photospheric vortical cells twist the coronal field, reconnection
between neighbouring cells cancels the twist between them, and the twist
flux moves in an inverse cascade to the polarity inversion lines (PILs), where it
accumulates as large-scale shear (a filament channel). Resolving the cells
explicitly ("full helicity condensation", FHC) is costly.

STITCH replaces the cells by one term in the induction equation, taken from
Mackay et al. (2014): $\partial_t\boldsymbol B=-\nabla\times\nabla_s(\mathcal ZB_n)$,
with the single parameter $\mathcal Z=\langle a_c^2\Omega_c\rangle/2$. The term is
divergence-free, leaves the normal field unchanged and injects relative
helicity at the rate $-2\iint \mathcal ZB_n^2\,d\sigma$. Its finite-volume form is
a difference of vertex values on the side faces of the bottom cell layer,
which is a discrete Gauss law. The paper's "subgrid-scale model" is
therefore a parametrized boundary source term (a modified Ohm's law at the
coronal base), not an LES closure: no filter, subgrid stress or
electromotive force is derived. It is a different object from the mean-field
closure of the [subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md).

All runs use the [adaptive-mesh](/methods/mesh-adaptation.md) code ARMS in
spherical geometry, with ideal MHD and an adiabatic temperature equation.
Against an FHC run with 107 cells (about two months of computing), STITCH
with uniform $\mathcal Z$ reproduces filament-channel formation and a breakout
eruption with a fast coronal mass ejection in about four days, a factor 15
in cost. It stores about 20% more free energy, releases less of it, and
releases it faster. A localized $\mathcal Z$ confines energization to one PIL
segment, and a synthetic active region with a corrugated PIL is energized
with no geometry-specific driver. The evidence is numerical, from single
runs without a resolution study.

# Version read

arXiv preprint arXiv:2112.00641v1 [astro-ph.SR], 1 December 2021 ("Draft
version December 2, 2021", "Submitted to ApJ", AASTeX631), 18 pages, not the
ApJ version of record. The "Received/Revised/Accepted December 2, 2021" line
is a template placeholder. Title and authors on page 1 match Crossref
(capitalization differs only). The version read prints no DOI. Section and
equation numbers on this page are those of the preprint.

# Key claims

Page-local symbols: $\mathcal Z$ the STITCH helicity-injection parameter (the
source's $\zeta$, renamed because the registry's $\zeta^\pm$ are the
Elsasser potentials), $B_n$ and $\boldsymbol B_s$ the normal and horizontal
field at the surface, $\nabla_s$, $\nabla_n$ the horizontal and normal
gradients, $H_r$ the relative magnetic helicity, $a_c$ and $\Omega_c$
the radius and rotation rate of a cyclonic cell.

1. STITCH is the extra induction-equation term $\partial_t\boldsymbol B=\nabla\times\partial_t\boldsymbol A_s=-\nabla\times\nabla_s(\mathcal ZB_n)$ of Mackay et al. (2014, Eq. A1); the authors name it STITCH (§2, Eq. 1). **Stated** (derivation cited)
2. The single parameter is $\mathcal Z=\langle a_c^2\Omega_c\rangle/2$, with $\langle\cdot\rangle$ a local space–time average (§2, Eq. 2). **Stated**
3. Assumptions: the cyclonic cells are small, numerous and nominally identical (their properties may vary on large scales), and reconnection between cells is efficient enough that opposite twist fields cancel algebraically (§2). **Stated**
4. The term preserves $\nabla\cdot\boldsymbol B=0$, "subject only to the requirement that [$\mathcal ZB_n$] be sufficiently smooth (i.e., differentiable) everywhere" (§2, Eq. 3). **Derived**
5. It leaves the normal field unchanged, $\partial_tB_n\equiv0$, and changes the horizontal field as $\partial_t\boldsymbol B_s=+\nabla_s\times\nabla_n(\mathcal ZB_n)$, in spherical and Cartesian coordinates (§2, Eqs. 4–5). **Derived**
6. The relative-helicity injection rate is $dH_r/dt=-2\iint \mathcal ZB_n^2\,d\sigma$, as required by helicity conservation through reconnection and twist-flux transport (§2, Eq. 6). **Stated** (details in Mackay et al. 2014)
7. Discretization: on the faces normal to the horizontal coordinates $s_1$, $s_2$, the flux change rates are $\partial_t\Phi_{s_1}=-\mathrm D_{s_2}(\mathcal ZB_n|_{n_0})$ and $\partial_t\Phi_{s_2}=+\mathrm D_{s_1}(\mathcal ZB_n|_{n_0})$, with $\mathcal Z$ vanishing at the top of the first cell layer; the field update divides by the face areas (§2, Eqs. 7–14). **Derived**
8. The four side-face flux changes of every cell sum to zero (each vertex value enters twice with opposite signs): a discrete Gauss law (§2). **Derived**
9. The FHC run uses 107 tessellated $B_r$-conserving cyclonic flows, maximum $|V_\perp|\approx50$ km s⁻¹ after a 1,000 s ramp; energy builds up for about 90,000 s, "approximately two continuous months of computational time". The uniform STITCH run builds up in about 6,000 s, "approximately four days" (§3). **Shown**
10. With $\mathcal Z_0=1.4\times10^{16}$ cm² s⁻¹ the horizontal field is injected at up to about 1 G s⁻¹; Alfvén waves spread it along the channel field lines, and the maximum tangential field is about 100 G (about twice the peak radial field of the minority polarity); the injected tangential flux is about the normal flux of the minority polarity (§3). **Shown**
11. The cost of STITCH is lower by "a factor of 15", matching the reduction in driving time; the saving comes from sub-Alfvénic flux injection replacing subsonic vortical driving; the saving from coarser grids was "not exploited" (§4, §7). **Shown** (one comparison)
12. Both FHC and STITCH form a low-lying, highly sheared filament channel under weakly sheared overlying field, and the whole channel erupts with $V>1000$ km s⁻¹ (§4, Fig. 3). **Shown**
13. The overlying loops acquire shear under FHC but stay nearly shear-free under STITCH, because uniform-$\mathcal Z$ STITCH injects field in a zone of width $w=|B_r|/|\nabla_sB_r|$ next to the PIL, while the FHC channel is at least a cell diameter $2a_c$ wide; here $2a_c\approx w$ (§4). **Shown**/**Stated**
14. Magnetic energy: $E_M/E_{M0}\approx1.24$ (STITCH) against 1.20 (FHC), "some 20% higher" free energy; release $\Delta E_M/E_{M0}\approx0.04$ against 0.10; after the eruption 1.20 against 1.10 (§4, Fig. 4a). **Shown**
15. Release time $\approx1{,}000$ s (STITCH) against $\approx4{,}000$ s (FHC), a release rate higher "by a factor of 0.4*4.0 = 1.6"; the storage rate of STITCH is "just over 15× faster" (§4, Fig. 4b). **Shown**
16. Kinetic energy $E_k/E_{M0}=\langle V^2\rangle/\langle V_A^2\rangle=\langle M_A^2\rangle$ is about $10^{-4}$ in the slow driving and a few $10^{-2}$ in the eruption; the FHC kinetic-energy peak is about 50% above that of STITCH (§4, Fig. 4c). **Shown**
17. The shear proxy $|B_\phi|_{\max}$ rises, declines as the arcade inflates, and peaks again in the flare loops: STITCH 110/80 G, FHC 70/70 G, with a minimum of about 40 G at eruption onset in both (§4, Fig. 4d). **Shown**
18. Injected at the slow FHC rate, STITCH would take longer than FHC to build up; in the true subgrid regime $2a_c\ll w$ the two should agree better and the time-scale disparity grow (§4). **Stated** (not simulated)
19. A localized cosine profile of $\mathcal Z$ (Eq. 15) weakens injection on the eastern, northern and western PIL segments, spreads some injection into the minority-polarity interior through $\mathcal Z$ gradients and gives reversed shear near the centre; only the southern channel is primed to erupt (§5, Figs. 5–6). **Shown**
20. The uniform-$\mathcal Z$ curves halved track the localized curves through the buildup and into the eruption, so the northern and southern PIL segments store roughly equal energy under uniform $\mathcal Z$ (§5, Fig. 7). **Shown**
21. A synthetic active region of 30 subsurface dipoles with a corrugated PIL, driven with $\mathcal Z_0=5\times10^{15}$ cm² s⁻¹, erupts after some 15,000 s with no change to the driving procedure (§6, Figs. 8–9). **Shown**
22. A five-step recipe (assign $\mathcal Z$; evaluate $\mathcal ZB_n$ at the base; difference along the horizontal coordinates; divide by the face areas; multiply by $\Delta t$) applies to "any of the MHD codes presently used by the space science community"; smoothness requires $\mathcal ZB_n\to0$ smoothly at the boundary of a tailored region (§7). **Stated**
23. STITCH avoids the difficulties of flux emergence, shear flows, flux cancellation and flux-rope insertion, can be halted at any time to study marginal stability, and can be combined with those methods (§7). **Stated**
24. STITCH represents generically the outcome of an inverse helicity cascade from any helicity-injecting mechanism, not only convective vortices (§1, §7). **Stated**

# Printed slips

- **Name (§7).** "STatiscal InjecTion of Condensed Helicity"; "STatistical" elsewhere.
- **Subscript.** Eq. 2 prints $\omega_l$, §7 prints $\omega_\ell$.
- **Typos.** "it is simple and ease to use" (§1); "about four time faster" (§4).
- **Storage-rate ratio (§4)** *(compiler check, not in the sources)*. With the printed energy gains (0.24 and 0.20 of $E_{M0}$) and buildup times (about 6,000 s and 90,000 s), the ratio of mean storage rates is $(0.24/6000)/(0.20/90000)=18$, against the printed "just over 15×"; the ratio of the buildup times is $90000/6000=15$. The text attributes its figure to the rate curves of Fig. 4b.

# Notation map

| Dahlin et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$, $\mathbf A$, $\mathbf A_s$ | $\boldsymbol B$, $\boldsymbol A$, (surface-parallel vector potential) | Gaussian units (G) |
| $B_n$, $\mathbf B_s$; subscripts $n$, $s$ | $B_n$, $\boldsymbol B_s$ (page-local) | normal and horizontal to the surface; $B_n=B_r$ in the runs |
| $\nabla_s$, $\nabla_n$ | (page-local) | horizontal and normal gradients |
| $\zeta$, $\zeta_0$ | $\mathcal Z$, $\mathcal Z_0$ (page-local) | **collision** with the registry's Elsasser potentials $\zeta^\pm$; units cm² s⁻¹ |
| $\ell$, $\omega_l$ ($\omega_\ell$) | $a_c$, $\Omega_c$ (page-local) | cell radius and angular rotation rate; **collision** with the specific dissipation rate $\omega$ |
| $\langle\cdot\rangle$ | (local space–time average; volume average in §4) | not a Reynolds average |
| $H_r$ | $H_r$ (page-local) | relative helicity, not the density $H_m$ |
| $\Phi_{s_1}$, $\Phi_{s_2}$, $A_{s_1}$, $A_{s_2}$ | $\Phi_{s_1}$, $\Phi_{s_2}$, $\mathcal A_{s_1}$, $\mathcal A_{s_2}$ (face fluxes, face areas) | $A_s$ is not the vector potential |
| $\Delta_{s_1}$, $\Delta_{s_2}$ | $\mathrm D_{s_1}$, $\mathrm D_{s_2}$ (finite differences of vertex values) | **collision** with the filter width $\Delta$ |
| $\Delta t$ | (time step; also the release time in §4) | two uses |
| $d=2\ell$ | $2a_c$ | **collision** with the wall distance $d$ |
| $w=\lvert B_r\rvert/\lvert\nabla_sB_r\rvert$ | (STITCH channel width) | |
| $V_A$, $M_A$ | $v_A$, (Alfvén Mach number) | |
| $E_M$, $E_{M0}$, $E_k$ | (magnetic energy, its initial value, kinetic energy) | **collision:** not the spectrum $E(k)$ |
| $\phi$, $\psi$, $\theta$, $r$ | (longitude, latitude, colatitude, radius) | |
| $\phi_0,\psi_0,\phi_w,\psi_w$ | (centre and width of the Eq. 15 profile) | |

# Reference list

56 printed references, author–year (AAS) style without titles except
Biskamp (1993). The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-year works
are disambiguated in printed order (Berger 1984 and Berger & Field 1984;
Knizhnik 2017a, b). Priest & Titov (1996) is printed with the journal
"RSPSA" but a DOI of Phil. Trans. R. Soc. A (10.1098/rsta.1996.0136). Lynch
et al. (2016) prints a truncated page "10", Howard et al. (1982) a garbled
"Sheeley, N. R., J.", and several items carry stacks.iop.org URLs without a
DOI. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-25). This source is cited on:

- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [STITCH helicity-condensation model](/methods/stitch-helicity-condensation-model.md)
- [Subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md)
- [Decaying MHD turbulence and its invariants](/results/decaying-mhd-turbulence.md)
