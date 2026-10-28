---
type: Source
title: "Cheng et al. (2023) — An accurate and practical numerical solver for simulations of shock, vortices and turbulence interaction problems"
description: "OpenFOAM finite-volume implicit-LES solver with AUSM+-up fluxes and ROUND normalised-variable reconstruction recast as a compact flux limiter; two low-dissipation parameter sets beat van Leer and MUSCL limiters on shock, vortex and Taylor–Green tests and on deep-cavity Reynolds stresses."
resource: "doi:10.1016/j.actaastro.2023.04.049"
source_kind: paper
authors: [Cheng L., Deng X., Xie B.]
year: 2023
venue: "Acta Astronaut. 210:1–13"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Acta_Astronautica_Cheng_An_accurate_and_practical_numerical_solver_for_simulations_o.pdf"
tags: [implicit-les, shock-capturing, numerical-dissipation, finite-volume, compressible]
timestamp: 2026-10-27T21:10:00Z
---

# Summary

Cheng et al. (2023) build a compressible finite-volume solver in
[OpenFOAM](/software/openfoam.md) for shock–vortex and shock–turbulence
problems, run as [implicit LES](/definitions/implicit-les.md): no explicit
subgrid model, the subgrid scales being "solved and stabilized by the
inherent [numerical dissipation](/properties/numerical-dissipation.md)" of
the shock-capturing reconstruction. Citing Garnier et al., the authors
hold that explicit subgrid models do not suit
[shock–turbulence interaction](/results/shock-generated-turbulence.md):
they miss the intermodal energy transfer among acoustic, entropy and
vorticity modes and the kinetic-to-internal energy conversion at shocks.
The convective flux is AUSM+-up; face values of the primitive variables
come from Deng's ROUND normalised-variable reconstruction (a blend of the
third-order line into TVD bounding lines, introduced in Deng 2023), here
with two parameter sets, ROUND_A and the less dissipative ROUND_A+,
claimed TVD, low-dissipation and structure-preserving, and recast as a
flux limiter on a gradient ratio so that the stencil stays compact on
unstructured meshes. Unstructured high-order alternatives such as
[WENO](/methods/weno-scheme.md) are called too complex for practical
codes.

Against the van Leer and MUSCL limiters the ROUND schemes give smaller
errors and finer structures on an isentropic vortex (second-order
convergence where the limiters fall short), the Shu–Osher problem, a 2-D
shock/entropy wave, a shock/vortex interaction, the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) (lower
enstrophy and kinetic-energy dissipation; the central-flux
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
remark is cited), under-expanded planar jets and a shock-tube jet on a
triangular obstacle (triangular mesh). The only turbulence-statistics
validation is a Mach 0.8 deep cavity: classical limiters underestimate the
Reynolds stresses, ROUND improves them, and near the upstream wall ROUND
captures the peak of the in-plane fluctuation energy that the fifth-order
reference ILES of Thornber & Drikakis overestimates, on a finer grid
here. Evidence is numerical and mostly from figures; no time integrator,
CFL or cost is reported.

# Version read

Version of record (Elsevier; received 13 March 2023, revised 24 April,
accepted 28 April, online 6 May 2023), 13 pages, all read; page 3
(Eqs. 2.6, 2.9–2.13) read visually at 300 dpi. Page 1 matches the
metadata; no identity issue. Equation numbers are those of this version.

# Key claims

Page-local symbols: $\hat\phi$ a normalised variable of the
normalised-variable diagram (not a test filter), $\hat{\mathcal R}$ the
ROUND operator, $\gamma_0$, $\gamma_1$, $\lambda_1$ its dissipation
parameters, $\psi_{\mathrm{lim}}(r)$ the flux limiter of the gradient
ratio $r$, $M_s$ and $M_v$ shock and vortex Mach numbers, $L_{\mathrm{cav}}$
the cavity length.

1. Explicit SGS models are "not suited to shock-vortex and shock-turbulence problems": they cannot account for intermodal energy transfer among acoustic, entropy and vorticity modes and usually fail to capture the kinetic-to-internal energy conversion across shocks (§1, citing [19]). **Stated**
2. The dissipation of shock-capturing schemes can mimic standard SGS models; low-dissipation shock-capturing schemes are a more pragmatic ILES route than conventional TVD schemes (§1). **Stated**
3. Most TVD limiters over-dissipate (Minmod) or are unstable through excessive anti-dissipation (SuperBee); symmetric TVD schemes fail to reach uniform third order (§1). **Stated**
4. $k$-exact least-squares and unstructured WENO raise stencil, boundary and parallel-communication complexity, so high-order finite volumes on arbitrary unstructured grids are rare in practical codes (§1). **Stated**
5. ROUND_A ($\gamma_0=500$, $\gamma_1=1000$, $\lambda_1=0.25$) is low-dissipation and shape-preserving; ROUND_A+ ($\gamma_0=1100$, $\gamma_1=800$, $\lambda_1=0.15$) reduces dissipation further without losing structure preservation; both "also satisfy the TVD condition" (§2.2, Eq. 2.11). **Stated** (parameters by numerical tuning; no proof of the TVD property)
6. The reconstruction is recast as a limiter $\psi_{\mathrm{lim}}(r)$ with a Darwish–Moukalled gradient ratio, giving a compact stencil "algorithmically simple for parallel computation" (Eqs. 2.12–2.14). **Derived**
7. Isentropic vortex ($t=10$, meshes of 40–320 cells per side): ROUND preserves the vortex better with smaller accumulated density error (Eq. 3.1); "the convergence ratio of ROUND schemes are 2nd-order, while the vanLeer and MUSCL schemes cannot reach 2nd-order" (§3.1, Fig. 2). **Shown**
8. Shu–Osher problem ($h=1/600$, reference fifth-order WENO at $h=1/2000$): ROUND_A+ gives the high-frequency amplitude closest to the reference; low-frequency parts are nearly identical for all schemes (§3.2, Fig. 3). **Shown**
9. 2-D shock/entropy wave ($h=1/80$): ROUND resolves high-frequency density waves that van Leer and MUSCL "dampen … seriously" (§3.3, Fig. 4). **Shown**
10. Shock/vortex interaction ($M_s=1.5$, $M_v=0.9$, $h=1/300$): ROUND is competitive with a ninth-order reference, ROUND_A+ resolving the vortex splitting best (§3.4, Fig. 5). **Shown**
11. Inviscid Taylor–Green vortex ($128^3$, $t=10$): ROUND shows more small structures and enstrophy and kinetic-energy histories with "overall lower dissipation and better accuracy than classical TVD schemes" (§3.5, Figs. 6–7). **Shown**
12. Deep cavity ($M=0.8$, $Re=8.6\times10^5$ on $L_{\mathrm{cav}}=0.05$ m, 10.36 million cells, smallest $L_{\mathrm{cav}}/120$, 60 shedding cycles): mean velocities agree well with the experiment and mostly match the fifth-order ILES of Thornber & Drikakis, some better, which "may benefit from the finer grid size" (§3.6, Figs. 9–10). **Shown**
13. Deep cavity: "TVD schemes underestimate the Reynolds stresses due to numerical dissipation while the fifth-order MUSCL scheme tends to slightly overestimate them"; ROUND outperforms the two classical limiters (§3.6, Figs. 11–13). **Shown**
14. Deep cavity: the fifth-order scheme "significantly overestimated the turbulent kinetic energy close to the upstream wall, while ROUND schemes almost accurately capture the peak" of $(\langle u'^2\rangle+\langle w'^2\rangle)/U^2$ at $x/L_{\mathrm{cav}}=0.05$, 0.6, 0.95 (§3.6, Fig. 14). **Shown**
15. 2-D under-expanded planar jet (Mach 1.4): evolution comparable to a high-order WENO LES, finer vortical structures with ROUND (§3.7, Figs. 15–16). **Shown**
16. 3-D planar jet (Mach 1.8): van Leer "almost fails to produce 3D flow structures"; ROUND_A+ "is the only scheme that captures the early roll-up of the mixing layer" (§3.7, Fig. 17). **Shown**
17. Shock-tube jet on a triangular obstacle (primary shock Mach 1.57, triangular mesh): ROUND_A+ resolves reflections, triple points, Kelvin–Helmholtz instability and shock–vortex interaction, so the solver "can robustly handle irregular geometry" (§3.8, Figs. 19–20). **Shown** (qualitative)
18. The solver captures shocks without oscillation, resolves above-grid scales with low dissipation and stabilises "the under-resolve isotropic sub-grid scale" (§4). **Stated**

The ROUND operator (Eq. 2.11, as printed): for
$0<\hat\phi_C\le0.5$, $\hat{\mathcal R}=\min\big((\tfrac13+\tfrac56\hat\phi_C)\omega_0+2\hat\phi_C(1-\omega_0),\,2\hat\phi_C\big)$;
for $0.5<\hat\phi_C\le1$,
$\hat{\mathcal R}=\min\big((\tfrac13+\tfrac56\hat\phi_C)\omega_1+(\lambda_1\hat\phi_C-\lambda_1+1)(1-\omega_1),\,\lambda_1\hat\phi_C-\lambda_1+1\big)$;
otherwise $\hat{\mathcal R}=\hat\phi_C$; with
$\omega_{0,1}=[1+\gamma_{0,1}(\hat\phi_C-1)^4]^{-2}$. The face values are
then $\phi_f^L=\phi_C+\tfrac12\psi_{\mathrm{lim}}(r_f^L)(\phi_C-\phi_D)$ as
printed (Eq. 2.14; see Printed slips).

# Printed slips

- **Eq. (2.13):** the second branch contains a symbol $\beta_2$ defined nowhere. With $\hat\phi_C=r/(1+r)$ and the normalised form of the limited reconstruction, the second branch of Eq. 2.11 reproduces Eq. 2.13 when $\beta_2=\gamma_1$ *(compiler check, not in the sources)*.
- **Eq. (2.11) against Eq. (2.13):** the polynomials $B=\gamma_0(0.5-0.5r)^4+(1+r)^4$ and $D=\gamma_1(1-r)^4+16(1+r)^4$ of Eq. 2.13 correspond to weights $[1+\gamma_{0,1}(\hat\phi_C-0.5)^4]^{-2}$, since $(r/(1+r)-0.5)^4=(0.5-0.5r)^4/(1+r)^4$, not to the printed $[1+\gamma_{0,1}(\hat\phi_C-1)^4]^{-2}$; with the former both branches of Eq. 2.13 agree identically with Eq. 2.11 *(compiler check, not in the sources)*. The paper does not state which weight its code uses with the quoted $\gamma_0$, $\gamma_1$.
- **Eq. (2.14):** $\phi_f^L=\phi_C+\tfrac12\psi(r_f^L)(\phi_C-\phi_D)$, $\phi_f^R=\phi_D+\tfrac12\psi(r_f^R)(\phi_D-\phi_C)$. For linear data Eq. 2.12 gives $r_f^L=1$ and Eq. 2.13 gives $\psi(1)=1$, so the printed formula gives $\phi_C+\tfrac12(\phi_C-\phi_D)$, extrapolating away from $D$, instead of the value $\tfrac12(\phi_C+\phi_D)$ of the linear data at a face midway between the centres *(compiler check, not in the sources)*.
- **Eq. (2.6):** $\frac{d}{dt}\int_\Omega\overline{\mathbf U}dV$ is added to flux terms divided by $|\Omega|$. The first term then carries one more factor of volume than the flux terms *(compiler check, not in the sources)*.
- **Eq. (2.5):** $\tau=2\mu\mathbf S-\frac23\mu(\nabla\cdot\mathbf u)$ is printed without an identity tensor on the second term.
- **Eq. (3.3):** the post-shock region is printed "$0\le x\le-4$" on the domain $[-5,5]$.
- **§3.8:** the driven section is called "atmospheric", and "The initial static pressure in the driven section is 8.84 bar"; the section title names a cone, the computation a 2-D isosceles right triangle; $D$ in $h=D/128$ is not defined.
- **§3.4:** $v_\phi$ is called "angular velocity" while Eq. 3.4 gives a tangential velocity.
- **§3.6:** "TVD schemes" sometimes includes ROUND, sometimes only van Leer and MUSCL; Fig. 11 caption calls the reference scheme "fifth-order MUSCL", MUSCL also being a second-order comparison limiter.
- Typos: "Godnunov's theorem" (§1); "$\Omega_c$" for $\Omega_C$ (§2.1); abstract "the multi-scale raised in".
- References [7] and [25] are the same Godunov (1959) paper with different title translations.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline{\mathbf U}$ | (cell average, page-local) | **collision:** not the LES filter |
| $\rho$, $\mathbf u$, $p$, $E$, $\gamma$ | $\rho$, $u_i$, $p$, $E$, $\gamma$ | $E$ per unit volume |
| $\mathbf S$ | $S_{ij}$ | |
| $\tau$ | $\sigma_{ij}$ | **collision:** viscous stress, not the SGS stress |
| $k$ | (thermal conductivity, page-local) | **collision** with the TKE |
| $\Omega$, $\lvert\Omega\rvert$ | (cell and its volume, page-local) | **collision** with $\Omega_{ij}$ |
| $h$ | $h$ | uniform cell size |
| $\hat\phi$, $\hat{\mathcal R}$ | $\hat\phi$, $\hat{\mathcal R}$ (page-local) | **collision:** hat is not the test filter here |
| $\gamma_0$, $\gamma_1$, $\lambda_1$, $\omega_0$, $\omega_1$ | (ROUND parameters and weights, page-local) | not the ratio of specific heats $\gamma$, the Taylor microscale $\lambda$ or the specific dissipation rate $\omega$; the WENO page writes them $g_0$, $g_1$, $\lambda_{\mathrm R}$, $\mathsf b_0$, $\mathsf b_1$ (and $\hat\phi$ as $\phi_{\mathrm n}$) |
| $\psi(r_f)$ | $\psi_{\mathrm{lim}}(r)$ (page-local) | **collision** with the $k$-$\sqrt kL$ surrogate $\psi$ |
| $A$, $B$, $C$, $D$ (Eq. 2.13) | (auxiliary polynomials) | $C$, $D$ are also cell labels |
| $\overline{u'^2}$, $\overline{u'w'}$, $\overline{w'^2}$ | $\langle u'^2\rangle$, $\langle u'w'\rangle$, $\langle w'^2\rangle$ | **collision:** overbar is the time average; components named as printed |
| $L$ | $L_{\mathrm{cav}}$ (page-local) | **collision** with the integral scale |
| $Q$ | (Q-criterion iso-value 0.15) | |
| $M_s$, $M_v$ | $M_s$, $M_v$ (page-local) | |

# Reference list

52 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug; the
printed duplicate [7]/[25] (Godunov 1959) is one entry. Ref [37] is the
ingested [deng-2022](/sources/deng-2022.md). Several cited works share
keys with different works already in the bibliography (Deng 2019, 2020
and 2023, Zhang 2015, Thornber 2008) and were matched by venue. [47]
prints no volume, [51] no venue, [52] no volume or pages; [17] and [18]
are AIAA papers with paper numbers printed as pages; [45] is printed with
year 2002.

# Pages created or updated

Chunk 11 (2026-10-27). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
- [OpenFOAM](/software/openfoam.md)
