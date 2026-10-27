---
type: Source
title: "Fischer et al. (2022) — NekRS, a GPU-accelerated spectral element Navier–Stokes solver"
description: "Describes NekRS, the GPU port of the Nek5000 spectral element incompressible-flow solver built on libParanumal kernels, with its time stepping, matrix-free operators, gather–scatter communication and Chebyshev-accelerated p-multigrid pressure preconditioning, and reports scaling to all 27,648 V100 GPUs of Summit for reactor-flow cases."
resource: "doi:10.1016/j.parco.2022.102982"
source_kind: paper
authors: [Fischer P., Kerkemeier S., Min M., Lan Y.H., Phillips M., Rathnayake T., Merzari E., Tomboulides A., Karakus A., Chalmers N., Warburton T.]
year: 2022
venue: "Parallel Comput. 114:102982"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Parallel_Computing_Fischer_NekRS_a_GPU-accelerated_spectral_element_NavierStokes_solver.pdf"
tags: [software, gpu, spectral-element, incompressible-flow]
timestamp: 2026-10-26T20:48:00Z
---

# Summary

Fischer et al. (2022) present NekRS, an open-source C++ solver for the
incompressible Navier–Stokes and energy equations on GPUs, with kernels
written in the OCCA kernel language and translated at run time to CUDA,
HIP or OpenCL. It combines the user interface, features and gather–scatter
library (gslib) of the CPU code [Nek5000](/software/nek5000.md) with
roofline-tuned kernels forked from libParanumal. The discretization is the
continuous Galerkin spectral element method on curvilinear hexahedra with
Gauss–Lobatto–Legendre (GLL) nodal bases of degree $N$, tensor-product sum
factorization, matrix-free operators, a diagonal mass matrix and
over-integration (dealiasing) of the advection term; it is the continuous
relative of the
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md),
which the paper cites only through a GPU DG incompressible solver of
libParanumal. Time stepping is semi-implicit BDF$k$/EXT$k$ or a
characteristics (operator-integration-factor) variant that allows Courant
numbers 2–4, with a fractional-step split into a pressure Poisson problem
and Helmholtz problems for the velocity.

The paper is about performance engineering. Its algorithmic contributions
for GPUs are device-aware autotuning of gslib communication, a choice
between 2D and 3D thread structures for the dealiased advection kernel, and
a pressure preconditioner built from $p$-multigrid with Chebyshev-accelerated
Jacobi or Schwarz smoothers, single-precision smoothing, adaptive
gather–scatter and projection-based initial guesses, which together cut the
pressure-solve time 4.85-fold on a 1,568-pebble bed. Turbulence enters
only as the application class: a spacer-grid case the paper labels
[LES](/definitions/large-eddy-simulation.md) and a 5×5 rod-bundle case it
labels [DNS](/definitions/direct-numerical-simulation.md) are timing
benchmarks, with no subgrid model, resolution argument, statistics or
validation reported. NekRS on Summit is 4.8× faster per step than Nek5000
on Mira for the spacer grid at comparable efficiency. Strong scaling to all
27,648 V100 GPUs of Summit for meshes of up to 175 million elements at
$N=7$ (60 billion points) gives 80% efficiency at about 2.5 million points
per GPU.

# Version read

arXiv preprint arXiv:2104.05829v1 [cs.PF], 12 April 2021 (footer
"Preprint submitted to arXiv, April 14, 2021"), 15 pages, all read. Title
and the eleven authors match the Crossref record of the version of record
(Parallel Comput. 114:102982, 2022) up to capitalization; the preprint
prints no DOI. The published article may differ in tables and numbers;
claims and locators here are those of the preprint.

# Key claims

1. NekRS is an open-source C++/OCCA incompressible Navier–Stokes solver for GPUs based on the spectral element method, combining Nek5000's scalable infrastructure with libParanumal's kernels; it keeps the Nek5000 interface and features such as conjugate heat transfer (§1, §5). **Stated**
2. Calculations with up to 60 billion grid points scale to 27,648 V100 GPUs on OLCF Summit (Abstract; §4.2, Table 3: $175{,}618{,}000$ elements, $N=7$). **Shown**
3. The integrator the paper calls standard is BDF$k$/EXT$k$ (Eq. 6), typically $k=3$ at Courant number 0.5; the characteristics alternative (Eqs. 7–8) is typically run at Courant numbers 2–4 but only at second order, because its fully dealiased hyperbolic substeps are expensive (§2.1). **Stated**
4. The pressure Poisson problem carries the fastest (acoustic, infinitely fast) modes and is the stiffest and most communication-intensive substep; isolating it avoids evaluating the viscous and advection operators at each iteration (§2.2, §3.4). **Stated**
5. With GLL tensor-product bases the leading $O(nN)$ work becomes small dense matrix–matrix products and storage is $O(n)$; a full gradient needs $10E(N+1)^3\approx10n$ memory references and $6E(N+1)^4+15E(N+1)^3$ operations, printed as $\approx n(15+6N)$; the local stiffness product needs $7(N+1)^3$ references and $12(N+1)^4+15(N+1)^3$ operations per element (§2.3). **Derived** (see Printed slips)
6. GLL quadrature is exact for affine elements when the integrand has degree $\le2N-1$, enough for the Poisson operator but not for the advection operator, whose integrand has degree $3N$ and needs over-integration (§2.3). **Stated**
7. The gather–scatter operator has a unit-depth stencil for all $N$, so the discretization is "communication minimal" (§2.3). **Stated**
8. The strong-scale limit is 2,000–4,000 points per MPI rank for Nek5000 on Mira and 2–4 million points per V100 GPU (§3, citing [12]). **Stated**
9. Pre-partitioning with recursive coordinate bisection cuts recursive-spectral-bisection run times by a factor of 100; partitioning 60 million elements on 8,100 Summit cores takes about 40 s with Lanczos plus 0.8 s for the coordinate bisection (§3.1). **Stated**
10. The communication strategy matters (10×) for distributed AMG coarse-grid problems; with 3 billion points on a million Mira ranks, setup with 10 trials per method takes under one second and one exchange takes 0.000325 s (pairwise) against 0.0046 s (crystal router) (§3.2). **Shown**
11. The 3D thread block of the advection kernel is limited by the 1,024 threads per block to $N_q\le10$ dealiasing points per direction ($N\le9$); the 2D structure reaches the limit only at $N_q=32$, and keeping the third direction in registers cuts shared-memory loads "by nearly a factor of three" (§3.3, Algorithms 1–2). **Derived**
12. On GPUs Chebyshev-accelerated smoothers beat the plain additive Schwarz smoother: Chebyshev–Jacobi is 30% faster than the baseline and 2.5× with the enhancements; Chebyshev–Schwarz is 1.85× in its default form and 4.85× with adaptive gather–scatter, single-precision smoothing and projection-based initial guesses (§3.4, Fig. 4; 1,568-pebble case, 22 nodes, 1.36 million points per GPU). **Shown**
13. Characteristics time stepping (CHAR-BDF2, $\Delta t=1.0\times10^{-3}$, Courant number 4.05) allows a 4× larger step for a 2× increase in time per step relative to BDF3-EXT3 ($\Delta t=2.5\times10^{-4}$, Courant number 1.06): 0.503 s against 0.259 s with Chebyshev–Schwarz (§3.4, Table 1). **Shown**
14. With Chebyshev–Schwarz the pressure iterations per step fall from 93 (Schwarz) to 16 with CHAR-BDF2 and from 39 to 8 with BDF3-EXT3 (Table 1). **Shown**
15. After the 4.85-fold reduction about 25% of wall time is still in the pressure step; the interior gather–scatter kernels (10% of wall time) sustain 80% of global memory bandwidth, the pressure operator (6.4%) 90%, the fast-diagonalization solve 80% of shared-memory bandwidth, and the characteristics substep takes about 18% of wall time at 70% of shared-memory bandwidth (§3.4, Fig. 5). **Shown**
16. Spacer-grid case labelled LES ($Re_D=14{,}000$, 3.2 million elements, $N=7$): Nek5000 on 8,192 Mira nodes runs at 0.68 s per step at about 80% efficiency; NekRS on 98 Summit nodes at 0.14 s, 4.8× faster at comparable efficiency; the GPU time splits into about 22% advection, 24% velocity solve and 52% pressure (8% coarse grid) (§4.1, Table 2). **Shown**
17. 5×5 rod-bundle case labelled DNS ($Re_D=19{,}000$, 8.4 million elements, $N=7$): NekRS at 0.183 s per step is about 2× faster than the estimated Mira strong-scale time of 0.35 s; its Summit scaling is "not ideal" (best at 3.9 million points per GPU), for unclear reasons (§4.1). **Shown**
18. Strong scaling to all of Summit gives 80% efficiency at about 2.5 million points per V100; points per rank, not the rank count, is the leading indicator of scalability (§4.2, Table 3). **Shown**
19. Weak scaling at 2.1 million points per GPU: the 17×17 rod bundle loses 18% efficiency over a 53-fold increase in GPU count (82.5% at 27,648 GPUs); the full-core case drops to 54% over a 17-fold increase, correlated with the maximum number of neighbours in the communication graph; the authors suggest partitioning to minimize neighbour count rather than data volume (§4.2, Table 3). **Shown**
20. Pressure iterations are about 2 per step for the rod bundles (synthetic initial condition not yet turbulent) against about 8 for pebble beds; the authors expect 4–8 once turbulence is established (§4.2). **Shown** (counts) / **Stated** (expectation)
21. Single-GPU turbulent pipe flow ($N=7$): the A100 is 1.52× faster than the Summit V100, in line with its memory bandwidth; MI100 and MI60 deliver 85% and 60% of the Summit V100; one V100 matches 336 Power9 cores on 8 nodes; per-device hand tuning is still needed (§4.3, Table 4). **Shown**
22. NekRS on Summit's Power9 CPUs reaches 74% parallel efficiency at 6,615 points per rank (§4.3, Table 4). **Shown**
23. Single-node stratified atmospheric boundary layer (32,768 elements, $N=7$, 11.2 million points): the 80% strong-scale limit is 1.8 million points per GPU on both V100 and A100, and the A100 runs 1.55× faster (0.055 s per step); the low limit is attributed to the low neighbour count (§4.3, Table 5). **Shown**
24. 44,257-pebble bed (13 million elements, $N=7$, 4.5 billion points) on 1,788 V100s: 0.54 s per step, 10% advection, 6% velocity, 84% pressure; a 300,000-pebble target (about 30 billion points) is "well within the current performance envelope on Summit" (§4.3). **Shown** (timings) / **Stated** (projection)
25. NekRS sustains 80–90% of the realizable, bandwidth-limited peak (§5). **Stated**
26. The double-precision local spectral element matrix–vector kernels of libParanumal exceed 1 TFLOPS on the V100 (§1, citing [8, 12]). **Stated**

# Printed slips

- **Table 1 header.** It prints "$n = 2,569,495,663$" for the 1,568-pebble case, whose rows give 524,386 elements at $N=7$ and whose text (§3.4) gives $n=180$M. With the paper's $n\approx EN^3$, $524{,}386\times7^3=179{,}864{,}398$, matching the text and not the header *(compiler check, not in the sources)*.
- **Table 2, Summit Nek5000 CPU, 38 nodes.** The printed time per step is 1.68e+01 s, but the same block's speedups 2.12, 4.56 and 9.64 against 0.50e+01, 0.23e+01 and 0.11e+01 s imply about 10.6 s ($2.12\times5.0=10.6$, $9.64\times1.1=10.6$) *(compiler check, not in the sources)*.
- **Mira spacer-grid time.** §4.1 prints "$t_{step}=0.68$s"; Table 2 prints 6.90e-01.
- **Malformed number (§4.1).** "80% strong-scale limit timings would be realized at $P\approx 5,242,88$ ranks".
- **Node count as rank count (§4.2).** "the partitioning for $P = 271$ resulted in a 2D decomposition": 271 is the node count of that row of Table 3, which has 1,626 GPUs, while $P$ is defined as the number of ranks.
- **Undefined quantity (§4.2).** "the large $n_{0.8}$ values": no $n_{0.8}$ is defined or tabulated.
- **Pipe-flow mesh (§4.3, Table 4).** The text and the Table 4 caption give "$E = 6840$" and "$n = 2,346,120$"; the Table 4 header and rows give $E=6480$ and $n=2{,}222{,}640$. Both pairs are internally consistent ($6840\times343=2{,}346{,}120$, $6480\times343=2{,}222{,}640$), so they describe different meshes; the "$n/P=6615$" of claim 22 equals $2{,}222{,}640/336$ *(compiler check, not in the sources)*.
- **CPU speed ratio (§4.3).** "Summit's single V100 ... is only 248× faster than a single CPU"; Table 4 gives $19.9/0.0851=234$ *(compiler check, not in the sources)*.
- **A100 model.** "Nvidia A100 SXM2" (Table 4 caption) against "A100 SXM4" (Table 5 caption) for the same ThetaGPU nodes; Table 5's title prints "Singe Node".
- **Operation count (§2.3).** $6(N+1)^4+15(N+1)^3=(N+1)^3(6N+21)$, so with $n=E(N+1)^3$ the count is $n(21+6N)$, not the printed $\approx n(15+6N)$ *(compiler check, not in the sources)*.
- **Integration interval (§2.1).** The characteristic foot is found "integrating the velocity field backward in time over $[t^n,t^{n-1}]$", while Eq. 8 is posed on $[t^{n-j},t^n]$.
- **Typos.** "emthod" (§2.3), "anomolous" (§4.1, §4.2), "Architetures" (§4.3 heading), "constrast", "discrepency", "hexadral".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u$, $p$, $T$ | $\boldsymbol u$, $p$, $T$ | nondimensional, incompressible |
| $Re$, $Pe$, $Re_D$ | $Re$, (Péclet number), $Re_D$ | $Re_D$ on diameter and mean velocity |
| $N$ | $N$ | polynomial degree; $N+1$ GLL points per direction |
| $\xi_j$, $\rho_i$ | $\xi_j$, $w_i$ | GLL nodes and quadrature weights; **collision:** the source's $\rho_i$ are weights, not densities |
| $h_i$ | $\ell_i$ (page-local Lagrange cardinal functions) | **collision** with the element size $h$ |
| $\hat D$ | $D_{ij}$ | 1D differentiation matrix |
| $\omega$ | $\boldsymbol\omega$ (extrapolated vorticity, $\sum_j\alpha_j\nabla\times\boldsymbol u^{n-j}$) | not the specific dissipation rate |
| $\tilde{\mathbf u}^{n-j}$ | (velocity at the foot of the characteristic) | **collision:** not a Favre filter |
| $\beta_j$, $\alpha_j$ | (BDF and extrapolation coefficients) | **collision** with the field-inversion $\beta$ and the DG blending factor $\alpha$; indexed here |
| $E$, $E_p$ | $N_e$ (page-local element count, total and per rank) | **collision** with the total energy $E$ |
| $n$, $P$, $n/P$ | (grid points, ranks or GPUs, points per rank) | $n\approx EN^3$ in the text, $E(N+1)^3$ in table headers |
| $N_q$ | (dealiasing quadrature points per direction) | |
| $Q$, $A$, $B^e$, $G^e_{mm'}$ | (global-to-local map, stiffness matrix, diagonal mass matrix, geometric factors) | |
| CFL | (Courant number) | |

# Reference list

42 printed references, numbered style ([1]–[42]). The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Refs. [1], [13] and [28] are software web pages with corporate
authors (Nek, gslib, OCCA). Refs. [6], [7], [11], [16], [27] and [42]
print no year and are keyed with the citing year 2022; [11], [30] and [42]
are arXiv preprints and [16] is "Under Review", each its own entry. Partly
unparseable printed data: [6] prints "1094342015576846" in place of volume
and pages, [7] only the journal, [36] no journal name, [37] the page range
"4422–44251", [35] the run-together author "YongpengZhang", [40] the first
author "X. chuan Cai"; all recorded as printed. No printed duplicates.

# Pages created or updated

Chunk 3 (2026-10-26), cited further in chunk 6. This source is cited on:

- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [GALÆXI](/software/galaexi.md)
- [Nek5000 and NekRS](/software/nek5000.md)
