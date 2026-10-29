---
type: Method
title: "Artificial-viscosity shock capturing"
description: "Artificial-viscosity shock capturing adds a dissipative term, switched by a shock sensor or built from compression, to stabilize high-order schemes at shocks; this page gives the von Neumann–Richtmyer viscous pressure in modal DG, localized artificial diffusivity, filtered and residual-based forms, and how they compare with order-lowering schemes in compressible turbulence."
status: established
aliases: [artificial viscosity, localized artificial diffusivity, LAD, von Neumann–Richtmyer artificial viscosity, viscous pressure, Persson–Peraire artificial viscosity, entropy-stable artificial viscosity]
tags: [shock-capturing, numerical-dissipation, dg, compressible, implicit-les, entropy-stable]
timestamp: 2026-10-29T05:13:00Z
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

**Localized artificial diffusivity of Kawai–Lele in a compact
finite-difference DNS.** [Kang & Lee (2024)](/sources/kang-2024.md),
§II.B, Eqs. (10)–(14), add to the molecular viscosity and conductivity of
their sixth-order compact finite-difference DNS of a Mach 2.9, 24°
compression ramp an artificial shear viscosity and conductivity
($\mu_{\mathrm{LAD}}$, $\kappa_{\mathrm{LAD}}$ page-local, the source's
$\mu_a$, $\kappa_a$), written in the generalized coordinates $\xi_l$ of
the curvilinear grid:
$$\mu_{\mathrm{LAD}}=C_{\mathrm{LAD},\mu}\,\mathcal G_{\mathrm{tg}}\Big[\rho\,\Big|\sum_{l=1}^{3}\Big[\sum_{m=1}^{3}\Big(\frac{\partial\xi_l}{\partial x_m}\Big)^2\Big]^2\frac{\partial^4S}{\partial\xi^4}\,h^6\Big|\Big],\qquad
\kappa_{\mathrm{LAD}}=C_{\mathrm{LAD},\kappa}\,\mathcal G_{\mathrm{tg}}\Big[\frac{\rho c}{T}\,\Big|\sum_{l=1}^{3}\Big[\sum_{m=1}^{3}\Big(\frac{\partial\xi_l}{\partial x_m}\Big)^2\Big]^2\frac{\partial^4e}{\partial\xi^4}\,h^5\Big|\Big],$$
with $h$ the cube root of the local cell volume, $e$ the specific internal
energy, $C_{\mathrm{LAD},\mu}=0.002$ and $C_{\mathrm{LAD},\kappa}=0.01$ (page-local, the source's $C_\mu$, $C_\kappa$) "taken from previous studies",
and $\mathcal G_{\mathrm{tg}}$ (page-local, the source's double overbar) an
approximate truncated Gaussian filter applied along each grid line, with
weights $3565/10368$ at the centre and $3091/12960$, $1997/25920$,
$149/12960$, $107/103680$ at distances 1 to 4, mirrored at boundaries
(Eq. 14). The weights sum to one and their alternating sum is zero, so
the filter keeps constants and removes the grid-scale mode *(compiler
check, not in the sources)*. The source quantity $S$ of the viscosity is
not defined in the text (see Qualifications). The diffusivity is meant for
oscillations from turbulent structures with large gradients; shocks are
handled in addition by an adaptive compact filter that a modified Ducros
sensor drops from eighth to second order (see
[shock sensors](/definitions/shock-sensor.md) and
[explicit modal filtering](/methods/explicit-modal-filtering.md)).

**Sensor-switched upwind diffusion on a split central flux.** In the
OpenFOAM-based finite-volume LES of supersonic film cooling of
[Wei et al. (2023)](/sources/wei-2023.md), §II C, Eqs. (16)–(19), the
added dissipation is not a viscosity but the numerical-diffusion part of
an AUSM-type flux, added to an energy-preserving split convective flux
only where a compression-only Ducros sensor exceeds 0.05, and not to the
species equations (flux on
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md),
sensor on [shock sensors](/definitions/shock-sensor.md)).

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
The same group's $p$-multigrid DG RANS solver of
[Bulgarini et al. (2025)](/sources/bulgarini-2025.md), §2, Eq. (9),
prints the identical term (logarithmic pressure, $|s_p|+|d_p|$, the factor
$f_p=|\nabla_h\ln p|h_K/N$, $C=0.2$), active in every element "without the
use of any shock sensor" and, they state, introducing viscosity only where
nonphysical oscillations occur; its transonic RAE 2822 case converges with
the multigrid without "any robustness issue with the shock" (§7.2,
Table 7). The isogeometric DG of
[Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), §3.4,
Eqs. (27)–(31), prints the Bassi et al. form in conservative variables,
$\nu_{\mathrm{av}}=C\,h^2|s_p|/|p|$ with $s_p=(\partial p/\partial\boldsymbol q)\cdot\boldsymbol s_k$
and $\boldsymbol s_k$ the lifted jump between numerical and physical normal
inviscid fluxes, along $\boldsymbol b=\nabla p/(|\nabla p|+\epsilon)$,
$C=0.2$, without the $d_p$ and $f_p$ factors of the two papers above
(page-local $\boldsymbol q$ the conserved variables). It replaces the
element size $h_K$ by the minimum distance between element corners,
because the control points of a Bézier element do not interpolate its
borders (after Duvigneau, cited); the term then captures the shock of the
transonic [NACA 0012](/benchmarks/naca-0012-airfoil.md) on adapted meshes
(§6.2; see [shock sensors](/definitions/shock-sensor.md)).

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

**Bulk artificial viscosity in a spectral-difference DNS.**
[Tonicello et al. (2022)](/sources/tonicello-2022.md), §2.2, Eqs.
(2.6)–(2.10), App. B, regularize the shocks of a DNS of a Mach 2.91
compression–expansion ramp (spectral difference of degree $N=5$, the
source's order $N=6$; see [spectral difference](/methods/spectral-difference-method.md))
with an element-wise constant bulk artificial viscosity $\mu_{b,\mathrm{AV}}$
(registry §11; the source's $\beta_{AV}$) added to the viscous stress, and a
matching artificial conductivity:
$$\sigma_{ij}=2\mu S^d_{ij}+\mu_{b,\mathrm{AV}}\,\frac{\partial u_k}{\partial x_k}\,\delta_{ij},\qquad \kappa_{\mathrm{av}}=\frac{\mu_{b,\mathrm{AV}}c_p}{Pr_{\mathrm{AV}}},\qquad Pr_{\mathrm{AV}}=Pr\,\big\{1+\exp[-4(M(\boldsymbol x)-3)]\big\},$$
($\kappa_{\mathrm{av}}$ page-local, $Pr_{\mathrm{AV}}$ registry §11), the Mach-dependent
artificial Prandtl number avoiding "unnecessary thermal dissipation" at low
Mach number. $\mu_{b,\mathrm{AV}}=\rho f(s)$, with $f$ a sinusoidal ramp from 0
to $\varepsilon_0=C_\varepsilon\lambda_{\max}h/(N+1)$ ($\lambda_{\max}$ the
largest wave speed in the domain; $C_\varepsilon$ not printed) of a modal
decay sensor $s$, self-calibrated on a manufactured solution and multiplied
by a Ducros-type factor that is non-zero only in compression (formula on
[shock sensors](/definitions/shock-sensor.md)); a Zhang–Shu
positivity-preserving limiter is applied at every Runge–Kutta stage (App. C).
The authors state that the Ducros factor keeps the viscosity off at walls,
where "unlike eddy viscosity, artificial viscosity does not vanish", and in
vortical regions; the mean $\mu_{b,\mathrm{AV}}/\mu$ is non-zero only near the
shock (Fig. 12) and the limiter's time–span-averaged activation flag peaks
at about $10^{-4}$ (Fig. 13). They add the AV contribution to the resolved
kinetic-energy budget,
$$K_{\mathrm{av}}=\frac{\partial}{\partial x_j}\Big(\mu_{b,\mathrm{AV}}\frac{\partial\tilde u_k}{\partial x_k}\tilde u_j\Big)-\mu_{b,\mathrm{AV}}\Big(\frac{\partial\tilde u_k}{\partial x_k}\Big)^2$$
(the source's $K_5$, a flux part and a sink part), and find it of order
$10^{-5}$ in units of $\rho_\infty u_\infty^3/\delta$, small against the
other terms and dominated by the flux part (§4.1, Fig. 18); the budget
itself is on [energy backscatter](/definitions/energy-backscatter.md). The
same bulk-viscosity form motivates their proposal of a bulk-viscosity
subgrid model for the trace of the SGS stress (§5; see
[bulk viscosity](/definitions/bulk-viscosity.md)).

**Artificial diffusion on the mass flux only, as an LES closure.**
[Svärd (2022)](/sources/svard-2022.md), §4, Eqs. (20)–(25), modifies the
entropy-conservative, kinetic-energy-preserving two-point flux of
Chandrashekar by adding a density diffusion
$-\lambda^\rho\Delta\rho$ to the mass flux only, with
$\lambda^\rho=|\bar u|/2+|\Delta u|/4$ (arithmetic mean and jump of the two
states; page-local), and reusing that mass flux inside the momentum and
energy fluxes, so that momentum and energy are diffused by the physical
terms alone; Proposition 4.1 states that the scheme is conservative,
entropy stable, at least as diffusive as a kinetic-energy-preserving flux,
density-positive and linearly stable in the continuity equation (proofs on
[entropy conservation](/properties/entropy-conservation.md)). A scaling
argument (§3.1) identifies upwind-type artificial viscosity with an eddy
viscosity $\nu_t\sim h\max(|u_i|,|u_{i+1}|)$ and a turbulent cell Reynolds
number of order one, which the author says "can not be ruled out as
subgrid-scale models"; the scheme runs the Shu–Osher problem stably "without
additional artificial diffusion" at the strong shock (§5.1, Fig. 1).
Adding the same diffusion to all variables (Eqs. 42–43) removes spurious
roll-ups in a Kelvin–Helmholtz test but is "significantly more diffusive"
and is dropped (§5.2, Table 4). The use as implicit LES is on
[implicit LES](/definitions/implicit-les.md).

**LAD in flux reconstruction for real-fluid shock tubes.**
[Ruggeri et al. (2022)](/sources/ruggeri-2022.md), §VI, run their
fourth-order [flux-reconstruction](/methods/flux-reconstruction.md) shock
tube of supercritical CO$_2$ with the localized
artificial diffusivity of Haga & Kawai (no formula or coefficient printed),
as the setting in which they compare interface fluxes; at fourth order the
differences between exact, Rusanov and neural-network Riemann solvers shrink,
the largest remaining at the density contact, where Rusanov oscillates most,
because "with high order, the interfaces of the mesh have a less important
role than for order 1" (Fig. 7; the networks are on
[physics-informed neural networks](/methods/physics-informed-neural-network.md)).

**A survey for discontinuous schemes.** The review of high-order
discontinuous schemes for multiphase and multicomponent flows of
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §4.2, traces DG
artificial viscosity from Johnson's form, of magnitude proportional to
$h^2|R_e|$ ($R_e$ the local element residual, page-local), which they
criticize because "larger residual magnitude does not always correspond
to the solution near the discontinuity", to the sensor-switched
localized viscosity of Persson & Peraire, scaling as $h/N$, which gives
subcell shock resolution (all cited). They group the later work on three
axes: the indicator (inter-element jump, entropy residual, intra-element
pressure jump, pressure gradient, neural network), the smoothness of the
viscosity field (linear interpolation, filtering, PDE-based fields) and
its magnitude (CFL arguments, stability eigenvalues, a non-oscillatory
condition, sequential adaptation for steady problems). For LES with
discontinuous schemes they report that artificial-viscosity formulations,
or filtered forms such as the entropy-stable
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
of Mateo-Gabín et al., have become more popular than limiting, which
stays "too intrusive for high-order solutions" even with a good sensor;
the dissipation of either can smear smooth extrema and kill small
scales. They also use artificial viscosity together with the conservative
$L^2$-projection of the equation of state for interfaces with variable
thermodynamics (see
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).
On the parameters the review prints two statements: in §4.2 that tuning
"can be easily done during the course of LES run", since LES needs long
integration, and in §7 that artificial viscosity "continues to be
problematic due to the dependence on problem-specific parameters". No
test of either is shown.

**An open item in 2012.** The first High-Order CFD Workshop lists robust,
parameter-free, accuracy-preserving shock capturing that also converges for
steady problems among the four pacing items of high-order methods:
artificial viscosity "involves user-specified parameters", solution
limiting "often causes iterative convergence to stall", and the surveyed
participants add that subcell resolution in shocked cells may be needed
([Wang et al. 2013](/sources/wang-2013.md), §2 Q5, §6). For non-smooth
problems the workshop found that high-order accuracy was not attained and
that there was "not enough evidence" to rank high against low order (§6);
on the transonic NACA 0012 the benefit of $N=2$ over $N=1$ was "not as
great as for smooth problems" (§5.2).

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
[Deng et al. (2022)](/sources/deng-2022.md), §1, list central schemes with
artificial viscosity or diffusivity among the hybrid options whose
dissipation must not "overwhelm" the small scales, and adjust the
dissipation of a BVD reconstruction instead (see
[WENO](/methods/weno-scheme.md)); [Ma et al. (2022)](/sources/ma-2022.md),
§1, list added artificial diffusivity among nonlinear compact schemes and
use a nonlinear compact interpolation; and
[Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), §1, judge artificial
dissipation competitive with filtering in cost but in need of a sensor, and
stabilize under-resolved flux reconstruction with an optimized modal filter
([explicit modal filtering](/methods/explicit-modal-filtering.md)).
Two sources add no artificial viscosity:
[Cheng et al. (2023)](/sources/cheng-2023-b.md), §2.2, capture shocks
with a bounded (TVD) reconstruction alone (see [WENO](/methods/weno-scheme.md)),
and [Fureby & Nilsson (2023)](/sources/fureby-2023.md), §3.4, name
localized artificial diffusivity only as an alternative they do not use.
In the review of the canonical shock–turbulence interaction of
[Cuadra et al. (2025)](/sources/cuadra-2025.md), §III A 1, artificial
viscosity (von Neumann–Richtmyer, Jameson et al., and the LES-oriented
forms of Cook 2007 and Mani et al. 2009, all cited) is one of the two
shock-capturing classes next to nonlinear ENO/WENO/TENO reconstructions,
"less invasive", with similar stabilization and "sometimes more
dissipation"; both need a grid fine enough to capture all scales of shock
wrinkling (see [shock-generated turbulence](/results/shock-generated-turbulence.md)).
The moving-mesh DG of [Zou et al. (2025)](/sources/zou-2025-b.md), §II B,
judges artificial viscosity parameter-dependent and over-dissipative, and
reconstruction-based capturing hard in complex geometry, and uses a
positivity-preserving limiter with an unstructured WENO limiter instead,
in two-dimensional laminar runs of a cylinder with synthetic jets (no
troubled-cell indicator or parameter printed). The entropy correction of
[Alberti et al. (2025b)](/sources/alberti-2025-c.md), §II A 1, is likened
by its authors to artificial viscosity and to the entropy viscosity of
Guermond et al., but they state that it is "not designed to have
shock-capturing capabilities" (see
[entropy conservation](/properties/entropy-conservation.md)).
Three further sources on discontinuous high-order methods review
artificial viscosity and choose another route:

- [Liu & Yuan (2023)](/sources/liu-2023-b.md), §1, object that local
  artificial dissipation for flux reconstruction needs an extra
  reconstruction of the solution gradient and problem-dependent empirical
  parameters, and use an a posteriori
  [subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
  limiter for one-dimensional detonations;
- [Potluri et al. (2023)](/sources/potluri-2023.md), §1, survey for
  hypersonic finite-element and DG solvers the streamline-upwind
  (SUPG) stabilization with artificial viscosity and the smooth PDE-based
  artificial viscosities (Barter & Darmofal and later work, Ching et al.
  among them), and adopt the subcell blending of Hennemann et al. for
  laminar hypersonic interactions;
- [Shi & Yan (2023)](/sources/shi-2023.md), §I, cite the
  Persson–Peraire viscosity and the comparison of physical (bulk) and
  Laplacian viscosities by Tonicello et al. (2022) for a ramp interaction,
  and limit their flux-reconstruction implicit LES of a Mach 2.9 ramp with
  a WENO limiter and a positivity-preserving limiter instead (see
  [WENO](/methods/weno-scheme.md)).

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

**The same comparison against an entropy filter.** In the software paper
of [PyFR](/software/pyfr.md), [Witherden et al. (2025)](/sources/witherden-2025.md),
§5.1, Figs. 11–12, Table 1, rerun this case ($16^3$ to $128^3$ hexahedra,
$N=3$, Gauss–Lobatto points) with positivity-preserving entropy filtering
instead of artificial viscosity and plot their $\varepsilon_d$ beside the
data of Chapelier and co-workers: the PyFR profiles are closer to the
$2048^3$ TENO reference than those of CODA and SD3D (both AV) and FLEXI
(subcell finite volumes) at equal resolution and order, which the authors
read as "less shock dissipation" and as evidence that entropy filtering
"does not introduce excessive numerical dissipation" (the filter is on
[explicit modal filtering](/methods/explicit-modal-filtering.md)). PyFR
itself also offers Persson–Peraire-type AV (§3.2), which the authors
describe as requiring parameterisation and as able to reduce the maximum
stable explicit time step; they give no results with it.

## Comparison with entropy-stable stabilization in DGSEM

[Bilocq et al. (2025)](/sources/bilocq-2025.md) compare, in one Cartesian
collocated Gauss–Legendre DGSEM with local Lax–Friedrichs flux and
incomplete interior penalty, five discretizations of under-resolved
compressible turbulence with shocks or shocklets: unstabilized DG, DG with
Laplacian AV (DG-AV), fully entropy-stable DG on Gauss–Legendre and on
Gauss–Lobatto nodes, and a selective scheme DG-ES that uses the
entropy-stable discretization only in sensor-flagged cells. DG-AV is the
Persson–Peraire Laplacian $\nabla\cdot(\mu_{\mathrm{av}}\nabla\boldsymbol q)$
with the Hennemann calibration of the modal-energy sensor and the scaling
of Vandenhoeck et al. (§3.5, Eqs. 29–31):
$$\mu_{\mathrm{av}}=\alpha\,\mu_{\mathrm{av},0},\qquad \mu_{\mathrm{av},0}=C_{\mathrm V}\,\frac{h}{N}\,\lambda_{\max},\qquad C_{\mathrm V}=0.27\,\frac{M_\infty-1}{M_\infty},$$
elementwise constant, with $\alpha\in[0,1]$ the logistic sensor value
(on [shock sensors](/definitions/shock-sensor.md)), $\lambda_{\max}$ the
largest wave speed and $M_\infty$ bounded below by 1.2 to keep
$C_{\mathrm V}$ positive ($C_{\mathrm V}$ page-local, the source's $c$;
the Vandenhoeck form is stated to remove the need for parameter tuning).
Findings (§4, §5):

- **Cost and robustness.** DG-AV costs 1.07–1.08 times the unstabilized DG,
  DG-ES 1.25–1.27 and the entropy-stable Gauss–Legendre scheme 1.86–2.27
  times (Tables 3, 8); where DG-AV is the baseline, DG-ES costs 1.21–1.28
  and the entropy-stable Gauss–Legendre scheme 1.58–1.68 times DG-AV
  (Tables 10, 12; 2× AMD EPYC 7763). DG-AV stabilizes every coarse mesh
  on which the unstabilized DG diverges (Tables 1, 6). Its largest stable
  CFL is 0.8 on the strong vortex/shock case, where the schemes with an
  entropy projection drop to 0.16 and 0.08 (Table 9).
- **Shocks.** In the supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  ($M_0=1.25$, $Re=1600$, $N=3$) DG-AV gives a thicker but
  oscillation-free shock and underpredicts the dilatational dissipation at
  all resolutions because it "reduces shock intensity", while the entropy-stable
  schemes overpredict it; its solenoidal dissipation is among the highest,
  close to the unstabilized DG at the two finest grids (§4.2.3, Figs. 7,
  9–10).
- **Vortices and post-shock turbulence.** In the vortex/shock interaction
  DG-AV captures the shock cleanly but under-resolves the vortex; since
  the sensor never fires inside the vortex, the authors attribute the
  damping to the earlier interaction with the shock (§4.3.3, Figs. 12–14); in the
  canonical shock–turbulence interaction ($M=1.28$, $M_t=0.22$,
  $Re_\lambda=40$) the entropy-stable methods capture the post-shock
  amplification of $R_{11}$ and $R_{22}$ better than DG-AV on the coarse
  grid (§4.4.3, Fig. 15). Their conclusion: "even modest dissipation"
  added near shocks degrades the post-shock turbulence although no
  stabilization acts there.
- **Sensitivity.** DG-AV is strongly sensitive to the detector calibration
  and to the node set: a collocated Gauss–Legendre basis beats
  Gauss–Lobatto interpolation with Gauss–Legendre quadrature, a
  sensitivity DG-AV shows, in the authors' words, "somewhat unexpectedly"
  (§4.1.5, Figs. 3–5).

They recommend DG-AV when robust and efficient shock resolution is the
main concern, DG-ES when under-resolved turbulent structures must be
captured accurately (§5); the entropy-stable side is on
[entropy conservation](/properties/entropy-conservation.md), the
dissipation measure on [numerical dissipation](/properties/numerical-dissipation.md).

## Qualifications

- **Printed forms in Bilocq et al. (2025).** The AV term is printed as
  $\nabla\cdot(\mu_{\mathrm{av}}\nabla u)$ with $u$ the symbol of the
  conservative variables, and Eq. (31) writes $h/p$ with italic $p$, the
  symbol also used for pressure, while the degree is written p elsewhere
  and $N$ in the quadrature statements.
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
- Tonicello et al. (2022) restrict the name "direct numerical simulation"
  to the turbulent scales: the shocks stay under-resolved and regularized
  by the artificial terms (§2.2). Their constant $C_\varepsilon$ and the
  calibrated sensor thresholds are not printed.
- **Printed slips (Kang & Lee 2024).** The quantity $S$ in Eq. (12) of
  the artificial viscosity is not defined in the text; the energy flux of
  Eq. (3) is printed with the strain rate $S_{ij}u_i$ where the viscous
  stress of Eq. (2) belongs, and the heat flux as
  $q_i=-\kappa\,\partial T_i/\partial x_j$. The diffusivity constants are
  taken from earlier studies with no sensitivity shown.
- Lv & Ekaterinaris (2023) is a review: the scalings, groupings and the
  preference for artificial viscosity over limiting in LES are reported
  from the cited works, with no computation of the review's own.
- Svärd's (2022) identification of upwind dissipation with a subgrid
  model is a scaling argument (§3.1), not tested against subgrid physics;
  the same paper calls the Rusanov (E-scheme) flux "very diffusive and
  generally considered inappropriate for turbulent simulations" (§3).

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
- [Ruggeri et al. (2022)](/sources/ruggeri-2022.md) — §VI, Fig. 7 (Haga–Kawai LAD in fourth-order flux reconstruction; interface fluxes at high order).
- [Wang et al. (2013)](/sources/wang-2013.md) — §2, Q5; §5.2; §6 (shock capturing as a pacing item; artificial viscosity against limiting).
- [Liu & Yuan (2023)](/sources/liu-2023-b.md) — §1 (objections to local artificial dissipation in flux reconstruction).
- [Potluri et al. (2023)](/sources/potluri-2023.md) — §1 (SUPG with artificial viscosity and PDE-based smooth artificial viscosity for hypersonic DG and finite elements, reviewed).
- [Shi & Yan (2023)](/sources/shi-2023.md) — §I (Persson–Peraire and physical against Laplacian viscosity, cited).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §2.2, Eqs. (2.6)–(2.10), App. B–C (bulk artificial viscosity, Mach-dependent artificial Prandtl number, modal sensor with Ducros factor, positivity limiter); §3.2, Figs. 12–13; §4.1, Eq. (4.13), Fig. 18 (AV term of the resolved kinetic-energy budget).
- [Svärd (2022)](/sources/svard-2022.md) — §3.1 (upwind artificial viscosity as a subgrid model, cell Reynolds number); §4, Eqs. (20)–(25), Proposition 4.1 (mass-flux artificial diffusion); §5.1–5.2, Fig. 1, Table 4.
- [Deng et al. (2022)](/sources/deng-2022.md) — §1 (artificial viscosity among hybrid shock-capturing options).
- [Ma et al. (2022)](/sources/ma-2022.md) — §1 (artificial diffusivity among nonlinear compact approaches).
- [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md) — §1 (artificial dissipation against filtering: cost and sensor).
- [Cheng et al. (2023)](/sources/cheng-2023-b.md) — §2.2 (shock capturing by a TVD reconstruction, no artificial viscosity; passing).
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.4 (localized artificial diffusivity named, not used; passing).
- [Kang & Lee (2024)](/sources/kang-2024.md) — §II.B, Eqs. (10)–(14) (Kawai–Lele localized artificial diffusivity in curvilinear compact finite differences, $C_\mu=0.002$, $C_\kappa=0.01$ as printed, truncated Gaussian filter).
- [Wei et al. (2023)](/sources/wei-2023.md) — §II C, Eqs. (16)–(19) (Ducros-switched AUSM-type diffusion on a split energy-preserving flux).
- [Witherden et al. (2025)](/sources/witherden-2025.md) — §3.2 (Persson–Peraire-type AV in PyFR: parameterised, time-step penalty); §5.1, Figs. 11–12, Table 1 (entropy filtering against the AV and subcell solvers of the supersonic Taylor–Green comparison).
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §4.2 (survey of DG artificial viscosity: Johnson, Persson–Peraire, three axes of extension, preference over limiting in LES, tuning); §7 (parameter dependence).
- [Bilocq et al. (2025)](/sources/bilocq-2025.md) — §3.5, Eqs. (29)–(31) (Persson–Peraire Laplacian AV, Hennemann calibration, Vandenhoeck scaling); §4.1–4.4, Tables 1–12, Figs. 3–5, 7, 9–15 (comparison with entropy-stable and selective entropy-stable DG: cost, CFL, dissipation, post-shock turbulence, sensitivity); §5.
- [Bulgarini et al. (2025)](/sources/bulgarini-2025.md) — §2, Eq. (9) (sensor-free residual-based directional AV in $p$-multigrid DG RANS); §7.2, Table 7.
- [Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md) — §3.4, Eqs. (27)–(31) (Bassi et al. AV with corner-distance element size on Bézier elements); §6.2.
- [Cuadra et al. (2025)](/sources/cuadra-2025.md) — §III A 1 (artificial viscosity as a shock-capturing class for shock–turbulence interaction; review).
- [Zou et al. (2025)](/sources/zou-2025-b.md) — §II B (AV judged parameter-dependent and over-dissipative; limiters used instead; 2-D laminar runs).
- [Alberti et al. (2025b)](/sources/alberti-2025-c.md) — §II A 1 (entropy correction likened to AV, not a shock-capturing device).
