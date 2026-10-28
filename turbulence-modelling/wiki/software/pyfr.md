---
type: Software
title: "PyFR"
description: "PyFR is the open-source Python framework for high-order flux reconstruction on mixed unstructured grids, generating kernels for CPU and GPU back ends; this page records its v2.0.3 design, its four stabilization options for under-resolved runs, its synthetic-eddy inflow, its validation and scaling on Taylor–Green vortices, and the studies run with it."
status: established
aliases: [PyFR v2.0.3, PyFR v0.1.0]
tags: [software, flux-reconstruction, gpu, implicit-les, numerical-dissipation]
timestamp: 2026-10-28T17:00:00Z
---

# PyFR

**PyFR** is an open-source (BSD 3-clause) Python framework that implements
Huynh's [flux reconstruction](/methods/flux-reconstruction.md) (FR) for
scale-resolving simulation (LES, implicit LES, DNS) near complex geometry.
Python generates the compute kernels for C/OpenMP, CUDA, OpenCL, HIP and
Metal back ends. [Witherden et al. (2025)](/sources/witherden-2025.md)
describe the release v2.0.3, which updates the original v0.1.0 paper with
the features added over more than 30 releases, with industrial adoption as
the stated aim (program summary, §1). They call FR "a form of
discontinuous spectral element method" (§2); see
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) and the
[spectral difference method](/methods/spectral-difference-method.md) for
the relatives. Earlier bundle sources use or name the code:
[Dzanic et al. (2022)](/sources/dzanic-2022.md) implement
[PANS](/methods/partially-averaged-navier-stokes.md) in it;
[Ferrer et al. (2023)](/sources/ferrer-2023.md), Table 1, compare
[HORSES3D](/software/horses3d.md) with it among open-source high-order
codes; [Kurz et al. (2025)](/sources/kurz-2025.md), §1, name it among the
GPU high-order solvers, for flux reconstruction.

## Formulation

Witherden et al. (2025, §2, Eqs. 1–7) recap FR on a mixed mesh. Each
element is mapped to a reference element with Jacobian determinant
$\mathcal J$, and the transformed flux is $\mathcal J$ times the inverse
Jacobian matrix times the physical flux. A step of the scheme has four
parts:

1. interpolate the solution from the solution points to the flux points on
   the element surface (which conform across interfaces);
2. compute a common normal flux at each flux point, "e.g. an appropriate
   Riemann solver";
3. evaluate the discontinuous transformed flux at the solution points and
   its normal component at the flux points;
4. form the divergence at the solution points as the divergence of the
   discontinuous flux polynomial plus, for every flux point, the jump
   between the common and the discontinuous normal flux times the
   divergence of that flux point's correction function.

The result feeds an explicit time integrator. Point sets used in the paper
are the $\alpha$-optimized points on tetrahedra and Gauss–Legendre–Lobatto
points on hexahedra (Fig. 1, §5.1). The polynomial degree is the registry's
$N$ (the paper writes $\wp$).

The earlier configuration of Dzanic et al. (2022, §2.3) is a Rusanov-type
Riemann solver, BR2 viscous fluxes and explicit fourth-order Runge–Kutta,
run at $N=1$ and $N=3$ (see the table of interface fluxes on
[flux reconstruction](/methods/flux-reconstruction.md)).

## Performance portability (v2.0.3)

As described by Witherden et al. (2025, §3.1):

- **Kernel language.** A domain-specific language derived from Mako gives
  "complete feature parity" across the five back ends (Fig. 2). It supports
  reductions (an argument annotated `reduce(op)` is reduced into memory by
  atomic operations) and automatic staging of reused read-only arguments in
  GPU shared memory.
- **Matrix multiplications.** Operations $\mathsf C\leftarrow\mathsf A\mathsf B+\beta_{\mathrm{mm}}\mathsf C$
  with a constant operator matrix $\mathsf A$ (page-local symbols) are served by GiMMiK on
  CUDA and HIP, bespoke fully unrolled kernels that skip multiplications by
  zero, and by libxsmm on CPUs. Each generated kernel is benchmarked against
  dense BLAS at run time and the fastest is kept. When the flux points are a
  subset of the solution points the multiplication is skipped.
- **Data layout.** The structure-of-arrays layout of v0.1.0 is replaced by
  an array-of-structures-of-arrays packing whose block size follows the
  hardware vector length, plus a second level of blocking on CPUs (Fig. 3).
- **Task graphs.** One graph of kernels per right-hand-side evaluation,
  native CUDA graphs on NVIDIA hardware; HIP and Metal emulate them by serial
  submission (HIP graphs were found slower than direct launches in
  preliminary studies), OpenCL uses out-of-order queues. On a 2D
  incompressible cylinder case on one V100 the run time falls from 256 s to
  122 s with task graphs.
- **Cache blocking** of kernel calls on CPUs, which "can improve performance
  by a factor of two" (as the authors cite their earlier work); eight
  hexahedra at $N=4$ for the Euler equations in double precision need
  160 kB of solution and flux storage.
- **Multi-node.** mpi4py with a standardized message format, so that ranks
  can run on different back ends; GPU-aware MPI, with "twofold performance
  improvements" in "the most extreme cases" on A100 clusters (as cited).

## Stabilization for under-resolved runs

The authors state that PyFR is often used for under-resolved DNS, "also
referred to as ILES", in which FR suffers aliasing-driven instabilities, and
v2.0.3 offers four remedies (§3.2; see
[implicit LES](/definitions/implicit-les.md)):

| Strategy | What it does | Cost and parameters as stated |
|---|---|---|
| [modal filtering](/methods/explicit-modal-filtering.md) | periodic damping of the high modes | conservative and cheap but indiscriminate; strength, frequency and cut-off mode are free parameters |
| anti-aliasing | quadrature-based least-squares projection of the flux (Polyquad rules) | results "markedly superior" to modal filtering (as cited); run time "typically doubled" in 3D at anti-aliasing degree $N+1$ |
| [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md) | Persson–Peraire-type viscosity added in elements with Gibbs-type behaviour | needs parameterization; can reduce the maximum stable explicit time step |
| entropy filtering | modal filter applied only in elements that violate positivity of density or pressure or a minimum-entropy bound | the bound is the minimum discrete entropy of the element and its Voronoi neighbours at the previous step; "does not explicitly require any problem-dependent parameterisation", with a small fixed tolerance for finite precision |

Entropy filtering is the method of Dzanic & Witherden (2022) and of Trojak &
Dzanic, as Witherden et al. cite them; the double Mach reflection and a
viscous shock tube are named as demonstrations, without results in the
paper. The same filter is compared with a switched modal filter in the FR
code of Wang (2024) on [flux reconstruction](/methods/flux-reconstruction.md).

## Further capabilities (v2.0.3)

- **Elements and partitioning** (§3.3): quadrilaterals and triangles;
  hexahedra, prisms, tetrahedra, and pyramids with an affine base.
  Built-in METIS and SCOTCH partitioning, weighted partitioning (a
  quadrilateral weighted 3/2 of a triangle in Fig. 6), tracking of MPI wait
  times, and balanced partitioning with an equal count of each element type
  per domain. A single set of element weights cannot work for mixed meshes,
  because the relative cost depends on "around half a dozen" parameters.
- **Metrics** (§3.4): the cross-product metric of v0.1.0 has twice the
  polynomial order of the shape function on curved grids, its discrete
  divergence need not vanish and free-stream preservation is lost; v2.0.3
  builds the metric terms as a curl, divergence-free regardless of the
  approximation error (Fig. 7, $N=2$ on cubically curved tetrahedra). See
  [geometric conservation law](/properties/geometric-conservation-law.md).
  For linear elements the metrics are computed on the fly from $3\times8=24$
  vertex terms instead of $3^2\times125=1125$ stored terms of a hexahedron at
  $N=4$.
- **Time stepping** (§3.5): adaptive steps from embedded pairs of
  low-storage Runge–Kutta methods.
- **Incompressible solver** (§3.6): artificial compressibility with dual
  time stepping, accelerated by polynomial multigrid and locally adaptive
  pseudo-time steps.
- **Files** (§3.7): HDF5 with 64-bit integers, the configuration history
  embedded, export to high-order and parallel VTU.
- **Plugins** (§3.8): pure-Python plugins with read-only access to the
  solution and its gradients: point sampling, time averages (of arbitrary
  functions of the primitives and gradients, with variances), fluid forces,
  in-situ visualization with Ascent, and a turbulence-generation plugin
  that injects isotropic eddies of the synthetic eddy method through a
  source term with prescribed intensity and length scale. Its cost scales
  with the number of eddies intersecting an element, not the number
  injected, and the eddies are generated on the device by a PCG generator
  from one 32-bit seed (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

## Validation and performance

**Supersonic Taylor–Green vortex** (§5.1, Figs. 11–12, Table 1). The
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$ and
Mach 1.25 with Sutherland viscosity, run on $16^3$ to $128^3$ hexahedra at
$N=3$ ($64^3$ to $512^3$ degrees of freedom) with Gauss–Legendre–Lobatto
points and entropy filtering. The solenoidal dissipation $\varepsilon_s$
(the volume average of $\mu\,\omega_i\omega_i$) agrees "excellent[ly]" with
the reference of [Chapelier et al. (2024)](/sources/chapelier-2024.md)
(TENO finite differences on $2048^3$ points). At equal resolution and
order PyFR "generally show[s] less shock dissipation": its dilatational
dissipation $\varepsilon_d$ (the volume average of
$\tfrac43\mu(\partial_iu_i)^2$) is closer to the reference than that of
CODA (modal DG with artificial viscosity), [FLEXI](/software/flexi.md)
(DGSEM with [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md))
and SD3D (spectral difference with artificial viscosity), which the authors
read as "the entropy filtering shock capturing approach does not introduce
excessive numerical dissipation" (see
[numerical dissipation](/properties/numerical-dissipation.md)). The
comparison data were supplied by Chapelier and co-workers.

**Strong scaling** (§5.2, Tables 2–3, Fig. 13). A subsonic Taylor–Green
vortex (Mach 0.08, constant viscosity) on $12\times105^3=13\,891\,500$
tetrahedra with "seventh-order solution polynomials" and $\alpha$-optimized
points, in double precision; its enstrophy on 1024 MI250X GCDs agrees with
van Rees et al. (as cited). Throughput is measured in GDoF/s, the number of
degrees of freedom over the time of one right-hand-side evaluation.

| Ranks | Frontier, MI250X GCD (GDoF/s, efficiency) | Alps, GH200 (GDoF/s, efficiency) |
|---|---|---|
| 16 | 26.21, 1.00 | 96.07, 1.00 |
| 128 | 193.37, 0.92 | 806.95, 1.05 |
| 512 | 669.80, 0.80 | 2861.56, 0.93 |
| 2048 | 1537.68, 0.46 | 5753.96, 0.47 |

One GH200 is about 3.7 times faster than one MI250X GCD; the authors
attribute this to memory bandwidth and to the larger caches that matter for
the interface kernels. Frontier ran without HIP-aware MPI, and since Alps
moves about 3.7 times more data over the same Slingshot network at 2048
ranks with similar efficiency, the authors infer that the network is not
the limit on Frontier and point to the missing HIP-aware MPI and native HIP
graphs. Per GPU, throughput rose by a factor 49.2 over a decade, from 0.122
GDoF/s on a K40c with v0.2.2 (fourth-order, mostly tetrahedral mesh) to
6.004 GDoF/s on a GH200 (the 16-rank case above), which the authors call
"conservative" because seventh order needs more operations per degree of
freedom. Earlier, PyFR runs reached 13.7 DP-PFLOP/s (58% of peak) on
18 000 K20X GPUs of Titan, shortlisted for the 2016 Gordon Bell Prize (as
cited).

## Applications in the sources

- **PANS against under-resolved DNS** (Dzanic et al. 2022): the
  [periodic hill](/benchmarks/periodic-hill.md) and the
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) at
  $Re_D=3900$, at $N=1$ and $N=3$ with equal degrees of freedom; a DNS of
  the cylinder at $N=3$ with about 55.6 million degrees of freedom gives
  $St=0.209$. Results are on
  [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
  and [implicit LES](/definitions/implicit-les.md).
- **User community** (Witherden et al. 2025, §4, as showcases without data):
  DNS of the MTU-T161 low-pressure [turbine cascade](/benchmarks/turbine-cascade.md),
  implicit LES of a model high-rise building with the incompressible
  solver, DNS of a triangular airfoil for a Martian rotorcraft, re-entry
  capsules, wind-turbine wakes with an actuator line (as a cited title; see
  [actuator line models](/methods/actuator-line-model.md)) and
  [channel flow](/benchmarks/turbulent-channel-flow.md).
- **Cost against finite volumes**, as relayed by
  [Saini et al. (2023)](/sources/saini-2023.md), §1, from Vermeire et al.
  (2017): fifth-order PyFR more accurate than a commercial finite-volume
  code but about 2 and 6 times more expensive on two cases.

## Qualifications

- Witherden et al. identify under-resolved DNS with implicit LES (§3.2);
  Dzanic et al. (2022) do the same ("URDNS"). The definitions of other
  sources are on [implicit LES](/definitions/implicit-les.md).
- Entropy filtering "does not explicitly require any problem-dependent
  parameterisation" but carries a fixed entropy tolerance, which the
  authors state is not varied between problems and does not affect
  positivity preservation (§3.2); [Wang (2024)](/sources/wang-2024-b.md), §4.4.3, calls the filter
  "not completely parameter-free" because of that tolerance (see
  [flux reconstruction](/methods/flux-reconstruction.md)).
- The factor 49.2 compares different meshes, orders, code versions and
  hardware; it is a per-GPU throughput ratio, not a speedup on one problem.
  "Seventh-order solution polynomials" (§5.2) does not say whether the degree
  is 6 or 7; the supersonic case states "third-order polynomials", order
  four in Table 1.
- Printed slips (Witherden et al. 2025, §2): Eq. (7) writes the correction
  term as $\mathfrak F_\alpha f^{(f_\perp)}-f^{(f_\perp)}$, dropping the
  tildes and the "C" superscript of the common flux defined in Eq. (5), and
  carries a stray "$*$"; the normal is hatted in Eq. (5) but not in Eq. (6);
  the third step's text indexes solution-point quantities with the
  flux-point index $\sigma$; Eq. (2) prints the intersection of all elements
  as the empty set for non-overlap. The four-step description above follows
  the text.

# Citations

- [Witherden et al. (2025)](/sources/witherden-2025.md) — program summary; §1; §2, Eqs. (1)–(7), Fig. 1 (FR recap, point sets); §3.1, Figs. 2–5 (DSL, GiMMiK and libxsmm, AoSoA, task graphs, cache blocking, GPU-aware MPI); §3.2 (four stabilization strategies); §3.3, Fig. 6; §3.4, Fig. 7 (conservative metric); §3.5–§3.8 (time stepping, incompressible solver, files, plugins, synthetic eddies); §4, Figs. 8–10; §5.1, Figs. 11–12, Table 1 (supersonic Taylor–Green vortex); §5.2, Fig. 13, Tables 2–3 (strong scaling, factor 49.2).
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — arXiv v1: §2.3 (PyFR configuration: Rusanov, BR2, fourth-order Runge–Kutta); §3.1–§3.2 (periodic hill, cylinder at $Re_D=3900$).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — Table 1 (PyFR among compared open-source high-order codes).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1 (PyFR among GPU high-order solvers).
- [Saini et al. (2023)](/sources/saini-2023.md) — §1 (fifth-order PyFR against a commercial finite-volume code, as cited).
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §4.4.3 (entropy filter not completely parameter-free); comparison with a switched modal filter in its FR code.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — reference data of the supersonic Taylor–Green comparison, as used by Witherden et al.
