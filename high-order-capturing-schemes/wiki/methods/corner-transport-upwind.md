---
type: Method
title: "Corner transport upwind (CTU)"
description: "Colella's unsplit, single-step Godunov scheme: edge states carry a transverse correction from transverse Riemann fluxes, so the data swept in through cell corners is upwinded and the Courant limit is that of operator splitting (the largest directional Courant number at most 1), against the sum-form limit of donor cell; second order by characteristic tracing of limited slopes, at twice the Riemann solves of splitting in 2D and 12 (or 6, without corner coupling) in 3D."
status: established
aliases: [CTU, corner-transport-upwind, unsplit Godunov method, Colella's unsplit scheme, corner coupling]
tags: [godunov, unsplit, multidimensional, finite-volume, cfl]
timestamp: 2026-10-13T00:00:00Z
---

# Corner transport upwind (CTU)

**What it is** ([Colella (1990)](/sources/colella-1990.md), §§1–2). A
conservative, second-order, **unsplit** Godunov-type scheme in 2D: all
fluxes are computed and differenced in one step from the characteristic
form of the full multidimensional equations at each edge, with no
operator splitting. Its first-order member for scalar advection is
*corner transport upwind*. Its design criteria (p. 173): on a
grid-aligned 1D problem it reduces to the second-order Godunov method of
Colella and Woodward ([PPM](/methods/ppm.md) line); the unlimited
second-order scheme and the fully limited first-order scheme have the
same linear CFL limit, equal to that of operator splitting; the fully
limited scheme obeys a maximum principle for linear advection. TVD is
rejected as a multi-D criterion because it implies at most first order
(Goodman and LeVeque, cited there;
[total variation diminishing](/properties/total-variation-diminishing.md)).

## Scalar advection

For $\partial_t u + \mathbf v\cdot\nabla u = 0$ with constant
$\mathbf v = (v_x, v_y)$, $v_x, v_y > 0$, the new average is the average
of the piecewise-constant data over the cell traced back along the
characteristics, corners included: four cells contribute, with
nonnegative weights (eq. 1.2, Figs. 1–2). In conservation form
(eqs. 1.3–1.4),
$$\bar u^{n+1}_{i,j} = \bar u^n_{i,j} + \frac{v_x\Delta t}{h_x}\left(u^{n+1/2}_{i-1/2,j} - u^{n+1/2}_{i+1/2,j}\right) + \frac{v_y\Delta t}{h_y}\left(u^{n+1/2}_{i,j-1/2} - u^{n+1/2}_{i,j+1/2}\right),$$
$$u^{n+1/2}_{i+1/2,j} = \bar u^n_{i,j} + \frac{v_y\Delta t}{2h_y}\left(\bar u^n_{i,j-1} - \bar u^n_{i,j}\right),\qquad u^{n+1/2}_{i,j+1/2} = \bar u^n_{i,j} + \frac{v_x\Delta t}{2h_x}\left(\bar u^n_{i-1,j} - \bar u^n_{i,j}\right).$$
Donor cell is the same update without the transverse term; Colella
describes it as donor cell minus a term that, to leading order in the
truncation error, is always destabilizing (p. 175).

**Courant limits** (eqs. 1.5–1.6, p. 175):
$$\text{CTU:}\ \max\left(\frac{v_x\Delta t}{h_x},\ \frac{v_y\Delta t}{h_y}\right) \le 1,\qquad \text{donor cell:}\ \frac{v_x\Delta t}{h_x} + \frac{v_y\Delta t}{h_y} \le 1,$$
the first stated as sufficient, the second as necessary, "as is easily
checked using Fourier analysis". At equal directional Courant numbers
the donor-cell (sum) form allows each only $\tfrac12$; the corner-coupled
scheme allows 1, the limit of operator splitting.

**Second order** (eqs. 1.8–1.9, p. 176). The edge state adds a limited
normal slope,
$$u^{n+1/2}_{i+1/2,j} = \bar u^n_{i,j} + \left(\tfrac12 - \frac{v_x\Delta t}{2h_x}\right)\delta^{\mathrm{MC}}\bar u_{i,j} - \frac{v_y\Delta t}{2h_y}\left(\bar u^n_{i,j} - \bar u^n_{i,j-1}\right),$$
with $\delta^{\mathrm{MC}}\bar u_{i,j}$ the monotonized-central slope taken
in $x$. The normal slope is MC-limited, the transverse difference upwind
and unlimited; this asymmetry makes the fully limited scheme reduce to
first-order CTU. Under the CTU limit the second-order scheme amplifies no
Fourier mode, checked numerically on the amplification factor (p. 176).

## Systems

The characteristic relation on multidimensional characteristic surfaces
is a 1D characteristic equation normal to an edge with the tangential
derivatives as source terms (eqs. 2.3–2.4); the scheme discretizes this
structure (§2, p. 179):
1. *Limited slopes* in each direction, by characteristic limiting after
   Harten: the central and the doubled one-sided differences are expanded
   on the $r^{(p)}$, each field's coefficient is limited
   minmod-fashion with the sign of the central one (zero if the one-sided
   ones differ in sign), and the slope is recombined (eqs. 2.5–2.6;
   [characteristic decomposition](/methods/characteristic-decomposition.md)).
2. *Normal predictor.* Time-centred left and right edge states by
   characteristic tracing; components of waves not moving toward the edge
   are discarded, with reference states taken from the farthest-reaching
   wave, which gives the [PPM](/methods/ppm.md)-style tracing for
   piecewise-linear data (eqs. 2.7–2.12).
3. *Transverse correction.* Each normal-predicted state is corrected by
   $-\tfrac{\Delta t}{2h_y}$ times the difference of the $y$-fluxes of
   two transverse Riemann problems (eq. 2.14). Their inputs are either
   the cell averages on each side of the transverse edges (eq. 2.13),
   transverse first-order Godunov, which is "sufficiently accurate" for
   second order; or the normal-predicted states of those edges
   (eq. 2.15), recommended for moderately strong oblique discontinuities.
4. *Normal Riemann problem* with the corrected states, then the
   conservative update with all edge fluxes at once.

For constant coefficients the edge value satisfies finite-difference
approximations to the characteristic relations through the edge whatever
the reference states, and for smooth nonlinear solutions up to
second-order terms (eq. 2.16).

**System Courant limit** (eq. 2.17): the largest directional Courant
number over all fields and cells at most 1. It is proved necessary and
sufficient, for the limited and the unlimited scheme, only when the two
directional Jacobians commute; otherwise it is unproved but was used as
the gas-dynamics time-step control with "no evidence of instability".

**Mapped grids and gas dynamics** (§§3–4). The scheme extends to smooth
quadrilateral grids with the same predictor in mapped coordinates; the
metric term is differenced to cancel the transverse flux difference
exactly when there are no transverse gradients (eq. 3.10), and the
Courant condition becomes: a wave normal to an edge must not reach the
opposite edge in $\Delta t$ (eq. 3.12). For Euler the predictor runs in
primitive variables with explicit eigenvectors, the slopes come from a
fourth-order limited central difference, one flattening coefficient,
the minimum over the two directions, multiplies the slopes in both, and
reflecting walls use mirror states. The numerical domain of dependence
is a $9\times9$ block, so 4 ghost cells are needed.

## Cost and three dimensions

* **2D** (§6, p. 198). Twice the Riemann solves of operator splitting,
  about 50 % more time; about 24,000 zones per CPU second on a vectorized
  Cray 1.
* **3D** (§6, p. 199). The full 3D analogue of the corner-averaging
  scheme needs **12** Riemann solves per zone per step, against **3** for
  splitting. Relaxing the maximum-principle criterion, with donor-cell
  transverse predictors that drop the corner-coupling (third-order
  truncation) terms, needs **6**. Both reduce to the 2D scheme on
  grid-aligned 2D problems; which is appropriate is "undoubtedly problem
  dependent". **No 3D Courant limit is stated.**

## Evidence

* *Double Mach reflection* at $400\times100$, $h_x = h_y = 1/100$,
  $t = 0.2$: the unsplit and the operator-split runs are "essentially
  identical", visually, with no error norm. The unsplit one needed
  "a considerable degree of care": the transverse inputs of eq. 2.15
  rather than 2.13 (or the wall jet loses resolution), careful
  reflecting-wall conditions, and multidimensional flattening against
  low-amplitude post-shock noise, where splitting needed only 1D
  flattening per sweep (§5, Figs. 8–10;
  [double Mach reflection](/benchmarks/double-mach-reflection.md)).
* *Steady regular shock reflection* (Yee, Warming and Harten's set-up):
  shocks about 2–2½ zones wide normal to the shock; without flattening,
  low-amplitude oscillations (§5, Figs. 5–7).
* The unsplit scheme matches the split one in resolution and is more
  sensitive to implementation details (§6).

## Use in this corpus

* *CTU-GLM.* Mignone and Tzeferacos build their cell-centred GLM-MHD
  scheme on Colella's CTU integrator with 6 Riemann solves per zone,
  Courant number below 1 in 2D and below 1/2 in 3D (defaults 0.8 and
  0.4), and call multidimensional source terms in the normal predictors
  "of crucial importance" ([Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md),
  §3.1; [hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)).
  The 6-solve count is Colella's reduced 3D variant, without corner
  coupling; the 3D limit of 1/2 is theirs, since Colella states none.
  PLUTO hosts the CTU-GLM, CTU-EGLM and CTU-CT schemes they compare
  ([PLUTO](/software/pluto.md)).
* *Unsplit base schemes of cut-cell codes.* An unsplit piecewise-linear
  Godunov scheme credited to Colella (1990) and Saltzman (1994)
  ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2–3),
  and "Colella's unsplit MUSCL" ([Berger & Giuliani (2021)](/sources/berger-2021.md), §3;
  [cut-cell finite volume](/methods/cut-cell-finite-volume.md)).
* *Split schemes that point to it.* Zachary, Malagoli and Colella's MHD
  scheme is Strang-split and announces a fully unsplit version after
  Colella (1990) as future work ([Zachary, Malagoli & Colella (1994)](/sources/zachary-1994.md),
  pp. 264, 283). Dai and Woodward's face-field update can follow "an
  unsplit $L_{\Delta t}$" credited to Colella and Saltzman, but their
  demonstration is split, and only the face field must be updated
  unsplit ([Dai & Woodward (1998)](/sources/dai-1998.md), §§2–2.1;
  [constrained transport](/methods/constrained-transport.md)).
* *Unsplit limits without corner coupling.* With RK3, FV-WENO is stated
  stable up to Courant number 1/2 in 2D, "as unsplit Godunov"
  ([Titarev & Toro (2004)](/sources/titarev-2004.md), §2); by eqs. 1.5–1.6
  that is the sum-form (donor-cell) limit, not CTU's
  ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)). A fourth-order
  method-of-lines scheme states its RK4 limit in the same sum form, "with
  no corner coupling" ([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), eq. 57;
  [fourth-order finite volume](/methods/fourth-order-finite-volume.md)).
* *AMR.* Colella reports that the gas-dynamics algorithm has been used in
  adaptive-mesh-refinement calculations, citing Berger and Colella (§5).
  Berger and Colella call their integrator "a second-order Godunov
  method" by Colella and do not say whether it is split or unsplit
  ([Berger & Colella (1989)](/sources/berger-1989.md), §§1, 5, 7), so the
  two papers together do not establish that their runs used CTU.

# Citations

1. [Colella (1990)](/sources/colella-1990.md), §§1–6, eqs. 1.2–1.9, 2.3–2.17, 3.10, 3.12, Figs. 1–2, 5–10 (equations read from page images).
2. [Mignone & Tzeferacos (2010)](/sources/mignone-2010-b.md), §3.1.
3. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§2–3 (arXiv v1).
4. [Berger & Giuliani (2021)](/sources/berger-2021.md), §3 (arXiv v1).
5. [Zachary, Malagoli & Colella (1994)](/sources/zachary-1994.md), pp. 264, 283.
6. [Dai & Woodward (1998)](/sources/dai-1998.md), §§2–2.1, 4.
7. [Titarev & Toro (2004)](/sources/titarev-2004.md), §2.
8. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), eq. 57.
9. [Berger & Colella (1989)](/sources/berger-1989.md), §§1, 5, 7.
