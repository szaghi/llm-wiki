---
type: Source
title: "Kokkinakis & Drikakis (2025) — Advancing fluid flow simulation through low-dissipation shock and vortex-resolving methods"
description: "Proposes WENO5-H++, a fifth-order WENO whose nonlinear weights combine the WENO-D modifier, WENO-IM and WENO-MZ mappings and the WENO-ZPM extra term, and compares it with four other WENO5 variants on shock tests, double-vortex pairing and the Taylor–Green vortex at Re 1600."
resource: "doi:10.1063/5.0303027"
source_kind: paper
authors: [Kokkinakis I.W., Drikakis D.]
year: 2025
venue: "Phys. Fluids 37:116101"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Physics_of_Fluids_Kokkinakis_Advancing_fluid_flow_simulation_through_low-dissipation_shoc.pdf"
tags: [weno, shock-capturing, numerical-dissipation, implicit-les, taylor-green-vortex, compressible]
timestamp: 2026-10-29T05:09:00Z
---

# Summary

Kokkinakis & Drikakis (2025) propose WENO-H++ (fifth-order WENO5-H++), a
[WENO](/methods/weno-scheme.md) reconstruction whose nonlinear weights
merge several published improvements in one formula: the WENO-D modifier
$\Phi$ (Wang et al. 2019), the WENO-IM mapping of the smoothness
indicators inside the Z-type term (Hu 2021), a WENO-MZ weighting function
(Tang & Li 2024) that sets the adaptive weight of the WENO-ZPM extra term
(Luo & Wu 2021, a corrected WENO-Z+). The authors stress that with $n$
enhancements there are $n!$ orderings and the order matters, and that
lower dissipation exposes dispersion errors; they raise the
smoothness-indicator power to 3 and set the regularization to
$10\,\mathrm{epsilon}(1.0\mathrm D0)\simeq2.22\times10^{-15}$. The scheme
runs in a Godunov finite-volume solver (HLLC, primitive-variable
dimension-by-dimension reconstruction, five-stage fourth-order SSP
Runge–Kutta, fourth-order central viscous terms); the code is not named
in this paper (the [CNS3D](/software/cns3d.md) page lists the authors'
solver).

WENO5-H++ is compared with WENO5-JS, WENO5-Z+, WENO5-ZM and WENO5-MD on
step advection, the Shu–Osher and Titarev–Toro problems, double-Mach
reflection, a 2D double-vortex-pairing problem (a two-mode
[temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md))
and the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
$Re=1600$ on $96^3$ against the $512^3$
[DNS](/definitions/direct-numerical-simulation.md) of Dairay et al. (sixth-order
[compact](/methods/compact-finite-difference-scheme.md)). The viscous
cases carry no turbulence model, and the paper does not use the term
[implicit LES](/definitions/implicit-les.md) for them. [Numerical dissipation](/properties/numerical-dissipation.md)
is measured as the residual of the kinetic-energy balance (viscous and
[pressure-dilatation](/definitions/pressure-dilatation.md) parts removed),
and in the TGV as a numerical viscosity from $\varepsilon=2\nu\mathcal Z$.
WENO5-H++ has the lowest advection errors, the lowest accumulated
dissipation in vortex pairing (0.822 of WENO5-JS), the highest TGV
enstrophy peak and a numerical viscosity the text puts below that of
WENO11-JS, at 30–40% extra cost over WENO5-JS. The Stokes-hypothesis
coefficient is named "second viscosity" in §II A and
"[bulk viscosity](/definitions/bulk-viscosity.md)" in §III F. Shock–turbulent
[boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
is named as a target application only. Evidence is numerical; no
order-of-accuracy or stability analysis is given.

# Version read

Version of record (AIP; submitted 18 September 2025, accepted 15 October
2025, published online 3 November 2025), 22 PDF pages (AIP cover plus
article pages 116101-1 to -21), all read; the equations were transcribed
from the page images because the text layer garbles them. Page 1 matches
the metadata. Numbering on this page is that of the version read.

# Key claims

Page-local symbols: $p_{\mathrm W}$ the power of the smoothness-indicator
ratio (the paper's $p$; not the pressure); $\Phi$ the WENO-D modifier;
$\varepsilon_p$ the pressure-dilatation part of the kinetic-energy
balance.

1. WENO-H++ combines WENO-M-type (WENO-IM, WENO-MZ) and WENO-Z-type (WENO-ZPM) enhancements with the WENO-D modifier, giving "very low numerical dissipation". §II C, Eqs. (11)–(12). **Stated** (construction); dissipation **Shown** in §III.
2. Combining $n$ WENO enhancements gives $n!$ configurations, and the order of combination strongly changes the result (some orderings too dissipative, others too dispersive); "there is no established framework that can fully explain these phenomena". §II C. **Stated**
3. With the literature parameters the hybrid showed "significant dispersion errors" in preliminary trials; $p_{\mathrm W}=3$ was adopted instead of the value 2 that §II B uses "unless otherwise stated", "necessary for stability purposes in several of the test cases", though $p_{\mathrm W}=2$ was better in some others; all results use $p_{\mathrm W}=3$. §II C. **Stated** (trials not shown)
4. $p_{\mathrm W}=r$ ($r=3$ at fifth order) follows Gerolymos et al.; the regularization $10\,\mathrm{epsilon}(1.0\mathrm D0)\approx2.22\times10^{-15}$; "the above two measures help prevent the growth of numerical noise arising from excessive dispersion errors". §II C. **Stated**
5. Lower numerical dissipation makes dispersion errors noticeable, so further hybridization (e.g. IMWENO-P indicators) was not pursued. §II C. **Stated**
6. Step advection (200 cells, $t=2$): WENO5-H++ has the lowest errors, $L^1=0.007$, $L^2=0.040$, $L^\infty=0.304$, against JS 0.012/0.052/0.386, Z+ 0.010/0.046/0.352, ZM 0.008/0.042/0.338, MD 0.017/0.070/0.510. §III A, Table I. **Shown**
7. WENO5-MD (with $\Phi$ built from $\sqrt{\mathrm{IS}_{\mathrm G}}$) gives the sharpest upper edge but overshoots and oscillates, so its errors exceed WENO5-JS; the alternative modifier Eq. (A14) reduces but does not remove the oscillations and diffuses the discontinuity. §III A, Fig. 1, Table I. **Shown**
8. WENO5-H++ reduces the $L^\infty$ error "by almost ~30%" relative to WENO5-JS, the second-best WENO5-ZM by "~14%". §III A. **Shown** (see Printed slips)
9. Shu–Osher (250 cells, $t=1.8$, reference 4000 cells): every enhancement improves on WENO5-JS; WENO5-MD and WENO5-H++ agree best; WENO5-MD is best at the shock ($x\simeq2.4$), WENO5-H++ in the sinusoidal density field. §III B, Fig. 2. **Shown**
10. Titarev–Toro (900 cells, $t=5$): all fifth-order WENO methods "to the best knowledge of the authors" damp the high-frequency waveform as $x\to-1.8$; WENO5-H++ keeps a constant amplitude slightly below the reference; WENO5-Z+ also does, except in the last two to three cycles. §III C, Fig. 3. **Shown**
11. Double-Mach reflection ($t=0.2$, rotated HLLC, reference $4000\times1000$ with fifth-order MUSCL): WENO-Z+ gives only modest gains, as Acker et al. noted, while WENO-H++ resolves fine structures along the slip line. §III D, Fig. 4. **Shown**
12. Double-vortex pairing ($64^2$, reference $256^2$, $t=6$ s): every variant sharpens the passive scalar relative to WENO5-JS; WENO5-H++ agrees best with the reference. §III E 1, Fig. 5. **Shown**
13. Normalized inner vortex lengths: JS 0.373, Z+ 0.534, ZM 0.609, MD 0.679, H++ 0.745; outer: 0.496, 0.586, 0.674, 0.895, 0.868; the merged-vortex rotation angle is the same for all. §III E 2, Table II, Fig. 6. **Shown**
14. Accumulated numerical dissipation $\int_0^T\varepsilon_{\mathrm{num}}\,dt$ ($T=6$ s), normalized by WENO5-JS: Z+ 0.942, ZM 0.888, MD 0.829, H++ 0.822; the initial velocity jump is "the leading contributing factor". §III E 3, Table III, Eqs. (22)–(28). **Shown**
15. On finer grids the differences between WENO5 variants shrink, and gains from enhancements are smaller for higher-order schemes such as WENO11-JS. §III E 3. **Stated** (not shown)
16. TGV ($Re=1600$, $M_0=0.1$, $96^3$): WENO5-MD and WENO5-H++ resolve more vortical structures than WENO11-JS on the same mesh at $t=9$ and $15$; WENO5-Z+ and ZM perform on a par with WENO11-JS. §III F, Figs. 7–8. **Shown** (isosurfaces of $Q_A$)
17. TGV kinetic energy decays earliest with WENO5-JS; WENO5-H++ is closest to the Dairay et al. DNS "for most of the simulation duration". §III F, Fig. 9. **Shown**
18. WENO5-H++ gives the largest enstrophy peak and the lowest numerical viscosity $\nu_{\mathrm{num}}/\nu=\varepsilon/(2\mathcal Z\nu)-1$, followed by WENO5-MD; both lie below WENO11-JS; all schemes underestimate enstrophy on this grid. §III F, Eq. (35), Fig. 10. **Shown** (the WENO11-JS comparison is stated in the text; Fig. 10 does not plot WENO11-JS)
19. In the TGV, kinetic energy and $\varepsilon$ change little between schemes, while enstrophy and numerical viscosity improve by 25.5% and 44.5% with WENO5-H++. §III G. **Shown** (the reference scheme of the percentages is not stated)
20. WENO5-H++ costs about 30–40% more than WENO5-JS, depending on the Riemann solver and on viscous terms; WENO11-JS costs "over twice (100%)" WENO5-JS; the memory overhead is one extra vector of size 3. §III G. **Stated** (no timing table or hardware)
21. The extra cost is "primarily justified for inviscid flows or under-resolved viscous flows"; on a fine enough mesh even WENO5-JS resolves the flow. §III G. **Stated**
22. Other variants (WENO5-Z, WENO5-M, WENO5-AIM, …) were also run; WENO5-AIM beat all but WENO5-H++ in the double-Mach reflection; results omitted. §III F. **Stated**
23. Extension to unstructured meshes "may seem straightforward" since the weight computation is the same on structured and unstructured meshes, but unstructured WENO uses different linear weights and element-dependent dissipation and dispersion, so the parameters would need recalibration. §III G. **Stated**
24. The WENO-Z+ parameter $\lambda^{Z+}=\Delta x^{2/3}$ of Acker et al. is confirmed optimal by the authors' tests. Appendix. **Stated**

# Printed slips

- **§III A vs Table I:** "reduces the $L^\infty$ error by almost ~30%, while the second-best WENO5-ZM method does so by ~14%"; the conclusions repeat "nearly 30%". *(Compiler check, not in the sources: from Table I the reductions relative to WENO5-JS are 21.2% and 12.4%; dividing the differences by the new errors gives 27.0% and 14.2%. The vortex-pairing percentages of §III E 3 are relative to WENO5-JS.)*
- **Abstract vs Table III:** "reduces numerical dissipation by nearly 20%"; the conclusions print both "nearly 20%" and "~18%"; Table III gives 0.822. *(Compiler check, not in the sources: $1-0.822=17.8\%$.)*
- **Table II vs text:** the WENO5-H++ inner length is "more than twice that of the original WENO5-JS"; Table II gives 0.745 and 0.373. *(Compiler check, not in the sources: ratio 1.997.)*
- **Double-Mach reflection grid:** §III D prints $1000\times250$ cells, the Fig. 4 caption $1000\times240$.
- **Eq. (15), Shu–Osher data:** the post-shock state is printed for "$-5\le x<4$" and the perturbed state for "$4\le x\le5$"; the text places the shock at $x\simeq2.4$ at $t=1.8$. *(Compiler check, not in the sources: the jump condition of the paper's mass equation, Eq. 1, with the printed post-shock state and the unperturbed density 1 ahead gives a shock speed $(27/7)(4\sqrt{35}/9)/(20/7)=3.549$; starting from $x=-4$ the shock reaches 2.39 at $t=1.8$, from $x=4$ it would leave the domain.)*
- **Eq. (14) vs §III A text:** Eq. (14) sets $f_0=0$ on $[-1,0)$ and 1 on $[0,1]$; the text describes the "upper left side … [$f(x<0,t=2)$]" and the "lower right side [$f(x>0,t=2)$]". Eq. (13) is printed "$f_t+c\,f_x$" without "$=0$".
- **Eq. (12):** $z=(1+\tilde\Psi_{\min})/\sum_{l=0}^{r-1}d_k(1+\tilde\Psi_k)$ sums over $l$ a summand indexed $k$; $\tilde\Psi_{\min}$ is not defined.
- **Eq. (12) vs Eq. (A18):** the WENO-MZ weighting is printed in (A18) with $\gamma_k=(\tau/(\mathrm{IS}_k+\epsilon))^{p_{\mathrm W}}$ and $\gamma_k^{p_{\mathrm W}}$ inside the function, and in (12) with $\gamma_k=(\tau/(\mathrm{IS}_k+\epsilon))^{\tilde p}$ and $\gamma_k$ inside: the power is applied twice in one form and once in the other.
- **Eq. (A3):** the text says $A=1$, $K=2$ "results in the original mapping function", while the numerator is printed $(\omega_k+d_k)^{K+1}A$. *(Compiler check, not in the sources: with $(\omega_k-d_k)^{K+1}$, $A=1$, $K=2$, Eq. (A3) equals the paper's own WENO-M mapping Eq. (A2); with the printed plus sign it does not.)*
- **Eq. (A9):** the left side is printed "$(\beta_k)=\beta+\dots$" without the function name $g$.
- **Eq. (A10):** $\beta^Z_k$ is defined and not used.
- **Conclusions vs §III C:** "WENO5-Z distinguished itself and performed reasonably well" on the Titarev–Toro problem, where §III C names WENO5-Z+ and WENO5-Z is not plotted.
- **Sign of $\varepsilon$:** Eq. (22) $\varepsilon=-\mathrm de_k/\mathrm dt$; §III F "$\varepsilon=\mathrm dE_k/\mathrm dt$".
- **Eq. (23):** called "volumetric-averaged" but printed without a $1/V$ factor.
- **Vortex-pairing Reynolds number:** "$Re_\infty\simeq1600$" on $\Delta U$, $L$, $\nu_\infty$, with $L$ not given numerically.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\beta_k$ | $\mathrm{IS}_k$ | smoothness indicator of stencil $k$ |
| $a_k$, $\omega_k$, $d_k$ | $a_k$, $\mathsf w_k$, $d_k$ | unnormalized, normalized and linear weights; superscripts JS, Z, Z+, ZPM, D, MZ, MD, ZM, H++ name the variant |
| $r$ | $r$ | candidate stencils; order $2r-1$ |
| $p$ | $p_{\mathrm W}$ (page-local) | power of the indicator ratio; **collision** with the pressure $p$ |
| $\varepsilon$ (Eq. 8, 11–12) | $\epsilon$ | regularization: $10^{-41}$ in Eq. (8), $\approx2.22\times10^{-15}$ in WENO-H++; **collision** with the dissipation rate $\varepsilon$ |
| $\tau$, $\tau_5$ | $\mathrm{IS}_{\mathrm G}$ | global smoothness indicator $\lvert\mathrm{IS}_0-\mathrm{IS}_2\rvert$, as on [WENO schemes](/methods/weno-scheme.md) |
| $\Phi$, $\varphi$ | $\Phi$ (page-local) | WENO-D modifier $\min(1,\varphi)$ |
| $\Psi_k$, $\tilde\Psi_k$, $\gamma_k$, $g(\beta_k)$, $\lambda$, $\tilde\lambda$, $\hat\lambda$, $z$, $\eta_k$, $\tilde p$ | as printed (page-local) | weight-construction auxiliaries of Eq. (12); $\lambda$ is not the Taylor microscale |
| $\lambda=-2\mu/3$ | Stokes-hypothesis second coefficient | **collision** with the weight $\lambda$ |
| $\varepsilon$, $\varepsilon_\nu$, $\varepsilon_p$, $\varepsilon_n$ | $\varepsilon$, $\varepsilon_\nu$, $\varepsilon_p$, $\varepsilon_{\mathrm{num}}$ | total, viscous, pressure-dilatation and numerical dissipation; $\varepsilon_{\mathrm{num}}$ the residual |
| $\zeta$ | $\mathcal Z$ | volume-averaged enstrophy $\langle\omega_i\omega_i/2\rangle$ |
| $\nu_l$, $\nu_n$, $\bar\nu_n$ | $\nu$, $\nu_{\mathrm{num}}$, $\nu_{\mathrm{num}}/\nu$ | |
| $Q=\frac12(\lVert\Omega\rVert^2-\lVert\mathsf S\rVert^2)$ | $Q_A$ | second invariant of the velocity-gradient tensor |
| $\mathsf S$, $\Omega$ | $S_{ij}$, $\Omega_{ij}$ | |
| $\bar{\bar\tau}$ | $\sigma_{ij}$ | viscous stress |
| $\phi$ | passive scalar | |
| $V_0$, $L$, $M_0$, $t_c$ | TGV velocity, length, Mach number, $L/V_0$ | |

# Reference list

81 printed references, numbered AIP style, no DOIs printed, all parsed.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [50] (Kokkinakis et al. 2025, AIAA J. 63:1262,
aeroelastic panel SBLI) falls on this page's own key and ref. [49]
(Kokkinakis & Drikakis 2023, internal explosions) on the key of
[Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md); both are different works and are keyed `kokkinakis-2025-c` and `kokkinakis-2023-b`, as are four further works whose natural keys belong to different bundle sources (Tang & Li 2024, Xu et al. 2023, Li et al. 2021, Jiang et al. 2025: `tang-2024-b`, `xu-2023-f`, `li-2021-i`, `jiang-2025-c`). Three items are bundle
sources: [17] [Wang et al. (2024b)](/sources/wang-2024-i.md), [57]
[Luo & Wu (2021)](/sources/luo-2021-b.md) and [72]
[Chapelier et al. (2024)](/sources/chapelier-2024.md). Ref. [15] (Deng
2011, AIAA conference paper) prints no pages; no item is printed twice.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Temporally developing mixing layer](/benchmarks/temporal-mixing-layer.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Vortex identification criteria](/definitions/vortex-identification-criterion.md)
- [Compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
