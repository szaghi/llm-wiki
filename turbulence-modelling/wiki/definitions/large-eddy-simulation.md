---
type: Definition
title: "Large-eddy simulation: filtering and the subgrid-scale stress"
description: "Large-eddy simulation resolves the filtered velocity and models the subgrid-scale stress; this page fixes the filtered equations, the filters and filter widths used by the sources (including high-aspect-ratio cells and element methods), the commutation and discretization terms, and the gauge freedom of the subgrid stress."
status: established
aliases: [LES, filtered Navier–Stokes equations, subgrid-scale stress, SGS stress, subfilter stress, coarse-grained equations]
tags: [les, filtering, sgs-model, compressible]
timestamp: 2026-10-27T11:01:00Z
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
$\tau_{\mathrm{col},t}$ page-local, as on the gas-kinetic page; the
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
width $\Delta_f$ (page-local, the paper's $\delta_f$). The kernel is truncated by the
fluid indicator and **not rescaled**: the filtered indicator, a fluid
volume fraction $\varphi_f$ (page-local, the paper's $\alpha_f$; $\tfrac12$ at a planar wall for any
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
| [Blind et al. (2023)](/sources/blind-2023.md), §2.3 | $\mathrm{Vol}^{1/3}/(N+1)$ in DG (Vreman length scale), and $[(N+1)/(N_f+1)]^{1/3}$ times it for a modal test filter keeping degrees up to $N_f$ (page-local, as on the mesh-adaptation page) |
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
| [Reddy et al. (2026)](/sources/reddy-2026.md), §3.4, Table 1 | $\min(h_x,h_y,h_z)/(N+1)$ for continuous spectral elements of size $h_x,h_y,h_z$ (page-local) and degree $N$; Table 1 lists $(h_xh_yh_z)^{1/3}/N$ and a Scotti–Meneveau–Lilly correction for anisotropic grids |
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
(page-local), with the analogous heat flux; substituting it recovers the
classical filtered equations. With the grid projection written as a
second, implicit filter and assumed to commute with the explicit one, the
total unresolved stress is the sum of a grid-truncation part, which
deconvolution cannot recover, and a subfilter part between grid and
explicit filter, which it can,
$\tau^{\mathrm{tot}}_{ij}=\tau^{\mathrm{gr}}_{ij}+\tau^{\mathrm{sf}}_{ij}$
(page-local; see
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
recirculation bubble (reattachment length $x_R$, page-local) from $x_R/H=7.19$ to 7.43 against the experimental
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

**Activity parameter.** [Löhrer & Fröhlich (2025)](/sources/lohrer-2025.md)
(App. C, Eqs. C1–C3, Figs. 28–29) rate their canopy LES with the subgrid
activity parameter of Geurts & Fröhlich, which they cite,

$$Q_\varepsilon=\frac{\varepsilon_{\mathrm{sgs}}}{\varepsilon_{\mathrm{res}}+\varepsilon_{\mathrm{sgs}}},\qquad
\varepsilon_{\mathrm{res}}=\nu\,\bar S_{ij}\partial_j\bar u_i,\quad
\varepsilon_{\mathrm{sgs}}=\nu_t\,\bar S_{ij}\partial_j\bar u_i ,$$

($Q_\varepsilon$, $\varepsilon_{\mathrm{res}}$, $\varepsilon_{\mathrm{sgs}}$
page-local).

- **Range.** $Q_\varepsilon$ is 0 for DNS and 1 for LES at infinite
  Reynolds number. For eddy-viscosity models it reduces to
  $\nu_t/(\nu_t+\nu)$ (Celik et al., cited by Löhrer & Fröhlich).
- **Values.** In their run the mean is 0.11, the 95th percentile about
  0.23 and the local maximum about 0.3.
- **The authors' reading.** They call the run "a high-resolution LES …
  close to a DNS". The subgrid share of the mean drag is below the viscous
  one everywhere.
- **Caveat.** Their $\nu_t$ is damped near the immersed blades with the
  immersed-boundary delta kernel (§2.3). Since
  $Q_\varepsilon\approx\nu_t/(\nu_t+\nu)$ grows with $\nu_t$, this damping
  lowers $Q_\varepsilon$ there *(compiler check, not in the sources)*.

[Rismondo et al. (2025)](/sources/rismondo-2025.md) (§3, Fig. 8c) use the
same quantity informally. A ratio $\nu_t/\nu$ mostly between 0 and 10 in a
wall-resolved wind-turbine LES is, for them, an indication of high
resolution; they report no grid-convergence study.

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
  (page-local symbols as on the Sigma-model page, the paper's $\sigma_i$
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

## Qualifications

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
