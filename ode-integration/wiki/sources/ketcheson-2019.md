---
type: Source
title: "Ketcheson (2019) — Relaxation Runge–Kutta methods: conservation and stability for inner-product norms"
description: "Develops relaxation Runge–Kutta methods for inner-product norms: scales each update by an explicit relaxation parameter so that energy is conserved or dissipated exactly, places the result at t_n + γ_n h to keep order p, and shows enlarged stability regions and preserved SSP coefficients."
resource: "doi:10.1137/19M1263662"
source_kind: paper
authors: [Ketcheson D.I.]
year: 2019
venue: "SIAM J. Numer. Anal. 57(6):2850-2870"
local_file: "/home/stefano/papers/mosaic/ode-integration/2019_Crossref_SIAM_Journal_on_Numerical_Analysis_Ketcheson_Relaxation_Runge--Kutta_Methods_Conservation_and_Stability_f.pdf"
tags: [relaxation, structure-preserving, runge-kutta, explicit, entropy-stability, ssp]
timestamp: 2026-10-29T18:13:00Z
---

# Summary

For an ODE that is dissipative, $\langle y,f(t,y)\rangle\le0$, or conservative,
$\langle y,f\rangle=0$, in an inner-product norm, a Runge–Kutta step changes
$\lVert y\rVert^2$ by the "correct" production
$2h\sum_jb_j\langle Y_j,f_j\rangle$ plus a spurious quadratic form
$-h^2\sum m_{ij}\langle f_i,f_j\rangle$, with $M=BA+A^\top B-bb^\top$. The paper
states that explicit methods can be neither algebraically stable nor
symplectic ([A- and algebraic stability](/properties/a-stability.md),
[symplecticity](/properties/symplecticity.md)). The
[relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md) (RRK) method
scales the update by $\gamma_n$, given by an explicit formula that cancels the
spurious terms exactly. Ketcheson (2019, §1) credits the idea to Dekker &
Verwer (1984, pp. 265–266) for classical RK4, with later development by Del
Buono & Mastroserio (2002) and Calvo et al. (2006). The paper's own step is to
read the relaxed solution as an approximation at $t_n+\gamma_nh$, not at
$t_n+h$.

The relaxed method is conservative, and with $b\ge0$ it preserves
monotonicity of the norm while $\gamma_n\ge0$ ([strong stability](/properties/strong-stability.md),
[entropy stability](/properties/entropy-stability.md) for quadratic
entropies). Since $\gamma_n=1+O(h^{p-1})$, proved with
[B-series](/definitions/b-series.md) and the
[order conditions](/results/runge-kutta-order-conditions.md), the RRK
interpretation keeps order $p$, while the incremental direction technique
(IDT) of Calvo et al., which places the result at $t_n+h$, has order $p-1$.
The [stability function](/definitions/stability-function.md) of a relaxed
step is $1+\gamma(R(z)-1)$; the stability region grows monotonically as
$\gamma$ decreases. The [SSP](/methods/strong-stability-preserving-runge-kutta.md)
coefficient is unchanged for $0\le\gamma\le\gamma_*$. The conclusions state
that [embedded error estimators](/methods/embedded-runge-kutta-pair.md) and
[dense output](/methods/dense-output.md) of the base method carry over. Tests
use Fourier-spectral [linear advection](/benchmarks/linear-advection-equation.md),
a non-normal $3\times3$ matrix, a nonlinear oscillator, and the inviscid
[Burgers equation](/benchmarks/burgers-equation.md) with an energy-conservative
and a dissipative flux.

# Version read

arXiv:1905.09847v1 [math.NA], 23 May 2019, 23 pages, all read (equation pages
4–12 checked visually). This is the author preprint, not the SIAM version of
record; the preprint prints no DOI, and its ref. [22] (Ranocha et al.) reads
"To appear on arXiv". The printed title capitalizes as "Relaxation
Runge-Kutta Methods: Conservation and stability for Inner-Product Norms"; the
published title differs only in capitalization and dash. Section, equation,
theorem and figure numbers on this page are those of arXiv v1.

# Key claims

Registry notation: $h$ is the step (source $\Delta t$), $y_n$ and $Y_i$ the
solution and the stage values (source $u^n$, $y_i$), $f_i=f(t_n+c_ih,Y_i)$,
$\gamma_n$ the relaxation parameter and $y^\gamma_{n+1}$ the relaxed solution
(source $u^{n+1}_\gamma$), $\tau$ a rooted tree with order $\lvert\tau\rvert$
and density $\gamma(\tau)$ (source $t$, $\rho(t)$, $\gamma(t)$), $\theta_k$
the coefficients of $P(z)=1+\sum_k\theta_kz^k$ (source $\alpha_k$).
"Monotonicity preserving" means $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ for
every dissipative problem; "conservative" means $\lVert y_{n+1}\rVert=\lVert y_n\rVert$
for every conservative problem (§1, Eqs. (2)–(5)).

1. For any Runge–Kutta method,
   $\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=2h\sum_jb_j\langle Y_j,f_j\rangle-2h^2\sum_{i,j}b_ia_{ij}\langle f_j,f_i\rangle+h^2\sum_{i,j}b_ib_j\langle f_i,f_j\rangle$
   (Eq. (7)); the last two terms are $-h^2\sum m_{ij}\langle f_i,f_j\rangle$
   with $M=BA+A^\top B-bb^\top$, $B=\mathrm{diag}(b)$ (Eq. (8)). **Derived**
2. "explicit methods cannot be algebraically stable or symplectic" (§1.1,
   p. 4). **Stated**
3. For conservative problems "no explicit Runge–Kutta method of any order can
   enforce discrete conservation, even for linear autonomous problems"; for
   nonlinear autonomous dissipative systems "no methods of order greater than
   one are known to be monotonicity preserving" (§1, p. 2). **Stated**
4. Ketcheson (2019, §1, p. 2) credits the approach to Dekker & Verwer
   ("originally proposed by Dekker & Verwer [7, pp. 265-266], who noted that
   the classical four-stage RK method could be modified slightly to conserve
   energy while maintaining its accuracy"), its extension to a class of
   fourth-order methods to Del Buono & Mastroserio (2002), and the proof of
   order at least $p-1$ without step-size adjustment to Calvo et al. (2006).
   The paper calls the methods "not entirely new". **Stated**
5. With
   $\gamma_n=\dfrac{2\sum_{i,j}b_ia_{ij}\langle f_i,f_j\rangle}{\sum_{i,j}b_ib_j\langle f_i,f_j\rangle}$
   (and $\gamma_n=1$ when $\lVert\sum_jb_jf_j\rVert=0$) (Eqs. (11)–(12)), the
   relaxed update $y^\gamma_{n+1}=y_n+\gamma_nh\sum_jb_jf_j$ (9) satisfies
   $\lVert y^\gamma_{n+1}\rVert^2-\lVert y_n\rVert^2=2\gamma_nh\sum_jb_j\langle Y_j,f_j\rangle$
   (§2). **Derived**. The name comes from the relaxation parameter of
   iterative solvers; for conservative systems $\gamma_n$ is the nonzero root
   of a quadratic energy change with one root at zero, a line search (p. 5).
6. Lemma 1: if $\sum b_ia_{ij}>0$ and $f$ is smooth, $\gamma_n>0$ for small
   enough $h$; the condition holds for every method of order $\ge2$ (§2,
   pp. 4–5). **Stated** ("straightforward to show"; no proof printed)
7. Remark 1: "small enough" means $h$ "no more than about $1/L$", with $L$ the
   Lipschitz constant of $f$, the size of the absolutely stable step of any
   explicit method (p. 5). **Stated**
8. Theorem 2: for a base method of order $\ge2$, RRK is conservative; with
   nonnegative weights it is monotonicity preserving "as long as $\Delta t$ is
   chosen so that $\gamma_n\ge0$" (p. 5). **Proved**
9. Remark 2: RRK conserves linear invariants (p. 5). **Stated**
10. Remark 4: computing $\gamma_n$ costs $s+1$ inner products; the numerator
    trick is credited to Ranocha (private communication) (p. 5, §5).
    **Stated**
11. Theorem 3: if $\gamma_n=1+O(h^{p-1})$ and the base method has order $p$,
    the IDT interpretation ($y^\gamma_{n+1}\approx y(t_n+h)$) has order $p-1$
    and the RRK interpretation ($y^\gamma_{n+1}\approx y(t_n+\gamma_nh)$) has
    order $p$ (§2.1, p. 6). **Proved** (with the order conditions written, after
    Albrecht, as $b^\top c^{k-1}=1/k$, $k\le p$, plus $b^\top v=0$ for
    $v\in V_p$, Eq. (14))
12. Lemma 4: with $\gamma_n$ from (12), $\gamma_n=1+O(h^{p-1})$ for every
    Runge–Kutta method of order $p$ (§2.1; proof pp. 8–9 by B-series, through
    the identity (19) on pairs of trees with $\lvert\tau_1\rvert+\lvert\tau_2\rvert\le p-2$).
    **Proved**. Remark 5 notes a proof for a family of four-stage fourth-order
    methods by Del Buono & Mastroserio; Remark 7 points to a generalization
    without B-series in Ranocha et al.
13. Corollary 5: RRK has order $p$, IDT order $p-1$; Remark 6 notes that the
    IDT part was proved by other means by Calvo et al. (p. 7). **Proved**
14. On the nonlinear oscillator, $\max\lvert\gamma-1\rvert$ decays at least as
    $O(h^{p-1})$; for SSPRK(2,2) and RK(4,4) "at one order higher than
    expected", which the paper attributes to the symmetry of the problem
    (Fig. 1, p. 7). **Shown**
15. RRK is a projection method along $y_{n+1}-y_n$ with step length
    $1-\gamma_n$, but "the existing formalism for such methods does not
    include the possibility of interpreting the new solution as an
    approximation at a time different from $t_n+\Delta t$"; projecting time as
    well, after autonomization, gives $t_n+\gamma_nh$ (§2.2, p. 9). **Derived**
16. A relaxed step with fixed $\gamma$ has stability function
    $R_\gamma(z)=1+z\gamma b^\top(I-zA)^{-1}\mathbf 1=1+\gamma(R(z)-1)$
    (Eq. (21), §3.1). **Derived**
17. Theorem 7: for $0\le\gamma_1\le\gamma_2$ the stability region of
    $(A,\gamma_2b)$ is contained in that of $(A,\gamma_1b)$, and it tends to
    $\mathbb C$ as $\gamma\to0$ (§3.1, p. 10). **Proved**
18. For any RRK method of order $p\ge2$, the E-polynomial
    $E_\gamma(y)=1-\lvert R_\gamma(iy)\rvert^2$ is
    $\sum_{j=1}^{p/2}\frac{2}{(2j)!}\gamma(1-\gamma)y^{2j}+O(y^{p+2})$, so for
    $\gamma\in[0,1)$ the stability region contains an imaginary-axis segment
    around 0, even for two-stage second-order methods whose unrelaxed region
    contains none (§3.1, p. 11). **Derived**
19. For $0\le\gamma\le1$, $\mathcal C(A,\gamma b)\ge\mathcal C(A,b)$, because
    the relaxed solution is a convex combination of $y_n$ and $y_{n+1}$
    (§3.2, p. 12). **Derived**
20. Lemma 8 and Theorem 9: if $(A,b)$ is absolutely monotonic at $-r$, then
    $(A,\gamma b)$ with $\gamma\ge0$ is iff $R_\gamma(-r)\ge0$; hence
    $\mathcal C(A,\gamma b)\ge\mathcal C(A,b)$ for
    $0\le\gamma\le\gamma_*=-1/(R(-\mathcal C)-1)$, with $\gamma_*\ge1$ (p. 12).
    **Proved**. Here $\mathcal C$ is the radius of absolute monotonicity,
    from the conditions (22) of Ferracina & Spijker.
21. Table 1: $\gamma_*=2$ for SSPRK(2,2), $s/(s-1)$ for SSPRK($s$,2), $3/2$ for
    SSPRK(3,3), 1 for SSPRK(4,3), SSPRK(5,3), SSPRK(9,3), 1.312 for
    SSPRK(5,4), 25/24 for SSPRK(10,4); "direct computation shows that
    $\mathcal C(A,\gamma b)=\mathcal C(A,b)$ for $0\le\gamma\le\gamma_*$, while
    taking $\gamma>\gamma_*$ leads to a decrease in the SSP coefficient"
    (p. 12). **Shown** (computed). *(compiler check, not in the sources:
    SSPRK(2,2) has $\mathcal C=1$ and the stability polynomial $1+z+\frac{z^2}2$, unique for
    two stages and order 2 (Gottlieb et al. 2001, Prop. 3.2), so $R(-1)=\frac12$ and
    $\gamma_*=-1/(\frac12-1)=2$.)*
22. Fourier-spectral advection with 128 modes: RRK(4,4) with white-noise data
    damps high wavenumbers and amplifies some low ones while keeping the total
    energy; with smooth data its amplification is "nearly indistinguishable"
    from RK4; at $1.02$ times the linear step limit RRK "greatly amplifies the
    highest-wavenumber mode" (§4.1, Fig. 3). **Shown**
23. RRK(4,4) stays stable beyond the linear step limit, but 1.016 times the
    limit gives "highly inaccurate and oscillatory" solutions at $t=400\pi$;
    there $\gamma$ stays within $10^{-2}$ of 1, and from about 1.25 times the
    limit $\gamma\to0$ within a few steps and the run never completes
    (§4.1, Fig. 4, Remark 8). **Shown**
24. Sun–Shu non-normal problem (25): at $h=0.5$ the largest singular value of
    $R(hA)$ for RK(4,4) is "approximately 1.001", one step from the first right
    singular vector increases the energy (more at $h=0.7$), and RRK(4,4) is
    monotone at both steps (§4.2, Fig. 5). **Shown**
25. Nonlinear oscillator (26): SSPRK(3,3) energy increases monotonically for
    every positive step (stated, citing Ranocha), other explicit methods show
    growth or decay, the RRK versions conserve energy to roundoff and are "on
    par with or more accurate than the original method" in convergence
    (§4.3, Figs. 6–7). **Shown**
26. Burgers with the energy-conservative flux (28): RRK conserves energy to
    roundoff to $t=0.2$ at $h=0.3\Delta x$; at $t=0.03$ the RRK methods reach the
    base order while the IDT methods lose one order "as predicted by Theorem 3"
    (Fig. 9 caption: "in some cases") (§4.4.1, Figs. 8–9). **Shown**
27. Burgers with the dissipative flux (29), $\epsilon=1/100$, $h=0.2\Delta x$:
    relaxation "dramatically improves the numerical approximation of the
    global dissipation"; the unrelaxed methods show "excessive dissipation,
    due to numerical errors" (§4.4.2, Figs. 10–11). **Shown**
28. Conclusions: the technique applies to implicit methods; embedded error
    estimators and dense output of the base method can be used unchanged
    (dense-output times rescaled); with entropy-stable spatial
    discretizations RRK gives "a fully-discrete, explicit scheme that is
    provably entropy stable (for quadratic entropies)" (§5). **Stated**
29. "it is clear that in practice one should always use the latter
    interpretation" (RRK over IDT) (§5, p. 22). **Stated**

# Printed slips

- §1.1, p. 3: "We make the usual assumption that $c_j=\sum_i a_{ij}$"; the
  row-sum convention sums over $j$, $c_i=\sum_ja_{ij}$.
- §2, p. 5: "$\Delta E(\gamma):=\|u^{n+1}_\gamma\|^2-\|u^{n+1}\|^2=0$, which is a
  quadratic function of $\gamma$ with one root at zero": the root at
  $\gamma=0$ holds with $\|u^n\|^2$ in the second term
  ($u^{n+1}_0=u^n$). A few lines later $\Delta E(1)$ denotes the exact energy
  change $\|u(t_n+\Delta t)\|^2-\|u(t_n)\|^2$.
- Proof of Theorem 3, p. 6: "$\gamma_n(b^Tc^{k-1}-\gamma_n^{k-1}/k)=\frac{\gamma_n}{k}(1-(1+\Delta t^{(k-1)(p-1)}))=O(\Delta t^{(k-1)(p-1)})$".
  From $\gamma_n=1+O(h^{p-1})$, $\gamma_n^{k-1}-1=O(h^{p-1})$, and
  $O(h^{p-1})\cdot O(h^k)=O(h^{p+k-1})$ with $p+k-1\ge p+1$ for $k\ge2$
  *(compiler check, not in the sources)*; the conclusion of order $p$ is
  unchanged.
- p. 8: "$\beta_{ij}(t_1,t_2)=\sum_ka_{ik}\Phi_k(t_1)\sum_la_{jl}\Phi_j(t_2)$"
  leaves the index $l$ unused ($\Phi_l(t_2)$ in the second factor).
- p. 8: the series printed for $f_i$,
  "$\sum_{q=1}^\infty\frac{\Delta t^q}{q!}\sum_{t\in LT_q}\gamma(t)\sum_ka_{ik}\Phi_k(t)F(t)(u_0)$",
  starts at $q=1$ and so has no $h^0$ term, while $f_i=f(t_n+c_ih,Y_i)\to f(t_n,y_n)$ as
  $h\to0$ *(compiler check, not in the sources)*; the expansion of
  $\langle f_i,f_j\rangle$ that follows uses the coefficients
  $\Phi_i(t_1')\Phi_j(t_2')$ of grafted trees.
- Corollary 5, p. 7: "$\|u^1_\gamma-u(\gamma_1\Delta t)\|$" indexes the first
  step with $\gamma_1$, while (9) gives $\gamma_0$ for the step from $t_0$.
- "In case the the denominator" (p. 4); "little compensation is need"
  (§4.1); ref. [13] prints "Nø rsett" and "{I}".
- Ref. [9]: "Mathematics of Computation, 249:201–219, 2005", where 249 is the
  issue number of volume 74.

# Notation map

| Ketcheson (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u(t)$, $u^n$ | $y(t)$, $y_n$ | |
| $f(t,u)$ | $f(t,y)$ | non-autonomous; autonomized in §2.2 |
| $\Delta t$ | $h$ | |
| $y_i$ | $Y_i$ | stage values; **$y$ is the registry solution** |
| $f_i$ | $f_i=f(t_n+c_ih,Y_i)$ | stage derivatives |
| $a_{ij}$, $b_j$, $c_j$, $A$, $e$ | $a_{ij}$, $b_j$, $c_j$, $A$, $\mathbf 1$ | printed $c_j=\sum_ia_{ij}$ (Printed slips) |
| $B=\mathrm{diag}(b)$, $M=BA+A^TB-bb^T$ | same | algebraic-stability matrix; **$M$ is the registry mass matrix** |
| $\gamma_n$, $\gamma$ | $\gamma_n$ | relaxation parameter; **$\gamma(t)$ is also the tree density in §2.1** |
| $u^{n+1}_\gamma$ | $y^\gamma_{n+1}$ | relaxed solution |
| $t$, $t'$, $[t_1,t_2]$ | $\tau$, $\tau'$, $[\tau_1,\tau_2]$ | rooted trees; $t$ is also time |
| $\rho(t)$, $\gamma(t)$, $\Phi_j(t)$, $F(t)$ | $\lvert\tau\rvert$, $\gamma(\tau)$, $\Phi_j(\tau)$, $F(\tau)$ | |
| $V_p$ | — | vectors encoding the non-bushy order conditions (after Albrecht) |
| $\beta_{ij}(t_1,t_2)$, $\delta$, $\eta$ | — | proof quantities of Lemma 4; **$\beta_{ij}$ is not a Shu–Osher coefficient, $\eta$ is not the entropy** |
| $R(z)$, $R_\gamma(z)$ | $R(z)$, $R_\gamma(z)$ | base and relaxed stability functions |
| $\alpha_k$ | $\theta_k$ | coefficients of an explicit $R(z)=1+\sum\alpha_kz^k$; **$\alpha$ is the registry Shu–Osher letter** |
| $S(A,b)$ | $\mathcal S$ | absolute stability region |
| $E(y)$, $E_\gamma(y)$ | — | E-polynomial $1-\lvert R(iy)\rvert^2$; **$y$ here is a real variable** |
| $I(A,b)$ | — | length of the imaginary stability interval |
| $\mathcal C(A,b)$ | $\mathcal C$ | radius of absolute monotonicity |
| $\gamma_*$ | — | largest $\gamma$ that keeps $\mathcal C$ (Theorem 9) |
| $L$ | — | Lipschitz constant (Remark 1); **$L$ is the registry linear operator** |
| $\lambda$, $\Phi$ | — | projection length and direction (§2.2); **$\Phi$ is the registry elementary weight** |
| $D$ | $L$ | Fourier-spectral differentiation matrix, skew-Hermitian |
| $\mu$ | — | $\Delta t/\Delta t_{\max}$, the ratio to the linear step limit |
| $m$ | $d$ | number of grid points (ODE dimension) |

# Reference list

The preprint prints 27 references in numbered alphabetical style
([1]–[27]). All are merged complete into the [bibliography](/bibliography.md)
with `citedby` ketcheson-2019. Pre-publication and non-journal items are kept
as their own entries: [19] Ranocha (2018, no venue printed), [20] Ranocha
(private communication, 2019), [22] Ranocha et al. ("To appear on arXiv",
2019) and the arXiv preprint [25]. [21] (Ranocha & Öffner, J. Sci. Comput.,
2018) prints "pages 1–17" without a volume; [9] prints the issue number 249
as the volume. No DOIs are printed.

# Pages created or updated

Chunk 7 (2026-10-29). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [B-series, composition and substitution laws](/definitions/b-series.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Dense output](/methods/dense-output.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Energy method for Runge–Kutta stability](/methods/runge-kutta-energy-method.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Strong stability (monotonicity) of Runge–Kutta methods for linear seminegative problems](/properties/strong-stability.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
