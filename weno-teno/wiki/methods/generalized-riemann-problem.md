---
type: Method
title: "Generalized Riemann problem (GRP) solvers"
description: "A generalized Riemann problem has piecewise-linear (or piecewise-smooth) data across a jump; its approximate HLL solution gives the interface flux and its time derivative, hence a one-step second-order flux; Liu, Feng and Wang carry the HLL-GRP solver to multidimensional ideal MHD through rotational invariance."
status: established
aliases: [GRP, HLL-GRP, HLL-type generalized Riemann problem solver, generalized Riemann problem, rotational gradient]
tags: [riemann-solver, numerical-flux, finite-volume, mhd]
timestamp: 2026-10-23T23:00:00Z
---

# Generalized Riemann problem (GRP) solvers

A **generalized Riemann problem** (GRP) is the initial-value problem for
$\partial_tu+\partial_xf(u)=0$ with data that jump at $x=0$ and are linear (more generally
smooth) on each side,

$$u(x,0)=\begin{cases}u^-+(\partial_xu^-)\,x,&x<0,\\ u^++(\partial_xu^+)\,x,&x>0,\end{cases}$$

with $u^\pm$ the reconstructed interface states and $\partial_xu^\pm$ their normal gradients
(page-local notation; [Liu et al. (2023a)](/sources/liu-2023.md), §3.1.3, Eq. (52)). Its
**associated Riemann problem** is the same problem with the linear terms dropped (§3.2.1). A
GRP solver returns not only the interface state at $t=0^+$, as a Riemann solver does, but also
its time derivative there, so the time-averaged flux over a step can be expanded to second
order in one stage. As recalled by Liu et al. (§1), this lets GRP-based schemes reduce the
number of [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) stages and guide mesh motion in ALE
codes, and the HLL-type GRP solvers (HLL-, HLLC-, HLLD-GRP of Goetz, Balsara and Dumbser;
HLLI-GRP of Balsara, Li and Montecinos) had been applied to one-dimensional systems only.

## The HLL-GRP solver

As recalled by Liu et al. (§3.2.1, Eqs. (57)–(66), after Goetz, Balsara and Dumbser and
Balsara, Li and Montecinos), the HLL fan of the associated Riemann problem has the left,
intermediate and right states $u^-$, $u^{\mathrm{HLL}}$, $u^+$, separated by the speeds $s^-\le s^+$,
with $u^{\mathrm{HLL}}$ and the subsonic flux as on
[HLL-family solvers](/methods/hll-riemann-solvers.md). Each state is evolved linearly in time
inside its region of the fan, $\xi=x/t$ (page-local):

$$\tilde u(\xi,t)=u_\bullet+t\,\big(\xi I-A(u_\bullet)\big)\,\partial_xu_\bullet,\qquad u_\bullet\in\{u^-,u^{\mathrm{HLL}},u^+\}.$$

The intermediate gradient $\partial_xu^{\mathrm{HLL}}$ comes from the overdetermined least-squares
system that the authors derive "according to the Rankine–Hugoniot jump conditions" across the
two HLL waves ([Rankine–Hugoniot condition](/definitions/rankine-hugoniot-condition.md)):

$$\begin{pmatrix}\big(A(u^{\mathrm{HLL}})-s^-I\big)^2\\ \big(A(u^{\mathrm{HLL}})-s^+I\big)^2\end{pmatrix}\partial_xu^{\mathrm{HLL}}=\begin{pmatrix}\big(A(u^-)-s^-I\big)^2\,\partial_xu^-\\ \big(A(u^+)-s^+I\big)^2\,\partial_xu^+\end{pmatrix}$$

(Eq. (64); a $16\times8$ system for MHD). The time-averaged flux is expanded at $\xi=0$, ADER-like,
$\frac1{\Delta t}\int_0^{\Delta t}f(\tilde u(0,t))\,dt=f(\tilde u)\big|_{(0,0)}+A\,\partial_t\tilde u\big|_{(0,0)}\frac{\Delta t}2$
(Eq. (65)), with the first term the HLL flux of the associated problem. Since
$\partial_t\tilde u=-A\,\partial_xu_\bullet$ at $\xi=0$, the result is

$$h^{\mathrm{GRP}}=\begin{cases}f(u^-)-A(u^-)^2\,\partial_xu^-\,\dfrac{\Delta t}2,&s^->0,\\ h^{\mathrm{HLL}}(u^-,u^+)-A(u^{\mathrm{HLL}})^2\,\partial_xu^{\mathrm{HLL}}\,\dfrac{\Delta t}2,&s^-\le0\le s^+,\\ f(u^+)-A(u^+)^2\,\partial_xu^+\,\dfrac{\Delta t}2,&s^+<0\end{cases}$$

(Eq. (66); page-local $h^{\mathrm{GRP}}$). The update is a single forward stage with this flux.

## Multidimensional MHD by rotational invariance

Liu et al. (2023a) implement the HLL-GRP flux in a 2D and 3D finite-volume scheme for ideal
MHD with the Godunov–Powell source, which they call "the first attempt" at a multidimensional
HLL-GRP implementation (§1). The ingredients (§2–§3):

- **Rotation** (§3.1.3, Eqs. (41)–(56)). By rotational invariance, the normal flux at an edge
  midpoint is $f(u)\cdot n_{ij}=\mathsf T_{ij}^{-1}f^{(1)}(\mathsf T_{ij}u)$, $\mathsf T_{ij}$ the
  $8\times8$ rotation of the $x$ axis onto the normal $n_{ij}$ of the edge between cells $i$ and $j$ (page-local; App. A). The GRP data are
  the rotated states and the rotated **normal** gradients,
  $\partial_xu^\pm=\mathsf T_{ij}\big(\partial_xu\,n_{ij,x}+\partial_yu\,n_{ij,y}\big)^\pm$; the tangential
  gradients "have no effect on the normal flux". The authors claim to give "for the first time"
  an explicit expression of this "rotational gradient". The GRP is posed without the Powell
  source, which might "affect the stability and accuracy" (§3.1.3).
- **Reconstruction**: the locally divergence-free [WLS-ENO](/methods/wls-eno.md) linear
  reconstruction of primitive variables $w$ (page-local) of [Liu et al. (2021)](/sources/liu-2021.md), the same
  first author's earlier scheme, with row weights
  $W_j=1/[(\bar w_j-\bar w_i)^2+\varepsilon h^2]$, $\varepsilon=10^{-2}$, $h=\sqrt{\lvert I_i\rvert}$, four
  neighbours (page-local; §3.1.1, Eqs. (19)–(24)), and conservative gradients assembled by the
  product rule at each edge point (Eqs. (30)–(40)).
- **Limiter**: a Barth–Jespersen limiter on density and pressure at the edge midpoints, which
  the authors call a "PP limiter"; it keeps the reconstructed $\rho$, $p$ there between the
  neighbouring averages (§3.1.2, Eqs. (25)–(29)).
- **Source term**: the Wu–Shu discretization of the Godunov–Powell term (jump of the normal
  magnetic field weighted by $-s^-/(s^+-s^-)$), evaluated at $t^n+\Delta t/2$ with a
  Cauchy–Kowalewski predictor $\partial_tu=-A\,\partial_xu-A^{(2)}\partial_yu-(\nabla\cdot B)\,S_{\mathrm P}(u)$, $S_{\mathrm P}=(0,B,v,v\cdot B)$ the Powell vector (page-local)
  (§3.2.2, Eqs. (67)–(70); [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- **Wave speeds and time step**: the Wu–Shu estimates, with $0$ included in the
  minimum and maximum for the source weights and without it for $s^\pm$ of the GRP (Eqs.
  (10)–(15), (59)–(60)), and the Wu–Shu CFL-type step, which in Wu and Shu's analysis gives a
  provably positivity-preserving HLL scheme; Liu et al. apply it "without making a rigorous
  proof" for their own scheme (§2.2, Eqs. (16)–(18)).
- **Least squares**: every least-squares problem (reconstruction and Eq. (64)) is solved by
  truncated SVD with threshold $10^{-10}$ times the largest singular value, because the matrices
  "may be ill-conditioned as the mesh is refined" (§3.3, Eqs. (71)–(77)).

## Evidence

Liu et al. (2023a) (§4; Cartesian grids; CFL $0.8$ unless stated) compare the one-stage
HLL-GRP scheme with forward Euler (FE) and two-stage SSP-RK2 schemes built on the HLL flux with
the same reconstruction.

- **Accuracy** ([circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
  $t=2$, CFL $0.2$, $16^2$ to $256^2$, $L^1$ errors of $v_x$, Table 1): HLL-GRP errors
  $1.7210\times10^{-2}$ to $5.5446\times10^{-5}$, orders $2.1125$, $1.9463$, $2.3627$, $1.8565$;
  RK2 orders $2.0953$, $1.9895$, $2.4408$, $2.3915$ with $3.6834\times10^{-5}$ on $256^2$; FE orders
  fall to $1.0034$.
- **Cost** (Table 1, $256^2$, 64 cores of Tianhe-1A): $714.7742$ s (FE), $4202.0244$ s (HLL-GRP),
  $1681.4516$ s (RK2); the authors attribute the cost of HLL-GRP to the truncated-SVD solves.
  *(compiler check, not in the sources: HLL-GRP takes $2.50$ times the RK2 time.)*
- **Robustness**: on the [Brio–Wu tube](/benchmarks/brio-wu-shock-tube.md) HLL-GRP and RK2
  "basically coincide"; the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) runs to
  $t=100$ on $200^2$; the [blast wave and rotor](/benchmarks/mhd-blast-wave.md) (plasma beta
  about $2.51\times10^{-4}$) and a 3D blast wave on $200^3$ give profiles close to RK2, and "no
  negative pressure or negative density was generated in all simulations" (§4–§5). Divergence
  norms of HLL-GRP lie between or below those of FE and RK2.

## Qualifications

- The observed orders of HLL-GRP are erratic and fall to $1.86$ on the finest mesh, where its
  error is 1.5 times that of RK2 *(compiler check, not in the sources: $5.5446/3.6834=1.51$)*; the paper reads them as "the expected convergence order"
  (§4.2). The errors are those of the reconstructed polynomial (Eq. (84)), measured against the exact
  solution at $t=2$, "which is the initial value" (§4.2).
- The one-stage flux is motivated as cheaper than multi-stage Runge–Kutta, but this
  implementation is slower than RK2 at equal mesh; the authors name the SVD cost and the
  inability to "model multidimensional wave propagation as faithfully and accurately as
  genuine multidimensional schemes" as limitations (§5). Unstructured meshes are claimed
  applicable "in theory" and not tested.
- No positivity proof is claimed: the "PP limiter" is a local-extremum limiter at edge
  midpoints, not a [Zhang–Shu scaling](/methods/zhang-shu-scaling-limiter.md) of the update
  ([bound preservation](/properties/bound-preservation.md)).
- Liu et al. label the plotted blast-wave quantity "magnetic pressure $\lvert B\rvert$", while
  other figures use $\lvert B\rvert^2/2$ (§4.4, Figs. 8–9). *(compiler check, not in the
  sources: the printed colour range $[21,34]$ contains the initial
  $\lvert B\rvert=100/\sqrt{4\pi}\approx28.2$ and not $\lvert B\rvert^2/2\approx398$, so the plotted
  field is $\lvert B\rvert$.)*
- A time-dependent interface flux with its time derivative is also what
  [gas-kinetic schemes](/methods/gas-kinetic-scheme.md) supply to two-stage fourth-order
  time stepping; the sources do not compare the two.

# Citations

- [Liu et al. (2023a)](/sources/liu-2023.md) — §1, §2 (Eqs. (1)–(18)), §3 (Eqs. (19)–(77)), §4 (Table 1, Figs. 3–20), §5, Apps. A–B.
- [Liu et al. (2021)](/sources/liu-2021.md) — the WLS-ENO reconstruction reused by Liu et al. (2023a).
