---
type: Source
title: "Zhang et al. (2024) — A hybrid WENO5IS-THINC reconstruction scheme for compressible multiphase flows"
description: "Finite-volume five-equation solver with viscosity and surface tension whose reconstruction is incremental-stencil WENO5IS away from interfaces and a simplified, mirror-flipped THINC for volume fraction and partial densities in interface cells, followed by a positivity- and boundedness-preserving interpolation limiter; tested on gas–liquid shocks, droplets and bubble collapse."
resource: "doi:10.1016/j.jcp.2023.112672"
source_kind: paper
authors: [Zhang W., Fleischmann N., Adami S., Adams N.A.]
year: 2024
venue: "J. Comput. Phys. 498:112672"
local_file: "/home/stefano/papers/mosaic/weno-teno/2024_Crossref_Journal_of_Computational_Physics_Zhang_A_hybrid_WENO5IS-THINC_reconstruction_scheme_for_compressibl.pdf"
tags: [multiphase, interface-capturing, thinc, finite-volume, bound-preserving]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

Zhang et al. (2024a) build a Godunov-type finite-volume interface-capturing scheme for the
quasi-conservative [five-equation model](/definitions/five-equation-model.md) of two compressible
fluids with [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md) closures, molecular
viscosity and a CSF-type surface tension. Primitive variables are reconstructed by the fifth-order
[incremental-stencil WENO](/methods/incremental-stencil-weno.md) (WENO5IS) of Wang, Xiang & Hu.
In cells flagged as interfacial (volume fraction strictly inside $(10^{-3},1-10^{-3})$ and locally
monotone), only the volume fraction and the two partial densities are replaced by
[THINC](/methods/thinc-reconstruction.md) values; velocity and pressure keep the WENO5IS values. This
makes the scheme a [hybrid](/methods/hybrid-weno.md) polynomial/THINC reconstruction.

The THINC step is simplified. The jump centre comes in closed form from the cell average, the partial
densities scale with the THINC volume fraction, and left and right values are obtained by mirror
flipping. The gradient sign is then not needed, which avoids the floating-point asymmetry
($e^x\neq1/e^{-x}$ exactly) that breaks [symmetry](/properties/symmetry-preservation.md) in earlier
THINC implementations. The positivity- and boundedness-preserving interpolation limiter of
[Wong et al. (2021)](/sources/wong-2021.md) follows (see the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md) page), then HLLC
fluxes with a surface-tension star state and SSP Runge–Kutta 3 at CFL 0.5. All in the code ALPACA.

The evidence is numerical: [material-interface advection](/benchmarks/material-interface-advection.md),
[gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md) up to 1 GPa,
[shock–water-column](/benchmarks/shock-water-column.md) interaction at Mach 2.4, 6 and 10, a Mach 10
(about 100 GPa) [shock-induced bubble collapse](/benchmarks/shock-bubble-interaction.md), the Laplace
law and the [oscillating droplet](/benchmarks/oscillating-droplet.md). The comparisons are with
WENO5IS alone and MUSCL-THINC. WENO5IS-THINC keeps the interface width, resolves waves and
small vortices better than MUSCL-THINC, and keeps the flow symmetric where MUSCL-THINC loses symmetry
at high resolution. As base scheme WENO5IS triggers the limiter least of WENO-JS5, TENO5 and WENO5IS.
With surface tension the THINC steepness must be small ($\beta_{\mathrm T}=1.3$).

# Version read

Version of record (Elsevier typeset; received 7 August 2023, accepted 22 November 2023, online
28 November 2023, issue 2024), 31 pages, all read; text extraction clean, with Eqs. (8), (34), (B.2)
and Algorithm 1 partly garbled by the layout and reconstructed. Page 1 matches Crossref (title,
four authors, venue, DOI). Numbering cited here is that of this version.

# Key claims

Registry notation: the source's $\alpha_1$, $\rho_k\alpha_k$, $P_\infty$, $\mathbf u$ are $\phi_1$,
$\phi_k\rho_k$, $p_\infty$, $v$; its THINC $\beta$ is $\beta_{\mathrm T}$; its surface tension
$\sigma$ and curvature $\kappa$ are $\sigma_{\mathrm{st}}$ and $\kappa_{\mathrm c}$; its WENO5IS
$\eta_k$ is $\alpha_k$ and its reference indicator $\tau_5$ is $\tau^{\mathrm{ref}}_5$; its
$\mathbf q^L$, $\mathbf q^R$ are $u^-$, $u^+$.

1. On the five-equation model the Wood mixture sound speed (Eq. 17) is non-monotone in the volume fraction, which can spoil acoustics across a diffuse interface and cause failure; the six-equation formula (Eq. 18) works but is "not as efficient"; the frozen form $c=\sqrt{\gamma(p+p_\infty)/\rho}$ (Eq. 16) is used throughout (§2.3, Fig. 1). **Stated**
2. The THINC centre that preserves the cell average of $\tfrac12[1+\tanh(\beta_{\mathrm T}(X+c_i))]$ on $X\in[0,1]$ is $c_i=\frac1{2\beta_{\mathrm T}}\ln\frac{e^{2\beta_{\mathrm T}\phi_{1,i}}-1}{e^{2\beta_{\mathrm T}}-e^{2\beta_{\mathrm T}\phi_{1,i}}}$ (§3.3, Eqs. 35–38). **Derived**
3. The four left and right face values for positive and negative gradients (Eqs. 39–42) collapse into the single formula (43) with two constants and the gradient sign (§3.3). **Derived**
4. The THINC symmetry relation (44) holds in exact arithmetic but not in floating point because $e^x=1/e^{-x}$ is not exact, so earlier THINC implementations can break symmetry; mirror flipping of left and right values removes the gradient sign from the centre (§3.3). **Stated** (shown in §4.7, Fig. 13)
5. In interface cells the phase densities are held constant, so $\phi_1\rho_1\propto\phi_1$ and $\phi_2\rho_2\propto1-\phi_1$ (Eq. 45); velocity and pressure are not THINC-reconstructed "since pressure and velocity should be continuous at the interface"; the approach is claimed more concise and efficient than those of Shyue & Xiao and Garrick et al. (§3.3). **Stated**
6. A cell is interfacial when $\varepsilon_{\mathrm{THINC}}<\phi_{1,i}<1-\varepsilon_{\mathrm{THINC}}$ and $(\phi_{1,i+1}-\phi_{1,i})(\phi_{1,i}-\phi_{1,i-1})>0$, $\varepsilon_{\mathrm{THINC}}=10^{-3}$ (Eq. 46). **Stated**
7. The hybrid face state is $\theta\big[(1-\delta^{\mathrm T})u^{\mathrm{WENO5IS}}+\delta^{\mathrm T}u^{\mathrm{THINC}}\big]+(1-\theta)u^{\text{first order}}$, with $\delta^{\mathrm T}=1$ in interface cells and $\theta$ the parameter of the Wong et al. limiter (Eq. 49, Algorithm 1). **Stated**
8. Limiter thresholds $10^{-11}$ (partial densities, volume fractions) and $10^{-9}$ ($\rho c^2$), with $10^{-8}$ added to initial data (§3.3). **Stated**
9. One-dimensional water-block advection ($N_x=128$, ten periods): both THINC hybrids keep the interface width, WENO5IS alone smears it, and velocity and pressure stay free of oscillation; likewise the 2D droplet at $128^2$ (§4.1, Figs. 3–4). **Shown**
10. Gas–liquid Riemann problem (density ratio $10^3$, pressure ratio $10^4$): WENO5IS-THINC sharpens the interface and resolves shock and rarefaction best (§4.2, Fig. 5). **Shown**
11. A 1 GPa shock on a static water–air interface: WENO5IS alone oscillates at the transmitted shock and the rarefaction head, interface sharpening suppresses this, and WENO5IS-THINC gives the best shock position (§4.3, Fig. 6). **Shown**
12. On a moving interface the oscillations of WENO5IS are stronger; WENO5IS-THINC agrees best with the reference, though a "remarkable discrepancy in the shock position" remains at $N_x=512$ (§4.4, Fig. 7). **Shown**
13. $L_1$ errors of these two problems on $N_x=128$ to 2048: the THINC methods converge at roughly first order, WENO5IS below one, and WENO5IS-THINC has the smallest errors (§4.4, Fig. 8). **Shown**
14. In smooth regions THINC is inactive and the scheme is finite-volume WENO5IS with HLLC; "Thus, the overall theoretical accuracy is first-order according to the analysis in [25]" (§4.4). **Stated** (no smooth-data convergence test is shown) *(compiler check, not in the sources: the WENO5IS candidates (C.1)–(C.2) and weights $d_k=(15/32,5/32,5/16,1/16)$ combine exactly into $\frac1{128}(3,-20,90,60,-5)$, the Lagrange interpolation of point values at $x_{i+1/2}$; the fifth-order reconstruction of a face value from cell averages is $\frac1{60}(2,-13,47,27,-3)$. Applied to cell averages, as §3.1 states, the formula is second-order accurate.)*
15. Mach 2.4 shock on a water cylinder ($3072\times2048$): the numerical schlieren agrees qualitatively with the experiment of Sembian et al.; the water "mist" is a pseudo-capillary effect of interface sharpening (§4.5, Fig. 9). **Shown**
16. Mach 6 shock on two cylinders: WENO5IS-THINC captures vortices more clearly and develops Rayleigh–Taylor and Kelvin–Helmholtz instabilities more strongly than MUSCL-THINC; the [carbuncle](/definitions/carbuncle-phenomenon.md) appears for both (§4.6, Figs. 10–11). **Shown**
17. Mach 10 shock on a water cylinder: negative pressure appears in the water behind strong rarefactions; from $480\times320$ to $1920\times1280$ MUSCL-THINC loses symmetry as resolution increases, while WENO5IS-THINC "perfectly preserves the symmetry at different resolutions" (§4.7, Figs. 12–13). **Shown**
18. Mach 10 air-bubble collapse in water ($3840\times1920$): jet, water-hammer shock and sheet jetting are reproduced, bubble outlines converge under refinement, and the bubble mass is conserved exactly over the domain (§4.8, Figs. 14–16a). **Shown**
19. The fraction of cells using the limiter exceeds 1% for WENO-JS5, is much lower for TENO5 and is lowest for WENO5IS, never above 0.04%, hence WENO5IS is "the optimal choice" of base scheme (§4.8, Fig. 16b). **Shown**
20. Laplace law ($128^2$): $\beta_{\mathrm T}$ from 1.3 to 2.3 leaves $\phi_1$ nearly unchanged, but 1.8 and 2.3 add a spurious pressure jump ($L_1$ pressure errors $0.99$, $1.66$, $1.81\times10^{-2}$); $\beta_{\mathrm T}$ should not be too large with surface tension (§4.9, Table 11, Fig. 17). **Shown**
21. Laplace law at $\beta_{\mathrm T}=1.3$, $64^2$–$256^2$: THINC methods converge at about first order in pressure, WENO5IS below one (§4.9, Fig. 18). **Shown**
22. Oscillating ellipse: larger $\beta_{\mathrm T}$ damps the kinetic energy more and shifts the period; $\beta_{\mathrm T}=1.3$ matches the analytic half period best; MUSCL-THINC decays most (§4.10, Fig. 19). **Shown**
23. Parasitic currents at Laplace number $10^{11}$: capillary numbers $10^{-6}$–$10^{-7}$, similar for the three methods and decreasing with resolution (§4.11, Fig. 20). **Shown**
24. A head-on droplet collision with surface tension and viscosity ($512^2$) shows merging, a filament and a satellite droplet with symmetry kept (§4.12, Fig. 21). **Shown**
25. The method leaves the model equations unchanged and extends to 3D "straightforward[ly]" (§5). **Stated**

# Printed slips

- Eq. (8): $\mathbf D=\frac12(\nabla\cdot\mathbf u+(\nabla\cdot\mathbf u)^T)$, the divergence where the velocity gradient $\nabla\mathbf u$ is meant.
- Eq. (34): $\kappa=-\nabla\cdot\mathbf n$ printed as $-(\psi_{xx}+\psi_{yy}+\psi_{zz})/\lvert\nabla\psi\rvert$. *(Compiler check, not in the sources: with $\mathbf n=-\nabla\psi/\lvert\nabla\psi\rvert$ (Eq. 32), $-\nabla\cdot\mathbf n=\Delta\psi/\lvert\nabla\psi\rvert-\nabla\psi\cdot\nabla\lvert\nabla\psi\rvert/\lvert\nabla\psi\rvert^2$; the printed form has the opposite sign and drops the second term.)* The text reads "Eq. (32) and ((34)".
- §3.3: "$\rho c^2=\frac{p+P_\infty}{\gamma-1}$ is used to limit $c^2$"; Eq. (16) gives $\rho c^2=\gamma(p+P_\infty)$. Both are positive iff $p+P_\infty>0$, so the limiter acts the same.
- Fig. 5 caption and §4.2: "$\rho_1=1000$ kg/m²".
- §4.6: "diameters of $D=0.064$ m and $D=0.005$ m" in the domain $[0,0.03]\times[0,0.025]$ m; a 0.064 m cylinder does not fit.
- Table 7 (Mach 6): post-shock air pressure $4.05\times10^6$ Pa. *(Compiler check: ideal-gas Rankine–Hugoniot at Mach 6 into $\rho=1.2$, $p=10^5$, $\gamma=1.4$ gives $\rho=6.322$, $v=1660.4$ m/s, matching the printed 6.32 and 1660.39, and $p=4.183\times10^6$ Pa; $4.05\times10^6$ corresponds to Mach 5.90. Table 8, Mach 10, agrees with the same relations.)*
- Table 6 (Mach 2.4): *(compiler check: the same relations with $\rho=1.17$ give $\rho=3.758$, $v=571.7$ m/s and $p=6.55\times10^5$ Pa against the printed 3.76, 574.57 and $6.62\times10^5$, a mismatch of about 1 % in $v$ and $p$.)*
- §4.10: $T/2=40.56$; with $R=1$, $\sigma_{\mathrm{st}}=1$ and densities 1000 and 1, $\pi\sqrt{1001/6}=40.58$ *(compiler check)*.
- §4.8 calls the ALPACA paper [58] a "front-tracking method"; §1 "Tagaki et al. [37]" for Takagi; Fig. 15 caption labels two panels "(a)".
- Ref. [5] prints "J. Comput. Phys. 50 (2017)"; ref. [22] prints "Phys. Fluids 13 (2013)", while ref. [16] has volume 13 for 2001. Refs. [64], [65] print "N. Fleischman" for the co-author Fleischmann.

# Notation map

| Zhang et al. (2024a) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\alpha_1$, $\alpha_2$ | $\phi_1$, $\phi_2$ | volume fractions; 1 = water, 2 = air; **$\alpha$ is $\alpha_k$ (unnormalized weights) in the registry** |
| $\rho_1\alpha_1$, $\rho_2\alpha_2$ | $\phi_1\rho_1$, $\phi_2\rho_2$ | "phase densities" = partial densities |
| $\rho$, $\mathbf u=(u,v,w)$, $p$, $E$, $e$ | $\rho$, $v=(v_1,v_2,v_3)$, $p$, $E$, $e$ | |
| $\gamma$, $P_\infty$ | $\gamma$, $p_\infty$ ($p_{\infty,k}$ per phase) | stiffened gas |
| $c$ | $c$ | frozen mixture sound speed, Eq. (16) |
| $\sigma$ (surface tension) | $\sigma_{\mathrm{st}}$ | |
| $\sigma$ (Eq. 43) | page-local gradient sign | **collides with the surface tension** |
| $\kappa$, $\mathbf n$, $\psi$ | $\kappa_{\mathrm c}$, $\mathbf n$, $\psi=\phi_1$ | **$\kappa$ is the kinetic energy in the registry** |
| $\boldsymbol\tau$, $\mathbf D$, $\mu$ | kept | viscous stress, deformation rate, mixture viscosity |
| $\mathbf q^L_{i+1/2}$, $\mathbf q^R_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | primitive variables reconstructed |
| $s_L$, $s_R$; $s^\pm=\min/\max(0,s_{L,R})$; $s^*$ | $s^-$, $s^+$; kept; $s^*$ | Einfeldt estimates; **the source's $s^\pm$ are not the registry's $s^\pm$** |
| $X$ | kept | $(x-x_{i-1/2})/\Delta x\in[0,1]$ |
| $\beta$, $\beta_i=\beta\lvert n_{x,i}\rvert+0.01$ | $\beta_{\mathrm T}$ | THINC steepness; **$\beta$ collides with $\beta_k$** |
| $c_i$ | $-x^c_i$ | the profile $\tanh(\beta_{\mathrm T}(X+c_i))$ jumps at $X=-c_i$; **$c$ is the sound speed** |
| $\varepsilon_{THINC}$ | kept | interface threshold $10^{-3}$ |
| $\delta_{i+1/2}$ | $\delta^{\mathrm T}_{i+1/2}$ (page-local) | THINC switch; **not the TENO flag $\delta_k$** |
| $\theta_{i+1/2}$ | $\theta$ | limiter blending factor toward the first-order value |
| $\epsilon_{PP1}$, $\epsilon_{PP2}$, $\epsilon_{initial}$ | kept | |
| $S_0,\dots,S_3$, $S_{01}$, $S_5$ | kept | WENO5IS candidates of 2, 2, 3, 3 points, merged $S_0\cup S_1$, full stencil |
| $\tilde q^k_{i+1/2}$, $d_k$, $\beta_k$, $\beta_{01}$ | $u^{(k)}$, $d_k$, $\beta_k$, $\beta_{01}$ | |
| $\tau_5$ | $\tau^{\mathrm{ref}}_5$ | TENO reference indicator, **not the registry's $\tau_5=\lvert\beta_0-\beta_2\rvert$** |
| $\eta_k$, $\omega_k$, $\epsilon$ | $\alpha_k$, $\omega_k$, $\epsilon$ | $\epsilon=10^{-15}$ |
| $La$, $Ca$ | kept | Laplace and capillary numbers |

# Reference list

69 printed references in numbered style ([1]–[69]), all parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `zhang-2024`. No DOIs or arXiv identifiers are
printed. [25] is [Wong et al. (2021)](/sources/wong-2021.md), [37]
[Takagi et al. (2022)](/sources/takagi-2022.md), [38] [Liang et al. (2022)](/sources/liang-2022.md),
[39] [Paula et al. (2023)](/sources/paula-2023.md) and [47] [Bryngelson et al. (2021)](/sources/bryngelson-2021.md). [44] (Harlow & Amsden, LA-4700) is a technical report. The printed volumes of [5] and [22] are
implausible (see Printed slips); "N. Fleischman" in [64], [65] is the spelling of Fleischmann. No
printed duplicates.

# Pages created or updated

Chunk 8 (2026-10-23), cited further in chunk 9 (2026-10-23). This source is cited on:

* [Boundary variation diminishing (BVD)](/definitions/boundary-variation-diminishing.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gas–liquid Riemann problems](/benchmarks/gas-liquid-riemann-problems.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Incremental-stencil WENO](/methods/incremental-stencil-weno.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Oscillating droplet](/benchmarks/oscillating-droplet.md)
* [Positivity-preserving flux limiter (Hu–Adams–Shu)](/methods/positivity-preserving-flux-limiter.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Shock–water-column interaction](/benchmarks/shock-water-column.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Targeted ENO (TENO)](/methods/targeted-eno.md)
* [TENO-THINC](/methods/teno-thinc.md)
* [THINC reconstruction](/methods/thinc-reconstruction.md)
