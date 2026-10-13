---
type: Source
title: "Barrio Sanchez, Almgren, Bell, Henry de Frahan & Zhang (2024) — A new re-redistribution scheme for weighted state redistribution with adaptive mesh refinement"
description: "Shows why cut-cell redistribution done level by level breaks conservation when the embedded boundary crosses a coarse–fine interface, and repairs it with a register built from the sparse matrix form of weighted state redistribution, merged with the reflux register and spread over uncovered coarse neighbours; conservation is observed to round-off, but tiny coarse cut cells at the interface still fail."
resource: "doi:10.1016/j.jcp.2024.112879"
source_kind: paper
authors: [Barrio Sanchez I., Almgren A.S., Bell J.B., Henry de Frahan M.T., Zhang W.]
year: 2024
venue: "J. Comput. Phys. 504:112879"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2024-JCP-BarrioSanchez-101016jjcp2024112879.pdf"
tags: [embedded-boundary, amr, conservation, boundary-treatment]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

With block-structured AMR and subcycling, Berger–Colella synchronization
averages fine data down and refluxes coarse–fine fluxes. Near an
embedded boundary each level also redistributes its small cut cells on
its own, which moves conserved quantities into covered coarse cells and
fine ghost cells, both outside the composite solution; and the
corrections land in cells that can be tiny. The paper builds a
re-redistribution register from the matrix form of weighted state
redistribution, merges it with the reflux register, and applies it at
synchronization. Merged into [state redistribution](/methods/state-redistribution.md).

# Key claims

1. **Scheme** (§§2–3, App. C): cut-cell finite volume with unsplit
   piecewise-linear Godunov (Colella 1990; Saltzman 1994) and a two-shock
   Riemann solver, or a method-of-lines predictor–corrector; weighted SRD
   (eqs. 6–13) with Barth–Jespersen-limited gradients.
2. **Matrix form** (§3.3): unit column sums make weighted SRD
   conservative; gradients do not change the total (asserted).
3. **The four leaks** (§§2.4, 3.4): coarse uncovered↔covered and fine
   valid↔ghost transfers; tiny receiving cells make direct corrections
   unstable.
4. **Register** (§3.4.1, eqs. 14–16): extensive contributions from the
   sparse matrix, coarse and fine parts, slope terms frozen and spread over
   the neighbourhood.
5. **Application** (§3.4.2): at synchronization with average-down and
   reflux; full cells take the correction directly, cut cells keep
   $\kappa_i$ of it and spread the rest over reachable 3×3×3 neighbours;
   one half per stage for the predictor–corrector (eq. 19).
6. **Evidence** (§4.1, Fig. 3): mass conserved to round-off with reflux
   and re-redistribution together, in 2D and 3D, Godunov and method of
   lines, weighted SRD and flux redistribution. No proof, no convergence
   order. Fails when an uncovered coarse cut cell at the interface is
   below a volume fraction of about $10^{-4}$.
7. **No moving boundaries**; neighbourhoods are recomputed at regrid only.

**Tests:** a tilted-cylinder channel for conservation (§4.1); Sod in a
channel rotated 30° with dynamic AMR crossing the walls
([Sod](/benchmarks/sod-shock-tube.md), §4.2); Mach 2.81
[shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md)
with partial refinement (§4.3); a PeleC compression-ignition engine, where
adaptive refinement of the boundary is 3–4× cheaper than refining all of
it (§4.4, Table 1).

# Notation map

| Barrio Sanchez et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Lambda_{i,j,k}$ | $\kappa_i$ | $\Lambda$ is the eigenvalue matrix |
| $V$, $V_{target}$, $\widehat V$ | $\vert I_i\vert$, $\tfrac12 h^d$, $\widehat{\mathcal V}_i$ | |
| $\alpha$, $\beta$ | $\eta^{\mathrm{self}}_i$, $\eta^{\mathrm{nb}}_i$ | |
| $A$ | $\mathsf W$ | |
| $\mathcal R$, $\delta R$, $\delta\mathbf R$ | words | register |
| $\ell$ | words (AMR level) | |

# Pages created or updated

* Contributed to [State redistribution](/methods/state-redistribution.md) (re-redistribution), [Cut-cell finite volume](/methods/cut-cell-finite-volume.md), [Shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md).
* Updated [High-order AMR](/methods/high-order-amr.md), [Sod shock tube](/benchmarks/sod-shock-tube.md), [Positivity preservation](/properties/positivity-preserving.md).
* Also cited on [Exact Riemann solver for the Euler equations](/methods/exact-riemann-solver.md) (created in batch 12).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2024-JCP-BarrioSanchez-101016jjcp2024112879.pdf`.
   * **Version.** arXiv:2309.06372v1 (12 September 2023), not the typeset
     article. The collection labelled it "barrio-2024"; the first author's
     surname is Barrio Sanchez.
   * **Identity.** doi:10.1016/j.jcp.2024.112879, checked on Crossref:
     J. Comput. Phys. 504:112879, May 2024.
   * **How it was read.** Text extraction, all sections; eqs. 6–19 checked
     on the page images.
   * **Recorded as printed.** The conclusions call §4.3 "shock reflection
     from a sphere"; the upstream pressure of §4.3 is typographically
     ambiguous.
   * **Reference list:** 38 entries (the published version has 39).
