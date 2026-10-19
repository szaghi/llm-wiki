---
type: Method
title: "Padé-based high-order implicit time integration of structural dynamics"
description: "Song and Eisenträger replace the matrix exponential of the exact one-step map of linear structural dynamics by its $(m,m)$ diagonal Padé approximant, giving one-step schemes of order $2m$ solved as $m$ shifted Newmark-like systems, one real or one complex system per root or conjugate pair."
status: established
aliases: [Padé time-stepping, Padé expansion time integration, rational approximation time stepping, O(M,M) scheme]
tags: [implicit, linear-algebra, stability, exponential]
timestamp: 2026-10-19T23:00:00Z
---

# Padé-based high-order implicit time integration of structural dynamics

For the linear semi-discrete equations of structural dynamics
$M\ddot u+C\dot u+Ku=f(t)$ (page-local: $u$ the displacement vector, $C$ and $K$ the
damping and stiffness matrices, $f$ the load; $M$ is the registry's mass matrix),
[Song & Eisenträger (2022)](/sources/song-2022.md) write the exact one-step map in
state-space form, replace its matrix exponential by the $(m,m)$ diagonal Padé
approximant and obtain an implicit one-step scheme of order $2m$ for any $m$. The
contribution is the implementation: the Padé denominator is factored into its $m$
roots, each real root costs one real and each complex-conjugate pair one complex
sparse system of the original size, every such system has the Newmark-like matrix
$r^2M+rhC+h^2K$, and neither the state matrix nor $M^{-1}$ is ever formed (§2.2–2.4).
For $m=1$ the scheme is the constant-average-acceleration
[Newmark method](/methods/newmark-method.md) (§2.4.1).

**Page-local notation.** $x=[h\dot u;\,u]$ is the state vector (velocity block first,
scaled by $h$), $\mathcal A$ the scaled state matrix, $m$ the Padé degree (Song &
Eisenträger's $M$, which clashes with the mass matrix), $\hat N_m$, $\hat D_m$ the
unnormalized Padé numerator and denominator, $r_i$ the roots of $\hat D_m$, $p_{\mathrm f}$
the degree of the load polynomial within a step, $\mathcal B_k$, $\mathcal C_k$ the
load matrices, $\mathcal F_k$ the load coefficients. The source steps from $t_{n-1}$ to
$t_n$; the formulas below are shifted to the registry's $t_n\to t_{n+1}$.

## Exact one-step map

With step-local time $t=t_n+\theta h$, $\theta\in[0,1]$, the equations become
$x'=\mathcal Ax+F$ in $\theta$ with

$$\mathcal A=\begin{bmatrix}-hM^{-1}C&-h^2M^{-1}K\\ I&0\end{bmatrix},\qquad F=\begin{bmatrix}h^2M^{-1}f\\0\end{bmatrix}$$

(Song & Eisenträger 2022, §2.1, Eqs. (7)–(9)). $\mathcal A$ already contains the step:
for $C=0$ its eigenvalues are $\pm\mathrm i\omega h$ with $\omega^2$ the eigenvalues of
$M^{-1}K$, so $\mathcal A$ plays the role of $z=h\lambda$. If the load is expanded in
each step about the midpoint, $F=\sum_{k=0}^{p_{\mathrm f}}\mathcal F_k(\theta-\tfrac12)^k$
(fitted on Gauss–Lobatto–Legendre points in the code, Eq. (17)), variation of
constants gives the exact map

$$x_{n+1}=e^{\mathcal A}x_n+\sum_{k=0}^{p_{\mathrm f}}\mathcal B_k\mathcal F_k,\qquad
\mathcal B_k=\int_0^1(\theta-\tfrac12)^ke^{\mathcal A(1-\theta)}\,d\theta,$$

with the recurrence $\mathcal B_0=\mathcal A^{-1}(e^{\mathcal A}-I)$,
$\mathcal B_k=\mathcal A^{-1}\big(k\mathcal B_{k-1}+(-\tfrac12)^k(e^{\mathcal A}-(-1)^kI)\big)$
(Eqs. (19)–(21)). $\mathcal B_0=\phi_1(\mathcal A)$ in the registry's
[φ-function](/methods/exponential-integrators.md) notation *(compiler check, not in
the source)*. The authors trace this exponential route to the precise integration
method of Zhong and Williams and its successors (§2.1), and give the reason not to use
it directly: with a consistent mass matrix $M^{-1}C$, $M^{-1}K$ and $e^{\mathcal A}$ are
full (§2.1). Polynomial (Taylor) approximations of $e^{\mathcal A}$ give explicit,
conditionally stable schemes; rational ones give implicit, possibly unconditionally
stable schemes (§2.2).

## The Padé scheme

The $(m,m)$ diagonal Padé approximant in the unnormalized form of the source is

$$e^{\mathcal A}\approx\hat D_m(\mathcal A)^{-1}\hat N_m(\mathcal A),\qquad
\hat N_m(z)=\sum_{j=0}^m\frac{(2m-j)!}{j!\,(m-j)!}z^j,\qquad \hat D_m(z)=\hat N_m(-z)$$

(App. B, Eqs. (B.2)–(B.3)); $\hat N_m(0)=(2m)!/m!$, so it differs from the normalized
form on the [stability-function](/definitions/stability-function.md) page by a constant
factor. Multiplying by $\hat D_m$ gives

$$\hat D_m(\mathcal A)\,x_{n+1}=\hat N_m(\mathcal A)\,x_n+\sum_{k=0}^{p_{\mathrm f}}\mathcal C_k\mathcal F_k,\qquad
\mathcal C_k=\hat D_m\mathcal B_k=\mathcal A^{-1}\big(k\,\mathcal C_{k-1}+(-\tfrac12)^k(\hat N_m-(-1)^k\hat D_m)\big),$$

$\mathcal C_0=\mathcal A^{-1}(\hat N_m-\hat D_m)$, all polynomials in $\mathcal A$
(Eqs. (22)–(26)). The scheme has order $2m$ in time; the load degree must be
$p_{\mathrm f}=m$ for that order, except $p_{\mathrm f}=1$ for $m=1$ (§2.2, footnote 7).
Solving for $x_{n+1}+x_n$ ($m$ odd) or $x_{n+1}-x_n$ ($m$ even) cancels the highest
power of $\mathcal A$ on the right-hand side (Eqs. (27)–(31)).

## Factored solve

With $\hat D_m(z)=\prod_{i=1}^m(r_i-z)$ the step is $m$ successive shifted solves
$(r_iI-\mathcal A)\,x^{(i)}=x^{(i-1)}$ (Eqs. (29), (32)–(33)), a factorization the authors
credit to Reusch, Ratzan, Pomphrey and Park for parabolic problems (§2.2).

- **Real root.** Eliminating the second block of $(rI-\mathcal A)\xi=\rho$
  (page-local $\xi=[\xi_1;\xi_2]$, $\rho=[\rho_1;\rho_2]$) gives
  $$(r^2M+rhC+h^2K)\,\xi_1=rM\rho_1-h^2K\rho_2,\qquad \xi_2=(\xi_1+\rho_2)/r,$$
  a sparse symmetric positive definite system "similar to the Newmark scheme", with no
  mass-matrix inverse (§2.3.1, Eqs. (39)–(42)).
- **Complex-conjugate pair.** By partial fractions,
  $(rI-\mathcal A)(\bar rI-\mathcal A)\xi=\rho$ with real $\rho$ is solved by one complex
  solve $(rI-\mathcal A)\upsilon=\rho$ and $\xi=-\operatorname{Im}\upsilon/\operatorname{Im}r$; the
  complex matrix $r^2M+rhC+h^2K$ is symmetric but not Hermitian (§2.3.2, Eqs. (43)–(52)).
  The products $\mathcal A\xi=-\operatorname{Im}(r\upsilon)/\operatorname{Im}r$ and
  $\mathcal A^2\xi=\rho+2\operatorname{Re}(r)\mathcal A\xi-r\bar r\xi$ come free, so the
  right-hand side of the next step needs no extra product (Eqs. (53)–(54), (90)).
- **Cost.** Each increase of the order by two adds one real or one complex system of the
  original size $d$, not $2d$; the system size does not grow with order, unlike the
  continuous-Galerkin schemes of Idesman and of Kim and Reddy, whose systems grow with
  the order (§1, §2.4). For linear problems the factorizations are computed once and
  reused (§2.3.1).

| $m$ | order | $\hat D_m(z)$ | roots $r_i$ | systems per step |
|---|---|---|---|---|
| 1 | 2 | $2-z$ | $2$ | 1 real |
| 2 | 4 | $12-6z+z^2$ | $3\pm\sqrt3\,\mathrm i$ | 1 complex |
| 3 | 6 | $120-60z+12z^2-z^3$ | $4.644370709252171$; $3.677814645373910\pm3.508761919567443\,\mathrm i$ | 1 real, 1 complex |
| 4 | 8 | $1680-840z+180z^2-20z^3+z^4$ | $4.207578794359259\pm5.314836083713504\,\mathrm i$; $5.792421205640749\pm1.734468257869007\,\mathrm i$ | 2 complex |

(Eqs. (55)–(56), (70)–(71), (75)–(76), (81)–(82).) The roots $r_i$ are the eigenvalues
of $A^{-1}$ for the $m$-stage Gauss method, since $\hat D_m(z)$ is proportional to
$\det(I-zA)$ for that method, whose zeros are the reciprocals of the eigenvalues of $A$
*(compiler check, not in the source)*; the factored solve is thus the real/complex
eigenvalue decoupling used for the stage systems of
[fully implicit Runge–Kutta methods](/methods/fully-implicit-runge-kutta.md), applied
here to the linear second-order system without forming $\mathcal A$. See
[solving the stage equations](/methods/implicit-stage-solvers.md).

## Stability and dispersion

The authors state that Padé-based integrators are unconditionally stable "since the
spectral radius of the rational approximation … is of unit value", with no amplitude
decay and no numerical damping, citing Gallopoulos and Saad; they give no
amplification-matrix analysis and defer controllable numerical damping (A- and L-stable
high-order variants with prescribed spectral radius at infinity) to future work
(§3.2.1, §4). The diagonal Padé approximant is A-stable and not L-stable,
$\lvert R(\infty)\rvert=1$, which is the "no numerical damping" property
([A-stability](/properties/a-stability.md); *compiler check, not in the source*). On
linear seminegative problems the scheme's energy behaviour is that of
[unconditional strong stability of diagonal Padé schemes](/results/diagonal-pade-strong-stability.md).
As remedy for unresolved high frequencies the authors suggest a very small
stiffness-proportional Rayleigh damping, from preliminary results not shown (§4).

## Numerical evidence

MATLAB with direct sparse solvers (Song & Eisenträger 2022, §3; Intel i7-8700 for the
rod, Xeon E5-2637 v4 for the 3D case):

- **Single-degree-of-freedom oscillators** (six cases, damped and undamped, free and
  forced, from Kim): convergence rates 2, 4, 6, 8 down to an error plateau of about
  $10^{-9}\,\%$ (§3.1, Table 1, Fig. 2).
- **Long-time accuracy** (undamped free oscillation, 10,000 periods $T$): for 1 %
  amplitude error the eighth-order scheme needs only $h=T/2$, the sixth-order $h<T/3$,
  the fourth-order $h<T/8$, second-order methods $h<T/85$. Period elongation at $h=T/2$
  is about 0 %, 0.5 %, 7.7 % and 56.5 % (orders not labelled, presumably 8, 6, 4, 2),
  against 61.7 % for HHT-α and 30.7 % for the Bathe method (§3.2, Fig. 3).
- **2D rod in plane stress** (66 to 658,434 degrees of freedom): per-step cost relative
  to Newmark 1.09, 2.73, 3.92, 5.51 for $m=1,\dots,4$; for 1 % $L_2$ error the admissible
  step grows by factors 17, 49, 90, giving speed-ups "roughly 6, 12, and 15" (§3.3,
  Figs. 6–8).
- **Lamb's problem** (821,762 degrees of freedom): per-step cost 1, 4.55, 5.53, 9.96;
  step factors 12.14, 31.67, 49.88; speed-ups 2.67, 5.73, 5.01 (§3.4, Figs. 14–15).
- **3D mountain model** (scaled-boundary finite elements, 755,337 degrees of freedom):
  the eighth-order scheme at the Nyquist step $h_{\max}\approx0.09$ s matches a
  central-difference reference; Newmark needs $h_{\max}/50$, at 24.1 times the cost of
  Newmark at $h_{\max}$, against 4.05 times for the eighth-order scheme (§3.5, Fig. 19).
- The $m=1$ scheme and Newmark give identical errors (Figs. 7, 14).

## Qualifications

- **Scope.** Only linear problems with $M$, $C$, $K$ constant within a step are treated;
  there is no nonlinear extension (§2.1).
- **"Padé-based … unit spectral radius".** The statement holds for diagonal approximants
  on the undamped (imaginary) spectrum; with damping the spectral radius is below one,
  and off-diagonal Padé approximants (e.g. the L-stable subdiagonal ones) do not have unit
  modulus at infinity, so the blanket wording is broader than what the paper uses
  *(compiler check, not in the source)*.
- **Relation to Gauss methods.** The paper never mentions that its homogeneous propagator
  $\hat D_m^{-1}\hat N_m$ is the stability function of the $m$-stage Gauss method, so that
  on linear constant-coefficient problems the scheme coincides with Gauss Runge–Kutta in
  the homogeneous part *(compiler remark, not in the source)*. Its novelty is the
  structural-dynamics implementation, not the approximation.
- **Printed figures.** The speed-up "15" for $m=4$ on the rod is low against the
  printed factors ($90/5.51\approx16.3$); the period-elongation values are not assigned
  to orders; the Fig. 18 caption names the $O(1,1)$ scheme and $h=0.0018$ s while the text
  describes the eighth-order scheme at $h_{\max}$; the conclusions write the Padé degree
  as $p$ (arXiv v1).
- **Labels.** The source labels its schemes $O(M,M)$, the Padé type, not a Landau
  symbol; "$O(4,4)$" is the eighth-order scheme.

# Citations

- [Song & Eisenträger (2022)](/sources/song-2022.md) — §1; §2.1 Eqs. (7)–(21); §2.2 Eqs. (22)–(33), footnote 7; §2.3 Eqs. (37)–(54); §2.4 Eqs. (55)–(90); §3.1–3.5 Table 1, Figs. 2–19; §4; App. B Eqs. (B.1)–(B.5).
