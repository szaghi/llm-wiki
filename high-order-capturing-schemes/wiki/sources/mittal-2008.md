---
type: Source
title: "Mittal, Dong, Bozkurttas, Najjar, Vargas & von Loebbecke (2008) — A versatile sharp interface immersed boundary method for incompressible flows with complex boundaries"
description: "Finite-difference sharp-interface ghost-cell immersed boundary for incompressible viscous flow with stationary, moving and deforming 3D bodies and membranes: closest-element node classification, an image point mirrored across the boundary intercept with trilinear interpolation, implicit coupled Dirichlet (velocity) and nominally first-order Neumann (pressure correction) closures, Ye et al.'s fresh-cell rule, inside a collocated second-order fractional-step solver; velocity converges at second order in a self-convergence test read from a graph."
resource: "doi:10.1016/j.jcp.2008.01.028"
source_kind: paper
authors: [Mittal R., Dong H., Bozkurttas M., Najjar F.M., Vargas A., von Loebbecke A.]
year: 2008
venue: "J. Comput. Phys. 227:4825–4852"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2008-JCP-Mittal-101016jjcp200801028.pdf"
tags: [immersed-boundary, moving-boundary, boundary-treatment, navier-stokes, accuracy]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A finite-difference, sharp-interface ghost-cell immersed-boundary (IB)
method for incompressible viscous flow around stationary, moving and
deforming 3D bodies, zero-thickness membranes included. The bodies are
unstructured triangulated surface meshes immersed in non-uniform
Cartesian grids. Each ghost node (a solid node with a fluid neighbour) is
reflected along the wall normal to an image point, with the boundary
intercept exactly midway; the image-point value is a trilinear (bilinear
in 2D) interpolant of the 8 (4) surrounding nodes, and the ghost value
follows from a linear relation along this probe. The relation imposes a
Dirichlet condition on the velocity or a Neumann condition on the
pressure correction, and it is solved implicitly and fully coupled with
the flow equations. Moving bodies use the fresh-cell treatment of Ye et
al. (1999), adapted to the same image-point stencil. The flow solver is a
collocated, cell-centred, second-order central-difference fractional-step
scheme. Velocity is claimed globally and locally second order from a
self-convergence study; the rest of the validation compares with
published data for cylinders, an airfoil, a sphere and impulsively started
bodies, and two demonstrations (a fish fin, a dragonfly) close the paper.
There is no compressible flow, no shock and no capturing scheme. Merged
into [immersed-boundary methods](/methods/immersed-boundary-method.md).

# Key claims

1. **Two IB families** (§1, after the Mittal & Iaccarino review):
   continuous forcing (Peskin; Goldstein et al.; Saiki & Biringen) gives a
   "diffuse" boundary; discrete forcing depends on the discretization but
   can keep the boundary sharp. The present method is discrete forcing
   (§2.2), with no ad-hoc constants and no momentum forcing in any fluid
   cell (§1).
2. **Flow solver** (§2.1, eqs. 1–13). Constant-property incompressible
   Navier–Stokes. Cell-centred collocated velocity and pressure, plus
   face-centre velocities (Fig. 1). Van Kan's fractional step in three
   sub-steps: second-order Adams–Bashforth convection, Crank–Nicolson
   diffusion, second-order central differences, line-SOR for the momentum
   predictor (eq. 3). Face velocities come from a Rhie–Chow-like averaging
   that removes and re-adds the old pressure gradient (eqs. 4–8), against
   odd–even decoupling. The pressure-correction Poisson equation (eq. 10)
   carries Neumann conditions on every boundary and is solved by geometric
   multigrid with a line Gauss–Seidel smoother. The face velocities are
   discretely divergence-free "to machine accuracy". Good discrete
   kinetic-energy conservation is claimed to allow $\mathrm{Re}$ up to at
   least $O(10^4)$ without upwinding or artificial dissipation (stated,
   not shown).
3. **Time step** (§3, eq. 25): explicit convection limits
   $\Delta t\,(\vert v_x\vert/h_x + \vert v_y\vert/h_y + \vert v_z\vert/h_z) < \nu_{\max}$,
   with $\nu_{\max} \approx 0.5$ found stable.
4. **Classification is not ray tracing** (§2.2.2, Fig. 4). For each node
   the closest surface element is found; the sign of the dot product of
   its outward normal with the vector from the element to the node decides
   fluid (positive) or solid (negative). Done once for stationary bodies;
   each step for moving bodies, only near the previous fluid–solid
   boundary, because the body moves at most about one cell per step.
   Ghost cells are solid nodes with at least one face-neighbour in the
   fluid (Fig. 5); interior solid nodes get the trivial equation "value =
   0".
5. **Boundary intercept and image point** (§2.2.2, Figs. 5–6). The
   normal segment from the ghost node to the surface gives the boundary
   intercept; the image point lies on its extension so that the intercept
   is exactly midway (probe length twice the ghost-to-wall distance). The
   intercept search is made robust: closest surface vertex, then normal
   intercepts on the elements sharing it (the shortest if several), a
   wider search if none, and finally the closest point on the first
   element set, possibly on an edge or a vertex. A wrong intercept gives
   oversized stencils and poor iterative convergence.
6. **Interpolation** (§2.2.2, eqs. 14–19, Appendix A). A trilinear
   interpolant on the 8 nodes around the image point, its coefficients
   from the inverse Vandermonde matrix, gives the image value as a
   weighted sum of nodal values plus a truncation error $O(h^2)$
   (Appendix A); the weights depend only on geometry and grid. If the
   ghost node is itself one of the 8 nodes, its row is replaced by the
   wall condition at the intercept. If the stencil holds other ghost
   nodes, the ghost values are coupled; the system is claimed diagonally
   dominant and is solved by point Gauss–Seidel, "within about 10
   iterations in most cases".
7. **Closures** (eqs. 20–23). Dirichlet (velocity): the wall value is the
   mean of the ghost and image values, implemented as "ghost value plus
   interpolated image value equals twice the wall value". Neumann
   (pressure correction): the wall normal derivative is the central
   difference along the probe, implemented as "ghost value minus image
   value equals minus the probe length times the prescribed normal
   derivative". Both are solved fully coupled with the momentum and
   Poisson equations of the neighbouring fluid cells.
8. **Order argument** (§2.2.2, after eq. 23). With the probe length
   $O(h)$ the Dirichlet closure is second order, so velocity is locally
   and globally second order. The Neumann closure is "nominally
   first-order" (its interpolation error divided by the probe length is
   $O(h)$), so the pressure gradient is locally first and globally second
   order, and the pressure itself second order; velocity stays second
   order because the gradient enters the update multiplied by
   $\Delta t = O(h)$. These are arguments: only velocity errors are
   measured (§3.1).
9. **Against the ghost-fluid method of Gibou et al.** (§§1, 2.2.2). That
   method interpolates along grid lines, so a Neumann condition needs
   tangential derivatives at the wall, and its Dirichlet form becomes
   ill-conditioned as the wall approaches a node. The midway-intercept
   construction stays well behaved as the probe length vanishes; "no need
   to resort to lower-order fixes".
10. **Against cut cells** (§1): the same spatial order as the
    sharp-interface cut-cell methods, but "easily extended" to complex 3D
    geometries, whereas "successful implementation of the cut-cell method
    to 3D geometries has not yet been accomplished" (after Mittal &
    Iaccarino). This is the source's 2008 view; later 3D cut-cell work in
    this bundle (e.g. [Giuliani et al. (2022)](/sources/giuliani-2022.md))
    postdates it.
11. **Collocated grid** (§2.2.2): one set of ghost cells, instead of four
    (three velocity components and pressure) on a staggered grid.
12. **Moving bodies and fresh cells** (§2.2.3, eq. 24, Fig. 7). Surface
    vertices are advanced with a prescribed or computed velocity; ghost
    cells, intercepts, image points and weights are recomputed every
    step. A fresh cell (solid at $t^n$, fluid at $t^{n+1}$) is at most one
    cell deep because of the CFL limit, and lacks the old convective,
    diffusive and pressure-gradient terms. Following Ye et al.'s cut-cell
    method, its intermediate velocity is interpolated: normal to the wall,
    image point, trilinear interpolation on the 7 non-fresh nodes around
    it plus the intercept. Its pressure then comes from the Poisson
    equation like any cell. Consistency is argued from every fresh cell
    having been a ghost cell the step before. Freshly covered nodes are
    only re-classified; no conservation statement is made.
13. **Membranes** (§3.5.1): a zero-thickness body needs ghost cells on
    both sides, so a node can be ghost and fluid at once (auxiliary arrays
    and pointers).
14. **Cost of motion** (§3.6.1): only the interpolation weights in one
    layer of cells around the body are recomputed per step, against a
    full remeshing for body-fitted methods.

**Tests** (§3; all incompressible and viscous):
* *Grid convergence* (§3.1, Figs. 8–9): cylinder at $\mathrm{Re} = 100$
  in a domain two diameters square, uniform grids $210^2$, $126^2$, $90^2$ and
  $70^2$ against a $630^2$ solution of the same scheme, fixed
  time step of $10^{-4}$ diameters over the free-stream speed, for 2000 steps. Errors of both velocity
  components in $L_1$, $L_2$ and $L_{\max}$, largest around the
  cylinder: "nearly second-order convergence", "globally and locally
  second-order accurate". No rates are tabulated; Fig. 9 shows the errors
  against a second-order line. The compiler's read-off from the plot,
  approximate: $L_{\max}$ falls from about $1.4\times10^{-1}$ to about
  $1.4\times10^{-2}$ while the spacing falls by a factor of about 3,
  slope about 2. Caveats (compiler's): self-convergence, not against an
  exact solution; a small domain and an early transient
  (0.2 convective time units); pressure is not measured.
* *Stationary cylinder* (§3.2, Table 1), $\mathrm{Re} = 40, 100, 300, 1000$:
  mean drag coefficients 1.53, 1.35, 1.36, 1.45 against Henderson's 1.54,
  1.35, 1.37, 1.51; Strouhal number and base suction graphical only.
* *NACA 0008 airfoil* (§3.3, Table 2), $\mathrm{Re} = 2000$ and 6000 at
  0° and 4°: drag and lift within 0.006 of Kunz & Kroo (e.g. lift 0.240
  against 0.234 at 6000 and 4°).
* *Sphere* (§3.4, Table 3), $\mathrm{Re} = 100$–350: recirculation
  length 0.84 at 100 (others 0.87–0.88), Strouhal number 0.135 at 300 and
  0.142 at 350; the mean drag curve is graphical only.
* *Impulsively started flat plate and cylinder* (§3.5): bubble length and
  drag history match vortex-particle and experimental data graphically;
  an impulsively started sphere at $\mathrm{Re} = 550$ is offered as a
  future benchmark without comparison data.
* *Bluegill sunfish pectoral fin and dragonfly* (§3.6): deforming and
  flapping demonstrations, qualitative only.

# Notation map

| Mittal et al. (2008) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$ | $\mathbf v$ ($v_x, v_y, v_z$) | cell-centre velocity; registry $u$ is the conserved state |
| $U_i$ | words (face velocity) | face-centre velocity |
| $u_i^*$, $\tilde u_i$, $\tilde U_i$, $U_i^*$ | words (intermediate velocity) | registry $u^*$ is a boundary derivative approximation |
| $p$, $p'$, $\rho$ | $p$, words (pressure correction), $\rho$ | |
| $\nu$ | words (kinematic viscosity) | registry $\nu$ is the CFL number |
| $N_i$, $D_i$, $\delta/\delta x_j$ | words | convective and diffusive terms, central difference |
| $\Delta$, $\Delta x_i$ | $h$, $h_x, h_y, h_z$ | |
| $\Delta t$, $n$ | $\Delta t$, $t^n$ | |
| $\mathrm{CFL}_{\max}$ | $\nu_{\max}$ | eq. 25 |
| GC, BI, IP | words | ghost node, boundary intercept, image point |
| $\Delta l$ | words (probe length) | |
| $\beta_i$ | words (interpolation weights) | registry $\beta_k$ are smoothness indicators |
| $C_1, \dots, C_8$, $[V]$ | words | trilinear coefficients, Vandermonde matrix |
| $\phi$ | words (generic variable) | registry $\phi_{\mathrm{IB}}$ is the Peskin kernel |
| $\hat n$, $\vec p$ | words | outward surface normal, element-to-node vector |
| $X_i$, $V_i$ | words | surface vertex position and velocity; registry $\mathbf X$, $\mathbf X_{\mathrm{IB}}$ differ |
| $Re_d$, $Re_c$, $Re_h$ | $\mathrm{Re}$ | length scale named in the text |
| $C_D$, $C_L$, $C_{pb}$, St | words | free-stream coefficients; registry $C_D$ is normalized by the post-shock flow |

# Pages created or updated

* Contributed to [Immersed-boundary methods](/methods/immersed-boundary-method.md) (batch-13 block).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2008-JCP-Mittal-101016jjcp200801028.pdf`.
   * **Version.** The publisher's version of record (Elsevier typeset
     PDF, 28 pages), not a preprint.
   * **Identity.** doi:10.1016/j.jcp.2008.01.028, printed on page 1 and
     checked on Crossref: J. Comput. Phys. 227(10):4825–4852, May 2008,
     same title and six authors. Received 15 February 2007, accepted 7
     January 2008.
   * **How it was read.** Text extraction, all sections; eqs. 3–13, 20–23
     and 25 checked on the page images; eq. A.5 read on the page image,
     where the text layer is wrong. Eq. A.2 (the trilinear coefficients in
     terms of nodal values) is garbled in the text layer and is not
     reproduced. The order of the image-point truncation error is taken as
     printed; eq. A.5 omits the derivative factors.
   * **Recorded as printed.** §3.1 speaks of "three grids" but lists and
     plots four; the sphere text compares parameters "for $Re_d = 40$ and
     150" while Table 3 lists 100 and 150; Fig. 9's caption says
     $L_\infty$ where the text says $L_{\max}$; "Siedel" for Seidel. The
     Neumann data used for the pressure correction on moving bodies are
     not stated.
   * **Reference list:** 65 entries, all merged. The key `mittal-2008`
     already existed (cited by baskaya-2024, natarajan-2022 and
     seshadri-2020). Kim, Kim & Choi (2001) is `kim-2001-b` and Peskin's
     1972 J. Comput. Phys. paper is `peskin-1972-b`; the bare keys hold
     other works. Two printed errors, verified on Crossref, are recorded
     in the entries' notes with the keys following the printed values:
     Felten & Lund is printed 2000 (Crossref: 2006, J. Comput. Phys.
     215:465–484; `felten-2000`), and Williamson's review is printed Annu.
     Rev. Fluid Mech. 8 (Crossref: 28:477–539; `williamson-1996`).
