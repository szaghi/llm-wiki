---
type: Source
title: "Balsara et al. (2024) — Efficient Finite Difference WENO Scheme for Hyperbolic Systems with Non-conservative Products"
description: "Extends point-value finite-difference WENO to hyperbolic systems with non-conservative products through a fluctuation form with one reconstruction per zone and an HLLI Riemann solver, which preserves stationary contacts exactly; design order to nine is shown for Euler, Baer–Nunziato, debris-flow and two-layer shallow-water systems."
resource: "doi:10.1007/s42967-023-00275-9"
source_kind: paper
authors: [Balsara D.S., Bhoriya D., Shu C.W., Kumar H.]
year: 2024
venue: "Commun. Appl. Math. Comput. 6:907-962"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Communications_on_Applied_Mathematics_and_Computation_Balsara_Efficient_Finite_Difference_WENO_Scheme_for_Hyperbolic_Syste.pdf"
tags: [finite-difference, non-conservative-systems, path-conservative, stationary-contact-preservation, weno-ao, multiphase]
timestamp: 2026-10-21T12:00:00Z
---

# Summary

Classical finite-difference WENO on point values (Shu–Osher flux splitting of
point fluxes, the [conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md))
cannot treat systems with non-conservative products,
$\partial_tu+\partial_xf(u)+\mathcal C(u)\,\partial_xu=0$. The paper writes the
semi-discrete scheme in [fluctuation form](/methods/fluctuation-form-fd-weno.md):
one WENO reconstruction per zone, in the
[characteristic variables](/methods/characteristic-decomposition.md) of the
zone, gives the face states $u^-_{i+1/2}$ and $u^+_{i-1/2}$ inside zone $i$; a
single-state [HLL-type](/methods/hll-riemann-solvers.md) Riemann solver with
path-integrated non-conservative terms (the HLLI solver of Dumbser & Balsara
2016) is solved at each face; and

$$\frac{d}{dt}u_i=-A(u_i)\frac{u^-_{i+1/2}-u^+_{i-1/2}}{\Delta x}-\frac1{\Delta x}\big(\mathcal D^-_{i+1/2}+\mathcal D^+_{i-1/2}\big),$$

with $A=\partial f/\partial u+\mathcal C$ the quasilinear matrix and $\mathcal D^\mp$ the left-
and right-going fluctuations. For a constant-coefficient linear system in the
[local Lax–Friedrichs](/methods/lax-friedrichs-flux.md) limit this reduces
algebraically to the upwind finite-difference WENO scheme that equals
Shu–Osher/Jiang–Shu LLF FD-WENO; the high-order claim for nonlinear systems
rests on this equivalence and on numerical evidence. Extremal signal speeds
are taken over all faces of the contributing stencils to protect the order.
Anti-diffusive terms restricted to linearly degenerate fields give exact
[stationary contact preservation](/properties/stationary-contact-preservation.md),
and lake-at-rest tests come out [well-balanced](/properties/well-balancing.md)
without modification. For conservation laws as well the scheme needs one
reconstruction per zone instead of two.

Reconstruction is [WENO-AO or multi-resolution WENO](/methods/weno-ao.md),
with fixes in Appendix D: the power of the WENO-Z-type $\tau$ must grow with
the order, and the first-order base polynomial of third-order
multi-resolution WENO is replaced by a [TVD-limited](/definitions/total-variation-diminishing.md)
linear one. Time stepping is [SSP Runge–Kutta](/methods/ssp-runge-kutta.md),
and IMEX for stiff relaxation. Evidence: 2D accuracy tables at orders 3–9 for
Euler ([isentropic vortex](/benchmarks/isentropic-vortex.md)), Baer–Nunziato,
Pitman–Le debris flow and two-layer shallow water; 1D Riemann problems,
Abgrall and well-balancing tests and [blast waves](/benchmarks/woodward-colella-blast-wave.md);
new 2D [shock–bubble](/benchmarks/shock-bubble-interaction.md) and
[shock–vortex](/benchmarks/shock-vortex-interaction.md) tests for the three
non-conservative systems; the [forward-facing step](/benchmarks/forward-facing-step.md),
the [double Mach reflection](/benchmarks/double-mach-reflection.md) and
[2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md) with
stiff relaxation. The flattener of the anti-diffusion is a
[shock indicator](/definitions/troubled-cell-indicator.md); the survey cites
[WENO-Z](/methods/weno-z.md), [mapped WENO](/methods/mapped-weno.md),
[CWENO](/methods/cweno.md) and closed-form
[smoothness indicators](/definitions/smoothness-indicator.md). No theorem is
proved.

# Version read

Author's accepted manuscript (double-spaced, no journal typesetting), 109 PDF
pages: body and appendices pp. 1–58, references pp. 59–64, figure captions
pp. 65–69, figures pp. 71–109. Not the version of record; the journal page
range 907–962 cannot be checked against this file. Page 1 matches Crossref
(title, four authors in this order). The filename year 2023 is the online
year; the issue year is 2024. Equations garbled in the text extraction were
read visually. Equation, table and section numbers cited here are those of the
manuscript.

# Key claims

Registry notation (see the notation map): the source's $U$, $F$, $\hat U^\mp$,
$S$, $S_L$, $S_R$ are $u$, $f$, $u^\mp$, $a$, $s^-$, $s^+$; its $C$, $U^*$, $D^\mp$, $\psi$ are the
page-local $\mathcal C$, $u^{\mathrm{HLL}}$, $\mathcal D^\mp$, $\varphi$ of the concept pages; its WENO-AO linear
weights $\gamma_k$ and unnormalized weights $w_k$ are $d_k$ and $\alpha_k$.

1. Classical FD-WENO (Shu–Osher, Jiang–Shu) has, to the authors' knowledge, never been extended to nonlinear hyperbolic systems with non-conservative products; the paper does so through a fluctuation form (Abstract, §I, §II). **Stated**
2. For a linear constant-coefficient system the first-order upwind scheme (2.2) with $A^\pm=\tfrac12(A\pm aI)$ has the maximal step $\Delta t=\Delta x/a$, $a$ the largest eigenvalue of $\lvert A\rvert$ (§II). **Stated**
3. The high-order version (2.3), $\frac{d}{dt}u_i=-A^+\frac{u^-_{i+1/2}-u^-_{i-1/2}}{\Delta x}-A^-\frac{u^+_{i+1/2}-u^+_{i-1/2}}{\Delta x}$, is conservative and high order for constant $A$, "reduces identically to the LLF scheme from Shu and Osher or Jiang and Shu when the flux is linear in the conserved variables", and keeps pointwise accuracy dimension by dimension for multidimensional linear systems (§II). **Stated**
4. Neither (2.3) nor its naive nonlinear upgrade (2.6), with $A_i^\pm=\tfrac12(A(u_i)\pm a_iI)$, preserves a stationary contact exactly; (2.6) is "unacceptable" (§II). **Stated**
5. Preserving isolated stationary contacts is crucial for the lake-at-rest property and for well-balancing (§III). **Stated**
6. The implicit equation (3.1) for the HLL resolved state with path-integrated non-conservative matrices converges in "a few fixed point iterations" from the first iterate (3.4), "always very rapid for all the problems that we tested" (§III). **Shown** (asserted from experience, no iteration counts)
7. A straight-line path integrated with four-point Gauss–Lobatto quadrature is "often sufficient" (§III). **Stated**
8. The anti-diffusive flux (3.8), added to $\mathcal D^-$ and subtracted from $\mathcal D^+$, is fully conservative and adjusts automatically when $s^\pm$ change, so it is "exactly right whether we choose an HLL formulation or an LLF formulation" (§III, Eqs. 3.8–3.9). **Derived**
9. Anti-diffusion needs only the eigenvectors of the linearly degenerate fields; the rows and columns of $L$, $R$ for genuinely nonlinear fields may be set to zero, as in all results of the paper, which is necessary for debris flow, whose nonlinear eigenvectors are only numerical (§III). **Stated**
10. Resetting $s^-_{i+1/2}$ ($s^+_{i+1/2}$) to the minimum (maximum) over all faces of the stencils contributing to $x_{i+1/2}$ is "needed in order to obtain the order property" (§IV, §VI step 5). **Stated**
11. In the LLF limit and for constant $A$ the fluctuation form (4.1) is algebraically identical to (2.3) (§V, Eqs. 5.1–5.5). **Derived**
12. Eq. (4.1) is not new: "it occurs, with slight modification, as eqn. (32) in DB16 where it is presented as a second order scheme"; the novelty is showing it is legitimately higher-order in the finite-difference sense and demonstrating it across applications (§V). **Stated**
13. The scheme needs one WENO reconstruction per zone against two (for the right- and left-going split fluxes) in LLF FD-WENO, so it is "half as computationally expensive" if the reconstruction dominates the cost (§VI, §XI). **Stated** (no timings)
14. Stiff sources are easy in finite differences because they are collocated pointwise with the unknowns; IMEX Runge–Kutta of Pareschi & Russo is recommended (§VI, §X). **Stated**, illustrated in §X
15. The 2D Euler isentropic vortex reaches design order with WENO-AO-3/(5,3)/(7,3)/(9,3) and multi-resolution WENO of orders 3/5/7/9 with the LLF solver, e.g. WENO-AO-(9,3) $L_1$ error $1.01355\times10^{-10}$ at $384^2$ (rate 8.78) and WENO-AO-(7,3) $5.18406\times10^{-10}$ at $512^2$ (6.93) (§VII.a, Table I). **Shown**
16. The $\tau$ term of WENO-AO had to scale with the order, and third-order multi-resolution WENO "got less than second order accuracy with the published third order accurate version", fixed by an MC- or van Albada-limited linear base polynomial (§VII.a, App. D). **Shown**
17. 2D Baer–Nunziato smooth test: WENO-AO-(7,3) gives $L_1$ rates 7.01/7.02, WENO-AO-(9,3) 9.03 then 8.76 at $192^2$ (Table II). **Shown**
18. 2D Baer–Nunziato vortex: design orders reached; "The seventh order scheme shows a slight degradation in accuracy when the non-linear limiting is turned on" (§VII.b, Table III; see Printed slips). **Shown**
19. The 2D debris-flow and two-layer shallow-water vortices reach design order at 3, 5, 7, 9 for both reconstructions (Tables IV, V). **Shown**
20. Debris-flow RP1 (three superposed stationary linearly degenerate jumps and two shear waves) is preserved exactly "at all orders", HLL and LLF results are identical, and $x$-velocity fluctuations stay below $1.4\times10^{-14}$ (§VIII.a, Fig. 2). **Shown**
21. Lake-at-rest perturbation tests come out well-balanced "without any special modifications for the well-balancing" for debris flow (Fig. 4) and two-layer shallow water (Fig. 9) (§VIII.a, §VIII.c). **Shown** (visual agreement with DB16, no error norms)
22. In the Abgrall test for Baer–Nunziato the pressure deviates from unity by less than $9\times10^{-13}$ and the phase velocities by less than $2\times10^{-13}$; HLL and LLF profiles are "entirely comparable" thanks to anti-diffusion (§VIII.b, Fig. 5). **Shown**
23. Baer–Nunziato RP1–RP6 are run with the anti-diffusion switched off because no good flattener exists for Baer–Nunziato; higher orders resolve interfaces more crisply but "inevitable wiggles close to shocks are also exaggerated by the higher order schemes" (§VIII.b, Fig. 6). **Shown**
24. Integrated solid and gas masses are conserved to at least one part in $10^{12}$ for Baer–Nunziato RP2, RP4 and RP5 (Fig. 6g). **Shown**
25. In two-layer shallow-water RP1 the stationary jumps of the intermediate fields are preserved, higher orders and LLF identical (§VIII.c, Fig. 7). **Shown**
26. Shock positions converge for the Woodward–Colella blast wave (1000 zones, third-order reference on 10,000 zones) at orders 3, 5, 7 (§VIII.d, Fig. 10). **Shown**
27. The 2D shock–bubble and shock–vortex interactions for Baer–Nunziato, two-layer shallow water and debris flow are "genuinely novel" multidimensional tests; fifth and seventh order resolve structures much more crisply than third (§IX, Figs. 11–16). **Shown**
28. Vortices survive passage through shocks of modest strength in Baer–Nunziato and two-layer flow, attributed to angular-momentum conservation via rotational invariance and Noether's theorem (§IX.b, §IX.d). **Stated** (physical interpretation)
29. Seventh-order HLL-based FD-WENO (Fig. 17–18 captions) shows pronounced vortex-sheet roll-up on the forward-facing step ($1440\times480$) and resolves Mach-stem instabilities on the double Mach reflection ($1920\times480$); fifth order is similar (§IX.g, §IX.h, Figs. 17–18). **Shown**
30. IMEX-SSP3(4,3,3) with FD-WENO handles moderately stiff (relaxation rates $10^3$, $10^2$) and severely stiff ($10^5$, $10^2$) Baer–Nunziato relaxation, matching Dumbser & Boscheri (§X, Figs. 19–20). **Shown**

# Printed slips

- §I, p. 3: "In Balsara, Garain and Shu [3] and Balsara et al. [4] we presented closed form expressions"; [3] is Balsara & Shu (2000), Balsara, Garain & Shu is [6].
- §VII, p. 19: "a third order SSP-RK scheme from Shu and Osher [46]"; [46] is Pelanti et al., Shu–Osher is [55].
- §V, p. 16: "by examining eqn. (4.2) along with eqns. (5.2) to (5.5)"; there is no Eq. (4.2), (4.1) is meant.
- Eq. (3.7) uses $S_{i+1/2}$, never defined; Eq. (3.8) uses $S_L$, $S_R$.
- §VII.a, p. 20: "we had to change the 'ε' term that is used in the smoothness indicators so that it scales with the order of accuracy"; App. D changes the power of $\tau$ in the weights and leaves $\epsilon$ unchanged.
- §VII.b, p. 23: the text announces in Table III the accuracy "with the non-linear limiter and also … when only the central stencil is used", but Table III shows WENO-AO against multi-resolution WENO; no limiter-off results are printed. The multi-resolution ninth-order $L_1$ rates in Table III read 4.29, 12.06, 8.55, uncommented.
- §VIII.b, p. 34: "we had to set $\psi=1$ in eqn. (3.8)" right after "we switched off any contribution from the anti-diffusive flux"; in (3.8) $\psi=1$ is full anti-diffusion and $\psi=0$ switches it off.
- §III says "We don't consider well-balancing in this paper", while §VIII is headed "Including Well-Balancing" and §VIII.c states "our method is well-balanced".
- §VII.c, p. 26: "$h_f,u_f,v_f$ as the fluid height, the fluid x-velocity and the solid y-velocity"; fluid y-velocity is meant.
- §VIII.b, p. 33: the right state of the Abgrall test is written "$\phi_{1,L}=0.01$".
- §IX.c, p. 40: the post-shock state is labelled "$(h_{1L},u_{1L},v_{1L},h_{1R},u_{1R},v_{1R},b)$", the second triple being layer-2 quantities; same pattern in §IX.e.
- §IX.f, p. 44: "By an intermediate time of t=0.6, half of the vortex has interacted with the shock"; the final time is 0.24 and the figures are at 0.06.
- §VII.b p. 22 "Adrianov and Warnecke [1]" against the reference list "N. Andrianov".
- App. A says the domain is doubled "for the fifth, seventh and ninth order schemes", §VII.b "for fifth and seventh orders".
- The corrected Eq. (43) of Dumbser et al. given on p. 23 uses $D$, $F_k$, $G$, $H_k$ without defining them, and App. A gives a different closed form for the same angular velocities; the two are not reconciled.

# Notation map

| Balsara et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $U_i$ | $u$, $u_i$ | "primal" (conserved) variables, point values at zone centres: finite difference |
| $F(U)$ | $f(u)$ | physical flux |
| $C(U)$ | $\mathcal C(u)$ (local) | non-conservative product matrix; **$C$ is the TENO constant in the registry** |
| $B=\partial F/\partial U$, $A=B+C$ | $A(u)$, $A=\partial f/\partial u+\mathcal C$ | **the source's $A$ includes $C$, the registry's $A$ is the flux Jacobian; $B$ is the magnetic field and the SBP boundary matrix in the registry** |
| $A^\pm=\tfrac12(A\pm SI)$ | $A^\pm=\tfrac12(A\pm aI)$ | Lax–Friedrichs matrix splitting, not eigen-splitting |
| $S$, $S_i$ | $a$, $a_i$ | largest eigenvalue of $\lvert A\rvert$; **$S(u)$ is the source term in the registry** |
| $S_{L;i+1/2}$, $S_{R;i+1/2}$ | $s^-_{i+1/2}$, $s^+_{i+1/2}$ | extremal signal speeds; LLF limit $s^\pm=\pm\max(\lvert s^-\rvert,\lvert s^+\rvert)$ |
| $\hat U^-_{i+1/2}$, $\hat U^+_{i-1/2}$ | $u^-_{i+1/2}$, $u^+_{i-1/2}$ | face states reconstructed from zone $i$ |
| $U^*_{i+1/2}$ | $u^{\mathrm{HLL}}_{i+1/2}$ (local) | single HLL resolved state; **$u_*$ is the GQL auxiliary state in the registry** |
| $\tilde C(\cdot,\cdot)$, $\Phi(p)$ | $\tilde{\mathcal C}(\cdot,\cdot)$, path $u_{\mathrm a}+\mathsf s(u_{\mathrm b}-u_{\mathrm a})$ (local) | path-averaged matrix on a straight-line path; **$\Phi$ also names the anti-diffusive flux $\Phi_{AD}$** |
| $D^\mp_{HLL}$, $D^\mp_{HLLI}$ | $\mathcal D^\mp$ (local) | fluctuations; **$D$ is the DG differentiation matrix in the registry** |
| $F^*_{HLL}$, $F^*_{HLLI}$ | $\hat f_{i+1/2}$ | numerical flux, given "for conceptual completeness" |
| $\Lambda$, $\Lambda^\pm$, $L$, $R$ | $\lambda_l$, $L$, $R$ | eigenvalues and eigenvectors at $U^*$; only linearly degenerate rows and columns kept |
| $\delta(U^*)$, $\Phi_{AD}$ | $\Delta_{\mathrm{AD}}$, $\Phi^{\mathrm{AD}}$ (local) | anti-diffusion matrix (3.7), anti-diffusive flux (3.8); **$\delta_k$ is the TENO flag in the registry** |
| $\psi_{i+1/2}$ | $\varphi_{i+1/2}$ (local) | flattener, 0 at shocks, 1 in smooth flow; **$\psi$ is the TVD limiter and the entropy flux potential in the registry** |
| $\gamma_k^{r3}$, $\gamma^{r5}_3$ | $d_k$ | WENO-AO linear weights; **$\gamma_k$ is the TENO measure in the registry** |
| $w_k$ | $\alpha_k$ | unnormalized nonlinear weights |
| $\beta_k^{r3}$, $\beta_3^{r5}$ | $\beta_k$ | smoothness indicators of the small and large stencils |
| $\tau$, $\varepsilon$ | $\tau$, $\epsilon$ | WENO-Z-type global indicator, raised to $\tau^2,\tau^3,\tau^4$ for orders 5, 7, 9 |
| $q_1(x)$, $\bar w_i$ | kept | base polynomial and data of multi-resolution WENO |
| $MC_\beta$, $vanAlbada_\varepsilon$ | slope limiters $\psi$ | **the MC parameter $\beta\in[1,2]$ collides with $\beta_k$** |
| $L(U)$, $S(U)$ | $\mathcal L(u)$, $S(u)$ | non-stiff and stiff operators of the IMEX scheme |
| $\alpha,\beta,\eta$ (IMEX) | kept | IMEX-SSP3(4,3,3) coefficients; **collide with $\alpha_k$, $\beta_k$, $\eta$** |
| $\lambda$, $\mu$ | kept | interphase drag and pressure-relaxation rates; **$\lambda$ collides with eigenvalues** |
| $\phi_j,\rho_j,v_j,p_j,\gamma_j,\pi_j$, $P_I$, $V_I$ | kept | Baer–Nunziato phase quantities, stiffened-gas constants, interface pressure and velocity |
| $h_s,h_f$, $h_1,h_2$, $b$, $g$, $\rho$ | kept | debris-flow and two-layer heights, bottom, gravity; **$\rho$ is a density ratio in both models** |
| WENO-AO-$(r_H,3)$ | kept | adaptive-order WENO with large-stencil order $r_H=5,7,9$ and three 3-point stencils |

# Reference list

64 printed references in numbered style ([1]–[64]), roughly alphabetical,
all parsed and merged complete into the [bibliography](/bibliography.md) with
`citedby` `balsara-2024`. Pre-publication items kept as their own entries:
[16] Chiochetti & Müller "in preparation (2022)" and [63] Zhu & Qiu
"accepted, Journal of Computational Physics (2016)". Refs. [4], [8], [11] and
[45] are incomplete (no volume or pages, or start page only); [44] (Pao &
Salas) is an AIAA conference paper. No DOIs are printed. Possible printed
errors in [1] (volume) and [12] (page range) are kept as printed, unverified.
No printed duplicates.

# Pages created or updated

Chunk 1 (2026-10-21), cited further in chunks 2–7 (2026-10-22/23). This source is cited on:

* [Central WENO (CWENO)](/methods/cweno.md)
* [Central-upwind schemes](/methods/central-upwind-scheme.md)
* [Characteristic decomposition](/methods/characteristic-decomposition.md)
* [Conservative finite-difference scheme](/definitions/conservative-finite-difference-scheme.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Fluctuation-form finite-difference WENO for non-conservative systems](/methods/fluctuation-form-fd-weno.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [IMEX Runge–Kutta schemes](/methods/imex-runge-kutta.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [Mapped WENO](/methods/mapped-weno.md)
* [Multi-resolution WENO](/methods/multi-resolution-weno.md)
* [Path-conservative schemes](/methods/path-conservative-scheme.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Smoothness indicators](/definitions/smoothness-indicator.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stationary contact preservation](/properties/stationary-contact-preservation.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [Well-balancing](/properties/well-balancing.md)
* [WENO-AO (adaptive-order WENO)](/methods/weno-ao.md)
* [WENO-JS reconstruction](/methods/weno-js-reconstruction.md)
* [WENO-Z weights](/methods/weno-z.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
