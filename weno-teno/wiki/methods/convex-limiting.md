---
type: Method
title: "Convex limiting and invariant-domain-preserving schemes"
description: "Convex limiting blends a high-order update with a bound-preserving low-order update, adding as much antidiffusive flux as target bounds allow; the page gives the FCT form, graph viscosity and bar states, sparse low-order DG operators, Zalesak and convex limiters, element- versus subcell-wise blending, bound relaxation, subcell Rusanov finite volumes as sparse IDP DG, and semi-discrete monolithic convex limiting."
status: established
aliases: [flux-corrected transport, FCT, algebraic flux correction, AFC, invariant-domain-preserving limiting, IDP limiting, a posteriori blending, Zalesak limiter, sparse IDP DG, subcell convex limiting, monolithic convex limiting, MCL, residual blending]
tags: [limiting, bound-preserving, positivity, dg, entropy-stable]
timestamp: 2026-10-24T06:00:00Z
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
et al.; Pazner uses the FCT convention, in which Pazner's limiter value 1 means
full antidiffusion, so Pazner's coefficient is $1-\alpha$. Pazner's high-order
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

**Navier–Stokes and triangles** ([Lin, Chan & Tomas (2023)](/sources/lin-2023.md),
§3.2, §5). Lin et al. carry the construction to entropy-stable nodal DG on
quadrilaterals and triangles for the Euler and the explicit Navier–Stokes
equations. On quadrilaterals they use Pazner's piecewise-linear sparse
operator; on simplices they build a new sparse low-order SBP operator
from an adjacency graph of the nodes (two nodes adjacent when their
distance is below a multiple of a power of their quadrature weights,
Eq. 11), using that a diagonal-norm SBP operator is fixed by its skew
part: the skew entries are differences of a "potential" vector obtained
from one graph-Laplacian solve with a zero-mean constraint (Eqs. 9–10,
§3.2; [summation-by-parts operator](/operators/summation-by-parts-operator.md)).
The low-order scheme is central flux differencing of the *total*
(inviscid minus viscous) flux on that operator plus a graph viscosity
whose coefficient is Zhang's Navier–Stokes positivity coefficient
(Eqs. 16–18; [positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md));
its forward-Euler step is a convex combination of bar states that include
the viscous fluxes, hence positivity-preserving under
$\Delta t\le m_i/(2\lambda_i)$, with $\lambda_i$ the summed
coefficients of node $i$ (page-local; Lemma 5.1, Theorem 5.2). With the
coefficient enlarged to include a maximum-wave-speed bound it is also
semi-discretely entropy stable, being a subcell finite-volume scheme with
Lax–Friedrichs-type fluxes (Theorem 6.1, Eq. 45). Sparsifying keeps the
low-order Leblanc solution nearly the same for $N=2$ and $N=5$ at 600
degrees of freedom (Table 1a, Fig. 3).

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
   $s_{\mathrm P}=\ln\big(e^{1/(\gamma-1)}\rho^{-1}\big)$ (page-local; the registry's $s$ times
   $1/(\gamma-1)$ up to an additive constant) from below by its minimum over
   the neighbouring states at $t^n$, not over bar states (Eq. (67)), in the
   convex invariant set $\{\rho>0,\ e>0,\ s_{\mathrm P}\ge s_{\min}\}$ (Eq. (65)); the
   entropy bound also keeps the internal energy positive. Rueda-Ramírez et
   al. bound the modified specific entropy $e\rho^{1-\gamma}$ (Eq. (48)),
   which they prefer to $\ln(p\rho^{-\gamma})$ as cheaper and better suited
   to Newton's method; the two are monotone functions of each other,
   $s_{\mathrm P}=\frac{1}{\gamma-1}\ln(e\rho^{1-\gamma})$, so the bounded sets coincide
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
  minimum in Pazner's FCT convention; Rueda-Ramírez et al. 2022,
  $\alpha_{(i,m)j}=\max(\tilde\alpha_{ij},\tilde\alpha_{mj})$), and the
  update is conservative (Prop. 10). Pazner presents this
  dimension-by-dimension procedure as the author's improvement over the
  multidimensional subcell limiter of Lohmann et al., which required a
  minimization problem (§4.1.3).

- **Element-wise for positivity only, in closed form** (Lin et al.,
  §6.1, Eqs. 37–43). Lin et al. limit the update, not the fluxes:
  $m_iu^{n+1}_i=m_iu^{\mathrm L,n+1}_i+\Delta t\,\mathsf l_K\,(r^{\mathrm L}_i-r^{\mathrm H}_i)$,
  with $u^{\mathrm L,n+1}_i$ the low-order update, $r^{\mathrm L}_i$, $r^{\mathrm H}_i$
  their low- and high-order residuals, defined with the sign opposite to
  Pazner's above ($m_i(u^{\mathrm L,n+1}_i-u^n_i)/\Delta t+r^{\mathrm L}_i=0$),
  and one $\mathsf l_K\in[0,1]$ per element $K$ (page-local; $\mathsf l_K=1-\alpha$
  in this page's convention), the
  largest that keeps every node above relaxed bounds proportional to the
  low-order density and internal energy. The density constraint is
  linear in $\mathsf l_K$ and the internal-energy constraint quadratic, so $\mathsf l_K$ is
  the minimum of a ratio and of the smallest non-negative root of a
  quadratic ([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)).

Subcell-wise coefficients are stricter per interface, because each must
guarantee the bound independently of the others, yet they limit less in
practice: on an under-resolved Kelvin–Helmholtz instability they add about
three orders of magnitude less low-order method than element-wise blending
(Rueda-Ramírez et al. 2022, §5.2.1, Fig. 4), and at fixed degrees of
freedom element-wise limiting stops improving beyond $N=1$ while subcell
limiting improves with $N$ (Pazner, §4.1.4, Fig. 3); see
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md).

- **Convex-constraint factors as caps of an entropy program**
  ([Lin & Chan (2024)](/sources/lin-2024.md), §3, Thms 3.1–3.3). The
  factors that a convex limiter allows at each subcell interface
  (relaxed positivity, $\rho\ge\tfrac12\rho^{\mathrm L}$ and
  $\rho e\ge\tfrac12\rho e^{\mathrm L}$ of the low-order update, or
  TVD-like density bounds over the low-order neighbours, Eqs. (62), (67))
  become upper bounds $l^{\mathrm C}$ on the high-order weights $l=1-\alpha$
  of a linear program that maximizes $\sum l$ under the semi-discrete cell
  entropy inequality of the element. Because the constraint is a single
  linear inequality, the program is a continuous knapsack problem solved
  exactly by a greedy sort; the result keeps the convex constraints,
  conservation and the cell entropy inequality (page-local $l$,
  $l^{\mathrm C}$; the construction is on
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
  The constraints are imposed per substate of the update, half of it
  carrying each of the two interface fluxes of a node (Eq. (63)), the
  same device as the per-direction provisional states above *(compiler
  check, not in the sources)*.

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
construction is not needed (Prop. 2, Eqs. (35)–(36)). Pazner
describes the nodes as subcell-centred values but does not state the
equivalence (§4.1.3). The equivalence is why the bar-state bounds can
always be met for that low-order scheme: on the Mach 4 bow shock they hold
to machine precision (§5.2.2).
[Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) (§2.2.1,
Eqs. 9–13, arXiv v1) restate the scheme in bar-state form,
$u^{\mathrm{FV},n+1}_i=\big(1-\tfrac{\Delta t}{J\mathsf w_i}(a_{(i,i-1)}+a_{(i,i+1)})\big)u^n_i+\tfrac{\Delta t}{J\mathsf w_i}\big(a_{(i,i-1)}\breve u_{(i,i-1)}+a_{(i,i+1)}\breve u_{(i,i+1)}\big)$,
with $a_{(i,j)}$ an upper bound of the maximum wave speed of the Riemann
problem between nodes $i$ and $j$, and note that the Rusanov bar state
is the HLL intermediate state, which is why it lies in every convex
invariant set ([HLL-family solvers](/methods/hll-riemann-solvers.md)).

## Monolithic convex limiting

[Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) (§2.2, arXiv
v1) transfer Kuzmin's monolithic convex limiting (MCL), designed for
continuous finite elements and extended by Hajduk to Bernstein-basis DG,
to the LGL [DGSEM](/methods/dgsem.md). The LGL-DGSEM is first written in
subcell [flux-differencing](/methods/flux-differencing.md) form with
explicit symmetric subcell fluxes $\hat f^{\mathrm{DG}}_{(i,i+1)}$ between
neighbouring nodes (Eqs. 5–8), and the compatible low-order scheme is the
Rusanov subcell scheme above. For the LGL nodes this needs no
sparsification of the derivative operator, no graph Laplacian and no
linear solve; for Bernstein DG with $N>1$ the same form requires solving
$n_{\mathrm{eq}}$ linear systems of size $N+1$ per element and
Runge–Kutta stage (Remark 2). The limited semi-discretization is
$$J\mathsf w_i\,\dot u_i=\hat f_{(i-1,i)}-\hat f_{(i,i+1)},\qquad
\hat f_{(i,j)}=\hat f^{\mathrm{FV}}_{(i,j)}+(1-\alpha_{(i,j)})\big(\hat f^{\mathrm{DG}}_{(i,j)}-\hat f^{\mathrm{FV}}_{(i,j)}\big)$$
(Eqs. 14–15, in this page's convention for $\alpha$; the source's factor,
1 for the high-order flux, is $1-\alpha$). With the antisymmetric
antidiffusive flux $\Delta\hat f_{(i,j)}=(i-j)\big(\hat f^{\mathrm{DG}}_{(i,j)}-\hat f^{\mathrm{FV}}_{(i,j)}\big)$
the high-order update takes the bar-state form with **high-order bar
states** $\breve u_{(i,j)}+\Delta\hat f_{(i,j)}/a_{(i,j)}$ (Eq. 19). MCL
limits $\Delta\hat f$ so that the **limited bar states**
$\breve u_{(i,j)}+\Delta\hat f^{\mathrm{Lim}}_{(i,j)}/a_{(i,j)}$ satisfy
the bounds (Eq. 21). The constraints are imposed on the
semi-discretization, before any time step: the limited flux depends on
the state only, and the nonlinear spatial operator is independent of
$\Delta t$, unlike the FCT/IDP form above, whose antidiffusive correction
and bounds depend on the step (§2.2.2, §2.2.4).

All correction factors are in closed form (Remark 9):

- **Conserved scalar** (Eqs. 22–24). With bounding fluxes
  $\Delta\hat f^{\rho,+}_{(i,j)}=a_{(i,j)}\min\{\rho^{\max}_i-\breve\rho_{(i,j)},\ \breve\rho_{(i,j)}-\rho^{\min}_j\}$
  and
  $\Delta\hat f^{\rho,-}_{(i,j)}=a_{(i,j)}\max\{\rho^{\min}_i-\breve\rho_{(i,j)},\ \breve\rho_{(i,j)}-\rho^{\max}_j\}$,
  the limited flux is $\min\{\Delta\hat f^\rho,\Delta\hat f^{\rho,+}\}$ if
  $\Delta\hat f^\rho\ge0$ and $\max\{\Delta\hat f^\rho,\Delta\hat f^{\rho,-}\}$
  otherwise, which guarantees the two-sided bounds on both bar states of
  the interface and is a convex blend of the FV and DG fluxes. Computing
  $\alpha$ explicitly is "unnecessary and numerically ill posed" for small
  denominators.
- **Ratios** (sequential limiting, Eqs. 25–30). For
  $\phi=(\rho\phi)/\rho$ (velocity components, specific total energy) the
  density flux is limited first, then an auxiliary flux built from the
  discrete product rule keeps the limited $\phi$ bar states in their
  bounds; with LGL nodes the low-order bar state of $\phi$ is symmetric,
  $\breve\phi_{(i,j)}=\breve{(\rho\phi)}_{(i,j)}/\breve\rho_{(i,j)}$, which the authors list as an
  advantage over Bernstein-basis DG. The factor this induces on the
  conserved flux of $\rho\phi$ "does not necessarily lie in the range
  [0,1]" (Remark 8).
- **Pressure positivity** (Eqs. 31–36). One factor for all components of
  an interface turns positivity of $\rho(\rho E)-\tfrac12\lvert\rho v\rvert^2$
  at the limited bar states into a quadratic inequality in the factor;
  with $\alpha^2\le\alpha$ on $[0,1]$ a linear sufficient condition gives
  it in closed form ([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)
  for the same algebra). A "sharp" variant uses the exact linear
  coefficient, a "cautious" one an upper bound of it, chosen for
  continuous dependence on the data; on the high-Mach jet the cautious
  variant suppresses the vortical structures of the shear layer that the
  sharp one lets develop (Fig. 9).
- **Entropy** (Eqs. 37–39, after Kuzmin, Hajduk and Rupp). One factor
  per interface enforces Tadmor's shuffle condition
  $[\![w]\!]\cdot\hat f_{(i,j)}\le[\![\psi]\!]$ on the limited flux
  ([entropy stability](/properties/entropy-stability.md)).

**Bounds** (§2.2.3). Global bounds are physical admissibility
($\rho\ge0$, $p\ge0$); local bounds are the extrema of the low-order bar
states around a node, $\phi^{\min}_i=\min_{j\in\{i-1,i,i+1\}}\breve\phi_{(i,j)}$
with $\breve\phi_{(i,i)}=\phi_i$ (Eq. 41), which makes the constraints
always feasible. Bounds taken from the next-step low-order solution, the
FCT/IDP choice, are more dissipative but can relax the time step. The
paper uses the tight bounds (41) for both MCL and FCT/IDP, without
relaxation.

**Time step** (§2.2.4, Eqs. 43–45). Bar-state constraints, in MCL and in
FCT/IDP, require
$\Delta t\lesssim\min_i m_i/\big(2\sum_da^{(d)}_i\big)$ ($m_i$ the
diagonal mass entry, $a^{(d)}_i$ the largest wave speed at node $i$ in
direction $d$; page-local), more restrictive than the low-order
condition $\Delta t\lesssim\min_i\min_d\Delta x^{(d)}_i/a^{(d)}_i$,
"especially for multiple space dimensions". To the authors' knowledge
the only way to circumvent it while keeping the bounds is FCT/IDP without
bar-state bounds.

**Evidence** (§3, Euler in Trixi.jl, LGL-DGSEM with Ranocha's
entropy-conservative and kinetic-energy-preserving volume flux unless
stated; [Trixi.jl](/software/trixi-jl.md)).

- **Accuracy.** On a 2D [density wave](/benchmarks/density-wave-advection.md)
  with only the positivity bounds, the mean experimental orders over
  $N_e=4\to32$ elements per direction are 4.16 ($N=3$) and 4.75 ($N=4$);
  with the tight local bounds they are 1.82 and 1.61, "at most second
  order, independent of the polynomial degree" (Tables 1–4).
- **Robustness.** On the [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
  ($N=7$, $64^2$ elements, $t=10$) MCL with strict positivity and FCT/IDP
  with the relative bounds $\rho\ge0.1\rho^{\mathrm{FV}}$,
  $p\ge0.1p^{\mathrm{FV}}$ both reach the final time with "remarkably
  similar looking results"; FCT/IDP needs the positive fraction, "as
  otherwise some nodes might get an invalid vacuum state" (Fig. 1). Local
  bounds add dissipation in both (Fig. 2).
- **Limiter variants.** On the [Sedov blast wave](/benchmarks/sedov-blast-wave.md)
  ($N=3$, $64^2$, Chandrashekar volume flux) the sequential limiter with
  local bounds followed by the pressure and entropy limiters leaves
  "artifacts at the shock front"; limiting the density first and applying
  its effective factor to all conserved fluxes removes these
  "Carbuncle-like artefacts" ([carbuncle phenomenon](/definitions/carbuncle-phenomenon.md));
  adding the sequential limiter after it is "clearly more dissipative"
  (§3.4, Figs. 5–7).
- **Dependence on the time step.** On a [high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md)
  (jet Mach number 2156.91, $N=3$, $256^2$, $t=10^{-3}$) the number of MCL
  steps is 10284, 20568, 41138 and 102844 at CFL 0.9, 0.45, 0.225 and
  0.09, a constant CFL × steps of about 9256, while FCT/IDP takes 10758,
  25608, 71577 and 241974 steps (CFL × steps from 9682 to 21778)
  *(compiler check, not in the sources: the products)*. The FCT/IDP solution changes markedly with CFL:
  a smaller step limits less, lowers $\rho_{\min}$ from $4.43\times10^{-3}$
  to $7.11\times10^{-4}$ and raises $p_{\max}$ from 172640 to 228165,
  which raises the sound speed and shortens the step further, a "feedback
  effect" (Table 5, Fig. 8). The authors conclude that "time convergence
  can be expected for MCL but not for FCT schemes in problems that need
  stabilization" (§4).

## Blending residuals of a non-conservative update

[Abgrall et al. (2026)](/sources/abgrall-2026.md) (§3) apply the construction to
the [PAMPA scheme](/methods/pampa-scheme.md), whose interface point values are
evolved by residuals that need not be conservative. The cell averages follow the
pattern above: the flux is the local Lax–Friedrichs flux plus a fraction
$\mathsf e_{i+1/2}=1-\alpha$ (page-local, the weight of the high-order part) of the
antidiffusive flux $f(u_{i+1/2})-\hat f^{\mathrm{LO}}_{i+1/2}$, and under
$\Delta t\le\Delta x/(a_{i-1/2}+a_{i+1/2})$ the update is a convex combination of
the old average and two intermediate states, each a Lax–Friedrichs bar state
shifted by $\pm\mathsf e\,\Delta\hat f/a$ (Eqs. (3.1)–(3.4)). The point values are
limited the same way but per residual: each of the two residuals a node receives
has its own coefficient, which is allowed because the point update carries no
conservation constraint, and the update is again a convex combination of
node bar states shifted by the limited residual differences (Eqs. (3.7)–(3.12)).
The coefficients come in closed form, as the largest values that keep every
intermediate state inside global bounds (Props. 3.1–3.2, Eqs. (3.5), (3.13)–(3.14))
or inside local bounds built from the old average and its two bar states
(Eq. (3.18), the formula of Kuzmin and Vilar, as the authors state). The local
bounds are relaxed in cells that a derivative-based smooth-extrema detector marks
as smooth, and the tests run the bounds either strict or widened by
$\max\big(10^{-4},10^{-3}(u_{\max}-u_{\min})\big)$. With strict global bounds the
linear-advection rates fall to about $2.2$–$2.6$ ($L^2$, $L^1$) and $1.8$
($L^\infty$), with the relaxed ones they are $3.00$ (Tables 1–2); the authors
attribute the loss to the strict global bounds, the local ones being switched off
by the detector (Ex. 1, Remark 4.1), so it is not the local-bound order barrier of
Pazner and Rueda-Ramírez et al. (2024) recorded under Qualifications.
For the Euler equations the nonlinear internal-energy constraint is made linear by
[geometric quasilinearization](/methods/geometric-quasilinearization.md), so the
coefficient is again a closed-form ratio, minimized over the auxiliary velocity by
an eigenvalue formula (§3.4, Appendix A), instead of the Newton-type line searches
used for nonlinear bounds above.

**Active Flux averages.** [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md)
(arXiv v3, §4.1) limit the averages of the generalized
[Active Flux](/methods/active-flux.md) method, whose high-order flux is Simpson's rule
over the interface point values, in the same bar-state form. The low-order scheme is
first-order local Lax–Friedrichs on the averages, with $a_{i+1/2}$ the larger spectral
radius of the two adjacent averages, rewritten as a convex combination of $\bar u_i$ and
the bar states $\breve u_{i\pm1/2}$ under
$\Delta t\le\tfrac12\min\{\Delta x/(a^{(1)}_{i-1/2}+a^{(1)}_{i+1/2}),\ \Delta y/(a^{(2)}_{j-1/2}+a^{(2)}_{j+1/2})\}$
(Lemma 4.1, Eq. (30); bar-state admissibility for scalar laws and Euler in Lemmas
B.1–B.2). The limited states are $\breve u_{i\pm1/2}\mp\mathsf e_{i\pm1/2}\Delta\hat f_{i\pm1/2}/a_{i\pm1/2}$,
$\mathsf e\in[0,1]$ the weight of the antidiffusive flux (page-local as above; the
source's $\theta$), and Proposition 4.1 makes the limited forward-Euler update bound
preserving, then SSP-RK3 by convexity (§4.1). The coefficients are those of the
monolithic limiter above:

- **Scalar laws** (§4.1.1, Eq. (34)): the same closed-form bounding fluxes
  $a\min\{\breve u-u^{\min}_i,\ u^{\max}_{i+1}-\breve u\}$ and
  $a\max\{u^{\min}_{i+1}-\breve u,\ \breve u-u^{\max}_i\}$, with global bounds over all
  averages and point values or local bounds over the cell, its bar states and its
  neighbours' averages.
- **Euler** (§4.1.2, Eqs. (35)–(37)): density first, by the same min/max rule against a
  floor $\min\{10^{-13},\dots\}$; then pressure, whose constraint at the limited bar
  states is quadratic in $\mathsf e$, replaced, after Kuzmin as the authors state, by the
  linear sufficient condition from $\mathsf e^2\le\mathsf e$, which gives
  $\mathsf e=\min\{1,C/(\max\{0,A\}+\lvert B\rvert)\}$ ($A$, $B$, $C$ the coefficients of
  the quadratic, page-local).

Two points are specific to Active Flux. Limiting the averages is not enough, because the
point values are degrees of freedom too: they are limited
separately by a [Zhang–Shu-type](/methods/zhang-shu-scaling-limiter.md) blend with a
first-order point update, and on a 2D advection test the bounds hold only with both
limiters (Example 5.4, Table 1). And the time-step condition is evaluated at $t^n$ only;
when a later Runge–Kutta stage violates it the implementation halves $\Delta t$ and
restarts the step (Remark 4.2). A further factor $\theta^{\mathrm s}\in(0,1]$ (page-local) from a
shock sensor scales the limited antidiffusive flux once more, which keeps the bounds
([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

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
minimum and maximum bounds. Limiting that recomputes flagged cells after
the step instead of blending fluxes before it is
[MOOD a posteriori limiting](/methods/mood-a-posteriori-limiting.md).

## Viscosity without invariant-domain guarantees

[Dao & Nazarov (2022)](/sources/dao-2022.md) stabilize continuous finite
elements for ideal MHD with a residual-based
[artificial viscosity](/methods/artificial-viscosity.md) capped by a
first-order viscosity $C_{\max}h_ia_i$ ($h_i$ a nodal mesh size, $a_i$
the largest eigenvalue modulus at node $i$; page-local $C_{\max}$,
$h_i$), which in 1D gives the Lax–Friedrichs scheme, but claim no
invariant-domain property. They cite the convex limiting of Guermond,
Nazarov, Popov and Tomas as the route to invariant-domain preservation
and to a correction of strongly imposed boundary conditions, and state,
citing Guermond and Popov's first-order invariant-domain scheme, that a
positivity-preserving first-order viscosity would need a more accurate
maximum-wave-speed estimate than the largest eigenvalue they use
(§1, §4.2, §4.5, §6). The graph viscosity above instead takes its wave
speed $a_{\max}$ from the maximum wave speed of the Riemann problem between neighbouring
nodes (Pazner, §3.1).

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
  [entropy stability](/properties/entropy-stability.md). Lin et al. agree:
  one blending parameter per element blends two entropy-stable
  semi-discretizations and keeps the semi-discrete cell entropy
  inequality (Theorem 6.2), whereas subcell convex limiting with
  positivity as the only constraint cannot be shown to keep it (App. B.1);
  earlier convex limiting enforced local density bounds and a minimum
  principle on the specific entropy, which Lin et al. drop because that
  principle holds for Euler but not for Navier–Stokes (§1). When the
  high- and low-order schemes share the same Lax–Friedrichs interface flux
  and interface matrices, subcell limiting localizes to element interiors
  and needs no exchange of limiting parameters between neighbours
  (App. B.2, Eqs. 80–81). Lin & Chan (2024) add the entropy inequality as
  an extra constraint on the subcell coefficients and prove that subcell
  blending then keeps the semi-discrete cell entropy inequality (Thms 3.1,
  3.3); the high-order accuracy of the result is shown only numerically
  (§4.2).
- **Wave-speed estimates.** The Davis estimate used by Lin et al. is not
  a guaranteed upper bound of the maximum wave speed; a case where the
  Rusanov estimate underestimates it would compromise the provable
  positivity and entropy stability of the low-order scheme, though none
  was observed (footnote 3). They also note a staircasing-like effect of
  the sparse low-order scheme near element boundaries, seen in other
  bar-state discretizations and speculatively attributed to diagonal mass
  entries that decrease towards the boundary (footnote 4).
- **Order barrier of local bounds.** [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md)
  state that local discrete maximum principles impose a second-order
  accuracy barrier and that global-DMP limiters "may fail to prevent
  nonphysical solution behavior" (§1); they propose AFC on top of their
  [dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md)
  when strict bounds or entropy inequalities are required (§7.4).
  [Pazner (2021)](/sources/pazner-2021.md) measures first order: with strictly
  local bar-state bounds Pazner's scheme is first order on smooth data, which the author
  calls "consistent with other results reported in the literature" (§5.1), and the design order returns only
  where the bounds are relaxed to global ones (Table 1). Pazner recalls that
  TVD schemes are at most first order at smooth extrema (§4.4).
  Rueda-Ramírez et al. (2024) measure the second-order version of the
  barrier with MCL on tight bar-state bounds (mean orders 1.82 and 1.61
  for $N=3$, 4) and the design order with global bounds (4.16, 4.75), and
  name smoothness indicators as a way to relax the bounds (§2.2.3, §3.1).
  First order (Pazner, strict bar-state bounds on advection) and second
  order (Rueda-Ramírez et al., local bounds on the Euler density wave) are
  measured on different tests and limiters, and both lie at or under
  Kuzmin & Vedral's barrier.
- **Time-step independence, one test.** The claim that MCL converges in
  time and FCT/IDP does not (Rueda-Ramírez et al. 2024, §2.2.4, §4) rests
  on the jet test; the authors add that the dependence of FCT/IDP on the
  step "may be an advantage or a disadvantage" depending on the
  application.
- **Printed slips of Rueda-Ramírez et al. (2024, arXiv v1).** In the
  pressure constraint (Eq. 33) the constant term is printed
  $Q=\breve w^\rho\breve w^{\rho E}+\tfrac12\lvert\breve w^{\rho v}\rvert^2$
  ($\breve w=a\breve u$); expanding the positivity condition (31) at
  the limited bar states gives the printed quadratic and linear
  coefficients and $Q=\breve w^\rho\breve w^{\rho E}-\tfrac12\lvert\breve w^{\rho v}\rvert^2$,
  $a^2$ times $\rho\cdot\rho e$ of the low-order bar state *(compiler
  check, not in the sources)*. In the entropy factor (Eq. 39) the
  numerator is printed $[\![w]\!]\cdot\hat f^{\mathrm{FV}}-[\![\psi]\!]$;
  substituting the limited flux into the shuffle condition bounds the
  factor by $\big([\![\psi]\!]-[\![w]\!]\cdot\hat f^{\mathrm{FV}}\big)/\big([\![w]\!]\cdot\Delta\hat f^{\mathrm{Lim}}/(i-j)\big)$,
  the opposite sign *(compiler check, not in the sources)*. The bow-shock
  state $\rho=1.4$, $p=1$, $v_1=4$ is printed as "Mach number Ma = 1.4";
  with $\gamma=1.4$ its sound speed is 1 and its Mach number 4 (§3.3)
  *(compiler check, not in the sources)*. §3.5 says the number of steps
  "depends linearly" on the CFL number for MCL; Table 5 shows it
  inversely proportional.
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
  condition do not match Pazner's arXiv v1 (above); this page cites the arXiv
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
- [Dao & Nazarov (2022)](/sources/dao-2022.md) — arXiv v1: §1; §4.2; §4.5; §6 (invariant-domain preservation left out of scope).
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — arXiv v1: §2.1–2.2 (Eqs. (5)–(45), Remarks 2, 6–9); §3.1–3.5 (Tables 1–5, Figs. 1–9); §4.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — arXiv v2: §1; §3.2, Eqs. (9)–(11); §5, Eqs. (16)–(24), Lemma 5.1, Theorem 5.2; §6.1–6.2, Eqs. (37)–(45), Theorems 6.1–6.2; Table 1, Fig. 3; App. B, Eqs. (70)–(81); footnotes 3–4.
- [Lin & Chan (2024)](/sources/lin-2024.md) — §3.1–3.2, Eqs. (25), (46), Thms 3.1–3.3; §4.3–4.4, Eqs. (62)–(68).
- [Abgrall et al. (2026)](/sources/abgrall-2026.md) — §3.1–3.4, Eqs. (3.1)–(3.18), Props. 3.1–3.2; Appendix A; §4, Tables 1–2.
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — arXiv v3: §4.1, Eqs. (27)–(38), Lemma 4.1, Prop. 4.1, Remarks 4.1–4.2; App. B, Lemmas B.1–B.2; Example 5.4, Table 1.
