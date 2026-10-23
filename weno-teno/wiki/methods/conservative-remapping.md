---
type: Method
title: "Conservative remapping for ALE schemes"
description: "Conservative remapping transfers cell averages from an old Lagrangian mesh to a rezoned mesh of the same topology in indirect ALE methods; the page records Gu et al.'s formulation as a moving-mesh solve of a trivial equation, its third-order multi-resolution WENO finite volumes, and its proved positivity under a cell-average decomposition."
status: established
aliases: [remapping, remap, conservative interpolation, ALE remapping, WENO remapping, P-WENO remapping, rezone and remap]
tags: [finite-volume, weno, positivity, bound-preserving, reconstruction]
timestamp: 2026-10-23T03:53:00Z
---

# Conservative remapping for ALE schemes

An indirect arbitrary Lagrangian–Eulerian (ALE) method alternates three
steps: a Lagrangian step, in which the mesh moves with the fluid; a
**rezone**, in which a less distorted mesh with the same number of cells
and the same connectivity is chosen; and a **remap**, in which the cell
averages $\bar u_i$ of the conserved variables are transferred from the
old mesh to the new one. The remap must conserve each integral
$\sum_i\lvert I_i\rvert\bar u_i$, keep the accuracy of the Lagrangian
scheme, create no oscillations, and keep the states in the admissible
set $G$ (§1 of the source below). [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md)
group the existing remaps into intersection-based methods, which
integrate the old reconstruction over the overlaps of old and new cells,
and transport- or flux-based methods, which advect the data from one mesh
to the other in a pseudo-time (§1). Their own method is of the second
kind.

## Remapping as a moving-mesh solve

Gu et al. solve the trivial equation $\partial_tu=0$ in a pseudo-time
$t\in[0,T_{\mathrm r}]$ (page-local: $T_{\mathrm r}$ is the final
pseudo-time) on a mesh whose nodes travel on straight lines from their
old positions at $t=0$ to the new ones at $t=T_{\mathrm r}$ (§2.1–2.2).
Let $v_{\mathrm g}$ denote the mesh (grid) velocity, page-local; it is
constant in time at every node,
$v_{\mathrm g}=(x^{T_{\mathrm r}}-x^0)/T_{\mathrm r}$, and linear along
each edge (Eqs. 2.3–2.4). Integrating over the moving control volume
$I_{i,j}(t)$ and applying the Reynolds transport and divergence
theorems turns the trivial equation into a linear conservation law with
flux $-v_{\mathrm g}u$ (Eq. 2.2):

$$\frac{d}{dt}\Big(\lvert I_{i,j}(t)\rvert\,\bar u_{i,j}(t)\Big)+\int_{\partial I_{i,j}(t)}\big(-v_{\mathrm g}u\big)\cdot n\,dl=0 .$$

The solution at $t=T_{\mathrm r}$ is the remapped field. The construction
needs no cell intersections and no bound on the node displacement: only
the topology of the two meshes must agree, so a node may move by more
than one cell (§1, §2). It applies to any polygonal mesh with matching
topology; only quadrilaterals are shown (§2.1).

**Choice of the pseudo-time.** Following the moving-mesh finite-volume
analysis of Klingenberg, Schnucke and Xia and of Li et al., which they
cite and do not re-prove, Gu et al. state that high-order accuracy
needs only boundedness, $\lvert v_{\mathrm g}\rvert\le C_0$, and Lipschitz
continuity, $\lvert\partial v_{\mathrm g}/\partial x\rvert\le C_{0,1}$,
of the mesh velocity, with constants independent of the mesh size; both
hold if $T_{\mathrm r}$ is large enough (§2.2; page-local $C_0$,
$C_{0,1}$, both set to 10). No formula for $T_{\mathrm r}$ is printed;
$T_{\mathrm r}$ "depends on the magnitude of the mesh movement" and
halves with the mesh size (§3.4). They set this against "most existing
transport equation based remapping methods in which the final
pseudo-time is fixed as a constant such as 1", and against transport
remaps that need a sufficiently smooth old-to-new mapping (§1, §3.4).

## Discretization

**Finite volumes on moving quadrilaterals** (§2.3). Each edge integral
is a three-point Gauss–Lobatto (Simpson) sum, chosen over Gauss
quadrature because it eases the positivity decomposition. The flux is
upwind on the sign of $v_{\mathrm g}\cdot n$:
$-v_{\mathrm g}u^{\mathrm{in}}$ when $v_{\mathrm g}\cdot n\le0$ and
$-v_{\mathrm g}u^{\mathrm{out}}$ otherwise, with $u^{\mathrm{in}}$,
$u^{\mathrm{out}}$ the traces from inside and outside the cell
(the source's $u^-$, $u^+$, here not the registry's left and right
states); the sign of the flux reverses the upwind direction with
respect to $v_{\mathrm g}$.

**Reconstruction** (§2.4). The third-order two-dimensional
[multi-resolution WENO](/methods/multi-resolution-weno.md) of Zhu and Shu:
the constant $\bar u_{i,j}$ on the cell itself, and a quadratic fitted by
constrained least squares on the $3\times3$ block of cells, constrained
to reproduce $\bar u_{i,j}$; linear weights $d_1=1/11$, $d_2=10/11$,
called "a good balance" between smooth-flow accuracy (larger $d_2$) and
oscillations. The [smoothness indicator](/definitions/smoothness-indicator.md)
of the quadratic is of Jiang–Shu type with area scaling (Eq. 2.6); that
of the constant, which Eq. (2.6) would set to zero, is replaced by
$\beta_1=\min\{\zeta_1+\zeta_2,\zeta_2+\zeta_3,\zeta_3+\zeta_4,\zeta_4+\zeta_1\}$,
with $\zeta_\ell$ the squared differences between $\bar u_{i,j}$ and its
four edge neighbours (page-local $\zeta_\ell$), because $\beta_1=0$ "does
lead to more smearing" at strong shocks and contacts. The nonlinear
weights are of [WENO-Z](/methods/weno-z.md) type,
$\alpha_k=d_k\big(1+(\tau/(\beta_k+\epsilon))^2\big)$ with
$\tau=\lvert\beta_2-\beta_1\rvert$ and $\epsilon=10^{-3}$. Because the
linear weights of multi-resolution WENO may be any positive numbers
summing to one, they need not be recomputed as the cells deform, which
the authors call "particularly suitable and efficient for the remapping
problem" (§1, §2.4).

**Time stepping** (§2.5). [SSP-RK3](/methods/ssp-runge-kutta.md) on the
products $\lvert I_{i,j}\rvert\bar u_{i,j}$, with the area at the second
stage taken as $\tfrac12(\lvert I_{i,j}^n\rvert+\lvert I_{i,j}^{n+1}\rvert)$
(Eq. 2.7). The step is $\Delta t=0.8\,h/\max\lvert v_{\mathrm g}\cdot n\rvert$,
$h$ the smallest inscribed-circle diameter of the cells, capped at $5h$
for temporal accuracy (Eq. 2.8).

## Positivity

For the Euler variables $u=(\rho,\rho v,E)$ the admissible set is
$G=\{\rho>0,\ \rho e>0\}$, with $\rho e=E-\tfrac12\rho\lvert v\rvert^2$
(§2.6.1). Gu et al. obtain [bound preservation](/properties/bound-preservation.md)
by the Zhang–Shu route.

- **First order.** The first-order upwind remap is positivity-preserving
  for $\Delta t\le\tfrac12\min_{i,j}\big[\lvert I_{i,j}\rvert/\big(\sum_k\lvert e_k\rvert\,\max_k\lvert v_{\mathrm g}\cdot n_k\rvert\big)\big]$,
  $\lvert e_k\rvert$ the edge lengths (page-local) (Theorem 2.1; proof referred to Cheng–Shu
  and Zhang–Shu).
- **High order.** Each cell is mapped to $[-\tfrac12,\tfrac12]^2$ and its
  average is decomposed on the $3\times3$ tensor Simpson points
  (quadrature weights $\mathsf w=\tfrac16,\tfrac23,\tfrac16$) with the
  Jacobian values of the map; the forward-Euler update then becomes a
  convex combination of interior point values and first-order updates
  of the boundary point values (Eq. 2.11). If $\bar u^n_{i,j}\in G$ and
  all nine point values lie in $G$, the update stays in $G$ for
  $\Delta t\le\frac{\mathsf w_1}{2}\cdot\frac12\min_{i,j}\big\{\lvert J\rvert_{i,j}/\big(\sum_k\lvert e_k\rvert\,\max_{k,m}\lvert v_{\mathrm g}\cdot n_k\rvert\big)\big\}$,
  $\mathsf w_1=\tfrac16$, with $\lvert J\rvert_{i,j}$ the smallest
  Jacobian value at the boundary points (Theorem 2.2, Eq. 2.12); SSP-RK3
  inherits it by convexity of $G$.
- **Limiter.** The point values are brought into $G$ by the
  [Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md),
  first for density, then for internal energy, at the nine points
  (§2.6.3).
- **In practice** the code runs at the larger step of Eq. (2.8) and,
  when a new average leaves $G$, repeats the step with $\Delta t/2$;
  Theorem 2.2 bounds the number of repetitions (Remark, §2.6.2).

## Evidence

All remap tests are on $[0,1]^2$, start from a uniform mesh and remap
$N=10$ times through a sequence of meshes back to the initial one, so
the error is $\bar u^N-\bar u^0$ (§3). "WENO" denotes the remap without,
"P-WENO" with the positivity limiter.

| Test (§3) | Mesh sequence | Result |
|---|---|---|
| $u=\sin^2(2\pi x)\sin^2(2\pi y)$ | smoothly moving | $L^1$ error $3.403\times10^{-2}$ ($20^2$) to $5.225\times10^{-6}$ ($320^2$), orders 2.67, 3.63, 2.99, 3.37 (Table 3.1) |
| same | randomly moving, node shifts up to a quarter of a cell per direction ($C_r=0.5$ times a random number in $[-0.5,0.5]$, page-local $C_r$) | $L^1$ orders 3.59, 4.20, 3.46, 3.73; WENO leaves 2.86 % of averages negative at $20^2$, 0.03 % at $320^2$; P-WENO none (Table 3.2) |
| same | "flipping": cell sizes reversed, nodes move more than one cell | WENO $L^1$ orders 2.48, 3.44, 3.08, 3.14, with up to 5.67 % negative averages; P-WENO 2.54, 3.42, 3.05, 3.13, none negative (Table 3.3) |
| piecewise data, values 10, 0.1 and a sinusoid | random, $80^2$ | no oscillations near the discontinuities (Fig. 6) |
| step of height 100; cylinder and cone | random $80^2$; flipping $160^2$ | WENO gives 13, 19 and 35 negative averages (smallest $-3.83\times10^{-4}$, $-1.88\times10^{-3}$); P-WENO none (Figs. 7–12) |

**Cost** (§3.4, Table 3.4). For a mild mesh motion (nodes within one
cell), each remap needs three pseudo-time steps at every resolution
from $20^2$ to $320^2$, because $T_{\mathrm r}$ and the step both halve
under refinement; the cost then scales with the cell count, 0.641 s to
69.47 s (WENO) and 0.641 s to 70.08 s (P-WENO). No hardware is stated.

**Inside an ALE code** (§3.5). With the third-order positivity-preserving
ENO Lagrangian scheme of Cheng and Shu, rezoning and P-WENO remapping
every 20 Lagrangian steps, the ALE runs are robust on the
[Sedov blast wave](/benchmarks/sedov-blast-wave.md) ($t=1$), the Saltzman
piston (to $t=0.925$; the pure Lagrangian run fails after $t=0.6$), the
[Noh implosion](/benchmarks/noh-implosion-problem.md) (to $t=0.6$; the
pure Lagrangian run fails after $t=0.54$), the
[Leblanc shock tube](/benchmarks/leblanc-shock-tube.md) ($t=6$) and a
two-material [Sod tube](/benchmarks/sod-and-lax-shock-tubes.md)
($t=0.2$), Figs. 13–20. In the Noh run the positivity limiter of the
remap is needed: without it negative internal energy and pressure stop
the code; the limited cells are marked in Fig. 17, and no run without
the limiter is displayed.

## Relation to other mesh-motion strategies

The remap is a moving-mesh finite-volume solve with a prescribed,
straight-line node motion, not with the monitor-driven motion of an
[adaptive moving mesh](/methods/adaptive-moving-mesh.md).
[Ramani & Shkoller (2023)](/sources/ramani-2023.md) take the other route
of that page: they write the Euler equations in ALE form on the fixed
reference domain, with the mesh velocity $\partial_t\psi$ of their mesh
map $\psi$ inside the fluxes, so the solution is never transferred
between two meshes (§6.1). The two sources share the concern for the
geometric terms of a moving cell: Ramani & Shkoller evolve the Jacobian
by the geometric conservation law ([free-stream preservation](/properties/free-stream-preservation.md)),
and Gu et al. do not discuss it.

## Qualifications

- The accuracy argument rests on moving-mesh analyses cited from DG,
  LDG and finite-difference WENO work in one dimension or for
  Hamilton–Jacobi equations; it is not proved for this two-dimensional
  finite-volume scheme (§2.2).
- The area of a quadrilateral whose vertices move linearly in time is a
  quadratic polynomial in time, because the shoelace formula is a sum of
  products of two coordinates; the mean
  $\tfrac12(\lvert I^n\rvert+\lvert I^{n+1}\rvert)$ used at the
  second Runge–Kutta stage equals the area at $t^{n+1/2}$ only when the
  quadratic coefficient vanishes *(compiler check, not in the sources)*.
- The internal energy is written per unit volume in §2.6 and per unit
  mass in the Sedov set-up ($p=(\gamma-1)\rho e$); the positivity
  statements are unaffected.
- The statements that the pure Lagrangian scheme fails on Saltzman and
  Noh concern the Lagrangian scheme of Cheng and Shu; the authors note
  that other Lagrangian schemes "may produce better or more robust
  results" (§3.5).
- Gu et al.'s Leblanc initial data are printed with five components for
  a four-component state $(\rho,v_1,v_2,e)$ on the left (§3.5.4); the
  [Leblanc page](/benchmarks/leblanc-shock-tube.md) records the printed
  variants of that problem.

# Citations

- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §1; §2.1–2.6, Eqs. (2.1)–(2.12), Theorems 2.1–2.2; §3.1–3.5, Tables 3.1–3.4, Figs. 6–20.
- [Ramani & Shkoller (2023)](/sources/ramani-2023.md) — §6.1, Eqs. (41)–(46) (ALE without remap; arXiv v2).
