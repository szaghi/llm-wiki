---
type: Method
title: "Zhang–Shu positivity-preserving scaling limiter"
description: "A conservative linear rescaling of the high-order polynomial about its cell average, first in density then in pressure, that puts the Gauss–Lobatto point values in the admissible set; with a positive first-order flux and SSP stepping it makes FV, DG and FD WENO schemes positivity-preserving without losing order."
status: established
aliases: [Zhang-Shu limiter, positivity limiter, linear scaling limiter, maximum-principle-satisfying limiter]
tags: [positivity, limiter, weno, dg, finite-difference]
timestamp: 2026-10-08T00:00:00Z
---

# Zhang–Shu positivity-preserving scaling limiter

The limiter enforces the sufficient condition of
[positivity preservation](/properties/positivity-preserving.md):
$\mathcal{P}_i(\hat x^{(a)}_i) \in \mathcal{G}$ at the $N_{\mathrm{GL}}$
Gauss–Lobatto points ($2N_{\mathrm{GL}} - 3 \ge K$), together with
$\nu \le \hat w_1\,\nu_0$ ([Zhang & Shu (2010)](/sources/zhang-2010.md),
Theorem 2.1). It generalizes the maximum-principle-satisfying limiter
of Zhang and Shu for scalar laws to the convex set $\mathcal{G}$.

## Algorithm (one dimension, forward Euler)

Given $\mathcal{P}_i(x) = (\rho_i(x), m_i(x), E_i(x))$ with mean
$\bar u_i \in \mathcal{G}$, set
$\epsilon_{\mathcal{G}} = \min_i\{10^{-13}, \bar\rho_i, p(\bar u_i)\}$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §§2.2–2.3; eqs. 2.4–2.11
checked on the page images).

1. **Density.** Replace $\rho_i(x)$ by
   $\hat\rho_i(x) = \theta_\rho\left(\rho_i(x) - \bar\rho_i\right) + \bar\rho_i$, with
   $$\theta_\rho = \min\left\{\frac{\bar\rho_i - \epsilon_{\mathcal{G}}}{\bar\rho_i - \rho_{\min}},\ 1\right\},\qquad \rho_{\min} = \min_a \rho_i(\hat x^{(a)}_i).$$
2. **Pressure.** Let $\hat{\mathcal{P}}_i = (\hat\rho_i, m_i, E_i)$. For
   each point with $p(\hat{\mathcal{P}}_i(\hat x^{(a)}_i)) < \epsilon_{\mathcal{G}}$
   solve the quadratic equation
   $p\left((1 - t_a)\,\bar u_i + t_a\,\hat{\mathcal{P}}_i(\hat x^{(a)}_i)\right) = \epsilon_{\mathcal{G}}$
   for $t_a \in [0,1]$ (otherwise $t_a = 1$), and set
   $\theta_p = \min_a t_a$ and
   $\tilde{\mathcal{P}}_i(x) = \theta_p\left(\hat{\mathcal{P}}_i(x) - \bar u_i\right) + \bar u_i$.

**Properties.** The mean is unchanged (conservation); every
$\tilde{\mathcal{P}}_i(\hat x^{(a)}_i)$ lies in the convex set
$\{\rho \ge \epsilon_{\mathcal{G}},\ p \ge \epsilon_{\mathcal{G}}\} \subset \mathcal{G}$
(Lemma 2.5); and for smooth solutions bounded away from vacuum
$1 - \theta_p = O(h^{K+1})$, so the limiter is accurate. Under SSP time
stepping the limiter acts at every stage. Theorem 2.1 extends to
rectangular meshes by tensor quadratures — Gauss points along edges
times Gauss–Lobatto points across them — with
$\nu = \Delta t(\alpha_1/h_x + \alpha_2/h_y)$
([Zhang & Shu (2010)](/sources/zhang-2010.md), §3).

**CFL bound.** With the Lax–Friedrichs flux and $\nu_0 = 1$ the bound is
$\hat w_1$: $1/6$ for $K = 2, 3$ and $1/12$ for $K = 4, 5$
([Zhang & Shu (2010)](/sources/zhang-2010.md), Table 2.1), only slightly
below the linear-stability limits of DG. For fifth-order WENO
$\hat w_1 = 1/12$, for seventh order $1/20$
([Zhang & Shu (2012)](/sources/zhang-2012.md), Remark 3.3). The bound is
sufficient, not necessary; in practice it is enforced only when a trial
step produces a negative density or pressure. With Runge–Kutta the
stage wave speeds are unknown in advance, and a safety factor of 2–3 on
$\Vert(\vert u\vert + c)\Vert_\infty$ worked in all tests; multistep SSP
avoids the issue ([Zhang & Shu (2010)](/sources/zhang-2010.md), Remark 2.7).

## Variants

* **DG** ([Zhang & Shu (2010)](/sources/zhang-2010.md), §4): third-order
  RKDG with the TVB limiter applied first; the positivity limiter lets
  the TVB constant $M$ be raised far above values that otherwise blow up
  (Leblanc: $M_1 = M_3 = 10^{10}$–$10^{20}$). The TVB limiter is still
  needed for shocks.
* **FV WENO.** WENO yields only point values, so a polynomial must be
  built from the point values and the mean; for fifth order the
  degree-four $\mathcal{P}_i$ interpolates $u^\pm_{i\mp1/2}$ and the
  means of $I_{i-1}, I_i, I_{i+1}$
  ([Zhang & Shu (2012)](/sources/zhang-2012.md), §2.1). In practice only the
  combination $\bar u_i - \hat w_1 u^+_{i-1/2} - \hat w_{N} u^-_{i+1/2}$
  is needed ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4).
* **FD WENO** ([Zhang & Shu (2012)](/sources/zhang-2012.md), §3). With the
  global Lax–Friedrichs splitting $f^\pm = \frac12(f \pm \alpha u)$ the
  FD scheme is a sum of two FV WENO schemes for the reconstruction
  pairs of the states $\pm f^\pm/\alpha = \frac12\left(u \pm f(u)/\alpha\right)$.
  These states lie in $\mathcal{G}$ whenever $u$ does (the Lax–Friedrichs
  argument above), so the limiter is applied to their reconstructed
  interface values. The CFL condition is
  $\alpha\Delta t/h \le \hat w_1$, halved for local Lax–Friedrichs
  (§4.1). For a scalar maximum principle the same device fails:
  $\mathcal{H}$ has larger extrema than $u$, so bounding it destroys
  accuracy — but positivity of a solution bounded away from zero is
  safe (§2.2).
* **Compact FV WENO** ([Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4):
  the same limiter on the globally coupled
  [compact-reconstruction WENO](/methods/compact-reconstruction-weno.md)
  values, with the HLLC flux of Batten et al. and the CFL bound
  $\hat w_1$; the polynomial is still local, so the accuracy argument
  carries over (Remark 2).
* Source terms and general equations of state: split the update as
  $\frac12(F + S)$, with $S = u + 2\Delta t\,s(u)$ positive under its own
  step limit for geometric, gravity, reaction and radiative-cooling
  sources ([Zhang & Shu (2012)](/sources/zhang-2012.md), §§4.2–4.3).

* **MHD, point values only, divergence-free traces**
  ([Ding & Wu (2024)](/sources/ding-2024.md), §2.4; arXiv v1). No
  polynomial is built. In 2D the interior Gauss–Lobatto values are
  replaced by one remainder state: the cell average minus the
  $\hat w_1$-weighted edge averages of the traces, divided by
  $1 - 2\hat w_1$, which must also lie in $\mathcal G$. The second step
  scales the whole state about $\bar u_i$ by a ratio, using the concavity
  of the internal energy $\rho e(u)$ and Jensen's inequality, with no
  quadratic solve. Because the scaling is affine about the cell mean, it
  keeps the discrete divergence of the traces zero (Thm. 2.9). Floors are
  cell-wise, $\min\{10^{-13}, \bar\rho_i\}$ and
  $\min\{10^{-13}, \rho e(\bar u_i)\}$. The theory allows a Courant number
  of $\hat w_1 = 1/12$ at fifth order, but the runs use 0.3, with the CFL
  definition not given ([positivity preservation](/properties/positivity-preserving.md)).

**Alternatives.** The [flux limiter](/methods/positivity-preserving-flux-limiter.md)
of Hu, Adams and Shu limits fluxes instead of point values and needs a
weaker time-step condition for accuracy.

# Citations

1. [Zhang & Shu (2010)](/sources/zhang-2010.md), §§1–4 (Theorem 2.1, Lemma 2.5, Table 2.1; eqs. 2.1–2.12 read from the page images).
2. [Zhang & Shu (2012)](/sources/zhang-2012.md), §§2–5 (Theorem 3.1, eqs. 3.7–3.11 and Remark 3.3 read from the page images).
3. [Guo, Xiong & Shi (2014)](/sources/guo-2014.md), §2.4.
4. [Hu, Adams & Shu (2013)](/sources/hu-2013.md), §2.4.
5. [Ding & Wu (2024)](/sources/ding-2024.md), §§2.4, 3 (arXiv v1).
