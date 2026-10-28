---
type: Source
title: "Simonis et al. (2022) — Temporal large eddy simulation with lattice Boltzmann methods"
description: "First combination of temporal large-eddy simulation, closed by the temporal direct deconvolution model, with a multiple-relaxation-time lattice Boltzmann method: the time-filtered residual stress enters as the second Hermite moment of the filtered BGK residual; Taylor–Green vortex calibration, comparison with spectral-element TLES and an error analysis."
resource: "doi:10.1016/j.jcp.2022.110991"
source_kind: paper
authors: [Simonis S., Oberle D., Gaedtke M., Jenny P., Krause M.J.]
year: 2022
venue: "J. Comput. Phys. 454:110991"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Computational_Physics_Simonis_Temporal_large_eddy_simulation_with_lattice_Boltzmann_method.pdf"
tags: [lattice-boltzmann, temporal-les, approximate-deconvolution, taylor-green-vortex, sgs-model]
timestamp: 2026-10-27T15:46:00Z
---

# Summary

Simonis et al. (2022) combine temporal large-eddy simulation (TLES),
which filters the incompressible Navier–Stokes equations in time with a
causal exponential kernel of width $\Theta$ instead of in space, with the
[lattice Boltzmann method](/methods/lattice-boltzmann-method.md). For the
exponential kernel the filter has a differential form, so the unfiltered
field is recovered exactly by direct deconvolution and the temporal
residual stress obeys a closed relaxation equation: the temporal direct
deconvolution model (TDDM) of Oberle, Pruett & Jenny (2020), with no
model constant besides $\Theta$. In the filtered BGK Boltzmann equation of
Malaspinas & Sagaut the second Hermite moment of the residual is, as the
paper notes, usually closed by an eddy viscosity ([Smagorinsky](/methods/smagorinsky-model.md),
[WALE](/methods/wale-model.md) and other lattice Boltzmann
[LES](/definitions/large-eddy-simulation.md) models are listed); the
authors instead identify it with the temporal residual stress and advance
it by the TDDM, discretized to first or second order, inside a D3Q19
multiple-relaxation-time (MRT) collision implemented in OpenLB. The
closure is local in space and costs memory for past time levels.

The only test is the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
framed by the authors as decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
At $Re=800$ the filter width ($\Theta=10\Delta t$) and lattice Mach
number (0.1) are calibrated. At $Re=3000$ the method is compared with
under-resolved DNS and with a [spectral-element](/methods/spectral-element-method.md)
TLES in [Nek5000](/software/nek5000.md), against spectral-element
[DNS](/definitions/direct-numerical-simulation.md): both TLES variants
improve the peak of the total dissipation rate over under-resolved DNS.
An error analysis in the subgrid-activity framework of Geurts & Fröhlich
shows the subgrid activity decreasing with refinement and an error
plateau the authors attribute to the compressibility defect of the
lattice Boltzmann method. The authors conjecture that MRT lattice
Boltzmann without a model already acts as an
[implicit LES](/definitions/implicit-les.md), its
[numerical dissipation](/properties/numerical-dissipation.md) being about
half the total dissipation at $N_x=64$.

# Version read

Version of record (Elsevier; received 4 December 2020, online 20 January
2022), 19 pages, all read; pp. 2–6, 9, 11–12, 14 and 16 also read
visually to recover $\Theta$ and equations lost by the text layer. Page 1
matches the metadata; no identity issue. Equation, section, table and
figure numbers are those of this version.

# Key claims

Page-local symbols: the overbar is here a causal exponential **time**
filter of width $\Theta$, $\Theta=\tilde\Theta\Delta t$;
$\hbar=\Delta t/\Theta$ the temporal subgrid resolution; $\tau_{ij}$ the
temporal residual stress $\overline{u_iu_j}-\bar u_i\bar u_j$ (positive
trace); $K(t)$ and $\mathcal Z(t)$ the volume-averaged kinetic energy and
enstrophy (no factor ½ in $\mathcal Z$); $\varepsilon_{\mathrm{tot}}=-dK/dt$,
$\varepsilon_{\mathrm{res}}$, $\varepsilon_{\mathrm{mod}}=\varepsilon_{\mathrm{tot}}-\varepsilon_{\mathrm{res}}$
the total, enstrophy-based resolved and model dissipation rates;
$s(N_x,t)=|\varepsilon_{\mathrm{mod}}|/|\varepsilon_{\mathrm{tot}}|$ the
subgrid activity; $\mathrm{Ma}$ the lattice Mach number; UDNS
under-resolved DNS; TLESo1, TLESo2 TLES with first- and second-order
TDDM; AS, DS acoustic and diffusive scaling; EOC experimental order of
convergence.

1. To the authors' knowledge neither TLES nor the TDDM had been combined with the lattice Boltzmann method before (§1). **Stated**
2. A cited comparison found OpenLB on average 32 times faster than OpenFOAM for wall-modelled LES of an IC engine (§1). **Stated**
3. With the exponential kernel, $\partial_t\bar\phi=(\phi-\bar\phi)/\Theta$, inverted exactly as $\phi=\bar\phi+\Theta\,\partial_t\bar\phi$, and $\partial_t\tau_{ij}=-\tau_{ij}/\Theta+\Theta\,\partial_t\bar u_i\,\partial_t\bar u_j$, which closes the time-filtered equations (§2.1, Eqs. 4–6, which the authors cite from Oberle et al.). **Derived**
4. In the filtered BGK equation the Hermite residual moments are zero at orders 0 and 1 and $\tau_{ij}+\eta_{\mathrm{sgs}}\delta_{ij}$ at order 2; isothermal second-order truncation sets $\eta_{\mathrm{sgs}}\equiv0$, and the paper reads $\tau_{ij}$ as the temporal residual stress instead of modelling it with an eddy viscosity (§2.2, Eqs. 8–11). **Derived**
5. The filtered lattice Boltzmann equation is expected to converge with second order in space and first in time under diffusive scaling, with $\nu=c_s^2(\tau_{\mathrm{LB}}-\Delta t/2)$ (§2.4, Eq. 15). **Stated**
6. The residual forcing in the MRT equation is unrelaxed, in contrast to Malaspinas & Sagaut, and the equilibrium moments are chosen consistent with the single-relaxation-time (SRT) derivation (§2.4). **Stated**
7. The TDDM updates (Eqs. 18–19) are local in space: a higher order costs stored time levels, not non-local communication, unlike spatial approximate deconvolution for lattice Boltzmann (§2.4, §4). **Stated**
8. Filter-width calibration ($Re=800$, $N_x=64$, $\mathrm{Ma}=0.1$): $\tilde\Theta=5$ has marginal impact, 10 and 20 bring the $\varepsilon_{\mathrm{tot}}$ peak towards the DNS, 40 drives model-dissipation oscillations to "complete overdrive"; above 10 the oscillations are "clearly unphysical", and larger widths move energy from the inertial range to $k\gtrsim30$; $\tilde\Theta=10$ is chosen (§3.2.1, Figs. 2–3). **Shown**
9. Mach calibration ($0.05$–$0.2$): initial dissipation oscillations grow with $\mathrm{Ma}$, $\mathrm{Ma}=0.05$ gives clearly negative model dissipation, and $\mathrm{Ma}=0.1$ is the lowest without an overly increased dissipation tail; running to $t=20$ is "essential" (§3.2.2, Figs. 4–5). **Shown**
10. A Mach number well below 0.3 is needed because the residual stress derives from the incompressible equations while the lattice Boltzmann method is weakly compressible (§3.2.2). **Stated**
11. The initial dissipation deviation originates in initialization errors of the lattice Boltzmann method, amplified by the model and its first-order differences; larger $\mathrm{Ma}$ and larger $\Theta$ amplify it (§3.2.3, Fig. 6). **Shown**
12. Deconvolved and filtered spectra agree except near $k\approx30$ (§3.2.3, Fig. 6). **Shown**
13. The original regularization of the spectral-element TLES (relaxing unfiltered to filtered velocity) introduces a phase lag, severe for the transient Taylor–Green vortex, avoided by Pruett's temporal approximate-deconvolution regularization (§3.3). **Stated**
14. UDNS at $Re=3000$: the lattice Boltzmann method underpredicts the $\varepsilon_{\mathrm{tot}}$ peak relative to spectral elements at $N_x=64$, less at $N_x\approx128$; spectral elements show a high-wavenumber pile-up, lattice Boltzmann an early dissipation range, starting at $k\approx20$ ($N_x=64$) and $k\approx50$ ($N_x=128$) (§3.3.1, Fig. 7). **Shown**
15. TLES at $Re=3000$: lattice Boltzmann TLES recovers a distinct $\varepsilon_{\mathrm{tot}}$ peak near $t\approx9$ at $N_x=64$, spectral-element TLES a "distorted crown"; both improve on UDNS and keep or slightly improve the spectra, attributed to injected model dissipation (§3.3.2, Fig. 8). **Shown**
16. The authors conjecture that MRT lattice Boltzmann UDNS already acts as an implicit LES: at $N_x=64$ its $\varepsilon_{\mathrm{mod}}$ is about half of $\varepsilon_{\mathrm{tot}}$ (§3.3.2, Fig. 7a). **Shown** (conjecture)
17. Under acoustic scaling ($N_x=24$–$192$) the subgrid activity of TLES and UDNS decreases on average with refinement "with increasing (up to presumably second) order", and is about equal with and without the model for $t\in(5,15)$ (§3.4, Fig. 9). **Shown**
18. The spectrum error at $t=9$ falls with order two for $N_x\le64$, then reaches a plateau for both UDNS and TLES (§3.4, Fig. 9f). **Shown**
19. The relative TLES–UDNS deviation decreases with $N_x$, as about $N_x^{-0.47}$ for subgrid activity and $N_x^{-0.83}$ for the spectrum error (§3.4, Fig. 9i). **Shown**
20. Up to about 75% of the resolved wavenumbers the spectrum error falls with resolution; the last 25% gives an asymptotically constant contribution (§3.4, Figs. 9g–h). **Shown**
21. "The present work proves" that with $\hbar=0.1$ the MRT TLES approaches the incompressible solution "up to a known combination of errors"; the support is numerical. The compressibility defect, besides the dissipative nature of the method, is concluded to be the main source of the plateau (§3.4). **Shown** (worded as a proof)
22. Under diffusive scaling the method is consistent but first order in time; acoustic scaling suggests second order until the compressibility plateau, so a first-order TDDM is reasonable under DS and a second-order one conjecturally more consistent under AS (App. B). **Stated**
23. SRT at $N_x=256$ shows only a marginal compressibility plateau, taken to show that an incompressible turbulence model is reasonable at $\mathrm{Ma}\le0.1$ (App. B, Fig. 10). **Shown**
24. MRT reduces the EOC but is stable in highly under-resolved settings ($N_x=32$); unexpectedly MRT lowers the EOC under DS relative to AS by about 0.5 (App. B, Table 3). **Shown**
25. TLES improves the EOC of the total-dissipation error over UDNS for every collision operator and scaling, more for AS and for second-order TDDM: SRT UDNS 1.70/1.80, TLESo1 1.78/1.83, TLESo2 2.11/2.07; MRT UDNS 1.52/1.09, TLESo1 1.63/1.17, TLESo2 1.81/1.20 (AS/DS) (App. B, Table 3). **Shown**
26. EOC values from turbulent cases without analytical solution are "prone to interference by statistical outliers" and are fuzzy (App. B). **Stated**

# Printed slips

- Eq. (25): $\epsilon_{res}(t)=2\pi\nu\zeta$. *(Compiler check, not in the sources: multiplying the paper's incompressible momentum equation by $\boldsymbol u$ and averaging over the periodic box, the viscous term gives $-dK/dt=\nu|\Omega|^{-1}\int|\nabla\boldsymbol u|^2dx=\nu|\Omega|^{-1}\int(\nabla\times\boldsymbol u)^2dx$ for a divergence-free periodic field; with $K$ of Eq. (22) and $\zeta$ of Eq. (23) this is $\nu\zeta$, with no factor $2\pi$.)*
- Eq. (14) relaxes with $\Delta t/(\tau+\frac{\Delta t}{2})$, while Eq. (15) gives $\nu=c_s^2(\tau-\Delta t/2)$. *(Compiler check, not in the sources: Table 1's $\tau=0.50217$ for $N=64$, $Ma=0.1$, $Re=800$ equals $0.5+3\nu_L$ with the lattice viscosity $\nu_L=\Delta t/(Re\,\Delta x^2)=0.00576/(800\times0.09973^2)=0.000724$ and $c_s^2=1/3$ (the lattice sound speed $1/\sqrt3$ printed by the sources of the [lattice Boltzmann page](/methods/lattice-boltzmann-method.md)), the form of Eq. (15); the $Ma=0.2$ row, $\Delta t=0.01154$, gives $0.50435$ against the printed $0.50434$.)*
- Table 1, $N=128$: $\Delta t=0.00288$ at $Ma=0.1$ and $0.00144$ at $Ma=0.05$. *(Compiler check, not in the sources: $u^L\Delta x$ gives $0.05776\times0.04947=0.002857$ and $0.02887\times0.04947=0.001428$, the rule the other $N=128$ rows follow and the values that reproduce the printed $\tau$; Table 2 prints 0.00285 for the same setting.)*
- App. B: "The corresponding discretization parameters are summarized in Table 1", while the Fig. 10 caption refers to Table 2.
- §3.3 and Fig. 6 caption: "$\Theta=10$" for the dimensionless $\tilde\Theta=10$ of Eq. (28).
- Typographical: "where set to", "wheres the LBM", "looses its model effectiveness", "Therefor".

# Notation map

| Simonis et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar g$, $\bar u_\alpha$, $\bar p$ | $\bar\phi$ | **the overbar is a causal time filter here, not a spatial LES filter** |
| $\Upsilon\in\{\boldsymbol u,p\}$ | $\phi$ | generic unfiltered quantity |
| $\Theta$, $\tilde\Theta$, $\hbar$ | $\Theta$, $\tilde\Theta$, $\hbar$ (page-local) | temporal filter width, its value in time steps, $\Delta t/\Theta$ |
| $T_{\alpha\beta}=\overline{u_\alpha u_\beta}-\bar u_\alpha\bar u_\beta$ | $\tau_{ij}$ | temporal residual stress; same positive-trace sign as the registry; written $T^{\mathrm t}_{ij}$ on the [lattice Boltzmann page](/methods/lattice-boltzmann-method.md), where $\tau$ is the relaxation time |
| $\eta$ (subgrid temperature) | $\eta_{\mathrm{sgs}}$ | **$\eta$ is the Kolmogorov length in the registry**; set to 0 |
| $\bar f_i$, $n_i$, $\boldsymbol\xi_i$, $w_i$ | $f_q$, $\boldsymbol c_q$, $w_q$ | filtered and shifted populations, discrete velocities, weights |
| $\tau$ (relaxation time) | $\tau_{\mathrm{LB}}$ | **not the SGS stress** |
| $s_e$, $s_P$, $s_q$, $s_\mu$, $s_\varepsilon$, $s_\Pi$ | page-local | MRT relaxation frequencies; $s_q$, $s_\mu$ Mach-dependent |
| $N$ | $N_x$ | grid points per direction (lattice) or equivalent spectral-element points, **not the polynomial degree $N$** |
| $k$, $\zeta$ | $K$, $\mathcal Z$ | **$\boldsymbol\zeta$ is the feature vector in the registry**; spectral convention for $K$ |
| $\epsilon_{tot}$, $\epsilon_{res}$, $\epsilon_{mod}$ | $\varepsilon_{\mathrm{tot}}$, $\varepsilon_{\mathrm{res}}$, $\varepsilon_{\mathrm{mod}}$ | |
| $\kappa$, $E(\kappa,t)$, $D(\kappa,t)$ | $k$, $E(k)$, $D(k)$ | **$\kappa$ is the von Kármán constant in the registry** |
| $\chi$ (SEM regularization) | $\chi_f$ | 4.0 at $N_x=64$, 2.0 at $N_x=127$ |
| $Ma$ | $\mathrm{Ma}$ (lattice Mach number) | $M$ in the registry is the flow Mach number |
| $Re$ | $Re$ | $U_cl_c/\nu$ with $l_c=1$ m, $U_c=1$ m/s |

# Reference list

47 printed references, numbered style [1]–[47]. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. [9] (Hou et al. 1994) is an arXiv preprint and kept as one; [25]
is an OpenLB release on Zenodo and [26] a Nek5000 web page with no title;
[15] prints no page or article number. No printed duplicates and no
unparseable items.

# Pages created or updated

Chunk 10 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [WALE model](/methods/wale-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Nek5000 and NekRS](/software/nek5000.md)
