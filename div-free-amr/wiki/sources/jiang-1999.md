---
type: Source
title: "Jiang & Wu (1999) — A high-order WENO finite difference scheme for the equations of ideal MHD"
description: "Fifth-order characteristic WENO finite-difference scheme for ideal MHD with Lax-Friedrichs splitting and Brio-Wu-normalized eigenvectors; a Poisson projection of the field is needed for stability, as Orszag-Tang otherwise loses pressure positivity."
resource: "doi:10.1006/jcph.1999.6207"
source_kind: paper
authors: [Jiang G.-S., Wu C.-C.]
year: 1999
venue: "J. Comput. Phys. 150:561-594"
local_file: "~/papers/mosaic/div-free-amr/1999-JCP-Jiang-101006jcph19996207.pdf"
tags: [weno, finite-difference, high-order, projection, eight-wave, positivity, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper presents a fifth-order WENO finite-difference scheme for ideal
MHD. It extends the Jiang–Shu scheme to MHD:
* conservative point-value fluxes, built dimension-by-dimension;
* characteristic decomposition at the arithmetic-mean interface state;
* global Lax–Friedrichs flux splitting;
* fourth-order Runge–Kutta in time, at CFL 0.8.

The eigenvectors use the Brio–Wu normalization, which stays well defined
at degenerate wave speeds. Two eigensystems are tried in 2D: the $7\times7$
one, which ignores the normal-field equation, and Powell's $8\times8$ one.

For the bundle, the paper's interest is its divergence control. The paper
holds no discrete invariant. After the WENO update it solves a Poisson
equation by relaxation and subtracts a gradient, and it finds this step
necessary for stability. It is merged into
[projection](/methods/projection-method.md),
[eight-wave](/methods/eight-wave.md) and
[positivity–divergence coupling](/results/positivity-divergence-coupling.md).

# Key claims

1. **Scheme** (§2). Fifth-order WENO-JS weights with $\epsilon = 10^{-6}$
   on Lax–Friedrichs-split characteristic fluxes. The degenerate cases in
   the eigenvectors are switched at tolerance $\delta \approx 10^{-12}$.
   The $8\times8$ system adds a fifth (normal-field) characteristic with a
   nonzero numerical flux component. The $7\times7$ system keeps that
   component at zero, and otherwise both give the same fluxes.
2. **Divergence control** (§1, eqs. in text). The correction solves
   $\nabla^2\phi + \nabla\cdot B = 0$ and sets $B_c = B + \nabla\phi$,
   following Brackbill–Barnes, by a relaxation method. The discrete
   stencils and the placement within the Runge–Kutta stages are not
   specified.
3. **Rotated shock tube** (§3.1). The Brio–Wu problem, at $45°$ on
   $600^2$, with the $8\times8$ system: without correction there are
   spurious oscillations near the slow rarefaction in the compound wave.
   With correction the run agrees with the 1D result on 800 points.
4. **Orszag–Tang** (§3.4, $192^2$).
   * Without correction both eigensystems go unstable once pressure turns
     negative: at $t \approx 3.9$ with $8\times8$ and $t \approx 2.5$ with
     $7\times7$.
   * The authors attribute the difference to the missing diffusion in the
     normal-field flux of the $7\times7$ system. A fourth-order diffusion
     added to that equation brings it to the $8\times8$ level.
   * With correction both run to $t = 8$ with nearly identical results,
     and the uncorrected pressure is more oscillatory at $t = 3$.
   * The density error converges at about fourth order at $t = 0.2$
     against a $512^2$ reference.
5. **Accuracy and cost** (§§3.2–3.3).
   * Intermediate-shock formation from a slow simple wave: about fifth
     order before steepening (4.5 at 80–320 points, with
     $\Delta t \sim \Delta x^{5/4}$), first order after shocks form.
   * Periodic Kelvin–Helmholtz with $B$ normal to the plane: WENO at
     $50\times100$ reaches about 97% of the saturated energy. Two-step
     Lax–Wendroff needs more than $100\times600$ for 93%.
   * Per grid point, the cost is about 4 times that of a second-order
     Liu–Lax scheme.
6. **Stated caveats** (§§1, 4). Intermediate shocks make the solution
   depend on the dissipation mechanism, so a shock-capturing scheme can
   converge to different solutions. Third- and higher-order FD WENO needs a
   uniform or smoothly varying grid.

# Notation map

| Jiang & Wu (1999) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi$, $\nabla^2\phi + \nabla\cdot B = 0$ | projection potential and Poisson problem | discrete stencils unspecified, so no $D_h$ superscript is assigned |
| $B_c = B + \nabla\phi$ | $B_h = B_h^* - G_h\phi_h$ up to the sign convention of $\phi$ | |
| $8\times8$ eigensystem | Powell eigenvectors, without source terms | not the eight-wave formulation itself |
| $\hat F_{i+1/2}$, $f^\pm$ | numerical flux, Lax–Friedrichs split fluxes | |

# Pages created or updated

* Updated [Projection method](/methods/projection-method.md): the high-order finite-difference use and its necessity.
* Updated [Eight-wave formulation](/methods/eight-wave.md): the eigensystem's dissipation, separated from the source terms.
* Updated [Positivity–divergence coupling](/results/positivity-divergence-coupling.md): an early observation of the pressure failure without divergence control.

# Citations

1. `~/papers/mosaic/div-free-amr/1999-JCP-Jiang-101006jcph19996207.pdf` (doi:10.1006/jcph.1999.6207): text extraction, all pages including the reference list (36 entries). The eigenvector formulas in §2.3 were read in outline, and none is reproduced on concept pages. Figures were read from their captions only.
