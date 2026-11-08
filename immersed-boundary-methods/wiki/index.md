---
okf_version: "0.1"
---

# immersed-boundary-methods — Knowledge Bundle

Immersed boundary methods, as collected in an immersed-boundary bibliography
of 1972–2026: methods that compute flows around bodies, or across
interfaces, on grids that do not conform to them — by forcing the flow
equations, by correcting stencils with interface jumps, by ghost values, or
by clipping finite volumes — together with their accuracy, conservation and
stability, and the fluid–structure, compressible and high-order problems they
are applied to.

**Start here:** the [Notation registry](/notation.md), which is normative for
every page ($\Omega_s$ the body, $\Gamma$ the immersed boundary with normal
$\mathbf n$ out of the body, $\mathbf X(\mathbf s,t)$ its Lagrangian configuration,
$\mathbf F$ and $\mathbf f$ the Lagrangian and Eulerian force densities, $\delta_h$
the regularized delta function with kernel $\varphi$, $\mathcal S$ and $\mathcal J$
spreading and interpolation, $\eta$ and $\chi_s$ the penalization parameter and
body mask, $\kappa$ the cut-cell volume fraction, $\phi$ the level set), and the
[update log](/log.md).

**Corpus:** 40 of the 57 archived papers ingested in 4 chunks. Chunk 1 holds
the founding papers of 1972–2002:
[Peskin (1972)](/sources/peskin-1972.md) invents the immersed boundary method
for heart valves, and [Peskin (2002)](/sources/peskin-2002.md) gives its
mathematical structure; [Goldstein et al. (1993)](/sources/goldstein-1993.md)
introduce feedback forcing; [LeVeque & Li (1994)](/sources/leveque-1994.md)
the immersed interface method; [Pember et al. (1995)](/sources/pember-1995.md)
the compressible embedded-boundary method with redistribution;
[Fedkiw et al. (1999)](/sources/fedkiw-1999.md) the ghost fluid method;
[Ye et al. (1999)](/sources/ye-1999.md) the incompressible cut-cell method;
[Angot et al. (1999)](/sources/angot-1999.md) the convergence theory of
penalization; [Fadlun et al. (2000)](/sources/fadlun-2000.md) and
[Kim et al. (2001)](/sources/kim-2001.md) direct forcing. Chunk 2 (2003–2015)
brings the ghost-cell line ([Tseng & Ferziger 2003](/sources/tseng-2003.md),
[Ghias et al. 2007](/sources/ghias-2007.md), [Mittal et al. 2008](/sources/mittal-2008.md),
[Chaudhuri et al. 2011](/sources/chaudhuri-2011.md)), the review that fixed the
classification ([Mittal & Iaccarino 2005](/sources/mittal-2005.md)), Lagrangian
direct forcing for particles ([Uhlmann 2005](/sources/uhlmann-2005.md)), the
formally consistent embedded-boundary method ([Colella et al. 2006](/sources/colella-2006.md)),
the projection formulation ([Taira & Colonius 2007](/sources/taira-2007.md)),
the inverse Lax–Wendroff treatment ([Tan & Shu 2010](/sources/tan-2010.md))
and CutFEM ([Burman et al. 2015](/sources/burman-2015.md)). Chunk 3 (2014–2022)
adds the fluid–structure reviews ([Sotiropoulos & Yang 2014](/sources/sotiropoulos-2014.md),
[Griffith & Patankar 2020](/sources/griffith-2020.md)), the shifted boundary
method ([Main & Scovazzi 2018](/sources/main-2018.md), [Atallah et al. 2022](/sources/atallah-2022.md)),
state redistribution ([Berger & Giuliani 2021](/sources/berger-2021.md),
[Giuliani et al. 2022b](/sources/giuliani-2022-b.md)), strongly coupled and
material-point fluid–structure coupling ([Nair & Goza 2022](/sources/nair-2022.md),
[Ni et al. 2022](/sources/ni-2022.md)), moving embedded boundaries with AMR
([Natarajan et al. 2022](/sources/natarajan-2022.md)) and directional ghost
cells for reacting flow ([Ou et al. 2022](/sources/ou-2022.md)). Chunk 4
(2022–2023) brings provably stable high-order embedded boundaries
([Sharan et al. 2022](/sources/sharan-2022.md)), moving cut cells without
spurious pressure oscillations ([Xie et al. 2022](/sources/xie-2022.md)),
thin porous parachutes ([Boustani et al. 2022](/sources/boustani-2022.md)),
compressible penalization ([Reiss 2022](/sources/reiss-2022.md),
[Ménez et al. 2023](/sources/menez-2023.md)), DG state redistribution
([Giuliani 2022](/sources/giuliani-2022.md)), the history of the field
([Verzicco 2023](/sources/verzicco-2023.md)), small cut elements in finite
elements ([de Prenter et al. 2023](/sources/deprenter-2023.md)), the
penalty-free shifted boundary method ([Collins et al. 2023](/sources/collins-2023.md))
and GPU sharp-interface methods ([Raj et al. 2023](/sources/raj-2023.md)).

## Reading guide

1. **What an immersed boundary method is.**
   [Immersed boundary method](/definitions/immersed-boundary-method.md) is the
   hub: continuous versus discrete forcing, and the families.
   [Sharp and diffuse interface representations](/definitions/sharp-and-diffuse-interface.md)
   is the second classification, and the one that decides accuracy.
2. **Peskin's method and its operators.**
   [Classical (Peskin) immersed boundary method](/methods/classical-immersed-boundary-method.md),
   built on the [regularized delta function](/operators/regularized-delta-function.md)
   and the adjoint pair of [spreading and interpolation operators](/operators/spreading-and-interpolation.md).
3. **Forcing a prescribed boundary.**
   [Feedback forcing](/methods/feedback-forcing.md) (a controller, stiff) and
   [direct forcing](/methods/direct-forcing.md) (solved from the discrete
   equations, accuracy set by the velocity reconstruction);
   [volume penalization](/methods/volume-penalization.md) and its
   [convergence theory](/results/convergence-of-volume-penalization.md);
   the [immersed boundary projection method](/methods/immersed-boundary-projection-method.md),
   which makes the force a Lagrange multiplier.
4. **Sharp interfaces.**
   The [immersed interface method](/methods/immersed-interface-method.md),
   the [ghost fluid method](/methods/ghost-fluid-method.md), and the
   [cut-cell method](/methods/cut-cell-method.md) with its
   [small-cell problem](/definitions/small-cell-problem.md) and
   [redistribution](/methods/redistribution.md); the
   [ghost-cell method](/methods/ghost-cell-method.md), the workhorse of
   sharp-interface finite differences, its [fresh-cell problem](/definitions/fresh-cell-problem.md)
   for moving bodies, and its high-order relative, the
   [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) treatment;
   [CutFEM](/methods/cutfem.md), the finite-element counterpart, and the
   [shifted boundary method](/methods/shifted-boundary-method.md), which avoids
   cut cells; [state redistribution](/methods/state-redistribution.md), the
   second-order successor of flux redistribution.
7. **Moving and deforming bodies.** [Fluid–structure coupling](/methods/fluid-structure-coupling.md):
   loose and strong coupling, added mass, and the structural models;
   [spurious force and pressure oscillations](/definitions/spurious-force-oscillations.md).
8. **High Reynolds numbers.** [Wall models for immersed boundaries](/methods/wall-models-for-immersed-boundaries.md).
5. **Cross-cutting properties.**
   [First-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)
   and [discrete conservation](/properties/discrete-conservation.md).
6. **Validation cases.** [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md),
   [flow past a sphere](/benchmarks/flow-past-sphere.md) and
   [shock–obstacle interaction](/benchmarks/shock-obstacle-interaction.md).

## Catalogs

- [Definitions](/definitions/index.md)
- [Methods](/methods/index.md)
- [Operators](/operators/index.md)
- [Results](/results/index.md)
- [Properties](/properties/index.md)
- [Benchmarks](/benchmarks/index.md)
- [Sources](/sources/index.md)
- [Bibliography](/bibliography.md) — every work cited by an ingested source.
