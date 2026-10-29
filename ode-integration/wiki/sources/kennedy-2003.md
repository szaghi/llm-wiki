---
type: Source
title: "Kennedy & Carpenter (2003) — Additive Runge–Kutta schemes for convection–diffusion–reaction equations"
description: "Analyses N-additive Runge–Kutta methods (colored-tree order conditions, coupling counts, additive stability function, conservation, dense output) and constructs the IMEX pairs ARK3(2)4L[2]SA, ARK4(3)6L[2]SA and ARK5(4)8L[2]SA: an explicit method coupled to an L-stable, stiffly accurate, stage-order-2 ESDIRK, tested for stiffness leakage, order reduction and step-size control."
resource: "doi:10.1016/S0168-9274(02)00138-1"
source_kind: paper
authors: [Kennedy C.A., Carpenter M.H.]
year: 2003
venue: "Appl. Numer. Math. 44(1-2):139-181"
local_file: "/home/stefano/papers/mosaic/ode-integration/2003_Crossref_Applied_Numerical_Mathematics_Kennedy_Additive_RungeKutta_schemes_for_convectiondiffusionreaction.pdf"
tags: [imex, additive, diagonally-implicit, order-conditions, step-size-control, order-reduction]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

The paper builds complete IMEX additive Runge–Kutta integrators for
method-of-lines discretizations of convection–diffusion–reaction equations
(compressible reacting Navier–Stokes), with stiff chemistry implicit and
convection plus diffusion explicit. Part one treats general $N$-additive
methods: [order conditions](/results/runge-kutta-order-conditions.md)
through $N$-colored trees, counts of coupling conditions with and without
shared $b$ and $c$, the principal error norm and the
[embedded-pair](/methods/embedded-runge-kutta-pair.md) quality measures,
the multivariable [stability function](/definitions/stability-function.md),
conservation of linear and quadratic invariants and
[dense output](/methods/dense-output.md).

Part two couples an explicit method with an L-stable, [stiffly accurate](/properties/stiff-accuracy.md),
stage-order-2 ESDIRK ([DIRK](/methods/diagonally-implicit-runge-kutta.md))
sharing $b$ and $c$ ([IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)).
It shows that L-stability of the pair needs one more coupling coefficient to
vanish, studies the [internal stability](/definitions/internal-stability.md)
of the implicit stages, Newton [stage solves](/methods/implicit-stage-solvers.md)
with dense-output predictors and I, PI, PID and PC
[step-size controllers](/methods/step-size-control.md). The three new
methods, [ARK3(2)4L[2]SA, ARK4(3)6L[2]SA and ARK5(4)8L[2]SA](/methods/kennedy-carpenter-ark-methods.md),
are printed as rationals with embedded methods and dense output; they are the
IMEX tables of [ARKODE](/software/arkode.md).

Tests on Kaps' problem, the [van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md),
Pareschi and Russo's problem and a hydrogen–oxygen Mach-5 reacting shock
show "catastrophic" stiffness leakage for several earlier IMEX methods,
[order reduction](/definitions/order-reduction.md) at intermediate
[stiffness](/definitions/stiffness.md) for every additive pair of classical
order above 2 but not for the IMEX-BDF (SBDF)
[multistep schemes](/methods/imex-linear-multistep-methods.md), and the best
behaviour for the PID controller. The singular-perturbation limits are
index-1 [DAEs](/definitions/differential-algebraic-equation.md).

# Version read

NASA Technical Memorandum NASA/TM-2001-211038 (July 2001, report L-18107),
54 PDF pages (printed pp. 1–49; text pp. 1–37, references pp. 38–42,
Appendices A–D pp. 43–49), all read. It is the pre-publication report, not
the journal typeset; its title equals the journal title. It is a bitonal scan
whose text layer is unusable for equations: every equation, table and
tableau was read visually, and the Appendix D tableaux were transcribed from
crops. Section, equation, table and appendix numbers cited here are those of
the TM; page numbers are its printed numbers.

# Key claims

1. For an $N$-additive method the number of order conditions at order $i$ is $N\alpha_i^{[N]}$ with $\sum_i\alpha_i^{[N]}x^{i-1}=\prod_i(1-x^i)^{-N\alpha_i^{[N]}}$; e.g. $\alpha^{[2]}=\{1,2,7,26,107,458\}$ (§2.1.2, Eq. 6). **Stated**
2. Without simplifications error-free coupling of $N$ methods holds only to first order; with shared $b$ or shared $c$ to second order; with both, any number of third-order methods with the same stages couple without coupling error (§2.1.2, Tables 1–4). **Derived**
3. With $b^{\mathrm E}=b^{\mathrm I}$ and $c^{\mathrm E}=c^{\mathrm I}$, a 2-additive method has 2, 13, 63 and 272 coupling conditions at orders 4, 5, 6, 7 (Table 4). **Derived**
4. Additive methods conserve linear invariants in general only if all $b$ agree, and certain quadratic invariants only if additionally $\mathcal M^{[\nu,\mu]}_{ij}=b^{[\nu]}_ia^{[\nu]}_{ij}+b^{[\mu]}_ja^{[\mu]}_{ji}-b^{[\nu]}_ib^{[\mu]}_j=0$; cubic invariants cannot be conserved by Runge–Kutta methods (§2.1.6, Eq. 20). **Stated**
5. An ESDIRK cannot be algebraically stable once stage order 2 is imposed (§3, citing Spijker). **Stated**
6. Imposing $D(1)$ on both methods forces $b_s\gamma=b_s(1-c_s)$ and $b_s(1-c_s)=0$, so a column simplifying assumption fits only one of them, and with stiff accuracy ($c_s=1$) only the explicit one (§3.1.1, Eq. 25). **Derived**
7. Stage order 3 is impossible for the ESDIRK because of its second stage: $\sum_ja^{\mathrm I}_{2j}c_j^2-c_2^3/3=4\gamma^3/3\ne0$ (§3.1.1). **Derived**
8. The additive stability function is $R(z_{\mathrm E},z_{\mathrm I})=P(z_{\mathrm E},z_{\mathrm I})/(1-\gamma z_{\mathrm I})^{s-1}$; L-stability of the pair needs $\mathsf p_{s,0}=\mathsf p_{s-1,0}=0$ and the coupling coefficient $\mathsf p_{s-1,1}=0$; "several of the methods given by Ascher et al. and Griepentrog do not account for this and consequently have $R(z^{[E]},-\infty)$ depending linearly on $z^{[E]}$" (§3.1.2, Eq. 31); App. B lists Ascher (2,3,3) with $R(z_{\mathrm E},-\infty)=-0.732(1+z_{\mathrm E})$ and Ascher (3,4,3) with $0.106z_{\mathrm E}$. **Derived**
9. SDIRKs have internal stability $R^{(n)}_{\mathrm{int}}(-\infty)=0$ at every stage, ESDIRKs in general do not (§3.1.2, Eq. 30); Griepentrog's three- and four-stage methods have $R^{(n)}_{\mathrm{int}}(-\infty)=-2.464$ and $-4.909$ at their last stages (Tables 10, 12). **Derived**
10. ARK3(2)4L[2]SA: 4 stages, $\gamma\approx0.43586652150845899941601$ (the I-stable root of $6\gamma^3-18\gamma^2+9\gamma-1=0$), $c_3=3/5$, $\mathcal A^{(4)}=0.07217$, explicit stability limits $(\lambda_{\mathrm{inv}},\lambda_{\mathrm{visc}})=(1.24,0.92)$ (§4, App. B, App. D). **Derived**
11. A five-stage stiffly accurate L-stable stage-order-2 ESDIRK of order 4 needs $24\gamma^4-96\gamma^3+72\gamma^2-16\gamma+1=0$ with one L-stable root, $c_2=2\gamma\approx1.1456$, and minimal principal error $\mathcal A^{(5)}=0.03855$, "approximately 15 times greater than SDIRK4" (§5, Eq. 50). **Derived**
12. ARK4(3)6L[2]SA: $\gamma=1/4$, $c=(0,\tfrac12,\tfrac{83}{250},\tfrac{31}{50},\tfrac{17}{20},1)$, $\mathcal A^{(5)}=0.01224$, $(\lambda_{\mathrm{inv}},\lambda_{\mathrm{visc}})=(2.01,1.06)$ (§5, Eq. 52, App. B). **Derived**
13. ARK5(4)8L[2]SA: 8 stages, $\gamma=41/200$, $\mathcal A^{(6)}=0.006988$; "Better 5(4) pairs probably require nine-stages"; a fourth-order dense output is not possible (§6, Eqs. 58–59). **Derived**/**Stated**
14. All three new pairs couple without coupling error to their full order; all are A-stable and stiffly accurate, the embedded methods are A-stable but not stiffly accurate (App. B, App. C). **Derived**
15. Stiffness leakage, the stiffness of the implicit terms leaking into the explicit ones, is measured by the maximum stable CFL number as the reaction stiffness grows; Zhong ASIRK-3A, Yoh SIRK-3A, Shen ASIRK-3A and Yoh LSSIRK-3A/-4A drop from 0.36–0.57 at $\varepsilon=10^0$ to 0.0 at $10^6$ ("catastrophic") (§8.1, Table 8). **Shown**
16. Under nonequilibrium initial data with exothermic chemistry every additive method leaks in fixed-step mode (e.g. ARK3(2)4L[2]SA 0.57 at $\varepsilon=10^0$ to 0.001 at $10^{-7}$), SBDF2/3/4 show insignificant leakage, and with step-size control the three new methods pass the transient (§8.1, Tables 11, 13). **Shown**
17. On the reacting shock ARK3(2)4L[2]SA and Ascher (2,3,3) are the most accuracy-efficient third-order methods; "ARK4(3)6L[2]SA would appear to be the most efficient high-order IMEX additive Runge-Kutta method of which we are aware for this problem"; the fifth-order results are "disappointing" (§8.2, Figs. 2–3; §9). **Shown**
18. Order reduction appears for all additive pairs of classical order above 2 on Kaps, van der Pol and Pareschi–Russo, but not for SBDF; it is worst at $\varepsilon\approx h$, larger for algebraic than for differential variables; stage order 2 "does not translate into higher order-of-accuracy for the differential variables for any of the IMEX schemes" (§8.3, Figs. 8–12, Table 15). **Shown**
19. Global error model $c_1h^{\alpha}+c_2\varepsilon h^{\beta}$ for $\varepsilon\le\mathrm{Const.}\,h$ (after Hairer et al.), with Table 15's empirical exponents; "No attempt is made to theoretically predict the form of the global error of IMEX ARK$_2$ methods" (§8.3). **Stated**
20. Controllers: $h_{n+1}=\kappa h_n\,\mathrm{err}_n^{-0.49/\hat p}\,\mathrm{err}_{n-1}^{0.34/\hat p}\,\mathrm{err}_{n-2}^{-0.10/\hat p}$ (gains $k_I=0.25$, $k_P=0.14$, $k_D=0.10$, $\hat p$ the embedded order), with variable-step gain formulas (Eq. 43); the I-controller uses $1/(\hat p+1)$ (Eq. 39); PC is ineffective, I marginal, PI and PID guide the integration and PID behaves best, with no theory offered (§3.2.3, §8.4). **Shown**
21. Third-order dense output used as Newton predictor (extrapolation to $\theta=1+rc_i$) gives a uniform speedup for $\varepsilon=10^0$ to $10^{-6}$; extrapolated values are "one and one half orders less accurate" (§3.2.2, §8.5, Table 16). **Shown**
22. Third- and fourth-order SBDF are slightly more efficient than the additive pairs on the reacting shock but lack error estimation and step-size control; Ascher (2,3,2) is substantially more efficient than SBDF2; BDF of order $\ge3$ is "only L($\alpha$) stable" ([BDF](/methods/backward-differentiation-formula.md)) (§1, §8.2, §9). **Shown**

# Printed slips

- Explicit stability limits of ARK5(4)8L[2]SA: §6 prints "$(\lambda,\lambda_v)=(0.43,0.96)$", App. B prints $(0.43,0.67)$. Table 14 gives the viscous efficiency $0.096$ with 7 implicit stages: $0.67/7=0.096$, $0.96/7=0.137$ *(compiler check, not in the sources)*.
- App. B labels a row "Ascher (1,2,2)" with $(s,s_I)=(2,1)$ and orders $(2,2,3,2)$, while §8.2 and Table 14 name "Ascher (1,2,1)" as "a first-order method".
- App. C, ARK3(2)4L[2]SA: the overall $B^{(p+2)}$ entry prints 0.01827, the value of $\hat A^{(p+1)}$ in the adjacent column; ARK4 and ARK5 print 4.455 and 3.072.
- Eq. (59) prints the dense-output quadrature condition as $\sum_ib^*_ic_i^{k-1}=1/k!$; the printed ARK5 coefficients satisfy $\sum_ib^*_{i3}c_i^2=1/3$, the $1/k$ form, which differs from $1/k!$ at $k=3$ *(compiler check, not in the sources)*.
- Table 8 heads its columns $\varepsilon=10^0,10^2,10^4,10^6$ for increasing reaction stiffness; Tables 9, 11 and 13 head theirs $\varepsilon=10^0$ and negative powers of ten (down to $10^{-8}$), and §7.4 defines $\varepsilon^{-1}=k_2/k_3$.
- Eq. (33) defines the norm $\sqrt{M_{ij}M_{ji}}$ with free indices.
- Eq. (46) prints $\delta^{n+1}$ where the other equations write $\delta^{(n+1)}$.
- "Pareshi and Russo" (§7.3) beside "Pareschi"; section title "Kap's Problem"; ref. [51] "Departimento"; ref. [18] "A. Gerische".

# Notation map

| Kennedy & Carpenter (2003) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $U^{(n)}$, $U^{(i)}$ | $y$, $y_n$, $Y_i$ | stage values |
| $\Delta t$ | $h$ | |
| $F^{[\nu]}$, $N$ | $f^{\{\nu\}}$, — | $N$ additive terms |
| $F_{\rm ns}$, $F_{\rm s}$ | $f^{\mathrm E}$, $f^{\mathrm I}$ | nonstiff explicit, stiff implicit |
| $a^{[E]}_{ij}$, $a^{[I]}_{ij}$, $b$, $\hat b$, $c$ | $a^{\mathrm E}_{ij}$, $a^{\mathrm I}_{ij}$, $b$, $\hat b$, $c$ | $b$, $\hat b$, $c$ shared by both tableaux |
| **$q$**, **$p$** | $p$, $\hat p$ | **collision**: the source's $q$ is the main order and $p$ the embedded order |
| $q_{so}$ | $q$ | stage order (of the implicit method) |
| $\mathbf e$ | $\mathbf 1$ | |
| $\gamma$ | $\gamma$ | ESDIRK diagonal $a^{\mathrm I}_{ii}$, $i\ge2$; **also** tree density (§2.1.1) and a PID exponent (Eq. 41) in the source |
| $\tau^{(q)}_{k}$, $\Phi$, $\alpha,\sigma$ | — , $\Phi(\tau)$, — | truncation coefficient $\tau=\frac1\sigma\Phi-\frac{\alpha}{q!}$; **$\alpha$ also a PID exponent** |
| $A^{(q+1)}$, $\hat A$, $B$, $C$, $D$, $E$ | $\mathcal A^{(p+1)}$, $\hat{\mathcal A}$ (page-local), $B$, $C$, $D$, $E$ | principal error norm and embedded quality measures (Kennedy–Carpenter–Lewis); **$A$ collides with the Butcher matrix** |
| $z^{[\nu]}=\lambda^{[\nu]}\Delta t$ | $z_{\mathrm E}$, $z_{\mathrm I}$ (page-local) | |
| $R(z^{[E]},z^{[I]})=P/Q$, $p_{ij}$, $q_i$ | $R(z_{\mathrm E},z_{\mathrm I})$, $\mathsf p_{ij}$, $q_i$ (page-local) | $\mathsf p_{ij}$ multiplies $z_{\mathrm E}^jz_{\mathrm I}^i$; sans-serif because $p$ is the order |
| $R^{(n)}_{\rm int}$ | $R^{(n)}_{\mathrm{int}}$ (page-local) | internal stability function of stage $n$ |
| $\lambda$, $\lambda_v$ | $\lambda_{\mathrm{inv}}$, $\lambda_{\mathrm{visc}}$ (page-local) | inviscid and viscous explicit stability limits; **collide with the eigenvalue $\lambda$** |
| $M^{[\nu,\mu]}_{ij}$ | $\mathcal M_{ij}$ (page-local) | conservation matrix; **$M$ is the registry's mass matrix** |
| $\nu$ (Eq. 45) | $\mu$ (page-local) | viscosity; **collides with the registry's Courant number** |
| $b^*_{ij}$, $\theta$, $p^*$ | same | dense output $b^*_i(\theta)=\sum_jb^*_{ij}\theta^j$ |
| $\delta^{(n+1)}/\epsilon$, $\kappa$ | $\mathrm{err}_n$, $\kappa$ | max-norm error estimate over tolerance; safety factor |
| $\alpha,\beta,\gamma$ (PID) | $\beta_1/k,\ -\beta_2/k,\ \beta_3/k$ | source normalizes by the embedded order $\hat p$, the registry by $k=\min(p,\hat p)+1$ |
| $\varepsilon$ | $\varepsilon$ | stiffness parameter, $\varepsilon^{-1}=k_2/k_3$ |
| ARK$q(p)sS[q_{so}]X$ | — | naming: orders, stages, "L" L-stable, stage order, "SA" stiffly accurate |

# Reference list

The paper prints 77 references in numbered style ([1]–[77], superscript
citations). The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Several printed
items carry keys that collide with different works already in the
bibliography (Hairer 1981 and 1988, ref. [24], [25]; Söderlind, ref. [63],
"To appear", undated; Pareschi & Russo, ref. [51], a 2000 Ferrara preprint,
kept distinct from its published version); the merge resolves them. Refs.
[35] and [63] are cited as accepted or to appear; [61] and [74]–[76] are AIAA
conference papers; [28] unpublished notes; [62] the Sloane–Plouffe book with
a URL; [72] has the corporate author Wolfram Research. Spelling slips are
listed above. No DOIs are printed; all items parsed.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [ARKODE](/software/arkode.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Dense output](/methods/dense-output.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Differential-algebraic equations and their Runge–Kutta treatment](/definitions/differential-algebraic-equation.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Generalized additive Runge–Kutta (GARK) methods and internal consistency](/methods/generalized-additive-runge-kutta.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [IMEX linear multistep and IMEX-BDF methods](/methods/imex-linear-multistep-methods.md)
* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Kennedy–Carpenter additive Runge–Kutta methods (ARK3, ARK4, ARK5)](/methods/kennedy-carpenter-ark-methods.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Order reduction](/definitions/order-reduction.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Stiffness](/definitions/stiffness.md)
* [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
