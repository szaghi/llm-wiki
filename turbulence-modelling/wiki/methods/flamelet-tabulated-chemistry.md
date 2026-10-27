---
type: Method
title: "Flamelet-based tabulated chemistry"
description: "Flamelet-based tabulated chemistry stores the thermochemical state of one-dimensional flames in a table indexed by mixture fraction, progress variables and enthalpy; this page gives manifold construction and coupling by major species, extensions for curvature, ignition, wall quenching and exhaust-gas recirculation, subgrid mixture-fraction variance in supersonic LES, assessments against references, and the non-tabulated RANS eddy dissipation concept as contrast."
status: established
aliases: [eddy dissipation concept, EDC, tabulated chemistry, flamelet manifold, flamelet/progress variable, FPV, flamelet-generated manifold, FGM, QFM, quenching flamelet-generated manifold, QFM-EGR, FPV-κ, FPV-h, composition space model, ignition source-term patch, optimal estimator, premixed flamelet tabulation, subgrid mixture-fraction variance, scalar variance model]
tags: [combustion, dns, tabulated-chemistry, flame-wall-interaction, hybrid-rans-les]
timestamp: 2026-10-27T15:49:00Z
---

# Flamelet-based tabulated chemistry

**Flamelet-based tabulated chemistry** replaces the transport of tens of
species and hundreds of reactions by a look-up table: the thermochemical
state $\psi=(T,p,Y_1,\dots,Y_{n})$ (page-local; $Y_k$ the species mass
fractions) of a family of one-dimensional laminar flames is stored as a
function of a few **control variables** (a mixture fraction, one or two
progress variables, an enthalpy), and the flow solver transports only
those variables and reads density, temperature, species and the
progress-variable source term from the table. The family of flames chosen
decides which physics the table can represent: unstretched freely
propagating flames, flames with prescribed strain and curvature, or
transient flames quenching on a cold wall. In the bundle the method serves
as the chemistry of flame-resolved and DNS-like combustion simulations
([Domingo & Vervisch 2023](/sources/domingo-2023.md)) and is itself the
object of assessment against detailed-chemistry references
([Böttler et al. 2023](/sources/bottler-2023.md);
[Steinhausen et al. 2023](/sources/steinhausen-2023.md)).

Page-local notation: $\psi$ the tabulated thermochemical state; $Z$ the
Bilger mixture fraction; $Y_c$ a (non-normalized) progress variable built
from species mass fractions and $c$ its normalized form; $c_2$ a second
normalized progress variable; $h_t$ the total (sensible plus formation)
enthalpy ($h$ is the registry's element size); $\kappa_{\mathrm f}$ the
flame-front curvature and $K_{\mathrm f}$ the flame strain rate (the
registry's $\kappa$ is the von Kármán constant); $l_{\mathrm F}$ the
thermal flame thickness; $\phi_{\mathrm{eq}}$ the equivalence ratio;
$Z_v=\widetilde{Z^2}-\tilde Z^2$ the subgrid (Favre-filtered) variance of
the mixture fraction (the sources' $\widetilde{Z''^2}$), $\chi_Z$ its
scalar dissipation rate ($\chi$ is the registry's Spalart–Allmaras ratio),
$Sc_t$ the turbulent Schmidt number; $\mu_t^{\mathrm{bl}}=\bar\rho\nu_t^{\mathrm{bl}}$
the eddy viscosity of Tang et al.'s wall-distance-blended hybrid RANS/LES
(not the constrained-LES $\nu_t^{\mathrm{hyb}}$ of the registry).

## The manifold family

Böttler et al. (2023, §1) cite the flamelet/progress-variable
(FPV) approach of Pierce & Moin, which stores the state in a low-dimensional
manifold parametrized by control variables; flamelet-generated manifolds
(FGM) and flame prolongation of ILDM (FPI) are related approaches,
non-premixed manifolds are built from stretched non-premixed flamelets,
and premixed manifolds from unstretched premixed flamelets recover
moderate stretch effects. Steinhausen et al. (2023, §1) list FGM, FPI,
ILDM and REDIM as the manifold family for chemistry reduction, separate
from the turbulence–chemistry interaction closure that RANS or LES of a
reacting flow also needs.

The sources build their tables from different flame families:

| Source | Flames tabulated | Control variables |
|---|---|---|
| Domingo & Vervisch (2023, §3.1–3.2) | freely propagating premixed flamelets, GRI-3.0 mechanism | progress variable (with a presumed filtered PDF of its subgrid fluctuations in the LES zones) |
| Böttler et al. (2023), FPV-$h$ (§2, after their earlier work) | unstretched premixed flames with an enthalpy variation | $(Z,h_t,Y_c)$ |
| Böttler et al. (2023), FPV-$\kappa$ (printed FPV-$\kappa_c$; §2.1, contribution) | composition-space-model flames over $0.275\le\phi_{\mathrm{eq}}\le0.6$, $-1500\le\kappa_{\mathrm f}\le5000$ m⁻¹, at fixed strain $K_{\mathrm f}=500$ s⁻¹ | $(Z,c,c_2)$, $c_2$ from the H radical |
| Steinhausen et al. (2023), QFM (§5, after Efimov et al.) | one transient head-on quenching flame of an undiluted mixture on a 300 K wall | progress variable and enthalpy |
| Steinhausen et al. (2023), QFM-EGR (§4, contribution) | 63 transient head-on quenching flames with cold exhaust-gas dilution $0\le Y_{\mathrm{EGR}}\le0.3$, plus preheated flames 300–750 K | $(c,c_2,h_t)$, $c$ from $\mathrm{CO_2}$, $c_2$ from $\mathrm{CO}$ |
| Tang et al. (2022), FPV of Pierce & Moin (§2.2) | laminar counterflow (non-premixed) flamelets, all three branches, 9-species 19-step H$_2$–air mechanism, unity Lewis number, at 1.1 and 1.9 bar | $(\tilde Z,Z_v,\tilde c)$, presumed $\beta$-PDF in $Z$ and $\delta$-PDF in $c$ |
| [Böttler et al. (2022)](/sources/bottler-2022.md), §2.2 (the FPV-$h$ of Böttler et al. 2023) | composition-space-model solutions blending unstretched premixed flames with constant-pressure homogeneous ignition, over $0.35\le\phi_{\mathrm{eq}}\le2.0$ and fresh-gas temperatures 300–3500 K, plus exhaust-diluted flames for the low-enthalpy bound; Li et al. hydrogen mechanism, mixture-averaged diffusion | $(Z,H_{\mathrm n},c)$, $H_{\mathrm n}$ the normalized enthalpy |

## Construction

**Mixture fraction.** Böttler et al. (2023, Eqs. 1–2) map each flame to the
Bilger mixture fraction,
$$Z=\frac{\beta_{\mathrm B}-\beta_{\mathrm B,0}}{\beta_{\mathrm B,1}-\beta_{\mathrm B,0}},\qquad \beta_{\mathrm B}=\sum_{l=1}^{N_e}\gamma_l\sum_{k=1}^{N_s}\frac{a_{l,k}M_lY_k}{M_k},$$
with subscripts 1 fuel and 0 oxidizer, $\gamma_l$ the element weights of
Bilger et al., $a_{l,k}$ the number of atoms of element $l$ in species $k$,
$M_l$, $M_k$ the molecular weights (page-local symbols).

**Normalized progress variables.** Böttler et al. and Steinhausen et al. normalize a
species-based progress variable between its local bounds, then condition a
second variable on the first (Böttler et al. 2023, Eqs. 3–4; Steinhausen
et al. 2023, Eqs. 3–5):
$$c=\frac{Y_c-Y_{c,\min}}{Y_{c,\max}-Y_{c,\min}},\qquad c_2=\frac{Y_{c_2}-Y_{c_2,\min}(c)}{Y_{c_2,\max}(c)-Y_{c_2,\min}(c)},$$
the bounds of $c$ taken at fixed $Z$ in Böttler et al. and the bounds of
$c_2$ at fixed $(Z,c)$; Steinhausen et al. add a third normalization of
$h_t$ between bounds conditioned on $(c,c_2)$ and look up in the order $c$,
$c_2$, $h_t$, on a $150\times201\times101$ table. Böttler et al. use
$Y_c=Y_{\mathrm{H_2O}}-Y_{\mathrm{H_2}}-Y_{\mathrm{O_2}}$ for lean hydrogen and
$Y_{c_2}=Y_{\mathrm H}$, justified because $Y_{\mathrm H}$ increases
monotonically with curvature (Fig. 2); Steinhausen et al. use
$Y_c=Y_{\mathrm{CO_2}}$ and $Y_{c_2}=Y_{\mathrm{CO}}$ for methane–air. In
both, the second progress variable is how a physical effect outside the
one-dimensional flame family (curvature; recirculated exhaust gas) enters
the table.

**Coupling to the flow solver.** Steinhausen et al. (2023, Fig. 7)
transport the non-normalized $(Y_c,Y_{c_2},h_t)$ and normalize at look-up;
the table returns the source terms and the density. Böttler et al. (2023,
§2.1) instead transport the major species $\mathrm{H_2O}$, $\mathrm{H_2}$,
$\mathrm{O_2}$ with mixture-averaged diffusion and reconstruct the control
variables from them, which, they state, avoids further modelling
assumptions on the transport properties of composed quantities such as
mixture fraction and progress variable; this is how differential diffusion
of hydrogen enters.

The coupling is set out in [Böttler et al. (2022)](/sources/bottler-2022.md),
§2.1–2.2, Fig. 3, the earlier work that Böttler et al. (2023) cite for it.
The solver transports $Y_{\mathrm{H_2}}$, $Y_{\mathrm{O_2}}$,
$Y_{\mathrm{H_2O}}$ with mixture-averaged fluxes, whose Lewis numbers and
source terms are read from the table, and the enthalpy (Eqs. 1–3); the
gradient of the mean molecular mass and Soret diffusion are neglected.
The mixture fraction is an *approximate* Bilger mixture fraction built
from the three transported species only, defined the same way in the
table so that the coupling is consistent; the authors state that it
recovers the characteristics of the full definition with "no significant
modeling error", without showing a comparison (§2.1). Because the
enthalpy equation needs the diffusive fluxes of all species (radicals
such as H weigh little in the element balance but much in the formation
enthalpy), the contribution of the species *not* transported is
tabulated from the one-dimensional flamelets as a closure term (Eq. 9).
The table is generated by the composition space model in $Y_c$-space
(Eqs. 5–8): at low fresh-gas temperature its solution is the unstretched
premixed flame with eigenvalue $s_L$ (the laminar burning velocity), and
in the limit $g_c\to0$ of vanishing progress-variable gradient ($g_c$
page-local) all diffusive terms vanish and it becomes constant-pressure
homogeneous ignition, so one set of equations covers deflagration and
autoignition. The state is stored as $\psi(Z,H_{\mathrm n},c)$ with
$H_{\mathrm n}=(h_t-h_{t,\min})/(h_{t,\max}-h_{t,\min})$ normalized
between bounds conditioned on $(Z,Y_c)$ and $c$ normalized between bounds
conditioned on $(Z,H_{\mathrm n})$ (Eqs. 12–13). Under differential
diffusion the enthalpy bounds depend on $Y_c$ and the look-up would be
iterative; the lower bound is extrapolated to a constant minimum and the
upper bound (homogeneous-ignition solutions) is already constant, which
gives a two-step look-up. Since a mixture at $c=0$ has zero tabulated
source terms and could never ignite, the source terms of the transported
species at $c=0$ are replaced, above a critical normalized enthalpy (value
not printed), by their mean over $0\le c\le10^{-9}$ (Eq. 14, adapted from
Sun et al.). The authors state that the model cuts the cost "by an order
of magnitude" against detailed chemistry while halving the number of
transport equations, without timings (§3), and that more complex fuels
would need more transported species (§4).

**Stretch and curvature.** Laminar canonical flames are limited in the
strain and curvature they can reach; the composition space model of the
authors' group, solved in composition space with respect to $Y_c$ and
needing only strain and curvature as external parameters, removes the
limit (Böttler et al. 2023, §2.1). Their definitions are
$K_{\mathrm f}=\nabla_t\cdot\boldsymbol u_t-(\boldsymbol u\cdot\boldsymbol n_{\mathrm f})\kappa_{\mathrm f}$
and $\kappa_{\mathrm f}=-\nabla\cdot\boldsymbol n_{\mathrm f}$, $\boldsymbol n_{\mathrm f}$
the flame-normal unit vector and $\nabla_t\cdot\boldsymbol u_t$ the
flame-tangential straining (page-local). No burning solution exists below
$\kappa_{\mathrm f}=-1500$ m⁻¹ for their lean hydrogen–air flame (Fig. 1).

**Wall quenching and exhaust-gas recirculation.** For flame–wall
interaction the building blocks are transient one-dimensional head-on
quenching flames, which include the wall enthalpy loss (quenching
flamelet-generated manifold, QFM, of Efimov et al., which
Steinhausen et al. 2023, §1, §5, cite). Steinhausen et al. (2023, §4) extend it
by diluting the fresh side of a freely propagating flame with cold exhaust
gas at the inflow temperature, quenching each diluted flame on a 300 K
wall, and spanning the manifold in flamelet coordinate, time and
$Y_{\mathrm{EGR}}$ (the mass fraction of cold burnt gas mixed into the
fresh gas, page-local).

**Subgrid variance of the mixture fraction.** In LES with a presumed PDF
the table needs the subgrid variance $Z_v$ as an extra coordinate.
[Tang et al. (2022)](/sources/tang-2022.md), §2.2, Eqs.
(10)–(11), cite the flamelet/progress-variable model of Pierce & Moin, which stores
$\psi(Z,c)$ from counterflow flamelets, the progress variable selecting
among the burning, unstable and extinguished branches, and filters it as
$$\tilde\psi=\iint\psi(Z,c)\,P_\beta(Z;\tilde Z,Z_v)\,\delta(c-\tilde c)\,dZ\,dc,$$
with a $\beta$-PDF $P_\beta$ (page-local) in $Z$ and, by a fast-chemistry
assumption, a $\delta$-PDF in $c$; $\tilde Z$ and $\tilde c$ are
transported, $\tilde c$ with the tabulated source term (Eqs. 12–13). Tang
et al. compare two closures for $Z_v$ (§2.2):

- an algebraic **scale-similarity** estimate (see
  [scale-similarity models](/methods/scale-similarity-model.md)),
  $Z_v=c_{\mathrm{ss}}(\widehat{\tilde Z^2}-\hat{\tilde Z}^2)$ with a test
  filter of width $\hat\Delta=2\Delta$, evaluated by a seven-point stencil
  (Eqs. 15–16; $c_{\mathrm{ss}}$ page-local, its value not printed, the
  discrete form corresponding to $c_{\mathrm{ss}}=1$);
- a **transport equation** (Eq. 17)
$$\partial_t(\bar\rho Z_v)+\partial_j(\bar\rho\tilde u_jZ_v)=\partial_j\Big[\Big(\bar\rho D_{\mathrm m}+\frac{\mu_t^{\mathrm{bl}}}{Sc_t}\Big)\partial_jZ_v\Big]+2\frac{\mu_t^{\mathrm{bl}}}{Sc_t}\partial_j\tilde Z\,\partial_j\tilde Z-\bar\rho\chi_Z,$$
  with molecular diffusivity $D_{\mathrm m}$, production by the resolved mixture-fraction
  gradient, a modelled dissipation proportional to $\mu_t^{\mathrm{bl}}Z_v/Sc_t$
  with constant $c_q=40.0$, $Sc_t=0.5$ (printed form in Qualifications),
  and $\mu_t^{\mathrm{bl}}$ the blended eddy
  viscosity of their [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
  (Eq. 14).

The authors describe the scale-similarity estimate as having no transport
or dissipation of the variance, "no historical effects" (§3.1).

## Assessment

Böttler et al. (2023) and Steinhausen et al. (2023) both separate an **a priori** test, in which the control
variables are taken from the detailed-chemistry reference and the table's
state is compared with the reference state, from an **a posteriori** test
with the table coupled to the solver; Steinhausen et al. (2023, §5,
Fig. 7) state that the a priori test isolates the tabulation error from
the errors of the control-variable transport. The usage matches that of
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
for turbulence closures, here applied to a chemistry model.

**Curvature in a thermo-diffusively unstable hydrogen flame** (Böttler et
al. 2023). The reference is a detailed-chemistry two-dimensional
spherical expanding flame, lean hydrogen–air at $\phi_{\mathrm{eq}}=0.4$,
300 K, atmospheric pressure; the flame is laminar and intrinsically
unstable, with no turbulence.

- *A priori* (§3.1, Fig. 3): the largest deviations sit in negatively
  curved segments; FPV-$h$ errs by up to 5% in temperature and 40% in
  $Y_{\mathrm{OH}}$; FPV-$\kappa$ errs less and over a smaller area.
- *Linear stability* (§3.2, Fig. 4): both tables give a wider range of
  unstable wavelengths than detailed chemistry; FPV-$\kappa$ reproduces the
  maximum growth rate with its wavelength slightly shorter, FPV-$h$
  over-predicts the peak and shifts it further.
- *Coupled expanding flame* to a radius of about 6 cm (§3.3, Figs. 5–8):
  both tables produce smaller secondary cells, cell-size distributions
  peaking below the detailed-chemistry peak of 7–8 $l_{\mathrm F}$, faster
  linear growth of the perturbation, and flame speeds over-predicted by up
  to 15% at the largest radii; FPV-$\kappa$ gives a microstructure (mixture
  fraction, temperature, OH, $\mathrm{HO_2}$) closer to the reference. The
  authors conclude that curvature in the table improves local features,
  while global features are reproduced reasonably by both (§4). Both
  tables recover the unstretched burning velocity "very accurately" (§4, no
  number printed).

**Exhaust-gas recirculation in turbulent side-wall quenching**
(Steinhausen et al. 2023). The reference is a three-dimensional
"fully resolved simulation with detailed chemistry" of a stoichiometric
methane–air V-flame quenching on the cold wall of a turbulent channel at
bulk Reynolds number 2770 (half-width based), 24 species and 165
reactions, 200 million cells with a first wall spacing of $\Delta y^+=0.14$
(§2.1). Near-wall vortices recirculate cold burnt gas into the fresh
mixture between flame and wall (the flame–vortex interaction mechanism
proposed from experiments by Zentgraf et al., numerically verified here),
giving $\mathrm{CO}$ levels at fixed $\mathrm{CO_2}$ below the minimum of
the laminar side-wall-quenching flame; more than 80% of the lateral
locations show such an event over 5 ms (§3, Figs. 2–5). A priori, over the
reaction zone of twenty snapshots (§5, Figs. 8–9):

- the two-dimensional QFM deviates by up to 70% inside the recirculation
  region "for all species studied", so the near-wall mixture is not on the
  QFM states at all;
- QFM-EGR gives "very good agreement" with the reference fields (Fig. 8)
  and "excellent agreement" in the mean relative errors (Fig. 9);
- beyond two flame thicknesses from the wall both tables are good.

The coupled LES evaluation is left to future work (§6).

**Flame-resolved simulations with tabulated chemistry** (Domingo & Vervisch
2023). A premixed Bunsen jet at $Re=24\,000$ is computed as well-resolved
LES with a nested DNS-resolution box, premixed flamelet tabulation in both
zones (§3.1); deconvolution by one-dimensional filtered flamelets
over-estimates methane and oxygen consumption more than three-dimensional
approximate deconvolution and enhances the CO over-estimation a
posteriori, its error growing with the subgrid flame wrinkling (§3.1,
Figs. 5–6). A 1.6-billion-cell flame-resolved simulation of the
Cambridge/Sandia bluff-body burner at 100 µm, "about twice the Kolmogorov
scale", uses tabulated chemistry from freely propagating premixed
flamelets and is validated against measured velocity, temperature and CO
(§3.2). The authors suggest repeating it with detailed chemistry to test
the flamelet-manifold hypothesis itself under curvature and unsteady strain
(§3.2). See also
[direct numerical simulation](/definitions/direct-numerical-simulation.md).

**Forced ignition and propagation of laminar hydrogen flames** (Böttler
et al. 2022, §3). The table above, coupled to a second-order low-Mach
[OpenFOAM](/software/openfoam.md) solver, is compared with fully resolved
detailed chemistry (Li et al. mechanism, mixture-averaged diffusion) for
hydrogen–air at 300 K and 1 atm, $\phi_{\mathrm{eq}}=0.7$, 1.0, 1.4
(effective Lewis numbers about 0.5, 0.95, 1.4); every case is laminar.

- *Planar flame* ($\phi_{\mathrm{eq}}=0.7$, Fig. 5): "very good agreement"
  for all quantities, including the variation of $Z$ and enthalpy across
  the flame that differential diffusion produces, with minor deviations in
  $Y_{\mathrm{OH}}$ on the burned side.
- *Cylindrical and spherical expanding flames* ignited by a Gaussian hot
  spot (radius 0.2 mm, duration 0.2 ms; cells of 11 µm; Figs. 6–8): with
  the propagation speed split as $dR_f/dt=u_g+s_d$ (flame radius $R_f$,
  unburned-gas velocity $u_g$, displacement speed $s_d$, page-local), the
  offset comes from an under-predicted $u_g$ while $s_d$ agrees "very
  well"; the authors trace it to a small shift of $Z$ toward leaner
  mixture, which changes the density. The largest deviations are in the
  lean case: about 7% in $u_g$ for the cylindrical flame and about 8% in
  propagation speed for the spherical one, against less than 1% (rich
  cylindrical) and less than 2% otherwise.
- *Igniting counterflow* (global strain 1000 s⁻¹, Figs. 9–10): slightly
  slower radial propagation and an axial position slightly closer to the
  centre, slightly higher $Z$ on the burned side and over-predicted
  $Y_{\mathrm{OH}}$ near the stagnation plane, temperature insensitive.
- *Minimum ignition energy* by bisection (Fig. 11): the trend with
  $\phi_{\mathrm{eq}}$ is reproduced with slightly over-estimated values,
  well at $\phi_{\mathrm{eq}}=1.0$ and 1.4 and worse toward the lean case.

Extension to LES with a turbulence–chemistry closure is left to future
work (§4).

**What a manifold for unstable lean hydrogen flames must contain**
([Berger et al. (2022)](/sources/berger-2022.md)). Three-dimensional
detailed-chemistry [DNS](/definitions/direct-numerical-simulation.md) of a
turbulent premixed slot jet, hydrogen–air at $\phi_{\mathrm{eq}}=0.4$,
$Re=11\,000$ on the slot width and Karlovitz number about 15, are run with
realistic Lewis numbers and Soret diffusion (thermodiffusively unstable)
and with unit Lewis numbers (stable); the second follows the unstretched
premixed flamelet closely in the progress-variable source term, the first
scatters strongly through local equivalence-ratio variations (§3.4.1,
Fig. 15). An optimal-estimator analysis, the irreducible error
$\langle(\dot\omega_c-\langle\dot\omega_c|\boldsymbol\psi\rangle)^2\,|\,c_{\mathrm{H_2}}\rangle$
of the source term $\dot\omega_c$ of the progress variable
$c_{\mathrm{H_2}}=1-Y_{\mathrm{H_2}}/Y_{\mathrm{H_2},u}$ for a set of
parameters $\boldsymbol\psi$ (page-local; Eqs. 22–23), finds large errors
with $c_{\mathrm{H_2}}$ alone, a strong reduction when the Bilger mixture
fraction is added, about the same with temperature instead, and much less
gain from adding stretch, tangential strain or curvature, singly or
together (Fig. 16). The authors read this as the source term depending
not on the instantaneous stretch but possibly on its history, while $Z$
records the result of differential diffusion; the mixture-fraction
fluctuations themselves are set by curvature, not strain (Figs. 21–22).
Because an irreducible error measures only correlated fluctuations and is
blind to a shift of the mean (§3.4.3), they compare the conditional mean
$\langle Z|c_{\mathrm{H_2}}\rangle$ with laminar premixed counterflow
flamelets at the turbulent flame's mean tangential strain, which
reproduce its shift to richer mixture (counterflow consumption speed 0.49
m/s against 0.17 m/s unstretched with the unstable diffusivity model; 0.32
against 0.34 m/s with unit Lewis numbers; §3.4.4, Figs. 27–29). They
conclude that turbulent combustion models must account for the
thermodiffusive instability (§4); the paper builds no table.

**Mixture-fraction space and the diffusion-flame structure.**
[Cuenot et al. (2022)](/sources/cuenot-2022.md), §1–2, cite the
pre-tabulated flamelet approach of Peters and state that it loses the direct interaction of
the local flame structure with the flow, and the
[thickened flame model](/methods/thickened-flame-model.md) can be combined
with tabulated flamelets instead of replacing them. Their analysis of the
steady strained counterflow diffusion flame writes it in mixture-fraction
space as $-\chi_Z\,\partial^2\phi_k/\partial Z^2=\dot\omega_{\phi_k}$ for any
species or temperature $\phi_k$ (Eq. 4, $\chi_Z=2D_{\mathrm m}(\partial_xZ)^2$ the scalar
dissipation rate of the one-dimensional flame, page-local; $D_{\mathrm m}$ the molecular diffusivity), whose solution for a
steady strained flame is insensitive to the diffusion coefficients; in
physical space the consumption speed then scales as $\sqrt{a_{\mathrm{cf}}D_{\mathrm m}}$ with the
strain rate $a_{\mathrm{cf}}$ (detail on the thickened-flame page).
[Agostinelli et al. (2021)](/sources/agostinelli-2021.md), §2, use
analytically reduced chemistry with a dynamically thickened flame rather
than a table in their LES of a swirl combustor.

**Supersonic hydrogen combustion in hybrid RANS/LES** (Tang et al.
2022). The solver blends the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md)
in a wall layer of 10–20% of the boundary-layer thickness with a
one-equation subgrid-energy LES model elsewhere, prescribed by wall
distance (§2.1), with fifth-order [WENO](/methods/weno-scheme.md) inviscid
fluxes. Two experiments are computed:

- *DLR strut-injection scramjet* (Mach 2 air, sonic parallel H$_2$
  injection; §3.1, Figs. 5–7). The scale-similarity variance peaks near
  0.01 but is mostly below 0.001, concentrated where mixture-fraction
  gradients are large; the transport-equation variance is mostly below
  0.002 and more widely spread. The scale-similarity run releases more
  heat near the injector ($x=80$–90 mm), shortens the flame lift-off and
  moves the flame core upstream; the transport-equation run agrees better
  with the measured temperature at $x=125$ mm and is more consistent in
  velocity.
- *NUDT cavity combustor* (Mach 2.52, transverse sonic H$_2$ injection
  30 mm upstream of the cavity, equivalence ratio 0.28; §3.2,
  Figs. 12–16). The scale-similarity variance is higher across almost the
  whole jet wake, which the authors attribute to the confined, high-gradient
  fuel of transverse injection; combustion is over-intensified and the
  thermal disturbance propagates upstream through the subsonic boundary
  layer, separating it ahead of the cavity. Both closures give acceptable
  lower-wall pressures, the transport equation relatively better.

In both cases the variance from the two closures differs by "almost [an]
order of magnitude" at some mixture fractions (§4), and higher variance gives
"a bit higher heat release" in the table (§3.1, not shown). A Takeno flame
index $\nabla Y_{\mathrm{H_2}}\cdot\nabla Y_{\mathrm{O_2}}/(\lvert\nabla Y_{\mathrm{H_2}}\rvert\lvert\nabla Y_{\mathrm{O_2}}\rvert)$
(Eq. 18), positive in premixed and negative in diffusion burning, shows
diffusion combustion over almost the whole reacting zone in both combustors,
which the authors take as support for a non-premixed flamelet model there
(Figs. 8, 15). They recommend the transport equation when computing
resources allow (§4). The evidence is visual comparison of contours,
scatter plots and profiles; no error norm is given.

## Contrast: the eddy dissipation concept in RANS

Not every turbulence–chemistry closure tabulates. In the **eddy
dissipation concept** (EDC) of Magnussen, as restated by
[Mardani & Nazari (2022)](/sources/mardani-2022.md), §2, reactions take
place only in "fine structures" whose size and residence time follow from
an energy-cascade model, and each fine structure is integrated as an
isobaric batch (plug-flow) reactor with a detailed mechanism (here DRM-22,
24 species and 104 reactions) from the current cell state: the chemistry is
computed on the fly, not read from a flamelet table. The authors run it in
two-dimensional axisymmetric RANS with the standard
[$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) (production constant
raised from 1.4 to 1.6 for the round jet) for MILD (moderate or intense
low-oxygen dilution) combustion in jet-in-hot-coflow burners, a regime in
which, they state, the default constants are inadequate; their literature
review lists flamelet-generated manifolds and flamelet models as the
tabulated alternatives for MILD flames (§1).

Page-local symbols: $\gamma_{\mathrm{fs}}$ the fine-structure length
fraction (the source's $\gamma$; not the ratio of specific heats),
$\tau_{\mathrm{fs}}$ its residence time, $C_{\mathrm{vf}}$ and $C_{\tau}$
their constants (the source's $C_\gamma$, $C_\tau$), $C_{D1}$, $C_{D2}$
the cascade constants (names as in the model), $Re_T=k^2/(\nu\varepsilon)$
the turbulence Reynolds number, $Da$ the Damköhler number of the
Kolmogorov time to a chemical time, $S_L$, $S_T$ the laminar and
turbulent flame speeds, $\chi_{\mathrm{fs}}$ the reacting fraction of the
fine structure, $Y_k^*$ the fine-structure mass fractions.

**The cascade and the defaults** (§2, Eqs. 1–17). Matching the cascade
eddy viscosity to the $k$-$\varepsilon$ one gives $\tfrac23C_{D1}=C_\mu=0.09$,
$C_{D1}=0.135$; Magnussen's experimental value is $C_{D2}=0.5$. With a
frequency doubling between cascade steps, three quarters of the
dissipation occurs in the fine structures. Then

$$\gamma_{\mathrm{fs}}=C_{\mathrm{vf}}Re_T^{-1/4},\qquad \tau_{\mathrm{fs}}=C_\tau\Big(\frac{\nu}{\varepsilon}\Big)^{1/2},\qquad \bar R_k=\frac{\rho\,\gamma_{\mathrm{fs}}^2\chi_{\mathrm{fs}}}{\tau_{\mathrm{fs}}(1-\gamma_{\mathrm{fs}}^3\chi_{\mathrm{fs}})}\big(Y_k^*-\langle Y_k\rangle\big),$$

with defaults $C_{\mathrm{vf}}=2.1377$, $C_\tau=(C_{D2}/3)^{1/2}$ and
$\chi_{\mathrm{fs}}=1$ ($\bar R_k$ the mean reaction rate of species $k$,
page-local; Eqs. 11, 14, 17).

**Validity limits** (§4, Eqs. 18–20, Fig. 2). The fine structure must be
smaller than the cell, $\gamma_{\mathrm{fs}}<1$, i.e. $Re_T>20.8$; the
time-scale fraction $\gamma_{\mathrm{fs}}^2/(1-\gamma_{\mathrm{fs}}^3)$ of
De et al. must stay below one, which the authors print as
$\gamma_{\mathrm{fs}}<0.7568$, $Re_T>64.31$. A 10% decrease or increase of
$C_{\mathrm{vf}}$ moves the second limit to $Re_T>42$ or $Re_T>95$, so
tuning the constants changes where the model is valid.

**Cascade frequency ratio** (§4.1, §6.1–6.2, Eqs. 21–25, Table 3, Figs.
4–5). With a general ratio $\alpha_{\mathrm c}$ (page-local; default 2)
between the frequencies of successive cascade steps, the total-to-fine-structure
dissipation ratio becomes $1/(1-\alpha_{\mathrm c}^{-2})$. On the Adelaide
burner (case HM1) a larger $\alpha_{\mathrm c}$ lowers the error 30 and
60 mm downstream of the jet exit, where $Da$ is low, and a smaller one at
120 mm, where entrainment of wind-tunnel air ends the MILD regime; the
fine-structure to Kolmogorov scale ratios behave alike: "finding an optimum
α for all regions seems to be impossible".

**A localized EDC** (§4.2, Eqs. 26–35; contribution). Following Parente
et al., the fine-structure velocity is identified with the turbulent flame
speed, $S_T\approx S_L\sqrt{Re_T+1}$, which gives
$C_{D2}\approx3/[4(Re_T+1)Da^2]$ and, cell by cell,

$$C_\tau=\frac{C_{D3}}{2Da\sqrt{Re_T+1}},\qquad C_{\mathrm{vf}}=C_{D4}\Big(\frac{9}{16C_{D1}^2(Re_T+1)Da^2}\Big)^{1/4},\qquad C_{D3}=1.0,\ C_{D4}=0.65,$$

with $C_{D1}$ kept at 0.135 and $C_{D4}$ chosen from tests between 0.2 and
1.0 against measurements. $Da$ uses the Arrhenius rate of one reaction
(OH + H$_2$ ⇌ H$_2$O + H) or the fastest of the 104, and the constants are
updated every iteration, without the precomputation with a global
mechanism that Parente et al.'s variant needs. The authors note that
their $C_{\mathrm{vf}}$ decreases with $Da$ and $Re_T$, the opposite of
the correlations of Parente et al. and of Romero-Anton et al. that they
cite.

**Results** (§6.3, Figs. 6–12). On HM1 the local constants span
$C_{\mathrm{vf}}$ 0.6–3.5 and $C_\tau$ 0.2–3, with $Da<8.5$ and
$\gamma_{\mathrm{fs}}<0.75$, inside the validity limits. Against the
standard EDC the maxima of temperature, OH and CO$_2$ improve by more than
15% at 120 mm for HM1 and more than 12% for HM3, with comparable accuracy
upstream; the accuracy on HM1 is near that of Parente et al.'s local
approach, and the Delft burner's temperatures improve at 90–150 mm. The
two definitions of $Da$ give similar results at "relatively the same" cost
per iteration for the single-reaction one (no timings). Results for the
Sandia flame D and the Sydney bluff-body burner are only in supplementary
material, which is not in the file read.

## Qualifications

- **Printed forms in Mardani & Nazari (2022)** *(compiler checks, not in
  the sources, from the paper's own definitions)*. The root of
  $\gamma_{\mathrm{fs}}^2=1-\gamma_{\mathrm{fs}}^3$ is 0.7549, which with
  $C_{\mathrm{vf}}=2.1377$ gives the printed $Re_T>64.31$ and matches the
  clipping value 0.7548 printed for their code (§6.3); the printed 0.7568
  gives $Re_T>63.66$. The default $C_{\mathrm{vf}}=2.1377=(3C_{D2}/4C_{D1}^2)^{1/4}$
  implies $C_{D1}=0.134$, not the stated 0.135, and the $C_{\mathrm{vf}}$
  column of Table 3 follows the exponent $\tfrac14$ with $C_{D1}=0.134$, not
  the $\tfrac12$ printed in Eq. (25); the Table 3 entry $C_\tau=0.6369$ at
  $\alpha_{\mathrm c}=1.2$ is 0.6396 by Eq. (24), all other rows agreeing.
  §4 calls the default "$C_{D1}=2.137$", the value of $C_{\mathrm{vf}}$.
  $Re_T$ is defined as $k^2/(\nu\varepsilon)$ (Eqs. 11, 18, 34) and, before
  Eq. (27), as $\nu_t/\nu$, which differ by the factor $C_\mu$; the
  derivation of the local constants uses the second, their evaluation the
  first. The improvement is quoted as more than 10% (abstract), 13%
  (conclusions) and 12–15% (§6.3) for different subsets.
- **Printed forms in Tang et al. (2022).** The variance dissipation is
  printed as $\bar\rho\chi_Z=\frac{\mu_t^{\mathrm{bl}}}{Sc_t}\frac{c_q}{\Delta^{1/3}}\bar\rho Z_v$
  (Eq. 17), with units kg$^2$ m$^{-13/3}$ s$^{-1}$ against the kg m$^{-3}$
  s$^{-1}$ of the other terms; the paper prints no other form *(compiler check, not in the sources)*. Eqs. (12)–(13) add the
  turbulent flux $(\mu_t^{\mathrm{bl}}/Pr_t)\nabla\tilde Z$ inside the
  divergence with the sign opposite to the molecular flux
  $-\bar\rho D_{\mathrm m}\nabla\tilde Z$, which as printed is anti-diffusive, and use
  $Pr_t$ for a scalar where Eq. (17) uses $Sc_t$ *(compiler check, not in
  the sources)*. The constant $c_{\mathrm{ss}}$ of Eq. (15) is not given.
- **Scope of Tang et al.'s recommendation.** It rests on two configurations
  compared visually with experiment (§3, §4); both variance closures run in
  the same hybrid RANS/LES solver with the same numerics (§2.1).
- **Agreement on the failure mode.** Böttler et al. (2023) and Steinhausen
  et al. (2023) both find that a table built from flames without the
  relevant physics (unstretched flames; undiluted quenching flames) fails
  locally where that physics is strong (negative curvature; exhaust-gas
  recirculation near the wall), and that adding a second progress variable
  conditioned on the first removes most of the local error a priori. Their
  configurations, fuels and references differ, and neither shows a
  turbulent a posteriori test of its new table.
- **Domain of the claims.** Steinhausen et al. state that the
  flame–vortex mechanism is "not restricted to the equivalence ratio or
  even fuel" (§3) from one stoichiometric methane simulation and
  qualitative agreement with dimethyl-ether experiments. Böttler et al.'s
  configuration is laminar; it bears on turbulence modelling only through
  the tabulation method and the a priori/a posteriori protocol.
- **Flame thickness.** Böttler et al. ($l_f$) and Steinhausen et al.
  ($\delta_L$) both define the thermal thickness
  $l_{\mathrm F}=(T_b-T_u)/\max|\mathrm dT/\mathrm dx|$ (Böttler §3.2;
  Steinhausen §2.1, printed with $\delta$ in the gradient).
- **Printed formula.** Steinhausen et al.'s mean relative error (Eq. 7)
  divides a ratio of sums by the number of samples $N$; the ratio of sums
  is already independent of the sample count, so as printed the error
  scales with $1/N$ *(compiler check, not in the sources)*.
- The versions read are arXiv preprints (Böttler et al. 2301.06780v1;
  Steinhausen et al. 2212.03762v1) and the HAL author manuscript of Domingo
  & Vervisch.
- **Böttler et al. (2022)** compare with detailed chemistry only in
  laminar flames. Their Conclusions state agreement in "ignition delay
  times" and minimum-ignition-energy deviations "below 3 %" (§4), but the
  body reports no ignition delay times and gives no number for the
  minimum ignition energy, whose evidence is Fig. 11 alone. Eq. (9)
  prints the closure over the species $k\notin\{\mathrm{H_2},\mathrm{O_2},\mathrm{H_2O}\}$;
  text extraction of the PDF renders it as $\in$. They neglect Soret
  diffusion after Liang et al. while citing Grcar et al. for its growing
  importance in very lean hydrogen flames; their leanest case is
  $\phi_{\mathrm{eq}}=0.7$.
- **Berger et al. (2022)** print the Karlovitz number $(l_{\mathrm F}/\eta)^2$
  as 20 and 16 for the unstable and stable flames (Table 1), while the
  $l_{\mathrm F}$ and $\eta$ of the same table give about 15.7 and 17.3
  *(compiler check, not in the sources)*. In §3.5 "TurbStable" is printed twice where the argument is
  about the unstable flame, and $I_0$ is said to appear in Eq. (7) where it
  appears in Eq. (9). Claims on halving the lateral laminar domain and on a
  half-resolution run rest on supplementary material not in the file read.

# Citations

- [Böttler et al. (2022)](/sources/bottler-2022.md) — §1; §2.1–2.2, Eqs. (1)–(14), Figs. 2–3 (coupling by major species, approximate Bilger mixture fraction, enthalpy closure, composition-space manifold with homogeneous ignition, normalization, ignition patch); §3.1–3.5, Figs. 5–11 (laminar planar, expanding and counterflow flames, minimum ignition energy); §4.
- [Berger et al. (2022)](/sources/berger-2022.md) — §2.1–2.2, Table 1; §3.4.1, Eqs. (21)–(23), Figs. 15–16 (flamelet comparison, optimal estimator); §3.4.2, Figs. 21–22; §3.4.3–3.4.4, Figs. 23–29 (strained counterflow flamelets); §3.5.
- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §1 (pre-tabulated flamelets; thickened flame with tabulated chemistry); §2, Eqs. (2)–(4) (counterflow diffusion flame in mixture-fraction space).
- [Agostinelli et al. (2021)](/sources/agostinelli-2021.md) — §2 (analytically reduced chemistry with a thickened flame instead of tabulation).
- [Böttler et al. (2023)](/sources/bottler-2023.md) — arXiv 2301.06780v1: §1 (FPV family); §2–2.1, Eqs. (1)–(4), Figs. 1–2 (FPV-$h$, FPV-$\kappa$, composition space model, coupling by major species); §3.1, Fig. 3 (a priori); §3.2, Fig. 4 (linear stability); §3.3, Figs. 5–8 (expanding flame); §4.
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — arXiv 2212.03762v1: §1 (manifold family, QFM); §2.1, Table 1 (reacting channel); §3, Eqs. (1)–(2), Figs. 2–5 (flame–vortex interaction); §4, Eqs. (3)–(5), Fig. 6 (QFM-EGR); §5, Eqs. (6)–(9), Figs. 7–9 (a priori assessment); §6.
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1, Eq. (14) (hybrid RANS/LES, blended eddy viscosity); §2.2, Eqs. (10)–(18) (FPV, presumed PDFs, scale-similarity and transport closures of the subgrid variance, flame index); §3.1, Figs. 5–8; §3.2, Figs. 12–16; §4.
- [Mardani & Nazari (2022)](/sources/mardani-2022.md) — §1; §2, Eqs. (1)–(17) (Magnussen cascade, EDC); §4, Eqs. (18)–(20), Fig. 2 (validity limits); §4.1, Eqs. (21)–(25), Table 3; §4.2, Eqs. (26)–(35) (localized EDC); §5; §6.1–6.3, Figs. 4–12; §7.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — HAL author manuscript: §3.1, Figs. 5–6 (LES-embedded DNS with premixed flamelet tabulation, flamelet deconvolution); §3.2 (flame-resolved bluff-body burner, flamelet-hypothesis test proposed).
