---
type: Source
title: "Prieto Saavedra et al. (2024) — An implicit large-eddy simulation perspective on the flow over periodic hills"
description: "Implicit LES of the periodic hill at Re_h = 5600, 10 600 and 37 000 with the SUPG/PSPG-stabilized continuous-Galerkin finite-element code Lethe and no subgrid model, studying how time step, averaging time and mesh affect reattachment and Reynolds stresses."
resource: "doi:10.1016/j.compfluid.2024.106390"
source_kind: paper
authors: [Prieto Saavedra L., Radburn C.E.N., Collard-Daigneault A., Blais B.]
year: 2024
venue: "Comput. Fluids 283:106390"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Computers_amp_Fluids_Prieto_An_implicit_large-eddy_simulation_perspective_on_the_flow_ov.pdf"
tags: [implicit-les, periodic-hill, numerical-dissipation, stabilized-fem, separated-flow]
timestamp: 2026-10-26T10:27:00Z
---

# Summary

Prieto Saavedra et al. (2024) simulate the
[periodic hill](/benchmarks/periodic-hill.md) at the hill-height Reynolds
number $Re_h=5600$, with shorter runs at 10 600 and 37 000, using the
open-source code Lethe. Lethe is a continuous-Galerkin finite-element solver
of the incompressible Navier–Stokes equations with SUPG/PSPG stabilization,
equal-order trilinear ($Q_1$) elements for velocity and pressure, BDF2 time
stepping, Newton linearization and ILU-preconditioned GMRES. No subgrid-scale
model is used. The authors call the approach
[implicit LES](/definitions/implicit-les.md), "often referred to in the
literature as under resolved DNS": the stabilization term, a stabilization
parameter $\tau_u$ times the strong momentum residual, supplies the extra
[numerical dissipation](/properties/numerical-dissipation.md). Because
$\tau_u$ contains $1/\Delta t$, this dissipation depends on the time step as
well as on the mesh.

Meshes of 120K to 4M hexahedra (0.5M to 16M degrees of freedom) are
compared with the 12.4M-cell LESOCC explicit
[LES](/definitions/large-eddy-simulation.md) of Breuer et al. (dynamic
Smagorinsky, see the [dynamic procedure](/methods/dynamic-procedure.md)) and
with Rapp's experiment. At $Re_h=5600$ the mean velocity and Reynolds
stresses agree well with both. On the coarse mesh, *reducing* $\Delta t$
lengthens the reattachment point from 4.73 to 5.37 and degrades the bulk
Reynolds stresses, which the authors attribute to the smaller stabilization;
on the fine mesh all time steps but the largest give similar results, even at
Courant numbers near 2.8. Averaging needs at least 700 s; the reattachment
point approaches the measured $x/h=4.83$ non-monotonically as the mesh is
refined. At 10 600 and 37 000 the Reynolds stresses are overpredicted. The
paper places its wall resolution between [DNS](/definitions/direct-numerical-simulation.md)
and wall-resolved LES ([grid requirements](/results/les-grid-point-requirements.md))
and tabulates earlier periodic-hill studies, including high-order
[DG](/methods/discontinuous-galerkin-spectral-element-method.md) runs,
[Nektar++](/software/nektar-plus-plus.md) implicit LES, the
[WALE model](/methods/wale-model.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) entries. Its stabilization is
residual-based (SUPG/PSPG on a continuous discretization), not a
[jump penalty](/methods/jump-penalty-stabilization.md) on element
interfaces.

# Version read

Version of record (Elsevier, open access CC BY; received 30 December 2023,
accepted 1 August 2024, online 3 August 2024), 16 pages, all read; the
equations on pp. 3 and 5 were checked visually. Page 1 matches the metadata.
The first author's surname is the two-word "Prieto Saavedra"; the archive
filename says only "Prieto".

# Key claims

1. Lethe's stabilized continuous-Galerkin FEM (SUPG/PSPG, $Q_1$–$Q_1$, BDF2) without any SGS model reproduces the mean velocity and Reynolds stresses of the periodic hill at $Re_h=5600$ in good agreement with Rapp's experiment and Breuer et al.'s LESOCC LES, with "minimum discrepancies between the meshes" (§4.1, Figs. 4–5). **Shown**
2. Baseline ($\Delta t=0.1$ s, averaging 207–1000 s, printed as 793 s or 88 flow-throughs) reattachment points: 4.73 (coarse), 4.40 (regular), 4.35 (fine), all shorter than Rapp (4.83) and Breuer et al. (5.09) (§4.1). **Shown**
3. Meshes (Table 4 note): very coarse about 120K cells / 500K DoFs; coarse 250K / 1.1M; intermediate 500K / 2.4M; regular 1M / 4.5M; fine 4M / 16M; against 12.4M cells for LESOCC Case 7 (Table 1). **Stated**
4. Time-step study (§4.2, Table 5), reattachment point and Courant number for $\Delta t=0.1$, 0.05, 0.025, 0.0125 s: coarse 4.73±0.05, 4.87±0.05, 5.07±0.05, 5.37±0.06 (CFL ≈ 2.2, 0.9, 0.5, 0.2); regular 4.40±0.05, 4.59±0.05, 4.80±0.05, 4.88±0.05 (≈ 3.2, 1.6, 0.7, 0.4); fine 4.35±0.4, 4.74±0.4, 4.83±0.4, 4.85±0.4 (≈ 5.1, 2.8, 1.2, 0.6). **Shown**
5. On coarse meshes a smaller time step reduces the accuracy of the mean velocity and especially of the Reynolds stresses in the bulk; the authors explain it by $\tau_u$ (Eq. 10) decreasing with $\Delta t$, which reduces the stabilization dissipation, consistent with Hsu et al., Calderer et al. and Gamnitzer et al. (§4.2). **Shown** (effect) / **Stated** (mechanism)
6. On the fine mesh the strong residual is smaller, the stabilization matters less, and all time steps except the largest (0.1 s) converge towards Breuer et al.'s solution (§4.2, Figs. 6–8). **Shown**
7. "For the case where Re = 5600, we observe that using a stabilized formulation along with an implicit scheme allows us to refine the mesh and use a time step as large as 0.05 without losing the accuracy of the solution" (§4.2). **Shown**
8. On the fine mesh only the smallest time step fulfils "the usual CFL" condition, yet the others still give accurate results; an explicit scheme needs CFL < 0.8 for this case according to Mokhtarpoor et al. (§4.2, Table 5). **Shown** / **Stated** (the 0.8 limit)
9. A cost comparison of implicit against explicit time stepping is out of scope; implicit iterations are generally more expensive (§4.2, §5). **Stated**
10. Mean profiles are independent of the averaging period over 500–1000 s on all three meshes; the largest differences are near the walls and in the Reynolds stresses (§4.3, Figs. 9–11). **Shown**
11. Averaging starts after 207 s (23 hills passed); reattachment error bands follow Krank et al.'s $e=\pm c/\sqrt{T_f}$, with $c$ adjusted by hand so that all extracted points lie in the band (§4.3, Fig. 12). **Shown**
12. The error bands shrink markedly after 500 s and 600 s of averaging, "which reassures that a minimum of 700 s is required to accurately predict specific quantities" (§4.3). **Shown**
13. Reattachment points approach Rapp's measured value as the mesh is refined, non-monotonically (the 500K intermediate mesh shows this); Breuer et al.'s value lies within the coarse-mesh error band (§4.3, Fig. 12). **Shown**
14. The 1M and 4M meshes give very close reattachment points, "indicating that mesh-independent results were obtained" (§5). **Shown**
15. $Re_h=10\,600$ ($\Delta t=0.025$ s, averaging 800 s): reattachment $x/h=4.54$, 4.90, 4.01 (very coarse, coarse, intermediate) against Rapp 4.21 and Breuer et al. 4.69; mean velocity good on all meshes, Reynolds stresses overpredicted; reattachment more sensitive to the averaging period (§4.4, Figs. 13–14). **Shown**
16. $Re_h=37\,000$: reattachment $x/h=4.20$, 4.09, 3.49 (very coarse to intermediate) against Rapp 3.76; velocity underpredicted in the lower channel and overpredicted in the upper; all Reynolds stresses overpredicted, the intermediate mesh closest (§4.4, Figs. 15–16). **Shown**
17. Wall resolution at $Re_h=5600$ (Appendix B, Table B.6), with the paper's $\Delta y^+$ based on half the wall-to-first-node distance: average $\Delta y^+=1.66$, 1.16, 0.61 and maximum 4.30, 3.15, 1.73 for 250K, 1M, 4M; average $\Delta x^+=2.96$, 2.40, 1.39; average $\Delta z^+=4.20$, 2.26, 1.51. The authors place these between DNS (Krank et al.: $\Delta y^+_{\max}<0.86$, $\Delta x^+_{\max}=\Delta z^+_{\max}=7.2$) and wall-resolved LES ($\Delta x^+\approx50$–100, $\Delta y^+\approx1$, $\Delta z^+\approx15$–30), "which is exactly the definition of implicit LES when it comes to mesh resolution" (§3.2). **Shown** / **Stated**
18. Apart from $y^+$ criteria, no a posteriori mesh-quality criteria were found in the literature on stabilized methods (§3.2). **Stated**
19. In implicit LES, "often referred to in the literature as under resolved DNS, there is no subgrid-scale model"; in stabilized approaches the extra dissipation comes from a stabilization term made of a stabilization parameter and the strong momentum residual (§1). **Stated**
20. The paper is "the first work in the literature that studies closely the effect of such parameters when using a stabilized FEM approach" (§1). **Stated**
21. Only two earlier finite-element implicit-LES studies of the periodic hill exist: Krank et al. (high-order DG) and Wang et al. (hp spectral elements) (§1, §2.4). **Stated**
22. Breuer et al. attribute their slightly underpredicted pressure to the SGS model, which delays separation and overpredicts reattachment; earlier implicit-LES studies agree better with Rapp's reattachment point, while their bulk profiles are closer to Breuer et al.'s data (§3.3.2). **Stated**
23. A 1% change of the separation point gives a 7% change of the reattachment point (citing Fröhlich et al.) (§2.3). **Stated**
24. Cost (Appendix C, Table C.9; Niagara, 40 Skylake cores per node), core-hours for 1000 s at $Re_h=5600$ and $\Delta t=0.1$, 0.05, 0.025, 0.0125: coarse 3647, 5180, 6933, 9400; regular 16 800, 24 667, 36 667, 39 933; fine 116 667, 174 000, 188 000, 167 333. $Re_h=10\,600$ (800 s, $\Delta t=0.025$): 3061, 5493, 15 307; $Re_h=37\,000$: 3173, 5440, 15 253 (very coarse, coarse, intermediate). **Shown**
25. Conclusion: implicit LES "provide accuracy, do not require the calibration of a subgrid scale model, and can reduce the computational effort, in terms of mesh size and degrees of freedom" compared with traditional LES (§5). **Stated** (no cost comparison at equal accuracy is shown)

The stabilization parameter (Eq. 10, transient form), with $h_{\mathrm{conv}}$ and $h_{\mathrm{diff}}$ both the diameter of the sphere of the cell's volume in Lethe:
$$\tau_u=\left[\left(\frac{1}{\Delta t}\right)^2+\left(\frac{2\lVert\boldsymbol u\rVert}{h_{\mathrm{conv}}}\right)^2+9\left(\frac{4\nu}{h_{\mathrm{diff}}^2}\right)^2\right]^{-1/2}.$$
The flow rate is held constant by a mean pressure gradient $g_x(t)$ updated as $g_x^{n+1}=g_x^n-(\alpha_{\mathrm{rel}}/\Delta t)(U^0-2U^n+U^{n-1})$, with $U^n$ the average inlet velocity and $\alpha_{\mathrm{rel}}$ a relaxation coefficient whose value is not given (Eq. 2). **Stated**

# Printed slips

- **Table 5 caption:** "The experimental reattachment points are: 4.83 for the experimental benchmark by Rapp [11] and 5.09 for the numerical benchmark by Breuer et al. [12]"; 5.09 is a numerical value.
- **Table 5, fine mesh:** every uncertainty is printed "±0.4", against ±0.05 and ±0.06 for the other meshes (flagged; the text does not allow a check).
- **Mesh names:** the Fig. 12 caption reads "coarse (250K), intermediate (500K), fine (1M) and very fine (4M)", whereas the text and Table 4 call 1M "regular" and 4M "fine".
- **§4.3:** "The lowest averaging period considered was of 500 s or 44 flow throughs and the largest averaging period was 1000 s or 88 flow throughs". With one flow-through $L_x/u_B=9$ s, implied by "207 s, or after 23 hills", 44 and 88 flow-throughs are the windows 207–600 s and 207–1000 s, so "500 s" and "1000 s" read as end times *(compiler check, not in the sources)*. Table 4 gives "500 to 1100" s for the averaging study while the text says 500–1000 s.
- **Breuer et al. averaging:** §3.3.2 gives 1300 s for both Case 7 and Case 9, while Tables 1 and 2 print 145 and 142 flow-throughs; both cannot follow from the same 1300 s at 9 s per flow-through *(compiler check, not in the sources)*.
- **Appendix A:** the hill polynomials are printed with intervals in units of $h$ ($x\in[0;0.3214h]$, …, $[1.429h;1.929h]$), but the coefficients vanish at the hill foot only with $x$ in millimetres for a 28 mm hill (polynomial 6 at $x=54$ gives about 0.0002; at $x=1.929$ it gives about 1.88) *(compiler check, not in the sources)*.
- **Appendix B:** "in terms of wall-coordinates $\Delta x^+$, $\Delta y^+$ and $\Delta x^+$" ($\Delta z^+$ meant); "The average and maximum values are reported in for all the coordinates are reported in Tables B.6–B.8".
- **Table B.6 caption:** "average time of 800 s and a time step of 0.025" for $Re_h=5600$, whose runs average to 1000 s.
- **Table 3:** HHTBLEC/F listed with 200K and 350K cells but 12.4M DoFs.
- **CRediT statement:** "Software, DEFAULT Methodology".
- **§3.3.1, §4.3:** "Rapp et al. [11]" for Rapp's single-author thesis.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u$ | $u_i$ | resolved velocity; no filter symbol (implicit LES) |
| $p^*=p/\rho$ | $p$ (kinematic) | in Eq. 1 $p$ is the periodic (dynamic) part |
| $\boldsymbol\tau=\nu(\nabla\boldsymbol u+\nabla\boldsymbol u^T)$ | $\sigma_{ij}/\rho=2\nu S_{ij}$ | **collision:** called "deviatoric stress tensor"; not $\tau_{ij}$ (SGS stress) |
| $\tau_u$ | (SUPG/PSPG stabilization parameter, page-local) | **collision:** not a stress |
| $h$ | (hill height; $Re_h$ reference length) | **collision:** $h$ is the element size in the registry |
| $h_{conv}$, $h_{diff}$ | $h$ (element size for convection and diffusion) | equivalent-sphere diameter in Lethe |
| $\beta(t)$ | $g_x(t)$ (driving mean pressure gradient, page-local) | **collision** with the field-inversion $\beta(\boldsymbol x)$ and the plasma beta $\beta_p$ |
| $\alpha$ (Eq. 2) | $\alpha_{\mathrm{rel}}$ (relaxation coefficient, page-local) | **collision** with the DG/FV blending factor $\alpha$ |
| $\overline U^n$ | $U^n$ (average inlet velocity at step $n$) | **collision:** overbar is a spatial average, not the LES filter |
| $\boldsymbol v$, $q$, $K$, $\Omega_k$ | (test functions, number of elements, element domain) | |
| $Q_1$ | $N=1$ (trilinear Lagrange) | continuous, not DG |
| $k$ (Tables 1–3) | $N$ | polynomial degree of the cited DG/FEM studies |
| $Re=u_Bh/\nu$ | $Re_h$ | $u_B$ bulk velocity over the crest section (Eq. 4) |
| $u'u'/u_b^2$, $u'v'/u_b^2$ | $R_{11}/u_B^2$, $R_{12}/u_B^2$ | time and spanwise average; sign convention not printed |
| $\Delta y^+=y_{cc}u_\tau/\nu$ | $\Delta y^+$ | **convention:** $y_{cc}$ is half the wall-to-first-node distance |
| $u_\tau$, $\tau_w$ | $u_\tau$, $\tau_w$ | |
| $T_f$, $e=\pm c/\sqrt{T_f}$ | (averaging time in flow-throughs, error band) | Krank et al.'s method |
| RP | $x_R/h$ | reattachment point |
| URDNS | under-resolved DNS | used as a synonym of implicit LES |

# Reference list

38 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Items recorded as
printed: the ERCOFTAC wiki (corporate author); the PhD theses of Rapp (2009),
Z. Chen (2010) and W. Wang (no university printed); four journal items
without volume or article number; one item with a page field "119" only; and
one book-series item printed with both a conference name and *Advances in
Applied Mechanics* vol. 28. Leschziner is printed "Leschzinger". No printed
duplicates.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 10. This source is cited on:

- [Periodic hill](/benchmarks/periodic-hill.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [Variational multiscale method](/methods/variational-multiscale-method.md)
- [WALE model](/methods/wale-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nektar++](/software/nektar-plus-plus.md)
