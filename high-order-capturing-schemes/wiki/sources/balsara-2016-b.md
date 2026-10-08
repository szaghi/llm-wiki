---
type: Source
title: "Balsara & Kim (2016) — A subluminal relativistic magnetohydrodynamics scheme with ADER-WENO predictor and multidimensional Riemann solver-based corrector"
description: "One-step second- to fourth-order finite-volume relativistic MHD on a Yee mesh that keeps velocities subluminal: one conserved-to-primitive inversion per cell via the 1/24 average–point identity, WENO or PPM reconstruction of the four-velocity, an ADER predictor in those variables, and a multidimensional HLLC/HLLEM Riemann solver for the edge electric fields."
resource: "doi:10.1016/j.jcp.2016.02.001"
source_kind: paper
authors: [Balsara D.S., Kim J.]
year: 2016
venue: "J. Comput. Phys. 312:357-384"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2016-JCP-Balsara-101016jjcp201602001.pdf"
tags: [mhd, relativistic, ader, constrained-transport, multidimensional-riemann-solver]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Keyed `balsara-2016-b`, since WENO-AO holds the bare key. Merged into the
ADER, constrained-transport (including a new open Contradictions entry),
Riemann-solver, characteristic, fourth-order FV, PPM and positivity pages,
and the rotor, blast, vortex, shock–vortex and Alfvén-wave benchmarks.

# Key claims

1. **Why the four-velocity** (§2): reconstructing conserved variables needs
   a fragile inversion and can go superluminal anywhere in the cell;
   reconstructing $\mathbf v$ is ill-conditioned at large Lorentz factor.
   With the four-velocity, $v^2 = \vartheta/(1 + \vartheta) < 1$ for any
   $\vartheta \ge 0$ (eqs. 2.4–2.5).
2. **Conversion** (eqs. 2.6–2.7, page image): point values from averages by
   the $\tfrac1{24}$ Laplacian, one inversion at the centre, averages of the
   primitives back, with a flattener on the correction.
3. **Flattener** (eqs. 2.8–2.9): from the divergence of the four-velocity
   against the minimum relativistic sound speed over 27 cells.
4. **Predictor** (§3): ADER in primitive variables; Lax–Wendroff at second
   order, explicit nodal collocation at third and fourth, with 2 and 3
   iterations. Runge–Kutta is rejected because its stages carry no
   subluminal guarantee.
5. **1D solvers** (§4.1, Appendix B): relativistic HLLC (modified for a
   common normal velocity and total pressure) and HLLEM; positivity proofs
   exist only for first-order 1D HLL-type solvers.
6. **Multidimensional solver** (§4.2, eqs. 4.1–4.15, page images): a
   strongly interacting state with linear sub-structure of the entropy and
   Alfvén waves; the edge field from two numerical fluxes. It removes the
   need to double the dissipation (§1).
7. **Divergence** (§1): divergence-free MHD "requires the use of a
   staggered, Yee-type mesh". This conflicts with the unstaggered CT of
   Christlieb et al., and is recorded as an open contradiction on the CT page.
8. **Tests** (§§5–6): Lorentz-boosted vortices (design order; Tables 3 and
   4 are identical, a probable duplicate); a relativistic rotor resolution
   study ($400^2$ never reaches the nominal Lorentz factor); blast (third or
   fourth order, both stated); a relativistic shock–vortex interaction; an
   axisymmetric jet; torsional Alfvén-wave decay.

# Notation map

| Balsara & Kim (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\gamma$ (Lorentz factor), $\Gamma$ (polytropic index) | (words), $\gamma$ | roles swapped |
| $V = (\rho, \gamma\mathbf v, P_g, \mathbf B)$ | primitive vector with the four-velocity | words |
| $\varepsilon$, $h$ (enthalpy) | $E$, (words) | |
| $\phi$ (eq. 2.6), $\eta$ (eq. 2.8) | $1 - \phi_i$, $\phi_i$ | opposite conventions in one paper |
| $\bar U$, $U_\xi$, $U_\psi$ (strongly interacting state) | (words), $f^{**}_x$, $f^{**}_y$ for its fluxes | |
| $S_L, S_R, S_D, S_U$ | same | |
| $E_z$ | $\mathcal E_z$ | |

# Pages created or updated

* Updated [ADER one-step schemes (arbitrary high order using derivatives)](/methods/ader.md).
* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Created [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Updated [Fourth-order finite-volume method with average–point conversions](/methods/fourth-order-finite-volume.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2016-JCP-Balsara-101016jjcp201602001.pdf` (doi:10.1016/j.jcp.2016.02.001, checked on Crossref: J. Comput. Phys. 312:357–384, May 2016; typeset journal article): text extraction, all sections; pp. 360, 361, 368–370 and 379 read from the page images. Appendices A–B, eqs. 4.12–4.13 (undefined $\lambda^{\pm}$) and the jet ambient pressure are not reproduced. Reference list: 73 entries.
