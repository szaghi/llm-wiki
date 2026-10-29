---
type: Source
title: "Bilocq et al. (2025) — Comparison of stabilization strategies applied to scale-resolved simulations using the discontinuous Galerkin method"
description: "Comparison, in one collocated DGSEM code, of unstabilized DG, Laplacian artificial viscosity, entropy-stable DG on Gauss–Legendre and Gauss–Lobatto nodes and a new selective entropy-stable DG for under-resolved compressible turbulence with shocks, judged by turbulence statistics, kinetic-energy budgets, stable CFL and cost."
resource: "doi:10.1016/j.jcp.2025.114238"
source_kind: paper
authors: [Bilocq A., Borbouse M., Levaux N., Terrapon V.E., Hillewaert K.]
year: 2025
venue: "J. Comput. Phys. 539:114238"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Bilocq_Comparison_of_stabilization_strategies_applied_to_scale-reso.pdf"
tags: [dg, entropy-stable, shock-capturing, numerical-dissipation, implicit-les, compressible]
timestamp: 2026-10-29T10:04:00Z
---

# Summary

Bilocq et al. (2025) compare stabilization strategies for the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
(collocated on Gauss–Legendre points, local Lax–Friedrichs flux,
incomplete interior penalty) in under-resolved scale-resolving runs of
compressible turbulence with shocks or shocklets; the equations solved
(Eq. 1) carry no subgrid model, and the paper motivates the study by LES,
which "results in highly under-resolved turbulence" (§1) (see
[implicit LES](/definitions/implicit-les.md)).
Five schemes share one Cartesian solver: unstabilized DG; DG with
Persson–Peraire Laplacian [artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
(DG-AV) driven by the Hennemann calibration of the modal-energy
[sensor](/definitions/shock-sensor.md); fully
[entropy-stable](/properties/entropy-conservation.md) DG on Gauss–Legendre
nodes with Chan's hybridized SBP operator, Chandrashekar flux and entropy
projection (ESDG-GL); entropy-stable DG on Gauss–Lobatto nodes
(ESDG-GLL); and the new DG-ES, which applies ESDG-GL only in cells the
Hennemann sensor flags. Tests: decaying compressible
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
with eddy shocklets, the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), a 2D inviscid
strong vortex crossing a stationary shock, and the canonical
[shock–turbulence interaction](/results/shock-generated-turbulence.md)
of Larsson & Lele. Accuracy is read from reference data and from a
kinetic-energy budget (solenoidal and dilatational dissipation,
[pressure dilatation](/definitions/pressure-dilatation.md), boundary
flux) whose imbalance measures the instantaneous numerical error.

Every stabilization keeps the coarse cases stable where unstabilized DG
diverges. Full entropy stability damps vortical structures (through the
entropy-projection error on Gauss–Legendre nodes, through
under-integration on Gauss–Lobatto nodes), overpredicts the dilatational
dissipation and, for ESDG-GL, degrades the pressure dilatation; the
authors say entropy-stable methods, "despite not adding explicit
diffusion, significantly impact these budgets" (§1) (see
[numerical dissipation](/properties/numerical-dissipation.md)). DG-AV is
cheapest (at most 1.08 times DG) and best with moving shocks but depends
on the detector and on the node set, and damps the post-shock turbulence.
DG-ES gives the most accurate turbulent structures, depends little on the
detector, costs 1.25–1.27 times unstabilized DG (1.21–1.28 times DG-AV)
and inherits the time-step
restriction of the entropy projection, quadratic in mesh size with strong
shocks. The conclusion questions the accuracy of positivity-preserving
entropy-stable schemes built on low-order
[subcell finite volumes](/methods/subcell-finite-volume-shock-capturing.md),
among them [FLEXI](/software/flexi.md) ([Krais et al. 2021](/sources/krais-2021.md)).
Evidence is numerical; no entropy inequality is proved for the selective
scheme.

# Version read

Version of record (Elsevier; received 15 December 2024, revised 10 July
2025, accepted 10 July 2025, online 14 July 2025), 24 pages, all read;
pages 3, 4, 7, 8, 12, 17 and 18 checked visually for equations, tables and
captions. Page 1 matches the metadata (title, five authors, venue, DOI).
Numbering on this page is that of the version read.

# Key claims

Page-local symbols: $\mathbb E_{\mathrm P}$ the single-ratio modal-energy
indicator (the source's $\mathcal E$, Eq. 30; written as on
[shock sensors](/definitions/shock-sensor.md)) and $\mathbb T(N)$ its
Hennemann threshold;
$\alpha\in[0,1]$ the logistic sensor value (not the registry's DG/FV
blending factor); $\mu_{\mathrm{av}}$, $C_{\mathrm V}$ the artificial
viscosity and its Vandenhoeck scaling; $\epsilon_1,\dots,\epsilon_5$ the
kinetic-energy budget terms of Eq. (4) and $\Delta\epsilon$ their
imbalance; $\mathcal E=-\rho s$ the mathematical entropy and $\boldsymbol W$
the entropy variables; DOF the degrees of freedom per direction.

1. Unstabilized DGSEM is stable for the isotropic-turbulence case on $11^3$ elements at $N=5$ ($66^3$ DOF) and diverges on every coarser mesh tested ($4^3$, $8^3$ at $N=3$; $3^3$, $6^3$ at $N=4$; $3^3$, $5^3$ at $N=5$); DG-AV, ESDG-GLL, ESDG-GL and DG-ES are stable on all of them (§4.1.3, Table 1). **Shown**
2. Entropy stability in the troubled cells only (DG-ES) stabilizes every coarse mesh tested; it "appears sufficient to satisfy the second law of thermodynamics only in the troubled cells" (§4.1.3). **Shown**
3. ESDG-GL and ESDG-GLL agree with unstabilized DG on the mean-square velocity, temperature and dilatation but underestimate the peak of mean-square vorticity; for ESDG-GL this is attributed to the error of projecting the non-polynomial entropy variables onto the polynomial space (§4.1.2, Fig. 1). **Shown** (attribution **Stated**)
4. Over-integration would reduce the entropy-projection error but "significantly degrades computational performance" (§4.1.2). **Stated**
5. In the isotropic case DG-AV and DG-ES flag at most about 10% of the elements and behave like unstabilized DG; unstabilized DG has the smallest budget error, ESDG-GL the largest (§4.1.2, Fig. 2). **Shown**
6. The schemes with an entropy projection (DG-ES, ESDG-GL) have the most restrictive time steps. Largest stable CFL at $N=5$: on $3^3$ DG-AV 0.31, DG-ES 0.19, ESDG-GL 0.19, ESDG-GLL 0.28; on $5^3$ 0.28/0.22/0.22/0.29; on $11^3$ DG 0.23, DG-AV 0.23, DG-ES 0.18, ESDG-GL 0.18, ESDG-GLL 0.27 (Table 2). **Shown**
7. Cost relative to DG in the isotropic case ($N=3$ on $16^3$, $N=4$ on $13^3$, $N=5$ on $11^3$): DG-AV 1.07, 1.07, 1.08; DG-ES 1.25, 1.25, 1.27; ESDG-GL 2.27, 2.25, 2.19; ESDG-GLL 1.24, 1.30, 1.53 (Table 3); the SBP operator needs $O(N^4)$ two-point flux evaluations against $O(N^3)$ single-point ones (§4.1.4). **Shown** (operation count **Stated**)
8. DG-AV is strongly sensitive to the detector (original Persson–Peraire calibration, Hennemann calibration, or the dilatation–vorticity shock sensor of Fernandez et al.); DG-ES much less, and in the worst case it matches ESDG-GL (§4.1.5, Fig. 3). **Shown**
9. The original Persson–Peraire calibration flags close to 100% of the cells and over-dissipates; the shock sensor fires in more cells than the Hennemann calibration because shocklets persist, strongly damps the dilatation fluctuations, and fails on $4^3$ ($N=3$), $3^3$ and $6^3$ ($N=4$), $3^3$ and $5^3$ ($N=5$) (§4.1.5, Fig. 4, Table 4). **Shown**
10. DG-AV is sensitive to the node choice: a collocated Gauss–Legendre basis beats Gauss–Lobatto interpolation with Gauss–Legendre quadrature; DG-ES barely is (§4.1.5, Fig. 5, §5). **Shown**
11. Supersonic Taylor–Green vortex ($M_0=1.25$, $Re=1600$, $N=3$): unstabilized DG is unstable up to $128^3$ DOF and stable at $256^3$ and $512^3$; every stabilized scheme is stable at all resolutions; the troubled-cell fraction falls from about 37% at the coarsest grid to about 6.5% at $128^3$ DOF and below 1% at the finest (§4.2.2, Table 6). **Shown**
12. Largest stable CFL in the Taylor–Green vortex ($64^3$, $128^3$, $256^3$, $512^3$ DOF): DG unstable, unstable, 0.25, 0.15; DG-AV 0.51, 0.27, 0.25, 0.15; DG-ES and ESDG-GL 0.23, 0.27, 0.25, 0.15; ESDG-GLL 0.51, 0.54, 0.31, 0.19; on refinement all show a "parabolic" (viscous) time-step restriction (§4.2.2, Table 7). **Shown**
13. DG-ES and DG-AV give the highest solenoidal dissipation at every resolution, close to unstabilized DG at the two finest; ESDG-GL underpredicts it from the peak on and ESDG-GLL is more dissipative still; all converge at the finest resolution (§4.2.3, Fig. 7). **Shown**
14. DG-AV underpredicts the dilatational dissipation at all resolutions because it weakens the shocks; the SBP-based schemes overpredict it, most of all those with the entropy projection, because the entropy variables perturb surface quantities and hence the velocity divergence (§4.2.3, Fig. 9). **Shown** (mechanism **Stated**)
15. Mach profiles at $t/t_c=2.5$: DG-AV gives a thicker, oscillation-free shock; ESDG-GL and DG-ES larger under- and overshoots; ESDG-GLL controls oscillations better; at the finest resolution unstabilized DG is almost oscillation-free (§4.2.3, Fig. 10). **Shown**
16. ESDG-GL has the largest pressure-dilatation errors and the slowest convergence, attributed to ill-conditioning of the entropy-to-conservative map (Eq. 12, $\rho e$ exponential in $s$) near large pressure gradients, under-resolved features or near-vacuum states; DG-ES improves on it by confining the projection; DG-AV is best on the coarsest grid; the reference is unstabilized DG at $512^3$ DOF, for lack of literature data (§4.2.3, Fig. 11). **Shown** (mechanism **Stated**)
17. Taylor–Green cost at $N=3$ on $64^3$ cells relative to DG: DG-AV 1.07, DG-ES 1.27, ESDG-GL 1.86, ESDG-GLL 1.16 (Table 8). **Shown**
18. In the strong vortex/shock interaction unstabilized DG is unstable, and the plain Hennemann sensor cannot keep DG-AV and DG-ES stable; it is widened by one sweep $\alpha=\max_{\mathcal K}(\alpha,0.5\alpha_{\mathcal K})$ over face neighbours, enlarging the stabilized region (§4.3.2, Eq. 39). **Shown**
19. Largest stable CFL there (100×50, 200×100 elements): DG-AV 0.8, 0.8; DG-ES and ESDG-GL 0.16, 0.08; ESDG-GLL 0.86, 0.86; with the entropy projection the time-step constraint decreases "quadratically with grid refinement, rather than linearly as might be expected" (§4.3.2, Table 9). **Shown**
20. DG-AV captures the stationary shock cleanly but under-resolves the vortex; the entropy-stable schemes resolve the vortex better but oscillate near and behind the shock; the sensor never fires inside the vortex, so DG-AV's damping is attributed to dissipation during the earlier interaction with the shock (§4.3.3, Figs. 12–14). **Shown**
21. Cost relative to DG-AV: strong vortex/shock ($N=3$, 200×100) DG-ES 1.28, ESDG-GL 1.68, ESDG-GLL 1.01 (Table 10); shock–turbulence interaction ($736\times128^2$ DOF) DG-ES 1.21, ESDG-GL 1.58, ESDG-GLL 1.06 (Table 12). **Shown**
22. Shock–turbulence interaction ($M=1.28$, $M_t=0.22$, $Re_\lambda=40$): largest stable CFL DG-AV, DG-ES and ESDG-GL 0.53, ESDG-GLL 0.69, nearly constant with refinement because the shock is weaker (Table 11); on the coarse grid ($368\times64^2$ DOF) the entropy-stable schemes capture the post-shock amplification of $R_{11}$ and $R_{22}$ better than DG-AV, without spurious oscillations (§4.4.3, Fig. 15). **Shown**
23. DG-AV is recommended when robust, efficient shock resolution is the main concern, DG-ES when under-resolved turbulent structures must be captured accurately; even modest dissipation that DG-AV adds near shocks degrades the post-shock turbulence, although no stabilization acts there (§5). **Shown** (recommendation **Stated**)
24. Entropy-stable schemes with positivity-preserving limiters [40, 64–66] often rest on first- or second-order finite-volume discretizations, and the resulting loss of accuracy "requires further evaluation" (§5). **Stated**

The budget of §2.1 in registry notation (Eq. 4, as printed):
$$-\underbrace{\frac{\mathrm d}{\mathrm dt}\int_\Omega\tfrac12\rho u_iu_i\,\mathrm dV}_{\epsilon_1}=\underbrace{\int_\Omega\mu\,\omega_i\omega_i\,\mathrm dV}_{\epsilon_2}+\underbrace{\tfrac43\int_\Omega\mu(\partial_ju_j)^2\,\mathrm dV}_{\epsilon_3}-\underbrace{\int_\Omega p\,\partial_ju_j\,\mathrm dV}_{\epsilon_4}+\underbrace{\oint_{\partial\Omega}\big(pu_j-\sigma_{ij}u_i-\tfrac12\rho u_iu_iu_j\big)n_j\,\mathrm dS}_{\epsilon_5},$$
with $\Delta\epsilon=\epsilon_2+\epsilon_3+\epsilon_4+\epsilon_5-\epsilon_1$
the "indicator of the *instantaneous* numerical error" (after
[Wang et al. (2024)](/sources/wang-2024.md)); $\epsilon_2$ and $\epsilon_3$
are the unnormalized $\varepsilon_s$ and $\varepsilon_d$. The entropy is
$\mathcal E=-\rho s$, $s=\log\big((p/p_{\mathrm{ref}})/(\rho/\rho_{\mathrm{ref}})^\gamma\big)$,
"the only admissible entropy function for the compressible Navier–Stokes
equations with non-zero heat flux" (Eq. 5, citing [29]), with entropy
variables $\boldsymbol W=\partial\mathcal E/\partial\boldsymbol U$ and the
inequality $\frac{\mathrm d}{\mathrm dt}\int_\Omega\mathcal E\,\mathrm dV\le0$
under suitable boundary conditions (Eqs. 6–9). ESDG-GL computes the
convective divergence by flux differencing with the hybridized operator
$\begin{pmatrix}\boldsymbol Q-\boldsymbol Q^T&\boldsymbol E^T\boldsymbol B\\-\boldsymbol B\boldsymbol E&0\end{pmatrix}$
(Eq. 24) and a two-point entropy-conservative flux, after the entropy
projection: entropy variables at the volume points, $L^2$-projected and
interpolated to volume and surface points, converted back (§3.3); on
Gauss–Lobatto nodes the projection is the identity but the quadrature is
exact only to degree $2N-1$ (§3.4). The sensor (Eqs. 29–30) is
$\alpha=\big(1+\exp(-\tfrac{9.21024}{\mathbb T}(\mathbb E_{\mathrm P}-\mathbb T))\big)^{-1}$,
$\mathbb T=0.5\cdot10^{-1.8(N+1)^{1/4}}$, cut off by
$\alpha_{\min}=0.001$, with $\mathbb E_{\mathrm P}$ the energy fraction of
the highest mode of density; the viscosity (Eq. 31) is
$\mu_{\mathrm{av}}=\alpha C_{\mathrm V}\tfrac hN\lambda_{\max}$,
$C_{\mathrm V}=0.27(M_\infty-1)/M_\infty$, $M_\infty\ge1.2$. RK(4,4) in
all cases; CFL defined by Eq. (32) on the initial condition.

# Printed slips

- **Eqs. (2) and (4):** the boundary flux is printed $(p\boldsymbol v-\boldsymbol\tau\cdot\boldsymbol v-\rho k\boldsymbol v)\cdot\mathbf n$. *(Compiler check, not in the sources: the mass and momentum equations of the paper's Eq. (1) give $\partial_t(\rho k)+\nabla\cdot(\rho k\boldsymbol v)=-\boldsymbol v\cdot\nabla p+\boldsymbol v\cdot(\nabla\cdot\boldsymbol\tau)$, whose integral over $\Omega$ puts $+\rho k\boldsymbol v$ in that flux; the term vanishes in the periodic cases.)*
- **Fig. 5 caption:** "Temporal evolution of the percentage of troubled cells", while the panels show $\langle\omega_i\omega_i\rangle\tau_0^2$ and $\langle\theta'\theta'\rangle\tau_0^2$.
- **Fig. 10:** the caption says "extracted from the $y$ line at $x=y=0$", the text (§4.2.3) "along a line in the $y$-direction at $x=z=0$".
- **Tables 5–7:** Table 5 lists $16^3$ to $128^3$ elements ($64^3$ to $512^3$ DOF); Table 6 has a further $32^3$ column (DG unstable, all others stable) that matches no Table 5 entry and is absent from Table 7.
- **§4.4.1 against Table 11:** the shock–turbulence runs use "CFL = 0.535", above the 0.53 printed as the largest stable CFL of DG-AV, DG-ES and ESDG-GL.
- **Degree symbols:** "p" throughout, quadrature exactness printed as "$2N+1$" (§3.2.3) and "$(2N-1)$" (§3.4), and italic $p$ in $h/p$ of Eq. (31), the symbol of pressure.
- **Velocity gradient** written $\nabla\boldsymbol u$, with $\boldsymbol u$ the conservative variables, in $\boldsymbol S$ and $\boldsymbol\tau$ (p. 3) and in the AV term $\nabla\cdot(\mu_{av}\nabla u)$ (§3.5); the average is printed $\{\mathbf a\}=(\boldsymbol u^++\boldsymbol u^-)/2$ (§3.2.2).
- **Eq. (27):** $\boldsymbol f^k_S(\{\boldsymbol w\}_{\log})$, a single argument for the two-argument flux $\boldsymbol f_S$.
- **§4.4.3:** "Both methods reproduce …" where four stabilized schemes are compared in Fig. 15; §4.3.3 mixes "$t/t_c=0.3$" and "$t=0.7$" for one dimensional-time case; §4.2.3 writes "$t/t_C=10$" once.
- **References:** [11] and [47] are the same Johnsen et al. (2010) paper, printed with slightly different titles; [21] and [39] are identical; [20] prints "(2023) 30 1–30"; [12] prints the year 2012 for Theor. Comput. Fluid Dyn. 27.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| p, $N$, $p$ | $N$ | polynomial degree ("interpolation order") |
| $\boldsymbol u=\{\rho,\rho\boldsymbol v,\rho E\}$ | $\boldsymbol U$ (page-local) | **collision:** $\boldsymbol u$ is the registry's velocity |
| $\boldsymbol v$, $v_i$; $u,v,w$ (Eqs. 33–35) | $\boldsymbol u$, $u_i$; $(u,v,w)$ | |
| $k=\boldsymbol v\cdot\boldsymbol v/2$ | $\tfrac12u_iu_i$ | **collision** with the turbulent kinetic energy $k$ |
| $\boldsymbol\tau$ | $\sigma_{ij}$ | viscous stress, Stokes hypothesis |
| $\boldsymbol S^d$, $\zeta$, $\kappa$ | $S^d_{ij}$, $\mu_b=0$, thermal conductivity | |
| $\boldsymbol\omega$, $\xi=\boldsymbol\omega\cdot\boldsymbol\omega/2$ | $\omega_i$, half the enstrophy density | |
| $\theta$ | $\partial_ju_j$ | dilatation |
| $\epsilon_2$, $\epsilon_3$, $\epsilon_4$ | unnormalized $\varepsilon_s$, $\varepsilon_d$; pressure dilatation | see [pressure dilatation](/definitions/pressure-dilatation.md) |
| $U=-\rho s$, $\boldsymbol w$, $\mathcal F$ | $\mathcal E$, $\boldsymbol W$, entropy flux (page-local) | as on [entropy conservation](/properties/entropy-conservation.md) |
| $\{\cdot\}$, $\{\cdot\}_{\log}$, $[\cdot]$ | $\{\!\{\cdot\}\!\}$, $\phi^{\ln}$, $[\![\cdot]\!]$ | |
| $\boldsymbol f_S$ | $f^{\#}$ | two-point (Chandrashekar) flux |
| $\boldsymbol f^*$ | $f^*$ | local Lax–Friedrichs |
| $\mathcal E$, $\mathcal T$, $s=9.21024$ | $\mathbb E_{\mathrm P}$, $\mathbb T(N)$, sharpness | **collision** of $s$ with the entropy |
| $\alpha$ | sensor value (page-local) | not the registry's blending factor |
| $\mu_{av}$, $c$, $h$, $\lambda_{max}$ | $\mu_{\mathrm{av}}$, $C_{\mathrm V}$, $h$, $\lambda_{\max}$ | |
| $\lambda$, $Re_\lambda$, $M_t$ | $\lambda$, $Re_\lambda$, $M_t$ | $v_{\mathrm{rms}}=\sqrt{\langle v_iv_i\rangle/3}$; $M_t$ with $\sqrt{\langle v_iv_i\rangle}$ |
| $\tau_0=\lambda_0/v_{rms,0}$, $t_c$ | initial eddy time; Taylor–Green convective time | |
| $\tilde k$, $\tilde k_M$ | wavenumber, spectrum peak | |
| $R_{ij}=\widetilde{v''_iv''_j}$ | $R_{ij}$ in Favre form | kinematic, positive trace |
| $\tilde f$, $f''$ | $\langle f\rangle_\rho$, $f''$ | Favre average, not a filter |

# Reference list

66 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Two pairs
are printed twice ([11] and [47], Johnsen et al. 2010; [21] and [39],
Chan, Del Rey Fernández & Carpenter 2019) and are folded into one entry each.
Ref. [53] (Wang Z. et al., Phys. Fluids 36, 2024, interpolation-based
WENO for the compressible Taylor–Green vortex) is the ingested [Wang et al. (2024b)](/sources/wang-2024-i.md), whose printed-order key `wang-2024-b` is that of a different work. Three
items are bundle sources: [24] [Wang et al. (2024)](/sources/wang-2024.md),
[55] [Chapelier et al. (2024)](/sources/chapelier-2024.md) and [64]
[Krais et al. (2021)](/sources/krais-2021.md). [19] and [37] print an
author as "D.C. D.R. Fernández"; [15] prints the venue "AIAA Paper 2
(2006)"; [16] is an arXiv preprint; [4], [6], [7] print no venue beyond
DOI and pages, [17] no volume or pages; [32] is a Los Alamos report. No
item is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Pressure dilatation](/definitions/pressure-dilatation.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
- [FLEXI](/software/flexi.md)
