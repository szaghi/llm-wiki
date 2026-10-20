---
type: Method
title: "Superviscosity-stabilized explicit Runge–Kutta methods"
description: "Sun and Shu enforce strong stability of an explicit Runge–Kutta method on linear seminegative problems by adding diffusive and dispersive superviscosity of order $h^{2\\zeta-1}$ to the operator or as a post-step filter, with sharp critical coefficients and no loss of linear order, plus an adaptive filter for nonlinear problems."
status: established
aliases: [superviscosity filtering, hyperviscosity stabilization, modified method, filtering method, adaptive filtering method, anti-superviscosity]
tags: [stability, runge-kutta, explicit, structure-preserving]
timestamp: 2026-10-20T16:00:00Z
---

# Superviscosity-stabilized explicit Runge–Kutta methods

Many explicit Runge–Kutta methods are not [strongly stable](/properties/strong-stability.md)
on $y'=Ly$ with $L$ seminegative and non-normal: the $p$-stage, order-$p$ methods fail
for $p\equiv1,2\pmod4$, and RK4 fails on a $3\times3$ non-normal test
([Sun & Shu 2021](/sources/sun-2021.md), §1, §6.1.1). Sun & Shu borrow
*superviscosity* (hyperviscosity) from spectral methods, a high-order term that
penalizes high-frequency modes, and couple it to the time integrator so that the
fully discrete scheme satisfies $\lVert y_{n+1}\rVert\le\lVert y_n\rVert$ while keeping
the linear order $p$. The correction is tuned by the
[energy method](/methods/runge-kutta-energy-method.md): its order is set by the leading
index $\zeta$ (Sun & Shu's $k^*$) of the energy expansion, and its critical size by the
leading coefficient $\eta_\zeta$ and the leading block of the quadratic-form matrix
$\Upsilon$ (page-local symbols as on the energy-method page).

## The two variants

Let $Z:=hL$ and $L^\top$ be the adjoint of $L$ (page-local). Two coefficients are
introduced (page-local): $\mu_1$, the **dispersive** superviscosity, and $\mu_2$, the
**diffusive** one, with the convention that $\mu_2<0$ dissipates and $\mu_2>0$ is
anti-diffusive ("anti-superviscosity").

**Modified method.** Apply the unchanged method to $y'=\tilde Ly$ with

$$\tilde L=L+\mu_1h^{2\zeta-2}(L^\top)^{\zeta-1}L^{\zeta}+\mu_2h^{2\zeta-1}(L^\top)^{\zeta}L^{\zeta}$$

(Sun & Shu 2021, §3.1, Eqs. (3.1)–(3.3)). Then
$\langle\tilde Lv,v\rangle\le-\frac{\mu_1}{2}h^{2\zeta-2}\lvert L^{\zeta-1}v\rvert_L^2+\mu_2h^{2\zeta-1}\lVert L^\zeta v\rVert^2$,
with $\lvert\cdot\rvert_L$ the dissipation semi-norm of
[strong stability](/properties/strong-stability.md) *(compiler check, not in the sources: Sun & Shu state
the inequality for the $Z$-scaled quantities, i.e. multiplied by $h$)*, so for $\mu_1>0$, $\mu_2<0$ the modified operator is "weakly coercive"
(Remark 3.1, Eq. (3.4)).

**Filtering method.** Post-process the update $y_+=R(Z)y_n$ by

$$y_F=\bigl(I+\mu_1(Z^\top)^{\zeta-1}Z^{\zeta}+\mu_2(Z^\top)^{\zeta}Z^{\zeta}\bigr)y_+$$

(Sun & Shu 2021, §3.1, Eq. (3.5)). It is a splitting approximation of the modified
method: the Runge–Kutta step for $y'=Ly$ followed by one forward Euler step for
$y'=(\tilde L-L)y$ (Remark 3.2); the two differ by a high-order term and the filter
"seems to be more efficient" in practice.

For fixed $L$ the added term $\tilde Z-Z$ has norm
$O\bigl(h^{2\zeta-1}(\lvert\mu_1\rvert+\lvert\mu_2\rvert h)\bigr)$, hence perturbs the truncation error only at $O(h^{p+1})$ when
$\zeta=\lceil(p+1)/2\rceil$ (Eq. (3.10)).

## Stability and sharpness

**Theorem (Sun & Shu 2021, Thm. 3.1).** For a method of linear order $p$ with
$\zeta=\lceil(p+1)/2\rceil$, both the modified and the filtering method are linearly
of order $p$ and strongly stable for $h\lVert L\rVert$ small enough, provided

$$\mu_2<\mu_2^0:=-\frac{\eta_\zeta}{2}\quad\text{and}\quad\begin{cases}\mu_1=0, & p\text{ odd},\\ \mu_1>\mu_1^0, & p\text{ even},\end{cases}$$

where $\mu_1^0$ is the threshold that makes the leading block of $\Upsilon$ minus
$\mathrm{diag}(0,\dots,0,\mu_1^0)$ negative semidefinite. The proof combines the
small-step energy estimate of the base method with two-sided bounds on
$\lVert y_\#\rVert^2-\lVert y_+\rVert^2$, $\#\in\{F,M\}$ (Lemma 3.1, Eqs.
(3.6)–(3.7), proved in §4).

**Theorem (Sun & Shu 2021, Thm. 3.2).** If $\mu_2>\mu_2^0$ neither method is strongly
stable; the proof uses an energy-conserving $L$ ($\langle Lv,v\rangle=0$), for which
the semi-norm terms vanish. The diffusive threshold is therefore sharp "up to an equal
sign". Sharpness of $\mu_1^0$ is checked only numerically (Remark 3.3, §6.1.1).

No explicit step bound is given: the theorems hold for $h\lVert L\rVert\le c_0$ with
an unspecified $c_0\ll1$.

## Critical values

For the $p$-stage, order-$p$ linear methods $R(z)=\sum_{j=0}^pz^j/j!$ (Sun & Shu 2021,
§6, Table 6.1):

| $p$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $\mu_1^0$ | — | $-\frac14$ | — | $\frac1{144}$ | — | $-\frac1{4800}$ |
| $\mu_2^0$ | $-\frac12$ | $-\frac18$ | $\frac1{24}$ | $\frac1{144}$ | $-\frac1{720}$ | $-\frac1{5760}$ |

Reading the table: $p=1,2,5,6$ need genuine diffusive superviscosity ($\mu_2^0<0$).
For $p=3$, $\mu_2^0=\frac1{24}>0$: RK3 is already strongly stable and even tolerates
anti-superviscosity up to $\frac1{24}$. For $p=4$, $\mu_1^0=\frac1{144}>0$, so a
dispersive term is **necessary**: with $\mu_1=0$, even $\mu_2=-100$ does not give
$\lVert R_4(Z)\rVert\le1$ for small $h$ on the non-normal test (§6.1.1, Table 6.3).
With $\mu_1,\mu_2$ 1% beyond the critical values, $\lVert R_p(Z)\rVert\le1$ for small
$h$ on both the $3\times3$ test and an upwind DG advection operator (Tables 6.3, 6.5).

## Adaptive filter for nonlinear problems

For a nonlinear semi-discretization $y'=f(y)$ with $\langle f(v),v\rangle\le0$, the
filter becomes

$$y_F=(I+\mu_2D^\top D)\,y_+,\qquad \mu_2=\min\Bigl\{\frac{\lVert y_n\rVert^2-\lVert y_+\rVert^2}{\lVert Dy_+\rVert^2},\,0\Bigr\},$$

for a chosen operator $D$ (page-local), e.g. $D=Z^\zeta$, or a conservative
approximation of $h^\zeta\partial_x^\zeta$ for conservation laws, or $D=I$ when mass
conservation is not needed (Sun & Shu 2021, §5, Eq. (5.1)). It is modelled on
relaxation Runge–Kutta. **Proposition 5.1:** if $\lvert\mu_2\rvert\lVert D\rVert^2\le1$
then $\lVert y_F\rVert\le\lVert y_n\rVert$. Accuracy is unaffected when
$\lVert D^\top Dy_+\rVert/\lVert Dy_+\rVert^2=O(1)$ (Remark 5.1); for linear problems
with $D=Z^\zeta$ the coefficient is $O(1)$ for odd $p$ but $O(h^{-1})$ for even $p$,
which can force the step condition $h\lVert L\rVert=O(h^{1/(2\zeta)})$, stricter than
the usual CFL condition (Remark 5.2).

## Numerical evidence

All from Sun & Shu (2021, §6):

- **Order.** With $\mu_2=O(1)$ the stabilized methods keep order $p$ for $p=1,\dots,4$
  on the $3\times3$ test; with $\mu_1=O(1)$ odd-order methods lose order (RK3 with
  $(\mu_1,\mu_2)=(1,0)$ gives order 2.00), confirming $\mu_1=0$ for odd $p$ (§6.1.2,
  Table 6.4). Upwind DG $P^{p-1}$ with stabilized RK$p$, $p=1,\dots,5$, reaches the
  design order, modified and filtering errors nearly identical (Table 6.6).
- **Long time.** With $P^p$ upwind DG and $p=1,2,5$ the original methods let the $L^2$
  norm grow at $h=0.05\Delta x$; with superviscosity it decays (Fig. 6.1).
  Anti-superviscosity $(\mu_1,\mu_2)=(0,\frac1{24})$ with RK3 reduces the
  over-damping of $\sin(5x)$ up to $T=1000$ (Figs. 6.2–6.3), though the amplitude still
  decays for larger $T$.
- **Discontinuities.** Superviscosity of size $O(h^4)$ only mildly reduces over- and
  undershoots; dispersive superviscosity pushes oscillations to one side; a strong
  $\mu_2=-2$ smooths central-flux oscillations (§6.2.4).
- **Burgers.** With an entropy-conservative DG flux, the adaptive filter turns the
  growing $L^2$ norm of the original RK2 and Fehlberg six-stage fifth-order methods
  into a decreasing one, at orders 2 and 5 (Table 6.7, Fig. 6.8); it does not suppress
  post-shock oscillations, which need a strong fixed $\mu_2$ (Figs. 6.9–6.10).

## Qualifications

- The analysis of the modified and filtering methods is linear and autonomous; for
  nonlinear problems only the adaptive filter with Prop. 5.1 is proved.
- The adaptive filter's possible extra step restriction for even $p$ is a cost that
  relaxation Runge–Kutta does not have (Sun & Shu 2021, Remark 5.2, as read).
- Printed slips in the version read (arXiv v1): the closed forms for $\eta_\zeta$ in
  Prop. 2.2(3) are inconsistent with Table 6.1 (details on
  [strong stability](/properties/strong-stability.md)); Table 6.3 prints positive
  entries for the unstabilized RK3 at some steps although the text calls it strongly
  stable; Eq. (4.32) drops a factor; the discontinuous initial datum is
  $\mathbf 1_{[\pi/2,3\pi/2]}$ in the text and $\mathbf 1_{[-\pi/2,3\pi/2]}$ in the
  figure captions.

# Citations

- [Sun & Shu (2021)](/sources/sun-2021.md) — §1, §2 (Def. 2.1, Props. 2.1–2.2), §3.1 (Eqs. 3.1–3.5, Remarks 3.1–3.2), §3.2 (Lemma 3.1, Thms. 3.1–3.2, Eq. 3.10, Remark 3.3), §4, §5 (Eq. 5.1, Prop. 5.1, Remarks 5.1–5.2), §6 (Tables 6.1, 6.3–6.7, Figs. 6.1–6.10).
