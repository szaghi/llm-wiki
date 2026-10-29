---
type: Method
title: "k-ε models"
description: "Two-equation RANS eddy-viscosity models transporting the turbulent kinetic energy and its dissipation rate: the standard form of Launder and Spalding with its constants, log-law calibration and round-jet correction, the Jones–Launder low-Reynolds form, realizable and elliptic-relaxation relatives, and evidence on adverse pressure gradients, bluff-body wakes, periodic hills and learned corrections."
status: established
aliases: [k-epsilon, standard k-ε, Launder–Spalding k-ε, Launder–Sharma k-ε, Jones–Launder k-ε, JL k-ε, realizable k-ε, RKE, Shih k-ε, enhanced wall treatment, EWT, two-layer k-ε]
tags: [rans, eddy-viscosity, separated-flow, boundary-layer]
timestamp: 2026-10-29T16:21:00Z
---

# k-ε models

The $k$-$\varepsilon$ models close the RANS equations with a
[Boussinesq](/definitions/boussinesq-hypothesis.md) eddy viscosity built from
two transported quantities, the turbulent kinetic energy $k$ and its
dissipation rate $\varepsilon$:

$$\nu_t=C_\mu\frac{k^2}{\varepsilon}.$$

The family includes the standard high-Reynolds-number model, low-Reynolds
forms with near-wall damping, the realizable model of Shih et al., and
elliptic-relaxation descendants. The standard model with its constants
and its wall functions is the one Launder & Spalding (1974) recommend as
the best compromise between economy, range of applicability and physical
realism: "the simplest kind of model that permits prediction of both
near-wall and free-shear-flow phenomena without adjustments to constants or
functions" ([Launder & Spalding (1974)](/sources/launder-1974.md), §1.2,
§2.2, §4). In this bundle the standard model is the
baseline of a learned non-linear correction (Tang et al. 2023), the
realizable model is the industrial reference of an automotive study
(Delassaux et al. 2023), and the $k$-$\varepsilon$ branch is the outer
formulation of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md).

## The standard model

**The founding form.** Launder & Spalding (1974) print the high-Reynolds-number
model as the recommendation of the Imperial College group, its
$\varepsilon$ equation "first developed and used in the Imperial College
group by Hanjalić" and its constants taken from Launder et al. (1972) (both
as cited) ([Launder & Spalding (1974)](/sources/launder-1974.md), §2.2,
Eqs. 2.2-1–2.2-3, Table 2.1). In registry notation, for constant density
and with $D/Dt=\partial_t+\langle u_j\rangle\partial_j$,

$$\begin{aligned}
\frac{Dk}{Dt}&=\partial_j\Big[\frac{\nu_t}{\sigma_k}\partial_jk\Big]+\nu_t\big(\partial_j\langle u_i\rangle+\partial_i\langle u_j\rangle\big)\partial_j\langle u_i\rangle-\varepsilon,\\
\frac{D\varepsilon}{Dt}&=\partial_j\Big[\frac{\nu_t}{\sigma_\varepsilon}\partial_j\varepsilon\Big]+C_{\varepsilon1}\frac{\varepsilon}{k}\nu_t\big(\partial_j\langle u_i\rangle+\partial_i\langle u_j\rangle\big)\partial_j\langle u_i\rangle-C_{\varepsilon2}\frac{\varepsilon^2}{k},\\
\nu_t&=C_\mu\frac{k^2}{\varepsilon},
\end{aligned}$$

with the constants of the table below ($C_\mu=0.09$, $C_{\varepsilon1}=1.44$,
$C_{\varepsilon2}=1.92$, $\sigma_k=1.0$, $\sigma_\varepsilon=1.3$; the source's
$C_1$, $C_2$). The authors call these values appropriate to plane jets and
mixing layers and expect them to be equally satisfactory near walls
(§2.2). The production term equals $2\nu_t\langle S_{ij}\rangle\langle S_{ij}\rangle$, the
$P_k$ of the Boussinesq closure in incompressible flow *(compiler check, not
in the sources)*. The high-Reynolds form carries no molecular diffusion:
the molecular viscosity enters only the low-Reynolds form of the same paper
(§2.3-2, below). Launder & Spalding define the dissipation rate as
$\varepsilon=\nu\langle\partial_ku_i'\,\partial_ku_i'\rangle$ (Eq. 2.1-4), whereas the registry
writes $2\nu\langle s_{ij}s_{ij}\rangle$; for divergence-free fluctuations the two differ by
$\nu\,\partial_i\partial_jR_{ij}$, which vanishes in homogeneous turbulence
*(compiler check, not in the sources)*. Their §2.1 also defines a length
scale $L=c_lk^{3/2}/\varepsilon$ with a constant $c_l$ (page-local, the
source's $C_D$, not the drag coefficient; value not printed), while §2.3
uses $L=k^{3/2}/\varepsilon$.

**Why $\varepsilon$.** Launder & Spalding (§2.1) argue that the alternative
second variables $kL$ and the time$^{-2}$ variable $k/L^2$ (interpreted as a
mean-square vorticity fluctuation, after Spalding and Saffman as cited) are
formally interconvertible with $\varepsilon=k^{3/2}/L$ (Eqs. 2.1-5, 2.1-6),
but a gradient-diffusion model of the third-order correlations is not
invariant under the change of variable. In a constant-stress near-wall
layer with uniform $k$ and $L\propto y$, the equation of a generic variable
$k^m/L^n$ reduces to (Eqs. 2.1-10–2.1-13)

$$\frac{n^2}{\sigma_t}+\frac{C_1C_\mu^{1/2}}{\kappa^2}-\frac{C_2C_\mu^{1/2}}{\kappa^2}=0,$$

with $\sigma_t$ the Prandtl number of the variable and $C_1$, $C_2$ its
production and destruction constants, which depend on $m$ and $n$
(page-local; $C_{\varepsilon1}$, $C_{\varepsilon2}$ for $n=1$). With "the proper
values" of the constants it gives $\sigma_t=-0.8$ for $kL$ ($n=-1$), $2.9$
for $k/L^2$ ($n=2$) and $1.3$ for $\varepsilon$ ($n=1$); only the last fits
the spreading of free shear flows, so only the $k$-$\varepsilon$ model avoids
making a "constant" depend on $y/L$ (§2.1; the values of $\kappa$ and of the
$m,n$-dependent constants are not printed). For $n=1$ the relation is the
log-law condition of Heinz (2020) below *(compiler check, not in the
sources)*. In the round jet no single set
of constants fits together with plane free shear flows and wall flows;
Launder & Spalding recommend Rodi's modification (as cited)

$$C_\mu=0.09-0.04f,\qquad C_{\varepsilon2}=1.92-0.0667f,\qquad f=\Big|\frac{Y}{2\Delta U}\Big(\frac{dU_{cl}}{dx}-\Big|\frac{dU_{cl}}{dx}\Big|\Big)\Big|^{0.2},$$

with $U_{cl}$ the axis velocity, $Y$ the width of the mixing region and
$\Delta U$ the velocity difference across it (page-local), which makes $f$
vanish in wakes, and add that "little universality can truly be claimed
for it" (§2.2, Eqs. 2.2-4–2.2-6; see
[turbulent round jet](/benchmarks/turbulent-round-jet.md)). In weak-shear
flows with production well below dissipation (far wakes) $C_\mu$ assumes
higher values; near walls production is always large, so the table values
are "nearly always applicable" for engineering flows (§2.2).

**Breadth claimed in 1974.** Launder & Spalding (§3) show nine flows
computed by their group (figures only): in a plane jet in a moving stream
the $k$-$\varepsilon$ model follows the data where the mixing-length and the
one-equation ($k$ only) models fail beyond the potential core, "the
two-equation level is the simplest at which universality is secured for
both jet and mixing layer" (§3.1, Fig. 3.1); on wall jets over cones of
$11^\circ$ and $90^\circ$ half-angle it predicts the decay of the maximum
velocity where a plane-calibrated mixing length underestimates it (§3.2);
confined coaxial jets and a ventilated room are reproduced with wall
functions (§3.6–§3.7); a tube with a twisted tape insert agrees "not so
good", which the authors attribute mainly to strongly anisotropic turbulent
viscosity (§3.8); and in a square duct the isotropic eddy viscosity gives
no motion in the cross-sectional plane, whereas an algebraic stress model
predicts the secondary flow (§3.9; see the
[explicit algebraic Reynolds-stress model](/methods/explicit-algebraic-reynolds-stress-model.md)
and the [Boussinesq page](/definitions/boussinesq-hypothesis.md)). On a
film-cooling wall jet behind a thick lip the wall-function value of
$\varepsilon$ had to be reduced by a factor of 20 on the downstream faces of
the step and lip (§3.5; see [RANS wall functions](/methods/rans-wall-function.md)).

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

**Near-wall integration.** Launder & Spalding (1974, §2.3) present two
near-wall treatments side by side: wall functions, which economize
computer time and storage and require the first node to satisfy
$(k^{1/2}L/\nu)_P\gg1$ (see [RANS wall functions](/methods/rans-wall-function.md)),
and the low-Reynolds-number model of Jones & Launder (as cited) integrated
to the wall, described below; the low-Reynolds model needs "nearly 100
cross-stream grid points for computational accuracy within 1% (about four
times as many as when the wall-function method is used)" (§3.3). Elzaabalawy et al. (2023, §1) state that
wall-resolved versions of the model need ad hoc damping functions near the
wall "that increase the stiffness of the model and can present problems",
so that wall functions are usually employed with $k$-$\varepsilon$, whereas
the $k$-$\omega$ model integrates to the wall without damping functions but
with $\omega\to\infty$ there
([Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md), §1; see the
[Wilcox $k$-$\omega$ page](/methods/k-omega-model.md) and
[RANS wall functions](/methods/rans-wall-function.md)). Tomboulides et al.
(2025) make the same comparison from the side of a high-order
spectral-element code: they state (§1) that the $k$-$\varepsilon$ model needs
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
$0.1872$, $\kappa=0.433$ *(compiler check, not in the sources)*. The
same condition is the $n=1$ case of Launder & Spalding's near-wall
constraint above (Eq. 2.1-11) *(compiler check, not in the sources)*, from
which they obtain $\sigma_\varepsilon=1.3$ without printing $\kappa$ (§2.1). Heinz's
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

- **Jones–Launder.** Launder & Spalding (1974) print the low-Reynolds form
  of Jones & Launder (as cited), integrated to the wall
  ([Launder & Spalding (1974)](/sources/launder-1974.md), §2.3-2, Eqs.
  2.3-4–2.3-7). In registry notation, for constant density and with
  $Re_t=k^2/(\nu\varepsilon)$ (page-local, the source's $R_t$),
  $$\begin{aligned}
  \frac{Dk}{Dt}&=\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_k}\Big)\partial_jk\Big]+\nu_t\,\partial_j\langle u_i\rangle\big(\partial_j\langle u_i\rangle+\partial_i\langle u_j\rangle\big)-2\nu\big(\partial_jk^{1/2}\big)^2-\varepsilon,\\
  \frac{D\varepsilon}{Dt}&=\partial_j\Big[\Big(\nu+\frac{\nu_t}{\sigma_\varepsilon}\Big)\partial_j\varepsilon\Big]+C_{\varepsilon1}\frac{\varepsilon}{k}\nu_t\,\partial_j\langle u_i\rangle\big(\partial_j\langle u_i\rangle+\partial_i\langle u_j\rangle\big)-C_{\varepsilon2}\frac{\varepsilon^2}{k}-2.0\,\nu\nu_t\big(\partial_j\partial_l\langle u_i\rangle\big)^2,\\
  C_\mu&=0.09\exp\Big[\frac{-2.5}{1+Re_t/50}\Big],\qquad C_{\varepsilon2}=1.92\big[1-0.3\exp(-Re_t^2)\big],
  \end{aligned}$$
  with $C_{\varepsilon1}$, $\sigma_k$, $\sigma_\varepsilon$ at their high-Reynolds
  values and $\varepsilon=0$ at the wall. The term $-2\nu(\partial_jk^{1/2})^2$,
  equal to the dissipation rate near the wall, is added "for computational
  rather than physical reasons" so that $\varepsilon=0$ can be imposed; a
  zero-gradient condition on $\varepsilon$ did not admit a compatible set of
  Reynolds-number functions; the last term of the $\varepsilon$ equation is
  included "to produce satisfactory variation of $k$ with distance from the
  wall" (§2.3-2). Jones & Launder used $C_{\varepsilon1}=1.55$ and
  $C_{\varepsilon2}=2.0$; Launder & Spalding state that in wall flows only
  $C_{\varepsilon2}-C_{\varepsilon1}$ matters to first order and is "very nearly
  the same", so the standard constants give only slightly different
  predictions (footnote, p. 278). With it, the friction-factor predictions
  of pipe flow are "excellent" down to the onset of intermittency and the
  departure of the $Re=6000$ velocity profile from the high-Reynolds log
  law is reproduced, where Reynolds-independent near-wall formulae tuned for
  $Re>20\,000$ overpredict $C_f$ (§3.3, Figs. 3.3a,b); on the pressure surface
  of a turbine blade at three free-stream turbulence levels it reproduces
  the measured heat transfer without a prescribed transition point: the
  model "has its own built-in 'transition criterion'" (§3.4, Fig. 3.4). Menter
  (1994) uses the same Jones–Launder model as the $k$-$\varepsilon$ comparator
  of the SST paper (see **Adverse pressure gradients** below).
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
- **Written in $\omega$.** Menter (1994) transforms the standard
  high-Reynolds model into $k$-$\omega$ variables to build the outer layer
  of the BSL and SST models: the $\omega$ equation acquires the
  cross-diffusion term $2\sigma_{\omega2}\omega^{-1}\partial_jk\,\partial_j\omega$
  and the constants $\sigma_{k2}=1.0$, $\sigma_{\omega2}=0.856$,
  $\beta_{\omega2}=0.0828$, $\beta^*=0.09$, $\kappa=0.41$,
  $\gamma_{\omega2}=\beta_{\omega2}/\beta^*-\sigma_{\omega2}\kappa^2/\sqrt{\beta^*}$; "a
  small additional diffusion term is neglected in the transformation", with
  virtually no effect on the solutions according to Menter's Ref. 9 (as
  cited) ([Menter (1994)](/sources/menter-1994-b.md), Eqs. 3–4, App. Eq. A5;
  see the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)). From the
  printed constants, $\beta_{\omega2}/\beta^*=0.92=C_{\varepsilon2}-1$ and
  $\gamma_{\omega2}=0.440=C_{\varepsilon1}-1$, while $1/\sigma_{\omega2}=1.17$ is
  the $\sigma_\varepsilon$ that the log-law condition above (Launder &
  Spalding Eq. 2.1-11 with $n=1$; Heinz 2020, §2.3) gives with the table's
  $C_\mu$, $C_{\varepsilon1}$, $C_{\varepsilon2}$ and $\kappa=0.41$, not the
  1.3 of Launder & Spalding's table *(compiler check, not in the sources)*. Menter also states that changing the first
  blending argument to $\min\big(500\nu/(d^2\omega),\,4\sigma_{\omega2}k/(CD_{k\omega}d^2)\big)$
  ($d$ the wall distance, $CD_{k\omega}$ the positive part of the
  cross-diffusion term as on the SST page) gives a two-layer $k$-$\varepsilon$ model with the $k$-$\omega$ model in the
  sublayer, analogous to Rodi's two-layer model (as cited) but blending
  without user input; "The modification ensures that $F_1$ is zero for
  $y^+>70$" (Eq. 13). In free shear layers BSL and SST reduce to the same
  model, "virtually identical" to the standard $k$-$\varepsilon$ model (p. 1601,
  results in Menter's Ref. 9).
- Inside SST the outer branch is a $k$-$\varepsilon$ model written in
  $\omega$; its detached-eddy constant is $C_{\mathrm{DES}}=0.61$ against
  0.78 for the inner branch, blended through $F_1$ (Delassaux et al. 2023,
  §4.1.3, Eq. 9; Carlsson et al. 2023, §4.2; see
  [detached-eddy simulation](/methods/detached-eddy-simulation.md)).

## Evidence

**Adverse pressure gradients.** Menter (1994) compares the Jones–Launder
model with the Wilcox, BSL and SST $k$-$\omega$ models
([Menter (1994)](/sources/menter-1994-b.md), pp. 1601–1603). On the
Samuel–Joubert boundary layer it gives too high a skin friction while the
three $k$-$\omega$ models reproduce the data (results in Menter's Ref. 9, as
cited); in Driver's separated axisymmetric flow it stays firmly attached,
predicts a significantly higher shear stress approaching separation, and
its maximum eddy viscosity $\nu_{t,\max}/(u_e\delta^*)$ falls only barely below
Clauser's 0.0168 (Figs. 2–6; $u_e$ the edge velocity, page-local); on the
Driver–Seegmiller backward-facing step ($120\times120$ grid, with $90\times90$
and $240\times240$ virtually identical) its reattachment length is 5.5 step
heights against about 6.4 measured and 6.5, 5.9 and 6.4 for SST, BSL and
Wilcox $k$-$\omega$, "better than previously reported" thanks to the fine grid,
but its skin-friction variations are too large (Figs. 7–8; see
[backward-facing step](/benchmarks/backward-facing-step.md)); on the NACA
4412 airfoil at $13.87^\circ$ the original $k$-$\omega$ model lies even further
from the experiment than this model, which Menter attributes to the
freestream dependency of $k$-$\omega$ (Fig. 9; see
[NACA 4412](/benchmarks/naca-4412-airfoil.md)). Menter states that the
$k$-$\varepsilon$ model does not suffer from that freestream sensitivity, that
$k$-$\omega$ is superior to it in the log region of equilibrium
adverse-pressure-gradient and compressible flows (citing Wilcox and others),
and that the specific form of the $k$-$\varepsilon$ damping functions has
little to no effect on the velocity profiles and skin friction of
high-Reynolds-number flows (citing two earlier studies) (pp. 1598–1599; see
the [Wilcox $k$-$\omega$ page](/methods/k-omega-model.md) and
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md)).

**Bluff-body wakes.** On the 25° Ahmed body Delassaux et al. (§5) cite
their earlier calibration, in which the realizable model gives no separation on
the slant, SST a massive one, and only the scale-resolving models capture the
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
Figs. 7–8, Table 5). The authors state that their tensor-basis closure
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

**Lattice Boltzmann hosts.** Mozaffari et al. (2024, §1) cite
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

**Shock/boundary-layer interaction, a priori.** On their DNS of Mach 5
oblique-shock/boundary-layer interactions (wedges of $14^\circ$, $10^\circ$,
$6^\circ$, run with [STREAmS](/software/streams.md)), Yu et al. (2023b)
evaluate the two-equation estimate $\mu_t=C_\mu\langle\rho\rangle k^2/\varepsilon$
with $C_\mu=0.09$ against the best-fit eddy viscosity of the DNS stresses
([Yu et al. (2023b)](/sources/yu-2023-b.md), §IV, Eq. 20, Fig. 18a). It
matches upstream but "severely" overestimates the eddy viscosity downstream
of the interaction (at $y/\delta_r=0.5$ in the strongest case), as Morgan et
al. (2013) also found (as cited). A wall-pressure-dependent coefficient

$$C_\mu(x)=\frac{0.09}{1+C_{\mu,1}\big(\langle p_w\rangle(x)/\langle p_w\rangle_r-1\big)},\qquad C_{\mu,1}=1,$$

($C_{\mu,1}$ page-local, fitted to the DNS; $\langle p_w\rangle_r$ the wall
pressure at the reference station) restores the downstream eddy viscosity
and the reconstructed shear stress except where separation begins (Eq. 21,
Figs. 18b, 19). The authors transfer it to the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) as a variable
$\beta^*$, which they call equivalent to $C_\mu$ (§V); the a posteriori
results are on that page and on
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**A heuristic for the RANS/LES interface.** Wang et al. (2024c) cite the
model's eddy viscosity $\mu_t=C_\mu\langle\rho\rangle k^2/\varepsilon$
($C_\mu=0.09$) in a wall-resolved LES of a Mach 2 flat-plate boundary
layer: the resolved dissipation falls rapidly above $y^+\approx14$ on all
three grids while the kinetic energy peaks near there, so $y^+\approx14$
"corresponds to the critical location of modeled Reynolds stresses" and
"may be the appropriate RANS/LES interface" of a scale-adaptive hybrid
([Wang et al. (2024c)](/sources/wang-2024-j.md), §III.E, Figs. 12–14; the
paper runs no RANS computation; see
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

**Vortex flows.** In the CAWAPI campaign on the F-16XL, as surveyed by
Luckring & Rizzi (2024), the second phase improved the prediction of the
secondary vortex by switching from Spalart–Allmaras to a $k$-$\varepsilon$
model together with grid refinement (Elmiligui et al., as cited); the
authors argue that SA "fails to predict secondary separation because it
does not transport the right quantities"
([Luckring & Rizzi (2024)](/sources/luckring-2024.md), §3.2.3.3; see
[delta-wing vortex flow](/benchmarks/delta-wing-vortex-flow.md) and the
[Spalart–Allmaras page](/methods/spalart-allmaras-model.md)).

**Baseline of learned and physics-informed models.** Fang et al. (2026), a
review, quote an LSTM trained on channel DNS at "Re = 180" whose
centre-region shear-stress error is "less than 5%" against "about 12%" for
the "traditional" $k$-$\varepsilon$ model (Pasinato et al., as cited), and a
physics-informed network with the standard model embedded that reconstructs
a backward-facing step at a Reynolds number of 5100 from sparse data (Pioch
et al., as cited) ([Fang et al. (2026)](/sources/fang-2026.md), §3.4, Table
3, §4.2.2; the review reports no out-of-sample test of the LSTM; see
[physics-informed neural networks](/methods/physics-informed-neural-network.md)).
Le et al. (2024) list Bayesian calibrations of $k$-$\varepsilon$ coefficients
among the parametric uncertainty studies they review, without coefficient
values ([Le et al. (2024)](/sources/le-2024.md), §3.1.1; see
[Bayesian closure calibration](/methods/bayesian-closure-calibration.md)).

**Combustion closures.** In the RANS form of conditional source-term
estimation the scalar-dissipation relaxation time is the model's $k/\varepsilon$
(Favre-averaged), and RANS $k$-$\varepsilon$ hosts the sooting-flame and
CSE–CMC comparison studies that Salehi et al. (2024) review
([Salehi et al. (2024)](/sources/salehi-2024.md), Eq. 21 and text, §3.1;
see [conditional source-term estimation](/methods/conditional-source-term-estimation.md)).

## Qualifications

- Yu et al. (2023b) justify $\langle p_w\rangle$ as the variable of their
  $C_\mu(x)$ "by simple reasoning and data fitting" (§IV) and note that model
  constants such as $C_{\mu,1}$ in RANS can differ from DNS-fitted values
  (§V).
- Delassaux et al. print neither the realizable model nor the Wolfshtein
  length scales; the statements above are their description.
- Tang et al. attribute the constants to Launder & Sharma while printing the
  model without the damping functions of a low-Reynolds form (§II A); the
  page records the form as printed. Launder & Spalding (1974, Table 2.1)
  print the same five values and attribute them to Launder et al. (1972, as
  cited); Menter (1994, Eqs. 3–4 and text) codes the standard model after
  Launder & Sharma (Menter's Ref. 15, a work distinct from Launder & Spalding). Tang et al.
  print molecular diffusion in both equations, Launder & Spalding's
  high-Reynolds form none (Eqs. 2.2-1–2.2-2).
- Launder & Spalding's concluding claim that the model needs no
  adjustment of constants between near-wall and free shear flows (§4)
  stands in the same paper beside the round-jet modification, the higher
  $C_\mu$ of weak-shear flows (§2.2) and the factor-20 reduction of the
  wall-function $\varepsilon$ behind a step (§3.5).
- Launder & Spalding's §2.1 gives $\nu_t=C_\mu k^{1/2}L$ with
  $L=c_lk^{3/2}/\varepsilon$ (Eqs. 2.1-2, 2.1-13) and calls
  $\nu_t=C_\mu k^2/\varepsilon$ (Eq. 2.2-3) "its equivalent in terms of
  $\varepsilon$"; (2.1-2) with (2.1-13) gives $\nu_t=C_\mu c_lk^2/\varepsilon$
  *(compiler check, not in the sources)*, and §2.3 writes
  $L=k^{3/2}/\varepsilon$; the value of $c_l$ is not printed.
- Menter's Figure 10 (transonic bump) labels its $k$-$\varepsilon$ curve "k-ε
  std.", the other figures "k-ε JL" (p. 1603).
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
- [Yu et al. (2023b)](/sources/yu-2023-b.md) — §IV, Eqs. (20)–(21), Figs. 18–19 (two-equation eddy viscosity against DNS in shock interactions, wall-pressure-dependent $C_\mu$); §V.
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §III.E, Figs. 12–14 ($k$-$\varepsilon$ eddy viscosity in the interface argument).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §3.2.3.3 (CAWAPI-2 secondary vortex with $k$-$\varepsilon$, as cited).
- [Fang et al. (2026)](/sources/fang-2026.md) — §3.4, Table 3 (LSTM against $k$-$\varepsilon$, as cited); §4.2.2 ($k$-$\varepsilon$ inside a PINN, as cited).
- [Le et al. (2024)](/sources/le-2024.md) — §3.1.1 (Bayesian calibrations cited).
- [Salehi et al. (2024)](/sources/salehi-2024.md) — Eq. (21) and text (RANS time scale $k/\varepsilon$); §3.1 (RANS-CSE studies).
- [Launder & Spalding (1974)](/sources/launder-1974.md) — §1.2, §2.1 Eqs. 2.1-2–2.1-13 (choice of $\varepsilon$, near-wall constraint), §2.2 Eqs. 2.2-1–2.2-6, Table 2.1 (standard model, constants, round-jet modification), §2.3 Eqs. 2.3-4–2.3-7 (Jones–Launder low-Reynolds form), §3.1–§3.9 Figs. 3.1–3.9, §4.
- [Menter (1994)](/sources/menter-1994-b.md) — pp. 1598–1599 (freestream sensitivity, damping functions), Eqs. 3–4, 13, App. Eq. A5 (transformed $k$-$\varepsilon$, two-layer option), pp. 1601–1603 Figs. 2–9 (Jones–Launder model in adverse pressure gradients, step, NACA 4412).
