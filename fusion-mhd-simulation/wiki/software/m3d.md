---
type: Software
title: "M3D"
description: "M3D is a nonlinear 3D MHD code, distinct from its finite-element successor M3D-C1, with an axisymmetric thin resistive wall; in this bundle it supplies the nonlinear resistive-wall tearing-mode simulations of locked-mode thermal quenches and appears in surveys of 3D VDE and stellarator codes."
status: established
aliases: [M3D code, Multilevel 3D]
tags: [mhd, wall, disruption, tearing]
timestamp: 2026-10-16T18:35:00Z
---

# M3D

M3D is a nonlinear three-dimensional MHD code (Park et al. 1999, reference
17 of [Strauss et al. (2022)](/sources/strauss-2022.md), not ingested) with a
thin resistive wall (Pletzer & Strauss 2011, reference 18 of the same
source). It is a different code from [M3D-C1](/software/m3d-c1.md), which
uses $C^1$ finite elements and places its conductors inside the
computational domain; the two are used side by side in the same study, M3D-C1
for linear and M3D for nonlinear runs
([Strauss et al. (2022)](/sources/strauss-2022.md), §II–III). None of the
sources of this bundle prints the M3D equations or its discretization.

## Wall model

[Isernia et al. (2023)](/sources/isernia-2023.md) (§I) group M3D with
[NIMROD](/software/nimrod.md) as codes coupled "only to axisymmetric thin
walls", in contrast with M3D-C1 (conductors inside the domain) and
JOREK–STARWALL/CARIDDI (3D conductors); see
[resistive-wall coupling](/methods/resistive-wall-coupling.md). Strauss et
al. (2022, §III) describe the wall of their M3D runs only as a thin
resistive wall, characterized by $S_{\mathrm{wall}}=\tau_w/\tau_A$, which is
consistent.

## Applications in the sources

- **Resistive-wall tearing mode and the locked-mode thermal quench.** The
  nonlinear runs of the DIII-D locked-mode study use Lundquist number
  $S=10^6$, parallel and perpendicular heat diffusivities
  $\kappa_\parallel=10R_0^2/\tau_A$ and $\kappa_\perp=10^{-4}a^2/\tau_A$, a
  kinematic viscosity $\nu=10^{-4}a^2/\tau_A$ (the source writes these as
  conductivities and a viscosity $\mu$, in diffusivity units), 16 poloidal
  planes, "adequate to resolve low toroidal mode numbers", small random
  initial perturbations in all $n$, and $S_{\mathrm{wall}}$ from $10^3$ to
  $3.3\times10^4$ ([Strauss et al. (2022)](/sources/strauss-2022.md),
  §III). They show a (2,1) [resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md)
  growing to a complete [thermal quench](/definitions/thermal-quench.md)
  with $\tau_{\mathrm{TQ}}\approx3.4/\gamma\approx\tau_w/2$ at the
  experimental wall time (§III, Fig. 4). Time step, solver and cost are not
  given.
- **3D VDEs.** Strauss's earlier M3D VDE work is listed by
  [Artola et al. (2021)](/sources/artola-2021.md) (§1) among the 3D VDE
  studies of different codes that had not been cross-benchmarked before the
  [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md); M3D did not
  take part in that benchmark.
- **Stellarators.** [Nikulsin et al. (2022)](/sources/nikulsin-2022.md)
  (§I) list M3D, with M3D-C1 and MIPS, among the nonlinear codes extended to
  stellarators and describe them as using full MHD on flux-surface-aligned
  grids (except MIPS, cylindrical; the sentence is self-contradictory as
  printed).
- The JOREK review mentions M3D only by name
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md)).

## Limits of the record

The bundle holds no M3D benchmark and no description of its numerics. Its
wall-force, halo-current and 3D-wall capabilities are known only through
the one-line characterization of Isernia et al.; the thermal-quench
predictions it supports for ITER (75–125 ms) rest on extrapolating the
$\tau_{\mathrm{TQ}}\propto\tau_w$ scaling, not on ITER runs (Strauss et al.
2022, §V).

## Citations

- [Strauss et al. (2022)](/sources/strauss-2022.md), §II–V.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §I.
- [Artola et al. (2021)](/sources/artola-2021.md), §1.
- [Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §I.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), code survey.
