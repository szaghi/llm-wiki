---
type: Source
title: "Wang (2024) — On the implicit Large Eddy Simulation of turbomachinery flows using the Flux Reconstruction method"
description: "Introduces the flux-reconstruction implicit-LES solver ATHOS with a local modal filter gated by the Persson–Peraire indicator, gives a threshold range for it, and compares it with an entropy filter and HLLC against Roe fluxes on the Taylor–Green vortex, the T106C cascade and the LS89 vane."
resource: "doi:10.1016/j.compfluid.2024.106422"
source_kind: paper
authors: [Wang F.]
year: 2024
venue: "Comput. Fluids 284:106422"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Computers_amp_Fluids_Wang_On_the_implicit_Large_Eddy_Simulation_of_turbomachinery_flow.pdf"
tags: [implicit-les, flux-reconstruction, dg, numerical-dissipation, turbomachinery, filtering]
timestamp: 2026-10-26T10:27:00Z
---

# Summary

Wang (2024) presents ATHOS, an in-house C++ flux-reconstruction solver for
[implicit LES](/definitions/implicit-les.md) of turbomachinery flows. The
correction functions recover collocated nodal
[DG](/methods/discontinuous-galerkin-spectral-element-method.md) on
Gauss–Lobatto–Legendre points, viscous fluxes are LDG with zero penalty, and
time integration is an explicit low-storage five-stage fourth-order
Runge–Kutta scheme. No subgrid model is used. Two questions are studied.
First, non-linear stabilization by a *local modal filter* (LMF): the
exponential modal filter is applied only in elements where the
Persson–Peraire smoothness indicator $s_e$ exceeds a threshold $s_0$. The
Li–Wang thresholds cannot be used directly; a range $[s_0-\kappa_s:s_0]$ with
$\kappa_s\approx1$ works, summarized as $s_0\in[-(N+2):-(N+1)]$. The LMF is
compared with the positivity-preserving entropy filter of Dzanic and
Witherden, which stabilizes without tuning but is more dissipative at high
frequency and about 15% more expensive per iteration. Second, Riemann
solvers: Rusanov is used on no-slip walls; on interior faces HLLC is more
robust than Roe, but both give nearly the same mean flow when stable. Both
the filter and the interface flux add to the
[numerical dissipation](/properties/numerical-dissipation.md) that implicit
LES relies on; the author links solution filtering to
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) and
leaves the flux-reconstruction analogue to future work.

Evidence: on the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
at $Re=1600$ and 5000 the LMF leaves the dissipation rate and spectra of the
unfiltered run unchanged (5.5% overhead). On the T106C low-pressure
[turbine cascade](/benchmarks/turbine-cascade.md) (exit $Re=8\times10^4$,
with a [laminar separation bubble](/definitions/laminar-separation-bubble.md))
both fluxes match the measured isentropic Mach number. On the VKI LS89 vane
(exit $Re=1.13\times10^6$) a study of $N$ and spanwise resolution brings the
heat-transfer coefficient towards experiment and finds a spanwise spacing
$\Delta z^+\approx45$–60 sufficient for the mean heat transfer, a point for
the [grid requirements](/results/les-grid-point-requirements.md) of
high-order implicit LES.

# Version read

arXiv preprint 2405.17288v2 (footer "Preprint submitted to computer and
fluids, July 26, 2024"), the author's revised manuscript, not the typeset
version of record. 49 PDF pages (a graphical abstract and a highlights page
precede printed pages 1–47), all read; printed pages 5–9 and 14 were checked
visually. Page numbers cited are the printed ones. Title and author match
the published identity; the preprint prints the title in title case. The
acknowledgements say "The authors" for a single-author paper.

# Key claims

1. HLLC is more robust than Roe for implicit LES of turbomachinery flows with flux reconstruction, but both give very similar results when stable solutions are obtained (Abstract; §4.3.2; Table 7; §5). **Shown**
2. On no-slip walls the convective flux is computed from ghost values with a Riemann solver (after Mengaldo et al.); among Rusanov, Roe and HLLC the most dissipative, Rusanov, is the most robust at the wall, and the hybrid Rusanov-at-wall with Roe or HLLC in the interior is used throughout (§2.4.2). **Stated** (no figure)
3. LMF: the modal filter (Eqs. 17–18) is applied only in elements with $s_e\ge s_0$ (Algorithm 1, Appendix A), $s_e$ the Persson–Peraire indicator computed on density (Eq. 19) (§2.3). **Stated** (the paper's contribution)
4. The Li–Wang thresholds (Table 2a, $\kappa_s=4$, $C_0=4$) cannot be used directly: $s_0-\kappa_s$ filters too many elements (excessive dissipation), $s_0+\kappa_s$ does not stabilize; a value around $s_0$ balances accuracy and robustness, and $[s_0-\kappa_s:s_0]$ with $\kappa_s\approx1$ performs well (Table 2b: $N=2$, $[-3.7,-2.7]$; $N=3$, $[-5.3,-4.3]$) (§2.3, pp. 10–11). **Shown** (by the later cases)
5. The conclusions summarize the range as $s_0\in[-(N+2):-(N+1)]$ for $N=2,3$ (§5). **Stated**
6. A large negative $s_0$ (e.g. $-16$) filters every element; in T106C the smooth upstream flow has $s_e<-7$ for $N=2$ and 3, so $s_0<-7$ filters essentially all cells (§4.2 p. 18; §4.4.1, Fig. 18). **Shown**
7. One $s_0$ can be kept during the $N=0\to3$ ramp-up, since the value for the higher degree is conservative for the lower ones (§4.4.1). **Stated**
8. Taylor–Green vortex at $Re=1600$ and 5000, Mach 0.1, $64^3$ hexahedra, $N=3$, HLLC, LMF with $s_0=-4$: no noticeable difference in the kinetic-energy dissipation rate (Fig. 2) or in the spectra at $t=9$ and $t=14$ (Fig. 3) between the LMF and the unfiltered run, both in excellent agreement with DNS (§4.1). **Shown**
9. The LMF costs about 5.5% more than the unfiltered computation on the Taylor–Green vortex (§4.1). **Shown**
10. T106C: HLLC-LMF and Roe-LMF ($N=3$, $s_0=-4.0$) are both stable; the isentropic Mach number agrees excellently with the experiment of Michálek et al. and with the CPR $N=3$ results of Alhawwary & Wang; the LMF has negligible impact on it (Table 4; Fig. 8; §4.2). **Shown**
11. T106C pressure spectra behind the trailing edge: Roe and HLLC agree in the inertial subrange and differ at high frequency (Fig. 6, cut-off $St\approx6300$); the reason "would require further investigations" (§4.2); the conclusions add that Roe decays faster at high frequency (§5). **Shown** / **Stated**
12. T106C resolution with HLLC-LMF, $N=3$: mean $y^+\approx0.5$ (with the $1/(N+1)$ scaling of Eq. 26), $\Delta x^+\approx20$, $\Delta z^+\approx6$; averaging over $5t_c$ (§4.2; Fig. 7). **Shown**
13. For DG and flux reconstruction a first-cell $y^+$ computed from the cell height is divided by $N+1$: $y^+=\rho u_\tau d_1/(\mu(N+1))$ (Eq. 26) (§4.2). **Stated**
14. LS89: the isentropic Mach number is insensitive to the degrees of freedom in 3D, and comparing it alone is insufficient to validate a solver on LS89 (§4.3.1, Fig. 13). **Shown** / **Stated**
15. LS89: all setups predict the transition location well; differences appear only in the turbulent region, where heat-transfer coefficient and $C_f$ increase; the heat-transfer coefficient improves from Setup 1 to Setup 4 (Figs. 13–14; §4.3.1). **Shown**
16. Raising $N$ from 2 to 3 on a fixed grid improves the heat-transfer coefficient towards the suction-side trailing edge; refining the spanwise spacing at $N=3$ improves it further; 15 spanwise layers ($\Delta z^+\approx60$) are cost-effective (Fig. 14; §4.3.1). **Shown**
17. A spanwise spacing $\Delta z^+\approx45$–60 suffices for a satisfactory mean heat-transfer prediction on LS89 (Abstract; §4.3.1; §5). **Shown**
18. Spanwise coarsening is less critical for mean quantities; Alhawwary and Wang's statement for the isentropic Mach number on a low-pressure turbine also holds for the heat-transfer coefficient (§4.3.1). **Shown**
19. LS89, $N=3$, Setup 2: HLLC is stable with $s_0=-4$ and $-4.3$, Roe only with $-4.3$ (Table 7); the author explains it by Roe's known lack of robustness near vacuum states, after Toro (§4.3.2). **Shown** / **Stated**
20. LS89, $N=2$: HLLC stable with $s_0=-3.3$ and $-3.7$; Roe fails with $-3.3$ and is stable with $-3.7$ (Table 8; §4.4.2). **Shown**
21. The heat-transfer coefficient depends more on the filter threshold than on the Riemann solver: Roe-LMF and HLLC-LMF ($s_0=-4.3$) agree, HLLC-LMF-2 ($s_0=-4.0$) improves; the transition location is insensitive to $s_0$, the turbulent-region heat transfer is not (Fig. 17; §4.3.2). **Shown**
22. The entropy filter stabilizes LS89 "without any tuning parameters" but resolves the trailing-edge pressure waves less sharply than HLLC-LMF-2, consistent with Gao et al. (Fig. 15; §4.3.2). **Shown**
23. LS89 pressure spectra (Fig. 16): HLLC-LMF-2 and Jia et al.'s CPR $N=3$ agree in the inertial subrange, but the CPR run decays faster at high frequency, so HLLC-LMF-2 is less dissipative; the author attributes the extra CPR dissipation to the hpMusic limiter; the entropy-filter spectrum resembles the CPR one (§4.3.2). **Shown** / **Stated**
24. The entropy filter slightly underpredicts the heat-transfer coefficient relative to HLLC-LMF-2 but does slightly better than HLLC-LMF and Roe-LMF; the isentropic Mach number is insensitive to filter and Riemann solver (Fig. 17; §4.3.2). **Shown**
25. A posteriori, the wake and transitional regions have $s_e\approx[-5:-4]$ in LS89 $N=3$, $[-4.5:-3.3]$ in LS89 $N=2$ and $[-5:-3]$ in T106C $N=2$, consistent with Table 2b; only a tiny proportion of elements is filtered (Figs. 18–20; §4.4). **Shown**
26. The entropy filter acts on more elements than the LMF, although its strength is small in most of them; both target similar regions (Figs. 19, 21; §4.4.2). **Shown**
27. Per iteration the entropy filter is about 15% more expensive than the LMF on LS89; the LMF is simpler to implement; the entropy filter is "not completely parameter-free", since its tolerance controls how strictly the minimum entropy principle is enforced (§4.4.3). **Shown** / **Stated**
28. Solution filtering adds local numerical dissipation to the total numerical dissipation that implicit LES relies on as a subgrid model (§2.3, citing Edoh et al.), and may cause time inconsistency (§5). **Stated**
29. Solution filtering can be connected to spectral vanishing viscosity in finite differences (Lamballais et al.); the flux-reconstruction analogue is left to future work (§2.3; §5). **Stated**
30. Over-integration may not remove all instabilities in under-resolved cases; aliasing-driven instability is more likely on coarse grids (§1; §4.3.2). **Stated**

The filter (Eqs. 17–18), with $\mathcal V$ the Vandermonde matrix and $\vartheta_m=m/(N_p-1)$ the normalized mode index (page-local), and the indicator (Eq. 19):
$$\mathcal F=\mathcal V\Lambda\mathcal V^{-1},\qquad \Lambda_{mm}=\begin{cases}1,&\vartheta_m<\vartheta_c\\ \exp\!\left[-\alpha_f\left(\dfrac{\vartheta_m-\vartheta_c}{1-\vartheta_c}\right)^{s_f}\right],&\vartheta_c<\vartheta_m<1\end{cases},\qquad s_e=\log_{10}\frac{(\rho-\rho_{N-1},\rho-\rho_{N-1})_e}{(\rho,\rho)_e},$$
with $\alpha_f=36$, $s_f=6$ throughout and $\rho_{N-1}$ the density truncated to degree $N-1$ (the cut-off $\vartheta_c$ of the LMF is not printed). The entropy filter takes $s_f=2$, $\vartheta_c=0$ and chooses $\alpha_f$ per element so that the entropy function $\mathcal S=\rho\ln(p\rho^{-\gamma})$ does not fall below its local minimum minus $\epsilon_{\mathcal S}=10^{-4}$, with $\rho,p\ge10^{-8}$ (Eqs. 20–22). **Stated**

# Printed slips

- **Table 2a**, $N=2$ row: $s_0+\kappa_s$ printed "2.77", while $s_0=-2.7$ and $\kappa_s=4$ give 1.3 (the $N=3$ row, $-8.3$, $-4.3$, $-0.3$, is consistent) *(compiler check, not in the sources)*.
- **Table 2a–2b:** $-4\ln2=-2.77$ and $-4\ln3=-4.39$ are printed $-2.7$ and $-4.3$ (truncated) *(compiler check, not in the sources)*.
- **Table 2b against §5:** Table 2b gives $[-3.7,-2.7]$ and $[-5.3,-4.3]$; the summary $[-(N+2):-(N+1)]$ gives $[-4,-3]$ and $[-5,-4]$ *(compiler check, not in the sources)*.
- **§4.4.1:** "For p3, these regions are marked by a range of [-5.5:4]" (sign of the upper bound missing).
- **Eq. 7:** conductivity printed $k=\dfrac{C_p}{\mu}Pr$; the dimensions require $C_p\mu/Pr$ *(compiler check, not in the sources)*. The text prints "$Cp=\frac{\gamma}{\gamma-1}RT$", which has the dimensions of an enthalpy *(compiler check, not in the sources)*.
- **§4.1:** Mach 0.1 with $V_0=0.1\sqrt{p/\rho}$; with the sound speed $\sqrt{\gamma p/\rho}$ that gives $0.1/\sqrt{1.4}\approx0.085$ *(compiler check, not in the sources)*. Eq. 23 prints the velocity without $V_0$ and the pressure term as "$\cos(2z+2)$".
- **Eq. 18:** the printed cases leave $\vartheta_m=\vartheta_c$ and $\vartheta_m=1$ uncovered; "$N_p$ the maximum order of the polynomial" is ambiguous for the indexing.
- **p. 6:** Jacobian printed $\partial(x,y,z)/\partial(\varepsilon,\eta,\zeta)$ with $\hat{\boldsymbol x}=(\xi,\eta,\zeta)$.
- **Eq. 13:** left side printed $\hat{\mathbf F}$ for the text's $\hat{\mathbf F}^D$. **Eq. 19:** numerator printed $(\phi-\hat\phi)_e$ with one argument of the inner product. **Eq. 15:** "iff = f2".
- **End of §4.3.2:** "similar conclusions can be drawn as in Fig. 12: isentropic Mach number is insensitive…"; Fig. 12 shows the density-gradient magnitude, the isentropic Mach number is Fig. 13.
- **Entropy-filter attribution:** "The entropy filter (EF) proposed by Dzanic and Witherden [31]"; [31] is Dzanic, Trojak & Witherden (2023, arXiv), the entropy-filter paper is [42].
- **"Jia and Wang [8]"** for the five-author reference [8].
- Typos: "Legendre-Gauss-Labbato", "Vicent et al. [33]", "Tabel 2a", "invsicid", "adpatively", "Tayor-Green", "schemnes", "Sunction side" (Fig. 11 legend), "gird spacing", "instataneous".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, "p3" | $N$, $N=3$ | **collision:** $p$ is also the pressure |
| $\mathbf U=(\rho,\rho u,\rho v,\rho w,\rho e)$ | ($\rho$, momentum, $E=\rho e$) | $e$ total energy per unit mass |
| $\mathbf V$ | $u_i$ | |
| $h=e+p/\rho$ | (total enthalpy, page-local) | **collision** with the element size $h$ |
| $\sigma_{ij}$ | $\sigma_{ij}$ | agrees |
| $k$ (Eq. 6–7) | (thermal conductivity) | **collision** with the turbulent kinetic energy; $k$ is also the flux-point index of Eq. 14 |
| $\hat\cdot$ | (reference-element quantity) | **collision** with the test filter; in Eq. 19 the hat is the truncated expansion, written $\rho_{N-1}$ here |
| $\xi,\eta,\zeta$ | $\xi$ (reference coordinates) | **collision:** $\eta$ is the Kolmogorov length in the registry |
| $\tau$, $\beta$ (Eq. 16) | (LDG penalty $=0$ and bias $=\pm0.5$) | **collision** with $\tau_{ij}$ and the field-inversion $\beta$ |
| $\eta_i=i/(N_p-1)$, $\eta_c$ | $\vartheta_m$, $\vartheta_c$ (normalized mode index and cut-off, page-local) | renamed: $\eta$ is the Kolmogorov length and $\eta_m$ the magnetic diffusivity; as on [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md) |
| $\alpha$ (Eq. 18) | $\alpha_f$ (filter strength, page-local) | **collision** with the DG/FV blending factor $\alpha$ |
| $s$ (Eq. 18) | $s_f$ (filter order, page-local) | **collision:** the source's $s=\rho\ln(p\rho^{-\gamma})$ in Eq. 21 is the entropy, written $\mathcal S$ here |
| $s_e$, $s_0$ | $s_e$, $s_0$ (smoothness indicator and threshold, page-local) | $s_0$ is $-C_0\ln N$ in Tables 1 and 2a, the activation threshold in the LMF |
| $\kappa$, $C_0$ | $\kappa_s$, $C_0$ (ramp width, threshold constant) | **collision** with the von Kármán $\kappa$ |
| $\varepsilon_s$ | $\epsilon_{\mathcal S}$ (entropy tolerance, page-local) | as on [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md) |
| $K$, $\varepsilon_K=dK/dt$ | (domain-integrated kinetic energy and its rate) | plotted as "TKE dissipation rate" |
| $t_c$ | (convective time: $L/V_0$ for the vortex, chord over exit velocity for the turbines) | |
| $y^+$ (Eq. 26) | $y^+$ divided by $N+1$; $d_1$ the first-cell height | |
| $x^+$, $z^+$ | $\Delta x^+$, $\Delta z^+$ | averaged spacings |
| $M_{is}$, HTC | (isentropic Mach number, heat-transfer coefficient) | |
| LMF, EF | local modal filter, entropy filter | |

# Reference list

54 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Reference [42]
(Dzanic & Witherden 2022, J. Comput. Phys. 468:111501, the entropy filter)
is a different work from the Source `dzanic-2022` (`dzanic-2022-b`);
reference [26] (Li & Wang 2017, AIAA paper) differs from the existing
`li-2017` entry (`li-2017-b`); reference [31] is an arXiv preprint (2023),
kept as its own entry. References [32], [49], [51], [52] print a volume but
no page or article number, recorded as printed. No printed duplicates.

# Pages created or updated

Chunk 5 (2026-10-26), cited further in chunk 7. This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [Spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
