---
type: Source
title: "Petrocchi & Barakos (2024) — Transonic buffet simulation using a partially-averaged Navier-Stokes approach"
description: "Applies SST-based partially-averaged Navier–Stokes with a dynamic, grid-dependent unresolved-energy ratio to transonic buffet on the OAT15A aerofoil in a half wind tunnel; PANS predicts buffet and stall cells where URANS converges to a steady state, at about 3% more cost per step."
resource: "doi:10.1016/j.ast.2024.109134"
source_kind: paper
authors: [Petrocchi A., Barakos G.]
year: 2024
venue: "Aerosp. Sci. Technol. 149:109134"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Aerospace_Science_and_Technology_Petrocchi_Transonic_buffet_simulation_using_a_partially-averaged_Navie.pdf"
tags: [pans, hybrid-rans-les, rans, compressible, separated-flow]
timestamp: 2026-10-26T10:25:00Z
---

# Summary

Petrocchi & Barakos (2024) test whether
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
in its [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) form can predict
transonic buffet, the self-sustained shock oscillation of a
[shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
with shock-induced separation, on the ONERA OAT15A supercritical aerofoil
at $M_\infty=0.73$, $Re_c=3\times10^6$, at a cost close to URANS. Unlike
most earlier computations of the case (two-dimensional or short-span
periodic, unconfined), they model half of the S3Ch wind tunnel, with slip
upper and lower walls shaped to mimic the adaptive walls and a no-slip side
wall, so that the wing–wall junction separation and three-dimensional
structures can develop. The solver is the Glasgow HMB3 code.

PANS, a [hybrid RANS/LES](/definitions/hybrid-rans-les.md) bridging method
whose eddy viscosity keeps the [Boussinesq](/definitions/boussinesq-hypothesis.md)
form reduced through $f_k$, is run with $f_\varepsilon=1$ and a dynamic
$f_k$, recomputed every step from the modelled length scale
$L_t=\sqrt{k_u}/(C_\mu\omega_u)$ and the local grid size, either as a power
law with a calibrated constant or as a tanh blending attributed to
Elmiligui et al., clipped from below and set to one in the blocks next to
the side wall. At $\alpha=2.5°$ PANS recovers URANS; at $\alpha=3.5°$
three-dimensional URANS converges to a steady state, while PANS predicts
buffet on all three grids. On the finest grid (about 16.7 M cells) it
captures stall cells and an undulating shock front consistent with the
oil-flow and schlieren images, mean and RMS pressures and velocity profiles
agree well, and the buffet frequency is 50–60 Hz against 69 Hz measured.
The results depend on the tunnel back pressure, the trip location and the
lower clip of $f_k$. PANS is presented as usable on RANS-like grids,
against [DES-family](/methods/detached-eddy-simulation.md) methods whose
LES mode brings back the [LES grid requirements](/results/les-grid-point-requirements.md)
and the time-step demands of [LES](/definitions/large-eddy-simulation.md).
Appendices compile earlier URANS predictions of the case, in which
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) runs mostly miss the
oscillation and solvers such as [elsA](/software/elsa.md) appear, and
classify about forty PANS studies by constant, static or dynamic $f_k$.

# Version read

Version of record (Elsevier; received 29 May 2023, accepted 8 April 2024),
19 pages, all read; equation pages checked visually. Page 1 matches the
Crossref record. Ref. [71] is the authors' ECCOMAS 2022 conference paper
with the same title, a distinct work. Equation, section, figure, table and
appendix numbers on this page are those of the version of record.

# Key claims

Page-local symbols: $L_t=\sqrt{k_u}/(C_\mu\omega_u)$ the modelled
turbulent length scale; $h$ the local grid size (the source's $\Delta$);
$C_{\mathrm{PANS}}$ the constant of Eq. (6); $f_{k,\min}$ the lower clip
of $f_k$ (printed $f_{k,\rm inf}$ in Table 2 and $f_{k,min}$ in Fig. C.20); $t_{ku}$ the "unresolved Kolmogorov time scale" of Eq. (8); BP
the outlet-to-inlet pressure ratio; SIO shock-induced oscillation.

1. In the three-dimensional confined configuration at $\alpha=3.5°$, URANS (SST) converges to a steady state, while PANS predicts SIO (§4.5.5; Table 2, runs U3C35a/b "No" against P3C35a–P3F35 "Yes"). **Shown**
2. The URANS failure is attributed to excessive corner separation, which deviates the trailing-edge flow spanwise and keeps the shock-foot and trailing-edge separations from merging, and to too high a post-shock eddy viscosity (§4.5.5). **Stated** (interpretation of shown fields)
3. In two dimensions SST URANS predicts no buffet even at $\alpha=3.9°$ (run U2M39), while PANS with constant $f_k=0.7$ does (P2M35a/b, P2M39) (§4.3, Table 2). **Shown**
4. At the statistically steady $\alpha=2.5°$ PANS recovers the URANS solution within a tolerance; the shock position depends slightly on the grid because the grid-dependent $f_k$ of Eq. (7) is lower on finer grids, reducing the eddy viscosity and promoting separation (§4.4, Figs. 4–5). **Shown**
5. The two $f_k$ estimates, Eq. (6) $f_k=C_{\mathrm{PANS}}(h/L_t)^{2/3}$ and Eq. (7) $f_k=\tfrac12[1+\tanh(2\pi(\Lambda-0.5))]$ with $\Lambda=[1+(L_t/h)^{4/3}]^{-1}$, give similar distributions; Eq. (7) is preferred because it needs no calibrated constant, leaves RANS slightly later in the boundary layer, and is bounded in $[0,1]$, whereas Eq. (6) can exceed one in the far field (§2.1, §4.5.1, Fig. 6). **Shown**
6. An earlier study of the authors [71] found $C_{\mathrm{PANS}}=0.5$ optimal for this configuration and grid size; larger values removed the centreplane boundary-layer separation and overpredicted the corner separation; $C_{\mathrm{PANS}}$ is reduced from the static value $1/\sqrt{C_\mu}$ because $L_t$ is built from unresolved quantities (§2.1, §4.5.1). **Stated**
7. Constant $f_k$ needs a sensitivity study and is unreasonable with confined high-turbulence regions and anisotropic grids; static $f_k$ suits localized statistically steady turbulence; the dynamic approach "is required" for intrinsically unsteady flows such as buffet (§2.1). **Stated**
8. Lowering the tunnel back pressure (BP $=0.99$ against 1) increases the shock-oscillation amplitude and the pressure RMS over the whole section; the 1% drop is motivated by Thiery & Coustols [37] (§4.5.2, Fig. 7). **Shown**
9. The coarse grid C3 cannot resolve three-dimensional structures in the separated layer; the medium grid M3 resolves mainly spanwise trailing-edge shedding; the fine grid F3, with half the time step, reproduces the experimental topology with stall cells (§4.5.3, Fig. 8). **Shown**
10. On finer grids the mean shock moves slightly upstream, fluctuation levels rise and the mean $C_p$ agreement improves; the residual gap is $\Delta C_p<0.06$ (suction side) and $<0.08$ (pressure side), attributed to the unknown experimental set-up and adaptive-wall shape (§4.5.3, Fig. 9). **Shown**
11. Mean and RMS streamwise velocity agree well with LDV at $x/c=0.28$, 0.45, 0.6, 0.75, except that the RMS at $x/c=0.28$ is practically zero because the boundary-layer fluctuations are not resolved, and the RMS peak at $x/c=0.45$ differs owing to the slightly upstream shock (§4.5.4, Figs. 10–11). **Shown**
12. Buffet cycle on F3: at the most downstream shock position the flow is attached and the shock strengthens until shock-foot separation; trailing-edge separation follows from the reduced eddy viscosity; the two regions merge near the centreline into a vortical structure; trailing-edge disturbances drive the shock upstream; the structures spread spanwise into large stall cells and a non-uniform shock front; near the most upstream position the shock weakens and the flow reattaches (§4.5.5, Figs. 12–13). **Shown**
13. Three spectral bands: the buffet fundamental at 50–60 Hz (experiment 69 Hz) with harmonics, a bump at 1000–2000 Hz and a wake bump at 5000–6000 Hz, associated after Szubert et al. [41] with buffet, von Kármán shedding and Kelvin–Helmholtz instabilities (§4.5.6, Figs. 14–15). **Shown** / **Stated** (association)
14. The spectral energy distribution is invariant along the span despite the three-dimensional topology, as in the experiment (§4.5.6, Fig. 17). **Shown**
15. PANS costs about 3% more than URANS per time step on the same grid and processors (Table 3: total 2.00 against 1.95 s, printed "+3.1%"); the largest increase is the residual-Jacobian evaluation (printed "+7%"); linear-solver iterations rise from 3.86 to 4.59 (§4.6). **Shown**
16. Fixing transition at the trip location $x/c=0.07$ improves the RMS peak and trailing-edge RMS in two dimensions; transition at $x/c=0.25$ moves the mean shock downstream but creates a leading-edge laminar separation and higher RMS upstream; the pressure-side transition location matters little (§4.3, App. C.1, Figs. 2, C.18–C.19). **Shown**
17. The Spalart–Rumsey sustainability term gives a slightly upstream shock and high trailing-edge unsteadiness in two dimensions and is not used in three; the free-stream turbulence level matters little; inflow $\mu_t/\mu=10$ with the trip at $x/c=0.07$ agrees best (§4.3). **Shown**
18. A lower clip $f_{k,\min}=0.4$ gives too upstream a shock and too much trailing-edge unsteadiness on C3; 0.6 improves the agreement at $\alpha=3.5°$ and $3.9°$ (App. C.2, Fig. C.20). **Shown**
19. Spanwise-periodic, short-span, unconfined configurations "do not allow for a correct characterization of the buffet flow dynamics" of this case (§1). **Stated**
20. PANS can improve on RANS-like grids as long as $f_k$, $f_\varepsilon$ stay reasonably high, whereas DES-family methods switching to LES mode reintroduce LES grid and time-step requirements (§1, citing [3] and [5]). **Stated**
21. Earlier URANS predictions of OAT15A buffet at $\alpha=3.5°$ scatter widely across models and solvers (Spalart–Allmaras mostly without SIO; several corrected and Reynolds-stress models with SIO at $St\approx0.066$–0.074); the authors' own earlier HMB3 SST URANS [70] gives no SIO (App. A, Table A.4). **Stated** (compilation)
22. The experiment shows unsteadiness from $\alpha=3.1°$, fully established SIO at $3.5°$, and a single buffet frequency $St=0.06$ (§1, §4.1). **Stated**
23. The confined case is "intermediate" between two-dimensional cases with periodic stall cells and three-dimensional cases with outboard-propagating buffet cells; pressure disturbances originate at the wing–wall junction and propagate to the tunnel centre (§5). **Stated**

The model as printed, in registry notation: $f_k=k_u/k$, $f_\varepsilon=\varepsilon_u/\varepsilon=1$,
$f_\omega=f_\varepsilon/f_k$ (Eqs. 1–2); the SST-PANS equations of Luo et
al. for $k_u$, $\omega_u$ with diffusion multiplied by $f_\omega/f_k$, the
destruction coefficient $\beta'=\alpha\beta^*-\alpha\beta^*/f_\omega+\beta/f_\omega$,
the cross-diffusion multiplied by $f_\omega/f_k$, and
$\mu_t=\min(\rho k_u/\omega_u,\rho a_1k_u/(|S|F_2))$, $a_1=0.31$ (Eqs.
3–5); the other SST constants are "calculated as prescribed in reference
[22]", not printed. Eq. (8) proposes the time step from
$t_{ku}=(\nu_u/\varepsilon_u)^{1/2}=\sqrt{C_\mu f_k}/\omega$, minimized
over the domain outside the boundary layer; how it fixed the time steps of
Table 2 is not shown. **Gap:** the paper lists four grid-size definitions
(Eqs. 16–19: maximum, minimum, cell diagonal, cube root of the volume) and
does not state which one the reported runs use.

# Printed slips

- **Table 2:** the two F3 runs after P3F25a are labelled "P3M25b" and "P3M25c", the IDs of the M3 runs above; "P3C35d" appears twice (with $x_{tr}/c=0.07$ and $0.25$).
- **Nomenclature:** "SST Shear Stress Tensor", Table A.4 caption "Menter's Shear Stress Model", main text "Shear-Stress Transport model".
- **Nomenclature and §3:** $k_h$ "heat transfer coefficient" with units W m$^{-1}$ K$^{-1}$, those of a thermal conductivity.
- **§3:** "$E=e+u_iu_j/2$", with a free index $j$ in the kinetic energy per unit mass.
- **§1:** "e.g. in et al. [48,51]", with the author name missing.
- **Eq. (8), not established as a slip:** if $\nu_u=k_u/\omega_u$, $\varepsilon_u=C_\mu k_u\omega_u$ and $\omega_u=\omega/f_k$ ($f_\varepsilon=1$), then $(\nu_u/\varepsilon_u)^{1/2}=f_k/(\sqrt{C_\mu}\,\omega)$, not the printed $\sqrt{C_\mu f_k}/\omega$ *(compiler check, not in the sources)*; the paper defines neither $\nu_u$ nor which $\omega$ enters Eq. (8), so the printed form cannot be checked against the paper itself. The text writes the RANS time scale as $1/(c_\mu\omega)$ (§2.2).
- **Table 3:** from the printed times, the total ratio $2.00/1.95$ is $+2.6\%$ against the printed "+3.1%", and the high-order-gradient ratio $0.00025/0.00024$ is $+4.2\%$ against "+8%"; the printed URANS components sum to 1.935, not 1.95 *(compiler check, not in the sources)*. The text gives the overhead as "about 3%" (§4.6).
- **Table B.5:** "Lakshimpathyi & Girimaji", "Cylynder"; Srinivasan & Girimaji listed as 2014 while ref. [84] prints 2011. **Table A.4:** "Zimmernann" against "Zimmermann" in ref. [76]; ref. [67] "van Aldaba" against "Van Albada" in §3; §4.5.3 "trailind edge".
- **References with mismatched DOIs or venues:** [39] (Spalart et al. 2006, Theor. Comput. Fluid Dyn., with an Int. J. Heat Fluid Flow 2008 DOI), [46], [53], [57] (same DOI as [56]), [41] (year 2020, DOI of 2015), [34], [72], [28].

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $f_k$, $f_\epsilon$, $f_\omega$ | $f_k$, $f_\varepsilon$, $f_\omega$ | agree |
| $k$, $\omega$ (Eqs. 3–5) | $k_u$, $\omega_u$ | unresolved quantities, subscript dropped in the source |
| $k_u$, $\epsilon_u$, $\omega_u$ | $k_u$, $\varepsilon_u$, $\omega_u$ | |
| $C_{\rm PANS}$, $L_t$, $\Lambda$ | same (page-local) | |
| $\Delta$ | $h$ | **collision:** local grid size, not a filter width; definition not stated |
| $\gamma$, $\beta$, $\beta^*$, $\sigma_k$, $\sigma_\omega$, $\sigma_{\omega2}$, $a_1$ | $\alpha$, $\beta$, $\beta^*$, $\sigma_k$, $\sigma_\omega$, $\sigma_{\omega2}$, $a_1$ (SST constants, as on the SST page) | **collision:** $\gamma$ is the ratio of specific heats or the intermittency, so it is written as the SST $\alpha$ |
| $\beta'$ | (modified destruction coefficient) | |
| $C_\mu$, $c_\mu$ | $C_\mu$ | both spellings printed; value not printed |
| $F_1$, $F_2$ | $F_1$, $F_2$ | agree |
| $S$ | $\lvert S\rvert$ | "main strain rate tensor"; norm not defined |
| $\mu_t$, $\mu_T$, $\nu_t$ | $\mu_t$, $\nu_t$ | |
| $P_k=\tau_{ij}\partial u_i/\partial x_j$ | $P_k$ | as printed in the nomenclature |
| $\tau_{ij}$ (Eq. 10) | $\sigma_{ij}$ | **collision:** viscous stress |
| $t_{ku}$, $\nu_u$ | (unresolved Kolmogorov time, undefined unresolved viscosity) | |
| $k_h$ | (thermal conductivity) | **collision** with $k$ |
| $E$, $e$ | $E/\rho$, (internal energy) | per unit mass |
| $U_j$, $u_i$ | $\langle u_j\rangle$ (partially averaged), $u_i$ | no filter or Favre symbol used |
| $Re_c$, $M_\infty$, $St=fc/U_\infty$ | $Re_c$, $M_\infty$, $St$ | |
| $C_p$, $C_L$ | $C_p$, $C_L$ | |
| $x_{tr}/c$, $P_{out}/P_{in}$, $T_B$ | (trip location, back-pressure ratio, buffet period) | |

# Reference list

99 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [91],
Dzanic et al. (2022), is the ingested [dzanic-2022](/sources/dzanic-2022.md).
Refs. [29] (Liu et al. 2022, PANS for rotating flow) and [30] (Wang et al.
2023, PANS of a square-back van) are works distinct from this bundle's
Sources of the same author and year and take suffixed keys (`liu-2022-d`, `wang-2023-f`). Same-author
same-year pairs (Girimaji 2006, Ma 2011, D'Aguanno 2021, Klapwijk 2019,
Saroha 2020) take suffixes in printed order. Ref. [71] is the authors'
same-title conference paper, keyed `petrocchi-2022` and kept distinct.
Ref. [90] prints only a title; its author and year come from Table B.5.
Several titles are garbled as printed and several DOIs mismatch their
venues (kept as printed, with notes). No printed duplicates.

# Pages created or updated

Chunk 5 (2026-10-26). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [elsA](/software/elsa.md)
