---
type: Source
title: "Runge (1895) — Ueber die numerische Auflösung von Differentialgleichungen"
description: "The origin of multi-evaluation one-step methods: generalizes Simpson's rule to ODEs, giving the midpoint and Heun (trapezoidal) methods with second-order agreement and a four-evaluation third-order combination, proved by Taylor matching for single equations and two-equation systems; error judged by comparing variants and halving the step."
resource: "doi:10.1007/BF01446807"
source_kind: paper
authors: [Runge C.]
year: 1895
venue: "Math. Ann. 46:167–178"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1895-MathAnn-Runge-101007bf01446807.pdf"
tags: [time-discretization, runge-kutta]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

Runge observes that the numerical solution of differential equations
without analytic solutions had drawn little attention, apart from
Euler's polygon method, whose error is of the order of the step. He
generalizes the composite midpoint ("tangent trapezoid") and trapezoid
("chord trapezoid") quadratures, and Simpson's rule, which combines
them, to $u' = \mathcal L(t, u)$. The result is the first family of
one-step methods that evaluate the right-hand side several times per
step. Merged into [explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md).
In the paper's own words, quadrature methods "sich verallgemeinern
lassen, so dass sie mit ähnlichem Erfolge auf jede beliebige
Differentialgleichung angewendet werden können" (p. 167).

# Key claims

1. **Euler's method** (p. 167): attributed to Euler's "Introductio"; its
   convergence proof to Cauchy; low accuracy shown on a quadrature.
2. **Midpoint method** (eq. 2, p. 168) and **Heun method** (eq. 3,
   p. 169): both agree with the Taylor series of the exact step through
   $\Delta t^2$; Runge's "dritte Ordnung" is the local error order.
3. **The naive Simpson combination fails** (p. 169): (2) plus one third of
   (3) − (2) is third order only if $\mathcal L$ does not depend on $u$.
4. **Third-order method** (eqs. 3a, 4, p. 170): a modified chord step
   with one more evaluation makes the combination third order for any
   $\mathcal L$; four evaluations per step.
5. **Systems** (pp. 172–174): the construction and the third-order
   agreement carry over to two first-order equations, written out with
   grouped third-order terms; the extension to $n$-th order equations is
   asserted, not written out.
6. **Choice of independent variable** (pp. 172, 174): the expansion fails
   where $du/dt$ becomes infinite, so the faster-changing coordinate is
   taken as the independent variable.
7. **Error estimate** (pp. 172, 177–178): the agreement of the two
   variants and step halving; no error bound is proved and no step rule
   is given.

**Not in the paper:** a fourth-order method, the general $s$-stage form,
order conditions, stability analysis or automatic step control.

**Examples** (hand computation): $du/dt = (u - t)/(u + t)$, $u(0) = 1$,
with steps 0.2, 0.3, 0.5, giving $u(1) = 1.499$ against an exact value
between 1.498 and 1.499 (pp. 170–172); the meridian of a resting drop
or bubble, computed with a slide rule and a change of independent
variable, rim at $r = 0.818$, $z = 1.657$ to one unit in the third
decimal (pp. 175–177). Neither is a benchmark of this bundle.

# Notation map

| Runge (1895) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$ (independent variable), $\Delta x$ | $t$, $\Delta t$ | $x$ is space in the registry |
| $y$; $y, z$ (systems) | $u$ | |
| $f(x, y)$ | $\mathcal L(t, u)$ | $f$ is the flux in the registry |
| $\Delta' y$, $\Delta'' y$, $\Delta''' y$ | stage increments $\Delta t\,\mathcal L(Y_j)$ | |
| $f_1, f_2, f_{11}, \dots$; $U$, $V$ | words | partial derivatives; grouped terms |
| "Tangententrapez", "Sehnentrapez" | midpoint, Heun (trapezoidal) method | |

# Pages created or updated

* Contributed the origin section of [Explicit Runge–Kutta methods](/methods/explicit-runge-kutta.md).
* Updated [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) (origin of the second-order methods), [Step-size control](/methods/runge-kutta-step-size-control.md) (precursor).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1895-MathAnn-Runge-101007bf01446807.pdf`.
   * **Version.** The publisher's scan (12 pages, image only with a poor
     OCR layer); the text is signed "Potsdam, im September 1894".
   * **Identity.** doi:10.1007/BF01446807, checked on Crossref: Math. Ann.
     46(2):167–178, June 1895.
   * **How it was read.** Every page read visually (German). The
     difference (3a) − (2) on p. 170 and the tables of pp. 176–177 were
     re-rendered at higher resolution.
   * **Recorded as printed.** On p. 170 the difference (3a) − (2) prints
     $f_1$ where the algebra needs $f_{11}$.
   * **No reference list.** The paper has no bibliography and no
     footnotes. It names Euler's "Introductio", Cauchy, Simpson's rule and
     C. Dittmann's tables in the text, without bibliographic data or
     years. Nothing was merged into the bibliography, so this source
     stays on the `--pending` list (see `log.md`).
