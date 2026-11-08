---
type: Definition
title: "Immersed boundary method"
description: "A family of methods that solve the flow equations on a grid that does not conform to the body or interface, representing the boundary through forcing, modified stencils, ghost values or cut cells; the hub page that separates continuous from discrete forcing and diffuse from sharp interfaces."
status: established
aliases: [IB method, IBM, immersed boundary technique, Cartesian grid method, non-boundary-conforming method, fictitious domain method, embedded boundary method]
tags: [immersed-boundary, classification, cartesian-grid]
timestamp: 2026-11-08T18:08:00Z
---

# Immersed boundary method

An **immersed boundary method** solves the equations of a flow around a body
$\Omega_s$, or across an interface $\Gamma$, on a grid that does not conform to
$\Gamma$: typically a uniform or block-refined Cartesian grid covering the
whole domain $\Omega$. The boundary condition on $\Gamma$ is not imposed on
grid points that lie on it, because none need to; it is imposed by modifying
the discrete equations near $\Gamma$. Grid generation becomes trivial, a
moving or deforming body needs no remeshing, and a fast solver for the regular
grid can be kept ([Peskin 1972](/sources/peskin-1972.md), §I;
[LeVeque & Li 1994](/sources/leveque-1994.md), §1.1;
[Ye et al. 1999](/sources/ye-1999.md), §1;
[Fadlun et al. 2000](/sources/fadlun-2000.md), §1). The price is that the
boundary cuts the grid arbitrarily, so accuracy, conservation and stability
near $\Gamma$ must be engineered.

The name was coined by [Peskin (1972)](/sources/peskin-1972.md) for elastic
boundaries that move with a viscous fluid and exert forces on it; in that
original sense the method replaces the boundary by a singular force field
spread to the grid with a [regularized delta function](/operators/regularized-delta-function.md)
([classical immersed boundary method](/methods/classical-immersed-boundary-method.md)).
The term has since widened to every non-conforming approach. Ye et al. (1999,
§1) still reserve "immersed boundary" for force-based methods and call their
cut-cell scheme a "Cartesian grid method"; Pember et al. (1995) speak of a
body "treated as an interface embedded in a regular Cartesian mesh"; Angot et
al. (1999) call penalization a "fictitious domain method". This bundle uses
"immersed boundary method" for the whole family and names the variant.

## Two classifications

**How the boundary enters the equations.**

- *Continuous forcing*: a force term is added to the continuous momentum
  equation and then discretized — the elastic forces of the
  [classical method](/methods/classical-immersed-boundary-method.md), the
  [feedback forcing](/methods/feedback-forcing.md) of
  [Goldstein et al. (1993)](/sources/goldstein-1993.md), and
  [volume penalization](/methods/volume-penalization.md), where the body is a
  porous medium of vanishing permeability ([Angot et al. 1999](/sources/angot-1999.md)).
- *Discrete forcing*: the force (or the stencil) is defined from the discrete
  equations so that the discrete solution satisfies the boundary condition —
  [direct forcing](/methods/direct-forcing.md)
  ([Fadlun et al. 2000](/sources/fadlun-2000.md); [Kim et al. 2001](/sources/kim-2001.md)),
  the [immersed interface method](/methods/immersed-interface-method.md)
  ([LeVeque & Li 1994](/sources/leveque-1994.md)), the
  [ghost fluid method](/methods/ghost-fluid-method.md)
  ([Fedkiw et al. 1999](/sources/fedkiw-1999.md)) and the
  [cut-cell method](/methods/cut-cell-method.md)
  ([Pember et al. 1995](/sources/pember-1995.md); [Ye et al. 1999](/sources/ye-1999.md)).

**How sharply the boundary is represented** ([sharp and diffuse interfaces](/definitions/sharp-and-diffuse-interface.md)):
a diffuse method spreads the boundary over a few cells (the delta-function
and Gaussian-spread methods), a sharp method keeps it a codimension-one set
that the stencils see exactly (interface jumps, ghost values, cut cells).

## Families in the founding papers

| family | idea | founding source in this bundle |
|---|---|---|
| [classical IB](/methods/classical-immersed-boundary-method.md) | elastic structure → singular force, spread and interpolated by $\delta_h$ | [Peskin (1972)](/sources/peskin-1972.md), [Peskin (2002)](/sources/peskin-2002.md) |
| [feedback forcing](/methods/feedback-forcing.md) | proportional–integral controller drives $\mathbf u\to\mathbf u_\Gamma$ on $\Gamma$ | [Goldstein et al. (1993)](/sources/goldstein-1993.md) |
| [direct forcing](/methods/direct-forcing.md) | force chosen from the discrete momentum equation so $\mathbf u=\mathbf V$ at forcing points | [Fadlun et al. (2000)](/sources/fadlun-2000.md), [Kim et al. (2001)](/sources/kim-2001.md) |
| [volume penalization](/methods/volume-penalization.md) | Brinkman term $\eta^{-1}\chi_s(\mathbf u-\mathbf u_\Gamma)$ | [Angot et al. (1999)](/sources/angot-1999.md) |
| [immersed interface](/methods/immersed-interface-method.md) | stencils corrected with the jump conditions across $\Gamma$ | [LeVeque & Li (1994)](/sources/leveque-1994.md) |
| [ghost fluid](/methods/ghost-fluid-method.md) | ghost states across a level-set interface | [Fedkiw et al. (1999)](/sources/fedkiw-1999.md) |
| [cut cell](/methods/cut-cell-method.md) | finite volumes clipped by $\Gamma$, [small cells](/definitions/small-cell-problem.md) stabilized | [Pember et al. (1995)](/sources/pember-1995.md), [Ye et al. (1999)](/sources/ye-1999.md) |

## Qualifications

- The accuracy of a diffuse method with a true interface is first order,
  whatever the formal order of the interior scheme
  ([first-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)).
- Whether the method conserves mass, momentum and energy depends on the
  variant ([discrete conservation](/properties/discrete-conservation.md)).

## The formal dichotomy and the cost of a Cartesian grid

[Mittal & Iaccarino (2005)](/sources/mittal-2005.md) give the two forcing
classes an algebraic form. Write the flow equations as $\mathcal L(\mathbf U)=0$
with $\mathbf U=(\mathbf u,p)$. *Continuous forcing* adds $\mathbf f_b$ to the
continuous system, $\mathcal L(\mathbf U)=\mathbf f_b$, and then discretizes it
everywhere; *discrete forcing* first discretizes, $[L]\{\mathbf U\}=0$, then
modifies the operator near $\Gamma$, $[L']\{\mathbf U\}=\{\mathbf r\}$, which is the
same as a discrete force $\{\mathbf f'_b\}=\{\mathbf r\}+[L]\{\mathbf U\}-[L']\{\mathbf U\}$.
Continuous forcing is independent of the discretization; discrete forcing
depends on it but gives direct control of accuracy, stability and discrete
conservation. Ghias et al. (2007, §1) and Mittal et al. (2008, §1) use the same
classification.

For a body of size $L$ with a boundary layer of thickness $\delta$, a Cartesian
grid grows like $(L/\delta)^2$ relative to a body-conformal grid, that is like
$Re$ in 2-D and $Re^{1.5}$ in 3-D for a laminar boundary layer, partly offset by
not solving inside the body, cheaper operations per point and line or
multigrid solvers (Mittal & Iaccarino 2005). Ghias et al. (2007, §1) answer
with body-non-conformal *curvilinear* grids that cluster points in the
boundary layer.

## Families added by later sources

| family | idea | sources |
|---|---|---|
| [ghost cell](/methods/ghost-cell-method.md) | values at solid points next to the fluid enforce the boundary condition at the normal intercept | [Tseng & Ferziger (2003)](/sources/tseng-2003.md), [Ghias et al. (2007)](/sources/ghias-2007.md), [Mittal et al. (2008)](/sources/mittal-2008.md), [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) |
| [Lagrangian direct forcing](/methods/direct-forcing.md) | direct force computed at Lagrangian points and spread with $\delta_h$ | [Uhlmann (2005)](/sources/uhlmann-2005.md) |
| [IB projection](/methods/immersed-boundary-projection-method.md) | boundary force as Lagrange multiplier of no-slip | [Taira & Colonius (2007)](/sources/taira-2007.md) |
| [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) | high-order ghost values from the PDE and boundary data | [Tan & Shu (2010)](/sources/tan-2010.md) |
| [CutFEM](/methods/cutfem.md) | unfitted finite elements, Nitsche conditions, ghost penalty | [Burman et al. (2015)](/sources/burman-2015.md) |

# Citations

- [Peskin (1972)](/sources/peskin-1972.md) — §I, §VI.
- [Goldstein et al. (1993)](/sources/goldstein-1993.md) — introduction.
- [LeVeque & Li (1994)](/sources/leveque-1994.md) — §1, §1.1.
- [Pember et al. (1995)](/sources/pember-1995.md) — §1.
- [Fedkiw et al. (1999)](/sources/fedkiw-1999.md) — §1, §3.
- [Ye et al. (1999)](/sources/ye-1999.md) — §1.
- [Angot et al. (1999)](/sources/angot-1999.md) — §1.
- [Fadlun et al. (2000)](/sources/fadlun-2000.md) — §1.
- [Kim et al. (2001)](/sources/kim-2001.md) — §1.
- [Peskin (2002)](/sources/peskin-2002.md) — §1, §3.
- [Tseng & Ferziger (2003)](/sources/tseng-2003.md) — §1, §2.2.
- [Mittal & Iaccarino (2005)](/sources/mittal-2005.md) — introduction, imposition of boundary conditions.
- [Uhlmann (2005)](/sources/uhlmann-2005.md) — §1.
- [Ghias et al. (2007)](/sources/ghias-2007.md) — §1.
- [Taira & Colonius (2007)](/sources/taira-2007.md) — §1.
- [Mittal et al. (2008)](/sources/mittal-2008.md) — §1.
- [Tan & Shu (2010)](/sources/tan-2010.md) — §1.
- [Chaudhuri et al. (2011)](/sources/chaudhuri-2011.md) — §1.
- [Burman et al. (2015)](/sources/burman-2015.md) — §1.
