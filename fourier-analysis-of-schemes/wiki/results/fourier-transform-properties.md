---
type: Result
title: "Fourier transform properties"
description: "Operational rules of the unitary Fourier transform: differentiation multiplies the transform by i omega (so a derivative of order p by (i omega)^p, the gradient by i k and the Laplacian by -k^2), integration divides by i omega plus a delta for the constant, scaling, translation as a phase factor, sign change and conjugation, exponential multiplication as a shift of the argument, the transforms of t f(t) and of odd or periodic functions, and their use to turn the wave, heat and Poisson equations into algebra in k."
status: established
aliases: [differentiation theorem, shift theorem, translation property, modulation theorem, scaling theorem]
tags: [fourier-transform]
timestamp: 2026-10-14T00:00:00Z
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

[Arfken et al. (2013)](/sources/arfken-2013.md) list the rules in three
dimensions (§20.3, eqs. 20.48–20.56) under their opposite-sign convention
(see the [Fourier transform](/definitions/fourier-transform.md)). Mapped to the
registry, with $\mathbf a$ a fixed vector and $a > 0$:

| Rule (Arfken et al.) | Registry form | Eq. |
|---|---|---|
| Translation | $\mathcal F[f(\mathbf r - \mathbf a)] = e^{-\mathrm i\mathbf k\cdot\mathbf a}\hat f(\mathbf k)$ | 20.48 |
| Change of scale | $\mathcal F[f(a\mathbf r)] = a^{-3}\hat f(\mathbf k/a)$ | 20.49 |
| Sign change | $\mathcal F[f(-\mathbf r)] = \hat f(-\mathbf k)$ | 20.50 |
| Complex conjugation | $\mathcal F[f^*(-\mathbf r)] = \hat f^*(\mathbf k)$ | 20.51 |
| Gradient | $\mathcal F[\nabla f] = \mathrm i\mathbf k\,\hat f(\mathbf k)$ (printed with $-\mathrm i$) | 20.52 |
| Laplacian | $\mathcal F[\nabla^2 f] = -k^2\hat f(\mathbf k)$ | 20.53 |
| $p$-th derivative (1-D) | $\mathcal F[f^{(p)}(t)] = (\mathrm i\omega)^p\hat f(\omega)$ (printed with $(-\mathrm i\omega)^p$) | 20.55–20.56 |
| Multiplication by $t^p$ | $\mathcal F[t^pf(t)] = \mathrm i^p\,\mathrm d^p\hat f/\mathrm d\omega^p$ (printed with $\mathrm i^{-p}$) | ex. 20.3.5 |

After the sign map every entry agrees with Riley et al.'s, where both state
it. Before mapping, only the sign of $\mathrm i$ differs, in the translation,
derivative and $t^p$ rules. The scaling rule is again printed without an absolute
value. Arfken et al. derive the gradient and Laplacian rules from the inverse
formula and note that "this demonstration requires the existence of the
integrals involved" (p. 980). They leave the first four rules to exercises.

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
  not made in the chapters read of either source. Arfken et al.'s exercise
  20.3.6 is the case of a point source: for $\varphi'' - \kappa_0^2\varphi = \delta(x)$
  the transform method gives $\varphi = -e^{-\kappa_0\lvert x\rvert}/(2\kappa_0)$
  (their neutron-diffusion form, rescaled).
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

## Partial differential equations in transform space

Arfken et al. (§20.3, pp. 981–985) use the differentiation rules to replace a
PDE in $(x, t)$ by an ODE in $t$ for each $k$, solve it, and transform back. In
registry form, with $\varphi(x,t)$ the unknown:

* **Wave equation** $\varphi_{tt} = c_0^2\varphi_{xx}$, $\varphi(x,0) = f(x)$,
  $\varphi_t(x,0) = 0$ (Example 20.3.1). The transformed equation is
  $\hat\varphi_{tt} = -c_0^2k^2\hat\varphi$, so
  $\hat\varphi(k,t) = \hat f(k)\cos(c_0kt)$ (eq. 20.63), and
  $\varphi(x,t) = \tfrac12[f(x - c_0t) + f(x + c_0t)]$ (eq. 20.65): half the
  initial profile travels each way at speed $c_0$.
* **Heat equation** $\varphi_t = \nu\varphi_{xx}$ (Example 20.3.2). Each mode
  decays independently, $\hat\varphi(k,t) = \hat\varphi(k,0)\,e^{-\nu k^2t}$, and for
  an initial $\delta(x)$ the inverse transform is the Gaussian
  $\varphi(x,t) = (4\pi\nu t)^{-1/2}\exp(-x^2/(4\nu t))$. The source prints it
  with the constant $C$, the transform of $\delta$ (eq. 20.14); the explicit
  constant is the compiler's substitution of $C = (2\pi)^{-1/2}$.
* **Poisson's Green's function** $\nabla^2\mathcal G = \delta(\mathbf r - \mathbf r_0)$
  (Example 20.3.3), with $\mathbf r_0$ a fixed source point:
  $\hat{\mathcal G} = -(2\pi)^{-3/2}e^{-\mathrm i\mathbf k\cdot\mathbf r_0}/k^2$ and
  $\mathcal G = -1/(4\pi\lvert\mathbf r - \mathbf r_0\rvert)$. The form in
  $\mathbf r - \mathbf r_0$ is found, not assumed.

A compiler remark: these are the exact Fourier-space evolutions of the model
equations. Each wavenumber keeps its amplitude and moves at the same speed
$c_0$ (wave), or decays at rate $\nu k^2$ (heat). They are the continuum
behaviour against which the per-step factor $G(\xi)$ of a scheme is later
compared, though neither source makes that comparison.

**Limits stated by the source** (p. 984). The transforms and their inverses
must exist. The method yields a single solution, so it works only when the
solution is unique. Requiring an exponential Fourier transform "imposes
Dirichlet boundary conditions at infinity". For initial data the
[Laplace transform](/definitions/laplace-transform.md) is "more natural".

## See also

For odd and even $f$ see the sine and cosine transforms on the
[Fourier transform](/definitions/fourier-transform.md) page. For products and
correlations see the [convolution theorem](/results/convolution-theorem.md)
and the [Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md).

# Citations

* [Riley et al. (2006)](/sources/riley-2006.md), §13.1.5 (pp. 443–445); exercises 13.2, 13.5 (pp. 460–461) and answer to 13.5 (p. 466).
* [Arfken et al. (2013)](/sources/arfken-2013.md), §20.3 (eqs. 20.48–20.67, Examples 20.3.1–20.3.3, pp. 980–985); exercises 20.3.1–20.3.6.
