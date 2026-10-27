---
type: Source
title: "Menter et al. (2022) — An Algebraic LCTM Model for Laminar–Turbulent Transition Prediction"
description: "An algebraic local-correlation-based transition model coupled to k-ω SST: the intermittency follows from the ratio of a vorticity Reynolds number to a local onset correlation, with a sublayer limiter, harmonic averaging of k against hysteresis, and a separation-bubble term; validated on flat plates, airfoils and a turbine cascade."
resource: "doi:10.1007/s10494-022-00336-8"
source_kind: paper
authors: [Menter F.R., Matyushenko A., Lechner R., Stabnikov A., Garbaruk A.]
year: 2022
venue: "Flow Turbul. Combust. 109:841-869"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Flow_Turbulence_and_Combustion_Menter_An_Algebraic_LCTM_Model_for_LaminarTurbulent_Transition_Pred.pdf"
tags: [rans, transition, intermittency]
timestamp: 2026-10-25T13:53:00Z
---

# Summary

Menter et al. (2022) present an algebraic, zero-transport-equation member of the
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md),
called γ-alg-SST in the tests. It is coupled to the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md)
(or to its generalized form GEKO). The two-equation γ-$Re_\theta$ model solves transport equations
for the intermittency $\gamma$ and for the onset correlation, and the one-equation γ model solves one
for $\gamma$. Here $\gamma=\tanh(Rat_{Re}^2)$ is computed directly from the ratio of a vorticity
Reynolds number $Re_{V22}=\tilde\Omega d^2/(2.2\nu)$ to a critical $Re_{\theta c}$. This critical
value comes from a local correlation in a turbulence-intensity indicator $Tu_l$ and a pressure-gradient
indicator $\lambda_{\theta l}$, built from the wall-normal derivative of the wall-normal velocity, so
the model is Galilean invariant. The intermittency multiplies only the production of $k$,
$P_k\to\gamma P_k$, and not the destruction term as in earlier models of the family.

Three devices complete the model. A lower limit of 60 on $Re_{V22}$ in the ratio lets $\gamma=1$
reach into the viscous sublayer downstream of transition, so that the fully turbulent SST solution is
recovered. A harmonic average of $k$ over face neighbours in $Tu_l$ removes a "hysteresis": a
transition location that depends on whether the run starts laminar or fully turbulent. The authors
also report this hysteresis for the one-equation γ model in a cell-centred code and for other
algebraic models. A bubble term raises $\gamma$ above one, by up to 3, inside laminar separation
bubbles, to speed up the response of the turbulence model. The correlation coefficients are blended
between bypass ("High") and natural ("Low") values and are left open to user tuning.

Validation covers the ERCOFTAC T3 flat plates, the Schubauer–Klebanoff plate, the Volino–Hultgren
separated plate, four airfoils (Eppler 387, S809, NLF(1)-0414F, NLF(1)-0416F) and the Pak-B
low-pressure-turbine cascade. The algebraic model matches the transport models in quality. It
predicts earlier natural transition and smaller bubbles on airfoils, and it is less forgiving of
coarse streamwise grids. The survey of transition-model families mentions
[Spalart–Allmaras](/methods/spalart-allmaras-model.md)-based variants.

# Version read

Version of record (Springer typeset), 29 pages (pp. 841–869). Title, authors in this order, venue and
DOI on page 1 match the published metadata above. No identity issue. Equation, section and figure
numbers on this page are those of the version of record.

# Key claims

1. The model is algebraic, follows the LCTM concept, is Galilean invariant, uses only local variables, and covers natural, bypass and separation-induced transition (Abstract; §5). **Stated** (Galilean invariance by construction of Eq. 10; coverage **Shown** in §3).
2. Transport-equation transition models are dominated by their source terms, with convection and diffusion playing a minor but not negligible role, which justifies an algebraic reduction (§1). **Stated**.
3. The algebraic models of Sandhu & Ghosh and of Kubacki et al. give transition locations that depend on the initial condition (laminar or fully turbulent start) at low $Tu$; the same "hysteresis" can occur in transport models (§1, §2.3). **Stated** for those models; **Shown** for the one-equation γ model (Fig. 3).
4. $Re_{V22}=\tilde\Omega d^2/(2.2\nu)$ with $\tilde\Omega=\max(\lvert S\rvert,\lvert\Omega\rvert,0.1\omega)$; the factor 2.2 makes the maximum of $Re_{V22}$ across a zero-pressure-gradient laminar layer equal $Re_\theta$ (Eq. 1, §2.1). **Stated**.
5. The intermittency is algebraic: $\gamma=\tanh(Rat_{Re}^2)$, $Rat_{Re}=\max(Re_{V22},60)/Re_{\theta c}$, with $Re_{\theta c}=\min\big(CTu_{Crit}\,ReC_{C1}/Tu_l^{ReC_{C2}},\,ReC_{Max}\big)\,FPG(\lambda_{\theta l})$ (Eqs. 2–4). **Stated** (contribution).
6. The limiter 60 is needed to recover fully turbulent behaviour downstream of transition: without it, on T3A, $C_f$ is underpredicted after transition and the velocity profile departs from the log law; with it $\gamma=1$ reaches deeper into the sublayer (§2.2, Fig. 1). **Shown**.
7. A formulation with $\gamma=1$ through the whole viscous layer downstream of transition "is not possible with a criterion as given by Equations (2)-(3)" (§2.2). **Stated**.
8. Transition takes place approximately for $250<Re_\theta<1200$, depending on $Tu$ and pressure gradient (§2.1). **Stated**.
9. $\gamma$ enters only the production of $k$, $P_k\to\gamma P_k$, unlike earlier LCTM formulations in which the destruction term also depended on $\gamma$ (Eq. 5). **Stated** (contribution).
10. The Fluent SST implementation uses $P_\omega=\alpha\rho P_k/(\mu_t+0.001\mu)$ against division by zero; this has little effect in fully turbulent flow but a small noticeable effect on transition (Eq. 6). **Stated**.
11. The Langtry–Menter (2009) modification of the SST blending, $F_1=\max(F_{1,\mathrm{SST}},F_3)$ with $F_3=\exp(-(R_y/120)^2)$, $R_y=\rho d\sqrt k/\mu$, is retained (Eq. 7). **Stated** (background).
12. The harmonic mean $k_h=n/\sum_{i=1}^n k_i^{-1}$ over face-connected cells in $Tu_l$ removes multiple solutions on the Schubauer–Klebanoff plate; with the local cell value the run started fully turbulent differs from the one started laminar (§2.3, Eq. 12, Fig. 2). **Shown**.
13. The hysteresis of the one-equation γ model appeared in Ansys Fluent (cell-centred finite volume) but not in Ansys CFX, attributed to the different stencils; harmonic averaging is now standard in the one-equation model in Fluent (§2.3, Fig. 3). **Shown** (Fig. 3) / **Stated** (attribution).
14. Without a bubble term the laminar separation bubble is too large, because the production of the underlying two-equation model acts too slowly, even when $\gamma$ is switched at the right location by hand (§2.4). **Stated**.
15. The bubble term ($\gamma\to\gamma+\gamma_{\mathrm{Bubble}}$, $\gamma_{\mathrm{Bubble}}\le3$) prevents a strong overestimate of the bubble on the Eppler 387 at $Re_c=10^5$; without it the lift is lower at $\alpha=4^\circ$–$8^\circ$ through laminar stall (§2.4, Figs. 4–5). **Shown**.
16. $\Phi_1$ switches the bubble term off once $\mu_t>2\mu$, and $\Phi_3$ activates it only where $\gamma\approx1$ already, so the term enhances transition but does not start it (§2.4, Eqs. 15, 17). **Stated**.
17. The twelve coefficients of Table 1 are more than the calibration needs; they serve user fine-tuning, the "rubber-band" philosophy of GEKO (§2.5). **Stated**.
18. The tripping indicator of Juntasaro et al. (2021), $Re_{crit}=k/(\lvert S\rvert\nu)$, is with $\omega\sim\lvert S\rvert$ proportional to $Re_{V22}Tu_l^2$, so that model is an LCTM with correlation $Re_c\sim1/Tu_l^2$ (Eqs. 23–24). **Derived**.
19. The Fluent and NTS implementations agree closely; NTS slightly delays the T3 onset (Fig. 7) and differs a little on S809 (Fig. 12). **Shown**.
20. On the zero-pressure-gradient T3 cases the transition location agrees with the transport models and experiment (Fig. 8); on T3C the agreement is satisfactory, with earlier bypass transition than the transport models, while for T3C3 and T3C4 γ-alg-SST and γ-SST predict bubble transition later than γ-$Re_\theta$-SST (Fig. 9). **Shown**.
21. On the Volino cases the model captures the reduction of bubble size with Reynolds number but tends to underpredict the bubble size (Fig. 10). **Shown**.
22. On NLF(1)-0416F the upper-surface transition location agrees with experiment for $\alpha=-12^\circ$ to $+2^\circ$, while γ-$Re_\theta$-SST falls outside the experimental range at all angles and γ-SST delays transition at negative $\alpha$; all models capture the laminar drag bucket (Figs. 13–15). **Shown**.
23. On the Eppler 387 the algebraic model slightly underpredicts and γ-$Re_\theta$-SST slightly overpredicts the bubble size; γ-SST overpredicts it significantly at low $Re_c$ in the mid-$\alpha$ range, which points to a deficiency of that model's bubble terms (Figs. 16–19). **Shown**.
24. On S809 natural transition starts at $\alpha=6^\circ$ for the algebraic model and $7^\circ$ for the transport models, against about $5^\circ$ in experiment; the algebraic model gives slightly better lift and drag (Figs. 20–22). **Shown**.
25. On Pak-B all three LCTM models reproduce the bubble-size trends; γ-alg-SST is on the small-bubble side at $Re=5\cdot10^4$, $Tu=0.08\%$, and γ-SST overpredicts the bubble at $Re=5\cdot10^4$, $Tu=2.85\%$ (Fig. 24). **Shown**.
26. The transport models give reasonable T3A results even with streamwise spacing $10\delta$; the algebraic model deviates from $2\delta$ and is "clearly less forgiving", especially compared with γ-$Re_\theta$ (§4, Fig. 26). **Shown**.
27. The transition location is virtually insensitive to the first-cell height for $y^+_{\max}<5$; γ-alg-SST is unaffected for $y^+_{\max}<6$; on the coarsest mesh transition moves to the leading edge (§4, Fig. 27). **Shown** (the passage is internally inconsistent; see Printed slips).
28. Mesh recommendations: $y^+\le1$ in the transition region, wall-normal expansion ratio at most 1.15 (above 1.2 to be avoided), streamwise step not much larger than the boundary-layer thickness; wall-function meshes are unsuitable (§4). **Stated** (from Figs. 26–28).
29. A hysteresis test (laminar against turbulent start) should be a standard procedure for every new transition model (§1, §5). **Stated**.

# Printed slips

- Eq. (22): "$CAPG = CAPG_{High}(1 - F_{RV1}1) + CAPG_{low}F_{RV1}$": a stray "1"; Eqs. (20)–(21) have the form $(1-F_{RV1})$.
- §2.4: "This term is simply added to the intermittency in Eq. (2) a and thereby enters the production term (Eq. (5):": stray "a" and an unbalanced parenthesis.
- §3.3 heading: "Natural Laminar Flow NLF(1)-0416F and NLF(1)-0416F Airfoils": the section treats NLF(1)-0416F and NLF(1)-0414F.
- Figs. 14 and 15 captions cite "Somers 1861"; the reference is Somers (1981), NASA TM 1861 (Fig. 13 says 1981).
- Introduction: "Slotnick et al. 2030" against the reference list's 2014 report; "Smith and Gamberone (1956)" against "Gamberoni" in the list; "Coder and Maughmer (2014, 2019)" while the 2019 reference is Coder alone; "Drela (1987)" for Drela and Giles (1987); "Ge at al. (2015)".
- §3.1: "experiments of Hultgren and Volino (2001)"; reference and Fig. 10 caption give Volino and Hultgren (2001).
- §3.1 gives the Volino cases at "Tu = 0.2% and Tu = 7%"; Table 2 lists $Tu=0.2$ and $2.5$ (%).
- Table 4: NLF(1)-0416F inlet $Tu=1.5570\%$ and $\mu_t/\mu=1.5515$, against inlet values of about 0.05–0.11% for the other airfoils and 0.10% at the leading edge, with freestream-sustaining terms that "prevent rapid turbulence intensity decay". Inconsistent with the stated setup; the intended value cannot be recovered from the paper.
- §4, p. 864: "For higher values of y+, the transition location moves upstream for the γ-SST and stays unaffected for the γ-alg-SST models. For the γ-alg-SST model, the solution is unaffected for y+max < 6 and then moves upstream." The two sentences contradict each other for γ-alg-SST.
- Typos: "The 'max' function in the denominator us applied" (§2.4); "Alternative correlations where developed" (§1).
- Reference list: Ge et al. (2015) prints the journal "Flow Turbul. Combust." with DOI 10.31274/etd-180810-4424; Suluksna et al. (2009) prints "Int. J. Heat Mass Transf." with a DOI of Int. J. Heat Fluid Flow and a title ending "- ScienceDirect".
- Eq. (11) with Table 1: *(compiler check, not in the sources)* with $CFPG=0.6$ or $1.0$ and $CAPG=-0.5$, both branches give $FPG\le1$ (the floor 0.25 is reachable, the cap 4 is not), so the onset correlation is lowered for both signs of $\lambda_{\theta l}$. The paper neither plots nor discusses $FPG$; this is recorded, not asserted as a slip.

# Notation map

| Menter et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\gamma$ | $\gamma$ | intermittency (transition pages); here algebraic, and above one with the bubble term |
| $S=\sqrt{2S_{ij}S_{ij}}$, $\Omega=\sqrt{2\Omega_{ij}\Omega_{ij}}$ | $\lvert S\rvert$, $\lvert\Omega\rvert$ | with the factor two |
| $d_w$, $y$ | $d$ | wall distance; $y$ used interchangeably in Eq. (24) |
| $Re_\theta$, $Re_{\theta c}$, $Tu$ | $Re_\theta$, $Re_{\theta c}$, $Tu$ | as in the registry; the model name writes "Reθt" |
| $Re_{V22}$, $Rat_{Re}$, $\tilde\Omega$ | $Re_V$, $\mathrm{Rat}$, $\Omega_V$ (page-local on the transition page) | vorticity Reynolds number over 2.2, onset ratio, $\max(\lvert S\rvert,\lvert\Omega\rvert,0.1\omega)$; $\tilde\Omega$ is **not** a Favre filter |
| $Tu_l$, $\lambda_{\theta l}$ | $Tu_l$, $\lambda_{\theta l}$ (page-local) | local intensity (percent, capped at 100), local pressure-gradient indicator |
| $\gamma_{Bubble}$, $C_{bubbleC1}$, $C_{bubbleC2}$, $F_{RV1}$, $RV1_{switch}$ | $\gamma_b$, $C_{b1}$, $C_{b2}$, $F_{RV}$, $RV_{\mathrm{switch}}$ (page-local) | bubble term and coefficient blending |
| $\tilde k$ | $k_h$ (page-local) | **collision:** harmonic mean of $k$ over face-connected cells (Eq. 12), not a Favre filter |
| $\alpha$ | $\alpha$ (SST page) | SST $\omega$-production coefficient; **collision** with the registry's DG blending factor, resolved by page context; also used for the angle of attack |
| $F_1$, $F_{1,SST}$, $F_3$ | $F_1$ | SST blending function and its Langtry–Menter modification |
| $\mu$, $\mu_t$, $\nu$ | $\mu$, $\mu_t$, $\nu$ | as in the registry |
| $c_f$, $C_p$, $C_l$, $C_d$ | $C_f$, $C_p$, $C_L$, $C_D$ | skin-friction, pressure, lift, drag coefficients |
| $\delta$ | $\delta$ | boundary-layer thickness (unit of the streamwise mesh study) |
| $Re$ | $Re_c$ (airfoils) | chord-based on the airfoils; Volino on exit velocity and plate length; Pak-B on inlet velocity and axial chord |

# Reference list

80 printed references in author–year (Springer) style, alphabetical, all merged into the
[bibliography](/bibliography.md) with `citedby` this slug. Xu et al. 2016a and 2016b are printed in
the opposite order to their letters, so their keys are resolved by venue, not by printed order. Two
entries ("Xing-hao", "Daniele") print given names in the surname slot, and their keys need the
Crossref surname. The DOIs printed for Ge et al. (2015) and Suluksna et al. (2009) do not match the
printed journals (see Printed slips). The ERCOFTAC database is an undated web item. Five items lack
volume or pages; none is unparseable and no printed duplicate was found.

# Pages created or updated

Chunk 1 (2026-10-25), cited further in chunks 2, 4, 5, 7. This source is cited on:

- [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)
- [ERCOFTAC T3 flat-plate transition cases](/benchmarks/ercoftac-t3-flat-plate.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Laminar separation bubble](/definitions/laminar-separation-bubble.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [Local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
