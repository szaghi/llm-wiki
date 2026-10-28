---
type: Method
title: "Mesh adaptation for turbulent-flow simulation"
description: "Changing the mesh (h, p or hp; isotropic or anisotropic) from an error estimate or refinement criterion in a turbulent-flow computation: Hessian and metric criteria for RANS, Hessians scaled by DG error estimators, time-averaged criteria for hybrid RANS/LES, LES modelling-residual, small-scale-energy, residual and truncation-error estimators, error transport equations, output-based estimates for chaotic flows, and refinement as a dissipation control."
status: established
aliases: [unsteady residual indicator, smoothness indicator, adaptive mesh refinement, AMR, adaptive grid refinement, AGR, anisotropic mesh adaptation, metric-based mesh adaptation, hp-adaptation, average-based mesh adaptation, goal-oriented mesh adaptation, grid adaptation for LES, LES modelling residual, Toosi–Larsson residual estimator, tau-estimation, p-adaptation, Hessian scaling, error transport equations, ETE]
tags: [mesh-adaptation, hybrid-rans-les, rans, dg, numerical-dissipation, wmles]
timestamp: 2026-10-28T07:05:00Z
---

# Mesh adaptation for turbulent-flow simulation

**Mesh adaptation** changes the discretization during a computation so that
resolution goes where an error estimate or refinement criterion says it is
lacking. The sources of this bundle use three mesh operations: h-refinement
by cell division or by remeshing, p-enrichment of element polynomial
degree $N$, and their combination (hp-adaptation); the cells may be
isotropic or stretched along a metric (anisotropic). The adapted quantity
is a mesh, not a model: in RANS the closure is fixed and adaptation
controls the discretization error; in scale-resolving simulation the mesh
also sets the resolved/modelled split of
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and the
[numerical dissipation](/properties/numerical-dissipation.md) of implicit
LES, so the mesh change itself perturbs the turbulence. A
[boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md)
is the a priori counterpart for wall-modelled LES: its size rule is set
from an estimate of $\delta$, not adapted from the solution.

## Components

Every adaptive procedure in the sources has the same four parts.

| Part | Mozaffari et al. (2022) | Alauzet et al. (2022) | Basile et al. (2023) | Blind et al. (2023) | Ferrer et al. (2023) | Martin-Alvarez et al. (2022) | Schotte et al. (2026) | Ims & Wang (2023) |
|---|---|---|---|---|---|---|---|---|
| Flow and model | incompressible hybrid RANS/LES (IDDES, DDES-SST) and RANS, ISIS-CFD | steady compressible RANS, Spalart–Allmaras without $f_{t2}$, Wolf | compressible ZDES on the negative Spalart–Allmaras model, modal DG (CODA) | wall-resolved and wall-modelled LES with the Vreman model, DGSEM ([FLEXI](/software/flexi.md)) | compressible and multiphase flows, DGSEM ([HORSES3D](/software/horses3d.md)) | ideal MHD, cosmological galaxy formation, RAMSES | steady compressible RANS, negative Spalart–Allmaras, modal DG with $N=1$–3 (CODA) | compressible implicit LES (no SGS model), FR/CPR ([hpMusic](/software/hpmusic.md)) |
| Criterion | Hessians of $p$ and $u_i$, time-averaged | $L^4$ Mach-number interpolation error or adjoint-weighted goal-oriented estimate | modal small-scale energy plus inter-element jumps; modal-decay smoothness | directional LES modelling residual from a modal test filter, time- and element-averaged | truncation error ($\tau$-estimation); interface tracking for multiphase | mass per cell (quasi-Lagrangian) or a density threshold (quasi-Eulerian) | $L^4$ Mach-number Hessian for the anisotropy, a DG small-scale estimator for the size | unsteady residual at degree $N+1$; modal smoothness (Persson–Peraire); directional small-scale energy (Toosi–Larsson variant); all time-averaged |
| Operation | anisotropic h-refinement and derefinement of hexahedra by cell division | anisotropic remeshing of tetrahedra to a metric (Feflo.a) | isotropic remeshing (MMG) plus p-enrichment, $N\in\{1,2,3\}$; prism layer frozen | anisotropic hexahedral grids built by hand to the target spacing, 2-to-1 mortars | anisotropic p-adaptation, a degree per element and direction, mortar faces | octree refinement, at most one level jump | anisotropic remeshing of triangles and tetrahedra to a metric (Tucanos) | isotropic h-refinement of curved cells into equal sub-cells following the parent's curvature, fixed $N$, mortar faces |
| Driver | refinement every 25 steps (backward-facing step) | mesh-convergence loop at doubled complexity | static steps, dof count doubled per step | post-processing between full LES runs, about four times the elements per step | one step on a converged moderate-degree solution (steady) or at fixed intervals (unsteady) | every step, on the running flow | fixed-complexity loop of 5–20 iterations, then a higher complexity | top 20% of cells per round plus size and clumping constraints, restart from interpolated fields |

The models and codes have their own pages:
[detached-eddy simulation](/methods/detached-eddy-simulation.md) (the
DDES, IDDES and ZDES of Mozaffari et al. and Basile et al.), the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) (Alauzet et
al., Basile et al.), [RAMSES](/software/ramses.md) and the
[small-scale dynamo](/results/small-scale-dynamo.md) (Martin-Alvarez et
al.); Mozaffari et al.'s calibration case is the
[backward-facing step](/benchmarks/backward-facing-step.md); Blind et al.
adapt for [wall-modelled LES](/methods/wall-modelled-les.md) of
[channel flow](/benchmarks/turbulent-channel-flow.md) and a transonic
airfoil. [Dahlin et al. (2022)](/sources/dahlin-2022.md) (§3) run their
solar coronal MHD simulations in the adaptive-mesh code ARMS, with the
maximally refined grid covering the separatrix dome and a volume above it;
they state no refinement criterion. [Ruan et al. (2023)](/sources/ruan-2023.md)
(§2) run a 3D resistive MHD solar-flare simulation in MPI-AMRVAC with a
$64^3$ base grid and five refinement levels, an effective $1024^3$ with
cells below 100 km in a 100 Mm box; they too state no refinement
criterion. The scheme is HLL with a third-order limiter on the coarse
levels and the second-order van Leer limiter on the fine levels in
high-gradient regions; no SGS model is used, and the paper does not
discuss numerical dissipation. [Sun et al. (2023)](/sources/sun-2023.md)
(§2.2.2, §3.9) adapt OpenFOAM's hexahedral refinement library to 2-D
quadrilaterals for laminar and inviscid detonation computations: a cell
is split into four when the face-centre $\lvert\nabla\rho\rvert$ exceeds a
refinement threshold and recombined below a lower coarsening threshold,
with parent values copied to the children and children averaged on
coarsening. Combined with dynamic load balancing of the chemistry, it
cuts the cell count of an oblique-detonation case to about 1/6 and the CPU
time to about 1/5 of the uniform mesh with nearly identical steady
structure (Figs. 15–16; see [OpenFOAM](/software/openfoam.md)).
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md) (§4.6, Fig. 8; §6.2,
Figs. 12–13), reviewing high-order discontinuous schemes for multiphase
and reacting flows, show the same gradient criterion in DG: isotropic
h-refinement with hanging nodes, five refinement and derefinement levels
driven by $\lvert\nabla\rho\rvert$ for a Mach 4 step (from the second
author's earlier work, as cited), and, for a reacting Mach 8 flow over a
capsule-like body, isotropic h-refinement at the bow shock combined with
p-enrichment near the wall; for multiphase flows the cited criteria are a
range or gradient of the interface scalar. Neither case is turbulent and
no reference data are shown. In the one-dimensional turbulence model
reviewed by [Chen et al. (2024b)](/sources/chen-2024-c.md) (§3.1) the
line itself is adapted in space and time (Lignell et al. 2013, as cited),
avoiding excessive adaptation, which would add numerical transport, and
easing the load imbalance between regions with many and few eddy events
(see [one-dimensional turbulence](/methods/one-dimensional-turbulence.md)).

## Hessian and metric criteria

For a second-order scheme the local interpolation error of a variable $q$
scales as its Hessian times the squared cell size. Both RANS-derived
criteria rest on this.

**Equidistributed Hessian criterion (Mozaffari et al. 2022, §2, Eqs. 1–4).**
A metric tensor $\mathcal K$ (page-local; the paper's $C$, renamed to keep $\mathcal C$ for the complexity below) is built from the Hessian
$H(q)$; with $\lvert H\rvert$ the tensor with the same eigenvectors and the
absolute eigenvalues, equidistribution of a second-order error gives
$\mathcal K=\lvert H(q)\rvert^{1/2}$. The cells are refined until each of
their three edge vectors $\boldsymbol d_j$ satisfies
$\lVert\mathcal K\,\boldsymbol d_j\rVert=T_r$, with $T_r$ (page-local) one
global threshold. The pressure–velocity criterion takes the tensor maximum
of $\lvert H(p)\rvert$ and $\rho U\lvert H(u_i)\rvert$, $U=\lvert\boldsymbol u\rvert$,
before the square root. A minimum cell size, refinement boxes and
boundary-layer protection keep the mesh regular.

**Continuous-mesh metric (Alauzet et al. 2022, §6, Eqs. 30–35).** A
Riemannian metric field $\mathcal M(\boldsymbol x)$ (page-local) prescribes
a unit mesh, and the optimal mesh minimizes an error functional at fixed
complexity $\mathcal C(\mathcal M)=\int_\Omega\sqrt{\det\mathcal M}$, which
is about $\sqrt2/12$ times the number of tetrahedra. For the
interpolation error in $L^p$ of a sensor with Hessian $H$ in $d$
dimensions, the optimal metric is

$$\mathcal M_{L^p}=\mathcal N^{2/d}\left(\int_\Omega\det\lvert H\rvert^{\frac{p}{2p+d}}\right)^{-2/d}\det\lvert H\rvert^{-\frac{1}{2p+d}}\,\lvert H\rvert,$$

with $\mathcal N$ the target complexity. The sensor is the local Mach
number and $p=4$, following a cited finding that $L^4$ adapts boundary
layers faster in RANS than $L^2$ (§6.1). The **goal-oriented** variant
bounds the error of an output functional by an adjoint-weighted sum of
$L^1$ interpolation errors of the conservative variables, with weights
built from the discrete adjoint and scaled by $(\mu+\mu_t)/\rho$ (§6.2);
the turbulence equation is left out of the estimate (Remarks 5.1, 6.1).
The output functionals are turbomachinery quantities (mass flow,
total-pressure and total-temperature ratios, isentropic efficiency, loss
coefficient), differentiated including the rotating-frame chain rule (§5).

**The same metric for a wake to 20 spans (Bouhafid et al. 2024).**
[Bouhafid et al. (2024)](/sources/bouhafid-2024.md) (App. A, Eqs.
A.1–A.3, Fig. 32) use the continuous-mesh $L^p$ metric of Loseille and
Alauzet with the Feflo.a remesher for steady RANS of a full aircraft (the
NASA Common Research Model in cruise with engines, $M_\infty=0.85$, not
the high-lift version), as the first stage of a RANS-then-LES wake computation.
Their choices differ from Alauzet et al.'s turbomachinery ones:

- *Sensor and norm.* A kinetic-energy sensor $\tfrac12\lvert\boldsymbol u\rvert^2+k$
  in the $L^2$ norm, which, citing earlier work, they state gives more
  wake resolution than $L^4$ (App. A).
- *Hessian.* Recovered from a P2 reconstruction of the solution by double
  $L^2$ projection or a Green formula, with absolute eigenvalues.
- *Loop.* Solve, metric, mesh, interpolate, three to five times per
  complexity, then raise the complexity; twelve iterations in all, to
  about $110\times10^6$ cells.
- *Walls.* The aircraft surface mesh is fixed, with ten prism layers and
  wall functions at $y^+\approx80$ (about 40 million prisms), whereas
  Alauzet et al. adapt purely tetrahedral meshes to the wall.

The initial coarse mesh underpredicts the wake circulation through
numerical diffusion; iterations 6, 9 and 12 approach the elliptic-loading
value $\Gamma=528\ \mathrm{m^2/s}$ (page-local $\Gamma$, circulation;
$C_L=0.5$), and the vortex core radius, growing linearly with distance,
is mesh-converged over the last three iterations (§4.2.2, Fig. 12). On a
validation wing with a jet the adapted RANS mesh has 10 M tetrahedra and
0.85 M prisms (§3). The adapted RANS field is then sliced and passed to a
temporal LES on a fixed mesh (see
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)).

Mozaffari et al. (2022, §3.3) note that Toosi and Larsson derive "an almost
identical criterion for LES starting from a directional equidistribution
of the turbulence", and take this as support for using the Hessian in
hybrid RANS/LES.

## Indicators for scale-resolving DG (Basile et al. 2023)

Basile et al. (2023, §3) drive hp-adaptation of a modal DG discretization
with two time-averaged indicators computed on momentum.

- **Error estimator (Eqs. 8–10).** The sum, each min–max normalized over
  the mesh, of the small-scale energy density (the energy of the highest
  modal level, $\lVert(\rho\boldsymbol u)_N-(\rho\boldsymbol u)_{N-1}\rVert^2_{L^2(K)}/\lvert K\rvert$
  on element $K$) and of the mean squared inter-element jump of momentum.
  The small-scale energy alone is reliable only at high $N$; the jump is
  reliable at every degree. The authors give the small-scale energy a
  turbulence reading: the energy at the discretization cutoff, related to
  subgrid activity.
- **Smoothness indicator (Eqs. 11–12).** The exponent $\sigma$ (page-local)
  of a least-squares fit $E^{(q)}\simeq C_Eq^{-\sigma}$ of the modal energy
  against the modal degree $q$, excluding $q=0$, so computable only for
  $N\ge2$. The threshold is $\sigma=5/3$, the inertial-range slope,
  following Chapelier and Lodato's spectral-element dynamic model, in which,
  as Basile et al. cite it, the threshold was evaluated a priori from
  Taylor–Green DNS at $Re=5000$ (§3.2). Elements with $\sigma>5/3$ are p-enriched (up
  to $N=3$), the others h-refined to the size
  $h^*=h(\epsilon^*/\epsilon)^{1/m}$ with $m=N+1$ if smooth and 1
  otherwise ($\epsilon$, $\epsilon^*$ the element and target errors,
  page-local), with at most a factor 4 per step (Eq. 19).

This replaces the decay-rate formulation of Mavriplis used in the authors'
earlier RANS hp-adaptation; the authors justify it by the two cutoffs of
DG (mesh and full discretization), between which the element's modal
spectrum lies, and take the threshold $5/3$ from the inertial-range slope (§3.2). Pure p-adaptation on a
fixed mesh would need very high degrees, with load-balancing problems,
higher cost per degree of freedom and aliasing instabilities (§1).

## LES modelling residual (Blind et al. 2023)

[Blind et al. (2023)](/sources/blind-2023.md) transfer the grid-adaptation
method of Toosi and Larsson (as they cite it, §1–2) from finite-difference
and finite-volume codes to the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md). The
version read is the arXiv v1, whose title differs from the published one.
Page-local notation:

- $\boldsymbol w_\Delta$ is the discrete solution and
  $\partial_t\boldsymbol w_\Delta=\mathcal R_\Delta(\boldsymbol w_\Delta)$
  the discrete equations;
- the hat is a test filter, as in the registry;
- $h_i$ is the element spacing in direction $i$.

**Why a modelling residual.** Classical residual estimates (leading
Taylor-series terms, or interpolating the solution onto a finer mesh) do
not work for LES. The finer-mesh solution would contain smaller scales,
and LES is far from the asymptotic range, so many Taylor terms are large
(§2.2). The estimator instead evaluates the residual at an imagined
coarser resolution $\hat\Delta$, assuming that the test filter commutes
with the time derivative (Eq. 2):

$$\mathcal E_{\hat\Delta}=\mathcal R_{\hat\Delta}(\hat{\boldsymbol w}_\Delta)-\widehat{\mathcal R_\Delta(\boldsymbol w_\Delta)},$$

where $\mathcal E$ (page-local) is the modelling residual. It is the part
of the error source due to under-resolved small-scale turbulence;
numerical error is excluded. It is evaluated at $\hat\Delta$ rather than
$\Delta$ so as not to double-count scales the SGS model already
represents. In $\mathcal R_{\hat\Delta}$ the SGS model uses the
test-level length scale. For implicit LES without an explicit model, the
SGS terms vanish in the estimate (§2.2).

**DG realization (contribution, §2.3).**

- *Test filter.* An element-local, uni-directional modal cutoff. With
  polynomial degree $N=5$, the modes of degree 4 and 5 are zeroed in one
  direction only. Filtering each direction in turn gives three residual
  fields per hexahedral element, which allows anisotropic adaptation. It
  works equally on unstructured grids. The authors state that the method
  transfers to "any DG or related scheme ... as long as an element-local
  filter operation can be specified" (§2.1).
- *Change at the test level.* Only the SGS length scale changes. The
  Vreman length scale $\Delta=V_e^{1/3}/(N+1)$, with $V_e$ the element
  volume, becomes $\hat\Delta=[(N+1)/(N_f+1)]^{1/3}\Delta$, where
  $N_f=3$ (page-local) is the highest retained mode.
- *Exact square.* The residual is mapped to degree $2N$ before squaring, so
  $\mathcal E_i\mathcal E_i$ is represented exactly.
- *Element averaging.* The squared residual is averaged over each element
  before the time and homogeneous averaging. Without this, the estimator
  flags element boundaries, an artefact of the discontinuous solution and
  of overshooting gradients in under-resolved regions. The averaging makes
  the target spacing piecewise constant per element. The authors find the
  estimator "most efficient when applied elementwise and not per
  collocation point" (§5).

**Optimal spacing (§2.4, Eqs. 4–6).** The directional indicator is
$\mathcal G(\boldsymbol x,\boldsymbol n)=\sqrt{\langle\mathcal E_i\mathcal E_i\rangle}$,
with $\boldsymbol n$ the filter direction and $\langle\cdot\rangle$ the
time, homogeneous-direction and element average. It is modelled as
$\mathcal G=\varrho_r\,h^{a}$, with $\varrho_r$ a residual density and
$a=2$ (page-local). The authors call $a=2$ "almost certainly larger than
the 'correct' value in most flow scenarios"; a large exponent damps the
variation of the optimal spacing. Minimizing the residual in all
directions at a fixed number of elements gives

$$\varrho_{r,i}\,h_{i,\mathrm{opt}}^{a}\,V_{\mathrm{opt}}=\Lambda,\qquad i=1,2,3,\qquad V_{\mathrm{opt}}=\prod_m h_{m,\mathrm{opt}}:$$

the element-integrated residual is equidistributed in space and direction,
independently of the norm used to combine directions. $\Lambda$ follows by
root-finding from the target element count.

**Workflow (§2.5, §3).**

- *Between runs.* Adaptation is a post-processing step between full LES
  runs, and the grids are built by hand to mimic the target spacing;
  automation is future work. In the channel, each new grid has about four
  times the elements of the previous one.
- *Mortars.* FLEXI's 2-to-1 mortar interfaces let the wall-parallel spacing
  coarsen away from the wall. The smallest required spacing is kept until
  the optimal spacing has at least doubled, and then an interface is
  inserted (§3.2).
- *Convergence.* The residual says nothing about whether a grid is
  converged; that must be judged on quantities of interest (§2.5).
- *Wall-modelled LES.* The estimator sees the strongest under-resolution
  next to the wall, but below $h_{\mathrm{wm}}$ under-resolution is a
  choice. The target spacing of the cells between the wall and
  $h_{\mathrm{wm}}$ is therefore reset to its value at $h_{\mathrm{wm}}$, in
  all directions, a rule credited to Toosi (personal communication). The
  exchange location may then lie in the second cell (§3.3).

**Results.**

| Case | Start | Final iteration | Outcome |
|---|---|---|---|
| Wall-resolved channel, $Re_\tau=550$ (§3.1, Table 1) | $10\times2\times3$ elements | $l=4$: $50\times9\times36=16{,}200$ elements, 3,499,200 DOF; wall spacing per DOF $(\Delta x^+,\Delta y^+,\Delta z^+)=(18.33,1.28,7.64)$ | mean velocity converged to DNS at $l=4$, Reynolds stresses at $l=3$; spacing sequence "similar" to Toosi–Larsson's finite-difference one; spacing "acceptable (albeit a bit fine)" |
| Wall-resolved channel, $Re_\tau=2000$, mortars (§3.2, Tables 2–3) | 60 elements | $l=5$: 142,662 elements, 30,814,992 DOF, 128,154 elements saved | mortars save "up to approx. 50%" of the elements of a structured mesh of the same spacing; the time step is unchanged, so the saving is in processor count |
| Wall-modelled channel, $Re_\tau=2000$, Vreman constant 0.11, Spalding wall law, $h_{\mathrm{wm}}=0.1\delta$ ($h^+_{\mathrm{wm}}=200$) (§3.3, Table 4) | 60 elements | $l=4$: 31,217 elements | mean velocity agrees with DNS above $h_{\mathrm{wm}}$ at $l=3$; stresses acceptable at $l=4$, the streamwise one not exactly converged, which the authors attribute to WMLES, not to adaptation |
| Transonic NACA 64A-110, $M=0.72$, $Re_c=930{,}000$, zero incidence, wall-modelled (§4, Tables 5–6) | 6 elements per chord, maximum $y^+\approx1100$ | $l=3$: 222,426 elements, 214,902 saved by spanwise mortar zones | $C_p$, $\tau_w$ and $\delta_{99}$ converge to an in-house wall-resolved LES within four meshes; $C_p$ fastest, $\delta_{99}$ slowest |

- *Wall-parallel spacing.* In the wall-resolved channel the suggested $x$
  and $z$ spacings are larger in the viscous sublayer than in the buffer
  layer. The authors call this the correct behaviour, because wall-parallel
  length scales grow in the viscous sublayer (§3.1, Fig. 1). The
  converged grids also bear on the
  [grid-point requirements of LES](/results/les-grid-point-requirements.md).
- *Airfoil.* The indicator refines most in the wall-normal direction, then
  spanwise, then wall-tangential. It suggests a very coarse spanwise
  spacing at the laminar leading edge and refines the turbulent wake (§4,
  Fig. 12).

**Place among the criteria.** Blind et al. (2023, §1) reject three earlier
measures of LES resolution:

- the ratio of subgrid to viscous dissipation, meaningful only in the
  buffer layer;
- the ratio of modelled to resolved kinetic energy, which correlates poorly
  with known length scales of wall-bounded flows;
- local spectra, valid for isotropic flows only.

They call the Toosi–Larsson residual "the most well-grounded approach to
date". Mozaffari et al. (2022, §3.3) describe the same authors' criterion as
"almost identical" to their own Hessian criterion. The two approaches
differ in flow, discretization and in whether adaptation runs during the
computation. The modelling residual is also a different object
from the a posteriori error estimator of Basile et al., which measures the
modal energy at the discretization cutoff and inter-element jumps.

## Truncation-error p-adaptation (Ferrer et al. 2023)

[Ferrer et al. (2023)](/sources/ferrer-2023.md) (§3.6) describe the
adaptation of [HORSES3D](/software/horses3d.md), a DGSEM code; the version
read is arXiv v1.

- *Operation.* Anisotropic p-adaptation: each element carries its own
  degree in each direction. Faces with different degrees on the two sides
  are coupled by mortars, "which does not retain entropy stability" (§3.6).
- *Criterion.* The truncation error, estimated by $\tau$-estimation, is the
  preferred sensor. It "targets the source of the discretisation error", is
  cheap compared with adjoint techniques, and comes as a by-product of a
  multigrid cycle. Citing the group's earlier work, the authors state
  that the truncation error controls all functional errors (§3.6.1–3.6.2).
- *Steady procedure.* Converge at a moderate degree until the residual is
  below the truncation-error threshold. Then estimate the truncation error
  for all lower degrees and choose, in one step, the lowest degree per
  element and direction that meets the threshold, extrapolating if none of
  the degrees up to the current one does (§3.6.2).
- *Unsteady procedure.* Re-estimate and adapt at prescribed intervals
  (§3.6.2).
- *Threshold.* It "does not have any direct physical or engineering
  meaning", a past drawback that the group now bypasses by linking it to a
  flow functional (§3.6.2).
- *Feature-based variant.* For multiphase flow, elements containing the
  Cahn–Hilliard interface (phase field between 0.1 and 0.9) are refined
  (§3.6.2, Fig. 2).

The illustrations are a sphere at $Re=200$ (Fig. 1) and multiphase flows;
a wind-turbine immersed-boundary case uses degree 3 near the rotor and
wake and 2 elsewhere (§4.7, Fig. 14). The paper shows no adapted turbulent
case.

## Three indicators for adaptive implicit LES with flux reconstruction (Ims & Wang 2023)

[Ims & Wang (2023)](/sources/ims-2023.md) compare three per-cell
indicators for h-adaptation at fixed polynomial degree $N$ of
[implicit LES](/definitions/implicit-les.md) with the
[flux reconstruction](/methods/flux-reconstruction.md) (FR/CPR) method in
[hpMusic](/software/hpmusic.md). They argue (§1) that output-adjoint
adaptation, "the most efficient" for steady RANS, is "simply impractical"
for LES: the unsteady adjoint runs backward in time, the mesh would have
to adapt at different times, and chaos pervades even the mean quantities.
They call the new approaches, among them Fidkowski (2022, below), which
they describe as machine-learning models trained "to approximate the
adjoint from a time-averaged primal", "encouraging" but not yet
"time-tested" (§1). They also
prefer h to p alone, because p-enrichment can fail on shocks, shear layers
and contacts, and name hp "the ultimate approach" (§1).

**The indicators (§3).** With $Q_N$ the degree-$N$ solution,
$\mathrm{Res}_N$ the FR/CPR spatial residual operator and $\Pi_N$ the
projection onto degree $N$ (page-local):

- *unStdE, the unsteady residual at one degree higher* (an unsteady
  extension of the steady criterion of Gao & Wang, as cited). Since the
  unsteady residual vanishes at degree $N$ by construction, its value at
  $N+1$ is
  $$\epsilon=\mathrm{Res}_{N+1}\big(\Pi_{N+1}[Q_N]\big)-\Pi_{N+1}\big[\mathrm{Res}_N(Q_N)\big]$$
  (Eqs. 8–12; page-local $\epsilon$, not the dissipation rate
  $\varepsilon$), whose absolute value is cell-averaged for density, momentum
  and energy, each normalized by its domain mean, averaged over the three
  and over time (Eqs. 13–14).
- *smthE, the Persson–Peraire smoothness indicator*, called a "spectral
  decay indicator" by Naddei et al. as cited: the squared difference
  between $Q_N$ and its projection to degree $N-1$, relative to
  $\lVert Q_N\rVert^2$, per variable, averaged over the three variables,
  the cell and time (Eqs. 15–17). It is a
  [shock sensor](/definitions/shock-sensor.md) repurposed. For
  comparison, the small-scale energy of Basile et al. (2023, above,
  Eqs. 8–10) is the energy of the highest modal level of the momentum per
  element volume, with no division by the solution norm.
- *T.L.errE, a variant of the Toosi–Larsson small-scale energy*: the
  directional high-pass filter $-\tfrac{h_\xi^2}{4}\partial^2\boldsymbol u/\partial\xi^2$
  applied along each reference coordinate $\xi$ of the curved cell, with
  $h_\xi=1/(N+1)$ so that the physical width adapts to the local cell size
  and curvature; its squared magnitude is cell- and time-averaged per
  direction and the indicator is the square root of the maximum over
  directions (Eqs. 18–22). Transforming the physical-space directional
  derivative instead (Eqs. 19–20) would add a metric term, which the
  authors drop on the argument that the polynomials live in computational
  space and the term is nearly constant unless the mesh is unevenly
  curved (§3.3). This quantity is the small-scale velocity energy of
  Toosi & Larsson, not the modelling residual of Blind et al. (above).

**Procedure (§4).** Indicators are computed during the run; the top 20%
of cells are marked, plus cells forced by a one-level size constraint and
by a clumping rule (a cell at least 50% flanked by marked neighbours),
iterated until the marking stops changing. Marked cells are split
isotropically into equal children that follow the parent's high-order
curvature; the flow is interpolated and the run restarted. Hanging nodes
use mortar faces; the face geometry must be taken from the coarse side
when its polynomial is linear and should be taken from the fine side
otherwise, or the under-integrated coarse side makes the computation
unstable (an implementation observation, no data shown).

**Results (§5, Figs. 5–34).** On the
[T106c and T106a turbine cascades](/benchmarks/turbine-cascade.md)
($N=2$ at $M_{is}=0.65$, $Re_{is}=80\,000$ against an hpMusic DNS; $N=1$
at $M_{is}=0.4$, $Re_{is}=60\,000$ against an $N=4$ run on a uniformly
refined mesh), with the same budget for every indicator, the evidence is
visual (entropy snapshots, marked-cell maps, the $uv$ Reynolds stress and
power spectral densities of the turbulent kinetic energy at a wake point):

- all three improve the solution and none refines much at the leading
  edge, "possibly" because the laminar flow is already resolved there, in
  the authors' reading;
- smthE favours small boundary-layer cells on both surfaces, T.L.errE
  large wake cells (refining once even at the domain exit), unStdE lies in
  between;
- smthE converges slowest; unStdE and T.L.errE converge "nearly in
  lockstep", T.L.errE slightly ahead;
- on T106a a random marking with the same budget improves the solution
  "at a pace almost equal to" smthE, and moves the low-frequency spectral
  peaks toward the reference faster than the two better indicators, which
  the authors read as those indicators de-emphasizing laminar convergence;
  the hanging-node boundaries at random locations do not disturb the flow.

The authors attribute the ranking to vortex sensitivity, recommend
T.L.errE when vortex activity matters most and unStdE as easier to
implement (it needs only a projection and the residual at $N+1$, "freely
available" in an hp-aware solver) and possibly "the more truthful
estimate of the physics errors"; T.L.errE is hard to make efficient
across MPI, threads and SIMD (§5.3, §6). No error norms, cell counts or
costs are reported.

## Adaptation in scale-resolving simulation

**Mesh changes perturb resolved turbulence.** In a DES of freely decaying
turbulence crossing a plane where the cell size doubles, the resolved
kinetic energy drops abruptly and the modelled energy decays more slowly on
the coarse side, but "the loss of resolved turbulence is never equal to the
gain in modeled turbulence", so "a single change in mesh size causes a
lasting perturbation" (Mozaffari et al. 2022, §1, Fig. 1, from the first
author's thesis). Martin-Alvarez et al. (2022, §1, §2.1) state the
analogous effect for implicit dissipation on octree meshes: multi-level
refinement introduces numerical viscosity and resistivity at one scale per
level, energy is "dissipated significantly more than expected for the
$\Delta x_{\max}$ employed", and small-scale structure is lost when gas
crosses into coarser levels. The two sources reach the same design
conclusion from different flows: avoid changing the cell size along the
path of the turbulence. [van Noordt et al. (2022)](/sources/vannoordt-2022.md)
see a third effect in immersed-boundary WMLES on block-structured octree
grids: coarse–fine interfaces (from $\Delta x$ to $2\Delta x$) partly
reflect the acoustic radiation of the transition region back toward the
boundary layer of a Mach 6 shock/boundary-layer interaction, visible in
the wall-normal Reynolds stress and negligible on the means (§3.3.2, Fig.
24; see [immersed boundary methods](/methods/immersed-boundary-method.md)).

**Time-averaged criteria and static meshes.** Instantaneous refinement
follows every eddy and keeps changing the mesh. Mozaffari et al. (2022,
§3) compute the criterion from time averages so that the mesh converges
to a static one for statistically steady flows. Two options: the
criterion of the averaged flow (CA) or the average of the instantaneous
criterion (AC). AC is recommended: CA meshes are irregular, because the
linear interpolation of the averaged solution onto refined cells has
discontinuous derivatives that inflate the Hessian, and they never become
steady (§4.2, Fig. 9); AC satisfies the instantaneous requests "in an
average way" (§3.3). Basile et al. (2023, §3.3, §4.1) likewise adapt
statically from indicators averaged over $30$ convective times
$D/U_j$, against $150$ for the statistics, and state that the estimator
needs no long accumulation to be representative.

**Results on the backward-facing step** (Mozaffari et al. 2022, §4, Table
2; IDDES, Vogel–Eaton configuration at $Re_H=28\,000$, measured
reattachment length $6.66H$):

| Run | Cells ($10^6$) | Reattachment ($H$) | Error |
|---|---|---|---|
| Fixed fine mesh | 9.3 | 7.3 | 9.6% |
| Instantaneous criterion, $T_r=0.01$ | 6.6 (peaks near 20) | 8.35 | 25% |
| CA, $T_r=0.0025$ | 2.4 | 7.14 | 7.2% |
| AC, $T_r=0.0025$ | 1.3 | 7.9 | 18.7% |
| AC, $T_r=0.002$ | 2.5 | 7.0 | 5.1% |
| AC, $T_r=0.0015$ | 9.9 | 6.9 | 3.6% |
| AC, sliding window of 1250 steps | 2.5 | 7.7 | 15.6% |
| AC with a box on recirculation and shear layer | 2.0 | 6.5 | $-2.5\%$ |
| AC with a box on the shear layer | 1.8 | 6.3 | $-5.4\%$ |

The two box runs give similar results, which the authors read as showing
that the faster generation of resolved content, not small recirculation
eddies, drives the gain (§4.5). The Hessian criterion never refines the
low-velocity forward recirculation zone (§4.3).

**Averaging window.** A sliding window converges the mesh faster; a window
of one refinement interval (less than one Kelvin–Helmholtz period) made
the cell count grow until the run was stopped (§4.4). To average a
phenomenon out, the window "should span at least 4 to 10 of its
characteristic periods" (§6), chosen from the flow's spectrum (Strouhal
numbers on step height from 0.86 for the shear-layer instability down to
0.008 for flapping, §4.4).

**Starting mesh.** Both Mozaffari et al. (2022, §4.5, §6) and Basile et al.
(2023, §3.3) start the scale-resolving adaptation from a RANS-adapted
mesh; Basile et al. state that a very coarse start would prevent turbulent
structures from developing, could destabilize the run and would need many
unsteady steps.

**Recommendations of Mozaffari et al. (2022, §6).** Average of the
instantaneous criterion; a RANS precursor; a short sliding window switched
to whole-run averaging once the mesh converges; a minimum cell size of a
quarter of the Taylor microscale $\lambda$; the same threshold as for RANS
($L/5$ to $L/20$, $L$ the body length). On the DTMB 5512 hull at $10^\circ$
drift (DDES-SST, $Re_L=4.65\times10^6$) the adapted 154 M-cell mesh
reproduces the vortex-core results of a 163 M-cell hand-made mesh up to
$x/L=0.4$ and agrees better downstream, at about 160 000 CPU hours against
about 250 000 (different processor counts; "the adaptation probably saves
some time, but not a lot") (§5.1, Figs. 18–19).

**hp-adapted jet (Basile et al. 2023, §4).** For the isothermal PPRIME jet
at $M_j=0.9$, $Re_D\simeq10^6$, two adaptation steps from the RANS-adapted
mesh give 11.6, 18.9 and 31.7 M degrees of freedom. The estimator flags the
lip line and the end of the potential core; the degrees of freedom move to
the turbulent shear layers, whereas RANS adaptation had concentrated them
in the high mean-gradient zone of the potential core (§4.2.1). Refinement
lengthens the potential core: the 18.9 M mesh is closest to experiment
and the 31.7 M mesh overpredicts it but matches the finest ZDES and ILES
references, which used 48–154 M and 23 M cells; a DG LES of 78 M degrees
of freedom is also listed (§4.2.3, Table 1). The far-field overall sound
level of the finest mesh is within about 1–2 dB of experiment (§4.4). The
modelled viscosity falls with the square of the element size, so
adaptation lowers $\mu_t$ in the shear layer step by step (§4.2.2).

**Refinement strategy as a dissipation control (Martin-Alvarez et al.
2022).** In ideal-MHD galaxy simulations ($\eta_m=0$, so all dissipation is
numerical), quasi-Lagrangian refinement (refine when a cell's mass
exceeds that of eight dark-matter particles) resolves the cold dense phase
finely and the warm and hot phases coarsely. The authors' quasi-Eulerian
refinement forces the finest level (cell size $h_{\min}$) wherever the gas
density exceeds $10^{-24}\,\mathrm{g\,cm^{-3}}$, giving an almost uniform
grid over the galaxy (§2.1, Fig. 2). At fixed $h_{\min}$ it yields
more small-scale turbulence, about one decade more magnetic energy at
$20$ pc, and higher dynamo growth rates (§3.2, Figs. 6–7). In the
accretion phase the quasi-Eulerian runs "follow well" the fiducial
scaling $\Gamma_E\propto Re^{1/2}\propto h_{\min}^{-1/2}$ drawn in
Fig. 7 ($\Gamma_E$ the growth rate of the specific magnetic energy and
$h_{\min}$ the finest cell size, as on the
[small-scale dynamo](/results/small-scale-dynamo.md) page), while the quasi-Lagrangian runs "appear to follow" one
"resembling" the $Re^{0.3}$ of Federrath et al. (2011) below 80 pc; the
authors read the comparison as markedly favouring the new refinement
(§3.2). The extra cost is "minor" below 80 pc and about a factor
two at 20 pc (§2.2). See [small-scale dynamo](/results/small-scale-dynamo.md).

## Adaptation for steady RANS (Alauzet et al. 2022)

**Loop (§3, Algorithms 1–2).** At fixed complexity the solver, adjoint,
metric, remeshing and interpolation steps are repeated (typically four
times) until mass flow, pressure ratio and temperature ratio change by
less than 1% over three consecutive meshes; then the complexity is
doubled and the loop restarts from the previous mesh and solution. To
trace a compressor characteristic each outlet pressure restarts from the
previous one at the same complexity, because coarse adapted meshes diverge
near stall.

**Periodicity and rotation (§4.3, §7).** Periodic boundaries are handled by
ghost elements in the solver and adjoint, and by a four-step remeshing
(remesh with frozen periodic surfaces, migrate five element layers across,
remesh with the original periodic surface as an embedded constraint,
migrate back), with the metric rotated as $R\mathcal MR^{T}$. Without
adapting the periodic surfaces the interior refinement leaves them too
coarse and the solver breaks down (§7.3). The overhead is a factor two
over non-periodic adaptation (§7.4, Table 1).

**Results.** On the LS89 turbine vane and NASA Rotor 37 (16 plus 7
operating points, adapted meshes up to about 11 M vertices and 61 M
tetrahedra), the converged functionals do not depend on the initial mesh
or on the estimate, with one exception at the lowest LS89 pressure ratio
(§8.1.3). Goal-oriented adaptation converges earlier: the Rotor 37 choke
total-pressure ratio is within 0.1% of the reference after 0.5 M vertices,
against 0.2–0.5% for feature-based adaptation (§8.2.4, Fig. 32). Purely
tetrahedral adapted meshes reach $y^+\approx1$ ahead of the shock and
about 2 in the separated boundary layer, unchanged from the coarsest to
the finest adapted mesh (§8.2.5, Fig. 40), and the authors conclude that
prismatic or hexahedral boundary-layer meshes are not necessary (§9). The
mean anisotropic ratio on the 10 M-vertex mesh is 112, and the anisotropic
quotient of 9892 implies almost four orders of magnitude fewer elements
than an isotropic adapted mesh (§8.2.6, Table 3). Against structured
[elsA](/software/elsa.md) RANS on 3–32 M cells, the adapted solutions give
higher pressure ratio and efficiency, better endwall profiles and better
preserved tip vortices; the authors attribute the differences to the
resolution of the non-adapted meshes, and the above-experiment
characteristic to the cold blade geometry (§8.2.4–8.2.5). Their
perspective is that, with discretization error removed, turbulence models
can be compared without mesh contamination (§9).

Mozaffari et al. (2022, §5.2) add the RANS limit of their method: for
steady flows instantaneous and average-based refinement are equivalent,
and for RANS solutions with some unsteadiness the averaged criterion gives
smoother meshes.

## Anisotropic adaptation for high-order DG RANS (Schotte et al. 2026)

[Schotte et al. (2026)](/sources/schotte-2026.md) carry the continuous-mesh
metric of Alauzet et al. to a modal DG discretization of steady RANS with
the negative [Spalart–Allmaras model](/methods/spalart-allmaras-model.md),
in the ONERA–DLR–Airbus solver CODA with the remesher Tucanos (§2). The
version read is the HAL deposit of the version of record.

**The difficulty (§1, §3).** The optimal $L^p$ metric above controls the
interpolation error exactly only for piecewise-linear approximations. For
polynomial degree $N\ge2$ the interpolation error is not quadratic and has
no direct link to a metric. The authors set aside the high-order
approaches that address this (log-simplex fitting, Coulaud et al.;
directional derivatives, Rangarajan et al.) as "too computationally
demanding for industrial applications" and follow Venditti & Darmofal: the
Hessian of the Mach number supplies the orientations and anisotropic
quotients of the metric, an isotropic DG error estimator supplies the
element size. They assume that the Hessian's anisotropy stays adequate at
$N=2$ and 3, "a sweet spot for modal DG applied to complex
configurations", and expect the assumption to weaken as the order rises
(§3).

**Element Hessian (§3.1, Eqs. 15–19).** Elements are linear, so a constant
Hessian per element suffices. Projecting the gradient of $\partial_iw$ (page-local: $w$
the scalar sensor) onto constants on element $K$ gives

$$H^*_K=\frac1{\lvert K\rvert}\int_{\partial K}\nabla w\,\boldsymbol n^{\mathsf T}\,d\Gamma,\qquad H_K=\tfrac12\big(H^*_K+H^{*\mathsf T}_K\big),$$

with the face gradient the average of the two lifted gradients (BR1 or
BR2) and the symmetrization needed because quadrature breaks the symmetry.
The sensor is the Mach number with BR1 gradients.

**Hessian scaling (§3.2, Eq. 21).** The element Hessian is divided by its
"global density" and multiplied by an isotropic estimator $e_K$,

$$H^{\mathrm{sc}}_K=e_K\,\frac{H_K}{\big[\sqrt{\det H_K}\,\lvert K\rvert\big]^{2/d}},$$

($d$ the space dimension), which removes the element-size content of the
Hessian and keeps its orientations and anisotropic quotients; $H^{\mathrm{sc}}_K$
then enters the $L^4$ optimal metric. Two estimators, both on momentum
(Eqs. 22–25):

- *SSED*, the small-scale energy density of Kuru et al. with the volume
  normalization of Naddei et al., $e_K=\lVert(\rho\boldsymbol u)_N-(\rho\boldsymbol u)_{N-1}\rVert_{L^2(K)}/\lvert K\rvert^{1/2}$,
  the energy of the highest modes; this is the square root of the
  small-scale energy density of Basile et al. (2023) above *(compiler
  check, not in the sources)*, which the same group used for isotropic
  h- and p-adaptation;
- *SSL*, the small-scale lifted estimator of Naddei & de la Llave Plata,
  designed to capture vortices in LES, which adds to the SSED norm the
  lifting operator of momentum projected on the element's characteristic
  length vectors.

**Numerics (§2.2, §4.1).** Roe flux with entropy fixes, BR2 viscous terms
(penalty 3 on triangles, 4 on tetrahedra), Laplacian
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
with the Persson–Peraire sensor and a positivity limiter in transonic
cases, implicit backward Euler with restarted GMRES. Each new mesh is
started by $p$-staging ($N=0$, then higher), and solutions are transferred
between meshes with their modes up to $N=1$. Metric gradation and a
curvature metric bound the mesh (§2.5).

**Hessian check (§3.3, Figs. 3–7).** On an analytic 2-D X-shaped function
($N=1$, complexity 5000) and a 3-D smooth-shock function (complexity
$10^5$), the BR1 Hessian adapts meshes whose interpolation error is close
to that of the exact Hessian and below those of Tucanos' least-squares and
$L^2$-projection Hessians, which use a nodally interpolated solution and
miss the small 3-D variations.

**RANS results.**

| Case | Conditions | Outcome |
|---|---|---|
| HLPW4 three-element airfoil (§4.2, Table 2) | $M_\infty=0.2$, $\alpha=16^\circ$, $Re_c=5\times10^6$ | at about $10^5$ DOF: $N=1$ $C_L=3.796$, $C_D=0.06172$; $N=2$ unscaled 3.798, 0.06104; SSED 3.802, 0.06106; SSL 3.802, 0.06092. Scaling beats the unscaled Hessian at $N=2$, SSL slightly ahead; at $N=3$ the unscaled Hessian leaves very large isotropic elements on the lower wing and "needs a correction". Every strategy is more efficient than FUN3D uniform refinement; goal-oriented adaptation on lift (GGNS) is more efficient at the coarse complexity, $N=2$ SSL slightly more accurate in drag at the finer ones |
| RAE2822, case 9 (§4.3, Table 4) | $M_\infty=0.734$, $\alpha=2.79^\circ$, $Re_c=6.5\times10^6$ | $N=1$: 67,395 DOF, $C_L=0.8235$, $C_D=0.01893$; $N=2$ unscaled 63,378, 0.8238, 0.01894; SSED 69,954, 0.8222, 0.01884; SSL 37,560, 0.8229, 0.01885; finite volume on hexahedra 230,084, 0.816, 0.0189. The scaled strategies are less accurate on very coarse meshes but converge earlier, SSL with the fewest DOF |
| [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md), HLPW5 wing–body (§4.4, Figs. 19–22) | $M_\infty=0.2$, $\alpha=11^\circ$, $Re=5.6\times10^6$ on the root chord | SSL scaling captures the tip vortex better than the unscaled Hessian at $N=2$ ("+2 drag counts and +0.1 lift counts"); $N=2$ needs "≈ 8e6 less DOFS" than $N=1$ for similar forces; all adapted DG strategies "clearly outperform" FUN3D, CHAMPS and CODA finite-volume results; $y^+$ near 1 reached at $N=1$, anisotropic ratios up to $10^5$ |
| ONERA M6 wing, NASA case 2308 (§4.5, Figs. 23–25) | $M_\infty=0.84$, $\alpha=3.06^\circ$, $Re=14.6\times10^6$ on the root chord; $N=1$ only | "overly dissipative at lower mesh complexities", then close to the adaptive node-based finite-volume results (Wolf with Feflo.a, same estimator) and to the NASA $C_p$ cuts |

Higher degrees are not run on the M6 wing because steady implicit
high-order computations with shocks do not converge systematically, and
non-converged solutions corrupt the estimators (§4.5). The authors
call the good $N=2$ result of the unscaled Hessian on the CRM
"surprising" (§4.4) and claim the first published high-order DG
metric-based adaptation of complex 3-D cases, "including a full high-lift
aircraft configuration" (§1); the configuration run is the wing–body.
Their perspective is $hp$-adaptation, keeping $N=1$ at shocks, and curved
boundary elements, without which $N=3$ meshes could not be coarsened to
equal DOF (§4.2, §5).

## Adaptation in the first High-Order CFD Workshop (Wang et al. 2013)

The summary of the first International Workshop on High-Order CFD Methods
(2012), [Wang et al. (2013)](/sources/wang-2013.md), compares methods by
error against cost (work units of a benchmark code), so that adaptive and
uniform refinement enter the same plots. Its findings on adaptation:

- **Survey (§2, Q3, Q6).** p-adaptation is preferred in smooth regions and
  h-adaptation at discontinuities; adjoint-based output adaptation is
  effective for lift and drag; robust anisotropic adaptation remains a
  challenge.
- **Singular and shocked airfoil cases (§5.2, Figs. 16–19).** On the
  inviscid subcritical [NACA 0012](/benchmarks/naca-0012-airfoil.md)
  uniform refinement does not reach high-order rates because of the
  trailing-edge singularity, and MIT's fixed-DOF output-based mesh
  optimization gives the highest rates, at least for drag. On the
  transonic case adaptive refinement generally beats uniform refinement;
  one group used hp-adaptation with polynomial degree 1 to 4.
- **RANS (§5.4, Fig. 23, Table V).** On the
  [RAE 2822](/benchmarks/rae-2822-airfoil.md) case 9 ($M=0.734$,
  $\alpha=2.79^\circ$, $Re=6.5\times10^6$), three DG groups with the
  Spalart–Allmaras, EARSM and Wilcox $k$-$\omega$ models show "a large
  spread among the groups and virtually no improvement from high order
  under uniform mesh refinement", attributed partly to inadequate wake
  alignment of the initial mesh and partly to the turbulence model;
  adaptive mesh optimization (MIT, at fixed DOF) is "markedly superior"
  (conditions in §4.8). Schotte et al. (2026, §4.3, Table 4) print the
  same case-9 conditions (row of the table above).
- **Conclusions and pacing items (§6).** Output-based or solution-based
  hp-adaptation is "very effective"; output-adjoint, entropy-based and
  residual-based indicators have proved effective, as cited; high-order
  viscous meshing with hp-adaptation is one of the four pacing items, with
  curved-mesh generation, scalable low-memory time integrators (the
  memory of line-implicit solvers scales as the sixth power of the
  polynomial degree) and parameter-free shock capturing. High-order RANS
  is less robust than low-order RANS in reaching a steady state, which the
  authors "believe" is related to non-smooth turbulence models: "smooth
  turbulence models are needed".

## Discretization-error estimation by error transport equations (Wang & Roy 2023)

[Wang & Roy (2023)](/sources/wang-2023.md) (journal pre-proof) estimate
the discretization error of a modal DG solution of the steady 2-D Euler
equations, the quantity that error-based adaptation needs; the paper
adapts no mesh and has no turbulence content. Page-local: $\boldsymbol q_h$
the DG solution, $I^h\boldsymbol q$ the projection of the exact solution,
$\boldsymbol\epsilon_h=\boldsymbol q_h-I^h\boldsymbol q$ the
discretization error, $\boldsymbol\tau_h$ the truncation error (the
residual of the discrete operator at $I^h\boldsymbol q$, Eq. 11), and
$p$, $q$, $r$ the orders of accuracy of the primal solution, of the error
solve and of the truncation-error estimate (the triplet of Yan &
Ollivier-Gooch as cited; the primal polynomial degree is $N=p-1$).

- *Equations (§3.1, Eqs. 12–14).* Subtracting the discrete equations
  at $I^h\boldsymbol q$ from those at $\boldsymbol q_h$ gives a nonlinear
  error transport equation for an estimate $\bar{\boldsymbol\epsilon}_h$
  driven by $-\boldsymbol\tau_h$; linearizing about $\boldsymbol q_h$
  gives the linearized one, which reuses the Jacobian of the implicit
  primal solver. The corrected solution is $\boldsymbol q_h-\bar{\boldsymbol\epsilon}_h$.
- *Expected order (Eqs. 15–16, derivation cited to Banks et al.).*
  $O(h^{\min(p+q,r)})$ for the nonlinear and $O(h^{\min(2p,p+q,r)})$ for
  the linearized equation, for smooth solutions and grid metrics; $q=p$
  throughout.
- *Truncation-error estimate.* $\boldsymbol\tau_h$ is estimated by
  substituting a higher-order reconstruction of $\boldsymbol q_h$ from
  neighbouring elements, with an "iterative correction" that re-estimates
  it (generalized from Tyson et al.'s relinearization); without that
  correction the estimate misses its expected order (§4.1.1, Fig. 2).
- *Smooth problems (§4.1).* On a sinusoidal manufactured solution and
  Ringleb's flow with curved walls, for primal orders 2–4, the
  estimates with estimated truncation error reach order $r$ after the
  correction; the estimate costs less than the primal solve once the
  number of DOF is large enough (Table 1; see
  [method of manufactured solutions](/methods/method-of-manufactured-solutions.md)).
- *Non-smooth problems (§4.2).* Across a supersonic expansion fan and on a
  Kármán–Trefftz airfoil with a trailing-edge singularity the primal order
  falls to 1, the truncation-error estimate falls below first order (fan)
  or to nearly zeroth order (airfoil), and the corrected error barely
  improves on the base error; the linearized equation fails to be
  higher order on the fan even with the exact truncation error. The lift
  coefficient of the corrected airfoil solution is nevertheless second
  order.
- *Conclusion (§5).* Truncation-error estimation, not the error
  equation, limits non-smooth problems; the remedies proposed are grids
  aligned with discontinuities and embedded-grid truncation-error
  estimation ($\tau$-estimation), the sensor of
  [Ferrer et al. (2023)](/sources/ferrer-2023.md) above.

## Output-based adaptation of chaotic unsteady flows (Fidkowski 2022)

[Fidkowski (2022)](/sources/fidkowski-2022.md) adapts high-order DG meshes
(Roe flux, BR2 viscous flux, third-order modified extended BDF in time,
$N=2$ by default) for time-averaged outputs of chaotic flows without an
unsteady adjoint, which is unstable in all three test cases (Figs. 4, 11,
17). The output error is estimated by the adjoint-weighted residual
on the space enriched to degree $N+1$. Writing the adjoint and the
residual as time mean plus fluctuation, the author assumes that the
correlation of the fluctuations is negligible for chaotic statistically
steady flows, so that only the time-mean adjoint is needed (§4, Eqs.
17–18). That adjoint is replaced by the steady adjoint of a
[field-inversion-corrected](/methods/field-inversion-machine-learning.md)
Spalart–Allmaras RANS fitted to the averaged unsteady state, restricted
to the Navier–Stokes components; this works because the augmented system
keeps the original residuals additively (§2.2, §4, Eqs. 7, 23). Two
estimates follow:

- **E1** weights the time-averaged fine-space residual of the unsteady
  run, accumulated during the run, by the surrogate adjoint;
- **E2** is the steady adjoint-weighted residual of the corrected RANS
  system alone, which allows several cheap steady adaptation passes per
  unsteady run but measures the error of the surrogate, not of the
  unsteady mesh (§4, Eq. 23; §5.2).

Elemental indicators $|\delta\Psi_e^\top\delta R_e|$ (page-local: fine
adjoint minus its coarse projection, times the fine residual of element
$e$) drive either fixed-fraction $p$-adaptation (top 20% of elements) or
MOESS, a metric-based anisotropic optimization that minimizes the output
error at fixed degrees of freedom with error and cost models sampled
locally (§5.1–5.2, Eq. 24). Their sum is called conservative: it avoids
unpredictable cancellation between elements in chaotic simulations but
is not a bound (§5.1). Only two to four unsteady runs per adapted mesh are
needed, with no stored states or checkpointing (§5.2–5.3).

Results on 2-D airfoils at $M=0.2$ (§6, Tables 1–3):

- NACA 0012 at $7^\circ$, $Re=10^4$ (unsteady laminar separation;
  Navier–Stokes with no model): field-inversion MOESS with E1 gives a mean
  lift of 0.7355 at 9000 degrees of freedom, estimate 0.0057, actual error
  0.0045; with E2, 0.7175, estimate 0.0087, actual 0.0225; E1 estimates
  are "reasonably accurate (within a factor of 2)" (Table 1, Fig. 7);
- NACA 0012 at $Re=2\times10^4$ (transitional, with a
  [laminar separation bubble](/definitions/laminar-separation-bubble.md)):
  E1 with the adjoint-weighted inversion objective is best, 0.6569 at
  20,250 degrees of freedom with estimate 0.0024 and actual error 0.0011
  (Table 2); residual-based $p$-refinement oscillates away from the
  converged value in its last iterations;
- a high-lift airfoil at $17^\circ$, $Re=10^6$, with "a variation of
  the [detached-eddy simulation](/methods/detached-eddy-simulation.md)
  (DES) model" in which the mesh-based wall-distance adjustment is replaced
  by the fixed attenuation $d=d_{\max}\tanh(d/d_{\max})$, $d_{\max}$ 2% of
  the chord, so that the model does not change as the mesh adapts (§2.1,
  Eq. 3): the estimates over-predict the error by about a factor of two on the
  finest meshes, which the author attributes to the lack of cancellation
  in the conservative sum (Table 3, Fig. 18); from a poor isotropic
  13,500-degree-of-freedom start the method recovers in about three
  iterations (Fig. 19).

In every case uncorrected RANS-based MOESS converges to a wrong lift with
small error estimates (modelling error; see
[model-form uncertainty](/definitions/model-form-uncertainty.md)), and
residual-based adaptation, "distracted" by wake and far-field residuals,
performs poorly (§7). Output-adapted meshes for the unsteady flows carry
thicker, more isotropic boundary-layer refinement and refinement where the
upper-surface laminar flow breaks into vortices, whereas RANS-adapted
meshes are highly anisotropic along the surface (Fig. 9). The method is
stated to extend directly to 3-D, not attempted for cost (§7).

## Output-based adaptation in industrial practice (Mani & Dorgan 2023)

[Mani & Dorgan (2023)](/sources/mani-2023.md), an industrial review
(MIT and Boeing) with no new data, describe the adaptation loop used with
Boeing's finite-volume and finite-element RANS solvers, which share the
EPIC (Edge Primitive Insertion and Collapse) mesh-mechanics tool (§1,
§4.3, Fig. 9): initial grid, flow solution, optional adjoint, error
estimation, an anisotropic metric field, and, while the errors exceed the
user's limits, mesh mechanics that make the mesh conform to the metric,
with the previous solution interpolated as the initial guess, until an
accuracy or run-time criterion stops the loop. Surface and volume meshes
are both adapted, and the adapted surface mesh must be projected onto the
CAD geometry, not onto the initial surface mesh (§4.2–4.3). Cell-centred
finite volume needs mixed-element meshes with prismatic or hexahedral
layers, which are harder to adapt than the pure tetrahedra of
node-centred finite volume or finite elements (§4.3).

- **Output-based against feature-based.** A Hessian (feature-based)
  criterion refines features that do not affect the output; an
  adjoint (output-based) criterion resolves only those that do. Their
  reproduced example (Venditti & Darmofal, as cited) is a transonic RAE
  airfoil at $M=0.725$, $\alpha=2.466^\circ$: 22,150 nodes when adapted for
  lift, 18,698 for drag, 37,681 with a pure Hessian criterion (Fig. 7).
- **Methods converge to one answer by different paths.** Citing Michal
  et al. (2021): four flow solvers, four mesh-mechanics methods and four
  error estimates on the two-dimensional airfoil section of
  the high-lift CRM (a cut of the
  [three-dimensional configuration](/benchmarks/nasa-crm-high-lift.md)) give nearly
  identical lift once adapted to sufficient mesh convergence, with
  different convergence trajectories, output-error methods reaching a
  prescribed error on coarser meshes (Fig. 8, $\alpha=8^\circ$).
- **Higher order.** Adaptive continuous-Galerkin variational multiscale
  with discontinuous subscales at third and fourth order is cited as
  needing an order of magnitude less time than second-order methods for
  the same lift error, below $10^{-4}$ (Ursachi et al., Fig. 4); curved
  meshes are required (§4.4).
- **Unsteady and chaotic flows.** Unsteady output-based adaptation must
  store the forward states for the backward adjoint sweep: 50 million
  points with five variables are 250 million values, 2 GB per time step
  in double precision (§4.3); temporal windows that reuse a mesh over many
  steps and checkpointing are the cited answers. For chaotic turbulent
  flows the adjoint sensitivities "blow up as the backward sweep
  approaches the initial conditions", and general techniques are needed
  before unsteady output-based adaptation is useful (§4.3). Fidkowski
  (2022, above) meets the same instability in all three of its cases and
  sidesteps it with a steady surrogate adjoint.
- **Certification.** Robust, efficient adaptation is one of the
  requirements the authors list for certification by analysis (§5).

## Qualifications

- **Ims & Wang (2023)** rank their indicators by visual comparison of
  fields and spectra on two cascades at one marking fraction, with no
  error norm, degree-of-freedom count or cost; the claim that unStdE is
  the more truthful estimate is argued from its definition. The round
  counting differs between the text and the captions of §5.1 and §5.2
  (two rounds plus a reference marking in the text, rounds 1–3 in the Fig.
  9 caption; the Fig. 21 caption says "second" where the text says
  third). After Eq. 12 the text refers to the error generation rate "from
  equation (12)", which is defined in Eq. 11; in Eq. 22 the pointwise
  product is equated with $A_\xi^2$, which Eq. 21c defines as an average.

- **Scope of each criterion.** Mozaffari et al. test their Hessian
  criterion for hybrid RANS/LES only indirectly (threshold convergence and
  the refinement-box test), and it misses low-velocity recirculation;
  Alauzet et al.'s goal-oriented estimate omits the turbulence equation;
  Basile et al.'s $5/3$ threshold identifies a modal degree with a Fourier
  wavenumber, which the paper presents as a "similarity" (§3.2).
- **Fidkowski (2022)** calls the $Re=10^4$ airfoil case "low-Reynolds
  number large-eddy simulation" (§7) while §6.1 solves the compressible
  Navier–Stokes equations with no subgrid model, in 2-D; the negligible
  correlation of adjoint and residual fluctuations (§4) is assumed, not
  checked against a regularized unsteady adjoint; averaging lengths and
  time steps are fixed a priori and not printed.
- **Grid dependence is kept, not removed.** Mozaffari et al. (2022, §1,
  §3) average the criterion because the resolved/modelled split of hybrid
  RANS/LES depends on the cell size; the converged static mesh still sets
  that split.
- **Printed slips.** Basile et al. (2023, Eq. 18) print the new degree as
  $\max(N+1,N_{\max})$, which with their marking condition $N+1\le N_{\max}$
  would always give $N_{\max}$, while the text enriches by one degree per
  step; $\min$ is consistent with the text *(compiler check, not in the
  sources)*. Alauzet et al. (2022, §8.2.6) print the anisotropic ratio as
  $\sqrt{\min_i\lambda_i/\max_i\lambda_i}=\max_ih_i/\min_ih_i$; with
  $h_i=\lambda_i^{-1/2}$ the square-root form is inverted and would not
  exceed one, against the reported mean of 112 *(compiler check, not in
  the sources)*.
- **Minimum cell size.** Mozaffari et al. (2022, §5.2) set the 1 mm
  minimum cell of the delta-wing DDES "to correspond to" a Taylor
  microscale of 2.86 mm, i.e. about $\lambda/2.9$ *(compiler check, not in
  the sources)*, while their §6 recommends $\lambda/4$; the paper does not
  comment on the difference.
- **"A priori" in the numerical-analysis sense.** Alauzet et al. call
  their goal-oriented bound an a priori estimate and Basile et al. their
  indicators an a posteriori estimator; neither use is the closure test of
  [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).
- **Claims and slips in Blind et al. (2023).**
  - *Test-level eddy viscosity.* §2.3 states that it is "a factor of
    $[(P+1)/(M+1)]^{2/3}\approx1.59$ larger" (the paper's $P$, $M$ are $N$,
    $N_f$ here). With $N=5$ and $N_f=3$, $1.5^{2/3}\approx1.31$ *(compiler
    check, not in the sources)*.
  - *Table 4 caption.* It names the wall-modelled "$Re_\tau=550$" channel,
    while §3.3 and the table's spacings are for $Re_\tau=2000$. The
    $Re_\tau$ computed on the last WMLES mesh is printed as 1555.60, which
    the text does not discuss.
  - *Polynomial degree of the airfoil.* Table 6 gives 512 DOF per element
    for the airfoil, i.e. $(N+1)^3$ with $N=7$, while §2.3 states $N=5$
    "throughout this work" *(compiler check, not in the sources)*.
  - *Savings.* The "up to 50%" savings of the abstract are measured against
    structured meshes with the same finest spacing, not against independent
    hand-made grids. For the channel the authors place the saving in
    processor count, because the time step is unchanged (§3.2). For the
    airfoil they say it translates "directly" into compute time (§4).
  - *Heuristic settings.* The Vreman constant 0.11 for WMLES rests on
    "previous experience" (§3.3).
- **Scale-resolving use of $\tau$-estimation.** Ferrer et al. (2023)
  describe truncation-error p-adaptation as a code capability and
  illustrate it on laminar and multiphase cases; its behaviour in
  turbulent flow is not shown there.
- **Not every "adaptation" changes the mesh.** The modelling-height
  adaptation of the [immersed boundary method](/methods/immersed-boundary-method.md)
  of [Constant et al. (2024)](/sources/constant-2024.md) (§4.2) turns some
  target (wall-modelled) points of a fixed octree Cartesian mesh into
  computed points where the stored $y^+$ one layer below already exceeds
  the target value; the mesh
  and the wall distance are not recomputed, and the run restarts from the
  converged solution. Their octree meshes are generated once from the
  surface mesh with a prescribed minimum near-wall spacing (§3.1). It is a
  static, single-pass change of which cells are modelled, recorded here
  for contrast only.
- **Operator adaptation on a fixed mesh, for contrast.** The
  [NASA Rotor 37](/benchmarks/nasa-rotor-37.md) blade that Alauzet et al.
  (2022) treat by RANS mesh adaptation is computed by
  [Kurz et al. (2025)](/sources/kurz-2025.md) (§6) as a mid-span linear
  cascade with wall-resolved LES on a fixed hexahedral mesh
  ($1.2\times10^6$ elements, $N=5$, $2.6\times10^8$ degrees of freedom) in
  [GALÆXI](/software/galaexi.md). What adapts there is the element-wise
  blending factor of the
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md),
  between 0.1 and 0.7 near the leading-edge shock only (Fig. 13), not the
  mesh.
- **Filter adaptation on a fixed mesh, for contrast.**
  [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) (arXiv v1, §II.B)
  set the cut-off of an element-local
  [explicit modal filter](/methods/explicit-modal-filtering.md) from the
  second invariants of the strain- and rotation-rate tensors, taken from
  the machine-learning mesh adaptation of Tlales et al. as they cite it,
  and normalize them by averages over under-resolved elements instead of
  thresholds, which they state, citing Pang et al., are problem-dependent.
  The mesh does not change.
- **Claims and slips in Schotte et al. (2026).**
  - *Eq. 20.* The element Hessian is written as $d_K^{2/d}$ times the
    orientation–quotient factor, with $d_K=\sqrt{\det H_K}\,\lvert K\rvert$.
    With the pointwise density $\sqrt{\det H_K}$ of their Eq. 14 that
    product is $H_K$; with $d_K$ as defined it is $\lvert K\rvert^{2/d}H_K$.
    Eq. 21 is then a definition, $e_K\lvert K\rvert^{-2/d}$ times the
    orientation–quotient factor *(compiler check, not in the sources)*;
    the paper does not comment on the factor $\lvert K\rvert^{-2/d}$.
  - *RAE2822 drag.* §4.3 states that the adapted strategies "always
    provide a higher $C_l$ and lower $C_d$" than the finite-volume
    results, while Table 4 prints $C_D=0.01893$ ($N=1$) and 0.01894
    ($N=2$ unscaled) against 0.0189 for finite volume, given to three
    digits.
  - *Residuals.* §2.4 gives convergence "up to $10^{-6}$ for all
    residuals", §4.1 gives $10^{-10}$ for the 2-D cases and $10^{-6}$ for
    the 3-D ones. The Fig. 10 caption names a complexity of 80,000 that
    Table 1 does not list.
  - *Reynolds number of the CRM.* Schotte et al. give $5.6\times10^6$ on
    the root chord for the HLPW5 wing–body; the benchmark page gives the
    values of other workshops and reference lengths (see
    [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)).
- **Wang & Roy (2023)** report the linearized error solve as taking
  "approximately 2/3" of the time of the nonlinear one; their Table 1
  ratios range from about 0.48 to 0.77 (e.g. 3.28/6.82 and 112.25/145.22)
  *(compiler check, not in the sources)*. With the exact truncation error
  the nonlinear error equation is satisfied by the exact discretization
  error itself, so the round-off-level corrected error they report there
  holds by construction *(compiler check, not in the sources)*.
- Mozaffari et al. (2022, §3.3) state that, to their knowledge, no
  refinement criterion had been evaluated for hybrid RANS/LES; Basile et
  al. (2023) is later and uses a different (DG-specific) criterion.

# Citations

- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — author manuscript, §1 (Fig. 1), §2 (Eqs. 1–4), §3, §4.1–4.5 (Table 2, Figs. 6, 9–15), §5.1–5.2 (Figs. 18–23, 26–27), §6.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §3 (Algorithms 1–2), §4.3, §5, §6 (Eqs. 30–38), §7 (Table 1), §8.1.3, §8.2.4–8.2.6 (Figs. 32, 40, Table 3), §9.
- [Basile et al. (2023)](/sources/basile-2023.md) — HAL accepted manuscript, §1, §3.1–3.4 (Eqs. 8–19), §4.1, §4.2.1–4.2.3 (Table 1), §4.4.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1, §2.1–2.2 (Fig. 2), §3.2 (Figs. 6–7).
- [Blind et al. (2023)](/sources/blind-2023.md) — arXiv v1: §1 (earlier resolution measures), §2.1–2.5, Eqs. 1–7 (modelling residual, DG test filter, optimal spacing, workflow), §3.1–3.3, Tables 1–4, Figs. 1–11 (channels), §4, Tables 5–6, Figs. 12–14 (airfoil), §5.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — arXiv v1: §3.6–3.6.2, Figs. 1–2 (anisotropic p-adaptation, $\tau$-estimation, interface tracking), §4.7, Fig. 14.
- [Dahlin et al. (2022)](/sources/dahlin-2022.md) — arXiv v1: §3 (ARMS adaptive mesh, refined region; no criterion stated).
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — App. A, Eqs. A.1–A.3, Fig. 32 (metric-based $L^2$ adaptation, kinetic-energy sensor, loop, wall treatment); §3 (validation mesh); §4.2.2, Fig. 12 (circulation against iterations).
- [Ruan et al. (2023)](/sources/ruan-2023.md) — §2 (five-level AMR, no criterion stated, numerical scheme).
- [Constant et al. (2024)](/sources/constant-2024.md) — HAL author manuscript: §3.1 (octree Cartesian meshes), §4.2 (modelling-height adaptation without mesh change).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §6, Fig. 13 (Rotor 37 cascade LES on a fixed mesh, local shock-capturing blending).
- [Schotte et al. (2026)](/sources/schotte-2026.md) — HAL deposit of the version of record: §1, §2.2–2.5 (DG, CODA, Tucanos), §3.1–3.2, Eqs. 15–25 (element Hessian, scaling, SSED and SSL), §3.3, Figs. 3–7, §4.1–4.5, Tables 2, 4, Figs. 9–25, §5.
- [Wang et al. (2013)](/sources/wang-2013.md) — §2 (survey, Q3, Q6), §5.2, Figs. 16–19 (NACA 0012 adaptation), §4.8 (RAE 2822 case 9 conditions), §5.4, Fig. 23, Table V (RAE 2822 RANS), §6 (conclusions, pacing items, RANS robustness).
- [Wang & Roy (2023)](/sources/wang-2023.md) — journal pre-proof: §3.1, Eqs. 11–16 (error transport equations, expected orders), §4.1, Table 1, Fig. 2, §4.2, §5.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §II.B (invariants from mesh-adaptation work, normalization instead of thresholds).
- [Fidkowski (2022)](/sources/fidkowski-2022.md) — §2.1–2.3, Eqs. 2–9 (DG, simplified DES, augmented system, adjoint); §4, Eqs. 14–23 (time-averaged adjoint-weighted residual, E1 and E2); §5.1–5.3, Eq. 24, Fig. 2 (indicators, $p$-adaptation, MOESS, loop); §6, Tables 1–3, Figs. 4–19; §7.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §3.3.2, Fig. 24 (octree coarse–fine interfaces reflect acoustic waves).
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §1 (EPIC shared by BCFD and GGNS); §4.2 (CAD projection); §4.3, Figs. 7–9 (output-based against Hessian adaptation, method comparison of Michal et al., loop, unsteady memory, chaotic adjoints); §4.4, Fig. 4 (adaptive higher-order finite elements); §5.
- [Ims & Wang (2023)](/sources/ims-2023.md) — §1 (adjoint impractical for LES, h against p); §2 (FR/CPR implicit LES); §3.1–3.3, Eqs. 7–22 (three indicators); §4 (marking, splitting, mortars); §5–6, Figs. 5–34 (cascades, random control, recommendations).
- [Sun et al. (2023)](/sources/sun-2023.md) — §2.2.2, Table 1, Fig. 2 (2-D density-gradient AMR in OpenFOAM); §3.9, Figs. 15–16 (cell and CPU savings).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.6, Fig. 8 (isotropic h-AMR with hanging nodes in DG, $\lvert\nabla\rho\rvert$ criterion); §6.2, Figs. 12–13 (h at the shock, p near the wall).
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §3.1 (adaptive-mesh one-dimensional turbulence, cited).
