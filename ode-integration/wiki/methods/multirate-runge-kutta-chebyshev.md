---
type: Method
title: "Multirate Runge–Kutta–Chebyshev (mRKC) methods and the averaged-force modified equation"
description: "The multirate Runge–Kutta–Chebyshev method applies an outer RKC scheme, whose stage count depends only on the slow spectral radius, to a modified equation whose averaged force comes from a short inner RKC run on the fast part; the page states the averaged-force bounds, the parameter choice, the discrete stability theorem and the measured speedups."
status: established
aliases: [mRKC, multirate RKC, explicit stabilized multirate method, averaged force, modified equation with averaged force]
tags: [multirate, stabilized, explicit, stiff, stability, runge-kutta]
timestamp: 2026-10-20T06:18:00Z
---

# Multirate Runge–Kutta–Chebyshev (mRKC) methods and the averaged-force modified equation

The **multirate Runge–Kutta–Chebyshev method (mRKC)** of
[Abdulle, Grote & Rosilho de Souza (2022)](/sources/abdulle-2022.md) is an explicit
[stabilized Runge–Kutta method](/methods/stabilized-explicit-runge-kutta.md) for
$y'=f(y)=f^{\{\mathrm f\}}(y)+f^{\{\mathrm s\}}(y)$ in which $f^{\{\mathrm s\}}$ is expensive but only
mildly stiff and $f^{\{\mathrm f\}}$ is cheap but severely stiff, typically because it acts on
the few degrees of freedom of a locally refined mesh (§1). A plain RKC method takes its
stage count $s$ from the spectral radius $\rho$ of the whole Jacobian, so every expensive
$f^{\{\mathrm s\}}$ evaluation is repeated about $\sqrt{h\rho}$ times because of a few stiff
components. mRKC instead applies an outer $s$-stage RKC scheme, whose stage count is set by
the slow spectral radius $\rho_{\mathrm s}$ alone, to a **modified equation** whose
right-hand side, the **averaged force**, is evaluated by a short inner $m$-stage RKC run on
the fast part. Page-local symbols: $\rho_{\mathrm f}$, $\rho_{\mathrm s}$ the spectral radii of
the Jacobians of $f^{\{\mathrm f\}}$, $f^{\{\mathrm s\}}$; $\eta>0$ the length of the averaging
interval (not the registry entropy, and not a step of the solution); $m$ the number of inner
RKC stages (not the registry step ratio $H/h$, which mRKC does not have); $u$ the auxiliary
solution; $\phi_1(z)=(e^z-1)/z$ is the registry $\phi_1$. The step is $h$ (the source's
$\tau$).

## The averaged force and the modified equation

For $\eta>0$ the averaged force is (Def. 2.1, Eqs. (2.1)–(2.3))

$$f_\eta(y)=\frac1\eta\bigl(u(\eta)-y\bigr),\qquad u'=f^{\{\mathrm f\}}(u)+f^{\{\mathrm s\}}(y),\quad u(0)=y,$$

with $f^{\{\mathrm s\}}$ frozen at $y$ over $[0,\eta]$; equivalently
$f_\eta(y)=f^{\{\mathrm s\}}(y)+\frac1\eta\int_0^\eta f^{\{\mathrm f\}}(u(\theta))\,d\theta$, and
$f_0=f$. The modified equation is $y_\eta'=f_\eta(y_\eta)$, $y_\eta(0)=y_0$. The multirate
strategy is to solve the modified equation with an explicit method whose stability depends
only on $f^{\{\mathrm s\}}$ and to evaluate each $f_\eta$ with an explicit method whose
stability depends only on $f^{\{\mathrm f\}}$.

**Linear fast part.** If $f^{\{\mathrm f\}}(y)=A^{\{\mathrm f\}}y$ (page-local matrix), then
$u(\eta)=e^{\eta A^{\{\mathrm f\}}}y+\eta\phi_1(\eta A^{\{\mathrm f\}})f^{\{\mathrm s\}}(y)$ and

$$f_\eta(y)=\phi_1(\eta A^{\{\mathrm f\}})\,f(y)$$

(Lemma 2.2, Eqs. (2.6)–(2.7)). The auxiliary solve is then one exponential-Euler step of
length $\eta$ applied to the full problem (Remark 2.3; see
[exponential integrators](/methods/exponential-integrators.md)), but mRKC never forms
$\phi_1(\eta A^{\{\mathrm f\}})$, and $\eta$ is not a step size. Since $0<\phi_1(z)<1$ for
real $z<0$ and $\phi_1(z)\to0$ as $z\to-\infty$, the averaged force **damps (compresses)
the fast spectrum**.

**Smoothing bound** (Lemma 2.2). If $f^{\{\mathrm f\}}$ is one-sided Lipschitz,
$\langle f^{\{\mathrm f\}}(z)-f^{\{\mathrm f\}}(y),z-y\rangle\le\mu_{\mathrm f}\lVert z-y\rVert^2$
(page-local constant $\mu_{\mathrm f}$), then
$\lVert f_\eta(y)\rVert\le\phi_1(\eta\mu_{\mathrm f})\lVert f(y)\rVert$.

**Contractivity and error** (Thms. 2.4–2.5). Assume $A^{\{\mathrm f\}}$ symmetric, $f$
one-sided Lipschitz through its Jacobian with constant $\mu\le0$ (page-local), and
$A^{\{\mathrm f\}}$ commuting with $\partial f^{\{\mathrm s\}}/\partial y$. Then $f_\eta$ is
one-sided Lipschitz with constant
$\mu_\eta=\mu\min_{\lambda\in\lambda(A^{\{\mathrm f\}})}\phi_1(\eta\lambda)\le0$, so contractivity
of the original problem is inherited, and

$$\lVert y(t)-y_\eta(t)\rVert\le\max_{\lambda\in\lambda(A^{\{\mathrm f\}})}\lvert1-\phi_1(\eta\lambda)\rvert\int_0^te^{\mu_\eta(t-\theta)}\lVert f(y(\theta))\rVert\,d\theta,$$

a bound independent of the stiffness of $f^{\{\mathrm f\}}$ and $\mathcal O(\eta)$ as
$\eta\to0$ (Eq. (2.9)). The authors call the commutativity hypothesis "a rather strong
assumption, rarely satisfied in practice" and use it for insight only.

**Spectral bound without scale separation** (Lemma 2.6, Thm. 2.7). On the scalar multirate
test equation $y'=\lambda^{\{\mathrm f\}}y+\lambda^{\{\mathrm s\}}y$ with real
$\lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\le0$ (see
[multirate linear stability](/definitions/multirate-linear-stability.md)),
$f_\eta(y)=\phi_1(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})y$. For
$\lambda^{\{\mathrm s\}}<0$,

$$\phi_1(\eta\lambda^{\{\mathrm f\}})\bigl(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}}\bigr)\in[\lambda^{\{\mathrm s\}},0]\quad\text{for all }\lambda^{\{\mathrm f\}}\le0\qquad\Longleftrightarrow\qquad\eta\ge\frac2{\lvert\lambda^{\{\mathrm s\}}\rvert},$$

the constant 2 being $1/\phi_1'(0)$. For $\eta\ge2/\rho_{\mathrm s}$ the stiffness of the
modified equation is therefore that of $f^{\{\mathrm s\}}$ alone, for every fast eigenvalue,
with no assumption of scale separation between the parts (§2.3).

## The mRKC scheme

Outer scheme (Eq. (3.5)): first-order RKC with $s$ stages (recurrence and damped Chebyshev
coefficients on [stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md),
damping $\varepsilon_{\mathrm d}$ as there), applied to the modified equation with $f_\eta$
replaced by its numerical approximation $\bar f_\eta(y)=(u_\eta-y)/\eta$ (Eq. (3.6)). Inner
scheme (Eq. (3.7)): $u_\eta$ is **one step** of length $\eta$ of an $m$-stage first-order RKC
method on $u'=f^{\{\mathrm f\}}(u)+f^{\{\mathrm s\}}(y)$ from $u(0)=y$, with its own Chebyshev
coefficients (Eq. (3.8)). $f^{\{\mathrm s\}}(y)$ is evaluated once per outer stage and frozen
across the inner stages, so a step costs $s$ evaluations of $f^{\{\mathrm s\}}$ and $sm$ of
$f^{\{\mathrm f\}}$. No interpolation or extrapolation between stages is needed, and the
fast and slow roles may change in time (§3.2).

**Parameter choice** (Eqs. (3.4), (3.9)). With $\beta=2-\frac43\varepsilon_{\mathrm d}$
(page-local; $\varepsilon_{\mathrm d}=0.05$), $s$ and $m$ are the smallest integers with

$$h\rho_{\mathrm s}\le\beta s^2,\qquad \eta\rho_{\mathrm f}\le\beta m^2,\qquad \eta=\frac{6h\,m^2}{\beta s^2(m^2-1)};$$

in practice $m$ is taken from $6h\rho_{\mathrm f}\le\beta^2s^2(m^2-1)$ and then $\eta$ from the
last relation. The spectral radii are estimated by nonlinear power methods. The formula is
undefined for $m=1$; Abdulle et al. state separately that for $m=1$ mRKC and RKC coincide
(§5.3).

**Relaxed choice under scale separation** (Eq. (3.13)): $\eta=2h/(\beta s^2)$ with the inner
condition $\eta\rho_{\mathrm f}\le\bar\beta m^2$, $\bar\beta=2-\frac43\bar\varepsilon_{\mathrm d}\approx1.86$,
$\bar\varepsilon_{\mathrm d}=0.1$ (page-local). It is justified under scale separation
(Remark 4.4) and verified numerically on locally refined parabolic problems without it
(§5.5).

## Stability and accuracy of the discrete method

Let $P_m(z)$ be the stability polynomial of the inner RKC and
$\Phi_m(z)=(P_m(z)-1)/z$ (page-local), the discrete analogues of $e^z$ and $\phi_1(z)$.
On the scalar test equation the inner run gives
$\bar f_\eta(y)=\Phi_m(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})y$
(Lemma 4.1, Eq. (4.4)), so the **mRKC stability polynomial** is

$$R_{s,m}=P_s\bigl(h\,\Phi_m(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})\bigr),$$

with $P_s$ the outer RKC polynomial (Def. 4.2; the source writes $R_s$). Unlike
[multirate linear stability](/definitions/multirate-linear-stability.md) of GARK methods,
it has a single step $h$ and the inner run is parametrized by $\eta$, not by a step ratio.

- **Lemma 4.3** (discrete analogue of Lemma 2.6). For damping below an $m$-dependent
  threshold, $\Phi_m(z)(z+w)\in[w,0]$ for all $z$ in the inner stability interval iff
  $\lvert w\rvert\ge2/P_m''(0)$ ($w\le0$ page-local). For $\varepsilon_{\mathrm d}=0$,
  $2/P_m''(0)=6m^2/(m^2-1)>6$, against $2$ in the continuous case, because $\Phi_m$ is
  flatter at 0 than $\phi_1$. *(Compiler check, not in the sources: with
  $P_m(z)=T_m(1+z/m^2)$ and $T_m''(1)=m^2(m^2-1)/3$, $P_m''(0)=(m^2-1)/(3m^2)$.)*
- **Theorem 4.5.** For $\lambda^{\{\mathrm f\}}\le0$, $\lambda^{\{\mathrm s\}}<0$, with
  $h\lvert\lambda^{\{\mathrm s\}}\rvert$ and $\eta\lvert\lambda^{\{\mathrm f\}}\rvert$ inside the real
  stability intervals $\ell_s$, $\ell_m$ of the outer and inner RKC, and

  $$\eta\ge\frac{6h}{\ell_s}\,\frac{m^2}{m^2-1},$$

  $\lvert R_{s,m}\rvert\le1$ (Eq. (4.5)). With $\ell_s\approx\beta s^2$ this is the choice (3.4).
  The damping restriction of Lemma 4.3 is "probably not needed in practice": the
  equivalence was checked numerically for any $\varepsilon_{\mathrm d}\ge0$ (Fig. 8). Because
  $\eta$ depends on $f^{\{\mathrm s\}}$ only through $s$ and $\ell_s\ge2$, $\eta$ cannot blow up
  as $\lambda^{\{\mathrm s\}}\to0$ (p. 15).
- **Necessity under coupling** (§4.1, Eqs. (4.6)–(4.8), Fig. 9). On the real symmetric
  $2\times2$ model with fast and slow diagonal entries and coupling $\sigma$, $\sigma^2\le\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}$
  (page-local $\sigma$), whose fast and slow parts are not simultaneously triangularizable
  unless $\sigma=0$ or $\sigma^2=\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}$, the choice (4.5)
  keeps the method stable, while $\eta=0.9$ or $0.95$ of the bound produces an instability
  near the origin even for weak coupling ($\sigma=10^{-1},10^{-2},10^{-3}$ times
  $\sqrt{\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}}$). This is numerical evidence.
- **Theorem 4.6.** mRKC is first-order accurate: the local error is
  $\mathcal O(\eta h+h^2)$, and (3.4) gives $\eta\le8h$. The proof splits the error into
  modified-equation, inner-RKC and outer-RKC parts.

## Cost model

With $\varepsilon_{\mathrm d}=0$, real $s,m$, $\rho=\rho_{\mathrm f}+\rho_{\mathrm s}$ (a modelling
choice, p. 11) and relative costs $c_{\mathrm f}+c_{\mathrm s}=1$ of one evaluation of each part
(page-local), RKC costs $\sqrt{h\rho/2}$ and mRKC
$(1-c_{\mathrm f})\sqrt{h\rho_{\mathrm s}/2}+c_{\mathrm f}\sqrt{3h\rho_{\mathrm f}/2+h\rho_{\mathrm s}/2}$
(Eqs. (3.10)–(3.11)), from $s=\sqrt{h\rho_{\mathrm s}/2}$ and $m^2=3\rho_{\mathrm f}/\rho_{\mathrm s}+1$.
With $r=\rho_{\mathrm f}/\rho_{\mathrm s}$ (page-local) the predicted speedup is

$$S=\frac{\sqrt{1+r}}{1+c_{\mathrm f}\bigl(\sqrt{1+3r}-1\bigr)}\qquad\text{(Eq. (3.12))},$$

which exceeds one iff
$c_{\mathrm f}<(\sqrt{1+r}-1)/(\sqrt{1+3r}-1)$, a threshold above $0.5$ for $r>8$ (Fig. 5b).
The relaxed choice (3.13) gives a speedup above one for every $c_{\mathrm f}<1$ and above $S$
for every $c_{\mathrm f}$ (Fig. 6).

## Numerical evidence

All on first-order methods, with RKC, second-order RKC2 and implicit Euler (IE, Jacobian
and LU once per step) as comparators (§5):

| Problem | Finding |
|---|---|
| [Robertson](/benchmarks/robertson-problem.md), $f^{\{\mathrm f\}}=$ the $-10^4y_2y_3$ term | RKC and mRKC both first order, errors hardly distinguishable; mean $\eta\ll h$; mRKC's $s$ falls with $\rho_{\mathrm s}$ while RKC's grows with $\rho$ (Figs. 10–11) |
| [Heat equation](/benchmarks/heat-equation.md), unit square, two refinement levels, first-order DG | first-order space–time convergence in $H^1$, errors as RKC, much smaller $s$, constant $m$ (Fig. 12) |
| Diffusion through a narrow channel of width $1/2^k$, $k=0,\dots,15$ | speedup over RKC (CPU time) always $\ge1$, up to about 40; RKC–mRKC difference at most $3\cdot10^{-4}$ (Fig. 15); at width $1/2^{12}$ mRKC 10 to 70 times faster than RKC2, IE always slightly faster than mRKC (Fig. 16) |
| Nonlinear integro-differential problem, $N=100$ and $3200$ | at $N=3200$ mRKC fastest; IE dominated by the direct solver; RKC and RKC2 "could not be run to completion" (Fig. 17) |
| Reaction–convection–diffusion on three refined meshes | $h\rho_\eta\le\beta s^2$ iff $\lvert w(\eta)\rvert\ge2$, with $\rho_\eta$ the spectral radius of the averaged-force Jacobian and $w(\eta)=-\eta\ell_s/h$ (page-local): the relaxed condition (3.13) is necessary and sufficient here without scale separation (§5.5, Figs. 18–19) |

The conclusion states that mRKC is up to 40 times faster than RKC and up to 70 times cheaper
than RKC2 "for moderately high error tolerances", and that it "performed similarly, or even
better, than IE" in all experiments (§6).

## Relation to other multirate approaches

- **Multirate infinitesimal methods.** [MIS and MRI-GARK](/methods/multirate-infinitesimal-methods.md)
  also solve an auxiliary fast problem forced by slow information, but their analysis assumes
  the fast problem is integrated exactly. mRKC discretizes the fast problem explicitly,
  with compressed spectrum, and its stability analysis is fully discrete (Abdulle et al.
  2022, §2.1). Both freeze or interpolate slow data on the fast interval; in mRKC the slow
  force is frozen at the outer stage value.
- **Multirate GARK.** Abdulle et al. state that semi-discrete
  [multirate GARK](/methods/multirate-gark.md) and MRI-GARK schemes typically need "some
  implicitness or very small steps sizes" for stability in practice (p. 3), and that earlier
  multirate RK schemes with predictor and interpolation or extrapolation steps are "prone to
  instability" (p. 2).
- **Local time stepping.** mRKC splits the right-hand side, not the mesh, but its target is
  the locally refined mesh of [local time stepping](/methods/local-time-stepping.md): the
  fast part collects the degrees of freedom on and next to the refined elements. Unlike
  interpolation-based multirate RKC with adaptive mesh refinement, whose time interpolation
  of missing stage values "can cause numerical instabilities" according to the authors'
  own earlier report as recalled there (§1), mRKC needs no interpolation.
- **Heterogeneous multiscale and projective methods** need scale separation; the averaged
  force does not (§2.1, Thm. 2.7).
- **Mixed precision.** [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) recall mRKC
  (§4.1) and run it with most evaluations in reduced precision, first order preserved (§4.2,
  Thm. 4.3); see
  [mixed-precision Runge–Kutta methods](/methods/mixed-precision-runge-kutta.md).

## Qualifications

- **First order only.** Every result on this page is for first-order outer and inner RKC.
  The theorems on the modified equation (2.4, 2.5) need a linear symmetric fast part
  commuting with the slow Jacobian; Theorem 4.5 is for the scalar test equation; the
  coupled $2\times2$ necessity and the relaxed condition (3.13) without scale separation are
  numerical findings.
- **Comparison with implicit Euler.** The conclusion's "similarly, or even better, than IE"
  covers the narrow-channel case at width $1/2^{12}$, where by the authors' own Fig. 16 IE
  "always remains slightly faster"; the linear symmetric Laplacian favours IE there.
- **Robertson data.** The Robertson test starts from $y(0)=(1,\,2\cdot10^{-5},\,10^{-1})$, not
  the standard $(1,0,0)$; the paper gives no reason beyond the statement that with these
  data only the $-10^4y_2y_3$ term is severely stiff.
- **Printed slips (arXiv v6).** The proof of Thm. 2.4 minimizes over the eigenvalues of
  $A$ in its last line where the statement uses those of the fast matrix $A^{\{\mathrm f\}}$.
  In App. A the second critical point is printed $z_2=-2m^2\sin(\pi/m)$; with
  $1-\cos\theta=2\sin^2(\theta/2)$ at $\theta=2\pi/m$ it is $-2m^2\sin^2(\pi/m)$, the form the
  next line of the proof uses. Eq. (4.8) carries a stray $y$ ($A_\eta=\Phi_m(\eta A^{\{\mathrm f\}})Ay$
  for the matrix $\Phi_m(\eta A^{\{\mathrm f\}})A$, as restated in §5.5). The caption of Fig. 13
  says $t=1$ for a problem run to $T=0.1$.
- The source writes $\tau$ for the step, $f_F$, $f_S$ for the parts, $\lambda$ and $\zeta$ for
  the fast and slow eigenvalues of the test equation, $\varphi$ for $\phi_1$, $R_s$ for the
  outer stability polynomial, $\varepsilon$ for the damping, $c_F$, $r_\rho$ for the cost
  ratios; these are translated above.

# Citations

- [Abdulle, Grote & Rosilho de Souza (2022)](/sources/abdulle-2022.md) — §1, §2 (Def. 2.1, Lemma 2.2, Remark 2.3, Thms. 2.4–2.5, Lemma 2.6, Thm. 2.7), §3 (Eqs. 3.1–3.13, Figs. 5–6), §4 (Lemma 4.1, Def. 4.2, Lemma 4.3, Remark 4.4, Thms. 4.5–4.6, §4.1 Eqs. 4.6–4.8, Figs. 8–9), §5 (Figs. 10–19), §6, App. A.
- [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) — §4.1 (mRKC recalled), §4.2 (mixed-precision mRKC, Thm. 4.3).
