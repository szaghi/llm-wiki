---
type: Benchmark
title: "Shock–vortex interaction"
description: "An isentropic vortex advected through a stationary Mach 1.1 shock on [0,2]×[0,1]; the reference setup tests the resolution of the shocked vortex through pressure profiles against fine-grid references, and amplified, strong-vortex, relativistic or non-Euler variants test bound preservation, shock-capturing dissipation and non-conservative multiphase schemes."
status: established
aliases: [shock–vortex, vortex–shock interaction, shock/vortex interaction]
tags: [benchmark, weno, dg, bound-preserving, multiphase]
timestamp: 2026-10-22T20:00:00Z
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

### Variants of the Euler setup

- **Moving shock, same vortex.** [Yu & Hesthaven (2022)](/sources/yu-2022.md)
  §5.4.2 use the vortex parameters of the table ($\mathcal E=0.3$,
  $\mathcal A=0.204$, $r_c=0.05$) centred at $(2.25,2)$ (see
  Qualifications for their printed formula), with a different shock: on $[0,4]^2$,
  of which $[2,4]\times[1,3]$ is the physical region, the state
  $(1,\sqrt\gamma,0,1)$ on $1.5<x<2.5$ and, elsewhere, the state with
  $p_{\mathrm R}=1.3$ and density and velocity from their printed
  Rankine–Hugoniot formulas; $h=1/50$ triangles, output at $t=0.36$ and
  $0.8$. The formulas give $\rho_{\mathrm R}=1.2055$ and
  $v_{1,\mathrm R}=0.9571$, and the jump at $x=2.5$ is then a shock of
  relative Mach number 1.121 moving at speed $-0.143$, which satisfies
  the Rankine–Hugoniot conditions to round-off; the upstream stream is
  sonic in the laboratory frame, not at Mach 1.1 *(compiler check, not
  in the sources)*.
- **Strong shock and strong vortex.** [Sousa & Scalo (2022)](/sources/sousa-2022.md)
  §5.2 (arXiv v2), after Ellzey et al., Rault et al. and Tonicello et
  al., hold a shock at $x=L/2$ of $[0,2L]\times[0,L]$ against an inflow
  of speed $1.5$ times the upstream sound speed, and send through it a
  zero-circulation vortex centred at $(L/4,L/2)$ whose azimuthal speed
  grows linearly to $0.9$ times the inflow speed at $r=0.075L$ and
  decays to zero at $r=0.175L$, pressure from radial balance with the
  isentropic relation; inviscid, grids $192\times96$ to $768\times384$,
  snapshots at $tV_0/L=0.45$, $1.65$, $2.4$ ($V_0$ the inflow speed),
  and a sinusoidally distorted grid variant.
- **Relativistic.** [Chen & Wu (2022)](/sources/chen-2022-b.md)
  Ex. 4.10 (arXiv v1) pass their Lorentz-boosted
  [isentropic vortex](/benchmarks/isentropic-vortex.md) (speed $0.9$,
  strengths 5 and 10.0828) through a standing shock at $x=-6$ of
  $[-17,3]\times[-5,5]$, pre-shock $(\rho,v_1,v_2,p)=(1,-0.9,0,1)$,
  post-shock $(4.891497310766981,-0.388882958251919,0,11.894863258311670)$,
  $\gamma=1.4$, $h=1/40$ triangles, outflow at $x=-17$, reflection at
  $y=\pm5$, $t=19$. The printed post-shock state satisfies the
  relativistic Rankine–Hugoniot conditions of a standing shock to about
  $10^{-12}$ *(compiler check, not in the sources)*.

## Findings across sources

**Resolution of the transmitted vortex.** Li et al. find WENO-ZN
closest to the $2000\times1000$ reference in pressure along $y=0.5$
(Fig. 8). Huang et al. find ROUND more accurate at the shock front than
WENO3-NN and WENO5-JS, and LD-ROUND most accurate near $x\approx0.55$,
capturing the lowest pressure near $x\approx0.95$ (Fig. 15). Peng et
al. use the test as a robustness check and report no nonphysical
oscillations (Fig. 12).

Yu & Hesthaven stabilize the computation "with reasonable wiggles";
the vortex is well resolved and only marginally affected by the
artificial dissipation (§5.4.2, Figs. 13–15).

**Explicit dissipation and the strong vortex.** Sousa & Scalo find
that their [quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md)
and localized artificial diffusion both miss the asymmetric splitting of
the vortex on $192\times96$, are qualitatively right on $384\times192$
and converge to the same result; the quasi-spectral viscosity gives a
sharper shock and less noise on the two finer grids but underestimates
the core size of the top vortex after the shock on $384\times192$, and
it sustains the shock on the distorted grid (Figs. 6–7).

**Low-density stress test.** Cui, Ding & Wu enlarge the vortex
($r_c=0.4$) and its strength so that the minimum density is
$4.7\times10^{-15}$ and the minimum pressure $8.8\times10^{-21}$. The
DG code breaks down without the bound-preserving limiter; a WENO
limiter in troubled cells is applied before it. With the limiter all
three cell-average decompositions give comparable solutions, and the
optimal one allows larger time steps: for $\mathbb P^4$, 1299.55 min
(optimal), 1327.45 min (quasi-optimal) and 1772.26 min (classic) to
$t=0.6$ (Table 8). In Chen & Wu's relativistic run the
physical-constraint-preserving limiter is required for the strong
vortex, as it is for the vortex alone (Ex. 4.10, Figs. 15–16).

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
  check, not in the sources)*.
- Yu & Hesthaven print (Eq. (5.10)) $\delta v_1=\mathcal E\,\frac{\bar y}{r_c}e^{\mathcal A(1-r^2)}$
  and $\delta v_2=+\mathcal E\,\frac{\bar x}{r_c}e^{\mathcal A(1-r^2)}$
  with $r$ the unscaled distance to the centre. Taken literally the
  velocity is a strain field, not a rotation, and its Gaussian decays
  over a unit length instead of $r_c$; the form of the other sources
  has $-\bar x$ and $r/r_c$. The paper does not show which was run.
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
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.2, Figs. 13–15.
- [Sousa & Scalo (2022)](/sources/sousa-2022.md) — §5.2, Eqs. (58)–(60), Figs. 6–7 (arXiv v2).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.10, Figs. 15–16 (arXiv v1).
