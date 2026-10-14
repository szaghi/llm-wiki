---
type: Result
title: "Fourier transform properties"
description: "Operational rules of the unitary Fourier transform: differentiation multiplies the transform by i omega (so a derivative of order p by (i omega)^p), integration divides by i omega plus a delta for the constant, scaling, translation as a phase factor, exponential multiplication as a shift of the argument, and the transforms of t f(t) and of odd or periodic functions."
status: established
aliases: [differentiation theorem, shift theorem, translation property, modulation theorem, scaling theorem]
tags: [fourier-transform]
timestamp: 2026-10-13T00:00:00Z
---

# Fourier transform properties

For the unitary [Fourier transform](/definitions/fourier-transform.md)
$\hat f(\omega) = \mathcal F[f(t)]$ the source lists, "without proof; they can
be verified by working from the definition"
([Riley et al. (2006)](/sources/riley-2006.md), §13.1.5, pp. 443–444):

| Rule | Statement | Eq. |
|---|---|---|
| Differentiation | $\mathcal F[f'(t)] = \mathrm i\omega\,\hat f(\omega)$, hence $\mathcal F[f''(t)] = -\omega^2\hat f(\omega)$, and so on | 13.28 |
| Integration | $\mathcal F\!\left[\int^t f(u)\,\mathrm du\right] = \frac{1}{\mathrm i\omega}\hat f(\omega) + 2\pi c\,\delta(\omega)$, with $c$ the constant of integration | 13.29 |
| Scaling | $\mathcal F[f(at)] = \frac1a\hat f(\omega/a)$ | 13.30 |
| Translation | $\mathcal F[f(t + a)] = e^{\mathrm ia\omega}\hat f(\omega)$ | 13.31 |
| Exponential multiplication | $\mathcal F[e^{\alpha t}f(t)] = \hat f(\omega + \mathrm i\alpha)$, $\alpha$ real, imaginary or complex | 13.32 |

## Scope of each rule

* **Differentiation** is the one rule proved (p. 444), by integration by
  parts. The boundary term vanishes "if $f(t)\to0$ at $t = \pm\infty$, as it
  must since $\int\lvert f\rvert\,\mathrm dt$ is finite". In space it reads
  $\mathcal F[f'(x)] = \mathrm ik\,\hat f(k)$, so in Fourier space exact
  differentiation is multiplication by $\mathrm ik$. Exercise 13.5 uses this,
  through $\mathcal F[\varphi''] = -k^2\hat\varphi$, to solve
  $\varphi'' - \kappa_0^2\varphi = f$ as
  $\varphi(x) = -\frac{1}{\sqrt{2\pi}}\int\frac{e^{\mathrm ikx}\hat f(k)}{k^2 + \kappa_0^2}\,\mathrm dk$.
  Here $\varphi$ is the unknown and $\kappa_0$ a constant (the source's $\phi$
  and $K$). The comparison of difference operators against $\mathrm ik$ is
  not made in the chapters read.
* **Scaling** is printed as $\frac1a\hat f(\omega/a)$ without an absolute
  value. A compiler remark, not in the source: the formula as printed holds
  for $a > 0$, and for $a < 0$ the factor is $1/\lvert a\rvert$, as for
  $\delta(at)$ (eq. 13.16). Exercise 13.2(c) states the same form,
  $\mathcal F[f(at + c)] = \frac{e^{\mathrm i\omega c/a}}{a}\hat f(\omega/a)$
  (source: $m$ for $a$).
* **Exponential multiplication** with imaginary $\alpha = \mathrm i\omega_c$ is the
  modulation shift used for amplitude-modulated carriers: the spectrum moves to
  $\hat f(\omega - \omega_c)$ (eqs. 13.33–13.34). Here $\omega_c$ is the
  carrier frequency.
* Exercises 13.2(a)–(b), stated for the reader to prove: if $f$ has period
  $a$ then $\hat f(k) = 0$ unless $ka = 2\pi p$ for an integer $p$, and
  $\mathcal F[t f(t)] = \mathrm i\,\mathrm d\hat f/\mathrm d\omega$.

For odd and even $f$ see the sine and cosine transforms on the
[Fourier transform](/definitions/fourier-transform.md) page. For products and
correlations see the [convolution theorem](/results/convolution-theorem.md)
and the [Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.5 (pp. 443–445); exercises 13.2, 13.5 (pp. 460–461) and answer to 13.5 (p. 466).
