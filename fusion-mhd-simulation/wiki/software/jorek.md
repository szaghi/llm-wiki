---
type: Software
title: "JOREK"
description: "Fully implicit nonlinear extended-MHD code for tokamak X-point plasmas: ansatz-based reduced and full visco-resistive MHD on G1 Bézier finite elements times a toroidal Fourier series, linearized Crank–Nicolson/BDF2 steps solved by GMRES with a per-harmonic block preconditioner, free boundary through STARWALL or CARIDDI, and fluid, kinetic and particle extensions for impurities, neutrals, pellets, runaway and energetic particles."
status: established
aliases: [JOREK 2]
tags: [code, mhd, reduced-mhd, full-mhd, extended-mhd, tokamak, finite-elements, spectral, time-integration, linear-solver, disruption, elm, free-boundary, wall]
timestamp: 2026-10-16T20:00:00Z
---

# JOREK

JOREK is a massively parallel, fully implicit, nonlinear extended-MHD code
for tokamak plasmas in realistic X-point geometry, developed since 2002 and as
"JOREK 2" since 2006 ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §1).
It is Fortran 90/95 (Fortran 2003/2008 in the particle parts) with C/C++
cores, more than 250 000 lines and more than 40 users, kept in Git with about
50 regression tests run on every push (§3.7). The stellarator version is
[JOREK3D](/software/jorek3d.md).

## Physics models

**Reduced MHD.** The base model is an ansatz-based
[reduced MHD](/methods/reduced-mhd.md):
$\mathbf B=F_0\nabla\phi+\nabla\psi\times\nabla\phi$ with $F_0$ constant and
$\mathbf v=-R^2\nabla u\times\nabla\phi+\mathbf v_{\mathrm{dia},i}+v_\parallel\mathbf B$,
$u$ being the electrostatic potential divided by $F_0$. Five fields
($\psi$, $u$, $\rho$, $T$, $v_\parallel$) are evolved and two are defined,
$j=\Delta^*\psi$ and the vorticity $\varpi$ (Hoelzl et al. 2021, §2.3.1, Eqs.
25–39, Table 1). The reduction is "not an aspect ratio expansion of the full
MHD model" (§2.3.1), which [Artola et al. (2021)](/sources/artola-2021.md)
(Abstract, §5) credit for capturing 3D VDE dynamics "even in the spherical
tokamak limit". The model keeps the Grad–Shafranov equilibrium with constant
$F_0$, conserves energy at equation level and momentum only globally, removes
fast magnetosonic waves, and fails for pressure-driven internal kinks at
finite $\beta$ through a spurious stabilizing term (Hoelzl et al. 2021,
§2.3.3, Figs. 18–19); [Nikulsin et al. (2022)](/sources/nikulsin-2022.md)
(§VIII) repeat that it "cannot accurately reproduce kink modes at higher β".

Variants of the reduced model used in the chunk-2 applications:
* **Pressureless two-field model** ($\psi$, $u$ only, flat constant density,
  no parallel flow, fixed boundary with $u=\varpi=j=0$) for double tearing
  modes ([Nardon et al. (2023b)](/sources/nardon-2023-b.md), Eqs. 1–2).
* **Two temperatures and an impurity density** with frictional heating of
  ablated particles and the ionization energy carried as potential energy,
  with coronal-equilibrium ([Hu et al. (2021)](/sources/hu-2021.md),
  Eqs. 1–12) or collisional-radiative impurities
  ([Hu et al. (2023)](/sources/hu-2023.md), Eqs. 1–17;
  [Hu et al. (2024)](/sources/hu-2024.md), §2.1). All species share one
  velocity; Spitzer resistivity with a Hirshman $Z_{\mathrm{eff}}$ factor and
  a temperature floor (2 keV in Hu et al. 2021 to resolve the resistive skin
  current, 1 eV in Hu et al. 2023).
* **Diamagnetic and bootstrap extensions for pedestals**: the ion
  diamagnetic velocity in the flow ansatz, a Sauter bootstrap current
  entering Ohm's law through $\eta(j-j_{\mathrm{src}})$ so that the current
  relaxes on the resistive time, and $v_\parallel$ set only by Mach-1
  conditions at the targets ([Cathey et al. (2024)](/sources/cathey-2024.md),
  §3.1; [Cathey et al. (2023)](/sources/cathey-2023.md), §2.2). The two-fluid
  version with toroidal rotation and neoclassical poloidal friction, at
  $T_i=T_e$, is used for ITER RMPs ([Becoulet et al. (2022)](/sources/becoulet-2022.md),
  §2). JOREK's heuristic ion stress for neoclassical poloidal-flow damping
  is "based off of" the Gianakon closure ([Howell et al. (2022)](/sources/howell-2022.md),
  §I, stated).
* **Fluid neutrals** with a transient Gaussian D$_2$ source for plasmoid-drift
  studies ([Kong et al. (2025)](/sources/kong-2025.md), §2).
* **Field-free fluid model** (all magnetic fields and currents set to zero,
  $\rho$, $u$, $T$ only) on a 1 m slab at $R=10$ m, used to generate blob
  data for neural-operator surrogates
  ([Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.1).
* **Wall-force runs** with Ohmic heating and radiation assumed to cancel,
  no density or temperature sources, and an artificial axisymmetric thermal
  quench by raised $\kappa_\perp$ ([Artola et al. (2022)](/sources/artola-2022.md),
  §2–3).

**Full MHD.** A [visco-resistive full-MHD model](/methods/visco-resistive-mhd-model.md)
evolves $\mathbf A$ in the Weyl gauge with $\mathbf B=F\nabla\phi+\nabla\times\mathbf A$,
$F(\psi)$ frozen from the equilibrium, and projects momentum on $\mathbf e_R$,
$\mathbf e_Z$ and $\mathbf B$, which removes $\mathbf J\times\mathbf B$ exactly
from the parallel projection (Hoelzl et al. 2021, §2.2, §2.12;
[Bhole et al. (2023)](/sources/bhole-2023.md), §3.3.5). It carries
diamagnetic terms, neoclassical friction, rotation and the bootstrap source,
but in 2021 no neutral model (Hoelzl et al. 2021, §2.12); Bhole et al. (2023)
(Eqs. 1–14) add a coronal-equilibrium impurity species. A two-temperature
version with resistivity acting only on the toroidal component of Ohm's law,
"to improve the numerical stability", is used for flux pumping over the
resistive time ([Zhang et al. (2025)](/sources/zhang-2025.md), §2.2, Eqs. 1–4).

**Extensions** (Hoelzl et al. 2021, §§2.4–2.14, unless cited otherwise):
drift-ordered diamagnetic Ohm's law, gyroviscous cancellation, neoclassical
friction and a current source $\mathbf J_x$ following the
[bootstrap current](/definitions/bootstrap-current.md) (§2.2); two
temperatures (§2.5); [fluid](/methods/fluid-neutral-models.md) and Monte Carlo
[kinetic](/methods/kinetic-neutral-model.md) neutrals (§2.6;
[Korving et al. (2023)](/sources/korving-2023.md), §III–IV);
[coronal-equilibrium](/methods/coronal-equilibrium-impurity-model.md) and
[collisional-radiative](/methods/collisional-radiative-impurity-model.md)
impurities (§2.7; [Hu et al. (2021b)](/sources/hu-2021-b.md), §2); pellet and
[shattered-pellet](/definitions/shattered-pellet-injection.md) ablation
sources (§2.8; Bhole et al. 2023, Eqs. 47–48); a
[runaway-electron fluid](/methods/runaway-electron-fluid-model.md) with
current coupling and no Dreicer source (§2.11;
[Bandaru et al. (2024)](/sources/bandaru-2024.md), §II); a kinetic particle
framework with full-orbit and guiding-centre pushers and moments
[projected onto the finite-element basis](/methods/particle-to-mesh-projection.md)
(§2.10), through which energetic particles enter by anisotropic
[pressure coupling](/methods/pressure-and-current-coupling.md)
([Bogaarts et al. (2022)](/sources/bogaarts-2022.md), §II); electrostatic ITG
fluid and fully kinetic models (§2.13–2.14). [Hoelzl et al. (2024)](/sources/hoelzl-2024.md)
(§5) call these "model families" that toggle extensions.

## Discretization

Isoparametric bicubic Bézier/Hermite finite elements in the poloidal plane,
four degrees of freedom per node and variable (value, two first derivatives,
mixed derivative) with element-specific scale factors (Hoelzl et al. 2021,
§3.1, Eqs. 51–54; Bhole et al. 2023, §3.3.2); see
[Bézier–Hermite finite elements](/methods/bezier-finite-elements.md). Hoelzl et
al. (2021) call them $G^1$, not enforced at the axis and near X-points; Bhole
et al. (2023) call them $C^1$ (see Contradictions). Grids are flux-surface
aligned per topological domain and can extend to the first wall; polar or
rectangular grids serve as initial grids and for VDEs (§3.1.2). Toroidally, a
real Fourier series with optional periodicity; with $N_{\mathrm{tor}}$
counting cosine and sine terms separately, at least $2(N_{\mathrm{tor}}-1)$
toroidal planes are needed for de-aliasing (§3.1.3). Since 2021:
arbitrary-order Bézier elements and axis regularization (Hoelzl et al. 2024,
§5).

## Time integration and solvers

* **Time stepping.** A linearized implicit three-level scheme containing
  Crank–Nicolson and BDF2 (Gear); implicit Euler is not used in production;
  the definition equations are imposed at the new level; full Newton iteration
  was tested and left out for cost and memory (Hoelzl et al. 2021, §3.2, App.
  C). Bhole et al. (2023) (Eq. 40) call the step one Newton iteration with an
  approximate Jacobian; BDF2 "does not conserve energy exactly" (Korving et al.
  2023, §V F). See [implicit time integration](/methods/implicit-time-integration.md).
* **Linear solver.** Restarted GMRES on the distributed sparse matrix (direct
  LU only for axisymmetric runs), preconditioned by a block-Jacobi in toroidal
  harmonics: each diagonal block is LU-factorized by PaStiX, MUMPS, WSMP or
  STRUMPACK, factors are reused until the GMRES count crosses a threshold, and
  "mode groups" may merge coupled harmonics; matrix-free assembly was rejected
  (Hoelzl et al. 2021, §3.4–3.5). BiCGSTAB and a preconditioner that retains
  some nonlinear harmonic couplings were added later (Hoelzl et al. 2024, §5).
* **Stabilization and boundaries.** VMS and Taylor–Galerkin terms (Hoelzl et
  al. 2021, §3.3); Bhole et al. (2023) add [VMS](/methods/variational-multiscale-stabilization.md)
  and [shock capturing](/methods/shock-capturing-artificial-viscosity.md) to
  full MHD, cutting the GMRES time of a 3D neon SPI run to $t\approx1.5$ ms
  from 13.6 h to 5 h on 64 MPI processes (Table 1). Dirichlet conditions on
  flux surfaces, [Bohm sheath conditions](/methods/sheath-boundary-conditions.md)
  where field lines hit the wall (Hoelzl et al. 2021, §2.3.2).

## Parallelism and GPU

Hybrid MPI and OpenMP; MPI tasks are a multiple of the number of harmonics,
the full plasma state is duplicated on all ranks (no particle migration), and
rank 0 handles I/O and the $n=0$ block (Hoelzl et al. 2021, §3.6). A JT-60SA
ELM case reaches about 50 % relative strong-scaling efficiency from 16 to 160
nodes (§3.6, Fig. 9). The 2021 code was CPU only; particles were later ported
to GPUs with OpenACC (Hoelzl et al. 2024, §5; Bogaarts et al. 2022, §II).
A 3D flux-pumping case over 700 ms costs about 0.5 M core-hours on
Marconi-Fusion; 3D runs over the resistive time of ITER or DEMO, where
$\tau_R/\tau_A$ is more than 10 and 40 times that of AUG, are judged
"impractical" (Zhang et al. 2025, §6.2). A 2D field-free blob run of 2000
steps costs about 350 core-hours (16 or 48 cores per run); this cost, and
2000 such runs as training data, motivate the
[Fourier-neural-operator surrogates](/methods/fourier-neural-operator-surrogates.md)
(Gopakumar et al. 2024, §2.1, §3.1.1).
A 3D ITER current-quench run with STARWALL costs about 5 million
core-hours, on the ITER cluster, Marconi-Fusion and Google Cloud
(Artola et al. 2022, §5); low-resistivity double-tearing runs are "very
expensive" (Nardon et al. 2023b, §IV).
Reported costs: 9000–10000 CPU-hours per steady state of ITER divertor runs
on 4 nodes of 36 cores (Korving et al. 2023, §V D); about 30 s per fluid step
of an axisymmetric impurity run on 4 nodes (Hu et al. 2021b, §2.2).

## Coupled codes

Free boundary and resistive walls via [STARWALL](/software/starwall.md) (thin
walls, Green's-function vacuum) and [CARIDDI](/software/cariddi.md) (3D
volumetric conductors); see [resistive-wall coupling](/methods/resistive-wall-coupling.md)
(Hoelzl et al. 2021, §2.9; [Isernia et al. (2023)](/sources/isernia-2023.md)).
GVEC and EXTENDER_P feed JOREK3D (Nikulsin et al. 2022, §I); HELENA and CASTOR
compute continua and NUBEAM distributions initialize markers (Bogaarts et al.
2022, §II, §V); IMAS, MUSCLE3 and RaySect workflows (Hoelzl et al. 2024, §5).

## Verification and benchmarks

From Hoelzl et al. (2021) unless cited otherwise:
* Growth-rate error $\propto$ (points per direction)$^{-5}$ on a tearing and a
  cbm18 ballooning case (§4.1); $\kappa_\parallel/\kappa_\perp>10^{10}$ resolved
  with 0.3 % error on a 200×200 aligned grid (§4.2); energy balance closed in
  VDE and RMP runs, to about 90 % in massive-injection runs (§4.3).
* Ballooning growth rates within 4 % of [BOUT++](/software/bout-plus-plus.md),
  reduced versus full peeling–ballooning within 5 %, nonlinear 2/1 tearing
  within 5 % of SpeCyl (§4.4–4.5); runaway fluid within 1 % of GO (§4.7), and
  the [ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md)
  (Bandaru et al. 2024).
* Free boundary: within 10–20 % of CEDRES++, a few cm of DINA, 20 % of CASTOR3D
  (§4.8); the [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md), thermal
  quench 0.14 ms against 0.24 (M3D-C1) and 0.20 ms (NIMROD) (Artola et al.
  2021, §4.1.3); JOREK–CARIDDI against JOREK–STARWALL within 2 % (VDE) and 1 %
  (tearing) (Isernia et al. 2023, §IV–V).
* [DIII-D gas injection](/benchmarks/diii-d-mgi-impurity-benchmark.md): the
  coronal model collapses about 2× slower than M3D-C1 and NIMROD (§2.7); the
  collisional-radiative model agrees with NIMROD, argon peak 0.15 ms later at
  constant $\eta$ (Hu et al. 2021b, §6).
* Kinetic neutrals against SOLPS-ITER: divertor power within 10 %, peak heat
  flux about 2× higher, detachment at about 10 % higher upstream density
  (Korving et al. 2023, §V C).
* [MARS-F](/software/mars-f.md): early-phase X-point displacement of the
  ITER 12.5 MA RMP case about 6–8 mm against about 7 mm linear; about 60 mm
  later in the nonlinear phase (Becoulet et al. 2022, §6).
* [ITPA TAE](/benchmarks/itpa-tae-benchmark.md) in "reasonable agreement" with
  the lowest frequencies of the set; [NLED-AUG](/benchmarks/nled-aug-benchmark.md)
  in good agreement in drive and structure (Bogaarts et al. 2022, §IV).

## Limitations

* Even with the implicit scheme, Alfvénic time steps limit ITER pedestal
  runs to a few tens of ms against a confinement time above 3 s, and the
  resistivity is set about two orders above the realistic central value
  (Becoulet et al. 2022, §2, §7). The ITER RMP model is fixed-boundary, with
  the ERGOS vacuum field imposed at the wall.
* The single-temperature model without a torque source over-deepens the
  pedestal radial-electric-field well and misplaces mode frequencies
  (Cathey et al. 2023, §2.2; Cathey et al. 2024, §3.2). MHD validity needs
  mode frequencies well below the ion cyclotron frequency; a smaller time
  step would not make faster physics valid (Cathey et al. 2023, §2.2).
* Wall-force runs used Dirichlet conditions ($T_e=1$ eV,
  $\mathbf v\cdot\mathbf n=0$, $v_\parallel=0$) instead of sheath conditions,
  so heat leaves only by conduction (Artola et al. 2022, §3, §4.4).

* Reduced MHD is wrong for finite-$\beta$ internal kinks (Hoelzl et al. 2021,
  §2.3.3), and its boundary (potential constant) acts as a poloidal ideal
  conductor, so the toroidal $I_p$ asymmetry of the 3D VDE is below 0.01 %
  against 1–1.4 % (M3D-C1) and 3–4 % (NIMROD) (Artola et al. 2021, §4.1.6;
  see the [Result](/results/reduced-mhd-current-asymmetry.md)).
* No implicit wall-potential coupling in 2021, halo currents only as a
  wall-force post-processor (Hoelzl et al. 2021, §2.9); JOREK–CARIDDI couples
  reduced MHD only, without halo currents (Isernia et al. 2023, §VII).
* Preconditioner memory, direct-solver scalability and degradation under
  strong mode coupling; refactorization almost every step dominates strongly
  nonlinear phases (Hoelzl et al. 2021, §3.5).
* Stabilization coefficients are tuned "based on experience", and $c=50$
  alters the thermal quench (Bhole et al. 2023, §4.3, §5); full-$f$ markers
  relax, and energetic-particle current coupling was "too noisy" (Bogaarts et
  al. 2022, §II, §IV).

## Applications in the cited sources

[ELMs](/definitions/edge-localized-mode.md) and RMP control (Hoelzl et al.
2021, §5; 2024, §2); [disruptions](/definitions/disruption.md) with
[shattered-pellet](/definitions/shattered-pellet-injection.md) and gas
injection, [thermal quench](/definitions/thermal-quench.md),
[VDEs](/definitions/vertical-displacement-event.md),
[halo currents](/definitions/halo-current.md), [wall forces](/definitions/wall-forces.md),
[vertical-force mitigation](/results/vertical-force-mitigation.md) and runaway
beams (Hoelzl et al. 2021, §6; 2024, §3; Artola et al. 2021; Bhole et al.
2023; Bandaru et al. 2024); detachment and the
[high-field-side high-density region](/results/high-field-side-high-density-region.md)
(Korving et al. 2023); Alfvén eigenmodes (Bogaarts et al. 2022).

Chunk-2 applications, with the resolution each paper states:

| Study | Application | Resolution and setup | Source |
|---|---|---|---|
| ITER mitigated current quench | 3D CQ, halo currents, wall forces after $I_p\to0$ | polar grid 100×200 bicubic Bézier elements, $n=0$–10; STARWALL with 75 000-triangle 3D inner vessel | [Artola et al. (2022)](/sources/artola-2022.md), §2 |
| ITER RMP ELM suppression | natural ELMs and $n=2$–4 RMPs at 15, 12.5, 10 MA | $n=1$–9 seeded; domain to the ITER wall; Bohm sheath at targets; ERGOS boundary field | [Becoulet et al. (2022)](/sources/becoulet-2022.md), §2 |
| AUG EDA H-mode | resistive peeling–ballooning modes and the QCM | 214×354 elements, 1.28 mm radial in the pedestal, 64 planes, $n=0$–13, ideal wall; $\Delta t$ one JOREK time unit (0.6687 µs), halved at times | [Cathey et al. (2023)](/sources/cathey-2023.md), §2.2 |
| AUG regimes without type-I ELMs; JT-60SA | QH, small ELMs, EDA; linear pedestal scans | $n=0$–6 (QH), even $n\le12$ (small ELMs), $n=0$–13 (EDA); double-X-point grid with JOREK's own Grad–Shafranov solve (JT-60SA) | [Cathey et al. (2024)](/sources/cathey-2024.md), §3–4 |
| JET Ar and ITER Ne/H SPI | TQ trigger at $q=2$ or $q=1$, radiation asymmetry, dual SPI | not stated ($n\ge6$ implied); MARCONI and Tianhe-3 | [Hu et al. (2021)](/sources/hu-2021.md), §2 |
| ITER Ne–D SPI, collisional-radiative | assimilation, 1/1-kink TQ, temperature holes | $n=0$–11; ideal wall at the thin-wall equivalent of the blanket | [Hu et al. (2023)](/sources/hu-2023.md), §2.2 |
| ITER H-mode dual SPI | plasmoid drift and first-wall energy impact | $n=0$–11; radiation ray-traced onto the ITER wall with Raysect/CHERAB in IMAS | [Hu et al. (2024)](/sources/hu-2024.md), §2 |
| JET plasmoid drift | drift velocity against shear-Alfvén and Pégourié braking theory | $n\le10$, fixed boundary, fluid neutrals | [Kong et al. (2025)](/sources/kong-2025.md), §2 |
| JET-like double tearing mode | resistivity window of violent relaxation | 120×64 flux-aligned elements, $n=0$–15 | [Nardon et al. (2023b)](/sources/nardon-2023-b.md), §II |
| W7-AS soft β limit (JOREK3D) | parallel flow and finite-element vacuum field | see [JOREK3D](/software/jorek3d.md) | [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) |

Chunk-3 applications:

| Study | Application | Resolution and setup | Source |
|---|---|---|---|
| AUG hybrid #36663, full MHD | [flux pumping](/definitions/magnetic-flux-pumping.md) and the [MHD dynamo](/definitions/mhd-dynamo.md) over 700 ms (3D) and 1.8 s (2D) | polar grid of 100×100 elements, $n\le4$ ($n\le1$ insufficient, $n\le2$ and $n\le4$ within 1%), $\Delta t=2.30\,\mu$s, implicit Gear scheme (order not stated), fixed boundary at the LCFS; about 0.5 M core-hours per 3D case | [Zhang et al. (2025)](/sources/zhang-2025.md), §2.4, §6.2 |
| HL-3 QH-mode, predictive | [edge harmonic oscillation](/definitions/edge-harmonic-oscillation.md), loss of QH-mode at lower $q_{95}$ | 11 136 $G^1$ Bézier elements in lower single null (71×121 inside the separatrix), $n=0$–12, ideal wall, Mach-1 sheath targets, Taylor–Galerkin stabilization; time step and solver not given | [Liang et al. (2025)](/sources/liang-2025.md), §III |
| AUG H-mode Ne/D SPI | two-stage thermal quench, scans of neon fraction, fragment size and speed | 70×110 flux-aligned X-point grid, $n=0$–7, ideal wall, $\Delta t=0.1$–2 normalized units (about 0.61 µs each); HAWK (HLRS) CPUs, no cost given | [Tang et al. (2025)](/sources/tang-2025.md), §3.1 |
| EU-DEMO upward hot VDE with runaway beam | 2D beam formation, 3D termination at $q_{95}\approx2.3$, wall loads | JOREK–STARWALL, polar grid (node counts not given), $n\le3$, 5 or 7; the 3D runs "would not have been possible" without the enhanced preconditioner of Holod et al. (2021, as cited); no time step or cost given | [Vannini et al. (2025)](/sources/vannini-2025.md), §5 |
| 2D blob data for surrogates | field-free fluid model | 200×200 bicubic elements, $\Delta t=0.15\,\mu$s, 2000 steps (300 µs), about 350 core-hours per run | [Gopakumar et al. (2024)](/sources/gopakumar-2024.md), §2.1 |

Liang et al. (2025, §III) state the orientation explicitly: JOREK's $\phi$
runs clockwise seen from the top. Zhang et al. (2025, §2.4) describe the
elements as "$G^1$-continuous … bi-cubic Bezier elements", a further
statement on the $G^1$ side of the continuity question below.

Of the chunk-2 papers only Cathey et al. (2023) state the time step; of
the chunk-3 papers Zhang et al. (2025), Tang et al. (2025) and Gopakumar
et al. (2024) state it, Vannini et al. (2025) name the preconditioner but
give no step, and Liang et al. (2025) give neither. The
[resonant magnetic perturbation](/definitions/resonant-magnetic-perturbation.md)
and [ELM](/definitions/edge-localized-mode.md) pages carry the pedestal
results.

## Contradictions

* **Continuity of the Bézier element.** *Open.* Hoelzl et al. (2021, §3.1) and
  Artola et al. (2021, Table 1, footnote G = geometric, C = parametric) say
  $G^1$, as do Zhang et al. (2025, §2.4) and Liang et al. (2025, §III); Bhole et al. (2023, §3.3.2) say $C^1$, the arc-length derivatives
  being shared. A statement of which derivatives are continuous across edges
  in physical space would settle it; recorded in full on
  [Bézier–Hermite finite elements](/methods/bezier-finite-elements.md).
* **Order of the Gear scheme.** *Open.* Artola et al. (2021, arXiv v1, §2,
  Table 1) print "BDF5 Gears"; Hoelzl et al. (2021, App. C), Bhole et al.
  (2023, Eq. 40) and Korving et al. (2023, §II C) describe BDF2. The published
  version of Artola et al. would settle it; recorded in full on
  [implicit time integration](/methods/implicit-time-integration.md).

# Citations

1. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §§1–7, App. C.
2. [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §§2–5.
3. [Artola et al. (2021)](/sources/artola-2021.md) — §2, Table 1, §4.
4. [Bhole et al. (2023)](/sources/bhole-2023.md) — §§2–5, Table 1.
5. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §I, §VIII.
6. [Isernia et al. (2023)](/sources/isernia-2023.md) — §§II–VII.
7. [Korving et al. (2023)](/sources/korving-2023.md) — §§II–V.
8. [Bogaarts et al. (2022)](/sources/bogaarts-2022.md) — §§II, IV, V.
9. [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §§II–IV.
10. [Hu et al. (2021b)](/sources/hu-2021-b.md) — §§2, 6.
11. [Artola et al. (2022)](/sources/artola-2022.md) — §§2–5.
12. [Becoulet et al. (2022)](/sources/becoulet-2022.md) — §§2, 6, 7.
13. [Cathey et al. (2023)](/sources/cathey-2023.md) — §2.2.
14. [Cathey et al. (2024)](/sources/cathey-2024.md) — §§3–4.
15. [Hu et al. (2021)](/sources/hu-2021.md) — §2.
16. [Hu et al. (2023)](/sources/hu-2023.md) — §2.
17. [Hu et al. (2024)](/sources/hu-2024.md) — §2.
18. [Kong et al. (2025)](/sources/kong-2025.md) — §2.
19. [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — §§II, IV.
20. [Ramasamy et al. (2024)](/sources/ramasamy-2024.md) — §2.
21. [Howell et al. (2022)](/sources/howell-2022.md) — §I.
22. [Zhang et al. (2025)](/sources/zhang-2025.md) — §2, §6.2.
23. [Liang et al. (2025)](/sources/liang-2025.md) — §III.
24. [Tang et al. (2025)](/sources/tang-2025.md) — §2.1, §3.1.
25. [Vannini et al. (2025)](/sources/vannini-2025.md) — §2–3, §5: model, numerics, preconditioner.
26. [Gopakumar et al. (2024)](/sources/gopakumar-2024.md) — §2.1, §3.1.1.
