---
type: Source
title: "Kleine, Ritzerfeld & Grönig (1995) — Shock wave diffraction: new aspects of an old problem"
description: "Shock-tube experiments (nitrogen, M_s 1.05–3.0) and a second-order Godunov-type Euler run (Colella–Glaz, superbee, Roe, Strang splitting) of a planar shock diffracting at a sharp 90° corner, focused on the regime below M_s^* ≈ 2.07; density contours agree visually with interferometry, an extra shock parallel to the terminator appears only in experiment, and a nozzle-analogy criterion bounds shock-free supersonic pockets."
resource: "doi:10.1007/978-3-642-79532-9_18"
source_kind: paper
authors: [Kleine H., Ritzerfeld E., Grönig H.]
year: 1995
venue: "Shock Waves @ Marseille IV (Springer), pp. 117–122"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1995-ShockWaves-Kleine-101007978-3-642-79532-9_18.pdf"
tags: [euler, 2d, godunov, tvd, riemann-solver, mach-reflection, experiment]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A six-page conference paper combining shock-tube experiments with a
second-order Euler computation of a planar shock diffracting around a
sharp 90° convex corner in nitrogen. It concentrates on the transition
regime $1.3 < M_s < M_s^*$, with $M_s^* \approx 2.07$ for
$\gamma = 7/5$: the flow behind the incident shock is still subsonic in
the laboratory frame, yet secondary shock systems develop. The authors
catalogue the flow elements as functions of $M_s$ (terminator, second
shock, recompression shock, shocks on the vortex periphery, the density
minimum inside the slipstream), compare numerical density and
density-gradient contours with interferograms and colour schlieren
records, report one shock seen only in experiment, and propose a
nozzle-analogy criterion for shock-free supersonic pockets behind the
diffracting shock. It is the experimental and physical background of the
[shock-diffraction benchmark](/benchmarks/shock-diffraction.md) geometry.

# Key claims

1. **Regimes** (§1, Fig. 1). The flow pattern is well understood when
   the post-shock flow is supersonic, $M_s > M_s^* \approx 2.07$, and the
   corner angle exceeds 75°. The transition regime $1.3 < M_s < M_s^*$ is
   little studied (Skews 1967 is the main reference). Fig. 1a is labelled
   $1.4 < M_s < M_s^*$, Fig. 1b $M_s \ge M_s^*$.
2. **Corner-angle independence** (§1, citing Skews 1967). The flow
   separates for corner angles above 20°; above 75° the pattern does not
   depend on the angle, so $M_s$ is the only parameter at fixed $\gamma$;
   changing the gas does not alter the pattern qualitatively. Above
   $M_s^*$ the pattern depends only mildly on $M_s$ (a shock bulge near the
   wall, then a reflection pattern as $M_s$ grows).
3. **Self-similarity** (§3). The Euler equations have no characteristic
   length, so the pattern is self-similar about the corner. The mean free
   path (small scales), cumulative viscous effects (large scales) and, in
   the computation, the finite cell size break it, so experiment and
   computation are only approximately self-similar; numerically the effect
   is strongest at early times.
4. **Model** (§3). Reynolds number behind the incident shock up to
   $10^5$, pressure below 0.5 MPa, temperature below 800 K, so nitrogen is
   treated as a non-reacting perfect gas with the 2D time-dependent Euler
   equations.
5. **Scheme** (§3, steps 1–4). A second-order Godunov-type scheme after
   Colella & Glaz (1985): (1) piecewise-linear reconstruction of the
   primitive variables $(\rho, p, \mathbf v)$ with Roe's superbee limiter
   (TVD); (2) left and right interface states at the half time level from
   the characteristic form; (3) fluxes from Roe's approximate Riemann
   solver; (4) a conservative update. Extended to 2D by Strang splitting,
   "preserving second order accuracy in space and time" (p. 120).
   Equally spaced Cartesian grid aligned with the corner walls,
   inflow/outflow or reflecting-wall boundaries, vectorized on an IBM 3090.
   The grid size is not stated ("high-resolution" only).
6. **Agreement** (§4, Figs. 2a–b, 4, 5). Numerical density and
   density-gradient contours "coincide almost perfectly in all regions
   where the Euler equations can be expected to give correct results";
   the vortex structure is represented "extraordinarily well"; the
   secondary shock systems appear in both. No quantitative error measure
   is given.
7. **Wavelets at $M_s = 1.45$** (§4). The post-shock flow is subsonic,
   yet wavelets with a terminator, a second shock and a slipstream
   triangle appear, repeated with shrinking size; the simulation shows at
   most two such systems, the experiment more.
8. **$M_s = 1.6$** (§4). The wavelets merge into an almost centred
   expansion fan with a terminator, and a second shock runs from the end of
   the terminator to the slipstream, where it apparently reflects; the
   computation matches their location and extent. A further shock almost
   parallel to the terminator, reaching the second shock, is seen in the
   experiment but not in this or other simulations (Hillier 1991); the
   authors have "no plausible explanation".
9. **Vortex-periphery shocks** (§4). Kinks of the outer spiral on the
   right side of the vortex grow with $M_s$ and are more pronounced in the
   computation, which the authors attribute to the missing friction near
   the slipstream. At $M_s = 1.6$ the first kink is a shock into the vortex
   core that later merges with the second shock and destroys the circular
   vortex; above $M_s^*$ a distorted remnant of the core sits at the lower
   end of the second shock. A recompression shock on the wall side of the
   vortex is first visible at $M_s = 1.45$ and becomes an almost straight
   shock normal to the wall above $M_s^*$.
10. **Slipstream** (§4). It is not a narrow discontinuity (Skews 1967);
    every record shows a local density minimum inside it.
11. **Shock-free supersonic pockets** (§4, Eq. 1, Fig. 6). The computation
    shows local supersonic regions even for $M_s < 1.4$, with no secondary
    shocks. A nozzle analogy gives the criterion
    $$\frac{p_{0,2}}{p_1} \ge \left(\frac{\gamma+1}{2}\right)^{\frac{\gamma}{\gamma-1}} = 1.893 \quad (\gamma = 7/5),$$
    with $p_{0,2}$ the total pressure behind the incident shock before
    diffraction and $p_1$ the static pressure ahead of it, printed as
    satisfied for $M_s \ge 1.31$; the computation shows supersonic regions
    for $M_s \ge 1.33$. The authors stress that a simulation alone is no
    proof and leave the question open.

# Tests

**Experiment** (§2). Shock tube of 54.5 mm × 54.5 mm square cross-section,
test gas nitrogen, $M_s$ from 1.05 to 3.0, measured to better than 1%
because the pattern is sensitive to $M_s$, especially for
$1.4 < M_s < 1.7$. The model is a sharp 90° convex corner (a
backward-facing step from the tube wall). Driver gas, initial pressures
and model dimensions are not stated. Diagnostics:
* shadowgraphs (Fig. 3: $M_s$ = 1.45, 1.58, 1.84, 2.93);
* 1D colour schlieren (gradient magnitude) and 2D colour schlieren
  (gradient direction) (Fig. 2a: $M_s = 1.60$, 1D, horizontal cutoff;
  Fig. 2c: $M_s = 1.58$, 2D; Fig. 2d: $M_s = 1.83$, 2D);
* holographic reference-beam interferometry at infinite fringe width,
  1:1 image holograms (Fig. 4: $M_s$ = 1.34, 1.78) and transmission
  holograms for 3D records.

The records are qualitative wave patterns and isopycnics. No triple-point
trajectory, vortex position or pressure history is tabulated, so the data
can score a simulation only by comparison with the figures.

**Simulation** (§§3–4). 2D Euler, $\gamma = 7/5$, the scheme of claim 5.
Comparisons:
* Fig. 2a: numerical density-gradient contours over the 1D schlieren
  record, $M_s = 1.60$;
* Fig. 2b: numerical density contours over reconstructed holographic
  isopycnics, $M_s = 1.58$;
* Fig. 5: numerical density contours at $M_s$ = 1.35 and 1.80, against the
  Fig. 4 interferograms at 1.34 and 1.78;
* Fig. 6: sonic-line contours ($\mathrm{Ma} \ge 1$) at $M_s$ = 1.35, 1.58,
  1.80.

Agreement is visual (claim 6). Discrepancies: the terminator-parallel
shock (experiment only), fewer wavelet systems and stronger vortex kinks
in the computation.

# Notation map

| Kleine et al. (1995) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M_S$ | $M_s$ | shock Mach number |
| $M_S^*$ | $M_s^*$ | sonic post-shock flow, $\approx 2.07$ for $\gamma = 1.4$ |
| $\widehat{M_S}$ | words | threshold of Eq. 1, printed 1.31 |
| $\delta$ (corner angle) | words | bare $\delta$ is taken by difference operators |
| $\rho$, $p$, $u$, $v$ | $\rho$, $p$, $\mathbf v$ | |
| $p_{20}$, $p_1$ | $p_{0,2}$, $p_1$ | used on this page only, defined inline |
| flow Mach number (Fig. 6) | $\mathrm{Ma}$ | distinct from $M_s$ |

# Pages created or updated

* Updated [Shock diffraction at a backward-facing corner](/benchmarks/shock-diffraction.md) (experimental background of the 90° corner, regimes, the Euler comparison, the Eq. 1 threshold).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1995-ShockWaves-Kleine-101007978-3-642-79532-9_18.pdf`.
   * **Version.** The publisher scan (6 pages) with an Acrobat Paper
     Capture OCR layer.
   * **Identity.** doi:10.1007/978-3-642-79532-9_18, checked on Crossref:
     book chapter, *Shock Waves @ Marseille IV* (eds. R. Brun,
     L. Z. Dumitrescu, from the page-1 footer; Crossref has no editor
     field), Springer, 1995, pp. 117–122, authors Kleine, Ritzerfeld,
     Grönig (Stoßwellenlabor, RWTH Aachen). These are the proceedings of
     the 19th ISSW (Marseille, 1993): the paper calls the 18th ISSW "the
     last ISSW" and cites Hillier (1993) as "These Proceedings".
   * **How it was read.** The OCR text layer; page 1 and Eq. 1 checked on
     page images (the OCR renders $\gamma$ as "1", $M_S^*$ as "M~" and
     "≥" as "2:").
   * **Recorded as printed.** Eq. 1 is printed as satisfied for
     $M_s \ge 1.31$. A reader check with the normal-shock relations
     ($\gamma = 1.4$, $p_{0,2}$ the isentropic stagnation pressure of the
     laboratory-frame post-shock flow) gives $p_{0,2}/p_1 = 1.893$ at
     $M_s \approx 1.27$, and $p_{0,2}/p_1 \approx 2.07$ at $M_s = 1.31$.
     The paper does not print the expression for $p_{0,2}$ it used, so the
     difference (another definition, or an error) cannot be settled; the
     printed 1.31 stands. The reader also checked that the laboratory-frame
     post-shock flow becomes sonic at $M_s = 2.068$ for $\gamma = 1.4$,
     consistent with the printed $M_s^* \approx 2.07$.
   * **Reference list:** 10 entries. OCR misreads were corrected from the
     page image ("Griinig" for Grönig, "J. Compo Phys." for J. Comp. Phys.).
     Colella & Glaz (J. Comput. Phys. 59:264, 1985) is `colella-1985-b`,
     the published form of the work Colella & Woodward's PPM paper cites
     as "in preparation" (that entry, `colella-1984-c`, was folded into
     it in this batch); the bare key `colella-1985` is Colella's direct
     Eulerian MUSCL paper. Hillier's "These Proceedings" paper takes the
     printed year 1993, with a note that the volume appeared in 1995.
