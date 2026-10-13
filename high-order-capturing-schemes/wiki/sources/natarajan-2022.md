---
type: Source
title: "Natarajan, Grout, Zhang & Day (2022) — A moving embedded boundary approach for the compressible Navier–Stokes equations in a block-structured adaptive refinement framework"
description: "Second-order cut-cell finite volume with flux redistribution and a mirrored-state Riemann problem at the wall, extended to moving bodies in AMReX: freshly cleared cells are filled by a volume-weighted neighbour average; the order drops to 1 on a receding piston and a closed piston loses up to 0.9% of its mass, so the moving scheme is consistent but not conservative."
resource: "doi:10.1016/j.jcp.2022.111315"
source_kind: paper
authors: [Natarajan M., Grout R., Zhang W., Day M.]
year: 2022
venue: "J. Comput. Phys. 465:111315"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2022-JCP-Natarajan-101016jjcp2022111315.pdf"
tags: [embedded-boundary, moving-boundary, amr, boundary-treatment]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

A second-order Godunov/MUSCL cut-cell finite-volume scheme (characteristic
van Leer limiting, RK2) in the AMReX compressible example solver, with
flux redistribution for small cells, extended to bodies that move. The
wall flux comes from a Riemann problem against a mirrored state with the
wall's normal velocity. Freshly cleared cells are filled by a
volume-weighted neighbour average. All cut cells are refined to the
finest AMR level. Merged into [cut-cell finite volume](/methods/cut-cell-finite-volume.md).

# Key claims

1. **Flux redistribution** (§2, after Colella et al. 2006 and Pember et
   al. 1995): hybrid conservative/non-conservative update over a 3×3×3
   neighbourhood, excess redistributed with weights $\kappa_j/\sum\kappa_k^2$;
   no monotonicity or positivity claim.
2. **Moving update** (§2.1, eqs. 2–5): Reynolds transport theorem,
   division by the old volume fraction, no swept-volume term.
3. **Wall flux** (eqs. 6–8): the ghost velocity is the fluid velocity
   with its normal component reflected about the wall's normal velocity,
   passed to the face Riemann solver.
4. **Cleared cells** (§2.1): volume-weighted average of fluid neighbours,
   justified by free-stream preservation; covered cells not discussed.
5. **Order** (§3.2.2, Fig. 5c): first order in entropy $L^2$ on a
   receding piston, attributed to the cleared-cell fill.
6. **Mass** (§3.6, Fig. 11f): up to 0.92 % lost at $32^3$, 0.31 % at
   $64^3$ in a closed piston. The paper concludes that "the algorithm
   ensures conservation"; the numbers show consistency, not discrete
   conservation.
7. **AMR** (§3.1): every cut cell refined to the finest level, so no
   coarse–fine boundary crosses the body; Wong–Lele shock tagging.
8. **Viscous walls** (§2.2, App.): a third-order least-squares fit for
   wall gradients.

**Tests:** a pulsating sphere (acoustic, no cell clearing); advancing and
receding pistons; a moving cylinder into a stationary Mach 1.34 or 2.82
shock ([shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md));
moving wedge and cone ([Schardin's problem](/benchmarks/schardin-problem.md));
a pitching NACA 0012 at Mach 0.755; a reciprocating piston; moving and
oscillating cylinders at Re 40–185. Comparisons are mostly graphical.

# Notation map

| Natarajan et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha$ (volume fraction) | $\kappa_i$ | $\alpha$ is the Lax–Friedrichs speed |
| $Q$, $\bar f$ | $u$ | |
| $F$ | $\mathbf f$ | |
| $(\nabla\cdot F)_c$, $(\nabla\cdot F)_{nc}$ | $(\nabla\cdot\mathbf f)^{\mathrm c}$, $(\nabla\cdot\mathbf f)^{\mathrm{nc}}$ | |
| $\delta M$, $w_j$ | words | |
| $u$; $u_w$, $u_g$ | $\mathbf v$; words | wall and ghost velocity |
| $\tilde w$ | words | Wong–Lele sensor |

# Pages created or updated

* Contributed to [Cut-cell finite volume](/methods/cut-cell-finite-volume.md) (moving bodies, flux redistribution), [Shock reflection from a cylinder](/benchmarks/shock-reflection-from-cylinder.md), [Schardin's problem](/benchmarks/schardin-problem.md).
* Updated [High-order AMR](/methods/high-order-amr.md), [Free-stream preservation](/properties/free-stream-preservation.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2022-JCP-Natarajan-101016jjcp2022111315.pdf`.
   * **Version.** arXiv:2108.00126v1 (31 July 2021), not the typeset
     article.
   * **Identity.** doi:10.1016/j.jcp.2022.111315, checked on Crossref:
     J. Comput. Phys. 465:111315, September 2022.
   * **How it was read.** Text extraction, all sections.
   * **Recorded as printed.** The energy flux of eq. 8 is right only for
     $\gamma = 2$; the entropy definition has the wrong sign on the
     exponent; the Mach 2.82 post-shock density does not match its stated
     ratio; the text cites "Eqn. 9" for the unnumbered cleared-cell fill.
   * **Reference list:** 90 entries.
