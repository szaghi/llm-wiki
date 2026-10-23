---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "One-dimensional ideal-MHD Riemann problem with a constant normal field and a reversing transverse field, whose solution contains a compound wave; used to validate MHD Riemann solvers, continuous finite elements, unstaggered central schemes, positivity-filtered DG, all-Mach IMEX WENO, a one-step HLL-GRP finite-volume scheme, and, in a relativistic two-fluid variant, entropy-stable finite differences."
status: established
aliases: [Brio–Wu problem, Brio–Wu tube, MHD shock tube, Brio and Wu shock tube]
tags: [benchmark, mhd, riemann-solver, central-scheme, relativistic]
timestamp: 2026-10-23T20:00:00Z
---

# Brio–Wu MHD shock tube

The Brio–Wu problem is the MHD analogue of the
[Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md): two uniform
states at rest, Sod's density and pressure jump, a constant normal
magnetic field $B_1$ and a transverse field $B_2$ that reverses sign
across the initial discontinuity. The reversal of $B_2$ produces, among
the waves, a compound wave that a scheme must capture without spurious
oscillation; the sources use it to validate MHD Riemann solvers
and shock capturing for ideal MHD, and one runs a relativistic
two-fluid version of it. Velocities are $v=(v_1,v_2,v_3)$
and the field $B=(B_1,B_2,B_3)$ in the notation of the registry.

## Setup as printed

| Source | Domain | Left state | Right state | $\gamma$ | $t$ |
|---|---|---|---|---|---|
| [Dao & Nazarov (2022)](/sources/dao-2022.md) §5.2 | $[0,1]$, jump at $x=0.5$ | $(\rho,v_1,p,B_1,B_2)=(1,0,1,0.75,1)$ | $(0.125,0,0.1,0.75,-1)$ | 2 | 0.2 |
| [Kanbar et al. (2022)](/sources/kanbar-2022.md) §5.1 | $[-1,1]^2$, jump at $x=0$ | $(\rho,v_1,v_2,v_3,B_2,B_3,p)=(1,0,0,0,1,0,1)$, $B_1=0.75$ | $(0.125,0,0,0,-1,0,0.1)$, $B_1=0.75$ | not printed | 0.25 |
| [Lesur et al. (2023)](/sources/lesur-2023.md) §4.2 | 1D | "as Mignone et al. (2007)", not reprinted | — | 5/3 | not printed |
| [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) Ex. 5.3 | $[0,1]$, jump at $x=0.5$ | $(\rho,v_1,v_2,v_3,B_1,B_2,B_3,p)=(1,0,0,0,0.75,1,0,1)$ | $(0.125,0,0,0,0.75,-1,0,0.1)$ | 2 | 0.1 |
| [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.2 | $[0,1]$, jump at $x=0.5$ | $(\rho,v_1,v_2,B_1,B_2,p)=(1,0,0,0.75,1,1)$ | $(0.125,0,0,0.75,-1,0.1)$ | 2 | 0.1 |
| [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) §4.1 | $(-1,1)$, jump at $x=0$ | $(\rho,v_1,v_2,v_3,B_1,B_2,B_3,p)=(1,0,0,0,0.75,1,0,1)$ | $(0.125,0,0,0,0.75,-1,0,0.1)$ | 2 | 0.1 |

Dao & Nazarov, Kanbar et al., Chen, Wu & Xiong, Dzanic & Witherden and
Liu, Feng & Wang print the same states; their final times differ (0.2 on $[0,1]$ for Dao
& Nazarov, 0.1 on $[0,1]$ for Chen, Wu & Xiong and Dzanic & Witherden,
0.25 on a domain twice as wide for Kanbar et al., 0.1 on the domain
$(-1,1)$ for Liu, Feng & Wang). Chen, Wu & Xiong use
reflective boundaries; Dzanic & Witherden run it on a one-element-wide
2D quadrilateral mesh, Dirichlet left and right, periodic top and
bottom. Lesur et al.
state $\gamma=5/3$, while Dao & Nazarov, Chen, Wu & Xiong, Dzanic &
Witherden and Liu, Feng & Wang print $\gamma=2$: the sources
run the problem in two variants of the ratio of specific heats, and the
wave positions of one cannot be compared with those of the other. Both
Dao & Nazarov and Lesur et al. write MHD in units without $4\pi$
(magnetic pressure $\lvert B\rvert^2/2$); in those units the plasma beta
$2p/\lvert B\rvert^2$ of the printed states is $1.28$ on the left and
$0.128$ on the right *(compiler check, not in the sources)*. Kanbar et
al. describe the solution as having "seven discontinuities".

## Runs in the sources

**Continuous finite elements with residual viscosity.** Dao & Nazarov run
their explicit continuous Galerkin $\mathbb P_1$ and $\mathbb P_3$
discretization with residual-based
[artificial viscosity](/methods/artificial-viscosity.md) at 600 and 1200
degrees of freedom against an Athena reference on 10000 points (Fig. 2,
density with zooms). The compound wave is captured, and at equal degrees
of freedom $\mathbb P_3$ is sharper than $\mathbb P_1$. Boundary
conditions are not stated.

**Unstaggered central scheme on a 2D grid.** Kanbar et al. run the tube
in two dimensions with their second-order
[unstaggered central scheme](/methods/unstaggered-central-scheme.md)
(CFL 0.485, MC parameter 1.5) on 200, 400 and 800 points with the
constrained-transport correction and on one grid without it, and compare
cross sections of $\rho$, $v_1$, $v_2$, $B_1$, $B_2$, $p$ with the
literature, "very good" agreement (Fig. 3). The correction, which keeps
a centred discrete divergence of $B$ at zero (see
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)),
adds "a small smearing out effect". The overlay of three grids is
called a convergence study; no error is measured.

**Riemann solvers of a Godunov code.** Lesur et al. run the problem in
the [IDEFIX](/software/idefix.md) code with the Roe solver and linear
reconstruction on 500 points, against a PLUTO 4.3 Roe reference on 8000
points (Fig. 6). The test is one-dimensional and so validates the
Riemann solvers only, not the constrained-transport electromotive
forces. A small post-shock velocity oscillation remains, which they
ascribe to the reconstruction of primitive variables without
[characteristic decomposition](/methods/characteristic-decomposition.md).

**Positivity-preserving entropy filtering in DG.** Dzanic & Witherden run
nodal DG/flux reconstruction ($\mathbb P_3$, 200 and 400 elements,
$\Delta t=2\cdot10^{-4}$ and $10^{-4}$) with their MHD
[entropy filter](/methods/entropy-filtering.md), against a $\mathbb P_0$
reference on $5\cdot10^4$ elements (Fig. 2). Rarefactions and shocks are
resolved within an element without noticeable oscillations; minor
density oscillations remain between the compound wave and the contact,
with minor undershoots ahead of the contact.

**All-Mach IMEX WENO in the compressible regime.** Chen, Wu & Xiong run
their semi-implicit [IMEX](/methods/imex-runge-kutta.md) fifth-order
finite-difference WENO scheme with constrained transport at
$\varepsilon=1$ (their sonic Mach parameter, i.e. the fully compressible
regime) on $N=200$ against an explicit WENO reference on $N=2400$
(Fig. 5.1, $\rho$ and $B_2$), as the shock-capturing check of an
[asymptotic-preserving](/properties/asymptotic-preservation.md) scheme.

**One-step HLL-GRP finite volumes.** Liu, Feng & Wang run the tube as
the first test of their multidimensional finite-volume implementation of
the HLL [generalized Riemann problem](/methods/generalized-riemann-problem.md)
solver (one stage, second order in time), with locally divergence-free
[WLS-ENO](/methods/wls-eno.md) reconstruction of primitive variables, on
800 cells at CFL 0.8 on one core, against a forward-Euler HLL run on
2000 cells as reference (Fig. 3). The one-step HLL-GRP profiles and
those of a two-stage SSP-RK2 HLL scheme with the same reconstruction
"basically coincide".

**Relativistic two-fluid variant.** [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md)
(§6.1.2) solve the two-fluid relativistic plasma equations (ion and
electron relativistic fluids coupled to Maxwell's equations) on
$[-0.5,0.5]$ with Neumann boundaries, $\gamma=2$, $t=0.4$, left state
$(\rho_{\mathrm i},p_{\mathrm i},\rho_{\mathrm e},p_{\mathrm e},B_1,B_2)=(0.5,0.5,0.5,0.5,\sqrt\pi,\sqrt{4\pi})$ and
right state $(0.0625,0.05,0.0625,0.05,\sqrt\pi,-\sqrt{4\pi})$, charge-to-mass
ratios $r_{\mathrm i}=-r_{\mathrm e}=10^3/\sqrt{4\pi}$ (skin depth $10^{-3}/\sqrt{\rho_{\mathrm i}}$), and
stiff cases $10^4/\sqrt{4\pi}$ and $10^5/\sqrt{4\pi}$ (page-local
species subscripts $\mathrm i$, $\mathrm e$ and ratios $r_{\mathrm i}$, $r_{\mathrm e}$, as on the Source page). Their
[entropy-stable](/properties/entropy-stability.md) finite-difference
schemes of orders 2–4 ([TeCNO](/methods/tecno-scheme.md)-type
diffusion) give (Figs. 1–2, Table 4):

- at 400 cells roughly the single-fluid RMHD profile, and at 1600 and
  6400 cells the dispersive two-fluid waves; orders 3 and 4 show the
  dispersive effects already at 400 cells, order 4 better than order 3;
- almost the same entropy decay for explicit and IMEX time stepping of
  the same order, less entropy dissipated as the order rises;
- in the stiff cases on 400 cells, profiles close to RMHD that stay
  stable without resolving the small-scale oscillations;
- on 10 CPU cores at $r=10^5/\sqrt{4\pi}$ and 800 cells, 413.55 s
  explicit against 12.11 s IMEX at order 2, 374.54 s against 47.00 s at
  order 4; at $r=10^4/\sqrt{4\pi}$ and 800 cells IMEX is slower at orders
  3 and 4 (22.14 s against 13.04 s, 44.90 s against 37.98 s), faster at
  order 2 (14.28 s against 17.90 s).

## Related problems

The same sources follow the tube with two-dimensional MHD tests: the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (Dao & Nazarov,
Lesur et al., Chen, Wu & Xiong, Dzanic & Witherden, Liu, Feng & Wang,
Bhoriya et al. in its relativistic form), the [rotor](/benchmarks/mhd-blast-wave.md) (Dao &
Nazarov, Lesur et al., Liu, Feng & Wang), the [MHD blast wave](/benchmarks/mhd-blast-wave.md)
(Chen, Wu & Xiong, Dzanic & Witherden, Liu, Feng & Wang, Bhoriya et al.), the
[circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)
(Liu, Feng & Wang) and a four-state
MHD Riemann problem (Kanbar et al., recorded on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)).

## Qualifications

- Bhoriya et al. state that $\Delta x=0.0025$ at 400 cells is slightly
  larger than the skin depth "in the entire domain"; with their own
  formula the right state has skin depth $4\times10^{-3}>\Delta x$
  *(compiler check, not in the sources)*.
- No source reports an error norm; all comparisons are visual, against
  a reference code (Athena, PLUTO), a fine-grid run, a lower-order
  run (Liu, Feng & Wang's forward-Euler reference) or the literature.
- All sources except Liu, Feng & Wang (version of record) are read in
  arXiv versions (v1; Dzanic & Witherden v2, Bhoriya et al. v2), not the
  versions of record. Kanbar et al. print no $\gamma$ for any test; Lesur et al. do
  not reprint the data.

# Citations

- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §5.2, Fig. 2 (arXiv v1).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §5.1, Fig. 3 (arXiv v1).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.2, Fig. 6 (arXiv v1).
- [Chen, Wu & Xiong (2023)](/sources/chen-2023-b.md) — Ex. 5.3, Fig. 5.1 (arXiv v1).
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.2, Eq. (42), Fig. 2 (arXiv v2).
- [Bhoriya, Kumar & Chandrashekar (2023)](/sources/bhoriya-2023.md) — §6.1.2, Figs. 1–2, Table 4 (arXiv v2).
- [Liu, Feng & Wang (2023a)](/sources/liu-2023.md) — §4.1, Fig. 3.
