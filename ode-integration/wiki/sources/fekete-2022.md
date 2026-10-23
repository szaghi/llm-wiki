---
type: Source
title: "Fekete et al. (2022) — Embedded pairs for optimal explicit strong stability preserving Runge–Kutta methods"
description: "Constructs embedded lower-order weights for optimal explicit SSP Runge–Kutta methods of orders 2 to 4, keeping the SSP coefficient where possible, and tests them with I, PI, PID and Gustafsson step-size controllers against classical embedded pairs."
resource: "doi:10.1016/j.cam.2022.114325"
source_kind: paper
authors: [Fekete I., Conde S., Shadid J.N.]
year: 2022
venue: "J. Comput. Appl. Math. 412:114325"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Computational_and_Applied_Mathematics_Fekete_Embedded_pairs_for_optimal_explicit_strong_stability_preserv.pdf"
tags: [ssp, embedded-pair, step-size-control, runge-kutta, explicit, error-estimation]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

Optimal explicit [SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
are the standard integrators for method-of-lines semi-discretizations of
hyperbolic conservation laws. In practice they run at a fixed, CFL-limited step,
because they have no embedded error estimator; this rules out the adaptive
[step-size control](/methods/step-size-control.md) that the Bogacki–Shampine
3(2) and Dormand–Prince 5(4) pairs allow.

The paper constructs [embedded weights](/methods/embedded-runge-kutta-pair.md)
$\hat b$ for optimal SSP [Runge–Kutta methods](/definitions/runge-kutta-method.md)
of order $2\le p\le4$. The weights share $A$ with the main method, so the error
estimate costs no extra function evaluation. The design targets are:

- the embedded method has order $\hat p=p-1$;
- it is non-defective, meaning it violates every order-$p$
  [order condition](/results/runge-kutta-order-conditions.md);
- its coefficients are rational where possible;
- where possible, it has the same SSP coefficient $\mathcal C$ as the main method.

The secondary criteria are the stability-region radii of the embedded
[stability function](/definitions/stability-function.md) and
Kennedy–Carpenter–Lewis error measures.

**Results.** SSPERK($s$,2) has two closed-form first-order families with
$\hat{\mathcal C}=s-1$. For SSPERK(4,3) the embedding is $\hat b=\frac14\mathbf 1$.
For SSPERK($n^2$,3) with $n\ge3$ it is $\hat b=\frac1{n^2}\mathbf 1$, since no
embedding with the full SSP coefficient was found.

SSPERK(10,4) is the [low-storage](/methods/low-storage-runge-kutta.md)
fourth-order method. For it the paper lists eight rational third-order
embeddings. A non-defective one cannot exist, because one fourth-order
condition holds for every $\hat b$. Numerically optimized weights are added for
five more methods.

**Tests.** The I, PI, PID and Gustafsson controllers run on Van der Pol, the
Brusselator, square-wave advection and Sod's shock tube (the last two with
WENO5). The PID controller is best. The new second-order pairs meet the
tolerance where classical second-order pairs do not. Third-order SSP pairs cost
30–40% more than Bogacki–Shampine. The fourth-order SSP pairs beat
Dormand–Prince on the hyperbolic problems for tolerances $\ge10^{-4}$, but not
for $\le10^{-5}$. All evidence is numerical; the paper proves no theorem.

# Version read

The file is the arXiv preprint arXiv:1806.08693v1 [math.NA] (22 Jun 2018),
22 pages, not the JCAM version of record. Its identity differs from the
published one in two ways:

- **Title.** Page 1 reads "Embedded error estimation and adaptive step-size
  control for optimal explicit strong stability preserving Runge–Kutta
  methods".
- **Author order.** Page 1 lists Conde, Fekete, Shadid, with Conde as
  corresponding author. Crossref gives Fekete, Conde, Shadid.

The subject and core results (the embedded pairs for SSPERK($s$,2),
SSPERK($n^2$,3) and SSPERK(10,4)) are the same. Revisions made between 2018 and
2022 cannot be checked from this file. The preprint defers the SSP coefficients
and error measures of its pairs to a GitHub draft (its ref. [3]). Everything on
this page is a claim of arXiv v1, with arXiv v1 numbering.

# Key claims

1. An explicit RK method is SSP with coefficient $\mathcal C$ if $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ whenever the forward Euler condition (6) holds and $h\le\mathcal C h_{\mathrm{FE}}$. The coefficient is the supremum of the $r$ for which $(I+rK)^{-1}$ exists, $K(I+rK)^{-1}\ge0$ and $rK(I+rK)^{-1}\mathbf 1\le\mathbf 1$, with $K=\begin{pmatrix}A&0\\b^\top&0\end{pmatrix}$ (§1.1, Thm. 1, citing Gottlieb–Ketcheson–Shu). **Stated**
2. $\mathcal C>0$ implies $A\ge0$ and $b\ge0$, so any SSP embedded weight vector satisfies $0\le\hat b\le\mathbf 1$ (§1.1, Thm. 2; §2). **Stated**
3. No explicit RK method of order $p\ge5$ has positive SSP coefficient (§1.1). **Stated**
4. The Shu–Osher convex decomposition into forward Euler steps is "a sufficient and necessary condition for the SSP property" (§1.1). **Stated**
5. The embedded-pair search is posed as a simplified problem (eqs. 9–11). It fixes $\hat{\mathcal C}$ equal to the main method's $\mathcal C$ and imposes three things: the SSP conditions on $\begin{pmatrix}A&0\\\hat b^\top&0\end{pmatrix}$, the order-$(p-1)$ conditions, and non-defectiveness. **Derived**
6. For a defective pair, the order-$p$ error coefficients of the embedded method vanish. The ratio measures $C^{(p+1)}$ then diverge, so non-defectiveness is needed for a meaningful error estimate (Remark 2). **Derived**
7. For numerically optimal SSP methods, embedded weights are found by minimizing the max-norm of a vector of error measures (eq. 14). The constraints are the order-$\hat p$ conditions and nonnegative weights, and the solver is MATLAB fmincon. The coefficients are not rational, and the weight vectors are not printed. **Shown**
8. SSPERK($s$,2) (Ruuth–Spiteri, $\mathcal C=s-1$) admits two non-defective first-order embeddings with $\hat{\mathcal C}=s-1$: $\hat b_1=[\frac1{s-1},\dots,\frac1{s-1},0]$ and $\hat b_2=[\frac{s+1}{s^2},\frac1s,\dots,\frac1s,\frac{s-1}{s^2}]$. The paper prefers $\hat b_2$, though the two are "equally good for $s\ge4$" on stability regions alone (§2.1, Fig. 1). **Shown**
9. For SSPERK(2,2), $\hat b_2$ has a far larger embedded stability region than $\hat b_1$ (Fig. 1a vs 1e). **Shown**
10. SSPERK($n^2$,3) with $n\ge2$ has $\mathcal C=n^2-n=s-\sqrt s$. Its Butcher form is given in (15)–(16) (§2.2, citing Ketcheson). **Stated**
11. For SSPERK(4,3), the known embedding $\hat b_1=[\frac13,\frac13,\frac13,0]$ is an exceptional case. The proposed $\hat b_2=\frac14\mathbf 1$ has a significantly larger stability region (§2.2, Fig. 3). **Shown**
12. For SSPERK($n^2$,3) with $n\ge3$, the searches found no embedding with $\hat{\mathcal C}=n^2-n$. The proposed non-defective second-order embedding is $\hat b=\frac1{n^2}\mathbf 1$, which has $\hat{\mathcal C}>0$ (§2.2, Fig. 5). **Shown**
13. For SSPERK(10,4) (Ketcheson, $\mathcal C=6$, low-storage), no non-defective embedding exists: the order condition $b^\top(\frac{c^3}{3!}-\frac{Ac^2}{2!})=0$ (8g) holds for every $\hat b$. The searches found no embedding with $\hat{\mathcal C}=6$ (§2.3). **Shown** (compiler check, not in the sources: (8g) holds for all eight listed $\hat b$)
14. Eight rational third-order embeddings $\hat b_1,\dots,\hat b_8$ for SSPERK(10,4) are printed. They are "good candidates … but not an outstanding one", and $\hat b_3$ is suggested (§2.3, Fig. 6). **Shown**
15. Step-size control (§3.1, eqs. 17–19). The error is $\mathrm{err}_n=\lVert(y_{n+1}-\hat y_{n+1})/sc\rVert_\infty$, with componentwise scale $sc=\mathrm{atol}+\max(\lvert y_n\rvert,\lvert y_{n+1}\rvert)\,\mathrm{rtol}$. The step factor is limited by safety $0.9$, minimum $0.1$ and maximum $5$, and the maximum drops to $0.9$ right after a rejection to avoid an observed infinite loop. Local extrapolation is used: the solution advances with order $p$. **Stated**
16. Controller gains, in registry form $h_{n+1}=h_n\,\mathrm{err}_n^{-\beta_1/k}\mathrm{err}_{n-1}^{-\beta_2/k}\mathrm{err}_{n-2}^{-\beta_3/k}$ (§3.1, eqs. 20–23):
    - I: $\beta_1=1$.
    - PI: $(\beta_1,\beta_2)=(0.8,-0.31)$.
    - PID: $(\beta_1,\beta_2,\beta_3)=(0.58,-0.21,0.1)$.
    - Explicit Gustafsson: printed as $\mathrm{err}_n^{-0.367/p}(\mathrm{err}_n/\mathrm{err}_{n-1})^{0.268/p}$, i.e. $(\beta_1,\beta_2)=(0.099,0.268)$, with an error floor of $10^{-10}$.

    The paper attributes these defaults to "SUNDIALS/CVODE". **Stated**
17. Van der Pol ($\varepsilon=0.1$, tolerance $10^{-4}$) with SSPERK(2,2)–$\hat b_2$, steps taken (rejected):
    - I controller: 1982 (495);
    - PI: 1270 (210);
    - PID: 753 (17);
    - Gustafsson: 795 (38).

    The final $L_2$ errors are $4.06\times10^{-5}$, $1.09\times10^{-4}$, $1.59\times10^{-4}$ and $1.53\times10^{-4}$ (§3.1.1, Fig. 9). **Shown**
18. Brusselator with SSPERK(3,3) at tolerance $10^{-4}$, steps (rejected): I 419 (103), PI 312 (17), PID 305 (17), Gustafsson 332 (35) (Fig. 10). **Shown**
19. The PID controller "performed significantly better" in the vast majority of tests and never needed a second attempt. All later comparisons use PID (§3.1.1). **Shown**
20. Second order: the new SSP pairs reach a global error close to the tolerance. RKF23, Ceschino24 and Fehlberg12 "fail to obtain a global error better than 1e−5 even with a restrictive tolerance of 1e−7" on all four problems (§3.2.2, Fig. 11). **Shown**
21. Third order: Bogacki–Shampine 3(2) is cheaper and has better error measures. On the hyperbolic problems, SSPERK(4,3)–$\hat b_2$ is "relatively similar" for tolerances $\ge10^{-2}$ and "only 30%–40% more costly otherwise" (Fig. 12). **Shown**
22. Fourth order: none of the literature fourth-order pairs is SSP, since each has a negative coefficient. The SSPERK(10,4) and SSPERK(6,4) pairs are the most efficient on the hyperbolic problems for tolerances $\ge10^{-4}$, and lose that advantage for tolerances $\le10^{-5}$ (Figs. 13c–d). **Shown**
23. SSPERK(10,4)–$\hat b_2$ is the worst on all problems. It overestimates the local error, takes tiny steps and is "not practical" (§3.2.2). **Shown**
24. Methods with many stages, and hence large stability regions and SSP coefficients, are "very robust and perform less work per degree of accuracy" (§4). **Shown** (qualitative)
25. Recommendations (§4):
    - second order: SSPERK(4,2)–$\hat b_2$, SSPERK(6,2)–$\hat b_2$ and SSPERK(3,2) with optimized weights;
    - third order: SSPERK(4,3)–$\hat b_2$ and the SSPERK(3,3) pair;
    - fourth order: SSPERK(10,4) with $\hat b_1$, $\hat b_3$, $\hat b_5$ or $\hat b_8$.

    **Stated**
26. The Higueras–Ketcheson–Kocsis perturbation technique can give existing non-SSP pairs a positive SSP coefficient, "at the expense of an additive routine" (§4). **Stated**

# Printed slips

- Def. 1 (p. 5) defines real-axis inclusion as $\delta_R=\sup\{\gamma\ge0: l(-\gamma,\gamma)\subset S\}$, a symmetric segment. For an explicit method this gives $\delta_R=0$; the intended segment is presumably $l(-\gamma,0)$.
- §2.1 (p. 6) speaks of "embedded pairs for SSPERK(s, 1) methods", and the Fig. 4 caption says "embedded ERK(s,1) methods with s = 4, 3". The embedded methods of the third-order main methods are second order. The Fig. 4 caption also names "SSPERK(s,3)" twice.
- Remark 2 (p. 6) is garbled: "we know it's a non-defective method of order p. Otherwise, it would be a non-defective method of order p + 1".
- The captions of Figs. 5 and 6 say "embedded SSPERK($n^2$,2)" and "SSPERK(10, 3)", while the text says ERK. §2.3 writes $\mathcal C=6$ where $\tilde{\mathcal C}$ is meant.
- Dormand–Prince appears as "4(5)" in §1 and "54" in §3, and as using "six function evaluations" (§3.1) but "seven-stage" (§3.2.2).
- §3.2.2 says RKF23, Ceschino24 and Fehlberg12 "appear … less costly". Fig. 11d shows a relative work of about 1.3–1.75 for them, i.e. more costly than the reference.
- References: [19] and [20] are the same paper (Kennedy, Carpenter, Lewis 2000), and so are [21] and [22] (Ketcheson 2008). The abstract cites "[5, 19]" for error measures, but [5] is Dekker–Verwer.
- Typos: "lookign", "the the", "DormanndPrince54", "Ceshino24", "Felhber12", "Numerial", "immidiately", "developped", "inpractical", "SSPRK(6,2)".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u'=f(t,u)$; $u_t=F(u)$ | $y'=f(t,y)$ | ODE and autonomous semi-discretization |
| $\Delta t$, $\Delta t_n$ | $h$, $h_n$ | step size |
| $A$, $b^T$, $c=A\mathbf e$ | $A$, $b^\top$, $c=A\mathbf 1$ | agrees |
| $\mathbf e$ | $\mathbf 1$ | vector of ones |
| $Y_i$ | $Y_i$ | stage values (agrees) |
| $\tilde b^T$, $\tilde w$ | $\hat b^\top$ | embedded weights, closed-form or optimized |
| $u_{n+1}$, $\hat u_{n+1}$ | $y_{n+1}$, $\hat y_{n+1}$ | order-$p$ and order-$(p-1)$ solutions; local extrapolation |
| $\Delta t_{FE}$ | $h_{\mathrm{FE}}$ | |
| $\mathcal C$, $\tilde{\mathcal C}$ | $\mathcal C$, $\hat{\mathcal C}$ | SSP coefficient of the main and embedded methods; $\mathcal C_{\mathrm{eff}}$ is never used |
| $\psi(z)$ | $R(z)$ (here $P(z)$) | stability function |
| $S$ | $\mathcal S$ | absolute stability region |
| $R(\psi)$ | — | radius of absolute monotonicity; **collision** with registry $R$ (stability function) |
| $\tau^{(p+1)}$, $\tilde\tau^{(p)}$ | — | error-coefficient vectors (Kennedy–Carpenter–Lewis); **collision**: registry $\tau$ is a tree, and $\tau^{(k)}$ is the stage-order residual |
| $C^{(p+1)}$ | — | error-measure ratio, distinct from the SSP coefficient $\mathcal C$ |
| $Atol$, $Rtol$, $err_{n+1}$ | $\mathrm{atol}$, $\mathrm{rtol}$, $\mathrm{err}_n$ | **index shift**: the source's $err_{n+1}$ is the error of the current step, which the registry calls $\mathrm{err}_n$ |
| $\beta_{n+1}=err_{n+1}^{-k_1/p}err_n^{k_2/p}err_{n-1}^{-k_3/p}$ | $\beta_1=k_1$, $\beta_2=-k_2$, $\beta_3=k_3$, exponent denominator $k=p$ | the registry's $k=\min(p,\hat p)+1=p$ here; whether the source's $p$ is the main or embedded order is not specified |
| $\epsilon$ (Van der Pol) | $\varepsilon$ | stiffness parameter |
| $\nu=c_{max}\Delta t/\Delta x$ | $\nu$ | Courant number (agrees) |

# Reference list

The paper prints 43 references in numbered style ([1]–[43], alphabetical). The
list is merged complete into the [bibliography](/bibliography.md), with
`citedby` this slug. It contains two printed duplicates, [19]/[20] (Kennedy et
al. 2000) and [21]/[22] (Ketcheson 2008); each pair is folded into one entry
(`kennedy-2000`, `ketcheson-2008`), so the list gives 41 entries. Several items are
incomplete:

- [28] Merson 1957 prints no venue;
- [14] Higueras–Ketcheson–Kocsis is online-first, with no volume or pages;
- [3] is a GitHub draft (March 2018);
- [29] is the Tempus software;
- [42] Trefethen 1996 has no publisher.

No DOIs are printed.

# Pages created or updated

Chunk 1 (2026-10-19); updated in later chunks. This source is cited on:

* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [Runge–Kutta method](/definitions/runge-kutta-method.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Sod shock tube](/benchmarks/sod-shock-tube.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Van der Pol oscillator](/benchmarks/van-der-pol-oscillator.md)
