---
type: Method
title: "Spectral difference method"
description: "The spectral difference method is a nodal high-order discontinuous scheme in differential form: a degree-N solution polynomial on solution points, a degree-(N+1) flux polynomial on staggered flux points with common interface fluxes, and flux derivatives at the solution points; sources limit it with TENO/WENO Hermite reconstructions or entropy filters."
status: established
aliases: [SD, SD method, spectral difference, nodal spectral difference, SD3, SD4]
tags: [dg, flux-reconstruction, limiting, teno]
timestamp: 2026-10-23T23:55:00Z
---

# Spectral difference method

The spectral difference (SD) method, as recalled by
[Chen & Fu (2024)](/sources/chen-2024.md) after Kopriva & Kolias and Liu, Vinokur & Wang
(§2, Eqs. (1)–(11)), discretizes $\partial_tu+\sum_d\partial_{x_d}f^{(d)}(u)=0$ in differential
form on each element. The solution is a polynomial of degree $N$ in each direction, stored
by its values at $N+1$ **solution points** (SPs); the flux is a polynomial of degree $N+1$
interpolated from its values at $N+2$ staggered **flux points** (FPs), which include the two
element faces. At the face FPs the two-sided flux is replaced by a common numerical flux;
the update of each SP value is the derivative of the flux polynomial evaluated there. SD is
a member of the family that [flux reconstruction](/methods/flux-reconstruction.md) unifies:
energy-stable FR recovers DG, SD and spectral-volume schemes through the choice of the
correction function, as recalled by [Cicchino et al. (2022)](/sources/cicchino-2022.md) (§1–2).

## The scheme

Chen & Fu map each quadrilateral isoparametrically to the reference square
$[-\tfrac12,\tfrac12]^2$ (§2). In one reference direction:

- **Solution points** $\xi_j=-\tfrac12\cos\Big(\dfrac{(2j+1)\pi}{2(N+1)}\Big)$,
  $j=0,\dots,N$ (Eq. (3), translated from the source's count of $N+1$ points). The source
  calls them "the Gauss points"; the formula gives Chebyshev–Gauss points *(compiler check,
  not in the sources: for $N=2$ it gives $0,\pm\sqrt3/4\approx\pm0.433$, against the
  Gauss–Legendre $0,\pm\sqrt{15}/10\approx\pm0.387$ on $[-\tfrac12,\tfrac12]$)*.
- **Flux points** $\xi_{-1/2}=-\tfrac12$, $\xi_{N+1/2}=\tfrac12$ and the $N$ roots of the
  Legendre polynomial of degree $N+1$ on the reference interval (page-local half-integer
  indices for FPs).
- The solution is $u_h=\sum_{j}\sum_{k}u^{j,k}\,\ell_j(X)\ell_k(Y)$ with
  Lagrange bases $\ell_j$ on the SPs ($(X,Y)$ the reference
  coordinates, page-local), and the flux is
  $f_h=\sum_k\sum_{r=-1}^{N}f^{r+1/2,k}\,\ell_{r+1/2}(X)\ell_k(Y)$ with Lagrange bases
  $\ell_{r+1/2}$ on the FPs (Eqs. (4)–(7)).
- Interior FP fluxes are the physical flux of the interpolated solution,
  $f^{r+1/2,k}=f\big(u_h(\xi_{r+1/2},\xi_k)\big)$; at the faces a common flux is used, the
  [local Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md) in Chen & Fu (Eqs. (8)–(10)).
- The derivative at the SPs on a uniform mesh is (Eq. (11))

$$\Big(\frac{\partial f}{\partial x}\Big)_{j,k}=\frac1{\Delta x}\sum_{r=-1}^{N}f^{r+1/2,k}\,\ell'_{r+1/2}(\xi_j).$$

Chen & Fu integrate in time with Ruuth's five-stage third-order
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) scheme, with
$\Delta t=\dfrac{\nu}{2N+1}\dfrac{\Delta x}{a}$ and $\nu=0.3$ in all tests (§3, Eq. (12)).
They name the schemes by order: SD3 ($N=2$) and SD4 ($N=3$). They state that the staggered
flux points give SD additional stability without filtering or de-aliasing (§1), and that a
nodal representation needs $(N+1)^2$ degrees of freedom per 2D cell against
$(N+1)(N+2)/2$ for a modal one, so nodal methods need limiting strategies of their own (§1).

## Shock capturing for SD

**TENO-based limiter and troubled-cell indicator** (Chen & Fu 2024). The limiter acts on lines
of solution points, dimension by dimension, and uses only the target cell and its two face
neighbours (§7, Algorithm 1). From the nodal data it computes, by quadrature, the cell
averages and the cell-averaged first and second derivatives of the neighbouring SD
polynomials, and builds [Hermite](/methods/hermite-weno.md) candidates: three quadratics
(3-DoF reconstruction, SD3 and SD4) and, for SD4, four cubics (4-DoF). The limited
polynomial is a direct convex combination of the candidates, with linear weights from
Taylor matching of the cell-averaged derivatives at the SD solution points:
$d_k=(\tfrac8{31},\tfrac{15}{31},\tfrac8{31})$ for SD3, $(\tfrac14,\tfrac12,\tfrac14)$ for
the SD4 3-DoF set and $(\tfrac5{14},\tfrac5{14},\tfrac17,\tfrac17)$ for the cubics (Eqs.
(49), (50), (54)). The weights depend on the SP distribution. The nonlinear weights are of WENO-JS type or
[adaptive TENO](/methods/adaptive-teno.md) type with an adaptive cut-off $C_T$; a
[scale sensor](/definitions/scale-sensor.md) with cut-off $0.6$ triggers a
compression towards the cell average at strong shocks, and a
[Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md) at the flux points is needed only
in the double Mach reflection (§§5–9). The limiter leaves cell averages unchanged (Eq. (75)).
Details are on [WENO limiters for DG](/methods/weno-limiter-dg.md) and
[troubled-cell indicators](/definitions/troubled-cell-indicator.md): Chen & Fu's
TENO indicator flags $x$ and $y$ independently, so a cell can be limited in one direction
only, and on the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) it detects the
shocklets that the KXRCF indicator misses (§4.2, §9.3). On 2D density-wave advection with every
cell limited, all limiters keep the design order, e.g. $L_1$ orders $3.03$, $3.08$ for SD3
with TENO3-A and $4.13$, $4.09$ for SD4 with TENO4-A (Table 1). Combining the third-order limiter
with SD4 degrades the solution against SD3 with the same limiter, so a fourth-order limiter is
needed (§9.4, stated from experiments not shown).

**Entropy filtering** ([Peyvan et al. 2023](/sources/peyvan-2023.md)). Peyvan et al.
stabilize SD, like FR, with the positivity-preserving
[entropy-based adaptive modal filter](/methods/entropy-filtering.md) of Dzanic & Witherden,
with entropy threshold $10^{-4}$ (§1, §4). In their one-dimensional comparisons at $N=3$:

- on the [Leblanc shock tube](/benchmarks/leblanc-shock-tube.md) (1000 elements) SD has the
  largest oscillations and undershoots of all methods compared, which the authors attribute to
  its flux polynomial of degree $N+1$; FR and SD resolve the contact more sharply than the
  entropy-stable [DGSEM](/methods/dgsem.md) with subcell blending (§4.1, Fig. 1);
- on their Mach-10 variant of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md)
  (170 elements) SD and FR miss the dip at $x=2.82$ that the DGSEM resolves (§4.2, Fig. 2);
- on a three-species reacting [Sod problem](/benchmarks/sod-and-lax-shock-tubes.md) FR and SD
  agree better with the reference than WENO and the DGSEM but oscillate, SD with a large
  $\mathrm O_2$ undershoot (§4.3, Fig. 3);
- on the five-species non-equilibrium Sod problem FR and SD are unstable, because the filter finds no strength that keeps
  the five species densities and the pressure positive and satisfies the entropy criterion at
  once (§4.5.1, stated, no figure).

The authors also state that, in their experience, artificial viscosity cannot stabilize the
high-order spectral methods for shock waves with high pressure ratios (§4.1).

## Qualifications

- Chen & Fu's linear weights are tied to their Chebyshev–Gauss solution points; other point
  sets give other coefficients (Eqs. (30)–(35)). *(Compiler check, not in the sources.)* The
  printed conditions $-\tfrac{11}{96}d_0+\tfrac5{24}d_1-\tfrac{11}{96}d_2=\tfrac1{24}$ (Eq. (43)),
  $d_0=d_2$ (Eq. (48)) and $\sum_kd_k=1$ give $d_0=\tfrac8{31}$, $d_1=\tfrac{15}{31}$.
- The two sources agree that SD resolves discontinuities sharply and needs an added
  stabilization, and differ only in which one: Chen & Fu use troubled-cell detection with
  nonlinear Hermite limiting on 2D Euler problems, Peyvan et al. use a modal entropy filter
  in 1D strong-shock and reacting problems. Their statements about robustness concern
  different stabilizations and are not competing claims about one scheme.

# Citations

- [Chen & Fu (2024)](/sources/chen-2024.md) — §§1–3, §§5–9, Eqs. (1)–(12), (49), (50), (54), (75), Algorithm 1, Table 1.
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §1, §§4.1–4.3, §4.5.1, Figs. 1–3.
- [Cicchino, Nadarajah & Del Rey Fernández (2022)](/sources/cicchino-2022.md) — §§1–2 (ESFR recovers DG, SD and spectral volume).
