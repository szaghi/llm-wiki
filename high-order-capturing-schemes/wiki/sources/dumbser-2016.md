---
type: Source
title: "Dumbser & Balsara (2016) — A new efficient formulation of the HLLEM Riemann solver for general conservative and non-conservative hyperbolic systems"
description: "Generalizes Einfeldt's HLLEM to any conservative or path-conservative hyperbolic system: a linear sub-structure along chosen intermediate fields subtracts an anti-diffusive term with diagonal weight derived from Einfeldt's stability condition (alias HLLI); one eigen-decomposition per face, complete when all intermediate fields are included, exactly well balanced for shallow water; tested in 1D at second order on eight systems."
resource: "doi:10.1016/j.jcp.2015.10.014"
source_kind: paper
authors: [Dumbser M., Balsara D.S.]
year: 2016
venue: "J. Comput. Phys. 304:275-319"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2016-JCP-Dumbser-101016jjcp201510014.pdf"
tags: [riemann-solver, hllem, path-conservative, well-balanced]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper rederives HLL in the similarity variable and builds a
path-conservative HLL for systems with non-conservative products. Its HLL
state is implicit and found by Picard or quasi-Newton iteration. It then
extends Einfeldt's HLLEM to this setting and to general nonlinear systems.
The HLL state varies linearly along chosen intermediate characteristic
fields, which subtracts an anti-diffusive term from the HLL flux. Einfeldt's
scalar weight becomes a diagonal matrix derived from Einfeldt's stability
condition. Only the intermediate eigenstructure is needed, once per face.
The solver "could alternatively be called the HLLI Riemann solver". All
tests are 1D, second-order TVD. Merged into the new
[HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md) and
[well-balanced schemes](/properties/well-balanced.md) pages, the
Riemann-solver page and three benchmarks.

# Key claims

1. **Name** (abstract, §4). The paper says HLLEM throughout. "HLLI"
   appears twice, as an alternative name, with "I" for the intermediate
   fields. "LLFI" does not occur.
2. **Speeds** (eq. 5). $S_L$ and $S_R$ are clipped at zero, using
   eigenvalues at $u^-$, $u^+$ and the mean state.
3. **Path-conservative HLL state** (§2.1, eqs. 8–20). Integrating along the
   two segments through the HLL state makes that state implicit, and
   Picard or quasi-Newton iterations converge "very rapidly". For
   conservation laws the classical closed form needs no iteration.
4. **HLLEM flux** (§2.2, eqs. 26–30, from the page images): the HLL flux
   minus $\frac{S_L S_R}{S_R - S_L}\sum_p\delta_p r^{(p)}\ell^{(p)}(u^+ - u^-)$
   over the intermediate fields. A flattener between 0 (HLL) and 1 scales
   it.
5. **Anti-diffusion weight** (eq. 29, App. B):
   $\delta_p = 1 - \min(\lambda^{(p)},0)/S_L - \max(\lambda^{(p)},0)/S_R$.
   It is derived as the upper bound from Einfeldt's condition that the
   viscosity-matrix eigenvalues dominate $\vert\lambda^{(p)}\vert$ at the
   Roe state. At the bound the intermediate fields get Roe-like
   dissipation. For the Euler contact it reduces to Einfeldt's scalar.
6. **Completeness** (§2.3). Including all intermediate fields, genuinely
   nonlinear ones too, makes the solver complete. This is done for MHD and
   relativistic MHD, including the slow waves.
7. **Resonance** (§2.2). Where eigenvectors are incomplete, the
   anti-diffusion is dropped, "a very crude procedure".
8. **Asserted properties.** It inherits positivity and entropy enforcement
   from HLL; this is asserted, not proved. It needs no entropy fix and
   shows no sonic glitch (abstract, §§1, 3.6.1). It "outperforms the DOT
   RS by a wide margin", with no timings given (§4).
9. **Exact C-property for shallow water** (§3.1.1, eqs. 39–45). At lake at
   rest, zero eigenvalues give $\delta_p = 1$ and the fluctuations vanish
   for any topography. The velocity error is $1.1\times10^{-15}$ in double
   and $3.7\times10^{-31}$ in quadruple precision (Table 1).
10. **High order** (§4, one sentence). Freezing the speeds and the viscosity
    matrix per face would allow a quadrature-free ADER-WENO formulation.
    The remark cites Dumbser, Käser, Titarev & Toro (2007). It is not
    demonstrated.

**Tests** (§3; 1D, minmod TVD with a half-step predictor):
* single-layer shallow water (lake at rest; RP0–RP4, with a dry bed);
* two-layer shallow water;
* Pitman–Le debris flow;
* Baer–Nunziato, where the flattener had to be 0.97 on RP3–RP6;
* ideal MHD with GLM, with Brio–Wu data at $\gamma = 5/3$;
* Euler, Toro's RP0–RP6, including the modified Sod and the 1-2-3 double
  rarefaction;
* n-heptane with a real-gas equation of state across a phase transition,
  where RP-H3 failed with the generalized Osher solver;
* Godunov–Romenski elasticity;
* relativistic MHD.

There is no multidimensional test and no shock-instability test.

# Notation map

| Dumbser & Balsara (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $Q$; $Q_L$, $Q_R$ | $u$; $u^-$, $u^+$ | |
| $s_L$, $s_R$ | $S_L$, $S_R$ | clipped at 0 |
| $Q_*$ | $u^{\mathrm{HLL}}_*$ | |
| $R_*$, $L_*$, $\Lambda_*$ | $r^{(p)}$, $\ell^{(p)}$, $\lambda^{(p)}$ for $p \in \mathcal I$ | |
| $\delta_*$ (diagonal) | $\delta_p$ | |
| $\bar Q$ | $\tfrac12(u^- + u^+)$ | the bar would read as a cell average |
| $\varphi$ (flattener) | words | inverted sense against the PPM $\phi_i$ |
| $B(Q)$ | non-conservative product (words) | bold $\mathbf B$ is the magnetic field |
| $\Theta$ | $\Theta_{i+1/2}$ | |
| $D^\pm$ | fluctuations (words) | |
| $\psi$ (path); $\psi$, $c_h$ (GLM) | words; $\psi_{\mathrm{GLM}}$, $c_h$ | |

# Pages created or updated

* Created [HLLEM (HLLI) Riemann solver](/methods/hllem-riemann-solver.md), [Well-balanced schemes](/properties/well-balanced.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (the HLLI attribution and the LLFI caveat), [Sod shock tube](/benchmarks/sod-shock-tube.md), [Double rarefaction](/benchmarks/double-rarefaction.md), [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md).
* Updated [Notation registry](/notation.md): $\delta_p$, $\mathcal I$, $\Theta_{i+1/2}$, $u^{\mathrm{HLL}}_*$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-JCP-Dumbser-101016jjcp201510014.pdf`.
   * **Version.** An Elsevier-licensed author manuscript (dated 7 October
     2015, 54 pages) from the Trento IRIS repository.
   * **Why it is the revised manuscript.** The resonance paragraph of
     §2.2 is highlighted in blue, and the acknowledgments thank the
     referees for added test cases.
   * **Identity.** doi:10.1016/j.jcp.2015.10.014, checked on Crossref:
     J. Comput. Phys. 304:275–319, January 2016, with 96 references.
   * **How it was read.** Text extraction, all sections and Appendices
     A–C. Eqs. 1–5 and 26–34 and Table 6 were checked on the page images.
   * **Not reproduced.** The system-specific eigenvectors (eqs. 38, 48,
     54, 61–63, 69, 74, 77–82) are garbled in the text layer.
   * **Reference list:** 96 entries.
