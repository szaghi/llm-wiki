---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-14T00:00:00Z
---

# Notation registry

This page is **normative** for the bundle. Concept pages must use these symbols
exclusively; each Source page maps its source's native notation to this
registry in a `# Notation map` section. Extend this registry (and record the
extension in [the log](/log.md)) before writing math that needs a symbol it
lacks.

The registry was seeded once, at scaffolding (2026-10-13), from the
conventions of the founding source and of the Fourier-analysis literature on
difference schemes. It is wiki-native law from then on. Entries marked
**reserved** are fixed now so that later sources map onto them, but no concept
page uses them yet; their meaning is confirmed, and if needed refined, when
the first source that defines them is ingested.

## Independent variables, grids and indices

| Symbol | Meaning |
|---|---|
| $x$ | space coordinate (one dimension); $\mathbf r = (x, y, z)$ in three dimensions |
| $t$ | time; also the independent variable of an ordinary differential equation |
| $L$ | period in $x$ of a periodic function (one period is $x_0 \le x < x_0 + L$, $x_0$ arbitrary) |
| $T$ | period in $t$ of a periodic function of time |
| $h$ | uniform grid spacing in $x$; grid points $x_j = x_0 + jh$ |
| $j$ | spatial grid index; $f_j = f(x_j)$ is a grid value |
| $N$ | number of grid points or samples in one period |
| $\Delta t$ | time step; time levels $t^n = t^0 + n\,\Delta t$ |
| $n$ | time-level index, written as a superscript: $y^n \approx y(t^n)$ |
| $f^{(p)}$, $f^{(p)}_j$ | $p$-th derivative of $f$, and its value at $x_j$ |
| $\mathrm i$ | imaginary unit, $\mathrm i^2 = -1$ |
| $z^*$ | complex conjugate of $z$ (a superscript star is never a convolution) |

## Fourier series

| Symbol | Meaning |
|---|---|
| $m$ | integer mode index, $m \in \mathbb Z$ (series) |
| $k_m = 2\pi m/L$ | wavenumber of mode $m$ on period $L$ |
| $\omega_m = 2\pi m/T$ | angular frequency of mode $m$ on period $T$ (series in $t$); $\omega_1$ is the fundamental |
| $a_m$, $b_m$ | real (cosine, sine) Fourier coefficients, $m \ge 0$ and $m \ge 1$ |
| $\hat f_m$ | complex Fourier coefficient of $f$; $\hat f_m = \frac1L\int_{x_0}^{x_0+L} f(x)\,e^{-\mathrm i k_m x}\,\mathrm dx$ |
| $S_M f$ | partial sum of the series through $\lvert m\rvert \le M$ (or $m \le M$ for the real form) |

Series pair (normalization of the founding source, kept as canonical):
$$f(x) = \sum_{m=-\infty}^{\infty} \hat f_m\,e^{\mathrm i k_m x} = \frac{a_0}{2} + \sum_{m=1}^{\infty}\bigl[a_m\cos k_m x + b_m \sin k_m x\bigr],$$
$$\hat f_m = \tfrac12(a_m - \mathrm i b_m),\qquad \hat f_{-m} = \tfrac12(a_m + \mathrm i b_m).$$
The coefficient carries the $1/L$; the series carries no factor. A source that
puts the factor elsewhere is mapped by a constant in its Notation map.

## Fourier transform

| Symbol | Meaning |
|---|---|
| $k$ | (angular) wavenumber, the variable conjugate to $x$; wavelength $2\pi/k$ |
| $\omega$ | angular frequency, the variable conjugate to $t$ |
| $\hat f(k)$, $\hat f(\omega)$ | Fourier transform of $f$; the argument distinguishes it from a series coefficient $\hat f_m$ |
| $\mathcal F[f]$, $\mathcal F^{-1}$ | the Fourier transform and its inverse as operators |
| $\hat f_s$, $\hat f_c$ | Fourier sine and cosine transforms |
| $\mathbf k$ | wave vector, conjugate to $\mathbf r$ |

Transform pair (**canonical normalization: symmetric, unitary**, that of the
founding source):
$$\hat f(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x)\,e^{-\mathrm i k x}\,\mathrm dx,\qquad f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat f(k)\,e^{\mathrm i k x}\,\mathrm dk,$$
and identically with $(t,\omega)$ in place of $(x,k)$; in $d$ dimensions the
factor is $(2\pi)^{-d/2}$. The forward transform carries $e^{-\mathrm i k x}$.
Under this convention Parseval's theorem has no constant and the convolution
theorem has a factor $\sqrt{2\pi}$. A source using the non-symmetric pair
($\int f e^{-\mathrm ikx}\mathrm dx$ forward, $\frac1{2\pi}\int$ back, or the
reverse) or the opposite sign is mapped by its constant and sign in its
Notation map; concept pages never mix conventions.

## Discrete Fourier analysis

| Symbol | Meaning |
|---|---|
| $\xi = kh$ | Scaled (non-dimensional) wavenumber of a grid mode $e^{\mathrm i k x_j} = e^{\mathrm i j\xi}$; sources writing it $w$, $\theta$, $\alpha$ or $\kappa$ map onto $\xi$. For the discrete Fourier transform on $N$ points of one period, $\xi = 2\pi m/N$ (in use from 2026-10-14, arfken-2013) |
| $\tilde k$, $\tilde\xi = \tilde k h$ | **reserved.** Modified (effective) wavenumber of a difference operator, in general complex |
| $G$, $G(\xi)$ | **reserved** as the amplification factor: the factor multiplying one mode (or, for a scalar recurrence, the solution) per time step, $y^{n+1} = G\,y^n$ |
| $\hat f^{N}_m$ | Discrete Fourier coefficient of $N$ samples, $\hat f^{N}_m = \frac1N\sum_{j=0}^{N-1} f_j\,e^{-2\pi\mathrm i jm/N}$ (normalized so that it approximates $\hat f_m$), with inverse $f_j = \sum_{m=0}^{N-1}\hat f^{N}_m\,e^{2\pi\mathrm i jm/N}$; periodic in $m$ with period $N$. A source with another normalization or sign is mapped by its constant and sign (in use from 2026-10-14, arfken-2013: see [discrete Fourier transform](/definitions/discrete-fourier-transform.md)) |

## Generalized functions, convolution and correlation

| Symbol | Meaning |
|---|---|
| $\delta(t)$, $\delta(\mathbf r)$ | Dirac delta function |
| $H(t)$ | Heaviside unit step, $H(0) = \tfrac12$ |
| $f * g$ | convolution (binary operator; see [convolution](/definitions/convolution.md) for the infinite and the one-sided forms) |
| $f \otimes g$, $C_{fg}(z)$ | cross-correlation $\int f^*(x)\,g(x+z)\,\mathrm dx$ |
| $C_{ff}(z)$ | auto-correlation of $f$ |
| $z$ | lag (displacement) argument of a correlation |

## Laplace transform

| Symbol | Meaning |
|---|---|
| $s$ | Laplace transform variable (real in the founding source) |
| $\mathcal L\{f\}(s)$ | Laplace transform $\int_0^\infty f(t)\,e^{-st}\,\mathrm dt$; always written in full, with braces (no overbar or capital-letter shorthand, which later sources reserve for cell averages and amplification factors) |
| $\mathcal L^{-1}$ | inverse Laplace transform |
| $s_0$ | abscissa of convergence: the transform exists for $s > s_0$ |

## Difference operators and time stepping

| Symbol | Meaning |
|---|---|
| $D_0$ | central first difference, $D_0 f_j = (f_{j+1} - f_{j-1})/(2h)$ |
| $D_+$, $D_-$ | forward and backward first differences, $D_+ f_j = (f_{j+1}-f_j)/h$, $D_- f_j = (f_j - f_{j-1})/h$ |
| $D_+D_-$ | second central difference, $D_+D_- f_j = (f_{j+1} - 2f_j + f_{j-1})/h^2$ |
| $y(t)$, $y^n$ | exact solution of an ordinary differential equation, and its discrete approximation at $t^n$ |
| $F(t, y)$ | right-hand side of the ODE $\mathrm dy/\mathrm dt = F(t, y)$ |
| $\lambda$ | coefficient of the linear test equation $\mathrm dy/\mathrm dt = \lambda y$ |

## Special functions, widths and example parameters

| Symbol | Meaning |
|---|---|
| $\mathrm{sinc}\,u$ | $(\sin u)/u$ (unnormalized) |
| $J_0$ | Bessel function of the first kind, order zero |
| $\Gamma$ | gamma function, $\Gamma(p+1) = p!$ for integer $p \ge 0$ (added 2026-10-14, arfken-2013) |
| $\beta$ | real abscissa of the Bromwich (inverse Laplace) contour, to the right of every singularity of the transform (added 2026-10-14, arfken-2013) |
| $r = \lvert\mathbf r\rvert$, $k = \lvert\mathbf k\rvert$ | radius and wavenumber magnitude (spherically symmetric transforms) |
| $\sigma_x$, $\sigma_k$, $\sigma_t$, $\sigma_\omega$ | root mean square widths of a function and of its transform (never $\Delta$, which is reserved for steps) |
| $f$, $g$ | generic functions; $\phi$ a generic function whose zeros are sought |
| $\varphi$ | unknown of a model differential equation solved by transform; $\kappa_0$ a real constant in it |
| $\varphi(x,t)$ | unknown of a model partial differential equation solved by transform (added 2026-10-14, arfken-2013; same symbol as the ODE unknown above) |
| $c_0$ | constant wave (phase) speed of the model wave equation $\varphi_{tt} = c_0^2\varphi_{xx}$ (added 2026-10-14, arfken-2013) |
| $\nu$ | constant diffusivity of the model heat equation $\varphi_t = \nu\,\varphi_{xx}$ (added 2026-10-14, arfken-2013) |
| $\mathcal G(\mathbf r, \mathbf r_0)$, $\mathbf r_0$ | Green's function of a model equation, and its fixed source point; calligraphic so as not to clash with the amplification factor $G$ (added 2026-10-14, arfken-2013) |
| $\alpha$ | complex constant in the exponential-multiplication rule |
| $\omega_c$ | carrier angular frequency (modulation) |
| $q$ | observed (convolved) distribution in the measurement model of convolution |
| $a$, $b$, $c$ | generic constants (linearity, shift and scaling rules, table entries) |
| $t_0$, $t_i$ | fixed time instants (delay, zeros of $\phi$) |
| $x_d$ | location of a jump discontinuity |
| $\epsilon$ | small positive increment in a one-sided limit |
| $\Omega$ | band limit of a truncated spectrum, $\lvert\omega\rvert \le \Omega$ |
| $A$ | amplitude of an example function |
| $\gamma$ | decay rate of an example function, $\gamma > 0$ |
| $u$, $v$ | dummy integration variables |
| $p$ | auxiliary integer index (orthogonality relations, symmetry rules) |
