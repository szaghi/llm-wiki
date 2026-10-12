---
type: Source
title: "Navas-Montilla & Murillo (2019) — Improved Riemann solvers for an accurate resolution of 1D and 2D shock profiles with application to hydraulic jumps"
description: "For the shallow-water equations with a bed source, explains the slowly moving shock anomaly by the curved Hugoniot locus of the captured intermediate state, removes the discharge spike with a source-corrected extrapolated flux in shock cells (exact steady discharge), and cures the carbuncle of the augmented Roe solver by adding dissipation only to the shear wave; first-order Godunov only."
resource: "doi:10.1016/j.jcp.2018.11.023"
source_kind: paper
authors: [Navas-Montilla A., Murillo J.]
year: 2019
venue: "J. Comput. Phys. 378:445-476"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2019-JCP-NavasMontilla-101016jjcp201811023.pdf"
tags: [riemann-solver, shock-instability, shallow-water, well-balanced]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper treats two "numerical shockwave anomalies" of the shallow-water
equations with a bed source, at hydraulic jumps: the slowly moving shock
anomaly and the carbuncle. It explains the first by the curved Hugoniot
locus of the captured intermediate state. It removes the discharge spike
with a "spike-reducing" flux, which extrapolates the cell-centred flux in
shock cells and corrects it with the source so that both generalized
Rankine–Hugoniot equilibria hold. It cures the carbuncle of the complete
augmented Roe solver (ARoe) by adding dissipation only to the shear
wave. All schemes are first-order Godunov finite volume, with no
reconstruction and no stability analysis. Merged into the
[slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md),
[numerical shock instability](/definitions/numerical-shock-instability.md),
[its cures](/methods/shock-instability-cures.md),
[well-balanced schemes](/properties/well-balanced.md) and the Riemann-solver page.

# Key claims

1. **Origin of the slowly moving shock anomaly** (§4.1, eqs. 43–47).
   * A captured shock is a three-state jump. The intermediate state lies
     on the Hugoniot locus, so it is an admissible weak solution. The
     locus is curved and non-monotone, so the intermediate discharge
     exceeds the constant discharge of the end states.
   * The anomaly is "always present with independence of the choice for
     the Riemann solver". Citing Zaide, it would vanish for linear
     Hugoniot curves.
2. **Refinement does not help** (§4.1.3). From $40\times50$ to
   $160\times200$ the spike amplitude depends only on the sub-cell shock
   position and the end states; refinement raises only its frequency.
   Numerical diffusion "barely helps" across transcritical shocks.
3. **2D** (§4.1.2). The spike runs along the bow shock. A shock that is
   not aligned with the grid sheds transverse waves when it jumps between
   cell columns. ARoe carries them away; HLLS damps them but perturbs the
   shock speed.
4. **Carbuncle** (§4.2). The mechanism is "still not clear". The paper's
   account: a curved shock appears as one-cell jumps that can move by two
   cells, triggering cross flow and a downstream recirculation. The
   complete ARoe triggers it; the incomplete two-wave HLLS does not, at
   the price of high shear diffusion (§4.2.1).
5. **Solvers** (§3).
   * ARoe is Roe with the bed source as a stationary wave. It is well
     balanced and has an entropy correction taken from earlier work.
   * HLLS is HLL plus the stationary source wave. It ignores the contact
     and coincides with ARoe on the 1D jump when Roe speeds are used.
6. **Spike-reducing flux** (§5.1, eqs. 50–57).
   * In shock cells, detected by a sign change of the Roe speed, the
     cell flux is replaced by an extrapolation from the two neighbours
     (after Zaide and Roe's "flux function A"), plus a correction built
     from a composite-trapezoid source integral.
   * It satisfies both generalized Rankine–Hugoniot equilibria and is
     consistent to $O(h^2)$ (App. A, under a linear-Hugoniot assumption).
   * In 2D it is applied direction by direction, on a detection band 3
     cells wide (§5.2).
7. **Shear-wave cures** (§5.3).
   * The first upwinds the shear flux with the ARoe star discharge, which
     makes the tangential momentum a passive scalar.
   * The second takes the shear flux from HLLS.
   * Either may act only in shock cells (§5.4). The authors recommend the
     first with the spike-reducing flux (§7).
8. **Residual weakness** (§6.1.1). Narrow spikes survive while the shock
   crosses a cell interface in a quasi-steady sweep.

**Tests** (all first order, shallow water):
* a 1D slowly moving hydraulic jump (900 cells);
* a 2D bow shock ahead of a cylinder, with a mesh study;
* a supercritical bow-shock carbuncle test ($\Delta x = 0.5$ m);
* a steady jump over a hump at seven sub-cell shock positions, where the
  spike-reducing flux gives the exact discharge 0.6 m²/s "with machine
  precision";
* a quasi-steady shock sweep;
* a Mach-stem reflection on a wedge (Froude 4.2, $400\times220$), where
  ARoe fails at the stem;
* grid and inflow perturbations;
* a cylinder over an irregular bed.

# Notation map

| Navas-Montilla & Murillo (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $W$ | $u$ | the paper's $W$ is conserved; registry $\mathbf W$ is primitive |
| $F$, $F_1$, $F_2$ | components of $\mathbf f$ | |
| $h$ (depth), $\Delta x$ | water depth (words), $h$ | registry $h$ is the grid spacing |
| $S$, $\bar S_{i+1/2}$ | $\mathbf s(u)$ and its integral over a face cell | $S$ collides with $S_{L,R}$ |
| $\tilde J$, $\tilde\lambda^m$, $\tilde e^m$ | Roe Jacobian; $\lambda^{(p)}$, $r^{(p)}$ at the Roe state | |
| $\alpha^m$, $\bar\beta^m$, $\gamma^m$ | wave, source and flux-jump strengths (words) | collide with $\alpha$, $\beta_k$, $\gamma$ |
| $\lambda^1$, $\lambda^2$ (HLLS) | $S_L$, $S_R$ | |
| $\check F_i$, $\hat F_i$ | extrapolated and corrected cell fluxes (words) | collide with $\hat f$ |
| $x_{S,i}$ | sub-cell shock position | same role as $\epsilon_{\mathrm{sh}}$ |
| $Fr$ | Froude number (words) | |

# Pages created or updated

* Created [Slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md), [Numerical shock instability](/definitions/numerical-shock-instability.md), [Cures for numerical shock instability](/methods/shock-instability-cures.md), [Well-balanced schemes](/properties/well-balanced.md), [Hypersonic blunt-body carbuncle test](/benchmarks/hypersonic-blunt-body.md) (shallow-water analogue).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (ARoe and HLLS).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2019-JCP-NavasMontilla-101016jjcp201811023.pdf`.
   * **Version.** The author manuscript (40 pages, line-numbered) from the
     Zaragoza Zaguan repository, with no arXiv id. Its page-1 footer
     reads "Preprint submitted to Computers & Fluids", but the content is
     the JCP paper.
   * **Identity.** doi:10.1016/j.jcp.2018.11.023, checked on Crossref:
     J. Comput. Phys. 378:445–476, February 2019, with 28 references.
   * **How it was read.** Text extraction, all sections. Eqs. 46, 50 and
     69–70 were checked on the page images.
   * **Inconsistencies recorded as printed.** The flat bed of §4.1.2
     against eq. 48. The last branch of eq. 71. "72 × 180" against
     80×200 in §6.4. The inflow ramp of §6.4.2.
   * **Reference list:** 28 entries.
