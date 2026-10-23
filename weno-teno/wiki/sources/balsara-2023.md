---
type: Source
title: "Balsara et al. (2023) — Efficient WENO-Based Prolongation Strategies for Divergence-Preserving Vector Fields"
description: "High-order prolongation of face-collocated, divergence-constrained vector fields on AMR hierarchies: an analytically exact fourth-order divergence-preserving reconstruction, and WENO-ADPT, a face-matching WENO interpolation of orders 3–5 followed by a least-squares touch-up that restores the fine-zone constraint to round-off."
resource: "doi:10.1007/s42967-021-00182-x"
source_kind: paper
authors: [Balsara D.S., Samantaray S., Subramanian S.]
year: 2023
venue: "Commun. Appl. Math. Comput. 5:428-484"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_OpenAlex_Communications_on_Applied_Mathematics_and_Computation_Dinshaw_Efficient_WENO-Based_Prolongation_Strategies_for_Divergence-.pdf"
tags: [amr, mhd, weno, reconstruction, smoothness-indicator]
timestamp: 2026-10-23T10:00:00Z
---

# Summary

The paper treats prolongation in [block-structured AMR](/methods/adaptive-mesh-refinement.md):
the transfer of a coarse-zone solution to newly created fine zones, for vector
fields whose normal components live on zone faces and obey an involution, the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
$\nabla\cdot B=0$ or the electric displacement constraint $\nabla\cdot D=\rho_{\mathrm q}$
of computational electrodynamics. Fine faces that overlie coarse faces inherit
the coarse data; only the new internal faces are free
([divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md)).

Two routes are given. (i) An analytically exact, fourth-order volumetric
reconstruction that matches 12 facial moments per face (enough to keep the mean
and two slopes of each of four abutting fine faces) and satisfies the constraint at
all polynomial orders; its coefficient stack lives in an online supplement that the
PDF does not contain. (ii) **WENO-ADP**, a one-dimensional, moment-by-moment
WENO-type hybridization of interpolants of facial values in the normal direction,
at orders $r=3,4,5$, whose divergence error converges at order $r-1$; and
**WENO-ADPT**, which adds a constrained least-squares correction of the internal
fine-face fluxes so that every fine zone satisfies the integrated constraint to
round-off (closed form for refinement ratio two, a KKT system for larger ratios).
The candidate interpolants carry Legendre-basis [smoothness indicators](/definitions/smoothness-indicator.md)
written as sums of perfect squares, following [WENO-AO](/methods/weno-ao.md); the
paper claims the finite-volume analogue as new. It recalls [CWENO](/methods/cweno.md),
WENO-ZQ, [multi-resolution WENO](/methods/multi-resolution-weno.md) and
PDE-aware [hybrid schemes](/methods/hybrid-weno.md) as cheaper alternatives to
[WENO-JS](/methods/weno-js-reconstruction.md)-type reconstruction.

A sub-cycled two-level time step for a Faraday-type update (ADER predictor,
prolongation of fine ghost zones, edge-electric-field defect correction,
restriction) is described. Verification uses prescribed analytic fields (in the
spirit of the [method of manufactured solutions](/definitions/method-of-manufactured-solutions.md))
and a 2D Maxwell scattering test on a static two-level mesh, which reaches
design order 2–4 with the divergence at round-off and no late-time instability at
the fine–coarse interface. Nothing is proved; the evidence is derivation plus
numerics.

# Version read

Version of record (Springer typeset, open access), pp. 428–484, 57 pages, all
read; equations the text layer garbled were read from the page images. Page 1
matches Crossref (title, three authors, venue, DOI). The filename names the first
author by the given name ("Dinshaw") and carries the online year 2022; the
published issue is 2023. Supplements A (finite-volume WENO with perfect-square
indicators) and B (the coefficient stack of the fourth-order exact reconstruction,
Eqs. B.1–B.24) are online-only and were not read; claims resting on them are
recorded as stated. Numbers cited here are those of the version of record.

# Key claims

Registry notation: the source's $IS_i$ is $\beta_k$, its stencil index $i$ is the
candidate index $k$ (numbered from 1, left to right); its $r$ is both the design
order of WENO-ADP and, in §5, the refinement ratio (written $\mathsf r$ below).

1. At fourth order a coarse face abutting four fine faces, each with a mean and two linear moments, needs 12 facial moments, not the 10 of a fourth-order facial reconstruction; the earlier formulation of Balsara et al. (2018) cannot carry the two extra moments, the present one can (§2, Eqs. 2–4, Fig. 3). **Stated**
2. The 12 coarse-face moments follow from the 12 fine-face data by inverting a $12\times12$ linear system, printed in closed form (§2, Eq. 7). **Derived**
3. Three fourth-order volume polynomials (Eqs. 8–10) match all facial moments, satisfy $\nabla\cdot D=\rho_{\mathrm q}$ at all orders of the expansion and minimize the quadratic energy of the field; this needs terms borrowed from fifth and sixth order, and a few zone-centred coefficients are set by a WENO step over neighbouring faces (§2, Supplement B). **Stated** (Supplement B not in the PDF)
4. An analytically exact construction beyond fourth order is "very challenging" because too many terms and constraints must be balanced (§1, §10). **Stated**
5. Moment-by-moment linear interpolation between two opposing faces gives a second-order volume field (Eq. 12), at the price of two extra terms at second order, three at third, four at fourth and five at fifth (§3). **Derived**
6. The WENO-ADP candidates interpolate facial point values, not cell averages: every candidate matches the two zone-face values at $x=\mp1/2$, so every convex combination does, and the nonlinear hybridization keeps the facial values exactly (§3.1). **Derived**
7. Third-, fourth- and fifth-order WENO-ADP use 2, 3 and 4 candidate stencils of $r$ facial values each, with coefficients in Eqs. (15)–(16), (20)–(22) and (26)–(29) (§3). **Derived**
8. The WENO-ADP indicators are sums of perfect squares in the Legendre basis, e.g. $\beta_k=(d^k_x)^2+\tfrac{13}{3}(d^k_{xx})^2$ for $r=3$ (Eqs. 17, 23, 30) (§3). **Derived**
9. Third-, fourth- and fifth-order WENO-ADP have divergence residuals of second, third and fourth order (abstract, §1); Tables 4, 6, 8, 10 show the divergence error converging at about design order minus one (e.g. Table 4, fifth order: 3.79, 3.75, 4.00, 4.01). **Shown** (not proved)
10. Freezing the coarse-face fluxes and correcting only the internal fine faces by least squares (WENO-ADPT) brings the fine-zone divergence to round-off, $1.08\times10^{-15}$ to $4.2\times10^{-13}$, and keeps design order (§§8.3–8.6, Tables 5, 7, 9, 11). **Shown**
11. For refinement ratio two in 2D only 3 of the 4 fine-zone constraints are independent (Eq. 31); one free parameter remains, with a closed-form least-squares optimum (Eqs. 33–36) (§4.1). **Derived**
12. For refinement ratio two in 3D there are 12 internal fine-face fluxes and 7 independent constraints; the five free parameters have closed-form least-squares optima (Eqs. 38–42) (§4.2). **Derived**
13. Because the constraint is written for area-integrated fluxes and volume-integrated charges, the touch-up holds unchanged for non-uniform subdivisions and curved zone boundaries, provided the fluxes are accurate (§§4.1–4.2). **Stated**
14. For refinement ratio $\mathsf r$ the touch-up has $3(\mathsf r^3-\mathsf r^2)$ new facial variables, $\mathsf r^3-1$ independent constraints and $2\mathsf r^3-3\mathsf r^2+1$ free parameters; the free-to-new ratio is $5/12$, $28/54$, $81/144$ for $\mathsf r=2,3,4$ and tends to $2/3$ (Table 1, Fig. 7). **Derived**
15. For $\mathsf r>2$ the touch-up is a constrained least-squares problem solved through a KKT matrix that, for fixed ratio and uniform fine zones, is assembled and inverted once per level, leaving one small matrix–vector product per zone (§5). **Stated**
16. Imposing the constraint with the touch-up slightly lowers the field error relative to plain WENO-ADP (Tables 5 vs 4, 7 vs 6) (§8.3). **Shown**
17. At fourth order the exact reconstruction of §2 has lower error than WENO-ADPT on very coarse meshes (one reconstruction step instead of several), while WENO-ADPT holds the constraint better ($10^{-14}$–$10^{-15}$ against $10^{-12}$–$10^{-10}$), because round-off accumulates in the long Supplement-B coefficient stack (§§8.3–8.4, Tables 2–3, 5, 7). **Shown**
18. The §2 prolongation reaches fourth order in $L_1$ for a divergence-free field (Table 2: 2.91, 3.87, 4.63, 5.07); $L_\infty$ is "not as well-regulated" (1.07, 2.89, 3.43, 3.02) (§8.1). **Shown**
19. The finite-volume WENO of Supplement A prolongs the scalar charge density at design order 2–5 (Table 12, fifth order $L_1$: 4.75, 4.86, 4.96, 4.99), "a very effective algorithm" for unconstrained variables on AMR hierarchies (§8.7). **Shown**
20. Finite-volume WENO smoothness indicators on structured meshes can be written in closed form as sums of perfect squares in a Legendre basis, which "has never been documented in the literature before"; the finite-difference analogue was shown with WENO-AO (§1, §6.3, §10; Supplement A). **Stated** (supplement not read)
21. A two-level sub-cycled AMR step for a Faraday-type update: the coarse step uses an ADER predictor; fine ghost zones at $t^{n+1/2}$ come from the stored ADER space–time reconstruction; at $t^{n+1}$ edge-electric-field defect correction (Eqs. 48–52) and restriction (Eq. 47) follow (§7, Figs. 8–10). **Stated**
22. Without defect correction a sub-cycled composite-mesh code develops late-time instabilities or a local build-up of divergence at fine–coarse interfaces; defect correction makes the composite mesh divergence-preserving (§7). **Stated**
23. The ADER predictor may fill fine ghost zones at $t^{n+1/2}$ but "can never be used to re-initialize a fine mesh", being only approximately divergence-preserving (§7). **Stated**
24. In the 2D Maxwell dielectric-cylinder test, composite-mesh runs at second, third and fourth order reach design order on the final mesh pair (fourth order: 4.47/4.60/4.62 for $D_x$, $D_y$, $B_z$), with the normalized undivided divergence at $10^{-14}$–$10^{-12}$ (Tables 13–15). **Shown**
25. Over "many thousands of timesteps" no late-time instability, error pile-up or mesh imprinting appears at the fine–coarse interfaces, with no ad hoc fix; the authors call this "a conceptually tight solution of this long-standing problem" (§9, Figs. 13–15). **Shown** (one 2D static-patch linear test)
26. The fourth-order scheme reaches design accuracy on coarser meshes than the second- and third-order ones: Fig. 15 (360×180 composite, fourth order) has smaller errors than Fig. 13 (720×360, second order) (§9). **Shown**
27. Because finite-volume-type schemes show asymptotic order only at high resolution, the time-dependent order test was done in 2D, not 3D (§9). **Stated**

# Printed slips

- §4.2, p. 450: "inserted in Eq. (30)"; Eq. (30) is the fifth-order smoothness indicator, the parametrized solution is Eq. (40).
- Eq. (36), p. 446: the last three terms are printed "$+2\phi_1-\phi_2+\phi_3$"; they should be the fine-zone charges, $2Q_1-Q_2+Q_3$. *(compiler check, not in the sources: solving Eqs. (32)–(33) and minimizing the objective (35) symbolically gives Eq. (36) term by term with $2Q_1-Q_2+Q_3$.)*
- §3.2, p. 443: "we have to accept four more polynomial terms" followed by "five more terms is still substantially fewer"; §3.3 assigns five to fifth order.
- §3.3, p. 443: "the ith cubic polynomial corresponding to stencil $S_i$", but Eq. (25) is quartic.
- §§8.5–8.6, pp. 467–468: "mirrors Subsect. 7.3" and "mirrors Subsect. 7.4"; the mirrored subsections are 8.3 and 8.4 (Section 7 has no subsections).
- §1, p. 433: the perfect-square result for finite-difference WENO is attributed to "Balsara et al. [5]" (Balsara & Dumbser 2015, divergence-free MHD on unstructured meshes); §6.3 and §10 attribute it to [6] (WENO-AO, 2016).
- §9, p. 475: "the 2 440 × 1 440 zone simulation"; the reference mesh is 2 880 × 1 440 everywhere else.
- Table 13, p. 477, uniform-mesh $D_y$ block, 360×180 row: the $L_\infty$ error cell is empty and the accuracy cell holds "0.168 288 889 7". The next row's error $2.2859\times10^{-1}$ with order 1.93 implies a 360×180 error near $0.87$ *(compiler check, not in the sources: $0.22859\cdot2^{1.93}\approx0.871$)*; the cell is misplaced or mistyped.
- §9, p. 472: "$\varepsilon_0=8.85\times10^{-12}\,\mathrm{C^2\cdot N^{-1}\cdot m^2}$"; the unit is $\mathrm{C^2\,N^{-1}\,m^{-2}}$.
- Tables 2–11 head the error columns "$B_x$" while the field of Eqs. (53)–(54) and the constraint column are written for $D$.
- §5, p. 451: "Karusch-Kuhn-Tucker" and "Karusch [28]"; the reference list prints "Karush".
- §8.1, p. 462: the sentence "The L∞ norm in Table 2 only measures the maximum pointwise deviation and for the WENO schemes described here." is incomplete.
- Tables 5–7: digit-grouping errors ("1.21 98E−03", "8.98 36E−05").
- The fine-face moments $d^{zk}_x$, $d^{zk}_y$ entering Eq. (7) are not defined (normalization, basis) in the main text, so the printed coupling coefficients of $D^z_x$, $D^z_{xxx}$, $D^z_{xxxy}$ cannot be checked from the PDF. Recorded as unverifiable, not as a slip.
- The nonlinear weights of WENO-ADP (linear weights, $\epsilon$, exponent) are not given in the main text; the scheme cannot be reproduced from the PDF alone.

# Notation map

| Balsara et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$, $\mathbf D$ | $B$; $D$ kept | magnetic induction; electric displacement (page-local) |
| $\mathbf E$, $\mathbf H$ | kept | edge-collocated electric and magnetic fields; **$E$ is the total energy in the registry** |
| $\rho$, $\rho_E$ | $\rho_{\mathrm q}$ | charge density and its reconstructed polynomial; **$\rho$ is the mass density in the registry** |
| $q_0,q_x,q_{xx},\dots$ | kept | Legendre moments of the charge density; **$q$ is the weight exponent in the registry** |
| $D^{x\pm}_0,D^{x\pm}_y,\dots$ | kept | modal coefficients on the right/left $x$-face, Legendre basis on $[-1/2,1/2]$ |
| $D^{x2\pm}_0,D^{x3\pm}_0,D^{x4\pm}_0$ | kept | facial means one, two, three zones beyond the zone faces |
| $S_i$, $i=1,2,\dots$ | $S_k$ | candidate stencils numbered from 1, left to right (registry numbers from 0, $S_0$ most upwind) |
| $d^i(x)$, $d^i_0,d^i_x,\dots$ | kept | candidate interpolant and its Legendre coefficients; **$d_k$ is the linear weight in the registry** |
| $IS_i$ | $\beta_k$ | Jiang–Shu-type indicator in perfect-square form |
| $r$ (§3) | $r$; $n_{\mathrm f}$ (page-local) on [divergence-preserving prolongation](/methods/divergence-preserving-prolongation.md) | design order = facial values per candidate stencil; the registry's $r$ gives design order $2r-1$ for classical WENO, so the concept page renames it |
| $r$ (§5, Table 1) | $\mathsf r$ | refinement ratio; **same letter as the stencil size** |
| $\phi^x_{bk},\phi^x_{tk},\phi^x_{FVk},\phi^x_{ck}$ | $\Phi$, $\Phi^{\mathrm{FV}}$, $\Phi^{\mathrm c}$ (page-local on the prolongation page) | frozen, WENO-ADP and corrected area-integrated fluxes; "FV" is a label |
| $Q_k$ | $\mathcal Q_k$ (page-local) | volume-integrated charge of fine zone $k$; **$Q$ is the SBP stiffness matrix in the registry** |
| $\alpha,\beta,\gamma,\delta,\varepsilon$ | kept | free parameters of the touch-up; **collide with $\alpha_k$, $\beta_k$, $\gamma_k$/$\gamma$, $\delta_k$, $\epsilon$** |
| $B^n_{1,x}$, $b^n_{k,x}$, $E^{n+1/2}_{k,z}$, $e^{n+1/4}_{k,z}$ | kept | coarse (upper case) and fine (lower case) face and edge variables; **$e$ is the specific internal energy in the registry** |
| $\Delta x,\Delta y,\Delta z$ | $\Delta x$, $\Delta y$ | agrees |
| $\boldsymbol\varepsilon$, $\boldsymbol\mu$, $\varepsilon_r$ | kept | permittivity, permeability, relative permittivity |

# Reference list

43 printed references in numbered Springer style ([1]–[43]), alphabetical with the
Balsara entries first, all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `balsara-2023`. No DOIs or arXiv
identifiers are printed. Evans & Hawley [24] is printed with year 1989 and
volume 332 and is keyed by the printed year; Karush [28] is a master's thesis;
[32] and [33] are both Liu & Sarris (2006), keyed in printed order. No printed
duplicates were found.

# Pages created or updated

Chunk 4 (2026-10-23), cited further in chunks 5–6 (2026-10-23). This source is cited on:

* [Block-structured adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)
* [Central WENO (CWENO)](/methods/cweno.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Divergence-preserving prolongation and reconstruction for AMR](/methods/divergence-preserving-prolongation.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [WENO-AO (adaptive-order WENO)](/methods/weno-ao.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
