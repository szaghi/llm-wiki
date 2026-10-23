---
type: Source
title: "Southworth et al. (2024) — Implicit-explicit Runge-Kutta for radiation hydrodynamics I: Gray diffusion"
description: "Applies linearly implicit IMEX (LIMEX) Runge–Kutta methods to gray-diffusion radiation hydrodynamics: a temperature equation and partitions usable by any LIMEX scheme, a three-tableau variant that nearly reproduces the Lie–Trotter split, discrete energy conservation, and errors 3–5 orders below the split at the hydro CFL."
resource: "doi:10.1016/j.jcp.2024.113339"
source_kind: paper
authors: [Southworth B.S., Park H.K., Tokareva S., Charest M.]
year: 2024
venue: "J. Comput. Phys. 518:113339"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Journal_of_Computational_Physics_Southworth_Implicit-explicit_Runge-Kutta_for_radiation_hydrodynamics_I.pdf"
tags: [imex, runge-kutta, splitting, asymptotic-preserving, structure-preserving]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

Non-relativistic radiation hydrodynamics with gray (one-group) radiation diffusion couples hydrodynamics, which runs on an explicit time scale, to radiation-energy and material–radiation coupling terms whose speed-of-light scaling forces implicit treatment. The production standard in DOE codes is a first-order Lie–Trotter-type [operator split](/methods/operator-splitting.md): explicit hydro step, radiation material-motion correction, implicit radiation and temperature solve, energy deposition. Standard additive [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) does not apply directly: the stiff terms depend nonlinearly on the hydro variables through opacities and the equation of state, so there is no clean additive split.

The paper adopts the [linearly implicit IMEX (LIMEX) Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md) approach of Boscarino et al. The state is duplicated into an explicit copy $y^*$ and an implicit copy $y$, the system is written $y'=f(y^*,y)$, ${y^*}'=f(y^*,y)$, and an IMEX pair with $b^{\mathrm I}=b^{\mathrm E}$ is applied, explicit in $y^*$ and implicit in $y$. The contributions are:

- a time-dependent temperature equation, which avoids coupling the tabular equation of state nonlinearly into the implicit solve;
- explicit and semi-implicit partitions of the system, usable by any LIMEX scheme;
- a three-tableau variant (ALIMEX) that reproduces the Lie–Trotter split except for the temperature initial value, showing that the split is "almost" but not exactly a Runge–Kutta method;
- a proof of local and global discrete total-energy conservation under a numerical-flux consistency condition ([conservation of the fully discrete scheme](/properties/entropy-stability.md)).

Tests are 1D radiative shocks at Mach 1.2, 3 and 45 with a second-order finite-volume discretization. Four LIMEX schemes with [L-stable DIRK](/methods/diagonally-implicit-runge-kutta.md) implicit parts and [SSP](/methods/strong-stability-preserving-runge-kutta.md) explicit parts converge at order 2 (sometimes 3). Their errors at the hydro CFL are 3–5 orders of magnitude below those of the split, for 2–4 times the wall-clock cost. Most third-order IMEX schemes failed through negative temperatures at shocks ([positivity](/properties/positivity-preservation.md)). The scheme choice follows an [asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md) requirement attributed to Pareschi and Russo, and reduced orders at Mach 3 and 45 are attributed to solver tolerances ([order reduction](/definitions/order-reduction.md)).

# Version read

Version of record (Elsevier typeset; received 8 May 2023, revised 22 July 2024, accepted 2 August 2024, online 10 August 2024; LA-UR-23-24702), 17 pages, all read; pp. 6–8 and 10–15 were also read visually for equations, tableaux, Table 1 and figures. Page 1 matches Crossref and prints the DOI. This is a different paper from the ingested [southworth-2022](/sources/southworth-2022.md). Its Ref. [31] (Southworth, Olivier, Park & Buvoli, arXiv 2024) is a third, different work and is keyed southworth-2024-b in the bibliography.

# Key claims

Notation: $h$ the step and $\Delta x$ the mesh width (the source's $\Delta t$ and $h$); $f^{\mathrm E}$, $f^{\mathrm I}$ the explicit and implicit parts (the source's $N_E$, $N_I$); $(A^{\mathrm E},b^{\mathrm E},c^{\mathrm E})$ and $(A^{\mathrm I},b^{\mathrm I},c^{\mathrm I})$ the explicit and implicit tableaux (the source's tilde and plain tableaux); $(A^{\mathrm L},b^{\mathrm L})$ the third tableau of ALIMEX (the source's hat); $Y_i$, $Y^*_i$ the implicit and explicit stage values. See the notation map.

1. Lie–Trotter splitting is limited to first order, and any operator splitting has "a hard limit of 2nd-order accuracy"; Strang splitting suffers order reduction on stiff problems (§1, §2). **Stated** (cited)
2. Component-wise (partitioned) and additive partitions of an ODE are equivalent classes (§2.1). **Stated**
3. The LIMEX duplication (4), ${y^*}'=f(y^*,y)$, $y'=f(y^*,y)$, $y(t_0)=y^*(t_0)=y_0$, has the exact solution $y=y^*$ equal to the solution of (3), so partitioned integrators explicit in $y^*$ and implicit in $y$ apply whatever the nonlinear interaction (§2, Eq. (4)). **Derived**
4. LIMEX-RK (9) uses an additive IMEX pair (7) with $b^{\mathrm I}=b^{\mathrm E}$, so $y_{n+1}=y^*_{n+1}$ and no separate explicit solution is stored (§2.2, Eqs. (9), (11)). **Derived** (following Boscarino et al.)
5. The most effective schemes found have $c^{\mathrm I}\ne c^{\mathrm E}$, so non-autonomous problems need care (time as an auxiliary scalar variable) to avoid doubling the stage storage (§2.2). **Stated**
6. A three-tableau ALIMEX-RK (15) with the first-order tableaux (16) gives the step (17): an explicit $f^{\mathrm E}$ step, then a linearization of $f^{\mathrm I}$ about the explicit update and an implicit solve, i.e. a Runge–Kutta realization of the classical split (§2.3). **Derived**. The authors see "no clear benefits" over two-partition LIMEX (§2.3, §3.3.2). **Stated**
7. The standard rad-hydro operator split (steps 1, 1.5, 2, 2.5) sums to the single time-discrete scheme (19a–e), with $T^*=f_T(\rho^{n+1},e_t^*-\lVert\mathbf u^{n+1}\rVert^2/2)$ (§3.1). **Derived**
8. A temperature closure through the equation of state $T=f_T(\rho,e_i)$ inside the radiation solve couples tabular data nonlinearly into the solve; the paper instead derives the temperature equation (24) from $de_i=c_v\,dT$ (§3.2, Eqs. (20)–(24)). **Derived**
9. Additive partitions must sum to the original operator, so the operator-split substitution $\rho\frac{d}{dt}e_i\mapsto\frac{d}{dt}(\rho e_t)$ that uses $\frac{d}{dt}\rho=0$ is not allowed in a Runge–Kutta partition (§3.3, item 2). **Derived**
10. LIMEX-Euler applied to the partition (27) gives the scheme (28), an operator-split-like method that linearizes about $t_n$ rather than after the hydro step (§3.3.1). **Derived**
11. The standard operator split "cannot be exactly posed as a standard ODE integrator due to inconsistent evaluation of temperature in the hydrodynamics vs. radiation equations" (§1, §3.3.2). ALIMEX (29) reproduces the split exactly if $T^*=T_n+h\,\mathcal L_T(\rho^*,\mathbf u^*,e_t^*)/(\rho^*c_v^*)$ (Eq. (30)); both are formally first order (§3.3.2). **Derived**
12. LIMEX-Euler (28) with a finite-volume discretization is locally conservative in total energy $E=\rho e_t+E_r$ if the numerical fluxes satisfy $\hat F_E^n=\hat F_{\rho e_t}^n+\hat F_{E_r}^n$ (Eq. (36)), which local Lax–Friedrichs guarantees when both fluxes use the same viscosity coefficient; the diffusion and volume terms must be discretized identically in (32a) and (32b) (§4.1). **Proved** (short formal argument)
13. Local conservation implies global conservation: the total discrete energy changes only by boundary fluxes (37), and with no boundary flux $\sum_K\lvert K\rvert E^{n+1}=\sum_K\lvert K\rvert E^n$ (§4.2). **Proved**
14. Each stage of a general LIMEX-RK (9) "takes exactly the form of a scaled (by $b_j$) LIMEX-Euler step", so energy conservation extends to every LIMEX-RK scheme (§4.3). **Derived** (one-paragraph argument)
15. Conservation of linear invariants is trivial for explicit and implicit Runge–Kutta but "much more challenging for IMEX integration when the different partitions of the operator are evaluated at different stage vectors"; LIMEX gives a more natural route to conservation than ARK-type methods (§4.3). **Stated**
16. Pareschi & Russo "proven that for IMEX schemes to be asymptotic preserving for hyperbolic equations with stiff relaxation terms, they must have equal implicit and explicit number of stages/not have explicit stages in the implicit method"; none of the chosen schemes is of ESDIRK type or padded (§5.1). **Stated** (attributed to Pareschi & Russo; stronger than the type-A / type-CK classification recorded on the AP and IMEX pages, where type-CK schemes can be AP under further conditions)
17. Radiation hydrodynamics (1) is viewed as a hyperbolic system with stiff relaxation in which $1/\varepsilon$ corresponds to $\sigma_Ec$ and $\sigma_pac$ (§5.1). **Stated**
18. Most third-order IMEX schemes tested had poor stability on these problems and only I-IMEX(3,4,3) proved robust; the authors attribute this to higher-order methods producing nonphysical negative temperatures at shocks, which the code "fixes" (§5.1). **Shown** (only the robust scheme is reported); explanation **Stated**
19. Fine mesh (Figs. 7–9): at large steps the LIMEX schemes reach errors orders of magnitude below the operator split, even with a TVD-RK3 hydro step; for Mach 3, "4–5 orders of magnitude" smaller (§5.2, Fig. 8). Abstract: "3–5 orders of magnitude smaller than the first-order Lie-Trotter operator split at the hydrodynamic CFL"; §1: "3–4 orders of magnitude" for Mach 3. **Shown**
20. Second-order convergence is observed in almost all cases; for Mach 1.2, I-IMEX(3,4,3) and SSP-LDIRK3(3,3,2) converge at order 3, the latter although only formally second order, which the authors attribute to an error dominated by the hydro part, integrated by a third-order explicit tableau (§5.2, Fig. 7). **Shown**
21. Mach 3 and Mach 45 show order reduction, attributed to the implicit-solve tolerance and to the 10-digit coefficients of I-IMEX(3,4,3) as printed in its source, not to the methods (§5.2). **Shown** (reduction); cause **Stated**
22. Lie–Trotter (19) and LIMEX-Euler (28) give nearly identical accuracy on all three problems (§3.3.2, Figs. 7–9). **Shown**
23. Wall-clock (Fig. 10, normalized to LIMEX-Euler): the operator split is about 25% faster than LIMEX-Euler only because the IMEX code is unoptimized; cost scales linearly with the stage count (2-stage about 2×, 3-stage about 3×, 4-stage about 4×), sublinearly in some Mach-45 cases; "for a 2–4× increase in computational cost, one can achieve hundreds or thousands times better accuracy" (§5.2). Hardware is not stated. **Shown**
24. Coarse mesh (200 cells, unresolved shocks): convergence persists, and I-IMEX(3,4,3) gives a more robust third order; convergence is measured against the semi-discrete ODE, not the PDE solution (§5.3, Fig. 11). **Shown**
25. Schemes absent from a convergence plot were unstable at the initial (hydro-CFL) step (§5). **Shown**
26. Even with nonlinear shocks, robust second-order convergence in time to the semi-discrete solution is achievable (§5). **Shown**

*(Compiler checks, not in the sources.)* The "hard limit of 2nd-order accuracy" in claim 1 holds for splittings with real positive coefficients, the case that matters here because stiff diffusion cannot be integrated backward in time. For an additive IMEX pair with $b^{\mathrm I}=b^{\mathrm E}$, linear invariants of each part are kept; the difficulty in claim 15 is specific to an invariant shared by terms evaluated at different stage vectors. The implicit part of I-IMEX(3,4,3) is stiffly accurate, which the paper does not state.

# Printed slips

1. Table 1, Problem 3: $\sigma_a=4.494\times10^8\rho^2/T^{-3.5}$ equals $\rho^2T^{+3.5}$; a Kramers-type opacity is $\rho^2T^{-3.5}$, so either the "/" or the minus sign is a slip.
2. Fine mesh: §5 says "All simulation are run with 2048 spatial cells in 1d"; §5.2 says "a fine spatial mesh of 2000 cells".
3. Improvement for Mach 3: "3–4 orders of magnitude smaller" (§1), "4–5 orders of magnitude smaller" (§5.2), "3–5 orders" (Abstract).
4. Cross-references: §3.3.1 "as derived in [17] and discussed in Section 2.1" (LIMEX is §2.2); Acknowledgements "three-way ARK methods discussed in Section 2.2" (ALIMEX is §2.3).
5. The LIMEX framework is credited to [17] in §1–§2 and to [16] in §6 (both of the same series).
6. Eqs. (28c) and (29c): the flux $-\nabla\cdot[(\rho^ne_t^n+p^n+p_r^n)\mathbf u]$ lacks the superscript $n$ on $\mathbf u$ (compare (19c)).
7. Eq. (29d): the source term $+\sigma_p^*acT^4$ lacks $(T^{n+1})$; (29e): $\sigma_E^*cE_r$ lacks the superscript $n+1$, which (29c,d) carry.
8. Eq. (28e) has $(\rho^{n+1}c_v)$ on the left and an undivided $+\mathcal L_T(\rho^n,\mathbf u^n,e_t^n)$ on the right, whereas (27) divides both terms of the $T$ row by $\rho^*c_v^*$ (for LIMEX-Euler $\rho^*=\rho^n$); multiplying through gives $\rho^nc_v^n$, not $\rho^{n+1}c_v$. Possible inconsistency or an unstated reformulation.
9. Line before (19): "$\sigma_E^*cE^{n+1}-\sigma_P^*ac(T^{n+1})^4$" — $E^{n+1}$ for $E_r^{n+1}$, and $\sigma_P$ for $\sigma_p$.
10. Eq. (30) writes $T_n$ (subscript), elsewhere $T^n$; §3.3.2 writes $T^*=f_T(\rho^*,e_i^*)$, §3.1 $f_T(\rho^{n+1},\cdot)$.
11. §3.1, step 1: "$T^*=f_T(\rho^{n+1},e_t^*)$" — the argument should be $e_i^*$, as in the same sentence and after (19).
12. I-IMEX(3,4,3): the implicit last row prints "0.43586652150" (an extra trailing 0) against "0.4358665215" elsewhere.
13. Tableau (16): the hat tableau prints $\hat c_2=1$ with the row $(0,0)$, so $\hat c\ne\hat A\mathbf 1$ (harmless for autonomous problems, where nodes do not enter, as the paper notes).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $n$ | $h$, $n$ | |
| **$h$** | $\Delta x$ | mesh spacing; **collides** with the registry step |
| $N(y)$; $N_E$, $N_I$ | $f(y)$; $f^{\mathrm E}$, $f^{\mathrm I}$ | autonomous throughout |
| $N(y^*,y)$ | $f(y^*,y)$ | LIMEX right-hand side, explicit in $y^*$, implicit in $y$ |
| $y^*$, $Y_*^{(i)}$; $Y^{(i)}$ | $y^*$, $Y^*_i$; $Y_i$ | stage values; the source's $*$ also marks frozen coefficients ($\sigma^*$, $D^*$) and the post-hydro state of the split |
| $(\tilde{\mathbf c},\tilde A,\tilde{\mathbf b})$ | $(c^{\mathrm E},A^{\mathrm E},b^{\mathrm E})$ | explicit tableau; tilde marks explicit |
| $(\mathbf c,A,\mathbf b)$ | $(c^{\mathrm I},A^{\mathrm I},b^{\mathrm I})$ | DIRK tableau |
| **$(\hat{\mathbf c},\hat A,\hat{\mathbf b})$** | $(c^{\mathrm L},A^{\mathrm L},b^{\mathrm L})$ (page-local) | third (explicit) ALIMEX tableau; **the hat collides** with the registry embedded weights |
| $\epsilon$ | $\varepsilon$ | stiffness parameter |
| **$\gamma$** | $\gamma$ (DIRK diagonal) | the source also uses $\gamma$ for the adiabatic index in Table 1 |
| **$M$** | Mach number $\mathrm{Ma}$ | **collides** with the registry mass matrix |
| $\rho$, $\mathbf u$, $e_t$, $e_i$, $p$, $p_r$, $E_r$, $T$ | kept | hydro and radiation variables |
| $\sigma_E$, $\sigma_p$, $\sigma_a$, $\sigma_s$, $D$, $a$, $c$, $c_v$ | kept | opacities, diffusion coefficient, radiation constant, speed of light, specific heat; $c$ is not an abscissa |
| $\mathcal L_T$, $f_T$, $f_p$ | kept | hydro temperature source, equations of state |
| $\hat F$, $K$, $\lvert K\rvert$ | kept (page-local) | numerical flux, finite-volume cell; **$K$ collides** with the registry iteration count |
| (s, σ, p) names, e.g. SSP-LDIRK3(3,3,2) | kept | Pareschi–Russo naming: implicit stages, explicit stages, order |

# Reference list

35 printed references, numbered [1]–[35]. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` southworth-2024. Ref. [4] has 20 authors, all transcribed. The DOI of [15] is printed with an "ff" ligature and transcribed as 10.3847/1538-4365/ab18ff. Refs. [31], [34] and [35] are arXiv preprints and are kept as their own entries. [31] (arXiv:2401.04285) is keyed southworth-2024-b so that it does not merge with this source. [34] (Buvoli & Southworth, arXiv:2401.04859, the preprint of the later SIAM paper buvoli-2025) is keyed buvoli-2024-b, because buvoli-2024 is a different archive source. Refs. [16] and [18] share the author list and take keys boscarino-2015 and boscarino-2016-b; [17] (Boscarino, Filbet & Russo) is boscarino-2016. Refs. [12] (Hairer 1981) and [32] (Söderlind & Wang 2006) are hairer-1981-b and soderlind-2006-b, because the bibliography already held other works under the plain keys. Ref. [33] is the ingested [ranocha-2022](/sources/ranocha-2022.md). There are no printed duplicates and no unparseable items.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [IMEX and additive Runge–Kutta methods](/methods/imex-runge-kutta.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Order reduction](/definitions/order-reduction.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Semi-implicit and linearly implicit IMEX Runge–Kutta methods](/methods/semi-implicit-imex-runge-kutta.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
