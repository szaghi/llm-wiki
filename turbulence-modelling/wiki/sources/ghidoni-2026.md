---
type: Source
title: "Ghidoni et al. (2026) — Assessment of an explicit wall function implementation for the high-order discontinuous Galerkin solution of the RANS and k-ω turbulence model equations"
description: "Explicit wall function for a high-order modal discontinuous Galerkin RANS solver with the Wilcox 2006 k-ω model: an inverted power-law wall model fed from the farthest internal quadrature point of the wall element, accurate on attached layers up to first-element y+ of 320 with about 70% less computing time."
resource: "doi:10.1016/j.jcp.2025.114637"
source_kind: paper
authors: [Ghidoni A., Mantecca E., Noventa G., Pasquale D.]
year: 2026
venue: "J. Comput. Phys. 550:114637"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Journal_of_Computational_Physics_Ghidoni_Assessment_of_an_explicit_wall_function_implementation_for_t.pdf"
tags: [wall-model, k-omega, rans, dg, high-order]
timestamp: 2026-10-27T15:54:00Z
---

# Summary

Ghidoni et al. (2026) build, validate and assess a
[wall function](/methods/rans-wall-function.md) for steady RANS with the
[Wilcox (2006) $k$-$\omega$ model](/methods/k-omega-model.md), solved in
log-$\omega$ form by a high-order modal discontinuous Galerkin method (BR2
lifting, primitive variables, degree up to $N=6$; the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) page
covers its relatives). The closure is a
[Boussinesq](/definitions/boussinesq-hypothesis.md) eddy viscosity. The
motivation is to relax the near-wall resolution of DG RANS, stated as a
first element at $y_1^+\sim10$, and with it the element aspect ratio and
cost. No-slip becomes a slip condition, and the wall stress enters through
a modified viscous flux. The stress comes from the solution at the internal
quadrature point of the wall element farthest from the wall, the matching
practice of [wall-modelled LES](/methods/wall-modelled-les.md) and the
[equilibrium wall model](/methods/equilibrium-wall-model.md). The novelty is
an explicit [law of the wall](/definitions/law-of-the-wall.md): the
Wilhelm–Jacob–Sagaut power law, which originates in
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) RANS, is inverted
in closed form for $u_\tau$. Viscous and power-law values are blended
quartically (Menter), and a turbulent-kinetic-energy velocity scale (Ignat
et al.) keeps the stress defined at separation.

The validation covers the Wieghardt zero-pressure-gradient plate, the
Samuel–Joubert and DLR/UniBw DM2/DM3
[adverse-pressure-gradient plates](/benchmarks/turbulent-boundary-layer.md),
the Driver–Seegmiller [backward-facing step](/benchmarks/backward-facing-step.md)
and the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re_c=6\times10^6$,
on meshes with $y_1^+$ from 1 to 320. Skin friction stays within about 1% of
the wall-resolved reference up to $y_1^+=10$ from $N=3$, and computing time
drops by about 70% at $y_1^+=320$. The explicit law beats Spalding's
iterative one in cost. Accuracy degrades in strong
[adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
($y_1^+>80$, compared there with an SSG/LRR-$\omega$
[Reynolds-stress](/methods/reynolds-stress-model.md) solution) and in the
step's recirculation ($y_1^+>10$). The [Spalart–Allmaras](/methods/spalart-allmaras-model.md)
DG implementation of the group is cited for robustness. The
[SST](/methods/k-omega-sst-model.md) is not used.

# Version read

Version of record (Elsevier typeset, J. Comput. Phys. 550 (2026) 114637;
received 14 August 2025, available online 31 December 2025); 15 pages, all
read, with pp. 2–6 and 13 checked visually. Page 1 agrees with Crossref.

# Key claims

1. Accurate wall-resolved solutions need the first element at $y_1^+\sim1$ for finite volumes and $y_1^+\sim10$ for DG; $y_1^+$ is the height of the first element, not its centroid (§1). **Stated**
2. The only prior wall-function implementation in a DG solver is Tiberga et al. [8], for the $k$-$\varepsilon$ model (§1). **Stated**
3. Implicit laws of the wall (log law, Reichardt, Spalding) need a Newton solve for $u_\tau$ at every wall quadrature point, at a cost that grows with the solution approximation; the explicit power law of Wilhelm et al. [11] avoids it (§1, §3.3, Eqs. 12–14). **Stated** (cost difference **Shown**, Table 2)
4. The power law (Eq. 13) with $y_c^+=11.81$, exponent $m_{\mathrm{pl}}=1/7$, $A_{\mathrm{pl}}=8.3$ inverts explicitly to Eq. (14) for $u_{\tau,\mathrm{vis}}$ and $u_{\tau,\mathrm{log}}$ (§3.3). **Derived**. The inversion and the continuity of Eq. (13) at $y_c^+$ ($8.3\times11.81^{1/7}=11.81$) check out *(compiler check, not in the sources)*.
5. Viscous and power-law friction velocities are merged without discontinuity as $u_\tau=(u_{\tau,\mathrm{vis}}^4+u_{\tau,\mathrm{log}}^4)^{1/4}$, after Menter et al. [26] (Eq. 15). **Stated**
6. Eqs. (14)–(15) are undefined at separation ($U_t\to0$), so the two-velocity-scale approach of Ignat et al. [27] is adopted, $u^*=\beta^{1/4}\sqrt{\bar k}$ (Eq. 16, as printed); because $\bar k=\max(0,k)$ can vanish at low degree or on coarse meshes, the paper sets $\tau_w=\rho_w\max(u^*,u_\tau)\,u_\tau$ (Eq. 17) instead of Ignat's $\rho_wu^*u_\tau$ (§3.3). **Stated** (design choice)
7. The feeding point is the internal quadrature point of the wall element nearest the face opposite the wall (Fig. 1, Alg. 1), so the flow used is resolved, its dependence on the solution approximation is limited, and all computations are local, leaving parallel efficiency unaffected (§3.3). **Stated**
8. Zero-pressure-gradient plate ($Re=11.1\times10^6$ on the plate length, $M_\infty=0.096$): $C_f$ agrees for all $y_1^+$ and $N=1$–$6$; up to $y_1^+=10$ the error against the reference is below 1% from $N=3$ (§4.1, Figs. 2–4, Table 1). **Shown**
9. At $y_1^+=20$ the error is not monotone in $N$ and reaches "about 5%" at $N=6$ (Table 1: 5.514%), attributed to feeding points in the buffer layer where the wall model blends its two branches (§4.1). **Shown**
10. For $y_1^+\ge40$ "an error $<3\%$ is reached from $\mathbb P^3$", with non-ideal convergence in $N$ because feeding points move away from the wall as $N$ grows (§4.1, §5). **Shown** (Table 1 differs at $y_1^+=40$: see Printed slips)
11. The computing-time reduction against the $y_1^+=1$ wall-resolved run grows with $y_1^+$: averages over $N=1$–$6$ of 29.76, 34.14, 45.85, 59.54, 68.96% for $y_1^+=20,40,80,160,320$, maximum 71.77% ($y_1^+=320$, $N=3$) (Table 2). **Shown**
12. At $y_1^+=320$ the explicit law saves more time than the implicit Spalding law: 68.96% against 63.73% on average (Table 2). **Shown**
13. The reduction increases with $N$ on a fixed mesh, attributed to the wall function decoupling the modelled part of the boundary layer from the solution approximation (§4.1). **Shown** (Table 2 is not monotone: see Printed slips)
14. Weak adverse pressure gradient (Samuel–Joubert, $1.5<\beta_{RC}<4.5$): $C_f$ agrees for all $y_1^+$ and $N$; the $y_1^+=1$ mesh converges from $N=2$, the $y_1^+=320$ mesh needs $N=4$, one degree more than at zero pressure gradient; at $N=6$ there is a discrepancy for $y_1^+>20$, mostly on the first part of the plate (§4.2, Figs. 6–7). **Shown**
15. Strong adverse pressure gradient (DM2/DM3, $25<\beta_{RC}<45$): agreement deteriorates for $y_1^+>80$; at $N=6$ the $C_f$ difference grows for $y_1^+=160$ and 320 near the end of the adverse-gradient region, $0.8<x/L<0.85$, because the wall law refers to zero-pressure-gradient layers only (§4.2, Fig. 8). **Shown**
16. Although the power law assumes zero pressure gradient, the wall function "remains accurate even with moderate pressure gradients" (§1). **Shown** (weak-gradient case)
17. Backward-facing step (Driver–Seegmiller, $Re_H=36\,000$, $M_\infty=0.128$): $C_p$, $C_f$, velocity and $Tu$ profiles agree for all $y_1^+\le80$ and $N$; at $N=6$ the $C_f$ difference grows for $y_1^+>10$ only in the recirculation, where the law of the wall gives a wrong $u_\tau$; the effect is confined to the viscous sublayer, so the profiles still agree (§4.3, Figs. 10–11). **Shown**
18. NACA 0012 ($Re_c=6\times10^6$, $M=0.15$, $-15^\circ$ to $15^\circ$): $C_p$, $C_f$, $C_D$, $C_L$ agree for all $y_1^+$ and $N$; at $N=6$ the $C_f$ difference grows for $y_1^+>80$ near the leading edge; $y_1^+=320$ under-predicts the $C_f$ peak and recovers from $x/c=0.15$, with negligible effect on $C_D$, $C_L$ (§4.4, Figs. 13–14). **Shown**
19. At $15^\circ$ incidence, incipient suction-side separation from $x/c=0.72$ reattaches only at the trailing edge; the step-type $C_f$ under-prediction does not appear because the recirculation is smaller (§4.4). **Shown** (qualitative)
20. Accuracy is preserved up to $y_1^+=320$ "with a drastic computing time reduction" (Abstract, §5). **Shown** on attached and weak-gradient layers; claims 15 and 17 bound it
21. Future work: strong adverse gradients, transonic and supersonic regimes, unsteady flows, hybrid RANS/LES and wall-modelled LES (§5). **Stated**

The model and the wall treatment, translated. With $\bar k=\max(0,k)$, a
lower limit on $\ln\omega$, and the source's stress $\tau_{ij}=-\langle\rho
u_i''u_j''\rangle$ written as $-\bar\rho R_{ij}$ (Favre form):
$$\bar\rho R_{ij}-\tfrac23\bar\rho\bar k\delta_{ij}=-2\mu_tS^d_{ij},\qquad \mu_t=\alpha^*\bar\rho\bar k/\omega,$$
with constants $\alpha=13/25$, $\alpha^*=1$, $\beta=0.0708$, $\beta^*=9/100$,
$\sigma_\omega=1/2$, $\sigma_k=3/5$, $\sigma_d=1/8$ (cross-diffusion), the
$\omega$ equation carried as $\ln\omega$ (Eq. 1). Wall-resolved $\omega$
(Eq. 4): $\ln\omega_w=\ln\big(6\nu_w/(\beta(a_Ny_1)^2)\big)$ with
$a_N=\exp(-\sum_{n=1}^N1/n)$. Wall function (Eqs. 13–18):
$$u^+=\begin{cases}y^+, & y^+\le y_c^+,\\ A_{\mathrm{pl}}(y^+)^{m_{\mathrm{pl}}}, & y^+>y_c^+,\end{cases}\qquad u_{\tau,\mathrm{vis}}=\sqrt{\frac{\nu U_t}{y}},\quad u_{\tau,\mathrm{log}}=\Big(\frac{U_t}{A_{\mathrm{pl}}}\Big)^{\frac1{1+m_{\mathrm{pl}}}}y^{-\frac{m_{\mathrm{pl}}}{1+m_{\mathrm{pl}}}}\nu^{\frac{m_{\mathrm{pl}}}{1+m_{\mathrm{pl}}}},$$
$$\tau_w=\rho_w\max(u^*,u_\tau)\,u_\tau,\qquad \boldsymbol n\cdot\nabla k=0,\qquad \omega=\sqrt{\omega_{\mathrm{vis}}^2+\omega_{\mathrm{log}}^2},\quad \omega_{\mathrm{vis}}=\frac{6\nu_w}{\beta y^2},\quad \omega_{\mathrm{log}}=\frac{\max(u^*,u_\tau)}{\sqrt\beta\,\kappa y},$$
the constants as printed. The tangential part of the wall traction is
replaced by $-\tau_w\boldsymbol t$, $\boldsymbol t=\boldsymbol U_t/|\boldsymbol U_t|$
(Eq. 19). The Spalding comparison law (Eq. 12) uses $\kappa\approx0.41$, $B=5$.

# Printed slips

- §4.1: "for the characteristic height of $y_1^+=1$ already for $\mathbb P^1$ solution approximation the error is below 0.5%"; Table 1 prints 0.811% (experiment) and 1.970% (reference) for $y_1^+=1$, $N=1$; 0.416% is the value at $N=2$.
- §4.1 and §5: "From the characteristic height of $y_1^+=40$, an error $<3\%$ is reached from $\mathbb P^3$"; Table 1 prints 3.833% at $y_1^+=40$, $N=3$ (below 3% from $N=4$ there, and from $N=3$ at $y_1^+=80$, 160, 320).
- §4.1, $y_1^+=20$: "the error decreases up to $\mathbb P^3$ solution approximation, reaching approximately 0.5%"; Table 1 prints 7.714, 0.043, 0.409% for $N=1,2,3$, so the minimum is at $N=2$.
- §4.1: "the reduction increases with the solution approximation considering the same mesh"; Table 2 is not monotone (e.g. $y_1^+=320$: 71.77% at $N=3$, 66.84% at $N=4$; $y_1^+=80$: 49.64% at $N=4$, 47.21% at $N=5$).
- Table 1 caption gives the error "on the plate at $x/L=0.923$", whereas Eq. (20) defines it as an average over 1000 wall points. The printed errors for $y_1^+=1$, $N=1$–$3$ agree, within the rounding of the tabulated $C_f$, with the pointwise relative differences of the tabulated $C_f$ from the $N=6$ value ($|2.479-2.431|/2.431=1.97\%$, then 0.41%, 0.21%) *(compiler check, not in the sources)*.
- §4.4: "a lower number of elements, e.g., $5\,929<n_e<2\,899$" (inverted bounds).
- §2: "the turbulent and total stress tensor, $\hat\tau_{ij}$ and $\tau_{ij}$", names swapped relative to the formulas ($\tau_{ij}$ turbulent, $\hat\tau_{ij}$ total).
- §3.1: the discrete solution is sought in $\mathbf V^k_h$ after the space is defined as $\mathbf V^l_h$ (Eq. 7), $l$ being the degree.
- §3.2: the CFL law uses $\mathrm{CFL_{ord}}$, never defined; the listed parameter $\mathrm{CFL_{max}}=10^{20}$ does not appear in the formula; $\alpha$ denotes the CFL exponent, an equation index and the model constant $13/25$.
- Fig. 6 caption "The distribution of Wilcox [32]" and Fig. 7 caption "The distribution of FUN3D [30]", while both legends read "Wilcox $k$-$\omega$ [30]".
- Ref. [32] (Wilcox, "Progress in hypersonic turbulence modeling") printed with year 2025 and the DOI 10.2514/6.1991-1785.
- Typos: "The last raw" (Table 2 caption), "ℙ.6" (Fig. 5 caption).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$, $p$, $\rho$, $T$ (no bars) | $\langle u_i\rangle$, $\langle p\rangle$, $\bar\rho$, … | RANS mean quantities; the source's bar marks limited quantities |
| $\tau_{ij}=2\bar\mu_t(S_{ij}-\frac13\partial_ku_k\delta_{ij})-\frac23\rho\bar k\delta_{ij}$ | $-\bar\rho R_{ij}$ | **collision:** negative convention, and not the SGS stress |
| $\hat\tau_{ij}$ | $\sigma_{ij}-\bar\rho R_{ij}$ | **collision:** hat is not a test filter; total stress |
| $\bar k=\max(0,k)$, $\bar\mu_t$ | $\bar k$, $\mu_t$ (page-local limited values) | **collision:** bar is not the LES filter |
| $\tilde\omega=\log\omega$, $\tilde\omega_r$, $\tilde\omega_{r0}$ | $\ln\omega$, (limited value and its floor) | **collision:** tilde is neither Favre nor SA |
| $\alpha$, $\alpha^*$, $\beta$, $\beta^*$ | $\alpha$, $\alpha^*$, $\beta$, $\beta^*$ (Wilcox names, as on the [$k$-$\omega$ model](/methods/k-omega-model.md) page; $\beta$ is $\beta_\omega$, registry §11, on the [wall-function](/methods/rans-wall-function.md) page) | Wilcox constants 13/25, 1, 0.0708, 9/100; **collision:** $\alpha$ is not the DG/FV blending factor, $\beta$ not the field-inversion multiplier |
| $\sigma^*$, $\sigma$, $\sigma_d$ | $\sigma_k$, $\sigma_\omega$, $\sigma_d$ | 3/5, 1/2, 1/8 |
| $l$, $\mathbb P^l$ | $N$, degree-$N$ approximation | |
| $\alpha^l$ | $a_N$ (page-local) | wall-distance factor of the wall $\omega$ |
| $y_1$, $y_1^+$ | $y_1$, $y_1^+$ (page-local) | first-element height and its wall-unit value |
| $y_{WF}$ | (feeding-point distance, page-local) | plays the role of $h_{\mathrm{wm}}$ |
| $u_t$, $\mathbf u_t$, $\mathbf t$ | $U_t$, $\boldsymbol U_t$, $\boldsymbol t$ (page-local) | tangential velocity at the feeding point |
| $F(y^+)$ | $f(y^+)$ | §11 |
| $y_c^+$, $A$, $B=1/7$ | $y_c^+$, $A_{\mathrm{pl}}$, $m_{\mathrm{pl}}$ (page-local) | **collision:** $B$ is not the log-law intercept |
| $\kappa$, $B=5$ | $\kappa$, $B$ | Spalding and log law |
| $u_{\tau,vis}$, $u_{\tau,log}$, $u^*$ | same (page-local) | **collision:** $u^*$ is not semi-local scaling |
| $\omega_{vis}$, $\omega_{log}$ | same (page-local) | |
| $\beta_{RH}$ | $\beta_{RC}$ (registry §11) | Rotta–Clauser parameter, printed $(\delta^*/\tau_w)\,\partial p/\partial x$ |
| $c_p$, $c_f$, $c_d$, $c_l$ | $C_p$, $C_f$, $C_D$, $C_L$ | |
| $Re_\infty$ | $Re$ | plate length, step height $H$ or chord |
| $Tu$ | $Tu$ | computed as $\sqrt{2k/3}/u_\infty$ |
| $\eta_f$ | (BR2 stability parameter, page-local) | not the Kolmogorov length |
| $n_e$ | (number of elements) | |

# Reference list

33 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. No printed
duplicates. [12] prints "W. Tillman" for Tillmann; [19] (Abbott & von
Doenhoff) is a 2012 reprint printed without publisher; [22] is the PETSc web
page; [30] is the NASA Langley Turbulence Modeling Resource as a corporate
author (2025); [32] carries year 2025 with a 1991 AIAA DOI and is keyed by
the printed year; [5] prints volume issue "(0)" and no DOI.

# Pages created or updated

Chunk 7 (2026-10-26). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Differential Reynolds-stress models](/methods/reynolds-stress-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
