---
type: Source
title: "Heinz (2020) — A review of hybrid RANS-LES methods for turbulent flows: Concepts and applications"
description: "Single-author review that classifies hybrid RANS/LES into wall-modelled LES, source-term, RANS-bound and RANS-coefficient methods, criticizes each, derives the continuous-eddy-simulation coefficient from a variational analysis, and compiles periodic-hill, hump, transonic-bump and NACA 4412 results from the literature."
resource: "doi:10.1016/j.paerosci.2019.100597"
source_kind: paper
authors: [Heinz S.]
year: 2020
venue: "Prog. Aerosp. Sci. 114:100597"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2020_Crossref_Progress_in_Aerospace_Sciences_Heinz_A_review_of_hybrid_RANS-LES_methods_for_turbulent_flows_Conc.pdf"
tags: [hybrid-rans-les, des, pans, rans, separated-flow, review]
timestamp: 2026-10-27T15:55:00Z
---

# Summary

Heinz (2020) reviews [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
around one question: how a hybrid controls the balance of modelled and
resolved motion when the grid and the Reynolds number change. A common
framework comes first (§2). The Reynolds stress (RANS) or subgrid stress
(LES) is read as the variance of a velocity PDF or filtered density function
governed by a Fokker–Planck model. From it the author derives the
[Boussinesq](/definitions/boussinesq-hypothesis.md) algebraic stress, the
[$k$-$\varepsilon$](/methods/k-epsilon-model.md) and
[$k$-$\omega$](/methods/k-omega-model.md) models with their
[log-law](/definitions/law-of-the-wall.md) consistency conditions, and the
mode relations $R_{ij}=R^{\mathrm{res}}_{ij}+\langle\tau_{ij}\rangle$,
$k_{\mathrm{tot}}=k_{\mathrm{res}}+k$. RANS and LES equations are said to
differ only in the scale they are supplied with.

§3 sorts existing hybrids into four groups:
[wall-modelled LES](/methods/wall-modelled-les.md), source-term methods,
RANS-bound methods ([DES](/methods/detached-eddy-simulation.md), the
author's unified RANS-LES, Reynolds-stress-constrained LES) and
RANS-coefficient methods ([PANS](/methods/partially-averaged-navier-stokes.md),
PITM, [SAS](/methods/scale-adaptive-simulation.md)). It names a conceptual
weakness of each. PANS and PITM, for instance, drop a transport difference
and so hold strictly only in homogeneous turbulence.

§4 summarizes the author's earlier variational analysis (Heinz 2019), the
basis of [continuous eddy simulation](/methods/continuous-eddy-simulation.md)
(CES). The destruction coefficient of the $\varepsilon$ (or $\omega$)
equation becomes $1+L_+^2(\alpha_\varepsilon-1)$, which makes $L_+^2$ the
resolution measure; four model variants follow, and a CES–DES equivalence
gives $C_{DES}$ values of 0.75 and 0.61, "not far from the standard value" 0.65.

§5 compiles published results on the [periodic hill](/benchmarks/periodic-hill.md),
the [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md), the
Bachalo–Johnson transonic axisymmetric bump and the
[NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md). From these the author
argues that existing hybrids show prediction variability through design
parameters, resolution deficiencies and inconsistent improvements. The
review runs no simulation of its own. The conclusions favour hybrids built
in a single equation framework, such as CES.

# Version read

Version of record (Elsevier, Prog. Aerosp. Sci. 114:100597; received
31 October 2019, online 19 March 2020); 25 pages (text and Appendices A–C
pp. 1–19, references pp. 20–25), all read, Eqs. (1)–(20) and (24)–(55)
checked visually. Page 1 matches Crossref; no identity problem.

# Key claims

Registry notation (see the Notation map); $\tau_k=k/\varepsilon$, and the
subscript $+$ marks a modelled-to-total ratio, never wall units.

1. RANS and LES equations have the same structure and differ only in the length or time scale supplied, the RANS scales being much larger (§1, §2.3). **Stated**
2. The number of "hybrid RANS-LES" papers grows as $P_{n+1}-P_n=a^2(n+1)^2$ with $a=1.29$, $n=N-1995$, so $P_n=P_0+a^2n(n+1)(2n+1)/6$ with $P_0=48$, projecting 9.2K papers in 2020 and 25K in 2030 (Google Scholar; §1, Fig. 2). **Shown** (fit to bibliometric data)
3. Physical (PDF) realizability means a stress model is the variance of a realizable stochastic process; mathematical realizability (Schumann) requires a positive semi-definite modelled stress, and it extends to SGS stresses when the filter is positive (§2.1). **Stated**
4. Dynamic LES that does not honour realizability (the dynamic Smagorinsky model) is often computationally unstable; "fully realizable dynamic LES" is stable without averaging or clipping (§2.1, citing ref. [30]). **Stated**
5. The Fokker–Planck model (Eq. 2) yields the algebraic stress $\tau_{ij}=\tfrac23k\delta_{ij}-2\nu_t\bar S_{ij}$ (or $R_{ij}$ with $\langle S_{ij}\rangle$ in RANS), with $\nu_t=k\tau_L/3=C_\mu k\tau_k$ and $C_\mu=2(1-c_0)/3$ (§2.2). **Derived**
6. The standard $k$-$\varepsilon$ constants $C_{\varepsilon1}=1.44$, $C_{\varepsilon2}=1.92$, $\sigma_\varepsilon=1.3$ satisfy the log-law condition $\kappa^2=C_\mu^{1/2}\sigma_\varepsilon(C_{\varepsilon2}-C_{\varepsilon1})$ only with "a relatively high value" $\kappa=0.43$; the $k$-$\omega$ constants $(C_{\omega1},C_{\omega2},C_\mu,C_\omega,\sigma_\omega)=(0.49,0.072,0.09,1.1,1.8)$ give $\kappa=0.41$ (§2.3, Eqs. 8–11). **Derived**
7. The $k$, $\varepsilon$ and $\omega$ equations can be rewritten as BGK-type relaxations towards equilibrium values with sink terms (Eq. 12, after Asinari et al.). **Derived**
8. For small $\Delta_+$ the LES length scale is $L=C_+\Delta$ with $C_+=(3C_K/2)^{3/2}/\pi$; the paper states that $C_K=(1.3,1.43,1.5)$ gives $C_+=(0.876,1.0,1.074)$, "hence $L=\Delta$ is very reasonable" (§2.3, App. C). **Derived** (see Printed slips)
9. $R_{ij}=R^{\mathrm{res}}_{ij}+\langle\tau_{ij}\rangle$, hence $k_{\mathrm{tot}}=k_{\mathrm{res}}+k$ and $\varepsilon_{\mathrm{tot}}=\varepsilon_{\mathrm{res}}+\varepsilon$; the term neglected in $\varepsilon_{\mathrm{tot}}$ is at most about 2% (§2.4, Eqs. 14–18). **Derived**/**Stated**
10. WMLES depends on design parameters: the exchange location, the mesh distribution and the prescribed total viscosity in the Park–Moin correction $\nu_t=\nu_{t,\mathrm{tot}}-\nu_{t,\mathrm{res}}$; adequate boundary-layer resolution makes it "orders of magnitude more expensive than original DES" (§3.1). **Stated**
11. Source-term methods have a correct mathematical formulation, but reconstructing LES variables is an ill-posed deconvolution and their cost exceeds that of LES (§3.2). **Stated**
12. DES switches only the dissipation term; the unified RANS-LES (UNI-LES) switches the time scale $\tau_u=\min(\Delta k^{-1/2},\tau_k)$ in all terms of the $k$ and momentum equations, "highly beneficial" for fluctuations in transition regions (§3.3, Eqs. 22–23). **Stated**
13. Reynolds-stress-constrained LES can produce an unphysical mean modelled stress $\langle\tau_{ij}\rangle=R_{ij}-R^{\mathrm{res}}_{ij}$ when the anisotropies of the Reynolds stress and of the resolved stress disagree (§3.3). **Stated**
14. In PANS, $\alpha_{\mathrm{PANS}}=1+(\alpha_\varepsilon-1)f_k/f_\varepsilon$ and $\beta_{\mathrm{PANS}}=1+(\alpha_\omega-1)f_k/f_\varepsilon$; the neglected transport difference $D_k-f_kD_{k,\mathrm{tot}}=\partial_j[(1-f_\varepsilon/f_k^2)\nu_t\partial_jk]$ is non-zero in general, so PANS is strictly valid only for homogeneous turbulence (§3.4, Eqs. 24–30). **Derived**
15. PITM is "basically equal" to PANS with $f_\varepsilon=1$, the maximum-transport Prandtl number and $k_+=L_+^{2/3}$, $L_+$ from Eq. (58) (§3.4). **Stated**/**Derived**
16. In the SAS $\nu_t$ equation (Eq. 31) the standard settings $(\zeta_1,\zeta_2,\zeta_3,\sigma_\Phi)=(0.8,1.47,0.0288,2/3)$ give $\kappa=0.41$ and imply $C_{\varepsilon1}=1.2$, $C_{\varepsilon2}=1.82$, $C_{\omega1}=0.2$, $C_{\omega2}/C_\mu=0.82$ (Eqs. 33–37). **Derived**
17. Under $Q=0$ and spatially constant $\delta k/k$, $\delta\varepsilon/\varepsilon$, the variational analysis of the $k$-$\varepsilon$ model gives $\alpha^*_\varepsilon=1+L_+^2(\alpha_\varepsilon-1)$, identifying $L_+^2$ as the resolution measure (§4.2, Eqs. 38–44). **Derived**
18. The same measure follows for $k$-$\omega$ ($\alpha^*_\omega=1+L_+^2(\alpha_\omega-1)$, Eq. 49) and for the $k$-equation (DES-type) hybridizations ($\alpha^*_\varepsilon=1+\alpha_\varepsilon-\psi_\alpha$, $\alpha^*_\omega=1+\alpha_\omega-\psi_\beta$, Eqs. 46, 51), giving the four variants CES-KES, CES-KEK, CES-KOS and CES-KOK (§4.3). **Derived**
19. Several RANS models "can generate resolved motions if $L_+\le1$" (answer to the paper's question Q2; §4.3), while §4.1 says an "exact mathematical proof … is currently missing". **Derived** (by analogy of coefficient structures)
20. Inserting the PANS assumption into the variational equation (Eq. 52) requires $N_\varepsilon=0$ and $D_k=0$, confining PANS to homogeneous turbulence without $\varepsilon$ variations (§4.4). **Derived**
21. With $f_\varepsilon=1$, PANS uses $\alpha^*_\varepsilon=1+L_+^{2/3}(\alpha_\varepsilon-1)$ against CES's $1+L_+^2(\alpha_\varepsilon-1)$; since $L_+^{2/3}\ge L_+^2$, PANS and PITM "require a much finer grid" for the same resolution (§4.4). **Derived**/**Stated**
22. CES–DES equivalence gives $L_+=\min\{[\sqrt{1+4\alpha_\varepsilon(\alpha_\varepsilon-1)C_{DES}^2\Delta_+^2}-1]/[2(\alpha_\varepsilon-1)C_{DES}\Delta_+],1\}$, with $L_+\to\alpha_\varepsilon C_{DES}\Delta_+$ for small $\Delta_+$; with $C_+=1$ this gives $C_{DES}=0.75$ ($k$-$\varepsilon$, $\alpha_\varepsilon=1.33$) and 0.61 ($k$-$\omega$, $\alpha_\omega=1.63$), "not far from the standard value" 0.65 (§4.4, Eqs. 53–55, Fig. 5). **Derived**
23. "The technical solution to adjust $\Delta_+$ to $L_+$ is absurd"; the framework of DES is too narrow and DES is unstable under grid variation (§4.4, item 3). **Stated**
24. Periodic hill: the experimental reattachment length follows $x_R/h=0.49(Re_h/10^4)^{-1.4}+3.71$ (Kähler et al.); PANS, PITM, WMLES, DES and RSC-LES show large variability through design parameters, while SAS, source-term methods and UNI-LES "apparently reduce the RANS error significantly", UNI-LES at $Re_h=37{,}000$ "agree[ing] very well" with experiment (§5.1, Fig. 6). **Shown** (compiled from the literature)
25. PANS on the same flow: Ma et al. recommend $f_k=0.4$, Razi et al. $f_k=0.15$, and the two give different $x_R$–$f_k$ trends (§5.1, Fig. 7). **Shown** (cited)
26. PITM $k_+$ on four periodic-hill grids ($Re_h=37{,}000$) does not follow the expected grid trend near the wall; two grids of about the same point count give different $k_+$ (Fig. 8, from Chaouat & Schiestel). **Shown** (cited)
27. NASA hump, compiled $x_R/c$ (Table 3): experiment 1.10, RANS 1.188–1.305 (8–18.6% error), LES 1.095, DES 1.114–1.152, WMLES 1.035–1.105, source-term methods 1.08–1.19; the double-peak $C_f$ structure is missed by WMLES and DES (§5.2, Figs. 10–11). **Shown** (compiled)
28. Bachalo–Johnson bump ($M_\infty=0.875$, $Re_c=2.763\times10^6$): experiment $x_R/c=1.10$; Spalart et al. obtain 1.18 with DNS (7.3% error, attributed to a small domain) and 1.08 with LES; WMLES cannot match both the shock and the reattachment $C_f$ maxima by choosing the exchange location (§5.3, Table 5, Fig. 14). **Shown** (compiled)
29. NACA 4412: no methodology predicts both lift and drag accurately; RSM+PITM hybrids reduce the RANS lift and drag errors from (+14%, −54%) to (+7%, −39%) (§5.4). **Stated** (cited)
30. Classical hybrids (WMLES, DES) feed no resolved-motion information back to the model; only PANS and PITM try, with the shortcomings listed; CES needs "exactly one equation framework" and is not affected by the filter-width dependence of LES (§6). **Stated**

# Printed slips

- §2.3 and App. C: "Values $C_k=(1.3,1.43,1.5)$, e.g., result in $C_+=(0.876,1.0,1.074)$". From the printed $C_+=(3C_K/2)^{3/2}/\pi$, $C_K=1.3$ gives $C_+=0.867$ (1.43 and 1.5 give 1.000 and 1.074) *(compiler check, not in the sources)*.
- Table 5, WMLES row: $x_R/c=1.157$ with printed error 5.3%; against the experimental 1.10 the printed numbers give 5.2% *(compiler check, not in the sources)*.
- Symbol drift: $c_0$ printed $c_o$ in Eq. (4) and in $C_\mu=2(1-c_o)/3$; the Kolmogorov constant printed both $C_K$ and $C_k$ in the same sentence (§2.3, App. C).
- §4.4 is titled "Hybrid model concept validation by theory", the title of §4.
- Reference list: [87] and [222] are the same work (Xia et al., J. Turbul. 14(1) 2013, 1–21); [215] prints the page range "115105/1–025112/11"; [33] prints "535–61"; [218] prints its title in garbled word order ("Young-person's Guide Simulation Grids to Detached-Eddy"); volume–year pairs inconsistent within the list: [130], [131] Flow Turbul. Combust. 78 with 2010 against [121] 78 with 2007; [116] AIAA J. 42 with 2011; [67] Phys. Fluids 6 with 1989 against [138] 6 with 1994; [16] Int. J. Heat Fluid Flow 24(2) with 2005 against [57] 24(4) with 2003; [297] "39th Aerospace Sciences Meeting … AIAA Paper 09-3812, San Antonio, TX, 2009" against [173], [302] (39th ASM, 2001, Reno); [177] AIAA Paper 09-0919 for the 48th ASM in 2010.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde U_i$ | $\langle u_i\rangle$ (RANS) or $\bar u_i$ (LES) | **collision:** the source's tilde is the RANS mean or the LES filter, never a Favre filter |
| $D_{ij}=\widetilde{u_iu_j}$ | $R_{ij}$ (RANS) or $\tau_{ij}$ (LES) | positive trace, full stress; $k=D_{nn}/2$ |
| $d_{ij}$ | $b_{ij}$ | |
| $R_{ij}$, $R^{res}_{ij}$, $\langle D_{ij}\rangle$ | $R_{ij}$, $R^{\mathrm{res}}_{ij}$, $\langle\tau_{ij}\rangle$ | $\langle\cdot\rangle$ ensemble average of LES fields |
| $k$, $k_{res}$, $k_{tot}$; $\varepsilon$, $\varepsilon_{res}$, $\varepsilon_{tot}$ | $k$, $k_{\mathrm{res}}$, $k_{\mathrm{tot}}$; $\varepsilon$, $\varepsilon_{\mathrm{res}}$, $\varepsilon_{\mathrm{tot}}$ | modelled, resolved, total |
| $\tilde S_{ij}$, $S=(2\tilde S_{mn}\tilde S_{nm})^{1/2}$ | $\bar S_{ij}$, $\lvert\bar S\rvert$ | factor two included in the source |
| $P=\nu_tS^2$ | $P_k$ | |
| $\tau=k/\varepsilon$ | $\tau_k$ (page-local) | **collision** with $\tau_{ij}$, $\tau_w$ |
| $\omega=\tau^{-1}$ | $\varepsilon/k=C_\mu\omega$ | **collision:** the source's $\omega$ lacks the $\beta^*$ ($C_\mu$) of the registry $\omega$ |
| $L=k^{3/2}/\varepsilon$, $L_{tot}$, $\tau_{tot}$ | same (page-local) | not the integral scale of §8 |
| $k_+$, $\varepsilon_+$, $L_+$ | $k_+$, $\varepsilon_+$, $L_+$ (registry §11); $f_k$, $f_\varepsilon$ in PANS | **collision:** "+" is not wall units |
| $\Delta_+=\Delta/L_{tot}$, $\Delta_{C+}$, $C_+$, $C_K$ | same (page-local) | no cell-based definition of $\Delta$ printed |
| $\alpha=C_{\varepsilon2}/C_{\varepsilon1}$, $\alpha^*$ | $\alpha_\varepsilon$, $\alpha^*_\varepsilon$ (as on [continuous eddy simulation](/methods/continuous-eddy-simulation.md)) | **collision** with the DG blending factor $\alpha$ and the Wilcox constant $\alpha^*$ |
| $\beta=C_{\omega2}/(C_\mu C_{\omega1})$, $\beta^*$ | $\alpha_\omega$, $\alpha^*_\omega$ (registry §11) | **collision** with the registry $\beta^*$ and $\beta_\omega$; $\alpha_\omega\approx1.63$ |
| $C_{\omega1}$, $C_{\omega2}$, $C_\omega$, $\sigma_\omega$ | same (Bredberg et al. constants, page-local) | $C_{\omega1}$ plays the role of Wilcox's $\alpha$ |
| $\alpha_{PANS}$, $\beta_{PANS}$ | $\alpha_{\mathrm{PANS}}$, $\beta_{\mathrm{PANS}}$ (page-local) | |
| $D_k$, $D_\varepsilon$, $D_\omega$, $D_{k,tot}$ | same (turbulent transport, page-local) | |
| $\psi_{DES}$, $\psi_\alpha$, $\psi_\beta$, $C_{DES}$ | same (page-local; $\psi_\beta$ also registry §11) | $C_{DES}=0.65$ |
| $N_k$, $N_{k\varepsilon}$, $N_\varepsilon$, $N_\omega$, $Q$ | same (page-local) | not the polynomial degree $N$ |
| $\tau_u$, $\tau_L$, $c_0$ | same (page-local) | UNI-LES time scale; Lagrangian relaxation time; PDF diffusion parameter |
| $\zeta_1$, $\zeta_2$, $\zeta_3$, $\sigma_\Phi$, $R_{SAS}$, $S'$ | same (page-local) | |
| $L_{vK}$ | $L_{vK}$ | registry §11 |
| $\nu_{t,tot}$, $\nu_{t,res}$ | same (page-local) | RANS and resolved viscosities |
| $\mu$, $\eta$ (Speziale's model) | $\eta$ (Kolmogorov length), $\eta_S$ (page-local constant, 0.001) | **collision:** the source's $\mu$ is not the dynamic viscosity, its $\eta$ not the Kolmogorov length |
| $x_2$ | $y$ | wall-normal |
| $\tilde\tau_{w,i2}$, $h$ | $\tau_w$, $h_{\mathrm{wm}}$ | **collision:** $h$ is the hill height on the periodic hill |
| $\tau_{BGK}$, $k_{BGK}$, $e$ | $\tau_{\mathrm{LB}}$, same | lattice Boltzmann (App. A) |
| $x_r$ | $x_R$ | |
| $Re=U_bh/\nu$ | $Re_h$ | periodic hill |

# Reference list

325 printed references, numbered style ([1]–[325]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Refs. [87] and [222] are one work printed twice (folded into one entry).
Ref. [310] (Heinz, Mokhtarpoor & Stöllinger, *Hybrid RANS-LES methods with
continuous mode variation*, DLES XII, Springer 2020) is a different work from this review and is keyed `heinz-2020-c`. The same author is
printed both "Stoellinger" and "Stöllinger". Two author-less web items
([12] ERCOFTAC UFR 3-30, [256] NASA TMR bump data) and one corporate
author ([36]) are keyed by hand; refs. [18] and [221] were reconstructed
from the column layout. All items parsed.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md)
- [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md)
- [Periodic hill](/benchmarks/periodic-hill.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Energy backscatter and the subgrid energy flux](/definitions/energy-backscatter.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Continuous eddy simulation](/methods/continuous-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Dynamic procedure and the Germano identity](/methods/dynamic-procedure.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)
- [Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
