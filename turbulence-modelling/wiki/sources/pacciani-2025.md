---
type: Source
title: "Pacciani et al. (2025) — A Reformulation of the Laminar Kinetic Energy Model to Enable Multi-mode Transition Predictions"
description: "Reformulates the authors' laminar-kinetic-energy transition model with a local production length scale, an intermittency coupling to k-ω SST, a pressure-gradient-dependent onset threshold and separation-aware terms, calibrated on the ERCOFTAC T3 plates and validated on LS89, T106C, T108 and S809 as a base for machine-learnt corrections."
resource: "doi:10.1007/s10494-024-00590-y"
source_kind: paper
authors: [Pacciani R., Fang Y., Metti L., Marconcini M., Sandberg R.]
year: 2025
venue: "Flow Turbul. Combust. 114:81–116"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Flow_Turbulence_and_Combustion_Pacciani_A_Reformulation_of_the_Laminar_Kinetic_Energy_Model_to_Enabl.pdf"
tags: [transition, rans, laminar-kinetic-energy, turbomachinery, data-driven]
timestamp: 2026-10-27T06:13:00Z
---

# Summary

Pacciani et al. (2025) rebuild their
[laminar kinetic energy transition model](/methods/laminar-kinetic-energy-transition-model.md)
(Pacciani et al. 2011–2012), designed for separated-flow transition in
low-pressure turbines, into a multi-mode (bypass and separated-flow) RANS
closure. It is meant as a simple base framework whose few closure functions
are the targets of later gene-expression-programming corrections
([symbolic regression](/methods/symbolic-regression-closure.md)). The motive
is a finding of Fang et al. (2024): training the old model's production and
transfer terms gave opposite correction trends for separated-flow and bypass
transition.

The changes are five. The production of the laminar kinetic energy $k_L$
uses a local length scale $|\Omega|d^2/U$ and the large-scale (shear-sheltered)
part of $k$ as velocity scale. The old coupling through the Wilcox
low-Reynolds damping is replaced by an algebraic intermittency multiplying
the production of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md),
as in [local-correlation-based models](/methods/local-correlation-based-transition-model.md).
A laminar-fluctuation viscosity enters the diffusive fluxes. The onset
threshold becomes a function of a local pressure-gradient parameter. Separation-aware
production and transfer terms, switched on by a vorticity-Reynolds-number
criterion, target overlong [laminar separation bubbles](/definitions/laminar-separation-bubble.md).
The model is local but not Galilean invariant. The authors note that linear
[eddy-viscosity](/definitions/boussinesq-hypothesis.md) models need boosted
production to avoid overpredicted reattachment lengths.

Calibration on the [ERCOFTAC T3 plates](/benchmarks/ercoftac-t3-flat-plate.md)
fixes six constants. Steady 2-D RANS validation covers bypass transition with
heat transfer on the VKI LS89 vane, separated-flow transition on the T106C and
T108 [turbine cascades](/benchmarks/turbine-cascade.md) at exit
$Re=0.8$–$1.6\times10^5$, and the S809 airfoil at $0^\circ$–$12^\circ$. Onset
is predicted with "engineering accuracy", comparable to
$\gamma$-$Re_{\theta}$, but transition lengths are consistently too short.
Higher-fidelity results enter as references:
[DNS and LES](/definitions/direct-numerical-simulation.md) of the cascades,
and the validation is called a posteriori
([testing](/definitions/a-priori-and-a-posteriori-testing.md)).

# Version read

Version of record (Springer, open access CC BY 4.0; received 19 April 2024,
accepted 25 September 2024, online 8 October 2024), 36 pages (journal
pp. 81–116), all read; the equations on pp. 85, 87–91, 100–101 and 112–113
were checked visually because text extraction garbled them. Page 1 matches the
metadata. The archive filename carries the online year 2024; the issue year is
2025.

# Key claims

1. The baseline model has four weaknesses: it is non-local (shear-layer vorticity thickness), has no bypass-transition term, uses a constant onset threshold $c_5$ that should depend on pressure gradient and free-stream turbulence, and couples poorly to the turbulence model through damping functions (§3.2). **Stated**
2. Fang et al. (2024), training the baseline's production and transfer terms with a multi-objective multi-case machine-learning algorithm, found opposite correction trends for separated-flow and bypass transition, which motivates the reformulation (§1, §3.2). **Stated**
3. With the baseline coupling (damping $\alpha^*(R_T)$), bypass transition on T3A gives an "erratic" skin friction, a non-physical series of relaminarizations and retransitions, because $\alpha^*(R_T)$ keeps the transfer term from igniting the turbulence model; rational and exponential forms of $\alpha^*$ did not fix it (§4.2, Fig. 1). **Shown**
4. The length scale $|\Omega|d^2/U$ (Eq. 10) has a wall-normal maximum roughly proportional to the momentum thickness, at about half the boundary-layer thickness in attached layers and on the outer shear layer of laminar separation bubbles; verified on Falkner–Skan profiles (§4.1). **Stated** (verification described, not shown)
5. The non-Galilean-invariant length scale behaves the same in the boundary layer when the velocity is taken in the frame of each solid wall (§4.1). **Stated**
6. The intermittency $\gamma=k_{T,s}/(k_L+k_{T,s})$ instead of $k/(k_L+k)$ avoids $\gamma\to1$ in accelerating laminar layers where $k_L$ is smaller than the free-stream $k$ diffused into the layer (§4.2, Eq. 14). **Derived** (argued)
7. The intermittency coupling (Eqs. 15–18) can be used with any two-equation model; with Wilcox $k$-$\omega$ on T3A it gives the same onset as with SST but a quicker transition and a different turbulent $C_f$ level, so the constants "should be retouched" per host model (§4.2; §5.1.1, Fig. 5). **Stated** / **Shown**
8. $c_1$ and $c_5$ compete: at fixed onset $c_5$ must decrease when $c_1$ increases, because a larger $c_1$ raises $k_L$ and smooths the rise of $\gamma$; $c_1=0.03$, $c_5=22$ gives the slowest approach to the turbulent $C_f$ (§5.1.1, Figs. 2–3a). **Shown**
9. $c_1=0.02$ with $c_5=24$ best matches the measured T3A profiles of the total fluctuation energy $k_L+k$ up to $Re_x\simeq2.0\times10^5$; at $Re_x=2.38\times10^5$ and $2.74\times10^5$ the computed peak sits farther from the wall, attributed to the turbulence model (§5.1.1, Fig. 2). **Shown**
10. $c_3=0.02$: lower values do not start transition reliably; higher values only raise the peak turbulent production and can make transition too rapid (§5.1.1). **Shown** (described)
11. $c_{\mu,L}$ has a minor effect at zero and adverse pressure gradient but changes the transitional $C_f$ ramp in favourable gradient, not the onset; a larger value widens the transition region; 0.03 fits best and then agrees "very well" with $\gamma$-$Re_\theta$ (§5.1.2, Fig. 10). **Shown**
12. Grid study on T3A-: $165\times65$, $289\times129$, $541\times221$; medium and fine coincide (§5.1.1, Table 3, Fig. 8). **Shown**
13. On the low-$Tu$ T3A- and Schubauer–Klebanoff plates (the model has no natural-transition term) the transition path is "definitely too steep" with both this model and $\gamma$-$Re_\theta$, in line with Menter et al. (2015) (§5.1.1, Figs. 7–8). **Shown**
14. With constant $c_5=24$ the adverse-gradient plates T3C2, T3C3, T3C4 show a significantly delayed onset; $c_5(f_{PG})$ (Eq. 28) and $c_5(\lambda'_{\theta l})$ (Eq. 29) give almost coincident, corrected results on T3C2; the predicted transition region remains too short (§5.1.3, Figs. 11–13). **Shown**
15. On T3C4 a small separation is computed but $P_{\mathrm{sep}}$ does not activate, because $c_5(f_{PG})$ triggers transition before $f_{\mathrm{sep}}$ switches on (§5.1.3). **Shown**
16. On T3B and T3C1 the onset is correct but the laminar $C_f$ is off (overestimated on T3C1), attributed to the absent leading-edge modelling (§5.1.1–5.1.2, Figs. 6, 9). **Shown**
17. LS89 (bypass): with the inlet length scale tuned per case to match the leading-edge heat transfer, the suction-side onset is "reasonably well predicted" at exit $Re\simeq6\times10^5$ and "in very good agreement" with the measurements at $2\times10^6$; at Mur239 ($Tu=6\%$) transition also occurs on the pressure side at $s/s_{\mathrm{tot}}\approx0.4$, as measured (§6.1, Fig. 15). **Shown**
18. On LS89 the shock impinges on the suction side at $x/C_x=0.83$ and fixes transition there only at low $Tu$ (Mur247); at Mur239 transition occurs upstream of the shock (§6.1, Fig. 16). **Shown**
19. On LS89 transition develops too quickly compared with the measurements, as in most RANS results in the literature; the quasi-DNS of Segui et al. (2017) gives a smoother transition (§6.1). **Shown** / **Stated**
20. With Wilcox $k$-$\omega$ the LS89 leading-edge heat transfer stayed below the measurement even with an exaggerated length scale, suspected to be due to the realizability constraint (Durbin 1996), "mandatory" for physically consistent Wilcox results; this motivates the choice of SST (§4.2, §6.1). **Stated**
21. T106C at exit $Re=0.8\times10^5$: an open separation as measured, but transition too early and a smaller separated region, hence a narrower wake and underestimated integral loss; deemed satisfactory for 2-D RANS given the 3-D secondary-flow effects shown by the LES of Rosenzweig et al. (2023) (§6.2, Figs. 18a, 19a, 20). **Shown**
22. T106C at $1.2$ and $1.6\times10^5$: closed bubbles and better agreement, the isentropic Mach number in the bubble slightly underestimated; the suction-side distribution is "practically coincident" with the original model's, with a slightly better wake loss at $1.2\times10^5$ (§6.2, Figs. 18b–c, 19b–c). **Shown**
23. On T106C at $1.2\times10^5$, $f_{\mathrm{sep}}$ becomes non-zero at about 80% axial chord, at the separation point, drives a kink and growth of $k_L$ in the separated shear layer and boosts the transfer at transition (§6.2, Fig. 20). **Shown**
24. T108 (front-loaded): short bubbles at all Reynolds numbers, well matched in isentropic Mach number, wake loss and lapse rate; the computed separated region covers the measured zero quasi-wall-shear-stress region, but the post-reattachment $\tau_w$ is lower than measured, attributed to the turbulence model (§6.2, Figs. 21–23). **Shown**
25. The model is "quite insensitive" to $c_{\mathrm{sep}}$ in 10–100; above 100 the pressure recovery after reattachment is too steep; below 10 unsteady transition paths can appear in the separated shear layer (§6.2). **Shown** (described)
26. S809 at $Re_c=2\times10^6$, $Tu=0.2\%$, 20 angles in $0^\circ$–$12^\circ$: up to about $5.5^\circ$ transition is separation-induced on both sides; on the suction side onset moves rapidly upstream above $5^\circ$ and sits near the leading edge above $9^\circ$; the trends are reproduced but transition is predicted slightly upstream of the measurements at all angles (§6.3, Figs. 24–25). **Shown**
27. All results are space-converged according to grid studies not reported (§1). **Stated**
28. Separated-flow predictions reach essentially the accuracy of the baseline model designed for that purpose (§7). **Shown**

The reformulated model (Eqs. 13–19, 23–28; Appendix A), with $d$ the wall distance, $U$ the local velocity magnitude, $R_y=d\sqrt k/\nu$ and $R_T=k/(\nu\omega)$:
$$\begin{aligned}
\frac{Dk_L}{Dt}&=(1-\gamma)P_L-\mathcal R-2\nu\frac{k_L}{d^2}+\partial_j(\nu\,\partial_jk_L),\qquad
\frac{Dk}{Dt}=\gamma P_k+\mathcal R-\max(\gamma,0.1)\beta^*k\omega+\partial_j\!\left[\left(\nu+\frac{\nu_t}{\sigma_k}\right)\partial_jk\right],\\
P_L&=c_1\frac{|\Omega|d^2}{U}|S|^2\sqrt{k_{T,l}}+f_{\mathrm{sep}}\max(c_{\mathrm{sep}}\mu-\mu_t,0)|S|^2,\qquad
\mathcal R=c_3\,(f_t+3c_{\mathrm{sep}}f_{\mathrm{sep}})\,k_L\,\omega,\\
f_t&=1-e^{-\psi/c_4},\quad \psi=\max(R_y-c_5,0),\quad k_{T,s}=e^{-(c_{SS}\nu|\Omega|/k)^2}k,\quad k_{T,l}=k-k_{T,s},\quad \gamma=\frac{k_{T,s}}{k_L+k_{T,s}},\\
f_{\mathrm{sep}}&=1-\exp\!\left[-\max\!\left(\frac{Re_v}{R_{cr}}-1,0\right)\right],\quad Re_v=\frac{|S|d^2}{\nu},\quad R_{cr}=800\max[\min(2r,8),1],\quad r=\frac{|S|d}{U},\\
c_5&=24-2\max(f_{PG},0),\qquad f_{PG}=\frac{d}{\nu|S|}\frac{\partial p}{\partial s},
\end{aligned}$$
with $c_1=0.02$, $c_3=0.02$, $c_4=8$, $c_5=24$ (zero or favourable gradient), $c_{\mu,L}=0.03$, $c_{\mathrm{sep}}=10$, $c_{SS}=2$ (Table 2), $k_L=0$ at the inlet and the walls, the $\omega$ equation and the eddy viscosity those of SST, and the laminar-fluctuation viscosity $\mu_L=c_{\mu,L}f_{\mu,L}\rho(|\Omega|d^2/U)\sqrt{k_L}$ added to $\mu_t$ in the diffusive fluxes. **Stated** (the normalization of $|S|$ is not printed; see the Notation map)

# Printed slips

- **Eq. 19 and Eq. A13:** $f_{\mu,L}=1-e^{R_T^{2.5}}$, with a positive exponent in both places. For $R_T>0$ this is negative and unbounded, whereas the text says $f_{\mu,L}$ "prevents $\mu_L$ from affecting the viscous sublayer" *(compiler check, not in the sources)*.
- **Eq. A2 against Eqs. 16 and A11:** A2 writes $P_k$ and $D_k$ where Eq. 16 writes the intermittency-modified $\tilde P_k$, $\tilde D_k$, which A11 then defines.
- **§6.1, Fig. 14:** "as evident from Fig. 14(a), which reports static pressure isolines superimposed to color Mach number contours for the Mur224 configuration"; the caption makes (a) the grid and (b) the pressure and Mach plot "for the Mur239 test case".
- **§6.1, Fig. 15:** "(Mur239 and Mur247, Fig. 15a"; the caption assigns them to Fig. 15(b).
- **§6.2, Fig. 20:** "suction surface distributions ... are shown in Fig. 20b" and "boosting the transfer term R ... appreciated in Fig. 20b", while the caption puts them in (a).
- **§5.1.2 and Fig. 10:** the text does not name the case of the $c_{\mu,L}$ sensitivity; the caption says "for the T3C5 test case".
- **§4.2:** $Re_x=\frac{\rho U_\infty x}{\nu}$, with both $\rho$ and the kinematic $\nu$ *(compiler check, not in the sources)*. Eqs. 20 and 22 are dimensionless only with a kinematic pressure, which the paper does not state *(compiler check, not in the sources)*.
- **§5.1:** "The viscosity ratio (or turbulent Reynolds number) $\nu_T/\nu$", while §3.1 and §4.3 define the turbulent Reynolds number as $R_T=k/(\nu\omega)$.
- **Names:** "Mayle and Schultz" (§3.1) against "Schulz" elsewhere; $c_{SS}$ (Eq. 11) against $c_{ss}$ (Appendix A); "Kubacky" (§4.1).
- Typos: "flat plat cases" (abstract), "flate plate", "onbtained", "Neverthelesss", "schockwave", "thec5"; "marchine-learnt" in a reference title.
- **Reference list:** Chorin (1967), J. Comput. Phys. 2:12–26, printed with DOI 10.1006/JCPH.1997.5716; Lardeau et al. (2007) printed "ASME J. Turbomach. 1(129), 1–7".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y$ | $d$ (wall distance) | the model terms use the distance to the nearest wall |
| $k_\ell$ | $k_L$ (laminar kinetic energy, page-local) | |
| $k_{T,s}$, $k_{T,l}$ | $k_{T,s}$, $k_{T,l}$ (small- and large-scale parts of $k$, page-local, as on the LKE page) | shear-sheltering split; not $k_{\mathrm{sgs}}$, $k_{\mathrm{res}}$ |
| $k_{tot}=k_\ell+k$ | $k_L+k$ | **collision:** the registry's $k_{\mathrm{tot}}$ is resolved plus subgrid |
| $f_{SS}$, $c_{SS}$ | (shear-sheltering function and constant) | |
| $\nu_T$, $\mu_T$ | $\nu_t$, $\mu_t$ | SST limiter with $a_1$, $F_2$ (Eq. A14) |
| $\mu_\ell$, $f_{\mu,\ell}$, $c_{\mu,\ell}$ | $\mu_L$, $f_{\mu,L}$, $c_{\mu,L}$ (laminar-fluctuation viscosity, its damping and constant) | |
| $R_T=k/(\nu\omega)$ | $R_T$ (turbulent Reynolds number, page-local) | §5.1 also calls $\nu_t/\nu$ the turbulent Reynolds number |
| $\sqrt k\,y/\nu$ | $R_y$ | registry §11 |
| $R$ | $\mathcal R$ (transfer from $k_L$ to $k$, page-local, as on the LKE page) | **collision** with the Reynolds stress $R_{ij}$ |
| $P_\ell$, $D_\ell$, $P_k$, $D_k$ | $P_L$, $D_L$ (production and dissipation of $k_L$), $P_k$, $\beta^*k\omega$ | $P_k=\nu_tS^2$ |
| $\gamma$ | $\gamma$ (intermittency) | algebraic, $k_{T,s}/(k_L+k_{T,s})$, not the transported $\gamma$ of $\gamma$-$Re_\theta$ |
| $S$, $\Omega$ | $\lvert S\rvert$, $\lvert\Omega\rvert$ (vorticity magnitude) | the factor two in $S$ is not printed |
| $U$ | (local velocity magnitude) | source of the non-Galilean invariance |
| $\ell=\Omega y^2/U$ | $\lvert\Omega\rvert d^2/U$ (production length scale, written out as on the LKE page) | |
| $Re_v=Sy^2/\nu$, $R_{cr}$, $r$ | (vorticity Reynolds number, its critical value, shape function) | built with $\lvert S\rvert$ |
| $f_{sep}$, $P_{sep}$, $c_{sep}$ | (separation switch, separation production, constant) | |
| $f_{PG}$, $\lambda_\theta$, $\lambda_{\theta L}$, $\lambda'_{\theta L}$ | $f_{PG}$, $\lambda_\theta$, $\lambda_{\theta l}$, $\lambda'_{\theta l}$ (pressure-gradient parameters, as on the transition pages) | $s$ the streamwise coordinate |
| $\alpha^*$, $\alpha$, $\beta$, $\beta^*$ | (Wilcox $k$-$\omega$ constants and damping), $\beta^*$ | baseline model only |
| $c_f$ | $C_f$ | |
| $C_p=(p_{0,\infty}-p)/(\tfrac12\rho U_\infty^2)$ | $C_p$ | **convention:** based on the free-stream total pressure (§6.3) |
| $Re_{2,is}$, $M_{2,is}$ | $Re$, $M$ (exit isentropic, axial chord) | |
| $\ell_T$ | $L$ (inlet turbulent length scale) | |
| $Y$, $H$ | (total-pressure loss coefficient, heat-transfer coefficient) | |
| $\alpha$ (S809) | (angle of attack) | **collision** with the DG/FV blending factor |

# Reference list

44 printed references, author–year style, alphabetical. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
The two Pacciani et al. 2011 papers take suffixes in printed order (the text
does not say which is "2011a"). Chorin (1967) carries a printed DOI with a
1997 tag and Lardeau et al. (2007) a swapped volume and issue, recorded as
printed; Akolekar et al. (2019), Pacciani et al. (2014), Kubacki et al. (2020)
and Li et al. (2021) print no volume or pages; Wilcox (2006) is printed with a
garbled title. No printed duplicates.

# Pages created or updated

Chunk 5 (2026-10-26). This source is cited on:

- [ERCOFTAC T3 flat-plate transition cases](/benchmarks/ercoftac-t3-flat-plate.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [A priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Symbolic-regression turbulence closures](/methods/symbolic-regression-closure.md)
