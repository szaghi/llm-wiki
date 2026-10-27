---
type: Method
title: "Artificial-viscosity shock capturing"
description: "Artificial-viscosity shock capturing adds a dissipative term, switched by a shock sensor or built from compression, to stabilize high-order schemes at shocks; this page gives the von Neumann–Richtmyer viscous pressure in modal DG, localized artificial diffusivity, filtered and residual-based forms, and how they compare with order-lowering schemes in compressible turbulence."
status: established
aliases: [artificial viscosity, localized artificial diffusivity, LAD, von Neumann–Richtmyer artificial viscosity, viscous pressure, Persson–Peraire artificial viscosity, entropy-stable artificial viscosity]
tags: [shock-capturing, numerical-dissipation, dg, compressible, implicit-les, entropy-stable]
timestamp: 2026-10-27T06:08:00Z
---

# Artificial-viscosity shock capturing

**Artificial-viscosity (AV) shock capturing** stabilizes a discretization at
discontinuities by adding a dissipative term to the equations, of a size that
spreads a shock over a few grid points or sub-element nodes, and switching it
off (or making it negligible) in smooth flow by a sensor or by construction.
It keeps the polynomial or stencil of the scheme, unlike the order-lowering
[subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
and [WENO](/methods/weno-scheme.md) approaches. In scale-resolving
simulation of compressible turbulence the question is how much the added
dissipation also damps the resolved turbulence, the property measured by
[numerical dissipation](/properties/numerical-dissipation.md).

Page-local symbols: $c$ the sound speed; $p_{\mathrm{av}}$ an artificial
viscous pressure (the source's $\Pi$, renamed because $\Pi$ is the SGS energy
flux of the registry); $C_{\mathrm q}$, $C_{\mathrm l}$ its quadratic and
linear coefficients (the source's $\alpha_{\rm visc}$, $\beta_{\rm visc}$);
$A_s=p/\rho^\gamma$ the entropic function; $\nu_{\mathrm{av}}$ an artificial
kinematic viscosity.

## Forms in the sources

**Viscous pressure from compression (von Neumann–Richtmyer) in modal DG.**
[Cernetic et al. (2024)](/sources/cernetic-2024.md), §3.1, Eqs. (14)–(16),
add to the thermal pressure, only at the internal Gauss points of the volume
integral of a modal (Legendre, total-degree) DG scheme and not in the
surface integrals, where the HLLC Riemann solver supplies the entropy, the
quadratic viscous pressure
$$p_{\mathrm{av}}=C_{\mathrm q}\,\rho\Big(\frac{h}{N+1}\Big)^2|\nabla\cdot\boldsymbol u|^2\quad\text{for }\nabla\cdot\boldsymbol u<0,\qquad p_{\mathrm{av}}=0\ \text{otherwise},$$
optionally augmented by a linear bulk term
$C_{\mathrm l}\,\rho c\,\frac{h}{N+1}|\nabla\cdot\boldsymbol u|$ to damp
post-shock oscillations, and capped by
$p_{\mathrm{av}}\le\tfrac12\rho\big(\tfrac{h}{N+1}\big)^2|\nabla\cdot\boldsymbol u|/\Delta t$
($h$ the cell size, $h/(N+1)$ the effective resolution of a scheme of order
$N+1$; the source writes $h/p$ with $p=k+1$ the order). Recommended
$C_{\mathrm q}\sim2.0$ (range 1.0–3.0) and $C_{\mathrm l}\sim0.2$ (zero or
about $0.1C_{\mathrm q}$), "largely independent of flow type and DG-order",
from the authors' experience. They state that the precise $C_{\mathrm q}$
does not set post-shock states, which the conservation laws fix, only shock
width and residual oscillations, and that the form needs no extra storage.
The motivation (§3.1): on the inviscid Euler equations DG has no sub-cell
entropy source, lacking the entropy that a finite-volume scheme produces in
its cell-averaging step. The viscous pressure replaces the authors' earlier
scheme, an evolved viscosity field with shock and "wiggle" sensors and its
own diffusion solver, which they call complicated, costly and partly "post
hoc damage control"; neither AV alone sufficed for strongly supersonic flow
at high order without their re-projection of primitive variables at faces
(Conclusions; see the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page).

**Localized artificial diffusivity (LAD) switched by a modal sensor.** In the
code comparison of [Chapelier et al. (2024)](/sources/chapelier-2024.md),
§III.B, three solvers add a dissipation operator: the modal DG code CODA
(order 4) computes a Persson–Peraire sensor from the amplitude of the
highest density modes with the calibration of Glaubitz et al., scales the
viscosity by the maximum wave speed in the domain, applies a Laplacian to
all conservative variables and multiplies it at each quadrature point by the
Ducros function, which reduces it where vorticity dominates dilatation; the
spectral-difference code SD3DvisP (order 4) uses a self-calibrated subcell
artificial viscosity with amplitude 0.5 instead of 1 (to avoid strong time-step
restrictions), made $C^0$-continuous by averaging at mesh vertices and
trilinear interpolation, acting as a bulk viscosity on momentum and a
thermal diffusivity on energy, none on mass; and the flux-reconstruction code
H3AMR uses the "Block Spectral Stresses" model, which builds sub-filter
stresses, heat flux and pressure work from the spectra of the velocity
gradient and is meant to capture shocks and model turbulence at once (no
formula printed; §III.B.g).

**Filtered entropy-stable AV.** In the DGSEM,
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §2.2–2.3, §5–6,
write the Guermond–Popov regularization (density diffusion carried into
momentum and energy, plus a viscosity) in entropy variables, filter it with
a [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
kernel and switch it by an element-wise density-gradient sensor, which keeps
the semi-discrete scheme entropy stable; [HORSES3D](/software/horses3d.md)
uses it for shocks ([Ferrer et al. 2023](/sources/ferrer-2023.md), §4.4,
Eqs. 15–19). Formulas and tests are on the DGSEM page.

**Residual-driven AV.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§3.1, Eq. (3-10), stabilize an interior-penalty DG RANS solver with Hartmann's
$\nu_{\mathrm{av}}=C_{\mathrm H}h^{2-\beta_s}\,|\nabla\cdot(F^c-F^v)|$
(page-local constants), which concentrates at the shock of their transonic
case. The [residual-based dynamic SGS model](/methods/residual-based-dynamic-sgs-model.md)
of [Reddy et al. (2026)](/sources/reddy-2026.md), §1, §3.3, is of the same
family: an eddy diffusivity proportional to the residual of the inviscid
filtered equations, capped by a first-order-upwind value
$0.5\Delta\,\big\||\boldsymbol u|+c\big\|_\infty$, designed to stabilize
high-order Galerkin solvers at sharp gradients and used "as a by-product" as
a subgrid model.

**Sensor-switched Laplacian AV in steady high-order RANS.** In the modal DG
discretization of CODA used by [Schotte et al. (2026)](/sources/schotte-2026.md)
for adaptive steady RANS (Spalart–Allmaras, negative variant), the transonic
cases (RAE2822 airfoil, ONERA M6 wing) are stabilized by a Laplacian
artificial viscosity driven by the Persson–Peraire sensor with the
calibration of Glaubitz et al., the same sensor and calibration as in
CODA's LAD above, combined with the positivity-preserving limiter of Wang
et al., which rescales the polynomial coefficients to keep pressure and
density positive when the cell averages are (§2.2, §4.3). They run the
ONERA M6 wing at degree $N=1$ only, because systematic residual convergence
of high-order steady implicit computations with shocks is "problematic" and
non-converged solutions corrupt the error estimators of their
[mesh adaptation](/methods/mesh-adaptation.md) (§4.5), and they name
$hp$-adaptation, keeping $N=1$ around shocks and raising $N$ in smooth
regions of high error, as a perspective (§4.5, §5). No AV formula or
coefficient is printed, and the AV's own effect is not assessed.

**Ducros-weighted JST dissipation as the implicit closure of a jet LES.**
[Ahn et al. (2023)](/sources/ahn-2023.md), §III, Eqs. (1)–(6), run implicit
LES (MILES, no subgrid model) of over-expanded supersonic twin square jets
with the unstructured node-based finite-volume solver EDGE: second-order
central convective fluxes, fourth-order central viscous fluxes, four-stage
Runge–Kutta, and a modified Jameson–Schmidt–Turkel dissipation applied at
the end of the first stage of each step. Between nodes 0 and 1 (registry
§11 symbols $\kappa^{(2)}$, $\kappa^{(4)}$, $\Phi$; page-local $L$ the
undivided Laplacian, $r_{01}$ the face spectral radius times the face area,
$g_{01}$ a grid-stretching factor, $s_{\mathrm n}=3(N_0+N_1)/(N_0N_1)$ from
the neighbour counts $N_0$, $N_1$):
$$\mathcal D_{01}=\big[\kappa^{(2)}_{01}(U_1-U_0)-\kappa^{(4)}_{01}(LU_1-LU_0)\big]g_{01}r_{01},\qquad g_{01}=\frac{4g_0g_1}{g_0+g_1},\quad g_0=\Big(\frac{r_0}{4r_{01}}\Big)^{0.3},$$
$$\kappa^{(2)}_{01}=\max(\kappa^{(2)}_0,\kappa^{(2)}_1),\qquad
\kappa^{(4)}_{01}=\Big(\tfrac12+\tfrac12\min\big(\max(\Phi_0,\Phi_1),\max(\Theta_0,\Theta_1)\big)\Big)\max\big(0,\,0.04-\kappa^{(2)}_{01}\big)\frac{s_{\mathrm n}^2}{4},$$
with $\kappa^{(2)}_0=1.5\,\Phi_0\,s_{\mathrm n}$ times a pressure-jump ratio
over the node's neighbours, $\Phi$ the Ducros factor (printed without a
regularizer) and $\Theta=1-\Phi$ its vortical complement ($\mathcal D_{01}$, $U$
page-local; printed forms discussed on [shock sensors](/definitions/shock-sensor.md)).
The second-difference term is thus active only where dilatation dominates
and the pressure jumps, and the background fourth-difference term is
halved where vorticity dominates. The authors state that "the physical
dissipation originated by small-scale eddies is implicitly considered by
taking the advantage of truncation errors" and that the scheme set is
proven for supersonic jet aeroacoustics (refs. 28, 29, 32, 51–53). The
same JST structure with a Ducros-weighted sensor, and much smaller
fourth-difference coefficients, is the LD2C scheme on
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md);
Ahn et al.'s cap $0.04\,s_{\mathrm n}^2/4$ is not compared with it. Their
implicit LES, the nozzle tripping and the far-field noise are on
[implicit LES](/definitions/implicit-les.md),
[inflow turbulence generation](/methods/inflow-turbulence-generation.md)
and [Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md).

**Residual-based directional AV in modal DG RANS.** In the modal DG RANS
solver used by [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) for
a laminar-kinetic-energy transition model up to the transonic NLR-7301
airfoil (Appendix), shock capturing acts in the whole domain as an
artificial diffusion along the direction of the pressure gradient. With
the primitive working variable $\ln p$, the element size
$h_K=(\Delta x^{-2}+\Delta y^{-2}+\Delta z^{-2})^{-1/2}$ and degree $N$:
$$\nu_{\mathrm{av}}=C\,h_K^2\,\frac{|s_p|+|d_p|}{p}\,f_p,\qquad f_p=\frac{|\nabla_h\ln p|\,h_K}{N},\qquad \boldsymbol b_p=\frac{\nabla_h\ln p}{|\nabla_h\ln p|+\epsilon},\qquad C=0.2,$$
where $d_p$ is built from the flux divergence (the element residual) and
$s_p$ from the interface flux jumps ($\nu_{\mathrm{av}}$ here the
coefficient, $\boldsymbol b_p$ the diffusion direction, $s_p$, $d_p$,
$f_p$ page-local; the source writes $\varepsilon_p$, $\boldsymbol\beta$,
$\ell$ and $e^{\tilde p}$ with $\tilde p=\log p$). It is of the residual
family of Zhao et al. above, made anisotropic; the shock-dominated
transition of the NLR-7301 near $M_\infty=0.724$–$0.748$ is where the
transition model's onset error is largest (81.16%, §V, where the authors
state that the shock dominates transition), see
[laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md).

**Artificial bulk viscosity in finite volumes and ALE codes.** The
[charLES](/software/charles.md) solver adds an artificial bulk viscosity at
discontinuities ([Griffin et al. 2023](/sources/griffin-2023.md), §4), and
the radiation-hydrodynamics code of
[Davidovits et al. (2022)](/sources/davidovits-2022.md), §II A, has no
physical viscosity, only artificial viscosity at shocks, which leads the
authors to call their runs implicit LES rather than DNS (see
[shock-generated turbulence](/results/shock-generated-turbulence.md)). A
physical bulk viscosity is a different matter, treated on
[bulk viscosity](/definitions/bulk-viscosity.md).

**Where the sources choose something else.** The sources on reconstruction
schemes list artificial viscosity among the established shock-capturing
families and take another route: hybrid TENO schemes switched by a
discontinuity indicator ([Liang & Fu 2024](/sources/liang-2024.md), §1;
[Takagi et al. 2022](/sources/takagi-2022.md), §1; see
[WENO](/methods/weno-scheme.md)). In high-order DG RANS,
[Jiang et al. (2025)](/sources/jiang-2025.md), §3.1, §4.2, use the
element-resolution indicator (citing Persson & Peraire) to trigger a
Hermite-WENO limiting of the turbulent kinetic energy, and the same HWENO
limiter on the mean flow at the shock of the RAE2822 airfoil. The
sensors themselves are compared on [shock sensors](/definitions/shock-sensor.md).

## Shock-capturing tests

Cernetic et al. (2024, §3.1.1–3.1.2, Figs. 1–2) test the viscous pressure on
the Shu–Osher problem at $t=1.8$ with 100, 200 and 400 cells, stable up to
degree $N=9$ (order 10) at 400 cells without ringing, and DG of order 2 more
accurate than a second-order finite-volume scheme especially for the narrow
waves; and on the Liska–Wendroff implosion on $400\times400$ cells, where
order-2 DG keeps the symmetry with "clearly less numerical diffusion" than
second-order finite volumes. In driven isothermal turbulence up to rms Mach
12.8 the AV with primitive-variable re-projection runs stably (§5).

## Comparison in a supersonic Taylor–Green vortex

Chapelier et al. (2024) compare seven high-order solvers on the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) ($Re=1600$,
$M_0=1.25$) at $64^3$ to $512^3$ degrees of freedom against a $2048^3$
sixth-order TENO reference, all without subgrid model. They rank shock
capturing by the dilatational dissipation
$\varepsilon_d\propto\int\mu(\nabla\cdot\boldsymbol u)^2$ (registry §11; $\varepsilon_s$ the solenoidal part): low
$\varepsilon_d$ marks strong capturing with smooth thick shocks, high and
oscillating $\varepsilon_d$ sharp shocks with Gibbs oscillations (§IV.A,
Fig. 6). Findings:

- SD3DvisP (LAD) gives oscillation-free but thick shocks and among the
  lowest $\varepsilon_d$; its strong capturing is "probably hindering" the
  small scales on the finer grids (§IV.A–B, Figs. 6–8);
- CODA (LAD) gives sharp shocks with limited oscillations, slight
  oscillations of $\varepsilon_d$ near its first peak from $256^3$, attributed
  to the sharp on/off switching, and among the highest solenoidal
  dissipation $\varepsilon_s$ on all grids (§IV.A–B, Fig. 7);
- H3AMR (BSS, run at second order) has low $\varepsilon_d$ and is too
  dissipative overall, as second-order schemes are (§IV.A);
- in the conclusions, AV approaches give "smooth but thick shocks on coarse
  grids", local switching to lower-order schemes sharp but oscillating
  shocks (TENO excepted), and filtering alone the largest oscillations; TENO
  and LAD-based schemes mitigate oscillations best at all resolutions, and
  shock capturing has overall "a low impact" on the turbulent scales
  (§IV.B, §V).

## Qualifications

- **Printed slips (Cernetic et al. 2024, arXiv v2).** Eq. (13) prints the
  entropic-function evolution with a factor $\tfrac12$,
  $\mathrm dA_s/\mathrm dt=-\tfrac12\frac{\gamma-1}{\rho^\gamma}p_{\mathrm{av}}\nabla\cdot\boldsymbol u$;
  with $p=(\gamma-1)\rho e_{\mathrm{int}}$ ($e_{\mathrm{int}}$ the specific
  internal energy, page-local), $\mathrm de_{\mathrm{int}}/\mathrm dt=-(p+p_{\mathrm{av}})\nabla\cdot\boldsymbol u/\rho$
  and $\mathrm d\rho/\mathrm dt=-\rho\nabla\cdot\boldsymbol u$, the continuum
  result is $\mathrm dA_s/\mathrm dt=-\frac{\gamma-1}{\rho^\gamma}p_{\mathrm{av}}\nabla\cdot\boldsymbol u$,
  without the $\tfrac12$ *(compiler check, not in the sources)*; the sign
  (entropy grows under compression) is the same. The text speaks of DG
  order 6 at 200 cells where the figure panel is labelled order 5.
- **Internal inconsistency (Chapelier et al. 2024, HAL accepted
  manuscript).** §III.B.e describes SD3DvisP's AV as a bulk viscosity on
  momentum and a thermal diffusivity on energy, none on mass; §III.B.h says
  that for SD3D and CODA it is "a Laplacian operator impacting all
  conservative variables". Table I files H3AMR's BSS model under "LAD".
- **Different measures.** Cernetic et al. judge their AV by sub-cell shock
  width in one- and two-dimensional problems and by spectra of driven
  turbulence; Chapelier et al. judge LAD by shock thickness and
  $\varepsilon_d$ in the supersonic Taylor–Green vortex. The "thick shocks" of
  the latter and the "sub-cell" shocks of the former concern different AV
  forms, codes and tests, so they are not recorded as a contradiction.
- Cernetic et al.'s recommended coefficients are empirical ("from our
  experience"), with no sensitivity study printed.
- Schotte et al. (2026, §4.3) print "the artificial viscosity method
  described in is employed", with the cross-reference missing; their
  artificial viscosity is described in §2.2.
- **Printed forms (Ahn et al. 2023).** Eq. (2) prints the local spectral
  radius as $|u_{01}n_{01}+c_{01}|S_{01}$, with the averaged sound speed
  inside the absolute value; Eq. (6) prints the pressure ratio with
  $\sum_kp_k-p_0$, which for more than one neighbour is not a sum of
  pressure differences (see [shock sensors](/definitions/shock-sensor.md))
  *(compiler check, not in the sources)*. The scheme is credited to Gojon et al. and Ducros et al.
  and its benchmark performance is referred to them, not shown.
- Ghidoni & Noventa (2026) give the AV only in the Appendix, with no
  sensitivity to $C$ and no separate assessment of its effect on the
  transition predictions.

# Citations

- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — arXiv 2401.06841v2: §3.1, Eqs. (12)–(16) (von Neumann–Richtmyer viscous pressure at internal Gauss points, coefficients, cap, motivation); §3.1.1–3.1.2, Figs. 1–2 (Shu–Osher, Liska–Wendroff); §5; Conclusions.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.a, e, g, h, Table I (LAD in CODA and SD3DvisP, BSS in H3AMR, sensors); §IV.A–B, Figs. 5–8 ($\varepsilon_d$ ranking, shock profiles); §V.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §2.2–2.3, §5–6 (entropy-stable filtered Guermond–Popov AV).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.4, Eqs. (15)–(19) (AV shock capturing in HORSES3D).
- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §3.1, Eq. (3-10) (residual-driven AV).
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §1, §3.3, Eqs. (10)–(14) (residual-based diffusivity with upwind cap as stabilization).
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4 (artificial bulk viscosity in charLES).
- [Davidovits et al. (2022)](/sources/davidovits-2022.md) — §II A (artificial viscosity, no physical viscosity).
- [Schotte et al. (2026)](/sources/schotte-2026.md) — HAL hal-05567956v2 (version of record): §2.2 (Laplacian AV with Persson–Peraire sensor and Glaubitz calibration, positivity-preserving limiter in CODA); §4.3, §4.5, §5 (transonic RANS cases, $N=1$ for the shocked M6 wing, $hp$ perspective).
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §III, Eqs. (1)–(6) (modified JST dissipation with Ducros sensor in EDGE, MILES).
- [Ghidoni & Noventa (2026)](/sources/ghidoni-2026-b.md) — Appendix (residual-based directional AV in modal DG RANS); §V (NLR-7301 onset errors).
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §3.1, §4.2 (Persson–Peraire indicator driving HWENO limiting instead of AV).
- [Liang & Fu (2024)](/sources/liang-2024.md) — §1 (artificial viscosity among shock-capturing families).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1 (same).
