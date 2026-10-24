---
type: Source
title: "Liang & Fu (2024) — A new high-order shock-capturing TENO scheme combined with skew-symmetric-splitting method for compressible gas dynamics and turbulence simulation"
description: "TENO-S: a hybrid finite-difference scheme that uses a dispersion-optimized eight-point kinetic-energy-preserving skew-symmetric split flux in smooth regions and an eight-point adaptive TENO flux in cells flagged by a new indicator built from six equal-width three-point stencils, sixth order and cheaper than WENO-CU6, TENO6 and TENO8."
resource: "doi:10.1016/j.cpc.2024.109236"
source_kind: paper
authors: [Liang T., Fu L.]
year: 2024
venue: "Comput. Phys. Commun. 302:109236"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computer_Physics_Communications_Liang_A_new_high-order_shock-capturing_TENO_scheme_combined_with_s.pdf"
tags: [teno, hybrid-scheme, kinetic-energy-preserving, split-form, troubled-cell, spectral-analysis]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds **TENO-S**, a [hybrid](/methods/hybrid-weno.md) finite-difference
scheme for the compressible Euler and Navier–Stokes equations on uniform Cartesian
meshes. In cells declared smooth, the interface flux is the non-dissipative
cubic (Kennedy–Gruber) [split convective form](/methods/split-convective-forms.md),
written in Pirozzoli's locally conservative two-point form, extended to an
eight-point stencil and given dispersion-optimized sixth-order coefficients
$a_\ell$; this path is claimed to give
[kinetic energy preservation](/properties/kinetic-energy-preservation.md). In
flagged cells the flux is an eight-point [TENO](/methods/targeted-eno.md)
reconstruction with an optimized sixth-order background linear scheme, applied in
[characteristic variables](/methods/characteristic-decomposition.md) with
[Rusanov flux splitting](/methods/lax-friedrichs-flux.md) and with the
[adaptive TENO](/methods/adaptive-teno.md) cut-off, $C_T$ between $10^{-7}$ and
$10^{-10}$.

The new ingredient is an eight-point
[troubled-cell indicator](/definitions/troubled-cell-indicator.md): six equal-width
three-point stencils covering $x_{i-3},\dots,x_{i+4}$, three of which do not contain
$x_i$, Jiang–Shu-type [smoothness indicators](/definitions/smoothness-indicator.md)
integrated over the target cell, TENO-like measures $\gamma_k=(\beta_k+\epsilon)^{-6}$
normalized to $\chi_k$, and the cell declared smooth only if every $\chi_k>10^{-6}$.
It is evaluated on density (and total energy in 1D) in physical space, so the costly
characteristic TENO path runs only in flagged cells. Both the skew-split flux and
the TENO background scheme take their dispersion from one
[approximate-dispersion-relation](/definitions/approximate-dispersion-relation.md)
optimization; the [numerical dissipation](/definitions/numerical-dissipation.md) of
the background scheme is set separately by $b_0=0.01$.

Evidence is numerical: sixth-order convergence on an entropy wave, shock tubes,
Shu–Osher, interacting blast waves, 2D Riemann configurations, double Mach
reflection, Rayleigh–Taylor, Kelvin–Helmholtz, an implosion, inviscid and viscous
Taylor–Green vortices and decaying compressible isotropic turbulence, against
[WENO-CU6](/methods/weno-cu6.md), TENO6 and TENO8 with single-CPU wall-clock times.
TENO-S is the cheapest in every reported case (25–52% cheaper in 2D) and keeps the
kinetic energy of the inviscid Taylor–Green vortex constant to plotting accuracy.

# Version read

Version of record (Elsevier typeset; received 6 October 2023, accepted 6 May 2024,
online 10 May 2024), 28 pages, all read; Eqs. (27)–(30), (40), (43), (44), (48) and
Figs. 1, 2 read visually. Page 1 matches Crossref (title, two authors, venue, DOI).
The C++ code is stated to be at `https://github.com/LMNS3d/TENO_CPC` (Algorithm 1).
Numbering cited here is that of this version.

# Key claims

Registry notation (see the notation map): the source's $w_k$ are $\omega_k$, its
$\beta_{k,r}$ are $\beta_k$, its $\varepsilon$ is $\epsilon$, its reduced wavenumber
$\xi$ is $\vartheta$, its velocity $(u,v,w)$ is $v=(v_1,v_2,v_3)$, its TENO-A
quantities $(m,\eta,g,\alpha_1,\alpha_2,\beta)$ are $(\mu_d,\sigma,\varphi,b_1,b_2,b)$.

1. Classical shock-capturing schemes cannot run long-time non-dissipative simulations (e.g. the inviscid Taylor–Green vortex) because their inherent dissipation prevents conservation of quadratic invariants such as kinetic energy (Abstract, §1, §3.2). **Stated**
2. The cubic (Kennedy–Gruber) split form, Eq. (23), is more robust than the quadratic (Feiereisen) form, Eq. (22) (§2.3, citing [36,52]). **Stated**
3. Inserting the two-point flux $\hat f^{\mathrm{skew}}_{i+1/2}=\tfrac18(\rho_i+\rho_{i+1})(\phi_i+\phi_{i+1})(v_i+v_{i+1})$ (Eq. (26)) into the conservative difference (25) recovers the non-conservative cubic split form (24); the form extends to arbitrary order as $\hat f^{\mathrm{skew}}_{i+1/2}=2\sum_{\ell=1}^La_\ell\sum_{m=0}^{\ell-1}\tfrac18(\rho_{i-m}+\rho_{i-m+\ell})(\phi_{i-m}+\phi_{i-m+\ell})(v_{i-m}+v_{i-m+\ell})$ (Eqs. (27)–(28), citing Pirozzoli). **Stated**
4. The eight-point indicator built from six equal-width three-point stencils (Fig. 2, Eqs. (31)–(34)) separates non-smooth high-wavenumber fluctuations and discontinuities from smooth scales "in the wavenumber space", and is "more universal for general conservation laws" than physical-variable sensors such as the Ducros sensor (§3.1). **Stated** (universality; no comparison shown); the behaviour is **Shown** in indicator maps (Figs. 3, 5, 8, 10–15)
5. Indicator parameters: $\epsilon=10^{-4}$ (1D) and $10^{-2}$ (multi-D) in $\gamma_k=(\beta_k+\epsilon)^{-6}$, Eq. (32), threshold $C_{T2}=10^{-6}$ in Eq. (34); density and total energy are used in 1D, density alone in multi-D (§3.1). **Stated**
6. TENO-S (Eq. (35), Algorithm 1) takes the TENO flux (20) where the indicator is 1 and the skew-symmetric flux (27) where it is 0; characteristic decomposition (Roe average) and Rusanov splitting are used only in flagged cells (§3.2). **Stated** (definition)
7. The optimized eight-point skew-split coefficients are $a_1=0.8441336457279522$, $a_2=-0.2441336457279522$, $a_3=0.0570096576929319$, $a_4=-0.006723831837710873$ (sixth order, weight exponent 7 in the objective (41)); the flux is "still non-dissipative" because only the dispersive part enters (§3.3.1). **Derived** *(Compiler check, not in the sources: these values give $2a_1+4a_2+6a_3+8a_4=1$ and annul the $\Delta x^2$ and $\Delta x^4$ Taylor coefficients of Eq. (40) to round-off.)*
8. The optimal sixth-order background linear scheme of the eight-point TENO is Eq. (46), with $d_0=0.4130855804023061$, $d_1=0.2193140179474727$, $d_2=0.06459052081827904$, $d_3=0.1439236310125986$, $d_4=0.02746675592227204$, $d_5=0.1316194938970745$, obtained with $b_0=0.01$ chosen to make the dispersion–dissipation ratio $\zeta\approx O(10)$ (Eq. (45)) (§3.3.1). **Derived** *(Compiler check, not in the sources: $\sum_kd_k\hat f^{(k)}_{i+1/2}$ with the candidate fluxes of Eq. (11) reproduces the coefficients of Eq. (46) to $2\times10^{-15}$; the antisymmetric part of the implied derivative stencil equals the $a_\ell$ of claim 7, and its symmetric part is $(b_0,\dots,b_4)=(0.01,-0.008,0.004,-0.00114286,0.000142857)=\tfrac{b_0}{70}(70,-56,28,-8,1)$, the eighth undivided difference. The TENO background scheme is therefore the skew-split central scheme plus an eighth-difference dissipation of strength $b_0$.)*
9. The objective weight favours low wavenumbers because "for higher wavenumbers, the activated TENO nonlinear adaptation will dominate the spectral resolution properties" (§3.3.1). **Stated**
10. The adaptive cut-off of [49] is used: $C_T=10^{-\lfloor b\rfloor}$, $b=b_1-b_2(1-\varphi(\mu_d))$, $b_1=10.5$, $b_2=3.5$, $\varphi(\mu_d)=(1-\mu_d)^4(1+4\mu_d)$, $C_r=0.23$, $\varepsilon_0=10^{-3}$, giving $C_T\to10^{-7}$ at discontinuities and $10^{-10}$ in smooth regions (Eqs. (47)–(49)). **Stated** *(Compiler check, not in the sources: $\mu_d=1$ gives $b=7$, $\mu_d=0$ gives $b=10.5$, $\lfloor b\rfloor=10$.)*
11. TENO-S reaches sixth order on the 1D entropy wave: $L_1$ orders 5.617, 5.932, 5.983, 5.995 for $N=8\to20\to40\to80\to100$ at $t=20$, and 5.612, 5.932, 5.982, 5.989 at $t=200$ (Tables 1, 2). **Shown**
12. Sod and 2D Riemann configuration 6 are "not very sensitive" to CFL 0.4, 0.5, 0.6 (Figs. 4, 9). **Shown**
13. Slight overshoots near the Lax contact appear in velocity and pressure, as the authors say they do for other high-order WENO/TENO schemes (§4.2, Fig. 5). **Shown**
14. 1D timings (WENO-CU6 / TENO8 / TENO-S): Sod 32.66/43.87/29.42 ms, Lax 43.55/65.96/33.41 ms (Table 3), Shu–Osher 135.28/218.32/119.59 ms (Table 4), interacting blast waves 953.32/1316.49/912.98 ms (Table 5). **Shown**
15. 2D timings at $800\times800$ (WENO-CU6 / TENO6 / TENO8 / TENO-S): configuration 6 472.48/527.61/600.10/396.89 s, configuration 12 517.96/540.17/628.79/388.08 s ("about 25.07% … 28.15% … 38.28% cheaper"), configuration 16 337.77/375.11/423.21/269.93 s (Tables 6–8). **Shown**
16. Double Mach reflection: 29.42/31.13/36.38/17.42 s at $512\times128$ and 113.30/127.21/156.44/82.60 s at $800\times200$, i.e. "about 40.78% (27.09%) … 44.04% (35.06%) … 52.11% (47.20%) cheaper" (Table 9, §4.6). **Shown** *(Compiler check, not in the sources: the printed percentages are the ratios truncated, not rounded, e.g. 40.79, 25.08, 52.12.)*
17. In the double Mach reflection "more than 90% computational cells are handled by the highly efficient skew-symmetric-splitting scheme" (§4.6). **Stated** (no count shown)
18. At $512\times128$ TENO-S resolves the slip-line vortices better than WENO-CU6, TENO6 and TENO8; WENO-CU6 at $800\times200$ is "even not better" than TENO-S at $512\times128$ (§4.6, Figs. 12–13). **Shown**
19. Rayleigh–Taylor ($64\times256$; 31.78/33.93/38.36/24.59 s) and Kelvin–Helmholtz ($400\times400$; 87.34/100.19/121.72/57.68 s): TENO-S resolves the most small-scale structure at the lowest cost; WENO-CU6 is "much more dissipative" (§§4.7–4.8, Tables 10–11). **Shown**
20. 2D implosion ($600\times600$; TENO6/TENO8/TENO-S 997.53/1207.17/843.20 s): TENO-S keeps the large-scale shock motion and resolves more interfacial instabilities (§4.9, Table 12). **Shown**
21. Inviscid Taylor–Green vortex ($64^3$, to $t=100$): TENO-S "successfully performs long-time stable computations without numerical dissipation by preserving the total kinetic energy", while WENO-CU6, TENO6 and TENO8 smear the small vortices after $t\approx5$ (§4.10, Figs. 17–18). **Shown**
22. Viscous Taylor–Green vortex ($64^3$ for $\mathrm{Re}\le3000$ against Brachet's $256^3$ DNS; $128^3$ for $\mathrm{Re}=5000$, $10^4$ against Dairay's DNS): TENO-S matches the DNS dissipation rates better than the other schemes (§4.11, Figs. 19–20). **Shown**
23. Decaying compressible isotropic turbulence ($M_{t0}=0.6$, $\mathrm{Re}_{\lambda0}=100$, $64^3$): TENO-S predicts the mean-square velocity, density and temperature fluctuations, dilatation and enstrophy better than the other schemes against filtered DNS (§4.12, Fig. 21). **Shown**
24. For the interacting blast waves "the Roe scheme with entropy-fix is employed for flux splitting to obtain a stable result", replacing Rusanov; TENO-S predicts the density peak near $x=0.75$ better and has no pressure overshoot near $x=0.86$, which WENO-CU6 shows (§4.4, Fig. 7). **Shown**
25. Limitation: "numerical difficulties may occur for extreme configurations due to the positivity-preserving problem"; a positivity-preserving limiter is left to future work (§5). **Stated**
26. The skew-split discretization works on physical variables and is "significantly more efficient" than characteristic-space ENO-like reconstruction; the scheme is modular (§2.3, §3.2). **Stated**

# Printed slips

- §2.2.1: the stencil union is printed $\bigcup_{K=0}^{K-3}S_k$, index $K$ for $k$.
- §2.2.1 and Eq. (9) speak of "arbitrary $K$th-order schemes" with $K$ the number of points, while the eight-point scheme is sixth order (Eq. (46)); Eq. (9), $\{3,3,3,4,\dots,\tfrac{K+2}2\}$, must read $\{3,3,3,4,4,5\}$ for $K=8$ (Fig. 1, Eq. (11)).
- §1 cites "total variation diminishing (TVD) schemes [10][11]": ref. [10] ("N.J. Von, R. Richtmyer", J. Appl. Phys. 21 (1950) 232) is ref. [8] (von Neumann & Richtmyer, artificial viscosity) with a mangled author.
- Energy flux, Eq. (30) against Eq. (27) and Algorithm 1 (checked visually on p. 5): Algorithm 1 builds every skew flux from the triple average with $\phi\in\{1,v_1,v_2,v_3,E/\rho\}$, whereas Eq. (30) prints $\mathcal E_{i+1/2}=2\sum_\ell a_\ell\sum_m\tfrac14(E_{i-m}+E_{i-m+\ell})(v_{i-m}+v_{i-m+\ell})$, a double average of $E$ and $v$, plus a separate double-average pressure-work flux $\mathcal K$. *(Compiler check, not in the sources: for $\phi=E/\rho$ the triple average $\tfrac18(\rho_a+\rho_b)(E_a/\rho_a+E_b/\rho_b)(v_a+v_b)$ differs from $\tfrac14(E_a+E_b)(v_a+v_b)$ unless $\rho_a=\rho_b$; for $\phi=1$ the two coincide, as $\mathcal M$ shows.)* Which energy flux the code uses cannot be decided from the paper.
- The final time of the Rayleigh–Taylor test, $t=1.95$, appears only in the Fig. 14 caption.
- Reference list: [70] prints only "P. Woodward" for Woodward & Colella (1984); [25] prints "Y.-X. Ren, H. Zhang, et al."; [27], [38], [43], [59] print no volume.

# Notation map

| Liang & Fu (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $K$, $S_k$, $r_k$ | $K$, $S_k$, $r_k$ | agrees; $K=8$ |
| $\hat f_{k,i+1/2}$ | $\hat f^{(k)}_{i+1/2}$ | candidate fluxes, Eq. (11) |
| $\beta_{k,r}$ | $\beta_k$ | second index = stencil width |
| $\tau_K$ | $\tau_K$ | full-stencil indicator, $O(\Delta x^6)$, as on [TENO](/methods/targeted-eno.md) |
| $\gamma_k$, $q$, $\chi_k$, $\delta_k$, $C_T$ | agrees | Eq. (12) TENO form; **Eq. (32) indicator form $\gamma_k=(\beta_k+\epsilon)^{-6}$ has no $\tau$ and no constant** |
| $C_{T2}$ | kept | indicator threshold $10^{-6}$, smooth if every $\chi_k>C_{T2}$ |
| $\varepsilon$ | $\epsilon$ | $10^{-40}$ (TENO), $10^{-4}/10^{-2}$ (indicator); a third $\varepsilon$ in Eq. (48) |
| $d_k$ | $d_k$ | agrees |
| $w_k$, $\alpha_k$ | $\omega_k$, $\alpha_k$ | $\alpha_k=d_k\delta_k$ |
| $u$ (scalar §2.1), $(u,v,w)$ | $u$, $v=(v_1,v_2,v_3)$ | **$u$ is both the scalar unknown and the velocity in the source** |
| $\phi$, $\boldsymbol\varphi$ | kept | transported quantity per unit mass |
| $a_\ell$, $L$ | kept | central first-derivative coefficients, $L=4$ |
| $b_j$ | kept | symmetric (dissipative) coefficients, Eq. (39) |
| $\hat f^{skew}$, $\mathcal M,\mathcal{MU},\mathcal E,\mathcal K,\mathcal P$ | kept | skew-split interface fluxes, Eqs. (29)–(30) |
| $\xi=wh$, $\tilde\xi_R$, $\tilde\xi_I$ | $\vartheta$, $\tilde\vartheta_r$, $\tilde\vartheta_i$ | reduced and modified wavenumbers; the source writes $j$ for the imaginary unit |
| $v$ (Eq. 41), $p$ (Eq. 42) | kept | objective weight exponent (7) and order index (4); **$v$ collides with velocity, $p$ with pressure** |
| $\zeta$ | kept | dispersion–dissipation ratio, Eq. (45); **$\zeta$ is also the characteristic variable of the registry** |
| $m$, $\eta_i$, $C_r$, $g(m)$, $\alpha_1$, $\alpha_2$, $\beta$ | $\mu_d$, $\sigma_i$, $C_r$, $\varphi(\mu_d)$, $b_1$, $b_2$, $b$ | as on [adaptive TENO](/methods/adaptive-teno.md); **$\eta$ is the entropy, $\beta$ the smoothness indicator in the registry** |
| $\mathbf L$, $\mathbf R$ | $L$, $R$ | Roe-averaged eigenvectors |
| $\lambda^{(m)}_{max}$ | $a$ | per-field maximum speed of Rusanov splitting |

# Reference list

78 printed references in numbered Elsevier style ([1]–[78]), all parsed and merged
complete into the [bibliography](/bibliography.md) with `citedby` `liang-2024-b`.
Ref. [10] duplicates ref. [8] (von Neumann & Richtmyer 1950) under a mangled author
and is merged with it. Ref. [21] (Luo & Wu, WENO-Z+) is the ingested `luo-2021-b`;
refs. [2] (Tsoutsanis & Dumbser, C&F) and [19] (Tsoutsanis et al., CWENO interface
capturing) are mapped to `tsoutsanis-2021-b` and `tsoutsanis-2021` respectively;
the six Fu et al. (2019) works are matched to existing keys by venue. Ref. [34]
(Feiereisen 1981) prints no document type; ref. [61] (Hu et al., arXiv:1204.5088)
is kept as a preprint entry.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunks 8–11 (2026-10-23/24). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Approximate dispersion relation](/definitions/approximate-dispersion-relation.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Entropy filtering for DG and FR](/methods/entropy-filtering.md)
* [Flux differencing and split-form DG](/methods/flux-differencing.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Kinetic energy preservation](/properties/kinetic-energy-preservation.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Roe approximate Riemann solver](/methods/roe-riemann-solver.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [Split convective forms](/methods/split-convective-forms.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [WENO-CU6](/methods/weno-cu6.md)
