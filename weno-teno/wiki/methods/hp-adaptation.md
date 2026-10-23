---
type: Method
title: "h- and hp-adaptation for DG"
description: "Adaptive DG refines the mesh (h) or raises the polynomial degree (p) where an estimator is large: Basile et al.'s hp loop with a modal-decay smoothness test on shock-free flows, Bai and Li's quadtree h-refinement, Mossier et al.'s p-adaptation with finite-volume subcells on a static mesh, Kou et al.'s static p-refinement, and Abgrall et al.'s entropy-stable degree transfer."
status: established
aliases: [hp-adaptivity, h-adaptation, p-adaptation, p-refinement, metric-based mesh adaptation, a posteriori error estimation, SSED estimator, hp-shock capturing]
tags: [dg, amr, entropy-stable, limiting, turbulence]
timestamp: 2026-10-22T16:24:00Z
---

# h- and hp-adaptation for DG

In solution-adaptive [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
computations, an a posteriori error estimator marks the elements whose
error is large. Each marked element is then refined, either by a smaller
size (h-adaptation) or by a higher polynomial degree (p-enrichment).
hp-adaptation chooses between the two per element: p-enrichment where the
solution is smooth, h-refinement where it is not.
[Basile et al. (2022)](/sources/basile-2022.md) build an isotropic,
metric-based h- and hp-adaptation loop for a modal DG discretization of
steady compressible laminar Navier–Stokes and RANS–Spalart–Allmaras flows
on unstructured simplicial and hybrid meshes. The loop is implemented in
the Airbus–ONERA–DLR solver CODA, with the open-source remesher MMG (§1–3).

## Discretization

The DG space uses a hierarchical orthonormal modal basis built per element
by modified Gram–Schmidt on monomials, so the mass matrix is diagonal and
the modes of each total degree $\ell$ form a group. The convective flux is
Roe's with a Harten-type entropy fix, and the viscous terms use BR1.
Steady states are reached by implicit backward Euler with matrix-free
GMRES (§2.3, Eqs. (15)–(23)). Degree $N_K$ may vary per element.

## Error estimator

The estimator works on the momentum magnitude, written here
$m_h=\lvert\rho v\rvert_h$ (page-local). The error of degree $N_K$ is
modelled by the content of the highest modes, $\lVert u_h-u\rVert\approx\lVert u_{h,N}-u_{h,N-1}\rVert$,
with $u_{h,N-1}$ the truncation to degree $N_K-1$ (Eq. (28)). Two
indicators are summed (Eqs. (29)–(35)); page-local $\mathsf E$ denotes
estimator values.

- **Small-scale energy density (SSED).**
  $\mathsf E^2_{\mathrm{SSED},K}=\lVert m_{h,N}-m_{h,N-1}\rVert^2_{L^2(K)}/\lvert K\rvert$.
- **Interface jump.** On each face $e$ of $K$,
  $\mathsf E^2_{\mathrm{JUMP},e}=\int_e\lvert[\![m_h]\!]\rvert^2dS\,/\,(4\lvert e\rvert)$,
  averaged over the faces of $K$. The factor $\tfrac14$ comes from taking
  the face average as the exact trace.
- **Combination.** Each indicator is min–max normalized over the mesh and
  the two are added, so $\mathsf E_K\in[0,2]$.

Basile et al. depart from Colombo et al. and Bassi et al., as they recall
them. Those works weight the jump term down as $N$ grows and switch the
modal term off at $N=1$. Basile et al. use the same sum for every degree,
and dimensional estimators on the momentum rather than estimators on the
pressure normalized by the solution (§4.1). They state that dimensional
estimators behave better in recirculation zones, where small momentum
biases normalized ones, after Naddei. No comparative figure is shown.

## Smoothness test for the h/p decision

After Mavriplis, as recalled, the per-degree modal content is fitted by an
exponential decay. Let page-local $\hat a^{(\ell)}_K=\big(\sum_{l\in d_\ell}(\hat u^{(l)}_K)^2\big)^{1/2}$
be the norm of the modal coefficients of total degree $\ell$. Then

$$\hat a^{(\ell)}_K\simeq C\,e^{-\varrho_K\ell},\qquad \ell=1,\dots,N_K,$$

with $C$ and the decay rate $\varrho_K$ (page-local) from a least-squares
fit of $\ln\hat a^{(\ell)}_K$ (Eqs. (36)–(37)). The mean ($\ell=0$) is
excluded because it "can severely bias the decay rate". An element with
$\varrho_K>1$ counts as smooth and is p-enriched; otherwise it is
h-refined. The fit needs $N_K\ge2$, so elements of degree 1 are marked
smooth by fiat and always p-enriched (§4.2, §4.4).

The test belongs to the modal-decay family of the Persson–Peraire
indicator ([troubled-cell indicator](/definitions/troubled-cell-indicator.md)),
used here for the h/p choice and not for limiting. Its "smoothness
indicator" has the opposite sense to the WENO
[smoothness indicator](/definitions/smoothness-indicator.md) $\beta_k$:
a large $\varrho_K$ means smooth. Basile et al. state that a different,
shock-suited indicator will be needed for strong discontinuities (§4.2).

The decay model differs between sources. Basile et al. fit an
exponential decay in the degree $\ell$. [Yu & Hesthaven (2022)](/sources/yu-2022.md)
use the algebraic model of Klöckner, Warburton & Hesthaven,
$\lvert\hat u_\ell\rvert\simeq C\,\ell^{-\mathfrak a_K}$ with page-local
decay exponent $\mathfrak a_K$ (the symbol of the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) page), as the sensor of their
[artificial viscosity](/methods/artificial-viscosity.md), and recall
that the same decay rate serves as smoothness indicator in hp-adaptive
DG (§4.1, their ref. [59]). The two models are different conventions, not
competing claims: neither source compares them.

## Adaptation with shocks and interfaces

[Bai & Li (2022)](/sources/bai-2022.md) use h-refinement only, on a
quadtree-like multi-level Cartesian mesh after Berger–Oliger and
Berger–Colella, for a sharp-interface DG solver of compressible two-phase
flows with shocks. Cells are refined by their distance from the level-set
interface or by the magnitude of the pressure gradient, and coarse and
fine levels exchange data conservatively by $L^2$ projections, following
their earlier DG cut-cell work (§2, solution procedure §2.6). Their space–time diagrams of
the air–helium shock–bubble interaction converge over four AMR grid
configurations (two to four levels), and the underwater explosion runs on a $160\times160$ base mesh
with three levels where the reference uses $1200\times1200$ cells
(§3.4, §3.6; [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md),
[underwater explosion](/benchmarks/underwater-explosion.md)). The
block-structured finite-volume counterpart is on
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

## p-adaptation with finite-volume subcells on a static mesh

[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) call their scheme
"hp-adaptive", but the DG mesh never changes at run time: it "comes
without the need for mesh adaptation during the run time" (§1, §4). The
"p" is a variable element-local degree $N\in[N_{\min},N_{\max}]$ of the
Gauss-node [DGSEM](/methods/dgsem.md) of [FLEXI](/software/flexi.md) in
smooth regions. The "h" is the switch of a whole troubled element to a
second-order TVD finite-volume scheme on $N_{\mathrm{FV}}^d$ equidistant
subcells of the reference element, with $N_{\mathrm{FV}}$ (page-local,
subcells per direction) chosen independently of $N$. The method is
therefore a variant of [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)
combined with p-adaptation, not mesh refinement in the sense of Basile et
al. or Bai & Li: the element is either pure DG or pure finite volume, with
no convex blending ($\alpha\in\{0,1\}$ in the registry's terms). The
authors motivate the split by the finding of Li and Jameson, as they
recall it, that h-refinement is better at discontinuities and
p-refinement more efficient in smooth regions (§1).

**Coupling of different degrees** (§3.3, Eqs. (14)–(17)). At a face
between degrees $N<M$ (page-local $M$), the lower-degree trace is
interpolated to the $M+1$ nodes of the higher degree, the Riemann solver
is evaluated there, and the flux is brought back to degree $N$ by a
Legendre modal cut-off: nodal values to modal coefficients by a
Vandermonde matrix, truncation to the first $N+1$ modes, back to nodal
values. Any distribution of degrees between neighbours is admissible. The
authors call the modal-truncation projection "conservative". It keeps the
reference-space mean; whether it conserves $\int Ju\,d\xi$ on curved
elements, where $J$ varies, is not discussed *(compiler check, not in
the sources)*.

**Subcell resolution and time step** (§4.3, Eqs. (18), (31)). The DG
step is $\Delta t=\nu\,\alpha_{\mathrm{RK}}(N)\,\Delta x_{\mathrm{DG}}/\big((2N+1)a\big)$
and the subcell step $\Delta t=\nu\,\alpha_{\mathrm{RK}}(0)\,\Delta x_{\mathrm{FV}}/a$,
with page-local Runge–Kutta factor $\alpha_{\mathrm{RK}}>1$, element and
subcell sizes $\Delta x_{\mathrm{DG}}$, $\Delta x_{\mathrm{FV}}=\Delta x_{\mathrm{DG}}/N_{\mathrm{FV}}$
CFL number $\nu$ and maximum signal speed $a$. Following Dumbser et al.,
as recalled, subcells do not tighten the time step up to
$N_{\mathrm{FV}}=2N+1$. Equating the two bounds and ignoring the
difference between $\alpha_{\mathrm{RK}}(N)$ and $\alpha_{\mathrm{RK}}(0)$
gives exactly this value *(compiler check, not in the sources)*. The
hp setups use one global $N_{\mathrm{FV}}=2N_{\max}+1$, against
$N_{\mathrm{FV}}=N+1$ in the earlier FLEXI subcell scheme of Sonntag and
Munz. The step counts confirm it: 4695/4726/4765 (double Mach
reflection), 19 969/19 136/19 993 (forward-facing step) and 235/241/248
(3D explosion) for static, p-adaptive and hp-adaptive runs (Tables 3, 4,
6).

**Transfer operators** (§4.3, Eqs. (27)–(30)). DG to subcells is the
subcell integral mean, evaluated by the DG quadrature mapped to each
subinterval; subcells back to DG is the pseudo-inverse, a constrained
least-squares fit with conservation of the element integral as
constraint, after Dumbser and Zanotti, so that the two operators compose
to the identity on the DG space. Subcell metric terms are the subcell
means of $J$ and $Ja^{(d)}$, the same operator applied to the DG metrics
(Eqs. (19)–(21); [free-stream preservation](/properties/free-stream-preservation.md)).

**One indicator for both decisions** (§5, §7.3, Eqs. (32)–(38)). The
indicator is the Mavriplis modal decay rate, as recalled: the relative
energy of the modes of order $m$ in reference direction $d$, summed over
the other two directions and normalized by the total, is fitted to
$a\,e^{-\varrho^{(d)}_Km}$ (page-local amplitude $a$), and the indicator is
$\min_d\lvert\varrho^{(d)}_K\rvert$, evaluated on one scalar (density or
pressure, per test). The fitting procedure, including which modes enter,
is not specified. Four thresholds per degree, ordered
$FV^N_{\mathrm{lower}}<FV^N_{\mathrm{upper}}<DG^N_{\mathrm{refine}}<DG^N_{\mathrm{coarse}}$
(page-local), act as follows:

| indicator of a DG element | action |
|---|---|
| above $DG^N_{\mathrm{coarse}}$ | lower $N$ by one if $N>N_{\min}$ (over-resolved) |
| between $DG^N_{\mathrm{refine}}$ and $DG^N_{\mathrm{coarse}}$ | keep $N$ |
| between $FV^N_{\mathrm{lower}}$ and $DG^N_{\mathrm{refine}}$ | raise $N$ by one if $N<N_{\max}$ |
| below $FV^N_{\mathrm{lower}}$ | switch to finite-volume subcells |

A finite-volume element returns to DG when the indicator, computed on its
least-squares DG polynomial, exceeds $FV^N_{\mathrm{upper}}$; the band
between the two FV thresholds is a hysteresis that prevents repeated
switching. Thresholds are linear in $N$, which leaves four free
parameters, the $FV_{\mathrm{lower}}$ and $DG_{\mathrm{refine}}$ values at
$N_{\min}$ and $N_{\max}$, tuned per test case: e.g. $[3.5,5.0]$ and
$[2.4,3.3]$ for Sod, $[5.6,6.5]$ and $[3.2,4.1]$ for the double Mach
reflection. The decay rate here is fitted to squared coefficients and per
direction, Basile et al.'s to coefficient norms by total degree with the
mean excluded, so the numerical thresholds of the two papers are not
comparable *(compiler check, not in the sources: an amplitude decay
$e^{-\varrho\ell}$ gives an energy decay $e^{-2\varrho\ell}$)*. The
indicator is recorded on [troubled-cell indicator](/definitions/troubled-cell-indicator.md).

**When the decisions are taken** (§7.2). Degrees change only at the start
of a time step, after which the indicator is recomputed for the new
degree and DG/FV switching applied. After each Runge–Kutta stage only the
switch from DG to finite volumes is checked; the reverse switch and
degree changes inside a step "could violate the time step restriction".

**Implementation** (§6). To keep FLEXI's static arrays, the solution,
face and flux arrays of every degree in $[N_{\min},N_{\max}]$ and the
subcell arrays are allocated for every element at start-up, and metric
terms are precomputed for all degrees and for the subcells. Memory grows
by about 20 % (p-adaptive) and a factor 4 (hp-adaptive), dominated by the
metric terms (§6, §8.6). Load balancing is not addressed; all adaptive
runs are single-core (§8.3, §9).

**Evidence** (§8, Euler, $\gamma=1.4$). Three setups are compared:
static ($N$ fixed, $N_{\mathrm{FV}}=N+1$, the open-source FLEXI),
p-adaptive ($N_{\mathrm{FV}}=N_{\max}+1$) and hp-adaptive
($N_{\mathrm{FV}}=2N_{\max}+1$).

| test | DOFs per element (static/p/hp) | wall time, s (static/p/hp) |
|---|---|---|
| [Double Mach reflection](/benchmarks/double-mach-reflection.md), $240\times60$, $N\in[2,5]$ | 216 / 35 / 54 | 15 578 / 3856 / 6569 |
| [Forward-facing step](/benchmarks/forward-facing-step.md), Mach 3 | 216 / 44 / 82 | 65 782 / 19 774 / 40 217 |
| 3D spherical explosion, $50^3$ | 216 / 56 / 141 | 10 839 / 3557 / 8601 |

The authors state speedups of "a factor 4" and "almost a factor 2.5"
(double Mach reflection), "almost a factor 3" and "about 1.6"
(forward-facing step), and three and 25 % (3D explosion) for the p- and
hp-adaptive setups; the table ratios are 4.04, 2.37, 3.33, 1.64, 3.05 and
1.26 *(compiler check, not in the sources)*, with equal or sharper shocks; in the 3D case almost
8 % of the elements are finite-volume limited, which cuts the hp gain
(Tables 3, 4, 6). On the [Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md)
the adaptive run uses 151.6 against 216 DOFs per element and resolves the
shock more sharply, on the [Shu–Osher problem](/benchmarks/shu-osher-problem.md)
70.8 against 216 with a better match behind the shock (§8.4–8.5). Mixed
degrees converge at the order $N_{\min}+1$ of the lowest degree present
(checkerboard $N_{\max}=6$, $N_{\min}=2$–$5$, Table 2), and the cost per
degree of freedom and time step is at most about 15 % above FLEXI for a
half–half split of degrees and up to 80 % for a checkerboard (Fig. 7).
The DG/FV interfaces emit acoustic waves, strongest for
$N_{\mathrm{FV}}=N+1$, which $N_{\mathrm{FV}}=2N+1$ "almost completely
avoids" (§8.6–8.7, schlieren images).

## Static local p-refinement

[Kou et al. (2022)](/sources/kou-2022.md) use a fixed, geometry-based
p-refinement of [flux reconstruction](/methods/flux-reconstruction.md)
near an immersed wall: degree 1 in the far field, 2 in a buffer and 3 in
cells whose centre lies within a quarter of the cylinder diameter of its surface, with
mortar elements at faces between degrees, on which the common and
interaction fluxes are computed and projected back (§5.2). On the
cylinder at $\mathrm{Re}=40$ this reproduces the uniform degree-3 result
with 148 296 against 532 576 degrees of freedom, 28 % (Fig. 14); solution-adaptive
p-adaptation is left to future work ([immersed-boundary methods](/methods/immersed-boundary-method.md)).

## Entropy-stable transfer between degrees

Transferring a solution between degrees by interpolation or $L^2$
projection can create entropy.
[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) pose
$p$-refinement and $p$-coarsening as convex problems: find the state of the
target space closest (in its mass-matrix norm) to the interpolant, subject
to conservation and to a total entropy no larger than before (App. A.1,
Eqs. (47)–(50)). The first-order condition makes the solution the
interpolant plus a non-negative multiple of the mean-free entropy
variables, the same structure as an
[entropy correction term](/methods/entropy-correction-term.md) (Eq.
(48)). On a 1D test with LGL nodes, degree $\le6$ (fine) and $\le3$
(coarse) and entropy $e^u$, interpolation creates entropy
$3.566\times10^{-3}$ on refinement and $9.749\times10^{-2}$ on coarsening
($7.767\times10^{-2}$ for $L^2$ projection), while the optimization
changes it by $-3.980\times10^{-8}$ and $-3.429\times10^{-7}$ (Fig. 9),
solved with Ipopt. The test is an isolated transfer, not an adaptive run.

## Size and degree prescription

With the error model $\mathsf E_K\simeq Ch_K^{\mathsf r_K}$ (page-local
size $h_K$ and rate $\mathsf r_K$), the new size is (Eqs. (38)–(40))

$$h^*_K=h_K\Big(\frac{\mathsf E^*}{\mathsf E_K}\Big)^{1/\mathsf r_K},\qquad \mathsf r_K=\begin{cases}N_K+1&\text{smooth},\\ 1&\text{non-smooth},\end{cases}$$

with $\mathsf r_K=N_K+1$ the DG $L^2$ rate. Sizes are averaged to the mesh
nodes, may shrink by at most a factor 2 per step, and stay unchanged where
$\mathsf E\le\mathsf E^*$. The nodal size map is passed to MMG as an
isotropic metric $h^{-2}I$, and the solution is moved to the new mesh by
$L^2$ projection (§3, §4.3). In hp mode, p-marked elements raise their
degree by one up to $N_{\max}=3$, and the nodal averages use only the
elements that are not p-marked. Degrees move to the new mesh by
nearest-neighbour assignment (§4.4, Fig. 1).

**Target error.** Classical fixed-fraction marking performs poorly with
magnitude-dependent sizing, according to the authors (no figure). They
choose instead the target $\mathsf E^*$ for which the predicted number of
degrees of freedom grows by a fixed factor $\mathsf g$ (page-local),
$\sum_KN_p(N^*_K)\,(h_K/h^*_K)^d=\mathsf g\cdot\mathrm{NDOF}_i$, solved by
bisection (Eqs. (47)–(49)). The default is $\mathsf g=1.5$.

Boundary-layer prisms, and for the jet the tetrahedra inside the nozzle,
are frozen during remeshing; they can still be p-enriched, then without
the smoothness test (§4.6).

## Evidence

All tests are steady, subsonic and shock-free (§5–6).

| test | setting | result |
|---|---|---|
| 2D NACA0012 | $M_\infty=0.5$, $\alpha=1°$, $Re=5000$ | four adaptation steps beat the finest uniform mesh in drag error for $N=1,2,3$; hp reaches it with the fewest degrees of freedom; final drag and lift errors about two orders below uniform refinement |
| 3D sphere | $Re=200$ | $h$-adaptation at $N=1$ saves about a factor 10 in degrees of freedom; hp fastest in the first steps |
| 3D delta wing | $M=0.3$, $\alpha=12.5°$, $Re=4000$ | hp fastest early, then coincides with $h$ at $N=2$; elements at the geometric singularity stay at $N=2$ until it is resolved |
| PPRIME jet, RANS–SA | $M_j=0.9$, $Re_D\simeq10^6$ | hp results at 7–15 M degrees of freedom agree better with LES and experiment than a 48 M-element second-order structured finite-volume RANS |

The growth factor study on NACA0012 ($\mathsf g$ from 1.2 to 2) shows that
all values converge, with smaller $\mathsf g$ needing fewer degrees of
freedom but more steps (Fig. 7). The authors also state that raising the
degree progressively from $N=1$ helps the robustness of the implicit
solver on stiff problems (§5.2, §6.2); no failing alternative is shown.

## Qualifications

- No CPU-time comparison of hp against h-adaptation is given, because a
  fair one would need load balancing and optimized implicit solvers
  (§5.2). The jet comparison with finite volumes counts degrees of
  freedom only.
- Basile et al.'s method has not been tried on flows with shocks; the
  authors defer them (§4.2). Bai & Li's refinement handles shocks but is
  h-only and uses geometric and pressure-gradient criteria, not an error
  estimator.
- "hp" means different things in the sources. In Basile et al. it is
  mesh refinement plus degree enrichment; in Mossier et al. it is degree
  adaptation plus whole-element switching to finite-volume subcells on a
  fixed mesh (§1, §4). The two are kept apart on this page; neither
  source compares with the other's strategy.
- Mossier et al.'s comparisons are single-core, except the static airfoil
  run on 32 cores; there the adaptive runs need about 2.9 times fewer time
  steps, but 2.4–2.7 times the wall time of the 32-core run (Table 5),
  which the text gives as "about 3 times" *(compiler check, not in the sources: ratios of the printed Table 5 values)*. Their thresholds are tuned per
  test, and their statement "about 25% less DOFs" on Sod corresponds to
  $1-151.6/216=30$ % (§8.4) *(compiler check, not in the sources)*.
- Mossier et al. print the linear threshold law (37)–(38) with $N$ where
  linear interpolation between $N_{\min}$ and $N_{\max}$ needs $N-N_{\min}$;
  as printed it reproduces the end values only for $N_{\min}=0$
  *(compiler check, not in the sources)*. One bullet of §7.3 names
  $FV^N_{\mathrm{lower}}$ as the switch-back threshold where the other
  bullet and Fig. 4 use $FV^N_{\mathrm{upper}}$, which is meant. How
  $DG^N_{\mathrm{coarse}}$ is set is not stated.
- Eq. (43) prints the new degree as $\max(N_K+1,N_{\max})$. The text and
  Algorithm 2 increase the degree by one with the cap $N_{\max}$, which is
  $\min$.

# Citations

- [Basile et al. (2022)](/sources/basile-2022.md) — §1, §2.3 Eqs. (15)–(23), §3, §4.1–4.6 Eqs. (28)–(49), Fig. 1, Algorithms 1–2, §5.1–5.3 Figs. 3–14, §6 Figs. 16–20 (author manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.6, §3.4, §3.6.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §4.1.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — App. A.1 Eqs. (47)–(50), Fig. 9 (arXiv v4).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1, §3.3 Eqs. (14)–(18), §4.1–4.3 Eqs. (19)–(31), §5 Eqs. (32)–(36), §6, §7.2–7.3 Eqs. (37)–(38) Figs. 3–4, §8.2–8.9 Tables 2–6, Fig. 7, §9.
- [Kou et al. (2022)](/sources/kou-2022.md) — §5.2, Fig. 14.
