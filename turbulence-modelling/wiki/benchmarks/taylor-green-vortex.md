---
type: Benchmark
title: "Taylor–Green vortex"
description: "The triply periodic vortex flow started from a single-mode analytic field that transitions to turbulence and decays, used at Re 40,000 against a 5400³ DNS to separate explicit Smagorinsky and implicit LES errors, and in its 2D analytic form to compare continuous and discrete commutator errors."
status: established
aliases: [TGV, Taylor-Green vortex, 2D Taylor–Green vortex]
tags: [benchmark, les, implicit-les, sgs-model, dns]
timestamp: 2026-10-25T13:45:00Z
---

# Taylor–Green vortex

The Taylor–Green vortex (TGV) starts from a single-mode, divergence-free
velocity field in a periodic box. In three dimensions the initial vortices
stretch, break down into turbulence and then decay, so a single run sweeps a
laminar phase, a transition with a peak of dissipation, and decaying
turbulence. Because the initial condition is analytic and the box periodic,
every reference and LES run of the same $Re$ starts from the same state and
filtered DNS can be compared with LES at the same time instant. In two
dimensions the vortex is an exact decaying solution of the Navier–Stokes
equations and serves as an analytic test of filtering and discretization
operators.

## Three-dimensional TGV as an LES benchmark

**Set-up.** [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md),
§6.1, Eq. (43), use the cube $[0,2\pi]^3$ with
$$u=\sin x\cos y\cos z,\qquad v=-\cos x\sin y\cos z,\qquad w=0,$$
incompressible flow and $Re=1/\nu=40{,}000$. The Taylor-scale Reynolds
number after breakdown is about 400 ($Re_\lambda\approx493$ at $t=10$,
$\approx389$ at $t=15$). The reference DNS has $5400^3$ nodes, run on the
impermeable sub-box $[0,\pi]^3$ using the flow's symmetries (eight times
fewer degrees of freedom), over $0\le t\le20$. Diagnostics are the volume
averages
$$K=\frac{1}{(2\pi)^3}\int\tfrac12u_iu_i\,d^3x,\qquad \varepsilon=\frac{1}{(2\pi)^3}\int\nu\,\partial_ju_i\,\partial_ju_i\,d^3x,\qquad \frac{dK}{dt}=-\varepsilon,$$
(Eqs. 44–46), with LES total dissipation $-d\bar K/dt$, and shell-averaged
spectra $E(k)$, the spectral eddy viscosity and the effective filter
transfer function $\sqrt{E_{\mathrm{LES}}/E_{\mathrm{DNS}}}$ (§6.3).

**LES meshes** (cubic cells, cutoff $k_c=\pi/h$ with $h$ the cell size):

| Mesh | Nodes | $k_c$ | DNS cutoff over $k_c$ | Cost reduction against DNS |
|---|---|---|---|---|
| VHR | $1080^3$ | 540 | 5 | not stated |
| HR | $540^3$ | 270 | 10 | $10^4$ |
| LR | $216^3$ | 108 | 25 | $25^4$ |

The solver is the sixth-order compact finite-difference code Incompact3d
with skew-symmetric (kinetic-energy-conserving) convection and third-order
time stepping (§3).

**What it shows.** The case separates the error of an explicit model from
the error of the discretization it runs on:

- *Truncated Euler and no model.* Without viscosity the kinetic-energy-conserving
  scheme keeps $K$ within 1% over $0\le t\le20$ and evolves to a thermalized
  spectrum $E(k)\sim k^2$. A no-model LES on the LR mesh thermalizes over more than
  80% of the wavenumbers, piles energy near $k_c$ from $t=5$ and overestimates the total
  dissipation during breakdown (§6.2, Figs. 4–7). The same $k^2$
  equipartition appears for no-model runs of
  [homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).
- *Smagorinsky.* With $C_s=0.1$ and the filter width equal to the cell size,
  the [Smagorinsky model](/methods/smagorinsky-model.md) cannot control the
  pile-up and over-dissipates. At fixed $\Delta=\pi/108$, numerical
  convergence through breakdown is reached only with $h=\Delta/5$
  ($k_c=540$), equivalent to $C_s=0.5$ in the cell-based form (§6.3, Figs.
  7–12).
- *Implicit spectral vanishing viscosity.* The
  [spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
  form of [implicit LES](/definitions/implicit-les.md) prevents
  thermalization and captures the dissipation peak. The authors report LR
  and HR runs at fixed $\Delta$ as "virtually identical" (not shown). The
  model misses the low-wavenumber plateau of the a priori spectral eddy
  viscosity, which carries up to 24%, 16% and 6% of the total dissipation at
  LR, HR and VHR (§6.4, Figs. 13–18).

The numerical viscosity ratios that §5.3 derives for the HR and LR
cutoff ratios are $\nu_0/\nu=181$ and 700; §6 does not restate the values
used. Details of these results live on the model pages linked above and on
[spectral eddy viscosity](/methods/spectral-eddy-viscosity.md) and
[numerical dissipation](/properties/numerical-dissipation.md).

## Two-dimensional analytic TGV as a commutator test

[Agdestein & Sanderse (2025)](/sources/agdestein-2025.md), App. F, use the
2D TGV on $[0,2\pi]^2$ (Eq. F.1),
$$u=-\sin x\cos y\,e^{-2\nu t},\qquad v=\cos x\sin y\,e^{-2\nu t},\qquad p=\tfrac14(\cos2x+\cos2y)\,e^{-4\nu t},$$
not as a simulation but to compute the convective subfilter force in closed
form. Under a continuous top-hat filter of width $\Delta$, the
$x$-component of the force is
$$c_x=-\tfrac12\big(\mathrm{sinc}^4(\Delta/2)-\mathrm{sinc}(\Delta)\big)\sin2x=-\frac{\Delta^4}{480}\sin2x+O(\Delta^6)$$
(Eqs. F.9, F.12). The discrete commutator of the staggered second-order
scheme with a discrete top-hat filter has the same $\sin2x$ dependence but a
different coefficient (Eqs. F.29–F.30). The authors conclude that a closure
trained on discretize-first data is inconsistent with a filter-first LES
equation (see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)
and [divergence-consistent LES](/methods/divergence-consistent-les.md)).

The 3D initial condition of Vicente Cruz & Lamballais and the 2D solution of
Agdestein & Sanderse differ by an overall sign of the velocity *(compiler check, not in the
sources)*.

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §3; §5.3; §6.1–6.5, Eqs. (43)–(46), Figs. 4–22.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — App. F, Eqs. (F.1), (F.5), (F.9), (F.12), (F.29)–(F.30).
