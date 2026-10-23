---
type: Source
title: "Başkaya et al. (2024) — Assessment of immersed boundary methods for hypersonic flows with gas–surface interactions"
description: "Compares body-fitted, strictly conservative cut-cell and non-conservative ghost-cell immersed-boundary finite-volume solvers on eight reacting hypersonic benchmarks; ghost-cell methods fail on cold-wall heat flux and ablation blowing, which the authors attribute to wall conservation errors."
resource: "doi:10.1016/j.compfluid.2023.106134"
source_kind: paper
authors: [Başkaya A.O., Capriati M., Turchi A., Magin T., Hickel S.]
year: 2024
venue: "Comput. Fluids 270:106134"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computers_amp_Fluids_Başkaya_Assessment_of_immersed_boundary_methods_for_hypersonic_flows.pdf"
tags: [immersed-boundary, finite-volume, amr, reacting-flows, benchmark]
timestamp: 2026-10-23T23:45:00Z
---

# Summary

The paper assesses [immersed-boundary methods](/methods/immersed-boundary-method.md)
on adaptive Cartesian meshes for atmospheric-entry flows in chemical
nonequilibrium with gas–surface interactions (catalysis, ablation). Three
finite-volume wall treatments are compared. The first is a body-fitted (BF)
reference, US3D (modified Steger–Warming flux,
[MUSCL](/methods/muscl-hancock.md) second order, implicit relaxation to steady
state). The second is the strictly conservative cut-cell ("cut-element")
method of the block-Cartesian [AMR](/methods/adaptive-mesh-refinement.md)
solver INCA (third-order finite-volume WENO with HLLC, explicit RK3, Strang
splitting of the chemistry). The third is a pair of non-conservative
ghost-cell methods: CHESS (Steger–Warming flux-vector splitting with MUSCL),
and INCA with its cut-cell flux treatment switched off. All three codes use the
same thermochemistry library, so the authors attribute the differences to the
wall treatment.

Eight cases form a verification and validation set: a 0-D reactor, a 1-D
diffusion tube, a 1-D catalytic diffusion tube with an analytical solution
(Appendix), the five-species Grossman–Cinnella
[shock tube](/benchmarks/sod-and-lax-shock-tubes.md), the HEG
[cylinder](/benchmarks/flow-past-circular-cylinder.md) at $M=8.98$ with inert
adiabatic, inert isothermal and fully catalytic walls, and a graphite ablator
in nitrogen plasma. All codes agree on the verification cases. On the
cylinder, BF and cut-cell results agree "almost exactly". The grid-converged
stagnation heat flux is 7.144 MW/m² (cut-cell) and 7.345 MW/m² (BF), against
an experimental 7.402 ± 0.220 MW/m². The CHESS ghost-cell result on the cold
isothermal wall is 0.167 MW/m², with a larger shock stand-off. Both ghost-cell
methods also over-predict ablation blowing. Since INCA-GP and INCA-CC differ
only in the conservative flux treatment, the authors attribute the failure to
the loss of discrete wall conservation, which acts as a spurious surface
blowing; the conclusion concerns discrete
[local conservation](/results/local-conservation-flux-form.md) at an embedded
boundary. No error analysis is given: the evidence is numerical comparison.

# Version read

Author preprint in the Elsevier template, footer "Preprint submitted to
Computers & Fluids — September 19, 2023", not the version of record. No arXiv
stamp, no DOI or volume printed; the published identity is from Crossref. It
has 37 PDF pages: a graphical abstract and a highlights page, then 35 numbered
pages (Appendix pp. 28–29, references pp. 29–35). Title and authors match
page 1, apart from case and dash differences ("Gas-Surface" in the preprint).
Section, equation, table and figure numbers are those of this preprint.

# Key claims

Registry notation: velocity is $v$, the wall temperature $T_w$. The source's
gas–surface reaction efficiency $\gamma$ is written $\gamma_{\mathrm{GSI}}$
here, to keep $\gamma$ for the ratio of specific heats (see the notation map).

1. Ghost-cell IB methods do not ensure strict conservation of mass, momentum and energy at the fluid–solid interface; the errors in implicitly satisfying the conservative flux boundary condition "result from the nonlinearity of the flux function, from the image point interpolation, and from the interface curvature" (§3, p. 8). **Stated**
2. The cut-cell IB approach ensures strict conservation by the flux balance over the fluid part of each cut cell, with face fluxes scaled by wetted areas and the wall exchange computed from the boundary conditions and a locally interpolated solution; small cut cells are "mixed or merged with nearby cells" (§3, p. 8). **Stated**
3. INCA's cut-element method keeps all details of the intersection of the Cartesian grid with the surface triangulation (several cut-elements per cut cell) instead of a planar cell–wall intersection, giving "sub-cell accuracy and robustness for complex geometries"; it is "a consistent and conservative extension of the finite volume flux balance" (§3.2, pp. 9–10). **Stated**
4. INCA uses ghost cells in addition to cut cells so that unmodified stencils work everywhere; switching off the cut-cell flux treatment yields a standard ghost-cell method with "nominally the same order of convergence" (§3.2, §5, p. 25). **Stated**
5. 0-D reactor (five-species air, Park mechanism): the code-to-code agreement of US3D, INCA and CHESS "is excellent" (§4.1, Fig. 2). **Shown**
6. 1-D diffusion tube: US3D and INCA (100 cells) match "perfectly"; CHESS (400 cells) shows slight mass-fraction differences with identical temperature profiles; Fick and Stefan–Maxwell diffusion differ negligibly in INCA (§4.2, Fig. 3). **Shown**
7. 1-D catalytic diffusion tube: all numerical predictions are "in excellent agreement" with the analytical solution for $\gamma_{\mathrm{GSI}}\in\{0.001,0.01,0.1,1\}$; the wall N₂ mole fraction reaches unity for $\gamma_{\mathrm{GSI}}=1$ (§4.3, Fig. 4). **Shown**
8. Grossman–Cinnella shock tube (600 cells, $t=99\ \mu$s): contact, shock and expansion are captured and the post-shock density peak matches the reference "without any oscillations"; CHESS predicts slightly more N₂ and less N than US3D and INCA. Two-temperature tests showed "no significant differences", so thermal-equilibrium results are shown (§4.4, Figs. 5–6). **Shown**
9. Inert adiabatic cylinder: shock stand-off and N₂/O₂ dissociation agree between BF, cut-cell (IB-CC) and ghost-cell (IB-GP) results; the adiabatic-wall implementation has "no noticeable effect" (§4.5.1, Fig. 7). **Shown**
10. Inert isothermal cylinder ($T_w=300$ K): BF and IB-CC match "almost exactly", including the steep boundary-layer variations; IB-GP shows "a significant difference in the shock stand-off distance", attributed to the non-conservative ghost-cell formulation, whose mass-conservation errors "could manifest as an unphysical blowing from the surface" (§4.5.2, Fig. 8). **Shown** (attribution **Stated**)
11. All methods predict the wall pressure accurately; BF and IB-CC heat fluxes match the experiment better than the simulations of Nompelis reported by Knight et al. (§4.5.2, Fig. 9). **Shown**
12. Grid convergence of the stagnation heat flux (Table 7): BF 8.422 → 7.576 → 7.345 → 7.308 MW/m² for wall cell sizes 0.44, 0.22, 0.1, 0.05 µm; IB-CC 6.684 → 7.028 → 7.144 → 7.189 MW/m² for 2.5, 1.25, 0.625, 0.3125 µm; the medium-fine level is taken as converged for both. IB-CC under-predicts on coarse meshes while BF over-predicts, "a sign of complex interactions between transport and chemistry" (§4.5.2, Fig. 10). **Shown**
13. IB-GP gives 0.167 MW/m² at a 1.0 µm wall cell size, against the experimental 7.402 ± 0.220 MW/m² (Table 7). Brahmachary et al. linked a similar under-prediction to linear interpolation of temperature; because the cut-cell method also uses second-order reconstruction and predicts correctly, the authors attribute the deficiency to conservation errors (§4.5.2, p. 19). **Shown** (attribution **Stated**)
14. Fully catalytic isothermal cylinder ($\gamma_{\mathrm{GSI}}=1$, 300 K): BF and IB-CC are in "excellent agreement"; catalysis raises the heat flux only within the experimental uncertainty, so the effective recombination coefficient of the experiment cannot be inferred (§4.5.3, Fig. 11). **Shown**
15. Taking BF as reference, the IB-CC stagnation heat flux is 2.7 % lower on the inert wall and 0.2 % lower on the fully catalytic wall; the better agreement is "mostly associated with the dominant nature of the catalytic boundary condition" (§4.5.3, p. 21). **Shown** (Table 7 medium-fine values give $(7.345-7.144)/7.345=2.74\,\%$ *(compiler check, not in the sources)*)
16. Ablator, BF with a nine-species N–C mixture including ions: stagnation mass blowing rate 3.41 g/m²s, "within the experimental uncertainty range set by 2.8864 ∓ 0.965 g/m² s", which validates the nitridation model of Eq. (13) (§4.6, p. 22). **Shown**
17. Simplified 2-D ablator (six species, no ions, wall spacing $10^{-5}$ m for all methods): BF and IB-CC agree on stagnation-line species and mass blowing; IB-GP shows "noticeable discrepancies" yet captures the profiles qualitatively (§4.6, Fig. 15). **Shown**
18. Both ghost-cell methods (INCA-GP and CHESS-GP) fail on the isothermal-cylinder heat flux and on the ablator blowing; INCA-GP is closer to INCA-CC and US3D than CHESS-GP, but "both ghost-cell methods give clearly wrong results", and INCA-GP over-predicts the blowing much as CHESS does (§5, Fig. 18). **Shown**
19. Since the only difference between INCA-GP and INCA-CC is the conservative flux treatment, "conservation errors inherent to ghost-cell IB methods are responsible for large errors at cold walls" (§5, p. 26). **Shown** (controlled comparison; mechanism **Stated**)
20. The conservation errors of ghost-cell methods are expected to converge at the rate of the truncation errors of the baseline scheme, so they are small unless the wall gradients of the conserved variables are very large: this explains why errors appear at cold walls and not at adiabatic ones (§5, pp. 26–27). **Stated** (no convergence study of the conservation error)
21. Only a strictly conservative cut-cell IB method is "on par with body-fitted grid methods" (Abstract, §6). **Shown**
22. The 1-D catalytic diffusion tube has an analytical solution from Fick's law in the molar continuity equation (no advection, constant temperature, steady state), with the wall constant solved by Newton–Raphson (Appendix, Eqs. (.1)–(.5)). **Derived** (the printed form has a slip; see Printed slips)

# Printed slips

- Appendix, Eqs. (.3)–(.4): the printed solution is $x_{\mathrm{N_2}}=e^{C_1M_{\mathrm N}\eta}e^{C_2M_{\mathrm N}}/M_{\mathrm N}$ with $C_2=\ln M_{\mathrm N}/M_{\mathrm N}$, derived from "$(X_{N_2})_{\eta=0}=0$". Substituting (.4) gives $e^{C_2M_{\mathrm N}}=M_{\mathrm N}$, hence $x_{\mathrm{N_2}}=e^{C_1M_{\mathrm N}\eta}$ and $x_{\mathrm{N_2}}(0)=1$, not 0. Eq. (.2), $\frac{d}{d\eta}\big(\frac{1}{x_{\mathrm{N_2}}+1}\frac{dx_{\mathrm{N_2}}}{d\eta}\big)=0$, integrates to $x_{\mathrm{N_2}}=e^{a\eta+b}-1$, and the boundary value gives $b=0$. The printed (.3) satisfies it only with a trailing "$-1$". With that "$-1$", the denominator $2-e^{C_1LM_{\mathrm N}}$ of (.5) equals $1-x_{\mathrm{N_2}}(L)=x_{\mathrm N}(L)$, which supports the reading. *(compiler check, not in the sources)* The same sentence also writes $X_{N_2}$ for $x_{N_2}$.
- Author spelling alternates: "Grossman and Cinnella" (§4.4 first line, Fig. 5 caption, ref. [56]) and "Grossmann and Cinnella" (§4.4, twice).
- "IB methologies" (§1, p. 4).
- The experimental blowing rate is printed "2.8864 ∓ 0.965 g/m² s" (§4.6), with "∓" for "±".
- Conclusion: "two non-conservative ghost-cell methods implemented in INCA and an independently developed solver" reads as two methods in INCA; the Abstract and §5 have one ghost-cell method in INCA and one in CHESS.

# Notation map

| Başkaya et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u$ | $v$ | velocity |
| $\rho$, $p$, $E$, $e$ | $\rho$, $p$, $E$, $e$ | **$E$ is specific total energy here** ($\rho E$ the energy density), not the registry's energy per unit volume |
| $\rho_i$, $y_i$, $x_i$ | $\rho_k$, $Y_k$, kept | species partial density and mass fraction (registry index $k$); $x_i$ mole fraction kept |
| $\overline M$, $M_i$ | $\bar W$, $W_k$ | mixture and species molar masses |
| $\dot\omega_i$ | $\Omega_k$ | gas-phase mass production rate |
| $\dot\omega_{i,\mathrm{wall}}$, $\mathbf J_i$ | kept | surface source and diffusion flux of species $i$ |
| $\gamma$ | $\gamma_{\mathrm{GSI}}$ | **gas–surface reaction efficiency; collides with the ratio of specific heats** |
| $\boldsymbol\tau$, $\mu$, $\lambda$, $\mathbf q$ | kept | viscous stress, viscosity, conductivity, heat flux; **$\lambda$ is not an eigenvalue** |
| $T_w$, $T_{\mathrm{wall}}$ | $T_w$ | wall temperature (both spellings printed) |
| $\Delta h_w$ | kept | wall-normal size of the first cell (Table 7) |
| $\eta$, $L$, $C_1$, $C_2$ | kept locally | Appendix coordinate, tube length, integration constants; **$\eta$ is the entropy in the registry** |
| BF, IB-CC, IB-GP; INCA-CC, INCA-GP, CHESS-GP | kept | body-fitted, cut-cell and ghost-cell labels of §4.5 and §5 |

# Reference list

60 printed references in numbered style ([1]–[60]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby`
`baskaya-2024`. No reference prints a DOI. AIAA papers are entered as
`@misc`. Ref. [17] (a PhD thesis) prints no institution and the date "(12
2022)"; ref. [30] (NASA report) prints "(10 2002)"; ref. [41] is a
WCCM-ECCOMAS 2020 proceedings item printed with year 2021. Refs. [16]
(AIAA 2022-3276, the conference precursor) and [51] (3AF conference) are
same-group works distinct from this source. No printed duplicates were found.

# Pages created or updated

Chunk 7 (2026-10-23). This source is cited on:

* [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
