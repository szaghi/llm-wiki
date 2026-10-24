---
type: Benchmark
title: "Mach 3 forward-facing step"
description: "Two-dimensional Euler benchmark of Mach 3 flow in a wind tunnel with a step, run to t=4 or to a steady state; it tests robustness at the expansion corner, the resolution of the Kelvin–Helmholtz roll-up of the vortex sheet from the triple point, shock stability of Riemann solvers and steady-state convergence of WENO residuals."
status: established
aliases: [forward-facing step, wind tunnel with a step, Mach 3 wind tunnel]
tags: [benchmark, low-dissipation, weno]
timestamp: 2026-10-23T20:39:00Z
---

# Mach 3 forward-facing step

A uniform Mach 3 flow of ideal gas enters a wind tunnel of unit height
containing a step of height $0.2$ whose corner sits at $(0.6,0.2)$. A bow
shock forms ahead of the step, reflects from the upper wall and the step
top, and a triple point forms on the upper wall from which a vortex
sheet trails downstream. The expansion corner of the step is a
singularity that strains robustness, and the vortex sheet is
Kelvin–Helmholtz unstable, so the benchmark measures both whether a
scheme survives and how much small-scale structure it resolves.
Twenty-four sources of the bundle run it, seven of them on triangles (one of these
in a relativistic version), one on polygons and one as a steady-state
problem; those
that name an origin attribute it to Woodward & Colella.

## Setup

[Balsara et al. (2024)](/sources/balsara-2024.md) §IX.g and
[Li et al. (2022b)](/sources/li-2022-b.md) §4.4.3 print the same data:
domain $[0,3]\times[0,1]$, step corner at $(0.6,0.2)$, Mach 3 inflow
with $\rho=1.4$, $p=1$, $\gamma=1.4$, final time $t=4$. The sound speed
of that state is $c=\sqrt{1.4\cdot1/1.4}=1$, so the inflow velocity is
$(v_1,v_2)=(3,0)$ *(compiler check, not in the sources)*.
Walls are reflecting, the left boundary is inflow and the right one
outflow. Balsara et al. treat the corner singularity "in the same manner
as Woodward and Colella"; Li et al. do not mention a corner
treatment. [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.4 refer the
setup to Woodward & Colella without reprinting it and run to $t=4$.
[Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.10 and
[Wang et al. (2021)](/sources/wang-2021.md) Example 5.8 print the
tunnel ($3\times1$, step of height 0.2 at $x=0.6$) and $t=4$, and both
plot 30 density contours from 0.32 to 6.15, as do
[Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.5, who describe a
right-moving Mach 3 initial flow in the same tunnel with reflecting
walls and inflow/outflow boundaries and no corner treatment beyond
local mesh refinement. [Yu & Hesthaven (2022)](/sources/yu-2022.md)
§5.4.5 run the Mach 3 step to $t=3$ on fully unstructured triangles,
without special treatment of the corner, and compare with Chaudhuri et
al.

[Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.11 and
[Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.7 print the
same data in $(\rho,v_1,v_2,p)$, $(1.4,3,0,1)$, in
$[0,3]\times[0,1]$ with the step $[0.6,3]\times[0,0.2]$; Hu et al.
impose inflow on the left, zero gradient on the right and reflecting
walls, to $t=4$, citing Woodward & Colella; Mossier et al. run the
domain as one element thick in $z$ with periodic $z$ boundaries and
print no final time. [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md)
Ex. 3.9 describe a right-going Mach 3 flow, reflecting walls, inflow
and outflow, $t=4$, and 30 density contours from 0.32 to 6.15, on a
domain printed as $[0,0.6]\times[0,1]\cup[0.6,1]\times[0.2,1]$ (checked
on the PDF page), a tunnel of length 1 rather than 3. Their
$960\times320$ mesh gives square cells only for a tunnel of length 3,
and the contour levels are those of the length-3 runs above, so the
mesh and the contours fit a tunnel of length 3, not the printed upper
bound 1 *(compiler check, not in the sources)*.
[Fan et al. (2025a)](/sources/fan-2025.md) Ex. 3.11, from the same group,
print the same domain, Mach 3 inflow, $t=4$ and $960\times320$ mesh,
with the same mismatch between the printed length 1 and the 3:1 mesh.
[Vilar & Abgrall (2024)](/sources/vilar-2024.md) §4.3.3 (HAL preprint)
print the tunnel $3\times1$ with a step of height 0.2 at $x=0.6$,
$\gamma=7/5$, $\rho_0=1.4$, $p_0=1$, $v_0=(3,0)$, inflow on the left,
to $t=4$.

[Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 16 print the domain
as $[0,0.6]\times[0,1]\cup[0.6,3]\times[0.2,1]$ with $(1.4,3.0,0,1.0)$,
inflow/outflow and reflective walls, to $t=4$.
[Liu et al. (2023b)](/sources/liu-2023-b.md) §5.3 print
$[0,3]\times[0,1]$, a step of height 0.2 at $x=0.6$, inflow
$(1.4,3,0,1)$, reflecting top and bottom, $t=4$.
[Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.6 (arXiv v1)
print the domain $[0,3]\times[0,1]\setminus[0.6,3]\times[0,0.2]$ with
inflow $\rho=1$, $v=(3,0)$, $p=1/1.4$, slip walls, no corner fix, to
$t=4$. Their state has sound speed $\sqrt{1.4\cdot(1/1.4)/1}=1$, so it is
the same Mach 3 flow as $(1.4,3,0,1)$ with density and pressure both
divided by 1.4, which changes no velocity and no wave pattern
*(compiler check, not in the sources)*.

[Tang (2024)](/sources/tang-2024.md) §4.4.7, Eq. (40) print
$(1.4,3.0,0,1.0)$ in the fluid region $[0,0.6]\times[0,1]\cup[0.6,3]\times[0.2,1]$,
inflow on the left, outflow on the right, reflective top, bottom and
step face, to $t=4.0$, and set the field inside the step to the
constant $(0.1,0.1,0.1,0.1)$ "with inflow boundaries set in the step",
which the author calls "not physically realistic".
[Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.6 (arXiv v1)
print the domain as $[0,7]\times[0,3]-[0.6,7]\times[0,0.2]$, the Mach 3 flow with $\rho_0=\gamma=1.4$, $p_0=1$, the
left ghost state fixed to the initial data, a supersonic exit and walls
top and bottom, with outputs at $t=2.5$ and $4.0$; with a tunnel height
of 3 the step of height 0.2 is a fifteenth of the height instead of a
fifth, so the printed domain is not the Woodward–Colella tunnel
*(compiler check, not in the sources)*; the text does not say whether
the printed domain is the one that was run.

[Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) Ex. 5.9
(arXiv v3) print $[0,3]\times[0,1]$, a step of height 0.2 from $x=0.6$,
initial $(1.4,3,0,1)$ and $t=4$.
[Huang et al. (2025b)](/sources/huang-2025-b.md) §4.2.5 print a tunnel 1
wide and 3 long with the step at 0.6 from the left, inflow on the left,
zero gradient on the right, reflective walls, $\rho=1.4$, $p=1$, $v_1=3$,
$\gamma=1.4$, $t=4$, and 30-level contours from 0.28 to 6.15; the step
height is not printed. [de Romémont et al. (2026)](/sources/deromemont-2026.md)
§6.3 print $(0,3)\times(0,1)$, $\gamma=1.4$, initial $(1.4,3,0,1)$, a
left inlet, supersonic inflow and outflow and slip walls; neither the
step geometry nor the final time is printed.

**Steady version.** [Wan & Xia (2022)](/sources/wan-2022.md) Ex. 4.5
march the same tunnel ($3\times1$, step of height 0.2 on $[0.6,3]$,
Mach 3 inflow $(1.4,3,0,1)$) to a steady state on $90\times30$ cells,
with the corner fix of Woodward & Colella, and judge schemes by whether
the residual falls to machine zero; at finer grids the flow is not
purely steady because of the slip line.

**Relativistic version.** [Chen & Wu (2022)](/sources/chen-2022-b.md)
Ex. 4.9 (arXiv v1) run the same tunnel and step for the
[relativistic](/definitions/relativistic-hydrodynamics.md) Euler
equations with $\gamma=1.4$ and $\rho=1.4$ at a "Newtonian" Mach number
3, with inflow speeds $v_1=0.9$, $0.99$ and $0.999$ to $t=6$, $4.45$ and
$4$, on 149,436 triangles ($h=1/160$), reflecting walls and no entropy
fix at the corner.

| Source | Scheme | Grid | CFL |
|---|---|---|---|
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.4 | [WENO-Z+M](/methods/weno-z-plus.md) vs WENO-Z, WENO-Z+, WENO-IS-I, WENO-Z7, WENO-Z9 | $481\times161$ | 0.5 |
| [Li et al. (2022b)](/sources/li-2022-b.md) §4.4.3 | seventh-order [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z | $600\times200$ | not restated for 2D |
| [Balsara et al. (2024)](/sources/balsara-2024.md) §IX.g | seventh-order [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md), HLL-based (Fig. 17 caption) | $1440\times480$ | 0.4 |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) Ex. 3.10 | sixth-order moment-based [multi-resolution HWENO](/methods/hermite-weno.md), HLLC: HWENO6 vs HWENO6-M5-I | $600\times200$ | 0.6 |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.8 | [multi-resolution WENO](/methods/multi-resolution-weno.md) (New WENO5, original WENO5-MR) vs WENO-JS5, WENO-AO5 | $1200\times400$ | 0.6 |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) Ex. 4.5 | RKDG $\mathbb P^1$, $\mathbb P^2$ with the improved vs the original [simple WENO limiter](/methods/weno-limiter-dg.md), KXRCF $C_k=0.01$ | triangles, $h=1/400$ near the corner, $1/100$ elsewhere | 0.3 ($\mathbb P^1$), 0.18 ($\mathbb P^2$) |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.5 | nodal DG, ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md) with decay-rate threshold $\mathfrak a_0=2.5$ (page-local) and their min-rule (4.8) | unstructured triangles, $h=1/80$ | — |
| [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.11 | second-order MUSCL, TVD RK2; HLLC, HLLEM and the shock-stable RHLLEM-LD | $720\times240$ | 0.5 |
| [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) §8.7 | [p-adaptive DG with FV-subcell hp shock capturing](/methods/hp-adaptation.md) in [FLEXI](/software/flexi.md), HLLE, density indicator | $180\times60\times1$ minus the $144\times12\times1$ step, $h=1/60$ | — |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.9 | finite-difference [HWENO](/methods/hermite-weno.md): HWENO-R, HWENO-L vs WENO-ZQ | $960\times320$ | — |
| [Wan & Xia (2022)](/sources/wan-2022.md) Ex. 4.5 | steady [hybrid WENO](/methods/hybrid-weno.md) WENO-H vs CWENOZ (WENO-ZQ), MRWENO, WENO-JS | $90\times30$ | — |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 16 | fifth-order FV IMWENO-P (symmetric smoothness indicators) vs WENO-JS, WENO-Z, WENO-NS, WENO-P, MWENO-P; global LF, SSP-RK3 | $900\times300$ | 0.5 |
| [Liu et al. (2023b)](/sources/liu-2023-b.md) §5.3 | implicit fourth-order [RBF differential-quadrature](/methods/rbf-differential-quadrature.md) FV (IRBFDQ-FV), Roe flux, PEEB limiter, vs a second-order FV scheme | 108,543 triangles ($h\approx1/160$ equivalent) | — |
| [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) §4.6 | fourth-order compact [gas-kinetic scheme](/methods/gas-kinetic-scheme.md), no troubled-cell detection | triangles, $h=1/120$ | 0.8 |
| [Chen & Wu (2022)](/sources/chen-2022-b.md) Ex. 4.9 | third-order FV WENO on triangles, physical-constraint-preserving limiter, HLL (relativistic) | triangles, $h=1/160$ | 0.5 |
| [Tang (2024)](/sources/tang-2024.md) §4.4.7 | [TENO-AZ](/methods/adaptive-teno.md) vs TENO-Z, TENO-A, TENO-LAD; finite difference, global LF splitting, TVD-RK3 | $720\times240$ | 0.45 |
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.9 | finite-volume ALW-MR-WENO-3/4/5 on triangles vs [MR-WENO](/methods/multi-resolution-weno.md), characteristic-wise | triangles, boundary mesh size 1/160; $t=4$; 30 contours 0.32–6.15 | 0.6 |
| [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) Ex. 3.6 | [hybrid](/methods/hybrid-weno.md) HMR-WENO5/7/9 vs MR-WENO; third-order TVD Runge–Kutta | $600\times200$; $t=4$; 30 contours 0.32–6.15 | 0.6 |
| [Fan et al. (2025a)](/sources/fan-2025.md) Ex. 3.11 | moment-based [HWENO](/methods/hermite-weno.md) with unified stencils HWENO-U vs HWENO-M, WENO-ZQ; modified SSP-RK3 | $960\times320$ | 0.6 |
| [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) Ex. 5.9 | generalized [Active Flux](/methods/active-flux.md), flux-vector-split point values, bound-preserving limiting, with and without shock-sensor limiting ($\kappa_{\mathrm s}=1$) | $480\times160$, $960\times320$ | — |
| [Huang et al. (2025b)](/sources/huang-2025-b.md) §4.2.5 | MUSCL, MUSCL-THINC-[BVD](/definitions/boundary-variation-diminishing.md), deepMTBVD (network-selected BVD), dimensional splitting | $480\times160$ ($\Delta x=1/160$) | — |
| [de Romémont et al. (2026)](/sources/deromemont-2026.md) §6.3 | second-order MUSCL with [learned slopes](/methods/learned-weno-weights.md) (van Albada limiter kept), Rusanov flux, explicit Euler | $384\times128$, reference $768\times256$ | Courant 0.01 |
| [Vilar & Abgrall (2024)](/sources/vilar-2024.md) §4.3.3 | $\mathbb P^5$ DG with a posteriori local subcell correction ([MOOD-type](/methods/mood-a-posteriori-limiting.md)), first-order FV fallback | 680 triangles, no refinement at the corner | — |
| [Gaburro et al. (2024)](/sources/gaburro-2024.md) §5.1.6 | quasi-conservative [ADER](/methods/ader-scheme.md)-DG $\mathbb P^2$, $\mathbb P^3$ in primitive variables, a posteriori subcell FV limiter with conservative correction in shock cells | polygons, $h=1/80$ | 0.5 after 10 steps at 0.1 |

## What the benchmark measures

**Robustness of very-high-order WENO.** Luo & Wu report that both the
seventh- and the ninth-order WENO-Z schemes fail on this problem at CFL
0.5, while WENO-Z+M runs and resolves the shear layer "significantly
better" than WENO-IS-I (§5.3.4, Fig. 16). The same paper needs CFL 0.1 for
WENO-Z9 on the [double Mach reflection](/benchmarks/double-mach-reflection.md),
so the two problems together expose a stability margin that design
order alone does not show.

**The corner without a fix.** Five sources describe no
Woodward–Colella corner treatment: Yu & Hesthaven, Chen & Wu, Zhao
et al. and Vilar & Abgrall say so, Du et al. mention only local mesh
refinement. Vilar & Abgrall run sixth-order DG on only 680 triangles,
with no special treatment beyond their subcell correction (no
corner refinement, no change of the scheme), and show the solution at
$t=4$ (Fig. 41). Zhao et
al.'s compact gas-kinetic scheme at CFL 0.8 captures the slip-line
instability without a corner fix (Fig. 9). Du et al. see a spurious Mach stem at
the bottom wall, caused by the corner, in the $\mathbb P^2$ result with the
original limiter, which "decreases when using the improved limiter";
the improved limiter saves 9.35 % ($\mathbb P^1$) and 33.96 % ($\mathbb P^2$) of the
CPU time (Ex. 4.5, Fig. 4.9, Table 4.9). Yu & Hesthaven stabilize the
shocks without special treatment of the corner; an entropy layer along
the step wall, triggered by the corner (where their Lobatto edge nodes
put a zero velocity), decreases with the polynomial degree, and the
results agree with Chaudhuri et al. The run needs the tuned setting
$\mathfrak a_0=2.5$ (the threshold of the modal decay rate
in their viscosity switch, page-local; default 2) with the min-rule
(§5.4.5, Figs. 21–23). In Chen & Wu's
relativistic runs the physical-constraint-preserving limiter is needed
to keep the scheme running at every inflow speed (Ex. 4.9, Fig. 13).

Tang lowers the CFL number to 0.45 because TENO-Z and TENO-A "may
fail if the CFL number is too large"; at that value the TENO-AZ
captures finer vortices near $y=0.7$ than the other TENO schemes
(§4.4.7, Fig. 17), with 45 density contours in $[0.5,6.5]$. Gaburro et
al.'s primitive-variable DG with a conservative correction only in the
shock-triggered subcells runs at third and fourth order (Fig. 5).

Duan, Barsukow & Klingenberg find that their bound-preserving Active
Flux captures the vortices better than third-order $\mathbb P^2$ DG with a TVB
limiter on the same mesh while using fewer degrees of freedom, and that
the shock-sensor limiting
$\exp(-\kappa_{\mathrm s}\varphi_{\mathrm J}\Psi_{\mathrm D})$ ($\varphi_{\mathrm J}$ a Jameson pressure sensor and $\kappa_{\mathrm s}$ the sensor strength, page-local; $\Psi_{\mathrm D}$ the modified [Ducros sensor](/definitions/ducros-shock-sensor.md)) strongly reduces the oscillations behind
the strong shocks; $\kappa_{\mathrm s}$ is problem-dependent (§4.1.3, Ex. 5.9). de
Romémont et al. report a relative $L^1$ error 19 % below that of the
same MUSCL scheme with standard slopes on the same grid, with an
overshoot and spurious oscillations at the corner that they attribute to
"the double boundary condition at the corner" (Fig. 15); the case is not
in their slip-wall training data.

**Shock stability of the Riemann solver.** Hu, Yuan & Zhao use the
step as one of their tests of the
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md): HLLC and
HLLEM, "especially the latter", show shock instabilities, and their
RHLLEM-LD does not (§5.11); see
[HLL-family solvers](/methods/hll-riemann-solvers.md).

**Steady-state convergence.** On Wan & Xia's steady run all schemes
converge to a residual of about $10^{-13}$ except MRWENO, which stalls;
raising its Lax–Friedrichs speed by a factor 1.1 (MRWENO(1.1)) makes
it converge (Ex. 4.5).

**Cost of adaptivity and of Hermite WENO.** Mossier et al. compare a
static run with their $p$-adaptive and $hp$-adaptive setups: 216, 44
and 82 degrees of freedom per element, wall times 65,782 s, 19,774 s
and 40,217 s, memory 4.8, 5.8 and 18.7 GB (Table 4); the speedups are
$65782/19774=3.33$ and $65782/40217=1.64$ *(compiler check, not in the
sources)*, which the paper describes as "almost a factor 3" and "about
1.6". Their finer FV subcells ($N_{\mathrm{FV}}=2N+1$) almost completely
suppress the acoustic waves that DG/FV interfaces emit with
$N_{\mathrm{FV}}=N+1$ (§8.7, Fig. 16). Fan et al. (2023)'s HWENO-R and HWENO-L
resolve the flow better than WENO-ZQ, owing to their more compact
stencils, HWENO-R slightly better than HWENO-L (Fig. 3.13); the total
CPU times are 29093.92 s, 31945.12 s and 20542.55 s, ratios 1.416 and
1.555 to WENO-ZQ, in Fortran 95 on an Intel Xeon Gold 6130 (Ex. 3.9).
Fan et al. (2025a) find the results of HWENO-U and HWENO-M comparable
(Fig. 16), on the same hardware; over their shock tests the total CPU
time of HWENO-U always lies between those of WENO-ZQ and HWENO-M
(Table 7).

**Learned selection of THINC cells.** Huang et al. (2025b) find
deepMTBVD resolving the vortical structure as MUSCL-THINC-BVD does, with
consistent THINC-cell maps between the two (Figs. 9–10); both select more
THINC cells near the shock above the step than Cheng's results they
compare with, which they attribute to dimensional splitting. Their
totals are 215.66 s (deepMTBVD) against 242.54 s (MUSCL-THINC-BVD),
hardware not stated (Table 4); the printed MUSCL-THINC-BVD components,
212.22 s and 50.32 s, sum to 262.54 s, which would make the saving
17.9 % instead of the 11.1 % implied by the printed totals *(compiler
check, not in the sources)*.

**Vortex-sheet roll-up.** Li et al. find that all schemes capture the
shocks and that WENO-ZN gives the clearest Kelvin–Helmholtz roll-up of
the vortex sheet (§4.4.3, Fig. 9). Balsara et al. show "pronounced"
vortex-sheet roll-up at seventh order on $1440\times480$ (Fig. 17).
Luo & Wu plot 60 density contours from 0.2568 to 6.607. Wang et al.
(2021) find the multi-resolution schemes resolving the roll-up better
than WENO-JS5 (Fig. 5.14). In Zhong et al.'s runs all schemes capture
the shocks sharply; WENO-JS and WENO-Z fail to resolve the vortex
sheets from the Mach stem, WENO-NS, WENO-P, MWENO-P and IMWENO-P show
them, and IMWENO-P and WENO-NS roll them up more intensely than WENO-P
and MWENO-P (Fig. 21). On triangles, Liu et al. (2023b) find
that their fourth-order IRBFDQ-FV captures the Kelvin–Helmholtz
instability along the contact discontinuity, which their second-order
scheme does not, and separates the shock from the wall-reflected wave;
the pattern agrees with k-exact finite-volume results they cite
(Fig. 8).

**Multi-resolution WENO and its hybrids.** Lin & Zhu find that the
resolution, "especially for the vortex sheet roll-up", improves with
the order of their two-stencil ALW-MR-WENO on triangles, which gives
results similar to MR-WENO of the same order (Case 3.9, Figs.
3.15–3.17). Zuo & Zhu (2024b) find their hybrid HMR-WENO, which applies
MR-WENO only in cells where an extremum of the high-degree interpolant
is detected, outperforming MR-WENO of the same order, "especially for
addressing the Kelvin-Helmholtz instability and roll-up of the contact
line" (Ex. 3.6, Figs. 3.9–3.10, with the troubled-cell map), at lower
cost: MR-WENO 3763.48, 9589.80 and 14582.4 s against HMR-WENO 1671.75,
4182.02 and 10283.0 s at orders 5, 7 and 9 (Table 3.1, a laptop). Lin &
Zhu's ALW/MR time ratios over their Cases 3.3–3.11 are 0.60–0.96, smallest at
fifth order (Table 3.1). Neither paper describes a corner treatment.

**Hermite WENO and its first moments.** Li, Shu & Qiu recall that the
original Hermite WENO schemes are "not stable enough" for the forward
step, because first-derivative values grow large near discontinuities
(§1). Their sixth-order scheme runs both without and with the
modification of the first moments in troubled cells; the modified one
gives "much better resolutions and sharper shock transitions", and the
troubled cells flagged by their modified KXRCF indicator are plotted
(Fig. 3.8, comment p. 31). See
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

## Qualifications

- Evidence is visual (contour plots), apart from de Romémont et al.'s
  relative $L^1$ error against a twice-finer run of the standard scheme;
  no source reports an error against an exact or converged solution.
- The Cartesian grids of the unsteady runs differ by a factor of three
  in each direction ($481\times161$ to $1440\times480$), Mossier et
  al.'s $180\times60$ DG elements and Wan & Xia's steady $90\times30$
  cells are coarser still, the triangular meshes are
  locally refined or unstructured, and the time steppers and fluxes
  differ, so the roll-up seen in the papers is not comparable across
  them.
- Yu & Hesthaven stop at $t=3$, the other non-relativistic unsteady
  runs that print a final time at $t=4$; Mossier et al. print none.
- Li et al. write that the problem "is also originally from the paper
  of [30]", with no preceding mention of that paper.
- Tang's step interior and Gaburro et al.'s printed domain depart from
  the Woodward–Colella setup (see Setup).

# Citations

- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.4, Fig. 16.
- [Li et al. (2022b)](/sources/li-2022-b.md) — §4.4.3, Fig. 9.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.g, Fig. 17.
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §1; Ex. 3.10, Fig. 3.8; comment p. 31 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.8, Fig. 5.14.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — Ex. 4.5, Figs. 4.8–4.9, Table 4.9.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.5, Figs. 21–23.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.9, Fig. 13 (arXiv v1).
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.11.
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §8.7, Table 4, Fig. 16.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.9, Fig. 3.13.
- [Wan & Xia (2022)](/sources/wan-2022.md) — Ex. 4.5.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.4, Ex. 16, Fig. 21.
- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §5.3, Fig. 8.
- [Zhao, Ji, Shyy & Xu (2023)](/sources/zhao-2023.md) — §4.6, Fig. 9 (arXiv v1).
- [Tang (2024)](/sources/tang-2024.md) — §4.4.7, Eq. (40), Fig. 17.
- [Gaburro et al. (2024)](/sources/gaburro-2024.md) — §5.1.6, Fig. 5 (arXiv v1).
- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3, Case 3.9, Figs. 3.15–3.17, Table 3.1.
- [Zuo & Zhu (2024b)](/sources/zuo-2024-b.md) — §3, Ex. 3.6, Figs. 3.9–3.10, Table 3.1.
- [Fan et al. (2025a)](/sources/fan-2025.md) — §3, Ex. 3.11, Fig. 16, Table 7.
- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — §4.3.3, Fig. 41 (HAL preprint).
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §4.1.3, Ex. 5.9 (arXiv v3).
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §4.2.5, Table 4, Figs. 9–10.
- [de Romémont et al. (2026)](/sources/deromemont-2026.md) — §6.3, Fig. 15.
