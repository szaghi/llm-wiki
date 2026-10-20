---
type: Source
title: "Croci & Rosilho de Souza (2022) — Mixed-precision explicit stabilized Runge–Kutta methods for single- and multi-scale differential equations"
description: "Defines order-preserving mixed-precision Runge–Kutta schemes and builds mixed-precision Runge–Kutta–Chebyshev and multirate RKC methods that evaluate only one or two right-hand sides per step in high precision, with order, error-propagation and rounding-error results and bfloat16/double experiments on stiff parabolic problems."
resource: "doi:10.1016/j.jcp.2022.111349"
source_kind: paper
authors: [Croci M., Rosilho de Souza G.]
year: 2022
venue: "J. Comput. Phys. 464:111349"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Computational_Physics_Croci_Mixed-precision_explicit_stabilized_RungeKutta_methods_for_s.pdf"
tags: [mixed-precision, stabilized, runge-kutta, explicit, multirate, stiff]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper designs [mixed-precision](/methods/mixed-precision-runge-kutta.md)
Runge–Kutta–Chebyshev (RKC) methods, a family of
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md)
in which a low order $p$ is paired with $s\gg p$ stages so that the real
stability interval grows like $s^2$. The few right-hand-side evaluations
that buy accuracy are done in high precision (fp64) and the many that only
buy stability in low precision (bfloat16, fp16, fp32).

A heuristic linear analysis shows that an all-low-precision method has
global error $O(u h^{-1}+h^p)$, with $u$ the low-precision unit roundoff,
and a "standard" mixed-precision method (matrix–vector products in low
precision) stagnates at $O(u+h^p)$. The paper defines a
$\tilde q$-order-preserving scheme as one converging with order $\tilde q$
when the high-precision operations are exact; computing the first
$\tilde q$ products exactly gives $O(uh^{\tilde q}+h^p)$. The source calls
the stagnation an "order-reduction phenomenon", a different meaning from
stiff [order reduction](/definitions/order-reduction.md).

For nonlinear problems RKC is written in delta form and each
$f(y_n+d_j)$ is replaced by $f(y_n)$ plus a low-precision approximation of
the difference, accurate to $O(\epsilon h)$ (1-order-preserving) or
$O(h^2)$ (2-order-preserving), the latter used through a hybrid switch so
as to keep [internal stability](/definitions/internal-stability.md).
Practical forms use low-precision matrix–vector products or scaled
finite-difference Jacobian actions. A mixed-precision multirate RKC (mRKC)
follows the same pattern. Theory gives Taylor order results, local error
propagation bounds independent of $s$ and of the stiffness, and a
worst-case internal rounding-error bound that guarantees boundedness only
for $s^2u=O(1)$; a rigorous stability proof is stated to be out of reach.
The [stability polynomial](/definitions/stability-function.md) is the
RKC Chebyshev polynomial. Emulated bfloat16/double FEM experiments show
order preservation, stability up to $s=512$ and errors 2–8 orders of
magnitude below standard mixed precision; there are no timings.

# Version read

arXiv preprint arXiv:2109.12153v2 [math.NA], 6 April 2022, author LaTeX,
38 pages (main text pp. 1–33, references pp. 34–37, appendices A–B
pp. 37–38). It is not the JCP version of record: page, section and
equation numbers cited here are those of the arXiv v2, and the DOI is not
printed on the copy. Title and authors match Crossref. The paper is
dedicated to Assyr Abdulle.

# Key claims

Registry notation: $h$ step, $s$ stages, $p$ classical order, $z=h\lambda$,
$P_s(z)$ the stability polynomial, $\rho$ the spectral radius of $J$. Page-
local: $u$ the low-precision unit roundoff, $\tilde q$ the preserved order
(the source's $q$, which is not the stage order), $\epsilon$ the accuracy
constant of the difference approximations, $\varepsilon_{\mathrm d}$ the
RKC damping, $T_k$, $U_k$ Chebyshev polynomials, $r$ the high/low cost
ratio.

1. An RK method with all operations in precision $u$ has local error
   $O(u+h^{p+1})$ and global error $O(uh^{-1}+h^p)$, so it does not
   converge as $h\to0$ (§3.1, Eq. (15)). **Derived**
2. A "standard" mixed-precision RK (matrix–vector products low, vector
   operations high) converges only to $O(u+h^p)$ (§3.1, Eq. (16)).
   **Derived**
3. Computing the first $\tilde q$ products in high precision for $f=Ly$
   gives error $O(uh^{\tilde q}+h^p)$: rate $p$ until $h\propto
   u^{1/(p-\tilde q)}$, then rate $\tilde q$ (§3.1, Eq. (17); Remark 3.1,
   Eq. (18)). **Derived**
4. Cost reduction $\varrho=(s-\tilde q)(r-1)/(sr)$, tending to $1-1/r$ as
   $s\to\infty$ and to $1-\tilde q/s$ as $r\to\infty$ (Eqs. (19), (40)–(41));
   e.g. RK4 with $\tilde q=2$, fp64/fp16, $\varrho=37.5\%$ ($r=4$) or
   $\approx47\%$ ($r=16$); 64-stage RKC2 with $\tilde q=1$,
   $\varrho\approx74\%$ or $\approx92\%$ (§3.1). **Derived**
5. To the authors' knowledge these are the first explicit order-preserving
   mixed-precision methods (§3, after Def. 3.1). **Stated**
6. Running only the first RKC stage in high precision stagnates, because
   all $f(y_n+d_j)$, $j=1,\dots,s-1$, enter the $O(h)$ term (Remark 3.3).
   **Derived**
7. Under condition (21), a difference approximation accurate to
   $O(\epsilon h)$, the mixed-precision RKC (20) satisfies
   $y_{n+1}=y_n+hf(y_n)+O(\epsilon h^2+h^2)$, i.e. is 1-order-preserving
   for RKC1 and RKC2 coefficients (Thm 3.3, Eq. (57)). **Proved**
8. Under condition (24), accuracy $O(h^2)$, with RKC2 coefficients
   $y_{n+1}=y_n+hf+\frac12h^2f'f+O(h^3)$, i.e. 2-order-preserving
   (Thm 3.3, Eq. (58)). **Proved**
9. Under Assumption 3.2 (internal stability) and symmetric nonpositive
   definite $J$, the difference between exact and mixed-precision RKC obeys
   a one-step recursion (Eqs. (62), (63), (70)) whose constants depend
   neither on $s$ nor on the stiffness (Thms 3.4, 3.5). **Proved**
10. For RKC2 the constant $C_s=4s(s+1)/(s^2-1)$ (undamped) is decreasing
    in $s$ and $\le8$ (Lemma 3.2). **Proved** (exact undamped,
    approximate with damping)
11. Worst-case internal rounding error for linear symmetric negative
    definite $L$: $y_{n+1}=P_s(hL)y_n+r_s$ with $\lVert r_s\rVert_2$ bounded
    by $\max_k\lVert P_k(hL)-I\rVert_2((1+Chu)^{s-1}-1)\lVert y_n\rVert_2$
    (Thm 3.6, Eqs. (71)–(73)); hence the constant $\le2e^{2\bar Cs^2u}$ is
    small only if $s^2u=O(1)$ (Eq. (81)). **Proved**
12. In the asymptotic regime the mixed-precision stability constant behaves
    like $1+C\rho uh^2\le1+Cs^2uh$, versus $1+Cs^2u$ for RKC entirely in
    precision $u$ (Verwer et al.); the difference comes from order
    preservation (§3.6, Eqs. (84)–(86)). **Derived**
13. Under condition (24) the perturbation constant is $O(s^2)$ larger than
    under (21), so (24) must be used only in a convergence regime, which is
    the reason for the hybrid scheme (25) (Eqs. (82)–(83); Remark 3.7).
    **Derived**
14. No rigorous stability proof: rounding errors destroy the spectral
    relations between $y_n$ and $d_j$, and damping alone suffices only if
    the smallest eigenvalue of $hL$ is separated from 0 (§3.6). **Stated**
15. The finite-difference Jacobian action with $\delta=\sqrt u/h$
    (Eq. (32)) satisfies condition (21) with $\epsilon=\sqrt u$ (Eq. (33),
    Lemma A.1). **Proved**
16. The mixed-precision mRKC (98)–(101) needs one high-precision
    evaluation of the fast and slow parts per step and is 1-order-preserving
    (Thm 4.3, Eq. (105)); its finite-difference variant satisfies (101) with
    $\epsilon$ replaced by $\sqrt u+\epsilon$ if $h\le\sqrt u$ (Lemma B.2).
    **Proved**
17. The rounding-error analysis of mixed-precision mRKC is omitted as
    similar to RKC1; numerically mRKC is more stable than mixed-precision
    RKC1 (§4.3). **Stated** / **Shown** (qualitatively)
18. Stability test (2D heat, double/bfloat16, $s=2^{5+i}$, $i=0..4$): both
    standard and order-preserving mixed-precision RKC1/RKC2 are stable up to
    $s=512$, "as stable as the high-precision implementation" (§5.2.1,
    Fig. 1). **Shown**
19. Linear 3D heat, $\tilde q$-order-preserving RK4, $\tilde q\in\{0,1,2,3\}$:
    order $\tilde q$ recovered after a pre-asymptotic order-4 regime whose
    length grows with $\tilde q$; $\tilde q=1$ reduces the error by up to 4
    orders of magnitude (§5.2.2, Fig. 2). **Shown**
20. Nonlinear problems, bfloat16/double: order-preserving RKC1/RKC2 and
    mRKC1 recover full order; standard mixed precision stagnates at about
    $10u$ (Problems 1, 2), $100u$ (Problem 3) and $0.1u$ (Problem 4); the
    order-preserving methods are 2–8 orders of magnitude more accurate
    (§5.2.2, Figs. 3–6). **Shown**
21. Rounding versus discretization error as a function of $s$ (up to 512):
    order-preserving schemes keep rounding error at or below the
    discretization error; all mixed-precision schemes are stable for every
    $s$ tested, "more robust than our theory predicts" (§5.2.3,
    Figs. 7–9). **Shown**
22. Space–time convergence: order-preserving methods match fully-double
    convergence, standard mixed precision stagnates (§5.2.4,
    Figs. 10–11). **Shown**
23. Cost (Remark 5.3): implicit Euler with PETSc Newton and PCG/BoomerAMG
    needs about 54 high-precision matrix–vector equivalents per step,
    against 1 high- and 32 half-precision products for order-preserving
    RKC1 with $s=33$. **Shown** (operation count, not timing)
24. Low precision is emulated in software (libchopping); no CPU timings are
    reported (§5.1.5). **Stated**
25. Cost ratios: sparse $L$ with linear-cost nonlinearity gives $r=2$
    (double–single, single–half) and $r=4$ (double–half); dense $L$ or
    quadratic-cost nonlinearity up to $r=4$ and $r=16$ (§3.4). **Derived**
26. The approach extends to ROCK2/ROCK4 (Remarks 3.4, 3.6), to SDEs via
    SK-ROCK and SK-mROCK (Remarks 3.5, 4.1) and to incompressible
    Navier–Stokes via projection RKC (Example 3.1). **Stated**
27. The authors cannot build efficient mixed-precision three-term-recurrence
    stabilized methods that preserve more than order 2 (Remark 3.2).
    **Stated**

# Printed slips

- Eq. (96): "$\upsilon_1=T_m(\upsilon_0)/T_m'(\upsilon_1)$"; the argument
  of $T_m'$ should be $\upsilon_0$, as in Eq. (8); as printed it is
  circular.
- Proof of Theorem 3.5: "The proof is analogous to Theorem 4.3", which
  should be Theorem 3.4.
- Eq. (27) text "(i.e. ε = u)" and §3.3 "(again ε = u)" use the damping
  symbol $\varepsilon$ where the accuracy constant $\epsilon$ is meant.
- Example 3.1 writes $\hat\Delta_1f_j$, $\hat\Delta_2f_j$ for the
  $\hat\Delta_1g_j$, $\hat\Delta_2g_j$ of Eqs. (34)–(36); Eqs. (37)–(38)
  write $\hat v^j$ for $\hat v_j$.
- Remark 5.3: "the solution of Problem 3 required on average roughly 6
  preconditioned conjugate gradient iterations"; the remark concerns
  Problem 1 in 3D.
- Figs. 10–11 captions say "total error vs $\Delta t$", while the axes are
  labelled $\Delta x$.
- §5.2.4 writes $\beta_2(s_i,\frac2{13})$ for the $\beta^2$ of Eq. (12),
  and "Strategies 1 and 2" for "Scenario 1 and 2".
- Lemma 4.2 states $O(\eta)$ while its proof gives $O(\epsilon\eta+\eta^2)$;
  Lemma 3.2 uses $b_k/b_j<4/3$, Theorem 3.6 $b_k/b_j\le3/2$ (consistent).
- Ref. [4] printed "Numerische Mathematik 18 (2001)" (generally cited as
  volume 90); ref. [25] "Royal Society Open Science 9.3 (2021)"; refs. [5],
  [6] "(in press)". All recorded as printed.

# Notation map

| Croci & Rosilho de Souza (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y'=f(y)$, $y\in\mathbb R^n$ | $y'=f(y)$, $y\in\mathbb R^d$ | autonomous form |
| $\Delta t$ | $h$ | |
| $y^n$, $\hat y^n$ | $y_n$ | hat = computed in finite precision |
| $s$, $p$ | $s$, $p$ | agree |
| **$q$** | $\tilde q$ | **order preserved by the mixed-precision scheme; collides with stage order $q$** |
| $d_j$, $\hat d_j$ | $Y_j-y_n$ | delta-form stage increments |
| $f_F$, $f_S$ | $f^{\{\mathrm f\}}$, $f^{\{\mathrm s\}}$ | fast and slow parts |
| $f'$ | $J$ | Jacobian |
| $A$ (in $f=Ay+g$) | $L$ | **collides with the Butcher matrix $A$** |
| $R_s(z)$, $R_k$ | $P_s(z)$, internal $P_k$ | stability polynomial of an explicit method; $z=h\lambda$ agrees |
| $\ell_s^\varepsilon=2\omega_0/\omega_1$, $\beta^p(s,\varepsilon)$ | — | real stability boundary and its lower bound |
| $T_j$, $U_j$ | — | Chebyshev polynomials of the first and second kind; **$T$ collides with the tree set and the time slices $T_j$, $U_j$ with the Parareal iterate $U^{(k)}_j$** |
| $\mu_j,\nu_j,\kappa_j,\gamma_j$, $\omega_0,\omega_1$, $a_j$, $b_j$ | — | RKC recurrence coefficients; **$\nu_j$, $\gamma_j$, $a_j$, $b_j$ collide with the Courant number, Rosenbrock $\gamma$ and Butcher coefficients** |
| $c_j$ | $c_j$ | internal abscissae, $c_s=1$; agrees |
| **$\varepsilon$** | $\varepsilon_{\mathrm d}$ | **RKC damping; collides with the stiffness parameter $\varepsilon$** |
| $\epsilon$ | $\epsilon$ | accuracy constant of conditions (21), (100), (101), page-local |
| $u$ | — | unit roundoff $2^{-t}$; also the PDE unknown in §5 |
| $\rho$, $\rho_F$, $\rho_S$ | — | spectral radii |
| **$\eta$** | — | **mRKC averaging parameter; collides with the entropy $\eta$** |
| $\varphi(z)=(e^z-1)/z$ | $\phi_1(z)$ | agrees with the registry normalization |
| $\delta$ | — | finite-difference scaling $\sqrt u/h$; also the rounding error in Eq. (3) |
| "order reduction" | — | precision-induced loss of order, **not** stiff order reduction |
| "internal stability" | [internal stability](/definitions/internal-stability.md) | error propagation across the stages of one step |

# Reference list

The paper prints 76 references in numbered style, alphabetical by first
author. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` croci-2022. Many entries print only "et al." after the
first author; preprints without venue ([11], [12], [13], [18], [31]) are
kept with their printed years; ref. [5] has no printed year and takes the
citing year; ref. [10] is printed as a PhD thesis. No printed duplicates or
unparseable items.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Internal stability of explicit Runge–Kutta methods](/definitions/internal-stability.md)
* [Mixed-precision explicit Runge–Kutta methods](/methods/mixed-precision-runge-kutta.md)
* [Multirate Runge–Kutta–Chebyshev (mRKC) methods and the averaged-force modified equation](/methods/multirate-runge-kutta-chebyshev.md)
* [Order reduction](/definitions/order-reduction.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping](/methods/stabilized-explicit-runge-kutta.md)
