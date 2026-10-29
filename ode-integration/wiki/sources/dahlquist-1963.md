---
type: Source
title: "Dahlquist (1963) — A special stability problem for linear multistep methods"
description: "Introduces A-stability for linear multistep methods, proves that no explicit method is A-stable and that an A-stable method has order at most 2 with error constant at least 1/12, attained only by the trapezoidal rule, and bounds the global error of the trapezoidal rule on nonlinear problems through a Lyapunov-norm condition."
resource: "doi:10.1007/BF01963532"
source_kind: paper
authors: [Dahlquist G.G.]
year: 1963
venue: "BIT 3(1):27-43"
local_file: "/home/stefano/papers/mosaic/ode-integration/1963_Crossref_BIT_Dahlquist_A_special_stability_problem_for_linear_multistep_methods.pdf"
tags: [linear-multistep, stability, stiff, implicit, b-convergence]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

The paper introduces the term **A-stability** for a
[linear multistep method](/methods/linear-multistep-method.md): all
solutions of the difference equation tend to zero as $n\to\infty$ when the
method is applied with any fixed $h>0$ to $y'=\lambda y$,
$\operatorname{Re}\lambda<0$. The motivation is long-time integration of
a forced linear system $y'=Ly+u(t)$ ($u$ page-local) when some eigenvalues of
$L$ have large modulus and negative real part (the paper does not use the word "stiff"; see
[stiffness](/definitions/stiffness.md)): once the transient has died out, the step should
be dictated by the slowly varying particular solution alone. The paper
calls A-stability "an extreme formulation" of that wish.

Section 2 proves that a method is A-stable iff $\varrho(\zeta)/\sigma(\zeta)$
is regular with non-negative real part for $\lvert\zeta\rvert>1$
(Lemma 2.1), that no explicit method is A-stable (Thm. 2.1), and the main
result, [Dahlquist's order barrier for A-stable multistep methods](/results/dahlquist-second-barrier.md)
(Thm. 2.2): the order of an A-stable linear multistep method cannot exceed
2, and the smallest error constant, $c^*=\frac1{12}$, belongs to the
trapezoidal rule, the only method with $p=2$ and $c^*=\frac1{12}$. The
proof maps $\lvert\zeta\rvert>1$ onto a half-plane and uses a variant of the
Riesz–Herglotz representation suggested by P. D. Lax. The section also
shows that classical RK4 is not A-stable, and that passive Richardson
[extrapolation](/methods/extrapolation-methods.md) of the trapezoidal rule
is A-stable of order 4 while feeding the extrapolated values back is not.

Section 3 extends the idea to nonlinear problems for the trapezoidal rule.
Under a condition C$_\kappa'$ on a time-dependent quadratic Lyapunov
function of the error equation it proves existence and uniqueness of the
implicit step and a global error bound (Thm. 3.1) that stays bounded for
all $t$ when $\kappa<0$, with no restriction from $\lvert h\,\partial f/\partial y\rvert$:
"a generalization of the A-stability property". The paper does not use
the term [B-convergence](/definitions/b-convergence.md). Theorems 3.2–3.3
treat the borderline $\kappa=0$. The paper closes with remarks on
[solving the implicit step](/methods/implicit-stage-solvers.md): fixed-point
iteration converges only for small $h\,\partial f/\partial y$, and a fixed
number of iterations can make the error unbounded. There are no numerical
experiments.

# Version read

Version of record, a publisher scan of BIT pp. 27–43 (17 PDF pages, 2005
digitization), all read visually because the OCR layer is unreliable in
the equations. Title and author agree with the Crossref record; the DOI and
the issue number are not printed, and no received date is printed.
Section, equation, lemma and theorem numbers are those of the paper.

# Key claims

Registry notation: $y$ for the paper's solution $x$, $\lambda$ for the
coefficient $q$ of the test equation (1.8), $z=h\lambda$ for its $qh$;
$\alpha_j$, $\beta_j$, $\varrho$, $\sigma$, $k$, $p$ agree with the registry.
Page-local symbols of §3 are renamed (notation map).

1. Definition: "A $k$-step method is called A-stable, if all solutions of
   (1.2) tend to zero, as $n\to\infty$, when the method is applied with
   fixed positive $h$ to any differential equation of the form $dx/dt=qx$
   (1.8), where $q$ is a complex constant with negative real part" (§1,
   p. 29). **Stated** (definition introduced here)
2. "In most applications A-stability is not a necessary property"; it is
   desirable for long-time integration of $y'=Ly+u(t)$ with decaying modes
   of large modulus, and "the requirement of A-stability is an extreme
   formulation of the wishes in such situations" (§1, p. 29). **Stated**
3. Order $p$ is the largest integer with $L\varphi=0$ for all polynomials
   of degree $p$, where $L=\varrho(E)-hD\sigma(E)$; then
   $L\varphi(t)\sim-c\,h^{p+1}\varphi^{(p+1)}(t)$ (second Eq. (1.5)), and
   the error constant is $c^*=c/\sigma(1)$. Consistency is $p\ge1$, i.e.
   $\varrho(1)=0$, $\varrho'(1)=\sigma(1)$ (1.6) (§1). **Stated**
   (background, cited to Henrici)
4. For given $k$ the order can reach $p=2k$ and no more, and "no method with
   $p>k+2$ can possess a certain stability property" (§1, p. 28, citing
   Henrici, pp. 217 and 229). **Stated**
5. Lemma 2.1: a $k$-step method is A-stable iff $\varrho(\zeta)/\sigma(\zeta)$
   is regular and has a non-negative real part for $\lvert\zeta\rvert>1$
   (§2, p. 30). In the proof, $\sigma$ has no zeros in $\lvert\zeta\rvert>1$,
   while "simple zeros of $\sigma(\zeta)$ may, however, exist on the
   boundary". **Proved**
6. Theorem 2.1: an explicit $k$-step method cannot be A-stable (p. 30).
   **Proved**
7. A-stable consistent methods exist: the trapezoidal rule
   $\varrho=\zeta-1$, $\sigma=\frac12(\zeta+1)$ (2.2); $\varrho=\zeta-1$,
   $\sigma=\zeta$; and, for every positive integer $k$,
   $\varrho=\zeta^k-1$, $\sigma=\frac12k(\zeta^k+1)$ (p. 30). **Stated**
   ("it is easy to verify")
8. Theorem 2.2: "The order, $p$, of an A-stable linear multistep method
   cannot exceed 2. The smallest error constant, $c^*=\frac1{12}$, is
   obtained for the trapezoidal rule, $k=1$" (p. 31). Proof: with the
   page-local Möbius variable $w=(\zeta+1)/(\zeta-1)$ the polynomials
   become $r(w)$, $s(w)$; for $p\ge2$,
   $r(w)/s(w)=2w^{-1}+(\frac23-8c')w^{-3}+O(w^{-4})$ (2.3), with $c'=c^*$
   if $p=2$ and $c'=0$ if $p>2$; the Riesz–Herglotz representation (2.4)
   makes $xr(x)/s(x)$ non-decreasing for $x>0$ (2.5), so
   $\frac23-8c'\le0$ (pp. 31–32). **Proved**
9. The trapezoidal rule is the only linear multistep method with $p=2$,
   $c^*=\frac1{12}$ (p. 32). **Proved**
10. The least upper bound for the order of A-stable methods "is equal to
    2"; a preliminary upper bound was obtained in the author's ref. [4,
    Theorem 4] (§1, p. 29). **Stated**
11. Robertson's ref. [7] takes a "less extreme approach": $k=2$, $p=3$
    methods such that all solutions "tend to zero in a large portion of the
    complex plane for the quantity $qh$, though not in the whole half-plane
    $\operatorname{Re}(qh)<0$" (§1, p. 29). **Stated**
12. "The concept of A-stability has an obvious meaning also outside the
    class of linear multi-step methods": classical RK4 applied to (1.8)
    gives $(1+z+z^2/2!+z^3/3!+z^4/4!)^n$, whose base tends to infinity as
    $z\to-\infty$, so it is not A-stable (pp. 32–33). **Derived**
13. Passive Richardson extrapolation of the trapezoidal rule,
    $y^*(t,h)=\frac13\bigl(4y(t,h)-y(t,2h)\bigr)$ at $t=2h,4h,\dots$,
    "without using the extrapolated values in the succeeding computation",
    has error $O(h^4)$ and is A-stable "since it is obtained by subtraction
    of the results of two A-stable procedures" (p. 33). **Stated** (no
    proof)
14. If the extrapolated values are used in the succeeding computation,
    A-stability is lost:
    $\lim_{z\to-\infty}\frac13\Bigl(4\bigl(\frac{1+z/2}{1-z/2}\bigr)^2-\frac{1+z}{1-z}\Bigr)=\frac53>1$
    (p. 33). **Derived**
15. §3, framework: for the error $u=y-y(t)$ of the trapezoidal rule,
    $f(t,y(t)+u)-f(t,y(t))=A(t)u+j(t,u)$. If the linearization is
    uniform-asymptotically stable, Malkin's theorem gives a quadratic
    Lyapunov function $V=u^\top G(t)u$ with
    $\underline m^2\lvert u\rvert^2\le V\le\overline m^2\lvert u\rvert^2$
    (3.7) and $\lvert\partial G/\partial t\rvert\le\underline m^2\gamma_G$
    (3.8) (pp. 34–35). Condition C (existence of such a $V$ with negative
    definite derivative) is less restrictive: $y'=-y^3$ with $V=y^2$
    satisfies it although its linearization is only non-asymptotically
    stable (p. 35). **Derived** / **Shown**
16. Condition C$_\kappa'$ (3.19) bounds a discrete analogue $W$ of
    $dV/dt$ (3.18) by $2\kappa(\lvert u\rvert^2+\lvert\frac12h g\rvert^2)$;
    $\kappa'=\kappa\underline m^{-2}$ if $\kappa\ge0$,
    $\kappa\overline m^{-2}$ if $\kappa\le0$. For a linear equation with a
    time-independent quadratic Lyapunov function a negative $\kappa$
    satisfies C$_\kappa'$ for all $h$ (p. 36). **Stated** ("It can then be
    shown")
17. Fixed-point iteration for the implicit step "converges, roughly
    speaking, only if all eigenvalues of $\frac12h\,\partial f/\partial x$
    are located inside the unit circle"; under-relaxation extends this to
    real parts less than unity. The existence proof therefore uses
    continuation in the step size instead (p. 38). **Stated**
18. Lemmas 3.1–3.3: if $h\kappa'<1$ (no restriction on $h$ if
    $\kappa\le0$), the implicit step (3.10) has at most one solution in the
    tube $\mathfrak S_\delta$ around $y(t)$, $I-\frac12h\,\partial f/\partial y$
    is non-singular there, and a solution exists under (3.33) (pp. 38–39).
    **Proved**
19. The local truncation error of the trapezoidal rule "is known to be less
    than $h^3\sup\lvert x'''(t)\rvert/12$" (p. 38). **Stated**
20. Theorem 3.1: under $h\kappa'<1$, C$_\kappa'$ and a smallness condition
    on $\Phi(t,h)$, (3.10) defines $y_1,y_2,\dots$ uniquely and
    $\lvert y_n-y(t_n)\rvert\le\Phi(t_n,h)(\overline m/\underline m)(1-h\kappa')^{-1/2}$
    (3.35), with
    $\Phi(t,h)=\varepsilon_0e^{\mu(t-h)}+\rho^*\frac{1-e^{\mu t}}{1-e^{\mu h}}$
    (3.29), $\mu=\frac1{2h}\log\frac{1+h\kappa'}{1-h\kappa'}$ (3.25),
    $\varepsilon_0$ the initial-error bound and $\rho^*$ a bound on the
    perturbations plus the local truncation error (3.32) (pp. 39–40).
    **Proved**
21. When $\kappa<0$ the step can be chosen from the local truncation error
    and the rate of change of the Lyapunov function alone; even when
    $\lvert h\,\partial f/\partial y\rvert$ is large the error stays bounded
    in an unlimited computation: "This is a generalization of the
    A-stability property" (pp. 40–41). **Proved** (from Thm. 3.1)
22. The bounds of the author's dissertation (ref. [3, Ch. 5]) are less
    general than Theorem 3.1 for the trapezoidal formula: "they do not always
    give sharp bounds, when Liapunov functions with variable coefficients are
    needed, and, above all, they are based on the assumption
    $\frac12h\lvert\partial f/\partial x\rvert<1$" (p. 40). **Stated**
23. For $\kappa=0$, $\Phi$ grows linearly in $t$ (p. 41). Theorems 3.2–3.3,
    under the stronger condition C$_0''$, bound
    $s_n=\lvert u_n-\frac12hg_n\rvert_{n-1}$ for all $n$ or in the limit
    superior, with $\overline{\lim}\,\lvert y_n-y(t_n)\rvert\le\underline m^{-1}M$
    (pp. 41–42). $y'=-y^3$ satisfies C$_0''$ but C$_\kappa'$ for no negative
    $\kappa$ (p. 42). **Proved** / **Shown**
24. The trapezoidal rule has two disadvantages, order 2 and implicitness;
    the first can be partly compensated by Richardson extrapolation (p. 42).
    **Stated**
25. With a fixed number $j$ of fixed-point iterations the error can grow to
    infinity even when $\lvert h\,\partial f/\partial y\rvert$ is rather
    small: for $f=\lambda y$ with small imaginary $z$, boundedness of the
    iterated trapezoidal sequence depends on $j\bmod4$ (remark of H. Keller)
    (pp. 42–43). **Stated**
26. Note added in proof: an A-stable method applied to (1.8) with purely
    imaginary $\lambda$ has bounded solutions; the roots of the
    characteristic equation satisfy $\lvert\zeta\rvert\le1$ and those of
    unit modulus are simple (p. 43). **Derived** (proof sketched)

The paper does not use the phrase "second barrier", nor the terms
zero-stability, stiffness, G-stability or B-convergence. Its $G(t)$ is a
$d\times d$ Lyapunov matrix in state space for the one-step trapezoidal
error, not a matrix on a multistep history vector.

*(Compiler check, not in the sources.)*
$y(t+h)-y(t)-\frac h2\bigl(y'(t+h)+y'(t)\bigr)=-\frac1{12}h^3y'''+O(h^4)$,
so with the minus sign of (1.5) $c=\frac1{12}$, $\sigma(1)=1$ and
$c^*=+\frac1{12}$, as printed.

# Printed slips

- Two different equations are numbered (1.5) on p. 28: "$Ex(t)=x(t+h)$, or
  $Ex_n=x_{n+1}$" and "$L\varphi(t)\sim-ch^{p+1}\varphi^{(p+1)}(t)$"; later
  references to (1.5) mean the second.
- p. 30, proof of Lemma 2.1: "Hence $\sigma(\zeta_1)\neq0$, if
  $\lvert\zeta\rvert>1$" (subscript missing on $\zeta$).
- p. 37: "Hence, by (3.5) and (3.15)" precedes (3.21), which uses the bounds
  of (3.7); p. 39: (3.34) is obtained "by (3.6) and (3.5)" while the
  inequality uses (3.8) and (3.7).
- p. 37: "$\varepsilon_0$ be an upper bound of the errors in
  $x_0(1-h\lambda')^{\frac12}$ and $x_0+\frac12hf(t_0,x_0)$", transcribed as
  printed.
- p. 38, after (3.31): "(3.10) has a solution $(t_{n+1},x_{n+1})\in\mathfrak S_\lambda$";
  elsewhere the tube is $\mathfrak S_\delta$.
- p. 41: "$\lim_{\lambda\to0}\frac{1-e^{\mu t}}{1-e^{\mu h}}=\frac th$": the
  limit variable is $\lambda$, the expression depends on $\mu$.
- p. 41: Condition C$_0''$ is introduced "in addition to condition C$_0'$",
  a symbol not defined separately (C$_\lambda'$ with $\lambda=0$).

# Notation map

| Dahlquist (1963) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $x(t)$, $x_n\in R^s$ | $y$, $y(t)$, $y_n\in\mathbb R^d$ | **the paper's $y$ is the error in §3**, here $u$; its $s$ is the dimension, **not the number of stages** |
| $f(t,x)$ | $f(t,y)$ | |
| $h$, $t_m=mh$ | $h$, $t_m$ | constant step |
| $k$, $\alpha_j$, $\beta_j$, $\varrho(\zeta)$, $\sigma(\zeta)$ | same | agree; $\varrho$, $\sigma$ assumed coprime, $\alpha_k$ not normalized |
| $E$, $D$, $L=\varrho(E)-hD\sigma(E)$ | — | shift, $d/dt$, difference operator; $L$ **collides with the registry linear operator $L$** |
| $p$ | $p$ | order |
| $c$, $c^*=c/\sigma(1)$ | — | error constant, page-local; sign fixed by $L\varphi\sim-ch^{p+1}\varphi^{(p+1)}$, trapezoidal $c^*=+\frac1{12}$ |
| $q$, $qh$ in $dx/dt=qx$ (1.8) | $\lambda$, $z=h\lambda$ | test equation |
| $Q$, $f(t)$ in $dx/dt=Qx+f(t)$ (§1) | $L$, $u(t)$ | motivating linear system; $u$ page-local in the Summary and claim 2 (it is the error only in claims 15–23) |
| **$z=(\zeta+1)/(\zeta-1)$** | $w$ | **collision with $z=h\lambda$**; proof-local Möbius variable |
| $r(z)$, $s(z)$, $a_j$, $b_j$, $c'$ | $r(w)$, $s(w)$ | transformed polynomials; **$a_j$, $b_j$ collide with splitting coefficients and RK weights** |
| $\omega(t)$ (§2); $\omega(\varepsilon)$ (§3) | — | Herglotz measure; modulus of continuity of $\partial f/\partial x$ |
| $A(t)=\partial f/\partial x$ along $x(t)$ | $J$ along $y(t)$ | **collision with the Butcher matrix $A$** |
| $y$, $g(t,y)$, $j(t,y)$ (§3) | $u$, $g$, $j$ | error, its right-hand side, nonlinear remainder |
| **$G(t)$**, $V=y^TG(t)y$ | $G(t)$, $V=u^\top G(t)u$ | **collision with the registry $G$ of [G-stability](/properties/g-stability.md)** ($k\times k$ on history vectors); here $d\times d$ in state space |
| **$\alpha$, $\beta$, $\gamma$** (3.7)–(3.8) | $\underline m$, $\overline m$, $\gamma_G$ | **collision with $\alpha_j$, $\beta_j$ and the tree density $\gamma$**; page-local |
| **$\lambda$, $\lambda'$** (C$_\lambda'$) | $\kappa$, $\kappa'$ | **collision with the eigenvalue $\lambda$**; a one-sided bound on $W$; page-local |
| $\mu$ | $\mu$ | exponential rate of the bound (3.25), page-local |
| $p_n$, $q_n$, **$q^*$** | perturbations, $\rho^*$ | **$q^*$ collides with the test coefficient $q$ and the stage order $q$** |
| $\Phi(t,h)$, $\varepsilon_0$ | same | bounding function (3.29); **$\Phi$ collides with the elementary weight $\Phi(\tau)$** |
| $\lvert y\rvert_n=\sqrt{y^TG(t_n)y}$, $W$, $W_1$, $s_n$, $M$ | same | §3 norms and bounds, page-local; **$M$ collides with the mass matrix** |
| $\mathfrak S_\delta$ | — | tube $\{(t,y):\lvert y-y(t)\rvert<\delta\}$ |
| $x(t,h)$, $x^*(t,h)$ | $y(t,h)$, $y^*(t,h)$ | trapezoidal result with step $h$; extrapolated value |
| $j$ (p. 43) | — | number of fixed-point iterations |

# Reference list

The paper prints 7 references, numbered [1]–[7] and ordered
alphabetically. All 7 are merged complete into the
[bibliography](/bibliography.md) with `citedby` dahlquist-1963. Ref. [3]
is the author's 1958 Stockholm dissertation, also printed in Trans. Roy.
Inst. Technol. Stockholm Nr. 130 (1959), recorded as a thesis with the
alternative venue in a note. Ref. [4] is printed "To appear" in Proc.
Symposia on Applied Mathematics vol. 15 (1962) and kept as its own
pre-publication entry. Ref. [7] (Robertson, Information Processing, UNESCO,
Paris, pp. 106–108) prints no year. Ref. [6] prints the author as
"Henrici, P. K.". No DOIs are printed. No printed duplicates.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [B-convergence](/definitions/b-convergence.md)
* [Dahlquist's order barrier for A-stable multistep methods](/results/dahlquist-second-barrier.md)
* [Extrapolation methods (Richardson extrapolation of a base integrator)](/methods/extrapolation-methods.md)
* [G-stability](/properties/g-stability.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Solving the stage equations of implicit Runge–Kutta methods](/methods/implicit-stage-solvers.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stiffness](/definitions/stiffness.md)
* [Zero-stability](/definitions/zero-stability.md)
