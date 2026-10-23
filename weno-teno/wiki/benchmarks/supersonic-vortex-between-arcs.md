---
type: Benchmark
title: "Supersonic vortex between concentric arcs"
description: "Steady isentropic, irrotational supersonic flow between two concentric circular arcs with an exact smooth solution; it measures the order of accuracy of boundary treatments on curved slip walls, where straight-sided meshes, ghost cells and inexact boundary gradients reduce unstructured finite-volume and DG schemes to first or second order."
status: established
aliases: [supersonic vortex, isentropic supersonic vortex, supersonic vortex flow, vortex between concentric arcs, quarter-annulus supersonic vortex]
tags: [benchmark, finite-volume, dg, immersed-boundary, boundary-conditions]
timestamp: 2026-10-23T23:45:00Z
---

# Supersonic vortex between concentric arcs

Between two concentric circular arcs of radii $r_i<r_o$ (page-local, as all symbols of this
paragraph), an inviscid gas turns in a steady, isentropic and irrotational vortex whose speed
is inversely proportional to the radius, $\lvert v\rvert=c_iM_i\,r_i/r$, with $c_i$ and $M_i$
the sound speed and Mach number on the inner arc. Constant entropy and constant total enthalpy
give the density in closed form,

$$\rho(r)=\rho_i\Big[1+\frac{\gamma-1}2M_i^2\Big(1-\frac{r_i^2}{r^2}\Big)\Big]^{1/(\gamma-1)},\qquad p=\frac{\rho^\gamma}{\gamma},$$

(the density as printed by [Wei et al. (2023)](/sources/wei-2023.md), Eq. (38); the pressure as
printed by Ciallella et al., Eq. (39), which Wei et al.'s inner-arc value $p=1/\gamma$ matches).
Both sources use $r_i=1$, $r_o=1.384$, $\rho_i=1$ and $M_i=2.25$, so the flow is supersonic
everywhere; Wei et al. state $\gamma=1.4$, Ciallella et al. do not print $\gamma$. In Wei et
al.'s setup the arcs are slip walls and the inflow and outflow sections are the straight
radial segments of a quarter annulus, the inlet at the top and the outlet at the bottom. Because the solution is smooth and known everywhere,
the test isolates the error that a boundary treatment of a curved wall adds: the flow is
tangent to a curved wall, so a straight-sided boundary face or a mirror ghost state with the
face normal is not consistent with the wall to more than first or second order.

## Setups

| Source | Scheme | Meshes | Boundary conditions | Measured |
|---|---|---|---|---|
| Wei et al. (2023) §7.1 | second-order cell-centred unstructured FV, weighted least-squares gradients, LU-SGS at CFL 50 | five regular triangular grids, $11\times4$ to $176\times64$ points | inlet at the top fixed to the exact solution, supersonic outlet at the bottom, slip walls on both arcs | $L_\infty$ relative errors of $\rho$ and $p$ near the wall, $L_2$ over the field; CPU time over 700 steps |
| [Ciallella et al. (2024)](/sources/ciallella-2024.md) §6.2 | modal ADER-DG $P_1$–$P_3$ on triangles | four conformal straight-sided meshes, 92 to 6016 triangles, $h=0.150$ to $0.0187$ (Table 8) | Dirichlet on the inner arc, slip wall on the outer arc | $L_2$ errors and orders, uncorrected vs ROD-ADER-DG with curved slip-wall conditions |

## Findings across sources

**Uncorrected boundary treatments lose order.** On Wei et al.'s grids only their ghost-cell
constrained gradient (WLSQ-GCC) is second order near the boundary; the vertex-neighbour
stencil, the symmetric and curvature-corrected ghost cells and Haselbacher's constrained least
squares all drop to first order, with the error maximum in the corner cell that joins the inlet
or the outlet to a wall (§7.1, Figs. 13–15; see
[unstructured gradient reconstruction](/methods/unstructured-gradient-reconstruction.md)).
Ciallella et al.'s DG with the classical reflecting state on the straight outer faces
converges at rates below 2 (about 1.5 for $P_1$ and $P_2$, 1.1–1.25 for $P_3$), its errors
**increase** with the polynomial degree on a given mesh, and $P_3$ on the coarsest mesh stops
before the final time (Table 9); the authors connect this to the known growth of spurious
errors with the order for reflecting conditions on linear meshes.

**Boundary reconstruction restores accuracy, but not the full order with slip walls.** With
their space-time Reconstruction for Off-site Data and the curved slip-wall conditions
$v_n=0$, $\partial_ns=0$, $\partial_nH=0$, $\partial_nv_\tau=v_\tau\kappa_{\mathrm w}$ (normal
and tangential velocity $v_n$, $v_\tau$, wall curvature $\kappa_{\mathrm w}$, page-local; their
Eq. (21)), Ciallella et al. obtain errors several orders of magnitude below the uncorrected
ones, lower by at least one order per degree increase; the observed order is about $N$ rather
than $N+1$, which they attribute to the derivatives of the polynomial in the Neumann and Robin
conditions (§6.2, Table 10; see [ADER schemes](/methods/ader-scheme.md),
[immersed boundary methods](/methods/immersed-boundary-method.md)). Their finest-level rates
are 2.04–2.11 for $P_1$, 2.07–2.09 for $P_2$ and 2.40–2.57 for $P_3$, whose rate falls from
3.12–3.68 at the previous level.

**Cost.** Wei et al.'s constrained gradient adds 6.8% total CPU time over 700 steps on a grid
with 5.4% boundary cells, with at most two secant iterations per boundary cell (Table 4).

## Qualifications

- Ciallella et al. print the density with the factor $\frac{\gamma+1}2$ in place of
  $\frac{\gamma-1}2$ (Eq. (38)). Their own Eq. (39), $\lvert v\rvert=c_iM_i/r$ and $p=\rho^\gamma/\gamma$
  (so $c^2=\rho^{\gamma-1}$), with constant total enthalpy gives the factor $\frac{\gamma-1}2$, the
  form Wei et al. print; at $r=r_o$ with $\gamma=1.4$ the printed factor would give $\rho\approx30.1$ instead of
  $\rho\approx2.68$ *(compiler check, not in the sources)*.
- Ciallella et al.'s statement that the order with slip walls is "$M$ rather than $M+1$"
  (their $M$ is the degree $N$) matches $P_2$ at the finest level, but $P_1$ still converges at
  about $N+1=2$ and $P_3$ at 2.4–2.6, below $N=3$ (Table 10).
- Wei et al. impose the ghost-cell (GC) variant with a weak Riemann boundary flux and the
  others with a weak prescribed flux, so their comparison mixes two impositions (§7.1).
- Neither source prints the final time or, in Ciallella et al.'s case, the CFL number.

# Citations

- [Wei et al. (2023)](/sources/wei-2023.md) — §7.1, Eq. (38), Table 4, Figs. 12–15.
- [Ciallella et al. (2024)](/sources/ciallella-2024.md) — §4.2 (Eq. (21)), §6.2, Eqs. (38)–(39), Tables 8–10 (arXiv v1).
