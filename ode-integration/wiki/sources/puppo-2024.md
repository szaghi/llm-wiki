---
type: Source
title: "Puppo et al. (2024) — Quinpi: Integrating Stiff Hyperbolic Systems with Implicit High Order Finite Volume Schemes"
description: "Extends Quinpi, a third-order implicit CWENO finite-volume scheme with Alexander's SDIRK, to stiff hyperbolic systems: a composite backward Euler predictor freezes the nonlinear weights of the stage equations, and a conservative flux-centered a-posteriori time limiter driven by numerical entropy production suppresses oscillations at large Courant numbers."
resource: "doi:10.4208/cicp.oa-2023-0199"
source_kind: paper
authors: [Puppo G., Semplice M., Visconti G.]
year: 2024
venue: "Commun. Comput. Phys. 36:30-70"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_Communications_in_Computational_Physics_Puppo_Quinpi_Integrating_Stiff_Hyperbolic_Systems_with_Implicit_Hi.pdf"
tags: [implicit, stiff, implicit-stage-solvers, hyperbolic-conservation-laws, method-of-lines]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper extends [Quinpi](/methods/quinpi.md) ("implicit CWENO"), introduced by the same authors for scalar conservation laws in 2023, to 1D systems of hyperbolic conservation laws whose wave speeds differ by orders of magnitude, such as low-Mach gas dynamics. The aim is a third-order implicit finite-volume scheme whose step is set by accuracy on the slow material wave, not by the CFL limit of the fast acoustic waves. The authors state explicitly that the scheme is not [asymptotic preserving](/definitions/asymptotic-preserving-scheme.md).

Space uses third-order CWENOZ reconstruction without ghost cells. Time uses Alexander's three-stage, third-order, L-stable [SDIRK](/methods/diagonally-implicit-runge-kutta.md). With CWENO the stage equations are nonlinear even for a linear PDE, because the nonlinear weights depend on the unknowns. Quinpi removes that nonlinearity with a first-order implicit predictor: composite backward Euler at the DIRK abscissae, itself a DIRK with rows $(\theta_1,\dots,\theta_k,0,\dots)$, $\theta_k=c_k-c_{k-1}$, and a piecewise-constant reconstruction. The predictor freezes the weights at each stage, so the corrector stage equation is nonlinear only through the physical flux, and its Newton Jacobian can be assembled explicitly. The predictor also supplies the Newton initial guess and low-order fluxes for limiting (see [implicit-stage solvers](/methods/implicit-stage-solvers.md)).

The new ingredient is a conservative, flux-centered, a-posteriori time limiter inspired by MOOD. Troubled cells are detected from the numerical entropy production of the third-order solution and of the predictor. At their faces the high-order stage fluxes are replaced by the predictor fluxes, repeatedly until no cell is marked.

The evidence is numerical. An advected density wave converges at third order at Courant numbers 10.7 and 673.3, and a low-Mach smooth problem down to $\varepsilon=10^{-4}$ at Courant number 20. Three stiff Riemann problems run at Courant numbers of about 10–12, where the implicit scheme beats explicit CWENOZ on the contact wave with a step about 10 times larger. The paper also runs [colliding acoustic pulses](/benchmarks/colliding-acoustic-pulses.md). Scalar linear-transport and [Burgers](/benchmarks/burgers-equation.md) tests compare the new limiter with the earlier cell-centered and MOOD limiters.

# Version read

arXiv:2307.14685v4 [math.NA], 16 Jul 2024 (title page dated 17 July 2024), 39 pages (text pp. 1–35, references pp. 36–39), all read. It is a post-review manuscript (the acknowledgments thank "the unknown referee"), not the CiCP version of record, and it prints no DOI or journal pagination. Title (in sentence case) and authors match Crossref; no identity problem. Page, equation, table and figure numbers cited here are those of arXiv v4.

# Key claims

Notation: $h$ is the step and $\Delta x$ the mesh width (source $\Delta t$ and $h$). $Y_k$ are the DIRK stage values (source $U^{(k)}$), $Y^\star_k$ the predictor stages (source $U^{\star,(k)}$), $\gamma$ the SDIRK diagonal (source $\lambda$) and $\nu$ the Courant number (source $C$). Finite-volume symbols are those of the source.

1. A high-order implicit finite-volume scheme with WENO or CWENO reconstruction has two nonlinearities in its stage equations: the physical flux, and the reconstruction weights and smoothness indicators. Even for linear PDEs a nonlinear solve is needed, and the Newton Jacobian of the third-order scheme is block-pentadiagonal with $m\times m$ blocks whose entries depend on complicated weight expressions. (§2.2, after Eq. (16)) **Stated**
2. The first-order predictor (piecewise-constant reconstruction and composite backward Euler at the DIRK abscissae) is a DIRK with lower-triangular tableau whose row $k$ is $(\theta_1,\dots,\theta_k,0,\dots)$, $\theta_k=c_k-c_{k-1}$, $c_0=0$, $b=\theta$; it has the same abscissae as the high-order DIRK. (§3.1, Eqs. (19), (22)) **Derived**
3. First-order schemes need no space limiting because they are unconditionally TVD (cited to [43, §2]); the predictor's only nonlinearity is the flux, and its Newton Jacobian is block-tridiagonal. (§3.1, Eqs. (23)–(24)) **Stated** (TVD) / **Derived** (Jacobian)
4. Freezing the nonlinear weights $W_{j,\alpha}$ with the predictor makes the interface values linear in the unknown cell averages (Eq. (18)). The corrector stage system (26) is then nonlinear only through $f$; its Jacobian has the bandwidth of the fully implicit scheme, but its entries "can now be computed explicitly". (§3, §3.2, Eqs. (17)–(18), (25)–(27)) **Derived**
5. Third-order CWENO accuracy holds if $d_k-\omega_k=O(\Delta x)$ (Eq. (29), from the error split (28), citing [19]). Weights computed from first-order cell averages satisfy this asymptotically: in Table 1 their error drops from $3.58\times10^{-1}$ ($N=20$) to $1.37\times10^{-3}$ ($N=5120$), final rate 2.03, equal to the error of the third-order-based weights from $N=160$ on. (§3.2.1, Table 1) **Shown**
6. On large steps, space limiting alone does not prevent spurious oscillations, and a time limiter is needed (citing [4, 24, 43]); without time limiting (Q3) the colliding-flows Riemann problem "blows up at time t = 0.93". (§3.3; §4.1.2, Fig. 4) **Shown**
7. The cell-centered time limiter of [43] is not conservative and needs a conservative correction that is "nontrivial" to extend to systems; the flux-centered limiter is conservative by construction. (§3.3, §5) **Stated** (the extension difficulty is asserted, not demonstrated)
8. The numerical entropy production $S^p$ of an order-$p$ scheme scales as $O(\Delta x^p)$ on smooth cells, $O(\Delta x^{-1})$ at shocks, $O(\Delta x)$ at rarefaction corners and $O(1)$ at contact waves (from [41]). (§3.3.1, after Eq. (31)) **Stated**
9. Detector I2 (ratio $S^3/(S^1+\sigma)>\gamma_2$) fails on flat regions, where both indicators are floating-point zeros: it limits every flux and reduces the scheme to the first-order predictor, and Q3I2 converges at first order ($L^1$ rates 0.48 to 0.98 for $\kappa=0$, 0.61 to 0.99 for $\kappa=4$). (§3.3.1; §4.1.1, Tables 3–4) **Shown**
10. Q3I1 and Q3I3 reach third order on the advected density wave (41)–(42) at $h/\Delta x=4$, for $\kappa=0$ ($\nu\approx10.7$) and $\kappa=4$ ($\nu\approx673.3$): $L^1$ rate 3.00 at $N=2560$ with error $5.44\times10^{-8}$ ($\kappa=0$) and $5.15\times10^{-8}$ ($\kappa=4$). Their errors equal those of the unlimited Q3, because the limiter never fires on this smooth profile. (§4.1.1, Tables 3–4) **Shown**
11. The error on the advected wave is the same for $\kappa=0$ and $\kappa=4$, "even though the latter uses a time-step which violets the explicit CFL by a factor of 60". (§4.1.1) **Shown**
12. On the three stiff Riemann problems the threshold $\gamma_2=1$ gives the smallest $L^1$ contact-wave errors among $\gamma_2\in\{0.10,0.25,0.50,0.75,1.00\}$, so all Q3I3 Riemann runs use $\gamma_2=1$; the convergence and scalar tests use $\gamma_2=0.1$; throughout $\gamma_1=\Delta x$ and $\sigma=10^{-10}$. (§4, §4.1.2, Fig. 3) **Shown**
13. Detector I1 alone is more diffusive than I3; Q3I3 is as accurate as Q3 on the contact waves of the non-symmetric expansion and stiff Lax problems while it reduces oscillations on acoustic waves. (§4.1.2, Fig. 4) **Shown**
14. The time limiter acts on all waves at early times while they separate, later mainly on shocks, and problems with shocks have a larger share of limited steps. Table 5 (Q3I3, maximum limited fluxes / % limited steps): non-symmetric expansion $N=400$: 41/12.5, $N=800$: 52/6.45, $N=1600$: 60/8.2; colliding flows $N=1000$: 27/4, $N=2000$: 43/15, $N=4000$: 68/64.5; stiff Lax $N=200$: 38/83.33, $N=400$: 67/45.46, $N=800$: 77/22.73. (§4.1.2, Table 5, Fig. 5) **Shown**
15. Against explicit CWZb3 at its stability step, implicit Q3I3 at the accuracy step is less accurate on acoustic waves and more accurate on the contact wave, with a step "about 10 times larger". Step pairs (explicit against implicit): $2.7\times10^{-3}$ against $3.3\times10^{-2}$ (non-symmetric expansion, $N=800$); $8.5\times10^{-4}$ against $1.0\times10^{-2}$ (colliding flows, $N=2000$); $7.0\times10^{-4}$ against $7.1\times10^{-3}$ (stiff Lax, $N=800$). (§4.1.2, Fig. 6; §5) **Shown**
16. On the low-Mach smooth problem (rescaled Euler (46)) at $\nu=20$, Q3 without time limiting reaches third order: $L^1$ rate at $N=1280$ of 2.94 ($\varepsilon=0.8$), 2.93 ($\varepsilon=0.3$) and 2.99 ($\varepsilon=10^{-4}$), the last far beyond the explicit limit. Coarse-grid rates are low (0.98, 1.75, 0.26 at $N=160$). (§4.2.1, Table 6) **Shown**
17. The authors "do not claim that the Quinpi approach is asymptotic preserving"; the low-Mach tests show only stability and accuracy. (§4.2) **Stated**
18. Two colliding acoustic pulses (Klein [36]), $\varepsilon=1/11$ and $10^{-4}$, $N=440$, Q3 at $\nu=6.78$: pressure profiles at $t=0.815$ and $1.63$ are compared with explicit CWZb3, graphically only. (§4.2.2, Fig. 7) **Shown**
19. Linear transport, 400 cells, $h/\Delta x=5$ and 10: Q3I3 is less dissipative than Q3P1 [43] and Q3P1MOOD [50] on the discontinuous sine profile and oscillates slightly more on the double step; at $h/\Delta x=10$ no scheme reproduces the upper flat part of the step. (§4.3.1, Fig. 8) **Shown**
20. Burgers equation, 400 cells, $h/\Delta x=3$ and 10: no scheme oscillates before shock formation, but Q3P1 is more diffusive; at $t=0.6$ Q3P1MOOD shows a small undershoot at the left shock and Q3I3 does not; at the larger Courant number Q3P1 and Q3P1MOOD become more dissipative while Q3I3 stays accurate and non-oscillatory. (§4.3.2, Fig. 9) **Shown**
21. Alexander's three-stage SDIRK with $\gamma=0.4358665215$ "is A-stable and stiffly accurate, and therefore it is L-stable", with strictly increasing abscissae, which are "not necessary for our construction". (§4, p. 20) **Stated**
22. The framework carries over to reconstruction in characteristic variables if the predictor computes and stores the characteristic transformation at each stage, so that the corrector stays linear in the reconstruction. (§3.2, Remark 2) **Derived** (not tested)
23. An explicit first-order predictor (Gottlieb, Mullen & Ruuth [31]) restricts the method to small Courant numbers; an implicit predictor costs more but is stable and non-oscillatory at high Courant numbers. (§1, §3) **Stated**
24. Future work: other integrators ("hybrid BDF schemes"), higher order, analysis, dedicated linear solvers and preconditioners, a cheaper time limiter. (§5) **Stated**

The predictor tableau (22) is [stiffly accurate](/properties/stiff-accuracy.md) by construction (its last row equals $b=\theta$) *(compiler check, not in the sources)*; for Alexander's SDIRK the paper gives $\theta=(\gamma,\tfrac{1-\gamma}2,\tfrac{1-\gamma}2)$ (p. 20). In the paper, Newton is solved with GMRES and an ILU(0) preconditioner, and the Rusanov flux Jacobian drops the derivative of the viscosity coefficient. For the Euler tests the Rusanov viscosity is the material speed only, a deliberate under-dissipation of the acoustic waves. *(Compiler caveats, not in the sources:)* third order is verified only on smooth data where the limiter is inactive; no convergence study runs with an active limiter, and no CPU-time comparison between the implicit and explicit schemes is given. The explicit integrator of CWZb3 is not stated.

# Printed slips

- Eq. (26) prints $G(U^{(k)}):=U^{(k)}+\frac{a_{kk}\Delta t}h\Delta\hat F^{(k)}-U^{(k-1)}=0$. Consistency with (15a) and (16) requires $-U^n+\frac{\Delta t}h\sum_{i<k}a_{ki}\Delta\hat F^{(i)}$ in place of $-U^{(k-1)}$; as printed it is the composite-backward-Euler form (23) with $\theta_k\to a_{kk}$ (p. 13).
- Fig. 1 (p. 19) refers to equations "(3.7) with (3.8)", "(3.10) with (3.11)", "(2.14b)–(3.9)" and "(3.22)", which do not exist in the sequentially numbered paper (presumably (23)/(24), (26)/(27), (15b)/(25) and (38)).
- §2.1 after Eq. (4): "$I_0$, $I_L$ and $I_R$ are the regularity indicators of the associated polynomials $P_L$, $P_{\rm opt}$ and $P_R$, respectively"; $I_0$ belongs to $P_{\rm opt}$.
- §3.2.1 writes the third-order weights "$\omega_{j,k}$, $k=0,1,2$", while elsewhere $k=0,L,R$.
- §1: "A fifth order implicit WENO scheme was proposed in [32]"; [32] is Gottlieb–Shu–Tadmor (SIAM Rev. 2001), and the scheme meant is [31], correctly cited in §3.
- Fig. 7 caption: for $\varepsilon=1/11$, $\Delta x=0.1$ and $h/\Delta x=0.423$ give $h=0.0423$ (explicit $6.24\times10^{-3}$), but the caption prints 4.23 and 0.624, which exceed the final time 0.815; for $\varepsilon=10^{-4}$ the caption prints $5.1\times10^{-3}$ and $7.5\times10^{-4}$ against $5.1\times10^{-2}$ and $7.5\times10^{-3}$ from the text. The caption also writes "n = 440 cells".
- Table 6: the first row ($N=160$) prints rates although no coarser grid is listed.
- §4.1.1: "violets the explicit CFL by a factor of 60" ("violates"; the Courant-number ratio is $673.3/10.7\approx63$). Also "Courant-Friedrichs-Levy" (§1), "Mathemtical" (ref. [30]), "weigths" (§3), "exploting" (§2.1).
- Test (a), Eq. (43), uses $(\rho,u,p)$ while (44)–(45) use $(\rho,v,p)$.
- Table 1 is said to show the $O(\Delta x)$ weight condition "fulfilled in both cases", but the observed rates stay below 1 up to $N=640$ (0.08 at $N=80$).

# Notation map

| Puppo et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $t^n$ | $h$, $t_n$ | |
| $h$ | $\Delta x$ | **source $h$ is the mesh width** |
| $U^{(k)}$, $t^{(k)}=(n+c_k)\Delta t$ | $Y_k$, $t_n+c_kh$ | stage values (stage-value form) |
| $a_{ki}$, $b_k$, $c_k$, $s$ | $A$, $b$, $c$, $s$ | $c=A\mathbf 1$ assumed |
| $\lambda=0.4358665215$ | $\gamma$ | SDIRK diagonal; **source $\lambda$ is not the Dahlquist eigenvalue**; $\lambda_j(u)$ also denotes flux-Jacobian eigenvalues |
| $\theta_k=c_k-c_{k-1}$ | kept | composite backward Euler sub-step fractions |
| $U^{\star,(k)}$, $F^{\star,(k)}$ | $Y^\star_k$, kept | predictor stages and first-order fluxes |
| $G$, $G^\star$, $J$, $J^\star$ | kept, page-local | stage residuals and Jacobians of the flux differences; $J$ agrees in role with the registry Jacobian |
| $C$ | $\nu$ | Courant number; in §4.1.2 the ratio of accuracy to stability steps |
| $\varepsilon$ | $\varepsilon$ | low-Mach scaling parameter, $\mathrm{Ma}=\varepsilon/\sqrt\gamma$ |
| $\gamma$ | kept | adiabatic index 1.4; **collides with the SDIRK diagonal $\gamma$ of this page** |
| $\gamma_1$, $\gamma_2$, $\sigma$ | kept | detector thresholds and regularizer |
| $\eta$, $\psi$, $\Psi$ | $\eta$, kept | entropy, entropy flux, numerical entropy flux |
| $(S^p)^n_j$, $S^1$, $S^3$ | kept | numerical entropy production |
| $d_k$, $\omega_k$, $\alpha_k$, $I_k$, $\tau$, $\epsilon$, $p$ | kept | CWENO linear and nonlinear weights, indicators, regularizer, exponent; **$p$ also the RK order and the pressure; $\alpha$ also the Rusanov viscosity** |

# Reference list

51 printed references, numbered [1]–[51], alphabetical by first author. The list is merged complete into the [bibliography](/bibliography.md) with `citedby` puppo-2024. [7] (Barsukow & Borsche) is printed as an arXiv preprint (arXiv:2303.13318, 2023) and is its own preprint entry, `barsukow-2023-b`, distinct from the Barsukow 2023 article already keyed `barsukow-2023`. [16] and [17] are two Coquel, Nguyen, Postel & Tran papers of 2010 and take suffixed keys in printed order; [15] (2009) and [18] (2006) are separate works. [8] and [37] print "Le Veque" in two words. [4] prints a volume but no pages; [27] and [28] print the last co-author "Žeravý" without an initial. [43] (the scalar Quinpi paper, 2023), [50] (Visconti et al., 2023) and [46] (the reconstruction used) are the direct predecessors. [51] prints the author order Zanotti, Dumbser, Loubère, Diot and a variant title of the a-posteriori subcell-limiting paper, which is already in the bibliography as `dumbser-2014`; the printed form is kept in its note. No DOIs are printed.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Colliding acoustic pulses](/benchmarks/colliding-acoustic-pulses.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Quinpi: implicit high-order finite-volume time stepping with a-posteriori time limiting](/methods/quinpi.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
