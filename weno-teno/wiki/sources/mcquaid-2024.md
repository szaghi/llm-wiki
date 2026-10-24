---
type: Source
title: "McQuaid & Brehm (2024) — Heat flux predictions for hypersonic flows with an overset near body solver on an adaptive block-structured Cartesian off-body grid"
description: "A hypersonic heat-flux solver coupling an automatically extruded body-conformal near-body grid to a block-structured Cartesian AMR grid, whose off-body WENO-Z flux is blended with a first-order flux by the Ducros sensor to remove shock-induced heating artifacts, validated on MSL, Orion and AS-202 capsules."
resource: "doi:10.1016/j.compfluid.2023.106121"
source_kind: paper
authors: [McQuaid J.A., Brehm C.]
year: 2024
venue: "Comput. Fluids 269:106121"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computers_amp_Fluids_McQuaid_Heat_flux_predictions_for_hypersonic_flows_with_an_overset_n.pdf"
tags: [hypersonic, weno-z, hybrid-scheme, ducros-sensor, amr, overset-grid]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper presents the three-dimensional extension and validation of the
"NBS-Cart" solver of the CHAMPS code for hypersonic viscous flow, perfect gas and
two-temperature five-species air in thermochemical non-equilibrium. A body-conformal,
wall-normal-structured near-body grid is extruded automatically from a surface mesh
and solved with a third-order MUSCL reconstruction, a modified Steger–Warming flux
and an implicit line-relaxation method. It is coupled both ways to a block-structured
Cartesian off-body grid with [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
Cartesian data reach the near-body grid at image points by weighted least squares,
and near-body data are interpolated into three or four Cartesian cell layers next to
the surface, so no [immersed-boundary](/methods/immersed-boundary-method.md)
stencil is needed. Cell counts are 3 to 11.7 million, which the authors call
comparable to body-fitted solutions.

The part relevant to this bundle is the off-body discretization: a fifth-order
finite-difference [WENO-Z](/methods/weno-z.md) flux reconstruction in
[characteristic variables](/methods/characteristic-decomposition.md) on the
Roe-averaged state with Steger–Warming flux splitting, blended with a first-order
flux through the [Ducros sensor](/definitions/ducros-shock-sensor.md),
$\hat f_{i+1/2}=(1-\tilde\alpha_{\mathrm D})\hat f^{\mathrm{WENO}}_{i+1/2}+\tilde\alpha_{\mathrm D}\hat f^{\mathrm{O1}}_{i+1/2}$,
so that the scheme drops fully to first order at strong shocks. This is a
[hybrid scheme](/methods/hybrid-weno.md) whose partner is a first-order flux, not a
central one. On the Mars Science Laboratory capsule at 8° four flux treatments are
compared (WENO-Z with local or stencil-maximum [Rusanov splitting](/methods/lax-friedrichs-flux.md),
with Steger–Warming, and with Steger–Warming plus the Ducros fallback); only the
last removes the velocity streaks that the shock on a non-aligned Cartesian grid
sends to the near-body interface and that imprint a surface heating artifact, at the
cost of a slightly more diffused shock.

Validation is against wind-tunnel data for the Mach 9.47 MSL capsule (0–16°) and the
Mach 6 Orion capsule (16–32°), within the experimental uncertainty, and against the
DPLR solution and flight calorimeters for the AS-202 capsule with five-species air
and a fully catalytic radiative-equilibrium wall. No standard inviscid
shock-capturing benchmark is run.

# Version read

Version of record (Elsevier typeset; received 17 June 2023, accepted 13 November
2023, online 17 November 2023), 27 pages, all read; p. 10 (Eqs. (18)–(30)) checked
visually. Page 1 matches Crossref (title, two authors, venue, DOI). Numbering cited
here is that of this version.

# Key claims

Registry notation (see the notation map): the source's face states $q^L,q^R$ are
$u^-,u^+$, its MUSCL parameter $\kappa$ is $\kappa_{\mathrm M}$, its limiter
$\phi$ is $\psi$, its face-normal velocity $\hat u$ is $v_n$ and its sound speed $a$
is $c$.

1. Cartesian/immersed-boundary solvers need near-wall cell aspect ratios near 1 and cell Reynolds numbers of order one, hence "millions or tens of millions of cells for even the most simple 2D/3D geometries" (§1, citing Meakin et al. [2]). **Stated**
2. A ghost-cell (non-conservative) immersed-boundary solver under-predicts heat flux against cut-cell and body-fitted solvers; Baskaya et al. [6] "demonstrates that a conservative convective and viscous scheme is essential to correctly capturing heating loads" (§1). **Stated**
3. Meshing is fully automatic from a surface mesh, the refinement tracks shock, wake and surface changes, and the approach gives "order of magnitude savings in computational costs versus a fully-resolved Cartesian/IB solver" (§1, §5). **Stated** (no immersed-boundary run is shown)
4. The solver "is the first of its kind to be applied within the context of low and high enthalpy, hypersonic viscous flows" (Abstract). **Stated**
5. The near-body wall-normal spacing is mirrored across the overset interface; two guard cells are used, consistent with the third-order MUSCL stencil (§3.2, Fig. 3). **Stated**
6. Second-order image-point interpolation suffices because the image points lie in smooth flow; "Higher order accuracy has negligible impact on the final solution for the cases tested" (§3.4). **Stated** (no data shown)
7. Interpolating pressure and $n_s-1$ mass fractions, instead of all species densities, into the Cartesian overset cells removes pressure artifacts in the first cell layer; pressure oscillations from overset interpolation affect stability far more than other quantities (§3.5, Figs. 11–12). **Shown** (contours)
8. An extrusion factor $h_{\mathrm{NBS}}/\Delta\tilde x_{\mathrm{Cart}}$ of at least about 4 is needed for a stable coupling, with 4–6 accurate and stable; shock interaction with the near-body interface is avoided because it can be unstable (§3.6, Eqs. (16)–(17)). **Shown** (experience over the test cases)
9. Refinement uses a normalized pressure gradient with level-scaled thresholds 0.05 and 0.1, plus refinement of every block containing subsonic flow for the wake (§3.7, Eqs. (18)–(19)). **Stated**
10. WENO-Z "provides a good compromise between accuracy and cost; it eliminates order reduction at critical points, but it is more expensive than a mapped WENO scheme" (§3.8, citing Brehm et al. [27]). **Stated**
11. The paper calls its scheme "the WENO-Z scheme of Jiang and Shu [25] with smoothness indicators proposed by Liu et al. [26]" (§3.8); no WENO-Z weight, indicator, $\epsilon$ or exponent is printed, and no Borges et al. reference appears. **Stated** (attribution as printed)
12. "For flow-fields with strong shocks on non-aligned grids, even the reduced order WENO scheme can produce pre- and post-shock artifacts", hence characteristic reconstruction on the Roe-averaged state and Steger–Warming splitting in all cases (§3.8). **Stated**
13. Shock artifacts on non-aligned grids that corrupt the surface heat flux are removed "by fully reducing to a first order convective scheme in the presence of strong shocks" through the Ducros blend of Eq. (20); the sensor formula, threshold and regularization are not printed (§3.8). **Shown** (Fig. 14)
14. On MSL at 8°, methods 1–3 produce shock-generated velocity streaks interpolated to the near-body interface and a significant heating artifact; method 4 removes them with a slightly more diffused shock; the cause is assumed to be shock–grid misalignment (§4.1, Fig. 14). **Shown**
15. The modified Steger–Warming flux $\hat f_{i+1/2}=A^+_iu^-_{i+1/2}+A^-_{i+1}u^+_{i+1/2}$, $A^\pm=R\Lambda^\pm L$, $\lambda^\pm=\tfrac12(\lambda\pm\sqrt{\lambda^2+\epsilon_{\mathrm{SW}}^2})$, $\epsilon_{\mathrm{SW}}=0.3(\lvert v_n\rvert+c)$, evaluates $A^\pm$ at the face from a pressure-switched average state, $w=\tfrac12/\big((6\,\Delta_pp)^2+1\big)$ with $\Delta_pp=\lvert p_i-p_{i+1}\rvert/\min(p_i,p_{i+1})$, reverting to the cell-centred evaluation at shocks, to lower the boundary-layer dissipation (§3.8, Eqs. (25)–(32)). **Stated**
16. The Cartesian solver uses two-stage second-order Runge–Kutta and the near-body solver the DPLR line-implicit method; a large CFL mismatch between the two grids can cause oscillations (§3.8). **Stated**
17. MSL grid study at 16°: pressure is converged on all grids; a wall spacing of $2\times10^{-6}$ m slightly under-predicts stagnation heating, $10^{-6}$ and $5\times10^{-7}$ m agree; 100 wall-normal points with $10^{-6}$ m are kept (§4.1, Fig. 15). **Shown**
18. MSL at 0°: stagnation heating is under-predicted by "about 3%", possibly because of the first-order reduction at the shock and of the possibly under-resolved boundary layer of Chen et al. [33] (§4.1, Fig. 17). **Shown**
19. MSL at 8°: slight over-prediction on the leeward fore-body, partly attributed to the first-order reduction; pure WENO-Z stays just below the upper uncertainty bound but has a heating artifact near the nose (§4.1, Fig. 21). **Shown**
20. MSL at 12°: stagnation heating about 5% above Chen et al. [33], within experimental error; at 16° the windward-shoulder heating exceeds the stagnation heating (§4.1, Figs. 23, 25). **Shown**
21. Orion at 16–32° (about 11.7 million points): NBS-Cart "consistently remains within the estimated experimental uncertainty" (±12%); surface pressure and heat flux are insensitive to the wall-normal resolution (§4.2, Figs. 28–29). **Shown**
22. AS-202: peak temperature about 13000 K (the true peak expected slightly higher because of the first-order reduction at the shock), strong thermal non-equilibrium in the shoulder expansion; 75 wall-normal points under-resolve the heating; 5.3 million points in total (§4.3, Figs. 30, 32). **Shown**
23. AS-202 heat-flux decomposition: the vibrational part contributes least, translational–rotational and diffusion parts about equally; peak wall temperature about 2200 K (§4.3, Fig. 33). **Shown**
24. AS-202 aft-body calorimeters: probes a–d, f and g "see good alignment with the flight data with only probe f over-predicting"; the largest disagreement is at probe s (flight 1.2824–1.9327, DPLR 0.2414, CHAMPS 0.2430), cause unknown (§4.3, Table 4). **Shown**
25. A chemical-equilibrium wall would fully recombine O$_2$ at the surface and over-predict heating (§4.3, Fig. 36). **Stated**
26. Future work targets higher-order, low-dissipation schemes for transitional and turbulent flow (§5). **Stated**

# Printed slips

- Eq. (22), MUSCL right state (checked visually on p. 10): printed $q^R_{i+1/2}=q_{i+1}-\tfrac14\big[(1-\kappa)\phi(\nabla r_{i+1})(q_{i+2}-q_{i+1})+(1+\kappa)\phi(\Delta r_{i+1})(q_{i+2}-q_{i+1})\big]$, both terms on $(q_{i+2}-q_{i+1})$. *(Compiler check, not in the sources: with $\psi=1$ this gives $q_{i+1}-\tfrac12(q_{i+2}-q_{i+1})$ for every $\kappa_{\mathrm M}$, against the stated $\kappa$-dependence of the order; the mirror image of Eq. (21) has $(q_{i+1}-q_i)$ in the second term.)*
- Mach number of AS-202: the Abstract says "a Mach 25.2 AS-202 capsule", Table 3 prints $M=25.6$.
- Table 4 against the text: probe g, said to align with the flight data, has CHAMPS 0.9784 above the flight upper bound 0.9695 (DPLR 1.0315); probe e has CHAMPS 1.1498 and DPLR 1.0164, both below the lower bound 1.2630.
- Eq. (33): the local Rusanov splitting is printed $\hat f^\pm_i=f_i\pm\lambda_iU_i$, without the factor $\tfrac12$; summed as printed the split fluxes give $2f_i$.
- Eq. (18) has no absolute value in the numerator of the normalized pressure gradient.
- §1: Meakin et al. simulate the wake of "a sphere", then the text speaks of the separation point "on the cylinder"; "Brahmachary et al. [3], Sekhar et al. [4], and Arslanbekov et al. [5] which both employed".
- App. A: $\gamma_s=\rho_s/(\rho M_s)$ (A.8) and $m_s=M_s/N_a$ (A.9) are both called "the molar concentration"; (A.19) uses $\gamma_t$ where (A.20) defines $y_t$; (A.16) writes $D$ for $D_s$; (A.1) uses $C_{vtr,s}$, defined only through $C_{vt,s}$ and $C_{vr,s}$.
- Units missing: $\rho_\infty$, $T_\infty$ (Table 3), the heat fluxes of Table 4, the aft-body spacing $1.56\times10^{-3}$ (§4.2).
- Symbol reuse: $\alpha$ is the extrusion factor (Eq. 16), the switch sensitivity (Eq. 31) and the kinetic energy per unit mass (App. D); $\epsilon$ the emissivity (Eq. 8) and the Steger–Warming smoothing (Eq. 27); $\gamma_s$ a molar concentration and a catalytic efficiency.
- Ref. [7] prints year 2020 for AIAA paper 2009-3792; ref. [12] prints 2022 with DOI 10.2514/6.2021-0926.

# Notation map

| McQuaid & Brehm (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol U$, $\boldsymbol F$ | $u$, $f$ | conserved state and convective flux |
| $q^L_{i+1/2}$, $q^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | finite-volume face states |
| $\kappa$ | $\kappa_{\mathrm M}$ | MUSCL parameter, $1/3$ used |
| $\phi(\Delta r_i)$, $\phi(\nabla r_i)$ | $\psi(r_i)$ | minmod-type limiter of the forward and backward ratios; $\Delta$, $\nabla$ are labels, not operators |
| $\hat f^{WENO}$, $\hat f^{O1}$ | $\hat f_{i+1/2}$ | fifth-order WENO-Z and first-order fluxes |
| $\tilde\alpha$ | $\tilde\alpha_{\mathrm D}$ (page-local, as on [Ducros sensor](/definitions/ducros-shock-sensor.md)) | Ducros blending weight, formula not printed; **collides with $\alpha_k$ and with the DG–FV blending $\alpha$** |
| $A$, $A^\pm$, $R$, $L$, $\Lambda^\pm$ | $A$, kept, $R$, $L$, kept | face-normal Jacobian and its Steger–Warming split |
| $\epsilon$ (Eq. 28) | $\epsilon_{\mathrm{SW}}$ | eigenvalue smoothing; **not the WENO regularization $\epsilon$** |
| $\hat u$, $a$ | $v_n$, $c$ | face-normal velocity, sound speed; **$a$ is the maximum wave speed in the registry** |
| $w$, $\alpha=6$, $\nabla p$ (Eqs. 29–32) | kept, kept, $\Delta_pp$ | pressure switch, sensitivity, normalized pressure jump |
| $\lambda$ (Eqs. 33–35) | $a$ | Rusanov speed, local or stencil maximum |
| $\alpha=h_{NBS}/\Delta\tilde x_{Cart}$ | kept | extrusion factor |
| $\Psi$, $\Psi_l$, $\Psi_u$, $L_{max}$ | kept | refinement function, thresholds, maximum level |
| $T$, $T_v$, $\rho_s$, $Y_s$ | kept, kept, $\rho_k$, $Y_k$ | two-temperature model, species densities and mass fractions |
| $St$, $Re_{\infty,D}$ | kept, $\mathrm{Re}$ | Stanton and Reynolds numbers |

# Reference list

48 printed references in numbered Elsevier style ([1]–[48]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby` `mcquaid-2024`.
Ref. [6] (Baskaya et al. 2022, AIAA Aviation) is a conference work distinct from the
journal paper `baskaya-2024`; ref. [24] (Browne et al. 2018) is distinct from the
ingested `browne-2022`. Ref. [7] prints 2020 for a 2009 AIAA paper and ref. [12] a
DOI of 2021 with year 2022; both are kept as printed with a note. Seven references are
NASA technical reports; [16] and [45] print volumes without article numbers. No
printed duplicates were found.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–10 (2026-10-23). This source is cited on:

* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Flux vector splitting](/methods/flux-vector-splitting.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [WENO-Z weights](/methods/weno-z.md)
