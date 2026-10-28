---
type: Source
title: "De Cosmo et al. (2025) — Validation of a low-dissipation Finite-Volume solver for implicit Large-Eddy Simulation"
description: "Ports a second-order unstructured finite-volume URANS code to wall-resolved implicit LES with a low-dissipation Roe flux that zeroes the linear-wave eigenvalues and scales the acoustic ones by a coefficient calibrated on decaying isotropic turbulence, then validates it on a channel at Re_tau 200 and a channel with a curved-wall bump."
resource: "doi:10.1016/j.compfluid.2025.106623"
source_kind: paper
authors: [De Cosmo G., di Mare L., Carnevale M.]
year: 2025
venue: "Comput. Fluids 295:106623"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Computers_amp_Fluids_De_Validation_of_a_low-dissipation_Finite-Volume_solver_for_imp.pdf"
tags: [implicit-les, numerical-dissipation, finite-volume, compressible, turbomachinery, channel-flow]
timestamp: 2026-10-28T12:42:00Z
---

# Summary

De Cosmo et al. (2025) port Zephyrus, a cell-centred unstructured
compressible finite-volume URANS code (C++, on the data structure of AU3X,
for turbomachinery), to wall-resolved
[implicit LES](/definitions/implicit-les.md): the subgrid stress of the
Favre-filtered equations ([LES](/definitions/large-eddy-simulation.md)) is
dropped, the run is "laminar" on a fine grid, and the dissipation of the
convective scheme acts as the closure. The Roe flux with
second-order U-MUSCL reconstruction (Nishikawa) is judged too dissipative,
so the authors rescale the eigenvalues of the Roe matrix when the
dissipation matrix is assembled: the three linear (entropy and vorticity)
eigenvalues are set to zero and the two acoustic ones, $u_n\mp c$, are
multiplied by a scalar $c_{\mathrm{diss}}$, a hybrid of jump-vector fixes
(Thornber et al., Rieper) and whole-matrix scalings (Amirante & Hills,
Camarri et al., Bui). Unlike earlier work, which takes the smallest stable
value, $c_{\mathrm{diss}}$ is calibrated on decaying
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
against the Comte-Bellot–Corrsin spectra: $c_{\mathrm{diss}}=0.001$; larger
values over-dissipate (steeper inertial range, lower energy), smaller ones
pile energy up near the Nyquist wavenumber
([numerical dissipation](/properties/numerical-dissipation.md)). The
reference for that case is OpenFOAM with the
[WALE model](/methods/wale-model.md). An isentropic vortex checks the
second-order accuracy.

Validation is a [channel](/benchmarks/turbulent-channel-flow.md) at
$Re_b=3173$, $Re_\tau=200$ (Banchetti, Luchini & Quadrio mesh and domain),
against DNS at $Re_\tau=180$: centreline-to-bulk ratio 1.186 against 1.168,
$u^+$ 2% high at $y^+=100$ (read as excess dissipation through the
[law of the wall](/definitions/law-of-the-wall.md)), Reynolds stresses and
kinetic-energy budgets close to DNS. The second case is the same channel
with an asymmetric two-Gaussian bump on the lower wall (Banchetti et al.;
not the Boeing bump), fed by the periodic channel as precursor
([inflow generation](/methods/inflow-turbulence-generation.md)) and
compared with DNS and an [OpenFOAM](/software/openfoam.md) LES with the
[one-equation subgrid model](/methods/subgrid-kinetic-energy-equation-model.md):
the $C_p$ suction peak is 6% and the $C_f$ peak 4% high, and two normal
Reynolds stresses are slightly low, which the authors attribute to
dissipation from mesh non-orthogonality and non-uniformity. The authors
conclude that a second-order finite-volume scheme with this fix suffices
for implicit LES of these cases; SLAU and $k$-exact schemes are named as
alternatives, not used. Zephyrus also has [Wilcox $k$-$\omega$](/methods/k-omega-model.md)
and $k$-$\varepsilon$ URANS closures, unused here. The
[Smagorinsky model](/methods/smagorinsky-model.md) enters only through
the literature review (Camarri et al.'s dynamic Smagorinsky model with an
upwind parameter; Amirante & Hills's results comparable to Smagorinsky),
and the [DNS](/definitions/direct-numerical-simulation.md) of Banchetti
et al. only as the reference.

# Version read

Version of record (Elsevier, open access CC BY; received 17 December 2024,
accepted 31 March 2025, online 12 April 2025), 14 pages, all read,
pp. 3–6 and 8–10 checked visually. Page 1 matches the metadata; no
identity issue. Equation, figure, table and section numbers are those of
this version.

# Key claims

Page-local symbols: $c_{\mathrm{diss}}$ the scaling of the acoustic
eigenvalues; $\lambda^{\mathrm R}_1=u_n-c$, $\lambda^{\mathrm R}_{2,3,4}=u_n$,
$\lambda^{\mathrm R}_5=u_n+c$ the Roe-matrix eigenvalues and
$\lambda^{\mathrm{ld}}_i$ their rescaled values (the source's $\lambda_i$,
$\tilde\lambda_i$); $\mathsf A_{\mathrm{Roe}}$ the Roe matrix; $\boldsymbol q_L$,
$\boldsymbol q_R$ the reconstructed face states (the source's $\bar\Phi$);
$U_b$ the bulk velocity (the source's $V_b$); $u_{\mathrm{cl}}$ the
centreline velocity (the source's $u(h)$); $t^*=tV_0/L$ the isotropic
turbulence time; $\varepsilon^{\mathrm{ps}}$ the pseudo-dissipation.

1. Most second-order finite-volume methods for compressible flows are too dissipative for implicit LES; the numerical dissipation of compressible schemes "does not scale correctly for Mach numbers approaching zero" (formally proved in [10]) (§1, §2.2). **Stated**
2. Implicit LES "reduces to a laminar simulation on a sufficiently fine grid, adopting a timestep small enough"; the high refinement is "the only characteristic that distinguishes the iLES from a Very Large-Eddy Simulation (VLES) or from a laminar simulation" (§1). **Stated**
3. Amirante & Hills [16] state that a zero scaling in their low-dissipation Roe scheme is impossible because it reduces to a central scheme with unbounded oscillations (§1). **Stated**
4. Per Bui [33], better turbulence predictions with Roe flux-difference splitting come only from scaling the dissipation down by a scalar, not from refining space or time or from more accurate time marching, and the scaling should be the minimum stable value (§2.2). **Stated**
5. Proposed fix (Eq. 8): $\lambda^{\mathrm{ld}}_1=c_{\mathrm{diss}}\lambda^{\mathrm R}_1$, $\lambda^{\mathrm{ld}}_{2,3,4}=0$, $\lambda^{\mathrm{ld}}_5=c_{\mathrm{diss}}\lambda^{\mathrm R}_5$, applied when the dissipation matrix is assembled, not to the flux; the linear-wave dissipation "can be completely discarded" in the absence of shocks or other compressible effects needing stabilization, while the acoustic dissipation "is essential for the stability of the calculation" (§2.2, Eqs. 6–8). **Stated** (design argument, no analysis)
6. $c_{\mathrm{diss}}$ cannot be set to the minimum value that ensures stability, because "this leads to the dissipation being too low"; it is calibrated on the isotropic-turbulence decay (§2.2, §3.2). **Shown** (Fig. 5)
7. With U-MUSCL the vortex-transport error falls "almost with slope 2" (Fig. 2 legend: 1.904); first order gives a slope below 1 (legend 0.459), rising to 0.6 on the two finest levels; the second-order error stays below 1%, down to 0.01% (§3.1, Fig. 2). **Shown**
8. Isotropic turbulence with $c_{\mathrm{diss}}=0.001$: the initial spectrum matches $t^*=42$ up to Nyquist on all grids; at $t^*=98$ both Zephyrus and OpenFOAM (WALE) catch the $-5/3$ slope and depart only near Nyquist, less on finer grids; agreement with experiment at $t^*=171$ is "equally satisfactory"; OpenFOAM is "slightly less dissipative" (§3.2, Fig. 4). **Shown**
9. Sensitivity on $64^3$ at $t^*=98$ with $c_{\mathrm{diss}}=0.0001$, 0.0005, 0.001, 0.002, 0.01: values above 0.001 steepen the $-5/3$ range and lower the energy, values below 0.001 flatten the curves and overestimate the energy near Nyquist (§3.2, Fig. 5). **Shown**
10. The channel domain $12\delta\times2\delta\times4\delta$ is adequate: the two-point correlations at $y^+=20$ (streamwise) and $y^+=200$ (spanwise) reach almost zero (§3.3, Fig. 7). **Shown**
11. Centreline-to-bulk velocity: DNS 1.168, Dean's correlation $1.28\,Re_b^{-0.0116}=1.156$, implicit LES 1.186, "3% higher than the reference value", related to an underestimated bulk velocity (§3.3). **Shown**
12. Mean velocity is in "excellent agreement" with DNS, at most 3% high at the centreline; the velocity defect agrees with DNS and departs from the log law at low $y/\delta$; $u^+$ is 2% high at $y^+=100$ (§3.3, Figs. 8–9). **Shown**
13. A high $u^+$ in the log layer "indicates too high numerical dissipation and an underestimation of $\tau_w$", and a high $\langle u'u'\rangle$ indicates excessive numerical dissipation, "marginally the case here" (§3.3). **Stated** (diagnostic), applied **Shown**
14. Kinetic-energy budgets: production peaks at $y^+\approx12$, dissipation is maximum at the wall and balanced by viscous transport; agreement with DNS is "qualitatively good", peak differences being ascribed to the $Re_\tau$ mismatch (200 against 180) and to the isothermal walls; a minor overestimate in the log layer suggests "still slightly over-dissipative" (§3.3, Fig. 10). **Shown**
15. The total shear stress is linear in $y$; deviations "normally indicate an incomplete statistical convergence", negligible here (§3.3, Fig. 9). **Shown**
16. Bump $C_p$: Zephyrus, OpenFOAM and DNS agree "excellent[ly]" (OpenFOAM practically coincident with DNS); the implicit LES shows a small upstream shift of the positive pressure peak and a 6% overestimate of the negative peak at the bump tip (§3.4, Fig. 14). **Shown**
17. Bump $C_f$: the maximum at the tip is about 3 times the flat-wall value; the flat-wall value $C_f=2(u_\tau/U_b)^2=7.93\cdot10^{-3}$ is matched; the flow does not separate; the $C_f$ peak is 4% high (§3.4, Fig. 15). **Shown**
18. Bump Reynolds stresses at $x/\delta=0$, 3, 10 agree "reasonably well" with OpenFOAM (no DNS fluctuation data), slightly lower in $\langle v'v'\rangle$ and $\langle w'w'\rangle$, attributed to "higher numerical dissipation induced in the iLES by the mesh non-orthogonality and non-uniformity in the streamwise direction" (§3.4, Fig. 16). **Shown** (attribution **Stated**)
19. A second-order finite-volume scheme is sufficient for implicit LES of the investigated cases; lower-dissipation or higher-order schemes (low-dissipation AUSM, $k$-exact) "has not proved essential" (§4). **Stated** (for the cases shown)
20. Calibration on a simple case (isotropic turbulence) leads to accurate modelling of turbulence in more complex cases (channel, bump) (§4). **Shown** (two cases)
21. The channel CFL of 0.3 (on $U_b$ and $\Delta x$) is "more restrictive than it is commonly found in the literature (where often CFL > 1.5)" (§3.3). **Stated**

The scheme in registry notation (Eqs. 4–8): the subgrid stress
$t^{SF}_{ij}=-\tau_{ij}$ is set to zero; the face flux is printed
$f^*=\tfrac12(f_L+f_R)-\tfrac12|\mathsf A_{\mathrm{Roe}}|(\boldsymbol q_L-\boldsymbol q_R)$
with the dissipation $\sum_i\alpha^{\mathrm w}_i|\lambda^{\mathrm R}_i|\boldsymbol k_i$
over wave strengths $\alpha^{\mathrm w}_i$ and right eigenvectors
$\boldsymbol k_i$, and the fix replaces $\lambda^{\mathrm R}_i$ by
$\lambda^{\mathrm{ld}}_i$. Gradients by weighted least squares, Van Leer
limiting face by face, dual time stepping with a second-order backward
scheme, matrix-free Jacobi pseudo-time iterations; air with $\gamma=1.4$,
$Pr=0.72$, Sutherland's law. The channel is driven by a body force per unit
volume $\tau_w/\delta=\rho u_\tau^2/\delta$, isothermal walls at 298 K,
$M=0.143$, $\Delta x^+=15$, $\Delta y^+=7.5$, $\Delta z^+=10$ at the
centreline, first cell at $y^+=0.5$, about $1.2\cdot10^6$ cells. The bump
is $y(x)=a\exp[-((x-b)/c)^2]+a'\exp[-((x-b')/c')^2]$ with height
$0.0837\delta$ at $x/\delta=4.14$ (Eq. 32, Table 5).

# Printed slips

- **Eq. (5):** printed $\bar F^*_c=\frac12(\bar F_L+\bar F_R)-\frac12|\bar A_{Roe}|(\bar\Phi_L-\bar\Phi_R)=\frac12\bar F_{cen}-\frac12|\bar A_{Roe}|\Delta\bar\Phi$: the second form has $\frac12\bar F_{cen}$ against $\frac12(\bar F_L+\bar F_R)$ of the first, and the jump $\Delta\bar\Phi$ and the face-normal convention are not defined.
- **Eq. (6):** $\bar d=\frac12\bar A_{Roe}\cdot\Delta\bar\Phi=\sum_{i=1}^5\alpha_i|\lambda_i|\bar k^i$: the middle term lacks the absolute value of Eq. (5), the right-hand side the factor $\frac12$ of the middle term.
- **§3.1:** "$T_c=\frac{L}{V_0}=10^{-5}$ s". *(Compiler check, not in the sources: with the printed $L=0.1$ m and $V_0=200$ m/s, $L/V_0=5\cdot10^{-4}$ s.)*
- **§3.3, Dean's correlation:** "$1.28\,Re_b^{-0.0116}=1.156$" with $Re_b=3173$, and the implicit-LES 1.186 "3% higher than the reference value". *(Compiler check, not in the sources: $1.28\times3173^{-0.0116}=1.166$; $1.186/1.156=1.026$, while against the DNS value 1.168 named in the preceding sentence $1.186/1.168=1.015$.)*
- **Units:** Table 5 lists $a$, $a'$ as "[−]" and Table 1 lists $R_v=0.005$ as "[–]". *(Compiler check, not in the sources: Eq. 32 makes $a$, $a'$ lengths, and with $\delta=Re_\tau\delta_\nu=10^{-3}$ m and $a$, $a'$ in metres the printed parameters give $h_b/\delta=0.0837$ as printed; Eq. 9 divides a distance by $R_v$.)*
- **Eq. (25):** $V_b=\int_AV\,dA$, printed without $1/A$.
- **Eqs. (23)–(24):** $\nabla\cdot(\rho\bar u\times\bar u)$ (cross product) and $\nabla\cdot(\rho H)$ without the velocity.
- **Below Eq. (20):** "$\kappa=\bar\kappa\cdot\bar\kappa$" without the square root that Eq. (20) carries; Eq. (15) sums to $M$ modes while the text gives "$m=5000$".
- **Eqs. (28)–(31):** $\langle uv\rangle$ and $\langle u_iu_j\rangle$ without primes, while the text writes $R_{ij}=\langle u_i'u_j'\rangle$; Eq. (29) has no average on the right-hand side.
- **Reference data:** §3.3 takes $Re_b=3173$, $Re_\tau=200$ "from the reference DNS in Banchetti et al. [41]", then compares with "DNS data available for a lower friction Reynolds number ($Re_\tau=180$)" and with the centreline ratio 1.168 "from Banchetti et al."; which DNS gives which reference curve is not stated.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar f$, $\tilde f$, $f''$ | $\bar\phi$, $\tilde\phi$, $\phi''$ | filter, Favre filter; $\bar{(\cdot)}$ also marks vectors in §3 |
| $t^{SF}_{ij}=-\bar\rho(\widetilde{u_iu_j}-\tilde u_i\tilde u_j)$ | $-\tau_{ij}$ | **negative convention** |
| $\tilde\tau_{ij}$ | $\sigma_{ij}$ | Eq. (4) prints $2\mu[\partial_j\tilde u_i+\partial_i\tilde u_j-\frac23\partial_k\tilde u_k\delta_{ij}]$; with the paper's own $\bar S=(\nabla\bar u+\nabla\bar u^T)/2$ (Eq. 33) the bracket is $2\tilde S^d_{ij}$, so the printed expression equals $2\sigma_{ij}$ of the registry ($\sigma_{ij}=2\mu S^d_{ij}$) |
| $\lambda_i$, $\tilde\lambda_i$ | $\lambda^{\mathrm R}_i$, $\lambda^{\mathrm{ld}}_i$ (page-local) | **collision** with the Taylor microscale $\lambda$; the tilde is not a Favre filter |
| $c_{diss}$ | $c_{\mathrm{diss}}$ (page-local) | Amirante & Hills's $\epsilon$ |
| $\bar A_{Roe}$, $\bar\Phi_{L,R}$, $\alpha_i$, $\bar k^i$ | $\mathsf A_{\mathrm{Roe}}$, $\boldsymbol q_{L,R}$, $\alpha^{\mathrm w}_i$, $\boldsymbol k_i$ (page-local) | **collision** of $\alpha_i$ with the DG blending factor |
| $\kappa$, $\bar\kappa$, $E(\kappa)$ (§3.2) | $k$, $\boldsymbol k$, $E(k)$ | wavenumber; **collision** with the von Kármán $\kappa$ of §3.3 |
| $R_{ij}(\bar r)$ | (page-local) two-point correlation | **collision** with the Reynolds stress $R_{ij}$, which the source also writes $R_{ij}$ |
| $h$ (§3.3–3.4), $h$ (§3.1) | $\delta$; $h$ | channel half-height; mesh size of the vortex grids |
| $V_b$, $u(h)$ | $U_b$, $u_{\mathrm{cl}}$ (page-local) | bulk and centreline velocity |
| $Re_b=\rho V_bh/\mu$, $Re_\tau$, $\delta_\nu$ | $Re_b$, $Re_\tau$, $\delta_\nu$ | on the half-height |
| $f_e$ | $\rho f_x$ | body force per unit volume |
| $k$, $P$, $\tilde\varepsilon$ | $k$, $P_k$, $\varepsilon^{\mathrm{ps}}$ (page-local) | pseudo-dissipation $\nu\langle\partial_ju_i'\partial_ju_i'\rangle$ |
| $\kappa$, $B_1=0.2$, $B=5.2$ | $\kappa$, $B_1$ (page-local), $B$ | defect-law and log-law constants; $\kappa$ not printed |
| $\bar\Omega$, $\bar S$, $Q$ | $\Omega_{ij}$, $S_{ij}$, $Q$-criterion | |
| $\beta$, $R_v$, $V_0$, $T_c$ | (page-local) | vortex strength, radius, velocity, convective period |
| $t^*=tV_0/L$, $N$ | $t^*$ (page-local), $N_x$ | isotropic-turbulence time; points per direction |

# Reference list

42 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [35] is the
ingested [wang-2013](/sources/wang-2013.md). Ref. [4] (Piomelli 2022) has no
venue; [13] prints the author twice ("Ollivier-Gooch C, Ollivier-Gooch
C"); [39] is a thesis given by an ADS URL; [42] a Zenodo service
description. The cited works under the keys `grinstein-2007`, `li-2015`,
`olliviergooch-1997`, `wang-2016`, `wang-2017`, `wang-2018`, `white-2019`
and `taylor-1935` are different works from the bibliography entries already
holding those keys and are keyed `grinstein-2007-b`, `li-2015-b`, `olliviergooch-1997-b`, `wang-2016-k`, `wang-2017-s`, `wang-2018-m`, `white-2019-b` and `taylor-1935-b`. No item is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Inflow turbulence generation](/methods/inflow-turbulence-generation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
- [One-equation subgrid kinetic-energy models](/methods/subgrid-kinetic-energy-equation-model.md)
- [WALE model](/methods/wale-model.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [OpenFOAM](/software/openfoam.md)
