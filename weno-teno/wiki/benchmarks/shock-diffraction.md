---
type: Benchmark
title: "Shock diffraction"
description: "Shock-diffraction benchmarks: the 2D Mach 5.09 corner problem, its relativistic counterpart and a Mach 10 step variant, testing positivity preservation in the near-vacuum expansion behind the corner; 3D diffraction by a sphere, an adaptive-mesh GPU scaling test; and Schardin's weak shock over a wedge, and a cone in 3D, checking hybrid schemes and immersed boundaries."
status: established
aliases: [shock diffraction problem, shock diffraction at a corner, shock diffraction around a backward-facing step, Mach 5.09 shock diffraction, Mach 10 shock reflection and diffraction]
tags: [benchmark, positivity, bound-preserving, dg, relativistic, gpu]
timestamp: 2026-10-24T05:58:00Z
---

# Shock diffraction

A planar shock of Mach number $5.09$ runs to the right along a channel
of height 5 and leaves it at a backward-facing corner, where the
channel opens downwards into a much larger box. The shock diffracts
around the corner, and the gas expanding behind it reaches very low
density and pressure next to the vertical wall below the corner. The
problem has no exact solution; the sources read it as a robustness
test: a scheme must keep density and pressure positive in the
expansion and stay free of oscillations at the strong shock, and the
contours of density and pressure at $t=2.3$ are compared visually.
Five sources of the bundle run it, four in the Euler form (one on a
rescaled geometry) and one in a relativistic form; two, one of them
already counted, run a Mach 10 variant in which the double-Mach-reflection shock meets a
backward step, one runs the three-dimensional diffraction of a
strong shock by a sphere, five the diffraction of a weak shock by a
triangular wedge (Schardin's problem), and one its three-dimensional
counterpart on a cone.

## Setup

[Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.7 and
[Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.4 print the same
data, with $\gamma=1.4$:

- domain $[0,1]\times[6,11]\cup[1,13]\times[0,11]$: the channel
  $0\le x\le1$, $6\le y\le11$ opens at the corner $(1,6)$ into the box
  $1\le x\le13$, $0\le y\le11$;
- a right-moving shock of Mach number $5.09$ initially at $x=0.5$,
  $6\le y\le11$, moving into air at rest with $\rho=1.4$, $p=1$;
- inflow at $x=0$, $6\le y\le11$; outflow at $x=13$ and at $y=0$,
  $1\le x\le13$; reflecting walls on $0\le x\le1$, $y=6$ and on $x=1$,
  $0\le y\le6$;
- final time $t=2.3$; 20 density contours from 0.066227 to 7.0668 and
  40 pressure contours from 0.091 to 37 (Du et al. on triangles, Fan,
  Zhang & Qiu 2021).

[Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.6, the
finite-difference companion of Fan et al. (2021), prints the same data,
outflow at $y=11$, $\Delta x=\Delta y=1/64$, $\mathrm{Re}=1000$ and
$\infty$, and the same 20 density contours (Fig. 5.5).

The top boundary differs: Fan et al. (2021, 2022) state outflow on $y=11$,
$0\le x\le13$; Du et al. impose the exact motion of the shock there.

### Rescaled corner of Hu, Yuan & Zhao

[Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.12 run a Mach 5.09
normal shock around a $90^\circ$ corner at $(0.05,0.6)$ in $[0,1]^2$ on
$400\times400$ cells: quiescent $(\rho,v_1,v_2,p)=(1.4,0,0,1)$, the
Rankine–Hugoniot post-shock state at the inlet above the corner,
reflecting bottom and left boundary below the corner, zero gradient on
the right, a shock-following top boundary, CFL 0.5, $t=0.15$; they cite
no origin for the test.

The pre-shock state has sound speed $c=\sqrt{1.4\cdot1/1.4}=1$, so the
shock moves at speed $5.09$, and the Rankine–Hugoniot conditions give
the post-shock state
$\rho=1.4\cdot\frac{(\gamma+1)M^2}{(\gamma-1)M^2+2}=7.041$,
$v_1=\frac{2c}{\gamma+1}\big(M-\frac1M\big)=4.078$,
$p=1+\frac{2\gamma}{\gamma+1}(M^2-1)=30.06$ with $M=5.09$ *(compiler
check, not in the sources)*. Hu et al. do not print this state.

### Relativistic version

[Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.11 (arXiv v1) run a
[relativistic](/definitions/relativistic-hydrodynamics.md) shock
diffraction at a corner: a shock with speed $0.8$ along $x=3.4$,
$6\le y\le11$, pre-shock $\rho=1.4$, $p=1$ at rest, post-shock
$(\rho,v_1,v_2,p)=(2.58962919872684,\ 0.40445979062926,\ 0,\ 2.865544850466692)$;
reflecting walls on the corner, inflow on $x=0$, $6\le y\le11$, outflow
elsewhere, $t=8$. The paper states no $\gamma$ for the example, whose
default is $5/3$: with $\gamma=5/3$ the printed post-shock state
satisfies the relativistic Rankine–Hugoniot conditions of a shock of
speed 0.8 against the pre-shock state to round-off, while with
$\gamma=1.4$ the momentum and energy jumps fail by about 0.55
*(compiler check, not in the sources)*.

### Mach 10 reflection and diffraction over a step

[Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.8 and
[Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.12 run the
[double Mach reflection](/benchmarks/double-mach-reflection.md) shock
over a wall that ends in a backward step, so that the reflected
structure then diffracts downwards. As printed by Fan et al. (2023):
$\gamma=1.4$, left state
$(\rho,v_1,v_2,p)=(8,\ \tfrac{33}{4}\sin\tfrac\pi3,\ -\tfrac{33}{4}\cos\tfrac\pi3,\ 116.5)$
for $x<\tfrac16+y/\sqrt3$, $(1.4,0,0,1)$ elsewhere; reflecting walls on
$\tfrac16\le x\le1$, $y=0$ and on $x=1$, $-1\le y\le0$; the exact
post-shock state on $0\le x\le\tfrac16$, $y=0$; the exact moving shock on
the top boundary for $0\le x\le\tfrac16+(1+20t)/\sqrt3$; inflow on the
left, outflow on the right and bottom; $t=0.2$. The left state is the
double-Mach post-shock state, $8.25\sin(\pi/3)=7.1447$,
$8.25\cos(\pi/3)=4.125$ *(compiler check, not in the sources)*, and
Fan et al. (2022) state that the reflection part is "exactly the same
as" double Mach reflection.

| Source | Scheme | Mesh | Positivity treatment |
|---|---|---|---|
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.8 | finite-difference WENO-JS5, JS7, ZQ5, Euler and Navier–Stokes ($\mathrm{Re}=1000$); 50 density contours 0–25 | $\Delta x=\Delta y=1/480$ | positivity-preserving Navier–Stokes flux and scaling limiter, active on 0.0017 %, 0.0016 %, 0.0034 % of the cells ($\mathrm{Re}=\infty$) and 0.0002 %, 0.0001 %, 0.0009 % ($\mathrm{Re}=1000$) |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.12 | finite-difference HWENO-R, HWENO-L, WENO-ZQ | $960\times320$ | parametrized PP flux limiter, needed by HWENO-R and WENO-ZQ, active on 0.0012 % of the cells |

At $\mathrm{Re}=1000$ the Kelvin–Helmholtz fine structure of the slip
line is smeared by numerical plus physical viscosity, but Fan et al.
(2022) find that the positivity treatment adds no excessive numerical
viscosity, and WENO-ZQ5 the least dissipative of their three schemes
(Fig. 5.7). Fan et al. (2023) report the HWENO-R run at 12902.85 s,
about 1.50 times WENO-ZQ, in Fortran 95 on an Intel Xeon Gold 6130.

Both papers print the domain as the union of $[0,1]\times[0,1]$ and
$[-1,1]\times[1,3]$. The wall $x=1$, $-1\le y\le0$ lies outside that
union; the boundary data and the plotted axes of Fan et al. (2023)
($x\in[0,3]$, $y\in[-1,1]$) fit $[0,1]\times[0,1]\cup[1,3]\times[-1,1]$,
i.e. the intervals of the second block are swapped in print.

### Three-dimensional diffraction by a sphere

[Zaghi et al. (2023)](/sources/zaghi-2023.md) §3, after the experiment
of Bryson & Gross (1961), diffract a planar shock by a sphere centred
at $(10,10,10)$ in a cube of side 20 (non-dimensional; the radius is
not stated in the text), with the compressible Navier–Stokes equations
for air: pre-shock $(\rho,p)=(1.4,1)$ at rest, post-shock
$\rho=5.1432014$, $p=9.0454500$, $v=(2.0451168,0,0)$, imposed as
supersonic inflow on the left, extrapolation elsewhere; fluid
properties $c_p=1005.2$, $c_v=718.0$, viscosity $\mu=0.0013485123$ (page-local) (Fig. 4b); the
initial shock position is not stated; measurements at $t=5$,
figures at $t=4$ and $6$; refinement on the modulus of the density
gradient, between levels 3 and 8. The text states a shock Mach number
of 2.89; with $\gamma=1.4$ and pre-shock sound speed 1, the
Rankine–Hugoniot state at Mach 2.89 is $\rho=5.2544$, $p=9.5775$,
$v_1=2.1200$, whereas the printed state is reproduced to all printed
digits at Mach 2.81 ($\rho=5.1432014$, $p=9.04545$, $v_1=2.045107$)
*(compiler check, not in the sources)*: the computed shock is about
Mach 2.81.

### Diffraction by a wedge: Schardin's problem

[Maltsev et al. (2023)](/sources/maltsev-2023.md) §3.5 compute a
triangular wedge hit by a normal shock of Mach 1.34 moving left to
right, in a domain of the dimensions of Schardin's experiment, with the
Euler equations, $\gamma=1.4$, gas constant $R=287$ J/(kg K) (page-local): pre-shock $p=101325$
Pa, $T=288.15$ K, at rest; post-shock $p=195557.25$ Pa, $T=350.5$ K,
$v_1=168.62$ m/s (their Table 2). Walls of wedge, top and bottom are
reflective, left and right boundaries non-reflecting; about 340,000
mixed quadrilaterals and triangles with edge size $h=0.01$ mm near the
wedge; SSP-RK3 at CFL 0.3; the run starts when the shock meets the
wedge and stops at $t=200$ ms as printed. They compare a pure
finite-volume CWENOZ5 scheme with their hybrid DG($\mathbb P^3$)–FV(CWENOZ4)
and DG($\mathbb P^4$)–FV(CWENOZ5) schemes in [UCNS3D](/software/ucns3d.md), with
a relaxed MOOD-type [troubled-cell](/definitions/troubled-cell-indicator.md)
switch.

[Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.7, Eq. (44) run a
dimensionless Schardin problem, with initial data taken from an earlier
paper they cite: on $[-2,6]\times[-3,3]$, a wedge of unit length and
height with its tip at the origin, symmetry top and bottom, inflow and
outflow left and right, $(\rho,v_1,v_2,p)=(2.122,0.442,0,1.805)$ for
$x<-1$ and $(1.4,0,0,1)$ for $x\ge-1$, on 403,660 triangles
($h\approx3/275$), with their dual-stencil-selection unstructured TENO
of orders 4 to 7 in [UCNS3D](/software/ucns3d.md), outputs at $t=2.1$
and $4.0$. The pre-shock state has unit sound speed, and the printed
post-shock state is the Rankine–Hugoniot state of a Mach 1.3 shock
into it to the printed digits ($\rho=2.12197$, $p=1.805$,
$v_1=0.44231$) *(compiler check, not in the sources)*.

[Liang et al. (2025)](/sources/liang-2025.md) §4.6, Eq. (38) and
[Chen & Chen (2026)](/sources/chen-2026.md) §3.2, the latter after Liang &
Fu as they cite it, run the same post-shock state with the shock at the
wedge tip: $(\rho,v_1,v_2,p)=(2.122,0.442,0,1.805)$ for $x<0$ and
$(1.4,0,0,1)$ for $x\ge0$, on $[-5,13]\times[-5,5]$ with the wedge tip at
the origin, Euler (slip) walls top and bottom, inflow and outflow left and
right, schlieren $e^{-10\lvert\nabla\rho\rvert/\max\lvert\nabla\rho\rvert}$.
Liang et al. (2025) run TENO5-E to TENO7-E and CWENO5 to CWENO7 in
[UCNS3D](/software/ucns3d.md) on a multi-resolution triangular mesh of
about 1,627,638 elements ($h\approx0.004$ in the wake region, 0.015 and
0.06 farther out) at CFL 0.6 to $t=4.0$ (Figs. 17–18, Table 4). Chen &
Chen compute the wedge as a sharp-interface
[immersed boundary](/methods/immersed-boundary-method.md) (adiabatic
slip) on a uniform Cartesian $6000\times3000$ grid ($h\approx0.003$), with
their positivity-preserving finite-difference
[adaptive TENO](/methods/adaptive-teno.md), against WENO-Z with the
same immersed boundary, outputs at $t=3.09$ and $4.26$ (Figs. 10–13).

**A cone in three dimensions.** Liang et al. (2025) §4.8 run the 3D
counterpart: the post-shock state of Eq. (38), a right-moving Mach 1.3
shock at the tip of a half cone of length 2 and foot radius 1 (tip at the
origin) inside a half cylinder of radius 4.5, $x\in[-3,8]$, solid walls on
the cone and the cylinder mantle, 2,495,825 tetrahedra, CFL 0.6, TENO6-E
only, troubled cells shown at $t=1.0$ and $4.0$ (Figs. 21–23).

[Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.7 run Schardin's
problem on triangles with their finite-volume ALW-MR-WENO of orders 3
to 5 and the MR-WENO of the same group: domain $[0,3]\times[0,1.5]$, a
Mach 1.34 shock passing "half an equilateral triangle", inflow on the
left and reflection elsewhere, boundary mesh size $1/160$, $t=1.46$,
CFL 0.6, 30 density contours from 0.5 to 2.9 (Figs. 3.8–3.10). They
print the states $(2.21953028430161,\,1.09817058096415,\,0.0,\,1.79567311218210)$
for $x\le1$ and $(1.4,0,0,1)$ for $x>1$ under the heading
$(\rho,v_1,v_2,p)$. For a Mach 1.34 shock into $(\rho,p)=(1.4,1)$ with
$\gamma=1.4$ the Rankine–Hugoniot state is $\rho=2.2195302843$,
$v_1=0.49478$, $\rho v_1=1.0981705810$, $p=1.9282$, $E=5.0922$: the first
two printed entries are $\rho$ and the momentum $\rho v_1$ to all
printed digits, while the fourth matches neither $p$ nor $E$ *(compiler
check, not in the sources)*. The paper prints no $\gamma$.

## Runs in the sources

| Source | Scheme | Mesh | Notes |
|---|---|---|---|
| [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) Ex. 4.7 | positivity-preserving hybrid [HWENO](/methods/hermite-weno.md), finite volume, cubic reconstruction, SSP-RK3; Euler and Navier–Stokes ($\mathrm{Re}=1000$, $\mathrm{Pr}=0.72$) | $\Delta x=\Delta y=1/32$ | time step with page-local constants $a=1/12$, $b=0.001$ as in their whole paper |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.4 | RKDG $\mathbb P^1$, $\mathbb P^2$ with the improved vs the original [simple WENO limiter](/methods/weno-limiter-dg.md), KXRCF threshold $C_k=0.01$, SSP-RK3 | triangles, $h=1/16$ | CFL 0.3 ($\mathbb P^1$), 0.18 ($\mathbb P^2$) |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.10 | as above, DG on polygonal cells from random point clouds | 219,200 ($\mathbb P^1$) and 493,200 ($\mathbb P^2$) points | positivity-preserving limiter for $\mathbb P^2$; 20 density contours 0.066227–7.1 |
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.6 | finite-difference WENO-JS5, JS7, ZQ5 with the [positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md); Euler and $\mathrm{Re}=1000$ | $\Delta x=\Delta y=1/64$ | $T=2.3$ |
| [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.12 | second-order MUSCL, TVD RK2; HLLC, HLLEM and the shock-stable RHLLEM-LD | $400\times400$ on the rescaled corner | CFL 0.5, $t=0.15$ |
| [Zaghi et al. (2023)](/sources/zaghi-2023.md) §3 | conservative finite differences with WENO reconstruction, Rusanov flux-vector splitting, SSP-RK3, [immersed boundary](/methods/immersed-boundary-method.md) by pseudo-time normal extrapolation, block-octree [AMR](/methods/adaptive-mesh-refinement.md) in [ADAM](/software/adam.md) on V100 GPUs | 3.6 M cells (strong scaling) to 350.3 M cells (684,258 blocks) | WENO order not stated for this case; 3D Navier–Stokes |
| [Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.11 | third-order finite-volume WENO on triangles with a physical-constraint-preserving limiter and HLL flux, vs first-order HLL | $h=1/40$; first order also $h=1/160$ | relativistic; CFL 0.5 |

## Findings across sources

**Positivity behind the corner.** Fan, Zhang & Qiu (2021) use the
problem to show
robustness in the low-density, low-pressure region behind the corner.
Their scaling positivity limiter is triggered in only 0.23 % of the
cells, identically for the hybrid and non-hybrid schemes and for both
Reynolds numbers, and they state that the earlier hybrid HWENO of Zhao,
Chen & Qiu blows up on this problem from loss of positivity, without a
figure (§1, §4, Fig. 4.7, Table 4.2). Du et al. switch on a
positivity-preserving limiter for their $\mathbb P^2$ runs on point clouds; on
triangles no positivity limiter is mentioned. See
[bound preservation](/properties/bound-preservation.md) and the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md).

Fan, Zhang & Qiu (2022) state that without their positivity flux and
limiter all three WENO schemes blow up (§5); the limiter acts on
0.0024 %, 0.0026 % and 0.0125 % of the cells per step for WENO-JS5,
JS7 and ZQ5 at $\mathrm{Re}=\infty$, and 0.0005 %, 0.0010 % and
0.0079 % at $\mathrm{Re}=1000$ (Example 5.6).

**Shock stability.** Hu, Yuan & Zhao use the corner as one of their
tests of the [carbuncle phenomenon](/definitions/carbuncle-phenomenon.md):
HLLC and HLLEM, "especially the latter", show shock instabilities, and
their RHLLEM-LD, which damps the anti-diffusion of HLLEM near shocks,
does not; see [HLL-family solvers](/methods/hll-riemann-solvers.md).

**Limiters and troubled cells.** On triangles Du et al.'s improved
limiter, which combines only two polynomials per edge direction, gives
results "almost identical" to the original limiter; it saves 6.6 %
($\mathbb P^1$) and 11.73 % ($\mathbb P^2$) of the CPU time although it flags more
cells at $\mathbb P^2$ (12.63 % against 9.48 %; Figs. 4.6–4.7, Table 4.8). On
point clouds both limiters give the same quality, more oscillatory than
on triangles, with savings of 9.90 % and 40.91 % (Fig. 4.16,
Table 4.18). Fan, Zhang & Qiu's (2021) hybrid scheme applies its
nonlinear HWENO
reconstruction in 5.07 % (Euler) and 4.39 % (Navier–Stokes) of the
cells, and saves 63.76 % ($\mathrm{Re}=\infty$) and 64.45 %
($\mathrm{Re}=1000$) of the CPU time of the non-hybrid
positivity-preserving scheme, hardware not stated (Table 4.2). See
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

**Third against first order in the relativistic case.** Chen & Wu
compare their third-order scheme at $h=1/40$ with the first-order HLL
scheme at $h=1/40$ and $h=1/160$ (Fig. 17); the figure is the evidence,
and no error norm is given.

**Adaptive refinement and GPU scaling on the sphere.** Zaghi et al.
use the sphere case to measure their AMR library on Marconi100 (Table 1,
13 runs): with $8^3$-cell blocks on 3.6 M cells the strong scaling is
superlinear up to 8 GPUs (speedup 8.94), about 90 % efficient at 16
(14.23) and below 60 % at 32 (18.84), so each V100 needs more than about
250 K cells; larger blocks ($16^3$, $32^3$) lower the grind time, until
inter-node ghost exchange matters at $32^3$. Raising the fine-to-coarse
resolution ratio from 2 to 32 on 1 to 256 GPUs grows the grid by a
factor 4–5 per halving of the finest spacing instead of 8, up to
350.3 M cells, while the grind time rises less than threefold; the
serial octree update grows to 527.97 s on 684,258 blocks, which they
call acceptable for statistically steady but problematic for transient
runs. The flow field (incident, reflected, diffracted and transmitted
shocks, triple point) agrees qualitatively with a digitized schlieren
photograph of Bryson & Gross, the curved reflected shock being slightly
ahead in the experiment (Fig. 11); they claim the finest resolution
published for this case.

**Hybrid DG–FV against experiment on the wedge.** Maltsev et al. find
the tip vortices, bow shock and contact surfaces between the vortices
and the shock triple point in agreement with the experiment of Chang &
Chang that they cite (Fig. 13); both hybrid variants resolve more
structures and acoustic waves from the shock–vortexlet interactions
than pure FV-CWENOZ5 (Fig. 14), the Mach number along the wedge
symmetry line agrees among the three schemes, and fewer than 0.4 %
($\mathbb P^3$) and 0.2 % ($\mathbb P^4$) of the cells are troubled throughout (Fig. 15).

Lin & Zhu find that ALW-MR-WENO and MR-WENO "can provide good
resolution" with similar results on the wedge (Case 3.7, Figs.
3.8–3.10), the ALW schemes at 0.60–0.96 of the MR-WENO time over their
two-dimensional cases (Table 3.1). No comparison with experiment is
made.

Ji, Liang & Fu (2023) find their seventh-order TENO7-D at $t=2.1$ in
good agreement with the experimental shadowgraph of Van Dyke's album,
plotted as $e^{-\lvert\nabla\rho\rvert}$ with a normalised gradient, and
all orders with similar shock patterns and counter-rotating vortices at
$t=4.0$, without visible oscillations (§4.7, Figs. 16–17).

Chen & Chen find both WENO-Z and their adaptive TENO, each with the
immersed boundary, in agreement with the Chang & Chang experiment at
$t=3.09$ and $4.26$, the adaptive TENO "exhibit[ing] lower numerical
dissipation in resolving the fine structures" (§3.2, Figs. 11–13); its
cut-off $C_T$ adapts in $[10^{-9},10^{-1}]$ ([TENO](/methods/targeted-eno.md)).
Liang et al. (2025)'s TENO-E captures more tip vortices than CWENO of the
same order, and costs less: with CWENO5 as 1.00, total times of 0.56,
0.67 and 0.79 for TENO5-E, TENO6-E and TENO7-E against 1.12 and 1.33 for
CWENO6 and CWENO7, reconstruction times of 0.48, 0.59, 0.72 against 1.14
and 1.38 (Table 4); TENO-E runs the linear reconstruction, without
characteristic decomposition, in cells that a density-jump variance
indicator does not flag ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
On the cone "very few elements are misidentified" by that indicator
outside the shock and the torus vortex (Figs. 22–23).

## Qualifications

- Liang et al. (2025)'s bracketed time ratios are truncated, not
  rounded, to two decimals (e.g. $51096.02/89682.30=0.5697$, printed
  0.56) *(compiler check, not in the sources)*; their timings come from
  one unspecified workstation.
- The Mach 1.3 post-shock state of Liang et al. (2025) and Chen & Chen
  is Ji, Liang & Fu's; the three differ in the initial shock position
  (at the tip against $x=-1$), the domain and the wedge size, which
  Liang et al. (2025) and Chen & Chen give only in figures.

- Evidence is visual throughout; no source reports a reference
  solution or an error norm. Maltsev et al. compare with experimental
  flow visualization.
- Maltsev et al. name the pure FV variant FV(CWENOZ5) in the text and
  Fig. 14 and FV(CWENOZ4) in the caption of Fig. 15.
- Zaghi et al.'s Table 1 labels the grind time "[s]" while the printed
  values (0.28 for $1.019$ s per step on $3.6\times10^6$ cells and one GPU)
  are in microseconds per cell update; their "8 billions" cells for
  uniform refinement of the cube at the finest spacing $0.015625$ is
  $1280^3\approx2.1\times10^9$ *(compiler check, not in the sources)*.
  The sphere problem is three-dimensional and viscous, unlike the 2D
  Euler corner problems above.
- Hu, Yuan & Zhao's corner ($[0,1]^2$, corner at $(0.05,0.6)$, $t=0.15$)
  is a different geometry from the $[0,13]\times[0,11]$ problem; their
  contours are not comparable with the others'.
- Fan, Zhang & Qiu (2021, 2022) and Du et al. differ in the top
  boundary condition (outflow against the exact shock motion) and in
  the discretization family (finite volume or finite difference on a
  Cartesian grid against DG on triangles and polygons), so their
  contour plots are not directly comparable.
- Chen & Wu do not describe the corner geometry beyond "wedge walls",
  and give no $\gamma$ for the example (see the relativistic setup).

# Citations

- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §4, Ex. 4.7, Fig. 4.7, Table 4.2.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §4.2; Ex. 4.4, Figs. 4.5–4.7, Table 4.8; Ex. 4.10, Fig. 4.16, Table 4.18.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.11, Fig. 17 (arXiv v1).
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Examples 5.6 and 5.8, Figs. 5.5, 5.7.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.12, Remark 3.2.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.12.
- [Zaghi et al. (2023)](/sources/zaghi-2023.md) — §3, §3.2–3.3, Table 1, Figs. 4–15.
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3, Case 3.7, Figs. 3.8–3.10, Table 3.1.
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §3.5, Table 2, Figs. 12–15.
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.7, Eq. (44), Figs. 16–17.
- [Liang et al. (2025)](/sources/liang-2025.md) — §§4.6, 4.8, Eq. (38), Table 4, Figs. 17–18, 21–23.
- [Chen & Chen (2026)](/sources/chen-2026.md) — §2.3.2, §3.2, Figs. 10–13.
