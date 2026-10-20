---
type: Source
title: "Quezada de Luna & Ketcheson (2022) — Maximum principle preserving space and time flux limiting for diagonally implicit Runge–Kutta discretizations of scalar convection–diffusion equations"
description: "Combines a high-order WENO and DIRK baseline with a backward-Euler low-order scheme and limits the space-time antidiffusive flux by FCT or implicit GMC limiting, giving maximum-principle-preserving schemes of high order for any step size, and states conditions for bound-preserving DIRK stages."
resource: "doi:10.1007/s10915-022-01922-8"
source_kind: paper
authors: [Quezada de Luna M., Ketcheson D.I.]
year: 2022
venue: "J. Sci. Comput. 92:102"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Scientific_Computing_Quezada_Maximum_Principle_Preserving_Space_and_Time_Flux_Limiting_fo.pdf"
tags: [positivity, structure-preserving, implicit, ssp, runge-kutta, implicit-stage-solvers]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper is the implicit companion of [Kuzmin et al. (2022)](/sources/kuzmin-2022.md).
It extends [bound-preserving flux limiting](/methods/bound-preserving-flux-limiting.md)
from explicit Runge–Kutta methods to
[diagonally implicit Runge–Kutta](/methods/diagonally-implicit-runge-kutta.md)
time stepping and to diffusion. The model is the scalar convection–diffusion
equation $u_t+\nabla\cdot g(u)-\nabla\cdot(\epsilon(u,x)\nabla u)=0$ on a
finite-volume mesh. The target is the global discrete maximum principle
$\min_jy^n_j\le y^{n+1}_i\le\max_jy^n_j$, a form of
[positivity preservation](/properties/positivity-preservation.md), **for any
step size**, at high order in space and time.

Two schemes are combined. The high-order baseline is WENO5 with point-value
fluxes, integrated by an $s$-stage DIRK; the experiments use a five-stage
fifth-order SDIRK of Kennedy & Carpenter. The baseline violates the bounds
slightly. The low-order scheme is first-order Rusanov and central fluxes with
backward Euler. Its semi-discretization has a bar-state form that is local
extremum diminishing, so it is unconditionally maximum-principle preserving.
The difference between the time-averaged high-order flux
$\sum_ib_i(\cdot)(Y_i)$ and the implicit low-order flux carries spatial and
temporal corrections at once, and is limited by coefficients in $[0,1]$.

Zalesak-type FCT limiting around the backward-Euler solution is explicit once
that solution is known and can be iterated. GMC limiting keeps the low-order
flux implicit; Theorem 1 proves the maximum principle with no step
restriction, and the nonlinear system is solved by a fixed-point iteration.
Both limiters conserve mass. Intermediate stages can be limited, or taken from
methods whose stages satisfy relaxed SSP-stage conditions; backward-Euler
[extrapolation methods](/methods/extrapolation-methods.md) satisfy these for
every step, and the ten-stage IEX4 tableau is printed. Unlike the
[SSP route](/methods/strong-stability-preserving-runge-kutta.md), the time
scheme need not be SSP, so its order barriers do not apply. Tests cover
advection–diffusion, viscous [Burgers](/benchmarks/burgers-equation.md),
Buckley–Leverett, a drift–diffusion steady state, solid-body rotation and a
swirling vortex as variable-coefficient
[advection](/benchmarks/linear-advection-equation.md), and the KPP problem.

# Version read

arXiv:2109.08272v1 [math.NA], 17 September 2021 (footer "September 20,
2021"), 26 pages, all read; pp. 9–16 were also checked visually. This is the
preprint, not the J. Sci. Comput. version of record, although the archive
filename says "Crossref_Journal_of_Scientific_Computing"; the file prints no
DOI or journal data. Title and authors match Crossref (Crossref
title-cases the title). Section, equation and table numbers on this page are
those of arXiv v1. Code is printed at github.com/manuel-quezada/BP_Lim_for_imp_RK_Methods.

# Key claims

Registry notation: $h$ is the step (source $\Delta t$), $s$ the number of
stages (source $M$), $a_{ij}$, $b_i$, $c_i$ the Butcher coefficients (source
$a_{ms}$, $b_m$, $c_m$), $Y_i$ the stage values (source $y^{(m)}$),
$h_{\mathrm{FE}}$ the forward-Euler bound (source $\Delta t^{FE}$), $y_i$ the
cell averages with global bounds $y^{\min}$, $y^{\max}$. The finite-volume
quantities ($K_i$, $S_{ij}$, $G^L_{ij}$, $G^H_{ij}$, $\lambda_{ij}$,
$\bar y_{ij}$, $\alpha_{ij}$) and the GMC relaxation parameter $\kappa$ are
page-local (see Notation map).

1. Backward Euler with first-order Rusanov convective and central diffusive
   fluxes is maximum-principle preserving (MPP) **for every step size**. The
   semi-discretization is local extremum diminishing because it reads
   $\lvert K_i\rvert\dot y_i=\sum_j\lvert S_{ij}\rvert\lambda_{ij}(\bar y_{ij}(y)-y_i)$
   with $\lambda_{ij}\ge0$ and $\bar y_{ij}\in[\min\{y_i,y_j\},\max\{y_i,y_j\}]$
   (§3, Eqs. (12)–(14)). **Derived** (unconditional MPP of backward Euler
   cited)
2. The same semi-discretization with forward Euler is MPP only for
   $h\le\lvert K_i\rvert/\sum_j\lvert S_{ij}\rvert\lambda_{ij}=O(\Delta x^2)$,
   because diffusion enters $\lambda_{ij}$ (Remark 1). **Derived**
3. The limited update
   $y^{n+1}_i=y^n_i-\frac{h}{\lvert K_i\rvert}\sum_j\lvert S_{ij}\rvert[G^L_{ij}-\alpha_{ij}(G^L_{ij}-G^H_{ij})]$
   with $G^H_{ij}=\sum_ib_i(F^H_{ij}-P^H_{ij})(Y_i)$ corrects the low-order
   scheme in space and time at once; earlier space-time FCT combined explicit
   schemes and was MPP only under a step restriction (§1, §2, §4, Eqs. (6),
   (21)–(22)). **Stated** (positioning)
4. FCT limiting (Zalesak's algorithm (24) with
   $Q^\pm_i=\frac{\lvert K_i\rvert}{h}(y^{\max/\min}-y^{L,n+1}_i)$) gives
   $y^{\min}\le y^{n+1}_i\le y^{\max}$ for any $h$ and conserves mass (§5,
   Eqs. (23)–(24)). **Proved** (short proof in text)
5. The limiters are computed explicitly, although the low- and high-order
   methods are implicit (§5). **Stated**
6. Theorem 1 (maximum principle, GMC): with
   $Q^\pm_i:=a_i[(y^{\max/\min}-\bar y_i(y^{n+1}))+\kappa(y^{\max/\min}-y^{n+1}_i)]$,
   if $y^n_i\in[y^{\min},y^{\max}]$ and the $\alpha_{ij}$ satisfy
   $Q^-_i\le\sum_j\lvert S_{ij}\rvert\alpha_{ij}(G^L_{ij}-G^H_{ij})\le Q^+_i$,
   then $y^{n+1}_i$ from (28) lies in $[y^{\min},y^{\max}]$ with no step
   restriction (§6, Eqs. (26)–(30)). **Proved**
7. The GMC-limited scheme (28) conserves mass (§6). **Proved**
8. Newton with the exact Jacobian of (28) is impractical; the fixed-point
   iteration (31), suggested by D. Kuzmin, is used with tolerance $10^{-12}$ in
   $\ell^2$ (§6, Eq. (31), Acknowledgment). **Stated**. Its convergence is not
   analysed; the step-size independence is a property of the solution of (28),
   not of the iteration.
9. Sections 5–6 guarantee MPP of $y^{n+1}$ only; the DIRK stages $Y_i$ may
   still violate the bounds (§4, §7). **Stated**
10. Approach 1 limits each DIRK stage; this "can (at least formally) reduce
    the order of accuracy", though Kuzmin et al. saw no loss with explicit RK
    (§7). **Stated**
11. Approach 2: if the semi-discretization is MPP under forward Euler for
    $h\le h_{\mathrm{FE}}$ and, with $X(\mu)=(I+\mu A)^{-1}$,
    $AX(\mu)\ge0$ and $AX(\mu)\mathbf 1\le\mathbf 1$ entrywise, then the stages
    are MPP for $h\le\mu h_{\mathrm{FE}}$. These conditions "are more relaxed
    than those required for the full method to be SSP" (§7, Eq. (32)).
    **Stated** (attributed to Kuzmin et al.)
12. Backward Euler extrapolation methods satisfy (32) for arbitrarily large
    $\mu$, so their stages are unconditionally SSP; they are A($\alpha$)-stable
    with $\alpha$ close to 90°, exist at any order and parallelize well
    (§7.1). **Stated**
13. IEX4 has 10 stages with weights
    $b=(-\tfrac16,2,2,-\tfrac92,-\tfrac92,-\tfrac92,\tfrac83,\tfrac83,\tfrac83,\tfrac83)$
    (Eq. (33)). **Stated**. These are the Aitken–Neville weights
    $(-\tfrac16,4,-\tfrac{27}2,\tfrac{32}3)$ of the harmonic sequence
    $1,2,3,4$ divided by the substep counts *(compiler check)*.
14. SSP time stepping is limited to order 4 (explicit) or 6 (implicit), and
    "existing high-order implicit SSP methods are not A-stable", so they
    impose severe step restrictions on (1) (§1). **Stated**
15. The present time discretization need not be SSP, can have any order and
    can be diagonally implicit, so it avoids the SSP order barriers (§1, §9).
    **Stated**
16. Methods that impose local bounds (TVD limiters, FCT) are at most second
    order because they clip smooth extrema; global bounds allow higher order
    (§1). **Stated**
17. The limiters do not impose a local non-oscillatory property, so a
    high-order baseline with only small MPP violations, such as WENO, is a key
    ingredient (§9). **Stated**
18. Linear advection–diffusion (35), $\epsilon=0$, $h=0.5\Delta x$,
    $t=2\pi$: WENO-SDIRK has $E_1=1.25\times10^{-4}$ at $\Delta x=1/200$ (rate
    4.15) and $\delta=-2.08\times10^{-5}$. FCT-SDIRK needs two iterations to
    match it ($1.15\times10^{-4}$, rate 4.15, $\delta=-1.69\times10^{-21}$);
    with one iteration it reaches $1.66\times10^{-4}$, rate 3.65. GMC-SDIRK
    needs $\kappa\ge2$ ($1.16\times10^{-4}$, rate 4.15); with $\kappa=0$ it
    gives $4.03\times10^{-4}$, rate 3.10. Low-BE gives $9.42\times10^{-1}$,
    rate 0.59 (Table 1). **Shown**
19. Same problem with $\epsilon=0.001$: physical dissipation reduces limiter
    action; one FCT iteration and $\kappa=0$ suffice, and the three high-order
    variants reach $E_1\approx5.46$–$5.48\times10^{-5}$ with rates 4.52–4.55 at
    $\Delta x=1/200$ (Table 2). **Shown**
20. Pure diffusion: the high-order discretization is already MPP and the
    limiters do not activate (§8.1). **Shown** (no table)
21. IEX4 with GMC limiting of the semi-discretization (MPP stages) plus
    limiting of the update, $\epsilon=0.001$: rates 3.63, 3.89, 4.61,
    $E_1=5.81\times10^{-5}$ at $1/200$, $\delta>0$ throughout (Table 3,
    §8.1.1). **Shown**
22. Viscous Burgers ($\epsilon=0.01$, $t=0.25$): WENO-SDIRK has
    $\delta=-2.67\times10^{-9}$ (200 cells) and $-2.41\times10^{-5}$ (400
    cells); the limited schemes and Low-BE stay at round-off,
    $\delta\sim-10^{-14}$–$-10^{-15}$ (Fig. 2). **Shown**
23. Viscous Buckley–Leverett ($t=0.2$): WENO-SDIRK has
    $\delta=-1.29\times10^{-9}$ and $-1.25\times10^{-8}$; the limited schemes
    reach round-off (Fig. 3). **Shown**
24. Drift–diffusion steady state (38) to $t=20$: the MPP methods remove the
    WENO-SDIRK undershoots on coarse grids (e.g. $\delta=-3.64\times10^{-3}$ at
    $\Delta x=1/25$); all high-order variants give the same $E_1$
    ($3.24\times10^{-2}$ to $2.64\times10^{-5}$) with rates 3.95, 4.05, then
    2.26 at $1/200$ (Table 4). **Shown**
25. Solid-body rotation, $128^2$ cells, $t=1$: WENO-SDIRK ranges over
    $[-7.80\times10^{-4},1.0023]$ with $E_1=2.09\times10^{-2}$; FCT-SDIRK
    $2.22\times10^{-2}$ and GMC-SDIRK $2.10\times10^{-2}$, both within bounds;
    Low-BE $1.32\times10^{-1}$ with maximum 0.2772 (Fig. 6). **Shown**
26. Periodic swirling vortex, $T=1.5$, $128^2$: WENO-SDIRK ranges over
    $[-7.01\times10^{-3},1.0366]$; FCT and GMC give $E_1=2.99\times10^{-2}$
    against $2.97\times10^{-2}$ for WENO (Fig. 7). **Shown**
27. 2-D linear advection–diffusion ($\epsilon=10^{-3}$, $t=0.5$): full accuracy
    needs at least two FCT iterations or $\kappa\ge1$; at $\Delta x=1/200$
    WENO $1.08\times10^{-4}$ (rate 4.60), FCT with two iterations
    $1.17\times10^{-4}$ (4.70), GMC with $\kappa=1$ $1.08\times10^{-4}$ (4.52)
    (Table 5). **Shown**
28. KPP ($\epsilon=0$): Low-BE is MPP and entropy stable for every entropy
    pair, so it converges to the entropy solution but is very dissipative;
    WENO-SDIRK reproduces the rotating wave but violates the bounds
    ($\delta=-6.03\times10^{-8}$); FCT and GMC keep $u\in[\pi/4,14\pi/4]$
    "without a noticeable degradation in accuracy" (Fig. 8, §8.8). Global-bound
    limiting alone does not guarantee entropy solutions. **Shown** / **Stated**
29. The limiters apply to "a wide range of space and time discretizations",
    with local error of any order and a step "restricted only by accuracy
    considerations" (§9). **Stated**
30. Appendix A: the FCT route solves $s$ DIRK stage systems plus one
    backward-Euler system; GMC skips the low-order solve but iterates (31).
    Newton uses pseudo-Jacobians (the low-order Jacobian scaled by
    $a_{ii}h$ for the WENO stages, wave-speed bounds frozen) with tolerances
    $10^{-12}$ (low order) and $10^{-8}$ (stages); a constant linearized
    Jacobian factorized once is an alternative (App. A.1–A.3), see
    [implicit stage solvers](/methods/implicit-stage-solvers.md). **Stated**

The temporal order cannot be read off the tables: space and time are refined
together at $h=0.5\Delta x$, the SDIRK has design order five, and every
measured rate is about four. Possible stiff order reduction of the SDIRK on
the diffusive problems is not discussed.

# Printed slips

- Eq. (35b): the initial condition is printed $u(x,0)=\sin^4(2\pi x)$ on
  $[0,2\pi]$, but the printed exact solution
  $\frac38-\frac12e^{-4\epsilon t}\cos(2(x-t))+\frac18e^{-16\epsilon t}\cos(4(x-t))$
  is $\sin^4(x-t)$ at $\epsilon=0$; the 2-D analogue (43b) prints
  $\sin^4(x+y)$ correctly.
- §8.1 and Table 5: $\Delta x$ is listed as $1/25,\dots,1/200$ on domains of
  length $2\pi$; as printed, $\Delta x$ is ambiguous.
- Table 3 caption: "See the third approach in Section 7", but Section 7 lists
  two approaches.
- §8 names the low-order method "LLF-BE"; text, tables and figures call it
  "Low-BE".
- Eq. (36a): $u_t+\left(\frac{u^2}{2}\right)=\epsilon u_{xx}$ lacks the
  $x$-derivative on the flux.
- §8.2: the wave-speed bound
  $\max\{u_i,u_{i+1},\hat u^+_i,\hat u^-_{i+1}\}$ uses undefined hatted states
  and no absolute values (harmless since $u\ge0$).
- §8.4: problem (38) is called "nonlinear" (text, Table 4, Fig. 4) although
  its flux is linear in $u$; "we get $u^A_{i+1/2}\ge0$" lacks the bar.
- Table 4: at $\Delta x=1/100$ and $1/200$ all four high-order columns print
  the same $\delta$, and the rate drop to 2.26 is not commented on.
- Appendix A.3: $\bar u=\frac12[\max u_0-\min u_0]$ is a half-range, while the
  text claims $\bar u\in[\min u_0,\max u_0]$; $\frac12[\max+\min]$ is likely
  meant.

# Notation map

| Quezada de Luna & Ketcheson (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$ | $h$ | time step; **the source's $h$ is the mesh size** (Remark 1), and Algorithm 1 uses $h$ for the step |
| $M$ | $s$ | number of DIRK stages; **$M$ is the registry mass matrix** |
| $a_{ms}$, $b_m$, $c_m$ | $a_{ij}$, $b_i$, $c_i$ | Butcher coefficients; **$s$ is the column index in the source** |
| $y^{(m)}$ | $Y_i$ | stage values |
| $u_i$, $u^{\min}$, $u^{\max}$ | $y_i$, $y^{\min}$, $y^{\max}$ | cell averages and global bounds |
| $f(u)$, $c(u,x)$ | $g(u)$, $\epsilon(u,x)$ (page-local) | convective flux and diffusion coefficient; **the registry $f$ is the ODE right-hand side and $c$ the abscissae** |
| $\Delta t^{FE}$ | $h_{\mathrm{FE}}$ | forward-Euler MPP step |
| $F_{ij}$, $P_{ij}$, $G_{ij}$ | — | convective, diffusive and time-averaged total face fluxes; superscripts $L$, $H$ for low and high order |
| $\alpha_{ij}$ | — | flux limiter in $[0,1]$; **not a Shu–Osher coefficient** |
| $\lambda^A_{ij}$, $\lambda_{ij}$, $\bar u_{ij}$ | —, —, $\bar y_{ij}$ | wave-speed bound, combined coefficient and bar state; **$\lambda$ is not an eigenvalue** |
| $\gamma$ | $\kappa$ (page-local) | GMC relaxation parameter, as on the [flux-limiting page](/methods/bound-preserving-flux-limiting.md); **$\gamma$ is the registry SDIRK diagonal, which the source also uses** |
| $X(\mu)=(I+\mu A)^{-1}$, $e$ | —, $\mathbf 1$ | SSP-stage resolvent; **$\mu$ is not a Nevanlinna–Odeh multiplier** |
| $Y_{kj}$, $T_{jk}$ | — | extrapolation substep values and Aitken–Neville table |
| $\delta$ | — | smallest bound margin over all cells and steps; MPP iff $\delta\ge0$ |
| $E_1$ | — | $L^1$ error |

# Reference list

The paper prints 44 references in numbered, alphabetical style. All are merged
complete into the [bibliography](/bibliography.md) with `citedby`
quezadadeluna-2022. No DOIs are printed. Ref. [25], printed as "Preprint:
arXiv:2009.01133, 2020", is the preprint of the ingested
[kuzmin-2022](/sources/kuzmin-2022.md) and is kept as its own entry,
`kuzmin-2020-f`. The five Kuzmin 2020 works [21]–[25] are matched by title to
the entries `kuzmin-2020`, `kuzmin-2020-b`, `kuzmin-2020-c`, `kuzmin-2020-e`
and `kuzmin-2020-f`, not suffixed in printed order. Ref. [13] is the 1997
reprint of Harten's 1983 paper and is keyed by the printed year
(`harten-1997`); ref. [14] is a 1974 NYU technical report; ref. [18] (Kennedy
& Carpenter) is a NASA Langley publication printed without a report number
(`kennedy-2016`); ref. [10] prints literal braces in "{II}", removed in the
`.bib`, and is merged into `hairer-1996`.

# Pages created or updated

Chunk 6 (2026-10-20). This source is cited on:

* [Bound-preserving flux limiting of Runge–Kutta stages and updates](/methods/bound-preserving-flux-limiting.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [Extrapolation methods (Richardson extrapolation of a base integrator)](/methods/extrapolation-methods.md)
* [Invariant-domain preserving high-order time stepping (explicit and IMEX)](/methods/invariant-domain-preserving-time-stepping.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Positivity preservation in time integration](/properties/positivity-preservation.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
