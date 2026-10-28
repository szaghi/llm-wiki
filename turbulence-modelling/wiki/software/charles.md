---
type: Software
title: "CharLES"
description: "CharLES is Cascade Technologies' compressible, low-dissipation, second-order finite-volume LES code on Voronoi grids; this page records its scheme, meshing, GPU cost and the wall-modelled LES of aircraft (including its HLPW-4 high-lift submission), juncture flows, bumps, compressible channels and a wall-modelled LES grid-convergence study, machine-learning wall models trained in it, and the CharlesX variant of a detonation-engine LES."
status: established
aliases: [charLES, Cascade charLES]
tags: [software, les, wmles, kinetic-energy-preserving, gpu]
timestamp: 2026-10-28T07:04:00Z
---

# CharLES

**CharLES** (printed "charLES" by Goc et al. 2021 and most later sources,
"CharLES" by Hu et al. 2024) is a massively parallel,
compressible, unstructured finite-volume LES code of Cascade Technologies. It is
the solver of the aircraft [wall-modelled LES](/methods/wall-modelled-les.md) of
[Goc et al. (2021)](/sources/goc-2021.md), of the boundary-layer-conforming
study of [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), of the
Gaussian-bump runs of [Agrawal et al. (2022)](/sources/agrawal-2022.md) and of
the compressible-channel runs of [Griffin et al. (2023)](/sources/griffin-2023.md),
and the solver in which [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
train and test their
[building-block-flow wall model](/methods/building-block-flow-wall-model.md).
[Hu et al. (2024)](/sources/hu-2024.md) run their grid-convergence study of
wall-modelled LES in it ("Cascade Technologies Inc. and Cadence", §4), and
[Vignat et al. (2024)](/sources/vignat-2024.md) name "CharlesX" as the
unstructured compressible code of their reacting LES of a rotating
detonation engine (see the section on CharlesX below).

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
  Hu et al. (2024, §4, Eq. 5) close the SGS stress and heat flux with the
  Vreman model and use the same algebraic law of the wall (linear–quadratic
  below $y^+=23$, log law with $\kappa=0.41$, $B=5.2$ above), which returns
  only the magnitude of the wall stress, its direction aligned with the LES
  velocity at $h_{\mathrm{wm}}$ (§6.1).
- **Matching location.** Lozano-Durán et al. (2022, §II.B) match at the first
  off-wall cell centre with no temporal filtering; Agrawal et al. (2022, §VIII)
  also match at the first point on Voronoi grids and report no
  [log-layer mismatch](/definitions/log-layer-mismatch.md) in their earlier
  tests; Griffin et al. (2023, §4) match at $0.3\delta$ with 12 points per
  channel half-height. Hu et al. (2024, §5) place $h_{\mathrm{wm}}$ at a
  cell centre of isotropic grids, at $h_{\mathrm{wm}}=0.1\delta$ and
  $0.2\delta$ in the channel and $0.05\delta$ to $0.15\delta$ in a
  three-dimensional boundary layer; the channel grids of Table 1 put it at
  the first to the ninth cell centre, $\Delta/h_{\mathrm{wm}}=2$ down to
  $0.118$ *(compiler check, not in the sources: ratio of the printed
  $\Delta^+$ to $h_{\mathrm{wm}}^+$)*.

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
- Grid convergence of wall-modelled LES (Hu et al. 2024, §6): in a channel
  at $Re_\tau=1000$, Spalart's boundary layer under a rotating free stream
  and a channel at $Re_\tau=934$ with a sudden spanwise pressure gradient,
  the mean wall stress, mean velocity and mean flow direction converge at
  coarser grids for larger $h_{\mathrm{wm}}$, with onset near
  $\Delta/h_{\mathrm{wm}}\approx0.3$–$0.4$; the streamwise rms velocity
  converges more slowly, with errors an order of magnitude larger than the
  mean velocity's, and is not controlled by $h_{\mathrm{wm}}$. Details on
  [wall-modelled LES](/methods/wall-modelled-les.md).

## CharlesX in a rotating detonation engine

Vignat et al. (2024, §3, Table 1) describe the code of their LES of the
AFRL methane–oxygen rotating detonation rocket engine as a fully
compressible unstructured finite-volume solver, citing two papers of the
Stanford group (Khalighi et al.; Ma et al.), and name it "CharlesX" in
their survey table. The configuration they print differs from the
second-order scheme above:

- a "combination of centered and upwind-biased Riemann flux", with a
  high-order polynomial reconstruction that is fourth order on uniform and
  third order on non-uniform meshes outside sensor regions (Table 1
  summary: "3rd order central"), and first-order reconstruction in cells
  flagged by a pressure- and density-gradient sensor (detonations, shocks,
  flames) or a sensor on unphysical mass fractions or temperatures below
  260 K (§3.5);
- an operator splitting with a fourth-order Rosenbrock–Krylov integrator
  for the stiff chemistry (FFCMy-12, 12 species, 38 reactions, no
  turbulence–chemistry closure) and third-order strong-stability-preserving
  Runge–Kutta for advection and diffusion, with a typical convective time
  step of 4.3 ns (§3.4);
- the [Vreman model](/methods/vreman-model.md) with $C=0.07$, "as
  specified in the original paper", and turbulent Prandtl and Schmidt
  numbers of 0.7 ([turbulent Prandtl number](/definitions/turbulent-prandtl-number.md));
  no-slip adiabatic walls without a wall model, boundary layers unresolved
  (§3.3, §3.6);
- 54 million cells, 50–100 μm in the detonation region (§3.1).

The LES gives two co-rotating detonation waves where the experiment shows
three, a wave speed 24% below the measured one (the other groups'
LES of this case under-predict it by up to 30%), and thrust within 3.1% of
the measurement (§3.9, Table 2). The paper does not state how CharlesX
relates to Cascade Technologies' charLES.

## In the HLPW-4 wall-modelled LES summary

[Kiris et al. (2023)](/sources/kiris-2023.md) summarize the wall-modelled
LES and lattice-Boltzmann focus group of the 4th AIAA High-Lift Prediction
Workshop on the [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md)
($Re=5.5\times10^6$ on the mean aerodynamic chord, Mach 0.2), where
charLES is submission W-021 (Stanford and Cascade Technologies). As
tabulated (Tables 1–2): explicit RK3, second-order finite volumes on
self-made Voronoi grids of aspect ratio 1, the dynamic Smagorinsky model
with an equilibrium wall model fed from the first off-wall point
($0.5\Delta$), non-dimensional $\Delta t=5.7\times10^{-5}$, a best-practice
grid of 362M degrees of freedom, wall-normal spacing 6.8 mm up to 25% chord
and 13.6 mm after it at full scale (7 m mean aerodynamic chord); free-air
(case 2a) and in-tunnel (case 2b) runs. Kiris et al. group W-021 with the
kinetic-energy- and entropy-consistent discretizations (§II.2). Findings:

- **Grid refinement.** From 12M to 40M, 146M and 362M degrees of freedom
  the loads converged "largely monotonically", the leading-order effect
  being kinematic: the inviscid, curvature-induced acceleration on the
  outboard wing and slats (§III, Fig. 6). Below 300M the W-021 pressure
  distributions remain sensitive to refinement, unlike those of the
  structured-overset W-020 above 300M (§IV.2, Figs. 14–17).
- **Subgrid model.** W-021 "reported little sensitivity" between the
  dynamic Smagorinsky and Vreman models on intermediate grids (§II.4).
- **Stall topology.** In free air W-021 falls in topology A, inboard stall
  growing from the wing–body juncture, with a pitch break between 20.5°
  and 21.47° (§IV.3).
- **In tunnel.** W-021 predicts the pitch break between 18.9° and 19.9°
  "in perfect agreement with the experiment"; W-020 and W-021 give
  essentially identical wing-root topologies, and the stalled state at
  19.9° is largely invariant to the tunnel-floor boundary layer, which no
  team reproduced (§V, Figs. 27–36).
- **GPUs.** W-021 and W-047 ([hpMusic](/software/hpmusic.md)) showed
  "substantial" reductions of wall-clock hours on GPUs; the authors give no
  figures and call best-practice WMLES 5–10 times as expensive as a
  representative steady RANS (§VI.4).

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
  source before Hu et al. (2024, below) outside this author group runs the code; Mani & Dorgan
  (2023) only relay results of Goc et al. and Lehmkuhl et al. in a review.
- Mani & Dorgan (2023, §4.5.2) report lift over-prediction at lower angles
  of attack in the JSM WMLES of Goc et al. (2020, Fig. 12b); Goc et al.
  (2021) report maximum lift within five lift counts of experiment (see
  Results above). The two statements are recorded side by side.
- The equilibrium model of Lozano-Durán et al. (2022) reads the first
  off-wall cell centre; the one of Lozano-Durán & Bae (2023, Eq. 3.1) the
  second off-wall point.

- Kiris et al. (2023, abstract, §IV) find more than 250M degrees of
  freedom necessary for the outboard suction peaks and the pitching moment
  at high angle of attack, which they call "somewhat contradictory" to the
  coarse-grid success on the JAXA-CRM of Goc et al. (2021) above; they
  attribute the extra need to inviscid acceleration on the outboard wing
  (the W-021 refinement study). None of the authors of Kiris et al. is
  affiliated with Stanford or Cascade Technologies (page 1); they
  summarize the W-021 submission in a workshop report.
- Hu et al. (2024; University of Pennsylvania and Pennsylvania State
  University) run the code outside the Moin–Bose author group of the
  earlier item; Park, their corresponding author, co-authored the
  Park & Moin wall-model papers they cite. Vignat et al. (2024) are of
  Stanford University (page 1).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) compute the Gaussian bump in
  a different, incompressible finite-volume code (You, Ham & Moin) and find
  no separation with the dynamic Smagorinsky model, citing Agrawal et al.
  (2022), whose bump runs above are charLES runs, among the studies in
  which it did separate; they attribute the difference possibly to
  clipping, filtering, mesh topology and numerics (§3.1). See
  [Gaussian bump](/benchmarks/gaussian-bump.md).

# Citations

- [Goc et al. (2021)](/sources/goc-2021.md) — §2.1, Eq. (2.6); §2.3 (scheme, meshes, GPUs); §4, Tables 1–2, Fig. 15 (cost, scaling, meshing).
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §II.B, Eq. (1); §III.A (Voronoi grids); §IV.B; §V.A (cost); App. B.
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §IV (solvers and meshes); §VIII (wall model); §IX, Tables IV–V (GPU cost).
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §4 (WMLES set-up, artificial bulk viscosity, cost).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.4–2.6 (stencil, solver-consistent training, cost); §3.1–3.2, Eq. (3.1) (scheme, Voronoi grids, closures); §4 (results); §5.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §3 (GPU potential); §4.4 (KEEP scheme in charLES); §4.1.2, Fig. 6; §4.5.2, Fig. 12 (WMLES of HiLiftPW-3 and JSM, industrial needs).
- [Kiris et al. (2023)](/sources/kiris-2023.md) — Tables 1–2 (W-021 configuration); §II.2, §II.4; §III, Fig. 6 (refinement); §IV.2–IV.3, Figs. 14–17, 23–25 (pressure sensitivity, topology A); §V, Figs. 27–36 (in-tunnel pitch break); §VI.4 (GPUs, cost).
- [Hu et al. (2024)](/sources/hu-2024.md) — §4, Eq. (5) (solver, Vreman model, algebraic wall model); §5, Tables 1–2 (grids, matching heights); §6 (convergence results).
- [Vignat et al. (2024)](/sources/vignat-2024.md) — §3.1, §3.3–§3.6, Table 1 (CharlesX configuration); §3.9, Table 2 (validation).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.1 (solver), §3.1 (dynamic Smagorinsky separation against Agrawal et al., cited).
