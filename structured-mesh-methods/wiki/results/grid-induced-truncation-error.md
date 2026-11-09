---
type: Result
title: "Grid-induced truncation error"
description: "The truncation error of difference formulas on a curvilinear grid depends on the rate of change of the spacing and on the departure from orthogonality, not only on the spacing: a central difference stays second order only if the spacing varies slowly (x_ξξ of order x_ξ²), and nonorthogonality adds a term in the cotangent of the line angle."
status: established
aliases: [stretching error, skewness error, grid smoothness requirements]
tags: [accuracy, truncation-error, grid-quality]
timestamp: 2026-11-08T20:37:00Z
---

# Grid-induced truncation error

[Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md), Section O,
derive the error that a curvilinear grid adds to a difference formula. In
one dimension the central difference of $f_x=f_\xi/x_\xi$ on a stretched grid
has two leading truncation terms: the usual one proportional to the square
of the spacing, and one proportional to $x_{\xi\xi}$, produced by the unequal
spacing, which acts as numerical diffusion (as de Rivas showed). The formula
is therefore truly second order only if

$$x_{\xi\xi}=O(x_\xi^2),$$

that is, if the spacing changes slowly. Stating the error as
$f_{\xi\xi\xi}\Delta\xi^2$ and concluding second order is not justified, since
$f_{\xi\xi\xi}$ depends on the coordinate system and $\Delta\xi$ need not be
small.

On a nonorthogonal grid the same analysis adds a term proportional to
$\cot\theta$, $\theta$ the angle between coordinate lines; departures from
orthogonality up to $45^\circ$ are tolerable once the spacing condition holds.
Rules of thumb quoted: successive spacing ratios at most 2 and departures
from orthogonality under half a radian (Forester). Higher-order evaluation
of the metric terms improves accuracy (Holst; fourth-order metrics with a
second-order flow scheme). The authors prefer compact formulas with a grid
made smooth enough over long formulas that account for nonuniform,
nonorthogonal spacing.

These are the measures that [mesh quality metrics](/definitions/mesh-quality-metric.md)
quantify element by element and that the
[elliptic](/methods/elliptic-grid-generation.md) and
[variational](/methods/variational-grid-generation.md) generators control.

## High-order schemes on nonsmooth meshes

Compact sixth-order schemes on meshes with sudden spacing jumps or sustained
metric variation produce spurious oscillations; a discriminating high-order
low-pass filter restores stability and keeps their accuracy advantage over
second-order schemes even across large grid discontinuities
([Visbal & Gaitonde 2002](/sources/visbal-2002.md)). Grids with
discontinuous point derivatives (randomized grids) amplify the metric errors
of schemes that do not satisfy the discrete metric identities
([Nonomura, Iizuka & Fujii 2010](/sources/nonomura-2010.md);
[Deng et al. 2013](/sources/deng-2013.md)).

# Citations

- [Thompson, Warsi & Mastin (1982)](/sources/thompson-1982.md) — Section O.
- [Visbal & Gaitonde (2002)](/sources/visbal-2002.md) — §4.1.
- [Nonomura, Iizuka & Fujii (2010)](/sources/nonomura-2010.md) — conclusion.
- [Deng et al. (2013)](/sources/deng-2013.md) — numerical tests.
