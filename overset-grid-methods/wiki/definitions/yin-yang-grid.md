---
type: Definition
title: "Yin–Yang grid"
description: "Kageyama and Sato's overset grid for spheres and spherical shells: two congruent latitude–longitude patches, each 90° by 270° plus a buffer, in perpendicular polar frames related by an involution. It is orthogonal and quasi-uniform with no pole problem, reuses one solver and stencil set, rotates vectors by an angle ψ, and overlaps about 6%."
status: established
aliases: [Yin-Yang grid, Yin–Yang overset grid, spherical overset grid, n-grid and e-grid]
tags: [spherical-grid, overset-grid, geophysics, finite-difference, interpolation]
timestamp: 2026-11-02T11:28:00Z
---

# Yin–Yang grid

The Yin–Yang grid of [Kageyama & Sato (2004)](/sources/kageyama-2004.md) covers
a sphere with two geometrically identical component grids. Each is the
low-latitude part of a latitude–longitude grid in its own spherical polar
coordinates $(r,\theta,\phi)$, with colatitude $\theta$:
$$\Big(\frac{\pi}{4}-\delta\le\theta\le\frac{3\pi}{4}+\delta\Big)\cap\Big(-\frac{3\pi}{4}-\delta\le\phi\le\frac{3\pi}{4}+\delta\Big)$$
(Eq. (1)). This is a band 90° wide about the equator and 270° long. The
buffer $\delta$, proportional to the grid spacing, guarantees a minimum
overlap. The Yang grid (superscript $\mathrm e$) is the Yin grid (superscript
$\mathrm n$) expressed in a second polar frame whose axis lies in the Yin
equatorial plane (Fig. 2). Each component is therefore orthogonal and
quasi-uniform, with analytically known metrics and no pole. The two are
coupled as an [overset grid](/definitions/overset-grid.md): the border
points of each component are receptors interpolated from the other (§II).
The spherical-shell grid stacks the 2-D grid in $r$,
$r_{\mathrm{in}}\le r\le r_{\mathrm{out}}$ (Fig. 3). The version read is the
arXiv preprint physics/0403123v1. The locators below are its sections and
equation numbers.

## Motivation: the pole problem

Kageyama & Sato (§I) separate two defects of the latitude–longitude grid:
- the **coordinate singularity** at the poles, which is benign and handled at
  negligible cost by l'Hospital's rule on the pole grid (as recalled from
  earlier work);
- the **grid convergence** near the poles, which is serious because it
  restricts the time step and forces a filter.

They estimate the filter's waste for a grid of angular spacing $\Delta$
(page-local). A quasi-uniform grid would need $4\pi/\Delta^2$ points, the
latitude–longitude grid has $2\pi^2/\Delta^2$, so a fraction
$(2\pi^2-4\pi)/2\pi^2=1-2/\pi\approx36\%$ of the information is discarded at
every step. In their latitude–longitude geodynamo code the FFT filter took
more than 30% of the run time.

Because the low-latitude band is free of both defects, two such bands
suffice. No single grid on the sphere is orthogonal and free of both
singularity and convergence, so the sphere must be decomposed. The authors
note that this can be done with patched grids (no overlap) or overset grids
(partial overlap); see [patched (zonal) grids](/definitions/patched-grid.md).

## Coordinate transformation

The Cartesian frames are related by (Eqs. (2), (4), (5))
$$\begin{pmatrix}x^{\mathrm e}\\y^{\mathrm e}\\z^{\mathrm e}\end{pmatrix}=\mathsf M\begin{pmatrix}x^{\mathrm n}\\y^{\mathrm n}\\z^{\mathrm n}\end{pmatrix},\qquad \mathsf M=\begin{pmatrix}-1&0&0\\0&0&1\\0&1&0\end{pmatrix},\qquad \mathsf M^{-1}=\mathsf M,$$
i.e. $(x^{\mathrm e},y^{\mathrm e},z^{\mathrm e})=(-x^{\mathrm n},z^{\mathrm n},y^{\mathrm n})$.
The map is symmetric: Yin and Yang play interchangeable roles.
$\det\mathsf M=+1$, so $\mathsf M$ is a rotation, by $\pi$ about the axis
$(0,1,1)/\sqrt2$ *(compiler check, not in the sources)*. In spherical
coordinates (Eqs. (6)–(9)):
$$r^{\mathrm e}=r^{\mathrm n},\quad \sin\theta^{\mathrm e}\cos\phi^{\mathrm e}=-\sin\theta^{\mathrm n}\cos\phi^{\mathrm n},\quad \sin\theta^{\mathrm e}\sin\phi^{\mathrm e}=\cos\theta^{\mathrm n},\quad \cos\theta^{\mathrm e}=\sin\theta^{\mathrm n}\sin\phi^{\mathrm n}.$$

**Discretization** (Eqs. (10)–(13)). Each component uses the same uniform
grid, $\theta_i=\theta_{\min}+i\,\Delta\theta$ ($i=0,\dots,N_\theta-1$) and
$\phi_j=\phi_{\min}+j\,\Delta\phi$ ($j=0,\dots,N_\phi-1$), with
$\Delta\theta=(\theta_{\max}-\theta_{\min})/(N_\theta-1)$ and $\Delta\phi$
likewise. The example of Fig. 1 uses $\Delta\theta=\Delta\phi=2\delta$.

## Consequences of the symmetry

Kageyama & Sato (§II) draw three consequences from the congruence of the two
components:

- **One solver, called twice.** The metric tensors at Yin point $(i,j)$ equal
  those at Yang point $(i,j)$. The same subroutine advances both components,
  and equations, formulas and libraries written for spherical polar
  coordinates apply unchanged on each.
- **One interpolation routine, called twice.** The donor stencil and
  coefficients that set the Yin border point $(i,j)$ from Yang points are
  exactly those that set the Yang border point $(i,j)$ from Yin points. The
  interpolation order and stencil width are not specified in the paper. See
  [inter-grid interpolation](/methods/inter-grid-interpolation.md).
- **Even domain decomposition.** The grid splits naturally into Yin and Yang
  and then into subdomains of each, which the authors find suited to
  massively parallel vector computers such as the Earth Simulator (§IV).

## Vector components

The Yin→Yang map is a rotation about the origin, so the radial component is
invariant and the horizontal components rotate by a local angle $\psi$
(Eqs. (14)–(16)):
$$\begin{pmatrix}v^{\mathrm e}_r\\v^{\mathrm e}_\theta\\v^{\mathrm e}_\phi\end{pmatrix}=\mathsf P\begin{pmatrix}v^{\mathrm n}_r\\v^{\mathrm n}_\theta\\v^{\mathrm n}_\phi\end{pmatrix},\qquad \mathsf P=\begin{pmatrix}1&0&0\\0&\cos\psi&-\sin\psi\\0&\sin\psi&\cos\psi\end{pmatrix},$$
with $\cos\psi=\hat{\boldsymbol\phi}^{\mathrm n}\cdot\hat{\boldsymbol\phi}^{\mathrm e}$
and $\sin\psi=-\hat{\boldsymbol\phi}^{\mathrm n}\cdot\hat{\boldsymbol\theta}^{\mathrm e}$.
Evaluated (Eqs. (20), (21) final members, (23)):
$$\cos\psi=-\sin\phi^{\mathrm e}\sin\phi^{\mathrm n},\qquad \sin\psi=-\frac{\cos\phi^{\mathrm e}}{\sin\theta^{\mathrm n}}=\frac{\cos\phi^{\mathrm n}}{\sin\theta^{\mathrm e}} .$$
The inverse (Eq. (24)) is obtained by interchanging the superscripts
$\mathrm n\leftrightarrow\mathrm e$ and equals $\mathsf P^T$. The
denominators $\sin\theta$ are bounded away from zero on both components,
since $\theta\in[\pi/4-\delta,3\pi/4+\delta]$ *(compiler check, not in the
sources)*.

## Overlap and minimum-overlap variants

- **Size of the basic grid** (§II–III). As $\delta\to0$, each component covers
  $\int_{\pi/4}^{3\pi/4}\sin\theta\,d\theta\int_{-3\pi/4}^{3\pi/4}d\phi=3\pi/\sqrt2\approx2.12\pi$
  of the unit sphere's $4\pi$. Even with vanishing buffer, the overlap is
  $(3\pi/\sqrt2-2\pi)/2\pi\approx6.1\%$ of the sphere. The four corners of
  each Mercator-rectangular component intrude most into the other.
- **Minimum-overlap dissections** (§III, Figs. 5–8). Any closed curve that cuts
  the sphere into two congruent halves defines a minimum-overlap Yin–Yang
  grid, and there are infinitely many. Two are shown: a "baseball" type and a
  "cube" type. Each component keeps its latitude–longitude grid but masks the
  points outside its non-rectangular half (the masked points become hole
  points; see [point classification](/definitions/point-classification.md)).
  The authors state that both variants mask the same number of points,
  because each unmasked area tends to $2\pi$. No parametrization of the cut
  curves is given.
- **Three-component variant** (§IV, Fig. 9). Three identical components, each
  $(\pi/4\le\theta\le3\pi/4)\cap(-\pi/2\le\phi\le\pi/2)$ in its own rotated
  frame, cover "about 1/3" of the sphere each and suit processor counts that
  are multiples of three. Each covers $\sqrt2\pi$, i.e. 0.354 of the sphere
  *(compiler check, not in the sources)*. The rotations and any buffer are
  not specified.

## Applications reported

Kageyama & Sato (§IV) report these results as statements, with details
deferred to other papers:
- A finite-difference Yin–Yang mantle-convection code (Boussinesq, infinite
  Prandtl number, uniform and variable viscosity) reproduced benchmark Nusselt
  numbers and mean velocities "within a few percent or even better".
- A geodynamo (MHD) code converted from their latitude–longitude code
  reproduced earlier results "with shorter calculation time". The conversion
  was "straightforward and rather easy since the base grid is common".

No grid sizes, overlap widths, interpolation orders or timings are given.

## Relation to other spherical grids

As recalled by Kageyama & Sato (§I), earlier composite spherical grids
include:
- Phillips' latitude–longitude grid capped by polar stereographic grids;
- two hemispheric stereographic grids overlapping at the equator in a global
  circulation model;
- two perpendicular spherical frames in an ocean model, the second used only
  as an auxiliary;
- the six-patch cubed sphere.

The authors claim the Yin–Yang grid is simpler in geometry and metrics than
these, and that it exploits the symmetry of the two frames fully. They call
the cubed sphere "an overset grid".

## Qualifications

- **Version read.** The arXiv v1 preprint; the published G-cubed article
  (vol. 5, issue 9, article 2004GC000734) may differ in wording, numbering
  and figures.
- **Scope.** The paper contains no interpolation-accuracy, conservation or
  stability analysis, and it does not discuss whether the interpolation
  across the 6% overlap conserves mass.
- **Printed slips** (the final results quoted above are correct):
  - **Eq. (3)** prints $(x^{\mathrm e},y^{\mathrm e},z^{\mathrm e})^T=\mathsf M(x^{\mathrm n},z^{\mathrm n},y^{\mathrm n})^T$,
    which contradicts Eq. (2). The right-hand vector must be
    $(x^{\mathrm n},y^{\mathrm n},z^{\mathrm n})^T$.
  - **Eq. (21)**: the first two printed members equal
    $+\hat{\boldsymbol\phi}^{\mathrm n}\cdot\hat{\boldsymbol\theta}^{\mathrm e}=-\sin\psi$.
    The sign flips silently to the correct final members. Projecting random
    vectors on both bases confirms $\cos\psi$, the final $\sin\psi$ and
    $\mathsf P$, and that Eq. (24) times Eq. (23) is the identity
    *(compiler check, not in the sources)*.
  - **Eq. (25)** states "$\mathsf P^2=1$" as expressing the complementary
    relation. As a matrix identity this is false: $\mathsf P^2$ is the
    rotation by $2\psi$, not the identity at generic points *(compiler check,
    not in the sources)*. What holds is $\mathsf P^{-1}=\mathsf P^T$, i.e.
    the Yin→Yang map composed with the superscript-interchanged map is the
    identity.

# Citations

- [Kageyama & Sato (2004)](/sources/kageyama-2004.md) — arXiv physics/0403123v1: §I (pole problem, 36% estimate, filter cost, earlier spherical grids), §II (Eqs. (1)–(13), Figs. 1–3, symmetric solver and interpolation), §III (Eqs. (14)–(25), Fig. 4, overlap estimate, Figs. 5–8), §IV (applications, decomposition, Fig. 9).
