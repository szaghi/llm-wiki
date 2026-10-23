---
type: Benchmark
title: "Gray–Scott model"
description: "The two-species Gray–Scott reaction–diffusion system on a periodic square, discretized by finite differences, is a stiff two-dimensional benchmark; the page gives the parameter sets of two sources and what they measured with exponential Runge–Kutta and linearly implicit multistep methods."
status: established
aliases: [Gray–Scott reaction–diffusion model, Gray-Scott, 2D Gray–Scott]
tags: [stiff, verification, exponential]
timestamp: 2026-10-19T19:14:00Z
---

# Gray–Scott model

The **Gray–Scott model** couples two chemical species $u$ and $v$ (page-local) through an
autocatalytic reaction, with feed rate $\mathcal F$ and kill rate $\mathcal K$
(page-local) and diffusion coefficients $d_u$, $d_v$:

$$\begin{aligned}
\partial_tu&=d_u\Delta u-uv^2+\mathcal F(1-u),\\
\partial_tv&=d_v\Delta v+uv^2-(\mathcal F+\mathcal K)v.
\end{aligned}$$

In the bundle's sources it is solved in two dimensions with periodic boundary conditions
and second-order finite differences. The discrete Laplacian supplies the stiff linear
part, and the cubic reaction the nonlinearity. That suits integrators that separate a
stiff linear operator from a nonlinear remainder
([exponential integrators](/methods/exponential-integrators.md)), and Jacobian-based
methods with direct solves.

## Variants used

| source | $d_u$, $d_v$ | $\mathcal F$, $\mathcal K$ | domain and grid | time | initial data |
|---|---|---|---|---|---|
| [Luan (2021)](/sources/luan-2021.md), Ex. 6.3 | $0.02$, $0.01$ | $0.065$, $0.035$ | $[0,1.5]^2$, $150\times150$ | $[0,2]$ | $u=1-e^{-150((x-1.5)^2+(y-1.5)^2)}$, $v=e^{-150((x-1.5)^2+2(y-1.5)^2)}$ |
| [Glandon et al. (2022)](/sources/glandon-2022.md), §8.2 | $0.2$, $0.1$ | $0.04$, $0.06$ | $128\times128$ (domain not stated), $2\times128^2$ unknowns | $[0,2]$ | not stated |

Luan writes the feed and kill rates as $\alpha$ and $\beta$, and Glandon et al. write them
as $F$ and $k$, with diffusion coefficients $\varepsilon_1$, $\varepsilon_2$. Both sets are
the sources' own; they differ, so results are not comparable across the two papers.

## What the tests showed

**Exponential Runge–Kutta methods** (Luan 2021, §6, Figs. 6.3–6.4, Table 6.1). Constant
steps, max-norm error at $t=2$ against a small-step expRK4s6 reference. The new
expRK4s6 is much more accurate than Hochbruck–Ostermann's expRK4s5 at equal step counts,
and expRK5s10 slightly more accurate than Luan–Ostermann's expRK5s8. In CPU time expRK4s6
is the most efficient overall, and expRK5s10 overtakes it below an error of $10^{-11}$.
Steps needed to reach a given error:

| error | $10^{-5}$ | $10^{-6}$ | $10^{-7}$ | $10^{-8}$ | $10^{-9}$ | $10^{-10}$ | $10^{-11}$ |
|---|---|---|---|---|---|---|---|
| expRK4s5 | 18 | 36 | 66 | 121 | 215 | 385 | 685 |
| expRK4s6 | 10 | 19 | 28 | 46 | 122 | 230 | 420 |
| expRK5s8 | 7 | 18 | 33 | 57 | 92 | 149 | 238 |
| expRK5s10 | 8 | 17 | 30 | 51 | 82 | 130 | 208 |

The methods are on [exponential integrators](/methods/exponential-integrators.md), and the
theory behind them is at
[stiff order conditions](/results/exponential-runge-kutta-stiff-order-conditions.md).

**Linearly implicit multistep methods** (Glandon et al. 2022, §8.2, Fig. 8.2). Variable
steps, full Jacobian, direct LU factorization reused across solves, tolerances
$10^{-2}$–$10^{-10}$. The five multistep integrators reach similar errors with similar step
counts: Limm, Limm-W, an in-house [BDF](/methods/backward-differentiation-formula.md), and
MATLAB ode15s in BDF and NDF modes. The one-step SDIRK4a and RODAS4 need fewer steps.
ode15s is fastest in CPU time, which the authors attribute to software optimization. Limm
and Limm-W show a "small performance advantage" over the in-house BDF, because they need
one linear solve per step. See
[linearly implicit multistep methods](/methods/linearly-implicit-multistep-method.md).

## Qualifications

- Luan's text says that the new methods "use smaller steps" for the same accuracy and
  therefore "can take larger step sizes". His Table 6.1 shows that they use fewer steps
  (printed slip). His order plot is announced for $N=32,\dots,1024$ steps while the figure
  axis starts at 16.
- Both studies are serial MATLAB runs on one workstation. Glandon et al. compare their
  multistep methods only within their own framework.

# Citations

- [Luan (2021)](/sources/luan-2021.md) — §6, Ex. 6.3, Figs. 6.3–6.4, Table 6.1; arXiv v1.
- [Glandon et al. (2022)](/sources/glandon-2022.md) — §8, §8.2, Eq. (8.2), Fig. 8.2.
