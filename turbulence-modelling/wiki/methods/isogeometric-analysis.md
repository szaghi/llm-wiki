---
type: Method
title: "Isogeometric analysis and isogeometric discontinuous Galerkin"
description: "Isogeometric analysis uses the CAD bases (B-splines, NURBS) both for the geometry and for the solution; the page gives the basis, knot insertion and Bézier extraction, an isogeometric DG with CAD-exact anisotropic h-adaptation for compressible RANS, and continuous NURBS discretizations of variational-multiscale LES."
status: established
aliases: [IGA, isogeometric discontinuous Galerkin, NURBS-based DG, NURBS-DG, isogeometric DG, spline-based discretization, NURBS elements, Bézier extraction]
tags: [dg, mesh-adaptation, rans, les, high-order]
timestamp: 2026-10-29T05:08:00Z
---

# Isogeometric analysis and isogeometric discontinuous Galerkin

**Isogeometric analysis (IGA)** takes the functions of computer-aided
design, B-splines and non-uniform rational B-splines (NURBS), both to
describe the geometry and to span the approximate solution space, so that
the discrete domain is the CAD domain at every refinement level
([Bulgarini et al. 2025b](/sources/bulgarini-2025-b.md), §1, citing Hughes
et al.). Two kinds of isogeometric discretization appear in the bundle: a
**discontinuous** one, in which a NURBS patch is split into rational Bézier
elements that serve as the elements of a
[discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
method (Bulgarini et al. 2025b, steady compressible RANS with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md)), and a
**continuous** one, in which $C^{N-1}$ NURBS of degree $N$ carry an
incompressible [variational-multiscale](/methods/variational-multiscale-method.md)
LES ([Sun et al. 2026](/sources/sun-2026.md)). Bulgarini et al. (§1) state
that IGA has been used mainly in structural mechanics, "with limited
applications in CFD"; Sun et al. (§1) state, citing Evans and co-workers,
that spline bases "enjoy superior dispersion and dissipation
characteristics, especially for large wavenumbers" compared with
low-order bases and that IGA offers "a seamless means of handling complex
geometries".

Page-local symbols: $\boldsymbol\Xi=[\xi_1,\dots,\xi_m]$ the knot vector
(open: end knots repeated $N+1$ times); $B_i^N$ the B-spline basis
function of degree $N$ (the registry's polynomial degree; the sources'
$p$ in Bulgarini et al. and $k$ in Sun et al.); $W_i$ the NURBS weights
(not quadrature weights, which keep the registry's $w_i$); $R_i^N$ the
NURBS basis; $\boldsymbol P_i$ the control points; $(\xi,\eta)$ the
parametric coordinates ($\eta$ is not the Kolmogorov length here); $I_K^{\mathrm{SSED}}$, $I_K^{\mathrm{SD}}$,
$I_K^{\mathrm{LNC}}$, $I_K^{\mathrm{GNC}}$ the refinement indicators of
element $K$ (the source's $\eta_J$; $\eta$ is the Kolmogorov length in the
registry); $f_{\mathrm{ref}}$ the percentage of elements flagged for
refinement per cycle (the source's $ne^{adp}$).

## Basis, knot insertion and Bézier extraction

Bulgarini et al. (2025b, §2, Eqs. 1–7) cite Piegl & Tiller and Hughes et
al. for the B-spline basis, which follows the Cox–de Boor recursion
$$B_i^0(\xi)=\begin{cases}1,&\xi_i\le\xi<\xi_{i+1},\\0,&\text{otherwise},\end{cases}\qquad
B_i^N(\xi)=\frac{\xi-\xi_i}{\xi_{i+N}-\xi_i}B_i^{N-1}(\xi)+\frac{\xi_{i+N+1}-\xi}{\xi_{i+N+1}-\xi_{i+1}}B_{i+1}^{N-1}(\xi),$$
with $0/0:=0$, and the NURBS basis and curve are
$$R_i^N(\xi)=\frac{W_iB_i^N(\xi)}{\sum_jW_jB_j^N(\xi)},\qquad \boldsymbol C(\xi)=\sum_iR_i^N(\xi)\,\boldsymbol P_i,$$
with surfaces by tensor product. **Knot insertion** adds a knot
$\bar\xi\in[\xi_k,\xi_{k+1})$ and replaces the control points by
$\bar{\boldsymbol P}_i=(1-\alpha^{\mathrm{ki}}_i)\boldsymbol P_{i-1}+\alpha^{\mathrm{ki}}_i\boldsymbol P_i$,
with $\alpha^{\mathrm{ki}}_i=1$ for $i\le k-N$,
$(\bar\xi-\xi_i)/(\xi_{i+N}-\xi_i)$ for $k-N+1\le i\le k$, and 0 for
$i\ge k+1$ (page-local $\alpha^{\mathrm{ki}}_i$, not the DG/FV blending
factor $\alpha$); the geometry does not change, and inserting an existing
knot of multiplicity $r$ lowers the continuity there from $C^{N-r}$ to
$C^{N-r-1}$. **Bézier extraction** raises the multiplicity of every
interior knot to $N$, which turns each knot span into a rational Bézier
element of degree $N$ (their Fig. 3: five NURBS basis functions become
nine Bézier functions), the form in which a continuous patch can carry a
discontinuous Galerkin method (§2.3).

## Isogeometric DG with CAD-exact $h$-adaptation

**Discretization** (Bulgarini et al. 2025b, §3). The rational Bézier
basis of each element is the geometry map and the DG trial and test space,
$U_h|_{\Omega_j}=\sum_iU_i(t)R_i^N(\boldsymbol x)$ (Eq. 23), following the
"fully isogeometric" route of Duvigneau et al., which they prefer to the
NURBS–DG couplings of Sevilla et al. and Silveira et al., whose mapping for
spatial integration "could be considered excessive" (§1). Integrals are
taken in parametric space through the Jacobian of the NURBS map (Eq. 26),
with Gauss–Legendre quadrature of at least $(N+1)^d$ points in $d$
dimensions; on a highly curved $N=5$ element of aspect ratio about
$6\times10^5$, thickness $10^{-6}$–$10^{-7}$ and curvature 6000 (mesh
units), representative of boundary-layer elements, this rule integrates
non-polynomial functions accurately (§3.3, Figs. 5–6). The rest is the
Brescia DG lineage: Roe flux, BR2 viscous flux, the pressure-gradient-directed
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md) of
Bassi et al. with constant 0.2, the negative-$\tilde\nu$ modification of
Spalart–Allmaras by Crivellini et al. ($r$ clipped at $10^3$,
$\tilde\nu_\infty=10^{-3}\nu_\infty$; see the SA page), and implicit
backward Euler with pseudo-transient continuation, FGMRES and
block-Jacobi/BILU(0) preconditioning (Eqs. 13–35). Because the control
points do not interpolate the element borders, the element size of the
artificial viscosity is taken as the minimum distance between element
corners, after Duvigneau, instead of Bassi et al.'s
$1/\sqrt{1/\Delta x^2+1/\Delta y^2}$, which is "not a suitable option for
a Bézier patch" (§3.4). The conservative unknown of the SA equation is
$\tilde\nu$, not $\rho\tilde\nu$ (Eq. 17).

**Adaptation by knot insertion** (§4). Each initial element is the root
of a quad-tree; isotropic refinement splits it into four sons, anisotropic
into two, by inserting knots at $\xi=0.5$ and/or $\eta=0.5$ of the father;
a face may touch at most two elements of the other side. Refinement
applies the same knot insertion to the solution coefficients, so the
transfer is exact; coarsening uses a least-squares projection plus a
correction that restores the integral of the solution (Eqs. 36–38), and
loses information, an effect the authors call negligible because they
adapt converged steady solutions (§4.1–4.2). Non-conforming faces are
integrated with the quadrature points of the smaller element. Four
indicators are compared (§4.2, Eqs. 39–43), with $(\cdot)_{h,N-1}$ the
projection on degree $N-1$ and $\rho\boldsymbol u$ the momentum:
$$I_K^{\mathrm{SSED}}=\Big(\frac{\|(\rho\boldsymbol u)_{h,N}-(\rho\boldsymbol u)_{h,N-1}\|_{L^2(K)}}{|K|}\Big)^{1/2},\qquad
I_K^{\mathrm{SD}}=\frac{\|(\rho\boldsymbol u)_{h,N}-(\rho\boldsymbol u)_{h,N-1}\|_{L^2(K)}}{\|(\rho\boldsymbol u)_{h,N}\|_{L^2(K)}},$$
the small-scale energy density (normalized by the element size, because
the unnormalized form "shows poor results if the mesh presents a large
variation in element size") and the spectral decay; and the local and
global non-conformity, the maximum and the sum over the faces and face
quadrature points of the normalized momentum jump
$\|(\rho\boldsymbol u)^+-(\rho\boldsymbol u)^-\|/\|(\rho\boldsymbol u)^++(\rho\boldsymbol u)^-\|$.
The top $f_{\mathrm{ref}}$ per cent of elements are refined per cycle.
The direction comes from a new anisotropy test (Eqs. 44–45, Algorithm 1):
the Jacobian-weighted element average of the velocity gradient is mapped
to parametric space with the averaged inverse Jacobian, and the element
is split along $\xi$ if that component exceeds three times the $\eta$
component, along $\eta$ in the reverse case, isotropically otherwise
(which velocity component, or combination, enters is not stated). See
[mesh adaptation](/methods/mesh-adaptation.md).

**Results** (§4.3, §5, §6):

- **Laminar cylinder** at $M=0.1$, $Re=40$ (adaptation from $N=3$, four
  cycles, $f_{\mathrm{ref}}=25\%$): all four indicators mark the separation
  and recirculation edges and give "a computational speed-up of ≈ 2 times"
  against a fine reference (4608 elements, $N=3$, 73,728 degrees of
  freedom, $C_D=1.41764$); spectral decay is "the most effective overall",
  the small-scale energy density over-refines the detachment region, and
  anisotropic refinement beats isotropic (Figs. 9–10; see
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).
- **Curved against straight boundaries.** On the inviscid Ringleb flow
  ($N=1$–5) linear-boundary meshes develop spurious shocks in the
  recompression region (Figs. 11–12); at about equal degrees of freedom,
  straight boundaries prevent full convergence of the transonic
  [NACA 0012](/benchmarks/naca-0012-airfoil.md) and distort $C_p$ and
  $C_f$ near its leading edge, and on the T106A cascade force a smaller
  CFL-law exponent (Figs. 19, 23).
- **Turbulent flat plate** ($M=0.2$, $Re=1.1\times10^7$): adaptation from
  1152 patches at first-element $y_1^+=100$ to 1834 patches at
  $y_1^+\approx1$ matches the law of the wall and the Wieghardt data with
  about 60% fewer degrees of freedom and less computing time than a
  4617-element reference mesh at $y_1^+=1$ (§6.1, Fig. 15; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
- **Transonic NACA 0012** ($M_\infty=0.751$, $Re=3.91\times10^6$,
  $\alpha=1.99^\circ$; Table 2): with $f_{\mathrm{ref}}=6\%$, 12% and 20%
  the adapted runs reach 46,528, 81,232 and 132,928 degrees of freedom at
  speed-ups of about 5.9, 2.9 and 2.7 and drag deviations of 0.34%, 1.90%
  and 1.88% from the fine-mesh $C_D=1.80200\times10^{-2}$; the coarse
  starting mesh gives a skin friction the authors call "completely wrong".
- **T106A cascade** ($M_{2}=0.59$, $Re=1.1\times10^6$; Table 4): speed-ups
  of about 2.6, 1.7 and 1.5 for $f_{\mathrm{ref}}=5\%$, 10% and 15%, with
  loss-coefficient deviations of 0.17%, 1.49% and 0.24% from
  $\zeta_{\mathrm L,\mathrm{ref}}=2.417\times10^{-2}$ (page-local $\zeta_{\mathrm L}$ the
  total-pressure loss coefficient; see
  [turbine cascades](/benchmarks/turbine-cascade.md)).

The authors conclude that spectral decay "emerges as the best" indicator
and that the anisotropic strategy gives "up to ≈ 6× speed-up with respect
to the standard non-refined meshes" (§7). The same group's
[$p$-multigrid modal DG](/methods/discontinuous-galerkin-spectral-element-method.md)
of [Bulgarini et al. (2025)](/sources/bulgarini-2025.md) uses the same
lineage (BR2, Bassi et al.'s artificial viscosity, but an exact-Riemann
inviscid flux in place of Roe's) on a polynomial, not isogeometric, basis.

**Indicator rankings in two regimes.** Bulgarini et al. (2025b) cite
[Ims & Wang (2023)](/sources/ims-2023.md) for the cylinder case (§1).
Ims & Wang, adapting flux-reconstruction implicit LES of turbine cascades,
find the small-scale-energy and unsteady-residual indicators converging
fastest, judged visually (see [flux reconstruction](/methods/flux-reconstruction.md));
Bulgarini et al., adapting converged steady laminar and RANS solutions,
find spectral decay best and the size-normalized small-scale energy
density over-refining. The two studies use different flows, solvers,
normalizations of the small-scale energy and criteria of convergence.

## Continuous NURBS in variational-multiscale LES

Sun et al. (2026) discretize the incompressible Navier–Stokes equations
with equal-order NURBS of degree $N=2$, 3 or 4 and continuity $C^{N-1}$
for velocity and pressure, stabilized by a residual-based
[variational multiscale](/methods/variational-multiscale-method.md) model
that they derive on each stage of a half-explicit Runge–Kutta step (the
model, its mesh-independent parameter and its LES results are on the VMS
page). The spline-specific points:

- **Spatial order** (§7.1, Fig. 6). On a manufactured solution with
  $C^1$ quadratic and $C^2$ cubic NURBS, velocity and pressure converge at
  order three and four in $L^2$ and two and three in $H^1$, i.e. $N+1$ and
  $N$, which the authors call "higher than those from the error analysis
  for the Darcy equations" that govern each stage; temporal orders 1–4 are
  verified on $80\times80\times4$ $C^3$ quartic elements (Fig. 7; see
  [method of manufactured solutions](/methods/method-of-manufactured-solutions.md)).
- **Fourier analysis** (§5, App. B). The one-dimensional advection–diffusion
  analysis uses $C^1$ quadratic B-splines on a uniform mesh, which give a
  five-point stencil; it compares the stage-wise ("Rothe") VMS with the
  semi-discrete VMS of the vertical method of lines; see
  [eigensolution analysis](/methods/eigensolution-analysis.md).
- **Linear algebra** (§6–7.1). Because each stage operator is linear and
  scales only through the time step and the stage coefficient, one
  constant symmetric matrix is assembled once; with identical Dirichlet
  conditions on all velocity components the Kronecker structure of its
  velocity block cuts matrix storage by 45%, against about 20% without it,
  relative to their fully implicit reference.
- **Turbulence test.** The [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  at $Re=1600$ runs on $C^1$ quadratic NURBS on $64^3$, $96^3$ and $128^3$
  elements against a $512^3$ pseudo-spectral DNS (§7.2); results on the VMS page.

## Qualifications

- **Scope.** Bulgarini et al. (2025b) are two-dimensional and steady
  (laminar and RANS); Sun et al. (2026) are three-dimensional,
  incompressible and continuous, on Cartesian-like NURBS meshes. Neither
  paper runs an isogeometric discretization on a complex three-dimensional
  CAD geometry, and Sun et al. state the geometric advantage of IGA from
  the cited literature only.
- **Degrees in the adaptation table.** Bulgarini et al. (2025b, Table 5)
  list the degree used to drive adaptation as $N=1$ for the flat plate and
  $N=2$ for the NACA 0012, while the captions of Figs. 15–18 state
  "$\mathbb P^3$ solution approximation" for the same cases; the paper does
  not say whether the two degrees differ.
- **Printed slips (Bulgarini et al. 2025b).** §4.2 calls the global
  non-conformity indicator "the $L^2$ norm of all the jumps", while Eq. (43)
  is a plain sum of normalized jump norms; the energy equation of Eq. (8)
  prints the viscous work with $(\nabla\boldsymbol u-\nabla\boldsymbol u^{\mathsf T})$,
  while the momentum equation and the flux of Eq. (19) use the symmetric
  combination, and prints the heat flux outside the divergence; Eq. (36)
  sums the father expansion over "the number of quadrature points"; the
  Table 3 caption names degrees of freedom for a column of elements. The
  CFL-law constants and the coarsening threshold are not printed.
- **Printed slips (Sun et al. 2026).** The same family is named
  RK($s,p$)-VMS (§5), HERK($s,p$)-VMS (§7) and "RK-VMS(3, 3)" (p. 17);
  Eq. (3.5) sums over $i$ with stage arguments indexed $j$. The
  supplementary material (stencils, further spectra) was not available.

# Citations

- [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md) — §1 (IGA, NURBS–DG lineage, Duvigneau et al.); §2, Eqs. (1)–(7), Fig. 3 (B-splines, NURBS, knot insertion, Bézier extraction); §3, Eqs. (8)–(35), Figs. 4–6 (RANS–SA isogeometric DG, quadrature, artificial viscosity on Bézier patches, implicit solver); §4, Eqs. (36)–(45), Algorithm 1, Figs. 9–10 (quad-tree knot-insertion adaptation, indicators, anisotropy); §5, Figs. 11–14 (Ringleb, flat plates); §6, Tables 1–5, Figs. 15–23 (adaptive plate, NACA 0012, T106A); §7.
- [Sun et al. (2026)](/sources/sun-2026.md) — §1 (spline bases and IGA for LES, as cited); §5, App. B (Fourier analysis with $C^1$ quadratic B-splines); §6 (constant stage matrix); §7.1, Figs. 6–9 (spatial and temporal orders, storage); §7.2 (Taylor–Green vortex on NURBS).
- [Bulgarini et al. (2025)](/sources/bulgarini-2025.md) — §3 (the same group's polynomial modal DG, for contrast).
- [Ims & Wang (2023)](/sources/ims-2023.md) — §3.1, §5 (indicator ranking in adaptive FR implicit LES, cited by Bulgarini et al.).
