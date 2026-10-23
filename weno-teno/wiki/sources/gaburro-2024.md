---
type: Source
title: "Gaburro et al. (2024) — Discontinuous Galerkin schemes for hyperbolic systems in non-conservative variables: quasi-conservative formulation with subcell finite volume corrections"
description: "ADER-DG on polygonal meshes that evolves primitive variables, with a local conservation defect, a Lax–Wendroff theorem for vanishing defects, proofs that the defect vanishes for smooth flow and contacts, and a shock-triggered conservative subcell finite-volume correction; multi-material Euler tests."
resource: "doi:10.1016/j.cma.2024.117311"
source_kind: paper
authors: [Gaburro E., Boscheri W., Chiocchetti S., Ricchiuto M.]
year: 2024
venue: "Comput. Methods Appl. Mech. Eng. 431:117311"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Computer_Methods_in_Applied_Mechanics_and_Engineering_Gaburro_Discontinuous_Galerkin_schemes_for_hyperbolic_systems_in_non.pdf"
tags: [dg, limiting, non-conservative-systems, path-conservative, multiphase, unstructured-mesh]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

The paper builds an arbitrary-high-order [ADER](/methods/ader-scheme.md)
[discontinuous Galerkin](/methods/discontinuous-galerkin.md) scheme on polygonal
meshes. Predictor and corrector both evolve a non-conservative set of variables,
the primitive $\mathsf V=(\rho,v_1,v_2,p,\chi)$ of two-material
[Euler equations](/definitions/multicomponent-euler-equations.md) with an advected
marker $\chi$. Primitive formulations avoid the interface pressure oscillations of
conservative schemes but converge to wrong shocks. The face terms are
[path-conservative](/methods/path-conservative-scheme.md) fluctuations along the
segment path.

The theory introduces a local conservation defect $\Delta^n_i$: the cell balance
of the conserved averages holds up to $\lvert K_i\rvert\Delta^n_i$. Proposition 1 is a
[Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) for such schemes: if
$\sup_{i,n}\lVert\Delta^n_i\rVert\to0$ and the scheme converges, the limit is a weak
solution. The authors call such schemes locally quasi-conservative. The defect
vanishes in three cases:

* smooth discrete solutions, for both the DG and the subcell finite-volume update
  (Props. 2–3);
* face-data mismatches of order $h^{1+\beta}$ between limited and unlimited cells
  (Prop. 4);
* quasi-one-dimensional contacts with constant velocity and pressure (Prop. 5).

Prop. 5 bears on [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md);
the authors call it a generalization of Abgrall (1996).

At shocks the defect does not vanish. The
[a posteriori subcell limiter](/methods/mood-a-posteriori-limiting.md) therefore
gets a third, shock-triggered detection criterion, a Balsara-type
undivided-divergence [sensor](/definitions/troubled-cell-indicator.md). In the
flagged subcells a [MUSCL–Hancock](/methods/muscl-hancock.md) finite-volume
corrector acts on the conserved variables with the
[Rusanov flux](/methods/lax-friedrichs-flux.md), which removes the defect there.
The other troubled cells are limited in primitive variables.

The tests run $P_1$ to $P_3$ on polygonal meshes:

* the [isentropic vortex](/benchmarks/isentropic-vortex.md), at orders 2 to 4;
* planar Mach 5 to 20 shocks and the [Lax tube](/benchmarks/sod-and-lax-shock-tubes.md);
* a circular Sod [explosion](/benchmarks/explosion-and-implosion-problems.md), where
  the purely primitive scheme gets a wrong shock speed and the hybrid gets the
  right one;
* the [Woodward–Colella blast wave](/benchmarks/woodward-colella-blast-wave.md), the
  [forward-facing step](/benchmarks/forward-facing-step.md) and the
  [double Mach reflection](/benchmarks/double-mach-reflection.md);
* the Quirk–Karni and Haas–Sturtevant [shock–helium bubble](/benchmarks/shock-bubble-interaction.md)
  problems, where conservative second-order schemes oscillate and the hybrid does not.

# Version read

arXiv:2406.15644v1 [math.NA], 21 June 2024, footer "Preprint submitted to Computer
Methods in Applied Mechanics and Engineering, June 25, 2024": a preprint, not the
typeset version of record. 36 pages. Title and authors match page 1. Crossref
capitalizes "Quasi-conservative"; page 1 prints "quasi-conservative". Section,
equation, table and page numbers are those of arXiv v1.

# Key claims

Registry notation, with these page-local symbols: polygonal cell $K_i$ of area
$\lvert K_i\rvert$, subcells $\tau_{i,\alpha}$, characteristic size $h$, primitive vector
$\mathsf V$, marker $\chi$ with values $\chi^{(1)},\chi^{(2)}$, and
$\mathsf G(\chi)=1/(\tilde\gamma(\chi)-1)$ with $\tilde\gamma$ the
material-dependent ratio of specific heats. The defect is $\Delta^n_i$, the shock
sensor $\sigma_{\mathrm s}$ (see the Notation map).

1. Non-conservative formulations give inadmissible results at genuinely nonlinear discontinuities (shocks) but suit interfaces and contacts. Evolving physical variables avoids evaluating complex thermodynamics across interfaces, "a well known source of spurious oscillations" (§1). **Stated**
2. The path-conservative approach with the segment path "is in general not consistent with the correct jump conditions" and may give wrong shocks unless corrected (§1). **Stated**
3. The paper's premise: conservation is expressed only through cell averages, so a non-conservative formulation can be used for the higher modes everywhere if the averages are updated consistently. Exact conservation is strictly needed only at shocks (§1). **Stated**
4. Proposition 1 (local quasi-conservation and Lax–Wendroff). Assume four things: the modified balance $\lvert K_i\rvert(\bar u^{n+1}_i-\bar u^n_i)/\Delta t+\sum_\ell\hat f^n_{i\ell}=\lvert K_i\rvert\Delta^n_i$ (49); weakly convergent initial data; the TVB-type condition (50) on shape-regular meshes; and $\sup_{i,n}\lVert\Delta^n_i\rVert$ vanishing as $h\to0$ (51). Then a convergent scheme converges to a weak solution. The extra term is bounded by $\lvert\Omega\rvert\,t_f\,\lVert\varphi\rVert_{L^\infty}\sup\lvert\Delta^n_i\rvert$ (§4.1). **Proved** (the classical part by reference to Shi & Shu and Abgrall & Roe)
5. The non-conservative path-integral ADER-DG scheme (32) satisfies (49) with the cell defect (54) (§4.2). **Stated** ("can be easily shown")
6. Proposition 2: under the smoothness bounds (59)–(60) there exist consistent continuous numerical fluxes for which the ADER-DG scheme is quasi-conservative with $\Delta^n_i=o(1)$. Appendix A constructs the flux (A.2) and shows $\Delta_i=O(h)$ (§4.3.1, App. A). **Proved** (formal)
7. Proposition 3: the same holds for the subcell path-conservative finite-volume update (39), with subcell defect $\Delta^n_{i,\alpha}=O(h)$ and cell defect $\sum_\alpha(\lvert\tau_{i,\alpha}\rvert/\lvert K_i\rvert)\Delta^n_{i,\alpha}=o(1)$ (§4.3.1). **Proved** (sketch)
8. The hypotheses (59)–(60) bound first derivatives and are stronger than the TVB-type requirement (50) of the Lax–Wendroff proof of Shi & Shu (§4.3.1). **Stated**
9. Proposition 4: when a limited cell and an unlimited one see different face data, and no flux correction is applied, the scheme stays quasi-conservative if the two traces differ by $O(h^{1+\beta})$, $\beta>0$. The proof uses the Lipschitz continuity of the numerical flux. This justifies extending the troubled flag to a layer of neighbours instead of correcting the unflagged cells (§4.3.1). **Proved**
10. Proposition 5: let velocity and pressure be constant up to $O(h^{1+\epsilon})$ in a ball (63), with quadrature exact for degree $N-1$ in cells and $N$ on faces. Then the scheme (32) is quasi-conservative for mass, momentum and energy in three cases. (1) Single-material flow. (2) Multi-material flow with $\mathsf G(\chi)=\chi/(\gamma-1)$ (closure (11)). (3) Multi-material flow with $\tilde\gamma=\chi\gamma$ (closure (12)), provided the discrete equivalence (64) holds. The authors call this a generalization of Abgrall's classical result (§4.3.2, App. B). **Proved** (formal)
11. Points 1 and 2 of Prop. 5 are "well known". Point 2 restates that advecting $1/(\tilde\gamma-1)$ makes the mass, momentum and energy jump conditions hold across material interfaces (§4.3.2). **Stated**
12. In shock-triggered subcells the conservative finite-volume update (67) with the Rusanov flux "entirely removes the local conservation defect", so the scheme formally meets the hypotheses of Prop. 1. The reconstruction (40) preserves the conservative averages by construction (Abstract, §4.4). **Derived**
13. A subcell is shock-triggered if $\sigma_{\mathrm s}<0$. Here $\sigma_{\mathrm s}=(\widetilde{\nabla\cdot v}+m_1h_{i,\alpha}c_{\min})/(m_1h_{i,\alpha}c_{\min})$, with $\widetilde{\nabla\cdot v}$ the undivided divergence (65), $h_{i,\alpha}=\lvert\tau_{i,\alpha}\rvert^{1/2}$ and $m_1\in[1,15]$. The paper uses $m_1=1$ for single-gas Euler and $m_1=15$ for multi-material flows with spatially varying parameters (§4.4, §5). **Stated** (parameter choice)
14. Isentropic vortex on polygonal meshes: orders "as expected", with final-row orders 2.2/2.2 ($P_1$), 2.7/2.7 ($P_2$) and 3.8/3.6 ($P_3$) for $\rho$/$p$. The limiter never activates. The abstract claims "up to fourth order of accuracy in space and time" (§5.1.1, Table 1). **Shown** (but see Printed slips)
15. Planar shocks at $M=5,10,20$ ($P_2$, $P_3$, $h=1/180$, $t_f=0.04$): "both shock position and magnitude are always perfectly captured". Start-up perturbations behind the shock are attributed to the mismatch between the 1D Rankine–Hugoniot and the discrete 2D jump conditions, which conservative schemes also show (§5.1.2, Fig. 1). **Shown**
16. Circular Sod explosion: the DG scheme in non-conservative form everywhere, shocks included, gives a wrong shock speed. Switching to the conservative finite-volume limiter in shock cells "is enough to restore" the correct speed ($h=1/50$ and $1/215$, $P_2$, $P_3$) (§5.1.4, Fig. 3). **Shown**
17. Lax tube ($h=1/430$): the conservative second-order limiter activates "exactly where the shock wave is located", with no shock-speed error (§5.1.3, Fig. 2). **Shown**
18. Woodward–Colella blast wave ($h=1/1080$, $t=0.038$): all waves and shock positions are correct against a 50000-point 1D residual-distribution reference, and $P_2$ to $P_3$ shows visual convergence (§5.1.5, Fig. 4). **Shown**
19. Double Mach reflection ($P_2$, $h=1/220$): the conservative form is used only in shock regions; most of the domain stays in primitive variables. The roll-up of the shear layer is visible (§5.1.7, Fig. 6). **Shown**
20. Quirk–Karni 1D shock/helium-bubble test: a classical conservative second-order finite-volume scheme gives spurious pressure oscillations even on a fine mesh ($h=1/2690$). The $P_2$ quasi-conservative scheme at $h=1/270$ "perfectly agree[s]" with a Kapila-model reference on 20000 cells (§5.2.1, Fig. 7). **Shown**
21. 2D shock–helium bubble: a second-order conservative ENO finite-volume scheme at $h=1/750$ emits circular spurious pressure waves from the interface, while the $P_2$ quasi-conservative scheme at $h=1/150$ "completely avoids any spurious oscillations". Both use the same ENO reconstruction in the limiter, so the oscillations come from the conservative fluxes at material interfaces and are "not related to Gibbs-like oscillations" (§5.2.2, Fig. 8). **Shown**
22. The limiter activates both at the bubble interface and at the shock, but the conservative form is used only in shock-triggered cells, so the oscillation-free primitive solution at the interface is unaffected (Fig. 9). Mesh convergence of the main structures is shown for $h=1/30$, $1/75$, $1/150$ (Fig. 10). **Shown**
23. The method is "naturally formulated within the very high order ADER predictor-corrector approach with a posteriori limiting". It extends Zanotti & Dumbser, who used primitive variables only in the predictor (§1, §4). **Stated**
24. Open issues: the free parameter $m_1$ of the shock sensor; models with non-conservative terms, where the conservative correction is not obvious; Lagrangian and IMEX extensions (§6). **Stated**

# Printed slips

- App. B, Case 3 (p. 33): $\Gamma_0:=\frac1{\chi_2-\chi_1}\big(\frac1{\gamma_2-1}-\frac1{\gamma_2-1}\big)$ is identically zero. The linear map below (64) uses $\frac1{\gamma_2-1}-\frac1{\gamma_1-1}$, so the second term should carry $\gamma_1$.
- Eq. (57) (p. 12): the subcell balance is printed with $\lvert\omega_i\rvert(\bar q^{n+1}_{i,\alpha}-\bar q^n_{i,\alpha})/\Delta t$ on the left. The subcell balance (44) and the definition (55) require $\lvert\tau_{i,\alpha}\rvert$.
- Eq. (75), Quirk–Karni data: the "otherwise" state is printed "$(1,0,0,1,1,1)$", six entries for the five-component $(\rho,u,v,p,c)$.
- §5.2.2, output times: $t=t^*+[32,\dots,983]$ μs are said to correspond to $T=T^*+[0.584,\dots,5.754]$. The ratio $t/T$ is constant only if the bracketed list holds absolute dimensionless times: $107/0.584=183.2$ μs, $1058/5.754=183.9$ μs and $75/0.410=182.9$ μs, while the increments give 54.8 to 170.8 μs. Fig. 10 also labels $t=2.731$, $4.074$, $5.754$. The printed definition $T=t/(r_b/(c_aM))$ with $r_b=0.05$, $c_a=331.6$ m/s and $M=1.22$ gives a time unit of 123.6 μs, not about 183 μs, so the printed parameters are mutually inconsistent *(compiler check, not in the sources)*.
- §5.2.2: $\rho_a=1.29\cdot10^{-3}$ [kg/m$^3$]. $\sqrt{\gamma p_a/\rho_a}$ gives the printed $c_a=331.6$ m/s only with $\rho_a=1.29$ kg/m$^3$; the printed value is in g/cm$^3$ *(compiler check, not in the sources)*.
- §3.1: the space–time basis of monomials of total degree $\le N$ in $(x,y,t)$ is said to have $\mathcal L=\mathrm{dof}(N+1,d)$ elements. That count is $\mathrm{dof}(N,d+1)=(N+1)(N+2)(N+3)/6$, 4 for $N=1$, against $\mathrm{dof}(N+1,2)=6$ *(compiler check, not in the sources)*.
- Table 1, last $P_3$ row: the printed orders are 3.8 ($\rho$) and 3.6 ($p$), but the printed $h=1.15\to0.92$ and errors $6.00\times10^{-3}\to2.73\times10^{-3}$, $6.75\times10^{-3}\to3.16\times10^{-3}$ give 3.53 and 3.40. Rounding of the printed $h$ ($1.145$–$1.155$, $0.915$–$0.925$) moves them to at most 3.69 and 3.56, so it accounts for the printed 3.6 of $p$ but not for the 3.8 of $\rho$; the other rows of Table 1 are reproduced to within 0.05 *(compiler check, not in the sources)*.
- Cross-references: §4.1 places the subcell limiter in "Section 3.2" (it is §3.4); §4.4 cites "Property 4" for Proposition 4; Prop. 2 calls (54) the "subcell conservation defect", which is (55).
- After Eq. (7) the Lipschitz constants are listed as $K_{\mathbf T}$, $K_{\mathbf A}$, $K_{\mathbf A_{\mathbf V}}$, while (7) uses $K_{\mathbf T}$, $K_{\mathbf T^{-1}}$, $K_{\mathbf A_{\mathbf V}}$.
- §4.4 gives $N_{\tau,i}$ two values ($N_{k,i}$, then $N_{k,i}N^2$).
- §5.1.1 is titled "Moving isentropic Shu-type vortex", but the background velocity is zero and the text calls it "a stationary equilibrium"; $r$ is not defined.
- (47) and (51) use "$O(1)$" for a quantity vanishing as $h\to0$, i.e. $o(1)$, as the text after (47) explains.
- The last row of the Roe-type average (18) begins with $\bar{\tilde\gamma}_{12}$ where (15) has $\chi$.
- Typos: "Lax-Wedroff" (Prop. 1), "rarefaction fun" (§5.1.3), "quasi-concervative" (Figs. 5–6), "spurios" (Fig. 7), "mutiphase" (§5.2.1), "Hass and Sturtevant" in the text against "Haas" in ref. [38].

# Notation map

| Gaburro et al. 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf Q$, $\mathbb F=(\mathbf F,\mathbf G)$ | $u$, $(f^{(1)},f^{(2)})$ | conserved variables and fluxes |
| $\mathbf V=(\rho,u,v,p,\chi)$ | $\mathsf V=(\rho,v_1,v_2,p,\chi)$ (local) | primitive variables; the source's $u,v$ are velocity components |
| $\mathbf T=\partial\mathbf V/\partial\mathbf Q$ | $\partial\mathsf V/\partial u$ | change of variables; $\widehat{\mathbf T}^{-1}$ a Roe-type average |
| $\mathbf A$, $\mathbf B$; $\mathbf A_{\mathbf V}$, $\mathbf B_{\mathbf V}$ | $A^{(1)}$, $A^{(2)}$; their similar primitive-variable matrices | same eigenvalues $\lambda_l$ |
| $\mathbf H=\mathbf A_{\mathbf V}\partial_x\mathbf V+\mathbf B_{\mathbf V}\partial_y\mathbf V$ | non-conservative product | as $\mathcal C(u)\partial_xu$ of the path-conservative pages |
| $\mathcal D\cdot\mathbf n$, $\mathcal D^-_{\mathbf n}$, $\Psi$ | path-integral fluctuation, segment path | **collision**: $\Psi$ is the path, not the Ducros sensor $\Psi_{\mathrm D}$ |
| $\chi$, $\chi_1$, $\chi_2$ | $\chi$, $\chi^{(1)}$, $\chi^{(2)}$ (local) | material marker; **collision** with the TENO measure $\chi_k$, so the values carry superscripts here |
| $\tilde\gamma$, $\tilde\lambda=1/(\tilde\gamma-1)$ | $\tilde\gamma$, $\mathsf G(\chi)$ | **collision**: $\tilde\lambda$ is not an eigenvalue |
| $\kappa=u^2/2+v^2/2$ | $\kappa/\rho$ | **collision**: registry $\kappa$ is per unit volume |
| $\beta(p,\chi,\gamma)$ | — | thermodynamic entry of $\mathbf T^{-1}$; **collision** with $\beta_k$ |
| $c$ | $c$ | sound speed; **collision**: in Eqs. (75)–(78) $c$ is the marker $\chi$ |
| $\omega_i$, $\lvert\omega_i\rvert$, $h_i$ | $K_i$, $\lvert K_i\rvert$, $h$ | polygonal cell; **collision** with the weights $\omega_k$ |
| $\tau_{i,\alpha}$, $h_{i,\alpha}$ | $\tau_{i,\alpha}$, $h_{i,\alpha}$ (local) | subcell triangles; **collision**: $\alpha$ is a subcell index, not the blending coefficient |
| $N$, $P_N$ | $N$, $\mathbb P^N$ | DG degree, order $N+1$; agrees |
| $\mathbf v_h$, $\tilde{\mathbf v}_h$ | $u_h$ (in primitive variables), space–time predictor | |
| $\mathcal P$, $\mathcal R$ | projection to subcell averages, reconstruction | **collision**: $\mathcal R$ is the normalised reconstruction operator on other pages |
| $\Delta^n_i$, $\Delta^n_{i,\alpha}$; $\Phi_i$ | $\Delta^n_i$, $\Delta^n_{i,\alpha}$ (local); flux balance | conservation defect |
| $F^n_{i\ell}$, $\mathbf F(\cdot,\cdot)\cdot\mathbf n$ | $\hat f_{i\ell}$, $h(u^-,u^+)$ | face flux; Rusanov $=h^{\mathrm{LF}}$ |
| $\sigma_{i,\alpha}$, $m_1$ | $\sigma_{\mathrm s}$, $m_1$ (local) | shock sensor; **collision** with the affine scaling $\sigma$ |
| $\delta$, $\delta_0$, $\epsilon$ | DMP relaxation, positivity threshold | $\epsilon$ is also the exponent in (63) and the vortex strength $\mathcal E=5$ in (68) |
| $\rho(\chi_h)$ in (64) | — | linear map from closure (11) to (12), not the density |
| CFL | $\nu$ | with the factor $(2N+1)d$ of (21) |

# Reference list

The paper prints 78 references, numbered [1]–[78] and sorted alphabetically; no
DOIs are printed. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` including `gaburro-2024`.
Same-author same-year works take suffixes in printed order (Abgrall 2003 [7]/[9],
Gaburro 2021 [35]/[36]). [51] (Li, Duan & Tang, CMAME 399:115311) is the ingested
source `li-2022-c`, not `li-2022`. [31] prints no volume, [23] no pages, [69] no
volume, and [74] no venue. [8] and [20] are book chapters. No item is unparseable.

# Pages created or updated

Chunk 7 (2026-10-23), cited further in chunk 8 (2026-10-23). This source is cited on:

* [ADER schemes](/methods/ader-scheme.md)
* [Discontinuous Galerkin method](/methods/discontinuous-galerkin.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Isentropic vortex](/benchmarks/isentropic-vortex.md)
* [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md)
* [Mach 3 forward-facing step](/benchmarks/forward-facing-step.md)
* [MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Path-conservative schemes](/methods/path-conservative-scheme.md)
* [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Subcell finite-volume limiting for DG](/methods/subcell-finite-volume-limiting.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
* [Two-dimensional explosion and implosion problems](/benchmarks/explosion-and-implosion-problems.md)
* [Woodward–Colella interacting blast waves](/benchmarks/woodward-colella-blast-wave.md)
