---
type: Source
title: "Christlieb, Rossmanith & Tang (2014) — Finite difference WENO schemes with constrained transport for ideal MHD"
description: "Fourth-order unstaggered constrained transport: collocated FD-WENO MHD whose predicted field is replaced each stage by the fourth-order central curl of a WENO-HJ-evolved potential, holding the collocated central divergence exactly."
resource: "doi:10.1016/j.jcp.2014.03.001"
source_kind: paper
authors: [Christlieb A.J., Rossmanith J.A., Tang Q.]
year: 2014
venue: "J. Comput. Phys. 268:302-325 (arXiv:1309.3344)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2014-JCP-Christlieb-101016jjcp201403001.pdf"
tags: [constrained-transport, vector-potential, collocation, high-order, finite-difference, weno, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

A high-order member of the unstaggered constrained-transport line of
Tóth, Rossmanith and Helzel–Rossmanith–Taetz. Every variable is a point
value on one mesh, including $B$ and the potential $A$. This is the
[vector-potential](/methods/vector-potential-evolution.md) route to an
exactly held collocated divergence, with fourth-order accuracy in space
and time.

One SSP-RK stage has three steps:
1. The Jiang–Wu fifth-order FD-WENO base scheme predicts $B^*$.
2. The potential is advanced with a modified Jiang–Peng Hamilton–Jacobi
   WENO, with the velocity frozen.
3. $B^*$ is overwritten by the fourth-order central curl of $A$.

The total energy is kept unchanged through the correction (their Option 1).

The file read is the arXiv v2 preprint. Volume and pages were verified on
Crossref.

# Key claims

1. **Exact collocated divergence** (§6, eqs. 6.2, 6.8). The authors look
   for discrete curl and divergence operators whose derivative factors
   commute, and they use fourth-order central differences. Then
   $D_h^{\mathrm{c}} C_h^{\mathrm{c}} A_h = 0$ identically
   ([notation](/notation.md)). This is the high-order version of the
   second-order central choice of Tóth, Rossmanith and Helzel et al.
   Claim 6.1, with the proof omitted: each component of $B$ is conserved
   globally between stages.
2. **Potential system** (§2.2). In the Weyl gauge the 3D system
   $\partial_t A + (\nabla\times A)\times u = 0$ is non-conservative and
   only weakly hyperbolic, with incomplete eigenvectors at
   $\alpha = 0, \pi/2, \pi, 3\pi/2$ between $n$ and $u$. Following
   Helzel et al., they note this is an artifact of freezing $u$; the full
   MHD system stays strongly hyperbolic. In 2D only $A_z$ is evolved, by
   strongly hyperbolic advection, and $B_z$ is left to the base scheme.
3. **WENO-HJ limits the field, not the potential** (§5.1, Fig. 1). The
   weights are computed on central differences of $A$. Oscillations are
   therefore controlled in $\partial_x A$, which is $B$. On 1D advection
   of a kinked profile, conservation-law WENO gives a clean $q$ but an
   oscillatory $q_x$; WENO-HJ keeps both clean.
4. **Artificial resistivity in 3D** (§5.3, eqs. 5.19–5.24).
   * The unsplit scheme gets upwind dissipation in only two of three
     directions for each component.
   * A term $\varepsilon_1\,\partial_x^2 A_1$ (and its cyclic analogues)
     supplies the third, with
     $\varepsilon_1 = 2\nu\gamma_1\,\Delta x^2/(\delta + \Delta t)$, where
     $\delta = 0$ in all runs.
   * $\gamma_1$ is a WENO-style smoothness indicator of $\partial_x A_1$.
     It makes the term $O(\Delta x^6)$ on smooth data and $O(1)$ at kinks.
   * Forward-Euler stability holds for $\nu \le 0.5$ up to CFL 1. With
     SSP-RK4 they use $\nu \in [0.02, 0.2]$, and 0.1 in the runs shown.
5. **Fourth-order central curl and discontinuities** (§6). The curl
   stencil by itself would produce oscillations at magnetic
   discontinuities. The authors credit the WENO-HJ limiting of $A$ with
   suppressing them.
6. **Time stepping** (§3). Ketcheson's low-storage 10-stage SSP-RK4 runs
   at CFL 3.0. They argue this is cheaper than RK44 at CFL 0.8, and they
   flag that a many-stage method enlarges AMR ghost regions and
   inter-patch traffic.
7. **Results** (§7).
   * Fourth-order convergence of $B$ and $A$ on 2D and 3D Alfvén waves at
     CFL 3.
   * Rotated shock tube at $\tan^{-1}0.5$: the base scheme oscillates and
     the CT scheme does not.
   * Orszag–Tang runs to $t = 30$ without negative pressure. The base
     scheme goes negative near $t = 4$.
   * Cloud–shock in 2D, 2.5D and 3D: structure appears at $256^2$ that
     second-order MHDCLAW shows only at $512^2$.
   * No divergence norm is reported; the invariant holds by construction.
8. **Scope** (§8). Uniform or smoothly mapped grids only. AMR via the
   Shen–Qiu–Christlieb WENO-AMR is stated as future work.
9. **Record inconsistency.** Ref. [20], Helzel et al. 2011, is printed as
   "J. Comp. Phys. 227:9527–9553". Crossref gives 230:3803–3829.

# Notation map

| Christlieb, Rossmanith & Tang (2014) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf{A}$ (point values) | $A_h$, collocated | not edge-staggered as in the registry default $V_h^1$ |
| $D^x_{ij}, D^y_{ij}, D^z_{ijk}$ (eqs. 6.3, 6.9–6.11) | 1D antisymmetric derivative primitive | fourth-order central |
| $\nabla\times$ (eqs. 6.1, 6.5–6.7) | $C_h^{\mathrm{c}}$ | |
| $\nabla\cdot B_{ij}$ (eqs. 6.2, 6.8) | $D_h^{\mathrm{c}}$ | |
| $B^*$ | predicted, uncorrected field | |
| $\psi$ (scalar potential) | gauge function | **not** the GLM $\psi_h$; set to zero (Weyl gauge) |
| $\nu$, $\gamma_m$, $\varepsilon_m$ | artificial-resistivity parameters | no registry symbol |

# Pages created or updated

* Updated [Vector-potential evolution](/methods/vector-potential-evolution.md): the collocated high-order realization.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): published support for collocated $D_h^{\mathrm{c}} C_h^{\mathrm{c}} = 0$ at fourth order.
* Updated [Constrained transport](/methods/constrained-transport.md): the unstaggered potential-based line.
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md): base scheme against CT.
* Updated [Divergence source at collocated 2:1 seams](/results/collocated-seam-divergence-source.md): the interior identity is published, the seam behavior is not.

# Citations

1. `~/papers/mosaic/div-free-amr/2014-JCP-Christlieb-101016jjcp201403001.pdf` (doi:10.1016/j.jcp.2014.03.001): text extraction, all pages, including the reference list (47 entries).
