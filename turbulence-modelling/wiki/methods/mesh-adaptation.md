---
type: Method
title: "Mesh adaptation for turbulent-flow simulation"
description: "Changing the mesh (h, p or hp; isotropic or anisotropic) from an error estimate or refinement criterion in a turbulent-flow computation: Hessian and metric criteria for RANS, time-averaged criteria for hybrid RANS/LES, LES modelling-residual and truncation-error estimators for high-order DG, and refinement strategy as a dissipation control."
status: established
aliases: [adaptive mesh refinement, AMR, adaptive grid refinement, AGR, anisotropic mesh adaptation, metric-based mesh adaptation, hp-adaptation, average-based mesh adaptation, goal-oriented mesh adaptation, grid adaptation for LES, LES modelling residual, Toosi–Larsson residual estimator, tau-estimation, p-adaptation]
tags: [mesh-adaptation, hybrid-rans-les, rans, dg, numerical-dissipation, wmles]
timestamp: 2026-10-26T15:41:00Z
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

| Part | Mozaffari et al. (2022) | Alauzet et al. (2022) | Basile et al. (2023) | Blind et al. (2023) | Ferrer et al. (2023) | Martin-Alvarez et al. (2022) |
|---|---|---|---|---|---|---|
| Flow and model | incompressible hybrid RANS/LES (IDDES, DDES-SST) and RANS, ISIS-CFD | steady compressible RANS, Spalart–Allmaras without $f_{t2}$, Wolf | compressible ZDES on the negative Spalart–Allmaras model, modal DG (CODA) | wall-resolved and wall-modelled LES with the Vreman model, DGSEM ([FLEXI](/software/flexi.md)) | compressible and multiphase flows, DGSEM ([HORSES3D](/software/horses3d.md)) | ideal MHD, cosmological galaxy formation, RAMSES |
| Criterion | Hessians of $p$ and $u_i$, time-averaged | $L^4$ Mach-number interpolation error or adjoint-weighted goal-oriented estimate | modal small-scale energy plus inter-element jumps; modal-decay smoothness | directional LES modelling residual from a modal test filter, time- and element-averaged | truncation error ($\tau$-estimation); interface tracking for multiphase | mass per cell (quasi-Lagrangian) or a density threshold (quasi-Eulerian) |
| Operation | anisotropic h-refinement and derefinement of hexahedra by cell division | anisotropic remeshing of tetrahedra to a metric (Feflo.a) | isotropic remeshing (MMG) plus p-enrichment, $N\in\{1,2,3\}$; prism layer frozen | anisotropic hexahedral grids built by hand to the target spacing, 2-to-1 mortars | anisotropic p-adaptation, a degree per element and direction, mortar faces | octree refinement, at most one level jump |
| Driver | refinement every 25 steps (backward-facing step) | mesh-convergence loop at doubled complexity | static steps, dof count doubled per step | post-processing between full LES runs, about four times the elements per step | one step on a converged moderate-degree solution (steady) or at fixed intervals (unsteady) | every step, on the running flow |

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
discuss numerical dissipation.

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
  in the $L^2$ norm, which, as recalled there, gives more wake resolution
  than $L^4$ (App. A).
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
  following Chapelier and Lodato's spectral-element dynamic model; as
  recalled there, the threshold was evaluated a priori from Taylor–Green
  DNS at $Re=5000$ (§3.2). Elements with $\sigma>5/3$ are p-enriched (up
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
method of Toosi and Larsson (as recalled there, §1–2) from finite-difference
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
date". Mozaffari et al. (2022, §3.3) recall the same authors' criterion as
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
  multigrid cycle. As recalled from the group's earlier work, the
  truncation error controls all functional errors (§3.6.1–3.6.2).
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
path of the turbulence.

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
numerical), standard quasi-Lagrangian refinement (refine when a cell's mass
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

## Qualifications

- **Scope of each criterion.** Mozaffari et al. test their Hessian
  criterion for hybrid RANS/LES only indirectly (threshold convergence and
  the refinement-box test), and it misses low-velocity recirculation;
  Alauzet et al.'s goal-oriented estimate omits the turbulence equation;
  Basile et al.'s $5/3$ threshold identifies a modal degree with a Fourier
  wavenumber, which the paper presents as a "similarity" (§3.2).
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
