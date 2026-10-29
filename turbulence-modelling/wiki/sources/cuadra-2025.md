---
type: Source
title: "Cuadra et al. (2025) — Review of shock-turbulence interaction with a focus on hypersonic flow"
description: "Reviews the canonical interaction of isotropic turbulence with a normal shock, from linear interaction analysis to DNS and LES, and adds linear-interaction results for air in thermochemical equilibrium up to Mach 40–60, with entropic and acoustic upstream content, flight-altitude effects and a compilation of DNS data against the theory."
resource: "doi:10.1063/5.0255816"
source_kind: paper
authors: [Cuadra A., Di Renzo M., Hoste J.J.O.E., Williams C.T., Vera M., Huete C.]
year: 2025
venue: "Phys. Fluids 37:045129"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Cuadra_Review_of_shock-turbulence_interaction_with_a_focus_on_hyper.pdf"
tags: [compressible, hypersonic, dns, les, shock-capturing, review]
timestamp: 2026-10-29T05:11:00Z
---

# Summary

Cuadra et al. (2025) review the canonical shock–turbulence interaction:
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
convected through a normal shock, the isolated configuration behind
[shock-generated turbulence](/results/shock-generated-turbulence.md) in
supersonic and hypersonic flight and a building block of
[shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).
The first strand is [linear interaction analysis](/methods/linear-interaction-analysis.md)
(LIA, Ribner, Moore, Chang): weak upstream turbulence is decomposed into
Kovasznay vortical, entropic and acoustic modes, the Rankine–Hugoniot
conditions are linearized about the mean shock, and the post-shock
amplitudes are integrated over an isotropic distribution of wave
orientations to give the amplification factor of the turbulent kinetic
energy, $\mathrm{AF}_k$. The authors' framework extends this to air in
thermochemical equilibrium with the Combustion Toolbox (26 species) and
three Rankine–Hugoniot slope parameters. New results give $\mathrm{AF}_k(M_1)$
up to $M_1\approx40$–60 for vortical, vortical–entropic and
vortical–acoustic upstream turbulence, the amplification of turbulent
intensity and turbulent Reynolds number, and flight-altitude effects, with
the thermochemical relaxation length from 1-D HTR computations. Upstream
density disturbances come to dominate the shock response as $M_1$ grows,
and a small upstream compressibility changes $\mathrm{AF}_k$ more than
endothermic effects do.

The second strand reviews numerical work. Shock-resolving DNS is limited
to $M_1\lesssim1.5$; shock capturing uses [WENO/TENO](/methods/weno-scheme.md)
hybridized with central, [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
or [compact](/methods/compact-finite-difference-scheme.md) schemes through
a [shock sensor](/definitions/shock-sensor.md), or
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
(including artificial [bulk viscosity](/definitions/bulk-viscosity.md)),
with an overall [numerical dissipation](/properties/numerical-dissipation.md)
that depends on the sensor; shock fitting is a third class.
[DNS](/definitions/direct-numerical-simulation.md) covers wrinkled,
broken and vanished shock regimes and the LIA–DNS reconciliation through
the ratio of shock thickness to Kolmogorov length;
[LES](/definitions/large-eddy-simulation.md) results favour the
[dynamic](/methods/dynamic-procedure.md) over the static
[Smagorinsky model](/methods/smagorinsky-model.md) and switching the
subgrid fluxes off where shock capturing is active. A compilation of DNS
conditions ($M_1\in[1.1,6]$, $M_t\in[0.02,0.691]$, $Re_\lambda\in[9,74]$)
is compared with LIA. The hypersonic regime ($M_1\ge5$) is nearly
unexplored by DNS and LES; new subgrid models for high-enthalpy flows and
new DNS databases, also for [a priori testing](/definitions/a-priori-and-a-posteriori-testing.md),
are called for. GPU finite-difference codes such as
[STREAmS](/software/streams.md) appear among the cited frameworks.

# Version read

Version of record (AIP, Special Topic "Measurement, Modelling and
Prediction of Hypersonic Turbulence"; with the AIP cover page and a
download stamp of 26 October 2026; submitted 31 December 2024, accepted
17 February 2025, online 4 April 2025), 26 PDF pages (cover plus
045129-1 to 045129-25), all read; every equation, table and caption of
pp. 2–22 read on the page image. Page 1 matches the metadata (six
authors, corresponding author Huete); no identity issue. Printed as a
research article, the paper is a review with new LIA results. Equation,
figure, table and section numbers are those of this version.

# Key claims

Page-local symbols: $M_1$, $M_2$ the pre- and post-shock Mach numbers;
$\mathcal R=\rho_2/\rho_1$, $\mathcal P=P_2/P_1$, $\mathcal T=T_2/T_1$ the
jump ratios; $\Gamma_{\mathrm H}$, $\Gamma_\rho$, $\Gamma_p$ the normalized
Rankine–Hugoniot slope parameters; $\beta_c=c_2/c_1$ the sound-speed
ratio; $\mathrm{AF}_k$ the amplification of the turbulent kinetic energy
across the shock and $\mathrm{AF}_{11}$, $\mathrm{AF}_{22}$ those of the
streamwise and transverse Reynolds stresses (registry §11 $\mathrm{AF}_q$;
$x_1$ normal and $x_2$ tangential to the shock); $\theta_k$ the angle of the wavevector to the shock normal; $\epsilon_{\mathrm w}$ the amplitude of one upstream wave; $\chi_{\mathrm e}$
the entropic–vortical correlation; $\eta_{\mathrm a}$ the upstream
dilatational-to-solenoidal kinetic-energy ratio; $\mathcal K_{\mathrm D}$,
$\mathcal K_{\mathrm{br}}$ the two similarity parameters of the source
(both printed $\mathcal K$); $\delta_{\mathrm{sh}}$ the laminar shock
thickness; $\ell$, $\ell_T$ the upstream integral length and the
thermochemical non-equilibrium thickness; $\mathcal I$ the turbulent
intensity and $Re_\ell$ the turbulent Reynolds number at $\ell$.

1. In the canonical interaction with solenoidal upstream turbulence only, the incoming turbulence is characterized by $M_t$ (Eq. 1) and $Re_\lambda$ (Eq. 2), plus the spectrum shape; anisotropy is not considered (§I). **Stated**
2. For isotropic turbulence, LIA finds that $\mathrm{AF}_k$ depends neither on the spectrum shape $E(k)$ nor on $Re_\lambda$ or $M_t$; the only independent parameters are $M_1$ and the gas compressibility through $\gamma$ (§I, p. 4). **Stated**
3. Rapid distortion theory has been applied to the interaction (refs. 43–45), with assumptions even more restrictive than those of LIA (§I). **Stated**
4. For LIA to hold, variations of the upstream Mach number must be small compared with its mean, and the residence time across the shock and the non-equilibrium region must be small compared with the turbulence time scale; the LIA cutoff removes the smallest eddies (§I, p. 4). **Stated**
5. For a calorically perfect ideal gas in thermochemical equilibrium, the normalized inverse Hugoniot slope reduces to $\Gamma_{\mathrm H}=M_1^{-2}$ (after Eq. 18), and $\Gamma_\rho=-\mathcal R^{-1}$, $\Gamma_p=\mathcal PM_1^{-2}$ (after Eq. 29). **Derived**
6. Thermochemical equilibrium (26 species) gives a significantly higher compression ratio than frozen gas; with ionization neglected the maximum compression ratio $d+1$ falls from 6 to 4 ($d=5$ rigid diatomic, $d=3$ atoms); ionization becomes significant for $M_1\ge30$; results agree with NASA CEA "always" excellently (§II B 2, Fig. 3). **Shown**
7. As $M_1\to\infty$ only density disturbances (acoustic or entropic) can substantially affect the shock, because $1/\beta_c$ decreases inversely with $M_1$ while the density jump stays finite (§II B 2, Eq. 28). **Derived**
8. Upstream density disturbances are non-negligible when $\delta\rho_1/\rho_1\sim(c_1/c_2)[2/(M_2\mathcal R(1+\Gamma_\rho))]\,\delta u_1/c_1$ (Eq. 30); for $\gamma=1.4$ and $M_1=5$, $\delta\rho_1/\rho_1$ matters when about one order of magnitude smaller than $\delta u_1/c_1$, a threshold that decreases with shock strength (§II B 2, Fig. 4b). **Derived**
9. Density disturbances ahead of the shock can also come from numerical turbulence forcing (Petersen & Livescu 2010), so any treatment of the interaction should account for them (§II B 2). **Stated**
10. For purely vortical upstream turbulence in air ($T_1=300$ K, $P_1=1$ atm), $\mathrm{AF}_k(M_1)$ is non-monotonic with two peaks in the O$_2$ and N$_2$ dissociation regions; the acoustic kinetic energy is negligible in hypersonic conditions; $\mathrm{AF}_k$ is governed by the endothermic increase of the compression ratio (more flow deflection, more transverse kinetic energy) and by the Rankine–Hugoniot slope (§II B 3a, Fig. 5). **Shown** (LIA computation)
11. The turbulent-intensity ratio $\mathcal I_2/\mathcal I_1=\mathrm{AF}_k^{1/2}\mathcal R$ (Eq. 32) is 1.5 times its thermochemically frozen value at $M_1=10$ and, at its maximum near $M_1\simeq26$, twice the frozen value ($\mathcal I_2/\mathcal I_1\simeq8$), at the Hugoniot turning point ($\Gamma_{\mathrm H}=0$, $\mathcal T\simeq42$, $\mathcal R\simeq12$) (§II B 3a, Fig. 6a). **Shown**
12. Small entropic fluctuations ($\chi_{\mathrm e}\sim10^{-2}$) can significantly alter the downstream turbulence; at $M_1=10$ and $\chi_{\mathrm e}=-0.5M_1^{-1}=-0.05$, $\mathrm{AF}_k$ rises by 29% over the solenoidal case, while endothermic effects add only 8.6% over the calorically perfect approximation (§II B 3b, Fig. 7). **Shown**
13. Upstream acoustic disturbances can raise or lower the downstream kinetic energy; the acoustic amplification crosses unity at $M_1=1.11$ and 2.35 (Huete et al. 2012), where $\mathrm{AF}_k$ is independent of $\eta_{\mathrm a}$; in the hypersonic regime acoustic content raises $\mathrm{AF}_k$, its asymptotic contribution growing as $M_1^2$ (§II B 3c, Fig. 8). **Shown** / **Stated**
14. Compressible upstream fluctuations cannot be neglected a priori in the hypersonic regime even below 10% compressibility; thermochemical effects have only a secondary effect on $\mathrm{AF}_k$ for vortical and vortical–entropic cases (§II B 3c). **Shown**
15. A cruise hypersonic aircraft must fly between 15 and 30 km at Mach 5 and 30–45 km at Mach 15 (Smart 2007) (§II C). **Stated**
16. At $M_1=10$ the relaxation length $\ell_T$ grows from about $10^{-4}$ m to $10^{-2}$ m between 0 and 30 km altitude (1-D HTR, 1200 points, CFL about 0.1), so the LIA condition $\ell\gg\ell_T$ becomes less likely at altitude; endothermic effects raise $\mathrm{AF}_k$ over the whole Mach range, the more so the higher the altitude (§II C, Fig. 9). **Shown**
17. The Moin & Mahesh scaling $\eta/\delta_{\mathrm{sh}}=0.13\sqrt{Re_\lambda}(M_1-1)/M_t$ (Eq. 38) makes shock-resolving DNS unfeasible once $M_1$ exceeds 1.5 (§III A 1). **Stated**
18. Numerical frameworks fall into shock-resolving, shock-capturing (nonlinear ENO/WENO/TENO, hybrids with central or energy-preserving schemes through a sensor, or artificial viscosity) and shock-fitting classes; the overall dissipation depends strongly on the shock sensor (§III A 1). **Stated**
19. LIA and DNS agree that for $M_1<1.65$ the post-shock Kolmogorov scale increases while higher Mach numbers reduce it; post-shock refinement is needed (§III A 2, refs. 46, 84). **Stated**
20. The highest pre-shock Mach numbers of DNS are near $M_1\sim5$, only at moderate $Re_\lambda\sim40$; LIA misses the post-shock anisotropy, which comes from further growth of the streamwise Reynolds stress by pressure transport (§III A 2). **Stated**
21. Negatively correlated upstream velocity and temperature (entropic) fluctuations increase the amplification, positively correlated ones decrease it, through baroclinic torque (Mahesh et al. 1997); upstream dilatational energy also increases it at high Mach numbers (Grube & Martín 2023; Cuadra et al. 2024) (§III A 2). **Stated**
22. Shock regimes are wrinkled, broken (Larsson) and vanished (Chen & Donzis 2019); the wrinkled-to-broken transition is described by $\mathcal K_{\mathrm{br}}=M_t/(M_1-1)$, broken for $\mathcal K_{\mathrm{br}}>0.6$; the vanished state correlates with $\delta_{\mathrm{sh}}/\eta\sim7.69$; both $\delta_{\mathrm{sh}}/\eta$ and $\mathcal K_{\mathrm{br}}$ decrease with $M_1$, making broken and vanished shocks unlikely in hypersonic flows and favouring LIA–DNS agreement (§III A 2). **Stated**
23. LES of the interaction depends sensitively on the subgrid stress closure; Garnier et al. (2002) found dynamic Smagorinsky better than coarsened DNS (under-dissipative) and static Smagorinsky (over-dissipative) in well-resolved runs; at coarse resolution, when the shock corrugations become subgrid, LES deteriorates because the shock is under-resolved, not because the SGS model fails (§III A 3). **Stated**
24. Switching the SGS fluxes off in cells where shock capturing is active improves LES (Bermejo-Moreno et al. 2010); Braun et al. (2019) used AMR and a hybrid stretched-vortex model to obtain Reynolds-stress profiles largely independent of the post-shock resolution at high $Re_\lambda$ (§III A 3). **Stated**
25. LES of the interaction has been developed almost entirely for supersonic flows; at higher Mach the isotropic subgrid part $\tau_{kk}$ becomes important, and filtered vibrational-energy and species equations add subgrid closures studied only in refs. 126–127 (§III A 3). **Stated**
26. DNS of the interaction requires $Re_\lambda>100$ for fully developed turbulence (refs. 112, 131), far above the compiled range (§III B, p. 18). **Stated**
27. For $\eta_{\mathrm a}=0$, $\mathrm{AF}_{11}$ dominates up to $M_1\sim2$, then falls below $\mathrm{AF}_{22}$, which peaks near $M_1\sim10$ about 15% above the frozen value; at $M_1=5$, LIA gives about 42% ($\mathrm{AF}_{11}$) and 16% ($\mathrm{AF}_{22}$) more amplification for $\eta_{\mathrm a}=0.05$, and about 80% and 31% for $\eta_{\mathrm a}=0.1$, relative to the solenoidal $\gamma=1.4$ case; with $\eta_{\mathrm a}=0.1$ endothermic effects lower $\mathrm{AF}_{11}$ by 7% and raise $\mathrm{AF}_{22}$ by 5%; the acoustic part of the amplification is about 3% at Mach 2 and 5% at Mach 5 for $\eta_{\mathrm a}=0.1$ (§III B, Figs. 11–12). **Shown**
28. LIA predicts $\mathrm{AF}_{22}>\mathrm{AF}_{11}$, opposite to DNS; with endothermic effects LIA predicts a decrease of $\mathrm{AF}_{11}$ and an increase of $\mathrm{AF}_{22}$ whereas DNS shows both amplified; the authors' explanation is LIA's idealized conservation of tangential velocity across a thin non-equilibrium zone; the DNS $\mathrm{AF}_{11}$ exceeds LIA for $M_1\gtrsim2.5$ (§III B). **Stated** (with **Shown** comparison)
29. The total amplification $\mathrm{AF}_k=(\mathrm{AF}_{11}+2\mathrm{AF}_{22})/3$ from DNS is much closer to LIA than the components, and DNS approaches LIA for $M_t\ll1$ and $Re_\lambda\to\infty$ (§III B, Fig. 12). **Shown**
30. The ratio of Kolmogorov lengths across the shock scales as $\eta_2/\eta_1\sim\mathcal P\mathcal T^{11/8}$ (Eq. 40, from ref. 46); the worst DNS cost is at the hypersonic border near Mach 5; small $M_t/M_1$ requires many flow-through times per eddy turnover; the cost of a shock-capturing scheme scales with the number of unknowns to the power two or three (§IV A 2). **Stated**

The theory in registry notation. $M_t=\sqrt{R_{kk}}/\tilde c=\sqrt{2k}/\tilde c$
(Eq. 1) with the Favre Reynolds stress
$R_{ij}=\langle\rho u_i''u_j''\rangle/\langle\rho\rangle$ (Eq. 4) and
$\tilde c$ the Favre-averaged sound speed; $Re_\lambda$ uses the
one-component $u_{\mathrm{rms}}$. The linearized jump conditions with
upstream vortical, entropic and acoustic content (Eq. 28) involve
$\Gamma_{\mathrm H}=u_2^2\,\partial\rho_2/\partial P_2|_{P_1,\rho_1}$,
$\Gamma_\rho=(\Gamma_{\mathrm H}/u_1^2)\,\partial P_2/\partial\rho_1|_{P_1,\rho_2}$,
$\Gamma_p=\Gamma_{\mathrm H}\,\partial P_2/\partial P_1|_{\rho_1,\rho_2}$ (Eq. 29). For
isotropic vortical turbulence (Eqs. 22–25)
$$\mathrm{AF}_k=\frac12\Big[\int_0^{\pi/2}(\hat u^2+\hat v^2)\sin^3\theta_k\,d\theta_k+1\Big]=K_a+K_r,$$
the acoustic part integrating over frequencies $\zeta\ge1$ only (the
acoustic mode decays for $\zeta<1$); with acoustic upstream content
$\mathrm{AF}_k=(\mathrm{AF}^{\mathrm r}_k+\eta_{\mathrm a}\mathrm{AF}^{\mathrm a}_k)/(1+\eta_{\mathrm a})$ (Eq. 37).
The turbulent Reynolds number ratio is
$Re_{\ell,2}/Re_{\ell,1}=\mathrm{AF}_k^{1/2}\mathcal T^{-0.7}\sqrt{(2\mathcal R^2+1)/3}$
(Eq. 33). The Donzis parameter is
$\mathcal K_{\mathrm D}=M_t/[Re_\lambda^{1/2}(M_1-1)]$ (p. 7); the authors
argue that $\gamma(T)$ prevents reducing the hypersonic problem to it. A
vibrational Damköhler number $\mathrm{Da}=\delta_\nu/(u_2t_{\mathrm{vib}})$
separates frozen, coupled and equilibrium post-shock relaxation. The LES
momentum equation (Eq. 39) prints the subgrid stress as
$\bar\rho(\tilde u_i\tilde u_j-\widetilde{u_iu_j})=-\tau_{ij}$ on the
right-hand side, with a subgrid viscous stress
$\bar\sigma_{ij}-\sigma_{ij}(\tilde u)$ usually neglected and an
eddy-viscosity closure of the deviatoric part on the Favre strain. *(Compiler
check, not in the sources: the vanished-regime value
$\delta_{\mathrm{sh}}/\eta\sim7.69$ equals $1/0.13$, the inverse prefactor
of Eq. 38.)*

# Printed slips

- **Eq. (17):** the density ratio is printed $\mathcal R=[(\gamma+1)\mathcal M_1^2+\gamma-1]/[(\gamma-1)\mathcal M_1^2+2]$ (p. 6, checked on the page image). *(Compiler check, not in the sources: at $M_1=1$ this gives $\mathcal R=2\gamma/(\gamma+1)\ne1$ while the printed $\mathcal P(1)=1$; with the numerator $(\gamma+1)M_1^2$ and the printed $\mathcal P$, Eq. 18 gives exactly the $\Gamma_{\mathrm H}=M_1^{-2}$ stated after Eqs. 18 and 29, and with the printed numerator it does not; the strong-shock limit $(\gamma+1)/(\gamma-1)$ is the same either way.)*
- **Eq. (5):** $\Phi_{ij}=\frac1{(2\pi)^2}\int R_{ij}(\mathbf r)e^{-\mathbf k\cdot\mathbf r}d^3r$: the exponent lacks the imaginary unit. *(Compiler check, not in the sources: with the inverse $R_{ij}=\int\Phi_{ij}e^{i\mathbf k\cdot\mathbf r}d^3k$, the forward transform over $d^3r$ carries $(2\pi)^{-3}$.)*
- **Fig. 3 caption:** the curves are "a function of the downstream Mach number", while panel (b) is labelled "Pre-shock Mach number, $\mathcal M_1$" and panel (a) is plotted against $\rho_1/\rho_2$.
- **$\mathcal K$, two definitions:** $\mathcal M_t/[Re_\lambda^{1/2}(\mathcal M_1-1)]$ (p. 7) and $\mathcal M_t/(\mathcal M_1-1)$ with threshold 0.6 (p. 16, matching the Fig. 10 line); the wrinkled/broken criterion is credited to Larsson and Donzis (p. 16), to Donzis (Fig. 10 caption) and to "Larsson et al." (p. 17).
- **Eq. (28c):** upright $R$ for $\mathcal R$.
- **Names:** ref. 60 is printed "S. Ghosh and P. P. Kerkar" and cited as "Kerkar and Ghosh"; ref. 104 is printed "N. Grube and M. Martín" and cited as "Grube and Martin" (p. 16) and "Grube and Pino" (Table I); refs. 18 and 16 print "M. D. Renzo" and "G. D. Posta".
- **Gao et al.:** Table I cites ref. 105 (the 2020 paper), while the Fig. 10 caption gives the same symbol to ref. 130 (a thesis).
- **p. 16 against Table I:** the highest DNS pre-shock Mach numbers "remain in the neighborhood of $\mathcal M_1\sim5$", while Table I lists Larsson et al. up to 6.
- Typos: "kinetic energy ration" (nomenclature), "an different prediction is what concerns" (p. 19).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathcal M_1$, $\mathcal M_2$, $\mathcal M_t$ | $M_1$, $M_2$ (page-local), $M_t$ | $M_t=\sqrt{R_{kk}}/\tilde c=\sqrt3u_{\mathrm{rms}}/\tilde c$ |
| $Re_{\lambda_\alpha}$, $\lambda_\alpha$ | $Re_\lambda$, $\lambda$ | |
| $R_{ij}=\widetilde{u_i''u_j''}$ | $\langle\rho u_i''u_j''\rangle/\langle\rho\rangle$ | Favre Reynolds stress; the tilde is a Favre average here |
| TKE | $k$ | |
| $K$, $K_a$, $K_r$, $K^r$, $K^a$ | $\mathrm{AF}_k$ (registry §11), $K_a$, $K_r$, $\mathrm{AF}^{\mathrm r}_k$, $\mathrm{AF}^{\mathrm a}_k$ (page-local) | **collision** with the spectral-page $K$ |
| R$_{11}$, R$_{22}$ (amplification, Figs. 11–12) | $\mathrm{AF}_{11}$, $\mathrm{AF}_{22}$ | **collision:** amplification factors, not stresses; index 2 is tangential to the shock |
| $\mathcal K$ (p. 7), $\mathcal K$ (p. 16) | $\mathcal K_{\mathrm D}$, $\mathcal K_{\mathrm{br}}$ (page-local) | two definitions in the source |
| $\eta_k$ | $\eta$ | Kolmogorov length |
| $\eta$, $\eta'$ | $\eta_{\mathrm a}$, $\eta'_{\mathrm a}$ (page-local) | **collision** with the Kolmogorov length |
| $\chi$ | $\chi_{\mathrm e}$ (page-local) | sign opposite to refs. 27 and 72 (different frame), as stated |
| $\delta$ | $\delta_{\mathrm{sh}}$ (page-local) | **collision** with the boundary-layer thickness |
| $\beta=c_2/c_1$ | $\beta_c$ (page-local) | |
| $\varepsilon$, $\varepsilon_r$, $\varepsilon_e$, $\varepsilon_a$ | $\epsilon_{\mathrm w}$, $\epsilon_{\mathrm r}$, $\epsilon_{\mathrm e}$, $\epsilon_{\mathrm a}$ (page-local) | perturbation amplitudes; **collision** with the dissipation $\varepsilon$ |
| $\tau$, $\theta$ | $\tau$, $\theta_k$ (page-local) | dimensionless time (not a stress); wavevector angle to the shock normal |
| $\Gamma$ | $\Gamma_{\mathrm H}$ (page-local) | normalized inverse Hugoniot slope |
| $\mathcal R$, $\mathcal P$, $\mathcal T$, $\Gamma_\rho$, $\Gamma_p$, $A_\rho$, $A_u$, $A_p$, $\mathrm P(\zeta)$ | (page-local) | jump ratios, slope parameters, prefactors, frequency density |
| $\Phi_{ij}$, $E(k)$ | (page-local), $E(k)$ | spectrum tensor, energy spectrum |
| $\bar\rho$, $\tilde u_i$ (Eq. 39) | $\bar\rho$, $\tilde u_i$ | filter and Favre filter |
| $\tau^{SGS}_{ij}=\bar\rho(\tilde u_i\tilde u_j-\widetilde{u_iu_j})$ | $-\tau_{ij}$ | **negative convention** |
| $\hat\sigma_{ij}$, $\mathcal V^{SGS}_{ij}=\bar\sigma_{ij}-\hat\sigma_{ij}$ | $\sigma_{ij}(\tilde u)$, (page-local) | the hat is not a test filter |
| $\mu_t$, $\tilde S_{ij}$ | $\mu_t$, $\tilde S^d_{ij}$ | Favre traceless strain |
| $\ell$, $\ell_T$, $\mathcal I$, $Re_\ell$, Da, $\delta_\nu$, $\delta_{\rm vib}$ | (page-local) | $\delta_\nu$ here is a viscous-dissipation thickness, not the registry's viscous length |
| $T$, $T_{ve}$ | (page-local) | two-temperature model |

# Reference list

134 printed references, numbered (superscript) style in order of first
citation. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. 14 is the
ingested [De Vanna et al. (2022)](/sources/devanna-2022.md). Refs. 39
(Ribner, NACA Report 1164) and 68 (Gordon & McBride, NASA report) print no
title and are identified by venue and number. Ref. 125 is a technical
report without institution, ref. 78 a university publication, ref. 100 a
DLR report, ref. 81 a reprint year; refs. 12 and 57 are arXiv preprints,
kept as their own entries, and ref. 66 a software version. Abbreviated
names are entered with the surnames printed elsewhere in the list (Della
Posta, Di Renzo, Martín). No item is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Linear interaction analysis of shock–turbulence interaction](/methods/linear-interaction-analysis.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
- [STREAmS](/software/streams.md)
