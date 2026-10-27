---
type: Source
title: "Jiang et al. (2025) — Efficient implementation of the k-√k L turbulence model with the discontinuous Galerkin method"
description: "First implementation of Menter's k-√kL model, the RANS model behind scale-adaptive simulation, in a high-order modal discontinuous Galerkin solver: HWENO limiting of k, a positive surrogate of the length-scale variable, and compact lift-operator second derivatives for the von Kármán length; tested on a flat plate, RAE2822 and a square cylinder."
resource: "doi:10.1007/s10409-024-24174-x"
source_kind: paper
authors: [Jiang Z., Yan C., Yu J., Li Y.]
year: 2025
venue: "Acta Mech. Sin. 41:324174"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Acta_Mechanica_Sinica_Jiang_Efficient_implementation_of_the_k-sqrtk_L_turbulence_model_w.pdf"
tags: [rans, hybrid-rans-les, dg, eddy-viscosity, shock-capturing]
timestamp: 2026-10-27T15:54:00Z
---

# Summary

Jiang et al. (2025) implement the $k$-$\sqrt k L$ (KSKL) two-equation model
of Menter, Egorov and Rusch, the RANS model on which
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md) (SAS) is
built, in a high-order modal discontinuous Galerkin solver for the
compressible RANS equations (Taylor basis, local Lax–Friedrichs flux, BR2
viscous flux, preconditioned GMRES or ESDIRK); see the
[DG spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
page for the element-method family. The model closes the stress with the
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md). To the
authors' knowledge KSKL had only been run in finite-volume codes.

Three devices make it work. First, oscillations of $k$ near the
under-resolved boundary-layer edge are removed by replacing the polynomial
of $k$ in troubled cells, flagged by an element-resolution indicator, with a
Hermite-[WENO](/methods/weno-scheme.md) reconstruction; the same HWENO
limiter captures the shock of the transonic case. (The authors cite the
indicator of Persson and Peraire; no
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md) is
used.) Second, the normalized length-scale variable is mapped to an
always-positive surrogate $\psi$, a device borrowed from a DG treatment of
the [Spalart–Allmaras model](/methods/spalart-allmaras-model.md), which
replaces it in the source terms and the eddy viscosity. Third, the second
velocity derivatives of the von Kármán length $L_{\mathrm{vK}}$ are the
gradient of the projected first derivatives corrected by the BR2 global
lift operator, so the stencil stays compact.

On a [flat-plate boundary layer](/benchmarks/turbulent-boundary-layer.md)
($M_\infty=0.3$, $Re=3\times10^6$) the stabilization makes the implicit
solver converge, the lift operator removes an anomaly of $L_{\mathrm{vK}}$
at $y^+\approx3000$, and $C_f$ improves with mesh and order. On RAE2822
lift and drag are within about 3% and 5% of experiment. On the
two-dimensional [square cylinder](/benchmarks/square-cylinder-flow.md) at
$Re=10^4$ KSKL gives a smaller eddy viscosity in the wake than SA and
"SAS-like" unsteadiness, with mean velocities in substantial but not full
agreement with a two-dimensional DNS.

# Version read

Version of record (Springer, online 4 September 2024, issue 2025); 12
pages including Appendix A and a Chinese abstract, all read, Eqs. (1)–(20)
and (A1)–(A5) visually. Page 1 matches Crossref. The filename carries the
online year 2024. Equation, section and reference numbers are those of the
version of record.

# Key claims

The KSKL equations as printed (A1), in registry symbols, with $\Phi_L$ the
length-scale variable (dimensionally $\sqrt k\,L$, never written so in the
paper) and $C_\mu$ for the printed $C_u$:

$$\begin{aligned}
\partial_t(\rho k)+\nabla\cdot(\rho k\boldsymbol u)&=P_k-C_\mu^{3/4}\rho\frac{k^2}{\Phi_L}-2\mu\frac{k}{d^2}+\nabla\cdot\big[(\mu+\sigma_k\mu_t)\nabla k\big],\\
\partial_t(\rho\Phi_L)+\nabla\cdot(\rho\Phi_L\boldsymbol u)&=C_{\phi1}\frac{\Phi_L}{k}P_k-C_{\phi2}\rho k-6\mu\frac{\Phi_L}{d^2}f_\phi+\nabla\cdot\big[(\mu+\sigma_\phi\mu_t)\nabla\Phi_L\big],
\end{aligned}$$

with $P_k=\min(P,\,20C_\mu^{3/4}\rho k^2/\Phi_L)$,
$C_{\phi1}=\zeta_1-\zeta_2(\Phi_L/(\sqrt kL_{\mathrm{vK}}))^2$,
$C_{\phi2}=\zeta_3$, $L_{\mathrm{vK}}=\kappa|S|/|\nabla^2\boldsymbol u|$ and
$\sigma_k=\sigma_\phi=2/3$, $\kappa=0.41$, $C_\mu=0.09$, $\zeta_1=0.8$,
$\zeta_2=1.47$, $\zeta_3=0.0288$ (A2–A5). The positive surrogate (Eq. 10)
and the modified eddy viscosity (Eq. 13):

$$\psi=\begin{cases}0.02\log\big(1+e^{50\chi_\Phi}\big),&\chi_\Phi\le5,\\ \chi_\Phi,&\chi_\Phi>5,\end{cases}\qquad \chi_\Phi=\frac{\Phi_L}{\nu},\qquad \mu_t=C_\mu^{1/4}\rho\,\nu\psi .$$

1. KSKL had not been developed within a high-order DG framework before (to the authors' knowledge); earlier assessments are finite-volume (§1). **Stated**
2. In DG discretizations of RANS the turbulence variables behave non-smoothly because of the high-order approximation of nonlinear functions, and most works stabilize them somehow (§1, §3.1). **Stated**
3. Oscillations of $k$ occur near the under-resolved boundary-layer edge, where the $k$ profile changes slope rapidly; HWENO limiting of $k$ in troubled cells detected by an element-resolution indicator removes them (§3.1). **Stated** (method); effect **Shown** (Fig. 1a)
4. $\psi$ (Eq. 10) is positive whatever the value of $\Phi_L$; replacing $\Phi_L$ by $\nu\psi$ in the sources (Eqs. 11–12) and in $\mu_t$ (Eq. 13) keeps the eddy viscosity positive (§3.1). **Derived**
5. Second derivatives in DG should be at least as accurate as the first derivatives and use face neighbours only (§3.2). **Stated**
6. Finite-volume or finite-difference central differencing of gradients does not carry over to DG, because the volume Gauss points are not equally spaced, and would break compactness and complicate the implicit Jacobian (§3.2). **Stated**
7. $\boldsymbol g_h=\nabla\boldsymbol s_h+\boldsymbol R_h$ (Eq. 17), with $\boldsymbol s_h$ the $L^2$ projection of the first derivatives and $\boldsymbol R_h$ the BR2 global lift, meets both requirements; the "local derivative method" $\boldsymbol g_h=\nabla\boldsymbol s_h$ uses only the cell's own data (§3.2, Eqs. 14–20). **Derived**
8. On the flat plate (medium mesh, $N=2$) both derivative procedures give close $L_{\mathrm{vK}}$ profiles, but the lift operator removes the anomalous oscillation of the local method at $y^+\approx3000$ (§4.1, Fig. 2). **Shown**
9. With explicit three-stage TVD Runge–Kutta the stabilized method oscillates much less in the residual history than the original (§4.1, Fig. 1a). **Shown**
10. With preconditioned GMRES the computation diverges without the stabilization; with it the residual drops about 5 or 6 orders before stagnating for $N=2$ and $N=3$ (§4.1, Fig. 1b). **Shown**
11. Velocity profiles agree in the viscous sublayer and log layer on the medium and refined meshes; different orders on the medium mesh give almost identical profiles; $C_f$ improves with grid density and order (§4.1, Figs. 3–4). **Shown**
12. Large $C_f$ differences for $x<0.1$ between meshes are a streamwise-resolution effect: after Rumsey, the laminar region near the plate nose grows with grid density, and the higher order also gives a later "transition", a numerical and not a physical one (§4.1, Figs. 3b, 4). **Shown** (difference) / **Stated** (explanation)
13. RAE2822 ($M_\infty=0.734$, $Re=6.5\times10^6$, $2.79°$): $C_L=0.779$ ($N=2$) and $0.782$ ($N=3$), $C_D=0.0177$ and $0.0176$, against measured $0.803$ and $0.0168$, errors "around the range of 3% and 5%" (§4.2). **Shown**
14. RAE2822: the density residual drops almost 5 orders for $N=3$; $C_p$ agrees with experiment, with a small deviation at the shock (§4.2, Fig. 6). **Shown**
15. $L_{\mathrm{vK}}$ oscillates around the shock without visibly affecting the eddy viscosity, and follows the boundary layer, wake and shock (§4.2, Fig. 7). **Shown**
16. Square cylinder ($M_\infty=0.05$, $Re=10^4$, $N=3$): through $L_{\mathrm{vK}}$ KSKL gives a smaller eddy viscosity, especially in large separated regions, and "slightly chaotically vortex flows" behind the cylinder, SAS-like in two dimensions (§4.3, Figs. 8–9). **Shown**
17. Square cylinder: mean velocities of KSKL agree substantially, though not fully, with the two-dimensional DNS of Wissink; boundary-layer stations agree well, wake stations in trend (§4.3, Figs. 10–11). **Shown**
18. The SA comparison on the square cylinder "may not be a fair comparison", SA being meant for steady high-Reynolds-number flow; a fairer one would be three-dimensional DES or SAS (§4.3). **Stated**
19. The local Lax–Friedrichs flux is highly dissipative; Roe or HLLC fluxes also apply (§2). **Stated**
20. The stabilization and derivative techniques extend directly to three dimensions; HWENO limiting stays complicated there (§5). **Stated**
21. The method could extend DG URANS to large separated flows; the long-term goal is hybrid RANS/LES with DG (§5). **Stated**

# Printed slips

- Eqs. (4), (11), (A1), (A2) print the destruction and limiter constant as $C_u^{3/4}$; Eq. (13), (A4) and the constant list (A5) use $C_\mu$, and (A5) defines no $C_u$.
- Eqs. (11)–(12) use the unlimited production $P$ where (A1) uses the limited $P_k$.
- $f_\phi=(1+C_{d1}\xi)/(1+\xi^4)$ (A2) uses $C_{d1}$; (A5) prints no value for it.
- (A4) prints "$C_{12}\kappa d[P/C_\mu^{3/4}\rho k^2/\Phi]$" without grouping of the denominator.
- $\kappa$ is both the thermal conductivity (Eq. 3) and the von Kármán constant (A3, A5).
- Eq. (10) writes "log" without base; the two branches of $\psi$ meet at $\chi_\Phi=5$ only with the natural logarithm ($0.02\ln(1+e^{250})\approx5.00$) *(compiler check, not in the sources)*.
- §4: "The explicit single diagonal implicit Runge-Kutta solver, which is also known as the ESDIRK solver".
- "Mach number counters" (Fig. 5 caption), "turbulent viscosity counters" (§4.2, §4.3), "the wake of the squire" (Fig. 11 caption).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Phi$ | $\Phi_L$ (KSKL length-scale variable, page-local) | **collision** with the Ducros factor $\Phi_i$ |
| $\chi=\Phi/\upsilon$, $\psi$ | $\chi_\Phi$, $\psi$ (page-local) | **collision** with the SA $\chi=\tilde\nu/\nu$ |
| $\upsilon=\mu/\rho$ | $\nu$ | kinematic viscosity |
| $C_u$ (Eqs. 4, 11, A1, A2) | $C_\mu$ | printed slip |
| $\tau_{ij}$ (A2) $=\mu_t(2S_{ij}-\tfrac23\partial_ku_k\delta_{ij})-\tfrac23\rho k\delta_{ij}$ | $-\langle\rho u_i''u_j''\rangle$ | **sign:** negative of the registry's positive-trace Reynolds stress |
| $\underline{\boldsymbol\tau}$ (Eq. 6) | $(\mu+\mu_t)$ times twice the deviatoric strain | molecular plus eddy stress |
| $\kappa$ (Eq. 3) | $\kappa_{\mathrm{th}}$ (thermal conductivity, page-local) | **collision** with the von Kármán $\kappa$ |
| $\kappa$ (A3, A5) | $\kappa$ | 0.41 |
| $U'=\sqrt{2S_{ij}S_{ij}}$ | $\lvert S\rvert$ | with the factor two |
| $U''$ | $\lvert\nabla^2\boldsymbol u\rvert$ | two-dimensional Laplacian magnitude |
| $L_{vK}$ | $L_{\mathrm{vK}}$ (page-local) | von Kármán length |
| $P$, $P_k$ | $P_k$ (unlimited), $\min(P_k,\dots)$ | production and its limited form |
| $\xi$, $f_\phi$, $C_{d1}$, $C_{11}$, $C_{12}$, $\zeta_{1,2,3}$, $C_{\phi1}$, $C_{\phi2}$, $\sigma_\phi$ | same (page-local) | **collision:** $\xi$ is not the reference coordinate |
| $d$, $\mu_t$, $\sigma_k$ | $d$, $\mu_t$, $\sigma_k$ | |
| DG(P1)–DG(P3), "$p+1$ order" | $N=1$–$3$ | "third order" is $N=2$ |
| $N$ (number of modes), $v_h$, $M_K$ | (page-local) | **collision:** $N$ is not the polynomial degree here |
| $\boldsymbol s_h$, $\boldsymbol g_h$, $\boldsymbol r_h^\sigma$, $\boldsymbol R_h$ | (projected first derivatives, second derivatives, local and global lift, page-local) | |
| $c_f$ | $C_f$ | |
| $Re_\infty$ | $Re$ | on plate length, chord or square height |

# Reference list

46 printed references, numbered style, all parsed. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [8] (Zhao et al. 2023, Comput. Fluids 263:105967) is the
ingested `zhao-2023-b`, not `zhao-2023`; ref. [12] (Wang L. et al. 2013,
AIAA) is keyed `wang-2013-e`, distinct from the ingested [wang-2013](/sources/wang-2013.md), a different work. Refs. [17], [18], [23], [25], [26], [27] are the existing
bibliography entries `lodares-2022`, `elzaabalawy-2023`, `ghidoni-2022`,
`basile-2023`, `kou-2023` and `ferrer-2023`, all ingested Sources
([ghidoni-2022](/sources/ghidoni-2022.md) among them). Two Fu et al. (2022) papers are keyed in
printed order. Refs. [20] and [23] print the journal as "Numer. Methods
Fluids"; ref. [5] prints "Fran-ranchina".

# Pages created or updated

Chunk 8 (2026-10-27), cited further in chunk 9. This source is cited on:

- [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md)
- [Flow past a square cylinder](/benchmarks/square-cylinder-flow.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Scale-adaptive simulation](/methods/scale-adaptive-simulation.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
