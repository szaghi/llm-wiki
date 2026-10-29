---
type: Source
title: "Zhang et al. (2024b) — Effects of wall temperature on hypersonic shock wave/turbulent boundary layer interactions"
description: "GPU DNS of a Mach 6, 34-degree compression-ramp interaction at three wall-to-recovery temperature ratios: wall cooling shrinks the separation bubble, free-interaction theory with a new streamwise coordinate predicts wall pressure across wall temperatures, and wall cooling suppresses the low-frequency unsteadiness, found to be driven mainly from downstream."
resource: "doi:10.1017/jfm.2024.533"
source_kind: paper
authors: [Zhang J., Guo T., Dang G., Li X.]
year: 2024
venue: "J. Fluid Mech. 990:A21"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Journal_of_Fluid_Mechanics_Zhang_Effects_of_wall_temperature_on_hypersonic_shock_waveturbulen.pdf"
tags: [dns, compressible, hypersonic, shock-boundary-layer-interaction, gpu, boundary-layer]
timestamp: 2026-10-29T07:41:00Z
---

# Summary

Zhang et al. (2024b) run [DNS](/definitions/direct-numerical-simulation.md)
of the [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
over a $34^\circ$ compression ramp at $M_\infty=6$, with unit Reynolds
number $20\,000$/mm and isothermal walls at $T_w/T_r=0.50$, 0.75 and 1.0. The
code is the GPU finite-difference code [OpenCFD-SCU](/software/opencfd-scu.md).
Its hybrid scheme switches between seventh-order upwind linear, WENO7 and
WENO5 ([WENO](/methods/weno-scheme.md)) under a two-threshold
Jameson-type pressure [sensor](/definitions/shock-sensor.md). The authors
rank the [dissipation](/properties/numerical-dissipation.md) of the three
branches and state that the linear and WENO7 branches are not robust at
reattachment. The incoming [boundary layers](/benchmarks/turbulent-boundary-layer.md)
have matched $\delta$ and $Re_\tau=675$, 411 and 293. They are checked against
the van Driest [transformation](/definitions/compressible-velocity-transformation.md)
and the [log law](/definitions/law-of-the-wall.md), whose intercept is 5.6–6.0.
They are also checked against the Walz, Duan–Martín and generalized
Reynolds-analogy temperature–velocity relations and against semi-locally
scaled turbulent-kinetic-energy budgets, which include the
[pressure-dilatation](/definitions/pressure-dilatation.md) term. The
introduction notes that [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md)
is not necessarily valid at non-adiabatic hypersonic conditions.

Wall cooling shrinks the separation bubble markedly, and the authors
explain this by fuller near-wall density and momentum profiles. The
separation and plateau pressures are insensitive to $T_w$, as
free-interaction theory (FIT) predicts. With the coordinate
$x_{\chi}=(x-x_s)/L_{\mathrm{int}}$ (page-local; the source's $\chi$), $L_{\mathrm{int}}=x_c-x_s$, the FIT
correlation function collapses across wall temperatures. The authors
combine this with the power law $L_{\mathrm{int}}/\delta\propto(T_w/T_r)^n$,
$n\sim0.85$, into Eq. (3.27), which predicts the wall pressure upstream of
the corner at one wall temperature from that at another. They test it on
three Mach 2.9, $24^\circ$ ramp DNS that replicate Zhu et al. (2017). The
low-frequency separation-shock motion lies at $St_\delta\approx0.015$–0.03.
Time-delayed wall-pressure correlations, with and without a low-pass
filtered reference, indicate that this motion is driven mainly from
downstream by the separation bubble. Wall cooling suppresses it by
shrinking the bubble.

# Version read

Version of record (Cambridge University Press, open access; received 4
September 2023, revised 20 May 2024, accepted 28 May 2024), 35 pages
(A21-1 to A21-35), all read, with the equation pages checked visually.
Page 1 matches the Crossref metadata; no identity problem.

# Key claims

1. DNS of a Mach 6, $34^\circ$ compression-ramp interaction at $T_w/T_r=0.50$, 0.75, 1.0, spanning $Re_\tau=293$–675 at the reference station $x=-70$ mm (§2.2, Table 3). **Shown**
2. The seventh-order upwind linear scheme and WENO7 lack robustness in the reattachment region and cannot keep the simulation stable; WENO5 is robust but significantly more dissipative than WENO7; the hybrid scheme uses the three in smooth, non-smooth and extremely non-smooth regions, chosen by a modified Jameson–Schmidt–Turkel pressure-gradient sensor with two thresholds (§2.1). **Stated**
3. Mean wall pressure and $C_f$ near the corner are almost identical on the coarse and fine meshes ($\Delta x^+,\Delta y^+,\Delta z^+$ from about 4.9/0.48/4.8 to 3.5/0.35/3.5): grid independence (Fig. 3, Table 2). **Shown**
4. Spanwise two-point correlations at $x=-70$ mm, $y^+=50$ approach zero for $r_z>0.2L_z$, and $L_z^+>1000$ in every case (§2.2, Fig. 4). **Shown**
5. The van Driest velocity follows a log law of slope about 2.44 with intercepts 5.6–6.0, above the incompressible 5.1; the intercept is more sensitive than the slope to wall temperature, colder walls depart from $u^+=y^+$ closer to the wall, and the transformation is more applicable to the adiabatic wall (§3.1, Eq. 3.2, Fig. 5a). **Shown**
6. As the wall temperature decreases, the peak of the density-scaled velocity fluctuations moves closer to the wall, as in Duan et al. (2010) (Fig. 5b). **Shown**
7. The temperature–velocity relation matches the Duan & Martín (2011) relation and the generalized Reynolds analogy of Zhang et al. (2014) for non-adiabatic walls; the Walz relation deviates more as $T_w$ departs from $T_r$, and near the edge at $T_w/T_r=1.0$ because of the total-temperature overshoot (maximum $1.02T_{0\infty}$) (§3.1, Eqs. 3.4–3.6, Fig. 6). **Shown**
8. Semi-locally scaled budgets of turbulent kinetic energy agree with the M5T5 case of Duan et al. (2010) and balance, confirming semi-local scaling in hypersonic boundary layers (§3.1, Fig. 7). **Shown**
9. Streak counts from the zero crossings of $C_f$ minus its spanwise mean give mean streak widths 0.148, 0.203, 0.283 $\delta$ for $T_w/T_r=0.5$, 0.75, 1.0, about 100 wall units in each case; streaks are thinner at a colder wall (§3.2, Figs. 8–9). **Shown**
10. The reattached boundary layer is much thinner than upstream, so its streamwise vortices are smaller (§3.2, Figs. 10–11). **Shown** (qualitative)
11. The separation bubble shrinks markedly with wall cooling: a colder wall raises the near-wall density at constant wall pressure, lowers the viscosity, fills the velocity profile and gives more near-wall momentum against the adverse pressure gradient (§3.2, Figs. 12–13, Table 4). **Shown**
12. A secondary counter-rotating corner bubble exists, two orders of magnitude smaller than the main one (§3.2, Figs. 12d, 15a). **Shown**
13. The amplification of turbulent kinetic energy peaks at separation and reattachment, and the strong region expands with the larger bubble at higher wall temperature (§3.2, Fig. 14). **Shown**
14. The interaction origin moves upstream and the plateau lengthens with wall heating ($x_0/\delta=-2.69$, $-3.76$, $-4.86$), while the plateau end ($x_{p2}/\delta=-0.17$, $-0.20$, $-0.23$), the plateau pressure ($p_w/p_\infty=4.63$, 4.46, 4.55) and the separation pressure (1.54, 1.50, 1.54) are insensitive to $T_w$ (Table 4, §3.2). **Shown**
15. The pressure rise in the interaction onset follows FIT under different wall thermal conditions: $F(x_{\mathrm{FIT}})$ collapses for $x_{\mathrm{FIT}}<2.5$ across Mach 2.9 and 6, Reynolds number, compression angle and wall temperature, consistent with Volpiani et al. (2020) (§3.3, Eq. 3.16, Fig. 18). **Shown**
16. $F$ at the corner is 5.55–5.82 at $M_\infty=2.9$ and 6.79–7.05 at $M_\infty=6$ (§3.3, Fig. 18). **Shown**
17. The coordinate $x_{\chi}=(x-x_s)/L_{\mathrm{int}}$ collapses $F$ better upstream of the plateau and, when only the wall temperature differs, also downstream of it; it also holds for the Mach 5 impinging-shock data of Volpiani et al. (2020) with $x_c$ the impingement point (§3.3, Eq. 3.17, Figs. 19–20). **Shown**
18. The Zhu et al. (2017) law $L_{sr}/\delta\propto(T_w/T_r)^{0.85}$ ($L_{sr}=x_r-x_s$) predicts the Mach 6 separation lengths within 5 %; the Touré & Schülein (2023) formula underperforms at $T_w/T_r=0.75$ and 1.0 (errors 17.2 % and 22.7 %) and underestimates wall-temperature effects, which the authors attribute to its fitting on impinging-shock data (Table 6, §3.3). **Shown**
19. The predictive relation (3.27) holds under three conditions (same free stream and corner angle; separation strong enough for a plateau; $x<x_c$); predictions agree with DNS for $x<0$ and the error grows for $x>0$, especially at $M_\infty=6$; applicability is "preliminarily confirmed" for $Re_\tau=160$–675 (§3.3, Eqs. 3.24–3.28, Fig. 21). **Derived** and **Shown**
20. The low-frequency separation-shock motion has dominant $St_\delta\approx0.015$–0.03 and $St_{L_i}\approx0.016$–0.022, close to Gonsalez & Dolling (1993), with intermittent lengths $L_i=0.61$, 0.74, $1.07\delta$; raising $T_w$ increases the low-frequency energy and the intermittent region and lowers the dominant frequency (§3.4, Fig. 23). **Shown**
21. The characteristic frequency upstream rises as the wall temperature decreases (§3.4). **Shown** (qualitative)
22. The peak low-frequency energy proportion $P_L$ rises by about 28 % and the extent of $P_L>0.3$ by about 200 % from $T_w/T_r=0.50$ to 1.0; the peak exceeds 0.5 for 0.75 and 1.0 (§3.4, Eq. 3.30, Fig. 24). **Shown**
23. Wall cooling shortens the recovery from mid to high frequency downstream of reattachment, as reattachment moves upstream (§3.4). **Shown**
24. Delayed correlations with Station 5 show a steep first peak (negative delay upstream, positive downstream: upstream influence) and a broad second peak of opposite sign (downstream influence), absent at Stations 1–2; after low-pass filtering Station 5 at $0.1U_\infty/\delta$ the first peak disappears while the second is almost unaffected, so the downstream mechanism dominates the low-frequency unsteadiness (§3.5, Eq. 3.31, Figs. 25–26). **Shown**
25. Wall cooling suppresses the low-frequency unsteadiness primarily by shrinking the separation bubble; its upstream effect (smaller, higher-frequency structures diluting $P_L$) is indirect and secondary (§3.5, §4). **Derived** (interpretation)
26. Many turbulence models fail to simulate hypersonic interactions accurately (Roy & Blottner 2006), which motivates DNS databases (§1). **Stated**
27. Morkovin's hypothesis holds at moderate Mach number ($M<5$) on adiabatic walls but is not necessarily valid under non-adiabatic hypersonic conditions (§1). **Stated**

Free-interaction theory (Chapman, Kuehn & Larson 1958) and the
wall-temperature prediction, in page-local symbols ($p_{w0}$, $C_{f0}$ at
the interaction origin $x_0$, $L_{0s}=x_s-x_0$, $x_c$ the corner, subscripts
1 and 2 two wall temperatures, $p_{w1,0}$, $p_{w2,0}$ the origin pressures
of the two cases), Eqs. (3.16) and (3.27) as printed:

$$F(x_{\mathrm{FIT}})=\frac{p_w-p_{w0}}{p_\infty}\frac{1}{\gamma M_\infty^2}\sqrt{\frac{2(M_\infty^2-1)^{1/2}}{C_{f0}}},\qquad x_{\mathrm{FIT}}=\frac{x-x_0}{L_{0s}},$$

$$p_{w2}\!\left(\frac{x}{\delta_2}\right)=\left(\frac{C_{f2}}{C_{f1}}\right)_0^{1/2}\left[p_{w1}\!\left(\frac{x-x_{c2}}{\delta_2}\left(\frac{T_{w1}}{T_{w2}}\right)^n+\frac{x_{c1}}{\delta_1}\right)-p_{w1,0}\right]+p_{w2,0},\qquad n\sim0.85 .$$

# Printed slips

- Fig. 3 caption (p. A21-7): "(a–c) wall pressure and (d–f) skin friction coefficient", while panels (a–c) are labelled $C_f$ and (d–f) $\bar p_w/p_\infty$.
- Fig. 11 caption (p. A21-15) lists "(a,d) $T_w/T_r=0.50$", while Fig. 11 has panels (a–c) only.
- §3.2 (p. A21-11): "Considering the reappearing streamwise streak structure in figure 7 … as shown in figure 7"; Fig. 7 is the kinetic-energy budget and the streaks are in Fig. 8.
- p. A21-17: "The values of $x_0$, $x_s$ and $L$ are given in table 4"; Table 4 lists $x_0$, $x_s$, $x_{p1}$, $x_{p2}$, $x_r$, and $L$ appears in Table 6.
- Table 6 (p. A21-24), header "Relative errors of $L'_{sr}$, $L'$ and $L''$": at $T_w/T_r=0.75$ the printed values give $|3.98-4.02|/4.02=1.0$ % ($L'_{sr}$) and $|2.93-3.02|/3.02=3.0$ % ($L'$), printed "2.96 %, 1.08 %"; at 1.0, $|5.06-4.86|/4.86=4.1$ % and $|3.74-3.79|/3.79=1.3$ %, printed "1.44 %, 4.12 %"; the first two percentages appear in the order $L'$, $L'_{sr}$ *(compiler check, not in the sources)*.
- Eq. (3.6) (p. A21-10) defines $\bar T_{rg}=\bar T_\infty+r\bar u_\infty^2/(2C_p)$ with $r$ and then defines $r_g$, which is not used.
- Eq. (3.31) (p. A21-28) prints a double sum $\sum\sum$ under the first square root of the denominator and a single sum under the second.
- Fig. 21 legends (p. A21-25) label the cases "$T_w/T_\infty$", while the cases are defined by $T_w/T_r$.
- Table 2 header prints "$x^+, y^+, z^+$" for the grid spacings (Table 5: $\Delta x^+,\Delta y^+,\Delta z^+$).
- Reference list, as printed: Dang et al. (2022a) author "X, L.I.", "Phys. Fluid", Zhang et al. (2014) "wall-bddounded", Marusic et al. (2010) article number "65103".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\psi$, $\psi'$ | $\langle\psi\rangle$, $\psi'$ | Reynolds average; **collision:** the registry overbar is the LES filter |
| $\tilde\psi$, $\psi''$ | $\langle\psi\rangle_\rho$, $\psi''$ | Favre average |
| $\bar u^+_{VD}$ | van Driest velocity | |
| $1/\kappa$, $C$ | $\kappa^{-1}$, $B$ | log-law slope and intercept |
| $u_\tau^*$, $y_\tau^*$ | $u_\tau^*$, $\delta_\nu$ in semi-local form | agree with the registry $(\cdot)^*$ |
| $u_i^*$, $(u_iu_j)^*$ | density-scaled r.m.s. and shear stress (Eq. 3.3) | **collision** with semi-local scaling |
| $x^*=(x-x_0)/L_{0s}$ | $x_{\mathrm{FIT}}$ | page-local; **collision** with semi-local scaling |
| $L=x_c-x_s$ | $L_{\mathrm{int}}$ | interaction length (separation to corner) |
| $L_{sr}$, $L_{0s}=L_i$, $L'$, $L'_{sr}$, $L''$ | bubble length, intermittent length, predicted lengths | page-local; **collision:** $L_i$ is also the SATES integral length |
| $F(x^*)$, $F(\chi)$, $\chi$ | $F(x_{\mathrm{FIT}})$, $F(x_{\chi})$, $x_{\chi}$ (page-local) | FIT correlation function; **collision:** $\chi$ is the SA ratio in the registry, $F$ the thickening factor |
| $n$ | $n$ | wall-temperature exponent of $L_{\mathrm{int}}/\delta$ |
| $\tilde k$, $P_k$, $T_k$, $\Pi_t$, $\Pi_d$, $D$, $\varepsilon$, $M_k$ | $k$, $P_k$, turbulent transport, pressure diffusion, $\Pi^{\mathrm t}_{\mathrm{pd}}$, viscous diffusion, $-\varepsilon$, mass-flux term | the source's $\varepsilon$ carries a minus sign; **collision:** $\Pi$ is the registry's SGS flux |
| $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress; **collision** with the SGS stress |
| $St_\delta$, $St_{L_i}$ | $St$ on $\delta$ and $L_i$ | agree |
| PSD, WPSD, $P_L$ | same | $P_L$ page-local low-frequency energy proportion |
| $\beta$, $\varphi$, $c_p$, $c_p^*$ | shock angle, deflection angle, pressure coefficient and its scaled form (Touré & Schülein) | page-local; $c_p$ is not the specific heat |
| $R_{\alpha,\beta}(\tau)$ | delayed correlation coefficient | $\tau$ is the delay |
| $T_r$, $r=0.89$, $T_{0\infty}$ | recovery temperature, recovery factor, total temperature | page-local |

# Reference list

54 printed references, author–year style (JFM). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Zhang, Guo, Dang & Li (2022, Phys. Fluids 34:116110) is the ingested
[zhang-2022-g](/sources/zhang-2022-g.md) and Dang et al. (2022a) the
ingested [dang-2022](/sources/dang-2022.md); Dang et al. (2022b, AIP Adv.),
Zhu et al. (2017, AIAA J.), Li et al. (2010, Sci. China) and Xu et al.
(2021, JFM 929:A33) collide with keys of other works in the bundle and are the entries `dang-2022-d`, `zhu-2017-b`, `li-2010-b` and `xu-2021-c`. The author "X, L.I." of Dang et al. (2022a) enters
as Li X., with a note.

# Pages created or updated

Chunk 13 (2026-10-28). This source is cited on:

- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Morkovin's hypothesis and Reynolds analogies](/definitions/morkovin-hypothesis.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [OpenCFD-SCU](/software/opencfd-scu.md)
