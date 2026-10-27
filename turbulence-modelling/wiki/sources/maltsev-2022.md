---
type: Source
title: "Maltsev et al. (2022) — High-order methods for diffuse-interface models in compressible multi-medium flows: A review"
description: "Review of diffuse-interface models for compressible multi-medium flows (Baer–Nunziato, five- and six-equation, gamma-based) and their high-order discretizations: unstructured WENO and CWENO, DG and reconstructed DG, lattice Boltzmann hybrids, interface sharpening (THINC, BVD, anti-diffusion); turbulence enters only through WENO spectral dissipation."
resource: "doi:10.1063/5.0077314"
source_kind: paper
authors: [Maltsev V., Skote M., Tsoutsanis P.]
year: 2022
venue: "Phys. Fluids 34:021301"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/0000_manual_no_journal_Unknown_10106350077314titleHigh-order.pdf"
tags: [review, shock-capturing, weno, dg, lattice-boltzmann, compressible]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Maltsev et al. (2022) review the numerical solution of diffuse-interface
models (DIM) for compressible multi-species and multi-medium flows (gas–gas,
gas–liquid, fluid–elastoplastic solid), in which the material interface is
not tracked but captured as a numerically smeared mixture zone carried by a
volume-fraction, mass-fraction or $\gamma$-based equation. Section II gives
the model hierarchy: the seven-equation Baer–Nunziato model, Kapila's and
Allaire's five-equation reductions, the $\gamma$-based four-equation model of
Abgrall and Shyue, the six-equation pressure-non-equilibrium model of Saurel
et al., the closing equations of state, and fluid–solid diffuse-interface
models. Section III reviews the discretizations: unstructured high-order
finite-volume reconstruction with MUSCL limiting and
[WENO](/methods/weno-scheme.md) on central and sectorial stencils, CWENO,
discontinuous Galerkin and reconstructed DG ($P_NP_M$), and
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) and hybrid lattice
Boltzmann/finite-volume schemes. Section IV collects the high-order DIM
implementations: HLLC fluxes adapted to the volume-fraction equation,
reduced-dissipation WENO variants and the MDCD-WENO hybrid of the
[low-dissipation low-dispersion](/methods/low-dissipation-low-dispersion-scheme.md)
family, interface sharpening (compression terms, anti-diffusion, THINC,
the Overbee limiter, MUSCL-THINC/QQ-BVD, CWENO), DG treatments of
non-conservative products with troubled-cell
[indicators](/definitions/shock-sensor.md) and
[a posteriori subcell limiting](/methods/subcell-finite-volume-shock-capturing.md),
and fluid–structure extensions. Two benchmarks are compiled from the
literature, the shock–helium-bubble interaction ($M_s=1.22$) and a shock in
molybdenum-encapsulated MORB. No new computation is presented.

The authors conclude that DIM have reached maturity only in the
finite-volume framework (MUSCL and WENO, unstructured and 3-D), that DG
applications are mostly limited to reduced five-equation models on
structured meshes, that reconstructed-DG and hybrid FV–LB applications
exist only in 1-D or at an early stage, that CWENO relieves the stencil cost
of high-order finite volumes, and that the field lacks convergence studies
and a common library of test problems. Turbulence enters only in passing:
the Jiang–Shu WENO dissipates turbulent fluctuations at the highest
resolvable wavenumbers ([numerical dissipation](/properties/numerical-dissipation.md)),
and a WENO code for implicit LES is cited. The paper is a compressible
multiphase-numerics review with a minimal footprint in this bundle.

# Version read

Version of record (Phys. Fluids 34:021301, submitted 1 November 2021,
accepted 11 January 2022, published online 3 February 2022, CC BY 4.0):
35 PDF pages, an AIP cover page plus journal pages 021301-1 to 021301-34, all
read; the equation pages were checked visually because the text layer
garbles matrices and Greek symbols. Page-1 title, authors, venue and DOI
match the metadata above; the archive filename carries no author or year.
No identity problem. Numbering on this page is that of this version.

# Key claims

The volume fraction of phase $k$ is written $\phi_k$ (page-local; the source
alternates $\phi$ and $\alpha$).

1. DIM split into phase-field methods (visco-capillary Cahn–Hilliard structure, needing fine interface resolution) and VOF-like extensions of the conservation laws with phase-mass and volume-fraction equations (Baer–Nunziato, Abgrall four-equation, Allaire and Kapila five-equation) (§I). **Stated**
2. The inherited drawback of DIM is an interface smearing that grows with simulation time and limits the time horizon; sharpening terms or THINC are the counter-measures (Abstract, §I). **Stated**
3. The Baer–Nunziato seven-equation model is unconditionally hyperbolic but contains non-conservative terms and so admits no Rankine–Hugoniot relations; for immiscible interfaces velocity and pressure equilibrium must be imposed (Saurel–Abgrall relaxation after wave propagation) (§II A). **Stated**
4. Kapila's five-equation model is a zero-order asymptotic reduction of Baer–Nunziato under stiff mechanical relaxation; its non-conservative volume-fraction source makes it converge slowly or not at all to the exact solution, and its Wood sound speed (Eq. 10) is non-monotonic and can fall below both pure-fluid sound speeds (§II B, Eqs. 8–10). **Stated**
5. Mixture-rule ($\gamma$) models must satisfy single-fluid degeneracy, hyperbolicity, conservation of total mass and energy, and numerical stability at interfaces; averaging $\gamma$ itself (Eq. 11) gives interface oscillations, averaging $1/(\gamma-1)$ (Abgrall) does not (§II C, Eqs. 11–12). **Stated**
6. Under the isobaric closure Allaire's five-equation model (Eq. 13) captures interfaces without spurious oscillations (the "consistency condition") and recovers the separate phase properties through two mass balances (§II C). **Stated**
7. The six-equation model of Saurel et al. keeps pressure non-equilibrium, has the monotonic mixture sound speed $c^2=Y_1c_1^2+Y_2c_2^2$ (Eq. 17), and with the added mixture-energy equation (Eq. 15) is overdetermined, to be read as a solution procedure for the five-equation model rather than a new physical model (§II D). **Stated**
8. The simplest five-equation models are very efficient and reach shock–bubble accuracy comparable to non-equilibrium models, but lack the compressibility source of Eq. (8) and are unsuitable for bubble collapse and dynamic interface appearance; the Kapila source is numerically unstable under strong shocks; the seven-equation model has up to seven wave speeds and needs intricate Riemann solvers, so most effort goes into reduced models (§II, "Interim considerations"). **Stated**
9. In 3-D the number of DG basis polynomials grows steeply with order; the authors state ten for a second-order and 20 for a third-order reconstruction (§III B, Eq. 61 and text). **Stated**
10. The $P_NP_M$ reconstructed-DG family unifies finite volumes ($N=0$) and DG ($M=N$); with $M>N$ it reaches accurate solutions at minor extra cost; the Taylor-basis RDG($P_1P_2$) is cheaper than Dumbser's $L_2$-projection recovery, and the hybrid least-squares variant (HLSr) restores the order lost by centroid matching; Fig. 1 (adapted from Cheng et al., subsonic cylinder) prints orders 2.48 for DG($P_1$), 3.32, 3.82 and 3.87 for the $P_1P_2$ variants (GG, LSr, HLSr) and 3.63 for DG($P_2$) (§I, §III C, Eqs. 64–70, Fig. 1). **Shown** (cited figure)
11. MUSCL limiting is robust and compact but parameter-dependent and accuracy-degrading; WENO preserves accuracy and is less parameter-sensitive but needs large stencils that may hurt efficiency and robustness; the Barth–Jespersen limiter is limited to second order and non-differentiable (§III D). **Stated**
12. WENO on unstructured mixed-element meshes uses one central and several sectorial stencils with central linear weight $10^2<d_0<10^5$, sectorial $d_k=1$, exponent 4 and $\varepsilon=10^{-6}$ in $a_k=d_k/(\varepsilon+\mathrm{IS}_k)^4$; the smoothness indicator depends only on the reconstruction basis and can be computed once per element (§III D, Eqs. 76–79). **Stated**
13. The classical lattice Boltzmann method is limited to low Mach number (expansion of the Maxwellian); fixed velocity stencils restrict the attainable $\gamma$ and $Pr$, and compressible extensions need more discrete velocities, counterterms, double distributions or multiple relaxation times (§III E). **Stated**
14. For high-order finite-volume DIM the interface advection equation must be written in non-conservative form to avoid interface oscillations (Abgrall); reconstruction is done on primitive variables projected in characteristic space; recovering primitive averages from conservative averages introduces a second-order error that Coralic and Colonius remove with two-point Gaussian quadrature, recovering formal fifth order (§IV). **Stated**
15. HLLC is preferred to the exact Riemann solver (cost) and to Roe (positivity at very low pressure and density) but suffers from the carbuncle in strong shocks; a contact-restoring HLL with a THINC-like jump and BVD selection keeps HLL robustness (§IV). **Stated**
16. The Jiang–Shu WENO dissipates turbulent fluctuations at the higher resolvable wavenumbers and degrades spectral properties through its upwind-biased nonlinear reconstruction (citing Johnsen et al. 2010 and Pirozzoli 2006) (§IV). **Stated**
17. On the multi-species advection test of Wong and Lele at 128 cells, MUSCL reaches order 1.666, WENO-JS 4.743, WENO-SYMBO 4.339 and MDCD-WENO 4.619, with errors $1.153\times10^{-3}$, $3.223\times10^{-8}$, $5.541\times10^{-8}$ and $2.814\times10^{-8}$ (§IV, Table I, adapted from Wang et al. 2020). **Shown** (cited table)
18. MDCD-WENO is more efficient than WENO-JS when 10–20 cells per wavelength resolve the highest wavenumber (§IV, citing Ref. 166). **Stated**
19. Contact discontinuities, unlike shocks, have parallel characteristics that do not counteract numerical diffusion, so interface smearing is unavoidable without corrections to the governing equations (§IV A). **Stated**
20. The sharpening terms of Shukla et al. are inconsistent with the mixture thermodynamic models and can accumulate error far from the interface (§IV A). **Stated**
21. Per Tiwari et al., all compared sharpening techniques improve the collapsing-bubble surface; the techniques of Refs. 38 and 39 halve the diffusion of baseline five-equation models, which in 3-D would otherwise need an eight times finer mesh; the So et al. anti-diffusion has no grid-scale parameter, so its interface thickness evolves with the flow (§IV A). **Stated** (cited)
22. Fifth-order WENO represents the collapsing-bubble radius better than second-order MUSCL-minmod on Cartesian meshes, because mesh directionality affects lower-order methods more (§IV A, Fig. 2, from Tiwari et al.). **Shown** (cited figure)
23. Schmidmayer et al. found that THINC with time integrators other than the wave-propagation algorithm gives a 44% larger error at low pressure ratios and less spherical bubbles; THINC behaves better with lower-order MUSCL, and coupling it with WENO above third order is generally avoided to prevent over-sharpening (§IV A, Fig. 3). **Shown** (cited)
24. The Overbee limiter of Chiapolino et al. (Eqs. 115–116) combines the second-order TVD region of Superbee with the upper boundary of the first-order TVD region; with $b=2$ it keeps the interface within $3\pm1$ cells on unstructured grids (§IV B). **Stated** (cited)
25. MUSCL-THINC/QQ-BVD with only second-order candidates produced less error than third-order WENO (§IV B, citing Ref. 177). **Stated**
26. CWENO on mixed-element unstructured meshes keeps the accuracy of WENO (Table II orders up to 6.11 at sixth order) at lower wall-clock time; the authors state "an approximately 80% saving in computational time is found for the higher accuracy order" (§IV B, Table II). **Shown** (Table II; see Printed slips for the 80% figure)
27. For DG with non-conservative products, weak solutions in the classical sense do not exist; the Dal Maso–LeFloch–Murat path-conservative theory gives a weak formulation (Rhebergen et al.; Franquet and Perrier for Baer–Nunziato), whose limiting by truncation of higher-order terms lacks a proper treatment of oscillations (§IV C, Eqs. 124–126). **Stated**
28. Gryngarten and Menon found their LDG DIM solver more accurate when reconstructing primitive rather than conservative variables (§IV C). **Stated** (cited)
29. RDG($P_1P_2$) with zero slopes of bulk velocity, partial densities and partial pressures in the mixture region gives, on 1-D Gaussian volume-fraction advection, convergence slopes FV1 0.881, FV2 1.704, DG($P_1$) 2.027 and rDG($P_1P_2$) 2.862 (§IV D, Fig. 5, from Pandare et al.). **Shown** (cited)
30. DIM maturity is reached only in finite volumes (MUSCL/WENO, unstructured, 3-D); DG applications are limited mostly to reduced five-equation models on structured meshes; rDG DIM applications exist only in 1-D; hybrid FV–LB DIM are at an early stage; most high-order DIM works lack convergence studies and quantitative multi-dimensional interface-diffusion analysis; a common library of test problems is needed (§V). **Stated**

# Printed slips

- **Eq. (27) against Eq. (8):** the volume-fraction source of the
  Favrie–Gavrilyuk model is printed
  $\phi_s\phi_g\frac{\rho_s\phi_s^2-\rho_g\phi_g^2}{\phi_s\rho_sa_g^2+\phi_s\rho_ga_g^2}\frac{\partial u}{\partial x}$:
  the numerator carries $\phi^2$ where the paper's own Kapila term (Eq. 8)
  carries the squared sound speeds, and the denominator repeats $\phi_s$
  and $a_g$.
- **Eq. (98):** the right wave-speed estimate is printed
  $s^R=\min(\bar u+\bar c,u_L+c_L)$, built on the left state, while the left
  estimate is $s^L=\min(\bar u-\bar c,u_L-c_L)$; Eq. (96) prints the mixed
  "$\rho_Ru_r(s_r-u_R)$".
- **Eq. (140):** the first bracket is multiplied by $\frac{1}{\gamma-1}$, the
  second differentiates $\frac{1}{1-\gamma}$, in the expansion of the
  derivative of $\rho\gamma/(\gamma-1)$.
- **Table II:** both order columns carry the same label; the one next to
  $e_{L^2}$ repeats the label of the column next to $e_{L^1}$.
- **"approximately 80% saving" (§IV B):** *(compiler check, not in the
  sources)* from the wall-clock times of Table II, the saving
  $1-t_{\mathrm{CWENO}}/t_{\mathrm{WENO}}$ at sixth order is 39.9% (10 edges
  per side, 2.227 against 3.704), 45.3% (20 edges, 16.729 against 30.602),
  42.2% (40 edges, 175.908 against 304.109) and 38.2% (80 edges, 1493.933
  against 2417.527), and 35.6% at fifth order with 80 edges (1119.209
  against 1738.832); no entry of the table reaches 80%.
- **Eq. (48) against Eq. (61):** *(compiler check, not in the sources)* the
  number of non-constant basis functions of a degree-$r$ reconstruction in
  three variables is printed $K=\frac12(r+1)(r+2)(r+3)-1$, which gives 11
  for $r=1$; the paper's own count of polynomials of degree $k$ in $n=3$
  dimensions, $d=\binom{n+k}{k}$ (Eq. 61), gives $d-1=3$.
- **Eq. (86) against Eq. (88):** *(compiler check, not in the sources)* the
  Maxwellian-type equilibria are printed
  $\rho(2\pi RT)^{-D/2}\exp\big((c-u)^2/(2RT)\big)$, with a positive
  exponent that makes the distribution non-normalizable; the Hermite form
  of Eq. (88) carries $e^{-c^2/2}$.
- **Eq. (69):** the mixed second derivative is printed
  $U_{xy}=\frac{\partial^2U}{\partial y}\big|_c\Delta x\Delta y$, with a
  single differentiation variable (Eq. 62 uses the mixed derivative).
- **Eq. (92):** $f_k^{eq}=\rho[A_k+B_k(u_xc_{xk}+u_yc_{yk})^2+C_k(u_xc_{xk}+u_yc_{yk})^2]$
  prints two identical squared terms.
- **Eqs. (31) and (33):** the reactant equation is printed
  $\partial_t(\phi_2\rho_2\lambda)+\mathrm{div}(\phi_2\rho_2u\lambda)=\phi_2\rho_2K$
  and then $\partial_t(\rho\lambda)+\mathrm{div}(\rho_2u\lambda)=K$, with
  $\rho$ in the time derivative and $\rho_2$ in the flux.
- **Eq. (3) against Eqs. (4), (6), (14):** $\mu_c$ divides the pressure
  difference in Eq. (3) ("dynamic compaction viscosity") and multiplies it
  in the others (a relaxation rate).
- **Eq. (126)** prints "$V^R$" in the path derivative for $U^R$; **Eqs.
  (145)–(146)** print "$\min(h_h,h_{j+1})$" and "$\min(h_{j-1,h_j)})$";
  **Eq. (106)** uses $\kappa$, $\Gamma_k$, $\Pi_k$ without defining them;
  **Eqs. (105), (109)** mix $\alpha$ and $\phi$ for the volume fraction.
- **Eqs. (21)–(22) against Eq. (151):** the bulk sound speed is $a_0$ in
  Eq. (21) and $c_0$ in the test-case parameters; Eq. (21) has $\Gamma_0$,
  Eq. (22) $\gamma_0$, without saying whether they are equal.
- **Eqs. (114), (116) against the text:** the limiter parameter is printed
  $\beta$ in the equations and $b$ in the text; after Eq. (114) $b=1$, 2 give
  minmod and superbee, after Eq. (116) "when $b=1$ this corresponds to the
  Superbee limiter".
- **Citation slips:** the Fig. 6 caption and text attribute the CWENO
  helium-bubble results to "Ref. 200" (Tsoutsanis & Dumbser, Comput. Fluids
  225) while naming the CWENO paper in J. Sci. Comput. 89, which is Ref.
  178; the Fig. 1 caption cites Cheng et al. in Comput. Fluids 139 (2016),
  while Ref. 127 is AIAA paper 2016-1330; Fig. 8(a) dates Cheng et al., J.
  Comput. Phys. 428, to 2020 and Ref. 177 to 2021; Figs. 11–12 date Luo et
  al., J. Sci. Comput. 87, to 2020 and Ref. 190 to 2021; the Fig. 11 caption
  prints "Copyright 2104".
- **Typos:** "noble-able-stiffened-gas" (Noble–Abel, as in the title of
  Ref. 93), "left Cachy–Green", "Bathnagar" (text and Ref. 146),
  "Broiulette" and "Richtmeyer" (Ref. 208), "the mixture sound of speed".

# Notation map

| Maltsev et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\phi_k$, also $\alpha_k$ | $\phi_k$ (page-local volume fraction) | **collision:** the registry $\alpha$ is the DG/finite-volume blending factor |
| $\rho_k$, $u_k$, $P_k$ ($p_k$), $e_k$, $E_k$ | $\rho$, $u$, $p$ per phase | $E_k$ is a specific total energy here, not per unit volume |
| $Y_k$ | (page-local mass fraction) | |
| $a_k$, $c_k$, $c$ | (page-local phase and mixture sound speeds) | $c$ also the LB particle velocity (Eq. 80) |
| $\mu_c$ | (page-local compaction viscosity or relaxation rate) | **collision** with $\mu$, the molecular viscosity |
| $\lambda$ | (drag coefficient; reactant fraction; CWENO weights $\lambda_s$; basis $\lambda_k$) | **collision** with the Taylor microscale $\lambda$ |
| $\gamma$ | $\gamma$ | ratio of specific heats; $\gamma_l$, $\pi_\infty$ stiffened-gas parameters |
| $U$, $F$, $H$, $S$ | (conserved vector, flux, non-conservative vector, source) | Eq. (1) |
| $k$ (DG degree), $d$, $n$ | $N$, $(N+n)!/(N!\,n!)$, space dimension | $N$ and $M$ of $P_NP_M$ agree with the registry $N$ |
| $r$ | (page-local reconstruction degree of finite volumes) | |
| $\omega_\alpha$ | $w_i$ | quadrature weights |
| $d_m$, $\gamma_m$, $\omega_m$, $IS_m$, $p$, $\varepsilon$ | $d_k$, $a_k$, $\mathsf w_k$, $\mathrm{IS}_k$, exponent, regularizer | registry §11 WENO symbols; **collision:** the source's $\gamma_m$ and $\omega_m$ are not $\gamma$ and $\omega$ |
| $\Theta_i$ | (slope-limiter value) | |
| $\beta$ (Eq. 110) | $\beta_{\mathrm{TH}}$ | THINC steepness; $\beta$ is also a multi-index in Eq. (79) and the limiter parameter in Eq. (114) |
| $b$ | (Overbee/superbee limiter parameter) | |
| $f$, $f^{eq}$, $\tau$, $c_i$ | $f_q$, $f_q^{eq}$, $\tau_{\mathrm{LB}}$, $\boldsymbol c_q$ | lattice Boltzmann; $\tau$ is also a pseudo-time and a relaxation time (Eqs. 103, 137) |
| $s^L$, $s^R$, $s^*$, $s^\pm$ | (HLLC wave speeds) | |
| $\mathscr U_0$, $\varepsilon_h$, $\boldsymbol n$ | (compression velocity, interface-thickness length, interface normal) | sharpening terms |
| $|V_i|$, $|f|$, $N_f$, $N_{qp}$ | (cell volume, face area, face count, quadrature points) | |
| $At$, $M_s$ | (Atwood number, shock Mach number) | $A_\sigma$ of the registry is a pre-shock average, not this one |

# Reference list

210 printed references, numbered (AIP superscript style), no DOIs printed.
The list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. Same-author same-year works take suffixes in printed
order (Saurel 1999 [15], [17]; Fedkiw 1999 [19], [24]; Luo 2010 [121],
[126]; Tsoutsanis 2018 [81], [132]; Dumbser 2016 [136], [195]; Wallis 2021
[109], [113]; Tsoutsanis 2021 [178], [200]; Sambasivan 2009 [204], [205]).
Ref. [179] (Li et al., Phys. Fluids 33:056104, 2021) is not the ingested
gene-expression-programming paper of Li et al. (2021) and is keyed `li-2021-i`. Names are keyed as printed ("Bathnagar" [146], "Broiulette"
[208], "O. L. Metayer" [the same person as Le Métayer, Ref. 93]); Ref. [54]
prints a title ending "II. PDF", kept as printed, as are the author
names of Ref. [128]. AIAA papers and the ICASE report are
entered as reports. No printed duplicates, no unparseable item.

# Pages created or updated

Chunk 9 (2026-10-27). This source is cited on:

- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [High-order gas-kinetic schemes for turbulence simulation](/methods/high-order-gas-kinetic-scheme.md)
- [Lattice Boltzmann methods for turbulent flow](/methods/lattice-boltzmann-method.md)
- [Low-dissipation low-dispersion schemes with shock sensor](/methods/low-dissipation-low-dispersion-scheme.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
