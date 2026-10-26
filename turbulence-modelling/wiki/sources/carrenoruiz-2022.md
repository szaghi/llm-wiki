---
type: Source
title: "Carreño Ruiz & D'Ambrosio (2022) — Validation of the γ-Reθ Transition Model for Airfoils Operating in the Very Low Reynolds Number Regime"
description: "Validates the γ-Re_θ transition model with k-ω SST in STAR-CCM+ on airfoils at chord Reynolds numbers 2×10⁴ to 2×10⁵, comparing two correlation calibrations and two separation-induced corrections against LES, DNS and experiments, and proposing a second parameter for the separation-induced correction."
resource: "doi:10.1007/s10494-022-00331-z"
source_kind: paper
authors: [Carreño Ruiz M., D'Ambrosio D.]
year: 2022
venue: "Flow Turbul. Combust. 109:279-308"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Flow_Turbulence_and_Combustion_Carreño_Validation_of_the_gamma_text-Re__theta_Transition_Model_for.pdf"
tags: [rans, transition, separated-flow, eddy-viscosity]
timestamp: 2026-10-25T19:45:00Z
---

# Summary

Carreño Ruiz & D'Ambrosio (2022) assess the $\gamma$-$Re_\theta$
[local-correlation-based transition model](/methods/local-correlation-based-transition-model.md)
(Menter et al. 2006; Langtry 2006), coupled to the
[k-ω SST model](/methods/k-omega-sst-model.md) in STAR-CCM+ 14.06.12. The
regime is airfoils at "very low" chord Reynolds numbers, $Re_c\sim2\times10^4$
to $2\times10^5$, where laminar separation bubbles and separation-induced
transition dominate. Two calibrations of the empirical correlations are
compared. The Suluksna–Juntasaro calibration is the STAR-CCM+ default and has
no pressure-gradient correction. Menter's calibration (Langtry & Menter 2009)
has the pressure-gradient function $F(\lambda_\theta)$. Two forms of the
separation-induced intermittency $\gamma_{\mathrm{sep}}$ are also compared:
an older one (threshold 2.193, damping $R_T/15$, cap 5) and an updated one
(3.235, $R_T/20$, cap 2).

On the SD7003 airfoil at $Re_c=60{,}000$ the references are LES, PIV and
[DNS](/definitions/direct-numerical-simulation.md) data. Menter's calibration
beats the default one, and the older $\gamma_{\mathrm{sep}}$ beats the updated
one: its higher cap speeds turbulent-kinetic-energy production and
reattachment. The model gives too low a skin friction after reattachment,
which leads to premature stall, and too early a transition at
$\alpha=6^\circ$–$8^\circ$. At $Re_c=30{,}000$ neither calibration
reattaches. No single value of the coefficient $s_1$ fits all angles of
attack. The default calibration with $s_1=6$ reproduces the forces of
Menter's calibration and places transition closer to the
[LES](/definitions/large-eddy-simulation.md). Menter's correlation without
pressure gradient behaves like the default one. The authors read this as a
double counting of pressure-gradient effects by $F(\lambda_\theta)$, which
then acts like the separation-induced correction. They propose a second
parameter in $\gamma_{\mathrm{sep}}$ to control bubble position and length
separately.

URANS is needed at low angles, where trailing-edge vortex shedding raises the
mean lift, and near bubble bursting. Across SD7003, Ishii and Eppler 387
cases, the two-dimensional model captures the nonlinear lift curve at very
low $Re_c$ and agrees with experiments at $Re_c=200{,}000$. It fails on the
more cambered E387, whose flow is three-dimensional.

# Version read

Version of record (Springer, open access CC BY 4.0; received 4 February 2022,
accepted 13 May 2022), deposited in the Politecnico di Torino IRIS
repository. The PDF has 31 pages: a repository cover ("pp. 1-30", online-first
pagination) and 30 article pages, all read. The article pages carry no
journal page numbers, so locators here are sections, equations, tables and
figures. Text extraction garbled the equations, so they were read on the
rendered pages. The Crossref title carries TeX markup, and the title above is
that of page 1. There is no identity problem.

# Key claims

1. The $\gamma$-$Re_\theta$ model with SST $k$-$\omega$ "can reproduce the 2D behavior of transition in airfoils with an accuracy that increases with the Reynolds number" (§7). **Shown**
2. For SD7003 at $Re_c=60{,}000$, Menter's calibration "performs significantly better" than the default Suluksna–Juntasaro calibration. At $\alpha=4^\circ$, as separation, transition and reattachment over chord, then $C_L$, $C_D$: Menter gives 0.202, 0.518, 0.660, 0.600, 0.0221; Suluksna–Juntasaro gives 0.184, 0.53, 0.743, 0.600, 0.0257; the LES gives 0.23, 0.55, 0.65, 0.59, 0.021 (Table 5, §3.5). **Shown**
3. At $\alpha=8^\circ$, $Re_c=60{,}000$: Menter gives 0.035/0.158/0.280, $C_L=0.922$, $C_D=0.0409$; Suluksna–Juntasaro gives 0.037/0.178 with no reattachment, $C_L=0.868$, $C_D=0.0557$; the LES gives 0.04/0.18/0.28, 0.92, 0.043 (Table 6). **Shown**
4. Post-reattachment skin friction from RANS is much smaller than from LES, and Suluksna–Juntasaro gives negative $C_f$ (no reattachment) at $\alpha=8^\circ$. The model "cannot produce a sufficiently large value of the friction coefficient after reattachment", which can lead to early stall (§3.5, Figs. 4–5). **Shown**
5. At $Re_c=30{,}000$, $\alpha=8^\circ$ neither calibration reattaches. Table 7: Menter separates at 0.054 and transitions at 0.250, with $C_L=0.828$, $C_D=0.070$; Suluksna–Juntasaro 0.066, 0.303, 0.71, 0.086; the LES 0.05, 0.25, reattachment at 0.53, 0.89, 0.070. Prediction "deteriorate[s] for decreasing Reynolds numbers and increasing angles of attack" (§3.5, Fig. 6). **Shown**
6. The older separation-induced correction (Eq. 6: 2.193, $R_T/15$, cap 5) outperforms the updated one (Eq. 5: 3.235, $R_T/20$, cap 2) on SD7003 at $Re_c=60{,}000$, $\alpha=4^\circ$. Eq. 6 gives 0.202/0.518/0.660, $C_L=0.600$, $C_D=0.0221$; Eq. 5 gives 0.185/0.535/0.769, $C_L=0.603$, $C_D=0.0259$ (Table 8). Lowering the cap from 5 to 2 reduces the production of $k$ and "considerably delays reattachment" (Fig. 7). **Shown**
7. With Eq. 6 the effective intermittency in separated regions reaches "values well above 3". The production term then "can be over 300% larger than in the natural or bypass transition", which makes the solution insensitive to $F_{\mathrm{length}}$ and $Re_{\theta c}$ (§3.5, Fig. 7). **Shown** (qualitative, contour plot)
8. A hybrid correction that delays transition with the 3.235 threshold but keeps the faster production "could outperform the previous two corrections" (§3.5). **Stated** (suggestion)
9. The model has two flaws: low wall shear stress after transition (premature stall) and early transition and reattachment at intermediate angles of $6^\circ$–$8^\circ$ (§4, Tables 6, 9). At $\alpha=6^\circ$ Menter gives 0.098/0.317/0.44, $C_L=0.767$, $C_D=0.0287$, against LES 0.11/0.34/0.45, 0.748, 0.0319 (Table 9). **Shown**
10. No single constant $s_1$ fits the LES drag at all angles: a low $s_1$ is needed at $6^\circ$ and a high one at $11^\circ$. "The original value of $s_1=2$ seems to be an acceptable compromise" for $4^\circ$, $6^\circ$, $8^\circ$ (§4, Fig. 8). **Shown**
11. Menter's pressure-gradient correction (Eq. 19) causes "a slightly premature transition", possibly through double accounting of pressure-gradient effects, as Malan et al. (2009) suggested (§4, §7). **Shown** (indirectly, through the zero-pressure-gradient comparison); interpretation **Stated**
12. Menter's correlation with $F(\lambda_\theta)=1$ behaves like Suluksna–Juntasaro. It gives 0.184/0.544/0.767, $C_L=0.597$, $C_D=0.0264$, against 0.184/0.530/0.743, 0.600, 0.0257 (Table 10). Simple $Re_{\theta c}$ and $F_{\mathrm{length}}$ correlations therefore do as well as complex ones for separation-induced transition, and the priority is tuning the separation-induced correction (§4). **Shown**
13. Suluksna–Juntasaro with $s_1=6$ gives 0.202/0.536/0.680, $C_L=0.593$, $C_D=0.0228$ (Table 10): forces close to Menter's calibration and a transition location closer to the LES, with similar results at all tested angles (Figs. 9–10). The pressure-gradient correction and the separation-induced correction "play a similar role" (§4). **Shown**
14. A second parameter in the separation-induced correction, independent of $s_1$, would allow bubble position and length to be controlled together (§4, §7). **Stated** (proposal, not implemented)
15. The effect of the free-stream turbulent viscosity ratio is "almost negligible" once the ratio is large enough to avoid a dormant turbulence model. The minimum ratio grows with $Tu$. A ratio of 1 "seems to work adequately", although it is higher than Rumsey & Spalart (2009) recommend for SST. With $Tu=0.43\%$ and a ratio of 0.001 or 0.01 the solution is laminar and inconsistent, with $C_L=-0.0318$ and $-0.0060$ (§3.4, Table 4, Fig. 3). **Shown**
16. Free-stream $Tu$ should not exceed 0.1% and should not be used as a tuning parameter. $Tu=0.03\%$ is used to compare with LES with an ideal free stream, near Langtry's lower stability limit of 0.027% (§3.4). **Stated** (with the sensitivity of Table 4)
17. Grid convergence (SD7003, $Re_c=60{,}000$, $\alpha=4^\circ$): the medium grid (69,834 cells) gives separation at 0.181 and reattachment at 0.741, $C_L=0.6020$, $C_D=0.02585$; the finest (167,084 cells) gives 0.182, 0.741, 0.6016, 0.02574 (Table 3). **Shown**
18. Steady laminar solutions at small $\alpha$ miss trailing-edge vortex shedding, and URANS raises the mean lift. For SD7003 at $Re_c=23{,}000$, $\alpha=2^\circ$: steady $C_L=0.193$, $C_D=0.0273$; unsteady 0.237, 0.0283 (+22.80%, +3.66%) (§5, Table 11, Fig. 11). **Shown**
19. At $Re_c=60{,}000$ only $\alpha<1^\circ$ gives a fully laminar suction side, while at $Re_c=20{,}000$ laminar flow persists up to $3^\circ$–$4^\circ$ (§5). **Stated**
20. At $Re_c=23{,}000$, $\alpha=4^\circ$, unsteady runs with Menter's calibration show a lift drop: early transition from the pressure-gradient correction produces $k$, which damps the unsteadiness. Suluksna–Juntasaro with $s_1=6$ predicts the lift accurately (§5, Fig. 12). **Shown**
21. Near bubble bursting RANS oscillates. URANS either converges to a steady state or keeps suction-side vortex shedding whose time average is a closed bubble. Local instantaneous reattachment can switch off the production of $k$ (Eq. 1) and give near-laminar solutions, more often with Suluksna–Juntasaro than with Menter (§5). **Shown** / **Stated**
22. Once the transients end, steady and unsteady solutions converge, so URANS is not worth its cost there (§5). **Shown**
23. SD7003 at $Re_c=200{,}000$: "agreement is excellent" with the UIUC experiments in lift and drag, and the two calibrations are almost identical. The suction-side features agree with oil-flow visualization, with the trailing-edge bubble moving upstream as $\alpha$ grows (§6.1, Figs. 15–16). **Shown**
24. The model captures the nonlinear, s-shaped lift curve at $Re_c=23{,}000$. Near first reattachment the low-$Re_c$ curves have higher $C_L$ than the high-$Re_c$ ones, because the thicker bubble increases the effective camber, as in Uranga (2010) (§6.1, Fig. 17). **Shown**
25. Ishii airfoil at $Re_c=23{,}000$: the computed lift is systematically higher than experiment and LES (Anyoji et al. 2014). This is attributed to a mismatch in the definition of zero angle (thick trailing edge). After a shift of $+0.587^\circ$ the agreement is good at small $\alpha$, and the discrepancies at and above $6^\circ$ are attributed to three-dimensional flow (§6.2, Fig. 18). **Shown**
26. Eppler 387 at $Re_c=60{,}000$: the two-dimensional results agree with the 2D Navier–Stokes results of Sahin et al. (2008) but not with three-dimensional data. The higher camber of the E387 makes the flow three-dimensional, which is the main limitation of 2D simulation (§6.3, §7, Fig. 19). **Shown** / **Stated**
27. STAR-CCM+'s one-equation $\gamma$ model (Menter et al. 2015) lacks the separation-induced transition constant $C_{\mathrm{SEP}}$, so the paper uses $\gamma$-$Re_\theta$ (§1). **Stated**
28. Polyhedral cells "can potentially speed up simulations convergence" (Peric & Ferguson 2005). Adaptive refinement on pressure and velocity gradients changes the cell count by up to a factor of 2 in massive separation (§3.3). **Stated**

# Printed slips

- **§2, end of the model description.** "through the transport equation for the transition onset momentum thickness Reynolds number (Eq. (11))". The transport equation is Eq. (10), and Eq. (11) is its production term.
- **Eq. (1).** Unbalanced parenthesis: "$\nabla\cdot[(\mu+\sigma_k\mu_t)\nabla k)]$".
- **Eq. (24).** The paper prints "$TVR=\frac{k}{\omega\mu}$". $k/\omega$ has the dimension of a kinematic viscosity and $\mu$ that of a dynamic viscosity, so the printed ratio is not dimensionless. A dimensionless $\mu_t/\mu$ is $\rho k/(\omega\mu)$. *(Compiler check, not in the sources.)*
- **§3.5, "over 300% larger".** The production term is $\gamma_{\mathrm{eff}}P_k$. With $\gamma_{\mathrm{eff}}=3$ it is 200% larger than with $\gamma=1$, and "over 300% larger" needs $\gamma_{\mathrm{eff}}>4$. *(Compiler check, not in the sources.)*
- **Attribution of the two $\gamma_{\mathrm{sep}}$ forms.** §2 says the 3.235 threshold of Eq. 5 is "shown in Menter et al. (2006)" and the 2.193 one "appears in a first version … presented in Langtry et al. (2006)". §3.5 says "The first formulation (Eq. (6)), was introduced by Menter et al. (2004) and was later updated by Langtry and Menter (2009) (Eq. (5))".
- **Table 3 against Table 5.** The grid-study row "Medium/Medium" (0.181, 0.741, $C_L=0.6020$, $C_D=0.02585$) and Table 5's Menter row for the same case (0.202, 0.660, 0.600, 0.0221) differ. The paper does not say which calibration the grid study uses.
- **Conclusions.** "a lack of turbulent kinetic energy production for both calibrations resulting in a failure to reattach the boundary layer after the transition, as observed in LES simulations". The LES of Table 7 does reattach ($x_{\mathrm{re}}/c=0.53$).
- **Branch limits.** Eq. (18) has the branches $Tu<1.3\%$ and $Tu>1.3\%$, and Eq. (19) has $\lambda_\theta<0$ and $\lambda_\theta>0$. The equality cases are not assigned. Eq. (16) reuses $D_1$, $D_2$, $D_3$ in two branches.
- **Spelling.** "Saluksna-Juntasaro Calibration" (§2.1) against "Suluksna" elsewhere; "Polhausen's method"; "untill"; "ouflow".
- **Reference list.** The DOI of Menter et al. (2006) is printed "10.1007/s10494-006-9047", without the final "-1".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\gamma$, $\gamma_{eff}=\max(\gamma,\gamma_{sep})$, $\gamma_{sep}$ | $\gamma$ (intermittency, transition pages only), $\gamma_{\mathrm{eff}}$, $\gamma_{\mathrm{sep}}$ (page-local) | $\gamma_{\mathrm{eff}}$ can exceed 1; caps 2 (Eq. 5) or 5 (Eq. 6) |
| $Re_{\theta_c}$ ($Re_{\theta c}$) | $Re_{\theta c}$ | critical (onset of intermittency growth); printed both ways |
| $Re_{\theta_t}$ | (transition-onset momentum-thickness Reynolds number from the correlation, page-local) | Eq. 18 |
| $\overline{Re}_{\theta_t}$ | $\mathcal R_{\theta t}$ (transported onset Reynolds number, page-local on the transition page) | **collision:** the overbar marks the transported scalar, not the LES filter |
| $Re_v$ | $Re_V$ (page-local, transition page) | strain-rate (vorticity) Reynolds number; no formula printed |
| $R_T$ | (viscosity-ratio argument of the damping) | not defined in the paper |
| $s_1$ | (separation-correction coefficient) | default 2; 6 recommended with Suluksna–Juntasaro |
| $F_{\theta_t}$, $F_{onset}$, $F_{turb}$, $F_{length}$, $F_{sublayer}$ | (blending, onset, relaminarization and transition-length functions) | |
| $c_{a1}$, $c_{a2}$, $c_{e1}$, $c_{e2}$, $c_{\theta_t}$, $\sigma_\gamma$, $\sigma_{\theta_t}$ | (model constants) | values of Menter et al. (2006), not printed |
| $S$, $W$ (in Eqs. 8–9) | $\lvert S\rvert$, $\lvert\Omega\rvert$ | not defined in the paper; the transition page reads them as the strain-rate and vorticity magnitudes (compiler identification) |
| $P_k=G_k+G_{nl}+G_b$, $D_k$ | $P_k$, (destruction of $k$) | turbulent, nonlinear and buoyancy production |
| $\beta^*$, $f_{\beta^*}$, $k_0$, $\omega_0$ | $\beta^*$, (free-shear factor, ambient values of Spalart & Rumsey 2007) | |
| $\mu_t$, $\sigma_k$ | $\mu_t$, $\sigma_k$ | |
| $Tu=\sqrt{2k/3}/U$ | $Tu$ (percent) | |
| $TVR$ | $\mu_t/\mu$ (free-stream viscosity ratio) | printed as $k/(\omega\mu)$, see Printed slips |
| $\lambda_\theta=\frac{\theta^2}{\nu}\frac{dU}{ds}$, $F(\lambda_\theta)$ | (Thwaites parameter, pressure-gradient function, page-local) | $\theta$ is the momentum thickness |
| $H$ | (shape factor $\delta^*/\theta$) | 3.5 at separation |
| $d$ | $d$ | wall distance |
| $x_{sep}/c$, $x_{tr}/c$, $x_{re}/c$ | (separation, transition, reattachment over chord) | $x_{\mathrm{tr}}$ is where $C_f$ starts to drop (§3.5) |
| $C_l$, $C_d$, $c_L$ | $C_L$, $C_D$ | |
| $\alpha$ | (angle of attack) | **collision:** not the DG/FV blending factor |
| $Re$ | $Re_c$ | chord-based |

# Reference list

49 printed references in author–year style (alphabetical, Springer). The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. The authors' own AIAA SciTech 2022 paper on quadrotor blades in
the Martian atmosphere would take the key of this source, but it is a
different work and is keyed apart from it. Langtry's 2006 thesis and the
Part II paper of Langtry et al. (printed with year 2006) are disambiguated in
printed order. The bibliography already records that Part II from another
citing source under the year 2004, and the merge reconciles the two. Menter
(1994) here is the AIAA Journal article. The DOI of Menter et al. (2006) is
printed truncated and is kept only in a note. The corporate or undated items
are the STAR-CCM+ User Guide V. 2019.3, the UIUC Applied Aerodynamics Group
web page (accessed 13 March 2020) and a 2014 Rumsey web page. Two theses
(Langtry 2006, Uranga 2010) are printed without a thesis type. There are no
unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunk 4. This source is cited on:

- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
