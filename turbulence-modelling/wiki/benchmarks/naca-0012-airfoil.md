---
type: Benchmark
title: "NACA 0012 airfoil"
description: "The symmetric NACA 0012 airfoil at chord Reynolds numbers of 1 to 6 million, from attached incidence to near stall and to 45° massive separation, and transonic at Mach 0.804: a validation case of high-order DG RANS, of immersed-boundary wall-modelled RANS and of lattice Boltzmann hybrid RANS/LES."
status: established
aliases: [NACA0012, NACA 0012, NACA-0012]
tags: [benchmark, rans, hybrid-rans-les, immersed-boundary, dg, separated-flow]
timestamp: 2026-10-26T10:26:00Z
---

# NACA 0012 airfoil

The NACA 0012 is a symmetric airfoil of 12% thickness. At low Mach number
and chord Reynolds numbers $Re_c$ of a few million its boundary layers are
attached at small incidence $\alpha$ (page-local: angle of attack), lift
grows linearly with $\alpha$, and near stall the suction peak and the thin
leading-edge boundary layer dominate the forces; at very high incidence the
flow separates massively from the leading edge. The quantities compared are
the lift and drag coefficients $C_L$ and $C_D$, the pressure coefficient
$C_p$ and the skin friction $C_f$ along the chord $c$. Reference data
recalled by the sources are the measurements of Ladson (forces and $C_p$) and
the compilation of McCroskey. In this bundle the airfoil validates
discretizations and near-wall treatments of RANS and hybrid RANS/LES rather
than a turbulence model as such.

## Configurations in the sources

| Item | [Zhao et al. (2023b)](/sources/zhao-2023-b.md) | [Constant et al. (2024)](/sources/constant-2024.md) | [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) |
|---|---|---|---|
| Flow | $M=0.15$, $Re_c\approx6\times10^6$, $\alpha=0^\circ$, $10^\circ$; transonic $M=0.804$, $Re_c=4.09\times10^6$, $\alpha=0.05^\circ$ | $M=0.15$, $Re_c=6\times10^6$, $\alpha=0^\circ$ to $15^\circ$ | $Re_c=3\times10^6$, $\alpha=2^\circ$, $6^\circ$, $10^\circ$, $15^\circ$ and $45^\circ$; Mach number not stated |
| Model | [$k$-$\omega$ SST](/methods/k-omega-sst-model.md) RANS, wall-resolved | [Spalart–Allmaras](/methods/spalart-allmaras-model.md) RANS with Musker's wall function | SST RANS, SST-IDDES and SST-based continuous eddy simulation |
| Discretization | interior-penalty DG of degree $N=2$ for the mean flow, first-order finite volumes for SST | ghost-cell [immersed boundary](/methods/immersed-boundary-method.md) on octree Cartesian grids, second-order finite volumes (FastS) | [lattice Boltzmann](/methods/lattice-boltzmann-method.md) D3Q19 on octree Cartesian grids with immersed boundaries ([ProLB](/software/prolb.md)) |
| Grid | 5883 elements (grid independence on 6834, 8844, 10854); 8954 cells transonic | IBM6: $h_{\min}/c=10^{-4}$, target $y^+=100$, $3.8\times10^6$ cells; body-fitted wall-resolved reference with $h_{\min}/c=10^{-6}$, $y^+=1$, $8\times10^6$ cells | 7 refinement levels to $\Delta_{\min}\approx0.18\%c$; span equal to chord, periodic |
| Reference | Ladson ($C_p$), McCroskey (forces), ONERA data (transonic) | the body-fitted wall-resolved solution | Ladson (forces, $C_p$); for $45^\circ$ the data of Shur et al. as cited |

## What the case tests

**Attached and moderate incidence.** [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§5.2, obtain $C_p$ coinciding with Ladson's experiment at $0^\circ$ for
polynomial degrees 1 to 3, and agreement with experiment at $10^\circ$ (Figs.
5-4, 5-6). Their forces (Table 5-1) are:

| $\alpha$ | $C_L$ IPDG / McCroskey | $C_D$ IPDG / McCroskey |
|---|---|---|
| $0^\circ$ | 0.00 / 0.00 | 0.0084 / 0.0083 |
| $10^\circ$ | 0.93 / 1.05 | 0.011 / 0.012 |

The authors attribute the $10^\circ$ lift deficit "probably" to the RANS
assumption; it is 11.4% *(compiler check, not in the sources)*. On the
lattice Boltzmann solver, [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
§3.2, find $C_L$ and $C_D$ close to Ladson's data at $2^\circ$, $6^\circ$ and
$10^\circ$ for all three models, with a slight RANS discrepancy at $15^\circ$
(Fig. 12). IDDES, CES and RANS give identical mean $C_p$ at $10^\circ$; at
$15^\circ$ the hybrids differ slightly downstream of the leading edge
because the fine leading-edge grid lets them run as LES in the outer
boundary layer with only the first few nodes in RANS (Figs. 10–11); see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[detached-eddy simulation](/methods/detached-eddy-simulation.md).

**Near stall with an immersed boundary and a wall function.**
[Constant et al. (2024)](/sources/constant-2024.md) (read in the HAL
author manuscript) use the airfoil at $15^\circ$ as the "critical flow
incidence" for wall-function boundary conditions on Cartesian grids:

- A modelling height estimated from a flat-plate skin-friction correlation
  places the first computed point at a $y^+$ far above the target near the
  leading edge: the relative error is "close to 300%" for a target of 300
  at $15^\circ$ (§4.1, Fig. 10). After their one-pass adaptation, the
  largest suction-side $y^+$ falls from 435 to 243 for a target of 100
  (§6.1, Fig. 18).
- Over the first 10% of the chord the equilibrium wall function cannot
  represent the velocity profile; beyond it the log region is established
  (§6.1, Figs. 19–21); see
  [equilibrium wall model](/methods/equilibrium-wall-model.md) and
  [wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md).
- Extrapolating the wall pressure from the image point with zero normal
  gradient misplaces the suction peak; a first- or second-order
  reconstruction from a second layer of image points corrects it (§6.1,
  Figs. 23–24).

Forces at $15^\circ$ (Table 3):

| Solution | $C_D\times10^3$ | error | $C_L$ |
|---|---|---|---|
| body-fitted, wall-resolved | 20.85 | — | 1.516 |
| IBM, single modelling height, zeroth-order pressure | 40.44 | 94% | 1.416 |
| IBM, adapted height, zeroth-order pressure | 30.57 | 47% | — |
| IBM, adapted height, second-order pressure | 24.51 | 17% | 1.476 |

Only the adapted solution keeps the lift error below 3% at every incidence
(Fig. 25). The authors relate the remaining drag error of about 20% at
$15^\circ$ to the sensitivity of this test case reported by others, and to
the equilibrium wall model at the leading edge (§6.1).

**Massive separation at $45^\circ$.** [Mozaffari et al. (2024)](/sources/mozaffari-2024.md),
§3.2, Table 2, after 234 flow-through times with 110 averaged:

| Model | $C_L$ | $C_D$ |
|---|---|---|
| SST RANS | 2.238 | 2.053 |
| SST-IDDES | 1.231 | 1.038 |
| SST-CES | 1.192 | 0.993 |
| reference (Shur et al., as cited) | 1.097 | 1.180 |

The RANS lift and drag exceed the reference by factors of about 2.0 and
1.7 *(compiler check, not in the sources)*; the two hybrids "perform
almost the same without any superiority" (§3.2).

**Transonic shock.** At $M=0.804$, [Zhao et al. (2023b)](/sources/zhao-2023-b.md),
§5.3, place the shock at $x\approx0.47c$ with $C_p$ extrema consistent with
ONERA data, but "the ending position of the shock wave slightly lags
behind", attributed to an overestimated shock–boundary-layer interaction
(Figs. 5-9–5-11); see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md).

**Implicit LES polars.** As recalled by [Ferrer et al. (2023)](/sources/ferrer-2023.md),
§4.1, Fig. 7, from the group's earlier paper, a DG implicit LES at
$Re_c=10^6$ on 18,000 hexahedra with $N=4$ (2.2 million degrees of freedom)
gives lift and drag polars in "very good agreement" with experimental data
not named in that paper; see [implicit LES](/definitions/implicit-les.md)
and [HORSES3D](/software/horses3d.md).

**What the sources share.** Away from stall the RANS solutions of all
three discretizations match the reference forces; the discrepancies
gather at the leading edge at high incidence: the $10^\circ$ lift deficit
in [Zhao et al. (2023b)](/sources/zhao-2023-b.md), the wall-function
leading-edge error at $15^\circ$ in
[Constant et al. (2024)](/sources/constant-2024.md), the $15^\circ$ RANS
discrepancy in [Mozaffari et al. (2024)](/sources/mozaffari-2024.md).

## Qualifications

- The configurations differ in Reynolds number ($10^6$, $3\times10^6$,
  $6\times10^6$) and reference ($C_p$ and forces of experiments, a
  body-fitted computation); no source compares its errors with another's.
- [Constant et al. (2024)](/sources/constant-2024.md) print a lift error
  of 5.6% for the non-adapted solution in Table 3, while the table's own
  coefficients give 6.6%, and call the non-adapted lift error at $15^\circ$
  "almost 10%" in the text *(compiler check, not in the sources)*.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) head the
  $45^\circ$ reference column "Exp." while citing Shur et al.'s
  detached-eddy simulation of an airfoil at high incidence; they mention
  $60^\circ$ without reporting results. The chord is not stated.

# Citations

- [Zhao et al. (2023b)](/sources/zhao-2023-b.md) — §5.2, Table 5-1, Figs. 5-4–5-6; §5.3, Figs. 5-9–5-11.
- [Constant et al. (2024)](/sources/constant-2024.md) — §4.1, Fig. 10; §5.1, Figs. 12–13; §6.1, Tables 1–3, Figs. 18–25.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §3.2, Table 2, Figs. 9–12.
- [Ferrer et al. (2023)](/sources/ferrer-2023.md) — §4.1, Fig. 7 (recalled result).
