---
type: Source
title: "Hausmann et al. (2022) — An efficient model for subgrid-scale velocity enrichment for large-eddy simulations of turbulent flows"
description: "Subgrid velocity enrichment model: a truncated Fourier series per sub-domain evolved by the linearized subgrid momentum equation, with an RNG spectral eddy viscosity for the nonlinear relaxation and stochastic forcing toward a Yoshizawa energy target; it restores DNS spectra and intermittent gradient statistics in forced isotropic and shear turbulence at about twice the LES cost."
resource: "doi:10.1063/5.0127231"
source_kind: paper
authors: [Hausmann M., Evrard F., van Wachem B.]
year: 2022
venue: "Phys. Fluids 34:115135"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Physics_of_Fluids_Hausmann_An_efficient_model_for_subgrid-scale_velocity_enrichment_for.pdf"
tags: [sgs-velocity-reconstruction, spectral-eddy-viscosity, isotropic-turbulence, rapid-distortion-theory, kinematic-simulation]
timestamp: 2026-10-27T21:09:00Z
---

# Summary

Hausmann et al. (2022) propose a
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md) model
for applications that need the subgrid velocity field itself, not only a
closure of the stress of [large-eddy simulation](/definitions/large-eddy-simulation.md):
particle-laden flows, interface methods, mixing. From the exact subgrid
momentum equation the model keeps the linear sweeping and straining terms
(the rapid-distortion equations), replaces the nonlinear relaxation term by
the wavenumber-dependent RNG viscosity of Canuto & Dubovikov (a
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)), and
replaces the coupling with the subgrid stress by a stochastic forcing that
drives the subgrid kinetic energy toward Yoshizawa's estimate
$k_{\mathrm{sgs}}=C_I\Delta^2\lvert\bar S\rvert^2$ (the algebraic closure of
[one-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md);
a dynamic $C_I$ via the [dynamic procedure](/methods/dynamic-procedure.md) is
mentioned). The subgrid velocity is a truncated Fourier series, as in
kinematic simulation, but its coefficients evolve by explicit algebraic
updates followed by a divergence-free projection; a coarse structured grid
of sub-domains, with sub-domain-averaged LES velocity and gradients, carries
inhomogeneity, and an optional sigmoid interpolation makes the field nearly
divergence-free across sub-domain boundaries.

In forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
($Re_\lambda=75$; [DNS](/definitions/direct-numerical-simulation.md) $256^3$,
LES $32^3$ with the [Smagorinsky model](/methods/smagorinsky-model.md)) the
enriched field recovers the DNS spectrum beyond the cutoff and widens the
velocity-gradient and $Q_A$ distributions toward the DNS, with too little
skewness; results are insensitive to sub-domain count, mode number and
$C_\nu$, and the cost is about twice that of the LES. In a sinusoidally
forced shear flow (LES $16^3$ with the [Vreman model](/methods/vreman-model.md))
the generated field is inhomogeneous and anisotropic with a DNS-like
$R_{12}$ trend. The evaluation compares statistics of the running LES with
DNS ([a posteriori](/definitions/a-priori-and-a-posteriori-testing.md));
[variational multiscale](/methods/variational-multiscale-method.md) and
deconvolution reconstructions are reviewed as costlier alternatives.

# Version read

Version of record (Phys. Fluids 34:115135, AIP, CC BY 4.0; submitted 20
September 2022, accepted 19 October 2022, online 10 November 2022), 18 PDF
pages (an AIP cover and article pages 115135-1 to -17), all read; every
equation checked visually because text extraction garbled them. Page-1
title, authors and DOI match the metadata. No identity problem. Numbering on
this page is that of this version.

# Key claims

The source's tilde (LES filter) is the registry overbar; its subgrid
velocity $u'$ is $u^<_i$, its RNG viscosity $\nu'_t(k)$ is written
$\nu^{\mathrm{RNG}}_t(k)$ (page-local), its $K_{desired}$, $K_{actual}$ are $k^{\mathrm{tgt}}_{\mathrm{sgs}}$, $k^{\mathrm{act}}_{\mathrm{sgs}}$,
and $Q$ (second invariant of the velocity gradient) is $Q_A$.

1. Existing reconstructions (fractal interpolation, kinematic simulation, deconvolution and estimation, dynamic deconvolution, spectral enrichment of Bassenne et al., variational multiscale and multilevel methods, Gabor modes of Ghate & Lele) are limited in efficiency, applicability or accuracy; Bassenne et al. cost "of the order of a DNS", Ghate & Lele need mode quenching for long times (§I). **Stated**
2. The exact subgrid momentum equation contains three advection terms: nonlinear relaxation $u^<_j\partial_ju^<_i$, sweeping $\bar u_j\partial_ju^<_i$ and straining $u^<_j\partial_j\bar u_i$ (§II A, Eq. 8). **Derived**
3. After Laval et al., omitting the nonlinear relaxation overestimates the spectrum and the intermittency, and a turbulent viscosity compensates both (§II A). **Stated**
4. Nonlinear relaxation also shapes strain–rotation relations (the distribution of $Q_A$), which a turbulent viscosity cannot reproduce (§II A, §IV A). **Stated**/**Shown** (indirectly)
5. The RNG viscosity $\nu^{\mathrm{RNG}}_t(k)$ (Eq. 11, $C_\nu=2/5$) is larger at small wavenumbers and tends to zero at high wavenumbers, mimicking the transfer to small scales (§II B). **Stated**
6. The subgrid velocity is a truncated Fourier series of $N_m$ modes whose coefficients are updated explicitly (Eqs. 15–16) and projected to zero divergence (Eqs. 17–18); the cost is linear in $N_m$ (§II C). **Derived**
7. The projection follows from a spectral pressure Poisson equation for the Fourier coefficients of the subgrid pressure (Appendix, Eqs. A1–A13). **Derived**
8. Forcing directions are random on the unit sphere and correlated in time by an Ornstein–Uhlenbeck-type recursion with weights set by each mode's eddy rate (§II C, Eqs. 19–22). **Stated** (model design)
9. Sub-domains carry inhomogeneous statistics; the LES velocity and gradient are averaged per sub-domain, but the energy target is taken at the sub-domain centre cell because averaging Gaussianizes its distribution (§II D, §II F, Fig. 3). **Shown**
10. The interpolation of Eqs. (31)–(37) gives a nearly divergence-free field except at edges where four sub-domains meet; without it the divergence between sub-domains is significant (§II E, Fig. 2). **Shown**
11. Yoshizawa's estimate lies within ten percent of the subgrid kinetic energy of the DNS with a spectrally sharp filter in the isotropic case (§II F). **Shown** (stated numerically)
12. The subgrid spectrum from the coefficients (Eq. 23) coincides with the DNS, and LES plus subgrid spectra recover the whole DNS range (§IV A, Fig. 8). **Shown**
13. The enriched LES gives much wider, more intermittent velocity-gradient distributions than the LES, close to DNS except the extreme tails; the skewness of the longitudinal gradient is not reproduced (§IV A, Fig. 9). **Shown**
14. Non-Gaussian gradients arise despite Gaussian forcing from the non-Gaussian energy target across sub-domains and from sweeping and straining (§IV A). **Stated**
15. The $Q_A$ distribution is much wider than that of the LES and improved in shape, with less skewness than the DNS (§IV A, Fig. 10). **Shown**
16. In the decomposition of $Q_A$ (Eq. 54) the non-local terms $\bar u_iu^<_j+u^<_i\bar u_j$ are represented and $u^<_iu^<_j$ is not; improving $Q_A$ requires nonlinear relaxation and a modified forcing (§IV A, Eqs. 53–54). **Derived**/**Stated**
17. $Q_A$ distributions almost coincide for $8^3$, $16^3$ and $32^3$ sub-domains in isotropic turbulence (Fig. 10a). **Shown**
18. Multiplying the energy target by 1.5 and 2 widens the $Q_A$ tails without changing shape (Fig. 10b). **Shown**
19. No trend with mode number for $N_m\ge100$; without a nonlinear term modes exchange no information, so wavenumber-space parallelization is trivial (Fig. 10c). **Shown**
20. Varying $C_\nu$ from 0.1 to 1.6 changes the $Q_A$ distribution very little (Fig. 10d). **Shown**
21. $Q_A$ distributions with and without the divergence-free interpolation almost coincide (Fig. 11); the results are obtained without it. **Shown**
22. Time per reference time (isotropic case): LES $32\times10^3$ s, enriched LES $69\times10^3$ s, DNS $340\times10^6$ s; the enrichment about doubles the LES cost (Table III). **Shown**
23. In the shear flow the Vreman LES overpredicts the mean velocity amplitude and the $R_{11}$, $R_{22}$ correlations deviate from DNS; the small subgrid energy does not correct this (§III B 2, §IV B, Figs. 6, 12a). **Shown**
24. The generated subgrid velocity is inhomogeneous (extrema of the correlations located as in the DNS) and anisotropic (non-zero $R_{12}$ with a DNS-like trend), stepwise across sub-domains (§IV B, Fig. 12b). **Shown**
25. The Smagorinsky model is inaccurate in shear-dominated flows (citing Lévêque et al.), so the Vreman model, "known to produce more physical results in transitional shear flows", is used for the shear flow (§III A–B). **Stated**

# Printed slips

- **Eq. (11):** printed $\nu'_t(k)=\left(\nu_f^2-C_\nu\int_k^\infty q^{-2}E(q)\,dq\right)^{1/2}-\nu_f$. *(compiler check, not in the sources)* With the minus sign inside the root, $\nu'_t\le0$ (imaginary when the integral exceeds $\nu_f^2/C_\nu$), against the text that $\nu'_t$ is "larger for small wave numbers" and removes energy as a positive viscosity.
- **Eq. (40):** printed $\nu_t=(C_S\Delta)^2|\tilde S_{ij}|^2$. *(compiler check, not in the sources)* The printed product has units m²s⁻², not those of a viscosity.
- **Eq. (39):** printed viscous plus subgrid flux $\partial_j\{(\nu_f+\nu_t)/2\,(\partial_j\tilde u_i+\partial_i\tilde u_j)\}$. *(compiler check, not in the sources)* Eqs. (5) and (9) give $\partial_j\{(\nu_f+\nu_t)(\partial_j\tilde u_i+\partial_i\tilde u_j)\}$ for a divergence-free $\tilde u$, without the factor $1/2$.
- **Eq. (54):** printed $Q=\partial_i\partial_j(\tilde u_i\tilde u_j+\tilde u_iu'_j+u'_i\tilde u_j+u'_iu'_j)$. *(compiler check, not in the sources)* Eq. (53) with $\partial_iu_i=0$ gives $Q=-\tfrac12\partial_i\partial_j(u_iu_j)$.
- **Table I against §III B 1:** the text says the transverse integral length "is half the longitudinal" and that Table I approximately shows it, while Table I prints $l_{11}/L=0.079$, $l_{22}/L=0.49$, $l_{33}/L=0.38$.
- **$T_{E,m}=\sqrt{|k_m|^3E(|k_m|)}$** is called an "eddy-turnover time"; *(compiler check, not in the sources)* it has units of an inverse time and enters $\exp(-\Delta t\,T_{E,m})$ as a rate.
- **§IV A:** "standard deviations $\sigma_{A_{11}}$ and $\sigma_{A_{11}}$" (Fig. 9b prints $A_{12}/\sigma_{A_{12}}$).
- **Names:** "Lavel et al." (§II A, §II B) for Laval; "Domaradski et al." (p. 2) for Domaradzki.

# Notation map

| Hausmann et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde\phi$ | $\bar\phi$ | LES (grid) filter; **not** a Favre filter |
| $\phi'=\phi-\tilde\phi$, $u'$ | $\phi^<$, $u^<_i$ | subgrid part; the prime is the registry's Reynolds fluctuation |
| $\rho_f$, $\nu_f$ | $\rho$, $\nu$ | |
| $\tau_{ij}=\widetilde{u_iu_j}-\tilde u_i\tilde u_j$ | $\tau_{ij}$ | positive trace, agree |
| $\lvert\tilde S_{ij}\rvert=\sqrt{2\tilde S_{ij}\tilde S_{ij}}$ | $\lvert\bar S\rvert$ | factor two included |
| $C_S$, $C_V$, $C_I$ | $C_s$, (Vreman coefficient), $C_I$ | 0.1, 0.025, 0.0826 |
| $\nu'_t(k)$, $C_\nu$ | $\nu^{\mathrm{RNG}}_t(k)$, $C_\nu$ | page-local RNG viscosity of the subgrid equation and its constant; compare $\nu_t(k\mid k_c)$ |
| $K_{desired}$, $K_{actual}$, $K_{est}$ | $k^{\mathrm{tgt}}_{\mathrm{sgs}}$, $k^{\mathrm{act}}_{\mathrm{sgs}}$, $k_{\mathrm{sgs}}$ (target, present, Yoshizawa estimate) | page-local superscripts, as on the enrichment page |
| $K$ (total), $u_{rms}=\sqrt{2K/3}$ | $k$, $u_{\mathrm{rms}}$ | |
| $A_m$, $B_m$, $k_m$, $N_m$ | (Fourier coefficients, wavevector, mode count) | page-local |
| $T_{E,m}$, $\alpha_m$, $\beta_m=\sqrt{1-\alpha_m^2}$ | $\omega_{E,m}$, $a_m$, $\sqrt{1-a_m^2}$ | page-local eddy rate of mode $m$ and direction memory weights, as on the enrichment page; the source's $\alpha_m$, $\beta_m$ would collide with $\alpha_k$, $\beta_k$ |
| $\alpha$, $W$, $\Psi$ | (sigmoid sharpness, interpolation and correction kernels) | **collision** with the DG blending factor $\alpha$ |
| $Q=\tfrac12(\Omega_{ij}\Omega_{ij}-S_{ij}S_{ij})$ | $Q_A$ | second invariant of the velocity gradient |
| $\tilde A_{ij}=\partial\tilde u_i/\partial x_j$ | (resolved velocity gradient) | |
| $\mathscr C_{ij}$ | $R_{ij}$ | averaged in time, $x$ and $z$ |
| $l_{\alpha\alpha}$, $\lambda$, $\eta$, $\tau_\eta$ | $L$ (per direction), $\lambda$, $\eta$, $\tau_\eta$ | agree |
| $\mathscr P$, $F_i$, $s_i$ | (modified pressure), $f_i$ | large-scale forcing; the source's $f_i$ is the **subgrid** forcing (collision) |

# Reference list

50 printed references, numbered (AIP superscript style). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Mallouppas 2013 (article and PhD thesis) take suffixes in printed order;
Jiménez (2007) is printed without pages. No printed duplicate, no
unparseable item.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [Subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)
- [Variational multiscale method](/methods/variational-multiscale-method.md)
- [Vreman model](/methods/vreman-model.md)
