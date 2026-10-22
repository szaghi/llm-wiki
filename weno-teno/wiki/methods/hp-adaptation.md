---
type: Method
title: "h- and hp-adaptation for DG"
description: "Solution-adaptive DG refines the mesh (h) or raises the polynomial degree (p) where an error estimator is large; Basile et al. give an hp loop with a modal-decay smoothness test on steady shock-free flows, Bai and Li a quadtree h-refinement with shocks and interfaces, and Abgrall et al. entropy-stable transfer between degrees."
status: established
aliases: [hp-adaptivity, h-adaptation, metric-based mesh adaptation, a posteriori error estimation, SSED estimator]
tags: [dg, amr, entropy-stable, turbulence]
timestamp: 2026-10-22T20:00:00Z
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
- Eq. (43) prints the new degree as $\max(N_K+1,N_{\max})$. The text and
  Algorithm 2 increase the degree by one with the cap $N_{\max}$, which is
  $\min$.

# Citations

- [Basile et al. (2022)](/sources/basile-2022.md) — §1, §2.3 Eqs. (15)–(23), §3, §4.1–4.6 Eqs. (28)–(49), Fig. 1, Algorithms 1–2, §5.1–5.3 Figs. 3–14, §6 Figs. 16–20 (author manuscript).
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.6, §3.4, §3.6.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §4.1.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — App. A.1 Eqs. (47)–(50), Fig. 9 (arXiv v4).
