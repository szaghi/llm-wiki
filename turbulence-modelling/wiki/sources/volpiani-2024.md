---
type: Source
title: "Volpiani (2024) — A Comprehensive Study About Implicit/Explicit Large-Eddy Simulations with Implicit/Explicit Filtering"
description: "Introduces the Python solver BASIC and compares, on the compressible Taylor–Green vortex, relaxation filtering and kinetic-energy-preserving split forms for central schemes, with and without Smagorinsky, multiscale and dynamic models; implicit LES with a new optimized sixth-order filter performs best."
resource: "doi:10.1007/s10494-024-00577-9"
source_kind: paper
authors: [Volpiani P.S.]
year: 2024
venue: "Flow Turbul. Combust. 113:891–922"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Flow_Turbulence_and_Combustion_Volpiani_A_Comprehensive_Study_About_ImplicitExplicit_Large-Eddy_Simu.pdf"
tags: [implicit-les, filtering, kinetic-energy-preserving, numerical-dissipation, sgs-model, compressible]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Volpiani (2024) introduces BASIC, an open-source compressible Navier–Stokes
solver written in Python 3 with MPI, using explicit centred finite
differences on uniform Cartesian grids and low-storage Runge–Kutta time
stepping. With it the author compares two stabilizations of central schemes
for [implicit LES](/definitions/implicit-les.md) (no subgrid model) and
explicit LES (with a model), on the compressible
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $M=0.085$:

- **relaxation filtering** (RF): an explicit high-order low-pass filter
  $u^f=u-\chi_fD(u)$ applied to the conservative variables every step, which
  makes the run explicitly filtered with a known filter
  ([explicit filtering](/methods/explicit-modal-filtering.md),
  [large-eddy simulation](/definitions/large-eddy-simulation.md));
- **split forms** (SF) of the convective term (Feiereisen, Ducros,
  Kennedy–Gruber), minimally dissipative and (near) kinetic-energy preserving
  ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).

A new 11-point dispersion-optimized derivative (formally sixth order), a new
11-point optimized selective filter (sixth order) and optimized five- and
six-stage Runge–Kutta schemes are designed by constrained minimization of
spectral error integrals
([low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).
In the inviscid case split forms conserve or nearly conserve kinetic energy
while RF drains it, less so at higher filter order. At $Re=1600$ ($64^3$ to
$512^3$), RF implicit LES predicts the directly measured dissipation rate on
every grid while underpredicting the enstrophy-based rate on coarse grids;
the author reads this as the [numerical dissipation](/properties/numerical-dissipation.md)
carrying the subgrid drain. RF implicit LES on $128^3$ also matches the
[DNS](/definitions/direct-numerical-simulation.md) of Dairay et al. (2017) at
$Re$ up to $10000$. Split-form runs without model are noisy and pile up
aliased energy; the [Smagorinsky model](/methods/smagorinsky-model.md),
its multiscale variants and the [dynamic model](/methods/dynamic-procedure.md)
(all [Boussinesq-type](/definitions/boussinesq-hypothesis.md)) do not cure it;
adding RF does. The best result is implicit LES with the optimized filter and
no model; split forms plus RF allow the filter strength to drop from 0.1 to
0.01. The compressible dissipation includes a
[bulk-viscosity](/definitions/bulk-viscosity.md) term; pressure-equilibrium
and entropy-preserving forms are named but not tested
([pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)).

# Version read

Version of record (Springer, Flow Turbul. Combust. 113:891–922; received
24 April 2024, accepted 2 August 2024, online 12 August 2024), 32 pages, all
read; pp. 895, 902 and 918–919 checked visually for Eq. 4, Eqs. 21–25 and
Eqs. 30–40. Page 1 matches Crossref; single author.

# Key claims

Notation: $\mathcal K$ volume-averaged kinetic energy and $\mathcal E_\omega$
enstrophy (per $\rho_0$), $\varepsilon_K=-d\mathcal K/dt$,
$\varepsilon_\omega=2(\mu/\rho_0)\mathcal E_\omega$, $\chi_f$ filter strength,
$N_p$ half-stencil, $c_j$ and $d_j$ derivative and filter coefficients
(page-local; Notation map).

1. BASIC is a structured-grid compressible Navier–Stokes solver in Python 3, parallelized with MPI, and open source ("will be accessible via the author's GitHub page") (§1, §2, Data availability). **Stated**
2. The new 11-point derivative FDo11p, minimizing $\int_{0.2}^{1.5}\lvert k^*\Delta x-k\Delta x\rvert\,d(k\Delta x)$ under three moment constraints, is formally sixth order "instead of the forth order obtained in Bogey and Bailly (2004)" (§2.2.1, Eq. 6, Table 2). **Derived**
3. FDo11p outperforms the standard 11-point scheme for $0.2\le k\Delta x\le1.5$, is close to Bogey–Bailly's there and worse above 1.5 (App. 1, Fig. 19). **Shown** (Fourier analysis)
4. The new 11-point filter RFo11p, optimized over $0.2\le k\Delta x\le1.3$ with a slope penalty, is formally sixth order and more accurate than Bogey–Bailly (2004) at low wavenumbers and than Bogey et al. (2009) at high wavenumbers (§2.2.2, Eq. 8, App. 1, Fig. 20, Table 3). **Shown** (Fourier analysis)
5. The Bogey–Bailly (2004) filter is more dissipative for long waves because of its lower formal order, visible as early kinetic-energy loss of RF-5-2004 (§4, p. 905). **Shown**
6. Higher derivative order lowers dispersion error for short waves, but grid-to-grid waves ($k\Delta x=\pi$) are never resolved (§2.2.1, Fig. 1). **Shown**
7. Inviscid Taylor–Green vortex at $64^3$: $\mathcal K/\mathcal K_0$ at $t=5$ is 0.983, 0.978, 0.963, 0.903, 0.176 for RF-5 to RF-1; 0.978, 0.985, 0.986 for RF-5-2004, -2009, -2024; 0.999 for all SF1 and SF2; 0.998 for all SF3 (Table 1). **Shown**
8. Inviscid case: $\mathcal E_\omega/\mathcal E_{\omega,0}$ at $t=3.5$ is 3.23/3.18/3.06/2.65/0.40 for RF-5 to RF-1; 3.24/3.25/3.26 for RF-5-2004/2009/2024; 3.34 to 2.95 for the split forms; references 3.46 (Brachet et al. 1983) and 3.33, 3.34, 3.23, 3.13 (codes of Johnsen et al. 2010) (Table 1). **Shown**
9. The Feiereisen (SF1) and Kennedy–Gruber (SF3) forms conserve kinetic energy in the inviscid limit, in agreement with Pirozzoli (2010); the Ducros form (SF2) "is not formally conservative" but loses only a few percent by $t=10$ (§4, §6). **Shown**
10. The Blaisdell et al. (1996) form applied to momentum and energy only "was not robust enough and made computations diverge" (§4, §6). **Shown** (stated outcome, no figure)
11. With RF added to split forms in the inviscid case the filter dissipation dominates, as with RF on the divergence form (§4). **Shown** (stated, no figure)
12. All split forms give monotonic enstrophy growth over the period observed; RF enstrophy decreases after some time because of filter dissipation (§4, Fig. 4). **Shown**
13. Cost per 100 iterations per processor (Broadwell Xeon): RF-5 78.9 s, RF-1 49.6 s, SF1-5 115.9 s, SF2-5 156.2 s, SF3-5 298.9 s; operation counts per node $(1+2N_p)$ per derivative plus $(1+2N_p)$ for the filter (RF), $(8+6N_p)$ (SF1, SF2) and $(20+14N_p)$ (SF3) per derivative (Table 1, §4). **Shown** / **Derived**
14. Inviscid spectra at $t=5$: RF-5-2024 and SF1 agree with a $256^3$ reference for $k\le17$; beyond, energy accumulates at the highest wavenumbers, consistent with aliasing onset at $2/3$ of the maximum wavenumber (Johnsen et al. 2010) (§4, Fig. 5). **Shown**
15. Viscous case, RF-5 implicit LES: $\varepsilon_K$ is close to the reference on all grids while $\varepsilon_\omega$ is underpredicted on coarse grids, the two being "not equivalent"; $256^3$ and $512^3$ vorticity contours are "practically indistinguishable" (§5, Figs. 6–8). **Shown**
16. Correct $\varepsilon_K$ with low $\varepsilon_\omega$ means the structures are under-resolved and the scheme's numerical dissipation carries the energy drain: selective filtering "is well adapted for implicit large-eddy simulation" (§5, §6). **Shown** (interpretation)
17. At $Re=1600$ on $64^3$, RF-5-2024 predicts the dissipation peak best among RF-5, RF-5-2009 and RF-5-2024, and is the least dissipative (§5, Fig. 9). **Shown**
18. RF-5-2024 implicit LES on $128^3$ agrees with the DNS of Dairay et al. (2017) at $Re=2500$, $5000$, $10000$ ($768^3$, $1280^3$, $2048^3$), including the dissipation peak; the largest discrepancy is at the highest $Re$ (§5, Fig. 10). **Shown**
19. Split-form runs without model on coarse grids over-predict structures in $\varepsilon_\omega$, build up aliased energy at high wavenumber for every split form, contaminating even low wavenumbers; vorticity fields on $64^3$ and $128^3$ are "extremely noisy" (§5, Figs. 11–13). **Shown**
20. The "Laplacian form" of the viscous terms (Sandham et al. 2002) avoids odd–even decoupling but does not cure the coarse-grid split-form problem (§5, p. 909). **Shown** (stated, no figure)
21. With split forms the Smagorinsky model does not depend on the split formulation, is too dissipative, poorly describes transition and underestimates the dissipation peak; $C_s=0.1$ does not fix it (not shown) (§5, Fig. 15a). **Shown**
22. The multiscale Smagorinsky models improve the dissipation history, especially on $128^3$; the dynamic Smagorinsky model does not improve on them (§5, Figs. 15c–d). **Shown**
23. Adding RF to split-form LES with subgrid models improves the results: aliasing errors not removed affect the solution even with an eddy-viscosity model (cf. Dairay et al. 2017) (§5, Figs. 16–17). **Shown**
24. "Regardless of the model, the best result is achieved for the implicit LES with RF with the optimized filter and no SGS model" (§5, §6). **Shown**
25. Split forms plus RF allow $\chi_f$ to drop from 0.1 to 0.01 (the divergence form with $\chi_f=0.01$ is unstable) and remove the energy pile-up on $64^3$; the best $\chi_f$ "might be case dependent" (§5, Fig. 18). **Shown**
26. The optimized five- and six-stage Runge–Kutta schemes (optimized up to $\omega\Delta t=1.2$) are less dissipative and dispersive than the standard four-stage scheme and have larger stability limits (App. 1, Fig. 21, Table 4). **Shown** (Fourier analysis)
27. Results were independent of the time integrator; production runs use the standard four-stage low-storage scheme (§2.3). **Shown** (stated, no figure)
28. After Aubard et al. (2013), solution quality becomes independent of the derivative scheme beyond a 7-point stencil, while the filter shape strongly affects LES (§5). **Stated**
29. "Implicit LES and explicit LES can be both viable approaches to obtain high-fidelity simulations, as long as dissipation is carefully tuned and guided by the physics"; implicit LES needs only the numerical dissipation mastered and is faster (§6). **Stated**

# Printed slips

- **p. 910:** "For grids 643 and 1288 the vorticity fields are extremely noisy"; the grids are $64^3$ and $128^3$.
- **Eq. 38 (p. 919):** the numerator is printed $\mathcal L_{ij}-\frac13\mathcal L_{ij}\delta_{ij}$; the deviatoric part needs the trace $\mathcal L_{kk}$.
- **§5, p. 906:** the enstrophy-based dissipation is said to be computed "using Eq. (25)", which is the compressible dissipation; the enstrophy relation is Eq. 24.
- **App. 2, Eq. 31:** the "large-small" multiscale model is described as depending on the large scales, but Eq. 31 uses the strain of the full resolved field.
- **Fig. 18 caption:** "RT" and "SF+RT" for RF and SF+RF.
- **Citation labels vs reference list:** "Wang and Rahmani 2021" vs "Wang, Z.J., Salman, R."; "Corentin et al. 2014" vs Carton de Wiart et al.; "Hu 1996" and "Bardina and Ferziger 1980" for three-author works.
- Typos: "standand" (captions of Figs. 1, 2, 19, 20), "forth order" (p. 896), "tree-dimensional" (p. 900), "erros", "stategy" (p. 912), "differencial" (p. 899); item "(vi)" numbered twice (p. 893).
- Not printed: the $C_s$ of the Smagorinsky runs, the weights $c_1$, $c_2$ of Eq. 20, the test-filter kernel and averaging of the dynamic model, the scale-separation operator of the multiscale models.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $\tilde f=\overline{\rho f}/\bar\rho$, $\hat f$ | $\bar\phi$, $\tilde\phi$, $\hat\phi$ | LES filter, Favre filter, test filter ($\hat\Delta=2\Delta$) |
| $\bar\Delta=(\Delta x\Delta y\Delta z)^{1/3}$ | $\Delta$ | |
| $\tau_{ij}$ (Eq. 2) | $\sigma_{ij}$ | viscous stress; **collision** with the SGS stress |
| $\tau^{sgs}_{ij}$, $\tau^{sgs,d}_{ij}$ | $\tau_{ij}$, $\tau^d_{ij}$ (compressible, positive trace) | enters as $\bar\sigma_{ij}-\tau_{ij}$; $\tau_{ii}/2$ is the SGS energy in Eq. 4 |
| $q^{sgs}_j$, $Pr_t=0.6$ | (SGS heat flux), $Pr_t$ | |
| $\rho e$ | $E$ | total energy per unit volume |
| $\lambda$ (conductivity), $r$ (gas constant) | page-local | $\lambda$ **collides** with the Taylor microscale |
| $\nu_t$, $C_s$, $\lvert\tilde S\rvert=(2\tilde S_{ij}\tilde S_{ij})^{1/2}$ | $\nu_t$, $C_s$, $\lvert\tilde S\rvert$ | factor two included |
| $C_i$, $C_I$ | $C_I$ (Yoshizawa isotropic coefficient, page-local) | 0.0066 static |
| $C_d$ | $C_s^2$ (dynamic) | |
| $T_{ij}$, $\mathcal L_{ij}$, $\mathcal M_{ij}$ | (test-level stress), $L_{ij}$ (Favre form), $M_{ij}$ | $T_{ij}$ **collides** with the integrity basis $T^{(n)}$ |
| $u_>$, $u_<$, prime | $\phi^{\mathrm L}$, $\phi^{\mathrm S}$ (large and small resolved scales, page-local) | multiscale models; not the registry's $\phi^>$, $\phi^<$ (resolved and subfilter parts): both are *resolved* scales here |
| $E_k$, $\zeta$ | $\mathcal K$, $\mathcal E_\omega$ (page-local) | $\zeta$ **collides** with the feature vector $\boldsymbol\zeta$ |
| $\epsilon(E_k)$, $\epsilon(\zeta)$, $\epsilon_t=\epsilon_1+\epsilon_2+\epsilon_3$ | $\varepsilon_K$, $\varepsilon_\omega$, $\varepsilon_t$ (page-local) | $\epsilon_2$ the bulk-viscous part |
| $\mu_b$, $\theta=u_{i,i}$ | $\mu_b$, $\nabla\cdot\boldsymbol u$ | $\theta$ **collides** with the momentum thickness |
| $\chi$ | $\chi_f$ (relaxation-filter strength, page-local) | **collision** with the SA $\chi$ |
| $N_p$, $a_j$, $d_j$, $D$, $D_k$, $k^*$ | $N_p$, $c_j$, $d_j$, $D$, $D_k$, $k^*$ (page-local) | half-stencil, derivative coefficients ($c_j$ as on the low-dissipation page), filter coefficients ($d_j$ as on the explicit-filtering page, $e_j$ on the low-dissipation page), filter operator, damping function, effective wavenumber; $a_j$ **collides** with the unnormalized WENO weight $a_k$ |
| $\alpha$, $\beta$ (Eq. 14) | $\alpha_{\mathrm{KG}}$, $\beta_{\mathrm{KG}}$ (page-local) | Kennedy–Gruber; **collisions** with the DG blending factor and the field-inversion multiplier |
| $C^D$, $C^\phi$, $C^u$, $C^\rho$ | page-local | divergence and split forms |
| $\alpha_l$, $\gamma_j$, $g$, $\omega^*$ | page-local | Runge–Kutta coefficients, amplification factor, effective frequency; $\gamma_j$ **collides** with $\gamma$ |
| $Re$, $M$ | $Re$, $M$ | $Re=1600$; $M=0.085$ |

# Reference list

65 printed references in Springer author–year style, alphabetical; merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
The cited Cao et al. (2022, Phys. Fluids, implicit LES analysis) is the
planned source `cao-2022-c`, not `cao-2022`; Bernades et al. (2023) and
Wang (2013) are the ingested sources [Bernades et al. (2023)](/sources/bernades-2023.md)
and [Wang et al. (2013)](/sources/wang-2013.md), and Kiris et al. (2023) is
the same work as the planned source of that key. Items printed without volume or pages: Asada et al. (2023), Cao
et al. (2022), Cook (2007), Kiris et al. (2023). Boris (1990) is a book
chapter; Feiereisen et al. (1981), Kraft (1988) and Larsson et al. (2007) are
reports. Text labels that differ from the list are recorded under Printed
slips. No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27), cited further in chunk 10. This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Variational multiscale method](/methods/variational-multiscale-method.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
