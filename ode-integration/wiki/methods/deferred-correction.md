---
type: Method
title: "Deferred correction (DeC)"
description: "Arbitrarily high-order integrators that correct a cheap low-order solution by high-order defect estimates: Abgrall's subnode form (bDeC, sDeC and their convex family, all Runge–Kutta methods) iterates a low-order operator against a collocation operator, can add subnodes between iterations, and has Patankar, two-derivative and spectral (SDC) variants; the implicit-midpoint hierarchy DC2j is A-stable at every order."
status: established
aliases: [DeC, deferred correction method, Abgrall's DeC, explicit DeC, IMDeC, implicit deferred correction, DC2j, deferred correction for the implicit midpoint rule, difference correction, spectral deferred correction, SDC, multirate SDC, MRSDC, bDeC, sDeC, alpha-DeC, αDeC, bDeCu, bDeCdu, sDeCu, sDeCdu, efficient DeC, p-adaptive DeC, mPDeC, MPDeC, modified Patankar deferred correction, HBPC, Hermite–Birkhoff predictor–corrector, two-derivative deferred correction, Picard SDC, adaptive SDC]
tags: [deferred-correction, explicit, implicit, stiff, order-conditions, stability]
timestamp: 2026-10-20T06:18:00Z
---

# Deferred correction (DeC)

Deferred correction computes the solution of a high-order implicit collocation problem
on subnodes of one step. It does so by a fixed number $K$ of corrections, each of which
solves only a cheap low-order problem. In the two-operator form of Abgrall, used by
[Han Veiga et al. (2021)](/sources/hanveiga-2021.md) (§3, after Dutt, Greengard &
Rokhlin), a low-order explicit operator $\mathcal L^1$ is iterated against a high-order
operator $\mathcal L^2$. The fixed point of the iteration is the collocation solution
$\mathcal L^2=0$, and each iteration gains one order of accuracy. The method reaches
arbitrary order without solving Runge–Kutta
[order conditions](/results/runge-kutta-order-conditions.md), which Han Veiga et al. give
as its motivation (§1, Remark 3.2). With $K$ fixed it is itself a
[Runge–Kutta method](/definitions/runge-kutta-method.md) (Remark 3.2, citing Christlieb,
Ong & Qiu), whose Butcher tableaux [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md)
write out (§5, Tables 1–4). Micalizzi & Torlo also order the variants into one family
(bDeC, sDeC and their convex combinations), show that subnodes can be added between
iterations to save stages, and prove the stability function of the bDeC branch. The same
iteration carries a Patankar modification for positivity
([Torlo et al. 2022](/sources/torlo-2022.md); [Ciallella et al. 2022](/sources/ciallella-2022.md)),
an implicit two-derivative corrector ([Zeifang & Schütz 2022](/sources/zeifang-2022.md)),
and, read as a preconditioned Picard iteration, spectral deferred correction (SDC)
([Saupe et al. 2025](/sources/saupe-2025.md); [Čaklović et al. 2025](/sources/caklovic-2025.md)).

A second family corrects across the time grid instead of within one step.
[Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) build a hierarchy
DC2, DC4, DC6, … on the implicit midpoint rule. Each level is computed with the
same implicit-midpoint step as the base scheme, plus centred finite-difference
corrections evaluated on the previous level's solution, and has order $2j$. Every level
is A-stable in their sense and B-convergent, and for $j\ge1$ the scheme is not a
Runge–Kutta method (§2, Remark 2.3). It extends the Gustafsson–Kress idea from linear
problems under monotonicity to nonlinear problems (§1). The two families share the
principle (a low-order solve corrected by a high-order defect) but neither source
relates them; they are described separately below.

**Page-local notation (subnode DeC).** Problem $y'=f(y)$ (autonomous; the source writes
$\partial_t\alpha+F(\alpha)=0$, so $f=-F$). Subnodes $t_{n,m}=t_n+c_mh$,
$m=0,\dots,\mathsf M$, with $c_0=0$ and $c_{\mathsf M}=1$ when the nodes include the
endpoints. $Y_m^{(k)}$ is the subnode value after $k$ corrections, and
$\mathbf Y=(Y_0,\dots,Y_{\mathsf M})$. $\ell_r$ are the Lagrange polynomials on the nodes
$c_0,\dots,c_{\mathsf M}$ (a basis, unrelated to the registry's multirate micro-step
index $\ell$). $\omega_{mr}=\int_0^{c_m}\ell_r(\vartheta)\,d\vartheta$ are the
integration weights (the source's $\theta^m_r$, normalized to the unit interval).

## The two operators and the iteration

The high-order operator is the collocation (Picard-integral) form on the subnodes, and the
low-order operator is forward Euler from $t_n$ (Han Veiga et al. 2021, eqs. (18)–(20);
signs translated):

$$\begin{aligned}
\mathcal L^2(\mathbf Y)_m&=Y_m-Y_0-h\sum_{r=0}^{\mathsf M}\omega_{mr}\,f(Y_r),\\
\mathcal L^1(\mathbf Y)_m&=Y_m-Y_0-c_m\,h\,f(Y_0),\qquad m=1,\dots,\mathsf M .
\end{aligned}$$

$\mathcal L^2(\mathbf Y)=0$ is an implicit collocation method. The DeC algorithm
(eq. (23)) sets $Y_0^{(k)}=y_n$ for all $k$ and $Y_m^{(0)}=y_n$, then iterates

$$\mathcal L^1(\mathbf Y^{(k)})=\mathcal L^1(\mathbf Y^{(k-1)})-\mathcal L^2(\mathbf Y^{(k-1)}),\qquad k=1,\dots,K,$$

and returns $y_{n+1}=Y^{(K)}_{\mathsf M}$. The unknown enters only through $\mathcal L^1$,
so each correction is explicit. With the forward-Euler $\mathcal L^1$ the correction
collapses to *(compiler algebra, not in the sources)*

$$Y_m^{(k)}=y_n+h\sum_{r=0}^{\mathsf M}\omega_{mr}\,f\big(Y_r^{(k-1)}\big),$$

a discrete Picard iteration on the collocation problem. One step therefore costs
$1+(K-1)\mathsf M$ evaluations of $f$ ($Y^{(0)}_r=y_n$ for all $r$, so the first
correction needs only $f(y_n)$) *(compiler count)*.

**Convergence** (Abgrall's proposition, Prop. 3.1, as recalled by Han Veiga et al.;
Micalizzi & Torlo 2024, Thm. 2.1, with the proof in their supplement, Thm. 1.1). Let
$\mathcal L^1$ be coercive,
$\kappa_1\lVert\mathbf Y-\mathbf Z\rVert\le\lVert\mathcal L^1(\mathbf Y)-\mathcal L^1(\mathbf Z)\rVert$.
Let $\mathcal L^1-\mathcal L^2$ be Lipschitz with constant $\kappa_2h$. Let
$\mathcal L^2=0$ have a unique solution $\mathbf Y^*$ ($\kappa_1$, $\kappa_2$ page-local).
If $\kappa_2h/\kappa_1<1$, the iteration converges and
$\lVert\mathbf Y^{(k)}-\mathbf Y^*\rVert\le(\kappa_2h/\kappa_1)^k\lVert\mathbf Y^{(0)}-\mathbf Y^*\rVert$.
Each correction therefore gains one power of $h$, and $K$ corrections give order
$\min(\mathsf M+1,K)$ (see [equivalence of DeC and ADER](/results/dec-ader-equivalence.md),
Thm. 4.5). Han Veiga et al. take $K=\mathsf M+1$, "as many iterations as the desired order
of accuracy" (§3). If the collocation solution has order $p$ and the start is first-order
accurate, $K=p$ iterations is optimal and more are wasted (Micalizzi & Torlo 2024, §2).
The collocation order depends on the subnodes: $\mathsf M+1$ for equispaced subnodes,
$2\mathsf M$ for Gauss–Lobatto subnodes, for which $\mathcal L^2=0$ is the Lobatto IIIA
method (Micalizzi & Torlo 2024, §3.1, Supp. Props. 2.1–2.2;
Ciallella et al. 2022, §4.1). Order $p$ therefore takes $\mathsf M=p-1$ equispaced or
$\mathsf M=\lceil p/2\rceil$ Gauss–Lobatto subintervals, with $K=p$ iterations; the
Lipschitz constant of $\mathcal L^1-\mathcal L^2$ is $\kappa_2=L_f\max_m\sum_{r=1}^{\mathsf M}\lvert\omega_{mr}\rvert$ (the sum omits $r=0$, since $Y_0=y_n$ is data)
with $\kappa_1=1$ ($L_f$ the Lipschitz constant of $f$, page-local; Micalizzi & Torlo 2024,
§3.1, Supp. Remark 2.1).

**Choices** (Remark 3.2). A higher-order $\mathcal L^1$ speeds up convergence of the
iteration but can lower the final accuracy, because the error loses smoothness (citing
Christlieb et al.). Gauss–Legendre subnodes exclude the endpoint and need an extrapolation
to $t_{n+1}$. For continuous finite elements, mass lumping in $\mathcal L^1$ avoids inverting
the global mass matrix while $\mathcal L^2$ keeps the consistent one. This is Abgrall's
motivation, and it makes residual-distribution schemes high order in time (§3, §4.5.1).
Micalizzi & Torlo (2024, §7.2, Remark 7.1) make the continuous-Galerkin version precise:
$\mathcal L^1$ uses forward Euler with first-order lumping $\int\varphi_i$ of each basis
function, which is well posed iff these integrals are nonzero (true for Bernstein
elements, false for quadratic Lagrange elements on triangles), and the scheme is not a
Runge–Kutta method because $\mathcal L^1$ and $\mathcal L^2$ carry different mass matrices.
Its operator properties are proved under a Poincaré-like assumption (Supp. §3); see
Qualifications for the order loss they observe.

## The bDeC–sDeC family

The correction above integrates over the "big" interval $[t_n,t_{n,m}]$ and is called
**bDeC**; it updates all subnodes in parallel within an iteration. **sDeC** marches
subnode by subnode over the "small" intervals $[t_{n,m-1},t_{n,m}]$ (Micalizzi & Torlo
2024, §3.2, Eqs. (11)–(15)). With page-local $\Delta c_m=c_m-c_{m-1}$, small-interval
weights $\omega^{\mathrm s}_{mr}=\int_{c_{m-1}}^{c_m}\ell_r(\vartheta)\,d\vartheta$ (so
$\sum_{j\le m}\omega^{\mathrm s}_{jr}=\omega_{mr}$) and a parameter $\alpha\in[0,1]$
(page-local, after Ketcheson & bin Waheed), the convex family **αDeC** reads (Eq. (16))

$$Y^{(k)}_m=y_n+h\sum_{r=0}^{\mathsf M}\omega_{mr}f\big(Y^{(k-1)}_r\big)+\alpha h\sum_{j=0}^{m-1}\Delta c_{j+1}\Big(f\big(Y^{(k)}_j\big)-f\big(Y^{(k-1)}_j\big)\Big),$$

with $\alpha=0$ bDeC and $\alpha=1$ sDeC. sDeC is the forward-Euler spectral deferred
correction of Dutt, Greengard & Rokhlin in residual/error form (proved by direct
computation, App. A.1); bDeC has an analogous residual form (App. A.2), and the sDeC iterate
is an $\mathcal O(h^{k+1})$ perturbation of the bDeC iterate (Supp. Prop. 2.4). In stage
counts, αDeC with $\alpha\ne0$ costs $\mathsf MK$ evaluations, bDeC $\mathsf M(K-1)+1$
because only the endpoint is needed in the last iteration (§5.1, Tables 1–2), in agreement
with the count above. Micalizzi & Torlo prefer Abgrall's operator form to the
residual form because structure-preserving, mass-matrix-free and ADER generalizations are
"straightforward" in it (§2–3).

## Efficient DeC: adding subnodes between iterations

Iteration $k$ is only $k$-th order accurate, yet the standard algorithm evaluates $f$ on
all $\mathsf M+1$ subnodes from the first iteration. Micalizzi & Torlo (2024, §4) start
from the two nodes $t_n$, $t_{n+1}$ and add one equispaced subnode per iteration,
passing from $k+1$ to $k+2$ nodes by Lagrange interpolation, until $\mathsf M+1$ nodes are
reached; a final iteration without interpolation reaches the order of the full method. The
"ladder" idea was used in implicit SDC by Minion and others; the authors say it had "never
been deeply studied and analyzed" for explicit DeC (§1). Two variants:

- **αDeCu** interpolates the solution: the interpolated vector of iteration $k-1$ feeds
  the right-hand side of iteration $k$ (Eqs. (25)–(27));
- **αDeCdu** interpolates the right-hand side values $f(Y^{(k-1)}_r)$ instead (Eq. (29)).

They coincide on linear problems, since interpolation commutes with a linear right-hand
side (Thm. 6.2, proved). Stage counts (§5.2–5.3): bDeCu
$\mathsf M(K-1)+1-\frac{(\mathsf M-1)(\mathsf M-2)}2$; αDeCdu
$\mathsf MK-\frac{\mathsf M(\mathsf M-1)}2$; bDeCdu
$\mathsf M(K-1)+1-\frac{\mathsf M(\mathsf M-1)}2$; αDeCu with $\alpha\ne0$ has no stage
reduction, but about half its stages are cheap interpolations (Remark 5.1). The
theoretical speed-ups (stage ratios) at order 13 (Tables 5–6):

| subnodes | αDeCdu | bDeCu | bDeCdu |
|---|---|---|---|
| equispaced, $\mathsf M=12$ | 1.733 (156→90) | 1.611 (145→90) | 1.835 (145→79) |
| Gauss–Lobatto, $\mathsf M=7$ | 1.300 (91→70) | 1.214 (85→70) | 1.328 (85→64) |

With Gauss–Lobatto subnodes the interpolation must happen in the first iterations, since
$k+1$ Gauss–Lobatto nodes give a collocation order $2k$ but interpolation only order $k+1$
(§4.3). The accuracy of the new variants is argued, not proved. Measured on two ODEs and
two hyperbolic PDEs, the new bDeC variants dominate the error–CPU-time Pareto front: about
2 for equispaced order 9 on a linear system, about $\frac43$ with Gauss–Lobatto nodes, up
to 1.8 on 1-D advection with continuous finite elements, and 1.25 on a 2-D shallow-water
vortex, equal to the theoretical $\frac54$ when interpolated stages are not counted; for
sDeC the gain is irregular (§9, Figs. 5, 7, 10, 12).

**Order adaptivity** (§8, Eq. (60)). Because the node count need not be fixed in advance,
the iteration can continue until the relative change of the endpoint value between two
successive iterations falls below a tolerance. With tolerance $10^{-8}$ at fixed $h$ the
error is roughly constant in $h$ and the mean iteration count falls from about 13 to about 5
as $h$ decreases (Figs. 6, 9). This adapts the order, not the step.

## Linearly implicit DeC for stiff sources (IMDeC)

For $y'=f^{\mathrm E}(y)+f^{\mathrm I}(y)$ with stiff $f^{\mathrm I}$, the IMDeC of
Abgrall & Torlo (as recalled by Han Veiga et al. 2021, §4.4, eqs. (38)–(42)) puts the
stiff part into $\mathcal L^1$, linearized at $y_n$:

$$\mathcal L^1(\mathbf Y)_m=Y_m-Y_0-c_mh\Big(f^{\mathrm E}(Y_0)+J^{\mathrm I}_n\,Y_m\Big),\qquad J^{\mathrm I}_n=\frac{\partial f^{\mathrm I}}{\partial y}(y_n)$$

($J^{\mathrm I}_n$ page-local). Each correction then solves, at every subnode,

$$\big(I-c_mh\,J^{\mathrm I}_n\big)\big(Y_m^{(k)}-Y_m^{(k-1)}\big)=-\mathcal L^2\big(\mathbf Y^{(k-1)}\big)_m,$$

i.e. a $d\times d$ linear system per subnode, in which the Jacobian does not interact with
the subnode coupling. Han Veiga et al. compare it with the implicit ADER, which couples all
subnodes in one larger system (see [ADER](/methods/ader-time-integration.md)). On a stiff
linear three-species system ($h=1$, fourth order) and on the [Robertson problem](/benchmarks/robertson-problem.md) (third order,
30 steps with $h_n=2h_{n-1}$), both implicit variants follow the reference solution while the
explicit DeC and ADER fail. Implicit ADER is visibly more accurate than IMDeC (Figs. 9–10).
Their heuristic is that IMDeC treats the $\mathcal L^1$ terms "in a very simplified first
order manner", while implicit ADER "is closer to a pure implicit scheme" (§4.4, §5.3).
Abgrall & Torlo's scheme was designed as an AP IMEX scheme for kinetic models (see
[asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)).

## Modified Patankar DeC (mPDeC)

For a [production–destruction system](/definitions/production-destruction-system.md) the
modified Patankar DeC of Öffner & Torlo, as recalled by Torlo et al. (2022, §2) and
Ciallella et al. (2022, §4.3), multiplies each production and destruction term of the
bDeC correction by a Patankar weight in the unknown subnode value, which makes every
correction a linear system with an M-matrix: unconditionally positive and conservative.
Negative interpolation weights $\omega_{mr}$ are handled by swapping the index of the
weighted value, so that the matrix keeps a positive diagonal and nonpositive off-diagonal
entries. Order $p$ uses $\mathsf M=p-1$ equispaced subintervals and $K=p$ corrections;
mPDeC1 is the modified Patankar–Euler method and mPDeC2 is MPRK(2,2,1). The family, its
weights and its competitors are on
[modified Patankar methods](/methods/modified-patankar-methods.md); the DeC-specific
findings are these:

- **Oscillation-free step bounds.** On the linear $2\times2$ test of Torlo et al. (2022,
  Fig. 6a) the largest oscillation-free step is 2 for mPDeC2 (proved sharp, Thm. 4.7) and
  irregular at higher order with equispaced subnodes (1.19, 1.11, 1.07, 1.04, 1.04, 1.37,
  6.96, 1.0, 15.5, … for orders 3 to 11); with Gauss–Lobatto subnodes it is 1.0 from order
  6 on. Unconditional positivity does not make the scheme free of oscillations.
- **Order reduction for vanishing data** (Thm. 5.5). When a component starts at
  $\varepsilon\to0$ faster than $h$, mPDeC drops to order 2, and to order 1 if a final
  correction weight $\omega_{\mathsf Mr}$ is negative (equispaced order 9 and orders
  $\ge11$); a negative weight carries the vanishing state through the iterations
  (Prop. 5.6). Gauss–Lobatto mPDeC drops only to order 2 (§6, Table 2).
- **First PDE use.** Ciallella et al. (2022, §4–6) apply mPDeC5 to the water height of a
  WENO5 finite-volume shallow-water scheme, written as a production–destruction system of
  face fluxes, while the momenta take the explicit DeC5 with the same subnodes and
  corrections. Each correction solves a sparse system with at most 5 nonzeros per row by
  Jacobi iteration (10–20 iterations, worst case 40). The water height stays positive at
  Courant numbers up to 1.5 in a dry dam break, fifth order is kept, and the overhead over
  DeC5 is about 10–18 %. The step is still limited by the explicit DeC of the momenta, and
  the stability of the combination is assumed, not analysed (Remark 5.5).
- **Against multistep Patankar methods.** [Izzo et al. (2025)](/sources/izzo-2025.md)
  (§4) find the Öffner–Torlo mPDeC code more efficient than their modified Patankar linear
  multistep methods on small systems and less efficient on a 6-species Brusselator, an
  8-compartment epidemic model and a diffusion PDE; on the epidemic model with zero initial
  components the mPDeC code returns NaN. Their explanation (several linear systems per step
  against one) is not measured.

## Two-derivative implicit DeC (HBPC)

Zeifang & Schütz (2022, §2, Alg. 1) use deferred correction to approximate an implicit
two-derivative Hermite–Birkhoff Runge–Kutta method of order $p\in\{4,6,8\}$ on $s$
equispaced nodes $c_1=0<\dots<c_s=1$ (tableaux on
[multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md); $\dot f$ as in the
registry, $\Delta c_l=c_l-c_{l-1}$ page-local). The **predictor** marches the implicit
fourth-order two-point Hermite rule over the subintervals,

$$Y^{(0)}_l=Y^{(0)}_{l-1}+\frac{\Delta c_lh}2\Big(f(Y^{(0)}_{l-1})+f(Y^{(0)}_l)\Big)+\frac{(\Delta c_lh)^2}{12}\Big(\dot f(Y^{(0)}_{l-1})-\dot f(Y^{(0)}_l)\Big),$$

and each **correction** is an implicit two-derivative Taylor step against the Hermite–Birkhoff
quadrature $I_l$ of the previous iterate,

$$Y^{(k+1)}_l=y_n+h\Big(f(Y^{(k+1)}_l)-f(Y^{(k)}_l)\Big)-\frac{h^2}2\Big(\dot f(Y^{(k+1)}_l)-\dot f(Y^{(k)}_l)\Big)+I_l\big(\mathbf Y^{(k)}\big),\qquad I_l=h\sum_ja_{lj}f(Y_j)+h^2\sum_j\dot a_{lj}\dot f(Y_j),$$

with $y_{n+1}=Y^{(K)}_s$. The order is $\min(4+K,p)$, one per correction from the
fourth-order predictor (Remark 2, quoted from Schütz, Seal & Zeifang and confirmed up to
order 8, Figs. 7–9); corrections beyond saturation can still lower the error. The scheme,
HBPC($p$, $K$), is a DeC whose low-order operator is the implicit two-derivative Taylor
step, as IMDeC's is a linearized implicit Euler step *(compiler remark, not in the sources)*. Every predictor
and corrector stage is one nonlinear system
$Y-\alpha_1hf(Y)+\frac{\alpha_2h^2}2\dot f(Y)=\text{known}$ ($\alpha_1$, $\alpha_2$
page-local: $\frac{\Delta c_l}2,\frac{\Delta c_l^2}6$ in the predictor, $1,1$ in the
corrector; Eqs. (7)–(9)), solved by Newton–GMRES with the extended preconditioner on
[implicit stage solvers](/methods/implicit-stage-solvers.md). The predictor of Zeifang &
Schütz is fully implicit; the original HBPC of Schütz, Seal & Zeifang used an IMEX
predictor, so the two variants share a name but not the predictor (§2).

## Linear stability

For $y'=\lambda y$ the explicit DeC (orders 2 to 5) and explicit ADER have identical
stability regions, independent of the node family (equispaced, Gauss–Lobatto,
Gauss–Legendre), and the regions grow with the order (Han Veiga et al. 2021, §5.1, Fig. 2;
computed numerically). They call an analytic study "not feasible". Their reason is that it
"leads to solving polynomial inequalities of degree $p(p+1)$". The node independence has a
short explanation, first given here as a compiler check and since proved by Micalizzi &
Torlo (2024, Thm. 6.1): the stability function of every bDeC, bDeCu and bDeCdu method of
order $K$ is

$$R(z)=\sum_{j=0}^{K}\frac{z^j}{j!},$$

for every distribution of subnodes. Their proof writes the Butcher matrix in $K$ block rows
with nonzero blocks only in the first block column and the first block subdiagonal, so
$A^K=0$ and $R$ is a polynomial of degree $K$ that matches $e^z$ to order $K$. This is the
[stability polynomial](/definitions/stability-function.md) of every $K$-stage explicit
Runge–Kutta method of order $K\le4$: the extra stages of bDeC buy no stability. sDeC is
different: its regions depend on the subnodes and differ from bDeC's, and sDeCu and sDeCdu
share theirs by Thm. 6.2 (Fig. 3, orders 3–13, computed). The Picard form of SDC with $K$
sweeps reproduces the contour of the $K$-stage order-$K$ explicit method
(Čaklović et al. 2025, §3.2, Fig. 5), as expected if Picard SDC is read as the bDeC
iteration (see below) *(compiler remark, not in the sources)*.

## Accuracy observations

On the scalar test $y'=\lambda y$ ($\lambda=10$, $t\in[0,0.1]$), with orders up to 11, DeC
keeps its design order with equispaced nodes. ADER with equispaced nodes does not at the
highest orders. Han Veiga et al. attribute this to DeC not needing a mass matrix (§5.2.1),
and they note that equispaced quadrature weights turn negative from ninth order. On a
nonlinear scalar ODE, a linear three-species system, Lotka–Volterra (including $t\le100$
with $h=1$) and on spectral-difference semi-discretizations of linear advection and
Burgers (orders 3 to 9, $h=\frac{0.5}{\mathsf M+1}\frac{\Delta x}{\lvert v_{\max}\rvert}$),
DeC and ADER both reach their design orders (§5.2–5.3).

Micalizzi & Torlo (2024, §9.1) confirm orders 3–9 on a linear $2\times2$ system and a
damped forced oscillator; on the linear system bDeC, bDeCu and bDeCdu give identical
errors, on the forced (non-autonomous) oscillator they differ slightly, the new variants
being a little less accurate at fixed $h$ but cheaper.

**Relation to ADER.** [Popov (2024)](/sources/popov-2024.md) (Introduction) repeats the
finding of Han Veiga et al. that DeC "competes with" ADER and is easier to implement; his
own [ADER](/methods/ader-time-integration.md) solver is the implicit variant, iterated to
convergence. Micalizzi & Torlo (2024, Conclusions) list the extension of subnode interpolation to
ADER as future work. The algebraic link between the two is on
[equivalence of DeC and ADER](/results/dec-ader-equivalence.md).

## Deferred correction of the implicit midpoint rule (DC$2j$)

**Page-local notation (DC$2j$).** Uniform step $h$, $t_n=nh$, $t_{n+1/2}=t_n+h/2$.
$y^{[2j]}_n$ is the level-$2j$ approximation of $y(t_n)$. For a grid sequence $v_n$:
$Dv_{n+1/2}=(v_{n+1}-v_n)/h$, $Ev_{n+1/2}=(v_{n+1}+v_n)/2$,
$D_+v_n=(v_{n+1}-v_n)/h$, $D_-v_n=(v_n-v_{n-1})/h$, so $D_+D_-$ is the centred second
difference. $d_{2i}$, $d_{2i+1}$ are the coefficients of the centred expansions (the
source's $c_{2i}$, $c_{2i+1}$, renamed because $c$ is the abscissa vector). $\Lambda$
and $\mu$ are the Lipschitz and one-sided Lipschitz constants of $f$, as on
[B-convergence](/definitions/b-convergence.md). The source writes $u'=F(t,u)$ with step
$k$ in a Banach space.

**Centred expansions.** As recalled by Koyaguerebo-Imé & Bourgault (2022, Eqs.
(2.4)–(2.5), from their companion preprint),

$$\begin{aligned}
y'(t_{n+1/2})&=Dy(t_{n+1/2})-\sum_{i=1}^{j}d_{2i+1}h^{2i}(D_+D_-)^iDy(t_{n+1/2})+\mathcal O(h^{2j+2}),\\
y(t_{n+1/2})&=Ey(t_{n+1/2})-\sum_{i=1}^{j}d_{2i}h^{2i}(D_+D_-)^iEy(t_{n+1/2})+\mathcal O(h^{2j+2}).
\end{aligned}$$

The values of $d_{2i}$, $d_{2i+1}$ are not printed; Taylor expansion gives $d_2=1/8$
and $d_3=1/24$ *(compiler check, not in the sources)*. Inserting these expansions into the midpoint rule
for the unknown itself gives a centred multistep scheme, "multi-steps and prone to
stability restrictions", which the authors do not use (Eq. (2.6)).

**The scheme** (Eqs. (2.7)–(2.9)). DC2 is the implicit midpoint rule. For $j\ge1$
the corrections are applied to the *previous level's* solution:

$$\frac{y^{[2j+2]}_{n+1}-y^{[2j+2]}_n}{h}-\sum_{i=1}^{j}d_{2i+1}h^{2i}(D_+D_-)^iD\,y^{[2j]}_{n+1/2}
=f\Big(t_{n+1/2},\;\frac{y^{[2j+2]}_{n+1}+y^{[2j+2]}_n}{2}-\sum_{i=1}^{j}d_{2i}h^{2i}(D_+D_-)^iE\,y^{[2j]}_{n+1/2}\Big),$$

with $y^{[2j+2]}_0=y_0$. The correction sums use $y^{[2j]}$ at $t_{n-j},\dots,t_{n+1+j}$,
so each lower level runs $j$ steps ahead of the next. Each new value solves one
nonlinear system of implicit-midpoint shape, $x-a-hf\big(t_{n+1/2},\tfrac12x+b\big)=0$
with known $a$, $b$ (page-local), so it reuses the base scheme's
[stage solver](/methods/implicit-stage-solvers.md). DC$2j$ costs $j$ such solves per
step over all levels and stores $j^2+3j+1$ vectors (Remark 2.2, Eq. (2.14); §6.7).
The first $j$ values of level $2j+2$ are computed by the same correction on a sub-grid
of step $h/(2j+1)$ inside the first step, with one-interval expansions whose
coefficients are tabulated for $j\le4$ (for $j=1$: $9/8$ and $9/8$), so no values
at $t<0$ are needed (Remark 2.1, Eqs. (2.10)–(2.13), Table 2.1).

**Not a Runge–Kutta method.** For $j\ge1$, $y^{[4]}_{n+1}$ depends on values
$y^{[2]}_i$ that evolve independently of $y^{[4]}_n$ and are not stages computed from
it, so DC$2j$ is not a [Runge–Kutta method](/definitions/runge-kutta-method.md) and has
no one-step recurrence $y_{n+1}=R(z)y_n$. The authors call this "the main ingredient
behind the A-stability of our DC2j methods independently of the order of accuracy"
(Remark 2.3). This contrasts with the subnode DeC above, which with $K$ fixed is a
Runge–Kutta method.

### Convergence theory

- **Deferred Correction Condition** (Def. 3.1). A level-$2j$ solution satisfies it if
  it has order $2j$ and the centred differences $(D_+D_-)D$ and $D_+D_-$ of its error
  are also $\mathcal O(h^{2j})$: the error must be smooth across the grid for the
  difference corrections to act on it.
- **One level up** (Thm. 3.1). If level $2j$ satisfies the condition and the starting
  values of level $2j+2$ are $\mathcal O(h^{2j+2})$, then level $2j+2$ has order
  $2j+2$, under any one of: $f$ Lipschitz with $0\le\Lambda h<2$; finite dimension with
  bounded iterates; convergence in infinite dimension; or a Hilbert space with $f$
  one-sided Lipschitz and $-2\le\mu h<2$ (Eqs. (3.4)–(3.8), (3.14)). The correction
  can be applied to any base scheme satisfying the condition (Remark 3.2).
- **Base case** (Lemma 4.1). The implicit midpoint error and all its centred
  differences $(D_+D_-)^mD$, $(D_+D_-)^m$, $m\le p$, are $\mathcal O(h^2)$.
- **All levels** (Thm. 4.1). For $y\in C^{2p+3}$ and $f\in C^{2p+2}$, every DC$2j$,
  $j=1,\dots,p+1$, has order $2j$ and satisfies the condition, by induction on $j$.
- **B-convergence** (Cor. 4.1). Under a one-sided Lipschitz condition in
  $\mathbb R^d$ the order-$2j$ bound holds with a constant independent of $\Lambda$,
  for $h<2/\mu$ ($\mu>0$) or all $h$ ($\mu\le0$); see
  [B-convergence](/definitions/b-convergence.md) for the statement and its caveats.

### Linear stability

On $y'=\lambda y$, $y(0)=1$, $z=h\lambda$, Lemma 5.2 proves by induction

$$y^{[2j+2]}_n=\Big(\frac{2+z}{2-z}\Big)^{n-j}P_j(n),\qquad n\ge j,$$

with $P_j$ a polynomial of degree $j$ in $n$ whose coefficients depend on $z$. Since
$\lvert(2+z)/(2-z)\rvert<1$ for $\operatorname{Re}z<0$, $y^{[2j+2]}_n\to0$, and every
DC$2j$ is A-stable (Thm. 5.1) in the asymptotic sense of their Def. 5.1,
$\lim_{n\to\infty}\lvert y_n\rvert=0$. That definition differs from the
stability-function definition used elsewhere in the bundle; the difference is set out
on [A-stability](/properties/a-stability.md).

### Numerical tests

Fixed steps in Scilab, against fixed-step BDF2, BDF4, BDF6, explicit RK4 and Scilab's
adaptive BDF and RKF45 solvers (§6):

- **Bernoulli** $y'=-0.1y-1000y^{20}$: accurate at large steps (DC10
  $1.3\times10^{-4}$ at $h=1$), but orders below design and RK4 more accurate than DC4
  in the asymptotic range (Table 6.1; see [B-convergence](/definitions/b-convergence.md)).
- **Long-time oscillatory** $y'=10\,y\cos t$ to $t=10^6$: each level shows its
  design order (DC10 ratio 10.1 between $h=5\times10^{-2}$ and $2.5\times10^{-2}$) down
  to an error floor of about $3\times10^{-6}$; at $h=1.56\times10^{-3}$ the BDF methods
  and the adaptive solvers have errors from $2.6\times10^3$ to $2.2\times10^4$ against
  $3.8\times10^{-4}$ for DC4 (Table 6.2).
- **Modified B5** (eigenvalues $-10\pm5000i$): exact design orders 2 to 10, but "BDF
  methods perform better for this problem" (BDF6 $2.3\times10^{-12}$ against DC6
  $1.36\times10^{-9}$ at $h=1.25\times10^{-6}$; Table 6.3).
- **E5:** DC beats fixed-step BDF (DC10 $4.51\times10^{-16}$ against BDF6
  $3.5\times10^{-11}$ in the first component at $h=10$); RK4 unstable for
  $h\ge2\times10^{-4}$ (Table 6.4).
- **[Robertson](/benchmarks/robertson-problem.md)** and
  **[Van der Pol](/benchmarks/van-der-pol-oscillator.md)** ($\mu=1000$): accurate at
  large steps on Robertson; on Van der Pol DC2 and DC4 fail to converge in the tested
  range while DC6 and DC8 reach orders of about 6 to 7.6 (Tables 6.5–6.6).

**Step-size heuristic** (§6.7). For eigenvalues $\lambda$ the authors state that
$h\max\{\operatorname{Re}\lambda,\lvert\operatorname{Im}\lambda\rvert\}<2$ suffices
"for a good accuracy", with faster convergence when $-\operatorname{Re}\lambda\gg\lvert\operatorname{Im}\lambda\rvert$,
while convergence at the design order needs $h\Lambda<2$. For eigenvalues in the left
half-plane the printed maximum reduces to $\lvert\operatorname{Im}\lambda\rvert$, which
matches their contrast between modified B5 and E5 *(compiler check, not in the
sources)*.

**Cost.** On the Bernoulli test DC10 reaches a maximum error of about
$1.1\times10^{-11}$ with about $5\times10^6$ nonlinear solves, DC2 about
$8.9\times10^{-7}$ with $5\times10^6$ steps. No CPU times are reported, because the
DC code is interpreted Scilab while the reference solvers are compiled (§6.7).

**Position against other correction methods** (§1, as stated by the authors, not
demonstrated in the paper). Spectral, integral and Runge–Kutta-based deferred
corrections (Dutt–Greengard–Rokhlin, Christlieb–Ong–Qiu, Hansen–Strain, Kushnir–Rokhlin)
are "linear perturbation[s] of a low order scheme" for which stiff problems are "a
challenge"; Kushnir–Rokhlin's solver needs small steps for moderately stiff problems
and drops to order 2 for very stiff ones; the iterated deferred correction of
Daniel–Pereyra–Schumaker is inaccurate at large steps and gains nothing asymptotically
from high correction levels.

## Spectral deferred correction as a preconditioned Picard iteration

The SDC literature writes the collocation problem on $\mathsf M$ quadrature nodes
$0<\tau_1<\dots<\tau_{\mathsf M}\le1$ of the step (page-local; $t_n$ itself is not a node)
as $\mathbf Y=y_n\mathbf 1+hQf(\mathbf Y)$, with $Q$ the collocation matrix of the registry,
i.e. the Butcher matrix $A$ of the underlying fully implicit Runge–Kutta method. A sweep
preconditions the Picard iteration by a cheap approximation $Q_\Delta$ of $Q$
([Saupe et al. 2025](/sources/saupe-2025.md), §2.1, Eq. (12);
[Čaklović et al. 2025](/sources/caklovic-2025.md), §2.1):

$$\mathbf Y^{(k+1)}-hQ_\Delta f\big(\mathbf Y^{(k+1)}\big)=y_n\mathbf 1+h\big(Q-Q_\Delta\big)f\big(\mathbf Y^{(k)}\big).$$

- $Q_\Delta=0$ is plain Picard iteration, which converges only for small steps or
  non-stiff problems (Saupe et al., §2.1). It is the bDeC update of this page, with the
  integration weights $\omega_{mr}$ in the role of $Q$ *(compiler remark, not in the sources)*.
- Lower-triangular $Q_\Delta$ from explicit or implicit Euler between nodes is classical
  SDC; the explicit-Euler version is sDeC (Micalizzi & Torlo 2024, App. A.1). The LU
  choice $Q_\Delta=U^\top$ with $LU=Q^\top$ (Weiser, as recalled by Saupe et al.) converges
  fast but does not guarantee one order per sweep. With $Q_\Delta$ lower triangular, SDC
  is an iterated implicit Runge–Kutta method of van der Houwen & Sommeijer, and
  $Q_\Delta=Q=A$ for a DIRK reproduces that DIRK, so an SDC code runs any DIRK or explicit
  method (Čaklović et al., §1, Remark 2.2).
- **Diagonal** $Q_\Delta$ decouples the node updates within a sweep, so they can run in
  parallel across the method; the coefficient choices (MIN-SR-NS, MIN-SR-S, MIN-SR-FLEX),
  their nilpotency theorems and stability are on
  [parallel SDC](/methods/parallel-sdc.md).

With a first-order preconditioner each sweep raises the order by one up to the
collocation order, provided the iteration converges; higher-order preconditioners can gain
more but lose it when the error is not smooth (Saupe et al., §2.1, citing Christlieb, Ong &
Qiu). For any diagonal $Q_\Delta$ the order after $K$ sweeps is $\min(K,p^*)$, $p^*$ the
collocation order, as Čaklović et al. (§3.1) recall from van der Houwen et al. This is the
same "one order per iteration up to the collocation order" as the bound $\min(\mathsf M+1,K)$
above. The collocation update $y_{n+1}=y_n+hb^\top f(\mathbf Y)$ raises the order of the
step but can destroy the apparent A-stability of some preconditioners, so Čaklović et al.
(Remark 2.1) use only nodes with $\tau_{\mathsf M}=1$, where the last node value is the
step value.

**Adaptive SDC.** Saupe et al. (2025, §2.2, Algorithms 1–2) select the step of SDC as for
an [embedded pair](/methods/embedded-runge-kutta-pair.md): with a fixed number of sweeps the
increment between the last two sweeps (orders $K$ and $K-1$) is the error estimate; or, the
sweeps run until the collocation residual is small and the error is estimated from the
collocation polynomial at one node against an interpolant through the others, which
chooses both $h$ and the iteration count. Adaptive SDC needs about 70 times fewer Newton
iterations than fixed-step SDC on the stiff [Van der Pol](/benchmarks/van-der-pol-oscillator.md)
oscillator, and at least one parallel adaptive variant beats the order-5 embedded
ESDIRK5(3) or ARK5(4) in measured wall-clock time on each of four problems, the pairs being
faster only on the Schrödinger problem at low accuracy (§4.2, Fig. 10). Earlier SDC step selection doubled or
halved the step from the increment (Dutt, Greengard & Rokhlin, as recalled, §1). The
controller and its tolerance behaviour are on [step-size control](/methods/step-size-control.md).

## Multirate spectral deferred correction (MRSDC)

Spectral deferred correction, as recalled by
[Loffeld et al. (2024)](/sources/loffeld-2024.md) (§2.2, after Dutt, Greengard &
Rokhlin), writes the step as a Picard integral over quadrature nodes (Gauss–Lobatto,
Gauss–Radau, Gauss–Legendre or Clenshaw–Curtis) and corrects the node values in sweeps
of forward or backward Euler; each sweep raises the order by one up to the order of the
quadrature, the same principle as the subnode form above. Semi-implicit variants
correct the stiff part implicitly and the nonstiff part explicitly, and multi-implicit
multirate SDC gives each process its own node set (§2.2, as recalled).

In the explicit multirate variant MRSDC used by Loffeld et al., the slow part
$f^{\{\mathrm s\}}$ (transport) lives on coarse Gauss–Lobatto nodes and the fast part
$f^{\{\mathrm f\}}$ (chemistry) on nested fine nodes, every coarse node being a fine node.
"MRSDC-XYZ" has $X$ coarse nodes and a $Y$-node quadrature applied $Z$ times in each
coarse subinterval, hence $X+(X-1)(Z-1)+(X-1)(Y-2)Z$ fine nodes. One forward-Euler
correction sweep from fine node $q$ to $q+1$ reads, with page-local symbols
($t_q$ fine nodes, $t_p$ the coarse node at or left of $t_q$, $h_q=t_{q+1}-t_q$,
superscript $(k)$ the sweep, $\mathcal I^{\mathrm f}_q$, $\mathcal I^{\mathrm s}_q$ the
quadratures of $f^{\{\mathrm f\}}$ and $f^{\{\mathrm s\}}$ over $[t_q,t_{q+1}]$ from the
previous sweep),

$$Y_{q+1}^{(k+1)}=Y_q^{(k+1)}+h_q\big(f^{\{\mathrm s\}}(Y_p^{(k+1)})-f^{\{\mathrm s\}}(Y_p^{(k)})\big)+h_q\big(f^{\{\mathrm f\}}(Y_q^{(k+1)})-f^{\{\mathrm f\}}(Y_q^{(k)})\big)+\mathcal I^{\mathrm f}_q+\mathcal I^{\mathrm s}_q$$

(Loffeld et al. (2024), §2.2, Eq. (4), time arguments dropped); evaluating the fast
difference at $t_{q+1}$ instead gives a backward-Euler correction. The study compares
fourth-order single-rate SDC (3 nodes, 4 sweeps), MRSDC-338 and MRSDC-352 (4 sweeps
each) with [multirate infinitesimal methods](/methods/multirate-infinitesimal-methods.md)
on a 3D methane flame with 53 species (§3.2, §5):

* **Non-monotonic convergence.** Despite their theoretical fourth order, MRSDC-338
  shows rates 2.72, 3.28, 2.51, 2.07, 1.69, 0.77, 0.08 and stagnates near
  $2\times10^{-6}$; MRSDC-352 shows 7.17, 4.02, 8.98, 1.24. The authors suggest that
  smaller steps or more sweeps could cure it (§5.2, Table 1, Fig. 3).
* **Stable steps.** Single-rate SDC is stable only for $H\le6.25\times10^{-8}$ s, set
  by the chemistry eigenvalues; MRSDC-338 at $2.0\times10^{-6}$ s and MRSDC-352 at
  $2.5\times10^{-7}$ s (Table 1).
* **Cost.** MRSDC beats single-rate SDC, confirming the earlier SMC results that the
  paper recalls (Fig. 4). The multirate infinitesimal methods are cheaper than MRSDC at
  most accuracies, because SDC sweeps several times over the step while a
  multirate infinitesimal step passes once: at $H=6.25\times10^{-8}$ s MRSDC-338 needs
  129 slow and 7,169 fast evaluations and 833 s, MRSDC-352 257, 2,049 and 376 s, the
  infinitesimal methods 97 slow evaluations and 173–274 s. At the smallest steps
  MRSDC-352 is comparable (§2.2, §5.2, Table 2, Fig. 4).

The authors contrast SDC's "ostensibly no upper bound" on order with the at most fourth
order of the multirate infinitesimal methods available to them (§2.2). The comparison
is one problem with constant steps and fixed sweep counts.

## Qualifications

- **Order of the collocation operator.** Han Veiga et al. state that $\mathcal L^2=0$ is of
  order $\mathsf M+1$, and they also say the order "depends on the used quadrature rule"
  (§2–3). For Gauss–Lobatto or Gauss–Legendre subnodes the underlying collocation method is
  of higher order ($2\mathsf M$ and $2\mathsf M+2$ respectively; see
  [fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md)). The bound
  $\min(\mathsf M+1,K)$ is therefore a lower bound for such nodes, not the sharp order
  *(compiler note)*. Micalizzi & Torlo (2024, §3.1) and Ciallella et al. (2022, §4.1)
  state the Gauss–Lobatto order $2\mathsf M$ explicitly and choose
  $\mathsf M=\lceil p/2\rceil$ accordingly, which confirms the note.
- **Robustness with equispaced nodes.** The explanation that DeC "does not require a mass
  matrix" is incomplete. DeC still uses the interpolation weights $\omega_{mr}$, which for
  equispaced nodes suffer the same negative-weight problem the paper reports *(compiler
  note, not in the sources)*.
- **Printed slips** (arXiv v3). The ODE is written $\alpha'+F(\alpha)=0$, but the DeC
  operators (eqs. (18)–(20)) carry $-hF$ (i.e. $\alpha'=+F$), and the stiff examples set the
  stiff term equal to the right-hand side. The spectral-difference DeC update (eq. (68))
  restarts from $u^{(k)}$ where the algorithm (23) restarts from $u(t_n)$, as in the formula
  above. Eq. (42) has $\mathcal L^2(\mathbf Y^{(k+1)})$ for $\mathcal L^2(\mathbf Y^{(k)})$.
- The claim that implicit ADER beats IMDeC rests on two plots without error tables.
- **DC$2j$: B-stability announced, B-convergence proved.** Koyaguerebo-Imé & Bourgault
  (2022, §1) announce that each DC scheme "is B-stable"; the body proves B-convergence
  (Cor. 4.1) and no contractivity result. The introduction also says the schemes
  "inherit the A-stable property of the trapezoidal rule", although the base scheme is
  the implicit midpoint rule; the two coincide only on linear problems, which is where
  the A-stability proof works.
- **DC$2j$: printed slips** (arXiv v4). Remark 3.1 calls the Deferred Correction
  Condition "equivalent" to Eqs. (3.2)–(3.3), but only one direction is argued, and its
  transform is printed without the index shifts that make it an identity; Remark 4.2
  prints the constant as $c_{2j+1}$ and refers to it as $c_{2j+3}$ in the next sentence.
- **Order loss of continuous-Galerkin DeC.** With Bernstein B3, B4 and equispaced
  Lagrange P3 elements, Abgrall's mass-matrix-free DeC reaches only second order on
  unsteady problems with the optimal iteration count; the formal order needs 10 (P3), 80
  (B3) or 320 (B4) iterations, a smaller CFL number does not help, and a higher-derivative
  stabilization lowers the error but not the order. Mass-lumpable Gauss–Lobatto Lagrange
  and cubature elements and steady problems are unaffected (Micalizzi & Torlo 2024,
  Remark 9.1; Supp. §3.2, Figs. S1–S3). The authors suspect that the Poincaré-like
  Assumption 3.8 of their own proof of the operator properties fails, so those proofs
  rest on an assumption the authors doubt for these elements.
- **Stage counts against measured speed-ups.** Measured speed-ups of the efficient
  variants exceed the stage ratios in some cases (bDeCdu, equispaced order 9: about 2
  against $65/37\approx1.76$) and fall short in others (order 3: about 1.0 against 1.25);
  Remark 5.1 (stage count is not cost) is the only explanation given. On PDEs the
  speed-ups depend on the code: the Fortran B2 runs gain more than the Python cubature
  runs (Micalizzi & Torlo 2024, §9).
- **SSP property.** Ciallella et al. (2022, §6.6) state that "arbitrary high order DeC
  cannot be recast as a convex combination of explicit Euler method", and conclude only
  that explicit DeC5 with the positivity limiter has no positivity proof under the
  forward-Euler limiter CFL; they give no proof and name no order from which the statement
  holds. Liu, Shu & Zhang (2008), whose title concerns the SSP property of deferred
  correction, is cited by Ciallella et al. (§4.1) only among the developments of DeC and by
  Micalizzi & Torlo (2024, §1, §3.1) only as the origin of bDeC and of the α-family; no
  ingested source reports which DeC methods, of which orders, Liu, Shu & Zhang find SSP. The
  bundle therefore holds no source-backed SSP claim for DeC and no contradiction; see
  [SSP methods](/methods/strong-stability-preserving-runge-kutta.md).
- **Printed slips** (Micalizzi & Torlo 2024, arXiv v4). Thm. 2.1 assumes $\alpha_1\ge0$
  but divides by it; $\alpha_1>0$ is meant, as Supp. Prop. 3.10 writes. The speed-up of
  §9.1.1 is defined as the ratio of bDeCdu to bDeC times, which is below one; the plotted
  values are the inverse. Zeifang & Schütz (2022, Eq. (9)) print the corrector's
  right-hand side without the quadrature term $I_l$ that their Eq. (6) contains.
- **MRSDC: printed slips** (arXiv v1 of Loffeld et al. 2024). Eq. (4) prints periods
  for commas in the arguments, and the text names the slow quadrature $S_C$ where the
  equation has $S_S$; Fig. 4 also plots an MRSDC-352 run with two sweeps that the text
  does not describe.

# Citations

- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §1; §3 (eqs. (18)–(23), Prop. 3.1, Remark 3.2); §4.3 (Thm. 4.5); §4.4 (eqs. (37)–(47)); §4.5.1 (DeC–residual distribution); §5.1 (Fig. 2); §5.2–5.3 (Figs. 3–14).
- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §1; §2 (Eqs. (2.4)–(2.14), Remarks 2.1–2.3, Table 2.1); §3 (Def. 3.1, Thm. 3.1, Remarks 3.1–3.2); §4 (Lemma 4.1, Thm. 4.1, Cor. 4.1, Remarks 4.1–4.2); §5 (Def. 5.1, Lemma 5.2, Thm. 5.1); §6 (Tables 6.1–6.6, §6.7).
- [Loffeld et al. (2024)](/sources/loffeld-2024.md) — §2.2 (Eq. (4), node count), §3.2, §5.2 (Tables 1–2, Figs. 3–4).
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — §1–2 (Thm. 2.1); §3.1–3.3 (Eqs. (8)–(20)); §4 (Eqs. (21)–(29)), §4.3; §5 (Tables 1–6, Remark 5.1); §6 (Thms. 6.1–6.2, Fig. 3); §7.2–7.3 (Remark 7.1, Eq. (59)); §8 (Eq. (60)); §9 (Figs. 4–13, Remark 9.1); Conclusions; App. A; Supp. Thm. 1.1, Props. 2.1–2.4, Remark 2.1, §3.
- [Torlo et al. (2022)](/sources/torlo-2022.md) — §2 (mPDeC), Thm. 4.7, Fig. 6a; §5 (Thm. 5.5, Prop. 5.6, Table 2); §6.
- [Ciallella et al. (2022)](/sources/ciallella-2022.md) — §4.1 (subnode orders), §4.3 (mPDeC), Remarks 4.4, 5.1, 5.5; §5.1; §6 (Figs. 5–16, Tables 1–2), §6.6.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §4 (comparison with mPDeC, Figs. 5, 14, 19–20, Table 6).
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) — §2 (Alg. 1, Eqs. (5)–(9), Remark 2); §4.3 (Figs. 7–8); §5.2 (Fig. 9).
- [Popov (2024)](/sources/popov-2024.md) — Introduction (DeC and ADER).
- [Saupe et al. (2025)](/sources/saupe-2025.md) — §1; §2.1 (Eq. (12)); §2.2 (Algorithms 1–2); §4.
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — §1, §2.1 (Remarks 2.1–2.2), §3.1, §3.2 (Fig. 5).
