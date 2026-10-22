---
type: Benchmark
title: "High-Mach astrophysical jets"
description: "Mach 80 and Mach 2000 gas jets injected into a light ambient medium, and their relativistic and MHD relatives; near-vacuum, extreme-Mach-number robustness tests that most high-order schemes pass only with a positivity- or invariant-domain-preserving limiter."
status: established
aliases: [Mach 2000 jet, Mach 80 jet, astrophysical jet, high Mach number jet]
tags: [benchmark, positivity, bound-preserving, relativistic, mhd]
timestamp: 2026-10-21T12:00:00Z
---

# High-Mach astrophysical jets

A dense, fast gas jet is injected through a narrow slot into a lighter
ambient gas at the same pressure. With injection speed 800 the jet Mach
number is about 2000, with speed 30 it is about 80; the bow shock, the
contact surface and the cocoon then sit next to regions of nearly zero
density and pressure, and in the Mach 2000 jet the kinetic energy per unit volume of the
injected gas exceeds its internal energy by a factor of about
$2.6\times10^6$ *(compiler check, not in the sources)*. Pressure, a small difference of large
energies, can then leave $G=\{\rho>0,\ p>0\}$, and the sources use the
test as a demonstration of
[bound preservation](/properties/bound-preservation.md); the amount of
small-scale structure in the shear layer is a secondary, visual
measure of resolution.

## The Euler jets

Common data ($\gamma=5/3$), printed by [Fu (2021)](/sources/fu-2021.md)
§5.7.3 and [Takagi et al. (2022)](/sources/takagi-2022.md) §4.9, both
citing Zhang & Shu's positivity-preserving DG paper for it (their refs.
[76] and [74]; Rueda-Ramírez et al. attribute the Mach 2000 jet to Ha et
al., Wang & Don take the setup from Gao et al.), in $(\rho,v_1,v_2,p)$:

- **Mach 80:** domain $[0,2]\times[-0.5,0.5]$, ambient $(0.5,0,0,0.4127)$,
  jet inflow $(5,30,0,0.4127)$ through $|y|\le0.05$ on the left boundary
  (Takagi et al.: $(5,0,0,0.4127)$ on the rest of that boundary).
- **Mach 2000:** domain $[0,1]\times[-0.25,0.25]$, the same ambient state,
  jet inflow $(5,800,0,0.4127)$; outflow on the other boundaries.

The jet sound speed is $c=\sqrt{\gamma p/\rho}=\sqrt{(5/3)(0.4127)/5}=0.371$,
so the jet Mach numbers are $30/0.371=80.9$ and $800/0.371=2156.9$
*(compiler check, not in the sources)*.
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.2.3 print the same value: Mach 2156.91 with respect to the jet sound
speed and 682.08 with respect to the ambient one.

| Source | Scheme | Grid | Final time | Positivity treatment |
|---|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.7.3 | [TENO-AA](/methods/adaptive-teno.md), LLF | Mach 80: $448\times224$; Mach 2000: $800\times400$ | not printed | positivity-preserving flux limiter |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.9 | [TENO-THINC](/methods/teno-thinc.md), TENO5, WENO5-Z | $800\times400$, CFL 0.35 | not stated | positivity-preserving flux limiter |
| [Fu (2023)](/sources/fu-2023.md) Fig. 5 | TENO10 (review, reproduced) | $448\times224$, $800\times400$ | — | positivity-preserving limiter |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.4 | [affine-invariant WENO-Z/D](/methods/affine-invariant-weno.md) | setup from Gao et al. (not reproduced) | — | PP limiter needed |
| [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) §5.2.3 | [DGSEM](/methods/dgsem.md), $N=3$, [subcell IDP limiting](/methods/subcell-finite-volume-limiting.md) | $[-0.5,0.5]^2$, $256^2$ elements | $10^{-3}$ | bar-state bounds |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.18 | [OEDG](/methods/oedg.md), third order | $320\times160$ | $0.001$ | none mentioned |

Rueda-Ramírez et al. run the Mach 2000 jet on the square
$[-0.5,0.5]^2$ with inflow at $x=-0.5$, periodic top and bottom and
characteristic inflow/outflow left and right, a different box from the
$[0,1]\times[-0.25,0.25]$ of the other sources.

## Findings across sources

**A positivity limiter is needed by most schemes.** Fu (2021) computes
both jets with LLF and the positivity-preserving flux limiter; Takagi
et al. use the same kind of limiter for all three schemes they compare;
Fu (2023) presents the TENO10 jet as an example of near-vacuum robustness
"with the PP limiter". Wang & Don state that their affine-invariant
schemes are not positivity preserving in general and need a PP limiter
on the Mach 2000 jet; at the final time it is active only around the jet
front and the two inlet corners (§3.2.4, Fig. 8). Rueda-Ramírez et al.
make DGSEM robust by blending with a low-order finite-volume scheme up
to invariant-domain-preserving bar-state bounds, element-wise or
subcell-wise (Figs. 8–9).

**An exception without a stated limiter.** Peng, Sun & Wu compute the
Mach 2000 jet with OEDG on $320\times160$ to $t=0.001$ and report no
nonphysical oscillations; the paper neither claims bound preservation
nor mentions a positivity limiter, and says only that the results agree
with earlier ones (Ex. 5.18, Fig. 14). Whether OEDG alone keeps $\rho$
and $p$ positive here is not established by the source.

**Resolution.** Takagi et al. rank TENO-THINC, then TENO5, then WENO5-Z
by small-scale structure and claim TENO-THINC beats earlier WENO5-JS and
DG results (Fig. 20). Fu (2021) claims "much richer small-scale
structures" than fifth- and seventh-order WENO and a DG scheme (Figs.
11–14). Rueda-Ramírez et al. find that the low-order partner matters:
going from first-order FV with LLF, to first-order FV with HLLE, to
second-order FV with HLLE sharpens shocks and develops finer scales,
and subcell-wise blending beats element-wise blending. The second-order
and HLLE partners are not guaranteed to satisfy the bar-state bounds;
the authors keep the bounds and the blending returns the solution
closest to them (§5.2.3).

## Relativistic and MHD variants

- **Axisymmetric relativistic jet.** [Cui, Ding & Wu (2024)](/sources/cui-2024.md)
  Example 5: special-relativistic hydrodynamics in cylindrical $(r,z)$
  coordinates with a geometric source, $\gamma=5/3$, domain
  $[0,15]\times[0,45]$, $240\times720$ cells; ambient
  $(\rho,v_1,v_2,p)=(0.01,0,0,0.000170304823218172071)$, jet
  $(0.01,0,0.99,\text{same }p)$ through $r\le1$ at $z=0$; reflective
  symmetry axis, outflow elsewhere; classical Mach 6, relativistic Mach
  about 41.95; $t=100$. The DG code breaks down without the
  bound-preserving limiter; with the
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
  the $\mathbb P^4$ run takes 297.26 h against 414.19 h for the classic
  decomposition (Table 10).
- **Two-component MHD jet.** [Wu & Shu (2023)](/sources/wu-2023-b.md)
  Ex. 7.2: two-component ideal MHD, domain $[-0.5,0.5]\times[0,1.5]$,
  ambient $(\rho,p)=(0.14,1)$, inflow $(\rho,p)=(1.4,1)$ with
  $v=(0,800,0)$ through $|x|<0.05$ at $y=0$, magnetic field
  $B=(0,\sqrt{4000},0)$; $200\times600$ cells on the half domain; output
  at $t=0.001$, $0.0015$, $0.002$. The run fails without any one of the
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md), the locally
  [divergence-free](/properties/divergence-free-magnetic-field.md) basis
  or the discretized Godunov-symmetrization source term, which the
  paper's [geometric quasilinearization](/methods/geometric-quasilinearization.md)
  analysis shows is needed for provable bound preservation, even with a
  WENO limiter; this failure is stated in text, without a
  figure.

## Qualifications

- Fu (2021) and Takagi et al. do not print the final times of the jets;
  the sources that do (Rueda-Ramírez et al., Peng et al.) use
  $t=10^{-3}$ for Mach 2000.
- Resolution claims are visual comparisons, partly against figures
  from other papers.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.7.3, Figs. 11–14 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9, Fig. 20.
- [Fu (2023)](/sources/fu-2023.md) — §3.1, Fig. 5 (reproduced).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.4, Fig. 8.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.2.3, Figs. 8–9 (arXiv v2).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.18, Fig. 14 (arXiv v1).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Example 5, Table 10 (arXiv v1).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Ex. 7.2, Fig. 6 (arXiv v1).
