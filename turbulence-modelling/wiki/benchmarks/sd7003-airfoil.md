---
type: Benchmark
title: "SD7003 airfoil"
description: "The Selig–Donovan SD7003 airfoil at chord Reynolds numbers 23,000 to 200,000, whose laminar separation bubble and separation-induced transition test implicit LES (the High-Order CFD Workshop case at 60,000 and 4° or 8°) and transitional RANS calibrations, against implicit LES, DNS, PIV and wind-tunnel references."
status: established
aliases: [SD7003, SD 7003, Selig–Donovan SD7003, SD7003 wing, High-Order CFD Workshop case C3.3]
tags: [benchmark, transition, implicit-les, separated-flow, flux-reconstruction, rans]
timestamp: 2026-10-29T05:14:00Z
---

# SD7003 airfoil

The SD7003 is a thin low-Reynolds-number airfoil on which, at chord
Reynolds numbers of a few $10^4$, the laminar boundary layer separates on
the suction side, transitions in the separated shear layer and reattaches
as a turbulent layer, forming a
[laminar separation bubble](/definitions/laminar-separation-bubble.md)
whose length shrinks as the incidence grows. The bubble couples the
three regimes a simulation must handle, which makes the airfoil a test of
[implicit LES](/definitions/implicit-les.md) that has to pass "in a
seamless fashion" through "the mixed laminar, transitional, and turbulent
flow regions" ([Wang et al. (2013)](/sources/wang-2013.md), §4.13), and of
transition-sensitive RANS. On this page $\alpha$ is the angle of attack
(page-local; the registry's $\alpha$ is the DG/finite-volume blending
factor), $Re_c$ the chord Reynolds number, and $x_{\mathrm{sep}}$,
$x_{\mathrm{tr}}$, $x_{\mathrm{re}}$ the separation, transition and
reattachment points in chords (page-local).

## The workshop case

[Wang et al. (2013)](/sources/wang-2013.md), §4.13, specify case C3.3 of
the first International Workshop on High-Order CFD Methods: the SD7003
wing at $Re_c=6\times10^4$ and $M=0.1$, spanwise periodic over $0.2c$, far
field at 100 chords, wall-to-free-stream temperature ratio 1.002 and a
trailing edge rounded with radius about $0.0004c$, at $\alpha=4^\circ$,
which gives a relatively long bubble, and $\alpha=8^\circ$, which gives a
shorter one. The case is posed for implicit LES, with dynamic subgrid
models also mentioned; the summary shows no results.

## Scale-resolving results at $\alpha=8^\circ$

[Vermeire (2024)](/sources/vermeire-2024.md), §4.3, runs the
shorter-bubble case, $Re_c=6\times10^4$ and $\alpha=8^\circ$, as an
implicit LES with incompressible
[flux reconstruction](/methods/flux-reconstruction.md) (the nodal-DG
variant on Gauss points, Rusanov and BR2 fluxes) and entropically damped
artificial compressibility, an explicit artificial-compressibility
formulation with pressure diffusion (incompressibility factor
$M_{\mathrm{AC}}=0.2$, page-local; not the Mach number $M$), on an
"intentionally coarse" mesh of 57,100 hexahedra: $20c$ upstream and above
and below, $40c$ of wake, span $0.2c$ with 10 elements, periodic in span,
run to $60c/U_\infty$ and averaged over the last $30c/U_\infty$ with paired
explicit Runge–Kutta (Fig. 19). At fixed mesh the polynomial degree $N$
decides the flow (Figs. 20–21, Table 3):

| Run or reference | $C_L$ | $C_D$ | flow on the suction side |
|---|---|---|---|
| $N=1$ | 0.949 | 0.110 | fully separated, no distinct pressure recovery |
| $N=2$ | 1.002 | 0.045 | laminar separation bubble, attached turbulent flow downstream |
| $N=3$ | 0.971 | 0.041 | transition moved upstream |
| $N=4$ | 0.950 | 0.046 | agrees with the references |
| Vermeire et al. (FR, $N=4$, Mach 0.2) | 0.941 | 0.049 | reference |
| Garmann et al. (sixth-order finite differences, Mach 0.1) | 0.969 | 0.039 | reference |
| Beck et al. (DG, $N=7$, Mach 0.1) | 0.932 | 0.050 | reference |

The author concludes that $N=4$ "shows good agreement while requiring
significantly fewer degrees of freedom" than the references (§4.3), and,
with the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and the
channel of the same paper, that the framework suits implicit LES with
$N\le4$ (§5); the references are described further on the
[DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md)
and [spectral difference](/methods/spectral-difference-method.md) pages.
The implicit LES of Galbraith & Visbal used as the reference of the RANS
study below gives, at the same conditions, $x_{\mathrm{sep}}=0.04$,
$x_{\mathrm{tr}}=0.18$, $x_{\mathrm{re}}=0.28$, $C_L=0.92$, $C_D=0.043$
([Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md),
Table 6). Across the four references printed by the two sources $C_L$
spans 0.92 to 0.969 and $C_D$ 0.039 to 0.050 *(compiler check, not in the
sources)*.

### Implicit finite-volume LES on unstructured meshes

[Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md), §5.2, run the
same incidence, $Re_c=6\times10^4$ and $\alpha=8^\circ$, at $M=0.2$ as an
implicit LES with the high-order finite-volume
[CWENOZ reconstruction](/methods/weno-scheme.md) of UCNS3D on two hybrid
hexahedral/prismatic meshes, span $0.2c$ periodic and the domain extending $50c$ up- and downstream:
mesh A of 5.3 million cells (wall spacings $y^+=0.87$, $x^+=3.1$,
$z^+=5.4$) and mesh B of 12.3 million cells ($0.87$, $0.9$, $4.0$). All
runs use a Roe flux, the low-Mach correction of Simmonds et al. and
second-order implicit dual-time stepping with $\Delta t=t_c/500$, averaged
over $20t_c$ after a transient of $20t_c$. The fourth-order CWENOZ4, with
and without the authors' a priori, cell-by-cell
[dissipation–dispersion adjustment](/properties/numerical-dissipation.md)
(ADDA), is set against a second-order MUSCL scheme with the Barth–Jespersen
limiter on both meshes (Table 4; $x_{\mathrm{sep}}$ and $x_{\mathrm{re}}$
in chords):

| Run or reference | $C_L$ | $C_D$ | $x_{\mathrm{sep}}$ | $x_{\mathrm{re}}$ |
|---|---|---|---|---|
| MUSCL2, mesh A | 0.918 | 0.050 | 0.026 | 0.26 |
| MUSCL2, mesh B | 0.933 | 0.041 | 0.023 | 0.23 |
| CWENOZ4, mesh A | 0.926 | 0.044 | 0.039 | 0.28 |
| CWENOZ4-ADDA, mesh A | 0.927 | 0.045 | 0.041 | 0.27 |
| reference [12] (DGSEM), as printed by Tsoutsanis & Nogueira | 0.923 | 0.045 | 0.027 | 0.310 |
| Galbraith & Visbal (FDLI3D), as printed by Tsoutsanis & Nogueira | 0.917 | 0.044 | 0.031 | 0.303 |

CWENOZ4 on the coarser mesh A agrees better with the PyFR, STAR-CCM+,
DGSEM and FDLI3D references in $C_p$ and $C_f$ than MUSCL2 does even on
mesh B, and ADDA improves $C_f$ further (Fig. 19). The authors judge
second-order MUSCL "unsuitable for iLES simulations at under-resolved grid
settings, due to their excessive dissipation characteristics", since its
skin friction, separation and reattachment move unpredictably from mesh A
to mesh B (§5.2). The ADDA indicator selects low dissipation in the
bubble, switches to high-dissipation-dominant settings in the turbulent
region after transition and returns to low dissipation further downstream
(Fig. 18).

## Transitional RANS from $Re_c=23{,}000$ to 200,000

[Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) use the
airfoil as the main test of the $\gamma$-$Re_\theta$
[local-correlation-based transition model](/methods/local-correlation-based-transition-model.md)
with [$k$-$\omega$ SST](/methods/k-omega-sst-model.md), in two-dimensional
compressible RANS and URANS (STAR-CCM+, second-order Roe flux, polyhedral
mesh with a prism layer at $y^+<1$ and adaptive refinement; medium grid of
69,834 cells, grid-converged against 167,084; free-stream $Tu=0.03\%$ and
viscosity ratio 1; §3.3–3.4, Tables 1–4). At $Re_c=6\times10^4$ they take
three references: the implicit LES of Galbraith & Visbal, the PIV of Ol et
al. and the DNS of Carton de Wiart & Hillewaert, the latter at $\alpha=4^\circ$
with $x_{\mathrm{sep}}=0.209$, $x_{\mathrm{re}}=0.654$, $C_L=0.602$,
$C_D=0.0196$ (§3.5, Table 5). Their findings at $Re_c=6\times10^4$
(§3.5, §4, Tables 5–10):

| $\alpha$ | setting | $x_{\mathrm{sep}}$ | $x_{\mathrm{tr}}$ | $x_{\mathrm{re}}$ | $C_L$ | $C_D$ |
|---|---|---|---|---|---|---|
| 4° | Langtry–Menter calibration | 0.202 | 0.518 | 0.660 | 0.600 | 0.0221 |
| 4° | Suluksna–Juntasaro (default), $s_1=2$ | 0.184 | 0.530 | 0.743 | 0.600 | 0.0257 |
| 4° | Suluksna–Juntasaro, $s_1=6$ | 0.202 | 0.536 | 0.680 | 0.593 | 0.0228 |
| 4° | implicit LES (Galbraith & Visbal) | 0.23 | 0.55 | 0.65 | 0.59 | 0.021 |
| 6° | Langtry–Menter calibration | 0.098 | 0.317 | 0.44 | 0.767 | 0.0287 |
| 6° | implicit LES | 0.11 | 0.34 | 0.45 | 0.748 | 0.0319 |
| 8° | Langtry–Menter calibration | 0.035 | 0.158 | 0.280 | 0.922 | 0.0409 |
| 8° | Suluksna–Juntasaro | 0.037 | 0.178 | no reattachment | 0.868 | 0.0557 |
| 8° | implicit LES | 0.04 | 0.18 | 0.28 | 0.92 | 0.043 |

($x_{\mathrm{tr}}$ is where the skin friction starts to drop, §3.5.) The
model gives too low a skin friction after reattachment, which leads to
premature stall, and too early a transition and reattachment at
$6^\circ$–$8^\circ$; no single $s_1$ fits all incidences (§4, Fig. 8). At
$Re_c=3\times10^4$, $\alpha=8^\circ$ neither calibration reattaches, while
the LES reattaches at 0.53 (Table 7). At $Re_c=23{,}000$, $\alpha=2^\circ$
the steady solution misses trailing-edge shedding and URANS raises the
mean lift by 22.80% (0.193 to 0.237) and the drag by 3.66% (§5, Table 11);
the two-dimensional model captures the s-shaped lift curve at that
Reynolds number (Fig. 17), and at $Re_c=2\times10^5$ its lift and drag
agree "excellent[ly]" with the UIUC experiments, the trailing-edge bubble
moving upstream as $\alpha$ grows (§6.1, Figs. 15–16). Detail on the
calibrations and the separation-induced intermittency is on the
transition-model page; the bubble physics is on
[laminar separation bubble](/definitions/laminar-separation-bubble.md).

## What the case shows

- The bubble is decided by resolved dissipation as much as by modelling:
  in the implicit LES of Vermeire (2024) the polynomial degree at fixed
  mesh moves the flow from fully separated ($N=1$) to a bubble with
  turbulent reattachment ($N\ge2$), and in the RANS of Carreño Ruiz &
  D'Ambrosio (2022) the calibration of the separation-induced
  intermittency moves reattachment from 0.660 to 0.769 at $\alpha=4^\circ$
  (Table 8).
- Both sources use scale-resolving simulations as the reference at
  $Re_c=6\times10^4$; experiments enter as PIV (Carreño Ruiz &
  D'Ambrosio) and at $Re_c=2\times10^5$.
- In the finite-volume implicit LES the convective scheme moves the
  bubble: on the same mesh A, CWENOZ4 and MUSCL2 give separation at 0.039
  and 0.026 and reattachment at 0.28 and 0.26, and the authors ascribe the
  unsuitability of MUSCL2 to "excessive dissipation characteristics"
  ([Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md), §5.2,
  Table 4).

## Qualifications

- Vermeire (2024) prints the force coefficients as
  $C_L=L/(2\rho_\infty u_\infty^2)$, $C_D=D/(2\rho_\infty u_\infty^2)$
  (Eqs. 23–24) without a reference area and calls $L$ and $D$
  "coefficients"; the conclusions (§5) say the coefficients "converged to
  reference DNS data", while §4.3 calls the references "high-order
  compressible simulations"; the incompressibility factor is called a
  "compressibility factor" in §4.3.
- The value 0.2 of Vermeire (2024) is the incompressibility factor
  $M_{\mathrm{AC}}$ of an incompressible formulation, not a Mach number;
  the workshop case (Wang et al. (2013), §4.13) and the references of
  Garmann et al. and Beck et al. are at Mach 0.1, the author's earlier FR
  reference at Mach 0.2 (Vermeire (2024), §4.3).
- Carreño Ruiz & D'Ambrosio (2022) print a grid-study row (Table 3:
  0.181, 0.741, $C_L=0.6020$, $C_D=0.02585$) that differs from their
  Langtry–Menter row for the same case (Table 5) without naming the
  calibration of the grid study, and write in the conclusions that the LES
  fails to reattach at $Re_c=3\times10^4$, while their Table 7 gives the LES
  reattachment at 0.53. Their RANS is two-dimensional.
- [Wang et al. (2013)](/sources/wang-2013.md) specify the case only.
- The references are printed with different values by different sources.
  For Galbraith & Visbal at $\alpha=8^\circ$, Carreño Ruiz & D'Ambrosio
  (2022), Table 6, print $x_{\mathrm{sep}}=0.04$, $x_{\mathrm{re}}=0.28$,
  $C_L=0.92$, $C_D=0.043$; Tsoutsanis & Nogueira (2025), Table 4, print
  0.031, 0.303, 0.917, 0.044. For the DGSEM reference, Vermeire (2024),
  Table 3, prints "Beck et al. (DG, $N=7$)" with $C_L=0.932$,
  $C_D=0.050$; Tsoutsanis & Nogueira (2025) cite their ref. [12], whose
  first author is Beck, as "Frank et al." throughout and print 0.923 and
  0.045 without naming the run, polynomial degree or Mach number of the
  reference. In the bibliography both cite Beck et al. (2014); for
  Galbraith & Visbal, Carreño Ruiz & D'Ambrosio cite the 2010 AIAA paper
  and Tsoutsanis & Nogueira the 2008 one.
- Tsoutsanis & Nogueira (2025), §5.2, write that "marginal differences are
  noticed in the separation location and reattachment between all
  predictions", while their Table 4 gives CWENOZ4 separation at
  0.039–0.041 against 0.027–0.031 for the references and reattachment at
  0.27–0.28 against 0.303–0.310.

# Citations

- [Vermeire (2024)](/sources/vermeire-2024.md) — §4.3, Eqs. 22–24, Table 3, Figs. 19–21; §5.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §3.3–3.5, Tables 1–8, Figs. 4–7; §4, Tables 9–10, Figs. 8–10; §5, Table 11; §6.1, Figs. 15–17; §7.
- [Wang et al. (2013)](/sources/wang-2013.md) — §4.13 (case C3.3; specification only).
- [Tsoutsanis & Nogueira (2025)](/sources/tsoutsanis-2025.md) — §5.2, Table 4, Figs. 18–19.
