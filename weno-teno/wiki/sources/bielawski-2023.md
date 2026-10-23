---
type: Source
title: "Bielawski et al. (2023) — Highly-scalable GPU-accelerated compressible reacting flow solver for modeling high-speed flows"
description: "GPU (CUDA) port of an unstructured second-order OpenFOAM finite-volume solver for compressible reacting flows: face loops with atomics, boundary-only host–device transfers, static and adaptive cell-batched chemistry integrators, scaling to 6144 V100 GPUs, detonation-engine and scramjet demonstrations, and a central/HLLC/AUSMDV dissipation comparison."
resource: "doi:10.1016/j.compfluid.2023.105972"
source_kind: paper
authors: [Bielawski R., Barwey S., Prakash S., Raman V.]
year: 2023
venue: "Comput. Fluids 265:105972"
local_file: "/home/stefano/papers/mosaic/weno-teno/2023_Crossref_Computers_amp_Fluids_Bielawski_Highly-scalable_GPU-accelerated_compressible_reacting_flow_s.pdf"
tags: [software, gpu, finite-volume, reacting-flows, unstructured-mesh, performance]
timestamp: 2026-10-23T16:00:00Z
---

# Summary

The paper ports an unstructured, cell-centred finite-volume OpenFOAM solver for
the compressible reacting Navier–Stokes equations
([multicomponent](/definitions/multicomponent-euler-equations.md), with
Arrhenius chemistry) to NVIDIA GPUs with CUDA. It keeps OpenFOAM's data
structures. The solver is named once, "UMReactingFlow". Its discretization is
standard and nominally second order, and none of it is the paper's contribution:

- [HLLC](/methods/hll-riemann-solvers.md) with slope-limited interpolation to
  the faces;
- a "KNP formulation" cited for the viscous terms, after Greenshields et al.'s
  OpenFOAM implementation of semi-discrete central schemes
  ([central-upwind](/methods/central-upwind-scheme.md)); no formula is printed;
- a Gauss [gradient](/methods/unstructured-gradient-reconstruction.md);
- explicit second-order Runge–Kutta;
- Strang [operator splitting](/methods/operator-splitting.md) of the stiff
  chemistry.

The contribution is computational. The paper identifies three GPU issues:
coalesced data access, thread divergence and thread safety. Its remedies are:

- face loops, accumulated into cells with an `atomicCAS`-based add;
- separate boundary arrays, so that only $O(N_{\mathrm{cells}}^{2/3})$ data moves
  between host and device for the MPI exchange;
- two cell-batched chemistry integrators for the operator-split
  constant-volume reactor. The static-cell integrator threads every kernel over
  all cells. The adaptive-cell hybrid CPU/GPU integrator compacts the
  still-reacting cells and hands the last few to the CPU.

On Summit (V100), weak scaling from 6 to 6144 GPUs at $2^{20}$ cells per GPU is
near-ideal up to 3072 GPUs. A roofline shows the fluid kernels memory-bound and
the chemistry kernels near peak. The demonstrations are a CH4–O2 rotating
detonation engine and an ethylene scramjet
([shock-induced combustion](/benchmarks/shock-induced-combustion.md)).

Appendix A compares a skew-symmetric central scheme
([split convective forms](/methods/split-convective-forms.md)), HLLC and AUSMDV
on [decaying compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
on structured and skewed tetrahedral meshes. The
[numerical dissipation](/definitions/numerical-dissipation.md) ranks central <
HLLC < AUSMDV. At turbulent Mach 0.6 the scheme matters more than the mesh, and
the authors suggest a [hybrid](/methods/hybrid-weno.md) central/HLLC scheme.
[PyFR](/software/pyfr.md) is cited as a GPU code whose cost is dominated by
matrix multiplication.

# Version read

The file is the accepted author manuscript, not the typeset version of record.
Page 1 carries the header "Version of Record:
https://www.sciencedirect.com/science/article/pii/S0045793023001974", a
manuscript stamp and the footer "Preprint submitted to Elsevier, October 2022".
It has 56 PDF pages: 46 of text including Appendices A–B, references on
pp. 47–53, then highlights, CRediT and declarations. All were read, with
pp. 7–9, 17, 18 and 38 also checked visually. Page 1 matches Crossref (title,
four authors, order); it capitalizes the title and prints the first author's given
name as "Ral". Numbers cited here are those of the manuscript.

# Key claims

Registry notation: velocity $v$; the source's conductivity $\alpha$ is written
$\lambda_{\mathrm{th}}$ (see the notation map).

1. The baseline solver discretizes the viscous terms with a "KNP formulation" [35] and the inviscid terms with slope-limited interpolation and HLLC. Time integration is explicit second-order Runge–Kutta. Each component is "nominally second-order accurate" (§3). **Stated**
2. Interpolating conservative variables to faces with a limiter can break $\sum_kY_k=1$, because the limiter acts differently on the mass-weighted scalars and on the face mass. This gives each scalar a different effective contact speed, and the error "can grow and become significant over a simulation". Species limiting also occurs in mixing and burning regions (§3). **Stated** (not demonstrated)
3. HLLC is chosen for its low cost and its resolution of contact waves. Approximate Riemann solvers are described as giving "near minimal possible dissipation across discontinuities while maintaining a monotonicity preserving solution" (§3). **Stated**
4. Explicit finite-volume fluxes have low arithmetic intensity, while chemistry and thermophysical-polynomial evaluations have high intensity and dominate the cost (§4). **Stated**, partly **Shown** (Fig. 9)
5. A face loop is preferred to a cell loop. It exposes about 3× more parallelism on hexahedral meshes and is accessed coalesced. Its race when accumulating into cells is resolved with an `atomicCAS`-based `threadSafeAdd` (§4). **Stated**
6. The Newton–Raphson temperature inversion converges in about 10 iterations, nearly independently of the state, so its thread divergence needs no mitigation (§4, Alg. 2). **Stated**
7. The number of chemistry sub-steps varies between cells by $O(10^4)$ for stiff mechanisms. Adaptive data rearrangement gives "nearly a factor of 70 reduction in computational cost for the chemical system" (§4). **Stated** (no table or test gives the factor)
8. Internal (MPI) and external boundary data are stored in separate arrays, so the host–device copy per step scales as $O(N_{\mathrm{cells}}^{2/3})$ (§4, App. B). **Stated**
9. The static-cell algorithm (Alg. 3) puts the time-integration loop outside the per-cell loops, so each loop becomes a kernel over all $N_C$ cells. Finished cells are frozen by multiplying their sources by an indicator $F_i\in\{0,1\}$ (Eq. 13). The extra arithmetic is acceptable when the GPU is undersaturated (§5.1). **Derived** (algorithm design)
10. The adaptive-cell algorithm (Alg. 4) compacts the active cells every $UF$ iterations when $N_{CNR}<N_{CA}$ and $N_{CA}>N_{\mathrm{sat}}$, and hands over to the CPU when $N_{CA}\le N_{\mathrm{CPU}}$. With $N_{\mathrm{CPU}}=-1$, $N_{\mathrm{sat}}=\infty$ it recovers the static GPU algorithm, and with $N_{\mathrm{CPU}}=\infty$ the conventional CPU one (§5.2, Table 1). **Derived**
11. For very few reacting cells ("e.g. 5–10") the CPU integrates the chemistry faster than the GPU (§5.2). **Stated**
12. Weak scaling from $6\times10^6$ to $6.4\times10^9$ cells (6 to 6144 GPUs, 1,048,576 cells per GPU) is near-ideal up to 3072 GPUs. Beyond that the compute time grows by about 50%, attributed to MPI transfer costs (§6.3, Fig. 8). **Shown**
13. Strong scaling is ideal over a range of GPU counts for each grid, and drops off below the saturation limit of $2\times10^5$ cells per V100 (§6.3, Fig. 8). **Shown**
14. A single GPU holds at most about $8.4\times10^6$ cells. The saturated throughput regime of the chemistry kernel can start "as low as 1000 cells" (§6.3, Fig. 9). **Shown** and **Stated**
15. In the roofline, most kernels have arithmetic intensity below 1 and lie near the bandwidth limit. The chemical-source and energy-to-temperature kernels exceed 1 and reach near-peak FLOPS (§6.3, Fig. 9). **Shown**
16. Cost split (Table 2): the detonation engine (1176 GPUs, 8232 CPUs, 312 M cells) spends 57.7% in the fluid and 42.3% in the reaction advance; the scramjet (300 GPUs, 2100 CPUs, 41 M cells) spends 66.5% and 33.5%. **Shown**
17. In the rotating detonation engine two co-rotating detonation waves travel at 1357 m/s (267 g/s, equivalence ratio 1.16), and the flow chokes at the chamber exit. A 25° sector is refined from 200 µm to 20 µm ("near-DNS") (§6.1, Fig. 5). **Shown**
18. In the 1D detonation tests at $\nu=0.2$, all three mechanisms run at time steps of about 6 ns. The stiffness ratio is of order $10^2$ for H2/air and CH4/O2 and about $10^4$ for RP2 (§6.4, Fig. 11). **Shown**
19. The speedup of the adaptive-cell over the static-cell algorithm grows "at constant rate" with the cells per GPU. It is larger for more complex mechanisms and its slope increases with stiffness (§6.4, Fig. 12). **Shown** (graphically only)
20. At turbulent Mach 0.3, $\mathrm{Re}_\lambda=30$, the skew-symmetric central scheme on the structured mesh tracks the spectral solution well. HLLC is closer to it than AUSMDV, which "adds additional numerical dissipation even at the turbulent Mach number of 0.3". Unstructured meshes deviate more and show small-scale energy pile-up (App. A.1, Figs. A.13–A.14). **Shown**
21. At turbulent Mach 0.6, $\mathrm{Re}_\lambda=100$ (eddy shocklets), both shock-capturing fluxes are much more dissipative than the central scheme in enstrophy and dilatation, and the HLLC–AUSMDV gap narrows. Mesh structure matters little compared with the scheme's own dissipation. A hybrid central/HLLC scheme is postulated to be beneficial (App. A.2, Figs. A.15–A.16). **Shown**, plus a **Stated** suggestion
22. "More than a petaflop of measurable performance was achieved using a fraction of the GPUs present on the SUMMIT machine" (§7). **Stated** (no measurement in the body)
23. The one-dimensional projection between neighbouring cell centres need not pass through the face centre, which is a source of error on skewed cells (§3). **Stated**

# Printed slips

- Eq. (10), $\partial Q_c/\partial t+\sum_jF_jA_j+\sum_jG_jA_j=0$, lacks the $1/V$ factor in front of the face sums.
- Eqs. (8)–(9): with $+\partial G/\partial x$ and $G=(0,\tau_{lj},\alpha\partial_{x_j}T+\tau_{lj}u_l,\rho D\partial_{x_k}Y_k)$, the viscous and diffusive terms take the opposite sign to Eqs. (2), (5) and (6). The species row reuses the species index $k$ as a spatial index.
- Eq. (12), $dT_i/dt=-\sum_k\frac{Y_{i,k}}{c_{v,k}}\sum_k\frac{\epsilon_k}{W_k}\Omega_{i,k}$: since $\Omega_k$ is a mass rate per unit volume (Eq. 11), the product has units K kg m⁻³ s⁻¹ (with the mass-based $c_{v,k}$ of the text) and lacks a factor $1/\rho$. The constant-volume energy balance gives $dT/dt=-\big(\rho\sum_kY_kc_{v,k}\big)^{-1}\sum_k(\epsilon_k/W_k)\Omega_k$, and $\sum_kY_k/c_{v,k}\ne1/\sum_kY_kc_{v,k}$ for more than one species. *(compiler check, not in the sources)* The paper replaces Eq. (12) by a Newton solve in practice.
- Algorithm 2, step b.3: "$T_{guess}=T-(e-e_{guess,T})/dEdT$" with $dEdT=e(T_{guess}+1)-e(T_{guess})>0$. A Newton step for $e(T)=e$ is $T_{guess}\leftarrow T_{guess}+(e-e_{guess,T})/dEdT$, so the printed form has the opposite sign and an undefined $T$. *(compiler check, not in the sources)*
- Algorithm 4: step l-1 is labelled "Device-to-host" but sends data "from CPU to GPU", and step l-3 is labelled "Host-to-device" but sends "from GPU to CPU". Step m) refers to a non-existent step "k-1-1".
- Code listings (§4):
  - `magSqrU[j] =+ ...` assigns rather than accumulates;
  - the wrapper's parameter is `Ncell` but the body uses `Ncells`;
  - `loopOverFaces` launches `loopOverCells_d`;
  - several kernels use undefined arguments;
  - `threadSafeAdd` is passed a value where it takes a pointer;
  - the text writes "facePerCell, cell2Fave".
- App. B: `boundaryContribution_atomic` is launched with 6 arguments, but its definition takes 7. A boundary-face routine is commented as handling "an internal face value".
- §6.1 says the engine mesh has "118 million cells", while Table 2 gives 312 M.
- The Fig. 4 caption keeps an editorial note: "– join the two into one figure."
- App. A.2 points to Fig. A.14 for the turbulent-Mach-0.6 spectrum, which is Fig. A.16.
- The viscous terms are attributed to a "KNP formulation" [35], whose printed title is "Implementation of semi-discrete, non-staggered central schemes in a colocated, polyhedral, finite volume framework, for high-speed viscous flows".
- "cuBLAS [25]", where [25] is clBLAS.
- Name misspellings: "Gorbets and Bakhvalov [42]" (Gorobets in the list); "Modesti an Pirozzol [57]" (twice).
- The molecular weight is $M_k$ in Eq. (7) and $W_k$ in Eq. (12) and Alg. 3.

# Notation map

| Bielawski et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u_j$ | $v_j$ | velocity |
| $e$ | kept locally ("total chemical energy" per unit mass) | **not the registry's specific internal energy $e$; the registry's $E$ is per unit volume** |
| $h=e+p/\rho$ | $H$ | total enthalpy including chemical energy |
| $\alpha$ | $\lambda_{\mathrm{th}}$ | thermal conductivity; **collides with $\alpha_k$ and the DG–FV blending $\alpha$** |
| $Y_k$, $N_S$ | $Y_k$ | mass fractions; agrees |
| $\Omega_k$, $M_k$/$W_k$, $\nu'_{k,l}$, $\nu''_{k,l}$ | kept | production rate, molecular weight, stoichiometric coefficients; **$\nu$ is the CFL number in the registry** |
| $\epsilon_k$ | kept | species molar internal energy; **collides with the WENO $\epsilon$** |
| $Q$, $F$, $G$ | $u$, $f$, viscous flux | **$G$ is the admissible set in the registry** |
| $Q_c$, $A_j$, $N_f$, $S_f$ | $\bar u_i$, face area, face count, area vector | polyhedral cells; owner $P$, neighbour $N$ |
| $F_i$ | kept | reaction-progress indicator; **collides with the flux $F$** |
| $N_C$, $N_{CR}$, $N_{CNR}$, $N_{CA}$, $N_{\mathrm{sat}}$, $N_{\mathrm{CPU}}$, $UF$ | kept | parameters of the chemistry algorithms |
| $M_{t,0}$, $Re_{\lambda,0}$ | $M_t$, $\mathrm{Re}_\lambda$ | initial turbulent Mach and Taylor Reynolds numbers |

# Reference list

There are 58 printed references in numbered style ([1]–[58]), with no DOIs
printed. All are parsed and merged complete into the
[bibliography](/bibliography.md) with `citedby` `bielawski-2023`. The list prints
two duplicates: [26] = [43] (Barwey & Raman 2021, Energies) and [27] = [36]
(Weller et al. 1998). Each pair is folded into one entry (`barwey-2021`, `weller-1998`). Undated or corporate items are [13] (CUDA guide,
2022), [25] (clBLAS), [44] (Summit specifications, citing year) and [14] (MPI
Forum). [47] is a personal communication. No item was unparseable.

# Pages created or updated

Chunk 5 (2026-10-23), cited further in chunks 6–7 (2026-10-23). This source is cited on:

* [Central-upwind schemes](/methods/central-upwind-scheme.md)
* [Decaying compressible isotropic turbulence](/benchmarks/compressible-isotropic-turbulence.md)
* [Gradient reconstruction on unstructured meshes](/methods/unstructured-gradient-reconstruction.md)
* [HLL-family approximate Riemann solvers](/methods/hll-riemann-solvers.md)
* [Hybrid central-WENO schemes](/methods/hybrid-weno.md)
* [Multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [OpenFOAM-based compressible solvers](/software/openfoam.md)
* [Operator splitting for stiff source terms](/methods/operator-splitting.md)
* [PyFR](/software/pyfr.md)
* [Shock-induced combustion and detonation](/benchmarks/shock-induced-combustion.md)
* [Split convective forms](/methods/split-convective-forms.md)
