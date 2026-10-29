---
type: Source
title: "Bulgarini et al. (2025) — p-Multigrid high-order discontinuous Galerkin solver for three-dimensional compressible turbulent flows"
description: "Nonlinear p-multigrid (FAS, full multigrid V-cycle) for a modal DG discretization of steady compressible RANS with a log-ω Wilcox k-ω model: logarithmic variables, automatic smoothing counts, level-dependent CFL and GMRES settings, finest-level turbulence source; 50–95% time savings over single-order implicit solves on eight 3D cases."
resource: "doi:10.1016/j.jcp.2025.113766"
source_kind: paper
authors: [Bulgarini D., Ghidoni A., Mantecca E., Noventa G.]
year: 2025
venue: "J. Comput. Phys. 525:113766"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Journal_of_Computational_Physics_Bulgarini_p-Multigrid_high-order_discontinuous_Galerkin_solver_for_thr.pdf"
tags: [dg, rans, k-omega, high-order, turbomachinery, high-lift]
timestamp: 2026-10-28T17:46:00Z
---

# Summary

Bulgarini et al. (2025) improve a three-dimensional $p$-multigrid solver
for a modal discontinuous Galerkin discretization (BR2 viscous flux, exact
Riemann solver, orthogonal hierarchical basis in physical space; not the
nodal [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md))
of the steady compressible RANS equations closed with the Wilcox
[$k$-$\omega$ model](/methods/k-omega-model.md) written in
$\tilde\omega_\ell=\ln\omega$. The solver is the nonlinear Full
Approximation Scheme inside a Full Multigrid V-cycle. Six changes are
listed: logarithmic primitive variables ($\ln p$, $\ln T$,
$\tilde\omega_\ell$); automatic pre- and post-smoothing counts by a
modified residual criterion of Rueda-Ramírez et al.; a level-dependent
CFL law; level-dependent GMRES tolerance, Krylov dimension and iteration
cap; the turbulence-model source and the Jacobian computed on the finest
level only and restricted to the coarser ones; and skip conditions that
drop inaccurate coarse corrections. Three smoothers are compared
(block-implicit and line-implicit Runge–Kutta, linearized backward
Euler) against single-order implicit time integration with
matrix-explicit GMRES. Shock capturing is a residual-based directional
[artificial viscosity](/methods/artificial-viscosity-shock-capturing.md)
active everywhere "without the use of any [shock sensor](/definitions/shock-sensor.md)".

Cases: the ADIGMA BTC0 body and the VFE-2 65° [delta wing](/benchmarks/delta-wing-vortex-flow.md)
up to degree 6; the quasi-3D [backward-facing step](/benchmarks/backward-facing-step.md)
and the transonic [RAE 2822](/benchmarks/rae-2822-airfoil.md) up to
degree 3; the T106A [cascade](/benchmarks/turbine-cascade.md) (subsonic
and transonic), the DrivAer car (cited with the
[Ahmed body](/benchmarks/ahmed-body.md) as a reference geometry), the
NASA Trap-Wing of HiLift-1 (a different geometry from the
[NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) configuration)
and the DLR-F6. The line- and block-implicit smoothers work only with
degree 1 as the coarsest level, are fastest at degrees 2–3 and cut memory
by about 84–86%; the linearized backward Euler smoother allows a
free-stream start and is best above degree 3. Wall-clock reductions
against the single-order solver lie between about 50% and 95%. Flow
predictions agree with experiment and with reference RANS, among them
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) and SST results on
the step and the [laminar-kinetic-energy](/methods/laminar-kinetic-energy-transition-model.md)
$k_L$-$k$-$\omega$ results of Lorini et al. on the T106A; the DrivAer
literature cited includes [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
work. Evidence is numerical; the paper is about the solver, not the
closure.

# Version read

Version of record (Elsevier, open access CC BY; received 10 July 2024,
revised 10 December 2024, accepted 19 January 2025, online 22 January
2025), 29 pages, all read; Eqs. (4)–(5), (9), (17)–(18), the
shock-capturing term and Algorithm 1 checked visually on pages 3, 4 and 9.
Page 1 matches the metadata (title, four authors, venue, DOI). A
different paper of the same first author and year,
[Bulgarini et al. (2025b)](/sources/bulgarini-2025-b.md), is not cited
here. Numbering on this page is that of the version read.

# Key claims

Page-local symbols: MG level $l=1,\dots,l_{\max}$, level $l$ carrying
degree $N=l-1$ (Fig. 1); SO the single-order implicit solver; FMG the
full multigrid with fixed smoothing counts and a-FMG with automatic
counts; $\nu_{\mathrm{pre}}$, $\nu_{\mathrm{post}}$, $\nu_c$ the pre-,
post- and coarsest-level smoothing iterations; $N_{\mathrm{ite}}$ the
iterations to convergence; $t_{\mathrm{CPU}}$ the CPU time in units of
the TauBench time (10.32 s) and $\Delta t_{\mathrm{CPU}}$ its change
against SO; BIRK, LIRK, LBE the block-implicit RK, line-implicit RK and
linearized backward Euler smoothers.

1. FAS-FMG $p$-multigrid with an LBE smoother cuts wall-clock time by 50% to 95% against SO in all test cases, whatever the coarsest level (Conclusion (iv); Tables 3–11). **Shown**
2. The abstract states "an average reduction of the computing time around 75% with respect to single-order implicit solvers". **Shown** (no averaging procedure stated)
3. Only LBE permits a free-stream start (coarsest degree 0); BIRK and LIRK do not, "as proved by Ghidoni et al. [20,21,23] and Colombo et al. [6]", so the smoothers are compared with coarsest degree 1 (§6). **Stated** (cited)
4. BTC0 coarse mesh, coarsest degree 1: BIRK/LIRK is best at $N=2,3$ ("up to ∼75%"), LBE for $N>3$ ("up to ∼80%"); BIRK/LIRK3 is the most efficient BIRK/LIRK variant (e.g. $N=3$ BIRK/LIRK3 $-76.22\%$, $N=6$ LBE $-81.40\%$) (§6.1, Table 1). **Shown**
5. The stage count of BIRK/LIRK has limited influence for turbulent flows, "in contrast with Colombo et al. [6]", where more stages were best for laminar cases (§6.1). **Shown**
6. More smoothing iterations reduce $N_{\mathrm{ite}}$ while the wall time passes through a minimum; $\nu_{\mathrm{post}}$ matters more than $\nu_{\mathrm{pre}}$, $\nu_{\mathrm{post}}>2$ avoids instabilities in stiff problems; best values $\nu_{\mathrm{pre}}=1$, $\nu_{\mathrm{post}}=2$–5 for LBE and $\nu_{\mathrm{pre}}=\nu_{\mathrm{post}}=5$–10 for BIRK/LIRK (§6.1, Table 2). **Shown**
7. With $\nu_{\mathrm{pre}}=\nu_{\mathrm{post}}=1$ the LBE iteration count grows with $N$ (92 to 141 for $N=2$–6); the text gives "$53<N_{ite}<55$" with 50 smoothing iterations; "only a higher number of pre- and post-smoothing iterations allows to satisfy the $p$ independent condition, also known as asymptotic scalability" (§6.1). **Shown** *(Compiler check, not in the sources: Table 2 prints 53–55 only for BIRK/LIRK3 and 54–58 for LBE; see Printed slips.)*
8. The automatic smoothing count gives "a computational time comparable or lower than" fixed counts and can choose different counts per level (§6.1 Table 3, §6.2 Table 5, Conclusion (v)). **Shown**
9. BTC0: FMG cuts time "up to ∼78%" on the coarse mesh (832 hexahedra) and "∼63%" on the fine one (6656); the reduction grows with $N$ on the coarse mesh and shrinks on the fine one, explained by "the effectiveness of the FMG algorithm increases with the number of levels" (§6.1, Table 3). **Shown**
10. With LBE, coarsest degree 0 or 1 makes no difference to the time, which answers the concern that a degree-0 coarse problem is under-resolved (§6.1). **Shown**
11. VFE-2 delta wing: BIRK/LIRK cut the memory footprint by $-86.36\%$ at $N=2$ and $-83.96\%$ at $N=3$–6 against SO; LBE memory is "comparable" to SO because the finest-level data dominate (§6.2, Table 4). **Shown**
12. VFE-2: FMG cuts time "up to ∼83%" with GMRES tolerance $10^{-12}$ and "up to ∼92%" with $10^{-2}$; the looser tolerance speeds SO up by about 10% at low $N$ and destabilizes it at high $N$, so $10^{-12}$ is kept on the finest level from §7 on (§6.2, Table 5). **Shown**
13. Backward-facing step ($Re_h=28\,000$, $N=3$): $C_f$ and velocity profiles agree with Vogel & Eaton and with the SA and SST references, "without an underestimation of the skin friction coefficient in the attached turbulent boundary layer"; reduction "up to ∼82%" ($-81.22\%$, $-80.42\%$, $-71.03\%$) (§7.1, Fig. 5, Table 6). **Shown**
14. RAE 2822: reduction "up to ∼77%", decreasing only slightly with $N$; "the $p$-MG algorithm does not show any robustness issue with the shock" (§7.2, Table 7). **Shown**
15. T106A subsonic: up to about 90% (quasi-3D coarse, $N=3$: $-91.41\%$; 3D fine, $N=1$: $-90.99\%$); the text states that "the worst reduction … guarantees a saving of about 49%" (§8.1, Table 8). **Shown**
16. T106A: the $\tilde\omega_\ell$ residual converges last; on the quasi-3D coarse mesh at $N=3$ the reduction is 90.76% at convergence and "reduces to 95.01%" at an $L^2$ residual of about $10^{-3}$, FMG reaching quasi-convergence early (§8.1). **Shown**
17. T106A transonic: reduction "up to ∼95%" for all domains, meshes and degrees, without loss as $N$ rises (up to $-93.61\%$) (§8.1, Table 9). **Shown**
18. DrivAer: up to about 70% (coarse, 48 264 cubic hexahedra) and 60% (fine, 113 780), decreasing with $N$, performance "seems to be only DoFs dependent"; the $N=3$ solution agrees better with experiment than the $k$-$\omega$ RANS of Heft et al. (§8.2, Figs. 12–13, Table 10). **Shown**
19. NASA Trap-Wing: up to about 70%, decreasing with $N$; DLR-F6: up to about 60%, nearly constant in $N$ (§8.3, Table 11). **Shown**
20. With orthogonal hierarchical modal bases the $L^2$-projection restriction and prolongation reduce to selecting the low-order modes and zero-padding the high-order ones, and the residual restriction is the transpose of the prolongation (§4.3, Eqs. 19–24). **Derived**
21. Computing the turbulence source on the finest level only and freezing it on the coarser levels costs no extra memory and is "proposed for the first time in a high-order framework"; restricting the Jacobian with the Galerkin operator instead of reassembling it "does not have a negative influence on the robustness, but guarantees a huge reduction of the computational cost" (§1 (v), §4.2). **Stated** (no ablation shown)
22. Logarithmic $p$, $T$ and $\omega$ guarantee positivity of the thermodynamic state and a smoother solution, "of paramount importance for the robustness of the MG algorithm", claimed as their first use in a $p$-multigrid DG solver (§1 (i), §3). **Stated** (no ablation)
23. The preconditioner (block Jacobi with ILU(0), or additive Schwarz) has a "negligible" influence on FMG performance (§3). **Stated**
24. A matrix-free approach would save memory, "up to 36% for a $\mathbb P^6$ solution approximation, as shown in [29]" (§1). **Stated** (cited)
25. The element aspect ratio in boundary layers, shocks and wakes "does not seem to influence the performance of the algorithm" (Conclusion (vii)). **Shown** (indirectly; no controlled aspect-ratio study)
26. "The algorithm does not show an asymptotic scalability … the number of iterations to reach the convergence for each solution approximation is different" (Conclusion (i), Secs. 7–8). **Shown**

The model of §2 in registry notation (Eqs. 1–5, as printed), with
$\bar k=\max(0,k)$ in the eddy viscosity and the sources and
$\tilde\omega_{\ell,r}=\max(\tilde\omega_\ell,\tilde\omega_{\ell,r0})$ the
realizability-limited variable:
$$\begin{aligned}
\partial_t(\rho k)+\partial_j(\rho u_jk)&=-\rho R_{ij}\partial_ju_i-\beta^*\rho\bar k\,e^{\tilde\omega_{\ell,r}}+\partial_j\big[(\mu+\sigma^*\mu_t)\partial_jk\big],\\
\partial_t(\rho\tilde\omega_\ell)+\partial_j(\rho u_j\tilde\omega_\ell)&=-\frac{\gamma_\omega}{\bar k}\rho R_{ij}\partial_ju_i-\beta_\omega\rho\,e^{\tilde\omega_{\ell,r}}+\partial_j\big[(\mu+\sigma\mu_t)\partial_j\tilde\omega_\ell\big]\\
&\quad+(\mu+\sigma\mu_t)\partial_k\tilde\omega_\ell\,\partial_k\tilde\omega_\ell+\sigma_d\rho\,e^{-\tilde\omega_{\ell,r}}\max\big(\partial_kk\,\partial_k\tilde\omega_\ell,0\big),
\end{aligned}$$
with $\mu_t=\alpha^*\rho\bar k\,e^{-\tilde\omega_{\ell,r}}$ and the
Boussinesq stress $-\rho R_{ij}=2\mu_t(S_{ij}-\tfrac13\partial_ku_k\delta_{ij})-\tfrac23\rho\bar k\delta_{ij}$
(the source's $\tau_{ij}$, negative convention). The constants are "those
of the high- and low-Reynolds number model of Wilcox [30]"; no values are
printed, nor $\tilde\omega_{\ell,r0}$, $Pr$, $Pr_t$. $k$ may become
negative in the solution, which the authors attribute to poor accuracy
removed by refinement or higher degree. The turbulence source enters the
coarse levels only through the restricted residual: with the residual
split $\mathbf R=\mathbf R_f+\mathbf R_t$ (fluxes, turbulence source), the
two coarse $\mathbf R_t$ terms of the FAS smoothing step cancel (Eqs.
15–18), and the coarse Jacobian is the Galerkin restriction of the fine
one (Eq. 25). The smoothing criteria (Eqs. 26–27) compare the coarse
residual with the restricted fine residual, $\lVert\mathbf R^{l-1}\rVert_\infty<1.1\,\lVert\mathbf I^{l-1}_l\mathbf r^l\rVert_\infty$
before and $\le$ after; when they fail, the correction is skipped. The
artificial viscosity is
$\nu_{\mathrm{av}}=Ch_K^2\,(\lvert s_p\rvert+\lvert d_p\rvert)\,f_p/p$,
$f_p=\lvert\nabla_h\ln p\rvert h_K/N$, $C=0.2$, along the direction of
$\nabla_h\ln p$, with $s_p$ from interface flux jumps and $d_p$ from the
element divergence of the inviscid flux, as on the
[artificial-viscosity](/methods/artificial-viscosity-shock-capturing.md)
page for the same solver family.

# Printed slips

- **RAE 2822 Mach number:** the §7 introduction says "transonic flow around a RAE2822 airfoil … at Mach number M = 0.8", §7.2 "Mach number M = 0.725" (with $\alpha=2.92^\circ$).
- **§8.1:** "the worst reduction … guarantees a saving of about 49%", while the smallest reduction in Table 8 is $-53.09\%$ (3D fine, $N=3$).
- **§6.2:** "the computational time reduces between 81.95% and 61.61%" for tolerance $10^{-12}$; Table 5 prints $-61.64\%$ (FMG, $N=6$).
- **§6.1:** "$53<N_{ite}<55$ with $\nu_{pre}=1$ and $\nu_{post}=50$, or $\nu_{pre}=\nu_{post}=50$", while the LBE rows of Table 2 print 54, 56, 58, 58, 57 and 55, 57, 58, 58, 57; "Tables 1 and 2 show the performance … with the LBE and both coarsest levels", while both tables are captioned coarsest degree 1 and the degree-0 results are in Table 3.
- **$\Delta t_{\mathrm{CPU}}$ against the printed times.** *(Compiler check, not in the sources: with $\Delta t_{\mathrm{CPU}}=-(1-t_{\mathrm{FMG}}/t_{\mathrm{SO}})$, Table 3 coarse $N=1$: $1.87/4.54$ gives $-58.81\%$ (printed $-66.11\%$), a-FMG $1.58/4.54$ gives $-65.20\%$ (printed $-68.14\%$); Table 3 fine $N=6$: $5.16\times10^3/7.91\times10^4$ gives $-93.48\%$ (printed $-61.53\%$), a-FMG $5.01\times10^3/7.91\times10^4$ gives $-93.67\%$ (printed $-62.69\%$); Table 4 $N=4$ BIRK/LIRK5: $1.23\times10^3/3.52\times10^3$ gives $-65.06\%$ (printed $-69.94\%$); Table 9 quasi-3D fine $N=2$: $1.57\times10^2/3.48\times10^3$ gives $-95.49\%$ (printed $-93.14\%$), 3D fine $N=2$: $1.07\times10^4/1.37\times10^5$ gives $-92.19\%$ (printed $-90.03\%$); Table 10 coarse $N=3$: $5.78\times10^3/1.38\times10^4$ gives $-58.12\%$ (printed $-55.55\%$); Table 11 Trap-Wing $N=3$: $1.33\times10^5/3.96\times10^5$ gives $-66.41\%$ (printed $-64.01\%$), DLR-F6 $N=1$: $3.11\times10^3/9.05\times10^3$ gives $-65.64\%$ (printed $-62.59\%$).)*
- **Table 2:** the $N=2$ $t_{\mathrm{CPU}}$ column of BIRK/LIRK3 is identical to the LBE column in both blocks (13.3, 9.43, 7.46, 6.74, 7.80, 12.4 and 13.3, 8.80, 7.85, 8.69, 10.4, 16.8), while the $N_{\mathrm{ite}}$ differ.
- **Tables 1 and 2, same settings:** BIRK/LIRK3 $N=2$, $\nu=10/10$: 55 iterations and 6.02 (Table 1) against 54 and 8.69 (Table 2); LBE $N=6$, 1/5: 66 and $3.90\times10^3$ against 64 and $1.84\times10^3$; LBE $N=5$, 1/5: 65 and $6.38\times10^2$ against 64 and $5.25\times10^2$; BIRK/LIRK3 $N=3$, 1/5: 58 and $3.04\times10^1$ against 61 and $3.39\times10^1$. BTC0 coarse $N=5$ SO is $2.06\times10^3$ in Table 1 and $2.07\times10^3$ in Table 3.
- **Algorithm 5 (LBE)** prints the right-hand side $+\mathbf R^l(\mathbf W^l_n)$, Eq. (11) $-\mathbf R(\mathbf W^n)$.
- **§4 switch criterion** printed "TOL = max($\lVert c^l\rVert_2$) < $10^{-7}$", with $c^l$ undefined; §6 prints $\max(\lVert\mathbf R^l\rVert_2)$.
- **Attribution:** the model constants are credited to "Wilcox [30]", ref. [30] being Bassi, Crivellini, Rebay & Savini (2005); "BR2 scheme proposed by Bassi and Rebay [30]" names two of its four authors; no Wilcox work is in the list.
- **Symbol $\alpha$:** the CFL-law growth rate, the $\omega$-equation constant, the RK stage coefficients $\alpha_k$ and the angle of attack.
- **Unprinted values:** the CFL-law $\alpha$ and $n_{sf}$, $\nu_{\mathrm{pre,max}}$, $\nu_{\mathrm{post,max}}$, $\tilde\omega_{r0}$, the $k$-$\omega$ constants, $Pr$, $Pr_t$, the RK coefficients.
- **Typos:** "Additive Schwartz Method"; "the MG correction is kipped"; "DLR-F6 drom".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\tilde\omega=\log\omega$ | $\tilde\omega_\ell$ | **collision:** the tilde means logarithm, not Favre filter or SA variable |
| $\tilde p=\log p$, $\tilde T=\log T$ | $\ln p$, $\ln T$ | same tilde collision |
| $\tilde\omega_r$, $\tilde\omega_{r0}$ | $\tilde\omega_{\ell,r}$, $\tilde\omega_{\ell,r0}$ | realizability limit |
| $\bar k=\max(0,k)$ | $\bar k$ (page-local) | **collision:** the bar is clipping, not the LES filter |
| $u_i$, $p$, $\rho$, $T$ | mean quantities | no averaging mark in the paper |
| $\tau_{ij}$ | $-\rho R_{ij}$ | Boussinesq, negative convention with the isotropic part |
| $\hat\tau_{ij}$, $\hat q_j$ | total stress, total heat flux | **collision:** the hat is not a test filter |
| $\alpha$, $\beta$ ($\omega$ equation) | $\gamma_\omega$, $\beta_\omega$ | registry §11 |
| $\alpha^*$, $\beta^*$, $\sigma$, $\sigma^*$, $\sigma_d$ | as named | no values printed |
| $\mathbb P^l$, $l$ | degree $N$; MG level | **collision:** $l$ is the degree in §3 and the tables, the level (degree plus one) in the MG notation |
| $\mathbf q$, $\mathbf w$, $\mathbf P=\partial\mathbf q/\partial\mathbf w$ | conservative and log-primitive unknowns, transformation Jacobian | seven variables |
| $\varepsilon_p$, $C$, $h_K$, $\mathbf b$ | $\nu_{\mathrm{av}}$, $C$, $h_K$, $\boldsymbol b_p$ | as on the AV page |
| $[[z]]$ | $[\![z]\!]$ | jump |
| $\gamma$ | $\gamma$ | ratio of specific heats |
| $Tu=\sqrt{2k/3}/u_\infty$ | $Tu$ | |
| $c_p$, $c_f$, $c_L$ | $C_p$, $C_f$, $C_L$ | T106A $c_p=(p_{01}-p)/(p_{01}-p_2)$ |
| $Re_L$, $Re_c$, $Re_h$, $Re_{2,is}$ | $Re$ per case | body length, chord, step height, outlet isentropic |

# Reference list

53 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [32]
repeats [21] verbatim (Ghidoni, Colombo, Bassi & Rebay 2014, Int. J.
Numer. Methods Fluids 75) and is folded into one entry. Ref. [27] (Bassi
et al., Int. J. Comput. Fluid Dyn. 30, 2016, turbomachinery) falls on the
key of a different bundle entry (Bassi et al., Eur. J. Mech. B/Fluids 55)
and is keyed `bassi-2016-b`. Ref. [23] prints "51st AIAA Aerospace
Sciences Meeting … 2013, AIAA 2013-1002, AIAA, 2007", two years; it is
keyed by the printed year 2007 with a note. [10] prints the last author
"L. Darmofal", [19] "D. Darmofal"; [41] prints the issue "(181)", equal to
its first page; several items are authorless web pages (VFE-2, NPARC,
NASA TMR, HiLift-1, DPW3, GridPro) keyed with the citing year; [36] is a
KTH report. No item is unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [Delta-wing and concentrated vortex flows](/benchmarks/delta-wing-vortex-flow.md)
- [RAE 2822 airfoil](/benchmarks/rae-2822-airfoil.md)
- [Turbine cascades (T106, T161, VKI LS89)](/benchmarks/turbine-cascade.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Isogeometric analysis and isogeometric discontinuous Galerkin](/methods/isogeometric-analysis.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [Laminar kinetic energy transition models](/methods/laminar-kinetic-energy-transition-model.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
