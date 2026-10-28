---
type: Source
title: "Yeung et al. (2025b) — GPU-enabled extreme-scale turbulence simulations: Fourier pseudo-spectral algorithms at the exascale using OpenMP offloading"
description: "Describes GESTS, a Fortran OpenMP-offload Fourier pseudo-spectral DNS code for forced isotropic turbulence on the Frontier exascale machine, with slab and pencil decompositions and GPU-aware all-to-all transposes, and reports its performance up to 32768³ grid points, dominated by MPI communication."
resource: "doi:10.1016/j.cpc.2024.109364"
source_kind: paper
authors: [Yeung P.K., Ravikumar K., Nichols S., Uma-Vaideswaran R.]
year: 2025
venue: "Comput. Phys. Commun. 306:109364"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Computer_Physics_Communications_Yeung_GPU-enabled_extreme-scale_turbulence_simulations_Fourier_pse.pdf"
tags: [dns, isotropic-turbulence, gpu, software]
timestamp: 2026-10-28T17:05:00Z
---

# Summary

Yeung et al. (2025b) describe GESTS, a Fortran 90/95 suite of Fourier
pseudo-spectral codes for
[direct numerical simulation](/definitions/direct-numerical-simulation.md)
of incompressible, constant-density, forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) in a
$2\pi$-periodic cube, written for Frontier, the first exascale computer
(AMD MI250X GPUs, Slingshot-11 dragonfly network). The numerics are
Rogallo's (1981) algorithm and are not new: five stored nonlinear terms
through a modified pressure, an exact integrating factor for the viscous
term, second-order Runge–Kutta predictor–corrector stepping, and
de-aliasing by phase shifting plus truncation beyond
$k_{\max}=\sqrt2N_x/3$. The contribution is the GPU implementation and its
performance. Frontier's device and host memories are equal, so the whole
problem stays in GPU memory inside a single OpenMP `TARGET DATA` region;
packing loops are offloaded, the 1D FFTs call rocFFT through HIPFORT, the
`MPI_ALLTOALL` transposes run GPU-aware from device pointers, and the CPU
works only for I/O. The code has slab (1D) and pencil (2D) decompositions,
strided complex-to-complex transforms, a per-GCD memory model, Fourier-space
checkpoints with two velocity components, and a multi-variable all-to-all
that sends $Q_{\mathrm v}$ variables per call.

The largest run is $N_x^3=32\,768^3$ (35 trillion points) on 4096 nodes in
12.07 s per step, a figure of merit 6.6 times the Summit $18\,432^3$
record. Weak scaling is near 90% or better; strong scaling is near 100% at
$8192^3$ and $16\,384^3$ but 70–80% at $32\,768^3$ between 4096 and 8192
nodes. The GPU code is about 10 times faster than a CPU-only pencil code.
MPI all-to-all dominates the cost, and an all-to-all test code measures the
effective bandwidths of the row and column communicators, which degrade at
the largest scales with small peer-to-peer messages and dragonfly
inter-group limits. The code is the one behind the exascale DNS of
[Yeung et al. (2025)](/sources/yeung-2025.md) (§6 announces that work). The
paper holds no turbulence modelling and no flow statistics (bundle fit:
peripheral, HPC of a DNS code); the algorithms are recorded inline on the
DNS page.

# Version read

Version of record (Elsevier, open access CC BY-NC-ND; received 30 April
2024, accepted 2 September 2024, online 5 September 2024), 19 pages, all
read; page 1 carries a DOE public-access footnote, no preprint stamp. Page 1
matches the metadata (title, four authors, DOI). This is a different work
from the ingested [yeung-2025](/sources/yeung-2025.md) (J. Fluid Mech.); the
bibliography already held it as the cited entry `yeung-2025-b`. Equation,
table and section numbers are those of this version.

# Key claims

Page-local symbols: $N_x$ grid points per direction (the source's $N$);
$N_{\mathrm{MPI}}$ the number of MPI processes (the source's $P$),
$P_{\mathrm r}\times P_{\mathrm c}=N_{\mathrm{MPI}}$ the pencil process
grid; $Q_{\mathrm v}$ the number of variables per all-to-all call (the
source's $Q$); $\chi_{\mathrm{FOM}}\propto N_x^3/t_{\mathrm{step}}$ the
figure of merit (the source's $\chi$, $T$); $u_{j,\boldsymbol k}$ Fourier
coefficients (the source's hats); $P^\perp_{jl}(\boldsymbol k)=\delta_{jl}-k_jk_l/k^2$
the projection tensor; WS1, WS2, SS1, SS2 weak and strong scaling
efficiencies as defined in §4.1.

1. A Fourier pseudo-spectral DNS of 3D turbulence was run at $32\,768^3$ (35 trillion grid points) on Frontier, 5.6 times as many points as the $18\,432^3$ record [14] and 8 times the $16\,384^3$ record [12] (Abstract; §1). **Shown**
2. Orthogonal Fourier representations are, "for a given count of grid points, demonstrably more accurate than finite difference methods of any order" [18] (§1). **Stated**
3. In large pseudo-spectral DNS the cost of 3D FFTs, and of the simulation itself, is "dominated by data movement, rather than purely computational number crunching" (§1). **Stated**
4. Frontier's GPU and CPU memories are equal ("4x the device memory of Summit"), so the whole problem stays in GPU memory and host–device copies are needed only for I/O, unlike the batched asynchronous algorithm used on Summit [6] (§1, §2.2). **Stated**
5. With 99% of each node's flops on the GPUs [16], leaving the CPU idle wastes little; overlapping CPU and GPU work "would lead to only very minimal (if any) benefit" on Frontier (§2.2). **Stated**
6. For complex-to-complex FFTs of three variables, non-strided library calls are faster than strided ones, but including packing and unpacking the strided transforms are cheaper overall at $8192^3$ and above ($8192^3$: 0.202 s strided against 0.259 s; $32\,768^3$: 0.373 s against 0.947 s), so strided transforms are used in $y$ and $z$ (§2.1, Table 1). **Shown**
7. Memory per GCD is about $(8+2Q_{\mathrm v}+0.5)\times(N_x^3/2N_{\mathrm{MPI}})\times8/1024^3$ GiB; for $Q_{\mathrm v}=1$, $N_x=2048$, $N_{\mathrm{MPI}}=8$ this is 42 GiB, so $2048^3$ is the largest problem on one node and $32\,768^3$ needs at least 4096 nodes (§3.2, Eq. 9). **Derived** ("verified … by our actual measurements")
8. Raising $Q_{\mathrm v}$ adds about $8(Q_{\mathrm v}-1)(N_x^3/N_{\mathrm{MPI}})/1024^3$ GiB per GCD (§4.4). **Derived**
9. A Fourier-space checkpoint stores two velocity components and recovers the third from continuity (Eq. 12); it is close to $8N_x^3$ bytes, 256 TiB for $N_x=32\,768$ (§3.2). **Derived**
10. Slab code (Table 2): $32\,768^3$ on 4096 nodes (32 768 ranks) takes 13.07 s per step (April 2023) or 12.07 s (April 2024); the 2023 breakdown is FFT 3.423, packing and unpacking 0.276, MPI 8.621, other 0.747 s; WS1 is 96.6% (2023) and 104.6% (2024) relative to $4096^3$ on 8 nodes (§4.2, Table 2). **Shown**
11. Weak scaling is low from $2048^3$ on 1 node to $4096^3$ on 8 nodes, because intra-node communication is much faster than inter-node, and very good from 8 nodes upward (§4.2, Table 2; §4.3, Table 3). **Shown**
12. FFT cost per process scales as $(N_x^3/N_{\mathrm{MPI}})\log_2N_x$ up to $8192^3$; the degradation at $16\,384^3$ and above is attributed to "an existing artifact of the AMD ROCm library affecting large transform lengths" (§4.2). **Shown** (attribution **Stated**)
13. Figure of merit $\chi_{\mathrm{FOM}}\propto N_x^3/t_{\mathrm{step}}$, the $\log_2N_x$ factor omitted because communication dominates: $\approx2.91\times10^{12}$ on Frontier ($N_x=32\,768$, 12.07 s, 4096 nodes), 6.6 times the Summit value $4.40\times10^{11}$ ($N_x=18\,432$, 14.24 s, 3072 nodes [6]), more than the 5.9 times reported in [16] (§4.1). **Shown**
14. Pencil code (Table 3): row-communicator MPI time falls by about 27% from $P_{\mathrm r}=8$ to 4 and by about 51% from 4 to 2, and vanishes at $P_{\mathrm r}=1$; with $P_{\mathrm r}=1$ the pencil code is slightly faster than the slab code at $4096^3$ and $8192^3$ and within 2% at $16\,384^3$ (§4.3). **Shown**
15. Pencil weak scaling (workload $\propto N_x^3\log_2N_x$) is close to 90% for $32\,768^3$ on 4096 nodes relative to $4096^3$ on 8 nodes, and above 95% for each doubling of $N_x$ beyond 4096 (§4.3, Table 3). **Shown**
16. The column-communicator message size per variable is $4N_x^3/(N_{\mathrm{MPI}}P_{\mathrm c})$ bytes in single precision: 0.125 MiB for Case 18 against 0.5 MiB for Case 16 of Table 3; there are 14 column all-to-all calls per step (3 inverse plus 4 forward, at each of 2 Runge–Kutta substeps) when $Q_{\mathrm v}=1$ (§4.3). **Derived**/**Shown**
17. The GPU code is about 20 times faster than a pure-MPI CPU pencil code (FFTW, 64 cores per node) at $2048^3$ on one node and about 10 times faster at larger sizes; at $8192^3$ the component speedups are printed as "roughly 13x, 33x, 3x, and 65x" for FFT, packing and unpacking, MPI and other (§4.3, Table 4). **Shown** (see Printed slips)
18. Strong scaling at $8192^3$ (Table 5) is above 93% at each doubling from 64 to 512 nodes for all $P_{\mathrm r}\in\{8,4,2,1\}$, and three of the four (all but $P_{\mathrm r}=2$) reach about 100% or better over an 8-fold increase, although communication is about 75% of the execution time (§4.4). **Shown**
19. At $16\,384^3$ (Table 6) strong scaling is high from 512 to 1024 nodes; the step to 2048 nodes shows large step-to-step variability, which $Q_{\mathrm v}=4$ makes "nearly ideal"; the fastest configuration is $1\times16\,384$ (Case 12, 2.90 s), the stable production choice $4\times4096$ (Case 6) (§4.4). **Shown**
20. At $32\,768^3$ from 4096 to 8192 nodes (Table 7) strong scaling is 70–80% (79.6%, 71.8%, 74.9% for $P_{\mathrm r}=8,4,2$), limited by the column communicator; $Q_{\mathrm v}=4$ improves the mean time only modestly but cuts the step-to-step variation from 3–5 s to below 0.1 s (§4.4). **Shown**
21. Slab strong scaling is 98% over a 4-fold node increase at $8192^3$ (10.72, 5.49, 2.73 s on 64, 128, 256 nodes) and at $16\,384^3$ (11.30, 5.57, 2.89 s on 512, 1024, 2048 nodes) (§4.4). **Shown**
22. "Unlike common experiences in large-scale computing", strong scaling improves from $2048^3$ to $16\,384^3$ before falling off at $32\,768^3$ (§4.4, Fig. 7). **Shown**
23. In GPU codes communication can become "even more dominant than for CPU codes", because the flop rate rises by a large factor while communication improves modestly (§4.4, §6). **Stated**
24. The effective unidirectional all-to-all bandwidth per rank is $BW=(P2P\times R)/t_{\mathrm{MPI}}$, self-communication included (Eq. 13); slab GPU bandwidth is 32.90 GB/s on 1 node (65.8% of an expected 50 GB/s), 8.71 GB/s on 8 nodes and 5.58 GB/s on 4096 nodes; CPU MPI with host–device copies costs 13 times GPU MPI on 1 node, 3.65 times on 512 nodes and "2.4x" on 4096 nodes (§5.1, Table 10). **Shown** (see Printed slips)
25. With $P_{\mathrm r}=2$ the row communicator (GCD to GCD on one GPU) reaches about 93 GB/s effective, about 46.5 GB/s of real cross-GCD traffic, 93% of the 50 GB/s single-link DMA limit of [44] and [16] and over 30 times CPU MPI; 16 row all-to-all calls per step at 0.046 s reproduce the 0.74 s of the DNS tables (§5.2, Table 11). **Shown**
26. Column-communicator GPU bandwidth is 46.93 GB/s on 1 node (93.9% of 50 GB/s), then 7.97 GB/s on 8 nodes down to 6.09 GB/s on 4096 nodes; the peer-to-peer message size falls by a factor 8 per doubling of $N_x$ (§5.2, Table 12). **Shown**
27. On 2048 and 8192 nodes the column communicator with $P_{\mathrm r}=4$ is faster than with $P_{\mathrm r}=8$ despite smaller messages, "the first known demonstration of this behavior", a dependence on the decomposition beyond message size and dragonfly topology (§5.2, Table 13). **Shown** (novelty **Stated**)
28. All multi-node effective bandwidths exceed, or lie in the upper half of, the 1.5–4 GB/s per rank inter-group range derived from [16] (§5.1–5.2). **Shown**
29. The pencil code has been used for production runs on intermittency at Taylor-scale Reynolds number close to 2500 at up to $32\,768^3$, to be reported separately, and underlies particle-tracking and passive-scalar codes (§6). **Stated**

The equations in registry notation (§3.1, Eqs. 4–8): $\partial_ju_j=0$,
$\partial_tu_i+u_j\partial_ju_i=-\partial_ip+\nu\partial_j\partial_ju_i+f_i$
with $p$ kinematic and $f_i$ a large-scale solenoidal forcing [39, 40]; in
Fourier space
$(\partial_t+\nu k^2)u_{j,\boldsymbol k}=-\mathrm ik_mP^\perp_{jl}(\boldsymbol k)(u_lu_m)_{\boldsymbol k}$.
The time step follows a Courant number
$\Delta t\,[|u|/\Delta x+|v|/\Delta y+|w|/\Delta z]_{\max}$ held below 1.
Dissipation $\varepsilon=2\nu s_{ij}s_{ij}$, the enstrophy density
$\omega_i\omega_i$ (no factor $\tfrac12$) and the pressure from
$-k^2p_{\boldsymbol k}=k_ik_j(u_iu_j)_{\boldsymbol k}$ are computed on the
fly (Eqs. 10–11). Arithmetic is single precision; the Fourier transforms
are printed without normalization.

# Printed slips

- **Table 2, WS2 of the April-2024 slab row:** printed 98.9% for $32\,768^3$ at 12.07 s. *(Compiler check, not in the sources: with the paper's definition, workload $\propto N_x^3\log_2N_x$ relative to $16\,384^3$ at 11.53 s, $11.53\times(15/14)/12.07=102.4\%$; the 2023 WS2, $11.53\times(15/14)/13.07=94.5\%$, matches its printed 94.5.)*
- **§4.3:** "roughly 13x, 33x, 3x, and 65x" for FFT, packing and unpacking, MPI and other at $8192^3$. *(Compiler check, not in the sources: from Table 3 Case 10 and Table 4 Case 6 the packing-and-unpacking ratio is $33.3/0.40=83$; the other three, $20.9/1.56=13.4$, $22.6/8.14=2.8$, $28.1/0.43=65$, agree with the text.)*
- **§5.1:** "2.4x … for the largest problem size on 4096 nodes". *(Compiler check, not in the sources: Table 10 gives $2.006/0.771=2.60$; the other two quoted ratios, $2.152/0.590=3.65$ and $1.706/0.131=13.0$, agree.)*
- **Table 4, Case 6:** $8192^3$ on "8" nodes with $P_{\mathrm r}=P_{\mathrm c}=64$. *(Compiler check, not in the sources: $64\times64=4096$ ranks at the 64 cores per node stated in §4.3 need 64 nodes, and Eq. 9 also requires at least 64 nodes for $8192^3$.)*
- **Acronym:** GESTS is "GPUs for Extreme Scale Turbulence Simulations" in the abstract and "GPU-enabled Extreme Scale Turbulence Simulations" in §1.
- **§3.1:** the solenoidal condition is printed "$\mathbf u\cdot\hat{\mathbf k}=0$", the hat on the wavevector, while the sentence describes the Fourier-space velocity orthogonal to the wavevector.
- **Call counts:** §5.2 counts 16 row-communicator all-to-all calls per step with $Q_{\mathrm v}=1$, §4.3 counts 14 column calls (3 inverse plus 4 forward variables, times 2 substeps); the text does not explain the difference.
- **§4.3** cites "column-communicator timings seen with $P_r=2$ in Sec. 4.2", while the pencil tables are in §4.3. Typos: "Sze (MiB)" in the Table 13 header, "Analyis" in the §5 title, "perpsective" in ref. [46].
- **References:** [38] prints "D.A. Davidson", [46] "P.A. Davidson" (editor); [29] prints the first author "H.W. Muer" and a co-author "M. Meuer".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $N$, $N^3$ | $N_x$, $N_x^3$ | grid points per direction; **collision** with the polynomial degree $N$ |
| $\hat f(\boldsymbol k)$, $\hat u_j$ | $f_{\boldsymbol k}$, $u_{j,\boldsymbol k}$ | Fourier coefficients; the registry hat is the test filter |
| $\mathbf u$, $u_j$, $p$, $\mathbf f$ | $\boldsymbol u$, $u_j$, $p$ (kinematic $p/\rho$), $f_i$ | zero-mean velocity; $p$ the pressure fluctuation |
| $P_{jl}(\mathbf k)$ | $P^\perp_{jl}(\boldsymbol k)$ (page-local) | projection tensor; **collision** with $P$ (processes) and $P_k$ |
| $k_{max}=\sqrt2N/3$ | $k_{\max}=\sqrt2N_x/3$ | truncation wavenumber |
| $\epsilon=2\nu s_{ij}s_{ij}$ | $\varepsilon$ | |
| $\Omega=\omega_i\omega_i$ | $\omega_i\omega_i$ | enstrophy density without $\tfrac12$; **collision** with $\Omega_{ij}$ |
| $s_{ij}$, $\boldsymbol\omega$ | $S_{ij}$ (of the fluctuating field), $\omega_i$ | zero mean velocity |
| $C$ | Courant number | not a model constant |
| $R_\lambda$ | $Re_\lambda$ | §6 only |
| $P$ | $N_{\mathrm{MPI}}$ (page-local) | MPI processes, 8 per Frontier node |
| $P_r$, $P_c$ | $P_{\mathrm r}$, $P_{\mathrm c}$ (page-local) | pencil process grid |
| $Q$ | $Q_{\mathrm v}$ (page-local) | variables per all-to-all; **collision** with the $Q$-criterion |
| $\chi$, $T$ | $\chi_{\mathrm{FOM}}$, $t_{\mathrm{step}}$ (page-local) | **collision** with the SA ratio $\chi$ and with temperature $T$ |
| $BW$, $P2P$, $R$, $t_{MPI}$ | $BW$, $P2P$, $R$, $t_{\mathrm{MPI}}$ (page-local) | Eq. 13; $R$ not a Reynolds stress |
| $M$ | (page-local) | number of checkpoint files; not a Mach number |
| WS1, WS2, SS1, SS2 | (page-local) | scaling efficiencies of §4.1 |

# Reference list

50 printed references, numbered style. The list is merged complete into the
[bibliography](/bibliography.md) with `citedby` this slug. Ref. [15] prints
a book-level DOI and pages but no book title; the undated Top500 item [29]
is keyed with the citing paper's year and the printed "Muer" spelling; [44]
carries a URL; [50] prints "120 (2023) 34" with no article number. Refs.
[36] and [37] (Chapman, Parts I and II, 2021) are keyed in printed order.
The cited works under the keys `zhou-2021`, `lee-2013`, `chatterjee-2018`,
`turner-2022`, `eswaran-1988`, `donzis-2010` and `tian-2023` are different
works from the bibliography entries already holding those keys and are keyed `zhou-2021-g`, `lee-2013-b`, `chatterjee-2018-b`, `turner-2022-b`, `eswaran-1988-b`, `donzis-2010-b` and `tian-2023-d`. `ravikumar-2019` and `yeung-2020` were already cited
by [yeung-2025](/sources/yeung-2025.md). No item is unparseable.

# Pages created or updated

Chunk 14 (2026-10-28). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md)
