---
type: Benchmark
title: "Flow past a square cylinder"
description: "Turbulent flow past a square cylinder with separation fixed at the front corners: at Re 21,400–22,000 a test of data assimilation into Spalart–Allmaras RANS (momentum sources fit the DNS mean flow, eddy-viscosity multipliers fail), of a DNS-database subgrid closure, SST-DDES variants and a wall-modelled immersed boundary; at Re 10,000 a 2D URANS test of the k-√k-L model."
status: established
aliases: [square cylinder, square-cylinder wake, flow over a square cylinder, SQCYL]
tags: [benchmark, separated-flow, rans, field-inversion, data-driven, dg, des, immersed-boundary]
timestamp: 2026-10-29T10:03:00Z
---

# Flow past a square cylinder

A uniform stream passes a square cylinder of side $L_{\mathrm{sq}}$
(page-local). Separation is fixed at the corners
([Cato et al. (2023)](/sources/cato-2023.md), §V), the wake is turbulent,
and the time-averaged flow has a recirculation bubble behind the body.
[Fanizza et al. (2025)](/sources/fanizza-2025.md) build the Reynolds
number on $L_{\mathrm{sq}}$ and the free-stream velocity (§4.2). Both sources use $Re=22{,}000$ and the DNS of Trias,
Gorobets & Oliva (2015) as reference, assimilating its time-averaged
velocity field into steady two-dimensional RANS with the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md). In this
bundle the case tests which correction term of a RANS model can absorb the
model error of a bluff-body wake (see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)),
next to the [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md).
At $Re=10^4$ and in two dimensions the case also tests whether a
length-scale-adaptive RANS model lets an unsteady wake develop
([Jiang et al. (2025)](/sources/jiang-2025.md), §4.3). At $Re=22{,}000$
the same DNS is also the reference of a scale-resolving closure test
([Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.6) and of a
hybrid RANS/LES validation ([Wu et al. (2024)](/sources/wu-2024.md),
§3.1b).

## Configurations in the sources

| Item | [Cato et al. (2023)](/sources/cato-2023.md) | [Fanizza et al. (2025)](/sources/fanizza-2025.md) |
|---|---|---|
| Equations | incompressible steady RANS, negative SA variant | compressible steady RANS at $M=0.1$, SA |
| Discretization | finite elements (FreeFEM), first cells below $y^+=1$, grid convergence stated without details | modal discontinuous Galerkin (Aghora), $N=2$, 45,000 elements |
| Domain | coordinates scaled by the side; not otherwise printed | half domain $(-10,10)\times(0,10)$ in units of $L_{\mathrm{sq}}$ with a symmetry plane, non-reflecting outer boundaries, adiabatic no-slip walls |
| Data | dense time-averaged DNS velocity | dense time-averaged DNS velocity |
| Optimizer | adjoint, L-BFGS | discrete adjoint, L-BFGS; flexible inner–outer GMRES for the adjoint system |

## What the case tests

**Ranking of the correction terms.** Both sources compare corrections of
the same kinds, one at a time, under the same cost.

- [Cato et al. (2023)](/sources/cato-2023.md), §V A–B, Figs. 12–15: the
  momentum forcing vector and the divergence of a trace-free tensor
  reproduce the DNS (the latter "slightly noisier"); a source proportional
  to $\tilde\nu$ in the SA equation "performed almost as well as the source
  terms in the momentum equations"; a production multiplier and an additive
  SA source improve the result partially, the additive source degrading the
  shear layer above the cylinder; the eddy-viscosity multiplier "was not
  able to correct the field". There is no error table for this case.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md), §4.2, Figs. 7–8: a
  momentum and energy source corrects the velocity best, then the source
  proportional to $\tilde\nu$ in the SA equation and the production
  multiplier; the eddy-viscosity multiplier "lacks precision" and its cost
  stays on a plateau "from the very first iterations". The cost falls by at
  least one order of magnitude for the production multiplier, more than
  one for the SA source and more than two for the momentum source. The
  authors state agreement with Cato et al., who used an incompressible
  solver.

In Fanizza et al. the momentum source needs more
iterations, which the authors attribute to an optimization problem three
times larger in 2D (two momentum components and an energy component,
against one SA field).

**Mean flow against Reynolds stresses.** Baseline SA predicts a
recirculation bubble larger than the DNS (both sources; Cato et al.,
Fig. 11) and Reynolds stresses "very weak compared to the DNS"; the
stress–strain alignment indicator exceeds 0.8 only in "a few areas"
([Cato et al. (2023)](/sources/cato-2023.md), §V A, Fig. 12; see
[Boussinesq hypothesis](/definitions/boussinesq-hypothesis.md)). After
assimilation the stresses rise, but no correction reproduces the DNS
stresses, not even the trace-free-tensor divergence with its large drop of
the cost; near the corners its stresses and those of the proportional
source are wrong. Cato et al. conclude that "the mean-flow prediction can
be accurate even though the Reynolds stresses are wrong", as long as the
Reynolds force vector is right: the tensor divergence reproduces the
streamwise force reasonably, the momentum forcing the streamwise but not
the cross-stream component, and the proportional source gives "a realistic
stress tensor especially in the wake region" (§V C, Figs. 16–19).
[Fanizza et al. (2025)](/sources/fanizza-2025.md) make the related point
on their supersonic interaction that only the momentum source escapes the
Boussinesq constraint (see
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).

**Unsteady RANS with a length-scale-adaptive model.**
[Jiang et al. (2025)](/sources/jiang-2025.md), §4.3, run the
$k$-$\sqrt kL$ model behind
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md) in a
fourth-order modal discontinuous Galerkin solver at $Re=10^4$ on the side,
$M_\infty=0.05$, with an outer boundary at about 30 sides, 6188
quadrilaterals and 9896 triangles, first-cell $y^+\approx0.5$ and ESDIRK
time stepping, averaged over about 20 shedding cycles; the reference is a
two-dimensional DNS of Wissink at the same conditions, and the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md) is run for
comparison. Through the von Kármán length scale the model gives a smaller
eddy viscosity than SA in the separated wake and "slightly chaotically
vortex flows" behind the cylinder, which the authors call SAS-like
characteristics (Figs. 8–9). Time-averaged velocities agree well with the
DNS at the stations above the cylinder and follow the general trend at the
wake stations $x/L_{\mathrm{sq}}=2$–5 (the source's $x/h$; Figs. 10–11). The authors call the 2D
computation a verification, not a validation, since the flow is
three-dimensional, and the SA comparison "may not be a fair comparison"
because SA is meant for steady high-Reynolds-number flow; a fair one would
be three-dimensional DES or SAS (§4.3).

**A DNS-database subgrid closure against LES.**
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.6, Figs.
17–18, Table 2, run
[pseudo-direct numerical simulation](/methods/pseudo-direct-numerical-simulation.md),
whose subgrid stress comes from a database of DNS on representative volume
elements, and an LES with the dynamic $k$-equation subgrid model of Kim
& Menon (§2.10, see
[subgrid kinetic-energy equation models](/methods/subgrid-kinetic-energy-equation-model.md))
on the same mesh of about 2 million hexahedra (domain
$27\times13\times\pi$ sides in the streamwise, cross-stream and spanwise
directions, cell size $0.04L_{\mathrm{sq}}$ at the surface, symmetry top and
bottom, periodic span; second-order schemes at Courant number at most 1;
300 time units, the last 200 averaged), against the 300-million-cell DNS of
Trias et al. With $L_r$ the length of the mean recirculation behind the
cylinder in units of $L_{\mathrm{sq}}$:

| Quantity | DNS (Trias et al.) | P-DNS | LES |
|---|---|---|---|
| cells | 300 M | 2 M | 2 M |
| $St$ | 0.132 | 0.127 | 0.115 |
| mean $C_D$ | 2.18 | 2.551 | 2.701 |
| rms of $C_D$ | 0.205 | 0.233 | 0.293 |
| mean $C_L$ | 0.002 | 0.044 | 0.049 |
| rms of $C_L$ | 1.71 | 1.574 | 1.771 |
| $L_r$ | 1.04 | 1.108 | 1.404 |

The two large recirculations above and below the cylinder are predicted,
the secondary corner recirculations are not, which the authors attribute
to the lack of grid refinement; the main vortex near the cylinder is
placed more accurately by P-DNS than by the LES, while the large mean-flow
curvatures upstream are "only partially predicted by both approaches", and
the Reynolds-stress profiles agree better with the DNS for P-DNS (Fig. 18).
P-DNS is closer to the DNS than the LES in every row of the table except
the rms lift, where the LES is closer *(compiler check, not in the
sources)*.

**A unified RANS/LES model as validation.**
[Wu et al. (2024)](/sources/wu-2024.md), §3.1b, Figs. 5–6, use the case to
validate SATES-σ, their variant of
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md),
in [PHengLEI](/software/phenglei.md) with the fourth-order
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md),
at $Re=2.2\times10^4$ on the side and $M=0.2$. The domain follows the DNS
of Trias et al.: $10L_{\mathrm{sq}}$ upstream, $19.5L_{\mathrm{sq}}$
downstream, a periodic span of $3.14L_{\mathrm{sq}}$; the grids have 0.66 M
and 1.73 M cells with $y^+<1$, time steps printed as
$\Delta t\,D/U_\infty=5\times10^{-3}$ and $2.5\times10^{-3}$ ($D$ the
source's side), and 300 time
units of which the last 160 are averaged. Mean velocities and resolved
normal stresses at $x/L_{\mathrm{sq}}=0$, 1, 2, 3 agree well with the DNS
and with the LDV data of Lyn et al. on both grids. No integral quantities
($St$, $C_D$, $L_r$) are printed for this case.

**SST-DDES with adaptive eddy-viscosity filtering and grid scale.**
[Guo & Wang (2025)](/sources/guo-2025.md), §2.2.1, §3.1, run the cylinder
at $Re=U_\infty L_{\mathrm{sq}}/\nu=21{,}400$ ($L_{\mathrm{sq}}=0.04$ m,
$U_\infty=0.535$ m/s) in [OpenFOAM](/software/openfoam.md)-v2306 with four
variants of the [$k$-$\omega$ SST](/methods/k-omega-sst-model.md)-based
DDES (see [detached-eddy simulation](/methods/detached-eddy-simulation.md)):
MAX- and ADD- denote the maximum cell size and the authors' adaptive
switch to the least-squares length of Trias et al. as subgrid length,
-FDDES the damping of the SST eddy viscosity where the RANS length
exceeds a resolvable filter width. The domain reaches $5L_{\mathrm{sq}}$
upstream and $15.5L_{\mathrm{sq}}$ downstream, height $14L_{\mathrm{sq}}$,
span $9.8L_{\mathrm{sq}}$ periodic, about 4.08 million cells with a
refined wake box and [RANS wall functions](/methods/rans-wall-function.md)
on the cylinder ($y^+$ not printed); the grid was shown converged in an
earlier paper of the authors; forces are averaged over 3.5–10 s, on 64
cores in about 288 core-hours. Their Table 4, with $L_r$ the
recirculation length measured from the cylinder centre:

| Run | $St$ | mean $C_D$ | rms $C_L$ | rms $C_D$ | $L_r$ |
|---|---|---|---|---|---|
| MAX-SSTDDES | 0.127 | 2.43 | 1.26 | 0.28 | 1.46 |
| ADD-SSTDDES | 0.120 | 2.74 | 1.43 | 0.17 | 1.27 |
| MAX-SSTFDDES | 0.135 | 2.48 | 1.43 | 0.26 | 1.39 |
| ADD-SSTFDDES | 0.127 | 2.71 | 1.60 | 0.20 | 1.42 |
| DNS, Trias et al. ($Re=22{,}000$, as quoted) | 0.132 | 2.18 | 1.71 | 0.205 | 1.04 |
| experiment, Lyn et al. (as quoted) | 0.13 | 2.1 | — | — | 1.4 |
| range compiled by Rodi (as quoted) | 0.09–0.15 | 2.17–2.77 | 1.15–1.79 | 0.14–0.27 | 0.94–1.68 |

The DNS values they quote equal those of the
[Idelsohn et al. (2024)](/sources/idelsohn-2024.md) table above *(compiler
check, not in the sources)*. The
authors call all mean drags "slightly higher than the experimental …
data" but within Rodi's range, the adaptive variants giving the higher
drag; they find the ADD-SSTFDDES rms lift (1.60) close to the DNS (1.71)
and its rms drag (0.20) closest to the DNS 0.205. Qualitatively, the
baseline separates late, with a narrow initial wake, a short
recirculation and slow recovery, while ADD-SSTFDDES separates earlier and
keeps more small vortices in the mid and far wake; the authors judge the
variants also by how close the probability density of the streamwise
fluctuations at wake probes is to a Gaussian, ADD-SSTFDDES being the
closest (§3.1, Figs. 10–20).

**A wall-modelled immersed boundary in a compact high-order code.**
[Yan et al. (2024)](/sources/yan-2024.md), §III B, run the cylinder at
$Re_D=2.2\times10^4$ in [Xcompact3d](/software/xcompact3d.md) (sixth-order
compact differences, implicit
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md)
with $\nu_0/\nu=80$), the walls represented by a diffused-interface
[immersed boundary](/methods/immersed-boundary-method.md) carrying an
explicit wall function with a pressure-gradient correction (see
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)):
domain $-5\le x/L_{\mathrm{sq}}\le15$, $-10\le y/L_{\mathrm{sq}}\le10$,
span $4L_{\mathrm{sq}}$, grid $601\times291\times30$ with about 30 points
per side, $U_0\Delta t/L_{\mathrm{sq}}=2.5\times10^{-3}$. They obtain mean
$C_D=2.46$, rms $C_L=1.06$, $L_r/L_{\mathrm{sq}}=0.81$ (printed $l_r/D$)
and $St=0.144$, against the DNS values of Trias et al. 2.18, 1.71, 1.04
and 0.132 (Table IV), calling the rms lift and recirculation length
"slightly lower" than the references. The wall model misses the two small
leading- and trailing-edge recirculation bubbles of wall-resolving LES,
which the authors attribute to the assumed constant pressure gradient
between probe and wall and to the coarse mesh (Figs. 12–13). The cost is
13.2 CPU hours per shedding cycle, against about 1058 and 676 hours they
infer for two wall-resolving LES (Table V).

**A $p$-adaptive DG LES with dynamic load balancing.**
[Valvo & Abbà (2025)](/sources/valvo-2025.md), §5, use the cylinder at
$Re=22{,}000$ and $M=0.3$ as the second test of dynamic load balancing in
the $p$-adaptive local discontinuous Galerkin solver dg-comp: a
two-dimensional section of side $L_{\mathrm{sq}}=1$ extruded over a span of
$4L_{\mathrm{sq}}$, with domain extents $L_f=10$ upstream, $L_r=20$
downstream and $L_y=10$ cross-stream (their Table 8), 23,816 tetrahedra refined near the body, sponge layers at
inflow and outflow, slip walls top and bottom, periodic span; a compressible
[Smagorinsky](/methods/smagorinsky-model.md) LES with $\Delta t=0.0004$,
the degree adapted within $2\le N\le4$ by a structure-function indicator
of under-resolution (see [mesh adaptation](/methods/mesh-adaptation.md)).
Their Table 9 compares the uniform $N=4$ run (833,560 degrees of freedom)
with the adaptive run without load balancing (about 463,000):

| Run or reference | mean $C_D$ | column "RMS$_{C_L}$" | column "RMS$_{C_D}$" |
|---|---|---|---|
| uniform $N=4$ | 2.445 | 0.1531 | 1.366 |
| $p$-adaptive, no load balancing | 2.3818 | 0.1934 | 1.305 |
| "Other LES data" (Rodi et al. workshop, as printed) | 1.66–2.77 | 0.10–0.27 | 0.38–1.79 |

The authors place both mean drags within the LES range of Rodi et al. and
call the statistics of the two runs equivalent (Table 9; Fig. 16 compares
the two centreline velocities only, with no experimental or DNS curve).
The case is used to measure cost: adaptation without load balancing saves
only 9.2% of the elapsed time (18,568 s to 16,866 s) although the degrees
of freedom fall by about 45%, while repartitioning with Zoltan saves 40.9%
to 44.6% against the uniform run, which the authors call "near to the
theoretical optimum" (Tables 10–11). The averaging window is not printed.

**Vortex-driven $h$-adaptation of a laminar wake.**
[Lv et al. (2025)](/sources/lv-2025.md), §V A, take a laminar,
two-dimensional version of the case, $Re=150$ and $M_\infty=0.3$ (after
Jacobs & Armstrong), to test a high-order discontinuous Galerkin solver
($N=2$, direct DG viscous flux, SSP-RK3) with $h$-adaptive refinement on
quadrilaterals with hanging nodes, driven either by the $\Omega$ criterion
or by a characteristic-based vortex indicator found by symbolic regression
(see [vortex identification criteria](/definitions/vortex-identification-criterion.md)).
Both adaptive runs, from 13,268 elements with two refinement levels,
concentrate cells in the vortex street and resolve it about as well as a
uniform grid of 80,000 elements at $t=2$ (Figs. 6–7); the serial CPU times
are 12.05 min (coarse uniform), 230.37 min (fine uniform), 40.88 min
($\Omega$-driven) and 43.58 min (indicator-driven), reductions of 82.25%
and 81.08% against the fine grid (Table I). No force coefficient, Strouhal
number or reference data is printed; the flow is laminar and no turbulence
model is used.

**Adjoint solvers.** [Fanizza et al. (2025)](/sources/fanizza-2025.md),
§3.4.1, Fig. 2, use the first adjoint system of this optimization to
compare linear solvers at a 180-vector memory budget: GMRES(180) with
block-ILU(0) does not converge, flexible GMRES (outer and inner Krylov
sizes 60) converges in 12,000 matrix–vector products and its
deflated-restart variant in 8000; plain GMRES would need a Krylov space of
860 to match. The inner solve runs in single precision.

## Qualifications

- [Cato et al. (2023)](/sources/cato-2023.md) (read in a HAL author
  manuscript) give no mesh details beyond $y^+<1$ and do not state the
  Reynolds-number definition; their correction $f_{\tilde\nu}$ of the SA
  equation is the additive source, while the source of
  [Fanizza et al. (2025)](/sources/fanizza-2025.md) enters as
  $\rho\tilde\nu f_{\tilde\nu}$ in their notation ($\rho\tilde\nu g_{\tilde\nu}$
  on their Source page) and corresponds to Cato et al.'s
  proportional source, although Fanizza et al. credit it to Cato et al. as
  "a source term ... in the SA equation".
- Fanizza et al. write the production correction as $(1+\beta)$ around
  zero, not as the multiplier with nominal value 1 of Singh & Duraisamy
  that they cite.
- Both studies assimilate dense full-field data; neither tests sparse data
  on this case.
- The $Re=22{,}000$ assimilation studies and the $Re=10^4$ URANS of
  [Jiang et al. (2025)](/sources/jiang-2025.md) use different references
  (a three-dimensional DNS against a two-dimensional one) and are not
  compared with each other. Jiang et al. print the upper-side stations of
  Fig. 10 in the non-monotone order $x/L_{\mathrm{sq}}=0.48$, 0.12, 0.1, 0.49.
- [Wu et al. (2024)](/sources/wu-2024.md) write the 300 time units as
  "flow-through times ($tU_\infty/C$)" with the chord symbol $C$ of their
  airfoil case, and normalize the profiles by $U_0$ while the set-up uses
  $U_\infty$ (§3.1b).
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md), §2.10.6, write
  that P-DNS "results in lR = 1.04", the DNS value, while their Table 2
  prints 1.108 for P-DNS and 1.04 for the DNS. They place the Reynolds
  stresses in Fig. 18b, c in one sentence and in Fig. 18d, e in another.

- [Guo & Wang (2025)](/sources/guo-2025.md) measure $L_r$ from the
  cylinder centre to the end of the mean recirculation, where the
  centreline pressure first returns to its upstream value, and quote the
  same 1.04 for the DNS that [Idelsohn et al. (2024)](/sources/idelsohn-2024.md)
  print for the recirculation behind the cylinder. Guo & Wang call the ADD-SSTDDES rms drag
  0.17 "slightly lower than the experimental and DNS ranges", while their
  Table 4 lists a DNS range of 0.117–0.181 that contains it, and give a
  "LES/DES reference range of 0.18–0.22" that does not match the LES/DES
  entries of the same table; they print the projected area as
  "$0.04*0.392=0.1568$ m²", which evaluates to 0.01568 m² *(compiler
  check, not in the sources)*. Their closeness-to-Gaussian criterion for
  the wake fluctuations is not compared with DNS or experimental
  distributions in the paper. They print no time step.
- [Yan et al. (2024)](/sources/yan-2024.md) print the cost of the two
  wall-resolving LES as inferred from those works; they define their
  $l_r$ only as the "length of the recirculation bubble" (nomenclature) and
  write $D$ for the side.
- The Rodi workshop range is printed differently by two sources:
  [Guo & Wang (2025)](/sources/guo-2025.md), Table 4, give mean $C_D$
  2.17–2.77, rms $C_L$ 1.15–1.79 and rms $C_D$ 0.14–0.27;
  [Valvo & Abbà (2025)](/sources/valvo-2025.md), Table 9, give mean $C_D$
  1.66–2.77 and, under the column headings RMS$_{C_L}$ and RMS$_{C_D}$,
  0.10–0.27 and 0.38–1.79. Valvo & Abbà's own entries under the same
  headings are 0.1531 and 1.366 (uniform run) and 0.1934 and 1.305
  (adaptive run). The two sources cite different works of the workshop:
  Guo & Wang the J. Wind Eng. Ind. Aerodyn. comparison of LES and RANS
  around bluff bodies, Valvo & Abbà the J. Fluids Eng. workshop report
  (both 1997).
- [Valvo & Abbà (2025)](/sources/valvo-2025.md) compare the cylinder
  statistics only between their adaptive and uniform runs and with the
  workshop range; no averaging window is printed.
- [Lv et al. (2025)](/sources/lv-2025.md) compare their adaptive runs
  with the uniform grids visually only.

# Citations

- [Cato et al. (2023)](/sources/cato-2023.md) — §II B; §V A–C, Figs. 11–19.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §3.3, Eqs. 26–31; §3.4.1, Fig. 2; §4.2, Figs. 7–8.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §4.3, Figs. 8–11.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.10.6, Figs. 17–18, Table 2.
- [Wu et al. (2024)](/sources/wu-2024.md) — §3.1b, Figs. 5–6.
- [Guo & Wang (2025)](/sources/guo-2025.md) — §2.1; §2.2.1; §3.1, Table 4, Figs. 10–20.
- [Yan et al. (2024)](/sources/yan-2024.md) — §III B, Tables IV–V, Figs. 10–13.
- [Valvo & Abbà (2025)](/sources/valvo-2025.md) — §5, Tables 8–11, Fig. 16.
- [Lv et al. (2025)](/sources/lv-2025.md) — §V A, Table I, Figs. 5–7.
