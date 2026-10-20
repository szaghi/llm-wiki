---
type: Source
title: "Faleichik & Moisa (2026) — Explicit Runge–Kutta–Chebyshev methods of second order with monotonic stability polynomial"
description: "Constructs second-order Runge–Kutta–Chebyshev methods whose stability polynomial is positive and monotonically non-decreasing on the longest possible negative real interval, realized by a three-term recurrence with internally stable stages, trading a shorter stability interval for more convex regions and much smaller error constants."
resource: "doi:10.1016/j.cam.2025.117061"
source_kind: paper
authors: [Faleichik B., Moisa A.]
year: 2026
venue: "J. Comput. Appl. Math. 476:117061"
local_file: "/home/stefano/papers/mosaic/ode-integration/2026_Crossref_Journal_of_Computational_and_Applied_Mathematics_Faleichik_Explicit_RungeKuttaChebyshev_methods_of_second_order_with_mo.pdf"
tags: [stabilized, runge-kutta, explicit, stability, step-size-control]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper builds a new family of second-order
[stabilized explicit Runge–Kutta](/methods/stabilized-explicit-runge-kutta.md)
methods of Runge–Kutta–Chebyshev type for mildly stiff problems, called
"monotonic" (solver MONO). Besides the order conditions
$P_s(0)=P_s'(0)=P_s''(0)=1$, the degree-$s$
[stability polynomial](/definitions/stability-function.md) is required to
be positive and non-decreasing on the longest possible interval
$(-\varrho_s,0]$. The motivation, after Bobkov, is consistency with the
exponential, which is positive and monotone on the negative axis, whereas
classical RKC polynomials oscillate between damping bounds.

The construction takes $P_s'$ as a shifted, scaled, non-negative Chebyshev
polynomial, $\mathsf b_{s-1}(1+T_{s-1}(w_0+w_1z))$, and integrates it from
$-\varrho_s$. The order conditions fix $\mathsf b_{s-1}$, $w_1$ and a scalar
transcendental equation for $w_0$, solved with 500 digits. The result is
a combination of $T_s$ and $T_{s-2}$ plus a linear term, realized by a
three-term recurrence close to the second-order RKC of Verwer, Hundsdorfer
and Sommeijer. The internal stage polynomials lie in $[0,1)$ on
$[-\varrho_s,0)$, so the method has
[internal stability](/definitions/internal-stability.md) by construction,
and stage $Y_{s-1}$ is a first-order approximation at $t_n+h$.

This is another way of choosing an
[optimal stability polynomial](/methods/optimal-stability-polynomial.md):
it maximizes the monotonicity interval instead of the stability interval.
The interval grows like $\varrho_s\approx0.31(s+0.83)^{1.87}$, markedly shorter
than RKC's $\approx0.65s^2$, but the regions are more convex and the error
constant is about 6 times smaller for large $s$. The implementation uses a
fitted stage-number formula, a Taylor-based error estimate and the RKC
[step-size control](/methods/step-size-control.md). On four stiff problems
MONO takes larger steps for the same accuracy but more stages per step,
and matches requested to achieved accuracy better on the combustion
problem. Everything is shown by construction and tables; no convergence
theorem is proved.

# Version read

arXiv preprint arXiv:2504.00323v1 [math.NA], 1 April 2025 ("Preprint
submitted to Elsevier, April 2, 2025"), 10 PDF pages: a graphical-abstract
page, then the paper on pp. 2–10. It is not the JCAM version of record;
page and equation numbers are those of the arXiv v1. Title and authors
match Crossref (the preprint writes "Runge-Kutta-Chebyshev" with hyphens);
the keyword field is empty.

# Key claims

Registry notation: $h$ step, $t_n\to t_{n+1}$ one step (the source's
$x_0\to x_0+h$), $P_s(z)$ the stability polynomial with real argument $z$
(the source's $R_s(x)$), $\tilde P_j$ the internal stage polynomials, $Y_j$
stage values. Page-local: $T_k$ Chebyshev polynomials of the first kind,
$w_0$, $w_1$ shift and scale, $\mathsf b_j=1/(1+T_j(w_0))$ (not Butcher
weights), $\varrho_s$ the monotonicity-interval length, $C_s$ the error
constant.

1. Imposing $P_s'(z)\ge0$ and $P_s(z)>0$ on $(-\varrho_s,0]$ with $\varrho_s$
   maximized improves the consistency of the stability function with the
   exponential, after Bobkov (§1, Eq. (2)). **Stated**
2. The conditions $P_s(0)=P_s'(0)=P_s''(0)=1$ are "sufficient for the final
   Runge–Kutta scheme to have order two" (§1, Eq. (3)). **Stated**
   (nonlinear order 2 of scheme (17) is not proved)
3. Maximizing $\varrho_s$ requires minimal deviation of $P_s'$ from zero,
   hence $P_s'(z)=\mathsf b_{s-1}(1+T_{s-1}(w_0+w_1z))$ with
   $\varrho_s=(1+w_0)/w_1$ (§2, Eqs. (4)–(6)). **Derived** (optimality of the
   Chebyshev shape argued, not proved)
4. $P_s''(0)=1$ gives $w_1=1/(\mathsf b_{s-1}T'_{s-1}(w_0))$; $w_0$ is the
   root of the scalar equation (12), solved numerically with 500 digits
   (§2, Eqs. (7), (12)). **Derived**
5. Closed form: $P_s(z)=1+\mathsf b_{s-1}z+\gamma_s(T_s(w_0+w_1z)-T_s(w_0))+\delta_s(T_{s-2}(w_0+w_1z)-T_{s-2}(w_0))$,
   $\gamma_s=\mathsf b_{s-1}/(2sw_1)$, $\delta_s=-\mathsf b_{s-1}/(2(s-2)w_1)$
   (§2, Eqs. (9)–(11)); defined for $s\ge3$. **Derived**
6. Scheme (17) realizes $P_s$ through the three-term Chebyshev recurrence
   and is "very similar to the second-order RKC method" (§2,
   Eqs. (13)–(18)). **Derived**
7. Stage $Y_j$ has stability polynomial
   $\tilde P_j(z)=1+\mathsf b_j(T_j(w_0+w_1z)-T_j(w_0))$, and
   $0\le\tilde P_j(z)<1$ on $[-\varrho_s,0)$, $j>0$: the method is internally
   stable (§2, Eq. (13)). **Derived**
8. $P_s'=\tilde P_{s-1}$, so $Y_{s-1}$ is a stable first-order
   approximation of $y(t_n+h)$, usable as an embedded estimate (§2,
   Eq. (19)). **Derived**
9. The abscissae are $c_j=w_1\mathsf b_jT_j'(w_0)$ with
   $c_{j-1}<c_j<c_{s-1}=1$, $j=1,\dots,s-2$ (§2, Eq. (20)). **Derived**
10. There is no exact formula for $\varrho_s$; the fit is
    $\varrho_s\approx0.31(s+0.83)^{1.87}$ (§3). **Shown** (fit)
11. $\varrho_3=3.5874010$, $\varrho_5=8.6189019$, $\varrho_{10}=29.268039$,
    $\varrho_{20}=100.80657$, $\varrho_{50}=525.59171$, $\varrho_{100}=1855.5228$,
    $\varrho_{200}=6617.5217$, $\varrho_{500}=36059.771$, $\varrho_{1000}=131320.58$,
    $\varrho_{2000}=481823.56$ (Table 1). **Shown**
12. For large $s$ the stability-interval length is "just slightly greater
    than $\varrho_s$" (§3). **Stated**
13. Monotonic methods have shorter stability intervals than RKC (about
    130,000 against 650,000 at $s=1000$, read from Fig. 3) but more convex
    regions (Fig. 2: MONO $s=9$ reaches about $-29$, RKC $s=9$ about $-53$)
    (abstract, §3, Figs. 2–3). **Shown**
14. Error constant $C_s=(1-P_s'''(0))/6$ is much smaller than RKC's, about
    6 times for large $s$: $C_3=0.0833333$, $C_{10}=0.0322256$,
    $C_{100}=0.0158146$, $C_{2000}=0.0100482$ (§3, Table 1, Fig. 3).
    **Shown**
15. Stage-number formula fitted on $(\varrho_s,s)$:
    $s\approx-0.8306782+1.8547888\,\rho^{0.5338714}$, $\rho$ a spectral-radius
    estimate (§4, Eq. (21)). **Shown** (fit)
16. The $Y_{s-1}$ estimator has an $s$-dependent error constant and would
    need normalization; the code uses instead
    $\mathrm{err}=\frac1{10}(y_n-y_{n+1}+f(t_n+h,y_{n+1}))$, "asymptotically
    correct" for a first-order embedded method with leading error
    $\frac1{10}h^2y''$ (§4, Eqs. (22)–(23)). **Stated** (see Printed slips)
17. All other step-size-selection details are taken from the RKC code of
    Sommeijer, Shampine and Verwer (§4). **Stated**
18. MONO (C) against RKC and the two-step TSRKC2 on CUSP, FINAG, BURGERS
    and COMB at tolerances $10^{-3}$, $10^{-5}$, $10^{-7}$: MONO uses larger
    steps for the same accuracy but more stages; overall comparable (§5,
    Table 2). **Shown**
19. On COMB MONO matches requested and achieved accuracy better: error
    $3.72\cdot10^{-1}$ at tolerance $10^{-3}$ (RKC and TSRKC2
    $1.84\cdot10^{1}$), $1.81\cdot10^{-2}$ at $10^{-5}$ (RKC $1.20$,
    TSRKC2 $3.77\cdot10^{-1}$), $6.12\cdot10^{-4}$ at $10^{-7}$ (RKC
    $5.97\cdot10^{-2}$, TSRKC2 $4.17\cdot10^{-3}$) (Table 2). **Shown**
20. Cost at tolerance $10^{-7}$ ($f$-evaluations, accepted, rejected, ms):
    CUSP RKC 8640/1303/5/1.00, TSRKC2 26117/8187/221/3.44, MONO
    24420/3796/5/2.87; BURGERS RKC 1094/462/0/0.58, MONO 3224/1074/0/1.54;
    COMB RKC 4745/1491/0/65.04, MONO 13993/3563/0/196.54; hardware not
    stated (Table 2). **Shown**
21. Source code and examples are public at
    github.com/MoisaAndrew/StabilizedMethods (§5). **Stated**

*(Compiler observation, not in the sources.)* On CUSP, BURGERS and COMB, RKC uses fewer
$f$-evaluations and less time than MONO at every tolerance; the paper's
"competitive" conclusion rests on the error-to-tolerance match, without a
work–precision plot.

# Printed slips

- Eq. (8): "$R_s(x)=b_{s-1}\int_{-\rho_s}^x(1+T_{s-1}(\xi))d\xi$"; the
  integrand argument should be $w_0+w_1\xi$ to agree with (4) and with
  (9)–(11).
- Eq. (23): "$err=\frac1{10}(y_0-y_1+f(x_0+h,y_1))$" lacks a factor $h$ on
  $f$. With $h$ restored the expression equals $\frac1{20}h^2y''+O(h^3)$,
  not the $\frac1{10}h^2y''$ of (22); the asymptotically correct factor
  would be $\frac15$ *(compiler expansion, not in the sources; to check against the version of
  record and the code)*.
- Table 2: RKC has no FINAG row at tolerance $10^{-3}$, unexplained.
- Abstract "monotonically increasing" against the non-strict condition
  $R_s'\ge0$ of (2).
- "FitzHug" for FitzHugh (§5); ref. [5] prints "doi:doi:10.2478/…"; ref. [9]
  year printed "????".

# Notation map

| Faleichik & Moisa (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$, $y'(x)=f(x,y)$ | $t$, $y'=f(t,y)$ | independent variable |
| $x_0$, $y_0\to y_1$ | $t_n$, $y_n\to y_{n+1}$ | one step |
| $h$ | $h$ | agrees |
| **$x$ in $R_s(x)$** | $z=h\lambda$ (real) | **the same letter as the time variable** |
| $R_s$ | $P_s(z)$ | stability polynomial of an explicit method |
| $\tilde R_j$ | $\tilde P_j$ | internal stage polynomials |
| $R_s^{\rm RKC}$ | — | second-order RKC polynomial (Fig. 1) |
| $s$ | $s$ | stages = degree of $P_s$ |
| $T_k$ | — | Chebyshev polynomial of the first kind; **$T$ collides with the tree set** |
| $w_0$, $w_1$ | — | shift and scale of the Chebyshev argument |
| **$b_j$** | $\mathsf b_j$ | **$1/(1+T_j(w_0))$; collides with the weights $b$** |
| $\alpha_s,\gamma_s,\delta_s$ | — | Chebyshev-form coefficients (9); **$\alpha$, $\gamma$ collide with Shu–Osher and Rosenbrock symbols** |
| $\mu_j,\nu_j,\tilde\mu_j$ | — | recurrence coefficients (16); **$\nu_j$ collides with the Courant number** |
| $Y_j$, $F_j=f(x_0+c_jh,Y_j)$ | $Y_j$, $f(t_n+c_jh,Y_j)$ | stage values; agrees |
| $c_j$ | $c_j$ | abscissae, $c_{s-1}=1$ |
| $\rho_s$ | $\varrho_s$ (page-local) | monotonicity-interval length; as on the [stabilized methods](/methods/stabilized-explicit-runge-kutta.md) page; **not the multistep generating polynomial $\varrho(\zeta)$** |
| $\rho$ | — | spectral-radius estimate used to choose $s$ |
| $C_s$ | — | error constant $(1-P_s'''(0))/6$; not the SSP $\mathcal C$ |
| $le$, $err$ | $\mathrm{err}_n$ (unscaled) | local error and its estimate |

# Reference list

The paper prints 10 references in numbered style. All are merged complete
into the [bibliography](/bibliography.md) with `citedby` faleichik-2026.
Refs. [6] and [7] print no page or article number; refs. [6] and [8]
share first author and year and take keys in printed order; ref. [9] is an
undated GitHub repository keyed by the citing year; ref. [5] prints a
doubled "doi:" prefix. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [FitzHugh–Nagumo model](/benchmarks/fitzhugh-nagumo-model.md)
* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Optimal stability polynomials for explicit Runge–Kutta methods](/methods/optimal-stability-polynomial.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping](/methods/stabilized-explicit-runge-kutta.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
