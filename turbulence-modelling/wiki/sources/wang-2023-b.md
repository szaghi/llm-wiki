---
type: Source
title: "Wang et al. (2023b) — Multiple-GPU accelerated high-order gas-kinetic scheme for direct numerical simulation of compressible turbulence"
description: "Ports a WENO-based high-order gas-kinetic scheme to single and multiple GPUs with CUDA and CUDA-aware MPI, reports speed-ups and strong scaling on the Taylor–Green vortex, a compressible Taylor–Green Mach sweep, and a single- against double-precision comparison in incompressible and compressible channel DNS."
resource: "doi:10.1016/j.jcp.2022.111899"
source_kind: paper
authors: [Wang Y., Cao G., Pan L.]
year: 2023
venue: "J. Comput. Phys. 476:111899"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2023_Crossref_Journal_of_Computational_Physics_Wang_Multiple-GPU_accelerated_high-order_gas-kinetic_scheme_for_d.pdf"
tags: [gpu, gas-kinetic, dns, compressible]
timestamp: 2026-10-27T15:52:00Z
---

# Summary

Wang et al. (2023b) port the authors' [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
(HGKS) to Nvidia GPUs. HGKS is a finite-volume Navier–Stokes solver whose
interface flux comes from the time-dependent solution of the BGK equation,
with a two-stage fourth-order time discretization and fifth-order
[WENO](/methods/weno-scheme.md) reconstruction applied dimension by
dimension. The single-GPU code uses CUDA kernels with one thread per cell;
the multi-GPU code uses CUDA-aware MPI with a one-dimensional (slab)
decomposition in $x$. It is an implementation and performance paper: no new
turbulence model and no new discretization. HGKS is used for
[DNS](/definitions/direct-numerical-simulation.md), without an SGS model.
The paper is peripheral to closure modelling and is cited here for GPU
performance and arithmetic precision in scale-resolving simulation.

On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at
$Re=1600$, $M=0.1$, one GPU runs about 7 (TITAN RTX) and 16 (Tesla V100)
times faster than an 8-core desktop CPU in double precision; the V100 has
about 15 times the double-precision peak of the TITAN RTX but is only about
twice as fast, which the authors attribute to memory bandwidth. Multi-GPU
strong scaling degrades beyond 8 GPUs, when communication leaves the node.
A compressible Taylor–Green sweep ($M=0.25$–$1.0$, $256^3$) shows
non-monotone kinetic energy for $M\ge0.75$. On the
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
(nearly incompressible $Re_\tau=395$ and compressible bulk $Re=3000$,
$M=0.8$) single precision halves memory and runs 1.7–2.7 times faster;
statistics averaged over 200 $\delta/U_c$ agree between precisions, while
instantaneous rms profiles differ. The authors conclude that single
precision "may not be safe" for DNS of time-evolving turbulence and may be
used for LES and RANS. The compressible mean velocity is checked through the
van Driest [compressible velocity transformation](/definitions/compressible-velocity-transformation.md)
against the [law of the wall](/definitions/law-of-the-wall.md). The
introduction cites GPU DNS of
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md),
and an HGKS [implicit LES](/definitions/implicit-les.md) (ref. [39]) in
passing.

# Version read

arXiv preprint 2207.01173v1 [math.NA], 4 July 2022 ("Preprint submitted to
Elsevier, July 5, 2022"), 27 pages, all read; Fig. 4, a flow chart rendered
with a broken font, read visually. The metadata above are those of the
published version (J. Comput. Phys. 476:111899, 2023), whose content was not
seen. Title and authors on page 1 match the Crossref record. Section,
equation, table and figure numbers on this page are those of arXiv v1.

# Key claims

1. HGKS (BGK-based flux, two-stage fourth-order time stepping, fifth-order WENO with dimension-by-dimension reconstruction) is implemented on one GPU with CUDA, one thread per cell, grid `dim3(Nz, Nx/blockx, 1)` and block `dim3(blockx, Ny, 1)` (§3.1, Alg. 1, Fig. 2). **Stated**
2. Multi-GPU HGKS uses MPI + CUDA with CUDA-aware MPI; slab decomposition in $x$ is used for GPUs because it "reduces the frequency of GPU-GPU communications and improves performances", whereas the CPU code with thousands of cores uses pencil decomposition (§3.2, Fig. 3). **Stated**
3. The halo exchange orders blocking `MPI_SEND`/`MPI_RECV` calls by even and odd process index; periodic boundaries add an exchange between the first and last processes, and the first process handles I/O (Alg. 2, Fig. 4). **Stated**
4. Single-GPU speed-up over an 8-core i7-9700 OpenMP code (double precision, Taylor–Green vortex, 20 convective times): $64^3$: TITAN RTX 6.0, V100 16.1; $128^3$: 7.6, 16.0; $256^3$: 7.4, 15.4 (Table 3), summarized as "7x" and "16x". **Shown**
5. Although the V100 is "approximately 15 times faster than the TITAN RTX in FP64 precision computation ability", it "only performs 2 times faster", indicating that "the memory bandwidth is the bottleneck for current memory-intensive simulations" (§4.1, Tables 2–3). **Shown** (timing) / **Stated** (attribution, not profiled)
6. The largest mesh on one 24 GB TITAN RTX is $256^3$ cells (§4.1). **Stated**
7. For $256^3$, one V100 (11.697 h) is "comparable with the MPI code with supercomputer using approximately 300 Intel Xeon E5-2692 cores" (Tables 4–5; 256 cores take 13.5 h). **Shown**
8. For $512^3$, 1024 Xeon cores (66 h) take "approximately 3 times longer" than 8 V100s (22.252 h); the authors infer that 8 V100s equal about 3000 CPU cores, in agreement with FluTAS [26] (§4.1, Tables 4–5). **Shown** (ratio) / **Stated** (the 3000-core figure is inferred, not measured)
9. Multi-GPU times: $256^3$ on 1/2/4/8 GPUs 11.697/6.201/3.223/1.987 h; $512^3$ on 8/12/16 GPUs 22.252/19.055/13.466 h; the communication time grows from 0.079 h (2 GPUs) to 0.439 h (8 GPUs) at $256^3$ and from 0.869 to 1.983 h at $512^3$ (Table 5, Fig. 6). **Shown**
10. Scaling degrades beyond 8 GPUs because inter-node communication goes over RoCE rather than NVLink; InfiniBand is to be tested (§4.1, Figs. 5–6). **Shown** (timings) / **Stated** (cause)
11. Doubling the cells in every direction multiplies the total work by 16; the $256^3$ time on one GPU "approximately equals" the $512^3$ time on 16 GPUs (§4.1). **Stated**
12. The kinetic-energy, dissipation and enstrophy histories of the nearly incompressible Taylor–Green vortex ($M=0.1$) from the GPU code are "identical" to those of the earlier CPU code [23] (§4.1). **Stated** (not plotted)
13. Compressible Taylor–Green vortex ($Re=1600$, $M=0.25,0.5,0.75,1.0$, $256^3$): for $M=0.75$ and $1.0$ the kinetic energy has "regions of increasing kinetic energy rather than a monotone decline", consistent with Peng & Yang [38] (increase during $2\le t\le4$); the dissipation peak is delayed and flattened as $M$ grows; the $M=0.25$ peak matches $M=0.1$; for higher $M$ the dissipation is "significantly higher in the late evolution region (i.e., $t\ge11$)" (§4.1, Fig. 8). **Shown**
14. Single-precision memory is about half of double precision: ratios 1.940/1.968 (TITAN RTX, grids G1/G2), 1.928/1.959 (V100) (Table 8). **Shown**
15. Single- over double-precision speed-up on the incompressible channel (2 GPUs, 10 $\delta/U_c$): TITAN RTX 2.783 (G1), 2.670 (G2); V100 1.703 (G1), 1.757 (G2); summarized as 2.7x and 1.7x (Table 8). **Shown**
16. Because the single-precision peaks of the two GPUs are comparable, their single-precision run times are comparable; the authors conclude that the two GPU architectures "perform comparably for memory-intensive computing tasks in FP32 precision" (§4.2). **Shown** (times) / **Stated** (architectural conclusion)
17. With averaging over 200 $\delta/U_c$, mean velocity, rms and Reynolds-stress profiles from single and double precision show "negligible" qualitative differences; a deviation of $u^+_{\mathrm{rms}}$ between precisions is judged acceptable (§4.2, Figs. 10–13). **Shown**
18. Instantaneous rms profiles at $t=20$ and $200\,\delta/U_c$ (grids G2, H2, restarted from the same field) deviate visibly between precisions; the deviations "are caused by the round-off error of FP32 precision, which is approximately equals to or larger than the errors of numerical scheme" (§4.2, Fig. 14). **Shown** (deviation) / **Stated** (attribution and size comparison, not quantified)
19. "FP32 precision may not be safe for DNS in turbulence especially for time-evolutionary turbulent flows"; for LES and RANS "FP32 precision may be used" (§4.2, §5). **Stated**
20. The fine grids G2 and H2 "can meet the mesh resolution for DNS in turbulent channel flows" (Tables 6–7), and the H2 results "agree well" with the DNS of Fu et al. [9] (§4.2, Fig. 13). **Shown**
21. The van Driest-transformed compressible mean velocity is expected to follow the incompressible log law with $\kappa=0.40$, $B=5.5$ (Eqs. 10–11, Fig. 11). **Stated** (background) / **Shown** (comparison)
22. An earlier single-GPU DG-based HGKS [29] reached 6–7x (TITAN RTX) and 10–11x (V100) over the i7-9700 (§1). **Stated** (cited)

# Printed slips

- **Table 3, $256^3$ row:** printed speed-ups 7.4 (TITAN RTX) and 15.4 (V100). *(Compiler check, not in the sources: the printed times give $182.720/24.256=7.53$ and $182.720/11.697=15.62$; the other rows agree with their times.)*
- **Eq. (9) against the text:** $S_n=T^{total}_{n,GPU}/T^{total}_{1,GPU}$ is a time ratio that decreases with $n$, yet "the ideal scalability of parallel computations would be equal to $n$"; the $512^3$ case does not fit on one GPU, and its normalization in Fig. 5 is not stated.
- **Table 8:** $R_{fp}$ is defined as "the ratio of memory cost with FP32 to memory cost with FP64", but the printed values are double over single (*compiler check, not in the sources:* $5.355/2.761=1.94$); $S_{fp}$ likewise is double-precision time over single-precision time.
- **Table 8 against §4.2:** the text says G1 and H1 run on one GPU and G2 and H2 on two, while Table 8 labels all times $T^{total}_{2,GPU}$ and states "In the computation, two GPUs are used".
- **§4.1 against Fig. 4:** "MPI REDUCE for global time step" in the text, `MPI_ALLREDUCE` in the flow chart.
- **Eq. (6):** unbalanced parentheses "$-\tau A_r)]$" and "$-\tau A_l)]$".
- **Fig. 14 caption:** "instantaneous profiles of $U^+,V^+,W^+$", while the axes and text are the rms profiles.
- **Typos:** "TITAN TRX" (§4.1), "TITAN TRTX" (§3.3), "reference date" (§4.2), "constant moment flux", "is excepted" (expected), "Ackonwledgement".
- **Reference [29]** prints "Computers & Fluids 55 (2022) 105510".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol u=(u,v,w)$ (§2) | $\boldsymbol c$ (particle velocity, page-local, as on the [cao-2022](/sources/cao-2022.md) page) | **collision:** lower case is the microscopic velocity of the BGK equation |
| $\boldsymbol U=(U,V,W)$ | $u_i$ | macroscopic velocity |
| $f$, $g$, $\tau$ | $f$, $g$ (distribution function, Maxwellian; page-local), $\tau_{\mathrm{col}}$ (collision time $\mu/p$, registry §11) | **collision:** $\tau$ is not a stress |
| $\xi$, $N$ (§2) | $\vartheta$, $K_{\mathrm{int}}=(5-3\gamma)/(\gamma-1)$ (page-local) | **collision:** $\xi$ is not a reference coordinate; $N$ is also the number of GPUs (§3.2) |
| $\omega_{mn}$ | $w_i$ | Gauss weights; **collision:** $\boldsymbol\omega$ is the vorticity in §4 |
| $Q$, $L$, $F_p$ | (conservative variables, spatial operator, face flux) | **collision:** $L$ is also the Taylor–Green reference length |
| $\Omega_{ijk}$, $\Omega$ | (cell, domain and its volume) | **collision:** not the rotation-rate tensor |
| $Ma$ | $M$ | $M=V_0/c_0$ in the Taylor–Green vortex; bulk $M=0.8$ in the channel |
| $E_k$, $\varepsilon_{com}$ | $K$, (total viscous dissipation, page-local) | $\varepsilon_{com}$ = solenoidal plus $\tfrac43$ dilatational term, normalized by $\rho_0$ |
| $H$, $U_c$ | $\delta$, (velocity scale of the time unit $\delta/U_c$, not defined) | channel half-height |
| $\langle\cdot\rangle$, $\phi'$ | $\langle\cdot\rangle$, $\phi'$ | Reynolds average over time, $x$ and $z$; no Favre averages |
| $U^+$, $Y^+$, $\langle U\rangle^+_{VD}$ | $u^+$, $y^+$, (van Driest-transformed velocity) | |
| $\kappa=0.40$, $B=5.5$ | $\kappa$, $B$ | as printed |
| $-\langle U'V'\rangle$, $\langle-\rho U'V'\rangle/\langle\tau_w\rangle$ | $-R_{12}^+$, $-\langle\rho\rangle R_{12}/\tau_w$ (Reynolds-averaged form) | negative sign kept for plotting |
| $M_t=q/\langle c\rangle$ | $M_t$ | $q^2=\langle u_i'u_i'\rangle$ |
| $T^{total}_{n,GPU}$, $S_{gc}$, $S_n$, $S_{fp}$, $R_{fp}$ | — | wall-clock time; GPU/CPU speed-up; scalability; precision speed-up; memory ratio (see Printed slips) |

# Reference list

42 printed references, numbered style ([1]–[42]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this slug.
Ref. [23] (Cao, Pan & Xu, J. Comput. Phys. 448:110739) is the ingested
[cao-2022](/sources/cao-2022.md). Refs. [26] (FluTAS), [30] (Lehmann et al.)
and [39] (Cao et al.) are arXiv preprints and stay separate preprint
entries. Several printed keys (Pan & Xu 2018, Yang, Pan & Xu 2021,
Pirozzoli et al. 2021, Li 2019) share author-year stems with different works
already in the bibliography and are disambiguated at merge. [31] and [39]
print no year; several items end in "et al." and [40], [41] print garbled
author names.

# Pages created or updated

Chunk 4 (2026-10-26). This source is cited on:

- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Compressible velocity transformations](/definitions/compressible-velocity-transformation.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [High-order gas-kinetic schemes for turbulence simulation](/methods/high-order-gas-kinetic-scheme.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
