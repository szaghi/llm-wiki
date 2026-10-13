---
type: Definition
title: "Slowly moving shock anomaly"
description: "Spurious post-shock oscillations, and a spike in the conserved flux of the shock cell, produced when a captured shock moves slowly relative to the grid; the captured intermediate state is an admissible point of the curved Hugoniot locus, so the anomaly appears with any Riemann solver and does not shrink under grid refinement."
status: established
aliases: [slowly-moving shock, post-shock oscillations, discharge spike]
tags: [shock-instability, riemann-solver, robustness, definition]
timestamp: 2026-10-13T00:00:00Z
---

# Slowly moving shock anomaly

Roberts called it "numerical noise generated in the discrete shock
transition layer which is transported downstream"
([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.1,
quoting Roberts). A captured shock that moves slowly through the grid
emits waves behind it every time it crosses a cell. In a conservation
law with a mass flux, such as shallow water, the flux in the shock cell
also shows a spike above both end states.

**What "slowly" means.** The literature uses three definitions
([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §I footnote):
1. the shock takes many time steps to cross a cell;
2. a characteristic speed changes sign across the shock;
3. Kitamura & Shima's own: $0 < M_{\mathrm{prop}} < M_{\mathrm{sig}}$. Here
   $M_{\mathrm{sig}}(M_s)$ is the post-shock sound speed over the
   pre-shock one, from the Rankine–Hugoniot pressure and density ratios
   (eq. 10b). It tends to
   $$M_{\mathrm{sig}} \to \frac{\sqrt{2\gamma(\gamma-1)}}{\gamma+1}\,M_s \approx 0.44\,M_s \qquad (\gamma = 1.4)$$
   as $M_s \to \infty$. Below this speed, noise generated downstream can
   catch up with the shock and disturb it. The convection speed is
   neglected, so $M_{\mathrm{sig}}$ is a lower bound
   ([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §III.B, eqs. 7–10).

**Mechanism.** A captured shock is a three-state jump: a left state, an
intermediate cell state and a right state. The intermediate state lies on
the Hugoniot locus, so it is an admissible weak solution. When the
Hugoniot curve is curved and not monotone in the flux, the intermediate
flux exceeds the constant flux of the end states, and that excess is the
spike. On this account:
* the anomaly is "always present with independence of the choice for the
  Riemann solver";
* it would vanish for linear Hugoniot curves, even in a nonlinear system;
* refining the grid does not shrink the spike, only raises its frequency;
* numerical diffusion "barely helps" across transcritical shocks, where a
  characteristic speed changes sign and forces a sharp profile.

([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md),
§§4.1–4.1.3.) In 2D the spike runs along the whole bow shock. A shock that
is not aligned with the grid sheds transverse spurious waves each time it
jumps from one cell column to the next (§4.1.2).

**Severity against shock speed.** On Kitamura & Shima's map, the slowly
moving range $0 < M_{\mathrm{prop}} < 0.44\,M_s$ is the most severe case
for fluxes that capture the shock within one cell (Roe, AUSM+-up, LDFSS).
Such shocks suffer both from the perturbed grid, since crossing a cell
takes long, and from downstream noise. Fluxes that spread the shock over
a few cells or carry multidimensional dissipation are insensitive to
shock speed. Second-order schemes "reportedly" show post-shock
oscillations from moving shocks more readily than first-order ones
([Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§II.B, IV.B, V).
The same paper, and the one-dimensional carbuncle of a steady shock
([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §4.2),
tie this anomaly to [numerical shock instability](/definitions/numerical-shock-instability.md).

**Remedies.**
* Extra dissipation for slowly moving strong shocks, through a diffusive
  flux or alternating grid motion. Colella & Woodward added it to PPM
  because even first-order Godunov has a 3 % post-shock entropy error
  there ([Colella & Woodward (1984)](/sources/colella-1984.md), §4; [PPM](/methods/ppm.md)).
* The more diffusive Davis wave-speed estimates in an HLL-type flux,
  offered as "useful for suppressing possible post-shock oscillations"
  ([Xie et al. (2021)](/sources/xie-2021.md), §5).
* A spike-reducing flux for shallow water with a bed source. In the shock
  cells only, the cell-centred flux is replaced by one extrapolated from
  the two neighbours, plus a source correction that keeps both
  generalized Rankine–Hugoniot equilibria; the interface flux is then
  upwinded with the augmented Roe solver. The steady discharge across a
  hydraulic jump is exact to machine precision at every tested sub-cell
  shock position. Narrow spikes remain while the shock crosses a cell
  interface in a quasi-steady sweep. The scheme is first order
  ([Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§5.1, 6.1).

**Later uses (batch 11).** *An early account.*
[Woodward & Colella (1984)](/sources/woodward-1984.md) describe the
anomaly for strong shocks in gas dynamics.
* *Size and persistence* (§Vc). Strong shocks that move slowly relative
  to the grid, as do all shocks of the [step problem](/benchmarks/forward-facing-step.md)
  after $t = 2$, leave post-shock oscillations of about 1–2 % amplitude.
  Their wavelengths are many zones, so they cannot be damped once
  generated.
* *Cure in PPM* (§Vc). The shock is broadened to about 2 zones "in the
  worst cases", by flattening plus either an alternating ("jiggled")
  remap grid, a diffusive error that is fifth-order small, or Lapidus
  viscosity with coefficient 0.1, third-order small in smooth flow
  ([PPM](/methods/ppm.md)). This is the remedy listed first above, with
  its error orders.
* *Grid-aligned shocks in 2D* (§VIb). Thin captured shocks that are
  nearly aligned with the mesh emit noise where they jump from one zone
  column to the next, as in the 2D statement above. Godunov and MUSCL show
  it on the step and the [double Mach reflection](/benchmarks/double-mach-reflection.md),
  MUSCL more strongly because its shocks are thinner, in line with the
  report that second-order schemes show these oscillations more readily.
  The authors call it a "numerical instability of 2-D, strong, stationary
  shocks" and cure it with more dissipation at such shocks
  ([numerical shock instability](/definitions/numerical-shock-instability.md)).
* *Vanishing characteristic speeds* (§VIc, Fig. 10). Single-step Eulerian
  MUSCL is noisy along the nearly steady reflected shock of the double
  Mach reflection, while MUSCL as Lagrange step plus remap is not, which
  "demonstrates the extra sensitivity of single-step Eulerian schemes to
  vanishing characteristic speeds".

# Citations

1. [Navas-Montilla & Murillo (2019)](/sources/navasmontilla-2019.md), §§4.1–4.2, 5.1, 6.1.
2. [Kitamura & Shima (2019)](/sources/kitamura-2019.md), §§I, II.B, III.B, IV.B, V.
3. [Colella & Woodward (1984)](/sources/colella-1984.md), §4.
4. [Xie et al. (2021)](/sources/xie-2021.md), §5.
5. [Woodward & Colella (1984)](/sources/woodward-1984.md), §§Vc, VIb–VIc.
