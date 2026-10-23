---
type: Software
title: "UCNS3D"
description: "UCNS3D is an open-source Fortran 2003, MPI and OpenMP cell-centred finite-volume code for unstructured hybrid meshes that hosts arbitrary-order least-squares WENO, CWENO and TENO reconstructions and a modal discontinuous Galerkin module; the sources use it for multicomponent interface capturing with the five-equation model, for the first unstructured TENO schemes and for hybrid DG–finite-volume schemes with troubled-cell switching."
status: established
aliases: [UCNS3D code]
tags: [software, finite-volume, weno, cweno, teno]
timestamp: 2026-10-23T03:53:00Z
---

# UCNS3D

UCNS3D is the open-source unstructured high-order finite-volume code of
Tsoutsanis and co-workers, written in object-oriented Fortran 2003 and
parallelized with MPI and OpenMP
([Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md), §3, ref. [68];
[Ji, Liang & Fu (2022)](/sources/ji-2022.md), §2.1, §5.10, who give the site
www.ucns3d.com;
[Maltsev et al. (2023)](/sources/maltsev-2023.md), §2.3, who add a modal
discontinuous Galerkin module and hybrid DG–FV schemes). No source describes the code's organization, input or
licence; what follows is the numerical method they run in it.

## Numerical method

**Meshes and unknowns.** Cell averages on conforming tetrahedra, hexahedra, prisms
and pyramids in 3D and triangles and quadrilaterals in 2D, with Gauss–Legendre
quadrature on faces and volumes (Tsoutsanis et al., §3.1, Eqs. (13)–(17); Ji et
al., §2.1, Eqs. (1)–(3)).

**Reconstruction framework.** Each candidate polynomial is a constrained
least-squares fit of the cell averages of its stencil, computed in a reference
space obtained by an affine map of one sub-tetrahedron (or sub-triangle) of the
target cell, which leaves averages unchanged; the basis is zero-mean, the
constraint on the target cell is exact and the others hold in the least-squares
sense, and the pseudo-inverse is obtained once by Householder QR and stored
(Tsoutsanis et al., §3.2, Eqs. (18)–(28); Ji et al., §2.2, Eqs. (4)–(14)).
Maltsev et al. instead solve the reconstruction in physical space, "without
the transformation to a reference space" of the group's earlier work, with a
cell-centred Taylor basis normalised by $h_i$, the square root of the cell
volume, shared with their DG module; the stencil algorithm is the
stencil-based compact one, again with twice as many cells as coefficients,
and the pseudo-inverse is pre-stored (§2.1–2.2.1, Eqs. (6), (13)–(17)). A
stencil carries twice as many cells as the polynomial has coefficients,
"for enhanced robustness" (Tsoutsanis et al., Eq. (23)) or as "recommended"
(Ji et al., Eq. (6)). Smoothness indicators are Jiang–Shu-type integrals of all
derivatives of orders 1 to the degree, taken in reference space without a
mesh-size factor and precomputed as quadratic forms (Tsoutsanis et al.,
Eqs. (33)–(35); Ji et al., Eq. (17)); see
[smoothness indicators](/definitions/smoothness-indicator.md).

**Reconstructions hosted.**

- *Equal-order WENO*: all directional candidates carry the target order, so no
  optimal linear weights are needed (Ji et al., §2.3; Tsoutsanis et al., §3.2.1,
  "the original WENO type of schemes for unstructured meshes").
- *CWENO*: one high-order polynomial on a central stencil and low-order
  polynomials on small directional ("Type3", one per face) stencils, combined in
  the CWENO form with weights $d_k/(\epsilon+\beta_k)^4$; the central linear weight
  is set from a free large parameter. Tsoutsanis et al. use second-order
  directional polynomials and $\epsilon=10^{-6}$ (§3.2.1, Eqs. (29)–(37)); Ji et al.
  use quadratic ones, $\epsilon=10^{-14}$ and the free parameter $10^4$, finding
  larger values sharper but less robust (§2.4, §5.5). See [CWENO](/methods/cweno.md).
- *CWENOZ*: the CWENO combination with WENO-Z-type weights
  $\alpha_k=d_k\big(1+\tau/(\epsilon+\beta_k)\big)$, where $\tau$ is the mean
  absolute difference between each directional indicator and the central one,
  raised to the power $4$, and $\epsilon=10^{-14}$; the unnormalised central
  linear weight is $10^7$, any value above $10^3$ being needed for the design
  order (Maltsev et al., §2.2.2, §3.1, Eqs. (18)–(28), after Tsoutsanis &
  Dumbser).
- *TENO3–TENO6*: the CWENO stencil layout with a sharp cut-off, the large
  polynomial taken alone when smooth and an equal-weight mean of the surviving
  small ones otherwise (Ji et al., §3); see [targeted ENO](/methods/targeted-eno.md).

**Fluxes and time stepping.** HLLC for the multicomponent runs (Tsoutsanis et
al., §3.3) and a rotated-frame HLL with Einfeldt-type Roe-average speeds for the
TENO runs (Ji et al., §4, Eqs. (29)–(36)); SSP-RK3 in both, at CFL 0.4 in Ji et
al. ([HLL-family solvers](/methods/hll-riemann-solvers.md),
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md)). An extended-bounds limiter of
Tsoutsanis is available and is what equal-order WENO5 and WENO6 need to survive
double Mach reflection (Ji et al., §5.8).

**Multicomponent model.** The quasi-conservative
[five-equation model](/definitions/five-equation-model.md) of Allaire, Clerc and
Kokh with the [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md),
the volume-fraction equation in Johnsen–Colonius form with its source evaluated as
a surface integral of the Riemann-solver normal velocity, and reconstruction in
primitive variables, which removes the pressure and velocity oscillations that
conservative reconstruction produces at an isolated material interface
(Tsoutsanis et al., §2, §3.1, §4.2, Figs. 3–4).

**Hybrid DG–finite-volume schemes.** Maltsev et al. evolve the solution by
modal [discontinuous Galerkin](/methods/discontinuous-galerkin.md) of degree
$N=2$ to $4$ on mixed-element meshes, without over-integration, modal
filtering or split-form fluxes (§2.1, §3.6). At every Runge–Kutta stage an a
priori [troubled-cell indicator](/definitions/troubled-cell-indicator.md)
checks the unlimited DG solution: a KXRCF-like shock detector with threshold
$C_k$, or MOOD-type physical and numerical admissibility checks with relaxation
$10^{-3}$ or $10^{-1}$ and bounds over the direct neighbours or over the whole
stencil ([MOOD](/methods/mood-a-posteriori-limiting.md)). In flagged cells the
DG modes above the mean are overwritten by the coefficients of a CWENOZ
reconstruction of the same order from the cell averages; because both use the
same Taylor basis and the mean is kept, the substitution is a copy of
coefficients and conserves (§2.4, §2.5, Eq. (33); see
[WENO limiters for DG](/methods/weno-limiter-dg.md)). A fallback to MUSCL or
first-order Godunov if density or pressure leave positivity or change by more
than $80\%$ at a face quadrature point is coded but was never activated
(Eq. (34)). The authors report that without the $h_i$ normalisation of the
basis they "could not achieve higher than 4th" order (§2.1).

## Verification, validation and performance

- Design orders 3 to 6 on multi-species advection on triangular meshes, CWENO
  and WENO with almost identical errors (Tsoutsanis et al., §4.1, Table 1); TENO3–6
  with errors identical to the linear schemes on 2D advection and design order on
  the isentropic vortex (Ji et al., §5.1–5.2, Tables 1–4, Fig. 2).
- Multiphase validation against experiment: shock–helium bubble interface
  velocities within the experimental uncertainty in 2D and 3D, gas-bubble collapse
  in water and shock–water-column runs compared with other codes and schlieren
  (Tsoutsanis et al., §§4.4–4.6, Table 2; see
  [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md),
  [shock–water column](/benchmarks/shock-water-column.md)).
- Shock-capturing benchmarks on unstructured meshes: solid-body rotation, shock
  tubes, Shu–Osher, explosions, Kelvin–Helmholtz, double Mach reflection on up to
  752,708 triangles, a 3D explosion on tetrahedra (Ji et al., §5).
- Hybrid DG–FV (Maltsev et al., §3, Appendices B–C): pure DG reaches close to
  design order on the isentropic vortex on quadrilateral, triangular and hybrid
  meshes, CWENOZ of the same degree only on finer meshes (Table 1); with all
  cells forced to be troubled the hybrid keeps orders 3.01, 4.04 and 4.99 for
  $N=2$, $3$, $4$ (Table B.4). With active detectors the observed orders exceed
  design (up to 6.89) because the troubled fraction falls under refinement,
  which the authors say makes convergence "practically difficult to determine"
  (Table B.3). Extended bounds flag far fewer cells than direct-neighbour
  bounds; re-checking at every stage or freezing the flag for the step makes a
  negligible difference (§3.2, Fig. 7). Further tests: solid-body rotation,
  Shu–Osher, double Mach reflection, Schardin's shock–wedge problem, the
  inviscid subsonic and supersonic Taylor–Green vortex on $64^3$ and $128^3$
  hexahedra, and the near-field sonic-boom signature of the LM1021 model on the
  5.3 million-cell workshop mesh, where the third-order hybrid matches the
  measured pressure signature better than CWENOZ3 (§3.3–3.8, Fig. 22). The
  datasets are deposited at doi 10.17862/cranfield.rd.21436389.
- Cost of the hybrid relative to pure DG: about $1.4$–$1.5\times$ on coarse
  meshes with many troubled cells and about $1.05\times$ on fine ones (range
  $1.01$–$1.56$ in Table 1), with negligible extra cost while the troubled
  fraction stays within $20\%$ (Maltsev et al., §3.1, Appendix B).
- Cost: CWENO needs "approximately 60–80%" of the time of equal-order WENO
  (Tsoutsanis et al., §4.1). *(Compiler check, not in the sources: from the
  normalized times of their Table 1 at 80 edges per side the ratios are 0.84,
  0.82, 0.64 and 0.62 at orders 3 to 6.)* TENO and CWENO of equal order cost the
  same, and the reconstruction time per element and iteration grows by about 65%
  from TENO3 to TENO6 (for example $1.36\times10^{-6}$ to $2.24\times10^{-6}$ s on
  double Mach reflection), on an Intel Xeon E5-2690 with Intel Fortran 19 and Intel
  MPI 2019, 8 MPI ranks times 7 OpenMP threads (Ji et al., §5.10, Table 7). Large
  runs used the Cambridge Peta4 and HLRS HAWK systems (Tsoutsanis et al.).

## Qualifications

- Both sources print the number of polynomial coefficients as
  $\frac1{d!}\prod_{l=1}^d(r+l)$ for degree $r$ in $d$ dimensions, which includes the
  constant, while their expansions index only the non-constant coefficients by that
  number (Tsoutsanis et al., Eqs. (23), (25); Ji et al., Eqs. (6)–(7)). *(Compiler
  check, not in the sources: the two are consistent only with one coefficient
  fewer.)* Maltsev et al. print the same count as "the number of DOFs"
  against a basis summed from index 0 (Eqs. (2), (5)), and say that it
  "increases exponentially" with the order, while the formula is a polynomial
  of degree $d$ in $r$ *(compiler check, not in the sources)*.
- Maltsev et al. write the Runge–Kutta stages with $+\Delta t\,M^{-1}R_i$
  (Eqs. (29)–(31)) after defining $M\,du/dt+R=0$ (Eq. (9)), a sign
  inconsistency in print *(compiler check, not in the sources)*.
- The central-stencil algorithm is named differently in the two papers
  ("stencil-based compact", Tsoutsanis et al.; "Naive Cell Based", Ji et al., each
  citing an earlier Tsoutsanis paper), and the CWENO configurations differ in the
  degree of the directional polynomials and in $\epsilon$; both are recorded as
  conventions of each paper, not as a disagreement.
- Ji et al.'s version read is a preprint; Tsoutsanis et al.'s CWENO central weight
  parameter is not stated.

# Citations

- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §§2–4, Eqs. (13)–(37), Tables 1–2, Figs. 3–4: code, reconstruction framework, multicomponent CWENO, cost.
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §§2–5, Eqs. (1)–(36), Tables 1–4, 7: reconstruction framework, unstructured TENO, HLL flux, timing (preprint).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2, Eqs. (1)–(37); §3, Table 1, Figs. 4–22; Appendices A–C, Tables B.3–B.4: modal DG module, physical-space CWENOZ, hybrid DG–FV switching, cost.
