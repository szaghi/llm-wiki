---
type: Method
title: "Flux reconstruction"
description: "Flux reconstruction (FR/CPR) corrects a degree-N discontinuous flux polynomial per element with Riemann-solver interface corrections; its correction functions recover nodal DG or spectral difference. The page covers formulation, the correction parameter as a filter, nonlinearly stable split-form FR, implicit transitional RANS, fully discrete eigenanalysis, implicit LES, explicit SGS models, stabilization and shock limiting."
status: established
aliases: [FR, flux reconstruction method, correction procedure via reconstruction, CPR, FR/CPR, lifting collocation penalty, Huynh flux reconstruction, ESFR, energy-stable flux reconstruction, VCJH schemes, NSFR, nonlinearly stable flux reconstruction]
tags: [flux-reconstruction, dg, implicit-les, numerical-dissipation, entropy-stable, wmles]
timestamp: 2026-10-29T07:41:00Z
---

# Flux reconstruction

**Flux reconstruction (FR)**, in the form of Huynh, and its variant the
**correction procedure via reconstruction (CPR)** solve the differential
(strong) form of a conservation law
$\partial_tU+\nabla\cdot(F^c(U)-F^v(U,\nabla U))=0$ with a nodal polynomial
of degree $N$ in each element. The flux evaluated at the solution points
gives a *discontinuous* flux polynomial, which a *correction* term makes
continuous in its normal component at the element faces: the correction is
the jump between a common interface flux $f^*$ (from an approximate Riemann
solver) and the discontinuous flux, spread into the element by correction
functions. The choice of correction functions fixes the scheme, and one
choice recovers the nodal [discontinuous Galerkin](/methods/discontinuous-galerkin-spectral-element-method.md)
method, which [Dzanic et al. (2022)](/sources/dzanic-2022.md), §2.2, describe
as FR being "a generalization of the nodal discontinuous Galerkin method".
In the turbulence sources FR runs as [implicit LES](/definitions/implicit-les.md)
or under-resolved DNS ([Dzanic et al. 2022](/sources/dzanic-2022.md);
[Wang 2024](/sources/wang-2024-b.md)), with explicit subgrid models in
[wall-modelled LES](/methods/wall-modelled-les.md)
([Duan & Wang 2024](/sources/duan-2024.md)), and with
[PANS](/methods/partially-averaged-navier-stokes.md) as the hybrid closure
(Dzanic et al. 2022). As a steady RANS solver with laminar–turbulent
transition it runs fully implicitly in [COOLFluiD](/software/coolfluid.md)
([Vandenhoeck et al. 2022](/sources/vandenhoeck-2022.md)). A provably
entropy-stable split-form variant,
nonlinearly stable FR, is assessed as DNS and implicit LES of free-shear
turbulence without any added dissipation by
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md); another choice of
correction functions recovers the
[spectral difference method](/methods/spectral-difference-method.md)
(Brillon & Nadarajah 2026, §1, §3.1.5).

Page-local symbols: $\boldsymbol g_{f,k}$ the correction function of flux
point $k$ on face $f$; $N_{sp}$ the number of solution points of an element;
$\ell_i$ the nodal Lagrange basis; $c_{q,f,l}$ the CPR lifting coefficients
(the source's $\alpha_{q,f,l}$, renamed because $\alpha$ is the DG/FV blending
factor of the registry); $V_e$ the element volume; $c_{\mathrm{FR}}$ the
correction parameter of energy-stable FR (Brillon & Nadarajah's $c$), with
the named values $c_{\mathrm{DG}}=0$, $c_{\mathrm{SD}}$, $c_{\mathrm{HU}}$,
$c_+$; $\mathsf M$, $\mathsf K$ the element mass matrix and the FR
correction operator.

## Formulation

**FR form** (Dzanic et al. 2022, §2.2, Eqs. 18–22; Wang 2024, §2.2,
Eqs. 9–15). In each element, mapped to a reference element, the solution is
$U\approx\sum_{i=1}^{N_{sp}}U_i\,\ell_i(\boldsymbol\xi)$ with
$\ell_i(\boldsymbol\xi_j)=\delta_{ij}$. The flux splits as
$$F=F^D+F^C,\qquad F^D=\sum_{i=1}^{N_{sp}}F(U_i)\,\ell_i(\boldsymbol\xi),\qquad
F^C(\boldsymbol\xi)=\sum_{f}\sum_{k}\Big[(f^*\cdot\boldsymbol n)_{f,k}-(F^D\cdot\boldsymbol n)_{f,k}\Big]\boldsymbol g_{f,k}(\boldsymbol\xi),$$
with the correction functions normalized at the flux points,
$\boldsymbol g_{f,k}\cdot\boldsymbol n_{f_2,k_2}=1$ if $(f,k)=(f_2,k_2)$ and
$0$ otherwise (Wang 2024, Eq. 15). Dzanic et al. (2022, §2.2) add that the
sum of the correction functions lies in the Raviart–Thomas space of order
$N$. The divergence of $F^D$ needs only the derivatives of the Lagrange basis;
that of $F^C$ the divergence of $\boldsymbol g_{f,k}$; FR "solves the
differential form" of the equations (Wang 2024, §2.2).

**CPR form** (Duan & Wang 2024, §3, Eqs. 16–25). The same scheme written at
solution point $q$ of element $k$ as
$$\frac{\partial U_{k,q}}{\partial t}+\Big[\nabla\cdot\hat F^c(U_k)\Big]_q-\Big[\nabla\cdot\hat F^v(U_k,\nabla U_k)\Big]_q+\frac{1}{\mathcal J_{k,q}}\sum_f\sum_l c_{q,f,l}\Big([F^n]_{f,l}-[F^n_v]_{f,l}\Big)A_{f,l}=0,$$
where $\hat F$ are the flux polynomials interpolated from the solution
points, $[F^n]_{f,l}$ and $[F^n_v]_{f,l}$ the jumps between the common and the
interpolated normal fluxes at flux point $l$ of face $f$, $A_{f,l}$ the local
face area, $\mathcal J$ the mapping Jacobian, and the lifting coefficients
$c_{q,f,l}$ depend only on the element shape. Duan & Wang state that the
normal fluxes "must be continuous across element interfaces at the flux
points to ensure conservation".
Ims & Wang (2023, §2, Eqs. 1–6) and Shi & Yan (2023, §II.A, Eqs. 2–5)
print the same CPR form as a correction field $\delta$ of degree $N$ added
to the projection of the flux divergence onto the degree-$N$ space,
$\partial_tU+\Pi_N[\nabla\cdot F]+\delta=0$, with $\delta$ at solution point
$j$ of element $i$ lifted from the face jumps by the shape-dependent
coefficients and the face areas, divided by the element volume ($\Pi_N$
page-local; [Ims & Wang (2023)](/sources/ims-2023.md);
[Shi & Yan (2023)](/sources/shi-2023.md)); Shi & Yan add that FR/CPR
"unifies" DG and spectral difference. Vermeire (2024, §3, Eqs. 6–13) prints
the same lifting-collocation-penalty form for straight-faced elements and
takes the lifting coefficients of the DG-recovering variant (FRDG) from a
weighted-residual identity between the correction field and the face jumps,
which recovers DG for linear equations; other choices of the coefficients
recover energy-stable spectral difference, spectral volume and DG
([Vermeire (2024)](/sources/vermeire-2024.md)). The solution points are Gauss
points, the geometry is mapped with quadratic polynomials (linear for
$N=1$), and cross-product-form metrics are free-stream preserving with Gauss
points and FRDG provided the mapping degree does not exceed $N$ (§3, as
cited; see [geometric conservation law](/properties/geometric-conservation-law.md)).

**One-dimensional correction functions.** Liu & Yuan (2023, §2.1–2.2,
Eqs. 8–21) print Huynh's one-dimensional scheme on the reference element
$[-1,1]$ with degree-$(N+1)$ correction functions
$g_L(\xi)=g_R(-\xi)$, $g_L(-1)=1$, $g_L(1)=0$, in the
Vincent–Castonguay–Jameson–Huynh (VCJH) family
$$g_L=\frac{(-1)^N}{2}\Big[L_N-\frac{c_{\mathrm{FR}}L_{N-1}+L_{N+1}}{1+c_{\mathrm{FR}}}\Big],\qquad
g_R=\frac12\Big[L_N+\frac{c_{\mathrm{FR}}L_{N-1}+L_{N+1}}{1+c_{\mathrm{FR}}}\Big],$$
with $L_N$ the Legendre polynomial of degree $N$ and
$-1<c_{\mathrm{FR}}<\infty$ the correction parameter in Liu & Yuan's
normalization (the source's $\eta$), which affects dispersion and
dissipation, order and CFL limit; $c_{\mathrm{FR}}=c_{\mathrm{DG}}=0$
recovers collocation nodal DG, which they use on Gauss–Legendre solution
points, chosen, after Witherden & Vincent, to minimize aliasing from the
collocated nonlinear flux ([Liu & Yuan (2023)](/sources/liu-2023-b.md);
energy stability for linear fluxes holds for any solution points, as
cited). Tonicello et al. (2023, §2.1, Eqs. 4–11) write the same
one-dimensional scheme for linear advection with an interface flux that
weights the upwind and downwind traces by $1-\alpha_{\mathrm T}$ and
$\alpha_{\mathrm T}$ (page-local, the source's $\alpha$; $\alpha_{\mathrm T}=0$
upwind, 0.5 centred; the upwinding parameter of
[eigensolution analysis](/methods/eigensolution-analysis.md) is
$\lambda_{\mathrm{up}}=1-2\alpha_{\mathrm T}$),
"mimicking" the upwinding of Riemann solvers, and recover DG and spectral
difference only through the correction-function matrices
([Tonicello et al. (2023)](/sources/tonicello-2023.md)). Lv & Ekaterinaris
(2023, §3.3, Eqs. 23–27) write Huynh's one-dimensional scheme on the
reference element $[0,1]$: the discontinuous flux polynomial of degree $N$ is
corrected by $(\hat F(0)-F^D(0))g_L+(\hat F(1)-F^D(1))g_R$ with correction
functions of degree $N+1$ satisfying $g_L(0)=1$, $g_L(1)=0$, $g_R(0)=0$,
$g_R(1)=1$, and they cite energy-stable FR and PyFR as its extensions
([Lv & Ekaterinaris (2023)](/sources/lv-2023.md); see Qualifications for
their printed symmetry relation).

**Node sets.** The sources place the solution points differently: Gauss
points ("usually", Duan & Wang 2024, §3), Legendre–Gauss–Lobatto points for
both solution and flux points so that nodal DG is recovered (Wang 2024, §2.2,
§3, Fig. 1), Williams–Shunn points on triangles with Gauss–Legendre flux
points (Dzanic et al. 2022, Fig. 1), $\alpha$-optimized points on tetrahedra
and Gauss–Legendre–Lobatto points on hexahedra in PyFR
([Witherden et al. 2025](/sources/witherden-2025.md), Fig. 1, §5.1).
Witherden et al. (2025,
§2, Eqs. 1–7) recap the same four steps (interpolation to the flux points,
common interface flux, discontinuous flux, correction by the divergence of
the correction functions) on mixed elements and call FR "a form of
discontinuous spectral element method"; the code is described on
[PyFR](/software/pyfr.md).

**Interface fluxes and time stepping in the sources.**

| Source | code | inviscid flux | viscous flux | time stepping | degrees used |
|---|---|---|---|---|---|
| Dzanic et al. (2022), §2.3 | PyFR | Rusanov-type | BR2 | explicit fourth-order Runge–Kutta | $N=1$, $3$ |
| Duan & Wang (2024), §3 | hpMusic | Roe | common solution and gradients, face gradients by BR2 | explicit SSP-RK3, or optimized BDF2 with (block) LU-SGS | $N=2$–$5$ |
| Wang (2024), §2.2, §3 | ATHOS | Rusanov at no-slip walls, Roe or HLLC inside | LDG, penalty $0$, directional parameter $\pm0.5$ | explicit low-storage five-stage fourth-order Runge–Kutta, CFL $0.85/(2N+1)$ | up to $N=3$ |
| Vandenhoeck et al. (2022), §2–3 | COOLFluiD | AUSM$^+$-up (Roe named as an option) | BR2 | implicit backward Euler, Newton linearization, GMRES (PETSc); CFL ramped up to 1250 | $N=0$–$6$ |
| Ims & Wang (2023), §2 | hpMusic | common flux from a local Riemann problem | BR2 | explicit SSP-RK3 or implicit BDF2OPT | $N=1$, 2, reference at 4 |
| Shi & Yan (2023), §II.A, §IV.A | NFR (in-house) | Roe | BR2 | explicit SSP-RK3 | $N=2$ (ramp), 3 (Taylor–Green) |
| Liu & Yuan (2023), §2, §5 | 1-D research code | local Lax–Friedrichs | none (Euler) | SSP-RK3, CFL $1/(2N+1)$ | $N=2$–$5$ |
| Witherden et al. (2025), §2, §3.5–§3.6, §5 | PyFR v2.0.3 | "an appropriate Riemann solver" (not specified further) | not stated | explicit, with adaptive steps from embedded low-storage Runge–Kutta pairs; dual time stepping with $p$-multigrid for the artificial-compressibility solver | $N=3$ (supersonic Taylor–Green), "seventh-order solution polynomials" (scaling) |
| Vermeire (2024), §3 | not named | Rusanov with Davis wave speed | BR2 | classical RK4 (Taylor–Green), optimal explicit Runge–Kutta (channel), paired explicit Runge–Kutta (airfoil) | $N=1$–$6$ |
| Gao et al. (2025b), §II A, §II D, §III | not named | HLLC at the wall (hybrid with a weakly prescribed flux); interior flux not stated | not stated | low-dissipation low-dispersion Runge–Kutta of Hu et al., 2N-storage | $N=2$–$4$ |

Wang (2024, §2.2) reads the Rusanov flux as a central flux with scalar
dissipation (the largest local wave speed) and the Roe flux as a central flux
with matrix dissipation, so that "the choice of Riemann solver can have an
impact on the accuracy and robustness of implicit LES". The LDG penalty on
the solution jump is set to zero, "the minimum dissipation version of LDG"
(§2.2, Eq. 16; see [jump-penalty stabilization](/methods/jump-penalty-stabilization.md)).
Wang's ATHOS is a new in-house C++ FR solver on linear quadrilaterals and
hexahedra, which raises the order by restarts $N=0\to1\to2\to3$ (§3, §4.2).

## The FR family, the correction parameter and nonlinear stability

**Lineage**, as Brillon & Nadarajah (2026, §1) cite it: after Huynh's
FR, Wang and Gao's lifting collocation penalty applied a "correction field"
to the surface integral; Haga et al. merged the two into CPR, and Jameson
et al. proved the FR surface reconstruction identical to the CPR
correction field, so that "FR" and "CPR" became "loosely
interchangeable". The **energy-stable FR (ESFR)** or
Vincent–Castonguay–Jameson–Huynh schemes form a family of provably
linearly stable schemes, extended to linear advection–diffusion by
Castonguay et al., some of which allow "significantly higher explicit
time-step limits than DG schemes while maintaining the expected order of
accuracy"; with suitable correction functions ESFR recovers DG and the
[spectral difference](/methods/spectral-difference-method.md) method.
Allaneau and Jameson read ESFR in one dimension as a filtered DG scheme,
and Zwanenburg and Nadarajah extended the equivalence to three-dimensional
elements and to weak and strong modal DG (all as cited there, §1).

**Correction parameter as a filter** (Brillon & Nadarajah 2026, §3.1.5,
citing those works). The FR mass matrix $\mathsf M+\mathsf K$ "effectively
acts as a linear filtering operator" on the DG residual. For
$c_{\mathrm{FR}}<0$ the filter amplifies the highest mode of the residual;
$c_{\mathrm{FR}}=c_{\mathrm{DG}}=0$ is unfiltered DG; $0<c_{\mathrm{FR}}\le c_+$
damps the highest mode, $c_+$ being the largest stable value determined by
Castonguay for $N\in[2,5]$. Two further values recover known schemes:
$c_{\mathrm{SD}}$ the stable spectral difference scheme and
$c_{\mathrm{HU}}$ Huynh's $g_2$ scheme. No numerical values of the
parameter are printed.

**Nonlinearly stable FR (NSFR).** Brillon & Nadarajah (2026, §2.7,
Eqs. 62–72) use the NSFR scheme of Cicchino et al. (cited; proofs in
the cited works), implemented in the open-source PHiLiP code on deal.II.
On tensor-product hexahedra with a modal basis of degree $N$ and
Gauss–Lobatto–Legendre (GLL) solution nodes, the convective volume term is
written in split form,
$$(\mathsf M+\mathsf K)\frac{d\hat U}{dt}=-\mathsf X^{\mathsf T}\big[(\tilde Q-\tilde Q^{\mathsf T})\odot F^{\#}\big]\mathbf 1-(\text{surface flux term})+(\text{viscous volume and surface terms}),$$
with $\hat U$ the modal coefficients, $\mathsf X$ the basis evaluated at the
volume and face flux nodes, $\tilde Q-\tilde Q^{\mathsf T}$ Chan's
skew-symmetric stiffness operator, $\odot$ the Hadamard product, and
$F^{\#}$ the matrix of two-point fluxes $f^{\#}$ between all pairs of
volume and face flux nodes, each multiplied by the average of the two
nodes' metric cofactor matrices (page-local symbols; the source writes
$\chi$ for $\mathsf X$, which the registry keeps for the Spalart–Allmaras
ratio). The two-point fluxes
are evaluated on **entropy-projected variables**, which the authors call
"key in enabling entropy stability on uncollocated solution and flux or
integration nodes", so the flux nodes may be Gauss–Legendre (GL,
uncollocated) or GLL (collocated). The correction operator $\mathsf K$
carries $c_{\mathrm{FR}}$; the auxiliary (gradient) equation always uses
$c_{\mathrm{DG}}$; viscous fluxes use the symmetric interior penalty;
tensor and Hadamard products use sum factorization. The authors present
the scheme as "provably nonlinear stable by construction, i.e. entropy
stability", stable "on the coarsest of meshes", "without over-integration"
and "without upwind-type dissipation" (§1); the baseline uses the
entropy-conserving Ismail–Roe two-point flux with no upwind interface
dissipation (§2.7.1, Eqs. 73–79), and time stepping is SSP-RK3. See
[entropy conservation](/properties/entropy-conservation.md) and
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
for the split-form framework, and the collocated GLL variant, which the
authors call "also known as DG-SEM" (§3.1.4), on
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md).

## Nonlinearly stable FR on free-shear turbulence

Brillon & Nadarajah (2026, §3) assess NSFR on the viscous
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($Re=1600$,
$M=0.1$) and on the Comte-Bellot–Corrsin decaying grid turbulence (see
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)).
Baseline: $c_{\mathrm{DG}}$, Ismail–Roe flux, GL flux nodes, no upwinding,
no over-integration, CFL 0.1. Comparison scheme: classical strong-form DG
with a Roe flux and over-integration on $2(N+1)$ quadrature points per
direction ("OI").

- **DNS.** At $256^3$ degrees of freedom ($N=7$ on $32^3$ elements, and
  $N=3$ on $64^3$) NSFR without added dissipation reproduces the
  kinetic energy and dissipation rate of the $512^3$ reference of Dairay
  et al., and its effective viscosity, the dissipation rate over twice the
  enstrophy times $Re$, stays within 4.5% of the physical one; the
  schemes with Roe interface dissipation are briefly more dissipative than
  the reference and lower the peak enstrophy (§3.1.1, Figs. 2, 4; see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md)).
- **Under-resolved runs** ($96^3$, $64^3$, $48^3$, $24^3$ degrees of
  freedom, mostly $N=5$): NSFR is stable at every resolution without added
  dissipation, whereas strong DG without over-integration at $N=7$,
  $64^3$, fails around $t^*=6$, "a linearly stable scheme can be unstable
  in the absence of over-integration" (§3.1.2–3.1.3, Figs. 8, 11). NSFR
  reaches a higher peak enstrophy than over-integrated strong DG at all
  resolutions, while at $64^3$ the latter's dissipation rate is slightly
  more accurate through transition (§3.1.3).
- **Cost.** Per SSP-RK3 step on $4^3$ elements and 16 MPI ranks,
  over-integrated strong DG costs about twice the CPU time of split-form
  NSFR for $N\in[5,12]$ (§3.1.3, Fig. 12).
- **Flux nodes.** GL nodes integrate exactly to degree $2N+1$ and GLL to
  $2N-1$; at $N=5$, $96^3$, the collocated GLL scheme departs from the
  expected dissipation rate near $t^*\approx5$, while with three extra
  quadrature points both node sets agree and the uncollocated GL scheme
  without over-integration already matches them: "with sufficient
  integration accuracy, the solution is independent of the choice of flux
  nodes" (§3.1.4, Fig. 13).
- **Correction parameter.** The dissipation peak orders as
  $c_+>c_{\mathrm{HU}}>c_{\mathrm{SD}}>c_{\mathrm{DG}}$, "the added
  dissipation associated with larger c values", with similar spectra. The
  authors' CFL limits at $N=5$, $96^3$, defined as the largest CFL that is
  stable and keeps the kinetic energy non-increasing, are 0.26 for
  $c_{\mathrm{DG}}$ NSFR, 0.36 for $c_+$ NSFR and 0.14 for over-integrated
  strong DG with Roe flux, so that $c_+$ gives "a solution similar to that
  of $c_{\mathrm{DG}}$ and strong DG at about half the computational cost"
  (§3.1.5, Table 5, Figs. 14–15).
- **Two-point flux.** Ismail–Roe (entropy conserving), Kennedy–Gruber
  (kinetic-energy preserving), Chandrashekar (both) and Chandrashekar as
  modified by Ranocha (both, plus pressure-equilibrium preserving) give
  nearly indistinguishable spectra, energies and dissipation rates on the
  viscous case; Kennedy–Gruber is the cheapest, having no logarithmic mean
  (§3.1.6, Fig. 16; see
  [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
- **Added interface dissipation.** Roe or low-dissipation (L2) Roe
  dissipation lowers the peak enstrophy; added Lax–Friedrichs upwinding
  gives a higher peak enstrophy and more small-scale energy than the
  projected DNS, which the authors call "anti-dissipative" behaviour; all
  three almost remove the oscillations of the node-wise pressure-dilatation
  term that the dissipation-free scheme shows, as Flad & Gassner reported
  for split-form DG (§3.1.1, §3.1.7, Figs. 3, 17–18). The oscillations
  are much smaller with collocated GLL flux nodes, which the authors read
  as coming from interpolating the flux to the face nodes (§3.1.4).
- **Explicit subgrid models.** Smagorinsky ($C_s=0.10$), shear-improved,
  high-pass-filtered and dynamic Smagorinsky models, all with a
  low-Reynolds-number correction and filter width $V_e^{1/3}/(N+1)$,
  raise the dissipation rate marginally, lower the peak enstrophy and
  drain energy at wavenumbers where the baseline already has a deficit, so
  "the SGS models considered in this work are not recommended for the LES
  of transitional turbulent free-shear flows using NSFR" (§3.1.8, Fig. 19;
  see [Smagorinsky model](/methods/smagorinsky-model.md) and
  [implicit LES](/definitions/implicit-les.md)). Collocated strong DG
  without over-integration at $N=5$ is stabilized by a high-pass-filtered
  shear-improved Smagorinsky model, but inaccurately: "a stable scheme
  without any de-aliasing can lead to inaccuracies" (§3.1.8, Fig. 20).
- **Decaying grid turbulence.** Collocated NSFR at $N=3$ on $32^3$
  elements ($128^3$ degrees of freedom, $96^3$ unique) reproduces the
  measured spectra; its kinetic-energy error against the integrated
  measured spectrum at the last station is 1.36% (5.30% when its spectrum is
  truncated at $k_c=31$), against 29.81% for a sixth-order
  finite-difference LES at $64^3$ and 15.55% and 29.75% for CPR at $N=5$
  ($78^3$) and $N=1$ ($126^3$), as tabulated from the cited works; the
  authors expect the lower error to be "partially due" to more unique
  degrees of freedom and to oversampling in the post-processing (§3.2,
  Table 6).

The authors state it is, to their knowledge, "the first study on the use of
a provably entropy conserving and stable high-order flux reconstruction
method for the simulation of viscous turbulent flows" (§1).

## Implicit FR for RANS with transition

[Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) present what
they call, to their knowledge, the first FR solver for RANS with
laminar–turbulent transition; earlier FR-RANS work used the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) and Wilcox
[$k$-$\omega$](/methods/k-omega-model.md) models (Abstract, §1). The
closures are the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) model
of 2003 rewritten to transport $\ln\omega$ (an idea they take from Bassi et
al.'s DG $k$-$\omega$, which removes the steep near-wall growth of $\omega$
that made high-order SST unstable and guarantees $\omega>0$) and the
Langtry–Menter [local-correlation transition model](/methods/local-correlation-based-transition-model.md)
(§1). The FR scheme is Huynh's on tensor elements with Gauss–Legendre
solution points, VCJH correction functions ($c_{\mathrm{SD}}$ by default),
BR2 for diffusion and AUSM$^+$-up at interfaces (§2, Eqs. 47–61).

**Semi-analytical Jacobian** (§3.2.2, Eqs. 66–87). A purely numerical
Jacobian, which repeats the whole FR procedure for every perturbed
solution-point value, is costly and does not scale with order (§3.2.1).
The authors differentiate the FR operator analytically and split the
Jacobian into six contributions, from the element-interior flux and the
face correction, each through the state and through the corrected
gradient, the face terms for the interface and for the extrapolated
discontinuous flux; on tensor elements the corrected gradient at a solution
point depends on $3d(N+1)$ states of the element and its $2d$ neighbours
($d$ the space dimension, page-local). Only the derivatives of the
physical flux are taken by finite differences, whence "semi-analytical".
Per element the Jacobian has $O(N^{d+1})$ entries, and the corrected
gradient adds a factor $O(N)$ to each with diffusion, so the time per degree
of freedom scales at best as $O(N^2)$ in any dimension; single-thread
timings on an Intel Core i7-9700K follow that scaling, with or without the
two transition equations (§4.3, Fig. 17).

**Source-term Jacobian.** Of a full analytical, a negative-part-only
(after Merci et al.), a decoupled (no derivatives with respect to the
mean-flow variables, turbulence and transition blocks separate) and a
diagonal treatment, all reach the target CFL of 1250 at $N=2$ on the
ERCOFTAC T3A case, whereas without a source Jacobian the CFL limit had to
be lowered to 500; the fully numerical Jacobian stagnates, and the
decoupled treatment, slightly the fastest, is kept (§3.2.3, Figs. 6–7).
At a no-slip wall the ghost value of $\ln\omega$ uses the distance of the
first solution point instead of the theoretical zero (§3.3.1, Eq. 88).

**Accuracy on coarse grids.** On the Wieghardt
[flat plate](/benchmarks/turbulent-boundary-layer.md)
($Re_L=1.03\times10^7$), on 784 elements with first-element height
$y_1^+\simeq10$, the higher-order velocity profiles coincide and agree with
experiment, Spalding's law and a degree-2 DG reference (Wilcox $k$-$\omega$) on 8800
elements, and the $N=4$ skin friction lies considerably closer to
experiment than lower orders and that reference; on 392 elements with
$y_1^+\simeq25$ discontinuities visible at $N=5$ disappear at $N=6$, so
accurate results are obtained at $y_1^+\simeq25$ without
[wall functions](/methods/rans-wall-function.md), which the authors state
is beyond second-order finite volumes without such functions (§4.1, Figs.
9–10). On the [ERCOFTAC T3 plates](/benchmarks/ercoftac-t3-flat-plate.md)
on 143 elements the two highest orders coincide and approach experiment;
$N=0$ shows no transition; T3A and T3A$-$ results are very close to a
finite-volume reference on about 39 000 elements, and for T3B the FR
solution is "remarkably closer" to experiment (§4.2, Figs. 12–13). The
T3A skin friction at $N=5$ is nearly identical for the correction
parameters $c_{\mathrm{SD}}$, $c_{\mathrm{DG}}$ and $c_{\mathrm{HU}}$ (the
source's $c_{g2}$, Huynh's $g_2$; Fig. 14; see
[spectral difference method](/methods/spectral-difference-method.md)).

## Linear eigenanalysis of FR and its time integration

Tonicello et al. (2023) extend the spatial eigenanalysis of FR (a real
frequency prescribed, complex numerical wavenumbers solved for, as in
inflow–outflow problems) from the semi-discrete setting to the fully
discrete one with explicit Runge–Kutta schemes of one to five stages
(§2.2, Eqs. 13–23; method and results on
[eigensolution analysis](/methods/eigensolution-analysis.md)). For the
FR family the findings are:

- with upwind fluxes the number of transmitted eigenmodes equals the
  number of Runge–Kutta stages, one of them physical; non-upwind fluxes
  double it with reflected modes (§3, Figs. 2, 4–5);
- in its DG recovery FR has a more restrictive CFL limit than in its
  spectral-difference recovery (both upwind), so its dissipation curves
  extend to higher frequencies, and it is spatially less dissipative
  overall (§3, Fig. 7; App. Figs. 29–30; see
  [spectral difference method](/methods/spectral-difference-method.md));
- for fifth-order FR-SD with three-stage Runge–Kutta the spatial
  superconvergence of order $2N+1=9$ falls to fourth order at small
  wavenumbers, set by the time scheme, and is kept in an intermediate
  range that smaller time steps widen (§3, Fig. 8);
- larger time steps reduce the high-frequency dissipation of upwind FR
  until anti-dissipation at the CFL limit, and smooth the "dissipative
  bubbles" of nearly centred fluxes (§3, Fig. 9).

On under-resolved inviscid Taylor–Green and duct flows the time step has
almost no effect until very close to the CFL limit, so that in implicit
LES "temporal errors are more likely overshadowed by spatial errors",
while in well-resolved flows the time-integration order limits the
convergence (§4.2–§4.3, §5; see [numerical dissipation](/properties/numerical-dissipation.md)).

## FR as implicit LES

Duan & Wang (2024, §3) state that projecting a solution onto the
piecewise-polynomial space "can be considered a space-filtering operation",
so FR/CPR without a subgrid model "becomes ILES", and an explicit model
amounts to extra dissipative flux terms. Evidence in the sources:

- **Well-resolved flows favour no model.** On the viscous
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=1600$
  ($64^3$ elements, $N=4$) the no-model enstrophy lies "almost on top of"
  the DNS, and in a wall-resolved [channel](/benchmarks/turbulent-channel-flow.md)
  at $Re_\tau=180$ ($N=3$, per-degree-of-freedom spacing
  $\Delta x^+=5.7$, $\Delta y^+=0.68$, $\Delta z^+=5.7$) the no-model LES
  agrees very well with DNS (Duan & Wang 2024, §5.2–5.3, Figs. 7, 9–10). Wang
  (2024, §4.1, Figs. 2–3) reproduces the DNS dissipation rate and spectra of
  the Taylor–Green vortex at $Re=1600$ and $5000$ on $64^3$ elements at $N=3$.
- **Under-resolution breaks it.** In a wall-modelled channel at
  $Re_\tau=5200$ on $60\times16\times40$ elements the no-model run was not
  stable (Duan & Wang 2024, §5.4); in decaying isotropic turbulence on
  $32^3$ cells, $N=2$ and $3$ pile up energy at high wavenumbers, which the
  authors attribute to aliasing (§5.2, "we believe"). Dzanic et al. (2022,
  §3.1, Fig. 5) see large oscillations of the wall-normal variance in $N=3$
  under-resolved DNS of the [periodic hill](/benchmarks/periodic-hill.md),
  attributed to aliasing-driven instability and absent with PANS.
- **Order at fixed degrees of freedom.** Dzanic et al. (2022, §2.3, §3)
  compare $N=1$ ("comparable to a finite volume formulation") with $N=3$ at
  equal degrees of freedom, the $N=1$ meshes carrying "approximately 6-8
  times as many elements": fourth order improves first-order statistics of under-resolved
  DNS and PANS about equally, but second-order statistics and the cylinder's
  spectral peaks much more for PANS, which the authors attribute to the
  lower [numerical dissipation](/properties/numerical-dissipation.md) of the
  high-order scheme (details on the [PANS](/methods/partially-averaged-navier-stokes.md)
  page). Their new $N=3$ DNS of the cylinder at $Re_D=3900$ uses about
  55.6 million degrees of freedom (§3.2; see
  [direct numerical simulation](/definitions/direct-numerical-simulation.md)).
- **The interface flux as the model.** Hamedi & Vermeire (2022, §1,
  §2.1) state, citing earlier FR studies, that the numerical dissipation
  of FR with suitable high-order time stepping acts as a built-in
  subgrid model, the Riemann-solver dissipation "reducing or eliminating
  a pile-up of kinetic energy in high-frequency modes"; they call their
  unfiltered runs ILES and their filtered runs "LES", the filter being the
  only model.
- **ILES on adapted meshes.** Ims & Wang (2023) run FR/CPR as implicit
  LES ("we apply no subgrid scale model") with an accuracy-preserving
  limiter in severely under-resolved areas, and adapt the mesh by
  isotropic splitting of curved cells with mortar faces at hanging nodes
  (§2, §4). In three dimensions the geometry vectors of a mortar face must
  come from the coarse side if its polynomial is linear and, "possible and
  advisable", from the fine side otherwise, or the calculation turns
  unstable through under-integration of the coarse side (§4; no data
  shown). Of three refinement indicators, the unsteady residual evaluated at
  degree $N+1$ is "literally the instantaneous flaw in the simulated flow
  field", a map of where the discrete equations depart from Navier–Stokes
  (§3.1, §5.3); details on [mesh adaptation](/methods/mesh-adaptation.md).
- **ILES of a shock/boundary-layer interaction.** Shi & Yan (2023) run
  $N=2$ FR/CPR as wall-resolved implicit LES of the Mach 2.9 flow over a
  $24^\circ$ compression ramp, citing evidence that dissipative
  discontinuous methods (DG, SD, FR/CPR) support implicit LES without an
  explicit model, and state that FR/CPR simulations of shock-dominated
  supersonic turbulence are rare, the configuration having been computed
  mainly with high-order finite differences (§I). Their solver reproduces
  the Taylor–Green vortex at $Re=1600$ with $N=3$ on $32^3$, $64^3$ and
  $96^3$ cells (128–384 degrees of freedom per direction), converging to the
  spectral $512^3$ reference (§III.A, Figs. 1–2).
- **Incompressible ILES with artificial compressibility.** Vermeire
  (2024) couples FRDG with the entropically damped artificial
  compressibility (EDAC) formulation of Clausen, which replaces the
  pressure Poisson equation by an explicit pressure evolution with a
  diffusion term that damps pressure waves,
  $$\partial_tp+u_j\partial_jp+\frac{1}{M_{\mathrm{AC}}^2}\partial_ju_j=\frac{1}{Re}\,\partial_j\partial_jp$$
  (Eq. 1; $M_{\mathrm{AC}}$, page-local, the "incompressibility factor",
  smaller meaning stricter). Rewritten in dimensional flux form under
  $\partial_ju_j=0$ (Eqs. 2–5), the pressure flux is $u_j(p+\zeta)$ with
  $\zeta=1/M_{\mathrm{AC}}^2$, $p$ kinematic, and the pressure-diffusion
  coefficient is $\nu$, so that the system is fully explicit, without
  pseudo-time sub-iterations or global solves (§1–§2). The scheme runs as implicit LES, its
  interface upwinding "akin to a numerical dissipation stabilized
  under-resolved DNS" (§1). At fixed degrees of freedom, accuracy rises with
  $N$ on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
  $Re=1600$ (64 and 128 degrees of freedom per direction, $N=1$–6), on the
  wall-resolved [channel](/benchmarks/turbulent-channel-flow.md) at
  $Re_\tau=395$ (one quarter and one half of the DNS degrees of freedom per
  direction) and on the [SD7003 airfoil](/benchmarks/sd7003-airfoil.md) at
  $Re_c=60{,}000$, $\alpha=8^\circ$ (§4, Figs. 3–21, Table 3). $N=1$ is
  over-dissipative: on the vortex the dissipation rate is over-predicted
  while enstrophy is under-predicted, so most of the dissipation is
  numerical, and in the channel the mean velocity and drag are over-predicted
  (§4.1–§4.2). The volume-averaged divergence error falls roughly linearly
  with $M_{\mathrm{AC}}$ and also with $N$: the medium-resolution $N=6$ run at
  $M_{\mathrm{AC}}=1/5$ has less divergence error than $N=1$ at $1/40$
  (Figs. 7–8). Instabilities appear at high degree: oscillations after the
  dissipation peak at $N=5$ and divergence at $N=6$ with
  $M_{\mathrm{AC}}=1/5$ and $1/10$ on the coarse vortex mesh, and most channel
  runs at $N=5$, 6 unstable, which the author attributes to numerical
  dissipation that "may not be sufficient for ILES" (§4.1–§4.2). The
  conclusion is that the combination suits low and moderately resolved
  implicit LES with $N\le4$ (§5); no dealiasing or filtering is mentioned.
  Details on [implicit LES](/definitions/implicit-les.md) and
  [numerical dissipation](/properties/numerical-dissipation.md).
- **Cost against finite volumes**, as relayed by
  [Saini et al. (2023)](/sources/saini-2023.md), §1, from earlier studies:
  fifth-order PyFR was more accurate than a commercial finite-volume code but
  about 2 and 6 times more expensive on two cases, and third-order FR was more
  accurate at one third of the cost of a second-order run on a 64 times larger
  mesh.

## Explicit subgrid models on FR: element averaging and filter width

Duan & Wang (2024) calibrate the [Smagorinsky](/methods/smagorinsky-model.md),
[WALE](/methods/wale-model.md) and [Vreman](/methods/vreman-model.md) models in
hpMusic for high-order WMLES, where they argue ILES "often runs into
robustness and accuracy issues due to the low dissipation embedded in these
methods" (Abstract, §1). Their implementation choices (§3):

- **Element-averaged eddy viscosity**, to make the model "less oscillatory":
  $$\nu_t=\frac{1}{V_e}\sum_q w_q\,\nu_{t,q},$$
  with $\nu_{t,q}$ the pointwise value at solution point $q$ (Eq. 26).
- **No interface subgrid flux**: the common flux of the subgrid stress is set
  to zero on every face, "to guarantee the conservation and minimize data
  communication", on the ground that model stresses are poorly correlated
  with the physical ones and serve only to drain energy (Eq. 27).
- **Model stress** added to the viscous stress with the viscous sign, built
  on the full strain rate, $\tau_{ij}=-2\nu_t\bar S_{ij}$ (no deviatoric
  projection printed), with the subgrid heat flux, pressure work and
  turbulent diffusion dropped "for the low Mach number flows considered"
  (§2.1–2.2).

**Filter width.** The model coefficients are kept and the length scale is
recalibrated, with three choices (Eqs. 28–30):
$$\text{d1: }\Delta=V_e^{1/3},\qquad \text{d2: }\Delta=\frac{V_e^{1/3}}{\sqrt{N+1}},\qquad \text{d3: }\Delta=\frac{V_e^{1/3}}{N+1}.$$
d1 is the finite-volume convention (one degree of freedom per element), d3
the "natural" choice with $N+1$ degrees of freedom per direction, and d2 is
introduced because the models "have been mostly calibrated and used for
2nd-order methods" and high-order methods have much less numerical
dissipation, so d3 is expected to under-dissipate (§3). Findings (§5–6):

- dissipation ranks WALE < Vreman < Smagorinsky; on the inviscid
  Taylor–Green vortex ($16^3$ elements, $N=4$) every model and length scale
  dissipates far more than the Riemann-solver dissipation of the scheme, and
  d2, d3 much less than d1 (Figs. 5–6);
- in isotropic turbulence d1 shrinks the resolved wavenumber range, d3 is
  close to no model, d2 is a "good balance" (Fig. 8);
- in the wall-resolved channel Smagorinsky fails at every length scale,
  WALE and Vreman match DNS with d2 and d3 (Figs. 9–10);
- in the wall-modelled channel at $Re_\tau=5200$ ($N=2$–$5$, element sizes
  $\Delta x^+=1088$, $\Delta y^+=650$, $\Delta z^+=544$) and at
  $Re_\tau=544$ ($N=3$), Vreman gives the same ranking at every degree, d1
  too dissipative, d3 too little, d2 best; WALE is best with d1 for $N=2$–$4$
  and with d2 at $N=5$, where the trend with length scale reverses
  (Figs. 11–15).

The recommendation is Vreman with d2 for high-order WMLES (§6). The DG
sources of this bundle use d3 as the DG filter width (see
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md), "Filter
width"); Duan & Wang's d2 is calibrated with their element-averaged eddy
viscosity and zero interface subgrid flux, in wall-modelled channels and
the other cases of §5.

**Wall model on FR.** Duan & Wang (2024, §4, Fig. 4) impose the
[equilibrium wall model](/methods/equilibrium-wall-model.md) weakly at the
wall flux points and take its input at the interface between the first and
second element off the wall, from the second element, because "the
turbulent eddies at the first element are always under-resolved", so the
matching height equals the first element height; they call a near-wall
aspect ratio of one desirable.

**Wall model at the first solution point.**
[Gao et al. (2025b)](/sources/gao-2025-b.md), §II C–D, build a
wall-stress WMLES in an FR/CPR solver with the
[Vreman model](/methods/vreman-model.md) ($c_v=0.07$, isotropic filter
width) and three departures from the earlier DG/FR practice of Frère et
al., Shi et al. and Wang that they cite:

- **Input point.** The wall model reads the velocity at the solution point
  of the wall-adjacent element closest to each wall flux point, not at the
  interface between the first and second elements, to keep the compact
  stencil on unstructured meshes; they state that the second-cell input
  leaves "pronounced oscillations" in the first-cell velocity profiles of
  those studies even after long averaging (§I, §II C3, Fig. 1). Duan &
  Wang (2024, §4) above take the input from the second element because
  "the turbulent eddies at the first element are always under-resolved".
- **Non-iterative wall laws.** The equilibrium law of Allmaras, Johnson &
  Spalart is inverted by a five-branch fit of $y^+$ against the local
  Reynolds number $Re_y=Uy/\nu$ (registry §11), and a pressure-gradient
  correction after Shih et al. is applied in a second step (§II C1–C2,
  App. A); details on [equilibrium wall model](/methods/equilibrium-wall-model.md)
  and [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md).
- **No-slip wall with a hybrid inviscid wall flux.** Instead of the slip
  condition "previous wall-model studies all stressed", they impose
  no-slip and take the inviscid wall flux as a convex combination
  $C_1F_{\mathrm{PRE}}+C_2F_{\mathrm{RM}}$, $C_1+C_2=1$, of a weakly
  prescribed flux, accurate but producing grid-level wall oscillations
  except in simple channels, and a weak-Riemann HLLC flux, stable but
  giving "an excessively steep mean velocity profile"; $C_2$ is the
  smallest stable value, $1/12$ to $1/5$ (§II D, Eqs. 33–37, Fig. 2;
  page-local $C_1$, $C_2$, $F_{\mathrm{PRE}}$, $F_{\mathrm{RM}}$). Rusanov
  is rejected at the wall as too dissipative, because the extrapolated
  tangential velocity at the wall flux point is not zero (§II D3).

On a [channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=2000$,
5200 and $10\,000$ ($48\times24\times24$ elements, $N=2$–4; first solution
point at $y^+\approx120$ at $Re_\tau=10^4$) the mean velocity follows the
log law without the first-element oscillations of the cited data at
$Re_\tau=5200$ (Figs. 3–5). On the [periodic hill](/benchmarks/periodic-hill.md)
at $Re=10\,595$ (meshes of $32\times12\times16$ and $48\times24\times24$
quadratic hexahedra) the $L_2$ errors of mean velocity and Reynolds stress
against the PIV data fall with $N$ from 2 to 4 and with refinement
(Fig. 13), and $Re=37\,000$ runs at $N=3$ on the coarse mesh (§III B).
Shi et al., as they cite them, preferred an even degree in the wall
element (quadratic over cubic); Gao et al. report improvement monotone
in $N$ from 2 to 4 on the hill. On one core the standard and generalized
wall models add 6% and 12.5% to the run time (§III B). See
[wall-modelled LES](/methods/wall-modelled-les.md).

## Stabilization of FR implicit LES

Under-resolved FR needs an added dissipation mechanism. Duan & Wang (2024,
§1, Fig. 2) show, for a fourth-order discontinuous method in a channel at
$Re_\tau=5200$, that the outcome of solution limiting depends on its amount:
too little damping over-predicts the wall friction and under-predicts the
velocity, too much does the reverse, which they call "very ad hoc" (§5.4)
and replace by explicit models.

Wang (2024) keeps implicit LES and stabilizes it by **solution filtering**:
a local modal filter switched on in elements whose Persson–Peraire
smoothness indicator exceeds a threshold, or the positivity-preserving
entropy filter of Dzanic and Witherden; both are described, with their
thresholds, costs and turbine results, on
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
("Indicator-switched modal and entropy filters"). The author states that
filtering adds local dissipation to the total numerical dissipation that
ILES relies on, and that solution filtering may cause time inconsistency
(§2.3, §5). Further findings on the interface flux (§2.4.2, §4.3.2, Tables
7–8):

- at no-slip walls the convective flux is computed from ghost states with a
  Riemann solver; of Rusanov, Roe and HLLC the most dissipative, Rusanov,
  is the most robust there, consistent with Mengaldo et al. as cited;
- inside the domain HLLC is more robust than Roe (stable with less
  filtering) on the VKI LS89 vane, which the author explains by Roe's known
  failure near vacuum states, citing Toro; when both are stable, mean-flow
  results are nearly identical, and the predicted heat-transfer coefficient
  depends more on the filter threshold than on the Riemann solver.

[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) stabilize
under-resolved FR by a **modal filter applied after every time step**,
which they prefer to de-aliasing and limiting (relatively costly) and to
artificial viscosity (which needs a sensor), while citing Park et al. as
finding filtering harmful to accuracy (§1). Their
FR variant is the DG-recovering one (Radau correction functions, Gauss
solution and flux points, Rusanov interface flux, BR2 viscous flux), and
they state that the resulting filters "may not be optimal" for other
Riemann solvers and "would not be generally suitable" for other
correction functions (§2.1, §3.4). The filter acts on the orthonormal
modal coefficients through the Vandermonde matrix and is normalized by
the number of steps per characteristic time, so that its cumulative
strength does not depend on $\Delta t$; its exponential parameters are
optimized on more than 14,000 inviscid Taylor–Green runs at $16^3$
degrees of freedom for $N=3$–$5$ (details, tables and caveats on
[explicit modal filtering](/methods/explicit-modal-filtering.md)). With the
strongest filter:

- a turbulent [channel](/benchmarks/turbulent-channel-flow.md) at
  $Re_\tau=395$ with about 3/8 of the DNS degrees of freedom
  (Table 2 spacings $\Delta x^+\approx25$, $\Delta y^+\approx0.9$,
  $\Delta z^+\approx17$) is stable unfiltered at $N=3$ and 4 but needs the filter
  at $N=5$; filtered and unfiltered mean velocity and Reynolds stresses
  agree with each other and with DNS, and at $N=3$ the filtered near-wall
  rms fluctuations are closer to DNS for $10<y^+<40$ (§5.1, Table 2, Figs.
  23–25);
- on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
  $Re=1600$ ($64^3$ degrees of freedom, linear and sinusoidally curved
  meshes) the filters "slightly increase the amount of numerical
  dissipation" without significant loss of accuracy (§4.2–4.3);
- on a stalled NACA 0020 at $20^\circ$, $Re=20\,000$, $M=0.2$, the mean
  $C_L$/$C_D$ are 0.651/0.357 filtered and 0.639/0.353 unfiltered against
  0.64/0.35 in the DNS of Rosti et al. (§5.2, Table 3);
- on the isentropic vortex the observed orders are nearly unchanged
  (e.g. 7.626557 unfiltered against 7.626587 filtered at $N=3$), both
  above $N+1$ (§4.1, Table 1).

They name two sources of aliasing in FR: the non-linearity of the fluxes
and, on curved elements, a non-constant mapping Jacobian, a
"geometrical-aliasing source" (§2.2; see
[geometric conservation law](/properties/geometric-conservation-law.md)).

**Wall cells of wall-modelled LES on cold walls.**
[Okano & Haga (2026)](/sources/okano-2026.md) run
[wall-modelled LES](/methods/wall-modelled-les.md) in JAXA's hexahedral FR
code LS-FLOW-HO, the same DG-recovering variant (Radau correction
functions, Gauss–Legendre solution points, BR2 viscous flux) with the SLAU
inviscid flux, SSP Runge–Kutta (4 stages, third order), $N=3$ by default
and no explicit SGS model (§2.1). They state that in the coarse cells below
the matching height the under-resolved Reynolds shear stress makes the
resolved gradients too steep and the high-order polynomials oscillate
(§1). A wall-normal [modal filter](/methods/explicit-modal-filtering.md)
on the wall-adjacent cells, of the Hamedi–Vermeire type above (as they
cite it), keeps a channel stable at a wall-to-recovery temperature ratio
of 0.8 but not below 0.4; at 0.1 the run blows up within 500 steps at
$N=3$, and at $N=1$ after a sharp near-wall temperature drop (§3,
Figs. 2–4). A smooth
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
confined to those cells, vanishing at the wall and at the matching height,
stabilizes the runs down to 0.1 at $N=1$, 2 and 3 with matched degrees of
freedom; the authors make the profile smooth within each cell because, as
they state, an artificial viscosity that oscillates inside a cell is
amplified by the polynomial gradient (§4–5; numbers on the
wall-modelled-LES page). A finite-volume WMLES on such walls (Mettu &
Subbareddy, as cited) did not report such an instability; the authors
met it with FR (§1).

**Four options in one code.** Witherden et al. (2025, §3.2) state that
PyFR is often run as under-resolved DNS, "also referred to as ILES", where
FR is subject to aliasing-driven instabilities, and offer four remedies:
[modal filtering](/methods/explicit-modal-filtering.md) (conservative and
cheap, but indiscriminate, with strength, frequency and cut-off modes as
free parameters); anti-aliasing by a quadrature-based least-squares
projection of the flux, "markedly superior" to modal filtering as they
cite it and "typically" doubling the run time in 3D at anti-aliasing degree
$N+1$; Persson–Peraire-type
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md),
which needs parameterization and can lower the stable explicit time step;
and the entropy filter of Dzanic & Witherden, applied only where density
or pressure positivity or a minimum-entropy bound (over the element and its
Voronoi neighbours at the previous step) is violated, which "does not
explicitly require any problem-dependent parameterisation" apart from a
small fixed tolerance. They also replace the cross-product metric, which
loses free-stream preservation on curved grids, by a conservative curl-form
metric (§3.4; see [geometric conservation law](/properties/geometric-conservation-law.md)).
Wang (2024, §4.4.3) writes that the entropy filter is "not completely
parameter-free", its tolerance controlling how strictly the minimum
entropy principle is enforced.

**Shock capturing by sensor and limiter.** For shock-dominated flows the
sources add a troubled-cell sensor and a limiter to FR. Shi & Yan (2023,
§II.B, Eqs. 6–18) use the KXRCF sensor of Krivodonova et al. rewritten
without its grid-length scaling, on density, with threshold $C_{\mathrm{KX}}=0.01$ (page-local), the
P-weighted compact WENO limiter of Li, Wang & Ren with modified linear
weights and a rule that zeroes the weights of lower modes when they
oscillate more than higher ones, and the Zhang–Shu positivity-preserving
limiter on the Gauss–Lobatto points, because the WENO limiter does not keep
density and pressure positive and non-physical states crash the runs;
on the double Mach reflection the sensor also marks parts of the shear
layer and vortex, and the combination does "not completely remove the
numerical oscillations" (§III.B, Fig. 3). Liu & Yuan (2023, §3) extend the
a posteriori subcell finite-volume limiter of Dumbser et al. from DG to FR,
recompute troubled cells on $N+1$ subcells and precede the relaxed
maximum-principle test by a KXRCF-type pre-detection, which stops the shock
cell of a steady detonation from switching between FR and finite volume
and lets the solution converge (Table 2); details and both sensors on
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
and [shock sensors](/definitions/shock-sensor.md). Lv & Ekaterinaris (2023,
§4.2) relay that in the limiter-assisted FR LES of the NASA CRM by Wang &
Rahmani "only 0.3% of elements have the limiter activated", within their
caution that limiter dissipation can kill small scales in LES and that
under-resolved turbulence can be mistaken for shocks (see the
[NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)). At
equal degrees of freedom Liu & Yuan's $N=2$ FR with second-order subcells resolves one-dimensional
detonations without the oscillations behind the front that fifth-order
WENO-JS and WENO-Z show (§5.5, Fig. 9); the flows are inviscid and laminar.

**Wall units on high-order grids.** Wang (2024, §4.2, Eq. 26, after Jia et
al.) divides the first-cell $y^+$ computed from the cell height by $N+1$;
the [PANS](/methods/partially-averaged-navier-stokes.md) wall value of
Dzanic et al. (2022, Eq. 26) likewise uses the element height over $N+1$ as
first-point distance.

## Applications in the sources

- **Turbomachinery** (Wang 2024, §4.2–4.4): the T106C low-pressure-turbine
  cascade at exit $Re=80{,}000$ ($N=3$, 7.87 million degrees of freedom per
  equation) and the VKI LS89 high-pressure-turbine vane at
  $Re=1.13\times10^6$ with heat transfer (6.6 to 31.3 million degrees of
  freedom), see [turbine cascades](/benchmarks/turbine-cascade.md). Raising
  $N$ from 2 to 3, then refining the span, moves the heat-transfer
  coefficient towards experiment, and a spanwise spacing
  $\Delta z^+\approx45$–$60$ suffices for the mean heat transfer (§4.3.1).
- **Hybrid RANS/LES**: PANS with the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md)
  closure on the periodic hill and the circular cylinder (Dzanic et al.
  2022; see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).
- **Canonical LES**: Taylor–Green vortex, Comte-Bellot–Corrsin decaying
  [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
  wall-resolved and wall-modelled channels (Duan & Wang 2024, §5).
- **Moving and deforming grids** ([Liu et al. (2022b)](/sources/liu-2022-g.md),
  §2.1–2.2, Eqs. 1–11, Fig. 1): FR/CPR for the compressible Navier–Stokes
  equations in arbitrary Lagrangian–Eulerian form on moving triangles,
  with Roe common fluxes for the inviscid and BR1 for the viscous part.
  The two spatial metric identities of the
  [geometric conservation law](/properties/geometric-conservation-law.md)
  are satisfied by the high-order discretization and the temporal one is
  enforced by GCL error compensation; the correction field is evaluated
  in physical space, divided by the Jacobian determinant $\mathcal J$, to
  minimize errors on curved elements. Solution points are the
  $(N+1)(N+2)/2$ nodes of a high-strength triangle quadrature, flux points
  Gauss–Legendre points on the edges. At $N=2$ the scalar-wave test
  reaches third order on both stationary and deforming grids ($L_2$ error
  $8.22\times10^{-3}\to1.25\times10^{-5}$, orders 3.4, 3.0, 3.0, and
  $1.24\times10^{-2}\to1.76\times10^{-5}$, orders 3.1, 3.2, 3.2, from
  $10\times10$ to $80\times80$ split quadrilaterals; §3.1.1, Table 1). The
  applications are laminar fluid–structure interaction at $Re=100$–1000,
  vortex-induced vibration of a cylinder (see
  [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)) and a
  pitching and plunging NACA 0012 energy harvester (§3.2–3.3); the
  extension to implicit LES, RANS or wall-modelled LES is future work, with
  robustness against non-smooth eddy-viscosity fields and the cost of
  wall-distance-based models on moving grids named as the challenges (§4).
- **Shock tubes with learned fluxes** ([Ruggeri et al. (2022)](/sources/ruggeri-2022.md),
  §VI, Fig. 7): fourth-order FR ($N=3$) with the localized artificial
  diffusivity of Haga & Kawai, as cited, runs one-dimensional real-fluid
  shock tubes with neural-network, exact and Rusanov interface fluxes.
  The differences between fluxes shrink against the first-order runs, the
  largest being at the density contact where Rusanov oscillates more,
  "because with high order, the interfaces of the mesh have a less
  important role than for order 1". The flows are inviscid.
- **The High-Order CFD Workshop** ([Wang et al. (2013)](/sources/wang-2013.md),
  §5, Tables II–IV, VII): CPR–DG submissions of Iowa State University
  entered the bump, NACA 0012, vortex-transport and
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) cases of the
  first workshop, whose results are compared by error against work units
  (see [NACA 0012](/benchmarks/naca-0012-airfoil.md)); Huynh's
  flux-reconstruction paper appears only in the §1 list of high-order
  methods for unstructured meshes.
- **Adaptive turbine-cascade ILES** (Ims & Wang 2023, §5): T106c at
  $Re=80\,000$ ($N=2$), compared with an hpMusic DNS, and T106a at
  $Re=60\,000$ ($N=1$), compared with an $N=4$ run on a uniformly refined
  mesh; three indicators each refine the top 20% of cells per round, and the
  small-scale-energy and unsteady-residual indicators converge fastest,
  judged visually (see [turbine cascades](/benchmarks/turbine-cascade.md)
  and [hpMusic](/software/hpmusic.md)).
- **High-lift aircraft** (Kiris et al. 2023, Table 1, §III, §VI 1a): in the
  Fourth High-Lift Prediction Workshop the hpMusic submission ran $N=2$ FR
  as implicit LES with an equilibrium wall model taking its input at the
  interface of the first and second elements, implicit BDF2, 13 million
  degrees of freedom and aspect ratios up to 71; it obtained "reasonably
  accurate" integrated loads at maximum lift but lacked the outboard
  slat-bracket-wake separation, and its solutions switched between vastly
  different states with transients over more than 40 convective time units
  ([Kiris et al. (2023)](/sources/kiris-2023.md); see
  [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md)).
- **Compression-ramp interaction** (Shi & Yan 2023, §IV): the $24^\circ$
  ramp at $M_\infty=2.9$, $Re_\infty=5.966\times10^6\,\mathrm m^{-1}$, with
  digital-filter inflow; the incoming boundary layer is converged on three
  grids and the corner $C_f$ and wall pressure converge on the two finer
  ones to the WENO DNS references; the maximum amplification of the
  turbulent kinetic energy is 3.34 (§IV.B–C, Table IV; see
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- **GPU throughput** (Witherden et al. 2025, §5.2, Tables 2–3): a
  subsonic Taylor–Green vortex on 13 891 500 tetrahedra in double precision
  scales from 16 to 2048 ranks with efficiency 0.46 on Frontier (MI250X
  GCDs) and 0.47 on Alps (GH200), at 1537.68 and 5753.96 GDoF/s; per GPU,
  throughput rose 49.2-fold over a decade of code and hardware (details on
  [PyFR](/software/pyfr.md)).
- **A comparison target for explicit-filter LES** (Najafiyazdi et al.
  2023, §6.2, Fig. 10): the $N=1$ FR-DG, FR-OFR and FR-SD implicit LES of
  Bull & Jameson, printed as "128 degrees of freedom, i.e. p 1 Legendre polynomials on a 64³ grid",
  are less accurate in both energy- and vorticity-based dissipation than an
  approximate-deconvolution LES on a $64^3$ linear finite-element grid of
  the Taylor–Green vortex at $Re=1600$, as the source prints the two
  resolutions ([Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md);
  see [scale-similarity model](/methods/scale-similarity-model.md)).

## Low-order FR and the spectral-difference relative in a shock–turbulence comparison

In the multi-code comparison of [Chapelier et al. (2024)](/sources/chapelier-2024.md)
on the supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
($Re=1600$, $M_0=1.25$), the FR code H3AMR (HySonic Technology) runs on
unstructured meshes in a block-spectral form with $N+1$ Gauss–Legendre
points per direction and element, correction functions averaged over Radau
polynomials of different orders, a Rusanov interface flux and third-order
Runge–Kutta (§III.B.g). Its shock capturing is the "Block Spectral
Stresses" model, which computes sub-filter stresses, heat flux and pressure
work from the spectra of the velocity gradient, is activated by the energy
of the highest polynomial mode of momentum, and is meant to capture shocks
and model turbulence at once (see
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).
Run at second order ($N=1$, $32^3$ to $256^3$ elements, Table II), it
under-estimates the kinetic energy at $64^3$ degrees of freedom and gives
the lowest solenoidal dissipation of all solvers on every grid, the excess
numerical dissipation "typical of second-order upwind schemes" (§IV.A,
Figs. 5, 7); in the subsonic verification case it runs at fourth order and
agrees with the other codes (App. A). The comparison also includes
SD3DvisP, a fourth-order [spectral-difference](/methods/spectral-difference-method.md)
code on unstructured hexahedra
(Roe flux with entropy fix, centred viscous flux, subcell artificial
viscosity), which captures small scales well on coarse grids but whose
strong shock capturing "probably" hinders them on the finer ones (§III.B.e,
§IV.A, §V). High-order element methods resolve both large and small scales
better than second order in this compressible setting (§V). The PyFR
compressible FR code is named by [Kurz et al. (2025)](/sources/kurz-2025.md),
§1, among the GPU high-order solvers.

**Entropy-filtered FR on the same case.** Witherden et al. (2025, §5.1,
Figs. 11–12, Table 1) run PyFR on the supersonic Taylor–Green vortex at
$N=3$ on $16^3$ to $128^3$ hexahedra with Gauss–Legendre–Lobatto points and
entropy filtering, and compare with the Chapelier et al. data (supplied by
its authors): the solenoidal dissipation agrees "excellent[ly]" with the
$2048^3$ TENO reference at $128^3$ elements, and at equal resolution and
order the dilatational dissipation is closer to the reference than that of
CODA (modal DG, artificial viscosity), [FLEXI](/software/flexi.md) (DGSEM,
subcell finite volumes) and SD3D (spectral difference, artificial
viscosity), "indicating that the entropy filtering shock capturing approach
does not introduce excessive numerical dissipation" (see
[numerical dissipation](/properties/numerical-dissipation.md)). H3AMR is
not among the solvers of their Table 1.

**Spectral difference against FR.** [D'Ayer et al. (2026)](/sources/dayer-2026.md),
§1, cite earlier studies for the statement that the computing time of the spectral
difference method is equivalent to that of FR "under favourable
conditions" or slightly higher in some circumstances, and validate their
spectral-difference volume-penalization
[immersed boundary](/methods/immersed-boundary-method.md) against the
FR implementation of the same penalization by Kou et al. (2022) on a
laminar circular cylinder, with errors they call similar (§3.1).

## Qualifications

- Lv & Ekaterinaris (2023) print the symmetry of the correction functions as
  $g_L(\xi)=g_R(1/2-\xi)$ (Eq. 25). With their own end conditions (Eq. 24)
  this would require $g_R(1/2)=1$ and $g_R(-1/2)=0$, which those conditions
  do not give; the relation consistent with Eq. 24 on $[0,1]$ is
  $g_L(\xi)=g_R(1-\xi)$ *(compiler check, not in the sources)*.
- Vermeire (2024) prints the Taylor–Green initial pressure with
  $\cos(2z+2)$ (Eq. 17), while the pressure that satisfies the Poisson
  equation of the printed velocity field carries $(\cos2z+2)$
  *(compiler check, not in the sources)*; the ratio of specific heats in
  that equation is not defined for the incompressible system. The author
  calls $M_{\mathrm{AC}}$ the "incompressibility factor" in §2 and §4 and
  the "compressibility factor" in §4.3.
- Vandenhoeck et al. (2022) report the instability of high-order SST
  without the logarithmic variable from experience, with no figure (§1.1).
  Between Eqs. (82) and (83) they print the same face-solution symbol
  twice where the second should be the element's own value, and in §3.2.2
  write derivatives of $F^D$ where the interface flux $F^I$ is meant; the
  free-stream turbulence intensity of the Wieghardt plate, printed
  "$10^{-2}$" (§4.1), is ambiguous against the percent units that §3.3.2
  defines.

- Chapelier et al. (2024) print H3AMR's order as the number of points per
  direction ("$N$ = spatial order of accuracy", §III.B.g), here translated
  to the registry's degree $N$ (order $N+1$).
- Duan & Wang (2024) do not print the coefficient values used in the runs;
  only the "often estimated" $C_s=0.16$, WALE constant $0.325$ and the
  relation $c_v\approx\sqrt{2.5}\,C_s$ for the Vreman constant (§2.2–2.4).
  Their evidence is comparison of profiles and spectra; no error norms are
  tabulated.
- Duan & Wang (2024, §5.3) print $Re_\tau=u_\tau L/\nu$ for a channel they
  describe as based on $\delta$, with no $L$ defined.
- Wang (2024) is the arXiv v2 preprint of the Computers & Fluids paper; the
  robustness ranking of Riemann solvers is shown for this FR solver and
  filter only. The author's statement that the entropy filter needs no
  tuning (§4.3.2, §5) is qualified in §4.4.3, where the entropy tolerance is
  called a parameter.
- Dzanic et al. (2022) is the arXiv v1 preprint; it reports no
  de-aliasing test for its attribution of the $N=3$ oscillations to
  aliasing, and prints no timings for its statement that the high order
  comes "without a significant increase in computational effort" (§4).
- Brillon & Nadarajah (2026) is the arXiv v1 preprint (November 2024) of
  the Computers & Fluids paper; their evidence is two free-shear,
  nearly incompressible flows, and the recommendation against eddy-viscosity
  models rests on the Taylor–Green vortex at $96^3$, $N=5$. They use
  "iLES" for implicitly filtered LES *with* an explicit subgrid model and
  "ILES" for implicit LES without one (§1), a usage that differs from
  sources where the two abbreviations are synonyms. Their CFL limits use
  their own criterion (stable and non-increasing kinetic energy), and the
  timing comparison is for one code (PHiLiP) on one machine. The
  equivalences of ESFR with DG and spectral difference, and the filter
  interpretation of the correction parameter, are cited from earlier
  works, not derived there.
- Hamedi & Vermeire (2022) print the dissipative term of their Rusanov
  flux as $+\tfrac{s}{2}(u_L+u_R)$ (Eq. 44, $s$ the wave-speed estimate);
  with $u_L=u_R$ this does not reduce to the physical flux, so the
  consistent Rusanov form carries the jump of the states *(compiler check,
  not in the sources)*. The paper does not name the solver that ran the
  simulations, and its filters are tied to the DG-recovering correction
  function and the Rusanov flux (§3.4).
- Liu & Yuan (2023, §2.2) state, citing the VCJH literature, that the
  energy-stable schemes have "$(2K-1)$th order of super-accuracy with
  $K+1$ solution points" for linear advection ($K$ the degree), while
  Tonicello et al. (2023, §3) state a spatial superconvergence of order
  $2N+1$ for their fifth-order FR-SD; both are reported as printed. Liu & Yuan print the
  sum of Eq. 17 over $k$ with the coefficient indexed $j$; Tonicello et al.
  print $\mathbf C^0$ with $-(\alpha_{\mathrm T}-1)$ on the left correction
  term, where their preceding unnumbered equation gives
  $+(\alpha_{\mathrm T}-1)$ *(compiler check, not in the sources)*.
- Kiris et al. (2023, §VI 1c) say the implicit codes used time steps "only
  about 10× larger" than the explicit ones; from their Table 2 the hpMusic
  step ($9.7\times10^{-5}$) is 1.7–3.3 times the explicit steps
  ($2.9$–$5.7\times10^{-5}$) *(compiler check, not in the sources)*.
- Ims & Wang (2023) report no error norms, cell counts, time steps or
  timings; their ranking of indicators rests on visual comparison of
  fields and spectra.
- **Printed slips (Gao et al. 2025b).** The friction velocity is printed
  $u_\tau=U/yF^{-1}(Re_y)$ (Eq. 19), while $F^{-1}$ returns $y^+$, so the
  dimensionally consistent form is $u_\tau=\nu F^{-1}(Re_y)/y$; the
  pressure-gradient velocity is printed $u_p=(\nu/\rho)|\partial p_w/\partial x_i|$
  (Eq. 20), a velocity cubed; Eq. (31) omits the factor $u_p/u_c$ that
  solving Eq. (28) for the wall stress gives *(compiler checks, not in the
  sources)*. The $Re=37\,000$ run is described as "128 × 48 × 60 points"
  on $32\times12\times16$ elements at $N=3$, which with $N+1=4$ points
  per direction gives $128\times48\times64$ *(compiler check, not in the
  sources)*;
  the value of $C_2$ in each case, the constants $\kappa$, $C$, $\alpha$,
  $\beta$ of the Shih functions and the fourth coefficient of the last fit
  branch are not printed.
- Witherden et al. (2025, §2) print the correction term of Eq. (7) as
  $\mathfrak F_\alpha f^{(f_\perp)}-f^{(f_\perp)}$, without the tildes and
  the "C" superscript of the common flux of Eq. (5) and with a stray "$*$";
  the description above follows their text. They identify under-resolved
  DNS with ILES (§3.2), as Dzanic et al. (2022) do.

# Citations

- [Duan & Wang (2024)](/sources/duan-2024.md) — Abstract; §1, Fig. 2 (limiting amount); §2.1–2.4 (governing equations, SGS models); §3, Eqs. (16)–(30) (FR/CPR, element-averaged eddy viscosity, zero interface SGS flux, filter widths d1–d3); §4, Fig. 4 (wall model on FR); §5.1–5.4, Figs. 5–15; §6.
- [Wang (2024)](/sources/wang-2024-b.md) — arXiv v2: §2.2, Eqs. (9)–(16) (FR with DG-recovering correction, Riemann solvers, LDG); §2.3 (solution filtering); §2.4.2 (wall flux); §3 (ATHOS); §4.1, Figs. 2–3; §4.2, Eq. (26); §4.3, Tables 5–8; §4.4.3; §5.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — arXiv v1: §2.2, Eqs. (18)–(22) (Huynh FR, correction functions, generalization of nodal DG); §2.3 (PyFR, Rusanov, BR2, RK4, equal degrees of freedom); Eq. (26); §3.1–3.2, Figs. 3–5, 11–13; §4.
- [Saini et al. (2023)](/sources/saini-2023.md) — §1 (relayed cost and accuracy comparisons of FR against finite volumes).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.e, g, Tables I–II (H3AMR flux reconstruction, Block Spectral Stresses, SD3DvisP spectral difference); §IV.A, Figs. 5, 7; §V; App. A.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §1 (PyFR among GPU high-order codes).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §1 (FR lineage, ESFR, equivalences, iLES/ILES); §2.6–2.10, Eqs. (46)–(90) (SGS models, NSFR split form, Ismail–Roe flux, SSP-RK3, added Riemann dissipation, strong DG with over-integration); §3.1.1–3.1.8, Tables 1–5, Figs. 2–20 (Taylor–Green DNS and implicit LES: stability, cost, flux nodes, correction parameter, CFL, two-point fluxes, upwinding, SGS models); §3.2, Table 6 (Comte-Bellot–Corrsin).
- [D'Ayer et al. (2026)](/sources/dayer-2026.md) — HAL hal-05075852v1: §1 (spectral difference against FR cost, cited); §3.1 (comparison with the FR penalization of Kou et al.).
- [Liu et al. (2022b)](/sources/liu-2022-g.md) — §2.1–2.2, Eqs. 1–11, Fig. 1 (ALE FR/CPR on triangles, GCL compensation, physical-space correction field); §3.1.1, Table 1 (order on deforming grids); §4 (turbulence as future work).
- [Ruggeri et al. (2022)](/sources/ruggeri-2022.md) — §VI, Fig. 7 (fourth-order FR shock tubes with learned fluxes).
- [Wang et al. (2013)](/sources/wang-2013.md) — §1 (Huynh cited); §5, Tables II–IV, VII (CPR–DG submissions to the first High-Order CFD Workshop).
- [Vandenhoeck et al. (2022)](/sources/vandenhoeck-2022.md) — Abstract, §1–1.1 (first FR-RANS with transition, $\ln\omega$ SST); §2, Eqs. (47)–(61) (FR, VCJH, BR2, AUSM$^+$-up); §3.2, Eqs. (62)–(87), Figs. 5–7 (implicit solver, semi-analytical and source Jacobians); §3.3.1, Eq. (88); §4.1–4.3, Figs. 9–17 (Wieghardt plate, T3 cases, VCJH parameters, $O(N^2)$ cost).
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §1, §2.1–2.2 (DG-recovering FR, LCP, geometric aliasing, dissipation as SGS model); §3.2–3.4 (time-step-independent modal filter, optimization, scope); §4.1–4.3, Table 1; §5.1–5.2, Tables 2–3, Figs. 23–25; Eq. 44.
- [Ims & Wang (2023)](/sources/ims-2023.md) — §2 Eqs. 1–6 (FR/CPR, BR2, limiter, SSP-RK3/BDF2OPT, ILES); §3.1, §4 (indicators, mortar faces); §5.1–§5.3.
- [Shi & Yan (2023)](/sources/shi-2023.md) — §I; §II.A Eqs. 2–5; §II.B Eqs. 6–18 (KXRCF, P-weighted WENO, positivity); §III.A–B Figs. 1–3; §IV.A–C Table IV.
- [Liu & Yuan (2023)](/sources/liu-2023-b.md) — §2.1–2.2 Eqs. 8–21 (1-D FR, VCJH); §3 (a posteriori subcell limiter, KXRCF pre-detection); §5, §5.5 Table 2 Fig. 9.
- [Tonicello et al. (2023)](/sources/tonicello-2023.md) — §2.1 Eqs. 4–11; §2.2 Eqs. 13–23; §3 Figs. 2, 4–9; §4.2–§4.3; §5; App. Figs. 29–30.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — Table 1, Table 2, §III, §VI 1a, §VI 1c.
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) — §6.2, Fig. 10.
- [Vermeire (2024)](/sources/vermeire-2024.md) — §1–§2, Eqs. (1)–(5) (EDAC); §3, Eqs. (6)–(13) (FRDG in lifting-collocation-penalty form, metrics, Rusanov/BR2, time integrators); §4.1–§4.3, Figs. 3–21, Tables 1–3 (Taylor–Green, channel, SD7003); §5; Eq. (17).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §3.3, Eqs. (23)–(27) (one-dimensional FR, correction functions, energy-stable FR, PyFR); §4.2 (limiter-assisted FR LES of the CRM, as cited).
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §2, Eqs. (1)–(7), Fig. 1 (FR recap, point sets, FR as a discontinuous spectral element method); §3.2 (four stabilization strategies); §3.4 (conservative metric); §3.5–§3.6; §5.1, Figs. 11–12, Table 1 (supersonic Taylor–Green comparison); §5.2, Tables 2–3 (scaling).
- [Gao et al. (2025b)](/sources/gao-2025-b.md) — §I (input point and wall condition of earlier DG/FR WMLES, as cited); §II A, Eqs. (1)–(10) (FR/CPR, LDDRK); §II B (Vreman); §II C, Eqs. (17)–(32), Fig. 1, App. A (first-solution-point input, non-iterative wall laws); §II D, Eqs. (33)–(37), Fig. 2 (no-slip wall, hybrid inviscid wall flux); §III A–B, Figs. 3–15 (channel, periodic hill, cost); printed slips in Eqs. (19), (20), (31), §III B2.
- [Okano & Haga (2026)](/sources/okano-2026.md) — §1; §2.1 (LS-FLOW-HO: Radau FR, Gauss–Legendre points, SLAU, BR2, SSPRK(4,3), no SGS model); §3, Figs. 2–4 (wall-normal modal filter failing on cold walls); §4; §5.4, Table 4 ($N=1$–3 at matched degrees of freedom).
