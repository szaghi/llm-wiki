---
type: Method
title: "Flamelet-based tabulated chemistry"
description: "Flamelet-based tabulated chemistry stores the thermochemical state of one-dimensional flames in a low-dimensional table indexed by mixture fraction, progress variables and enthalpy; this page gives the manifold construction, the extensions for curvature, wall quenching and exhaust-gas recirculation, and their a priori and a posteriori assessment against flame-resolved simulations."
status: established
aliases: [tabulated chemistry, flamelet manifold, flamelet/progress variable, FPV, flamelet-generated manifold, FGM, QFM, quenching flamelet-generated manifold, QFM-EGR, FPV-κ, premixed flamelet tabulation]
tags: [combustion, dns, tabulated-chemistry, flame-wall-interaction]
timestamp: 2026-10-26T10:27:00Z
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
thermal flame thickness; $\phi_{\mathrm{eq}}$ the equivalence ratio.

## The manifold family

As recalled by Böttler et al. (2023, §1), the flamelet/progress-variable
(FPV) approach of Pierce & Moin stores the state in a low-dimensional
manifold parametrized by control variables; flamelet-generated manifolds
(FGM) and flame prolongation of ILDM (FPI) are related approaches,
non-premixed manifolds are built from stretched non-premixed flamelets,
and premixed manifolds from unstretched premixed flamelets recover
moderate stretch effects. Steinhausen et al. (2023, §1) list FGM, FPI,
ILDM and REDIM as the manifold family for chemistry reduction, separate
from the turbulence–chemistry interaction closure that RANS or LES of a
reacting flow also needs.

The three sources build their tables from different flame families:

| Source | Flames tabulated | Control variables |
|---|---|---|
| Domingo & Vervisch (2023, §3.1–3.2) | freely propagating premixed flamelets, GRI-3.0 mechanism | progress variable (with a presumed filtered PDF of its subgrid fluctuations in the LES zones) |
| Böttler et al. (2023), FPV-$h$ (§2, after their earlier work) | unstretched premixed flames with an enthalpy variation | $(Z,h_t,Y_c)$ |
| Böttler et al. (2023), FPV-$\kappa$ (printed FPV-$\kappa_c$; §2.1, contribution) | composition-space-model flames over $0.275\le\phi_{\mathrm{eq}}\le0.6$, $-1500\le\kappa_{\mathrm f}\le5000$ m⁻¹, at fixed strain $K_{\mathrm f}=500$ s⁻¹ | $(Z,c,c_2)$, $c_2$ from the H radical |
| Steinhausen et al. (2023), QFM (§5, after Efimov et al.) | one transient head-on quenching flame of an undiluted mixture on a 300 K wall | progress variable and enthalpy |
| Steinhausen et al. (2023), QFM-EGR (§4, contribution) | 63 transient head-on quenching flames with cold exhaust-gas dilution $0\le Y_{\mathrm{EGR}}\le0.3$, plus preheated flames 300–750 K | $(c,c_2,h_t)$, $c$ from $\mathrm{CO_2}$, $c_2$ from $\mathrm{CO}$ |

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
flamelet-generated manifold, QFM, of Efimov et al., as recalled by
Steinhausen et al. 2023, §1, §5). Steinhausen et al. (2023, §4) extend it
by diluting the fresh side of a freely propagating flame with cold exhaust
gas at the inflow temperature, quenching each diluted flame on a 300 K
wall, and spanning the manifold in flamelet coordinate, time and
$Y_{\mathrm{EGR}}$ (the mass fraction of cold burnt gas mixed into the
fresh gas, page-local).

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
zones (§3.1); deconvolution by one-dimensional filtered flamelets,
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

## Qualifications

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

# Citations

- [Böttler et al. (2023)](/sources/bottler-2023.md) — arXiv 2301.06780v1: §1 (FPV family); §2–2.1, Eqs. (1)–(4), Figs. 1–2 (FPV-$h$, FPV-$\kappa$, composition space model, coupling by major species); §3.1, Fig. 3 (a priori); §3.2, Fig. 4 (linear stability); §3.3, Figs. 5–8 (expanding flame); §4.
- [Steinhausen et al. (2023)](/sources/steinhausen-2023.md) — arXiv 2212.03762v1: §1 (manifold family, QFM); §2.1, Table 1 (reacting channel); §3, Eqs. (1)–(2), Figs. 2–5 (flame–vortex interaction); §4, Eqs. (3)–(5), Fig. 6 (QFM-EGR); §5, Eqs. (6)–(9), Figs. 7–9 (a priori assessment); §6.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — HAL author manuscript: §3.1, Figs. 5–6 (LES-embedded DNS with premixed flamelet tabulation, flamelet deconvolution); §3.2 (flame-resolved bluff-body burner, flamelet-hypothesis test proposed).
