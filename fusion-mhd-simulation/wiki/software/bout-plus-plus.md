---
type: Software
title: "BOUT++"
description: "Finite-difference plasma-fluid framework for 3D initial-value problems in field-aligned coordinates with quasi-ballooning derivatives and CVODE BDF time integration; a hybrid 2D/1D field solver removes the flute ordering for n = 0 and low-n modes, enabling full-annulus edge simulations that resolve a two-stage resistive drift-ballooning ELM crash, and its ideal-ballooning growth rates agree with ELITE and JOREK within 2–4 %."
status: established
aliases: [BOUT, BOUT++ framework]
tags: [reduced-mhd, edge, pedestal, elm, ballooning, finite-differences, time-integration, linear-solver, verification]
timestamp: 2026-10-16T18:35:00Z
---

# BOUT++

BOUT++ is a framework for 3D plasma-fluid equations posed as initial-value
problems in curvilinear geometry and discretized by finite differences
([Seto et al. (2023)](/sources/seto-2023.md), §1–2). The extension described
here is built on version 3.1. It is used for tokamak edge MHD and turbulence,
including ELM simulations (§1, §5). [Jiang et al. (2024)](/sources/jiang-2024.md)
(§I) cite it as a field-aligned code, and
[Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§I, §III) list it among
codes applicable to stellarators and base their Python Dommaschk-potential
implementation on a BOUT++ version.

## Coordinates and discretization

* Fields are stored in [field-aligned coordinates](/methods/field-aligned-coordinates.md):
  $x=\psi-\psi_{\mathrm o}$, $y=\theta$, and $z$ the toroidal angle minus the
  integrated field-line pitch, with twist-shift periodicity at the $y$
  boundary (Seto et al. 2023, §2, Eqs. 5–9).
* Derivatives are taken in "quasi-ballooning" coordinates, which combine the
  field-aligned system with orthogonal flux-surface coordinates through the
  shifted radial derivative and the shifted metric, so the integrated shear
  disappears from the metric and from every operator (§2, Eqs. 12–14).
* Transforms between field-aligned and flux-surface coordinates are an FFT in
  the toroidal angle plus a phase shift; the axisymmetric equilibrium lets the
  two poloidal planes share grid points (Eqs. 10–11).
* A toroidal wedge $0\le\phi<2\pi/N$ keeps only multiples of $N$ (§1, §2).

## Time integration and field solvers

* Time integration is BDF through CVODE (SUNDIALS) (Seto et al. 2023, §2).
  See [implicit time integration](/methods/implicit-time-integration.md).
* The vorticity–potential Helmholtz equation is the expensive elliptic step.
  The standard solver applies the flute ordering, dropping parallel
  derivatives, and solves 1D radial tridiagonal systems per toroidal mode by
  the Thomas algorithm or parallel variants (Eq. 17). This is invalid for
  $n=0$ and may fail at low $n$, which is why earlier BOUT++ runs dropped the
  $n=0$ component and used wedges with $N\sim5$ (§1, §3.1).
* The extension adds a [hybrid 2D/1D field solver](/methods/hybrid-2d-1d-field-solver.md):
  modes $0\le n\le n_{2D\max}$ are inverted in the orthogonal
  $(\psi,\theta)$ plane without flute ordering, with fourth-order central
  differences on a nine-point star stencil and PETSc GMRES preconditioned by
  Hypre AMG; modes up to $n_{1D\max}$ use the 1D solver; the results are
  summed in Fourier space (§3.2–3.3, Eqs. 19–20, Fig. 1). The perpendicular
  Laplacian and the gradient-coefficient term in the evolution equations use
  the same split. Because the 2D grid is not field aligned, it must resolve
  poloidal mode numbers of order $nq$, which restricts it to low $n$ (§3.2).
  For the 2D problem AMG is "more effective" than the SOR preconditioner of
  the earlier $n=0$-only solver (§3.1; no numbers).
* Parallelism is MPI through BOUT++ and PETSc; no GPU (§5.3).

## Physics models in the cited sources

* A linear three-field peeling–ballooning [reduced MHD](/methods/reduced-mhd.md)
  model: vorticity, parallel vector potential and pressure (Seto et al. 2023,
  §4, Eqs. 21–27).
* A two-fluid four-field model for drift-wave resistive ballooning modes, with
  ion diamagnetism through a generalized flow potential, Chang–Callen
  gyroviscous cancellation, resistivity and hyper-resistivity (§5.1, Eqs.
  28–35).
* Only the flute ordering of the field solver is removed; the flute ordering
  inside the reduced model remains (§1).

## Verification and benchmarks

* **[cbm18 ideal-ballooning benchmark](/benchmarks/cbm18-ballooning-benchmark.md)**
  (cbm18_dens8; $\tau_A$ is based on a reference length of 3 m and 2 T,
  $3.08\times10^{-7}$ s): at $n=20$, $\gamma\tau_A=0.244$ (2D solver) and $0.246$ (1D
  solver), against an earlier BOUT++ value of 0.245 and ELITE's 0.239. The
  1D–2D difference grows from about 1 % at $n=20$ to about 36 % at $n=5$,
  which the authors read as the $O(1/n)$ flute-ordering error (Seto et al.
  2023, §4, Fig. 3). They state that the 2D solver reduces "to some level" the
  low-$n$ overestimate of BOUT++ relative to ELITE and GATO found in Dudson et
  al. (2011), without re-plotting those codes at low $n$ (§4, §6).
* **JOREK**: linear ballooning growth rates in a circular case (aspect ratio
  3.3, $q_{95}=3$, density $10^{19}$ m$^{-3}$, $\eta=6.1\times10^{-6}\,\Omega$ m)
  agree within 4 % with and without diamagnetic effects; there is no
  nonlinear comparison ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md),
  §4.5, Fig. 21).

## Applications in the cited sources

Pedestal collapse driven by drift-wave resistive ballooning modes on the
cbm18_dens4 equilibrium ($\tau_A$ based on 3.5 m and 2 T) (Seto et al.
2023, §5; see
[ballooning mode](/definitions/ballooning-mode.md) and
[edge-localized mode](/definitions/edge-localized-mode.md)):
* the linear spectrum peaks at $n=32$ with $\gamma\tau_A=7.86\times10^{-2}$;
  modes $n\le10$ and $n\ge53$ are stable; 1D and 2D solvers differ by 2–8 % for
  $n=11$–20 (Fig. 5b);
* $n_{2D\max}=4$ suffices: 4, 8 and 12 give nearly the same energy loss and
  spectra (Fig. 6);
* full torus ($N=1$) and quarter torus ($N=4$) reach a similar final energy
  loss (about 6.5–7 % of the pedestal energy), but in the full torus low-$n$
  and zonal modes grow first, the spectral peak shifts down and the collapse
  comes later ($313\,\tau_A$ against $231\,\tau_A$); a tearing-like $(2,1)$
  global structure coexists with high-$n$ filaments (Figs. 7–10). The authors
  conclude that wedges give the energy loss but a full annulus is needed for
  the loss process (§5.3).
* Cost: $8.3\times10^5$ core-hours for the full-torus run (4096 cores for
  8.5 days on JFRS-1), about 40 % in the field solver (§5.3).

[Seto et al. (2024)](/sources/seto-2024.md) analyse the same full-torus run
(compiler's identification by identical model, coefficients and spectrum)
and add a half-torus run (see
[two-stage ELM crash](/results/two-stage-elm-crash.md)):
* the energy-loss rate has two peaks; the 2023 saturation at about
  $210\,\tau_A$ is a first, small crash and the 2023 collapse at about
  $313\,\tau_A$ the second, main crash, $103\,\tau_A$ later (compiler's
  cross-check of the two papers);
* the crash interval is $103$, $64$ and $3\,\tau_A$ for wedge numbers
  $N=1$, 2 and 4, with the final loss at about 6% of the pedestal energy for
  all three; the fundamental islands of a $2\pi/N$ wedge are $2N/N$ and
  stochastize sooner (§III, Figs. 13–15);
* setup: $N_z=256/N$ binormal points so the binormal spacing is the same
  for every wedge, $n\ge81$ removed by a low-pass filter, initial
  perturbations on all harmonics except $n=0$ (§II);
* per-$n$ energy budgets with three-wave decompositions of the
  $E\times B$ convection and Maxwell-stress transfer identify the trigger of
  each crash (Eqs. 6–29).

## Limitations

* Version 4.4.2 stores fields in flux-surface coordinates but still
  differentiates in quasi-ballooning coordinates, so low-$n$ handling "is
  therefore still an open issue" there (Seto et al. 2023, footnote 1).
* The equilibria are shifted circles without an X-point, and the simulation
  domain lies inside the last closed surface (§5.1).
* In the pedestal-crash model the parallel Laplacian is linearized (no
  magnetic flutter), the hyper-resistivity is constant and there is no
  neoclassical poloidal flow, so the stochastic electron heat transport and
  stochastic hyper-resistivity are absent: "ELM energy loss in this work is
  driven by E × B convection and numerical diffusion" (Seto et al. 2024,
  §II).
* No run cost is given for the 2024 runs (Seto et al. 2024, §II).

## Contradictions

* **Low-$n$ ballooning overestimate.** *Open (indirect).* Seto et al. (2023,
  §4, §6) state that their 2D solver corrects "to some level" the low-$n$
  overestimate of flute-ordered BOUT++ growth rates relative to ELITE and GATO
  reported by Dudson et al. (2011); the evidence is the 1D–2D gap (36 % at
  $n=5$), not a new overlay with ELITE or GATO. A low-$n$ comparison of the 2D
  solver with ELITE on cbm18_dens8 would settle it. Recorded in full on the
  [cbm18 benchmark](/benchmarks/cbm18-ballooning-benchmark.md).

# Citations

1. [Seto et al. (2023)](/sources/seto-2023.md) — §§1–6, App. A, Figs. 1–10.
2. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §4.5, Fig. 21.
3. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §I, §III.
4. [Jiang et al. (2024)](/sources/jiang-2024.md) — §I.
5. [Seto et al. (2024)](/sources/seto-2024.md) — §§II–IV, Eqs. 1–34, Figs. 3–15.
