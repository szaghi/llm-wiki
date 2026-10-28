---
type: Method
title: "Multi-resolution independent simulations"
description: "MRIS obtains dissipation-range DNS statistics at resolutions too costly for long runs: a long coarse run is refined in time, then in space, for a few Kolmogorov times from several independent snapshots, and ensemble averaged; Yeung et al. (2025) extend it to raise the Reynolds number by viscosity reduction."
status: established
aliases: [MRIS, multi-resolution independent simulation protocol]
tags: [dns, gpu, intermittency, grid-requirements]
timestamp: 2026-10-28T16:59:00Z
---

# Multi-resolution independent simulations

**Multi-resolution independent simulations (MRIS)** is a protocol for
[direct numerical simulation](/definitions/direct-numerical-simulation.md) of
statistically stationary turbulence whose small-scale statistics are needed at
a resolution too expensive to run for many large-eddy times. A long run at a
resolution adequate for scales larger than the Kolmogorov length $\eta$
provides independent snapshots; from each, the simulation is continued for
only a few Kolmogorov times $\tau_\eta$ at finer temporal and then spatial
resolution, and the small-scale statistics of these short segments are
ensemble averaged. The protocol was introduced by Yeung & Ravikumar (2020, which
[Yeung et al. 2025](/sources/yeung-2025.md), §2.2, cite) and extended by
Yeung et al. (2025) to raise the Reynolds number; with it they obtain forced
[isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md) at
$Re_\lambda\approx2500$ (the source's $R_\lambda$) on a $32\,768^3$ grid.

Page-local symbols: $C=[|u|+|v|+|w|]_{\max}\Delta t/\Delta x$ the Courant
number; $k_{\max}$ the largest resolved wavenumber of the pseudo-spectral
grid; $N_1$, $N_2$ the points per direction before and after refinement
(registry $N_x$); $T_1$, $T_2$, $T_3$ the durations of the three phases;
$M_{\mathrm{seg}}$ the number of independent segments (the source's $M$,
renamed because $M$ is the Mach number); $T_E$ the large-eddy turnover time;
$u_{\mathrm{rms}}$ the r.m.s. velocity component (the source's $u'$).

## Premise

Newly added high-wavenumber modes receive energy by spectral transfer within
a short time, and small-scale statistics have short time scales: after a
halving of the time step or the grid spacing, scales of the order of the
coarser grid's $\eta$ equilibrate in approximately $2\tau_\eta$ (Yeung et al.
2025, §2.2, citing Yeung et al. 2018 and Yeung & Ravikumar 2020). A long run
is therefore needed only for the large scales, and the expensive resolution
only for a few $\tau_\eta$.

## The three phases

Yeung et al. (2025, §2.2; Table 1 caption) define, with the resolution pair
$\{k_{\max}\eta,\,C\}$:

1. **Phase 1**: a reasonably long run at temporal and spatial resolution
   adequate for scales larger than $\eta$, $\{k_{\max}\eta,C\}\approx\{1.4,0.6\}$;
2. **Phase 2**: continuation with halved time step for a few $\tau_\eta$,
   $\{1.4,0.3\}$;
3. **Phase 3**: halved grid spacing for a small number of $\tau_\eta$,
   $\{2.8,0.3\}$.

The sequence is repeated from different phase-1 snapshots and the results are
ensemble averaged over $M_{\mathrm{seg}}$ segments; the early portion of phase 3 is excluded
from the time averages. Refinement may be done in increments, e.g.
$N_1\to3N_1/2\to2N_1$. The resolution parameter of their Fourier
pseudo-spectral code is $k_{\max}\eta=(\sqrt2N_x/3)\,\eta\approx2.96/(\Delta x/\eta)$
(§2.2); with $\Delta x=2\pi/N_x$ the factor is $2\sqrt2\pi/3=2.96$
*(compiler check, not in the sources)*. The authors note "conceptual
similarities" with scale enrichment in LES (citing Ghate & Lele 2020).

## Extension: raising the Reynolds number

Yeung et al. (2025, §2.2) reach higher $Re_\lambda$ by reducing the viscosity
at fixed forcing and fixed $k_{\max}\eta$ while refining the grid from
$N_1^3$ to $N_2^3$. With $\eta=(\nu^3/\langle\varepsilon\rangle)^{1/4}\propto1/N_x$
and $\langle\varepsilon\rangle$ independent of $\nu$,
$$\nu\propto N_x^{-4/3},\qquad \langle\varepsilon\rangle=15\nu\Big(\frac{u_{\mathrm{rms}}}{\lambda}\Big)^2\ \Rightarrow\ Re_\lambda\propto N_x^{2/3},\qquad Re_{\lambda,2}\approx Re_{\lambda,1}\Big(\frac{N_2}{N_1}\Big)^{2/3},$$
a 58% increase for $N_2=2N_1$ ($\lambda$ the Taylor microscale). In this extended protocol "phase 1"
includes the transition after the viscosity drop. In the step from
$Re_\lambda=2080$ ($12\,288^3$) to 2500 ($16\,384^3$) the kinetic energy varies
little, the mean dissipation recovers within about $20\tau_\eta$ and the
dissipation skewness sooner (Fig. 1a). At the start of a refinement
$Re_\lambda$ jumps to $Re_{\lambda,1}/0.6814$, then decreases to about
$0.84Re_\lambda(0)=1.23Re_{\lambda,1}$, which they set against the expected 21.1%
increase for $N_2/N_1=4/3$ (p. R2-6). The numbers are consistent:
$(3/4)^{4/3}=0.6814$ is the viscosity ratio for $N_2/N_1=4/3$ (with
$\lambda$ momentarily unchanged, $Re_\lambda\propto1/\nu$), $0.84/0.6814=1.233$
and $(4/3)^{2/3}=1.211$ *(compiler check, not in the sources)*. The
dissipation spectrum settles quickly onto a new stationary form (Fig. 1b);
for $N_2/N_1=2$ the transition is longer.

## Application: isotropic turbulence up to $Re_\lambda\approx2500$

Run parameters (Yeung et al. 2025, Table 1; $(2\pi)^3$ box, forcing of
Donzis & Yeung keeping the energy of the first three wavenumber shells
constant, single precision):

| $Re_\lambda$ | finest grid | $\nu$ | $M_{\mathrm{seg}}$ | $T_1/\tau_\eta$ | $T_2/\tau_\eta$ | $T_3/\tau_\eta$ |
|---|---|---|---|---|---|---|
| 390 | $2048^3$ | $4.370\times10^{-4}$ | 4 | $>60$ | 5.00 | 3.74 |
| 650 | $4096^3$ | $1.732\times10^{-4}$ | 3 | – | – | 4.06 |
| 1000 | $8192^3$ | $6.883\times10^{-5}$ | 3 | 83 | 2.63 | 2.56 |
| 1600 | $16\,384^3$ | $2.7319\times10^{-5}$ | 3 | 107 | 3.01 | 1.84 |
| 2500 | $32\,768^3$ | $1.10555\times10^{-5}$ | 3 | 43 | 1.93 | 1.93 |

Phases 1–2 were not needed at $Re_\lambda=650$, which started from an earlier
stationary state at $C=0.15$. MRIS results are used at every Reynolds number
except the lowest (§2.2). The physics obtained (dissipative anomaly,
intermittency of dissipation and enstrophy, spectral
[bottleneck](/definitions/bottleneck-effect.md)) is on
[homogeneous isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md);
the cost and code on [DNS](/definitions/direct-numerical-simulation.md).

**Why the protocol is needed.** The best timing of the $32\,768^3$ grid is
13 s per step on 44% of Frontier; at $Re_\lambda\approx2500$ one $\tau_\eta$
takes about 1000 steps and $T_E/\tau_\eta\approx300$, so a run over
$10T_E$ would take "two years or more of virtually non-stop computing"
(Yeung et al. 2025, §1). [Yeung et al. (2025b)](/sources/yeung-2025-b.md)
describe a GPU Fourier pseudo-spectral DNS code for Frontier and state that
its pencil version has been used for production runs on intermittency at
$Re_\lambda$ close to 2500 at up to $32\,768^3$, to be reported
separately (§6); the paper does not describe MRIS. Its slab version takes
13.07 s per step at $32\,768^3$ on 4096 nodes (April 2023; 12.07 s in
April 2024), of which 8.621 s are MPI communication (§4.2, Table 2), and
$32\,768^3$ needs at least 4096 nodes because of the memory per GPU
(§3.2, Eq. 9).

**Sensitivity check.** According to the authors, a single segment at
$Re_\lambda=1000$ on $8192^3$ spanning $27\tau_\eta$ shows no dependence of
the results on the values of $T_3/\tau_\eta$ in the table, "presumably because the energy of the large
scales is kept frozen by the forcing scheme" (§2.2; the test is not plotted).

## Scope

The authors restrict the protocol to statistics of the dissipation range: it
"may not be directly applicable" to phenomena evolving on inertial-range or
energy-containing time scales, such as non-stationary turbulence or highly
variable forcing (Yeung et al. 2025, §5). Extensions to passive-scalar small
scales and short-time Lagrangian statistics are planned.

## Qualifications

- The equilibration premise rests on earlier studies and on one unplotted
  $27\tau_\eta$ test; at the highest $Re_\lambda$ the phase-3 segments last
  $1.84$–$1.93\tau_\eta$, close to the stated equilibration time of about
  $2\tau_\eta$ (Table 1).
- With the printed figures, $10T_E=3000\tau_\eta\approx3\times10^6$ steps at
  13 s each is about $3.9\times10^7$ s, i.e. 1.2 years, against the "two years
  or more" of the text; the 13 s is the best timing on 44% of the machine,
  and the paper does not say what else the estimate includes *(compiler
  check, not in the sources)*.
- All runs are single precision; the authors judge machine-precision effects
  unlikely to change the conclusions over segments of about $2\tau_\eta$ but
  concede that "rigorous testing is not readily available" (§2.2).
- The paper writes $R_\lambda(0)$ and $R_{\lambda0}$ (here $Re_\lambda(0)$) for the same quantity
  (p. R2-6).
- Successive viscosity ratios in the table are 2.523, 2.516, 2.520 and 2.471,
  against $2^{4/3}=2.520$ for a doubling of $N_x$; the last step passes
  through the intermediate $12\,288^3$ grid *(compiler check, not in the
  sources)*. The paper does not claim the viscosities follow the scaling
  exactly.

# Citations

- [Yeung et al. (2025b)](/sources/yeung-2025-b.md) — §3.2, Eq. 9 (memory, at least 4096 nodes); §4.2, Table 2 (time per step at $32\,768^3$); §6 (production runs at $Re_\lambda\approx2500$ announced). The code paper; MRIS not described.
- [Yeung et al. (2025)](/sources/yeung-2025.md) — §1 (cost of a long $32\,768^3$ run); §2.2, Table 1, Fig. 1 (MRIS phases, resolution pairs, viscosity-reduction extension, transitions, sensitivity check, precision); §5 (scope).
