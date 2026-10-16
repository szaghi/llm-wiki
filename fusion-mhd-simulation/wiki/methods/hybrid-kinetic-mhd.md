---
type: Method
title: "Hybrid kinetic-MHD models"
description: "Models that advance the bulk plasma as an MHD fluid and a kinetic species (classically a minority energetic-particle population, in the kinetic-thermal-ion variant also the bulk ions) as markers, closing the fluid momentum equation with a moment of the marker distribution; the codes of this bundle differ in the MHD model, the kinetic ordering, the representation of the distribution and the time coupling."
status: established
aliases: [kinetic-MHD hybrid, hybrid MHD-kinetic, hybrid MHD-gyrokinetic, MHD-kinetic hybrid model]
tags: [hybrid-kinetic, energetic-particles, particles, mhd, alfven-eigenmode, numerics]
timestamp: 2026-10-16T20:00:00Z
---

# Hybrid kinetic-MHD models

A hybrid kinetic-MHD model splits the plasma in two. The thermal (bulk)
plasma is advanced by an MHD model, which may be reduced, full, resistive or
two-fluid. A minority of energetic particles (EPs), with density
$n_h\ll n_i$, is advanced kinetically by markers. The EPs act on the
fluid only through one moment of their distribution $f_h$ inserted in the
fluid momentum (or vorticity) equation: the pressure tensor $\mathsf P_h$ or
the EP current density $\mathbf J_h$
([Liu et al. (2022)](/sources/liu-2022.md), §4;
[Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II;
[Vlad et al. (2025)](/sources/vlad-2025.md), §1). The two choices are
compared on
[pressure coupling and current coupling](/methods/pressure-and-current-coupling.md).
The model is cheaper than a fully kinetic or fully gyrokinetic description
of all species, and it keeps the wave–particle resonances that drive
Alfvén eigenmodes. Bogaarts et al. (2022, §I) give this as the reason for
the approach; Liu et al. (2024, §I) state that it is "more popular" than
pure gyrokinetics for EP-driven Alfvén eigenmodes because it is cheaper
([Liu et al. (2024)](/sources/liu-2024.md)).

**Scope beyond the minority.** The definition above, with its
$n_h\ll n_i$ premise, is that of the chunk-1 sources and remains the
classical form. It does not cover the
[kinetic-thermal-ion](/methods/kinetic-thermal-ions.md) variant, in which
the **bulk ions** are also $\delta f$ markers and the fluid keeps only the
perpendicular momentum, the field and the electron pressure:
[M3D-C1-K](/software/m3d-c1-k.md) with kinetic thermal and fast ions
([Liu et al. (2022b)](/sources/liu-2022-b.md), §2) and
[MEGA](/software/mega.md) with kinetic thermal ions alone
([Sato et al. (2024)](/sources/sato-2024.md), §2) or together with a second
kinetic species of Maxwellian 100 keV energetic ions
([Sato & Todo (2026)](/sources/sato-2026.md), p. 8). There the kinetic species
is not a minority, the ion density and parallel flow come from the markers,
and the coupling moment is that of the bulk ions. The common structure is
the split itself: some species as fluid, some as markers, joined through
moments in the fluid momentum equation.

The assumption $n_h\ll n_i$ is used explicitly to drop the EP momentum
density from the bulk momentum balance in the perpendicular direction
([Liu et al. (2022)](/sources/liu-2022.md), §4). The fully gyrokinetic code
[ORB5](/software/orb5.md) keeps fast-ion inertia, and the hybrid codes do
not. Vlad et al. (2025, §7) list this omission as one of the candidate causes
of the nonlinear disagreements in the
[NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md), because the EP
fraction of that case is high ($n_{h0}/n_{i0}\approx0.027$ on axis,
Table 1).

## Building blocks

Every hybrid code of this bundle makes four choices.

1. **The bulk model.** It can be reduced MHD with a vorticity equation
   ([GMEC](/software/gmec.md),
   [Liu et al. (2024)](/sources/liu-2024.md), Eq. 1, built on the
   reduced-MHD solver of
   [Jiang et al. (2024)](/sources/jiang-2024.md)). It can be full,
   reduced or extended MHD solved nonlinearly
   ([JOREK](/software/jorek.md), [M3D-C1-K](/software/m3d-c1-k.md),
   [MEGA](/software/mega.md)), linear resistive full MHD
   ([HYMAGYC](/software/hymagyc.md)), or two-fluid MHD
   ([XTOR-K](/software/xtor-k.md)) ([Vlad et al. (2025)](/sources/vlad-2025.md),
   §§3, 4, 6). The
   [reduced-MHD](/methods/reduced-mhd.md) variant of JOREK was used for the
   AUG-NLED case "as results agree with full MHD while computational costs
   are lower", with no comparison shown
   ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §IV.B).
2. **The kinetic ordering of the EPs.** The EPs can be full orbit
   (JOREK, XTOR-K), drift-kinetic guiding centre (MEGA, M3D-C1-K's RK4
   option), Pauli particles pushed by a slow-manifold Boris scheme
   (M3D-C1-K), or gyrokinetic (GMEC, HYMAGYC). Finite-Larmor-radius (FLR)
   effects are intrinsic to full orbits and are added to drift-kinetic codes
   by an $N$-point gyroaverage. The pushers are compared on
   [particle pushers](/methods/particle-pushers.md).
3. **The representation of $f_h$.** It can be full-$f$ (JOREK, XTOR-K)
   or $\delta f$ (M3D-C1-K, GMEC, HYMAGYC, MEGA, ORB5). See the
   [δf particle method](/methods/delta-f-method.md).
4. **The coupling moment and its time coupling.** The moment is the pressure
   tensor (JOREK, M3D-C1-K, GMEC, HYMAGYC, XTOR-K) or the current (MEGA,
   optionally M3D-C1-K). The moments are projected onto the fluid
   discretization, for example by a Galerkin projection onto finite elements
   (see [particle-to-mesh projection](/methods/particle-to-mesh-projection.md)).

| code | bulk model | EP model | $f_h$ | coupling | source |
|---|---|---|---|---|---|
| [JOREK](/software/jorek.md) | reduced or full MHD, nonlinear, implicit | full orbit (Boris) | full-$f$ | anisotropic pressure, explicit, step-averaged | [Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II |
| [M3D-C1-K](/software/m3d-c1-k.md) | M3D-C1 full MHD, implicit or semi-implicit | RK4 guiding centre or slow-manifold Boris; optionally kinetic thermal ions | $\delta f$ | pressure or current | [Liu et al. (2022)](/sources/liu-2022.md), §§2–4; [Liu et al. (2022b)](/sources/liu-2022-b.md), §2 |
| [GMEC](/software/gmec.md) | linearized reduced MHD (model B), RK4 | gyrokinetic, RK4, 4-point gyroaverage | $\delta f$ | pressure, through the curvature term | [Liu et al. (2024)](/sources/liu-2024.md), §II |
| [HYMAGYC](/software/hymagyc.md) | linear resistive full MHD, backward Euler | gyrokinetic (Brizard), $N=32$ gyroaverage | $\delta f$ | pressure, $\nabla\cdot\mathsf P_h$ | [Vlad et al. (2025)](/sources/vlad-2025.md), §3 |
| [MEGA](/software/mega.md) | nonlinear visco-resistive full MHD, finite differences, explicit RK4 | drift-kinetic, ad-hoc gyroaverage | $\delta f$ | current | [Vlad et al. (2025)](/sources/vlad-2025.md), §4; [Hezaveh et al. (2022)](/sources/hezaveh-2022.md), §2; [Sato et al. (2024)](/sources/sato-2024.md), §2; [Sato & Todo (2026)](/sources/sato-2026.md), p. 2 |
| [XTOR-K](/software/xtor-k.md) | two-fluid MHD, Newton–Krylov | full orbit (Boris–Buneman) | full-$f$ | perpendicular pressure, Picard-iterated | [Vlad et al. (2025)](/sources/vlad-2025.md), §6 |

[ORB5](/software/orb5.md) is the fully gyrokinetic reference against which
the hybrid codes are benchmarked. All its species are kinetic, its markers
are pushed by RK4 along gyrocentre characteristics, and its fields come from
quasi-neutrality and parallel Ampère's law
([Vlad et al. (2025)](/sources/vlad-2025.md), §5).

## Time coupling

The common strategy advances the EP contribution explicitly and the bulk
MHD implicitly ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II,
which call it "a common strategy across different hybrid codes").

- **JOREK.** The pressure tensor is averaged over several gyro-orbits,
  commonly one MHD step, to remove high-frequency noise. It then enters
  the implicit momentum equation as an explicit source
  ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II). Fast ions
  take 100–1000 particle steps per fluid step
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.10).
- **M3D-C1-K.** Particles are subcycled between two MHD steps in fields
  frozen during the subcycles, and the fields are copied to the GPU once per
  MHD step ([Liu et al. (2022)](/sources/liu-2022.md), §5). The fluid and
  kinetic equations are solved "subsequently in one timestep"; with kinetic
  thermal ions this sequential splitting is what makes duplicated fluid and
  marker estimates of $\delta n$ and $\delta v_\parallel$ drift apart,
  hence the synchronization of
  [kinetic thermal ions](/methods/kinetic-thermal-ions.md)
  ([Liu et al. (2022b)](/sources/liu-2022-b.md), §2).
- **MEGA.** Particles and fluid are advanced together by explicit
  fourth-order Runge–Kutta ([Sato et al. (2024)](/sources/sato-2024.md),
  §2).
- **GMEC.** The same explicit RK4 step, $\Delta t\approx0.01\tau_A$, is used
  for fluid and particles. RK4 is unstable for $\Delta t/\tau_A\ge0.04$
  ([Liu et al. (2024)](/sources/liu-2024.md), §II C, App. C).
- **XTOR-K.** XTOR-K is the exception. It nests the implicit
  Newton–Krylov fluid step and the Boris push (16 particle steps per fluid
  step) in a Picard iteration that is repeated until fluid and kinetic parts
  converge together ([Vlad et al. (2025)](/sources/vlad-2025.md), §6).
- **JOREK kinetic neutrals.** The same explicit-moment pattern couples
  JOREK's [kinetic neutrals](/methods/kinetic-neutral-model.md). The
  explicit particle moments multiply implicit MHD terms, and the accuracy
  can drop in order when the kinetic particles dominate
  ([Korving et al. (2023)](/sources/korving-2023.md), §IV C).

## Parallelization and cost

- **M3D-C1-K.** Particles are parallelized by particle, not by domain. Each
  GPU holds the whole-mesh field, gathered with MPI-3 shared memory, and the
  push is ported with OpenACC. The push runs about 11× faster on 24 V100
  GPUs than on 8 POWER9 CPUs: 134.22 s on CPU against 12.65 s on GPU for
  RK4, and 10.32 s for GPU Boris at a 4× smaller step. The text says
  16 M particles for this measurement and the Fig. 2 caption says 4 M
  ([Liu et al. (2022)](/sources/liu-2022.md), §5, Fig. 2). Deposition and
  the MHD solve stay on CPUs. In the nonlinear kinetic-thermal-ion run on
  Perlmutter (8 nodes, 4 A100 GPUs each) the GPUs compute the MHD matrix
  elements as well as the push, while the CPUs solve the matrix (PETSc)
  and compute the particle moments
  ([Liu et al. (2022b)](/sources/liu-2022-b.md), §6).
- **MEGA.** Runs on NEC SX-Aurora TSUBASA vector engines and Fugaku with
  about $10^8$ markers (32 per cell); no GPU use is reported
  ([Sato et al. (2024)](/sources/sato-2024.md), §2). The nonlinear LHD
  kinetic-thermal-ion run at $S=10^7$ used about $6.7\times10^8$ thermal-ion
  markers on a $128\times640\times128$ grid and took about 164.4 h on 2048
  SX-Aurora vector engines ([Sato & Todo (2026)](/sources/sato-2026.md), p. 3).
- **JOREK.** The JOREK particle framework duplicates the full plasma state
  on all MPI ranks, which avoids particle migration
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §3.6). Its kinetic and
  gyrokinetic particles have since been ported to GPUs with OpenACC
  ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5).
- **GMEC.** GMEC is CPU-only, with MPI decomposition in $y$ and Intel TBB
  threads. The gyrokinetic run costs 8× the drift-kinetic one: 2838.60
  against 353.13 core-hours for $2\times10^4$ steps of the $n=3$ TAE on
  896 cores. Strong-scaling efficiency is 63% at 896 cores
  ([Liu et al. (2024)](/sources/liu-2024.md), Table I, App. B).
- **Grid choice.** [Jiang et al. (2024)](/sources/jiang-2024.md) (§III C,
  Eq. 36) choose GMEC's "simple shifted metric" so that the field grid
  points coincide with toroidal-angle grid points. Particles can then be
  pushed "using the same grids without interpolation" of the field to the
  particle. See [field-aligned coordinates](/methods/field-aligned-coordinates.md).

## Scope of present use

The published hybrid results of the chunk-1 sources are mostly linear.

- **GMEC.** It filters a single toroidal harmonic and omits the nonlinear
  fluid terms ([Liu et al. (2024)](/sources/liu-2024.md), §II A).
- **JOREK.** Bogaarts et al. leave nonlinear use to "dedicated verification
  and validation" ([Bogaarts et al. (2022)](/sources/bogaarts-2022.md),
  §VI). Hoelzl et al. (2024) list nonlinear
  [fishbone](/definitions/fishbone.md) studies and kinetic thermal ions as
  work in progress ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §4.2).
- **NLED-AUG.** The only deeply nonlinear code comparison is the
  [NLED-AUG benchmark](/benchmarks/nled-aug-benchmark.md). It keeps the EP
  nonlinearity and omits the fluid nonlinearity
  ([Vlad et al. (2025)](/sources/vlad-2025.md), §2). The four codes agree
  qualitatively and disagree quantitatively.

Chunk 2 adds three nonlinear hybrid applications:

- **Nonlinear fishbone (M3D-C1-K).** An NSTX non-resonant
  [fishbone](/definitions/fishbone.md) with kinetic thermal and fast ions,
  8 toroidal planes and $16\times10^6$ markers, saturating at about 0.5 ms
  ([Liu et al. (2022b)](/sources/liu-2022-b.md), §6).
- **Chirping TAE (MEGA).** An $n=6$
  [TAE](/definitions/toroidal-alfven-eigenmode.md) followed through
  long-range frequency chirping, analysed with the
  [wave-frame action-angle diagnostic](/methods/chirping-phase-space-diagnostic.md)
  ([Hezaveh et al. (2022)](/sources/hezaveh-2022.md), §4).
- **Infernal modes with kinetic thermal ions (MEGA).** Nonlinear $n=3$
  [infernal modes](/definitions/infernal-mode.md) with no EPs at all
  ([Sato et al. (2024)](/sources/sato-2024.md), §3.2).

Chunk 3 adds a fourth: nonlinear high-beta LHD interchange and ballooning
modes in MEGA with kinetic thermal ions, and with energetic ions added
($\beta_h\le0.8\,\%$), which lower the linear $n=2$ growth rate but leave
the saturation level and the final pressure profile essentially unchanged
([Sato & Todo (2026)](/sources/sato-2026.md), pp. 7–9; see
[kinetic thermal ions](/methods/kinetic-thermal-ions.md)).

The same kinetic infrastructure carries non-EP species in JOREK: impurities,
neutrals, [runaway electrons](/definitions/runaway-electrons.md) and
electrostatic ITG ions ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
§§2.10, 2.14). Two-way pressure or current coupling of kinetic runaway
electrons is in development
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.5).

## Contradictions

None between sources on the model itself. The kinetic-thermal-ion codes
widen the scope of the opening definition (the kinetic species need not be a
minority); this is recorded above as a qualification of the definition, not
as a contradiction. The open disagreements are about
the coupling scheme
([pressure and current coupling](/methods/pressure-and-current-coupling.md))
and about benchmark outcomes (the benchmark pages).

# Citations

- [Liu et al. (2022)](/sources/liu-2022.md): M3D-C1-K, the coupling derivation, the GPU push.
- [Liu et al. (2024)](/sources/liu-2024.md): GMEC with gyrokinetic EPs.
- [Jiang et al. (2024)](/sources/jiang-2024.md): the GMEC reduced-MHD foundation and the simple shifted metric for particles.
- [Bogaarts et al. (2022)](/sources/bogaarts-2022.md): the JOREK hybrid extension.
- [Vlad et al. (2025)](/sources/vlad-2025.md): HYMAGYC, MEGA, ORB5 and XTOR-K, compared nonlinearly.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md): the JOREK particle framework.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md): JOREK EP status and GPU port.
- [Korving et al. (2023)](/sources/korving-2023.md): explicit coupling of particle moments to implicit MHD.
- [Liu et al. (2022b)](/sources/liu-2022-b.md): kinetic thermal ions in M3D-C1-K, sequential splitting, GPU matrix assembly, the nonlinear fishbone.
- [Hezaveh et al. (2022)](/sources/hezaveh-2022.md): MEGA equations and the nonlinear chirping TAE.
- [Sato et al. (2024)](/sources/sato-2024.md): MEGA with kinetic thermal ions, its numerics and hardware.
- [Sato & Todo (2026)](/sources/sato-2026.md): MEGA with kinetic thermal and energetic ions together, run size and cost.
