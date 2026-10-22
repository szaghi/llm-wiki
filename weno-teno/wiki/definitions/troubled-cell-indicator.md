---
type: Definition
title: "Troubled-cell and shock indicators"
description: "A troubled-cell (shock, discontinuity) indicator is a cheap local functional of the discrete solution that decides where a high-order scheme must be limited, blended or switched; the page defines the indicators the sources use — modal energy, WENO deviation, undivided-difference, TENO-flag and flattener types — with their parameters and stated limitations."
status: established
aliases: [shock indicator, shock sensor, shock detector, discontinuity indicator, discontinuity sensor, smoothness sensor, flattener, troubled-cell detector]
tags: [limiting, dg, teno, finite-difference, low-dissipation]
timestamp: 2026-10-21T12:00:00Z
---

# Troubled-cell and shock indicators

A **troubled-cell indicator** is a local functional of the discrete solution
that classifies each cell (or interface) as smooth or as containing a
discontinuity, and so decides where a non-oscillatory mechanism acts: a
limiter that overwrites the solution, a blending coefficient toward a
low-order scheme, a switch between a linear and a nonlinear reconstruction,
or the suppression of antidiffusion. The indicator is distinct from the
[smoothness indicators](/definitions/smoothness-indicator.md) $\beta_k$ of
WENO, which grade candidate stencils inside one reconstruction, although
several indicators below are built from them. Indicators output either a
binary flag or a continuous value in $[0,1]$; the sources use both, and
with opposite conventions (1 = troubled in some, 1 = smooth in others),
recorded per indicator below.

## Indicators used in the sources

**Modal-energy indicator (DGSEM, a priori blending).** Hennemann et al.'s
modification of the Persson–Peraire indicator, as used by
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
(§2.4, Eqs. (19)–(22)). Let $\hat m_l$, $l=0,\dots,N$, be the hierarchical
Legendre modal coefficients of an indicator quantity (density, pressure, or
$u$ for a scalar law; page-local). Then
$$\mathbb E=\max\Big(\frac{\hat m_N^2}{\sum_{l=0}^{N}\hat m_l^2},\ \frac{\hat m_{N-1}^2}{\sum_{l=0}^{N-1}\hat m_l^2}\Big),\qquad
\alpha=\frac{1}{1+\exp\big(-\frac{\mathfrak s}{\mathbb T}(\mathbb E-\mathbb T)\big)},\qquad \mathbb T(N)=0.5\cdot10^{-1.8(N+1)^{1/4}},$$
with sharpness $\mathfrak s=9.21024$, chosen so that $\alpha(\mathbb E=0)=10^{-4}$
*(compiler check: $1/(1+e^{9.21024})=1.0\times10^{-4}$)*, and an optional
cap $\alpha=\min(\alpha,\alpha_{\max})$ ($\mathbb E$, $\mathbb T$,
$\mathfrak s$, $\alpha_{\max}$ page-local). $\alpha$ is the DG–FV blending
coefficient of [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md):
1 means troubled. Strengths: it needs only data of the previous step and is
cheap. Weakness: it is heuristic with user parameters. For subcell-wise
blending the authors suggest nodal, feature-based indicators instead.

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

**Undivided-difference sensor (finite differences, Ren–Liu–Zhang type).**
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

**TENO-flag indicators (finite differences).** The binary cut-off flags
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

**Flattener (finite differences, antidiffusion control).**
[Balsara et al. (2024)](/sources/balsara-2024.md) (§III, Eq. (3.8)) multiply
the antidiffusive term of their HLLI Riemann solver by a shock
detector/flattener $\psi_{i+1/2}\in[0,1]$ (Balsara 2012, as recalled), 0 at
shocks and 1 in smooth flow (page-local). For the Baer–Nunziato system no
good flattener exists, so antidiffusion is switched off in its Riemann
problems (§VIII.b).

**Indicators in DG limiting.** [Wu & Shu (2023)](/sources/wu-2023-b.md)
apply a locally divergence-free WENO limiter in cells flagged by the KXRCF
indicator before their bound-preserving limiter (§7);
[Cui, Ding & Wu (2024)](/sources/cui-2024.md) apply the Qiu–Shu WENO limiter
in troubled cells before the
[scaling limiter](/methods/zhang-shu-scaling-limiter.md) (Ex. 3–5). Neither
paper analyses the indicator.

## Positions on indicators

- **Case and parameter dependence.** [Takagi et al. (2022)](/sources/takagi-2022.md)
  state that the sensors of classical hybrid schemes are mostly "case and
  parameter sensitive" (§1, §3.2) and present their detector as
  parameter-free; the three-cell reach of the rule, the THINC steepness and
  the first-order fallback for non-monotone data are nonetheless fixed
  design choices *(compiler remark, not in the sources)*, and
  their own blast-wave refinement shows $C_T$ affects overshoots at contacts
  (§4.5, Fig. 9). Rueda-Ramírez et al. call the modal-energy indicator
  heuristic (§2.4).
- **Avoiding the indicator.** [Peng, Sun & Wu (2024)](/sources/peng-2024.md)
  call troubled-cell limiters "problem-dependent" and liable to alter
  desirable properties of the DG scheme (§1). Their
  [OEDG](/methods/oedg.md) method applies a solution-dependent damping in
  every cell after every stage instead of detecting troubled cells; Kuzmin &
  Vedral likewise evaluate their sensor in every cell.
- **Physical sensors.** Fu (2023) reports the case-dependence of the Ducros
  sensor as a reason for the TENO-based indicator (§3.4), yet records that
  later TENO6-A work replaced the undivided-difference sensor by a modified
  Ducros sensor (§4.1).

# Citations

- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — arXiv v2: §2.4, Eqs. (19)–(22).
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — arXiv v1: §3 (Eqs. (9)–(10)); §5; Rem. 6.
- [Fu (2021)](/sources/fu-2021.md) — arXiv v1: §3.4, Eqs. (17)–(19).
- [Fu (2023)](/sources/fu-2023.md) — §3.4 (Eqs. (21)–(24)); §4.1 (Eqs. (31)–(33)).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §1; §3.1 (Eqs. (18)–(20), Table 1); §3.2; §4.5 (Fig. 9).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §III (Eq. (3.8)); §VIII.b.
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1.
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §7 (KXRCF indicator).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §8, Ex. 3–5 (WENO limiter in troubled cells).
