---
type: Source
title: "Menter (1994) — Two-equation eddy-viscosity turbulence models for engineering applications"
description: "Defines the baseline (BSL) model, which blends Wilcox's k-ω near walls with a transformed k-ε away from them, and the shear-stress transport (SST) model, whose eddy-viscosity limiter enforces Bradshaw's relation in adverse pressure gradients; constants, blending functions, boundary values and tests on separated and transonic flows."
resource: "doi:10.2514/3.12149"
source_kind: paper
authors: [Menter F.R.]
year: 1994
venue: "AIAA J. 32:1598-1605"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/1994_Crossref_AIAA_Journal_Menter_Two-equation_eddy-viscosity_turbulence_models_for_engineerin.pdf"
tags: [rans, k-omega, eddy-viscosity, separated-flow, boundary-layer]
timestamp: 2026-10-29T16:21:00Z
---

# Summary

Menter (1994) builds two two-equation eddy-viscosity models "on a strictly
empirical basis". The **baseline (BSL) model** transforms the standard
high-Reynolds [$k$-$\varepsilon$ model](/methods/k-epsilon-model.md) into
$k$-$\omega$ variables, which adds a cross-diffusion term to the $\omega$
equation, and blends it with the original
[Wilcox $k$-$\omega$ model](/methods/k-omega-model.md) through a
wall-distance-based function $F_1$, equal to one in the sublayer and log
layer and going to zero in the wake region and free shear layers; constants
are blended the same way. BSL keeps the near-wall behaviour of Wilcox's
model (no damping functions, a Dirichlet wall value of $\omega$, robustness)
and removes its strong dependence on the freestream $\omega$. The
**shear-stress transport (SST)** model redefines the eddy viscosity as
$\nu_t=a_1k/\max(a_1\omega,|\Omega|F_2)$ so that Bradshaw's relation
$-\langle u'v'\rangle=a_1k$ holds in adverse-pressure-gradient boundary
layers where production exceeds dissipation, mimicking the lag effect of the
Johnson–King model; $F_2$ confines the limiter to wall-bounded flows. This is
the founding journal definition of the [$k$-$\omega$ SST model](/methods/k-omega-sst-model.md).

Incompressible computations with INS3D, and a transonic solver, compare SST,
BSL, the original $k$-$\omega$ and the Jones–Launder $k$-$\varepsilon$ on a
flat plate (freestream sensitivity, a [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)),
Driver's separated axisymmetric adverse-pressure-gradient flow, the
Driver–Seegmiller [backward-facing step](/benchmarks/backward-facing-step.md),
the [NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md) at 13.87° and the
Bachalo–Johnson transonic bump. The original $k$-$\omega$ eddy viscosity
changes by almost 100% when the freestream $\omega$ drops by four orders of
magnitude while BSL and SST do not; SST gives the best pressure, separation
and velocity profiles for Driver's flow, the best displacement on NACA 4412
and a significantly better wall pressure on the bump. The appendix gives the complete
models and warns that the $\omega$ production must be written with
$\gamma/\nu_t$, not $\gamma\omega/k$, for SST.

# Version read

Version of record (AIAA Journal 32, No. 8, August 1994; presented as AIAA
Paper 93-2906 in July 1993, received 26 July 1993, revised 30 December 1993),
a scan with an OCR layer that garbles the equations, which were read visually
at 300 dpi; 8 pages (pp. 1598–1605; the lower half of p. 1605 is an
advertisement), all read. Page 1 matches the Crossref metadata; the DOI is
printed in the download stamp. Numbering cited on this page is that of the
paper.

The archive also holds a byte-identical copy of this PDF (same MD5),
`0000_manual_no_journal_Unknown_10_2514_3_12149.pdf`; it is the same file, not another version.

# Key claims

Page-local symbols: $\gamma_1$, $\gamma_2$, $\gamma$ the $\omega$-production
coefficients as printed (the registry's $\gamma_\omega$; written $\alpha$ on
the [SST page](/methods/k-omega-sst-model.md)), $\beta_1$, $\beta_2$,
$\beta$ the $\omega$-destruction coefficients (the registry's
$\beta_\omega$); $\phi_1$, $\phi_2$ inner and outer constants; $CD_{k\omega}$
the positive part of the cross-diffusion; $\mathrm{arg}_1$, $\mathrm{arg}_2$
the blending arguments; $\omega_\infty$, $k_\infty$, $\nu_{t\infty}$ the
freestream values and $L$ the domain length; $\Delta d_1$ the first-point
wall distance. The source writes $y$ for the wall distance; it is $d$ here.

1. Changes of 5–10% in constants can significantly improve or degrade predictions, and no theoretical tool fixes constants to that accuracy, so models must be validated on challenging research flows (Introduction). **Stated**
2. The $k$-$\omega$ model needs no damping functions, admits Dirichlet wall conditions, and is superior in numerical stability and as accurate for mean-flow profiles (Introduction). **Stated**
3. Lack of near-wall asymptotic consistency does not spoil the mean profile or skin friction, because there $\nu_t\ll\nu$ (Introduction). **Stated**
4. Citing Refs. 2–3: the form of $k$-$\varepsilon$ damping functions has little effect on velocity profiles and skin friction at high Reynolds number, and fitting DNS $k$ and $\varepsilon$ need not improve the eddy viscosity (pp. 1598–1599). **Stated**
5. $k$-$\omega$ is superior to $k$-$\varepsilon$ in the log region for equilibrium adverse-pressure-gradient and compressible flows (Refs. 1, 5) (p. 1599). **Stated**
6. The original $k$-$\omega$ is strongly sensitive to the freestream $\omega$: the eddy viscosity can change by more than 100% (Ref. 6); $k$-$\varepsilon$ is not; no theory distinguishes freestream-dependent from independent models (p. 1599). **Stated**
7. The wake-region eddy viscosity, not the log-region behaviour, decides whether an eddy-viscosity model predicts strong adverse pressure gradients (p. 1599). **Stated**
8. Two-equation models give $\tau=\rho\sqrt{P_k/\varepsilon}\,a_1k$ (Eq. 11, Ref. 10), which overpredicts the shear stress where $P_k/\varepsilon>1$, violating Bradshaw's $\tau=\rho a_1k$ (Eq. 9), with $\tau=-\rho\langle u'v'\rangle$ (p. 1600). **Derived**
9. $\nu_t=a_1k/\max(a_1\omega,|\Omega|F_2)$ (Eq. 12, A14), $|\Omega|$ "the absolute value of the vorticity", guarantees Eq. 9 where $|\Omega|>a_1\omega$ in adverse-pressure-gradient boundary layers and recovers $\nu_t=k/\omega$ elsewhere (p. 1600). **Derived**
10. The added cost is the blending functions (needing the wall distance, computed once unless the grid moves) and the cross-diffusion; computing time and stability are not affected (p. 1600; Conclusions). **Stated**
11. Changing $\mathrm{arg}_1$ to $\min\big(500\nu/(d^2\omega),\,4\rho\sigma_{\omega2}k/(CD_{k\omega}d^2)\big)$ (Eq. 13) gives a two-layer $k$-$\varepsilon$ model with $k$-$\omega$ in the sublayer, blending without user input; "The modification ensures that $F_1$ is zero for $y^+>70$" (p. 1600). **Stated**
12. Flat plate: with the freestream $\omega$ reduced by four orders of magnitude (and $k$ to keep $\nu_t$ fixed) the original $k$-$\omega$ eddy viscosity changes by almost 100%, BSL and SST not at all (Fig. 1). **Shown**
13. All models agree with $u^+$–$y^+$ and $C_f$ correlations on the flat plate (Ref. 9); the $k$-$\omega$ models tolerate a first point up to $y^+=3$ (p. 1601). **Stated**
14. In free shear layers SST and BSL reduce to the same model ($F_1=F_2=0$), virtually standard $k$-$\varepsilon$ (Ref. 9) (p. 1601). **Stated**
15. Samuel–Joubert flow: the three $k$-$\omega$ models reproduce the data, Jones–Launder $k$-$\varepsilon$ gives too high $C_f$; the flow is not a strong enough test (Ref. 9) (p. 1601). **Stated**
16. Driver's flow: SST gives the best wall pressure, the largest separation and the best velocity profiles; Jones–Launder stays attached; BSL and original $k$-$\omega$ are close to each other (Figs. 2–4). **Shown**
17. Driver's flow: Jones–Launder predicts much higher shear stress approaching separation; SST reproduces the drop of $\nu_{t,\max}/(u_e\delta^*)$ in very good agreement, BSL and original $k$-$\omega$ are too high, and $k$-$\varepsilon$ falls barely below Clauser's 0.0168 (Figs. 5–6). **Shown**
18. Backward-facing step ($120\times120$; $90\times90$ and $240\times240$ virtually identical): reattachment at 6.5 (SST), 5.9 (BSL), 6.4 (original $k$-$\omega$), 5.5 (Jones–Launder) step heights against about 6.4 measured; the $k$-$\varepsilon$ value is better than previously reported thanks to the fine grid, but its $C_f$ varies too much (Figs. 7–8). **Shown**
19. No model captures the relaxation downstream of reattachment, nor, per Ref. 19, a more complex anisotropic model (Fig. 8). **Shown**
20. NACA 4412: SST predicts the displacement effect in very good agreement; BSL responds somewhat; original $k$-$\omega$ is further from experiment than Jones–Launder, attributed to its freestream dependence (Fig. 9). **Shown**
21. NACA 4412 with a freestream $\omega$ about fifty times larger: SST changes very little, original $k$-$\omega$ changes significantly and approaches BSL (Fig. 9). **Shown**
22. Transonic bump at $M=0.925$: SST predicts a significantly better wall pressure than the other models (Fig. 10). **Shown**
23. SST "is the only available two-equation model that has demonstrated the ability to accurately predict pressure-induced separation and the resulting viscous-inviscid interaction" and "should be the model of choice for aerodynamic applications" (Conclusions). **Stated**
24. The models are very stable in complex applications (Ref. 23), and an early SST version compares very favourably with a full Reynolds-stress model on complex 3D flows (Ref. 24) (Conclusions). **Stated**
25. In $\mathrm{arg}_1=\min\big[\max\big(\sqrt k/(0.09\,\omega d),\,500\nu/(d^2\omega)\big),\,4\rho\sigma_{\omega2}k/(CD_{k\omega}d^2)\big]$ (A9), the first argument equals 2.5 in the log layer, the second keeps $F_1=\tanh(\mathrm{arg}_1^4)=1$ in the sublayer, and the third drives $\mathrm{arg}_1\to0$ at the boundary-layer edge when the "degenerate" solution of Ref. 6 is approached; $F_2=\tanh(\mathrm{arg}_2^2)$, $\mathrm{arg}_2=\max\big(2\sqrt k/(0.09\,\omega d),\,500\nu/(d^2\omega)\big)$ (A15–A16) (Appendix). **Derived**
26. The wall value $\omega=10\cdot6\nu/(\beta_1\Delta d_1^2)$ (A12) simulates Wilcox's smooth-wall condition as long as $\Delta d_1^+<3$; freestream values $\omega_\infty=(1$–$10)U_\infty/L$, $\nu_{t\infty}=10^{-(2\text{–}5)}\nu_\infty$, $k_\infty=\nu_{t\infty}\omega_\infty$ (A11) (Appendix). **Stated**
27. SST was calibrated with the production $(\gamma/\nu_t)\tau_{ij}\partial_ju_i$ of (A2); the form $\gamma(\omega/k)\tau_{ij}\partial_ju_i$ (A17) differs for SST because of (A14) "and should therefore not be used" (Appendix). **Stated**

The models (A1)–(A10) read, with $\tau_{ij}\partial_ju_i=\rho P_k$,
$D(\rho k)/Dt=\rho P_k-\beta^*\rho\omega k+\partial_j[(\mu+\sigma_k\mu_t)\partial_jk]$ and
$D(\rho\omega)/Dt=(\gamma/\nu_t)\rho P_k-\beta\rho\omega^2+\partial_j[(\mu+\sigma_\omega\mu_t)\partial_j\omega]+2(1-F_1)\rho(\sigma_{\omega2}/\omega)\partial_jk\,\partial_j\omega$,
with $\phi=F_1\phi_1+(1-F_1)\phi_2$ and
$CD_{k\omega}=\max\big(2\rho\sigma_{\omega2}\omega^{-1}\partial_jk\,\partial_j\omega,\,10^{-20}\big)$
(A10). Set 1 (A4):
$\sigma_{k1}=0.5$, $\sigma_{\omega1}=0.5$, $\beta_1=0.0750$; set 2 (A5):
$\sigma_{k2}=1.0$, $\sigma_{\omega2}=0.856$, $\beta_2=0.0828$; $\beta^*=0.09$,
$\kappa=0.41$, $\gamma_i=\beta_i/\beta^*-\sigma_{\omega i}\kappa^2/\sqrt{\beta^*}$;
SST changes set 1 to $\sigma_{k1}=0.85$ and adds $a_1=0.31$ (A13). The printed
formula gives $\gamma_1=0.5532$ and $\gamma_2=0.4404$ *(compiler check, not in
the sources)*. The [SST page](/methods/k-omega-sst-model.md) records a floor
of $10^{-10}$ on $CD_{k\omega}$ from a later source; this paper prints
$10^{-20}$ (A10).

# Printed slips

- **Data reference:** the NACA 4412 section (p. 1602) cites "Coles and Wadcock"; Ref. 20 prints "Coles, D., and Wadock, A. J.".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_i$ | $\langle u_i\rangle$ | mean velocity, no overbar in the source |
| $\tau_{ij}$ (A7) | $-\rho R_{ij}$ | modelled as $\mu_t(2S_{ij}-\tfrac23\partial_ku_k\delta_{ij})-\tfrac23\rho k\delta_{ij}$; $\tau_{ij}\partial_ju_i=\rho P_k$ |
| $\tau=-\rho\overline{u'v'}$ | $-\rho R_{12}$ | principal shear stress |
| $\gamma_1$, $\gamma_2$, $\gamma$ | $\gamma_\omega$ (§11) | **collision** with the ratio of specific heats; $\alpha$ on the SST page |
| $\beta_1$, $\beta_2$, $\beta$ | $\beta_\omega$ (§11) | |
| $\beta^*$, $\sigma_k$, $\sigma_\omega$, $a_1$ | same | 0.09, blended, blended, 0.31 |
| $\Omega$ | $\lvert\Omega\rvert$ | $\partial u/\partial y$ in boundary layers, absolute vorticity in general |
| $F_1$, $F_2$ | $F_1$, $F_2$ | |
| $y$ | $d$ | distance to the nearest no-slip surface |
| $\omega_f$, $\omega_\infty$ | $\omega_\infty$ (page-local) | freestream value |
| $\Delta y_1$ | $\Delta d_1$ (page-local) | first-point wall distance |
| $\epsilon$ | $\varepsilon$ | |
| JL | Jones–Launder $k$-$\varepsilon$ | "k-ε std." in Fig. 10 |

# Reference list

24 printed references, numbered, AIAA style; no DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. 9 (AIAA 93-2906) is the conference version of this paper. Ref. 15
(Launder & Sharma 1974, Lett. Heat Mass Transfer) is a different work from Launder & Spalding (1974) and is the bibliography's `launder-1974-b`; Menter (1992, two
AIAA J. papers), Wilcox (1993, AIAA J. article), Huang (1992, NASA TM),
Rogers (1992, 1994, AIAA papers) and Michelassi (1991, NASA TM) share author–year keys with different works and are keyed `menter-1992-b`, `menter-1992-c`, `wilcox-1993-b`, `huang-1992-b`, `rogers-1992-b`, `rogers-1994-b` and `michelassi-1991-b`. Ref. 14
(Rogers) is a private communication; Refs. 17 and 20 print page ranges
differing by one from existing entries. No item is unparseable.

# Pages created or updated

Chunk 17 (2026-10-29). This source is cited on:

- [Turbulent boundary layers: zero and adverse pressure gradient, compressible](/benchmarks/turbulent-boundary-layer.md)
- [k-ε models](/methods/k-epsilon-model.md)
- [Wilcox k-ω model](/methods/k-omega-model.md)
- [k-ω SST model](/methods/k-omega-sst-model.md)
