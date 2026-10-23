---
type: Method
title: "Zhang–Shu scaling limiter"
description: "The Zhang–Shu limiter scales a high-order polynomial linearly toward its cell average until the point values of a cell-average decomposition lie in the admissible set; it conserves the cell average and, with a BP first-order flux and a CFL bound, makes the update bound-preserving; a one-parameter blend toward a low-order update reuses its algebra."
status: established
aliases: [scaling limiter, bound-preserving limiter, positivity-preserving limiter, maximum-principle-satisfying limiter, BP limiter, simplified BP limiter, PP limiter]
tags: [bound-preserving, positivity, limiting, dg, finite-volume]
timestamp: 2026-10-23T14:55:00Z
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
- **Remapping on moving quadrilaterals** ([Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md),
  §2.6.3). The same two steps at the nine Simpson points of a
  quadrilateral mapped to $[-\tfrac12,\tfrac12]^2$: density with
  $\varepsilon_1=10^{-13}$, then the whole state with $\theta_2=1$ where
  $\rho e(\hat u)\ge0$ at the point ($\hat u$ the density-limited state) and otherwise
  $\theta_2=\min_q\rho e(\bar u_i)/\big(\rho e(\bar u_i)-\rho e(\hat u_q)\big)$
  over the points; the floor is zero, so by the concavity argument later in this section
  the limited states satisfy $\rho e\ge0$, not the strict $\rho e>0$ of
  $G$ *(compiler check, not in the sources)*. It is the limiter of their
  "P-WENO" [conservative remap](/methods/conservative-remapping.md); in
  the remap tests it removes all negative cell averages (Tables 3.1–3.3).
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
  [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (§3.1.3, Eq. (3.9),
  Lemma 3.2, Remark 3.4, arXiv v1) use the same two stages, $D$ then the
  concave $g$, with $\varepsilon_D=\min_i\{10^{-13},\bar D_i\}$ and
  $\varepsilon_g=\min_i\{10^{-13},g(\bar u_i)\}$ and the absolute values
  inside the minimum, in a finite-volume Hermite WENO scheme. The point set
  is the four Gauss–Lobatto points of the cell, the two inner ones
  included, plus the interior state
  $\Pi_i=\big(\bar u_i-\tfrac1{12}(u^+_{i-1/2}+u^-_{i+1/2})\big)/(1-\tfrac16)$
  of the four-point decomposition (in 2D, the Gauss points of the edges
  and the inner points, with the directional weights
  $\mu_1=\dfrac{a^{(1)}/\Delta x}{a^{(1)}/\Delta x+a^{(2)}/\Delta y}$,
  $\mu_2=1-\mu_1$, page-local, $a^{(1)}$, $a^{(2)}$ the global maximum
  wave speeds in $x$ and $y$).
  The inner points are limited too because the fluxes are evaluated there,
  and the recovery of the primitive variables converges only for states in
  $G$, which the authors note "differs from the Euler equations" (Remark
  3.4). Lemma 3.2, the admissibility of all limited states, is stated with
  a proof "similar to" Chen & Wu's Prop. 3.1.
- **Multicomponent MHD** ([Wu & Shu (2023)](/sources/wu-2023-b.md), App. B):
  three successive scalings — density, mass fractions (from negative
  partial densities), and the concave function
  $g(u)=E-\tfrac12\big(\lvert\rho v\rvert^2/\rho+\lvert B\rvert^2\big)$,
  used in place of the pressure, which is not concave in $u$ when $\gamma$
  depends on the mass fractions (Eq. (6.3)).
- **Relativistic MHD, central DG** ([Ding & Wu (2024b)](/sources/ding-2024-b.md),
  §3.3, §4.5, Eqs. (33)–(36), Remarks 4–6, 8). Three successive scalings
  into the shrunk set $\{D\ge\varepsilon_D,\ q\ge\varepsilon_q,\ \Phi_\varepsilon\ge0\}$,
  with $q=E-\sqrt{D^2+\lvert m\rvert^2}$ and $\Phi$ the closed-form third
  constraint of the relativistic MHD admissible set, $\Phi_\varepsilon$ the
  same with $E-\varepsilon$ ($\varepsilon=10^{-13}\bar E$): the density with
  $\varepsilon_D=\min\{10^{-13},\bar D\}$; then $(D,m,E)$ toward the mean
  with $\varepsilon_q=\min\{10^{-13},q(\bar u)\}$, $B$ left unscaled;
  then the whole vector with the smallest, over the points, root in
  $[0,1)$ of $\Phi_\varepsilon$ along the segment from the mean (Eq. (36); page-local $q$, $\Phi$,
  $\varepsilon_D$, $\varepsilon_q$). The point set is the Gauss–Lobatto
  points of the decomposition **plus** the Gauss flux-quadrature points,
  because the flux needs primitive variables recovered from conserved
  ones, which fails for inadmissible states, a requirement the authors say
  does not arise in non-relativistic MHD (Remark 6). In 1D the limiter
  keeps the constant $B_1$, in 2D the locally divergence-free space of the
  magnetic field (Remarks 4, 8; stated). Without it every shock test of the
  paper fails ([divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- **Euler with a nodal spectral-difference method** ([Chen & Fu (2024)](/sources/chen-2024.md),
  §8, Eqs. (80)–(84)). At the flux points of the
  [spectral difference method](/methods/spectral-difference-method.md),
  $\theta_1=\min\{(\bar\rho-\varepsilon_\rho)/(\bar\rho-\rho_{\min}),1\}$ for
  the density and, if some flux-point pressure is negative,
  $\theta_2=p(\bar u)/(p(\bar u)-p_{\min})$ for the whole vector. Only the
  double Mach reflection needs it, and only the pressure step: at $t=0$
  0.12 % of the cells, mean $\theta_2=0.96$, at the first step for third
  order and the first few steps for fourth order (§9, Fig. 4). The
  authors note that their TENO troubled-cell indicator can miss a
  direction in which three consecutive cells carry the same discontinuity,
  so the TENO limiter alone cannot guarantee positive pressure (§9).
- **Ideal MHD with a reconstructed pressure** ([Liu et al. (2021)](/sources/liu-2021.md),
  §3.3.4, Eqs. (36)–(38)): $\theta=\min\{1,(\bar u_i-\epsilon)/(\bar u_i-\min u_h)\}$,
  $\epsilon=\min\{10^{-13},\bar u_i\}$, applied to "the reconstructed
  polynomials of density and thermal pressure"; how the pressure polynomial
  is obtained from the reconstructed conservative variables is not stated.

- **Reacting Navier–Stokes in molar concentrations** ([Ching et al. (2025)](/sources/ching-2025.md),
  §4.3). Four successive scalings at the end of every Runge–Kutta stage, on the
  volume and surface quadrature points: the species concentrations $C_k$
  (page-local) toward their means by
  $\theta_1=(\rho(\bar u)-\varepsilon)/(\rho(\bar u)-\min\rho)$ if the density falls below
  $\varepsilon$ ($10^{-10}$, for example); each $C_k$ by its own
  $\bar C_k/(\bar C_k-\min C_k)$ where it is negative; the whole state by the
  same ratio form for $\rho e^*$, the internal energy shifted by its value at $T=0$
  (concave, so positivity follows); and, on the convective half of their split
  update only, the whole state by $\chi(\bar u)/(\chi(\bar u)-\min\chi)$ with
  $\chi=\rho s-\rho s_{\mathrm b}$ and $s_{\mathrm b}$ the local minimum of the
  specific entropy over the cell and its neighbours at the previous step
  (page-local $\chi$, $s_{\mathrm b}$). The new state is the mean of the limited
  convective and viscous halves
  ([positivity-preserving Navier–Stokes fluxes](/methods/positivity-preserving-navier-stokes-flux.md)).
  The authors state that the limiter "is not expected to suppress all small-scale
  instabilities" and run it with artificial viscosity.
- **Ideal MHD on finite-volume point values with a discrete divergence
  constraint** ([Ding & Wu (2024a)](/sources/ding-2024.md), §2.4, Eqs.
  (37)–(39), Thm 2.9, arXiv v1). The limiter acts on the interface quadrature
  values of a WENO reconstruction, with no polynomial: first the density alone,
  $\theta_1=\min\{(\bar\rho-\varepsilon_1)/(\bar\rho-\rho_{\min}),1\}$,
  $\varepsilon_1=\min\{10^{-13},\bar\rho\}$, then the whole state with the same form
  for the internal energy $E-\tfrac12(\lvert\rho v\rvert^2/\rho+\lvert B\rvert^2)$. For
  order $k\ge3$ the minima include the interior remainder state of the
  Gauss–Lobatto decomposition, written from the point values. The second step
  also scales $B$ toward its cell average, and the limited values keep the
  discrete divergence condition of the cell because the discrete divergence is
  linear and vanishes for a constant state (Thm 2.9). On a low-pressure vortex
  (minimum pressure about $5.3\times10^{-12}$) the fifth-order scheme with the
  limiter reaches orders $4.80$–$5.05$ (Table 4.1); without it the blast and jet
  computations stop on negative pressure (Ex. 4.4–4.5;
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)).
- **Five-equation two-phase model** ([Yan, Abgrall & Wu (2024)](/sources/yan-2024.md),
  Eqs. (2.39)–(2.40), (3.33)–(3.34), Thms 2.13–2.14). On the union of the Gauss and
  Gauss–Lobatto points, first one factor for the whole state, the smallest of
  $\min\{(1-\bar\phi_1)/(\max\phi_1-\bar\phi_1),\ \bar\phi_1/(\bar\phi_1-\min\phi_1),\ 1\}$
  for the volume fraction and of the density-type factors for the two partial
  densities (floors $\min\{\overline{\phi_k\rho_k},10^{-13}\}$), then a second factor for
  the internal energy with floor $\min\{\rho e(\bar u),10^{-13}\}$. The limiter maps
  $u$ to $\bar u+\theta_2\theta_1(u-\bar u)$ and is therefore invariant under linear
  identities $\Lambda u\equiv c$ (Thm 2.13, proof omitted), which is how it keeps
  uniform velocity and pressure at a material interface (Thm 2.14;
  [OEDG](/methods/oedg.md)).

**Iterated halving for the pressure.** In the GPU discontinuous Galerkin
code [TENET](/software/tenet.md), [Cernetic et al. (2023)](/sources/cernetic-2023.md)
(§4.2, Eq. 47, accepted manuscript) evaluate the density at the union of
the volume and surface Gauss quadrature points of the cell, and if its
minimum falls below $\rho_{\mathrm{bot}}=10^{-6}\bar\rho$ (page-local) they
multiply the higher modal weights of **all** fields by
$(\bar\rho-\rho_{\mathrm{bot}})/(\bar\rho-\rho_{\min})$. For the
pressure they "simply adopt" the factor $0.5$ and apply it repeatedly
until the minimum pressure exceeds a floor whose value is not printed.
They describe the limiter as a last line of defence that keeps the run
alive, not an oscillation control; it never acts on their smooth tests
and acts only during the first steps of discontinuous initial data.

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

## A one-parameter blend toward a low-order update

[Lin, Chan & Tomas (2023)](/sources/lin-2023.md) (§6.1, Eqs. 37–43) use
the same algebra with a different target: instead of scaling the
polynomial toward its cell average, they move the nodal update of an
entropy-stable DG element from a positivity-preserving low-order update
$u^{\mathrm L}_i$ toward the high-order one, $u_i=u^{\mathrm L}_i+\mathsf l_K\,P_i$ with
$P_i=\frac{\Delta t}{m_i}(r^{\mathrm L}_i-r^{\mathrm H}_i)$ and one $\mathsf l_K\in[0,1]$ per element $K$
($r^{\mathrm L}$, $r^{\mathrm H}$ the low- and high-order residuals, $m_i$ the lumped mass;
page-local), the largest $\mathsf l_K$ that keeps $\rho\ge\rho^{\min}_i$ and
$\rho e\ge\rho e^{\min}_i$ at every node. They call it "Zhang–Shu type".
The density bound is linear in $\mathsf l_K$; the internal-energy bound, multiplied
by $\rho>0$, is the quadratic $a\mathsf l^2+b\mathsf l+c\ge0$ with
$a=E^P\rho^P-\tfrac12\lvert(\rho v)^P\rvert^2$,
$b=E^{\mathrm L}\rho^P+\rho^{\mathrm L}E^P-(\rho v)^{\mathrm L}\cdot(\rho v)^P-\rho^P\rho e^{\min}$,
$c=E^{\mathrm L}\rho^{\mathrm L}-\tfrac12\lvert(\rho v)^{\mathrm L}\rvert^2-\rho^{\mathrm L}\rho e^{\min}$
(superscripts $\mathrm L$ and $P$ for the components of $u^{\mathrm L}_i$ and $P_i$), and $\mathsf l^{\rho e}$ is its smallest non-negative root,
or 1 if none; $\mathsf l_K=\min(\mathsf l^\rho,\mathsf l^{\rho e})$ (Eqs. 39–42) *(compiler check,
not in the sources: expanding $(\rho^{\mathrm L}+\mathsf l\rho^P)(E^{\mathrm L}+\mathsf lE^P)-\tfrac12\lvert(\rho v)^{\mathrm L}+\mathsf l(\rho v)^P\rvert^2-(\rho^{\mathrm L}+\mathsf l\rho^P)\rho e^{\min}$
gives these coefficients)*. The bounds are relaxed to
$\rho^{\min}_i=\zeta_{\mathrm r}\rho(u^{\mathrm L}_i)$,
$\rho e^{\min}_i=\zeta_{\mathrm r}\rho e(u^{\mathrm L}_i)$ with
$\zeta_{\mathrm r}\in(0,1]$ (page-local; 0.1 or 0.5 in the runs) rather
than to a floor $\epsilon_0$, which they found to avoid "the time-step
size converging to zero" (§6.1). The update stays a convex combination
of the low- and high-order states, so it is conservative and keeps the
semi-discrete entropy inequality of both (Theorem 6.2); the target is
the low-order solution, not the cell average
([convex limiting](/methods/convex-limiting.md),
[bound preservation](/properties/bound-preservation.md)).

[Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) (§2.2.2,
Eqs. 31–35, arXiv v1) meet the same quadratic pressure constraint in
monolithic convex limiting, one factor per subcell interface of an LGL
element rather than per element, and do not solve for its root: since
$\alpha^2\le\alpha$ on $[0,1]$ they replace $A\alpha^2+B\alpha\le Q$ by
the linear sufficient condition $\big(\max\{0,A\}+|B|\big)\alpha\le Q$,
which gives the factor in closed form (page-local $A$, $B$, $Q$; their
$\alpha$ = 1 is the high-order flux; see
[convex limiting](/methods/convex-limiting.md)).

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

## Scaling toward the mean as oscillation control

[Chen & Fu (2024)](/sources/chen-2024.md) (§5.6, Eqs. (66)–(69)) use the
same algebra in the opposite role, after their TENO limiter for the
spectral difference method: in cells where a five-point effective scaled
wavenumber exceeds $0.6$ ([scale sensor](/definitions/scale-sensor.md)),
the limited polynomial is compressed toward the cell average,
$\tilde u^{\mathrm{new}}=(1-r_{\mathrm c})\bar u_i+r_{\mathrm c}\tilde u_h$,
$r_{\mathrm c}=\min\Big\{\frac{\bar u_i-u_{\mathrm{low}}}{\bar u_i-u_{\min}},\frac{u_{\mathrm{high}}-\bar u_i}{u_{\max}-\bar u_i},1\Big\}$,
with $u_{\mathrm{low}}$, $u_{\mathrm{high}}$ the extreme nodal values of the
cell and its two neighbours and $u_{\min}$, $u_{\max}$ those of the limited
polynomial in the cell (page-local $r_{\mathrm c}$). The bounds are local,
not those of an admissible set, so the step keeps the cell's nodal values
within the nodal range of the cell and its two neighbours where the
sensor fires *(compiler check, not in the sources)*; the authors use it
for robustness at strong shocks ([WENO limiters for DG](/methods/weno-limiter-dg.md)).

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
- **Chen & Fu's pressure factor** is printed as a minimum of a single
  argument, $\theta_2=\min\{p(\bar u)/(p(\bar u)-p_{\min})\}$, and has no
  floor, so with $p$ concave in $u$ it gives $p\ge0$ at the flux points,
  not $p>0$ (Eq. (83)) *(compiler check, not in the sources)*; the density
  floor is written $\epsilon_\rho$ in the equation and $\varepsilon_\rho$
  in the text.
- **Point values that a constraint couples.** Ding & Wu (2024a) state that the
  coupling of the interface values by their discrete divergence condition
  "invalidates" the classical convex-decomposition proof of Zhang & Shu, and prove
  positivity of the averages with
  [geometric quasilinearization](/methods/geometric-quasilinearization.md) instead
  (§3); the limiter itself is unchanged in form.
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
- [Gu, Li, Cheng & Shu (2023)](/sources/gu-2023.md) — §2.6.3; §3.1–3.3, Tables 3.1–3.3.
- [Lin, Chan & Tomas (2023)](/sources/lin-2023.md) — arXiv v2: §6.1, Eqs. (37)–(44); §6.2, Theorem 6.2; §7.
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — arXiv v1: §3.1.3, Eq. (3.9); Lemma 3.2; Remark 3.4; §4.1 (2D point set).
- [Cernetic et al. (2023)](/sources/cernetic-2023.md) — accepted manuscript: §4.2, Eq. (47).
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — arXiv v1: §2.2.2, Eqs. (31)–(35).
- [Ding & Wu (2024b)](/sources/ding-2024-b.md) — §3.3, Eqs. (33)–(36), Remarks 4–6; §4.5, Eq. (75), Remark 8; §5.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §5.6, Eqs. (66)–(69); §8, Eqs. (80)–(84); §9, Fig. 4.
- [Ching et al. (2025)](/sources/ching-2025.md) — §4.3 (limiting procedure); Remark 9.
- [Ding & Wu (2024a)](/sources/ding-2024.md) — arXiv v1: §2.4, Eqs. (37)–(39), Thm 2.9; §3 intro; §4, Table 4.1, Ex. 4.4–4.5.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Eqs. (2.39)–(2.40), (3.33)–(3.35); Thms 2.13–2.14.
