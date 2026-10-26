---
type: Software
title: "FLEXI"
description: "FLEXI is an open-source high-order DGSEM framework for compressible scale-resolving simulation, with the HOPR mesh generator and POSTI post-processing; this page records its numerics, turbulence features, parallel performance and the LES studies run with it."
status: established
aliases: [FLEXI framework, HOPR, POSTI]
tags: [software, dg, les, kinetic-energy-preserving, reinforcement-learning]
timestamp: 2026-10-26T15:52:00Z
---

# FLEXI

**FLEXI** is an open-source (GNU GPL v3.0) framework for hyperbolic–parabolic
conservation laws, centred on the unsteady compressible Navier–Stokes equations
for DNS, LES and direct aeroacoustics, presented by authors from the University of
Stuttgart, the University of Cologne and the Max Planck Institute for Plasma
Physics. It is written "predominantly in modern,
procedural Fortran" with MPI and HDF5 I/O, and comprises three parts: the mesh
preprocessor **HOPR**, the [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
solver FLEXI, and the post-processing suite **POSTI**
([Krais et al. 2021](/sources/krais-2021.md), §1–§2, Fig. 1).
[Beck & Kurz (2023)](/sources/beck-2023.md) and
[Kurz et al. (2023)](/sources/kurz-2023.md) use it as the LES solver of their
reinforcement-learning closures, coupled to the agent by
[Relexi](/software/relexi.md).

## Numerics

As derived by Krais et al. (2021, §3–§4):

- DGSEM on curved hexahedra, Legendre–Gauss or Legendre–Gauss–Lobatto nodes,
  weak and strong forms, curl-form metric terms for free-stream preservation.
- BR1 (and BR2) lifting of primitive variables for viscous fluxes; Roe,
  Rusanov and HLL-type Riemann solvers.
- Split-form DG with two-point volume fluxes, giving
  [kinetic-energy-preserving](/properties/kinetic-energy-preservation.md) or
  entropy-conserving schemes, with dissipative surface fluxes optional.
- [Hybrid DG/finite-volume subcell shock capturing](/methods/subcell-finite-volume-shock-capturing.md)
  with Persson–Peraire, JST or Ducros indicators and a two-threshold switch.
- Explicit low-storage Runge–Kutta time integration (Williamson two-register
  form), with empirically corrected time-step factors depending on $N$.
- **Mortars** for non-conforming hexahedral interfaces (2:1 in either side
  direction and 4:1): the large-side solution is interpolated to the small
  sides, and the small-side fluxes are $L^2$-projected back to the large side
  (§3.2, Eqs. 43–51, after Kopriva).

## Turbulence and LES features

Krais et al. (2021, §2.2.3) list: implicitly filtered LES with implicit closure
through the discretization (choice of numerical flux) for well-resolved LES;
explicit [Smagorinsky](/methods/smagorinsky-model.md), $\sigma$ and
[Vreman](/methods/vreman-model.md) eddy-viscosity models (no formulas or
constants printed); volume or surface filtering for filter-based LES and
variational multiscale models; a wall-stress model after Larsson et al. (see
[equilibrium wall model](/methods/equilibrium-wall-model.md)); Spalart–Allmaras
RANS initialization by pseudo-time stepping; synthetic inflow by anisotropic
linear forcing combined with recycling–rescaling; sponge layers damping toward
a moving time average; on-the-fly time averaging and record points. Beck & Kurz
(2023, §III A, §V) run it with split-form DG, the L2Roe interface flux and BR1
lifting, and compare no-model LES, a static Smagorinsky model ($C_s=0.17$) and
the compressible [dynamic Smagorinsky](/methods/dynamic-procedure.md) model with
their learned closures.

## Mesh generation: HOPR

HOPR writes curved high-order unstructured hexahedral meshes to an HDF5 format
ordered along a space-filling curve, so that any number of processes (not
exceeding the number of elements) can read contiguous element ranges of the
same file in parallel (Krais et al. 2021, §2.1.1). Boundary curving is done by
surface subdivision (a refined surface mesh with points on the exact geometry)
or by the point-normal method; the displacement is spread into the volume by
radial-basis-function interpolation, which "dramatically" improves the scaled
Jacobian at a NACA 0012 leading edge (§2.1.2–2.1.3, Fig. 6). Block-structured
meshes can be agglomerated by a factor $n_b$ in each direction: for a serrated
nozzle (20.6 million linear cells to 322,110 elements, $n_b=N_{\mathrm{geo}}=4$)
curving every element left 10 invalid elements, curving only the boundary
layer 61, while keeping 2–4 curved layers left none (§2.1.4, Table 1).

## Parallel performance

On a Cray XC40 (Hazel Hen; two 12-core Xeon E5-2680 per node), a free-stream
problem with $N=6$ on LG nodes, meshes from $6^3$ to $96\times96\times48$
elements and 24 to 49,152 cores, Krais et al. (2021, §5.8, Fig. 20) define the
performance index
$$\mathrm{PID}=\frac{\text{wall time}\times\#\text{cores}}{\#\text{DOF}\times\#\text{time steps}\times\#\text{RK stages}}$$
(Eq. 68) and find: super-linear strong scaling in cache-favourable regimes; a
parallel efficiency that does not drop below 70% for pure DG; a PID nearly
constant above about $10^5$ degrees of freedom per core, with an optimum near
$10^4$ and latency dominating below; the hybrid DG/FV operator 15–20% slower.
The memory per degree of freedom is 0.74 KiB at $N=5$ (Table 4). The DGSEM
volume integral costs $O(N)$ operations per degree of freedom (Table 3).

Later sources extend these figures. [Chapelier et al. (2024)](/sources/chapelier-2024.md),
§III.B.f, state superlinear strong scaling "up to 262.000 CPUs" (read as 262,000,
the point being a thousands separator *(compiler check, not in the
sources)*) down to one element per
process. They cite it to the FLEXI exascale preprint of Blind et al. (2023),
a study other than the measured one of Krais et al. above.
[Kurz et al. (2025)](/sources/kurz-2025.md), §4.4, put CPU FLEXI's optimum
in a "narrow band" of 3000–10 000 degrees of freedom per core. At higher
load the cache is exhausted and memory bandwidth limits the code; at lower
load latency dominates. They cite Krais et al. (2021) and Blind et al. for
this band.

## GPU port: GALÆXI

[GALÆXI](/software/galaexi.md) is FLEXI ported to NVIDIA GPUs in CUDA
Fortran. It keeps FLEXI's data structures, MPI strategy (space-filling-curve
partition, sorted contiguous MPI face data, non-blocking messages with MPI
faces first) and parameter files, so that FLEXI set-ups run on it unchanged.
On the Taylor–Green vortex the two codes give results identical "up to
machine precision" at $M_0=0.1$, and identical dissipation histories at
$M_0=1.25$. On a NASA Rotor 37 cascade, FLEXI on 32 768 cores of HAWK used
339 kWh per convective time unit, against 147 kWh for GALÆXI on 128 A100
GPUs (Kurz et al. 2025, §1, §3.1, §5.2, §6.3, Table 3). The GPU code's
kernels, scaling and energy accounting are on its page.

## Reproducibility

Unit tests at every build, check-in tests in GitLab CI, and nightly and weekly
regression tests with the REGGIE tool (which checks convergence rates); every
HDF5 state file carries a "userblock" with the parameter file, the git
revision and local patch, and the build configuration, from which the exact
binary can be rebuilt (Krais et al. 2021, §6).

## Post-processing: POSTI

A ParaView reader plugin hands the ParaView MPI communicator to the Fortran
visualization tool, which reuses solver routines (I/O, mesh, lifting, DG
operator, equation of state) to compute derived quantities such as $\lambda_2$
and super-samples high-order data to linear output (Krais et al. 2021, §2.3,
§5.9).

## Applications in the sources

- **NACA 64418 airfoil**, wall-resolved implicit LES at $Re_c=10^6$, $M=0.2$,
  angle of attack 4°: split DG with Pirozzoli's kinetic-energy-preserving flux
  "following Flad & Gassner [28]", $N=7$, 229,620 elements, about 117 million
  degrees of freedom per variable, $\Delta x^+\approx40$–$60$,
  $\Delta z^+\approx20$–$30$, $\Delta y^+\approx3$ (spacings divided by $N+1$);
  12,000 cores, 47,000 CPU-hours per convective time unit, PID 1.35 µs. The
  pressure coefficient agrees with XFoil except near the suction-side trailing
  edge, where the LES shows a separation XFoil cannot predict (Krais et al.
  2021, §7.1, Fig. 24).
- **Open cavity**, zonal [wall-modelled LES](/methods/wall-modelled-les.md) and
  direct noise computation: Kawai–Larsson wall model, Vreman SGS model, $N=7$,
  30 million degrees of freedom, $Re_\theta=6300$, $U_\infty=42.5$ m/s; the
  cavity spectrum matches the experiment in level and width above 2 kHz and
  captures the first two Rossiter modes below; the Vreman model "helps to reduce
  artificial pressure fluctuations caused by the wall-model" (§7.3, Fig. 27).
- **Supersonic turbulent boundary layer DNS** at $M=2.67$ up to
  $Re_\theta=3878$, 1.458 billion degrees of freedom per variable (§2.2.2,
  Fig. 8, shown as a picture, the result of a cited work).
- **Forced isotropic turbulence** at $Re_\lambda\approx180$: the DNS reference
  of Beck & Kurz (2023, §IV A) used $N=7$ and $64^3$ elements ($512^3$ points),
  about 30,000 CPU-hours on 16,384 cores of HAWK; their LES at 24 and 36
  degrees of freedom per direction and $N=3,5,8$ run the RL agent through the
  [Relexi](/software/relexi.md) framework, which couples FLEXI to the agent
  on HPC systems (§IV B). The earlier study of
  [Kurz et al. (2023)](/sources/kurz-2023.md) uses the same set-up at
  $Re_\lambda\approx180$, $M=0.1$, with Lundgren's linear isotropic forcing
  applied nodally and the KEP split form on LGL nodes (§3.2, §3.5): LES at
  24, 32, 36 and 48 degrees of freedom per direction ($N=5$ or 7, $4^3$ to
  $8^3$ elements; Table 2) learn an element-wise Smagorinsky coefficient in
  $[0,0.5]$; Relexi (TensorFlow, TF-Agents and SmartSim) launches several
  FLEXI runs per training iteration, and training took one to five days on
  HAWK with up to 1024 CPU cores for the simulations and one GPU node for
  the network (§4.1). Their element-wise
  [dynamic Smagorinsky](/methods/dynamic-procedure.md) baseline uses a modal
  cut-off test filter to degree 2 ($N=5$) or 3 ($N=7$), element averages of
  the Lilly numerator and denominator and an eddy viscosity clipped to
  $[-100\mu,1000\mu]$, since unclipped values "deteriorated the solution
  quite drastically" (App. A); evaluating the learned policy cost about 10%
  more than this dynamic procedure on one CPU core (§4.2).

- **Grid adaptation for wall-resolved and wall-modelled LES**
  ([Blind et al. 2023](/sources/blind-2023.md)): FLEXI with LGL nodes, Roe
  interface flux, BR1 lifting, low-storage Runge–Kutta, the Pirozzoli
  split form and the [Vreman model](/methods/vreman-model.md) (constant
  0.03 wall-resolved, raised to 0.11 for wall-modelled runs "from previous
  experience") with the isotropic length $V_e^{1/3}/(N+1)$, $N=5$ (§2.1,
  §2.3, §3.3). The Toosi–Larsson modelling-residual estimator, transferred to
  the DGSEM through an element-local modal test filter, drives
  [mesh adaptation](/methods/mesh-adaptation.md) of channels at
  $Re_\tau=550$ and 2000 (wall-resolved, against Lee & Moser DNS) and
  $Re_\tau=2000$ (Spalding-law wall model at $h_{\mathrm{wm}}=0.1\delta$), and
  of a transonic NACA 64A-110 at $M=0.72$, $Re_c=930{,}000$ from a
  6-element-per-chord start; FLEXI's mortars, limited to 2-to-1 interfaces,
  save up to about half of the elements (§3–§4; see
  [wall-modelled LES](/methods/wall-modelled-les.md)).

- **Supersonic Taylor–Green vortex** in the seven-code comparison of
  [Chapelier et al. (2024)](/sources/chapelier-2024.md) at $Re=1600$,
  $M_0=1.25$ (§III.B.f, Tables I–II; HAL accepted manuscript): fourth-order
  DGSEM ($N=3$) on $16^3$ to $128^3$ elements ($64^3$ to $512^3$ degrees of
  freedom), Roe flux with the second Harten–Hyman entropy fix, BR1,
  fourth-order low-storage Runge–Kutta and no explicit subgrid model
  ([implicit LES](/definitions/implicit-les.md)). Shocks are captured by the
  [subcell finite-volume](/methods/subcell-finite-volume-shock-capturing.md)
  switch: troubled elements are solved with a second-order TVD finite-volume
  scheme with a generalized minmod limiter, flagged by a modal-decay
  indicator on the pressure. FLEXI's kinetic energy lies closer to the
  finite-difference codes than to the two other Riemann-flux element codes
  (CODA and SD3D, both with localized artificial diffusivity), which the
  authors attribute to the finite-volume subcells (§IV.A). FLEXI is among
  the three codes with the highest solenoidal dissipation on every grid. Its
  dilatational dissipation oscillates on the coarse grids, which the
  authors attribute to the DG–FV switching per element. It gives the
  sharpest shocks of all codes, matching the reference Mach profile at
  $256^3$ and oscillating below (§IV.A–B, Figs. 6–8; see
  [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)).
- **NASA Rotor 37 cascade, CPU reference** for GALÆXI (Kurz et al. 2025,
  §6.3, Table 3): $2.6\times10^8$ degrees of freedom at $N=5$ on 32 768
  cores (about 7900 per core), PID $1.02\times10^{-6}$ s, 7538 s of wall
  time per convective time unit; see [NASA Rotor 37](/benchmarks/nasa-rotor-37.md).

Ferrer et al. (2023, §2, Table 1), comparing high-order codes, tick for
Flexi/Fluxo a Fortran DG code for compressible flow with energy- or
entropy-stable formulations, $p$-adaptation, LES and shock capturing, and no
RANS, multiphase, particle, aeroacoustics or immersed-boundary capability,
as judged by the HORSES3D authors in June 2022 (see
[HORSES3D](/software/horses3d.md)).

Flad & Gassner (2017) ran their study of kinetic-energy-preserving DG LES in an
"in-house DG simulation framework" that the paper does not name; Krais et al.
(2021, §2.2.3, §7.1) cite it as the basis of FLEXI's implicit-LES approach.

## Qualifications

- Krais et al. (2021) print "perfect strong scaling performance" for more than
  one billion degrees of freedom on 100,000 cores (§2.2.2), while their measured
  study ran to 49,152 cores with an efficiency that "does not drop below 70%"
  (§5.8). The measured values are the quantitative ones.
- The version read is the arXiv v1 preprint (October 2019); section and equation
  numbers are those of the preprint.
- Krais et al. (2021, Eq. 46) swap the superscripts of the two mortar
  interpolation matrices relative to their own Eqs. (43) and (45).
- The validation of the airfoil LES is against XFoil only.
- Krais et al. (2021, §3.2) call their mortar types 2:1 and 4:1 by the
  number of small faces per big face, the big face being halved in one or in
  both reference directions, "always cut at the middle"; Blind et al. (2023,
  §3.2) call FLEXI's mortars "2-to-1" by the element-size ratio. Both
  describe a halving of the element size across a mortar face; the labels
  count different things.
- Blind et al. (2023, §2.3) state that $N=5$ is used "throughout this work",
  but their airfoil table gives 512 degrees of freedom per element, i.e.
  $N=7$, against 216 ($N=5$) in the channel tables *(compiler check, not in
  the sources)*. The version read is the arXiv v1 preprint, retitled at
  publication.
- Kurz et al. (2025, Eq. 22) define the PID with the total number of
  Runge–Kutta stages in the denominator. Krais et al. (2021, Eq. 68) write
  time steps times stages per step. The two definitions are the same
  quantity *(compiler check, not in the sources)*.
- Chapelier et al. (2024, App. A, Fig. 9) show a FLEXI run at $384^3$
  degrees of freedom in the subsonic verification case, which their text
  does not list among the resolutions used.

# Citations

- [Krais et al. (2021)](/sources/krais-2021.md) — §1–§2 (framework, HOPR, POSTI, features); §3–§4 (numerics); §5.6–5.8, Eq. (68), Tables 3–4, Fig. 20 (cost and scaling); §6 (reproducibility); §7.1–7.3 (applications).
- [Beck & Kurz (2023)](/sources/beck-2023.md) — §III A (scheme); §IV A–B (DNS cost, Relexi); §V (reference closures).
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §2.1, §6.1 (the in-house DG framework and the split-form LES strategy FLEXI cites).
- [Blind et al. (2023)](/sources/blind-2023.md) — §2.1, §2.3 (FLEXI set-up, Vreman length scale, modal test filter); §3.1–3.3, Tables 1–4 (channels, mortars); §4, Tables 5–6 (NACA 64A-110).
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §2, Table 1 (Flexi/Fluxo capabilities as judged by the HORSES3D authors).
- [Kurz et al. (2023)](/sources/kurz-2023.md) — arXiv v2: §3.2 (linear forcing); §3.5, Table 2 (FLEXI set-up, Relexi); §4.1–4.2 (training cost, policy cost); App. A (element-wise dynamic Smagorinsky in FLEXI).
- [Chapelier et al. (2024)](/sources/chapelier-2024.md) — HAL accepted manuscript: §III.B.f, Tables I–II (FLEXI configuration, scaling claim); §IV.A–B, Figs. 5–8 (supersonic Taylor–Green results); App. A, Fig. 9.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1, §3.1 (GALÆXI as a FLEXI port, MPI strategy); §4.4 (CPU optimum per core); §5.2 (identical Taylor–Green results); §6.3, Table 3 (Rotor 37 CPU reference, energy).
