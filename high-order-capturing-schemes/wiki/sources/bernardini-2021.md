---
type: Source
title: "Bernardini, Modesti, Salvadore & Pirozzoli (2021) — STREAmS: a high-fidelity accelerated solver for direct numerical simulation of compressible turbulent flows"
description: "Code paper for STREAmS, a CUDA Fortran finite-difference DNS solver for supersonic wall-bounded flows: kinetic-energy-preserving central fluxes of order 2–8 hybridized with characteristic WENO by a Ducros-type sensor, low-storage RK3, a staggered wall, GPU optimizations giving 2.2× on one V100 and 97% weak scaling on 1024 GPUs."
resource: "doi:10.1016/j.cpc.2021.107906"
source_kind: paper
authors: [Bernardini M., Modesti D., Salvadore F., Pirozzoli S.]
year: 2021
venue: "Comput. Phys. Commun. 263:107906"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2021-CPC-Bernardini-101016jcpc2021107906.pdf"
tags: [software, finite-difference, weno, hybrid, turbulence, gpu]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Merged into the new [STREAmS](/software/streams.md) software page and
the hybrid compact-WENO, conservative-FD and SSP pages.

# Key claims

1. **Equations** (§2): compressible Navier–Stokes, Sutherland viscosity,
   Prandtl 0.72, channel forcing.
2. **Fluxes** (§2.1, eqs. 4–8, page image): a locally conservative
   kinetic-energy-preserving central flux of order 2–8, hybridized at
   compressions with Lax–Friedrichs split characteristic WENO of order 1–7
   by a modified Ducros sensor. Eq. 8 prints $u_0^2/L_0$, which is not
   dimensionally consistent; reproduced as printed.
3. **Viscous terms** in Laplacian form to eighth order (eq. 9).
4. **Time** (§2.2, eqs. 10–14): low-storage RK3 with one negative
   coefficient (not SSP); time-step limits in wall units.
5. **Wall** (§3.1): on an interface node, for exact mass conservation and
   twice the time step.
6. **Validation** (§3): Mach 1.5 channel (full WENO3 and WENO5 too
   dissipative), Mach 2 and 5.86 boundary layers, Mach 2.28 oblique
   shock/boundary-layer interaction.
7. **GPU** (§4): dual host/device arrays, `!$cuf` kernels, layout and
   register optimizations (656 → 297 ms per step), CUDA-aware or staged MPI
   with overlap, 97% weak scaling on 1024 GPUs, and about 10 times faster
   and 21 times leaner than ZEFR at equal accuracy.

# Notation map

| Bernardini et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf w$, $u$, $v$, $w$ | $u$, $\mathbf v$ | |
| $E$ (per unit mass), $H$ | $E/\rho$, (words) | |
| $\mathbf R(\mathbf w)$ | $\mathcal L(u)$ | |
| $\theta$ (sensor) | (words) | registry $\theta$ is the limiter parameter; its threshold is $\vartheta$ |
| $\alpha_\ell$, $\beta_\ell$ (RK) | (words) | |
| $a_l$, $b_l$ | central-difference coefficients | collide with $a_{ik}$, $b_{ik}$ |
| $\Delta x$ | $h$ | |

# Pages created or updated

* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Hybrid compact-WENO schemes](/methods/hybrid-compact-weno.md).
* Created [STREAmS (compressible wall-turbulence DNS on GPUs)](/software/streams.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2021-CPC-Bernardini-101016jcpc2021107906.pdf` (doi:10.1016/j.cpc.2021.107906, checked on Crossref: Comput. Phys. Commun. 263:107906, June 2021; typeset publisher version): text extraction, all 14 pages; p. 3 (eqs. 4–12) read from the page image. Not stated: the sensor-to-interface rule, the splitting speed and the production CFL. Reference list: 63 entries (mostly without titles).
