---
type: Definition
title: "Whitney forms (discrete differential forms)"
description: "Finite elements that extend cochain data on mesh facets into piecewise-polynomial differential forms, with exterior derivative commuting with the extension."
status: established
aliases: [edge elements, face elements, Nédélec elements, discrete differential forms]
tags: [finite-elements, whitney-forms, differential-forms, de-rham]
timestamp: 2026-07-08T00:00:00Z
---

# Whitney forms (discrete differential forms)

The finite-element family whose degrees of freedom are **integrals over
mesh $l$-facets** — point values (0-forms/nodal elements), edge
circulations (1-forms/*edge elements*), face fluxes (2-forms/*face
elements*), cell volumes (3-forms) — i.e. exactly the cochain data of the
complex $V_h^0 \to V_h^1 \to V_h^2 \to V_h^3$
([notation](/notation.md)), extended into cell interiors by the **Whitney
map** $\mathsf{W}^l$ ([Hiptmair (2002)](/sources/hiptmair-2002.md) §3.2),
required to satisfy:

1. *extension*: integrating $\mathsf{W}^l u$ over any $l$-facet returns the
   cochain coefficient;
2. *commuting diagram*:
   $d \circ \mathsf{W}^l = \mathsf{W}^{l+1} \circ \mathsf{D}^l$ — the
   exterior derivative of the extension is the extension of the
   combinatorial derivative;
3. *strict locality*: cell-supported data give cell-supported forms;
4. *simple proxies*: piecewise-polynomial vector fields (barycentric
   formulas on simplices, e.g.
   $\lambda_i\,\mathrm{grad}\,\lambda_j - \lambda_j\,\mathrm{grad}\,\lambda_i$
   for edge elements; tensor-product versions on bricks; curved cells by
   pullback).

Interpolation inherits the structure:
$d \circ \Pi^l = \Pi^{l+1} \circ d$, so the discrete de Rham theorem holds
for Whitney forms with cohomology of the correct Betti dimensions
([discrete exactness theorems](/results/discrete-exactness-theorems.md)).

## Why this placement and no other

The staggered-collocation lesson in FE form: put the DOFs on the facets
matching the field's form degree, and discrete potentials exist *inside the
finite element family*. Componentwise Lagrangian vector elements fail
precisely here — a curl-free piecewise-linear proxy field has a potential
only as a $C^1$ piecewise-quadratic object with no localized basis
([Hiptmair (2002)](/sources/hiptmair-2002.md) §3.3). This is the FE
statement of the collocation constraint that runs through the whole domain:
[staggered grids](/definitions/staggered-grid.md) (FD/FV), Whitney forms
(FE), and the [mimetic natural operators](/definitions/support-operator-method.md)
are the same placement discipline in three languages.

The engineering counterpart: the material matrices of the
[finite integration technique](/methods/finite-integration-technique.md)
are discrete Hodge operators, and in edge-finite-element form they are
*exactly* the mass matrices obtained by quadrature of Whitney shape
functions ([Clemens & Weiland (2001)](/sources/clemens-weiland-2001.md)) —
two derivations, one object.

Within [FEEC](/definitions/finite-element-exterior-calculus.md), Whitney
forms are the lowest member of a two-family hierarchy:
$\mathcal{P}_1^-\Lambda^k$, isomorphic to simplicial cochains — with
higher-degree families $\mathcal{P}_r\Lambda^k, \mathcal{P}_r^-\Lambda^k$
extending the same complex structure to arbitrary polynomial order
([Arnold, Falk & Winther (2006)](/sources/arnold-falk-winther-2006.md)).

# Citations

1. [Hiptmair (2002)](/sources/hiptmair-2002.md), §3.
2. [Clemens & Weiland (2001)](/sources/clemens-weiland-2001.md), §3.
3. [Arnold, Falk & Winther (2006)](/sources/arnold-falk-winther-2006.md), §1.
