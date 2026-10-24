---
type: Software
title: "URANOS"
description: "URANOS is a BSD-licensed Fortran 90, OpenACC and MPI finite-difference solver for compressible wall-bounded flows (DNS, wall-resolved and wall-modelled LES): a sixth-order energy-preserving central scheme hybridized with WENO-Z, TENO or adaptive TENO by a priori shock sensors, with a ghost-point immersed boundary, on GPUs."
status: established
aliases: [Unsteady Robust All-around Navier-StOkes Solver, URANOS GPU]
tags: [software, gpu, finite-difference, teno, turbulence, immersed-boundary]
timestamp: 2026-10-24T06:38:53Z
---

# URANOS

URANOS ("Unsteady Robust All-around Navier-StOkes Solver") is a
high-order finite-difference solver for the filtered compressible
Navier–Stokes equations on uniform or stretched structured Cartesian
meshes, aimed at wall-bounded flows (channels and boundary layers) by
direct numerical simulation, wall-resolved LES and equilibrium
wall-modelled LES. It is written in Fortran 90 with OpenACC for GPUs and
MPI, and released under the BSD 2.0 licence (CPC Library and a GitLab
repository). The software paper is
[De Vanna et al. (2023b)](/sources/devanna-2023-b.md); two companion
papers of the same group use it to study the effect of the convective
scheme on wall-modelled LES ([De Vanna et al. 2023a](/sources/devanna-2023.md))
and to couple wall-modelled LES with an immersed boundary
([De Vanna et al. 2023c](/sources/devanna-2023-c.md)). Its numerical
ingredients are recalled from earlier work; the contribution of the
software paper is the GPU port and its measurement.

## Convective discretization

The convective terms are discretized by one of six schemes, all in the
[conservative finite-difference](/definitions/conservative-finite-difference-scheme.md)
form (De Vanna et al. 2023b §3.1; De Vanna et al. 2023a §3.1):

- a sixth-order central, fully split **energy-preserving** (EP) scheme
  after Pirozzoli, which preserves the total kinetic energy semi-discretely
  in the incompressible inviscid limit on uniform and non-uniform
  Cartesian meshes, has nominally zero numerical dissipation, and "cannot
  stably develop shocks/shocklets" (no split form is printed; see
  [split convective forms](/methods/split-convective-forms.md) and
  [kinetic energy preservation](/properties/kinetic-energy-preservation.md));
- [WENO-Z](/methods/weno-z.md) of orders 3, 5 and 7 in the arbitrary-order
  form of Castro, Costa & Don, with the regularization set to
  $\epsilon=10^{-12}$ to limit dissipation;
- fifth-order [TENO](/methods/targeted-eno.md) with $C_T=10^{-7}$
  (parameters of Fu et al. 2017);
- fifth-order [adaptive TENO](/methods/adaptive-teno.md) (TENO-A5), whose
  cut-off varies between $10^{-10}$ and $10^{-7}$ with the printed
  constants $\alpha_1=10.5$, $\alpha_2=3.5$ (page-local TENO-A constants, not
  the weights $\alpha_k$), $C_r=0.25$ and $\xi_{\mathrm A}=10^{-3}$ (printed $\xi$)
  (parameters of Fu et al. 2018). De Vanna et al. (2023c) also run a
  seventh-order TENO-A7 (§4.3) without printing its constants.

None of the three papers prints a weight, smoothness-indicator or
cut-off formula; the schemes are named and parametrized only.

**Hybridization.** The shock-capturing schemes run either everywhere
("pure") or in a [hybrid](/methods/hybrid-weno.md) with the EP scheme:
an a priori shock sensor (one of the three below) is evaluated at
each interface, and where it exceeds a user threshold
$\Psi^*$ the WENO/TENO flux is used in the
flagged cell and in a band of 2, 3 or 4 neighbouring cells for orders 3,
5 and 7; the EP scheme is used elsewhere (De Vanna et al. 2023b §3.2,
Eqs. 8–10). Three sensors are offered:

- the maximum over the three directions of the divided density
  gradient $\lvert(\rho_{j+1}-\rho_j)/(x_{j+1}-x_j)\rvert$ (Eq. 8);
- the corresponding density jump $\lvert\rho_{j+1}-\rho_j\rvert$
  (Eq. 9), which "generally reduces the WENO/TENO intervention";
- a modified [Ducros sensor](/definitions/ducros-shock-sensor.md),
  $$\Psi_{\mathrm D}=\max\Big(-\frac{\nabla\cdot v}{\sqrt{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}}},\,0\Big),$$
  with regularization $\epsilon_{\mathrm D}=(v_\infty/L)^2$
  in De Vanna et al. (2023b, Eq. 10), $(v_\infty/\delta_0)^2$ with the
  inflow boundary-layer thickness $\delta_0$ in De Vanna et al. (2023a,
  Eq. 9), and the square of $v_\infty/L_0$ in De Vanna et al. (2023c,
  Eq. 13). It flags only compressions and is not squared; it is the
  sensor recommended for wall flows (2023b §3.2) and found "peculiarly
  accurate" in low-resolution wall-modelled LES, where ENO-like detectors
  read noise as shocklets (2023c §3.2).

Because the shock detection makes the error scaling of a hybrid scheme
discontinuous, De Vanna et al. (2023b) report convergence only for the
pure schemes, and they call $\Psi^*$ "strongly dependent
on the flow", to be tuned beforehand (§3.2). De Vanna et al. (2023a)
study $\Psi^*\in\{0,0.1,0.2,0.4\}$ and recommend about
$0.2$ (see **Use** below); De Vanna et al. (2023c) use $0.1$ (§4.3–4.4).

## Viscous terms, models and time stepping

- **Viscous fluxes.** The "incompressible" part of the viscous stress is
  written in flux-difference form with high-order interface stresses,
  $\partial_x(\mu_{\mathrm{tot}}\partial_xv_1)\simeq(\hat\tau_{i+1/2}-\hat\tau_{i-1/2})/\Delta x_i$
  with page-local $\mu_{\mathrm{tot}}$ (molecular plus subgrid viscosity)
  and $\hat\tau_{i+1/2}$ a high-order interface stress whose coefficients
  are deferred to De Vanna et al. (Acta Mech. 2021); the heat flux is
  treated alike (2023b §3.3, Eqs. 11–13). It reduces to central
  differences of the same order for smooth viscosity and is said to
  conserve viscous fluxes independently of stretching and viscosity
  variations; the sixth-order form is used (2023a §3.3; 2023c §3.3). The
  remaining "compressible" part is not written out.
- **Subgrid models.** Smagorinsky, WALE, Sigma and the Mixed Time Scale
  model, with a Boussinesq closure, subgrid Prandtl number 0.9 and the
  triple correlation neglected (2023b §2.2).
- **Wall model.** An equilibrium wall-stress model: thin-boundary-layer
  ordinary differential equations for the wall-parallel velocity and the
  temperature are integrated on an embedded one-dimensional grid from the
  wall to an exchange height, and the resulting wall shear stress and
  heat flux are imposed by raising the wall viscosity and conductivity to
  effective values, so that no-slip and isothermal or adiabatic
  conditions stay enforced (2023b §2.3; 2023a §2.2, Eqs. 4–8; see
  [wall-modelled LES](/methods/wall-modeled-les.md)).
- **Immersed boundary.** De Vanna et al. (2023c) add a sharp-interface
  ghost-point [immersed boundary](/methods/immersed-boundary-method.md):
  ray tracing flags solid and fluid points once at start; for each ghost
  point a wall-normal probe defines an image point, where bilinear (2D)
  or trilinear (3D) interpolation gives the state; Dirichlet data are
  imposed by $\phi_g=2\phi_b-\phi_{ip}$ and Neumann data by
  $\phi_g=\phi_{ip}$ (page-local: ghost, boundary and image-point values)
  on the primitive variables (§2.3, Eqs. 9, 15–18). The wall model is
  switched on per ghost point only where the local inner-scaled spacings
  fail $\Delta x^+<40$, $\Delta y^+<5$, $\Delta z^+<20$ after a
  Reichardt-law first guess of the friction velocity; elsewhere the wall
  is treated as resolved (§3.5, Eqs. 19–25).
- **Time stepping.** The three-stage third-order
  [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) method of Gottlieb &
  Shu in Shu–Osher form (2023b Eq. 14), which the papers call
  "low-storage TVD"; the time step is the minimum of a convective limit
  and two Fourier limits (viscosity and conductivity). De Vanna et al.
  (2023b) state that a linear analysis gives stability up to
  $\mathrm{CFL}=1$ and recommend CFL 0.5–0.8 and Fourier number 0.1–0.3
  (§3.4, Eqs. 15–16); the two companion papers run CFL 0.5 and Fourier
  number 0.1.
- **Boundaries.** Navier–Stokes characteristic boundary conditions at
  top and outflow, digital-filter turbulent inflow on a van
  Driest-transformed Musker profile, a constant-mass-flow forcing in
  channels (2023b §5).

## GPU implementation

De Vanna et al. (2023b) §4 port the code with OpenACC:

- one `!$acc data copy` region encloses the time loop, so the fields stay
  on the device; every routine of a Runge–Kutta substep runs in
  `parallel` regions (the `kernels` construct is deliberately not used)
  with `loop gang, vector collapse(3)` (Algorithms 1–2);
- MPI ranks are bound to GPUs through `MPI_Comm_split_type` on the
  shared-memory communicator (Algorithm 3);
- halo exchange has three options, blocking `MPI_SENDRECV`, non-blocking
  `MPI_ISEND`/`MPI_IRECV`, and non-blocking with derived datatypes; on
  CPUs the third "considerably outperformed" the others, and it is not
  reported on GPUs because OpenACC is "not optimised" for derived
  datatypes (§4.1.2);
- the exchange is either host-staged, with asynchronous `update` queues
  hiding the staging behind the first send, or GPU-aware, passing device
  pointers through `host_data use_device` (Algorithms 4–5).

**Performance** (3D bi-periodic Riemann problem on $256^3$ points, one
GPU against one full CPU node, seconds per iteration, §4.2.1, Fig. 1):

| System | CPU node | GPU, host-staged MPI | GPU, GPU-aware MPI |
|---|---|---|---|
| MARCONI100: POWER9 (32 cores) / V100 | 3.13 | 0.99 (×3.15) | 0.89 (×3.50) |
| GALILEO100: Xeon Platinum (48 cores) / V100 | 1.77 | 1.14 (×1.55) | 0.92 (×1.92) |
| DGX-A100: EPYC 7742 (128 cores) / A100 | 1.16 | 0.58 (×2.01) | 0.49 (×2.38) |

The right-hand side takes about 95 % of an iteration; the MPI boundary
exchange is "nearly ×10" faster GPU-aware than host-staged (×57.8
against ×6.2 over the CPU node, Fig. 2). Strong scaling on MARCONI100
($512\times256\times256$, up to 32 units) gives about 60 % efficiency on
32 CPU nodes and a reduction "by around 50%" on 32 GPUs; weak scaling at
$256^3$ per unit stays above 75 % up to 256 units (§4.2.3, Fig. 3). The
authors place their GPU weak scaling "in line with" AFiD, CaNS and
[STREAmS](/software/streams.md) (§4.2.3).

## Verification and validation

In De Vanna et al. (2023b), App. A and §5:

- all six convective schemes converge at their design order in $L_1$,
  $L_2$ and $L_\infty$ on an advected sinusoidal density wave
  (App. A.1, Fig. 11);
- Sod and Shu–Osher on 200 points and a four-quadrant two-dimensional
  Riemann problem on $1600^2$ improve with WENO order and from WENO-Z to
  TENO ([Sod tube](/benchmarks/sod-and-lax-shock-tubes.md),
  [Shu–Osher](/benchmarks/shu-osher-problem.md),
  [2D Riemann problems](/benchmarks/two-dimensional-riemann-problems.md);
  App. A.2–A.3);
- the viscous discretization converges at orders 2, 4 and 6 on a laminar
  Kolmogorov flow (App. A.4);
- [turbulent channel flow](/benchmarks/turbulent-channel-flow.md) DNS at
  bulk Mach 0.1 ($\mathrm{Re}_\tau=180$, computed 179; CPU and GPU agree
  "down to machine precision") and 1.5 ($\mathrm{Re}_\tau=215$), LES at
  $\mathrm{Re}_\tau=590$ and wall-modelled LES at $\mathrm{Re}_\tau=5200$
  agree with reference DNS (§5.1, Table 1);
- [supersonic turbulent boundary layers](/benchmarks/supersonic-turbulent-boundary-layer.md)
  at $M_\infty=2$ (DNS and LES) and a wall-modelled $M_\infty=5.86$ layer
  with TENO-A5 agree with reference DNS in mean velocity and temperature
  (§5.2).

## Use: the convective scheme in wall-modelled LES

De Vanna et al. (2023a) run 69 cases of spatially developing boundary
layers at $M_\infty=2$ and $5.86$ with all six schemes, pure and hybrid
(§4, Tables 1–4). Their findings, all numerical:

- in wall-resolved LES, upwinding lowers the friction, raises the
  log-layer velocity and the turbulent-kinetic-energy peak; the error
  shrinks with WENO order and with TENO, and the EP scheme matches DNS
  (§4.2);
- in wall-modelled LES, pure WENO/TENO damp or destroy near-wall
  turbulence, and WENO-Z3 fails at every grid; hybridization with
  $\Psi^*=0.1$ restores realistic statistics, and at
  $0.4$ all shock-capturing schemes give the same curves because most of
  the flow is computed by the EP scheme (§4.3);
- at $M_\infty=5.86$ a pure EP run diverges because of shocklets, and
  $\Psi^*=0.2$ is the largest stable threshold; the
  authors recommend $\Psi^*\simeq0.2$ (§4.4, §6);
- the wall time per iteration relative to pure EP is 0.90–1.00 for the
  hybrids and 0.95–1.32 for the pure schemes, the maximum for TENO-A5 on
  the fine grid (§4.3.1, Table 2; 13 Intel KNL nodes).

See [numerical dissipation](/definitions/numerical-dissipation.md) for
the mechanism they propose.

## Qualifications

- The abstract of De Vanna et al. (2023b) claims "over three times
  speed-up for a node-to-node comparison, even at large scales, with an
  efficiency of about 80% while using 1024 GPUs". The body compares one
  GPU with one CPU node, reaches ×3.5 only on MARCONI100 (×1.92 and ×2.38
  on the other systems), and shows weak scaling up to 256 units; no
  1024-GPU run is reported (§4.2).
- De Vanna et al. (2023a) state that pure schemes cost "about 5÷30%" more
  than EP, but their coarse-grid pure WENO-Z values are 0.95–0.99
  (Table 2); they also cite a "roughly doubled computing cost" of TENO
  against EP from earlier work, which their own table does not show
  (§4.3.2).
- The thresholds $\Psi^*$ belong to this non-squared,
  compression-only sensor and its regularization; they are not
  transferable to the classical squared Ducros ratio.
- De Vanna et al. (2023b) print $\Delta t_{\mathrm{Fo1}}$ for both Fourier
  limits (Eq. 15c should be $\Delta t_{\mathrm{Fo2}}$, as Eq. 16 shows)
  and $\tilde e=c_p\tilde T$ for the internal energy, while their own
  energy equation (Eq. 6a) is consistent with $c_v\tilde T$, the form
  De Vanna et al. (2023c) print (§2.1).
- No convergence or scaling data accompany the immersed boundary of
  De Vanna et al. (2023c); its parallel ray tracing is replicated on all
  ranks (§3.6).

# Citations

- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — program summary; §2.1–2.3; §3.1–3.4, Eqs. (8)–(16); §4.1–4.2, Algorithms 1–5, Figs. 1–3; §5.1–5.2, Tables 1–2; App. A.1–A.4, Figs. 11–14.
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §2.2, Eqs. (4)–(8); §3.1–3.4, Eq. (9); §4.2–4.4, Tables 1–4; §6.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §2.3, Eqs. (9), (15)–(18); §3.1–3.6, Eqs. (13), (19)–(25); §4.3–4.4.
