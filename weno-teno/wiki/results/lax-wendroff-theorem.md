---
type: Result
title: "Lax–Wendroff theorem"
description: "The Lax–Wendroff theorem makes conservation, in flux form with consistent numerical fluxes, the condition for a convergent scheme to converge to a weak solution; the bundle's sources invoke it to justify local conservation, Active Flux, the subcell flux form of DGSEM and conservative sharp-interface multi-medium schemes, and show wrong shock positions when conservation is dropped."
status: established
aliases: [Lax–Wendroff convergence theorem, Lax–Wendroff consistency condition, conservation and convergence to weak solutions]
tags: [finite-volume, finite-difference, dg]
timestamp: 2026-10-23T08:00:00Z
---

# Lax–Wendroff theorem

Solutions of nonlinear conservation laws develop discontinuities in finite time even from
smooth data, so the natural setting is weak solutions; "for convergence to the weak
solution …, a numerical method needs to be conservative (Lax–Wendroff theorem)"
([Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), §1). The theorem (Lax & Wendroff
1960, cited by the sources, not ingested here) has two hypotheses the sources make explicit:
the scheme is written in **conservation (flux) form**,

$$\frac{d}{dt}\bar u_i=-\frac1{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big),$$

and the numerical flux is **consistent** with the physical one. The sources use it in one
direction only: conservation (with consistent fluxes) is what a scheme needs for
convergence to a weak solution (Abgrall & Barsukow, §1). No source
of this bundle restates the convergence hypotheses or the proof; the bundle records the
theorem through what they derive from it.

## The consistency condition

[Coppola & Veldman (2023)](/sources/coppola-2023.md) (§2.4, Eq. (22)) write the semi-discrete
scheme as $H\,\frac{d\phi}{dt}+(I-E^{-1})F\phi=0$, with $H$ a diagonal control-volume matrix,
$E$ the circulant shift and $F\phi$ the vector of interface fluxes (page-local symbols of the
source's matrix framework), and state the "classical" Lax–Wendroff condition as

$$F\phi_a\,\mathbf 1=F(\phi_a)\qquad\text{for every constant }\phi_a,$$

which "basically says that conservation and consistency imply that the numerical fluxes are
a fair interpolation between the adjacent nodal values". They assume it at the generality of
their framework and state that they "can not (yet) prove this" (§2.4).

The finite-difference statement is the same with point values: [Jeong et al. (2022)](/sources/jeong-2022.md)
(§2.1) write the conservative scheme $\frac{d}{dt}u_i=-\frac1{\Delta x}(\hat f_{i+1/2}-\hat f_{i-1/2})$
with a numerical flux $\hat f$ that is Lipschitz and consistent, $\hat f(u,\dots,u)=f(u)$, and
invoke the theorem for convergence to weak solutions of their
[RBF-based WENO](/methods/rbf-weno.md) ([conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)).

## Which schemes satisfy the flux-form hypothesis

- **Every globally conservative scheme.** Coppola & Veldman prove that a discrete operator
  with local support is locally conservative, i.e. of the form $(I-E^{-1})F$, if and only if
  all its column sums vanish, which is global conservation (Lemma A.1, Observation 1): for
  volume-consistent discretizations global and local conservation coincide, so every
  globally conservative finite-difference scheme is a cell-centred finite-volume scheme with
  an explicit numerical flux ([local conservation is equivalent to a flux
  form](/results/local-conservation-flux-form.md)). They cite Perot: "any method that is
  globally conservative, and that has weight functions with local support, must also be
  locally conservative" (Remark 1).
- **Active Flux.** The averages are updated by the exact finite-volume balance with the
  interface point values as flux arguments, hence conservatively, while the point values are
  free of the conservation constraint; Abgrall & Barsukow report that an analogue of the
  Lax–Wendroff theorem for [Active Flux](/methods/active-flux.md) has been shown by
  Abgrall (2020) (§1).
- **DGSEM on Gauss–Lobatto nodes.** [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md)
  (§2.1, Eq. (8)) rewrite the standard and split-form [DGSEM](/methods/dgsem.md) exactly in a
  subcell flux-differencing form with high-order inter-node fluxes and state that this
  "implies local subelement-wise conservation due to the well-known theorem of Lax and
  Wendroff"; it is what allows a compatible subcell finite-volume scheme to be blended in
  ([subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [flux differencing](/methods/flux-differencing.md)).

## What dropping conservation costs

Two sources show the consequence the theorem warns of, a wrong shock speed:

- **Non-conservative blending in time.** The [Quinpi](/methods/quinpi.md) scheme blends a
  high-order and a first-order implicit solution cell by cell, which is not conservative.
  Without the conservative correction that turns the blend back into a flux form, the
  scheme loses mass on Burgers' equation and places the shock wrongly; with it, mass is
  conserved at all times and the shock is located correctly
  ([Puppo et al. (2023)](/sources/puppo-2023.md), §3.3.4, §4.3.2, Fig. 7; see
  [local conservation is equivalent to a flux form](/results/local-conservation-flux-form.md)).
- **Non-conservative interface methods.** [Zheng et al. (2021)](/sources/zheng-2021.md) (§1)
  call the ghost-fluid family (GFM, modified and real GFM) and related interface
  treatments non-conservative, so that convergence to weak solutions is not assured, and
  build a conservative sharp-interface finite-difference scheme instead: a single
  computational variable updated by flux differences and redistributed between the two
  fluids (§2.3). On a strong shock hitting a gas–gas interface a finite-difference WENO
  ghost-fluid method misplaces both the shock front and the interface, while the
  conservative scheme does not (§4, Example 4, Fig. 8). They also recall that
  conservative schemes "tend to give oscillatory results if no special care is taken" at
  material interfaces (§1), which is the price conservation brings there (see
  [characteristic decomposition](/methods/characteristic-decomposition.md) on primitive
  variables).

## Qualifications

- What the sources cite is the conservation-and-consistency requirement; none of them
  proves a convergence statement for its own scheme from it. Conservation does not select
  the physically relevant weak solution: on the KPP rotating-wave problem the (conservative)
  standard DGSEM with shock capturing gives clean but **nonentropic** solutions, while the
  entropy-stable split-form DGSEM converges to the entropy solution
  ([Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md), §5.1, Figs. 2–3;
  [KPP rotating wave](/benchmarks/kpp-rotating-wave.md),
  [entropy stability](/properties/entropy-stability.md)).
- Rueda-Ramírez et al. attribute "local subelement-wise conservation" to the theorem; the
  conservation itself follows from the flux form (8), while the theorem is what gives it
  meaning for shock capturing.
- **Scope: conservation laws only.** For a system with a non-conservative product,
  $\partial_tu+\partial_xf(u)+\mathcal C(u)\partial_xu=0$, the product has no flux, so the
  flux-form hypothesis cannot be met for it *(compiler check, not in the sources)*. As
  recalled by [Chu et al. (2022)](/sources/chu-2022.md) (§1), weak solutions of such systems
  are defined as Borel measures in the sense of Dal Maso, LeFloch and Murat, which needs a
  choice of path across each jump, and are computed with
  [path-conservative schemes](/methods/path-conservative-scheme.md); with $\mathcal C=0$ their
  path-conservative central-upwind scheme is the conservative central-upwind scheme
  (§2, Eq. (2.1)).
- Coppola & Veldman's dual-sided first-order scheme conserves mass, momentum and total
  energy and gives a shock profile between the oscillating central and the smeared upwind
  scheme in a 1D Euler test without added dissipation (§8.2); they make no entropy claim.

# Citations

- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §1 (author preprint).
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §2.4 (Eqs. (18)–(22), Observation 1, Remark 1), App. A.1 (Lemma A.1), §8.2 (arXiv v1).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §2.1 (Eq. (8)), §5.1 (Figs. 2–3) (arXiv v2).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §3.3.4, §4.3.2 (Fig. 7) (arXiv v2).
- [Zheng et al. (2021)](/sources/zheng-2021.md) — §1, §2.3, §4 (Example 4, Fig. 8).
- [Chu et al. (2022)](/sources/chu-2022.md) — §1, §2 (Eq. (2.1)).
- [Jeong et al. (2022)](/sources/jeong-2022.md) — §2.1.
