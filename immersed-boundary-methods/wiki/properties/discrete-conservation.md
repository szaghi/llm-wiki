---
type: Property
title: "Discrete conservation"
description: "Whether an immersed boundary discretization conserves mass, momentum and energy at the discrete level near the boundary: exact by construction in cut-cell finite volumes with redistribution, restored by a mass source in direct forcing, guaranteed for the coupling operators of the classical method, and given up at the interface by the ghost fluid method."
status: established
aliases: [conservation, conservative immersed boundary, mass conservation]
tags: [conservation, cut-cell, coupling-operator, ghost-fluid, direct-forcing]
timestamp: 2026-11-08T17:31:00Z
---

# Discrete conservation

An immersed boundary scheme is **discretely conservative** for a quantity if
the sum of that quantity over the fluid cells changes only by the fluxes
through $\partial\Omega$ and the physical exchange with the body, to round-off.
The founding sources treat conservation differently:

| method | status | how | source |
|---|---|---|---|
| [cut-cell method](/methods/cut-cell-method.md) with [redistribution](/methods/redistribution.md) | conservative | finite-volume balance on clipped cells; the small-cell deficit is redistributed, equivalent to modified edge fluxes | [Pember et al. (1995)](/sources/pember-1995.md), §2.6 |
| cut-cell finite volume with face velocities | mass to machine precision | separately updated face-centre velocities satisfy the integral continuity exactly | [Ye et al. (1999)](/sources/ye-1999.md), §2 |
| [direct forcing](/methods/direct-forcing.md) with mass source | mass restored in cut cells | $q_m$ in each cell containing $\Gamma$; without it the fluid part of the cell gains or loses mass | [Kim et al. (2001)](/sources/kim-2001.md), §2.3 |
| [classical method](/methods/classical-immersed-boundary-method.md) | coupling neutral; momentum and energy conserved for uniform density | adjoint [spreading and interpolation](/operators/spreading-and-interpolation.md); skew-symmetric advection | [Peskin (2002)](/sources/peskin-2002.md), §5 |
| [ghost fluid method](/methods/ghost-fluid-method.md) | non-conservative at the interface, conservative under refinement in a stable flow | each fluid conservative; inter-fluid fluxes not unique; $O(\Delta x^n)$ error along the interface | [Fedkiw et al. (1999)](/sources/fedkiw-1999.md), §4.5 |

## Details

- **Classical method.** For uniform density and a translation-invariant
  elastic energy, total momentum is conserved by the spatially discretized
  scheme, and kinetic plus elastic energy decreases exactly by the viscous
  dissipation, because $S_h$ and $D_0$ are skew-symmetric, $L_h$ is symmetric
  non-positive and the discrete divergence vanishes. With non-uniform density
  these results are not available (Peskin 2002, §5). The interpolated boundary
  velocity is not discretely divergence-free, so the volume enclosed by a
  membrane leaks (Peskin 2002, §8).
- **Ghost fluid.** For a helium bubble advected in air the helium mass
  error converges at second order (Fedkiw et al. 1999, §4.5, Table I). When
  the interface length grows under refinement (Kelvin–Helmholtz or
  Richtmyer–Meshkov instability) the conservation error may not vanish, and
  the authors advise monitoring it.
- **Direct forcing.** Kim et al. (2001, §3.1) find the error of a
  decaying-vortex test with the mass source "much smaller" than without, and
  comparable with a computation that needs no immersed boundary.

# Citations

- [Pember et al. (1995)](/sources/pember-1995.md) — §2.6.
- [Fedkiw et al. (1999)](/sources/fedkiw-1999.md) — §4.5, §5.
- [Ye et al. (1999)](/sources/ye-1999.md) — §2.
- [Kim et al. (2001)](/sources/kim-2001.md) — §2.3, §3.1.
- [Peskin (2002)](/sources/peskin-2002.md) — §5, §8.
