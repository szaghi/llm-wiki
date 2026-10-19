---
type: Method
title: "Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping"
description: "Stabilized explicit Runge–Kutta methods fix a low order and use many stages whose stability polynomial, built from shifted Chebyshev or Legendre polynomials and realized by a three-term recurrence, has a real stability interval growing like s squared; the page covers RKC, RKL super-time-stepping, monotonic RKC, disk polynomials and their limits."
status: established
aliases: [explicit stabilized Runge–Kutta, ESRK, Runge–Kutta–Chebyshev, RKC, RKC1, RKC2, Runge–Kutta–Legendre, RKL, RKL1, RKL2, super-time-stepping, STS, monotonic RKC, MONO, Chebyshev methods]
tags: [runge-kutta, explicit, stabilized, stability, stiff, positivity]
timestamp: 2026-10-19T20:00:00Z
---

# Stabilized explicit Runge–Kutta methods: Chebyshev, Legendre and super-time-stepping

A **stabilized explicit Runge–Kutta method** fixes a low order $p$ (one or two,
sometimes four) and uses $s\gg p$ stages, spending the extra stages on the length of
the real stability interval rather than on accuracy. Its stability polynomial is a
shifted and scaled orthogonal polynomial, so the interval $[-\ell_s,0]$ on which
$\lvert P\rvert\le1$ grows like $s^2$ (page-local: $\ell_s$ the real stability
boundary). For a mildly stiff problem whose Jacobian eigenvalues lie near the
negative real axis (diffusion and parabolic semi-discretizations), the stage count is
chosen per step so that $h\rho\le\ell_s$, with $\rho$ the spectral radius of $J$
(page-local), and the number of right-hand-side evaluations per step grows like
$\sqrt{h\rho}$ instead of $h\rho$
([Croci & Rosilho de Souza 2022](/sources/croci-2022.md), §1, §2.2;
[Dawes 2021](/sources/dawes-2021.md), §1, §3). The stages are evaluated through the
three-term recurrence of the orthogonal family, which keeps the method stable stage
by stage ([internal stability](/definitions/internal-stability.md)) and needs only a
few registers.

## Optimal real-axis and disk polynomials

The shifted Chebyshev polynomial $T_s(1+z/s^2)$ (page-local: $T_j$ the Chebyshev
polynomial of the first kind, not the tree set of the registry) is the optimal
first-order polynomial for the negative real axis, stable on $[-2s^2,0]$, as recalled
by [Doehring et al. (2024)](/sources/doehring-2024.md) (App. A, Eqs. (A.1)–(A.2)).
For spectra filling a disk the optimal polynomials are known in closed form, as
recalled by Doehring et al. (§3.1, Eqs. (3.2)–(3.3), (3.11)): the first-order
$(1+z/s)^s$ contains the disk $\lvert z+s\rvert\le s$, and the second-order

$$P(z)=\frac{s-1}s\Bigl(1+\frac z{s-1}\Bigr)^s+\frac1s$$

contains the disk of radius $s-1$; the latter equals second-order RKC with infinite
damping and is a composition of forward Euler steps, hence SSP with optimal
coefficient (§3.1.2). These limits frame the family: real-axis inclusion grows like
$s^2$, disk inclusion like $s$, and one-sided imaginary-axis inclusion of a real
polynomial is bounded by $s-1$ (Doehring et al. 2024, §4.3). Stabilized methods
therefore pay off for parabolic spectra; for hyperbolic spectra the stable step of an
optimized polynomial grows only linearly in $s$, the regime of
[optimal stability polynomials](/methods/optimal-stability-polynomial.md) and
[paired explicit Runge–Kutta methods](/methods/paired-explicit-runge-kutta.md).

## Runge–Kutta–Chebyshev (RKC)

As recalled by Croci & Rosilho de Souza (2022, §2.2, Eqs. (5)–(12), from Sommeijer,
van der Houwen and Verwer), RKC is written in delta form with increments $d_j$
(stage value $y_n+d_j$):

$$\begin{aligned}
d_0&=0,\qquad d_1=\mu_1hf(y_n),\\
d_j&=\nu_jd_{j-1}+\kappa_jd_{j-2}+\mu_jhf(y_n+d_{j-1})+\gamma'_jhf(y_n),\qquad j=2,\dots,s,\\
y_{n+1}&=y_n+d_s,
\end{aligned}$$

(page-local recurrence coefficients $\mu_j,\nu_j,\kappa_j,\gamma'_j$; the delta form
is chosen because it accumulates smaller rounding errors). The coefficients come from
$\omega_0=1+\varepsilon_{\mathrm d}/s^2$ with a damping parameter $\varepsilon_{\mathrm d}$, and from
$\omega_1$ and $\mathsf b_j$ set by Chebyshev values at $\omega_0$ (page-local $\omega_0$,
$\omega_1$, $\varepsilon_{\mathrm d}$, $\mathsf a_j$, $\mathsf b_j$):
$\omega_1=T_s(\omega_0)/T_s'(\omega_0)$, $\mathsf b_j=1/T_j(\omega_0)$ for first-order
RKC1, and $\omega_1=T_s'(\omega_0)/T_s''(\omega_0)$,
$\mathsf b_j=T_j''(\omega_0)/T_j'(\omega_0)^2$ for second-order RKC2. The stability
polynomial is

$$P(z)=\mathsf a_s+\mathsf b_sT_s(\omega_0+\omega_1z),\qquad \mathsf a_j=1-\mathsf b_jT_j(\omega_0),$$

with real stability boundary $\ell_s=2\omega_0/\omega_1$ and bounds
$\ell_s\ge(2-\frac43\varepsilon_{\mathrm d})s^2$ (RKC1) and
$\ell_s\ge\frac23(1-\frac2{15}\varepsilon_{\mathrm d})(s^2-1)$ (RKC2). Typical damping is
$\varepsilon_{\mathrm d}=0.05$ (RKC1) and $\varepsilon_{\mathrm d}=2/13$ (RKC2); damping pulls $\lvert P\rvert$ below 1 away from the
real axis at a small cost in interval length. The spectral radius is estimated by a
nonlinear power method, and the stage polynomials
$P_j(z)=\mathsf a_j+\mathsf b_jT_j(\omega_0+\omega_1z)$ are the internal stability
polynomials (Lemma 3.1). ROCK2, ROCK4 and the stochastic SK-ROCK belong to the same
recurrence-based class (Remarks 3.4–3.6).

**Multirate RKC.** For $f=f^{\{\mathrm f\}}+f^{\{\mathrm s\}}$ with a cheap stiff part,
the multirate RKC of Abdulle, Grote & Rosilho de Souza, as recalled by Croci & Rosilho
de Souza (2022, §4.1, Eqs. (87)–(97)), applies RKC1 to a modified equation
$y'=f_\eta(y)$ whose averaged force $f_\eta$ is evaluated by an inner $m$-stage RKC1
run of length $\eta$ on $u'=f^{\{\mathrm f\}}(u)+f^{\{\mathrm s\}}(y)$; for linear
$f^{\{\mathrm f\}}=A^{\{\mathrm f\}}y$ (page-local) it equals
$\phi_1(\eta A^{\{\mathrm f\}})f(y)$. The outer stage count is then set by the slow
spectral radius only. See [multirate GARK](/methods/multirate-gark.md) for the
coupled-tableau approach.

## Runge–Kutta–Legendre super-time-stepping (RKL)

The RKL methods of Meyer, Balsara & Aslam, as recalled by Dawes (2021, §3, Eqs.
(7)–(11)), take $P(z)=\mathsf a_s+\mathsf b_s\mathcal P_s(1+w_1z)$ with
$\mathcal P_j$ the Legendre polynomial (page-local) and no damping. Each
multiplication by $X=I+w_1hL$ (page-local) is one forward Euler step of size
$h_{\mathrm e}=w_1h$, the largest step forward Euler can take (page-local
$h_{\mathrm e}$). The super-step is

$$h=\frac{s(s+1)}2h_{\mathrm e}\ \ (\text{RKL1: }w_1=\tfrac2{s(s+1)},\ \mathsf b_j=1),\qquad h=\frac{(s-1)(s+2)}4h_{\mathrm e}\ \ (\text{RKL2: }w_1=\tfrac4{(s-1)(s+2)}),$$

with $\mathsf b_j=\frac{(j-1)(j+2)}{2j(j+1)}$, $\mathsf a_j=1-\mathsf b_j$ and
$c_j=\frac{(j-1)(j+2)}{(s-1)(s+2)}$ for RKL2 (Eqs. (9)–(10)). Unlike RKC, RKL needs no
artificial damping to be stable (§1, §3).

**Forward Euler plus extrapolation.** Dawes (2021, §4–5, Eq. (12), App. A) shows that
the Legendre recurrence
$\mathcal P_j(X)=\frac{2j-1}jX\mathcal P_{j-1}(X)-\frac{j-1}j\mathcal P_{j-2}(X)$
is a linear extrapolation in time: $\mathcal P_j(X)y_n$ approximates the
solution at $t_n+\frac{j(j+1)}2h_{\mathrm e}$, obtained by extrapolating linearly
between $\mathcal P_{j-2}(X)y_n$ and one forward Euler step from
$\mathcal P_{j-1}(X)y_n$, with weight $\frac{2j-1}j$. For RKL2 the stage values
$\mathsf a_jy_n+\mathsf b_j\mathcal P_j(X)y_n$ are in addition linear
interpolations back to $t_n+c_jh$. For linear problems this gives a simplified
algorithm: run the pure recurrence and form $y_{n+1}=\mathsf a_sy_n+\mathsf b_s\mathcal P_s(X)y_n$
at the end, computing intermediate stage values only when the operator must be
updated. Dawes states that the same reading applies to RKC (§5, §9) without showing
it.

**Monotonicity and boundaries.** Each step is $y_{n+1}=P(hL)y_n$, and the entries of
the matrix $P(hL)$ decide monotonicity and positivity. With Neumann or periodic
boundaries all entries are nonnegative under the forward Euler condition, but with
Dirichlet boundaries every RKL scheme except one-stage RKL1 and two-stage RKL2 has
negative entries in up to $s-1$ cells next to the boundary, and the safe Fourier
number falls quickly with $s$ (Dawes 2021, §6–7). Details are on
[positivity preservation](/properties/positivity-preservation.md).

**Under-resolved data.** On a compact heat pulse a single many-stage RKL step
inverts the peak and truncates the base: one RKL1 step spreads data only $s$ cells
left and right, while forward Euler over the same time spreads it
$\frac{s(s+1)}2$ cells, and "the extrapolation cannot fill in for the missing data"
(§8.3). A 10-stage RKL1 step with one cycle inverts the peak of a pulse 20 cells wide,
whereas 19 two-stage cycles reproduce it with fewer operator applications than
forward Euler (55); a 30-stage RKL2 run with 28 cycles matches the analytic solution
with over 15 times fewer operator applications than the two-stage method (§8.3,
Figs. 32–41). On smooth data many-stage steps are accurate and far cheaper than
forward Euler (300-stage RKL1: 300 operator applications against 45150; §8.1). The
recommendation is empirical: fewer stages with more cycles, and a sensitivity study
on the stage count (§8.3, §9).

## Monotonic RKC

[Faleichik & Moisa (2026)](/sources/faleichik-2026.md) (§1–2, Eqs. (2)–(20)) require,
besides $P(0)=P'(0)=P''(0)=1$, that the stability polynomial be **positive and
nondecreasing** on the longest negative interval, $P'(z)\ge0$ and $P(z)>0$ for real
$z\in(-\varrho_s,0]$ (page-local: $\varrho_s$ the length of the monotonicity
interval), because the exponential has these properties (after Bobkov's "spectral
consistency"). Minimal deviation of $P'$ from zero leads to

$$P'(z)=\mathsf b_{s-1}\bigl(1+T_{s-1}(w_0+w_1z)\bigr),\qquad P(z)=\mathsf b_{s-1}\int_{-\varrho_s}^z\bigl(1+T_{s-1}(w_0+w_1\xi)\bigr)\,d\xi,$$

with $\mathsf b_j=1/(1+T_j(w_0))$ (this family's own constants), $\varrho_s=(1+w_0)/w_1$,
the shift $w_0$ and scale $w_1$ (page-local) of the Chebyshev argument, $w_1$ fixed by
$P''(0)=1$ and $w_0$ the root of a scalar equation solved to 500 digits; $P$ is a
combination of $T_s$, $T_{s-2}$ and a linear term. The scheme (Eq. (17)) is a
three-term recurrence close to RKC2 whose stage polynomials satisfy
$0\le\tilde P_j(z)<1$ on $[-\varrho_s,0)$ (page-local $\tilde P_j$; unlike RKC, the final
$P$ is not the last stage polynomial), so internal stability holds by construction, and
the stage $Y_{s-1}$, with $\tilde P_{s-1}=P'$, is a first-order approximation at $t_n+h$.
The trade-off (§3, Table 1, Figs. 2–3):

- the monotonicity interval grows like $\varrho_s\approx0.31(s+0.83)^{1.87}$ (fitted;
  e.g. $\varrho_{10}=29.27$, $\varrho_{100}=1855.5$, $\varrho_{1000}=131320.6$), against
  about $0.65s^2$ for the RKC stability interval, roughly five times shorter at
  $s=1000$; the stability interval is only slightly longer than $\varrho_s$;
- the stability regions are more convex (at $s=9$ to about $-29$, against about
  $-53$ for RKC);
- the error constant $(1-P'''(0))/6$ is about six times smaller than RKC's for large
  $s$.

In the solver MONO, with RKC's step-size selection, a fitted stage-number formula and
a Taylor-based local error estimate (§4), the method takes larger steps than RKC for
the same accuracy but more stages per step. On four stiff test problems at
tolerances $10^{-3}$, $10^{-5}$, $10^{-7}$ it is comparable overall with RKC and the
two-step TSRKC2 and matches requested and achieved accuracy better on a combustion
problem (at $10^{-5}$: error $1.81\times10^{-2}$ against $1.20$ for RKC) (§5, Table 2).
RKC still uses fewer function evaluations and less time on three of the four problems
at every tolerance.

## Many-stage methods for hyperbolic spectra

Doehring et al. (2024, §9, Eqs. (9.1)–(9.8)) realize polynomials of degree up to 128
optimized for DG spectra of hyperbolic problems as products of forward Euler steps
(real roots of $(P-1)/z$) and two-stage low-storage submethods (conjugate pairs) in
modified Shu–Osher form. These methods reach design order on linear problems, but
their SSP coefficient is zero, and on nonlinear problems the usable step drops to
28–79% of the linear limit, which the authors attribute to the missing SSP property
rather than to round-off (§9.4, §10.2). Grouping the near-imaginary roots with the
roots of largest real part, a generalization of Lebedev's ordering idea, reduces the
internal amplification by thirteen orders of magnitude (§9.3, Table 2); see
[internal stability](/definitions/internal-stability.md). The polynomial construction is
on [optimal stability polynomials](/methods/optimal-stability-polynomial.md).

## Reduced precision

Because most stages of a stabilized method buy stability, not accuracy, Croci &
Rosilho de Souza (2022) run them in low precision while keeping one or two
evaluations per step in high precision; see
[mixed-precision Runge–Kutta methods](/methods/mixed-precision-runge-kutta.md).

## Qualifications

- **Order from the linear conditions.** Faleichik & Moisa (2026, §1) state that
  $P(0)=P'(0)=P''(0)=1$ suffices for order two of the scheme; Doehring et al. (2024,
  §4.4, §9) state that linear order two implies order two for Runge–Kutta methods.
  Both hold for any Runge–Kutta method with $c=A\mathbf 1$, because the only
  order-two conditions, $b^\top\mathbf 1=1$ and $b^\top c=\frac12$, then coincide with the
  linear ones $\theta_1=1$, $\theta_2=b^\top A\mathbf 1=\frac12$ *(compiler check, not in the
  sources)*; neither paper states the row-sum hypothesis, and order reduction from
  time-dependent boundary data is outside both arguments.
- **Nonlinear problems and the recurrence.** Dawes (2021, §4) says the RKL recurrence
  "is not satisfied" for nonlinear systems because it assumes a fixed operator. The
  standard nonlinear RKL and RKC methods apply the recurrence to stage values with
  $f$ re-evaluated at each stage and are legitimate Runge–Kutta methods; the remark
  concerns the matrix-polynomial identity only. Dawes's results are for 1D
  constant-coefficient diffusion.
- **Printed slips.** Faleichik & Moisa (2026) print the integrand of $P$ as
  $T_{s-1}(\xi)$ (Eq. (8)) where $T_{s-1}(w_0+w_1\xi)$ is meant, and their error
  estimate (Eq. (23)) lacks the factor $h$ on $f$; with $h$ restored it estimates
  $\frac1{20}h^2y''$, not the $\frac1{10}h^2y''$ of Eq. (22) (reader's expansion).
  Croci & Rosilho de Souza (2022) print the inner RKC coefficient as
  $T_m(\upsilon_0)/T_m'(\upsilon_1)$ (Eq. (96)), where the argument of $T_m'$ is
  $\upsilon_0$. Doehring et al. (2024) label the outer roots of App. A in swapped
  order. Dawes's slips are listed on [positivity preservation](/properties/positivity-preservation.md).
- The sources write $\Delta t$ or $\Delta\tau$ for the step, $\varepsilon$ for the
  damping (here $\varepsilon_{\mathrm d}$, since $\varepsilon$ is the registry stiffness
  parameter), $\ell_s^\varepsilon$ or $\beta^p(s,\varepsilon)$ for the real stability
  bound, $E_s$ and $\mathbb X$ for Dawes's stability polynomial and its argument (here
  $P$ and $X$), $R_s$, $R_k$ for the RKC polynomials (here $P$, $P_j$), and $x$, $R_s$,
  $\tilde R_j$, $\rho_s$ in Faleichik & Moisa (here $z$, $P$, $\tilde P_j$, $\varrho_s$).

# Citations

- [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) — §1, §2.2 (Eqs. 5–12), Lemma 3.1, Remarks 3.4–3.6, §4.1 (Eqs. 87–97).
- [Dawes (2021)](/sources/dawes-2021.md) — §1, §3 (Eqs. 7–11), §4–5 (Eq. 12, simplified algorithm), §6–7, §8.1–8.3 (Figs. 26–44), §9, App. A.
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §1–2 (Eqs. 2–20), §3 (Table 1, Figs. 1–3), §4 (Eqs. 21–23), §5 (Table 2).
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §3.1 (Eqs. 3.2–3.11), §4.3–4.4, §9 (Eqs. 9.1–9.14, Table 2), §10.2, App. A.
