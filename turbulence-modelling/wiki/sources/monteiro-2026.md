---
type: Source
title: "Monteiro et al. (2026) — RHEA-X: Distributed GPU-resident high-fidelity flow solver for multiphysics turbulence"
description: "Presents RHEA-X, an open-source GPU-resident compressible DNS solver (C++, MPI and OpenACC with CUDA-aware MPI) with kinetic-energy- and pressure-equilibrium-preserving split forms, real-fluid thermodynamics, a penalty immersed boundary method and Lagrangian particles, validated on canonical flows and scaled to 256 GPUs."
resource: "doi:10.1016/j.cpc.2026.110233"
source_kind: paper
authors: [Monteiro C., Álvarez-Farré X., Martín D., Pizzi F., Jofre L.]
year: 2026
venue: "Comput. Phys. Commun. 326:110233"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2026_Crossref_Computer_Physics_Communications_Monteiro_RHEA-X_Distributed_GPU-resident_high-fidelity_flow_solver_fo.pdf"
tags: [dns, gpu, software, kinetic-energy-preserving, pressure-equilibrium, immersed-boundary]
timestamp: 2026-10-29T05:08:00Z
---

# Summary

Monteiro et al. (2026) present RHEA-X, an open-source (MIT) C++ solver
for [direct numerical simulation](/definitions/direct-numerical-simulation.md)
of compressible multiphysics turbulent flows on Cartesian, optionally
stretched, structured grids, made fully GPU-resident with OpenACC and
CUDA-aware MPI. It succeeds the CPU code RHEA and a partial OpenACC port
whose scaling degraded beyond a few tens of GPUs because of host–device
transfers and managed memory. Convection uses second-order central
differences in split form: the Kennedy–Gruber–Pirozzoli split
([kinetic-energy preservation](/properties/kinetic-energy-preservation.md))
as baseline, the KEEP-PEP scheme of Shima et al. for ideal-gas
[pressure equilibrium](/properties/pressure-equilibrium-preservation.md)
(the underlying KEEP of Kuya and Kawai also preserves entropy,
[entropy conservation](/properties/entropy-conservation.md)), and the
pressure-evolution KEP-PEP form of Bernades et al. for real fluids; HLL,
HLLC, HLLC+ and Murman–Roe fluxes add upwind dissipation where needed
([numerical dissipation](/properties/numerical-dissipation.md)). Time
integration is explicit SSP Runge–Kutta of order 1–3, with an optional
artificial compressibility method at low Mach. Thermodynamics covers ideal
and stiffened gases and the Peng–Robinson real fluid with Chung et al.
transport; modules add a volume-penalization
[immersed boundary method](/methods/immersed-boundary-method.md) with
Monte Carlo sub-cell tagging from STL geometry and Lagrangian point
particles. A comparison table places RHEA-X among other GPU solvers,
including [STREAmS](/software/streams.md), [GALÆXI](/software/galaexi.md)
and [CaLES](/software/cales.md).

Validation covers CO$_2$ properties against NIST, the Sod shock tube, a
[channel](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=590$ against
Moser et al., the [NACA 0012](/benchmarks/naca-0012-airfoil.md) at
$12^\circ$ and $Re_c=50000$ with the immersed boundary against DNS of
Rodríguez et al., a supercritical nitrogen jet against Raman data,
particle-laden forced [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
and a two-dimensional [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
for second-order convergence; a [cylinder](/benchmarks/circular-cylinder-wake.md)
case at $Re_D=3900$ is in the public test suite but not shown. On
MareNostrum 5 and Snellius (A100, H100) the routines run 11–46 times
faster on an H100 than on the CPU, CUDA-aware MPI beats host-staged MPI by
up to 8.84 times, the largest speed-up over the CPU is 66.25 at 128 GPUs,
and strong-scaling efficiency stays above 90% up to 64 GPUs on the large
mesh. No closure model is involved.

# Version read

Version of record (Elsevier, open access CC BY-NC-ND; received 12 November
2025, revised 10 April 2026, accepted 18 May 2026, online 20 May 2026), 24
pages, all read; pp. 5, 6 and 10 checked visually. Page 1 matches the
Crossref metadata; no identity issue. Program files are in the CPC Library
(doi:10.17632/dwv8gx3z9z.1). Equation, table, figure, listing and section
numbers are those of this version.

# Key claims

Page-local symbols: $\delta^h_j$ the second-order central difference;
$\xi_{\mathrm{KEP}}$ the blending parameter of the KEP split family and
$\eta_{\mathrm{PE}}$ the split parameter of the pressure-convection term; $\lambda_{\mathrm{th}}$
the thermal conductivity; $c$ the sound speed; $\chi_{\mathrm{IBM}}$ the
solid indicator, $K_{\mathrm{IBM}}=-\alpha_{\mathrm{IBM}}\Delta t$ the
penalization coefficient; $St_p=\tau_p/\tau_f$ the particle Stokes number;
CAMPI and CUMPI the CUDA-aware and host-staged MPI configurations; RF–HC the
real-fluid configuration with high-pressure transport and pressure
transport.

1. RHEA-X is fully GPU-resident: the entire time-integration loop runs on the device, and host–device transfers are restricted to initialization and output when CUDA-aware MPI is enabled (§3, §3.3). **Stated**
2. Managed memory was not adopted because explicit memory management gives "approximately 2× in time-to-solution" better performance, per the authors' earlier study (§3.2). **Stated** (cited)
3. The earlier partial OpenACC port achieved "up to a six-fold reduction in time-to-solution", but its scalability "degraded beyond a few tens of GPUs" (§3). **Stated** (cited)
4. With second-order central $\delta^h_j$ the split form $C^{\mathrm{split}}_{\rho\phi}=\xi_{\mathrm{KEP}}(C^D+C^\phi)/2+(1-\xi_{\mathrm{KEP}})(C^u+C^\rho)/2$ (Eq. 20) is skew-symmetric in the discrete inner product, and $\xi_{\mathrm{KEP}}=1/2$, the KGP split and the baseline, gives "second-order accuracy, low dispersion, and exact discrete kinetic-energy conservation" (§2.3.1). **Stated**
5. KEEP-PEP, with internal-energy flux $(p_{m+1}+p_m)(u_{j,m+1}+u_{j,m})/[4(\gamma-1)]$ (Eq. 21), keeps a uniform pressure invariant under the ideal-gas assumption and preserves kinetic energy, entropy and pressure equilibrium (§2.3.1). **Stated** (cited)
6. The pressure-evolution formulation (Eqs. 22–23, $\eta_{\mathrm{PE}}=0$) "preserves kinetic energy and pressure equilibrium to second order even under real-fluid conditions"; total energy is not strictly conserved, but "the residual error is dissipative and decays quadratically with grid refinement"; it is preferred for transcritical and supercritical flows (§2.3.1). **Stated** (cited)
7. SSP-RK schemes of order 1–3 in Shu–Osher form (Eqs. 24–30) "do not impose a more restrictive time-step than the forward Euler method" (§2.3.2). **Stated**
8. The artificial compressibility option, with a speed-up factor chosen automatically for a prescribed relative error, "delivered order-of-magnitude computational savings while accurately reproducing both mean and fluctuating statistics" in the cited tests (§2.3.2). **Stated** (cited)
9. Peng–Robinson with Chung et al. properties for CO$_2$ at $P/P_{\mathrm{cr}}=1.5$ and 2.0 shows "a good degree of agreement" with NIST for density, viscosity and Prandtl number, capturing the pseudo-boiling region at about 330 K (§4.1, Fig. 1). **Shown**
10. The Sod shock tube with HLLC converges to the exact solution for $\Delta x=10^{-2}$, $10^{-3}$, $10^{-4}$ m at CFL 0.9 (§4.2, Fig. 2). **Shown**
11. Channel at $Re_\tau=590$ ($384\times257\times384$): mean velocity and rms profiles agree with Moser et al., with the peak of $\langle u'u'\rangle^+$ at $y^+\approx14$ (§4.3, Fig. 4). **Shown**
12. NACA 0012 at $12^\circ$, $Re_c=50000$, $M=0.1$ ($1086\times1037\times128$ points): $C_p$ and $C_f$ are "in close agreement" with the DNS of Rodríguez et al., including the leading-edge suction peak, pressure plateau and separation-induced skin-friction reversal, with the penalty immersed boundary (§4.4, Fig. 5). **Shown**
13. Supercritical nitrogen jet (Mayer et al. Case 4): the centreline density decay agrees closely with Raman data, "a modest improvement" over the Favre-averaged Navier–Stokes predictions of the original study; spectra show a $k^{-5/3}$ range at $x/D_j=5$ and 30 (§4.5, Fig. 8). **Shown**
14. Particle-laden forced isotropic turbulence ($320^3$, $Re_\lambda\approx90$, $10^6$ tracers): the PDF of Voronoi cell volumes collapses onto the Gamma distribution of randomly distributed tracers, so no spurious numerical clustering appears (§4.6, Fig. 9). **Shown**
15. Two-dimensional Taylor–Green vortex at $Re=100$: second-order convergence of the $L_2$ errors of $u$ and $v$ on CPU and GPU (App. B, Fig. B.1). **Shown**
16. The immersed boundary and point-particle modules cost "on the order of 10%" of the runtime relative to the flow framework (§5.1, Fig. 10). **Shown**
17. On CPUs the real-fluid thermodynamics raises total runtime by 82–88%, "consistent with the 72% increase reported in CUBENS" (§5.1). **Shown** (own) / **Stated** (CUBENS)
18. Routine breakdown for RF–HC: on the CPU viscous 36.9%, inviscid 16.3%, equation of state and transport 30.5%, auxiliary 16.3%; on the GPU viscous 42.2%, inviscid 20.0%, equation of state and transport 14.1% (§5.2, Fig. 11). **Shown**
19. H100 against CPU routine speed-ups: viscous fluxes up to 15, inviscid 13, equation of state and transport 46, auxiliary 11; the 64 GB and 94 GB H100 results are "nearly indistinguishable" (§5.2, Fig. 12). **Shown**
20. The viscous-flux kernel is predominantly memory-bound; tiling or fusion could give roughly a factor two (as in URANOS-2.0) but was not pursued for portability and maintainability (§5.2). **Stated**
21. Single-GPU sweep $32^3$–$512^3$: CAMPI reaches near-ideal scaling beyond $128^3$ and outperforms CUMPI by 2–4 times and the CPU by more than an order of magnitude (§5.2, Fig. 14). **Shown**
22. Maximum speed-ups (Table 3): H100 64 GB (MareNostrum 5) CAMPI/CPU 23.30 at 8 GPUs ($500^3$) and 22.92 at 32 ($1000^3$), CUMPI/CPU 6.79 at 1 and 8.07 at 8, CAMPI/CUMPI 6.05 at 64 and 5.16 at 256; H100 94 GB (Snellius Phase 3) 36.46 at 8 and 66.25 at 128, 17.46 at 1 and 16.73 at 8, 8.84 at 64 and 6.29 at 128; A100 40 GB (Snellius Phase 1) 22.65 at 2 ($400^3$) and 22.52 at 32 ($800^3$), 6.92 at 1 and 7.06 at 8, 5.51 at 64 and 3.62 at 64. **Shown**
23. On the baseline mesh the CPU strong-scaling efficiency exceeds that of CAMPI beyond 16 GPUs (H100) and 8 GPUs (A100), owing to GPU under-utilisation and the communication-to-computation ratio; the real-fluid closure "is not the primary cause" (§5.3). **Shown**
24. On the larger mesh CAMPI keeps strong-scaling efficiencies "above 90% up to 64 GPUs" and near-ideal behaviour up to 128 GPUs on both H100 platforms, with a maximum speed-up of "approximately 70×" over the CPU on 128 GPUs (§5.3). **Shown**
25. Weak scaling: CAMPI stays mostly above 90% of ideal, while CPU and CUMPI drop to 69% and 52% on Snellius Phase 3 (§5.3). **Shown**
26. Deviations from ideal at the largest GPU counts "appear attributable to interconnect bandwidth constraints rather than algorithmic limitations" (§5.3). **Stated**
27. As a fully local compressible formulation without FFT-based Poisson solves, RHEA-X needs no global transposes; communication is halo exchange only (§3.3). **Stated**

The channel grid of claim 11 is printed with $\Delta x^+\approx9.8$,
$\Delta z^+\approx5.0$ for $L_x=2\pi\delta$, $L_z=\pi\delta$ and
$N_x=N_z=384$. *(Compiler check, not in the sources: at the nominal
$Re_\tau=590$ these give $\Delta x^+=2\pi\cdot590/384=9.65$ and
$\Delta z^+=\pi\cdot590/384=4.83$.)*

# Printed slips

- **§5.3:** "CUMPI still achieves a significant effective speed-up of up to 17× compared with CPU execution on a single A100 GPU"; Table 3 prints 6.92 for CUMPI/CPU on one A100 and 17.46 on one H100 94 GB.
- **§5.3, abstract, conclusions:** maximum CAMPI speed-up "approximately 70×" on 128 GPUs; the Table 3 maximum is 66.25.
- **Abstract, conclusions:** "97% of ideal strong-scaling behavior is maintained up to 64 GPUs"; §5.3 states "above 90% up to 64 GPUs" and prints no 97%.
- **Algorithms 1 and 2:** Algorithm 1 (line 15) performs the halo exchange of conserved variables once after the RK stage loop, Algorithm 2 (line 21) inside every stage.
- **§2.2:** Sutherland's law is cited as [77] (Poling et al.), and as [78] (Sutherland 1893) in §2.2.1.
- **Eq. (22):** $\beta_v$ and $\beta_T$ are not defined.
- **§2.2:** the Chung correlation inputs read "association factor $\kappa_a$ and dipole moment , and" (symbol missing).
- **References:** ref. [111] prints "R. Monchaux, F. Bourgoin", ref. [112] "R. Monchaux, M. Bourgoin"; ref. [37] (CaLES) is printed without a journal name.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf u=(u,v,w)$, $P$, $T$ | $\rho$, $\boldsymbol u$, $p$, $T$ | |
| $E=e+|\mathbf u|^2/2$ | $E/\rho$ | registry $E$ is per unit volume |
| $\boldsymbol\tau$, $\tau_{ij}$ | $\sigma_{ij}$ | viscous stress; **collision** with the SGS stress |
| $\kappa$ | $\lambda_{\mathrm{th}}$ (page-local) | thermal conductivity; **collision** with the von Kármán $\kappa$ |
| $\delta_j$ | $\delta^h_j$ (page-local) | discrete central derivative |
| $\xi$ | $\xi_{\mathrm{KEP}}$ (page-local) | **collision** with the reference coordinate $\xi$ |
| $\eta$ (Eq. 23) | $\eta_{\mathrm{PE}}$ (page-local) | **collision** with the Kolmogorov length (and registry §11 $\eta_p$, the penalization permeability) |
| $c$, $c_s$ | $c$ (page-local) | sound speed; $c$ is also the chord in $Re_c$, $c_i$ an SSP-RK coefficient |
| $Z=P/(\rho R'T)$ | (page-local) compressibility factor | |
| $\chi$, $\alpha$, $K_{\mathrm{IBM}}$ | $\chi_{\mathrm{IBM}}$, $\alpha_{\mathrm{IBM}}$, $K_{\mathrm{IBM}}$ (page-local) | **collision** with SA $\chi$ and the DG/FV blending $\alpha$ |
| $St=\tau_p/\tau_f$ | $St_p$ (page-local) | **collision** with the Strouhal number |
| $\langle f\rangle$, $f'$; $\tilde f=\langle\rho f\rangle/\langle\rho\rangle$, $f''$ | $\langle\phi\rangle$, $\phi'$; $\langle\phi\rangle_\rho$, $\phi''$ | **the tilde is a Favre average, not a Favre filter** |
| $Re$, $Pr$, $Ma$, $Br$, $Ec$ | $Re$, $Pr$, $M$, $Br$, $Ec$ | $Br=Pr\,Ec$ |
| $u_\tau$, $\delta_\nu$, $Re_\tau$, $\delta$ | $u_\tau$, $\delta_\nu$, $Re_\tau$, $\delta$ | channel half-height |
| $Re_c$, $Re_\lambda$ | $Re_c$, $Re_\lambda$ | |

# Reference list

122 printed references, numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Ref. [63] is
the ingested [bernades-2023](/sources/bernades-2023.md), ref. [48] the
ingested [kurz-2025](/sources/kurz-2025.md); ref. [13] (Kim & Leonard,
Annu. Rev. Fluid Mech. 56) is the ingested [kim-2024-b](/sources/kim-2024-b.md),
though its printed key is that of a different work. Ref. [37] has no
journal name; ref. [57] (Amdahl) prints no year and refs. [115], [116],
[118] print "n.d."; refs. [2] and [36] are arXiv preprints, kept as their
own entries; refs. [68], [69] are datasets with printed DOIs; the printed
initials of refs. [2], [45], [46], [47], [50] and [80] absorb surname
particles ("F.D. Vanna", "M.D. Renzo", "O.L. Métayer"). No item is
unparseable.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)
- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Turbulent round jets](/benchmarks/turbulent-round-jet.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Immersed boundary methods](/methods/immersed-boundary-method.md)
- [Entropy conservation and entropy stability](/properties/entropy-conservation.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md)
- [CaLES](/software/cales.md)
- [GALÆXI](/software/galaexi.md)
- [STREAmS](/software/streams.md)
