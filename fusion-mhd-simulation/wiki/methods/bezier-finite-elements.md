---
type: Method
title: "Bézier–Hermite finite elements with toroidal Fourier harmonics"
description: "JOREK's spatial discretization: isoparametric bicubic Bézier patches in the poloidal plane, written in nodal cubic-Hermite form with four degrees of freedom per node and element-dependent scale factors, combined with a real toroidal Fourier series; flux-aligned grids, convergence orders, the toroidally varying JOREK3D geometry, and the G1-versus-C1 labelling, closed by fiat as a difference of terminology."
status: established
aliases: [Hermite-Bézier elements, bicubic Bézier elements, Czarny–Huysmans elements, JOREK finite elements, G1 Bézier elements]
tags: [finite-elements, spectral, numerics]
timestamp: 2026-10-16T23:45:00Z
---

# Bézier–Hermite finite elements with toroidal Fourier harmonics

[JOREK](/software/jorek.md) discretizes the poloidal plane with
isoparametric bicubic Bézier quadrilaterals and the toroidal direction with a
real Fourier series; the test and basis functions are tensor products
$N(R,Z,\phi)=N^{\mathrm{pol}}(\hat s,\hat t)\,N^{\phi}(\phi)$ on
$\Omega=\Omega_{\mathrm{pol}}\otimes[0,2\pi)$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.1;
[Bhole et al. (2023)](/sources/bhole-2023.md), §3.3). Here
$(\hat s,\hat t)\in[0,1]^2$ are the reference coordinates of one element. The
element was introduced by Czarny and Huysmans (2008) as a generalization of the
isoparametric bicubic Hermite elements of HELENA; the papers of this bundle
restate it ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 51–54;
[Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 41–44, §3.3.3) and use it
throughout ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), App. A;
[Artola et al. (2021)](/sources/artola-2021.md), Table 1;
[Isernia et al. (2023)](/sources/isernia-2023.md), §II A;
[Korving et al. (2023)](/sources/korving-2023.md), §II C).

## Geometry: the Bézier patch

The cubic Bernstein polynomials are
$$B_i^3(\hat s)=\binom{3}{i}\hat s^{\,i}(1-\hat s)^{3-i},\qquad i=0,\dots,3,$$
and an element is the tensor-product patch
$$\mathbf X(\hat s,\hat t)=\big(R,Z\big)(\hat s,\hat t)=\sum_{i,j=0}^{3}\mathbf P_{ij}\,B_i^3(\hat s)\,B_j^3(\hat t)$$
with sixteen control points $\mathbf P_{ij}$
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 51–53). The element is
isoparametric: every physical variable is expanded in the same basis as the
geometry (Eq. 53).

## Nodal form: four degrees of freedom per node

The sixteen control values of a patch are linear functions of four quantities
at each of its four vertices: the value, the two first derivatives along the
element directions and the mixed second derivative
([Bhole et al. (2023)](/sources/bhole-2023.md), §3.3.2). With the 1D cubic
Hermite functions
$$H^0(z)=(1+2z)(1-z)^2,\qquad H^1(z)=z(1-z)^2,$$
the basis of vertex 1 is $H_1^0=H^0(\hat s)H^0(\hat t)$,
$H_1^1=H^1(\hat s)H^0(\hat t)$, $H_1^2=H^0(\hat s)H^1(\hat t)$,
$H_1^3=H^1(\hat s)H^1(\hat t)$; the other vertices follow from
$\hat s\to1-\hat s$ and/or $\hat t\to1-\hat t$. A field $f$ is represented on
element $e$ as
$$f\big|_e(\hat s,\hat t)=\sum_{v=1}^{4}\sum_{o=0}^{3}f_v^{\,o}\,\sigma^{e}_{v,o}\,H_v^{o}(\hat s,\hat t)$$
([Bhole et al. (2023)](/sources/bhole-2023.md), Eqs. 43–44;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eq. 54, which writes the
same sum with $k,l=1,\dots,4$). The nodal unknowns $f_v^{\,o}$ are **shared**
by all elements meeting at the node; the scale factors $\sigma^e_{v,o}$ are
**element-specific**. In Bhole et al. the shared derivatives are taken with
respect to arc length $(\ell_1,\ell_2)$ along the two grid directions, so
$$\sigma^e_{v,0}=1,\quad \sigma^e_{v,1}=\pm\Big(\frac{\mathrm d\ell_1}{\mathrm d\hat s}\Big)_v,\quad \sigma^e_{v,2}=\pm\Big(\frac{\mathrm d\ell_2}{\mathrm d\hat t}\Big)_v,\quad \sigma^e_{v,3}=\sigma^e_{v,1}\sigma^e_{v,2},$$
with the sign set by the orientation of the element relative to the reference
element. (Bhole et al. factor each derivative through an intermediate
"parametric" trapezoid coordinate; the product is the arc-length derivative
written here.) On an annulus with $\ell_1=r$, $\ell_2=r\theta$ the factors
are $\sigma^{e}_{1}=\pm\delta r_k$ and $\sigma^{e}_{2}=\pm r_k\,\delta\theta_l$
for the element $[r_k,r_{k+1}]\times[\theta_l,\theta_{l+1}]$
([Bhole et al. (2023)](/sources/bhole-2023.md), §3.3.3). Each variable
therefore carries four degrees of freedom per node
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.1;
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md), App. A). Local
refinement splits an element into two or four sub-elements
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.1).

## Toroidal direction

The toroidal factor is a real Fourier series,
$N^\phi\in\{1\}\cup\{\cos n\phi,\sin n\phi\}$
([Bhole et al. (2023)](/sources/bhole-2023.md), §3.3.1). In
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§3.1.3) the number of
toroidal basis functions counts cosines and sines separately and is
therefore odd, $N_{\mathrm{tor}}=2n_{\max}+1$ in this page's convention; a
periodicity keeps only multiples $n=0,k,2k,\dots$ of a chosen integer $k$.
The toroidal integrals of the weak form are sums over poloidal planes or an
FFT; the number of planes must be at least $2(N_{\mathrm{tor}}-1)$ for
de-aliasing, and powers of two are fastest with FFTW (§3.1.3, §3.4).

**Toroidally varying geometry (JOREK3D).** For stellarators the poloidal
geometry itself gets a Fourier expansion,
$$\{R,Z\}(\hat s,\hat t,\phi)=\sum_{n=1}^{N_{\mathrm{geo}}}\sum_{i,j=1}^{4}\{R,Z\}_{ijn}\,B_{ij}(\hat s,\hat t)\,Z^{c}_n(\phi),$$
with $Z^c_1=1$ and cosines and sines of multiples of the geometry
periodicity for $n>1$
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), Eq. A1). Geometry and
physics carry separate mode counts and periodicities, so a full-torus physics
run works on a five-periodic geometry (App. A); see
[JOREK3D](/software/jorek3d.md).

## Weak form and auxiliary variables

The equations are projected by Galerkin's method and integrated by parts so
that only first derivatives of the unknowns appear; natural boundary
conditions enter through the boundary integrals
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 17–20, 55). Second
derivatives are avoided by carrying the toroidal current $j=\Delta^*\psi$ and
the vorticity $\varpi$ as additional unknowns defined by their own weak
equations ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), Eqs. 38–39;
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II, where the only
remaining second derivatives sit in the hyperviscosity term). Nikulsin et
al. give the continuity class as the reason: the elements are only $G^1$, so
the vacuum potential $\chi$ of the stellarator model is represented
analytically by [Dommaschk potentials](/methods/dommaschk-potentials.md)
rather than in the element basis, which would make the advective terms
discontinuous (§II end, §III).

## Grids

The data structures admit unstructured grids; in practice the grids are
flux-surface aligned and structured per topological block (no X-point,
single or double X-point), built from a first Grad–Shafranov solve on a polar
or rectangular grid and extendable to the true first wall
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.2, §3.1.2;
[Bhole et al. (2023)](/sources/bhole-2023.md), §3.3.3, Fig. 3;
[Korving et al. (2023)](/sources/korving-2023.md), §II C). The polar grid has
a geometric singularity at the magnetic axis, treated in a separate
regularization (cited by [Bhole et al. (2023)](/sources/bhole-2023.md),
§3.3.3; [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5). Divertor work
needs about 1 mm resolution along the field near the strike points; Korving et
al. used 0.74 mm along and 8.1 mm across it (§II C, Fig. 2).

Grid sizes in the chunk-2 JOREK applications:
- AUG EDA pedestal: 214 radial (axis to wall) × 354 poloidal elements,
  packed so that one radial element spans 1.28 mm in the pedestal, with 64
  toroidal planes for $n=0$–13; this resolves a realistic
  $\kappa_\parallel/\kappa_\perp\sim10^9$
  ([Cathey et al. (2023)](/sources/cathey-2023.md), §2.2). With
  $N_{\mathrm{tor}}=27$ in this page's counting, 64 planes exceed the
  de-aliasing minimum of 52 (compiler's check).
- ITER current quench: a polar grid of 100×200 bicubic elements whose
  boundary follows the first wall but not the divertor details
  ([Artola et al. (2022)](/sources/artola-2022.md), §2, Fig. 1).
- Double tearing mode: 120 radial × 64 poloidal flux-aligned cells, $n=0$–15
  ([Nardon et al. (2023b)](/sources/nardon-2023-b.md), §II).
- ITER SPI: an X-point grid whose ideal-wall boundary is the thin-wall
  equivalent of the blanket modules, $n=0$–11
  ([Hu et al. (2023)](/sources/hu-2023.md), §2.2;
  [Hu et al. (2024)](/sources/hu-2024.md), §2.1).
- JT-60SA: a double-X-point grid on which JOREK re-solves the imported
  Grad–Shafranov equilibrium, with the core current smoothed at fixed
  4.6 MA ([Cathey et al. (2024)](/sources/cathey-2024.md), §4, Fig. 7).

Grid sizes in the chunk-3 JOREK applications:
- HL-3 lower single null: 11 136 elements, 71 radial × 121 poloidal points
  inside the separatrix, 18 radial points in the scrape-off layer, 6 in the
  private-flux region and 13 poloidal points along the divertor legs, refined
  radially in the pedestal and accumulated poloidally at the X-point; the
  confined radius at the outer midplane is 0.55 m and the scrape-off layer
  extends 0.04 m ([Liang et al. (2025)](/sources/liang-2025.md), §III, Fig. 1).
- AUG flux pumping: a polar grid of 100×100 elements up to the last closed
  surface, $n\le4$ ([Zhang et al. (2025)](/sources/zhang-2025.md), §2.4).
- AUG SPI: a 70×110 flux-aligned X-point grid, $n=0$–7
  ([Tang et al. (2025)](/sources/tang-2025.md), §3.1).
- 2D blob runs for surrogate training: 200×200 bicubic elements on a 1 m
  square slab ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.1).

## Convergence

- **Growth rates.** The error of a linear growth rate falls as
  $(\sqrt{N_{\mathrm{rad}}N_{\mathrm{pol}}})^{-5}$ for a tearing mode in full
  MHD and for the $n=20$ cbm18 ballooning mode in reduced MHD, with
  $N_{\mathrm{rad}},N_{\mathrm{pol}}$ the radial and poloidal node counts;
  full MHD gave only third order on the ballooning case
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.1, Figs. 13–14). The
  stated rationale is a local error $h^4$ for bicubic elements plus one power
  from integrating the energy.
- **Anisotropic heat transport.** On a flux-aligned grid
  $\kappa_\parallel/\kappa_\perp>10^{10}$ is resolved at $200\times200$ nodes
  within 0.3% core-temperature error, error $\propto N^{-3}$ in the node
  count; on an unaligned grid the error is $\propto N^{-2}$ and the limit is
  about $10^9$ ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.2, App. D,
  Fig. 16).

- **Toroidal truncation.** For the $1/1$ core dynamics of flux pumping,
  $n\le1$ "cannot correctly capture" the physics, while $n\le2$ and $n\le4$
  differ by about 1% in the saturated $q_0$ and $j_\phi$; time-step and grid
  scans converge the linear growth rate and the saturation amplitude
  (Zhang et al. 2025, §2.4; not plotted).

## Higher order and comparison with other codes

Pamela et al. (2022) generalized the basis to arbitrary-order $G^n$ Bézier
elements, reported as more efficient than the original element
([Bhole et al. (2023)](/sources/bhole-2023.md), §5, citing it;
[Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5: "speed-up or better
stability depending on the application"); it was not yet ported to JOREK3D
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §II). The W7-AS runs of
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§2.4) still use the
"typically $G^1$" elements and note that the higher-continuity elements
might later remove the auxiliary $j$ and $\varpi$ unknowns. They also
replace the analytic vacuum potential by a finite-element solution of a
Poisson problem in all runs (§2.2), against the continuity argument above
(recorded on [Dommaschk potentials](/methods/dommaschk-potentials.md)).

| Code | Poloidal elements | Continuity | Toroidal direction | Source |
|---|---|---|---|---|
| [JOREK](/software/jorek.md) | isoparametric bicubic Bézier quadrilaterals | $G^1$ (Table 1); $C^1$ in Bhole et al. | real Fourier series | [Artola et al. (2021)](/sources/artola-2021.md), Table 1 |
| [M3D-C1](/software/m3d-c1.md) | reduced-quintic (Bell) triangles | $C^1$ | cubic Hermite elements | [Artola et al. (2021)](/sources/artola-2021.md), Table 1, §2; [Zhang et al. (2021)](/sources/zhang-2021.md), §2 |
| [NIMROD](/software/nimrod.md) | spectral elements, Legendre-spaced nodes (bicubic; biquintic in Taheri et al.; fifth or sixth order on a 40×60 mesh in Ebrahimi & Bhattacharjee; degree 4 on 56×72 or degree 3 on 96×128 elements, $n\le10$ or 21, in Izzo et al.) | $C^0$ | Fourier series | [Artola et al. (2021)](/sources/artola-2021.md), Table 1; [Taheri et al. (2022)](/sources/taheri-2022.md), §2; [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md), p. 2; [Izzo et al. (2025)](/sources/izzo-2025.md), Table I |

M3D-C1 carries 12 degrees of freedom per scalar per vertex in 3D and 6 in 2D
([Artola et al. (2021)](/sources/artola-2021.md), §3); its runaway-electron
runs use 6454 elements per plane and 16 planes, with cubic Hermite
elements between planes ([Liu et al. (2021)](/sources/liu-2021.md), §2–3). The eigenvalue code
[SCELT](/software/scelt.md) uses the same Hermite-cubic idea in one dimension:
cubic radial elements times a poloidal Fourier series
([Ma & Guo (2022)](/sources/ma-2022.md), §3.1.3, App. A).

## Qualifications

- The order rationale "p = 4 because the Bézier elements are bi-cubic" uses $p$
  for the order of accuracy (polynomial degree plus one), not the degree
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.1; reader's note).
- The JOREK3D benchmarks warn that at $N_{\mathrm{tor}}=5$ field lines drift
  off flux surfaces and anisotropic transport is not properly modelled
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §VI).

## Contradictions

**Continuity class of the JOREK element — Closed by human fiat
(2026-10-16) as a difference of terminology.**
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§3.1) call the elements
$G^1$: value and *real-space* gradient are continuous, while the
element-specific scale factors make the derivatives with respect to the
reference coordinates jump between elements; $G^1$ is moreover *not strictly
enforced* at the magnetic axis and near X-points, where more than four
elements meet a node. [Artola et al. (2021)](/sources/artola-2021.md)
(Table 1 and its footnote: G = geometric, C = parametric continuity) list
JOREK as $G^1$ against $C^1$ for M3D-C1, and
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§II, §III),
[Isernia et al. (2023)](/sources/isernia-2023.md) (§II A),
[Ramasamy et al. (2024)](/sources/ramasamy-2024.md) (§2.4, "typically
$G^1$"), [Zhang et al. (2025)](/sources/zhang-2025.md) (§2.4) and
[Liang et al. (2025)](/sources/liang-2025.md) (§III) also write $G^1$; the
chunk-3 statements are labels, not derivations.
[Bhole et al. (2023)](/sources/bhole-2023.md) (§3.3.2) call the same element
$C^1$, because the arc-length derivatives are shared, element-independent
degrees of freedom. On regular nodes the two descriptions agree in substance
(continuous physical gradient, discontinuous parametric derivatives) and
differ in which coordinates the label refers to; they disagree on the
singular nodes, which Bhole et al. do not discuss except for the polar axis.
A source that states the continuity class of the field as a function of
$(R,Z)$ at every node type, including X-point nodes, would settle it.

* **Closed by human fiat (2026-10-16): a difference of terminology, not of
  substance.** The canonical label is $G^1$ in the sense of Artola et al.
  (2021): the field and its gradient are continuous in physical $(R,Z)$
  space, while the derivatives with respect to the element's reference
  coordinates are not. Bhole et al. (2023) say $C^1$ for the same element
  because the arc-length derivatives are shared degrees of freedom; on
  regular nodes this is the same property. On the magnetic axis and
  near X-points $G^1$ is not strictly enforced (Hoelzl et al. 2021, §3.1),
  and this caveat stands.
  *Fiat closure — `status: hypothesis` attribution: the closure is the
  human's judgment, not a source superseding a source; a later source can
  reopen it.*

# Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §3.1, Eqs. 51–55, §4.1–4.2.
- [Bhole et al. (2023)](/sources/bhole-2023.md) — §3.3, Eqs. 41–44.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §II, App. A, Eq. A1.
- [Artola et al. (2021)](/sources/artola-2021.md) — Table 1, §2–3.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §5.
- [Isernia et al. (2023)](/sources/isernia-2023.md) — §II A; [Korving et al. (2023)](/sources/korving-2023.md) — §II C.
- [Zhang et al. (2021)](/sources/zhang-2021.md) — §2; [Taheri et al. (2022)](/sources/taheri-2022.md) — §2; [Ma & Guo (2022)](/sources/ma-2022.md) — §3.1.3, App. A.
- [Cathey et al. (2023)](/sources/cathey-2023.md) — §2.2; [Cathey et al. (2024)](/sources/cathey-2024.md) — §4; [Artola et al. (2022)](/sources/artola-2022.md) — §2; [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — §II; [Hu et al. (2023)](/sources/hu-2023.md) — §2.2; [Hu et al. (2024)](/sources/hu-2024.md) — §2.1.
- [Zhang et al. (2025)](/sources/zhang-2025.md) — §2.4; [Liang et al. (2025)](/sources/liang-2025.md) — §III, Fig. 1; [Tang et al. (2025)](/sources/tang-2025.md) — §3.1; [Gopakumar et al. (2024)](/sources/gopakumar-2024.md) — §2.1.
- [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §2.2, §2.4; [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — p. 2; [Liu et al. (2021)](/sources/liu-2021.md) — §2–3; [Izzo et al. (2025)](/sources/izzo-2025.md) — Table I.
