---
type: Source
title: "Hochbruck & Ostermann (2010) — Exponential integrators"
description: "Acta Numerica survey of exponential integrators for semilinear parabolic and highly oscillatory problems: stiff-order convergence theory in a semigroup framework for exponential quadrature, Runge–Kutta, Rosenbrock, multistep and general linear methods, Magnus and trigonometric integrators, evaluation of φ-function actions, software and history."
resource: "doi:10.1017/S0962492910000048"
source_kind: paper
authors: [Hochbruck M., Ostermann A.]
year: 2010
venue: "Acta Numer. 19:209-286"
local_file: "/home/stefano/papers/mosaic/ode-integration/2010_Crossref_Acta_Numerica_Hochbruck_Exponential_integrators.pdf"
tags: [exponential, stiff, order-conditions, order-reduction, review]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

The survey treats two classes of [stiff](/definitions/stiffness.md)
problems: semilinear parabolic problems $y'=Ly+N(t,y)$ with $L$ the
generator of an analytic semigroup (the [heat equation](/benchmarks/heat-equation.md)
is the model, Ex. 2.1), and highly oscillatory problems with large imaginary
eigenvalues. [Exponential integrators](/methods/exponential-integrators.md)
integrate a linear prototype exactly and treat the remainder through the
variation-of-constants formula, which brings in $e^{hL}$ and the
$\phi_k$ functions. Every order statement is a **stiff order**: an error
bound $Ch^p$ with $C$ independent of the stiffness and of $h$
([order reduction](/definitions/order-reduction.md)).

For parabolic problems the paper proves or quotes convergence theorems for
exponential quadrature rules, exponential Euler (stiff order 1), explicit
exponential Runge–Kutta methods under the
[stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md)
of its Table 2.2 to order 4, exponential Rosenbrock methods (Table 2.3),
exponential Adams methods that reduce to Adams methods at $L=0$
([linear multistep methods](/methods/linear-multistep-method.md)), a
linearized exponential two-step method, exponential general linear methods
and Magnus integrators. Against these conditions the Cox–Matthews ETDRK4
reduces in the worst case to order 2 and the Krogstad and Strehmel–Weiner
four-stage schemes to order 3; a five-stage fourth-order method is given.
[Lawson methods](/methods/lawson-methods.md) and their generalization with
past values are written as exponential general linear methods. Exponential
Rosenbrock methods linearize at every step; the paper places their origin
beside the rational approximations behind
[Rosenbrock methods](/methods/rosenbrock-wanner-method.md).

For oscillatory problems the paper gives frequency-independent bounds for the
exponential midpoint (Magnus) rule and for filtered trigonometric
(Gautschi-type) methods, and reviews adiabatic, impulse and multiple
time-stepping methods. §4 surveys the [evaluation of φ-function actions](/methods/phi-function-evaluation.md)
(Chebyshev, Krylov, Leja, contour integrals) and software; §5 surveys
applications, including the [nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md);
§6 gives the history. Splitting methods are named as competitors but not
discussed ([operator splitting](/methods/operator-splitting.md)). The paper
has no numerical experiments.

# Version read

Version of record (Cambridge University Press), pp. 209–286, 78 pages, all
read; the text layer was used, and the pages with tableaux and key formulas
(pp. 226–229, 233–235, 243, 252, 255–257, 265–268) were read visually.
Page 1 matches Crossref (title, authors, volume, pages, DOI). Numbering cited
here is that of the journal.

# Key claims

1. A differential equation is stiff "whenever the implicit Euler method works (tremendously) better than the explicit Euler method"; for highly oscillatory problems implicit Euler also performs poorly because it "tends to resolve all the oscillations" (§1, p. 210). **Stated**
2. "Whenever we speak about the order of convergence in this article, we refer to the so-called stiff order": a global error bound $Ch^p$ on finite intervals with $C$ depending on the interval and the problem class "but neither on the stiffness nor on the step size $h$"; the classical order "is always an upper bound to the stiff order" (§1, p. 212). **Stated** (definition)
3. If $L$ generates a $C_0$ semigroup with $\lVert e^{tL}\rVert\le Ce^{\omega t}$ (Assumption 2.2), the operators $\phi_k(hL)$, $k\ge1$, are bounded (Lemma 2.4). **Proved**
4. An exponential quadrature rule with uniformly bounded weights and $\psi_j(hL)=0$, $j=1,\dots,p$, with $\psi_j(hL)=\phi_j(hL)-\sum_ib_i(hL)c_i^{j-1}/(j-1)!$ (Eq. 2.17), converges with order $p$ for $y'=Ly+N(t)$ on any step sequence (Thm 2.7); the collocation rule has order $s$ (Cor. 2.8). **Proved**
5. Exponential Euler has stiff order 1 under Assumptions 2.9–2.10 (analytic semigroup, $N$ locally Lipschitz from $D((-L)^\alpha)$) (Thm 2.14). **Proved**
6. For explicit exponential Runge–Kutta methods "it is not possible to achieve $\psi_{2,i}=0$ for all $i$": the internal stages have order one only (§2.3, p. 226). **Stated**
7. Thm 2.17 (from Hochbruck & Ostermann 2005a): an explicit exponential Runge–Kutta method satisfying the Table 2.2 conditions up to order $p-1$, $\psi_p(0)=0$ and the remaining order-$p$ conditions with $b_i(0)$ in place of $b_i(hL)$, $2\le p\le4$, has error $\le Ch^p$. Table 2.2 lists 9 conditions to order 4, including $\psi_1=0$ and the stage condition $\psi_{1,i}=0$. **Stated** (proof referred to 2005a)
8. Cox–Matthews ETDRK4 satisfies conditions 1–4, weakened 5, 6 and 9 and very weak 7, 8: "In the worst case, this leads to an order reduction to order two only"; Krogstad's scheme and the Strehmel–Weiner scheme reduce in the worst case to order 3 (Ex. 2.19, p. 228). **Derived** (no numerics)
9. The coefficients of these four-stage methods cannot be modified to reach order four for semilinear parabolic problems (answered "in the negative" by Hochbruck & Ostermann 2005a); the five-stage method of p. 229 with $c=(0,\tfrac12,\tfrac12,1,\tfrac12)$ has order four under Thm 2.17. **Stated**
10. The two-stage second-order families (2.39) and the $\phi_2$-free (2.40) are "B-consistent of order one" according to Strehmel & Weiner (1992), the Strehmel–Weiner scheme (2.43) of order two (Exs. 2.18–2.19; [B-convergence](/definitions/b-convergence.md)). **Stated**
11. Exponential Rosenbrock methods $Y_i=e^{c_ihJ_n}y_n+h\sum_ja_{ij}(hJ_n)N_n(Y_j)$ with $N_n(y)=f(y)-J_ny$ (Eq. 2.46) preserve equilibria, have simple stiff order conditions (Table 2.3: $\sum_ib_i=\phi_1$, $\sum_ja_{ij}=c_i\phi_1(c_i\cdot)$, $\sum_{i\ge2}b_ic_i^2=2\phi_3$, $\sum_{i\ge2}b_ic_i^3=6\phi_4$ for orders 1–4) and can be written so that each stage is a perturbed exponential Rosenbrock–Euler step (Eq. 2.48) (§2.4). **Stated**
12. Thm 2.22: under only a $C_0$ semigroup and a step-size condition (2.57), an exponential Rosenbrock method satisfying Table 2.3 to order $p$, $2\le p\le4$, has error $\le C\sum_jh_j^{p+1}$; proved for exponential Rosenbrock–Euler, which is second order (pp. 232–234). **Proved** ($p=2$), **Stated** ($p=3,4$)
13. Third-order exponential Rosenbrock methods need $\phi_3$ and fourth-order ones $\phi_3$ and $\phi_4$; methods using only $\phi_1$, including exp4 (classical order 4), "cannot have order larger than two" (pp. 235–236, Ex. 2.25). exprb32 and exprb43 are printed with embedded estimators. **Derived**
14. The $k$-step exponential Adams method has order $k$ (Thm 2.27, proved for $k=2$); the linearized exponential two-step method (2.72) has order 3 (Thm 2.29) and "better convergence properties" than Tokman's (2006) method, with which it coincides for $J_n=0$. **Proved**/**Stated**
15. Thm 2.31 (Ostermann, Thalhammer & Wright 2006): exponential general linear methods with stage and quadrature conditions to order $p-1$ and the order-$p$ quadrature condition only at $z=0$ (Eq. 2.78) converge with order $p$ up to a term $Ch^{p-\alpha+\beta}$. **Stated**
16. Lawson's method with Runge's method is "first-order accurate by Theorem 2.17"; the generalized Lawson method with one past value and Runge's method is second order; Krogstad's generalized Lawson scheme with two past values and classical RK4 has order 3 by Thm 2.31 (Exs. 2.32–2.34). **Derived**
17. The exponential midpoint rule for $\psi'=A(t)\psi$ with skew-Hermitian $A$ has error $\le Ch$ with $C$ independent of $\lVert A\rVert$, and $\le Ch^2t_n\max\lVert D\psi\rVert$ for $A=-i(D^2+V(t))$ under a commutator bound (Thms 3.4, 3.9); $p$-th order Magnus integrators satisfy the analogous bound with $D^{p-1}$ (Thm 3.10). **Proved** (3.4, 3.9), **Stated** (3.10)
18. Thm 3.15 (Grimm & Hochbruck 2006): filtered trigonometric one-step methods for $q''=-\Omega^2q+g(q)$ with finite energy have position error $\le Ch^2$ and momentum error $\le\tilde Ch$, constants independent of $\lVert\Omega\rVert$; Gautschi's and Deuflhard's methods "do not use an inner filter $\phi$, and thus suffer from resonances" (Ex. 3.14). **Proved** (sketch)
19. Symmetric trigonometric one-step methods are symplectic iff $\psi(\xi)=\operatorname{sinc}(\xi)\phi(\xi)$; the near-energy-conservation condition $\psi=\operatorname{sinc}^2\phi$ of Hairer & Lubich (2000) "cannot be satisfied by a symplectic method" (Remark 3.18). **Stated**
20. Krylov approximation of $e^{hL}v$ converges superlinearly once $m\ge\sqrt{\rho h}$ for Hermitian negative semidefinite $L$ with spectrum in $[-\rho,0]$, and once $m\ge\rho h$ for skew-Hermitian $L$ (Thms 4.4–4.5, after Hochbruck & Lubich 1997); "is always superlinear" (p. 267). **Stated**
21. Chebyshev error bounds (Thm 4.1, Stewart & Leyk; Thm 4.3, Lubich), Leja interpolation in Newton form (Eq. 4.6), contour-integral Laplace inversion (Thm 4.6) and the software exp4, EXPINT, Expokit, SPARSKIT and phipm are surveyed; "Most of the mathematical software for exponential integrators is still in its infancy" (§4). **Stated**
22. History: exponential integrators "were first considered by Hersch (1958)"; Certaine (1960) exponential multistep; Pope (1963) exponential Rosenbrock–Euler; Lawson (1967) and Ehle & Lawson (1975) the first exponential Runge–Kutta methods; Friedli (1978) the first with more φ-functions; "The term 'exponential integrators' was coined in the seminal paper by Hochbruck, Lubich and Selhofer (1998)" (§6). **Stated**

# Printed slips

- p. 268: "The situation in Theorem 4.4 corresponds to $\theta=0$, while Theorem 4.4 treats the case $\theta=\pi/2$"; the second reference denotes the skew-Hermitian case, Theorem 4.5. The wedge exponent $\alpha=\frac\pi2\frac1{\pi-\theta}$ gives $\tfrac12$ at $\theta=0$ and $1$ at $\theta=\pi/2$ *(compiler check, not in the sources)*.
- p. 254: $I(\Lambda)_{jk}=\int_{-h/2}^{h/2}e^{-\frac i\varepsilon\tau(\lambda_j-\lambda_k)}d\tau=\operatorname{sinc}\big(\frac h{2\varepsilon}(\lambda_j-\lambda_k)\big)$; the integral equals $h$ times the sinc, and the factor $1/h$ of (3.33) gives the printed right side *(compiler check, not in the sources)*.
- p. 215 (Ex. 2.1): the Neumann domain prints $v_x(0)=v_x(1)=0$ on $\Omega=(0,\pi)$.
- p. 236: the backward differences are defined by "$\nabla^{j+1}G_n=\nabla^jG_n-\nabla^jG_{n-1}$, $j=1,2,\dots$", with $\nabla^0G_n=G_n$.
- p. 267: "$e_m$ denotes the $m$th unit vector in $\mathbb C^d$" where the formulas use unit vectors of $\mathbb C^m$.
- p. 230: "an explicit exponential Runge–Kutta scheme (2.35)" refers to the method (2.20); (2.35) is the defect expansion.
- pp. 214–215: the solution is written $U(x,t)$ while the problem uses $U(t,x)$; pp. 243, 254 print $e^{-h/2A}$ for $e^{-(h/2)A}$.

# Notation map

| Hochbruck & Ostermann (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u'+Au=g(t,u)$ | $y'=Ly+N(t,y)$ | **$L=-A$**: the source's functions of $-hA$ are functions of $hL$; **$A$ collides with the Butcher matrix**; $N$ page-local, as on the exponential-integrators page |
| $u_n$, $U_{ni}$, $G_{ni}$ | $y_n$, $Y_i$, $N(t_n+c_ih,Y_i)$ | |
| $h$, $h_n$ | $h$, $h_n$ | agrees |
| $\varphi_k$, $\varphi_{j,k}=\varphi_j(-c_khA)$ | $\phi_k$, $\phi_j(c_khL)$ | same $1/(k-1)!$ normalisation |
| $\chi$, $\chi_i$ | — | coefficient of $y_n$ in update and stages, $e^z$ and $e^{c_iz}$ in the main case |
| $a_{ij}(z)$, $b_i(z)$, $c_i$ | $a_{ij}(z)$, $b_i(z)$, $c_i$ | operator-valued coefficients |
| $\psi_j$, $\psi_{j,i}$ | — | quadrature and stage defects; **opposite sign** to Luan (2021), stage sum from $k=1$ |
| $J$, $K$ in Table 2.2 | — | arbitrary bounded operators; **not the Jacobian** |
| $F$, $J_n=DF(u_n)$, $g_n$, $D_{ni}$, $v_n$ | $f$, $J_n$, $N_n$, $D_i$, $V_n$ (page-local) | exponential Rosenbrock: $N_n(y)=f(y)-J_ny$, $D_i=N_n(Y_i)-N_n(y_n)$, $V_n=\partial_tf(t_n,y_n)$; functions of $+hJ_n$ |
| $X$, $V=D(A^\alpha)$ | $X$, $V$ (page-local) | Banach space and fractional-power domain |
| $\gamma_j(z)$, $\nabla^jG_n$ | same (page-local) | exponential Adams weights and backward differences; **$\gamma$ collides** with registry uses |
| $v_\ell(z)$, $w_{i\ell}(z)$ | same (page-local) | past-value weights of exponential general linear methods |
| stiff order $p$ | $p$ | the paper's "order" throughout |
| stage order $q$, quadrature order $p$ | $q$, $p$ | for exponential general linear methods (§2.7) |
| $A(t)$, $\psi$, $\Omega_n$ (§3.1) | — | skew-Hermitian generator, wave function, Magnus logarithm; **sign convention $\psi'=A\psi$ without the minus** |
| $q$, $p$, $\Omega$ (§3.2) | $q$, $v$, $W$ (page-local) | positions, momenta, frequency matrix; **$p$ and $q$ collide with order and stage order** |
| $\phi,\psi,\psi_0,\psi_1$ (§3.2) | $\varpi$, $\sigma$ for $\phi$, $\psi$ (page-local) | filter functions; **$\phi$ collides with the φ-functions** |
| $\varepsilon$ | $\varepsilon$ | singular-perturbation parameter |

# Reference list

The paper prints 151 references in author–year style, alphabetical, with
same-author same-year items labelled a, b, c. The list is merged complete
into the [bibliography](/bibliography.md), with `citedby` this slug;
same-author same-year items take suffixes in printed order (e.g.
Hochbruck et al. 2009a/b/c, Hochbruck & Lubich 1999a/b/c). Pre-publication
items are kept as printed (Knizhnerman & Simoncini 2009 "In press";
Minchev & Wright 2005 preprint; Niesen & Wright 2009 arXiv:0907.4631v1; two
technical reports of 2009). Deuflhard et al. (1999) is an edited volume of
which two items are chapters. Friedli (1978) prints the editor "R.
Burlirsch". No DOIs are printed; no printed duplicates; all items parsed.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [B-convergence](/definitions/b-convergence.md)
* [Evaluating φ-functions: Leja interpolation, Krylov and related methods](/methods/phi-function-evaluation.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [Lawson (integrating-factor) methods](/methods/lawson-methods.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Multirate exponential Runge–Kutta and Rosenbrock methods (MERK, MERB)](/methods/multirate-exponential-methods.md)
* [Nonlinear Schrödinger equation](/benchmarks/nonlinear-schrodinger-equation.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Order reduction](/definitions/order-reduction.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Stiff order conditions of exponential Runge–Kutta methods and φ-order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md)
* [Stiffness](/definitions/stiffness.md)
