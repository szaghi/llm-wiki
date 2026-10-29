---
type: Source
title: "Dormand & Prince (1980) — A family of embedded Runge-Kutta formulae"
description: "Derives a four-parameter family of explicit embedded fifth/fourth-order Runge–Kutta pairs run in local extrapolation, seven stages with the last equal to the first of the next step, and prints RK5(4)7M (minimum truncation error), RK5(4)7S (extended stability) and the six-stage RK5(4)6M, tested on DETEST against Fehlberg's RKF4."
resource: "doi:10.1016/0771-050X(80)90013-3"
source_kind: paper
authors: [Dormand J.R., Prince P.J.]
year: 1980
venue: "J. Comput. Appl. Math. 6(1):19-26"
local_file: "/home/stefano/papers/mosaic/ode-integration/1980_Crossref_Journal_of_Computational_and_Applied_Mathematics_Dormand_A_family_of_embedded_Runge-Kutta_formulae.pdf"
tags: [runge-kutta, explicit, embedded-pair, step-size-control, order-conditions]
timestamp: 2026-10-29T18:00:00Z
---

# Summary

The paper derives explicit [embedded Runge–Kutta pairs](/methods/embedded-runge-kutta-pair.md)
RK5(4): a fifth-order formula and a fourth-order formula that share their
function evaluations. The pairs are designed for local extrapolation: the
fifth-order solution is propagated and the difference of the two solutions
estimates the error. The family has seven stages, the seventh evaluated at
the new solution, so that it equals the first evaluation of the next step
($c_7=1$, $a_{7j}=b_j$, $b_7=0$, Eq. (2.1); the term "FSAL" is not used).
After the first step this costs six evaluations per step, plus one lost
evaluation after each rejected step. The fifth-order formula uses six
stages and the fourth-order one all seven.

Simplifying assumptions (2.2)–(2.3) and $b_2=\hat b_2=0$ reduce the 25
[order conditions](/results/runge-kutta-order-conditions.md) (17 of order
5, 8 of order 4) to 11 independent equations, solved in closed form. Four
free parameters remain, $c_3$, $c_4$, $c_5$ and the embedded weight
$\hat b_7$. They are chosen for (a) a small 2-norm of the sixth-order
truncation-error coefficients of the fifth-order formula, given in closed
form (3.1), and (b) extended regions of absolute stability of both
formulas, whose [stability polynomials](/definitions/stability-function.md)
are given in (3.2)–(3.3). Three pairs are printed. RK5(4)7M (Table 2) is the
[Dormand–Prince 5(4) pair](/methods/dormand-prince-5-4.md), with error norm
$3.99\times10^{-4}$, "about 8 times" smaller than for Fehlberg's RKF4.
RK5(4)7S (Table 3) has larger stability regions. RK5(4)6M (Table 4) has six
stages and is sixth order on quadrature problems.

Section 4 runs the DETEST set of Hull et al. over seven tolerances with a
modified DETEST that measures the maximum global error (Table 5), and shows
efficiency curves for problem A3 and for the two-body problem D5 with
eccentricity 0.9, a [Kepler problem](/benchmarks/kepler-problem.md) on which
the step varies by about two orders of magnitude, a severe test of
[step-size control](/methods/step-size-control.md). The conclusion is that
the minimum-truncation-error formula is the most efficient, and that the
seventh evaluation buys either smaller truncation terms or a high-stability
pair.

# Version read

Version of record, a scan of J. Comput. Appl. Math. 6(1), pp. 19–26 (8
pages), with no received or accepted dates. The text layer is garbled in
every equation; all formulas and the three tableaux were read visually.
Title and authors agree with the Crossref record; the DOI is not printed.
Equation and table numbers are those of the paper. The pair name
"Dormand–Prince 5(4)" is later usage; the paper calls the pair RK5(4)7M.

# Key claims

Registry notation, with the hat convention **reversed** with respect to
the paper: $b$, $y_{n+1}$ are the propagated fifth-order weights and
solution (the paper's $\hat b$, $\hat y$), $\hat b$, $\hat y_{n+1}$ the
embedded fourth-order ones (the paper's $b$, $y$). $t$ for the paper's $x$;
stage derivatives $f(Y_i)$ for its $k_i/h_n$. $E^{(r)}_i$ (fifth-order
formula) and $\hat E^{(r)}_i$ (fourth-order formula) are page-local names
for the paper's truncation-error coefficients $\hat a^{(r)}_i$ and
$a^{(r)}_i$ (notation map).

1. A family of embedded RK5(4) formulas is derived, and from it formulas
   with "small" principal truncation terms in the fifth order and with
   extended regions of absolute stability (Abstract). **Derived**
2. Local extrapolation ("RKq(p) instead of RKp(q) mode"), "which practical
   results indicate is preferable" (refs. [5], [6]), propagates the
   higher-order solution; both formulas start from it (Eq. (1.6), §1).
   **Stated**
3. Two "widely used" step-size formulas (ref. [4]), with $\delta$ the
   maximum allowable local error and $p$ the lower order:
   $h_{n+1}=0.9h_n[\delta/\lVert\hat y_{n+1}-y_{n+1}\rVert_\infty]^{1/(p+1)}$
   (error per step) and
   $h_{n+1}=0.9h_n[\delta/\lVert(\hat y_{n+1}-y_{n+1})/h_n\rVert_\infty]^{1/p}$
   (error per unit step) (§1). **Stated**
4. Fehlberg's pairs make the principal truncation term of the lower-order
   formula small; "since this term gives the local error estimate an
   artificially small term could lead to poor step size control (see
   [11])" (§1). Yet "practical tests [8]" indicate good results for the
   lower-order mode when the error coefficients are made as small as
   possible, "in spite of our comments in section 1" (§3). **Stated**
5. "It is common practice that the higher order formula uses more stages
   than the lower order formula but in this work we shall also allow the
   converse to be true" (§1). The fifth-order conditions involve stages 1
   to 6, the fourth-order ones stages 1 to 7 (§2). **Stated**
6. The seventh stage is the first evaluation of the next step: $b_7=0$,
   $c_7=1$, $a_{7j}=b_j$, $j=1,\dots,6$ (Eq. (2.1)); "After the first step
   the effective number of function evaluations per step is still six
   although one extra function evaluation is lost after any step
   rejection" (§2). The device is credited to refs. [9] (Fehlberg 1972) and
   [11] (Dormand & Prince 1978). **Stated**
7. Under (2.2) $\sum_{i=1}^6b_ia_{ij}=b_j(1-c_j)$, $j=1,\dots,6$,
   $b_2=\hat b_2=0$, and (2.3) $\sum_ja_{ij}c_j=\frac12c_i^2$,
   $\sum_ja_{ij}c_j^2=\frac13c_i^3$, $i=3,\dots,6$, three of which are
   dependent (ref. [10]), the 25 conditions reduce to 11 independent ones
   (§2). **Derived**
8. Closed-form solution: $c_6=1$ follows from (2.2); $b_3,\dots,b_6$ are
   given by (2.6), e.g.
   $b_3=\frac{3-5(c_4+c_5)+10c_4c_5}{60c_3(1-c_3)(c_3-c_4)(c_3-c_5)}$;
   $c_2=\frac23c_3$, $a_{32}=\frac34c_3$,
   $a_{42}=3c_4^2(3c_3-2c_4)/(4c_3^2)$, $a_{43}=c_4^2(c_4-c_3)/c_3^2$; the
   remaining $a_{ij}$ follow in sequence. The embedded weights
   $\hat b_3,\dots,\hat b_6$ follow from three order conditions and (2.5)
   "given a value for $b_7$ which is arbitrary" (registry $\hat b_7$), the
   parameter that "tunes" the embedded process (§2, §3). **Derived**
9. The sixth-order error coefficients of the fifth-order formula satisfy 19
   linear relations to four of them, given in closed form (3.1):
   $E^{(6)}_1=\frac{\{2-3(c_3+c_4)+5c_3c_4\}-c_5\{3-5(c_3+c_4)+10c_3c_4\}}{7200}$,
   $E^{(6)}_6=\frac{(1-2c_3)-c_4(2-5c_3)}{720}$,
   $E^{(6)}_8=\frac{\{2-3c_4(3-5c_3)\}-3c_5\{1-5c_4(1-2c_3)\}}{720}$,
   $E^{(6)}_{20}=\frac{3c_4(2-5c_3)-1}{720}$ (§3). **Derived**
10. $E^{(6)}_1=0$ makes the fifth-order formula sixth order for $y'=f(t)$
    (quadrature); $E^{(6)}_{20}=0$ makes it sixth order for $y'=Ly+g$ with
    constant $L$, $g$ (p. 22). **Derived**
11. Embedded pairs "such as those of Fehlberg [7] with $p>5$, and Dormand &
    Prince [11]" fail on quadrature problems, where both formulas give the
    same approximation and the error estimate is zero; Shampine's ref. [15]
    modified RKF7, but "it is preferable to develop formulae which are free
    from this deficiency" (p. 22). **Stated**
12. Stability polynomials for $y'=\lambda y$, region defined by $\lvert\cdot\rvert<1$:
    fifth-order formula $P(z)=\sum_{r=0}^5z^r/r!+\theta_6z^6$ with
    $\theta_6=E^{(6)}_{20}+1/6!=c_4(2-5c_3)/240$ (3.2); fourth-order formula
    $\hat P(z)=\sum_{r=0}^4z^r/r!+\hat\theta_5z^5+\hat\theta_6z^6+\hat\theta_7z^7$
    (3.3) (§3). **Derived**
13. RK5(4)7M: $c_3=\frac3{10}$, $c_4=\frac45$, $c_5=\frac89$,
    $\hat b_7=\frac1{40}$ (Table 2), error norm
    $\lVert E^{(6)}\rVert_2=3.99\times10^{-4}$, $\theta_6=\frac1{600}$,
    $\hat\theta_5=\frac{1097}{120000}$, $\hat\theta_6=\frac{161}{120000}$,
    $\hat\theta_7=\frac1{24000}$ (p. 23). **Derived**
14. "For RKF4 [8], which practical results ([5],[6]) indicate is preferable
    in local extrapolation mode, $\lVert\hat a^{(6)}\rVert_2=3.36\times10^{-3}$
    which is about 8 times larger than that for the RK5(4)7M" (p. 23).
    **Stated** (RKF4 coefficients not printed)
15. Lawson "has shown that an enlarged stability region is obtained if
    $d=1/1280$ giving $c_4=3/(16(2-5c_3))$" (p. 23; $d$ is $\theta_6$).
    **Stated**
16. "It can be argued [16] that high stability for the lower order formula
    is unnecessary when local extrapolation is used. However, an absolute
    stability failure on the lower order formula could cause severe problems
    in step size control, resulting in a loss of computational efficiency.
    Consequently it is preferable to make the stability region of the lower
    order formula comparable to that of the higher order formula"
    (pp. 23–24). **Stated**
17. RK5(4)7S: $c_3=\frac13$, $c_5=\frac23$, printed $c_4=\frac59$,
    $\lVert E^{(6)}\rVert_2=1.81\times10^{-3}$; the best $\hat b_7$ for
    comparable stability regions is $\frac1{150}$, but "this results in a
    poorly 'tuned' formulae pair and a compromised choice is $b_7=-1/50$"
    (Table 3, p. 24). **Derived**
18. The choice $\theta_6=1/1275$ gives two pairs,
    $(c_3,c_4)=(\frac2{13},\frac{13}{85})$ and $(\frac{16}{45},\frac{72}{85})$,
    both "unsuitable because they result in 'large' $a_{ij}$, $\hat b_i$
    and $b_i$ which are unsatisfactory with regard to rounding error"
    (p. 24). **Stated** (coefficients not printed)
19. With $\hat b_7=0$ the seventh evaluation is not needed, and the two
    weight vectors coincide unless the $4\times4$ matrix with rows
    $(c_3,c_4,c_5,1)$, $(c_3^2,c_4^2,c_5^2,1)$, $(c_3^3,c_4^3,c_5^3,1)$,
    $(a_{32},a_{42},a_{52},a_{62})$ is singular, which happens iff
    $c_4=c_3/(2(5c_3^2-4c_3+1))$ (second Eq. (3.3), ref. [17]); the embedded
    weights then follow from a tuning parameter $\hat b_6\neq b_6$
    (p. 24). **Derived**
20. RK5(4)6M: $c_3=\frac3{10}$, $c_5=\frac23$, tuning $\hat b_6=\frac1{20}$
    (Table 4), $\lVert E^{(6)}\rVert_2=1.23\times10^{-3}$; it "is sixth
    order for quadrature problems" (p. 24). **Derived**
21. Seven-evaluation pairs give an extra degree of freedom for a smaller
    error norm or extended stability, at the price of one evaluation lost
    after a rejected step, "but this seems to be worthwhile" (p. 24, §5).
    **Stated**
22. Table 5, DETEST over the tolerances $10^{-3-r}$, $r=0,\dots,6$ (FCN
    calls / steps / maximum error / fraction deceived / fraction bad
    deceived): RKF4 in 5(4) mode 226208 / 36363 / 12.4 / 0.005 / 0.000;
    RK5(4)7M 209305 / 33126 / 9.7 / 0.008 / 0.000; RK5(4)6M 267324 / 43394 /
    1.2 / 0.000 / 0.000; RK5(4)7S 186229 / 29158 / 15.2 / 0.027 / 0.001
    (§4). **Shown**
23. By the criteria of Hull et al., the "minimum truncation error" formulas
    RK5(4)7M and RK5(4)6M "are more efficient than the RKF4" (§4).
    **Shown** (criteria not defined in the paper)
24. Problem A3 ($y'=y\cos t$, $y(0)=1$, $t\in[0,20]$): "800 function
    evaluations being sufficient for a maximum global error (absolute) of
    $10^{-6}$, compared with 1450 for the RKF4 (in local extrapolation
    mode)" (§4(a), Fig. 2). **Shown**
25. Problem D5 (two-body, $e=0.9$, $t\in[0,20]$) "is a severe test for the
    step-size control procedure since the step length must vary by about two
    orders of magnitude"; RK5(4)7M is again the most efficient (§4(b),
    Fig. 3). **Shown**
26. Any of the pairs may be applied to a moderately stiff system, but the
    step is then set by the stability limit over the largest eigenvalue
    modulus of the Jacobian unless the tolerance is very small; RK5(4)7S
    "will permit a substantial reduction in computing time *provided* only
    a modest global error is required. If high accuracy is needed the
    RK5(4)7S offers no advantage" (§4). **Stated**
27. Conclusion: "the formula with the higher asymptotic applicability is
    most efficient" (§5). **Stated**

# Printed slips

- p. 23: "Lawson [12] has shown that an enlarged stability region is
  obtained if $d=1/1280$"; Lawson is ref. [13] (p. 22 prints "Following
  Lawson [13]"), and ref. [12] is Shampine & Watts.
- §4: "problems including those given by Hull et al. [3] in the DETEST
  implementation"; Hull et al. is ref. [4], ref. [3] is Harris.
- The number (3.3) is used twice: for the fourth-order stability region
  (p. 22) and for the singularity condition
  $c_4=c_3/(2(5c_3^2-4c_3+1))$ (p. 24).
- (2.5) is printed $\sum_{i=1}^6b_ia_{i2}=0$ for the seven-entry
  fourth-order weights (paper notation); the seventh term has
  $a_{72}=0$ by (2.1).
- §4(a) quotes a maximum global error of $10^{-6}$ for problem A3, while
  the $\log_{10}$(max global error) axis of Fig. 2 is labelled from $-1$ to
  $-4$. Fig. 3 labels its axis "log$_e$ (max global error)".

# Notation map

| Dormand & Prince (1980) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $\underline y(x)$ | $t$, $y(t)$ | underline marks vectors; autonomous form (1.2) used |
| $h$, $h_n=\theta(x_n)h$ | $h$, $h_n$ | maximum step and step $n$; **$\theta$ is not the registry stability-polynomial coefficient** |
| $\underline k_i=h_n\underline f(\cdot)$ | $h_nf(Y_i)$ | stage increments include the factor $h_n$ |
| $a_{ij}$, $c_i$ | $A$, $c$ | agree; $c=A\mathbf 1$ assumed |
| **$\hat b_i$, $\hat{\underline y}_n$ (caps)** | $b_i$, $y_n$ | **hat reversed: the paper's caps mark the higher (fifth) order, propagated formula** |
| **$b_i$, $\underline y_n$** | $\hat b_i$, $\hat y_n$ | **the paper's unhatted quantities are the embedded fourth-order formula**; its $b_7$ is the registry $\hat b_7$ |
| $q$, $p$ in RK$q(p)$ | $p$, $\hat p$ | **the paper's $p$ is the lower order** ($q>p$); RK5(4)$s$X: propagated order 5, estimator order 4, $s$ stages counting the reused one |
| suffixes M, S | — | "minimum" truncation error and "stability" (from the text; not defined) |
| $\underline t_{n+1}$, $\underline\Phi$, $\underline\Delta$ | — | local truncation error (numerical minus exact), increment function, Taylor increment |
| $\underline F^{(r)}_i$, $n_r$ | $F(\tau)$, number of trees with $\lvert\tau\rvert=r$ | $n_r=1,1,2,4,9,20,48$ |
| $\hat a^{(r)}_i$ | $E^{(r)}_i$ | page-local; $=(\Phi(\tau)-1/\gamma(\tau))/\sigma(\tau)$ of the fifth-order formula (Table 1 normalization); **$a$ collides with the Butcher coefficients** |
| $a^{(r)}_i$ | $\hat E^{(r)}_i$ | the same for the fourth-order formula |
| $\lVert\hat{\underline a}^{(6)}\rVert_2$ | $\lVert E^{(6)}\rVert_2$ | 2-norm over the 20 sixth-order coefficients |
| $d$ | $\theta_6$ of $P(z)$ | coefficient of $z^6$, fifth-order formula |
| $e$, $f$, $g$ | $\hat\theta_5$, $\hat\theta_6$, $\hat\theta_7$ of $\hat P(z)$ | page-local hat for the embedded polynomial; **$f$ collides with the right-hand side** |
| $z=x+iy$ | $z=h\lambda$ | complex variable of the stability regions; **$x$, $y$ collide with time and solution** |
| $\underline E_{n+1}=\underline y_{n+1}-\hat{\underline y}_{n+1}$ | $\hat y_{n+1}-y_{n+1}$ | error estimate, lower minus higher order |
| $\delta$ | — | maximum allowable local error (tolerance), page-local |
| circled $\hat k$, $k$ | — | equation $k$ of Table 1 for the fifth-order (stages 1–6) and fourth-order (stages 1–7) formula |

# Reference list

The paper prints 17 references, numbered [1]–[17] in order of first
citation. All 17 are merged complete into the
[bibliography](/bibliography.md) with `citedby` dormand-1980. Ref. [12]
(Shampine & Watts, in *Mathematical Software III*, ed. Rice, 1977,
pp. 257–275) prints no chapter title and carries a placeholder title. Ref.
[4] (Hull et al. 1972) prints volume and issue but no pages. Ref. [10] is
Butcher's 1964 paper "On Runge-Kutta processes of high order" (J. Austral.
Math. Soc. 4), a different work from the ingested [Butcher (1964)](/sources/butcher-1964.md). Two
Shampine 1976 works are cited: [5] (with Watts) and [15] (single author).
No DOIs are printed. No printed duplicates.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [Dormand–Prince 5(4) pair](/methods/dormand-prince-5-4.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Kepler problem](/benchmarks/kepler-problem.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
