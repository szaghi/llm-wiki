---
type: Source
title: "Potluri et al. (2023) — High order discontinuous Galerkin simulation of hypersonic shock-boundary layer interaction using subcell limiting approach"
description: "Laminar hypersonic shock/boundary-layer interactions with a split-form DGSEM and the Hennemann subcell finite-volume blending extended to Navier–Stokes with BR1: the scheme crashes at Mach 6 and above, cured by a hypersonic modification that limits the near-wall diffusive residual and imposes a wall blender in the initial transient."
resource: "doi:10.1016/j.jcp.2023.112117"
source_kind: paper
authors: [Potluri V.D., Puranik B.P., Bodi K.V.R.]
year: 2023
venue: "J. Comput. Phys. 485:112117"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Potluri_High_order_discontinuous_Galerkin_simulation_of_hypersonic_s.pdf"
tags: [dg, shock-capturing, hypersonic, entropy-stable, kinetic-energy-preserving]
timestamp: 2026-10-28T02:15:00Z
---

# Summary

Potluri et al. (2023) compute **laminar** hypersonic shock/boundary-layer
interactions with a high-order
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) in
their deal.II-based code PLENS; the paper has no turbulence model, LES or
DNS of turbulence, and bears on this bundle only through its numerics. The
base scheme is the [subcell finite-volume blending](/methods/subcell-finite-volume-shock-capturing.md)
of Hennemann et al.: a split-form DGSEM residual with the Chandrashekar
[entropy-conservative](/properties/entropy-conservation.md) and
[kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
two-point volume flux, blended by $\alpha$ with a first-order
finite-volume residual on the Gauss–Lobatto subcells, $\alpha$ coming from
a Persson–Peraire-type modal [indicator](/definitions/shock-sensor.md) of
$\rho p$. The authors extend it to the Navier–Stokes equations through
the BR1 viscous discretization and find that it crashes within a few time
steps at $M_\infty\ge6$: in the initial transient a near-wall velocity
overshoot drives the temperature to zero, and the shock indicator does not
flag these boundary-layer gradients. Their "hypersonic modification"
scales the near-wall diffusive residual by $(1-\alpha_d)$,
$\alpha_d=\alpha/\alpha_{\max}$, and imposes a high blender in the wall
cells for $t\le t_w$, ramped to zero by $2t_w$, with $t_w\sim5\Delta y_w^2/\nu_\infty$.
At a sharp leading edge $\alpha_d$ stays non-zero, and zeroing it crashes
the run.

Validation covers subsonic and supersonic flat plates, the Mach 2.15
laminar interaction of Degrez et al. at $N=2,3,4$ with equal degrees of
freedom, a Mach 6.06 compression corner (adiabatic and cooled walls), the
Mach 11.44 hollow cylinder/extended flare (HCEF Run 9), a Mach 14.1 ramp
and a Mach 8.1 cylinder. Two surface fluxes give nearly identical Mach 11
results, but on refined grids the Mach 11 and 14 separation bubbles
oscillate and the runs diverge, which the authors attribute to explicit
local time stepping; they recommend implicit time integration. The
alternatives reviewed in the introduction are SUPG and PDE-based
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md).

# Version read

Version of record (J. Comput. Phys. 485:112117, Elsevier typeset;
received 18 Aug 2022, online 6 Apr 2023), 21 pages, all read; the
equations of pp. 4–9 were checked visually. Page-1 title, authors and DOI
match the metadata, except that page 1 prints the third author as "Kowsik
V.R. Bodi" (initials K.V.R.) where the Crossref card gives "Bodi K.V.";
the page-1 form is used. Numbering on this page is that of this version.

# Key claims

The blending factor is the registry's $\alpha$ ($\alpha=0$ pure DG,
$\alpha=1$ pure first-order finite volume); the modal energy indicators,
threshold and logistic sharpness are written $\mathbb E_{\mathrm P}$, $\mathbb E_{\mathrm H}$,
$\mathbb T(N)$, $s_{\mathrm{log}}$ (page-local), the diffusive-residual
scaling and wall blender $\alpha_d$, $\alpha_w$, $\alpha_{\mathrm{imp}}$,
$t_w$ (page-local), and the residuals $R_{\mathrm{std}}$,
$R^{\mathrm{HO}}_{\mathrm{sf}}$, $R^{\mathrm{LO}}_{\mathrm{sc}}$ as printed.

1. The DGSEM-BR1 subcell-limited algorithm "crashes when applied directly to viscous hypersonic flows ($M_\infty\ge6$)", within $O(1)$ time steps at CFL $O(0.1)$ from a freestream start, and also from an inviscid solution or a zero-velocity start (§3.3, Fig. 2). **Shown**
2. Mechanism: as the wall velocity drops, the velocity profile overshoots the freestream value and the temperature undershoot steepens until $T$ reaches zero; at $M=6$, $Re_L=1.5\times10^5$, $N=2$, CFL 0.1 the run crashes at the fourth time step (§3.3, Fig. 2). **Shown**
3. Inviscid hypersonic simulations at the same conditions run without issue, so the diffusive residual is suspected; the advective wall flux (ghost state with reversed velocity) sets up a simple shear flow that contact-resolving fluxes preserve (§3.3). **Stated**
4. The hypersonic modification, $\mathcal J\dot U_i+(1-\alpha)R^{\mathrm{HO}}_{\mathrm{sf}}(F_a)_i+\alpha R^{\mathrm{LO}}(F_a)_i+(1-\alpha_d)R_{\mathrm{std}}(F_d)=0$ with $\alpha_d=\alpha/\alpha_{\max}$ near the wall and $0$ elsewhere, plus the imposed wall blender $\alpha'_w=\max\{\alpha_{\mathrm{imp}},\alpha_w\}$ ($\alpha_{\mathrm{imp}}\sim0.95\alpha_{\max}$ for $t\le t_w$, ramped linearly to 0 at $2t_w$), ensures "that the viscous residual is sufficiently limited in the initial transient" (§3.3). **Derived** (heuristic) and **Shown** (§§4.4–4.7)
5. $t_w\sim5\,\Delta y_w^2/\nu_\infty$, a few viscous time scales of the first cell, "gives reasonable results" (§3.3). **Stated**
6. At a sharp leading edge $\alpha_d$ remains non-zero because $\alpha$ is; "setting $\alpha_d=0$ at the leading edge, even in converged solutions, would immediately lead to a crash" (§3.3). **Shown** (from runs)
7. Shock detectors "cannot be expected to detect the high gradients which show-up in the initial transient of hypersonic boundary layers": $\alpha$ is non-zero initially but "diminishes very quickly" (§3.3). **Stated**
8. The indicator $\mathbb E_{\mathrm P}=m_N^2/\sum_{i=0}^Nm_i^2$ (Persson & Peraire) is used for $N\le2$; for $N>2$, $\mathbb E_{\mathrm P}$ suffices for supersonic cases and $\mathbb E_{\mathrm H}=\max\{m_N^2/\sum_{i=0}^Nm_i^2,\,m_{N-1}^2/\sum_{i=0}^{N-1}m_i^2\}$ (Hennemann et al.) is used for hypersonic ones, $m_j$ being the Legendre modes of $\rho p$ (§3.1.1, Eqs. 11–12). **Stated**
9. Blender: $\alpha=1/(1+\exp[-s_{\mathrm{log}}(\mathbb E/\mathbb T-1)])$ clipped to $[\alpha_{\min},\alpha_{\max}]$ and smoothed over neighbours, with $\mathbb T(N)=0.5\times10^{-1.8(N+1)^{0.25}}$, $s_{\mathrm{log}}=9.21024$, $\alpha_{\min}=10^{-3}$, $\alpha_{\max}=0.5$ (supersonic) and 1 (hypersonic) (§3.1.1). **Stated**
10. The hypersonic cases use conservative-variable gradients in BR1 "since they are observed to perform better"; the supersonic cases use entropy-variable gradients (§4). **Stated**
11. Subsonic flat plate ($M=0.5$, $N=4$): $C_f$ "matches very well" with Blasius and Young's compressible correlation for $x/L\ge0.1$ (§4.1, Fig. 3). **Shown**
12. Mach 2.15 interaction of Degrez et al., $N=2,3,4$ at about $150\times108$ degrees of freedom: residuals drop six orders by $t=4$ ms; wall pressures are "virtually indistinguishable" except a small pre-separation difference; $C_f$ differs more ($N=2$ lower before separation and less smooth in the separated region); results agree closely with Boin et al., and Degrez et al.'s numerical $C_f$ differs in trend because of its constant-viscosity assumption (§4.3, Figs. 6–7, Table 2). **Shown**
13. Mach 6.06 corner, adiabatic wall, $Re_L=1.5\times10^5$, four meshes: pressures "almost identical", in agreement with Carter's numerics, with some discrepancy in the separation location against experiment; residuals stall after one to three orders without visible oscillations (§4.4.1, Fig. 9). **Shown**
14. Mach 6.06 corner, cold wall ($T_w/T_{0\infty}=0.2$), $Re_L=1.5$, 3, $5\times10^5$: "The numerical results for all values of $Re_L$ under-predict the separation extent compared to experiment", possibly from experimental uncertainty, since Carter's results do too (§4.4.2, Fig. 10). **Shown** (attribution **Stated**)
15. Mach 11.44 HCEF Run 9, $136\times45$ cells, $N=2$: Chandrashekar and Rusanov–HLLC surface fluxes give "almost identical results"; separation is over-predicted, reattachment peaks are lower, following Gnoffo's numerics; the over-predicted cylinder heat transfer is attributed to insufficient near-wall resolution (§4.5, Fig. 12). **Shown**
16. Finer grids (Mach 11 at $180\times64$; Mach 14 Mesh 2; also HCEF Runs 8, 11, 14) give "large scale oscillations in the separation bubble" and divergence; lower CFL, higher Runge–Kutta order and the Rusanov flux "prove to be ineffective" (§§4.5–4.6, Fig. 13). **Shown**
17. "For hypersonic flows with very high Mach numbers ($M_\infty\gtrsim10$), explicit time integration with local time stepping may not be a suitable choice for steady state calculations with the current DGSEM algorithm" (§4.5, §5). **Stated** (not tested against an implicit scheme)
18. The ratio of the stable local time step at the leading edge to that in the freestream is $O(10^{-3})$ for the coarse Mach 11 case against $O(10^{-1})$ for the Mach 2 interaction (§5). **Shown**
19. Mach 14.1 ramp (Mesh 1, $131\times44$): the 2-D simulation over-predicts the separation extent, as does the finite-volume result of Rudy et al. on $201\times201$ (§4.6, Fig. 14). **Shown**
20. Mach 8.1 cylinder: surface pressure agrees well with Kitamura et al.; at equal degrees of freedom, $N=2$ heat transfer oscillates in the stagnation region while $N=1$ does not but overshoots the stagnation heat flux, so the "stagnation region heat flux prediction can depend significantly on the $N$, even if the DoF count is kept constant" (§4.7, Fig. 15, Table 3). **Shown**
21. The flux independence at Mach 11 is "consistent with" Ching et al. in suggesting that high-order solutions "may alleviate the sensitivity of heat transfer predictions" (§5). **Stated** (one case, two fluxes)
22. Local time-step limiters $\tau_n\lesssim1.1$ (neighbour) and $\tau_g\sim10$ (global) "yield stable computation" (§3.4). **Stated**

# Printed slips

- **§3.3, modified semi-discrete equation:** the low-order term is printed $\alpha R^{LO}_{sf}(F_a)_i$, while Eqs. (9)–(10) and §3.2 define $R^{LO}_{sc}$; the term $(1-\alpha_d)R_{std}(F_d)$ lacks the node index $i$.
- **§3.1.1, modal expansion:** printed $\epsilon(\xi)=\sum_{i=0}^{N}m_jP_j(\xi)$, summation index $i$ against summand index $j$.
- **$\alpha_{\max}$:** §3.1.1 states "$\alpha_{max}$ is set to 0.5 and 1 for supersonic and hypersonic cases respectively", while the Mach 6 hypersonic case (§4.4.1) is run with "$\alpha_{max}=0.5$" and $\alpha_{imposed}=0.475$.
- **Footnote 1 (p. 9):** "Re$_u$ denotes the unit Reynolds number $\rho U/L$". *(compiler check, not in the sources)* $\rho U/L$ has dimensions kg m$^{-3}$ s$^{-1}$, not m$^{-1}$, the unit in which $Re_u$ is quoted.
- **Name:** the text and figures write "Chandrashekhar" flux; ref. [33] prints "P. Chandrashekar".
- **Ref. [37]:** printed "J. Sci. Comput. 77 (2018) 154–200" with DOI "10.1016/j.jcp.2018.02.020", a prefix the same list uses for J. Comput. Phys. ([14], [26], [27]).
- **Ref. [46]:** Gottlieb & Shu printed as "Tech. rep. 221, Mathematics of Computation of the American Mathematical Society, Jan. 1998, pp. 73–85".

# Notation map

| Potluri et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $U$, $\mathcal U$ | $(\rho,\rho\boldsymbol u,E)$ | conservative state; $E$ printed per unit mass ($\rho E$ the energy per volume) |
| $F_{ai}$, $F_{di}$ | (advective, diffusive fluxes) | $F_d$ carries a leading minus sign |
| $\tau_{ij}$ | $\sigma_{ij}$ | laminar viscous stress; **collision** with the SGS stress $\tau_{ij}$ |
| $k$ | (thermal conductivity) | **collision** with the turbulent kinetic energy |
| $N$ | $N$ | polynomial degree, agree |
| $\xi_i$, $w_i$ | $\xi_i$, $w_i$ | Gauss–Lobatto nodes and weights on $[0,1]$ |
| $D_{ij}$, $M$, $S$, $B$ | $D_{ij}$, (mass, stiffness, boundary matrices) | agree |
| $J$ | $\mathcal J$ | mapping Jacobian ($b-a$ in 1-D) |
| $F^\#$, $F^*$ | $f^{\#}$, $f^*$ | two-point volume flux, interface numerical flux |
| $\{\{x\}\}$, $x^{ln}$ | $\{\!\{\phi\}\!\}$, $\phi^{\ln}$ | arithmetic and logarithmic means, agree |
| $\beta=\rho/2p$ | (inverse-temperature variable) | **collision** with the field-inversion $\beta(\boldsymbol x)$ |
| $\mathcal W$, $\mathcal Z$, $s=\ln p-\gamma\ln\rho$ | (entropy variables, their gradients, specific entropy) | page-local |
| $\alpha$ | $\alpha$ | DG/FV blending factor, agree; also blends the dissipation matrix of $F^*_{Ch}$ |
| $\alpha_f$ | $\alpha_{\mathrm{face}}$ | face blender of the Rusanov–HLLC flux; **collision** with the exponential-filter strength $\alpha_f$ |
| $\alpha_{min}$, $\alpha_{max}$, $\alpha_d$, $\alpha_w$, $\alpha_{imposed}$, $t_w$ | $\alpha_{\min}$, $\alpha_{\max}$, $\alpha_d$, $\alpha_w$, $\alpha_{\mathrm{imp}}$, $t_w$ | page-local |
| $\epsilon=\rho p$, $m_j$, $P_j$ | (indicator quantity, Legendre modes and polynomials) | $\epsilon$ is not the dissipation rate |
| $\mathbb E_P$, $\mathbb E_H$, $\mathbb T(N)$, $s$ | $\mathbb E_{\mathrm P}$, $\mathbb E_{\mathrm H}$, $\mathbb T(N)$, $s_{\mathrm{log}}$ | page-local; $s$ renamed against the entropy $s$ |
| $\tilde u_1$, $\tilde a$, $K$, $\lvert\Lambda\rvert$ | (Roe averages, eigenvector matrix, dissipation matrix) | **collision:** the tilde is a Roe average, not a Favre filter |
| $\Delta t_e$, $\tau_n$, $\tau_g$, $h_e$ | (element time step, limiter constants), $h$ | **collision:** $\tau_n$, $\tau_g$ are not stresses or time scales of the registry |
| $\Delta y_w$, $y_w$, $r_w$ | (wall-cell height) | page-local |
| $Re_u$, $Re_L$ | (unit Reynolds number per metre), $Re$ on plate length $L$ | |
| $c_f$, $T_{0\infty}$, $X_{sh}$ | $C_f$, (freestream stagnation temperature), (shock impingement distance) | |

# Reference list

71 printed references, numbered [1]–[71]. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [50]
(Wang et al. 2013, Int. J. Numer. Methods Fluids 72) is the ingested
[wang-2013](/sources/wang-2013.md). The two Fisher works of 2013 take
suffixes in printed order ([29] `fisher-2013`, [31] `fisher-2013-b`). No
printed duplicates. Partially printed or garbled items: [12] (chapter
without title), [20] and [21] (no volume or pages), [37] (venue against
DOI), [46] (venue format), [55] (bare SALOME URL).

# Pages created or updated

Chunk 12 (2026-10-28). This source is cited on:

- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
