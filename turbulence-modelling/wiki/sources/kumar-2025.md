---
type: Source
title: "Kumar et al. (2025) — Delayed detached-eddy simulations of NACA wing sections using spectral elements"
description: "Implements a k-τ SST delayed detached-eddy simulation in the spectral-element code Nek5000, verifies it on the NASA flat plate and NACA 0012, and studies sample size, span and grid convergence for NACA 0021 and NACA 0012 stall up to 90°, including wind-tunnel confinement."
resource: "doi:10.1080/14685248.2025.2608679"
source_kind: paper
authors: [Kumar V., Tomboulides A., Fischer P., Min M.]
year: 2025
venue: "J. Turbul. 26:354-381"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Turbulence_Kumar_Delayed_detached-eddy_simulations_of_NACA_wing_sections_usin.pdf"
tags: [des, hybrid-rans-les, spectral-element, rans, separated-flow, high-order]
timestamp: 2026-10-29T05:08:00Z
---

# Summary

Kumar et al. (2025) implement SST-type RANS and a delayed
[detached-eddy simulation](/methods/detached-eddy-simulation.md) in
[Nek5000](/software/nek5000.md), a
[continuous-Galerkin spectral-element](/methods/spectral-element-method.md)
code, on the [$k$-$\tau$ SST model](/methods/k-tau-model.md) of
[Tomboulides et al. (2025)](/sources/tomboulides-2025.md), with
$\tau_t=1/\omega$. The motivation: $\omega$ is singular at walls
($\omega\sim d^{-2}$) and the large wall value used in low-order codes of
the [$k$-$\omega$ family](/methods/k-omega-model.md) causes persistent
oscillations in high-order codes, whose
[numerical dissipation](/properties/numerical-dissipation.md) is
negligible; $\tau_t$ vanishes at the wall and needs no wall distance for
its boundary condition. The authors claim the first DDES in a
spectral-element code built on $k$-$\tau$.

Verification on the NASA TMR zero-pressure-gradient flat plate
([turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md),
$Re_L=5\times10^6$) covers $N$- and wall-spacing convergence for $k$-$\tau$
SST and a regularized [$k$-$\omega$ SST](/methods/k-omega-sst-model.md);
the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re_c=6\times10^6$
and angles of attack 0°, 10° and 15° agrees with CFL3D
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) data within 5%.
In three dimensions, NACA 0021 at 60° and $Re_c=2.7\times10^5$ sets the
statistical sample: 600 convective time units bring the running mean of
$C_L$ within 0.2%, and ±2% is reached in 100–150 units. NACA 0012 DDES at
$Re_c=2\times10^6$ from 5° to 90° is grid-converged on the coarsest grid
(0.8M degrees of freedom), one level coarser than a second-order IDDES of
Bidadi et al., and under-predicts post-stall drag against wall-corrected
experiments by up to 11% at 90°. DDES inside the wind-tunnel cross-section
raises the 90° drag by up to 13% and matches the uncorrected experimental
drag within 5%, which the authors read as a call to re-assess empirical
wall corrections. Element-interface artefacts in $Q$ vanish under a
[gradient-jump penalty](/methods/jump-penalty-stabilization.md) without
changing the forces. An appendix sets out the Nek5000 numerics and a
high-pass-filtered relaxation-term LES model built on a modal filter
([explicit modal filtering](/methods/explicit-modal-filtering.md),
[LES](/definitions/large-eddy-simulation.md)), not used in the runs shown.
The introduction motivates [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
by the cost of resolved LES and DNS
([grid-point requirements](/results/les-grid-point-requirements.md)).

# Version read

Version of record (Taylor & Francis, with a cover page; received 25
September 2024, accepted 5 December 2025, online 8 January 2026, issue
vol. 26 nos. 10–11, 2025), 29 PDF pages (cover plus journal pp. 354–381),
all read; equation pages 357–359 and the appendix (pp. 377–380) read
visually because the text layer drops $\Gamma$, primes and other symbols.
Page 1 matches the metadata; no identity issue. Equation, figure, table
and section numbers are those of this version.

# Key claims

Page-local symbols: $\omega_w$, $\omega'$ the singular and regular parts
of $\omega$ in the regularized $k$-$\omega$ model; $R_\mu=\max(0.01\mu,\mu_t)$
the denominator of the free-stream limiter (the factor $\mu_t/R_\mu=\min(1,\mu_t/(0.01\mu))$ is the $R_{\mathrm{fs}}$ of the Tomboulides et al. page with $r=0.01$, *compiler check, not in the sources*); $\sigma_d$
the cross-diffusion coefficient; $N_{\mathrm{dof,tot}}$ the total degrees
of freedom of a mesh (registry $N_{\mathrm{dof}}$ is per element); $E$
the number of elements; $h_{\max}$ the longest element edge (registry $h$; the DDES grid scale is $h_{\max}/N$); $\Delta y_{\min}=\Delta y_{e,1}/N$ the averaged
first spacing; CTU the convective time unit $c/U_\infty$; $\chi_f$,
$m$ the relaxation strength and the number of filtered modes of the HPF
model (registry §11 $\chi_f$).

1. Close to walls $\omega$ scales as $d^{-2}$, making $\omega$ and its gradient singular; the arbitrarily large wall value of "standard CFD practice" can lead to persistent oscillations in high-order codes because of their negligible numerical diffusion (§1, citing [9], [10]). **Stated**
2. The regularized $k$-$\omega$ model of Tomboulides et al. [10] splits $\omega=\omega_w+\omega'$, giving a zero Dirichlet condition for $\omega'$ but requiring the wall distance and its gradients in additional source terms; $k$-$\tau$ needs neither regularization nor wall distance for its boundary condition (§1, §5). **Stated**
3. Choosing $g=\sqrt{\tau_t}$ (Benton et al. [13]) makes the source terms unbounded near the wall, whereas for $\tau_t$ they remain bounded (Kok & Spekreijse [14]); $\tau_t\sim d^2$ near the wall (§1). **Stated**
4. The work is, "to the best of our knowledge", the first implementation of DDES in a spectral-element solver based on the $k$-$\tau$ model (§1). **Stated**
5. The $k$-$\tau$ SST model is Eqs. (3)–(18), with the free-stream limiter multiplying the production, dissipation and transport terms of the $\tau_t$ equation by $\mu_t/R_\mu$ so that $k_\infty=0$ can be prescribed (§2.1, §2.1.1, Eq. 19). **Stated** (model description, implementation per [27])
6. The $k$-$\tau$ SST DDES uses $l_{\mathrm{DDES}}=l_{\mathrm{RANS}}-f_d\max(0,l_{\mathrm{RANS}}-l_{\mathrm{LES}})$, $l_{\mathrm{LES}}=C_{\mathrm{DES}}h_{\max}/N$ with $h_{\max}$ the largest spectral-element edge, $l_{\mathrm{RANS}}=\sqrt k\,\tau_t/C_\mu$, $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$, and $C_{d1}=20$, $C_{d2}=3$ in $f_d$ (§2.2, Eqs. 20–28). **Stated**
7. Time integration is semi-implicit BDF3/EXT3 splitting with characteristics-based time stepping permitting high CFL (CFL 3.0 for most cases); the pressure Poisson equation is solved by GMRES with a $p$-multigrid preconditioner (§2.2). **Stated**
8. Flat plate, $Re_L=5\times10^6$, $k$-$\tau$ SST: mean velocity and eddy viscosity at $x/L=0.97$ converge at $N=16$, with small $F_2$ differences between $N=8$ and 16 near the boundary-layer edge; converged profiles agree with the TMR CFL3D $k$-$\omega$ SST data (§3.1.2, Fig. 2). **Shown**
9. Mean friction and drag coefficients differ by less than 0.5% between $N=4$ and $N=16$, similar to SA in CFL3D/FUN3D and better than $k$-$\omega$ SSTVm in the same codes (§3.1.2, Fig. 3). **Shown**
10. Wall-spacing convergence: $C_D$ oscillates for $\Delta y^+_1>1.5$ for both Nek5000 models; the regularized $k$-$\omega$ SST converges like SA in CFL3D as the wall is refined, while $k$-$\tau$ SST keeps an oscillatory convergence (greater aspect-ratio sensitivity); values stay within 1% of other models (§3.1.3, Fig. 4). **Shown**
11. NACA 0012, $Re_c=6\times10^6$, 0°/10°/15°: $k$-$\tau$ SST $C_p$ and $C_f$ agree with CFL3D SA data, with a slight under-prediction of the suction pressure at 15° attributed to compressibility in CFL3D (§3.2.2, Fig. 6). **Shown**
12. Lift and drag differ from CFL3D by less than 5%: $C_L=1.05$ (10°), 1.45 (15°); $C_D=0.008$, 0.013, 0.023 at 0°/10°/15°; the experimental $C_D=0.018$ at 15° differs by about 20%, as does CFL3D, attributed possibly to RANS limits in strong adverse pressure gradient (§3.2.2, Table 3). **Shown**
13. On the 1c-span NACA 0021 ($Re_c=2.7\times10^5$, 60°), about 600 CTU bring the running mean of $C_L$ within 0.2% of the mean, about one-third of the time of the fully implicit lower-order code of Garbaruk et al. [23] (§4.2, Fig. 7b). **Shown**
14. Garbaruk et al.'s relaxed 500-CTU criterion corresponds to ±2% of the mean $C_L$, reached here in the first 100–150 CTU; for larger domains the requirement is much lower; the paper averages at least 200 CTU on the 4c span and states a ±2% sampling error (§4.2). **Shown**
15. All data sets (present, NTS DES of [23], experiment of [56]) give the primary shedding at $St=fc\sin\alpha/U_\infty\approx0.19$ (projected chord) and its harmonics; fluctuations on the wide domain are suppressed (§4.2, Fig. 7c). **Shown**
16. NACA 0021 mean forces: narrow span $C_L=1.0$, $C_D=1.76$; wide span $C_L=0.89$, $C_D=1.48$; experiment (Swalwell et al.) $C_L=0.93$, $C_D=1.51$ (below 5% in lift and 2% in drag for the wide span); almost 7% drag difference from the NTS DES ($C_L=0.88$, $C_D=1.38$ on 4c) (§4.2). **Shown**
17. The drag difference is attributed to sampling: the $C_D$ histograms are skewed to large values, and explicit or semi-implicit stepping with much smaller $\Delta t$ captures extreme events; an average $\Delta t\approx7\times10^{-5}$ gives about 8.5M samples against about 75 000 for NTS with $\Delta t=0.02$ (§4.2, Fig. 7d). **Shown** (histogram) / **Stated** (explanation)
18. $Q$-criterion fluctuations at element interfaces stem from the $C^0$ continuity of the spectral-element method; a gradient-jump penalty at 45° on the fine grid removes them without changing the main structures and gives nearly identical $C_L$, $C_D$ histories, so they are "merely a cosmetic issue" (§4.3.1). **Shown** (results not in figures)
19. NACA 0012 DDES at $Re_c=2\times10^6$: 5° and 17° stay fully attached, 17° near maximum lift; beyond 17° the flow separates massively, the separated region at 90° extending more than three chords (§4.3.1, Fig. 10). **Shown**
20. Differences among the Coarse, Medium and Fine grids are minimal even at high angles, so the Nek5000 DDES is grid-converged at the Coarse level, whereas Bidadi et al. [26] (second-order finite-volume Nalu-Wind IDDES) converged at Medium; attributed to high-order convergence (§4.3.2, §5, Fig. 11). **Shown**
21. Converged results agree well with Bidadi et al. in lift and drag at all angles; Strelets's DES ($Re_c=10^5$, 1c span) is consistently higher post-stall, attributed to the lower Reynolds number and narrower span (§4.3.2). **Shown**
22. Below stall $C_L$ and $C_D$ agree with the upper experimental envelope; post-stall drag is increasingly under-predicted relative to the wall-corrected experiments, by at most about 11% at 90° (§4.3.2). **Shown**
23. Confined DDES (tunnel cross-section $15c\times6c$, as Critzos et al.) at 90°: the unconfined $C_D$ varies by about 2% over $Re_c=0.1$–$2\times10^6$, the confined one rises by about 5% over that range and is consistently higher, by up to about 13% at $Re_c=2\times10^6$, trending toward the flat-plate value $C_D\approx2$ (Hoerner) (§4.4.2, Fig. 14). **Shown**
24. At $Re_c=2\times10^6$ the confined run agrees with the raw Critzos et al. drag within 5%, while the unconfined run differs from the corrected Critzos value by about 11%; corrected high-$Re$ experiments over-predict the unconfined drag by more than 7%; the authors call for a re-assessment of wind-tunnel wall-correction methods (§4.4.2, §5). **Shown** / **Stated** (interpretation)
25. The closed trailing edge limits CFL to 3.0; a curved trailing edge would permit higher CFL, with an order of magnitude higher CFL as the target; overlapping meshes instead of mono-domain meshes are planned for confined cases (§5). **Stated**
26. Performance tests (not reported) show excellent solver convergence and parallel performance, detailed in the companion ANL report [57] (§4.3). **Stated**

The model in registry notation. The $k$ equation of the DDES is
$\partial_t(\rho k)+\nabla\cdot(\rho k\boldsymbol u)=\nabla\cdot(\Gamma_k\nabla k)+P_k-\rho k^{3/2}/l_{\mathrm{DDES}}$
(Eq. 20), with $P_k=\min(\mu_t|S|^2,10\rho\beta^*k/\tau_t)$ (the
normalization of the printed $S$ is not stated) and $\mu_t=\rho k\tau_t$
in what §2.1 calls the "standard $k-\tau$ model" (Eqs. 7–10). The $\tau_t$ equation of the SST form
(Eq. 11) is
$$\partial_t(\rho\tau_t)+\nabla\cdot(\rho\tau_t\boldsymbol u)=\nabla\cdot(\Gamma_\omega\nabla\tau_t)-\gamma_\omega\frac{\rho}{\mu_t}\tau_t^2P_k+\rho\beta_\omega-2\frac{\Gamma_\omega}{\tau_t}\rho\,\nabla\tau_t\cdot\nabla\tau_t+C_{D_\tau}+2(1-F_1)\rho\sigma_{\omega2}\tau_t\nabla k\cdot\nabla\tau_t,$$
with the Kok–Spekreijse cross diffusion
$C_{D_\tau}=\rho\sigma_d\tau_t\min(\nabla k\cdot\nabla\tau_t,0)$,
$\sigma_d=1/8$ (Eq. 6), $\mu_t=\rho a_1k/\max(a_1\tau_t^{-1},F_2|S|)$
(Eq. 12), and $F_1$, $F_2$ written with $\tau_t$ (Eqs. 13–17). Constants
(Eq. 18): $\gamma_{\omega1}=5/9$, $\beta_{\omega1}=0.075$, $\sigma_{k1}=0.85$,
$\sigma_{\omega1}=0.5$; $\gamma_{\omega2}=0.44$, $\beta_{\omega2}=0.0828$,
$\sigma_{k2}=1$, $\sigma_{\omega2}=0.856$; $C_\mu=0.09$, $\kappa=0.41$,
$a_1=0.31$ (Eq. 27). The shielding function is
$f_d=1-\tanh[(C_{d1}r_d)^{C_{d2}}]$,
$r_d=(\nu_t+\nu)/\big(\kappa^2d^2\sqrt{0.5(S^2+\Omega^2)}\big)$ with $S$,
$\Omega$ the strain and vorticity magnitudes (Eqs. 25–26); only the $k$
equation is modified. *(Compiler check, not in the sources: with
$\mu_t=\rho k\tau_t$, $\rho\tau_t^2/\mu_t=\tau_t/k$, so the production
terms of Eqs. 4 and 11 agree; with $\omega=1/\tau_t$, the SST
cross-diffusion $2(1-F_1)\rho\sigma_{\omega2}\nabla k\cdot\nabla\omega/\omega$
that the paper prints in App. A.5 becomes the last term of Eq. 11. Eq. 11 keeps both $C_{D_\tau}$ and the
SST term as printed.)* The HPF model of App. A.4 filters the Legendre
coefficients with $\hat G_k=((m-i)/m)^2$ for $k=N-m+i$ and adds a
relaxation term $-\chi_f(u-\bar u)$, with $\chi_f=5$.

# Printed slips

- **§4, first sentence:** "five angle of attack values: 5°, 17°, 30°, 45°, 60° and 90°" lists six values; §5 says "AoA = 0 − 90°" while the simulated angles are 5–90°.
- **Eq. (2):** "$-\overline{u_i'u_j'}=\nu_t(\partial u_i/\partial x_j+\partial u_j/\partial x_i)-\tfrac23\rho k\delta_{ij}$": a kinematic stress with $\rho k$, and an unbarred velocity in the strain.
- **Eq. (12)** is introduced as "the kinematic eddy viscosity" but carries $\rho$.
- **Eq. (11):** the term "$-2\frac{\Gamma_\omega}{\tau}\rho\nabla\tau\cdot\nabla\tau$" carries a factor $\rho$ that Eq. (4) does not; $\Gamma_\omega=\mu+\mu_t/\sigma_\omega$ is already dynamic. Eq. (5) prints "$\Gamma\omega$" for $\Gamma_\omega$.
- **$\beta^*$** appears in Eqs. (3), (9), (14), (17) with no value printed; App. A.5 writes the production limiter with $C_\mu$.
- **App. A.5:** "$k=(1/2)(\langle u'\rangle+\langle v'\rangle+\langle w'\rangle)$" without squares, and "ω is the rate of dissipation of TKE", while §1 calls $\omega$ the specific dissipation rate.
- **Eq. (30):** "$C_f=\tau_w/(0.5\rho_0U_0^2L_0)$" with $L_0$ in the denominator, while Eq. (32) gives $C_f=\tau_w/(0.5\rho_0U_\infty^2)$; the Fig. 4 caption says "$L_0=1$ has been used" whereas the text sets $L_0\equiv2L$.
- **§3.1.3:** "The degrees of freedom in the final mesh remains the same ($N_x\times N_y\equiv257\times97$) as that used by NASA's CFL2D and FUN3D" ("CFL2D" for CFL3D). *(Compiler check, not in the sources: for $E=37\times16$ at $N=6$, $(37\cdot6+1)(16\cdot6+1)=223\times97=21\,631$, the value of Table 1, not $257\times97$.)*
- **Fig. 2 caption:** "solid line: N = 24", while Table 1 lists $N=2$, 4, 8, 16 only; the Fig. 3 caption has "x/c = 0.97" for the flat plate ($x/L$ in the text).
- **§4.2:** Swalwell et al. "used a span of 7.2c" and, later, "domain size 0.72c"; the text calls Fig. 7(d) a histogram of $C_d$, the caption "(d) histogram (percent occurrence) of $C_l$", with "±σ($C_d$)" lines.
- **§4.4.1:** "The boundary on the left assumes uniform inflow (0, 0, 0)".
- **App. A.4:** Eq. (A10) is printed without the relaxation term that the text says is added to it, and $\mathcal H_N$, $\chi$ refer to symbols absent from (A10); "we take $m=0$" stands beside "only affects the last mode". *(Compiler check, not in the sources: with the printed weights, $\sigma_k=1$ for $k\le N-m$, so $m=0$ filters no mode.)*
- **App. A.2, A.5.1:** $\gamma$ in Eq. (A4), and $\tilde rf(\tilde r)$ and $\alpha^*$ in Eq. (A31), are not defined.
- **Attributions:** §2.2 credits $f_d$ to "[19]" (Strelets 2001, "Detached eddy simulation of massively separated flows") and the shielding to "[6]" (Menter, Kuntz & Langtry 2003, "Ten years of industrial experience with the SST turbulence model"); ref. [7] (Spalart et al. 2006, "A new version of detached-eddy simulation, resistant to ambiguous grid densities") is cited only for grid-induced separation. §3.2.2 cites "the Spallart–Allmaras model" to ref. [51], printed as Spalart & Ferziger (1992), "Numerical studies of natural transition in a decelerating boundary layer". The SST variant is cited to [6], with Menter (1994) as [34].
- **References:** [69] and [70] are the same paper (Stolz, Schlatter & Kleiser 2005, same DOI) with different page fields; ref. [3] prints an issue-level DOI; refs. [43] and [73] have garbled venues.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar u_i$, $u_i'$ | $\langle u_i\rangle$, $u_i'$ | overbar is a Reynolds average here |
| $\overline{u_i'u_j'}$ | $R_{ij}$ | |
| $\tau=1/\omega$ | $\tau_t$ (registry §11) | **collision:** not a stress |
| $g=\sqrt\tau$ | $\sqrt{\tau_t}$ | Benton et al. variable, discussed only |
| $k$, $\omega$, $\mu_t$, $\nu_t$ | $k$, $\omega$, $\mu_t$, $\nu_t$ | |
| $\Gamma_k$, $\Gamma_\omega$ | $\Gamma_k$, $\Gamma_\omega$ (registry §11) | |
| $\alpha$, $\beta$, $\beta^*$, $\sigma_k$, $\sigma_\omega$ | $\gamma_\omega$, $\beta_\omega$, $\beta^*$, $\sigma_k$, $\sigma_\omega$ | registry §11 for $\gamma_\omega$, $\beta_\omega$ |
| $S$, $\Omega$ | $\lvert S\rvert$, $\lvert\Omega\rvert$ | normalization not printed |
| $R$ | $R_\mu$ (page-local) | **collision** with $R_{ij}$ |
| $d$, $y_d$, $y_w$ | $d$ | wall distance |
| $l_{\rm RANS}$, $l_{\rm LES}$, $l_{\rm DDES}$, $C_{\rm DES1}$, $C_{\rm DES2}$ | $l_{\mathrm{RANS}}$, $l_{\mathrm{LES}}$, $l_{\mathrm{DDES}}$, $C_{\mathrm{DES}}$ | as on the DES page |
| $h_{\max}$ | $h_{\max}/N$ (page-local $h_{\max}$ the longest element edge) | the source's $h_{\max}$ is the largest element edge over $N$ (§2.2); largest cell edge (App. A.6) |
| $f_d$, $r_d$, $C_{d1}$, $C_{d2}$ | $f_d$, $r_d$ (registry §11), $C_{d1}$, $C_{d2}$ | |
| $N$, $E$ | $N$, $E$ (page-local) | polynomial degree; element count |
| $N_{\rm dof}$ | $N_{\mathrm{dof,tot}}$ (page-local) | total, not per element (registry $N_{\mathrm{dof}}$) |
| $y_n^+$, $\Delta y_{\min}$ | $\Delta y^+_1$, $\Delta y_{\min}$ (page-local) | |
| $Re_L$, $Re_c$, CTU | $Re_L$, $Re_c$, CTU (page-local) | |
| $C_l$, $C_d$, $C_f$, $C_p$ | $C_L$, $C_D$, $C_f$, $C_p$ | |
| AoA, $\alpha$ | angle of attack (in words) | **collision** with the DG blending $\alpha$ |
| $Q=0.5(\lVert\Omega\rVert^2-\lVert\mathbf S\rVert^2)$ | $Q$ | $Q$-criterion |
| $\hat u$, $\hat\tau_{ij}=\widehat{u_iu_j}-\hat u_i\hat u_j$ | $\bar u$, $\tau_{ij}$ | App. A.3: the hat is the LES filter, not a test filter |
| $\chi$, $\mathcal H_N$, $\mathcal F_N$, $\sigma_k$, $m$ | $\chi_f$ (registry §11), (page-local), $\hat G_k$, $m$ (page-local) | HPF relaxation model |
| $\kappa$ | $\kappa$ | 0.41 |

# Reference list

75 printed references, numbered style ([1]–[75]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Ref. [27] is the ingested [Tomboulides et al. (2025)](/sources/tomboulides-2025.md);
ref. [14] (Kok & Spekreijse, NLR report) is an entry already in the
bibliography. Printed duplicate: refs. [69] and [70] are the same work and
are folded into one entry. Three cited works share a key with a different
work already in the bibliography and are keyed `kumar-2023-b`, `kumar-2024-b` and `wang-2025-b` respectively: ref. [44]
(Kumar et al., ANL report on turbulence modelling in Nek5000/RS, SOD2D and
Alya; not the ingested Kumar et al. (2023) combustion paper), ref. [57]
(Kumar et al., ANL report on hybrid RANS–LES of NACA 0012) and ref. [15]
(Wang S. et al., $\ell^2/g^2$ hybrid RANS/LES in spectral elements, Phys.
Rev. Fluids). Refs. [28] (Nek5000), [48] (NASA TMR) and [65] (Pointwise)
are software or web resources, the last two undated; [23] is a chapter
of the DESider volume; [37] prints the book title in the title position;
[43] and [73] have garbled venues; [54], [55], [62], [63] are reports
without printed institution.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [Hybrid RANS/LES](/definitions/hybrid-rans-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [Explicit modal filtering as an LES closure](/methods/explicit-modal-filtering.md)
- [Jump-penalty stabilization of high-order methods](/methods/jump-penalty-stabilization.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [The k-τ model](/methods/k-tau-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nek5000 and NekRS](/software/nek5000.md)
