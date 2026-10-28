---
type: Software
title: "CaLES"
description: "CaLES is an open-source GPU finite-difference solver for large-eddy simulation of incompressible wall-bounded flows, built on the DNS code CaNS; this page records its numerics, closures and wall model, its GPU design and performance on A100 nodes, and its validation, including non-monotonic grid convergence of wall-modelled LES."
status: established
aliases: [CaNS, CaNS-2.3.0]
tags: [software, gpu, les, wmles, sgs-model]
timestamp: 2026-10-28T17:00:00Z
---

# CaLES

**CaLES** is an open-source (MIT) solver for LES of incompressible
wall-bounded flows on GPUs, written in Fortran 90 with OpenACC directives,
CUDA Fortran and MPI, and built as an extension of version 2.3.0 of the DNS
code CaNS ([Xiao et al. 2025](/sources/xiao-2025.md), program summary,
§1–§2). It solves single-block Cartesian domains with non-uniform spacing
in one direction only (the wall-normal $y$ in the paper): isotropic
turbulence, temporal boundary layers, channels, ducts and cavities. Xiao et
al. state the platform, not a physical assessment of the models, as the
purpose, and motivate it by the hundreds or thousands of LES runs that
[model-consistent training](/methods/model-consistent-training.md) and
[reinforcement-learning closures](/methods/reinforcement-learning-closure.md)
need, and by grid-convergence studies of
[wall-modelled LES](/methods/wall-modelled-les.md) (§1).

Among the open-source solvers of their Table 1 (STREAmS-2, URANOS, AFiD,
LESGO, CaNS, CaLES), only URANOS and [LESGO](/software/lesgo.md) already
support LES, and LESGO has no GPU support; [STREAmS](/software/streams.md)
is listed as a compressible GPU DNS solver. The authors state that
incompressible solvers are "typically more efficient" than compressible
ones such as URANOS for low-Mach flows, mainly because explicit time
integration then allows much larger time steps (§1).

## Numerics (inherited from CaNS)

As described by Xiao et al. (2025, §2, Eqs. 11–22):

- **Space.** Second-order central finite differences on a staggered grid
  (Harlow & Welch), which avoids odd–even decoupling and preserves energy
  discretely in the inviscid limit (Verstappen & Veldman, as cited; see
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
- **Pressure.** Fractional-step pressure correction; a direct Poisson
  solver by eigenfunction expansion (FFTs, cuFFT on GPUs) with a Thomas
  tridiagonal solve along $y$.
- **Time.** Wray's low-storage three-step third-order Runge–Kutta, with
  coefficients $(8/15,5/12,3/4)$ and $(0,-17/60,-5/12)$ and their sums
  $(8/15,2/15,1/3)$ multiplying the pressure gradient; the step is set to
  0.95 of the stability limit. Viscous terms can be explicit,
  Crank–Nicolson in all three directions, or Crank–Nicolson in $y$ only;
  the modified Helmholtz equations use the same direct solver. The SGS term
  is always explicit, grouped with convection.

The fully implicit option is not analysed for efficiency because FFTs then
solve the momentum equations; with implicit viscous terms in all three
directions the wall model can only be applied on walls normal to $y$, since
the Fourier directions need homogeneous conditions (§2.2, §3.2).

## Closures added by CaLES

As implemented by Xiao et al. (2025, §2.1–§2.2):

- **Static [Smagorinsky model](/methods/smagorinsky-model.md)** with van
  Driest damping, $\nu_t=(C_s\Delta D(y))^2\lvert\bar S\rvert$ with
  $D(y)=1-\exp(-y^+/25)$ ($A^+=25$, $y^+$ in the simulation's own wall
  units). $C_s=0.18$ in decaying isotropic turbulence ($0.22$ was needed on
  the coarse box-filtered case, not shown); the value used in channels and
  ducts and the definition of $\Delta$ are not printed.
- **[Dynamic procedure](/methods/dynamic-procedure.md)** of Germano and
  Lilly, $\nu_t=C_s^2\Delta^2\lvert\bar S\rvert$ with
  $C_s^2=\langle M_{ij}L_{ij}\rangle/\langle M_{ij}M_{ij}\rangle$ averaged
  over the homogeneous directions and clipped to zero, box test filter of
  width ratio $\hat\Delta/\Delta=2$. In the first off-wall layer the
  wall-parallel velocity is extrapolated linearly to the ghost points and a
  3D filter applied with $\hat\Delta/\Delta=4^{1/3}$, which "mathematically
  corresponds to a 2D box filter"; it gave more accurate wall-modelled
  channels than $8^{1/3}$ (data not shown). Strain-rate components are formed at cell centres
  (off-diagonal ones at edge midpoints, then averaged).
- **[Equilibrium wall model](/methods/equilibrium-wall-model.md)**, the
  log law $U_{\mathrm{LES}}/u_\tau=\kappa^{-1}\ln(u_\tau h_{\mathrm{wm}}/\nu)+B$
  with $\kappa=0.41$, $B=5.2$ and $h_{\mathrm{wm}}=0.1\delta$, fed with the
  instantaneous wall-parallel velocity magnitude interpolated linearly
  between the first two off-wall staggered points and solved by
  Newton–Raphson to a relative tolerance of 0.01% in 3 to 7 iterations. The
  resulting wall stress is the boundary condition of the wall-parallel
  velocity, with impermeability for the normal one; the wall-model
  conditions are applied last in the boundary-condition sequence. In the
  first off-wall layer the wall-normal derivatives of the wall-parallel
  velocity are first-order one-sided (following Kawai & Larsson, as cited),
  "crucial" for the strain rate entering the SGS viscosity.

The authors argue, citing Larsson et al. and Bermejo-Moreno et al., that
the log law is not restricted to equilibrium flows, because wall-modelled
LES resolves the outer-layer non-equilibrium and the inner layer, with its
short time scale, may stay in quasi-equilibrium (§2.1; see
[law of the wall](/definitions/law-of-the-wall.md)). The conclusion names
the [Vreman model](/methods/vreman-model.md), an ODE-based wall model and
learned SGS and wall models as candidates for the platform (§5).

## GPU design and performance

**Implementation** (§2). Large arrays are moved to the GPU once and only
scalars and small arrays thereafter (except for output); OpenACC `kernels`
for simple assignments, `parallel loop collapse` for the advective,
viscous, SGS and time-advancement loops, `async` throughout. One MPI rank
per GPU on a 2D pencil decomposition managed by cuDecomp, which autotunes
the layout and the communication back ends (CUDA-aware MPI point-to-point
or all-to-all, NCCL, NVSHMEM) separately for transposes and halo exchanges.
The pencil axis is along $x$, except along $y$ with implicit-in-$y$ viscous
terms.

**Cost on Leonardo** (CINECA; one 32-core Xeon Platinum 8358 per CPU node,
four A100 64 GB per GPU node), channel on $512\times384\times1440$ points
(§3.2, Fig. 2, Table 2):

| Viscous terms | Run | CPU node (ns/step/point) | one A100 (ns/step/point) | speedup |
|---|---|---|---|---|
| explicit | DNS | 19.7 | 1.5 | 13 |
| explicit | wall-resolved LES | 34.5 | 1.8 | 19 |
| explicit | wall-modelled LES | 34.7 | 1.8 | 19 |
| implicit in $y$ | DNS | 28.9 | 2.4 | 12 |
| implicit in $y$ | wall-resolved LES | 46.4 | 2.7 | 17 |
| implicit in $y$ | wall-modelled LES | 46.5 | 2.7 | 17 |

The abstract summarizes one A100 as "approximately 15 CPU nodes". The wall
model adds negligible cost and the damped Smagorinsky model about
0.3 ns/step/point. With explicit viscous terms and the Smagorinsky model
the time splits into Poisson solver 38%, right-hand side 30%, SGS model
19% and correction 13% (Fig. 3). Memory per grid point is 136 B for DNS,
168 B with the Smagorinsky model and 352 B with the dynamic model
(explicit viscous terms; 160, 192 and 376 B implicit in $y$); wall-modelled
runs equal wall-resolved ones. Strong scaling on $512\times384\times11520$
and weak scaling on $512\times384\times(5760\,N_{\mathrm{nodes}})$ run from
2 to 64 nodes; the weak-scaling time grows by about 80% over that range,
and the implicit-in-$y$ run does not fit in GPU memory at 64 nodes (Fig. 4).
The authors cite earlier CaNS benchmarks: 4 V100 GPUs of a DGX-2 roughly
equivalent to 2048 CPU cores (0.9 times slower to 1.6 times faster), and
3.1 to 5.6 times faster with all 16 GPUs (§1).

## Validation

All tests are a posteriori (Xiao et al. 2025, §4):

- **Decaying [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)**
  of Comte-Bellot & Corrsin on $32^3$ and $64^3$ cells ($\Delta/\eta=60$
  and 30), initialized with a spectral-cutoff or a box-filtered field: the
  Smagorinsky model with $C_s=0.18$ matches the spectra at $tU_0/M=98$ and
  171 except on the coarse box-filtered case; the dynamic model agrees
  reasonably, nearly perfectly with the box filter, which the authors relate
  to its box test filter; deviations near the Nyquist limit are attributed
  to finite-difference errors (§4.1, Fig. 5).
- **Wall-resolved [channel](/benchmarks/turbulent-channel-flow.md)** at
  $Re_b=2u_b\delta/\nu=20\,000$ against the DNS of Lee & Moser
  ($Re_\tau=543.5$, $C_f=0.00591$), four grids from
  $192\times128\times128$ ($\Delta x^+=36.2$, $\Delta z^+=20.4$,
  $\Delta y^+_w=0.59$) to $576\times384\times384$ ($12.1$, $6.8$, $0.19$):
  Smagorinsky skin-friction errors fall from 9.38% to 0.50%; the dynamic
  model gives $-2.25$, $-0.69$, $-1.49$ and $-3.22\%$, which the text
  summarizes as "less than approximately 3%". Resolved shear stress is
  over-predicted with Smagorinsky and under-predicted with the dynamic
  model, matching the sign of the $C_f$ error, and the dynamic model gives
  the higher eddy viscosity (§4.2, Table 3, Figs. 6–8).
- **Wall-modelled channel** at $Re_b=250\,000$ (DNS $Re_\tau=5185.9$,
  $C_f=0.00344$) on 13 grids for each aspect ratio $\Delta x/\Delta z=1$
  and 2, from $\Delta/\delta=0.1$ to $0.002$ (finest $6144\times1536\times2304$,
  about 21.7 billion points, "approximately $\Delta z^+=10$"): grid
  convergence is **non-monotonic** in $C_f$, $\langle u'u'\rangle$ and
  $\langle u'v'\rangle$ for both SGS models and both aspect ratios, as
  Meyers & Sagaut found for wall-resolved LES (as cited). The finest-grid
  $C_f$ errors are 2.43% (Smagorinsky) and 0.44% (dynamic) at aspect ratio 1,
  0.26% and 1.30% at aspect ratio 2, and their sign on the finest grids is
  always positive, "consistent with the fact that mean wall shear stress
  obtained with WMLES is biased toward larger values when the instantaneous
  velocity is used as input for the wall model" (no reference printed).
  Aspect ratio 1 converges better (§4.3, Table 4, Fig. 12). Profile errors
  are integrated only over $0.1\le y/\delta\le1$, because the LES velocity
  inside the wall-modelled layer "should not be taken seriously". Details
  on [wall-modelled LES](/methods/wall-modelled-les.md).
- **Wall-modelled square duct** at $Re_b=40\,000$ against the DNS of
  Pirozzoli et al. ($Re_\tau=1055$, $C_f=0.00557$, secondary-flow kinetic
  energy $3.26\times10^{-5}$ in bulk units over one quadrant), six grids up
  to $2048\times320\times320$: $\lvert C_f\rvert$ errors within about 3%
  (largest $-3.08\%$), secondary-flow energy errors of about 22%
  (Smagorinsky) and 25% (dynamic) on the finest grid, both converging
  non-monotonically; unlike the channel, the streamwise-stress peak on the
  wall bisector rises with refinement and improves (§4.4, Table 5,
  Figs. 14–16).

The authors conclude that the dynamic model shows "somewhat superior
performance in grid convergence and turbulence prediction" (§5).

## Qualifications

- §5 calls the dynamic model "somewhat superior" in grid convergence;
  Table 4 prints, at aspect ratio 2, dynamic-model $C_f$ errors of
  $+6.83$, $+6.69$ and $+6.65\%$ on the three coarsest grids, against
  $+1.60\%$ for the Smagorinsky model on the coarsest.
- §4.3 states uniform refinement in all three directions, while Table 4
  keeps $N_y=256$ between its $1024\times256\times384$ and
  $1536\times256\times576$ rows.
- Printed slips: Eqs. (11), (17), (18), (21) write the Runge–Kutta
  subscripts as $\kappa+1$ where the text and the other equations use
  $k+1$; the Fig. 11 caption states both normalizations (DNS and own wall
  units) for panels (c, d); the Fig. 6 caption marks both total and viscous
  shear stress as solid lines.
- The GPU porting is described as "OpenACC directives, following CaNS-2.3.0"
  in the abstract and as CUDA Fortran plus OpenACC elsewhere; both are
  listed in the program summary.

# Citations

- [Xiao et al. (2025)](/sources/xiao-2025.md) — program summary; §1, Table 1 (motivation, open-source solvers, CaNS benchmarks); §2.1–§2.2, Eqs. (1)–(10) (Smagorinsky with van Driest damping, dynamic procedure, log-law wall model and its implementation); §2, Eqs. (11)–(22) (time integration, staggered differences, Poisson solver); §2 (OpenACC, cuDecomp); §3.2, Figs. 2–4, Table 2 (performance, memory, scaling); §4.1–§4.4, Tables 3–5, Figs. 5–16 (validation); §5.
