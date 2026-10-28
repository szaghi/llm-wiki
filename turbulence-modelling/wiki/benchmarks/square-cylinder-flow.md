---
type: Benchmark
title: "Flow past a square cylinder"
description: "Turbulent flow past a square cylinder with separation fixed at the front corners and a shedding wake: at Re 22,000 a test of variational data assimilation into Spalart–Allmaras RANS, where momentum sources fit the DNS mean flow and eddy-viscosity multipliers fail, and of a DNS-database subgrid closure; at Re 10,000 a 2D URANS test of the k-√k-L model."
status: established
aliases: [square cylinder, square-cylinder wake, flow over a square cylinder, SQCYL]
tags: [benchmark, separated-flow, rans, field-inversion, data-driven, dg]
timestamp: 2026-10-28T02:40:00Z
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

The two rankings agree, across an incompressible finite-element and a
compressible high-order DG discretization. The momentum source needs more
iterations, which Fanizza et al. attribute to an optimization problem three
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

# Citations

- [Cato et al. (2023)](/sources/cato-2023.md) — §II B; §V A–C, Figs. 11–19.
- [Fanizza et al. (2025)](/sources/fanizza-2025.md) — §3.3, Eqs. 26–31; §3.4.1, Fig. 2; §4.2, Figs. 7–8.
- [Jiang et al. (2025)](/sources/jiang-2025.md) — §4.3, Figs. 8–11.
- [Idelsohn et al. (2024)](/sources/idelsohn-2024.md) — §2.10.6, Figs. 17–18, Table 2.
- [Wu et al. (2024)](/sources/wu-2024.md) — §3.1b, Figs. 5–6.
