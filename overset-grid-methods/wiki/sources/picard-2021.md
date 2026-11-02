---
type: Source
title: "Picard et al. (2021) — A Finite Volume Chimera Method for Fast Transient Dynamics in Compressible Flow Problems"
description: "Cell-centred second-order finite-volume Chimera method for fast transient compressible two-component flows: a fixed patch superposed on an unmodified substrate without hole cutting, two ghost-cell layers, intersection-volume-weighted limited linear interpolation, a corner-radius limiter, and tests of accuracy, conservation and patch/substrate cell ratio."
resource: "doi:10.1080/10618562.2021.2009468"
source_kind: paper
authors: [Picard A., Lelong N., Jamond O., Faucher V., Tenaud C.]
year: 2021
venue: "Int. J. Comput. Fluid Dyn. 35:799-825"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2021_Crossref_International_Journal_of_Computational_Fluid_Dynamics_Picard_A_Finite_Volume_Chimera_Method_for_Fast_Transient_Dynamics_i.pdf"
tags: [chimera, finite-volume, compressible, shock-capturing, interpolation, conservation]
timestamp: 2026-11-02T14:54:00Z
---

# Summary

Picard, Lelong, Jamond, Faucher and Tenaud build a cell-centred, explicit, second-order
finite-volume [Chimera](/definitions/overset-grid.md) method for fast transient compressible
flows, with nuclear-safety accident scenarios in mind. A fixed, independently meshed local grid
(the *patch*) that carries a geometric detail is superposed on an unmodified global grid (the
*substrate*). The two-grid system is a [composite overlapping
grid](/definitions/composite-overlapping-grid.md) in which **no cell is deactivated**: the method
does no [hole cutting](/methods/hole-cutting.md), and the covered substrate cells keep being
integrated. The flow model is the five-equation two-component Euler system of Allaire, Clerc and
Kokh, solved by a MUSCL–Hancock/HLLC Godunov scheme with least-squares gradients and the
"K-Dubois" limiter, so the paper also bears on [shock capturing on overlapping
grids](/methods/shock-capturing-on-overset-grids.md).

The [domain connectivity](/definitions/domain-connectivity.md) is built once from geometric
cell–cell intersections. Each grid gets two layers of ghost cells, the paper's name for
[receptor (fringe) cells](/definitions/fringe-point.md), and a condition from the
[explicit-interpolation](/definitions/explicit-and-implicit-interpolation.md) literature keeps the
donor cells off the receptor layers. A last step closes the gap between the two receptor sets. The
[inter-grid interpolation](/methods/inter-grid-interpolation.md) gives each receptor the
intersection-volume-weighted average of the donor cells' limited linear reconstructions, evaluated
at the intersection barycentres. It is claimed second order on any mesh. The paper says outright
that it is not globally conservative: only flux interpolation is, which places it against the
[conservative overset interface](/methods/conservative-overset-interface.md) methods. A modified
limiter uses the cell-corner radius instead of the face-centre radius, because intersection
barycentres can lie farther from the cell centre than any face centre as the patch/substrate cell
ratio grows.

Five tests: advection of a sine density wave (second order kept, consistent with the
[interpolation-order requirement](/results/interpolation-order-requirement.md)), a stationary
Mach-1.5 shock on the patch boundary (conservation errors at most 0.635 %), Mach-3 flow past a
cylinder ([flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md),
[shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md); up to 3.5 times cheaper
than an equivalent fine single mesh), a shock–helium-bubble interaction and the double Mach
reflection. Artifacts appear at a cell ratio of 8, and the authors recommend at most 4. The patch
is static; [moving grids](/methods/moving-overset-grid.md) are future work.

# Version read

The HAL deposit hal-03779335v1 (deposited 19 September 2022): a revised author manuscript at the
accepted stage, not the journal typeset version. It has 40 PDF pages: a HAL cover page plus 39
manuscript pages, with references on pp. 37–39. The footer reads "Preprint submitted to
International Journal of Computational Fluid Dynamics, September 24, 2021", and the revised
passages are printed in red. All pages were read and pp. 4–12 checked visually. Page 1 matches
Crossref in title and author order; the journal pagination (799–825) does not apply. Section,
equation, table and figure numbers below are those of the manuscript.

# Key claims

Below, $G_1$ is the substrate and $G_2$ the patch, $h_1$ and $h_2$ their cell sizes, and the
cell ratio is $\kappa_h=h_1/h_2$ (the paper's $\chi$; $>1$ means a finer patch).

1. Grids exchange data by injecting into receptor cells conservative variables interpolated from
   the other grid at every time step. Receptors are not integrated and serve only for fluxes at the
   faces of donor-side cells. The exchange is symmetric between patch and substrate. (§3.2.1,
   Fig. 1) **Stated**
2. Receptor detection is done once (static patch). It deactivates no cell and modifies no grid,
   unlike the cited Chimera assemblies. (§3.2.2) **Stated**
3. Substrate receptors $\mathcal R_1$ must satisfy $\mathcal R_1\cap\mathcal R_2=\emptyset$ and
   $\mathcal R_1\cap\Omega_2\neq\emptyset$, the explicit-interpolation condition taken from the
   Ogen report. (Eq. 12) **Stated**
4. A final marking step reduces the gap between the two receptor sets (their minimum centre
   distance, Eq. 13) by adding patch receptors between them without breaking Eq. 12; it
   "eventually improves the stability" at high cell ratios. (§3.2.2) **Stated** (no separate test)
5. Two receptor layers ($n_f=2$) are needed so that a second-order flux at the first non-receptor
   face is independent of the patch boundary; $n_f=2$ throughout. (§3.2.3, Fig. 3) **Stated**
6. The receptor value
   $\mathbf q_{\mathbf i}=\sum_{\mathbf j}\dfrac{\lvert V_{\mathbf i}\cap V_{\mathbf j}\rvert}{\lvert V_{\mathbf i}\rvert}\big(\mathbf q_{\mathbf j}+\Phi_{\mathbf j}\nabla\mathbf q_{\mathbf j}\cdot(\tilde{\mathbf x}_{\mathbf i\mathbf j}-\mathbf x_{\mathbf j})\big)$,
   summed over the donor cells $V_{\mathbf j}$ that intersect the receptor cell $V_{\mathbf i}$,
   with $\tilde{\mathbf x}_{\mathbf i\mathbf j}$ the barycentre of the intersection and
   $\Phi_{\mathbf j}$ the limiter, is "spatial 2nd-order accurate … without any constraint on
   meshes". (§3.2.4, Eq. 15) **Stated**, supported by claim 10 **Shown**
7. The method is not fully conservative: "the only conservative Chimera approach is based on flux
   interpolation". (§3.2.4) **Stated**
8. The standard K-Dubois limiter (search radius = largest face-centre distance) can let the
   transfer create local extrema, because $\tilde{\mathbf x}_{\mathbf i\mathbf j}$ can lie farther
   from $\mathbf x_{\mathbf j}$ than every face centre, increasingly with the cell ratio. (§3.2.5,
   Eq. 18, Figs. 5–6) **Derived** (geometric argument)
9. Replacing the face-centre radius by the corner radius (Eq. 19) makes the limiter valid "whatever
   the location of the ghost cell and the cell ratio". (§3.2.5) **Stated**
10. Sine advection with cell ratio 1 and a non-coincident patch: $L_1$ density errors within about
    2 % of the single grid at all six resolutions; observed orders reach 2.026 (Chimera) against
    2.022 (single) between 800 and 1600 cells, and 2.108 against 2.119 between 1600 and 3200.
    (§4.1, Table 1) **Shown**
11. With a 200-cell substrate and cell ratios 1–16, the $L_1$ error falls only from 5.607e-5 to
    4.014e-5: the coarse substrate dominates, and the exchange errors "do not impact the global
    solution error when the patch is finer". (§4.1, Table 2) **Shown**
12. Stationary shock on the patch boundary, coincident grid interfaces, ratio 1: the conservation
    errors $\varepsilon_{\mathrm c}$ equal those of the single grid to all printed digits
    (5.97e-4 %, 2.45e-3 %, 4.46e-3 % for mass, momentum, energy). (§4.2, Table 3) **Shown**
13. Non-coincident interfaces: $\varepsilon_{\mathrm c}$ is 0.434 %, 0.635 %, 0.465 % at ratio 1
    and between 0.115 % and 0.599 % for ratios 2–16, never above 1 %. (§4.2, Tables 3–4) **Shown**
14. With non-matching grids the post-shock density jump loses at most 0.35 % of the exact state,
    judged "acceptable for industrial applications". (§4.2, Fig. 11b) **Shown**
15. Mach-3 cylinder, ratio 1: the time-averaged pressure force differs from the single grid by
    1.7 %, 1.47 %, 0.27 % and 0.47 % for 50–400 cells on the perimeter, converging toward about
    $202\times10^3$ N. (§4.3, Table 5) **Shown**
16. The moving front shock crosses into the patch without spurious reflection. (§4.3, Fig. 14)
    **Shown**
17. With a 100-cell substrate and ratios 1, 2, 4: errors against the equivalent fine single mesh
    1.47 %, 0.27 %, 0.5 %; CPU-time ratios 0.97, 2.3, 3.5; memory ratios 0.97, 2.41, 3.8. No
    hardware is stated. (§4.3, Table 6) **Shown**
18. The bow-shock standoff converges to the analytical value $0.3649D$ of Sinclair and Cui: a
    refined patch on a coarse substrate (ratio 4) gives the same standoff (0.372, 1.95 % error) as
    the uniformly refined grids. (§4.3, Table 7) **Shown**
19. Shock (Mach 1.22)–helium bubble at ratio 1 agrees with the single grid; a slight loss of
    symmetry at 200 cells is attributed to the 30°-rotated patch. (§4.4, Figs. 23–24) **Shown**
20. With a 50-cell substrate and ratios 1–8 the solution improves without artifacts: "Unlike what
    Pärt-Enander and Sjögreen observed, we show that refining a patch model … improves the quality
    of the solution without any discernable numerical damage". (§4.4, Fig. 25; §5) **Shown**
    (qualitative)
21. Double Mach reflection, ratio 1: Mach stems, reflected shocks and slip lines coincide with the
    single mesh; a few oscillations in the substrate are attributed to transfers interfering with
    acoustic waves. (§4.5, Fig. 28) **Shown**
22. Double Mach reflection with an 80-cell substrate: ratios 2 and 4 agree very well with the
    equivalent fine meshes; at ratio 8 the abrupt spacing change at the patch boundary perturbs the
    slip lines and the jet; artifacts arise when the ratio is "at least greater than 4", and the
    conclusion recommends at most 4. (§4.5, Figs. 29–31; §5) **Shown**
23. Double Mach reflection cost ratios (fine single mesh over Chimera) for ratios 1, 2, 4, 8: CPU
    0.39, 1.14, 2.38, 2.54; memory 0.43, 1.30, 2.67, 3.62. (§4.5, Table 8) **Shown**
24. The intersections are "already 3D compatible"; 3-D validation, moving deformable structures
    crossing the overlap, and an immersed-boundary FSI extension are future work. (§5) **Stated**

# Printed slips

- **Table 1:** the single-grid order at 100 cells is printed 1.595; the printed errors give
  $\log_2(1.609\times10^{-4}/5.499\times10^{-5})=1.549$. The other nine printed orders agree with
  the printed errors *(compiler check, not in the sources)*.
- **Table 5, 400 cells:** printed "0.47 %"; the printed forces give
  $\lvert202164-203000\rvert/203000=0.412\,\%$ *(compiler check, not in the sources)*.
- **§4.4 domain:** "$(x\times y)\in[-44.5\times10^{-3};44.5\times10^{-3}]\times[0;170\times10^{-3}]$
  m²" while the bubble centre is $x_b=52.5\times10^{-3}$ m and Fig. 20 labels $L_x=17$ cm,
  $L_y=8.9$ cm: the intervals are swapped.
- **§4.4 patch:** "a $6\times10^{-3}$ m side square grid, centered on the initial bubble
  location", while the bubble diameter is $50\times10^{-3}$ m and the bubble "is only prescribed
  inside the patch grid".
- **Eq. 26:** the post-shock state is assigned to "$x>x_s$" and quiescent air to "$x\le x_s$",
  though the shock at $x_s$ "moves to the right towards the bubble"; the inequalities are reversed.
- **§4.3:** "radius $D=1$ m" while the standoff is normalized by $D$ and the shock starts "8
  cylinder diameters" upstream; "$t^\star=tu_\infty/L$" with $L$ undefined for this test; a front
  shock "with a Mach number equal to $M_{sh}=1$"; "infinite Mach number $M_\infty=3$".
- **Fig. 18 caption:** "for the second study cases ($\chi=1$)" while the panels show $\chi=\{1,2\}$
  and $\{2,4\}$.
- **§3.2.5:** the limiter "acts on the primitive variables", while Eq. 15 applies the same
  $\Phi_j$ to gradients of conservative variables. The limiter is called "the K-limiter of Dubois
  [51]", but ref. [51] is printed as Solyga and Galon.
- **§3.2.5 and Eq. 18:** intersections printed with primes on substrate cells (primes mark patch
  cells in §3.2.1); text $\tilde{\mathbf x}_{ik}$ against Eq. 18's $\tilde{\mathbf x}_{ki}$; the
  figure references to Figs. 5 and 6 appear swapped; "$\mathbf x_{(nnode)_l}$".
- **Fig. 2 caption:** "2nd order reconstruction ($N=2$)"; $N$ is never defined.
- **§5:** the stationary-shock conservation impact is summarized as "of an order of magnitude of
  0.1%", while Tables 3–4 give 0.115–0.635 % for non-coincident interfaces.
- Typos: "gris cells" (Table 2), "transfert", "reflexion"; ref. [40] title "hoe cutting"; ref. [8]
  "Physics Revision B".

# Notation map

| Picard et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| substrate $\mathcal W$, patch $\mathcal V$ | $G_1$, $G_2$ | the patch has the higher priority; only two grids in all tests |
| $K_i$, $K'_i$, $\lvert K_i\rvert$ | $V_c$ (cells of $G_1$, $G_2$), $\lvert V_c\rvert$ | |
| $s_{ij}$, $\lvert s_{ij}\rvert$, $\mathbf n_{ij}$ | $f$, $S_f$, $\mathbf n_f$ | |
| ghost cells $\widetilde{\mathcal W}$, $\widetilde{\mathcal V}$ | $\mathcal R_1$, $\mathcal R_2$ | the paper's "ghost cells" are receptors, not boundary ghost points |
| sending cells $\mathcal W^s$, $\mathcal V^s$ | donor cells | all cells geometrically intersecting a receptor |
| $k_{GC}$ | $n_f$ | $=2$ |
| $\delta_{GC}$ | $d$ | minimum centre distance between the receptor sets of the two grids; **the registry $\delta$ is the Yin–Yang buffer angle** |
| $\delta_S=\delta_{GC}-\tfrac12(h^{\mathcal W}+h^{\mathcal V})$ | $d-\tfrac12(h_1+h_2)$ | $0$ for coincident interfaces |
| $h^{\mathcal W}$, $h^{\mathcal V}$ | $h_1$, $h_2$ | printed "measures", used as spacings |
| $\chi$, $\chi_i^{\mathcal V}$ | $\kappa_h$, $\kappa_{h,\mathbf i}$ ([registry](/notation.md) §9; global, local), as on [shock capturing](/methods/shock-capturing-on-overset-grids.md) | **the registry reserves $\chi$ for the solid indicator** |
| $\lvert\widetilde K_i\cap K'_j\rvert/\lvert\widetilde K_i\rvert$ | $\alpha_{\mathbf j}$ | sum to 1 when the receptor is fully covered |
| $\mathbf w_i$, $\mathbf v_i$, $\tilde{\mathbf w}_i$, $\tilde{\mathbf v}_i$ | $\mathbf q$ on $G_1$, $G_2$ and at receptors | |
| $\mathbf U$, $\mathbf F$, $\mathbf B$ | $\mathbf q$, $\mathbf F$, non-conservative coefficient | five-equation model, non-conservative form |
| $\mathbf Q=(\rho,u,v,w,p)^t$ | $\mathbf q_{\mathrm p}$ | |
| $\alpha_k$, $\rho_k$, $\gamma_k$ | phase volume fraction, density, ratio of specific heats | page-local; **$\alpha_k$ is not an interpolation weight** |
| $\Phi_i$, $K$ | limiter, compressivity constant ($0.75$) | page-local; $K$ is not a cell |
| $\varepsilon(\phi)$ | $\varepsilon_{\mathrm c}$ (relative, %) | |
| $N_{cells}$ | resolution parameter | test-specific meaning |
| $N$ (Fig. 2) | reconstruction order | **$N$ is reserved for the polynomial degree** |
| $\delta$, $D$ (§4.3) | bow-shock standoff, cylinder size | **$\delta$ clashes with the registry**; printed "radius" |

# Reference list

69 printed references, numbered [1]–[69]. All 69 are merged complete into the
[bibliography](/bibliography.md) with `citedby` picard-2021. Van Leer's two 1977 papers, refs. [47]
and [48], are `vanleer-1977` and `vanleer-1977-b`. Ref. [18], printed "LANL unclassified report
(1998) 96–3466", is the Ogen report `henshaw-1998`; ref. [16], Benek's 1986 grid-embedding report,
is `benek-1985-b`; Pärt-Enander and Sjögreen (ref. [56]) is `partenander-1994`; ref. [51] (printed
"Unpublished (2015)", with a ResearchGate DOI) is `solyga-2015`. Ref. [3] is printed "to appear" with a DOI. Ref. [40] prints a truncated DOI, which is omitted. Refs. [4], [63], [65] and [66] print
no volume.

# Pages created or updated

Chunk 2 (2026-11-02). This source is cited on:

- [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md)
- [Shock–cylinder interaction](/benchmarks/shock-cylinder-interaction.md)
- [Composite overlapping grid](/definitions/composite-overlapping-grid.md)
- [Domain connectivity and overset grid assembly](/definitions/domain-connectivity.md)
- [Explicit and implicit interpolation](/definitions/explicit-and-implicit-interpolation.md)
- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Adaptive mesh refinement on overlapping grids](/methods/amr-on-overset-grids.md)
- [Conservative overset interface](/methods/conservative-overset-interface.md)
- [Fluid–structure interaction on overlapping grids](/methods/fluid-structure-interaction-on-overset-grids.md)
- [Hole cutting](/methods/hole-cutting.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
- [Overlap optimization](/methods/overlap-optimization.md)
- [Shock capturing on overlapping grids](/methods/shock-capturing-on-overset-grids.md)
- [Interpolation order and overlap requirements](/results/interpolation-order-requirement.md)
- [Overture (and its grid generator Ogen)](/software/overture.md)
