---
type: Benchmark
title: "Taylor–Green vortex"
description: "The triply periodic vortex flow started from a single-mode analytic field that transitions to turbulence and decays: at Re 40,000 against a 5400³ DNS to separate Smagorinsky and implicit LES errors, at Re 1600 to measure numerical dissipation and test subgrid models, inviscid to tune spectral vanishing viscosity, and in 2D to compare commutator errors."
status: established
aliases: [TGV, Taylor-Green vortex, 2D Taylor–Green vortex, inviscid Taylor–Green vortex]
tags: [benchmark, les, implicit-les, sgs-model, dns, numerical-dissipation]
timestamp: 2026-10-25T19:46:00Z
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

## Three-dimensional TGV at $Re=1600$ and inviscid

**Set-up.** Three sources use the same initial velocity as above,
$u=\sin x\cos y\cos z$, $v=-\cos x\sin y\cos z$, $w=0$ on $[0,2\pi]^3$
(scaled by a length $L=1$ and velocity $V_0=1$), with $Re=V_0L/\nu=1600$ or
no viscosity. The compressible solvers add the pressure field
$p=p_0+\tfrac{1}{16}\rho_0V_0^2(\cos2x+\cos2y)(\cos2z+2)$ at low Mach number:
[Cao et al. (2022)](/sources/cao-2022.md), §3.1, at Mach 0.1 with
$\gamma=1.4$, $Pr=0.71$, $0\le t\le20$; [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md),
§6.1, Eq. (124), with $p_0=100$ and no viscosity (their Eq. 124 prints the
pressure product expanded; the two forms agree *(compiler check, not in the
sources)*). [Prakash et al. (2022)](/sources/prakash-2022.md),
§III.B.2, solve the incompressible equations and analyse only the transition
to the fully turbulent state.

| Source | Solver | Resolution | Reference |
|---|---|---|---|
| [Cao et al. (2022)](/sources/cao-2022.md) | finite-volume [high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md), no model | $128^3$, $256^3$, $512^3$, $1024^3$ cells | 13-point dispersion-relation-preserving finite differences at $512^3$ (DeBonis) |
| [Prakash et al. (2022)](/sources/prakash-2022.md) | stabilized trilinear finite elements, explicit SGS models | $64^3$, $128^3$ elements | DNS and filtered DNS of Shoraka; spectra of Brachet et al. |
| [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) | DGSEM, $N=8$, kinetic-energy-preserving split form, low-dissipation Roe flux, SVV-filtered Smagorinsky viscosity | $8^3$ elements ($72^3$ nodes, *compiler check, not in the sources*) | viscous $Re=1600$ result of van Rees et al. at $768^3$ |

**Numerical dissipation of a no-model DNS scheme.**
[Cao et al. (2022)](/sources/cao-2022.md), §3.1, Figs. 2–5, measure the
kinetic-energy decay rate $-dK/dt$ against the dissipation computed from the
resolved field, split into the deviatoric-strain, bulk-viscosity and
pressure–dilatation parts; the remainder is their numerical dissipation. The
kinetic energy agrees with the reference except on $128^3$; the peak
dissipation differs markedly on $128^3$ and $256^3$ and agrees with
refinement. The bulk and pressure–dilatation parts are negligible at Mach
0.1, and the numerical dissipation decreases with refinement. The authors
read the agreement of $-dK/dt$ as evidence that the coarse-mesh numerical
dissipation "correctly mimics" the unresolved dissipation and so supports
[implicit LES](/definitions/implicit-les.md) with high-order methods (see
[numerical dissipation](/properties/numerical-dissipation.md)). Their run
costs (Table 3) grow from 213 core hours at $128^3$ to 747,062 at $1024^3$,
about 1.4 times the core hours of the finite-difference reference at equal
grids, 1.2 after correcting for processor speed (§3.2); the comparison is
across machines and time steps. They call the $1024^3$ run "the finest
resolution" for the problem (§3.1).

**Explicit subgrid models during transition.**
[Prakash et al. (2022)](/sources/prakash-2022.md), §III.B.2, Figs. 5–7:
every model matches the filtered-DNS resolved kinetic energy on $128^3$, and
every model except the dynamic mixed model on $64^3$, which decays too fast.
In resolved dissipation, dynamic Smagorinsky under-predicts, the dynamic
mixed model under-predicts more (significantly even on $128^3$), the
unclipped [gradient model](/methods/gradient-model.md) over-predicts
(especially on $64^3$), and the gradient model with standard or optimal
clipping is the most accurate. At $t=9$ dynamic Smagorinsky and the dynamic
mixed model under-predict the high-wavenumber energy; the gradient-model
variants are closest to filtered DNS, optimal clipping slightly better than
standard clipping on $64^3$. The authors conclude that clipping may be more
accurate than the dynamic mixed model in laminar–turbulent transition
(§IV).

**Inviscid TGV and the shape of a spectral vanishing viscosity.**
[Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md), §6.1, Fig. 4, add
a [Smagorinsky](/methods/smagorinsky-model.md) viscosity ($C_s=0.2$, filter
width the cube root of the element volume over $(N+1)^3$) filtered modally
by the kernel $(i/N)^{P}$ of an entropy-stable
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md),
with $P$ the page-local kernel exponent. This is an explicit modal SVV
acting on an added viscous flux, a different construction from the
implicit SVV of Vicente Cruz & Lamballais above. Unfiltered ($P=0$) the model is
excessively dissipative; $P\approx0.1$ is best, with a spectrum close to
$k^{-5/3}$ over most resolved wavenumbers at $t=20$. The filtered viscosity
acts mainly at low and medium wavenumbers and prevents high-wavenumber
pile-up. For the first five time units the scheme dissipates less than the
viscous reference, then reaches a comparable level. Two sources thus agree
that a plain Smagorinsky viscosity over-dissipates the TGV (this source and
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) above),
and [Prakash et al. (2022)](/sources/prakash-2022.md) find the converse
failure, a pile-up at the cutoff, for a model with too little dissipation,
the unclipped gradient model, in forced
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md).

**Recalled uses.** As recalled by [Basile et al. (2023)](/sources/basile-2023.md),
§3.2 and §4.2.1, Chapelier et al. fixed a modal-decay smoothness threshold
close to the $-5/3$ slope a priori from TGV DNS at $Re=5000$, and the
authors' earlier TGV tests showed high-order DG more accurate than low
order at equal degrees of freedom. As recalled by
[Pereira et al. (2021)](/sources/pereira-2021.md), the companion study of
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
on the transitional TGV found that the coherent structures driving
transition must be resolved, which fixes the minimum physical resolution.

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

## Qualifications

- The sources measure two kinds of dissipation: the decay rate $-dK/dt$ of
  the volume-averaged kinetic energy, which includes model and numerical
  dissipation ([Cao et al. (2022)](/sources/cao-2022.md);
  [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md); the
  dissipation-rate curves of [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md)),
  and the viscous dissipation of the resolved field computed from its
  gradients or enstrophy ([Cao et al. (2022)](/sources/cao-2022.md);
  [Prakash et al. (2022)](/sources/prakash-2022.md), Eq. 27). Only the
  first includes what a model or a scheme removes, so the two are not
  interchangeable when comparing runs.
- [Cao et al. (2022)](/sources/cao-2022.md), §3.1, state both that the peak
  of $-dK/dt$ shows "a large discrepancy" on $128^3$ and $256^3$ and that it
  is "well predicted at all grid levels"; their implicit-LES conclusion
  rests on the second statement. Read in the arXiv v1 preprint.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) compare an
  inviscid run with a viscous $Re=1600$ reference, so the dissipation
  agreement is qualitative; they print the time as "seconds" and the
  Smagorinsky viscosity (Eq. 125) without a density factor, although it is
  used as a dynamic viscosity. Read in arXiv v3.
- [Prakash et al. (2022)](/sources/prakash-2022.md) run no no-model case
  on the TGV and stop the analysis at the end of transition, so their
  ranking does not cover the decay phase.

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §3; §5.3; §6.1–6.5, Eqs. (43)–(46), Figs. 4–22.
- [Agdestein & Sanderse (2025)](/sources/agdestein-2025.md) — App. F, Eqs. (F.1), (F.5), (F.9), (F.12), (F.29)–(F.30).
- [Cao et al. (2022)](/sources/cao-2022.md) — §3.1–3.2, Tables 1–4, Figs. 2–6.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §III.B.2, Eqs. (25)–(27), Figs. 5–7; §IV.
- [Mateo-Gabín et al. (2022)](/sources/mateogabin-2022.md) — §6.1, Eqs. (123)–(125), Fig. 4.
- [Basile et al. (2023)](/sources/basile-2023.md) — §3.2, §4.2.1 (recalled TGV studies).
- [Pereira et al. (2021)](/sources/pereira-2021.md) — §IV.3.4 (recalled companion TGV study).
