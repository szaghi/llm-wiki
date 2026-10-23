---
type: Benchmark
title: "Two-dimensional Riemann problems"
description: "Four-quadrant Riemann problems of the two-dimensional Euler equations in the Lax–Liu classification, chiefly configurations 3 and 12, with configurations 7 and 13 and two four-contact configurations; used as visual tests of resolution, of the jet's sideband and neck instabilities and of slip-line instability, of scale invariance and of moving-mesh efficiency, with relativistic, MHD, multispecies and Burgers relatives."
status: established
aliases: [2D Riemann problem, four-quadrant Riemann problem, Lax–Liu configuration 3, Lax–Liu configuration 12, Lax–Liu configuration 7]
tags: [benchmark, low-dissipation, weno, teno, central-scheme]
timestamp: 2026-10-23T23:50:00Z
---

# Two-dimensional Riemann problems

A two-dimensional Riemann problem divides the square into four
quadrants, each with a constant state; the sources that number the
configurations follow Lax & Liu (cited by Takagi et al., Luo & Wu,
Deng, Huang et al. and Zhong et al.; Wang et al. (2023b) and Chertock et al. take
configuration 3, and Fu 2023 configuration 12, from Kurganov & Tadmor;
Boscarino et al., Hong, Ye & Ye and Liang et al. cite Lax & Liu or
Schulz-Rinne et al.). Four kinds are used in the bundle:
**configuration 3**, in which a jet forms along the diagonal whose
sideband and neck instabilities serve as a resolution gauge,
**configuration 12**, **configuration 7**, **configuration 13**, and configurations of four
contacts that roll up into a spiral. The data of the first two are symmetric under the
exchange $x\leftrightarrow y$, $v_1\leftrightarrow v_2$ (see the tables
below) *(compiler check, not in the sources)*, so they also test
[symmetry preservation](/properties/symmetry-preservation.md).
All states use $\gamma=1.4$ and are written $(\rho,v_1,v_2,p)$.

## Configuration 3

With the quadrant split at $(x_0,y_0)$:

| Quadrant | State |
|---|---|
| $x>x_0$, $y>y_0$ | $(1.5,\ 0,\ 0,\ 1.5)$ |
| $x<x_0$, $y>y_0$ | $(0.5323,\ 1.206,\ 0,\ 0.3)$ |
| $x<x_0$, $y<y_0$ | $(0.138,\ 1.206,\ 1.206,\ 0.029)$ |
| $x>x_0$, $y<y_0$ | $(0.5323,\ 0,\ 1.206,\ 0.3)$ |

The sources use three placements and several final times:

| Source | Domain, split | Grid | Final time | Scheme |
|---|---|---|---|---|
| [Deng (2023)](/sources/deng-2023.md) App. A.10 | $[0,1]^2$, $(0.8,0.8)$ | $600\times600$ | 0.8 | [ROUND](/methods/round-scheme.md) |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.6, Eq. (6.8) | $[0,1]^2$, $(0.8,0.8)$ | $600\times600$ | 0.8 | ROUND, LD-ROUND, [WENO3-NN](/methods/learned-weno-weights.md), WENO5-JS |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) Example 5 | $[0,1]^2$, $(0.8,0.8)$, free boundaries | $\Delta x=\Delta y=1/400$ | 0.8 | A-WENO with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) |
| [Luo & Wu (2021)](/sources/luo-2021-b.md) §5.3.2 | not restated | $401\times401$, CFL 0.5 | 0.8 | [WENO-Z+M](/methods/weno-z-plus.md) |
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 5 | $[0,1.2]^2$, $(1,1)$, free boundaries | $\Delta x=\Delta y=3/2500$ | 1 | [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.8.1 | $[0,1]^2$, $(0.5,0.5)$ | $1024\times1024$ | 0.3 | [TENO-THINC](/methods/teno-thinc.md) |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.15 (their "second Riemann problem") | $[0,1]^2$, $(0.5,0.5)$, outflow | $320\times320$ | 0.35 | [OEDG](/methods/oedg.md), third order, data scaled by $\lambda\in\{1,100\}$ |
| [Wang et al. (2021)](/sources/wang-2021.md) Example 5.6 ("four shocks") | $[0,1]^2$, $(0.8,0.8)$ | $400\times400$, CFL 0.6 | 0.8 | [multi-resolution WENO](/methods/multi-resolution-weno.md) vs WENO-JS5, WENO-AO5 |
| [Boscarino et al. (2022)](/sources/boscarino-2022.md) Ex. 5.4(a) ("modified" configuration 3) | $[-1,1]^2$, $(0.8,0.8)$ | $400\times400$, CFL 0.25 | 0.8 | [semi-implicit all-Mach](/methods/semi-implicit-all-mach-scheme.md) WENO S4T3 at $\varepsilon=1$, reconstruction approaches A1–A3, S2T2 |
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.7 ("four-shock configuration") | $[0,1]^2$, $(0.5,0.5)$ | $512\times512$, van Leer flux | 0.3 | TENO-M6/M8 ([TENO](/methods/targeted-eno.md) with stencil extension) vs TENO, WENO; timing |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.6 | $[0,1]^2$, split not recorded | $512^2$, $1024^2$ | 0.3 | [TENO-THINC](/methods/teno-thinc.md)-family scheme vs TENO5-THINC, TENO5, WENO5-Z |
| [Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.7 | $[0,1]^2$, $(0.8,0.8)$, non-reflective | $400\times400$, CFL 0.2 | 0.8 | [gradient-based](/methods/gradient-based-reconstruction.md) MIG4, MIG4-base, MEG6 vs TENO5, primitive variables (arXiv v2) |
| [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.9 | $[0,1]^2$, $(0.8,0.8)$ | $400\times400$, CFL 0.2 | 0.8 | MEG7 (conservative and primitive) vs seventh-order mapped WCNS7M (arXiv v1) |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.6, Eq. (41) | $[0,1]^2$, $(0.8,0.8)$, non-reflective | $\Delta x=\Delta y=1/400$, CFL 0.5, HLLC with pressure control | 0.8 | six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS-SA vs WCNS-LD and ONL6 |
| [Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 13 ("a similar version of Configuration 3") | $[0,1]^2$, $(0.8,0.8)$, zero gradient | $400\times400$, CFL 0.5 | 0.8 | fifth-order FV IMWENO-P vs WENO-JS, WENO-Z, WENO-NS, WENO-P, MWENO-P |
| [Zuo & Zhu (2024a)](/sources/zuo-2024.md) Ex. 3.5 | $[0,1]^2$, $(0.8,0.8)$, boundary conditions not stated | $400\times400$, CFL 0.6 | 0.8 | [hybrid](/methods/hybrid-weno.md) MMR-WENO5/7/9 vs [MR-WENO](/methods/multi-resolution-weno.md) |
| [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) App. A.3 | box $L_0\times L_0$, quadrants split at $x=y=0$, extrapolation | $1600\times1600$ | $t/t_0=0.3$ | [WENO-Z](/methods/weno-z.md)5, WENO-Z7, TENO5, [TENO-A5](/methods/adaptive-teno.md) in [URANOS](/software/uranos.md) |

The two Chamarthi papers print the states as fractions,
$(33/62,\,4/\sqrt{11},\,0,\,0.3)$, $(77/558,\,4/\sqrt{11},\,4/\sqrt{11},\,9/310)$;
$33/62=0.53226$, $4/\sqrt{11}=1.20605$, $77/558=0.13799$ and
$9/310=0.029032$ round to the decimals of the table *(compiler check,
not in the sources)*.

Contours: Deng 40 from 0.14 to 1.7, Luo & Wu 40 from 0.14 to 1.7,
Huang et al. 43 from 0.135 to 1.75, Wang et al. (2023b) 35 from 0.1 to 1.8.
Boscarino et al.'s placement puts the split at $(0.8,0.8)$ of
$[-1,1]^2$, so the low-pressure quadrant covers $[-1,0.8]^2$ and the
high-pressure one only $[0.8,1]^2$ *(compiler check, not in the
sources)*; with $t=0.8$ the jet is not at the stage of the $[0,1]^2$
runs with the same split. Their time step uses
$\Delta t=\mathrm{CFL}\,\Delta x/\max(\lvert v_1\rvert+\lvert v_2\rvert+c)$
at $\varepsilon=1$ (§5).

## Configuration 7

[Liang et al. (2022)](/sources/liang-2022.md) §4.6, citing Lax & Liu,
run configuration 7 on $1024^2$ to $t=0.25$:

| Quadrant | State |
|---|---|
| north-east | $(1,\ 0.1,\ 0.1,\ 1)$ |
| north-west | $(0.5197,\ -0.6259,\ 0.1,\ 0.4)$ |
| south-west | $(0.8,\ 0.1,\ 0.1,\ 0.4)$ |
| south-east | $(0.5197,\ 0.1,\ -0.6259,\ 0.4)$ |

The data are symmetric under $x\leftrightarrow y$, $v_1\leftrightarrow v_2$
*(compiler check, not in the sources)*.

## Configuration 13

[Zhong et al. (2023)](/sources/zhong-2023.md) Ex. 14, citing Lax & Liu's
configuration 13, on $[0,1]^2$ split at $(0.5,0.5)$, transmissive
boundaries, $t=0.3$, $800\times800$ and $1200\times1200$:

| Quadrant | State |
|---|---|
| $x>0.5$, $y>0.5$ | $(1,\ 0,\ -0.3,\ 1)$ |
| $x<0.5$, $y>0.5$ | $(2,\ 0,\ 0.3,\ 1)$ |
| $x<0.5$, $y<0.5$ | $(1.0625,\ 0,\ 0.8145,\ 0.4)$ |
| $x>0.5$, $y<0.5$ | $(0.5313,\ 0,\ 0.4276,\ 0.4)$ |

On both halves of the vertical split $x=0.5$ the normal velocity $v_1$
vanishes and the pressure is continuous while $v_2$ jumps, so the two
discontinuities on $x=0.5$ are slip lines; across $y=0.5$ the pressure
falls from 1 to 0.4 *(compiler check, not in the sources)*. Zhong et
al. use the slip line as the dissipation gauge.

## Configuration 12

| Quadrant | State |
|---|---|
| $x>0.5$, $y>0.5$ | $(0.5313,\ 0,\ 0,\ 0.4)$ |
| $x<0.5$, $y>0.5$ | $(1,\ 0.7276,\ 0,\ 1)$ |
| $x<0.5$, $y<0.5$ | $(0.8,\ 0,\ 0,\ 1)$ |
| $x>0.5$, $y<0.5$ | $(1,\ 0,\ 0.7276,\ 1)$ |

as printed by [Takagi et al. (2022)](/sources/takagi-2022.md) §4.8.2,
Eq. (34), who call it configuration 12 after Lax & Liu
($1024\times1024$, $t=0.25$).
[Pazner (2021)](/sources/pazner-2021.md) §5.6 prints the same data in
exact form: $\rho=4/5$, $v=0$, $p=1$ on $(0,\tfrac12)^2$; $\rho=1$ with
$v=(3/\sqrt{17},0)$ and $v=(0,3/\sqrt{17})$, $p=1$, in the upper-left
and lower-right quadrants; $\rho=17/32$, $v=0$, $p=2/5$ on
$(\tfrac12,1)^2$ ($3/\sqrt{17}=0.72761$, $17/32=0.53125$)
*(compiler check, not in the sources)*. Pazner makes the problem periodic on $[0,2]^2$ by reflection about
$(1,1)$ and runs it to $t=0.25$.
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.3, their "2D
Riemann problem I", print the decimal states of the table above,
citing Brio, Zakharian & Webb (2001), and run to $t=0.25$.
[Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.1, citing Kurganov &
Tadmor for "Case 12", print the same decimal states, make the problem
periodic by tiling it on $[-0.5,2.5]^2$, and run nodal DG with
ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md)
on triangles with $h=1/160$ to $t=0.25$ (30 contours 0.515–1.665).
[Fu (2023)](/sources/fu-2023.md) Fig. 7 reproduces a configuration-12
run showing the density with the TENO discontinuity flags in $x$ and $y$
(43 contours).
[Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.15 name neither a
configuration number nor Lax & Liu; they call their two problems the
"first" ($320\times320$, $t=0.25$) and "second" ($t=0.35$) Riemann
problems. Their printed states coincide, quadrant by quadrant and with
the same split $(0.5,0.5)$, with Takagi et al.'s Eq. (34)
(configuration 12) and Eq. (33) (configuration 3) *(compiler check, not
in the sources)*; on that basis they
are listed here under those configurations.
[Chudzik et al. (2024)](/sources/chudzik-2024.md) Ex. 7.4, citing
Schulz-Rinne et al., print the same decimal states with the split at
$(0.5,0.5)$ of $[0,1]^2$, two forward-moving shocks and two stationary
contacts, and run them on $128^2$ and $512^2$ with their third-order
[Active Flux](/methods/active-flux.md) method without any limiter; the
output time is not given in the text (Fig. 24).

## Four-contact configurations

[Li, Duan & Tang (2022)](/sources/li-2022-c.md) Ex. 5.4, their "2D
Riemann problem II", citing Lax & Liu without a configuration number:

| Quadrant | State |
|---|---|
| $x>0.5$, $y>0.5$ | $(1,\ 0.75,\ -0.5,\ 1)$ |
| $x<0.5$, $y>0.5$ | $(2,\ 0.75,\ 0.5,\ 1)$ |
| $x<0.5$, $y<0.5$ | $(1,\ -0.75,\ 0.5,\ 1)$ |
| $x>0.5$, $y<0.5$ | $(3,\ -0.75,\ -0.5,\ 1)$ |

The pressure is uniform and the four initial discontinuities are
contacts, which roll up into a spiral; $t=0.3$. The data are not
symmetric under $x\leftrightarrow y$, $v_1\leftrightarrow v_2$ *(compiler
check, not in the sources)*.

[Boscarino et al. (2022)](/sources/boscarino-2022.md) Ex. 5.4(b), citing
Lax & Liu's configuration 5, print on $[-1,1]^2$ with the split at
$(0.5,0.5)$, $400\times400$, $t=0.23$:

| Quadrant | State |
|---|---|
| north-east | $(1,\ -0.75,\ -0.5,\ 1)$ |
| north-west | $(2,\ -0.75,\ 0.5,\ 1)$ |
| south-west | $(1,\ 0.75,\ 0.5,\ 1)$ |
| south-east | $(3,\ 0.75,\ -0.5,\ 1)$ |

These are Li, Duan & Tang's states with $v_1$ negated in every quadrant.
The normal velocity is continuous across both splits in either set, so
both are four-contact problems, but the tangential jumps across the
horizontal split change sign, so the two are different configurations,
not one problem in two placements *(compiler check, not in the
sources)*. Li, Duan & Tang give no configuration number; which of the
two is Lax & Liu's configuration 5 cannot be decided from the bundle's
sources.

[Tang (2024)](/sources/tang-2024.md) §4.4.2, Eq. (34) prints on $[0,1]^2$,
split at $(0.5,0.5)$, zero-order extrapolation boundaries, $512\times512$,
$t=0.8$, 14 density contours in $[0.2,2.2]$:

| Quadrant | State |
|---|---|
| $x\ge0.5$, $y\ge0.5$ | $(3,\ -0.75,\ -0.5,\ 1)$ |
| $x<0.5$, $y\ge0.5$ | $(2,\ 0.75,\ 0.5,\ 1)$ |
| $x<0.5$, $y<0.5$ | $(1,\ -0.75,\ 0.5,\ 1)$ |
| $x\ge0.5$, $y<0.5$ | $(1,\ 0.75,\ -0.5,\ 1)$ |

These are Li, Duan & Tang's states with the two right quadrants
exchanged. The normal velocity is then continuous across the horizontal
split but jumps across the vertical one ($0.75$ to $-0.75$ on top,
$-0.75$ to $0.75$ below), so the vertical discontinuities are not
contacts and the problem is not a four-contact configuration
*(compiler check, not in the sources)*; Tang cites no configuration
number.

## Findings across sources

**Jet instabilities as a dissipation gauge.** On configuration 3 the
lower-dissipation schemes resolve the sideband instability of the jet
and the instability along its neck: the LCD central-upwind scheme
against the earlier central-upwind scheme (Chertock et al., Fig. 5.5),
and the adaptive-diffusion CURH flux against the earlier A-WENO flux
(Wang et al. 2023b, Fig. 5), with the same wording in both papers. Takagi et
al. find TENO-THINC finer than WENO5-Z and TENO5 on both
configurations, with shocks sharp and stable and symmetry preserved
(Figs. 18–19). Luo & Wu find WENO-Z+ about equal to WENO-Z, and
WENO-Z+M better resolved and more symmetric than WENO-IS-I and WENO-Z9
(Fig. 14). Deng resolves the main structures "with less grid number"
than WENO-JS5 on $600\times600$ (Figs. 24, 35); Huang et al. compare
ROUND and LD-ROUND with WENO3-NN and WENO5-JS on the same grid.

Liang et al. find their scheme resolving more instability and vortical
structure than WENO5-Z, TENO5 and TENO5-THINC on configurations 3 and
7 (§4.6, Figs. 16–18). Hong, Ye & Ye find TENO-M slightly better than
TENO on the small structures along the slip lines, both much better
than the WENO schemes (§5.7, Fig. 15); per 1000 steps TENO-M6 takes
1632.51 s against 2034.43 s for TENO6, 1432.34 s for WENO-JS and
1746.42 s for WENO-CU6, and TENO-M8 1838.13 s against 2626.74 s for
TENO8 (Table 4, Intel i9-10980XE).

Chamarthi (2023a) ranks MIG4 above MEG6 above TENO5 in the vortical
structures, and MIG4 above MIG4-base, which isolates the effect of
reusing the high-order second derivative as the curvature of the
[MP limiter](/methods/monotonicity-preserving-limiter.md) (Fig. 10).
Chamarthi (2023b) finds MEG7 with conservative variables resolving the
slip-line structures better than WCNS7M, with a minor difference
between conservative and primitive variables (Fig. 12); the wall-clock
times are 1025 s (MEG7-prim), 1031 s (MEG7-cons) and 1502 s (WCNS7M),
hardware not stated (Table 2).

Zhou et al. find WCNS-LD and WCNS-SA resolving more vortices than ONL6
but with more post-shock noise (§5.6, Fig. 16). De Vanna et al. (2023b)
print the same four states and find that a higher WENO order and TENO
resolve additional shear-layer instabilities and more detail of the
central plume, compared qualitatively with Guo & Shi (App. A.3,
Fig. 13).

Zuo & Zhu (2024a) find their hybrid MMR-WENO giving "more delicate
roll-up structures" and "smaller numerical dissipations and higher
density resolutions" than MR-WENO of the same order on configuration 3,
with the flagged cells plotted (Ex. 3.5, Figs. 3.6–3.7), at 32.5 %, 23.6 % and 23.2 % of the MR-WENO CPU time
for orders 5, 7, 9 (Table 3.1).

**Unlimited Active Flux on configuration 12.** Chudzik et al. run
configuration 12 with no limiter at all, as all simulations of their
paper; the method uses the linearized bicharacteristic EG2 operator for
the point values and finite volumes with Simpson-rule fluxes for the
averages (§7, Ex. 7.4, Fig. 24). Their figure is the only evidence; the
paper reports no oscillation measure.

**Characteristic reconstruction in a semi-implicit scheme.** Boscarino
et al. use both of their problems at $\varepsilon=1$ to choose where
characteristic decomposition is needed in their all-Mach splitting:
characteristic-wise WENO on the explicit flux part with component-wise
WENO on the semi-implicit part (approach A1) is closest to the
reference without obvious oscillations, while component-wise
reconstruction everywhere (A2) or no splitting (A3) oscillates in the
middle region; the second-order S2T2 is closer to A1 but less resolved
(Ex. 5.4, Figs. 5.4–5.5). See [characteristic
decomposition](/methods/characteristic-decomposition.md).

Wang et al. (2021) find both multi-resolution WENO5 schemes capturing
more roll-up than WENO-JS5 and WENO-AO5 on configuration 3 (Fig. 5.12).
Pazner compares $N=1$ on $128^2$ elements with $N=3$ on $64^2$, the same
number of degrees of freedom, on configuration 12: $N=3$ gives sharper
interfaces and better small-scale features (Fig. 12).

Yu & Hesthaven report the oscillations suppressed and the contact
lines preserved on configuration 12 (Fig. 12).

**Moving meshes against uniform ones.** Li, Duan & Tang compare their
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) multi-resolution
WENO (MM-WENOMR) with uniform meshes on 4 cores. On configuration 12,
MM-WENOMR on $200^2$ (2 min 56 s) has sharper shocks than the uniform
$500^2$ run (7 min 9 s), at 41.0 % of its CPU time; MM-WENOJS on $200^2$
takes 2 min 37 s. On the four-contact problem MM-WENOMR on $200^2$
(2 min 50 s) costs 21.5 % of the uniform $600^2$ run (13 min 10 s) and
7.6 % more than MM-WENOJS, and resolves more small-scale roll-up
(Ex. 5.3–5.4, Table 5.1).

**Discontinuity location.** Fu (2023) uses configuration 12 to show
that the TENO stencil-selection flags locate the discontinuities, the
basis of the hybrid TENO scheme with a TENO-based indicator (§3.4,
Fig. 7).

**Scale invariance.** Peng, Sun & Wu multiply both configurations by a
factor $\lambda=100$ (page-local symbol): the OFDG damping grows, they state, to "$\lambda^2$ times
its original magnitudes" and smooths the features, while OEDG matches
its $\lambda=1$ result (Figs. 10–11).

**Symmetric smoothness indicators.** Zhong et al. find on
configuration 3 that all six fifth-order finite-volume schemes capture
the reflected shocks and contacts, that IMWENO-P, WENO-NS, WENO-P and
MWENO-P roll up the Kelvin–Helmholtz instability where WENO-JS and
WENO-Z do not, and that IMWENO-P resolves the finest roll-up (Fig. 15);
they add that weak solutions of the two-dimensional Euler equations are
not unique, so the small scales are scheme- and mesh-determined and
"usually are non-physical", while the test is still widely used as a
dissipation gauge. On configuration 13 at $800\times800$ only IMWENO-P
captures the slip-line instability; at $1200\times1200$ IMWENO-P and
MWENO-P resolve it, WENO-NS "very slightly", and WENO-JS, WENO-Z and
WENO-P do not (Figs. 16–19). See
[smoothness indicator](/definitions/smoothness-indicator.md).

**Adaptive TENO on the Tang configuration.** Tang finds that the
TENO-AZ generates more refined Kelvin–Helmholtz microstructures than
TENO-Z, TENO-A and TENO-LAD (§4.4.2, Fig. 11;
see [adaptive TENO](/methods/adaptive-teno.md)), at 0.98–1.01 of
TENO-Z's time per step on $400\times400$ (Table 6).

## Other systems

The same four-quadrant construction appears for other equations:
special-relativistic hydrodynamics ([Cui, Ding & Wu 2024](/sources/cui-2024.md)
Example 4, $\gamma=5/3$, $[0,1]^2$, $400\times400$, $t=0.4$, a
mushroom-like structure; the problem is symmetric about $y=x$, so the
quasi-optimal cell-average decomposition is close to the optimal one,
Table 9; see below for two further relativistic sources); the stiff Baer–Nunziato two-phase model
([Balsara et al. 2024](/sources/balsara-2024.md) §X.b, Table XIV,
$400\times400$, $t=0.15$); and the two-dimensional Burgers equation
([Peng, Sun & Wu 2024](/sources/peng-2024.md) Ex. 5.11, quadrant
values $0.5$, $0.8$, $-1$, $-0.2$, $256^2$, $t=0.5$; the same quadrant
values in [Pazner 2021](/sources/pazner-2021.md) §5.5, see
[Burgers equation tests](/benchmarks/burgers-equation-tests.md)).

**Relativistic configurations.** In
[relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md)
the quadrant states are printed as $(\rho,v_1,v_2,p)$ with
$\lvert v\rvert<1$, split at $(0.5,0.5)$ of $[0,1]^2$.
[Chen & Wu (2022)](/sources/chen-2022-b.md) Exs. 4.6–4.7 (arXiv v1),
on triangles with $h=1/400$ to $t=0.4$:

| Quadrant | Ex. 4.6 | Ex. 4.7 |
|---|---|---|
| $x>0.5$, $y>0.5$ | $(0.1,0,0,0.01)$ | $(0.1,0,0,20)$ |
| $x<0.5$, $y>0.5$ | $(0.1,0.99,0,1)$ | $(0.00414329639576,\ 0.9946418833556542,\ 0,\ 0.05)$ |
| $x<0.5$, $y<0.5$ | $(0.5,0,0,1)$ | $(0.01,0,0,0.05)$ |
| $x>0.5$, $y<0.5$ | $(0.1,0,0.99,1)$ | $(0.00414329639576,\ 0,\ 0.9946418833556542,\ 0.05)$ |

Their third-order finite-volume WENO blows up without the
physical-constraint-preserving limiter on both, on Ex. 4.7 in the first
step; on Ex. 4.6 the limiter acts on about 100 cells (0.3 %) early and
on 3 later (Figs. 10–11). In Ex. 4.7, they state, the shocks move at speed
0.66525606186639 and the contacts are stationary.
[Duan & Tang (2022)](/sources/duan-2022.md) Exs. 6.2–6.4 (arXiv v1) run
three relativistic configurations to $t=0.4$ (domain and boundary
conditions not stated, $[0,1]^2$ by the split): four vortex sheets of
one sign that wind into a low-density spiral, $(0.5,0.5,-0.5,5)$,
$(1,0.5,0.5,5)$, $(3,-0.5,0.5,5)$, $(1.5,-0.5,-0.5,5)$ in the quadrant
order above; four rarefactions, $(1,0,0,1)$, $(0.5771,-0.3529,0,0.4)$,
$(1,-0.3529,-0.3529,1)$, $(0.5771,0,-0.3529,0.4)$; and two contacts with
two shocks, $(0.035145216124503,0,0,0.162931056509027)$,
$(0.1,0.7,0,1)$, $(0.5,0,0,1)$, $(0.1,0,0.7,1)$, which forms a central
"mushroom cloud". Their fifth-order entropy-stable scheme on an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md) with $200^2$
cells matches the uniform-mesh scheme on $500^2$, $500^2$ and $600^2$
cells at 17.8 %, 30.6 % and 13.7 % of its CPU time, and on $150^2$
beats their second-order moving-mesh scheme on $200^2$ at comparable
cost (Figs. 6.5–6.7).

[Cai, Qiu & Wu (2024)](/sources/cai-2024.md) Exs. 5.6–5.7 (arXiv v1)
run Chen & Wu's two configurations again, on $[-0.5,0.5]^2$ (their text;
the Fig. 6 caption says $[0,1]^2$) with $400\times400$ cells to $t=0.4$,
Ex. 5.7 cited to Wu & Tang, with their physical-constraint-preserving
finite-volume [Hermite WENO](/methods/hermite-weno.md). On the first
two reflected curved shocks and a mushroom structure form and few cells
are limited. The second serves to compare the scaling of the
eigenvectors in the [characteristic decomposition](/methods/characteristic-decomposition.md):
without rescaling, and with "unitization" ($c=\lvert l\rvert$ for an
eigenvector pair $(cr,l/c)$, page-local), serious oscillations appear;
the "matching" scaling $c=\sqrt{\lvert l\rvert/\lvert r\rvert}$, which makes
$\lvert l\rvert/c=c\lvert r\rvert$, is best (Remark 3.3, Fig. 7).

**Multispecies shock box.** [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md)
§3.3 (accepted manuscript) fill a $1000\times1000$ mm box with slip walls
with an O$_2$:N$_2$ = 1:3.76 mixture at $(\rho,p)=(1.225$ kg m$^{-3}$,
$101325$ Pa$)$ in the corner $x\le250$ mm, $y\le250$ mm and
$(4.9$ kg m$^{-3}$, $405300$ Pa$)$ elsewhere, a two-state relative of the
four-quadrant problems; base mesh $128\times128$ with three levels of
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md), CFL
0.8, $t=2$ ms on a distorted mapped mesh. Pressure and Mach number agree
with Owen et al., and the reflected shock is captured on the finest
level of the distorted mesh (Figs. 7–8).

[Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md) §5.2 run
an ideal-MHD four-state problem with the uniform field $B=(2,0,1)$ and
$(\rho,v_1,v_2,p)=(1,0.75,0.5,1)$ for $x>0,y>0$, $(2,0.75,0.5,1)$ for
$x<0,y>0$, $(1,-0.75,0.5,1)$ for $x<0,y<0$, $(3,-0.75,-0.5,1)$ for
$x>0,y<0$, on $[-1,1]^2$ with $400\times400$ cells to $t=0.8$. Its
hydrodynamic states are those of the four-contact configuration above
except the sign of $v_2$ in the first quadrant ($0.5$ against $-0.5$)
*(compiler check, not in the sources)*. With the
constrained transport step of their
[unstaggered central scheme](/methods/unstaggered-central-scheme.md) the
discrete divergence of $B$ stays at the $10^{-14}$ level, without it it
reaches $O(1)$, while the density is visually the same (Figs. 4–5); see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).

## Qualifications

- Boscarino et al. print an unmatched parenthesis in the
  configuration-3 data, "(0.5323, 1.206, 0, 0.3))" (Eq. (5.6)).
- Deng compares with WENO-JS5 results "in [65]", a reference on an
  improved third-order WENO-Z scheme.
- The configuration-3 runs differ in split, domain and final time
  ($t=0.3$ to $1$), so the jet is at different stages of development in
  different papers; only the runs with split $(0.8,0.8)$ on $[0,1]^2$
  and $t=0.8$ (Deng, Huang et al., Wang et al. 2023b, Wang et al. 2021,
  the two Chamarthi papers, Zhou et al., Zhong et al., Zuo & Zhu 2024a) are directly comparable.
- Li, Duan & Tang's Ex. 5.4 says its monitor function and linear
  weights are those of Ex. 5.2, which states no linear weights; the
  non-default weights $(0.95,0.045,0.005)$ are set in Ex. 5.3.
- Yu & Hesthaven assign the first state $(0.5313,0,0,0.4)$ to
  "$0.5<x<1$, $0.5<y<1.5$" on their tiled domain, while the other states
  occupy $0.5\le x<1.5$ or $0.5\le y<1.5$; read literally, the strip
  $1\le x<1.5$, $0.5<y<1.5$ would take the "otherwise" state
  $(0.8,0,0,1)$ and break the tiling that their other states and the
  configuration-12 data of Takagi et al. and Pazner define, so the
  printed range is inconsistent with the tiling, which needs
  $0.5<x<1.5$.
- Evidence is visual throughout.

# Citations

- [Deng (2023)](/sources/deng-2023.md) — App. A.10, Figs. 24, 35.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.6, Eq. (6.8).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — §4, Example 5, Fig. 5.
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §5.3.2, Fig. 14.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.2, Ex. 5, Fig. 5.5 (arXiv v2).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.8, Figs. 18–19.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.11, Ex. 5.15, Figs. 10–11 (arXiv v1).
- [Fu (2023)](/sources/fu-2023.md) — §3.4, Fig. 7 (reproduced).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Example 4, Table 9 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §X.b, Table XIV.
- [Wang et al. (2021)](/sources/wang-2021.md) — Example 5.6, Fig. 5.12.
- [Pazner (2021)](/sources/pazner-2021.md) — §5.5–5.6, Figs. 11–12 (arXiv v1).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Ex. 5.3–5.4, Table 5.1 (arXiv v1).
- [Kanbar, Touma & Klingenberg (2022)](/sources/kanbar-2022.md) — §5.2, Figs. 4–5 (arXiv v1).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.1, Eq. (5.7), Fig. 12.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Exs. 4.6–4.7, Figs. 10–11 (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — Exs. 6.2–6.4, Figs. 6.5–6.7 (arXiv v1).
- [Peng, Atkins & Deiterding (2022)](/sources/peng-2022.md) — §3.3, Figs. 7–8 (accepted manuscript).
- [Boscarino et al. (2022)](/sources/boscarino-2022.md) — §5, Ex. 5.4, Eq. (5.6), Figs. 5.4–5.5 (arXiv v2).
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.7, Fig. 15; §6, Table 4.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4.6, Figs. 16–18.
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.7, Fig. 10 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.9, Fig. 12, Table 2 (arXiv v1).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.6, Eq. (41), Fig. 16.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — App. A.3, Fig. 13.
- [Zhong et al. (2023)](/sources/zhong-2023.md) — §4.4, Exs. 13–14, Figs. 15–19.
- [Tang (2024)](/sources/tang-2024.md) — §4.4.2, Eq. (34), Fig. 11, Table 6.
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — Remark 3.3; Exs. 5.6–5.7, Figs. 6–7 (arXiv v1).
- [Zuo & Zhu (2024a)](/sources/zuo-2024.md) — Ex. 3.5, Figs. 3.6–3.7, Table 3.1.
- [Chudzik et al. (2024)](/sources/chudzik-2024.md) — §7, Ex. 7.4, Fig. 24.
