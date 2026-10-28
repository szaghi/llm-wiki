---
type: Source
title: "Huang & Fu (2024) — A new troubled cell indicator and a new limiter based on TENO schemes for RKDG methods"
description: "A compact three-cell troubled-cell indicator and a TENO-type moment limiter for third-order modal RKDG, built on TENO's sharp stencil cut-off with one parameter set for all cases; shown on smooth advection and inviscid Euler shock tests against KXRCF and a compact WENO limiter."
resource: "doi:10.1016/j.cma.2024.116795"
source_kind: paper
authors: [Huang H., Fu L.]
year: 2024
venue: "Comput. Methods Appl. Mech. Engrg. 421:116795"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Huang_A_new_troubled_cell_indicator_and_a_new_limiter_based_on_TEN.pdf"
tags: [shock-capturing, dg, high-order, numerical-dissipation, weno]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Huang & Fu (2024) address shock capturing in modal Runge–Kutta discontinuous
Galerkin (RKDG) methods for hyperbolic conservation laws. They name two
weaknesses of current practice: the common troubled-cell indicators (TVB
minmod with its parameter $M$, and KXRCF with its threshold) need case-by-case
tuning, and WENO-type limiters smear small-scale structures. Both new
components borrow the sharp stencil cut-off of targeted ENO (TENO,
[WENO and TENO schemes](/methods/weno-scheme.md)): a candidate is kept with its
optimal linear weight or dropped entirely.

- **Troubled-cell indicator.** For cell $i$ the smoothness indicators of the DG
  polynomials on cells $i-1$, $i$, $i+1$ are turned into TENO smoothness
  measures; the cell is troubled when its own normalized measure falls below
  the cut-off $C_T=10^{-4}$. One parameter set is used in every test. In 2D the
  test runs direction by direction. This is one of the TENO-based
  troubled-cell indicators of the
  [shock-sensor](/definitions/shock-sensor.md) page.
- **TENO limiter.** In troubled cells the cell average is kept and the higher
  moments are rebuilt from three compact candidate polynomials (1D) or eight
  Hermite-WENO stencils (2D), with TENO weights that favour the central or
  large stencils by a factor 10.

Only flagged cells are limited; the rest run standard RKDG with polynomial
degree $N=2$, third-order SSP Runge–Kutta, CFL 0.15 and the Rusanov flux. The
method is a modal-RKDG limiter route, distinct from the nodal
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) and from
the [subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
and [artificial-viscosity](/methods/artificial-viscosity-shock-capturing.md)
treatments of troubled elements. The tests are inviscid Euler only: smooth 1D
and 2D advection (the indicator never fires; the limiter keeps third order
when TVB forces limiting), Sod and Lax tubes, Woodward–Colella blast waves,
Shu–Osher, double Mach reflection and the 2D Riemann problem configuration 3.
On the shock tests the authors report fewer and better-placed troubled cells
than KXRCF and more small-scale structure than the compact WENO limiter of
Zhu, Qiu & Zhu (2020); this evidence on
[numerical dissipation](/properties/numerical-dissipation.md) is visual only.
The paper has no turbulence case: turbulence enters as motivation.

# Version read

Version of record (Elsevier typeset; received 2 November 2023, accepted
20 January 2024, online 25 January 2024), 24 pages, all read; pp. 6, 7, 10
and 11 checked visually for Eqs. 26–41 and 56–60. Page 1 matches Crossref
(title, two authors, venue, DOI). No identity problem.

# Key claims

Notation: $\mathrm{IS}_k$ smoothness indicator, $\gamma^{\mathrm T}_k$ TENO
smoothness measure, $\chi^{\mathrm T}_k$ its normalized value,
$\delta^{\mathrm T}_k$ the 0/1 cut-off flag, $d_k$ optimal linear weights,
$\mathsf w_k$ nonlinear weights, $t_k$ stencil-favouring factor, with $k$ the
candidate (stencil or cell) index, and $N_x$ number of cells (see the Notation
map; all of them are registry §11 symbols except $t_k$, which is
page-local).

1. TVB minmod and KXRCF indicators rely on a critical parameter ($M$, or the KXRCF threshold) that depends on the solution and needs case-by-case tuning (§1, §4.1–4.2). **Stated**
2. The new indicator works with one parameter set for all cases: exponent 6, regulariser $10^{-3}$ and $C_T=10^{-4}$, "taken as $10^{-4}$ without tuning for all simulations in this work" (§4.3, Eqs. 33–35). **Shown**
3. The new indicator is compact, using only cells $i-1$, $i$, $i+1$; Fu's finite-difference discontinuity indicator needs four candidate stencils with six points in total (§4.3). **Stated**
4. For the 1D $N=2$ limiter the optimal linear weights recovering the quartic-polynomial first moment are $d_0=d_1=11/38$, $d_2=8/19$ (Eq. 40). **Derived**
5. For the second moment (cubic candidates, quintic target) the weights are $d_0=d_1=45/154$, $d_2=32/77$ (Eq. 49). **Derived**
6. In 2D the eight HWENO candidate stencils carry $d^{(l)}_{1..4}=11/76$ and $d^{(l)}_{5..8}=2/19$ for the first moments ($l=1,2$), and $d^{(l)}_k=1/8$ for the mixed and second moments ($l=3,4,5$); uniqueness is imposed by minimizing $\sum_k(d^{(l)}_k)^2$ (Eqs. 56–58). **Derived**
7. The central or large stencils are boosted with $t_k=10$ in $\gamma^{\mathrm T}_k=t_k/(\mathrm{IS}_k+\epsilon)^6$, "to enlarge the chance to choose the central stencil" ($t_2=10$ in 1D, Eq. 42; $t_{5..8}=10$ in 2D, Eq. 60) (§4.4). **Stated**
8. For the mixed and second moments the 2D smoothness indicators add first-derivative terms absent from the HWENO limiter, "for better robustness" (§5.2, Eq. 59; §7). **Stated**
9. The limiter keeps the cell average unchanged, so it is conservative (§4.4, §5.2). **Stated**
10. TENO components act only in the indicator and the limiter; unflagged cells run the standard RKDG method (§4.4). **Stated**
11. On smooth 1D Euler advection ($N_x=100$ to $800$, $t=1$) RKDG with WENO, with the new limiter and with no limiter give identical errors ($L_1=6.94\times10^{-10}$ at $N_x=800$, order 3.00), so the new indicator activates no limiter (Table 1). **Shown**
12. On the same test the TVB minmod indicator "may activate limiters" at smooth extrema (§6.1.1, citing [17]). **Stated**
13. With TVB at $M=1$ forcing limiting, the new limiter converges at third order: at $N_x=400$, $L_1=5.58\times10^{-9}$ (order 3.01) and $L_\infty=8.71\times10^{-9}$ (order 3.00) (Table 2). **Shown**
14. On 2D smooth Euler advection ($20^2$ to $160^2$, $t=2$) the three schemes give identical errors ($L_1=2.46\times10^{-7}$ at $160^2$, order 2.99) (Table 3); with TVB at $M=1$ the new limiter reaches $L_1=2.49\times10^{-7}$ (order 2.99) (Table 4). **Shown**
15. KXRCF's activation in accuracy tests depends on its parameter and the mesh, so TVB is used for order verification, "since it always labels some troubled cells regardless of its parameter" (§6.1.1). **Stated**
16. Sod and Lax ($N_x=100$): the new indicator locates troubled cells "much more precisely" than KXRCF, and the new limiter is non-oscillatory and less dissipative than WENO (Figs. 4–5, §6.2). **Shown** (visual)
17. Woodward–Colella blast waves ($N_x=400$, $t=0.038$): both schemes are robust and the new limiter gives "much better results than WENO" in zoomed views (Fig. 6, §6.3). **Shown** (visual)
18. Shu–Osher ($N_x=200$, $t=1.8$): the new limiter resolves the high-wavenumber fluctuations "substantially better" than WENO; these under-resolved fluctuations (about $x=5.6$ to $7.2$) must be flagged, and KXRCF misses them while the new indicator flags them (Fig. 7, §6.4). **Shown** (visual)
19. Double Mach reflection ($1000\times250$ and $1500\times375$, $t=0.2$): the new indicator is "much more precise than the KXRCF indicator with less noise", and the new limiter resolves "much richer small-scale structures" than WENO (Figs. 8–11, §6.5). **Shown** (visual)
20. 2D Riemann problem configuration 3 ($700^2$ and $1000^2$, $t=0.3$): KXRCF labels over 50% of the cells as troubled, so its distributions are not plotted; the new indicator gives "satisfactory results" and the new limiter more small-scale structure than WENO (Figs. 12–15, §6.6). **Shown** (visual)
21. Both schemes give asymmetric 2D Riemann solutions, attributed to low numerical dissipation failing to damp round-off disturbances (§6.6, citing [66,67]). **Stated**
22. Extension to 3D has "no obvious theoretical barriers" and is ongoing; RKDG cost grows with the number of basis functions and the small CFL number; unstructured meshes are planned (§7). **Stated**
23. TENO-family schemes have better robustness and lower dissipation than WENO and have been applied to gas dynamics, multiphase flow, MHD, detonation, fluid–structure–acoustics and turbulence [38–53] (§1). **Stated**

# Printed slips

- **Eq. 38, fourth line:** printed
  $\int_{I_i}q\,v_1\,dx=c_1\big(\tfrac{15}{19}(u^{(0)}_{i-1}-u^{(0)}_{i+1})-\tfrac{11}{38}(u^{(1)}_{i-1}+u^{(1)}_{i+1})\big)$
  (sign checked visually, p. 7). For linear data ($u^{(0)}_m=m$, $u^{(1)}_m=1$ in units of the cell size) the printed form gives $-41/19$ instead of $1$, and $\sum_kd_k\int p_kv_1$ with the printed $p_k$ lines and Eq. 40 weights gives the averages' difference as $u^{(0)}_{i+1}-u^{(0)}_{i-1}$ *(compiler check, not in the sources)*.
- **Table 2, new limiter, $N_x=50$:** $L_\infty$ printed $5.38\times10^{-7}$, smaller than the row's $L_1=3.02\times10^{-6}$ and than the $N_x=100$ value $5.56\times10^{-7}$, yet the printed $N_x=100$ order is 3.27; $\log_2(5.38\times10^{-6}/5.56\times10^{-7})=3.27$, so the printed order matches $5.38\times10^{-6}$ *(compiler check, not in the sources)*.
- **Eq. 56** imposes exactness "for $u=v_1^{(ij)},v_2^{(ij)},\dots,v_9^{(ij)}$", but the $N=2$ basis of Eq. 21 and Eq. 51 has only $v_0,\dots,v_5$; $v_6,\dots,v_9$ are never defined.
- **Ref. [63]** prints only "P. Woodward", while §6.3 says "Woodward and Colella [63]".
- Typos and gaps: "Dentisy" on the axes of Figs. 4–7; "withobstacles" in ref. [56]; ref. [5] prints only "Acta Mech. Sin. 4 (2024)"; refs. [12] and [29] print no volume.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k$ (DG degree), $P^k$, $(k+1)$th order | $N$, $P^N$, order $N+1$ | tests use $k=2$ |
| $N$, $N_x\times N_y$ (cells) | $N_x$, $N_x\times N_y$ | **collision** with the polynomial degree $N$ |
| $\Delta x$, $\Delta y$ | $h$ (cell size) | $\Delta$ is the filter width in the registry |
| $\beta_n$, $\beta_{n,r}$, $\beta_n^{(l)}$ | $\mathrm{IS}_k$, $\mathrm{IS}_k^{(l)}$ | the source's stencil index $n$ is written $k$ throughout (the source's $k$, the DG degree, is $N$ here); **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $\gamma_n$ | $\gamma^{\mathrm T}_k$ (TENO smoothness measure, registry §11) | **collision** with the ratio of specific heats $\gamma=1.4$ used in §6 |
| $\chi_n$ | $\chi^{\mathrm T}_k$ (registry §11) | **collision** with the SA ratio $\chi=\tilde\nu/\nu$ |
| $\delta_n$ | $\delta^{\mathrm T}_k$ (0/1 cut-off flag, registry §11) | **collision** with the boundary-layer thickness |
| $C_T$ | $C_T$ (TENO cut-off) | $10^{-4}$ here; "usually $10^{-5}$" for finite-volume TENO5 (§2) |
| $C$, $q$, $\tau_K$, $\tau_5$ | (TENO constants, exponent, global smoothness reference) | $q=6$; $\tau_K$ **collides** with the SGS stress |
| $\varepsilon$, $\varepsilon_1$, $\varepsilon_2$ | $\epsilon$ (regularisers, page-local) | $10^{-40}$, $10^{-3}$, $10^{-10}$; **collision** with the dissipation rate $\varepsilon$ |
| $d_n$, $d_n^{(l)}$; $w_n$ | $d_k$, $d_k^{(l)}$ (registry §11); $\mathsf w_k$ | optimal linear and nonlinear weights |
| $t_n$ | $t_k$ (page-local) | 1 or 10 |
| $u_i^{(l)}$, $u_{ij}^{(l)}$; $v_l^{(i)}$; $c_l$, $a_l$ | (DG moments, scaled Legendre basis, basis norms) | modal DG; $a_l$ unrelated to split-form weights |
| $p_n$, $q$ | $p_k$, $q$ (candidate and target reconstruction polynomials, page-local) | $q$ also the exponent 6 |
| $M$; $I_i^{KXRCF}$, $h$ (KXRCF) | $M_{\mathrm{TVB}}$ (TVB parameter, page-local as on [shock sensors](/definitions/shock-sensor.md)); $I^{\mathrm{KXRCF}}_i$, (circumscribed radius) | KXRCF's $h$ **collides** with the registry's cell size |
| $\hat f_{i+1/2}$ | $f^*$ (interface numerical flux) | Rusanov in all tests |
| $\rho,u,v,p,E$; $\gamma$ | $\rho$, $u$, $v$, $p$, $E$; $\gamma=1.4$ | Euler variables |

# Reference list

67 printed references in numbered Elsevier style, no DOIs printed; merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Same-author same-year works take suffixes in printed order (Cockburn 1989,
Qiu 2005, Zhu 2020 — J. Zhu and H. Zhu —, six Fu 2019 papers, Fu 2022).
Ref. [39] (Li, Fu & Adams 2021, J. Comput. Phys. 428:109960) is a different work from the ingested source [Li et al. (2021)](/sources/li-2021.md) and is keyed `li-2021-h`; ref. [36] is
[Takagi et al. (2022)](/sources/takagi-2022.md). Incomplete items: [5] (no
volume or pages beyond "4 (2024)"), [12] and [29] (no volume), [63] (one
author only). No printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
