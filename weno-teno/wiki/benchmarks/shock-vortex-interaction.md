---
type: Benchmark
title: "Shock–vortex interaction"
description: "An isentropic vortex advected through a stationary Mach 1.1 shock on [0,2]×[0,1]; the reference setup tests the resolution of the shocked vortex through pressure profiles against fine-grid references, and amplified or non-Euler variants test bound preservation and non-conservative multiphase schemes."
status: established
aliases: [shock–vortex, vortex–shock interaction, shock/vortex interaction]
tags: [benchmark, weno, dg, bound-preserving, multiphase]
timestamp: 2026-10-21T12:00:00Z
---

# Shock–vortex interaction

A stationary normal shock of Mach number $M=1.1$ stands at $x=0.5$ in
the box $[0,2]\times[0,1]$, and an isentropic vortex centred at
$(0.25,0.5)$ in the supersonic stream upstream of it is carried through
the shock. Profiles of pressure along $y=0.5$ after the
interaction, against a fine-grid reference, measure how well a scheme
resolves it. With an amplified
vortex the same configuration becomes a near-vacuum test for
[bound preservation](/properties/bound-preservation.md).

## Reference setup

[Li et al. (2022)](/sources/li-2022-b.md) §4.4.2, Eq. (46),
[Huang et al. (2026)](/sources/huang-2026.md) §6.10,
[Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.16 and
[Cui, Ding & Wu (2024)](/sources/cui-2024.md) Example 3 print the same
construction. The upstream state is
$(\rho,v_1,v_2,p)=(1,\,1.1\sqrt\gamma,\,0,\,1)$, so that the stream
moves at Mach 1.1 into the stationary shock; the downstream state
follows from the Rankine–Hugoniot conditions; $\gamma=1.4$. Let
$\mathcal E$ be the vortex strength, $\mathcal A$ its decay rate, $r_c$
its critical radius, $(\bar x,\bar y)$ the position relative to the
vortex centre, $r$ its distance and $T=p/\rho$ (page-local symbols). The
vortex perturbs the upstream state by

$$
(\delta v_1,\delta v_2)=\frac{\mathcal E}{r_c}\,e^{\mathcal A(1-r^2/r_c^2)}\,(\bar y,\ -\bar x),\qquad
\delta T=-\frac{(\gamma-1)\mathcal E^2}{4\mathcal A\gamma}\,e^{2\mathcal A(1-r^2/r_c^2)},\qquad
\delta s=0 .
$$

Li et al. and Huang et al. write the velocity as
$\mathcal E\,(r/r_c)\,e^{\mathcal A(1-r^2/r_c^2)}(\sin\theta,-\cos\theta)$
with $\theta$ the polar angle about the centre, which is the same field,
since $(r/r_c)\sin\theta=\bar y/r_c$ *(compiler check, not in the
sources)*.

| Source | $\mathcal E$ | $\mathcal A$ | $r_c$ | Grid | Final time | Scheme |
|---|---|---|---|---|---|---|
| [Li et al. (2022)](/sources/li-2022-b.md) §4.4.2 | 0.3 | 0.204 | 0.05 | $200\times100$; reference $2000\times1000$ WENO7-Z | 0.6 | [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.10 | 0.3 | 0.204 | 0.05 | $h=1/100$; fine-mesh WENO5-JS reference | not printed | [ROUND, LD-ROUND](/methods/round-scheme.md) vs WENO3-NN, WENO5-JS |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.16 | 0.3 | 0.204 | 0.05 | $400\times200$, reflective top and bottom | 0.8 | [OEDG](/methods/oedg.md) |
| [Cui, Ding & Wu (2024)](/sources/cui-2024.md) Example 3 | 1.378106 | 0.204 | 0.4 | $450\times225$, $\mathbb P^2$ and $\mathbb P^4$ DG | 0.6 (pressure at 0.2, 0.35, 0.6) | bound-preserving DG with [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md) |

## Findings across sources

**Resolution of the transmitted vortex.** Li et al. find WENO-ZN
closest to the $2000\times1000$ reference in pressure along $y=0.5$
(Fig. 8). Huang et al. find ROUND more accurate at the shock front than
WENO3-NN and WENO5-JS, and LD-ROUND most accurate near $x\approx0.55$,
capturing the lowest pressure near $x\approx0.95$ (Fig. 15). Peng et
al. use the test as a robustness check and report no nonphysical
oscillations (Fig. 12).

**Low-density stress test.** Cui, Ding & Wu enlarge the vortex
($r_c=0.4$) and its strength so that the minimum density is
$4.7\times10^{-15}$ and the minimum pressure $8.8\times10^{-21}$. The
DG code breaks down without the bound-preserving limiter; a WENO
limiter in troubled cells is applied before it. With the limiter all
three cell-average decompositions give comparable solutions, and the
optimal one allows larger time steps: for $\mathbb P^4$, 1299.55 min
(optimal), 1327.45 min (quasi-optimal) and 1772.26 min (classic) to
$t=0.6$ (Table 8).

## Non-conservative variants

[Balsara et al. (2024)](/sources/balsara-2024.md) introduce three new
shock–vortex tests for systems with non-conservative products, computed
with their [FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md):
a Baer–Nunziato vortex crossing a standing shock on the diagonal
$x+y=0.5$ of $[-0.5,1.5]^2$ (§IX.b, Table X, Fig. 12, $600\times600$,
$t=0.84$), and two-layer shallow-water and debris-flow vortices crossing
a diagonal bore (§IX.d and §IX.f, Tables XI–XII, Figs. 14 and 16,
$600\times600$, $t=0.24$). The vortices are the smooth equilibrium
vortices used in their convergence tests, advected with the pre-shock
velocity; the authors attribute their survival through the shock to
conservation of angular momentum, a physical interpretation rather than
a numerical result.

## Qualifications

- Cui, Ding & Wu print the Rankine–Hugoniot pressure ratio as
  $1+\frac{2\gamma}{\gamma+1}(M^2+1)$; the Rankine–Hugoniot pressure
  ratio is $1+\frac{2\gamma}{\gamma+1}(M^2-1)$, which gives $1.245$ at
  $M=1.1$ *(compiler check, not in the sources)*. Their density and
  velocity ratios agree with the Rankine–Hugoniot ones *(compiler
  check)*.
- Huang et al. do not print the final time, so their pressure profiles
  cannot be placed against those of Li et al. ($t=0.6$) and Peng et al.
  ($t=0.8$).
- Balsara et al. write "by an intermediate time of $t=0.6$" in §IX.f
  where the run ends at $t=0.24$ and the figures are at $0.06$; $0.06$ is
  meant.

# Citations

- [Li et al. (2022)](/sources/li-2022-b.md) — §4.4.2, Eq. (46), Fig. 8.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.10, Fig. 15.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.16, Fig. 12 (arXiv v1).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Example 3, Table 8 (arXiv v1).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.b, §IX.d, §IX.f, Tables X–XII.
