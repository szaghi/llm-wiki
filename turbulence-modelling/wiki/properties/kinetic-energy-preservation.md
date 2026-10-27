---
type: Property
title: "Kinetic-energy preservation and split forms"
description: "A discretization is kinetic-energy preserving when its convective terms neither create nor destroy discrete kinetic energy; this page gives the split-form families and two-point fluxes, kinetic energy as an entropy, why a dissipation-free baseline is robust but thermalizes or disperses without help, and what it does not control."
status: established
aliases: [KEP, KEEP, kinetic-energy and entropy preserving scheme, kinetic energy preserving scheme, kinetic-energy-conserving discretization, skew-symmetric form, split-form DG, flux differencing, energy-preserving scheme, entropy-stable discretization]
tags: [kinetic-energy-preserving, entropy-stable, numerical-dissipation, dg, les]
timestamp: 2026-10-27T06:08:00Z
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
[Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §II.A, use in HORSES3D
the split form with Chandrashekar averaging, a low-dissipation Roe flux and
BR1 (no penalty) or BR2 (penalty 1.5, "necessitated" by walls) for the
Taylor–Green vortex and channel flow, but the standard form for decaying
isotropic turbulence.
[Blind et al. (2023)](/sources/blind-2023.md), §2.1, run
[FLEXI](/software/flexi.md) with the skew-symmetric split form and Pirozzoli's
fluxes "to obtain a dissipation-free and kinetic-energy preserving
semi-discrete system", a Roe interface flux and a Vreman subgrid model, for
wall-resolved and wall-modelled LES on adapted grids.
[Gao et al. (2022)](/sources/gao-2022.md), §3.1, run the same split-form
FLEXI with Pirozzoli's two-point volume flux "for stability of
under-resolved turbulence", with no subgrid model, a Harten–Hyman-fixed
approximate Riemann solver and BR1, for an implicit LES of an oblique
shock/turbulent-boundary-layer interaction, with finite-volume subcells at
the shocks (see
[subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).

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

**The one-parameter family of locally conservative split forms.** As
recalled by [Bernades et al. (2023)](/sources/bernades-2023.md), §3.1.1,
Eqs. (9)–(11), from Coppola et al., the semi-discrete convective term
$C_{\rho\phi}$ of a quantity $\rho\phi$ ($\phi=1$ for mass, $u$ for
momentum; page-local symbols, $D_x$ a centred difference matrix with
summation by parts) can be written in five forms: divergence
$C^D=D_x(\rho u\phi)$, $C^\phi=\phi D_x(\rho u)+\rho uD_x\phi$,
$C^u=uD_x(\rho\phi)+\rho\phi D_xu$, $C^\rho=\rho D_x(u\phi)+\phi uD_x\rho$,
and the fully split $C^L$. The KEP forms that remain locally conservative
are the family
$$C^{\mathrm{KEP}}_{\rho\phi}=a_{\mathrm K}\,\frac{C^D_{\rho\phi}+C^\phi_{\rho\phi}}{2}+(1-a_{\mathrm K})\,\frac{C^u_{\rho\phi}+C^\rho_{\rho\phi}}{2},$$
with $a_{\mathrm K}=0$ the Feiereisen form, $a_{\mathrm K}=1$ the "C" form
and $a_{\mathrm K}=\tfrac12$ the **Kennedy–Gruber–Pirozzoli (KGP)** form
(page-local $a_{\mathrm K}$, the source's $\xi$); $C^L$ is excluded because it
cannot be written as a difference of fluxes. The KGP form has the
second-order flux
$F_{i+1/2}=\tfrac18(\rho_i+\rho_{i+1})(u_i+u_{i+1})(\phi_i+\phi_{i+1})$, i.e.
$\{\!\{\rho\}\!\}\{\!\{u\}\!\}\{\!\{\phi\}\!\}$ (footnote 3), and "proved to
be particularly robust". With $\phi=1$ and $\phi=u$ it preserves mass,
momentum and kinetic energy by convection, globally and locally. Bernades et
al. state that the KEP property "depends only" on the discretization of the
continuity and momentum equations (§3.1.2); the energy discretization decides
instead [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md).

**The KEP condition in flux form.** [Aiello et al. (2026)](/sources/aiello-2026.md),
§3.2, Eq. (7), state the same separation for a node-indexed second-order
finite-difference scheme with face fluxes $\mathcal F_{\rho\phi}$
(page-local): as recalled from Jameson and Veldman, kinetic energy is
preserved when the convective momentum flux is the mass flux times the
arithmetic mean of the velocity, $\mathcal F_{\rho u}=\mathcal F_\rho\{\!\{u\}\!\}$,
whatever the mass flux $\mathcal F_\rho$ and the pressure term; the induced
kinetic-energy flux is then $\mathcal F_\rho u_iu_{i+1}/2$. KEP is
therefore independent of the internal-energy flux, and the remaining
freedom (the face density inside $\mathcal F_\rho$ and the internal-energy
flux) can be spent on
[entropy conservation](/properties/entropy-conservation.md). For the same
reason KEP survives a change of the gas model, whereas entropy conservation
designed for a calorically perfect gas does not (§3.2). Kinetic energy and
entropy are, in their words, induced variables of the discretization
(§3.1).

The same five forms and the KGP choice are recalled by
[Wang et al. (2024)](/sources/wang-2024.md), §2.3, Eqs. (5)–(11), for the
second-order scheme **KGP2** of a cell-centred compressible finite-difference
solver; they print the KGP weights as "$\xi=1/2$, $\alpha=\beta=\delta=1/4$,
and $\varepsilon=0$" without defining $\xi$ or giving the weight of $C^u$.
With $a_{\mathrm K}=\tfrac12$ the family above puts weight $\tfrac14$ on each
of $C^D$, $C^\phi$, $C^u$, $C^\rho$ and none on $C^L$, so their $\xi$ is
Bernades et al.'s and the missing weight is $\tfrac14$ *(compiler check, not
in the sources)*.

**Kennedy–Gruber volume flux in a DG turbomachinery code.** The DGSEM of
DLR's TRACE solver used by [Morsbach et al. (2024)](/sources/morsbach-2024.md),
§2, for implicit LES of a low-pressure-turbine cascade stabilizes the
collocated Legendre–Gauss–Lobatto scheme ($N=5$) with the split formulation
and the kinetic-energy-preserving two-point volume flux of Kennedy and
Gruber, a Roe interface flux and BR1 viscous terms with a central flux and no
penalty, which the authors state is stable "in combination with a stable
advective discretisation" (citing Gassner et al.); no explicit subgrid model
is used.

**Entropy-conserving split form in a transonic DG implicit LES.** In the
same TRACE DGSEM, [Klose et al. (2025)](/sources/klose-2025.md), §2, use
the entropy-conserving split form of Chandrashekar "together with the
corresponding Riemann solver", BR1 viscous fluxes with a central flux and
$N=3$, for an implicit LES of a transonic
[compressor cascade](/benchmarks/compressor-cascade.md); they state that
kinetic-energy or entropy-conserving split forms "cancel numerical errors
and stabilize the high-order scheme", and add
[subcell finite-volume blending](/methods/subcell-finite-volume-shock-capturing.md)
at the shocks.

**Split-form flux reconstruction.** The nonlinearly stable
[flux reconstruction](/methods/flux-reconstruction.md) assessed by
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md), §2.7, uses the same
split-form volume term (with a Hadamard product and Chan's skew-symmetric
stiffness operator) with the entropy-conserving Ismail–Roe flux as
baseline. On the viscous Taylor–Green vortex at $Re=1600$, $M_\infty=0.1$,
$96^3$ degrees of freedom, swapping it for the Kennedy–Gruber (KEP), Chandrashekar
(entropy-conserving and KEP) or Chandrashekar–Ranocha (also
pressure-equilibrium preserving) flux gives "nearly indistinguishable"
spectra, kinetic energy, dissipation and enstrophy, Kennedy–Gruber being
the cheapest (§3.1.6, Fig. 16; see
[entropy conservation](/properties/entropy-conservation.md)).

**Pirozzoli split flux on GPUs.** The GPU DGSEM code
[GALÆXI](/software/galaexi.md) keeps FLEXI's split-flux formulation of
Gassner et al. with Pirozzoli's kinetic-energy-preserving two-point flux, on
LGL nodes, as its remedy for aliasing in under-resolved runs, the
alternatives named being over-integration and filtering
([Kurz et al. 2025](/sources/kurz-2025.md), §2.2). The shared-memory volume
integral keeps the structure of the standard one (App. A); the two-point
evaluation "increases the computational cost considerably" (§2.2), and the
volume integral, of $O(N^4)$ operations per element against $O(N^3)$ or
less for the other routines, takes 39% of the run time of a split-form
case at $N=7$ (Table 1, Fig. 5).

**Kinetic-energy- and entropy-preserving central finite differences
(KEEP).** [Maejima & Kawai (2025)](/sources/maejima-2025.md), §2, run DNS
and LES of compressible channel flow at $Re_\tau\approx1000$, $M_b\approx0.1$,
with the second-order kinetic-energy- and entropy-preserving split-form
central scheme of Kuya, Totani & Kawai, non-dissipative, chosen so that the
subgrid dissipation of the [super-resolution SGS model](/methods/super-resolution-sgs-model.md)
they train is not contaminated by numerical dissipation. In the code
comparison of [Chapelier et al. (2024)](/sources/chapelier-2024.md),
§III.B.b–c, the SPADE solver uses the same family (Kuya et al., Totani et
al.; orders 2 to 8, order 8 in the runs) blended with a third-order upwind
flux by the Ducros sensor (see [WENO and hybrid schemes](/methods/weno-scheme.md)),
and OpenSBLI offers central differences of arbitrary order in quadratic and
cubic split forms (Coppola et al., as recalled). On the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $64^3$ the two
dissipation-free central codes, SPADE and NS3D, predict the kinetic energy
very accurately up to $t\approx12$ and slightly too high afterwards, which
the authors explain by a small-scale pile-up near the cut-off without
subgrid closure (§IV.A, Fig. 5), the thermalization discussed below.

**Three split forms against relaxation filtering on central differences.**
[Volpiani (2024)](/sources/volpiani-2024.md), §2.2.3, Eqs. (9)–(17),
compares in the Python code BASIC three split forms of the convective term
$C=\partial(\rho u_j\phi)/\partial x_j$, $\phi\in\{1,u_i,e\}$, written with
the five forms of Coppola et al. ($C^D$, $C^\phi$, $C^u$, $C^\rho$ as above):
SF1 (Feiereisen et al.) $\tfrac12C^D+\tfrac12C^\phi$ for momentum and
energy only; SF2 (Ducros et al.) $\tfrac12C^D+\tfrac12C^u$ for all
equations; SF3 (Kennedy–Gruber) $\tfrac14(C^D+C^u+C^\phi+C^\rho)$ for all
equations, which is the Kennedy–Gruber family at $\alpha=\beta=1/4$
(page-local parameters) and, as Volpiani recalls from Coppola et al., conserves the
generalized energy $\rho\phi^2/2$. The energy equation is split on the
total specific enthalpy $e+p/\rho$, after Pirozzoli (2010), not on $\rho e$
and pressure separately; the Blaisdell et al. form applied to momentum and
energy "was not robust enough and made computations diverge" (§4). The
alternative stabilization is the relaxation filtering of the divergence
form (see [explicit modal filtering](/methods/explicit-modal-filtering.md)).
On the inviscid compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $64^3$ ($M=0.085$) the normalized kinetic energy at $t=5$ is 0.999 for
SF1 and SF2 and 0.998 for SF3 at every stencil width, against 0.983 to
0.986 for the eleven-point filtered schemes and 0.176 for the three-point
one (Table 1); SF1 and SF3 conserve kinetic energy, "in agreement with
Pirozzoli (2010)", and SF2, "not formally conservative", loses a few
percent by $t=10$; all split forms keep a monotonic enstrophy history
(§4, Fig. 4). The price is cost: per 100 iterations per processor the
eleven-point runs take 78.9 s filtered, 115.9 s (SF1), 156.2 s (SF2) and
298.9 s (SF3), from $(1+2N_p)$ operations per derivative and filter
against $(8+6N_p)$ for SF1 and SF2 and $(20+14N_p)$ for SF3 ($2N_p+1$ the
stencil width, page-local) (Table 1, §4).

**Arbitrary-order skew-symmetric fluxes in a shock-capturing hybrid.**
[Liang & Fu (2024)](/sources/liang-2024.md), §2.3, Eqs. (21)–(30), write
the quadratic (Feiereisen) and cubic (Kennedy–Gruber) split forms of
$\partial(\rho\phi u)/\partial x$ and recall, from Pirozzoli, that the
interface flux $\{\!\{\rho\}\!\}\{\!\{\phi\}\!\}\{\!\{u\}\!\}$ recovers the
second-order cubic form in conservative form, and that it extends to order
$2L$ as
$$\hat f_{i+1/2}=2\sum_{\ell=1}^{L}c_\ell\sum_{m=0}^{\ell-1}\mathcal A_{i-m,\ell}(\rho,\phi,u),\qquad
\mathcal A_{i,\ell}(f,g,h)=\tfrac18(f_i+f_{i+\ell})(g_i+g_{i+\ell})(h_i+h_{i+\ell}),$$
with $c_\ell$ the coefficients of a centred first derivative ($c_\ell$,
$\mathcal A$ page-local). They take $L=4$ and dispersion-optimized
sixth-order $c_\ell$ (see
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)),
and split the energy flux into total-energy convection and a pressure-work
term $\partial(up)/\partial x$, each in the same two-point form. They state,
citing others, that the cubic form is more robust than the quadratic one.
In TENO-S this flux is used, in physical variables and without
characteristic projection, in every cell that their discontinuity indicator
judges smooth (see [WENO](/methods/weno-scheme.md) and
[shock sensors](/definitions/shock-sensor.md)). On the inviscid
Taylor–Green vortex at $64^3$ TENO-S keeps the total kinetic energy to
$t=100$ while WENO-CU6 and TENO schemes dissipate it (§4.10, Fig. 17).

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

**Kinetic-energy preservation for RANS with the Spalart–Allmaras model.**
[Lodares et al. (2022)](/sources/lodares-2022.md) extend the same framework
to the compressible RANS equations with the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) model on the LGL
DGSEM. They add to the Navier–Stokes entropy (kinetic energy or
thermodynamic entropy) the energy $\tfrac12\rho\tilde\nu^2$ of the SA
variable, whose entropy variables $(-\tilde\nu^2/2,0,0,0,0,\tilde\nu)$ are
zero where the Navier–Stokes ones are not, so that the analysis splits
into the known Navier–Stokes part and an independent SA part (§3.2,
Eqs. 38–43). Any two-point flux of the general form whose momentum
component is $\widehat{\rho U}\{\!\{u\}\!\}$ extends to the SA equation by
the component $\widehat{\rho U}\{\!\{\tilde\nu\}\!\}$, which satisfies
Tadmor's jump condition for the SA energy for **any** momentum average
$\widehat{\rho U}$, by $2[\![\tilde\nu]\!]\{\!\{\tilde\nu\}\!\}=[\![\tilde\nu^2]\!]$
(Eqs. 68, 87–89; page-local $\widehat{\rho U}$ the two-point mass flux,
$\{\!\{\rho\}\!\}\{\!\{u\}\!\}$ for Pirozzoli's flux and
$\rho^{\ln}\{\!\{u\}\!\}$ for Chandrashekar's, $[\![\cdot]\!]$ the jump).
Their **kinetic-energy-preserving configuration** pairs the Pirozzoli split
form with Lax–Friedrichs interface dissipation and, with an upwinded SA
interface flux, gives a semi-discrete kinetic-energy law equal to the
continuous one up to the pressure work, with SA-energy growth only where
SA production exceeds destruction (§4.6, §5.3, Eq. 116). They repeat that
kinetic energy is not a strict mathematical entropy (pressure work, zero
fifth entropy variable, so it cannot bound $\rho e$) but call
kinetic-energy-preserving schemes robust and cheaper for subsonic flow,
thermodynamic-entropy schemes preferable for supersonic flow (§3.1). In a random-initial-condition test at
$\mu=10^{-8}$ ($10^3$ elements, $N=10$, central fluxes) the standard DG
diverges while the Pirozzoli form keeps a zero kinetic-energy remainder,
and they run all their RANS validation (flat plate, NACA 0012) with the
Pirozzoli form (§7.2–7.4, Figs. 5–6). The entropy-conserving configuration
is on [entropy conservation](/properties/entropy-conservation.md), the
discretization on the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page.

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
for non-linear stability, with an L2Roe interface flux, and
[Kurz et al. (2023)](/sources/kurz-2023.md), §3.5, use the same KEP split
form on LGL nodes ($N=5$ and 7) as the implicitly filtered baseline on which a
[reinforcement-learning closure](/methods/reinforcement-learning-closure.md)
learns the Smagorinsky coefficient; without a model that baseline "exhibits
a buildup of energy in the upper wavenumbers due to lacking dissipation" in
forced isotropic turbulence (§4.2).

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

**Aliasing that an eddy viscosity does not remove.** Volpiani (2024, §5,
Figs. 11–18) runs the viscous compressible Taylor–Green vortex at
$Re=1600$ on $64^3$ to $512^3$. Split-form LES without a subgrid model
are noisy on the coarse grids: for every split form, aliased energy builds
up at high wavenumbers, consistent with the onset of aliasing at two
thirds of the largest wavenumber that Volpiani cites from Johnsen et al., and the
error contaminates the low wavenumbers too; the vorticity fields on $64^3$
and $128^3$ are "extremely noisy", and a Laplacian form of the viscous
terms (Sandham et al.) improves robustness without curing it. Adding a
[Smagorinsky](/methods/smagorinsky-model.md), multi-scale Smagorinsky or
[dynamic Smagorinsky](/methods/dynamic-procedure.md) model to the split
forms helps (the Smagorinsky result does not depend on the split form)
but stays noisy; adding the relaxation filter to the split form with the
model improves the results, from which the author concludes that aliasing
errors, if not removed, affect the solution even with an eddy-viscosity
model (Figs. 15–17). The split form does help the filter: with SF1 the
filter strength can drop from 0.1 to 0.01, a value with which the
divergence form is unstable, and the $64^3$ spectrum then follows the
reference without pile-up (Fig. 18). The author's verdict is that the
minimally dissipative split forms are "unsuited to perform implicit
large-eddy simulations" on coarse grids (Abstract, §6); see
[implicit LES](/definitions/implicit-les.md).

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
[wall-modelled LES](/methods/wall-modelled-les.md) of aircraft; the same
charLES scheme, "kinetic-energy-conserving" and approximately entropy
preserving in the inviscid limit, carries the machine-learning wall model of
[Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md), §3.1. The
opposite case is a scheme that is not dissipation free:
[Saini et al. (2023)](/sources/saini-2023.md), §2.1, needed a 60%–40% blend
of second-order central and upwind convection for stability in their
second-order finite-volume combustor LES, and measured that numerical
dissipation supplies 80–90% of the non-viscous dissipation of those runs
in the turbulent subdomains, the explicit WALE model the rest (§5.2; see
[numerical dissipation](/properties/numerical-dissipation.md)).

**Reversibility, and the cost of second order.** Wang et al. (2024, §3.1,
Fig. 2) run the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
on $30^3$ cells to $t=20L/V_0$, reverse the velocity and run to
$t=40L/V_0$: KGP2 keeps the kinetic energy constant and returns to the
initial vorticity field, "verifying that the KGP2 scheme has the property
of non-dissipative energy conservation", while a sixth-order optimized
upwind scheme (OPT6), fifth-order WENO and third-order MUSCL lose energy
monotonically and do not recover the initial state. Exact conservation is
not accuracy, however: by an approximate dispersion-relation analysis KGP2
needs 14 points per wavelength for dispersion against 4 for OPT6 (§2.5,
Table 1), and in WALE LES of channel flow at $Re_\tau=180$ and of the
[periodic hill](/benchmarks/periodic-hill.md) OPT6 predicts the budget of
the turbulent kinetic energy better, especially on coarse grids, so the
authors recommend high-order upwind schemes for budget analysis (§3.2–3.3,
§5). The comparison sets a second-order KEP scheme against a sixth-order
upwind one; no high-order KEP scheme is tested (§2.3–2.4). See
[low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md).

**Without discrete kinetic-energy conservation.**
[Caban et al. (2026)](/sources/caban-2026.md), §3.2.2, run the incompressible
Taylor–Green vortex in a half-staggered compact-difference code that has no
discrete kinetic-energy-conserving formulation; aliasing is controlled by
the filtering that the interpolation between staggered nodes induces, or by
an explicit filter, and with error-free (Fourier) interpolation and no
filter the kinetic energy can grow. On $64^3$ such runs are unstable without
a model (at $t\approx3.5$) and with Smagorinsky or Vreman models at
$\Delta=2h$ (§5.3.1, Fig. 18; see [implicit LES](/definitions/implicit-les.md)).
The authors restrict their interpolation-related conclusions to staggered
and half-staggered algorithms: "collocated grids with discrete
kinetic-energy-conserving schemes" lack this dissipation (§6).

**Stable but inaccurate without a model.**
[Kim et al. (2024)](/sources/kim-2024.md), §2.1, run DNS and LES of the
flow over a circular cylinder at $Re_D=3900$ with second-order central
differences on a staggered mesh, a scheme that "conserves kinetic energy
as well as continuity and momentum, and does not exhibit numerical
dissipation"; they state that LES without a subgrid model can then be
stable but inaccurate, and unstable on very coarse grids. On their coarser untrained
grid the no-model LES gives a recirculation length $0.74D$ against
$1.56D$ in the DNS (Table 3), and on the two coarsest grids the LES with no
model, the dynamic Smagorinsky model or their neural-network model diverge,
the network model running only when its stress is clipped to zero wherever
it backscatters (App. C). Near the front of the cylinder the central scheme
produces spurious oscillations, removed by QUICK upwinding for $x/D<-0.25$
(§4.2.1). See
[neural-network SGS models](/methods/neural-network-sgs-model.md).

**An energy-conserving coarse operator as the stability guarantee of a
learned closure.** [van Gastelen et al. (2024)](/sources/vangastelen-2024.md),
§2.2, Eqs. (8)–(14), discretize Burgers' equation with a skew-symmetric
convection operator $\boldsymbol C(\boldsymbol u)$ satisfying
$\boldsymbol u^{\mathsf T}\boldsymbol C(\boldsymbol u)\boldsymbol u=0$, and
the Korteweg–de Vries equation with skew-symmetric stencils for both the
nonlinear and the third-derivative terms, so that the discrete energy
decays only by viscosity (Burgers) or is conserved (KdV). Their neural
closure adds to the coarse operator a skew-symmetric term, which exchanges
energy between the resolved field and auxiliary subgrid variables, and a
negative semi-definite dissipative term; the total model energy then
obeys a balance in which the closure can only dissipate, so stability holds
for any network weights "provided that" the coarse discretization is
structure preserving (§3.1, Eq. 37). Without a closure, the coarse KdV
discretization conserves the resolved energy exactly (§4.8). The
construction is described on
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)
and [neural-network SGS models](/methods/neural-network-sgs-model.md). The
authors' §4.5 reports energy conserved "up to machine precision", their
conclusion "up to a time discretization error" (§6), with explicit
Runge–Kutta time stepping; see the Qualifications below on KEP as a
semi-discrete property.

**What KEP does not control.** Kinetic-energy preservation constrains momentum,
not density and pressure. Flad & Gassner (2017, §5.1, Fig. 10) find that
neither the KEP split form nor the Smagorinsky model damps pressure and density
fluctuations, so the pressure–dilatation work oscillates strongly; only an
interface flux whose dissipation acts on density and pressure (the low-Mach
L2Roe solver, which scales the velocity jump by the local Mach number) removes
the oscillations, and the authors rank "split form + L2Roe + Smagorinsky" best
overall (§5.1, §6.1). Brillon & Nadarajah (2026) confirm the effect of
upwinding in split-form flux reconstruction: Roe, low-dissipation Roe and
Lax–Friedrichs face dissipation "almost completely" attenuate the
pressure-dilatation oscillations (§3.1.7, Fig. 17), but they add that the
collocated scheme (flux nodes equal to the Gauss–Lobatto solution nodes)
has much smaller oscillations than the uncollocated one even without
dissipation, which suggests to them that the oscillations come from
interpolating the flux to the face nodes (§3.1.4, Fig. 13c), and that
collocated plus upwind is best (§3.1.7, Fig. 18); no value of the
correction parameter and no eddy-viscosity model removes them (§3.1.5,
§3.1.8). Bernades et al. (2023, §4.2) reach a related conclusion
for real-gas (transcritical) flow: with a Peng–Robinson equation of state the
KGP scheme with total energy (KGP-Et) is not pressure-equilibrium
preserving, produces noisy pressure that contaminates the velocity and
diverges in an inviscid mixing layer on $64\times32$ points, so "the KEP
property alone is not sufficient to tackle transcritical flows"; adding
[pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
(their KGP-Pt) keeps the run smooth and stable. In a transcritical channel
DNS at $Re_\tau=100$ the two schemes agree, physical viscosity mitigating the
oscillations (§4.3). Vicente Cruz & Lamballais (2023, footnote 6) note that
their immersed-boundary treatment is not kinetic-energy conserving.
For a thermally perfect gas, Aiello et al. (2026, §4) find KEP without
entropy conservation insufficient at high Mach number: in DNS of
compressible channel flow at bulk Mach 3 to 5 the KEP-only KEEP scheme
overpredicts the thermodynamic fluctuations, its fluctuations drift after a
long stationary period, and its streamwise Reynolds stress differs by
10.98% (max-norm relative difference) from the entropy-conserving EC-TP
scheme at Mach 5 (Table 3); the
authors write that KEEP, "although reliable in calorically perfect
simulations, develops significant stability issues under thermally perfect
conditions" (§5; see
[entropy conservation](/properties/entropy-conservation.md)).

**A continuous energy bound is not a discrete property.**
[Llorente (2024)](/sources/llorente-2024.md), Theorem 1 (pp. 8–9), proves for
the Reynolds-averaged equations of a volume-penalized
[immersed boundary](/methods/immersed-boundary-method.md) that the $L^2$
norm of the mean velocity at a time $T$ is bounded by that of the body
velocity provided the total viscosity $\nu+\nu_t$ stays non-negative. It is
an energy estimate of the continuous system, conditional on exact
penalization inside the body, and says nothing about the kinetic-energy
behaviour of a discretization.

## Cost

Krais et al. (2021, §7.1) report 1.35 µs per degree of freedom, stage and core
for the split-form airfoil run, larger than in their scaling tests "mostly
because of the extra work of the split-form volume integral". Flad & Gassner
(2017, §6.1) state that split forms cost at least three times less than
polynomial de-aliasing in their in-house code, without timings.
Brillon & Nadarajah (2026, §3.1.3, Fig. 12) time one Runge–Kutta step on
$4^3$ elements for $N=1$ to 12: strong-form DG with over-integration costs
about twice the CPU time of the split-form flux reconstruction for
$N\in[5,12]$, and without over-integration the strong form is unstable on
the under-resolved Taylor–Green vortex (§3.1.3, Fig. 11).

## Qualifications

- KEP is a property of the semi-discrete spatial operator; time integration
  breaks it at the order of the scheme (Vicente Cruz & Lamballais 2023, §6.2;
  van Gastelen et al. 2024, §6).
- **Dissipation as an asset or a defect.** Flad & Gassner (2017), Goc et
  al. (2021) and Carlsson et al. (2023) treat a dissipation-free convective
  operator as the baseline to which only model dissipation should be
  added; Wang et al. (2024) prefer a dissipative sixth-order upwind scheme
  to a second-order KEP scheme for turbulent kinetic energy budgets. Wang
  et al. vary order and dissipation together (second-order central against
  sixth-order upwind, §2.3–2.5) on channel and periodic-hill LES, while
  Carlsson et al. vary the added dissipation of one central scheme; no
  source compares the two at fixed order on the same flow, so the entry is
  recorded as a qualification.
- **Explicit models on a split-form baseline.** Flad & Gassner (2017) find
  a Smagorinsky model on the dissipation-free split-form DGSEM better than
  DG implicit LES at $48^3$; Volpiani (2024) finds Smagorinsky,
  multi-scale and dynamic models on split-form central finite differences
  noisy on the Taylor–Green vortex at $64^3$ and $128^3$, and filter-based
  implicit LES best. The discretizations differ (DG with Riemann interface
  fluxes against eleven-point central differences with no dissipation at
  all), as do the flows (decaying isotropic turbulence against the
  Taylor–Green vortex), so the two findings are recorded side by side, not
  as a contradiction.
- **Naming of the split forms.** Volpiani (2024, Eq. 15) and Liang & Fu
  (2024, Eq. 22) call $\tfrac12(C^D+C^\phi)$ the Feiereisen form; in the
  family recalled by Bernades et al. (2023) that combination is
  $a_{\mathrm K}=1$, the "C" form, while $a_{\mathrm K}=0$,
  $\tfrac12(C^u+C^\rho)$, is called Feiereisen. The forms printed are
  unambiguous; only the attribution differs *(compiler check, not in the
  sources)*.
- **"Without numerical dissipation".** Liang & Fu (2024) support the
  long-time stability of TENO-S on the inviscid Taylor–Green vortex by
  kinetic-energy and enstrophy histories only; the spectra in which a
  dissipation-free scheme thermalizes (above) are not shown.
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
- [Bernades et al. (2023)](/sources/bernades-2023.md) — §3.1.1, Eqs. (9)–(11), footnote 3 (split forms, locally conservative KEP family, KGP flux); §3.1.2 (KEP depends on continuity and momentum only); §4.2–4.3 (KEP not sufficient in transcritical flow; channel DNS).
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2 (TRACE DGSEM with Kennedy–Gruber two-point volume flux, Roe, BR1 without penalty).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §3.5 (KEP split-form FLEXI baseline); §4.2 (pile-up without a model).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.1 (charLES: kinetic-energy-conserving, approximately entropy-preserving finite volumes).
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1 (central/upwind blend for stability); §5.2 (numerical share of the non-viscous dissipation).
- [Wang et al. (2024)](/sources/wang-2024.md) — §2.3, Eqs. (5)–(11) (five convective forms, KGP2); §2.5, Table 1 (dispersion and dissipation); §3.1, Fig. 2 (inviscid Taylor–Green time reversal); §3.2–3.3, §5 (TKE budgets, recommendation).
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1 (energy-conserving second-order central scheme, no-model stability); §4.2.1, Table 3 (no-model LES, QUICK near the front); App. C (divergence on the coarsest grids).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — arXiv 2301.13770v5: §2.2, Eqs. (8)–(14) (skew-symmetric Burgers and KdV discretizations); §3.1, Eq. (37) (stability conditional on an energy-conserving coarse operator); §4.5, §4.8, §6.
- [Klose et al. (2025)](/sources/klose-2025.md) — ASME accepted manuscript: §2 (Chandrashekar entropy-conserving split form with matching Riemann solver in TRACE).
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv 2404.12703v2: §2.2, Table 1, Fig. 5 (Pirozzoli split flux in GALÆXI, cost of the two-point volume integral); App. A.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §2 (second-order KEEP central scheme for DNS and LES).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL hal-04582857v1: §III.B.b–c (KEEP-based SPADE, split forms in OpenSBLI); §IV.A, Fig. 5 (late-time pile-up of the central codes).
- [Llorente (2024)](/sources/llorente-2024.md) — author accepted manuscript: Theorem 1, Eqs. (13)–(14) (continuous energy bound of penalized URANS).
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §3.1 (induced variables); §3.2, Eq. (7) (KEP condition in flux form, independence of the energy flux and of the gas model); §4, Table 3; §5 (KEEP for a thermally perfect gas).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §2.7 (split-form NSFR); §3.1.3, Figs. 11–12 (stability and cost against over-integration); §3.1.4, Fig. 13c; §3.1.5; §3.1.6, Fig. 16 (two-point flux choice); §3.1.7, Figs. 17–18 (upwinding and pressure dilatation); §3.1.8.
- [Caban et al. (2026)](/sources/caban-2026.md) — §3.2.2 (half-staggered code without discrete kinetic-energy conservation); §5.3.1, Fig. 18; §6.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv 2512.03315v1: §II.A (split form with Chandrashekar averaging, BR1/BR2).
- [Volpiani (2024)](/sources/volpiani-2024.md) — §2.2.3, Eqs. (9)–(17) (SF1, SF2, SF3, enthalpy splitting); §4, Table 1, Figs. 4–5 (inviscid Taylor–Green vortex, energy, cost); §5, Figs. 11–18 (aliasing pile-up, SGS models, SF with relaxation filtering); §6.
- [Liang & Fu (2024)](/sources/liang-2024.md) — §2.3, Eqs. (21)–(30) (quadratic and cubic split forms, arbitrary-order skew-symmetric flux); §3.2; §4.10, Fig. 17 (inviscid Taylor–Green vortex to $t=100$).
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §3.1–3.2, Eqs. (30)–(50) (kinetic energy and SA energy as entropies); §4.3, Eq. (68); §4.6; §5.1.2, Eqs. (87)–(89); §5.3, Eq. (116); §7.2–7.4, Figs. 5–6.
- [Gao et al. (2022)](/sources/gao-2022.md) — §3.1 (split-form FLEXI with Pirozzoli flux for an implicit LES with shocks).
