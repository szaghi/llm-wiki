---
type: Method
title: "Implicit shock tracking and moving DG (MDG-ICE)"
description: "Implicit shock tracking treats the mesh geometry as an unknown and moves element faces onto discontinuities by enforcing the flux-jump (Rankine–Hugoniot) condition weakly; the page gives the MDG-ICE formulation of Corrigan et al. as recalled and the MDG+ICE variant of Luo, Absillis and Nourgaliev, with its tests and the limits of its claims."
status: established
aliases: [MDG-ICE, MDG+ICE, moving discontinuous Galerkin with interface condition enforcement, moving discontinuous Galerkin with interface conservation enforcement, implicit discontinuity tracking, shock fitting by optimization]
tags: [shock-tracking, dg, numerical-flux]
timestamp: 2026-10-22T12:00:00Z
---

# Implicit shock tracking and moving DG (MDG-ICE)

Shock capturing keeps the mesh fixed and lets the scheme smear a
discontinuity over a few cells. **Implicit shock tracking** instead makes
the positions of the mesh vertices unknowns, solved together with the flow.
The extra equations are the *interface condition*: across every element
face the normal flux is continuous,

$$[\![F(u_h)\cdot n]\!]=F(u_h^+)\cdot n-F(u_h^-)\cdot n=0,$$

with page-local $F$ the flux (space–time flux in unsteady problems) and $n$ the face normal. In a space–time formulation $F$
includes the time component $u$, and the condition is the
[Rankine–Hugoniot jump condition](/definitions/rankine-hugoniot-condition.md)
along a moving face. It holds automatically in smooth regions. Across a
discontinuity it can hold only if a face lies on the discontinuity, so
enforcing it drives faces onto shocks and contacts.
[Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) develop the
MDG+ICE variant of this approach for the compressible Euler equations
(§I–III).

## MDG-ICE (Corrigan, Kercher & Kessler)

As recalled by Luo et al. (§3.2), the moving DG method with interface
condition enforcement (MDG-ICE) of Corrigan, Kercher and Kessler works as
follows:

- the flow is discretized by [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
  on space–time elements (or on space for steady problems);
- the space–time coordinates of the vertices are unknowns;
- the interface condition is tested against the *discontinuous* trace
  space, $\int_e[\![F(u_h)\cdot n]\!]\,v_h\,dS=0$ for all $v_h$ in that
  space (Eq. (3.6)).

For a 1D unsteady problem this gives $n_{\mathrm{face}}\times n_{\mathrm{basis}}\times n_{\mathrm{eqns}}$
equations for $2\,n_{\mathrm{poin}}$ geometric unknowns, an over-determined
and large system (Fig. 2; page-local counts of faces, face basis functions,
equations and vertices). Luo et al. credit the method with implicit
detection and tracking of all discontinuity types, rarefaction heads and
tails included, without a Riemann solver or a limiter.

## MDG+ICE (Luo, Absillis & Nourgaliev)

Luo et al. change three things (§3.2–3.5):

1. **Continuous trace space.** The interface condition is tested against
   the continuous, vertex-based trace space (Eq. (3.7)), as in embedded
   DG. This gives $n_{\mathrm{poin}}\times n_{\mathrm{eqns}}$ equations. For
   a scalar law the interface system is square.
2. **Time-fixed mesh and one slab per step.** Vertices move only in $x$,
   not in $t$. Each step solves one space–time slab $[t^n,t^{n+1}]$, with
   the $x$-coordinates of the vertices at $t^{n+1}$ as geometric unknowns.
   The interface condition is not enforced on the slab faces, where the
   flux is upwind "according to the causality principle" (Fig. 4). The 1D
   tests in the paper use a single slab over the whole time interval.
3. **No Riemann solver.** Since the interface condition defines the face
   flux at convergence (Eq. (3.14)), interior faces use the central average
   $\tfrac12\big(F(u_h^-)\cdot n+F(u_h^+)\cdot n\big)$ (Eq. (3.15)). No
   limiter, ENO/WENO reconstruction or
   [artificial viscosity](/methods/artificial-viscosity.md) is used. The
   authors state that an upwind space–time flux consistent with (3.14)
   "remains an open problem" (§3.3).

**Nonlinear solver.** The flow and geometry residuals form an
over-determined system $\mathbf R(\mathbf U)=0$, solved as
$\min\tfrac12\lVert\mathbf R\rVert^2$ by Levenberg–Marquardt and the
adaptive nonlinear least-squares algorithm of Dennis, Gay and "Walsh" (as printed; §3.4,
Eqs. (3.16)–(3.17)). The abstract calls the problem "regularized", but
§3.4 gives no regularization term or stopping criterion.

**Mesh management.** Elements next to an unfitted interface flatten as the
residual falls. Elements with a negative or too small Jacobian are removed
by edge swaps with cap removal, edge collapse for needles and an edge split
after each collapse, which keeps the numbers of triangles, points and
boundary faces fixed (§3.5, Figs. 6–7). The solver tolerates tangled
meshes and negative density or pressure during the iterations, but the
authors call solutions on tangled meshes "either non-physical or
meaningless".

## Why the jump condition fits discontinuities

Luo et al. verify the mechanism on Riemann data, along a straight
space–time face from $(x_i^n,t^n)$ to $(x_i^{n+1},t^{n+1})$ (Lemmas 1–2,
Eqs. (3.8)–(3.13)):

- **Linear advection**, $\partial_tu+a_0\partial_xu=0$ with page-local
  speed $a_0$: the interface condition holds iff
  $x_i^{n+1}=x_i^n+a_0(t^{n+1}-t^n)$, so the contact moves at the
  advection speed.
- **Burgers**, $\partial_tu+\partial_x(u^2/2)=0$: it holds iff
  $x_i^{n+1}=x_i^n+\tfrac12(u_l+u_r)(t^{n+1}-t^n)$, with page-local left
  and right states $u_l$, $u_r$, the Rankine–Hugoniot shock speed.

The intermediate equations (3.9) and (3.12) print a plus sign between the
two terms. With the face normal proportional to $(\Delta t,-\Delta x)$ the
sign is minus, and only then do the printed conclusions (3.10) and (3.13)
follow *(compiler check, not in the sources)*. No entropy condition enters:
the Burgers equation is satisfied equally by an entropy-violating jump with
$u_l<u_r$ *(compiler check, not in the sources)*.

## Evidence

| test | mesh | result (Luo et al.) |
|---|---|---|
| [Sod shock tube](/benchmarks/sod-and-lax-shock-tubes.md), $t=0.2$ | 8 space–time quadrilaterals, six degenerate at the origin | shock and contact fitted as true discontinuities; rarefaction head and tail "virtually resolved exactly" at $N=2,3$; an initial grid with a negative-volume element changes nothing significant |
| Lax problem, $t=0.15$ | 8 quadrilaterals | same behaviour |
| [123 (receding-flow) problem](/benchmarks/double-rarefaction-problem.md), $t=0.15$ | 16 quadrilaterals, $N=2$ | the two cells at the initial jump collapse and are removed; profiles without "overheating" |
| Noh problem, $\gamma=5/3$, $t=1$ | 4 quadrilaterals, $N=1$ | residuals reach $10^{-8}$–$10^{-9}$ in about 50 iterations; solution "virtually identical" to the exact one |
| Mach 3 flow past a 15° wedge | 189 triangles, $N=1$ | oblique shock fitted in about 20 iterations |
| Mach 2 diamond wedge in a channel | 500 triangles, $N=1$ | shock reflection, shock–shock interaction and expansion fan resolved |
| half cylinder at $M_\infty=8$ and $15$ | 315 and 497 triangles, $N=1$ | bow shock fitted, no [carbuncle](/definitions/carbuncle-phenomenon.md) |

The space–time elements are tensor-product, of degree $N$ in each variable
*(compiler check, not in the sources: the printed abscissae equal
$\log_{10}(1/\sqrt{(N+1)^2\cdot3\cdot8})$)*. Under p-refinement the $L^2$ space–time density error falls with slopes
8.75 and 10.48 (Sod) and 6.59 and 8.44 (Lax) against
$\log(1/\sqrt{\mathrm{DOFs}})$, three degrees per problem (§IV.A–B,
Tables 1). No test compares with a shock-capturing scheme.

## Qualifications

- **Scope of the claims.** The authors write that MDG+ICE reaches "the
  formal rate of p-convergence even for discontinuous solutions … that no
  other numerical methods can", and that it removes overheating "which no
  other numerical methods can". The first rests on three data points per
  problem. They cite but do not discuss the optimization-based implicit
  shock tracking of Zahr & Persson (ref. 44).
- **"Interface conservation" is not discrete conservation.** Luo et al.
  write that shock capturing has "a fatal flaw" because interface
  conservation "can never be achieved for discontinuities" (§I). Their
  interface conservation is the pointwise face condition above. A
  conservative shock-capturing scheme is discretely conservative, which is
  what the [Lax–Wendroff theorem](/results/lax-wendroff-theorem.md) uses;
  the two statements concern different properties *(compiler check, not
  in the sources)*.
- **Stability of the central flux.** The central interior flux is said to
  enhance stability for under-resolved flows. The paper attributes
  stability to the converged interface condition and gives no analysis.
- **Title.** Page 1 of the manuscript read says "Interface Conservation
  Enforcement"; the published title, per Crossref, says "interface
  condition enforcement".

# Citations

- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §I, §3.1–3.5 Eqs. (3.1)–(3.17), Lemmas 1–2, Figs. 2–7, §IV.A–E Figs. 8–28, Tables 1, §V (author manuscript).
