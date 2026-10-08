---
type: Method
title: "Flux-CT and the Godunov CT variants"
description: "Constrained transport driven by a shock-capturing base scheme: corner EMFs assembled from upwind fluxes (flux-CT) or interpolated fields (field-CT)."
status: established
aliases: [flux-interpolated CT, field-interpolated CT, transport-flux-CT]
tags: [constrained-transport, godunov, shock-capturing]
timestamp: 2026-07-08T00:00:00Z
---

# Flux-CT and the Godunov CT variants

The family of schemes combining [constrained transport](/methods/constrained-transport.md)
with conservative shock-capturing (Godunov-type) base schemes: the corner/edge
EMF $E_h$ is assembled from base-scheme data, then the staggered field is
updated by the standard CT circulation, preserving $D_h^{\mathrm{f}} B_h$
([notation](/notation.md)) to roundoff. The variants, as catalogued by
[Tóth (2000)](/sources/toth-2000.md) §4 (primary sources not yet ingested):

* **Field-interpolated CT** (Dai & Woodward): interpolate cell-centered
  $\mathbf{v}$ and $\mathbf{B}$ (two time levels, four cells) to the corner
  and form $E_h = -\bar{\mathbf{v}}\times\bar{\mathbf{B}}$ there.
* **Flux-interpolated CT** (Balsara & Spicer): average the four
  appropriately-signed upwind magnetic-field fluxes of the base scheme
  adjacent to the corner,
  $$E_h\big|_{j+\frac12,k+\frac12} = \tfrac14\left(-f^{x,*}_{j+\frac12,k} - f^{x,*}_{j+\frac12,k+1} + f^{y,*}_{j,k+\frac12} + f^{y,*}_{j+1,k+\frac12}\right),$$
  inheriting the base scheme's upwinding in the EMF.
* **Transport-flux-interpolated CT** (Ryu, Miniati, Jones & Frank): as
  flux-CT but averaging only the *transport part* of the upwind fluxes, with
  weight $\tfrac12$; coincides with the base scheme for 1D slab-symmetric
  problems.

## Properties

* Constraint mechanism identical to CT: once-per-edge EMF, two-face use with
  opposite signs.
* Each variant is exactly a pure finite-volume scheme on the cell-centered
  field — see [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md);
  the price of divergence preservation is flux averaging over a wider stencil
  than the base scheme.
* In [Tóth (2000)](/sources/toth-2000.md)'s ten-problem comparison, flux-CT is
  among the three most accurate and reliable schemes; field-CT is the least
  accurate CT variant; transport-flux-CT fails to run some 2D tests without
  limiter changes.

The averaging step is the family's acknowledged weak point and was later
superseded twice over: by genuinely two-dimensional four-state upwind EMFs
([Londrillo & Del Zanna (2000)](/sources/londrillo-delzanna-2000.md)), and
by direct evaluation of the EMF at zone edges from the multidimensional
Riemann data, with second/third-order unsplit time integration
([Balsara (2004)](/sources/balsara-2004.md) §2 — resolving his "Issue 4").

**The monopole objection.**
[Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md) §2.4
argue that a second weakness sits outside the EMF. These variants evolve
staggered data but feed *cell-centered averages* into the momentum and
energy fluxes. The orthogonality defect of the Lorentz force is then
governed by $D_h^{\mathrm{c}}$ of the averaged field, not by the exactly
held staggered divergence, and that residual is $O(1)$ wherever the field's
parallel derivative jumps. Numerical monopoles therefore arise despite exact
CT. The two views do not conflict:
* Tóth's equivalence says *which* divergence these schemes hold
  ($D_h^{\mathrm{k}}$);
* Londrillo & Del Zanna say *which* divergence the momentum flux sees,
  which is a different stencil.

Their remedy, [upwind constrained transport](/methods/upwind-constrained-transport.md),
puts the staggered components into every flux.

# Citations

1. [Tóth (2000)](/sources/toth-2000.md), §4.2–4.4, §6–7, Table IX.
2. [Balsara (2004)](/sources/balsara-2004.md), §2.
3. [Londrillo & Del Zanna (2004)](/sources/londrillo-delzanna-2004.md), §§2.2.1, 2.4, Table 3.
