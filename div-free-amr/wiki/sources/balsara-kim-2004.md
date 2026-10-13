---
type: Source
title: "Balsara & Kim (2004) — Divergence-cleaning vs staggered-mesh MHD"
description: "Cross-compares two scalar projections, a spectral vector projection and a staggered-mesh CT scheme on supernova-driven MHD turbulence: all cleaning variants show spurious energetics, structures and spectra, attributed to the non-locality of the elliptic step."
resource: "doi:10.1086/381051"
source_kind: paper
authors: [Balsara D.S., Kim J.]
year: 2004
venue: "Astrophys. J. 602:1079-1090"
local_file: "/home/stefano/papers/mosaic/div-free-amr/2004-ApJ-Balsara-101086381051.pdf"
tags: [projection, divergence-cleaning, constrained-transport, turbulence, non-locality]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Tests whether divergence cleaning and a staggered-mesh, divergence-free
scheme are interchangeable, which earlier comparisons on simple tests had
suggested. Four schemes run on one second-order base scheme (predictor–
corrector, piecewise-linear, HLL):
* **SDC1:** scalar projection with the wide central Laplacian;
* **SDC2:** scalar projection with the compact Laplacian;
* **VDC:** spectral (Fourier) vector projection;
* **SM:** the Balsara–Spicer flux-CT scheme.

The test is a stringent one: supernova-driven, radiatively cooling MHD
turbulence on $128^3$, periodic. All three cleaning schemes produce spurious
magnetic-energy spikes, polluted structures, shifted field histograms and
excess small-scale power. The authors attribute this mainly to the
**non-locality** of the elliptic step, plus aliasing and (SDC1) even–odd
decoupling. SM alone is clean on every diagnostic.

The file read is the arXiv preprint (astro-ph/0310728). The published title
is "A Comparison between Divergence-Cleaning and Staggered-Mesh Formulations
for Numerical Magnetohydrodynamics"; venue, pages and title were verified on
Crossref.

# Key claims

1. **Three cleaning variants** (§II.a–c), in registry terms
   ([projection](/methods/projection-method.md); [notation](/notation.md)):
   * **SDC1** solves $D_h^{\mathrm{c}} G_h \phi_h = D_h^{\mathrm{c}} B_h^*$
     with the wide stencil of spacing $2\Delta x$. It makes
     $D_h^{\mathrm{c}} B_h$ exactly zero, but it decouples the grid into
     $2^3$ independent sub-lattices (even–odd decoupling).
   * **SDC2** uses the compact Laplacian. It has no decoupling, but it is
     not exact: every application leaves a different nonzero divergence.
   * **VDC** projects each Fourier mode onto the plane orthogonal to its
     wavevector. That is exact in spectral space and not in physical space.
     The $1/k^2$ factor is a Poisson solve in disguise, and the method
     applies only to uniform periodic boxes, not to AMR.
2. **Non-locality as the mechanism** (§II.a D.7, §III.b.2). A localized
   divergence source corrects the field everywhere, with a $1/r^2$ fall-off
   that is even slower for line or sheet sources. Applied every step, the
   correction accumulates. Persistent converging flows (colliding cooling
   shells; also self-gravity, per the authors) build divergence locally, and
   the cleaning spreads the defect. The spurious fluctuations peak where the
   shells intersect, which is where the projection acts most strongly.
3. **Staggered-mesh properties** (§II.d). SM is exact in real space and fully
   local, needs no FFT and minimal communication, and extends to AMR
   ([Balsara (2001)](/sources/balsara-2001.md)). With
   [divergence-free reconstruction](/methods/divergence-free-reconstruction.md),
   discrete exactness yields a field that is divergence-free at *every
   point*. The authors say this is stronger than VDC's $N^3$ spectral
   conditions.
4. **Measured outcomes** (§III.b, Figs. 2–6).
   * SDC1 and SDC2 show chaotic magnetic-energy growth, saturating about an
     order of magnitude above SM. The authors judge them unsuitable for
     dynamo studies.
   * VDC fluctuates, then converges to SM's energy level once the
     fluctuations subside, over a run about 7× longer.
   * SDC1's histograms shift at each shell interaction. The spectra show
     excess small-scale power, worst for SDC1, slight for VDC, with SM best.
   * The results are reported as independent of the heating and cooling
     details.
5. **Framing.** The paper presents the comparison as "cleaning vs
   staggered mesh". Its SM scheme is flux-CT, which
   [Tóth (2000)](/sources/toth-2000.md) proved equivalent to a collocated
   finite-volume scheme
   ([CT–FV equivalence](/results/ct-finite-volume-equivalence.md)). What the
   test separates is therefore **constraint mechanism** (local exact update
   vs global projection), not field placement (compiler note).

# Notation map

| Balsara & Kim | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $B$ zone-centered before cleaning | $B_h^*$ (collocated) | |
| $\phi$ | $\phi_h$ | |
| eq. (2.3) central divergence | $D_h^{\mathrm{c}}$ | |
| eq. (2.4) wide Laplacian | $D_h^{\mathrm{c}} G_h$ ($2\Delta x$ stencil) | SDC1 |
| eq. (2.5) compact Laplacian | standard 7-point Laplacian | SDC2; does not equal $D_h^{\mathrm{c}} G_h$ |
| eq. (2.6) $\delta_{ij} - k_i k_j/k^2$ | spectral Leray projector | VDC; no registry symbol |
| SM, face $B$ / edge $E$ | $B_h \in V_h^2$, $E_h \in V_h^1$ | eqs. 2.9–2.14 |

# Pages created or updated

* Updated [Projection method](/methods/projection-method.md): the three variants, the non-locality failure mode, `## Contradictions`.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): exactness without locality.
* Updated [Staggered grid](/definitions/staggered-grid.md): why this comparison does not bear on the placement dispute.

# Citations

1. `~/papers/mosaic/div-free-amr/2004-ApJ-Balsara-101086381051.pdf` (arXiv:astro-ph/0310728; doi:10.1086/381051): text extraction, all 35 pp., including Tables I–II and the reference list (33 entries).
