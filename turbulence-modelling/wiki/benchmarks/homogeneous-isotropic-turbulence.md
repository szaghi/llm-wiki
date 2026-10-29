---
type: Benchmark
title: "Homogeneous isotropic turbulence (decaying and forced)"
description: "Turbulence in a triply periodic box, decaying or forced: a priori and a posteriori test of subgrid closures, learned closures and neural-operator surrogates, of filter widths and scheme dissipation, DNS up to Taylor-scale Reynolds number 2500 on 32768^3 points, supersonic isothermal and compressible runs, and driven MHD turbulence with and without bulk viscosity."
status: established
aliases: [HIT, DHIT, HID, DIT, Comte-Bellot–Corrsin experiment, CBC experiment, forced HIT, decaying isotropic turbulence, forced isotropic turbulence, periodic box turbulence, compressible isotropic turbulence, turbulent box simulation, supersonic isothermal turbulence, driven supersonic turbulence, exascale DNS of isotropic turbulence]
tags: [benchmark, les, sgs-model, data-driven, dns, compressible]
timestamp: 2026-10-28T17:52:00Z
---

# Homogeneous isotropic turbulence (decaying and forced)

Homogeneous isotropic turbulence (HIT) is computed in a periodic cube,
with no walls and no mean flow. In the **decaying**
variant a random field with a prescribed spectrum evolves freely and its
kinetic energy $K=\int E(k)\,dk$ and dissipation $\varepsilon$ decrease in
time. In the **forced** variant a body force $f_i$ injects energy at a rate
that keeps the flow statistically stationary. Because the flow is
homogeneous, the energy spectrum $E(k)$ and the time histories of $K$ and
$\varepsilon$ characterize the solution completely at the level the sources
compare. An LES is judged against a DNS filtered to the LES cutoff. The case
isolates the [subgrid-scale closure](/definitions/large-eddy-simulation.md)
and the [numerical dissipation](/properties/numerical-dissipation.md) of the
discretization from wall and inflow effects. (On this spectral page $k$ is
the wavenumber magnitude and $K$ the kinetic energy, as fixed in the
notation registry.)

## Set-ups in the sources

| Source | Variant | $Re_\lambda$ | Reference DNS | LES resolution | Initial field and forcing |
|---|---|---|---|---|---|
| [Flad & Gassner (2017)](/sources/flad-2017.md), §1, §3–5 | decaying | from about 162 to 97 over the run | pseudo-spectral, $512^3$, 2/3-rule de-aliasing | DG, $N=7$: $18^3$ elements ($144^3$ DOF) and $6^3$ elements ($48^3$ DOF) | filtered DNS field; maximum local Mach about 0.1 |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.A | decaying | 70 | $128^3$ | $32^3$ | Passot–Pouquet spectrum, $u_{\mathrm{rms}}=1$ |
| [Agrawal et al. (2022)](/sources/agrawal-2022.md), §VII.B–C | forced | 315; and $Re_\lambda\to\infty$ | filtered $1024^3$ DNS of Cardesa et al. | $128^3$ | linear momentum forcing at constant kinetic energy |
| [Beck & Kurz (2023)](/sources/beck-2023.md), §IV A | forced | about 180 | DG $N=7$, $64^3$ elements, 512 points per direction, run to $t=10$ (about 14 large-eddy turnovers) | DG, 24 or 36 DOF per direction, $N=3,5,8$ | Rogallo initialization, linear forcing applied at the nodes |
| [Vela-Martín (2022)](/sources/velamartin-2022.md), §5.1, Table 1 | forced | 140, 240, 324 | $256^3$, $512^3$, $1024^3$, with $k_{\max}\eta=1.5,1.5,2.0$; 290 independent fields | a priori only: filter scales $\ell/L$ from 0.65 to 0.08 | linear forcing |
| [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), §5, App. G.2 | forced (3D) | not stated ($Re=2000$) | $1024^3$, single precision | $32^3$, $64^3$ | random field with spectrum peaked at wavenumber 20; Kolmogorov force $\sin(8\pi x_2)$ on $[0,1]^3$ |
| [Prakash et al. (2022)](/sources/prakash-2022.md), §III.A, §III.B.1 | forced | 418 (a priori); effectively infinite in the LES ($\nu=10^{-12}$) | Johns Hopkins forced isotropic database (a priori); $k^{-5/3}$ spectrum with Kolmogorov constant 1.6 (a posteriori) | a priori box filters $\Delta\approx6.5\eta$ to $68\eta$, anisotropic up to $15\eta\times292\eta\times292\eta$; LES on $32^3$, $64^3$, $128^3$ trilinear finite elements | spectral forcing of the modes $\lvert k_i\rvert<3$ at injected power 62.843 |
| [Cao et al. (2022)](/sources/cao-2022.md), §3.4, Table 8 | decaying, compressible | 72 (initial) | none: the DNS is offered as reference data | DNS only, $512^3$ cells, $k_{\max}\eta_0=3.61$ | spectrum $E(k)\propto k^4\exp(-2k^2/k_0^2)$, $k_0=8$; turbulent Mach number $M_t=0.8$, 1.0, 1.2, 1.6 |
| [Seta & Federrath (2022)](/sources/seta-2022.md), §2 | forced, MHD, two-phase (heating and cooling) | not given; $Re=Rm=2000$ at the driving scale | none | DNS only, $512^3$, 200 pc box | solenoidal or compressive driving at $1\le kL/2\pi\le3$ to $u_{\mathrm{rms}}\approx10$ km/s; seed field $10^{-10}$ G |
| [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §III, §IV | forced (a priori); decaying (a posteriori) | 170, 240, 355 (a priori); 240 (a posteriori) | pseudo-spectral, $320^3$, $520^3$, $1024^3$; ten snapshots per $Re_\lambda$ | a priori box filters of dimensionless size 2 to 32; LES at sizes 4 and 20 from the $520^3$ DNS | decaying runs started from the filtered statistically stationary field; large-eddy turnover time about 2.7 |
| [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.2 | decaying (grid turbulence of Comte-Bellot & Corrsin) | not given; $U_0M_g/\nu=34{,}000$ on the grid mesh size $M_g$ | experiment, spectra at $tU_0/M_g=42$, 98, 171 | $32^3$, $64^3$, $128^3$ nodes, second-order finite volumes, SA- and SST-based LES | field built from the measured spectrum; turbulent Mach number 0.1 |
| [Gan et al. (2022)](/sources/gan-2022.md), §2 | forced, compressible isothermal MHD with a strong guide field | not given | none | ideal MHD, $512^3$ ($8\pi\times2\pi\times2\pi$ in one run), ATHENA++ | Ornstein–Uhlenbeck forcing at $0<\lvert\boldsymbol k\rvert\le2$, incompressible or compressible velocity driving; $v_A=8$, $\beta_p=0.4$, turbulent Mach number 0.12–0.18 |
| [Kurz et al. (2023)](/sources/kurz-2023.md), §3–4, Table 2 | forced | about 180 (training and tests); about 240 (generalization) | DNS spectrum and velocity PDF, resolution not stated | DG: $N=5$ on $4^3$, $6^3$, $8^3$ elements and $N=7$ on $4^3$ (24, 36, 48 and 32 DOF per direction) | Rogallo initialization, linear (Lundgren) forcing; Mach 0.1; large-eddy turnover time about 0.7 |
| [Kang et al. (2023)](/sources/kang-2023.md), §2, §3, App. A | forced (training, a posteriori); decaying (a posteriori) | 106 and 286 (training), 164 (validation) | pseudo-spectral, $192^3$, $512^3$ ($256^3$ at 164); 37 to 50 snapshots | pseudo-spectral LES, $24^3$, $48^3$, $96^3$ at 106; $128^3$ at 286 | set-ups of Mohan et al. (106) and Chumakov (286), forcing wavenumbers 2 and 1.5; decaying runs started from the converged filtered field |
| [Wang et al. (2023c)](/sources/wang-2023-c.md), §III, App. A–B, Tables I, V | forced; decaying from the forced field (App. B) | about 160 (calibration); 259 (generalization) | pseudo-spectral, $512^3$ ($\nu=0.0025$) and $1024^3$ ($\nu=0.001$), 2/3 de-aliasing | pseudo-spectral LES, $64^3$, Gaussian filter $\Delta=16$ DNS spacings, filter-to-grid ratio 2; also $\Delta=32$ spacings at 259 | LES started from filtered fully developed DNS; forcing fixes the energy of the two lowest wavenumber shells |
| [Domaradzki (2024)](/sources/domaradzki-2024.md), §3.1–3.3, Table 1 | forced | nominal $1.2\times10^4$ to $1.6\times10^4$ ($\nu=2.5\times10^{-7}$) | none: inertial-range theory ($k^{-5/3}$, Kolmogorov constant 1.4–2.1) is the reference | de-aliased pseudo-spectral LES, $64^3$ and $32^3$, Gaussian or top-hat filter of width $2\Delta x$ | $k^{-5/3}$ or pulse initial spectrum, random phases, 50–100 precursor DNS steps; forcing of Sullivan, Mahalingam & Kerr at $k=3$; about 10 large-eddy turnover times |
| [Domaradzki (2024)](/sources/domaradzki-2024.md), §3.1–3.2, Table 2 | decaying (grid turbulence of Comte-Bellot & Corrsin) | measured 71.6, 65.3, 60.7 at $tU_0/M_g=42$, 98, 171 | experiment | de-aliased pseudo-spectral LES, $64^3$, $k_c=30$ | initialised from the measured spectrum at $tU_0/M_g=42$ |
| [Duan & Wang (2024)](/sources/duan-2024.md), §5.2 | decaying (grid turbulence of Comte-Bellot & Corrsin) | not given; $U_0M_g/\nu=34{,}000$ | experiment, spectra at $tU_0/M_g=42$, 98, 171 | flux reconstruction, $32^3$ cells, $N=2$ to 5 | box of $11M_g$; field matched to the measured spectrum at $tU_0/M_g=42$ (method of Kwak et al.) |
| [Li et al. (2024)](/sources/li-2024.md), §V A, Table I | forced | about 100 (training); 160, 250 (extrapolation) | pseudo-spectral, $256^3$, 2/3 de-aliasing, $\nu=0.00625$; 100 fields × 600 time nodes | sharp spectral filter $k_c=21$, $64^3$; LES with dynamic Smagorinsky and dynamic mixed models | large-scale forcing; LES forced at the two lowest wavenumbers like the filtered DNS |
| [Zhao et al. (2025)](/sources/zhao-2025.md), §3.1, Table 1 | decaying (from a forced state) | about 60 | pseudo-spectral, $128^3$, 2/3 de-aliasing, $\nu=0.015625$; 5000 training cases | sharp spectral filter $k_c=10$, $32^3$; Smagorinsky LES with $C_s=0.1$ | spectrum $\propto k^4\exp[-2(k/k_0)^2]$, forced in the first two shells for 10,000 steps, then released for 5000 steps |
| [Yeung et al. (2025)](/sources/yeung-2025.md), §2, Table 1 | forced | about 390, 650, 1000, 1600, 2500 | pseudo-spectral on GPUs, $2048^3$ to $32\,768^3$, single precision, final $k_{\max}\eta\approx2.8$ | DNS only | constant energy in the first three shells ($k<2.5$), after Donzis & Yeung |
| [Cernetic et al. (2024)](/sources/cernetic-2024.md), §4–§6, Table 1 | forced, isothermal, supersonic | not given; rms Mach 0.1 to 12.8 | none | no explicit model: modal DG ($N=1$, 2) and second-order finite volumes, $256^3$; $512^3$ and $1024^3$ at Mach 3.2 | solenoidal Ornstein–Uhlenbeck forcing at $k\in[2\pi,4\pi]$ ($L=1$) |
| [Beattie et al. (2025)](/sources/beattie-2025.md), §4, Table 1 | forced, isothermal MHD with explicit bulk viscosity | not given; $Re=Rm=1000$ on half the box, $M_t\approx1$ | none | DNS-type, finite volumes, $128^3$ to $1024^3$ | Ornstein–Uhlenbeck forcing at $kL/2\pi=2$, 2:1 solenoidal to compressive; seed magnetic energy $10^{-10}\rho_0c_s^2$ ($\rho_0$ mean density, $c_s$ sound speed) |
| [Wang et al. (2021)](/sources/wang-2021-l.md), §3.1, App. B | decaying (grid turbulence of Comte-Bellot & Corrsin) | not given | experiment, spectra compared at $t^*=2.0$ | LES branch of Reynolds-stress-model IDDES, second-order finite volumes, $64^3$ cells | field from the inverse Fourier transform of the measured spectrum; implicit dual time stepping, $\Delta t=0.001$ |
| [Brillon & Nadarajah (2026)](/sources/brillon-2026.md), §3.2, Table 6 | decaying (grid turbulence of Comte-Bellot & Corrsin) | 71.6 to 60.6 (experiment, as printed) | experiment, spectra at $tU_0/M_g=42$, 98, 171 | no-model nonlinearly stable flux reconstruction, $N=3$, $32^3$ elements ($128^3$ DOF, $96^3$ unique), $k_c=48$ | field from the measured spectrum at $tU_0/M_g=42$, Misra–Lund scaling, $M_\infty=7.874\times10^{-4}$, CFL 0.2 |
| [Ranjbar et al. (2026)](/sources/ranjbar-2026.md), §III.A, Table I | decaying (case idc96 of Blaisdell et al.) | not given; $Re_c=450$ | DGSEM, $N=8$, $12^3$ elements (1,259,712 points), checked against the authors' earlier DSEM code | DGSEM, $N=7$, $6^3$ elements (110,592 points): no model, Smagorinsky, modal filters | top-hat spectrum on $8\le k\le16$ for velocity and temperature; $\gamma=1.4$, $Pr=0.72$ |
| [Caban et al. (2026)](/sources/caban-2026.md), §4.2 | not stated | 100 | $384^3$ ("closely corresponding" to an earlier database) | a priori only: Gaussian filter $\Delta=2h$ on a 64-node grid, $k_c=16$ | not stated |
| [Wu & Lele (2026)](/sources/wu-2026.md), §3.2.1, §5, §6.1 | forced | 433 | Johns Hopkins database, $1024^3$, 5 snapshots | $64^3$ ($\Delta=16$ DNS spacings) in a Fourier code with 2/3 de-aliasing (PadeOps) and a sixth-order compact code without it (PadeLibs); $32^3$ ($\Delta=32$ spacings) in PadeOps | run to statistical stationarity; forcing not described in the version read |
| [Liang & Fu (2024)](/sources/liang-2024.md), §4.12 | decaying, compressible | 100 (initial) | filtered DNS on $256^3$ | no model: hybrid TENO / skew-symmetric-split finite differences (TENO-S), WENO-CU6, TENO6, TENO8, $64^3$ | solenoidal field, $E(k)\propto k^4\exp[-2(k/k_0)^2]$ ($k_0$ not printed), $M_t=0.6$ (with $\sqrt3\,u_{\mathrm{rms}}$ over the mean sound speed), other parameters as in the case of Johnsen et al. that the authors cite |
| [Wang et al. (2022)](/sources/wang-2022-j.md), §II, §IV, Table III | forced | 259 | pseudo-spectral, $1024^3$, 2/3 de-aliasing, $\nu=0.001$, $\eta/h_{\mathrm{DNS}}=1.01$ | $128^3$, Gaussian filter $\Delta=16$ DNS spacings, filter-to-grid ratio 2 | large-scale forcing at the two lowest wavenumbers; LES started from filtered DNS |
| [Zhang et al. (2022b)](/sources/zhang-2022-f.md), §IV, Table I | decaying, compressible, density-unweighted filtering | 259 and 261 (initial) | $1024^3$, hybrid eighth-order compact / seventh-order WENO | $128^3$, Gaussian filter $\Delta=16$ DNS spacings, ratio 2 | forced statistically steady fields at $M_t=0.40$ and 0.79 released to decay |
| [Zhang et al. (2022d)](/sources/zhang-2022-h.md), §II–IV, Tables II–III | decaying, compressible dense gas (PP11, Martin–Hou equation of state) | 162.6 and 151.8 (initial) | $512^3$, hybrid compact / WENO | $64^3$, Gaussian filter $\Delta=16$ DNS spacings, ratio 2 | forced steady states at $M_t=0.40$ and 0.80; near-critical reference state |
| [Hausmann et al. (2022)](/sources/hausmann-2022.md), §III B 1, Table I | forced | 75 | second-order finite volumes, $256^3$, $k_{\max}\eta=1.37$ | $32^3$, Smagorinsky $C_s=0.1$, with and without SGS velocity enrichment | forcing of Mallouppas et al. in the band $kL/2\pi=3$ to 6 |
| [Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.3 | decaying | not given; Reynolds number on the rms fluctuation about 60 and 500 | $256^3$ | P-DNS and a dynamic $k$-equation LES on $32^3$, $16^3$, $8^3$, $4^3$ | von Kármán–Pao spectrum |
| [Li et al. (2022)](/sources/li-2022-k.md), §III A | decaying (grid turbulence of Comte-Bellot & Corrsin) | not given; $U_0M_g/\nu=34{,}000$ | experiment, spectra at $tU_0/M_g=42$, 98, 171 | LES branch of a dynamic Reynolds-stress-model IDDES, second-order Roe finite volumes, $64^3$ cells | Rogallo's method matched to the measured spectrum at 42; turbulence variables initialized on the frozen velocity field; three-stage Runge–Kutta |
| [Deng et al. (2022)](/sources/deng-2022.md), §4.15 | decaying, compressible, "with eddy shocklets" | 100 (initial) | $256^3$ DNS of Johnsen et al. | no model: finite-volume $P_nT_m$-BVD-AD schemes (polynomial and THINC candidates selected by boundary-variation diminishing, with adjustable dissipation), 6th to 10th order, and ninth-order WENO-M, $64^3$ and $128^3$ | $E(k)\propto u_{\mathrm{rms},0}^2k^4k_0^{-5}\exp(-2k^2/k_0^2)$, $k_0=4$, $M_t=0.6$, uniform initial density and pressure, power-law viscosity; spectra at $t/\tau=4$ ($\tau$ the initial eddy time of the case) |
| [Valencia et al. (2026)](/sources/valencia-2026.md), §IV, §V A | decaying, compressible | 100 (initial, with the Taylor microscale set to $2/k_0$) | finite-volume DNS in PeleC (Godunov, PPM with seventh-order WENO-Z), $512^3$, CFL 0.5, run to four initial eddy-turnover times $2/(k_0u_{\mathrm{rms},0})$; verified against the Motheau–Wakefield data | a priori only: top-hat filter and downsampling to $128^3$, $64^3$, $32^3$, then a Gaussian filter of width $\Delta=4h$, $2h$, $h$ (all $\Delta=16$ DNS spacings) | $E(k)\propto k^4\exp[-2(k/k_0)^2]$, $k_0=4$, $M_t=0.6$ (with $\sqrt{\langle u_iu_i\rangle}$), $T_0=1200$ K, $p_0=101.3$ kPa, $Pr=0.71$, constant viscosity and conductivity |
| [Kuya et al. (2018)](/sources/kuya-2018.md), §5.1, §5.3, App. C | decaying, compressible, inviscid (Euler) | infinite (no viscosity) | none; the de-aliased spectral run of Honein & Moin is the comparison at $M_{t0}=0.07$ | no model: second-order central split-form fluxes, $32^3$, classical fourth-order Runge–Kutta at CFL about 0.1, run to $t/T_E=180$ | $E(k)=A(k/k_0)^4e^{-2(k/k_0)^2}$, $k_0=6$, $A$ set by the initial turbulent Mach number $M_{t0}=0.07$ or 0.3; uniform initial $T$ and $\rho$; set-up of Honein & Moin except the CFL |
| [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md), §6.1 | decaying (grid turbulence of Comte-Bellot & Corrsin) | not given; $U_0M_g/\nu=34{,}000$ (§6.1) | experiment | continuous Galerkin finite elements, van Cittert approximate deconvolution of order 8 with an explicit differential filter, no eddy viscosity: $64^3$ hexahedra, the same with 20% node perturbation, and a tetrahedral mesh of 64 edge segments per side | method of Kwak et al. on $512^3$, interpolated to the LES meshes; compressible at reference Mach 0.1 |
| [Iwata et al. (2023)](/sources/iwata-2023.md), §II C, Table I | decaying, compressible, as the inflow of a detonation DNS | 240 | none (the field itself is a DNS) | DNS on a 4 µm grid in a 1.92 mm periodic cube ($480^3$); $k_{\max}\eta=2.31$ and 4.25 in the two gas mixtures | $E(k)\propto(u'^2_{\mathrm{rms}}/k_e)(k/k_e)^4\exp[-2(k/k_e)^2]$ ($k_e$ page-local, the energy-peak wavenumber), decayed until the velocity-derivative skewness lies between $-0.6$ and $-0.4$; turbulent Mach number 0.30 |
| [Li et al. (2021)](/sources/li-2021.md), §II A, §III A, §III C, §III E | forced, incompressible | about 260 (training and main tests); 180 and 250 (generalization) | pseudo-spectral, $1024^3$ (data of Xie et al.), second-order Adams–Bashforth, 2/3 de-aliasing | pseudo-spectral LES, $128^3$, top-hat filter $\Delta=16$ DNS spacings (filter-to-grid ratio 2); also $64^3$ and $32^3$ ($\Delta=32$, 64 DNS spacings) | energy spectrum held fixed in the two lowest wavenumbers; a "high-order dissipative numerical method" carries the energy flux at the highest wavenumbers |

The beck-2023 DNS used 16,384 cores of the HAWK system for almost two hours
(about 30,000 CPU hours). [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md)
run their main experiments in two dimensions: Kolmogorov-forced turbulence
at $Re=6000$ (DNS $4096^2$, LES $\bar n=32$ to 256 per direction) and a 2D
decaying case (App. G.1). These are periodic-box turbulence but neither
three-dimensional nor isotropic in the 3D sense, and the paper does not
state the reference velocity and length behind $Re$.

## What the case tests

**Dissipation by implicit and explicit closures.**
[Flad & Gassner (2017)](/sources/flad-2017.md) use decaying HIT to show that
no-model DG LES with Riemann-solver dissipation and polynomial de-aliasing
matches the DNS at $144^3$ DOF, where 43.2% of the dissipation is resolved
at their 3-points-per-wavelength cutoff $k_c=48$, but fails at $48^3$ DOF,
where 0.9% is resolved at $k_c=16$ (energy pile-up at mid-range wavenumbers,
then a sharp drop). From these two resolutions they infer that roughly 40%
of the dissipation must be resolved for this
[implicit LES](/definitions/implicit-les.md) practice to work. On the
kinetic-energy-preserving split form they show that a
[Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.12$ (in the
squared form of their Eq. A.1) beats no-model DG LES at $48^3$ DOF (§4,
Fig. 7). [Beck & Kurz (2023)](/sources/beck-2023.md) find no single best
baseline across polynomial degrees: no-model LES is best at $N=3$,
Smagorinsky with $C_s=0.17$ over-damps high wavenumbers at $N=5$, and the
[dynamic procedure](/methods/dynamic-procedure.md) is close to DNS at 36 DOF
but deviates at 24 DOF; their
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
reach or exceed the best baseline in all cases except no-model LES at $N=3$
(§V, Figs. 8–14).

**A reinforcement-learned Smagorinsky coefficient for implicitly filtered DG LES.**
[Kurz et al. (2023)](/sources/kurz-2023.md) (read in arXiv v2), from the
same group and on the same forced case at $Re_\lambda\approx180$ as
[Beck & Kurz (2023)](/sources/beck-2023.md), train with
[Relexi](/software/relexi.md) and [FLEXI](/software/flexi.md) a policy that
sets an element-wise Smagorinsky coefficient $C_s\in[0,0.5]$ from
element-local momentum alone, rewarded by the error of the instantaneous
spectrum against the time-averaged DNS spectrum up to a cutoff of 2.6 to 3
points per wavelength (§3.4–3.5, Table 2). A posteriori, from an unseen
initial state and over four times the training horizon, the policies are
stable; no-model LES piles up energy at high wavenumbers, static
Smagorinsky with $C_s=0.17$ over-dissipates near the resolution limit, the
dynamic Smagorinsky model matches the RL model except at 24 DOF, where the
RL model is "significantly better" and the authors suspect the test filter
lies outside the scale-similar range (§4.2, Fig. 6). The predicted $C_s$
shrinks with resolution (up to 0.5 at 24 DOF, at most 0.3 at 48 DOF); the
36- and 48-DOF policies transfer to each other's resolution and to
$Re_\lambda\approx240$ (§4.4–4.5, Figs. 8–9). Policies fed with the five
velocity-gradient invariants train slower and end worse (§4.3, Fig. 7). See
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
and [discretization-consistent closure](/definitions/discretization-consistent-closure.md).

**A neural-network mixed model, a priori and a posteriori.**
[Kang et al. (2023)](/sources/kang-2023.md) train a two-layer, 12-neuron
[neural-network SGS model](/methods/neural-network-sgs-model.md) on
filtered DNS of forced HIT at $Re_\lambda=106$ and 286 (§2, Table 1). With
the resolved strain alone as input, the network predicts a stress almost
aligned with the strain (correlation of its $\tau_{12}$ with $\bar S_{12}$
of $-0.82$, against $-0.28$ for the filtered-DNS stress), no backscatter, and LES almost identical to
the dynamic Smagorinsky model (§3.1, Table 3, Figs. 4–6). Adding the
resolved stress $L_{ij}$ as input doubles the a priori stress correlation
(0.70–0.72 against 0.35–0.37), reproduces the PDF of the SGS dissipation
including backscatter, and runs stably with no averaging or clipping (§3.1,
Table 4, Fig. 8). Trained at one Reynolds number and resolution, with inputs
and output normalized by volume-averaged norms, it predicts decaying HIT at
$24^3$ to $128^3$ and $Re_\lambda=106$ and 286 better than dynamic
Smagorinsky (§3.2, Table 5, Figs. 13–17), and beats the algebraic dynamic
mixed models a posteriori although they correlate as well or better a priori
(§3.3, Table 6, Figs. 19–22), at 0.71 of the cost of the dynamic
Smagorinsky stress evaluation (§3.4). The algebraic dynamic models diverge
within tens of steps without averaging and clipping (Fig. 20). See
[energy backscatter](/definitions/energy-backscatter.md) and
[scale-similarity models](/methods/scale-similarity-model.md).

**Dissipation of a non-Boussinesq model.**
[Agrawal et al. (2022)](/sources/agrawal-2022.md) use decaying HIT to show
that the [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
dissipates as well as the dynamic Smagorinsky model: both follow filtered DNS
in kinetic energy and dissipation after a transient of up to one eddy
turnover, with decay exponents $K\sim t^{-1.35}$ for both against
$t^{-1.37}$ for the box-filtered DNS (Figs. 3–4). In forced HIT at
$Re_\lambda=315$ both models recover the $k^{-5/3}$ range of the filtered
DNS spectrum (Fig. 5).

**Equipartition without dissipation.** Three sources agree that a
discretization without subgrid dissipation drives the resolved spectrum
towards energy equipartition, $E(k)\sim k^2$, near the cutoff:
[Agrawal et al. (2022)](/sources/agrawal-2022.md) for a no-model LES as
$Re_\lambda\to\infty$ (§VII.C, Fig. 6);
[Flad & Gassner (2017)](/sources/flad-2017.md) for the dissipation-free split-form
DG scheme at $48^3$ DOF, which stays stable (§3, Fig. 4); and, on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) for
truncated Euler and no-model runs (§6.2). This is the statement of the
benchmark that a stable, energy-conserving scheme must be supplemented by
dissipation, explicit or numerical. [Prakash et al. (2022)](/sources/prakash-2022.md),
§III.B.1, Fig. 4, find the same failure in forced HIT at effectively
infinite Reynolds number with a stabilized finite-element solver: the
no-model run (stabilization only) and the unclipped
[gradient model](/methods/gradient-model.md), whose a priori dissipation is
too low, both pile up energy at the highest resolved wavenumbers. Dynamic
Smagorinsky has no pile-up and follows the $k^{-5/3}$ slope but over-predicts
intermediate wavenumbers, as does the dynamic mixed model; the gradient model
with standard or optimal clipping of its backscatter gives the best spectra,
optimal clipping a slightly longer inertial range. The authors state, without
showing it, that the dissipation of the stabilization is much smaller than
the SGS dissipation of every explicit model.
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md), §IV, Fig. 8, find the
same pile-up in decaying HIT with a pseudo-spectral solver: the no-model run
on the LES grid accumulates energy at high wavenumbers, the Smagorinsky
model over-dissipates, and their dynamic
[fractional SGS model](/methods/fractional-sgs-model.md) lies between the two,
closest to the filtered DNS.

**A priori structure of structural models.**
[Prakash et al. (2022)](/sources/prakash-2022.md), §III.A, Figs. 1–3, box-filter
the Johns Hopkins forced database at $Re_\lambda=418$ to test the gradient
model. Unclipped, it is highly correlated with the exact SGS stress at all
filter widths but under-predicts the mean SGS dissipation. Standard clipping
(zeroing the stress where it backscatters) restores dissipation and lowers the
correlation, more under anisotropic book- and pencil-type filters; optimal
clipping (the nearest stress without local backscatter) keeps the unclipped
correlation and gives the same mean dissipation as standard clipping. See
[energy backscatter](/definitions/energy-backscatter.md) and
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

**Compressible decaying turbulence as a DNS test.**
[Cao et al. (2022)](/sources/cao-2022.md), §3.4, run decaying compressible
isotropic turbulence with their
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
at initial $Re_\lambda=72$ and turbulent Mach number $M_t=0.8$ to 1.6
(defined with $\sqrt3\,u_{\mathrm{rms}}$ over the sound speed), $512^3$
cells, viscosity $\propto T^{0.76}$, up to five large-eddy turnover times.
WENO-Z reconstruction in characteristic variables and a collision time
enlarged at pressure jumps keep the runs stable "without extra special
treatment", and the time histories of density rms, kinetic energy, velocity
derivative skewness and flatness, and of the dissipation are offered as
benchmark data. With rising $M_t$ the normalized density rms
$\rho_{\mathrm{rms}}/M_t^2$ decreases, the peak total dissipation grows, its
solenoidal part $\varepsilon_s=\langle\mu\,\omega_i\omega_i\rangle$ decreases
and its dilatational part $\varepsilon_d=\tfrac43\langle\mu(\nabla\cdot\boldsymbol u)^2\rangle$
increases; the pressure–dilatation correlation changes sign and stays small
and positive later, as in the subsonic results of Sarkar et al. that the
authors cite (Figs. 13–14; $\varepsilon_s$, $\varepsilon_d$ as in
registry §11).
Shocklets, regions where the dilatation is below $-3$ times its rms, appear as
long narrow ribbons beside block-like expansion regions (Fig. 15). The
resolution criterion $k_{\max}\eta_0\ge2.71$ is taken from the authors'
earlier work. The authors state that compact finite differences are limited
to $M_t\le0.8$ and that spectral and lattice Boltzmann methods fail to capture
shocklets (§1, §3.4).

[Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md), §3.1,
Fig. 2, use compressible decay as the first validation of their
curvilinear immersed-boundary LES code: initial spectrum
$E(k)=A k^4\exp(-2k^2/k_0^2)$ with $k_0=6$ and unit initial kinetic
energy, $M_t=u'/c=0.4$ with their fluctuation velocity $u'$ and sound
speed $c$, $Re_\lambda=153$,
$16^3$, $32^3$ and $64^3$ cells, the compressible
[dynamic Smagorinsky](/methods/dynamic-procedure.md) model and a hybrid of
skew-symmetric central and third-order WENO fluxes. On $64^3$ the spectrum
at five initial eddy turnover times follows the $-5/3$ law over an
inertial range, and the kinetic-energy history agrees with the DNS of
Samtaney et al. after two turnover times; the earlier discrepancy, also
present in the LES of Li et al. at similar resolution, is attributed to
the coarser resolution than the DNS.

**Small-scale statistics at record Reynolds number.**
[Yeung et al. (2025)](/sources/yeung-2025.md) reach $Re_\lambda\approx2500$
on a $32\,768^3$ grid with a GPU Fourier pseudo-spectral code on the Frontier
exascale machine (13 s per step on 44% of it). A long run at that size being
unaffordable, they use
[multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md):
a long run at $k_{\max}\eta\approx1.4$ and Courant number 0.6, a short one
at halved time step, and a short one at halved grid spacing
($k_{\max}\eta\approx2.8$), each of a few Kolmogorov times, averaged over
three or four independent segments; the Reynolds number is raised by
lowering $\nu\propto N_x^{-4/3}$ at fixed forcing, so that
$Re_\lambda\propto N_x^{2/3}$ (§2.2, Table 1). Findings (§3–§4, Figs. 2–6):

- **Dissipative anomaly.** The normalized dissipation
  $C_\varepsilon=\langle\varepsilon\rangle L/u'^3$ (page-local; $L$ the
  longitudinal integral scale, $u'$ the rms of one component) has a weak
  trend up to $Re_\lambda\approx1500$ and then stays at a constant "slightly
  larger than 0.4": the zeroth law holds beyond $Re_\lambda=2500$. The
  classical scalings $Re_L=C_\varepsilon Re_\lambda^2/15$,
  $L/\eta\propto Re_\lambda^{3/2}$ and a turnover time over $\tau_\eta$
  proportional to $Re_\lambda$ hold. The authors note that these
  conclusions "would differ" without the two highest Reynolds numbers (§5).
- **No inertial plateau.** The compensated spectrum
  $E(k)\langle\varepsilon\rangle^{-2/3}k^{5/3}$ has no plateau: the slope is
  steeper than $-5/3$ (an intermittency correction), and a
  [bottleneck](/definitions/bottleneck-effect.md) peaks at
  $k\eta\approx0.1$–0.2, just below the peak of the dissipation spectrum
  $k^2E(k)$, weaker in the one-dimensional spectrum than in $E(k)$ (§3,
  Fig. 3).
- **Intermittency of dissipation and enstrophy.** Very low and very high
  values of enstrophy are both more probable than those of dissipation. The
  left tails of the PDFs follow chi-square laws of order 3 (enstrophy) and 5
  (dissipation), so that the enstrophy PDF goes as the cube root of the
  dissipation PDF at small arguments, a kinematic result holding at
  $Re_\lambda=390$ and 2500 (Eq. 4.1); the right tails are stretched
  exponentials with about equal exponents; normalized moments of orders 2
  to 4 are larger for enstrophy, but their ratio is nearly independent of
  $Re_\lambda$, which the authors call consistent with the argument of
  Nelkin (1999) (§4, Eq. 4.2, Fig. 6).
- **Data.** One $32\,768^3$ snapshot (velocity and pressure, about half a
  petabyte) is in the Johns Hopkins Turbulence Database (§2.2).

See [direct numerical simulation](/definitions/direct-numerical-simulation.md).

**The code behind the exascale runs.** [Yeung et al. (2025b)](/sources/yeung-2025-b.md)
describe GESTS, the GPU Fourier pseudo-spectral code of these runs, on the
same flow (incompressible, forced, $2\pi$-periodic, single precision): the
Rogallo algorithm with an exact integrating factor, second-order
Runge–Kutta, phase shifting and truncation at $k_{\max}=\sqrt2N_x/3$, the
whole problem resident in GPU memory with OpenMP offloading, rocFFT and
GPU-aware all-to-all transposes in slab or pencil decompositions (§2–§3).
The benchmark runs report performance only, with no Reynolds number or
flow statistics: $32\,768^3$ on 4096 Frontier nodes takes 12.07 s per step
in the slab code, 6.6 times the figure of merit of the earlier $18\,432^3$
record on Summit, with communication dominating the cost (§4, Table 2).
The algorithm and its scaling are on
[direct numerical simulation](/definitions/direct-numerical-simulation.md).
For the same grid, [Yeung et al. (2025)](/sources/yeung-2025.md) quote
13 s per step on 44% of Frontier (above), and Yeung et al. (2025b),
Table 2, print 13.07 s (April 2023) and 12.07 s (April 2024) on 4096 of
its 9408 nodes.

**Supersonic isothermal turbulence.**
[Cernetic et al. (2024)](/sources/cernetic-2024.md) drive isothermal
turbulence from Mach 0.1 to 12.8 with no explicit viscosity, comparing a
GPU modal DG code with a second-order finite-volume scheme. All schemes
reproduce the change of spectrum from $k^{-5/3}$ to $k^{-2}$ with
increasing Mach number; DG extends the resolved range in the subsonic runs,
with a more pronounced bottleneck at $N=2$, but the gain "nearly
disappears" in the supersonic ones; density PDFs are nearly
scheme-independent at $256^3$ (§5, Figs. 5–7). At Mach 3.2 and $1024^3$,
DG resolves the sonic scale $l_s=L_{\mathrm{inj}}/M^2$ (page-local, Eq. 22)
where the finite-volume run does not (§6). Turbulence is fully developed only
after two turnover times, and statistics are averaged over three to eight
(§4.2, Fig. 9). Detail on
[shock-generated turbulence](/results/shock-generated-turbulence.md).
[Chapelier et al. (2024)](/sources/chapelier-2024.md), §I, name compressible
isotropic turbulence with shocklets as the flow closest to the late stages
of the supersonic [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).

**Neural-operator surrogates of LES.** Two sources from one group replace the
LES solver by a network that advances the filtered field, tested a posteriori
against filtered DNS (see [neural-operator LES surrogates](/methods/neural-operator-les-surrogate.md)):

- [Li et al. (2024)](/sources/li-2024.md) (read in arXiv v2), §V A: in forced
  HIT at $Re_\lambda\approx100$ a transformer-based neural operator is
  comparable to dynamic Smagorinsky and better than a Fourier neural
  operator and the dynamic mixed model. Its spectrum is closer to filtered
  DNS than dynamic Smagorinsky for $3\le k\le17$ and less close for
  $k\ge18$; the dynamic mixed model under-predicts low and "significantly
  overestimates" high wavenumbers; velocity-increment PDFs stay consistent
  with filtered DNS where both dynamic models deviate (Figs. 6–10). Per time
  node it costs 12.48 CPU s or 1.021 GPU s against 105.6 and 166.4 CPU s for
  the two LES (Table I). Applied without retraining at $Re_\lambda\approx160$
  and 250, it gives better structure functions and increment PDFs than both
  dynamic models but a worse spectrum than dynamic Smagorinsky (Figs. 12–13).
- [Zhao et al. (2025)](/sources/zhao-2025.md) (read in arXiv v3), §3.1: in
  decaying HIT at $Re_\lambda\approx60$ a physics-informed neural operator
  trained only on the residual of the Smagorinsky-closed filtered equations
  stays stable and close to Smagorinsky LES over five turnover times, while a
  data-driven Fourier neural operator, best in test loss, deviates
  significantly after about two (Figs. 6–8); inference is about 30 times faster than the LES
  (Table 5). Learning the coefficient from one trajectory recovers
  $C_s\approx0.1$ from Smagorinsky-LES data and gives about 0.19 from
  filtered DNS, with comparable a posteriori results (§4).

The review of [Fang et al. (2026)](/sources/fang-2026.md), §5.2, lists
further cited operators on isotropic targets: a linear-attention Fourier
neural operator that "reduces the turbulence prediction error by 40%" on
three-dimensional isotropic and free-shear turbulence without added cost,
and an implicit U-Net-enhanced Fourier neural operator that beats the
Fourier, U-Net Fourier and dynamic Smagorinsky references and generalizes
to higher Taylor-scale Reynolds numbers.

**Driven MHD turbulence and the small-scale dynamo.**
[Seta & Federrath (2022)](/sources/seta-2022.md) drive turbulence in a
triply periodic box with heating and cooling, so that the gas splits into a
cold supersonic phase (3–4% of the volume by their text, rms Mach number about 5) and a
warm transsonic phase, and follow the growth of a weak seed field. Explicit
viscosity and resistivity at $Re=Rm=2000$ are chosen to exceed the numerical
diffusion, whose effective Reynolds number they estimate at about $2N_x^{4/3}\approx8000$
for $N_x=512$ (§2.4, from McKee et al.). The kinematic growth rate of the
magnetic-to-kinetic energy ratio is the same in both phases, $0.37$ and
$0.18$ per driving time for solenoidal and compressive driving, and both
growth rate and saturation level are lower than the isothermal empirical
model of Federrath et al. at matching Mach numbers (§4.1, Table 1); they
explain the equal growth rates through a vorticity budget (§4.2).
[Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) cite
turbulent-box simulations of this kind (Balsara et al.; Federrath;
Schekochihin et al.) as the reference for the growth rates and the
resolution scaling expected of the dynamo in galaxy simulations.
[Beattie et al. (2025)](/sources/beattie-2025.md) add an explicit
[bulk viscosity](/definitions/bulk-viscosity.md) to a forced trans-sonic
isothermal MHD box ($Re=Rm=1000$): without it the compressive velocity modes
pile up at high wavenumber, and the authors call such shear-viscous runs
"an implicit large eddy simulation for the compressible modes" (§6, §9.1);
growth rate and saturation of the dynamo barely change until the bulk
viscosity acts on the turnover time scale (§5). See
[small-scale dynamo](/results/small-scale-dynamo.md).

**A priori structure of the subgrid flux.**
[Vela-Martín (2022)](/sources/velamartin-2022.md) uses the forced database
to show that the mean local SGS flux $\langle\Pi\rangle$ equals $\varepsilon$
at all filter scales tested (inertial-range filtering) and that the
backscatter it contains can be moved into a conservative spatial flux by a
gauge transformation of the SGS stress (see
[energy backscatter](/definitions/energy-backscatter.md)). The flux the
paper writes $T$ equals the registry's $\Pi$, because the paper's SGS
stress has the opposite sign.

**Learned closures, a priori against a posteriori.**
[Duraisamy (2021)](/sources/duraisamy-2021.md), §IV.B, Fig. 2, cites
Sirignano, MacArt & Freund for the finding that an a priori-trained SGS closure
over-predicts the resolved kinetic energy of decaying HIT, while a
model-consistent (differentiable-physics) closure follows the filtered DNS.
[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), App. G.2, find
that in 3D forced turbulence ($\bar n=32,64$) a CNN closure in their
divergence-consistent formulation beats no model and Smagorinsky
($C_s=0.17$) in a priori and a posteriori error, while Smagorinsky is too
dissipative at high wavenumbers. See
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [model-consistent training](/methods/model-consistent-training.md).

**A nonlocal closure, a priori and a posteriori.**
[Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) use forced HIT at
$Re_\lambda=170$, 240 and 355 to fix the order of their dynamic
[fractional SGS model](/methods/fractional-sgs-model.md) a priori: the order
that maximizes the stress correlation with box-filtered DNS falls with the
filter size and rises with $Re_\lambda$, fitted by a power law of the
filter size (§III.1, Table I). At $Re_\lambda=240$ and dimensionless filter
sizes 4 and 8 the dynamic fractional model correlates better with the exact
SGS stress than static and dynamic Smagorinsky and the static fractional
model in all six components, and predicts a backscatter volume fraction
$v^-$ of 24% and 25% against 26% and 30% in the filtered DNS and 20% and 18%
for dynamic Smagorinsky (§III.2, Figs. 4–5; see
[energy backscatter](/definitions/energy-backscatter.md)). A posteriori in
decaying HIT at $Re_\lambda=240$, its resolved-energy decay is closer to the
filtered DNS than that of dynamic Smagorinsky at filter size 4 and, more
markedly, at the very-large-eddy filter size 20, where dynamic Smagorinsky
decays too fast (§IV, Fig. 9).

**An ensemble-calibrated mixed model.**
[Wang et al. (2023c)](/sources/wang-2023-c.md) (read in arXiv v3), §III,
calibrate a mixed model, the [gradient model](/methods/gradient-model.md)
with its Taylor-expansion coefficient $\Delta^2/12$ plus a Smagorinsky
term $-C_{\mathrm f}\Delta^2\lvert\bar S\rvert\bar S_{ij}$ ($C_{\mathrm f}$
page-local, the functional coefficient; the authors relate it to $C_s$ by
$C_{\mathrm f}=2C_s^2$), on forced HIT at
$Re_\lambda\approx160$ with an
[ensemble Kalman filter](/methods/ensemble-kalman-closure-calibration.md)
whose observations are the filtered-DNS energy spectra at several instants.
The calibrated $C_{\mathrm f}\approx0.00738$ (ensembles of 10 and 20
members, 50 iterations; Fig. 2, Table II) is much smaller than the
"classical" $2C_s^2\approx0.05$ with $C_s=0.16$ that the authors quote
(§III). A posteriori against filtered DNS (Figs. 3–9):

- the dynamic Smagorinsky and dynamic mixed models slightly over-predict
  large-scale and under-predict small-scale energy, the pure gradient model
  does the reverse, and the calibrated model is closest in spectrum and
  kinetic-energy history;
- the gradient model gives the best SGS-stress PDF but the worst kinetic
  energy, which the authors read as "accurately reconstructing the SGS
  stress may not guarantee the adequate prediction of other important flow
  statistics" (see [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md));
- the PDF of the SGS flux $\Pi$ is strictly positive for dynamic
  Smagorinsky, too wide (too much backscatter) for the gradient model, and
  closest to filtered DNS for the calibrated model (Fig. 8; see
  [energy backscatter](/definitions/energy-backscatter.md));
- longitudinal structure functions of order 2 to 8 are best predicted by
  the calibrated model, with an error that grows with the order (Fig. 9).

Without recalibration the model also beats the dynamic models at
$Re_\lambda=259$ with filter widths of 16 and 32 DNS spacings, where the
pure gradient model diverges at 16, and in decaying HIT from
$Re_\lambda=259$ (App. B, Figs. 19–21); the functional part alone,
recalibrated to $C_{\mathrm f}=0.01$, is markedly worse in the strain and rotation
PDFs and the SGS flux (App. C).

**An autonomous eddy viscosity at very high Reynolds number.**
[Domaradzki (2024)](/sources/domaradzki-2024.md) runs the
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md),
whose viscosity is computed at each step from the energy flux of a
similarity stress of the LES field with no adjustable constant, in forced
HIT at nominal $Re_\lambda$ above $10^4$ (Table 1). The spectra recover a
$k^{-5/3}$ range with a compensated Kolmogorov function between 1.4 and 2.1
outside the forcing band, with minor departures near $k_c$ (§3.1,
Fig. 1); halving the resolution to $32^3$ causes "no visible
deterioration", the top-hat filter over-damps the highest wavenumbers
slightly, and a pulse initial spectrum settles at a higher energy level
with nearly the same Kolmogorov function (Figs. 2–3). The author stresses
that the model assumes neither the inertial-range exponent nor the
Kolmogorov constant, which the Smagorinsky and Chollet–Lesieur models do
(§3.1, §3.3). With a constant $0.8$ that enforces the global SGS transfer
of the Gaussian filter, the Kolmogorov function rises steeply near $k_c$,
which the author reads as insufficient SGS dissipation there (§3.2, Figs. 7–8), and the model
then acts as a time-dependent, spatially near-uniform viscosity (§3.3,
Fig. 10); see [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md).
The author states that the de-aliased spectral code makes numerical
dissipation negligible, so the observed effects are those of the model
(§3.3).

**Decaying grid turbulence of Comte-Bellot and Corrsin.** Nine sources use
this experiment. The last two of the list below, De Cosmo et al. and Xiao
et al., start from fields matching the spectrum at $tU_0/M_g=42$ and
compare at 98 and 171 (Xiao et al. also at 42). Of the other seven, three
start a simulation from the measured spectrum at
$tU_0/M_g=42$ ($M_g$ the grid mesh size, 5.08 cm, and $U_0=10$ m/s in
Domaradzki, Duan & Wang and Brillon & Nadarajah; $U_0M_g/\nu=34{,}000$ in
Duan & Wang and Brillon & Nadarajah) and compare later spectra, at 98 and
171 in Domaradzki and in Brillon & Nadarajah and at 98 in Duan & Wang; two
use the case to set the dissipation of hybrid RANS/LES:

- [Domaradzki (2024)](/sources/domaradzki-2024.md), §3.1, Figs. 4–5:
  under-resolved DNS without a model fails on $64^3$, the autonomous LES
  predicts the spectrum evolution "quite well". LES against experiment
  (Table 2):

| $tU_0/M_g$ | $u'$ | $\varepsilon$ | $\lambda$ | $L$ | $Re_\lambda$ |
|---|---|---|---|---|---|
| 98, LES / exp. | 1.21 / 1.28 | 5.58 / 6.33 | 0.0774 / 0.0764 | 0.41 / 0.345 | 63.0 / 65.3 |
| 171, LES / exp. | 0.865 / 0.895 | 1.73 / 1.74 | 0.099 / 0.102 | 0.48 / 0.490 | 57.2 / 60.7 |

  (in the author's converted units, length unit 10 cm). With the constant
  0.8 the LES over-predicts the measured spectrum at high wavenumbers at 98
  and under-predicts its peak at 171 (§3.2, Fig. 9).
- [Duan & Wang (2024)](/sources/duan-2024.md), §5.2, Fig. 8, test filter
  widths for explicit SGS models in [flux reconstruction](/methods/flux-reconstruction.md)
  on $32^3$ cells: $\Delta=h$, $h/\sqrt{N+1}$ and $h/(N+1)$, with $h$ the
  cube root of the cell volume. At $N=2$ and 3 the spectra pile up at high
  wavenumbers, which the authors attribute to aliasing; at $N=4$ and 5 the
  low wavenumbers agree with experiment, and unmodelled
  [implicit LES](/definitions/implicit-les.md) departs most from it at high
  wavenumbers. The [WALE](/methods/wale-model.md) and
  [Vreman](/methods/vreman-model.md) models give similar spectra, Vreman
  slightly more damped; $h/(N+1)$ adds very little dissipation, $h$ too
  much (the range of resolved wavenumbers is considerably reduced), and the intermediate $h/\sqrt{N+1}$ is "a good balance" (see
  [large-eddy simulation](/definitions/large-eddy-simulation.md)).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) (read in arXiv
  v1), §3.2, run the case with no subgrid model in their entropy-stable
  [flux reconstruction](/methods/flux-reconstruction.md) (collocated
  $N=3$ on Gauss–Lobatto nodes, $32^3$ elements), the measured times
  $tU_0/M_g=42$, 98, 171 mapping to their $t^*=0$, 1, 2; the spectra at
  $t^*=1$ and 2 are "in good agreement with the experiment" (Fig. 22).
  They score the kinetic energy obtained by integrating each spectrum to
  the scheme's cutoff against the integrated measured spectrum at $t^*=2$
  (Eq. 112, Table 6):

| Scheme | DOF (unique) | $k_c$ | Relative error |
|---|---|---|---|
| sixth-order flux-difference splitting (Jefferson-Loveday & Tucker) | $64^3$ | 31 | 29.81% |
| CPR, $N=5$ (Vermeire et al.) | $78^3$ ($65^3$) | 31 | 15.55% |
| CPR, $N=1$ (Vermeire et al.) | $126^3$ ($63^3$) | 31 | 29.75% |
| nonlinearly stable FR, $N=3$ | $128^3$ ($96^3$) | 48 | 1.36% |
| the same, truncated | $128^3$ ($96^3$) | 31 | 5.30% |

  The authors expect the lower errors to be "partially due" to the larger
  number of unique DOF and to oversampling the high-order field onto
  $2(N+1)$ equidistant points per element before the FFT, which their
  Taylor–Green tests show is needed to avoid an apparent energy pile-up
  near $k_c$ (§3.1.1, Table 4; see
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)).
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md), §6.1,
  Fig. 6, test their approximate deconvolution with an explicit differential
  filter on unstructured finite elements (order 8; hexahedral filter set
  for a cut-off of about $3\pi/4$ in units of the local grid spacing; see
  [scale-similarity and mixed models](/methods/scale-similarity-model.md)
  and [explicit modal filtering](/methods/explicit-modal-filtering.md)):
  on the $64^3$ Cartesian, the 20%-perturbed and the tetrahedral meshes
  the spectrum follows a $-5/3$ range below $k=8/\Delta x$ and is
  suppressed completely at the grid cut-off. The tetrahedral mesh is
  slightly more dissipative but keeps some energy beyond the structured
  cut-off, because the filter adapts to the smaller local element size.
  The spectra are compared at $t^*=48.3$, a time the text does not relate
  to the measured stations. Their Taylor–Green tests are on
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).
- [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.2 (below): the
  case measures the scheme dissipation of hybrid RANS/LES.
- [Wang et al. (2021)](/sources/wang-2021-l.md), §3.1 (below): the case
  calibrates $C_{DES}$ of Reynolds-stress-model IDDES.
- [Li et al. (2022)](/sources/li-2022-k.md), §III A (below): the case
  checks the dynamic version of that IDDES.
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md), §3.2, Figs. 4–5,
  use the decay to calibrate the dissipation of their low-dissipation Roe
  scheme for [implicit LES](/definitions/implicit-les.md) in a second-order
  unstructured finite-volume code (the scheme sets the entropy and
  vorticity eigenvalues of the Roe dissipation to zero and scales the
  acoustic ones by a coefficient $c_{\mathrm{diss}}$, page-local): box
  side $0.09\cdot2\pi$ m, $Re=34{,}000$ on $V_0=10$ m/s and $M_g=0.0508$ m,
  initial field of 5000 random modes matching the spectrum at $tU_0/M_g=42$,
  comparison at 98 and 171 on $32^3$, $64^3$ and $128^3$ cells, against the
  experiment and an OpenFOAM LES with the [WALE model](/methods/wale-model.md).
  With $c_{\mathrm{diss}}=0.001$ both codes catch the $-5/3$ slope and
  depart from it only near the Nyquist wavenumber, less on finer grids, the
  OpenFOAM run being "slightly less dissipative"; on $64^3$ at 98, larger
  values steepen the inertial range and lower the energy, smaller ones
  flatten the spectrum and pile energy up near Nyquist. The authors find
  that the coefficient cannot be set to the smallest stable value, as
  earlier works they cite did, "as this would spoil the energy decay in the
  inertial range" (see [numerical dissipation](/properties/numerical-dissipation.md)).
- [Xiao et al. (2025)](/sources/xiao-2025.md), §4.1, Fig. 5, validate the
  subgrid models of the GPU LES solver [CaLES](/software/cales.md)
  (second-order staggered finite differences): box edge $9\times2\pi$ cm
  ($\approx11M_g$), $32^3$ and $64^3$ cells ($\Delta/\eta=60$ and 30 at
  $tU_0/M_g=42$), $Re_\lambda=71.6$ at 42 and 60.6 at 171, initial fields
  generated on the LES grid with a spectral cut-off or on $256^3$ and
  box-filtered, comparison at 42, 98 and 171. The
  [Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.18$
  predicts the spectra on both grids for either filter, except on the
  coarse grid with the box filter, where 0.22 is needed (not shown); the
  [dynamic procedure](/methods/dynamic-procedure.md) agrees reasonably,
  nearly perfectly with the box filter, which the authors call
  consistent with its box test filter; deviations near the Nyquist limit are attributed to the
  finite-difference errors.

In Domaradzki, Duan & Wang and Carlsson et al. the departures that separate the models lie at
high wavenumbers: the constant-0.8 variant (Domaradzki, Fig. 9) and
unmodelled implicit LES (Duan & Wang, Fig. 8) depart there, as do the
widest filter width (Duan & Wang) and the RANS-type artificial dissipation
(Carlsson et al., Fig. 3) by damping.

**Numerical dissipation of hybrid RANS/LES schemes.**
[Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.2, Fig. 3, run the
decaying grid turbulence of Comte-Bellot & Corrsin with the LES branch of
Spalart–Allmaras- and SST-based
[detached-eddy simulation](/methods/detached-eddy-simulation.md) in an
unstructured second-order finite-volume code. With the fourth-difference
artificial-dissipation coefficient of RANS practice ($1/128$) the spectra
decay too steeply at high wavenumbers on all three grids; the
[low-dissipation low-dispersion scheme](/methods/low-dissipation-low-dispersion-scheme.md)
with $1/512$ or $1/1024$ matches the measured spectra, $1/512$ being only
slightly more dissipative. With it the constants $C_{DES}=0.65$
(Spalart–Allmaras) and 0.61 (the $k$-$\varepsilon$ branch of SST), which the
authors call standard, need no recalibration; 0.78 for the $k$-$\omega$ branch gives nearly identical
results (not shown). The authors conclude that in this case the numerical
dissipation of the convection scheme dominates the decay of turbulent
kinetic energy (§5). See [numerical dissipation](/properties/numerical-dissipation.md).

**Calibrating $C_{DES}$ of a Reynolds-stress-model DES.**
[Wang et al. (2021)](/sources/wang-2021-l.md), §2.3, derive under an
equilibrium assumption a theoretical DES constant that depends only on
the coefficients of the length-scale equation and on $C_s$: with $C_s=0.18$
it is 0.805 for the $\omega$ branch and 0.630 for the $\varepsilon$ branch,
the same for the LRR and SSG
[Reynolds-stress models](/methods/reynolds-stress-model.md) as for SST,
against the calibrated SST-DES values 0.78 and 0.61 that they cite. They state
that the theoretical value "only provides a reference" because numerical
dissipation shifts it, and calibrate on the Comte-Bellot–Corrsin decay
($64^3$ cells, spectra at $t^*=2.0$) with the adaptive-dissipation Roe
scheme of their applications: $C_{DES,SSG}=0.3$ and $C_{DES,LRR}=0.5$ fit
the measured spectra, while SSG 0.4, 0.5, 0.61 and LRR 0.65, 0.78 "yield
too much dissipation in the small turbulent scales" (§3.1, Fig. 1). With
the plain Roe scheme and its dissipation factor lowered to 0.05, the same
values "show better performance at the high-wavenumber" (App. B, Fig. B1).
They set the direction of a calibration from the inertial-range level:
$C_{DES}$ is lowered when the spectrum lies below the experiment (§3.1).
See [detached-eddy simulation](/methods/detached-eddy-simulation.md).
Wang et al. and Carlsson et al. agree that scheme dissipation decides the
constant that matches this experiment; their hosts (Reynolds-stress model
against Spalart–Allmaras and SST) and schemes differ, and neither runs the
other's combination, so their different constants are not in conflict.

[Li et al. (2022)](/sources/li-2022-k.md), §III A, Figs. 2–3, remove the
calibration: in their RSM-DynIDDES the constant is $C_{DES}=C_kC_s$ with
$C_s$ from the compressible [dynamic procedure](/methods/dynamic-procedure.md)
(test filter as a volume-weighted average over the direct neighbours of each cell, Lilly's least squares,
negative $C_s^2$ clipped to zero) and $C_k$ a fixed factor of the
length-scale equation. On the same $64^3$ decay, started at $tU_0/M_g=42$
from a Rogallo field that matches the measured spectrum, with the
turbulence variables initialized by solving their equations on the frozen
velocity field, the spectra at 171 agree with the experiment up to the
high wavenumbers for both the SSG and LRR branches. They descend
"slightly" at high wavenumbers as $C_k$ grows, a difference the authors
call "small enough to be ignored", so the method is not sensitive to
$C_k$; the chosen $C_k=1.67$ (SSG) and 2.78 (LRR) return the calibrated
0.3 and 0.5 of Wang et al. (2021) at $C_s=0.18$ (§III A). The tested $C_k$
range appears only in Fig. 3.

**Driven compressible MHD turbulence with a guide field.**
[Gan et al. (2022)](/sources/gan-2022.md) drive isothermal compressible MHD
in a periodic box threaded by a strong uniform field and decompose the
fluctuations into Alfvén, fast and slow modes. A spatial projection onto the
linear eigenvectors assigns 0.137 of the power outside the injection range
to fast modes under compressible driving; a space–time Fourier analysis that
counts only power within ±10% of each mode's linear frequency assigns 0.024
to fast modes and 0.73 to 0.79 to fluctuations on no linear branch
(§3, Fig. 2). The guide field makes the box anisotropic; see
[compressible MHD turbulence](/results/compressible-mhd-turbulence.md).

**Not this case: decaying MHD from the Orszag–Tang vortex.**
[Foldes et al. (2023)](/sources/foldes-2023.md) test a
[lattice Boltzmann](/methods/lattice-boltzmann-method.md) MHD code on a
triply periodic box too, but their initial field is the deterministic 3D
Orszag–Tang vortex, not isotropic turbulence (§4.4, §5); that test is
recorded on [decaying MHD turbulence](/results/decaying-mhd-turbulence.md).

**A self-tuning explicit modal filter in DGSEM.**
[Ranjbar et al. (2026)](/sources/ranjbar-2026.md) (read in arXiv v1),
§III.A, test their
[explicit modal filter](/methods/explicit-modal-filtering.md) in
[HORSES3D](/software/horses3d.md) first on decaying HIT, chosen as the case
for "small-scale turbulence". On the coarse mesh ($N=7$, $6^3$ elements,
110,592 points against 1,259,712) the unmodelled run over-predicts the
turbulent kinetic energy, which the authors attribute to the missing
subgrid dissipation. A [Smagorinsky model](/methods/smagorinsky-model.md)
with $C_s=0.12$, the value that "yields the optimal results in this case",
agrees with the DNS but over-dissipates for $t>2.4$. Their earlier filter
with a user-chosen number of removed mode groups brackets the DNS (six
groups better early, seven better after $t=3.6$), and the self-tuning
filter with its constant $c=0.65$ agrees best (Fig. 3). Its cut-off mode,
averaged over the elements, rises from 3.815 at $t=2$ to 5.923 at $t=6$
with standard deviations of 0.08 to 0.15, so the filtering weakens as the
turbulence decays and varies little in space (Fig. 5); element averages of
the strain and rotation invariants, too large on the unmodelled coarse
mesh, come "very close to the DNS results" with the filter (Fig. 6). A
10% and 20% decrease of $c$ gives values 0.042 and 0.105 of their error measure (Eq. 51),
and in the late, nearly laminar decay the energy above the cut-off becomes
negligible, so the filter switches itself off (§III.D.2, §III.D.4,
Figs. 17–18).

**Training filters for neural-network closures.**
[Wu & Lele (2026)](/sources/wu-2026.md) (read in arXiv v2) train a
tensor-basis graph [neural-network SGS model](/methods/neural-network-sgs-model.md)
on the forced Johns Hopkins database at $Re_\lambda=433$ (and channel
flow), filtered at 16 and 32 DNS spacings with a box filter, a compact
raised-cosine filter, or a box filter followed by a 2/3 spectral cutoff,
and run it a posteriori in forced HIT on $64^3$ in two solvers (§3.2, §5).
Their sum spectral error (SSE), the summed absolute difference of the
logarithms of the filtered-DNS and LES spectra, ranks the models (Tables
3–4); the authors warn that it is "artificially sensitive" to the
dissipative range and needs visual inspection (§5).

- In the Fourier code (Table 3, §5.1): static Smagorinsky with coefficient
  0.18 (SSE 16.6) and the [sigma model](/methods/sigma-model.md) with
  coefficient 1.3 (13.34) over-dissipate; the network trained on box-filtered
  data with the full set of velocity-gradient invariants as inputs
  under-dissipates and piles up energy at high wavenumbers (18.87); trained
  on box plus box-and-cutoff data it is best (4.0). The algebraic models
  reproduce the longitudinal flatness better, which the authors attribute to
  over-dissipation lowering its denominator; the networks reproduce the PDF
  of resolved enstrophy production far better (Fig. 5).
- In the sixth-order compact code without de-aliasing (Table 4, §5.2): the
  box-only network shows "an extreme buildup of high wavenumber energy"
  (SSE 32.58), box plus raised-cosine training gives 11.93, and a single
  three-filter network, run in both codes without retraining, beats the
  box-only one in both (14.22 here).
- With "simple" inputs, the strain and rotation magnitudes (plus the
  velocity-gradient trace, masked to zero), all variants give consistent spectra (SSE 3.68–4.98 in the Fourier
  code; §5.1.3); an extra layer normalization alone rescues the box-only
  network (SSE 5.56), so single-filter results are "very sensitive to the
  neural network architecture" (§5.1.2).
- On $32^3$ (Fourier code only) two-filter training again removes the
  under-dissipation; the sigma model over-dissipates less than at $64^3$
  "despite using the same coefficient", and no model captures the
  enstrophy-production PDF (§6.1, Figs. 13–14).

A priori, all networks agree within 5% in stress and dissipation error and
correlation (Table 2), so the filter choice shows only a posteriori; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)
and [discretization-consistent closure](/definitions/discretization-consistent-closure.md).

**A priori error of approximate deconvolution with a mismatched filter.**
[Caban et al. (2026)](/sources/caban-2026.md), §4.2, Fig. 8, filter a
$384^3$ HIT DNS at $Re_\lambda=100$ with a Gaussian of width $\Delta=2h$ to
a 64-node grid and measure the error of the SGS stress reconstructed by
approximate deconvolution when the filter assumed in the deconvolution
differs from the true one (the true numerical filter being mimicked by the
filters induced by their compact interpolation and derivative schemes).
The error is largest at high wavenumbers and of the order of the filtered
product itself for every assumed filter, the exact numerical one included;
at low wavenumbers, compact filters of second and fourth order give errors
about two orders of magnitude below the Layton–Lewandowski model and the
second-order explicit filter. With the second-order explicit filter more
deconvolution terms increase the total error; with the compact filters it
falls up to 4–6 terms and then stays constant, and the authors advise
keeping the number of terms small. Their a posteriori tests are on the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md); see
[scale-similarity models](/methods/scale-similarity-model.md).

**Explicitly filtered LES and deconvolution closures, a priori on compressible decay.**
[Valencia et al. (2026)](/sources/valencia-2026.md) compare four
deconvolution closures — the approximate deconvolution model (van Cittert
series of order 5), a discrete direct deconvolution on a Taylor-truncated
inverse Gaussian stencil (order 4), a dynamic iterative deconvolution with
least-squares stencil weights, and an exact spectral inversion of the
Gaussian transfer function $\hat G(k)=\exp(-k^2\Delta^2/24)$ capped at
$1/0.01$ — with the dynamic Smagorinsky and dynamic mixed models, all
cast in explicitly filtered LES (details on
[scale-similarity models](/methods/scale-similarity-model.md) and, for
explicit filtering and the filter-to-grid ratio $\Delta/h$, on
[large-eddy simulation](/definitions/large-eddy-simulation.md)). Their
protocol is "stringent": the $512^3$ DNS is first top-hat filtered at the
coarse spacing $h$ (to emulate the implicit filter of a centred
finite-volume scheme) and downsampled, then explicitly filtered, and the
target is the **total** unresolved stress, grid-truncation part included,
which no deconvolution can recover (§II C, §V A). Top-hat filtering and
downsampling keep 99.7%, 98.7%, 95%, 83.6% and 59.1% of the kinetic energy
at $h=2$, 4, 8, 16 and 32 DNS spacings (Table III). At a common
$\Delta=16$ DNS spacings the three retained cases miss 15–20% of the
energy; the sub-filter share of it is about 92% at $\Delta/h=4$, 72% at
$\Delta/h=2$ and 3.5% at $\Delta/h=1$ (Table IV). For $\tau_{xx}$ and
$\tau_{xy}$ the deconvolution models reach correlation 0.974–0.985 and
relative error 0.19–0.26 at $\Delta/h=2$, and correlation above 0.994 and
error 0.05–0.10 at $\Delta/h=4$; the spectral inversion is best (0.9989,
0.9992; 0.063, 0.046 at $\Delta/h=4$) and the iterative one least accurate.
The dynamic Smagorinsky model gives correlation 0.12–0.27 and relative
error 1.02–1.96, the dynamic mixed model 0.91 and 0.44–0.49 (Tables
VI–VII). The approximate deconvolution model fails at $\Delta/h=1$
(correlation below 0.15, error above 0.98, §V B 1), and explicit filtering
does not move the grid cutoff $k_c\approx\pi/h$: at $\Delta/h=1$ the
spectrum "essentially overlaps" the [implicit-LES](/definitions/implicit-les.md)
one (Fig. 3). The authors state that classical a priori tests on the DNS
grid "tend to overestimate model accuracy" (§I), and that their study is a
priori and HIT-only, with a posteriori stability left to future work (§VI);
see [a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md).

**A shock-capturing scheme on compressible decay without a model.**
[Liang & Fu (2024)](/sources/liang-2024.md), §4.12, run the same family of
decaying compressible case ($M_t=0.6$, initial $Re_\lambda=100$) on $64^3$
with no SGS model described and compare, against a $256^3$ filtered DNS, the mean
square velocity, density and temperature fluctuations, dilatation and
enstrophy. Their hybrid scheme, which takes a non-dissipative
skew-symmetric split flux wherever an eight-point
[shock sensor](/definitions/shock-sensor.md) flags smooth cells and an
eight-point TENO reconstruction elsewhere, predicts these "significantly
better" than WENO-CU6, TENO6 and TENO8 (Fig. 21; the scheme is on
[WENO schemes](/methods/weno-scheme.md) and
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
The final time and $k_0$ are not printed; the authors delegate them to the
cited case of Johnsen et al. The authors call the test one of "modeling
accuracy for broadband turbulence motions" with no model term, the setting
of [implicit LES](/definitions/implicit-les.md); their other turbulence
tests are the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $64^3$ and
$128^3$.

[Deng et al. (2022)](/sources/deng-2022.md), §4.15, run the same case
(initial $M_t=0.6$, Taylor-scale Reynolds number 100, $k_0=4$, DNS of
Johnsen et al. on $256^3$) as the one turbulence test of finite-volume
BVD schemes with an **adjustable-dissipation** stage: where both faces of
a cell keep the polynomial reconstruction, the two face values are
blended with a parameter $\lambda_{\mathrm{AD}}$ (page-local; not the
Taylor microscale), $\lambda_{\mathrm{AD}}=1$ giving the upwind-biased
scheme of order $n+1$ and $\lambda_{\mathrm{AD}}=0.5$ equal face values,
hence no upwind term in the Riemann flux and the non-dissipative central
scheme of order $n+2$ ($n$ the polynomial degree of the reconstruction).
With no subgrid model, $\lambda_{\mathrm{AD}}$ supplies the dissipation
of the implicit LES (see [implicit LES](/definitions/implicit-les.md)
and [numerical dissipation](/properties/numerical-dissipation.md)):

- on $64^3$ with $\lambda_{\mathrm{AD}}=0.75$ every scheme (the 6th-, 8th-
  and 10th-order variants, named by their central order $n+2$, i.e.
  $n=4$, 6, 8) gives a velocity spectrum at $t/\tau=4$ closer to the DNS than the
  ninth-order WENO-M implicit LES, and the 10th-order variant is close to
  the DNS (Fig. 23);
- lowering $\lambda_{\mathrm{AD}}$ improves the $64^3$ spectrum
  progressively: the 6th-order scheme ($n=4$) at $\lambda_{\mathrm{AD}}=0.65$ is
  comparable to the original BVD scheme with $n=6$, i.e. without the
  adjustable stage ($\lambda_{\mathrm{AD}}=1$, upwind-biased of order 7)
  (Fig. 24);
- on $128^3$, $\lambda_{\mathrm{AD}}=0.75$ and 0.5 both converge to the DNS
  spectrum (Fig. 25).

The comparison is of one quantity at one time; the fully central setting
$\lambda_{\mathrm{AD}}=0.5$ is run only on the finer grid. The authors
state that adjustable dissipation "is believed to work" in place of an
explicit subgrid model (Remark 2). The scheme's shock tests are on
[WENO schemes](/methods/weno-scheme.md).

[Bilocq et al. (2025)](/sources/bilocq-2025.md), §4.1, run the same
case of Johnsen et al. (uniform $\rho$, $p$, $T$, solenoidal velocity with
$E(k)\sim k^4\exp[-2(k/k_0)^2]$, $k_0=4/L$ on $[-\pi L,\pi L]^3$,
$M_{t,0}=0.6$, $Re_{\lambda,0}=100$, viscosity $\propto T^{3/4}$,
$Pr=0.71$, RK(4,4) at $\Delta t=5\times10^{-3}\tau_0$, to $t=4\tau_0$) as
the first test of stabilized Gauss–Legendre DGSEM, against the DNS of
Hillewaert et al. at $1920^3$ degrees of freedom. On the main mesh,
$11^3$ elements at $N=5$ ($66^3$ degrees of freedom), vanilla DG with a
local Lax–Friedrichs flux is stable, but it diverges on every coarser
mesh tried ($4^3$ and $8^3$ at $N=3$, $3^3$ and $6^3$ at $N=4$, $3^3$ and
$5^3$ at $N=5$), where artificial viscosity (DG-AV), full entropy
stability on Gauss–Legendre or Gauss–Lobatto nodes (ESDG-GL, ESDG-GLL) and
the selective entropy-stable DG-ES all run (Table 1); the authors infer
that it "appears sufficient to satisfy the second law of thermodynamics
only in the troubled cells" (see
[entropy conservation](/properties/entropy-conservation.md)). The full
entropy-stable schemes underestimate the peak of the mean-square
vorticity, ESDG-GL through the projection of the entropy variables, while
DG-AV and DG-ES flag at most about 10% of the elements and behave like
vanilla DG; vanilla DG has the smallest error of the kinetic-energy budget
(solenoidal and dilatational dissipation, pressure dilatation, boundary
flux) and ESDG-GL the largest (Figs. 1–2). Costs relative to vanilla DG are
1.07–1.08 (DG-AV), 1.25–1.27 (DG-ES), 2.19–2.27 (ESDG-GL) and 1.24–1.53
(ESDG-GLL) for $N=3$ to 5 (Table 3), and the schemes with an entropy
projection have the smallest stable time steps (Table 2). DG-AV is
strongly sensitive to the sensor calibration: the original Persson–Peraire
calibration flags nearly every cell and over-dissipates, and a
dilatation–vorticity shock sensor damps the dilatation and is less stable,
while DG-ES is much less sensitive and, in the worst case, matches ESDG-GL
(Figs. 3–5, Table 4; see [shock sensors](/definitions/shock-sensor.md)).

**A machine-learned implicit LES on compressible decay.**
[Bezgin et al. (2025)](/sources/bezgin-2025.md) train ML-ILES, a
finite-volume implicit LES whose HLLC + TENO6-A scheme keeps its four
Harten-type candidate polynomials but replaces the TENO weighting by three
small networks (density, velocity, pressure; three hidden layers of 20
units, 3132 parameters in all) that output the convex weights (see
[implicit LES](/definitions/implicit-les.md) and
[model-consistent training](/methods/model-consistent-training.md)). The
data are $512^3$ TENO6-A runs of forced compressible turbulence at
$M_t=0.4$, 0.6 and 0.8 ($Re_\lambda\approx200$, solenoidal forcing at
$k=2$ with uniform cooling, steady after $t/\tau\approx25$), whose snapshots
start decaying runs to $t/\tau_\lambda\approx10$, box-filtered by 16 in
space and time to $32^3$ (§4.1). The networks are trained end to end
through the differentiable JAX-Fluids solver, unrolled over $N_T=1$, 2 or
5 coarse steps. Eddy shocklets appear at $M_t=0.8$ as thin regions of
negative dilatation; at $M_t=0.4$ the flow is essentially shock free
(Fig. 5). In the short unrolled test on unseen trajectories, which the
authors call a priori, each model is best at its own training horizon
(Table 2); in the full a posteriori decay at $32^3$ the $N_T=1$ model has
the lowest total spectral error at every Mach number and the $N_T=5$ model
the highest (Table 3, mean absolute error):

| Model | $M_t=0.4$ | $M_t=0.6$ | $M_t=0.8$ |
|---|---|---|---|
| ML-ILES, $N_T=1$ | 0.8849 | 0.7923 | 0.6178 |
| ML-ILES, $N_T=5$ | 1.480 | 1.562 | 1.428 |
| TENO6-A | 1.110 | 1.153 | 1.173 |
| ALDM | 1.099 | 1.252 | 1.428 |

The authors conclude that "the cell-wise error computed in the previous
section does not necessarily correspond to good spectral properties during
the decay" (§5.2; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
ML-ILES follows the filtered-DNS kinetic-energy spectrum up to the cutoff
with less high-wavenumber dissipation than TENO6-A, gives the best density
spectra at the higher Mach numbers, where ALDM degrades, and generalizes to
an unseen $64^3$ grid (Figs. 7–9). The learned weights differ by field:
the pressure reconstruction discards the downwind polynomial, the density
keeps a weight of about 0.08 for it, and the velocity weights resemble the
spectrally optimized linear weights of TENO6-A (Figs. 10–12). Per cell and
step on an RTX A6000 the cost is 327.20 ns (ALDM), 452.70 ns (TENO6-A) and
1238.14 to 2004.14 ns (ML-ILES with 5 to 20 units per layer) (Table 5).

**Pressure terms of entropy-conservative fluxes.**
[Aiello et al. (2026)](/sources/aiello-2026.md), §4 and §4.2, cite the
authors' companion paper and Gassner et al. for the finding that the
pressure discretization of the entropy-conservative flux of Gouasmi et al.
(and of Chandrashekar's, to which it reduces for a calorically perfect gas)
spoils the kinetic-energy balance in inviscid HIT; their own test is a
compressible channel (see
[entropy conservation](/properties/entropy-conservation.md)).

**Inviscid compressible decay as a stability test of split-form fluxes.**
[Kuya et al. (2018)](/sources/kuya-2018.md), §5.3, run the inviscid
decaying case at $32^3$ with twelve combinations of second-order central
fluxes for mass, momentum, kinetic energy, internal energy and pressure
diffusion (Table 3), with no dissipation of any kind, the large-eddy
turnover time being $T_E=2\sqrt3/(k_0M_{t0})$ (printed with $k_0$ for the
peak wavenumber, which the paper names $\kappa_0$). At $M_{t0}=0.07$ every
scheme with a divergence-form mass flux and quadratic-split momentum flux
blows up by $t/T_E=40$, while the four with a quadratic-split mass flux and
cubic-split (Kennedy–Gruber-type) momentum flux run to at least
$t/T_E=180$; of these, only the scheme whose energy fluxes are consistent
with the discrete mass and momentum equations (their QC$_C$, the KEEP
scheme) keeps the total entropy constant and the RMS density and
temperature fluctuations bounded, the others showing entropy reduction
and growing thermodynamic fluctuations (Figs. 8–9). At $M_{t0}=0.3$ only
QC$_C$ gives a stable, entropy-conserving solution (Figs. 10–11). At
CFL about 1 and $M_{t0}=0.07$ QC$_C$ keeps the kinetic energy constant
and its normalized RMS density and temperature fluctuations converge to
about 0.32, which the authors call "fairly good agreement" with about 0.35
in Honein & Moin's de-aliased spectral simulation (App. C, Fig. 16); the
same appendix judges CFL about 1 not time-converged and finds that the
third-order strong-stability-preserving Runge–Kutta scheme produces
entropy. The flux construction is on
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
and [entropy conservation](/properties/entropy-conservation.md); the
companion test is the inviscid
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).

**A gene-expression-programming SGS model.**
[Li et al. (2021)](/sources/li-2021.md) train an explicit algebraic model
of the deviatoric SGS stress, a tensor-basis expansion in Pope's tensors
$T^{(1)}$–$T^{(4)}$ with constant coefficients found by gene-expression
programming (on
[symbolic-regression closures](/methods/symbolic-regression-closure.md)),
on the top-hat-filtered $1024^3$ forced DNS at $Re_\lambda\approx260$
coarse-grained to $64^3$ samples, $8\times64^3$ points in all, 70% for
training (§III A). A posteriori at $128^3$ (§III C, Figs. 2–8), against
the filtered DNS, the GEP model and the neural-network model of Xie et
al. nearly overlap the filtered-DNS spectrum, while the
[dynamic Smagorinsky](/methods/dynamic-procedure.md) and dynamic mixed
models are damped near the cutoff and "energy-rich" at lower
wavenumbers, and the run without a model deviates strongly near the
cutoff. At small separations the dynamic models underpredict the
longitudinal structure functions of orders 2, 4 and 6, more for higher
orders, and give too narrow PDFs of the velocity increments and of the
stress components; the dynamic Smagorinsky flux $\Pi$ is strictly
positive, whereas GEP and the network reproduce both forward transfer and
[backscatter](/definitions/energy-backscatter.md) (Fig. 6). The
generalization tests at $64^3$, $32^3$ and at $Re_\lambda=180$ and 250
compare energy spectra only (§III E, Figs. 11–12), and the authors limit
the model's validation to isotropic turbulence (§IV). The cost per
iteration of GEP is slightly above dynamic Smagorinsky and far below the
network (16 cores, Fig. 13; no timings printed).

**A constant-coefficient spatial gradient model.**
[Wang et al. (2022)](/sources/wang-2022-j.md), §III–IV, Tables II–III,
Figs. 2–6, test their SGM-7-19, a multi-point gradient model with
Taylor-derived constant coefficients (see
[gradient model](/methods/gradient-model.md)), on forced HIT at
$Re_\lambda=259$ ($1024^3$ DNS, Gaussian filter $\Delta=16$ DNS
spacings). A priori the correlation coefficients for $(\tau_{11},\tau_{12})$
are 0.973 and 0.973 against 0.945 and 0.946 for the plain gradient model
and 0.985 and 0.981 for the neural-network version it derives from, with
relative errors 0.241 and 0.237 (Table II). A posteriori on $128^3$ with
backscatter clipped, the dynamic Smagorinsky and dynamic mixed models
over-predict the spectrum at low wavenumbers and under-predict it at high
wavenumbers, which the authors ascribe to the strong dissipation of their
Smagorinsky parts, while SGM-7-19 is closest to filtered DNS (Fig. 2);
implicit LES with a hyperviscosity needs that hyperviscosity "artificially
adjusted", "Otherwise, the ILES always diverges" (§IV). SGM-7-19 also
matches the PDFs of strain rate and of velocity increments at
$r/\Delta=1$; at large separations all models coincide, which the authors
tie to the large-scale forcing (Figs. 3–5). The SGS modelling cost per
step on 64 cores is 0.272 s (dynamic Smagorinsky), 0.567 s (dynamic mixed)
and 0.399 s (SGM-7-19) (Table V).

**Density-unweighted and dense-gas compressible LES.** Two papers of one
group test closures on decaying compressible HIT at $M_t\approx0.4$ and
0.8 with a Gaussian filter of 16 DNS spacings and an LES grid at half the
filter width, against filtered DNS:

- [Zhang et al. (2022b)](/sources/zhang-2022-f.md), §IV, filter the
  equations **without density weighting**, which brings in an SGS mass
  flux, an SGS density–temperature correlation and SGS turbulent and
  viscous diffusion besides the SGS stress and heat flux, and close all of
  them with the gradient model, approximate deconvolution (van Cittert,
  four terms), dynamic Smagorinsky, dynamic mixed and the dynamic iterative
  approximate deconvolution (DIAD) model (see
  [large-eddy simulation](/definitions/large-eddy-simulation.md) and
  [scale-similarity models](/methods/scale-similarity-model.md)). A priori,
  the gradient model correlates above 0.9 and the two deconvolution models
  above 0.98 for $\tau_{11}$, $\tau_{12}$ and the heat flux, DIAD best with
  relative errors below 0.2 after two iterations (Figs. 1–3). Of the rms
  divergence terms at $\Delta=16$ spacings, the heat-flux, turbulent
  diffusion and stress terms dominate (51.29, 24.60, 10.32 at
  $M_t=0.40$), and the density–temperature term is small but grows with
  $M_t$ (0.0060 to 0.11; Table II). A posteriori, to $t/\tau=2.08$, DIAD is
  closest in kinetic-energy decay, spectra and the PDFs of the SGS terms,
  strain and vorticity; dynamic Smagorinsky and dynamic mixed are
  over-dissipative, approximate deconvolution under-dissipative, the
  gradient model close to DIAD (Figs. 5–23). The left (backscatter) tail of
  the PDF of $\Pi$ lengthens as $M_t$ rises, which the authors read as
  compressibility enhancing transfer from small to large scales (Fig. 9;
  see [energy backscatter](/definitions/energy-backscatter.md)).
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) run the same comparison
  for the **dense gas** PP11 near its critical point, whose Favre-filtered
  equations carry extra SGS terms from the nonlinear equation of state (SGS
  pressure, pressure work, internal-energy flux, density–temperature
  correlation). DIAD reconstructs them a priori with correlation above
  0.98 and relative error below 0.2, except the internal-energy flux at
  $M_t=0.4$ (above 0.96, below 0.3); a posteriori, on $64^3$, DIAD and a
  variant that closes only the stress and turbulent diffusion both beat the
  over-dissipative dynamic Smagorinsky model, and the thermodynamic SGS
  terms have little effect on the velocity and thermodynamic spectra in
  these cases (§IV). The cost per step on 32 cores is 0.241–0.245 s
  (dynamic Smagorinsky), 0.274–0.282 s (reduced DIAD) and 0.334–0.339 s
  (full DIAD).

Both papers rank DIAD first; [Valencia et al. (2026)](/sources/valencia-2026.md)
above rank their dynamic iterative deconvolution least accurate of four
deconvolution closures a priori. The comparisons differ in the set of
models (no exact spectral inversion or discrete direct deconvolution in
Zhang et al.) and in the protocol (filtered DNS on the DNS grid against
Valencia et al.'s top-hat-filtered and downsampled data with the
grid-truncation stress in the target), so the rankings stand side by
side.

**Generating the subgrid velocity.**
[Hausmann et al. (2022)](/sources/hausmann-2022.md), §III B 1, §IV A,
Figs. 2–3, 8–11, add a stochastic SGS velocity, built from a truncated
Fourier series on sub-domains coarser than the LES grid and driven toward
a Yoshizawa estimate of $k_{\mathrm{sgs}}$ (see
[subgrid velocity enrichment](/methods/subgrid-velocity-enrichment.md)), to
a $32^3$ Smagorinsky LES of forced HIT at $Re_\lambda=75$. The enriched
field recovers the DNS energy spectrum beyond the LES cutoff and widens the
PDFs of velocity gradients and of $Q$ toward the DNS, while their skewness
is under-predicted and the elongated structures of the DNS are missing.
The results are insensitive to the number of sub-domains ($8^3$ to
$32^3$), of modes ($N_m\ge100$, page-local) and to the coefficient of the
wavenumber-dependent turbulent viscosity of the model varied by a factor
16, while the target energy level sets the width of the
tails. The cost per reference time is $32\times10^3$ s (LES),
$69\times10^3$ s (LES with enrichment) and $340\times10^6$ s (DNS)
(Table III).

**A DNS-database closure on very coarse meshes.**
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.3, Figs. 11–12,
compare [pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md),
whose subgrid stress comes from a database of DNS on representative volume
elements, with a dynamic $k$-equation LES (Kim & Menon) on decaying HIT
with a von Kármán–Pao spectrum at Reynolds numbers on the rms fluctuation
of about 60 and 500, against a $256^3$ DNS, on $32^3$ down to $4^3$ cells.
P-DNS gives a reasonable kinetic-energy decay down to $4^3$, while the LES
is accurate at $32^3$ and departs as the mesh coarsens. The constants
$C_1=6.8$ and $C_2=4.0$ of the method's memory model are calibrated on this
case in an earlier paper (§2.9).

**A decaying box as the inflow of a reacting shock.**
[Iwata et al. (2023)](/sources/iwata-2023.md), §II C, decay a compressible
isotropic field in a periodic cube of the lateral size of their detonation
domain, on the same 4 µm grid, until the skewness of the velocity
derivative lies between $-0.6$ and $-0.4$, which they call "a reasonable
range for turbulence observed in actual systems", and feed it in at
$Re_\lambda=240$ and turbulent Mach number 0.30 around the detonation speed.
The resolution criterion $k_{\max}\eta\ge1.5$ ($k_{\max}$ page-local, the
largest resolved wavenumber) holds with 2.31 and 4.25 in the two mixtures
(Table I). What the turbulence does to the detonation is on
[shock-generated turbulence](/results/shock-generated-turbulence.md).

**Isotropic turbulence convected through a normal shock.** The canonical
shock–turbulence interaction feeds a box of decaying isotropic turbulence
through a normal shock (see
[shock-generated turbulence](/results/shock-generated-turbulence.md) and
[linear interaction analysis](/methods/linear-interaction-analysis.md)).
[Cuadra et al. (2025)](/sources/cuadra-2025.md), §I and §III B, Table I,
characterize the incoming turbulence by $M_t$, $Re_\lambda$ and the
spectrum shape, and compile the upstream states of the DNS studies of
the interaction: pre-shock Mach numbers 1.1 to 6, $M_t$ from 0.02 to
0.691 and $Re_\lambda$ from 9 to 74, against the $Re_\lambda>100$ they
state fully developed turbulence needs. [Bilocq et al. (2025)](/sources/bilocq-2025.md),
§4.4, generate their inflow for the case of Larsson & Lele from a
precursor decaying run (Ristorcelli & Blaisdell initialization, Gaussian
spectrum peaked at $k=6$), developed until the velocity-derivative
skewness is about $-0.5$ and the flatness about 4.0, and convect it with
Taylor's hypothesis at $M_t=0.22$ and $Re_\lambda=40$ ahead of a Mach-1.28
shock.

**A GPU DNS solver on forced and decaying boxes.**
[Monteiro et al. (2026)](/sources/monteiro-2026.md), §4.6 and §5, use the
periodic box twice in RHEA-X, a second-order kinetic-energy-preserving
finite-difference compressible solver. Forced turbulence at low Mach
number on $320^3$ points, with the solenoidal linear forcing of Watanabe
et al. targeting $Re_\lambda\approx90$, carries $10^6$ passive tracers
whose Voronoi-cell volumes follow the Gamma distribution of randomly
placed tracers, showing no spurious numerical clustering (Fig. 9).
Decaying turbulence, ideal-gas and supercritical CO2 at twice the critical
pressure at the pseudo-boiling temperature, on $32^3$ to $1000^3$ points,
is the benchmark of their GPU performance study, timed over 100 steps (see
[direct numerical simulation](/definitions/direct-numerical-simulation.md)).

**Not this case: isotropic turbulence ahead of a flame.**
[Chambers et al. (2022)](/sources/chambers-2022.md) generate nominally
isotropic turbulence in a shock tube by passing a leading shock through a
perforated plate, ahead of an accelerating flame, and
[Coulon et al. (2023)](/sources/coulon-2023.md) inject synthetic
isotropic turbulence ($u'=2.5$ m/s, integral scale 2.1 mm) at the inlet
of a slot-burner flame DNS; neither runs a periodic box, and both are
recorded on their Source pages (see also
[shock-generated turbulence](/results/shock-generated-turbulence.md)).
The review of [Salehi et al. (2024)](/sources/salehi-2024.md), §3.2, Fig. 33,
cites the DNS of Grout of a freely propagating premixed flame in a box of
isotropic turbulence, with a two-step mechanism, as the database of an a
priori test of [conditional source-term estimation](/methods/conditional-source-term-estimation.md)
in a RANS context; the review prints no turbulence statistics of the box.

**The first simulations of turbulence.**
[Kim & Leonard (2024)](/sources/kim-2024-b.md) date numerical turbulence
simulation from this case: Orszag & Patterson (1971, 1972) computed
decaying HIT with a pseudospectral method on $16^3$ and $32^3$ meshes at
initial $Re_\lambda=35$ on a CDC 6600 of 3 megaflops peak, 30 s per time
step at $32^3$, 200 steps in 1.5 h, and compared the velocity-derivative
skewness with direct-interaction theory and experiments (§2.2, Fig. 2a).
Aliasing was removed by spherical truncation with six shifted transforms
(Patterson & Orszag 1971), later more cheaply by the 2/3 rule with phase
shifts (Rogallo 1981; §2.2, §3.3). In an LES of isotropic turbulence and
irrotational plane strain, Kwak et al. (1975) obtained the Smagorinsky constant 0.206 by matching the decay
of Comte-Bellot & Corrsin (1971); the authors set it beside Lilly's 0.17
from consistency with the $k^{-5/3}$ law and Deardorff's 0.10 in the
channel (§2.5, §3.1; see [Smagorinsky model](/methods/smagorinsky-model.md)).
Clark et al. (1979) made the first a priori test of SGS models on a DNS
database of this flow (§3.1; see
[a priori and a posteriori testing](/definitions/a-priori-and-a-posteriori-testing.md)).
Forcing was introduced by Siggia & Patterson (1978) and Siggia (1981):
in the authors' words it models the large scales and computes the small
ones, "the opposite of the LES approach", and gives a statistically
steady state for small-scale statistics, intermittency and vortex tubes
(§4.3). They close with the $4096^3$ run of Kaneda et al. (2003), at 40%
of peak on the Earth Simulator, and the $8192^3$ run of Yeung et al.
(2015), at $Re_\lambda=1200$–1300, against a peak-speed growth of about
$10^{12}$ from the CDC 6600 to Frontier (§5); the later record runs are
those of [Yeung et al. (2025)](/sources/yeung-2025.md) above.

**One-dimensional turbulence on the case.** In the review of
[Chen et al. (2024b)](/sources/chen-2024-c.md) decaying HIT is one of the
first targets of the stochastic
[one-dimensional turbulence](/methods/one-dimensional-turbulence.md) model:
Kerstein's 1999 eddy-energy closure is printed for "decaying homogeneous
turbulence and shear flow" (Table 1, Eq. 4), McDermott's 2005 closure for
free shear flow and decaying isotropic turbulence (Eq. 8), and the
finite-volume LES-ODT coupling of McDermott is reported on decaying
isotropic turbulence, the finite-difference coupling of Echekki and
coworkers on autoignition in isotropic turbulence (§2.4.1); particle-laden
forced HIT is named among the applications. The review reproduces no HIT
result.

**Closure constants.**
[Duraisamy et al. (2019)](/sources/duraisamy-2019.md) cite the decay rates of grid
turbulence (Comte-Bellot & Corrsin 1966) as a constraint on the coefficients of RANS
closures (the coefficient layer of their taxonomy of
[model-form uncertainty](/definitions/model-form-uncertainty.md)).
[Agrawal et al. (2022)](/sources/agrawal-2022.md), §II.A, cite Lilly's derivation of
$C_s\approx0.17$ for isotropic turbulence with an inertial-range cutoff, as
do [Kim & Leonard (2024)](/sources/kim-2024-b.md), §2.5 (above);
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), §6.5,
quote Lilly's analytical value $C_s=\pi^{-1}(3C_K/2)^{-3/4}=0.18$ with
Kolmogorov constant $C_K=1.4$. The two printed values of Lilly's constant
are recorded side by side; neither source states the Kolmogorov constant
behind 0.17. The Chollet–Lesieur spectral eddy viscosity,
whose plateau 0.267 holds for an infinite Kolmogorov spectrum, is the
spectral reference used with HIT in both
[Flad & Gassner (2017)](/sources/flad-2017.md), App. C, and
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md), Eq. (55)
(see [spectral eddy viscosity](/methods/spectral-eddy-viscosity.md)).
[Basile et al. (2023)](/sources/basile-2023.md), §2.2, state that the
DES constant $C_{DES}=0.65$ is calibrated on decaying homogeneous turbulence
(see [detached-eddy simulation](/methods/detached-eddy-simulation.md)), the
value with which [Carlsson et al. (2023)](/sources/carlsson-2023.md)
reproduce the Comte-Bellot–Corrsin decay once the scheme's dissipation is
low enough; [Möller et al. (2024)](/sources/moller-2024.md), §II.B.1, state
that they verified the same value in their TRACE implementation of
shear-stress-transport DDES on decaying isotropic turbulence (results not
shown). [Pereira et al. (2021)](/sources/pereira-2021.md), §III, Fig. 4,
cite their companion paper, in which explicit filtering of forced HIT DNS of
Silva et al. at $Re_\lambda=140$ and 300 supports setting the dissipation
ratio of [partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
to $f_\varepsilon=1$ for $f_k\ge0.20$.

## Qualifications

- [Domaradzki (2024)](/sources/domaradzki-2024.md) uses the sign
  convention in which the SGS dissipation $\tau_{ij}\bar S_{ij}$ is
  negative for forward transfer, the opposite of the registry's $\Pi$; the
  description above is in words. The Table 1 Taylor microscales depart by
  up to about 6% from the printed definition
  $\lambda=(15u'^2\nu/\varepsilon)^{1/2}$ evaluated with the tabulated
  $u'$ and $\varepsilon$, while the tabulated $Re_\lambda$ are consistent
  with the tabulated $\lambda$ *(compiler check, not in the sources)*; the
  Table 2 caption gives the length unit as "[L] = 0.1 cm", whereas the
  text's conversion makes it 10 cm.
- [Wang et al. (2023c)](/sources/wang-2023-c.md) calibrate on the energy
  spectrum, a second-order statistic, and recalibrate separately for a
  temporal mixing layer ($C_{\mathrm f}\approx0.01$); their generalization tests stay
  within HIT.
- [Duan & Wang (2024)](/sources/duan-2024.md) set the model eddy viscosity
  constant in each element and the interface fluxes of the SGS stress to
  zero (§3, Eqs. 26–27); their filter-width ranking is obtained with these
  choices, and they do not state the model coefficients used.

- Forcing differs between sources (linear forcing at the nodes; linear
  momentum forcing; Kolmogorov forcing at a single wavenumber). [Beck & Kurz (2023)](/sources/beck-2023.md)
  note that their nodal forcing injects energy at all wavenumbers present
  and causes a slight departure of the spectrum from $k^{-5/3}$.
- [Flad & Gassner (2017)](/sources/flad-2017.md), §1, print the large-eddy
  turnover time as "$T=\bar v(t_{\mathrm{start}})/L_{\mathrm{int}}\approx1.3$",
  a velocity over a length; a time is length over velocity.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) prints $Re_\lambda=320$
  in the Fig. 6 and Fig. 7 captions and in §6.4 for the $1024^3$ case, for
  which Table 1 and §5.1 give 324.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) name the 3D
  case of App. G.2 both "forced" (title) and "decaying" (first sentence)
  while applying a body force, and print its amplitude as 5 while Eq. (31)
  of the 2D case has amplitude 1 and App. G.2 calls it "the same body force".
- [Cao et al. (2022)](/sources/cao-2022.md) were read in the arXiv v1
  preprint. Their Eq. (11) prints the energy balance as
  $d\langle K\rangle/dt=\varepsilon+\langle p\,\nabla\cdot\boldsymbol u\rangle$
  with $\varepsilon=\varepsilon_s+\varepsilon_d$, a sum of non-negative
  terms, while the text describes a decay; a decay needs $-\varepsilon$
  *(compiler check, not in the sources)*. They print the maximum resolved
  wavenumber as $\sqrt2k_0N_x/3$ with $k_0=8$. With $N_x=512$,
  $\Delta=2\pi/512$ and their $\Delta/\eta_0=0.819$, $\sqrt2N_x/3$ gives
  $k_{\max}\eta_0=3.617$, close to their Table 8 value 3.613, while the
  printed factor $k_0=8$ would give 28.9 *(compiler check, not in the
  sources)*. Their Mach number of the
  supersonic runs is the turbulent one; §1 calls the range "hypersonic",
  the abstract and §3.4 "supersonic".
- [Seta & Federrath (2022)](/sources/seta-2022.md) are a non-isothermal,
  magnetized, driven box: the isotropy of the large-scale forcing is the
  only sense in which the case is "isotropic". Read in arXiv v2.
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) (read in arXiv
  v3) multiply the squared filter width directly by their Smagorinsky
  coefficient, so that it corresponds to the registry's $C_s^2$, and print neither its value nor
  the constant of the static fractional model. Their filter size is the
  filter width over twice the DNS grid spacing, as printed. They label the
  subfilter energy $\tfrac12(\overline{u_iu_i}-\bar u_i\bar u_i)$ "resolved" and
  $\tfrac12\bar u_i\bar u_i$ "filtered" (Eq. 24); the labels are swapped
  relative to the formulas.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) give the resolution as
  $N^3$ nodes ($N_x^3$ here) and measure time from the first experimental
  station; their tests are hybrid RANS/LES in LES mode, not wall-resolved
  closure tests.
- [Gan et al. (2022)](/sources/gan-2022.md) (read in arXiv v1) are
  periodic-box turbulence but anisotropic by construction (guide field
  $v_A=8$); their fractions exclude the injection range $\lvert\boldsymbol k\rvert\le2$
  and the $(k_\parallel=0,\omega=0)$ component.
- [Kurz et al. (2023)](/sources/kurz-2023.md) and
  [Beck & Kurz (2023)](/sources/beck-2023.md) both compare reinforcement-learned
  closures with the dynamic Smagorinsky model on forced HIT at
  $Re_\lambda\approx180$ but in different configurations (polynomial degrees,
  DOF, action noise). Kurz et al. find the RL model equal to the dynamic
  model except at 24 DOF, where it is "significantly better" (§4.2); Beck &
  Kurz find the RL models better than the dynamic model for $N=5$ and $N=8$,
  with the dynamic model close at 36 DOF and off at 24 DOF (§V A–B). Both
  report the dynamic model's weakness at 24 DOF and relate it to the test
  filter leaving the scale-similar range, so they agree where their
  configurations overlap.
- [Kang et al. (2023)](/sources/kang-2023.md), App. A, Table 14, obtain
  $Re_\lambda=122.9$, not 164, when reproducing the forced DNS of Langford &
  Moser with the negative-viscosity forcing that paper describes, and 164.7
  with the deterministic forcing of Machiels. They print the Leaky-ReLU
  activation as $\max[-0.02x,x]$ (§2.4): for $x<0$ this returns
  $-0.02x>0$, a non-monotone function, whereas $\max[0.02x,x]$ has slope
  0.02 for negative arguments *(compiler check, not in the sources)*; the
  paper does not say which form the code uses.
- [Reddy et al. (2026)](/sources/reddy-2026.md) (read in a 2021 preprint)
  label their Taylor–Green vortex runs "homogenous, isotropic turbulence"
  (abstract, §1, §9); the case is recorded on
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md), not here.
  [Simonis et al. (2022)](/sources/simonis-2022.md) likewise frame their
  Taylor–Green runs at $Re=800$ and 3000 as decaying homogeneous isotropic
  turbulence; they too are on the Taylor–Green page.
- [Deng et al. (2022)](/sources/deng-2022.md) label the Fig. 23 spectra
  "$t/\pi=4$" where the text and the Fig. 24 caption give $t/\tau=4$, and
  define the time unit as $\tau=\sigma/u_{\mathrm{rms},0}$ with $\sigma$
  where the quantity defined is $\sigma_0=2/k_0$ (§4.15). They write the
  initial Taylor-scale Reynolds number $Re_{\sigma,0}$.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) state that doubling
  the Mach number needs a tripled driving strength, while their Eq. (32),
  $M\propto E_{\mathrm{inj}}^{1/3}$, gives a factor 8 *(compiler check, not
  in the sources)*; realized Mach numbers "fall slightly short" of the
  intended doubling above Mach 1 (§5). They print the density-weighted Mach
  number with $c_s$ not squared next to an equivalent form with $c_s^2$
  (§4.1).
- [Li et al. (2024)](/sources/li-2024.md) define $Re_\lambda$ with the rms of
  the velocity magnitude divided by $\sqrt3$ (Eq. 3), equivalent to the
  one-component form, and do not say how the $Re_\lambda\approx160$ and 250
  data were generated.
- [Yeung et al. (2025)](/sources/yeung-2025.md) rest the short multi-resolution
  segments (about two Kolmogorov times at the top Reynolds number) on an
  equilibration time of about $2\tau_\eta$ and on one unplotted
  $27\tau_\eta$ segment at $Re_\lambda=1000$ (§2.2); all their runs are in
  single precision, and "rigorous testing is not readily available".
  Eq. (4.1) is printed with an unclosed parenthesis.
- The set-ups differ in what is forced: velocity modes below a wavenumber
  at fixed power ([Prakash et al. (2022)](/sources/prakash-2022.md),
  Eqs. 21–23), solenoidal or compressive acceleration fields
  ([Seta & Federrath (2022)](/sources/seta-2022.md)), Ornstein–Uhlenbeck
  acceleration fields, solenoidal ([Cernetic et al. (2024)](/sources/cernetic-2024.md))
  or mixed ([Beattie et al. (2025)](/sources/beattie-2025.md)), constant
  energy in the lowest shells ([Yeung et al. (2025)](/sources/yeung-2025.md),
  [Zhao et al. (2025)](/sources/zhao-2025.md) before release), or nothing
  (the decaying runs).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) print the
  experiment's final $Re_\lambda$ as 60.6, [Domaradzki (2024)](/sources/domaradzki-2024.md)
  as 60.7 (Table 2). They call the truncated error "nearly a quarter" of the
  flux-difference-splitting one; Table 6 gives $5.30/29.81=0.18$
  *(compiler check, not in the sources)*. Their comparison schemes were
  scored from published data limited to $k_c=31$, below the cutoffs 32 and
  32.5 their own Eq. (103) would give (§3.2.2).
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) tune the filter
  constant per flow (0.65 here, 0.25 on the Taylor–Green vortex, 0.5 in the
  channel; optimum range $0.2\le c\le0.7$, §III.D.2) and compare with one
  Smagorinsky constant per flow, without a dynamic procedure.
- [Wu & Lele (2026)](/sources/wu-2026.md) print no formula for their
  Smagorinsky and sigma baselines, only the coefficients 0.18 and 1.3, the
  latter "the smallest coefficient in the recommended range" (§5.1); every
  network is trained on HIT and channel data together.
- [Caban et al. (2026)](/sources/caban-2026.md) do not say whether their
  $Re_\lambda=100$ DNS is forced or decaying.
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) print the
  Reynolds number of the case as 3,400 in the abstract and
  $Re_M=34{,}000$ in §6.1, and the mean velocity of the experiment as
  "$U_0=10$ cm/s" (§6.1), where Domaradzki, Duan & Wang and Brillon &
  Nadarajah, above, give 10 m/s; the grid mesh 5.08 cm is common to all.
  They give the filter cut-off as about $3\pi/4$ in §6.1, and the
  parameter-to-cut-off mapping only for the values they use.
- [Iwata et al. (2023)](/sources/iwata-2023.md) do not print the
  definition of their turbulent Mach number.
- [Kuya et al. (2018)](/sources/kuya-2018.md) compare $M_{t0}=0.3$ with
  "$M_{t0}=0.05$ shown in Fig. 9(a)" (§5.3), but Fig. 9 is the
  $M_{t0}=0.07$ run (0.05 is the Mach number of their Taylor–Green
  vortex). Their appended corrigendum (J. Comput. Phys. 391:397) relabels
  the kinetic-energy axis of Figs. 8–17(a) as $\rho k/(\rho_0k_0)$ (density
  times specific kinetic energy, normalized by its initial value). Their
  runs are inviscid stability tests at infinite Reynolds number, not LES
  with a model, and the Honein & Moin comparison is made at a time step the
  paper itself judges not time-converged.
- [Li et al. (2021)](/sources/li-2021.md) state that they sample "every
  17th grid point" of the $1024^3$ field to get $16^3$ datasets of $64^3$
  points (§III A); $1024/64=16$, so the stride that gives $64^3$ points
  and $16^3$ offsets is 16 *(compiler check, not in the sources)*. Their
  LES solver adds a "high-order dissipative numerical method" at high
  wavenumbers (§II A) in all runs, and the paper does not separate its
  dissipation from that of the models.

- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) print the
  fluctuation velocity as "$\langle u_i^2/3\rangle$" (printed with angle brackets), which has the dimension of a
  velocity squared, and the Taylor microscale with
  $\langle(\partial u_i/\partial x_i)^2\rangle$ under their summation
  convention, the mean square divergence (§3.1, Eq. 30); "the theoretical
  5/3 power law" omits the sign.
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) take the calibrated
  $c_{\mathrm{diss}}=0.001$ unchanged to their channel and bump runs (see
  [turbulent channel flow](/benchmarks/turbulent-channel-flow.md)); its
  sensitivity there is not shown.
- The $512^3$ reference of [Bezgin et al. (2025)](/sources/bezgin-2025.md)
  has $k_{\max}\eta\approx2.3$, below the $k_{\max}\eta\ge\pi$ that the
  authors state "is required to fully resolve all scales"; they add that
  TENO6-A "acts as an ILES model" where not all scales are resolved
  (§4.1). Their printed Taylor microscale (Eq. 34) has the summed
  dilatation $\langle(\partial_iu_i)^2\rangle$ in the denominator, which
  with their dilatation rms gives $\tau_\lambda=\sqrt3/\theta_{\mathrm{rms}}$
  of about 3.9 at $M_t=0.4$ and 0.84 at 0.8 ($\theta$ the dilatation,
  page-local), while their Table 1 prints $\tau_\lambda\approx0.42$ at all
  three Mach numbers *(compiler check, not in the sources)*. They write
  "$Re_\tau\approx200$" for the Taylor-scale Reynolds number (§4.1, Fig.
  5), call the run to $t=10\tau_\lambda$ "approximately 10 eddy turn-over
  times", and define $p_{\mathrm{rms}}=\langle p'p'\rangle$ without a
  square root. Their "a priori" evaluation runs the models inside the
  solver for up to 20 steps.
- [Cuadra et al. (2025)](/sources/cuadra-2025.md) is a review; the upstream
  states of Table I are compiled from the cited DNS.

# Citations

- [Flad & Gassner (2017)](/sources/flad-2017.md) — §1, §3–5, Figs. 1–10, App. C.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §II.A, §VII.A–C, Figs. 3–6.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §IV A–B, §V, Figs. 6–14, App. A.
- [Vela-Martín (2022)](/sources/velamartin-2022.md) — §5.1–5.3, Table 1, Figs. 1–7.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — §5, App. B.2, App. G.1–G.2.
- [Duraisamy (2021)](/sources/duraisamy-2021.md) — §IV.B, Fig. 2 (cited result).
- [Duraisamy et al. (2019)](/sources/duraisamy-2019.md) — test-problem list (cited grid-turbulence calibration).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §6.2, §6.4–6.5, Eq. (55).
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.A, Tables 1–2, Figs. 1–3; §III.B.1, Eqs. (21)–(24), Fig. 4.
- [Cao et al. (2022)](/sources/cao-2022.md) — §1; §3.4, Eqs. (9)–(11), Table 8, Figs. 13–15.
- [Seta & Federrath (2022)](/sources/seta-2022.md) — §2, §2.4, §4.1–4.2, Table 1, Figs. 7–10.
- [Martin-Alvarez et al. (2022)](/sources/martinalvarez-2022.md) — cited turbulent-box references.
- [Basile et al. (2023)](/sources/basile-2023.md) — §2.2 (cited calibration of $C_{DES}$).
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §III, Fig. 4 (cited a priori filtering).
- [Seyedi & Zayernouri (2022)](/sources/seyedi-2022.md) — §III.1–III.2, Eq. (23), Table I, Figs. 3–7; §IV, Figs. 8–10.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.2, Fig. 3; §5.
- [Gan et al. (2022)](/sources/gan-2022.md) — §2; §3, Figs. 1–3.
- [Kurz et al. (2023)](/sources/kurz-2023.md) — §1, §3.4–3.5, Table 2; §4.1–4.5, Figs. 5–9.
- [Kang et al. (2023)](/sources/kang-2023.md) — §2, Table 1; §3.1–3.4, Tables 3–6, Figs. 4–24; App. A, Table 14.
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §4.4, §5 (contrast only: Orszag–Tang initial field).
- [Wang et al. (2023c)](/sources/wang-2023-c.md) — §II.A–B, Eq. (14); §III, Tables I–II, Figs. 2–9; App. A–C, Table V, Figs. 18–24.
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §2.4; §3.1–3.3, Tables 1–2, Figs. 1–10.
- [Duan & Wang (2024)](/sources/duan-2024.md) — §3, Eqs. (26)–(30); §5.2, Fig. 8.
- [Li et al. (2024)](/sources/li-2024.md) — §II A, Eqs. (1)–(4); §V A, Table I, Figs. 6–13.
- [Zhao et al. (2025)](/sources/zhao-2025.md) — §3.1, Eqs. (19)–(20), Tables 1–2, 5, Figs. 6–8; §4.
- [Yeung et al. (2025)](/sources/yeung-2025.md) — §1; §2.1–2.2, Table 1, Fig. 1; §3, Figs. 2–3; §4, Eqs. (4.1)–(4.2), Figs. 4–6; §5.
- [Cernetic et al. (2024)](/sources/cernetic-2024.md) — §4.1–4.2, Eqs. (18)–(32), Fig. 9; §5, Figs. 5–7; §6.
- [Beattie et al. (2025)](/sources/beattie-2025.md) — §4, Table 1; §5; §6; §9.1.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — §I (compressible isotropic turbulence as the closest flow to the supersonic Taylor–Green vortex).
- [Möller et al. (2024)](/sources/moller-2024.md) — §II.B.1 (calibration check of $C_{DES}$, not shown).
- [Reddy et al. (2026)](/sources/reddy-2026.md) — abstract, §1, §9 (Taylor–Green vortex labelled isotropic turbulence).
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.3, Eqs. (13)–(18) (theoretical $C_{DES}$); §3.1, Fig. 1; App. B, Fig. B1 (calibration on Comte-Bellot–Corrsin decay).
- [Brillon & Nadarajah (2026)](/sources/brillon-2026.md) — arXiv 2411.12108v1: §3.1.1, Table 4 (spectrum oversampling); §3.2, Eqs. (108)–(112), Table 6, Figs. 21–22 (Comte-Bellot–Corrsin decay).
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — arXiv 2512.03315v1: §III.A, Eq. (45), Table I, Figs. 3, 5–6; §III.D.2, §III.D.4, Figs. 17–18.
- [Caban et al. (2026)](/sources/caban-2026.md) — §4.2, Eqs. (38)–(39), Figs. 7–8 (a priori deconvolution error on HIT data).
- [Wu & Lele (2026)](/sources/wu-2026.md) — arXiv 2511.17475v2: §3.2.1; §4, Table 2; §5, Eq. (5.1), Tables 3–4, Figs. 5–12; §6.1, Figs. 13–14.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §4, §4.2 (cited kinetic-energy imbalance of the Gouasmi et al. pressure term in inviscid HIT).
- [Liang & Fu (2024)](/sources/liang-2024.md) — §4.12, Fig. 21 (no-model TENO-S and WENO/TENO schemes on decaying compressible isotropic turbulence, $64^3$, against filtered DNS).
- [Valencia et al. (2026)](/sources/valencia-2026.md) — §I; §II C, Eqs. (23)–(29); §IV, Eqs. (51)–(52), Figs. 1–2; §V A–C, Tables III–VII, Fig. 3 (a priori deconvolution closures under explicit filtering on compressible decaying HIT).
- [Kuya et al. (2018)](/sources/kuya-2018.md) — §5.1, Eq. (73) (set-up); §5.3, Table 3, Figs. 8–11; App. C, Figs. 16–17 (inviscid compressible decay as a stability and entropy test of split-form fluxes); appended corrigendum.
- [Deng et al. (2022)](/sources/deng-2022.md) — Remarks 1–2, p. 6 (adjustable dissipation); §4.15, Eq. (40), Figs. 23–25 (no-model BVD-AD schemes on decaying compressible isotropic turbulence, $64^3$ and $128^3$).
- [Simonis et al. (2022)](/sources/simonis-2022.md) — §1, §3 (Taylor–Green vortex framed as decaying isotropic turbulence).
- [Li et al. (2021)](/sources/li-2021.md) — §II A, Eq. (17); §III A (training data); §III C, Figs. 2–8 (a posteriori against filtered DNS); §III E, Figs. 11–12; §III F, Fig. 13; §IV.
- [Wang et al. (2022)](/sources/wang-2022-j.md) — §II, Eqs. 3–4; §III, Table II; §IV, Table III, Figs. 2–6; §VI, Table V.
- [Zhang et al. (2022b)](/sources/zhang-2022-f.md) — §II–III; §IV A–B, Tables I–III, Figs. 1–23.
- [Zhang et al. (2022d)](/sources/zhang-2022-h.md) — §II–III; §IV, Tables II–III, Figs. 1–20.
- [Hausmann et al. (2022)](/sources/hausmann-2022.md) — §III B 1, Table I; §IV A, Table III, Figs. 2–3, 8–11.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.9; §2.10.3, Figs. 11–12.
- [Li et al. (2022)](/sources/li-2022-k.md) — §II C; §III A, Figs. 2–3.
- [Chambers et al. (2022)](/sources/chambers-2022.md) — §II (shock-tube turbulence; not a periodic box).
- [Coulon et al. (2023)](/sources/coulon-2023.md) — §2.2 (synthetic inlet turbulence; not a periodic box).
- [Najafiyazdi et al. (2023)](/sources/najafiyazdi-2023.md) — Abstract; §6.1, Fig. 6 (Comte-Bellot–Corrsin decay with approximate deconvolution on unstructured finite elements).
- [Iwata et al. (2023)](/sources/iwata-2023.md) — §II C, Eq. 1, Table I (decaying compressible precursor as detonation inflow).
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.2, Fig. 2a; §2.5; §3.1; §3.3; §4.3; §5 (historical).
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §2.2.2, Table 1, Eqs. 4, 8; §2.4.1 (ODT and LES-ODT on isotropic turbulence, cited).
- [Akbarzadeh & Borazjani (2025)](/sources/akbarzadeh-2025.md) — §3.1, Eqs. 30–32, Fig. 2.
- [De Cosmo et al. (2025)](/sources/decosmo-2025.md) — §2.2; §3.2, Eqs. 15–20, Figs. 3–5.
- [Xiao et al. (2025)](/sources/xiao-2025.md) — §4.1, Fig. 5.
- [Yeung et al. (2025b)](/sources/yeung-2025-b.md) — §2–§3; §4.1–4.2, Table 2.
- [Salehi et al. (2024)](/sources/salehi-2024.md) — §3.2, Fig. 33 (cited flame DNS, review).
- [Fang et al. (2026)](/sources/fang-2026.md) — §5.2 (cited neural operators, review).
- [Bilocq et al. (2025)](/sources/bilocq-2025.md) — §4.1, Tables 1–4, Figs. 1–5; §4.4 (precursor inflow).
- [Bezgin et al. (2025)](/sources/bezgin-2025.md) — §3.1; §4.1–4.2, Table 1, Figs. 2–5; §5.1–5.4, Tables 2–5, Figs. 7–12.
- [Cuadra et al. (2025)](/sources/cuadra-2025.md) — §I; §III B, Table I (review, compiled DNS).
- [Monteiro et al. (2026)](/sources/monteiro-2026.md) — §4.6, Fig. 9; §5.
