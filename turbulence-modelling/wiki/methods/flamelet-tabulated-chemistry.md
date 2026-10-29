---
type: Method
title: "Flamelet-based tabulated chemistry"
description: "Flamelet-based tabulated chemistry stores the thermochemical state of one-dimensional flames in a table indexed by mixture fraction, progress variables and enthalpy; this page gives manifold construction and coupling, premixed against counterflow tables, extensions for curvature, stretch, ignition and wall quenching, subgrid variance, neural-network and principal-component reduction, assessments, and non-tabulated closures."
status: established
aliases: [eddy dissipation concept, EDC, representative interactive flamelet, RIF, combustion regime diagram, Borghi–Peters diagram, Karlovitz number, coherent flame model, CFM, G-equation, direct chemistry integration, tabulated chemistry, flamelet manifold, flamelet/progress variable, FPV, flamelet-generated manifold, FGM, QFM, quenching flamelet-generated manifold, QFM-EGR, FPV-κ, FPV-h, composition space model, ignition source-term patch, optimal estimator, premixed flamelet tabulation, subgrid mixture-fraction variance, scalar variance model, neural-network tabulation, stretch factor, extended Takeno flame index, principal-component transport, PC transport, counterflow flamelet database, partially premixed flamelet tabulation]
tags: [combustion, dns, tabulated-chemistry, flame-wall-interaction, hybrid-rans-les]
timestamp: 2026-10-29T07:41:00Z
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
| [Zhang et al. (2023)](/sources/zhang-2023-c.md), FGM "FP" (§3.2) | freely propagating premixed methane–air flamelets, $0.4\le\phi_{\mathrm{eq}}\le2.6$ in steps of 0.02, GRI-Mech 3.0, unity Lewis number, interpolated to air below the lean limit | $(Z,Y_c)$, $Y_c=Y_{\mathrm{CO_2}}+Y_{\mathrm{H_2O}}$, on $500\times200$ points; $Z_v$ added for the presumed PDF |
| Zhang et al. (2023), "CF-Diff" (§3.2) | steady counterflow diffusion flamelets (air against methane) from strain 0.1 s⁻¹ to extinction, plus unsteady flamelets obtained by imposing a strain far above extinction | as FP |
| Zhang et al. (2023), "CF-PaPre" (§3.2) | as CF-Diff with a rich premixed fuel side at $\phi_{\mathrm{eq}}=2.6$ (the partially premixed flamelet tabulation of Wen et al., as cited there, with the boundary equivalence ratio fixed) | as FP |
| [Nmira et al. (2023)](/sources/nmira-2023.md), §2.1 (the authors' earlier LES/presumed-FDF model, extended to soot) | non-adiabatic steady laminar counterflow diffusion flamelets of ethylene, Qin et al. mechanism, solved in physical space; gas-phase soot rates stored in the same library | $(\tilde Z,\tilde\chi_Z,\tilde X_{\mathrm R})$ with $\widetilde{Z^2}$ transported, $\beta$ FDF in $Z$ and $\delta$ FDFs in $\chi_Z$ and $X_{\mathrm R}$ ("single flamelet closure") |
| [Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §6.3 (from the first author's earlier work) | FPV for a piloted dimethyl-ether/air jet diffusion flame | mixture fraction and progress variable |

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
premixed flame with eigenvalue $s_{\mathrm L}$ (the laminar burning velocity), and
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

Zhang et al. (2023, §3.3, Eq. 8) close the filtered source term of their
FGM table with a $\beta$-PDF in $Z$ and a top-hat PDF in $Y_c$, the two
taken as statistically independent, and obtain both subgrid variances
algebraically from the resolved gradients under local equilibrium,
$Z_v=\alpha_v\Delta(\nabla\tilde Z)^2$ and likewise for $Y_c$, with
$\alpha_v=1/12$ (page-local) and $\Delta$ the cube root of the cell
volume (printed form in Qualifications). Eleven points in $Z_v$ make the
table three-dimensional, about 591 Mb.

**Transported minor species.** A table built from premixed flamelets
carries the CO and H$_2$ of those flamelets. Zhang et al. (2023, §3.1,
Eq. 7), after earlier work they cite, also transport CO and H$_2$ with a
split source: the production rate is read from the table, the
consumption rate is made proportional to the transported mass fraction,
$\overline{(\dot\omega_{k,\mathrm c}/Y_k^{\mathrm{tab}})}\,\tilde Y_k$ with
$Y_k^{\mathrm{tab}}$ the tabulated value (page-local symbols), so that only
consumption adapts locally.

## Flamelet validity and combustion regimes

Whether a flame can be represented by laminar flamelets is judged on
regime diagrams, which the review of combustion models for
internal-combustion engines by [Posch et al. (2025)](/sources/posch-2025.md),
§3.3, states after Peters and Borghi, with unity Schmidt and Lewis
numbers. Page-local symbols: $u'$ the rms velocity fluctuation, $L$ the
integral length (registry §8), $Re_L=u'L/\nu$, the Damköhler number
$Da=\tau_L/\tau_{\mathrm{ch}}$ of the integral and chemical times
($\tau_{\mathrm{ch}}$ as in registry §11), the Karlovitz number
$Ka=\tau_{\mathrm{ch}}/\tau_\eta=(l_{\mathrm F}/\eta)^2$ and the
reaction-zone Karlovitz number $Ka_\delta=(l_{\mathrm r}/\eta)^2=(l_{\mathrm r}/l_{\mathrm F})^2Ka$,
$l_{\mathrm r}$ the reaction-zone thickness (Eqs. 13–17), with
$Re_L=Da^2Ka^2$ (Eq. 16). The premixed regimes (Fig. 2) are bounded by
$Re_L=1$, $Ka=1$, $u'/s_{\mathrm L}=1$ and $Ka_\delta=1$: wrinkled
flamelets ($Ka<1$, $u'/s_{\mathrm L}<1$), corrugated flamelets ($Ka<1$,
$u'/s_{\mathrm L}>1$), thin reaction zones ($Ka>1$, $Ka_\delta<1$) and
broken reaction zones ($Ka_\delta>1$); $l_{\mathrm r}/l_{\mathrm F}$ lies
between about 0.1 at atmospheric pressure and 0.03 at higher pressure, and
$Ka_\delta=1$ corresponds to $Ka=100$ for $l_{\mathrm r}/l_{\mathrm F}=0.1$
(Fig. 2). The non-premixed diagram (Fig. 3, Eqs. 18–23) compares the
stoichiometric mixture-fraction fluctuation with the diffusion and
reaction-zone thicknesses in mixture-fraction space and the stoichiometric
scalar dissipation rate with its extinction value, separating extinction,
connected reaction zones, connected flame zones and separated flamelets.
The premixed flamelet assumption holds at high $Da$ and needs $Ka<1$ for a
coherent front, "although it seems to stay valid while $Ka_\delta<1$"
(§4.1); Posch et al. cite DNS at several Karlovitz numbers by Lipatnikov et
al. concluding that the domain of flamelet validity is wider than first
assumed, and a revised diagram of Kheirkhah & Gülder (§4.1). Two limits are
stated (§3.3.2, §6.2.1): the diagrams assume homogeneous isotropic
turbulence, from which engine flow is "far", so they give only a "fairly
rough distinction"; and for thermodiffusively unstable flames the
classical premixed diagrams are inadequate, Aspden et al. and Howarth et
al. rescaling them with the speed and thickness of the freely propagating
flame, while Berger et al. found the consumption speed, and hence the
turbulent flame speed, raised by a factor of three by thermodiffusive
instabilities (as cited; the flame of
[Berger et al. (2022)](/sources/berger-2022.md) is in the assessment
below). The review excludes low-Damköhler cases, chemical times in most
technical applications being shorter than transport times (§3.3).

**The non-premixed flamelet and its mapping** (Posch et al., §4.8). With
unity Lewis number and a conserved $Z$, each species obeys
$\partial_tY_k=(\chi_Z/2)\,\partial^2Y_k/\partial Z^2+\dot\omega_k$ (Eq. 54;
$\dot\omega_k$ the production rate, page-local), in which the scalar
dissipation rate is the only link to the flow; the mean is mapped with a
$\beta$-PDF of $Z$ and a log-normal PDF of $\chi_Z$ (Eq. 55),
$$\tilde Y_k=\int_0^1\!\!\int_0^\infty P_Z(Z;\boldsymbol x,t)\,P_\chi(\chi_Z;\boldsymbol x,t)\,Y_k(Z,\chi_Z,p,T)\,\mathrm d\chi_Z\,\mathrm dZ .$$
Tabulated reductions (ILDM, FGM, flamelet/progress variable, unsteady and
tabulated FPV) store such solutions; FGM, the authors state, "provides a
good balance between computational efficiency and the ability to
accurately capture TCI". The **representative interactive flamelet** (RIF)
instead solves one-dimensional flamelets during the run with the history
of the scalar dissipation rate, costlier than tabulation because flamelet
time steps are much smaller than CFD steps, with multiple flamelets
introduced sequentially; the choice of progress variable matters, and
partially premixed flamelets or blended premixed and diffusion tables
serve multi-mode combustion (§4.8, §6.3.2–6.3.3, as cited). The same
equations bear on [conditional moment closure](/methods/conditional-moment-closure.md),
whose relation to flamelets the review prints in two readings.

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

**Premixed against counterflow tables in a multi-regime flame**
([Zhang et al. 2023](/sources/zhang-2023-c.md)). The Darmstadt
multi-regime burner flame MRB26b, a stratified methane–air flame with a
multi-regime inner reaction zone and a lean premixed outer zone, is
computed by LES in [OpenFOAM](/software/openfoam.md) (about 3.87 million
hexahedra, dynamic [Smagorinsky](/methods/smagorinsky-model.md) eddy
viscosity, second-order TVD convection, PISO, $\Delta t=0.32$ µs at CFL
about 0.4, 20 flow-through times of statistics; §2, §3.4). On the cold
flow the time-averaged ratio of subgrid to total kinetic energy is
generally below 0.2 in the flame region, so at least 80% of the
turbulent kinetic energy is resolved (Pope's criterion, as cited; §2,
Eqs. 1–2; see [large-eddy simulation](/definitions/large-eddy-simulation.md)).
Four cases combine the three tables above with the presumed PDF and, for
the premixed table only, the
[dynamically thickened flame](/methods/thickened-flame-model.md) (Table 1).
Against the Raman/Rayleigh measurements (§4.1, Figs. 6–11):

- all tables and both closures give very similar mean velocity,
  temperature, mixture fraction and major species (CH$_4$, O$_2$,
  CO$_2$, H$_2$O), in good agreement with experiment;
- the premixed table over-predicts CO and H$_2$ in the inner reaction
  zone, most downstream; the two counterflow tables, which give nearly the
  same results, match the experiment better. Scatter plots of $\tilde Z$
  against $\tilde Y_c$ are alike for the premixed and the partially
  premixed table while the conditional CO and H$_2$ differ, so the
  authors locate the error in the tabulation, not in the control-variable
  field; the counterflow flamelets contain species diffusion along $Z$
  (fuel–air mixing), which lowers CO and H$_2$ on the rich side, and
  strain, which a study they cite shows to reduce CO and H$_2$
  production (Fig. 11);
- transporting CO and H$_2$ with the linearized consumption source repairs
  the premixed table, bringing its conditional means close to the
  counterflow tables (Figs. 7, 9, 10, 12);
- in the outer premixed zone the minor species are nearly the same in all
  tables and are predicted well; even there the counterflow tables work,
  which the authors explain by similar control-variable bounds and
  near-premixed burning at low strain.

A Takeno-type flame index of fuel and oxidizer gradients,
$\nabla\tilde Y_{\mathrm{CH_4}}\cdot\nabla\tilde Y_{\mathrm{O_2}}/(\lvert\nabla\tilde Y_{\mathrm{CH_4}}\rvert\lvert\nabla\tilde Y_{\mathrm{O_2}}\rvert)$
(Eq. 20, after Yamashita et al. as cited), is binned into premixed
($>0.99$), dominantly premixed (0.8–0.99), multi-regime ($-0.8$ to 0.8),
dominantly non-premixed and non-premixed classes (Table 2). In the inner
zone the three tables give similar distributions: non-premixed burning is
rare, as in the experiment, and multi-regime burning dominates, but
downstream the simulations give more premixed than multi-regime burning,
unlike the experiment, which the authors read as too fast dilution of the
rich mixture (§4.3, Fig. 18). The angle between $\nabla\tilde Z$ and
$\nabla\tilde Y_c$ shows back-supported propagation (toward leaner
mixture) upstream and front-supported downstream, as in the experiment
(Eq. 21, Fig. 19). Tang et al. (2022) and Fureby & Nilsson (2023), here,
use the same kind of index for hydrogen.

**Soot and radiation on a non-adiabatic flamelet library** (Nmira et al.
2023). Page-local symbols for this paragraph: $X_{\mathrm R}$ the enthalpy
defect (radiative-loss parameter) of the flamelets, $N_{\mathrm s}$ and
$Y_{\mathrm s}$ the soot number density and mass fraction,
$\boldsymbol\phi_{\mathrm g}=(Z,\chi_Z,X_{\mathrm R})$ and
$\boldsymbol\phi_{\mathrm s}=(N_{\mathrm s},Y_{\mathrm s})$, $\alpha_{\mathrm s}$
the weight of the sooting mode (not the registry's DG blending factor
$\alpha$), $Z_{\mathrm s}$ the mixture fraction at which soot is burnt, $H$
the Heaviside function, and $f_{\mathrm{rad}}$ the radiant fraction. The
authors run LES of the 15-kW FM Global buoyant ethylene diffusion flames
(porous burner of diameter 15.2 cm, oxidizer $\mathrm O_2$ mole fractions
0.209, 0.168, 0.152) with a dynamic Smagorinsky stress and a dynamic eddy
diffusivity (see the [dynamic procedure](/methods/dynamic-procedure.md)),
the scalar dissipation of Jiménez et al. with a dynamic constant, and
Lindstedt's two-equation acetylene/benzene soot model whose parameters are
kept from earlier jet-flame studies (§2.1–2.2). The soot source factorizes
into a tabulated gas-phase part and a soot part computed on the fly,
$\dot\omega=\dot\omega_{\mathrm g}(\boldsymbol\phi_{\mathrm g})\,\dot\omega_{\mathrm s}(\boldsymbol\phi_{\mathrm s})$
(Eq. 1), and the filtered source is closed with a presumed bimodal
conditional FDF after Mueller and co-workers (Eqs. 2–7):

$$P(\boldsymbol\phi_{\mathrm s}\mid\boldsymbol\phi_{\mathrm g})=\big[(1-\alpha_{\mathrm s})\,\delta(\boldsymbol\phi_{\mathrm s})+\alpha_{\mathrm s}\,\delta(\boldsymbol\phi_{\mathrm s}-\boldsymbol\phi_{\mathrm s}^*)\big]\,H(Z-Z_{\mathrm s}),\qquad \alpha_{\mathrm s}=\frac{\tilde N_{\mathrm s}^2}{\widetilde{N_{\mathrm s}^2}\,H_{\mathrm{int}}},\quad H_{\mathrm{int}}=\int_0^1H(Z-Z_{\mathrm s})\,\tilde\beta(Z)\,\mathrm dZ,$$

with $\widetilde{N_{\mathrm s}^2}$ transported and $\boldsymbol\phi_{\mathrm s}^*=\tilde{\boldsymbol\phi}_{\mathrm s}/(\alpha_{\mathrm s}H_{\mathrm{int}})$.
Variant S1 drops the Heaviside factor (intermittency only, $H_{\mathrm{int}}=1$);
variant S2, the authors' contribution, keeps it, taking $Z_{\mathrm s}$ at
the lean zero of the tabulated surface-growth rate, where acetylene is
consumed, so that $Z_{\mathrm s}=Z_{\mathrm s}(\chi_{Z,\mathrm{st}},X_{\mathrm R,\mathrm{st}})$
comes from the flamelet library alone. Radiation uses a rank-correlated
full-spectrum $k$-distribution model with non-grey soot as reference;
subgrid absorption–turbulence interaction is neglected and subgrid
emission closed by convolution with the same presumed FDF (§2.3).

On $3.6\times10^6$ cells (2.5 mm near the burner, a grid that resolves
"more than 80% of temperature variance", §3.1) the baseline M1 reproduces
the measured mean and RMS temperature, soot volume fraction and soot
intermittency profiles, with radiant fractions 0.389, 0.255, 0.192
against measured 0.34, 0.30, 0.22, within about 15% (§3.2, Figs. 2–4,
Table 2), where $f_{\mathrm{rad}}=(\dot Q_{\mathrm{em}}-\dot Q_{\mathrm{abs}})/\dot Q$.
Dropping the soot–mixture-fraction correlation (S1, run M2) raises the
mean soot oxidation by one order of magnitude and makes soot radiation
negligible ($f_{\mathrm{rad}}$ 0.219, 0.159, 0.138), and neglecting the
subgrid emission interaction (M5) over-predicts the mean and RMS soot
volume fraction by a factor of about two although $f_{\mathrm{rad}}$ hardly
changes (0.386 against 0.389), because over-predicted soot emission
(+15.1%) balances under-predicted gas emission (−17.9%) (§3.3–3.4, Figs.
5–6, Table 2). Grey soot (M3) and a weighted-sum-of-grey-gases model (M4)
change $f_{\mathrm{rad}}$ little; the CPU time per step on 700 cores is
5.34 s for M1 and 4.10 s for M4 (Table 1). The authors conclude that
the soot prediction controls the thermal field and that the subgrid
emission interaction matters even in a well-resolved LES (§4). The
evidence is a comparison with one set of experiments and between model
variants; the soot-model equations and the grid study are in
supplementary material that is not in the file read.

**A discontinuous Galerkin LES with an FPV table.**
[Lv & Ekaterinaris (2023)](/sources/lv-2023.md), §6.3, Figs. 15–16, show a
discontinuous Galerkin LES (12,000 elements, polynomial degree $N=2$,
turbulent inflow condition) of the Sandia piloted dimethyl-ether/air jet
flame (jet diameter 7.45 mm; main jet, pilot and coflow at 45.9, 5.8 and
0.9 m/s) with an FPV table in mixture fraction and progress variable,
taken from the first author's earlier work. Mean temperature, Bilger
mixture fraction and CO mole fraction are in "excellent agreement" with
the measurements apart from a near-nozzle discrepancy, which the authors
attribute to "the lack of consideration for the heat-transfer effect in
the employed flamelet model formulation". No error norm is given.

**In engine CFD** (Posch et al. 2025, §5.2.5, §5.3). The
review reports, as the cited studies claim them: a five-dimensional FGM
matched an optical partially premixed engine where a four-dimensional FGM
predicted very late ignition, and FGM beat the partially stirred reactor
with roughly 90% less computational time (Xu et al.); lean and diluted
spark-ignition and jet-ignition engines raise the Karlovitz number and
move combustion out of the flamelet regimes, where tuning model constants
"often compromises the fundamental accuracy and predictive capability"
(§5.3, §6.3.2). The review's engine evidence is in-cylinder pressure and
heat release, emissions not allowing "any useful validation" (§5).

## Stretch beyond the unstretched flamelet

[Coulon et al. (2023)](/sources/coulon-2023.md) test the assumption that
the turbulent burning rate of a premixed flame is set by its area alone.
With the turbulent consumption speed $S_T$, the unstretched laminar flame
speed $s_{\mathrm L}$ (page-local, not the registry's Lundquist number
$S_L$), the turbulent flame surface $A_T=\int_\Omega\lvert\nabla c\rvert\,dV$
and a reference surface $A_0$, they write (Eqs. 7–9)
$$\frac{S_T}{s_{\mathrm L}}=I_0\,\frac{A_T}{A_0},$$
where the **stretch factor** $I_0$ (page-local, as are $S_T$, $A_T$, $A_0$)
accounts for strain and curvature; it is "generally assumed of order unity
in many flamelet models", which they call generally true for fuels with
Lewis number near one (§3.1). Their three-dimensional DNS of slot-burner
flames in the thin-reaction-zones regime (Karlovitz number about 7.8; see
[direct numerical simulation](/definitions/direct-numerical-simulation.md))
share $s_{\mathrm L}\approx0.38$ m/s and a thermal thickness of about 450 µm, so that
the fuel Lewis number is the main difference (§2.2, Table 1):

- methane–air at $\phi_{\mathrm{eq}}=1$ and ammonia–hydrogen–air (46% hydrogen
  by volume) at $\phi_{\mathrm{eq}}=1$ give $I_0\to1$ once stationary, so
  the burning-rate increase is wrinkling-driven (Damköhler's first
  hypothesis) (§3.1, Fig. 5);
- lean hydrogen–air at $\phi_{\mathrm{eq}}=0.45$ gives $I_0>1$, growing from
  about 1 at the flame foot to about 2.5 at the tip, with thin intensely
  burning segments at positive curvature and near-extinction at negative
  curvature (§3.3, Figs. 13, 16).

They state that the stretch effect at $\phi_{\mathrm{eq}}=0.45$ was not
observed in computations at $\phi_{\mathrm{eq}}=0.7$ by others, and that
Berger et al. report even higher $I_0$ in leaner conditions (§3.1, §3.3,
as cited there). Laminar premixed **counterflow flamelets** computed over
$0.3<\phi_{\mathrm{eq}}<0.7$ and strain rates up to twice the DNS mean
tangential strain on the isosurface (2436 s⁻¹) give one-dimensional stretch
factors between 1 and 3, and DNS points placed in strain–equivalence-ratio
space fall in the same range: near-flat elements map to about 2, rich
positively curved ones to 2–3 irrespective of strain (§3.4, Fig. 20).
The authors propose a manifold of such flamelets in strain and local
equivalence ratio to model the stretch effect on lean hydrogen propagation,
on top of a flame-surface-density treatment of the wrinkling; the model is
not implemented in an LES. Berger et al. (2022), above, find that
counterflow flamelets at the mean tangential strain
reproduce the shift of the lean hydrogen flame to richer mixture.

## Tabulation by neural networks

The review of [Ihme et al. (2022)](/sources/ihme-2022.md), §4.1.3, frames
tabulated chemistry as a reduced state of $N_{\mathrm c}$ control variables
(page-local) on a low-dimensional manifold (Eqs. 69–70) and states that a
structured look-up table needs memory growing as $\mathcal O(10^{N_{\mathrm c}})$,
which limits it to $N_{\mathrm c}\lesssim4$; regressing the manifold with a
neural network is the alternative. The works they review, all as cited
there:

- the first neural-network chemistry of Christo et al., in transported-PDF
  simulations, with two hidden layers, mixture fraction and progress
  variable as inputs and the progress-variable production rate as output;
- networks of optimal architecture found by pattern search, in which deep
  networks with connections beyond neighbouring layers are more accurate
  and the "knowledge density" (accuracy over memory) is "significantly
  higher" than for conventional tabulation, used in LES of a bluff-body
  swirl flame (Fig. 29);
- LES of a jet flame with networks trained on filtered steady flamelets
  (Flemming et al.; Kempf et al.), grouped multi-target networks for
  unsteady-flamelet/presumed-PDF engine LES (Owoyele et al.), and
  networks trained on linear-eddy-model simulations (Sen & Menon);
- principal-component manifolds, local, kernel and autoencoder variants,
  with Sutherland & Parente the first to transport principal components
  directly;
- a random-forest assignment of combustion submodels of different cost
  (finite-rate chemistry, a two-scalar flamelet/progress-variable model)
  in a rocket-combustor LES, which cut cost by 20% "with good agreement"
  with finite-rate-chemistry LES; its error is "limited by the predictive
  capability of the lowest-performing submodel" (§4.1.4, Fig. 34).

**Transporting principal components instead of species.**
[Kumar et al. (2023)](/sources/kumar-2023.md) apply the
principal-component route in a [DNS](/definitions/direct-numerical-simulation.md)
of turbulent premixed combustion (contribution: the three-dimensional
validation; the method is background they cite, §1–2). The temperature
and seven representative species (H$_2$, H, O$_2$, H$_2$O, CH$_4$, CO,
CO$_2$; the major species above a mass fraction of $10^{-2}$ plus the H
radical for curvature and differential diffusion) form a normalized state
$\boldsymbol\psi_r$ whose covariance eigenvectors $\mathsf Q$ give the
components $\boldsymbol\Psi=\mathsf Q^{\mathsf T}\boldsymbol\psi_r$
(page-local symbols; Eq. 8). Each retained component obeys a
transport equation with source $\dot{\boldsymbol\omega}_\Psi=\mathsf Q^{\mathsf T}\dot{\boldsymbol\omega}_{\psi}$
and diffusion matrix $\mathsf Q^{\mathsf T}\mathsf D_\psi\mathsf Q$, which is
diagonalized by a constant rotation of the components to one coefficient
each (Eqs. 9–11). Four of eight components carry more than 99% of the
variance; the third and fourth, about 2% together, carry H$_2$ and H and
are, the authors state, essential for curvature and differential
diffusion (§3.4, Figs. 3–4). The closure terms (component sources and
diffusivities, viscosity, ratio of specific heats, temperature, mixture
molecular weight) are small networks trained by Levenberg–Marquardt on
stacked snapshots of a two-dimensional species DNS, an architecture
[4 15 10 4] for the sources with correlation at least 99.9% against the
training data; larger networks fit better but are, they state, "very
sensitive to input fluctuations" (§3.4, Fig. 5). Non-transported species
such as HO$_2$ are recovered from the components by further networks.
Training on one-dimensional laminar flames is rejected because such
flames do not reach the states of the turbulent flame (§3.1, Fig. 2), and
the two-dimensional training data span the states reached by all
three-dimensional runs in the first two components (§3.7, Fig. 13).
Results and costs are on the
[DNS](/definitions/direct-numerical-simulation.md) page; the authors call
the choice of training data and representative species "largely domain
expert dependent" (§4). They list ISAT tabulation, PRISM, ILDM, CSP, adaptive chemistry and
network tabulation of chemistry as competing accelerations (§1).

The review's general caution, that learned closures are mostly tested
a priori, is on
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

Posch et al. (2025), §6.4, list the network uses in engine combustion
they cite: networks for representative species with PCA-based
classification, clustered networks for source terms, a network replacing
flamelet tables with a memory reduction by a factor of 5000 (Ihme et al.),
RCCE combined with networks, network flamelet libraries in engine LES,
and a physics-informed network for reaction-kinetics equations; they
state that learned closures "have been mostly developed and tested on
benchmark flame simulation cases" and that data-driven models need
training data covering the engine's temperature and pressure range
(§6.4.1–6.4.2).

## Contrast: closures that do not tabulate

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
Kolmogorov time to a chemical time, $s_{\mathrm L}$, $S_T$ the laminar and
turbulent flame speeds ($s_{\mathrm L}$ not the registry's Lundquist number $S_L$), $\chi_{\mathrm{fs}}$ the reacting fraction of the
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
speed, $S_T\approx s_{\mathrm L}\sqrt{Re_T+1}$, which gives
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

**Finite-rate chemistry with a partially stirred reactor in LES.**
[Fureby & Nilsson (2023)](/sources/fureby-2023.md), §3.3, choose finite-rate
chemistry over flamelet models for LES of a cavity-stabilized hydrogen
ramjet combustor (Mach 2.2 at the isolator entrance, air stagnation
temperatures 1080–1370 K) because the flame is highly fragmented and the
flow and chemical time scales are similar; the filtered rates are closed
with the LES partially stirred reactor (details on the
[thickened flame model](/methods/thickened-flame-model.md) page, where the
finite-rate alternatives are listed). Their own hydrogen mechanism (Z22) is
the only one of three tested that reproduces both observed stabilization
modes (§6.1, Fig. 4). An extended Takeno index,
$$\zeta_M=\tfrac12\,\frac{Z-Z_{\mathrm{st}}}{\lvert Z-Z_{\mathrm{st}}\rvert}\Big(1+\frac{\nabla Y_{\mathrm{H_2}}\cdot\nabla Y_{\mathrm{O_2}}}{\lvert\nabla Y_{\mathrm{H_2}}\cdot\nabla Y_{\mathrm{O_2}}\rvert}\Big)$$
($Z_{\mathrm{st}}$ the stoichiometric mixture fraction; $\zeta_M=0$
non-premixed, $+1$ rich premixed, $-1$ lean premixed; page-local), after
Lock et al., shows lean premixed burning dominating the cavity-stabilized
case and non-premixed burning the jet-wake-stabilized case (§6.6, Fig. 12).
Tang et al. (2022), above, find diffusion burning over almost the whole
reacting zone of their two scramjet combustors and take it as support for
a non-premixed flamelet table; the combustors, injection and operating
points differ.

**Detailed chemistry without a table in a detonation code.**
[Sun et al. (2023)](/sources/sun-2023.md), §2.1–2.2, integrate detailed
finite-rate chemistry with the stiff extrapolation solver seulex in an
operator-splitting step in the [OpenFOAM](/software/openfoam.md) solver
detonationFoam, without a table; the code has no turbulence–chemistry
closure and its validation cases are laminar or inviscid (§3).

**Quasi-laminar chemistry in supersonic film cooling.**
[Wei et al. (2023)](/sources/wei-2023.md), §II B, list flamelet, PDF and
linear-eddy closures as the options for the turbulence–chemistry
interaction and use none: in a wall-resolved LES of the Burrows–Kurkov
hydrogen film-cooling flame (Mach 2.44 vitiated air) the filtered rates
are evaluated at the filtered state,
$\overline{\dot\omega}_k=\dot\omega_k(\bar\rho,\tilde Y_1,\dots,\tilde T)$,
with a 7-species, 7-reaction hydrogen mechanism, justified by citing
earlier supersonic-combustion LES and by flow time scales much smaller
than the chemical ones, a well-stirred-reactor-like mode. They also find
non-equilibrium (finite-rate) burning, with oxygen penetrating the flame
front on the fuel-rich side, and conclude that finite-rate combustion
models are needed (§IV C). The subgrid closure is the
[one-equation subgrid kinetic-energy model](/methods/subgrid-kinetic-energy-equation-model.md);
the turbulent transport of heat and species is on
[turbulent Prandtl number](/definitions/turbulent-prandtl-number.md).

**Flame-surface, level-set, PDF and direct-chemistry closures in engine
CFD.** Posch et al. (2025), §4.3–4.6 and §5.1.5, state the other
non-tabulating families as cited; page-local symbols $\Sigma_{\mathrm f}$
the flame surface density, $\bar s_{\mathrm f}$ the mean consumption
speed, $\alpha_\Sigma$, $\beta_\Sigma$ the strain and consumption
constants, $\tilde c$ the Favre progress variable, $G$ a level-set
function and $\boldsymbol n=-\nabla G/|\nabla G|$:

- **Coherent flame model** (Marble & Broadwell, Candel & Poinsot): the
  mean rate $\rho_u\bar s_{\mathrm f}\Sigma_{\mathrm f}$ ($\rho_u$ the
  unburnt density; Eq. 32) with
  $\partial_t\Sigma_{\mathrm f}+\partial_i(\tilde u_i\Sigma_{\mathrm f})=\partial_i\big((\nu_t/Sc_t)\partial_i\Sigma_{\mathrm f}\big)+\alpha_\Sigma(\varepsilon/k)\Sigma_{\mathrm f}-\beta_\Sigma\bar s_{\mathrm f}\Sigma_{\mathrm f}^2/(1-\tilde c)$
  (Eq. 34), $\beta_\Sigma$ generally 1 and $\alpha_\Sigma$ of order one,
  settings far from unity "may significantly deteriorate the predictions"
  (§4.3); the review also states the engine extensions ECFM and ECFM3Z
  (§4.3, Fig. 5). Models that assume unity Lewis number a priori, such
  as this one, "are not able to account for differential diffusion
  effects" (§6.2.1).
- **G-equation** (Peters): the front $G=G_0$ moves as
  $\partial_tG+\boldsymbol u\cdot\nabla G=s_{\mathrm L}|\nabla G|$ (Eqs.
  36–40), valid for $Ka<1$, with an iso-temperature form for the thin
  reaction zones (Eq. 42) and turbulent flame-speed closures that allow
  calibration against experiment (§4.4, §5.1.3, Table 5).
- **PDF methods**: the presumed $\beta$-PDF (Eqs. 47–49) cannot represent
  the burnt-mixture probability of a premixed flame and is "not
  suitable" there (§4.6); the transported PDF (Eq. 50) needs a mixing
  model and constant ($C_\Phi=2.0$ in the cited engine studies) and its
  cost makes it "impractical for industrial applications" even in RANS
  (§5.2.2).
- **Direct chemistry integration**, finite-rate chemistry from the cell
  state with multi-zone grouping and adaptive mesh refinement, is "a
  clear trend" in RANS engine simulation, but computing sources from
  averaged values neglects the turbulence–chemistry interaction
  "completely" (§5.1.5, §5.3); for compression-ignition engines the review
  prints the disagreement between Kokjohn & Reitz (small-scale interaction
  not dominant in low-temperature diesel combustion) and Kung & Haworth
  (interaction relevant), and concludes that "a general justification to
  neglect TCI in CI engines cannot be derived" (§5.2.4).

## Tables inside conditional closures

Tabulated chemistry also supplies the reaction rates of conditional
closures, which take the table as given and close the
turbulence–chemistry interaction separately. The review of
[conditional source-term estimation](/methods/conditional-source-term-estimation.md)
(CSE) by [Salehi et al. (2024)](/sources/salehi-2024.md), §2.8, lists
three ways the chemistry enters, all as cited there:

- **Trajectory-generated low-dimensional manifolds** (TGLDM, after Pope
  and Maas): the homogeneous reactor equations $\partial_tY_k=\dot\omega_k$
  (page-local: $\dot\omega_k$ the reaction rate of species $k$) are
  integrated from points of the realizable boundary given by the element
  balance, and the state is tabulated along the trajectories against a few
  progress variables (for example $Y_{\mathrm{CO_2}}$ and
  $Y_{\mathrm{H_2O}}$), with Delaunay interpolation (§2.8.1, Eqs. 32–33).
  The authors report success for methane–air non-premixed flames and
  failure for longer-chain fuels, whose trajectories cross (n-heptane
  trajectories cross themselves), and for premixed flames unless many
  progress variables are used, because diffusion drives the
  low-temperature part of a premixed front (Fig. 12). FPI/FGM tables
  built from one-dimensional premixed flames (Eq. 34) and REDIM bring the
  diffusion effects into the manifold; the premixed CSE of Salehi et al.
  (ref. [88], as cited) generated its "TGLDM" trajectories from Eq. (34)
  (§2.8.1).
- **Laminar flamelet decomposition** (LFD, Bushe and Steiner): the
  conditional means are expanded in a library of $N_{\mathrm f}$ laminar
  flamelet profiles with unknown non-negative weights, the discrete PDF of
  upstream strain rate, solved by non-negative least squares (§2.8.2,
  Eqs. 35–38). Its accuracy is bounded by the library: in Sandia flame D a
  steady-flamelet library under-predicts NO, an unsteady one over-predicts
  it, and mixed libraries can "tune" the result without clear
  justification (§3.1.2, Fig. 25).
- **Detailed chemistry**, tested only a priori with a 16-species,
  35-reaction skeletal mechanism, at accuracy comparable to coarse-grid
  conditional moment closure; elemental mass conservation is not
  guaranteed because the conditional species come from an inverse problem
  (§2.8.3).

The table look-up is a cost item of its own: hash tables for the TGLDM
look-up and pre-tabulated PDF integrals brought the CSE share of the total
cost from 85% to 10% (first-order Tikhonov) and below 3% (Bernstein
polynomials of degree 10) in RANS of Sandia flames D and F (§3.1.2), and
in the latest CSE calculations, the review states, "search, retrieval
and interpolation of data from the tabulated chemistry have become the
most computationally expensive tasks in the CSE routine" (§4.1). CSE has
relied on static FGM or TGLDM tables, which "worked well for simple fuels
like methane, methanol, ethanol and acetone"; the authors propose
neural-network tabulation and direct chemistry integration as future
work, and state that "typically two chemical progress variables and if
needed, one for temperature or enthalpy, seem to be sufficient in most
cases" (§4.1–4.3).

The review of artificial intelligence for supersonic combustion by
[Le et al. (2024)](/sources/le-2024.md) lists
flamelet-generated manifolds and in-situ adaptive tabulation among the
classical accelerations of chemistry, which it states takes "over 85 % of
the total computational cost" of engine-combustion simulations (§3, §3.2);
it writes the filtered flamelet/progress-variable source as
$\tilde{\dot\omega}=\int\dot\omega(Z,c)\tilde P(Z,c)\,\mathrm dZ\,\mathrm dc$
with $\tilde P$ the filtered joint density (Eq. 19; $\dot\omega$
page-local, the progress-variable source) and reports, as cited, flamelet
closures of supersonic combustors (two-dimensional RANS, LES of the DLR
strut combustor with a partially premixed progress-variable flamelet, a
multi-mode flamelet), a deep network whose predicted joint filtered
density of $Z$ and $c$ in MILD combustion "deviates significantly" from
presumed shapes, and flamelet tables regressed by several multilayer
perceptrons (§3.3, Table 5).

## Qualifications

- **Printed forms in Mardani & Nazari (2022)**, from the paper's own
  definitions *(compiler check, not in the sources)*. The root of
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
  configuration is laminar.
- **Flame thickness.** Böttler et al. ($l_f$) and Steinhausen et al.
  ($\delta_L$) both define the thermal thickness
  $l_{\mathrm F}=(T_b-T_u)/\max|\mathrm dT/\mathrm dx|$ (Böttler §3.2;
  Steinhausen §2.1, printed with $\delta$ in the gradient).
- **Printed formula.** Steinhausen et al.'s mean relative error (Eq. 7)
  divides a ratio of sums by the number of samples $N$; the ratio of sums
  is already independent of the sample count, so as printed the error
  scales with $1/N$ *(compiler check, not in the sources)*.
- **Printed forms in Zhang et al. (2023).** §2 defines the central jet
  at $\phi_{\mathrm{eq}}=2.6$ and the first slot at $\phi_{\mathrm{eq}}=0$
  (air), while §3.2 bounds the premixed flamelets and the rich side of
  CF-PaPre by "$\phi_{slot1}=2.6$" and writes "$Z_{slot1}\approx0.132$"
  (§4.1.2 prints $Z\approx0.0446$ at the lean slot's 0.8; no relation
  between $Z$ and $\phi_{\mathrm{eq}}$ is printed). The variance model is
  printed with $\Delta$ to the first power, $Z_v=\alpha_v\Delta(\nabla\tilde Z)^2$
  ($\alpha_v=1/12$, page-local), whose right-hand side has the dimension
  of an inverse length for a dimensionless variance; $\Delta^2$ makes it
  dimensionless *(compiler check, not in the sources)*. Eleven points in
  $Z_v$ are said to increase the table "10 times". The attribution of the
  recirculation-zone discrepancies to the unity Lewis number rests on the
  authors' earlier work, not on a test in the paper (§4.1.1).
- **Kumar et al. (2023)** state that the semi-implicit pressure update
  does not impact accuracy without a run that isolates it (§2.2); the
  coverage of the composition space by the training data is shown in
  the first two components only (Fig. 13), for one fuel and mechanism.
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
- **Posch et al. (2025).** §5.2.5 says that flamelet-model examples
  "for SI engines are listed in Table 12", whose title is "Flamelet-based
  models CI engine application examples"; §4.4 calls $s_{\mathrm L}$ "the
  turbulent flame speed", the laminar flame speed elsewhere; §3.3.2 writes
  the mixture-fraction thicknesses as $(\nabla Z)_{\mathrm F}$,
  $(\nabla Z)_{\mathrm R}$ in the text and $(\Delta Z)_{\mathrm F}$,
  $(\Delta Z)_{\mathrm R}$ in Eq. (22); §3.3 writes $Le=a_m/D$ with $a_m$
  undefined. Their evidence is cited from the reviewed studies.
- **Berger et al. (2022)** print the Karlovitz number $(l_{\mathrm F}/\eta)^2$
  as 20 and 16 for the unstable and stable flames (Table 1), while the
  $l_{\mathrm F}$ and $\eta$ of the same table give about 15.7 and 17.3
  *(compiler check, not in the sources)*. In §3.5 "TurbStable" is printed twice where the argument is
  about the unstable flame, and $I_0$ is said to appear in Eq. (7) where it
  appears in Eq. (9). Claims on halving the lateral laminar domain and on a
  half-resolution run rest on supplementary material not in the file read.
- **Printed forms in Nmira et al. (2023) and Lv & Ekaterinaris (2023).**
  Nmira et al. announce "six different modelling approaches" in §3.1
  while Table 1 and the text list five (M1–M5), and print the radiation
  model of row M1 as "RCSFK" where the text has RCFSK. Lv &
  Ekaterinaris cite the FPV model as reference [165], a Hamilton–Jacobi
  DG paper in their list; their FPV jet-flame reference is [226].

# Citations

- [Böttler et al. (2022)](/sources/bottler-2022.md) — §1; §2.1–2.2, Eqs. (1)–(14), Figs. 2–3 (coupling by major species, approximate Bilger mixture fraction, enthalpy closure, composition-space manifold with homogeneous ignition, normalization, ignition patch); §3.1–3.5, Figs. 5–11 (laminar planar, expanding and counterflow flames, minimum ignition energy); §4.
- [Berger et al. (2022)](/sources/berger-2022.md) — §2.1–2.2, Table 1; §3.4.1, Eqs. (21)–(23), Figs. 15–16 (flamelet comparison, optimal estimator); §3.4.2, Figs. 21–22; §3.4.3–3.4.4, Figs. 23–29 (strained counterflow flamelets); §3.5.
- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §1 (pre-tabulated flamelets; thickened flame with tabulated chemistry); §2, Eqs. (2)–(4) (counterflow diffusion flame in mixture-fraction space).
- [Agostinelli et al. (2021)](/sources/agostinelli-2021.md) — §2 (analytically reduced chemistry with a thickened flame instead of tabulation).
- [Böttler et al. (2023)](/sources/bottler-2023.md) — arXiv 2301.06780v1: §1 (FPV family); §2–2.1, Eqs. (1)–(4), Figs. 1–2 (FPV-$h$, FPV-$\kappa$, composition space model, coupling by major species); §3.1, Fig. 3 (a priori); §3.2, Fig. 4 (linear stability); §3.3, Figs. 5–8 (expanding flame); §4.
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — arXiv 2212.03762v1: §1 (manifold family, QFM); §2.1, Table 1 (reacting channel); §3, Eqs. (1)–(2), Figs. 2–5 (flame–vortex interaction); §4, Eqs. (3)–(5), Fig. 6 (QFM-EGR); §5, Eqs. (6)–(9), Figs. 7–9 (a priori assessment); §6.
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1, Eq. (14) (hybrid RANS/LES, blended eddy viscosity); §2.2, Eqs. (10)–(18) (FPV, presumed PDFs, scale-similarity and transport closures of the subgrid variance, flame index); §3.1, Figs. 5–8; §3.2, Figs. 12–16; §4.
- [Mardani & Nazari (2022)](/sources/mardani-2022.md) — §1; §2, Eqs. (1)–(17) (Magnussen cascade, EDC); §4, Eqs. (18)–(20), Fig. 2 (validity limits); §4.1, Eqs. (21)–(25), Table 3; §4.2, Eqs. (26)–(35) (localized EDC); §5; §6.1–6.3, Figs. 4–12; §7.
- [Coulon et al. (2023)](/sources/coulon-2023.md) — §2.2, Table 1 (three flames of equal laminar speed and thickness); Eqs. (7)–(9) (stretch factor); §3.1, Fig. 5 ($I_0\approx1$ assumption tested); §3.3, Figs. 13, 16 (lean hydrogen $I_0$ up to 2.5); §3.4, Eq. (13), Fig. 20 (counterflow flamelets in strain–equivalence-ratio space).
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §4.1.3, Eqs. (69)–(70), Fig. 29 (manifold memory scaling, neural-network and PCA tabulation, cited works); §4.1.4, Fig. 34 (random-forest submodel assignment).
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.3 (finite-rate chemistry preferred to flamelets); §6.1, Fig. 4 (mechanism dependence of the stabilization mode); §6.6, Fig. 12 (extended Takeno index).
- [Zhang et al. (2023)](/sources/zhang-2023-c.md) — §2, Eqs. (1)–(2), Fig. 2 (burner, mesh, resolved-energy criterion); §3.1, Eqs. (3)–(7) (control variables, transported CO and H$_2$ with linearized consumption); §3.2, Figs. 3–4, 11 (FP, CF-Diff, CF-PaPre tables); §3.3, Eq. (8) (presumed PDF, gradient variances); §3.4, Table 1; §4.1, Figs. 6–12 (assessment of the tables); §4.3, Eqs. (20)–(21), Tables 2–3, Figs. 18–19 (flame index, propagation direction).
- [Kumar et al. (2023)](/sources/kumar-2023.md) — §1 (competing chemistry accelerations); §2.1, Eqs. (8)–(11) (principal-component transport); §3.1, Fig. 2 (training data); §3.4, Figs. 3–5 (retained components, network closures); §3.7, Fig. 13 (composition-space coverage); §4.
- [Sun et al. (2023)](/sources/sun-2023.md) — §2.1–2.2 (detailed chemistry by operator splitting and seulex, no tabulation); §3 (laminar and inviscid validation only).
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — HAL author manuscript: §3.1, Figs. 5–6 (LES-embedded DNS with premixed flamelet tabulation, flamelet deconvolution); §3.2 (flame-resolved bluff-body burner, flamelet-hypothesis test proposed).
- [Nmira et al. (2023)](/sources/nmira-2023.md) — §1; §2.1 (non-adiabatic counterflow flamelets, presumed FDF); §2.2, Eqs. (1)–(7), Fig. 1 (factorized soot source, bimodal conditional FDF S1/S2, $Z_{\mathrm s}$); §2.3, Eqs. (8)–(10) (filtered radiative transfer, subgrid emission closure); §3.1–3.4, Tables 1–2, Figs. 2–6 (FM Global flames, model variants M1–M5); §4.
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §6.3, Figs. 15–16 (DG LES with FPV of the Sandia dimethyl-ether jet flame; heat-transfer effect missing from the flamelet model).
- [Wei et al. (2023)](/sources/wei-2023.md) — §II B (quasi-laminar closure chosen over flamelet, PDF and linear-eddy closures); §IV C, Conclusions (finite-rate burning).
- [Salehi et al. (2024)](/sources/salehi-2024.md) — §2.8.1–2.8.3, Eqs. (32)–(38), Fig. 12 (TGLDM, FPI/FGM, laminar flamelet decomposition, detailed chemistry in CSE); §3.1.2, Fig. 25 (flamelet-library dependence, cost reduction); §4.1–4.2 (tabulation cost, recommendations).
- [Le et al. (2024)](/sources/le-2024.md) — §3, §3.2 (FGM and ISAT tabulation, chemistry cost); §3.3, Eq. (19), Table 5 (flamelet closures for supersonic combustion, learned joint density and tables; review, cited works).
- [Posch et al. (2025)](/sources/posch-2025.md) — §3.3, Eqs. (13)–(23), Figs. 2–3 (premixed and non-premixed regime diagrams); §4.1 (flamelet validity); §4.3–4.6, Eqs. (32)–(50) (coherent flame model, G-equation, presumed and transported PDF); §4.8, Eqs. (54)–(55) (flamelet equation, mapping, FGM, RIF); §5.1.5, §5.2.2, §5.2.4–5.2.5, §5.3 (engine assessments, direct chemistry, TCI); §6.2.1, §6.3.2–6.3.3, §6.4 (thermodiffusive flames, multi-mode, neural networks; review).
