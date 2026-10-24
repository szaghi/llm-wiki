---
type: Source
title: "Chertock et al. (2023) — Local characteristic decomposition based central-upwind scheme"
description: "Rewrites the second-order central-upwind flux as a central average plus diffusion in local characteristic variables, then gives each characteristic field its own one-sided speeds; the resulting LCD central-upwind scheme is upwind for any linear system and much less dissipative on 1D and 2D Euler tests."
resource: "doi:10.1016/j.jcp.2022.111718"
source_kind: paper
authors: [Chertock A., Chu S., Herty M., Kurganov A., Lukáčová-Medviďová M.]
year: 2023
venue: "J. Comput. Phys. 473:111718"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Journal_of_Computational_Physics_Chertock_Local_characteristic_decomposition_based_central-upwind_sche.pdf"
tags: [central-scheme, characteristic, numerical-dissipation, finite-volume, euler-equations]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

The paper reduces the numerical dissipation of the second-order semi-discrete
[central-upwind scheme](/methods/central-upwind-scheme.md) of Kurganov, Noelle and
Petrova (2001). The central-upwind flux is first rewritten as the central average
$\tfrac12\big(f(\bar u_i)+f(\bar u_{i+1})\big)$ plus a diffusion term. That term is
expressed with the [local characteristic decomposition](/methods/characteristic-decomposition.md)
$R_{i+1/2}$, $L_{i+1/2}=R_{i+1/2}^{-1}$, through three diagonal matrices whose entries
are the same scalar functions of the one-sided speeds $a^\pm_{i+1/2}$. The new
[LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md) replaces these
entries, field by field, with the same functions of one-sided characteristic speeds
$(\lambda_l^\pm)_{i+1/2}$, so each characteristic field receives its own
[numerical dissipation](/definitions/numerical-dissipation.md).

The reconstruction is piecewise linear with a generalized minmod limiter (factor 2),
from the [TVD limiter](/definitions/total-variation-diminishing.md) family, applied to
local characteristic variables. Time integration is three-stage third-order
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) at CFL 0.4. Lemma 3.1 proves that for a
constant-coefficient linear system the new scheme reduces to the second-order upwind
scheme $\hat f_{i+1/2}=A^+u^-_{i+1/2}+A^-u^+_{i+1/2}$ whatever the signs of the
eigenvalues. The original scheme reduces to upwind only when all eigenvalues have one
sign. The 2D scheme works dimension by dimension.

The tests use the 1D and 2D Euler equations:
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md), a stationary-contact problem
(see [stationary contact preservation](/properties/stationary-contact-preservation.md)),
the [Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md),
[2D Riemann configuration 3](/benchmarks/two-dimensional-riemann-problems.md),
explosion, implosion,
[Kelvin–Helmholtz](/benchmarks/kelvin-helmholtz-instability.md) and
[Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md). They show sharper
contacts and much richer instability structure than the original scheme. At equal CPU
time on the implosion problem, the new scheme on $\Delta x=1/2000$ beats the original
on $1/2500$. For Kelvin–Helmholtz, Cesàro averages of the two schemes differ, which
suggests that the limiting dissipative weak solution depends on the numerical
diffusion. No convergence-rate tables are given. The paper's own references link the
same characteristic machinery to [A-WENO](/methods/alternative-weno.md) and to the
[adaptive-diffusion central-upwind flux](/methods/adaptive-diffusion-central-upwind-flux.md).
The paper makes no [entropy-stability](/properties/entropy-stability.md) or positivity
claim.

# Version read

arXiv:2206.08803v2 [math.NA], 20 Jun 2022: an author version, not the JCP version of
record. It has 25 pages, does not print the DOI, and its title and authors match
Crossref. The last author's surname is printed both as "Lukáčová-Medvid'ová" and
"Lukáčová-Medviďová". Equation, example and page numbers are those of the arXiv v2.

# Key claims

The source writes $j$ for the cell index, $d$ for the number of equations and $U$, $F$
for state and flux. Below they become $i$, $m$, $u$, $f$, and the diagonal diffusion
matrices $P$, $M$, $Q$ become $\mathcal P$, $\mathcal M$, $\mathcal Q$, the diffusion $D$ becomes $\mathcal D$,
the characteristic variables $\Gamma$ become $\zeta$ and the threshold $\varepsilon$ becomes $\epsilon_{\mathrm{CU}}$, as on the
concept pages.

1. Staggered central schemes avoid Riemann solvers but carry relatively large numerical dissipation, because "they basically average over the Riemann fans rather than resolving them" (§1). **Stated**
2. Central-upwind schemes use nonuniform control volumes sized by the one-sided local speeds, and the scheme of Kurganov–Noelle–Petrova reduces to upwind for a system whose Jacobian has only positive (or only negative) eigenvalues (§1). **Stated**
3. Earlier ways to reduce central-upwind dissipation are a built-in anti-diffusion from a more accurate evolution step, a numerical dissipation switch, and sharper one-sided speeds from discrete Rankine–Hugoniot conditions (§1). **Stated**
4. The central-upwind flux (2.3) can be written as $\hat f_{i+1/2}=\tfrac12(f_i+f_{i+1})+\mathcal D_{i+1/2}$ with $f_i=f(\bar u_i)$. The diffusion $\mathcal D_{i+1/2}$ is expressed through $R_{i+1/2}$ and diagonal $\mathcal P,\mathcal M,\mathcal Q$ whose identical entries are $\big(a^+,-a^-,a^+a^-\big)/(a^+-a^-)$ ((3.1)–(3.4)). **Derived**
5. The LCD central-upwind flux replaces those entries by field-wise ones, $\big(\lambda_l^+,-\lambda_l^-,\lambda_l^+\lambda_l^-\big)/(\lambda_l^+-\lambda_l^-)$, where $\lambda_l^+=\max\{\lambda_l(A(u^-_{i+1/2})),\lambda_l(A(u^+_{i+1/2})),0\}$ and $\lambda_l^-$ is the corresponding minimum. Entries are set to zero when $\lambda_l^+-\lambda_l^-\le\epsilon_{\mathrm{CU}}$ ((3.5)–(3.8)). **Contribution (definition)**
6. The desingularization constant is $\epsilon_{\mathrm{CU}}=10^{-10}$ in all experiments (§3). **Stated**
7. Lemma 3.1: for $f(u)=Au$ with $A$ constant, the scheme (3.5)–(3.7) becomes the second-order semi-discrete upwind scheme $\hat f_{i+1/2}=A^+u^-_{i+1/2}+A^-u^+_{i+1/2}$, where $A^\pm=R\Lambda^\pm R^{-1}$ ((3.9)–(3.12)). **Proved** (the printed proof has a sign slip; see Printed slips)
8. In the linear case $\mathcal Q\equiv0$, because $\lambda_l^+\lambda_l^-=\max(\lambda_l,0)\min(\lambda_l,0)=0$ (proof of Lemma 3.1). **Proved**
9. The new scheme "has more built-in upwinding" than its predecessor, since it is upwind for linear systems "disregarding the sign of the eigenvalues of $A$" (§1, §3). **Derived** (from Lemma 3.1)
10. The minmod limiter is "the most compressive out of dissipative limiters". Applied to conservative variables it typically produces large oscillations, so it is applied to local characteristic variables (§2.1). **Stated**
11. Limiters are classified as dissipative, compressive or overcompressive: compressive ones can produce kinks, overcompressive ones jumps in the solution (§2.1). **Stated**
12. The formal order is set by the reconstruction and the ODE solver; here they are a second-order piecewise linear reconstruction and three-stage third-order SSP Runge–Kutta (§2). **Stated**
13. The LCD matrices for 1D and 2D Euler are built from the Jacobian at arithmetic averages of the primitive variables, not at Roe averages (Appendices A, B). **Stated**
14. Example 1 (shock–bubble, $\Delta x=1/100$): the new scheme is "sharper and less oscillatory", while the original has lower shock resolution and an oscillation at the contact (§5.1, Fig. 5.1). **Shown**
15. Example 2 (Shu–Osher, $\Delta x=1/80$): the new scheme is "substantially more accurate" in the smooth oscillatory region $x\in[0,3]$ (Fig. 5.2). **Shown**
16. Example 3 (stationary contact, travelling shock and rarefaction, $\Delta x=1/100$): both schemes are non-oscillatory, and the new one resolves the contact better (Fig. 5.3). **Shown**
17. Example 4 (Woodward–Colella, $\Delta x=1/400$): the new scheme gives "slightly higher resolution of the second density spike" (Fig. 5.4). **Shown**
18. Example 5 (2D Riemann configuration 3, $\Delta x=\Delta y=3/2500$): the new scheme captures the sideband instability of the jet and the instability along its neck better (Fig. 5.5). **Shown**
19. Example 6 (explosion, $\Delta x=\Delta y=3/800$, $t=3.2$): the contact curve of the new scheme is "substantially curlier", the mixing layer slightly wider and the shock still stable. The test is presented as a gauge of numerical dissipation (Fig. 5.6). **Shown**
20. Example 7 (implosion): at equal CPU time, the new scheme on $\Delta x=\Delta y=1/2000$ "still achieves a much higher resolution" than the original on $1/2500$. The original on $3/10000$ is "similar" to the new scheme on $1/2000$. No hardware or timings are given (Fig. 5.7). **Shown**
21. Example 8 (Kelvin–Helmholtz, $\Delta x=\Delta y=1/1024$, $t=4$): the new scheme captures much more complicated turbulent mixing (Fig. 5.8). **Shown**
22. For Kelvin–Helmholtz the numerical solutions do not converge under refinement. The limit is a dissipative weak solution, approximated by Cesàro averages that converge strongly in $L^q$, $1\le q<\infty$ (proved in the cited work of Feireisl et al.) (§5.2). **Stated**
23. The Cesàro averages of the new and original densities differ, which indicates "non-uniqueness of the limiting dissipative weak solution that apparently depends on the choice of the numerical diffusion" (Fig. 5.9). **Shown** (visual comparison only)
24. Example 9 (Rayleigh–Taylor, $\gamma=5/3$, $\Delta x=\Delta y=1/1024$): the resolution of the Rayleigh–Taylor structure at $t=1.95$ and $2.95$ is markedly better (Fig. 5.10). **Shown**
25. Settings: $\gamma=1.4$ in Examples 1–8, $\gamma=5/3$ in Example 9, CFL 0.4 throughout (§5). **Stated**

# Printed slips

- Proof of Lemma 3.1, (3.10)–(3.11), p. 7 *(compiler check, not in the sources)*: by (3.8), in the linear case $\mathcal M_l=-\lambda_l^-/(\lambda_l^+-\lambda_l^-)$ is $0$ for $\lambda_l>0$ and $1$ for $\lambda_l<0$, so $\mathcal M=\mathrm{diag}\big(-\min\{\mathrm{sign}\,\lambda_l,0\}\big)$. (3.10) prints $\mathrm{diag}\big(\min\{\mathrm{sign}\,\lambda_l,0\}\big)$, the opposite sign, and (3.11) compensates with a leading minus. Then the printed identity "$\Lambda^-=M\Lambda=\mathrm{diag}(\min\{\lambda_l,0\})$" is false: $\min\{\mathrm{sign}\,\lambda,0\}\,\lambda=-\min\{\lambda,0\}$, so the printed $M$ gives $M\Lambda=-\Lambda^-$. The final result (3.12) is correct.
- §4, p. 8: the $y$-direction diffusion $D^{\rm LCD}_{j,k+1/2}$ is printed with $-RM^{\rm LCD}R^{-1}[\dots]$, while (3.7) and the $x$-direction term have $+$. $M^{\rm LCD}$ is defined in the same way in both directions, so the sign should be $+$.
- Appendix B, last formula, p. 22: "$U^{\rm E,W}_{j+1/2}=R_{j+1/2,k}\Gamma^{\rm E,W}_{j+1/2,k}$" has mismatched indices; it should read $U^{\rm E}_{j,k}=R_{j+1/2,k}\Gamma^{\rm E}_{j,k}$ and $U^{\rm W}_{j+1,k}=R_{j+1/2,k}\Gamma^{\rm W}_{j+1,k}$.
- Appendix A, p. 19: the $(3,1)$ entry of the exact Jacobian $A(U)$ carries a hat, "$-\gamma u\hat E/\rho+(\gamma-1)u^3$", although no averaged quantity belongs in it.
- Cesàro average, p. 17: "$\rho_C(1/2^m)=\frac{\rho(1/2^5)+\dots+\rho(1/2^n)}{m-4}$": the upper index should be $m$.
- Example 8, p. 16: "the vortex streets formed by the adaptive scheme are more pronounced": the paper has no adaptive scheme (the new scheme is presumably meant).
- Example 3, p. 11: "the strong shocks interaction problem proposed in [43]" is the same phrase used for Example 4, but Example 3 is a stationary-contact problem, not the Woodward–Colella blast wave.
- Typos: "The main idea of the new the 1-D LCD-based CU scheme" (§3), "a library of different limiters are available", "which may results in" (§2.1).
- Reference list: [16] and [17] print the first author as "Kuganov". [17] prints the second author as "P. Noelle" and the pages "713–734", which are those of [16]. Also [27] "B. Wendrof", "diference"; [32] "difusion"; [35] page range "1394–1394"; [37] Acta Numer. volume printed "5 (2020)"; [20] "riemann" in lower case.
- Reference [43] *(compiler check, not in the sources)*: Woodward–Colella, J. Comput. Phys. 54, is printed with the year 1988. Crossref gives April 1984 for vol. 54, pp. 115–173.

# Notation map

| Chertock et al. 2023 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $j$ (cell index), $C_j=[x_{j-1/2},x_{j+1/2}]$ | $i$, $I_i$ | |
| $U$, $\bar U_j$ | $u$, $\bar u_i$ | finite-volume cell averages |
| $F(U)$, $G(U)$ | $f(u)=f^{(1)}$, $g(u)=f^{(2)}$ | |
| $F_j:=F(\bar U_j)$ | $f(\bar u_i)$ | flux of the cell average, used in the central part (3.1) |
| $d$ (number of equations) | $m$ | |
| $\lambda_1\le\dots\le\lambda_d$; $\mu_i$ | $\lambda_1\le\dots\le\lambda_m$; eigenvalues of $A^{(2)}$ | |
| $A=\partial F/\partial U$, $B=\partial G/\partial U$ | $A=A^{(1)}$, $A^{(2)}$ | **collision**: registry $B$ is the SBP boundary matrix |
| $U^-_{j+1/2}$, $U^+_{j+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | agree: $-$ is the left state |
| E, W, N, S point values of cell $(j,k)$ | $u^-_{i+1/2,j}$ (E), $u^+_{i-1/2,j}$ (W), and so on | |
| $a^\pm_{j+1/2}$ | $a^\pm_{i+1/2}$ | agree: one-sided local speeds |
| $\hat U_{j+1/2}$, $\hat A_{j+1/2}$ | $\hat u_{i+1/2}$, $A(\hat u_{i+1/2})$ | arithmetic average of the primitive variables, not Roe |
| $R_{j+1/2}$, $R^{-1}_{j+1/2}$ | $R_{i+1/2}$, $L_{i+1/2}$ | |
| $\Gamma_k=R^{-1}_{j+1/2}\bar U_k$, $\Gamma^\pm_{j+1/2}$ | $\bar\zeta_k=L_{i+1/2}\bar u_k$, $\zeta^\pm_{i+1/2}$ (page-local) | local characteristic variables, as on the [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) and [characteristic decomposition](/methods/characteristic-decomposition.md) pages; registry $\Gamma$ is a source spelling of $\gamma$ |
| $P$, $M$, $Q$ (and $^{\rm LCD}$) | $\mathcal P$, $\mathcal M$, $\mathcal Q$ (local) | **collision** with the mass matrix $M$ and the SBP matrix $Q$; renamed here |
| $D_{j+1/2}$, $D^{\rm LCD}_{j+1/2}$ | $\mathcal D_{i+1/2}$, $\mathcal D^{\mathrm{LCD}}_{i+1/2}$ (local) | numerical diffusion; **collision** with the DG differentiation matrix $D$ |
| $(\lambda_i^\pm)_{j+1/2}$ | $\lambda_l^\pm$ at $x_{i+1/2}$ (local) | one-sided characteristic speeds of field $l$ |
| $\varepsilon=10^{-10}$ | $\epsilon_{\mathrm{CU}}$ (local) | desingularization threshold, not the WENO $\epsilon$ |
| $\Lambda^\pm$, $A^\pm$ | $\Lambda^\pm$, $A^\pm$ | positive and negative parts, linear case |
| minmod with factors 2 | generalized minmod, parameter 2 | the source's limiter parameter is written out, not named $\theta$ (registry $\theta$ is the Zhang–Shu scaling factor) |
| $\rho$, $u$, $v$, $p$, $E$, $e$, $H$, $c$, $\gamma$ | $\rho$, $v_1$, $v_2$, $p$, $E$, $e$, $H$, $c$, $\gamma$ | velocity $u$, $v$ translated |
| $\hat\phi=2\hat H-\hat u^2(-\hat v^2)$ | — | auxiliary quantity of $L_{i+1/2}$, equal to $2\hat c^2/(\gamma-1)$ |
| $\rho_C(1/2^m)$ | — | Cesàro average of density |
| "Old CU", "New CU" | central-upwind scheme, LCD central-upwind scheme | |

# Reference list

The paper prints 44 references, numbered [1]–[44] and sorted alphabetically by first
author. The list is merged complete into the [bibliography](/bibliography.md), with
`citedby` including `chertock-2023`. [20] and [26] use a ditto dash for the authors
(Kurganov & Tadmor, Lie & Noelle). [21] is "in preparation" with no year and is its own
entry. [16] and [17] are keyed under the correct spelling "Kurganov". [43] is keyed by
its printed year. Same-author same-year pairs take suffixes in printed order (Feireisl
2021 [4]/[5], Lie 2003 [25]/[26], Schulz-Rinne 1993 [34]/[35]). No item is unparseable.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–11 (2026-10-22/24). This source is cited on:

* [Adaptive-diffusion central-upwind Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md)
* [Central-upwind schemes](/methods/central-upwind-scheme.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
* [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stationary contact preservation](/properties/stationary-contact-preservation.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
