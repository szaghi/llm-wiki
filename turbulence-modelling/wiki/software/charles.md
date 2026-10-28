---
type: Software
title: "CharLES"
description: "CharLES is Cascade Technologies' compressible, low-dissipation, second-order finite-volume LES code on Voronoi grids; this page records its scheme, meshing, GPU cost and the wall-modelled LES of aircraft, juncture flows, bumps and compressible channels run with it, including machine-learning wall models trained in it."
status: established
aliases: [charLES, Cascade charLES]
tags: [software, les, wmles, kinetic-energy-preserving, gpu]
timestamp: 2026-10-27T21:07:00Z
---

# CharLES

**CharLES** (printed "charLES" in all five sources) is a massively parallel,
compressible, unstructured finite-volume LES code of Cascade Technologies. It is
the solver of the aircraft [wall-modelled LES](/methods/wall-modelled-les.md) of
[Goc et al. (2021)](/sources/goc-2021.md), of the boundary-layer-conforming
study of [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), of the
Gaussian-bump runs of [Agrawal et al. (2022)](/sources/agrawal-2022.md) and of
the compressible-channel runs of [Griffin et al. (2023)](/sources/griffin-2023.md),
and the solver in which [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
train and test their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md).

## Discretization

- **Fluxes.** Low-dissipation fluxes built on discrete entropy preservation:
  they conserve entropy globally in inviscid shock-free flow and kinetic energy
  in inviscid low-Mach flow (Goc et al. 2021, §2.3, citing Tadmor, Honein &
  Moin, Chandrashekar); "kinetic-energy-conserving … approximately entropy
  preserving in the inviscid limit, thereby limiting the amount of numerical
  dissipation" (Lozano-Durán et al. 2022, §II.B; the same wording in
  Lozano-Durán & Bae 2023, §3.1). Griffin et al. (2023, §4) add
  an artificial bulk viscosity for discontinuities. See
  [kinetic-energy preservation](/properties/kinetic-energy-preservation.md).
- **Accuracy.** Formally second order in space; explicit third-order
  Runge–Kutta in time (Gottlieb–Shu–Tadmor) (Goc et al. 2021, §2.3;
  Lozano-Durán et al. 2022, §II.B; Agrawal et al. 2022, §IV; Lozano-Durán &
  Bae 2023, §3.1).
- **Meshes.** Arbitrary polyhedra; in practice Voronoi diagrams of points
  seeded in hexagonally close-packed arrangements, so that the vector joining
  two adjacent sites is parallel to their shared face normal (Goc et al. 2021,
  §2.3). Lozano-Durán et al. (2022, §III.A) and Lozano-Durán & Bae (2023,
  §3.1) apply ten iterations of Lloyd's algorithm to smooth the transitions
  between refinement levels; Agrawal et al. (2022, §IV) build centroidal Voronoi diagrams with
  homothetic refinement by a factor 2 in near-wall layers ten cells thick.
- **Closures used.** Static-coefficient [Vreman](/methods/vreman-model.md) model
  (free-air aircraft runs) and the compressible
  [dynamic Smagorinsky model](/methods/dynamic-procedure.md) of Moin et al.
  (in-tunnel aircraft, juncture flow with Lilly's modification, compressible
  channels) (Goc et al. 2021, §2.1; Lozano-Durán et al. 2022, §II.B; Griffin et
  al. 2023, §4); the [dynamic tensor-coefficient Smagorinsky model](/methods/dynamic-tensor-coefficient-smagorinsky-model.md)
  in Agrawal et al. (2022). Walls are treated with the
  [equilibrium wall model](/methods/equilibrium-wall-model.md), as an ODE in
  Goc et al. (2021, Eq. 2.6) or in the algebraic form of Lozano-Durán et al.
  (2022, Eq. 1: linear–quadratic below $y^+=23$, log law above, $\kappa=0.41$,
  $B=5.2$, $C^1$ matching), with the wall stress returned as a Neumann
  condition; Griffin et al. (2023) use their
  [inverse-velocity-transformation model](/methods/inverse-velocity-transformation-wall-model.md).
  Lozano-Durán & Bae (2023, §3.2) run the dynamic Smagorinsky model (with
  Lilly's modification) or the Vreman model with either the algebraic
  equilibrium model (Eq. 3.1, same constants, the velocity taken at the
  second off-wall grid point) or their neural-network wall model, which
  reads a two-point wall-normal stencil (§2.4).
- **Matching location.** Lozano-Durán et al. (2022, §II.B) match at the first
  off-wall cell centre with no temporal filtering; Agrawal et al. (2022, §VIII)
  also match at the first point on Voronoi grids and report no
  [log-layer mismatch](/definitions/log-layer-mismatch.md) in their earlier
  tests; Griffin et al. (2023, §4) match at $0.3\delta$ with 12 points per
  channel half-height.

**Solver-consistent training data.** Because the subgrid stress of an
implicitly filtered LES is not the stress obtained by filtering the
Navier–Stokes equations, Lozano-Durán & Bae (2023, §2.5–2.6) generate the
training data of their wall model in charLES itself: wall-modelled LES on
isotropic Voronoi grids $\Delta=\delta/n$, $n=5$ to 380 ($\delta$ the channel
half-height, page-local $n$), driven
by an "exact-for-the-mean" subgrid correction that forces the mean profile
onto DNS and a wall condition that samples the DNS wall-stress p.d.f. They
state that the model "must be re-trained for each flow solver" (§5; see
[discretization-consistent closure](/definitions/discretization-consistent-closure.md)).

## Voronoi mesh generation

Goc et al. (2021, §4, Fig. 15) report the meshing cost as negligible: the
157-million-cell grid of the [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
in about 2 minutes on $10^3$ Ivy Bridge cores; for the High-Lift Common
Research Model, 1.25, 3.29 and 11.4 billion cells on about 3,500, 10,000 and
40,000 cores, and $O(10^{10})$-cell grids in under 30 minutes. Because cells are
locally isotropic, Lozano-Durán et al. (2022, §III.A) prescribe grids by a
single local size $\Delta$, which allows the
[boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md) of
their study.

## Cost and parallel performance

| Case | Cells | Hardware | Cost |
|---|---|---|---|
| JSM, $\alpha=18.58^\circ$, 30 flow passes (Goc et al. 2021, Table 1) | 32 M | 2000 Ivy Bridge cores / 96 V100 GPUs | 1.4k core-h per pass; 21 h / 48 min |
| same | 157 M | same | 12.3k core-h per pass; 7.5 days / 7 h |
| [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) (Lozano-Durán et al. 2022, §V.A) | 6–174 M | Xeon E5-2670, Pleiades | 13k–398k core-h |
| Gaussian bump, spanwise periodic, fine (Agrawal et al. 2022, Table IV) | 52 M | 10 nodes of 6 V100 | 13 (DSM) vs 15 (tensor model) node-h per flow-through |
| Gaussian bump, 3D, fine (Agrawal et al. 2022, Table V) | 452 M | 80 nodes of 6 V100 | 100 vs 112 node-h per flow-through |
| NASA CRM-HL, 7° and 19° (Lozano-Durán & Bae 2023, §4.7) | 30 M | not stated | wall model 1.1–1.3 times the algebraic one (§2.6) |

Goc et al. (2021, §4) state strong scaling with parallel efficiency above 80%
down to about 2,000 cells per CPU core or about $10^6$ cells per GPU; the
medium-grid aircraft LES ($\approx4\times10^4$ core-hours) costs about as much
as a steady RANS run of the High-Lift Prediction Workshop in OpenFOAM
($\approx6\times10^4$), the fine grid six times more. Halving the cell size in
all directions halves the time step (§4). Griffin et al. (2023, §4) report their
wall model between 7% faster and 32% slower than the classical one inside the
code (implementation not optimized, no hardware stated).

## Results obtained with it

- Aircraft at $Re_c=1.96\times10^6$, $M_\infty=0.172$: maximum lift within five
  lift counts of experiment, in-tunnel drag and pitching-moment kick-back
  recovered (Goc et al. 2021; see the [JSM benchmark](/benchmarks/jaxa-standard-model.md)).
- Juncture flow: wall-pressure errors below 5% on every grid, mean-velocity
  errors 3–8% on the fuselage, about 15% in the wing–body juncture and about
  100% in the separated trailing-edge corner; 12-million-cell
  boundary-layer-conforming grids beat a 31-million-cell constant-size grid
  (Lozano-Durán et al. 2022, §V).
- [Channel flow](/benchmarks/turbulent-channel-flow.md) at $Re_\tau=4200$: the
  mean-velocity error scales as $e_u\approx0.08\,\Delta/\delta$ (registry $e_q$), with
  a non-monotonic convergence at $\Delta/\delta\approx0.03$–$0.05$ seen in both
  charLES and a staggered finite-difference code (Lozano-Durán et al. 2022,
  §IV.B, App. B).
- Compressible isothermal channels at bulk Mach 0.7–4 and $Re_\tau$ 320–1800
  (Griffin et al. 2023, §4).
- Building-block-flow wall model (Lozano-Durán & Bae 2023, §4): internal
  wall-model errors much below those of the equilibrium model in laminar,
  zero-pressure-gradient, pressure-gradient and three-dimensional unsteady
  channel and boundary-layer cases, but total errors dominated by the
  subgrid model; moderate improvements of lift, drag and pitching moment on
  the NASA High-Lift Common Research Model ($Re=5.49\times10^6$,
  $M_\infty=0.20$), and better juncture predictions on the
  [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md) with a
  boundary-layer-conforming grid of 5 points per boundary-layer thickness.

## In an industrial review

[Mani & Dorgan (2023)](/sources/mani-2023.md), an MIT–Boeing perspective
on aerospace CFD, do not run the code but cite it at three places:

- **GPUs.** A RANS solution of a full aircraft at low angle of attack is
  typically obtained within eight hours, and GPUs could cut this time by an
  order of magnitude, as FUN3D and "Cascade Technologies's charLES code"
  show (§3, citing the vendor and Goc et al. 2021).
- **Flux.** Among the low-dissipation fluxes for scale-resolving simulation
  they name the kinetic-energy- and entropy-preserving (KEEP) algorithm and
  write that Goc et al. (2021) "used charLES with a KEEP scheme and
  demonstrated accurate prediction of the maximum lift coefficient" of the
  High-Lift Prediction Workshop configuration (§4.4); compare the flux
  description under Discretization above.
- **WMLES of high-lift aircraft.** Their Fig. 6 (§4.1.2, adapted from
  Lehmkuhl et al. 2019; caption credits Lehmkuhl et al. 2019 and Goc et al.
  2021) sets $C_L(\alpha)$ of the Third High-Lift Prediction Workshop
  from RANS submissions against wall-modelled LES with two codes, Alya
  (finite elements, 10 and 65 million degrees of freedom) and CharLES
  (finite volumes, 12 and 35 million); the §4.1.2 text calls the Alya
  prediction of pre- and post-stall lift accurate and says nothing of the
  CharLES curves. Their Fig. 12b (§4.5.2, adapted from Goc et
  al. 2020) shows WMLES of the [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
  on 36 million cells (nacelle off) and 42 million (nacelle on). The authors
  write that the WMLES of Goc et al. (2020, 2021, 2022) "predicted the abrupt
  lift break near the stall", but that "the overprediction of lift at lower
  angles of attack show that further investment and research are needed";
  for routine industrial use they ask for mesh-independent quantities of
  interest within wind-tunnel uncertainty and for automating, or
  eliminating, the choice of the exchange location between LES and wall
  model (§4.5.2). See [wall-modelled LES](/methods/wall-modelled-les.md).

## Qualifications

- Goc et al. (2021, §4) estimate the 157-million-cell case at the scaling limit
  (about 80,000 cores or 160 GPUs) at under 4 hours; ideal linear scaling of
  their own Table 1 gives about 4.7 h (CPU) and 4.3 h (GPU), and their Table 1
  values give 7.7 days rather than the printed 7.5 for the CPU run *(compiler
  check, not in the sources)*.
- The four earlier sources (Goc et al. 2021, Lozano-Durán et al. 2022,
  Agrawal et al. 2022, Griffin et al. 2023) include Moin among the authors,
  three of them Bose (Cascade Technologies, the code's developer); Lozano-Durán & Bae
  (2023) do not, but Lozano-Durán co-authored Lozano-Durán et al. (2022). No
  source outside this author group uses the code so far; Mani & Dorgan
  (2023) only relay results of Goc et al. and Lehmkuhl et al. in a review.
- Mani & Dorgan (2023, §4.5.2) report lift over-prediction at lower angles
  of attack in the JSM WMLES of Goc et al. (2020, Fig. 12b); Goc et al.
  (2021) report maximum lift within five lift counts of experiment (see
  Results above). The two statements are recorded side by side.
- The equilibrium model of Lozano-Durán et al. (2022) reads the first
  off-wall cell centre; the one of Lozano-Durán & Bae (2023, Eq. 3.1) the
  second off-wall point.

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1, Eq. (2.6); §2.3 (scheme, meshes, GPUs); §4, Tables 1–2, Fig. 15 (cost, scaling, meshing).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §III.A (Voronoi grids); §IV.B; §V.A (cost); App. B.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §IV (solvers and meshes); §VIII (wall model); §IX, Tables IV–V (GPU cost).
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4 (WMLES set-up, artificial bulk viscosity, cost).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.4–2.6 (stencil, solver-consistent training, cost); §3.1–3.2, Eq. (3.1) (scheme, Voronoi grids, closures); §4 (results); §5.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §3 (GPU potential); §4.4 (KEEP scheme in charLES); §4.1.2, Fig. 6; §4.5.2, Fig. 12 (WMLES of HiLiftPW-3 and JSM, industrial needs).
