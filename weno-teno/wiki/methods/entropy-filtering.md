---
type: Method
title: "Entropy filtering for DG and FR"
description: "Entropy filtering applies, after every Runge–Kutta stage, an elementwise exponential modal filter whose single strength is the smallest value making the nodal values positive and above a local minimum of the entropy, under the assumption that the element mean already is; the page gives the filter, the constraints, the algorithm and the Navier–Stokes split."
status: established
aliases: [adaptive filtering, entropy-based adaptive filtering, positivity-preserving entropy filtering, constraint-driven modal filtering]
tags: [dg, flux-reconstruction, limiting, positivity, entropy-stable, bound-preserving]
timestamp: 2026-10-22T20:00:00Z
---

# Entropy filtering for DG and FR

**Entropy filtering**, proposed by
[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md), is a shock-capturing
and positivity-preserving post-processing for nodal discontinuous spectral
element methods: nodal [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
and [flux reconstruction](/methods/flux-reconstruction.md) with DG correction
functions. After every stage of an [SSP Runge–Kutta](/methods/ssp-runge-kutta.md)
method, each element whose nodal values violate a constraint is replaced by
a modally filtered version of itself, with the filter strength chosen as the
smallest one for which the nodal values satisfy (i) positivity of convex
constraint functions $g_i$ (registry §8; density and pressure for Euler) and
(ii) a local discrete minimum principle on an entropy. Smooth, resolved
elements are left untouched; at a shock the filter damps the high modes as
much as the constraints require and no more. The authors present it as a
nonlinear generalization of the
[Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md) and
call the name a reference to filtering the modes that drive the violation
of a minimum entropy principle (§3.1).

## Setting and the mean-value assumption

Let the element $K$ carry nodal values $u_j$ at closed (Gauss–Lobatto-type)
solution nodes $j\in S$, with modal coefficients $\hat u_j$ in an orthogonal
basis $\psi_j$ (Legendre on tensor elements, Proriol–Koornwinder–Dubiner–Owens
on triangles) of degree $n_j\le N$ (page-local $S$, $\hat u_j$, $\psi_j$,
$n_j$; the source writes $p_i$ for $n_j$ and $\mathbb P_p$ for the degree $N$)
(§2.2–§2.3, §4.2). The method rests on one assumption (§2.2, Eq. (10)): the
element mean evolves like a first-order finite-volume scheme, which holds
for nodal DG with suitable quadrature and for FR with DG correction
functions, and therefore, with SSP time stepping, a CFL condition and a
positivity-preserving, entropy-stable Riemann solver (Godunov, local
Lax–Friedrichs, or HLLC with suitable wave speeds), the element mean
satisfies the positivity constraints and the local minimum entropy
principle. The authors attribute these properties to Zhang & Shu, Zhang,
Xia & Shu and Chen & Shu, "without presenting a comprehensive proof"
(§2.2, §4.1).

## The filter

A filter maps $\hat u_j\mapsto H_j(\hat u_j)$, and is required to be
**dissipative**, $\lvert H_j(\hat u_j)\rvert\le\lvert\hat u_j\rvert$, and
**conservative**, the element mean unchanged (§2.3, Eqs. (13)–(15)). The
adaptive scheme needs four properties only: one free parameter, conservation,
a value that returns the unfiltered solution, and a value that returns the
element mean (§3.1). The chosen filter is the second-order exponential one,
$$H_j(\hat u_j)=\hat u_j\,e^{-\zeta_{\mathrm F}n_j^2},$$
(Eq. (18); $\zeta_{\mathrm F}\ge0$ the filter strength, page-local; the
source writes $\zeta$): $\zeta_{\mathrm F}=0$ is the unfiltered solution and
$\zeta_{\mathrm F}\to\infty$ the mean, reached in practice at
$\zeta_{\mathrm F}=O(-\ln\epsilon_{\mathrm m})$ with $\epsilon_{\mathrm m}$
the machine precision (page-local). One scalar $\zeta_{\mathrm F}$ acts on
all components of the element (Alg. 2).

## The constraints and the strength

The strength is (Eq. (19))
$$\zeta_{\mathrm F}=\min\Big\{\zeta\ge0:\ g_i\big(\tilde u(x_j)\big)\ge0,\ \ (\rho s)\big(\tilde u(x_j)\big)\ge(\rho s)^K_{\min}\ \ \forall j\in S\Big\},$$
with $\tilde u$ the filtered element solution. The constraints are imposed
**at the solution nodes only**, not over the whole element (§3). Because the
mean satisfies them and the filter tends to the mean, a feasible value
exists, with at least one inequality active; it is "generally unique,
although this is not guaranteed", and convergence to a local minimum is
accepted (§3.1).

**Local entropy bound** (§3.2, Eqs. (20)–(21), Alg. 1). The bound is the
minimum of the nodal entropy at the previous stage over the element and its
face neighbours, boundary elements using the boundary state. Under "some
standard CFL condition" (the source's wording) the domain of influence of one step lies within the
element and its direct neighbours, so the bound, computed before the step
and enforced after it, makes the local discrete minimum entropy
non-decreasing over its domain of influence. Any admissible entropy pair may
be used; the choice is "posited to have a minor overall effect" (§3.2).

**Euler instantiation** (§4.1, §4.3). $g_1=\rho-\rho_{\min}$,
$g_2=p-p_{\min}$ with floors $\rho_{\min}=p_{\min}=10^{-8}$, and the entropy
functional $\rho s=\rho\ln(p\rho^{-\gamma})$ with entropy flux $\rho s\,v$,
in the physical sign convention (entropy increasing; in registry terms
$\rho s=-(\gamma-1)\eta$). The entropy constraint is relaxed by an absolute
tolerance $\epsilon_\sigma=10^{-4}$ (page-local; Eq. (27)), because the
logarithm makes it sensitive to round-off near the floors and because strict
entropy enforcement can degrade accuracy (§4.3, citing convex-limiting and
Khobalatte–Perthame-type work).

## Algorithm

Per element and per stage (§4.3, App. A, Algs. 1–3):

1. compute the local entropy bounds from the previous (sub)stage;
2. if all nodal values satisfy the constraints (with the tolerance), keep
   the element;
3. otherwise bisect on $[0,-\ln\epsilon_{\mathrm m}]$, $\epsilon_{\mathrm m}=10^{-8}$,
   for 20 iterations, evaluating $\tilde u=\mathbf V(\hat u\odot e^{-\zeta_{\mathrm F}n^2})$
   with the Vandermonde matrix $\mathbf V$ (page-local), and return the
   feasible end of the bracket, so that the returned state always satisfies
   the constraints.

The cost on a smooth problem
([isentropic vortex](/benchmarks/isentropic-vortex.md), $N=3$, $40^2$
elements, five flow-throughs, one NVIDIA V100) is +1.1%, +1.7% and +2.0% of
the time to solution for 5, 10 and 20 bisection iterations (§5.1.3).

**Navier–Stokes** (§4.1, Alg. 4). The mean-value assumption fails for the
mixed hyperbolic–parabolic discretization, so the stage is split
explicitly: the inviscid update is filtered with positivity and entropy
constraints, the viscous increment is added, and the result is filtered
again with positivity only ($(\rho s)_{\min}=-\infty$). No-slip walls are
replaced by slip walls for the hyperbolic step. A parabolic discretization
that kept the minimum entropy principle on the mean would make the split
unnecessary (Remark, §4.1).

## Relation to other limiters

- **Scaling limiter.** With the degenerate "filter" $H_j(\hat u_j)=\hat u_j$
  for $n_j=0$ and $\zeta\hat u_j$ otherwise, the procedure is the Zhang–Shu
  linear convex limiter with $\theta=\zeta$ between the mean ($\zeta=0$) and
  the high-order solution ($\zeta=1$); with a nontrivial filter it is "a
  nonlinear (and generally non-convex) limiting operation" (Remark
  (Limiting), §3.1). The parametrization is reversed with respect to the
  exponential filter, where $\zeta_{\mathrm F}=0$ is the high-order
  solution. The strength is chosen from the constraints as $\theta$ is in
  the scaling limiter, but the exponential filter damps mode $j$ by
  $e^{-\zeta_{\mathrm F}n_j^2}$, more the higher its degree, whereas the
  scaling limiter damps every non-mean mode by the same factor $\theta$
  *(compiler check, not in the sources: compare Eq. (18) with the
  degenerate filter of the Remark)*; the source states that higher modes
  are damped more (§2.3).
- **Convex limiting and FCT.** Dzanic & Witherden name flux-corrected
  transport and [convex limiting](/methods/convex-limiting.md) as related
  approaches (§3.1).
- **Modal damping.** [OEDG](/methods/oedg.md) also multiplies each modal
  coefficient by an exponential in its degree, but with a strength computed
  from interface jumps in every cell, not from constraints
  ([Peng, Sun & Wu (2024)](/sources/peng-2024.md), §2.2); the
  [artificial viscosity](/methods/artificial-viscosity.md) page reads both
  as exponential modal filters, Peng, Sun & Wu relating their damping to
  spectral viscosity and filtering (Rem. 2.3, §1.2).
- Filtering is one of four classes of shock capturing for discontinuous
  spectral element methods named by the source, with artificial viscosity,
  limiting and stencil modification; it is attractive because it resolves
  discontinuities sharply at low cost without changing the underlying
  scheme (§1).

## Evidence

All runs use PyFR ([PyFR](/software/pyfr.md)): FR with DG correction
functions, HLLC, BR2 viscous fluxes, SSP-RK3, Gauss–Lobatto nodes on tensor
elements and $\alpha$-optimized nodes on simplices (§4.2, §5).

| Test | Setup | Finding |
|---|---|---|
| [Sod](/benchmarks/sod-and-lax-shock-tubes.md) | $N=2$–7, $t=0.2$ | first-order convergence: least-squares rates in $L^1$ 0.91, 0.94, 0.93, 0.92, 0.87, 0.86 and in $L^2$ 1.05, 0.98, 1.01, 1.01, 0.98, 1.03 (Tables 1–2); at fixed degrees of freedom lower $N$ gives marginally lower error, attributed to a more localized filter (Tables 3–4) |
| [Shu–Osher](/benchmarks/shu-osher-problem.md) | $N=3$, 100 and 200 elements, $t=1.8$ | compared with an exact-Godunov reference (§5.1.2) |
| [isentropic vortex](/benchmarks/isentropic-vortex.md) | $N=2$–7 | $L^2$ rates 2.59, 4.00, 4.27, 6.73, 6.10, 8.13, "generally in the range of $p$ to $p+1$" (Table 5) |
| [double Mach reflection](/benchmarks/double-mach-reflection.md) | $N=3$, $2400\times600$, $t=0.2$ | sub-element shock resolution, slip-line roll-up kept; the filter is active mainly at the shocks, far below the mean-mode strength (Fig. 4) |
| [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md) | $N=4$, $100^2$–$800^2$, unseeded, $t=2$ | roll-up resolved, no spurious oscillations (Fig. 5) |
| [Mach 800 jet](/benchmarks/high-mach-astrophysical-jet.md) | $N=3$, $200\times600$ and $800\times2400$, $t=0.002$ | robust; "significantly better resolution" than Wu & Shu's DG with the linear scaling limiter, partly attributable to the magnetic field in that computation (Fig. 6) |
| [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) | Re 1600, $M=0.08$, $N=3$–5, about $96^3$–$160^3$ degrees of freedom | agrees with DNS and with unfiltered runs: the filter is predominantly inactive (Fig. 7) |
| Daru–Tenaud viscous shock tube | $N=4$, $800\times400$, viscosity $10^{-3}$–$10^{-4}$, $t=1$ | agrees with Guermond et al.; about 16 elements need the positivity re-filter after the viscous step, with strength about $10^{-4}$ (Figs. 8–9) |
| VFE-2 delta wing LES | $N=3$, 4.1 M mixed elements, 104 M degrees of freedom per component, Re $3\cdot10^6$, $M=0.8$ | surface pressure agrees with PSP data at three of four stations (Figs. 10–11) |

## Qualifications

- **Guarantee.** Positivity and the entropy bound hold at the solution nodes
  and rest on the assumed properties of the element mean; between nodes the
  filtered polynomial may violate them (§2.2, §3).
- **Parameters.** The paper calls the approach "free of problem-dependent
  tunable parameters" (§6). The floors, the absolute entropy tolerance and
  the iteration count are global constants, not tuned per problem; the
  tolerance is absolute, hence scale-dependent, and a better way to set it
  is listed as future work (§6).
- **Which entropy.** The constraint bounds the density-weighted entropy
  $\rho s$: §4.1 sets the functional to $\sigma=\rho\log(P\rho^{-\gamma})$,
  with entropy flux $v\sigma$ (arXiv v3, p. 6). The minimum entropy
  principle of Tadmor concerns the specific entropy $s$, which other
  sources bound ([bound preservation](/properties/bound-preservation.md),
  [convex limiting](/methods/convex-limiting.md)), and the paper does not
  argue that a local minimum principle holds for $\rho s$. The set
  $\{\rho s\ge c\}$ is nevertheless convex, since $\rho s=-(\gamma-1)\eta$
  is concave in the conserved variables *(compiler check, not in the
  sources: $\eta=-\rho s/(\gamma-1)$ is the convex entropy of registry
  §6)*. The paper also calls $\rho s$ "some convex entropy functional"
  (§3) while adopting the physical sign, under which it is concave.
- **Printed slips (arXiv v3).** Alg. 3 prints the second and third SSP-RK3
  stages as $\tfrac34u^n+\tfrac14u^{(1)}+\Delta t\,\mathcal L(u^{(1)})$ and
  $\tfrac13u^n+\tfrac23u^{(2)}+\Delta t\,\mathcal L(u^{(2)})$; on
  $\dot u=\lambda u$ this gives the amplification
  $1+\tfrac{11}{6}\lambda\Delta t+\dots$, not first-order consistent, and the
  factors $\tfrac14$ and $\tfrac23$ on $\Delta t$ of the Shu–Osher form are
  missing (also in Alg. 4) *(compiler check, not in the sources)*. Alg. 4
  updates $u^{n+1}$ from itself in its last stage, where the filtered
  inviscid state is meant. Tables 1–4 print $L^2$ errors smaller than
  $L^1$ errors throughout, which the point-mean definitions of Eq. (28)
  exclude, since the root-mean-square of a set of numbers is not smaller
  than their mean absolute value *(compiler check, not in the sources)*.

# Citations

- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — arXiv v3: §1; §2.2–§2.3 (Eqs. (10)–(15)); §3.1 (Eqs. (16)–(19), Remark (Limiting)); §3.2 (Eqs. (20)–(21)); §4.1 (Eqs. (22)–(24), Remarks); §4.2; §4.3 (Eq. (27)); §5 (Tables 1–5, Figs. 2–11); §6; App. A (Algs. 1–4).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1.2; §2.2 (exponential damping of modes, for comparison); Rem. 2.3.
