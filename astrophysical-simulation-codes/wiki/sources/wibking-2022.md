---
type: Source
title: "Wibking & Krumholz (2022) — Quokka: A code for two-moment AMR radiation hydrodynamics on GPUs"
description: "Presents Quokka, a GPU-native subcycled block-structured AMR code on AMReX: RK2-SSP method-of-lines hydrodynamics with PPM, Miller–Colella flattening and HLLC; gray two-moment radiation under a reduced speed of light with a pluggable local closure, HLL fluxes and per-level radiation subcycling; a Newton–Raphson matter–radiation exchange; 18 verification tests, V100/A100 throughput and scaling, and a derivation that the reduced speed of light shifts closed-box equilibria."
resource: "doi:10.1093/mnras/stac439"
source_kind: paper
authors: [Wibking B.D., Krumholz M.R.]
year: 2022
venue: "Mon. Not. R. Astron. Soc. 512:1430–1449"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2022-MNRAS-Wibking-101093mnrasstac439.pdf"
tags: [software, radiation, reduced-speed-of-light, amr, gpu, riemann-solver, time-integration, performance, scaling, verification, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Quokka is a new block-structured, subcycling-in-time AMR radiation
hydrodynamics code built on AMReX and designed for GPUs from the start;
the authors claim it is the first code with two-moment AMR radiation
hydrodynamics on GPUs (§1.2). Hydrodynamics uses a method of lines
(RK2-SSP, PPM or PLM on primitive variables, Miller–Colella
multidimensional flattening, HLLC). Radiation uses the gray mixed-frame
two-moment equations with a reduced speed of light, a local Eddington
tensor (Levermore by default, Minerbo optional), HLL fluxes with
frozen-Eddington-factor wave speeds, explicit transport subcycled within
each AMR level, and a local Newton–Raphson matter–radiation exchange after
Howell & Greenough (2003) (§2). Explicit radiation is chosen for GPU
arithmetic intensity, simple memory access and control flow and the
absence of global communication (§1.2, §2.2.2). The code is checked on
9 hydrodynamic, 5 radiation and 4 coupled tests (§3); single-GPU
throughput exceeds 250 million cell updates per second for PPM
hydrodynamics on an A100, and weak-scaling efficiency is about 76–83 %
from 4 to 256 V100 GPUs (§4). The paper also derives that the reduced
speed of light shifts the closed-box gas–radiation equilibrium whenever
$\hat c \neq c$ (§3.2.3). Merged into [Quokka](/software/quokka.md),
[M1 radiation transport](/methods/m1-radiation-transport.md),
[reduced speed of light](/definitions/reduced-speed-of-light.md),
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), the
[radiation shadow test](/benchmarks/radiation-shadow-test.md) and the
[subcritical radiative shock](/benchmarks/subcritical-radiative-shock.md).

# Key claims

1. **Equations** (§2.1, eqs. 2–17). Inviscid, non-relativistic LTE
   radiation hydrodynamics in the mixed frame without scattering; the
   four-force is kept to first order in $\vert\mathbf v\vert/c$, and the
   "relativistic work term" is dropped because it matters only where the
   reduced speed of light cannot be used. $\hat c$ enters as
   $\partial_t E_{\mathrm r} + \nabla\cdot(\frac{\hat c}{c}\mathbf F_{\mathrm r})$
   and $\partial_t\mathbf F_{\mathrm r} + \nabla\cdot(c\hat c\,\mathsf P_{\mathrm r})$
   with $\hat c$ times the four-force on the right (eqs. 11–12). Flux-mean
   opacity taken as Rosseland, energy-mean as Planck. With $\hat c\neq c$
   neither energy nor momentum is conserved.
2. **Splitting** (§2.2, §2.2.3). Explicit hydro step, subcycled explicit
   radiation transport, local implicit coupling once per radiation
   subcycle.
3. **AMR** (§§2.2, 2.2.4). Berger–Oliger / Berger–Colella on AMReX
   `AMRCore`; $r_{\mathrm{ref}} = 2$ only; $\Delta t_l = \Delta t_0/2^l$;
   linear conservative interpolation, conservative average-down,
   flux-register synchronization. Radiation is subcycled within each
   level, at most a set number of substeps per level step (default 10),
   with coarse–fine flux mismatch added to adjacent coarse cells; a
   maximum of 1 reproduces RAMSES's flux synchronization.
4. **Time step** (§2.2.1, eqs. 18–21). $\Delta t = \nu h/\max(\vert\mathbf v\vert + c_s)$
   with the CFL number defined as a stability coefficient over $d$; the
   maximum stable value for RK2-SSP in 3D is $1/3$. The method of lines
   with higher-order reconstruction is unstable with forward Euler (as in
   Stone et al. 2020).
5. **Reconstruction and flattening** (§2.2.1, eq. 22, footnote 4).
   Symmetrically regrouped PPM on primitives with neighbour clipping and
   linear reversion at extrema; PLM-MC option; Miller & Colella (2002)
   flattening, no artificial viscosity.
6. **Riemann solvers** (§§2.2.1, 2.2.2). HLLC (primitive-variable wave
   speeds) for gas, carbuncle not fixed; HLL for radiation with wave speeds
   from Eddington factors frozen at the start of the step (Balsara 1999),
   so any closure can be used.
7. **Closure** (§2.2.2, eqs. 23–25). Levermore (M1 form), Minerbo option,
   any $f_{\mathrm r}\mapsto\chi_{\mathrm E}$ map pluggable; reconstruction
   of $E_{\mathrm r}$ and the reduced flux vector; causality rescaling for
   the closure; optically thick Riemann correction disabled where it
   violates causality.
8. **Implicit exchange** (§2.2.3, eqs. 26–43). Newton–Raphson on two
   residuals, tolerance $10^{-10}$ (to $10^{-15}$ for stiff problems), at
   most 400 iterations; backward-Euler flux absorption; momentum and work
   transfer after Skinner et al. (2019).
9. **Reduced-speed-of-light equilibrium shift** (§3.2.3, eqs. 57–58).
   With a heat capacity proportional to $T^3$, a closed box conserves
   $\rho e + (c/\hat c)E_{\mathrm r}$, so its equilibrium temperature
   depends on $\hat c$, "contrary to previous claims in the literature"
   (claims not identified); about 20 % high at $\hat c = 0.1c$; "a generic
   failing" of the approximation. Open boundaries that do not conserve that
   combination still reach the correct steady state (§3.3, §5.1).
10. **Applicability** (§5.1). $\hat c$ must exceed the fastest
    radiation-driven fronts in streaming and about $c$ over the optical
    depth in diffusion; no constant $\hat c$ preserves the ordering of
    hydrodynamic, diffusion and reduced light speeds everywhere (after
    Skinner & Ostriker 2013).
11. **Software quality** (§3, §3.1.9). 20 automated tests and SonarQube
    on every commit; exact $x$–$y$ symmetry on NVIDIA GPUs needs
    `fmad=false` and symmetric RK2-SSP flux sums.
12. **Performance** (§4, Tables 1–5). See the tests summary.

# Tests summary

* **Hydrodynamics** (§3.1, radiation off). 1D sound wave after Stone et
  al. (2008), PPM, CFL 0.1: L1 error $1.0\times10^{-7}$ ($N = 16$),
  $1.6\times10^{-9}$ (128), $1.7\times10^{-11}$ (1024), second order
  (Fig. 1). Stationary contact: error exactly zero. Stationary shock tube
  (1000 cells): relative L1 error $1.12\times10^{-3}$ (Fig. 2). LeBlanc
  shock tube (2000 cells): correct shock position, small overshoot (Fig.
  3). Shu–Osher at 400 cells against an Athena++ 1600-cell reference
  (Fig. 4). Slow-moving shock: residual oscillations (Fig. 5). Einfeldt
  1-2-3 rarefaction (Fig. 6). Kelvin–Helmholtz with 4 AMR levels on a
  $2048^2$ base, one GPU, about 4.5 h (Fig. 7, qualitative).
  Liska–Wendroff implosion at $1024^2$, exactly symmetric (Fig. 8,
  qualitative).
* **Radiation** (§3.2, hydro off). Marshak wave (Fig. 9), Su–Olson (Fig.
  10), radiation–matter exchange with $\hat c = c$ and $0.1c$ (Fig. 11),
  shadow test (Fig. 12, qualitative), beam (Fig. 13, qualitative).
* **Radiation hydrodynamics** (§3.3). Radiation pressure tube within
  0.2 % (Fig. 14); optically thin wind (Fig. 15); subcritical radiative
  shock with 0.4 % gas-temperature L1 error after drift correction (Fig.
  16); dust shell at $128^3$ (Fig. 17).
* **Performance** (§4). Gadi V100 nodes and one 4×A100 node; precision not
  stated; metric million cell updates per GPU per second. Hydro weak
  scaling to 256 GPUs: 82.76 % (PPM), 75.84 % (PLM) relative to one
  4-GPU node; RHD weak scaling 76.19 %; single A100 254.05 (Sedov PPM) and
  39.04 (RHD); AMR strong scaling 4→32 GPUs, 52.69 %.

# Notation map

| Wibking & Krumholz (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $E$, $c_s$, $\gamma$, $T$ | $\rho$, $\mathbf v$, $E$, $c_s$, $\gamma$, $T$ | same |
| $P$, $\mathsf P = \delta_{ij}P$ | $p$, $p\mathsf I$ | gas pressure |
| $c$, $\hat c$ | $c$, $\hat c$ | $f_c = \hat c/c$ |
| $E_r$, $\mathbf F_r$, $\mathsf P_r$ | $E_{\mathrm r}$, $\mathbf F_{\mathrm r}$, $\mathsf P_{\mathrm r}$ | |
| $\mathbf f = \mathbf F_r/(cE_r)$, $f$ | $\mathbf F_{\mathrm r}/(cE_{\mathrm r})$, $f_{\mathrm r}$ | the registry names only the magnitude |
| $\chi$, $\hat{\mathbf n}$ | $\chi_{\mathrm E}$, $\hat{\mathbf n}$ | |
| $\kappa_P$, $\kappa_R$, $\kappa_F$, $\kappa_E$ | $\kappa_{\mathrm P}$, $\kappa_{\mathrm R}$, $\kappa_{\mathrm F}$, $\kappa_{\mathrm E}$ | registry $\kappa$ with subscripts |
| $a_r$ | $a_{\mathrm r}$ | radiation constant; proposed registry row |
| $G^0$, $\mathbf G$ | words (four-force) | **collision:** registry $G$ is the gravitational constant |
| $\beta = v/c$ | $\vert\mathbf v\vert/c$ | **collision** with the shift $\beta^i$ |
| $B$ (Planck function) | words | **collision** with $\mathbf B$ |
| $\tau$, $\tau_{\mathrm{cell}}$ | words (optical depth, per cell) | **collision** with the Valencia $\tau$ |
| $E_g = E - \rho v^2/2$ | $\rho e$ | **collision:** registry $E_{\mathrm g}$ is a gravitational energy density |
| $E_0$, $E_{\mathrm{tot}}$ | $\rho e + (c/\hat c)E_{\mathrm r}$ | conserved combination |
| $C_v = \alpha T^3$ | words | $\alpha$ ambiguous with $\alpha_{\mathrm L}$, $\alpha_{\mathrm c}$ |
| $F_G$, $F_R$, $R$, $S$, $\epsilon$ | words | Newton residuals, exchange term, source, tolerance |
| $\Delta x$, $\Delta x_l$ | $h$, $h_l$ | |
| $l$, $\Delta t_l$ | $l$, $\Delta t_l$ | $r_{\mathrm{ref}} = 2$ |
| $D$ | $d$ | |
| $C_0$, CFL number $C_0/D$ | words; $\nu = C_0/d$ | **definition differs** from per-direction-minimum Courant numbers |
| $\lambda$ (signal speed) | words | **collision** with eigenvalues $\lambda^{(p)}$ |
| $U$ | $u$ | |
| $q_{j+1/2}$ | words (primitive interface value) | registry $u^\pm_{i+1/2}$ is a reconstructed state |
| $N_x$ | $N$ | |
| $N_{\mathrm{sub,max}}$ | words | maximum radiation substeps per level step |
| $\mathcal M$ | words (Mach number) | |
| $\mu$, $m_H$ | $\mu$, $m_{\mathrm H}$ | |

# Pages created or updated

* Created [Quokka](/software/quokka.md),
  [Radiation shadow test](/benchmarks/radiation-shadow-test.md),
  [Subcritical radiative shock](/benchmarks/subcritical-radiative-shock.md).
* Updated [M1 radiation transport](/methods/m1-radiation-transport.md),
  [Reduced speed of light](/definitions/reduced-speed-of-light.md),
  [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).
* Also cited, per the batch-3 page plan, on
  [Porting compressible-flow codes to GPUs](/methods/gpu-porting.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md),
  [Parallel scaling efficiency](/definitions/parallel-scaling-efficiency.md),
  [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
  [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Linear-wave convergence](/benchmarks/linear-wave-convergence.md),
  [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md), and,
  if created, [Liska–Wendroff implosion](/benchmarks/liska-wendroff-implosion.md),
  [Shu–Osher shock tube](/benchmarks/shu-osher-shock-tube.md) and
  [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md).
* Also cited on (batch 3) [CASTRO (compressible astrophysics code on BoxLib AMR)](/software/castro.md), [GAMER (GPU-accelerated octree AMR code), MHD extension](/software/gamer.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2022-MNRAS-Wibking-101093mnrasstac439.pdf`.
   * **Version.** arXiv:2110.01792v2 (30 Jan 2022), the accepted manuscript
     in MNRAS style ("Preprint 1 February 2022"), 21 pages, not the typeset
     article; section, equation, figure and table numbers are the
     preprint's. Repository linked as a hyperlink only
     (`https://github.com/BenWibking/quokka-code`); no code version.
   * **Identity.** doi:10.1093/mnras/stac439, checked on Crossref (title
     and both authors match): Mon. Not. R. Astron. Soc. 512(1):1430–1449,
     online 2022-02-18, print issue 2022-03-22.
   * **How it was read.** Text extraction, all sections; the text layer
     garbles display equations, so eqs. 2–17, 18–25, 26–38 and 56–58 were
     read on rendered pages 3, 4, 6 and 13; eqs. 59–60 and 62–65 are not
     reproduced. The LeBlanc pressures were checked on rendered page 8.
   * **Recorded as printed.** The sound-wave eigenvector $(1,-1,1,1,1.5)$
     has nonzero transverse velocity components, unusual for a sound wave
     from rest (§3.1.1). §3.3.3 refers to "Figure 11" for the Zel'dovich
     spike; the figure is Fig. 16. The Table 5 "Cells/GPU" column is the
     cube root of the cells per GPU (the text gives
     $211^3 \approx 9.4\times10^6$ at 32 GPUs). The abstract's "substantially
     faster than any other public RHD code" has no head-to-head
     measurement. Floating-point precision of the performance runs is not
     stated.
   * **Reference list:** 106 entries, no journal-article titles (MNRAS
     style); three printed DOIs. Same-stem works distinguished by
     journal, volume and page: `abel-2002-b`, `balsara-1999-b`,
     `mignone-2005-b`, `turk-2011-c`, `vanleer-1977-b`; the printed-order
     Krumholz et al. 2007 pair maps to `krumholz-2007-c` and
     `krumholz-2007`; Lecoanet et al. merges into `lecoanet-2015`. The
     citing list's Grete et al. 2019 (K-Athena, arXiv:1905.04341) is the
     work Stone et al. (2020) printed with year 2009; the entry was rekeyed
     `grete-2019` with a note.
