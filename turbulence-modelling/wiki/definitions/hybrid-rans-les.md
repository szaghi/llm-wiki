---
type: Definition
title: "Hybrid RANS/LES"
description: "Scale-resolving approaches that model all turbulence with RANS in some regions or limits and resolve part of it as in LES elsewhere; the distinction from wall-modelled LES, the three operating modes and unified against interfaced transitions, and the deficiencies the sources identify, modelled-stress depletion first."
status: established
aliases: [HRL, hybrid RANS-LES, RANS/LES hybrid, bridging model, hybrid turbulence model, scale-resolving simulation, SRS]
tags: [hybrid-rans-les, rans, les, des, pans]
timestamp: 2026-10-25T13:47:00Z
---

# Hybrid RANS/LES

A hybrid RANS/LES (HRL) method lets a simulation carry all of the turbulent
stress with a RANS model where the RANS model is adequate or the grid is too
coarse, and resolve part of the turbulence, as in
[large-eddy simulation](/definitions/large-eddy-simulation.md), where the
grid allows and RANS fails (separation, reattachment, mean
three-dimensionality). Haering et al. (2022) state the goal as "employing
LES only where RANS is deficient"
([Haering et al. (2022)](/sources/haering-2022.md), §I). Dzanic et al. (2022)
place hybrid ("bridging") models within scale-resolving simulation, which
relaxes the resolution requirements of LES while resolving the dominant
flow physics, with the intent "to resolve only the coherent flow structures
while modeling the stochastic portion of the flow"
([Dzanic et al. (2022)](/sources/dzanic-2022.md), §1).

## Hybrid RANS/LES and wall-modelled LES

Following the taxonomy of Larsson et al., as recalled by Haering et al.
(2022, §I):

- in [wall-modelled LES](/methods/wall-modelled-les.md), LES is active in
  the whole domain, the grid does not resolve the near-wall layer, and a wall
  model supplies the wall stress from the LES velocity;
- in HRL, RANS and LES are active in distinct regions; the near-wall layer
  is generally RANS, so the wall-normal grid must resolve the viscous layer
  and the wall stress is computed directly, but there is no wall-parallel
  resolution requirement there beyond resolving the geometry and the mean
  flow.

An HRL whose RANS model is active only near the wall can therefore be read as
a wall-modelled LES. The authors expect HRL to remain preferable where RANS
represents the boundary layers over most of a body, as in most external
aerodynamics, and wall-modelled LES to be more efficient where RANS fails
almost everywhere outside the viscous layer. Lozano-Durán et al. (2022)
quote the NASA CFD Vision 2030 study as naming hybrid RANS/LES and
wall-modelled LES the most viable approaches for realistic high-Reynolds
external aerodynamics, and note that most simulations of the NASA Juncture
Flow so far used RANS or hybrid RANS solvers
([Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §I; see
[NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)). In the Third
High-Lift Prediction Workshop delayed detached-eddy simulation was among the
few unsteady techniques submitted next to the dominant steady RANS
([Goc et al. (2021)](/sources/goc-2021.md), §1).

## How hybrids operate

Haering et al. (2022, §I) sort HRL methods into three modes:

1. reduce the RANS stress with a specified function so that resolved
   fluctuations can develop (e.g. the flow-simulation methodology);
2. carry distinct RANS and LES models and blend their modelled stresses;
3. carry a single model that switches internally between RANS-like and
   LES-like operation, as detached-eddy simulation (DES), "the most
   ubiquitous HRL approach", does.

The switch between modes is either *unified*, responding to local model or
flow parameters and a grid measure, or *interfaced*, prescribed ab initio.
Unified switches rely on ad hoc functions tuned per flow, such as the
model-reduction factor of the flow-simulation methodology or the delaying
function of delayed DES, so the methods "may not be predictive, in general".
Dzanic et al. (2022, §1) note that most earlier high-order work on such
models concerned RANS or zonal methods such as DES.

[Partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md)
is a single-model unified hybrid: one parameter, the unresolved fraction
$f_k$ of the kinetic energy, moves the same transport equations between RANS
($f_k=1$) and DNS. The [active model split](/methods/active-model-split.md)
method of Haering et al. is a two-model method with no blending function at
all.

### Mean-and-fluctuation splitting

A family of methods builds on the decomposition of Schumann (1975), as
recalled by Haering et al. (2022, §I), in which different eddy-viscosity
models act on the mean and on the fluctuating strain; the authors say it
"may actually be considered the first hybrid method". They recall:

- **two-velocity HRL** (Uribe et al.): RANS viscosity on the mean strain,
  Smagorinsky on the resolved fluctuating strain, with a hyperbolic-tangent
  length-scale blending that can cause "drastic model shifts";
- **RSC-SGS** (Chen et al.): the mean-strain RANS stress (Spalart–Allmaras
  or van Driest) reduced by the averaged resolved stress, dynamic
  Smagorinsky on the fluctuations; in expectation it returns the unaltered
  RANS stress, and its prescribed switch location makes it zonal;
- **dynamic HRL** (Bhushan & Walters): RANS on the mean blended with an
  implicit subgrid model through a ratio of productions, both active
  everywhere;
- **dual-mesh HRL**: separate RANS and LES simulations on two grids coupled
  by forcing terms that enforce consistency in expectation.

## Deficiencies identified by the sources

Haering et al. (2022, §II) name four deficiencies common to most HRL
formulations.

1. **Modelled-stress depletion (MSD).** If resolved turbulence is generated
   passively, by lowering the modelled stress and waiting for instabilities,
   the total stress must first be depleted: such methods "must exhibit
   regions of modeled-stress-depletion", with log-layer mismatch, reduced
   body forces, premature separation and delayed reattachment as
   consequences (see [log-layer mismatch](/definitions/log-layer-mismatch.md)).
   The authors judge explicitly introducing resolved fluctuations, at a rate
   consistent with the reduction of the modelled stress, to be "the only way
   to prevent regions of MSD", and view body forcing formally as a model of
   the commutator between the implicit filter and the substantial
   derivative (§II A). As they recall it, stochastic forcing at the RANS/LES
   interface removed log-layer mismatch in channel flow but is problem
   dependent (Piomelli et al.), and the forced scale-adaptive simulation
   SAS-F still showed log-layer mismatch (Menter et al.).
2. **One scalar eddy viscosity for two jobs.** A hybrid model must carry a
   non-negligible share of the mean stress and the energy transfer to the
   unresolved scales; a scalar eddy viscosity cannot do both (§II B; see
   the [Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)).
3. **Ad hoc blending and scalar grid measures.** The cube root of the cell
   volume tends to the smallest cell size as the aspect ratio grows and so
   overestimates the resolution; cell-diagonal measures are preferable, and
   resolution indicators should account for the anisotropy of both the grid
   and the resolved turbulence (§II C).
4. **RANS transport equations fed with fluctuating quantities.** Nonlinear
   sources calibrated on mean quantities, such as the $\varepsilon$
   destruction $C_{\varepsilon2}\varepsilon^2/k$, acquire spurious correlations
   when evaluated on fluctuating fields; a Taylor expansion shows that the
   mean of the destruction then depends on the amount of resolved
   turbulence. The rule: "what goes in to, and what comes out of,
   RANS-based transport models must be expected values". The problem
   concerns single-model unified methods, DES, PANS and PITM among them,
   and its symptoms are masked by numerical dissipation, coefficient tuning
   or averaging (§II D, Eqs. 1–2).

Dzanic et al. (2022) stress the numerical side: the excessive dissipation of
low-order schemes harms the modelled physics of hybrid simulations more than
RANS, and they find that raising the order of a flux-reconstruction
discretization at fixed degrees of freedom benefits PANS proportionally more
than [implicit LES](/definitions/implicit-les.md) (§1, §4; see
[numerical dissipation](/properties/numerical-dissipation.md)).

## Qualifications

- Haering et al.'s statement that explicit forcing is the only remedy for
  MSD is hedged in the source ("It appears that …", §II A) and rests on the
  cited forcing studies; no proof is given.
- The periodic hill has been simulated successfully at about one million
  cells with second-order delayed DES, PANS and PITM, as recalled by Haering
  et al. (2022, §V B); see [periodic hill](/benchmarks/periodic-hill.md).

# Citations

- [Haering et al. (2022)](/sources/haering-2022.md) — §I, §II A–D Eqs. 1–2, §V B.
- [Dzanic et al. (2022)](/sources/dzanic-2022.md) — §1, §4.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §I.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1.
