---
type: Definition
title: "Scale sensors and the effective scaled wavenumber"
description: "A scale sensor estimates the local reduced wavenumber of the data, exactly for a sinusoid, so that dissipation, the TENO cut-off or the linear scheme can follow the resolved scale; the page gives the six-point sensors and their phase-independent form, the five-point TENO5-A sensor, a spectral-difference shock detector and a bounded second-derivative sensor."
status: established
aliases: [scale sensor, effective scaled wavenumber, ESW, estimated scaled wavenumber, k_ESW, K_ESW, wavenumber sensor, second-derivative sensor, Li sensor, optimized scale sensor, phase-independent scale sensor, TENO6-SA sensor]
tags: [low-dissipation, teno, finite-difference, limiting]
timestamp: 2026-10-24T05:59:00Z
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
$\mathsf D_p=f^{(p)}(x_0)\Delta x^p$ (Li, Chen & Ren 2022a, Eqs. (18)–(19); Huang, Liang & Fu 2023,
Eqs. (21)–(22)). A dimensionless length scale follows from any pair $p>q$,

$$\delta=\beta_{\mathrm c}\Big|\frac{\mathsf D_q}{\mathsf D_p}\Big|^{1/(p-q)}=\frac{\beta_{\mathrm c}}{\Delta x}\Big|\frac{f^{(q)}}{f^{(p)}}\Big|^{1/(p-q)}$$

(page-local $\delta$ and calibration constant $\beta_{\mathrm c}$; Li, Chen & Ren 2022a, Eq. (20)).
Calibration on $f=A\sin(k_wx+\phi_0)$ selects $p=q+2$, "the simplest" choice with exact scaling,
and $\beta_{\mathrm c}=2\pi$ gives $\delta=\lambda_w/\Delta x$, the number of points per wavelength
$\lambda_w$ (page-local), hence $\vartheta=2\pi/\delta$ (Eqs. (21)–(26)). For a sinusoid

$$\sqrt{\frac{|\mathsf D_3|}{|\mathsf D_1|}}=\sqrt{\frac{|\mathsf D_4|}{|\mathsf D_2|}}=k_w\Delta x=\vartheta ,$$

(Li, Chen & Ren 2022a, Eqs. (27)–(28); Huang, Liang & Fu 2023, Eqs. (24)–(28)). Each ratio alone is
singular where $f'$ or $f''$ vanishes, so both sources combine them,

$$\vartheta_{\mathrm{ESW}}=\sqrt{\frac{|\mathsf D_3|+|\mathsf D_4|}{|\mathsf D_1|+|\mathsf D_2|+\varepsilon_{\mathrm s}}}$$

(page-local regularization $\varepsilon_{\mathrm s}$; Li, Chen & Ren 2022a, Eq. (29); Huang, Liang &
Fu 2023, Eq. (29)). *(Compiler check, not in the sources: for the sinusoid the numerator is
$\vartheta^2$ times the denominator, $\vartheta^3|A|(|\cos|+\vartheta|\sin|)$ against
$\vartheta|A|(|\cos|+\vartheta|\sin|)$, so with $\varepsilon_{\mathrm s}=0$ the combination is
exact at every phase, critical and inflection points included.)* At a discontinuity the higher
differences dominate and the sensor is large: Li, Chen & Ren read a jump as "a high-frequency
component" (§2.2, Fig. 5).

## Six-point sensor at the interface (Li, Chen & Ren 2022a)

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

$$\varepsilon_{\mathrm s}=0.005\,e^{-500\max\left((f_{\max}-f_{\min})-0.001,\ 0\right)}$$

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

## A re-optimized six-point sensor (Li et al. 2023b)

Li, Sun, Zha, Zhu, Ding & Xia (2023b, §3.2, Eqs. (29)–(34)) measure the six-point sensor above against
the exact wavenumber of sinusoids and find it accurate only at low $\vartheta$: within a 0.6 % relative
error (Lele's resolving-efficiency criterion) it reaches "around 41.06 %" of $\pi$, so it
underestimates $\vartheta$, and the dissipation it drives is too small, at medium and large
wavenumbers (Fig. 4a). Li, Chen & Ren (2022a) report the same sensor accurate below $\vartheta=1.5$
(section above); under the 0.6 % criterion the limit is $\vartheta\approx1.29$ *(compiler check, not
in the sources: $0.4106\pi=1.29$)*.

- **A fifth difference does not help.** Adding $|\mathsf D_5|$ to the numerator and $|\mathsf D_3|$ to
  the denominator (Eqs. (29)–(30)) makes the sensor oscillate in $\vartheta$, because its component
  ratios $\sqrt{|\mathsf D_3|/|\mathsf D_1|}$, $\sqrt{|\mathsf D_4|/|\mathsf D_2|}$ and
  $\sqrt{|\mathsf D_5|/|\mathsf D_3|}$, each exact for a sinusoid, disagree on sampled data; the first
  is the most accurate, exact below 1.33 (Eq. (31), Figs. 4b, 5).
- **Re-optimized stencils.** They parametrize $\mathsf D_1$ and $\mathsf D_3$ by their symmetric
  coefficients, keep consistency, and optimize the free ones for the largest $\vartheta$ within the
  0.6 % tolerance (Eq. (32)). The final sensor has the form of $\vartheta_{\mathrm{ESW}}$ with
  $\varepsilon_{\mathrm s}=10^{-8}$ and, on $f_{i-2},\dots,f_{i+3}$ (Eqs. (33)–(34)),

  | | $f_{i-2}$ | $f_{i-1}$ | $f_i$ | $f_{i+1}$ | $f_{i+2}$ | $f_{i+3}$ |
  |---|---|---|---|---|---|---|
  | $\mathsf D_1$ | $0.032$ | $-0.07$ | $-0.95$ | $0.95$ | $0.07$ | $-0.032$ |
  | $\mathsf D_2$ | $0.0483$ | $0.3551$ | $-0.4034$ | $-0.4034$ | $0.3551$ | $0.0483$ |
  | $\mathsf D_3$ | $0.15$ | $-1.75$ | $4.5$ | $-4.5$ | $1.75$ | $-0.15$ |
  | $\mathsf D_4$ | $\tfrac12$ | $-\tfrac32$ | $1$ | $1$ | $-\tfrac32$ | $\tfrac12$ |

  It is reliable up to $\vartheta=2.08$ for amplitudes 5, 0.5 and 0.05, "66.21 % resolving efficiency"
  (Fig. 6) *(compiler check, not in the sources: $2.08/\pi=0.662$)*. On three
  waveform tests it tracks high wavenumbers better than the earlier sensor, with slight oscillations
  (Eqs. (35)–(37), Fig. 7). Extension to non-uniform meshes is deferred.
- **Use.** It drives both the dispersion and the dissipation parameters of the fully discrete ADADF
  flux, with 2.08 as the end of every fit ([MDCD schemes](/methods/mdcd-scheme.md)).

*(Compiler check, not in the sources: the optimized stencils trade formal accuracy for spectral
fidelity. Taylor moments about $x_{i+1/2}$ show $\mathsf D_1=f'\Delta x-\tfrac{29}{600}f'''\Delta x^3+\dots$,
$\mathsf D_2=f''\Delta x^2+\tfrac{2287}{7500}f^{(4)}\Delta x^4+\dots$ and
$\mathsf D_3=f'''\Delta x^3-\tfrac1{40}f^{(5)}\Delta x^5+\dots$; $\mathsf D_4$ is unchanged.)*

## Five-point sensor at the node (Huang, Liang & Fu 2023)

A five-point stencil is too small for the interface version, so Huang, Liang & Fu (2023, §3.1,
Eqs. (30)–(31)) evaluate the four differences at $x_i$ with five-point central formulas,

$$\begin{aligned}
\mathsf D_1&=\tfrac1{12}f_{i-2}-\tfrac23f_{i-1}+\tfrac23f_{i+1}-\tfrac1{12}f_{i+2},\\
\mathsf D_2&=-\tfrac1{12}f_{i-2}+\tfrac43f_{i-1}-\tfrac52f_i+\tfrac43f_{i+1}-\tfrac1{12}f_{i+2},\\
\mathsf D_3&=-\tfrac12f_{i-2}+f_{i-1}-f_{i+1}+\tfrac12f_{i+2},\\
\mathsf D_4&=f_{i-2}-4f_{i-1}+6f_i-4f_{i+1}+f_{i+2},
\end{aligned}$$

with $\varepsilon_{\mathrm s}=10^{-12}$, results being "not sensitive" to it as long as it is small
(no sensitivity study shown). They assert that evaluating at $x_i$ or $x_{i+1/2}$ is "almost
identical" (no test shown). On the same four kinds of test function the sensor tracks the local
wavenumber at critical points and separates discontinuities, where Ren et al.'s discontinuity sensor
used by TENO5-A takes, at critical points, values different from those at other points of the same
wavenumber, and in one case a smaller value at the jump than at some critical points (Fig. 2). The
sensor is unbounded; it drives the TENO cut-off through
$C_T=10^{-\lfloor10-5\tanh(1.01\vartheta_{\mathrm{ESW}})\rfloor}$ from low wavenumbers to discontinuities
(Eq. (33); [adaptive TENO](/methods/adaptive-teno.md)). *(Compiler check, not in the sources: since
$\tanh\in[0,1)$, the exponent's argument lies in $(5,10]$, so $C_T\in\{10^{-10},\dots,10^{-5}\}$.)*

## A bounded second-derivative sensor (Zhou et al. 2023)

Zhou, Ding, Huang & Luo (2023, §4.3, Eqs. (29)–(30)) adapt the dissipation of their WCNS with a sensor that they cite from Li et
al. and that compares two second differences of different width,

$$\theta^{\mathrm L}_i=\frac{|\mathsf S_1-\mathsf S_2|}{|\mathsf S_1+\mathsf S_2|+\epsilon},\qquad \mathsf S_1=|u_{i+1}-2u_i+u_{i-1}|,\quad \mathsf S_2=\tfrac14|u_{i+2}-2u_i+u_{i-2}|,\qquad \theta^{\mathrm L}_{i+1/2}=\max\big(\theta^{\mathrm L}_i,\theta^{\mathrm L}_{i+1}\big)$$

(page-local $\theta^{\mathrm L}$, $\mathsf S_1$, $\mathsf S_2$, not candidate stencils). It lies in $[0,1]$; the authors state that it rises monotonically
from 0 to 1 with wavenumber and is independent of phase for a single sinusoid. *(Compiler check, not in the
sources: for $u=A\cos(k_wx+\phi_0)$ and $\epsilon=0$, $\mathsf S_1=4\sin^2(\vartheta/2)|u_i|$ and $\mathsf S_2=\sin^2\vartheta\,|u_i|$,
so $\theta^{\mathrm L}_i=\sin^2(\vartheta/2)/\big(1+\cos^2(\vartheta/2)\big)$, monotone on $[0,\pi]$ and phase-independent
wherever $u_i\ne0$; at a node with $u_i=0$ both differences vanish and $\theta^{\mathrm L}_i=0$, which the maximum
over two nodes masks at the interface. The thresholds 0.5 and 0.71 used below correspond to
$\vartheta=1.911$ and $\vartheta=2.29$.)* Unlike $\vartheta_{\mathrm{ESW}}$ it is bounded and returns a monotone
function of $\vartheta$, not $\vartheta$ itself. In WCNS-SA it switches the weight constant from
$2\times10^{10}$ to $2\times10^8$ at 0.5 and raises the linear dissipation parameter from 0.0075 above 0.71 as
$\big((\theta^{\mathrm L}-0.71)/0.29\big)^{1.5}$ towards its maximum (Eqs. (31)–(32), Table 3;
[WCNS](/methods/weighted-compact-nonlinear-scheme.md), [MDCD schemes](/methods/mdcd-scheme.md)). Which variable
feeds the sensor in the Euler system is not stated. The authors compare it with energy-ratio automatic
dissipation control, which also relies on a sensor (§4.3).

## Phase-independent six-point sensors (Zhang et al. 2024b)

Zhang, Jiang, Qin, Qu & Yan (2024b, §4) analyse the six-point interface sensors above on a sinusoid
$f=A\sin(k_wx+\phi_0)$, writing them with the two component ratios
$\vartheta_{\mathrm{ESW},1}=\sqrt{|\mathsf D_3|/|\mathsf D_1|}$ and $\vartheta_{\mathrm{ESW},2}=\sqrt{|\mathsf D_4|/|\mathsf D_2|}$
(Eq. (25)). They parametrize the four stencils by their symmetric coefficients under the consistency
constraints (Eqs. (28)–(29); $\mathsf D_4$ is fixed, $(\tfrac12,-\tfrac32,1,1,-\tfrac32,\tfrac12)$), with page-local
free coefficients $b_1$ of $\mathsf D_2$ on $f_i,f_{i+1}$ and $c_1$ of $\mathsf D_3$, and show:

- **$\vartheta_{\mathrm{ESW},2}$ is phase-independent for any $b_1$**,
  $$\vartheta_{\mathrm{ESW},2}=\sqrt{\frac{2(1-\cos\vartheta)}{\lvert(1+2b_1)\cos\vartheta-2b_1\rvert}},$$
  independent of $\phi_0$ and $A$; $b_1=-\tfrac5{12}$ is the Li, Chen & Ren sensor (Eq. (31)), which is
  phase-independent but resolves only up to $\vartheta=1.454$ within a 1 % error (resolving efficiency
  46.279 %, §4.1).
- **Equal component ratios.** The optimized sensor that they attribute to S. Li et al. (J. Sci. Comput., 2022;
  *compiler check, not in the sources: its coefficients are those of the re-optimized sensor of Li et al.
  2023b above*) reaches higher wavenumbers
  but oscillates with phase, because $\vartheta_{\mathrm{ESW},1}\ne\vartheta_{\mathrm{ESW},2}$ on sampled data (Fig. 3).
  Requiring $\vartheta_{\mathrm{ESW},1}=\vartheta_{\mathrm{ESW},2}$ for every sinusoid gives two constraints on the
  $\mathsf D_1$ coefficients, $a_1=\tfrac1{10}(1+2c_1+10b_1c_1)$, $a_2=\tfrac1{20}(1-10b_1-3c_1-10b_1c_1)$
  (page-local $a_1,a_2$; Eq. (32)); the whole sensor then equals the closed form above and depends on $b_1$
  alone, $c_1$ being irrelevant for single waves.
- **New sensor.** With $b_1=-0.398$, $c_1=-5$, $\varepsilon_{\mathrm s}=10^{-5}$ (Eq. (33)):

  | | $f_{i-2}$ | $f_{i-1}$ | $f_i$ | $f_{i+1}$ | $f_{i+2}$ | $f_{i+3}$ |
  |---|---|---|---|---|---|---|
  | $\mathsf D_1$ | $0.0204$ | $-0.004$ | $-1.09$ | $1.09$ | $0.004$ | $-0.0204$ |
  | $\mathsf D_2$ | $0.051$ | $0.347$ | $-0.398$ | $-0.398$ | $0.347$ | $0.051$ |
  | $\mathsf D_3$ | $0.2$ | $-2$ | $5$ | $-5$ | $2$ | $-0.2$ |
  | $\mathsf D_4$ | $\tfrac12$ | $-\tfrac32$ | $1$ | $1$ | $-\tfrac32$ | $\tfrac12$ |

  It resolves up to $\vartheta=2.137$ within 1 % (resolving efficiency 68.012 %, Fig. 4), against 1.454 for
  $b_1=-\tfrac5{12}$. *(Compiler check, not in the sources: on sampled sinusoids with these coefficients the sensor
  is the same at every phase to five digits and equals the closed form, and the 1 % limit is 2.137.)*
- **Against an arccos sensor.** Li & Ren's sensor of $\arccos$ type is exact for sinusoids on $[0,\pi]$ but is capped
  at $\pi$; the new one gives larger values at discontinuities, since all four differences use all six points,
  which Zhang et al. judge better suited to a TENO cut-off (§4.2, Eqs. (34)–(35)).

**Use: TENO6-SA.** The sensor selects, per interface, one of four wavenumber bands of a scale-adaptive sixth-order
TENO (§5.1, Algorithm 1; [adaptive TENO](/methods/adaptive-teno.md)). Below $\vartheta_{\mathrm{ESW}}=1.085$ the
linear scheme is the sixth-order central one and $C_T=10^{-5}$; on $[1.085,1.516)$ a fourth-order scheme of
maximum resolved bandwidth on the same six points, $C_T=10^{-10}$; on $[1.516,1.726)$ a second-order one,
$C_T=10^{-13}$; above 1.726 the second-order scheme with $C_T=10^{-8}$ ("piecewise spectrum optimization"; 1 %
dispersion bandwidths 1.100, 1.530, 1.726, switch points where the dispersion errors of neighbouring schemes are
equal). The linear weights reproduce the band's linear flux, $d=(\tfrac9{20},\tfrac3{10},\tfrac1{20},\tfrac15)$ and
$(\tfrac{21}{50},\tfrac9{50},\tfrac2{25},\tfrac8{25})$ in the TENO6 ordering (central, downwind, upwind, four-point), and
$(\tfrac{5571}{14000},\tfrac{321}{3500},\tfrac{1429}{14000},\tfrac{1429}{3500})$ by constrained least squares for the
second-order flux, which no convex combination of the candidates reproduces. The resulting scheme keeps sixth
order on smooth advection, has an ADR bandwidth of 1.767 against 1.100 for TENO6
([approximate dispersion relation](/definitions/approximate-dispersion-relation.md)), and survives a shock/wavy-wall
interaction on which TENO6-A fails (§5–§6). The $C_T$ falling with wavenumber up to 1.726 is opposite to the trend of
TENO-A; the authors reconcile the two by the relay of linear schemes (§5.1). In the 2-D Riemann problem the sensor
stays below 1.085 in most of the domain and exceeds the top band at shocks and slip lines (§6.3.2, Fig. 22).

## A five-point sensor on spectral-difference traces (Chen & Fu 2024)

Chen & Fu (2024, §5.6, Eqs. (66)–(69)) use the five-point differences of Huang, Liang & Fu with the
amplitude-dependent $\varepsilon_{\mathrm s}$ of Li, Chen & Ren as a **strong-shock detector** in a limiter for the nodal
spectral difference method. At an interface the five inputs are cell-centre values, interface means of the two
traces and a neighbour's trace, spaced $\Delta x/2$, and the cell value is $\vartheta_i=2\min(\vartheta_{i-1/2},\vartheta_{i+1/2})$;
where $\vartheta_i>0.6$ the limited polynomial is compressed towards the cell average,
$\tilde u^{\mathrm{new}}=(1-\theta_{\mathrm c})\bar u_i+\theta_{\mathrm c}\tilde u_h$, with $\theta_{\mathrm c}$ (page-local) the largest factor keeping
the polynomial's range inside the nodal range of the three cells *(compiler check, not in the sources: a
[Zhang–Shu-type scaling](/methods/zhang-shu-scaling-limiter.md))*.
Here the sensor neither sets a dissipation parameter nor a cut-off but switches an extra limiting step
([Hermite WENO](/methods/hermite-weno.md), [troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Not a scale sensor: Jameson-type normalized second differences

The feature sensor of the LLF-M flux of [Wang et al. (2023a)](/sources/wang-2023.md) (§3.2,
Eq. (21)) also uses second differences on three points, but normalizes them by the local level
of the variable, not by another difference:
$\varphi_{\mathrm J,i}[q]=\lvert(q_{i+1}-2q_i+q_{i-1})/(q_{i+1}+2q_i+q_{i-1})\rvert$ for $q=p$ and
$q=\rho$ (page-local, as on the [Ducros sensor](/definitions/ducros-shock-sensor.md) page, where
the full product with the Ducros ratio is given). The authors call the product "non-dimensional
scale-invariant" and tune its use with a problem-dependent constant ([Lax–Friedrichs
flux](/methods/lax-friedrichs-flux.md)). *(Compiler check, not in the sources: for
$q=q_0+A\cos(k_wx+\phi_0)$, $\varphi_{\mathrm J,i}[q]=\sin^2(\vartheta/2)\,\lvert A\cos(k_wx_i+\phi_0)\rvert/\lvert q_0+\cos^2(\vartheta/2)A\cos(k_wx_i+\phi_0)\rvert$.
It depends on the relative amplitude $A/q_0$ and on the phase, so it is not a wavenumber estimate.
Zhou et al.'s $\theta^{\mathrm L}$ above normalizes by a second second difference instead, and
amplitude and phase cancel. $\varphi_{\mathrm J}$ is invariant under $q\mapsto\sigma q$ but not
under $q\mapsto q+\mu$, so "scale-invariant" holds for scalings only.)*

## How the sources relate

The five-point sensor is the six-point one of Li, Chen & Ren, which Huang, Liang & Fu cite (with Sun et al.
and Su et al.) as its origin, moved from the interface to the node and with plain instead of optimized
differences and a constant instead of an amplitude-dependent $\varepsilon_{\mathrm s}$. Both sources
use it to modulate dissipation, not to switch schemes: the MDAD flux maps it to a dissipation
parameter, TENO5-A to a cut-off. Li, Chen & Ren (2022a, §1) claim the sensor and the adaptive-dissipation
strategy as first "according to our knowledge", while citing an earlier scale sensor of Li et al.
(2016) designed for second-derivative schemes (§2.2).

## Qualifications

- On sampled data the finite differences have their own modified wavenumber, so the sensor is exact
  only in the limit of resolved sinusoids; Li, Chen & Ren document the underestimate above
  $\vartheta=1.5$, Huang, Liang & Fu do not analyse it.
- Li, Chen & Ren (2022a, §2.2) write that $\varepsilon_{\mathrm s}$ is below $5\times10^{-5}$ when
  $f_{\max}-f_{\min}\ge0.01$. *(Compiler check, not in the sources: Eq. (33) gives
  $0.005e^{-4.5}=5.55\times10^{-5}$ at 0.01; the bound holds from about 0.0102.)*
- Li et al. (2023b) reprint the sensor of Li, Chen & Ren (2022a) with two slips: the $f_{i-2}$
  coefficient of $\mathsf D_1$ as $-\tfrac1{96}$ and the last term of $\mathsf D_2$ as
  "$-\tfrac1{24}f_{i+1}$", where the table above has $+\tfrac1{96}$ and $\tfrac1{24}f_{i+3}$
  (their Eq. (12)); the same index slip recurs in their Eq. (30). *(Compiler check, not in the sources:
  with the printed values neither stencil annihilates constants; with the values above $\mathsf D_1$ is
  a consistent fourth-order $f'\Delta x$ and $\mathsf D_2$ a consistent $f''\Delta x^2$.)* Their
  constraint relations of Eq. (32) have sign slips: the consistency conditions for the patterns
  $(-a_3,a_2,-a_1,a_1,-a_2,a_3)$ and $(c_3,-c_2,c_1,-c_1,c_2,-c_3)$ give $a_3=(1+3a_2-a_1)/5$,
  $c_3=(c_2-1)/5$ and $c_1=2c_2+1$, which reproduce both their Eq. (30) and Eq. (34), where the printed
  relations reproduce neither *(compiler check, not in the sources)*.
- Zhang et al. (2024b, §4.2) state that $b_1=-\tfrac5{12}$ is the value for which "the right derivative of the local
  $\varphi_{ESW}$ curve at $\varphi=0$ equals 1". *(Compiler check, not in the sources: the closed form expands as
  $\vartheta_{\mathrm{ESW}}=\vartheta\big(1+\vartheta^2[\tfrac{1+2b_1}4-\tfrac1{24}]\big)+O(\vartheta^5)$, so the derivative at 0 is 1
  for every $b_1$; $b_1=-\tfrac5{12}$ is the value that cancels the $\vartheta^3$ term.)* Their Eq. (31) prints the
  $f_i$, $f_{i+1}$ coefficients of $\mathsf D_2$ on the sinusoid as 1 instead of $b_1$ (their Eq. (28) has $b_1$). *(Compiler check,
  not in the sources: the closed form is right only with $b_1$.)* Later sections use 1.732 as the band limit, against 1.726 in Algorithm 1 (§6.1.3, §6.3.2).
- Zhang et al. (2024b, §5.3) state that the sensor adds "an approximate 13% increase in cost" to TENO6, but their
  Table 2 gives TENO6-SA/TENO6 CPU ratios of 1.29–1.31 on all five grids (e.g. 1151.83 s against 890.53 s at
  $N_x=1600$) *(compiler check, not in the sources: ratios of the printed times)*. In the flow tests the increment of
  TENO6-SA over WENO7-Z is 15.31–19.29 % (Table 6).
- Chen & Fu (2024, Eq. (67)) print only four of the five inputs of $\vartheta_{i-1/2}$, and use the exact solution's
  symbol for the cell value in it; the inputs of $\vartheta_{i+1/2}$ are complete.
- Li, Chen & Ren drop the $1/p!$ of the Taylor term in $\mathsf D_p$ (Eq. (19)); the ratios that enter
  the sensor are calibrated on that convention, which Huang, Liang & Fu share.

# Citations

- [Li, Chen & Ren (2022a)](/sources/li-2022.md) — §1; §2.2, Eqs. (18)–(33), Figs. 4–5; §2.3; §3.4; §4.4.
- [Li et al. (2023b)](/sources/li-2023-b.md) — §3.2, Eqs. (11)–(14), (29)–(37), Figs. 4–7; §3.3.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §1; §3.1, Eqs. (21)–(31), Fig. 2; §3.2, Eq. (33).
- [Zhou, Ding, Huang & Luo (2023)](/sources/zhou-2023.md) — §4.3, Eqs. (29)–(32), Table 3.
- [Zhang et al. (2024b)](/sources/zhang-2024-b.md) — §3.2; §4.1–4.2, Eqs. (22)–(35), Figs. 3–4; §5.1, Algorithm 1; §5.3, Table 2; §6.3.2, Fig. 22; Table 6.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §5.6, Eqs. (66)–(69).
- [Wang et al. (2023a)](/sources/wang-2023.md) — §3.2, Eq. (21): Jameson-type normalized second differences in the LLF-M feature sensor.
