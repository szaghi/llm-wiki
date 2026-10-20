---
type: Method
title: "Linearly implicit multistep methods (Limm, Limm-W)"
description: "Glandon, Narayanamurthi and Sandu's linearly implicit multistep methods add a Jacobian term to a linear multistep method so that each step costs one linear solve: definition and coefficient count, W- and exact-Jacobian order conditions via Taylor and B-series, linear stability, stiff convergence, optimized methods of orders 1 to 5 and a variable-step variable-order implementation."
status: established
aliases: [Limm, Limm-W, Limm-w, linearly implicit multistep method, Rosenbrock multistep method, multistep W-method]
tags: [linear-multistep, implicit, stiff, order-conditions, stability, step-size-control]
timestamp: 2026-10-20T16:00:00Z
---

# Linearly implicit multistep methods (Limm, Limm-W)

**Linearly implicit multistep methods** are to [linear multistep methods](/methods/linear-multistep-method.md)
what [Rosenbrock methods](/methods/rosenbrock-wanner-method.md) are to implicit Runge–Kutta
methods ([Glandon et al. (2022)](/sources/glandon-2022.md), §1–2, Def. 2.2). A $k$-step **Limm**
method for autonomous $y'=f(y)$ is

$$\sum_{j=0}^k\alpha_jy_{n+j}=h\sum_{j=0}^{k-1}\beta_jf(y_{n+j})+hJ\Big(\sum_{j=0}^k\kappa_jy_{n+j}+h\sum_{j=0}^{k-1}\xi_jf(y_{n+j})\Big),\qquad\alpha_k=1,$$

with $J$ the Jacobian at the last known value $y_{n+k-1}$. The coefficients $\kappa_j$ and
$\xi_j$ are page-local and are the source's $\mu_i$ and $\nu_i$, whose letters clash with the
registry. The equation is written here in the registry orientation; Glandon et al. index
backwards from the new point. In a **Limm-W** method $J$ is replaced by an arbitrary matrix,
chosen for stability "without impacting the order of accuracy", as in Rosenbrock-W methods.

The method never evaluates $f$ at the new point ($\beta_k=0$). Each step therefore solves exactly
one linear system,

$$(I-h\kappa_kJ)\,z=\text{known data},\qquad y_{n+k}=z-\text{known data}$$

(implementation form, p. 3). $\kappa_k$ plays the role of the Rosenbrock $\gamma$. Compared
with a $k$-step method of the classical form, which has $2k+1$ free coefficients, Limm has
$4k+1$ at the same storage of $k$ past values and $k$ past right-hand sides (§2). The authors
reject two alternatives:

- linearizing an implicit multistep method about $y_{n+k-1}$ (their Eq. (2.2)), which keeps the
  number of free coefficients and, they argue, degrades accuracy and stability;
- a variant with past Jacobian–vector products (Eq. (2.3)), which needs extra storage.

**Example.** The one-step Limm-W method with $\alpha=(-1,1)$, $\beta_0=1$, $\kappa=(-1,1)$ is
$y_{n+1}-y_n=hf(y_n)+hW(y_{n+1}-y_n)$, with $W$ the arbitrary matrix (page-local). This is the
linearly implicit Euler method (Table 6.2a).

## Order conditions

Let $\theta_j=(t_{n+j}-t_{n+k-1})/h$ (page-local) be the step fractions, with $\theta_j=j-k+1$ on
uniform grids. On variable grids they depend on the step ratios, and so do all coefficients.

**Limm-W** (Thm. 3.3, proved by Taylor expansion). Order $p$ holds iff

$$\sum_j\alpha_j=0,\quad\sum_j\kappa_j=0,\quad\sum_j\alpha_j\theta_j^{\ell}=\ell\sum_j\beta_j\theta_j^{\ell-1}\ (\ell=1,\dots,p),\quad\sum_j\kappa_j\theta_j^{\ell-1}+(\ell-1)\sum_j\xi_j\theta_j^{\ell-2}=0\ (\ell=2,\dots,p).$$

These are $2p+1$ conditions *(translated by the compiler from Eq. (3.3))*. The pair
$(\alpha,\beta)$ is itself an explicit $k$-step method of order $p$, and the $J$-terms
contribute only $O(h^{p+1})$ (Remark 3.5).

**Limm with the exact Jacobian** (Thm. 3.7). The authors derive the conditions with
[B-series](/definitions/b-series.md) over the rooted trees plus a "fat" node standing for $Jy$.
The result is $2p$ conditions. They coincide with the Limm-W conditions except at order two,
where the two separate order-2 conditions are replaced by one linear combination of them
(Eq. (3.17d), Remark 3.8). The conditions depend only on the number of vertices of a tree, not
on its shape (§3.2). This mirrors the relation between Rosenbrock and W-methods: the exact
Jacobian saves conditions.

**Stiff case** (Remark 3.4). If $hJ$ does not tend to zero, the local error of Limm-W is
dominated by the $J$-residual, which is only $O(h^p)$. Imposing the last $\kappa$/$\xi$ condition
up to order $p+1$ restores $O(h^{p+1})$. This is the multistep analogue of stiff order loss for
W-methods; see [order reduction](/definitions/order-reduction.md).

## Linear stability

For $y'=\lambda y$ and $z=h\lambda$ the characteristic equation is

$$\varrho(\zeta)-z\sum_j(\beta_j+\kappa_j)\zeta^j-z^2\sum_j\xi_j\zeta^j=0$$

(Eqs. (4.1)–(4.2)). The boundary locus is $z=\varrho/\sum_j(\beta_j+\kappa_j)\zeta^j$ when all
$\xi_j=0$, and otherwise a quadratic-root formula (Eq. (4.4)).

**Variable steps.** For $\xi_j=0$ one step is multiplication by a $k\times k$ companion matrix
that depends on the recent step ratios (Eq. (4.5)). At $z=0$ it reduces to multistep
zero-stability. The optimized methods have $\alpha_j$ independent of the step ratios, so they
are zero-stable on any grid (§4.1). Two further results, which concern different methods:

- **Two-step Limm, $z\to-\infty$.** The matrix has spectral radius at most 1 iff the step ratio
  is at least $1/3$. By computer algebra the same holds for every real $z<0$ (§4.1).
- **Two-step Limm-W.** A weighted 1-norm of the matrix is at most 1 for all real $z<0$ and all
  ratios in about $[0.1,1.57]$ (Remark 5.6); the bounds are computed.

See [zero-stability](/definitions/zero-stability.md).

## Convergence on stiff problems

**Theorem 5.8.** Take an order-$p$ Limm-W method with $\xi_j=0$, applied to a problem whose
stiffness is linear. Locally $f(y)=J_*y+r(y)$ (page-local), with $J_*$ diagonalizable with
eigenvalues of negative real part carrying all the stiffness, and $r$ with a moderate Lipschitz
constant. Assume further:

- the fixed-step scheme is A($\alpha$)-stable and strictly stable at $0$ and at $\infty$;
- $\kappa_k>0$ for all admissible ratios;
- every $h_i\lambda$ lies in the stability region;
- products of the variable-step stability matrices are uniformly bounded.

Then the global error is $O(h_{\max}^p)$ for all steps below a bound independent of the
stiffness. The proof rewrites the method as an
[IMEX multistep method](/methods/imex-linear-multistep-methods.md) for $f=(f-Jy)+Jy$ (Eq. (5.1)).
The theorem also holds in the nonstiff case (Remark 5.9). By an informal argument, a Limm with
$\xi_j=0$ that is strictly stable at infinity is of order $p$ in both components of
semi-explicit index-1 DAEs (Remark 5.10; see
[differential-algebraic equations](/definitions/differential-algebraic-equation.md)).

## Optimized methods

The authors design methods of orders $k=1,\dots,5$ with $k$ steps and $\xi_j=0$, leaving $3k+1$
free coefficients (§6). Their design choices:

- $\beta_0+\kappa_0=0$, so that the roots $\zeta(z)\to0$ as $z\to-\infty$ (damping at infinity);
- zero-stability as a nonlinear constraint;
- a multiobjective genetic algorithm in MATLAB that maximizes the A($\alpha$) angle and minimizes
  the residuals of the order-$(p+1)$ conditions;
- free parameters rationalized for exact coefficients.

Orders 1 and 2 are A-stable; orders 3–5 are A($\alpha$)-stable (Fig. 6.1, Table 6.1):

| $k$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| A($\alpha$) angle, BDF | $90^\circ$ | $90^\circ$ | $86.03^\circ$ | $73.35^\circ$ | $51.84^\circ$ |
| A($\alpha$) angle, Limm | $90^\circ$ | $90^\circ$ | $87.78^\circ$ | $78.07^\circ$ | $73.00^\circ$ |
| A($\alpha$) angle, Limm-W | $90^\circ$ | $90^\circ$ | $87.39^\circ$ | $77.91^\circ$ | $70.32^\circ$ |
| error constant, BDF | 0.5 | 0.333 | 0.25 | 0.2 | 0.167 |
| error constant, Limm | 0.5 | 0.222 | 0.167 | 0.205 | 0.217 |
| error constant, Limm-W | 0.5 | 0.425 | 0.403 | 0.381 | 0.365 |

The two-step Limm-W method, with all fractions over $D=133414177$ (page-local), has
$\alpha=(13204873,\,-146619050,\,D)/D$, $\beta=(-73309525,\,193518829)/D$ and
$\kappa=73309525\,(1,-2,1)/D$, listed for $j=0,1,2$ (Table 6.2b, in registry order). It
satisfies the order-2 conditions and $\beta_0+\kappa_0=0$ *(compiler check, exact rational arithmetic)*. The exact-Jacobian
Limm coefficients are only in the supplement, which the ingested file does not contain.

## Variable-step variable-order implementation

The implementation is a branch of the MATLAB package MATLODE (§7):

- **Error estimate** (Def. 7.1). The local error is estimated from the divided difference of
  order $k+1$ times an error constant built from the order-$(k+1)$ residuals. This needs one more
  past value than the method, and it may slightly overestimate.
- **Step and order.** The optimal step follows from $h_{\mathrm{opt}}=h_n\lVert e\rVert^{-1/(k+1)}$,
  with $e$ (page-local) the estimate, and orders $k-1$, $k$, $k+1$ are compared (Eq. (7.1), after
  Hairer–Nørsett–Wanner).
- **Step growth.** Steps grow only after $k$ successful steps at the current size, because
  explicit ratio bounds are not available for general multistep methods (Remark 7.3).
- **History and start.** Past values are stored as divided differences and updated
  recursively, much like Nordsieck vectors (Eqs. (7.6)–(7.8)). The method starts itself at order
  one (Remark 7.2).

See [step-size control](/methods/step-size-control.md).

## Numerical results

All runs are in MATLAB 2019a on a dual Xeon E5-2650 v3 node, with relative and absolute
tolerance equal (§8).

- **Lorenz-96** ($N=40$ variables, forcing $8+4\cos(3\pi t)$, $t\in[0,0.5]$, fixed steps). The
  observed slopes are 0.99, 1.95, 2.98, 3.97 and 4.93 for Limm and 0.99, 2.01, 3.13, 4.02 and
  5.00 for Limm-W. Limm-W has slightly smaller errors (§8.1, Fig. 8.1).
- **Gray–Scott** ($2\times128^2$ unknowns, direct LU). The five multistep integrators (Limm,
  Limm-W, in-house BDF, ode15s BDF and NDF) reach similar errors with similar step counts.
  SDIRK4a and RODAS4 need fewer steps, and ode15s is fastest in CPU time. Limm shows a "small
  performance advantage" over the in-house [BDF](/methods/backward-differentiation-formula.md)
  (§8.2, Fig. 8.2).
- **1.5-layer quasi-geostrophic model** ($127^2$ grid, GMRES with tolerance one tenth of the
  integrator's). Limm keeps its CPU advantage over BDF and matches or beats RODAS4 and SDIRK4a at
  similar errors; ode15s does poorly. The error–step curves are jagged at loose tolerances, which
  the authors attribute "possibly" to inexact GMRES solves (§8.3, Fig. 8.3; see
  [implicit stage solvers](/methods/implicit-stage-solvers.md)).

## Qualifications

- **Error constants are normalized differently.** The BDF row of Table 6.1 is $1/(k+1)$, the
  constant divided by $\sigma(1)$. The Limm rows are not divided by it (Eq. (7.3)). The abstract's
  "error constants comparable to BDF" holds for Limm but not for Limm-W, whose constants exceed
  BDF's for every $k\ge2$.
- **Damping at infinity is not L-stability.** The authors call $\beta_0+\kappa_0=0$ "a condition
  for L-stability" (§6). Orders 3–5 are only A($\alpha$)-stable, so the property obtained is
  damping at infinity.
- **Stiff order.** Remark 3.4 (generic matrix, local error) and Theorem 5.8 (stiffness confined
  to $J_*$, global error) concern different settings. The relation between them is not discussed.
  The optimized methods impose the $J$-conditions only to order $p$.
- **Performance evidence.** The performance claim, "outperforms a comparable BDF implementation
  for nonlinear problems" (§9), rests on two problems and an in-house BDF baseline.
- **Version read.** The ingested file is the review manuscript (unresolved references to the
  supplement). Its numbering may differ from the SIAM article. Several printed slips are recorded
  on the Source page: the solve-matrix factor in Eqs. (3.6)–(3.7) lacks the diagonal coefficient,
  and an upper summation limit in Eq. (3.17b) is $k$.

# Citations

- [Glandon et al. (2022)](/sources/glandon-2022.md) — §1–2 (Eqs. (2.2)–(2.4), Def. 2.2), §3 (Assumption 3.1, Thms. 3.3, 3.7, Remarks 3.4–3.8), §4 (Eqs. (4.1)–(4.5)), §4.1, §5 (Assumptions 5.1–5.5, Eq. (5.1), Thm. 5.8, Remarks 5.6–5.10), §6 (Eqs. (6.1)–(6.4), Tables 6.1–6.2, Fig. 6.1), §7 (Eqs. (7.1)–(7.8), Def. 7.1, Remarks 7.2–7.3), §8 (Figs. 8.1–8.3), §9.
