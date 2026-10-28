---
type: Source
title: "Tonicello et al. (2023) — Fully-discrete spatial eigenanalysis of discontinuous spectral element methods: Insights into well-resolved and under-resolved vortical flows"
description: "Extends spatial eigenanalysis of flux-reconstruction, spectral-difference and DG schemes to include explicit Runge–Kutta time integration, finding stage-dependent mode counts, periodic eigencurves and time-step effects on dissipation, confirmed for well-resolved flows but not for under-resolved Taylor–Green and two-dimensional turbulence."
resource: "doi:10.1016/j.compfluid.2023.106060"
source_kind: paper
authors: [Tonicello N., Moura R.C., Lodato G., Mengaldo G.]
year: 2023
venue: "Comput. Fluids 266:106060"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Computers_amp_Fluids_Tonicello_Fully-discrete_spatial_eigenanalysis_of_discontinuous_spectr.pdf"
tags: [high-order, numerical-dissipation, spectral-difference, flux-reconstruction, implicit-les, time-integration]
timestamp: 2026-10-28T07:07:00Z
---

# Summary

Tonicello et al. (2023) extend the **spatial** form of
[eigensolution analysis](/methods/eigensolution-analysis.md), in which a
real frequency is prescribed and complex numerical wavenumbers are
sought (the inflow–outflow setting), from semi-discrete to
**fully-discrete** form, including the errors of explicit Runge–Kutta
time integration (RK11, RK22, RK33 and the five-stage fourth-order
Carpenter–Kennedy RK45). The spatial scheme is
[flux reconstruction](/methods/flux-reconstruction.md) for 1D linear
advection with an upwind-parameterized interface flux, in its
[DG](/methods/discontinuous-galerkin-spectral-element-method.md) and
[spectral difference](/methods/spectral-difference-method.md)
recoveries. The fully-discrete dispersion relation
$\det(\mathbf T(k_h,\Delta t)-e^{-\iota\omega_{\mathrm f}\Delta t}\mathbf I)=0$ is a
polynomial in $z=e^{\iota k_h}$ whose degree grows with the number of
stages.

With upwinding the number of transmitted modes equals the number of
stages (twice that for non-upwind fluxes), one of them physical; the
eigencurves are periodic in frequency with period $2\omega_{\mathrm c}$,
$\omega_{\mathrm c}=\pi/\Delta t$, and the effective right-most frequency of an
$n_{\mathrm{RK}}$-stage scheme is $n_{\mathrm{RK}}\omega_{\mathrm c}/2$. At low frequency the superconvergence
order $2N+1$ falls to that of the time scheme; at high frequency a larger
step lowers the [numerical dissipation](/properties/numerical-dissipation.md)
until anti-dissipation at the stability limit, and for nearly centred
fluxes it smooths the "dissipative bubbles"; explicit Euler is
convectively unstable at low frequency. Linear-advection runs with an
oscillating inlet confirm these trends, and an inlet–outlet isentropic
vortex shows the convergence rate limited by the time scheme near the
stability limit (the well-resolved,
[DNS](/definitions/direct-numerical-simulation.md)-like regime). In the
under-resolved inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
and a 2D duct with forced inlet ([implicit-LES](/definitions/implicit-les.md)
proxies) the time step has almost no effect until very close to the
stability limit: spatial errors dominate, and the linear theory does not
predict the nonlinear under-resolved behaviour. Spectral vanishing
viscosity enters only through the cited eigenanalysis literature
([spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)).

# Version read

Version of record (Comput. Fluids 266:106060, Elsevier; received 30 Aug
2022, revised 23 Jun 2023, accepted 14 Sep 2023, online 23 Sep 2023), 23
pages, all read; equations of pp. 2–4 and 13–14 checked visually. Page-1
title, four authors, venue and DOI match the metadata; no identity
problem. Tonicello et al. (2022, J. Fluid Mech.) is a different work
([tonicello-2022](/sources/tonicello-2022.md)). Numbering on this page is
that of this version.

# Key claims

Symbols follow [eigensolution analysis](/methods/eigensolution-analysis.md).
The source's wavenumber $\theta$ and frequency $\omega$ are written $k$
and $\omega_{\mathrm f}$, their numerical (complex) counterparts $\tilde\theta$,
$\tilde\omega$ are $k_h$, $\omega_{\mathrm f,h}$; its upwinding parameter $\alpha$
($0$ upwind, $0.5$ centred) is $\alpha_{\mathrm T}$, i.e.
$\lambda_{\mathrm{up}}=1-2\alpha_{\mathrm T}$ in the convention of that page; its
$\tau=\Delta t/\Delta t_{\max}$ is $r_{\Delta t}$; its numbers of stages $M$, $R$ are $n_{\mathrm{RK}}$; its $N$, used as the
polynomial degree ("5th-order" is $N=4$), is the registry's $N$. The
semi-discrete operator is $\mathbf H(k_h)=-2(\mathbf C^-e^{-\iota k_h}+\mathbf C^0+\mathbf C^+e^{\iota k_h})$
and the RK amplification matrix $\mathbf T(k_h,\Delta t)=\sum_m\beta_m(\mathbf H\Delta t)^m/m!$
(Eqs. 11, 13).

1. Earlier spatial eigenanalyses of high-order methods were semi-discrete; the generalization including time discretization "remains, as of yet, unexplored", and this is "the first fully-discrete version of the spatial eigenalaysis for high-order methods" (§1, §5). **Stated**
2. The fully-discrete spatial dispersion relation is $\det(\mathbf T(k_h,\Delta t)-e^{-\iota\omega_{\mathrm f}\Delta t}\mathbf I)=0$ (Eq. 18), which for $\Delta t\to0$ reduces to the semi-discrete $\det(\mathbf H(k_h)+\iota\omega_{\mathrm f}\mathbf I)=0$ (Eqs. 17, 21) (§2.2). **Derived**
3. For explicit Euler (RK11) the characteristic polynomial in $z=e^{\iota k_h}$ has the order of the semi-discrete one, giving a single transmitted physical mode under upwinding (Eq. 20, §3, Fig. 1). **Derived**
4. The 5th-order upwind FR-SD scheme with RK11 shows negative dissipation (convective instability) at low frequency for $\Delta t=0.01,\dots,0.1$, "re-affirm[ing] that RK11 (explicit Euler) is only marginally stable for pure advection"; for moderately large $\Delta t$ waves regain stability beyond some frequency (§3, Fig. 1). **Shown**
5. With upwinding the number of modes equals the number of RK stages (RK22 two, RK33 three, RK45 five); for non-upwind fluxes the number of roots is twice the number of stages, half of them reflected (§3, Figs. 2, 4, 5, 31, 32). **Derived** / **Shown**
6. The physical mode is the one anchored at the origin of the dissipation plots (vanishing dissipation for well-resolved waves) (§3). **Stated**
7. For 2nd-order FR-SD with RK22, as $r_{\Delta t}$ grows the physical mode becomes less dissipative overall (at least for $\omega_{\mathrm f}h/(N+1)>0.5$) until it touches zero dissipation at $r_{\Delta t}=1$ (anti-dissipation beyond); the spurious transmitted mode, infinitely dissipated for $r_{\Delta t}\to0$, approaches the physical one as $r_{\Delta t}\to1$ (§3, Figs. 2–3). **Shown**
8. Fully-discrete spatial eigencurves are periodic in $\omega_{\mathrm f}$ with period $2\omega_{\mathrm c}$, $\omega_{\mathrm c}=\pi/\Delta t$, the spurious curves being shifted replications of the physical one; this periodicity "has not been noted in the literature so far" because $\omega_{\mathrm c}\to\infty$ as $r_{\Delta t}\to0$ (§3, Fig. 2). **Shown** / **Stated**
9. $\omega_{\mathrm c}h/(N+1)$ is the counterpart of the wavenumber limit $kh/(N+1)=\pi$ of temporal analysis, but the observed limit for an $n_{\mathrm{RK}}$-stage scheme is $n_{\mathrm{RK}}\omega_{\mathrm c}/2$, "as if multiple single-stage time steps of size $\delta t=2\Delta t/R$ had been employed" ($R=n_{\mathrm{RK}}$), the physical mode being symmetric about it (§3, Figs. 4–5). **Shown**
10. Upwind FR-DG has a more restrictive stability limit than FR-SD, so its curves extend to higher frequencies, and is spatially less dissipative overall (§3, Fig. 7; App. Figs. 29–30). **Shown** / **Stated** (cited)
11. For 5th-order FR-SD with RK33 the superconvergence of order $2N+1=9$ falls to fourth order at small wavenumbers and frequencies; order 9 survives in an intermediate range, which smaller time steps extend to smaller wavenumbers; the temporal error $E_T=|\omega_{\mathrm f,h}(k)-\omega_{\mathrm f}(k)|$ and the spatial error $E_S=|k_h(\omega_{\mathrm f})-k(\omega_{\mathrm f})|$ agree except at high frequencies and wavenumbers (§3, Eqs. 24–25, Fig. 8). **Shown**
12. For nearly centred fluxes ($\alpha_{\mathrm T}=0.49$) a larger $r_{\Delta t}$ reduces high-frequency dissipation and smooths the non-monotonic "dissipative bubbles"; for high enough $r_{\Delta t}$ the curve touches zero, with possible convective instability (clearly for RK33) (§3, Fig. 9). **Shown**
13. Non-monotonic dissipation in frequency "might potentially lead to undesirable non-smooth features in simulations with broadband energy content" (§3). **Stated**
14. For DNS-like flows the relevant part of the analysis is the well-resolved (small) wavenumber and frequency range; for LES the high-wavenumber and high-frequency range is the informative one (§3). **Stated**
15. 1D linear advection with an oscillating inlet (5th-order SD, 100 elements, $h=0.01$, $\alpha_{\mathrm T}=0.49$): at $\omega_1=1$ dissipation grows with $r_{\Delta t}$ for RK33 and RK45, RK33 dissipating more than RK45 at $r_{\Delta t}=0.9$; at $\omega_3=3.5$ (RK33) dissipation decreases as $r_{\Delta t}$ grows, "significantly lower" near the limit (§4.1, Figs. 11–12, 15). **Shown**
16. Over a large low-frequency range the effect of time integration is essentially dissipative (larger $\Delta t$, stronger dissipation); at high frequency it is the opposite, and the largest frequencies cause the stability limit (§4.1). **Shown** / **Stated**
17. With explicit Euler and 5th-order SD the theory predicts a switch from dissipative to anti-dissipative behaviour at normalized $\Delta t\approx0.01$, i.e. $\Delta t\approx1.0\times10^{-4}$ for $h=0.01$; runs at $9.825\times10^{-5}$, $9.925\times10^{-5}$ and $1.0925\times10^{-4}$ show decay, near-neutral behaviour and spatial growth (§4.1, Figs. 16–17). **Shown**
18. At the lowest frequency, with 1000 elements and $\Delta t=1.0\times10^{-6}$ and $1.0\times10^{-7}$, the signal grows slowly in space but not in time at a probe, consistent with convective instability (§4.1, Figs. 18–21). **Shown**
19. The fully-discrete spatial framework reproduces the convergence results of the fully-discrete temporal analysis of Vermeire & Vincent (§3, §4.2). **Stated** (comparison not displayed)
20. Inlet–outlet isentropic vortex (6th- and 8th-order SD, RK33, $r_{\Delta t}=0.1$, 0.5, 0.9): steps close to the limit slow the error convergence, the spatial rate being "eventually reduced to the order of the time integration scheme"; on deformed meshes this happens at smaller grid sizes (§4.2.1, Fig. 23). **Shown**
21. In the vortex case, entropy fields at $r_{\Delta t}=0.9$ and 0.99 differ only by irregular spurious oscillations, stronger downstream of the mesh coarsening; "a non-negligible influence of the time step choice is observed only very close to the CFL limit", in agreement with Vermeire et al. (§4.2.1, Fig. 24). **Shown**
22. Inviscid Taylor–Green vortex ($M=0.1$, $32^3$ elements, 6th-order SD, third-order RK): the numerical dissipation $\varepsilon_{\mathrm{num}}$ (kinetic-energy decay rate minus pressure dilatation, Eq. 28) is "almost indistinguishable" for $r_{\Delta t}=0.5$, 0.9, 0.95, peaking near $t/T=10$; "the gradual decrease of numerical dissipation observed in the theoretical framework does not manifest" (§4.3.1, Fig. 25). **Shown**
23. 2D inviscid duct with oscillating inlet ($M=0.03$, mesh coarsening at $x=12\pi$): all cases with $r_{\Delta t}$ below about 0.95 behave alike; only near the limit do spurious entropy oscillations appear; the mesh-size change triggers more spurious reflected waves than the outflow (§4.3.2, Fig. 28). **Shown**
24. In under-resolved flows spatial errors dominate the time-integration influence: the time step "plays a more relevant role in highly accurate simulations such as DNS", while in LES temporal errors are "more likely overshadowed by spatial errors" (abstract, §4.3.2, §5). **Shown** / **Stated**
25. The interaction of space and time errors is "more complex than otherwise anticipated" and the linear theory "is not always representative of more complex nonlinear dynamics"; quasi-linear and nonlinear analyses are future work (§4.3.2, §5). **Stated**

# Printed slips

- **Eq. (10):** $\mathbf C^0=\mathbf D-(\alpha-1)\mathbf g_L\mathbf l^T-\alpha\mathbf g_R\mathbf r^T$ is printed. *(compiler check, not in the sources)* Inserting the printed fluxes of Eq. (9) into the printed Eq. (7), the $\mathbf g_L$ term is $-2[(1-\alpha_{\mathrm T})e^{-\iota k_h}\mathbf g_L\mathbf r^T+(\alpha_{\mathrm T}-1)\mathbf g_L\mathbf l^T]\hat{\mathbf u}$, which gives $+(\alpha_{\mathrm T}-1)\mathbf g_L\mathbf l^T$ in $\mathbf C^0$ (the printed $\alpha$ is $\alpha_{\mathrm T}$); $\mathbf C^-$ and $\mathbf C^+$ follow as printed.
- **§4.1 against the captions of Figs. 17, 18, 20:** the text assigns the switch test near $\Delta t\approx1.0\times10^{-4}$ to "the second frequency" ($\omega_1=1.3$) and the 1000-element runs to "the lowest frequency" ($\omega_0=0.1$), while the captions print "Numerical solution of $\omega_0=0.1$" (Fig. 17), "$\omega_1=1.3$" (Fig. 18) and "$\omega_1=1.2$" (Fig. 20).
- **Eq. (27):** the Taylor–Green pressure is printed $p=P_0+\frac{\rho_0U_0}{16}[\cos(2x/L)+\cos(2y/L)][\cos(2z/L)+2]$. *(compiler check, not in the sources)* A pressure needs $\rho_0U_0^2$; with $U_0=1$ the values are unaffected.
- **§2.1:** "$N$ the order of the solution polynomial", while the "5th-order" scheme has $N=4$ (superconvergence $2N+1=9$; App.: "3rd order … $N=2$").
- **§3, Fig. 1:** the caption says RK11 "is convectively unstable for pure advection", the text "only marginally stable for pure advection".
- **References:** refs. [27] and [41] are the same work (Vanharen et al., J. Comput. Phys. 337:379–402, 2017) printed twice; ref. [11] prints the authors "Chapelier J-B, M D, Renac F, Lamballais E"; ref. [49] "Hairer E, Wanner G, Solving O. II: Stiff and differential-algebraic problems"; ref. [36] has no venue; refs. [15], [16] no volume.
- **Typos:** "eigenalaysis" (§5), "dumped" for damped (§4.1), "Discontinuous galerkin" (keywords).

# Notation map

| Tonicello et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\theta$ | $k$ | wavenumber (spectral-page convention; **collision** with the TKE $k$) |
| $\omega$ | $\omega_{\mathrm f}$ (page-local) | angular frequency; subscript avoids the specific dissipation rate $\omega$ |
| $\tilde\theta$, $\tilde\omega$ | $k_h$, $\omega_{\mathrm f,h}$ (registry §11) | numerical complex wavenumber and frequency; in the spatial relations (Eqs. 17–22) the prescribed real $\tilde\omega$ is written $\omega_{\mathrm f}$, as on [eigensolution analysis](/methods/eigensolution-analysis.md); **collision:** the source's tilde is not a Favre filter |
| $\iota$ | (imaginary unit) | |
| $N$ | $N$ | used as the polynomial degree; order $N+1$ |
| $h$ | $h$ | element width |
| $\hat x$, $\hat x_i$ | $\xi$, $\xi_i$ | reference coordinate and solution points on $[-1,1]$ |
| $\mathbf D$ | $D_{ij}$ | differentiation matrix |
| $\hat f_L^I$, $\hat f_R^I$ | $f^*$ | interface fluxes |
| $\alpha$ | $\alpha_{\mathrm T}$ (registry §11) | upwinding parameter, 0 upwind, 0.5 centred; $\lambda_{\mathrm{up}}=1-2\alpha_{\mathrm T}$ of [eigensolution analysis](/methods/eigensolution-analysis.md); **collision** with the DG/FV blending factor $\alpha$ |
| $l_j$, $g_L$, $g_R$, $\mathbf l$, $\mathbf r$, $\mathbf g_L$, $\mathbf g_R$ | (Lagrange basis, correction functions and their vectors) | page-local |
| $\mathbf C^-$, $\mathbf C^0$, $\mathbf C^+$, $\mathbf H$, $\mathbf T$ | (neighbour coupling matrices, semi-discrete operator, RK amplification matrix) | page-local |
| $\beta_m$, $\boldsymbol\beta$ | $\beta_m$ (page-local) | Runge–Kutta coefficients; **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $M$, $R$ | $n_{\mathrm{RK}}$ (page-local) | number of RK stages (both printed) |
| $\lambda(\mathbf T)$ | $\rho_{\mathrm s}(\mathbf T)$ (page-local) | spectral radius; **collision** with the Taylor microscale $\lambda$ |
| $\Delta t_{max}$, $\tau$ | $\Delta t_{\max}$, $r_{\Delta t}$ (page-local) | critical step and normalized step; **collision** with the stress $\tau_{ij}$ |
| $\omega_c$, $\delta t$ | $\omega_{\mathrm c}$ (temporal cut-off frequency $\pi/\Delta t$), $\delta t$ (effective sub-step $2\Delta t/n_{\mathrm{RK}}$) | page-local |
| $E_T$, $E_S$ | (temporal and spatial errors) | page-local |
| $\varepsilon_{num}$ | $\varepsilon_{\mathrm{num}}$ (page-local) | numerical dissipation of resolved kinetic energy, Eq. (28) |
| $\beta$ (Eq. 26) | $\beta_{\mathrm v}$ (page-local) | isentropic-vortex strength, 5 |
| $Ma$ | $M$ | Mach number |
| $L$, $U_0$, $\rho_0$, $P_0$, $T=L/U_0$ | (Taylor–Green reference length, velocity, density, pressure, time) | **collision:** $L$ is not the integral scale |
| $A$, $K$, $\Omega$ | (duct-inlet amplitude, transverse wavenumber, frequency $\omega_{\mathrm{in}}$) | **collision** with the rotation-rate tensor $\Omega_{ij}$ |
| $s=\log(\rho^{-\gamma}p)$ | (entropy indicator) | page-local |
| $N_{el}$, $N_x$, $N_y$ | (numbers of elements) | **collision:** the registry's $N_x$ counts grid points |

# Reference list

57 printed references, numbered style ([1]–[57]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Refs. [27] and [41] are one work (Vanharen et al. 2017) printed
twice and are folded into a single entry. Same-author same-year works
(Cockburn 1998, Vincent 2011, Tonicello 2021, Mengaldo 2018, Liang 2009)
take suffixes in printed order. Ref. [11] is printed with a garbled second
author and ref. [49] with a title fragment parsed as an author ("Solving
O."), both kept as printed; ref. [36] has no venue; refs. [17] and [34]
are arXiv preprints and stay their own entries.

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Eigensolution (dispersion–dissipation) analysis](/methods/eigensolution-analysis.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
