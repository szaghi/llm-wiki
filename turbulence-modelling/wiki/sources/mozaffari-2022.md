---
type: Source
title: "Mozaffari et al. (2022) — Average-based mesh adaptation for hybrid RANS/LES simulation of complex flows"
description: "Proposes adaptive grid refinement for hybrid RANS/LES driven by a time-averaged Hessian criterion, so the mesh converges to a quasi-static topology; calibrated on an IDDES of a backward-facing step and applied with DDES-SST to a ship hull at drift and a delta wing."
resource: "doi:10.1016/j.compfluid.2021.105202"
source_kind: paper
authors: [Mozaffari S., Guilmineau E., Visonneau M., Wackers J.]
year: 2022
venue: "Comput. Fluids 232:105202"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Computers_amp_Fluids_Mozaffari_Average-based_mesh_adaptation_for_hybrid_RANSLES_simulation.pdf"
tags: [hybrid-rans-les, des, mesh-adaptation, separated-flow, rans]
timestamp: 2026-10-25T19:46:00Z
---

# Summary

Mozaffari et al. (2022) start from the grid dependence of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md): the cell size sets the
split between modelled and resolved turbulence, so every change of cell
size in space or time perturbs the turbulence. In a
[detached-eddy simulation](/methods/detached-eddy-simulation.md) of decaying
turbulence crossing a fine-to-coarse interface, the resolved kinetic energy
drops at once and the modelled energy compensates only partly and slowly.
Instantaneous adaptive refinement, which follows every eddy, triggers such
perturbations all the time and adds interpolation error.

The authors make the refinement criterion of the finite-volume solver
ISIS-CFD, an anisotropic metric built from the Hessians of pressure and
velocity, act on time-averaged quantities. The
[adapted mesh](/methods/mesh-adaptation.md) then converges to a quasi-static
topology on which the main flow features cross locally uniform cells. On an
IDDES of the Vogel–Eaton [backward-facing step](/benchmarks/backward-facing-step.md)
($Re_H=28{,}000$), averaging the instantaneous criterion (AC) is preferred
over the criterion of the averaged flow (CA): CA gives irregular meshes that
never become steady. Lowering the threshold drives the reattachment-length
error from 18.7% to 3.6% with 1.3 to 9.9 million cells, against 9.6% on a
fixed 9.3-million-cell mesh and 25% with instantaneous refinement. A sliding
window sized from the flow's characteristic frequencies, and refinement
boxes that make resolved content appear earlier, speed up convergence.

With DDES based on the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md),
the method reproduces a 163-million-cell hand-made mesh on the DTMB 5512
hull at 10° drift with 154 million cells, and it compares SST, SSG/LRR-$\omega$
and DDES-SST on a delta wing at 24°. The recommendations are a RANS
precursor, the RANS threshold, and a minimum cell size of a quarter of the
Taylor microscale, a resolution rule in the spirit of the
[grid-point requirements](/results/les-grid-point-requirements.md). Blended
upwind convection is the only [numerical-dissipation](/properties/numerical-dissipation.md)
setting reported.

# Version read

Author manuscript in the Elsevier template ("Preprint submitted to
Elsevier" on every page), preceded by a one-page highlights sheet; not the
typeset version of record. 28 PDF pages (27 numbered plus highlights), all
read; Eq. 1 and the exponents on printed p. 16 checked visually. No arXiv
or HAL stamp. Page 1 matches the metadata; no identity problem. Page
numbers on this page are the manuscript's printed numbers.

# Key claims

1. Any change of cell size perturbs hybrid RANS/LES turbulence: in a DES of decaying turbulence crossing a fine-to-coarse interface, resolved TKE drops abruptly, modelled TKE decays more slowly on the coarser mesh, but "the loss of resolved turbulence is never equal to the gain in modeled turbulence"; "a single change in mesh size causes a lasting perturbation of the turbulence" (§1, Fig. 1, from the thesis [23]). **Shown**
2. Refinement driven by time-averaged criteria gives meshes that "do not evolve rapidly in time"; for statistically steady flows "the grid adaptation converges to a static mesh" (§3). **Shown** (backward-facing step, Fig. 6)
3. Instantaneous refinement (AGR-100, every 2 time steps, $T_r=0.01$) on the step reaches about 20 million cells at times, ends with 6.6 million and gives $L_r/H=8.35$, 25% above the experimental 6.66, with perturbed $C_f$ (§4.1, Figs. 6a, 8, Table 2). **Shown**
4. Averaged criteria are smaller, so the threshold must fall from 0.01 to 0.0025 to keep a similar cell count (§4.2). **Stated**/**Shown**
5. Averaging the criterion (AC) converges to a constant mesh of 1.3 million cells, about half the CA mesh (2.4 million), which "never becomes steady" (§4.2, Fig. 6a, Table 2). **Shown**
6. CA meshes are irregular: the linear interpolation of the averaged solution onto refined cells has discontinuous derivatives at coarse-cell faces, so the second-derivative criterion is spuriously high there (§4.2, Fig. 9). **Shown** (explanation **Stated**)
7. Averaging the instantaneous criterion is "the most suitable choice", because the mesh must resolve the instantaneous flow at every instant, which the averaged flow (a thin mean shear layer against thick instantaneous vortices) does not represent (§3.3, §4.2, §6). **Stated**, supported by the mesh regularity shown
8. Averaging the criterion costs more than averaging the flow: it is computed every time step and stores six tensor components against four flow variables (§3.1). **Stated**
9. Lowering the threshold refines the AC mesh and converges the solution: $T_r=0.0025$, 1.3 million cells, 18.7% error; $0.0020$, 2.5 million, 5.1%; $0.0015$, 9.9 million, 3.6% (§4.3, Table 2, Fig. 11a). **Shown**
10. Even at the lowest threshold the Hessian criterion does not refine the forward recirculation zone (low velocities give small second derivatives), which may explain the overestimated $C_f$ near $X/H=2$ (§4.3, §4.5). **Shown** (cause **Stated**)
11. Spectra of the fine IDDES: Kelvin–Helmholtz $St=0.86$ and vortex pairing 0.43 at $X/H=0.52$; step mode 0.22 and shedding 0.11 at $X/H=6.67$; flapping 0.008; periods of about 500 (shedding) and 7000 (flapping) time steps (§4.4, Fig. 13). **Shown**
12. A sliding window of 1250 steps (2.5 shedding periods, AC50-25) converges the mesh faster, doubles the final cell count (2.5 against 1.3 million) and gives $L_r/H=7.7$ (15.6%); the whole-run AC@-25 is judged "not fully converged" (§4.4, Figs. 6b, 10d, 12e, Table 2). **Shown**
13. A window of one refinement interval (25 steps, AC01-25) made the cell count grow until the run "became too expensive to continue and was stopped manually" (§4.4). **Shown** (no numbers)
14. To average out a phenomenon "the window should span at least 4 to 10 of its characteristic periods"; for the step, 10–15 periods (5000–8000 steps) average out the shedding and leave the flapping visible (§4.4, §6). **Stated**
15. Refinement boxes on the initial mesh (recirculation zone plus shear layer, or shear layer only) give similar final meshes of about 2 million cells, $L_r/H=6.5$ (−2.5%) and 6.3 (−5.4%), and good $C_f$; faster generation of resolved content, not small recirculation-zone eddies, drives the improvement (§4.5, Fig. 15, Table 2). **Shown**
16. This supports "refining where the most intense flow features occur": RANS-derived Hessian criteria with averaging "make sense" for hybrid RANS/LES, and a converged RANS adapted solution can replace manual refinement boxes (§4.5). **Stated**
17. Toosi & Larsson [34] derive "an almost identical criterion for LES starting from a directional equidistribution of the turbulence", so the Hessian "probably remains a valid choice" for hybrid RANS/LES (§3.3). **Stated**
18. DTMB 5512 at 10° drift: RANS underestimates the vortex-core TKE "by a factor of 10 to 100"; DES shows vortex cores made of unsteady horseshoe-like vortices rotating around the core (§5.1, citing [36, 37, 45]). **Stated**
19. Average-based refinement with DDES-SST reproduces the 163-million-cell fixed-mesh DDES up to $x/L=0.4$ (end of its finest box) and follows the experimental trends everywhere, with good agreement at $x/L=1$ (§5.1, Figs. 18–19). **Shown**
20. Cost on the DTMB 5512: EARSM 163 million cells about 30,000 CPU h against adaptive 47 million about 16,000 h; DDES adaptive 154 million cells 160,000 h against fixed 163 million about 250,000 h (different processor counts; RANS precursors excluded) — "the adaptation probably saves some time, but not a lot" (§5.1). **Shown**
21. The DDES-SST mesh converges in 1.5 flow-through units, against about 5 units of main growth and 25 units of full convergence for the RANS mesh (§5.1, Figs. 22–23). **Shown**
22. A minimum cell size of $\lambda_T/4$ (0.6 mm on the DTMB 5512), with $\lambda_T$ the Taylor microscale, keeps the vortex core on a locally uniform, time-invariant mesh — "the meshing goal of the average-based refinement is met" (§5.1, Fig. 21; §6). **Shown**
23. Delta wing ($Re=2.17\times10^6$, $M=0.15$, $\alpha=24°$): converged meshes of 60 million ($k$-$\omega$ SST, instantaneous criterion), 68 million (SSG/LRR-$\omega$, average-based because its RANS solution is unsteady) and 77 million cells (DDES-SST); about 30,000 CPU h for RANS and 60,000 h for DES (§5.2). **Shown**
24. Unsteady RANS solutions at high angle of attack are called incorrect, "since according to the RANS velocity decomposition, with the right Reynolds stresses, the mean flow should be steady" (§5.2). **Stated**
25. On the delta wing, SST and DDES-SST predict forces and the experimental vortex features well; SSG/LRR-$\omega$ gives a smeared velocity field with too much TKE at 24°; DDES-SST overestimates the core velocity peaks and the TKE of the first vortex, with the maximum at the centre rather than on the shear layer (§5.2, Figs. 26–27). **Shown**
26. Average-based refinement loses fine detail on unsteady flows but gives smoother meshes that improve accuracy, so it suits RANS flows with some unsteadiness too; for steady flows instantaneous and average-based refinement are equivalent (§5.2). **Stated**/**Shown**
27. Hybrid RANS/LES runs can use the threshold of the corresponding RANS runs ($L/5$ to $L/20$): "If these produce an adequate RANS mesh, then the same settings applied to DDES-SST also provide a good mesh" (§6). **Stated** (from two cases)

## Refinement criterion as printed

Cells are refined until each cell dimension vector $\mathbf d_{i,j}$ satisfies
$\lVert C_i\mathbf d_{i,j}\rVert=T_r$ (Eq. 1), with $C$ a metric tensor field
and $T_r$ a global threshold. With $H(q)$ the Hessian of a variable $q$
(Eq. 2) and an error of order Hessian times cell size squared, equidistribution
gives $C=\lVert H(q)\rVert^{1/2}$ (Eq. 3), where $\lVert\cdot\rVert$ keeps the
eigenvectors and takes absolute eigenvalues. The pressure–velocity criterion
is $C_{\mathrm{FCH}}=\big(\max(\lVert H(p)\rVert,\rho U\lVert H(u)\rVert,\rho U\lVert H(v)\rVert,\rho U\lVert H(w)\rVert)\big)^{1/2}$
with $U$ the velocity magnitude (Eq. 4). In AC the tensor is averaged over
the whole run or a sliding window; in CA it is computed from averaged $p$ and
$\boldsymbol u$ before each refinement.

# Printed slips

- **Fine-mesh size.** §4.1 (p. 7): "the reference mesh contains $9.2\times10^6$ cells"; Table 2: "Fine 9.3" ($\times10^6$).
- **Skin friction (§4.1, p. 8).** Printed $C_f=\tau_w/(1/2\rho U_\infty)$, with the velocity not squared.
- **RANS TKE deficit.** "RANS simulations underestimate this TKE by a factor of 10 to 100" (§5.1, p. 16) against "the turbulence is underestimated by several orders of magnitude" (p. 18).
- **Model name.** "anisotropic EARSM turbulence model [8]" (p. 16) and "original EASM … adaptive EASM computation" (p. 17) for the same RANS runs.
- **Window on the DTMB 5512 (§5.1, p. 17).** A 250-step window with an eddy period of "about 80 time steps" is described as "this averaging period of about 4 periods"; $250/80\approx3.1$ *(compiler check, not in the sources)*.
- **Minimum cell on the delta wing (§5.2).** "minimum cell size for DDES-SST is 1mm, to correspond to the Taylor microscale of $\lambda_T=2.86$mm", while §6 recommends $\lambda_T/4$; $2.86/4=0.715$ mm *(compiler check, not in the sources)*.
- **Time of first refinement (§4.2).** "at time $T=0.15$" follows 2500 steps of non-dimensional $\Delta t=0.018$, i.e. 45 non-dimensional units *(compiler check, not in the sources)*; the unit of $T$ is not stated.
- **Typos.** Fig. 1 caption "fine-to-course"; Fig. 2 caption "Sliding widow"; Fig. 15 caption "AC@25B1", "AC@25B2" without hyphen.

# Notation map

| Mozaffari et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $C$, $C_i$, $C_{FCH}$ | (refinement metric tensor, its cell value, pressure–velocity Hessian criterion) | page-local; written $\mathcal K$ on [mesh adaptation](/methods/mesh-adaptation.md), where $\mathcal C$ is the mesh complexity |
| $\mathbf d_{i,j}$, $T_r$ | (cell dimension vectors, refinement threshold) | $T_r$ dimensionless on the step, a length ($L/5$, $L/20$) in §5 |
| $H(q)$ | (Hessian of $q$) | **collision** with the step height $H$ |
| $\lVert\cdot\rVert$ (matrix) | (absolute-eigenvalue map) | not a norm |
| $n=1/2$ | (equidistribution exponent) | |
| $p$, $u,v,w$, $U$ | $p$, $u,v,w$, (velocity magnitude) | instantaneous or time-averaged per CA/AC |
| "averaged" | (running time average, whole run or sliding window) | no averaging operator printed |
| $H$, $L_r$ | (step height 0.038 m, reattachment length) | |
| $Re$ | $Re_H$ (step), $Re_L$ (hull length, wing chord) | |
| $St_h=fH/U_\infty$ | $St$ | on the step height |
| $\Delta x^+$, $\Delta z^+$, $y^+$ | $\Delta x^+$, $\Delta z^+$, $y^+$ | |
| $C_f$ | $C_f$ | printed without the square (see Printed slips) |
| $\lambda_T$ | $\lambda$ | Taylor microscale, estimated, no formula printed |
| $Q^*$ | (non-dimensional second invariant of the velocity gradient) | |
| $k$, TKE | $k$ | modelled, resolved and total distinguished in Fig. 1 |
| $L$, $V$, $Fn$, $tV/L$ | (hull length or wing chord, ship speed, Froude number, time unit) | |
| $\alpha$ | (angle of attack) | **collision** with the registry's DG blending factor |

# Reference list

46 printed references in Elsevier numbered style (alphabetical), most with
DOIs, all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year works take suffixes in printed order (Balan et al. 2020a, 2020b;
Mozaffari 2020, the PhD thesis, and 2020b, the DLES XII chapter). Two AIAA
papers (Balan et al. 2020b, Frazza et al. 2019) print only a DOI. The DOI
printed for ref. [8], 10.1007/s10773-003-0153-8, resolves on Crossref to
Duvigneau & Visonneau (2003), J. Mar. Sci. Technol., the cited work. The
fourth author of ref. [45] is printed "F., S."; Park et al. print "pp.
11–39" with a DOI ending in 2020-1139. No printed duplicates or
unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunk 5. This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
