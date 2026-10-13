---
type: Source
title: "Orszag & Tang (1979) — Small-scale structure of two-dimensional magnetohydrodynamic turbulence"
description: "Pseudospectral simulations of incompressible, viscous and resistive 2D MHD from the initial data later called the Orszag–Tang vortex; the dissipation peak falls about 20% per halving of the diffusivities; no shocks, and the divergence holds identically through the scalar potential."
resource: "doi:10.1017/S002211207900210X"
source_kind: paper
authors: [Orszag S.A., Tang C.-M.]
year: 1979
venue: "J. Fluid Mech. 90:129-143"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1979-JFM-Orszag-101017S002211207900210X.pdf"
tags: [benchmark, mhd, turbulence, spectral, incompressible]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A turbulence study, not a numerical-methods or benchmark paper. It asks
whether 2D MHD develops finite-time singularities (Pouquet's conjecture),
by direct simulation of the **incompressible, viscous and resistive** 2D
MHD equations in vorticity and scalar-potential form on a $2\pi$-periodic
box, with a pseudospectral Fourier method (up to $256^2$ modes). Its
non-random initial condition (eq. 7) is the ancestor of what later
compressible-MHD papers call the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md). The diagnostic is
the energy dissipation rate as the viscosity and magnetic diffusivity
(set equal) go to zero: its peak drops by about 20% per halving, which the
authors read as 2D MHD being "less singular than 3D hydrodynamics but more
singular than 2D hydrodynamics" (abstract; §3). At $t = 1$ the current
shows an S-shaped sheet at the box centre (Fig. 7). No shocks, density,
pressure, $\gamma$, $\beta$ or Mach number appear in the paper.

# Key claims

1. **Equations** (§2, eqs. 1–3). Vorticity equation with the Lorentz
   torque and viscous diffusion (eq. 1); advection–diffusion of the
   out-of-plane potential $A_z$ with magnetic diffusivity (eq. 2);
   $\nabla\cdot\mathbf B = 0$ and $\nabla\cdot\mathbf u = 0$ (eq. 3). The
   field is $\mathbf B = \nabla\times(A_z\hat{\mathbf z})$. Periodic box of
   side $2\pi$; all fields are Fourier series.
2. **Invariants and dissipation** (§2, eq. 4). Total energy, mean-square
   potential and cross-helicity are inviscid invariants; the dissipation
   rate is the viscous enstrophy plus the resistive current-squared
   integral.
3. **Numerical method** (§2). Pseudospectral with truncated Fourier series
   (Gottlieb & Orszag 1977); a modification of the KILOBOX code; 9 FFTs
   per step for MHD; about 6 s per step at $256^2$ on a CDC 7600;
   energy-dissipation results accurate to better than 1%. The time
   integrator, de-aliasing rule and time step are not stated.
4. **Initial condition** (§3, eq. 7): $\mathbf u = (-\sin y, \sin x)$,
   $A_z = \cos y + \tfrac12\cos 2x$, hence (compiler arithmetic)
   $\mathbf B = (-\sin y, \sin 2x)$, unit amplitude per component and equal
   initial kinetic and magnetic energy. "An analytical solution of
   (1)–(3) with these initial conditions does not seem possible" (§3).
5. **Resolution** (§3). Equal viscosity and diffusivity $\ge 0.02$:
   $64^2$ modes; 0.01: $128^2$; 0.005: $256^2$. Magnetic Prandtl numbers
   $\tfrac12$, 1, 2.
6. **Dissipation scaling** (§3, Fig. 1). For diffusivities 0.08 to 0.005
   (initial Reynolds numbers 36 to 1474), halving them lowers the peak
   dissipation by about 20%; random Gaussian initial data give about 26%
   (Fig. 2); 3D Taylor–Green changes about 10% per factor 4 (Fig. 3). The
   results "do not support Pouquet's hypothesis" of a finite nonzero
   limit.
7. **Enstrophy** (§3, Fig. 4): maximum kinetic-enstrophy enhancement
   about 2, $3\tfrac12$ and 10 at diffusivities 0.04, 0.02 and 0.005,
   peaking near $t \sim 1.5$.
8. **Structure** (§3, Figs. 7–12): at $t = 1$ and diffusivity 0.005, the
   current has "the distinctive S-shaped local structure" at the centre;
   the non-magnetic comparison flow is less intermittent.
9. **Mechanism** (§4): field lines wrap into ropes, reconnect by
   diffusion and snap back; this "does not give convincing proof" of an
   inviscid singularity.

**Divergence.** None as a numerical issue. $\nabla\cdot\mathbf B = 0$
holds identically because the field is evolved only through $A_z$ and
recovered by a spectral curl. No divergence is measured or discussed.

# Tests

| § / Fig. | Set-up | Findings |
|---|---|---|
| §3, Fig. 1 | eq. 7; diffusivities 0.08–0.005; $64^2$–$256^2$; $t \le 1.5$ | dissipation peak about 20% lower per halving |
| §3, Fig. 2 | Gaussian random data (eq. 8); 0.02, 0.01 | peak about 26% lower at 0.01 |
| §3, Fig. 3 | 3D Taylor–Green, non-magnetic | about 10% per factor 4 in viscosity |
| §3, Fig. 4 | eq. 7, viscosity and diffusivity in $\{0.02, 0.04\}$ | magnetic enstrophy set mainly by the diffusivity |
| §3, Fig. 5 | eq. 7, 0.02 | strong kinetic–magnetic energy exchange |
| §3, Fig. 6 | eq. 7 with magnetic-to-kinetic energy ratio $10^{-4}$ | seed-field growth "not inconsistent with growth to a finite level" |
| §3, Figs. 7–11 | eq. 7, 0.005, $t = 1$ | S-shaped central current sheet |
| §3, Fig. 12 | non-magnetic, eq. 9, 0.005, $t = 1$ | less intermittent vorticity |

# Notation map

| Orszag & Tang | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf h$ (magnetic field) | $\mathbf B$ | **collision:** $h$ is the grid spacing |
| $\mathbf v$ | $\mathbf u$ | velocity |
| $A$ ($\mathbf A = A\hat{\mathbf z}$) | $A_z$ | continuous potential, as on [vector-potential evolution](/methods/vector-potential-evolution.md) |
| $\zeta$ (vorticity), $j$ (current) | words | **collision risk:** $\omega_k$ are WENO weights |
| $\nu$, $\mu$ | words (kinematic viscosity, magnetic diffusivity) | not registered |
| $E$, $E^v$, $E^m$ | words (energies) | **collision:** $E_h$ is the electric field |
| $\epsilon(t)$ | words (dissipation rate) | distinct from $\epsilon_{\mathrm W}$ |
| $k$ | words (wavenumber) | **collision:** $k_{\mathrm s}$ stencil size |
| $R^v$, $R^m$ | words (Reynolds numbers, eqs. 5–6) | microscale-type definitions |

# Pages created or updated

* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md): an **Origin** paragraph and the qualification of "steepens into shocks".

# Citations

1. `~/papers/mosaic/div-free-amr/1979-JFM-Orszag-101017S002211207900210X.pdf`.
   * **Version read.** The published journal version, a 15-page scan with
     an OCR text layer (Acrobat Paper Capture). Received 6 October 1977.
   * **Identity.** doi:10.1017/S002211207900210X, checked on Crossref:
     title and authors match; J. Fluid Mech. vol. 90, issue 1, pp.
     129–143, published 16 January 1979. Page 1 prints "Steven A.
     Orszag" and "Cha-Mei Tang"; running heads "S. A. Orszag and C.-M.
     Tang".
   * **How it was read.** Text extraction; every equation used was checked
     on 300-dpi renders of pp. 130, 131, 133, 135, 142 and 143, because the
     OCR layer garbles exponents and fractions (eqs. 5, 6, 8, the decaying
     solution, "$3\tfrac12$").
   * **Recorded as printed.** The text cites "Frisch & Bardos 1976,
     unpublished" (§1), absent from the reference list and not merged.
     Figure values are read from plots only where stated; the equal
     initial energy split is compiler arithmetic from eq. 7.
   * **Reference list.** 10 entries, all merged; six print no title. The
     bibliography author was corrected to S.A. Orszag from page 1: the
     earlier note's "A. Orszag" is a citing source's spelling. The key
     `orszag-1979` was renamed `orszag-tang-1979` to match this page. The
     bibliography holds 3834 entries after this batch.
