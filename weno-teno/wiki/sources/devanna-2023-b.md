---
type: Source
title: "De Vanna et al. (2023) — URANOS: A GPU accelerated Navier-Stokes solver for compressible wall-bounded flows"
description: "Software paper on URANOS, a Fortran/OpenACC/MPI high-order finite-difference solver for compressible wall-bounded flows: energy-preserving central scheme hybridized with WENO-Z, TENO or TENO-A by a priori shock sensors, conservative viscous fluxes, LES and wall models, GPU porting and scaling, and channel and boundary-layer validation."
resource: "doi:10.1016/j.cpc.2023.108717"
source_kind: paper
authors: [De Vanna F., Avanzi F., Cogo M., Sandrin S., Bettencourt M., Picano F., Benini E.]
year: 2023
venue: "Comput. Phys. Commun. 287:108717"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computer_Physics_Communications_De_URANOS_A_GPU_accelerated_Navier-Stokes_solver_for_compressib.pdf"
tags: [software, gpu, finite-difference, turbulence, teno, hybrid-scheme]
timestamp: 2026-10-23T11:06:00Z
---

# Summary

[URANOS](/software/uranos.md) is a Fortran 90 + OpenACC + MPI high-order
finite-difference solver for the filtered compressible Navier–Stokes equations on
uniform or stretched Cartesian meshes. It targets wall-bounded flows with DNS,
wall-resolved LES and equilibrium
[wall-modelled LES](/methods/wall-modeled-les.md).

Its numerics are recalled from earlier work, with no new formulas. Six convective
schemes are available:

- a sixth-order central, fully split, energy-preserving (EP) scheme after
  Pirozzoli;
- [WENO-Z](/methods/weno-z.md) of orders 3, 5 and 7 after Castro, Costa and Don,
  with $\epsilon=10^{-12}$;
- TENO5 with $C_T=10^{-7}$;
- [TENO-A5](/methods/adaptive-teno.md), whose $C_T$ varies between $10^{-10}$ and
  $10^{-7}$.

They are used pure or hybridized: the shock-capturing scheme is applied only
where one of three a priori sensors exceeds a user threshold, and the EP scheme is
used elsewhere. The viscous fluxes are discretized in conservative form with
high-order interface stresses. Time stepping is the three-stage SSP Runge–Kutta
scheme.

The contribution is the GPU port:

- one OpenACC data region around the time loop, with `parallel loop gang vector
  collapse(3)` kernels;
- rank-to-GPU binding;
- host-staged and GPU-aware variants of blocking, non-blocking and
  derived-datatype halo exchange.

On a $256^3$ problem, a single GPU beats a full CPU node by $\times3.50$ (V100 vs
POWER9), $\times1.92$ (V100 vs Xeon) and $\times2.38$ (A100 vs EPYC). Weak-scaling
efficiency stays at or above 75% up to 256 GPUs.

Validation covers convergence on a smooth wave, Sod and Shu–Osher, a four-quadrant
2D Riemann problem, a viscous Kolmogorov flow, and two wall-bounded cases:

- [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) at
  $\mathrm{Re}_\tau=180$ to $5200$, bulk Mach 0.1 and 1.5;
- the [supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
  at $M_\infty=2$ and $5.86$, the latter in WMLES with TENO-A5.

Both are compared with reference DNS. There are no theorems.

# Version read

Version of record (Elsevier typeset, open access CC BY), received 10 Oct 2022 and
online 9 Mar 2023. It has 18 pages, all read, with pp. 4, 5, 9, 10 and 15–17 also
read visually. Page 1 matches Crossref (title, seven authors, venue, DOI). The
program is available as CPC Library doi:10.17632/pw5hshn9k6.1 and at
gitlab.com/fralusa/uranos_gpu (BSD 2.0). The program title is printed as
"Unsteady Robust All-around Navier-StOkes Solver".

# Key claims

1. URANOS provides six convective schemes: a sixth-order central, nominally non-dissipative, fully split energy-preserving (EP) scheme; WENO-Z of orders 3, 5 and 7; TENO5; and TENO-A5 (§3.1). **Stated**
2. The EP scheme preserves total kinetic energy $\kappa$ semi-discretely in the incompressible inviscid limit, on uniform and non-uniform Cartesian meshes, but "cannot stably develop shocks/shocklets" (§3.1). **Stated** (cited)
3. WENO-Z follows Castro et al.; $\epsilon$ is "adjusted to $10^{-12}$" to limit dissipation (§3.1). **Stated**
4. TENO5 uses a fixed $C_T=10^{-7}$ (the parameters of Fu et al. 2017). TENO-A5 (parameters of Fu et al. 2018) varies $C_T$ between $10^{-7}$ and $10^{-10}$, with $b_1=10.5$, $b_2=3.5$, $C_r=0.25$ and $\xi_{\mathrm A}=10^{-3}$ (§3.1–3.2). **Stated**
5. Hybridization: WENO/TENO is applied only where an a priori sensor $\Psi_{\mathrm D,i+1/2}$ exceeds a user threshold $\Psi^*$, and the EP scheme is used elsewhere. The flagged band is extended by 2, 3 or 4 cells for WENO/TENO orders 3, 5 and 7 (§3.2, Eqs. 8–10). **Stated**
6. The density-jump sensor (Eq. 9) "generally reduces the WENO/TENO intervention compared to the density gradient" (Eq. 8). The improved Ducros sensor (Eq. 10) is recommended for wall flows (§3.2). **Stated**
7. Hybrid schemes have discontinuous error scaling because of the shock detection, so error scaling is reported only for the pure schemes. $\Psi^*$ is strongly flow-dependent and needs preliminary tuning (§3.2). **Stated**
8. The incompressible part of the viscous term is discretized in conservative flux-difference form with high-order interface stresses (Eqs. 11–13). The scheme reverts to standard collocated finite-difference accuracy for smooth viscosity, and it "conserves viscous fluxes independently of grid stretching/resolution or viscosity variations" (§3.3). **Stated** (cited)
9. Time integration is the three-stage third-order TVD Runge–Kutta of Gottlieb and Shu (Eq. 14). A "linear analysis ... proved that the stability is recovered up to $CFL=1$". The recommended values are $\nu=0.5$–$0.8$ and Fourier number 0.1–0.3 (§3.4, Eqs. 15–16). **Stated**
10. The GPU strategy is a single `!$acc data copy` region outside the time loop. All routines of the RK substeps are ported with the `parallel` construct (not `kernels`) and `loop gang, vector collapse(3)` (§4.1.1, Algorithms 1–2). **Stated**
11. Three MPI options are offered: blocking SENDRECV, non-blocking ISEND/IRECV, and non-blocking with derived datatypes. On CPU the first two perform almost equally and the third "considerably outperformed" them. Derived datatypes are not reported on GPU, because OpenACC is "not optimised for dealing with MPI DDT" (§4.1.2). **Stated**
12. Host-staged MPI uses asynchronous `update host/device` queues to hide staging behind the MPI calls. GPU-aware MPI passes device pointers through `host_data use_device` (§4.1.2, Algorithms 4–5). **Stated**
13. Single node vs single GPU on a $256^3$ 3D bi-periodic Riemann problem, in s per iteration (§4.2.1, Fig. 1). **Shown**
    - MARCONI100: POWER9 node 3.13 s; V100 host-staged 0.99 s ($\times3.15$); V100 GPU-aware 0.89 s ($\times3.50$).
    - GALILEO100: Xeon node 1.77 s; V100 host-staged 1.14 s ($\times1.55$); GPU-aware 0.92 s ($\times1.92$).
    - DGX-A100: EPYC node 1.16 s; A100 host-staged 0.58 s ($\times2.01$); GPU-aware 0.49 s ($\times2.38$).
14. The interconnects are NVLink 2.0 on MARCONI100, PCIe3 on GALILEO100, and NVLink 3.0 (GPU–GPU) with PCIe4 (CPU–GPU) on DGX-A100 (Fig. 1 caption). **Stated**
15. Profiling on MARCONI100 (Fig. 2): the RHS takes about 95% of an iteration. The MPI boundary exchange is sped up $\times6.2$ (host-staged) and $\times57.8$ (GPU-aware) over a CPU node, "nearly $\times10$" between the two (§4.2.2). **Shown**
16. Strong scaling ($512\times256\times256$, up to 32 units): CPU efficiency is about 60% on 32 nodes, and GPU efficiency is "reduced by around 50% using 32 GPUs". GPU-aware is slightly better than host-staged (§4.2.3, Fig. 3a). **Shown**
17. Weak scaling ($256^3$ per unit): the parallel efficiency "never goes under 75%, even with 256 computational units" (§4.2.3, Fig. 3b). **Shown**
18. Default Spectrum MPI bindings cost 4% only for single-node 4-GPU host-staged runs (§4.2.3). **Shown**
19. The abstract claims "over three times speed-up for a node-to-node comparison, even at large scales, with an efficiency of about 80% while using 1024 GPUs" (abstract). **Stated**. The body reports single-GPU vs single-node comparisons and weak scaling only up to 256 units.
20. All six convective schemes converge at their theoretical order in $L_1$, $L_2$ and $L_\infty$ on an advected harmonic density wave (App. A.1, Fig. 11). **Shown**
21. On Sod and Shu–Osher (200 points) all shock-capturing schemes "accurately represent the system dynamics", with improvement with order and from WENO to TENO (App. A.2, Fig. 12). **Shown**
22. On the four-quadrant 2D Riemann problem ($1600^2$), higher WENO order and TENO resolve more shear-layer instabilities and more detail in the central plume (App. A.3, Fig. 13). **Shown**
23. The viscous discretization converges at 2nd, 4th and 6th order on a laminar Kolmogorov flow (App. A.4, Fig. 14). **Shown**
24. Channel DNS at bulk Mach 0.1, $\mathrm{Re}_\tau=180$, agrees with Bernardini et al. CPU and GPU results agree "down to machine precision"; the computed $\mathrm{Re}_\tau$ is 179 (§5.1, Table 1, Fig. 4). **Shown**
25. Channel DNS at bulk Mach 1.5, $\mathrm{Re}_\tau=215$, agrees with Modesti and Pirozzoli in velocity, Reynolds stresses and temperature (§5.1, Fig. 5). **Shown**
26. WRLES of the channel at $\mathrm{Re}_\tau=590$ on $96^3$: the $\mathrm{Re}_\tau$ error is 0.3% with MXTS and 0.6% with each of Sigma and WALE, against Vreman–Kuerten (§5.1, Table 1, Fig. 6). **Shown**
27. WMLES of the channel at $\mathrm{Re}_\tau=5200$ on $160\times128\times80$ agrees with the reference DNS away from the wall (§5.1, Fig. 7). **Shown**
28. Supersonic boundary layer ($M_\infty=2$, $\mathrm{Re}_\tau=250$): DNS ($2800\times128\times600$) agrees excellently and WRLES ($768\times128\times128$, WALE) agrees well with Pirozzoli–Bernardini (§5.2, Figs. 8–9). **Shown**
29. Hypersonic WMLES boundary layer ($M_\infty=5.86$, $\mathrm{Re}_\tau=1200$, wall-temperature ratio 0.76) with TENO-A5: excellent agreement with Cogo et al. in mean velocity and temperature, with deviations in inner-layer turbulent kinetic energy (§5.2, Fig. 10). **Shown**
30. The GPU weak scaling is "in line with" AFiD, CaNS and STREAmS. A lattice-Boltzmann code on 512 GPUs is quoted as "a factor 10 of acceleration compared to URANOS" (§4.2.3). **Stated**

# Printed slips

- Eq. (15c) is labelled $\Delta t_{Fo1}$ like Eq. (15b), while Eq. (16) uses $\Delta t_{Fo1}$ and $\Delta t_{Fo2}$ (p. 5).
- p. 5: "Here $\Delta x$, $\Delta z$ and $\Delta z$ are the grid step along the x, the y and the z coordinate"; the second should be $\Delta y$. Also "CFL an FO".
- §2.1: "$\tilde e=c_p\tilde T$" for the internal energy, with $c_v=R/(\gamma-1)$ defined in the same sentence. Internal energy is $c_vT$; $c_pT$ is the enthalpy.
- §2.1/§3.3: the conductivity $\lambda=c_p\mu/\mathrm{Pr}$ is called "thermal diffusivity".
- Fig. 7 caption cites DNS by Moser et al. [59], while the text cites Lee and Moser [58] for the same comparison.
- Fig. 10 caption: "DNS of turbulent boundary layer at $M_b=5.86$". The case is a WMLES (Table 2), and the Mach number is the free-stream $M_\infty$.
- The Sigma model is attributed to Toda et al. [16] in §2.2 and to [56] (Rieth et al.) in §5.1.
- App. A.2: the reference is "a $N_x=2000$ points numerical solution", while the Fig. 12 legend says "exact" and the caption "analytical".
- Eqs. (8)–(9): $\theta_{i+1/2}=\max_{j=1}^3\lvert\rho_{j+1}-\rho_j\rvert$ (and the gradient form) has a right side that does not depend on $i$, and $j$ is used both as a direction index and as a grid index.
- Algorithm 2 opens `!$acc parallel default(present)` with `!$acc loop` but closes with `!$acc end parallel loop`.
- Eq. (14) is called "low-storage", but the printed Shu–Osher form keeps $U^n$ through the step *(compiler check, not in the sources)*.
- Table 1: $\mathrm{Re}_\tau=586$ against 590 is a 0.68% error, printed "0.6%". *(compiler check, not in the sources)*
- References: [60] prints "S.K. Lelef"; [5]–[7] fuse the code name into the last author ("Neil D. Sandham Opensbli", "Peter E. Vincent Pyfr", "Antony Jameson Zefr"); [15] prints "Nicoud Franck".

# Notation map

| De Vanna et al. (2023b) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\bar\phi$, $\tilde\phi$ | kept | Reynolds and Favre filtering |
| $\bar\rho$, $\tilde u_i$, $\bar p$, $\tilde E$ | $\rho$, $v_i$, $p$, $E/\rho$ | **$\tilde E$ is per unit mass; the registry's $E$ is per unit volume** |
| $\gamma$ | $\gamma$ | default 1.4 |
| $\varepsilon$ (WENO-Z) | $\epsilon$ | WENO-Z regularization $10^{-12}$ |
| $\varepsilon$ (Eq. 10) | $\epsilon_{\mathrm D}$ (page-local on [Ducros shock sensor](/definitions/ducros-shock-sensor.md)) | Ducros-sensor regularization $(v_\infty/L)^2$; **same letter as the WENO-Z $\varepsilon$ in the source** |
| $C_T$ | $C_T$ | agrees |
| $\alpha_1$, $\alpha_2$, $C_r$, $\xi$ | $b_1$, $b_2$, $C_r$, $\xi_{\mathrm A}$ | TENO-A constants as on [adaptive TENO](/methods/adaptive-teno.md); **$\alpha$ also names the mesh stretching and the forcing amplitude** |
| $\theta_{i+1/2}$, $\bar\theta$ | $\Psi_{\mathrm D,i+1/2}$, $\Psi^*$ (as on [URANOS](/software/uranos.md) and the Ducros page) | shock-sensor value and threshold, the same letters for all three sensors; **$\theta$ is the Zhang–Shu factor in the registry** |
| $\hat\tau_{i+1/2}$, $\mathcal J_{i+1/2}$ | kept | interface viscous stress and heat flux |
| $\beta_l$, $\gamma_l$ | kept locally | viscous interpolation/derivative coefficients; **collide with $\beta_k$ and $\gamma$** |
| $\mathcal N(U)$ | $\mathcal L(u)$ | semi-discrete operator |
| $CFL$, $FO$ | $\nu$, kept | Courant and Fourier numbers |
| $\kappa$ (wall model) | kept locally (von Kármán constant 0.41) | **$\kappa$ is the kinetic energy in the registry** |
| $M_b$, $M_\infty$, $\mathrm{Re}_\tau$ | $M$ with subscript, $\mathrm{Re}_\tau$ | bulk and free-stream Mach numbers |

# Reference list

There are 69 printed references in numbered style ([1]–[69]). No titles are
printed for journal articles. All are parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `devanna-2023-b`. Name oddities
are listed under Printed slips. [10] and [65] lack pages or article number, [66]
lacks a volume, and [49] is undated (keyed with the citing year). The corporate
authors are OpenACC, NVIDIA and CINECA. Ref. [23] is the planned Source
`devanna-2023` (Comput. Fluids 250:105710), the same work, cited on the
bundle pages as [De Vanna et al. (2023a)](/sources/devanna-2023.md). No printed duplicates
were found.

# Pages created or updated

Chunk 5 (2026-10-22), cited further in chunks 6–9 (2026-10-23). This source is cited on:

* [Adaptive TENO (TENO-A, TENO-AA)](/methods/adaptive-teno.md)
* [Ducros shock sensor](/definitions/ducros-shock-sensor.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [PyFR](/software/pyfr.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [STREAmS](/software/streams.md)
* [Supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md)
* [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
* [Two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)
* [URANOS](/software/uranos.md)
* [Wall-modelled large-eddy simulation](/methods/wall-modeled-les.md)
* [WENO-Z weights](/methods/weno-z.md)
