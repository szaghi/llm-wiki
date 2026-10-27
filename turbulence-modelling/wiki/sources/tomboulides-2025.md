---
type: Source
title: "Tomboulides et al. (2025) — A robust spectral element implementation of the k−τ RANS model in Nek5000/NekRS"
description: "Implements the k-τ RANS model (τ = 1/ω) in the spectral element codes Nek5000 and NekRS with a capped near-wall source, a free-stream limiter and implicit source terms, and validates it on channel, pipe, backward-facing step, NACA 0012 and T-junction flows against the regularized k-ω model and OpenFOAM SST."
resource: "doi:10.1016/j.ijheatfluidflow.2024.109679"
source_kind: paper
authors: [Tomboulides A., Saini N., Shaver D.R., Obabko A.V., Yuan H., Merzari E., Fischer P.F.]
year: 2025
venue: "Int. J. Heat Fluid Flow 112:109679"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_International_Journal_of_Heat_and_Fluid_Flow_Tomboulides_A_robust_spectral_element_implementation_of_the_mmlmath_xmln.pdf"
tags: [rans, k-omega, spectral-element, high-order, eddy-viscosity, separated-flow]
timestamp: 2026-10-27T15:55:00Z
---

# Summary

Tomboulides et al. (2025) implement, verify and validate the
[$k$-$\tau$ model](/methods/k-tau-model.md) in the
[spectral element](/methods/spectral-element-method.md) codes
[Nek5000 and NekRS](/software/nek5000.md). The transported time scale is
$\tau_t=1/\omega$ (registry §11). The motivation is the wall
singularity of the [Wilcox $k$-$\omega$ model](/methods/k-omega-model.md),
$\omega\sim d^{-2}$. Prescribing a large wall value of $\omega$ leaves
grid-sensitive solutions and, in high-order codes with little numerical
diffusion, persistent oscillations. The authors' earlier regularized
$k$-$\omega$ model removes the singular part analytically, but its extra
sources depend on the wall distance and its derivatives. The $k$-$\tau$
model has the natural wall condition $\tau_t=0$ and bounded sources.

The formulation follows Kalitzin et al. (1996) and Kok & Spekreijse (2000),
with the Wilcox (2006) constants, a [Boussinesq](/definitions/boussinesq-hypothesis.md)
eddy viscosity $\mu_t=\rho k\tau_t$, Menter's production limiter, a
cross-diffusion term and the rewrite of the $\nabla\tau_t\cdot\nabla\tau_t/\tau_t$
term through $\nabla\tau_t^{1/2}$. The new ingredients are a cap on the
molecular part of that term, a Kalitzin-type free-stream limiter on all
sources, a low-Reynolds-number variant with Wilcox (1992) damping, and an
implicit treatment of the non-linear sources inside the Helmholtz operator
of the BDF$k$/EXT$k$ scheme.

The tests are the [turbulent channel](/benchmarks/turbulent-channel-flow.md)
at $Re_\tau\approx5200$, a pipe at $Re_\tau=1142$, the Driver–Seegmiller
[backward-facing step](/benchmarks/backward-facing-step.md), the
[NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re_c=6\times10^6$ and
the OECD/NEA T-junction. Results agree closely with the regularized
$k$-$\omega$ model and with [OpenFOAM](/software/openfoam.md)'s
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md). On the T-junction the
$k$-$\tau$ model runs at CFL $\sim2$ against $\sim0.1$ for the regularized
$k$-$\omega$ model. The [$k$-$\varepsilon$](/methods/k-epsilon-model.md)
family is set aside for its damping functions and wall-distance needs;
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) values from CFL3D
and FUN3D are airfoil references; [wall functions](/methods/rans-wall-function.md)
and an SST-type $k$-$\tau$ as the base of a
[DDES](/methods/detached-eddy-simulation.md) are future work. The pipe log
layer is compared with the [law of the wall](/definitions/law-of-the-wall.md)
($\kappa=0.41$, $B=5.5$).

# Version read

Version of record (Elsevier typeset, Int. J. Heat Fluid Flow 112 (2025)
109679; received 1 March 2024, available online 12 December 2024); 17
pages, all read, with pp. 2–5 checked visually. Page 1 agrees with
Crossref; page 1 prints the initials "D.R. Shaver", "A.V. Obabko" and
"P.F. Fischer", which the authors field above follows.

# Key claims

1. Near walls $\omega\sim d^{-2}$, so $\omega$ and its gradient are singular; an arbitrarily large wall value of $\omega$ suffices for finite-volume codes but causes persistent oscillations in high-order codes, and the solution stays sensitive to the near-wall spacing (§1). **Stated**
2. The regularized $k$-$\omega$ model (Tomboulides et al. 2018) writes $\omega=\omega_w+\omega'$ with $\omega'=0$ on walls, but its extra sources are functions of $d$ and its derivatives (§1). **Stated**
3. For the $k$-$\tau$ model the wall condition is $\tau_t=0$ and every source of the $\tau_t$ equation is bounded, so no regularization and no wall distance are needed (§1, §2). **Stated** (the free-stream limiter, claim 9, does use $d$)
4. Kok & Spekreijse (2000) showed that transporting $\sqrt{\tau_t}$ (Kalitzin et al. 1996) makes the sources unbounded, whereas for $\tau_t$ they stay bounded near the wall (§1). **Stated**
5. Near the wall $\tau_t\to\rho\beta_\omega d^2/(6\mu)$ (Eq. 19), so $\nabla\cdot(\mu\nabla\tau_t)\to\frac13\rho\beta_\omega$ and $2\frac{\mu}{\tau_t}\nabla\tau_t\cdot\nabla\tau_t\to\frac43\rho\beta_\omega$, balancing the constant source $\rho\beta_\omega$ (§2, Eq. 20). **Derived**. Substituting Eq. 19 gives both limits and $\rho\beta_\omega+\frac13\rho\beta_\omega-\frac43\rho\beta_\omega=0$ *(compiler check, not in the sources)*.
6. Writing $2\frac{\Gamma_\omega}{\tau_t}\nabla\tau_t\cdot\nabla\tau_t=8\Gamma_\omega\nabla\tau_t^{1/2}\cdot\nabla\tau_t^{1/2}$ (Eq. 18) is numerically preferable because $\tau_t^{1/2}$ is linear near the wall and no division by $\tau_t$ occurs (§2). **Stated**
7. The molecular part of that term is capped, $\min[S_{\lim},8\mu\nabla\tau_t^{1/2}\cdot\nabla\tau_t^{1/2}]$ (Eq. 21): without the cap, gradient errors near sharp corners and in transients drove $\tau_t$ and $\mu_t$ to unphysically small values that persisted and were convected away from walls (§2). **Stated** (authors' experience, no figure)
8. The theoretical cap is $S_{\lim}=\frac43\rho\beta_\omega$ (Eq. 20); all reported runs use the relaxed $S_{\lim}=\frac83\rho\beta_\omega$ for robustness (§2). **Stated**
9. The free-stream limiter $R_{\mathrm{fs}}=\min(1,\mu_t/(r\mu))$ for $d>d_{\lim}$ and $R_{\mathrm{fs}}=1$ otherwise (Eq. 22), with $r=0.01$ and $d_{\lim}=0.5D_h$, multiplies all sources and suppresses the free-stream growth of $\tau_t$ driven by the constant source $\rho\beta_\omega$; it may be ignored for internal flows and solutions are insensitive to $d_{\lim}$ (§2). **Stated**
10. Moving the non-linear sources into the Helmholtz operator ($\hat K=K-S$) adds no cost to the Helmholtz solve and leaves only the convective CFL limit, about 0.5 for BDF2 (§2.2, Eqs. 35–38). **Stated**
11. Channel, $Re_b=125\,000$, $Re_\tau\approx5200$, 7 elements across the half-channel, $N=3,5,7,9$ with first-node $y^+=1.7,0.73,0.39,0.25$: velocity, $k^+$ and $\tau_t^+$ are insensitive to near-wall resolution and indistinguishable under $N$-refinement except at $N=3$ (§3.1, Figs. 1–2). **Shown**
12. Channel $u_\tau$ (Table 1): $k$-$\tau$ 0.0412, regularized $k$-$\omega$ 0.0413, low-Re $k$-$\tau$ 0.0414, low-Re regularized $k$-$\omega$ 0.0415, OpenFOAM SST 0.0409, DNS (Lee & Moser) 0.0415; the Nek5000 models agree better with DNS than OpenFOAM (§3.1). **Shown**
13. $k$-$\tau$ and regularized $k$-$\omega$ profiles agree excellently, "expected since the $\tau$ and $\omega$ transport equations are equivalent" (§3.1, Fig. 3). **Shown**
14. Pipe, $Re_b=44\,000$, $Re_\tau=1142$, $N=7$, mean $y^+\approx0.8$: $u_\tau$ 0.0523 ($k$-$\tau$), 0.0524 (regularized $k$-$\omega$), 0.0528 and 0.0529 (low-Re variants), DNS (Wu & Moin) 0.0519; error below 1% (standard) and 2% (low-Re) (§3.2, Table 2). **Shown**
15. The low-Re variant captures the near-wall peak of $k$ (slightly offset from DNS), barely changes the velocity profile, and collapses onto the standard model towards the pipe centre (§3.2, Fig. 6). **Shown**
16. Backward-facing step, $Re=37\,425$ (step height, free-stream velocity), $N=7$, 2553 elements: $x_R=6.48H$ ($k$-$\tau$), $6.49H$ (regularized $k$-$\omega$), $6.44H$ (OpenFOAM SST, fine mesh), experiment $6.26H$; Menter (1994) reported $6.4H$ ($k$-$\omega$) and $6.5H$ (SST) (§3.3). **Shown**
17. On the step all models under-predict the downstream velocity; OpenFOAM SST under-predicts $C_f$, "a known behavior of the SST model"; the $N=4$ and $N=7$ $C_f$ profiles are indistinguishable (§3.3, Figs. 9–12). **Shown**
18. The downstream $k$ deviations from OpenFOAM SST "may be explained" by the absence of blending functions in the present $k$-$\tau$ model and by different parameters (§3.3). **Stated**
19. For external flows the free-stream limiter and the modified sources (Eqs. 22–24) are "imperative": limiting the far-field eddy viscosity avoids abrupt total-viscosity variations that cause instability or more pressure–velocity iterations; drag and lift are then consistent even for zero free-stream $k$ (§3.4). **Stated**
20. NACA 0012, $Re_c=6\times10^6$, $M=0.15$, $0^\circ$: $C_D=0.00831$ ($k$-$\tau$), 0.00835 (regularized $k$-$\omega$); CFL3D SA 0.008190, SST 0.008090, $k$-$\omega$ 0.00854; FUN3D SA 0.008120, SST 0.008160, $k$-$\omega$ 0.00837; experiment 0.0081 (Table 3). **Shown**
21. NACA 0012 at $10^\circ$: $k$-$\tau$ $C_D=0.01381$, $C_L=1.0618$; CFL3D SA 0.01231/1.0909, SST 0.01236/1.0778, $k$-$\omega$ 0.01259/1.0958; FUN3D SA 0.01242/1.0983, SST 0.01253/1.0840, $k$-$\omega$ 0.01297/1.1012; experiment 0.012/1.075. The text says $k$-$\tau$ "slightly overpredicts" drag and under-predicts lift, with a smaller $|C_L|$ error than the standard $k$-$\omega$ of either NASA code (§3.4, Table 4). **Shown**. The printed $C_D$ is 15.1% above the experiment, against at most 8.1% for the NASA-code values *(compiler check, not in the sources)*.
22. Airfoil results at $N=5$ and $N=7$ differ by less than 0.1% in every reported value; mean $y^+<1$ (§3.4). **Shown**
23. $C_p$ agrees with Gregory & O'Reilly (1970) and Ladson (1988) at both angles (§3.4, Fig. 16). **Shown**
24. T-junction (OECD/NEA 2010), $Re=40\,000$ at both inlets: both RANS models over-predict the axial velocity at moderate wall distances and under-predict it in the core against LES and experiment; $k$-$\tau$ and regularized $k$-$\omega$ differ slightly in the core, attributed to wall-distance errors near the sharp corner entering the regularized model (§3.5, Figs. 19–22). **Shown** (attribution **Stated**)
25. On the T-junction $k$-$\tau$ ran stably at CFL $\sim2$ thanks to the implicit sources, whereas the regularized $k$-$\omega$ was restricted to CFL $\sim0.1$ because its extra non-linear sources cannot be treated implicitly (§3.5, §4). **Shown** (no timing table)
26. T-junction profiles at $N=5,7,9$ differ very little at $x=1.6D$ (§3.5, Fig. 23). **Shown**
27. The model is also implemented in NekRS, "a numerically identical counterpart of Nek5000" for accelerators (§1, §4). **Stated** (no NekRS results shown)
28. Future work: $k$-$\tau$ wall functions (Shaver et al. 2022, 2023), steady solvers, and an SST version of $k$-$\tau$ as a base for DDES (Gritskevich et al. 2012) (§4). **Stated**

The model as implemented (Eqs. 23–24, with $\langle u_i\rangle$ written
$u_i$, incompressible, $P=\min(\mu_t|S|^2,10\rho\beta^*k/\tau_t)$,
$\mu_t=\rho k\tau_t$, $\Gamma_k=\mu+\mu_t/\sigma_k$,
$\Gamma_\omega=\mu+\mu_t/\sigma_\omega$):
$$\begin{aligned}
\partial_t(\rho k)+\nabla\cdot(\rho k\boldsymbol u)&=\nabla\cdot(\Gamma_k\nabla k)+\Big(P-\rho\beta^*\frac{k}{\tau_t}\Big)R_{\mathrm{fs}},\\
\partial_t(\rho\tau_t)+\nabla\cdot(\rho\tau_t\boldsymbol u)&=\nabla\cdot(\Gamma_\omega\nabla\tau_t)+\Big(-\gamma_\omega\rho\tau_t^2|S|^2+\rho\beta_\omega-8\Gamma_\omega\nabla\tau_t^{1/2}\cdot\nabla\tau_t^{1/2}+\rho\sigma_d\tau_t\min(\nabla k\cdot\nabla\tau_t,0)\Big)R_{\mathrm{fs}},
\end{aligned}$$
with the molecular part of the $8\Gamma_\omega$ term capped as in claim 7,
$\beta_\omega=0.0708$, $\beta^*=0.09$, $\gamma_\omega=0.52$,
$\sigma_k=1/0.6$, $\sigma_\omega=2$, $\sigma_d=1/8$ as printed. The low-Re
variant (Eqs. 25–31) sets $\mu_t=\alpha^*\rho k\tau_t$ and damps
$\alpha^*$, $\beta^*$ and $\gamma_\omega$ with $Re_T=\rho k\tau_t/\mu$,
$R_k=6$, $R_\beta=8$, $R_\tau=2.95$, $\alpha_0^*=\beta_\omega/3$.

# Printed slips

- §3.2 heading "Turbulent pipe flow, $Re_\tau=1000$" against the text's "$Re_\tau=1142$"; the text value follows from the printed data, $22\,000\times0.0519=1141.8$ *(compiler check, not in the sources)*.
- Eq. (29) writes "$Re_T/Re_\tau$" while Eq. (30) defines the constant as $R_\tau=2.95$; $\alpha_0$ in Eq. (29) is given no value.
- §2.1 says Eqs. (28)–(29) modify "the coefficients in the destruction term", but Eq. (29) modifies $\alpha$, the production coefficient of the $\tau_t$ equation.
- §1: "$k-\varepsilon$ (specific dissipation)" labels $\varepsilon$ as specific dissipation.
- §3.5: the text says Fig. 18 and Figs. 19–20 use "the $p=9$ mesh", while the captions of Fig. 18 ("polynomial order 7") and Figs. 19–22 ("$p=7$") give $N=7$.
- §3.3: "The coarse and fine meshes from OpenFoam show good agreement, however the coarsest mesh profile differs significantly", with meshes named coarse, medium and fine.
- §2.2: "for Eqs. Eqs. (12) and (24)".
- Table 3 caption cites Freeman & Roy (2014) and Table 4 caption and text cite Jespersen et al. (2016) for the same CFL3D/FUN3D data; "Spallart–Allmaras" in the text and Table 3 caption.
- Eq. (1) prints the momentum stress as $(\mu+\mu_t)(2\underline{\mathbf S}-\frac23Q\underline{\mathbf I})$ without the $-\frac23\rho k$ isotropic part (absorbed into the pressure, not stated).
- References: Deville et al. (2002) prints "Fischer, P.F." twice; the Lee & Moser (2015) title is truncated after "up to"; "Orzag" for Orszag (also in the text); "AAIA" for AIAA (Kalitzin 1996, Wilcox 2008); "Nacr." (Prandtl 1945).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf v=(u,v,w)$ | $\langle u_i\rangle$ | ensemble-averaged mean velocity |
| $\underline{\mathbf S}$, $S=\sqrt{2\underline{\mathbf S}:\underline{\mathbf S}}$ | $\langle S_{ij}\rangle$, $\lvert S\rvert$ | factor two included, as in the registry |
| $\underline{\boldsymbol\tau}=2\mu_t\underline{\mathbf S}$ | $-\rho R_{ij}$ (deviatoric part) | **collision:** negative convention; not $\tau_{ij}$ (SGS) |
| $\tau=1/\omega$ | $\tau_t$ (registry §11) | **collision:** turbulent time scale, not a stress or $\tau_w$ |
| $\tau^+=\tau u_\tau^2/\nu$ | $\tau_t^+$ (page-local) | |
| $k$, $\omega$, $\varepsilon$ | $k$, $\omega$, $\varepsilon$ | |
| $\mu_t=\rho k\tau$ | $\mu_t$ | $\alpha^*\rho k\tau_t$ in the low-Re variant |
| $P=\mu_tS^2$ | $P_k$ (limited) | |
| $\beta$, $\beta^*$, $\alpha$ | $\beta_\omega$, $\beta^*$, $\gamma_\omega$ | registry §11; Wilcox (2006) values |
| $\sigma_k$, $\sigma_\omega$, $\sigma_d$ | $\sigma_k$, $\sigma_\omega$, $\sigma_d$ | divide $\mu_t$: $\sigma_k=1/0.6$, $\sigma_\omega=2$ |
| $\Gamma_k$, $\Gamma_\omega$, $\Gamma_\tau$ | $\Gamma_k$, $\Gamma_\omega$ (registry §11), $\Gamma_\tau$ (page-local) | $\Gamma_\tau=\Gamma_\omega$ |
| $C_{D_\omega}$, $C_{D_\tau}$ | (cross-diffusion terms, page-local) | |
| $S_\tau=\nabla\tau^{1/2}\cdot\nabla\tau^{1/2}$, $S_{lim}$ | (page-local), $S_{\lim}$ | **collision:** not a strain rate |
| $R$, $r$, $y_{lim}$, $D_h$ | $R_{\mathrm{fs}}$, $r$, $d_{\lim}$, $D_h$ (page-local) | **collision:** $R$ is not $R_{ij}$ |
| $y_w$ | $d$ | wall distance |
| $\omega_w$, $\omega'$ | (page-local) | singular and regular parts of $\omega$, $\omega_w=6\nu/(\beta_\omega d^2)$ |
| $Re_T=\rho k\tau/\mu$; $\alpha^*$, $\alpha_0^*$, $\alpha_\infty$, $\beta^*_\infty$, $R_k$, $R_\beta$, $R_\tau$ | same (page-local) | low-Re damping |
| $p$ | $N$ | polynomial degree |
| $\underline{\mathbf M}$, $\underline{\mathbf C}$, $\underline{\mathbf K}$, $\hat{\underline{\mathbf K}}$, $\underline{\mathbf S}$, $\underline{\mathbf H}$ | (page-local matrices) | **collision:** $\underline{\mathbf S}$ is the source matrix in §2.2, not the strain |
| $\phi$, $\epsilon$, $s_l$, $s_{nl}$ | (page-local) | generic scalar, diffusivity, sources (Eq. 32) |
| $u_\tau$, $y^+$, $U^+$, $k^+$, $Re_\tau$ | $u_\tau$, $y^+$, $u^+$, $k^+$, $Re_\tau$ | $Re_\tau$ on the half-height (channel) or radius (pipe) |
| $Re_b$ | $Re_b$ | |
| $H$ | $\delta$ (channel) or step height $H$ | reused symbol |
| $C_f$, $C_d$, $C_L$, $C_p$ | $C_f$, $C_D$, $C_L$, $C_p$ | |

# Reference list

45 printed references, Elsevier author–year style, alphabetical and
unnumbered. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. No printed
duplicates. Two entries have no author or no year (the Nek5000 Version
19.0 web entry, cited "Nek, 2019"; the Fischer et al. Nek5000 User's
Manual, keyed with a synthetic year). Gregory & O'Reilly (1970) and Lam &
Bremhorst (1981) print no venue; Jespersen et al. (2016) prints "Tech.
rep." with no institution; Kalitzin et al. (1996) prints only "AAIA 96,
0327"; the Lee & Moser (2015) title is truncated. DOIs are printed only for
Shaver et al. (2021, 2022).

# Pages created or updated

Chunk 8 (2026-10-27). This source is cited on:

- [Backward-facing step](/benchmarks/backward-facing-step.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Boussinesq eddy-viscosity hypothesis](/definitions/boussinesq-hypothesis.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Detached-eddy simulation and its delayed and zonal forms](/methods/detached-eddy-simulation.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
- [The k-τ model](/methods/k-tau-model.md)
- [Wall functions for RANS](/methods/rans-wall-function.md)
- [Spalart–Allmaras model and its corrections](/methods/spalart-allmaras-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Nek5000 and NekRS](/software/nek5000.md)
- [OpenFOAM](/software/openfoam.md)
