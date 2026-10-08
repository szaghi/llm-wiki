---
type: Method
title: "Alternative finite-difference WENO (AFD-WENO)"
description: "The second Shu–Osher finite-difference form: WENO-interpolate point values to interfaces, apply any Riemann solver there, and add even-derivative flux corrections so the flux difference is high order; Balsara, Bhoriya and Shu make it general-purpose up to ninth order with a boundary-centred WENO interpolation of the corrections."
status: established
aliases: [AFD-WENO, alternative formulation of finite-difference WENO, Shu-Osher alternative flux]
tags: [finite-difference, weno, interpolation, riemann-solver, mhd]
timestamp: 2026-10-08T00:00:00Z
---

# Alternative finite-difference WENO (AFD-WENO)

**Two finite-difference forms.** Shu and Osher's papers contain two
routes to a conservative high-order FD scheme on point values. The
popular one reconstructs the split fluxes $f^\pm$ as if they were cell
averages of the [flux function](/methods/conservative-finite-difference.md)
$\mathcal{H}$. The other — introduced first, explained later by
Merriman and named "alternative" by Jiang, Shu and Zhang — interpolates
the solution and corrects the flux by even derivatives
([Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §I;
[Shu & Osher (1988)](/sources/shu-1988.md), §III). The classical form
needs a smooth splitting, which restricts it to Lax–Friedrichs or
Roe-type fluxes, and does not preserve free streams on curvilinear
meshes. The alternative form accepts any
[Riemann solver](/methods/approximate-riemann-solvers.md) pointwise and
preserves free streams (Jiang, Shu and Zhang, cited).

**Why corrections are needed** ([Balsara et al. (2025)](/sources/balsara-2025.md), §II.a;
checked on the page images). Even if $\hat f(u^-_{i+1/2}, u^+_{i+1/2})$
is pointwise exact at $x_{i\pm1/2}$, its difference is only second order:
$\frac1h\left[f(x_{i+1/2}) - f(x_{i-1/2})\right] = (\partial_x f)_i + \frac{h^2}{24}(\partial_x^3 f)_i + \dots$.
Subtracting $\frac{h^2}{24}\partial_x^2 f$ at the interface restores
fourth-order flux differences. The numerical fluxes for orders 3 to 9
are
$$\hat f_{i+1/2} = \hat f\left(u^-_{i+1/2}, u^+_{i+1/2}\right) - \left\{\frac{h^2}{24}\left[\partial_x^2 f\right]_{i+1/2} - \frac{7h^4}{5760}\left[\partial_x^4 f\right]_{i+1/2} + \frac{31 h^6}{967680}\left[\partial_x^6 f\right]_{i+1/2} - \frac{127 h^8}{154828800}\left[\partial_x^8 f\right]_{i+1/2}\right\},$$
truncated after the first, second, third or fourth term (eqs. 9–12). Here
$u^\pm_{i+1/2}$ are WENO *interpolations* of point values, not
reconstructions from averages; the two give polynomials of the same
degree with different coefficients. A computer-algebra script derives
the update at any order (Appendix A).

**Taming the corrections** ([Balsara et al. (2025)](/sources/balsara-2025.md), §§II.b, IV).
Finite-differencing $f$ to obtain $\partial_x^{2k} f$ is oscillatory at
shocks. Earlier fixes were equation-specific switches (Zheng–Shu–Qiu;
positivity-based switches for Euler by Gao et al.). The general fix
uses $\partial_x f = A\,\partial_x u$:
$\partial_x^{2k} f = \partial_x^{2k-1}(A\,\partial_x u)$. $A\,\partial_x u$ is
evaluated at cell centres, as a by-product of the interpolation, and a
new **boundary-centred WENO-AO interpolation** maps these values to the
odd derivatives needed at $x_{i+1/2}$. Two third-order stencils
straddling the interface (plus centred fourth-, sixth- and eighth-order
stencils at higher orders) are hybridized as in
[WENO-AO](/methods/weno-ao.md). When the two small stencils' slopes
disagree in sign they cancel, so the interpolation itself acts as a
discontinuity detector and suppresses the corrections at shocks.
Multiresolution (Zhu–Shu) hybridization works equally. The interface
interpolation can be done componentwise; characteristic projection
"works just as well" but costs more (§V).

**Cost.** Two WENO steps — the cell interpolation (in characteristic
variables, the expensive one) and the interface interpolation — match
the two flux reconstructions of classical FD-WENO, so the complexity is
the same ([Balsara et al. (2025)](/sources/balsara-2025.md), §§II.b, V).
Stiff sources are collocated with the unknowns, which suits IMEX
Runge–Kutta methods.

**Results** ([Balsara et al. (2025)](/sources/balsara-2025.md), §§VI–VIII).
Orders 3, 5, 7 and 9 reach design accuracy on 2D vortices for Euler,
relativistic hydrodynamics and the ten-moment gas model (HLLI/LLFI
fluxes; SSP-RK3, or SSP(5,4) with $\Delta t$ scaled as $(1/2)^{5/4}$ or
$(1/2)^{7/4}$ per refinement). Shock tubes, the blast waves, the forward
step and the double Mach reflection are run with a flattening algorithm
for the most stringent cases.

**Extensions.**
* **Divergence constraints** ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md)):
  cell-centred variables follow AFD-WENO, while face-averaged normal
  field components are updated in FV fashion from edge electric fields
  stabilized by a 2D Riemann solver
  ([constrained transport](/methods/constrained-transport.md)). Primitive
  variables can be interpolated as easily as conserved ones, which
  matters for relativistic MHD (§8).
* **Positivity / PCP** by flux hybridization
  ([flux limiter](/methods/positivity-preserving-flux-limiter.md)). The
  split of the flux into a Riemann-solver part and a derivative part is
  suggested as a route to positivity proofs
  ([Balsara et al. (2025)](/sources/balsara-2025.md), §II.b).
* Non-conservative products, well-balancing (Xu–Shu), curvilinear
  meshes and general relativity are cited as developed elsewhere
  ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §1).

**FD versus FV cost.** With identical ingredients and SSP-RK, FD
(AFD-)WENO MHD updates zones 7–14 times faster than FV-WENO in 2D and
5–12 times faster in 3D, with the gap growing with order. FV can recover
part of it (fewer Riemann calls, and ADER, which gives about a factor
of two over SSP-RK) ([Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §7.4).

**With MP5 on adaptive curvilinear grids.** [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md)
use the alternative form with MP5-limited primitive variables instead of
WENO, and any Riemann solver (HLLE in their tests). They build the
correction only from the face flux and cell-centre physical fluxes,
$\hat f_{i+1/2} = \hat f^{\mathrm R}_{i+1/2} - \tfrac16\left(f_i - 2\hat f^{\mathrm R}_{i+1/2} + f_{i+1}\right) + \tfrac1{180}\left(f_{i-1} - 9f_i + 16\hat f^{\mathrm R}_{i+1/2} - 9f_{i+1} + f_{i+2}\right)$,
where $\hat f^{\mathrm R}$ is the Riemann flux and $f_j = f(u_j)$
(eqs. 5–6, checked on the page image). The stencil is then three cells
per side and needs three ghost layers. The correction expands to the
$-\frac{h^2}{24}$, $\frac{7h^4}{5760}$ series above (a compiler's Taylor
check, not stated in the paper). It is left unlimited, so the scheme is
not monotonicity-preserving, and its oscillations stay small (§§2.2, 6).
The authors trace the route to Del Zanna's "FD-Primitive" scheme and the
explicit weighted compact nonlinear schemes of Deng et al. They rejected
global Lax–Friedrichs flux splitting as "quite diffusive" (§1). It runs on
block-adaptive curvilinear grids with
[free-stream preservation](/properties/free-stream-preservation.md) and
costs about 3 times the second-order scheme
([high-order AMR](/methods/high-order-amr.md)).

**In the reviews (batch 6).** Shu describes the alternative form as WENO
interpolation plus "all the even-order derivatives of the flux function",
and stresses that it "allows use of all monotone fluxes, regardless of
their smoothness". He promises other advantages without discussing them
([Shu (2020)](/sources/shu-2020.md), §4.2). The interpolation candidates and weights are on the
[WENO](/methods/weno.md) page ([Shu (2009)](/sources/shu-2009.md), §2.1).

# Citations

1. [Balsara, Bhoriya, Shu & Kumar (2025)](/sources/balsara-2025.md), §§I–IX (eqs. 2–12 read from the page images).
2. [Balsara, Bhoriya & Shu (2026)](/sources/balsara-2026.md), §§1, 2, 4, 7.4, 8.
3. [Shu & Osher (1988)](/sources/shu-1988.md), §III.
4. [Chen, Tóth & Gombosi (2016)](/sources/chen-2016.md), §§1–3, 6 (accepted manuscript).
5. [Shu (2020)](/sources/shu-2020.md), §4.2.
6. [Shu (2009)](/sources/shu-2009.md), §2.1.
