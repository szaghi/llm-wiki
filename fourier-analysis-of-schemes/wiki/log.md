# Directory Update Log

## 2026-10-14

* **Ingested [Arfken, Weber & Harris (2013)](/sources/arfken-2013.md)** (D21), the
  second textbook, through the merge path. Scoped read: preface, contents, ch. 19
  (Fourier series) and ch. 20 (integral transforms, including §20.6, the discrete
  Fourier transform), all exercises and both reading lists. No other chapter was read.
  * **New pages (2).** [Discrete Fourier transform](/definitions/discrete-fourier-transform.md)
    fills the gap the founding ingestion recorded, where the DFT appeared only as Riley's
    exercise 13.10. Arfken's $N^{-1/2}$, $e^{+}$ pair is mapped onto the registry's
    $\hat f^N_m$ ($1/N$, $e^{-}$). The page records aliasing and the FFT.
    [Sawtooth wave](/benchmarks/sawtooth-wave.md) is touched by both sources.
  * **Updated pages (13)** with the second citation and Arfken's extensions:
    [Fourier series](/definitions/fourier-series.md), [Dirichlet conditions](/definitions/dirichlet-conditions.md),
    [Fourier transform](/definitions/fourier-transform.md), [Dirac delta function](/definitions/dirac-delta-function.md),
    [convolution](/definitions/convolution.md), [Laplace transform](/definitions/laplace-transform.md),
    [convergence of Fourier series](/results/fourier-series-convergence.md),
    [Gibbs phenomenon](/results/gibbs-phenomenon.md) (now quantified: $1.1789797\ldots$ times the
    half-jump), [Parseval's theorem](/results/parseval-theorem.md),
    [convolution theorem](/results/convolution-theorem.md),
    [Fourier transform properties](/results/fourier-transform-properties.md) (transform solutions
    of the wave, heat and Poisson equations), [Laplace transform properties](/results/laplace-transform-properties.md),
    [square wave](/benchmarks/square-wave.md). [Riley et al. (2006)](/sources/riley-2006.md) gains two
    "Cited on" audit lines only.
  * **Contradictions: none.** **Qualifications recorded:** Fourier-transform sign (Arfken
    $e^{+\mathrm i\omega t}$ forward, same $1/\sqrt{2\pi}$) and §20.5's non-symmetric pair;
    normalized convolution ($1/\sqrt{2\pi}$ inside); DFT normalization and sign; Laplace
    notation (lowercase transform); Dirichlet conditions (two listed conditions, explicitly
    not necessary); Fourier-transform existence (Dirichlet conditions and decay of the
    transform against Riley's $\int\lvert f\rvert < \infty$); term-by-term differentiation (uniform
    convergence of the series against Riley's continuity and Dirichlet $f'$); division-by-$t$
    rule (a weaker condition); derivative rules (integrability against Riley's printed $s > 0$);
    coefficient decay (a heuristic rule where Riley gives none).
  * **Compiler notes (hypothesis):** Arfken's differentiation condition read literally is not
    sufficient (the series $\sum\sin(m^2x)/m^2$); the printed aliasing interpolant uses the point
    index and the opposite sign; the "otherwise 0" of the real discrete-orthogonality exercise
    holds only for indices up to $N/2$; Riley's exercise 13.10 disagreement for $m \ge N/2$
    is read as aliasing.
  * **Registry extensions** ([notation](/notation.md)): $\xi$ and $\hat f^N_m$ moved from
    reserved to in use, with the DFT inverse written out; added $\varphi(x,t)$, $c_0$, $\nu$,
    $\mathcal G(\mathbf r,\mathbf r_0)$, $\Gamma$ and $\beta$.
  * **Bibliography:** 36 entries (was 1). The source itself was added, and 34 cited works were
    merged with `citedby = {arfken-2013}`: the reading lists of chs. 19 (7) and 20 (18, with
    Jeffreys and Jeffreys shared) and 10 works cited in footnotes and text. Seven article DOIs
    were verified on Crossref (Raisbeek's author is spelled Raisbeck there; Cooley and Tukey's
    title is not printed).

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
