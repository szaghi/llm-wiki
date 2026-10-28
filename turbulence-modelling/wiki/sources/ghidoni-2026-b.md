---
type: Source
title: "Ghidoni & Noventa (2026) — A transition model based on laminar kinetic energy and empirical correlations for high-order simulation of incompressible and compressible flows"
description: "Reformulates the Walters–Cokljat laminar-kinetic-energy transition model so both transfer-term thresholds compare a local momentum-thickness Reynolds number with Langtry–Menter onset correlations, adding pressure-gradient and compressibility corrections; validated in a high-order DG RANS solver on incompressible, supersonic and airfoil transition cases."
resource: "doi:10.1063/5.0324855"
source_kind: paper
authors: [Ghidoni A., Noventa G.]
year: 2026
venue: "Phys. Fluids 38:054114"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Physics_of_Fluids_Ghidoni_A_transition_model_based_on_laminar_kinetic_energy_and_empir.pdf"
tags: [transition, rans, dg, high-order, compressible]
timestamp: 2026-10-28T07:09:00Z
---

# Summary

Ghidoni & Noventa (2026) modify the three-equation
[laminar-kinetic-energy transition model](/methods/laminar-kinetic-energy-transition-model.md)
$k_L$-$k$-$\omega$ of Walters & Leylek (2004) and Walters & Cokljat
(2008), carried with $\ln\omega$ as in the authors'
[$k$-$\omega$](/methods/k-omega-model.md) practice. In the original model
the two transfer terms from $k_L$ to $k$ (renamed here "main", $\mathcal R$,
and "triggering", $R_{\mathrm{TRG}}$, in place of the bypass and natural
labels) switch on when $k/(\nu|\Omega|)$ or $d^2|\Omega|/\nu$ exceeds a
model constant, and these constants need recalibration case by case.

Both thresholds are rewritten with a local momentum-thickness Reynolds
number, $Re_\theta\approx(d^2|\Omega|/\nu)/c_\theta$, compared with
critical values $Re_{\theta c}$ from the empirical onset correlation of
the [local-correlation-based models](/methods/local-correlation-based-transition-model.md)
(Langtry & Menter 2009): the natural branch ($Tu_l\le1.3$) feeds
$R_{\mathrm{TRG}}$, the bypass branch ($Tu_l>1.3$) feeds $\mathcal R$,
both evaluated with the local turbulence intensity. This admits the
Langtry–Menter pressure-gradient correction and a compressibility factor
$(1+M_e^2)$, together with the Mach- and temperature-ratio-dependent
zero-pressure-gradient part of $c_\theta$ (Liu et al. 2022). Edge
quantities come from isentropic relations. The model runs in the authors'
modal high-order DG RANS solver (BR2, exact Riemann solver, primitive
log-variables, [artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md);
a relative of the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md),
not DGSEM itself) at degree $N=4$.

Validation covers the [ERCOFTAC T3](/benchmarks/ercoftac-t3-flat-plate.md)
plates (T3A, T3B, T3A-, T3C2–T3C5, with a
[laminar separation bubble](/definitions/laminar-separation-bubble.md) in
T3C4), the Schubauer–Klebanoff and Schubauer–Skramstad natural-transition
plates, 42 Fransson–Shahinfar cases, the Blair heated plates, two
supersonic plates (the Mach 2.25 DNS of Pirozzoli et al. among the
[compressible boundary layers](/benchmarks/turbulent-boundary-layer.md)
and Chen et al. at Mach 3.5), and the S809, NFL(1)-0416 and NLR-7301
airfoils. Onset errors are mostly a few percent and $C_f$ errors 2–25%; the
corrections reduce them. The cost is a longer transition region and a
lower end-of-transition $C_f$ peak than the original model at high $Tu$
(T3B). A [law of the wall](/definitions/law-of-the-wall.md) with
$\kappa=0.41$, $B=5$ serves as reference in T3A.

# Version read

Version of record (AIP typeset, Phys. Fluids 38, 054114 (2026); submitted
27 January 2026, published online 18 May 2026); 30 PDF pages (an AIP cover
sheet and journal pp. 054114-1 to -29), all read, with the equation and
table pages checked visually. Page 1 agrees with Crossref. This paper is
distinct from [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) (explicit
wall function, same first author).

# Key claims

1. The thresholds of both transfer terms are rewritten with $Re_\theta\approx(d^2|\Omega|/\nu)/c_\theta$ against critical values from empirical correlations (Eqs. 21, 26), removing the case-by-case recalibration of $C_{R,\mathrm{crit}}$ and $C_{\mathrm{TRG,crit}}/f_{\mathrm{TRG,crit}}$ (§II, §VI). **Derived**
2. Correlations for critical values of $k/(\nu|\Omega|)$ or $d^2|\Omega|/\nu$, as Hu et al. (2025) attempted, are "difficult or impossible to write from experiments or high-fidelity simulations"; the $Re_\theta$ form admits the existing compressibility and pressure-gradient corrections for all modes, whereas Hu et al. correct the pressure gradient only in the natural-mode term (§I, §II). **Stated**
3. The model uses the local intensity $Tu_l=(\frac23k)^{1/2}/|\boldsymbol u|$, not $Tu_\infty$; it is called "local" although free-stream values enter the corrections, because no non-local integration is performed (§II, §III). **Stated**
4. Each correlation should be used with the intensity (local or free-stream) of its calibration, so no $Tu_\infty$-based correlation (Huang et al., Fan et al.) is adopted (§III). **Stated**
5. In incompressible adiabatic zero-pressure-gradient flow $c_\theta\sim2.197$; citing Huang et al., the maximum of $(d^2|\Omega|/\nu)/Re_\theta$ rises from 2.2 to 8.4 for $0.2<M_e<10$, is reduced by wall cooling, and reaches $\sim5.2$ at $\beta_h=-0.035$, $M_e=6$ (§II). **Stated**
6. The pressure-gradient term of Liu et al.'s $c_\theta$ is dropped, because Crivellini et al. (2026) found the first term dominant and dropping it avoids an iterative solve for $\theta$ (§III, Eq. 33). **Stated**
7. T3A, T3B, T3A-: $C_f$ errors 3.38, 15.81, 7.67%; onset errors 8.22% (T3A, $Re_{x,tr}=2.42\times10^5$ against $2.23\times10^5$) and 22.22% (T3B, $1.15\times10^5$ against $0.95\times10^5$) (§IV A, Fig. 4). **Shown**
8. For T3B the start of transition agrees but its end lies downstream ($1.59$ against $1.22\times10^5$), attributed to replacing $k/(\nu|\Omega|)$ by $Re_\theta$ in the main threshold, which "limits the transfer"; the original model gives a shorter transition and a higher peak $C_f$ (§IV A, Fig. 5). **Shown**
9. T3A- with the experimental $Tu_\infty=0.9\%$ lies outside all onset correlations (Coupland's onset differs from Abu-Ghannam & Shaw by 137.62%); with $Tu_\infty=0.48\%$, after Cakmakcioglu et al. and Crivellini et al., the difference is 1.39%, and 0.48% is used (§IV A, Fig. 6). **Shown**
10. $N$- and $h$-convergence on T3A: $C_f$ errors 3.89, 3.46, 3.39, 3.38% for $N=1$–4 on 4000 elements; 6.81 to 3.39% on 2000; 3.42 to 3.38% on 8000 (§IV A, Fig. 7). **Shown**
11. T3C2–T3C5: $C_f$ errors 7.56, 4.61, 12.67, 5.89%; onset errors 2.98% (T3C2) and 21.64% (T3C5); without the pressure-gradient correction 18.65% (onset) and 31.81% ($C_f$) for T3C2, 36.08% and 8.94% for T3C5 (§IV A, Fig. 8). **Shown**
12. T3C4: separation, onset and reattachment are captured but the peak shape factor, i.e. the bubble height, is underestimated; the separation-induced terms of Dellacasagrande et al. (omitted here) would reduce this (§IV A). **Shown**
13. Schubauer–Klebanoff: onset error 8.34% ($28.49$ against $31.54\times10^5$); Schubauer–Skramstad SS1–SS5: 6.01, 4.00, 4.01, 4.99, 3.00% (Table IV); the triggering terms act upstream of the main ones in natural transition and are zero in T3A (§IV A, Figs. 10–11). **Shown**
14. The intensity built from $k_L+k$ reproduces the measured $Tu$ profiles in the laminar and pre-transitional layer; the one built from $k$ alone underestimates them before the end of transition (§IV A, Fig. 13). **Shown**
15. A free-stream length-scale sweep at T3A conditions ($250<Re_{\lambda_\infty}<5000$) gives fits $Re_{x}=c_1Re_{\mathrm{FST}}^{c_2}+c_3$ for the start ($-5.86\times10^5$, $-0.71$, $2.21\times10^5$) and end ($-6.61\times10^5$, $-0.36$, $4.47\times10^5$) of transition; like the original model, the proposed one "seems to fail the prediction of the twofold effect" of Fransson & Shahinfar (§IV A). **Shown**
16. Fransson–Shahinfar C1–C42: onset error 18–23% with the $C_f$-based onset, 7–12% with $\gamma_A=k/(k_L+k)=0.5$, 5–9% with the proposed $\gamma_B=(k-k_{\min})/(k_{\max}-k_{\min})=0.5$ (Eq. 34, Fig. 14). **Shown**
17. Lowering $Tu_\infty$ from the T3A value to a tenth moves the onset monotonically, "without irregularities and slope reversals", including where the triggering terms switch on, unlike the models of Lorini et al. and Bulgarini et al. (§IV A, Fig. 15). **Shown**
18. Blair zero-pressure-gradient heated plates B1–B3: $C_f$ errors 14.51, 4.18, 1.94%; onset errors 1.66, 12.12, 1.01%; the compressibility corrections are negligible there (§IV B, Fig. 17). **Shown**
19. Blair favourable-gradient plates B7, B8, B13: $C_f$ errors 15.78, 14.89, 24.87%; onset errors 18.75, 15.78, 3.77%; the predicted transition is shorter than measured and its lengthening under favourable gradient is underestimated (§IV B, Figs. 19–20). **Shown**
20. Supersonic plate ($M_\infty=2.25$, DNS of Pirozzoli et al.): $C_f$ error 10.91%, onset error 6.96%; without the compressibility factor on the correlation 32.40% and 39.70%; without both corrections 46.78% and 64.42% (§IV C, Fig. 23). **Shown**
21. Chen et al. Mach 3.5 cases CMB1–3: onset errors 3.25, 4.23, 1.56% (Table IX); all models, this one included, underestimate the transitional $C_f$ overshoot (§IV C). **Shown**
22. On airfoils, coarse far-field elements produce negative $k_L$ or $k$, clipped to zero, and zero $k$ prevents triggering; high-order runs must start from converged lower-order ones on meshes that already avoid such zeros (§V). **Stated** (run experience)
23. S809, NFL(1)-0416, NLR-7301: onset errors mostly below 5–10%; the largest are 28.12% (NFL upper side, high incidence) and 81.16% (NLR-7301 near $M_\infty=0.724$–0.748, where the shock dominates transition) (§V, Figs. 25, 27, 29). **Shown**
24. All runs start $N=0$ from the free stream and each higher degree from the lower one; T3C4 needs pseudo-unsteady time-adaptive runs (Appendix). **Stated**

The modified thresholds, translated (Eqs. 19–30; $\mathcal R$ and
$R_{\mathrm{TRG}}$ are the transfer terms):
$$\phi_R=\max\Big[\frac{d^2|\Omega|}{\nu\,c_\theta}-Re_{\theta c},0\Big],\qquad \phi_{\mathrm{TRG}}=\max\Big[\frac{d^2|\Omega|}{\nu\,c_\theta}-Re_{\theta c,\mathrm{TRG}},0\Big],$$
$$Re_{\theta c}=Re^*_{\theta c}\big|_{Tu_l>1.3}\,\mathrm{PGC}(\lambda_{\theta l},Tu_l)\,(1+M_e^2),\qquad Re_{\theta c,\mathrm{TRG}}=Re^*_{\theta c}\big|_{Tu_l\le1.3}\,\mathrm{PGC}(\lambda_{\theta l},Tu_l)\,(1+M_e^2),$$
with $Re^*_{\theta c}$ the Langtry–Menter correlation (Eq. 27; bypass
branch $331.50(Tu_l-0.5658)^{-0.671}$), $\lambda_{\theta l}=(\theta^2/\nu)\,\partial|\boldsymbol u|/\partial s$
limited to $(-1,1)$, $\theta$ from Eq. (33), and $c_\theta=c_\theta^{\mathrm{ZPG}}(M_e,T_e/T_w)$.
The original model's constants are printed in Table I.

# Printed slips

- Eq. (27): "$1173.51\ 589.428Tu+\frac{0.2196}{Tu^2}$", the operator between the first two terms missing.
- Table I lists "$C_k=1000$", a constant used in no equation, and omits $C_{TS,\mathrm{crit}}$, which appears in Eq. (11).
- Table II gives T3A $Tu_\infty=3.3\%$; §IV A says "the free-stream turbulence intensity of the T3A case is $Tu_\infty=2.3\%$".
- Table VII (Blair B6–B15) prints $(\mu_t/\mu)_\infty=1.2$ for all cases and "$Tu_\infty$ (%)" $=2,8,34,67,100$, the sequence of the $(\mu_t/\mu)_\infty$ row of Table VI; the text says B6, B11, B12 do not transition "due to the low free-stream turbulence intensity" although B12 carries the same printed value as B7.
- p. 19, Blair favourable gradient "without" the correction: "err = 15.84% and 18.75% in the B7 case and err = 24.87% and 3.77% in the B13 case", presented as higher, repeat the with-correction values (the B13 pair is not higher).
- "the influence of the correction is lower in the B8 case (Table VIII)": Table VIII lists the supersonic cases.
- Table IX headers print "CMB1 CMB3 CMB3"; Table V labels print "CS", "CI I", "C2I" for C5, C11, C21.
- p. 11: degrees of freedom "$\{6,12,2,30\}$" for the 2000-element mesh; $2000(N+1)(N+2)/2$ gives 6, 12, 20, 30 thousand for $N=1$–4 *(compiler check, not in the sources)*.
- Schubauer–Klebanoff: p. 14 gives $Re_{x,\mathrm{start}}=2.67\times10^6$, $Re_{x,\mathrm{end}}=3.34\times10^6$; the next paragraph gives $24.33$ and $32.64\times10^5$ for the same onset $28.49\times10^5$, and only the second pair averages to it *(compiler check, not in the sources)*.
- Onset errors computed as $|Re_{x,tr}-Re^{\mathrm{ref}}_{x,tr}|/Re^{\mathrm{ref}}_{x,tr}$ reproduce Tables IV and IX, but give 2.6% for B1 (printed 1.66%) and 9.7% for Schubauer–Klebanoff (printed 8.34%), beyond the rounding of the printed $Re_{x,tr}$; the paper prints no formula for this error *(compiler check, not in the sources)*.
- "$100K<T_e/T_w<300K$" (p. 6), a ratio given in kelvin.
- §V, NLR-7301: six Mach numbers $\{0.5,0.6,0.724,0.748,0.774,0.8\}$ against seven incidences and error entries; Fig. 28 uses $M_\infty=0.7$; "NLR-73012"; element list "$\{21\,456; 23\,927; 20; 715\}$".
- Appendix: "According to Belpietro et al.,57", while ref. 57 is Noventa et al. (2020) and no Belpietro is listed.
- The transport equations print $R_{TGR}$; the text uses $R_{TRG}$.
- Eqs. (13)–(15) write $k_T\tilde\omega$, $\tilde\omega/k_T$ and $\tilde\omega^2$ where $\omega=e^{\tilde\omega}$ is used elsewhere; $\lambda_{TOT}$ in Eq. (17) is undefined; the Appendix conservative vector omits the $\rho\tilde\omega$ entry of the 8-entry primitive vector.
- Typos: "ReRST < 40" (p. 16), "the plat plate" (p. 18).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $k_T$ | $k$ | turbulent kinetic energy |
| $k_L$, $k_{TOT}=k_L+k_T$ | $k_L$, $k_L+k$ (page-local) | laminar kinetic energy |
| $k_s$, $k_l$ | (small- and large-scale parts of $k$, page-local) | |
| $\omega$, $\tilde\omega=\log\omega$ | $\omega$, $\tilde\omega_\ell=\ln\omega$ (registry §11) | **collision:** tilde is neither Favre nor SA |
| $\tilde p$, $\tilde T$ | $\ln p$, $\ln T$ | primitive log-variables |
| $\nu_T$, $\nu_{T,s}$, $\nu_{T,l}$ | $\nu_t$ and its small- and large-scale parts | |
| $\tau_{ij}=2\nu_T(\cdots)-\frac23\rho k_T\delta_{ij}$ | $-\bar\rho R_{ij}$ | **collision:** negative convention, not the SGS stress |
| $\hat\tau_{ij}$ | $\sigma_{ij}-\bar\rho R_{ij}$ | **collision:** hat is not a test filter |
| $S$, $\Omega$ | $\lvert S\rvert$, $\lvert\Omega\rvert$ | both with the factor two |
| $d$ | $d$ | wall distance |
| $\lambda_T$, $\lambda_{eff}$, $\lambda_\infty$ | (turbulent length scales, page-local) | **collision:** not the Taylor microscale |
| $f_\nu$, $f_{INT}$, $f_{SS}$, $f_W$, $f_\omega$, $\beta_{TS}$, $\beta_R$ | (damping and threshold functions, page-local) | **collision:** $\beta_R$, $\beta_{TS}$ are not the field-inversion multiplier |
| $R$, $R_{TRG}$ | $\mathcal R$, $R_{\mathrm{TRG}}$ (page-local, as on the laminar-kinetic-energy page) | **collision:** not $R_{ij}$ |
| $\phi_R$, $\phi_{TRG}$ | $\phi_R$, $\phi_{\mathrm{TRG}}$ (page-local) | threshold arguments |
| $Re_{k_T,\Omega}$, $Re_{d,\Omega}$, $Re_{d,S}$ | $k/(\nu\lvert\Omega\rvert)$, $d^2\lvert\Omega\rvert/\nu$, $d^2\lvert S\rvert/\nu$ | written out on the page |
| $Re_\theta$, $Re_{\theta,c}$, $Re^*_{\theta,c}$ | $Re_\theta$, $Re_{\theta c}$, $Re^*_{\theta c}$ | |
| $c_\theta$ | (scale factor, page-local) | $\sim2.197$ incompressible |
| $Tu$ (local), $Tu_\infty$ | $Tu_l$, $Tu$ | registry §4 and §11; percent |
| $\lambda_\theta$ | $\lambda_{\theta l}$ | registry §11 |
| $PGC$, $\beta_h$, $K$ | (pressure-gradient correction, Hartree parameter, acceleration parameter; page-local) | |
| $M_e$, $T_e$, $T_w$, $u_e$ | $M_e$ and edge/wall quantities | isentropic estimates |
| $\gamma_A$, $\gamma_B$ | (onset indicators, page-local) | **collision:** not a transported intermittency nor the ratio of specific heats |
| $\alpha_T$, $\alpha_\theta$ | (turbulent and thermal diffusivities, page-local) | **collision:** not the DG blending factor |
| $\ell$, $\mathbb P^\ell$ | $N$ | polynomial degree |
| $c_f$, $c_p$, $H$ | $C_f$, $C_p$, $\delta^*/\theta$ | |
| $\kappa$, $B$ | $\kappa$, $B$ | 0.41, 5 |

# Reference list

57 printed references, numbered AIP style, no DOIs printed. The list is
merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. No printed duplicates. Ref. 27 prints its authors as "Z. L.
Hexia Huang and H. Tan" and ref. 54 as "S. O. T. H. Han"; ref. 24 prints
"J. Fluids Eng. 139(2), 1–5 (2016)". Ref. 27 (Huang & Tan, Eng. Appl.
Comput. Fluid Mech.) and ref. 31 (Liu et al., AIAA J. 60:3909) are works distinct from the bundle sources keyed huang-2025 and liu-2022 and are keyed `huang-2025-b` and `liu-2022-h`; ref. 46 is the ingested [menter-2022](/sources/menter-2022.md).

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [ERCOFTAC T3 flat-plate transition cases](/benchmarks/ercoftac-t3-flat-plate.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
