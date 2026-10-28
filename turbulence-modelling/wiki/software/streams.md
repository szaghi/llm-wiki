---
type: Software
title: "STREAmS"
description: "STREAmS is an open-source multi-GPU finite-difference solver for compressible wall-bounded flows on Cartesian grids, combining energy-preserving central schemes with WENO shock capturing; this page records its numerics as configured in each study and its use for boundary-layer DNS with wall cooling and shock impingement, implicit LES of a capsule wake, and thermally perfect channel DNS."
status: established
aliases: [STREAmS-2.0, STREAmS 2.1, STREAMS]
tags: [software, gpu, dns, compressible, implicit-les, immersed-boundary, boundary-layer]
timestamp: 2026-10-28T01:57:00Z
---

# STREAmS

**STREAmS** is an open-source, GPU-accelerated finite-difference solver of
the compressible Navier–Stokes equations on Cartesian grids for canonical
wall-bounded flows, by Bernardini and co-workers (Bernardini et al. 2021,
and STREAmS-2.0, Bernardini et al. 2023, both cited by
[Placco et al. 2023](/sources/placco-2023.md), §2). It runs on multiple GPUs
through CUDA Fortran ([Cogo et al. 2022](/sources/cogo-2022.md), §2). The
first two studies of this bundle that use it ran on the Marconi100 system of
CINECA; [Aiello et al. (2026)](/sources/aiello-2026.md), §3.3, use the
open-source GPU release STREAmS 2.1 (Salvadore et al. 2025, which they cite),
with CINECA resources (machine not named).

## Numerics

- **Convective terms.** Cogo et al. (2022, §2) describe "consolidated,
  high-order, energy-preserving schemes" in shock-free regions, "free of
  numerical dissipation", and WENO shock capturing applied locally where the
  Ducros sensor flags shocks (see [kinetic-energy preservation](/properties/kinetic-energy-preservation.md)
  and [WENO and hybrid schemes](/methods/weno-scheme.md)). Placco et al.
  (2023, §2) describe fifth-order WENO for the convective terms, "to account
  for flow discontinuities", and do not mention the central part.
- **Viscous terms.** A locally conservative formulation "expanded to
  Laplacian for ensuring finite molecular dissipation at all resolved
  wavelengths" (Cogo et al. 2022, §2); sixth-order central differences
  (Placco et al. 2023, §2).
- **Time.** Third-order explicit Runge–Kutta of Wray (Placco et al. 2023,
  §2).
- **Immersed boundaries.** Placco et al. (2023, §2) represent a capsule with
  a ghost-point-forcing [immersed boundary method](/methods/immersed-boundary-method.md)
  that imposes no-slip and no-penetration through ghost nodes filled from the
  fluid.

Neither Cogo et al. nor Placco et al. gives orders of accuracy for the
central schemes or performance figures of the code.

**Configurations in two shock and wall-cooling studies.** Two DNS papers
that cite the original STREAmS release (Bernardini et al. 2021)
print different orders for the same hybrid design:

- [Yu et al. (2022)](/sources/yu-2022-e.md), §2: sixth-order
  kinetic-energy-preserving central convection (citing Pirozzoli
  2010), switched to fifth-order WENO near strong compression by the
  Ducros sensor; sixth-order central viscous terms in Laplacian form;
  Wray's three-stage third-order Runge–Kutta.
- [Zhang et al. (2022)](/sources/zhang-2022-b.md), §2: an eighth-order
  energy-preserving scheme in smooth regions and, in discontinuous ones,
  Lax–Friedrichs flux-vector splitting with seventh-order WENO
  reconstruction of the characteristic fluxes, switched by a modified
  Ducros sensor with threshold 0.15 and used only at $M_\infty=8$ ("the
  energy-preserving flux is applied throughout" at $M_\infty=0.5$ and 2);
  viscous terms in Laplacian form "to avoid odd–even decoupling", sixth
  order; the three-stage third-order Runge–Kutta of Spalart, Moser &
  Rogers; recycling–rescaling inflow, which they call "less noisy" than
  digital filtering, non-reflecting characteristic outflow and top
  boundaries, and sponge zones over the last 100 streamwise and 30
  wall-normal points.

Together with Cogo et al., Placco et al. and Aiello et al. below, the
sources print central orders six and eight and WENO orders five and seven,
each study stating its own configuration.

**STREAmS 2.1 as configured by Aiello et al. (2026, §3.3).** Sixth-order
central differences for both convective and diffusive terms, Wray's
low-storage third-order Runge–Kutta with an adaptive step at CFL 0.6, and
fifth-order WENO only during the initial transition (until a dimensionless
time of about 25), after which shock capturing is switched off and the run
is fully central. The built-in convective option is the KEEP scheme of Kuya
et al., which they cite, a kinetic-energy-preserving split form; the authors
add to the code the entropy-conservative fluxes of their EC-TP scheme, of
Gouasmi et al., of Ranocha and an asymptotic variant (see
[entropy conservation](/properties/entropy-conservation.md) and
[kinetic-energy preservation](/properties/kinetic-energy-preservation.md)).
They remove the ghost nodes at the walls, using second-order boundary
formulae on a stretched grid whose first nodes sit off the wall, because
negative temperatures occasionally appeared at ghost nodes during
hypersonic transients (an SCM3 test, not shown, found the boundary order
reduction negligible), and they discretize the viscous terms in
conservative divergence form, which they found more robust in these tests
than the non-conservative form "often employed to avoid odd-even
decoupling effects (Bernardini et al. 2021)". No performance figures are
given.

## Applications in the sources

- **DNS of zero-pressure-gradient boundary layers** (Cogo et al. 2022, §2,
  Table 1): four spatially developing [boundary layers](/benchmarks/turbulent-boundary-layer.md)
  over a cold isothermal wall ($T_w/T_r=0.76$), $M_\infty=2$ and 5.86, at
  $Re_\tau\approx450$ and $\approx2000$; recycling–rescaling inflow with the
  recycling station at $80\delta_{\mathrm{in}}$; wall-normal "natural"
  stretching of Pirozzoli & Orlandi (constant resolution in units of the
  local Kolmogorov length in the outer layer); grids up to
  $16384\times832\times2048$ points with $\Delta x^+\le7.9$, $\Delta z^+\le4.8$;
  runs of $200\,\delta_{\mathrm{in}}/u_\infty$. The database tests
  [Morkovin's hypothesis](/definitions/morkovin-hypothesis.md) and the
  [compressible velocity transformations](/definitions/compressible-velocity-transformation.md);
  resolution details are on [direct numerical simulation](/definitions/direct-numerical-simulation.md).
- **Implicit LES of a Mars entry capsule** (Placco et al. 2023, §2–§3):
  ExoMars-shaped capsule at $M_\infty=2$, $Re=10^6$ on the diameter
  $D=3.8$ m, CO$_2$ ideal gas ($\gamma=1.3$, $Pr=0.72$), angles of attack
  $0^\circ$ to $15^\circ$; $2048\times672\times672$ nodes on a
  $20D\times10D\times10D$ box, 32 GPUs; no subgrid model, the numerical
  dissipation of the discretization acting "as artificial viscosity at small
  scales" ([implicit LES](/definitions/implicit-les.md)). The drag
  coefficient falls from 1.5685 at $0^\circ$ to 1.5349 at $15^\circ$ and the lift spectrum peaks at
  $St=fD/U_\infty\approx0.2$–$0.3$ (Table 3, Fig. 11). The resolution in wall
  units is not reported and no reference data are compared.
- **DNS of a thermally perfect gas in a channel** (Aiello et al. 2026,
  §2–§4, Tables 2–3): compressible [channel flow](/benchmarks/turbulent-channel-flow.md)
  of CO$_2$ as a non-reacting thermally perfect gas (temperature-dependent
  specific heats from the NASA Glenn polynomials, Sutherland viscosity,
  $Pr=0.72$), isothermal walls at 298.15 K, box $10\delta\times2\delta\times3\delta$,
  constant mass flow; bulk Mach numbers on the wall sound speed 3, 4 and 5
  at $Re_\tau\approx470$, 630 and 800, on $512\times256\times324$ to
  $816\times356\times512$ points ($\Delta x^+\le9.68$, $\Delta y^+_w\le0.32$,
  $\Delta z^+\le4.62$); the centreline reaches about 1000 K at Mach 5. The
  study isolates the convective discretization: the non-entropy-conservative
  KEEP scheme over-predicts the pressure and density fluctuations, which
  drift after long times while both entropy-conservative schemes stay
  statistically stationary over a run extended by 50%; at Mach 5 KEEP's
  peak streamwise Reynolds stress differs from EC-TP by 10.98% and Gouasmi
  et al.'s (entropy-conservative, different pressure term) by 5.25%, and the
  wall-pressure r.m.s. is $2.57$ (EC-TP), $3.55$ (KEEP), $2.55$ (Gouasmi)
  and $2.78$ (Ranocha) in wall units. Differences are measured relative to
  EC-TP, with no external reference DNS. The authors state that with
  entropy-conservative fluxes no shock capturing was needed in this fully
  central set-up, and that KEEP or Ranocha's scheme would in practice be
  hybridized with WENO, at the price of dissipation (§4.2). Details are on
  [entropy conservation](/properties/entropy-conservation.md).

- **DNS of an impinging shock on a supersonic boundary layer** (Yu et al.
  2022, §2): $M_\infty=2.28$, inflow Reynolds number $12\,000$ on the inflow
  boundary-layer thickness $\delta_{\mathrm{in}}$, an $8^\circ$ wedge giving
  a shock at $33.2^\circ$ that impinges at $30\delta_{\mathrm{in}}$; box
  $60\times12\times6.5\,\delta_{\mathrm{in}}$ on $2000\times320\times240$
  points ($\Delta x^+\approx5.4$, $\Delta z^+\approx4.9$, $\Delta y^+_w\approx0.7$,
  $\Delta y^+\approx7.0$ in the outer uniform region); $Re_\tau=201$ at the
  reference station; statistics from 900 fields over
  $600\,\delta_{\mathrm{in}}/U_\infty$. The separation is incipient (scaled
  separation length about 1.87). Validation against the DNS of Pirozzoli &
  Bernardini; the scale-by-scale energy analysis is on
  [shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  (§2, Figs. 2–3).
- **Recovery downstream of the impinging-shock interaction**
  ([Yu et al. 2023](/sources/yu-2023.md), §2): a second analysis of the
  same STREAmS database, which the authors state "has been validated in
  our previous study (Yu et al. 2022)", with the same numerics, domain and
  grid. They add the boundary conditions: a Musker mean-velocity profile
  with digital-filter synthetic fluctuations at the inflow and
  temperature from a generalized Reynolds analogy, non-reflecting top and
  outflow boundaries with the Rankine–Hugoniot jump imposed at the top, and
  an isothermal wall at the recovery temperature, $T_w=1.92T_\infty$, "to
  mimic an adiabatic wall". Statistics are spanwise averages over 900
  fields in $t=351$–$959\,\delta_{\mathrm{in}}/U_\infty$, plus streamwise
  averaging over 11 grid points. The database serves a decomposition of
  the downstream boundary layer into a canonical part and a part induced by
  the hidden mixing layer of the separation bubble, and a decomposition of
  the skin friction (see
  [skin-friction decomposition](/definitions/skin-friction-decomposition.md)
  and [shock/turbulent boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- **DNS of cooled-wall boundary layers** (Zhang et al. 2022, §2, Tables
  1–3): six spatially developing zero-pressure-gradient
  [boundary layers](/benchmarks/turbulent-boundary-layer.md) at
  $M_\infty=0.5$, 2 and 8, each quasi-adiabatic ($T_w/T_r=1$) and cooled
  ($T_w/T_r=0.25$ at $M_\infty=0.5$, 0.5 otherwise), compared at
  $Re_\tau\approx650$; $2400\times320\times600$ points ($M_\infty\le2$) or
  $3600\times320\times400$ ($M_\infty=8$), $\Delta x^+=6.2$–12.9,
  $\Delta y^+_w=0.46$–0.77, $\Delta z^+=5.5$–7.7, over 200 stored fields per
  case. The $M_\infty=8$ free stream (51.8 K) is that of the Sandia
  hypersonic tunnel, low enthalpy without real-gas effects. The pressure
  fluctuations are split by Poisson equations into rapid, slow, viscous,
  compressible and harmonic parts (§6; see
  [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).

## Qualifications

- [Kurz et al. (2025)](/sources/kurz-2025.md), §1, describe STREAmS (citing
  both releases) as a solver of "high-order finite difference methods with
  WENO-type shock capturing", contrasting it with DG and flux
  reconstruction codes. The description agrees with Cogo et al. and Placco
  et al. and adds no figures.
- Yu et al. (2022) and Zhang et al. (2022) cite the same release for a
  sixth-order central/fifth-order WENO and an eighth-order
  central/seventh-order WENO configuration, and different third-order
  Runge–Kutta schemes (Wray; Spalart, Moser & Rogers). Zhang et al. state in §6.1 that
  "$\partial p/\partial y=0$" holds for the pressure components at the
  streamwise boundaries, whereas their Table 4 uses the $x$-derivative
  there.
- Cogo et al. and Placco et al. describe the convective discretization differently
  (energy-preserving central plus Ducros-switched WENO; fifth-order WENO
  only). Placco et al. do not state whether the central part was active in the
  capsule runs.

# Citations

- [Cogo et al. (2022)](/sources/cogo-2022.md) — §2, Table 1 (STREAmS numerics, CUDA Fortran, boundary-layer DNS set-up).
- [Placco et al. (2023)](/sources/placco-2023.md) — §2 (STREAmS and STREAmS-2.0, WENO, central viscous terms, Wray Runge–Kutta, ghost-point immersed boundary, implicit LES); §3, Table 1 (grid, 32 GPUs); §4, Table 3, Fig. 11.
- [Kurz et al. (2025)](/sources/kurz-2025.md) — arXiv v2: §1 (STREAmS as a high-order finite-difference WENO code).
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §2, Figs. 2–3 (STREAmS numerics, impinging-shock DNS set-up and validation).
- [Zhang et al. (2022)](/sources/zhang-2022-b.md) — §2, Tables 1–3 (STREAmS numerics, boundary conditions, six boundary-layer DNS); §6.1, Table 4.
- [Aiello et al. (2026)](/sources/aiello-2026.md) — §3.3 (STREAmS 2.1, sixth-order central schemes, Wray Runge–Kutta, WENO transient, KEEP baseline, ghost-node removal, conservative viscous terms); §2, §4, Tables 2–3, Figs. 1–3 (thermally perfect CO$_2$ channel DNS); acknowledgements (CINECA).
- [Yu et al. (2023)](/sources/yu-2023.md) — §2 (reuse of the STREAmS database of Yu et al. 2022, numerics, boundary conditions, statistics).
