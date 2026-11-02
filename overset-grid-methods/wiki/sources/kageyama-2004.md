---
type: Source
title: "Kageyama & Sato (2004) — \"Yin-Yang grid\": an overset grid in spherical geometry"
description: "Introduces the Yin–Yang grid, two identical low-latitude latitude–longitude patches in perpendicular spherical coordinates that overlap to cover the sphere without pole singularity or grid convergence, with the Cartesian involution and vector-rotation formulas between the two components and minimum-overlap variants."
resource: "doi:10.1029/2004GC000734"
source_kind: paper
authors: [Kageyama A., Sato T.]
year: 2004
venue: "Geochem. Geophys. Geosyst. 5(9):2004GC000734"
local_file: "/home/stefano/papers/mosaic/overset-chimera/2004_Crossref_Geochemistry_Geophysics_Geosystems_Kageyama_YinYang_grid_An_overset_grid_in_spherical_geometry.pdf"
tags: [spherical-grid, overset-grid, geophysics]
timestamp: 2026-11-02T11:28:00Z
---

# Summary

Kageyama and Sato propose the **[Yin–Yang grid](/definitions/yin-yang-grid.md)**, a spherical
[overset grid](/definitions/overset-grid.md) made of two geometrically identical component grids.
Finite-difference geodynamo and mantle-convection codes on the latitude–longitude grid suffer from
the pole singularity, which is benign, and from grid convergence near the poles, which forces a
filter to relax the time step. The authors estimate that such a filter discards about $36\,\%$ of
the grid's information, and that it costs more than $30\,\%$ of the run time in their geodynamo
code.

Each component is the low-latitude part of a latitude–longitude grid,
$\theta\in[\pi/4-\delta,3\pi/4+\delta]$, $\phi\in[-3\pi/4-\delta,3\pi/4+\delta]$, with a buffer
$\delta$ proportional to the spacing that guarantees a minimum overlap. The Yang component is the
same patch in a second spherical system whose polar axis lies in the Yin equatorial plane. The
Cartesian relation $(x^{\mathrm e},y^{\mathrm e},z^{\mathrm e})=(-x^{\mathrm n},z^{\mathrm n},y^{\mathrm n})$
is an involution, $\mathsf M^{-1}=\mathsf M$. Both components are orthogonal and quasi-uniform with
analytic metrics, so the equations keep their spherical-polar form. One solver routine and one
[inter-grid interpolation](/methods/inter-grid-interpolation.md) routine serve both components,
which fill their border ([fringe](/definitions/fringe-point.md)) points from each other.

The paper derives the transformation of vector components: $v_r$ is invariant, and the horizontal
components rotate by a local angle $\psi$. The basic grid overlaps about $6\,\%$ of the sphere in the
limit of fine spacing. Minimum-overlap variants follow from any closed curve that cuts the sphere
into two congruent halves ("baseball" and "cube" types), at the price of masking points. A
three-component variant is sketched, and [patched grids](/definitions/patched-grid.md) are named as
the non-overlapping alternative. No numerical results are shown. The paper reports that a Yin–Yang
mantle-convection code matched benchmark values "within a few percent or even better", and that a
converted geodynamo code reproduced earlier results in less time.

# Version read

The arXiv preprint physics/0403123v1 [physics.geo-ph] of 25 March 2004 (REVTeX layout), not the
G-cubed version of record. It has 15 pages: text and references on pp. 1–6, then Figs. 1–9 one
per page. The printed title is 'The "Yin-Yang Grid": An Overset Grid in Spherical Geometry'; the
authors and their order match Crossref. The published text was not available for comparison, so
the section, equation and figure numbers cited here are those of arXiv v1 and may differ from the
journal article. The article identifier 2004GC000734 (volume 5, issue 9) is that of the Crossref record, not of the version
read.

# Key claims

1. The latitude–longitude grid has two numerical problems. The coordinate singularity at the
   poles is not a real singularity and is handled cheaply by l'Hospital's rule on the pole points.
   Grid convergence near the poles is the more serious problem because of the time-step
   restriction. (§I) **Stated**
2. A filter that makes a latitude–longitude grid of angular spacing $h$ effectively quasi-uniform
   keeps $4\pi/h^2$ effective points out of $2\pi^2/h^2$, so it discards a fraction
   $(2\pi^2-4\pi)/2\pi^2\approx36\,\%$ of the information at every step. (§I) **Derived**
3. In the authors' latitude–longitude geodynamo code the FFT filter takes more than $30\,\%$ of the
   execution time. (§I) **Stated**
4. The low-latitude part of the latitude–longitude grid is orthogonal, with simple metric tensors
   and quasi-uniform spacing. The redundancy of the grid comes only from high latitudes. (§I)
   **Stated**
5. No single grid covers the whole sphere orthogonally and without singularity or grid
   convergence. The sphere must therefore be split into subregions, either patched (no overlap,
   ref. [37]) or overset (partial overlap, ref. [8]). (§I) **Stated**
6. The Yin component is
   $\{\pi/4-\delta\le\theta\le3\pi/4+\delta\}\cap\{-3\pi/4-\delta\le\phi\le3\pi/4+\delta\}$. The
   Yang component is defined by the same rule in a second spherical system perpendicular to the
   first. (§II, Eq. 1, Fig. 2) **Derived**
7. For $\delta\to0$ one component covers $3\pi/\sqrt2\approx2.12\pi$ of the unit sphere, about half
   of $4\pi$. (§II) **Derived**
8. $(x^{\mathrm e},y^{\mathrm e},z^{\mathrm e})=(-x^{\mathrm n},z^{\mathrm n},y^{\mathrm n})$
   (Eq. 2), that is
   $(x^{\mathrm e},y^{\mathrm e},z^{\mathrm e})^T=\mathsf M(x^{\mathrm n},y^{\mathrm n},z^{\mathrm n})^T$
   with $\mathsf M$ of Eq. (4) and $\mathsf M^{-1}=\mathsf M$ (Eq. 5): the transformation is
   symmetric. (§II) **Derived**
9. Each component is discretized uniformly, $\theta_i=\theta_{\min}+i\,\Delta\theta$ and
   $\phi_j=\phi_{\min}+j\,\Delta\phi$, with
   $\Delta\theta=(\theta_{\max}-\theta_{\min})/(N_\theta-1)$ and
   $\Delta\phi=(\phi_{\max}-\phi_{\min})/(N_\phi-1)$. Fig. 1 uses $\Delta\theta=\Delta\phi=2\delta$.
   (§II, Eqs. 10–13) **Derived**
10. The two components are identical and complementary. Hence the interpolation coefficients and
    relative stencils that fill a Yin border point are exactly those for the Yang border point with
    the same indices, and one interpolation routine is called twice. The interpolation scheme
    itself is not specified. (§II) **Derived**
11. The metric tensors at a Yin point equal those at the Yang point with the same indices, so one
    fluid-solver routine is called twice per step. (§II) **Derived**
12. Equations, formulas, libraries and tools written in spherical polar coordinates apply directly
    on each component. (§II) **Stated**
13. The 3-D spherical-shell grid is the 2-D grid stacked in $r$ between $r_{\mathrm{in}}$ and
    $r_{\mathrm{out}}$. (§II, Fig. 3) **Stated**
14. For vectors, $v_r^{\mathrm n}=v_r^{\mathrm e}$ and the horizontal components rotate by the
    local angle $\psi$ (Eq. 14), with
    $\cos\psi=\hat{\boldsymbol\phi}^{\mathrm n}\cdot\hat{\boldsymbol\phi}^{\mathrm e}$ (Eq. 15)
    and $\sin\psi=-\hat{\boldsymbol\phi}^{\mathrm n}\cdot\hat{\boldsymbol\theta}^{\mathrm e}$
    (Eq. 16). (§III, Fig. 4) **Derived**
15. $\cos\psi=-\sin\phi^{\mathrm e}\sin\phi^{\mathrm n}$ (Eq. 20) and
    $\sin\psi=-\cos\phi^{\mathrm e}/\sin\theta^{\mathrm n}=\cos\phi^{\mathrm n}/\sin\theta^{\mathrm e}$
    (Eq. 21, final members). (§III) **Derived**
16. $(v_r^{\mathrm e},v_\theta^{\mathrm e},v_\phi^{\mathrm e})^T=\mathsf P(v_r^{\mathrm n},v_\theta^{\mathrm n},v_\phi^{\mathrm n})^T$
    with $\mathsf P$ of Eq. (23). Its inverse (Eq. 24) follows by interchanging the superscripts
    $\mathrm n\leftrightarrow\mathrm e$. (§III) **Derived**
17. "$P^2=1$" (Eq. 25) "indicates the complemental relation". (§III) **Stated** (see Printed
    slips)
18. As $\Delta\theta=\Delta\phi\to0$ and $\delta\to0$, the basic grid still overlaps about $6\,\%$
    of the sphere, $(3\pi/\sqrt2-2\pi)/2\pi\approx0.061$. The four corners of each component
    intrude most into the other. (§III) **Derived**
19. Any closed curve that cuts the sphere into two identical parts gives a minimum-overlap Yin–Yang
    grid, and there are infinitely many. Two are shown: a "baseball" type (Figs. 5a, 6a, 7) and a
    "cube" type (Figs. 5b, 6b, 8). (§III) **Shown** (geometrically)
20. Non-rectangular components require masking some points. The baseball and cube variants mask
    the same number, since each unmasked area is $2\pi$ when the overlap is negligible. (§III)
    **Stated**
21. A finite-difference mantle-convection code on the basic grid (Boussinesq, infinite Prandtl
    number, uniform and variable viscosity) passed the "standard benchmark tests of the mantle convection" [39]: Nusselt number and
    mean velocity agree with other values "within a few percent or even better" [48]. (§IV)
    **Stated** (results not shown)
22. A Yin–Yang geodynamo code converted from the latitude–longitude code reproduced the earlier
    results "with shorter calculation time". The conversion was "straightforward and rather easy
    since the base grid is common". (§IV) **Stated** (no timings)
23. The two-component structure leads naturally to even-numbered domain decompositions, and the
    grid suits massively parallel vector computers. (§IV; Abstract) **Stated**
24. A three-component grid of identical patches
    $\{\pi/4\le\theta\le3\pi/4\}\cap\{-\pi/2\le\phi\le\pi/2\}$, each "about 1/3" of the sphere, could
    suit processor counts that are multiples of three. (§IV, Fig. 9) **Stated**

# Printed slips

- **Eq. (3)** prints $(x^e,y^e,z^e)^T=M\,(x^n,z^n,y^n)^T$. With $M$ of Eq. (4) this gives
  $(-x^n,y^n,z^n)$, which contradicts Eq. (2). The right-hand vector must be $(x^n,y^n,z^n)^T$;
  Eq. (2) and Eqs. (6)–(9) agree with each other *(compiler check, not in the sources)*.
- **Eq. (21), intermediate members.** The first printed line,
  $\sin\psi=\cos\theta^e\cos\phi^e\sin\phi^n-\sin\theta^e\cos\phi^n$, is
  $+\hat\phi^n\cdot\hat\theta^e=-\sin\psi$ by Eqs. (16), (18)–(19). The second line equals it. The
  final members ($-\cos\phi^e/\sin\theta^n=\cos\phi^n/\sin\theta^e$) carry the opposite, correct
  sign. The sign is flipped silently between lines 2 and 3; Eqs. (20), (21) final, (23) and (24)
  are correct *(compiler check, not in the sources: evaluated at random points)*.
- **Eq. (25)** prints "$P^2=1$". $\mathsf P$ of Eq. (23) is a rotation by $\psi$ in the horizontal
  plane, so $\mathsf P^2$ is the rotation by $2\psi$ and differs from the identity wherever
  $\sin\psi\neq0$. What holds is Eq. (24), $\mathsf P^{-1}=\mathsf P^T$: the Yin→Yang map composed
  with the superscript-interchanged Yang→Yin map is the identity *(compiler check, not in the
  sources)*.
- References: ref. [43] prints the editor as "J.F. Thomposon"; ref. [34] "octapole"; ref. [27]
  "Phy. Rev. Lett.".

# Notation map

| Kageyama & Sato (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| superscripts $n$, $e$ ("n-grid", "e-grid") | superscripts $\mathrm n$, $\mathrm e$ | upright in the registry; **italic $n$ is the time level, $e$ the error** |
| $\ell\in\{n,e\}$ (component label) | grid index $k$ | |
| $(r,\theta,\phi)$ | $(r,\theta,\phi)$ | agree; $\theta$ is colatitude |
| $r_i$, $r_o$ | $r_{\mathrm{in}}$, $r_{\mathrm{out}}$ | |
| $\delta$ | $\delta$ | agree (buffer angle) |
| $\Delta$ (spacing of a full latitude–longitude grid, §I) | $h$ | |
| $\Delta\theta$, $\Delta\phi$, $N_\theta$, $N_\phi$ | same | agree |
| grid indices $j$, $k$ (Eqs. 10–11) | $\mathbf i=(i,j)$, as in claim 9 | **$k$ is the grid index in the registry** |
| $M$ | $\mathsf M$ | **$M$ is the Mach number in the registry**; $\mathsf M$ is a rotation by $\pi$ about $(0,1,1)/\sqrt2$ *(compiler check, not in the sources)* |
| $P$ | $\mathsf P$ | orthogonal, $\mathsf P^{-1}=\mathsf P^T$ |
| $\psi$ | $\psi$ | agree |
| $\hat x^\ell$, $\hat\theta^\ell$, $\hat\phi^\ell$ | unit vectors of component $k$ | page-local |
| $v_r$, $v_\theta$, $v_\phi$ | spherical vector components | |
| "horizontal boundary condition", "internal boundary condition", border points | $\mathcal R_k$ | the border points of each component are receptors |
| "stencils", "interpolation coefficients" | $\mathcal S_{\mathbf i}$, $\alpha_{\mathbf j}$ | width $q$ and order not stated |
| "mask" | $\mathcal H_k$ | no numeric mask convention given |

# Reference list

50 printed references, numbered [1]–[50] in alphabetical order. All 50 are merged complete into the
[bibliography](/bibliography.md) with `citedby` kageyama-2004. Ref. [31] is printed "in press" and
ref. [48] "submitted" (keyed by the year of that form). Ref. [39] is the only
one with a printed DOI. Ref. [10] prints "Christensen, U. R., et al.". Refs. [22]–[24] share author
and year and take suffixes. There are no printed duplicates or unparseable items.

# Pages created or updated

Chunk 1 (2026-11-02). This source is cited on:

- [Fringe (receptor) points and overlap width](/definitions/fringe-point.md)
- [Overset (Chimera) grid](/definitions/overset-grid.md)
- [Patched (zonal) grids](/definitions/patched-grid.md)
- [Point classification and the iblank mask](/definitions/point-classification.md)
- [Yin–Yang grid](/definitions/yin-yang-grid.md)
- [Inter-grid interpolation](/methods/inter-grid-interpolation.md)
