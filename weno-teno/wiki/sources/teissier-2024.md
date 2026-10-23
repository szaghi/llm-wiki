---
type: Source
title: "Teissier et al. (2024) — Cost-efficient finite-volume high-order schemes for compressible magnetohydrodynamics"
description: "Dimension-by-dimension finite-volume constrained-transport MHD solvers of orders 2 to 10 that reconstruct one WENO value per face and pass through high-order point values for the fluxes, with explicit average-to-point formulas, consistent viscous, resistive and forcing terms, and matching SSP integrators."
resource: "doi:10.1016/j.jcp.2024.113287"
source_kind: paper
authors: [Teissier J.M., Mäusle R., Müller W.C.]
year: 2024
venue: "J. Comput. Phys. 515:113287"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Teissier_Cost-efficient_finite-volume_high-order_schemes_for_compress.pdf"
tags: [finite-volume, mhd, very-high-order, weno, turbulence, efficiency]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds a family of dimension-by-dimension finite-volume solvers S2–S10, of
orders 2, 4, 6, 8 and 10, for compressible MHD on Cartesian grids. The MHD may be
adiabatic or isothermal, and optionally viscous, resistive and radiatively cooled.
The magnetic field is evolved by
[constrained transport](/methods/constrained-transport.md), which keeps the
[discrete divergence of $B$](/properties/divergence-free-magnetic-field.md) at
machine precision. The solvers extend the authors' earlier fourth-order
[CWENO](/methods/cweno.md) MHD solver.

The key ingredient, taken from McCorquodale & Colella and Buchmüller & Helzel, is a
passage through point values. A 1D finite-volume
[WENO-JS](/methods/weno-js-reconstruction.md) reconstruction of order $n+1$ gives
face area averages. Explicit symmetric-stencil formulas turn these into face-centre
point values; this is the
[cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md).
Point-valued [local Lax–Friedrichs](/methods/lax-friedrichs-flux.md) fluxes are
computed from them and converted back to area-averaged fluxes. Only one
reconstructed value per face is needed at any order, and no face quadrature. The
paper prints every conversion formula up to tenth order (line, area and volume
averages, both ways) and the general Taylor and linear-system derivation. The face
values of the staggered field are interpolated to volume averages at matching order.
The edge electric field uses a multidimensional Lax–Friedrichs flux. Viscous,
resistive, cooling and Ornstein–Uhlenbeck forcing terms are added consistently with
the finite-volume and constrained-transport structure. Time integration uses
[SSP](/methods/ssp-runge-kutta.md) single-step methods (orders 2, 4) and
multistep-multistage methods (orders 6, 8, 10).

A 3D [MHD vortex](/benchmarks/magnetized-vortex.md) at low Mach number reaches the
design orders up to about 10. Without the point-value passage, or with a
second-order time integrator, the scheme falls to order 2. Exact decay of viscous
and resistive Fourier modes is reproduced at design order. Forced subsonic
hydrodynamic and MHD [turbulence](/benchmarks/compressible-isotropic-turbulence.md)
shows wider inertial ranges at higher order. Relative to S2, a step costs 1.3, 1.6,
2.2 and 5.9 for S4–S10. Because the same error is reached on much coarser grids,
higher order wins overall: S6 against S4 by "a factor of order 10". The large
[numerical dissipation](/definitions/numerical-dissipation.md) of the second-order
scheme at low Mach number is traced to the Lax–Friedrichs flux. Shocks are out of
scope.

# Version read

The archive file is arXiv:2306.09856v2 [math.NA], 27 June 2024 (title-block date 28
June 2024), 32 pages (text pp. 1–25, Appendix A pp. 25–30, references pp. 30–32), all
read; equations and tables of pp. 13–14 and 17–21 were checked on the page images.
It carries an earlier title, "High-order finite-volume integration schemes for
subsonic magnetohydrodynamics", and two of the three published authors, J.-M.
Teissier and W.-C. Müller (its author-contribution statement lists only them). The
arXiv API, checked 2026-10-23, links this record to the JCP DOI
10.1016/j.jcp.2024.113287, whose Crossref record has the title above and adds R.
Mäusle as second author. The version of record may therefore differ in content.
Every claim, equation and number on this page is that of arXiv v2.

# Key claims

Registry notation. Page-local: $\bar u$ a volume average, $\bar u^{x}$ an area
average over a face normal to $x$, $u$ without bar a point value; $\bar u^{\Sigma mn}$
the sum of the area averages at offsets $(\pm m,\pm n)$ and $(\pm n,\pm m)$, each
counted once (similarly $\bar u^{\Sigma\alpha\beta\gamma}$ in 3D); $\mu_{\mathrm v}$
the dynamic viscosity, $\eta_{\mathrm m}$ the magnetic diffusivity; S$n$ the solver of
order $n$ (see the Notation map).

1. One reconstructed value per face suffices at any order. Reconstructed area averages are converted to face-centre point values, point fluxes are evaluated, and these are converted back to area-averaged fluxes, with no multi-point face quadrature (§1, §3.2.2, §3.7, §5). **Derived**
2. Explicit area-average→point formulas are given for orders 2–10 (Eqs. 37–41), with their inverses (Eqs. 45–49), together with volume-average↔point (96–110) and line-average↔point (111–120) formulas, all on point-symmetric stencils built from the class sums $\bar u^{\Sigma mn}$, $\bar u^{\Sigma\alpha\beta\gamma}$. The fourth-order 2D case is $u_{ij}=\tfrac76\bar u^z_{ij}-\tfrac1{24}\bar u^{z\,\Sigma10}_{ij}+O(h_\Delta^4)$ (Eq. 38) (§3.2.2, App. A.3–A.4). **Derived**
3. Identifying an area average with the face-centre point value costs $O(\Delta x^2)$ (Eq. 36), so a solver without the passage through point values is limited to second order (§3.2.2). **Derived** (confirmed by S8P, claim 12)
4. The volume average of the staggered magnetic field is plain polynomial interpolation of its face values, with closed-form coefficients to tenth order (Eqs. 20–24). No non-oscillatory reconstruction is needed because the normal component is continuous along its direction (§3.1.1). **Derived** (continuity **Stated**)
5. Volume averages of derivatives, $(\partial_xv_n)_{ijk}=(\bar v^x_{n,i+1/2}-\bar v^x_{n,i-1/2})/\Delta x$, are exact, so the viscous and resistive terms keep the order of the scheme (§3.4.1, Eq. 52; §3.4.2, Eq. 53). **Derived**
6. The staggered constrained-transport update preserves the discrete divergence (17) to machine precision, because the edge electric-field contributions cancel in pairs (§2.3). **Stated** (cited)
7. Above order four no explicit single-step SSP Runge–Kutta method exists, and explicit two-step SSP methods have order at most eight, so tenth order needs at least three steps (§3.6). **Stated** (cited)
8. The integrators are SSP(2,10,1) and SSP(4,10,1), SSP(6,10,2), SSP(8,10,3) and SSP(10,20,3) (order, stages, steps), with CFL constants $1.9, 1.9, 1.5, 1.2, 2.1$ and viscous constants $5.5, 1.4, 0.6, 0.3, 0.5$. The eighth-order two-step methods need a smaller step than the three-step ten-stage method, which is therefore used (§3.6, Table 1). **Stated**
9. The multistep methods start with step doubling, $\Delta t^*=\Delta t_{\mathrm{CFL}}/2^{\alpha}$, with $\Delta t^*$ small enough that $(\Delta t^*)^{5}=O(\Delta t_{\mathrm{CFL}}^{p})$ for the fourth-order starter SSP(4,10,1) (§3.6, Eq. 60, Fig. 10). **Stated**
10. 3D MHD vortex, one period ($t=10$): S4, S6, S8 and S10 reach their design orders, with $L^2$ orders 4.46, 6.12, 7.87, 9.74 and errors $7.5\times10^{-5}$, $1.4\times10^{-6}$, $2.1\times10^{-8}$, $5.0\times10^{-10}$ at $192^3$. S2 converges only slowly at $t=10$ (orders 0.197, 0.657, 1.15) (§4.1, Table 2). **Shown**
11. For the vortex the WENO weights use $q=1$, $\epsilon=10^{-12}$: the "typical choice $p=2$, $\epsilon=10^{-6}$ leads to a worse convergence for schemes of order strictly greater than 4" (§4.1). **Shown** (no table)
12. S8P (S8 without the point-value passage) converges at order 2 (2.11, 1.97, 1.99), yet its energy loss stays close to that of S8, which the authors read as a hint of dispersive rather than dissipative errors. S8T (S8 with a second-order integrator at CFL 0.5) also tends to order 2 (2.12 at $192^3$) (§4.1, Table 2). **Shown**
13. S2 loses most of the fluctuating energy of the vortex (0.99 at $64^3$, 0.60 at $256^3$). The cause is Lax–Friedrichs dissipation at low Mach number, where $a(u^+-u^-)$ is dominated by the fast magnetosonic speed. Higher order makes the jump $u^+-u^-$ small enough to avoid excessive dissipation, an alternative to low-Mach-corrected Riemann solvers (§4.1). **Shown** (mechanism **Stated**)
14. Cost per step relative to S2 is 1.3 (S4), 1.6 (S6), 2.2 (S8) and 5.9 (S10); the cost to reach a fixed time (per-step cost divided by the CFL constant) is 1.3, 2.0, 3.5, 5.3. Both come from $512^3$ runs excluding start-up, on the same cores, compiler and processors; the hardware is not given (Table 3). **Shown**
15. The energy loss of S4 at $192^3$ ($9.0\times10^{-3}$) matches S6 at $96^3$ ($7.7\times10^{-3}$). S6 costs about 50 % more than S4, while halving the resolution saves a factor $2^4=16$ (8 in space, 2 in the step), so S6 is more efficient by "a factor of order 10"; the same holds for every increase of order on this smooth problem (§4.1). **Shown** (from Tables 2–3) / **Derived**
16. Viscous and resistive decay of 30 random Fourier modes ($\mu_{\mathrm v}=\eta_{\mathrm m}=10^{-4}$, $64^3$, $128^3$, $192^3$): rescaled by $(N_x/64)^n$ for S$n$, the error curves collapse, confirming the design order for orders 2–10; S10 at $192^3$ is affected by machine precision (§4.2, Fig. 11). **Shown**
17. In the pure-diffusion test the Lax–Friedrichs speed must be the diffusion speed, $a^x=\tfrac43\mu_{\mathrm v}/\Delta x$, and the edge speed $\eta_{\mathrm m}/\min(\Delta x,\Delta y)$. With zero speeds the scheme is unstable, because small-scale fluctuations grow (§4.2). **Shown** (instability asserted)
18. In the diffusion test the magnetic-field error stays near $5\times10^{-15}$ while the velocity error decreases; the authors attribute it to floating-point arithmetic and leave it (§4.2). **Stated**
19. In subsonic driven turbulence the finite-volume form turns all dissipated kinetic and magnetic energy into heat, because total energy is conserved. Without a sink the temperature rises and the RMS Mach number falls, as the estimates (78)–(81) predict (S4, $32^3$). The sink coefficient $\lambda_{\mathrm c}=\epsilon^K_{\mathrm{inj}}/U^4(0)$ keeps the temperature constant (§4.3.1, Eqs. 78–82, Fig. 12). **Shown** / **Derived**
20. In hydrodynamic turbulence S10 at $64^3$ shows detail similar to S2 at $256^3$, and its inertial range lies between those of S2 and S4 at $256^3$ (§4.3.2, Figs. 13–14). **Shown**
21. In MHD turbulence the power-law range grows with order, but less from S8 to S10 than at each earlier step (§4.3.3, Fig. 15). **Shown**
22. Kinetic forcing applied as an acceleration, $\partial_t(\rho v)=\rho f$, gives a broader inertial range than force-field forcing. The mean velocity produced by the stochastic driver is removed at each call, because magnetic fields break Galilean invariance (§3.5.4). **Stated**
23. For supersonic, non-smooth flows the high-order polynomials cause stability problems; flattening, possibly with positivity preservation, is suggested but not done (§1, §5). **Stated**
24. The Lax–Friedrichs speed (32)–(33) holds strictly only for ideal MHD, but can be used while $\max(\eta_{\mathrm m},\mu_{\mathrm v}/\rho)/\min(\Delta x,\Delta y,\Delta z)\ll\min c_f$ (§3.2.1). **Stated**

*(Compiler check, not in the sources.)* The 1D line-average-to-point formulas
(111)–(115), e.g. $u_i=\tfrac{1067}{960}\bar u_i-\tfrac{29}{480}(\bar u_{i+1}+\bar u_{i-1})+\tfrac3{640}(\bar u_{i+2}+\bar u_{i-2})$
at sixth order, and the face-to-volume interpolation coefficients (20)–(24) are exact
on polynomials of the stated degree; checked in rational arithmetic for orders 4–10.

# Printed slips

- **Eqs. (55), (76), (77)**: every area- or volume-average factor is printed as $(e^{ik_y\Delta y/2}-e^{ik_y\Delta y/2})(e^{ik_z\Delta z/2}-e^{ik_z\Delta z/2})$ (in (76) also the $x$ factor), with the same sign in both exponents, so each bracket is identically zero (checked on the page image of p. 21). *(Compiler check, not in the sources:)* the cell average of $e^{ik_xx}$ over a cell of width $\Delta x$ is $(e^{ik_x\Delta x/2}-e^{-ik_x\Delta x/2})/(ik_x\Delta x)=2\sin(k_x\Delta x/2)/(k_x\Delta x)$, so the second exponent of each bracket must carry a minus sign.
- Fig. 12: the caption reads "(b) the average sound speed and (c) the RMS Mach number", and the text cites the panels in the same way, but the panels show the RMS Mach number in (b) and the sound speed in (c).
- §3.5.1 calls $N(0,dt)$ a Gaussian "with zero mean and standard deviation $dt$" and writes $dW(t)=dt\,N(0,dt)$; *(compiler check, not in the sources: a Wiener increment has variance $dt$, hence standard deviation $\sqrt{dt}$; the forcing amplitude is fixed afterwards by the normalizations $A_K$, $A_M$ of Eqs. (56)–(57), so the injected power does not depend on this convention.)*
- Eq. (11) *(compiler check, not in the sources)*: the viscous momentum flux $-\mu_{\mathrm v}(\partial_xv_x+\tfrac13\nabla\cdot v)$, $-\mu_{\mathrm v}\partial_xv_y$ is a row of $\mu_{\mathrm v}\big(\nabla v+\tfrac13(\nabla\cdot v)I\big)$, not of the symmetric Newtonian stress; the two have the same divergence (8) only for constant $\mu_{\mathrm v}$. The energy flux carries neither viscous work nor a resistive Poynting term. Total energy is still conserved, and the turbulence runs have zero physical viscosity.
- Ref. [18] prints its co-authors as "O. S, C. T" (Osher, Chan); refs. [5] and [42] print only authors, journal and DOI.
- Typos: "Stoke's theorem" (§2.3), "Stefan-Boltzman" (§3.4.3).
- Not printed: $\gamma$ for the vortex test, the problem behind the $512^3$ cost runs of Table 3.

# Notation map

| Teissier & Müller (arXiv v2) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$ (generic conserved quantity) | $u$ | **collision** with the weight exponent $q$ |
| $\rho$, $v$, $p$ | $\rho$, $v$, $p$ | agree |
| $e$ (total energy density) | $E$ | **collision**: registry $e$ is the specific internal energy |
| $b$ | $B$ | magnetic field, Heaviside-type units (no $4\pi$) |
| $U=p/(\gamma-1)$ | internal energy density (local) | |
| $E$, $\bar E^z_z$ (electric field, edge line average) | $\mathcal E$, $\bar{\mathcal E}_3$ (page-local, as on [constrained transport](/methods/constrained-transport.md)) | **collision** with the total energy $E$; $\mathcal E$ is not the registry's vortex strength here |
| $\mu$ (viscosity), $\eta$ (magnetic diffusivity) | $\mu_{\mathrm v}$, $\eta_{\mathrm m}$ (local) | **collision** with the affine $\mu$ and the entropy $\eta$; in the vortex (66) $\mu$ and $\kappa$ are field amplitudes, $\phi$ a decay rate |
| $\sigma$ | viscous stress (local) | not the affine scaling |
| $S_e=\lambda U^4$ | cooling sink, $\lambda_{\mathrm c}$ (local) | **collision** of $\lambda$ with the eigenvalues |
| triple overbar $\bar q_{ijk}$ | $\bar u_{ijk}$ | volume (cell) average |
| $\bar q^x$, $\bar q^n$ | $\bar u^{x}$ (local) | area average over a face normal to $x$ |
| $\bar q^{\Sigma mn}$, $\bar q^{\Sigma\alpha\beta\gamma}$, $q^{\Sigma\alpha}$ | $\bar u^{\Sigma mn}$, … (local) | class sums; 4 or 8 terms in 2D, 6, 8, 12 or 24 in 3D |
| $h=\Delta x+\Delta y(+\Delta z)$ | $h_\Delta$ (local) | **collision** with the numerical flux $h$ |
| $q^-$, $q^+$ at $i+1/2$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | agree (left from cell $i$, right from cell $i+1$) |
| $n$ (WENO half width; $2n+1$ cells, order $2n+1$) | $r=n+1$ | |
| $P^{opt}$, $P^m$ | $P_{\mathrm{opt}}$, $P_k$ | as on the CWENO pages |
| $d^\pm_m$, $\alpha^\pm_m$, $w^\pm_m$ | $d_k$, $\alpha_k$, $\omega_k$ | per face side |
| $IS_m$ | $\beta_k$ | Jiang–Shu form |
| $\epsilon$, $p$ (in (28)) | $\epsilon$, $q$ | **collision**: $p$ is also pressure and the SSP order |
| $a^x$ | $a$ | maximum signal speed $\max(\lvert v_x\rvert+c_f^x)$ |
| $c_f$, $c_s$, $c_A$ | fast magnetosonic, sound, Alfvén speeds | registry $c$ is $c_s$ |
| $S$ (edge LLF speed) | edge speed (local) | **collision** with $S(u)$ |
| SSP$(p,s,n)$, $C_{CFL}$, $C_{VISCO}$ | order, stages, steps; step constants | $C_{CFL}$ is not the registry CFL number $\nu$ |
| $\delta_2(N)$, EOC$_2$, $E_{loss}$ | $L^2$ error, observed order, fraction of fluctuating energy lost | $N$ is the grid size $N_x$, not the DG degree |
| $\theta(k)$, $\zeta$, $\mathcal P^\zeta$, $t_{auto}$ | forcing profile, projection parameter, projector, correlation time | **collision** of $\zeta$ with the characteristic variables |

# Reference list

The file prints 44 references, numbered [1]–[44]. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `teissier-2024`. Refs. [5]
(Miczek et al.) and [42] (Leidi et al.) print only authors, journal and DOI; their
keys take years read from the A&A DOI series, to be verified. Ref. [18] has truncated
co-author names, ref. [29] prints its first author as "M. M. Low", ref. [39] is the
undated sspsite web page and ref. [20] an ICASE report. No item is unparseable.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunk 9 (2026-10-23). This source is cited on:

* [Cell-average to point-value conversion](/operators/cell-average-point-value-conversion.md)
* [Compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Constrained transport for the induction equation](/methods/constrained-transport.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Magnetized (MHD) vortex](/benchmarks/magnetized-vortex.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
