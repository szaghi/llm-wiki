---
type: Source
title: "Zhao et al. (2021) — High-order gas-kinetic scheme for large eddy simulation of turbulent channel flows"
description: "Compares implicit LES with the Vreman, dynamic Smagorinsky, WALE and dynamic Clark models in a high-order gas-kinetic finite-volume solver for wall-resolved channel flow at Re_tau 180 and 395, the models entering through an enlarged BGK relaxation time; implicit LES comes out generally best and cheapest."
resource: "doi:10.1063/5.0071059"
source_kind: paper
authors: [Zhao W., Wang J., Cao G., Xu K.]
year: 2021
venue: "Phys. Fluids 33:125102"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2021_Crossref_Physics_of_Fluids_Zhao_High-order_gas-kinetic_scheme_for_large_eddy_simulation_of_t.pdf"
tags: [gas-kinetic, implicit-les, sgs-model, numerical-dissipation, les]
timestamp: 2026-10-27T16:02:00Z
---

# Summary

Zhao et al. (2021) use the [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md),
a finite-volume scheme whose interface flux comes from the time-dependent
BGK solution, with fifth-order [WENO](/methods/weno-scheme.md)
reconstruction with linear weights normal to the face, fourth-order
polynomials along it, $2\times2$ Gauss points per face and two-stage
fourth-order time stepping. They compare [implicit LES](/definitions/implicit-les.md)
with four explicit eddy-viscosity closures of
[large-eddy simulation](/definitions/large-eddy-simulation.md) in
wall-resolved [channel flow](/benchmarks/turbulent-channel-flow.md) at
$Re_\tau=180$ and 395, $M=0.1$: the [Vreman model](/methods/vreman-model.md),
the [Smagorinsky model](/methods/smagorinsky-model.md) with the
[dynamic procedure](/methods/dynamic-procedure.md) and positive-part
clipping (which removes [backscatter](/definitions/energy-backscatter.md)),
the [WALE model](/methods/wale-model.md), and a dynamic Clark
[gradient model](/methods/gradient-model.md) mixed with Smagorinsky whose
coefficient is taken from the dynamic Smagorinsky procedure and whose
stress is converted into an eddy viscosity by matching dissipation. The
models enter the kinetic solver through an enlarged relaxation time
$\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$. A smooth-flow
interface distribution serves at $Re_\tau=180$ and a modified one with a
kinetic upwind part at $Re_\tau=395$.

Against the [DNS](/definitions/direct-numerical-simulation.md) of Kim,
Moin & Moser and of Moser, Kim & Mansour, all methods are close; implicit
LES gives the highest resolved $Re_\tau$, is generally best for mean
velocity, Reynolds stress at $Re_\tau=395$ and vortical structures, and is
cheapest; the dynamic Smagorinsky model is the best explicit model;
spectra show no visible differences. The authors attribute the result to
the scheme's [numerical dissipation](/properties/numerical-dissipation.md)
already sufficing as subgrid dissipation, so that an explicit model
over-dissipates and lowers the wall velocity gradient. No dissipation
budget or a priori analysis is shown. The log-law constants of the
[law of the wall](/definitions/law-of-the-wall.md) set the viscosity. The
WALE constant is taken from a lattice Boltzmann calibration
([lattice Boltzmann methods](/methods/lattice-boltzmann-method.md)).

# Version read

Version of record (AIP; submitted 11 September 2021, accepted
2 November 2021, online 1 December 2021): 20 PDF pages, an AIP cover page
plus article pp. 125102-1 to -19, all read, pp. 2–10 and 13 also visually.
Page 1 matches the metadata; no identity issue. Equation, table and
figure numbers are those of this version.

# Key claims

Page-local symbols: $f$, $g$, $g_0$ the gas distribution, the Maxwellian
and the interface equilibrium; $\tau_{\mathrm{col}}$ the collision time
(as on the [gas-kinetic](/methods/high-order-gas-kinetic-scheme.md) page);
$\tau_{\mathrm{col},t}$ its turbulent enlargement; $C$ the dynamic
Smagorinsky coefficient ($C=C_s^2$); $C_v$ the Vreman constant (as on
the [Vreman](/methods/vreman-model.md) page); $C_w$ the WALE constant;
$C_d$ the dynamic Clark coefficient; $H=\delta=1$ the half-height,
$U_c=1$ the centreline velocity; iLES and V, D, W, DC the implicit LES and
the four models; flux 1 and flux 2 the interface distributions of
Eqs. (7) and (8).

1. In the high-order gas-kinetic finite-volume framework implicit LES is generally superior to explicit LES for mean velocity profiles, Reynolds stress and Q-criterion iso-surfaces in channel flow (Abstract; §VI). **Shown** (for the Reynolds stress at $Re_\tau=180$ see claim 10)
2. Explanation offered: the numerical dissipation of the high-order scheme suffices to replace subgrid dissipation; an explicit model adds dissipation, lowers the near-wall velocity gradient and hence $u_\tau$, and degrades mean profiles and fluctuations (Abstract; §VI). **Stated** (not quantified)
3. Subgrid effects enter through $\partial_tf+u_i\partial_if=(g-f)/(\tau_{\mathrm{col}}+\tau_{\mathrm{col},t})$ with $\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$ from the Chapman–Enskog expansion (§III, Eqs. 12–13, after Chen et al. 2003, 2004). **Stated**
4. Resolved $Re_\tau$ at nominal 180 ($96^3$, flux 1): DNS 178.12, iLES 177.89, V 174.99, D 175.47, W 172.57, DC 172.06; $u_\tau$: iLES 0.0535, V 0.0526, D 0.0527, W 0.0519, DC 0.0517 (Table V). **Shown**
5. Resolved $Re_\tau$ at nominal 395 (flux 2): on $96^3$ DNS 392.24, iLES 360.35, V 351.36, D 359.54, DC 351.35, $u_\tau$ 0.0446, 0.0435, 0.0445, 0.0435 (Table VI); on $128^3$ iLES 376.33, V 370.13, D 375.22, DC 369.57, $u_\tau$ 0.0466, 0.0458, 0.0465, 0.0458 (Table VII). **Shown**
6. "For all cases, the resolved $Re_\tau$ value for iLES is higher than those given by the LES schemes, and the D-model exhibits a superior performance compared to those of the other LES models" (§V; Tables V–VII). **Shown**
7. CPU time per step, $64\times96\times64$, 16 cores: flux 1 iLES 0.520 s, V 0.534, D 0.613, W 0.552, DC 0.624 (Table III); flux 2 iLES 1.014, V 1.023, D 1.111, W 1.048, DC 1.123 (Table IV); flux 2 costs "almost twice" flux 1 (§V). **Shown**
8. At $Re_\tau=180$ the mean velocity in outer units shows no obvious differences (Fig. 2); scaled by the resolved $u_\tau$, all methods have a lower $u_\tau$ than DNS and $u^+$ above DNS in the outer region, iLES closest and D the best explicit model (Fig. 3, §V A). **Shown**
9. At $Re_\tau=395$ on $96^3$ the near-wall grid is "not fine enough", $u_\tau$ is low and the $u^+$ profiles diverge away from the wall; on $128^3$ all improve, iLES still slightly closest (Figs. 4–7, §V A). **Shown**
10. At $Re_\tau=180$ iLES is closest to DNS for the peaks of the streamwise, wall-normal and spanwise rms velocities, but "For the Reynolds stress, the results for D-model match better with DNS, followed by iLES"; D is the best explicit model "because the numerical dissipation in this model is relatively small as a result of the dynamic coefficient" (§V B, Figs. 8–9). **Shown** / explanation **Stated**
11. At $Re_\tau=395$ iLES and D are similar and better than V and DC for the near-wall streamwise rms; iLES is best for the wall-normal and spanwise rms and the Reynolds shear stress (§V B, Figs. 10–13). **Shown**
12. Streamwise and spanwise spectra at $y^+=30$ and 395 ($Re_\tau=395$) show no obvious differences; all show an "unnatural leveling-off" near the cutoff, attributed to insufficient resolution (§V C, Figs. 14–15). **Shown**
13. Q-criterion iso-surfaces ($Q=0.5$): iLES and D resolve more vortical structures than the other models on $96^3$; on $128^3$ iLES resolves more than all explicit models (§V D, Figs. 16–19). **Shown** (qualitative)
14. The $Re_\tau=395$ iLES results resemble the fifth-order WENO finite-volume iLES of Kokkinakis & Drikakis (2015) (§V A–C). **Stated** (not overlaid)
15. Flux 1 suffices at $Re_\tau=180$ because velocity gradients and interface discontinuities are small and the central character of the scheme keeps numerical dissipation low; at $Re_\tau=395$ interface discontinuities appear and the upwind part must be improved (§IV). **Stated**, Appendix A **Shown**
16. Appendix A: at $Re_\tau=180$ flux 1 is better than flux 2; at $Re_\tau=395$ flux 2 gives better turbulence intensities, flux 1 a slightly closer mean velocity, flux 2 being "a little larger" in dissipation; overall flux 2 is better at 395 (Figs. 22–27). **Shown**
17. Appendix B: refining the $Re_\tau=180$ grid ($64^3$, $64\times96\times64$, $96^3$) improves mean velocity, rms and Reynolds stress; "when the grids are refined, the numerical dissipation decreases" (Table VIII, Figs. 28–30). **Shown** / mechanism **Stated**
18. Vreman constant: $C_v$ from 0.01 to 0.1 tested at $Re_\tau=180$, best 0.01 used; $C_v=0.07$ at $Re_\tau=395$ after Vreman (2004) (§IV); the model is written $\mu_t=\bar\rho C_v\sqrt{B_\beta/(\alpha_{ij}\alpha_{ij})}$, $C_v=2.5C_s^2$ (Eq. 17). **Shown** (tuning results not displayed)
19. WALE: $C_w=0.5$ after the Weickert et al. (2010) calibration for $Re_\tau=395$ channel flow, also recommended for pipe flow by Nicoud & Ducros; $C_w^2\approx10.6C_s^2$ in isotropic turbulence (§III C, §IV). **Stated**
20. Transition from laminar flow takes about $400H/U_c$, statistics are averaged over $200H/U_c$, with constant flow rate kept by a body force (§IV). **Stated**
21. High- and low-speed streaks at $y^+=70$ ($Re_\tau=180$) and $y^+=100$ ($Re_\tau=395$) are elongated streamwise and finer at higher $Re_\tau$ (§V D, Figs. 20–21). **Shown** (qualitative)
22. Dynamic Clark model as used: $\tau_{ij}=\tfrac1{12}\Delta^2\partial_k\bar u_i\partial_k\bar u_j-C_d\Delta^2\overline{|\bar S|\bar S_{ij}}$ (Eq. 20) with $C_d$ set equal to the dynamic Smagorinsky coefficient, converted to $\nu_t=-\tau_{ij}\bar S_{ij}/(2\bar S_{ij}\bar S_{ij})$ by matching the dissipation of $\tau_{ij}=-2\nu_t\bar S_{ij}$ (Eqs. 21–23); clipping of a negative $\nu_t$ is not stated (§III D). **Derived**
23. Conclusion: in this high-order finite-volume approach iLES is "more suitable than traditional LES models", and the dynamic Smagorinsky model is the best explicit one (§VI). **Stated**

# Printed slips

- **Viscosity at $Re_\tau=180$:** printed $\mu=2.83\times10^{-4}$ (p. 9). Eqs. (25)–(26) give $U_c^+=2.5\ln180+5.5=18.48$, $u_\tau=1/18.48=0.0541$, $\mu=u_\tau/Re_\tau=3.006\times10^{-4}$; Table V gives $u_\tau/Re_\tau=0.0535/177.89=3.008\times10^{-4}$ and $0.0526/174.99=3.006\times10^{-4}$. The same procedure at $Re_\tau=395$ gives $1.238\times10^{-4}$, matching the printed $1.24\times10^{-4}$ *(compiler check, not in the sources)*.
- **Table VIII, $\Delta z^+$:** printed 8.33 for $N_z=64$ (G2, G3). $\pi\cdot180/64=8.84$, while $\Delta x^+=2\pi\cdot180/64=17.67$ matches the printed 17.66 *(compiler check, not in the sources)*.
- **Internal degrees of freedom (§II):** printed "$N=(5-3\gamma)(\gamma-1)$". For $\gamma=1.4$ the product gives 0.32, the quotient $(5-3\gamma)/(\gamma-1)$ gives 2 *(compiler check, not in the sources)*.
- **Eq. (16):** printed $C=[\langle M_{ij}L_{ij}\rangle/\langle M_{kl}M_{kl}\rangle]_+$ with $L_{ij}$ and $M_{ij}=\hat\Delta^2|\hat{\bar S}|\hat{\bar S}_{ij}-\Delta^2\widehat{|\bar S|\bar S_{ij}}$ as printed. With Eq. (15), the modelled deviatoric stress $-2C\Delta^2|\bar S|\bar S_{ij}$ turns the Germano identity into $L^d_{ij}=-2CM_{ij}$, whose least-squares solution is $C=-\tfrac12\langle L_{ij}M_{ij}\rangle/\langle M_{kl}M_{kl}\rangle$ *(compiler check, not in the sources)*.
- **Eqs. (21)–(23) against Eq. (13):** the conversion yields a kinematic $\nu_t$, while the coupling needs $\mu_t$; $\mu_t=\bar\rho\nu_t$ is not stated.
- **p. 12:** "DNS ... by Moser et al.$^1$", but ref. [1] is Kim, Moin & Moser (1987).
- **Fig. 20 caption:** dashed levels "0.2, −0.4, −0.6, −0.8, and −1".
- **WALE at $Re_\tau=395$:** §IV says "We use the same $C_w$ value for our channel-flow simulation" at $Re_\tau=395$, but Tables VI–VII and Figs. 4–19 carry no WALE results at $Re_\tau=395$.
- **Abstract and §VI against §V B:** implicit LES is called superior for the Reynolds stress, while §V B states that at $Re_\tau=180$ the dynamic Smagorinsky model matches DNS better, followed by implicit LES.
- Typographical: "S. Chi-Wang" for Chi-Wang Shu in ref. [36]; "progress" for "process" (§III B).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tau$ | $\tau_{\mathrm{col}}$ (registry §11) | BGK collision time; **collision:** not a stress |
| $\tau_t$ | $\tau_{\mathrm{col},t}$ (registry §11) | **collision:** the registry's $\tau_t$ is the $k$-$\tau$ time scale |
| $u_i$ in the BGK equation, $\xi$, $N$ | particle velocity, internal variables, their number | **collision:** $\xi$ is not the reference coordinate, $N$ not the polynomial degree |
| $\bar{(\cdot)}$ ($\bar U_i$) | $\bar\phi$ ($\bar u_i$) | resolved (cell-averaged) quantity; agrees; overbars on the coefficients $\bar a$, $\bar A$ of Eqs. (4)–(8) are equilibrium coefficients, not filters |
| $\tilde{(\cdot)}$, $\tilde{\bar\Delta}$ | $\hat\phi$, $\hat\Delta=2\Delta$ | **collision:** the source's tilde is the test filter, not a Favre filter |
| $\bar\Delta=(\bar\Delta x_1\bar\Delta x_2\bar\Delta x_3)^{1/3}$, $\bar\Delta_m$ | $\Delta$, $\Delta_k$ | |
| $\bar S_{ij}$, $\lvert\bar S\rvert=(2\bar S_{ij}\bar S_{ij})^{1/2}$, $\bar\Omega_{ij}$ | same | factor two included; agrees |
| $\bar S^d_{ij}$ (Eq. 18) | (WALE traceless square of the velocity gradient) | **collision:** not the registry's deviatoric strain $S^d_{ij}$ |
| $C(y,t)$, $C_s$ | $C=C_s^2$, $C_s$ | dynamic coefficient without the square split |
| $c$ | $C_v$ | Vreman constant, as on the Vreman page |
| $L_{ij}$, $M_{ij}$ | $L_{ij}$ (with $\hat\phi$), $M_{ij}$ | |
| $\tau_{ij}$ (Eq. 19), $\tau^r_{ij}$ | $\tau_{ij}$ | positive convention; agrees |
| $\mu$, $\mu_t$, $\nu_t$ | same | |
| $\omega_{mn}$ | $w_i$ | Gauss weights; **collision:** not $\omega$ |
| $H$, $U_\tau$, $\tau_{wall}$, $Y^+$, $U^+$ | $\delta$, $u_\tau$, $\tau_w$, $y^+$, $u^+$ | |
| $\kappa=0.40$, $B=5.5$ | $\kappa$, $B$ | |
| $b_g$, $\eta$ | (stretching parameter, uniform grid coordinate) | **collision:** $\eta$ is not the Kolmogorov length |
| $\langle\cdot\rangle_{ave}$, $\langle\cdot\rangle_{xz}$ | $\langle\cdot\rangle$ over $x$, $z$ | |
| $RS(U'_iU'_j)$, $RMS(U'_i)$ | $R_{ij}/u_\tau^2$, rms over $u_\tau$ | normalized by the resolved friction velocity |
| $Ma$ | $M$ | |
| $Q$ | $Q$ (page-local) | Q-criterion, Eq. (29); **collision:** not the vector of conservative variables |

# Reference list

48 printed references, numbered (superscript) AIP style with titles. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Ref. [38] (Cao, Pan & Xu 2022) is the ingested
[cao-2022](/sources/cao-2022.md). Same-author same-year works follow
printed order and are matched to existing keys by volume and page
(`cao-2019`, `li-2016`, `pan-2016` families). Ref. [4] (Manabe,
Smagorinsky & Strickler 1965) is the paper's citation for the Smagorinsky
model; ref. [29] prints Comput. Math. Appl. 78 with year 2016. No item is
unparseable.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Gradient (Clark) model and the clipping of structural SGS models](/methods/gradient-model.md)
- [High-order gas-kinetic schemes for turbulence simulation](/methods/high-order-gas-kinetic-scheme.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Vreman model](/methods/vreman-model.md)
- [WALE model](/methods/wale-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
