---
type: Benchmark
title: "NACA 4412 airfoil"
description: "The cambered NACA 4412 airfoil near maximum lift, chord Reynolds number about 1.6 million at 12°–14° with trailing-edge separation: a test of wall models in WMLES and of RANS, DES and RSM-based hybrids whose lift and drag errors stay large, with a debated experimental basis; at 200,000 a PINN boundary-layer case."
status: established
aliases: [NACA4412, NACA 4412, NACA-4412, Wadcock airfoil]
tags: [benchmark, wmles, wall-model, hybrid-rans-les, separated-flow, boundary-layer]
timestamp: 2026-10-27T11:00:00Z
---

# NACA 4412 airfoil

The NACA 4412 is a cambered airfoil of 12% thickness. Near maximum lift,
at incidence $\alpha$ (page-local: angle of attack) of about $12^\circ$ to
$14^\circ$ and chord Reynolds number $Re_c\approx1.6\times10^6$, its
suction-side turbulent boundary layer develops under a growing adverse
pressure gradient and separates mildly ahead of the trailing edge: the
separation is smooth-surface, pressure-gradient-driven and not fixed by
the geometry. The quantities compared are the lift and drag coefficients
$C_L$, $C_D$, the pressure coefficient $C_p$ (with its trailing-edge
plateau, the signature of the separation) and the velocity profiles of
the suction-side layer. In this bundle it is a test of
[wall-modelled LES](/methods/wall-modelled-les.md) in mild-adverse-gradient
separation, and of RANS and [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
force predictions, for which the sources record that no method yet gets
both lift and drag right. Both reviews cite the experiment of Wadcock
(1978) as the reference (Bose & Park, Fig. 7a; Heinz, §5.4).

## Configurations in the sources

| Item | [Bose & Park (2018)](/sources/bose-2018.md), §4.3, Fig. 7a | [Heinz (2020)](/sources/heinz-2020.md), §5.4, Fig. 15 | [Eivazi et al. (2022)](/sources/eivazi-2022.md), §3 |
|---|---|---|---|
| Flow | $Re_c=1.6\times10^6$, $\alpha=13.8^\circ$ | LES and WMLES usually at $12^\circ\le\alpha\le14^\circ$; a RANS study of 13 models over $7\times10^5\le Re_c\le9\times10^6$, $-10^\circ\le\alpha\le20^\circ$ | suction-side layer, $0.5<x/c<1$, $Re_c=2\times10^5$ |
| Method | WMLES with equilibrium, nonequilibrium and dynamic slip-wall models (compiled) | RANS, DES, RSM-based PITM hybrids, LES and WMLES (compiled) | [physics-informed neural network](/methods/physics-informed-neural-network.md) solving the RANS equations without a turbulence model |
| Reference | experiment of Wadcock | experiments of Wadcock, Coles & Wadcock, and Pinkerton | well-resolved spectral-element LES of Vinuesa et al. |

Both reviews compile results of other studies; neither runs the airfoil.

## What the case tests

**Wall models in mild trailing-edge separation.** As compiled by
[Bose & Park (2018)](/sources/bose-2018.md), §4.3, the equilibrium and
nonequilibrium wall-stress models and the dynamic slip-wall model all
reproduce the trailing-edge pressure plateau at $13.8^\circ$; their
Fig. 7a shows the slip-wall $C_p$ against Wadcock's data, with a
leading-edge over-prediction that they attribute to artificially induced
transition. The review sets this against the Aerospatiale-A airfoil at
$Re_c=2.1\times10^6$, where algebraic, equilibrium and Kawai–Larsson
nonequilibrium models disagree on the trailing-edge separation, and
concludes that mild-adverse-gradient separation is sensitive to the
details of the wall model and is among the open validation problems (§4.3,
§5). See [equilibrium wall model](/methods/equilibrium-wall-model.md),
[nonequilibrium wall model](/methods/nonequilibrium-wall-model.md) and
[log-layer mismatch](/definitions/log-layer-mismatch.md). The airfoil is one
of the points of their compilation of WMLES cell counts, from which they
conclude that most airfoil calculations need $n_xn_yn_z\gtrsim20^3$ points per
$\delta^3$ (page-local: points per boundary-layer thickness in each
direction), a factor 3 to 5 above the Choi–Moin estimate (§3, Fig. 5); see
[grid-point requirements of LES](/results/les-grid-point-requirements.md).

**Forces of RANS, DES and hybrids.** [Heinz (2020)](/sources/heinz-2020.md),
§5.4, uses the airfoil to argue that the hybrid methods the review covers do not
yet give reliable integrated loads:

- no methodology predicts both lift and drag accurately;
- the best performer of the 13-model RANS evaluation cited there
  over-predicts the drag, while the cited hybrid simulations
  under-predict it;
- the DES of Beyhaghi & Amano under-predicts the drag by more than 34%;
- RSM-based PITM hybrids on about 3 million points reduce the RANS lift
  and drag errors from $(+14\%,-54\%)$ to $(+7\%,-39\%)$;
- LES and WMLES studies rarely compare lift and drag at all, and narrow
  spanwise domains can make WMLES "artificially close" to the data.

See [detached-eddy simulation](/methods/detached-eddy-simulation.md),
[Reynolds-stress models](/methods/reynolds-stress-model.md) and, for the
partially-integrated transport model (PITM) that Heinz classes with PANS
among the RANS-coefficient methods,
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[partially-averaged Navier–Stokes](/methods/partially-averaged-navier-stokes.md).

**The experimental basis.** [Heinz (2020)](/sources/heinz-2020.md), §5.4,
records that Wadcock's measurements are considered more accurate than
those of Coles & Wadcock and of Pinkerton, but that their validity "is
still debated"; [Bose & Park (2018)](/sources/bose-2018.md) compare with
Wadcock's data only. Neither review quantifies the experimental
uncertainty.

**A boundary-layer reconstruction case.** At a lower Reynolds number,
[Eivazi et al. (2022)](/sources/eivazi-2022.md), §3, Table 1, Fig. 5,
reconstruct the mean suction-side layer over $0.5<x/c<1$ at
$Re_c=2\times10^5$ from RANS residuals and boundary data, with relative
$\ell_2$ errors of 1.56% (streamwise velocity), 2.17% (wall-normal
velocity), 7.30% (pressure) and 9.43%, 11.36%, 4.69% for $R_{11}$, $R_{12}$,
$R_{22}$, and inner-scaled profiles at $x/c\simeq0.625$, 0.75 and 0.875 in
"excellent agreement" with the LES; the case, with its adverse pressure
gradient, is also on
[turbulent boundary layers](/benchmarks/turbulent-boundary-layer.md). It
tests the network's reconstruction from boundary data, not a turbulence
model's prediction.

**What the two reviews report.** Bose & Park report that wall models
capture the trailing-edge $C_p$ plateau; Heinz reports that the force
predictions of RANS-based and hybrid methods remain far from the data.
The statements concern different quantities ($C_p$ plateau against
integrated forces) and different method classes.

## Qualifications

- Both reviews compile published results; no source on this page runs a
  new simulation of the airfoil near stall, and neither prints the force
  coefficients of the WMLES studies it cites.
- [Heinz (2020)](/sources/heinz-2020.md) gives the RANS evaluation's grid
  only as two-dimensional grids of up to about 300,000 elements, and the
  PITM hybrid's errors as quoted from the cited works.
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) were read in arXiv v1;
  their case is the boundary layer of the airfoil at $Re_c=2\times10^5$,
  not the near-stall flow of the reviews, and their network needs the
  reference Reynolds stresses on the domain boundaries.

# Citations

- [Bose & Park (2018)](/sources/bose-2018.md) — §3, Fig. 5; §4.3, Fig. 7a; §5.
- [Heinz (2020)](/sources/heinz-2020.md) — §5.4, Fig. 15 (compiled results).
- [Eivazi et al. (2022)](/sources/eivazi-2022.md) — §3, Table 1, Fig. 5 (arXiv v1).
