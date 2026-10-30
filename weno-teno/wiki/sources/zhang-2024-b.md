---
type: Source
title: "Zhang et al. (2024) — A finite difference scale-adaptive TENO scheme for turbulence simulations"
description: "Six-point TENO6-SA: a scale sensor made phase independent for sinusoids selects, per wavenumber band, a sixth-, spectrally optimized fourth- or second-order linear scheme with its own TENO cut-off, extending the resolved bandwidth by 60% over TENO6 while keeping sixth order on smooth data."
resource: "doi:10.1016/j.jcp.2024.112793"
source_kind: paper
authors: [Zhang X., Jiang Z., Qin X., Qu F., Yan C.]
year: 2024
venue: "J. Comput. Phys. 502:112793"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Zhang_A_finite_difference_scale-adaptive_TENO_scheme_for_turbulenc.pdf"
tags: [teno, low-dissipation, spectral-analysis, finite-difference, turbulence]
timestamp: 2026-10-24T06:00:00Z
---

# Summary

Zhang et al. (2024b) target the small-scale resolution of finite-difference shock-capturing schemes
for compressible turbulence. The authors argue that classical spectral optimization, whether by
changing the linear weights (TENO6-opt) or by tuning dispersion and dissipation separately (the
[MDCD schemes](/methods/mdcd-scheme.md)), always gives up formal order. Their **piecewise spectrum
optimization method (PSOM)** keeps the sixth-order central scheme at low wavenumbers and switches,
at locally detected wavenumbers, to spectrally optimized fourth- and second-order central schemes on
the same six-point stencil. At 1% dispersion error these resolve up to $\vartheta=1.100$, $1.530$
and $1.726$. All dissipation comes from the nonlinear
[TENO](/methods/targeted-eno.md) mechanism: each band has its own cut-off $C_T$
($10^{-5}$, $10^{-10}$, $10^{-13}$, $10^{-8}$) and its own linear weights.

The switch needs a local wavenumber. The authors analyse the six-point
[scale sensors](/definitions/scale-sensor.md) of Li, Chen & Ren (2022a) and of S. Li et al. (2022)
on a sinusoid. They show that the $\mathsf D_2,\mathsf D_4$ part is phase independent with a closed
form in one free coefficient. They then add two constraints that make the $\mathsf D_1,\mathsf D_3$
part agree with it, and pick the coefficient that resolves up to $\vartheta=2.137$, against 1.454
for Li, Chen & Ren. The last candidate stencil uses the average of the TENO6 four-point and the
[WENO-CU6](/methods/weno-cu6.md) six-point [smoothness indicators](/definitions/smoothness-indicator.md).

The resulting TENO6-SA has an
[approximate-dispersion-relation](/definitions/approximate-dispersion-relation.md) bandwidth of
1.767 and stays sixth order on smooth advection, where TENO6-opt drops to fifth and TENO6-A
([adaptive TENO](/methods/adaptive-teno.md)) to fourth order. It is compared with
[WENO-Z](/methods/weno-z.md) (WENO7-Z), EWENO-CU6, TENO6, TENO6-opt and TENO6-A on
[critical points](/properties/critical-point-accuracy.md), acoustic, shock-tube, two-dimensional and
turbulence cases, all evidence being numerical. TENO6-SA resolves the most small-scale structure and
survives the shock/wavy-wall case, where TENO6-A fails, at 15–19% more CPU time than WENO7-Z.

# Version read

Version of record (Elsevier typeset; received 20 June 2023, accepted 21 January 2024, online
26 January 2024), 41 pages, all read; text extraction clean, the equation pages checked visually.
Page 1 matches Crossref (title, five authors, venue, DOI). Numbering cited here is that of this
version.

# Key claims

Registry notation: the source's $\varphi$ is $\vartheta$, its $\Phi=\Phi_R+j\Phi_I$ is
$\tilde\vartheta=\tilde\vartheta_r+\mathrm i\,\tilde\vartheta_i$, its $\varphi_{ESW}$ and
$\Delta f_p$ are $\vartheta_{\mathrm{ESW}}$ and $\mathsf D_p$, its $IS_k$ is $\beta_k$, its $w_k$
is $\omega_k$. The free sensor coefficients $b_1$, $c_1$ are written $b^{\mathrm s}_1$,
$c^{\mathrm s}_1$ (page-local).

1. Spectral optimization in the finite-difference framework, by changing the optimal weights or by redesigning sub-stencils to tailor dispersion and dissipation separately, inevitably gives up accuracy order (§3.1). **Stated**
2. On the six-point stencil, dropping the highest-order constraint of the dispersion part and of the dissipation part (Eq. 21) frees one parameter in each at the cost of two orders; the result coincides with the MDCD scheme of Sun et al. (§3.1, Eqs. 19–21). **Derived**
3. The sixth-order central dispersion scheme ($a_1=3/4$, $a_2=-3/20$, $a_3=1/60$) has $\tilde\vartheta_r=\frac1{30}[45\sin\vartheta-9\sin2\vartheta+\sin3\vartheta]$ and a 1% resolved bandwidth of 1.100 (§3.2). **Derived** *(compiler check, not in the sources: 1.1001 from the printed $\tilde\vartheta_r$.)*
4. The optimized fourth-order scheme ($a_1=4/5$, $a_2=-19/100$, $a_3=2/75$) resolves up to 1.530 and the optimized second-order scheme ($a_1=104/125$, $a_2=-229/1000$, $a_3=21/500$) up to 1.726, about 56.9% above 1.100 (§3.2). **Derived** *(compiler check: 1.5303 and 1.7264.)*
5. The schemes switch at $\vartheta=1.085$ (sixth to fourth order) and $1.516$ (fourth to second), where the dispersion errors on the two sides are equal (§3.2, Fig. 1). **Derived**
6. In the approximate dispersion relation, the wavenumber at which TENO turns nonlinear grows as $C_T$ decreases, from 1.058 at $C_T=10^{-4}$ to 1.794 at $10^{-13}$ (Table 1). **Shown**
7. $C_T$ is set to $10^{-5}$, $10^{-10}$, $10^{-13}$ for the sixth-, fourth- and second-order schemes; the authors know of no other scheme with $C_T$ as small as $10^{-13}$, admissible because the better dispersion lowers the dissipation needed (§3.2). **Stated**
8. The sensor of Li, Chen & Ren (Eq. 27) is phase independent but resolves only up to 1.454 at 1% error (efficiency 46.279%); the sensor of S. Li et al. (Eq. 30) reaches higher wavenumbers but oscillates with the phase because its two ratios differ (§4.1–4.2, Fig. 3). **Shown**
9. For any sinusoid, $\sqrt{|\mathsf D_4|/|\mathsf D_2|}=\sqrt{|2(1-\cos\vartheta)|/|(1+2b^{\mathrm s}_1)\cos\vartheta-2b^{\mathrm s}_1|}$, independent of phase and amplitude; $b^{\mathrm s}_1=-5/12$ recovers the Li, Chen & Ren sensor (Eq. 31). **Derived**
10. Requiring $\sqrt{|\mathsf D_3|/|\mathsf D_1|}=\sqrt{|\mathsf D_4|/|\mathsf D_2|}$ gives two constraints on the $\mathsf D_1$ coefficients, after which the sensor depends on $b^{\mathrm s}_1$ alone and $c^{\mathrm s}_1$ does not affect monochromatic waves (Eq. 32). **Derived**
11. With $b^{\mathrm s}_1=-0.398$ ($c^{\mathrm s}_1=-5$, $\varepsilon_{\mathrm s}=10^{-5}$, Eq. 33) the sensor resolves up to $\vartheta=2.137$ at 1% error, efficiency 68.012% (§4.2, Fig. 4). **Shown** *(compiler check: 2.1367 and 68.01% from Eq. 31; 1.4539 for $b^{\mathrm s}_1=-5/12$.)*
12. $b^{\mathrm s}_1=-5/12$ makes the sensor curve tangent to $\vartheta_{\mathrm{ESW}}=\vartheta$ at the origin and keeps it below; smaller values stay below with larger error, larger values cross the reference at low wavenumber (§4.2). **Stated** *(compiler check: Eq. 31 expands as $\vartheta_{\mathrm{ESW}}=\vartheta\{1+\vartheta^2[(1+2b^{\mathrm s}_1)/4-1/24]+O(\vartheta^4)\}$, so the slope at the origin is 1 for every $b^{\mathrm s}_1$; $-5/12$ is the value that cancels the $\vartheta^3$ error term, and the stated behaviour on either side follows from its sign.)*
13. The arccos sensor of Li & Ren (2023), exact for sinusoids on $[0,\pi]$, is capped at $\pi$ at discontinuities; the proposed sensor gives larger values there, which suits TENO better (§4.2, Eqs. 34–35). **Stated**
14. TENO6-SA (Algorithm 1) uses four bands: $\vartheta_{\mathrm{ESW}}<1.085$ with $C_T=10^{-5}$ and $d_k=(9/20,3/10,1/20,1/5)$; $<1.516$ with $10^{-10}$ and $(21/50,9/50,2/25,8/25)$; $<1.726$ with $10^{-13}$, and $\ge1.726$ with $10^{-8}$, both with the least-squares weights $(5571/14000,321/3500,1429/14000,1429/3500)$, because the second-order flux is not a convex combination of the candidate fluxes (§5.1). **Stated** *(compiler check, not in the sources: with the TENO6 candidates ordered central, downwind, upwind, four-point, the first two weight sets reproduce the sixth- and fourth-order fluxes exactly; the third leaves residuals up to $8\times10^{-3}$ in the stencil coefficients.)*
15. The $C_T$ trend of TENO6-SA (smaller at higher wavenumber up to 1.726) is opposite to that of TENO-A, which raises $C_T$ at high wavenumber; the authors reconcile the two: TENO-A keeps a single linear scheme, PSOM relays linear schemes of better dispersion, and above 1.726 $C_T$ rises again (§5.1). **Stated**
16. The last candidate stencil of TENO6-SA takes $\tfrac12(\beta^{(4)}_3+\beta^{(6)}_3)$, the average of the TENO6 four-point and the EWENO-CU6 six-point indicators (Eq. 36). **Stated**
17. Resolved bandwidths in the approximate dispersion relation at 1%: TENO6-A 1.052, EWENO-CU6 1.086, TENO6 and TENO6-opt 1.100, WENO7-Z 1.330, TENO6-SA 1.767; at 1.5%: EWENO-CU6 1.165, TENO6 and TENO6-opt 1.184, WENO7-Z 1.418, TENO6-A 1.590, TENO6-SA 1.774 (§5.2, Fig. 5). **Shown**
18. TENO6-SA has no numerical dissipation in its resolved range and enough at moderate and high wavenumbers; in the nonlinear spectral analysis of Fauconnier & Dick (10000 samples) it has the best mean dispersion and a lower standard deviation at low and moderate wavenumbers (§5.2, Figs. 5–6). **Shown**
19. Advection of $\sin(\pi x-\sin(\pi x)/\pi)$ to $t=2$ (seventh-order linear SSP Runge–Kutta, CFL 0.1): WENO7-Z converges at order 7, EWENO-CU6, TENO6 and TENO6-SA at order 6 with identical errors ($L_1=6.17\times10^{-15}$ at $N_x=1600$), TENO6-opt at 5, TENO6-A at 4 (Table 2). **Shown**
20. The scale sensor adds about 13% to the cost of TENO6 in the advection test; TENO6-A costs slightly more than TENO6-SA (§5.3). **Stated** (see Printed slips)
21. Rates at an $n_{\mathrm{cp}}$-th order critical point of $x^{n_{\mathrm{cp}}+1}e^{100x}$, $n_{\mathrm{cp}}=0,\dots,6$: TENO6-SA and TENO6 6, 6, 2, 4, 4, 6, 6; TENO6-opt 5, 5, 2, 4, 4, 6, 6; TENO6-A 4, 4, 4, 3, 4, 6, 6; EWENO-CU6 6, 5, 2, 3, 4, 5, 6; WENO7-Z 7, 7, 6, 3, 4, 5, 6 (Table 3). **Shown**
22. Two-dimensional Gaussian advection ($200^2$, two periods): WENO7-Z has the smallest errors; among the six-point schemes TENO6-SA is best ($L_1=9.34\times10^{-5}$); TENO6-A shows a forward phase error and a spurious oscillation at the wavefront (§5.5, Table 4). **Shown**
23. Broadband acoustic waves (128 points): TENO6-SA has the lowest mean and maximum density errors at $k_0=10$ and $k_0=15$ (Table 5). **Shown**
24. In the Titarev–Toro problem, lowering $C_T$ of the lowest band ($10^{-3}$ to $10^{-10}$) sharpens the solution, but $10^{-7}$ creates spurious oscillations at several sound waves and $10^{-10}$ at all; conclusions from the monochromatic dispersion analysis do not transfer directly to nonlinear problems (§6.1.3, Fig. 13). **Shown**
25. All schemes run the 123 problem without a negative-pressure correction; TENO6-SA overshoots slightly at the Sod contact and the blast-wave strong shock but stays robust (§6.2). **Shown**
26. In the shock/wavy-wall interaction ($2500\times500$) TENO6-A fails through spurious oscillations, while TENO6-SA runs stably despite $C_T=10^{-13}$ (§6.3.3, Fig. 23). **Shown**
27. In the two-dimensional Riemann problem, $\vartheta_{\mathrm{ESW}}$ stays below 1.085 in most of the domain and exceeds the top band limit at shocks and slip lines (§6.3.2, Fig. 22). **Shown**
28. In the inviscid Taylor–Green vortex ($100^3$, $\gamma=5/3$), the viscous one ($\mathrm{Re}=100$, 400, 1600) and decaying compressible isotropic turbulence ($64^3$, $M_t=0.6$), TENO6-SA is closest to the reference in enstrophy and spectra (§6.4, Figs. 24–30). **Shown**
29. CPU-time increments over WENO7-Z in §6: TENO6-SA 15.31–19.29%, TENO6 4.56–12.32%, TENO6-A 17.15–25.20% (Table 6). **Shown**
30. The resolved bandwidth of TENO6-SA is 60.6% larger than that of TENO6 (Conclusions). **Shown**

# Printed slips

- §3.2: "The 6th-order dispersion scheme should be satisfied that $G_1=0$, $G_2=0$, and $G_3=0$" (likewise for the fourth and second order); §3.1 states $G_1=1$. *(Compiler check, not in the sources: the printed coefficients satisfy $G_1=1$, $2\cdot\frac34-4\cdot\frac3{20}+6\cdot\frac1{60}=1$.)*
- Eq. (21): the dissipation coefficient of $\Delta x\,f''$ is printed $\mathcal G_1=b_1+4b_2+6b_3$. *(Compiler check, not in the sources: $\sum_kb_k[f(x+k\Delta x)+f(x-k\Delta x)]$ contributes $\sum_kk^2b_k=b_1+4b_2+9b_3$; the printed $\mathcal G_2$ and $\mathcal G_3$ follow the same pattern, $\frac2{4!}\sum k^4b_k$ and $\frac2{6!}\sum k^6b_k$, and are correct.)*
- Eq. (2): $\frac{du_i}{dt}=-\frac{\partial f}{\partial x}\big|_{x_i}=\frac{h_{i+1/2}-h_{i-1/2}}{\Delta x}$, the right-hand side lacking the minus sign of Eq. (4); §2.1 says "Equation (4) can be expressed in the following approximate form" to introduce Eq. (4) itself.
- Eq. (11): the six-point indicator switches its index from $i$ to $j$, and two lines end "$+1325006f_{j+2}$" and "$-2792660f_{j+2}$" inside brackets that already contain $f_{j+2}$ *(compiler check, not in the sources: the pattern of the other lines requires $f_{j+3}$ there)*; §2.4 refers to "Eq. (13)" for the indicators, which are Eq. (11).
- Eq. (23): $f^{(2)}$ and $f^{(4)}$ of $A\sin(\omega x+\theta)$ are printed with $\cos$. *(Compiler check, not in the sources: both are multiples of $\sin(\omega x+\theta)$; the ratio $\omega$ is unaffected.)*
- Eq. (31), second bracket: the coefficients of $A\sin(\omega x+\theta)$ and $A\sin(\omega x+\omega\Delta x+\theta)$ are printed as 1 instead of $b_1$ (Eq. 28). *(Compiler check, not in the sources: the printed closed form holds only with $b_1$.)*
- §6.1.3 and §6.3.2 use 1.732 as the band limit and maximum resolved bandwidth, whereas Algorithm 1 and §3.2 give 1.726 and §5.2 gives 1.767.
- §6.1.3 places the junction of sound and entropy waves at "$x\approx2$" and later at "approximately $x\approx-2$".
- §5.3: "an approximate 13% increase in cost compared to the TENO6 scheme". *(Compiler check: Table 2 gives TENO6-SA/TENO6 CPU ratios 4.86/3.77, 18.81/14.33, 73.77/56.44, 289.83/222.97 and 1151.83/890.53, all 1.29–1.31, about 30%.)*
- Eq. (42), Shu–Osher left state $u=4\sqrt{39}/5\approx4.996$. *(Compiler check: the Rankine–Hugoniot conditions for $\rho:1\to27/7$, $p:1\to31/3$ into gas at rest give shock speed $\sqrt{12.6}\approx3.550$ and $u=\tfrac{20}{27}\sqrt{12.6}=4\sqrt{35}/9\approx2.629$, the value 2.629369 printed by [Wei & Xia (2024)](/sources/wei-2024.md).)*
- Eq. (47), double Mach reflection: the post-shock region is printed $y>\sqrt3x+1/6$, and the wall starts at $x=1/6$. *(Compiler check, not in the sources: that line meets $y=0$ at $x=-1/(6\sqrt3)$; the line through $(1/6,0)$ is $y=\sqrt3(x-1/6)$.)* The $1200\times900$ grid on $[0,3]\times[0,1]$ gives $\Delta x\ne\Delta y$, uncommented.
- Table 5 caption omits EWENO-CU6, which the table contains; "2D-Riemmann" (Table 6), "2th-order" (Algorithm 1), "invisid" (Fig. 24).
- Ref. [58] prints volume 4 for Commun. Comput. Phys. (2020); ref. [52] prints AIAA J. 57 with year 2018. Recorded as printed.

# Notation map

| Zhang et al. (2024b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f$, $f^\pm$, $\hat f_{i+1/2}$, $\hat f^k_{i+1/2}$ | $f$, $f^\pm$, $\hat f_{i+1/2}$, $\hat f^{(k)}_{i+1/2}$ | local Lax–Friedrichs splitting; agrees |
| $h$ (Eq. 3) | kept | implicit flux function of the conservative finite difference |
| $r$ | $r$ (WENO), number of sub-stencils (TENO) | **two meanings in §2.2 and §2.5** |
| $d^r_k$, $d_k$ | $d_k$ | linear weights; TENO6 candidates ordered central, downwind, upwind, four-point, **not** the registry's $S_0$ most upwind |
| $\omega^r_k$, $w_k$, $\alpha^r_k$ | $\omega_k$, $\alpha_k$ | |
| $IS^r_k$, $IS^4_3$, $IS^6_3$ | $\beta_k$, $\beta^{(4)}_3$, $\beta^{(6)}_3$ | superscript = stencil width |
| $\tau_{2r-1}$, $\tau_6$, $\tau_K$ | $\tau_{2r-1}$, $\tau_6$ | subscript = points of the global stencil; agrees |
| $\varepsilon$ | $\epsilon$; $\varepsilon_{\mathrm s}$ in the sensor | **also the 1% tolerance and the acoustic amplitude** |
| $p$, $q$, $C$, $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$ | $q$, $C$, $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$ | WENO exponent $p$ is the registry $q$ |
| $C_{max}$, $C_{min}$, $\theta$, $\xi$, $m$ (Eq. 12) | kept | EWENO-CU6 switch; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\alpha_1$, $\alpha_2$, $g(m)$, $m$, $\eta_i$, $C_r$, $\xi$, $\bar\beta$ (Eq. 17) | $b_1$, $b_2$, $\varphi(\mu_d)$, $\mu_d$, $\sigma_i$, $C_r$, $\xi_{\mathrm A}$, $b$ | TENO-A, as on [adaptive TENO](/methods/adaptive-teno.md) |
| $\varphi=\omega\Delta x$ | $\vartheta=k_w\Delta x$ | reduced wavenumber |
| $\Phi$, $\Phi_R$, $\Phi_I$ | $\tilde\vartheta$, $\tilde\vartheta_r$, $\tilde\vartheta_i$ | $\Phi_I<0$ dissipative |
| $j$ | $\mathrm i$ | imaginary unit |
| $a_k$, $b_k$ (§3) | kept page-local | dispersion and dissipation coefficients; **$a$ is the wave speed in the registry** |
| $G_1,G_2,G_3$, $\mathcal G_0,\dots,\mathcal G_3$ | kept page-local | Taylor coefficients; **collide with $G$ (admissible set) and $\mathcal G$ (amplification factor)** |
| $\varphi_{ESW}$ | $\vartheta_{\mathrm{ESW}}$ | as on [scale sensors](/definitions/scale-sensor.md) |
| $\Delta f_{1..4,i+1/2}$ | $\mathsf D_1,\dots,\mathsf D_4$ | |
| $a_k,b_k,c_k,d_k$ (§4) | coefficients of $\mathsf D_1,\dots,\mathsf D_4$; $b_1$, $c_1$ written $b^{\mathrm s}_1$, $c^{\mathrm s}_1$ | **$d_k$ collides with the linear weights, $b_1$ with TENO-A** |
| $n_{cp}$, $r_c$ | $n_{\mathrm{cp}}$, observed order | |
| $\mu_R$, $\mu_I$, $\sigma_R$ | kept | mean and standard deviation of the nonlinear spectral analysis |
| $Ma_t$, $Re_\lambda$, $k_0$ | $M_t$, $\mathrm{Re}_\lambda$, $k_0$ | turbulence parameters |

# Reference list

68 printed references in numbered style ([1]–[68]), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `zhang-2024-b`. All print DOIs except [31] (AIAA
conference paper) and [59] (Springer chapter without book title). Five cited works share a
first-author–year key with a different ingested or planned source: [26] Luo & Wu (WENO-Z+, JCP
445:110608), [46] S. Li et al. (J. Sci. Comput. 92:29), [55] Li & Ren (Phys. Fluids 35:036114),
[8] L. Huang et al. (JCP 486:112115) and [62] W. Huang et al. (Comput. Fluids 240:105435); they are
identified by venue, volume and page. [45] is [Li, Chen & Ren (2022a)](/sources/li-2022.md), [40] is
[Fu (2023)](/sources/fu-2023.md) and [51] is [Takagi et al. (2022)](/sources/takagi-2022.md).
Ref. [37] prints the first author as "I. Wibisono Yanuar" and [62] the last two authors as
"Y. Xianxu, C. Jianqiang"; kept as printed. No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunks 9–12 (2026-10-23/30). This source is cited on:

* [Accuracy at critical points](/properties/critical-point-accuracy.md)
* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Scale sensors and the effective scaled wavenumber](/definitions/scale-sensor.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [WENO-CU6](/methods/weno-cu6.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
