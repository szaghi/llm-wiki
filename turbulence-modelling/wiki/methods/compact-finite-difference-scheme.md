---
type: Method
title: "Compact finite-difference schemes"
description: "Compact (Padé-type) finite differences obtain derivatives, mid-point interpolations and low-pass filters from a tridiagonal system linking neighbouring unknowns; this page gives the sixth-order first-derivative, second-derivative, staggered and interpolation stencils of the sources, compact filters, their spectral behaviour and their use in DNS, implicit LES and shock-capturing hybrids."
status: established
aliases: [compact scheme, compact finite differences, Padé scheme, Lele scheme, sixth-order compact scheme, tridiagonal compact scheme, compact filter, compact interpolation]
tags: [dns, implicit-les, numerical-dissipation, filtering, software]
timestamp: 2026-10-29T05:13:00Z
---

# Compact finite-difference schemes

A **compact** (or Padé-type, implicit) finite-difference scheme computes a
derivative, an interpolated value or a filtered value at all nodes of a
grid line at once, from a linear system in which each unknown is coupled
to its neighbours (a tridiagonal one in the sources below). For the first derivative
on a uniform grid of spacing $h$ the sixth-order member of the family is

$$\alpha_{\mathrm c}\phi'_{i-1}+\phi'_i+\alpha_{\mathrm c}\phi'_{i+1}=a_{\mathrm c}\frac{\phi_{i+1}-\phi_{i-1}}{2h}+b_{\mathrm c}\frac{\phi_{i+2}-\phi_{i-2}}{4h},\qquad \alpha_{\mathrm c}=\tfrac13,\ a_{\mathrm c}=\tfrac{14}9,\ b_{\mathrm c}=\tfrac19,$$

as printed by [Yan et al. (2024)](/sources/yan-2024.md), App. A1,
Eq. (A2), for the [Xcompact3d](/software/xcompact3d.md) framework, and with
the same coefficients by [Kang & Lee (2024)](/sources/kang-2024.md),
§II.B, Eq. (8), for their compressible DNS solver (Lele; Visbal & Gaitonde,
as cited). The historical review of
[Kim & Leonard (2024)](/sources/kim-2024-b.md), §4.8, records that these
schemes (Lele 1992, as cited there) were developed to minimize numerical
dispersion error, for computational aeroacoustics at NASA Ames.

Notation (page-local): $\phi_i$ a grid function at node $x_i$, primes its
discrete derivatives; $\alpha_{\mathrm c}$, $a_{\mathrm c}$, $b_{\mathrm c}$
the compact coefficients (not the registry's DG blending factor $\alpha$
or modal-filter strength $\alpha_f$); $\alpha_{\mathrm{cf}}$ and $a_n$ the
parameter and coefficients of a compact filter, $\phi^{\mathrm f}_i$ the
filtered value (not the registry's test filter $\hat\phi$); $k'$, $k''$ the modified
wavenumbers of the first and second derivative; $k_c=\pi/h$ the grid
cut-off (registry §8).

## Stencils in the sources

- **First derivative, sixth order** (above). Applied to $\phi=x$ both
  sides equal $\tfrac53$, and the modified wavenumber is
  $k'h=\big[a_{\mathrm c}\sin(kh)+\tfrac{b_{\mathrm c}}2\sin(2kh)\big]/\big[1+2\alpha_{\mathrm c}\cos(kh)\big]$
  *(compiler check, not in the sources)*. Kang & Lee use it on generalized
  curvilinear coordinates ($h=1$) with sixth-order one-sided compact
  closures at the boundaries (§II.B).
- **Second derivative, sixth order** (Yan et al. 2024, Eq. A3):
  $$\tfrac2{11}\phi''_{i-1}+\phi''_i+\tfrac2{11}\phi''_{i+1}=\tfrac{12}{11}\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{h^2}+\tfrac3{11}\frac{\phi_{i+2}-2\phi_i+\phi_{i-2}}{4h^2}.$$
  Widening the right-hand side to nine points leaves two free
  coefficients, which Xcompact3d uses to make the scheme over-dissipative
  near $k_c$: the implicit
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  (Yan et al., App. B1; [Vicente Cruz & Lamballais 2023](/sources/vicentecruz-2023.md),
  §5.1).
- **Staggered first derivative, sixth order** (from nodes to mid-points;
  [Fang et al. 2025](/sources/fang-2025.md), §2.3, Eq. 15):
  $$\tfrac9{62}\phi'_{i-1/2}+\phi'_{i+1/2}+\tfrac9{62}\phi'_{i+3/2}=\tfrac{63}{62}\frac{\phi_{i+1}-\phi_i}{h}+\tfrac{17}{186}\frac{\phi_{i+2}-\phi_{i-1}}{h},$$
  exact for $\phi=x$ ($\tfrac{80}{62}$ on both sides) *(compiler check, not
  in the sources)*.
- **Mid-point interpolation, sixth order** (Fang et al. 2025, Eq. 16;
  Yan et al. 2024, Eq. A1):
  $$\tfrac3{10}\phi^I_{i-1/2}+\phi^I_{i+1/2}+\tfrac3{10}\phi^I_{i+3/2}=\tfrac34(\phi_{i+1}+\phi_i)+\tfrac1{20}(\phi_{i+2}+\phi_{i-1}),$$
  which reproduces a constant ($1.6$ on both sides) *(compiler check, not
  in the sources)*; it moves quantities
  between the velocity and pressure grids of a staggered or half-staggered
  arrangement (see Qualifications for Yan et al.'s printed form).

Fang et al. combine the staggered derivative in one direction with the
mid-point interpolation in the other to build the right-hand side of a
Poisson equation on the half-staggered pressure mesh, solved directly by
FFT; with the modified-wavenumber concept the discrete velocity
divergence vanishes "up to machine accuracy" (§2.3, Eq. 14, citing Lele
and Laizet & Lamballais). The same arrangement carries the magnetic
"pressure" correction of their MHD solver, whose divergence of the field
is about $10^{-13}$ after correction (§2.2).

## Spectral behaviour and induced filters

In the half-staggered
compact-difference code of [Caban et al. (2026)](/sources/caban-2026.md)
(sixth- and tenth-order compact derivatives, compact or spectral
interpolation), the filter induced by the first-derivative scheme changes
only the phase speed, the filter induced by the second-derivative scheme
lowers the viscous dissipation of the small scales, and two successive
interpolations act as a squared filter (§3.2, Eqs. 34–35); in the
transitional Taylor–Green vortex the interpolation order matters most
when it is close to the derivative order (§4.1, Fig. 5a; see
[discretization-consistent closures](/definitions/discretization-consistent-closure.md)).
The modified wavenumber of the first-derivative scheme above is real, so
that scheme adds no dissipation *(compiler check, not in the sources)*.
The sources add instead
a skew-symmetric form of the convective term
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md);
Fang et al. 2025, §2.1), an over-dissipative second derivative (the
implicit SVV above), or an explicit compact filter (below).

## Compact filters

A compact low-pass filter solves the same kind of system for the filtered
values $\phi^{\mathrm f}_i$:

$$\alpha_{\mathrm{cf}}\phi^{\mathrm f}_{i-1}+\phi^{\mathrm f}_i+\alpha_{\mathrm{cf}}\phi^{\mathrm f}_{i+1}=\sum_{n=0}^{4}\frac{a_n}2(\phi_{i+n}+\phi_{i-n}),$$

the eighth-order filter of Gaitonde & Visbal as printed by Kang & Lee
(2024), Eq. (9), with $a_0=(93+70\alpha_{\mathrm{cf}})/128$,
$a_1=(7+18\alpha_{\mathrm{cf}})/16$, $a_2=(-7+14\alpha_{\mathrm{cf}})/32$,
$a_3=(1-2\alpha_{\mathrm{cf}})/16$, $a_4=(-1+2\alpha_{\mathrm{cf}})/128$
and $-0.5<\alpha_{\mathrm{cf}}\le0.5$, less filtering as
$\alpha_{\mathrm{cf}}\to0.5$. Kang & Lee apply it with
$\alpha_{\mathrm{cf}}=0.47$ at every final Runge–Kutta stage and drop to a
second-order filter with $0.49$ at shocks flagged by a Ducros-type
[sensor](/definitions/shock-sensor.md), adding localized
[artificial diffusivity](/methods/artificial-viscosity-shock-capturing.md).
The full description of their scheme, with the check that the filter's
transfer function is one at zero wavenumber and zero at the grid Nyquist
wavenumber, is on
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md),
which also records the fourth-order compact filter ($\alpha_{\mathrm{cf}}=0.495$)
that Bernades et al. (2023) compare for real-gas flow. In the supersonic
Taylor–Green code comparison of
[Chapelier et al. (2024)](/sources/chapelier-2024.md) the NS3D solver runs
sixth-order compact differences with a tenth-order compact filter and no
shock capturing; replacing the compact derivatives by explicit
fourth-order ones in post-processing changes the solenoidal dissipation
by up to 5% (§III.B.d). Compact filters used as the closure of
under-resolved LES are on
[explicit modal filtering](/methods/explicit-modal-filtering.md).

**A one-parameter Padé filter as the LES model.** In the LES of
compressible round jets of [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md),
§II B, Fig. 1, the filter of the single-step approximate-deconvolution
method is, in the periodic azimuthal direction, the Padé filter with
transfer function
$$\hat G(\omega)=\Big(\alpha_{\mathrm{cf}}+\tfrac12\Big)\frac{1+\cos\omega}{1+2\alpha_{\mathrm{cf}}\cos\omega},\qquad \alpha_{\mathrm{cf}}=0.2,$$
on the scaled wavenumber $\omega\in[0,\pi]$ ($\omega$ page-local here,
not the specific dissipation rate), with an explicit physical-space filter
of similar spectral behaviour in the non-periodic directions (after Stolz,
cited). It equals one at $\omega=0$ and zero at $\omega=\pi$ for any
$\alpha_{\mathrm{cf}}\neq-\tfrac12$ *(compiler check, not in the
sources)*. The filter is composed with the van Cittert approximate inverse
($N_{\mathrm{AD}}=6$ terms, registry §11) and applied twice per time step,
$(Q_N*G)^2$; the authors show that the transfer functions of $Q_N*G$ and
$(Q_N*G)^2$ decay smoothly to zero at high wavenumber. The method is on
[scale-similarity model](/methods/scale-similarity-model.md).

## Use in turbulence simulation

- **Incompressible DNS and implicit LES (Xcompact3d).** Sixth-order
  compact differences on a Cartesian mesh (optionally stretched in $y$),
  third-order Runge–Kutta or Adams–Bashforth time stepping, an FFT
  Poisson solver on a half-staggered mesh and a 2D pencil decomposition;
  Fang et al. (2025) add an MHD module to it and validate it on
  Orszag–Tang vortices and Hartmann channel flow, and Yan et al. (2024)
  run implicit-SVV LES with a wall-modelled immersed boundary in it. On a
  circular cylinder at $Re_D=3.9\times10^3$ the sixth-order scheme with
  implicit SVV gives $C_D=1.02$ and a recirculation length $1.42D$
  against 1.17 and $2.42D$ for second-order central differences with the
  [Smagorinsky model](/methods/smagorinsky-model.md) on the same mesh, at
  lower cost (Yan et al., §III A, Table II). Code details are on
  [Xcompact3d](/software/xcompact3d.md).
- **Compressible DNS with shocks.** Kang & Lee (2024) stabilize their
  curvilinear compact scheme by filtering and artificial diffusivity for
  a Mach 2.9 compression-ramp interaction (see
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
  The reference DNS of [Zhang et al. (2022b)](/sources/zhang-2022-f.md),
  §III, and [Zhang et al. (2022d)](/sources/zhang-2022-h.md), §III A,
  instead switch between eighth-order compact differences in smooth
  regions (Lele's scheme, as the latter cites) and seventh-order WENO
  in shock regions (see
  [WENO](/methods/weno-scheme.md)).
- **LES of compressible round jets.** Rahatgaonkar & Ghosh (2025), §II A,
  compute all spatial derivatives of a characteristic (Sesterhenn) form of
  the compressible Navier–Stokes equations in cylindrical coordinates with
  Lele's sixth-order compact central differences, a low-storage
  third-order Runge–Kutta scheme and the Mohseni–Colonius axis treatment,
  on $512\times128\times120$ points over $60r_0\times20r_0$ ($r_0$ the
  inflow jet radius, page-local) at $Re=5\times10^5$; azimuthal spectra
  at $x/r_0=30$–50 decay at the highest resolved wavenumbers with a short
  $k^{-5/3}$ segment, which they take as evidence that grid and LES
  approach are adequate (§II D, Fig. 3). Results are on
  [turbulent round jet](/benchmarks/turbulent-round-jet.md).
- **Reference DNS and alternatives in shock-capturing studies.** The
  Taylor–Green DNS of Dairay et al. used as reference by
  [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md), §III F
  ($512^3$), is a sixth-order compact computation, and the authors cite
  compact schemes (Lele) and hybrid compact–WENO schemes (Pirozzoli) as
  near-spectral alternatives to WENO (§I). The review of
  shock–turbulence interaction of [Cuadra et al. (2025)](/sources/cuadra-2025.md),
  §III A 1, lists compact schemes (Lele 1992) next to skew-symmetric
  central ones as smooth-region schemes of shock-capturing hybrids.
- **Compact nonlinear interpolation.** The weighted compact nonlinear
  scheme of [Ma et al. (2022)](/sources/ma-2022.md) makes a seventh-order
  tridiagonal compact interpolation nonlinear, so that the system
  decouples at discontinuities (see
  [weighted compact nonlinear schemes](/methods/weighted-compact-nonlinear-scheme.md)).

## Qualifications

- **Stability at high speed.** [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md),
  §1, state that non-dissipative schemes, central and compact, "are
  unconditionally unstable" for high-speed flows governed by hyperbolic
  equations, which motivates their central/WENO hybrid; the claim is
  stated, not shown. The compact compressible solvers above are printed
  with filtering and artificial diffusivity (Kang & Lee, §II.B) or with
  WENO switching (Zhang et al. 2022b, 2022d), not as bare central compact
  schemes.
- **Printed slip (Kang & Lee 2024).** Eq. (8) prints the second
  right-hand-side term as $b_{\mathrm c}(\phi_{i+2}-\phi_{i-2})/(6h)$; with
  the printed $\alpha_{\mathrm c}=\tfrac13$, $a_{\mathrm c}=\tfrac{14}9$,
  $b_{\mathrm c}=\tfrac19$ the scheme is consistent only with the
  denominator $4h$ printed by Yan et al. (for $\phi=x$ the left side is
  $\tfrac53$, the right side $\tfrac{14}9+\tfrac19\cdot\tfrac46=\tfrac{44}{27}$
  as printed) *(compiler check, not in the sources)*.
- **Printed slip (Yan et al. 2024).** Eq. (A1) prints the mid-point
  interpolation with
  $\tfrac34\,\frac{\phi_{i+1}+\phi_i}2+\tfrac1{20}\,\frac{\phi_{i+2}+\phi_{i-1}}2$
  on the right; for a constant the right side is then $0.8$ against $1.6$
  on the left, half of Fang et al.'s consistent form
  *(compiler check, not in the sources)*.
- **Equation 16 of Fang et al. (2025)** applies the mid-point
  interpolation along $y$ to $x$-derivatives already at half nodes in $x$;
  the coefficients are those of the plain interpolation above.

# Citations

- [Yan et al. (2024)](/sources/yan-2024.md) — App. A1, Eqs. (A1)–(A3) (sixth-order compact interpolation, first and second derivatives); App. B1 (nine-point second derivative of the implicit SVV); §III A, Table II (sixth-order compact against second-order central).
- [Fang et al. (2025)](/sources/fang-2025.md) — §2.1 (skew-symmetric convection); §2.2 (magnetic correction); §2.3, Eqs. (14)–(16) (staggered derivative, mid-point interpolation, FFT Poisson solver, divergence to machine accuracy).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B, Eqs. (8)–(9) (sixth-order compact first derivative on curvilinear grids, eighth-order compact filter, adaptive shock filter).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §4.8 (compact schemes developed to minimize dispersion error; historical).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §5.1 (sixth-order compact second derivative tuned as implicit SVV).
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.2, Eqs. (34)–(35); §4.1, Fig. 5a (filters induced by compact derivatives and interpolations).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.d (NS3D: sixth-order compact differences with a tenth-order compact filter).
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §III (compact/WENO hybrid of the reference DNS).
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §III A (compact/WENO hybrid of the reference DNS).
- [Ma et al. (2022)](/sources/ma-2022.md) — §2.2 (nonlinear tridiagonal compact interpolation).
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §1 (central and compact schemes stated unstable for high-speed flows).
- [Rahatgaonkar & Ghosh (2025)](/sources/rahatgaonkar-2025.md) — §II A (sixth-order compact differences in cylindrical coordinates); §II B, Fig. 1 (Padé filter $\alpha_{\mathrm{cf}}=0.2$ inside single-step ADM); §II D, Fig. 3.
- [Kokkinakis & Drikakis (2025)](/sources/kokkinakis-2025.md) — §I (compact and compact–WENO schemes cited); §III F (compact reference DNS; passing).
- [Cuadra et al. (2025)](/sources/cuadra-2025.md) — §III A 1 (compact schemes as smooth-region schemes in shock–turbulence simulation; review, passing).
