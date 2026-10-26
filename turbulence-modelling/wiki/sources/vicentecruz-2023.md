---
type: Source
title: "Vicente Cruz & Lamballais (2023) — Physical/numerical duality of explicit/implicit subgrid-scale modelling"
description: "Spectral comparison of constant-coefficient Smagorinsky LES and implicit LES by spectral vanishing viscosity in sixth-order compact schemes, on the Taylor–Green vortex at Re=40000 and pipe flow at Re_tau=1000–2000, with a priori and a posteriori spectral eddy viscosities."
resource: "doi:10.1080/14685248.2023.2215530"
source_kind: paper
authors: [Vicente Cruz R., Lamballais E.]
year: 2023
venue: "J. Turbul. 24:235-279"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Turbulence_Vicente_Physicalnumerical_duality_of_explicitimplicit_subgrid-scale.pdf"
tags: [les, implicit-les, sgs-model, numerical-dissipation, eddy-viscosity, a-priori-a-posteriori]
timestamp: 2026-10-25T13:42:00Z
---

# Summary

Vicente Cruz & Lamballais (2023) ask whether explicit subgrid-scale modelling still has a role once
[implicit LES](/definitions/implicit-les.md) works. They compute two flows with the sixth-order
compact finite-difference code Incompact3d/Xcompact3d, with skew-symmetric, kinetic-energy-conserving
convection ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)): the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=40000$ (reference
[DNS](/definitions/direct-numerical-simulation.md) on $5400^3$ nodes) and turbulent pipe flow at
$Re_\tau=1000$ and $2000$ on a Cartesian mesh with an immersed boundary. The implicit model is
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) built into the
second-derivative scheme of the viscous term, with the single parameter $\nu_0/\nu$. The explicit model
is the [Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.1$ (no
[dynamic procedure](/methods/dynamic-procedure.md)).

The analysis follows Lesieur's spectral framework for [LES](/definitions/large-eddy-simulation.md):
Kraichnan's [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) is estimated a priori from
filtered DNS and a posteriori from the LES. The findings are these. No-model LES thermalizes and turns
over-dissipative. Smagorinsky LES with $h=\Delta$ is dominated by numerical errors, and numerical
convergence needs $h=\Delta/5$, i.e. $C_s=0.5$ in the cell-based form. At converged numerics the
Smagorinsky "filter" is weak, and its spectral eddy viscosity bears no resemblance to the a priori
one. Implicit spectral vanishing viscosity gives better spectra and dissipation and reproduces the
cusp near $k_c$, but its eddy viscosity vanishes at small $k$, where the a priori one has a plateau
carrying up to 24% of the total dissipation; the authors call this "a fundamental limitation of any
implicit LES" (see [numerical dissipation](/properties/numerical-dissipation.md) and
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)). It also
produces a bottleneck bump. Adding
Smagorinsky restores the plateau and removes the bump, but does not improve the dissipation. In the
pipe at $\Delta x^+=\Delta y^+\approx9$, implicit spectral vanishing viscosity predicts $u_\tau$
within 1.8% without wall treatment, but fails at $\Delta x^+=18$, so it cannot serve alone as
[wall-modelled LES](/methods/wall-modelled-les.md). The authors conclude that explicit models can
be read as an ersatz of regularization, the reverse of the usual reading.

# Version read

HAL author manuscript hal-04451824v1 (deposited 15 March 2025; LaTeX layout "Compiled May 10, 2023"),
not the journal typeset. Its 46 PDF pages are the HAL cover plus manuscript pages 1–45, so manuscript
page $n$ is PDF page $n+1$. Title and authors match the published version; the metadata above are
those of the published version (Crossref), and the HAL cover gives the same journal citation. Section,
equation, figure and page numbers on this page are those of the manuscript.

# Key claims

1. Convection in skew-symmetric form makes spatial differentiation kinetic-energy conserving up to time-integration error. In truncated-Euler runs over $0\le t\le20$ the deviation from $K=0.125$ is below 1%, and the energy loss scales about as $\Delta t^3$ (§3, §6.2). **Shown**.
2. Truncated-Euler solutions evolve to a thermalized white-noise state with $\bar E(k)\sim k^2$; transient small-scale thermalization damps the large scales (§6.2, Fig. 4). **Shown**.
3. No-model LES thermalizes on more than 80% of the wavenumbers at the low resolution, with pile-up near $k_c$ from $t=5$, and greatly overestimates the total dissipation during breakdown: "a subdissipative operator leads eventually to an overdissipative behaviour" (§6.2, Figs. 6–7). **Shown**.
4. The Smagorinsky model with $h=\Delta$ cannot control the pile-up near $k_c$ and overestimates the total dissipation. The authors attribute this to the interaction of differentiation errors with the model, not to the model itself; reducing $C_s$ would worsen it (§6.3, Figs. 7–8). **Shown** (attribution **Stated**).
5. At fixed $\Delta=\pi/108$, Smagorinsky LES reaches numerical convergence through breakdown only for $h=\Delta/5$ ($k_c=540$); $h=\Delta/2.5$ ($k_c=270$) still thermalizes in early transition. The cost factors are $2.5^4\approx39$ and $5^4=625$ (§6.3, Fig. 9). **Shown**.
6. Since $h=\Delta/5$ in $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$ equals $C_s=0.5$ in the cell-based form $\nu_t=(C_sh)^2\lvert\bar S\rvert$, numerical convergence requires $C_s=0.5$ when the filter width is the cell size; "such a high value is never used". At constant cost, $\Delta=2.5h$ ($C_s=0.25$) gives a better total dissipation than $\Delta=h$, and "$C_s=0.25$ and even $C_s=0.5$ is highly preferable to the common choice $C_s=0.1$" (§6.3, Fig. 12). **Shown**.
7. At numerical convergence the effective Smagorinsky transfer function satisfies $\hat G_{\mathrm{eff}}(k_\Delta)\approx0.6$ and decays slowly beyond $k_\Delta$: a weak "Smagorinsky filter" with poor ability to reduce degrees of freedom. It matches the Gaussian $\hat G(k)=\exp(-k^2\Delta^2/24)$ only at low $k$ (§6.3, Fig. 10, Eq. 49). **Shown**.
8. Proposed criterion: $\hat G_{\mathrm{eff}}(k_c)\lesssim0.1$ as a minimum condition to approach numerical convergence; the standard condition gives $\hat G_{\mathrm{eff}}(k_c)\approx1$ (§6.3). **Shown** (for this flow).
9. The a posteriori spectral eddy viscosity of the Smagorinsky model has "no common features" with the a priori one: same order at low $k$ but smaller, weakly $k$-dependent, and vanishing near $k_c$ where the a priori one rises. The drop scales on $k_c$, not $k_\Delta$, a signature of numerical error (§6.3, Fig. 11). **Shown**.
10. Implicit spectral vanishing viscosity damps $E(k)$ for $k_c/2\lesssim k\lesssim k_c$, prevents thermalization, reduces the spectral deviation for $k\lesssim k_c/2$ relative to Smagorinsky, and captures the dissipation peak during breakdown (§6.4, Figs. 13–14). **Shown**.
11. Implicit-SVV LES at fixed $\Delta$ is numerically converged in the standard condition: $\Delta=h$ and $\Delta=2.5h$ give "virtually identical results" (not shown) at $Re=40000$ (§6.4). **Shown** (data not displayed).
12. The effective implicit-SVV filter is approximated by the super-Gaussian $\hat G(k)=\exp(-k^6\Delta^6/256)$, but shows a bump with its top near $k\approx k_c/4$: a bottleneck (soft pile-up for $k<k_c/2$), "the main drawback of present implicit modelling" (§6.4, Fig. 15, Eq. 50). **Shown**.
13. The implicit-SVV spectral eddy viscosity reproduces the a priori cusp near $k_c$ but rises from lower $k$, with higher values for $k\gtrsim k_c/2$; the a priori cusp for $k\gtrsim k_c/2$ is sensitive to the constant 256 of Eq. (50) (§6.4, Fig. 16). **Shown**.
14. The anisotropies of the kinetic energy and of the implicit-SVV dissipation are anticorrelated, so the effective eddy viscosity is lower than the estimate from the uncorrelated assumption where anisotropy matters (§6.4). **Shown**.
15. The a priori $\nu_t(k\mid k_c)$ has a non-zero plateau as $k\to0$, about 12, 2 and 0.2 times $\nu$ at the low, high and very high resolutions ($t=10$); implicit SVV vanishes there, "a fundamental limitation of any implicit LES" (§6.4, Figs. 16–17). **Shown** (generalization to any implicit LES **Stated**).
16. A priori, the subgrid dissipation at $k<k_c/4$ missed by implicit LES is up to 24%, 16% and 6% of the total at the three resolutions; the plateau "cannot be ignored, making somewhat inconsistent the concept of implicit LES except when the mesh is close to DNS" (§6.4, Fig. 18, Eqs. 51–54). **Shown**.
17. The a priori subgrid dissipation is up to 77% (high) and 93% (low resolution) of the total, while the LES captures more than 97% and 92% of the kinetic energy (§6.1). **Shown**.
18. The plateau reflects non-local triad interactions and the cusp local ones. With a sharp cutoff, the a priori $\nu_t(k\mid k_c)$ at $t=10$ agrees with the Chollet–Lesieur model $\nu_t(k\mid k_c)=0.267[1+34.5\exp(-3.03k_c/k)]\sqrt{E(k_c)/k_c}$ in plateau and cutoff value. At $t=15$ the a priori plateau is more than twice lower, attributed to $Re_\lambda\approx389$ against $\approx493$ (§6.4, Fig. 19, Eq. 55). **Shown**.
19. The cusp produced by a super-Gaussian (non-idempotent) filter is more than an order of magnitude higher than with a sharp cutoff, so "there is no reason to design SGS modelling to match quantitatively this specific cusp when a different filtering is expected" (§6.4, Fig. 19). **Shown** + **Stated**.
20. Mixed Smagorinsky + implicit SVV with $C_s=0.1$ and $0.18$ reproduces the cusp and gives a non-zero small-$k$ eddy viscosity; $C_s=0.18$ matches the a priori plateau better at $t=10$; the bottleneck bump is reduced ($C_s=0.1$) or removed ($C_s=0.18$) (§6.5, Figs. 20–21). **Shown**.
21. The mixed model does not improve the total dissipation over pure implicit SVV. As $C_s$ goes from 0.18 to 0, implicit SVV compensates the missing explicit dissipation automatically, which the authors relate to Oran & Boris's "convenient conspiracy" (§6.5, Fig. 22). **Shown**.
22. The anisotropy-aware (shell-averaged) Pao-like closure gives $\nu_0/\nu=181$ and $700$ for $k_d/k_c=10$ and $25$, against $92$ and $355$ from the isotropic version (§5.3). **Derived**.
23. Implicit-SVV numerical dissipation is strongly anisotropic, largest along the mesh axes and smallest in oblique directions; the authors argue this is an asset because convective differentiation errors are also largest along the axes (§5.3, Fig. 1). **Shown** (illustration) + **Stated** (argument).
24. Pipe DNS at $Re_\tau=1000$ with uniform $\Delta x^+=\Delta y^+\approx3$ and an immersed boundary agrees with El Khoury et al. in mean velocity and Reynolds stresses; the authors suggest that one wall unit of near-wall spacing "may be somewhat over-demanding" (§7.1, Fig. 24). **Shown** + **Stated**.
25. Pipe LES at $\Delta x^+=\Delta y^+\approx9$ ($256\times256\times640$, cost reduction $3^4=81$): no model overestimates $u_\tau$ by 15.3%, Smagorinsky with van Driest damping by 9.6%, implicit SVV ($\nu_0/\nu=234$) underestimates it by 1.8%, with realistic mean and normal-stress profiles (§7.2–7.4, Figs. 25–27). **Shown**.
26. In the pipe LES the Smagorinsky eddy viscosity reaches instantaneous maxima of about $3\nu$ and a mean of about $0.3\nu$ near the wall (§7.3). **Shown**.
27. At $Re_\tau=2000$ the same mesh ($\Delta x^+=18$, $\nu_0/\nu=756$) underestimates $u_\tau$ by more than 12% ("implicit SVV cannot be used alone in the context of WMLES"); the doubled mesh ($\Delta x^+=9$) underestimates it by about 1.9% (§7.4, Fig. 28). **Shown**.
28. For $\Delta/h_{\mathrm{DNS}}\lesssim5$ the usefulness of explicit SGS modelling and wall adaptation "cannot be evidenced"; for stronger reductions the bottleneck and the missing non-local transfer of implicit modelling suggest an explicit model dedicated to non-local triad interactions (§8). **Stated**.

# Printed slips

- Eq. (23), the a priori estimator, is printed without a leading minus sign. *(Compiler check, not in the sources: from Eqs. 18, 20 and 21 as printed, $-T_>/\bar\varepsilon$ equals minus the printed ratio, since the factors $-4\pi k^2$ cancel.)*
- Eq. (38) lacks the factor $4\pi k^2$ in its numerator. *(Compiler check, not in the sources: with Eq. 12 for $E$ and Eq. 13 with Eq. 37 for $\varepsilon$, the ratio $\varepsilon/(2\nu k^2E)-1$ carries $4\pi k^2\langle k''\hat u_i^*\hat u_i\rangle$ in the numerator.)*
- Eq. (39), $\langle\hat u_i^*\hat L_i(\hat u_i)\rangle\approx-\langle k''\rangle\langle\hat u_i^*\hat u_i\rangle$, drops the factor $\nu$ present in Eq. (37).
- Fig. 24 legend reads "DNS [26]" while the text and caption cite [29] (El Khoury et al.).
- Fig. 16 legend labels the theoretical curve "from (40)" while the caption and text refer to (42).
- The one-dimensional kernel is written $\nu_s''(k_i)$ in Eq. (30) and $\nu''(k)$ in Eq. (41); §6.4 writes "$T(k_c,t)\lesssim0.1$" with the transfer symbol $T$ for the transfer function $T_f$.
- Spelling: "betweeen" (§5.2), "refereed" for "referred" (§1), "HR et VHR" (§6.4).
- Reference list: [15], [16] print the journal as "Physical Review F"; [26] has a truncated title ("turbulence deca"); [28] prints "T.J.R. Hughes and L. Mazzei K.E. Jansen"; [29] "P. F. Fischer F"; [18], [37], [43] lack pages and [54] a volume.

# Notation map

| Vicente Cruz & Lamballais (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar{(\cdot)}$ | $\bar\phi$ | LES filter at separation scale $\Delta$ |
| $\Delta$ | $\Delta$ | filter width, a continuous parameter independent of the mesh |
| $\Delta x$ | $h$ | cubic cell size, $k_c=\pi/h$ |
| $\hat{(\cdot)}$ | $\phi_{\boldsymbol k}$ | **collision:** Fourier coefficient, not the test filter |
| $\langle\cdot\rangle$ | — | **collision:** average over spherical shells in Fourier space; in the pipe section a statistical average as in the registry |
| $\tau_{ij}$ | $\tau_{ij}$ | model $\tau_{ij}=-2\nu_t\bar S_{ij}+\tfrac13\tau_{kk}\delta_{ij}$ (Eq. 24), consistent with the positive-trace convention |
| $\lvert\bar S\rvert=\sqrt{2\bar S_{ij}\bar S_{ij}}$ | $\lvert\bar S\rvert$ | with the factor two |
| $C_s$ | $C_s$ | 0.1; 0.18 from Lilly's value with $C_k=1.4$; equivalent 0.25, 0.5 |
| $\nu_s(k,t)$ | $\nu_t(k\mid k_c)$ | Kraichnan's spectral eddy viscosity, $-\nu T_>/\bar\varepsilon$ (Eq. 21); one symbol for the a priori, a posteriori and model (Eq. 55) forms |
| $E$, $\bar E$ | $E(k)$ | spectrum with the shell factor $4\pi k^2$; $\bar E$ resolved spectrum |
| $T$, $T_<$, $T_>$ | — | transfer spectra; **collision** with the temperature $T$ |
| $E_k$ | $K$ | total kinetic energy (spectral page convention) |
| $k_c$, $k_\Delta$, $k_d$ | $k_c$ | mesh cutoff; filter wavenumber and DNS-mesh cutoff are local |
| $T_f(k,t)$ | $\hat G_{\mathrm{eff}}(k)$ (local) | effective transfer function $\sqrt{E_{\mathrm{LES}}/E_{\mathrm{DNS}}}$; Eqs. (49)–(50) are model $\hat G(k)$ |
| $\nu_0$, $k_i''$, $k''$ | — | numerical viscosity at $k_c$; modified square wavenumber |
| $u_z$, $\langle u'_zu'_z\rangle$ | $u$, $R_{xx}$ | pipe axis is $z$ in the source; streamwise normal stress |
| $\Delta x^+=\Delta y^+$ | — | cross-section spacings of the Cartesian pipe mesh, in wall units |
| $P_k$ | $P_k$ | production of $k$ (premultiplied in the pipe figures) |

# Reference list

72 printed references in numbered style, alphabetical by first author, all merged into the
[bibliography](/bibliography.md) with `citedby` this slug. Same-author same-year pairs take suffixes
in printed order (Domaradzki 2021, [15]/[16]; Lamballais 2019, [35]/[38]). Ref. [27] is an edited
volume entered under its editors; ref. [3] is the Xcompact3d software paper. Partial items are listed
under Printed slips; none is unparseable and no printed duplicate was found.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2–3. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Discretization-consistent closure](/definitions/discretization-consistent-closure.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
