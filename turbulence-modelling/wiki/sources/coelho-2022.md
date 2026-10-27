---
type: Source
title: "Coelho et al. (2022) — Global fluid simulation of plasma turbulence in a stellarator with an island divertor"
description: "Extends the GBS two-fluid drift-reduced Braginskii code to non-axisymmetric fields and runs a global, flux-driven simulation of a five-period stellarator with a 5/9 island divertor, finding a coherent field-aligned ballooning-like m=4 mode, no broad-band turbulence and no blobs."
resource: "doi:10.1088/1741-4326/ac6ad2"
source_kind: paper
authors: [Coelho A., Loizu J., Ricci P., Giacomin M.]
year: 2022
venue: "Nucl. Fusion 62:074004"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Nuclear_Fusion_Coelho_Global_fluid_simulation_of_plasma_turbulence_in_a_stellarato.pdf"
tags: [plasma, numerical-dissipation]
timestamp: 2026-10-27T15:51:00Z
---

# Summary

Coelho et al. (2022) report what they call the first global, two-fluid,
flux-driven simulation of a stellarator with an island divertor. The GBS
code, used for a decade on tokamak boundary turbulence, is extended to
non-axisymmetric magnetic fields. GBS solves the drift-reduced Braginskii
equations in the electrostatic limit, without gyroviscous terms or
neutrals, and evolves the full fields without splitting equilibrium and
fluctuations. The authors apply what they call the Boussinesq
approximation (p. 3, citing [20], not defined further in the paper); it is
a plasma-fluid approximation, unrelated to the eddy-viscosity hypothesis of
RANS closures. The geometric operators of the stellarator are expanded in three
small parameters (field-component ratio $\sim0.1$, normalized mirror ratio
$\lesssim0.1$, perpendicular-to-parallel length-scale ratio $\sim0.01$,
checked a posteriori) and only leading-order terms are kept. The grid is
cylindrical, time stepping explicit fourth-order Runge–Kutta, space
fourth-order finite differences. There is no turbulence closure: small
perpendicular and parallel diffusion terms are added "to improve the
numerical stability", and the authors state that they produce much less
perpendicular transport than the turbulence, a claim bearing on
[numerical dissipation](/properties/numerical-dissipation.md) that is not
quantified.

The vacuum field is built from Dommaschk potentials: five field periods,
stellarator symmetry, a 5/9 island chain around nested surfaces, rotational
transform from 0.500 on axis to 0.555 at the last closed flux surface
(LCFS), very small shear; the islands strike the top and bottom walls as in
the W7-X island divertor. In the quasi-steady state the plasma is confined
inside the LCFS and the radial electric field is negative (ion root). A
single coherent field-aligned mode with poloidal and toroidal numbers
$m=4$, $n=5$ rotating in the ion diamagnetic direction dominates; no
broad-band turbulence and no blobs appear, unlike tokamak boundary
simulations. About 80% of the radial particle transport across the LCFS
is the time-averaged fluctuating $E\times B$ flux, mostly carried by this
mode, and the flux peaks on the high-field side. A non-local linear
eigenvalue analysis reproduces an edge-localized $m=4$, $n=5$ eigenmode
whose flux-balance amplitude matches the nonlinear run; removing the
curvature drive changes it, removing the drift-wave drive does not, so the
authors call the mode "ballooning-like", pending a linear analysis in more
complex geometry.

# Version read

arXiv preprint arXiv:2201.10871v1 [physics.plasm-ph], 26 January 2022
(LaTeX preprint layout; the text calls itself "this Letter"), 11 pages,
all read (equations of pp. 3, 7–9 checked visually). Title and authors
match the Crossref record of the version of record (Nucl. Fusion
62:074004); page 1 prints the first author as "A. J. Coelho", Crossref as
"Coelho A.". The journal DOI is not printed on the preprint. Locators are
those of the preprint.

# Key claims

1. This is "the first global, two-fluid, flux-driven simulation of a stellarator with an island divertor" (p. 3; restated p. 9). **Stated**
2. GBS is extended from tokamaks to non-axisymmetric fields; it solves the drift-reduced Braginskii equations [27] in the electrostatic limit with the (plasma) Boussinesq approximation [20], neglecting gyroviscous terms and neutral coupling, and evolves all quantities without separating equilibrium and fluctuations (p. 3, Eqs. 1–7). **Stated**
3. The drift-reduced Braginskii model holds in the high-collisionality regime, "often justified in the plasma boundary of magnetic fusion devices as well as in the core of low-temperature devices" (p. 3). **Stated**
4. Small numerical diffusion terms ($D_n\nabla_\perp^2n$, $D_n^\parallel\nabla_\parallel^2n$ and analogues) are added for numerical stability, and "the simulation results show that they lead to significantly lower perpendicular transport than turbulence" (p. 4). **Stated** (no quantitative evidence shown)
5. The geometric operators are expanded in $\delta_B=B_R/B\sim B_Z/B$, $\Delta_B=(B_{\max}-B_{\min})/B_{\mathrm{avg}}$ and $\sigma_\ell=l_\perp/l_\parallel$, keeping leading-order terms; here $\delta_B\sim0.1$, $\Delta_B\lesssim0.1$ and, a posteriori, $\sigma_\ell\sim0.01$ (p. 4). **Stated**
6. Numerics: cylindrical grid $(R,\varphi,Z)$ with rectangular cross-section $L_R\times L_Z$, explicit fourth-order Runge–Kutta in time and fourth-order finite differences in space [31, 24] (p. 4). **Stated**
7. Vacuum field from Dommaschk potentials [32]: five field periods, stellarator-symmetric, a 5/9 island chain around nested surfaces (rotating ellipses without torsion), rotational transform from 0.500 on axis to 0.555 at the LCFS, very small shear (pp. 4–5, Fig. 1). **Stated**
8. Parameters: $\rho_*^{-1}=1000$, $\nu_0=0.1$, $\tau_T=1$, $\chi_{\parallel e,i}=\eta_{0e,i}=1.0$, perpendicular numerical diffusion 10 on all fields, $D_n^\parallel=D_{\omega}^\parallel=1$, $L_R=380\rho_{s0}$, $L_Z=230\rho_{s0}$, grid $N_R\times N_Z\times N_\varphi=200\times120\times200$, time step $2.9\times10^{-6}R_0/c_{s0}$, equal density and temperature sources localized near the LCFS (p. 5). **Stated**
9. From a noisy start the run reaches a quasi-steady state in which sources, parallel and perpendicular transport and wall losses balance; particles are mostly exhausted where field lines strike the vessel (p. 5, Fig. 2). **Shown**
10. The plasma is well confined inside the LCFS; the time-averaged potential is negative in the core and positive in the edge, so the radial electric field is negative, the ion-root regime "expected as well in the neoclassical high-collisional regime" (p. 5, Fig. 3). **Shown** (sign of the field) / **Stated** (neoclassical expectation)
11. A coherent, field-aligned mode with $m=4$ ($k_y\rho_{s0}\approx0.04$) and $n=5$, rotating in the ion diamagnetic direction, dominates the global dynamics (pp. 5–6, Figs. 2, 4). **Shown**
12. "No broad-band turbulence nor blobs are observed, highly contrasting with typical tokamak boundary simulations [34, 35]" (p. 6). **Shown** (absence) / **Stated** (contrast)
13. An $m=4$ mode also appears with weaker and stronger sources and at $\rho_*^{-1}=1500$ and 2000 ("not shown") (p. 6). **Stated**
14. About 80% of the radial particle transport across the LCFS is the time-averaged fluctuating $E\times B$ flux $\Gamma^x_{E\times B}=\langle n'u^{x\prime}_{E}\rangle_t$ (Eq. 8), with its largest share from the $m=4$ mode (p. 7). **Shown** (numbers not tabulated)
15. The flux of Eq. 8 agrees well with the single-coherent-mode flux $\Gamma^c=\frac{k_y}{2B}|n'\Phi'|\sin\delta_{\Phi-n}$ (Eq. 9) built from the simulated amplitudes and phase difference (p. 7). **Stated** (no comparison figure)
16. On the unfolded LCFS the $E\times B$ flux peaks on the high-field side; the larger fluctuation amplitude at $\theta=\pi$ outweighs the phase-difference factor, which is larger on the low-field side (p. 7, Fig. 5). **Shown**
17. Non-local linear theory (Eq. 10; perturbations $\propto e^{\gamma_{\mathrm{lin}}t+i(m\theta-n\varphi)}$ with radial amplitude profiles, curvature simplified to a circular-tokamak form evaluated at the low-field side) gives an $m=4$, $n=5$ eigenmode large near the LCFS and decaying towards the core, like the nonlinear perturbation (p. 8, Fig. 6). **Shown**
18. The flux-balance amplitude estimate (Eqs. 11–12) exceeds the nonlinear amplitudes "by orders of magnitude" for most $(m,n)$, but gives $|n'\Phi'|\sim0.4$ for $(4,5)$, comparable to the nonlinear run (p. 9). **Derived** (Eq. 12 from Eqs. 9, 11) / **Shown** (estimate)
19. Removing the drift-wave drive (parallel temperature and pressure gradients in Ohm's law, Eq. 4) leaves the eigenmode nearly unchanged; removing the ballooning drive (curvature term of the vorticity equation, Eq. 6) changes it and removes its edge localization; the mode is therefore "ballooning-like", "a finding to be confirmed by linear analysis that take into account a more complex geometry" (p. 9, Fig. 6). **Shown**
20. From the literature: W7-X filaments stay essentially on their flux surface with radial velocity ~100 m/s and poloidal velocities of a few km/s; fluctuation spectra are broad-band at 1–10 kHz with quasi-coherent modes at 10–50 kHz; tokamak blobs travel ballistically at a few km/s (p. 2). **Stated**
21. In this Dommaschk-potential configuration the dynamics is dominated by a coherent low-$m$ mode with no blobs detaching into the scrape-off layer, in strong contrast with tokamak boundary simulations; the cause and the link with experiments are left to ongoing work (pp. 9–10). **Stated**

# Printed slips

- **Potential symbol (Eqs. 9, 12 and the text after Eq. 12).** The potential is $\Phi$ in Eqs. 1–8 and in the Fig. 5 label "$|\tilde n\tilde\Phi|$", but Eqs. 9 and 12 write "$|\tilde n\tilde\phi|$", while $\phi$ is the toroidal angle (p. 4, Eq. 10).
- **Name spelling.** "Dommasck potentials" (p. 4) and "Dommashck potentials" (p. 9), against "Dommaschk" in the abstract and in ref. [32].
- **Acknowledgments.** "Brendan Shannahan"; refs. [18, 19, 35] print "Shanahan".
- **Reference data.** Refs. [31] and [34] (both Paruta et al., Physics of Plasmas) print the same volume 26 with years 2018 and 2019. Ref. [4] (Ohyabu et al., Nuclear Fusion 34:387) prints the year 1984; Crossref gives 1994 for that volume and page (DOI 10.1088/0029-5515/34/3/i07). For ref. [31], Crossref gives Physics of Plasmas 25:112301 (2018) against the printed volume 26. Ref. [18] prints no page or article number; ref. [28] prints "73:10".
- **Typos.** "the the non-linear simulation" (p. 8); "linear analysis that take into account" (p. 9); "balistically" (p. 2).
- **Pressures.** $p_e$ and $p_i$ appear in Eqs. 1–6 but are not defined in the text.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\omega$ | $\omega_{\mathrm{pol}}$ (page-local scalar polarization vorticity) | **collision** with the specific dissipation rate $\omega$ and the vorticity vector $\omega_i$ |
| "Boussinesq approximation" | (plasma-fluid approximation, not defined in the paper) | **collision of terms:** not the Boussinesq eddy-viscosity hypothesis |
| $\tilde u$, $\langle u\rangle_t$ | $u'$, $\langle u\rangle$ (time average) | **collision:** the source's tilde is a time-average fluctuation, not a Favre filter |
| $\phi$ (toroidal angle) | $\varphi$ (page-local) | the source also prints $\phi$ for the potential in Eqs. 9, 12 |
| $\Phi$ | $\Phi$ (page-local electrostatic potential) | |
| $\nu=\nu_0T_e^{3/2}$ | $\nu_{\mathrm{Sp}}$ (page-local normalized Spitzer resistivity) | **collision** with the kinematic viscosity $\nu$ |
| $\tau=T_{i0}/T_{e0}$ | $\tau_T$ (page-local) | **collision** with the SGS stress $\tau_{ij}$ |
| $\delta$, $\Delta$, $\sigma$ | $\delta_B$, $\Delta_B$, $\sigma_\ell$ (page-local expansion parameters) | **collision** with the boundary-layer thickness, the filter width and the plasma $\sigma$ symbols |
| $\overline B$ | $B_{\mathrm{avg}}$ (toroidal average of $B$) | the overbar is not an LES filter |
| $\gamma$ | $\gamma_{\mathrm{lin}}$ (page-local linear growth rate) | **collision** with the ratio of specific heats |
| $\eta_{0e}$, $\eta_{0i}$ | (normalized parallel viscosities) | not the Kolmogorov length nor the magnetic diffusivity $\eta_m$ |
| $D_f$, $D_f^\parallel$, $\chi_{\parallel e,i}$ | (numerical perpendicular and parallel diffusion coefficients; parallel conductivities) | |
| $n$ | (plasma density; also the toroidal mode number) | **collision** inside the source |
| $m$ | (poloidal mode number) | |
| $\rho_{s0}$, $c_{s0}$, $\rho_*=\rho_{s0}/R_0$ | (sonic Larmor radius, sound speed, normalized machine size) | |
| $(R,\phi,Z)$ | $(R,\varphi,Z)$ cylindrical coordinates | not the registry's $(x,y,z)$ wall axes |
| $\Gamma^x_{E\times B}$, $\Gamma^c$, $\delta_{\Phi-n}$ | (fluctuating radial flux, single-mode flux, phase difference) | |
| $\Omega$, $\partial\Omega$ | (volume inside the LCFS, its surface) | not the rotation-rate tensor |

# Reference list

35 printed references, numbered style ([1]–[35]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Same-author same-year entries take suffixes in printed order
(`giacomin-2020`, ref. [22]; `giacomin-2020-b`, ref. [24]). Ref. [21] is an
arXiv preprint "Submitted to JCP: arXiv:2112.03573" with no printed year,
kept as its own entry `giacomin-2022` and never folded into a published
version. Ref. [27] (Zeiler, IPP report 5/88) is a technical report. The
year and volume problems of refs. [4], [31], [34] are recorded in the
entries' notes (`ohyabu-1994`, keyed by the Crossref year; `paruta-2018`,
with the Crossref volume 25; `paruta-2019`). No printed
duplicates or unparseable items.

# Pages created or updated

Chunk 3 (2026-10-26). This source is cited on:

- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Reduced MHD and Elsasser variables](/definitions/reduced-mhd.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
