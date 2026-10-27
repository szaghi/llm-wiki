---
type: Source
title: "Liang & Fu (2024) — A new high-order shock-capturing TENO scheme combined with skew-symmetric-splitting method for compressible gas dynamics and turbulence simulation"
description: "TENO-S: a hybrid finite-difference scheme that switches, by a new eight-point discontinuity indicator, between a dispersion-optimized sixth-order kinetic-energy-preserving split flux and an adaptive-dissipation eight-point TENO; inviscid TGV energy conservation, viscous TGV and compressible isotropic turbulence at lower cost."
resource: "doi:10.1016/j.cpc.2024.109236"
source_kind: paper
authors: [Liang T., Fu L.]
year: 2024
venue: "Comput. Phys. Commun. 302:109236"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Computer_Physics_Communications_Liang_A_new_high-order_shock-capturing_TENO_scheme_combined_with_s.pdf"
tags: [shock-capturing, kinetic-energy-preserving, numerical-dissipation, implicit-les, compressible, weno]
timestamp: 2026-10-27T06:09:00Z
---

# Summary

Liang & Fu (2024) propose TENO-S, a hybrid conservative finite-difference
scheme on Cartesian meshes, against two weaknesses of WENO/TENO shock
capturing in compressible turbulence: the cost of characteristic
decomposition and nonlinear weights at every interface, and the
[numerical dissipation](/properties/numerical-dissipation.md) of the upwind
background scheme, which prevents long-time non-dissipative runs of smooth
flows because quadratic invariants such as the kinetic energy are not
conserved.

- **Eight-point discontinuity indicator.** Six equal-sized three-point
  stencils over $x_{i-3},\dots,x_{i+4}$ give TENO-like smoothness measures
  of conserved variables in physical space (density and total energy in 1D,
  density in multi-D); a cell is troubled when any normalized measure falls
  below $C_{T2}=10^{-6}$. It is the eight-point indicator of the
  [shock-sensor](/definitions/shock-sensor.md) page, claimed more general
  than the Ducros sensor.
- **Smooth cells** take a non-dissipative skew-symmetric split flux: the
  Kennedy–Gruber cubic split form in Pirozzoli's locally conservative flux
  form, extended to eight points, with central coefficients optimized for
  dispersion under a sixth-order constraint
  ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
- **Troubled cells** take an eight-point TENO reconstruction in
  characteristic space (Roe eigenvectors, Rusanov splitting) whose background
  linear scheme is optimized for dispersion with a small dissipation
  ($e_0=0.01$, by the approximate dispersion relation of
  [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)),
  and whose cut-off $C_T$ adapts between $10^{-10}$ and $10^{-7}$ with a
  discontinuity-strength measure ([WENO and TENO](/methods/weno-scheme.md)).

The tests are the 1D entropy wave (sixth order), Sod, Lax, Shu–Osher,
blast waves, three 2D Riemann problems, double Mach reflection, a
single-mode inviscid Rayleigh–Taylor instability (a shock-capturing test, not
the mixing-layer turbulence of
[Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)),
Kelvin–Helmholtz, a 2D implosion, the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $64^3$ to $t=100$,
the viscous Taylor–Green vortex at $Re=100$ to $10000$ against
[DNS](/definitions/direct-numerical-simulation.md), and decaying compressible
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at
$M_t=0.6$, $Re_\lambda=100$ on $64^3$ against filtered DNS. The turbulence
runs have no subgrid model ([implicit LES](/definitions/implicit-les.md)).
TENO-S conserves kinetic energy in the inviscid Taylor–Green vortex, agrees
better with the references than WENO-CU6, TENO6 and TENO8, and is cheaper in
every printed timing (the percentages printed for the 2D Riemann
configuration 12 and the double Mach reflection range from 25.07% to
52.11%). Artificial viscosity appears only in the
introduction's list of shock-capturing families
([artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)).

# Version read

Version of record (Elsevier typeset, Comput. Phys. Commun. 302 (2024)
109236; received 6 October 2023, accepted 6 May 2024), 28 pages, all read;
pp. 3, 4, 5, 7 and 8 checked visually for Eqs. 9–16, 26–30 and 36–49. Page 1
matches Crossref. The paper's own ref. [47] (Liang & Fu, J. Comput. Phys.
497:112618, 2024) is a different work and takes a distinct bibliography key.
A C++ implementation of Algorithm 1 is printed as public.

# Key claims

Notation: $\gamma^{\mathrm T}_k$ TENO smoothness measure, $\chi^{\mathrm T}_k$ its
normalized value, $\delta^{\mathrm T}_k$ the cut-off flag, $\mathrm{IS}_k$
smoothness indicators, $d_k$ optimal weights, $c_\ell$ centred-derivative coefficients, $e_0$
dissipative coefficient,
$\mathcal K(t)$ and $\mathcal E_\omega(t)$ volume-integrated kinetic energy
and enstrophy (page-local; Notation map).

1. Classical shock-capturing schemes cannot run long-time stable non-dissipative simulations because the dissipation of the upwind background linear scheme prevents conservation of quadratic invariants such as kinetic energy; example the inviscid Taylor–Green vortex (§1, §3.2). **Stated**
2. Central finite differences of the inviscid equations tend to become unstable through accumulation of aliasing errors of the nonlinear convective terms, attributed to non-preservation of quadratic invariants (§1, refs. [31]–[33]). **Stated**
3. Divergence, quadratic-split (Feiereisen, Eq. 22) and cubic-split (Kennedy–Gruber, Eq. 23) forms are analytically equivalent but differ after discretization; the cubic split gives stronger robustness (§2.3). **Stated**
4. Pirozzoli's interface flux (Eq. 26) recovers the second-order cubic split form (Eq. 24), and the form extends to arbitrary order through Eq. 27 with maximum order $2L$ (§2.3). **Stated** ("it can be shown")
5. The eight-point indicator uses six equal-sized three-point stencils (Fig. 2), which reduces the cost of smoothness indicators of large stencils (§3.1, Eqs. 31–34). **Derived** (construction)
6. The indicator separates non-smooth from smooth scales "in the wavenumber space" and is "more universal for general conservation laws" than physical-variable sensors such as the Ducros sensor (§3.1). **Stated** (no comparison with the Ducros sensor is run)
7. Because characteristic-space TENO is used only in troubled cells and the indicator works on conserved variables in physical space, TENO-S is much cheaper than plain ENO/WENO/TENO (§3.2, Algorithm 1; Tables 3–12). **Shown**
8. In the double Mach reflection more than 90% of the cells use the split flux (§4.6). **Stated** (no count printed)
9. The optimized split scheme is sixth-order with $c_1=0.8441336457279522$, $c_2=-0.2441336457279522$, $c_3=0.0570096576929319$, $c_4=-0.006723831837710873$, and non-dissipative because only the dispersive part fixes $c_\ell$ (§3.3.1, Eqs. 40–42). **Derived**
10. The background linear scheme of the eight-point TENO (Eq. 46) is sixth-order with dissipation coefficient $e_0=0.01$, chosen so that the approximate dispersion relation ratio is about 10 (§3.3.1, Eqs. 43–46). **Derived**
11. Adaptive dissipation: $C_T\to10^{-7}$ where the discontinuity strength is near 1 (robust shock capturing) and $C_T\approx10^{-10}$ where it is near 0 (low-dissipation resolution of high-wavenumber fluctuations) (§3.3.2, Eqs. 47–49). **Derived**
12. TENO-S reaches sixth order on the 1D entropy wave: $L_1$ orders 5.617, 5.932, 5.983, 5.995 at $N_x=20,40,80,100$ ($t=20$) and 5.612, 5.932, 5.982, 5.989 ($t=200$) (§4.1, Tables 1–2). **Shown**
13. Sod and Lax ($N_x=100$): all schemes agree with the exact solution; TENO-S shows slight over/undershoots near the contact, also present in other WENO/TENO schemes; results are "not very sensitive" to CFL 0.4–0.6 (§4.2, Figs. 3–5). **Shown**
14. Shock-tube cost (WENO-CU6 / TENO8 / TENO-S): Sod 32.66 / 43.87 / 29.42 ms, Lax 43.55 / 65.96 / 33.41 ms (Table 3). **Shown**
15. Shu–Osher ($N_x=200$): TENO-S captures the shock as sharply as WENO-CU6 and TENO8 and resolves the density fluctuations better than WENO-CU6; cost 135.28 / 218.32 / 119.59 ms (§4.3, Fig. 6, Table 4). **Shown**
16. Blast waves ($N_x=400$): TENO-S better predicts the density peak near $x=0.75$ and has none of WENO-CU6's pressure overshoots near $x=0.86$; cost 953.32 / 1316.49 / 912.98 ms; this case switches the flux splitting to Roe with entropy fix "to obtain a stable result" (§4.4, Fig. 7, Table 5). **Shown**
17. 2D Riemann problems at $800^2$: TENO-S resolves more vortical structure than WENO-CU6, TENO6 and TENO8; costs (WENO-CU6/TENO6/TENO8/TENO-S, s): configuration 6 472.48/527.61/600.10/396.89, configuration 12 517.96/540.17/628.79/388.08, configuration 16 337.77/375.11/423.21/269.93 (§4.5, Figs. 8–11, Tables 6–8). **Shown**
18. Double Mach reflection: at $512\times128$ TENO-S resolves the slip-line vortices better than the other three schemes, and WENO-CU6 at $800\times200$ is "even not better than" TENO-S at $512\times128$; TENO-S is 40.78% (27.09%) cheaper than WENO-CU6, 44.04% (35.06%) than TENO6 and 52.11% (47.20%) than TENO8 on the coarse (fine) grid (§4.6, Figs. 12–13, Table 9). **Shown**
19. Rayleigh–Taylor instability ($64\times256$): TENO-S captures more small-scale structure; cost 31.78/33.93/38.36/24.59 s (§4.7, Fig. 14, Table 10). **Shown**
20. Kelvin–Helmholtz ($400^2$, $t=0.5$): WENO-CU6 is much more dissipative; cost 87.34/100.19/121.72/57.68 s (§4.8, Fig. 15, Table 11). **Shown**
21. 2D implosion ($600^2$, $t=0.7$): TENO-S has the same large-scale shock structure as TENO6 and TENO8 and more interfacial instability; cost (TENO6/TENO8/TENO-S) 997.53/1207.17/843.20 s (§4.9, Fig. 16, Table 12). **Shown**
22. Inviscid 3D Taylor–Green vortex ($64^3$, to $t=100$): TENO-S "successfully performs long-time stable computations without numerical dissipation by preserving the total kinetic energy and capturing the enstrophy growth"; WENO-CU6, TENO6 and TENO8 dissipate $\mathcal K$ and smear small vortices after $t\approx5$ (§4.10, Figs. 17–18). **Shown**
23. Viscous Taylor–Green vortex: TENO-S at $64^3$ ($Re=100$ to $3000$) and $128^3$ ($Re=5000$, $10000$) "performs significantly better than other state-of-the-art schemes" and agrees with the DNS of Brachet et al. ($256^3$) and Dairay et al. ($1280^3$, $2048^3$) for the dissipation rate on a coarse mesh (§4.11, Figs. 19–20). **Shown**
24. Decaying compressible isotropic turbulence ($M_t=0.6$, $Re_\lambda=100$, $64^3$): TENO-S predicts mean-square velocity, density fluctuation, dilatation, enstrophy and temperature fluctuation "significantly better than other considered schemes", in agreement with filtered $256^3$ DNS (§4.12, Fig. 21). **Shown**
25. All cases use the recommended parameters "without parameter tuning case by case" (abstract, §4). **Stated** — the paper itself prints the indicator regulariser as $10^{-4}$ in 1D and $10^{-2}$ in multi-D (Eq. 32), the indicator variables as density and energy in 1D and density in multi-D (§3.1), and the Roe-with-entropy-fix splitting for the blast waves (§4.4).
26. TENO-S is robust for conventional high-Mach gas-dynamics benchmarks and typical turbulence, but positivity problems may occur in extreme configurations; a positivity-preserving limiter is left to future work (§5). **Stated**

# Printed slips

- **§2.2.1:** the stencil union is printed $\bigcup_{K=0}^{K-3}S_k$; the running index should be lower-case $k$ (p. 3).
- **Refs. [8] and [10]** are the same work (von Neumann & Richtmyer, J. Appl. Phys. 21, 1950); [10] prints the first author as "N.J. Von" and is cited in the text as a TVD reference ("total variation diminishing (TVD) schemes [10][11]").
- **Cost percentages** of §4.5–4.6 are truncated, not rounded, from Tables 8–9 (e.g. $1-17.42/29.42=40.79\%$, printed 40.78%) *(compiler check, not in the sources)*.
- Gaps, not slips: the Rayleigh–Taylor final time is printed only in the Fig. 14 caption ($t=1.95$); the isotropic-turbulence $k_0$ and final time are delegated to Johnsen et al. [78]; the viscous Taylor–Green Mach number and Reynolds-number definition are not printed.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf U=[\rho,\rho u,\rho v,\rho w,E]$, $E$ | $\rho$, $\rho\boldsymbol u$, $E$ (total energy per unit volume) | |
| $\gamma$ | $\gamma$ | 1.4; 5/3 in the Rayleigh–Taylor case |
| $\gamma_k$ | $\gamma^{\mathrm T}_k$ (TENO smoothness measure, page-local) | **collision** with $\gamma$ |
| $\chi_k$; $\delta_k$ | $\chi^{\mathrm T}_k$; $\delta^{\mathrm T}_k$ (page-local) | **collisions** with the SA $\chi$ and the boundary-layer thickness |
| $\beta_{k,r}$ | $\mathrm{IS}_k$ | smoothness indicator of stencil $k$, width $r$ |
| $w_k$, $\alpha_k$, $d_k$ | $\mathsf w_k$, $a_k$, $d_k$ | nonlinear, unnormalized, optimal weights; $\alpha_k$ **collides** with the modelled-energy fraction |
| $C_T$, $C_{T2}$ | (TENO cut-off; indicator cut-off) | $10^{-10}$–$10^{-7}$ adaptive; $10^{-6}$ |
| $\tau_K$ | (global smoothness reference) | **collision** with the SGS stress |
| $K$ (points of the reconstruction) | $n_{\mathrm{pt}}$ (page-local) | eight points; **collision** with the spectral-page kinetic energy |
| $\varepsilon$ | $\epsilon$ (regularisers, page-local) | $10^{-40}$, $10^{-4}$/$10^{-2}$, Eq. 48 form; **collision** with the dissipation rate |
| $a_\ell$, $L$ | $c_\ell$ (centred-derivative coefficients, page-local, as on the low-dissipation and kinetic-energy pages), $L$ half-width | $a_\ell$ **collides** with the unnormalized WENO weight $a_k$; **collision** of $L$ with the integral scale |
| $b_j$ | $e_j$ (symmetric dissipative coefficients, page-local) | $e_0=0.01$ |
| $\delta/\delta x$ | $D_x$ | discrete derivative |
| $\hat f_{i\pm1/2}$ | $f^*$ | interface numerical flux; hat is not a test filter |
| $m$, $\eta_i$, $C_r$, $g(m)$, $\alpha_1$, $\alpha_2$, $[\beta]$ | $m$, $\varrho_i$, $C_r$, $g(m)$, $A_1$, $A_2$, $\lfloor b\rfloor$ (discontinuity strength, local ratio, threshold 0.23, mapping, 10.5, 3.5, floor; page-local, as on the WENO page) | |
| $E$ (Eq. 41), $v$, $p$ (Eq. 42) | (dispersion objective, weighting exponent 7, order parameter 4) | **collisions** with energy, velocity, pressure |
| $\zeta$ | (approximate-dispersion-relation ratio, about 10) | **collision** with the feature vector $\boldsymbol\zeta$ |
| $K(t)$, $\Omega(t)$ | $\mathcal K(t)$, $\mathcal E_\omega(t)$ (page-local) | **collision** of $\Omega$ with the rotation-rate tensor |
| $M_{t0}$, $Re_{\lambda0}$, $\lambda$ | $M_t$, $Re_\lambda$, $\lambda$ (initial values) | $\lambda$ printed "$=0.5$" |
| $N$ (cells) | $N_x$ | |

# Reference list

78 printed references in numbered Elsevier style; merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Refs. [8] and [10]
are one work printed twice (von Neumann & Richtmyer 1950; [10] garbled) and are folded into one entry, `vonneumann-1950`; refs. [9] and [11] are the conference (1993) and
journal (1994) versions of Jameson's paper, kept distinct. Ref. [47] (Liang &
Fu 2024, J. Comput. Phys. 497:112618) is keyed `liang-2024-b`, distinct from this slug.
Same-author same-year works take suffixes in printed order (Tsoutsanis 2021,
Pirozzoli 2011, six Fu 2019 papers). Items without volume or page: [3], [27],
[38], [43], [59]; [61] is an arXiv preprint (Hu et al., arXiv:1204.5088);
[25] and [78] print "et al.".

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Rayleigh–Taylor mixing](/benchmarks/rayleigh-taylor-mixing.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
