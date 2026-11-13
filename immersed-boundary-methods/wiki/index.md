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

**Corpus:** all 65 archived papers ingested in 7 chunks. Chunk 1 holds
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
Chunk 5 (2023–2025) brings a second history with a five-condition definition
of sharpness ([Mittal & Seo 2023](/sources/mittal-2023.md)), high-order
boundary treatments for compressible flow ([Liu et al. 2024](/sources/liu-2024.md),
[Turner et al. 2024](/sources/turner-2024.md), [Huang et al. 2024](/sources/huang-2024.md),
[Qi et al. 2024](/sources/qi-2024.md), [Marashi & Hejranfar 2025](/sources/marashi-2025.md)),
provably stable weighted state redistribution ([Berger & Giuliani 2024](/sources/berger-2024.md)),
the CutFEM review ([Burman et al. 2025](/sources/burman-2025.md)),
isogeometric slender rods ([Agrawal et al. 2024](/sources/agrawal-2024.md))
and penalized plasma walls ([Munschy et al. 2024](/sources/munschy-2024.md)).
Chunk 6 (2025–2026) closes the archive: the shifted boundary method for
compressible flow with shocks ([Zeng et al. 2025](/sources/zeng-2025.md)) and
as a polynomial correction on moving curved meshes ([Boscheri & Ciallella 2025](/sources/boscheri-2025.md)),
inverse Lax–Wendroff coupling with deformable solids ([Liu et al. 2025](/sources/liu-2025.md)),
energy-stable DG with state redistribution ([Taylor et al. 2025](/sources/taylor-2025.md)),
constrained-transport MHD embedded boundaries ([Jones et al. 2026](/sources/jones-2026.md)),
shock-adaptive high-order ghost cells ([Yang et al. 2026](/sources/yang-2026.md)) and
Riemann-based ghost fluids for shocked energetic materials ([Okafor et al. 2026](/sources/okafor-2026.md)).
Chunk 7 (2026-11-13) adds eight papers on bodies moving across fixed grids:
cell merging for moving cut cells ([Bayyuk et al. 1993](/sources/bayyuk-1993.md)),
implicit space-time cut cells ([Murman et al. 2003](/sources/murman-2003.md)),
the geometric-conservation origin of spurious pressure oscillations
([Seo & Mittal 2011](/sources/seo-2011.md)), smoothly varying moving cut cells
([Meinke et al. 2013](/sources/meinke-2013.md), [Schneiders et al. 2013](/sources/schneiders-2013.md),
[Schneiders et al. 2016](/sources/schneiders-2016.md)), moving-boundary flux
stabilization ([Bennett et al. 2018](/sources/bennett-2018.md)) and space-time
aggregated finite elements ([Badia et al. 2023](/sources/badia-2023.md)).

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
   [small-cell problem](/definitions/small-cell-problem.md),
   [cell merging](/methods/cell-merging.md) and
   [redistribution](/methods/redistribution.md); the
   [ghost-cell method](/methods/ghost-cell-method.md), the workhorse of
   sharp-interface finite differences, its [fresh-cell problem](/definitions/fresh-cell-problem.md)
   for moving bodies, and its high-order relative, the
   [inverse Lax–Wendroff](/methods/inverse-lax-wendroff.md) treatment;
   [CutFEM](/methods/cutfem.md), the finite-element counterpart, and the
   [shifted boundary method](/methods/shifted-boundary-method.md), which avoids
   cut cells; [state redistribution](/methods/state-redistribution.md), the
   second-order successor of flux redistribution.
5. **High order and compressible flow.**
   [High-order immersed boundary treatments for compressible flow](/methods/high-order-immersed-boundary.md):
   inverse Lax–Wendroff, polynomial weighted-least-squares ghost values with
   or without image points, DG polynomials at image points, summation-by-parts
   embedded boundaries and hybrid compact–WENO interiors, side by side.
6. **Moving and deforming bodies.** [Fluid–structure coupling](/methods/fluid-structure-coupling.md):
   loose and strong coupling, added mass, and the structural models;
   [spurious force and pressure oscillations](/definitions/spurious-force-oscillations.md)
   (one contradiction open on their primary cause) and the
   [geometric conservation law](/definitions/geometric-conservation-law.md)
   that cells changing status violate.
7. **High Reynolds numbers.** [Wall models for immersed boundaries](/methods/wall-models-for-immersed-boundaries.md).
8. **Cross-cutting properties.**
   [First-order accuracy of regularized-delta forcing](/results/first-order-accuracy-of-regularized-delta-forcing.md)
   and [discrete conservation](/properties/discrete-conservation.md).
9. **Validation cases.** [Flow past a circular cylinder](/benchmarks/flow-past-circular-cylinder.md),
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
