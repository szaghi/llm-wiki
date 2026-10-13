---
type: Source
title: "Giuliani, Almgren, Bell, Berger, Henry de Frahan & Rangarajan (2022) — A weighted state redistribution algorithm for embedded boundary grids"
description: "Extends state redistribution to 3D embedded-boundary grids in AMReX and introduces a weighted variant in which a small cell keeps a share of its own provisional state, so redistribution switches on smoothly; any redistribution matrix with unit column sums is conservative; second order in the volume and about 1.4 on the boundary, run in PeleC and MFIX-Exa at about 2% of the cost."
resource: "doi:10.1016/j.jcp.2022.111305"
source_kind: paper
authors: [Giuliani A., Almgren A.S., Bell J.B., Berger M.J., Henry de Frahan M.T., Rangarajan D.]
year: 2022
venue: "J. Comput. Phys. 464:111305"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2022-JCP-Giuliani-101016jjcp2022111305.pdf"
tags: [embedded-boundary, boundary-treatment, conservation, amr]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper carries Berger and Giuliani's state redistribution (SRD) to 3D
embedded-boundary grids in the AMReX framework and modifies its weights.
In weighted SRD a cut cell just below the half-cell threshold keeps most
of its own provisional state, so the scheme no longer jumps when a volume
fraction crosses 0.5. A matrix form shows that any redistribution with
unit column sums is conservative. Tests range from a ramp and the
supersonic vortex to a reacting piston-bowl injection (PeleC) and a
fluidized-bed gas flow (MFIX-Exa). Merged into
[state redistribution](/methods/state-redistribution.md).

# Key claims

1. **Geometry** (§§2.1–2.2): AMReX EB data (volume and area fractions,
   centroids, wall normal); one EB face per cell; split and multivalued
   cells unsupported.
2. **3D SRD** (§2.3, eqs. 1–6) as in the 2D original; neighbourhoods
   within 3×3×3; the slope stencil grows to 5×3×3 or drops to first
   order; SRD is also applied to the initial data. Diffusion is
   stabilized the same way (Remark, eq. 7).
3. **Weighted SRD** (§3.1, eqs. 8–13): same neighbourhoods, new weights;
   "may have some different stability properties", with no bound given.
4. **Conservation criterion** (§3.1): redistribution matrix with unit
   column sums; slopes do not change the total.
5. **Monotonicity**: "None of the algorithms guarantee monotonicity";
   on a ramp flux redistribution over- and undershoots, both SRD variants
   do not (§3.2, Fig. 4).
6. **Smooth activation** (Fig. 5): a $10^{-7}$ shift of a 45° ramp
   changes original SRD by 0.132 and weighted SRD by about $10^{-8}$.
7. **Accuracy** (§3.2, Fig. 6b): second order in the volume, about 1.4 on
   the boundary; weighted reduces centred-merging errors 2–3×.
8. **AMR** (§4): the coarse–fine boundary may not cross a cut cell, so
   SRD runs one level at a time; no refluxing across levels is discussed.
9. **Production** (§§5–6): PeleC (characteristic MUSCL, two-shock Riemann
   solver, predictor–corrector) and incompressible codes; SRD costs at
   most about 2 %; flux redistribution produced mass fractions outside
   $[0, 1]$ in the reacting run.

# Notation map

| Giuliani et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $V_{i,j,k}$, $V_{target}$ | $\vert I_i\vert$, $\tfrac12 h^d$ | |
| $\widehat U$, $\widehat Q$, $\widehat q$ | $u^{\mathrm{pr}}$, $\bar u^{\mathcal N}$, $q^{\mathcal N}$ | |
| $M$ | $\mathcal N_i$ | |
| $M^-$, $W$, $W^-$ | words | |
| $N$ | $N^{\mathrm{ov}}_i$ | |
| $\alpha_{i,j,k}$, $\beta_{i,j,k}$ | $\eta^{\mathrm{self}}_i$, $\eta^{\mathrm{nb}}_i$ | collide with $\alpha$, $\beta_k$ |
| $A$ | $\mathsf W$ | $A$ is the flux Jacobian |
| $e$ | $\mathbf 1$ | |

# Pages created or updated

* Contributed to [State redistribution](/methods/state-redistribution.md) (weighted variant), [Cut-cell finite volume](/methods/cut-cell-finite-volume.md), [Supersonic vortex](/benchmarks/supersonic-vortex-annulus.md).
* Updated [High-order AMR](/methods/high-order-amr.md), [Positivity preservation](/properties/positivity-preserving.md).
* Updated [Notation registry](/notation.md): $\eta^{\mathrm{self}}_i$, $\eta^{\mathrm{nb}}_i$, $\mathsf W$.
* Also cited on [Exact Riemann solver for the Euler equations](/methods/exact-riemann-solver.md) (created in batch 12).
* Also cited on [AMReX and PeleC](/software/amrex.md) (created 2026-10-13).
* Also cited on [Flux redistribution for small cut cells](/methods/flux-redistribution.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2022-JCP-Giuliani-101016jjcp2022111305.pdf`.
   * **Version.** arXiv:2112.12360v2 (11 May 2022), not the typeset
     article.
   * **Identity.** doi:10.1016/j.jcp.2022.111305, checked on Crossref:
     J. Comput. Phys. 464:111305, September 2022.
   * **How it was read.** Text extraction, all sections; eqs. 1–13 and the
     printed matrix checked on the page images.
   * **Recorded as printed.** Eq. 13 omits the evaluation point of the
     cell's own reconstruction; eq. 8 sums unweighted volumes while eqs.
     10–13 weight by overlap counts.
   * **Reference list:** 18 entries for 17 works (the AMReX paper is
     printed twice).
