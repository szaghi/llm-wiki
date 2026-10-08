---
type: Method
title: "Fourth-order finite-volume method with average–point conversions"
description: "The Colella-group fourth-order finite-volume scheme: cell averages are converted to point values (and back) with h²/24 Laplacian corrections, each face flux is one flux evaluation at a face-centre value plus a transverse-Laplacian correction (no Gauss points), limiting uses a modified Colella–Sekora PPM limiter, and classical RK4 advances the scheme; it extends to mapped grids, viscous fluxes and block-structured AMR."
status: established
aliases: [fourth-order FV, Colella–McCorquodale scheme, Chombo fourth-order method, average-to-point conversion]
tags: [finite-volume, fourth-order, multi-d, ppm, amr, mapped-grid]
timestamp: 2026-10-08T00:00:00Z
---

# Fourth-order finite-volume method with average–point conversions

**Idea.** Above second order, a finite-volume face flux must be a face
*average* of the flux. Instead of evaluating the flux at Gauss points,
this scheme uses one evaluation at the face centre plus a correction by
the transverse Laplacian, which is exact to fourth order. Averages and
point values are related by
$\bar u_i = u_i + \frac{h^2}{24}\Delta_h u_i + O(h^4)$ in each cell and
by the analogous identity on each face
([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §2.2;
[reconstruction from cell averages](/methods/finite-volume-reconstruction.md)).

## The single-level scheme

([McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §2,
extending Colella et al. 2011 to nonlinear systems; every formula
checked on the page images.) Reconstruction is in primitive variables
$\mathbf W = (\rho, \mathbf v, p)$. In the normal direction of a face:
1. Point values $u_i = \bar u_i - \frac{h^2}{24}\Delta_h\bar u_i$, then
   $\mathbf W_i = \mathbf W(u_i)$. The cell averages of the primitives are
   $\langle\mathbf W\rangle_i = \mathbf W_i + \frac{h^2}{24}\Delta_h\mathbf W(\bar u_i)$.
   The Laplacian acts on the second-order value $\mathbf W(\bar u_i)$ to
   keep the stencil small, at an $O(h^4)$ cost (eqs. 12–16).
2. Face averages from the centred four-point formula of
   [PPM](/methods/ppm.md),
   $\langle\mathbf W\rangle_{i+1/2} = \frac7{12}\left(\langle\mathbf W\rangle_i + \langle\mathbf W\rangle_{i+1}\right) - \frac1{12}\left(\langle\mathbf W\rangle_{i-1} + \langle\mathbf W\rangle_{i+2}\right)$
   (eq. 17), with one-sided fourth-order formulas at physical boundaries
   (eqs. 21–22).
3. Limiting gives the two interface states (below), and a Riemann solver
   gives the flux at the face centre.
4. Face centre value and face-averaged flux:
   $\mathbf W_{i+1/2} = \langle\mathbf W\rangle_{i+1/2} - \frac{h^2}{24}\Delta^\perp_h\langle\mathbf W\rangle_{i+1/2}$ and
   $\langle f\rangle_{i+1/2} = f(\mathbf W_{i+1/2}) + \frac{h^2}{24}\Delta^\perp_h f(\langle\mathbf W\rangle_{i+1/2})$
   (eqs. 18–20). The correction again uses the lower-order argument.
5. Classical RK4 in conservation form, with the total flux
   $\hat f^{\mathrm{tot}}_{i+1/2} = \frac16\left(\hat f^{(0)} + 2\hat f^{(1)} + 2\hat f^{(2)} + \hat f^{(3)}\right)_{i+1/2}$
   (eqs. 5–11). The method is not SSP. Its linear stability limit, from
   RK4 with first-order upwinding, is
   $\frac{\Delta t}{h}\sum_d\left(\vert\mathbf v\cdot\mathbf e_d\vert + c\right) \lesssim 1.3925$, with no
   corner coupling (eq. 57; [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

**Limiter** (§2.4.1). It is a modified Colella–Sekora extremum-preserving
PPM limiter, applied componentwise to primitives.
* PPM's first stage, which bounds the face value between neighbouring
  averages, is dropped: with RK4 it is redundant and too dissipative.
* Extrema are detected also from differences two cells apart, which is
  less sensitive to round-off.
* At an extremum the parabola is scaled by the ratio of a limited
  curvature to its own, with $C_2 = 1.25$.
* **Third-derivative test (new):** limit only if the variation of the
  third differences over four faces exceeds $C_3 = 0.1$ times their size.
  Without it, the original limiter fires at smooth multi-D extrema such
  as those of $x^3 - xy^2$ along $x = \pm y/\sqrt3$, and fourth order in
  the max norm is lost ([accuracy at critical points](/properties/accuracy-at-critical-points.md)).
* Away from extrema, PPM's overshoot reset in factor-2 form replaces
  Colella–Sekora's square-root formula (eqs. 33–34).

For strong shocks the extrapolants are flattened (Colella 1990) and a
fourth-order artificial viscosity is added. It is $O(h^4)$ in smooth
flow and reduces to PPM's at strong compressions; its two coefficients
are both 0.3 in all runs (§2.5).

**Results** (§4). Linear advection of a Gaussian converges at fourth
order in the max norm with the limiter on, and a square wave at about
0.8 in $L^1$, "as in" Colella–Sekora (Table 1). A Gaussian acoustic pulse
converges at fourth order with the limiter on or off (Table 2). Double
Mach reflection is "comparable to that of the best state-of-the-art
shock-capturing methods", with no set-up or error measure given
([double Mach reflection](/benchmarks/double-mach-reflection.md)).

## Mapped grids and viscous fluxes

([Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §§2–3; accepted
manuscript.) The same scheme runs on smoothly mapped grids for
$\mathcal J u$, with face averages of the metric-weighted fluxes, and
preserves free streams under moving refinement
([free-stream preservation](/properties/free-stream-preservation.md)).
For multispecies viscous flow with temperature- and composition-dependent
transport properties, face averages of products come from a fourth-order
product rule,
$$\langle w_1 w_2\rangle_{i+1/2} = \langle w_1\rangle_{i+1/2}\langle w_2\rangle_{i+1/2} + \frac{h^2}{12}\sum_{d' \ne d}\partial_{d'}w_1\,\partial_{d'}w_2\Big\vert_{i+1/2} + O(h^4)$$
(eq. 11, from Colella et al.), and face averages of the viscous flux
from its face-centre value plus $\frac{h^2}{24}$ times its second
tangential derivatives (eq. 14). The transport properties are then
evaluated pointwise at face centres instead of being averaged (§3.2,
five steps). Couette flow, a species-diffusion bubble and a stationary
viscous vortex converge at fourth order (Tables 1–3). Shocks need a
limiter in the inviscid flux, which this paper does not specify (§5).

**Block-structured AMR.** Both papers advance this scheme on Berger–Colella
hierarchies with subcycling. McCorquodale and Colella add conservative
refluxing of the total flux and ghost cells consistent with the
Runge–Kutta stages ([high-order AMR](/methods/high-order-amr.md)).

# Citations

1. [McCorquodale & Colella (2011)](/sources/mccorquodale-2011.md), §§2, 4 (equations checked on the page images).
2. [Owen, Guzik & Gao (2018)](/sources/owen-2018.md), §§2–5 (accepted manuscript).
