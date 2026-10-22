---
type: Benchmark
title: "Brio–Wu MHD shock tube"
description: "One-dimensional ideal-MHD Riemann problem with a constant normal field and a reversing transverse field, whose solution contains a compound wave; used to validate MHD Riemann solvers, continuous finite elements with residual viscosity and unstaggered central schemes, in 1D and on 2D grids."
status: established
aliases: [Brio–Wu problem, Brio–Wu tube, MHD shock tube, Brio and Wu shock tube]
tags: [benchmark, mhd, riemann-solver, central-scheme]
timestamp: 2026-10-23T10:00:00Z
---

# Brio–Wu MHD shock tube

The Brio–Wu problem is the MHD analogue of the
[Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md): two uniform
states at rest, Sod's density and pressure jump, a constant normal
magnetic field $B_1$ and a transverse field $B_2$ that reverses sign
across the initial discontinuity. The reversal of $B_2$ produces, among
the waves, a compound wave that a scheme must capture without spurious
oscillation; the three sources use it to validate MHD Riemann solvers
and shock capturing for ideal MHD. Velocities are $v=(v_1,v_2,v_3)$
and the field $B=(B_1,B_2,B_3)$ in the notation of the registry.

## Setup as printed

| Source | Domain | Left state | Right state | $\gamma$ | $t$ |
|---|---|---|---|---|---|
| [Dao & Nazarov (2022)](/sources/dao-2022.md) §5.2 | $[0,1]$, jump at $x=0.5$ | $(\rho,v_1,p,B_1,B_2)=(1,0,1,0.75,1)$ | $(0.125,0,0.1,0.75,-1)$ | 2 | 0.2 |
| [Kanbar et al. (2022)](/sources/kanbar-2022.md) §5.1 | $[-1,1]^2$, jump at $x=0$ | $(\rho,v_1,v_2,v_3,B_2,B_3,p)=(1,0,0,0,1,0,1)$, $B_1=0.75$ | $(0.125,0,0,0,-1,0,0.1)$, $B_1=0.75$ | not printed | 0.25 |
| [Lesur et al. (2023)](/sources/lesur-2023.md) §4.2 | 1D | "as Mignone et al. (2007)", not reprinted | — | 5/3 | not printed |

Dao & Nazarov and Kanbar et al. print the same states; their final times
differ (0.2 on $[0,1]$, 0.25 on a domain twice as wide). Lesur et al.
state $\gamma=5/3$, while Dao & Nazarov print $\gamma=2$: the sources
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

## Related problems

The same sources follow the tube with two-dimensional MHD tests: the
[Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (Dao & Nazarov,
Lesur et al.), the [rotor](/benchmarks/mhd-blast-wave.md) (Dao &
Nazarov, Lesur et al.) and a four-state MHD Riemann problem (Kanbar et
al., recorded on
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md)).

## Qualifications

- No source reports an error norm; all comparisons are visual, against
  a reference code (Athena, PLUTO) or against the literature.
- All three sources are read in arXiv versions (v1), not the versions of
  record. Kanbar et al. print no $\gamma$ for any test; Lesur et al. do
  not reprint the data.

# Citations

- [Dao & Nazarov (2022)](/sources/dao-2022.md) — §5.2, Fig. 2 (arXiv v1).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §5.1, Fig. 3 (arXiv v1).
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §4.2, Fig. 6 (arXiv v1).
