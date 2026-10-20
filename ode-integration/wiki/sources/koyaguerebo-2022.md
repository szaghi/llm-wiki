---
type: Source
title: "Koyaguerebo-Imé & Bourgault (2022) — Arbitrary high order A-stable and B-convergent numerical methods for ODEs via deferred correction"
description: "Builds a recursive hierarchy of deferred-correction schemes DC2, DC4, DC6, ... on the implicit midpoint rule, each level one midpoint-type nonlinear solve per step, and proves order 2j for every level, A-stability of all levels and B-convergence under a one-sided Lipschitz condition, with fixed-step stiff tests."
resource: "doi:10.1007/s10543-021-00875-y"
source_kind: paper
authors: [Koyaguerebo-Imé S.C.E.R., Bourgault Y.]
year: 2022
venue: "BIT Numer. Math. 62:139-170"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_BIT_Numerical_Mathematics_Koyaguerebo-Imé_Arbitrary_high_order_A-stable_and_B-convergent_numerical_met.pdf"
tags: [deferred-correction, implicit, stiff, stability, b-convergence]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds a recursive hierarchy of
[deferred-correction](/methods/deferred-correction.md) schemes DC2, DC4,
DC6, … on the implicit midpoint rule for $y'=f(t,y)$ in a Banach space,
extending the Gustafsson–Kress idea from linear monotone problems to
nonlinear ones. It is a different variant from the subnode and collocation
deferred corrections: no subnodes inside a step (except at start-up), and
the corrections use neighbouring step values. Centred finite-difference
expansions of $y'(t_{n+1/2})$ and $y(t_{n+1/2})$ in powers of
$h^2D_+D_-$ would give a high-order multistep scheme; instead, level
$2j+2$ applies the difference corrections to the already computed level-$2j$
solution $y^{[2j]}_n$. Each level thus solves one nonlinear system of
implicit-midpoint form per step. Start-up values use the level-$2j$ scheme
on a refined step $h/(2j+1)$.

A Deferred Correction Condition (the level-$2j$ error and its centred first
and second divided differences are $O(h^{2j})$) guarantees that the next
level has order $2j+2$, under any of four hypotheses on $f$. An induction
shows that every level satisfies the condition, so DC$2j$ has order $2j$.
Under a one-sided Lipschitz condition the error constant is independent of
the global Lipschitz constant: [B-convergence](/definitions/b-convergence.md).
On the Dahlquist test equation each level's solution is the trapezoidal
factor to the power $n-j$ times a polynomial of degree $j$ in $n$, which
proves [A-stability](/properties/a-stability.md) of every level in an
asymptotic sense. For $j\ge1$ the scheme is not a Runge–Kutta method and
has no one-step stability function.

Fixed-step Scilab tests on Bernoulli, a long-time oscillatory problem, a
modified B5, E5, the [Robertson problem](/benchmarks/robertson-problem.md)
and the [van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
with $\mu=1000$ compare DC2–DC10 with fixed-step BDF2/4/6, RK4 and Scilab's
solvers. Design orders appear on the linear problems; on the stiff
nonlinear ones convergence is often below design order (a form of
[order reduction](/definitions/order-reduction.md) that the authors
attribute to the non-asymptotic regime), while large-step accuracy is good.

# Version read

arXiv preprint arXiv:1903.02115v4 [math.NA], 3 April 2021, typeset in
the Springer BIT template ("will be inserted by the editor"), 28 pages
numbered 1–28, not the version of record (BIT 62:139–170, issue 2022,
online 2021). Page, equation and section numbers cited here are those of
the arXiv v4; the DOI is not printed on the copy. Title and authors match
Crossref. The authors' self-citations print the first author's initials
inconsistently ("S.C.E." in ref. [17], "S.C.R." in ref. [18]; page 1 gives
"Saint-Cyr E.R.").

# Key claims

Registry notation: $h$ the uniform step (the source's $k$), $y'=f(t,y)$
(the source's $u'=F(t,u)$), $y^{[2j]}_n$ the level-$2j$ solution at $t_n$
(the source's $u^{2j,n}$), $z=h\lambda$. Page-local: $D$, $D_\pm$ centred,
forward and backward divided differences; $\Lambda$ the Lipschitz constant
and $\mu$ the one-sided Lipschitz constant,
$\langle f(t,x)-f(t,w),x-w\rangle\le\mu\lVert x-w\rVert^2$ (the source's
$\mu$ and $\beta$).

1. DC$2j+2$ (Eqs. (2.8)–(2.9)) is a one-step-per-level scheme obtained from
   the multistep centred scheme (2.6) by substituting $y^{[2j]}$ for the
   unknown inside the correction sums; DC2 is the implicit midpoint rule
   (2.7) (§2). **Derived**
2. Each new value solves one system $x-a^j_n-hf(t_{n+1/2},\frac12x+b^j_n)=0$
   of implicit-midpoint form; storage is $j^2+3j+1$ vectors (Remark 2.2,
   Eq. (2.14)). **Stated**
3. Only DC2 is a Runge–Kutta method; for $j\ge1$ no recurrence
   $y^{[2j+2]}_{n+1}=R(z)y^{[2j+2]}_n$ exists, which the authors call "the
   main ingredient behind the A-stability of our DC2j methods independently
   of the order of accuracy" (Remark 2.3). **Stated** (follows from
   Lemma 5.2)
4. Start-up values $y^{[2j+2]}_1,\dots,y^{[2j+2]}_j$ come from scheme
   (2.10)–(2.11) on a sub-grid of step $h/(2j+1)$, with coefficients
   tabulated for $j=1..4$ (Remark 2.1, Table 2.1). **Derived**
5. Deferred Correction Condition: order $2j$ plus
   $\lVert D_+D_-D(y^{[2j]}_{n+1/2}-y(t_{n+1/2}))\rVert+\lVert D_+D_-(y^{[2j]}_{n+1}-y(t_{n+1}))\rVert\le Ch^{2j}$
   (Def. 3.1, Eq. (3.1)). **Stated** (definition)
6. If $y^{[2j]}$ satisfies the condition and the first $j$ start-up values
   of level $2j+2$ are $O(h^{2j+2})$, then
   $\lVert y^{[2j+2]}_n-y(t_n)\rVert\le Ch^{2j+2}$ under any of: (i) $f$
   Lipschitz, $0\le\Lambda h<2$; (ii) finite dimension and
   $y^{[2j+2]}_n$ within a bounded distance of $y$; (iii) infinite
   dimension and $y^{[2j+2]}_n\to y$; (iv) Hilbert space and $f$ one-sided
   Lipschitz, $-2\le\mu h<2$ (Thm 3.1, Eqs. (3.4)–(3.8), (3.14)).
   **Proved**
7. The correction applies to any scheme satisfying the condition, not only
   to implicit-midpoint levels (Remark 3.2). **Stated**
8. The implicit midpoint error has all centred divided differences
   $(D_+D_-)^mD$ and $(D_+D_-)^m$ of order $O(h^2)$, $m=0..p$ (Lemma 4.1,
   Eq. (4.2)). **Proved**
9. By induction every DC$2j$, $j=1..p+1$, has order $2j$ and satisfies the
   extended divided-difference estimate (4.1), hence the condition
   (Thm 4.1; requires $y\in C^{2p+3}$, $f\in C^{2p+2}$). **Proved**
10. B-convergence: for $f:\mathbb R^d\to\mathbb R^d$ one-sided Lipschitz,
    $\lvert y^{[2j]}_n-y(t_n)\rvert\le Ch^{2j}$ for $h\in(0,h_0)$,
    $h_0=2/\mu$ if $\mu>0$ and $h_0=+\infty$ if $\mu\le0$, with $C$
    independent of any global Lipschitz constant (it depends on derivatives
    of $y$ and on a Jacobian bound on a compact set) (Cor. 4.1, Eq. (4.18),
    Remark 4.1). **Proved**
11. The independence of $C$ from $J$ is "somewhat artificial", because
    $y''=f_t+Jy'$ ties the derivatives of $y$ to $J$ (Remark 4.1).
    **Stated**
12. Under one-sided Lipschitz,
    $\lVert y^{[2j+2]}_n-y(t_n)\rVert\le c\,C\big(\frac{2+\mu h}{2-\mu h}\big)^nh^{2j+2}$,
    $-2\le\mu h<2$; for $\mu<0$ and moderate $h$ large-step solutions are
    very accurate, while in the asymptotic region "a non B-convergent
    method can be competitive with respect to a B-convergent one for
    sufficiently small time steps" (Remark 4.2, Eq. (4.19)). **Derived**
13. On $y'=\lambda y$, $y(0)=1$:
    $y^{[2j+2]}_n=\big(\frac{2+z}{2-z}\big)^{n-j}P_j(n)$, $n\ge j$, with
    $P_j$ a polynomial of degree $j$ in $n$ whose coefficients depend on
    $z$ (Lemma 5.2, Eq. (5.4)). **Proved**
14. Every DC scheme is A-stable in the sense $\lim_{n\to\infty}\lvert
    y_n\rvert=0$ for all $\operatorname{Re}z<0$ (Def. 5.1, Thm 5.1).
    **Proved** (no bound uniform in $n$ and $z$ is given)
15. Bernoulli ($y'=-0.1y-1000y^{20}$): very accurate large-step solutions
    (at $h=1$, DC6 $1.8\cdot10^{-4}$, DC10 $1.3\cdot10^{-4}$, BDF6
    $6.1\cdot10^{-2}$; RK4 unstable for $h\ge2.03\cdot10^{-3}$), but
    suboptimal convergence; in the asymptotic region RK4 is more accurate
    than DC4 and the BDFs (§6.1, Table 6.1). **Shown**
16. Oscillatory problem $y'=\lambda y\cos t$, $\lambda=10$, $T=10^6$: each
    level shows its design order down to a floor of about
    $3\cdot10^{-6}$–$5\cdot10^{-6}$; at $h=1.56\cdot10^{-3}$ BDF2/4/6 errors
    are $22026$, $14837$, $5578$ against DC4 $3.8\cdot10^{-4}$ (§6.2,
    Table 6.2). **Shown**
17. Modified B5 ($\alpha=5000$, eigenvalues $-10\pm5000i$): DC2–DC10 show
    exact design orders 2–10, but "BDF methods perform better for this
    problem than DC schemes" (§6.3, Table 6.3). **Shown**
18. E5: DC outperforms the fixed-step BDFs (at $h=10$, DC10
    $4.51\cdot10^{-16}$ against BDF6 $3.5\cdot10^{-11}$ on component 1);
    higher levels show their order only over a small range of $h$; RK4
    unstable for $h\ge2\cdot10^{-4}$ (§6.4, Table 6.4). **Shown**
19. Robertson ($T=10^5$): accurate even at $h=0.5$ (DC6 maximum error about
    $2\cdot10^{-6}$), slow convergence for $h>1/300$; "the error constants
    might be 3 to 5 orders of magnitude smaller for DC than BDF methods";
    Scilab's `rkf` fails (§6.5, Table 6.5). **Shown**
20. Van der Pol ($\mu=1000$, $T=3000$): DC2 and DC4 show order 0 down to
    $h=7.5\cdot10^{-6}$, DC6 and DC8 reach orders of about 6–7.6, and DC10's
    order "is not observed, though the solutions obtained are accurate"
    (§6.6, Table 6.6). **Shown**
21. For eigenvalues $\lambda=\lambda_1+i\lambda_2$, good accuracy needs
    $h\max\{\lambda_1,\lvert\lambda_2\rvert\}<2$, while asymptotic
    convergence at full order needs $h\lvert\lambda\rvert<2$, i.e.
    $h\max\lVert J\rVert<2$ (§6.7). **Stated** (from the proof)
22. Cost: DC2 solves $N$ nonlinear systems and DC$2j$ $j\times N$; on
    Bernoulli DC10 reaches about $1.1\cdot10^{-11}$ with about
    $5\cdot10^6$ systems against DC2 $8.9\cdot10^{-7}$ with
    $N=5\cdot10^6$; no CPU times (§6.7). **Shown**
23. Earlier deferred and integral deferred corrections are "linear
    perturbation[s] of a low order scheme" for which stiff problems are "a
    challenge"; Kushnir–Rokhlin's method "requires sufficiently small time
    steps for moderately stiff problems while convergence is reduced to
    order 2 for 'very stiff' problems" (§1). **Stated**
24. A companion paper gives "an arbitrary high order and unconditionally
    stable method" for reaction–diffusion equations (ref. [18]) (§1).
    **Stated**

*(Compiler checks, not in the sources.)* The introduction says each DC
scheme "is B-stable", but the body proves B-convergence, not B-stability;
the A-stability of Def. 5.1 is weaker than $\lvert R(z)\rvert\le1$
power-boundedness (polynomial transient growth is allowed, and the factor
tends to $-1$ as $\lvert z\rvert\to\infty$, so the levels are not
L-stable); Corollary 4.1 drops the condition $\mu h\ge-2$ of Thm 3.1(iv).

# Printed slips

- Remark 4.2: Eq. (4.19) prints the constant as $c_{2j+1}C$, but the text
  then says "only $c_{2j+3}k^{2j+2}$ must dominate the constant $C$".
- Remark 3.1: the transform of $k^{2i}(D_+D_-)^i$ is printed without the
  index shifts on the right-hand side, so it is not an identity as
  printed; "$k^i(D_+D_-)^iD$" should read $k^{2i}$; "(3.1) is equivalent to
  (3.2)–(3.3)" is argued in one direction only. The index range is
  $n=1,\dots,N-2$ in Def. 3.1 and $n=j,\dots,N-j$ in Remark 3.1.
- Proof of Thm 3.1, case 3: "taking the DDC" (for DCC). §1: "proved is
  section 5". Eq. (2.4) has an unbalanced parenthesis.
- Table 6.4 prints two entries with a Fortran exponent ("2.85D-15",
  "4.09D-16"); §6.6 "$k=1.875\times\times10^{-6}$".
- §6.1: "DC10 achieves order 8.05 of convergence for $k=7.14\times10^{-6}$
  to $k=6.66\times10^{-6}$"; these steps are not in Table 6.1.
- §1: "inherit the A-stable property of the trapezoidal rule", although the
  base is the implicit midpoint rule (the two coincide only on linear
  autonomous problems).
- Table 6.5 "orders" at $h=1/600$ (14, 19.6, 27.7, …) are computed from
  errors at round-off level.

# Notation map

| Koyaguerebo-Imé & Bourgault (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u'=F(t,u)$, $u\in X$ | $y'=f(t,y)$ | $X$ a Banach space |
| $k$ | $h$ | uniform step |
| $t_n=nk$, $t_{n+1/2}$ | $t_n$, $t_{n+1/2}$ | |
| $u^{2j,n}$ | $y^{[2j]}_n$ | **superscript $2j$ is the level's order, not a power** |
| $D$, $D_+$, $D_-$, $E$ | — | centred, forward, backward divided differences; averaging |
| **$c_{2i}$, $c_{2i+1}$, $c^j_i$** | — | **expansion coefficients; collide with the abscissae $c_i$** |
| $\Lambda^j$, $\Gamma^j$ | — | correction operators; **$\Gamma$ collides with the MRI coupling $\Gamma^{(k)}$** |
| $\mu$ (Lipschitz) | $\Lambda$ | page-local |
| **$\beta$ (one-sided Lipschitz)** | $\mu$ | **$\beta$ collides with Shu–Osher $\beta_{ij}$ and the PID exponents** |
| **$\mu$ (van der Pol)** | $\mu$ | **the van der Pol parameter reuses the Lipschitz letter** |
| $F_u$, $d_uF$ | $J$ | Jacobian |
| $\lambda$, $z=\lambda k$ | $\lambda$, $z=h\lambda$ | agrees |
| $(2+\lambda k)/(2-\lambda k)$ | $R(z)$ of the implicit midpoint rule | for $j\ge1$ the scheme has no one-step $R(z)$ |
| $P_j(n)$ | — | polynomial in the step index; **not** a stability polynomial |
| $s$ (in $\mathbb R^s$) | $d$ | **collides with the stage number $s$** |
| DCC, DC$2j$ | — | Deferred Correction Condition; level-$2j$ scheme |

# Reference list

The paper prints 27 references in numbered style, alphabetical by first
author. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` koyaguerebo-2022. Ref. [1] is an encyclopedia chapter;
refs. [17] and [18] are the authors' own arXiv preprints, kept as their own
2020 entries in printed order; ref. [4] prints "Björck, A.k." (for "Å.");
ref. [11] is Hairer–Wanner II as "vol. 14"; ref. [20] prints the issue
"17(1-4)". No DOIs are printed and there are no printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [B-convergence](/definitions/b-convergence.md)
* [Deferred correction (DeC)](/methods/deferred-correction.md)
* [Order reduction](/definitions/order-reduction.md)
* [Robertson problem](/benchmarks/robertson-problem.md)
* [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
