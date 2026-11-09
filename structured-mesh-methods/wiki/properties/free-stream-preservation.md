---
type: Property
title: "Free-stream preservation"
description: "A scheme on a curvilinear grid preserves a uniform flow exactly only if its discrete metric terms satisfy the metric identities with the same discrete derivative operators; conservative evaluation of the metric terms achieves this, while analytic or averaged metrics leave spurious source terms."
status: established
aliases: [freestream preservation, discrete metric identities, surface conservation law, uniform-flow preservation]
tags: [free-stream-preservation, metric-identities, conservation]
timestamp: 2026-11-08T20:37:00Z
---

# Free-stream preservation

In the strong conservation form on a curvilinear grid the flux divergence is
$\sum_i\partial\hat{\mathbf f}^i/\partial\xi^i$ with contravariant fluxes
$\hat{\mathbf f}^i=J\mathbf a^i\cdot\boldsymbol{\mathcal F}$. For a uniform state
$\boldsymbol{\mathcal F}$ is constant, so the divergence reduces to
$\boldsymbol{\mathcal F}\cdot\sum_i\partial(J\mathbf a^i)/\partial\xi^i$, which
vanishes by the **metric identities** ([notation](/notation.md)). A
discretization preserves the free stream when the *discrete* metric terms
satisfy the identities with the *same* discrete operators:
$\sum_i\delta_i(J\mathbf a^i)=0$.

## Conservative metric evaluation

[Thomas & Lombard (1979)](/sources/thomas-1979.md) note, after Pulliam and
Steger, that central differences of the metrics in the usual form do not
make these terms cancel, and that the cancellation holds identically when
the metrics are first written in conservative form, e.g. in 3-D
$J\xi_x=(y_\eta z)_\zeta-(y_\zeta z)_\eta$, and differenced with the scheme's
operators. [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md),
Section P, show it in 2-D: the conservative derivative
$f_x=\big[(f\,y_\eta)_\xi-(f\,y_\xi)_\eta\big]/J$, with central differences for
both $f$ and the metrics, gives $f_x=0$ for constant $f$ because all
$y$-values cancel. With **analytically** evaluated metrics the discrete
$(y_\xi)_\eta$ differs from $(y_\eta)_\xi$ and a spurious source appears; so it
does when half-point metrics are averaged from integer points, unless the
grid is generated at the half points too.

On moving grids the same requirement extends to the time metric terms
through the [geometric conservation law](/properties/geometric-conservation-law.md).

## High order: three dimensions, errors, schemes

The 2-D practice of differencing the metrics with the flux operator does not
carry over to 3-D: with the cross-product form, central and compact schemes
violate the identities on curvilinear meshes, the error shrinks with order
but remains unacceptable even at sixth order, and analytic metrics should be
avoided altogether ([Visbal & Gaitonde 2002](/sources/visbal-2002.md)).
[Kopriva (2006)](/sources/kopriva-2006.md) shows what the violation does: a
uniform Mach 0.6 flow on a curved spectral-element mesh develops a
stationary pressure pattern and spurious sound waves radiating from the
centre, whereas with the identities satisfied the pressure error is
$2\times10^{-14}$ — spurious waves of the size of real acoustic signals
($10^{-4}$–$10^{-6}$ of the mean pressure) would otherwise contaminate
aeroacoustic results. [Deng et al. (2011)](/sources/deng-2011.md) split the
geometric conservation law into a volume law (moving grids) and a
**surface conservation law** — the discrete metric identities, which matter
on stationary grids and whose violation causes instabilities with high-order
schemes. How the identities are met — conservative forms, matching
operators, and the special difficulty of upwind and WENO fluxes — is on
[conservative metric evaluation](/methods/conservative-metric-evaluation.md).

# Citations

- [Thomas & Lombard (1979)](/sources/thomas-1979.md) — uniform-flow analysis, conservative metrics.
- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Section P.
- [Visbal & Gaitonde (2002)](/sources/visbal-2002.md) — §4.2.
- [Kopriva (2006)](/sources/kopriva-2006.md) — §1.
- [Deng et al. (2011)](/sources/deng-2011.md) — §1–§2.
