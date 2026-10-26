---
type: Source
title: "Vela-Martín (2022) — Subgrid-scale models of isotropic turbulence need not produce energy backscatter"
description: "Uses the gauge freedom of the subgrid-scale stress (adding a divergence-free tensor) and a projected-gradient optimisation on filtered isotropic-turbulence DNS to remove nearly all local backscatter, arguing that backscatter is conservative spatial flux and that purely dissipative SGS models suffice away from walls."
resource: "doi:10.1017/jfm.2022.123"
source_kind: paper
authors: [Vela-Martín A.]
year: 2022
venue: "J. Fluid Mech. 937:A14"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Journal_of_Fluid_Mechanics_Vela-Martín_Subgrid-scale_models_of_isotropic_turbulence_need_not_produc.pdf"
tags: [les, sgs-model, eddy-viscosity, a-priori-a-posteriori, energy-cascade]
timestamp: 2026-10-25T13:42:00Z
---

# Summary

Vela-Martín (2022) asks whether [LES](/definitions/large-eddy-simulation.md) subgrid models of
isotropic turbulence must reproduce [energy backscatter](/definitions/energy-backscatter.md), the
negative values of the local subgrid energy flux $\Pi=-\tau_{ij}\bar S_{ij}$. The argument rests
on a gauge freedom of the filtered Navier–Stokes equations. The subgrid stress enters only through
its divergence, so adding any symmetric divergence-free tensor leaves the resolved dynamics
unchanged. Such a change keeps the total subgrid energy term $-\bar u_i\partial_j\tau_{ij}$ and the
mean $\langle\Pi\rangle$. It moves the local exchange between the source $\Pi$ and a conservative
spatial-flux term $D$, which has zero mean.

The contribution is a projected-gradient-descent optimisation. Starting from the standard stress,
it minimises $\langle\Pi^2\rangle$, and hence the variance of $\Pi$, over all symmetric tensors that
have the prescribed divergence; the $L^2$ projector onto that set is derived analytically. The
optimisation is applied a priori to filtered DNS of linearly forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at $Re_\lambda=140$, 240 and
324, with sharp-Fourier and Gaussian filters at inertial-range widths. It cuts the backscatter
volume fraction from about 0.4–0.5 (sharp) or 0.15 (Gaussian) to about $10^{-3}$, and the net
backscatter to about $10^{-4}$, whatever the Reynolds number, filter width or filter type. The
optimised flux is almost uncorrelated with the standard one, while $D$ barely changes. Its flatness
does not grow with decreasing scale, whereas the gauge-invariant total does.

Three consequences are drawn. First, the "optimal" a priori eddy viscosity that reproduces the local
flux exactly ([Boussinesq form](/definitions/boussinesq-hypothesis.md),
$\nu_t^{\mathrm{opt}}=\Pi/\lvert\bar S\rvert^2$) can be made positive almost everywhere by choosing the
gauge. Second, backscatter is conservative spatial flux, not a local inverse cascade, which supports
purely dissipative models such as the [Smagorinsky model](/methods/smagorinsky-model.md) away from
walls; the author sets this against the view that backscatter is a local inverse cascade to be
modelled explicitly (dynamic localization), and notes that negative-viscosity
[dynamic](/methods/dynamic-procedure.md) and stable-backscatter [similarity](/methods/scale-similarity-model.md) models produce backscatter. Third, equivalent stress representations
correlate only 0.4–0.6 with each other, so a poor a priori correlation of a model is not, by itself,
evidence of poor modelling ([a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).

# Version read

Version of record (Cambridge University Press typeset, open access CC-BY 4.0), 28 pages
(937 A14-1 to A14-28). Title, single author, venue and DOI on page 1 match the published metadata
above. No identity issue. Equation, section and page numbers on this page are those of the version
of record.

# Key claims

The source writes the subgrid stress with the opposite sign to the registry; the claims below are
translated (see the Notation map). Superscripts S, A and O label the standard, an alternative and the
optimised representation.

1. The filtered equations depend on the subgrid stress only through its divergence, so $\tau^A_{ij}=\tau^S_{ij}+\tau^*_{ij}$ with $\partial_j\tau^*_{ij}=0$ is physically equivalent to $\tau^S_{ij}$ (gauge invariance, after Jiménez 2016) (§3, Eqs. 3.1–3.2). **Derived**.
2. Under such a change the total subgrid energy term is invariant, $D^S-\Pi^S=D^A-\Pi^A$ with $D=-\partial_j(\bar u_i\tau_{ij})$, and so is $\langle\Pi\rangle$ (since $\langle D\rangle=0$); the local $\Pi$ and $D$ in general change (§3, Eqs. 3.3–3.5). **Derived**.
3. The admissible representations form the linear set $\partial_j\tau_{ij}=\partial_j\tau^S_{ij}$, $\tau_{ij}=\tau_{ji}$; minimising $\langle\Pi^2\rangle$ in it minimises the standard deviation of $\Pi$, because $\langle\Pi\rangle$ is invariant (§4, Eqs. 4.1–4.3). **Derived**.
4. The constrained minimisation leads to a closed linear system (Eqs. A8–A9) with no known analytical solution; it is solved by projected gradient descent with descent direction $2\Pi\bar S_{ij}$ (the gradient of $\int_V\Pi^2\,dV$ with respect to the source's stress $-\tau_{ij}$) and an $L^2$-closest projector onto the constraint set (§4, Apps. A–B). **Derived**.
5. The projector is $\tau^P_{ij}=\tau^*_{ij}-\tfrac12(\partial_i\gamma_j+\partial_j\gamma_i)$, with $\gamma_i$ from Poisson problems for $\partial_k\gamma_k$ and $\gamma_i$ under periodic conditions (App. B, Eqs. B12–B14). **Derived**.
6. In the database $\langle\Pi^S\rangle/\varepsilon$ is very close to one for all filter widths, Reynolds numbers and both filters, which confirms inertial-range filter widths (§5.3, Fig. 1). **Shown**.
7. The standard flux shows backscatter in about half of the domain with the sharp-Fourier filter ($v^-\approx0.5$) and in less than one-fifth with the Gaussian filter ($v^-\approx0.15$); the net backscatter $f^-$ is close to one for the sharp filter and about 0.05 for the Gaussian; both grow as the filter width decreases (§5.3, Fig. 2c,d). **Shown**.
8. The optimisation reduces $\sigma(\Pi)$ by a factor of 10 before a plateau (sharp filter); the Gaussian filter starts from about half that value and plateaus at a similar one; whether a local or a global minimum is reached is unclear (§6.1, Fig. 3a–d; $\Delta=0.33L$, $Re_\lambda=240$). **Shown**.
9. From sharp-filter values $f^-\approx0.6$, $v^-\approx0.4$, the optimisation reduces backscatter by about three orders of magnitude, to $v^-\sim10^{-3}$ and $f^-\sim10^{-4}$; the Gaussian filter reaches comparable values; results are insensitive to the grid parameter $\alpha_{\mathrm g}=1,2,3$ (§6.1, Fig. 3e–h). **Shown**.
10. For all filter widths and $Re_\lambda$ the optimised fluxes have $v^-\approx10^{-3}$ and $f^-\approx10^{-4}$, nearly independent of width, Reynolds number and filter type (§6.2, Fig. 4c–f). **Shown**.
11. Logarithmic fits of the optimised standard deviation give $\sigma=\langle\Pi\rangle(0.25-0.037\log(\Delta/L))$ (sharp) and $\sigma=\langle\Pi\rangle(0.25-0.033\log(\Delta/L))$ (Gaussian): a weak dependence on the filter width (§6.2, Fig. 4a,b). **Shown**.
12. The optimisation changes $\Pi$ strongly and $D$ only slightly: $\rho(D^S,D^O)\approx0.9$ while $\rho(\Pi^S,\Pi^O)\approx0.01$, across $Re_\lambda$, widths and filters (§6.3, Fig. 5c,d). **Shown**.
13. Optimised fluxes from the two filters collapse in p.d.f. and correlate better than the standard ones ($\approx0.65$ against $\approx0.4$): part of the filter-type difference in $\Pi^S$ is conservative spatial flux (§6.3, Fig. 5b,f). **Shown**.
14. The skewness of $\Pi^S$ grows as the filter width decreases and is larger for the Gaussian filter; after optimisation the Gaussian skewness drops to sharp-filter values (§6.3, Fig. 6a,b). **Shown**.
15. The flatness of $\Pi^S$ grows as a power law as the width decreases (agreeing with Cerutti & Meneveau 1998), the flatness of $\Pi^O$ stays about constant, and the flatness of the gauge-invariant $D-\Pi$ grows: intermittency need not be modelled in the flux but persists in the total subgrid interaction (§6.3, Fig. 6c,d). **Shown**.
16. The correlation of the equivalent tensors $\tau^S_{ij}$ and $\tau^O_{ij}$ (all components) falls from about 0.6 at $\Delta/L=0.64$ to about 0.4 at $\Delta/L=0.08$; traceless-only or off-diagonal-only correlations are below 0.5 (§6.3). **Shown**.
17. In two-dimensional cuts ($\Delta=0.08L$, Gaussian filter), intense forward events of $\Pi^S$ are surrounded by intense backscatter in advection-like patterns; after optimisation backscatter survives only in isolated spots of size about $3\Delta$ and intensity about $-0.1\langle\Pi\rangle$ (§6.4, Fig. 7). **Shown**.
18. The $L^2$-optimal a priori eddy viscosity $\nu_t^{\mathrm{opt}}=-\tau_{ij}\bar S_{ij}/(2\bar S_{ij}\bar S_{ij})=\Pi/\lvert\bar S\rvert^2$ reproduces the local flux exactly; it is gauge-dependent, negative over a large part of the domain for $\tau^S$, and positive almost everywhere for $\tau^O$, so a purely dissipative eddy viscosity that is "perfect" for the flux exists (§7.1, Eqs. 7.2–7.5). **Derived** (positivity **Shown**).
19. Backscatter ($\Pi<0$) is not a net inverse interscale flux but conservative spatial flux, and need not be modelled to reproduce the local resolved–subgrid energy exchange in LES of isotropic turbulence (§8). **Shown** (a priori).
20. Inertial-range dynamics is time-reversible, and global inverse cascades are possible but highly improbable (statistical irreversibility); the elimination of backscatter suggests the same limitation acts locally, so the cascade can be modelled as an irreversible energy sink (§7.2, §8). **Stated** (argued, not proved).
21. Backscatter cannot always be eliminated: in the global inverse-cascade experiments of Carati et al. (2001) and Vela-Martín & Jiménez (2021) $\langle\Pi\rangle<0$, and the procedure cannot remove it (§8). **Stated**.
22. A poor correlation between a model stress and $\tau^S$ is not necessarily a sign of poor modelling, since equivalent representations are themselves poorly correlated; this may explain the success of eddy-viscosity models despite poor a priori correlation (§8). **Derived/Stated**.
23. The conclusions are limited to isotropic turbulence away from walls, at filter widths little affected by large-scale anisotropy (§8). **Stated**.
24. Eliminating backscatter may be unnecessary or undesirable for models with numerically stable backscatter (similarity, tensor-diffusivity); the procedure is a demonstration, not a model (§8). **Stated**.
25. Because the numerical filter is a projector, the stresses, fluxes, descent direction and optimised stresses are Galilean-invariant (§5.2). **Stated**.

# Printed slips

- §3, p. A14-6: "To $\tau^S_{ij}$ … we can add any tensor field with zero divergence … and $\tau^S_{ij}$ produces the same physical effect": the second $\tau^S_{ij}$ is evidently $\tau^A_{ij}$.
- Eq. (3.5) prints $\langle u_j\partial_i\tau^S_{ij}\rangle=\langle u_j\partial_i\tau^A_{ij}\rangle=\langle T^S\rangle=\langle T^A\rangle$, with unfiltered $u$ and indices swapped relative to Eq. (3.3) $\bar u_i\partial_j\tau^S_{ij}$. by Eq. 2.5 and $\langle D\rangle=0$, $\langle\bar u_i\partial_j\tau^S_{ij}\rangle=-\langle T^S\rangle$; the conclusion $\langle T^S\rangle=\langle T^A\rangle$ is unaffected *(compiler check, not in the sources)*.
- §6.1: "the PSD algorithm", for PGD.
- §6.3: "For the standard SGS fluxes, $\rho(T^S_s,T^O_g)=0.4$": for the standard fluxes the superscript should be S on both.
- Fig. 6 and Fig. 7 captions and §6.4 give $Re_\lambda=320$ for the $1024^3$ case; Table 1 and §5.1 give 324.
- §8 says intermittency "remains as part of the total SGS interactions (§ 6.2)"; the flatness of $D-T$ is discussed in §6.3.
- §6.1 gives sharp-filter starting values "$f^-\approx0.6$ and $v^-\approx0.4$" at $\Delta=0.33L$, $Re_\lambda=240$, while §5.3 states in general that sharp-filter backscatter occupies "around half of the points" with net backscatter "close to unity".
- Eq. (A4) writes $\partial\gamma_i\,\delta\tau_{ij}$ without the index $j$ (Eq. B5 prints $\partial_j\gamma_i$).
- Eqs. (A5)/(B6): $\mu_{ij}(\delta\tau_{ij}-\delta\tau_{ji})=(\mu_{ij}-\mu_{ji})\delta\tau_{ji}$. relabelling the dummy indices gives $(\mu_{ij}-\mu_{ji})\delta\tau_{ij}$, the negative of the printed right side; (A6)/(B7) use $\delta\tau_{ij}$. Harmless, since $\mu_{ij}$ is eliminated *(compiler check, not in the sources)*.
- Appendix B signs: (B4) prints the derivative of $\tfrac12(\tau^*_{ij}-\tau^P_{ij})^2$ with respect to $\tau^P_{ij}$ as $+(\tau^*_{ij}-\tau^P_{ij})$, and (B9) prints $2(\tau^P_{ij}-\tau^*_{ij})$ while (B10) and (B14) follow the opposite sign. the derivative is $-(\tau^*_{ij}-\tau^P_{ij})$; since $\gamma_i$ is a free multiplier, (B12)–(B14) remain self-consistent and (B14) satisfies the constraint *(compiler check, not in the sources)*.
- Eq. (B10) writes $\partial_i\tau^*_{ij}$ for $\partial_j\tau^*_{ij}$, and the text before it writes the constraint as $\partial_i\tau^P_{ij}=Q_i$ for $\partial_j\tau^P_{ij}=Q_i$ (B3).
- Reference list: Kraichnan (1967) "Phys. Fluids 10, 1417–1413" (end page below start page).
- Typo: "practial relevance" (§8).

# Notation map

| Vela-Martín (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau^S_{ij}=\bar u_i\bar u_j-\overline{u_iu_j}$ | $-\tau_{ij}$ | **sign opposite to the registry** (the author flags it as opposite to the usual); enters as $+\partial_j\tau^S_{ij}$ |
| $T=\bar S_{ij}\tau_{ij}$ | $\Pi=-\tau_{ij}\bar S_{ij}$ | same value and sign: positive = forward cascade |
| $D=\partial_j(\bar u_i\tau_{ij})$ | $D=-\partial_j(\bar u_i\tau_{ij})$ (local) | conservative spatial flux, zero mean |
| $\ell$ | $\Delta$ | filter width; sharp cutoff $k_c=\pi/\Delta$ |
| $\hat G(\mathbf k)$ | $\hat G(k)$ | Gaussian $\exp(-k^2\Delta^2/(2\pi^2))$ (Eq. 5.4) |
| $\widetilde{(\cdot)}$ | — | **collision:** numerical (Fourier-truncation) filter, not the Favre filter |
| $\hat{(\cdot)}$ | $\phi_{\boldsymbol k}$ | **collision:** Fourier transform, not the test filter |
| $\alpha$ | $\alpha_{\mathrm g}$ (local) | grid parameter of the numerical filter, $k_i^{\max}=\alpha\pi/\ell$; **collision** with the DG blending factor |
| $\nu_s$, $\nu_s^{opt}$ | $\nu_t$, $\nu_t^{\mathrm{opt}}$ | eddy viscosity; model written $\tau^M_{ij}-\tfrac13\tau^M_{kk}\delta_{ij}=2\nu_s\bar S_{ij}$, i.e. $\tau^d_{ij}=-2\nu_t\bar S_{ij}$ in registry sign |
| $\beta$ | — | step size of the gradient descent; **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $\gamma_i$, $\mu_{ij}$ | — | Lagrange multipliers; $\gamma_i$ **collides** with the ratio of specific heats |
| $\langle\cdot\rangle$, $\langle\langle\cdot\rangle\rangle$ | $\langle\cdot\rangle$ | domain average; domain and ensemble average |
| $q_i$ | $f_i$ | large-scale forcing per unit mass |
| $L$, $\lambda$, $\eta$, $Re_\lambda$ | $L$, $\lambda$, $\eta$, $Re_\lambda$ | as in the registry |
| $T$ (time) | — | eddy-turnover time $L/U$; same letter as the flux |
| $Q_i$ | $-\partial_j\tau_{ij}$ | target divergence $\partial_j\tau^S_{ij}$ of the admissible set |
| $\tau^*_{ij}$, $\tau^P_{ij}$ | — | divergence-free gauge tensor (§3), also the tensor to be projected (App. B); projected tensor |
| $\sigma(T)$ | $\sigma(\Pi)$ (local) | standard deviation of the flux; **collision** with the viscous stress $\sigma_{ij}$ |
| $\rho(\phi,\psi)$ | — | correlation coefficient (Eq. 6.5); **collision** with the density |
| $s$, $\kappa$ | — | skewness, flatness; $\kappa$ **collides** with the von Kármán constant |
| $H(T)$ | — | indicator, 1 for $T<0$ |
| $v^-$, $f^-$ | — | backscatter volume fraction and net backscatter (Eqs. 5.7–5.8) |

# Reference list

65 printed references in author–year (JFM) style, alphabetical, all merged into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author same-year works take suffixes:
Buzzicotti et al. 2018a/b; Meneveau 1994 and Meneveau & Lund 1994; Vela-Martín 2021 (JFM 913 R8)
and Vela-Martín & Jiménez 2021 (JFM 915 A36). Kraichnan (1967) is kept with its printed page range.
No DOIs are printed; no duplicate or unparseable item.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 4. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Anisotropic minimum-dissipation model](/methods/anisotropic-minimum-dissipation-model.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
