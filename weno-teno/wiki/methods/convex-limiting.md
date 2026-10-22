---
type: Method
title: "Convex limiting and invariant-domain-preserving schemes"
description: "Convex limiting blends a high-order update with a bound-preserving low-order update, adding as much antidiffusive flux as target bounds allow; the page gives the FCT form, graph viscosity and bar states, Pazner's sparse low-order DG operator, the Zalesak and convex limiters, element- versus subcell-wise blending, bound relaxation, and the equivalence of subcell Rusanov finite volumes with sparse IDP DG."
status: established
aliases: [flux-corrected transport, FCT, algebraic flux correction, AFC, invariant-domain-preserving limiting, IDP limiting, a posteriori blending, Zalesak limiter, sparse IDP DG, subcell convex limiting]
tags: [limiting, bound-preserving, positivity, dg, entropy-stable]
timestamp: 2026-10-22T20:00:00Z
---

# Convex limiting and invariant-domain-preserving schemes

Convex limiting starts from a low-order update that is
[bound-preserving](/properties/bound-preservation.md) by construction and adds
to it as much of the difference "high-order minus low-order" as a set of
target bounds allows. The result is a convex combination of the two updates
(per element, per node or per interface), so it stays conservative and
inherits whatever convex constraints the bounds encode. The family descends
from flux-corrected transport (Boris–Book, Zalesak, Löhner, Kuzmin) and the
invariant-domain-preserving (IDP) methods of Guermond and Popov, as recalled
by [Pazner (2021)](/sources/pazner-2021.md) (§1, §4),
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
(§2.4) and [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) (§1, algebraic
flux correction). Pazner (2021) is the source of the sparse IDP DG method
with subcell convex limiting that the later paper recasts.

## FCT form

Pazner (2021) (§4, Eqs. (44)–(47)) writes the forward-Euler step with
high- and low-order residuals $r^{\mathrm H}_i$, $r^{\mathrm L}_i$ of node
$i$ and lumped mass $m_i$ (page-local) as
$$\frac{m_i}{\Delta t}u^{n+1}_i=\frac{m_i}{\Delta t}u^n_i+r^{\mathrm L}_i+(1-\alpha_i)\big(r^{\mathrm H}_i-r^{\mathrm L}_i\big),$$
and Rueda-Ramírez et al. (2022) write the same step, to which SSP
Runge–Kutta stages reduce, being convex combinations of Euler steps, with
interface fluxes:
$$u^{n+1}_{ij}=u^{\mathrm{FV},n+1}_{ij}+\sum_{k\in\mathcal N(ij)\setminus\{ij\}}\big(1-\alpha_{(ij,k)}\big)\,\Delta f^{\mathrm{ad}}_{(ij,k)},\qquad
\Delta f^{\mathrm{ad}}_{(i,i+1)j}=-\frac{\Delta t}{J_{ij}\mathsf w_i}\Big(\hat f^{\mathrm{DG}}_{(i,i+1)j}-\hat f^{\mathrm{FV}}_{(i,i+1)j}\Big)$$
(Eqs. (26)–(27)), with $\mathcal N(ij)$ the five-point low-order stencil of
node $ij$ (page-local), $\Delta f^{\mathrm{ad}}$ the mass-weighted
antidiffusive flux (page-local; the source writes $\bar f$), $J_{ij}$ the
element Jacobian and $\mathsf w_i$ the LGL weight. On this page the
blending coefficient $\alpha$ is the weight of the **low-order** scheme
($\alpha=0$ pure high-order, $\alpha=1$ pure low-order), as in Rueda-Ramírez
et al.; Pazner uses the FCT convention, in which his limiter value 1 means
full antidiffusion, so his coefficient is $1-\alpha$. Pazner's high-order
target is the strong form of the DGSEM, chosen because the weak form is not
free-stream preserving on curved meshes (Prop. 3, §2.4.2).

## The low-order scheme: graph viscosity and bar states

**Graph viscosity** ([Pazner (2021)](/sources/pazner-2021.md), §3.1,
Eqs. (30)–(40), after Guermond and Popov). With the local Lax–Friedrichs
interface flux merged into the volume coefficients, the low-order
semi-discretization takes the graph form
$$m_i\,\dot u_i=\sum_{j\in\mathcal N(i)}\hat c_{ij}\cdot f(u_j)+\sum_{j\in\mathcal N(i)}\hat d_{ij}(u_j-u_i),\qquad
\hat d_{ij}=\max\big\{a_{\max}(u_i,u_j,n_{ij})\lVert\hat c_{ij}\rVert,\ a_{\max}(u_j,u_i,n_{ji})\lVert\hat c_{ji}\rVert\big\},$$
with $\sum_j\hat c_{ij}=0$ (constant preservation) and a zero-sum, symmetric
viscosity (Prop. 5; $\hat c_{ij}$, $\hat d_{ij}$, $n_{ij}=\hat c_{ij}/\lVert\hat c_{ij}\rVert$,
$a_{\max}$ page-local; the local Lax–Friedrichs flux is chosen because it
is compatible with this viscosity). The forward-Euler step is then the
convex combination
$$u^{n+1}_i=\Big(1-\sum_{j\ne i}\frac{2\Delta t\,\hat d_{ij}}{m_i}\Big)u^n_i+\sum_{j\ne i}\frac{2\Delta t\,\hat d_{ij}}{m_i}\,\breve u_{ij},\qquad
\breve u_{ij}=\tfrac12(u_i+u_j)+\frac{\hat c_{ij}}{2\hat d_{ij}}\cdot\big(f(u_j)-f(u_i)\big)$$
(Eqs. (38)–(39)) of the **bar states** $\breve u_{ij}$ (page-local; both
sources write $\bar u$, which the registry reserves for cell averages), which lie in every
convex invariant set that contains $u_i$ and $u_j$ (Prop. 6, proof deferred
to Guermond, Popov & Tomas). The low-order scheme is therefore IDP under
$\Delta t\le\min_i m_i/(2\sum_{j\ne i}\hat d_{ij})$ (Prop. 7, Eq. (40); see
Qualifications for the printed sign).
[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) (Eq. (25))
write the bar state between nodes $a$ and $b$ as
$\breve u_{ab}=\tfrac12(u_a+u_b)+\frac{1}{2a_{ab}}\big(f_n(u_a)-f_n(u_b)\big)$
with the flux $f_n$ normal to the subcell interface; the opposite sign of
the flux difference is a convention of the normal's direction (Pazner's
$\hat c_{ij}$ comes from the transposed, weak-form derivative), not a
different state.

**Sparsification** (Pazner, §3, Eq. (23), §3.1, Eqs. (25)–(29)). Every
connection of the stencil adds viscosity. Built on the dense DGSEM
derivative, which couples each node to $O(N)$ others, the graph-viscosity
scheme becomes very dissipative as $N$ grows at fixed degrees of freedom
(as observed by Lohmann et al., and shown in Fig. 1 for $N=3,7,15,31$ on
128 degrees of freedom). Pazner replaces the weighted 1D derivative $Q=MD$ by
$\widehat Q$, the weighted derivative of piecewise-linear hat functions on
the Gauss–Lobatto subgrid: tridiagonal with entries $\pm\tfrac12$, an
$O(1)$ stencil independent of $N$, conservative and SBP. The metric terms
are then perturbed by $O(h)$, with the minimum-norm correction of an
underdetermined system computed once by SVD on the reference element, to
restore the discrete metric identities and free-stream preservation
(Prop. 4; [free-stream preservation](/properties/free-stream-preservation.md)).
The sparsified low-order method shows no degradation with $N$ (Fig. 1).
For variable-velocity advection the bar states and the viscosity are
modified (Eqs. (42)–(43)), which requires a discrete divergence-free
condition on the velocity in the metric correction (§3.3).

## Target bounds

Three kinds are used (Pazner, §4.1.1, §4.3; Rueda-Ramírez et al. 2022,
§2.4, §5):

1. **Local min/max bounds** (Rueda-Ramírez et al. 2022, Eqs. (23)–(24)):
   $\min_{k\in\mathcal N(ij)}\rho(u^\star_k)\le\rho_{ij}\le\max_{k\in\mathcal N(ij)}\rho(u^\star_k)$,
   with $u^\star=u^n$ or $u^\star=u^{\mathrm{FV},n+1}$ when the low-order
   scheme is monotone (page-local $u^\star$). Pazner lists $u^n_j$,
   $u^{\mathrm L,n+1}_j$ and the bar states as candidates, notes that the
   low-order solution is the most restrictive because it is a convex
   combination of bar states, and takes the bar-state extrema
   $u^{\min,\max}_i=\min,\max_{j\in\mathcal N(i)}\breve u_{ij}$ (Eq. (51)).
2. **Bar-state and entropy bounds for Euler.** Both sources limit the
   density with a Zalesak limiter between bar-state bounds
   ($\min_k\breve\rho_{(ij,k)}\le\rho_{ij}\le\max_k\breve\rho_{(ij,k)}$;
   Pazner Eq. (66), Rueda-Ramírez et al. Eq. (47)) and add a local minimum
   principle on a specific entropy, enforced by convex limiting with a
   Newton-type line search. Pazner bounds
   $s=\ln\big(e^{1/(\gamma-1)}\rho^{-1}\big)$ from below by its minimum over
   the neighbouring states at $t^n$, not over bar states (Eq. (67)), in the
   convex invariant set $\{\rho>0,\ e>0,\ s\ge r\}$ (Eq. (65)); the
   entropy bound also keeps the internal energy positive. Rueda-Ramírez et
   al. bound the modified specific entropy $e\rho^{1-\gamma}$ (Eq. (48)),
   which they prefer to $\ln(p\rho^{-\gamma})$ as cheaper and better suited
   to Newton's method; the two are monotone functions of each other,
   $s=\frac{1}{\gamma-1}\ln(e\rho^{1-\gamma})$, so the bounded sets coincide
   *(compiler check, not in the sources)*. Bar states preserve every convex
   invariant of the system, and together these bounds guarantee positivity
   of density and pressure and a discrete entropy inequality (as recalled
   from Guermond et al.).
3. **Bounds relative to the low-order solution** (Rueda-Ramírez et al.
   2022, after Rueda-Ramírez & Gassner, Eq. (43)):
   $\rho_{ij}\ge\beta_{\mathrm{FV}}\rho^{\mathrm{FV}}_{ij}$,
   $p_{ij}\ge\beta_{\mathrm{FV}}p^{\mathrm{FV}}_{ij}$ with
   $\beta_{\mathrm{FV}}=0.1$ (page-local).

**Relaxing the bounds for accuracy** (Pazner, §4.4, Eqs. (68)–(70)). Local
bounds clip smooth extrema. Pazner interpolates between local and global
bounds with a modal smoothness factor $\varepsilon_K\in[0,1]$ of the
element (the Persson–Peraire indicator of the
[troubled-cell indicator](/definitions/troubled-cell-indicator.md) page,
1 in rough or under-resolved elements):
$\hat u^{\min}_i=\varepsilon_Ku^{\min}_i+(1-\varepsilon_K)g_{\min}$, and
likewise for the maximum, with $g_{\min}$, $g_{\max}$ global bounds such as
the extrema of the initial data. In smooth elements only the global bounds
are enforced. On smooth advection the scheme then converges at order $N+1$
for $N=3,4,5$ ($L^1$ rates 4.00, 5.00, 5.86 at 64 elements), and without
the relaxation at about first order (rates 1.00, 1.04, 1.29), which Pazner
calls consistent with the literature (§5.1, Table 1).

## Computing the blending coefficient

- **Linear bounds, Zalesak-type limiter** (Rueda-Ramírez et al. 2022,
  Eq. (28); Pazner, §4.1). With $P^\pm$ the sums of the positive and
  negative antidiffusive contributions to the bounded quantity,
  $$\alpha^{+}_{ij}=1-\min\Big(1,\frac{\rho^{\max}_{ij}-\rho(u^{\mathrm{FV},n+1}_{ij})}{P^+}\Big),\qquad
  \alpha^{-}_{ij}=1-\min\Big(1,\frac{\rho^{\min}_{ij}-\rho(u^{\mathrm{FV},n+1}_{ij})}{P^-}\Big),$$
  $\tilde\alpha_{ij}=\max(\alpha^-_{ij},\alpha^+_{ij})$.
- **Nonlinear convex bounds** (Rueda-Ramírez et al. 2022, Eq. (29), after
  Guermond et al. and Pazner; Pazner, Eqs. (58), (60)). Choose the nodal
  coefficient so that every provisional state
  $u^{\mathrm{FV},n+1}_{ij}+\Gamma(1-\tilde\alpha_{ij})\Delta f^{\mathrm{ad}}_{(ij,k)}$,
  $\Gamma=2d$ ($d$ the dimension; Pazner prints $\gamma$), satisfies the
  bound: $2d$ scalar nonlinear problems per node, solved by
  Newton–bisection or Newton–secant iterations. Because the full update is
  the average $\frac{1}{\Gamma}\sum$ of these provisional states, it
  satisfies every convex bound (Pazner, Prop. 11, Eq. (62)).
- **Element-wise.** Each element takes the coefficient of its most
  limited node (Pazner, Eqs. (52), (59); Rueda-Ramírez et al. 2022, §2.4),
  which keeps conservation because the antidiffusive residuals sum to zero
  over the element (Pazner, Prop. 8). Linear constraints are then solved in
  closed form; nonlinear convex constraints need a nonlinear solve.
- **Subcell-wise.** The antidiffusive residuals also sum to zero along each
  line of nodes in each direction (Pazner, Prop. 9), so they are
  differences of subcell-face fluxes (Eqs. (53)–(54)); each face takes the
  more limiting of its two nodal coefficients (Pazner, Eq. (55), the
  minimum in his FCT convention; Rueda-Ramírez et al. 2022,
  $\alpha_{(i,m)j}=\max(\tilde\alpha_{ij},\tilde\alpha_{mj})$), and the
  update is conservative (Prop. 10). Pazner presents this
  dimension-by-dimension procedure as his improvement over the
  multidimensional subcell limiter of Lohmann et al., which required a
  minimization problem (§4.1.3).

Subcell-wise coefficients are stricter per interface, because each must
guarantee the bound independently of the others, yet they limit less in
practice: on an under-resolved Kelvin–Helmholtz instability they add about
three orders of magnitude less low-order method than element-wise blending
(Rueda-Ramírez et al. 2022, §5.2.1, Fig. 4), and at fixed degrees of
freedom element-wise limiting stops improving beyond $N=1$ while subcell
limiting improves with $N$ (Pazner, §4.1.4, Fig. 3); see
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).

## Sparse IDP DG is subcell Rusanov finite volumes

[Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) prove that the
subcell finite-volume scheme of Hennemann et al. on LGL subcells, with
first-order reconstruction and the Rusanov (local
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md)) flux, **is** Pazner's
low-order sparse IDP scheme in the graph form above (Prop. 1, Eqs.
(30)–(33)). The factor $\tfrac12$ in $\hat c$ is Pazner's sparsified
derivative matrix (their Eq. (34); Eq. (23) of Pazner's arXiv v1), and the
subcell metrics of Hennemann et al. solve Pazner's conservation condition
$\sum_j\hat c_{ij}=0$ (their Eq. (35); Prop. 5 of Pazner's arXiv v1)
exactly and analytically, so the SVD-based minimisation of Pazner's
construction is not needed (Prop. 2, Eqs. (35)–(36)). Pazner himself
describes the nodes as subcell-centred values but does not state the
equivalence (§4.1.3). The equivalence is why the bar-state bounds can
always be met for that low-order scheme: on the Mach 4 bow shock they hold
to machine precision (§5.2.2).

## A nonlinear relative: constraint-driven modal filtering

[Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) (§3.1, Remark
(Limiting)) name flux-corrected transport and convex limiting as related
to their [entropy filtering](/methods/entropy-filtering.md).
It shares the structure of choosing, per element, the least restrictive
member of a one-parameter family that meets convex nodal bounds (positivity
of density and pressure, and a local minimum of $\rho s$ over the element
and its face neighbours), but the family is an exponential modal filter of
the high-order solution, not a convex combination with a low-order update.
With a degenerate linear filter it reduces to the element-wise blend of the
high-order solution with its cell average, the
[Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md); with the
exponential filter it is "a nonlinear (and generally non-convex) limiting
operation". The same authors relax the entropy bound by an absolute
tolerance $10^{-4}$, citing among their reasons that strictly enforced
entropy bounds can degrade accuracy, with reference to convex-limiting work
(§4.3).

## Related flux limiters

Parametrized positivity- and maximum-principle-preserving flux limiters
(Xu; Hu, Adams & Shu) belong to the same idea — limiting a high-order flux
toward a first-order bound-preserving one — and are recalled as background
by [Wu & Shu (2023)](/sources/wu-2023-b.md) (§1), together with the
Guermond–Popov invariant-domain framework. In the finite-difference papers
of the corpus the Hu–Adams–Shu limiter is the source of positivity for
near-vacuum and Mach 2000 jet computations: TENO-AA
([Fu (2021)](/sources/fu-2021.md), §5.7) and TENO-THINC
([Takagi et al. (2022)](/sources/takagi-2022.md), §4.9); neither paper
describes the limiter. [Wong et al. (2021)](/sources/wong-2021.md) write a
limiter of this kind out, blending with a first-order HLLC flux under floors on
partial densities, volume fraction and a concave energy-like quantity
(§5.2); it is on the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
page. Its coefficients are computed from floors on $g(u)$, not from local
minimum and maximum bounds.

## Qualifications

- **Bounds that a low-order scheme cannot meet.** The bar-state bounds are
  specific to the Rusanov / graph-Laplacian dissipation. When HLLE or a
  second-order subcell reconstruction replaces it, the bounds are no longer
  guaranteed attainable; Rueda-Ramírez et al. keep them "in the absence of
  better bounds" and the blending returns the solution closest to them
  (§4 item (3), §5.2.3). Those variants are not provably IDP.
- **Entropy stability.** A provable entropy inequality for the blended
  semi-discretization exists for element-wise blending of entropy-stable DG
  with entropy-stable finite volumes; for subcell-wise blending the proof
  is "still missing" (Rueda-Ramírez et al. 2022, §4 item (2)); see
  [entropy stability](/properties/entropy-stability.md).
- **Order barrier of local bounds.** [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
  state that local discrete maximum principles impose a second-order
  accuracy barrier and that global-DMP limiters "may fail to prevent
  nonphysical solution behavior" (§1); they propose AFC on top of their
  [dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md)
  when strict bounds or entropy inequalities are required (§7.4).
  [Pazner (2021)](/sources/pazner-2021.md) measures first order: with strictly
  local bar-state bounds his scheme is first order on smooth data, which he
  calls "consistent with other results reported in the literature" (§5.1), and the design order returns only
  where the bounds are relaxed to global ones (Table 1). He recalls that
  TVD schemes are at most first order at smooth extrema (§4.4).
- **Printed slips of Pazner (arXiv v1)** that touch this page: the CFL
  bound (40) is printed $\Delta t\le\min_i m_i/(2\hat d_{ii})$ with
  $\hat d_{ii}=-\sum_{j\ne i}\hat d_{ij}\le0$, which is negative; the
  convex combination (39) needs $\Delta t\le m_i/(2\lvert\hat d_{ii}\rvert)$
  *(compiler check, not in the sources; this page writes the corrected form, with
  $\lvert\hat d_{ii}\rvert=\sum_{j\ne i}\hat d_{ij}$)*, and §5 repeats the printed form. Eq. (45) prints the
  viscosity term of the low-order update with the anti-diffusive sign,
  against the diffusive sign of Eq. (36). Eq. (60) prints the index range
  "$1\le d\le k$" for $1\le k\le d$. The equation numbers that
  Rueda-Ramírez et al. (2022) attach to Pazner's matrix and conservation
  condition do not match his arXiv v1 (above); this page cites the arXiv
  v1 numbering for Pazner.

# Citations

- [Pazner (2021)](/sources/pazner-2021.md) — arXiv v1: §1; §2.4.2 (Prop. 3); §3 (Eq. (23), Fig. 1); §3.1 (Eqs. (25)–(40), Props. 4–7); §3.3 (Eqs. (42)–(43)); §4 (Eqs. (44)–(62), Props. 8–11); §4.1.1 (Eq. (51)); §4.1.3–§4.1.4 (Fig. 3); §4.3 (Eqs. (65)–(67)); §4.4 (Eqs. (68)–(70)); §5.1 (Table 1).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.4 (Eqs. (23)–(29)); §3 (Props. 1–2, Eqs. (30)–(36)); §4 items (2)–(3); §5.2.1 (Eq. (43), Fig. 4); §5.2.2 (Eqs. (47)–(48)); §5.2.3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §1 (AFC, order barrier of local bounds); §7.4.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §1 (flux-correction limiters and invariant-domain methods recalled).
- [Wong et al. (2021)](/sources/wong-2021.md) — arXiv v1: §5.2 (flux limiter blending with first-order HLLC).
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: §5.7 (Hu–Adams–Shu limiter used).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9 (Hu–Adams–Shu limiter used).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — arXiv v3: §3.1 (Remark (Limiting)); §4.3 (entropy tolerance).
