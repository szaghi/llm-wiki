---
type: Source
title: "Nguyen et al. (2022) — Fully compressible multiphase model for computation of compressible fluid flows with large density ratio and the presence of shock waves"
description: "A fully conservative multiphase model with phasic mass equations and mixture momentum and energy under pressure–temperature equilibrium and stiffened-gas phases, solved by a second-order MUSCL–HLLC finite-volume scheme on primitive variables with a compressive limiter on the volume fractions."
resource: "doi:10.1016/j.compfluid.2022.105325"
source_kind: paper
authors: [Nguyen V.-T., Phan T.-H., Duy T.-N., Kim D.-H., Park W.-G.]
year: 2022
venue: "Comput. Fluids 237:105325"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Computers_amp_Fluids_Nguyen_Fully_compressible_multiphase_model_for_computation_of_compr.pdf"
tags: [multiphase, interface-capturing, finite-volume, riemann-solver, tvd]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper proposes a "fully compressible multiphase model": one mass equation per phase for
$\phi_k\rho_k$, one mixture momentum equation and one mixture total-energy equation, closed by
velocity, pressure and temperature equilibrium in every cell. This is the fully conservative
form of the [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
with a $p$–$T$-equilibrium closure. Each phase has a
[stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md) written in
$(p,T)$ form, so that $\rho_k=\rho_k(p,T)$ and the volume fractions follow from the partial
densities. No volume-fraction advection equation is solved: $\phi_2,\dots,\phi_N$ are entries of
the primitive vector $\mathsf W=(p,v,T,\phi_2,\dots,\phi_N)$. The authors set the model against
[five-equation models](/definitions/five-equation-model.md), quasi-conservative formulations and
the [ghost-fluid method](/methods/level-set-method.md), and list [THINC](/methods/thinc-reconstruction.md)
among interface-sharpening techniques.

The discretization is a cell-centred finite-volume Godunov scheme. The fluxes are
[Rusanov](/methods/lax-friedrichs-flux.md) or an [HLLC](/methods/hll-riemann-solvers.md) solver
extended to $N$ partial densities with Davis–Einfeldt wave speeds. Reconstruction is
[MUSCL](/methods/muscl-hancock.md) $\kappa_{\mathrm M}=1/3$ on primitive variables, with a
[TVD limiter](/definitions/total-variation-diminishing.md): the compressive "overbee" limiter of
Chiapolino et al. on the volume fractions and van Leer elsewhere. Time stepping is
[third-order TVD Runge–Kutta](/methods/ssp-runge-kutta.md), applied to $\mathsf W$ through
$[\partial u/\partial\mathsf W]^{-1}$. A Tait equation of state with an artificially reduced
bulk modulus relaxes the acoustic time-step limit at low Mach number.

The tests are the following. A water–air interface advected at uniform $p$, $v$, $T$ keeps
errors "on the order of $10^{-14}$" and an interface about three cells thick, a test of
[contact preservation](/properties/stationary-contact-preservation.md) for a moving contact.
The others are a gas–gas [shock tube](/benchmarks/sod-and-lax-shock-tubes.md), the
air–water [gas–liquid Riemann problem](/benchmarks/gas-liquid-riemann-problems.md), an
[underwater explosion](/benchmarks/underwater-explosion.md) near a free surface, the Mach 1.22
[shock–helium-bubble](/benchmarks/shock-bubble-interaction.md) interaction and the Martin–Moyce
dam break. Van Leer smears the interface, a growth of
[numerical dissipation](/definitions/numerical-dissipation.md) at low Mach number, while
superbee and overbee keep it sharp. No order-of-accuracy study and no measurement of the
conservation error are shown.

# Version read

Version of record (Elsevier typeset, Comput. Fluids 237, 105325), 24 pages, all read;
pp. 4, 8, 12, 13, 16, 17 and 22 checked visually. Page 1 matches Crossref (title, venue,
DOI); page 1 prints the hyphenated given names Van-Tu, Thanh-Hoang, Trong-Nguyen, Dong-Hyun
and Warn-Gyu, followed here for the initials. Equation, table and figure numbers are those of
this version.

# Key claims

Registry notation (see the notation map): volume fraction $\phi_k$, phase density $\rho_k$,
stiffened-gas constant $p_{\infty,k}$, primitive vector $\mathsf W$, limiter $\psi(r)$, HLL
speeds $s^\pm$.

1. The model has $N$ phasic mass equations, one mixture momentum and one mixture energy equation (Eqs. (2a)–(2e)); since each phasic mass equation is in conservation form, the scheme "is always mass conservative for each phase" (Abstract, §§1, 2.1). **Stated** (the Runge–Kutta stages of Eqs. (29)–(30) update $\mathsf W$, not $u$, and the paper does not say how $u$ is recovered; if as $u(\mathsf W^{n+1})$, the per-cell change is the flux difference plus an $O(\Delta t^2)$ remainder that does not telescope, because $u$ is nonlinear in $\mathsf W$, so the phasic masses are conserved only up to that remainder *(compiler check, not in the sources)*; no conservation error is measured)
2. The model assumes velocity, pressure and temperature equilibrium in mixture cells, $p_k=p$, $T_k=T$ (§2.1). **Stated**
3. The volume fractions need no separate advection equation: they are recovered as entries of $\mathsf W=(p,v,T,\phi_2,\dots,\phi_N)$ through system (7) (§§2.1, 2.3, Conclusion). **Stated**
4. The system is hyperbolic "because each phase is considered compressible" and "thermodynamically compatible" for any number of phases (§§1, 2.1). **Stated** (no proof; eigenvalues listed only)
5. The eigenvalues of the primitive-variable system are $v_1\pm c$ and $v_1$ (repeated), with the Wood mixture sound speed $1/(\rho c^2)=\sum_k\phi_k/(\rho_kc_k^2)$, called the "Wallis" sound speed (Eqs. (16)–(17)). **Stated**
6. The stiffened-gas law in $(p,T)$ form gives $e_k$, $\rho_k=(p+p_{\infty,k})/((\gamma_k-1)C_{v,k}T)$, $h_k=\gamma_kC_{v,k}T+q_k$, $s_k$, the Gibbs function, and $\partial\rho_k/\partial p$, $\partial\rho_k/\partial T$, $\partial h_k/\partial p=0$, $\partial h_k/\partial T=\gamma_kC_{v,k}$ (Eqs. (10)–(11)). **Derived** *(compiler check, not in the sources: (10a)–(10c) follow from (8a)–(8b), e.g. $e_k-q_k+p/\rho_k=\gamma_kC_{v,k}T$.)*
7. Tait law for the liquid with $\rho_0=1000$ kg/m$^3$, exponent 7.15, $c_l=1500$ m/s gives $B=\rho_0c_l^2/7.15$; at very low Mach number the bulk modulus is reset to $B=\rho_0\lvert U_{\mathrm{ref}}\rvert^2/(7.15\,M_{\mathrm{ref}}^2)$ with $M_{\mathrm{ref}}\in[0.1,0.3]$ (Eqs. (12)–(13)). **Stated**
8. The spatial discretization (18) "yields overall second-order accuracy in multiple dimensions"; the MUSCL extrapolation with $\kappa_{\mathrm M}=1/3$ is called "third-order" (§2.3). **Stated**
9. The overbee limiter of Chiapolino et al. gives interfaces about three cells thick; the paper applies it to the volume fractions and van Leer to all other primitive variables (§2.3). **Stated** (the combination is the paper's choice)
10. CFL 0.5 for water–air tests and 0.9 for gas–gas tests; a higher density ratio needs a smaller CFL (§2.3). **Stated**
11. 1D water–air interface advection: velocity, pressure and temperature errors at the interface "on the order of $10^{-14}$", an interface about three cells thick, and convergence to the exact solution on four grids (§3.1, Fig. 1). **Shown**
12. Initial temperature jumps $\Delta T=0,100,500$ K between gas and water (800 cells, $t^*=0.3$): the interface stays sharp (§3.1, Fig. 2). **Shown**
13. Low-Mach advection (Mach about 0.001, 1.5 m/s) with Rusanov on 100 cells: the van Leer interface grows beyond ten cells, superbee and overbee keep it within three, overbee slightly sharper (§3.1, Fig. 3). **Shown**
14. HLLC at Mach 0.001–1.0 on 100 cells: similar results across the Mach range, sharper than Rusanov; van Leer within five cells, superbee and overbee within three at constant thickness (§3.1, Fig. 4). **Shown**
15. Stiffened-gas and Tait laws give similar sharp interfaces (§3.1, Fig. 5). **Shown**
16. Iteration counts with the stiffened-gas law: 255 at 1500 m/s, 2012 at 150 m/s, 195,249 at 1.5 m/s; with Tait and stiffened gas at 1.5 m/s, 52,017 (§3.1, Table 1). **Shown**
17. Gas–gas shock tube on 100–800 cells at $t=0.2$: no spurious oscillation in pressure, density or velocity, and grid convergence (§3.2, Figs. 6–9). **Shown**
18. Air–water shock tube ($10^9$ Pa water against $10^5$ Pa air), 100 and 1000 cells, $t=240\,\mu$s: "very good agreement" with the reference solution (§3.2, Fig. 10). **Shown**
19. Underwater explosion near a free surface: van Leer smears the interface and may underpredict the bubble height; superbee and overbee keep a sharp interface and the ligament; grid convergence on $300^2$ and $600^2$; initial bubble temperature 2779.91 K, still about 2750 K at 0.2 ms (§3.3, Figs. 11–15). **Shown**
20. Shock–helium bubble ($M_s=1.22$): overbee gives a better interface thickness and smoothness than superbee and is used in all later runs (§3.4, Fig. 17). **Shown**
21. Shock–helium bubble: upstream, jet and downstream interface positions nearly identical on three grids (50, 100, 200 cells per diameter), in good agreement with the front-tracking/ghost-fluid results of Terashima & Tryggvason, and wave patterns agreeing with the Haas–Sturtevant shadowgraphs (§3.4, Figs. 18–19). **Shown**
22. Dam break (Martin–Moyce): an interface within about three cells and wavefront and water level close to experiment, whereas the five-equation model of Murrone & Guillard "without special treatments for the sharp interface" overestimates the water level and underestimates the wavefront (§3.5, Figs. 21–22). **Shown** (at "the same computational grid resolution"; the paper does not say whether the five-equation results were recomputed or taken from Murrone & Guillard's paper)
23. Five-equation models need a mixture equation of state whose temperature equilibrium is "questionable" and "can result in temperature spikes at material discontinuities" (§1). **Stated**
24. Quasi-conservative $1/(\gamma-1)$-advection approaches are unclear for three or more fluids because "the number of unknowns would be higher than the number of equations" (§1). **Stated**
25. The ghost-fluid method needs complex thermodynamic management and "is limited to two fluids" (§1). **Stated**

# Printed slips

- §2.1 (p. 4): "The mixture density: $=\sum_{i=1,N}\alpha_i\rho_i$" lacks the symbol $\rho$; the mixture enthalpy $h=\sum_{j=1,N}\alpha_i\rho_ih_i/\rho$ sums over $j$ with summand in $i$.
- Eqs. (3a)–(3b): the viscous stress is printed $\mu(\Delta\mathbf u+\Delta\mathbf u^T)$, with the Laplacian symbol where the velocity gradient is meant.
- Eq. (6): "$F_3=\dots$" is printed twice.
- Eq. (16): $\lambda_3=\dots=\lambda_N=u$ does not match the size $N+4$ of the 3D system; Eq. (19) takes $\max_{j=1,7}\lvert\lambda_j\rvert$, seven eigenvalues for no stated case.
- Eq. (23): $S_R=\max(u_R-c_R,\bar u+\bar c)$; by symmetry with $S_L=\min(u_L-c_L,\bar u-\bar c)$ the right estimate should use $u_R+c_R$, as the same Einfeldt estimate is printed by [Bai & Li (2022)](/sources/bai-2022.md), Eq. (15).
- Eq. (27): $r_R=\Delta W_{i-1/2}/\Delta W_{i+3/2}$ uses a difference outside the right state's stencil; by mirror symmetry with $r_L$ it should relate $\Delta W_{i+1/2}$ and $\Delta W_{i+3/2}$.
- Eq. (29): $L(W^n)=\{[\partial Q/\partial W]^{-1}\nabla\cdot F(W)\}^n$ lacks the minus sign.
- Eq. (31): $\Delta t=CFL/\sum_{j=1}^3\max\lvert\lambda_k\rvert$ has no mesh spacing and mismatched indices.
- §2.3 "time matching" (marching); §3.1 "HCLL" (HLLC); "Rosanov" (Rusanov).
- §3.1 (p. 19): the temperature jumps are printed "ΔT = x003D0 K, ΔT = x003D100 K, and ΔT = x003D500 K" (escape artefacts of "=").
- §3.2: the water pressure is $10^9$ Pa in the text, but the pressure axis of Fig. 10 is labelled "Pressure (MPa)" with maximum 1.
- Phase labels: §3.1 sets water as $\alpha_2=1$, while the §3.2 air–water tube sets the water side as "$\alpha_1=1$ and $\alpha_2=0$" and Fig. 10 plots a gas volume fraction 0 on that side.
- Table 3: the headers "π (Pa), γ, ρ, u, v, p" do not match the row values, which read in the order $(\gamma,\rho,u,v,p,\pi)$; the helium row has five values.
- §3.4: "at = 610 μs" (missing $t$); "Until approximately 50 ms … After 150 ms" for a time axis in μs (Fig. 18); "as shown in Fig. 14" for a figure of the explosion.
- §2.2: the Tait exponent is described as "the heat capacity ratio relative to the EOS".
- Appendix (A1): the $\alpha$ columns of the partial-mass rows print off-diagonal entries $\mp\rho_ku$ and the momentum rows print $\rho_2u^2$, $\rho_2uv$, $\rho_2uw$, whereas $\partial(\alpha_k\rho_ku)/\partial\alpha_j=\delta_{kj}\rho_ku$ and, with $\partial\rho/\partial\alpha_2=\rho_2-\rho_1$ as in (A2), the momentum entries should be $(\rho_2-\rho_1)u^2$ and so on. (A2) prints $\rho_Nu$ where $\partial(\alpha_N\rho_N)/\partial\alpha_N=\rho_N$. (A3) labels the entry at row 5, column 6 $\Gamma_{65}$, while the defined quantity is $\Gamma_{56}$. *(compiler check, not in the sources: derivatives of the printed $u(\mathsf W)$.)*
- References [17] and [44] are the same paper printed with years 2016 and 2015; [37] and [56] are the same paper, [37] without volume.

# Notation map

| Nguyen et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha_i$, $\rho_i$, $i=1,\dots,N$ | $\phi_k$, $\rho_k$ | volume fraction and phase density; **$\alpha$ collides with the weights $\alpha_k$** |
| $\mathbf u=(u,v,w)$ | $v=(v_1,v_2,v_3)$ | mixture velocity |
| $\rho H-p$ | $E$ | total energy per unit volume |
| $Q$, $F$ | $u$, $f^{(d)}$ | conserved vector $(\phi_1\rho_1,\rho v,E,\phi_2\rho_2,\dots)$ and flux |
| $W=(p,u,v,w,T,\alpha_2,\dots,\alpha_N)$ | $\mathsf W$ (page-local) | primitive vector of reconstruction and time update; **$W$ is the Lorentz factor in the registry** |
| $\gamma_i$, $\pi_i$, $C_{v,i}$, $q_i$, $q'_i$ | $\gamma_k$, $p_{\infty,k}$, $C_{v,k}$, $q_k$, $q'_k$ | stiffened-gas parameters; **$q$ is the weight exponent in the registry** |
| $c_i$, $c$ | $c_k$, $c$ | phasic and Wood mixture sound speed |
| $B$, $\rho_0$, $p_0$, $\gamma_l$ | kept | Tait parameters; $\gamma_l=7.15$ is the Tait exponent |
| $S_L$, $S_R$, $S^*$, $S^\pm$ | $s^-$, $s^+$, $s^*$ | HLLC speeds; **$S^+$ of Eq. (19) is the Rusanov speed $a$** |
| $W^L_{i+1/2}$, $W^R_{i+1/2}$ | $\mathsf W^-_{i+1/2}$, $\mathsf W^+_{i+1/2}$ | interface states |
| $\kappa$ | $\kappa_{\mathrm M}$ (page-local) | MUSCL parameter; **$\kappa$ is the kinetic energy in the registry** |
| $\phi(r)$, $r_L$, $r_R$ | $\psi(r_i)$, $r_i$ | limiter and slope ratios; **$\phi$ is the volume fraction in the registry** |
| $\beta$ | $\beta_{\mathrm{ob}}$ (page-local) | compressive parameter, 2 for superbee, $[1,2]$ for overbee; **collides with $\beta_k$** |
| $L(W)$ | $\mathcal L$ | semi-discrete operator, here in primitive variables |
| $t^*$ | kept | dimensionless time |

# Reference list

70 printed references in numbered Vancouver style ([1]–[70]), all parsed and merged complete
into the [bibliography](/bibliography.md) with `citedby` `nguyen-2022`. Two pairs are printed
duplicates of one work each, kept as separate entries per printed reference with a note:
[17]/[44] (printed years 2016 and 2015) and [37]/[56]. [57] prints
the first author "Bruce Stewart H" and is keyed as printed; [65] carries "Part IV" into the
title. No DOIs are printed.

# Pages created or updated

Chunk 3 (2026-10-22). This source is cited on:

* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Lax–Friedrichs (Rusanov) flux and flux splitting](/methods/lax-friedrichs-flux.md)
* [Level-set and ghost-fluid interface methods](/methods/level-set-method.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [SSP Runge–Kutta time stepping](/methods/ssp-runge-kutta.md)
* [Stationary contact preservation](/properties/stationary-contact-preservation.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
* [Total variation diminishing (TVD) and slope limiters](/definitions/total-variation-diminishing.md)
* [Underwater explosion](/benchmarks/underwater-explosion.md)
