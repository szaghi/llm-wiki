---
type: Source
title: "Valvo & Abbà (2025) — A hardware locality-informed dynamic load balancing for a p-adaptive local discontinuous Galerkin LES solver"
description: "Dynamic load balancing for the p-adaptive local DG solver dg-comp: Zoltan graph and geometric partitioning with Gauss-point vertex and edge weights and a hardware locality-informed hierarchical partitioning, tested on an advected vortex and a Smagorinsky LES of the square cylinder at Re 22000."
resource: "doi:10.1016/j.compfluid.2025.106810"
source_kind: paper
authors: [Valvo P., Abbà A.]
year: 2025
venue: "Comput. Fluids 302:106810"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2025_Crossref_Computers_amp_Fluids_Valvo_A_hardware_locality-informed_dynamic_load_balancing_for_a_p-.pdf"
tags: [mesh-adaptation, dg, les, implicit-les, software]
timestamp: 2026-10-28T17:41:00Z
---

# Summary

Valvo & Abbà (2025) add dynamic load balancing to *dg-comp*, the
p-adaptive local discontinuous Galerkin (LDG) solver of the FEMilaro
library for compressible DNS, [implicit LES](/definitions/implicit-les.md)
(the subgrid flux set to zero) and explicit
[LES](/definitions/large-eddy-simulation.md), whose filter is the
projection onto the polynomial space. The degree $N\in[2,4]$ of each
tetrahedron is changed during the run by a second-order structure-function
indicator of under-resolved turbulence (the
[mesh adaptation](/methods/mesh-adaptation.md) of the group's earlier
work), so the per-element cost drifts and a pure-MPI run becomes
imbalanced. Load balancing is cast as graph partitioning: one vertex per
element weighted by its number of volume Gauss points, one edge per shared
face weighted by the face Gauss points of the higher-degree neighbour,
extra edges across periodic boundaries. Four Zoltan partitioners (RCB,
RIB, Hilbert curve HSFC, graph-based GRAPH) are embedded, and a
hierarchical partitioning (GRAPH between nodes, a geometric method inside
each node, with CPU binding of consecutive ranks) makes the partition
aware of hardware locality.

On an advected viscous vortex (no explicit closure, $Re=22000$,
$M=0.3$, 128 MPI tasks) balancing cuts the elapsed time by about 71%
against adaptation without balancing and by about 82.5% against uniform
$N=4$; the authors conclude that more than half of the adaptive gain is
lost without balancing. On a [Smagorinsky](/methods/smagorinsky-model.md)
LES of the [square cylinder](/benchmarks/square-cylinder-flow.md)
($Re=22000$, $M=0.3$, 336 tasks on 3 nodes) the reduction against uniform
$N=4$ is 40.9–44.6% with balancing and 9.2% without, close to the
reduction of degrees of freedom. Hierarchical partitioning lowers
inter-node communication volume (by 92% for HSFC on the vortex, by a
factor of about 4–10 on the cylinder) without lowering the total time,
which the authors relate to the face-neighbour LDG stencil and the
InfiniBand networks. The basis is modal and the elements are tetrahedra,
not the nodal hexahedra of the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md).
Evidence is numerical and profiler-based; no turbulence closure is
proposed.

# Version read

Version of record (Elsevier, open access CC BY; received 16 April 2025,
revised 14 July 2025, accepted 25 August 2025, online 11 September 2025),
16 pages, all read; pages 2, 13 and 14 checked visually (Eqs. 1–2,
Figs. 16–19). Page 1 matches the metadata (title, two authors, venue,
DOI). Supplementary material exists online and was not read. Numbering on
this page is that of the version read.

# Key claims

Page-local symbols: $w_i$ the vertex (element) weight and $w^e_{ij}$ the
edge (face) weight of the partitioning graph; $W_k$ the weight of
partition $P_k$; $V_{\mathrm{comm}}$ its communication volume (Eq. 9, in
face Gauss points, not bytes), $\bar V_{\mathrm{comm}}$ its mean over tasks
and $V^{a-b}_{\mathrm{comm}}$ the volume of the union of the partitions of
ranks $a$ to $b$; $n_g$ the number of volume Gauss points of an element;
$\mathcal I_{\mathrm{SF}}$ the structure-function adaptation indicator.

1. In a pure-MPI p-adaptive LDG solver, dynamic load balancing is mandatory: on the vortex test all four Zoltan methods reduce total elapsed time by about 71% against the adaptive run without balancing (p-AD-noLB) and by 82.3–82.7% against uniform $N=4$ (§4.5, Table 5). **Shown**
2. "More than half of the computational gain obtainable with adaptation is wasted if dynamic load balancing is not performed" (§4.5, Tables 2 and 5). **Shown**
3. Without balancing, adaptation of the vortex case reduces the degrees of freedom from 564 620 to about 170 680 on average; Table 2 prints $\Delta t=-39.5\%$ (p4: 13 060 s, 464 core hours; p-AD-noLB: 7523 s, 281 core hours), with accuracy matched to p4: maximum time-history deviation at most 0.008% in $\rho$ and 0.131% in $\lVert\boldsymbol u\rVert$ at four probe offsets $\Delta x=2.5$–$5.5$ (Table 1, Fig. 4). **Shown**
4. As vertex weight, the degree $N$ "completely misses the load peaks" (Fig. 5), the DOF count often overshoots them (Fig. 6), and $n_g$ "correctly captures the imbalance peaks up to twice the mean load, while for higher values it underestimates them" (Fig. 7); $n_g$ is adopted in preference to "more sophisticated weights and multi-weight approaches" (§4.4). **Shown**
5. Predicted relative element costs for $N=2,3,4$: 1.00/1.50/2.00 by $N$, 1.00/2.00/3.50 by DOFs (10/20/35), 1.00/1.71/3.07 by $n_g$ (14/24/43) (Table 3). **Stated** (weight definitions; quality shown in Figs. 5–7)
6. The edge weight $w^e_{ij}$ is the number of face Gauss points of the quadrature of the higher degree of the two neighbours, 6/12/16 for $N=2/3/4$ (ratios 1.00/2.00/2.67, Table 4); it agrees well with measured bytes per task and overpredicts the highest peaks (Fig. 8, vortex; Fig. 18, cylinder). **Shown**
7. With balancing, the estimated imbalance is limited to +10% of the average; about 15% of partitions show a "load hole" of significantly lower estimated load, attributed to a limitation of the partitioning approach and left to future work (§4.5, Fig. 9). **Shown**
8. Repartitioning at every adaptation step ($dt_{\mathrm{repart}}=dt_{\mathrm{adapt}}$) is best for the vortex: imbalance after adaptation "would double the elapsed time per time step", and "the partitioning step lasts as a balanced time step" (§4.5). **Stated**
9. GRAPH gives the lowest mean communication volume, $\bar V_{\mathrm{comm}}=269$, against 315 (RCB), 333 (RIB) and 658 (HSFC) (Table 6); its longer partitioning time (172 s against 122–132 s) cancels its computational-time advantage (Table 5). **Shown**
10. HSFC slices the box along the spanwise direction and cuts many more edges than the spatially compact RCB and RIB partitions (§4.5, Fig. 12). **Shown** (qualitative figure)
11. GRAPH partitions assigned to one rank group (0–63) are not spatially compact: GRAPH minimizes per-partition communication but not the communication between hardware components, so node-to-node communication is sub-optimal (§4.6, Fig. 13). **Shown**
12. Hierarchical partitioning (2 GRAPH partitions at node level, then 64 geometric partitions per node) "always outperforms the non-hierarchical one in terms of node-to-node communication": $V^{0-63}_{\mathrm{comm}}$ RCB 1251 to 654, RIB 744 to 624, HSFC 9291 to 741 (Table 7). **Shown**
13. For HSFC, hierarchical partitioning reduces node-to-node communication by 92% and slightly reduces total time (2232 to 2206 s); for RCB and RIB the total time rises slightly (2172 to 2280 s and 2172 to 2248 s), because partitioning costs more and second-level partitions of irregular subdomains raise $\bar V_{\mathrm{comm}}$ (RCB 315 to 324, RIB 333 to 341) (§4.6, Table 7). **Shown**
14. On the square cylinder, adaptation without balancing saves only 9.2% of elapsed time (18 568 to 16 866 s) although the DOFs fall by about 45% (833 560 to about 463 000) (Table 10). **Shown**
15. With balancing on the cylinder the reduction against Sc-p4 is 40.9–44.6%; since the DOFs fall by almost the same amount, this "is near to the theoretical optimum" (§5.2, Table 11). **Shown**
16. Hierarchical partitioning (3 GRAPH × 112 geometric) cuts inter-node communication volumes from about 9 000–24 000 to about 1 800–4 300 per node group, while the total time is longer (10 698–10 975 s against 10 286–10 751 s), "suggesting that the problem is not communication-bounded on this hardware" (§5.2, Table 11). **Shown**
17. The local LDG stencil (face neighbours only) together with an efficient InfiniBand network "likely reduces the importance of communication time on the overall elapsed time" (§5.2). **Stated**
18. Because the LDG stencil of an element is itself and its face neighbours, a connectivity-based graph is "fully equivalent to a stencil-based one, unless periodic boundary conditions are used", which need extra edges (§3, Eq. 7). **Derived**
19. Gauss-point edge weights estimate communicated bytes and are hardware independent; Gauss-point vertex weights are hardware independent only if the relative cost of elements of different degree is preserved across processors, assumed as "a rough but still acceptable approximation" for the AMD EPYC (Discoverer) and Intel Xeon (LEONARDO) clusters and supported by VTune profiling on LEONARDO (§5.2, Fig. 17). **Shown** (for the two machines)
20. The adaptive Sc-pAD-noLB and uniform Sc-p4 runs give $\langle C_D\rangle$ 2.3818 and 2.445, both within the LES range 1.66–2.77 of Rodi et al. [37] (Table 9, Fig. 16). **Shown**
21. Table 9 prints, in the columns labelled RMS$_{C_L}$ and RMS$_{C_D}$, 0.1531 and 1.366 for Sc-p4 and 0.1934 and 1.305 for Sc-pAD-noLB, against literature ranges printed as 0.10–0.27 and 0.38–1.79. **Shown**
22. The hardware-locality optimization is expected to matter more on topologies whose bandwidth falls at higher node counts (e.g. hypercube) and on configurations needing more than two hierarchical steps (§6). **Stated**

The discretization of §2 in registry notation: conservative state
$[\rho,\rho e^{\mathrm{tot}},\rho\boldsymbol u]$ (Favre-filtered in LES),
an auxiliary gradient variable for the viscous and subgrid fluxes built
from $[T,\boldsymbol u]$, a Rusanov flux on convective faces and the LDG
flux of Bassi & Rebay on viscous, subgrid and gradient faces, five-stage
fourth-order SSP Runge–Kutta in time (Eqs. 1–3). The subgrid flux
(Eq. 2) carries the SGS stress, the SGS heat flux and an SGS turbulent
diffusion flux; the compressible Smagorinsky model of Abbà et al. (2015)
[7] is used for the cylinder, with no constant or filter width given in
this paper. The adaptation indicator (Eqs. 4–5) is
$\mathcal I_{\mathrm{SF}}(K)=\big(\sum_{ij}[D_{ij}(K)-D^{\mathrm{ISO}}_{ij}]^2\big)^{1/2}$,
with $D_{ij}$ the second-order velocity structure function evaluated
inside element $K$ at separations comparable to the element size and
$D^{\mathrm{ISO}}_{ij}$ its isotropic part, subtracted because "both LES
and ILES simulations usually predict the isotropic part of the unresolved
turbulence at an acceptable level of accuracy"; $N$ is raised where
$\mathcal I_{\mathrm{SF}}$ exceeds a threshold $\epsilon_{N+1}$ and lowered
below $\epsilon_N$, thresholds set from a short coarse run (§2.2).

# Printed slips

- **Table 2, p-AD-noLB row:** 7523 s, 281 core hours and $\Delta t=-39.5\%$ are printed together. *(Compiler check, not in the sources: with 128 tasks the p4 row is consistent, $13060\times128/3600=464.4$ core hours, printed 464; $7523\times128/3600=267.5$, not 281; 281 core hours correspond to $281\times3600/128\approx7903$ s, and $1-7903/13060=0.395$ matches the printed $-39.5\%$ while $1-7523/13060=0.424$ does not; the Table 5 reduction of GRAPH, $-70.7\%$, fits $1-2310/7903=0.708$ rather than $1-2310/7523=0.693$.)*
- **Table 11:** the caption reads "Percentage reductions in the computational time", while the $\Delta t$ entries follow the Total column. *(Compiler check, not in the sources: $1-10286/18568=0.446$ and $1-10975/18568=0.409$ give the printed $-44.6\%$ and $-40.9\%$; Sc-RCB $9445+839=10284$ against the printed total 10 286; Sc-3GRAPH-112RCB $1-10698/18568=0.424$ against the printed $-42.3\%$.)*
- **§2.1:** the auxiliary variable is defined as "$\mathcal G=\nabla\mathbf U$", while the auxiliary equation of Eq. (1) is written in $\boldsymbol\Phi=[T,\mathbf u]$.
- **§2.1 against the rest:** the degree is $q$ in $\mathbb P^q(K)$, $p$ everywhere else.
- **§4.5:** "MPI tasks of rank 0–63 or, dually, 64–128"; the Fig. 13 caption has "64–127" for the 128 tasks.
- **Table 6 header:** "max($\bar V_{comm}$)" beside "min($V_{comm}$)".
- **§5.2:** "a small profiling test of 40 time is performed" (40 time steps in §4.4).
- **Ref. [12]:** pages printed "AIAAJ 2020;58:3728–4203".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $p$, $q$, $p_{max}$ | $N$, $N_{\max}$ | local polynomial degree, $N\in[2,4]$ in both tests |
| $\mathbb P^q(K)$, $\mathcal V_h$ | polynomials of degree $N$ on element $K$; broken space | modal orthonormal basis on tetrahedra |
| $\mathbf U=[\rho,\rho e^{tot},\rho\mathbf u]$ | conservative state | Favre-filtered in LES |
| $\boldsymbol\Phi=[T,\mathbf u]$, $\mathcal G$ | variables of the auxiliary gradient; auxiliary gradient | see Printed slips |
| $\mathbf F^e$, $\mathbf F^v$, $\mathbf F^{SGS}$ | Euler, viscous, subgrid fluxes | $\mathbf F^{SGS}=0$: DNS or [implicit LES](/definitions/implicit-les.md) by resolution |
| $\tau^{SGS}$, $\mathbf Q^{SGS}$, $\mathbf J^{SGS}$ | SGS stress, SGS heat flux, SGS turbulent diffusion flux | sign and trace convention not given in this paper |
| $k$ | thermal conductivity (Eq. 2); partition index ($P_k$, $W_k$); hardware scaling factor (§5.2) | **collision** with the registry's $k$ (turbulent kinetic energy) |
| $D_{ij}(\mathbf x,\mathbf r)$, $D^{ISO}_{ij}$ | second-order velocity structure function, its isotropic part | $\langle\cdot\rangle$ the expected value, as the registry's average |
| $Ind_{SF}(K)$, $\epsilon_i$ | $\mathcal I_{\mathrm{SF}}$ (page-local), thresholds | |
| $w_i$, $w^e_{ij}$, $W_k$, $V_{comm}$, $n_g$ | as printed (page-local) | Eqs. 6–9 |
| $\Gamma$, $R_v$, $\Psi$ | vortex strength, radius, stream function | Eq. 10, $\Gamma=0.412180318$, $R_v=0.5$ |
| $C_D$, $C_L$ | $C_D$, $C_L$ | |
| Re, M | $Re$, $M$ | 22000 and 0.3; cylinder side $L_H=1$ |

# Reference list

38 printed references, numbered style with DOIs. The list is merged
complete into the [bibliography](/bibliography.md) with `citedby` this
slug. Item [23] is software ("Femilaro, a finite element toolbox. 2025")
with no personal author; [10] prints the year 2025 with a DOI containing
2024; [12] carries the page range noted above; [37] prints its fourth
author as "Pourquie’e". No item is printed twice, none is unparseable, and
no cited work falls on the key of a planned or ingested bundle source.

# Pages created or updated

Chunk 15 (2026-10-28). This source is cited on:

- [Flow past a square cylinder](/benchmarks/square-cylinder-flow.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Mesh adaptation for turbulent-flow simulation](/methods/mesh-adaptation.md)
- [Smagorinsky model](/methods/smagorinsky-model.md)
