---
type: Source
title: "Wilfong et al. (2026) — MFC 5.0: An exascale many-physics flow solver"
description: "Release paper of MFC 5.0, a GPU finite-volume solver for compressible multiphase flow: unchanged WENO and HLL/HLLC core, new WENO-Z and TENO weights on non-uniform grids, low-Mach HLLC fixes, characteristic boundary conditions, immersed boundaries, splitting for stiff sources, MHD and many-physics models, with GPU performance and scaling data."
resource: "doi:10.1016/j.cpc.2026.110055"
source_kind: paper
authors: [Wilfong B., Le Berre H.A., Radhakrishnan A., Gupta A., Vickers D.J., Vaca-Revelo D., Adam D., Yu H., Lee H., Chreim J.R., Carcana Barbosa M., Zhang Y., Cisneros-Garibay E., Gnanaskandan A., Rodriguez Jr M., Budiardja R.D., Abbott S., Colonius T., Bryngelson S.H.]
year: 2026
venue: "Comput. Phys. Commun. 322:110055"
local_file: "/home/stefano/papers/mosaic/weno-teno/2026_Crossref_Computer_Physics_Communications_Wilfong_MFC_50_An_exascale_many-physics_flow_solver.pdf"
tags: [software, gpu, multiphase, weno, teno, riemann-solver]
timestamp: 2026-10-23T20:29:00Z
---

# Summary

Wilfong et al. (2026) announce [MFC](/software/mfc.md) 5.0, the successor of MFC 3.0
([Bryngelson et al. (2021)](/sources/bryngelson-2021.md)). MFC is a finite-volume
solver for compressible multi-component and multiphase flow. It is built on the
[five-equation](/definitions/five-equation-model.md) models of Kapila et al. and
Allaire et al. and on the [six-equation](/definitions/six-equation-model.md)
pressure-disequilibrium model of Saurel et al., closed with the stiffened-gas
equation of state. The core is unchanged from 3.0: cell averages, WENO
reconstruction of the interface states (fifth order kept with Henrick's mapped
weights), [HLL or HLLC](/methods/hll-riemann-solvers.md) fluxes, SSP Runge–Kutta
stepping and Thompson characteristic boundary conditions.

The numerical additions of 5.0 are WENO-Z and TENO weights at orders 3, 5 and 7, with
a generic non-uniform-grid reconstruction written in cell-average differences to cut
operation counts. They also include generalized characteristic relaxation boundary
conditions (Pirozzoli & Colonius), and Strang [operator splitting](/methods/operator-splitting.md)
with an adaptive embedded RK3(2) pair for stiff bubble sources. Two low-Mach fixes for
HLLC are implemented, Thornber et al.'s velocity modification and Chen et al.'s
anti-dissipation pressure correction; both keep the [Gresho vortex](/benchmarks/gresho-vortex.md)
down to $M=10^{-4}$, where plain HLLC fails; this is the low-Mach
[numerical dissipation](/definitions/numerical-dissipation.md) problem that
[semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md) treat by other means. On the
physics side, 5.0 adds ghost-cell [immersed boundaries](/methods/immersed-boundary-method.md),
infinite-rate phase change, Euler–Euler and Euler–Lagrange sub-grid bubbles,
hypo- and hyperelastic solids, reacting multispecies gas, surface tension in the
six-equation model, and ideal MHD with HLLD plus relativistic MHD. The software part
covers OpenACC and OpenMP offload from one source through Fypp macros, compile-time
case optimization, golden-file regression tests and per-process file I/O.

Evidence is convergence plots ([interface advection](/benchmarks/material-interface-advection.md),
linear advection, reacting [density waves](/benchmarks/density-wave-advection.md),
the [Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)), comparison with
published results ([Brio–Wu](/benchmarks/brio-wu-shock-tube.md), a
[reactive shock tube](/benchmarks/shock-induced-combustion.md), a Laplace pressure
jump) and performance data. Demonstrations include a
[shock–bubble](/benchmarks/shock-bubble-interaction.md) run at more than $8\times10^9$
points and a $1600^3$ [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md).
The paper has no theorems.

# Version read

The archive file is the version of record (Comput. Phys. Commun. 322:110055, section
"Computer Programs in Physics"; received 12 April 2025, revised 18 January 2026,
accepted 23 January 2026, online 30 January 2026), 23 pages, all read; pp. 3, 5, 10
and 12 checked on the page images. Title, the 19 authors and DOI match the Crossref
record; Wilfong, Le Berre and Radhakrishnan are marked as equal contributors. The
program summary gives the MIT licence, Fortran 2008 and Python, and states that the
new version supersedes MFC 3.0 (Comput. Phys. Commun. 266:107396).

# Key claims

Registry notation: cell averages $\bar u_i$, one-sided states $u^\mp_{i+1/2}$ (source
$q^{(L)}$, $q^{(R)}$), $r$ the number of points of a classical WENO candidate stencil
(source $k$, order $2r-1$), candidate index $k$ (source $r$), $d_k$, $\beta_k$,
$\alpha_k$, $\omega_k$, $\tau$, $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$; HLL speeds
$s^\pm$; volume fractions $\phi_k$, stiffened-gas constants $p_{\infty,k}$.
Page-local: $K_{\mathrm{Ka}}$ the Kapila coefficient; $s_*$ the HLLC contact speed;
$z_{\mathrm M}$ the low-Mach blending factor; $p_{\mathrm d}$ Chen et al.'s pressure
term; $\Delta\bar u_j=\bar u_{j+1}-\bar u_j$.

1. MFC 5.0 ran "the largest-to-date public CFD simulation at 200 trillion grid points" (1 quadrillion degrees of freedom), a 2025 Gordon Bell Prize finalist (Abstract, §1.2). **Stated**
2. The core diffuse-interface method (five- and six-equation models, finite-volume WENO with HLL/HLLC) is unchanged from MFC 3.0 apart from performance, testing and added physics (§2.1, §3). **Stated**
3. The $K_{\mathrm{Ka}}\nabla\cdot v$ term of Kapila's model gives thermodynamic consistency and is needed for spherical bubble collapse, but it is non-conservative and can cause numerical instability; without it the model is Allaire et al.'s (§2.1.1, after Schmidmayer et al.). **Stated**
4. The six-equation model in the infinite-relaxation limit has the same physics as Kapila's model but avoids the instability arising "from some interface capture schemes" (§2.1.2). **Stated**
5. The 3.0 scheme converges at the design orders 1, 3, 5 on a 1D two-component periodic advection after five periods, with HLL and HLLC (§3.5, Fig. 1). **Shown**
6. WENO-Z and TENO at orders 3, 5, 7 "recover their intended design orders, consistent with the original WENO-JS" on 1D linear advection (§4.2.2, Fig. 12). **Shown**
7. WENO-Z improves the spectral properties of classical WENO "while being faster than WENO-M"; its exponent $q$ is "typically set to 1 for fifth-order reconstruction"; its weights $\alpha_k=d_k\big(1+(\tau/(\beta_k+\epsilon))^q\big)$ with $\tau=\lvert\beta_0-\beta_{r-1}\rvert$ "apply to schemes of order 3, 5, and 7" (§4.2.2). **Stated**
8. TENO as implemented: "a $K$th order accurate TENO scheme uses $K-2$ candidate stencils of increasing width", with $\omega_k=d_k\delta_k/\sum_ld_l\delta_l$, $\delta_k=0$ if $\chi_k<C_T$ and 1 otherwise, $\chi_k=\gamma_k/\sum_l\gamma_l$ and $\gamma_k=d_k\big(1+\tau/(\beta_k+\epsilon)\big)^6$, $\tau$ the WENO-Z indicator; no values of $C_T$ or $\epsilon$ are given (§4.2.2). **Stated**
9. Writing the non-uniform-grid reconstruction and smoothness indicators in the differences $\Delta\bar u_j$ reduces the terms from $r$ to $r-1$ for the candidate value and from $r(r+1)/2$ to $(r-1)r/2$ for $\beta_k$, with all coefficients precomputed; $\beta_k$ is the Jiang–Shu form scaled by the local cell width (§4.2.2). **Derived**
10. Ghost-cell immersed boundaries: ghost points are solid cells within three cells of fluid; the image point is $x_{\mathrm{gp}}+2d_{\mathrm{IB}}(x_{\mathrm{gp}})$, with $d_{\mathrm{IB}}$ the vector to the closest boundary point; values are interpolated with inverse-distance-squared weights from the four surrounding fluid cells; the cost is negligible relative to the flow solve (§4.1.1, Algorithms 1–3). **Stated**; analytic and STL level sets agree for Mach 2 helium flow over a sphere at $\mathrm{Re}=6.5\times10^5$ (Fig. 2). **Shown**
11. The phase-change model matches the evaporation-front speeds of Simões-Moreira & Shepherd for n-dodecane at 180–300 °C, better at higher temperature (§4.1.3, Fig. 3). **Shown**
12. Euler–Lagrange single bubble against the Keller–Miksis solution: RMSE 2.76%; Euler–Euler against Euler–Lagrange for a bubble screen: RMSE below 2.1% (§4.1.5, Figs. 5–6). **Shown**
13. The reactive shock tube (12 cm, 400 cells, San Diego mechanism) agrees with Martínez-Ferrer et al. "sufficient for validation" (§4.1.7, Fig. 8); reacting advection shows the expected orders (Fig. 7). **Shown**
14. The six-equation model with surface tension is conservative except for the pressure-relaxation terms and satisfies the second law (**Stated**); a Laplace pressure jump is resolved on $128\times128$ with a time-stable residual (§4.1.8, Fig. 9) (**Shown**).
15. Brio–Wu with HLLD matches Miyoshi & Kusano; the smooth Alfvén wave of Tóth converges at the expected rate with WENO3 and WENO5; the RMHD shock tube matches Mignone & Bodo with WENO3 in place of their second-order scheme (§4.1.9–4.1.10, §4.2.5, Figs. 10–11). **Shown** The MHD description names no divergence-control method.
16. Plain HLLC loses accuracy on the Gresho vortex at reference Mach numbers $10^{-1}$ to $10^{-4}$ ($t/t_r=1$); the Thornber et al. and Chen et al. corrections, both blended by $z_{\mathrm M}=\min\big(\max(\lvert v_1^-\rvert/c^-,\lvert v_1^+\rvert/c^+),1\big)$, keep the flow "to visual accuracy for all tested Mach numbers" (§4.2.4, Fig. 14). **Shown**
17. Strang splitting with an adaptive embedded RK runs a bubble collapse at $p_\infty/p_b=1427$ with $\Delta t=0.8$ µs, where the unsplit scheme fails (negative radius) and needs $\Delta t=0.008$ µs (§4.2.3, Fig. 13). **Shown**
18. OpenACC outperforms OpenMP offload on NVIDIA and AMD; OpenMP is used where unified shared memory is needed on AMD; GNU 14 and Flang 18 are insufficient for MFC (§4.3.1, Table 1). **Stated**
19. Packing arrays for coalesced access before the WENO and Riemann kernels gives a "ten-fold speedup"; hipBLAS transposes are about 7× faster than collapsed OpenACC loops (§4.3.1). **Stated**
20. Grind time (ns per grid point, equation and right-hand-side evaluation; 3D inviscid five-equation, 8 equations, WENO5 + HLLC): GH200 0.32, H100 SXM5 0.38, H100 PCIe 0.45, B200 0.46, MI250X 0.55, MI300A 0.57, A100 0.62, V100 0.99; the best CPU (AMD EPYC 9965, 192 cores) 1.2 and the slowest (A64FX) 63 (Table 2). **Shown**
21. Roofline: the WENO and Riemann kernels reach 37% and 14% of peak on A100, 24% and 5% on GH200, 22% and 3% on MI250X; they take about half the wall time on NVIDIA and a third on AMD (§4.3.2, Figs. 15–16). **Shown**
22. Weak scaling: 97% from 128 to 13,824 V100 (Summit), 95% from 128 to 65,536 MI250X GCDs (Frontier), 99% from 192 to 196,608 MI300A XCDs (El Capitan) (Fig. 17). **Shown**
23. Strong scaling at 8× and 16×: Summit 79% and 51% (8M cells per device) or 81% and 77% (32M) without GPU-aware MPI, 84% and 60% with it; Frontier 96% and 92% with it (§4.3.3, Fig. 18). **Shown**
24. Compile-time case optimization gives about 2× on CPUs and 10× on GPUs; compile-time bounds in the generated chemistry kernels give about 5× (§4.3.6–4.3.7). **Stated**
25. Above $10^4$ processes, shared-file MPI-IO slows down, and MFC writes one file per process in waves of 128 (§4.3.4). **Stated**
26. Demonstrations: a 75-bubble shock–bubble-cloud collapse at about $2\times10^9$ points on 1024 MI250X GCDs in about 30 min; a shock–helium-bubble run at more than $8\times10^9$ points on 144 H200 in 16 h; a Taylor–Green vortex at $\mathrm{Re}=1600$, $M=0.1$, $1600^3$, in 28 h; three Mach 1.5 jets on $600\times400\times400$ (§5); validation is by prior work (§5.5). **Shown** (capability only)

# Printed slips

- Eq. (5) (checked on the page image, p. 3): $K_{\mathrm{Ka}}=(\rho_2c_2^2+\rho_1c_1^2)/(\rho_1c_1^2/\phi_1+\rho_2c_2^2/\phi_2)$, one positive coefficient in $\partial_t\phi_k+v\cdot\nabla\phi_k=K_{\mathrm{Ka}}\nabla\cdot v$ for both components. [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) print the numerator as the difference $\rho_2c_2^2-\rho_1c_1^2$ for $\phi_1$. *(Compiler check, not in the sources: summing the two volume-fraction equations with $\phi_1+\phi_2=1$ gives $0=2K_{\mathrm{Ka}}\nabla\cdot v$, so one positive coefficient for both components contradicts the mixture rule.)*
- §4.3.2, Table 2 case: "8 PDEs) and 8M grid points (158-cubed 3D uniform grid)". *(Compiler check, not in the sources: $158^3=3{,}944{,}312\approx3.9$M; $200^3=8$M.)*
- Six-equation model, phase-2 energy equation (§2.1.2, checked on p. 3, and §4.1.8): "$\nabla\cdot(\alpha_1\rho_2e_2u)$", where the phase-1 equation has $\alpha_1\rho_1e_1u$ and the symmetric flux is $\alpha_2\rho_2e_2u$. The same equations print "$\alpha_1p_1\cdot\nabla u$" (a scalar dotted with a tensor) and the interfacial pressure as $p_I$ against $P_I$ in Eq. (7). The relaxation
  sources are printed $-\mu p_I(p_2-p_1)$ (phase 1) and $-\mu p_I(p_1-p_2)$
  (phase 2), with $\partial_t\phi_1+v\cdot\nabla\phi_1=\mu(p_1-p_2)$; they cancel
  in the sum. [Wakimura et al. (2024)](/sources/wakimura-2024.md) print
  $-\mu p_I(p_1-p_2)$ for phase 1 ([six-equation model](/definitions/six-equation-model.md)).
  *(Compiler check, not in the sources: the work of phase 1 on expansion is
  $p_I\,\partial_t\phi_1$, which requires $-\mu p_I(p_1-p_2)$ in the phase-1
  equation, so both printed signs are reversed.)*
- Eq. (8): "$c_i=\sqrt{\gamma(p_i+\pi_{\infty,i})/\rho_i}$" without the subscript on $\gamma$ (Eq. (6) has $\gamma_i$). Eq. (3): "$e(\rho_1 p)$" without a comma.
- §4.1.3 (checked on p. 5): the pT-relaxation function prints "$\sum_{j=1}^N\alpha_j\rho_ie_{*,i}$", index $i$ inside a sum over $j$; the section defines pT and pTg relaxation but the test "focus[es] on the pTμ-relaxation"; "chocked flow" for choked.
- §4.2.3: the system is printed $\partial_tq=\nabla\cdot F(q)+s(q)$ while the transport sub-step is $\partial_tq^{**}=-\nabla\cdot F(q^{**})$.
- §4.2.1: the incoming and outgoing parts $\lambda_j\mp n_x\lvert\lambda_j\rvert$ carry no factor $\tfrac12$, so they sum to $2\lambda_j$.
- Regression tests: "over 300" (Abstract, §7) against "over 500" (§4, §4.3.5).
- §3.2.2: "Identical calculations are performed in the $x$- and $z$-directions" after the $x$ flux ($y$ and $z$ are meant). §4.3.3: "compares weak scaling with and without GPU-aware MPI" for the strong-scaling Fig. 18, whose caption attributes the base-case sizes to panel (b) where the text has (a).
- §4.1.6: "$J$ is the determinant of $b$" for $b=FF^\top$. Fig. 20 caption: "The initial droplet has 640 grid cells" for a helium bubble.
- References: [29] and [48] are the same work (Menikoff & Plohr 1989), as are [37] and [83] (Strang 1968); [101] prints "berkley" in its URL and [21] "(????)".

# Notation map

| Wilfong et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$, $q_{i,j,k}$ | $u$, $\bar u_{i,j,k}$ | **collision** of $q$ with the weight exponent |
| $q^{(L)}_{i+1/2}$, $q^{(R)}_{i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $F^{(x)}$, $F^{(y)}$, $F^{(z)}$ | $f^{(1)}$, $f^{(2)}$, $f^{(3)}$ | |
| $u$ (velocity) | $v$ | |
| $\alpha_i$, $\rho_i$, $\pi_{\infty,i}$, $\gamma_i$ | $\phi_k$, $\rho_k$, $p_{\infty,k}$, $\gamma_k$ | **collision** of $\alpha$ with $\alpha_k$ |
| $K$ (Kapila) | $K_{\mathrm{Ka}}$ (local) | **collision** with the TENO stencil size $K$ |
| $k$, order $2k-1$; stencil index $r$ | $r$, order $2r-1$; $k$ | **index swap** |
| $K$ (TENO order) | design order (stated in words) | registry $K$ counts points |
| $d_r$, $\beta_r$, $\omega^{(Z)}_r$, $\omega^{(T)}_r$ | $d_k$, $\beta_k$, $\omega_k$ | |
| $\tau=\lvert\beta_0-\beta_{k-1}\rvert$ | $\tau$ ($\tau_5$ at fifth order) | |
| $\gamma_r$, $\chi_r$, $\delta_r$, $C_T$ | $\gamma_k$, $\chi_k$, $\delta_k$, $C_T$ | source $\gamma_r$ carries a factor $d_r$ and no constant $C$ |
| $f_j$, $\Delta f_j$ | $\bar u_j$, $\Delta\bar u_j$ (local) | |
| $S_L$, $S_R$, $S_*$, $S_M$ | $s^-$, $s^+$, $s_*$ (local) | |
| $z$ (low-Mach factor) | $z_{\mathrm M}$ (local) | **collision** with the phasic impedance $z_i$ of the source |
| $p_d$ | $p_{\mathrm d}$ (local) | |
| $\varphi$ (level-set vector) | $d_{\mathrm{IB}}$ (local) | **collision** with $\phi_k$ and $\varphi_i$ |
| $B$, $c_f$, $v_A$; $\Gamma$ | $B$, fast and Alfvén speeds; $W$ | Lorentz factor |
| $\mu$ | pressure-relaxation rate (local) | also the viscosity in the bubble model |

# Reference list

The paper prints 107 references, numbered [1]–[107]. The list is merged complete
into the [bibliography](/bibliography.md), with `citedby` including `wilfong-2026`.
Ref. [1] is the ingested [Bryngelson et al. (2021)](/sources/bryngelson-2021.md).
Two printed duplicates, [29] = [48] (Menikoff & Plohr 1989) and [37] = [83] (Strang
1968), are recorded once each in the bibliography. Ref. [88] (Chen et al., the
anti-dissipation pressure correction, J. Comput. Phys. 456:111027) would take a key
already used by a different work and is keyed apart by venue. Corporate and web
items are keyed by the printed corporate name; [100] and [104] are arXiv preprints;
[32] (Toro 1997) is printed as a chapter without book title; [49] and [65] print no
page. No item is unparseable.

# Pages created or updated

Chunk 10 (2026-10-23), cited further in chunk 11 (2026-10-24). This source is cited on:

* [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md)
* [Bubble collapse near a wall](/benchmarks/bubble-collapse-near-wall.md)
* [Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
* [Density-wave advection](/benchmarks/density-wave-advection.md)
* [Five- and six-equation diffuse-interface models](/definitions/five-equation-model.md)
* [Gresho vortex](/benchmarks/gresho-vortex.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Immersed-boundary and cut-cell methods](/methods/immersed-boundary-method.md)
* [Material-interface advection tests](/benchmarks/material-interface-advection.md)
* [MFC](/software/mfc.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [Oscillating droplet](/benchmarks/oscillating-droplet.md)
* [Semi-implicit all-Mach schemes](/methods/semi-implicit-all-mach-scheme.md)
* [Shock-induced combustion and detonation](/benchmarks/shock-induced-combustion.md)
* [Shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
* [Six-equation two-phase model](/definitions/six-equation-model.md)
* [Stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
