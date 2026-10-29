---
type: Benchmark
title: "Supersonic axisymmetric base flow"
description: "The Mach 2.46 flow behind the blunt base of a cylindrical afterbody measured by Herrin & Dutton, a test of how fast a hybrid RANS/LES model and its scheme let the separated shear layer become turbulent; set-ups, reference data and the recirculation, reattachment, shear-stress and base-pressure results of SATES, IDDES, AIDDES and DDES runs."
status: established
aliases: [Herrin–Dutton base flow, Herrin and Dutton base flow, supersonic base flow, axisymmetric base flow, Mach 2.46 base flow]
tags: [benchmark, hybrid-rans-les, des, compressible, separated-flow, numerical-dissipation]
timestamp: 2026-10-29T10:03:00Z
---

# Supersonic axisymmetric base flow

The supersonic axisymmetric base flow is the flow behind the flat, blunt
base of a cylindrical afterbody aligned with a uniform supersonic stream,
at the conditions of the experiment of Herrin & Dutton (1994, as cited by
all three sources that run it): free-stream Mach number $M_\infty=2.46$
and base radius $R=31.75$ mm (page-local $R$). The attached boundary
layer of the afterbody separates at the base edge into an annular free
shear layer that encloses a recirculation region behind the base and
reattaches downstream
([Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.4;
[Wu et al. (2024b)](/sources/wu-2024-b.md), §IV.C.2;
[Wu et al. (2026)](/sources/wu-2026-b.md), §4.1). In this bundle it is a
test of [hybrid RANS/LES](/definitions/hybrid-rans-les.md): the incoming
boundary layer is treated in RANS mode and the question is how quickly
resolved turbulence appears in the initial shear layer, which depends on
the hybrid model's eddy viscosity there (the grey area) and on the
[numerical dissipation](/properties/numerical-dissipation.md) of the
scheme. $L_r$ is the recirculation length (registry §11), measured from
the base.

## Set-ups in the sources

| Item | [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.4 | [Wu et al. (2024b)](/sources/wu-2024-b.md), §IV.C.2 | [Wu et al. (2026)](/sources/wu-2026-b.md), §4.1 |
|---|---|---|---|
| Flow | $M_\infty=2.46$, $Re_R=1.632\times10^6$ on the base radius | $M_\infty=2.46$, $Re=45\times10^6$ per metre, $p_\infty=31\,415$ Pa, $T_\infty=145$ K | as Wu et al. (2024b); adiabatic no-slip base |
| Domain | $23R\times8R$; afterbody $8R$ long upstream of the base, chosen to match the measured momentum thickness of 1 mm upstream of the base; $15R$ downstream | inflow $8R$ upstream of the base (after Simon & Deck, as cited); far field $20R$ downstream and $8R$ radially; O–H blocks | uniform inflow $8R$ upstream (after Simon et al., as cited); far field $20R$ downstream and $8R$ radially |
| Model | SA-based [DDES](/methods/detached-eddy-simulation.md) with the shear-layer-adapted length, $C_{\mathrm{DES}}=0.65$ | [SATES](/methods/self-adaptive-turbulence-eddy-simulation.md) (BSL host) | SATES-SM, SATES-II, SST-IDDES, AIDDES |
| Scheme | second-order node-based finite volume, reference scheme against the [LD2C low-dissipation scheme](/methods/low-dissipation-low-dispersion-scheme.md) | fifth-order [WCNS](/methods/weighted-compact-nonlinear-scheme.md) with five nonlinear weightings | sixth-order WCNS with smooth scale-separating weights and adaptive Roe dissipation |
| Grids | 1.82, 2.06 (shear-layer refined) and 8.51 M cells | about 7 M and 42 M cells; "maximum $\Delta y^+$ far from the wall is estimated to be 2.0" | A1, A2: $5.07$ M cells ($N_\theta=120$, $N_r=50$; $\Delta x/R=0.01$ uniform or 0.005–0.022); B1, B2: $9.5$ M cells ($N_\theta=160$, $N_r=63$; 0.008 uniform or 0.005–0.016) |
| Time | $\Delta t=10^{-6}$ s $=0.018R/U_\infty$; $90R/U_\infty$ transient, $350R/U_\infty$ sampled | not recorded | $\Delta t\,U_\infty/R=0.003$ (A) and 0.002 (B); 70 000 steps, statistics over more than 30 000 |
| Averaging | time and azimuthal | — | time and circumferential |

($N_\theta$, $N_r$ page-local: points in the azimuthal and radial
directions as printed in Wu et al. 2026, Table 2.) Wu et al. (2026) find
"negligible discrepancies" of the SATES-II velocity profiles between their
four grids in the recirculation region and use B2 for the model
comparison (§4.1.1, Figs. 6–7).

## Reference data

The sources compare with the measurements of Herrin & Dutton as they
print them:

- base pressure flat at about $C_p=-0.102$; reattachment at $x/R=2.67$;
  turbulent shear stress at $x/R=1.57$ and 2.52 (Carlsson et al. 2023,
  §4.4, Fig. 10);
- recirculation length $L_r/R=2.63$; mean velocity at $x/R=0.1575$,
  0.9449, 1.8898 and 2.5197, the centreline velocity and the resolved
  turbulent kinetic energy (Wu et al. 2026, §4.1.3, Table 3, Figs. 9–11);
- resolved turbulent kinetic energy at $x/R=1.8898$ and 2.5197 (Wu et al.
  2024b, Fig. 14).

## Results

**Scheme dissipation in the initial shear layer.** Carlsson et al. (2023)
find that, with the shear-layer-adapted length, the onset of resolved
turbulence in the initial shear layer "is mainly governed by the amount
of numerical dissipation introduced by the numerical scheme and the
resolution of the grid": the reference scheme strongly delays resolved
structures and shows azimuthally coherent Kelvin–Helmholtz rollers, LD2C
unlocks the instability, and LD2C on the 1.82 M grid shows small scales
comparable to the reference scheme on 8.51 M cells (§4.4, Fig. 9).
Reattachment moves from $x/R\approx4.0$ (reference scheme, coarse grid)
and $\approx3.0$ (finer grids) to $\approx2.7$ with LD2C, and the shear
stress at $x/R=1.57$ agrees much better; the base pressure, however,
becomes wavy and under-predicted, with LD2C over-predicting the reverse
flow, so "improved numerics in the initial shear layer does not produce a
better prediction of the base pressure profile" (§4.4, Fig. 10). In the
same spirit, Wu et al. (2024b) find that Jiang–Shu weights of their WCNS
suppress the Kelvin–Helmholtz instability of the shear layer, while
TENO-type weights give more foot shocks under recompression and stronger
annular and axial shear-layer instability; on the 7 M grid the adaptive
smooth weights predict the resolved-energy peaks best, the fine-grid
reference being Jiang–Shu weights on 42 M cells; and within a time step the
sub-iteration residual falls by about one, three and two orders of
magnitude with the sharp, smooth and adaptive smooth cut-offs (§IV.C.2,
Figs. 12–14).

**Model eddy viscosity in the initial shear layer.** Wu et al. (2026)
compare four hybrids on the 9.5 M grid (Table 3):

| Model | $L_r/R$ | error | wall time (h, 640 cores) |
|---|---|---|---|
| SATES-SM | 3.17 | +20.5% | 50.28 |
| SATES-II | 2.81 | +6.8% | 51.59 |
| SST-IDDES | 3.58 | +36.1% | 45.30 |
| AIDDES | 2.81 | +6.8% | 46.54 |
| experiment | 2.63 | | |

*(Compiler check, not in the sources: $3.17/2.63=1.205$, $2.81/2.63=1.068$,
$3.58/2.63=1.361$.)* They attribute the IDDES overshoot to its delayed
RANS-to-LES transition in the separated shear layer, where its length-ratio
indicator "decays more slowly and remains at moderate values", while
AIDDES keeps the shielding of the attached boundary layer and drops
quickly in the shear layer; SATES-SM runs the upstream attached boundary
layer with $F_r$ of "about 0.2 − 0.4", i.e. too little modelled stress, and
SATES-II with $F_r\approx0.9$–1.0 (§4.1.2, Fig. 8). The resolved kinetic
energy of the shear layer deviates most with IDDES, less with SATES-SM,
and is most accurate with SATES-II, AIDDES being comparable (Fig. 11); the
remaining AIDDES deviations "may originate from the lack of a realistic
turbulent boundary layer at inlet" (§4.1.3).

**Earlier hybrid runs, as cited by Carlsson et al. (2023, §4.4).** An
SA-DES with the largest cell edge as grid length gave a good base
pressure but over-estimated the recirculation and under-predicted the
early shear-layer stresses, attributed to excessive eddy viscosity; the
ZDES of Simon et al. with the cube-root length and $C_{\mathrm{DES}}=0.55$
matched the recirculation length and the shear stress but over-predicted
the backflow, with a wavy, too low base pressure; an SA-DDES with the
shear-layer-adapted length (Guseva et al.) accelerated the instability
without a flat base pressure.

**Data-driven RANS.** Le et al. (2024), reviewing machine learning for
supersonic flow, cite an FIML-corrected Spalart–Allmaras model (Heo et
al.) that lowers the eddy viscosity in the separation region of a
supersonic axisymmetric base flow and improves the expansion and the
size of the vortex region ([Le et al. (2024)](/sources/le-2024.md),
§3.1.2, Fig. 11, as cited; see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md));
the review does not state the conditions of that case.

## What the case shows

- The separated shear layer is the sensitive region, as on the
  [30P30N slat cove](/benchmarks/30p30n-high-lift-airfoil.md): excess
  dissipation, from the scheme (Carlsson et al. 2023; Wu et al. 2024b) or
  from the hybrid model's eddy viscosity (Wu et al. 2026), delays its
  instability and lengthens the recirculation.
- Getting the shear layer and the reattachment right does not by itself
  give the flat measured base pressure (Carlsson et al. 2023, and the ZDES
  and DDES studies they cite).
- The hybrid's treatment of the attached boundary layer upstream of the
  base matters too: SATES-SM under-models it, and Wu et al. (2026) suspect
  the missing resolved inflow turbulence for the remaining deviations.

## Qualifications

- The three sources describe the experiment through the quantities they
  compare with; none reprints the experimental set-up beyond $M_\infty$,
  $R$ and the free-stream state.
- Carlsson et al. print $Re_R=1.632\times10^6$; Wu et al. (2024b, 2026)
  print $45\times10^6$ per metre, which with $R=31.75$ mm gives
  $Re_R\approx1.43\times10^6$ *(compiler check, not in the sources)*.
  The Source pages record no reference velocity or viscosity, so whether
  the two printed figures describe the same state is not established here.
- Wu et al. (2024b) and Wu et al. (2026) write the base radius $R_0$ in
  their figures and $R$ in the text; Wu et al. (2026) leave the "Points"
  column of their Table 2 (325, 406) unexplained. Wu et al. (2024b) give
  the fine-grid reference by one scheme (Jiang–Shu weights), not by
  experiment, for the coarse-grid ranking.
- Each comparison is one paper's model or scheme family on its own grids;
  no source compares SATES, DDES and ZDES on one grid and scheme.

## Contradictions

- **Measured reattachment length of the Herrin–Dutton experiment.**
  [Carlsson et al. (2023)](/sources/carlsson-2023.md), §4.4, Fig. 10,
  give the experimental reattachment point as $x/R=2.67$ and judge their
  LD2C runs ($x/R\approx2.7$) against it;
  [Wu et al. (2026)](/sources/wu-2026-b.md), §4.1.3, Table 3, give the
  experimental recirculation length, measured from the base, as
  $L_r/R=2.63$ and compute their model errors (+6.8 % to +36.1 %) from it.
  Both cite Herrin & Dutton (1994) for the value. *Open.*

# Citations

- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §4.4, Figs. 7–10 (set-up, grids, time step, SA-DDES with the shear-layer-adapted length, LD2C against the reference scheme, reattachment, shear stress, base pressure, earlier DES, ZDES and DDES runs as cited); §5.
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §IV.C.2, Figs. 11–14, Table I (set-up, SATES with five WCNS weightings, shear-layer instability, sub-iteration convergence, resolved-energy profiles, cost).
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §4.1, Table 2, Figs. 5–7 (set-up and grid study); §4.1.2, Fig. 8 (resolution indicators); §4.1.3, Table 3, Figs. 9–11 (recirculation length, cost, profiles, resolved energy).
- [Le et al. (2024)](/sources/le-2024.md) — §3.1.2, Fig. 11 (FIML-corrected SA on a supersonic axisymmetric base flow, as cited).
