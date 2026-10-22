---
type: Definition
title: "Troubled-cell and shock indicators"
description: "A troubled-cell (shock, discontinuity) indicator is a cheap local functional of the discrete solution that decides where a high-order scheme must be limited, blended or switched; the page defines the indicators the sources use — modal energy and decay, KXRCF, WENO deviation, smooth WENO-Z-type, undivided-difference, TENO-flag, physical-sensor and flattener types — with their parameters and stated limitations."
status: established
aliases: [shock indicator, shock sensor, shock detector, discontinuity indicator, discontinuity sensor, smoothness sensor, flattener, troubled-cell detector, KXRCF indicator, Persson–Peraire indicator, Ducros sensor]
tags: [limiting, dg, teno, finite-difference, low-dissipation]
timestamp: 2026-10-22T12:00:00Z
---

# Troubled-cell and shock indicators

A **troubled-cell indicator** is a local functional of the discrete solution
that classifies each cell (or interface) as smooth or as containing a
discontinuity, and so decides where a non-oscillatory mechanism acts: a
limiter that overwrites the solution, a blending coefficient toward a
low-order scheme, a switch between a linear and a nonlinear reconstruction,
the suppression of antidiffusion, the relaxation of limiter bounds, or the
strength of an artificial dissipation. The indicator is distinct from the
[smoothness indicators](/definitions/smoothness-indicator.md) $\beta_k$ of
WENO, which grade candidate stencils inside one reconstruction, although
several indicators below are built from them. Indicators output either a
binary flag or a continuous value in $[0,1]$; the sources use both, and
with opposite conventions (1 = troubled in some, 1 = smooth in others),
recorded per indicator below.

## Modal indicators (DG)

**Modal-energy indicator (DGSEM, a priori blending).** Hennemann et al.'s
modification of the Persson–Peraire indicator, used with the same map and
parameters by [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
(§5, Eqs. (82)–(88)) and
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
(§2.4, Eqs. (19)–(22)). Let $\hat m_l$, $l=0,\dots,N$, be the hierarchical
Legendre modal coefficients of an indicator quantity (page-local). Then
$$\mathbb E=\max\Big(\frac{\hat m_N^2}{\sum_{l=0}^{N}\hat m_l^2},\ \frac{\hat m_{N-1}^2}{\sum_{l=0}^{N-1}\hat m_l^2}\Big),\qquad
\alpha=\frac{1}{1+\exp\big(-\frac{\mathfrak s}{\mathbb T}(\mathbb E-\mathbb T)\big)},\qquad \mathbb T(N)=0.5\cdot10^{-1.8(N+1)^{1/4}},$$
with sharpness $\mathfrak s=9.21024$, chosen so that $\alpha(\mathbb E=0)=10^{-4}$
*(compiler check, not in the sources: $1/(1+e^{9.21024})=1.0\times10^{-4}$)*. The two highest
modes are both used to avoid odd/even effects, and the threshold is
motivated by a $1/N^4$ modal decay (Rueda-Ramírez et al. 2021, §5;
$\mathbb E$, $\mathbb T$, $\mathfrak s$ page-local). $\alpha$ is the DG–FV
blending coefficient of
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md):
1 means troubled. The two sources post-process it differently:

- Rueda-Ramírez et al. (2021) clip it, $\alpha=0$ below $\alpha_{\min}=0.01$
  (for efficiency: pure DG there) and $\alpha=\alpha_{\max}=1$ above
  (strong shocks); relax it in time,
  $\alpha^{(k+1)}=\max\{\alpha^{(k+1)},0.7\,\alpha^{(k)}\}$ over successive
  evaluations; and propagate it in space by two sweeps
  $\alpha=\max\{\alpha,0.7\,\alpha_E\}$ over the neighbours $E$ (Eqs.
  (86)–(88)). It is recomputed before every Runge–Kutta stage. The time
  relaxation is motivated by the observation that a plain modal indicator
  switches on and off with the position of a moving shock relative to the
  element boundaries (§5; stated, not shown). Indicator quantities: $p$
  (magnetic blast, Orszag–Tang) and $\rho p$ (GEM reconnection).
- Rueda-Ramírez et al. (2022) cap it, $\alpha=\min(\alpha,\alpha_{\max})$,
  and suggest nodal, feature-based indicators for subcell-wise blending.

Strengths: it needs only data of the previous step and is cheap. Weakness:
it is heuristic with user parameters (Rueda-Ramírez et al. 2022, §2.4).

**Modal-decay indicator with a sine ramp (bound relaxation).**
[Pazner (2021)](/sources/pazner-2021.md) (§4.4, Eqs. (68)–(70)) uses the
Persson–Peraire form
$$\mathbb S_K=\log_{10}\frac{\lVert u_K-\hat u_K\rVert^2_{L^2}}{\lVert u_K\rVert^2_{L^2}},\qquad
\varepsilon_K=\begin{cases}0,&\mathbb S_K<\mathbb S_0-\Delta_{\mathbb S},\\ \tfrac12-\tfrac12\sin\big(\pi(\mathbb S_K-\mathbb S_0)/(2\Delta_{\mathbb S})\big),&\lvert\mathbb S_K-\mathbb S_0\rvert\le\Delta_{\mathbb S},\\ 1,&\mathbb S_K>\mathbb S_0+\Delta_{\mathbb S},\end{cases}$$
with $\hat u_K\in\mathbb Q^{N-1}$ the element solution with its highest
modal coefficients zeroed, $\mathbb S_0\sim\log_{10}N^{-4}$ and
$\Delta_{\mathbb S}=1$, "effective choices" for $N>1$ ($\mathbb S_K$,
$\varepsilon_K$, $\mathbb S_0$, $\Delta_{\mathbb S}$ page-local; the source
writes $s_K$, $s_0$, $\kappa$). Here $\varepsilon_K=1$ means rough. The
indicator does not switch schemes: it relaxes the local
[convex-limiting](/methods/convex-limiting.md) bounds toward global ones,
$\hat u^{\min}_i=\varepsilon_Ku^{\min}_i+(1-\varepsilon_K)g_{\min}$ (and
likewise for the maximum, $g_{\min}$, $g_{\max}$ the global bounds), so that
smooth extrema are not clipped. With it the subcell IDP scheme converges at
order $N+1$ for $N=3,4,5$ (rates 4.00, 5.00, 5.86 at 64 elements); without
it the rates are about one (§5.1, Table 1); on solid-body rotation
($25^2$ elements, $N=3$) it lowers the $L^1$ error from
$2.6\times10^{-2}$ to $1.9\times10^{-2}$ and restores the range $[0,1]$
from $[0,0.95]$ (§4.4, Fig. 6;
[solid-body rotation](/benchmarks/solid-body-rotation.md)).

**Modal-decay rate for $hp$ decisions.** [Basile et al. (2022)](/sources/basile-2022.md)
(§4.2, Eqs. (36)–(37)) fit $\lvert a^{(q)}\rvert\simeq C\,e^{-\mathfrak d_Kq}$
to the per-degree $L^2$ norms $a^{(q)}$ of the modal coefficients of the
momentum norm, $q=1,\dots,N$ (the mean $q=0$ is excluded because it "can
severely bias the decay rate"), after Mavriplis; $\mathfrak d_K>1$ means
smooth and selects $p$-enrichment, otherwise $h$-refinement ($\mathfrak d_K$
page-local, the source's $\sigma$; $N=1$ cells are always treated as
smooth). The authors state that it is not suited to shocks
and that strong discontinuities need another indicator. They call it a
"smoothness indicator", with larger values smoother, the opposite sense of
WENO's $\beta_k$ ([h- and hp-adaptation](/methods/hp-adaptation.md)).

## Jump and deviation indicators

**KXRCF indicator (finite volumes and DG).** The Krivodonova et al.
indicator measures the jump of the cell polynomial across its inflow
boundary. [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) (§2, Eqs.
(2.25), (2.31)–(2.34)) flag cell $I_i$ as troubled if
$$\aleph_i=\frac{\big\lvert\int_{\partial I_i^-}\big(u_i(x)-u_{n_i}(x)\big)\,ds\big\rvert}{h_i^{(\ell+1)/3}\,\lvert\partial I_i^-\rvert\,\lVert u_i\rVert_\infty}>1,$$
with $\partial I_i^-$ the inflow part of the boundary, $u_{n_i}$ the
neighbour's polynomial across it, $h_i$ the cell size and $\ell=5$ the
degree of the reconstruction ($\aleph_i$, $\ell$ page-local). The authors
replace the original exponent $(\ell+1)/2$ by $(\ell+1)/3$ so that the
indicator "converge[s] to the smooth case twice as fast as the
discontinuous case": $\aleph_i=O(h^{2(\ell+1)/3})$ on smooth data and
$1/O(h^{(\ell+1)/3})$ at a discontinuity (Eqs. (2.32)–(2.33)). The
indicator variable is the density, with the fluid velocity defining
inflow. All values it needs are already computed by the reconstruction, so
it costs no extra reconstruction, unlike earlier HWENO indicators
(Remarks 2–3). It triggers a modification of the first moment in
[moment-based Hermite WENO](/methods/hermite-weno.md); on the smooth tests
it flags no cells (stated, from the observed orders). KXRCF also precedes
the bound-preserving limiter in
[Wu & Shu (2023)](/sources/wu-2023-b.md) (§7).

**WENO-deviation sensor (continuous finite elements).**
[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) (§3, Eqs. (9)–(10)) define
a cellwise factor (page-local $\varsigma_e$; the source writes $\gamma_e$)
$$\varsigma_e=1-\min\Big\{1,\ \Big(\frac{\lVert u_h^e-u_h^{e,*}\rVert_e}{\lVert u_h^e\rVert_e}\Big)^{\mathsf q}\Big\},\qquad
\lVert v\rVert_e=\Big(\sum_{1\le\lvert k\rvert\le N}h_e^{2\lvert k\rvert-d}\int_{K_e}\lvert D^kv\rvert^2dx\Big)^{1/2},$$
where $u_h^e$ is the finite element polynomial of cell $K_e$, $u_h^{e,*}$ a
[Hermite WENO](/methods/hermite-weno.md) reconstruction from the von Neumann
neighbours, $h_e$ the cell diameter, $k$ a multi-index and $\mathsf q\ge1$
an exponent (page-local; $\mathsf q=1$ by default, 3 in a smooth convergence
test, 2 in the analysis). Here $\varsigma_e=1$ means smooth. The seminorm
sums all derivatives of order $1..N$ and generalizes the Jiang–Shu
indicator. If $u_h$ is a polynomial of degree $\le N$ on the stencil, the
deviation vanishes and $\varsigma_e=1$ for any nonlinear weights
(Rem. 6). The factor blends high- and low-order dissipation without
overwriting the solution
([dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md));
the authors mention, without using it, a separate troubled-cell detector to
skip the reconstruction in smooth cells (§5).

## Finite-difference indicators

**Smooth WENO-Z-type discontinuity indicator.**
[Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) (§2.2.4, Appendix B),
after Xu–Shu and with a global term in the style of Zhu–Qiu, use the
six-point stencil $\{x_{i-2},\dots,x_{i+3}\}$ with its quintic interpolant
($k=0$) and the four three-point quadratics ($k=1,\dots,4$), the smoothness
indicators $\beta_k=\sum_{l=1}^{5}\int_{x_i}^{x_{i+1}}\Delta x^{2l-1}(\partial_x^lp_k)^2dx$,
and
$$\hat\tau=\frac14\sum_{k=1}^{4}(\beta_0-\beta_k)^2,\qquad
\mathcal B=\frac14\sum_{k=1}^{4}\frac{\hat\tau}{\beta_k+\epsilon},\qquad
\varphi_{\mathrm D,i+1/2}=\Big(\frac{1}{1+\mathcal B}\Big)^2\in[0,1]$$
($\hat\tau$, $\mathcal B$, $\varphi_{\mathrm D}$ page-local, as on the [level-set](/methods/level-set-method.md) page; $\varphi_{i+1/2}$ on the alternative-WENO page; $\hat\tau$ is not the
registry's $\tau$). The indicator is evaluated on density and on pressure
and the smaller value is kept. By Taylor expansion, $\varphi_{\mathrm D}=1+O(\Delta x^6)$
on smooth data and $\varphi_{\mathrm D}=O(\Delta x^4)$ when the big stencil contains a
discontinuity; the observed $L^1$ order of $1-\varphi_{\mathrm D}$ is 5.98 (Table 3).
$\varphi_{\mathrm D}$ multiplies the high-order central corrections of the
[alternative WENO](/methods/alternative-weno.md) flux and blends a
low-order interface flux with the high-order one,
$\hat f=\hat f^{\mathrm L}+\varphi_{\mathrm D}(\hat f^{\mathrm H}-\hat f^{\mathrm L})$,
near a [level-set](/methods/level-set-method.md) material interface
(Eqs. (6), (15)–(16)). Propositions 2.1–2.3 state what the blending needs to
keep fifth order: $\varphi_{\mathrm D}=1+O(\Delta x^3)$ on the correction terms,
$\varphi_{\mathrm D}=1+O(\Delta x^5)$ on the blended flux together with $\Delta t=O(\Delta x^r)$,
$r\le2$, and $\varphi_{\mathrm D}=1+O(\Delta x^4)$ in the redistribution. Here 1 means
smooth.

**Physical shock sensor (central scheme with artificial dissipation).**
[Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§3, Eq. (36))
switch the low-order dissipation of their
[JST-type scheme](/methods/artificial-viscosity.md) with the product
$$\Xi_i=\underbrace{\tfrac12\Big[1-\tanh\Big(2.5+10\,\frac{\Delta x}{c}\,\nabla\cdot v\Big)\Big]}_{\text{Bhagatwala–Lele}}\cdot
\underbrace{\frac{(\nabla\cdot v)^2}{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}}}_{\text{Ducros}}\cdot
\underbrace{\Big\lvert\frac{p_{i+1}-2p_i+p_{i-1}}{p_{i+1}+2p_i+p_{i-1}}\Big\rvert}_{\text{Jameson}},\qquad\epsilon_{\mathrm D}=10^{-16}$$
($\Xi_i$, $\epsilon_{\mathrm D}$ page-local, the source's $\varphi_j$; 1 means troubled). Each factor
covers a failure of another (§3, §5.1, Fig. 8, on an underexpanded jet):
the Ducros ratio alone is close to unity in smooth irrotational regions;
Jameson's pressure sensor cannot distinguish a shock from a solenoidal
high-vorticity region; the Bhagatwala–Lele factor, off in expansions and
normalised by $\Delta x/c$ to be mesh-size invariant, can over-damp
dilatational motion on under-resolved grids. The product localizes
dissipation on the shocks and Mach disk, with values below 0.02 elsewhere.
In 1D the Ducros factor is inactive, and the Bhagatwala–Lele factor
improves the entropy waves of the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md) by suppressing
spurious activations of the pressure sensor (§4.3); on a reacting 9000 K
shock tube it had to be switched off for robustness (§4.4).

**Undivided-difference sensor (Ren–Liu–Zhang type).**
[Fu (2021)](/sources/fu-2021.md) (§3.4, Eqs. (17)–(19)) and
[Fu (2023)](/sources/fu-2023.md) (§4.1, Eqs. (31)–(32)) use, with
undivided differences $\Delta f_{i\pm1/2}$ of the point values,
$$\sigma_i=\frac{\lvert2\,\Delta f_{i+1/2}\Delta f_{i-1/2}\rvert+\epsilon_\sigma}{(\Delta f_{i+1/2})^2+(\Delta f_{i-1/2})^2+\epsilon_\sigma},\qquad
\sigma_{i+1/2}=\min(\sigma_{i-1},\sigma_i,\sigma_{i+1},\sigma_{i+2}),\qquad
\mu_d=1-\min\Big(1,\frac{\sigma_{i+1/2}}{C_r}\Big),$$
($\sigma_i$, $\epsilon_\sigma$, $C_r$, $\mu_d$ page-local, as on the
[adaptive TENO](/methods/adaptive-teno.md) page), with $\mu_d\approx1$ at
discontinuities. Fu (2021) sets $\epsilon_\sigma=10^{-40}$, $C_r=0.265$ (the
text does not define $\Delta f$ explicitly); Fu (2023) gives
$\epsilon_\sigma=\frac{0.9C_r}{1-0.9C_r}\xi_{\mathrm A}^2$ with
scheme-dependent constants ($\xi_{\mathrm A}$ page-local, not an LGL node).
The sensor drives the adaptive TENO cut-off
$C_T=10^{-\lfloor b_1-b_2(1-\varphi(\mu_d))\rfloor}$,
$\varphi(\mu_d)=(1-\mu_d)^4(1+4\mu_d)$, $b_1=14$, $b_2=6.4$ in Fu (2021)
($b_1$, $b_2$, $\varphi$ page-local), so that $C_T=10^{-7}$ at shocks and
$10^{-14}$ in smooth regions. The design argument:
high-order undivided differences respond to high-wavenumber turbulent
fluctuations and to genuine discontinuities alike, low-order ones separate
them (Fu 2023, §4.1; Fu 2021, §3.4).

**TENO-flag indicators.** The binary cut-off flags
$\delta_k$ of [TENO](/methods/targeted-eno.md) already say which candidate
stencils are crossed by a discontinuity, and two sources build indicators
from them.
- *Hybrid switch* ([Fu (2023)](/sources/fu-2023.md), §3.4, Eqs. (21)–(24),
  recalled from Fu's hybrid TENO). On four candidate stencils, with the
  simplified measure $\gamma_k=1/(\beta_k+\epsilon)^q$, $q=6$, and
  $\chi_k=\gamma_k/\sum_l\gamma_l$: Flag $=0$ (smooth) if $\chi_k>C_T$ for
  all $k$, else 1, with $C_T=5\times10^{-4}$. Where Flag $=0$ the optimal
  linear scheme is used without characteristic decomposition, which makes
  the scheme about four times faster ([hybrid schemes](/methods/hybrid-weno.md)).
  The review calls the indicator "more universal" than physical sensors such
  as Ducros', because it separates non-smooth scales in spectral space.
- *Discontinuity-location detector* ([Takagi et al. (2022)](/sources/takagi-2022.md),
  §3.1, Eqs. (18)–(20)). With the TENO5 flags of the downwind- and
  upwind-side stencils, a cell flag $\zeta_i\in\{2,1,-1,0\}$ is set to 2 if
  both are 0, to 1 if only the downwind-side one is 0, to $-1$ if only the
  upwind-side one is 0, and to 0 otherwise (page-local $\zeta_i$). Cell $i$
  contains a discontinuity iff $\zeta_i=0$, some $\zeta_{i-3..i-1}\in\{1,2\}$
  and some $\zeta_{i+1..i+3}\in\{-1,2\}$. The rule comes from a model
  one-cell step, where the jump cell itself looks smooth to TENO5 (its
  downwind- and upwind-side flags are both 1) while its neighbours do not
  (Table 1). It adds no parameter
  beyond TENO5's ($q=6$, $C_T=10^{-5}$) and triggers the
  [THINC](/methods/thinc-reconstruction.md) flux in
  [TENO-THINC](/methods/teno-thinc.md).

**Flattener (antidiffusion control).**
[Balsara et al. (2024)](/sources/balsara-2024.md) (§III, Eq. (3.8)) multiply
the antidiffusive term of their HLLI Riemann solver by a shock
detector/flattener $\psi_{i+1/2}\in[0,1]$ (Balsara 2012, as recalled), 0 at
shocks and 1 in smooth flow (page-local). For the Baer–Nunziato system no
good flattener exists, so antidiffusion is switched off in its Riemann
problems (§VIII.b).

## Indicators that only select cells

Several sources use an indicator without defining or analysing it:
- [Wu & Shu (2023)](/sources/wu-2023-b.md) apply a locally divergence-free
  WENO limiter in KXRCF-flagged cells before their bound-preserving limiter
  (§7); [Cui, Ding & Wu (2024)](/sources/cui-2024.md) apply the Qiu–Shu WENO
  limiter in troubled cells before the
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md) (Ex. 3–5).
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) take the indicator of
  their hybrid HWENO predecessor (Zhao, Chen & Qiu 2020, as recalled; not
  given in the paper) to decide where the nonlinear HWENO reconstruction and
  the first-moment limiter act, and report the flagged fractions: from
  0.97% (Leblanc, $\mathrm{Re}=1000$) to 19.57% (double rarefaction, Euler),
  with CPU savings of 59–90% over the non-hybrid scheme (§4, Table 4.2).
  Fewer flagged cells at $\mathrm{Re}=1000$ than at $\mathrm{Re}=\infty$
  give slightly sharper fronts, which they read as evidence that the
  first-moment limiter acts as an
  [artificial viscosity](/methods/artificial-viscosity.md) (Ex. 4.2, §5).

## Positions on indicators

- **Case and parameter dependence.** [Takagi et al. (2022)](/sources/takagi-2022.md)
  state that the sensors of classical hybrid schemes are mostly "case and
  parameter sensitive" (§1, §3.2) and present their detector as
  parameter-free; the three-cell reach of the rule, the THINC steepness and
  the first-order fallback for non-monotone data are nonetheless fixed
  design choices *(compiler remark, not in the sources)*, and
  their own blast-wave refinement shows $C_T$ affects overshoots at contacts
  (§4.5, Fig. 9). Rueda-Ramírez et al. (2022) call the modal-energy
  indicator heuristic (§2.4).
- **Physical sensors.** Fu (2023) reports the case-dependence of the Ducros
  sensor as a reason for the TENO-based indicator (§3.4), yet records that
  later TENO6-A work replaced the undivided-difference sensor by a modified
  Ducros sensor (§4.1). [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)
  agree that the Ducros ratio alone activates spuriously in irrotational
  flow, note that tuning its $\epsilon$ to the flow scales costs
  generality, and repair it by multiplication with two other factors
  instead (§3, §5.1).
- **Avoiding the indicator.** [Peng, Sun & Wu (2024)](/sources/peng-2024.md)
  call troubled-cell limiters "problem-dependent" and liable to alter
  desirable properties of the DG scheme (§1). Their
  [OEDG](/methods/oedg.md) method applies a solution-dependent damping in
  every cell after every stage instead of detecting troubled cells; Kuzmin &
  Vedral likewise evaluate their sensor in every cell.
  [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) fit
  discontinuities with the mesh and need no indicator, limiter or
  artificial viscosity (§I, §V;
  [implicit shock tracking](/methods/implicit-shock-tracking.md)).
- **Indicators as bound relaxation, not switches.** Pazner's use of the
  modal indicator to interpolate between local and global bounds (above)
  weakens a guarantee instead of triggering a stabilization: in smooth
  cells only the global bounds hold. Among the sources ingested so far it
  is the only use of this kind *(compiler remark, not in the sources)*.

## Qualifications

- Zheng, Shu & Qiu's estimates $\varphi_{\mathrm D}=1+O(\Delta x^6)$ assume that the
  $\beta_k$ dominate $\epsilon$ and that the first derivative does not vanish
  at $x_{i+1/2}$ (Appendix B); the paper does not discuss the critical-point
  case, where the $\beta_k$ of the small stencils drop to $O(\Delta x^4)$
  *(compiler remark, not in the sources; see [critical-point accuracy](/properties/critical-point-accuracy.md))*.
  The value of $\epsilon$ in the indicator is not printed.
- Li, Shu & Qiu's derivation of the KXRCF scaling (Eqs. (2.32)–(2.33)) is
  written with a boundary measure $\lvert\partial I_i^-\rvert\sim h$; in 1D
  the inflow boundary is a point *(compiler remark, not in the sources)*.
- Pazner's "expected asymptotic rates for all cases except $N=1$" (§5.1) is
  not what Table 1 prints for $N=2$ (rates 1.18, 1.36, 1.82 with the
  indicator): only $N\ge3$ reach $N+1$, whereas §4.4 calls the indicator
  parameters effective for $N>1$ *(compiler check, not in the sources: comparison of the printed table with the text)*.

# Citations

- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — arXiv v1: §5 (Eqs. (82)–(88)).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.4, Eqs. (19)–(22).
- [Pazner (2021)](/sources/pazner-2021.md) — arXiv v1: §4.4 (Eqs. (68)–(70), Figs. 5–6); §5.1 (Table 1).
- [Basile et al. (2022)](/sources/basile-2022.md) — author manuscript: §4.2 (Eqs. (36)–(37)).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — arXiv v1: §2 (Eqs. (2.25), (2.31)–(2.34), Remarks 2–3); §3.
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §3 (Eqs. (9)–(10)); §5; Rem. 6.
- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §2.2.4 (indicator, Props. 2.1–2.3); Eqs. (6), (15)–(16); Appendix B; Table 3.
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — arXiv v1: §3 (Eq. (36)); §4.3–§4.4; §5.1 (Fig. 8).
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: §3.4, Eqs. (17)–(19).
- [Fu (2023)](/sources/fu-2023.md) — §3.4 (Eqs. (21)–(24)); §4.1 (Eqs. (31)–(33)).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §3.1 (Eqs. (18)–(20), Table 1); §3.2; §4.5 (Fig. 9).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §III (Eq. (3.8)); §VIII.b.
- [Fan, Zhang & Qiu (2021)](/sources/fan-2021.md) — §4 (Ex. 4.2–4.7, Table 4.2); §5.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1.
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — author manuscript: §I, §V.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §7 (KXRCF indicator).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §8, Ex. 3–5 (WENO limiter in troubled cells).
