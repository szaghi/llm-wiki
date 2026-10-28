---
type: Method
title: "Boundary-layer-conforming grids for wall-modelled LES"
description: "Grids whose local isotropic cell size follows the local boundary-layer thickness, floored by a minimum grid Reynolds number at leading edges and capped by surface curvature; the boundary-layer-thickness estimate they need, their cost, the evidence that they reduce WMLES error at fewer points than constant-size grids, and the opposite thickness-relative constraint of detached-eddy grids."
status: established
aliases: [BL-conforming grid, boundary-layer-conforming mesh, delta-conforming grid]
tags: [wmles, mesh-adaptation, boundary-layer, wall-model]
timestamp: 2026-10-28T07:09:00Z
---

# Boundary-layer-conforming grids for wall-modelled LES

A boundary-layer-conforming (BL-conforming) grid sets the local, isotropic cell
size $\Delta$ of a [wall-modelled LES](/methods/wall-modelled-les.md) to a fixed
fraction of the local boundary-layer thickness, $\Delta\approx\delta/n_\delta$,
so that every boundary layer is resolved by the same number of points
$n_\delta$ (page-local) across its thickness. [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md)
formulate it, build it for the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
in [CharLES](/software/charles.md), and compare it with constant-size grids;
they state that all published WMLES cost estimates assume such a grid, yet
"WMLES of an aircraft geometry has never been conducted using a true
BL-conforming grids until the present work" (§III.B). [Goc et al. (2021)](/sources/goc-2021.md)
(§2.2) cite the same work as the route to reducing WMLES cost, and use the
simpler constant-size practice described below.

## Grid-size rule

Because $\delta\to0$ at leading edges, the rule needs a floor; because $\delta$
can exceed the local radius of curvature, it needs a cap. Lozano-Durán et al.
(2022, §III.A, Eq. 2) set

$$\Delta(\boldsymbol x)\approx\min\left[\max\left(\frac{1.2\,\delta}{n_\delta},\ \frac{Re_\Delta^{\min}\,\nu}{U_\infty}\right),\ \frac{R_c}{2}\right],$$

with $R_c$ the local surface radius of curvature (page-local), the factor 1.2 a
margin to contain the instantaneous boundary layer, and
$Re_\Delta^{\min}=\Delta_{\min}U_\infty/\nu$ "the minimum local Reynolds number
that we are willing to marginally resolve": where the boundary layer is
thinner than $\delta_{\min}=n_\delta\Delta_{\min}$ the grid size stays at
$\Delta_{\min}$. The grid is locally isotropic and blends to a far-field size
(200 mm in their case). Both of their gridding strategies build Voronoi cells
from hexagonally close-packed seeds; for the constant-size grids they state
ten Lloyd iterations to smooth the transitions between layers.

The two parameters separate two questions: $n_\delta$ sets the accuracy of
the developed boundary layers, $Re_\Delta^{\min}$ the treatment of the leading
edge.

## Estimating the boundary-layer thickness

The rule needs $\delta$ on the whole surface before the production grid
exists. Lozano-Durán et al. (2022, §III.A, Eqs. 3–4) run two simulations on a
preliminary constant-size grid ($\Delta=2$ mm): a WMLES, and an inviscid one
(free-slip walls, no SGS model). The boundary-layer edge is the surface where
the time-averaged velocities differ by 1 %,

$$\frac{\lVert\langle\boldsymbol u_I\rangle-\langle\boldsymbol u\rangle\rVert}{\lVert\langle\boldsymbol u_I\rangle\rVert}=0.01 ,$$

with $\boldsymbol u_I$ the inviscid velocity (page-local), and $\delta$ at a
surface point is its distance to that edge surface. Layers thinner than 2 mm at
the leading edge are extrapolated by a power law; Q-criterion isosurfaces as
edge surface gave similar results. On the Juncture Flow $\delta$ runs from
about 0 at the wing leading edge to about 30 mm at the wing trailing edge and
over 50 mm on the aft fuselage (Fig. 5c).

## Cost

Counting only points inside the boundary layer (Eq. 5),
$N_{\mathrm{pts}}=\iint_{S}n_\delta\,\Delta^{-2}\,dA$, and for a flat plate with
$\delta/x=0.16\,Re_x^{-1/7}$ and $Re\gg Re_\Delta^{\min}$ (Eq. 6, App. A),

$$N_{\mathrm{pts}}\sim n_\delta^{13/6}\,Re\,\left(Re_\Delta^{\min}\right)^{-5/6},\qquad N_{\mathrm{steps}}\sim t_{\mathrm{run}}\,Re\left(Re_\Delta^{\min}\right)^{-1},$$

with $t_{\mathrm{run}}$ the run length in flow-through times (registry §11, as on the [grid-point requirements](/results/les-grid-point-requirements.md) page). With the
leading-edge extent fixed instead of $Re_\Delta^{\min}$ the exponent of
$n_\delta$ becomes 3 (Eq. 14). Further consequences are on the
[grid-point requirements](/results/les-grid-point-requirements.md) page.

## Evidence

On the Juncture Flow at $Re=2.4\times10^6$ (crank chord), Lozano-Durán et al.
(2022, §V) compare five constant-size grids (C-D7 to C-D0.5, 14–174 M cells,
31–398 thousand core-hours) with three BL-conforming ones:

| Case | $n_\delta$ | $Re_\Delta^{\min}$ | $\Delta_{\min}$ | Cells | Core-hours |
|---|---|---|---|---|---|
| C-N5-R2e3 | 5 | $2.8\times10^3$ | 0.6 mm | 12 M | 27 000 |
| C-N10-R2e3 | 10 | $2.8\times10^3$ | 0.3 mm | 40 M | 90 000 |
| C-N5-R5e3 | 5 | $5.6\times10^3$ | 1.3 mm | 6 M | 13 000 |

- BL-conforming grids are more accurate at all three stations; at the
  wing–body juncture and the separated trailing edge they lower the error
  constant $b_u$ of $e_u=b_u(\Delta/\delta)^{a_u}$ (registry §11, see
  [wall-modelled LES](/methods/wall-modelled-les.md)) and leave the rate
  $a_u$ unchanged (§V.C, Fig. 17a).
- C-N5-R2e3 (12 M cells) beats the constant-size C-D2 (31 M) at the juncture
  and trailing edge "using only one fourth of the number of grid points in each
  spatial direction (namely, a factor of 64 less points in the local volume)";
  the number of control volumes is therefore "a misleading metric" of WMLES
  quality (§V.C, Fig. 16).
- **Why constant-size grids lose.** A constant-size grid is agnostic of
  $\delta$: it puts less than one point per $\delta$ on the nose and wing
  leading edge and up to hundreds on the aft fuselage (§III.A). Errors made at
  the under-resolved leading edge are advected downstream over a recovery
  length $\Delta x_e\approx\Gamma U_\infty\delta_0/u_\tau$, about $300\delta_0$
  in high-$Re$ zero-pressure-gradient layers (page-local $\Delta x_e$,
  $\Gamma$, $\delta_0$). Re-plotting errors against an upstream
  Gaussian-averaged thickness collapses the constant-size fuselage errors onto
  the channel reference, "confirming that the diminished performance of
  constant-size grids is merely a matter of downstream error propagation"
  (§V.C, Fig. 17b).
- **Leading-edge parameter.** Halving $Re_\Delta^{\min}$ improves downstream
  profiles; errors converge as $(Re_\Delta^{\min})^{a}$ with $a\approx1$–2,
  steeper than in $n_\delta$, so leading-edge requirements are less demanding
  than those of the developed layers (§V.D, Fig. 19d). A model
  $e_u\sim n_\delta^{-1}\left[1+\Gamma Re_\Delta^{\min}n_\delta/\big(Re_x-(Re_\Delta^{\min}n_\delta/0.16)^{7/6}\big)\right]$
  with $\Gamma=300$ reproduces the trend. The under-resolved region for
  $Re_\Delta^{\min}<10^4$ covers less than 10 % of the chord (§III.B, Fig. 6b).
- The wall pressure is insensitive to all of this (errors below 5 % on every
  grid); the advantage concerns the velocity field.
- **Reuse with a learned wall model.** [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
  (§3.1, §4.8) run their Juncture Flow WMLES on the BL-conforming grid of
  Lozano-Durán et al. (2022) with 5 points per $\delta$, testing the
  [building-block-flow wall model](/methods/building-block-flow-wall-model.md)
  against the equilibrium model. The trailing-edge corner separation bubble
  is $0.3\delta$ thick on a grid of $\Delta\approx0.2\delta$, so it is spanned
  by about one grid point and external (SGS-model) errors dominate there; the
  learned model is better but "far from satisfactory" (Table 1).

## The varying thickness as a known gap

The WMLES review of [Bose & Park (2018)](/sources/bose-2018.md) (§3, Fig. 5)
names the difficulty of grids that follow a varying thickness. Comparing published
airfoil WMLES with Chapman-type estimates, they find that most calculations
need an outer-layer resolution of $n_xn_yn_z\gtrsim20^3$ points per
$\delta^3$ ($n_i$ the points per $\delta$ in direction $i$, page-local), and
that the scatter at equal Reynolds number "may be partially explained by
the difficulty in generating optimal grids", i.e. grids with
$\delta^3/(\Delta x\Delta y\Delta z)$ fixed, when $\delta=\delta(x)$: in
practice grids for complex geometries are set from "a nominal or average
boundary-layer thickness", as in Chapman's estimates, which "underscores
the need for concurrent development of mesh generation technologies" with
near-wall modelling. The same section treats the cost of thin laminar
regions: with isotropic cells they can dominate the count, $N\propto\int\delta^{-2}dA$,
but the isotropy assumption rests on outer-layer turbulence structure
($y/\delta>0.1$) and modest aspect ratios, $AR=O(10)$, would cut the
prefactor "by orders of magnitude"; relaxing the laminar resolution,
however, presupposes that the LES captures transition (see
[grid-point requirements](/results/les-grid-point-requirements.md)).

[Lv et al. (2021)](/sources/lv-2021.md) (§V) cite two preprints of
Lozano-Durán and co-workers, one of them the BL-conforming grid study, for
the view that advances in WMLES require "novel modeling venues encompassing
physical insights, together with improved gridding and numerical methods".
On the [periodic hill](/benchmarks/periodic-hill.md) their own runs find
that grid resolution "has a more notable impact on the results than the
wall model": the coarse grid, which does not capture the pressure force, is
noticeably worse than both regular-grid runs, one with an equilibrium and
one with their integrated wall model (§IV B 2; see
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)). Their
grids are body-fitted.

## Contrast: grids for detached-eddy simulation

Grid design relative to $\delta$ has the opposite sign in
[detached-eddy simulation](/methods/detached-eddy-simulation.md), where the
boundary layer must stay in RANS mode. [Delassaux et al. (2023)](/sources/delassaux-2023.md)
(§4.1.3, §4.4) state the criterion as keeping the largest wall-parallel
spacing $\Delta_{\max}$ above $\delta$, and cite Menter, who, with
$r=\Delta_{\max}/\delta$ (page-local), finds the effect of refinement delayed
to $r<0.2$ in DDES against $r<1$ in DES; violating it lets LES enter a
boundary layer it cannot resolve and produces grid-induced separation
(modelled-stress depletion). Their full-scale car grid is therefore
deliberately coarse on flat areas — 10 mm surface triangles, about
$\Delta x^+\approx600$ on the roof, against about 300 on the roof of their
Ahmed-body calibration with 4 mm — and wall-resolved in the normal direction:
20 prism layers with first height 0.020 mm and growth ratio 1.4 ($y^+\approx1$)
enclosing the boundary layer, or 30 layers with ratio 1.23, below the 1.25
advised by Spalart & Streett as they cite it; going from 20 to 30 layers
leaves the drag unchanged (§6, Table 3). Along a rounded separation line a
3 mm surface mesh is "too fine and leads to GIS", and 6 mm is advised (§7.3,
Fig. 21). The WMLES grid of this page refines towards $\delta/n_\delta$ to
resolve the outer eddies; the DES grid keeps the wall-parallel spacing large
against $\delta$ to protect the RANS layer.

## Constant-size practice for comparison

Goc et al. (2021, §3, §4) size their [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
grids uniformly and isotropically in all directions for about ten points
across the main-element trailing-edge boundary layer, $\delta_{99}/\Delta\approx10$,
predicted by a zero-pressure-gradient correlation on the mean aerodynamic
chord, with extra clustering at the slat leading edge for the inviscid
acceleration; the leading edges thus receive fewer points per $\delta$. They
generalize the practice as "a chosen $O(1)$ number of cells per boundary-layer
thickness at the trailing edge of the main element", complemented near leading
edges by keeping the grid spacing times the pressure gradient small for the
scheme used. This sufficed for $C_{L,\max}$ within five lift counts; the
coarsest grid under-predicts the outboard slat and main-element suction,
which they link to under-resolved leading-edge acceleration (§3.2, Fig. 9).

## Workshop practice on a full high-lift aircraft

In the HLPW-4 wall-modelled LES focus group on the
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) configuration,
summarized by [Kiris et al. (2023)](/sources/kiris-2023.md), the grids
were structured
overset curvilinear (W-020), isotropic Voronoi (W-021, [CharLES](/software/charles.md)),
unstructured anisotropic with very low wall-normal spacing near leading
edges (W-034), Cartesian isotropic with immersed boundaries (W-032,
W-049), and unstructured with aspect ratios from 1 to 71 (Table 2,
aspect ratio as the tangential-to-wall-normal spacing). The authors
(§I.2) frame the choice of grid isotropy as an open question: off-body
vorticity (chine vortex, slat and flap tip vortices) has no preferred
direction and suits isotropic grids, while thin leading-edge boundary
layers favour anisotropic cells. They set this against the larger
requirement the workshop found:

- **Inviscid curvature, not wall-layer resolution, set the leading-order
  grid requirement.** The suction peaks on the outboard slats and
  main-element leading edges ($C_p$ down to $-16$) must be resolved to
  predict the pitching moment, and "this curvature imposes a minimum
  requirement for grid spacing to accurately predict the inviscid potential
  flow effects" (§I.3). W-021's refinement from 12 M to 362 M degrees of
  freedom converged largely monotonically, which the authors read as a
  kinematic leading-order effect, curvature-induced acceleration (§III,
  Fig. 6). Every submission that met the outboard suction criterion had
  more than 250 M degrees of freedom (§IV, Fig. 12; see
  [grid-point requirements](/results/les-grid-point-requirements.md)).
- **Isotropic against anisotropic: no clear answer.** W-034 found that
  anisotropic grids with finer near-wall spacing, at a small cost in
  aspect ratio, gave more accurate outboard $C_p$ on coarser grids than
  unity-aspect-ratio Voronoi grids with larger wall-normal spacing. They
  also predicted a large-scale wing-root separation not seen on the
  Voronoi grids (§III, §IV.3, Figs. 8, 16, 21). W-020's off-wall
  refinement (275 M to 360 M) resolved the chine vortex better and delayed
  the onset of corner separation by more than 1.5° (§III, Fig. 7). The
  summary concludes that "no clear answer can be provided" (§VI.2).

Goc et al. (2021) cluster points at the slat leading edge for the inviscid
acceleration (above).

## Contrast: automatic anisotropic adaptation

A different route to resolving boundary layers without designing the mesh by
hand is metric-based [mesh adaptation](/methods/mesh-adaptation.md).
[Alauzet et al. (2022)](/sources/alauzet-2022.md) adapt purely tetrahedral,
anisotropic meshes for steady RANS (Spalart–Allmaras) of turbomachinery and
argue that prismatic or hexahedral boundary-layer meshes are "not absolutely
necessary" (§1, §9). On NASA Rotor 37 their feature-based adaptation (an
$L^4$ interpolation-error estimate of the Mach number) yields a first-cell
$y^+=1$ ahead of the shock and $y^+\approx2$ in the separated layer behind it,
the same on the coarsest (0.36 M vertices) and finest (2.8 M vertices)
adapted meshes, so the adaptation converges in the boundary layer without
over-refining (§8.2.5, Fig. 40); the mean anisotropic quotient of their 10 M
vertex mesh, about $10^4$, stands for "almost four order of magnitudes" fewer
elements than an isotropic adapted mesh (§8.2.6, Table 3). The comparison
concerns wall-resolved RANS, where the mesh follows the viscous sublayer; the
BL-conforming grid of Lozano-Durán et al. is isotropic and sized by $\delta$
for WMLES. No source of this bundle applies either approach to the other's
problem.

## Contrast: high-aspect-ratio grids of wall-resolved high-order RANS

Wall-resolved RANS keeps hand-built anisotropic near-wall cells, and the
cost of that choice falls on the discretization. [Huang et al. (2022b)](/sources/huang-2022-d.md)
build a fourth-order cell-centred finite-volume solver for
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS on mixed
triangle–quadrilateral grids whose near-wall quadrilaterals have aspect
ratios of $10^2$–$10^3$ (first cell $5\times10^{-6}$ chord, growth 1.2–1.4;
$y^+\approx0.5$–1 on their flat plate), and state that such cells degrade the accuracy of
high-order reconstruction (§1, §2.4). Their reconstruction is the compact
*variational reconstruction* (after Wang, Ren, Pan et al., as cited): the
degree-$k$ polynomial of each cell minimizes, over all faces, an
interface-jump integral of the polynomial and its derivatives,

$$I_f=\mathcal W^G_f\int_f\sum_{p+q\le k}\mathcal W^D_f(p,q)\left(\frac{\partial^{p+q}\phi_i}{\partial x^p\partial y^q}-\frac{\partial^{p+q}\phi_j}{\partial x^p\partial y^q}\right)^2dS,$$

which leads to a symmetric positive-definite global system with a unique
solution, solved by block Gauss–Seidel with one sweep per implicit
iteration, and uses face neighbours only (§2.3, Eqs. 19–25; $\mathcal W^G_f$,
$\mathcal W^D_f$ the geometric and derivative weights, $\phi_i$, $\phi_j$ the
reconstructed polynomials of the cells $i$, $j$ sharing face $f$, $k$ the
reconstruction degree, all page-local).

**Weights for stretched cells** (§2.4, Eqs. 26–51). The authors restrict the
derivative weights to $\mathcal W^D_f(p,q)=\varpi_{p+q}d_{ij}^{\,p+q}$ with
$\varpi_0=1$ and non-increasing $\varpi_n$, and the geometric weight to
$\mathcal W^G_f=(\lvert f\rvert/d_{ij})^{a_g}$ ($d_{ij}$ the distance between cell
centroids, $\lvert f\rvert$ the face length (the source's $S_{i,j}$), $\varpi_n$, $a_g$ page-local). The
$\varpi_n$ come from a modified-wavenumber analysis of one-dimensional
advection with a monotonicity constraint (cubic: $\varpi_1=0.5295$,
$\varpi_2=\varpi_3=0.2117$; quadratic: 0.4643, 0.1559; Table 1); the
unconstrained optima have better dispersion and dissipation curves but much
less dissipation and give schemes the authors found "not robust". The
exponent comes from a two-dimensional analysis on rectangles of aspect
ratio up to 1000: for linear reconstruction the objective is minimised for
$a_g\ge1/2$ at all aspect ratios and advection angles tested, and $a_g=1/2$
is "near-optimal" for quadratic
(optimum 3/2 for inclined advection at aspect ratio 1000), and is taken for
all degrees (Figs. 7–8, Eq. 51). The three-step procedure is called "of
course not rigorous"; the 3D weights are proposed but not tested.

**Evidence.** On a manufactured turbulent-boundary-layer profile (a
Reichardt-type law, see [law of the wall](/definitions/law-of-the-wall.md))
the $L_2$ error of $\partial u/\partial y$ of the cubic reconstruction is
$1.39\times10^{-3}$ and $7.33\times10^{-4}$ on a uniform mesh of aspect
ratio $5\times10^2$ and a curved mesh of about $10^3$, against
$3.49\times10^{-3}$ and $6.84\times10^{-2}$ with the weights of Pan et al.
and $5.22\times10^{-3}$ and $1.38\times10^{-3}$ with those of Cheng et al.
(as cited); optimal derivative weights combined with Pan et al.'s geometric
weight diverge on the first mesh, so the geometric weight must be optimized
too (§2.4.3, Table 3). On the [NACA 0012](/benchmarks/naca-0012-airfoil.md)
at $15^\circ$ ($Re_c=2.88\times10^6$, $M_\infty=0.15$, 11 880 to 33 150 cells) the
fourth-order scheme reaches a lift error of 0.19 % on the third mesh, where
the second-order one is at 14.88 % and still predicts a spurious
trailing-edge separation; by their efficiency measure, inverse error times
CPU time, the fourth-order scheme improves under refinement while the
second-order one degrades (§3.2, Tables 5–6). The study is two-dimensional,
steady and wall-resolved; it addresses the stretched cells that wall-resolved
RANS needs, the opposite of the isotropic $\delta$-sized cells of this page.

## Qualifications

- The method's evidence comes from one group, on one geometry and one
  Reynolds number (Lozano-Durán et al. 2022; reused by Lozano-Durán & Bae
  2023 without a constant-size comparison); its rule depends on a preliminary
  WMLES and inviscid solution.
- Lozano-Durán et al. contrast their low leading-edge sensitivity at small
  angle of attack with NACA 0012 cases in which the whole-chord solution
  depended strongly on leading-edge grid details (Goc, personal communication,
  as they cite it, §V.D).
- Printed slips in the version read (arXiv v1): §V.D gives
  $Re_\Delta^{\min}=2.6\times10^3$ and $5.8\times10^3$ for C-N5-R2e3 and
  C-N5-R5e3, while §V.A, the Fig. 18 caption and the case names give
  $2.8\times10^3$ and $5.6\times10^3$; §V.A says "the first six cases" use
  constant-size grids where five are listed.
- **Printed slips of Huang et al. (2022b).** On p. 13 the constraint drawn
  "according to Eq. (27)" is printed $\varpi_1\le\varpi_2\le\varpi_3$, the
  reverse of Eq. (27), which their Table 1 values satisfy
  ($0.5295\ge0.2117\ge0.2117$). Table 6 prints a lift error of 5.74 % for
  the second-order scheme on the 143 700-cell mesh with $C_L=1.437$ against
  the reference 1.526, which gives 5.83 %; the printed efficiency 0.791 is
  consistent with 5.74 % *(compiler check, not in the sources)*. That mesh is
  called "even smaller" although it has the most cells.

# Citations

- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §III.A, Eqs. (2)–(4), Figs. 3–5; §III.B, Eqs. (5)–(7), Fig. 6; §V.A–V.E, Figs. 16–21; App. A, Eqs. (13)–(14).
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.2; §3, Fig. 9; §4.
- [Alauzet et al. (2022)](/sources/alauzet-2022.md) — §1; §8.2.5–8.2.6, Fig. 40, Table 3; §9.
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.1; §4.8, Table 1, Fig. 18.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.3; §4.4, Table 1, Fig. 8; §6, Table 3; §7.3, Fig. 21 (HAL author manuscript).
- [Huang et al. (2022b)](/sources/huang-2022-d.md) — §1; §2.3, Eqs. (19)–(25); §2.4, Eqs. (26)–(51), Tables 1–3, Figs. 7–8; §3.2, Tables 4–6.
- [Bose & Park (2018)](/sources/bose-2018.md) — §3, Eq. (2), Fig. 5.
- [Lv et al. (2021)](/sources/lv-2021.md) — §IV B 2, Figs. 15–16; §V.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — §I.2–I.3; Table 2; §III, Figs. 6–8; §IV, Figs. 12, 16, 21; §VI.2.
