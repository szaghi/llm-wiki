---
type: Source
title: "Bryngelson et al. (2021) — MFC: An open-source high-order multi-component, multi-phase, and multi-scale compressible flow solver"
description: "Program description of MFC 1.0, an open-source Fortran/MPI finite-volume solver for diffuse-interface multi-component and bubbly compressible flows: WENO reconstruction of primitive or characteristic variables, HLLC fluxes, Gaussian face quadrature, five- and six-equation models, verification, validation and parallel scaling."
resource: "doi:10.1016/j.cpc.2020.107396"
source_kind: paper
authors: [Bryngelson S.H., Schmidmayer K., Coralic V., Meng J.C., Maeda K., Colonius T.]
year: 2021
venue: "Comput. Phys. Commun. 266:107396"
local_file: "/home/stefano/papers/mosaic/weno-teno/2021_Crossref_Computer_Physics_Communications_Bryngelson_MFC_An_open-source_high-order_multi-component_multi-phase_an.pdf"
tags: [software, multiphase, interface-capturing, weno, finite-volume]
timestamp: 2026-10-22T12:00:00Z
---

# Summary

A software paper describing version 1.0 of [MFC](/software/mfc.md) (Multi-component
Flow Code). MFC is GPL-licensed, written in Fortran 90 with MPI and Python input
scripts, and split into pre-processing, simulation and post-processing. Its physical
models are the [five-equation](/definitions/five-equation-model.md) diffuse-interface
model of Kapila et al. (with the $K\nabla\cdot v$ term) and its variants without $K$,
the six-equation pressure-disequilibrium model with infinite relaxation at every stage,
an ensemble-averaged bubbly-flow model with Keller–Miksis dynamics, and the
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md).

The numerical method follows Coralic & Colonius and is documented only at a high level.
It is a finite-volume scheme with first-, third- or fifth-order
[WENO](/methods/weno-js-reconstruction.md) reconstruction of primitive, conservative or
[characteristic](/methods/characteristic-decomposition.md) variables, with
[mapped WENO](/methods/mapped-weno.md) among the cited references but no weight
formulas printed. Fluxes come from [HLLC](/methods/hll-riemann-solvers.md) (HLL and
exact also available), integrated with two-point Gauss quadrature on each face.
Volume fractions are clipped and renormalized for mixture properties only, a weak form
of [bound preservation](/properties/bound-preservation.md). An optional limiter blends
a first-order flux with the WENO flux through [TVD limiters](/definitions/total-variation-diminishing.md)
driven by a volume-fraction ratio, a [hybrid](/methods/hybrid-weno.md) localised to
interfaces. Time stepping is the third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
scheme of Gottlieb & Shu.

Verification and validation use the [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
(feature velocities within 10% of Haas & Sturtevant), a
[shock–water-column](/benchmarks/shock-water-column.md) and a droplet aerobreakup, a
spherical bubble collapse (WENO keeps sphericity better than a MUSCL code), a steady
[isentropic vortex](/benchmarks/isentropic-vortex.md) (fifth order only with
fourth-order face quadrature) and the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).
Earlier [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md) are
recalled from prior papers. Strong and weak scaling is near ideal up to 4096 cores.
Nothing is proved.

# Version read

arXiv:1907.10512v1 [physics.comp-ph], 24 Jul 2019, footer "Preprint submitted to
Computer Physics Communications, July 25, 2019": the submitted preprint, about 1.5 years
older than the CPC version of record (DOI assigned 2020, issue 2021). 25 pages (19 of
text, 6 of references), all read. Title and authors match Crossref. Content, test cases
and numbering of the published version may differ; section, equation, figure and
reference numbers here are those of arXiv v1.

# Key claims

Registry notation (see the notation map): the source's state $q$ is $u$, its velocity
$u$ is $v$, its face states $q^L,q^R$ are $u^-,u^+$, its semi-discrete operator $L$ is
$\mathcal L$, its volume-fraction ratio $\chi_i$ is the slope ratio $r_i$, its volume
fractions $\alpha_k$ are $\phi_k$ and its stiffening constants $\pi_{\infty,k}$ are
$p_{\infty,k}$ (registry §10).

1. MFC solves mechanical-equilibrium multi-component flows in the form $\partial_tu+\nabla\cdot f(u)+h(u)\nabla\cdot v=S(u)$, with a non-conservative $h\nabla\cdot v$ term (§3, Eq. (1)). **Stated**
2. The Kapila et al. five-equation model includes $K\nabla\cdot v$ in the volume-fraction equation, $K$ from Eq. (8); it is thermodynamically consistent and gives the Wood mixture sound speed $\frac1{\rho c^2}=\sum_k\frac{\phi_k}{\rho_kc_k^2}$ (Eq. (9)) (§3.1). **Stated** (cited)
3. The Allaire et al. and Massoni et al. five-equation models omit $K$ and "do not strictly obey the second-law of thermodynamics, nor reproduce the correct mixture speed of sound (9)"; MFC supports them too (§3.1). **Stated**
4. The $K$ term "can result in numerical instabilities for problems with strong compression or expansion in mixture regions due to its non-conservative nature"; the model choice is left to the user (§3.1, §3.2). **Stated**
5. The six-equation model with infinite pressure relaxation at every Runge–Kutta stage gives a unique pressure at stage end, so the five- and six-equation models reconstruct the same variables; it costs about 5% more than the five-equation model for spherical bubble collapse (§4.6). **Stated**
6. After infinite relaxation the effective mixture sound speed of the six-equation model is the Wood speed (9), although its frozen speed is Eq. (14) (§3.2). **Stated**
7. The spatial discretization is finite volume with fifth-order WENO reconstruction of primitive or characteristic variables at cell faces; conservative-variable reconstruction and first/third-order WENO are also supported (§2.2, §4.1). **Stated**
8. Face fluxes and source terms are integrated with two Gauss points per direction, called "fourth-order" (Eqs. (29), (32)); $\nabla\cdot v$ uses a midpoint rule (Eq. (31)) (§4.1). **Stated**
9. On the 2D isentropic vortex the $L_\infty$ density error converges at second order with second-order cell averaging and at fifth order with fourth-order cell averaging: "the 4th-order-accurate cell averaging we employ is required to achieve 5th-order accuracy associated with the WENO reconstructions" (§5.4, Fig. 5a). **Shown**. *(compiler check, not in the sources: a two-point Gauss rule has an $O(\Delta y^4)$ face-average error, which bounds the formal order of the multi-dimensional scheme at four; the paper does not comment on the observed slope of 5.)*
10. HLLC is the default Riemann solver; HLL and exact solvers are available (§2.2, §4.1). **Stated**
11. Volume fractions are clipped to $[0,1]$ and renormalized to sum to one (Eq. (33)) only when mixture properties are computed, so mass conservation is not polluted (§4.2.1). **Stated**
12. "The WENO schemes we utilize are, in general, not TVD" and can become unstable "even when the usual CFL criteria are met"; an optional limiter blends a first-order flux with the WENO Riemann flux, driven by the volume-fraction ratio $r_i$ (Eq. (34)) and one of minmod, MC, ospre, superbee, Sweby, van Albada or van Leer, to localise the added dissipation (§4.2.2). **Stated**
13. Reconstructing conservative variables at an advected air–water interface produces spurious oscillations and even negative pressures; primitive-variable reconstruction keeps velocity and pressure free of oscillations to round-off (§5.5, recalled from Coralic & Colonius). **Stated** (shown in the cited work)
14. In cylindrical coordinates no modified azimuthal WENO weights are used (so high order away from discontinuities is not ensured); the axis lies on a cell face, an even number of azimuthal cells is required, a spectral filter near the axis relaxes the CFL, and the treatment is second-order accurate (§4.3). **Stated**
15. Time integration uses the three-stage third-order TVD Runge–Kutta scheme of Gottlieb & Shu (Eq. (39)); orders 1–5 are supported (§4.5). **Stated**
16. Shock–helium-bubble interaction (Mach 1.22): every simulated feature velocity is within 10% of experiment and generally within about 5% of the measured means, with no spurious oscillations in numerical schlieren (§5.1, Fig. 1). **Shown**
17. A Mach 1.47 shock on a 4.8 mm water cylinder reproduces the primary and secondary wave systems of the Igra–Takayama interferograms at $t=16$ and $32\,\mu$s (§5.2, Fig. 2). **Shown** (qualitative)
18. Water-droplet aerobreakup (helium shock, post-shock Mach 0.59) agrees qualitatively on shear-induced entrainment (§5.2, Fig. 3). **Shown** (qualitative)
19. In a spherical air-bubble collapse (water at 10 times higher pressure) the radius follows Keller–Miksis, and WENO (MFC) keeps sphericity better than the MUSCL scheme of ECOGEN with the same model (§5.3, Fig. 4). **Shown**
20. ECOGEN is "built upon an intrinsically low-order MUSCL scheme that can inhibit both efficient simulation and physically fidelity when compared to the WENO schemes" (§1). **Stated** (supported by claim 19)
21. On the 3D Taylor–Green vortex the kinetic-energy dissipation rate closely matches the spectral solution of Brachet et al., with its peak near $t\approx5$ (§5.4, Fig. 5b). **Shown**
22. A Mach 8.96 helium shock on an air interface and the Cocchi et al. gas–liquid shock tube match exact solutions without spurious oscillations (§5.5, recalled). **Stated**
23. The bubbly-flow model reproduces the linear-theory phase speed and attenuation of a bubble screen (§5.5, recalled). **Stated**
24. Strong scaling and speedup on a $500^3$ grid and weak scaling at $50^3$ cells per core stay "very near the ideal threshold until the number of cores is 4096" (§7, Fig. 8). **Shown**
25. In the illustrative cases (shock-induced bubble collapse in a vessel phantom, humpback-whale bubble-net acoustics) curved interfaces stay "smooth and free of spurious oscillations" despite large density and viscosity ratios (§6). **Shown** (qualitative)

# Printed slips

- Eq. (30): Gauss points printed as $y_{j_l}=y_j+(2l+1)\frac{\Delta y_j}{2\sqrt3}$, $l=1,2$, which lie outside the face (offsets $\frac{3}{2\sqrt3}\Delta y_j$, $\frac{5}{2\sqrt3}\Delta y_j$); two-point Gauss points are $y_j\pm\frac{\Delta y_j}{2\sqrt3}$ (checked visually, p. 10).
- §7: "288 compute nodes, each containing two 2.6 GHz six-core AMD Opteron processors" is 3456 cores, but scaling is reported to 4096 cores and the axes reach $10^4$.
- §6.1: "by $t=66$ ns it impinges the vessel surface", but the snapshots of Fig. 6 are at $t=0,39,46,58$ ns; typo "lareg density-".
- "References" heading printed twice.
- Ref. [41] (Coralic & Colonius) printed "J. Comp. Phys. 219 (2014) 715–732", the volume and pages of [40] (Johnsen & Colonius 2006), and inconsistent with 2014.
- [43] and [74] are the same Meng 2016 PhD thesis printed twice.
- [48] "C. W. Schu"; [50] "A. K. Henrick, T. D. A. an d J. M. Powers" (Henrick, Aslam, Powers); [39] "J. Comp. Phys. 456 (1999)"; [59] cites the Lustre synchronous programming language for the Lustre file system; [61] "The Visualization Handboo 717 (2005)"; [65] "Shock waves 26 (2009)"; [99] "Fishery Bull. 8 (1982)".
- Symbol reuse: $\mu$ (relaxation coefficient, Eq. (11); liquid viscosity, Eq. (20)), $\sigma$ (surface tension; width of the discrete delta, Eq. (37)), $k$ (component index; $z$-cell index).

# Notation map

| Bryngelson et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $q_{i,j,k}$ | $u$, $\bar u_{i,j,k}$ | state vector (with $\phi_1$ or phasic energies), cell average |
| $F$, $F^x,F^y,F^z$ | $f^{(d)}$ | physical fluxes; $F_{i+1/2,j,k}$ face average |
| $\hat F(q^L,q^R)$ | $h(u^-,u^+)$ | HLLC by default |
| $q^L_{i+1/2}$, $q^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | reconstructed face states |
| $h(q)$, $s(q)$ | $h(u)$ kept, $S(u)$ | **$h$ collides with the two-point flux $h$**; $s$ is the source, **not the entropy $s$** |
| $u=(u,v,w)$ | $v=(v_1,v_2,v_3)$ | velocity |
| $\rho$, $p$, $E$, $e$, $c$ | $\rho$, $p$, $E/\rho$, $e$, $c$ | **the source's $E$ is specific** |
| $\alpha_k$, $\rho_k$, $e_k$, $Y_k$, $N_k$ | $\phi_k$, $\rho_k$, $e_k$, $Y_k$ (registry §10), $N_k$ kept | volume fraction, phasic density and energy, mass fraction, number of components; **the source's $\alpha_k$ collides with the unnormalized WENO weights** |
| $\gamma_k$, $\pi_{\infty,k}$ | $\gamma_k$, $p_{\infty,k}$ (registry §10) | stiffened-gas parameters; **$\gamma_k$ collides with the TENO measure $\gamma_k$** |
| $K$ | kept | Kapila coefficient (Eq. (8)); **collides with the TENO stencil size $K$** |
| $T$, $D$, $\eta$ | kept | viscous stress, strain rate, shear viscosity; **$\eta$ collides with the entropy $\eta$** |
| $\mu$, $p_I$, $z_k$, $\delta p$ | kept | relaxation coefficient (also viscosity), interfacial pressure, impedance, pressure jump |
| $\chi_i$ | $r_i$ | volume-fraction ratio of the flux limiter (Eq. (34)); **$\chi$ collides with the TENO $\chi_k$** |
| $u^*$ | kept | contact velocity from the Riemann solver |
| $L$ | $\mathcal L$ | semi-discrete operator; **$L$ is $R^{-1}$ in the registry** |
| $\Delta x_i$, $I_{i,j,k}$ | $\Delta x$ (non-uniform), $I_i$ | stretched grids allowed |
| $N$ (Fig. 5a) | $N_x$ | cells per direction |
| $\varepsilon$ | kept | Taylor–Green dissipation rate, not $\epsilon$ |
| $\sigma$, $\psi$ | kept | surface tension or delta width; bubble sphericity |

# Reference list

99 printed references, numbered [1]–[99], all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `bryngelson-2021`. The printed
duplicate [43]/[74] (Meng 2016 thesis) is kept as two keys, `meng-2016` and
`meng-2016-b`, the second noted as a duplicate print. Doubtful items are kept as
printed: [50] garbled author string (transcribed as Henrick, Aslam, Powers), [61]
truncated venue, [41] copied volume and pages, [58] web reference (Silo), [55] "under
review (2019)", [36] arXiv preprint. No DOIs are printed.

# Pages created or updated

Chunk 2 (2026-10-22), cited further in chunks 3–4 (2026-10-22/23). This source is cited on:

* [Bound preservation](/properties/bound-preservation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [MFC](/software/mfc.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shock–water-column interaction](/benchmarks/shock-water-column.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
