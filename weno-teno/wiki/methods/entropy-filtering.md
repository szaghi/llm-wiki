---
type: Method
title: "Entropy filtering for DG and FR"
description: "Entropy filtering applies, after every Runge–Kutta stage, an elementwise exponential modal filter whose strength is the smallest making the nodal values positive and above a local entropy minimum, assuming the element mean already is; the page gives the filter, constraints, floors and tolerances, algorithm, Navier–Stokes split, ideal-MHD operator split and faster strength solve."
status: established
aliases: [adaptive filtering, entropy-based adaptive filtering, positivity-preserving entropy filtering, constraint-driven modal filtering]
tags: [dg, flux-reconstruction, limiting, positivity, entropy-stable, mhd]
timestamp: 2026-10-23T16:00:00Z
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

## Ideal MHD: operator-split filtering

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) extend the method to
ideal MHD on the same nodal DG/FR discretizations. The solenoidal
constraint is handled by Powell's eight-wave non-conservative source
$S_B(u)=-(0,\,B,\,v,\,v\cdot B)^\top\nabla\cdot B$, with the *global* discrete
divergence, interior plus interface-jump terms, rather than the interior
one, which they call usually sufficient in practice (§2.3, Eqs. (17)–(19);
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
The constraints are positivity of $\rho$ and $p$ and the local minimum
principle on the specific quantity $p\rho^{-\gamma}$, each required to be
strictly positive at the solution nodes (§3.1 Eqs. (20)–(22)). In the
implementation one constant $\epsilon=10^{-8}$ (page-local) is subtracted
from all three, $\rho-\epsilon$, $p-\epsilon$ and
$p\rho^{-\gamma}-(p\rho^{-\gamma})^K_{\min}-\epsilon$, "to avoid a vacuum
state for the Riemann solver and apply a numerical tolerance to the entropy
condition" (§4). As printed, the third constraint asks $p\rho^{-\gamma}$ to
exceed its local minimum by $\epsilon$, a margin, whereas the 2022 entropy
tolerance lets $\rho s$ fall below its minimum by $\epsilon_\sigma$ *(compiler
check, not in the sources: compare §4 with Alg. 2 of the 2022 paper)*.

**Why a split.** With the source term the mean-value argument no longer
gives an admissible element mean. Positivity of the mean is known when
$B$ is locally divergence-free (Wu & Shu), and the source-free update
$u^*=u^n+\Delta t\,\mathcal L_1(u^n)$, $\mathcal L_1=-\nabla\cdot f$, has an
admissible mean by the Bouchut–Klingenberg–Waagan solver and the
Zhang–Shu mean/Godunov equivalence, as they recall (§3.2, Eqs.
(29)–(31)). They therefore filter in two steps (Eqs. (32)–(33)):

$$\tilde u^*=H_{\mathrm e}\big[u^n+\Delta t\,\mathcal L_1(u^n)\big],\qquad
\tilde u^{n+1}=H_{\mathrm p}\big[\tilde u^*+\Delta t\,S_B(u^n)\big],$$

with $H_{\mathrm e}$ the filter with positivity and entropy constraints and
$H_{\mathrm p}$ (page-local) the filter with positivity only; each
SSP-RK3 stage is wrapped the same way, the entropy bounds taken from the
previous stage (Eq. (34)). The source is added with the old state, not in
a Strang-type split, to keep the temporal accuracy (§3.2). This is the
structure of the Navier–Stokes split above with the viscous increment
replaced by the Powell source *(compiler check, not in the sources)*.
The authors state that positivity of the DG element mean for a magnetic
field that is not exactly divergence-free "remains to be proven", so the
existence of an admissible filter strength is not guaranteed; in practice
the second filter is "very rarely" needed (§3.2). Unless the linear kernel
of the Zhang–Shu limiter is used, the nonlinear filter can raise the
divergence error slightly, which the source term then corrects; the effect
was "found to be negligible" (§3.2).

## Faster filter-strength solve

The 2022 algorithm evaluates the filtered solution with a full
matrix–vector product at every bisection step; Dzanic & Witherden (2023)
call this "quite computationally expensive" and replace it (§4.1, Eqs.
(35)–(37)):

1. solve for $\mathsf f=e^{-\zeta_{\mathrm F}}\in[0,1]$ (page-local), so that
   mode damping is the integer power $\mathsf f^{n_j^2}$;
2. precompute the degree-$k$ components $u^{(k)}=\mathbf V\,I^{(k)}\mathbf V^{-1}u$,
   $I^{(k)}$ the diagonal selector of modes of degree $k$, so that the
   filtered solution is $\tilde u=\sum_{k=0}^N\mathsf f^{k^2}u^{(k)}$ with no
   matrix product inside the iteration;
3. solve node by node with the Illinois (modified regula falsi) method,
   tolerance $10^{-8}$, at most 20 iterations, using each node's value as
   the upper bracket for the next and skipping nodes already admissible;
   the element value is $\mathsf f=\min_j\mathsf f_j$.

They state that the filter then costs "typically less than" the flux
divergence. On 16 NVIDIA V100 GPUs, for the weakly magnetized 3D
Rayleigh–Taylor run to $t=1$, the run time falls from 61.4 to 25.3 GPU
hours at $N=3$ ($64\times64\times128$ elements) and from 257 to 39.8 GPU
hours at $N=4$ ($51\times51\times102$, about the same number of degrees of
freedom), speed-ups of about 2.4 and 6.5 that grow with the order (§5.6,
Fig. 17).

The 2022 overhead of 1–2 % of the time to solution was measured on a
smooth isentropic vortex; the 2023 figures are whole-run times of a 3D
magnetized Rayleigh–Taylor instability. The two statements
concern different problems *(compiler check, not in the sources)*.

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

Ideal MHD (Dzanic & Witherden (2023), §5; HLLC with Davis wave speeds
except HLL for the blast, SSP-RK3, fixed $\Delta t$):

| Test | Setup | Finding |
|---|---|---|
| near-vacuum magnetized vortex (Christlieb et al.) | $N=2$–5, $20^2$–$67^2$, $t=0.05$ | $L^1$ rates of the magnetic-field error 2.89, 3.80, 4.62, 5.23; largest $1-\mathsf f$ from about $10^{-4}$ down to $3.3\times10^{-8}$ in Table 2, while the text says $10^{-7}$ (Tables 1–2, §5.1) |
| [Brio–Wu](/benchmarks/brio-wu-shock-tube.md) | $N=3$, 200 and 400 elements, $t=0.1$ | sub-element shocks and rarefactions, minor density oscillations between the compound wave and the contact (Fig. 2) |
| [Orszag–Tang](/benchmarks/orszag-tang-vortex.md) | $N=3$, $64^2$–$256^2$ | oscillations vanish with refinement; $\lvert\nabla\cdot B\rvert$ concentrated at strong gradients and decreasing with resolution; pressure cut agrees with a WENO reference (Figs. 3–6) |
| shock–cloud interaction | $N=2$, $400^2$, $t=0.06$ | comparable with Wu & Shu's DG with WENO limiter, "marginally better" on small scales; diverges with negative pressure without the positivity filter (Figs. 7–9) |
| [magnetized blast](/benchmarks/mhd-blast-wave.md), pressure ratio $10^5$, $B_0=1000/\sqrt{4\pi}$ | $N=4$ on triangles, $h=1/200$ and $1/400$ | discontinuities resolved over one to two nodes; without positivity treatment "would diverge almost instantly" (Figs. 10–13) |
| 3D magnetized [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md) | $N=3$, $64\times64\times128$, $B_0=0$, $0.1B_c$, $0.5B_c$, cutoff field $B_c=\sqrt2$ (page-local) | well behaved in all three regimes; the field slows the growth (Figs. 14–16) |

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
  The MHD paper, Dzanic & Witherden (2023), bounds the specific quantity
  $p\rho^{-\gamma}=e^s$ instead, and presents the method as the 2022 one
  without remarking on the change of functional (§3.1, §4).
- **Floors and tolerances are different quantities.** In the 2022 paper
  $10^{-8}$ is the positivity floor, $\rho_{\min}=p_{\min}=10^{-8}$, and
  $10^{-4}$ is the separate absolute tolerance $\epsilon_\sigma$ by which
  $\rho s$ may fall below its local minimum (§4.3, Alg. 2). In the 2023
  paper a single $\epsilon=10^{-8}$ is both the positivity floor and the
  entropy offset, applied with the opposite sign (§4; see above). Both are
  absolute, so their effect depends on the scale of the data *(compiler
  check, not in the sources)*.
- **MHD guarantee gap.** The title's positivity preservation rests, for
  the source-term step, on an unproven property of the element mean
  (Dzanic & Witherden (2023), §3.2); the evidence is the tests. The
  Powell form is non-conservative, which the authors note can cause
  inaccurate predictions near discontinuities, after Tóth (§2.3).
- **Printed slips (Dzanic & Witherden (2023), arXiv v2).** With the
  printed vortex data $\delta p=-\mu_{\mathrm v}^2(1+r^2)\phi(r)^2/(8\pi^2)$,
  $\phi=\exp(1-r^2)$ (page-local $\phi$, $\mu_{\mathrm v}=5.38948938512$, $r$ the radius;
  Eqs. (39)–(40)), the minimum pressure is
  $1-\mu_{\mathrm v}^2e^2/(8\pi^2)\approx-1.72$, not the stated
  $\approx2\times10^{-8}$; the stated value is $1-\mu_{\mathrm v}^2e/(8\pi^2)$,
  obtained with $\phi$ unsquared or with $\phi=\exp((1-r^2)/2)$, so one
  exponent is misprinted *(compiler check, not in the sources)*. The
  plasma beta of the extreme blast is printed as $\approx2.5\times10^{-4}$;
  with their $\beta_{\mathrm p}=2p/\lvert B\rvert^2$, $p=0.1$ and
  $B_0=1000/\sqrt{4\pi}$ it is $2.5\times10^{-6}$, the printed value
  belonging to the original $B_0=100/\sqrt{4\pi}$ *(compiler check, not in
  the sources)*. Eq. (36) prints the sum over degrees with a mismatched
  index; Eqs. (35) and (37) fix it as written above.
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
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — arXiv v2: §2.1 Eq. (5); §2.3 Eqs. (17)–(19); §3.1 Eqs. (21)–(22); §3.2 Eqs. (29)–(34); §4, §4.1 Eqs. (35)–(37); §5 Tables 1–2, Figs. 2–17.
