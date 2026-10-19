---
type: Method
title: "Deferred correction (DeC)"
description: "Arbitrarily high-order integrators that correct a cheap low-order solution by high-order defect estimates: Abgrall's subnode form iterates a low-order operator against a collocation operator (order min(M+1, K)); the implicit-midpoint hierarchy DC2j corrects across grid points and is A-stable and B-convergent at every order."
status: established
aliases: [DeC, deferred correction method, Abgrall's DeC, explicit DeC, IMDeC, implicit deferred correction, DC2j, deferred correction for the implicit midpoint rule, difference correction]
tags: [deferred-correction, explicit, implicit, stiff, order-conditions, stability]
timestamp: 2026-10-19T20:00:00Z
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
Ong & Qiu).

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

**Convergence** (Abgrall's proposition, Prop. 3.1, as recalled by Han Veiga et al.). Let
$\mathcal L^1$ be coercive,
$\kappa_1\lVert\mathbf Y-\mathbf Z\rVert\le\lVert\mathcal L^1(\mathbf Y)-\mathcal L^1(\mathbf Z)\rVert$.
Let $\mathcal L^1-\mathcal L^2$ be Lipschitz with constant $\kappa_2h$. Let
$\mathcal L^2=0$ have a unique solution $\mathbf Y^*$ ($\kappa_1$, $\kappa_2$ page-local).
If $\kappa_2h/\kappa_1<1$, the iteration converges and
$\lVert\mathbf Y^{(k)}-\mathbf Y^*\rVert\le(\kappa_2h/\kappa_1)^k\lVert\mathbf Y^{(0)}-\mathbf Y^*\rVert$.
Each correction therefore gains one power of $h$, and $K$ corrections give order
$\min(\mathsf M+1,K)$ (see [equivalence of DeC and ADER](/results/dec-ader-equivalence.md),
Thm. 4.5). Han Veiga et al. take $K=\mathsf M+1$, "as many iterations as the desired order
of accuracy" (§3).

**Choices** (Remark 3.2). A higher-order $\mathcal L^1$ speeds up convergence of the
iteration but can lower the final accuracy, because the error loses smoothness (citing
Christlieb et al.). Gauss–Legendre subnodes exclude the endpoint and need an extrapolation
to $t_{n+1}$. For continuous finite elements, mass lumping in $\mathcal L^1$ avoids inverting
the global mass matrix while $\mathcal L^2$ keeps the consistent one. This is Abgrall's
motivation, and it makes residual-distribution schemes high order in time (§3, §4.5.1).

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

## Linear stability

For $y'=\lambda y$ the explicit DeC (orders 2 to 5) and explicit ADER have identical
stability regions, independent of the node family (equispaced, Gauss–Lobatto,
Gauss–Legendre), and the regions grow with the order (Han Veiga et al. 2021, §5.1, Fig. 2;
computed numerically). They call an analytic study "not feasible". Their reason is that it
"leads to solving polynomial inequalities of degree $p(p+1)$". The node independence has a
short explanation *(compiler check, not in the sources)*. Each correction raises the degree
in $z=h\lambda$ by one, so $R(z)$ is a polynomial of degree at most $K$. Order $K$ then
forces $R(z)=\sum_{j=0}^{K}z^j/j!$ for $K\le\mathsf M+1$, the Taylor polynomial. This is the
[stability polynomial](/definitions/stability-function.md) of every $K$-stage explicit
Runge–Kutta method of order $K\le4$.

## Accuracy observations

On the scalar test $y'=\lambda y$ ($\lambda=10$, $t\in[0,0.1]$), with orders up to 11, DeC
keeps its design order with equispaced nodes. ADER with equispaced nodes does not at the
highest orders. Han Veiga et al. attribute this to DeC not needing a mass matrix (§5.2.1),
and they note that equispaced quadrature weights turn negative from ninth order. On a
nonlinear scalar ODE, a linear three-species system, Lotka–Volterra (including $t\le100$
with $h=1$) and on spectral-difference semi-discretizations of linear advection and
Burgers (orders 3 to 9, $h=\frac{0.5}{\mathsf M+1}\frac{\Delta x}{\lvert v_{\max}\rvert}$),
DeC and ADER both reach their design orders (§5.2–5.3).

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

## Qualifications

- **Order of the collocation operator.** Han Veiga et al. state that $\mathcal L^2=0$ is of
  order $\mathsf M+1$, and they also say the order "depends on the used quadrature rule"
  (§2–3). For Gauss–Lobatto or Gauss–Legendre subnodes the underlying collocation method is
  of higher order ($2\mathsf M$ and $2\mathsf M+2$ respectively; see
  [fully implicit collocation methods](/methods/fully-implicit-runge-kutta.md)). The bound
  $\min(\mathsf M+1,K)$ is therefore a lower bound for such nodes, not the sharp order
  *(compiler note)*.
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

# Citations

- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §1; §3 (eqs. (18)–(23), Prop. 3.1, Remark 3.2); §4.3 (Thm. 4.5); §4.4 (eqs. (37)–(47)); §4.5.1 (DeC–residual distribution); §5.1 (Fig. 2); §5.2–5.3 (Figs. 3–14).
- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §1; §2 (Eqs. (2.4)–(2.14), Remarks 2.1–2.3, Table 2.1); §3 (Def. 3.1, Thm. 3.1, Remarks 3.1–3.2); §4 (Lemma 4.1, Thm. 4.1, Cor. 4.1, Remarks 4.1–4.2); §5 (Def. 5.1, Lemma 5.2, Thm. 5.1); §6 (Tables 6.1–6.6, §6.7).
