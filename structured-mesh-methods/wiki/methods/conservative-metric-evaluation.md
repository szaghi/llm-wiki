---
type: Method
title: "Conservative metric evaluation"
description: "Computing the metric terms of a curvilinear discretization in a conservative (curl) form with the same discrete operators as the flux divergence, so that the discrete metric identities hold: the Thomas–Lombard form, the conditions of the conservative metric method (outer operator equal to the flux operator, inner equal to outer), the symmetrical (coordinate-invariant) form, the curl forms for spectral elements, and why upwind and WENO fluxes break it."
status: established
aliases: [conservative metric method, CMM, symmetrical conservative metric method, SCMM, conservative curl form, invariant curl form, Thomas–Lombard metrics]
tags: [free-stream-preservation, metric-identities, high-order, finite-difference]
timestamp: 2026-11-08T20:37:00Z
---

# Conservative metric evaluation

The metric terms $J\mathbf a^i$ can be written in several analytically
equivalent forms with different discrete errors. In 3-D the cross-product
form, e.g. $J\xi_x=y_\eta z_\zeta-y_\zeta z_\eta$, differenced with central
schemes does **not** satisfy the discrete metric identities
([free-stream preservation](/properties/free-stream-preservation.md)), even
though the same practice works in 2-D. The remedy common to all sources is
to write the metrics as a curl, so that their discrete divergence cancels.

## The conservative (curl) form

Thomas and Lombard's form ([Thomas & Lombard 1979](/sources/thomas-1979.md))
writes, with the outer and inner operators of the [notation](/notation.md),

$$J\xi_x=\delta^{\mathrm o}_\zeta\!\big(z\,\delta^{\mathrm{in}}_\eta y\big)-\delta^{\mathrm o}_\eta\!\big(z\,\delta^{\mathrm{in}}_\zeta y\big)$$

and cyclically. [Visbal & Gaitonde (2002)](/sources/visbal-2002.md) show
that with sixth-order compact schemes the standard form leaves free-stream
errors that shrink with order but stay unacceptable, while the conservative
form, differenced with the flux scheme, preserves a uniform flow on a
strongly curved 3-D mesh.

## Conditions: the conservative metric method

[Deng et al. (2011)](/sources/deng-2011.md) make the conditions explicit. The
discrete identities hold if (1) the conservative form is used and (2) the
outer operator in each direction equals the flux-derivative operator,
$\delta^{\mathrm o}_i=\delta_i$, so the cross differences commute. This is a
sufficient condition; it holds also at boundary and near-boundary closures,
and different operators in different directions are allowed. The inner
operator does not affect the identities in theory, but $\delta^{\mathrm{in}}_i\ne\delta^{\mathrm o}_i$
gave large errors and even breakdown, so $\delta^{\mathrm{in}}_i=\delta^{\mathrm o}_i$
is recommended. The flux operator must be **linear** (independent of the
solution): the method applies to central schemes, including the weighted
compact nonlinear scheme whose final difference is a linear central
midpoint-to-node formula, but not to upwind or dissipative schemes.

## The symmetrical (coordinate-invariant) form

[Deng et al. (2013)](/sources/deng-2013.md) average the two conservative
forms (the symmetrical form, identical to the coordinate-invariant form of
Vinokur and Yee) and pair it with a consistent Jacobian. With second-order
central differences these are exactly the finite-volume face vectors and
cell volume, so the face vectors enclose the cell; the geometric argument
also proves $\delta^{\mathrm{in}}_i=\delta^{\mathrm o}_i=\delta_i$ necessary. On
randomized grids the symmetrical method gives the most accurate and robust
results with high-order weighted compact schemes.

## Element-wise curl forms

For discontinuous spectral elements on curved hexahedra,
[Kopriva (2006)](/sources/kopriva-2006.md) writes the conservative form and
the invariant form as curls of interpolated products,
$J\mathbf a^i=-\nabla_{\boldsymbol\xi}\times\mathcal I_k(\dots)$, and proves:
in 2-D the usual cross-product form satisfies the discrete identities for
isoparametric geometry (mapping degree not above the solution degree $k$)
with Gauss quadrature; in 3-D it does not, except in special cases; the
interpolated curl forms always do (with Gauss quadrature, and for the
second weak form with Gauss–Lobatto).

## Upwind and WENO fluxes

The cancellation needs one linear operator for metrics and fluxes. In
finite-difference WENO the interpolated quantities are fluxes that contain
the metrics, so the metrics alter the nonlinear weights even in a free
stream, and the metrics cannot be split into upwind parts: WENO in
generalized coordinates does not preserve the free stream, while the
weighted compact nonlinear scheme, which interpolates the flow variables and
differences the fluxes centrally, does
([Nonomura, Iizuka & Fujii 2010](/sources/nonomura-2010.md)).
[Zhu & Hu (2019)](/sources/zhu-2019.md) split the Lax–Friedrichs flux into a
central part, treated with the symmetrical method, and a dissipative part
written as differences of the conservative variables between neighbouring
points; making each pair share one half-point Jacobian and metric set makes
the dissipation vanish in a uniform flow, for linear-upwind, WENO and hybrid
schemes.

# Citations

- [Thomas & Lombard (1979)](/sources/thomas-1979.md) — conservative metric form.
- [Visbal & Gaitonde (2002)](/sources/visbal-2002.md) — §4.2.
- [Kopriva (2006)](/sources/kopriva-2006.md) — §7, Theorems 3–5, §9.
- [Nonomura, Iizuka & Fujii (2010)](/sources/nonomura-2010.md) — formulations, conclusion.
- [Deng et al. (2011)](/sources/deng-2011.md) — §2–§3, §5.
- [Deng et al. (2013)](/sources/deng-2013.md) — symmetrical conservative form, concluding remarks.
- [Zhu & Hu (2019)](/sources/zhu-2019.md) — §3, §5.
