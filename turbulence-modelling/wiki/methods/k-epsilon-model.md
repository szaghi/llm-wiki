---
type: Method
title: "k-ε models"
description: "Two-equation RANS eddy-viscosity models transporting the turbulent kinetic energy and its dissipation rate: the standard high-Reynolds form, its constants and log-law calibration, the realizable variant with a two-layer wall treatment, low-Reynolds and elliptic-relaxation relatives, and evidence on bluff-body wakes, periodic hills and learned non-linear corrections."
status: established
aliases: [k-epsilon, standard k-ε, Launder–Sharma k-ε, realizable k-ε, RKE, Shih k-ε, enhanced wall treatment, EWT, two-layer k-ε]
tags: [rans, eddy-viscosity, separated-flow, boundary-layer]
timestamp: 2026-10-28T02:16:00Z
---

# k-ε models

The $k$-$\varepsilon$ models close the RANS equations with a
[Boussinesq](/definitions/boussinesq-hypothesis.md) eddy viscosity built from
two transported quantities, the turbulent kinetic energy $k$ and its
dissipation rate $\varepsilon$:

$$\nu_t=C_\mu\frac{k^2}{\varepsilon}.$$

The family includes the standard high-Reynolds-number model, low-Reynolds
forms with near-wall damping, the realizable model of Shih et al., and
elliptic-relaxation descendants. In this bundle the standard model is the
baseline of a learned non-linear correction (Tang et al. 2023), the
realizable model is the industrial reference of an automotive study
(Delassaux et al. 2023), and the $k$-$\varepsilon$ branch is the outer
formulation of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md).

## The standard model

Tang et al. (2023) print the incompressible high-Reynolds-number model that
OpenFOAM solves as their baseline, attributing the constants to Launder &
Sharma ([Tang et al. (2023)](/sources/tang-2023.md), §II A, Eqs. 4–8; arXiv
v1). In registry notation, with $\langle u_j\rangle$ the mean velocity:

$$\begin{aligned}
\partial_tk+\langle u_j\rangle\partial_jk&=\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_k}\Big)\partial_jk\Big]+P_k-\varepsilon,\\
\partial_t\varepsilon+\langle u_j\rangle\partial_j\varepsilon&=\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_\varepsilon}\Big)\partial_j\varepsilon\Big]+C_{\varepsilon1}\frac{\varepsilon}{k}P_k-C_{\varepsilon2}\frac{\varepsilon^2}{k},
\end{aligned}$$

with $P_k=-R_{ij}\partial_j\langle u_i\rangle$ and

| $C_\mu$ | $C_{\varepsilon1}$ | $C_{\varepsilon2}$ | $\sigma_k$ | $\sigma_\varepsilon$ |
|---|---|---|---|---|
| 0.09 | 1.44 | 1.92 | 1.0 | 1.3 |

The printed form carries no low-Reynolds damping functions. The authors
call the $\varepsilon$-equation empirical, "not based on the exact
transport equation" (§II A). Their Reynolds stress is the kinematic,
positive-trace $R_{ij}$ of the registry, closed as
$R_{ij}=\tfrac23k\delta_{ij}-2\nu_t\langle S_{ij}\rangle$ (Eq. 3).

**Expected values in, expected values out.** The destruction
$C_{\varepsilon2}\varepsilon^2/k$ is nonlinear in the transported variables.
Haering et al. (2022) use it as their example of a RANS source calibrated on
mean quantities that acquires spurious correlations when evaluated on
fluctuating fields inside a hybrid simulation; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)
([Haering et al. (2022)](/sources/haering-2022.md), §II D, Eqs. 1–2).

**Near-wall integration.** Elzaabalawy et al. (2023) recall that
wall-resolved versions of the model need ad hoc damping functions near the
wall "that increase the stiffness of the model and can present problems",
so that wall functions are usually employed with $k$-$\varepsilon$, whereas
the $k$-$\omega$ model integrates to the wall without damping functions but
with $\omega\to\infty$ there
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §1; see the
[Wilcox $k$-$\omega$ page](/methods/k-omega-model.md) and
[RANS wall functions](/methods/rans-wall-function.md)). Tomboulides et al.
(2025) make the same comparison from the side of a high-order
spectral-element code: they recall that the $k$-$\varepsilon$ model needs
wall damping functions that depend on the wall distance (citing Lam &
Bremhorst) and lacks a natural wall boundary condition for $\varepsilon$
(citing Patel et al.), and they motivate the
[$k$-$\tau$ model](/methods/k-tau-model.md), whose wall value is simply
zero, by these defects and by the wall singularity of $\omega$
([Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §1).

**Log-law calibration.** Heinz (2020) writes the $\varepsilon$ equation as
$D\varepsilon/Dt=C_{\varepsilon1}(\varepsilon^2/k)(P_k/\varepsilon-\alpha_\varepsilon)+D_\varepsilon$,
with $\alpha_\varepsilon=C_{\varepsilon2}/C_{\varepsilon1}=1.33$ (page-local,
the source's $\alpha$; the $\alpha^*_\varepsilon$ of the next paragraph is its
resolution-dependent form) and $D_\varepsilon$ the diffusion term, and inserts
the log-layer relations $\partial_y\langle u\rangle=u_\tau/(\kappa y)$,
$k=u_\tau^2/C_\mu^{1/2}$, $\varepsilon=u_\tau^3/(\kappa y)$, which give
$\nu_t=\kappa yu_\tau$ ([Heinz (2020)](/sources/heinz-2020.md), §2.3,
Eqs. 8–10). The $\varepsilon$ equation is then consistent with the
[law of the wall](/definitions/law-of-the-wall.md) only if

$$\kappa^2=C_\mu^{1/2}\sigma_\varepsilon\big(C_{\varepsilon2}-C_{\varepsilon1}\big),$$

which the standard constants (1.44, 1.92, 1.3) satisfy only with "a
relatively high value" $\kappa=0.43$, against $\kappa=0.41$ for the
$k$-$\omega$ constants Heinz uses (§2.3; see the
[Wilcox $k$-$\omega$ page](/methods/k-omega-model.md)). The right side is
$0.1872$, $\kappa=0.433$ *(compiler check, not in the sources)*. Heinz's
analogous condition for the scale-adaptive model gives $\kappa=0.41$ with
that model's standard settings (see [scale-adaptive simulation](/methods/scale-adaptive-simulation.md)).

**A stochastic derivation of the eddy viscosity.** Heinz derives the
algebraic Boussinesq stress from a Fokker–Planck model of the velocity
probability density: its simplest anisotropy balance gives
$R_{ij}=\tfrac23k\delta_{ij}-2\nu_t\langle S_{ij}\rangle$ with
$\nu_t=C_\mu k^2/\varepsilon$ and $C_\mu=2(1-c_0)/3$, where $0\le c_0\le1$ is
the diffusion parameter of the stochastic model (page-local, the source's
$c_0$), so that $C_\mu=0.09$ corresponds to $c_0=0.865$ *(compiler check,
not in the sources)*. The $k$ and $\varepsilon$ equations can also be
rewritten as BGK-type relaxations towards the equilibrium values
$k_{\mathrm{eq}}=kP_k/\varepsilon$ and $\varepsilon_{\mathrm{eq}}=P_k$, with
relaxation times $k/\varepsilon$ and $k/(C_{\varepsilon2}\varepsilon)$ and a
sink $(1-\alpha_\varepsilon^{-1})\varepsilon_{\mathrm{eq}}C_{\varepsilon2}\varepsilon/k$
in the $\varepsilon$ equation (§2.2–§2.3, Eqs. 2–7, 12, following Asinari et
al.); see the [Boussinesq page](/definitions/boussinesq-hypothesis.md).

**Eddy viscosity in compressible turbomachinery form.** Sandberg &
Michelassi (2022) list the model, with $\mu_t=0.09\langle\rho\rangle k^2/\varepsilon$
after Jones & Launder (1972), among the eddy-viscosity closures of
turbomachinery RANS, state that realizability conditions mitigate the
overproduction of $k$ at stagnation points (citing Durbin 1996), and list
the low-Reynolds models of Jones & Launder (1973) among transition
predictors whose wall damping has "no obvious relation to the transition
physics" ([Sandberg & Michelassi (2022)](/sources/sandberg-2022.md),
§2.2.2.1, §2.2.3, §3.3.1; see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)). Sandberg & Zhao (2022) list the same
eddy viscosity, and note that the gradient-diffusion heat flux written
with the $k$-$\omega$ constant, $\beta^*k^2/\varepsilon$, equals $\nu_t$
([Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md), §3.2, §4.2.1,
Eq. 9; see the [explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)).

**A resolution-dependent destruction coefficient.** In
[continuous eddy simulation](/methods/continuous-eddy-simulation.md) the
same model, with $C_{\varepsilon1}=1.44$, $C_{\varepsilon2}=1.92$,
$\sigma_\varepsilon=1.3$ and no $\sigma_k$ printed (the $k$-diffusion carries
$\nu_t$ alone), runs as a
hybrid RANS/LES model on the filtered velocity; the $\varepsilon$
destruction is written $C_{\varepsilon1}\alpha^*_\varepsilon\varepsilon^2/k$, with
$\alpha^*_\varepsilon$ (page-local) equal to $C_{\varepsilon2}/C_{\varepsilon1}=1.33$
in RANS and reduced towards one as the ratio of modelled to total length
scale falls ([Heinz (2022)](/sources/heinz-2022.md), §2, Eqs. 1–2,
Table 2). The time-scale form of the same coefficient, used in the
partially integrated transport model, is consistent only for homogeneous
flow when the transport terms carry the modelled viscosity, by Heinz's
argument (§2–§3). Heinz (2020) gives the variational origin of the
reduction, $\alpha^*_\varepsilon=1+L_+^2(\alpha_\varepsilon-1)$ with $L_+$ the
modelled-to-total length-scale ratio, under the assumptions stated on the
continuous-eddy-simulation page, and its $k$-equation (DES-like) variant
$\alpha^*_\varepsilon=1+\alpha_\varepsilon-\psi_\alpha$, with $\psi_\alpha$ the
multiplier of $\varepsilon$ in the $k$ equation (page-local) (§4.2–§4.3,
Eqs. 38–46).

**A length-scale equation in general form.** Wang et al. (2021) treat
$k$-$\varepsilon$ and $k$-$\omega$ as members of a family with length-scale
variable $\phi\propto k^m\varepsilon^n$ ($m=0$, $n=1$ for $k$-$\varepsilon$),
whose homogeneous-flow production and destruction coefficients are
$m+nC_{\varepsilon1}$ and $m+nC_{\varepsilon2}$, and derive from them the
detached-eddy constant of each branch
([Wang et al. (2021)](/sources/wang-2021-l.md), §2.3, Eqs. 11–12; see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)).

**Frozen baseline of a data-assimilated eddy viscosity.** Brenner et al.
(2022) print the same standard form (constants not printed) and use the
OpenFOAM `kEpsilon` model with a low-Reynolds wall function that sets
$\nu_t=0$ at the wall, solved once: its converged $\nu_t$ is frozen and
multiplied by a spatial field $\beta(\boldsymbol x)$ inferred by a discrete
adjoint from averaged LES velocity data
([Brenner et al. (2022)](/sources/brenner-2022.md), §2.1.1, §2.2, Eqs.
18–20, §3.1). On the periodic hill at $Re=10\,595$ ($180\times130$ cells,
first-cell $y^+\approx5$) the baseline departs from the LES most near the
walls and in the recirculation; with full-field velocity data the
corrected model matches the LES profiles except the velocity peaks near
the hill crest, but interior data alone do not improve the wall shear
stress, and adding wall data trades interior against wall agreement
(§3.4–3.6, Figs. 9, 16; see [field inversion](/methods/field-inversion-machine-learning.md)
and [periodic hill](/benchmarks/periodic-hill.md)).

**Host of a combustion model.** Mardani & Nazari (2022) run
two-dimensional axisymmetric Favre-averaged RANS of jet-in-hot-coflow
flames in MILD combustion with the standard model, its $C_{\varepsilon1}$
"modified … from 1.4 to 1.6" for the round jet (the standard value on this
page is 1.44) ([Mardani & Nazari (2022)](/sources/mardani-2022.md), §5). Their eddy-dissipation-concept closure is tied to the
turbulence model through its cascade constant: equating the cascade
eddy viscosity $\tfrac23C_{D1}k^2/\varepsilon$ to $C_\mu k^2/\varepsilon$ gives
$C_{D1}=1.5\,C_\mu=0.135$ (page-local $C_{D1}$), so the fine-structure
quantities depend on $C_\mu$ (§2, Eqs. 4–6), and the validity of the
default closure is stated in terms of the turbulence Reynolds number
$k^2/(\nu\varepsilon)$, above 20.8 and 64.31 for the fine-structure length and
time fractions (§4, Eqs. 18–20). Combustion lowers that Reynolds number
relative to the non-reacting jet, more strongly downstream, which the
authors describe as turbulence "relaminared" by combustion (§6.3, Fig.
7). Details on [flamelet-based tabulated chemistry](/methods/flamelet-tabulated-chemistry.md),
where the bundle's combustion closures are compared.

## The realizable model and a two-layer wall treatment

Delassaux et al. (2023) use the realizable $k$-$\varepsilon$ model of Shih et
al. in ANSYS Fluent as "the numerical reference for external flow
application" of their industrial partner
([Delassaux et al. (2023)](/sources/delassaux-2023.md), §4.1.1; HAL author
manuscript). They print no equation and describe two departures from the
standard model:

- a new dissipation-rate equation "based on the dynamic equation of the
  mean-square vorticity fluctuation for large Reynolds number";
- a realizable eddy-viscosity formulation "based on the positivity of
  square Reynolds stresses and Schwarz' inequality for turbulent shear
  stresses".

They couple it to Fluent's Enhanced Wall Treatment, a two-layer approach:
with the page-local wall-distance Reynolds number
$R_y=d\sqrt k/\nu$ (the source's $\rho y\sqrt k/\mu$, $y$ the wall distance
of the cell centre), the one-equation model of Wolfshtein supplies the eddy
viscosity where $R_y<200$ and the $k$-$\varepsilon$ formulation is used where
$R_y>200$ (§4.1.1). The same symbol $R_y=d\sqrt k/\nu$ enters the
transition-modified $F_1$ of the [SST page](/methods/k-omega-sst-model.md).
The authors state as a known drawback that the model underestimates the
turbulent kinetic energy in separated regions and therefore overestimates
the recirculation length "in most of the cases" (§4.1.1).

## Low-Reynolds and elliptic-relaxation relatives

- The [active model split](/methods/active-model-split.md) of Haering et al.
  (2022) needs a $k$-equation whose $k$ is the turbulent kinetic energy and
  uses the Chien low-Reynolds $k$-$\varepsilon$ model as one of its two base
  models, rejecting SST because its $k$ in attached boundary layers is "more
  akin to $\tfrac32v^2$" (§IV B, App. A).
- McConkey et al. (2022) build their learned anisotropy correction on the
  OpenFOAM $k$-$\varepsilon$-$\varphi$-$f$ elliptic-relaxation model, whose
  eddy viscosity is $C_\mu\varphi k\mathcal T$ with a time scale
  $\mathcal T=\max(k/\varepsilon,C_T\sqrt{\nu/\varepsilon})$ ($\varphi$,
  $\mathcal T$, $C_T$ page-local, the source's $T$; [McConkey et al. (2022)](/sources/mcconkey-2022.md), Eqs.
  10–16; see
  [periodic hill](/benchmarks/periodic-hill.md) and the
  [Boussinesq page](/definitions/boussinesq-hypothesis.md)).
- **Lag elliptic-blending model.** Mays et al. (2023) use the three-equation
  Lag elliptic-blending (EB) $k$-$\varepsilon$ model of Lardeau & Billard, as
  implemented in Simcenter STAR-CCM+, as the base of their hybrid RANS/LES and
  as their URANS comparator
  ([Mays et al. (2023)](/sources/mays-2023.md), §2.1.1, Eqs. 1–8, App. Eqs.
  16–21). With page-local symbols $\varphi_{\mathrm L}$ for the reduced stress
  function, $\alpha_{\mathrm{EB}}$ for the elliptic blending variable and
  $L=k^{3/2}/\varepsilon$ for the integral length, the eddy viscosity and the
  elliptic equation are
  $$\nu_t=C_\mu\varphi_{\mathrm L}\frac{k^2}{\varepsilon},\qquad
  \partial_j\big(L^2\partial_j\alpha_{\mathrm{EB}}\big)=\alpha_{\mathrm{EB}}-1,$$
  and $k$, $\varepsilon$ and $\varphi_{\mathrm L}$ are transported with the
  diffusivities $\nu/2+\nu_t/\sigma_k$, $\nu/2+\nu_t/\sigma_\varepsilon$,
  $\nu/2+\nu_t/\sigma_\varphi$ as printed (Eqs. 5–7). The reduced stress function
  "acts to reduce the viscosity usually over-predicted by failing to account
  for the lag between the stress and strain"; its equation is "reconstructed
  by analogy with a Reynolds Stress Model", which gives sensitivity to
  transition and non-linear effects, and its production (App. Eqs. 16–21)
  blends a near-wall and a homogeneous source with $\alpha_{\mathrm{EB}}^3$
  and contains the Reynolds-stress anisotropy of an algebraic relation and
  the Spalart–Shur rotation tensor (see the
  [Reynolds-stress page](/methods/reynolds-stress-model.md)). No constant is
  printed: they are "found in the STAR-CCM+ documentation". The authors chose
  it because their preliminary study found it the most appropriate available
  model for separated bluff-body flow (§2.1.1).
- **Myong–Kasagi with semi-local damping.** Diez Sanhueza et al. (2023) use
  the low-Reynolds Myong–Kasagi model in the form of Otero Rodriguez et al.,
  which replaces $y^+$ by the semi-locally scaled wall distance
  $y^*=y^+\sqrt{\langle\rho\rangle/\rho_w}\,\mu_w/\langle\mu\rangle$ in the damping functions,
  for fully developed channels with strong property variations
  ([Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md), §2.2, Eqs. 5–8).
  In the one-dimensional channel form, with $\mu_t$ the dynamic eddy
  viscosity and $Re_t=\rho k^2/(\mu\varepsilon)$ (page-local),
  $$\begin{aligned}
  0&=\mu_t\Big(\frac{\partial u}{\partial y}\Big)^2-\rho\varepsilon+\partial_y\Big[\Big(\mu+\frac{\mu_t}{\sigma_k}\Big)\partial_yk\Big],\\
  0&=C_{\varepsilon1}P_k\frac{\varepsilon}{k}-C_{\varepsilon2}f_\varepsilon\rho\frac{\varepsilon^2}{k}+\partial_y\Big[\Big(\mu+\frac{\mu_t}{\sigma_\varepsilon}\Big)\partial_y\varepsilon\Big],\\
  f_\varepsilon&=\Big(1-\tfrac29e^{-(Re_t/6)^2}\Big)\big(1-e^{-y^*/5}\big)^2,\qquad
  f_\mu=\big(1-e^{-y^*/70}\big)\Big(1+\frac{3.45}{\sqrt{Re_t}}\Big),\qquad
  \mu_t=C_\mu f_\mu\rho\frac{k^2}{\varepsilon},
  \end{aligned}$$
  with $C_{\varepsilon1}=1.4$, $C_{\varepsilon2}=1.8$, $C_\mu=0.09$,
  $\sigma_k=1.4$, $\sigma_\varepsilon=1.3$ and $Pr_t=1$. The original model,
  they state, uses $y^+$ in the damping functions, replaced here by $y^*$
  (§2.2). The integrated-gradients ranking places the same semi-local $y^*$
  above $\langle\rho\rangle/\rho_w$ and $\langle\mu\rangle/\mu_w$ as an input of their
  learned correction (§5, §6; see
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md)).
- Inside SST the outer branch is a $k$-$\varepsilon$ model written in
  $\omega$; its detached-eddy constant is $C_{\mathrm{DES}}=0.61$ against
  0.78 for the inner branch, blended through $F_1$ (Delassaux et al. 2023,
  §4.1.3, Eq. 9; Carlsson et al. 2023, §4.2; see
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

## Evidence

**Bluff-body wakes.** On the 25° Ahmed body Delassaux et al. recall from
their earlier calibration that the realizable model gives no separation on
the slant, SST a massive one, and only the scale-resolving models the
separation and reattachment (§5; see [Ahmed body](/benchmarks/ahmed-body.md)).
On a full-scale estate car (Peugeot 308 SW, $Re_L=1.3\times10^7$ on the car
length, 115 million cells, 20 prism layers at $y^+\approx1$) they compare it
with SST and SST-based delayed DES against wind-tunnel data (§6–§7):

- drag coefficient 0.242 against 0.244 measured, the same as SST, and
  insensitive to 30 prism layers (0.242) and to a refined wake grid (0.243)
  (Table 3); the authors attribute this agreement to error cancellation,
  the cumulative drag of this model and of DDES differing at the front
  fairings and at the rear (§6, Fig. 13);
- in the symmetry-plane wake a high-speed jet from the underbody reaches far
  into the wake, absent in the experiment; the recirculation is
  overpredicted, less than with SST but more than with DDES (§7.2, Figs.
  17–18);
- in the upper wake plane the streamwise velocity is predicted better than
  by both SST models (§7.2, Fig. 19);
- on rounded separation lines it overpredicts the pressure coefficient where
  SST is closest to the measurements (§7.3, Fig. 20), and behind the rear
  fairing it gives a recirculation larger than measured (§7.4, Fig. 23).

**Separated channel flows.** On the parametrized periodic hills of Xiao et
al. ($Re=5600$ on the hill height, steepness factors 0.5, 0.8, 1.0) and the
backward-facing step at $Re=5000$, Tang et al. (2023) find that the standard
model underestimates the separation bubble on the training hill; it
predicts the shear component of the anisotropy reasonably but the normal
components "far removed" from DNS, especially near the bottom wall, and its
anisotropy lies close to the plane-strain line of the barycentric map at
all stations (§III C, Figs. 7–9; see [periodic hill](/benchmarks/periodic-hill.md)
and [backward-facing step](/benchmarks/backward-facing-step.md)). Morsbach et
al. (2024) and Agrawal & Koutsourelakis (2024) state that a linear model ties
the anisotropy to the strain (see the Boussinesq page); the non-linear correction Tang et al. learn on top
of it is described on the [Boussinesq page](/definitions/boussinesq-hypothesis.md)
and on [symbolic-regression closures](/methods/symbolic-regression-closure.md).
They report that a converged RANS with the learned correction costs
"basically the same" as the baseline (§III A).

**Low-Reynolds backward-facing step.** Agrawal & Koutsourelakis (2024) use
the standard model (OpenFOAM simpleFoam, 35,709 degrees of freedom, $k$ and
$\varepsilon$ "obtained by solving the respective standard transport
equations") as the baseline of their probabilistic learned closure on a
two-dimensional step of expansion ratio 2 at $Re=500$ on the step height
and inlet bulk velocity
([Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md), §3.2, §3.4,
App. A; arXiv v2). Against a spanwise-periodic WALE LES, the baseline
"underestimates the size of the first recirculation zone and almost
completely misses the second one", gives a reattachment length of
$5.61h$ against $9.10h$, and "severely under/over-estimates" the magnitude
of the Reynolds stress and "misrepresents its spatial variability" (§3.4,
Figs. 7–8, Table 5). The authors recall that their tensor-basis closure
reduces to this model for $g^{(1)}=-0.09$ and all other coefficients zero
(§2.2.1, Eq. 15); with the Boussinesq closure and $\nu_t=C_\mu k^2/\varepsilon$
the coefficient of $T^{(1)}=\mathsf S$ in the registry's $b_{ij}$ is
$-C_\mu=-0.09$ *(compiler check, not in the sources)*; see the
[tensor-basis neural network](/methods/tensor-basis-neural-network.md),
[model-form uncertainty](/definitions/model-form-uncertainty.md) and
[backward-facing step](/benchmarks/backward-facing-step.md).

**Drag crisis of a circular cylinder.** URANS with the Lag EB model fails
to capture the drag crisis of a smooth cylinder: on meshes of 7.65–16.64
million cells with first-cell $y^+<1$, it gives $C_D=0.436$, 0.354, 0.204 and
0.156 at $Re_D=2.5$, 3.8, 5.3 and $7.2\times10^5$, against 0.833, 0.481, 0.296
and 0.213 from the reference wall-resolved LES, and recirculation lengths
of 1.107–1.339$D$ against 0.559–0.727$D$ (Mays et al. 2023, §3.2.1, Tables
4–5, Fig. 6). The authors attribute the failure to an over-predicted eddy
viscosity in the shear layers, which keeps them stable, consistent with
earlier linear-eddy-viscosity URANS they cite; the URANS eddy viscosity is
"typically on the order of ten times greater at least" than the maximum
subgrid viscosity ratio of their hybrid, 9.4–18.3 (§3.2.2, Table 6). URANS
still partly captures the laminar separation bubble, through a slight
inflection near separation and a non-zero mean lift (§3.2.1; see
[laminar separation bubble](/definitions/laminar-separation-bubble.md),
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

**Variable-property channels.** Fed with the DNS density and viscosity
profiles, the semi-local Myong–Kasagi model deviates strongly in channels
with strong property variations: over a database of 16 heated low-Mach,
nine supersonic ideal-gas (Mach 0.7–4) and five incompressible channels,
the $L^\infty$ error of the mean velocity reaches 23.4% in the hardest
low-Mach case (JFM.CRe$^\star_\tau$), 11.6% at Mach 4 and 2.3–3.0% in the
incompressible cases (Diez Sanhueza et al. 2023, §2.2, Fig. 1, Table 3).
Field-inversion multipliers on the dissipation terms of both equations and
a neural network that predicts the correction of the $k$ equation reduce the
error in almost all held-out cases, to 4.0% in that case, with one
extrapolation failure at $Re_\tau=4200$ (2.3% to 14.0%) (§5, Table 3; details
on [field inversion and machine learning](/methods/field-inversion-machine-learning.md)
and [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).

**Lattice Boltzmann hosts.** Mozaffari et al. (2024) recall
$k$-$\varepsilon$ implementations in lattice Boltzmann solvers, including
a $k$-$\varepsilon$-based hybrid RANS/LES of Sajjadi et al., as the
precedent of their SST implementation in a standard lattice Boltzmann
code ([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §1; HAL accepted
manuscript; see [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)).
Husson et al. (2024) name the very-large-eddy-simulation model of the
commercial lattice Boltzmann code PowerFLOW, which is based on the RNG
$k$-$\varepsilon$ model, as a hybrid whose RANS/LES switching criterion is
not disclosed in the open literature; they build their own lattice
Boltzmann hybrid on the Spalart–Allmaras-based zonal DES instead
([Husson et al. (2024)](/sources/husson-2024.md), §1; see
[detached-eddy simulation](/methods/detached-eddy-simulation.md)).

**Particle-laden channel.** Idelsohn et al. (2024) include an unsteady
RANS with the standard model and standard wall functions, "but no
additional term for turbulence modulation", among the solutions of a
particle-laden duct flow at $Re=57\,000$ (200 μm particles, volume fraction
$5\times10^{-4}$, no gravity), beside DNS, a static-Smagorinsky LES and
their pseudo-direct numerical simulation on $36\times12\times12$ cells
([Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §3.2.2, Fig. 28). The
DNS shows the mean kinetic energy of the carrier phase rising with the
particle load and the mean profile changing; the URANS shows "negligible
differences between the laden and unladen results", which the authors read
as "ensemble averaged solutions cannot predict turbulence modulation". In
§3.1 the authors state, citing earlier work, that energy-based modulation
sources depending only on the Stokes number predict non-realistic rates (see
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md)).

## Qualifications

- Delassaux et al. print neither the realizable model nor the Wolfshtein
  length scales; the statements above are their description.
- Tang et al. attribute the constants to Launder & Sharma while printing the
  model without the damping functions of a low-Reynolds form (§II A); the
  page records the form as printed.
- Delassaux et al. call the drag agreement of both RANS models fortuitous:
  "There is no valid reason that RANS predicts a more accurate $C_d$ than
  DDES" (§6), and do not take the agreement as evidence for the model; see
  [model-form uncertainty](/definitions/model-form-uncertainty.md).
- Mardani & Nazari (2022) define the turbulence Reynolds number as
  $k^2/(\nu\varepsilon)$ (Eqs. 11, 18, 34) and, before Eq. 27, as $\nu_t/\nu$;
  with $\nu_t=C_\mu k^2/\varepsilon$ the two differ by the factor $C_\mu=0.09$
  *(compiler check, not in the sources)*. The derivation of their local
  constants (Eqs. 27–33) uses the second, the evaluation (Eq. 34) the
  first.
- Brenner et al. (2022) do not print the model constants.
- Mays et al. (2023) print the Boussinesq closure of their base model as
  $T_{ij}=2\nu_t\langle S_{ij}\rangle-\tfrac13k\delta_{ij}$ (Eq. 3, $T_{ij}$ the
  negative kinematic Reynolds stress); with $\langle S_{ii}\rangle=0$ from their
  continuity equation (Eq. 1) the trace is $-k$, whereas a stress of trace
  $-2k$ needs $\tfrac23k\delta_{ij}$ *(compiler check, not in the sources)*.
  They print the production as $P_k=\nu_tS^2$ in §2.1.1 and as $2\mu_tS^2$ in
  the subfilter $k$ equation (Eq. 9), without defining the modulus $S$; the
  page records both as printed.
- Diez Sanhueza et al. (2023) give the baseline error of the hardest case as
  22.8% in §2.2 and 23.4% in Table 3, the abstract and §6, without stating two
  error definitions.

# Citations

- [Tang et al. (2023)](/sources/tang-2023.md) — §II A Eqs. 3–8, §III A, §III C Figs. 7–9 (arXiv v1).
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.1, §4.1.3 Eq. 9, §5, §6 Table 3 Fig. 13, §7.2–7.4 Figs. 17–20, 23 (HAL author manuscript).
- [Haering et al. (2022)](/sources/haering-2022.md) — §II D Eqs. 1–2, §IV B, App. A.
- [McConkey et al. (2022)](/sources/mcconkey-2022.md) — Eqs. 10–16 (arXiv v1).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.2.
- [Agrawal & Koutsourelakis (2024)](/sources/agrawal-2024.md) — §2.2.1 Eq. 15, §3.2, §3.4 Figs. 7–8 Table 5, App. A (arXiv v2).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §1 (HAL accepted manuscript).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1.
- [Heinz (2022)](/sources/heinz-2022.md) — §2 Eqs. 1–2, Table 2, §3.
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.3 Eqs. 11–12.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §1.
- [Husson et al. (2024)](/sources/husson-2024.md) — §1.
- [Heinz (2020)](/sources/heinz-2020.md) — §2.2–§2.3 Eqs. 2–12, §4.2–§4.3 Eqs. 38–46.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.1, §2.2.3, §3.3.1.
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §2.1.1, §2.2 Eqs. 18–20, §3.1, §3.4–3.6 Figs. 9, 16.
- [Mardani & Nazari (2022)](/sources/mardani-2022.md) — §2 Eqs. 4–6, §4 Eqs. 18–20, 27–34, §5, §6.3 Fig. 7.
- [Sandberg & Zhao (2022)](/sources/sandberg-2022-b.md) — §3.2, §4.2.1 Eq. 9.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §3.1, §3.2.2, Fig. 28.
- [Mays et al. (2023)](/sources/mays-2023.md) — §2.1.1 Eqs. 1–8, App. Eqs. 16–21, §3.2.1–§3.2.2 Tables 4–6, Fig. 6.
- [Diez Sanhueza et al. (2023)](/sources/sanhueza-2023.md) — §2.2 Eqs. 5–8, Fig. 1, §5 Table 3, §6.
