---
okf_version: "0.1"
---

# hyperbolic-pde-theory — Knowledge Bundle

Continuum theory of partial differential equations with emphasis on hyperbolic systems: classification, characteristics, general and particular solutions, separation of variables and transform methods, well-posedness and uniqueness, weak and entropy solutions, Riemann problems, characteristic boundary conditions.

**Corpus:** 2 sources, both scoped reads of textbooks:
[Riley et al. (2006)](/sources/riley-2006.md) (Chs. 14–15, 20–21) and
[Arfken et al. (2013)](/sources/arfken-2013.md) (Chs. 7, 9). The linear
theory, mostly in two variables, is covered, and most claims carry both
citations. Hyperbolic systems, conservation laws, weak and entropy
solutions and Riemann problems have no source yet. Their symbols are
reserved in the registry, but no page exists for them. One `Contradictions`
entry is open, on the [Helmholtz equation](/definitions/helmholtz-equation.md).

**Start here:** the [Notation registry](/notation.md), which is normative
for every page, and the [update log](/log.md).

## Reading guide

1. **What kind of equation is it?** [Classification of second-order linear PDEs](/definitions/second-order-pde-classification.md)
   and [characteristic curves](/definitions/characteristic-curve.md). This is the
   central concept of the bundle: curves on which data cannot fix the
   derivatives, along which information propagates.
2. **What data make a problem determinate?** [Dirichlet, Neumann and Cauchy boundary conditions](/definitions/boundary-condition-types.md),
   [boundary data by equation type](/results/boundary-data-by-equation-type.md)
   (stated without proof in both sources; Arfken's table covers every
   pairing, with stability), and the one proved case, the
   [uniqueness theorem for Poisson's equation](/results/uniqueness-theorem-poisson.md).
3. **The model equations:** the [wave equation](/definitions/wave-equation.md)
   (hyperbolic) with [d'Alembert's formula](/results/dalembert-formula.md);
   the [diffusion equation](/definitions/diffusion-equation.md) (parabolic);
   the [Laplace and Poisson equations](/definitions/laplace-and-poisson-equations.md) (elliptic),
   and the [Helmholtz equation](/definitions/helmholtz-equation.md) that
   separating time from the first two leaves behind.
4. **General solutions from characteristics:** [first-order linear PDEs](/methods/first-order-linear-pde-characteristics.md)
   and [constant-coefficient second-order PDEs](/methods/constant-coefficient-second-order-general-solution.md).
5. **Solving boundary-value problems:** [homogeneous equations and problems](/definitions/homogeneous-linear-problem.md)
   (superposition), [separation of variables](/methods/separation-of-variables.md),
   [integral transform methods](/methods/integral-transform-methods.md),
   [fundamental solutions](/definitions/fundamental-solution.md) and
   [Green's functions for linear PDEs](/methods/greens-functions-for-pdes.md).
6. **ODE support** (what the PDE methods rely on): [solution methods for first-order ODEs](/methods/first-order-ode-solution-methods.md)
   (characteristic equations), [structure of linear ODE solutions](/results/linear-ode-solution-structure.md),
   the [Wronskian](/definitions/wronskian.md), [variation of parameters](/methods/variation-of-parameters.md),
   [Green's functions for linear ODEs](/methods/greens-functions-for-linear-odes.md),
   and [series solutions (Frobenius' method)](/methods/frobenius-series-solutions.md)
   for the Bessel and Legendre equations that separation produces.

## Folders

* [Definitions](/definitions/index.md) · [Methods](/methods/index.md) · [Results](/results/index.md) · [Sources](/sources/index.md) · [Bibliography](/bibliography.md)
