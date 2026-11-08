---
type: Source
title: "Fedkiw et al. (1999) — A non-oscillatory Eulerian approach to interfaces in multimaterial flows (the ghost fluid method)"
description: "Introduces the ghost fluid method: a level set tracks a material interface, each grid point near it carries a ghost fluid of the other material with the real pressure and velocity and an extrapolated entropy, and each fluid is advanced with an unmodified single-phase ENO–Runge–Kutta scheme, keeping density profiles sharp without Riemann solvers or dimensional splitting."
resource: "doi:10.1006/jcph.1999.6236"
source_kind: paper
authors: [Fedkiw R.P., Aslam T., Merriman B., Osher S.]
year: 1999
venue: "J. Comput. Phys. 152(2):457-492"
local_file: "/home/stefano/papers/mosaic/immersed-boundary/1999_Crossref_Journal_of_Computational_Physics_Fedkiw_A_Non-oscillatory_Eulerian_Approach_to_Interfaces_in_Multima.pdf"
tags: [ghost-fluid, level-set, compressible, multimaterial, sharp-interface, conservation]
timestamp: 2026-11-08T17:46:00Z
---

# Summary

Fedkiw, Aslam, Merriman and Osher combine an Eulerian scheme with a
Lagrangian-like sharp treatment of material interfaces: the
[ghost fluid method](/methods/ghost-fluid-method.md). A level set marks the
interface; near it every node stores the real fluid and a ghost fluid of the
other material whose pressure and normal velocity are copied from the real
fluid and whose entropy is extrapolated, constant, from its own side, with
an isobaric fix against overheating. Each fluid is then advanced with a
standard single-phase scheme and the level set selects the valid result.
The method keeps a Heaviside density profile
([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)),
extends to multi-D and multistage time integration without splitting, and is
non-conservative only at the interface
([discrete conservation](/properties/discrete-conservation.md)).

# Version read

Version of record, J. Comput. Phys. 152, 457–492 (1999), 36 pages. Read in
full: §§1–4 (equations, level set, method, ghost cells, conservation) and the
Appendix; §5 (examples) read except the shock–bubble results, which were
skimmed. Page-1 title and authors match Crossref.

# Key claims

1. Eulerian schemes admit non-physical oscillations near material interfaces because of the smeared density and the change of equation of state; Lagrangian schemes handle interfaces but not large deformation (Abstract, §1). **Stated**
2. Earlier interface-Riemann Eulerian methods needed "ill-advised" dimensional splitting and were hard to combine with Runge–Kutta integrators; the ghost fluid method needs neither (§1, §3). **Stated**
3. With ghost values defined everywhere, each fluid is updated by a standard method and the sign of the level set picks the valid answer after every stage; only 3–5 ghost cells per side are needed (§3). **Stated**
4. Pressure and velocity are copied into the ghost fluid; entropy is extrapolated with constant one-sided extrapolation, preferred to high order because it minimizes overheating; the isobaric fix replaces the entropy of the interface node by its neighbour's (§4). **Stated**
5. "We do not need to solve a Riemann problem, consider the Rankine–Hugoniot jump conditions, or solve an initial boundary value problem at the interface" (§4). **Stated**
6. In multi-D, constant extrapolation in the normal direction is done by solving $I_t\pm\mathbf n\cdot\nabla I=0$ for a few fictitious steps after each Runge–Kutta substep; tangential velocity extrapolated as well preserves a tangential jump exactly (§4, Appendix). **Stated**/**Shown** (shear-wave example)
7. The method is formally non-conservative on the interface; conservation error is expected as $O(\Delta x^{n})$ times the interface length; under refinement conservation is achieved for stable interfaces, not necessarily for unstable ones whose interface lengthens (§4.5). **Derived** (heuristic)
8. Helium bubble advected in air: $L^1$ density error and helium mass error both converge at second order (§5, Table I). **Shown**
9. In 1-D shock–contact tests the contact is one cell off at all resolutions (first order in position), because its speed is estimated by the local fluid velocity (§5). **Shown**
10. Tests with ideal-gas, Tait (water, with cavitation cut-off) and JWL equations of state agree with exact or reference solutions (§5). **Shown**

# Notation map

| Fedkiw et al. (1999) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$ | $\phi$ | level set; agree |
| $\mathbf N=\nabla\phi/|\nabla\phi|$ (negative → positive fluid) | $\mathbf n$ | registry: out of the body; for two fluids the "$+$" side is named on the page |
| $\mathbf U$ | $\mathbf q$ | conserved variables |
| $E$, $e$ | $E$, $e$ | agree |
| $I$ | $I$ | extrapolated (isobaric-fix) variable, page-local |
| $\epsilon=1.5\Delta x$ | band half-width, page-local | |

# Reference list

34 printed references, merged complete into the [bibliography](/bibliography.md)
from the Crossref deposited list.

# Pages created or updated

Chunk 1 (2026-11-08), list updated in chunk 4 (2026-11-08). This source is cited on:

- [Immersed boundary method](/definitions/immersed-boundary-method.md)
- [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
- [Ghost fluid method](/methods/ghost-fluid-method.md)
- [Discrete conservation](/properties/discrete-conservation.md)
