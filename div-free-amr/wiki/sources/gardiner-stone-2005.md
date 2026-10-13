---
type: Source
title: "Gardiner & Stone (2005) — An unsplit Godunov method for ideal MHD via constrained transport"
description: "2D CTU+CT scheme: finite-volume/CT consistency relations, a systematic construction of corner EMFs that reduce to the 1D solver for grid-aligned flow (the contact-upwinded E^c), and the multidimensional MHD source terms PPM interface states require."
resource: "doi:10.1016/j.jcp.2004.11.016"
source_kind: paper
authors: [Gardiner T.A., Stone J.M.]
year: 2005
venue: "J. Comput. Phys. 205(2):509-539"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2005-JCP-Gardiner-101016jjcp200411016.pdf"
tags: [constrained-transport, upwind-emf, godunov, ctu, field-loop]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The two-dimensional predecessor of
[Gardiner & Stone (2008)](/sources/gardiner-stone-2008.md), and the algorithmic
core of the Athena code. It is a single-step, second-order, unsplit Godunov
scheme: PPM reconstruction, Colella's corner transport upwind (CTU), and
[constrained transport](/methods/constrained-transport.md) on face
(area-averaged) fields. The paper's three contributions:
* consistency relations that tie the finite-volume fluxes of the
  cell-centered field to the corner EMFs;
* a systematic construction of corner EMFs that reduce exactly to the 1D
  solver for plane-parallel, grid-aligned flow;
* the multidimensional terms that PPM interface states and the CTU
  transverse update need for MHD.

The file read is the arXiv preprint (astro-ph/0501557). Venue and pages were
verified on Crossref.

# Key claims

1. **FV–CT consistency** (§2.3, eqs. 19–24). If the cell-centered field is
   defined as the average of its two face values, at $t^n$ and at $t^{n+1}$,
   then the finite-volume flux of each cell-centered component *must equal*
   the average of the two adjacent corner EMFs. The Riemann-solver flux for
   the field is only a predictor; the CT EMF is the corrector. A CT-like
   update on cell-centered fields holds the divergence "on a different
   (larger) stencil than used to compute the fluxes".
2. **Plain averaging halves the dissipation** (§3.2.1, eqs. 34–38). For a
   grid-aligned plane-parallel flow, the arithmetic average of the four
   face EMFs reproduces the 1D flux with the numerical viscosity **halved**.
   The scheme then does not reduce to its 1D solver, and its stability is
   questionable. The cause is the average's lack of directional bias.
   Balsara–Spicer restored the bias with shock-sensing switches.
3. **The EMF as an integration from face centers** (§3.2.2, eq. 42). The
   corner EMF is the average of the four face values, each integrated to the
   corner with an estimate of its derivative. Three choices of derivative
   give three algorithms that all reduce exactly to the 1D solver for
   grid-aligned flow:
   * $\mathcal{E}^\alpha$, Lax–Friedrichs-upwinded derivatives: stable but
     diffusive;
   * $\mathcal{E}^\circ$, the $\alpha = 0$ limit, not upwinded: oscillatory
     on advection;
   * $\mathcal{E}^c$, derivatives upwinded by the sign of the mass flux
     (contact mode), independent of the Riemann solver: the recommended
     choice.

   At first order, $\mathcal{E}^\circ$ coincides with the
   [upwind-CT](/methods/upwind-constrained-transport.md) EMF of
   [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md).
4. **MHD needs multidimensional terms in the interface states** (§3.1, §4.1.2).
   In primitive variables the induction equation for the transverse field
   keeps terms in $\partial B_x/\partial x$, $\partial B_y/\partial y$ that
   no 1D system has. They must enter the characteristic tracing as source
   terms, and the CTU half-step update needs them too. "If they had been
   omitted, the field loop disintegrates in oscillations before completing a
   fraction of an orbital period."
   * Placing the $v_z\,\partial B_x/\partial x$ term in the CTU update, and
     not in the tracing, prevents the spurious coherent growth of $B_z$ in a
     loop advected with $v_z$. That is the seed of the 3D field-loop
     diagnostic of the 2008 paper.
   * Dimensionally split updates cannot hold the divergence between sweeps,
     hence the unsplit CTU.
5. **Rotated shock tube at a generic angle** (§5.3). At
   $\theta = \tan^{-1}2$ on a 256×128 grid, the cell-centered normal field
   oscillates by about 10% at the fast shocks, even under exact CT. Averaged
   conservatively onto $r_x\times r_y$ "macro-cells", the grid's symmetry
   period, the normal field is constant to round-off. The oscillation is the
   grid-scale transverse variation of the discrete solution, not
   insufficient EMF dissipation, since $\mathcal{E}^\alpha$ does not reduce
   it. Schemes that create a *jump* in the normal field cannot recover this
   property. At 45° the normal field stays constant to round-off by
   symmetry ([rotated shock tube](/benchmarks/rotated-shock-tube.md)).
6. **Field-loop advection, in 2D** (§3.3.1, §5.1). A loop with
   $\beta = 2\cdot10^6$ is advected diagonally on a $2N\times N$ periodic
   grid. It discriminates EMF dissipation: $\mathcal{E}^\alpha$ diffuses the
   static loop (a reconnection hole forms) and $\mathcal{E}^\circ$ goes
   oscillatory. The second-order scheme loses magnetic energy as a power law
   in time, and the circular field-line shape survives at low resolution
   ([field-loop advection](/benchmarks/field-loop-advection.md)).
7. **Other tests.** Linear waves converge at orders 2.0–2.29 at 63.4°. Also
   reported: a CP Alfvén wave (no parametric instability at these
   parameters), a current-sheet reconnection robustness test, and a
   low-$\beta$ blast with no grid artifacts. The authors claim the scheme is
   suited to static or adaptive refinement; this is not tested here.

# Notation map

| Gardiner & Stone (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B_{x,i\pm1/2,j}$, $B_{y,i,j\pm1/2}$ (area averages) | $B_h \in V_h^2$ | primary field data |
| $B_{x,i,j}$ (volume average, eq. 19) | collocated $B_h$ | mean of two faces |
| $E_{z,i\pm1/2,j\pm1/2}$ | $E_h \in V_h^1$ | corner EMF |
| $E_{z,i+1/2,j}$ (from the Riemann solver) | $f^{x,*}$, $f^{y,*}$ magnetic fluxes | base-scheme electric fields |
| $\mathcal{E}^\alpha$, $\mathcal{E}^\circ$, $\mathcal{E}^c$ | kept as named | CT EMF algorithms |
| $q_{i,j}$ (conserved variables) | written out in prose | |

# Pages created or updated

* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): consistency relations, the averaging defect, the $\mathcal{E}$ family.
* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): $\mathcal{E}^\circ$ = first-order UCT.
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): the macro-cell diagnostic.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): the 2D origin of the test.

# Citations

1. `~/papers/mosaic/div-free-amr/2005-JCP-Gardiner-101016jjcp200411016.pdf` (arXiv:astro-ph/0501557; doi:10.1016/j.jcp.2004.11.016): text extraction, all 45 pp., Appendix A and the reference list (33 entries).
