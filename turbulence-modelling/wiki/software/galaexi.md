---
type: Software
title: "GALÆXI"
description: "GALÆXI is the GPU port of the FLEXI DGSEM framework in CUDA Fortran for compressible flow on curved unstructured hexahedra, with split-form DG and subcell finite-volume shock capturing; this page records its kernel and stream design, memory, scaling to 1024 A100 GPUs, verification and energy-to-solution against FLEXI."
status: established
aliases: [GALAEXI, Galaexi, GPU FLEXI]
tags: [software, dg, gpu, implicit-les, turbomachinery]
timestamp: 2026-10-26T15:52:00Z
---

# GALÆXI

**GALÆXI** is the GPU version of the [FLEXI](/software/flexi.md) framework
of the University of Stuttgart, presented by
[Kurz et al. (2025)](/sources/kurz-2025.md). It solves the compressible
Navier–Stokes equations with the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) on
unstructured, curved hexahedral meshes, and keeps FLEXI's data structures,
parallelization and user interface, so that it is a "drop-in replacement"
that runs existing FLEXI set-ups on GPUs "without modifications" (§1). It is
written in Fortran 2008 with the device code in CUDA Fortran, so it runs on
NVIDIA hardware only; other back-ends are announced (§3, §7). The code is
open source under GPL-3.0. The version of Kurz et al. read is the arXiv v2
preprint (October 2024). Kurz and Kempf share the first authorship.

The paper contains no turbulence model: the governing equations carry only
the molecular viscous stress and Fourier heat flux, and every LES in it runs
without an explicit subgrid model. The authors call their cascade run a
"wall-resolved LES" and never use the term implicit LES; in this bundle's
terms these are [implicit LES](/definitions/implicit-les.md), the split-form
DGSEM and the shock-capturing blend supplying all the
[numerical dissipation](/properties/numerical-dissipation.md).

## Numerics

As described by Kurz et al. (2025, §2), all of it inherited from FLEXI:

- **DGSEM** on Legendre–Gauss or Legendre–Gauss–Lobatto nodes, polynomial
  degree $N$, curl-form metric terms; the semi-discrete form (Eq. 18) is
  written with each term labelled by the code routine that evaluates it
  (volume integral `VolInt`, surface integral `SurfInt`, Riemann flux
  `FillFlux`, Jacobian scaling `ApplyJac`).
- **Split form.** The [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md)
  two-point flux of Pirozzoli on Gauss–Lobatto nodes, as the nonlinear
  stabilization of under-resolved runs; the authors recall over-integration
  and filtering as the alternatives and state that two-point fluxes increase
  the cost "considerably" (§2.2).
- **Viscous terms** by BR1 lifting of the primitive-variable gradients,
  which re-executes the surface, volume, flux and Jacobian routines for each
  gradient direction.
- **Shock capturing** by the convex DG/finite-volume blend of Hennemann et
  al., $\partial_tU=(1-\alpha)R_{DG}(U)+\alpha R_{FV}(U)$ with $\alpha\in[0,1]$
  set per element by an a priori indicator; only element-interior
  contributions are blended, because the outer surface fluxes are the same
  for both operators (§2.3, Eq. 21; see
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md)).
  The authors relay from [Beck & Kurz (2023)](/sources/beck-2023.md) that
  such a blend "has also been demonstrated to yield a sensible turbulence
  model if tuned correctly".
- **Time integration** by low-storage explicit Runge–Kutta schemes: five
  stages, fourth order (Carpenter–Kennedy) for the verification, and 14
  stages, fourth order with a stability region optimized for convection
  (Niegemann et al.) for the cascade.
- **Cost per routine.** The volume integral scales as $O(N^4)$ per element
  and every other routine as $O(N^3)$ or $O(N^2)$ (Table 1).

## GPU design

Kurz et al. (2025, §3) state three design rules: keep FLEXI's data structures
and unstructured parallelization, keep most of the code base, and run every
routine of the time step on the device, with no host–device transfer;
initialization and infrequent analysis stay on the CPU. Parallelism has three
levels:

1. **Between GPUs:** FLEXI's pure-MPI scheme, with subdomains of nearly
   equal element count along a precomputed space-filling curve, face data
   sorted so that MPI partners exchange contiguous arrays in an order known
   a priori, non-blocking messages sent as early and awaited as late as
   possible, and CUDA-aware MPI; each GPU is paired with one CPU core of the
   same NUMA domain (§3.1).
2. **Within a GPU:** three CUDA streams with priorities, low for
   element-interior work, middle for inner faces, top for MPI faces, so that
   the data to be communicated are computed first and the communication is
   hidden behind interior work; the streams also absorb the "tail effect" of
   the last partial wave of thread blocks (§3.2, Fig. 4).
3. **Kernels:** pointwise operations use one thread per degree of freedom
   over flattened arrays, through hardware-agnostic elemental routines shared
   with the CPU code; the surface integral is rewritten in a "gather" form
   in which one thread owns one volume node and loops over the six faces of
   its element, flipping the flux sign on the replica side, so that only one
   thread writes each entry and no race condition arises without explicit
   synchronization (Alg. 4); the volume integral uses one thread block per
   element in shared memory, so that each two-point flux is computed once
   and never written to main memory (§3.3, App. A).

On one A100 with $N=7$, split-form DG and $8.9\times10^5$ degrees of freedom,
the volume integral takes 39.0% of the time and the conversion to primitive
variables 14.5%; the volume–surface routines (surface integral and
prolongation, with their lifting variants) take "only around 15%", which the
authors read as a negligible overhead of the unstructured mesh (§3.3, Fig. 5).

## Memory and scaling

- **Memory** per degree of freedom falls with the degree because the
  surface-to-volume ratio of the element falls: 1.457 KiB at $N=1$, 0.869
  KiB at $N=7$, 0.787 KiB at $N=12$; at $N=7$ about 48 million degrees of
  freedom fit on one 40 GiB device (§4.3, Table 2).
- **Performance index.** Kurz et al. (2025, Eq. 22) write
  $\mathrm{PID}=\text{wall time}\times\#\text{ranks}/(\#\text{RK stages}\times\#\text{DOF})$,
  a rank being a CPU core or a whole GPU; it is the PID of
  [FLEXI](/software/flexi.md) with the number of time steps folded into the
  stage count *(compiler check, not in the sources)*. They introduce the **energy-normalized** index
  $$\mathrm{EPID}=\frac{\text{wall time}\times\text{power}}{\#\text{RK stages}\times\#\text{DOF}}=P_{\mathrm{rank}}\times\mathrm{PID},$$
  the energy to advance one degree of freedom by one stage, $P_{\mathrm{rank}}$
  being the power per rank (§4.2, Eq. 23).
- **Load threshold.** On JUWELS Booster (four A100 per node, HDR200
  InfiniBand), with the Taylor–Green set-up at $N=7$ on meshes from 32 to
  $256^3$ elements (16 384 to $8.6\times10^9$ degrees of freedom) and 100
  time steps, the PID converges for every GPU count above about $10^6$
  degrees of freedom per GPU; below it kernel-launch overhead and tail
  effects degrade it even on one GPU, and communication latency on many.
  Weak scaling relative to one four-GPU node and strong scaling for
  $3.4\times10^7$, $5.4\times10^8$ and $2.1\times10^9$ degrees of freedom
  are "almost perfect" up to 1024 GPUs above that load; without the stream
  scheduling the low-load performance drops, the figure marking a gain of
  up to 92% from the streams (§4.4, Figs. 6–8).
- **Against CPU FLEXI.** CPU FLEXI also loses performance at high load,
  through cache exhaustion and memory bandwidth, which leaves a narrow
  optimum of 3000–10 000 degrees of freedom per core (citing Krais et al.
  2021 and Blind et al.); on the GPU more load only helps, up to the device
  memory (§4.4). Kurz et al. say the threshold "matches" the NekRS
  strong-scaling limit of about 2–4 million degrees of freedom per rank
  reported by [Fischer et al. (2022)](/sources/fischer-2022.md) (see
  [Nek5000 and NekRS](/software/nek5000.md)); the two figures differ by a
  factor of two to four *(compiler check, not in the sources)*.
- Communication cost rises markedly when the nodes of a run spread over more
  switch groups of the DragonFly+ network (192 GPUs each) (§4.4).

## Verification and validation

- **Manufactured solution** (periodic $[-1,1]^3$, density, velocity and
  energy as advected sine waves, amplitude 0.1): design order for every
  $N$ from 2 to 9, for standard DG on Gauss nodes and for split-form DG on
  Gauss–Lobatto nodes, from 1 to $64^3$ elements (§5.1, Fig. 9).
- **[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)** at
  $Re=1600$, $N=7$, $8^3$ to $64^3$ elements ($64^3$ to $512^3$ degrees of
  freedom), isothermal initialization ("Version II"): at $M_0=0.1$ GALÆXI
  and FLEXI agree "up to machine precision" and the solenoidal dissipation
  converges to the DeBonis reference, matching it "almost perfectly" at
  $512^3$; at $M_0=1.25$, with Sutherland's law and the FV blend at the
  same maximum $\alpha$ for every resolution, GALÆXI and FLEXI give the
  same solenoidal dissipation, which converges to the reference of
  [Chapelier et al. (2024)](/sources/chapelier-2024.md) and is "almost
  identical" at $512^3$ (§5.2, Figs. 10–11).

## Application: NASA Rotor 37 cascade

Kurz et al. (2025, §6) run a wall-resolved LES of a linear cascade built from
the mid-span profile of [NASA Rotor 37](/benchmarks/nasa-rotor-37.md),
extruded by 5% of chord, at a ground-idle condition: inflow Reynolds number
972 550 on chord, inlet relative Mach number 0.758, incidence 10.1°;
1.2 million elements at $N=5$ ($2.6\times10^8$ degrees of freedom), adiabatic
walls, sponge zones, Sutherland's law, the Pirozzoli split form and the
14-stage scheme, advanced 8 convective times from a converged state. The
FV blend is active only near the leading-edge shock, with $\alpha$ between
0.1 and 0.7 there, so that the scheme keeps high order elsewhere (Fig. 13).
The PID is about 35% higher than in the scaling tests, which the authors
attribute to sponges, boundary conditions, indicator, FV operator and load
imbalance. Per convective time (Table 3):

| Run | Ranks | DOF per rank | Power per rank | PID | EPID | Wall time | Energy |
|---|---|---|---|---|---|---|---|
| GALÆXI, A100 (HAWK-AI) | 128 GPUs | $2.03\times10^6$ | 448 W | $4.58\times10^{-9}$ s | $2.05\times10^{-6}$ J | 9209 s | 147 kWh |
| FLEXI, CPU (HAWK) | 32 768 cores | $7.93\times10^3$ | 4.94 W | $1.02\times10^{-6}$ s | $5.06\times10^{-6}$ J | 7538 s | 339 kWh |

The saving is 59.5% in EPID and 56.8% in energy. Power was measured per rack
by the computing centre, network switches included, and cooling included for
the GPU system but not for the CPU system; the authors call the figure "a
rough estimate" and "a conservative lower bound". They find it "reasonable"
to relate it to a similar cut in carbon emissions, "more than 55 %"; no
emission is measured (§6.3, §7). FLEXI's validation of this cascade against experiment is
cited to Kopper's PhD thesis (University of Stuttgart, 2024) and not shown; GALÆXI is "confirmed to match"
FLEXI without a comparison figure, and no turbulence statistics or wall-unit
resolutions are printed.

## Qualifications

- "Provable stability near shocks" (§1) comes from the blend of Hennemann
  et al., whose reference-list title reads "a provably entropy stable
  subcell shock capturing approach". The runs use Pirozzoli's
  kinetic-energy-preserving flux, which [Ferrer et al. (2023)](/sources/ferrer-2023.md), §3.3, list as a split
  form distinct from the entropy-conserving ones (see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
  and the paper does not state that the proof covers this configuration; the same point is recorded on
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).
- Printed slips in the version read: the Lagrange polynomial of Eq. (15)
  is printed with its own label as the product index and cannot satisfy the
  Kronecker property of Eq. (16); the Fig. 9 caption swaps left and right
  relative to the panel titles; the Fig. 11 caption writes "(left)" for both
  references; Appendix A refers SurfInt to §2.2 instead of §3.3; Eqs.
  (29)–(30) normalize by an undefined $\mu_0$, and a "viscous dissipation
  rate" $\varepsilon_T$ is named but never defined.
- §4.4 says the scaling mesh is refined from $4\times4\times2$ elements by
  doubling "in each spatial direction" up to $256^3$; doubling every
  direction from $4\times4\times2$ reaches $256\times256\times128$, while the
  printed endpoint counts (16 384 and $8.6\times10^9$ degrees of freedom)
  match 32 and $256^3$ elements at $N=7$ *(compiler check, not in the
  sources)*.
- The compressible Taylor–Green reference is cited as a manuscript
  "submitted to Physics of Fluids (2024)"; its published form is
  [Chapelier et al. (2024)](/sources/chapelier-2024.md).

# Citations

- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1 (scope, drop-in compatibility); §2.1–2.3, Eqs. (1)–(21), Table 1 (equations, DGSEM, split form, BR1, FV blending, cost per routine); §3.1–3.3, Algs. 1–4, Figs. 4–5, App. A (MPI, streams, kernels, time breakdown); §4.1–4.4, Eqs. (22)–(23), Table 2, Figs. 6–8 (hardware, PID and EPID, memory, scaling); §5.1–5.2, Figs. 9–11 (manufactured solution, Taylor–Green vortex); §6, Table 3, Fig. 13 (Rotor 37 cascade, energy); §7.
- [Beck & Kurz (2023)](/sources/beck-2023.md) — cited by Kurz et al. for the DG/FV blend as a turbulence model.
- [Fischer et al. (2022)](/sources/fischer-2022.md) — NekRS strong-scaling limit compared by Kurz et al.
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — supersonic Taylor–Green reference used by Kurz et al.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §3.3 (Pirozzoli and entropy-conserving split forms listed as distinct options).
