---
type: Source
title: "Shankar et al. (2023) — GRaM-X: A new GPU-accelerated dynamical spacetime GRMHD code for Exascale computing with the Einstein Toolkit"
description: "Code paper of GRaM-X, a C++ dynamical-spacetime GRMHD code for the Einstein Toolkit that runs on GPUs through the CarpetX driver on AMReX, with Z4c spacetime, Valencia GRMHD, HLLE fluxes, a three-stage primitive-recovery chain, tabulated nuclear EOS in unified memory, device-resident data and block-structured AMR without subcycling; verified on relativistic shock tubes, a cylindrical explosion, the relativistic rotor and a magnetized TOV star, with up to 0.47e8 zone-cycles/s on one V100 and 40-50% weak-scaling efficiency at 2304 Summit nodes relative to one node."
resource: "doi:10.1088/1361-6382/acf2d9"
source_kind: paper
authors: [Shankar S., Mösta P., Brandt S.R., Haas R., Schnetter E., de Graaf Y.]
year: 2023
venue: "Class. Quantum Grav. 40:205009"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2023-CQG-Shankar-1010881361-6382acf2d9.pdf"
tags: [software, mhd, relativity, gpu, amr, primitive-recovery, equation-of-state, performance, scaling, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

GRaM-X (General Relativistic accelerated Magnetohydrodynamics on AMReX) is
a dynamical-spacetime GRMHD code for the Einstein Toolkit, a C++ redesign
of GRHydro. It runs on CPUs and GPUs through the new Cactus driver CarpetX,
which delegates block-structured AMR, GPU kernel launches, MPI and OpenMP
to AMReX (abstract, §I, §III). The Einstein equations are evolved in the
Z4c formulation by finite differences on vertices, ideal GRMHD in the
Valencia formulation by finite volumes on cells, coupled by a fourth-order
interpolation of the fluid to vertices (§II A–B). The fluid solver uses TVD
minmod or WENO5 reconstruction, HLLE fluxes, RK2 or RK4 method of lines, a
3D Newton–Raphson → Newman → temperature-bisection recovery chain, and
analytic or tabulated nuclear EOSs (§II C). All data stay on the device; one
global time step serves all levels, so refluxing is not needed (§III A,
§III C). Tests: Balsara relativistic shock tubes, a cylindrical explosion,
the relativistic rotor and a magnetized TOV star in dynamical spacetime
(§IV). Performance on Summit V100s: up to $0.47\times10^8$ zone-cycles/s on
one GPU, and about 40–50% weak-scaling efficiency at 2304 nodes relative to
one node, limited by ghost-zone communication (§V). Merged into
[GRaM-X](/software/gram-x.md).

# Key claims

1. **Formulation** (§II A–B, eqs. 1–13). Z4c with 1+log slicing and a
   Γ-driver shift, constraint-damping parameters 0.02 and 0.0; other thorns
   see only ADM variables. Valencia GRMHD in flux-conservative form with
   conserved $D$, $S_i$, $\tau$ and the densitized field (eqs. 6–12).
2. **Mixed staggering** (§II B, §II C). Fluid as cell averages, spacetime
   and stress–energy tensor on vertices; fluid at vertices by a fourth-order
   symmetric 3D interpolation; metric at faces by linear interpolation from
   vertices. Second-order interpolation gave "even larger, unacceptable
   amplitudes of oscillations" (§IV D).
3. **Fluid solver** (§II C). Primitive recovery, TVD minmod or WENO5
   reconstruction, HLLE, flux divergence plus sources. Only HLLE is
   implemented; Roe and Marquina are planned because "methods which are
   compute intensive but not memory intensive add little extra cost on
   GPUs" (asserted).
4. **Primitive recovery** (§II C). 3D Newton–Raphson in $(W,
   \rho h_{\mathrm{rel}}W^2, T)$, then Newman & Hamlin, then bisection in
   temperature, justified by "the number of EoS calls is ∼ 20 times larger
   in case of Newman's method compared to 3D-NR" (citing Siegel et al.
   2018). Failure modes: non-convergence, negative density or pressure,
   speed above $c$, leaving the table.
5. **EOS** (§II C). Polytropic, $\gamma$-law, and a tabulated nuclear EOS
   with 19 quantities in $(\rho, T, Y_{\mathrm e})$, stellarcollapse.org
   format, loaded into unified memory.
6. **Framework** (§III). Cactus with CarpetX over AMReX; Silo and openPMD
   (ADIOS2) I/O; AMReX inter-level operators extended to higher-order
   templated stencils; "All of CarpetX's basic operations are fully GPU
   enabled"; GPU back ends CUDA, HIP, SYCL; NSIMD vectorization on CPUs.
7. **AMR** (§III A). Berger–Oliger block-structured, $r_{\mathrm{ref}} = 2$,
   proper nesting, typical $N_{\mathrm b} = 8$; **no subcycling**, "for
   simplicity" and because "Subcycling in time necessarily serializes
   evolving different refinement levels" (asserted; no AMR performance
   run).
8. **Conservation across levels** (§III C). Fine fluxes restricted to
   coarse faces; "As we are using a global time step, so-called refluxing
   is not necessary."
9. **Staggering** (§III B, Fig. 1). An edge-centred vector potential keeps
   $\nabla\cdot\mathbf B$ zero to round-off, "in particular near mesh
   refinement interfaces"; the algorithm itself is not described.
10. **Device residency** (§III C). "All data are stored on the
    accelerator's built-in memory at all times, and are moved from and to
    the CPU memory only for I/O"; no compute–communication overlap yet
    (§V B).
11. **Unsupported claim** (§VI). "10 times faster and computational cost 30
    times lesser compared to traditional CPU-based codes", without any CPU
    measurement in the paper.

**Tests** (§IV, on one NVIDIA RTX A6000 unless stated; comparisons visual).
Balsara relativistic MHD shock tubes 1–5 at 1600 cells, RK4, $\nu = 0.8$,
TVD + HLLE (Table I, Figs. 2–3; test 3 undershoots at the fast shock);
weak-field Komissarov cylindrical explosion at $200^2$, $t = 4$ (Fig. 4; see
[MHD blast wave](/benchmarks/mhd-blast-wave.md));
[relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md) at
$400^2$, maximum $W$ about 1.85 at $t = 0.4$ (Fig. 5); magnetized TOV star
with four AMR resolutions, "convergence order of ∼ 2" of the central-density
oscillations and mode frequencies matching perturbation theory except H3
(Fig. 6). **Performance** (§V, Tables II–III, Figs. 7–8): zone-cycles/s with
a full RK step counted as one cycle; single V100 $0.47\times10^8$ (static
spacetime, ideal gas, RK2), $0.26\times10^8$ (tabulated EOS, RK4),
$0.062\times10^8$ (dynamical spacetime); weak-scaling efficiency 0.40 and
0.49 at 2304 nodes (13,824 GPUs) relative to one 6-GPU node; strong-scaling
efficiency 0.19 at 1000 nodes relative to 8 nodes. Precision not stated.

# Notation map

| Shankar et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $P$, $\epsilon$ | $\rho$, $p$, $e$ | |
| $h = 1 + \epsilon + P/\rho$ | $h_{\mathrm{rel}}$ | **collision:** bare $h$ is the cell size |
| $h^* = 1 + \epsilon + (P + b^2)/\rho$ | words ("magnetized enthalpy") | not in the registry |
| $P^* = P + b^2/2$ | words | registry $P^*$ is the Newtonian $p + \tfrac12 B^2$; here the comoving field enters |
| $u^\mu$, $b^\mu$ | words | **collision:** bare $u$ is the conserved state; no registry symbol for the comoving field |
| $T^{\mu\nu}$, $F^{\mu\nu}$, $J^\mu$, $g_{\mu\nu}$, $\Gamma^\lambda_{\mu\nu}$ | words | not in the registry; $J^\mu$ vs registry $\mathbf J$ (current density), $T^{\mu\nu}$ vs temperature $T$ |
| $\alpha$, $\beta^i$, $\gamma_{ij}$ | $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | |
| $K_{ij}$ | words ("extrinsic curvature") | collides with the polytropic $K$ |
| $\gamma = \det\gamma_{ij}$ | words | **collision:** registry $\gamma$ is the adiabatic index |
| $\Gamma$ (ideal-gas index), $\gamma$ (polytropic exponent) | $\gamma$ | the paper uses two letters for the exponent of its two analytic EOSs |
| $K$ (polytropic constant) | words | |
| $W$ | $W$ | |
| $v^i$, $\tilde v^i = v^i - \beta^i/\alpha$ | $\mathbf v$, words | |
| $D$, $S_j$, $\tau$ | $D$, $S_i$, $\tau$ | |
| $B^i$, $\mathscr B^k = \sqrt\gamma B^k$ | $\mathbf B$, words | units as printed |
| $\mathbf U$, $\mathbf F^i$, $\mathbf S$ | $u$, $\mathbf f$, $s(u)$ | |
| $\mathbf P$ (primitive vector) | words | **collision** with pressure |
| $z = \rho h W^2$; Newman's $\epsilon \equiv B^2 + z$ | $\rho h_{\mathrm{rel}}W^2$; words | Newman's $\epsilon$ is not the internal energy |
| $T$, $Y_e$, $c_s$ | $T$, $Y_{\mathrm e}$, $c_s$ | |
| $\kappa_1$, $\kappa_2$; $\mu_L$, $\mu_S$, $\eta$ | words | **collisions** with opacity $\kappa$, mean molecular weight $\mu$, $\eta_1$, $\eta_2$ |
| $A_i$, $A_\varphi$ | words ("vector potential") | not in the registry |
| $\Delta x$; CFL factor $\Delta t/\Delta x$ | $h$; $\nu$ | |
| "half the spacing"; block $8^3$; 3 ghost zones | $r_{\mathrm{ref}} = 2$; $N_{\mathrm b} = 8$; $n_{\mathrm g} = 3$ | |
| $n_{\rm iter}$, $n_{\rm cells}$, $n_{\rm GPU}$, $t$ (wall time) | words | |

# Pages created or updated

* Created [GRaM-X](/software/gram-x.md),
  [Relativistic magnetic rotor](/benchmarks/relativistic-magnetic-rotor.md).
* Updated [Primitive-variable recovery in relativistic MHD](/methods/primitive-variable-recovery.md),
  [GAMER](/software/gamer.md), [CASTRO](/software/castro.md).
* Per the batch-3 page plan, also cited on
  [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md),
  [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md),
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) and
  [MHD blast wave](/benchmarks/mhd-blast-wave.md) (drafted by other
  drafters; the compiler confirms the final list).
* Also cited on (batch 3) [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md), [Constrained transport](/methods/constrained-transport.md).
* Also cited on (batch 4) [H-AMR](/software/h-amr.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2023-CQG-Shankar-1010881361-6382acf2d9.pdf`.
   * **Version.** arXiv:2210.17509v2 [astro-ph.IM], 21 Nov 2022 (header
     "Dated: 2022-10-31"), 22 pages; the archive filename names the CQG
     article, but the file is the arXiv v2 preprint. Differences from the
     version of record were not checked; all section, equation, table and
     figure numbers refer to v2. No repository URL, code version or
     licence is printed.
   * **Identity.** doi:10.1088/1361-6382/acf2d9, checked on Crossref (title
     and the six authors match page 1): Class. Quantum Grav. 40(20):205009,
     online 2023-09-19, issue 2023-10-19.
   * **How it was read.** Text extraction of all sections; the Valencia
     equations (eqs. 6–13), the TOV vector potential and Tables I–II read
     on the rendered pages, where the text layer garbles the magnetized
     enthalpy. Figure values beyond those stated in the text were not
     transcribed.
   * **Recorded as printed.** The rotor's 1D cuts are compared with
     "Fig. 8" of the GRHydro paper in the text and "Fig. 6" in the Fig. 5
     caption. The TOV central density is printed as
     "1.28 × 10⁻³ M_⊙". §III cites Bona et al. (1998), a
     numerical-relativity paper, for the Cactus framework being in use
     since 1998. H-AMR's single-GPU rate ($0.85\times10^8$) is called
     "comparable" to GRaM-X's best $0.47\times10^8$. Table I lists the
     specific internal energy, not the pressure. Weak-scaling efficiency
     is relative to one node, whose per-GPU rate is already below the
     single-GPU rate.
   * **Reference list:** 77 printed entries. GRHydro (printed with years
     2014 and 2013, merged as `mosta-2014`), Antón et al. (2006), Liska et
     al. (H-AMR) and the AMReX documentation (`amrex-2022`) are each
     printed twice and merged once; H-AMR's arXiv preprint is merged into
     its ApJS 2022 publication (`liska-2022`). The single-author Harten
     (1983) J. Comput. Phys. paper is keyed `harten-1983-b`, distinct from
     `harten-1983` (Harten, Lax & van Leer, SIAM Rev.); the printed Balsara
     (2001) ApJS paper is `balsara-2001-b`. Undated web references take the
     citing date (2022).
