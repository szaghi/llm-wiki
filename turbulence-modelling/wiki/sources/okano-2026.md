---
type: Source
title: "Okano & Haga (2026) — Robust wall-modeled large-eddy simulation with flux reconstruction scheme under extremely cold wall conditions"
description: "Stabilizes wall-modelled LES with a flux-reconstruction scheme on strongly cooled isothermal walls by an artificial viscosity confined below the matching height, shaped by a linear ramp times a semi-local van Driest damping and sized by a temperature-curvature LAD sensor; stable channel flows down to a wall-to-recovery temperature ratio of 0.1."
resource: "doi:10.1016/j.compfluid.2026.107109"
source_kind: paper
authors: [Okano Y., Haga T.]
year: 2026
venue: "Comput. Fluids 314:107109"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computers_amp_Fluids_Okano_Robust_wall-modeled_large-eddy_simulation_with_flux_reconstr.pdf"
tags: [wmles, flux-reconstruction, shock-capturing, compressible, channel-flow]
timestamp: 2026-10-29T10:10:00Z
---

# Summary

Okano & Haga (2026) treat a robustness failure of
[wall-modelled LES](/methods/wall-modelled-les.md) with a
[flux-reconstruction](/methods/flux-reconstruction.md) scheme on isothermal
walls much colder than the recovery temperature, the regime of liquid-rocket
combustion chambers. Below the matching height the LES cells are coarse and
carry little resolved Reynolds shear stress, so the resolved gradients are
over-predicted and the high-degree polynomials in those cells oscillate. The
earlier stabilization of Fukushima & Haga (an auxiliary gradient boundary
condition plus a wall-normal modal filter on wall-adjacent cells, the
[explicit modal filtering](/methods/explicit-modal-filtering.md) of Hamedi &
Vermeire) runs at $T_w/T_r=0.8$ but diverges for colder walls in the authors'
channel.

The contribution is an artificial viscosity added only in the cell line
between the wall and $h_{\mathrm{wm}}$, and through the molecular Prandtl
number to the conductivity. Its wall-normal profile is a linear ramp that
vanishes at $h_{\mathrm{wm}}$ times a semi-local van Driest damping that
vanishes at the wall; its magnitude, one value per cell line, is the maximum
over that line of a localized-artificial-diffusivity expression built on the
second derivative of temperature in reference coordinates, the device of
[artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
moved to the near-wall region. A limiter caps the value at the first solution
point when the first cell is very coarse.

The solver is JAXA's LS-FLOW-HO (hexahedral FR with Radau correction, Gauss
points, SLAU, BR2, SSPRK(4,3), no explicit subgrid model, i.e.
[implicit LES](/definitions/implicit-les.md) above the wall model) with the
ODE [equilibrium wall model](/methods/equilibrium-wall-model.md) at
$h_{\mathrm{wm}}=0.1\delta$. On compressible
[channel flow](/benchmarks/turbulent-channel-flow.md) ($M_b=0.8$,
$Re_b=3.4\times10^4$) at $T_w/T_r=0.81$ both the new method and the filter
approach match the DNS of Yao & Hussain within 5% in $Re_\tau$, $C_f$ and the
wall heat flux; at $T_w/T_r=0.4$, 0.2 and 0.1 only the new method stays stable,
also at doubled and quadrupled $Re_b$, with $N=1$, 2, 3 at matched degrees of
freedom and for $C_{\mathrm{AV}}\ge0.1$ ($N=3$) or $\ge0.05$ ($N=2$, 1). A
supersonic cold-wall channel ($T_w/T_r=0.18$, $Re_\tau=451$) is reproduced
within 2.5% in $Re_\tau$ and 4% in heat flux, and the temperature–velocity
relation agrees with Walz's. The introduction quotes Yang & Griffin's
wall-resolved scalings ([grid-point requirements](/results/les-grid-point-requirements.md)).

# Version read

Version of record (Elsevier; received 14 December 2025, revised 22 April 2026,
accepted 24 April 2026, online 30 April 2026), 13 pages, all read; Eqs. (12)
and (21) and pp. 2–4 and 8 read visually because the text layer garbles them.
Page 1 matches the Crossref metadata; no identity issue. Equation, table,
figure and section numbers are those of this version.

# Key claims

Page-local symbols: $T_w$, $T_r=T_c[1+(\gamma-1)rM_c^2/2]$ ($r=0.89$) the wall
and recovery temperatures, subscript $c$ the channel centre; $\mu_{\mathrm{AV}}$
the artificial viscosity and $\mu_{\mathrm{AV},0}$ its magnitude per cell line
$\Omega_{\mathrm{line}}$ (wall to $h_{\mathrm{wm}}$); $f_{\mathrm{lin}}=1-d/h_{\mathrm{wm}}$
and $f_{\mathrm{vD}}=[1-\exp(-y^*/A^+)]^2$ the ramp and the semi-local van
Driest damping; $\kappa_{\mathrm{th}}$ the thermal conductivity; $C_{\mathrm{AV}}$
the AV constant; $c$ the sound speed (not the Smagorinsky $C_s$); $h_l$ the
wall-normal solution-point spacing of Eq. (14);
$K_{\mathrm{ord}}$ the "order of spatial accuracy" of Eqs. (13)–(14);
$\mathcal R_{\mathrm{rp}}[\cdot]$ the restriction–prolongation filter;
$B_q=-q_w/(c_pu_\tau T_w\rho_w)$ the non-dimensional wall heat flux.

1. In WMLES with discontinuous finite-element methods the cells below $h_{\mathrm{wm}}$ are coarse and lack resolved Reynolds shear stress, so the velocity gradient is over-estimated to satisfy the stress balance, and high-degree polynomials on such cells oscillate (§1). **Stated**
2. The filter approach of Fukushima & Haga runs stably at $T_w/T_r=0.8$, but the channel diverges for walls colder than $T_w/T_r=0.4$ with the authors' numerics (§3). **Shown**
3. At $T_w/T_r=0.1$, $N=3$, CFL 0.4, the filter approach develops near-wall temperature oscillations from about 250 steps and blows up by 500 steps with a large local temperature rise (§3, Figs. 2–3). **Shown**
4. With $N=1$ under the same conditions the near-wall temperature drops sharply before blow-up (Fig. 4: after 5900 and 11800 steps) (§3). **Shown**
5. An artificial viscosity that itself oscillates inside a cell easily triggers instability, because the polynomial gradient amplifies the oscillation; the AV must have a smooth in-cell profile (§4, citing Haga & Kawai for the shock analogue). **Stated**
6. The AV is $\mu_{\mathrm{AV}}(d)=\mu_{\mathrm{AV},0}f_{\mathrm{lin}}f_{\mathrm{vD}}$ for $d\in[0,h_{\mathrm{wm}}]$, added to the molecular viscosity, $\mu=\mu_f+\mu_{\mathrm{AV}}$, and to the conductivity, $\kappa_{\mathrm{th}}=(\mu_f+\mu_{\mathrm{AV}})c_p/Pr$; it vanishes at $h_{\mathrm{wm}}$ ("there is originally no AV at the matching point height") and at the wall (the wall flux comes from the wall model) (§4.1, Eqs. 7–10; Fig. 9). **Shown**
7. For very coarse first cells the first solution point takes $\min[\mu_{\mathrm{AV},0}f_{\mathrm{lin}}f_{\mathrm{vD}},\ \tfrac12\mu_{\mathrm{AV},2}]$, $\mu_{\mathrm{AV},2}$ the value at the second solution point (Eq. 11); it activates only in the §5.3 runs. **Stated**
8. The magnitude is $\mu_{\mathrm{AV},0}=\max_{\Omega_{\mathrm{line}}}\big[C_{\mathrm{AV}}\,\mathcal R_{\mathrm{rp}}\big[\frac{\rho c}{T}\sum_{l=1}^3\frac{\partial^2T}{\partial\xi_l^2}\Delta\xi_l^2h_l\big]\big]$ with $C_{\mathrm{AV}}=0.4$, $\Delta\xi_l=2/(K_{\mathrm{ord}}+1)$, $h_l=\lvert\Delta\boldsymbol x_l\cdot\boldsymbol n\rvert/(K_{\mathrm{ord}}+1)$, $\Delta\boldsymbol x_l\cdot\boldsymbol n$ the projection of the cell edge on the wall normal; the maximum over the line is taken "for the numerical robustness" (§4.2, Eqs. 12–16). **Stated** (as printed, without an absolute value on $\partial^2T/\partial\xi_l^2$)
9. At $T_w/T_r=0.8$ (Table 1: 0.81), $Re_b=3.4\times10^4$, $M_b=0.8$: proposed method $Re_\tau=1677$, $10^3C_f=4.69$, $10^2B_q=1.09$; filter approach 1676, 4.69, 1.09; DNS 1692, 4.47, 1.13; errors below 5% (§5.1, Table 3). **Shown**
10. At $T_w/T_r=0.8$ the mean velocity, temperature, Reynolds shear and normal stresses of both methods match the DNS of Yao & Hussain over most of the channel (§5.1, Fig. 8). **Shown**
11. The filter approach blows up at $T_w/T_r=0.2$ and 0.1, while the proposed method stays stable at 0.4, 0.2 and 0.1 on the same grid (§5.2, Fig. 10). **Shown**
12. $u^+$ and the Reynolds shear stress in wall units grow as the wall is cooled, attributed to the smaller $u_\tau$ used for normalization (no compressible transformation is applied); the same $u^+$ trend is reported for a flat plate (§5.2, Fig. 10). **Shown** (trend) / **Stated** (attribution)
13. The averaged AV grows as the wall temperature decreases, consistent with the larger temperature gradient (§5.2, Fig. 11). **Shown**
14. At $T_w/T_r=0.1$ the method stays stable at $Re_b=6.8\times10^4$ and $1.4\times10^5$ (larger half-width, same grid) (§5.3, Fig. 12). **Shown**
15. The streamwise Reynolds normal stress above $h_{\mathrm{wm}}$ hardly changes with $Re_b$, because the outer-layer rise originates in inner-layer turbulence that WMLES cannot resolve (citing Maeyama & Kawai) (§5.3, Fig. 12c). **Shown** / **Stated**
16. The WMLES temperature–velocity relation agrees closely with Walz's $T/T_c=T_w/T_c+\frac{T_r-T_w}{T_c}\frac{u}{U_c}+\frac{T_c-T_r}{T_c}\big(\frac{u}{U_c}\big)^2$ at $Re_b=6.8\times10^4$ and $1.4\times10^5$, $T_w/T_r=0.1$ (§5.3, Eq. 21, Fig. 13). **Shown**
17. The AV grows with Reynolds number; the first-point limiter of Eq. (11) makes it drop sharply near the wall at the two higher $Re_b$ (§5.3, Fig. 14). **Shown**
18. $N=3$, 2, 1 at matched degrees of freedom ($h_{\mathrm{wm}}$ in the 3rd, 4th, 6th cell), $T_w/T_r=0.1$, $C_{\mathrm{AV}}=0.4$: $10^3C_f=4.02$, 4.01, 3.99 and $10B_q=1.35$, 1.36, 1.33 (§5.4, Table 4, Fig. 15). **Shown**
19. For $C_{\mathrm{AV}}\in\{0.025,0.05,0.1,0.2,0.4,0.8\}$ the runs blow up at 0.05 and 0.025 for $N=3$ and at 0.025 for $N=2$, 1; otherwise $B_q$ changes by at most 4% and $u_\tau$ by less than 4.3%, and the mean temperature changes slightly only below $h_{\mathrm{wm}}$ (App. A, Tables A.5–A.6, Fig. A.17). **Shown**
20. Refining from $40\times30\times20$ to $60\times46\times30$ cells ($N=3$, $T_w/T_r=0.1$) gives $10^3C_f=4.02$ against 4.00 and $10B_q=1.35$ for both; the grid criterion of Fukushima & Haga, derived for adiabatic walls, holds under extreme cooling (App. B, Tables B.7–B.8). **Shown**
21. Against the DNS of Coleman et al. ($T_w/T_r=0.18$, $Re_\tau=451$, $U_b/c_w=3.0$): $Re_\tau=441$ and 442, $B_q=0.142$ for both grids against 451 and 0.137, below 2.5% and 4% (App. C, Table C.10, Fig. C.19). **Shown**
22. For that supersonic case the wall-model eddy viscosity uses Iyer & Malik's "mixedmin2" scaling, $y^+_{\mathrm{mm2}}=\min\big(\tfrac12(y^++y^*),\tfrac12(y^+_{\mathrm{loc}}+y^*)\big)$ with $y^+_{\mathrm{loc}}=\rho u_\tau y/\mu$, because Iyer & Malik found it better there; the AV profile keeps $y^*$ (App. C, Eqs. C.1–C.4). **Stated**
23. A low-dissipation finite-volume WMLES at extremely cold walls (Mettu & Subbareddy) did not report this instability; the authors met it with FR (§1). **Stated**
24. Wall-resolved LES needs $N_{\mathrm{pts}}\sim Re^{1.86}$ grid points and $N_t\sim Re^{6/7}$ time steps, citing Yang & Griffin (§1). **Stated**
25. Without the bulk-temperature source term the bulk temperature of a cold-wall channel drifts down through wall heat loss (§5.1). **Stated**

The wall model (background, Kawai & Larsson) solves
$\frac{d}{dy}\big[(\mu+\mu_t)\frac{dU_\parallel}{dy}\big]=0$ and
$\frac{d}{dy}\big[(\mu+\mu_t)U_\parallel\frac{dU_\parallel}{dy}+c_p\big(\frac{\mu}{Pr}+\frac{\mu_t}{Pr_t}\big)\frac{dT}{dy}\big]=0$
with $\mu_t=\kappa\rho u_\tau^*y\,f_{\mathrm{vD}}$, $\kappa=0.41$, $A^+=17$,
$Pr_t=0.9$, semi-local $y^*=\rho u_\tau^*y/\mu$, by the Thomas algorithm
(Eqs. 1–6). Mass flow and bulk temperature are held by a two-step controller
with constants $2$ and $-0.2$ and a relaxation source with time
$0.3\delta/u_\tau$ (Eqs. 17–20).

*(Compiler check, not in the sources:)*
$40\times30\times20$ cells times $4^3$ solution points ($N=3$, §5.1) give
$1.536\times10^6$, which matches the printed $1.5\times10^6$ degrees of
freedom.

# Printed slips

- **§1:** "a more robust method is needed to perform WMLRS reliably".
- **§1:** "Fukushima et al. [24]"; ref. [24] has two authors (Fukushima, Haga).
- **§5.1 against Table 1:** the text writes $T_w/T_r=0.8$, Table 1 prints 0.81.
- **§4.2 and Eq. (12):** the text says the sum is taken "with the Einstein summation convention", while Eq. (12) also prints the explicit $\sum_{l=1}^3$.
- **Eq. (12):** printed without an absolute value on $\partial^2T/\partial\xi_l^2$ (recorded as printed).
- **Fig. 12c:** the axis label $\widetilde{u'u'}/u_\tau^2$ uses a tilde not defined in the text.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| P1, P2, P3 | $N=1$, 2, 3 | P3 is called "fourth-order spatial accuracy" |
| $K$ (Eqs. 13–14) | $K_{\mathrm{ord}}$ (page-local) | "order of spatial accuracy" as printed; **collision** with the spectral-page $K$ |
| SP | solution point (Gauss–Legendre) | |
| $\xi_l$ | $\xi_l$ | reference coordinate |
| $\mu_f$, $\mu$ (Eq. 7) | $\mu$, $\mu+\mu_{\mathrm{AV}}$ | the source's $\mu$ in Eq. (7) is the total |
| $\mu_{AV}$, $\mu_{AV0}$ | $\mu_{\mathrm{AV}}$, $\mu_{\mathrm{AV},0}$ (page-local) | a shear-type viscosity, not the artificial bulk viscosity $\mu_{b,\mathrm{AV}}$ |
| $\kappa$ | $\kappa_{\mathrm{th}}$ (page-local) | **collision** with the von Kármán $\kappa$ |
| $\varkappa=0.41$ | $\kappa$ | von Kármán constant |
| $D$ (Eq. 4) | $f_{\mathrm{vD}}$ (page-local) | squared van Driest form, semi-local |
| $L=1-d/h_{wm}$ | $f_{\mathrm{lin}}$ (page-local) | **collision** with the integral length $L$ |
| $y$ (wall model), $d$ (AV) | $y$, $d$ | wall distance |
| $y^*$, $u^*_\tau$ | $y^*$, $u^*_\tau$ | semi-local scaling |
| $y^+_{local}$, $y^+_{mixedmin2}$ | $y^+_{\mathrm{loc}}$, $y^+_{\mathrm{mm2}}$ (page-local) | Iyer & Malik |
| $h_{wm}$ | $h_{\mathrm{wm}}$ | $0.1\delta$; $0.2\delta$ in App. C |
| $\mu_t$ (Eq. 3) | $\mu_t$ | wall-model mixing-length eddy viscosity |
| $C$ | $C_{\mathrm{AV}}$ (page-local) | 0.4 |
| $c_s$ | $c$ (page-local) | sound speed; not $C_s$ |
| $\Delta_l$, $\Delta\boldsymbol x_{l,cell}$ (Eqs. 14–16) | $h_l$, $\Delta\boldsymbol x_l$ (page-local) | wall-normal-projected spacing; $\Delta$ stays the filter width |
| overbar (Eq. 12) | $\mathcal R_{\mathrm{rp}}[\cdot]$ (page-local) | restriction–prolongation filter; **not** the LES filter |
| $\Omega$ (Fig. 5) | $\Omega_{\mathrm{line}}$ (page-local) | cell line from the wall to $h_{\mathrm{wm}}$; not $\Omega_{ij}$ |
| $C_p$, $C_v$ | $c_p$, $c_v$ | |
| $T_w$, $T_r$, $T_c$, $U_c$, $M_c$ | page-local | wall, recovery, centre values |
| $B_q$ | $B_q$ (page-local) | non-dimensional wall heat flux |
| $\beta_1=2$, $\beta_2=-0.2$ | (controller constants) | not the field-inversion $\beta$ |
| $\tau_{relax}$ | (relaxation time) | $0.3\delta/u_\tau$ |
| $Re_b$, $M_b$, $Re_\tau$, $\delta$ | $Re_b$, $M_b$, $Re_\tau$, $\delta$ | half-width |
| $\Delta x_e$, $\Delta y_e$, $\Delta z_e$ | (effective spacing) | cell size over solution points per direction |
| $t^*u_\tau/\delta=1$ | (time unit) | called "one flow through time" |

# Reference list

61 printed references, numbered Elsevier style, no DOIs printed. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ingested works among them: ref. [2]
[Heinz (2020)](/sources/heinz-2020.md), [9] [Bose & Park (2018)](/sources/bose-2018.md),
[26] [Gao et al. (2025)](/sources/gao-2025.md) (printed without article
number), [27] [Hamedi & Vermeire (2022)](/sources/hamedi-2022.md), [57]
[Maeyama & Kawai (2023)](/sources/maeyama-2023.md), [59]
[Domingo & Vervisch (2023)](/sources/domingo-2023.md). Refs. [16] (Wang &
Hantla, J. Aircr. 2024) and [20] (Wang, AIAA J. 2024) are different works from the ingested Wang 2024 sources and are keyed `wang-2024-u` and `wang-2024-r` respectively. Refs. [4]
and [12] print Mech. Eng. Rev. article numbers "15–00418" and "15–00475";
refs. [5], [6], [7], [21], [25], [26], [48], [49] print volume (issue)
without page or article number; ref. [18] is keyed on the printed surname
"de Frahan". No item is unparseable.

# Pages created or updated

Chunk 16 (2026-10-29). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
