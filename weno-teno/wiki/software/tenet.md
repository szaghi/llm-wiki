---
type: Software
title: "TENET"
description: "TENET is a modal discontinuous Galerkin code for astrophysical compressible flow; its GPU rewrite TENETGPU solves the Euler and Navier–Stokes equations on uniform Cartesian meshes with MPI and CUDA, a time-evolved artificial viscosity instead of slope limiting, recovery-based viscous fluxes, and scales to 64 A100 GPUs."
status: established
aliases: [TENETGPU, TENET GPU]
tags: [software, gpu, dg, artificial-viscosity, turbulence]
timestamp: 2026-10-23T23:45:00Z
---

# TENET

TENET is a modal [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
code for the compressible Euler equations in astrophysics, due to Schaal
et al. (2015) and Guillet et al. (2019), as recalled by
[Cernetic et al. (2023)](/sources/cernetic-2023.md). The bundle's account
is that paper (accepted manuscript), which presents **TENETGPU**, a
rewrite from scratch in MPI-parallel C++17 with CUDA that adds the
Navier–Stokes equations and replaces the slope limiting of its CPU
predecessor by an [artificial viscosity](/methods/artificial-viscosity.md).
The authors call it "the first" astrophysical GPU code able to carry out
DG calculations of the full Navier–Stokes equations at order 10 and
beyond (§10).

## Discretization

- **Basis.** Orthonormal tensor products of scaled Legendre polynomials,
  truncated at total degree $N$: $(N+1)(N+2)(N+3)/6$ functions per cell
  in 3D, $(N+1)(N+2)/2$ in 2D, design order $N+1$ (§2.3, Eqs. 13–18).
  The mesh is uniform and Cartesian.
- **Quadrature.** Gauss points, $N+1$ per direction, more than polynomial
  integrands need, because the flux integrands are rational functions of
  the state (§2.4).
- **Interface flux.** A simplified HLLC solver taken from the AREPO code
  ([HLL-family solvers](/methods/hll-riemann-solvers.md)), and an exact
  Riemann solver for an isothermal equation of state (§2.2).
- **Time stepping.** The strong-stability-preserving Runge–Kutta rules
  of Schaal et al., with the order raised with the spatial order, up to
  five stages and fourth order
  ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)); time step
  $\Delta t=f_{\mathrm{CFL}}\,\Delta x/\big(2(N+1)(c_{\max}+\lvert v\rvert_{\max})\big)$
  with $f_{\mathrm{CFL}}=0.5$, 0.3 for the shock-tube and blast-wave tests (Eq. 23; page-local
  $f_{\mathrm{CFL}}$; the source writes $p$ for the order).
- **Viscous terms.** Interior gradients are those of the cell polynomial;
  interface gradients come from an $L^2$ projection of the two adjacent
  cell polynomials onto one polynomial of degree $N+1$ in the normal
  direction on a domain straddling the face, after van Leer and Nomura's
  recovery. BR1 lifting was implemented first and dropped as costly and
  not robust with large jumps (§3).
- **Shock capturing.** A viscosity field carried as an extra DG
  component, driven by compression and by the growth rate of the
  Persson–Peraire sensor and decaying on the time scale
  $f_\tau\Delta x/((N+1)c)$, not advected; no slope limiter (§4.1;
  [artificial viscosity](/methods/artificial-viscosity.md),
  [troubled-cell indicator](/definitions/troubled-cell-indicator.md)).
  A positivity limiter at all volume and surface quadrature points is the
  last line of defence (§4.2;
  [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).
- **Forcing.** Solenoidal Ornstein–Uhlenbeck forcing of the modes with
  $2\pi/L\le k\le4\pi/L$ for driven turbulence, with an ideal gas whose
  temperature is reset every step to emulate isothermality, so that HLLC
  can replace the slower isothermal solver (§7.1).

## Implementation

The domain is decomposed into slabs along $x$ of variable thickness;
neighbouring slabs exchange surface states or fluxes at the Gauss
points, overlapped with the volume integrals. Each GPU is driven by one
host core, the data stay on the device, and pinned host memory serves
input and output. Legendre and quadrature data sit in constant memory and
reductions in shared memory; when intermediates overflow shared memory,
quadrature points are processed in batches. Races are avoided without
locks by red–black checkerboard ordering, and the summation order at the
periodic wrap-around is fixed, so results are binary identical under
changes of the slab count. CPU and GPU kernels can be mixed per slab and
give the same results. No OpenACC or GPU library is used (CUDA 11.4,
g++ 11, OpenMPI 4, FFTW 3, GSL 2.4) (§8). The code is distributed on
Bitbucket.

**Memory.** With the viscosity field and the Runge–Kutta storage a run
holds $\big(3+d+f_t\big)N_x^d\,n_{\mathrm b}$ double-precision numbers,
with $N_x$ cells per direction, $n_{\mathrm b}$ basis functions per cell
and $f_t$ the order for orders up to 3 and 5 above (Eq. 62; page-local
symbols). No gradient fields are stored, unlike finite-volume codes such
as AREPO. One 40 GB A100 holds $128^3$ cells at degree 9 (37.81 GB,
Table 1).

## Performance

- **Weak scaling** from 1 to 64 A100 GPUs ($128^3$ to $512^3$, degrees
  0–5) is good, with losses at large sizes from thinner slabs, whose
  surface-to-volume ratio grows, and from inter-node communication over
  Omni-Path; it improves at higher order (§9.1, Fig. 20).
- **Strong scaling** at $256^3$ on 1–16 A100s and 1–256 Xeon-6138 cores:
  the CPU runs degrade from 16 to 32 cores because one 20-core socket
  saturates its memory bandwidth (checked with STREAM) and one-cell slabs
  communicate heavily (§9.2, Fig. 21).
- **GPU against CPU.** The node-level speedup (4 A100 against 40
  Xeon-6138 cores) peaks at "just over 8x", and one GPU is about 80 times
  one CPU core, close to the ratio of nominal double-precision peak
  performances (§9.3, Fig. 22).
- **Order against cells.** In viscous driven subsonic turbulence
  (Mach about 0.47) $64^3$ cells at order 4 reproduce the converged
  spectrum of $128^3$ at order 3, which $128^3$ at order 2 does not, and
  take 1.8 h on 16 A100s against 3.9 h, "about 2x faster" for the same
  converged result (§7.2.2, Fig. 19). On the viscous
  [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
  of Lecoanet et al. the $L^2$ dye error at 64 cells and order 4 equals
  that of ATHENA at 2048 cells (§6.3).

## Test problems

[Isentropic vortex](/benchmarks/isentropic-vortex.md) (orders 1–8,
design-order and exponential convergence), a Gaussian diffusion test of
the viscous flux, the [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md)
at 100 cells, supersonic top-hat advection over 100 crossings
([material-interface advection](/benchmarks/material-interface-advection.md)),
the viscous Kelvin–Helmholtz instability against DEDALUS, and driven
turbulence with and without physical viscosity (§5–§7).

## Qualifications

- The mesh is uniform and fixed, and the number of GPUs is capped by the
  number of cells per direction because of the slab decomposition (§8).
- The paper uses $p$ for the order ($p=N+1$, §2.3) but labels most
  figures and Table 1 by the degree; the memory formula reproduces
  Table 1 only with the degree. The node-level speedup sentence of §9.3
  reads "modest for order $p=2$ … At $p=2,3$ we reach the highest
  node-level speedup", which contradicts itself as printed.
- The resolution of the DEDALUS reference is printed $3096\times6144$ on a
  $1\times2$ domain, whose aspect ratio would give $3072\times6144$; the
  paper does not say which is meant.
- The time step scales as $1/(N+1)$; the paper does not compare it with
  other DG time-step scalings.

# Citations

- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — accepted manuscript: §1; §2.2–2.5, Eqs. (13)–(23); §3; §4.1–4.2; §5–§7, Figs. 5–19; §8, Eq. (62), Table 1; §9, Figs. 20–22; §10.
