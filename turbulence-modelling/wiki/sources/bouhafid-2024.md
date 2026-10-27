---
type: Source
title: "Bouhafid et al. (2024) — Combined Reynolds-averaged Navier-Stokes/Large-Eddy Simulations for an aircraft wake until dissipation regime"
description: "Simulates an airliner wake from the jet to the dissipation regime by extruding a slice of an adapted-mesh RANS solution into a periodic temporal LES, seeded with synthetic turbulence scaled to the RANS Reynolds stresses, and studies vortex lifespan, stratification and plume dilution."
resource: "doi:10.1016/j.ast.2024.109512"
source_kind: paper
authors: [Bouhafid Y., Bonne N., Jacquin L.]
year: 2024
venue: "Aerosp. Sci. Technol. 154:109512"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Aerospace_Science_and_Technology_Bouhafid_Combined_Reynolds-averaged_Navier-StokesLarge-Eddy_Simulatio.pdf"
tags: [hybrid-rans-les, les, rans, mesh-adaptation, anisotropy, compressible]
timestamp: 2026-10-26T10:05:00Z
---

# Summary

Bouhafid et al. (2024) study the wake of an airliner, a subject peripheral
to this bundle, through a sequential coupling that belongs to it: a
one-way, in-time form of [hybrid RANS/LES](/definitions/hybrid-rans-les.md).
Stage 1 is a steady compressible RANS computation of the full aircraft with
metric-based anisotropic [mesh adaptation](/methods/mesh-adaptation.md)
(Feflo.a, twelve iterations to about 110 M cells), closed by the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md) for a NACA-0012
wing with a jet and by the ATAAC differential
[Reynolds-stress model](/methods/reynolds-stress-model.md) for the NASA
Common Research Model with engines; the authors justify the latter because
the Reynolds stress and the mean strain are misaligned in wing-tip vortices,
where the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)
fails. Stage 2 extracts a cross-flow slice, extrudes it over one Crow
wavelength into a periodic box in the ground frame, and runs a temporal
[LES](/definitions/large-eddy-simulation.md) with the
[Smagorinsky model](/methods/smagorinsky-model.md).

The RANS turbulence reaches the LES as an initial condition built with the
MDSRFG Fourier-mode generator of [inflow turbulence generation](/methods/inflow-turbulence-generation.md),
rescaled cell by cell to the local RANS Reynolds stress; the same generator,
unscaled, supplies anisotropic atmospheric turbulence on $-5/3$ spectra.
On the NACA-0012 case the synthetic fluctuations are needed to reproduce
the jet roll-up and the measured total temperatures, and the 22.5 M-cell
temporal LES resembles an 89 M-cell zonal DES. On the CRM, mesh adaptation
recovers the elliptic-loading circulation; eight temporal LES of 160 M
cells vary atmospheric turbulence, wake turbulence and stratification: the
normalized vortex lifespan lies between 4 and 5 when atmospheric turbulence
is present, stratification shortens it, and the RANS initialization gives a
more turbulent secondary wake and a plume about three times less diluted
than an analytic Lamb–Oseen initialization with uncorrelated noise.

# Version read

Version of record (Elsevier), 23 pages, all read; equation pages checked
visually because the text layer garbles them. Page 1 matches the Crossref
record. Equation, section, figure and table numbers on this page are those
of the version of record.

# Key claims

Page-local symbols: $b$, $b_0=\tfrac\pi4b$ the wingspan and initial vortex
spacing; $\Gamma$, $r_c$ the vortex circulation and core radius;
$t_b=2\pi b_0^2/\Gamma$ the descent time; $\tau_{\mathrm{life}}$ the vortex
lifespan normalized by $t_b$; $\varepsilon_{\mathrm{atm}}$,
$\varepsilon_{\mathrm{wake}}$ the atmospheric and wake dissipation rates;
$\eta_{\mathrm{atm}}=2\pi b_0(\varepsilon_{\mathrm{atm}}b_0)^{1/3}/\Gamma$
the normalized atmospheric dissipation; $N_{\mathrm{BV}}$ the
Brunt–Väisälä frequency; $\lambda_{\mathrm{Crow}}=8.6b_0$; $R_j$ the jet
radius; $R^{\mathrm{t}}_{ij}$ the target Reynolds stress of the synthetic
field.

1. The methodology bridges the jet regime with the vortex and dissipation regimes with one solver, no precursor simulation for atmospheric turbulence and no source terms in the Navier–Stokes equations (which "often require calibration" [38, 32]) (§1, §2.1). **Stated**
2. The LES domain is the extrusion over $\approx8.6b_0$ (one Crow wavelength) of a RANS cross-flow slice, interpolated nearest-neighbour onto a new mesh, fixed in the ground frame, periodic in the flight direction with far-field conditions elsewhere (§2.1, Fig. 1). **Stated**
3. The MDSRFG series (Eq. 2.1) is divergence-free, correlated in space and time, and imposes arbitrary one-dimensional spectra (§2.1, cited [7]). **Stated**
4. A scaling step (Eqs. 2.2–2.4) followed by Smirnov's RFG transformation makes the series reproduce a prescribed Reynolds stress $R^{\mathrm{t}}_{ij}$; the rescaled field is in general not divergence-free, acceptable because it is only an initial condition, not an inlet condition (§2.1). **Derived** / **Stated**
5. On the test of Huang et al. (von Kármán spectrum) the generated spectrum before scaling agrees very well with the target; the linear scaling changes the levels but not the shape or the length scales (§2.1, Fig. 2). **Shown**
6. Differential Reynolds-stress models, which do not use the Boussinesq hypothesis, are "more accurate than two-equations models" for wing-tip vortex flows because the Reynolds stress and the mean strain are misaligned there [11], owing to rotation [21] (§2.2). **Stated**
7. NACA-0012 with jet: without synthetic turbulence the jet roll-up is not captured; with MDSRFG the LES agrees qualitatively with the experiment and much better in temperature; the roll-up at $x/b=5$ and 8 is slightly overestimated, attributed to the initial plume size and a pylon absent from the RANS geometry (§3.2, Figs. 4–6). **Shown**
8. The temporal LES (22.5 M cells) gives a result very similar to a ZDES of 89 M cells [8] in vortex centre and temperature levels, the ZDES reproducing the roll-up size more accurately, at a significantly lower cost (§3.2, Fig. 6d). **Shown** (no timings printed)
9. The CRM RANS jet radius follows $R_j\sim x^{0.52}$, against $R_j\sim x$ for a free round jet; the integral model of Jacquin & Garnier gives $R_j\sim x^{0.48}$, in good agreement; interpreted as "laminarization of the jet surroundings by the wing-tip vortex" (§4.2.1, Fig. 9). **Shown**
10. Around $x/b=13$ the jet radius departs from the $x^{0.52}$ law; jet–vortex interaction becomes important at $x/b\approx14$, where the interaction number is $\lesssim10$ (§4.2.1, Fig. 10). **Shown**
11. The initial coarse mesh underpredicts the circulation through numerical diffusion; adaptation iterations 6, 9, 12 approach the elliptic-loading value $\Gamma=528$ m$^2$/s; the core radius grows linearly with $x$ and is mesh-converged over the last three iterations (§4.2.2, Fig. 12). **Shown**
12. LES resolution: 100 points per Crow wavelength in $x$ (against 64, 100, about 488 and 350 in earlier works); $h/r_c=0.1$ in the descent zone, "almost twice the resolution in the vortex core" of [17] and [31]; only 9 points per shortest short-wave wavelength, judged not critical (§4.1). **Stated**
13. The decay of atmospheric turbulence needs no forcing because its time scale $(\lambda_{\mathrm{Crow}}^2/\varepsilon_{\mathrm{atm}})^{1/3}\approx9$ min for the strongest case exceeds the few-minute dissipation regime (§4.1.1). **Derived**
14. Wake turbulence from MDSRFG triggers a short-wave instability of the horizontal-tail vortices at $t/t_b=1.18$ (consistent with the optimal-perturbation analysis of Fabre et al. [14]); these vortices are destroyed at $t/t_b=3.5$, after which the main vortices show the instability (§4.3.1, Figs. 13–16). **Shown**
15. With $\varepsilon_{\mathrm{atm}}>0$ (Cases 1–3) the pair is destroyed by the Crow instability and a vortex ring forms ($t/t_b=5.84$–7); with $\varepsilon_{\mathrm{atm}}=0$ (Case 4) a shorter-wavelength instability destroys it with two rings at $t/t_b=7$, attributed to stratification (§4.3.1). **Shown**
16. $\tau_{\mathrm{life}}$ lies between 4 and 5 and decreases with $\eta_{\mathrm{atm}}$; it agrees with the Crow–Bate [12] and Sarpkaya [43] models and data for weak and medium turbulence, and departs from the models for strong turbulence while staying within the scattered experimental range (§4.3.1, Fig. 18b). **Shown**
17. "Atmospheric turbulence intensity does not seem to significantly impact the vortex pair lifespan", and atmospheric turbulence is not required to destroy the pair; the position and size of the vortex ring depend on it (§4.3.1). **Shown**
18. Stratification ($N_{\mathrm{BV}}=0.012$ rad/s) generates baroclinic vorticity forming a secondary wake rising to flight altitude and accelerates destruction: $\tau_{\mathrm{life}}\approx4.6$ with, $\approx6.0$ without stratification (§4.3.2, Figs. 17–19). **Shown**
19. The vortex-tube diameter grows at the same rate with and without stratification; "it is unclear if this growth is due to numerical diffusion or atmospheric turbulence" (§4.3.2). **Stated**
20. Without synthetic turbulence (Cases 6–7) only short-wave instabilities grow, late, without stratification; with stratification a medium-wave symmetric instability destroys the pair by $t/t_b=6.61$, explained by the shrinking vortex spacing and the turbulent secondary wake (§4.3.2, Fig. 20). **Shown** / **Derived**
21. The analytic initialization (Lamb–Oseen pair, uniform jets, uncorrelated Gaussian perturbations of standard deviation about 1.3 m/s) gives a similar primary-wake descent and lifespan but no short-wave instability at $t/t_b=3.89$, because per-cell uncorrelated noise does not excite short-wave modes (§4.3.3, Figs. 18, 21, 22). **Shown**
22. The RANS-initialized secondary wake is much more turbulent than the analytic one, attributed to vortex stretching by wavy vortex tubes interacting with baroclinic vorticity (§4.3.3). **Shown** / **Stated**
23. Plume dilution: initial areas 793 m$^2$ (RANS) and 239 m$^2$ (analytic); at the end of the dissipation phase the analytic plume is about three times more diluted, and the areas become similar (§4.3.3, Fig. 23). **Shown**
24. Plume temperature differences up to 0.3 K give, with the Murphy–Koop ice-saturation formula (Eq. 4.4) at $T=224$ K, a 4% difference in relative humidity (§4.3.3). **Derived**
25. Starting from the slice $x/b=15$ ($\varepsilon_{\mathrm{wake}}=80$ m$^2$s$^{-3}$) instead of $x/b=18$ changes the averaged aerodynamics and the plume very little; linking occurs at three locations instead of two (§4.3.4, Figs. 27–31). **Shown**
26. The vortex descent speed agrees very well with $\Gamma/(2\pi b_0)$ (§4.3.4, Fig. 27a). **Shown**
27. Mesh adaptation: twelve iterations on the sensor $\tfrac12U^2+k$ with the $L^2$ norm (more wake resolution than $L^4$ [2, 5]); final mesh about 110 M cells including 40 M prisms; wall functions at $y^+\approx80$ (App. A, Fig. 32). **Stated** / **Shown**

The equations in registry notation: Favre-averaged RANS with the
density-weighted Reynolds stress $\langle\rho u_i''u_j''\rangle$ (positive
convention) and a gradient turbulent heat flux with $Pr_t=0.9$ (Eq. 2.5);
Favre-filtered LES with $\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$,
positive trace, full tensor, and an SGS heat flux, both closed by the
Smagorinsky model whose constant, filter width and SGS Prandtl number are
not printed (Eq. 2.6). The wake dissipation is printed as "$\epsilon=k\omega$"
(§4.1), without the factor $\beta^*$ of the registry's
$\omega=\varepsilon/(\beta^*k)$ *(compiler check, not in the sources)*. The
ATAAC model is described only as six stress equations with pressure–strain
modelling "based on Wilcox's work", an $\omega$ equation and a near-wall
damping equation; no coefficients are printed.

# Printed slips

- **Abstract against §4.3.1:** the abstract states that "atmospheric turbulence intensity and stratification both accelerate the vortex decay", while §4.3.1 states that "atmospheric turbulence intensity does not seem to significantly impact the vortex pair lifespan".
- **Eq. (4.3):** "$\frac{dp_{LO}}{dr}=\rho\frac{V_{\theta,LO}}{r}$", dimensionally inconsistent; cyclostrophic balance needs $V_{\theta,LO}^2$ *(compiler check, not in the sources)*.
- **§4.1.1:** "$g=9.81$ m$^2$/s".
- **$t_b$:** printed $t_b=2\pi b_0^2/\Gamma=25.7$ s; with the printed $b=58.8$ m, $b_0=\tfrac\pi4b$ and $\Gamma=528$ m$^2$/s the formula gives 25.4 s *(compiler check, not in the sources)*.
- **§2.2:** "the MDSRFG synthetic turbulence methods described in Sec. 3", described in Sec. 2.1.
- **Introduction against §4.2.1:** the vortex regime is said to begin when the interaction number is "$\ll1$", while §4.2.1 calls interaction important "close to unity … for $x/b\approx14$ where $R_3\lesssim10$".
- **Name spellings:** "Kolemenskiy", "Churfield", "Sarpakaya", "Chmielaski" against Kolomenskiy, Churchfield, Sarpkaya, Chmielarski in the reference list.
- **Interaction number:** the formula prints $\rho_0$ while the text defines "$\rho_\infty$ is the ambient density".
- **Garbles:** "when atmospheric the atmosphere is stratified" (§4.3.2); "used defined senor" (App. A); Fig. 9b legend "Turbulent Flcws"; "the isosurface $U_x>\tfrac12U_j$" for a region (§2.1).
- **Undefined:** $k_0$ in $\tilde{\boldsymbol k}=\boldsymbol k/k_0$ (Eq. 2.1).
- **Ref. [14]:** Fabre, Jacquin & Loof (J. Fluid Mech. 451, 2002) printed with the AIAA 2023 DOI 10.2514/6.2023-3889. **Ref. [40]:** Pope's *Turbulent Flows* printed as "Meas. Sci. Technol. 12 (2001) 2020–2021". **Ref. [51]:** pages "14–015".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\Phi$ (Eq. 2.5) | $\langle\Phi\rangle$ | **collision:** overbar is the Reynolds average in the RANS equations |
| $\bar\Phi$ (Eq. 2.6) | $\bar\Phi$ | LES filter; agrees |
| $\tilde\Phi=\overline{\rho\Phi}/\bar\rho$ | $\langle\Phi\rangle_\rho$ (RANS), $\tilde\Phi$ (LES) | Favre average or filter |
| $\overline{\rho u_i''u_j''}$ | $\langle\rho u_i''u_j''\rangle$ | positive convention |
| $\tau_{ij}$ | $\sigma_{ij}$ | **collision:** viscous stress |
| $\tau^{sgs}_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ | $\tau_{ij}$ (compressible form) | agrees, positive trace |
| $\breve\tau_{ij}$ | $R^{\mathrm t}_{ij}$ (page-local) | target Reynolds stress; $\tfrac23k\delta_{ij}$ in the isotropic case |
| $e_0$ | $E/\rho$ | |
| $k$ | $k$ | also a wavenumber in the spectra (registry clash list) |
| $\omega$, $\boldsymbol\omega$, $\omega_{m,n}$ | $\omega$, $\omega_i$, (random frequency) | three meanings |
| $\epsilon$, $\epsilon_{wake}$, $\epsilon_{atm}$ | $\varepsilon$, $\varepsilon_{\mathrm{wake}}$, $\varepsilon_{\mathrm{atm}}$ | |
| $\eta=2\pi b_0(\epsilon_{atm}b_0)^{1/3}/\Gamma$ | $\eta_{\mathrm{atm}}$ (page-local) | **collision:** not the Kolmogorov length |
| $\tau$ | $\tau_{\mathrm{life}}$ (page-local) | **collision:** lifespan, not a stress |
| $N_b$ | $N_{\mathrm{BV}}$ (page-local) | **collision:** not the polynomial degree |
| $M$, $N$, $c_i$, $\theta_1$, $\tau_0$, $L_s$ | (MDSRFG parameters) | **collision:** $N$ is not the polynomial degree |
| $\lambda_{ij}$ | (scaling tensor) | **collision:** not the Taylor microscale |
| $\beta\approx1.256$ (Eq. 4.3) | (Lamb–Oseen constant) | **collision:** not the field-inversion $\beta$ |
| $\varepsilon=0.05$ (plume threshold) | (threshold fraction) | **collision:** not the dissipation rate |
| $\Delta$ | $h$ | LES grid spacing, not a filter-width definition |
| $C_k=1.5$, $r=u'_h/u'_v$ | (Kolmogorov constant, anisotropy factor) | atmospheric spectra |
| $b$, $b_0$, $\Gamma$, $r_c$, $d_c$, $t_b$ | same (page-local) | wake-vortex quantities |
| $R_j$, $R_3$, $J$, $D_j$ | (jet radius, interaction number, excess momentum, diameter) | |
| $\Theta$, $g$ | (potential temperature, gravity) | |
| $\mathcal M$, $\mathcal C$, $H$ | (metric, complexity, Hessian) | App. A |

# Reference list

54 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Two pairs of
same-author same-year works (Loseille 2011, refs. [27], [28]; Unterstrasser
2014, refs. [50], [51]) take suffixes in printed order. Ref. [14] carries a
mismatched DOI and ref. [40] a book-review record for Pope's book (both kept
as printed, with notes); ref. [39] is a discussion paper; refs. [3], [37],
[44] lack page or article numbers. No printed duplicates; all items parsed.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 7. This source is cited on:

- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
