---
type: Source
title: "Pakmor, Guillet, Bieri, Pfrommer, Springel & Teyssier (2026) — A comparison of numerical schemes for driven subsonic MHD turbulence"
description: "Preprint comparing CT (Athena++, Ramses), Powell and Dedner (Arepo, Arepo-dg) on driven subsonic small-scale-dynamo boxes: no systematic advantage for exact divergence, differences tracking numerical dissipation, and an unstable moving-mesh vector-potential CT."
resource: "doi:10.48550/arXiv.2607.06660"
source_kind: paper
authors: [Pakmor R., Guillet T., Bieri R., Pfrommer C., Springel V., Teyssier R.]
year: 2026
venue: "arXiv:2607.06660 (preprint, MNRAS style; not peer-reviewed)"
local_file: "~/papers/mosaic/div-free-amr/2026-arXiv-Pakmor-1048550arXiv260706660.pdf"
tags: [comparison, turbulence, small-scale-dynamo, constrained-transport, eight-wave, glm, vector-potential, moving-mesh]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper is a controlled code comparison. Driven, subsonic
($\mathcal{M} \approx 0.2$), nearly isothermal turbulence in a periodic box
amplifies a weak uniform seed field by small-scale dynamo action. All
dissipation is numerical. It runs four codes and six schemes at $32^3$ to
$256^3$ with identical stochastic solenoidal driving and one analysis
pipeline:
* **Arepo**, a moving Voronoi mesh: Powell and Dedner;
* **Arepo-dg**, second-order DG on a fixed Cartesian grid: Powell with a
  locally divergence-free basis, and Dedner;
* **Athena++**: CT with an upwind four-state EMF, PPM and characteristic
  limiting;
* **Ramses**: CT with a 2D HLLD EMF and linear reconstruction.

The headline finding: for this setup, exact-divergence CT has no
systematic advantage over the cleaning schemes. The residual differences
track numerical dissipation.

**Status.** The file is the arXiv v1 preprint (7 July 2026). DataCite
confirms the arXiv DOI. No journal version was found on Crossref, so every
claim from it is marked "preprint" on concept pages.

# Key claims

1. **Every scheme shows a dynamo** (§3). At sufficient resolution all six
   amplify exponentially to saturation.
   * Saturation agrees within a factor of 2 at $64^3$ and above.
   * The kinematic growth rate rises with resolution slightly faster than
     $\sqrt N$ for every scheme, with different normalizations.
2. **The divergence treatment sets an effective resistivity** (§§3, 6.2).
   With the hydrodynamics fixed, Powell grows about 3 times faster than
   Dedner in Arepo and about 2 times faster in DG. The field is
   dynamically irrelevant in that phase, so the authors attribute the gap
   to resistivity.
   * Powell is up to 3–4 times faster than Ramses-CT and up to 2 times
     faster than Athena-CT.
   * Arepo-Powell at $128^3$ matches Ramses-CT at $256^3$ in its kinematic
     magnetic spectrum (Fig. 11).
3. **Within CT, reconstruction matters more than the constraint**
   (§6.2, Fig. 13).
   * With linear reconstruction and primitive limiting, Athena-CT grows like
     Ramses-CT, the remainder plausibly from the EMF construction.
   * Characteristic-variable limiting raises the growth rate more than PPM
     does. Athena-CT is about 2 times faster than Ramses-CT at $64^3$ and
     40% faster at $256^3$.
4. **No split by divergence class** (§§4–5, 6.2, 7). Field-structure
   wavenumbers, histograms of $B$, $J^2$ and curvature, the $B$–$K$
   relation and the spectra (Kazantsev $k^{3/2}$ at large scales) do not
   separate the exact schemes from the cleaned ones.
   * Athena-CT has larger $k_\parallel$ and a tail at high field and high
     curvature.
   * Arepo-Dedner lacks the largest currents and curvatures.
   * The authors attribute both to scheme details other than the
     divergence treatment.
5. **Arepo-CT is unstable** (§6.3). The vector-potential CT of Mocz et al.
   (2016) is exact on Delaunay tetrahedra, yet it develops artifacts at
   $128^3$ and clear instability at $256^3$. The diagnosis:
   * the potential is non-conservative;
   * averaging does not commute with the curl;
   * Delaunay flips make the reconstructed field discontinuous;
   * the cell-centred EMF source is not upwinded;
   * the formulation is not Galilean-invariant.

   The authors advise against production use and say a stable moving-mesh
   CT is still open.
6. **Implementation details** (§2.1). Arepo-Powell computes the divergence
   as a face Gauss sum and gives up machine-precision momentum
   conservation. The Dedner parameters are $c_h$ equal to the maximum fast
   speed with $\tau = 2r_{\mathrm{cell}}/c_h$ (Arepo), and $1.05$ times the
   maximum signal speed with $c_r = 0.18$ (DG; dimensional, so not
   portable).
7. **A measurement caveat** (§2.2). Field gradients are recomputed in post-
   processing with Arepo's operator, so the analysed CT fields are not
   discretely divergence-free on that operator.
8. **Cost** (§7). At comparable resolution the fixed-grid CT codes run more
   than an order of magnitude faster than Arepo and Arepo-dg. Athena-CT at
   $256^3$ (growth rate 0.94) costs about two thirds of Arepo-Powell at
   $128^3$ (1.18).
9. **Scope** (§7). Idealized, subsonic, purely numerical dissipation, and no
   AMR (refinement was disabled in every code). Extensions to supersonic
   turbulence and explicit viscosity and resistivity are proposed.

# Notation map

| Pakmor et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Psi$ (Dedner scalar) | $\psi_h$ | |
| $c_h$ | $c_h$ | |
| $\tau$, $c_r$ | damping time and constant | registry $c_p$ via $\tau = c_p^2/c_h^2$ in the mixed GLM |
| $\boldsymbol{Q}_i = \int_{V_i}\boldsymbol{A}\,dV$ | cell-averaged potential | not the edge $A_h \in V_h^1$ |
| $\Phi_B = \oint \boldsymbol{A}\cdot d\boldsymbol{l}$ | face flux from the potential | on Delaunay faces |
| "cell-centred divergence" (Ramses) | $D_h^{\mathrm{f}} B_h$ | face-flux sum over a cell |
| $\Gamma$ | kinematic growth rate | no registry symbol |

# Pages created or updated

* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md): cleaning as effective resistivity in turbulence.
* Updated [Eight-wave formulation](/methods/eight-wave.md): the lowest-dissipation scheme in the comparison, and its moving-mesh and DG forms.
* Updated [Vector-potential evolution](/methods/vector-potential-evolution.md): the Arepo-CT instability and its diagnosis.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): a regime where the constraint class made no systematic difference.

# Citations

1. `~/papers/mosaic/div-free-amr/2026-arXiv-Pakmor-1048550arXiv260706660.pdf` (doi:10.48550/arXiv.2607.06660): text extraction, all pages including the reference list (48 entries). Figures were read from their captions, axis text and Table 1 only.
