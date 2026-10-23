---
type: Method
title: "MUSCL and MUSCL–Hancock schemes"
description: "MUSCL reconstructs limited piecewise-linear states from cell averages, in a one-parameter κ family; MUSCL–Hancock adds a half-step predictor of the boundary values and one Riemann solve per interface, a second-order single-step scheme that the bundle's AMR, immersed-boundary and multiphase solvers use as their base discretization."
status: established
aliases: [MUSCL, MUSCL reconstruction, kappa scheme, κ-scheme, MUSCL–Hancock method, MHM, van Leer MUSCL]
tags: [reconstruction, limiting, finite-volume, riemann-solver]
timestamp: 2026-10-23T11:06:00Z
---

# MUSCL and MUSCL–Hancock schemes

**MUSCL** reconstruction (after van Leer, as recalled by the sources) replaces the cell average
$\bar u_i$ by a limited linear function in each cell and evaluates it at the two faces; the
interface states feed a two-point flux $h(u^-_{i+1/2},u^+_{i+1/2})$. **MUSCL–Hancock** makes
the scheme second order in time within a single step: the two boundary values of each cell are
advanced by half a time step with the physical flux before the Riemann problems are solved.
In this bundle neither is a subject of study; both are the base discretization of
second-order finite-volume solvers into which the sources' contributions are built — adaptive
mesh refinement on curvilinear meshes, an immersed-boundary method, a multiphase model.

## The κ family of limited reconstructions

[Nguyen et al. (2022)](/sources/nguyen-2022.md) (§2.3, Eqs. (26)–(27)) use, with
$\Delta_{i+1/2}=\bar u_{i+1}-\bar u_i$ (page-local) and the slope ratio $r_i$ and limiter $\psi$
of [TVD and slope limiters](/definitions/total-variation-diminishing.md),

$$u^-_{i+1/2}=\bar u_i+\tfrac14\Big[(1-\kappa_{\mathrm M})\,\Delta_{i-1/2}\,\psi(r_i)+(1+\kappa_{\mathrm M})\,\Delta_{i+1/2}\,\psi(1/r_i)\Big],$$

and the mirror formula for $u^+_{i+1/2}$ from cell $i+1$, with $\kappa_{\mathrm M}=1/3$, which they call the
"third-order" upwind-biased extrapolation; the overall spatial scheme is stated to be second
order in multiple dimensions (page-local parameter $\kappa_{\mathrm M}$, the source's $\kappa$; not the
kinetic energy $\kappa$ of the registry). [Peng et al. (2022)](/sources/peng-2022.md)
(§2.4, Eqs. (15)–(17)) write the Cartesian reconstruction with a limiter factor $\varepsilon_i$
and a parameter $\omega$ (their symbols; registry $\psi$ and the $\kappa_{\mathrm M}$ above),
$\omega=0$ in all runs, and minmod as the limiter. *(compiler check,
not in the sources: their right-face value
$\bar u_i+\tfrac12\varepsilon_i(1-\omega)\delta_{i-1}\tfrac{\Delta x}2+\tfrac12\varepsilon_i(1+\omega)\delta_i\tfrac{\Delta x}2$,
with $\delta_i=\Delta_{i+1/2}/\Delta x$, is the $\kappa_{\mathrm M}$ formula above with $\kappa_{\mathrm M}=\omega$ and one
limiter factor for both differences; $\kappa_{\mathrm M}=\omega=0$ is the centred-slope case.)*

The variables reconstructed differ: primitive variables $(p,v,T,\phi_2,\dots,\phi_N)$ in the
multiphase model of Nguyen et al., with the over-compressive OverBee limiter on the volume
fractions and van Leer elsewhere; primitive or conservative variables in Peng et al.; primitive
variables in [Wang et al. (2022a)](/sources/wang-2022.md) (§2.1). On curvilinear meshes Peng et
al. divide the differences by physical centroid-to-face distances (Eqs. (18)–(20)); the
printed form is exact for linear data only where the two distances are equal, as worked out on
the TVD page.

## The Hancock predictor

As written by [Wang et al. (2022a)](/sources/wang-2022.md) (§2.1, Eqs. (4)–(6), after van Leer and
Toro), with a slope $\Delta_i$ per cell and page-local boundary values $u^{\mathrm L}_i$, $u^{\mathrm R}_i$
at the left and right faces of cell $i$:

1. **reconstruct:** $u^{\mathrm L}_i=\bar u_i-\tfrac12\Delta_i$, $u^{\mathrm R}_i=\bar u_i+\tfrac12\Delta_i$;
2. **evolve half a step:** $\bar u^{\mathrm{L,R}}_i=u^{\mathrm{L,R}}_i+\tfrac12\frac{\Delta t}{\Delta x}\big[f(u^{\mathrm L}_i)-f(u^{\mathrm R}_i)\big]$;
3. **solve the Riemann problem** at $x_{i+1/2}$ with $u^-_{i+1/2}=\bar u^{\mathrm R}_i$ and
   $u^+_{i+1/2}=\bar u^{\mathrm L}_{i+1}$, and update the averages in flux form.

The superscripts follow the cell, not the interface: $\mathrm R$ of cell $i$ is the left state
$u^-$ of $x_{i+1/2}$. For linear advection $f=au$ the flux is (Eqs. (7)–(8))

$$h^{\mathrm{MHM}}_{i+1/2}=\begin{cases}a\big[\bar u_i+\tfrac12(1-\nu)\Delta_i\big],&a>0,\\ a\big[\bar u_{i+1}-\tfrac12(1+\nu)\Delta_{i+1}\big],&a<0,\end{cases}$$

with the Courant number $\nu$ (signed in the source). *(compiler check, not in the sources: for
$a>0$ and the unlimited slope $\Delta_i=\bar u_{i+1}-\bar u_i$ this is the Lax–Wendroff flux, for
$\Delta_i=\bar u_i-\bar u_{i-1}$ the Beam–Warming flux, so the limiter interpolates between
second-order fluxes.)* Wang et al. do not state the slope or limiter. Peng et al. state that
MUSCL–Hancock gives "a scheme which is second-order accurate in space and time" (§2.4), with
the predictor not written out. Nguyen et al. do not use the Hancock step: they advance the
primitive variables with three-stage [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) through the
inverse Jacobian $[\partial u/\partial w]^{-1}$ (Eqs. (29)–(30); page-local primitive vector $w$).

**Quasilinear predictor on subcells.** In the a posteriori subcell limiter of the
primitive-variable ADER-DG scheme of [Gaburro et al. (2024)](/sources/gaburro-2024.md)
(§3.4, Eqs. (38)–(39)), the troubled subcells are recomputed by a MUSCL–Hancock scheme on
triangles, "equivalent to a second order ADER-FV scheme", written for the primitive vector
$w$ with its quasilinear matrices $A_{\mathrm p}$, $B_{\mathrm p}$ in $x$ and $y$ (page-local):
the predictor is
$\tilde w=w^n-(A_{\mathrm p}S_x+B_{\mathrm p}S_y)(t-t^n)+S_x(x-x_c)+S_y(y-y_c)$, $(x_c,y_c)$
the subcell barycentre, i.e. the time derivative is taken from the quasilinear system rather
than from flux differences; the slopes $S_x$, $S_y$ are chosen variable by variable by an ENO
rule, the candidate minimizing $S_x^2+S_y^2$. The corrector adds a volume term at
$t^{n+1/2}$ and [path-conservative](/methods/path-conservative-scheme.md) fluctuations at the
edge midpoints and $t^{n+1/2}$. In subcells flagged by their shock sensor the same predictor
feeds a **conservative** corrector, a Rusanov flux on the conserved variables (Eq. (67)),
which removes the conservation defect there (§4.4;
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md),
[MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)).

**Reconstructing an equilibrium variable.** The second-order well-balanced staggered scheme
of [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) (§2.3) is MUSCL-type without a Hancock
step: it reconstructs linearly the density, the equilibrium variable $\mathcal E(\rho)+z$
($\mathcal E$ the enthalpy-like potential, $z$ the topography or force potential, page-local)
and the velocity on the dual mesh; interface topography values
$z^\pm=(\mathcal E(\rho)+z)^\pm-\mathcal E(\rho^\pm)$ follow from the first two reconstructions; the limiters are called
"completely standard" and not specified, and only a forward-Euler step is written. The
reconstructed values feed hydrostatic reconstructions, and the source term needs a correction
to stay second order (see [well-balancing](/properties/well-balancing.md)).

## Where the sources use it

| Source | Solver and setting | Riemann solver | Contribution built on it |
|---|---|---|---|
| [Peng et al. (2022)](/sources/peng-2022.md) | [AMROC](/software/amroc.md)–Clawpack, multispecies reactive Euler, curvilinear block-structured AMR | AUSM, hybrid Roe/HLL | mapped-mesh slopes, area-weighted restriction, Newton-solved bilinear prolongation ([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)) |
| [Wang et al. (2022a)](/sources/wang-2022.md) | AMROC, Euler on Cartesian grids with level-set geometry | PVRS; HLL for the reactive case | bilinearly complete ghost-cell reconstruction ([immersed boundaries](/methods/immersed-boundary-method.md)) |
| [Nguyen et al. (2022)](/sources/nguyen-2022.md) | $N$-phase pressure–temperature equilibrium model | Rusanov, HLLC | MUSCL $\kappa_{\mathrm M}=1/3$ with compressive limiters (no Hancock step) |
| [Hu et al. (2022)](/sources/hu-2022.md) | Cartesian FV, Euler, dimension by dimension | HLLE, HLLEM, HLLC, RHLLEM | second-order MUSCL with second-order TVD Runge–Kutta, no Hancock step; MUSCL interface densities compete with THINC ones in a face-wise BVD selection ([HLL-family solvers](/methods/hll-riemann-solvers.md)) |
| [Lesur et al. (2023)](/sources/lesur-2023.md) | IDEFIX, HD and MHD on primitive variables | Rusanov, HLL, HLLC/HLLD, Roe | piecewise-linear reconstruction with the van Leer limiter (second order) beside LimO3 and PPM, with explicit RK2/RK3 ([IDEFIX](/software/idefix.md)) |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) | subcell limiter of primitive-variable ADER-DG, polygonal meshes, single- and multi-material Euler | path-conservative fluctuations; Rusanov in shock subcells | quasilinear Hancock predictor with ENO slopes; conservative corrector in shock-flagged subcells |
| [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) | staggered barotropic Euler and shallow water | kinetic-type split mass fluxes (no Riemann solver) | MUSCL on $\rho$ and $\mathcal E(\rho)+z$, well-balanced lake at rest including dry areas |
| [Başkaya et al. (2024)](/sources/baskaya-2024.md) | US3D (body-fitted) and CHESS (ghost-cell IB), reacting hypersonic flow | modified Steger–Warming; Steger–Warming flux-vector splitting | second-order MUSCL as the reference and the ghost-cell discretizations of an immersed-boundary assessment ([immersed boundaries](/methods/immersed-boundary-method.md)) |
| [Wakimura et al. (2024)](/sources/wakimura-2024.md) | six-equation two-phase model with infinite-rate relaxation, wave-propagation form, SSP-RK3 | HLLC fluctuations | method-of-lines MUSCL with the van Leer limiter (no Hancock step) as one candidate of a BVD selection against THINC, on quasi-primitive variables ([boundary variation diminishing](/definitions/boundary-variation-diminishing.md)) |
| [Dematté et al. (2024)](/sources/dematte-2024.md) | cell-centred semi-implicit all-Mach FV, ideal and visco-resistive MHD | Rusanov on the advective sub-system | second-order TVD MUSCL–Hancock with the van Leer limiter for the explicit advective terms, after Dumbser et al. ([semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)) |

Chemistry enters Peng et al.'s scheme by second-order Strang splitting with a semi-implicit
fourth-order generalized Runge–Kutta integrator, GRK4A (§2.1); see
[shock-induced combustion](/benchmarks/shock-induced-combustion.md) for their validation and
[HLL-family solvers](/methods/hll-riemann-solvers.md) for the fluxes.

## Accuracy actually observed

The formal second order is not measured as a global order in the three AMR, immersed-boundary
and multiphase sources; Hu et al. (2022) run no convergence study either (their order is the
formal one of MUSCL and RK2). The code paper is the exception:
[Lesur et al. (2023)](/sources/lesur-2023.md) (§4.2, Figs. 7–8) show second-order convergence
on linear MHD waves with piecewise-linear reconstruction and RK2 for all four Riemann solvers;
with HLLD, LimO3 and PPM (with RK3) have lower errors, but PPM stops converging at high
resolution, reaching about $10^{-2}$ for the slow mode, and the authors recommend LimO3, "as it
shows proper second order convergence for all of the resolutions we have tested".

- Peng et al.'s manufactured-solution test on stretched, skewed and distorted meshes with three
  static refinement levels (§3.1, Fig. 5) is read by the authors as second order; the paper
  prints no observed orders, only error curves against a second-order slope.
- Goudon & Minjeaud's second-order scheme reaches second-order $L^1$ accuracy on subcritical
  and supercritical shallow-water flow over a bump (§3.3.1, Fig. 13) and on a smooth steady
  test of Castro et al. (§3.3.4, Figs. 18–19), not on their transcritical test with a stationary
  shock, where the authors blame the shock and the limiter (Figs. 20–21), and gives an observed
  order of 1.8 on the 2D Thacker paraboloid (§3.5, Fig. 24).
- Dematté et al. (2024) (§4.1.2, Table 2) measure second order in **space** on a smooth MHD
  vortex with unlimited MUSCL–Hancock and a fixed $\Delta t=0.01$: $L_2(\rho)$ orders 1.573,
  1.854, 1.966, 1.992, 1.998 from $16^2$ to $512^2$ cells, error $3.647\times10^{-5}$ on $512^2$;
  the paper calls this "second order of accuracy in space" and leaves higher order in time to
  future IMEX Runge–Kutta work (§4.1.2).
- Gaburro et al. measure the order of the unlimited DG scheme only (their limiter never
  activates on the smooth vortex, §5.1.1), so their MUSCL–Hancock subcell scheme has no
  measured order.
- Wang et al.'s Prandtl–Meyer tests give boundary-region $L_2$ entropy orders between 1.13 and 1.37
  (1.36, 1.37, 1.35, 1.33 at deflections 20°–50° with their hybrid ghost-cell method, 1.13–1.25
  with the other two ghost-cell variants, Table 1), the order of the coupled scheme near an immersed wall, which they compare with
  about 1.14 reported by Pember et al. (§3.3).

## Qualifications

- Peng et al. state that the area-weighted restriction on mapped meshes is conservative but
  "may cause accuracy losses" when the areas of the refined cells do not sum to the coarse
  area (§2.5.2), a further limit on the second order of the composite scheme.
- Wang et al.'s observed orders mix the interior scheme with the immersed-boundary
  reconstruction, whose own local error they call second order on a Taylor argument; the
  tests do not separate the two.
- Wakimura et al. (2024) (Eqs. (27)–(28)) print the face values
  $u^-_{i+1/2}=\bar u_i+\tfrac12\psi(r)\,\Delta_{i+1/2}$ with $r=\Delta_{i+1/2}/\Delta_{i-1/2}$ and
  $u^+_{i-1/2}=\bar u_i-\tfrac12\psi(r')\,\Delta_{i-1/2}$ with $r'=\Delta_{i-1/2}/\Delta_{i+1/2}$, and the van
  Leer limiter $\psi(r)=(r+\lvert r\rvert)/(1+\lvert r\rvert)$. *(compiler check, not in the sources: with
  these ratios and $r>0$ the increments are $\Delta_{i+1/2}^2/(\Delta_{i-1/2}+\Delta_{i+1/2})$ and
  $\Delta_{i-1/2}^2/(\Delta_{i-1/2}+\Delta_{i+1/2})$, which do not come from one linear profile and are not
  van Leer's harmonic-mean slope $2\Delta_{i-1/2}\Delta_{i+1/2}/(\Delta_{i-1/2}+\Delta_{i+1/2})$; inverting each
  ratio recovers van Leer's MUSCL slope, so the printed ratios are inconsistent with the
  stated limiter.)*

# Citations

- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.3 (Eqs. (26)–(31)), §3.1.
- [Peng et al. (2022)](/sources/peng-2022.md) — §2.1, §2.3, §2.4 (Eqs. (15)–(20)), §2.5.2, §3.1 (Fig. 5) (accepted manuscript).
- [Wang et al. (2022a)](/sources/wang-2022.md) — §2.1 (Eqs. (4)–(11)), §3.3 (Table 1), §3.6.
- [Hu et al. (2022)](/sources/hu-2022.md) — §2.1, §4.2, §5.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.3, §4.2 (Figs. 7–8).
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §3.4 (Eqs. (38)–(39)), §4.4 (Eq. (67)), §5.1.1 (arXiv v1).
- [Goudon & Minjeaud (2024)](/sources/goudon-2024.md) — §2.3, §3.3, §3.5 (HAL wrap of the version of record).
- [Başkaya et al. (2024)](/sources/baskaya-2024.md) — §3.1–3.2 (author preprint).
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §3.2.2 (Eqs. (27)–(28)), §3.2.4, §3.3.
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §3.1, §4.1.2 (Table 2).
