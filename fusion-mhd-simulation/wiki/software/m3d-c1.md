---
type: Software
title: "M3D-C1"
description: "PPPL implicit 3D extended-MHD code with C1 reduced-quintic (Bell) triangles in the poloidal plane and Hermite cubic elements toroidally, scalar-potential representations of the field and flow, split-implicit time stepping, a meshed vacuum and thick resistive conductors inside the domain, stellarator geometry, a bootstrap-current closure and a fluid runaway-electron model advanced by characteristics; benchmarked against CLT, JOREK and NIMROD and applied to W7-X sawtooth-like crashes, resistive-wall tearing and the nonlinear edge instability of an optimized quasi-axisymmetric reactor stellarator."
status: established
aliases: [M3D-C^1]
tags: [code, mhd, full-mhd, extended-mhd, reduced-mhd, tokamak, stellarator, finite-elements, time-integration, wall, bootstrap-current, benchmark]
timestamp: 2026-10-16T20:00:00Z
---

# M3D-C1

M3D-C1 is an implicit, high-order finite-element code for nonlinear
extended (two-fluid) MHD developed at PPPL
([Zhang et al. (2021)](/sources/zhang-2021.md), §1–2;
[Saxena et al. (2025)](/sources/saxena-2025.md), §2). The kinetic-MHD hybrid
built on it is [M3D-C1-K](/software/m3d-c1-k.md).

## Physics models

* **Model hierarchy.** Two-variable reduced MHD, four-variable reduced MHD,
  full single-fluid MHD and two-fluid MHD are available
  ([Artola et al. (2021)](/sources/artola-2021.md), §2). The vector potential
  is written through the poloidal flux per radian $\psi$, a second scalar
  potential and a fixed term that carries the vacuum toroidal field; the
  velocity through a stream function, a toroidal-velocity scalar and a
  compressional potential (Artola et al. 2021, §2).
* **Single-fluid resistive MHD** of the CLT benchmark: continuity, pressure,
  momentum with a Laplacian viscosity, induction, and Ohm's law with the
  equilibrium current subtracted, $\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_0)$,
  so that the equilibrium does not diffuse resistively (Zhang et al. 2021,
  Eqs. 1.1–1.6). M3D-C1 advances $\mathbf A$ (Zhang et al. 2021, §2).
* **Single-fluid set with viscous stress** of the bootstrap paper: ion
  perpendicular, gyro- and parallel viscosity, electron viscosity as
  hyper-resistivity, anisotropic heat flux (Saxena et al. 2025, App. C).
* **Bootstrap current.** A non-inductive current $\mathbf J_x$ in Ohm's law,
  $\mathbf E=-\mathbf v\times\mathbf B+\eta(\mathbf J-\mathbf J_x)$, with the
  matching Ohmic heating $\eta\mathbf J\cdot(\mathbf J-\mathbf J_x)$. $\mathbf J_x$
  is parallel, with $\langle\mathbf J_x\cdot\mathbf B\rangle$ from the Sauter
  (1999) or Redl (2021) fits, mapped to quasi-symmetric stellarators by the
  Landreman isomorphism (Saxena et al. 2025, Eqs. 2.1–2.3, App. A–B). See
  [bootstrap current](/definitions/bootstrap-current.md) and
  [quasi-symmetry](/definitions/quasi-symmetry.md).
* **Impurities.** Charge-state-resolved models with KPRAD-fitted ADPAK
  atomic data in the Lyons et al. (2019) gas-injection benchmark
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §2.2, App. A;
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7).
* **Runaway electrons.** A fluid runaway model coupled to MHD exists (Liu et
  al. 2021, cited by [Bandaru et al. (2024)](/sources/bandaru-2024.md), §I;
  no comparison shown there). [Liu et al. (2021)](/sources/liu-2021.md)
  (§2–3) describe it directly: the runaway density is convected at a numerical
  speed $c_{\rm RE}$ along $\mathbf b$ plus the $\mathbf E\times\mathbf B$ drift,
  the runaway current (at the speed of light) is removed from the resistive
  term of Ohm's law and the Ohmic heating, and $en_{\rm RE}\mathbf E$ enters the
  momentum equation. The continuity equation is advanced not by the
  Galerkin $\theta$-implicit matrix but by a method of characteristics with
  pseudo particles at the quadrature points, pushed by a massless-limit Boris
  scheme; see
  [runaway-electron advection by characteristics](/methods/runaway-electron-advection-by-characteristics.md)
  and [runaway-electron fluid model](/methods/runaway-electron-fluid-model.md).
* **Stellarator single-fluid model.** Visco-resistive MHD in SI with constant
  density, a full viscous stress with compressional viscosity, anisotropic
  conduction, a Gaussian heat source and a fixed ECCD source current; two-fluid
  and other effects "are not yet functional in stellarator geometry"
  ([Zhou et al. (2023)](/sources/zhou-2023.md), §II).
  [Wright & Ferraro (2024)](/sources/wright-2024.md) (§II, App. A, Eqs.
  A1–A5, 1–2) run the stellarator model **with** the continuity equation,
  the density being held at its initial value at the wall (an implicit
  source), with $\eta J^2$ heating and no source current, the
  perpendicular heat flux written with the full temperature gradient as in
  Zhou et al. (2023), $\kappa_\perp/\kappa_\parallel=10^{-6}$
  ($\chi_\perp=2.18$ m²/s), dynamic viscosity
  $3.65\times10^{-4}$ kg m⁻¹ s⁻¹ (about 100 times experimental values) and
  no hyper-diffusion. Resistivity is
  $\eta=\eta_{\rm u}[\eta_c+\eta_0T_e^{-3/2}]$ with $\eta_{\rm u}=2.74\ \Omega$ m
  the code's resistivity unit (page-local symbols), constant
  ($\eta_c=10^{-6}$) or Spitzer-like ($\eta_0=1$, 10, 100); Saxena et al.
  (2025) use the same unit. "M3D-C1 itself is not a spectral code": a
  toroidal Fourier decomposition is a post-processing diagnostic (§III).

## Discretization

* Unstructured triangular mesh in $(R,Z)$, extruded toroidally. The 3D
  element is the tensor product of the reduced-quintic Bell triangle and a
  Hermite cubic in $\phi$, which gives $C^1$ continuity of every scalar
  (Artola et al. 2021, §2, Table 1; Zhang et al. 2021, §2). In 3D each
  scalar has 12 degrees of freedom per vertex, 6 in 2D (Artola et al. 2021,
  §3).
* Meshes are packed near resonant surfaces: 4800 poloidal elements and 16
  toroidal planes for the CLT tearing case, 3816 elements and 12 planes for
  the kink case (Zhang et al. 2021, §2, Figs. 3, 11); 17 424 vertices per
  plane and 16 toroidal Hermite elements in the 3D VDE benchmark (Artola et
  al. 2021, §3).
* The equilibrium is re-solved by Grad–Shafranov on the finite-element basis
  from the input profiles (Zhang et al. 2021, §2; see the
  [Grad–Shafranov equation](/definitions/grad-shafranov-equation.md)).
* Stellarator domains use non-axisymmetric domain geometry (Zhou et al.
  2021, cited by Saxena et al. 2025, §2); M3D-C1 is among the codes extended
  to stellarators with full MHD on flux-surface-aligned grids
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §I). For W7-X, the
  VMEC mapping $R(s,\theta,\phi)$, $Z(s,\theta,\phi)$ defines a fixed-boundary
  domain bounded by the last closed surface and does not evolve; $C^1$
  elements are used in all three dimensions, with 3807 reduced-quintic
  elements in the poloidal plane and 16 Hermite cubic elements per field
  period (80 for the full torus), the toroidal resolution being set by the
  strongly anisotropic heat transport ([Zhou et al. (2023)](/sources/zhou-2023.md),
  §II–IV). Boundary conditions: ideal for $\mathbf B$, no-slip for $\mathbf v$,
  fixed $p$.
* The QA reactor runs of Wright & Ferraro (2024, §II) use the full torus
  with no imposed symmetry, 72 toroidal planes and $8.64\times10^5$ 3D
  elements, about $4\times10^5$ CPU-hours and 14 days per run, without
  GPUs; the domain is the initial plasma boundary with a conducting wall,
  no vacuum region, and $T$ and $J$ zero at the wall.
* Runaway runs use 6454 elements per plane and 16 toroidal planes, packed near
  $q=2$; the runaway-loss fraction converges only with at least 16 planes
  ([Liu et al. (2021)](/sources/liu-2021.md), §3, §5.3, Fig. 14).

## Time integration and solvers

* **Split-implicit** advance in the order velocity, magnetic field,
  pressure(s), density, with optional implicit hyper-resistivity (Artola et
  al. 2021, §2, Table 1). The time step is not CFL-limited and is chosen by
  physics, so runs on transport time scales are possible (Saxena et al.
  2025, §2; [Liu et al. (2022)](/sources/liu-2022.md), §5).
* Zhang et al. (2021) (§2) describe a $\theta$-implicit advance with
  $\Delta t=1.0\,\tau_A$; Artola et al. (2021) (§3) use $\Delta t=0.5\,\tau_A$,
  halved for 0.048 ms in the most dynamic phase, followed by an added
  second-order "upwind" toroidal diffusion of pressure, density and field to
  avoid a numerical instability.
* A "2D-complex" version solves a single toroidal harmonic for linear runs;
  the 3D version runs nonlinearly (Zhang et al. 2021, §2).
* Finite-element matrices are built and solved on CPUs with MPI domain
  decomposition (Liu et al. 2022, §5). The sparse Galerkin systems are
  solved by GMRES with a block-Jacobi preconditioner; with strong toroidal
  advection ($c_{\rm RE}\gg v_A$) the toroidal derivative couples the
  per-plane blocks and "can dominate the matrix" at Alfvénic time steps,
  which motivated the characteristics scheme
  ([Liu et al. (2021)](/sources/liu-2021.md), §2–3). In the kinetic-ion
  extension the GPUs compute the MHD matrix elements while the CPUs solve the
  matrices with PETSc ([Liu et al. (2022b)](/sources/liu-2022-b.md), §6; see
  [M3D-C1-K](/software/m3d-c1-k.md)). See
  [implicit time integration](/methods/implicit-time-integration.md).
* The semi-implicit MHD advance is stated to help stabilize the numerical
  instabilities that appear once kinetic ions are included, and to allow
  large time steps (no evidence shown)
  ([Liu et al. (2022b)](/sources/liu-2022-b.md), §1, §7).
* The W7-X runs use $\Delta t=0.573\,\mu$s; lower dissipation needs better
  preconditioners ([Zhou et al. (2023)](/sources/zhou-2023.md), §III, §V).
* **GPU.** The runaway pseudo-particle push runs on GPUs: one advance of the
  runaway equation takes 126 s with the $\theta$-implicit solve and 39 s with
  characteristics on 32 POWER9 CPUs, and 3.8 s with characteristics on 96 V100
  GPUs (Summit), a comparison that is not like-for-like in hardware
  ([Liu et al. (2021)](/sources/liu-2021.md), §3, Fig. 1).

## Walls and boundaries

The computational domain extends past the plasma: conductors are meshed
regions in which only $\mathbf A$ is advanced with $\mathbf E=\eta_w\mathbf J$,
and the vacuum satisfies $\nabla\times\nabla\times\mathbf A=0$. Temperature and
density conditions are set at the plasma boundary, magnetic conditions at the
outermost boundary; the 3D VDE wall is axisymmetric and thick (Artola et al.
2021, §2, Table 1). [Isernia et al. (2023)](/sources/isernia-2023.md) (§I)
contrast this with JOREK's external Green's-function coupling (see
[resistive-wall coupling](/methods/resistive-wall-coupling.md)).

## Coupled codes

Fusion-IO post-processes M3D-C1 output into approximate magnetic coordinates
built from electron-temperature isotherms; the surface averages it computes
(trapped fraction, $\iota$, Boozer $G$ and $I$, inverse aspect ratio) feed
the bootstrap closure (Saxena et al. 2025, §2). SFINCS, NEO and XGCa serve as
neoclassical references, VMEC and SIMSOPT supply stellarator equilibria
(§3), and QSOLVER supplies the CLT benchmark profiles (Zhang et al. 2021,
§2). See [VMEC](/software/vmec.md).

## Verification and benchmarks

* **CLT.** In the [CLT–M3D-C1 benchmark](/benchmarks/clt-m3d-c1-benchmark.md)
  ($R/a=10$, $\beta\approx0$), linear 2/1 tearing growth rates differ by
  7–11 % for $\eta\ge3\times10^{-7}$ and 24 % at $\eta=10^{-7}$ (compiler's
  check of Table 1; the paper says "about 10%"), and 1/1 resistive-kink rates
  by 2.7–6.3 %; the printed scaling fits are $\gamma\propto\eta^{0.58}$ and
  $\eta^{0.30}$ for M3D-C1. Nonlinear $n=1$ kinetic-energy saturation is
  $1.4\times10^{-6}$ against CLT's $1.5\times10^{-6}$ (tearing), with peaks
  of $4.2\times10^{-5}$ against $4.4\times10^{-5}$ (kink) (Zhang et al. 2021,
  §3, Tables 1–2). See [tearing mode](/definitions/tearing-mode.md) and
  [resistive internal kink](/definitions/resistive-internal-kink.md).
* **NSTX VDE.** In the [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md)
  the 3D thermal quench lasts 0.24 ms (JOREK 0.14, NIMROD 0.20), peak
  vertical force is about 28 kN, peak sideways force about 2.8 kN (figure
  reading), and the toroidal asymmetry of $I_p$ is 1–1.4 % (Artola et al.
  2021, §4.1, Fig. 8). The axisymmetric predecessor showed "excellent
  agreement" of growth rate, axis motion and currents (Hoelzl et al. 2021,
  §4.8).
* **Impurities.** In the [DIII-D gas-injection benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md)
  M3D-C1 and NIMROD "follow each other rather well" (Hu et al. 2021b, §6.1).
  For SPARC 6-valve gas injection, M3D-C1 and [NIMROD](/software/nimrod.md)
  runs (Kleiner et al. 2025, as cited) with different approximations give "very similar levels of peak
  radiated power in the TQ and comparably high radiated energy fractions";
  no M3D-C1 numbers are printed, so the agreement is stated, not shown
  ([Izzo et al. (2025)](/sources/izzo-2025.md), §II C, §IV; see
  [massive gas injection](/definitions/massive-gas-injection.md)).
* **Resistive-wall tearing, linear.** On a DIII-D locked-mode reconstruction
  the $(2,1)$ mode is unstable with a resistive wall and stable with an ideal
  wall, with $\gamma\tau_A\propto(\tau_w/\tau_A)^{-2/3}$ at large wall time,
  fitted by a cylindrical dispersion relation
  ([Strauss et al. (2022)](/sources/strauss-2022.md), §II, Fig. 2; see
  [resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md)).
* **Runaway-electron $(2,1)$ mode.** The mode structure agrees with MARS-F
  (no curve overlaid); the linear growth rate is insensitive to $c_{\rm RE}$
  above $4v_A$ (within about 11%), while the nonlinear saturation is not
  ([Liu et al. (2021)](/sources/liu-2021.md), §5.2–5.3; see
  [MARS-F](/software/mars-f.md)).
* **Bootstrap.** On the CIRC1 tokamak case the M3D-C1 Sauter profile peak
  is within 2.18 % of NEO's Sauter model and within 0.04 % of XGCa; the
  M3D-C1 Redl peak is within 2.12 % of XGCa and 1.01 % of SFINCS (Saxena et
  al. 2025, §3.1, Fig. 1). For two quasi-axisymmetric stellarators the
  Redl-plus-isomorphism profile is "in close agreement" with SFINCS and the
  standalone Redl formula, by eye 5–10 % deeper at mid-radius (§3.2, Fig. 4).

## Applications in the cited sources

3D hot [VDEs](/definitions/vertical-displacement-event.md) and
[wall forces](/definitions/wall-forces.md) in NSTX (Artola et al. 2021);
[tearing](/definitions/tearing-mode.md) and resistive-kink verification
(Zhang et al. 2021); nonlinear quasi-axisymmetric stellarator runs at
$\langle\beta\rangle=2.5\,\%$, where the bootstrap closure sustains the
toroidal current against resistive decay and slows the breakup of edge
surfaces, while kinetic-energy growth still rises with resistivity (36
toroidal planes, $1.88\times10^5$ 3D elements) (Saxena et al. 2025, §3.3,
Figs. 5–7); the first nonlinear transport-time-scale simulations of
ECCD-driven [sawtooth-like crashes](/definitions/sawtooth-crash.md) in full
W7-X geometry, which match the measured crash amplitude and inversion radius
but are about ten times too slow ([Zhou et al. (2023)](/sources/zhou-2023.md),
§IV); the first nonlinear simulations of a reactor-scale two-period QA
configuration optimized without a stability target, in which edge
pressure-driven high-$n$ modes destroy the flux surfaces within about
$1500\tau_A$ for every resistivity model and only even toroidal harmonics
are destabilized ([Wright & Ferraro (2024)](/sources/wright-2024.md),
§III; see
[edge instabilities of an optimized QA reactor stellarator](/results/stellarator-edge-instability-qa.md));
and the termination of a DIII-D runaway plateau by a $(2,1)$ mode,
with more than 95% runaway loss in about 0.06 ms to the lower high-field-side
wall ([Liu et al. (2021)](/sources/liu-2021.md), §5.3; see
[runaway electrons](/definitions/runaway-electrons.md)).

## Limitations

* The bootstrap closure is valid only in quasi-symmetric geometry; its error
  away from quasi-symmetry is to be estimated with SFINCS but is not
  quantified (Saxena et al. 2025, §2, §4).
* Surface averages are computed outside the code on temperature isotherms,
  which become ill-defined once surfaces break ($t>250\,\tau_A$ in the QA
  run) (Saxena et al. 2025, §2, §3.3).
* M3D-C1's 3D VDE growth and saturation lag JOREK and NIMROD by about
  0.1–0.2 ms in the figures, not discussed by the authors (Artola et al.
  2021, Figs. 3, 5, 8).
* In stellarator geometry only the single-fluid model works, the coordinate
  mapping is fixed in time, and the boundary is fixed
  ([Zhou et al. (2023)](/sources/zhou-2023.md), §II–III, §V).

## Contradictions

* **Ohmic heating with a source current.** *Open.* Saxena et al. (2025,
  App. C) print $\eta\,\mathbf J\cdot(\mathbf J-\mathbf J_x)$; Zhou et al.
  (2023, Eqs. 2–3) print $\eta J^2$ with $\eta(\mathbf J-\mathbf J_x)$ in Ohm's
  law for the same code. Recorded in full on
  [visco-resistive MHD model](/methods/visco-resistive-mhd-model.md).
  Wright & Ferraro (2024, Eq. A3) also print $\eta J^2$, but without a
  source current, so their form does not bear on the question.
* **Resistivity dependence of the QA instability.** *Open.* Saxena et al.
  (2025, §3.3) present their resistivity trend as "supporting Wright &
  Ferraro (2024a)", whose runs are "qualitatively identical, regardless of
  resistivity model" with growth rates not monotonic in the multiplier.
  Recorded in full on [quasi-symmetry](/definitions/quasi-symmetry.md).

# Citations

1. [Artola et al. (2021)](/sources/artola-2021.md) — §2, Table 1, §3, §4.1.
2. [Zhang et al. (2021)](/sources/zhang-2021.md) — §§1–4, Tables 1–2.
3. [Liu et al. (2022)](/sources/liu-2022.md) — §5.
4. [Saxena et al. (2025)](/sources/saxena-2025.md) — §§2–4, App. A–C.
5. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.7, §4.8.
6. [Hu et al. (2021b)](/sources/hu-2021-b.md) — §§2.2, 6.1, App. A.
7. [Isernia et al. (2023)](/sources/isernia-2023.md) — §I.
8. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §I.
9. [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §I.
10. [Liu et al. (2021)](/sources/liu-2021.md) — §§2–5, Figs. 1, 5–14.
11. [Zhou et al. (2023)](/sources/zhou-2023.md) — §§II–V.
12. [Strauss et al. (2022)](/sources/strauss-2022.md) — §II, Fig. 2.
13. [Liu et al. (2022b)](/sources/liu-2022-b.md) — §6.
14. [Wright & Ferraro (2024)](/sources/wright-2024.md) — §§II–IV, App. A: stellarator model with continuity, resistivity models, QA reactor runs.
15. [Izzo et al. (2025)](/sources/izzo-2025.md) — §II C, §IV: SPARC gas-injection agreement with NIMROD (stated).
