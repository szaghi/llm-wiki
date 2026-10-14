# Directory Update Log

## 2026-10-13

* **Scaffolded the bundle and ingested [Riley, Hobson & Bence (2006)](/sources/riley-2006.md)**,
  the founding textbook (D20). Scoped read: preface, contents, ch. 12 (Fourier series),
  ch. 13 (integral transforms, all exercises included) and §§27.5–27.6 (finite differences;
  differential equations). Chs. 15, 17, 24, 25 and §27.7 onward, to which the text defers,
  were not read.
  * **Notation registry seeded** ([notation](/notation.md)). Sections: independent variables
    and grids; Fourier series; Fourier transform (canonical symmetric $1/\sqrt{2\pi}$ pair,
    forward kernel $e^{-\mathrm ikx}$); discrete Fourier analysis (reserved: $\xi = kh$,
    $\tilde k$ and $\tilde\xi$, $G$, and $\hat f^N_m$ with $1/N$ normalization); generalized functions,
    convolution and correlation; Laplace transform (written $\mathcal L\{f\}(s)$ in full); difference
    operators and time stepping ($D_0$, $D_\pm$, $D_+D_-$, $t^n$, $y^n$, $F(t,y)$, $\lambda$);
    special functions, widths and example parameters.
  * **New pages (21).** Definitions: [Dirichlet conditions](/definitions/dirichlet-conditions.md),
    [Fourier series](/definitions/fourier-series.md), [Fourier transform](/definitions/fourier-transform.md),
    [Dirac delta function](/definitions/dirac-delta-function.md), [convolution](/definitions/convolution.md),
    [cross-correlation and energy spectrum](/definitions/cross-correlation.md),
    [Laplace transform](/definitions/laplace-transform.md). Results:
    [convergence of Fourier series](/results/fourier-series-convergence.md),
    [Gibbs phenomenon](/results/gibbs-phenomenon.md), [Parseval's theorem](/results/parseval-theorem.md),
    [convolution theorem](/results/convolution-theorem.md), [Wiener–Khinchin theorem](/results/wiener-khinchin-theorem.md),
    [Fourier transform properties](/results/fourier-transform-properties.md),
    [Laplace transform properties](/results/laplace-transform-properties.md). Operators:
    [$D_0$](/operators/central-difference.md), [$D_\pm$](/operators/one-sided-differences.md),
    [$D_+D_-$](/operators/second-central-difference.md). Methods: [forward Euler](/methods/forward-euler-method.md),
    [Milne's method](/methods/milne-central-difference-method.md). Benchmarks:
    [square wave](/benchmarks/square-wave.md), [exponential-decay test equation](/benchmarks/exponential-decay-test-equation.md).
  * **Compiler notes (hypothesis)** on the Euler page (the printed $\lvert G\rvert < 1$ is
    stricter than non-divergence, since $\Delta t = 2$ is bounded; the large-step rows of table
    27.10 are step counts) and the Milne page (a parasitic root with $\lvert G_2\rvert > 1$ for
    every $\Delta t > 0$).
  * **Bibliography:** 1 entry (riley-2006). The chapters read cite no external work, so the
    `--pending` warning for riley-2006 is expected and permanent.
  * Out of scope, read but not compiled: Taylor-series, Adams, predictor–corrector and
    Runge–Kutta schemes and isoclines (§§27.6.2–27.6.5). None carries a Fourier or stability
    statement.
