---
type: Definition
title: "Large-eddy simulation: filtering and the subgrid-scale stress"
description: "Large-eddy simulation resolves the filtered velocity and models the subgrid-scale stress; this page fixes the filtered equations (Favre, density-unweighted, real-gas and reacting forms), the filters and filter widths used by the sources, the commutation and discretization terms, and the gauge freedom of the subgrid stress."
status: established
aliases: [LES, filtered Navier–Stokes equations, subgrid-scale stress, SGS stress, subfilter stress, coarse-grained equations]
tags: [les, filtering, sgs-model, compressible]
timestamp: 2026-10-28T16:59:00Z
---

# Large-eddy simulation: filtering and the subgrid-scale stress

**Large-eddy simulation (LES)** computes a low-pass filtered velocity
$\bar u_i=G*u_i$ that carries the large, energy-containing eddies, and
replaces the effect of the removed (subgrid) scales by a model of the
**subgrid-scale (SGS) stress**
$\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$. The filtered equations are
exact but unclosed; the closure question is what replaces $\tau_{ij}$ (an
explicit [subgrid-scale model](/methods/smagorinsky-model.md), the
discretization itself in [implicit LES](/definitions/implicit-les.md), or a
learned correction). The filter can be an explicit convolution, the grid
projection, or the operator induced by the discretization, and the sources
disagree on conventions (sign of $\tau_{ij}$, definition of the filter width
$\Delta$, meaning of "implicit"); this page records them in the registry
notation.

## Filtered equations

For incompressible flow, with a filter that commutes with differentiation,
Agrawal et al. (2022, §II, Eqs. 1–3)
[(source)](/sources/agrawal-2022.md) write

$$\begin{aligned}
\partial_i\bar u_i&=0,\\
\partial_t\bar u_i+\partial_j(\bar u_i\bar u_j)&=-\partial_i\bar p+\nu\,\partial_j\partial_j\bar u_i-\partial_j\tau_{ij},\qquad
\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j ,
\end{aligned}$$

with $p$ the kinematic pressure; the isotropic part
$\tfrac13\tau_{kk}\delta_{ij}$ is absorbed into a modified pressure, so only
the deviatoric part $\tau^d_{ij}$ is modelled. [Prakash et al. (2022)](/sources/prakash-2022.md)
(§II, Eqs. 1–2) and [Abe (2021)](/sources/abe-2021.md) (§II, Eqs. 1–2)
write the same equations; Abe includes $\tfrac13\tau_{kk}$ in the filtered
pressure, while Prakash et al. keep the full (not deviatoric) tensor. The same structure, with the
SGS term written as an operator $M_i=-\partial_j\tau_{ij}$ added to the
right-hand side, is used by [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§2.1, Eqs. 6–9), who stress that the LES problem can be posed independently
of the mesh: in their usage $\Delta$ is a separation scale, a continuous
parameter, and the cell size $\Delta x$ is chosen separately.

For compressible flow [Goc et al. (2021)](/sources/goc-2021.md) (§2.1,
Eqs. 2.1–2.5) filter the mass, momentum and total-energy equations with the
Favre filter $\tilde\phi=\overline{\rho\phi}/\bar\rho$; the momentum
equation carries $-\partial_j\tau_{ij}$ with
$\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$, and the
energy equation an SGS heat flux $\bar\rho(\widetilde{eu_j}-\tilde e\tilde u_j)$
plus the SGS work term $-\partial_j(\tilde u_i\tau_{ij})$. Goc et al. call
the overbar and tilde "Reynolds and Favre averaging operators" although they
use them as LES filters. [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md)
(§3) solve the spatially filtered compressible equations with a
cell-centred finite-volume method in arbitrary Lagrangian–Eulerian form, to
follow a deforming panel.

[Helm & Martín (2022)](/sources/helm-2022.md) (§II, Eqs. 1–8) write the
Favre-filtered equations in generalized curvilinear coordinates for LES of
hypersonic compression ramps, with four unclosed terms: the subgrid stress
$\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$, the subgrid
heat flux $\bar\rho(\widetilde{u_jT}-\tilde u_j\tilde T)$, the subgrid
turbulent diffusion $\bar\rho(\widetilde{u_ju_ku_k}-\tilde u_j\widetilde{u_ku_k})$
and the subgrid viscous diffusion $\overline{\sigma_{ij}u_i}-\tilde\sigma_{ij}\tilde u_i$
(registry notation; the paper writes the Favre filter with a hat). The
first two are closed by a [dynamic mixed model](/methods/scale-similarity-model.md),
the turbulent diffusion by $\tilde u_k\tau_{jk}$ (Knight et al., cited), and the viscous diffusion is neglected because it is "typically
an order of magnitude smaller than the SGS heat flux". The filtered total
energy carries $\tfrac12\tau_{kk}$.

[Duan & Wang (2024)](/sources/duan-2024.md) (§2.1) solve the
compressible equations for implicitly filtered variables, add a modelled
subgrid stress to the viscous stress and drop the subgrid pressure work,
heat transfer, turbulent diffusion and viscous diffusion "for the low Mach
number flows considered". [Bouhafid et al. (2024)](/sources/bouhafid-2024.md)
(§2.2, Eq. 2.6) keep the Favre-filtered subgrid stress and subgrid heat
flux $\bar\rho(\widetilde{Tu_j}-\tilde T\tilde u_j)$ in a temporal LES of
an aircraft wake, both closed by the Smagorinsky model.
[Kim et al. (2024)](/sources/kim-2024.md) (§2.1, Eqs. 2.1–2.2) add to the
incompressible filtered equations the mass source and momentum forcing of
an [immersed boundary](/methods/immersed-boundary-method.md) for LES of a
cylinder wake. [Domaradzki (2024)](/sources/domaradzki-2024.md) (§1, §2.3)
recalls that the filtered equations require filtering and differentiation
to commute, and writes the LES field as the projection of the DNS field on
the LES mesh, a sharp truncation at the mesh cutoff $k_c=\pi/\Delta x$.
Filtering that field once more with a graded filter splits the full
subgrid stress on the mesh into a part computable from the LES field, the
resolved stress $L_{ij}$ of the registry, and a part that contains all
interactions with the true subgrid scales beyond $k_c$ (Eqs. 2.35–2.37,
after Domaradzki et al. 2002, cited); the
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
is built on the first part.

[Duraisamy (2021)](/sources/duraisamy-2021.md) (§II, Eq. 2) frames LES and
RANS together: coarse-graining a high-fidelity system $\mathcal R(q)=0$ by
low-pass filtering (LES) or ensemble averaging (RANS) gives an equation for
the coarse-grained state plus the divergence of an unclosed term, and this
coarse-grained equation "is *not* an approximation"; the approximation enters
only with the closure.

[Sirignano & MacArt (2023)](/sources/sirignano-2023.md) (§2, Eq. 2.2) add
to the incompressible filtered equations a term $\Gamma_i$ (page-local)
that collects the unclosed boundary terms produced by filtering at an
immersed bluff body and the commutation error of a non-uniform filter on a
non-uniform mesh (Ghosal, cited); their learned closure replaces
$-\partial_j\tau_{ij}+\Gamma_i$ as a whole (see
[neural-network SGS models](/methods/neural-network-sgs-model.md)).
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§II, Eqs. 1–2;
§III A) assume commutation and filter channel DNS only in the homogeneous
directions, so that the filter leaves the Reynolds average unchanged and the
kinetic energy splits exactly into mean, resolved and subgrid parts; a
wall-normal filter would be inhomogeneous and add commutation terms, a
limitation they leave open. [Lederer et al. (2023)](/sources/lederer-2023.md)
(§3.1) list the commutation error, dissipation in laminar regions and a
model acting on all resolved scales as drawbacks of classical explicit LES
that motivate a variational multiscale formulation.

**Kinetic coupling of an eddy viscosity.** [Zhao et al. (2021)](/sources/zhao-2021-c.md)
(§III, Eqs. 12–13; citing Chen et al. 2003, 2004) solve compressible LES
with a [gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md),
in which no stress divergence is added: the eddy viscosity of any model
enters the BGK collision time,
$\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$ (the collision
time $\tau_{\mathrm{col}}$ and its turbulent increment
$\tau_{\mathrm{col},t}$, registry §11, as on the gas-kinetic page; the
paper's $\tau$, $\tau_t$), which by the Chapman–Enskog expansion adds
$\mu_t$ to the molecular viscosity. Because the solver needs an eddy
viscosity, the stress of their structural (Clark) model is first
converted to one (§III.D; see
[gradient model](/methods/gradient-model.md)). The resolved variables are
filtered cell averages with an implicit grid filter; no Favre filtering is
mentioned (§III.A).

**Volume filtering at walls.** [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md)
(§2.1–2.3, Eqs. 2.3–2.27) filter the incompressible equations up to and
across solid walls with a unitary, symmetric, compact kernel $G$ of support
width $\Delta_f$ (registry §11, the paper's $\delta_f$). The kernel is truncated by the
fluid indicator and **not rescaled**: the filtered indicator, a fluid
volume fraction $\varphi_f$ (registry §11, the paper's $\alpha_f$; $\tfrac12$ at a planar wall for any
symmetric kernel), carries the deficit, and filtered quantities extend
$\Delta_f/2$ into the solid. Exact commutation identities, which they cite from
Dave, Herrmann & Kasbaoui (2023), turn the wall terms into
surface integrals. The filtered momentum equation then contains two
unclosed terms, the subfilter stress (the registry's $\tau_{ij}$, full
tensor, positive convention, Eq. 2.20) and an immersed-boundary body force,
plus a **residual viscous stress**: the filtered viscous stress minus the
viscous stress of the filtered velocity, closed but non-zero within
$\Delta_f/2$ of the wall (Eqs. 2.17–2.18). At the wall this residual stress
is linear in the wall-slip velocity $\boldsymbol u_{\mathrm{slip}}$, with components $\bar u_i|_w-u_{w,i}$ (Eq. 2.27), and
the wall stress follows from that slip (Eq. 2.25), so the slip is the only
unclosed wall quantity and modelling it is a wall model (§2.3). The authors
contrast this with wall-resolved LES, whose filter is refined and rescaled
near the wall, and with the truncated-and-rescaled kernel of Bose & Moin
(as cited), which in their view carries commutation errors (§2.1, §4.2);
they recall that commutation terms, ignored by most LES, "can be of the
order of the subgrid terms" (§2.1, citing Ghosal & Moin and others).
A priori, on channel DNS at $Re_\tau=5200$ filtered with $\Delta_f^+=50$–300,
the residual viscous stress is larger than the filtered viscous stress at
every filter size tested, and the peak subfilter shear stress grows from
0.24 to 0.57 $\tau_w$ (§3.3, Fig. 10). The resulting immersed-boundary-modelled
LES (IBMLES) and its slip models are on
[immersed boundary methods](/methods/immersed-boundary-method.md) and
[wall-modelled LES](/methods/wall-modelled-les.md); no a posteriori run is
reported (§7).

**Two-dimensional LES.** [Jakhar et al. (2026)](/sources/jakhar-2026.md)
(p. 2, Eqs. 1–2; App. C) write the filtered equations of forced
two-dimensional (geophysical) turbulence with a forcing term that collects
a time-invariant forcing, Rayleigh drag and the Coriolis force, the full
tensor $\tau_{ij}$ in the positive convention, and solve them in
vorticity–streamfunction form with a pseudo-spectral code.

**One-equation closure in a hybrid solver.** [Tang et al. (2022)](/sources/tang-2022.md)
(§2.1, Eqs. 1–9) close the LES region of a zonal hybrid RANS/LES of
supersonic hydrogen combustion with the one-equation subgrid
kinetic-energy model of Yoshizawa (as cited): $\nu_t$ proportional to
$k_{\mathrm{sgs}}^{1/2}\Delta$ with constant 0.02075, a dissipation
$C_dk_{\mathrm{sgs}}^{3/2}/\Delta$ with $C_d=1.0$ (page-local), $\Delta$ the
box-filter width. They rewrite it as a transport equation for $\nu_t$ and
blend it near walls with the Spalart–Allmaras equation (see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)). The Favre-filtered
subgrid variance of the mixture fraction, a look-up coordinate of the
flamelet table, is closed either by scale similarity with a test filter of
width $2\Delta$ or by a transport equation, and the authors recommend the
latter (§2.2, Eqs. 15–17; §4); see
[flamelet tabulated chemistry](/methods/flamelet-tabulated-chemistry.md)
and [scale-similarity models](/methods/scale-similarity-model.md).

[Saini et al. (2023)](/sources/saini-2023.md) (§2.2, Eqs. 2–5) write the
budget of the resolved kinetic energy $\tfrac12\bar u_i\bar u_i$ in
incompressible LES, integrated over a subdomain: the subgrid term splits
into a subgrid dissipation $-\int\tau_{ij}\partial_j\bar u_i\,dV$ (the
volume integral of $\Pi$ when the stress enters the momentum equation as
$-\partial_j\tau_{ij}$, as in their Eq. 1 *(compiler check, not in the
sources)*) and a subgrid flux through the subdomain surface. The residual
of its discrete form measures the [numerical dissipation](/properties/numerical-dissipation.md).

In compressible LES the filtered total energy contains the subgrid kinetic
energy: Volpiani (2024, §2.1, Eq. 4), citing Kosović et al.,
writes $\bar\rho\tilde e=\bar p/(\gamma-1)+\tfrac12\bar\rho\tilde u_i\tilde u_i+\tfrac12\tau_{kk}$
($\tilde e$ the Favre-filtered total specific energy, page-local), and
notes that the last term "is usually neglected", which leaves the equation
of state unchanged. Valencia et al. (2026, §II B, Eq. 14) likewise take the
filtered equation of state as $p(\bar\phi)=\bar\rho R\tilde T$ ($R$ the
gas constant, page-local) and set the filtered pressure, viscous and
heat-conduction terms equal to their values at the filtered state, an error
they call "negligible" (citing their refs. 33 and 38).
[Qi et al. (2022)](/sources/qi-2022-b.md) (§2, Eqs. 2.3–2.4) keep the
term: their filtered total energy is
$\bar\rho C_v\tilde T+\tfrac12\bar\rho\tilde u_i\tilde u_i+\bar\rho k_{\mathrm{sgs}}$
(citing Martín et al. and Garnier et al.), with
$k_{\mathrm{sgs}}$ transported by its own exact compressible equation
(citing Chai & Mahesh), so that $\tau_{kk}=2\bar\rho k_{\mathrm{sgs}}$
(Eq. 2.12) is a solved quantity rather than a modelled one; that equation
contains a subgrid pressure-dilatation, a solenoidal and a dilatational
dissipation, each modelled separately (Eqs. 3.1–3.7; see the
[dynamic procedure](/methods/dynamic-procedure.md)).
[De Vanna et al. (2022)](/sources/devanna-2022.md) (§2.1, Eqs. 1–5) neglect
the isotropic part of the stress (citing Garnier et al.), split
the subgrid energy flux into a subgrid heat flux, a triple correlation and
the work of the stress trace, close the heat flux with a subgrid Prandtl
number of 0.9 and neglect the triple correlation.
[Tonicello et al. (2022)](/sources/tonicello-2022.md) (§4, Eqs. 4.2–4.5)
write the filtered momentum equation with a second unclosed term, the
difference between the filtered viscous stress and the viscous stress of
the filtered state, which arises from the temperature dependence of $\mu$
and is "often neglected". In their filtered DNS of a supersonic ramp the
subgrid Mach number $\sqrt{2\bar\rho k_{\mathrm{sgs}}/(3\gamma\bar p)}$
reaches about 0.4 for differential filters of width $4h$ and $8h$, and the
correlation of the subgrid flux with the resolved pressure dilatation grows
with the filter width; they conclude that the weight of compressibility in
the closure is set "not entirely by the physics of the problem" but by the
filter width (§4.2, Table 4; see
[energy backscatter](/definitions/energy-backscatter.md)).

[Xu et al. (2023)](/sources/xu-2023.md) (§2.1, Eqs. 2.1–2.14) write the
Favre-filtered equations for wall-bounded LES with the stress per unit
mass, $\tau_{ij}=\widetilde{u_iu_j}-\tilde u_i\tilde u_j$, entering the
momentum equation as $-\partial_j(\bar\rho\tau_{ij})$, a subgrid heat flux
$Q_j=\widetilde{u_jT}-\tilde u_j\tilde T$ (page-local) and a subgrid
turbulent diffusion
$\tfrac12\bar\rho(\widetilde{u_ju_iu_i}-\tilde u_j\widetilde{u_iu_i})$ in
the energy equation. The filtered total energy keeps
$\tfrac12\bar\rho\tau_{ii}$, and the temperature is recovered from it with
$\tau_{ii}$ subtracted (Eqs. 2.13–2.14). The two viscous unclosed terms
are neglected, citing several LES studies and "justified by the inviscid
criterion" of Aluie and of Zhao & Aluie, and the turbulent diffusion is
approximated by $\bar\rho\tau_{ij}\tilde u_i$ (after Martin et al. and
others, cited), so that only $\tau_{ij}$ and $Q_j$ are modelled; the
density $\bar\rho$ multiplies the stress inside the divergence, not
inside the definition of $\tau_{ij}$.

**Density-unweighted filtering.** Favre filtering is a choice, not a
requirement. [Zhang et al. (2022b)](/sources/zhang-2022-f.md) (§II,
Eqs. 8–20) filter the compressible equations with the plain filter
$\bar\phi=G*\phi$ only. The continuity equation then carries a subgrid
mass flux, $\partial_t\bar\rho+\partial_j(\bar\rho\bar u_j)=-\partial_j\mathcal M_j$
with $\mathcal M_j=\overline{\rho u_j}-\bar\rho\bar u_j$; the momentum
equation the stress $\tau^{\mathrm{du}}_{ij}=\overline{\rho u_iu_j}-\bar\rho\bar u_i\bar u_j$,
the gradient of a density–temperature correlation
$\mathcal H=\overline{\rho T}-\bar\rho\bar T$ in the pressure term and an
unsteady term $-\partial_t\mathcal M_i$; the energy equation a heat flux,
a turbulent diffusion, a viscous diffusion and the unsteady terms
$\partial_t(\tfrac12\tau^{\mathrm{du}}_{kk})$ and $\partial_t\mathcal H$
(page-local symbols, as on the [gradient model](/methods/gradient-model.md)
page). The authors say the unsteady terms "can lead to numerical
instability", and argue that Favre filtering has "intrinsic drawbacks" in
flows with rapid density variation because its filtered equations are
"simplified without considering some critical physical information"
(§I). They cite Sun & Lu for a priori tests only, Dupuy et al. for finding
the two filterings similar at low Mach number, and Sidharth et al. for a
density-unweighted scheme without the unsteady terms; how they integrate
the unsteady terms themselves is not stated. In decaying isotropic
turbulence ($\Delta=16$ DNS spacings) the rms divergences of the stress,
mass-flux, heat-flux and turbulent-diffusion terms are of order 4–51,
while the $\mathcal H$ term is 0.0060 at $M_t=0.4$ and 0.11 at $M_t=0.8$
(Table II); the authors keep it because it "might have special
significance" in flows with rapidly changing density (§IV A, §V). The
viscous-diffusion nonlinearity is neglected. Closures and results are on
the [gradient-model](/methods/gradient-model.md) and
[scale-similarity](/methods/scale-similarity-model.md) pages.

**Real-gas subgrid terms.** With a nonlinear equation of state the
Favre-filtered pressure and internal energy are not the functions of the
filtered state. For a dense gas (Martin–Hou equation of state, Chung
transport model), [Zhang et al. (2022d)](/sources/zhang-2022-h.md)
(§II, Eqs. 12–23), following Giauque et al. (cited), write four
thermodynamic subgrid terms beside the stress and the turbulent diffusion:
a subgrid pressure $\bar p-p(\bar\rho,\tilde T)$, a density–internal-energy
correlation $\overline{\rho e}-\bar\rho\,e(\bar\rho,\tilde T)$, a subgrid
pressure work $\overline{pu_j}-p(\bar\rho,\tilde T)\tilde u_j$ and a subgrid
internal-energy flux ($e$ the internal energy per unit mass, page-local);
the nonlinearities of the viscous, heat-flux and viscous-work terms are
dropped (after Giauque et al.). In decaying isotropic turbulence of the
fluid PP11 near its critical point, the divergences of the pressure work,
turbulent diffusion and stress dominate; the subgrid-pressure and
internal-energy-flux terms are an order of magnitude smaller in their
equations and grow with $M_t$ (rms of the subgrid-pressure gradient 0.101
and 0.386 at $M_t=0.4$ and 0.8, against 1.657 and 1.434 for the stress
divergence; Tables IV–V). Dropping the thermodynamic terms changes the
LES little "in the present study" (§IV B, §V), which the authors set
beside Giauque et al.'s statement, as they summarize it, that such terms
"should be modeled" (§I).

**Reacting flows.** [Fureby & Nilsson (2023)](/sources/fureby-2023.md)
(§3.1, Eq. 1) write the Favre-filtered equations of a reacting mixture with
the full density-weighted stress (positive trace) entering as its negative
divergence, species subgrid fluxes, a subgrid energy flux made of the
subgrid flux of total sensible energy, a pressure-work and a viscous-work
part, and filtered
reaction rates closed by a partially-stirred-reactor model; the subgrid
stress is closed by the localized dynamic
[one-equation model](/methods/subgrid-kinetic-energy-equation-model.md).
They add that extending subgrid models from incompressible to compressible
reacting flow by dimensional arguments "can be disputed but in the absence
of better alternatives this constitutes today's standards" (§3.2).
[Ihme et al. (2022)](/sources/ihme-2022.md) (§4.1.4, Eqs. 71–72) write the
filtered reacting-flow system as one vector equation whose right-hand side
groups the filtered source (turbulence–chemistry interaction), the
subgrid convective flux and the subgrid molecular-diffusion flux, the
framing of their review of data-driven closures (see
[neural-network SGS models](/methods/neural-network-sgs-model.md)).

**Further reacting, sooting and atmospheric forms.** Further sources
write the same structure with different closures of the subgrid
scalar fluxes:

- [Vignat et al. (2024)](/sources/vignat-2024.md) (§3.2, Eqs. 1–7) write
  the Favre-filtered equations of a reacting mixture (12-species
  mechanism) with molecular and subgrid fluxes merged: one stress
  $(\bar\mu+\mu_t)[\nabla\tilde{\boldsymbol u}+(\nabla\tilde{\boldsymbol u})^T]-\tfrac23(\bar\mu+\mu_t)(\nabla\cdot\tilde{\boldsymbol u})\boldsymbol I$,
  with conductivities and diffusivities increased by subgrid parts from
  turbulent Prandtl and Schmidt numbers of 0.7, and reaction rates
  evaluated from filtered variables without a turbulence–chemistry model.
  They call the unweighted filter "Reynolds filtering" and the merged
  stress a "Reynolds-averaged stress tensor", in an LES; no isotropic
  subgrid part is modelled separately.
- [Nista et al. (2023)](/sources/nista-2023.md) (§1, Eqs. 1–3) write the
  Favre-filtered momentum equation with the full subgrid stress
  $\widetilde{u_iu_j}-\tilde u_i\tilde u_j$ (positive trace, per unit
  mass, entering as $-\partial(\bar\rho\,\cdot)$) and the subgrid
  temperature flux $\widetilde{u_iT}-\tilde u_i\tilde T$, both closed by a
  [super-resolution model](/methods/super-resolution-sgs-model.md); their
  Eq. (1) is printed with inconsistent free indices.
- [Nmira et al. (2023)](/sources/nmira-2023.md) (§2.1) transport the
  filtered mixture fraction and its second moment, so that the subgrid
  variance follows from its definition, $\widetilde{Z^2}-\tilde Z^2$ ($Z$
  page-local), and close the scalar flux by a dynamic eddy diffusivity.
- [Wei et al. (2023)](/sources/wei-2023.md) (§II B, Eqs. 9–15) use the
  density-weighted stress $\overline{\rho u_iu_j}-\bar\rho\tilde u_i\tilde u_j$,
  constant subgrid turbulent Prandtl and Schmidt numbers (0.85, 0.7) and a
  laminar ("quasi-laminar") reaction-rate closure, and neglect the subgrid
  viscous work.
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) (§2, Eqs. 16–18 of the
  LES block) give the eddy-viscosity LES formulation of their review of
  discontinuous schemes for multicomponent flows, with subgrid heat and
  mass fluxes from turbulent Prandtl and Schmidt numbers, and treat "the
  effect of LES-filter operator" as "an augmented diffusion term from the
  numerical viewpoint"; no subgrid model or $\Delta$ is named.
- [Taschner et al. (2024)](/sources/taschner-2024.md) (§2.1, Eqs. 1–4)
  write the anelastic filtered equations of atmospheric LES, with a height
  dependent reference density, buoyancy, Coriolis and geostrophic forcing,
  turbine body forces and a Smagorinsky stress (see
  [actuator line model](/methods/actuator-line-model.md)).

**Subgrid kinetic-energy budget.** [Cao et al. (2022b)](/sources/cao-2022-c.md)
(§IV B, Eq. 17) write the Favre transport equation of
$\bar\rho k_{\mathrm{sgs}}=\tfrac12\tau_{kk}$ with production
$-\tau_{ij}\tilde S_{ij}$ (the registry's $\Pi$, read as inter-scale
transfer), dissipation, a subgrid pressure dilatation and diffusion terms,
and evaluate the production a priori (see
[energy backscatter](/definitions/energy-backscatter.md)); its transported
form is the basis of [one-equation models](/methods/subgrid-kinetic-energy-equation-model.md).

**When the subgrid velocity itself is needed.** For dispersed multiphase
flows, interface methods, wind-turbine loads and flame-front location the
closure of $\tau_{ij}$ is not enough; [Hausmann et al. (2022)](/sources/hausmann-2022.md)
(§I) generate an approximate subgrid velocity alongside the LES (see
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)).

### Sign conventions in the sources

The registry uses the positive-trace convention above. The following
sources print the opposite sign and are translated here:
[Vela-Martín (2022)](/sources/velamartin-2022.md) (§2.1, Eq. 2.3, said
explicitly by the author) defines the stress as $\bar u_i\bar u_j-\overline{u_iu_j}$
entering with $+\partial_j$; [Haering et al. (2022)](/sources/haering-2022.md)
(§III, Eq. 3) define $\tau^{sgs}_{ij}=-(\overline{u_iu_j}-\bar u_i\bar u_j)$;
Duraisamy (2021, §III.B) writes the SGS stress with the reversed sign while
the RANS stress of the same paper (Table I) is positive.
[Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) (§2.1,
Eqs. 1–3) define the compressible subgrid stress as
$\bar\rho\tilde u_i\tilde u_j-\overline{\rho u_iu_j}$, minus the registry's,
entering the momentum flux with a minus sign; their energy equation carries
a subgrid energy flux that the paper does not define further. Duan & Wang
(2024, §2.1–2.2) write the model stress with the sign of the viscous
stress, $+2\bar\rho\nu_tS_{ij}$ added to it, i.e. minus the registry's
modelled $\tau_{ij}$, with the full strain. Domaradzki (2024) uses the
positive stress but defines the subgrid dissipation as
$\tau_{ij}\bar S_{ij}$, negative for forward transfer, minus the registry's
$\Pi$. Agrawal et al. (2022), Goc et al.
(2021), Vicente Cruz & Lamballais (2023), Abe (2021) and Prakash et al.
(2022) use the positive convention, as do
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (§II, Eqs. 1–2),
[Kim et al. (2022)](/sources/kim-2022.md) (§II A, Eqs. 3–4),
Helm & Martín (2022, Eq. 5) and [Cai et al. (2022)](/sources/cai-2022.md)
(§II.A, Eqs. 9, 11), the last two in density-weighted form, and
Inagaki & Kobayashi (2023, Eq. 2), [Kang et al. (2023)](/sources/kang-2023.md)
(Eqs. 2.5–2.6) and Sirignano & MacArt (2023, Eq. 2.2), all three with the
full tensor, trace included; so do Domaradzki (2024, Eq. 1.2), Kim et al.
(2024, §2.1), [Wang et al. (2023c)](/sources/wang-2023-c.md) (Eq. 10) and,
in Favre form, Bouhafid et al. (2024). [Saini et al. (2023)](/sources/saini-2023.md)
(Eq. 1) do not print the sign or trace convention of their stress.
[Caban et al. (2026)](/sources/caban-2026.md) (§2,
Eq. 5), [Wu & Lele (2026)](/sources/wu-2026.md) (§2.1, Eq. 2.2), Jakhar et
al. (2026, Eqs. 1–2) and Rickard & Kasbaoui (2026, Eq. 2.20) use the
positive convention with the full tensor;
[Brillon & Nadarajah (2026)](/sources/brillon-2026.md) (§2.3, Eqs. 18–20)
write a deviatoric model stress $2\bar\rho\nu_t\bar S^d_{ij}$ that enters
like the viscous stress, minus the registry's.

Further sources split the same way.

- **Positive convention.**
  - [Li et al. (2024)](/sources/li-2024.md) (Eqs. 5–6) and
    [Zhao et al. (2025)](/sources/zhao-2025.md) (Eq. 4) use the positive
    convention with the full tensor.
  - [Reddy et al. (2026)](/sources/reddy-2026.md) (§2.1, Eqs. 3–4) use it
    in Favre form, $\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$. They
    close the full tensor as $-2\nu_t\tilde S_{ij}$, without the deviatoric
    projection and without $\bar\rho$.
  - [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) (§2.1, Eq. 2.4)
    write a dynamic (density-multiplied) stress that enters the total
    stress as $\boldsymbol\sigma_h-\boldsymbol\tau_{\mathrm{sgs}}$, which is
    the registry's sign.
  - [Li et al. (2021)](/sources/li-2021.md) (§II A, Eqs. 6–8) write the
    incompressible filtered equations with the full kinematic tensor, the
    registry's $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$, entering as
    $-\partial_j\tau_{ij}$ (their tilde is the LES filter, the registry's
    overbar, not a Favre filter); they model its deviatoric part.
- **Negative convention.**
  [Maejima & Kawai (2025)](/sources/maejima-2025.md) (§2.1, Eq. 2.9;
  §3.2) put the subgrid term with a minus sign in the filtered momentum
  equation. They define their model stress as the negative of the filtered
  product of sub-cell fluctuations. Their strain $S_{ij}$ is twice the
  registry's deviatoric strain.
  [De Cosmo et al. (2025)](/sources/decosmo-2025.md) (§2.1, Eqs. 1–4)
  define the Favre-filtered sub-filter stress with the minus sign and the
  density, $-\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$, add it to
  the filtered viscous stress, and drop it in their
  [implicit LES](/definitions/implicit-les.md).
- **Combined or unstated.**
  - [Zhao et al. (2021)](/sources/zhao-2021-c.md) (§III.D, Eq. 21) write
    the modelled stress as $-2\nu_t\bar S_{ij}$, the registry's sign,
    without a deviatoric projection or a statement of the trace.
  - [Mukha et al. (2025)](/sources/mukha-2025.md) (§II.A, Eq. 3) combine
    viscous and subgrid stresses in one kinematic tensor,
    $(\nu+\nu_t)(\partial_ju_i+\partial_iu_j)$, with a strain lacking the
    factor $\tfrac12$.
  - [Rismondo et al. (2025)](/sources/rismondo-2025.md) (§2.1, Eq. 2.2) add
    $+\partial_j\tau_{ij}$ on the right-hand side and do not define
    $\tau_{ij}$, so its sign convention is opposite to the registry's or
    unstated.
  - [Pan & Zhang (2023)](/sources/pan-2023.md) (§II.D, Eqs. 12–14) also
    add $+\partial_j\tau_{ij}$ without defining $\tau_{ij}$, and close it
    as $\tau_{ij}-\tfrac13\tau_{kk}\delta_{ij}=+2\nu_t\bar S_{ij}$: minus
    the registry's stress.
- **Compressible, positive.** [Valencia et al. (2026)](/sources/valencia-2026.md)
  (§II B, Eqs. 15–16) use the full density-weighted tensor
  $\overline{\rho u_iu_j}-\bar\rho\tilde u_i\tilde u_j$, the registry's
  Favre form, entering as $-\partial_j\tau_{ij}$. [Volpiani (2024)](/sources/volpiani-2024.md)
  (§2.1) subtracts the subgrid stress from the resolved viscous stress in
  the viscous flux, the registry's sign, without printing its definition.
  [Qi et al. (2022)](/sources/qi-2022-b.md) (§2, Eq. 2.8) and
  [De Vanna et al. (2022)](/sources/devanna-2022.md) (§2.1, Eqs. 1b, 2) use
  the same full density-weighted tensor entering as $-\partial_j\tau_{ij}$.
- **Further positive, full tensor.** [Hausmann et al. (2022)](/sources/hausmann-2022.md)
  (Eq. 6) and [Wang et al. (2022)](/sources/wang-2022-j.md) (Eq. 7; Favre
  form for their mixing layer, Eq. 31) keep the trace; [Cao et al. (2022b)](/sources/cao-2022-c.md)
  (Eq. 19), [Zhang et al. (2022d)](/sources/zhang-2022-h.md) (Eq. 19) and
  Fureby & Nilsson (2023, Eq. 1) use the Favre form with $\bar\rho$;
  [Zhang et al. (2022b)](/sources/zhang-2022-f.md) (Eq. 17) the
  density-unweighted $\overline{\rho u_iu_j}-\bar\rho\bar u_i\bar u_j$.
  [Ihme et al. (2022)](/sources/ihme-2022.md) (Eq. 74) print the Favre form
  and write the subgrid kinetic energy as $\tau_{kk}$, without the factor
  $\tfrac12$.
- **Compressible, negative.** [Tonicello et al. (2022)](/sources/tonicello-2022.md)
  (§4, Eq. 4.4) define $\bar\rho\tilde u_i\tilde u_j-\overline{\rho u_iu_j}$,
  minus the registry's, entering with $+\partial_j$, so its trace is
  $-2\bar\rho k_{\mathrm{sgs}}$ and its budget term $K_3$ is minus the
  registry's $\Pi$.
- **Printed without sign or trace.** [Chen et al. (2022)](/sources/chen-2022-g.md)
  (§4.1, Eq. 25) print the subgrid stress of their reference LES as
  $2\nu_t\tilde S_{ij}$, without the minus sign or a trace term, and switch
  between tilde and overbar for the filtered velocity (Eqs. 25–29 and 33).
- **Temporal residual stress.** [Simonis et al. (2022)](/sources/simonis-2022.md)
  (§2.1, Eqs. 2–3) define $\overline{u_iu_j}-\bar u_i\bar u_j$ with the
  overbar a *time* filter, the registry's sign, entering as
  $-\partial_j\tau_{ij}$ (see below).

## Filters and filter widths

**Kernels.** Vela-Martín (2022, §5.2, Eqs. 5.1–5.4) applies two homogeneous
filters to DNS of isotropic turbulence: the sharp Fourier filter,
$\hat G(k)=1$ for $|\boldsymbol k|<\pi/\Delta$ and 0 otherwise, and the
Gaussian filter $\hat G(k)=\exp\!\big(-k^2\Delta^2/(2\pi^2)\big)$, with
$\Delta$ the filter scale (the author's $\ell$). Vicente Cruz & Lamballais
(2023, §6.3, Eqs. 48–50) instead write the Gaussian as
$\exp(-k^2\Delta^2/24)$ and introduce a super-Gaussian
$\exp(-k^6\Delta^6/256)$; the two Gaussian forms are the same kernel with
widths related by $\Delta^2_{(24)}=12\Delta^2_{(2\pi^2)}/\pi^2$ *(compiler
check, not in the sources)*, a convention difference only. For a priori
filtering of channel DNS, Agrawal et al. (2022, §V) use a discretely
commutative filter with three vanishing moments applied recursively to a
width of three grid sizes. [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
(App. E, Eqs. E.1–E.5) give the transfer functions of the top-hat
volume-averaging filter, $\prod_\alpha\mathrm{sinc}(\pi k_\alpha\Delta/2)$,
and of their face-averaging filter, which omits the factor of the face-normal
direction and therefore damps less. Prakash et al. (2022, §III.A) box-filter
DNS of isotropic turbulence ($Re_\lambda=418$) isotropically and
anisotropically: "book-type" filters with one fine and two coarse widths and
"pencil-type" filters with two fine and one coarse width, the coarse
widths up to $292\eta$ against a fine width of $15\eta$. Abe (2021, §IV B, App. C) top-hat filters a fine LES of a
backward-facing-step flow in the two homogeneous-spacing directions only,
and checks with a three-point trapezoidal filter
$\bar\phi_i=\tfrac14(\phi_{i+1}+2\phi_i+\phi_{i-1})$ that filtering also in
the wall-normal direction changes the subgrid values little.
Xu et al. (2023, §2.2, Eq. 2.32) also filter channel DNS in the two
homogeneous directions only, with the discrete top-hat
$\bar f_i=\tfrac1{4n}\big(f_{i-n}+2\sum_{j=i-n+1}^{i+n-1}f_j+f_{i+n}\big)$
of width $2n$ DNS spacings (the integers $n$, and the filter-to-DNS
spacing ratios $n_x$, $n_z$, which "need to be even numbers", page-local),
$n_x=8$, $n_z=4$ for training.
[Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) (§3, Eqs. 7–17)
use elliptic **differential filters** solved on the grid: Germano's
$\bar\phi-\delta_{\mathrm G}^2\partial_i\partial_i\bar\phi=\phi$, with
transfer function $1/(1+\delta_{\mathrm G}^2k^2)$ ($\delta_{\mathrm G}$ the filter radius, registry §11), which never vanishes,
and their own filter with a second-derivative term on both sides, whose
right-hand coefficient gives complete attenuation at the grid cut-off
(page-local symbols and the design on unstructured elements are on
[explicit modal filtering](/methods/explicit-modal-filtering.md)). They
list the properties an LES filter must have: linearity, conservation of
constants, positivity of the kernel and commutation with differentiation
(Eqs. 14–17, the last two after the reference they cite). Positivity of
their discrete filter is reduced to a phase condition that they leave
open (§4.2).

[Kim et al. (2022)](/sources/kim-2022.md) (§III E) filter channel DNS
with a cut-off filter in the two homogeneous directions only.
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (§III) use a
three-dimensional box filter for both grid and test level on isotropic
turbulence. [Helm & Martín (2022)](/sources/helm-2022.md) (§III B, Eq. 12,
Fig. 6) validate their LES against DNS filtered with the top-hat test filter
of their model, in space and, through Taylor's hypothesis, in time, with
widths matching the LES-to-DNS grid ratio; the filter truncates the
spectrum like the LES, and spectra are essentially unaffected for
$f\delta/U_e\lesssim0.4$ ($f$ the frequency, $U_e$ the edge velocity).

**Graded against sharp filters.** Domaradzki (2024, §2.3, Eqs. 2.28–2.30)
uses the 1-D Gaussian kernel $G(r)=\sqrt{6/(\pi\Delta^2)}\exp(-6r^2/\Delta^2)$
and the box of width $\Delta$, as tensor products, with $\Delta=2\Delta x$;
[Wang et al. (2023c)](/sources/wang-2023-c.md) (Eqs. 19, A1) use the same
Gaussian and the top-hat, noting that the two have the same second moment.
This Gaussian has the transfer function $\exp(-k^2\Delta^2/24)$, the form of
Vicente Cruz & Lamballais above *(compiler check, not in the sources)*.
Domaradzki stresses the difference of kind: a sharp spectral filter
removes every scale beyond the cutoff, a graded filter modifies all scales
and removes none, so the filtered field keeps the spectral support of the
unfiltered one, and an invertible filter (the Gaussian exactly) loses no
information. Domaradzki expects LES built on graded filters to depend on the
filter type and width, and on 3-D against product-of-1-D filtering (§4).
Wang et al. (2023c, §II.A) filter with a filter-to-grid ratio of 2
($\Delta=2h$, $h$ the LES spacing) "to ensure that the influence of the
numerical errors is much less compared to that of the SGS model", with
$\Delta=8$, 16 or 32 DNS spacings. Kim et al. (2024, §2.2, Eqs. 2.3–2.6)
box-filter DNS of a cylinder wake with the LES grid size in each direction,
one-sided near the wall, and build a test-filtered dataset with a box
filter in the spanwise direction only.

**Scale partition and the grid cutoff.** Caban et al. (2026, §2, Eqs.
1–2, Fig. 1) separate the filter cutoff $k_c=\pi/\Delta$ from the grid
cutoff $\pi/h$ ($h$ the largest grid spacing): resolved flow scales below
$k_c$, sub-filter scales between $k_c$ and the grid cutoff, which "may be
contaminated by numerical errors", and subgrid scales beyond the grid
cutoff; capturing the resolved scales requires $\Delta\ge h$. Graded
filters do not vanish at the grid cutoff: the box filter of width $\Delta=mh$
($m$ odd) has transfer $2/(m\pi)$ there, the Gaussian 0.193 at $\Delta=2h$
and 0.0014 at $\Delta=4h$. Most numerically induced filters vanish at the
grid cutoff, so their effect on the solution "may surpass that of the
assumed LES filter" (§2); see the discretization terms below.

**Filter shape in training data.** Wu & Lele (2026, §2.1, §3, Eqs.
3.1–3.4, Fig. 1) exclude the sharp spectral cutoff for subgrid modelling
"for general application", because a kernel oscillatory in physical space
creates spurious small scales (citing Sagaut). They build training data
with three filters of width 16 or 32 DNS spacings: the box; a
raised-cosine "discrete spatial cosine filter",
$G(r)=\Delta^{-1}\big(1+\cos(2\pi r/\Delta)\big)$ for $|r|\le\Delta/2$,
positive and compact, whose spectral oscillations peak at 0.028 against
0.22 for the box; and a box filter followed by a two-thirds dealiasing
cutoff. Adding the dealiasing cutoff "completely changes the subgrid stress
field": higher intensity and much wider PDFs of $\tau_{11}$, $\tau_{12}$ and
$\Pi$ than box or cosine filtering (§3.2.2, Fig. 4). Their premise is that
the filter of a running LES is implicit, "a product of both the grid and
the numerical method" (§1, §3.3), so a closure trained on one explicit
filter can overfit its peculiarities; see
[neural-network SGS models](/methods/neural-network-sgs-model.md) and
[implicit LES](/definitions/implicit-les.md). Jakhar et al. (2026, pp. 2–3)
Gaussian-filter 2-D DNS with $\Delta$ twice the LES grid spacing and
coarse-grain by factors of 4 to 64. Rickard & Kasbaoui (2026, §3.1, §5,
Eqs. 3.1–3.2, 5.1–5.3) use tensor products of compact 1-D kernels
(cosine, triangle, parabolic, triweight) and find kernel effects on their
slip and stress statistics small (differences in the stress profiles below
1% at $\Delta_f^+=300$).

The amount of [backscatter](/definitions/energy-backscatter.md) measured
a priori depends strongly on the kernel: the local flux is negative in about
half of the domain with the sharp filter and in less than one-fifth with the
Gaussian filter (Vela-Martín 2022, §5.3).

For learned subgrid models, Kang et al. (2023, §2.2–2.3, §3.5) use a
Gaussian grid and test filter with $\hat\Delta/\Delta=\sqrt5$ on isotropic
turbulence (a top-hat gave "no considerable differences"), with the grid
filter width set to twice the spacing of the pseudospectral LES because its
implicit filter is a Fourier cutoff; on channel flow they use the
fourth-order commutative discrete filters of Vasilyev, Lund & Moin (cited) with $\Delta$ and $\hat\Delta$ equal to 4 and 8 DNS spacings.
Sirignano & MacArt (2023, §3.1, Eq. 3.2) apply a box filter of local width
equal to 4 or 8 DNS spacings on a non-uniform mesh, with one-sided kernels
near walls, and downsample the result. Inagaki & Kobayashi (2023, §III A)
use a sharp cut-off in $x$ and $z$, with cut-off wavelength $2\Delta$
($\Delta x^+,\Delta z^+=52.4,26.2$ and $105,52.4$ in channel flow at
$Re_\tau=400$).

For the training data of
[neural-operator surrogates](/methods/neural-operator-les-surrogate.md):

- **Li et al. (2024)** (§V) filter isotropic-turbulence DNS with a sharp
  spectral cutoff at $k_c=\pi/\Delta=21$ to a $64^3$ grid. They filter a
  temporal mixing layer with a Gaussian of width four DNS spacings at
  filter-to-grid ratio 1.
- **Zhao et al. (2025)** (§3.1–3.2) cut isotropic turbulence sharply at
  $k_c=10$ on $32^3$, and the mixing layer at a width of eight DNS spacings
  with filter-to-grid ratio 2.
- **Maejima & Kawai (2025)** (§4) build filtered DNS of channel flow by
  top-hat filtering and downsampling in $x$ and $z$. The coarsening factors
  are 4 and 8.

**Effective filter of an LES.** Vicente Cruz & Lamballais (2023, §6.3,
Eq. 48) measure the filter an LES actually applies through the transfer
function $T_f(k,t)=\sqrt{E_{\mathrm{LES}}(k,t)/E_{\mathrm{DNS}}(k,t)}$
(page-local symbol). A [Smagorinsky](/methods/smagorinsky-model.md) LES at
numerical convergence gives $T_f(k_\Delta)\approx0.6$ and a slow decay
beyond: a weak filter. The [implicit spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
LES is approximated by the super-Gaussian above.

**Filter width.** The sources define $\Delta$ differently:

| Source | $\Delta$ |
|---|---|
| [Beck & Kurz (2023)](/sources/beck-2023.md), §III B, Eq. 11 | $\sqrt[3]{\mathrm{Vol}}/(N+1)$ for a DG element of volume Vol and degree $N$; the authors note it is not unique (non-equidistant nodes, skewed elements) |
| [Flad & Gassner (2017)](/sources/flad-2017.md), App. A | printed as "the local cell volume divided by $(N+1)^3$" (see Qualifications) |
| Agdestein & Sanderse (2025), §3.3 | the coarse grid spacing, "the diameter of the averaging domain in the infinity norm" |
| Vicente Cruz & Lamballais (2023), §4.1 | a separation scale independent of the mesh; the cell-based variant sets $\Delta=\Delta x$ |
| Haering et al. (2022), §II C | argue that the cube root of the cell volume tends to the smallest cell length at high aspect ratio and overestimates the effective resolution; they prefer measures based on the cell diagonal and a resolution tensor |
| Prakash et al. (2022), §II–III | $(\Delta_1\Delta_2\Delta_3)^{1/3}$ (after Deardorff) for the Smagorinsky and gradient models; the grid size in the a posteriori LES |
| Abe (2021), §II, §IV D | compares $(\Delta x\Delta y\Delta z)^{1/3}$, $\max(\Delta x,\Delta y,\Delta z)$ and, in the author's mixed model, $\sqrt{\max(\Delta x\Delta y,\Delta y\Delta z,\Delta z\Delta x)}$, which equals the maximum when $\Delta x=\Delta z\gg\Delta y$ |
| [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §6.1, Eq. (125) | $\Delta^3=\mathrm{Vol}/(N+1)^3$ for a DG element of degree $N$ |
| [Basile et al. (2023)](/sources/basile-2023.md), §2.2 | DES length scale $\sqrt[3]{\mathrm{Vol}}/(N+1)$ on DG elements: the cube root instead of the maximum spacing of classical DES, divided by $N+1$ following Lorteau et al. |
| [François et al. (2022)](/sources/francois-2022.md), §3.1 | DES length scale switching from $\max(\Delta x,\Delta y,\Delta z)$ to $(\Delta x\Delta y\Delta z)^{1/3}$ where the DDES shielding function exceeds 0.8 (ZDES mode 2, after Deck) |
| [Helm & Martín (2022)](/sources/helm-2022.md), §II | $(\Delta_\xi\Delta_\eta\Delta_\zeta)^{1/3}$, the LES grid spacings in the computational (curvilinear) directions |
| [Kim et al. (2022)](/sources/kim-2022.md), §II C | $(\Delta x\Delta y\Delta z)^{1/3}$ in wall units as an input of a learned model, whose output is multiplied by $\Delta^2$ to generalize across grids |
| [Blind et al. (2023)](/sources/blind-2023.md), §2.3 | $\mathrm{Vol}^{1/3}/(N+1)$ in DG (Vreman length scale), and $[(N+1)/(N_f+1)]^{1/3}$ times it for a modal test filter keeping degrees up to $N_f$ (registry §11, as on the mesh-adaptation page) |
| [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §II–III | "the effective grid scale"; filter sizes are quoted as multiples of twice the DNS grid spacing |
| [Lederer et al. (2023)](/sources/lederer-2023.md), §3.1 | $\sqrt[3]{\Delta x\Delta y\Delta z}/(N+1)$ for elements of degree $N$ (the paper's $k$), in the WALE eddy viscosity |
| [Kang et al. (2023)](/sources/kang-2023.md), Eq. (2.8) | $\sqrt[3]{\Delta_1\Delta_2\Delta_3}$ (after Deardorff) |
| [Kurz et al. (2023)](/sources/kurz-2023.md), §3.3 | "filter width of the LES filter" in a DG Smagorinsky model, not defined further |
| [Sirignano & MacArt (2023)](/sources/sirignano-2023.md), §3.1–3.2 | the local LES mesh spacing; directional spacings $\Delta_k$ in the [AMD model](/methods/anisotropic-minimum-dissipation-model.md) |
| [Cheylan et al. (2023)](/sources/cheylan-2023.md), §2.7, Eq. (37) | the local lattice spacing of a lattice Boltzmann solver |
| [Duan & Wang (2024)](/sources/duan-2024.md), §3, Eqs. (28)–(30) | three choices for an element of volume $V$ and degree $N$ (the paper's $P$) in flux reconstruction: $V^{1/3}$, $V^{1/3}/\sqrt{N+1}$ (new), $V^{1/3}/(N+1)$; with the model coefficients kept, the intermediate width is recommended for wall-modelled LES with the [Vreman model](/methods/vreman-model.md) |
| [Domaradzki (2024)](/sources/domaradzki-2024.md), §2.3 | $2\Delta x$ for the graded filter applied to the LES field |
| [Wang et al. (2023c)](/sources/wang-2023-c.md), §III–IV | twice the LES spacing (explicit filter), $8$–$32$ DNS spacings |
| [van Gastelen et al. (2024)](/sources/vangastelen-2024.md), §2.3, §4.1.1 | the coarse cell of a discrete box (cell-average) filter in 1D; the Smagorinsky baseline uses the coarse grid spacing |
| [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md), §3, Eqs. (16)–(19) | for the grid size of a PANS resolution ratio: $\max$, $\min$, diagonal $\sqrt{\Delta x^2+\Delta y^2+\Delta z^2}$ or cube root of the spacings; which one the runs use is not stated |
| [Reddy et al. (2026)](/sources/reddy-2026.md), §3.4, Table 1 | printed as $\min(\Delta x,\Delta y,\Delta z)/(N+1)$ for continuous spectral elements of degree $N$ (the paper does not say whether $\Delta x,\Delta y,\Delta z$ are element sizes or grid spacings; see the Source page); Table 1 lists $(h_xh_yh_z)^{1/3}/N$ and a Scotti–Meneveau–Lilly correction for anisotropic grids |
| [Mukha et al. (2025)](/sources/mukha-2025.md), §II.D | from the local Gauss–Lobatto–Legendre spacing, "conservatively" the maximum over the element assigned to the whole element ($N=7$) |
| [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md), §2.1 | not printed; the Eulerian step $\sqrt[3]{\Delta x\Delta y\Delta z}$ is used for the immersed boundary |
| [Brillon & Nadarajah (2026)](/sources/brillon-2026.md), §2.6, Eq. (46) | $\sqrt[3]{\mathrm{Vol}}/(N+1)$ for a flux-reconstruction element of degree $N$ (after Duan & Wang); the test filter of the dynamic model uses degree 3 in place of $N$ (Eq. 58) |
| [Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §II.B, Eq. (42) | average grid spacing $\mathcal J^{1/3}/\prod_i(N_i+1)^{1/3}$ of a DGSEM element (after Komperda et al.), used in the resolvedness sensor; the width of the Smagorinsky comparator is not stated |
| [Caban et al. (2026)](/sources/caban-2026.md), §2, §5.3 | $2h$ or $4h$ for the explicit LES filter on a uniform grid of spacing $h$; the discrete width of a compact filter is where its transfer function equals 0.5 (§3.1) |
| [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md), §2.1, §3.1 | the support width $\Delta_f$ of a compact kernel ($\Delta_f^+=50$–300 a priori), uniform up to the wall; post-processing grid $\Delta_f/16$ |
| [Jakhar et al. (2026)](/sources/jakhar-2026.md), p. 3 | twice the LES grid spacing (Gaussian filter) |
| [Wu & Lele (2026)](/sources/wu-2026.md), §3.2.1 | 16 or 32 DNS spacings ($\Delta/\eta\approx35$ and 70), equal to the LES spacing a posteriori |
| [Tang et al. (2022)](/sources/tang-2022.md), §2.1 | "box-filter width", definition not stated |
| [Volpiani (2024)](/sources/volpiani-2024.md), App. 2 | $(\Delta x\Delta y\Delta z)^{1/3}$, test filter twice that |
| [Valencia et al. (2026)](/sources/valencia-2026.md), §V A | explicit Gaussian filter of width $\Delta=1$, 2 or 4 grid spacings $h$ (filter-to-grid ratio), on a grid itself top-hat filtered at $h$ |
| [Li et al. (2021)](/sources/li-2021.md), §III A, Eq. (17) | discrete top-hat of width $\Delta=16$ DNS spacings ($1024^3$ isotropic DNS, about 5% of the kinetic energy filtered); a posteriori LES spacing $\Delta/2$, so that LES–filtered-DNS differences are "mainly due to" the SGS model |
| [Zhao et al. (2021)](/sources/zhao-2021-c.md), §III.A–B | $(\Delta x_1\Delta x_2\Delta x_3)^{1/3}$, test filter twice the grid filter; directional cell widths in the Vreman model, where "the grids themselves act as the filter" |
| [Pan & Zhang (2023)](/sources/pan-2023.md), §II.B–D | "grid filter scale", not defined beyond the DES grid length $\max(\Delta x,\Delta y,\Delta z)$ of the same paper |
| [Xu et al. (2023)](/sources/xu-2023.md), §2.2, §3.2 | $(\Delta_x\Delta_y\Delta_z)^{1/3}$ in the eddy-viscosity baselines and the original nonlinear model; the learned model replaces it by $\Delta^*=1$ after scaling each gradient by the local grid width in its direction (below) |
| [Maeyama & Kawai (2023)](/sources/maeyama-2023.md), §2.2, Eqs. (2.9)–(2.11) | $f_{\mathrm{an}}(\Delta x\Delta y\Delta z)^{1/3}$ with an anisotropy factor $f_{\mathrm{an}}\ge1$ (the source's $C_w$, not the WALE constant) (below), in the selective mixed-scale model |
| [Zhang et al. (2023)](/sources/zhang-2023-c.md), §3.3 | cube root of the cell volume, also the length of the gradient model of the subgrid scalar variances |

In implicitly filtered LES the filter width and the grid spacing $h$
coincide approximately, $h\approx\Delta$, whereas in explicitly filtered LES
they are chosen independently (Beck & Kurz 2023, §I).

### Explicitly filtered LES and the filter-to-grid ratio

Volpiani (2024, §1) lists the trade-off as reported in the works cited there:
implicit filtering, embedded in the scheme, uses the full grid
resolution and costs nothing, but its size and shape are hard to
determine; an explicit filter applied to the discrete solution has a known
shape and width, separates the numerical errors near the mesh cutoff from
the physics, and converges when its width is held fixed as the mesh is
refined (Radhakrishnan & Bellan), but needs a finer grid (Lund) and lowers
the effective resolution, hence optimized filters. Volpiani's own explicitly
filtered runs apply a relaxation filter to the solution (see
[explicit modal filtering](/methods/explicit-modal-filtering.md) and
[implicit LES](/definitions/implicit-les.md) for the two axes of the
terminology).

Valencia et al. (2026, §II C, Eqs. 17–29) write the explicitly filtered
LES equations of Radhakrishnan & Bellan (as cited there) in compressible
form. The nonlinear advective terms are explicitly filtered, so the
momentum equation carries $\partial_j\overline{\bar\rho\tilde u_i\tilde u_j}$
in place of $\partial_j(\bar\rho\tilde u_i\tilde u_j)$, and the unclosed
stress becomes $\tau^{\mathrm{ef}}_{ij}=\overline{\rho u_iu_j}-\overline{\bar\rho\tilde u_i\tilde u_j}$
(registry §11), with the analogous heat flux; substituting it recovers the
classical filtered equations. With the grid projection written as a
second, implicit filter and assumed to commute with the explicit one, the
total unresolved stress is the sum of a grid-truncation part, which
deconvolution cannot recover, and a subfilter part between grid and
explicit filter, which it can,
$\tau^{\mathrm{tot}}_{ij}=\tau^{\mathrm{gr}}_{ij}+\tau^{\mathrm{sf}}_{ij}$
(registry §11; see
[scale-similarity model](/methods/scale-similarity-model.md)). The
grid-truncation part "can be neglected only when its magnitude is
significantly smaller" than the subfilter part.

Their a priori data (decaying compressible isotropic turbulence, $512^3$
DNS) quantify the split:

- **Grid filter alone** (Table III). Top-hat filtering and downsampling
  keep 99.7%, 98.7%, 95%, 83.6% and 59.1% of the kinetic energy at
  $h/h_{\mathrm{DNS}}=2$, 4, 8, 16, 32 ($256^3$ to $16^3$; $h_{\mathrm{DNS}}$
  page-local).
- **Explicit filter on top** (Table IV). On a given grid the
  grid-truncation energy hardly depends on the filter-to-grid ratio
  $\Delta/h$, while the subfilter energy grows with it; at $\Delta/h=1$ the
  subfilter energy is below the grid-truncation energy, from $\Delta/h=2$
  on it exceeds it. At equal explicit width $\Delta=16h_{\mathrm{DNS}}$,
  15–20% of the energy is unresolved: at $\Delta/h=4$ ($128^3$) 92% of it
  is subfilter, at $\Delta/h=2$ ($64^3$) 72%, at $\Delta/h=1$ ($32^3$)
  about 3.5% (§V B).
- **Spectra** (Fig. 3). Explicit filtering does not move the grid cutoff
  $k_c\approx\pi/h$; it damps energy below it, and at $\Delta/h=1$ the
  spectrum essentially overlaps the implicit-LES one.

They conclude that the filter-to-grid ratio is the decisive parameter of a
closure's accuracy in explicitly filtered LES (§VI).

[Hu et al. (2024)](/sources/hu-2024.md) (§1, §3) state the same contrast
from the side of grid convergence: in implicitly filtered LES numerical
and modelling errors are "fundamentally inseparable", because refining
the grid reduces both, whereas explicitly filtered LES with a fixed filter
width larger than the grid spacing "is known to produce grid-independent
LES solution" (citing Bose et al.; they also recall Lund's finding that
plain refinement improved statistics faster than explicit filtering).
They carry the analogy to wall-modelled LES: holding the wall-model
matching height $h_{\mathrm{wm}}$ fixed during refinement plays the role
of holding the filter width fixed, so the converged solution may depend on
$h_{\mathrm{wm}}$ and its error is wall-modelling error (see
[wall-modelled LES](/methods/wall-modelled-les.md)).

### High-aspect-ratio cells

Abe (2021) isolates the effect of cell anisotropy from wall damping by
testing in the free shear layer behind a [backward-facing step](/benchmarks/backward-facing-step.md)
($Re_\tau=290$ in the driver channel), where the cells are coarse in $x$ and
$z$ ($0.1H$) but fine in $y$ ($\Delta x/\Delta y\sim100$). A priori, the
[Smagorinsky](/methods/smagorinsky-model.md) viscosity with the cube-root
width is "clearly suppressed by the extremely narrow grid width in the
y-direction", and swapping widths between the Smagorinsky model and the
author's mixed model reverses which one is suppressed (§IV C–D, Figs. 9–10).
A posteriori, the mixed model with the cube-root width lengthens the
recirculation bubble (reattachment length $x_R$, registry §11) from $x_R/H=7.19$ to 7.43 against the experimental
6.51 (Table III). The author concludes that "the effect of a grid width in
one direction much smaller than in other directions must be excluded in
determining the filter width" (§V), which agrees with the argument of
Haering et al. (2022, §II C) that the cube root tends to the smallest
spacing. Abe tests only a free shear layer; near-wall treatment "was not
our main concern". The [dynamic procedure](/methods/dynamic-procedure.md)
sidesteps the question by computing $(C_s\Delta)^2$ as one product (Abe
2021, §II A); Prakash et al. (2022, §III) use it for the same reason in
their dynamic mixed model, since "the optimal definition of $\Delta$ for
anisotropic grids is not yet known". The two zonal-DES sources above choose the cube root in
LES regions without a comparison of definitions.

Two sources correct for the anisotropy instead of choosing a
different length. Maeyama & Kawai (2023, §2.2, Eqs. 2.9–2.11) multiply
the cube root by a factor
$f_{\mathrm{an}}=\cosh\sqrt{\tfrac4{27}(c_1^2-c_1c_2+c_2^2)}$ with
$c_1=\log(\Delta_{\max}/\Delta_{\mathrm{med}})$,
$c_2=\log(\Delta_{\mathrm{med}}/\Delta_{\min})$ (all page-local; the
largest, middle and smallest spacings of the cell), in the selective
mixed-scale model of Lenormand, Sagaut & Ta Phuoc (as cited). $f_{\mathrm{an}}=1$ on
a cube; reading $\log$ as the natural logarithm, for a cell with two
spacings ten times the third it is about 1.42, which lifts the width
from $4.64\Delta_{\min}$ to about $6.59\Delta_{\min}$, still below the
largest spacing $10\Delta_{\min}$ *(compiler check, not in the sources)*. [Xu et al. (2023)](/sources/xu-2023.md)
(§3.2, Eqs. 3.27–3.30) blame the near-wall weakness of their
nonlinear algebraic model on the isotropic cube root, since
$\Delta_y\ll\Delta_x,\Delta_z$ near the wall, and instead multiply each
velocity and temperature gradient by the local grid width in its
direction, $\partial/\partial(x_j/\Delta_j)$, building the strain,
rotation and invariants from these normalized gradients with a unit
length scale. A priori, the normalization raises the correlation of the
dynamic version most for $y^+<50$ (Fig. 8), and the learned version
generalizes to untrained grids, which the authors attribute to the grid
information "inherently embedded" in its inputs (§4.1, §5; see
[neural-network SGS models](/methods/neural-network-sgs-model.md)).

[Zhou & Bae (2024)](/sources/zhou-2024-b.md) (§3.3, Figs. 17–20) test
the cube-root width a posteriori in wall-modelled LES of the
[Gaussian bump](/benchmarks/gaussian-bump.md): with cells of aspect ratio
$\Delta_x:\Delta_y:\Delta_z=4:1:2$ at the cell volume of the isotropic
meshes, the separation prediction degrades for the models that use the
cube root (the [Vreman model](/methods/vreman-model.md), most for its
constant 0.025, and the [mixed similarity model](/methods/scale-similarity-model.md)),
while the [anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md),
built on directional spacings, is barely affected. The authors explain
this by the cube-root width, which they call adequate for isotropic but
error-prone for anisotropic cells (§3.3).

### Element methods

In discontinuous Galerkin LES, Basile et al. (2023, §3.2) note two cutoff
wavenumbers, that of the mesh and that of the full discretization, with the
modal spectrum inside an element covering the scales between them; they
build a smoothness indicator on it (see
[mesh adaptation](/methods/mesh-adaptation.md)). They attribute spurious
peaks in centreline rms profiles on coarse elements partly to DG
inter-element discontinuities, recalling an a priori study by Beck et al.
in which filtered DNS projected on a DG/LES grid is itself discontinuous at
element interfaces (§4.2.3, Fig. 10). In the continuous spectral element
method the velocity is continuous across elements but its gradient is not;
on coarse meshes [Gillyns et al. (2022)](/sources/gillyns-2022.md) (§2, §6,
§8) see Gibbs spikes in the fluctuation statistics at element boundaries,
which vanish as the mesh approaches DNS resolution and which they use as a
reference-free mesh-quality indicator. Their subgrid model is Nek5000's
approximate deconvolution model (see
[scale-similarity models](/methods/scale-similarity-model.md)).

## Commutation and discretization terms

Beck & Kurz (2023, §I, Eqs. 1–5) decompose the unclosed terms of the
filtered inviscid Burgers equation $\partial_tu+\tfrac12\partial_x(u^2)=0$
into three parts:

- a **commutation error** $C_1=\partial_x\overline{u^2}-\overline{\partial_x u^2}$,
  nonzero when $\Delta=\Delta(x)$ varies or is anisotropic, and present even
  for linear advection;
- the classical subfilter term $C_2=\partial_x(\bar u\bar u)-\partial_x\overline{u^2}$,
  the one-dimensional analogue of $-\partial_j\tau_{ij}$;
- a **discretization term**
  $C_3=\delta_x(\bar u\bar u)-\partial_x(\bar u\bar u)$, with $\delta_x$ the
  discrete derivative, which in the form of Geurts & van der Bos (cited
  by Beck & Kurz) is the divergence of a "computational subgrid stress"
  built with the numerically induced filter.

For $\Delta\approx h$ the computational term can be considerably larger than
the classical term, and for nonlinear schemes (upwinding, limiters,
reconstructions) it depends on the solution and cannot be determined a
priori (Beck & Kurz 2023, §I). This motivates the
[discretization-consistent closure](/definitions/discretization-consistent-closure.md).

Agdestein & Sanderse (2025, §3.2, Eqs. 11–12) make the same point in
discrete form: filtering the discrete DNS with a discrete filter $\Phi$ gives
an exact equation for $\Phi u$ whose closure term, the discrete commutator
error, contains both the subfilter effect and the coarse-grid
discretization error. Discrete filters do not in general commute with the
discrete divergence; their face-averaging filter does, which is the basis of
the [divergence-consistent LES](/methods/divergence-consistent-les.md).
[van Gastelen et al. (2024)](/sources/vangastelen-2024.md) (§2.3–2.4,
Eqs. 15–24) take the same "discretize first, filter next" route in 1D: a
discrete cell-average filter $\mathbf W$ with the piecewise-constant
reconstruction as right inverse, so that the closure term
$\mathbf Wf_h(\mathbf u)-f_H(\bar{\mathbf u})$ ($f_h$, $f_H$ the fine and
coarse discrete right-hand sides, page-local) is the discrete commutator
error and includes the coarse discretization error. With this pair the
discrete energy and momentum split exactly between resolved and subgrid
parts (Eqs. 28, 31; see [energy backscatter](/definitions/energy-backscatter.md)).
The price is a closure tied to the compression factor between the grids
(§5).
Haering et al. (2022, §II A, §IV) treat their active forcing term as a model
of the commutator between the implicit filter and the substantial
derivative.
Najafiyazdi et al. (2023, §3.1, Eq. 18) state that any differential
filter discretized on a non-uniform or unstructured grid loses the
commutation property, even in one dimension, because the filter width
varies in space; the commutation error vanishes only for a constant
width, so the filter commutes only in its continuous form on uniform
grids.

**Filters induced by derivatives and interpolation.** Caban et al. (2026,
§3.2, Eqs. 24–35, Fig. 3) write the discrete $r$-th derivative as a filter
$\mathcal F_h^{(r)}$ applied to the exact one,
$\delta^{(r)}_xf=\mathcal F_h^{(r)}*\partial^{(r)}_xf$ (registry symbol for
their $\mathcal G_I^{(r)}$); its transfer function is the ratio of the
discrete to the exact derivative, the modified wavenumber over the
wavenumber for $r=1$ (Eqs. 25, 28–29). For FD2, CD6 and CD10 its physical
kernel is non-zero over the whole periodic stencil, so every induced
filter couples all nodes (Fig. 3). In the semi-discrete
convection–diffusion equation (Eqs. 26–27) the first-derivative filter
only scales the phase speed, leaving mode amplitudes unchanged, while the
second-derivative filter sets a numerical viscosity
$\nu\hat{\mathcal F}_h^{(2)}\le\nu$, a slower decay; the authors note that
with time integration included, global spectral analysis can show an
effective viscosity above $\nu$ (§3.2.1). On their half-staggered grid the
pressure projection interpolates velocities to half nodes and back: two
second-order interpolations equal the trapezoidal filter
$\tfrac12+\tfrac12\cos(kh)=\cos^2(kh/2)$ (the paper's scaled wavenumber
$\omega$ is $kh$), and the authors state the
same squaring for higher-order compact interpolation (§3.2.2, Eqs. 34–35).
Their effective numerical filter is the product of the first-derivative
and squared interpolation filters, an approximation, since "no single
filter" represents the first- and second-derivative filters jointly
(§4.1, Fig. 5). They build it into the deconvolution of the
[approximate deconvolution model](/methods/scale-similarity-model.md),
where it helps only for a low-order LES filter (§5.4.2), and they restrict
the interpolation results to staggered or half-staggered algorithms:
collocated kinetic-energy-conserving schemes lack this dissipation (§6).
See [discretization-consistent closure](/definitions/discretization-consistent-closure.md)
and [implicit LES](/definitions/implicit-les.md).

[Luckring & Rizzi (2024)](/sources/luckring-2024.md) (§2.4.1.2), in a
survey of vortex aerodynamics, state the practical consequence after
Ghosal (cited): for low-order discretizations "the truncation error can be
the same order as the subfilter scale contributions, unless the cell size
is considerably smaller than filter width Δ". [Xiao et al. (2025)](/sources/xiao-2025.md)
(§1) state that the subgrid stress of implicitly filtered LES differs from
the filtered-Navier–Stokes stress, above all when the grid is much coarser
than the Kolmogorov scale, "as the numerical and modeling errors can then
be comparable" (see [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

## Gauge freedom of the subgrid stress

The resolved equations depend on $\tau_{ij}$ only through its divergence.
Vela-Martín (2022, §3, Eqs. 3.1–3.5), following an idea attributed to
Jiménez (2016), adds to $\tau_{ij}$ any symmetric divergence-free tensor
without changing the resolved dynamics. The total SGS term in the resolved
energy equation and the domain-averaged flux are invariant, but the local
split between the interscale flux $\Pi=-\tau_{ij}\bar S_{ij}$ and a
conservative spatial flux is not. The consequence drawn by the author is
that a model must reproduce the divergence of the stress, not the stress,
and that a poor a priori correlation between a model stress and the filtered
DNS stress is not by itself evidence of poor modelling: equivalent stress
representations correlate with one another only at 0.4–0.6 (§6.3, §8). See
[energy backscatter](/definitions/energy-backscatter.md).

## Resolution and the resolved fraction

Haering et al. (2022, §III B, Eqs. 9–10) use a triple decomposition
$u_i=\langle u_i\rangle+u_i^>+u_i^<$ (mean, resolved fluctuation, subgrid
fluctuation) with a filter that leaves the mean unchanged,
$\bar u_i=\langle u_i\rangle+u_i^>$, and write $\tau_{ij}$ as cross and
subgrid–subgrid products of $u^>$ and $u^<$. Their computable measure of
resolution is the unresolved fraction $1-k_{\mathrm{res}}/k_{\mathrm{tot}}$;
citing Jiménez & Moser, they recall that "for typical LES" this fraction is
expected to stay below about 0.1 over the entire domain "for the model to
perform well", and report that their hybrid model keeps a correct mean in
channel flow "well past this threshold", with the fraction as low as 0.4
at the channel centre on their finest grid (§V A 1).
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md)
(§III.1, p. 13) use the same figure descriptively to separate LES from
very-large-eddy simulation (VLES): "almost all of the LES studies are
designed to model about less than ten percent of the total kinetic energy",
and they mark the larger filter sizes of their a priori study as the VLES
region; a posteriori they test a filter five times wider than their LES one
there (§IV), and report that their model gives "promising results in the
VLES region as well as the LES region" (abstract). They do not print the
formula of the modelled-energy percentage.
[Helm & Martín (2022)](/sources/helm-2022.md) (§III B, Fig. 5; §V) run
compressible boundary layers with more modelled energy. Estimated from
filtered against unfiltered DNS as a fraction of the local DNS value, the
unresolved share of the turbulent kinetic energy at Mach 7 is "14% to 25%,
namely, 25% at the wall and in $z/\delta>0.7$, otherwise it is about 14%"
(§III B, which in the next sentence gives a maximum of 18% at the wall;
§V: about 25% at the wall and 12% over most of the layer), and between 10%
and 15% at Mach 3 and 10. As a direction for further savings, the authors
state that the a priori study of Martín et al. indicates that "maintaining
25%–30% TKE in the SGS throughout the boundary layer may be possible" for
their LES method (§V).
[Blind et al. (2023)](/sources/blind-2023.md) (§1) review measures of how
well an LES is resolved: the ratio of subgrid to viscous dissipation is
meaningful only in the buffer layer; the ratio of modelled to resolved or
total energy, proposed by Jiménez & Moser and by Pope (as cited), "has been
found to correlate poorly to the known behavior of length scales in
wall-bounded flows" (citing Toosi & Larsson); local-spectrum estimates fail
beyond isotropic flows. They call the LES modelling-residual estimate of
Toosi & Larsson "the most well-grounded approach to date" and use it for
[mesh adaptation](/methods/mesh-adaptation.md); they add that the residual
cannot be estimated by Taylor expansion or by interpolation on a finer
grid, because an LES is far from the asymptotic range and a finer grid
carries smaller scales (§2.2).
[Wang et al. (2024)](/sources/wang-2024.md) (§3.3, Table 2, Figs. 5–6)
find in LES of the [periodic hill](/benchmarks/periodic-hill.md) that
first-order statistics are nearly grid-insensitive while second-order
statistics and the terms of the turbulent-kinetic-energy budget are not:
"the higher the order of the statistics, the more challenging" on the same
grid. They use a significant imbalance of the budget as an indicator of
insufficient resolution (see [numerical dissipation](/properties/numerical-dissipation.md)).
[Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) (§3.2)
recall, for the periodic hill, wall-resolved LES spacings of
$\Delta x^+\approx50$–100, $\Delta y^+\approx1$, $\Delta z^+\approx15$–30,
and place their implicit-LES meshes between these and DNS.
In forced two-dimensional turbulence Jakhar et al. (2026, p. 4) find
their gradient-type closures long-term stable only when the LES resolves
more than 80% of the DNS enstrophy, and compare this with the 3-D rule,
which they cite from Pope, that LES should resolve at least 80% of the kinetic
energy (see [gradient model](/methods/gradient-model.md)).
[Pan & Zhang (2023)](/sources/pan-2023.md) (§III.B, Eq. 23, Fig. 6)
evaluate the modelled fraction $k_{\mathrm{sgs}}/(k_{\mathrm{res}}+k_{\mathrm{sgs}})$
of their impeller LES: largest in the separated shear layers at the blade
leading edges and "rather small" in the through-flow. They justify it by
a statement they attribute to Pope (2000): "the modeled turbulent kinetic
energy could reach as high as 80% of the overall fluctuating kinetic
energy". The two attributions to Pope are recorded as printed by each
source; Pan & Zhang do not define $k_{\mathrm{sgs}}$.
[Ahn et al. (2023)](/sources/ahn-2023.md) (§IV C 1, Fig. 12) take a
velocity spectrum following the $-5/3$ slope "for about one order of
magnitude" in the jet shear layer as a sign that their implicit LES grid
resolves a large part of the inertial range, with a rapid drop at high
Strouhal number marking the grid and scheme limit.
The grid counts needed for wall-resolved and
wall-modelled LES are on [LES grid-point requirements](/results/les-grid-point-requirements.md),
and the near-wall alternative on [wall-modelled LES](/methods/wall-modelled-les.md).

**LES or very-large-eddy simulation.** [Wu et al. (2023)](/sources/wu-2023-b.md)
(§2.1.1) cite Pope's definition of very-large-eddy simulation, a filter and
grid "too coarse to resolve 80% of the energy", to rename Han et al.'s
"VLES" as self-adaptive turbulence eddy simulation, since its runs resolve
"larger than 90%" of the turbulent kinetic energy even on coarse grids (see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)). Their motivation is
cost: they cite a wall-resolved LES of a three-element airfoil at
$Re_c=1.23\times10^6$ that used 2.6 billion cells and 6 million CPU hours
(§1). [Fureby & Nilsson (2023)](/sources/fureby-2023.md) (§6.2) use the
resolved fraction of the turbulent kinetic energy as their grid criterion:
90%, 94% and 96% on 7.3, 24.6 and 57.8 million cells, "rendering all grids
appropriate for LES" by the criteria they cite from Pope and from Matheou
& Chung, whose thresholds they do not print.
[Zhang et al. (2023)](/sources/zhang-2023-c.md) (§2, Eqs. 1–2, Fig. 2b)
qualify the 3.87-million-cell mesh of a stratified-burner LES with the
time-averaged modelled fraction
$M_E=\big\langle k_{\mathrm{sgs}}/(k_{\mathrm{sgs}}+k_{\mathrm{res}})\big\rangle$
($M_E$ page-local, named the Pope criterion and defined after Boudier et
al., cited), $k_{\mathrm{res}}$ built from the resolved fluctuation about
the time mean and $k_{\mathrm{sgs}}$ from the dynamic Smagorinsky model.
On the cold flow $M_E$ is "generally below 0.2" in the region of
interest, so "at least 80%" of the turbulent kinetic energy is resolved.

**Activity parameter.** [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md)
(App. C, Eqs. C1–C3, Figs. 28–29) rate their canopy LES with the subgrid
activity parameter of Geurts & Fröhlich, which they cite,

$$s_a=\frac{\varepsilon_{\mathrm{sgs}}}{\varepsilon_{\mathrm{res}}+\varepsilon_{\mathrm{sgs}}},\qquad
\varepsilon_{\mathrm{res}}=\nu\,\bar S_{ij}\partial_j\bar u_i,\quad
\varepsilon_{\mathrm{sgs}}=\nu_t\,\bar S_{ij}\partial_j\bar u_i ,$$

($s_a$, $\varepsilon_{\mathrm{res}}$, $\varepsilon_{\mathrm{sgs}}$
page-local; $s_a$ denotes the activity parameter in each of the forms
below).

- **Range.** $s_a$ is 0 for DNS and 1 for LES at infinite
  Reynolds number. For eddy-viscosity models it reduces to
  $\nu_t/(\nu_t+\nu)$ (Celik et al., cited by Löhrer & Fröhlich).
- **Values.** In their run the mean is 0.11, the 95th percentile about
  0.23 and the local maximum about 0.3.
- **The authors' reading.** They call the run "a high-resolution LES …
  close to a DNS". The subgrid share of the mean drag is below the viscous
  one everywhere.
- **Caveat.** Their $\nu_t$ is damped near the immersed blades with the
  immersed-boundary delta kernel (§2.3). Since
  $s_a\approx\nu_t/(\nu_t+\nu)$ grows with $\nu_t$, this damping
  lowers $s_a$ there *(compiler check, not in the sources)*.

[Rismondo et al. (2025)](/sources/rismondo-2025.md) (§3, Fig. 8c) use the
same quantity informally. A ratio $\nu_t/\nu$ mostly between 0 and 10 in a
wall-resolved wind-turbine LES is, for them, an indication of high
resolution; they report no grid-convergence study.

[Zhou & Bae (2024)](/sources/zhou-2024-b.md) (§3.1, Fig. 11) use the
activity parameter in the form
$s_a=\langle\Pi\rangle/(\langle\Pi\rangle+\langle\varepsilon_\nu\rangle)$
with $\Pi=-\tau_{ij}\bar S_{ij}$ the full subgrid dissipation and
$\varepsilon_\nu=2\nu\bar S_{ij}\bar S_{ij}$ ($\varepsilon_\nu$
page-local), citing Lozano-Durán & Bae and Geurts & Fröhlich, "constrained
to values between 0 and 1". In wall-modelled LES of a separated bump
flow subgrid dissipation dominates the boundary layer for the mixed and
AMD models, is comparable to the viscous one for Vreman with constant
0.025, and drops in the wall-adjacent cells for dynamic Smagorinsky. For
an eddy-viscosity model the two forms coincide, since then
$\Pi=2\nu_t\bar S_{ij}\bar S_{ij}$ and Löhrer & Fröhlich's
$\bar S_{ij}\partial_j\bar u_i=\bar S_{ij}\bar S_{ij}$ *(compiler check,
not in the sources)*.

**Resolved fractions in reacting LES.** Three reacting-flow sources
judge resolution by a resolved fraction rather than by grid convergence:

- [Wei et al. (2023)](/sources/wei-2023.md) (§III B, Eq. 34, Fig. 6)
  compute $\langle u_i''u_i''\rangle/(\langle u_i''u_i''\rangle+2k_{\mathrm{sgs}})$
  in a supersonic boundary layer and report that 99.5% of the cells
  resolve more than 80% of the turbulent kinetic energy, the remainder
  lying in the viscous sublayer; they attribute the criterion to Pope
  (cited).
- [Vignat et al. (2024)](/sources/vignat-2024.md) (§3.1) state that most
  injector jets of their detonation-engine LES have a subgrid share of the
  turbulent kinetic energy below 20%, "as recommended by Pope", from
  single-injector side simulations whose results are not shown.
- [Nmira et al. (2023)](/sources/nmira-2023.md) (§3.1, §3.4) resolve "on
  the whole more than 80% of temperature variance" in LES of buoyant
  sooting flames (figure in supplementary material, not in the file read),
  and still find that neglecting the subgrid fluctuations in the emission
  term over-predicts the mean and r.m.s. soot volume fraction by a factor
  of about 2.

**Wall-resolved criteria and spanwise extent.**
[Baldan & Guardone (2025)](/sources/baldan-2025.md) (§1.1, §2.1, Figs. 3–8)
verify the wall-resolved LES targets $\Delta x^+<40$, $\Delta y^+<5$,
$\Delta z^+<20$ of Piomelli & Balaras and Georgiadis et al., which they cite,
on a pitching NACA 0012 in deep dynamic stall at $Re_c=1.35\times10^5$.
Their grids have 62.7 to 374.7 million nodes. With spanwise-periodic
domains of 0.2, 0.4, 0.8 and 1.2 chords:

- the attached upstroke is span-insensitive ($C_L$ within 0.05);
- once the dynamic-stall vortex forms, the two short spans force a
  quasi-two-dimensional vortex and spurious downstroke lift peaks;
- 0.8 and 1.2 chords still differ at $10^\circ$ in the downstroke.

They conclude that the span must be at least one chord when structures of
chord size occur. Results obtained with the spans of 0.1 to 0.2 chord
reported in the literature "can be accepted only in the attached flow
region" (§3; the introduction quotes 5% to 20% of the chord). See
[NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md).

In element methods the same targets are quoted per element and degree:
[Gao et al. (2022)](/sources/gao-2022.md) (§5.1, Table 2) run their
wall-resolved DGSEM LES of a Mach 2 boundary layer with $N=6$ and
$\Delta x^+=30$, $\Delta y^+_{\min}=1.6$, $\Delta z^+=16$ at the reference
station, "in combination with $N=6$", without saying whether the
spacings are per element or per degree of freedom.

**Coarse-grained simulation, and the label "wall-resolved".**
[Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) (§I) use
coarse-grained simulation (after the volume edited by Grinstein, cited) as
the umbrella term: the large energy-containing structures are resolved,
the smaller ones filtered and their effect modelled, either by an explicit
subgrid model or by the shock-capturing scheme of an
[implicit LES](/definitions/implicit-les.md). Their production mesh for a
shock-induced panel-buckling interaction has $\Delta x^+=717$,
$\Delta z^+=634$ and a first point at $y^+=4.8$, while the wall-resolved
guidance they quote is $\Delta x^+\approx50$–130, $\Delta z^+\approx15$–30,
10–30 points across the boundary layer and a first point at $y^+\lesssim1$
(§III B 2); they judge it "adequately accurate, at least concerning the
flow properties of interest", against a finer mesh at $\Delta x^+=268$,
$\Delta z^+=100$ (see [LES grid-point requirements](/results/les-grid-point-requirements.md)).
At the other end, [Shi & Yan (2023)](/sources/shi-2023.md) (§I, §IV,
Table I) call their no-model flux-reconstruction run of a Mach 2.9
compression ramp a "wall-resolved large eddy simulation" within the
implicit-LES framework, on grids with $\Delta y_1^+=0.33$–0.50,
$\Delta x^+_{\min}=3.3$–5.0 and $\Delta z^+=4.69$, against
$0.2$/$3.4$/$4.1$ for the DNS of Wu & Martin that they tabulate beside
them (counted in degrees of freedom).

**Very coarse LES.** [Maejima & Kawai (2025)](/sources/maejima-2025.md)
(§1, §4.1, §5.3) define very-coarse-grid LES as LES in which even the
energy-containing near-wall eddies are under-resolved. In channel flow at
$Re_\tau\approx1000$ this means $(\Delta x^+,\Delta z^+)\approx(72,36)$,
two to three points per streak spacing. There the resolved field is itself
non-physical, and its statistics differ from filtered DNS
("fDNS ≠ vLES"). A model trained on filtered-DNS input therefore meets a
different input distribution in the LES. Their pipeline first maps the LES
field to a filtered-DNS-like field without paired data; see
[super-resolution SGS models](/methods/super-resolution-sgs-model.md).

**What the subgrid viscosity does below the matching height.**
[Maeyama & Kawai (2023)](/sources/maeyama-2023.md) (§5.3–5.4, Eq. 5.5,
Fig. 17; Apps. C–D) show that the wall-stress-modelled LES of a
supersonic boundary layer, whose grid does not resolve the near-wall
streaks, still holds coherent streak-like ejection–sweep pairs below the
matching height, about eight grid points per spanwise wavelength and
fixed in outer units. Their spanwise length scale collapses at
$Re_\tau\approx700$–14 000 only when the viscous length of semi-local
scaling is built with the molecular plus the subgrid eddy viscosity,
$\delta^{*,\mathrm{sgs}}_\nu=(\nu+\nu_t)/u_\tau^*$ (registry §11), so that "the diffusion introduced by the SGS eddy
viscosity dominantly determines" it; the collapse holds for other grids,
another scheme and the [Smagorinsky](/methods/smagorinsky-model.md)
model. See [wall-modelled LES](/methods/wall-modelled-les.md).

**Grid convergence of a supersonic boundary layer.** [Wang et al. (2024c)](/sources/wang-2024-j.md)
(§III.A–B, Table I, Figs. 1–2) run wall-resolved LES of a spatially
developing boundary layer at $M_\infty=2.0$, $Re_\delta\approx13\,500$
(on the inflow thickness) with a dynamic Smagorinsky–Yoshizawa model and
seventh-order WENO on three grids, $209\times161\times81$,
$321\times201\times161$ and $649\times201\times161$ over
$30\delta_0\times6\delta_0\times3.7\delta_0$ ($\delta_0$ the inflow
thickness, page-local), all with first-cell height $\Delta y^+_w=0.8$.
Only the finest grid matches the DNS of Pirozzoli et al. (cited) in van
Driest-transformed mean velocity and density-scaled Reynolds stresses;
the two coarser grids over-predict the streamwise normal stress and
slightly under-predict the shear stress, while below $y^+=7$ all runs
follow the wall law. No streamwise or spanwise spacing in wall units and
no friction Reynolds number are printed. The coarsest grid is the one on
which they compare hybrid models (see
[log-layer mismatch](/definitions/log-layer-mismatch.md) and
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md)).

**Grid estimates for aircraft and the Reynolds-number reach of wall-resolved LES.**
Luckring & Rizzi (2024) quote the grid estimate of Larsson et al. (cited)
for LES of the upper surface of a NACA 0012 at $M=0.1$, $\alpha=2.5^\circ$:
$1.6\times10^7$, $1.9\times10^9$ and $2.0\times10^{11}$ points in the inner
layer ($y/\delta<0.2$) and $3.3\times10^7$, $7.2\times10^7$ and
$2.5\times10^8$ in the outer layer at $Re_c=10^6$, $10^7$ and $10^8$
(§2.4.1.4, Table 1), about 33 billion points at $Re_c=4\times10^7$. They
state that wall-resolved LES is "currently restricted to low Reynolds
numbers (on the order of $10^4$)" (§3.1.1.2, §4.1.1), and that WMLES lacks
"well-established guidelines" for grid resolution, cell topology, schemes
and subgrid modelling (§2.4.1.4; see
[wall-modelled LES](/methods/wall-modelled-les.md)). Their survey uses LES
for wall-resolved LES throughout (see
[delta-wing vortex flows](/benchmarks/delta-wing-vortex-flow.md)).

## History and scope (inline)

[Kim & Leonard (2024)](/sources/kim-2024-b.md), a history of DNS and LES
from 1971 to the early 1990s by two participants (RANS excluded), record
these milestones, all cited there:

- **Name and equations.** The term LES was "first coined by William
  Reynolds at Stanford" (§2.5); Reynolds, Ferziger and Leonard were, to
  the authors' knowledge, the first to use it (§3.1). Leonard (1973, 1974)
  derived the LES equations by filtering the Navier–Stokes equations
  (§3.1; the deterministic term of that derivation is on the
  [gradient model](/methods/gradient-model.md) page).
- **First channel LES.** Deardorff (1970) used 6,720 grid points, a
  log-law wall condition and Arakawa differencing; Schumann (1975) up to
  65,000 volumes on anisotropic grids with a subgrid energy equation;
  Moin et al. (1978) the first LES with the wall region computed
  (§2.5, §3.1). Moin & Kim (1982) added Van Driest-like damping to the
  [Smagorinsky model](/methods/smagorinsky-model.md) (§3.4).
- **Numerics.** The authors call it "an important realization" that the
  formal accuracy of the discretization should be higher than that of the
  subgrid model, and that the inviscid discrete equations should conserve
  energy for long-term stability (§4.7; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
- **Premise.** A universal subgrid model presumes that all
  energy-containing scales are resolved; many practical LES do not
  resolve all large-scale motions, so the subgrid model must account for
  some flow-dependent motions (sidebar "Large-Eddy Simulations").
- **Present use.** A well-designed LES, "especially wall-modeled LES", can
  now be used as a design tool for high-lift aircraft, citing Goc et al.
  (2021) (§5; see [wall-modelled LES](/methods/wall-modelled-les.md)).

Two reviews place LES among other approaches.
[Chen et al. (2024b)](/sources/chen-2024-c.md) (§4.1) criticize
conventional subgrid closures, which they call top-down and, after
Kerstein, "parameterization", for relying on subgrid isotropy, which fails near walls where turbulence is not
homogeneous, and hybrid RANS/LES for an empirical RANS–LES interface;
they offer [one-dimensional turbulence](/methods/one-dimensional-turbulence.md),
coupled to LES as LES-ODT or ODTLES, as an alternative closure.
In passing, [Sabnis & Babinsky (2023)](/sources/sabnis-2023.md) (§3–§5) survey LES of
three-dimensional shock/boundary-layer interactions (swept corners and
fins, ducts, fenced ramps) beside RANS and experiments; see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
In the hybrid model SATES of [Wu et al. (2024)](/sources/wu-2024.md)
(§2.1) LES is one of three self-selected modes, between URANS and DNS (see
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md)).

## Other uses of the filter idea

- [Pereira et al. (2021)](/sources/pereira-2021.md) (§III, Eqs. 13–16) write
  the [PANS](/methods/partially-averaged-navier-stokes.md) decomposition as
  a filter with a resolved and a density-weighted resolved part, which
  reduces to Reynolds and Favre averaging in the RANS limit; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md).
- [Liu et al. (2022)](/sources/liu-2022.md) (§1) treat the scales resolved
  by a cosmological MHD simulation as the mean field of mean-field
  electrodynamics, with dissipation provided by truncation errors, and close
  the unresolved induction with a
  [subgrid turbulent dynamo model](/methods/subgrid-turbulent-dynamo-model.md);
  see [implicit LES](/definitions/implicit-les.md).
- **Temporal LES started from RANS.** Bouhafid et al. (2024, §2.1, §4.1)
  extract a cross-flow slice of a steady RANS solution of a full aircraft,
  extrude it over one Crow wavelength into a periodic box fixed in the
  ground frame and continue it as a temporal LES of the wake (160 million
  cells), with initial fluctuations rescaled cell by cell to the RANS
  Reynolds stresses (see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
  [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) (§1) note that
  few LES of transonic buffet exist because 3D LES is costly, which
  motivates their PANS study (see
  [PANS](/methods/partially-averaged-navier-stokes.md)).
- **Learning the filtered dynamics instead of the stress.**
  [Neural-operator surrogates](/methods/neural-operator-les-surrogate.md)
  learn the time advance of the filtered velocity on the LES grid and
  replace the solver, not the closure.
  - Li et al. (2024, §IV) train on filtered DNS.
  - Zhao et al. (2025, §2.5) train on the residual of the
    Smagorinsky-closed filtered equations. They state that, to their
    knowledge, the LES equations had not been used as the constraint of
    such a network for 3D turbulence.
- **Grid filtering of diffusion flames.** [Cuenot et al. (2022)](/sources/cuenot-2022.md)
  (§1, §2.2) use the grid filter as the LES filter and draw a consequence
  for non-premixed combustion: grid filtering lowers the resolved strain
  rate and numerical diffusion adds to the physical one, so a diffusion
  flame, which has no intrinsic thickness, thickens on an LES grid by
  itself; see [thickened flame model](/methods/thickened-flame-model.md).
  [Böttler et al. (2022)](/sources/bottler-2022.md) (§4) leave the LES
  closure of their laminar
  [flamelet tabulation](/methods/flamelet-tabulated-chemistry.md)
  (turbulence–chemistry interaction) to future work.
- **LES in a rotating frame.** Rismondo et al. (2025, §2.1, Eq. 2.2) write
  the filtered incompressible equations in a multiple reference frame,
  with Coriolis and centrifugal terms acting on the filtered inertial
  velocity. The LES feeds a
  [Ffowcs Williams–Hawkings](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)
  computation of wind-turbine noise.
- **Filtering in time.** [Simonis et al. (2022)](/sources/simonis-2022.md)
  (§2.1, Eqs. 1–6, citing Oberle, Pruett & Jenny and Pruett)
  filter the incompressible equations in time with a causal exponential
  kernel of width $\Theta$ (registry §11): $\partial_t\bar\phi=(\phi-\bar\phi)/\Theta$.
  The filter inverts exactly, $\phi=\bar\phi+\Theta\,\partial_t\bar\phi$
  ("direct deconvolution"), and the temporal residual stress obeys the
  closed relaxation equation
  $$\partial_t\tau_{ij}=-\frac{\tau_{ij}}{\Theta}+\Theta\,\partial_t\bar u_i\,\partial_t\bar u_j,$$
  so no model constant appears beyond $\Theta$. They advance this stress
  inside a multiple-relaxation-time lattice Boltzmann scheme (see the
  [lattice Boltzmann method](/methods/lattice-boltzmann-method.md)), with
  $\Theta=10\Delta t$ chosen on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  at $Re=800$; at $Re=3000$ the temporal LES recovers the dissipation peak
  better than under-resolved simulation on $64^3$ and $128^3$ (§3.2–3.3,
  Figs. 2–8). Both updates are local in space, trading storage of earlier
  time levels for non-local filtering (§2.4, §4). They monitor the subgrid
  activity $s_a=\lvert\epsilon_{\mathrm{mod}}\rvert/\lvert\epsilon_{\mathrm{tot}}\rvert$
  that they cite from Geurts & Fröhlich, the share of the total dissipation not
  accounted for by the resolved enstrophy, which decreases with refinement
  (§3.4, Eq. 29, Fig. 9).
- **Scale separation by projection.** In the
  [variational multiscale method](/methods/variational-multiscale-method.md)
  the resolved scales are the finite-element field and the unresolved ones
  a residual-driven correction, with no filter kernel
  ([Chen et al. 2022](/sources/chen-2022-g.md), §2.3;
  [Kang & Masud 2022](/sources/kang-2022.md), §3.4).
- **Filtering after the solve.** [Svärd (2022)](/sources/svard-2022.md)
  (§1, §2.2–2.3, §6) contrasts LES, which "applies a filter a priori", with
  weakly convergent numerical solutions, whose averages against a fixed
  test function converge on grids too coarse for point values and are read
  as filtered quantities a posteriori. The author separates fixed-width LES,
  whose grid-converged solution solves the filtered equations, from
  "vanishing LES" with $\Delta\propto h$ and from ILES, which both aim at a
  DNS; see [implicit LES](/definitions/implicit-les.md).

- **Rotor models in LES.** [Stanly et al. (2022)](/sources/stanly-2022.md)
  run an [actuator line](/methods/actuator-line-model.md) in a high-order
  implicit LES whose only closure is an eighth-order artificial-dissipation
  operator, and suggest that the coarse grids their filtered actuator line
  allows would suit explicit subgrid models better than implicit LES (§6).
  [Zhang et al. (2022e)](/sources/zhang-2022-i.md) (§II A) run wall-modelled
  LES of a neutral atmospheric boundary layer over a hill in
  [LESGO](/software/lesgo.md), with Smagorinsky and wall damping, a log-law
  wall stress, an [immersed boundary](/methods/immersed-boundary-method.md)
  terrain and an actuator disk.
- **A two-scale alternative.** [Idelsohn et al. (2024)](/sources/idelsohn-2024.md)
  (§1.4, §4) replace the subgrid model by fine-scale stresses from off-line
  DNS of representative volume elements and claim, from single coarse-mesh
  comparisons, better agreement than LES on coarse and medium meshes and
  that LES methods "do not comply with the self-similarity property or the
  averaged symmetry over the time of the flow"; see
  [pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md).
- **Functional and structural models.** [Wang et al. (2022)](/sources/wang-2022-j.md)
  (§I) divide SGS models into functional (eddy-viscosity: Smagorinsky,
  dynamic Smagorinsky, Vreman) and structural (similarity, gradient,
  deconvolution) ones, the latter more highly correlated with the true
  stress but needing extra treatment for stability; they filter with a
  Gaussian kernel and use a filter-to-grid ratio of 2 to limit numerical
  errors (§II, Eq. 8; see
  [gradient model](/methods/gradient-model.md)).

## Explicit models offered by codes

The software paper of the [HORSES3D](/software/horses3d.md) DG code
([Ferrer et al. 2023](/sources/ferrer-2023.md), §4.1) describes explicit
LES as resolving the large eddies and modelling the small ones, and lists
the [Smagorinsky](/methods/smagorinsky-model.md),
WALE (Nicoud & Ducros, as cited) and [Vreman](/methods/vreman-model.md)
models with the group's SVV-Smagorinsky combination (see
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md));
no formula is printed (the [WALE page](/methods/wale-model.md) has the
formula from other sources). The GPU
spectral-element code NekRS (see [Nek5000 and NekRS](/software/nek5000.md))
is benchmarked by [Fischer et al. (2022)](/sources/fischer-2022.md)
(§4.1, Table 2) on a spacer-grid LES at $Re_D=14\,000$ with 3.2 million
elements and $N=7$, without stating the subgrid model. The capsule-wake
LES of [Placco et al. (2023)](/sources/placco-2023.md) has no explicit
model (see [implicit LES](/definitions/implicit-les.md)).

Further explicit closures in this bundle's applications:

- [WALE](/methods/wale-model.md) in the second-order finite-volume LES of
  Saini et al. (2023, Table 1) and in the AVBP LES of a fan stage by
  [Lewis et al. (2023)](/sources/lewis-2023.md) (§3.2.1);
- the [Sigma model](/methods/sigma-model.md) of Nicoud et al. (cited by Moratilla-Vega et al.
  2024, §2.1, Eqs. 4–5) for jet-noise LES: an eddy viscosity
  $\mu_t=\bar\rho(C_\sigma\Delta)^2\,\varsigma_3(\varsigma_1-\varsigma_2)(\varsigma_2-\varsigma_3)/\varsigma_1^2$
  with $\varsigma_1\ge\varsigma_2\ge\varsigma_3\ge0$ the singular values of the
  resolved velocity-gradient tensor and $C_\sigma$ the model constant
  (registry §11 symbols, as on the Sigma-model page; the paper's $\sigma_i$
  and $C_m$; the constant and $\Delta$ are not printed). The
  paper prints the viscosity as $\mu_{SGS}=(C_m\Delta)^2\mathcal D_m$; the
  density factor is added here to make it a dynamic viscosity *(compiler
  check, not in the sources)*;
- the shear-improved [Smagorinsky](/methods/smagorinsky-model.md) model in
  the lattice Boltzmann LES of fluid–structure interaction of Cheylan et
  al. (2023, §2.7), who state that LES is "not well established in the FSI
  context" (§1);
- dynamic Smagorinsky and [Vreman](/methods/vreman-model.md) in the
  wall-modelled LES of [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
  (§3.2), and Smagorinsky and Vreman adapted to DG as comparators of
  [Kou et al. (2023)](/sources/kou-2023.md) (§4.2);
- [WALE](/methods/wale-model.md) in the channel and periodic-hill LES of
  Wang et al. (2024, §3.2–3.3), and [WALE](/methods/wale-model.md),
  [Vreman](/methods/vreman-model.md) and [Smagorinsky](/methods/smagorinsky-model.md)
  with recalibrated filter widths in the flux-reconstruction LES of Duan &
  Wang (2024);
- the [autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md)
  of Domaradzki (2024), with no adjustable constant, and the
  ensemble-Kalman-calibrated gradient-plus-Smagorinsky mixed model of
  Wang et al. (2023c) (see [gradient model](/methods/gradient-model.md));
- neural-network models with fused grid- and test-filtered inputs for the
  cylinder wake (Kim et al. 2024) and a structure-preserving learned
  closure with subgrid-energy variables in 1D (van Gastelen et al. 2024),
  on [neural-network SGS models](/methods/neural-network-sgs-model.md);
- the reinforcement-learning wall model of
  [Vadrot et al. (2023a)](/sources/vadrot-2023.md) runs in LESGO, whose
  subgrid model for those runs the paper does not state (§II.A; see
  [machine-learning wall models](/methods/machine-learning-wall-model.md));
- the anisotropic stress models, eddy-viscosity plus energy-transfer-free
  remainder, analysed by Inagaki & Kobayashi (2023): see
  [energy backscatter](/definitions/energy-backscatter.md);
- the Sigma model of Nicoud et al. (2011, cited by Mukha et al.) with $C_\sigma=1.35$
  and a cubic near-wall asymptote. [Mukha et al. (2025)](/sources/mukha-2025.md)
  (§II.D, §III.C) compare it with [Vreman](/methods/vreman-model.md) in
  spectral-element wall-modelled LES, where it gives a more oscillatory
  near-wall solution. Its constant is the $C_\sigma$ of the Sigma-model item
  above;
- the [residual-based dynamic model](/methods/residual-based-dynamic-sgs-model.md),
  [Vreman](/methods/vreman-model.md) and
  [Smagorinsky](/methods/smagorinsky-model.md) in continuous
  spectral-element LES of atmospheric-type flows (Reddy et al. 2026), which
  also close the potential-temperature and tracer fluxes with gradient
  diffusivities;
- [WALE](/methods/wale-model.md) in the wall-resolved LES of a pitching
  airfoil (Baldan & Guardone 2025, §1.2), of a model wind turbine
  (Rismondo et al. 2025, §2.1) and in the reference LES of a compressor
  cascade by [Möller et al. (2024)](/sources/moller-2024.md);
- [Smagorinsky](/methods/smagorinsky-model.md) ($C_s=0.15$) with near-body
  damping in the immersed-boundary canopy LES of Löhrer & Fröhlich (2025,
  §2.1);
- a GAN-based [super-resolution model](/methods/super-resolution-sgs-model.md)
  against the selective mixed-scale model of Lenormand et al. (cited by
  Maejima & Kawai)
  in very coarse channel LES (Maejima & Kawai 2025);
- [Smagorinsky](/methods/smagorinsky-model.md) ($C_s=0.1$, $\Delta=2h$ or
  $4h$), [Vreman](/methods/vreman-model.md), the approximate deconvolution
  model and its zeroth-order member, the Layton–Lewandowski model (see
  [scale-similarity models](/methods/scale-similarity-model.md)), on the
  transitional Taylor–Green vortex at $Re=1600$ on $64^3$ (Caban et al.
  2026, §2, §5.3–5.4); the ranking there is on
  [implicit LES](/definitions/implicit-les.md);
- Smagorinsky ($C_s=0.10$), its shear-improved and modal high-pass-filtered
  variants and dynamic Smagorinsky, all with a low-Reynolds-number
  correction, on nonlinearly stable
  [flux reconstruction](/methods/flux-reconstruction.md) (Brillon &
  Nadarajah 2026, §2.6, §3.1.8), which the authors do not recommend for
  that scheme (see [implicit LES](/definitions/implicit-les.md));
- [explicit modal filtering](/methods/explicit-modal-filtering.md) of the
  DGSEM solution with a self-tuned cutoff, presented as "an alternative or
  complement to subgrid-scale modeling", against Smagorinsky (Ranjbar et
  al. 2026, §I, pp. 3–4; §III);
- higher-order truncations of the [gradient model](/methods/gradient-model.md)
  against Smagorinsky, dynamic Smagorinsky and dynamic Leith in 2-D
  turbulence (Jakhar et al. 2026);
- the [Sigma model](/methods/sigma-model.md), with no constant printed, in
  the wall-resolved reacting LES of a swirl combustor with the AVBP code
  by [Agostinelli et al. (2021)](/sources/agostinelli-2021.md) (§2:
  20.3 million tetrahedra, $y^+\approx1$–3, dynamically thickened flame,
  see [thickened flame model](/methods/thickened-flame-model.md)); the
  paper varies the thermal wall condition, not the closure;
- Vreman, clipped dynamic Smagorinsky, WALE and a dynamic Clark model
  reduced to an eddy viscosity against implicit LES in a gas-kinetic
  channel solver (Zhao et al. 2021; ranking on
  [implicit LES](/definitions/implicit-les.md));
- a gene-expression-programming tensor model against dynamic Smagorinsky,
  dynamic mixed and neural-network models in forced isotropic turbulence
  (Li et al. 2021; see
  [symbolic-regression closures](/methods/symbolic-regression-closure.md)).

## Testing a closure

LES closures are assessed [a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md):
on filtered DNS fields outside the solver, or with the model running in the
LES. [Domingo & Vervisch (2023)](/sources/domingo-2023.md) (§1, §3.1) state
that a priori tests miss error accumulation and compensation over time, and
describe a **DNS embedded in LES** of a burner, whose DNS box can be
coarsened to LES resolution to test closures a posteriori in the same
configuration (see [direct numerical simulation](/definitions/direct-numerical-simulation.md)).

[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Introduction, p. 3;
Methods, p. 13) train a wall model inside a channel LES (staggered
second-order finite differences, anisotropic minimum-dissipation SGS model,
"known to perform well in highly anisotropic grids") so that the learned
policy compensates for the numerical and SGS errors of that solver; see
[model-consistent training](/methods/model-consistent-training.md). LES
and implicit LES also serve as reference data for RANS closures: the
transition-model study of [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md)
(§3–4, Tables 5–7; §3.5, Figs. 4–5) compares separation, transition and reattachment on the
SD7003 airfoil at $Re_c=6\times10^4$ with the implicit LES of Galbraith &
Visbal and finds the RANS post-reattachment skin friction much smaller
than the LES one; see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md).
The wall-resolved DG implicit LES of the T161 turbine cascade by
[Morsbach et al. (2024)](/sources/morsbach-2024.md) plays the same role for
SST and Reynolds-stress closures with a transition model.
[Batther & Lee (2022)](/sources/batther-2022.md) (§2.1, §4.2.1, §4.5)
take the wall-resolved LES of Visbal & Garmann (74 million points,
"several million CPU hours" for such LES, as they state) of a NACA 0012
pitching up at $Re_c=2\times10^5$ as the reference for
[delayed detached-eddy simulation](/methods/detached-eddy-simulation.md)
with transition models, on a grid of about 22% of its points (see
[dynamic stall](/definitions/dynamic-stall.md)); their time-step statements
disagree, "one order of magnitude larger" than the LES step (§2.1)
against "roughly 8%" of it (§4.5). [Pan & Zhang (2023)](/sources/pan-2023.md)
(§III–IV) rank DES against DDES by their closeness to a dynamic-Smagorinsky
LES run on the same grid, whose own comparison with PIV shows "remarkable
discrepancy" (§III.C).

Learned closures sharpen the a priori question. An a priori-trained
network of Sirignano & MacArt (2023, §5, Figs. 11–12) fits the subgrid
stress of filtered DNS "almost perfectly" and is substantially worse a
posteriori than the same network trained through the solver; Kang et al.
(2023, §3.3) find that a higher a priori correlation does not guarantee a
better LES; [Kurz et al. (2023)](/sources/kurz-2023.md) (§1) argue that
for implicitly filtered LES the a priori targets do not exist. In
wall-modelled LES, Lozano-Durán & Bae (2023, §4.7, §6) find that the
errors of the SGS model at the matching location ("external" errors)
dominate the wall-stress error once the wall model is good, so better
wall models need better SGS models. Wang et al. (2023c, §III) find that
the pure gradient model gives the best subgrid-stress PDF and the worst
kinetic energy of their models, and Kim et al. (2024, §4.1) that better
a priori predictions of their networks do not ensure better LES, though
networks with wrong-signed a priori shear stress do fail a posteriori.
Maejima & Kawai (2025, §5) run their a priori tests on snapshots of the
coarse LES itself rather than on filtered DNS. A super-resolution network
applied directly to coarse-LES input overpredicts the streamwise and shear
stresses a priori, and the same model overpredicts the velocity a
posteriori (§6.1).

**Where LES stands among closures.** In their turbomachinery review
[Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) (§2.2.2.1,
Fig. 1) place RANS, URANS, hybrid URANS/LES, LES and DNS along the energy
spectrum and state that RANS closure errors affect predictions far more
than LES closure errors, because RANS models carry all turbulent scales and
LES only the high-wavenumber part. They note that machine-learned SGS
models "have yet to be employed" in blade- or stage-level simulations, to
their knowledge (§4.3), and cite an entropy-loss analysis that also
quantifies the entropy generation of the LES subgrid terms as a
grid-resolution indicator (Zhao & Sandberg, cited; §4.2). The
High-Order CFD Workshop summary of [Wang et al. (2013)](/sources/wang-2013.md)
reports from its survey high-order methods as "routinely chosen for LES
and DNS of turbulent flows" (§2) and calls accurate vortex transport "very
important for LES and detached-eddy simulations" (§4.6, case C1.6). For the rod–airfoil configuration,
[Monfaredi et al. (2021)](/sources/monfaredi-2021.md) (§1, §4.2, §5) note
that most earlier studies used 3D LES or DES with an acoustic analogy;
their own adjoint shape optimization is 2D URANS, and LES and DES adjoints
are named as future work (see
[Ffowcs Williams–Hawkings analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)).

**Cost, fidelity and the modelling burden.** Four sources place LES
differently. [Le et al. (2024)](/sources/le-2024.md)
(§3, p. 9), reviewing supersonic combustion, class DNS and LES as "not
suitable to use in engineering applications" because of their cost, with
DES and RANS the engineering focus. [Xiao et al. (2025)](/sources/xiao-2025.md)
(§1) list high-lift aircraft, iced-wing separation and flows inside
aircraft engines as applications that "establish LES as a critical
component in the industry push toward Certification by Analysis".
[De Cosmo et al. (2025)](/sources/decosmo-2025.md) (§1) describe LES as
a "high-fidelity turbulence resolving approach" that resolves "usually
more than 70%" of the spectrum (citing Reynolds), and yet, "from a turbulence modelling perspective", as
"less-sophisticated than Unsteady-RANS", since it solves at most one,
usually algebraic, subgrid equation. For reacting flows,
[Salehi et al. (2024)](/sources/salehi-2024.md) (§1) state that a
turbulence–chemistry interaction model is almost always required even in
LES, because extinction events correlate with the smallest scales, which
the LES filter removes (see
[conditional source-term estimation](/methods/conditional-source-term-estimation.md)).
[Fang et al. (2026)](/sources/fang-2026.md) (§1, Eqs. 2–3; §4.1), a review
of machine learning, print the filtered momentum equation with a
subgrid stress left undefined and no filter specified, and note that DNS
and LES data reach terabyte to petabyte scale.

**Explicit against implicit LES as references.** [Cao et al. (2024)](/sources/cao-2024.md)
(§3.4, Figs. 14–16) compare their high-order gas-kinetic
[implicit LES](/definitions/implicit-les.md) of a compressible
[periodic hill](/benchmarks/periodic-hill.md) ($Re_b=2800$) with an
approximate-deconvolution LES (Ziefle et al., which they cite). They write
that "the explicit LES overpredicts the normalized Reynolds stresses …
the explicit LES model may pollute current low-Reynolds number separated
turbulent flow". In the same section they note that the reference LES
statistics are density-weighted while theirs and the DNS are not.
[Lederer et al. (2026)](/sources/lederer-2026.md) (§3) exclude explicit
SGS models from their DG-type LES of a transitional airfoil "due to their
inferior performance compared to ILES in a DG framework for wall-bounded
flow problems", citing their 2023 study and Fernandez et al.; see
[implicit LES](/definitions/implicit-les.md).
For compressible shock-capturing schemes, [Deng et al. (2022)](/sources/deng-2022.md)
(§1, Remark 2) recommend running their adjustable-dissipation scheme in its
non-dissipative central limit for DNS and explicit LES and with added
upwind dissipation as ILES, and [Ma et al. (2022)](/sources/ma-2022.md)
(§1) motivate ILES by the difficulty, which they cite from earlier work, of
subgrid modelling in compressible and especially wall-bounded flow.

**Plane-wise a priori metrics.** In wall-bounded flow [Xu et al. (2023)](/sources/xu-2023.md)
(§2.2, Eqs. 2.33–2.34) measure a model term $H$ against filtered DNS by
the correlation coefficient and the relative error computed over each
wall-parallel plane, the relative error being the plane r.m.s. of
$H^{\mathrm{real}}-H^{\mathrm{model}}$ over the plane r.m.s. of
$H^{\mathrm{real}}$, with 95% confidence intervals of the correlation from
the Fisher transformation (citing Bonett & Wright). Their a posteriori
references are filtered DNS with the filter ratio equal to the LES-to-DNS
grid ratio (§4). See
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

## Qualifications

- Zhang et al. (2022b, §IV A) call the $\mathcal H$ term at $M_t=0.8$ "two
  orders of magnitude higher" than at $M_t=0.4$; their Table II gives 0.11
  against 0.0060, a ratio of about 18 *(compiler check, not in the
  sources)*. They print $M_t=0.79$ in Tables I–II and 0.80 in Table III.
- Flad & Gassner (2017, App. A) print the filter width as "the local cell
  volume divided by $(N+1)^3$", which is a volume, not a length; the length
  form of the same idea is the cube root used by Beck & Kurz (2023, Eq. 11).
- Goc et al. (2021, p. 4) print the resolved viscous stress as
  $\mu(\tilde T)(\tilde S_{ij}-\tfrac13\tilde S_{kk}\delta_{ij})$; with
  $S_{ij}$ defined with the factor $\tfrac12$, the Newtonian deviatoric stress
  is $2\mu S^d_{ij}$ (the registry's $\sigma_{ij}$) *(compiler check, not in
  the sources)*, so the printed formula lacks the factor 2.
- Agdestein & Sanderse (2025, App. E) state that the top-hat transfer
  function in 3D "only depends on $\|k\|$"; their own Eq. (E.2) is a product
  of one-dimensional factors, which is isotropic only to second order near
  $k=0$ *(compiler check, not in the sources)*.

- Abe (2021) gives the coarse-grid case two labels, BSC and, in §III and the
  Fig. 8 caption, "BFC".
- **Modelled-energy fraction: different statements, not a conflict.**
  Haering et al. (2022, §V A 1) recall, citing Jiménez & Moser, that typical
  LES is expected to model below about 10% of the energy, and report their
  own hybrid model performing well past it; Seyedi & Zayernouri (2022,
  §III.1) use the 10% figure as a description of common LES practice to
  delimit LES from VLES, and test their model in both; Helm & Martín (2022,
  §V) state, from the a priori study of Martín et al., that 25–30% "may be
  possible" for their LES method in compressible boundary layers; Blind et
  al. (2023, §1) report, citing Toosi & Larsson, that the energy ratio
  correlates poorly with the length scales of wall-bounded flows and so is
  a weak grid criterion. No source states that LES fails above 10%, and the
  fractions are defined differently (domain-wide $1-k_{\mathrm{res}}/k_{\mathrm{tot}}$
  in Haering et al., a local fraction of the DNS energy in Helm & Martín,
  an unprinted percentage in Seyedi & Zayernouri); the statements are
  therefore recorded as qualifications, not as a contradiction.
- Helm & Martín (2022, §III B) give the Mach 7 unresolved share at the wall
  both as 25% and, a sentence later, as a maximum of 18%.
- Sirignano & MacArt (2023, Eq. 3.4) and Saini et al. (2023) do not state
  whether their $\lvert\bar S\rvert$ carries the factor two; Kang et al.
  (2023) and Kurz et al. (2023, Eq. 19) write $\sqrt{2\bar S_{ij}\bar S_{ij}}$,
  the registry convention.
- Seyedi & Zayernouri (2022, Eq. 24) call $\tfrac12(\overline{u_iu_i}-\bar u_i\bar u_i)$
  the "resolved" and $\tfrac12\bar u_i\bar u_i$ the "filtered" kinetic
  energy; the first is the subfilter energy and the second the resolved
  one.
- Caban et al. (2026) call the first-derivative induced filter
  "non-dissipative" (§1, §3.2.1) and elsewhere "dissipative … without
  inducing numerical diffusion" (abstract, §5.1, §6); in either wording it
  changes the phase speed only, as their Eq. (27) shows.
- Wu & Lele (2026, §2.1) rule out the sharp spectral cutoff for general
  subgrid modelling, while several sources above use it for a priori
  filtering (Vela-Martín 2022; Kim et al. 2022; Inagaki & Kobayashi 2023;
  Li et al. 2024). Wu & Lele state a modelling preference, not a result
  about those studies, so no contradiction is recorded.
- Rickard & Kasbaoui (2026) print the wall-stress relation (Eq. 2.25) with
  the density used inconsistently between its acceleration and stress
  terms *(compiler check, not in the sources)*; the slip models of §4 do
  not use that relation.
- **Luckring & Rizzi (2024), reach of wall-resolved LES.** The survey
  states that wall-resolved LES is restricted to Reynolds numbers "on the
  order of $10^4$" (§3.1.1.2, §4.1.1), while the same sections report
  wall-resolved LES of a NACA 0012 at $Re_c=1\times10^6$ on
  $267\times10^6$ nodes and of a C-130 afterbody at $Re_D=0.2\times10^6$
  on $210\times10^6$ nodes.

# Citations

- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II, Eqs. (1)–(4); §V (a priori filter).
- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1, Eqs. (2.1)–(2.5).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.1, Eqs. (6)–(9); §4.1; §6.3, Eqs. (48)–(50).
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §2.1, Eqs. (2.2)–(2.7); §3, Eqs. (3.1)–(3.5); §5.2–5.3; §6.3; §8.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §I, Eqs. (1)–(5); §III B, Eq. (11).
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §3.2–3.3, Eqs. (11)–(15); App. E.
- [Haering et al. (2022)](/sources/haering-2022.md) — §II A–C; §III, Eqs. (3)–(10); §V A 1.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — App. A.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §II, Eqs. (1)–(3), Table I; §III.B.
- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §1; §3.1.
- [Abe (2021)](/sources/abe-2021.md) — §II, Eqs. (1)–(2), (4), (12); §IV B–D, Tables I–III, Figs. 9–10; §V; App. C, Eq. (C1).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §II, Eqs. (1)–(3); §III; §III.A.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.1, Eq. (125).
- [Basile et al. (2023)](/sources/basile-2023.md) — §2.2; §3.2; §4.2.3, Fig. 10.
- [François et al. (2022)](/sources/francois-2022.md) — §3.1.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §2; §6; §8.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §III, Eqs. (13)–(16).
- [Liu et al. (2022)](/sources/liu-2022.md) — §1.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Introduction, p. 3; Methods, p. 13.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §3–4, Tables 5–7; §3.5, Figs. 4–5.
- [Helm & Martín (2022)](/sources/helm-2022.md) — §II, Eqs. (1)–(12); §III B, Figs. 5–6; §V.
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §II, Eqs. (1)–(4); §III; §III.1, Eq. (24); §IV.
- [Kim et al. (2022)](/sources/kim-2022.md) — §II A, Eqs. (3)–(4); §II C; §III E.
- [Blind et al. (2023)](/sources/blind-2023.md) — §1; §2.2–2.3.
- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (8)–(11).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1.
- [Fischer et al. (2022)](/sources/fischer-2022.md) — §4.1, Table 2.
- [Placco et al. (2023)](/sources/placco-2023.md) — §1–2.
- [Sirignano & MacArt (2023)](/sources/sirignano-2023.md) — §2, Eq. (2.2); §3.1, Eq. (3.2); §3.2, Eqs. (3.3)–(3.5); §5, Figs. 11–12.
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §II, Eqs. (1)–(5); §III A.
- [Kang et al. (2023)](/sources/kang-2023.md) — Eqs. (2.5)–(2.8); §2.2–2.3; §3.3; §3.5.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §1; §3.3, Eq. (19).
- [Lederer et al. (2023)](/sources/lederer-2023.md) — §3.1.
- [Saini et al. (2023)](/sources/saini-2023.md) — §2.1, Table 1; §2.2, Eqs. (1)–(5).
- [Moratilla-Vega et al. (2024)](/sources/moratillavega-2024.md) — §2.1, Eqs. (1)–(5).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.2.1.
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §1; §2.7, Eqs. (37)–(38).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §3.2; §4.7; §6.
- [Kou et al. (2023)](/sources/kou-2023.md) — §4.2.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §2.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §2.1–2.2; §3, Eqs. (28)–(30).
- [Bouhafid et al. (2024)](/sources/bouhafid-2024.md) — §2.1–2.2, Eq. (2.6); §4.1.
- [Kim et al. (2024)](/sources/kim-2024.md) — §2.1–2.2, Eqs. (2.1)–(2.6); §4.1.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §1, Eqs. (1.1)–(1.2); §2.3, Eqs. (2.28)–(2.41); §4.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A, Eqs. (7)–(10), (19); §III; App. A, Eq. (A1).
- [van Gastelen et al. (2024)](/sources/vangastelen-2024.md) — §2.3–2.6, Eqs. (15)–(32); §4.1.1; §5.
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — §1; §3, Eqs. (16)–(19).
- [Wang et al. (2024)](/sources/wang-2024.md) — §3.2–3.3, Table 2, Figs. 5–6.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §3.2.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §II.A.
- [Li et al. (2024)](/sources/li-2024.md) — arXiv v2: §II A, Eqs. (5)–(6); §IV; §V (filters, $k_c=21$, Gaussian width).
- [Zhao et al. (2025)](/sources/zhao-2025.md) — arXiv v3: §2.1, Eq. (4); §2.5; §3.1–3.2.
- [Reddy et al. (2026)](/sources/reddy-2026.md) — preprint of 4 March 2021: §2.1, Eqs. (2)–(7); §3.4, Table 1.
- [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md) — §2.1, Eq. (2.4); App. C, Eqs. (C1)–(C3), Figs. 28–29.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1; §2.1, Eq. (2.9); §3.2; §4–4.1; §5.3; §6.1.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — arXiv v1: §II.A, Eq. (3); §II.D; §III.C.
- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — §2.1, Eq. (2.2); §3, Fig. 8(c).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — arXiv v2: §1.1–1.2; §2.1, Figs. 3–8; §3.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv v1: §3.4, Figs. 14–16.
- [Möller et al. (2024)](/sources/moller-2024.md) — accepted manuscript: §III.A, Table 3 (WALE reference LES).
- [Caban et al. (2026)](/sources/caban-2026.md) — §1; §2, Eqs. (1)–(12), Fig. 1; §3.1; §3.2.1–3.2.2, Eqs. (24)–(35), Fig. 3; §4.1, Fig. 5; §5.3–5.4; §5.4.2; §6.
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv v1: §2.3–2.6, Eqs. (18)–(60); §3.1.8.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — arXiv v3: pp. 2–4, Eqs. (1)–(2); App. C.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv v1: §3.
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv v1: §I, pp. 3–4; §II.B, Eq. (42); §III.
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §2.1–2.3, Eqs. (2.3)–(2.27); §3.1, Eqs. (3.1)–(3.2); §3.3, Fig. 10; §4.2; §5, Eqs. (5.1)–(5.3); §7.
- [Tang et al. (2022)](/sources/tang-2022.md) — §2.1, Eqs. (1)–(9); §2.2, Eqs. (15)–(17); §4.
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv v2: §1; §2.1, Eqs. (2.1)–(2.2); §3, Eqs. (3.1)–(3.4), Fig. 1; §3.2.1; §3.2.2, Fig. 4; §3.3.
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §II B–C, Eqs. (14)–(29); §V A–B, Tables III–IV, Fig. 3; §VI.
- [Volpiani (2024)](/sources/volpiani-2024.md) — §1; §2.1, Eq. (4); App. 2.
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.B–D, Eqs. (12)–(14); §III.B–C, Eq. (23), Figs. 6, 8; §IV.
- [Ahn et al. (2023)](/sources/ahn-2023.md) — §IV C 1, Fig. 12.
- [Batther & Lee (2022)](/sources/batther-2022.md) — §2.1; §4.2.1; §4.5.
- [Gao et al. (2022)](/sources/gao-2022.md) — §5.1, Table 2.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §III, Eqs. (12)–(14), (17), (21); §III.A–D.
- [Li et al. (2021)](/sources/li-2021.md) — §II A, Eqs. (6)–(8); §III A, Eq. (17); §III C.
- [Cuenot et al. (2022)](/sources/cuenot-2022.md) — §1; §2.2.
- [Böttler et al. (2022)](/sources/bottler-2022.md) — §4.
- [Agostinelli et al. (2021)](/sources/agostinelli-2021.md) — §2.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.2.2.1, Fig. 1; §4.2; §4.3.
- [Wang et al. (2013)](/sources/wang-2013.md) — §2; §4.6.
- [Monfaredi et al. (2021)](/sources/monfaredi-2021.md) — §1; §4.2; §5.
- [Qi et al. (2022)](/sources/qi-2022-b.md) — §2, Eqs. (2.1)–(2.12); §3.1, Eqs. (3.1)–(3.7).
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §2.1, Eqs. (1)–(5).
- [Tonicello et al. (2022)](/sources/tonicello-2022.md) — §4, Eqs. (4.1)–(4.5); §4.2, Eq. (4.14), Table 4.
- [Chen et al. (2022)](/sources/chen-2022-g.md) — §2.3; §4.1, Eqs. (25)–(29), (33).
- [Simonis et al. (2022)](/sources/simonis-2022.md) — §2.1, Eqs. (1)–(6); §2.4; §3.2–3.4, Eq. (29), Figs. 2–9; §4.
- [Kang & Masud (2022)](/sources/kang-2022.md) — §3.4.
- [Svärd (2022)](/sources/svard-2022.md) — §1; §2.2–2.3; §6.
- [Deng et al. (2022)](/sources/deng-2022.md) — §1; §3.2, Remark 2.
- [Ma et al. (2022)](/sources/ma-2022.md) — §1.
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §I; §II, Eqs. (8)–(20); §IV A, Table II; §V.
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §I; §II, Eqs. (12)–(23); §IV A, Tables IV–V; §IV B; §V.
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §3.1, Eq. (1); §3.2; §6.2.
- [Ihme et al. (2022)](/sources/ihme-2022.md) — §4.1.4, Eqs. (71)–(72), (74).
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §IV B, Eqs. (17)–(19).
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §I; Eq. (6).
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §I; §II, Eqs. (7)–(8); §V, Eq. (31).
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1; §2.1.1.
- [Stanly et al. (2022)](/sources/stanly-2022.md) — §6.
- [Zhang et al. (2022e)](/sources/zhang-2022-i.md) — §II A.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §1.4; §4.
- [Xu et al. (2023)](/sources/xu-2023.md) — §2.1, Eqs. (2.1)–(2.14); §2.2, Eqs. (2.32)–(2.34); §3.2, Eqs. (3.27)–(3.30), Fig. 8; §4.1; §5.
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) — §3, Eqs. (7)–(18); §3.1; §4.2.
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §2.2, Eqs. (2.8)–(2.11); §5.3–5.4, Eq. (5.5), Fig. 17; Apps. C–D.
- [Zhang et al. (2023)](/sources/zhang-2023-c.md) — §2, Eqs. (1)–(2), Fig. 2b; §3.3.
- [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) — §I; §III B 2, Table III.
- [Shi & Yan (2023)](/sources/shi-2023.md) — §I; §IV, Table I.
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.1; §3.2, Eqs. (1)–(7); §3.3.
- [Nista et al. (2023)](/sources/nista-2023.md) — §1, Eqs. (1)–(3).
- [Nmira et al. (2023)](/sources/nmira-2023.md) — §2.1; §3.1; §3.4.
- [Wei et al. (2023)](/sources/wei-2023.md) — §II B, Eqs. (9)–(15); §III B, Eq. (34), Fig. 6.
- [Lv & Ekaterinaris (2023)](/sources/lv-2023.md) — §2 (LES block, Eqs. 16–18).
- [Taschner et al. (2024)](/sources/taschner-2024.md) — §2.1, Eqs. (1)–(4).
- [Hu et al. (2024)](/sources/hu-2024.md) — §1; §3.
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §3.1, Fig. 11; §3.3, Figs. 17–20.
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.5; §3.1; §3.4; §4.7; §5; sidebar "Large-Eddy Simulations".
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §4.1.
- [Sabnis & Babinsky (2023)](/sources/sabnis-2023.md) — §3–§5.
- [Wu et al. (2024)](/sources/wu-2024.md) — §2.1.
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §1 (resolved fraction, modelling burden against URANS); §2.1, Eqs. 1–4 (sign of the sub-filter stress).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §2.4.1.2 (truncation error against subfilter terms, Ghosal cited); §2.4.1.4, Table 1 (grid estimates, WMLES guidelines); §3.1.1.2, §4.1.1 (Reynolds-number reach of wall-resolved LES).
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §III.A–B, Table I, Figs. 1–2 (grid convergence of LES of a supersonic boundary layer).
- [Xiao et al. (2025)](/sources/xiao-2025.md) — §1 (industrial applications, implicit-filter mismatch on coarse grids).
- [Le et al. (2024)](/sources/le-2024.md) — §3, p. 9 (LES classed as too costly for engineering). Review, citation only.
- [Salehi et al. (2024)](/sources/salehi-2024.md) — §1 (filter removes extinction-relevant scales).
- [Fang et al. (2026)](/sources/fang-2026.md) — §1, Eqs. 2–3; §4.1 (filtered equations, data volumes). Review, citation only.
