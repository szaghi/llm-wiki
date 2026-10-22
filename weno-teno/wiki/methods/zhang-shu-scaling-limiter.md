---
type: Method
title: "Zhang–Shu scaling limiter"
description: "The Zhang–Shu limiter scales a high-order polynomial linearly toward its cell average until the point values used by a cell-average decomposition lie in the admissible set; it conserves the cell average and, with a BP first-order flux and a CFL bound, makes the cell-average update bound-preserving."
status: established
aliases: [scaling limiter, bound-preserving limiter, positivity-preserving limiter, maximum-principle-satisfying limiter, BP limiter, simplified BP limiter, PP limiter]
tags: [bound-preserving, positivity, limiting, dg, finite-volume]
timestamp: 2026-10-23T10:00:00Z
---

# Zhang–Shu scaling limiter

The Zhang–Shu limiter is the third ingredient of the cell-average route to
[bound preservation](/properties/bound-preservation.md). Given the
degree-$N$ polynomial $u_h$ of cell $I_i$ (DG solution or finite-volume
reconstruction) with cell average $\bar u_i\in G$, it replaces $u_h$ by
$$\tilde u_h=\theta\,(u_h-\bar u_i)+\bar u_i,\qquad 0\le\theta\le1,$$
with $\theta$ the largest factor for which the point values on a prescribed
point set lie in $G$. The cell average is unchanged, so conservation is
kept, and because $G$ is convex and $\bar u_i\in G$, a $\theta$ that works
always exists (at worst $\theta=0$). Combined with a BP first-order flux and
the CFL condition of a
[cell-average decomposition](/methods/optimal-cell-average-decomposition.md),
the next cell average stays in $G$
([Cui, Ding & Wu (2024)](/sources/cui-2024.md), §1, Eqs. (1.7)–(1.8);
Rem. 7.3; [Wu & Shu (2023)](/sources/wu-2023-b.md), App. B;
[Fan, Zhang & Qiu (2021)](/sources/fan-2021.md), §3.1;
[Renac (2021)](/sources/renac-2021.md), §6.3;
[Liu et al. (2021)](/sources/liu-2021.md), §3.3.4;
[Chen & Wu (2022)](/sources/chen-2022-b.md), §3.3;
[Du & Yang (2022)](/sources/du-2022-b.md), §4.3).

## Scalar bounds

For a scalar law with $G=[U_{\min},U_{\max}]$,
[Cui et al. (2024)](/sources/cui-2024.md) recall (Rem. 7.3, Eq. (7.15))
$$\theta=\min\Big\{\Big\lvert\frac{U_{\max}-\bar u_i}{p^{\max}-\bar u_i}\Big\rvert,\ \Big\lvert\frac{U_{\min}-\bar u_i}{p^{\min}-\bar u_i}\Big\rvert,\ 1\Big\},$$
where $p^{\max}$, $p^{\min}$ are the maximum and minimum of $u_h$ over the
point set $\Theta_i$ = edge Gauss points $\cup$ internal nodes of the
decomposition (page-local $\Theta_i$). The source prints $\delta$ for the
factor; it is the registry's $\theta$. For non-negativity alone
($U_{\min}=0$, no upper bound), [Zheng et al. (2022)](/sources/zheng-2022.md)
use $\theta=\lvert\bar u_i/(\bar u_i-m_i)\rvert$ with $m_i$ the minimum of
the reconstruction over the whole cell (§2.3.3, Eqs. (22)–(24)); see
*Point sets* below.

## Systems: successive scalings

For gas dynamics the constraints are enforced one after another, each
scaling acting on the result of the previous one, with the density first:

- **Euler and Navier–Stokes, positivity of $\rho$ and $\rho e$**
  ([Cui et al. (2024)](/sources/cui-2024.md), Rem. 8.1;
  [Fan et al. (2021)](/sources/fan-2021.md), Eqs. (3.14)–(3.15),
  (3.31)–(3.32)). Density: $\hat\rho=\theta_1(\rho_h-\bar\rho_i)+\bar\rho_i$,
  $\theta_1=\min\{\lvert(\bar\rho_i-\varepsilon_1)/(\bar\rho_i-\rho_{\min,i})\rvert,1\}$,
  with $\varepsilon_1=\min\{10^{-13},\bar\rho_i\}$ (Cui et al.) or
  $\varepsilon_1=10^{-13}$ (Fan et al.); then a second factor $\theta_2$
  built in the same way from $\rho e$ scales the whole state vector. Fan
  et al. compute $\theta_2$ as the minimum over the test states of
  $(\rho e(\bar u_i)-\varepsilon)/(\rho e(\bar u_i)-\rho e(u_q))$, taken
  only where $\rho e(u_q)<\varepsilon$, and justify $\theta_2\in[0,1]$ by
  the concavity of $\rho e$ (Jensen). Here $\varepsilon_1$, $\varepsilon_2$
  are round-off floors (page-local), not WENO regularizations.
- **Multicomponent Euler** ([Renac (2021)](/sources/renac-2021.md), §6.3,
  Eq. (67)). Three scalings on the nodal values of the DGSEM: density as
  above; each partial density toward
  $\breve\rho\,\overline{\rho Y_k}_i/\bar\rho_i$ (the scaled density
  times the cell's mean mass fraction, which keeps the cell average of
  $\rho Y_k$); then the vector $(\rho,\rho v,\rho E)$ with the largest
  factor that keeps $e\ge\varepsilon$ at every node, $\varepsilon=10^{-10}$
  (overbars the cell averages, $\breve\rho$ the limited density,
  page-local). The mass fractions are allowed to go slightly negative, down
  to a bound fixed by the gas constants of the components, which still
  keeps the partial densities and the mixture gas constant positive.
- **Reacting multicomponent Navier–Stokes** ([Du & Yang (2022)](/sources/du-2022-b.md),
  §4.3, from the authors' earlier work). Four steps on the point set of
  Gauss–Lobatto and Gauss points of Thm 4.3: if $\bar\rho\le10^{-13}$ the
  cell is set to its mean; otherwise density and all partial densities
  $\rho Y_k$ are scaled together with
  $\theta_1=(\bar\rho-10^{-13})/(\bar\rho-\rho_{\min})$ where $\rho_{\min}<0$;
  then the partial densities are pulled toward
  $\hat\rho\,\overline{\rho Y_k}/\bar\rho$ (the limited density times the
  cell's mean mass fraction), by **one** factor for all species, the
  smallest pull toward that state that makes every $\rho Y_k$
  non-negative at the points where one is negative; finally the whole vector
  is scaled toward the mean by the smallest pointwise ratio
  $P(\bar u)/(P(\bar u)-P(\tilde u(x)))$ over the points where $P<0$, with
  $P=E-\sum_k\rho Y_kh_k(0)-\tfrac12\rho\lvert v\rvert^2$ the concave
  pressure surrogate of the
  [bound-preservation](/properties/bound-preservation.md) page ($h_k(0)$
  formation enthalpies, page-local). A common factor in the second step
  keeps $\sum_k\rho Y_k=\rho$ when it holds before *(compiler check, not in
  the sources: sum the convex combination over $k$)*; no upper bound on
  $Y_k$ is enforced, because the scheme conserves $\sum_kY_k=1$ exactly and
  non-negative partial densities then give $Y_k\le1$. The second step is
  the construction of Renac above, toward the same target state.
- **Special relativistic hydrodynamics on triangles**
  ([Chen & Wu (2022)](/sources/chen-2022-b.md), §3.3, Eqs. (40)–(43),
  Prop. 3.1). Two steps: the lab-frame density $D$ with
  $\theta_1=\min\{(\bar D-\varepsilon_1)/(\bar D-D_{\min}),1\}$, then the
  whole vector with
  $\theta_2=\min\{(g(\bar u)-\varepsilon_2)/(g(\bar u)-g_{\min}),1\}$ for the
  concave $g(u)=E-\sqrt{D^2+\lvert m\rvert^2}$ that defines the admissible
  set of [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md),
  $\varepsilon_{1,2}=\min\{10^{-13},\cdot\}$ of the mean. The minima are taken over
  the edge Gauss points and over one "interior remainder" state, the
  triangle form of $\Pi_{ij}$ below, so no interior quadrature point is
  evaluated (Rem. 3.5, after a simplified limiter of earlier work).
  Concavity of $g$ replaces the quadratic equation of Qin, Shu & Yang's
  RHD limiter. Without the floors the limiter commutes with scaling: the
  limited version of $\sigma u_h$ is $\sigma$ times the limited $u_h$ for
  $\sigma>0$ (Eq. (45)), which the homogeneity of the RHD scheme needs. The printed $\theta_2$ carries an
  absolute value inside the minimum (Eq. (42)).
- **Multicomponent MHD** ([Wu & Shu (2023)](/sources/wu-2023-b.md), App. B):
  three successive scalings — density, mass fractions (from negative
  partial densities), and the concave function
  $g(u)=E-\tfrac12\big(\lvert\rho v\rvert^2/\rho+\lvert B\rvert^2\big)$,
  used in place of the pressure, which is not concave in $u$ when $\gamma$
  depends on the mass fractions (Eq. (6.3)).
- **Ideal MHD with a reconstructed pressure** ([Liu et al. (2021)](/sources/liu-2021.md),
  §3.3.4, Eqs. (36)–(38)): $\theta=\min\{1,(\bar u_i-\epsilon)/(\bar u_i-\min u_h)\}$,
  $\epsilon=\min\{10^{-13},\bar u_i\}$, applied to "the reconstructed
  polynomials of density and thermal pressure"; how the pressure polynomial
  is obtained from the reconstructed conservative variables is not stated.

Concavity is what lets a factor computed from point values alone work:
for concave $g$ and $\theta\in[0,1]$,
$g\big(\theta(u-\bar u_i)+\bar u_i\big)\ge(1-\theta)\,g(\bar u_i)+\theta\,g(u)$,
so the factor $\theta=\big(g(\bar u_i)-\varepsilon\big)/\big(g(\bar u_i)-\min g\big)$,
the form Wu & Shu print for their third scaling (App. B) and Fan et al. for
$\rho e$, keeps $g\ge\varepsilon$ at every point of the set *(compiler
check, not in the sources: the inequality is the definition of
concavity)*. The
[geometric quasilinearization](/methods/geometric-quasilinearization.md)
representation is the sources' tool for constraints that are not concave.

## Point sets and the simplified limiter

The point set is that of the decomposition: Gauss–Lobatto points in 1D and
the tensor Gauss / Gauss–Lobatto points of the classic 2D decomposition
([Wu & Shu (2023)](/sources/wu-2023-b.md), Thm 6.2, condition (6.12);
[Liu et al. (2021)](/sources/liu-2021.md), Eq. (36), with $Q$ Gauss and
$L$ Gauss–Lobatto points, $Q=1$, $L=2$ for linear and $Q=2$, $L=3$ for
quadratic reconstruction), the DGSEM nodes themselves
([Renac (2021)](/sources/renac-2021.md), whose positivity theorem assumes
all nodal values admissible, Thm 6.1), or the edge Gauss points plus the
internal nodes of an optimal decomposition
([Cui et al. (2024)](/sources/cui-2024.md), Rem. 7.3), which has far fewer
internal nodes and therefore a cheaper limiter.

In the **simplified BP limiter** recalled by Cui et al. (Rem. 7.4, Eqs.
(7.16)–(7.18)), the internal nodes are replaced by the single state
$$\Pi_{ij}=\frac{1}{1-2\varpi}\Big(\bar u_{ij}-\varpi\Big[\tfrac{1+\varkappa}{2}\sum_q\mathsf w^{\mathrm G}_q\big(u^+_{i-1/2,q}+u^-_{i+1/2,q}\big)+\tfrac{1-\varkappa}{2}\sum_q\mathsf w^{\mathrm G}_q\big(u^+_{q,j-1/2}+u^-_{q,j+1/2}\big)\Big]\Big),$$
computed from the cell average and the edge Gauss values alone
($\mathsf w^{\mathrm G}_q$ the Gauss weights, $\varkappa$ the anisotropy
parameter of the decomposition page, both page-local; $u^\pm$ the traces at
the edge Gauss points). The limiter then enforces $G$ at the edge points
and at $\Pi_{ij}$. [Fan et al. (2021)](/sources/fan-2021.md) use the same
construction with the classic decomposition, because their Hermite WENO
reconstruction delivers point values, not a polynomial: in 1D the test
states are the two interface traces and
$$\frac{\bar u_i-\varpi\big(u^+_{i-1/2}+u^-_{i+1/2}\big)}{1-2\varpi},$$
($\varpi$ the Gauss–Lobatto endpoint weight) whose components are, by the
mean-value theorem, values of the corresponding components of the
reconstruction at points inside the cell, not necessarily the same point
(Eqs. (3.9)–(3.10), (3.14)); in 2D the eight edge Gauss traces and one
such residual state, with the two directions weighted by
$\Delta t/\Delta x$ and $\Delta t/\Delta y$ (Eqs. (3.26)–(3.27), (3.31)–(3.32)).
The limiter needs only the cell average and the point values (Rems. 3.2,
3.4).

**Exact minima.** In the conservative
[semi-Lagrangian finite-volume](/methods/semi-lagrangian-finite-volume.md)
scheme of [Zheng et al. (2022)](/sources/zheng-2022.md) the new average is
an integral of the reconstruction over a curved upstream cell evaluated by
Green's formula, not a decomposition into point values; the authors report
that minima at Gauss–Legendre points are then insufficient and compute the
minimum of the cubic reconstruction over the cell by solving
$\partial_xu_h=\partial_yu_h=0$, two quadratics whose solutions are
intersections of conic sections (Rem. 2.1, Eq. (24)). Positivity is then
proved provided the line integrals are evaluated exactly (Prop. 3.2).

## Time stepping and accuracy

The limiter is applied after every stage of an
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md) or SSP multistep method,
which preserves the property because each stage is a convex combination of
forward-Euler steps ([Cui et al. (2024)](/sources/cui-2024.md), Rem. 7.9;
[Wu & Shu (2023)](/sources/wu-2023-b.md), §6.2;
[Fan et al. (2021)](/sources/fan-2021.md), §3.3;
[Renac (2021)](/sources/renac-2021.md), §6.3). That the limiter keeps the
design order is cited, not shown, by Wu & Shu (App. B) and Fan et al.
(Rems. 3.2, 3.4, citing Zhang 2017); Cui et al. show order $N+1$
numerically for $\mathbb P^2$, $\mathbb P^4$, $\mathbb P^6$ and
$\mathbb P^8$ DG with the limiter on 2D linear advection, with errors very
close to those of the classic decomposition (Ex. 1, Tables 3–6); Fan et al.
observe fifth order in 1D and fourth order in 2D for Navier–Stokes at
$\mathrm{Re}=100$ (Table 4.1); Liu et al. second and third order on a
smooth Alfvén wave (Table 1).

**How often it acts.** Fan et al. count the cells in which either factor is
below one: 0.00% on the Lax problem, 10.00% on the double rarefaction,
3.00% on the 1D Sedov problem, 0.25% on Leblanc, 1.09% on the 2D Sedov
problem and 0.23% on the shock diffraction, the same for the hybrid and the
non-hybrid scheme (Table 4.2;
[double rarefaction](/benchmarks/double-rarefaction-problem.md),
[Sedov](/benchmarks/sedov-blast-wave.md),
[Leblanc](/benchmarks/leblanc-shock-tube.md)).

**As a special case of filtering.** [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md)
(§3.1, Remark (Limiting)) recover the linear scaling limiter as their
[entropy filtering](/methods/entropy-filtering.md) with a degenerate
"filter" that keeps the mean mode and multiplies all others by one factor,
and replace it by an exponential modal filter whose strength is set by the
same nodal constraints, which they call a nonlinear generally non-convex
limiting. On the Mach 800 jet they report "significantly better
resolution" than Wu & Shu's DG results with the linear limiter, partly
attributable to the magnetic field present in those (§5.1.6, Fig. 6).

**A separate oscillation control.** In most sources a separate mechanism
acts first in troubled cells flagged by a
[troubled-cell indicator](/definitions/troubled-cell-indicator.md): a WENO
limiter (KXRCF in Wu & Shu, §7; the Qiu–Shu WENO limiter in Cui et al.,
Ex. 3–5), the nonlinear HWENO reconstruction and a first-moment limiter in
Fan et al. (§1), or subcell finite volumes. The scaling limiter controls
bounds, not oscillations. [Liu et al. (2021)](/sources/liu-2021.md) are the
exception: they use no limiter other than this one and rely on the
data-dependent weights of [WLS-ENO](/methods/wls-eno.md) for the rest
(Abstract, §4).

## Finite-difference counterparts

Finite-difference schemes have no cell polynomial to scale. The
interpolation limiter of [Wong et al. (2021)](/sources/wong-2021.md)
(§5.1, Algorithms 1–3) is of the same kind: each interpolated midpoint
state is blended convexly with the adjacent node value, the first-order
state, successively for partial densities, volume fraction and
$\rho e-\bar p_\infty$ ([stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)); it is followed by a
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
on the fluxes.

[Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) (§3.3, Eqs.
(3.12)–(3.14), Algorithm 1) transfer the limiter itself to
finite-difference WENO for Navier–Stokes. Read as a formal finite-volume
scheme, the point value of each split variable at $x_i$ is the "cell
average" of an auxiliary function, and the WENO value at $x_{i+1/2}$ is
its interface trace
([positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md)).
For each interface they scale the reconstructed trace toward that point
value, first the density with
$\theta_1=\min\{1,(\bar\rho-\varepsilon_1)/(\bar\rho-\rho_{\min})\}$,
then the internal energy with the factor $\theta_2$ that brings $\rho e$ of the
trace and of the derived residual state up to $\varepsilon_1$, with
$\varepsilon_1=\min\{10^{-13},\bar\rho\}$ and $\bar\rho$ the point value
of the split density; the residual state is computed, not
reconstructed. Each interface uses one value per side, so the
limited flux stays conservative. The limiter is "essentially the same" as
the finite-volume one applied to the two formal schemes of the proof, and
the scheme reduces to Zhang and Shu's finite-difference scheme for Euler
when the viscous flux vanishes (§1.3, §3.3). It acts on few cells: at the
finest accuracy meshes 0.01–1.25 % (Tables 5.1–5.2), and on average per
step 0.0001–0.42 % in the 2D shock tests (Ex. 5.5–5.8). That it keeps
high order is stated, by reference to Zhang and Shu, not proved.

[Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) take the other
route for finite-difference Hermite WENO: they note that the earlier
finite-volume HWENO schemes enforce positivity by polynomial scaling, and
use instead a parametrized flux limiter, which "allows larger time steps
in practice and is more convenient for FD schemes" (§1, Remark 2.3).

## Qualifications

- **Incompatible with prescribed interface values.**
  [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) note that the
  scaling limiter cannot be used in [Active Flux](/methods/active-flux.md),
  whose reconstruction must interpolate given interface point values; they
  use power-law limiters that keep continuity instead (discussion after
  Thm 2.2).
- **Missing caps in two printings.** The arXiv v1 of Wu & Shu (2023) prints
  the density factor of App. B as $(\bar\rho-\varepsilon_1)/(\bar\rho-\min\rho)$
  without $\min\{1,\cdot\}$ (and the mass-fraction factor without a cap),
  so as printed it can exceed one; the text says the limiter acts only "if
  this happens", i.e. on violation. Zheng et al. (2022) likewise print
  $\theta_{i,j}=\min\{\lvert\bar u/(\bar u-m)\rvert\}$ with a single
  argument (Eq. (22)). Cui et al., Fan et al. (2021, 2022), Renac and Liu et al. print
  the cap.
- **A sign slip in one printing.** Fan et al. (2021)'s 1D energy factor (p. 6)
  prints the numerator $\rho e(u_q)-\varepsilon$, which is negative whenever
  the limiter triggers; their 2D version and their Eq. (3.15) carry
  $\rho e(\bar u_i)-\varepsilon$, which is the correct form.
- **Scope.** The guarantee is on cell averages and on the chosen point set;
  between points the polynomial may leave $G$.

# Citations

- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §1 (Eqs. (1.7)–(1.8)); Rems. 7.3, 7.4, 7.9 (Eqs. (7.15)–(7.18)); Rem. 8.1; Ex. 1 (Tables 3–6), Ex. 3–5.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: Thm 6.2 (Eq. (6.12)); §6.2; App. B; §7.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §1; §3.1 (Eqs. (3.9)–(3.10), (3.14)–(3.15), Rem. 3.2); §3.2 (Eqs. (3.26)–(3.27), (3.31)–(3.32), Rem. 3.4); §3.3; Tables 4.1–4.2.
- [Renac (2021)](/sources/renac-2021.md) — arXiv v3: Thm 6.1; §6.3 (Eq. (67)).
- [Liu et al. (2021)](/sources/liu-2021.md) — Abstract; §3.3.4 (Eqs. (36)–(38)); §4 (Table 1).
- [Zheng et al. (2022)](/sources/zheng-2022.md) — §2.3.3 (Eqs. (22)–(24), Rem. 2.1); Prop. 3.2.
- [Wong et al. (2021)](/sources/wong-2021.md) — arXiv v1: §5.1 (Algorithms 1–3).
- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — author preprint, discussion after Thm 2.2 (scaling limiter incompatible with prescribed interface values).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — arXiv v1: §3.3 (Eqs. (40)–(45), Prop. 3.1, Rems. 3.4–3.5).
- [Du & Yang (2022)](/sources/du-2022-b.md) — §4.1; §4.3 (limiter); Thm 4.3 (point set).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — arXiv v3: §3.1 (Remark (Limiting)); §5.1.6 (Fig. 6).
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §1.3; §3.3, Eqs. (3.12)–(3.14), Algorithm 1; Tables 5.1–5.2; Ex. 5.5–5.8.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — §1; Remark 2.3 (scaling not used; flux limiter instead).
