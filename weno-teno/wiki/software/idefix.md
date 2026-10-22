---
type: Software
title: "IDEFIX"
description: "Lesur et al.'s performance-portable C++17 Kokkos code for astrophysical hydrodynamics and non-ideal MHD: a second-order Godunov finite-volume scheme close to PLUTO, with primitive-variable reconstruction, HLL-family and Roe solvers, constrained transport, super time-stepping and orbital advection, running the same source on CPUs and GPUs."
status: established
aliases: [IDEFIX, Idefix]
tags: [software, gpu, mhd, finite-volume, riemann-solver]
timestamp: 2026-10-23T10:00:00Z
---

# IDEFIX

IDEFIX is a finite-volume Godunov code for non-relativistic
hydrodynamics and magnetohydrodynamics of astrophysical flows, written in
C++17 on the Kokkos performance-portability library, so that one source
compiles for Intel and AMD CPUs and for NVIDIA and AMD GPUs
([Lesur et al. (2023)](/sources/lesur-2023.md), arXiv proof-stage
version). It is a deliberate rewrite of the PLUTO design rather than a
port: the same reconstruct–solve–average algorithm, nearly identical
parameter files, variable names and VTK outputs (§1–§2). It runs on
Cartesian, polar/cylindrical and spherical grids with piecewise-function
spacing, without [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md),
and is distributed on GitHub under the CeCILL licence (§2.6, §3).

## Equations

Dimensionless MHD with gravity, viscosity, thermal diffusion, Ohmic and
ambipolar diffusion and the Hall effect, in units without $4\pi$
(magnetic pressure $\lvert B\rvert^2/2$), conserved variables
$(\rho,\rho v,B,E)$ with $E=\rho e+\tfrac12\rho\lvert v\rvert^2+\tfrac12\lvert B\rvert^2$
(§2.1, Eqs. (1)–(5)). Unlike PLUTO, the pressure is included in the
momentum flux and handled by the Riemann solver, which creates extra
pressure source terms in curvilinear geometry; IDEFIX and PLUTO results
are therefore "expected to differ, even if the same algorithm
combination is chosen" (§2.3). In polar and spherical geometry the
azimuthal conserved quantity is the vertical angular momentum, which
conserves angular momentum to machine precision (§2.6).

## Numerical method

- **Reconstruction** of primitive variables $(\rho,v,B,p)$ to faces,
  without [characteristic decomposition](/methods/characteristic-decomposition.md):
  flat (first order), piecewise linear with van Leer limiter, Čada and
  Torrilhon's LimO3, or extremum-preserving PPM (Colella–Woodward,
  Colella–Sekora), as named; no formulas are printed (§2.3). The code is
  "at most globally second order" whatever the reconstruction.
- **Riemann solvers**, run-time selectable and ordered "from most to
  least diffusive": Rusanov ([Lax–Friedrichs](/methods/lax-friedrichs-flux.md)),
  HLL, HLLC (HLLD in MHD) ([HLL-family solvers](/methods/hll-riemann-solvers.md))
  and the [Roe solver](/methods/roe-riemann-solver.md) (Cargo–Gallice for
  MHD) (§2.3).
- **Divergence control** by constrained transport on face-centred $B$
  with edge electric fields reconstructed by averaging, Gardiner–Stone
  $\mathcal E^0$ or $\mathcal E^c$ (default) or 2D HLL/HLLD Riemann
  solvers, and an optional vector-potential form against round-off
  accumulation ([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md); §2.4).
- **Non-ideal terms**: parabolic fluxes added to the hyperbolic ones to
  keep conservation; Ohmic and ambipolar terms also added to the edge
  field; the Hall effect by adding the whistler speed to the HLL Riemann
  fan for the magnetic-field fluxes only, HLL being "our only solver
  compatible with the Hall effect" (§2.5).
- **Time integration**: explicit Euler, or the two- and three-stage
  "total variation diminishing" Runge–Kutta methods of Gottlieb and Shu
  in Shu–Osher form, $U_s=w_sU^*+w^0_sU_0$ with weights
  $(1,0;\frac12,\frac12)$ and $(1,0;\frac14,\frac34;\frac23,\frac13)$
  (Eq. (9), Table 1; [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).
  Applied to a linear one-step operator $I+\Delta t\mathcal L$, these give
  second- and third-order Taylor polynomials *(compiler check, not in the
  sources)*.
- **Time step** combining hyperbolic and parabolic limits pointwise,
  $\Delta t=\sigma_{\mathrm{CFL}}\big(\max_{\mathrm{cells}}\sum_d[c_{\max,d}/\Delta x_d+2\eta_{\max}/\Delta x_d^2]\big)^{-1}$,
  $\sigma_{\mathrm{CFL}}<1$, without PLUTO's dimension factor
  (page-local $c_{\max,d}$, $\eta_{\max}$, $\sigma_{\mathrm{CFL}}$); the
  step "can be somewhat larger" than PLUTO's (§2.7, Eq. (10)).
- **Super time-stepping** for parabolic terms by second-order
  Runge–Kutta–Legendre, with
  $s_{\mathrm{RKL}}\simeq2\sqrt{\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}}$
  stages against $2\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}$ for
  explicit RK2, called alternately before and after the main integrator
  to keep second order (§2.8, Eqs. (11)–(13); page-local symbols).
- **Orbital advection** of Fargo type, conservative after Mignone et al.,
  and shearing-box boundaries (§2.9, §4.3).

## Implementation and performance

All data live in device memory as aliases of `Kokkos::View`, all loops
are `idefix_for` kernels, and the host handles only input/output,
initial conditions and exceptions; one device per MPI rank, GPU-aware
MPI, device-side packing, and a sequential, dimension-by-dimension
ghost-zone exchange found faster than a simultaneous 26-neighbour
exchange, especially on NVIDIA GPUs (no timings shown), though unsuited
to an AMR version (§3). On a 3D Orszag–Tang test (HLLD, linear
reconstruction, $\mathcal E^c$, RK2, double precision; Table 4, §5):

| Node | Throughput (Mcell/s) | Energy ($10^{10}$ cell/kWh, TDP proxy) |
|---|---|---|
| 2 × AMD EPYC 7H12 (128 cores) | 41.3 | 2.7 |
| 2 × Intel 6248 (40 cores) | 25.0 | 3.0 |
| 4 × NVIDIA V100 | 484 | 11.3 |
| 4 × AMD MI250X | 1240 | 18.2 |

that is, speedups of 19.3 and 49.6 per node over the Intel node. Weak
scaling stays above 80 % to 512 V100 and to 131 072 AMD Rome cores and
above 95 % to 1024 MI250X GPUs, with a peak near $3\times10^{11}$ cell/s;
CPU performance and scaling are close to PLUTO 4.4. GPU efficiency drops
"substantially" for sub-domains smaller than $64^3$, where CPU and GPU
energy efficiencies become similar (§5, Fig. 18).

## Verification in the paper

[Sod](/benchmarks/sod-and-lax-shock-tubes.md) (500 points, Roe, linear,
RK2), [double Mach reflection](/benchmarks/double-mach-reflection.md)
at $1920\times480$, where LimO3 and PPM, "the least diffusive schemes in
IDEFIX", produce a more vigorous wall jet with the onset of
Kelvin–Helmholtz rolls, [Sedov](/benchmarks/sedov-blast-wave.md) blast
waves in Cartesian and spherical coordinates through the polar axis,
[Brio–Wu](/benchmarks/brio-wu-shock-tube.md) with a small post-shock
velocity oscillation "typical of the primitive variable reconstruction",
linear MHD waves, the magnetized rotor, the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md), planet–disc
orbital advection against FARGO3D, an ambipolar C-shock, a Hall-dominated
shock and shearing waves (§4). On linear MHD waves all four Riemann
solvers converge at second order with linear reconstruction; with HLLD,
PPM stops converging at high resolution, most strongly for the slow mode,
which also happens with HLL and in Athena++ with primitive
reconstruction, so the authors recommend LimO3, which converges at
second order at every resolution tested (Figs. 7–8). On Orszag–Tang,
RK3 + PPM + Roe is the most accurate combination at a given resolution
(Fig. 10).

## Qualifications

- The statement that primitive-variable reconstruction keeps "density and
  pressure positivity for instance" (§2.3) is a design remark; the paper
  gives no positivity proof or limiter
  ([bound preservation](/properties/bound-preservation.md)). The
  "fourth order" quoted for PPM and LimO3 refers to the reconstruction
  alone.
- **Printed slips.** The Sod test is printed with $p_L=p_R=0.1$ and
  $v=0$, a stationary contact that could not produce the rarefaction, contact and
  shock of the paper's own Fig. 2 (§4.1). The 2D
  Orszag–Tang resolution is printed as $128^3$ with a $512^3$ reference
  in the text and $128^2$ with a $1024^2$ reference in the captions. As
  printed, the viscous stress and the heat flux enter Eqs. (2) and (4)
  with the sign that makes them anti-diffusive for constant
  coefficients, opposite to the Ohmic term of Eq. (3), which is
  diffusive *(compiler check, not in the sources: the verdict depends on
  the sign convention; it holds for the printed definition of the stress
  tensor with positive viscosities and a positive thermal diffusion
  coefficient, and reverses if the stress tensor and the heat-flux term
  are meant with a minus sign, a convention the paper does not state)*. Page 1 carries a template date of 1996–1997.
- The ordering of the Riemann solvers by diffusivity is a general
  statement; on linear waves the four solvers lie within small factors
  of each other (Fig. 7).
- Comparison with other GPU codes is qualitative: K-Athena is described as
  similar but limited to Cartesian ideal MHD, and Parthenon as similar in
  hydrodynamic performance while providing AMR (§6).

# Citations

- [Lesur et al. (2023)](/sources/lesur-2023.md) — arXiv v1: §1; §2.1–2.9, Eqs. (1)–(13), Table 1; §3; §4.1–4.3, Figs. 2–17; §5, Tables 3–4, Fig. 18; §6.
