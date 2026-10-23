---
type: Source
title: "Wakimura et al. (2024) — High-resolution boundary variation diminishing scheme for two-phase compressible flow with cavitation and evaporation"
description: "Applies the MUSCL-THINC-BVD and adaptive THINC-BVD reconstructions to the Pelanti–Shyue six-equation two-phase model with infinite-rate pressure, temperature and Gibbs relaxation, with symmetry-preserving implementation rules, so that liquid–vapour interfaces created by cavitation and evaporation stay sharp."
resource: "doi:10.1016/j.jcp.2024.113164"
source_kind: paper
authors: [Wakimura H., Li T., Shyue K.-M., Aoki T., Xiao F.]
year: 2024
venue: "J. Comput. Phys. 513:113164"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Wakimura_High-resolution_boundary_variation_diminishing_scheme_for_tw.pdf"
tags: [bvd, thinc, multiphase, cavitation, phase-change, finite-volume]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

In a diffuse-interface model, a bubble created by phase change starts smaller than a
cell. The [numerical dissipation](/definitions/numerical-dissipation.md) of a limited
MUSCL scheme then smears it until it is lost. The paper addresses this by applying
two existing second-order hybrid reconstructions, chosen by the
[boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
principle, to the mixture-energy-consistent six-equation model of Pelanti and Shyue
(see [five- and six-equation models](/definitions/five-equation-model.md)). The two
reconstructions are MUSCL-THINC-BVD and adaptive THINC-BVD, both by Deng et al.
(2018). Mechanical, thermal and chemical relaxation are taken at infinite rate, and
the phases follow the [stiffened-gas law](/definitions/stiffened-gas-equation-of-state.md)
with a caloric law and a saturation curve.

The scheme uses [operator splitting](/methods/operator-splitting.md). The hyperbolic
part is solved by the high-order wave-propagation method of Ketcheson, Parsani and
LeVeque, with an [HLLC](/methods/hll-riemann-solvers.md) solver and third-order SSP
Runge–Kutta. Pressure, pressure–temperature and pressure–temperature–Gibbs
relaxations follow as algebraic steps: closed-form quadratics, plus a Newton
iteration on the saturation curve. The candidates are [MUSCL](/methods/muscl-hancock.md)
with the van Leer limiter and [THINC](/methods/thinc-reconstruction.md) with two
steepnesses. They act on quasi-primitive variables, and the BVD switch is applied
only to the volume fraction and the partial densities. An appendix lists the rules of
operation ordering that keep [mirror symmetry](/properties/symmetry-preservation.md)
exact in floating point.

All evidence is numerical, on four tests:
- a water cavitation tube, a [double rarefaction](/benchmarks/double-rarefaction-problem.md);
- a water shock tube with a mainly-vapour mixture, both among the
  [gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md);
- a cavitating [Richtmyer–Meshkov](/benchmarks/richtmyer-meshkov-instability.md)
  problem, here with phase change;
- the piston-driven compression of a dodecane vapour bubble.

The BVD schemes resolve contacts in about 3–4 cells and give more developed
Richtmyer–Meshkov structures. In the bubble test, on a $200\times200$ grid, they
reproduce the new vapour bubbles created by phase change; according to the authors,
MUSCL needs $400\times400$ or $800\times800$ for this. The authors claim this as the
first clear capture of dynamically generated liquid–vapour interfaces.

# Version read

Version of record (Elsevier typeset; received 24 February 2024, revised 28 May 2024,
accepted 1 June 2024, online 7 June 2024), 24 pages, all read; pp. 3–5, 7–10, 21 and
23 were checked on the page images because text extraction loses the calligraphic
symbols. Title, five authors, venue and DOI on page 1 match Crossref. Numbering on
this page is that of the version of record.

# Key claims

Registry notation. Page-local: phase $k=1$ is the liquid and $k=2$ the gas or vapour
in every test; $\phi_k$, $\rho_k$, $Y_k$, $p_{\infty,k}$ as in the registry;
$e_{0,k}$, $s_{0,k}$ the reference energy and entropy of the stiffened-gas law;
$\mu_p$, $\theta_{\mathrm T}$, $\nu_g$ the pressure, thermal and chemical relaxation
rates; $\beta_{\mathrm T,s}=1.1$ and $\beta_{\mathrm T,l}=1.6$ the two THINC
steepnesses (see the Notation map).

1. The limiter dissipation of MUSCL smears discontinuities and blurs gas–liquid interfaces. To the authors' knowledge, interfaces created dynamically by phase change "have never been captured" because of it (§1, §3.1). **Stated**
2. The Pelanti–Shyue six-equation model is chosen because its frozen mixture sound speed $c^2=Y_1c_1^2+Y_2c_2^2$ (Eq. 8) is monotone in the volume fraction. Wood's speed in Kapila's five-equation model is not, which (citing earlier work) can make transport of the mixture zone unstable (§1, §2.3). **Stated**
3. Accuracy above third order "may introduce spurious oscillation error due to the reconstruction of primitive variables", so second-order BVD schemes are used (§1). **Stated**
4. For $f=au$, the numerical flux has the canonical form $\tfrac12\big(f(u^-)+f(u^+)\big)-\tfrac{\lvert a\rvert}2(u^+-u^-)$ (Eq. 26); minimizing the boundary variation $\lvert u^+-u^-\rvert$ reduces the numerical dissipation (§3.2.1). **Stated**
5. THINC with $\beta_{\mathrm T}\approx1.1$ behaves like MUSCL with the van Leer limiter; $\beta_{\mathrm T}=\ln3\approx1.0986$ is analytically second order; $\beta_{\mathrm T}$ between 1.6 and 2.0 resolves a discontinuity in about 3–4 cells (§3.2.3). **Stated** (cited)
6. THINC is used with $\beta_{\mathrm T,s}=1.1$ or $\beta_{\mathrm T,l}=1.6$, and only where $(\bar u_{i+1}-\bar u_i)(\bar u_i-\bar u_{i-1})>10^{-20}$; elsewhere the cell is piecewise constant (§3.2.3). **Stated**
7. MUSCL-THINC-BVD chooses between MUSCL and THINC($\beta_{\mathrm T,l}$), adaptive THINC-BVD between THINC($\beta_{\mathrm T,s}$) and THINC($\beta_{\mathrm T,l}$). The choice in cell $i$ minimizes the total boundary variation over the four combinations of neighbour candidates at its two faces (Eqs. 35–36) (§3.2.4). **Stated** (algorithm from earlier work)
8. The BVD switch acts only on $\phi_1$, $\phi_1\rho_1$, $\phi_2\rho_2$. Velocity and pressure always use MUSCL (MUSCL-THINC-BVD) or THINC($\beta_{\mathrm T,s}$) (adaptive THINC-BVD) (§3.2.4). **Stated**
9. Thermal and chemical relaxation act only where $\epsilon_I\le\phi_1\le1-\epsilon_I$, $\epsilon_I=10^{-4}$, and chemical relaxation only if $T_{\mathrm{liq}}>T_{\mathrm{sat}}(p)$ (evaporation, no condensation). The authors "found" that this does not affect the solution for small enough $\epsilon_I$ (§2.4, Eqs. 10–11). **Stated** (no evidence shown)
10. At infinite rates, the pressure and pressure–temperature equilibria reduce to quadratics in the relaxed pressure (Eqs. B.5–B.6, C.4–C.5). The chemical equilibrium reduces to a quadratic for the temperature as a function of pressure, plus one scalar equation on the saturation curve (D.7), solved by Newton–Raphson (Appendices B–D). **Derived**
11. The pressure-relaxed variables (B.8)–(B.10) are mixture-energy consistent in the sense of Pelanti and Shyue (App. B). **Stated**
12. Floating-point non-associativity breaks mirror symmetry in low-dissipation schemes. Symmetry is kept by the symmetric THINC formulas, by adding the total fluctuation last (A.3), and by summing the $v\mp c$ waves before the contact wave (A.4)–(A.5). No symmetry-preserving method for two-phase flow had been proposed before (App. A). **Stated** (no symmetry error measured)
13. CFL number $\nu=0.5$ in all tests (§4). **Stated**
14. Cavitation tube: MUSCL and adaptive THINC-BVD give similar solutions. MUSCL-THINC-BVD differs from MUSCL in mass fraction by at most $1.49\times10^{-6}$ ($\lvert v_0\rvert=2$ m/s) and $6.00\times10^{-5}$ ($\lvert v_0\rvert=500$ m/s). The results agree with those of Pelanti and Shyue (§4.1, Figs. 1–2). **Shown**
15. At $\lvert v_0\rvert=500$ m/s, THINC($\beta_{\mathrm T,l}$) is admitted in the BVD choice only where $\nabla\cdot v<0$, "to address the strong rarefaction waves" (§4.1). **Stated** (no run without it shown)
16. Water shock tube with a mainly-vapour mixture: the results with pressure and pressure–temperature relaxation agree well with the four-equation results of Chiapolino et al. The BVD schemes capture the contact at $x\approx0.6$ m in about 3–4 cells, MUSCL in more (§4.2, Fig. 3). **Shown**
17. Cavitating Richtmyer–Meshkov problem: phase change gives more vaporization near the left wall. The instability is more developed with the BVD schemes, which the authors attribute to lower dissipation. No scheme shows significant pressure oscillations. This is the first run of the test with phase change "to our knowledge" (§4.3, Figs. 4–5). **Shown**
18. Vapour-bubble compression without phase change: no significant difference between MUSCL and the BVD schemes (§4.4, Fig. 6). **Shown**
19. With phase change, MUSCL gives a low vapour mass fraction in the compressed bubble and very small new bubbles. The BVD schemes give a vapour mass fraction close to 1 and clearly resolved new liquid–vapour interfaces on $200\times200$. MUSCL needs $400\times400$ or $800\times800$ for comparable results (§4.4, Figs. 7–9). **Shown** (the refined MUSCL runs are not shown)
20. Mechanism: pressure peaks at $t=1$ ms (the piston shock, reflected and focused near $(0.7,0.5)$ m) and at $1.15$ ms (interacting shocks). Two low-pressure regions, symmetric about the high-pressure zone, fall below the saturation pressure and nucleate vapour bubbles between $1.2$ and $1.4$ ms (§4.4, Figs. 8–9). **Shown**
21. The BVD bubble-compression results are, to the authors' knowledge, the first to clearly capture liquid–vapour interfaces generated dynamically by phase change (§4.4, §5). **Stated**
22. The cancellation-free quadratic root (E.2) still loses digits near a double root (App. E). **Stated**

*(Compiler check, not in the sources.)* Writing the THINC face values (34) with
$\mathcal T=\tanh(\beta_{\mathrm T}/2)$ and $\mathcal A=\mathcal T_{2,i}/\mathcal T$
gives $f_{\mathrm m}+f_{\mathrm j}(\mathcal A+\mathcal T)/(1+\mathcal A\mathcal T)$,
the form on the [THINC](/methods/thinc-reconstruction.md) page; (34) follows from
$\tanh(\beta_{\mathrm T}d_i)=-\mathcal T_{2,i}/\mathcal T$ and the tanh addition
formula at $X=\pm\tfrac12$. The initial phase densities of the tests follow from
$\rho_k=(p+p_{\infty,k})/\big((\gamma_k-1)C_{v,k}T\big)$ and Tables 1–2: $1150.0$ and
$0.630$ kg/m³ at $354.728$ K (water), $458.34$ and $3.4075$ kg/m³ at $600$ K
(dodecane).

# Printed slips

- §4.1: "the gas density is $\rho_2=1150$ kg/m$^3$. Then, using isothermal condition, $T_1=T_2=354.728$ K and $\rho_2=0.63$ kg/m$^3$ are obtained." The first $\rho_2$ is the liquid density $\rho_1$: Eq. (46) lists $\rho_1=1150$, $\rho_2=0.63$, and phase 1 is the liquid.
- Eqs. (27)–(28) *(compiler check, not in the sources)*: the printed face values $\bar u_i+\tfrac12\Phi(r_L)(\bar u_{i+1}-\bar u_i)$ with $r_L=(\bar u_{i+1}-\bar u_i)/(\bar u_i-\bar u_{i-1})$, and $\bar u_i-\tfrac12\Phi(r_R)(\bar u_i-\bar u_{i-1})$ with $r_R=(\bar u_i-\bar u_{i-1})/(\bar u_{i+1}-\bar u_i)$, give with the van Leer limiter the increments $\Delta_+^2/(\Delta_-+\Delta_+)$ and $\Delta_-^2/(\Delta_-+\Delta_+)$ ($\Delta_\pm$ the forward and backward differences). These are not the two ends of one linear profile, and the slope is not van Leer's harmonic mean $2\Delta_+\Delta_-/(\Delta_++\Delta_-)$. Inverting each ratio, or multiplying by the other difference, recovers the harmonic-mean slope.
- Eq. (41) prints the HLLC contact speed with $(p_L-p_R)$ in the numerator, where the Batten form printed by [Wong et al. (2021)](/sources/wong-2021.md) has the opposite pressure difference. *(Compiler check, not in the sources:)* for zero velocities, equal densities and $S_L=-c$, $S_R=c$ the printed form gives $S_\star=-(p_L-p_R)/(2\rho c)$, a contact moving towards the high-pressure side, so the sign as printed is a slip (see [HLL-family solvers](/methods/hll-riemann-solvers.md)).
- Table 2 gives dodecane parameters "for 300-500 K", but the bubble test starts at 600 K.
- Ref. [21] (Liu, Osher & Chan, J. Comput. Phys. 115, 1994) prints the DOI "10.1002/fld.3889", a Wiley prefix. Ref. [26] (Harten, "High resolution schemes for hyperbolic conservation laws") prints "Int. J. Numer. Methods Fluids 23 (1983) 309–323" with a DOI of a 1996 IJNMF issue. Ref. [53] (Takagi et al., J. Comput. Phys. 452:110899) prints the year 2021; volume 452 is 2022.
- The abstract and §1 call both schemes "proposed", although they come from Deng et al. (2018); the contribution is their use with the six-equation phase-change model.

# Notation map

| Wakimura et al. 2024 | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha_k$ | $\phi_k$ | volume fraction; **collision** with the weights $\alpha_k$ |
| $\rho_k$, $\rho$, $Y_k$ | $\rho_k$, $\rho$, $Y_k$ | agree |
| $\boldsymbol u=(u,v,w)$ | $v=(v_1,v_2,v_3)$ | **collision**: registry $u$ is the state |
| $\boldsymbol q$, $\bar{\boldsymbol q}_i$ | $u$, $\bar u_i$ | state and cell average |
| $\boldsymbol q^{qp}=(\alpha_1,\alpha_1\rho_1,\alpha_2\rho_2,\boldsymbol u,p)$ | quasi-primitive variables (local) | reconstructed variables |
| $\boldsymbol q_{L,i+1/2}$, $\boldsymbol q_{R,i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $E_k$, $E$ | $E_k$, $E$ | total energy per unit volume |
| $\mathcal E_k$, $\mathcal E$ | $\rho_ke_k$, $\rho e$ | internal energy per unit volume; **collision** with the vortex strength $\mathcal E$ |
| $\gamma_k$, $\pi_k$, $C_{vk}$ | $\gamma_k$, $p_{\infty,k}$, $C_{v,k}$ | stiffened gas |
| $\eta_k$, $\eta'_k$ | $e_{0,k}$, $s_{0,k}$ (local) | reference energy and entropy, as on the stiffened-gas page; **collision** with the entropy $\eta$ |
| $s_k$, $g_k$, $h_k$, $T_k$ | specific entropy, Gibbs energy, enthalpy, temperature | registry $s$ is the ideal-gas entropy |
| $\mu$, $\theta$, $\nu$ | $\mu_p$, $\theta_{\mathrm T}$, $\nu_g$ (local) | relaxation rates, all $\to\infty$; **collision** with the affine $\mu$, the Zhang–Shu $\theta$ and the CFL number $\nu$ |
| $p_I$, $\rho_I$, $e_I$, $\kappa$ | interface pressure, density, energy, thermal coefficient (local) | $\kappa$ is not the kinetic energy |
| $\mathcal Q$, $\dot m$ | heat transfer, $\dot m$ | $\dot m$ agrees with the registry's interfacial mass flux |
| $\Sigma$ | non-conservative energy exchange (local) | |
| $A_s$, $B_s$, $C_s$, $D_s$ | saturation-curve coefficients (local) | |
| $\Phi(r)$, $r_L$, $r_R$ | $\psi(r_i)$ | van Leer limiter and slope ratios (see Printed slips) |
| $\beta$, $\beta_s$, $\beta_l$ | $\beta_{\mathrm T}$, $\beta_{\mathrm T,s}$, $\beta_{\mathrm T,l}$ | THINC steepness; **collision** with $\beta_k$ |
| $q_{a,i}$, $q_{d,i}$, $\mathcal T_1$, $\mathcal T_{2,i}/\mathcal T_1$ | $f_{\mathrm m}$, $f_{\mathrm j}$, $\mathcal T$, $\mathcal A$ | as on the THINC page |
| $d_i$, $X_i$ | jump centre, local coordinate | the registry's $x^c_i$ corresponds to $x_i+d_i\Delta x$ |
| $mTBV^\xi_i$ | minimum total boundary variation (local) | |
| $S_L$, $S_\star$, $S_R$, $\chi_K$ | $s^-$, $s^*$, $s^+$, star factor (local) | HLLC speeds |
| $\mathcal A^\pm\Delta\boldsymbol Q_{i+1/2}$, $\mathcal A\Delta\boldsymbol Q_i$, $\mathcal W^l$ | fluctuations and waves (local) | wave-propagation form |
| $\mathcal L^{\Delta t}_{hyp}$, $\mathcal L_p$, $\mathcal L_{pT}$, $\mathcal L_{pTg}$ | hyperbolic and relaxation operators (local) | **collision** with the semi-discrete operator $\mathcal L$ |
| superscripts $0$, $*$, $**$, $\circledast$ | before relaxation, after the mechanical, thermal, chemical step | |
| $c_k$, $c$ | phasic and frozen mixture sound speeds | |

# Reference list

The paper prints 65 references, numbered [1]–[65]. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` including `wakimura-2024`. Ref. [53]
is the ingested [Takagi et al. (2022)](/sources/takagi-2022.md) (printed year 2021,
same DOI). Same-author same-year works take suffixes in printed order (Deng 2018
[28]/[29], Tann 2020 [32]/[33], Petitpas 2009 [17]/[44]). Printed inconsistencies:
[21] carries a wrong-prefix DOI and [26] a venue and DOI that do not match the year
1983 (see Printed slips). [35] prints no article number, [62] no pages; [19] prints
"Math. Sb." No item is unparseable.

# Pages created or updated

Chunk 8 (2026-10-23). This source is cited on:

* [Boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
* [Double rarefaction (123) problem](/benchmarks/double-rarefaction-problem.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [MUSCL and MUSCL–Hancock schemes](/methods/muscl-hancock.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [Richtmyer–Meshkov instability](/benchmarks/richtmyer-meshkov-instability.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
