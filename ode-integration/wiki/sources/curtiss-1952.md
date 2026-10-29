---
type: Source
title: "Curtiss & Hirschfelder (1952) — Integration of stiff equations"
description: "Calls stiff the equations dy/dx = (y − G)/a with |a/Δx| ≪ 1 and a slowly varying G, and introduces 'forward interpolation', the backward differentiation formulas of orders 1 to 4, which the authors state converge onto the smooth solution from any start and in either direction of integration."
resource: "doi:10.1073/pnas.38.3.235"
source_kind: paper
authors: [Curtiss C.F., Hirschfelder J.O.]
year: 1952
venue: "Proc. Natl. Acad. Sci. USA 38(3):235-243"
local_file: "/home/stefano/papers/mosaic/ode-integration/1952_Crossref_Proceedings_of_the_National_Academy_of_Sciences_Curtiss_Integration_of_Stiff_Equations.pdf"
tags: [stiff, bdf, linear-multistep, implicit, stability]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

The paper names and defines [stiffness](/definitions/stiffness.md). Its
motivation is chemical kinetics (free radicals in flames and detonations,
where the pseudo-stationary-state approximation is not accurate enough),
electrical circuit theory and missile guidance. The model problem is the
scalar equation $y'=(y-G(t))/a(t,y)$ (Eq. (1)). It is called stiff when
$\lvert a/h\rvert\ll1$ for the step $h$ one wants to use and $G$ varies much
more slowly than $\exp(t/a(t,G(t)))$ (Eq. (2)). The definition is relative to
the step. Near $y=G$ lies a smooth special solution $Y(t)$, given by a series
in the operator $a\,d/dt$ (Eqs. (3)–(5)). Every other solution departs from it
exponentially (Eqs. (6)–(7)). Ordinary methods magnify small errors in the
direction in which the solutions "horn out" and oscillate violently about
$Y$ in the other direction (§2).

The remedy, called "forward interpolation", evaluates the right-hand side at
the new point $t_n$ and replaces $y'(t_n)$ by the derivative of the
polynomial through $y_n,y_{n-1},\dots$: the straight line (Eq. (10)), the
quadratic (Eq. (17)), the cubic (Eq. (20)) and the quartic (Eq. (22)). These
are the [backward differentiation formulas](/methods/backward-differentiation-formula.md)
BDF1–BDF4, a family of implicit
[linear multistep methods](/methods/linear-multistep-method.md) (compiler
check below). The authors state that, whatever the starting point and the
direction of integration, the numerical solution converges rapidly to $Y$. A
geometric argument credited to C. Buck explains it (Fig. 3), and for $a=a(t)$
error recursions with a convergence factor $b$ (Eq. (15)) and asymptotic
errors proportional to $a$ follow (Eqs. (12)–(16), (18)–(19), (21), (23)).
The factor $b$ decreases as $h$ grows. The evidence is formal series, Taylor
expansions and two graphical integrations of $y'=5(y-t^2)$ (Figs. 3–4). The
paper prints no theorem, no table and no reference list. It has no
eigenvalue, stability-region or [A-stability](/properties/a-stability.md)
concept.

# Version read

Version of record, a scan of PNAS pp. 235–243 (9 PDF pages) downloaded from
pnas.org; "Communicated by Farrington Daniels, December 29, 1951". The
article starts mid-p. 235 and ends at the top of p. 243. Footnotes 10–13 at
the top of p. 235 belong to the preceding article, and the text below the
acknowledgments on p. 243 is the next article (V. Hlavatý). The text layer
is OCR of a scan; every page with equations was read visually. Title and
authors agree with the Crossref record. The DOI and the issue number (3)
are not printed on the pages read. Equation and figure numbers are those of
the paper (Eqs. (1)–(23), Figs. 1–4).

# Key claims

Registry notation: $t$ for the paper's $x$, $h$ for its $\Delta x$ (which may
be negative: its sign is the direction of integration); $G$, $a$, $Y$, $b$
and $\epsilon$ are page-local (see the notation map).

1. Equations of a particular type, arising in chemical kinetics, electrical
   circuit theory and missile guidance, are "exceedingly difficult to solve
   by ordinary numerical procedures"; the equations to which the method
   applies "are called 'stiff'" (Introduction, p. 235). **Stated**
2. Definition: $y'=(y-G(t))/a(t,y)$ (Eq. (1)) is stiff if
   $\lvert a(t,y)/h\rvert\ll1$ (Eq. (2)) "and $G(x)$ is well behaved", i.e.
   varies considerably more slowly than $\exp(t/a(t,G(t)))$, where $h$ is
   "the desired resolution of $x$ or the interval which will be used in the
   numerical integration" (§1, p. 236). **Stated**
3. For $y'=5(y-t^2)$ the solutions "horn out" in the positive $t$ direction,
   which "can be chosen as the positive $x$ direction without loss of
   generality" (§1, Fig. 1). **Shown** (direction field)
4. For small $a$ a special solution $Y$ close to $G$ is obtained by successive
   approximation $Y^{(1)}=G+a(t,G)G'$, $Y^{(2)}=G+a(t,Y^{(1)})Y^{(1)\prime}$,
   … (Eqs. (3)–(4)); for $a=a(t)$, $Y=\sum_{k\ge0}(a\,d/dt)^kG$ (Eq. (5))
   (§1). **Derived**
5. Near $Y$, with $a$ varying slowly with $y$,
   $y-Y=C\exp\bigl[\int dt/a(t,Y(t))\bigr]$ (Eqs. (6)–(7), Fig. 2): every
   other solution deviates from $Y$ exponentially (§1). **Derived**
6. With ordinary methods "small errors are rapidly magnified if the
   equations are integrated in the direction such that the family of
   solutions horn out, whereas the numerical solutions oscillate violently
   about $Y(x)$ if the integration is carried out in the opposite direction"
   (§2, pp. 237–238). **Stated**
7. The authors "have discovered a method … which has the desirable property
   that regardless of the starting conditions and regardless of the
   direction of integration, a solution is generated which rapidly converges
   to $Y(x)$" (§2, p. 238). **Stated**; illustrated graphically in
   Figs. 3–4. **Shown**
8. The linear (two-point) step sets $y'(t_n)=(y_n-y_{n-1})/h=(y_n-G_n)/a$
   (Eqs. (8)–(9)), so
   $y_n=\bigl[G_n-\frac{a(t_n,y_n)}{h}y_{n-1}\bigr]\big/\bigl[1-\frac{a(t_n,y_n)}{h}\bigr]$
   (Eq. (10)). It is explicit in $y_n$ when $a$ does not depend on $y$ and an
   implicit relation otherwise (§2, pp. 239–240). **Derived**
9. Equating the two slopes of Eqs. (8)–(9) is equivalent to choosing the
   exact solution of (1) whose tangent at $t_1$ passes through
   $(t_0,y_0)$; since the slope of a stiff equation is moderate only near $G$
   or $Y$, the scheme "limits us to approximating $Y(x)$" (§2, p. 240,
   Fig. 3; interpretation credited to Creighton Buck). **Derived**
   (geometric argument)
10. In the negative direction ("the direction of convergence of the manifold
    of solutions") the solution approaches the asymptote "without
    oscillations" (Fig. 4). The integration "is not reversible since the
    definition of the forward point depends upon the direction of
    integration", which "may be used numerically to hunt the special
    solution" by integrating in one direction and then reversing it (§2,
    p. 240). **Stated** / **Shown** (graphically)
11. For $a=a(t)$ the error obeys
    $y_n-Y_n=-b\,[y_{n-1}-Y_{n-1}+\epsilon]$ with
    $b=\frac{a(t_n)/h}{1-a(t_n)/h}$ (Eqs. (12), (15)) and
    $\epsilon=-Y_n+Y_{n-1}+hY'(t_n)=\frac12h^2Y''(t_{n-1})+\frac13h^3Y'''(t_{n-1})+\dots$
    (Eqs. (13)–(14)) (§3). **Derived**
12. "The larger the interval size, $\Delta x$, the smaller the value of $b$
    and the more rapidly $y_n$ converges toward $Y_n$. The series converges
    for values of $b$ less than unity and approaches an asymptote given
    approximately by" $y=Y+a(t)\bigl[\frac12hY''+\frac13h^2Y'''+\dots\bigr]$
    (Eq. (16), p. 241). **Derived** (see Printed slips for the sign)
13. The asymptotic discrepancy "is due to the poorness of the fit of $Y$ by
    successive linear segments. The smaller the intervals, $\Delta x$, the
    smaller this error" (§3, p. 241). **Stated**
14. With $r=a(t_n,y_n)/h$ (page-local), the quadratic fit gives
    $y_n=\bigl[G_n-2ry_{n-1}+\frac12ry_{n-2}\bigr]/\bigl[1-\frac32r\bigr]$
    (Eq. (17)), the cubic
    $y_n=\bigl[G_n+r(-3y_{n-1}+\frac32y_{n-2}-\frac13y_{n-3})\bigr]/\bigl[1-\frac{11}6r\bigr]$
    (Eq. (20)) and the quartic
    $y_n=\bigl[G_n+r(-4y_{n-1}+3y_{n-2}-\frac43y_{n-3}+\frac14y_{n-4})\bigr]/\bigl[1-\frac{25}{12}r\bigr]$
    (Eq. (22)), with error recursions (18), (21), (23) for $a$ independent
    of $y$ (footnote 1) and the quadratic asymptote
    $y=Y+a(t)\bigl[\frac29h^2Y'''+\frac1{18}h^3Y''''+\dots\bigr]$ (Eq. (19))
    (§3, pp. 241–242). **Derived**. The leading truncation terms printed in
    (14), (18), (21), (23) have coefficients $\frac12$, $-\frac13$,
    $-\frac14$, $-\frac15$.
15. "By taking higher order polynomials to fit $y$ at a large number of
    points, it is possible to obtain progressively more excellent fits of
    $Y$. In all cases, the use of forward interpolation in the evaluation of
    $(dy/dx)_n$ in terms of $y_n,y_{n-1},\dots$ is the mathematical
    operation which forces $y_n$ to seek out and approximate $Y_n$" (§3,
    p. 242). **Stated**
16. Systems: "The numerical procedure described here can easily be extended
    to sets of simultaneous first-order differential equations. In any
    particular region, the differential equations can be uncoupled by
    introducing suitable linear combinations of the original dependent
    variables"; the stiff uncoupled equations are integrated by this method
    and the others "by the more usual procedures" (Introduction, p. 235). No
    formula or example. **Stated**
17. The method "provides a means for obtaining solutions to equations of
    this type to any degree of accuracy", where the pseudo-stationary-state
    approximation is not accurate enough "in flames or detonations"
    (Introduction, p. 235). **Stated**

*(Compiler check, not in the sources.)* Multiplying out Eqs. (10), (17),
(20), (22) gives $\sum_j\alpha_jy_{n-j}=hf(t_n,y_n)$ with
$(\alpha_0,\alpha_1,\dots)=(1,-1)$, $(\frac32,-2,\frac12)$,
$(\frac{11}6,-3,\frac32,-\frac13)$, $(\frac{25}{12},-4,3,-\frac43,\frac14)$
(indices counted backwards from $t_n$): the BDF$k$ coefficients, $k=1,\dots,4$,
in the normalization $\sigma(\zeta)=\zeta^k$ of the
[BDF page](/methods/backward-differentiation-formula.md).

# Printed slips

- Eq. (9) prints $a(y_n,x_n)$; Eqs. (1), (10), (17), (20), (22) print the
  argument order $a(x,y)$, $a(x_n,y_n)$.
- Eq. (14): the second-derivative term carries the subscript $n-1$, the
  third-derivative term $x_{n-1}$.
- Eq. (16), sign. *(Compiler check, not in the sources.)* A constant
  asymptotic error $e$ in Eq. (12) satisfies $e=-b(e+\epsilon)$, so
  $e=-\frac b{1+b}\epsilon=-\frac a h\epsilon=-a\bigl[\frac12hY''+\frac13h^2Y'''+\dots\bigr]$
  by Eqs. (14)–(15), the opposite sign to the printed
  "$y=Y+a(x)[\dots]$".
- Eq. (19), sign and factor. *(Compiler check, not in the sources.)* A
  constant $e$ in Eq. (18) satisfies
  $e(1-\frac32r)=r(-\frac32e+L)$ with
  $L=-\frac13h^3Y'''-\frac1{12}h^4Y''''$, so
  $e=rL=-a\bigl[\frac13h^2Y'''+\frac1{12}h^3Y''''\bigr]$; the printed
  coefficients are $+\frac29$ and $+\frac1{18}$.
- Eq. (23): the third bracket term is printed
  "$-\frac43(y_{n-2}-Y_{n-2})$", while in Eq. (22) the coefficient
  $-\frac43$ multiplies $y_{n-3}$. *(Compiler check, not in the sources:
  subtracting the equation for $Y$ from (22) gives
  $-4e_{n-1}+3e_{n-2}-\frac43e_{n-3}+\frac14e_{n-4}$ with $e_m=y_m-Y_m$.)*
- Eq. (21): a stray dot after $(d^4Y/dx^4)$ in the remainder.
- p. 242: the callout "given by²" before Eq. (21) has no footnote 2 printed
  on pp. 242–243.
- p. 241: "The series converges for values of $b$ less than unity" is
  printed without a modulus. *(Compiler check, not in the sources: for
  Fig. 4, $a/h=-\frac15$, Eq. (15) gives $b=-\frac16$.)*

# Notation map

| Curtiss & Hirschfelder (1952) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$ | $t$ | independent variable |
| $y(x)$, $y_n$ | $y(t)$, $y_n$ | scalar; systems only mentioned (claim 16) |
| $\Delta x$ | $h$ | "interval"; may be negative (direction of integration) |
| $x_n$, $G_n$ | $t_n$, $G(t_n)$ | $n$ is the new ("forward") point |
| $G(x)$ | — | root of the right-hand side, page-local |
| $a(x,y)$ | — | page-local coefficient, right-hand side $(y-G)/a$; **printed $a(y_n,x_n)$ in Eq. (9)** |
| $a(x_n,y_n)/\Delta x$ | $r$ | page-local abbreviation of this page, not the paper's |
| $Y(x)$, $Y^{(k)}$ | — | special smooth solution and its successive approximations, page-local |
| $D/Dx=a(x)\,d/dx$ | — | operator of Eq. (5) |
| $S_0(x)$, $S_1(x)$ | — | exact solutions through grid points (Fig. 3) |
| $C$ | — | integration constant of Eq. (7) |
| $\epsilon$ | — | defect of $Y$ in the linear scheme, Eq. (13); **not the registry $\varepsilon$ (stiffness parameter)** |
| $b$ | — | convergence factor, Eq. (15); **collision with the registry weights $b$** |
| $y_m-Y_m$ | $e_m$ | page-local error symbol of this page |
| "stiff" | [stiffness](/definitions/stiffness.md) | Eq. (2): $\lvert a/\Delta x\rvert\ll1$ and slowly varying $G$ |
| "forward interpolation" | [BDF](/methods/backward-differentiation-formula.md) | slope at the forward (new) point from the polynomial through $y_n,y_{n-1},\dots$; "forward" names the new point, not a forward difference |
| linear / three-point / cubic / quartic | BDF$k$, $k=1,\dots,4$ | polynomial through $k+1$ points |

# Reference list

The paper prints no reference list and cites no published work. Its
footnotes are the funding note (*), footnote 1 (the assumption that $a$ is
independent of $y$) and the unprinted footnote 2 (callout only). Footnotes
10–13 at the top of p. 235 belong to the preceding PNAS article and are not
this paper's references. Nothing is merged into the
[bibliography](/bibliography.md), so no entry carries `citedby`
curtiss-1952 and `python3 tools/bib_to_md.py ode-integration/wiki --pending`
keeps listing this source; the empty list is recorded here.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [B-convergence](/definitions/b-convergence.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Order reduction](/definitions/order-reduction.md)
* [Stiffness](/definitions/stiffness.md)
