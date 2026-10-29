---
type: Source
title: "Akbarzadeh & Borazjani (2025) — Parallel large eddy simulations with curvilinear immersed boundary method for high-speed flows"
description: "Extends a sharp-interface curvilinear immersed boundary method to compressible LES with a dynamic Smagorinsky model, a hybrid skew-central/WENO flux and wall functions built into the boundary reconstruction; validated on isotropic turbulence, channels, a Mach-3 cylinder and shock diffraction, where the wall model matters more than the SGS model."
resource: "doi:10.1016/j.compfluid.2024.106495"
source_kind: paper
authors: [Akbarzadeh A.M., Borazjani I.]
year: 2025
venue: "Comput. Fluids 288:106495"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Computers_amp_Fluids_Akbarzadeh_Parallel_large_eddy_simulations_with_curvilinear_immersed_bo.pdf"
tags: [immersed-boundary, compressible, wmles, weno, shock-capturing, numerical-dissipation]
timestamp: 2026-10-29T07:41:00Z
---

# Summary

Akbarzadeh & Borazjani (2025) extend their sharp-interface curvilinear
[immersed boundary method](/methods/immersed-boundary-method.md) (CurvIB,
compressible version of Borazjani 2021) to
[large-eddy simulation](/definitions/large-eddy-simulation.md) of
high-speed flows. The Favre-filtered equations in curvilinear coordinates
are closed by the compressible
[Smagorinsky model](/methods/smagorinsky-model.md) of Moin et al. with the
[dynamic procedure](/methods/dynamic-procedure.md) (test filter a
$3\times3\times3$-cell cube) and a Yoshizawa isotropic part with
$C_I=0.06$. Convective fluxes blend a fourth-order skew-symmetric central
flux (Ducros et al.) with a third-order
[WENO](/methods/weno-scheme.md) flux through a smooth tanh switch driven by
a pressure-ratio [shock sensor](/definitions/shock-sensor.md). At immersed
boundary nodes the velocity is reconstructed along the wall normal; when
the viscous sublayer is not resolved, the linear tangential interpolation
is replaced by a log-law [wall function](/methods/rans-wall-function.md) or
by an integrated stress-balance
[equilibrium wall model](/methods/equilibrium-wall-model.md) with a damped
mixing-length eddy viscosity. The code is in C with MPI and PETSc.

Validation covers decaying compressible
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
($M_t=0.4$, $Re_\lambda=153$), a compressible
[channel](/benchmarks/turbulent-channel-flow.md) at $M=0.5$ and 1.5 with the
walls as immersed boundaries, a Mach-3
[circular cylinder](/benchmarks/circular-cylinder-wake.md) in a small and a
large domain, and diffraction of a Mach-2.81 moving shock by a cylinder,
with a [shock/boundary-layer](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
vortex. Fine grids and the hybrid scheme are needed to capture the
Kelvin–Helmholtz instability of the contact lines and that vortex; pure
WENO-3 or coarse grids damp them through
[numerical dissipation](/properties/numerical-dissipation.md). On fine grids
the explicit SGS model matters little because WENO supplies dissipation
implicitly ([implicit LES](/definitions/implicit-les.md)); the dynamic,
constant and no SGS model give the same reattachment length behind the
cylinder, while the wall model dominates: the log law gives $x_R=2.8$
against 1.04 in the experiment, the stress-balance model a similar value,
and a slip wall 1.1 ([wall-modelled LES](/methods/wall-modelled-les.md)).
The paper's "slip wall model" applies on the cylinder the slip condition
of its inviscid runs (§3.3); the dynamic slip wall model of Bose & Moin is
named as future work (§5). Strong
scaling exceeds 90% from 1536 to 4800 cores; LES costs about twice an
inviscid run. The central part is the fourth-order skew-symmetric flux of
Ducros et al., as cited (see
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md));
no conservation property is claimed. References: DNS of Samtaney
et al., Lee & Moser, Modesti & Pirozzoli
([DNS](/definitions/direct-numerical-simulation.md)).

# Version read

Version of record (Elsevier; received 20 May 2024, accepted 21 November
2024, online 6 December 2024), 15 pages, all read, the equations of
pp. 2–3 checked visually. Page 1 matches the metadata; no identity issue.
Equation, figure, table and section numbers are those of this version.

# Key claims

Page-local symbols: $u^n$, $u^t$ normal and tangential velocity at the wall
point $a$, the boundary node $b$ and the fluid point $c$ on the normal
through $b$ (Fig. 1), with $y^+_b$, $y^+_c$ their wall distances in wall
units; $\sigma_b$ the WENO fraction of the hybrid flux (registry §11; the
source writes $\sigma$ for the central fraction, $\sigma_b=1-\sigma$);
$r_{\mathrm p}$ the pressure smoothness indicator and $r_{\mathrm{th}}$ its
threshold (registry §11) (the source's $r_i$, $r_d$); $\nu_t^{\mathrm{wm}}$ the wall-model eddy viscosity;
$\alpha_{\mathrm E}$ the SGS term of the energy equation; $M_s$ the moving
shock Mach number; $x_b$ the bow-shock stand-off.

1. A sharp-interface immersed boundary method, reconstructing variables directly at boundary nodes by interpolation along the wall normal (no ghost cells), is extended to LES of high-speed compressible flows with wall functions built into the interpolation; the authors argue this makes wall models straightforward to implement, contrasting the ghost-cell approaches of van Noordt et al. [23] and De Vanna et al. [25] (§1). **Stated**
2. Non-dissipative schemes (central, compact) "are unconditionally unstable for high-speed flows that are governed by hyperbolic-type partial differential equations", which motivates hybrid WENO/central schemes (§1). **Stated**
3. The SGS stress is the compressible eddy-viscosity form of Moin et al. [6], Eqs. (7)–(9), with the coefficient computed dynamically by Eq. (10), a $3\times3\times3$-cell test filter, and averaging in homogeneous directions or, if none, over the test-filter cube (§2.1). **Stated**
4. Convective fluxes are $(1-\sigma_b)f^{\mathrm{central}}+\sigma_bf^{\mathrm{WENO}}$ at each face (Eq. 13), with a fourth-order skew-central flux (Eq. 14) and a third-order WENO flux, blended by the tanh switch of Eq. (15) built from the pressure indicator of Eq. (16) (§2.2). **Stated**
5. Near domain and immersed boundaries the discretization reverts to one-sided ENO (WENO part) and second-order central (central part), to avoid nodes outside the domain or inside solids (§2.2). **Stated**
6. Log-law wall model: $u_\tau$ from Eqs. (19)–(21) with $\kappa=0.42$, $B=5.2$, solved iteratively; boundary-node velocity from Eqs. (22)–(24) with a linear/log switch at $y^+_b=11.0$ (§2.4); the model "works properly when the flow is attached and the boundary layer is turbulent" but not for separated or transitional flows. **Stated**
7. The wall-stress-balance model, Eqs. (25)–(27), with a damped eddy viscosity and $u_\tau$ from Newton iteration, is presented as more suitable for separated and transitional flows (§2.4). **Stated**
8. Decaying isotropic turbulence: at $t/T_E=5$ the spectrum follows the "5/3 power law"; the kinetic-energy history agrees with DNS [43] for $t/T_E>2$, with a small discrepancy for $t/T_E<2$ attributed to the coarser resolution, since the LES of Li et al. [44] at similar resolution shows the same (§3.1, Fig. 2d–e). **Shown**
9. Channel at $M=0.5$ and 1.5, $Re_b=10\,000$ (bulk velocity, half-height): wall-resolved LES mean velocity agrees with DNS [45, 46] on grids 1 and 2; the wall-modelled LES on grid 3 ($24^3$) "cannot follow the log-law profile" because of low resolution; Reynolds stresses agree better with refinement (§3.2, Fig. 5). **Shown**
10. The $M=0.5$ channel is compared with incompressible DNS because below Mach 0.6 the flow is "quasi-incompressible" (§3.2). **Stated**
11. On fine grids the LES eddy viscosity rises sharply from the viscous sublayer to a peak near $y/\delta=0.05$ and decays smoothly; on coarser grids the peak moves towards $y/\delta\approx0.25$; the hybrid scheme also produces implicit (WENO) dissipation that affects the turbulence and the eddy viscosity (§3.2, Fig. 4). **Shown**
12. Loss of agreement on coarse grids is attributed to the implicit dissipation of the third-order WENO part, which a higher WENO order would reduce; Klapwijk et al. [47] report up to 30% discrepancy in the peak Reynolds stress on a coarse grid (§3.2). **Stated**
13. Mach-3 cylinder, small domain: the Kelvin–Helmholtz instability of the two contact lines from the bow-shock triple points is captured by the hybrid scheme on the fine grid ($h=0.0025$) and by LES, but not by pure third-order WENO nor by the hybrid on the coarse grid ($h=0.01$), "because of large numerical diffusion" (§3.3.1, Figs. 6–8). **Shown**
14. The drag coefficient peaks at about 2.25 at impingement and settles at about 1.1 in the periodic state; all schemes and the 3D run give close values, LES slightly higher periodic drag (attributed to earlier separation with no-slip); global features are "mostly independent of the smaller scale instabilities" (§3.3.1, Fig. 9). **Shown**
15. Bow-shock stand-off: Billig's formula $x_b/D=0.193\exp(4.67/M^2)$ gives 0.324 at $M=3$; the simulations give about 0.35 in both domains, "within the accuracy of the formula", which under-predicts measurements from $M=2.7$ to 4 [51] (§3.3.2). **Shown**
16. Large domain ($Re_D=750\,000$, experiment of Awasthi et al. [50]): no triple points on the bow shock and the wake reattaches; reattachment distance from the cylinder centre $x_R=1.04$ in the experiment against 2.8 in 2D wall-modelled LES with the log law (§3.3.2). **Shown**
17. The SGS model (dynamic, constant, none) did not affect the reattachment length, the wall model did: LES with a slip wall reproduced the inviscid hybrid result and gave $x_R=1.1$, while the log-law and stress-balance ("Cabot") models, both wall-stress models, gave similar, much longer separation; "Cabot will produce log-law under equilibrium conditions [52]" (§3.3.2, Fig. 12). **Shown** (the equivalence **Stated**)
18. 3D wall-modelled LES (log law and slip) give reattachment lengths similar to the 2D runs, so the 2D discrepancies are not due to two-dimensionality (§3.3.2, Fig. 13). **Shown**
19. Shock diffraction ($M_s=2.81$): on $h=0.001$ at $Re=8763$ the LES with the hybrid scheme captures all experimental features (reflected, incident and Mach shocks, two triple points, contact discontinuity) and the shock/boundary-layer-interaction vortex, located as in the experiments [53]; third-order WENO on the same grid does not capture the vortex (§3.4, Figs. 14–15). **Shown**
20. The vortex does not appear at $h=0.002$ nor at the lower Reynolds number on $h=0.001$; against Bryson & Gross's attribution to their measuring technique, the authors conclude that the vortex does not form at low $Re$, and that raising dissipation physically (lower $Re$) or numerically (dissipative schemes, coarse grids) prevents it (§3.4, Fig. 16). **Shown**
21. 2D small domain (5.1 million nodes), 200 000 steps on 896 cores of Terra: inviscid 2 h 20 min, LES 4 h 56 min, "about 2 times more expensive" (§4). **Shown**
22. 2D large domain (about 8.7 million nodes): inviscid 200 000 steps in 3 h on 46 nodes (1288 cores); LES 100 000 steps in about 4.5 h on 36 nodes (1008 cores) (§4). **Shown**
23. Strong scaling, 3D large-domain log-law case with over 313 million nodes on Grace (48 cores per node, GPUs not used): about 4, 2.1 and 1.4 h per 10 000 iterations on 32 (1536 cores), 64 (3072) and 100 (4800) nodes; speedup "very close to the ideal", efficiency "over 90%" (§4, Fig. 17a). **Shown**
24. Weak scaling (shock-diffraction case, grids from $1201\times1001\approx1.2\times10^6$ on 48 cores to $6001\times4001\approx24\times10^6$ on 960 cores): efficiency drops slightly, to 84% at about 1000 cores (§4, Fig. 17b). **Shown**
25. Required resolutions for the method: $h=0.0025$ to capture both instabilities and shocks over the Mach-3 cylinder, $h=0.001$ for the shock/boundary-layer vortex; the third-order WENO may have raised the grid requirements relative to the fifth-order WENO, which needs a 5-point stencil, more ghost nodes and more communication (§5). **Shown** / **Stated**
26. Simulations of high-speed flow over the cylinder "are more sensitive to the wall model than the LES subgrid model", hence the need for better wall models for high-speed flows; future work: the dynamic slip wall model of Bose & Moin [57] (§5). **Shown** (on the cases of the paper)
27. On fine grids "the importance of explicit LES modeling decreases as most scales are resolved and the WENO scheme provides the dissipation implicitly" (Abstract, §3.3.2). **Shown**
28. 2D and 3D LES of the supersonic cylinder agree on large-scale features but "other measures, e.g., turbulence statistics, greatly differ"; 2D turbulence is not a reduced version of 3D turbulence (citing Boffetta & Ecke [58]) (§5). **Stated** (statistics not shown)

The closures in registry notation (Eqs. 7–9, 19–27):
$\tau_{ij}=\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)=-2\mu_t\tilde S^d_{ij}+\tfrac23\bar\rho k_{\mathrm{sgs}}\delta_{ij}$,
$\mu_t=\bar\rho(C_s\Delta)^2|\tilde S|$ with the dynamic coefficient of
Eq. (10), $\bar\rho k_{\mathrm{sgs}}=C_I\bar\rho\Delta^2|\tilde S|^2$,
$C_I=0.06$ ($\Delta$ "the grid filter size", not otherwise defined). The
switch is
$1-\sigma_b=\tfrac12\tanh\!\big(3(r_{\mathrm p}-r_{\mathrm{th}})/\max(r_{\mathrm{th}},|r_{\mathrm p}-r_{\mathrm{th}}|)\big)/\tanh3+\tfrac12$
with $r_{\mathrm p}=(|2\Delta p_{i+1/2}\Delta p_{i-1/2}|+\epsilon)/(\Delta p_{i+1/2}^2+\Delta p_{i-1/2}^2+\epsilon)$
taken as the minimum of the two cells, $\epsilon<10^{-10}$. Wall models:
$u^+_c=\kappa^{-1}\ln y^+_c+B$ solved for $u_\tau$, then
$u^t_b=u^t_a+u^+_bu_\tau$; or
$u^t_b-u^t_a=(u^t_c-u^t_a)\int_0^{|ab|}\frac{dl}{\nu+\nu^{\mathrm{wm}}_t}\big/\int_0^{|ac|}\frac{dl}{\nu+\nu^{\mathrm{wm}}_t}$,
$\tau_w/\rho=(u^t_c-u^t_a)\big/\int_0^{|ac|}\frac{dl}{\nu+\nu^{\mathrm{wm}}_t}$,
$\nu^{\mathrm{wm}}_t/\nu=\kappa^{-1}y^+_b(1-e^{-y^+})$ as printed. Normal velocity
by linear interpolation in all regimes, $p_b=p_c$ at a stationary wall,
adiabatic wall with $\rho_a=\rho_b=\rho_c$ (Eqs. 17, 28–29).

# Printed slips

- **Eq. (14):** the last term of the skew-central flux is printed $\tfrac14(v_{i+1}+w_i)(v_{i+1}+w_i)$. *(Compiler check, not in the sources: for the printed pairs $(v,w)=(\rho u_1,U^1)$ or $(\xi^1_{x_1},p)$ the sum $v+w$ adds quantities of different dimensions.)*
- **Eq. (23):** the log branch is printed $\frac1\kappa\ln(y^+_c)+B$ while the condition is on $y^+_b$ and the text says "$u^+_b$ is calculated".
- **Eq. (15):** the threshold $r_d$ is never defined or given a value.
- **Eqs. (1) and (11):** "$\frac{\partial\mathbf Q}{t}$" and "$\frac{\partial}{\xi^q}$", each missing a $\partial$.
- **§3.2:** "$\Delta y^+=u_\tau\Delta y/\mu$" (with $\mu$, not $\nu$).
- **§3.1:** "The turbulence fluctuation velocity is $\langle u_i^2/3\rangle$", printed without a square root; "the theoretical 5/3 power law" without the sign.
- **§3.4:** the low Reynolds number is printed 877 and 873 in the text and 876 in the Fig. 16 caption (the high value is 8763).
- **§4, weak scaling:** "$6001\times4001\approx24\times10^6$ grid nodes on 10 nodes (960 cores)" and "$3001\times4001\approx12\times10^6$ … on 10 nodes (480 cores)". *(Compiler check, not in the sources: at the stated 48 cores per Grace node, 960 cores are 20 nodes.)*
- **§3.3.2:** "$2340\times1349\times101$ and $2300\times1349\times101$ ≈ 319 million grid nodes, respectively" gives one figure for two grids. *(Compiler check, not in the sources: the products are 318.8 and 313.4 million; §4 says "over 313 million" for the log-law case.)*
- **Attribution:** the stress-balance wall model is cited to [40] (Wang & Moin) and [41] (Kang et al.) in §2.4 and called the "Cabot wall model" [52] in §3.3.
- **§2.1:** "$\tilde p=(\gamma-1)(\bar\rho E-0.5\bar\rho\tilde u_r\tilde u_r)$ is filtered pressure", while Eq. (2) uses $\bar p$; Eq. (10) mixes $\rho$, $\bar\rho$, $\hat\rho$ and unfiltered $u$, $S$, and closes the bracket after the second term of the numerator, so $S_{kl}$ multiplies only that term as printed.
- **Eqs. (25), (27):** the numerator of (25) uses $\nu+\nu_t$ and the denominator $1/Re+\nu_t$; (27) has $y^+_b$ in the prefactor and an unsubscripted $y^+$ in the exponent.
- **Eq. (30):** $\lambda^2=u'^2/\langle(\partial u_i/\partial x_i)^2\rangle$. *(Compiler check, not in the sources: with the summation convention declared in §2.1 the denominator is the mean-square divergence, zero for the divergence-free initial field.)*
- **Table 1:** Grid 1 $\Delta z^+_{\min}=73.348$ and Grid 3 $\Delta x^+_{\min}=73.248$ for the same spacing 0.131.
- **§3.2:** the paragraph on the validation of wall-bounded flows is printed twice nearly verbatim; "maximum pick of Reynolds stress"; Fig. 11 caption "WLES". §3.3.1 defines $C_D=F/(\tfrac12\rho_\infty u_\infty^2D^2)$ with $D^2$. Abstract "dynamics Smagornisky model"; §5 "were turbulence is key". Ref. [52] has no title.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\xi^q$, $\xi^q_{x_r}$ | $\xi_i$, metric terms | curvilinear coordinates |
| $J=\lvert\partial(\xi^1,\xi^2,\xi^3)/\partial(x_1,x_2,x_3)\rvert$ | $1/\mathcal J$ | the source's $J$ is the physical-to-reference determinant |
| $\bar{(\cdot)}$, $\tilde{(\cdot)}$, $\widehat{(\cdot)}$ | $\bar\phi$, $\tilde\phi$, $\hat\phi$ | filter, Favre filter, test filter as in the registry |
| $\tau_{rm}=\bar\rho\widetilde{u_ru_m}-\bar\rho\tilde u_r\tilde u_m$ | $\tau_{ij}$ (compressible, positive trace) | enters as $\tilde\sigma-\tau$ |
| $\mu_t=C_s\bar\rho\Delta^2\lvert\tilde S\rvert$ | $\mu_t=\bar\rho(C_s\Delta)^2\lvert\tilde S\rvert$ | **the source's $C_s$ is the registry $C_s^2$** |
| $\tfrac13\bar\rho k^2$, $\bar\rho k^2=2C_I\bar\rho\Delta^2\lvert\tilde S\rvert^2$ | $\tfrac23\bar\rho k_{\mathrm{sgs}}$, $C_I$ | the source's $k^2$ equals $2k_{\mathrm{sgs}}$ by the trace of Eq. (7) |
| $\lvert\tilde S\rvert=\sqrt{2\tilde S_{rm}\tilde S_{rm}}$ | $\lvert\tilde S\rvert$ | factor two included |
| $E$ | $E/\rho$ | the source's $E$ is per unit mass |
| $\alpha$ | $\alpha_{\mathrm E}$ (page-local) | energy SGS term; **collision** with the DG blending factor $\alpha$ |
| $\sigma_{i+1/2}$ | $1-\sigma_b$ | central fraction of the hybrid flux |
| $r_i$, $r_d$ | $r_{\mathrm p}$, $r_{\mathrm{th}}$ (page-local) | **collision** with the DDES argument $r_d$ |
| $\nu_t$ (Eqs. 25–27), $\tau_t$ | $\nu^{\mathrm{wm}}_t$ (page-local), $\tau_w/\rho$ | wall-model eddy viscosity; kinematic wall stress |
| $\kappa=0.42$, $B=5.2$ | $\kappa$, $B$ | |
| $\tau$ (Eq. 32) | $T_E$ | initial large-eddy turnover time |
| $M_t=u'/c$, $Re_\lambda$, $\lambda$ | $M_t$, $Re_\lambda$, $\lambda$ | |
| $H$, $Re=\rho UH/\mu$ (channel) | $\delta$, $Re_b$ | channel half-height, bulk velocity |
| channel $z$ streamwise, $x$ spanwise | $x$ streamwise, $z$ spanwise | $y$ wall-normal in both |
| $h$ | $h$ | uniform grid size of the cylinder cases |
| $x_r$ | $x_R$ | reattachment distance from the cylinder centre |
| $M_s$, $x_b$ | (page-local) | shock Mach number; bow-shock stand-off |

# Reference list

58 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [23] is the
ingested [vannoordt-2022](/sources/vannoordt-2022.md). Ref. [52] (Cabot &
Moin, Flow Turbul. Combust. 63:269–291) is printed without a title; [42]
is the PETSc web page; [1] prints only an article number; [57] (Bose &
Moin 2014) has no page or article number. The two Akbarzadeh & Borazjani
2019 works [30], [31] are keyed in printed order; [14] is keyed under the
printed surname "Xiaoshuai". The cited works under the keys `lee-2009`,
`lee-1991`, `wang-2017`, `bernardini-2016`, `li-2017` and `chaudhuri-2011`
are different works from the bibliography entries already holding those
keys and are keyed `lee-2009-c`, `lee-1991-b`, `wang-2017-r`, `bernardini-2016-b`, `li-2017-g` and `chaudhuri-2011-c`. No item is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
