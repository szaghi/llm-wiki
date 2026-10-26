---
type: Software
title: "GHOST"
description: "GHOST (Geophysical High-Order Suite for Turbulence) is a pseudo-spectral community code with hybrid MPI/OpenMP/CUDA parallelism, second-order Runge–Kutta time stepping and two-thirds de-aliasing; in the sources it runs decaying compressible Hall-MHD DNS and serves as the reference for a lattice Boltzmann MHD code."
status: established
aliases: [ghost, Geophysical High-Order Suite for Turbulence]
tags: [software, mhd, plasma, dns, gpu]
timestamp: 2026-10-26T07:35:00Z
---

# GHOST

**GHOST** (Geophysical High-Order Suite for Turbulence) is a pseudo-spectral
framework for periodic-box turbulence that hosts a family of solvers for
geophysical fluids and space plasmas. Two ingested sources use it, both for
[direct numerical simulation](/definitions/direct-numerical-simulation.md)
of MHD-type turbulence without any closure: [Ferrand et al.
(2022)](/sources/ferrand-2022.md) produce with it the $1024^3$ decaying
compressible Hall-MHD runs on which they test [exact
laws](/results/turbulence-exact-laws.md), and [Foldes et al.
(2023)](/sources/foldes-2023.md) take it as the reference against which they
validate a [lattice Boltzmann](/methods/lattice-boltzmann-method.md) MHD
code. Neither source develops GHOST; both describe it as recalled from its
authors' papers (Gómez et al. 2005 and Mininni et al. 2011 in Ferrand et al.;
Mininni et al. 2011 and Rosenberg et al. 2020 in Foldes et al.).

## Discretization and parallelism

As described by Foldes et al. (2023, §4.4):

- **Spatial discretization.** Pseudo-spectral (Fourier) in a periodic cube,
  de-aliased by the classical two-thirds rule, which the authors credit with
  "very high accuracy in resolving the spatial scales" (Patterson & Orszag
  1971, as recalled). With de-aliasing the largest resolved wavenumber is
  $k_{\max}=N_x/3$ for $N_x$ points per direction, against the Nyquist
  $k_{\max}=N_x/2$ of their lattice Boltzmann code (§4.4).
- **Time integration.** Second-order Runge–Kutta.
- **Parallelism.** Hybrid MPI/OpenMP/CUDA, with GPU capability for several
  of its solvers, and "an optimal scaling up to hundreds of thousand
  computing cores"; it is presented as "a well-established community code"
  distributed on GitHub (§4.4). No scaling data are given in either source.

Ferrand et al. (2022, §3.1) use a module for **compressible Hall MHD** with
an optional uniform background field, run in dimensionless units in a box of
side $L_0=2\pi$.

## Uses in the sources

| Source | Equations | Grid | Parameters | Role |
|---|---|---|---|---|
| Ferrand et al. (2022, §3.1, Table 1) | isothermal compressible Hall MHD, free decay | $1024^3$ (one run $512^3$) | $\nu=\eta_m=3\times10^{-4}$, ion inertial length $0.02L_0$, mean field $B_0\in\{0,2\}$, initial sonic Mach number 0.25 or 0.5 | data for testing exact laws; see [compressible MHD turbulence](/results/compressible-mhd-turbulence.md) |
| Foldes et al. (2023, §4.4, Figs. 10–12) | MHD (no Hall term), Orszag–Tang decay | $512^3$ | amplitudes $U_0=1$, $B_{\mathrm{OT}}=0.8$ (no mean field), box $2\pi$, $Pm=1$, $Re\simeq1600$ at peak dissipation | reference solution for the LB code |

**As a reference solution.** Foldes et al. (2023, §4.4) run the same
Orszag–Tang decay (initial fields on [decaying MHD
turbulence](/results/decaying-mhd-turbulence.md)) with GHOST and with their
lattice Boltzmann code FLAME at $N_x=512$. They find the mean current
$\langle|\boldsymbol J|^2\rangle(t)$ and the kinetic and magnetic energies in
"very satisfactory" agreement, with a slight underestimation of the magnetic
dissipation by the LB run for a few steps after the peak (Fig. 10). The
magnetic spectra "perfectly match"; the LB kinetic spectrum is over-damped
at high wavenumbers and comes close to the $N_x=512$ GHOST spectrum only at
LB resolution $N_x=768$, which the authors call "qualitatively consistent" with
the statement of Shen et al. (2018), as recalled, that lattice Boltzmann
needs about twice the spatial resolution of a pseudo-spectral code
(Fig. 11). The spectral energy fluxes agree over all resolved wavenumbers
(Fig. 12). See [numerical dissipation](/properties/numerical-dissipation.md)
for the attribution of the LB over-damping to its collision operator.

## Time step in Hall MHD

Both sources state the same limitation of explicit Hall-MHD solvers, GHOST
included: whistler waves, whose phase speed grows linearly with the
wavenumber, impose a time step proportional to the square of the grid
spacing. Ferrand et al. (2022, §4) write the bound as "roughly"
$\sim(dx)^2/(d_iB)$ ($d_i$ the ion inertial length, page-local), so that
enlarging $d_i$ at fixed fine resolution becomes prohibitive, and recommend
hyperviscosity and hyperdiffusivity instead. Foldes et al. (2023, §3.4,
Eq. 3.41) derive $\Delta t\le\mu_0(\Delta x)^2/(\pi\alpha_HB)$, with
$\alpha_H=1/(en)$ the Hall parameter (page-local; $e$ the elementary charge,
$n$ the number density). For plain MHD they recall (Horstmann et al. 2022)
that an explicit lattice Boltzmann time step is smaller than that of an
incompressible pseudo-spectral code by roughly the Mach number, because it
resolves sound waves, so LB has little turnaround advantage there. In Hall
MHD both codes are whistler-limited, and the authors state that LB on GPUs then
gives "significantly smaller" wall-clock turnaround times (§5).

## Qualifications

- Foldes et al. (2023, §5) report no GHOST timing, for Hall-MHD or plain
  MHD runs, alongside their turnaround statement. Their timings (2.7 billion lattice updates per
  second at $512^3$ on 3 GPUs, §5) concern the LB code only.
- The GHOST comparison of Foldes et al. covers MHD without the Hall term;
  their Hall-MHD runs (Table 2) have no GHOST counterpart.

# Citations

- [Ferrand et al. (2022)](/sources/ferrand-2022.md) — §3.1, Table 1 (GHOST compressible Hall-MHD module, run set-up); §4 (whistler time-step bound, hyperviscosity recommendation).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — §3.4, Eq. (3.41) (whistler time-step bound); §4.4, Figs. 10–12 (GHOST description, Orszag–Tang comparison); §5 (time-step and turnaround discussion).
