---
type: Definition
title: "Scale sensors and the effective scaled wavenumber"
description: "A scale sensor estimates the local reduced wavenumber of the data from ratios of Taylor-term magnitudes, exactly for a sinusoid at every phase, so that numerical dissipation or the TENO cut-off can follow the resolved length scale; the page gives the six-point MDAD sensor of Li, Chen and Ren and the five-point TENO5-A sensor of Huang, Liang and Fu."
status: established
aliases: [scale sensor, effective scaled wavenumber, ESW, estimated scaled wavenumber, k_ESW, K_ESW, wavenumber sensor]
tags: [low-dissipation, teno, finite-difference, limiting]
timestamp: 2026-10-23T10:00:00Z
---

# Scale sensors and the effective scaled wavenumber

A **scale sensor** returns, at a grid point or interface, an estimate of the local reduced wavenumber
$\vartheta=k_w\Delta x$ of the data, as opposed to a discontinuity sensor, which only decides whether a
stencil is smooth ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)). In the
bundle the estimate is the **effective (or estimated) scaled wavenumber**, written here
$\vartheta_{\mathrm{ESW}}$ (page-local; Li, Chen & Ren's $k_{ESW}$, Huang, Liang & Fu's $K_{ESW}$). Its
two uses are a locally adaptive dissipation parameter of a linear scheme
([MDCD schemes](/methods/mdcd-scheme.md)) and a locally adaptive TENO cut-off
([adaptive TENO](/methods/adaptive-teno.md)).

## Construction

Write the Taylor expansion of the data about $x_0$ and let $\mathsf D_p$ (page-local) denote the
magnitude of its order-$p$ contribution without the factorial,
$\mathsf D_p=f^{(p)}(x_0)\Delta x^p$ (Li, Chen & Ren 2022, Eqs. (18)–(19); Huang, Liang & Fu 2023,
Eqs. (21)–(22)). A dimensionless length scale follows from any pair $p>q$,

$$\delta=\beta_{\mathrm c}\Big|\frac{\mathsf D_q}{\mathsf D_p}\Big|^{1/(p-q)}=\frac{\beta_{\mathrm c}}{\Delta x}\Big|\frac{f^{(q)}}{f^{(p)}}\Big|^{1/(p-q)}$$

(page-local $\delta$ and calibration constant $\beta_{\mathrm c}$; Li, Chen & Ren 2022, Eq. (20)).
Calibration on $f=A\sin(k_wx+\phi_0)$ selects $p=q+2$, "the simplest" choice with exact scaling,
and $\beta_{\mathrm c}=2\pi$ gives $\delta=\lambda_w/\Delta x$, the number of points per wavelength
$\lambda_w$ (page-local), hence $\vartheta=2\pi/\delta$ (Eqs. (21)–(26)). For a sinusoid

$$\sqrt{\frac{|\mathsf D_3|}{|\mathsf D_1|}}=\sqrt{\frac{|\mathsf D_4|}{|\mathsf D_2|}}=k_w\Delta x=\vartheta ,$$

(Li, Chen & Ren 2022, Eqs. (27)–(28); Huang, Liang & Fu 2023, Eqs. (24)–(28)). Each ratio alone is
singular where $f'$ or $f''$ vanishes, so both sources combine them,

$$\vartheta_{\mathrm{ESW}}=\sqrt{\frac{|\mathsf D_3|+|\mathsf D_4|}{|\mathsf D_1|+|\mathsf D_2|+\epsilon_{\mathrm s}}}$$

(page-local regularization $\epsilon_{\mathrm s}$; Li, Chen & Ren 2022, Eq. (29); Huang, Liang &
Fu 2023, Eq. (29)). *(Compiler check, not in the sources: for the sinusoid the numerator is
$\vartheta^2$ times the denominator, $\vartheta^3|A|(|\cos|+\vartheta|\sin|)$ against
$\vartheta|A|(|\cos|+\vartheta|\sin|)$, so with $\epsilon_{\mathrm s}=0$ the combination is
exact at every phase, critical and inflection points included.)* At a discontinuity the higher
differences dominate and the sensor is large: Li, Chen & Ren read a jump as "a high-frequency
component" (§2.2, Fig. 5).

## Six-point sensor at the interface (Li, Chen & Ren 2022)

The [MDAD scheme](/methods/mdcd-scheme.md) evaluates the sensor at $x_{i+1/2}$ on its six-point
stencil $\{i-2,\dots,i+3\}$. The highest-order differences are "not the best"; optimized six-point
formulas are used instead (Eq. (30); optimization procedure not given), with coefficients on
$f_{i-2},\dots,f_{i+3}$

| | $f_{i-2}$ | $f_{i-1}$ | $f_i$ | $f_{i+1}$ | $f_{i+2}$ | $f_{i+3}$ |
|---|---|---|---|---|---|---|
| $\mathsf D_1$ | $\tfrac1{96}$ | $-\tfrac1{96}$ | $-\tfrac{49}{48}$ | $\tfrac{49}{48}$ | $\tfrac1{96}$ | $-\tfrac1{96}$ |
| $\mathsf D_2$ | $\tfrac1{24}$ | $\tfrac38$ | $-\tfrac5{12}$ | $-\tfrac5{12}$ | $\tfrac38$ | $\tfrac1{24}$ |
| $\mathsf D_3$ | $\tfrac18$ | $-\tfrac{13}8$ | $\tfrac{17}4$ | $-\tfrac{17}4$ | $\tfrac{13}8$ | $-\tfrac18$ |
| $\mathsf D_4$ | $\tfrac12$ | $-\tfrac32$ | $1$ | $1$ | $-\tfrac32$ | $\tfrac12$ |

Adding $|\mathsf D_5|$ "cannot give the ideal result", because the fifth difference is unique on six
points and leaves nothing to optimize (Eq. (32)). The regularization depends on the stencil
amplitude,

$$\epsilon_{\mathrm s}=0.005\,e^{-500\max\left((f_{\max}-f_{\min})-0.001,\ 0\right)}$$

(Eq. (33); $f_{\max}$, $f_{\min}$ the non-dimensional stencil extremes): for
$f_{\max}-f_{\min}\le0.001$ the sensor stays below 1 at all wavenumbers, above 0.01 it is practically
unaffected. The sensor is accurate for $\vartheta<1.5$, underestimates above, but stays monotone in
$\vartheta$, with maximum $\vartheta_{\max}=2.45$ (§2.2–2.3, Fig. 4). Static tests on 192 points
(single sine, two sines with a jump, a damped growing sine, a chirp $\sin(2\pi e^{x+1}x)$) identify
the wavenumbers and treat critical and inflection points smoothly (Fig. 5). In the Euler
implementation the sensor is computed from the density, with inputs normalized by
$\max(|f_{\max}|,1)$; in the Taylor–Green vortex from the split characteristic fluxes (§3.4, §4.4).
The authors state that the calibration targets dissipation control only and that other uses need
further study.

## Five-point sensor at the node (Huang, Liang & Fu 2023)

A five-point stencil is too small for the interface version, so Huang, Liang & Fu (2023, §3.1,
Eqs. (30)–(31)) evaluate the four differences at $x_i$ with five-point central formulas,

$$\begin{aligned}
\mathsf D_1&=\tfrac1{12}f_{i-2}-\tfrac23f_{i-1}+\tfrac23f_{i+1}-\tfrac1{12}f_{i+2},\\
\mathsf D_2&=-\tfrac1{12}f_{i-2}+\tfrac43f_{i-1}-\tfrac52f_i+\tfrac43f_{i+1}-\tfrac1{12}f_{i+2},\\
\mathsf D_3&=-\tfrac12f_{i-2}+f_{i-1}-f_{i+1}+\tfrac12f_{i+2},\\
\mathsf D_4&=f_{i-2}-4f_{i-1}+6f_i-4f_{i+1}+f_{i+2},
\end{aligned}$$

with $\epsilon_{\mathrm s}=10^{-12}$, results being "not sensitive" to it as long as it is small
(no sensitivity study shown). They assert that evaluating at $x_i$ or $x_{i+1/2}$ is "almost
identical" (no test shown). On the same four kinds of test function the sensor tracks the local
wavenumber at critical points and separates discontinuities, where Ren et al.'s discontinuity sensor
used by TENO5-A takes, at critical points, values different from those at other points of the same
wavenumber, and in one case a smaller value at the jump than at some critical points (Fig. 2). The
sensor is unbounded; it drives the TENO cut-off through
$C_T=10^{-\lfloor10-5\tanh(1.01\vartheta_{\mathrm{ESW}})\rfloor}$ from low wavenumbers to discontinuities
(Eq. (33); [adaptive TENO](/methods/adaptive-teno.md)). *(Compiler check, not in the sources: since
$\tanh\in[0,1)$, the exponent's argument lies in $(5,10]$, so $C_T\in\{10^{-10},\dots,10^{-5}\}$.)*

## How the two sources relate

The five-point sensor is the six-point one of Li, Chen & Ren, which Huang et al. cite (with Sun et al.
and Su et al.) as its origin, moved from the interface to the node and with plain instead of optimized
differences and a constant instead of an amplitude-dependent $\epsilon_{\mathrm s}$. Both sources
use it to modulate dissipation, not to switch schemes: the MDAD flux maps it to a dissipation
parameter, TENO5-A to a cut-off. Li, Chen & Ren (2022, §1) claim the sensor and the adaptive-dissipation
strategy as first "according to our knowledge", while citing an earlier scale sensor of Li et al.
(2016) designed for second-derivative schemes (§2.2).

## Qualifications

- On sampled data the finite differences have their own modified wavenumber, so the sensor is exact
  only in the limit of resolved sinusoids; Li, Chen & Ren document the underestimate above
  $\vartheta=1.5$, Huang et al. do not analyse it.
- Li, Chen & Ren (2022, §2.2) write that $\epsilon_{\mathrm s}$ is below $5\times10^{-5}$ when
  $f_{\max}-f_{\min}\ge0.01$. *(Compiler check, not in the sources: Eq. (33) gives
  $0.005e^{-4.5}=5.55\times10^{-5}$ at 0.01; the bound holds from about 0.0102.)*
- Li, Chen & Ren drop the $1/p!$ of the Taylor term in $\mathsf D_p$ (Eq. (19)); the ratios that enter
  the sensor are calibrated on that convention, which Huang et al. share.

# Citations

- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §1; §2.2, Eqs. (18)–(33), Figs. 4–5; §2.3; §3.4; §4.4.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §1; §3.1, Eqs. (21)–(31), Fig. 2; §3.2, Eq. (33).
