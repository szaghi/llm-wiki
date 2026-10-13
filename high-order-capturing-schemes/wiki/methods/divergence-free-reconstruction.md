---
type: Method
title: "Divergence-free reconstruction of face-centred magnetic fields"
description: "Balsara's reconstruction for Yee-staggered MHD: from the normal component of B and its moments on the six faces of a zone, build a polynomial vector field inside the zone that is divergence-free everywhere and matches the faces; closed form at orders 2–4, energy-minimizing where face data leave freedom, and the source of a unique zone-centred field."
status: established
aliases: [divergence-free reconstruction, divergence-free prolongation, Balsara reconstruction]
tags: [mhd, divergence-free, constrained-transport, reconstruction, staggered, amr]
timestamp: 2026-10-13T00:00:00Z
---

# Divergence-free reconstruction of face-centred magnetic fields

**The problem** ([Balsara (2004)](/sources/balsara-2004.md), §1). A
Yee-staggered scheme evolves the normal field component on each face
([constrained transport](/methods/constrained-transport.md)). Four
questions are then left open:
1. how to obtain the zone-centred field;
2. whether to limit the derived zone field or the primal face field;
3. what to do about the jump in the normal field that Powell's
   eight-wave model needs;
4. how to get edge electric fields without averaging face fluxes in space.

A reconstruction of the whole zone field from face data, divergence-free
by construction, answers the first three.

## Second order

([Balsara (2001)](/sources/balsara-2001.md), §III, eqs. 3.5–3.39, where
the formulas first appear, with minmod-limited face slopes; restated in
[Balsara (2004)](/sources/balsara-2004.md), §3.1, eqs. 3.1–3.17, whose
equation numbers are used below.) Each
face carries the normal component and its two transverse slopes. Inside
the zone, in local coordinates centred on the zone, the field is
$$B_x = \hat B_{x,0} + \hat B_{x,x}\,x + \hat B_{x,y}\,y + \hat B_{x,z}\,z + \hat B_{x,xx}\,x^2 + \hat B_{x,xy}\,xy + \hat B_{x,xz}\,xz,$$
and cyclically for $B_y$ and $B_z$. Requiring $\nabla\cdot\mathbf B = 0$
at every point gives four constraints:
$$\hat B_{x,x} + \hat B_{y,y} + \hat B_{z,z} = 0,\qquad 2\hat B_{x,xx} + \hat B_{y,xy} + \hat B_{z,xz} = 0,$$
and the two cyclic analogues of the second. Matching the six faces then
fixes every coefficient in closed form. For example
$\hat B_{x,x} = (B^+_x - B^-_x)/h_x$, where $B^\pm_x$ are the face
values, and $\hat B_{x,xx} = -\tfrac12(\hat B_{y,xy} + \hat B_{z,xz})$.
* **A unique zone field.** The zone average is
  $$\langle B_x\rangle_i = \tfrac12\left(B^+_x + B^-_x\right) - \hat B_{x,xx}\frac{h_x^2}{6},$$
  not the arithmetic mean of the two faces (eq. 3.17). The correction need
  not be small at strong oblique shocks, especially in low-β plasma. This
  is the value used for the pressure.
* **Continuity.** $B_x$ is continuous across $x$-faces by construction, so
  no eight-wave model is needed. The tangential components jump, which
  keeps upwinding in the Riemann solver (§3.1).
* **Geometry.** Volumetric coordinates map the divergence in cylindrical
  and spherical meshes onto the Cartesian form, so the same formulas
  apply. A linear version also exists on tetrahedra (§4, Appendix C).
* **Pressure positivity.** In a low-β blast (ambient plasma beta
  $2.51\times10^{-4}$) the pressure stays positive where the fast shock
  runs oblique to the mesh. The author credits this to the reconstructed
  zone field. Arithmetic-mean zone fields gave a large pre-shock pressure
  drop in Tóth's comparison (§7.3;
  [MHD blast wave](/benchmarks/mhd-blast-wave.md);
  [positivity preservation](/properties/positivity-preserving.md)).

## Third and fourth order

([Balsara (2009b)](/sources/balsara-2009-b.md), §2; author manuscript.)
The face data become Legendre moments of the normal component, with 3, 6
and 10 moments per face at orders 2, 3 and 4, and the zone field becomes a
Legendre expansion with selected quartic terms. Matching the face
moments fixes most coefficients in closed form. The coefficients the
faces leave free are chosen to minimize the zone's magnetic energy. At
fourth order, for example, $\hat B_{x,xxxx} = -\tfrac14(\hat B_{y,xxxy} + \hat B_{z,xxxz})$
(eq. 11). The formulas must be applied in the printed order, from quartic
down to constant terms (eqs. 10–18). The only compatibility condition is
that the net flux through the six faces vanishes (eq. 18).
* Some coefficients exist only because of the constraint. They enter
  fluxes and Riemann problems but are not evolved
  ([Balsara et al. (2009)](/sources/balsara-2009.md), §2.3).
* The reconstruction is also an AMR prolongation. Ratio 2 is given in
  Balsara's 2001 paper, at second order (see the AMR section below). For ratio 3 the 9 degrees of freedom per face are
  obtained by relaxing one of the 10 fourth-order moments, and products of
  2 and 3 follow by recursion (Balsara 2009b, §2, observation 2;
  [high-order AMR](/methods/high-order-amr.md)).
* **Schemes built on it.**
  * RK-WENO finite volume with a face flux whose dissipation matrix is
    frozen at the face barycentre, so the flux integrates exactly over the
    face. It reaches design order up to fourth on a magnetized vortex and
    a 3D torsional Alfvén wave (Balsara 2009b, §§3–4, Tables I–II;
    [Alfvén-wave tests](/benchmarks/circularly-polarized-alfven-wave.md)).
    With RK3 the step must shrink faster than the mesh to show fourth
    order. The paper states a factor 0.396 per doubling, which matches
    $2^{-4/3}$ for $\Delta t$ rather than for the Courant number (a
    compiler's reading).
  * One-step [ADER](/methods/ader.md)-WENO
    ([Balsara et al. (2009)](/sources/balsara-2009.md)).

## On adaptive meshes

([Balsara (2001)](/sources/balsara-2001.md), §§III–VI.) The
second-order reconstruction is the first piece of a complete
divergence-free AMR scheme on a Yee mesh.
* **1D limit.** With variation along $x$ only, the reconstruction reduces
  to van Leer's MUSCL, so the fluxes coincide with a zone-centred TVD
  scheme (eq. 3.40).
* **Prolongation, ratio 2.** Where a coarse face overlies four fine faces,
  its profile gains a bilinear term fitted exactly to the four fine
  values, and the zone polynomial gains twelve terms under three further
  divergence constraints (eqs. 4.1–4.19). The system is under-determined;
  three coefficients are fixed by a simplifying choice that reduces the
  prolongation to the reconstruction when the cross terms vanish
  (eqs. 4.12–4.14), not by the energy minimization of the third- and
  fourth-order closure. Ratios 4 and 8 follow by recursion.
* **Restriction** averages the four fine face fields onto the coarse face
  (eq. 5.4).
* **Electric-field correction.** After the fine steps, coarse faces that
  share only an edge with the fine patch are corrected by the difference
  between the space–time average of the fine edge fields and the coarse
  one (eqs. 5.5–5.7): Berger–Colella refluxing moved from faces to edges
  ([high-order AMR](/methods/high-order-amr.md)). That this keeps the
  coarse field divergence-free is argued, not proved, and no run without
  the correction is shown.
* A divergence-*preserving* variant, which drops the constraint and
  prolongs a nonzero divergence faithfully, is suggested for nearly
  incompressible flow (§IV item 10).

**Scope.** A cheaper alternative builds no volumetric reconstruction:
finite-difference cell variables plus finite-volume face fields
([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md);
[constrained transport](/methods/constrained-transport.md)). For DG-like
schemes the same group reports that skipping the constraint-preserving
reconstruction gives instability (as cited by
[Balsara et al. (2023)](/sources/balsara-2023.md), §1). The curl
analogue is the [curl-preserving reconstruction](/methods/curl-preserving-reconstruction.md).

**Later uses (batch 15).** *The face-flux original of the edge
correction* ([Berger & Colella (1989)](/sources/berger-1989.md), §3,
eqs. 2–5). For a coarse cell next to a fine grid, the coarse flux through
the shared face is replaced by the fine fluxes through the
$r_{\mathrm{AMR}}$ fine faces summed over the $r_{\mathrm{AMR}}$ fine steps
and divided by $r_{\mathrm{AMR}}^2$, through a flux register initialized
with minus the coarse flux. The electric-field correction above, a
$\tfrac14$ sum over two fine edges and two fine half-steps, has the same
structure at $r_{\mathrm{AMR}} = 2$, with edges in place of faces. The
1989 algorithm is for the Euler equations and has no magnetic field.

# Citations

1. [Balsara (2004)](/sources/balsara-2004.md), §§1, 3, 4, 7.3, Appendix C.
2. [Balsara (2009b)](/sources/balsara-2009-b.md), §§2–5 (author manuscript).
3. [Balsara et al. (2009)](/sources/balsara-2009.md), §2.3.
4. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1–4.
5. [Balsara et al. (2023)](/sources/balsara-2023.md), §1.
6. [Balsara (2001)](/sources/balsara-2001.md), §§III–VI.
7. [Berger & Colella (1989)](/sources/berger-1989.md), §3.
