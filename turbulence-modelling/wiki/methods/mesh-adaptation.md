---
type: Method
title: "Mesh adaptation for turbulent-flow simulation"
description: "Changing the mesh (h, p or hp; isotropic or anisotropic) from an error estimate or refinement criterion during a turbulent-flow computation: Hessian and metric criteria for RANS, time-averaged criteria for hybrid RANS/LES, hp-adaptive DG with turbulence-based indicators, and refinement strategy as a control of numerical dissipation."
status: established
aliases: [adaptive mesh refinement, AMR, adaptive grid refinement, AGR, anisotropic mesh adaptation, metric-based mesh adaptation, hp-adaptation, average-based mesh adaptation, goal-oriented mesh adaptation]
tags: [mesh-adaptation, hybrid-rans-les, rans, dg, numerical-dissipation]
timestamp: 2026-10-25T19:46:00Z
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

| Part | Mozaffari et al. (2022) | Alauzet et al. (2022) | Basile et al. (2023) | Martin-Alvarez et al. (2022) |
|---|---|---|---|---|
| Flow and model | incompressible hybrid RANS/LES (IDDES, DDES-SST) and RANS, ISIS-CFD | steady compressible RANS, Spalart–Allmaras without $f_{t2}$, Wolf | compressible ZDES on the negative Spalart–Allmaras model, modal DG (CODA) | ideal MHD, cosmological galaxy formation, RAMSES |
| Criterion | Hessians of $p$ and $u_i$, time-averaged | $L^4$ Mach-number interpolation error or adjoint-weighted goal-oriented estimate | modal small-scale energy plus inter-element jumps; modal-decay smoothness | mass per cell (quasi-Lagrangian) or a density threshold (quasi-Eulerian) |
| Operation | anisotropic h-refinement and derefinement of hexahedra by cell division | anisotropic remeshing of tetrahedra to a metric (Feflo.a) | isotropic remeshing (MMG) plus p-enrichment, $N\in\{1,2,3\}$; prism layer frozen | octree refinement, at most one level jump |
| Driver | refinement every 25 steps (backward-facing step) | mesh-convergence loop at doubled complexity | static steps, dof count doubled per step | every step, on the running flow |

The models and codes have their own pages:
[detached-eddy simulation](/methods/detached-eddy-simulation.md) (the
DDES, IDDES and ZDES of Mozaffari et al. and Basile et al.), the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) (Alauzet et
al., Basile et al.), [RAMSES](/software/ramses.md) and the
[small-scale dynamo](/results/small-scale-dynamo.md) (Martin-Alvarez et
al.); Mozaffari et al.'s calibration case is the
[backward-facing step](/benchmarks/backward-facing-step.md).

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
spectrum lies, likely in the inertial range (§3.2). Pure p-adaptation on a
fixed mesh would need very high degrees, with load-balancing problems,
higher cost per degree of freedom and aliasing instabilities (§1).

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
- Mozaffari et al. (2022, §3.3) state that, to their knowledge, no
  refinement criterion had been evaluated for hybrid RANS/LES; Basile et
  al. (2023) is later and uses a different (DG-specific) criterion.

# Citations

- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — author manuscript, §1 (Fig. 1), §2 (Eqs. 1–4), §3, §4.1–4.5 (Table 2, Figs. 6, 9–15), §5.1–5.2 (Figs. 18–23, 26–27), §6.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §3 (Algorithms 1–2), §4.3, §5, §6 (Eqs. 30–38), §7 (Table 1), §8.1.3, §8.2.4–8.2.6 (Figs. 32, 40, Table 3), §9.
- [Basile et al. (2023)](/sources/basile-2023.md) — HAL accepted manuscript, §1, §3.1–3.4 (Eqs. 8–19), §4.1, §4.2.1–4.2.3 (Table 1), §4.4.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — §1, §2.1–2.2 (Fig. 2), §3.2 (Figs. 6–7).
