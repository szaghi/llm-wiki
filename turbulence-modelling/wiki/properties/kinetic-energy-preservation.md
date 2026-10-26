---
type: Property
title: "Kinetic-energy preservation and split forms"
description: "A discretization is kinetic-energy preserving when its convective terms neither create nor destroy discrete kinetic energy; this page gives the split-form and two-point-flux constructions, kinetic energy as an entropy with entropy-stable added dissipation, and why a dissipation-free baseline is robust but thermalizes without a subgrid model."
status: established
aliases: [KEP, kinetic energy preserving scheme, kinetic-energy-conserving discretization, skew-symmetric form, split-form DG, flux differencing, energy-preserving scheme, entropy-stable discretization]
tags: [kinetic-energy-preserving, entropy-stable, numerical-dissipation, dg, les]
timestamp: 2026-10-26T05:06:00Z
---

# Kinetic-energy preservation and split forms

A semi-discretization of the Navier–Stokes equations is **kinetic-energy
preserving (KEP)** when its convective (advective) terms reproduce at the
discrete level the continuous property that convection only redistributes
kinetic energy: the global discrete kinetic energy changes only through the
viscous, pressure and boundary terms. In the incompressible case this is
obtained by writing the convective term in **skew-symmetric (split) form**; in
element methods it is obtained by a **two-point (flux-differencing) volume
term** with a suitable symmetric flux $f^{\#}$. In scale-resolving simulation
the property removes the artificial dissipation of the convective operator,
which makes the scheme robust in under-resolved turbulence and separates
numerical stability from subgrid modelling.

## Constructions

**Skew-symmetric convection.** Vicente Cruz & Lamballais (2023, §2.1, Eq. 4)
write the incompressible convective term as
$$\tfrac12\Big(u_j\frac{\partial u_i}{\partial x_j}+\frac{\partial u_iu_j}{\partial x_j}\Big),$$
which makes centred spatial differentiation kinetic-energy conserving up to the
time-integration error; with a third-order time scheme their truncated-Euler
runs keep the kinetic energy within 1% of its initial value over
$0\le t\le20$, the loss scaling about as $\Delta t^3$ (§3, §6.2).

**Split-form DG with two-point fluxes.** On Legendre–Gauss–Lobatto nodes the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) has the
summation-by-parts property $(MD)+(MD)^{\mathsf T}=B$, which allows its
strong-form volume term to be replaced by a flux-differencing one. In one
Cartesian direction (Flad & Gassner 2017, Eq. 12; Krais et al. 2021, Eqs. 52–53):
$$\frac{\partial f}{\partial\xi}\Big|_{i}\approx\frac{1}{w_i}\Big(\delta_{iN}\big[f^*-f\big]_{N}-\delta_{i0}\big[f^*-f\big]_{0}\Big)+\sum_{m=0}^{N}2D_{im}\,f^{\#}(U_i,U_m).$$
As recalled by both sources from Gassner, Winters & Kopriva, any consistent and
symmetric two-point flux $f^{\#}$ yields a valid split-form scheme; specific
choices give kinetic-energy preservation (Jameson's definition) or entropy
conservation (Tadmor's), and reproduce known finite-difference split forms of
the advective terms. On curved elements the metric terms enter through their
arithmetic means $\{\!\{\mathcal J a^1_d\}\!\}$ (Krais et al. 2021, Eq. 54).

**The Pirozzoli flux.** The KEP flux used by Flad & Gassner (2017, Eq. 13), and
by Krais et al. (2021, §7.1) following them, is, in the first direction,
$$f^{\#}(U_i,U_m)=\Big(\{\!\{\rho\}\!\}\{\!\{u\}\!\},\ \{\!\{\rho\}\!\}\{\!\{u\}\!\}^2+\{\!\{p\}\!\},\ \{\!\{\rho\}\!\}\{\!\{u\}\!\}\{\!\{v\}\!\},\ \{\!\{\rho\}\!\}\{\!\{u\}\!\}\{\!\{w\}\!\},\ \{\!\{\rho\}\!\}\{\!\{u\}\!\}\{\!\{H\}\!\}\Big)^{\mathsf T},$$
with $\{\!\{\phi\}\!\}$ the arithmetic mean of the two nodal states and $H$
(page-local) the quantity printed $h$ in the energy component, which the source
does not define. Flad & Gassner state that it
is close to the Kennedy–Gruber form, is kinetic-energy preserving within each
element and, when the same flux serves as interface flux $f^*$, across the
whole domain: the scheme then has zero artificial kinetic-energy dissipation
(§2.1). Upwind dissipation can be added back by augmenting the central interface
flux with Lax–Friedrichs or Roe dissipation.

**Entropy-preserving finite-volume fluxes.** [CharLES](/software/charles.md)
builds its low-dissipation fluxes on discrete entropy preservation: as stated by
Goc et al. (2021, §2.3) they conserve entropy globally in inviscid shock-free
flow and kinetic energy in inviscid low-Mach flow; Lozano-Durán et al. (2022,
§II.B) describe the scheme as kinetic-energy conserving and approximately
entropy preserving in the inviscid limit, "thereby limiting the amount of
numerical dissipation"; Griffin et al. (2023, §4) and Agrawal et al. (2022, §IV)
call it low-dissipation and approximately entropy preserving, Griffin et al.
adding an artificial bulk viscosity for discontinuities. The Alya finite-element
code used by Goc et al. (2021, §2.3) relies instead on a Galerkin convective
form that conserves linear and angular momentum and kinetic energy discretely,
with no upwinding. Krais et al. (2021, §7.2) use the entropy-conserving
Chandrashekar flux in the DG cells of their shock-capturing scheme.

**Energy-preserving finite differences with shock capturing.** The GPU code
STREAmS used by [Cogo et al. (2022)](/sources/cogo-2022.md), §2, for DNS of
supersonic and hypersonic boundary layers applies "consolidated, high-order,
energy-preserving schemes" to the convective terms in shock-free regions,
"free of numerical dissipation", and a WENO scheme only where the Ducros
sensor flags shocks; its viscous terms are written in a locally conservative
form "expanded to Laplacian for ensuring finite molecular dissipation at all
resolved wavelengths". For an adiabatic Mach 2.5 boundary layer
[Huang et al. (2022)](/sources/huang-2022.md), §2.2, replace their
limiter-optimized seventh-order WENO by the eighth-order split convective
finite-difference scheme of Pirozzoli (2011), which "runs about twice as fast
as the conventional WENO method" and was shown robust up to edge Mach 4; the
paper does not discuss its energy-preservation properties.

**Catalogue of split forms in a DG code.** [HORSES3D](/software/horses3d.md)
offers the Morinishi, Ducros, Kennedy–Gruber, Pirozzoli, entropy-conserving
and Chandrashekar split forms on Gauss–Lobatto nodes, where the
summation-by-parts property recovers discrete energy or entropy conservation
and improves robustness "especially in the presence of high numerical
aliasing (e.g., under-resolved turbulence)"; the group has extended entropy
stability to the Spalart–Allmaras equations and to a Navier–Stokes/Cahn–Hilliard
model ([Ferrer et al. 2023](/sources/ferrer-2023.md), §3.3, §3.5). Two limits
are stated: the split forms need the Gauss–Lobatto nodes, whereas the
authors call the Gauss–Legendre nodes "more accurate" (§3.3), and the mortar
coupling of faces between elements of different polynomial degree "does not
retain entropy stability" (§3.6).
[Blind et al. (2023)](/sources/blind-2023.md), §2.1, run
[FLEXI](/software/flexi.md) with the skew-symmetric split form and Pirozzoli's
fluxes "to obtain a dissipation-free and kinetic-energy preserving
semi-discrete system", a Roe interface flux and a Vreman subgrid model, for
wall-resolved and wall-modelled LES on adapted grids.

**Energy-preserving central flux in an unstructured finite-volume code.**
In the node-based solver M-Edge the convective face flux is Kok's
skew-symmetric energy-preserving central flux, which "provides no numerical
dissipation", so a Jameson–Schmidt–Turkel matrix dissipation must be added
for stability on hybrid grids ([Carlsson et al. 2023](/sources/carlsson-2023.md),
§2, Eqs. 2–3). The [low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
keeps that flux, extrapolates its face values to cut dispersion and lowers
the fourth-difference dissipation coefficient from the RANS value $1/128$
to $1/512$–$1/1024$, which in their decaying-turbulence and channel tests
removes the excess dissipation of the RANS-level setting (§4.2–4.3). The
authors argue that the dissipation should ideally come only
from the subgrid model (§2.3), the premise of a dissipation-free baseline
discussed below.

## Kinetic energy as an entropy

[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §2, treat kinetic
energy and thermodynamic entropy in one framework. For a convex entropy
$\mathcal E(Q)$ (page-local; $Q$ the conservative variables) the entropy
variables are $W=\partial\mathcal E/\partial Q$; dissipative fluxes written as
$\mathcal B\nabla W$ with $\mathcal B$ symmetric positive semi-definite
dissipate $\mathcal E$ at the rate $(\nabla W)^{\mathsf T}\mathcal B\nabla W\ge0$
(Eqs. 19–22). Kinetic energy $\rho|\boldsymbol u|^2/2$ has
$W=(-|\boldsymbol u|^2/2,u,v,w,0)^{\mathsf T}$ (Eq. 23), the
thermodynamic entropy $-\rho s/(\gamma-1)$ with $s=\ln p-\gamma\ln\rho$ has
the entropy variables printed in Eq. 24. Kinetic energy is **not a strict
entropy**: its balance contains the pressure work
$\int_\Omega\boldsymbol u\cdot\nabla p\,d\Omega$, which cannot be bounded
(Eqs. 33–35), so kinetic-energy "stability" is weaker than entropy stability.
This is the continuous counterpart of the observation of Flad & Gassner
(2017) below that kinetic-energy preservation leaves density and pressure
uncontrolled. For an artificial viscosity $\mu_a$ added to the Navier–Stokes
viscous flux, the kinetic-energy dissipation is
$\mu_a\big(2S_{ij}S_{ij}-\tfrac23(\nabla\cdot\boldsymbol u)^2\big)\ge0$ (Eq. 25),
which is $2\mu_aS^d_{ij}S^d_{ij}$ *(compiler check, not in the sources)*.

On the LGL DGSEM, with the Pirozzoli flux (kinetic energy) or the
Chandrashekar flux (thermodynamic entropy), BR1 viscous terms and a modally
filtered artificial viscosity, they prove the semi-discrete scheme entropy
stable, or kinetic-energy stable up to the pressure work (§5.1, Eq. 118; the
construction is on the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
page). They describe kinetic-energy-preserving schemes as robust and cheaper
for subsonic flow and thermodynamic-entropy schemes as preferred for
supersonic flow (§5.1), and state that entropy-conserving split forms are
not by themselves stable at shocks, because entropy stability rests on
positive density, which oscillations near shocks can violate; shock
capturing must add density regularization (§1).

## Consequences in under-resolved turbulence

**Robustness without dissipation.** The dissipation-free split-form DGSEM
(Pirozzoli flux in volume and interfaces, BR1) is stable for decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) on
$6^3$ elements with $N=7$ ($48^3$ degrees of freedom, cut-off near
$k_c\approx16$), a case where only about 0.9% of the dissipation is resolved;
Flad & Gassner (2017, §3, Fig. 4) report this as the first such result with a
DG scheme. Krais et al. (2021, §7) call KEP split DG a stable scheme for
implicitly modelled LES, and use it for a wall-resolved LES of a NACA 64418
airfoil at $Re_c=10^6$, $M=0.2$ ($N=7$, about 117 million degrees of freedom).
Beck & Kurz (2023, §III A) use the split form in [FLEXI](/software/flexi.md)
for non-linear stability, with an L2Roe interface flux.

**Thermalization.** Without dissipation, energy reaching the cut-off has nowhere
to go. Flad & Gassner (2017, §3) observe an approximate $E(k)\propto k^2$
equipartition spectrum near the cut-off. Vicente Cruz & Lamballais (2023, §6.2,
Figs. 4–7) find the same with skew-symmetric sixth-order compact schemes: the
truncated Euler solution relaxes to a thermalized $E(k)\propto k^2$ state, and
the no-model LES of the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
thermalizes over more than 80% of the wavenumbers at the coarsest mesh and
"dramatically" over-estimates the total dissipation during breakdown, "a
subdissipative operator leads eventually to an overdissipative behaviour". Both
sources therefore add dissipation to the KEP baseline, an explicit model or a
scale-selective numerical one. Mateo-Gabín et al. (2022, §6.1, Fig. 4) do the
same for the inviscid Taylor–Green vortex ($8^3$ elements, $N=8$, Pirozzoli
split form, low-dissipation Roe flux): a Smagorinsky viscosity ($C_s=0.2$)
applied unfiltered is excessively dissipative, while the same viscosity
filtered towards the high modes with a
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
kernel avoids high-wavenumber pile-up and gives a spectrum close to
$k^{-5/3}$.

**Separating stability from modelling.** Flad & Gassner (2017, §1, §4) argue
that adding an explicit model to standard DG [implicit LES](/definitions/implicit-les.md)
is hard because the artificial dissipation interacts with the eddy viscosity,
whereas on a dissipation-free baseline stability and model dissipation are
strictly separate. On that baseline a [Smagorinsky model](/methods/smagorinsky-model.md)
with $C_s=0.12$ beats DG implicit LES at $48^3$ (§4, Fig. 7); a
[dynamic Smagorinsky](/methods/dynamic-procedure.md) model gives better
Reynolds stresses than DG implicit LES in [channel flow](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau=590$ (§6.2). Goc et al. (2021, §2.3) state, recalling Mittal &
Moin, that numerical dissipation is "extremely detrimental" for coarse LES,
which motivates low-dissipation (entropy- and KEP) schemes for
[wall-modelled LES](/methods/wall-modelled-les.md) of aircraft.

**What KEP does not control.** Kinetic-energy preservation constrains momentum,
not density and pressure. Flad & Gassner (2017, §5.1, Fig. 10) find that
neither the KEP split form nor the Smagorinsky model damps pressure and density
fluctuations, so the pressure–dilatation work oscillates strongly; only an
interface flux whose dissipation acts on density and pressure (the low-Mach
L2Roe solver, which scales the velocity jump by the local Mach number) removes
the oscillations, and the authors rank "split form + L2Roe + Smagorinsky" best
overall (§5.1, §6.1). Vicente Cruz & Lamballais (2023, footnote 6) note that
their immersed-boundary treatment is not kinetic-energy conserving.

## Cost

Krais et al. (2021, §7.1) report 1.35 µs per degree of freedom, stage and core
for the split-form airfoil run, larger than in their scaling tests "mostly
because of the extra work of the split-form volume integral". Flad & Gassner
(2017, §6.1) state that split forms cost at least three times less than
polynomial de-aliasing in their in-house code, without timings.

## Qualifications

- KEP is a property of the semi-discrete spatial operator; time integration
  breaks it at the order of the scheme (Vicente Cruz & Lamballais 2023, §6.2).
- The "first" claims of Flad & Gassner (2017, §3, §4) are priority statements
  of the authors.
- That Goc et al. (2021) and Lozano-Durán et al. (2022) describe the charLES
  fluxes slightly differently (entropy and kinetic energy conserved in their
  respective limits; kinetic-energy conserving and approximately entropy
  preserving) is a difference of wording about the same scheme.

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1; §2.1, Eqs. (9), (12), (13); §3, Fig. 4; §4, Fig. 7; §5.1, Fig. 10; §6.1–6.2.
- [Krais et al. (2021)](/sources/krais-2021.md) — §3.3, Eqs. (52)–(54); §7.1 (NACA 64418, Pirozzoli flux, cost); §7.2 (Chandrashekar flux).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1, Eq. (4); §3 (footnote 6); §6.2, Figs. 4–7.
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.3 (charLES and Alya discretizations, numerical dissipation in coarse LES).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B (charLES scheme).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III A (split form and L2Roe in FLEXI).
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4 (charLES scheme, artificial bulk viscosity).
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §IV (charLES, low-dissipation finite volume).
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §1; §2.1–2.3, Eqs. (19)–(35) (entropy variables, kinetic energy as an entropy, pressure work); §3 (Pirozzoli and Chandrashekar fluxes); §5.1, Eq. (118); §6.1, Fig. 4.
- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2 (STREAmS: energy-preserving schemes, WENO with Ducros sensor, Laplacian viscous terms).
- [Huang et al. (2022)](/sources/huang-2022.md) — §2.2 (eighth-order split convective finite differences).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §3.3, §3.5 (split forms in HORSES3D, Gauss–Lobatto requirement, entropy-stable extensions); §3.6 (mortars not entropy stable).
- [Blind et al. (2023)](/sources/blind-2023.md) — §2.1 (Pirozzoli split form in FLEXI for wall-resolved and wall-modelled LES).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §2, Eqs. (2)–(3) (Kok's energy-preserving flux, JST dissipation); §2.3 (dissipation only from the subgrid model).
