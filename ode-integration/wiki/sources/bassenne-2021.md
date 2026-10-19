---
type: Source
title: "Bassenne et al. (2021) — Time-Accurate and highly-Stable Explicit operators for stiff differential equations"
description: "Introduces TASE operators, rational preconditioners of the stiff linear(ized) operator built by Richardson extrapolation of (I - alpha h L)^(-1), which make an unchanged explicit Runge–Kutta method unconditionally or nearly unconditionally stable at the cost of p linear solves per evaluation, with stability theory and stiff PDE tests."
resource: "doi:10.1016/j.jcp.2020.109847"
source_kind: paper
authors: [Bassenne M., Fu L., Mani A.]
year: 2021
venue: "J. Comput. Phys. 424:109847"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_Journal_of_Computational_Physics_Bassenne_Time-Accurate_and_highly-Stable_Explicit_operators_for_stiff.pdf"
tags: [stiff, explicit, runge-kutta, stability, preconditioning, method-of-lines]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

The paper introduces [TASE operators](/methods/tase-operators.md), which
make an existing explicit integrator (nearly) unconditionally stable on
stiff linear or linearized terms without changing the integrator. The
system $y'=Ly$ is replaced by $y'=T^{(p)}_LLy$, where $T^{(p)}_L$ is a
rational function of $\alpha hL$ with $T^{(p)}_L=I+O(h^p)$. The first-order
operator $(I-\alpha hL)^{-1}$ comes from writing implicit Euler as explicit
Euler applied to $(I-hL)^{-1}Ly$. Higher orders follow by recursive
Richardson extrapolation in $\alpha$ (halving it), giving
$T^{(p)}_L=\sum_{k=0}^{p-1}\omega_{p,k}(2^kI-\alpha hL)^{-1}$, that is $p$
shifted linear solves per right-hand-side evaluation. The free parameter
is fixed by the necessary condition $\alpha\ge(2^p-1)/C$, where $C$ is the
negative-real-axis extent of the explicit scheme's stability region. On a
linear(ized) problem the combination is a linearly implicit method; the
reader notes its kinship with
[W-methods](/methods/rosenbrock-wanner-method.md), which the paper does not
draw.

For first-order TASE a sufficient condition $\alpha\ge\frac12\max
\beta_{ij}/\alpha_{ij}$ is proved through the
[Shu–Osher form](/methods/strong-stability-preserving-runge-kutta.md). For
general $p$ the [stability function](/definitions/stability-function.md) is
proved analytic in $\mathbb C^-$ and checked numerically on the imaginary
axis. Explicit Runge–Kutta methods with $s\le4$ stages and order $s$
combined with TASE of order $p\le s$, $p\le2$, are thus
[A-stable](/properties/a-stability.md) (proved for $p=1$, numerical for
$p=2$); for $p>2$ they are "nearly unconditionally stable", with
$\max\lvert R(iy)\rvert\approx1.02$.

Matlab tests cover the heat equation with a periodic source in three
stiffness scenarios, Dirichlet data entering as a source, a two-species
advection–diffusion–reaction system (when TASE may be split between
operators), nonlinear diffusion, the ODE $y'=-y^{10}$ through Jacobian
linearization, and 2D diffusion in polar coordinates. Steps $10$ to $10^4$
times the explicit limit keep the design order, and per-step timings
compare RK+TASE with SDIRK. The order claim rests on a non-stiff expansion;
[order reduction](/definitions/order-reduction.md) in the stiff regime is
not analysed.

# Version read

arXiv preprint arXiv:1911.08399v2 [math.NA], 5 August 2020 ("Preprint
submitted to Journal of Computational Physics, August 6, 2020"), 30 pages
(main text pp. 1–27, references pp. 27–29, Appendix A with Butcher tableaux
pp. 29–30). It is not the JCP version of record: page, section and equation
numbers are those of the arXiv v2, and the DOI is not printed on the copy.
Title and authors match Crossref. Figures are images; their content is
taken from captions and text.

# Key claims

Registry notation: $h$ step, $L$ the linear(ized) semi-discrete operator,
$z=h\lambda$ with $\lambda$ the original eigenvalue, $R(z)$ the stability
function of the preconditioned scheme (the source's $\sigma$), $s$ stages,
Shu–Osher coefficients $\alpha_{ij}$, $\beta_{ij}$ (the source's $a_{i,k}$,
$b_{i,k}$). Page-local: $\alpha$ the scalar TASE parameter (distinct from
the indexed Shu–Osher $\alpha_{ij}$), $T^{(p)}_L$ the TASE preconditioner,
$\omega_{p,k}$ its closed-form coefficients (the source's $\beta_{p,k}$),
$C$ the negative-real-axis stability limit of the explicit scheme.

1. $T^{(p)}_L=I+O(h^p)$, so the solution of $y'=T^{(p)}_LLy$ converges to
   that of $y'=Ly$ with order $p$; with $p$ equal to the explicit order,
   the global order is unaffected (§2.1, Eq. (5); §2.3). **Derived**
   (called "straightforward", no written proof)
2. Implicit Euler on $y'=Ly$ is identical to explicit Euler on
   $y'=(I-hL)^{-1}Ly$, motivating $T^{(1)}_L=(I-hL)^{-1}$ (§2.2,
   Eqs. (7)–(9)). **Derived**
3. Recursion: $T^{(p)}_L(\alpha,h)=[2^{p-1}T^{(p-1)}_L(\alpha/2,h)-T^{(p-1)}_L(\alpha,h)]/(2^{p-1}-1)$,
   $T^{(1)}_L=(I-\alpha hL)^{-1}$, $\alpha>0$ (§2.3, Eq. (10)). **Stated**
   (definition)
4. The leading error term of $T^{(p)}$ grows with $\alpha$, so
   $\alpha=\alpha_{\min}$ is recommended (§2.3; Fig. 7(b)). **Derived** /
   **Shown**
5. Explicit integration of $y'=T^{(p)}_\lambda\lambda y$ stays stable as
   $h\to\infty$ only if $\alpha\ge\alpha_{\min}=(2^p-1)/C$, since
   $hT^{(p)}_\lambda\lambda=-(2^p-1)/\alpha+O(h^{-1})$ (Thm 2.1,
   Eqs. (11)–(13)). **Proved** (asymptotic, necessary condition only)
6. $\alpha_{\min}$: RK1 ($C=2.00$) 0.50; RK2 ($C=2.00$) 0.50, 1.50; RK3
   ($C=2.50$) 0.40, 1.20, 2.80; RK4 ($C=2.79$) 0.36, 1.08, 2.51, 5.38 for
   $p=1,2,3,4$ (Table 1). **Stated** (computed; $C$ rounded, see Printed
   slips)
7. Schemes whose stability region is confined to the imaginary axis are
   incompatible with real $\alpha$ (§2.4). **Stated**
8. Closed forms: $T^{(p)}_L=\sum_{k=0}^{p-1}\omega_{p,k}(2^kI-\alpha hL)^{-1}$
   and $T^{(p)}_LL=\frac1{\alpha h}[-(2^p-1)I+\sum_{k=0}^{p-1}2^k\omega_{p,k}(2^kI-\alpha hL)^{-1}]$,
   with $\omega_{p,k}$: $p=1$: 1; $p=2$: $-1,4$; $p=3$: $\frac13,-4,\frac{32}3$;
   $p=4$: $-\frac1{21},\frac43,-\frac{32}3,\frac{512}{21}$ (§2.5,
   Eqs. (14)–(15), Tables 2–3). **Stated** (reader check:
   $\sum_k\omega_{p,k}=2^p-1$, $\sum_k2^{-k}\omega_{p,k}=1$)
9. TASE needs $p$ linear solves per right-hand-side evaluation, so the
   per-step cost is "at least comparable" to implicit schemes; the gain
   must come from larger $h$ (§2.5). **Stated**
10. Stability diagrams: $s$-stage order-$s$ RK ($s=1..4$) with TASE of
    order 1 or 2 at $\alpha_{\min}$ map the whole left half-plane into the
    RK stability region; TASE of order $p>2$ leaves tiny unstable regions
    near the imaginary axis, at eigenvalues whose imaginary part is about
    100 times the real part (§2.6, Figs. 1–2). **Shown**
11. With $\alpha<\alpha_{\min}$ large unstable regions appear in
    $\mathbb C^-$ for RK4 + TASE1–4; with $\alpha>\alpha_{\min}$ the
    residual regions shrink (§2.6, Fig. 3). **Shown**
12. Explicit Euler on $y'=T^{(1)}_\lambda\lambda y$ is the $\theta$-method
    with $\theta=\alpha$, $R(z)=(1+(1-\alpha)z)/(1-\alpha z)$, unconditionally
    stable iff $\alpha\ge\frac12$ (Lemma 3.3, Eqs. (17)–(18)). **Proved**
13. Any explicit RK in Shu–Osher form with $\alpha_{ij}\ge0$,
    $\beta_{ij}\ge0$, applied to the first-order TASE system, is
    unconditionally stable if $\alpha\ge\frac12\max_{i,j}\beta_{ij}/\alpha_{ij}$
    (Thm 3.2 via Lemma 3.4, Eqs. (19)–(21)). **Proved** (sufficient)
14. For linear SSP RK methods up to order 4, $\max\beta_{ij}/\alpha_{ij}=1$,
    giving $\alpha_{\min}=0.5$ for every order; this is more restrictive
    than the necessary 0.40 (RK3) and 0.36 (RK4), and the necessary value
    "works well in practice" (§3.1). **Proved** (the 0.5) / **Stated**
15. For any order of TASE and RK, $R(z)=N(z)/Q(z)$ with
    $Q(z)=\prod_{i=0}^{p-1}(2^i-\alpha z)^s$, analytic in $\mathbb C^-$
    because the poles $2^i/\alpha$ are positive real (§3.2(a),
    Eqs. (24)–(27)). **Proved**
16. $\lvert R(iy)\rvert\le1$ is not proved analytically but checked by
    sampling (Fig. 4); where the method is only nearly unconditionally
    stable, $\max\lvert R\rvert\approx1.02$ (§3.2(b)). **Shown**; the
    abstract's "unconditionally stable for $p\le s$, $p\le2$" rests on this
    check for $p=2$.
17. Scenario 1 (over-resolved heat equation, RK2 + TASE2 against RK2 and
    SDIRK2): at $N=600$ TASE runs at $6.08\cdot10^3$ times the explicit
    limit with profiles indistinguishable at plotting accuracy; second
    order preserved; error slightly larger than explicit and than SDIRK2
    (§4.1.1, Fig. 5). **Shown**
18. Per-step cost ($N=600$, Matlab): with precomputed inverses RK+TASE is
    "in general slightly better" than SDIRK of the same order; with
    on-the-fly solves it is more expensive ($p$ solves per stage against
    one) (§4.1.1, Table 4). **Shown** (hardware not stated)
19. Scenario 2 (steady state, RK4 + TASE4 against SDIRK4, Fourier, $N=6$):
    fourth order preserved; steps up to 8.07 times the limit give an
    accurate final state (§4.1.2, Fig. 6). **Shown**
20. Scenario 3 (quasi-steady stiff physics, RK2 + TASE2 against SDIRK2):
    steps 0.75, 7.5 and 75 times the limit capture the slow source
    oscillation; larger $\alpha$ keeps the order but increases the error
    (§4.1.3, Fig. 7). **Shown**
21. Boundary data entering as a source $S$ must be preconditioned together
    with $Ly$, $y'=T^{(p)}_L(Ly+S)$, to preserve the steady state
    $Ly+S=0$; preconditioning only $Ly$ keeps the order but produces large
    errors from the boundaries (§4.2, Eq. (32), Fig. 8). **Derived** /
    **Shown**
22. For several stiff operators, the combined form
    $T^{(p)}_{L_1+L_2}(L_1+L_2)y$ is required when they compete in a
    quasi-steady balance; the split form is acceptable otherwise; the
    combined form is always safe (§4.3.1, Eqs. (34)–(35)). **Stated**, then
    **Shown** on the two-species ADR problem (Fig. 9)
23. Nonlinear problems: $y'=T^{(p)}_{J}f(y)$ with $J$ the Jacobian at the
    current state reaches arbitrary order with linear solves only, no
    nonlinear system (§4.4.1, Eqs. (42)–(43)). **Stated**; order
    preservation **Shown** for Eqs. (44) and (46)
24. Nonlinear diffusion $\partial_ty=\partial_x(\frac{y^\beta}{2}\partial_xy)$,
    $\beta\in\{0,0.25,1,4\}$: RK4 + TASE4 stable and accurate at 9.56 times
    the limit; per step RK+TASE 2.1–40 ms, SDIRK (Matlab fsolve)
    237–1303 ms, RK 0.6–1.5 ms (§4.4.2, Fig. 10, Table 5). **Shown**
25. $y'=-y^{10}$ to $t=2\cdot10^4$: RK2 + TASE2 at $10^3$ and $10^4$ times
    the limit (0.2) cuts the steps from $10^5$ to $10^2$ and $10$, stable,
    with RK2 order preserved (§4.4.3, Fig. 11). **Shown**
26. 2D diffusion in polar coordinates ($N_r=10$, $N_\theta=40$): at
    $h=2\cdot10^{-3}$, 50 times the azimuthal limit, the explicit solution
    blows up near the pole, while TASE on the azimuthal operator only is
    visually exact (§4.5, Fig. 12). **Shown** (qualitative)
27. Background: A-stable linear multistep methods are at most second
    order; IMEX-RK accuracy is "typically limited to be lower than fifth";
    splitting for reacting flow is "typically limited to second order"
    (§1). **Stated**
28. Limitations: no rigorous stability proof for general high-order
    preconditioned explicit methods, and the cost of $p$ inversions per
    stage may outweigh the benefit for very high orders (§5). **Stated**

Reader remarks recorded with the notes: Theorem 3.2 for $s=4$ relies on a
linear-SSP Shu–Osher realization of $\sum_{k\le4}z^k/k!$, legitimate only
for linear constant-coefficient problems, since no 4-stage fourth-order
nonlinear SSP method exists; the A-stability analysis assumes
diagonalizable $L$, which does not give strong stability for non-normal
operators; the order claim is a non-stiff Taylor statement, so later
sources may contradict "preserved order" in the stiff regime.

# Printed slips

- Proof of Thm 3.2: "From lemma 3.2, we conclude … is unconditionally
  stable if only if $\alpha_{i,k}\ge0.5$"; there is no Lemma 3.2 (it is
  Lemma 3.3), and "if only if" should be "if and only if".
- §3.1 end: "provided in provided in Section 2.3"; the necessary condition
  is derived in §2.4.
- Table 1 rounds $C$: the true intercepts are $C\approx2.5127$ (RK3) and
  $C\approx2.7853$ (RK4) (reader's computation). The RK4 value is rounded
  up, so the printed $\alpha_{\min}$ 2.51 ($p=3$) and 5.38 ($p=4$) lie
  slightly below the exact thresholds 2.513 and 5.385; this may contribute
  to the $\max\lvert R\rvert\approx1.02$ (not verified).
- §4.5: the text says the baseline is fourth-order RK (Table A.9), the
  Fig. 12 caption says RK2 and RK2 + TASE2.
- §4.4.3: "The PDE is numerically solved", though Eq. (46) is an ODE.
- §4.1.2: "a factor fo 10 only", while the stated ratio is 15.
- §4.2.2: the TASE run is quoted at $6.08\cdot10^1=O(10^2)$ times the
  limit, the comparison at 100.
- §4.5 switches the unknown from $y$ to $T(r,\theta,t)$; Eq. (47) writes
  $L_y(\cdot)=-\beta y^{\beta-1}$ without the argument on the right.
- §4.1.1: "The error of the TASE method is slightly superior to that of
  the explicit method", meaning larger.
- Table 4: some RK+TASE timings with precomputed inverses are lower than
  plain RK of the same order (e.g. order 4: RK 20, TASE $p=3,4$: 16),
  likely timing noise.
- Ref. [57] prints the authors as "I. F. Z. Zlatev, Á. Havasi".

# Notation map

| Bassenne et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $dY/dt=F(X,t,Y)$, $Y$ | $y'=f(t,y)$, $y$ | semi-discrete system; $X$ is the grid |
| $dY/dt=LY$, $L$ | $y'=Ly$, $L$ | agrees |
| $\Delta t$ | $h$ | |
| $\sigma(z)$, $z=\lambda\Delta t$ | $R(z)$, $z=h\lambda$ | $\lambda$ is the original, not the preconditioned, eigenvalue |
| $S$ (set), $\mathbb C^-$ | $\mathcal S$, $\mathbb C^-$ | stability region |
| **$T^{(p)}_L(\alpha,\Delta t)$** | $T^{(p)}_L$ | TASE preconditioner, page-local; **$T$ collides with the tree set** |
| $\mathbb T^{(p)}_L=T^{(p)}_LL$ | $T^{(p)}_LL$ | modified operator |
| $p$ | — | order of the TASE operator, $T=I+O(h^p)$; **not the RK order** (the source's RK order equals $s$) |
| $s$ | $s$ | stages = order of the explicit RK, $s\le4$ |
| **$\alpha$** | $\alpha$ | TASE parameter; **collides with Shu–Osher $\alpha_{ij}$ and Rosenbrock $\alpha_{ij}$** |
| **$\beta_{p,k}$** | $\omega_{p,k}$ | **closed-form coefficients; collide with Shu–Osher $\beta_{ij}$** |
| **$\gamma_{p,k}$** | $2^k\omega_{p,k}$ | **collide with the Rosenbrock $\gamma_{ij}$** |
| $C$ | — | negative-real-axis stability limit of the explicit scheme; **not the SSP coefficient $\mathcal C$** |
| **$a_{i,k}$, $b_{i,k}$** | $\alpha_{ij}$, $\beta_{ij}$ | Shu–Osher coefficients; **collide with Butcher $A$, $b$** |
| $y^{(i)}$ | — | Shu–Osher stage values |
| $A_{s,k}$ | $\theta_{k+1}$ of $P(z)$ | coefficients of the explicit stability polynomial ($1/(k+1)!$ for order $s$) |
| $P(z)$, $Q(z)$ | — | numerator and denominator of $R(z)$; **$P$ collides with the stability polynomial**, written $N(z)$ above |
| $L_Y$ | $J$ | Jacobian of the nonlinear operator $N[Y]$ |
| $S$ (vector) | — | boundary source; same letter as the stability region |
| $\Delta t_{\rm stability}=C\Delta x^2/D$ | — | explicit limit for diffusion |
| **$T(r,\theta,t)$** | — | **polar-test unknown; reuses $T$** |
| "unconditionally stable" | A-stable | in the original $z$ |

# Reference list

The paper prints 62 references in numbered style, in order of first
citation. All are merged complete into the [bibliography](/bibliography.md)
with `citedby` bassenne-2021. Refs. [52] (Eberly, Geometric Tools) and [62]
(Kennedy & Carpenter DIRK review, NASA) are undated and keyed by the citing
year; ref. [1] prints a mis-parsed second author "G. Mathématicien";
ref. [37] prints the authors as "G. Wanner, E. Hairer" and is merged into
the Hairer–Wanner II entry `hairer-1996`;
ref. [57] has a garbled author list; ref. [59] is a volume of collected
lectures; ref. [34] is a technical report. No DOIs are printed and there
are no printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Order reduction](/definitions/order-reduction.md)
* [Rosenbrock–Wanner (ROW) and W-methods](/methods/rosenbrock-wanner-method.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [TASE operators: time-accurate and highly stable explicit operators](/methods/tase-operators.md)
