---
type: Source
title: "Biswas et al. (2024) — Algebraic Structure of the Weak Stage Order Conditions for Runge–Kutta Methods"
description: "Gives the first algebraic theory of weak stage order: it recasts the conditions as orthogonality of two invariant subspaces, proves barriers linking stages, order, weak stage order and distinct abscissae for general and diagonally implicit Runge–Kutta methods, and derives minimal-polynomial conditions that guide the construction of high-weak-stage-order DIRKs."
resource: "doi:10.1137/22m1483943"
source_kind: paper
authors: [Biswas A., Ketcheson D.I., Seibold B., Shirokoff D.]
year: 2024
venue: "SIAM J. Numer. Anal. 62:48-72"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_SIAM_Journal_on_Numerical_Analysis_Biswas_Algebraic_Structure_of_the_Weak_Stage_Order_Conditions_for_R.pdf"
tags: [runge-kutta, order-conditions, order-reduction, implicit, linear-algebra]
timestamp: 2026-10-19T12:00:00Z
---

# Summary

Stiff problems cause [order reduction](/definitions/order-reduction.md) in
Runge–Kutta methods. In the worst case the observed rate drops to the
[stage order](/definitions/stage-order.md) $q$, and $q>2$ is impossible for
[DIRK methods](/methods/diagonally-implicit-runge-kutta.md). For linear
problems the weaker conditions $b^\top A^j\tau^{(k)}=0$ ($0\le j\le s-1$,
$1\le k\le q_{\mathrm w}$) suffice. These conditions define the
[weak stage order](/definitions/weak-stage-order.md) $q_{\mathrm w}$ and go
back to the "parabolic order conditions" of Ostermann and Roche for
[Rosenbrock–Wanner](/methods/rosenbrock-wanner-method.md) and Runge–Kutta
methods. The eigenvector criterion of earlier constructions limits DIRKs
with invertible $A$ to $q_{\mathrm w}\le3$.

The paper gives the first algebraic theory of weak stage order.
$q_{\mathrm w}\ge k$ is equivalent to orthogonality of two invariant
subspaces: the smallest $A$-invariant subspace $\mathcal K_k$ containing
$\tau^{(1)},\dots,\tau^{(k)}$ and the smallest $A^\top$-invariant
subspace $\mathcal Y$ containing $b$. Hence
$\dim\mathcal Y+\dim\mathcal K_{q_{\mathrm w}}\le s$. Lower bounds on
$\dim\mathcal Y$ come from the degrees of the
[stability function](/definitions/stability-function.md) together with the
Padé and real-pole barriers. Lower bounds on $\dim\mathcal K_m$ come from a
polynomial construction on $\mathrm{diag}(c)$ and, for DIRKs, a
leading-block truncation. The result is a set of
[weak-stage-order barriers](/results/weak-stage-order-barriers.md) for
general Runge–Kutta methods and sharper ones for DIRKs, which recover
$p\le s+1$ at $q_{\mathrm w}=0$ and are refined for
[stiff accuracy](/properties/stiff-accuracy.md) and for the new class of
GEDIRKs.

The subspaces carry minimal polynomials $\mu_{\mathcal K}$ (for
$\mathcal K_{q_{\mathrm w}}$) and $Q$ (for $\mathcal Y$), with
$\mu_{\mathcal K}\mu_{\mathcal Y}\mid\det(xI-A)$. Expanding $Q$ in polynomials orthogonal for the
functional $x^n\mapsto1/(n+1)!$ yields a formula for $R(z)$. For DIRKs the
leading diagonal entries must be roots of $\mu_{\mathcal K}$; this is the design rule
used by the companion paper
[Biswas et al. (2023)](/sources/biswas-2023.md) to build the
[DIRK schemes with high weak stage order](/methods/dirk-high-weak-stage-order.md).
The examples characterize the $(s,p,q_{\mathrm w})=(2,2,3)$ and $(3,3,3)$
DIRKs and show that the
[Gauss–Legendre methods](/methods/fully-implicit-runge-kutta.md) attain the
general bound. The
[Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md) is
used analytically only. Everything is proved; there are no numerical
experiments.

# Version read

arXiv:2204.03603v2 [math.NA], 3 February 2024, a 26-page amsart preprint
(main text pp. 1–21, appendices pp. 21–23, references pp. 24–25). It is
the post-review revision, since the acknowledgements thank two referees,
but not the SINUM version of record (pp. 48–72). Title and authors match
the published version; page 1 prints "Runge-Kutta" with a hyphen. The DOI
is not printed in the file. Numbering on this page is that of arXiv v2.

# Key claims

Registry notation: $h$ step, $q$ stage order (the source's $\tilde q$),
$q_{\mathrm w}$ weak stage order (the source's $q$), $\mathcal Y$ and
$\mathcal K_m$ the source's $Y$ and $K_m$, $\delta_{\mathrm{SA}}=1$ for a
stiffly accurate method with invertible $A$ (else 0), $\delta_{\mathrm{GE}}=1$ for a
GEDIRK (else 0), $n_c$ the number of distinct abscissae.

1. Under $c=A\mathbf 1$, assumed throughout, $\tau^{(1)}=0$, and
   $\tau^{(k)}=Ac^{k-1}-\frac1kc^k$ (§1.1, Eq. (3)). **Stated**
2. Definition: $q_{\mathrm w}$ is the largest integer such that
   $b^\top A^j\tau^{(k)}=0$ for all $0\le j\le s-1$, $1\le k\le q_{\mathrm w}$
   (condition $S(q_{\mathrm w})$); $q_{\mathrm w}=\infty$ if this holds for
   every $k$ (Def. 1.1, Eq. (4)). **Stated** (definition)
3. Weak stage order relaxes stage order: $q\le q_{\mathrm w}$ for any method.
   DIRKs can have high $q_{\mathrm w}$, while their stage order cannot exceed
   2 (§1, §2.2). **Stated**
4. On the Prothero–Robinson problem, weak stage order $q_{\mathrm w}$ makes
   $W_k(z)=z\,b^\top(I-zA)^{-1}\tau^{(k)}$ vanish for $k\le q_{\mathrm w}$,
   giving local error $O(h^{q_{\mathrm w}+1})$ uniformly in $z$. It is the
   least restrictive condition with this property (§2.2, Eq. (9), citing
   Ketcheson et al. 2020, Thm 2). **Stated**
5. The theorems of Alonso-Mallo & Palencia for linear PDEs generated by a
   $C_0$-semigroup are stated with stage order but use only the
   weak-stage-order conditions in their proofs, so weak stage order is
   relevant for any $C_0$-semigroup problem, wave equations included (§2.2).
   **Stated** (the authors' reading, no proof given)
6. Ostermann & Roche: if
   $k\,b^\top(I-zA)^{-1}\tau^{(k)}/(R(z)-1)\equiv0$ for $k\le q_{\mathrm w}$
   (Eq. (11)), plus technical assumptions, the rate for linear parabolic
   PDEs is $\min\{p,q_{\mathrm w}+2+\bar\nu\}$ with $\bar\nu$ depending on the
   PDE (§2.3). **Stated**
7. Montijano: a necessary condition for order-$q$ convergence on
   Prothero–Robinson is $b^\top A^{-1}c^j=1$ for $0\le j\le q$ (§2.3).
   **Stated**
8. The weak-stage-order conditions (4) are necessary for any Runge–Kutta
   scheme, not only SDIRK, to avoid order reduction on the
   Prothero–Robinson problem (§2.3). **Stated**
9. $q_{\mathrm w}\ge k$ iff $\mathcal Y\perp\mathcal K_k$, and then
   $\dim\mathcal Y+\dim\mathcal K_k\le s$ (Lemma 3.4, Eq. (14)). **Proved**
10. Almost all irreducible schemes not designed for weak stage order have
    $\dim\mathcal Y=s$, so $q_{\mathrm w}$ is at most their stage order.
    The exceptions include explicit methods with a zero first-subdiagonal
    entry, such as the 8th-order Prince–Dormand method and some fifth-order
    SSP methods of Ruuth–Spiteri (§3.1). **Stated**
11. General Runge–Kutta (Thm 3.1). (1) If all $c_j\ne0$, then
    $q_{\mathrm w}\le2n_c-1$. (2) If some $c_j=0$, then either
    $q_{\mathrm w}\le2n_c-2$, or $q_{\mathrm w}=\infty$ with $p=1$. (3) If
    $q_{\mathrm w}\le2n_c-1$, then
    $q_{\mathrm w}+\lfloor(p+1+\delta_{\mathrm{SA}})/2\rfloor\le s+n_c$.
    **Proved**
12. DIRK (Thm 3.2): if $q_{\mathrm w}\le2n_c-1$, then
    $\lfloor(q_{\mathrm w}+\delta_{\mathrm{GE}})/2\rfloor-\delta_{\mathrm{GE}}+p\le s+1-\delta_{\mathrm{SA}}$.
    At $q_{\mathrm w}=0$ it gives back the classical DIRK barrier $p\le s+1$.
    **Proved**
13. Remark 3.3 as printed: "When $p=s+1-\sigma$" DIRKs are limited to
    $q_{\mathrm w}\le3$ and GEDIRKs to $q_{\mathrm w}\le4$; decreasing $p$ by 1
    raises the bound on $q_{\mathrm w}$ by 2; schemes attaining the barriers
    exist (§7). **Derived** (the stated numbers correspond to
    $p=s-\delta_{\mathrm{SA}}$, see Printed slips)
14. Both theorems hold when only $R(z)=e^z+O(z^{p+1})$ is assumed
    (Remark 3.6). **Stated**
15. $R=N/D$ with $\deg N,\deg D\le\dim\mathcal Y$ (Thm 3.8). **Proved**
16. $\lfloor(p+1+\delta_{\mathrm{SA}})/2\rfloor\le\dim\mathcal Y$ for any
    Runge–Kutta method, and $p\le\dim\mathcal Y+1-\delta_{\mathrm{SA}}$ for a
    DIRK (Thm 3.9, Eqs. (17)–(18), via the Padé barrier
    $p\le\deg N+\deg D$ and the Nørsett–Wolfbrandt real-pole barrier
    $p\le\deg N+1$). **Proved**
17. A sandwich of $A$-invariant spaces,
    $W_m\subseteq\mathrm{span}_A(W_m)\subseteq\mathcal K_m\subseteq\mathrm{span}_A(V)$
    for $m\ge n_c+1$, where $V$ is spanned by powers of $c$ (Lemma 3.10).
    **Proved**
18. $\dim\mathcal K_m\ge\max\{m-n_c,0\}$ for $m\le2n_c-1$. When all
    $c_j\ne0$ and $m\ge2n_c$, $\mathbf 1\in\mathcal K_m$. When some $c_j=0$
    and $m\ge2n_c-1$, $c\in\mathcal K_m$ (Thm 3.11). **Proved**
19. For a DIRK,
    $\dim\mathcal K_m\ge\min\{\lfloor(m+\delta_{\mathrm{GE}})/2\rfloor,n_c-\delta_{\mathrm{GE}}\}$
    (Lemma 3.13, Eq. (25)). **Proved**
20. Minimal polynomials: $b^\top \mu_{\mathcal Y}(A)=0$ with $\deg\mu_{\mathcal Y}=\dim\mathcal Y$. If
    $q_{\mathrm w}\ge2$, then $\mu_{\mathcal K}(A)\tau^{(k)}=0$ for
    $k=2,\dots,q_{\mathrm w}$, with
    $\deg\mu_{\mathcal K}\le\dim\mathcal K_{q_{\mathrm w}}$ and $\mu_{\mathcal K}\mu_{\mathcal Y}\mid\det(xI-A)$. The
    eigenvalues of $A$ split into roots of $\mu_{\mathcal K}$, roots of $\mu_{\mathcal Y}$ and a remainder
    (Lemma 4.4, Remark 4.6). **Proved**
21. $\deg\mu_{\mathcal K}\le\dim\mathcal K_{q_{\mathrm w}}\le s-\lfloor(p+1+\delta_{\mathrm{SA}})/2\rfloor$
    for fully implicit methods. For DIRKs the bound is printed
    "$s-p-1+\sigma$", whereas the derivation gives
    $s-p+1-\delta_{\mathrm{SA}}$ (Cor. 4.5). **Proved** (with a printed slip)
22. The Hankel matrices of the moments $\mu_n=1/(n+1)!$ are all nonsingular
    (closed form (48), proved with the Desnanot–Jacobi identity). The monic
    orthogonal polynomials $Q_j$ therefore exist, with
    $Q_{n+1}=xQ_n+\xi_n^2Q_{n-1}$ and $\xi_n^2=1/(4(4n^2-1))$. The
    functional is not positive-definite and the $Q_j$ have complex roots
    (§5, Eq. (33), Remark 5.3, App. B). **Proved**
23. Writing $Q=Q_d+\sum_{j<d}\alpha_jQ_j$ with $d=\dim\mathcal Y$, order $p$
    forces $\alpha_j=0$ for $j\le p-d-1$, and $p\le2d$ (Lemma 5.1).
    **Proved**
24. If $p\ge\dim\mathcal Y$, then $R(z)=1+z\beta_0(z)$, with $\beta_0$
    obtained by Cramer's rule from a tridiagonal system that depends only on
    $\alpha_j$, $j=p-\dim\mathcal Y,\dots,\dim\mathcal Y-1$ (Lemma 5.2,
    Eqs. (37)–(39)). **Proved**
25. For a DIRK that is not a GEDIRK, with $q_{\mathrm w}\ge2$ and distinct
    $c_1,\dots,c_r$, $r\le\lfloor q_{\mathrm w}/2\rfloor$, the minimal
    polynomial of the leading $r\times r$ block of $A$ divides $\mu_{\mathcal K}$
    (Lemma 6.1, Cor. 6.2). **Proved**
26. For an S-irreducible DIRK that is not a GEDIRK, with invertible leading
    $3\times3$ block: $q_{\mathrm w}>1$ makes $a_{11}$ a root of $\mu_{\mathcal K}$;
    $q_{\mathrm w}>3$ makes $a_{11}$ and $a_{22}$ roots; $q_{\mathrm w}>5$
    makes the minimal polynomial of the leading $3\times3$ block divide $\mu_{\mathcal K}$.
    For a DJ-irreducible DIRK, $a_{ss}$ is a root of $Q$ (Lemma 6.5,
    Remark 6.6). **Proved**
27. Any DIRK with $c_1=c_2$ is S-reducible (Remark 6.4). **Proved** (sketch)
28. The DIRKs with $(s,p,q_{\mathrm w})=(2,2,3)$ are exactly two schemes
    (Eq. (44)), with $a_{22}=\frac12$ and $R(z)=(1+z/2)/(1-z/2)$
    (Example 7.1). **Derived**
29. The DIRKs with $(s,p,q_{\mathrm w})=(3,3,3)$, sharp for Thm 3.2, form a
    one-parameter family in $a$. No $a$ gives $p=4$ or $q_{\mathrm w}=4$, and
    $0<a<\frac23$ or $a>1$ is needed for positive eigenvalues of $A$
    (Example 7.2). **Derived**
30. The eigenvector criterion of Rosales et al. and Ketcheson et al. limits
    DIRKs with invertible $A$ to $q_{\mathrm w}\le3$ (§1.2). **Stated**
    (asserted, not proved as a separate result)

# Printed slips

All checked against the rendered pages of arXiv v2.

- Remark 3.3 (p. 6): "When $p=s+1-\sigma$, Theorem 3.2 implies that DIRK
  schemes are limited to WSO $q\le3$, with the exception of GEDIRK schemes
  which are limited to WSO $q\le4$." Substituting $p=s+1-\sigma$ into
  Thm 3.2 gives $q_{\mathrm w}\le1$ (DIRK) and $q_{\mathrm w}\le2$ (GEDIRK).
  The stated values follow from $p=s-\sigma$, consistent with Example 7.2.
- Corollary 4.5 (p. 14): the DIRK bound is printed "$s-p-1+\sigma$". The
  derivation from (14) and (18) gives $s-p+1-\sigma$. The printed bound is
  $-1$ for Examples 7.1 and 7.2, where $\dim\mathcal K_{q_{\mathrm w}}=1$.
- Proof of Thm 3.1 (p. 11) is headed "(Of the Main Result Theorem 3.2)"
  and assigns parts (1)–(2) to Theorem 3.2; they belong to Theorem 3.1.
- Proof of Thm 3.2 (p. 12): "When $q\ge2n_c-1$", while the hypothesis is
  $q\le2n_c-1$.
- Truncation map (p. 11): "to isolate the top $s$ components of $\vec c$"
  should read "top $j$".
- Proof of Lemma 6.5(c) (p. 19): case (ii) reads "if $c_j=0$", where
  Thm 3.11(b) requires $c_j\ne0$.
- §2.3 (p. 5): "$z\vec b^T(I-zA)\vec\tau^{(k)}$" — the inverse is missing.
- Example 7.3 (p. 20): "The bound in Theorem 3.1 can be sharp" for the
  stiffly accurate (4,3,3) DIRKs; the sharp bound for these is Theorem 3.2.
  The same example also writes "a-posteriorily".
- Theorem 3.9 (p. 8): "If the scheme is diagonally implicit, (17) we have
  the stronger bound" (garbled).
- Lemma 4.4 proof (p. 14): "$k=1,\dots,q$" where (29) has $k=2,\dots,q$
  (harmless, since $\tau^{(1)}=0$).
- Duplicates in the printed reference list: [4]=[5] (Alonso-Mallo &
  Palencia 2003) and [12]=[13] (Calvo & Palencia 2002).
- Typos: "Carnegie Melon", "explicitly construction", "the the basis".
- Scope inconsistency: the abstract and §8 restrict the weak-stage-order
  remedy to "linear problems with time-independent operators", while §1.1
  says "linear (possibly time-dependent) operator".

# Notation map

| Biswas et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\Delta t$, $u_n$, $u'=f(t,u)$ | $h$, $y_n$, $y'=f(t,y)$ | |
| $g_i$ | $Y_i$ | stage values |
| $A$, $\vec b$, $\vec c$, $\vec e$ | $A$, $b$, $c$, $\mathbf 1$ | $c=A\mathbf 1$ assumed |
| $C$ | $\mathrm{diag}(c)$ | collides with $C(\xi)$ inside the source |
| $\vec\tau^{(k)}$ | $\tau^{(k)}$ | agrees |
| **$\tilde q$** | $q$ | **collision: the source's stage order is $\tilde q$** |
| **$q$** | $q_{\mathrm w}$ | **collision: the source's $q$ is the weak stage order** |
| **$S(\xi)$** | condition $q_{\mathrm w}\ge\xi$ | **collision with $S(\xi)$ of [Biswas et al. (2023)](/sources/biswas-2023.md), Albrecht's condition** |
| $B(\xi)$, $C(\xi)$ | $B(\xi)$, $C(\xi)$ | agrees |
| $z=\lambda\Delta t$, $R(z)=N/D$ | $z=h\lambda$, $R(z)$ | |
| **$Y$** | $\mathcal Y$ | **collision with stage values $Y_i$**; registry symbol for the smallest $A^\top$-invariant space containing $b$ |
| **$K_m$** | $\mathcal K_m$ | **collision with $K$ (correction iterations)**; registry symbol |
| $K(X)$ | $\mathrm{span}_A(X)$ | smallest $A$-invariant space containing $X$, page-local |
| **$\sigma$** | $\delta_{\mathrm{SA}}$ | **collision with tree symmetry $\sigma(\tau)$** |
| $\kappa$ | $\delta_{\mathrm{GE}}$ | GEDIRK indicator, page-local |
| $n_c$ | $n_c$ | number of distinct abscissae; agrees with the registry |
| $P(x)$, $Q(x)$ | $\mu_{\mathcal K}$, $\mu_{\mathcal Y}$ | minimal polynomials of $\mathcal K_{q_{\mathrm w}}$ and $\mathcal Y$, page-local as on [weak-stage-order barriers](/results/weak-stage-order-barriers.md); **collision: registry $P(z)$ is the stability polynomial** |
| **$p_j(x)$** | — | **collision with the order $p$**; minimal polynomial of the leading $j\times j$ block |
| $\mathrm{char}_A$ | $\det(xI-A)$ | |
| $N(x)$ (Remark 4.6) | — | remainder factor; also the numerator $N(z)$ of $R$ |
| $W_k(z)$, $\tilde W_k(z)$ | — | Prothero–Robinson and Ostermann–Roche functions |
| $\phi(t)$, $\lambda$ | $g(t)$, $\lambda$ | Prothero–Robinson solution; $\phi$ collides with $\phi_k$ |
| $L$, $\mu_n$, $Q_j$, $\xi_n$, $\zeta_i$ | — | moment functional, moments, orthogonal polynomials; $L$ collides with the linear operator |
| $\gamma$ | $\gamma$ | SDIRK diagonal; agrees with the Rosenbrock/diagonal meaning |

# Reference list

The paper prints 44 references in numbered style, alphabetical by first
author. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` biswas-2024, as 42 entries: the two printed duplicates
[4]=[5] and [12]=[13] are folded into one entry each (`alonsomallo-2003`,
`calvo-2002`). Ref. [7] is "In Press" with an
arXiv number, refs. [38] and [39] are arXiv preprints, and ref. [25] is a
MathOverflow post (version of 2017-04-13); all are their own entries. Ref.
[17] is a chapter in an edited volume. No DOIs are printed.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [B-convergence](/definitions/b-convergence.md)
* [Diagonally implicit Runge–Kutta methods (DIRK, SDIRK, ESDIRK)](/methods/diagonally-implicit-runge-kutta.md)
* [DIRK schemes with high weak stage order](/methods/dirk-high-weak-stage-order.md)
* [Fully implicit collocation Runge–Kutta methods (Gauss, Radau IIA, Lobatto IIIC)](/methods/fully-implicit-runge-kutta.md)
* [Order reduction](/definitions/order-reduction.md)
* [Prothero–Robinson problem](/benchmarks/prothero-robinson-problem.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stage order](/definitions/stage-order.md)
* [Stiff accuracy](/properties/stiff-accuracy.md)
* [Weak stage order](/definitions/weak-stage-order.md)
* [Weak-stage-order barriers](/results/weak-stage-order-barriers.md)
