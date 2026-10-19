---
type: Source
title: "Unfer (2021) — Third order asynchronous time integration for gas dynamics"
description: "A third-order asynchronous (cell-level local time stepping) explicit integrator, ARK3, built on SSPRK(3,3) for finite-volume compressible reacting Navier–Stokes: conservative by construction, with a recall mechanism, stability and entropy arguments for the first-order scheme, and measured speed-ups up to 36 with asynchronous AMR."
resource: "doi:10.1016/j.jcp.2021.110434"
source_kind: paper
authors: [Unfer T.]
year: 2021
venue: "J. Comput. Phys. 440:110434"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Computational_Physics_Unfer_Third_order_asynchronous_time_integration_for_gas_dynamics.pdf"
tags: [local-time-stepping, multirate, explicit, ssp, cfd, finite-volume]
timestamp: 2026-10-20T05:00:00Z
---

# Summary

The paper builds a third-order asynchronous explicit integrator, ARK3
("asynchronous Runge–Kutta", not additive), for finite-volume compressible
reacting multi-component Navier–Stokes on unstructured meshes. It is a form
of [local time stepping](/methods/local-time-stepping.md) at cell level:
every cell $K_i$ has its own step $h_i$, set by convective, diffusive and
chemical time scales. At each event time the mesh splits into refreshed
cells, their face neighbours and sleeping cells. Each cell carries two
time-continuous polynomial states: *conservative* states, integrated
whenever the cell or a neighbour is refreshed, and *extrapolated* states,
updated only at the cell's own refresh and used as flux inputs. These
polynomial states play the role of [dense output](/methods/dense-output.md).
The scheme is conservative by construction: whenever the flux on a face
changes, both adjacent cells are integrated to that time, so no
flux-correction step is needed.

For the first-order centered asynchronous scheme the paper argues
stability under a local CFL condition, a TV bound, consistency and a cell
entropy inequality, the last two with a *recall mechanism*: the local step
is re-estimated at every substep, and a cell whose step has dropped is
recalled and the event restarts. ARK3 is derived from the Shu–Osher
SSPRK(3,3) tableau ([SSP Runge–Kutta](/methods/strong-stability-preserving-runge-kutta.md)):
extrapolated states become parabolic, conservative states cubic, and face
fluxes are evaluated at three times per face interval. It reverts to
SSPRK(3,3) under a global step; no SSP property is claimed. A formal
truncation analysis gives third order in smooth regions, and strong shocks
need stage-wise fallbacks.

In the author's code, third order is confirmed on smooth density waves on
uniform and strongly stretched meshes, with single-thread speed-ups near 7
over synchronous SSPRK(3,3) when the theoretical speed-up is about 11, and
slow-downs (0.43–0.90) on uniform meshes. The [Sod shock tube](/benchmarks/sod-shock-tube.md)
and Shu–Osher results match the synchronous scheme. On the
[double Mach reflection](/benchmarks/double-mach-reflection.md) the
speed-up is 1.98, and 36.51 with asynchronous AMR. A viscous shock tube and
a 10-species reactive shock–bubble interaction complete the tests.

# Version read

Version of record (J. Comput. Phys. 440 (2021) 110434, Elsevier typeset),
32 pages, all read; pp. 6, 8–12 and 15–19 were read visually where the text
layer garbled equations. Page 1 prints the DOI and matches Crossref (title,
author, volume, article number). No identity problem. Equation and section
numbers on this page are those of the version of record.

# Key claims

Notation (see the notation map): $h_i$ the local step of cell $K_i$ (the
source's $\Delta t_i$); $t^i_p$ its refresh times and $t^i_q$ its
integration times; $t^{ij}_q$, $t^{ij}_{q+1}$ the last and next refresh
times of face $\Gamma_{ij}$; $\Delta x_i$ the cell size; $A_s$ the
asynchronous speed-up number; $\tau^i_p$ the local truncation error (not a
tree).

1. Asynchronous time integration gives each cell its own step; the maximum theoretical speed-up over a global step is $A_s=N_{\mathrm{cell}}/\big(\min_i h_i\sum_i1/h_i\big)$ (§3.1, Eq. (44)). Practical speed-up never reaches $A_s$ because of random memory access. **Stated**
2. The asynchronous family is conservative by construction: every flux update on $\Gamma_{ij}$ integrates both cells to that time and recomputes their derivatives, so the semi-discrete balance (14) holds at all times, unlike flux-capacitor or flux-memory-variable approaches with a correction step (Introduction, §3.2). **Derived**
3. Prop. 1: for a monotone Lipschitz flux under the local CFL condition, the extrapolated states stay in the convex admissible set $\Theta$ over $[t^i_p,t^i_{p+1}]$ if all $u_j(t^j_p)\in\Theta$ for $t^j_p<t^i_{p+1}$ (§3.3.1). **Proved**
4. The first-order centered asynchronous scheme is a convex combination of elements of $\Theta$, hence stable, under the local CFL condition $\sum_kh^i_k(a_k+b_k)\le\Delta x_i$ (§3.3.1, Eqs. (72)–(77)). **Proved** (sketch, with the slip of item 2 below)
5. A rise of the flux Lipschitz constants during a local step (an incoming shock) breaks the local CFL condition: in the inviscid Burgers Riemann problem with $u=1$ for $x\le\frac12$ and $u=0$ elsewhere, the right state has an infinite local step and the shock "cannot move further" without a wake-up mechanism (§3.3.1, Eq. (78)). **Derived**
6. The cure is the recall mechanism: re-estimate the local step at each integration substep and, if it is below the step used (with the stability margin), recall the cell at $t^i_p$ and restart (§3.3.1, App. A). For weak shocks with subsonic speed relative to the mesh the upwind asynchronous scheme needs no recall. **Stated**
7. The substep scheme is TV-stable, $\lVert u^{k+1}-u^k\rVert_1\le h_kL_{\max}\sum_j\sum_wTV(u^w)$ (§3.3.2, Eqs. (79)–(84)), following LeVeque. **Derived**
8. The first-order centered asynchronous scheme is consistent, $\tau^i_p=O(\Delta x_i)$, by induction from a synchronous first step, assuming $O(\Delta x)=O(h_p)=O(h_k)$ (§3.3.3, Eqs. (85)–(92)). **Derived**
9. Under the local CFL condition with recall, the update is non-decreasing in each argument and satisfies a cell entropy inequality consistent with the Kružkov form; the paper declares the convergence proof of the first-order scheme "complete" (§3.3.4, Eqs. (93)–(100)). **Derived** (the convergence step itself is asserted)
10. The MUSCL extension inherits stability from the first-order scheme through Berthon's decomposition of each substep (§3.4). **Stated**
11. Asynchronous Runge–Kutta (ARK) methods exploit that the effective duration of a face flux, $t^{ij}_{q+1}-t^{ij}_q$, differs from the cell's local step; ARK2 evaluates the flux at the midpoint of that interval (§3.5, Eqs. (101)–(102)). **Stated**
12. In the nonlinear case the final Runge–Kutta averaging stage cannot be applied, because the actual step duration is unknown at $t^i_p$; second order needs parabolic conservative states, third order parabolic extrapolated states and cubic conservative states (§3.5). **Derived**
13. ARK3 is built on the SSPRK(3,3) tableau $c=(0,1,\frac12)$, $a_{21}=1$, $a_{31}=a_{32}=\frac14$, $b=(\frac16,\frac16,\frac23)$ (Eq. (106)) and "reverts to the RK3 SSP method if a global time step is used"; "There is no claim at this point that the SSP property holds for the ARK3 method" (§3.5.2). **Stated**
14. With third-order spatial reconstruction, the ARK3 truncation error is $\tau^p_i=O(\Delta x_i^3)$: "third order accurate in the smooth regions" (§3.5.3, Eqs. (112)–(118)). **Derived** (formal; recall and fallbacks excluded)
15. Strong shocks require further stabilization: first-order cell values where extrapolated states are undefined, previous-stage fluxes where those are undefined, and a per-stage step re-estimate with recall (end of §3.5.2, App. B). **Stated**
16. Smooth 1D density wave, uniform mesh, CFL 0.4: ARK3 $L^2$ error ratios 7.91–8.06 for $N=25$–$25600$, errors nearly equal to SSPRK(3,3) ($2.166\times10^{-12}$ against $2.200\times10^{-12}$ at $N=25600$); $A_s=1.1$; speed-up 0.43–0.87, i.e. ARK3 is slower (§4.1). **Shown**
17. On the stretched "cubic" mesh ($\alpha=10^{-2}$): error ratios 7.09–8.00, $A_s$ 10.7–11.7, single-thread speed-up 6.00–7.53 ($N=200$: 213.3 s against 28.3 s); with 8 threads the speed-up falls to 0.98 ($N=800$) and 2.47 ($N=1600$), because the 1D case has many sparsely populated step classes (§4.1). **Shown**
18. 2D smooth wave, uniform mesh: ratio 8.00 at $200^2$, $A_s\approx1.04$, speed-up 0.62–0.90; strong scaling at $200^2$ on 8 threads 6.70 (ARK3) against 6.30 (SSPRK(3,3)); weak scaling $200^2\to400^2$ falls to 4.61/8 for ARK3 (memory bound) against 6.30/8 (§4.1). **Shown**
19. 2D "cubic by cubic" mesh: ratio up to 7.99 at $400^2$, $A_s$ 10.2–11.5; ARK3 strong scaling 5.55 on 8 threads at $100^2$ (no synchronous timing given) (§4.1). **Shown**
20. Sod (200 cells, $t=0.2$) and Shu–Osher (400 cells, $t=1.8$): little difference between ARK3 and SSPRK(3,3); small oscillations near the contact with sensor parameter 1, removable at the cost of local order loss (§4.2–4.3, Figs. 5–6). **Shown**
21. Double Mach reflection (Mach 10, $t=0.2$, $3840\times960$, CFL 0.4): SSPRK(3,3) 169499 s, ARK3 85502 s, ARK3 with asynchronous AMR ($240\times60$, 4 levels) 4643 s, speed-ups 1.98 and 36.51; $\langle A_s\rangle=4.6$, $\langle A_s^{\mathrm{AMR}}\rangle=144$; ARK3 shows more slip-line roll-ups, i.e. less numerical dissipation (§4.5, Figs. 10–11). **Shown**
22. The ratio $A_s/\text{speed-up}\approx4$ of the double Mach reflection projects a speed-up of 50 for the reactive shock–bubble case with $\langle A_s^{\mathrm{AMR}}\rangle\approx200$; that run took "an unreasonable 8-days time" (§4.7). **Stated** (projection, not measured)
23. Asynchronous integration handles small distorted cells of poor meshes efficiently: $A_s^{\mathrm{AMR}}$ surges to 400 when the shock reaches the smallest cell (§4.7, Figs. 19–20). **Shown**
24. Third-order asynchronous integration also gains precision, "because the level of numerical dissipation seems to be lower in practise" (Conclusion). **Stated** (backed only by the double-Mach roll-ups)
25. Extension to higher order is "relatively straight forward" through higher-degree time polynomials (Conclusion). **Stated**
26. The algorithm runs on shared memory with per-thread discrete time scheduling and three barrier-separated loops; it is compatible with MPI through buffered cell-level ghost-state and ghost-flux messages, not used here (App. A, App. C). **Stated**

*(Reader caveats, not in the source.)* Speed-ups are measured against the
same code run synchronously with asynchronous data structures, not an
optimized synchronous code. The lower dissipation of claim 21 is not
analysed; fewer dissipative updates per cell under larger local steps is a
plausible cause.

# Printed slips

1. Eq. (27), p. 6: "$S_R=\min(u_R+c_R,\hat u+\hat c)$" — the right wave-speed estimate is a max (checked visually).
2. p. 12, text before Eq. (76): "$\frac{\partial\tilde u_i}{\partial t}(t_p^i)=-\frac1{\Delta x}[a_1(\widetilde{u_{i+1}}(t_p^i)-u_i(t_p^i))+c_1(\widetilde{u_{i-1}}(t_p^i)-u_i(t_p^i))]$" — $c_1$ should be $b_1$ (Eq. (76) uses $b_1$), and the leading minus sign is inconsistent with Eq. (74), where the increments enter with a plus sign.
3. §4.1, uniform-mesh table: ARK3 $L^2$ error at $N=400$ printed "5.749e-6"; the neighbours (4.601e-6 at $N=200$, 7.187e-8 at $N=800$), the printed ratio 8.00 and the SSPRK3 value 5.754e-7 show it should be 5.749e-7.
4. §4.1, weak-scaling table: SSPRK3 printed 6.09/8, while $253/333\times8=6.08$ (rounding).
5. Eq. (106): the SSPRK(3,3) tableau is printed without its zero first row.
6. Eq. (105) against its describing sentence (p. 16): the text gives the stage-3 slope as $\partial_t\widetilde{\mathbf U}_i(t^i_p)+\partial_t^2\widetilde{\mathbf U}_i(t^i_p)(\Delta t_3-\Delta t_1)$, which yields the bracket $\frac12\Delta t_1^2+(\Delta t_3-\Delta t_1)^2$, but Eq. (105) prints $\frac12\Delta t_1^2+\Delta t_3^2-\Delta t_3\Delta t_1$, which corresponds to the slope with $\Delta t_3$. The two agree only for $\Delta t_1=0$ (global step); the paper does not say which the code uses (reader's derivation).
7. The truncation-error index moves from $\tau_p^i$ (Eqs. (85)–(92)) to $\tau_i^p$ (Eqs. (112), (118)).
8. Ref. [3] prints pages "624–625" for a J. Sci. Comput. article, implausibly short; recorded as printed.
9. Wording: "minimum time step reaches its anticlimax", "Double Mach Reflexion", "law amplitude wiggles", "theses".

The reader verified that the ARK3 face-flux polynomial (Eqs. (108)–(110))
integrates under a global step to $h(\frac16F_0+\frac16F_1+\frac23F_{1/2})$,
the SSPRK(3,3) weights, consistent with claim 13.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\partial_t\mathbf U_i=\frac1{\lvert K_i\rvert}\sum_j(\mathbf F_d-\mathbf F_c)\cdot\Gamma_{ij}\mathbf n_{ij}+S_i$ | $y'=f(t,y)$ | method-of-lines finite-volume system, Eq. (14) |
| $\mathbf U_i(t)$, $\widetilde{\mathbf U}_i(t)$ | kept | conservative and extrapolated time-polynomial states of cell $i$ |
| $\Delta t_i$, $\Delta t_k^i$ | $h_i$, $h^i_k$ | local step and substep; no multirate ratio is defined |
| $\Delta t_1,\Delta t_2,\Delta t_3$ | kept | ARK3 stage offsets from $t^i_p$, matching $c=(0,1,\frac12)$ |
| $\Delta x_i$ | $\Delta x_i$ | agrees |
| CFL 0.4 | $\nu=0.4$ | Courant number |
| **ARK, ARK2, ARK3** | kept | asynchronous Runge–Kutta; **collides** with additive Runge–Kutta (ARK) of the [IMEX](/methods/imex-runge-kutta.md) literature |
| RK3SSP | SSPRK(3,3) | Shu–Osher three-stage method |
| **$\tau_p^i$, $\tau_i^p$** | kept | local truncation error; **collides** with the registry tree $\tau$ |
| **$S$**, $S_i$ | kept | sleeping-cell set, cell source term; **$S$ collides** with the stability region $\mathcal S$ only typographically |
| $R$, $O$, $I$ | kept | refreshed, outer and integrated cell sets; **$R$ is not** the stability function |
| $a_k$, $b_k$ | kept (page-local) | incremental coefficients of the first-order scheme; **$b_k$ is not** a Runge–Kutta weight |
| $L_v$, $L_w$, $L_{\max}$ | kept | Lipschitz constants of the numerical flux |
| **$\eta$**, $\beta$ | kept | smoothness indicator and its tuning parameter (spatial); **$\eta$ collides** with the registry entropy |
| $A_s$, $A_s^{\mathrm{AMR}}$ | kept | asynchronous speed-up numbers |

# Reference list

34 printed references, numbered [1]–[34], in order of first citation. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` unfer-2021. Refs. [5] (Jameson and Turkel, AIAA J. 1981) and [29]
(Boivin and Jiménez, Proc. Combust. Inst. 2011) print no volume or pages;
[3] prints the implausible pages 624–625; [16] is an LNCS chapter (VECPAR
2016) and [26] a Notes Numer. Fluid Mech. chapter. The two Diegelmann et al.
2016 works [21], [22] take suffixes in printed order. [5] is the 1981 AIAA
paper of Jameson, Schmidt and Turkel, already in the bibliography as
`jameson-2024` (placeholder year of its first, undated citation); [24]
(Dawson and Kirby, printed 2000) is `dawson-2001`, the year of its SIAM J.
Sci. Comput. issue. No DOIs are printed.
There are no printed duplicates and no unparseable items.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Dense output](/methods/dense-output.md)
* [Double Mach reflection](/benchmarks/double-mach-reflection.md)
* [Local time stepping](/methods/local-time-stepping.md)
* [Sod shock tube](/benchmarks/sod-shock-tube.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
