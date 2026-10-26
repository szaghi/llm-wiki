---
type: Source
title: "Seyedi & Zayernouri (2022) — A data-driven dynamic nonlocal subgrid-scale model for turbulent flows"
description: "Adds a dynamic procedure, the Germano identity written for the subgrid force, to the fractional (nonlocal) subgrid-scale model, fixes the fractional order from filtered DNS data, and tests the model a priori and a posteriori in homogeneous isotropic turbulence, including backscatter."
resource: "doi:10.1063/5.0079461"
source_kind: paper
authors: [Seyedi S.H., Zayernouri M.]
year: 2022
venue: "Phys. Fluids 34:035104"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Seyedi_A_data-driven_dynamic_nonlocal_subgrid-scale_model_for_turbu.pdf"
tags: [les, sgs-model, data-driven, energy-cascade, a-priori-a-posteriori]
timestamp: 2026-10-26T05:09:00Z
---

# Summary

Seyedi & Zayernouri (2022) make the
[fractional subgrid-scale model](/methods/fractional-sgs-model.md) (FSGS) of
Samiee, Akhavan-Safaei & Zayernouri (2020) dynamic. FSGS comes from a
filtered Boltzmann–BGK equation whose filtered equilibrium is closed by an
isotropic Lévy $\beta$-stable distribution. At the continuum level the
subgrid force is a coefficient times the fractional Laplacian of the
filtered velocity, $\partial_j\tau_{ij}=C_{\mathrm{fr}} F(s)(-\nabla^2)^s\bar u_i$,
with $s\in(0,1]$. The new D-FSGS model writes the
[Germano identity](/methods/dynamic-procedure.md) for the force (the
divergence of the stress) rather than for the stress, with the test filter
at twice the grid filter, and obtains $C_{\mathrm{fr}}$ by a Lilly-type
least-squares contraction averaged over homogeneous directions. Test
filtering does not commute with the fractional operator, so the two terms
of the contraction differ.

The fractional order is set from filtered DNS: by maximizing the stress
correlation, by a power law $s^{\mathrm{opt}}=a\ell_\Delta^{\,b}$
fitted at $Re_\lambda=170$, 240, 355, or by the rule $s=0.5$ for the
range where less than about ten percent of the kinetic energy is modelled.

In a priori tests on forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
([DNS](/definitions/direct-numerical-simulation.md) at $320^3$ to $1024^3$,
box filters), D-FSGS correlates better with the filtered-DNS stress than the
[Smagorinsky model](/methods/smagorinsky-model.md), its dynamic version and
static FSGS. It predicts [backscatter](/definitions/energy-backscatter.md)
at 24% of the points against 26% in the DNS and 20% for dynamic
Smagorinsky (filter size 4). In a posteriori runs of decaying turbulence,
D-FSGS gives the resolved-energy decay and the third-order structure
function closest to the filtered DNS. Its gain over dynamic Smagorinsky is largest at the
very-large-eddy filter width. These are the
[a priori and a posteriori](/definitions/a-priori-and-a-posteriori-testing.md)
pair within [LES](/definitions/large-eddy-simulation.md). The introduction
motivates nonlocal closures by the failure of the local
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md).

# Version read

arXiv preprint arXiv:2111.10936v3 [physics.flu-dyn], 24 November 2021 (AIP
template, "Dated: 25 November 2021"), 26 pages, not the Phys. Fluids version
of record. Title and authors on page 1 match Crossref (capitalization
differs only). The version read prints no DOI. Section, equation and figure
numbers on this page are those of the preprint.

# Key claims

Page-local symbols, as on the [fractional SGS model](/methods/fractional-sgs-model.md)
page: $s$ the fractional order (the paper's $\alpha$); $(-\nabla^2)^s$ the
fractional Laplacian; $C_{\mathrm{fr}}$, $F(s)$, $\nu_s=C_{\mathrm{fr}}F(s)$
the model coefficient, its Gamma-function factor and their product;
$\ell_\Delta$ the filter width in units of DNS grid spacings (see the
notation map); $\mathcal T_{ij}$ the subtest-scale stress; $Q_i$ the nonlocal
contraction term.

1. D-FSGS is presented as the first SGS model that combines nonlocality and a dynamic procedure ("both nonlocality and dynamic features have been leveraged together for the first time") (§I, p. 4). **Stated**
2. Existing nonlocal models suffer from sensitivity to the model constant and fractional order, low correlation with the true SGS stress, and no backscatter; D-FSGS is designed to remove all three (§I, p. 4). **Stated**
3. The FSGS force is $\partial_j\tau_{ij}=\nu_s(-\nabla^2)^s\bar u_i$, $s\in(0,1]$, with $\nu_s=C_{\mathrm{fr}}F(s)$, $F(s)=2^{2s}\Gamma(\tfrac{2s+3}{2})\Gamma(2s+1)/(\pi^{3/2}|\Gamma(-s)|)$, and $C_{\mathrm{fr}}$ proportional to $U^{2s}\mathcal T_r^{2s-1}$ from kinetic theory (Eqs. 11, 14, 15, §II.1). **Stated** (recalled from Samiee et al. 2020)
4. Filtering commutes with integer-order derivatives (homogeneous filter) but not with fractional-order ones: for $s=0.6$ the PDFs of the test-filtered fractional derivative and of the fractional derivative of the test-filtered field differ (§II.2, Fig. 1). **Shown**
5. The Germano identity in force form, $\partial_j\mathcal T_{ij}-\widehat{\partial_j\tau_{ij}}=\partial_jL_{ij}$, with Lilly's least squares gives $C_{\mathrm{fr}}=\langle\partial_jL_{ij}Q_i\rangle/\langle Q_iQ_i\rangle$, $Q_i=F(s)(-\nabla^2)^s\hat{\bar u}_i-\widehat{F(s)(-\nabla^2)^s\bar u_i}$, assuming the same coefficient at grid and test level and a spatially uniform coefficient (Eqs. 16–22). **Derived**
6. To avoid instability from negative eddy viscosity over long periods, the coefficient is averaged over directions of statistical homogeneity (§II.2, p. 10). **Stated**
7. Fig. 2 compares the dynamic Smagorinsky and D-FSGS coefficients along "the middle imaginary line" of the periodic domain at $\ell_\Delta=4$; the text does not discuss the plot (§II.2). **Shown** (plot only)
8. First approach: sweeping $s$ from 0 to 1 in steps of 0.01 and maximizing the ensemble-averaged correlation over all stress components gives an $s^{\mathrm{opt}}$ that decreases with $\ell_\Delta$ at each $Re_\lambda$ (§III.1, Fig. 3a). **Shown**
9. Second approach: $s^{\mathrm{opt}}=a\ell_\Delta^{\,b}$ with $(a,b)=(1.53,-0.62)$ at $Re_\lambda=170$, $(1.39,-0.49)$ at 240, $(1.08,-0.30)$ at 355, coefficient of determination above 0.98; interpolation in Table I for other $Re_\lambda$ (Eq. 23, Table I). **Shown**
10. At a given filter size, $s^{\mathrm{opt}}$ rises with $Re_\lambda$ (§III.1, p. 12; §V). **Shown**. From Table I, $s^{\mathrm{opt}}\approx0.65$, 0.70, 0.71 at $\ell_\Delta=4$ and $\approx0.27$, 0.36, 0.47 at $\ell_\Delta=16$ for $Re_\lambda=170$, 240, 355 *(compiler check, not in the sources)*.
11. The error bars of $s^{\mathrm{opt}}$ grow in the very-large-eddy range because larger filters include more nonlocality (§III.1, p. 12). **Stated**
12. Third approach: since "almost all of the LES studies are designed to model about less than ten percent of the total kinetic energy", $s=0.5$ is taken for the LES range at all $Re_\lambda$ (§III.1, p. 13, Fig. 3b–d). **Shown** (rule chosen from the a priori plots)
13. With the second or third approach the model is "totally free of any tuning parameter including fractional-order" (§III.1, p. 13). **Stated**
14. A priori at $Re_\lambda=240$, D-FSGS has higher ensemble-averaged correlation than Smagorinsky, dynamic Smagorinsky and FSGS for all six stress components at $\ell_\Delta=4$ and 8 (§III.2, Fig. 4). **Shown**
15. The dynamic procedure raises the correlation markedly for the nonlocal model but not for the local one: "dynamic local models do not necessarily increase the correlation coefficient remarkably" (§III.2, Fig. 4). **Shown**
16. Only D-FSGS and dynamic Smagorinsky predict backscatter ($\Pi<0$); dynamic Smagorinsky overpredicts the tails of the $\Pi$ PDF, which the authors link to its need for averaging a posteriori (§III.2, Fig. 5). **Shown**
17. Fraction of points with backscatter (3D box filter at grid and test level): DNS 26%, dynamic Smagorinsky 20%, D-FSGS 24% at $\ell_\Delta=4$; 30%, 18%, 25% at $\ell_\Delta=8$ (§III.2, p. 15). **Shown**
18. The PDFs of the SGS force in all three directions at $\ell_\Delta=4$ and 8 agree better with the filtered DNS for D-FSGS than for the other three models, tails and peaks included (§III.2, Fig. 6). **Shown**
19. With the power-law $s^{\mathrm{opt}}$ or with $s=0.5$, D-FSGS still correlates better than the other models for all filter sizes tested ($\ell_\Delta$ from 2 to 10) (§III.2, Fig. 7). **Shown**
20. The dynamic model is less sensitive to $s$ near 0.5 because the dynamic coefficient compensates (§III.2, p. 17). **Shown** (Fig. 7); the explanation is **Stated**
21. An optimal order of 0.5 "validates that the overall scaled up and nonlocal behavior of the closure term in our dynamic model emerges of total" first order ($2s^{\mathrm{opt}}=1$), consistent with a closure originating from the first-order nonlinear convective term (§III.2, p. 17). **Stated**
22. A posteriori (decaying turbulence, $Re_\lambda=240$, $\ell_\Delta=4$), the spectra are compared at $t/\tau_L\simeq2$ and 4, long times chosen "to address the numerical stability of models"; Smagorinsky is called "one of the most dissipative models", the no-model run is expected to accumulate energy at high wavenumbers, and D-FSGS "should be ideally placed between" them (§IV, Fig. 8). **Stated** (the text gives no measure of the spectra)
23. Resolved kinetic energy decays closer to the filtered DNS with D-FSGS than with dynamic Smagorinsky at $\ell_\Delta=4$ and, more markedly, at $\ell_\Delta=20$ (very-large-eddy range), where dynamic Smagorinsky decays too fast (§IV, Fig. 9). **Shown**
24. All models nearly preserve the second-order structure function at $\ell_\Delta=4$, $t/\tau_L\simeq2$; the Smagorinsky-based models deviate more on the third-order one (§IV, Fig. 10). **Shown**
25. "Bigger filter sizes rather than the conventional LES filter sizes" show "promising potential" with D-FSGS and could compensate the cost of fractional operators (§V). **Stated**
26. Large-eddy turnover time of the a posteriori case $\tau_L\simeq2.7$; time step with CFL below one (§IV, p. 17). **Stated**

# Printed slips

- **Range of the operator order (Eq. 11).** "$(-\Delta^\alpha)(\cdot)$ denotes the space-fractional Laplacian of order $2\alpha\in(1,2]$", while the same equation states $\alpha\in(0,1]$, which gives $2\alpha\in(0,2]$; the sweep of §III.1 covers $\alpha$ from 0 to 1.
- **Operator symbol.** $(-\Delta^\alpha)$ in Eqs. 11, 13, 16, 19, $(-\Delta)^\alpha$ in Eq. 12, $(-\nabla)^\alpha$ in the Fig. 1b legend.
- **Relaxation time.** Eq. 7 writes $\tau$ where Eq. 5 uses $\mathcal T$.
- **Eq. 10.** $f^\beta(\bar{\mathcal K})=\frac{\rho}{U^3}F^\beta(\mathcal K)$: argument $\bar{\mathcal K}$ on the left, $\mathcal K$ on the right.
- **Eqs. 19, 21.** The velocity is written $\bar V_i$, $\hat{\bar V}_i$ (the kinetic-theory fluid velocity of Eq. 6), where Eq. 16 has $\hat{\bar u}_i$.
- **Eq. 22.** The bracket $\langle\cdot\rangle$ is not defined at that point (in §III it is the ensemble average over snapshots).
- **Eq. 24 labels.** The text calls $E_r=\tfrac12(\overline{u_iu_i}-\bar u_i\bar u_i)$ the "resolved" and $E_f=\tfrac12\bar u_i\bar u_i$ the "filtered" kinetic energy; $E_r$ as printed is the subfilter energy. The formula of the modelled-energy percentage is not printed.
- **Eq. 4.** $|\bar S|=\sqrt{2S_{ij}S_{ij}}$, without overbars inside the root.
- **Kraichnan citation.** The introduction dates Kraichnan's nonlocal expression to "the same year" as Hinze et al. (1974), but ref. 33 is Kraichnan, Phys. Fluids 7 (1964).
- **Egolf and Hutter.** The text cites "Egolf and Hutter$^{36,39}$"; ref. 39 prints "P. W. Egolf and K. Kutter".
- **Figs. 8–9 against the text.** §IV lists Smagorinsky among the models of Fig. 9, which shows only filtered DNS, dynamic Smagorinsky and D-FSGS; Fig. 8 has no dynamic-Smagorinsky curve.
- **Typos.** "lower and higher bonds", "subgird-scales" (p. 6), "Smagorisnky" (pp. 5, 6), "superior math" (p. 15).

# Notation map

| Seyedi & Zayernouri (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u_i$, $\hat{\bar u}_i$ | $\bar u_i$, $\hat{\bar u}_i$ | LES filter, test filter at twice the grid filter |
| $\tau_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$ | $\tau_{ij}$ | positive trace, as in the registry |
| $(\nabla.\tau)_i$ | $\partial_j\tau_{ij}$ | the model is posed on the force |
| $T_{ij}$ | $\mathcal T_{ij}$ (page-local) | subtest-scale stress, as on the dynamic-procedure page |
| $G_{ij}=\widehat{\bar u_i\bar u_j}-\hat{\bar u}_i\hat{\bar u}_j$ | $L_{ij}$ | resolved stress of the Germano identity |
| $\nu_t=C_s\mathcal L^2\lvert\bar S\rvert$ | $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$ | **collision:** the source's $C_s$ is the registry's $C_s^2$; value not printed |
| $\mathcal L$ | $\Delta$ | "effective grid scale"; **collision** with the registry loss $\mathcal L$ |
| $\mathcal L_\delta=\mathcal L/(2\delta_X)$, $\delta_X=2\pi/N$ | $\ell_\Delta$ (page-local) | filter size in DNS grid spacings, factor 2 as printed |
| $N$ | $N_x$ | DNS points per direction (320, 520, 1024) |
| $(-\Delta^\alpha)$, $(-\Delta)^\alpha$ | $(-\nabla^2)^s$ (page-local) | **collision:** the source's $\Delta$ is the Laplacian, not the filter width |
| $\alpha$, $\alpha^{opt}$ | $s$, $s^{\mathrm{opt}}$ (page-local) | fractional order; renamed because the registry's $\alpha$ is the DG/FV blending factor |
| $\mathcal C$, $C$, $C_1$, $C_2$ | $C_{\mathrm{fr}}$ (page-local) | dynamic coefficient, $C_1=C_2$ assumed; not $C_f$, the registry's skin-friction coefficient |
| $F(\alpha)$, $\nu_\alpha$, $c_{d,\alpha}$ | $F(s)$, $\nu_s$, $c_{d,s}$ (page-local) | Eqs. 12, 14, 15 |
| $N_i$ | $Q_i$ (page-local) | nonlocal term of the least-squares contraction, Eq. 21 |
| $f$, $f^{eq}$, $\mathcal T$, $U$, $V$, $\mathcal K$, $F^\beta$, $\mathfrak D_\beta$ | (kinetic-level symbols; relaxation time $\mathcal T_r$) | BGK derivation only |
| $\Pi=-\langle\tau_{ij}\bar S_{ij}\rangle$ (printed $\prod$) | $\Pi$ | same sign; the PDFs are of the local quantity |
| $\langle\cdot\rangle$ | $\langle\cdot\rangle$ | ensemble average over snapshots (§III), homogeneous-direction average (Eq. 22) |
| $E(K)$, $K$ | $E(k)$, $k$ | energy spectrum |
| $E_f$, $E_r$, $\phi$ | $\tfrac12\bar u_i\bar u_i$, $k_{\mathrm{sgs}}$, (modelled-energy percentage) | see Printed slips |
| $\tau_\mathcal L$ | $\tau_L$ (page-local) | large-eddy turnover time |
| $\delta_r\bar u_L$, $r$ | (longitudinal increment, separation) | Eq. 25 |
| UNS | (no-model run on the LES grid) | |

# Reference list

62 printed references, numbered (AIP style) with titles. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. 41 is printed "in press" with an arXiv identifier and is kept as a
pre-publication entry; refs. 21, 27, 35, 44, 50 and 60 are arXiv preprints.
Several entries are incomplete as printed (ref. 1 without publisher, ref. 26
"Numerical Methods 157 (2019)", ref. 52 without venue, ref. 39 with the
author "Kutter" and a garbled venue), recorded as printed. Same-surname
same-year works (Suzuki 2021, four; Akhavan-Safaei 2020 and 2021, two each)
are disambiguated in printed order. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-25). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Fractional subgrid-scale model](/methods/fractional-sgs-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
