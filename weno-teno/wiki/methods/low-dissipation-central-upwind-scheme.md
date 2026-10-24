---
type: Method
title: "Low-dissipation central-upwind schemes"
description: "The low-dissipation central-upwind (LDCU) flux adds to the central-upwind flux an anti-diffusion built from the HLL intermediate state; Chu et al. (2025a) make it adaptive by switching a characteristic-wise SBM slope limiter with a roughness indicator, and Chu et al. (2025c) move the subcell jump with the contact to remove spurious oscillations."
status: established
aliases: [LDCU scheme, LDCU flux, adaptive LDCU scheme, new LDCU scheme, A-MM scheme, A-WLR scheme, Kurganov–Xin flux]
tags: [central-scheme, numerical-flux, finite-volume, low-dissipation, limiting, characteristic]
timestamp: 2026-10-23T20:05:00Z
---

# Low-dissipation central-upwind schemes

A **low-dissipation central-upwind (LDCU)** scheme is a semi-discrete finite-volume scheme whose
numerical flux is the [central-upwind](/methods/central-upwind-scheme.md) flux plus a built-in
**anti-diffusion** term that subtracts part of the central-upwind numerical diffusion where the
reconstructed states allow it. Like every central-upwind flux it needs only the one-sided local
speeds $a^\pm_{i+1/2}$ and no Riemann solver. The flux is due to Kurganov and Xin (2023), as
recalled by [Chu et al. (2025a)](/sources/chu-2025.md) (§2.1), who build on it the **adaptive
LDCU schemes**: second-order LDCU schemes whose piecewise-linear reconstruction switches,
cell by cell, between an overcompressive and a dissipative slope limiter, driven by a roughness
indicator. The adaptive schemes are named A-MM and A-WLR after the indicator they use (§4).

## The LDCU flux

For $\frac{d}{dt}\bar u_i=-\frac1{\Delta x}\big(\hat f_{i+1/2}-\hat f_{i-1/2}\big)$ (Chu et al.
(2025a), Eq. (2.1)) the LDCU flux, as recalled in §2.1 (unnumbered), is

$$\hat f_{i+1/2}=\frac{a^+_{i+1/2}f(u^-_{i+1/2})-a^-_{i+1/2}f(u^+_{i+1/2})}{a^+_{i+1/2}-a^-_{i+1/2}}+\frac{a^+_{i+1/2}a^-_{i+1/2}}{a^+_{i+1/2}-a^-_{i+1/2}}\big(u^+_{i+1/2}-u^-_{i+1/2}\big)+\Phi^{\mathrm{ad}}_{i+1/2},$$

with the one-sided speeds of the central-upwind flux,
$a^+_{i+1/2}=\max\{\lambda_m(A(u^+_{i+1/2})),\lambda_m(A(u^-_{i+1/2})),0\}$ and
$a^-_{i+1/2}=\min\{\lambda_1(A(u^+_{i+1/2})),\lambda_1(A(u^-_{i+1/2})),0\}$, and the anti-diffusion
$\Phi^{\mathrm{ad}}_{i+1/2}$ (page-local). The first two terms are the central-upwind flux of
Kurganov, Noelle and Petrova written out on [central-upwind schemes](/methods/central-upwind-scheme.md).
For the one-dimensional Euler equations the anti-diffusion derived by Kurganov and Xin is, as
quoted by Chu et al. (2025a) (§2.1),

$$\Phi^{\mathrm{ad}}_{i+1/2}=\mathrm{minmod}\Big(-a^-_{i+1/2}\big(\rho^{\mathrm{HLL}}_{i+1/2}-\rho^-_{i+1/2}\big),\ a^+_{i+1/2}\big(\rho^+_{i+1/2}-\rho^{\mathrm{HLL}}_{i+1/2}\big)\Big)\begin{pmatrix}1\\ v^{\mathrm{HLL}}_{i+1/2}\\ \tfrac12\big(v^{\mathrm{HLL}}_{i+1/2}\big)^2\end{pmatrix},$$

where $\rho^{\mathrm{HLL}}$ and $(\rho v)^{\mathrm{HLL}}$ are the first two components of the HLL
intermediate state

$$u^{\mathrm{HLL}}_{i+1/2}=\frac{a^+_{i+1/2}u^+_{i+1/2}-a^-_{i+1/2}u^-_{i+1/2}-\big[f(u^+_{i+1/2})-f(u^-_{i+1/2})\big]}{a^+_{i+1/2}-a^-_{i+1/2}},$$

$v^{\mathrm{HLL}}=(\rho v)^{\mathrm{HLL}}/\rho^{\mathrm{HLL}}$, and
$\mathrm{minmod}(z_1,z_2,\dots)$ is $\min_jz_j$ if all $z_j>0$, $\max_jz_j$ if all $z_j<0$ and $0$
otherwise. The anti-diffusion is a density jump between the HLL state and one of the
reconstructed states, scaled by the corresponding one-sided speed and carried by the vector
$(1,v,v^2/2)$, the conserved-variable jump of a contact. In two dimensions the same flux is
applied in each direction, with speeds and anti-diffusion terms per direction; Chu et al. (2025a) do not
print the two-dimensional anti-diffusion and refer to Kurganov and Xin (§3, Eq. (3.1)).

*(compiler check, not in the sources: the minmod vanishes unless the two density differences have
the same sign, so the anti-diffusion is switched off whenever $\rho^{\mathrm{HLL}}$ does not lie
between $\rho^-$ and $\rho^+$.)* The same HLL intermediate state, under a componentwise minmod,
enters the anti-diffusion of the
[adaptive-diffusion central-upwind Rankine–Hugoniot flux](/methods/adaptive-diffusion-central-upwind-flux.md)
of [Wang et al. (2023b)](/sources/wang-2023-b.md) (Eq. (5)); the LDCU term instead acts only
through the density jump and the contact vector. The other route to lower central-upwind
dissipation, field-wise diffusion coefficients, is the
[LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md), which Chu et al. (2025a)
cite (§1).

## The new LDCU scheme: a jump that moves with the contact

[Chu et al. (2025c)](/sources/chu-2025-c.md) (arXiv v1; "Part II" of the Kurganov–Xin LDCU schemes) state that the LDCU schemes resolve contacts and 2D wave interactions much more sharply
than the central-upwind schemes but "sometimes produce more oscillatory results", especially
near the boundaries of the domain (Abstract, §1). Their fix is in the projection step of the
fully discrete derivation. There the solution in the Riemann fan
$[x_{i+1/2}+a^-_{i+1/2}\Delta t,\ x_{i+1/2}+a^+_{i+1/2}\Delta t]$ is replaced by two constant states
$u^{\mathrm{int},\mathrm L}$, $u^{\mathrm{int},\mathrm R}$ (page-local) whose jump the original LDCU
scheme places at $x_{i+1/2}$, with conservation
$a^+u^{\mathrm{int},\mathrm R}-a^-u^{\mathrm{int},\mathrm L}=(a^+-a^-)\bar u^{\mathrm{int}}$ for the fan
average $\bar u^{\mathrm{int}}$ (Eqs. (2.2)–(2.3)). The new scheme moves the jump to
$x_{i+1/2}+\tilde v\,\Delta t$, $\tilde v\in(a^-,a^+)$ an extra degree of freedom (page-local), so
that conservation reads
$(a^+-\tilde v)u^{\mathrm{int},\mathrm R}+(\tilde v-a^-)u^{\mathrm{int},\mathrm L}=(a^+-a^-)\bar u^{\mathrm{int}}$,
which reduces to the old one for $\tilde v=0$ (§2.1, Eqs. (2.4)–(2.5)). For the Euler equations,
continuity of velocity and pressure across the jump gives a velocity constant across the fan,
and the authors set $\tilde v$ to that velocity, so the jump travels with the contact; the
density jump is the largest one creating no new extrema, a minmod of the two weighted density
differences (§2.2, Eqs. (2.6)–(2.10)).

The semi-discrete limit (Eqs. (2.13)–(2.16)) is again the central-upwind flux plus an
anti-diffusion, now

$$\Phi^{\mathrm{ad}}_{i+1/2}=\alpha^*\,\mathrm{minmod}\Big(\big(v^{\mathrm{HLL}}-a^-\big)\big(\rho^{\mathrm{HLL}}-\rho^-\big),\ \big(a^+-v^{\mathrm{HLL}}\big)\big(\rho^+-\rho^{\mathrm{HLL}}\big)\Big)\begin{pmatrix}1\\ v^{\mathrm{HLL}}\\ \tfrac12\big(v^{\mathrm{HLL}}\big)^2\end{pmatrix},\qquad
\alpha^*=\begin{cases}\dfrac{a^+}{a^+-v^{\mathrm{HLL}}},& v^{\mathrm{HLL}}<0,\\ \dfrac{a^-}{a^--v^{\mathrm{HLL}}},&\text{otherwise,}\end{cases}$$

all at $x_{i+1/2}$, with the HLL intermediate state above, which the paper builds without naming
it (page-local $\alpha^*$). The density differences are weighted by $v^{\mathrm{HLL}}-a^-$ and
$a^+-v^{\mathrm{HLL}}$ instead of $-a^-$ and $a^+$, and the switch $\alpha^*$ depends on the sign of
$v^{\mathrm{HLL}}$. *(compiler check, not in the sources: for $v^{\mathrm{HLL}}=0$, $\alpha^*=1$ and the
term is the Kurganov–Xin anti-diffusion of the previous section, consistent with the reduction of
the conservation condition at $\tilde v=0$.)* If $a^+<\varepsilon_{\mathrm d}$ and
$a^->-\varepsilon_{\mathrm d}$ the flux is replaced by the central average
$\tfrac12\big(f(u^-)+f(u^+)\big)$, $\varepsilon_{\mathrm d}=10^{-12}$ (page-local; Remark 2.1). In 2D
the scheme is derived dimension by dimension on 1D restrictions, with anti-diffusion on the
density, on the transverse momentum and an energy term combining both,
$\alpha^*\big(q^\rho,\ v_1^{\mathrm{HLL}}q^\rho,\ q^{\rho v_2},\ q^E\big)$ for the $x$-flux (page-local
$q$; §2.3); the 2D fully discrete scheme is not printed.

**Evidence** (§3; second order, generalized minmod with factor 1.3, SSP-RK3 at CFL 0.475,
$\gamma=1.4$; visual only, no accuracy test, no theorem). Against the original LDCU scheme the new
one removes the oscillations near the left boundary in a shock–entropy problem ($\Delta x=1/80$,
$t=5$); is non-oscillatory on a stationary contact with a travelling shock and rarefaction where
the original scheme has small oscillations "whose magnitude does not decay when the mesh is
refined" ($\Delta x=1/200$ and $1/8000$;
[stationary contact preservation](/properties/stationary-contact-preservation.md)); and is
substantially less oscillatory on 2D Riemann configuration 3 ($\Delta x=0.001$, $t=1$). On the
Liska–Wendroff explosion the original scheme oscillates along the free boundaries and keeps
"slightly better resolution", and on the implosion the new one is slightly less oscillatory and
its jet travels further ([explosion and implosion](/benchmarks/explosion-and-implosion-problems.md)).
The authors summarize the new schemes as containing "almost the same small amount of numerical
dissipation" as the original ones (§1).

This variant is distinct from the adaptive LDCU schemes of Chu et al. (2025a): it changes the
anti-diffusion term and keeps a fixed limiter, whereas the adaptive schemes keep the
Kurganov–Xin anti-diffusion and switch the limiter.

## Reconstruction in local characteristic variables

Chu et al. (2025a) reconstruct piecewise linearly in **local characteristic variables** (§2.1,
Eqs. (2.4)–(2.5); App. A for 2D), following Chertock et al. With $R=R_{i+1/2}$ and $L=R^{-1}$
the eigenvector matrices of $A\big((\bar u_i+\bar u_{i+1})/2\big)$, the Jacobian at the
arithmetic mean of the two neighbouring cell averages (not a Roe average), and the local
characteristic variables $\bar\zeta_k=L\,\bar u_k$, $k=i-1,\dots,i+2$, the limited slopes of cells
$i$ and $i+1$ are computed field by field, the one-sided values
$\zeta^-_{i+1/2}=\bar\zeta_i+\tfrac{\Delta x}2(\zeta_x)_i$ and
$\zeta^+_{i+1/2}=\bar\zeta_{i+1}-\tfrac{\Delta x}2(\zeta_x)_{i+1}$ are formed, and
$u^\pm_{i+1/2}=R\,\zeta^\pm_{i+1/2}$. The purpose stated is to reduce the oscillations that
either limiter below can produce near shocks and contacts (§1, §2.1.1). See
[characteristic decomposition](/methods/characteristic-decomposition.md).

## The SBM limiter and its two settings

The slopes are limited by the two-parameter SBM limiter of Lie and Noelle, as recalled by Chu et
al. (2025a) (§2.1.1, Eq. (2.6)). In the slope-ratio convention of
[TVD and slope limiters](/definitions/total-variation-diminishing.md), with page-local
parameters $\beta\in[1,2]$ (the source's $\theta$) and $\tau_{\mathrm S}$ (the source's $\tau$),

$$\psi^{\mathrm{SBM}}(r)=\begin{cases}0,& r<0,\\ \min\{\beta r,\ 1+\tau_{\mathrm S}(r-1)\},& 0<r\le1,\\ r\,\psi^{\mathrm{SBM}}(1/r),& r>1.\end{cases}$$

*(compiler check, not in the sources: the source writes the slope as the limiter of the inverse
ratio times the backward difference; since the third branch makes $\psi^{\mathrm{SBM}}$
symmetric, $\psi(r)/r=\psi(1/r)$, the two forms give the same slope.)* After Lie and Noelle, Chu et
al. (2025a) classify the settings by $\tau_{\mathrm S}$ (§2.1.1):

- $\tau_{\mathrm S}\ge0.5$: **dissipative**; contacts are smeared in time;
- $0\le\tau_{\mathrm S}<0.5$: **compressive**; contacts stay sharp within a few points, smooth
  extrema are slightly compressed into kinks;
- $\tau_{\mathrm S}<0$: **overcompressive**; contacts stay very sharp, but smooth solutions are
  overcompressed into artificial $O(1)$ jumps.

Larger $\beta$ is less dissipative and in general more oscillatory; $\beta=2$ in all examples
(§2.1.1). With $\beta=2$, $\tau_{\mathrm S}=0.5$ the SBM limiter is the **Minmod2** limiter,
the generalized minmod with factor 2 of the TVD page, $\mathrm{minmod}(2\delta^-,\tfrac12(\delta^-+\delta^+),2\delta^+)/\Delta x$
in terms of the undivided differences (§2.2). *(compiler check, not in the sources: for
$0<r\le1$ both forms give $\min\{2r,(1+r)/2\}$ times the forward difference, for $r>1$ both give
$\min\{2,(1+r)/2\}$.)*

The **adaptive** rule (§2.2, §3.2): in a cell flagged rough, the overcompressive setting
$\beta=2$, $\tau_{\mathrm S}=-0.25$; elsewhere Minmod2. The plain "LDCU" scheme of the
comparisons uses Minmod2 everywhere. In 2D with the minmod-based indicator the switch is
directional: the overcompressive limiter is used for the $x$-slopes only in cells flagged by the
$x$-test and for the $y$-slopes only in cells flagged by the $y$-test (§3.2.1).

## Roughness indicators

Chu et al. (2025a) call both switches "smoothness indicators"; they detect shocks and contacts and
are not the WENO indicators $\beta_k$ of [smoothness indicators](/definitions/smoothness-indicator.md).
They belong with the [troubled-cell indicators](/definitions/troubled-cell-indicator.md).

**Minmod-based (MM) indicator** (§2.2.1; a slight modification of the shock indicator of Wang et
al. (2015), as the authors state). With
$s_i=\mathrm{minmod}(\bar\rho_{i+1}-\bar\rho_i,\ \bar\rho_i-\bar\rho_{i-1})$ (page-local), cell $i$
is rough if

$$\lvert s_i\rvert>\max\{\lvert s_{i-1}\rvert,\lvert s_{i+1}\rvert\}+\delta_{\mathrm{MM}},\qquad\delta_{\mathrm{MM}}=10^{-4}$$

in all examples ($\delta_{\mathrm{MM}}$ page-local, "a size of a jump in $\rho$, which we
neglect"); the authors state that the indicator "is not very sensitive" to its value. In 2D it is
applied direction by direction to the density differences along $x$ and along $y$ (§3.2.1).

**Weak-local-residual (WLR) indicator** (§2.2.2; the residual is that of Kurganov and Liu (2012),
its use as a limiter switch is the contribution). For the density equation, from the cell
averages at $t^{n-2}$, $t^{n-1}$ and the reconstructed interface values at those levels
(Eq. (2.7)),

$$\mathcal W_{i+1/2}=\frac{\Delta x}6\Big[\delta_t\rho_{i+3/2}+4\,\delta_t\rho_{i+1/2}+\delta_t\rho_{i-1/2}\Big]+\frac{\Delta t^{n-2}}4\Big[(\rho v)^{n-1}_{i+3/2}-(\rho v)^{n-1}_{i-1/2}+(\rho v)^{n-2}_{i+3/2}-(\rho v)^{n-2}_{i-1/2}\Big],$$

with $\delta_t\rho_k=\rho^{n-1}_k-\rho^{n-2}_k$ (page-local shorthand; $\mathcal W$ page-local, the source's $\varepsilon^{n-3/2}_{j+1/2}$) and the interface values taken
as $u^-_{i+1/2}$; using $u^+$ or the average makes "no visible advantages or disadvantages"
(Remark 2.2). The indicator is the Simpson average
$\bar{\mathcal W}_{i+1/2}=\tfrac16(\mathcal W_{i-1/2}+4\mathcal W_{i+1/2}+\mathcal W_{i+3/2})$ and
the test is $\bar{\mathcal W}>C_{\mathrm W}(\Delta x)^2$ (Eq. (2.9); $C_{\mathrm W}$ page-local, the
source's $C$). The expected sizes, recalled from Kurganov and Liu (Eq. (2.8)), are
$\|\mathcal W\|_\infty\sim\Delta$ at shocks, $\Delta^{\alpha_{\mathrm W}}$ with
$1<\alpha_{\mathrm W}\le2$ at contacts and $\Delta^4$ in smooth regions,
$\Delta=\max\{\Delta t,\Delta x\}$ ($\alpha_{\mathrm W}$ page-local). The constant is problem
dependent: $C_{\mathrm W}=0.1$, $0.35$, $0.1$, $4$, $5$, $3$ in Examples 1–6. The 2D residual
(§3.2.2) is the tensor Simpson–trapezoid analogue centred at the vertex
$(x_{i+1/2},y_{j+1/2})$, over $[x_{i-1/2},x_{i+3/2}]\times[y_{j-1/2},y_{j+3/2}]$; since no values
are reconstructed at vertices, these are set to the average of the four surrounding cell
averages. The 2D residual is divided by $\max\{\Delta t,\Delta x,\Delta y\}$, the 1D one is not,
and both are tested
against $C_{\mathrm W}\max\{(\Delta x)^2,(\Delta y)^2\}$.

*(compiler check, not in the sources: the space bracket is Simpson's rule over
$[x_{i-1/2},x_{i+3/2}]$, of length $2\Delta x$, and the flux bracket the trapezoidal rule over
$[t^{n-2},t^{n-1}]$; both carry half their natural weights, $\Delta x/6$ for $\Delta x/3$ and
$\Delta t/4$ for $\Delta t/2$, a common factor that only rescales $C_{\mathrm W}$.)*

## Time stepping and test set

All runs use three-stage third-order [SSP Runge–Kutta](/methods/ssp-runge-kutta.md) at CFL
0.4, $\gamma=1.4$ (Examples 1–5) or $5/3$ (Example 6) (§4). A-MM and A-WLR are compared with the
plain LDCU scheme; references are LDCU runs on finer meshes. All evidence is visual (no error
tables, no timings), and no theorem is proved.

| Example | problem | mesh | outcome (Chu et al. (2025a), §4) |
|---|---|---|---|
| 1 | shock–entropy wave, $\sin(20x)$ density, $[-10,5]$, $t=5$ | $\Delta x=1/80$ | both adaptive schemes resolve the high-frequency waves behind the shock much better; A-WLR best (Fig. 4.1) |
| 2 | [Shu–Osher](/benchmarks/shu-osher-problem.md), $[-5,15]$, $t=5$ | $1/40$ | both beat LDCU; A-MM resolves the smooth parts better than A-WLR, attributed to the large $C_{\mathrm W}=0.35$ (Fig. 4.2) |
| 3 | [Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md), $t=0.038$ | $1/400$ | A-MM beats LDCU, A-WLR resolves the contact near $x=0.6$ sharply (Fig. 4.4) |
| 4 | [2D Riemann configuration 3](/benchmarks/two-dimensional-riemann-problems.md), $[0,1.2]^2$, $t=1$ | $\Delta x=\Delta y=3/2500$ | sideband instability of the jet and the instability along its neck better captured; A-WLR flags mostly the shocks (Figs. 4.5–4.6) |
| 5 | Liska–Wendroff [implosion](/benchmarks/explosion-and-implosion-problems.md), $t=2.5$ | $1/2000$ | the diagonal jet travels much further; A-MM less diffusive than A-WLR (Figs. 4.7–4.8) |
| 6 | [Rayleigh–Taylor](/benchmarks/rayleigh-taylor-instability.md), $\gamma=5/3$, $t=1.95$, $2.95$ | $1/1024$ | more small structures; A-MM uses the overcompressive limiter in more cells (Figs. 4.9–4.10) |

*(compiler check, not in the sources: $\Delta x=3/2500$ on $[0,1.2]$ is $1000$ cells per direction.)* Across the 2D
tests A-MM flags more cells than A-WLR (§4.2). For the blast wave the authors claim that A-WLR is,
to their knowledge, "the first Riemann-problem solver-free scheme" to resolve the contact near
$x=0.6$ sharply (§4.1); the claim rests on the figure.

**Tuning of the WLR constant.** Kurganov and Liu tuned the constant on a coarse mesh and reused it
on finer meshes for adaptive artificial viscosity; for the limiter switch Chu et al. (2025a) find
this "does not seem to be robust" (Example 2, Fig. 4.3): $C_{\mathrm W}=0.2$ gives a smooth
solution on $\Delta x=1/40$ and clear staircases on $1/200$. In the implosion problem a smaller
$C_{\mathrm W}$ sharpens coarse-mesh A-WLR results but gives "severe instabilities" on $1/2000$
(Example 5). The conclusion (§5): the WLR indicator helps in some examples but depends on a
constant that is hard to tune; the MM indicator gives a robust adaption strategy.

**Symmetry.** In the implosion and Rayleigh–Taylor problems the symmetry about $y=x$ and about
$x=0.125$ is lost to round-off in these low-dissipation schemes; it is enforced by averaging
mirrored cell values after every step, after Wang et al. (2020) (Remarks 4.1–4.2). See
[symmetry preservation](/properties/symmetry-preservation.md) and
[numerical dissipation](/definitions/numerical-dissipation.md).

## Qualifications

- The version read is the arXiv v1 preprint with two authors (Chu, Kurganov); the version of
  record adds Menshov, and its content may differ.
- The adaptive scheme relies on the indicator never flagging smooth regions, since by the
  authors' own account the overcompressive setting creates $O(1)$ jumps in smooth flow
  (§2.1.1); the staircases of Fig. 4.3 show the WLR switch failing in this way.
- As printed, the WLR test (2.9) carries no absolute value although $\mathcal W$ is signed, and
  is indexed by the cell $i$ while $\bar{\mathcal W}$ lives at interfaces; how an interface value
  flags a cell is not stated. The SBM definition (2.6) leaves $r=0$ to the third branch, where
  $\psi(1/r)$ is undefined *(compiler check, not in the sources: the limit $r\to0^+$ of the third branch gives $0$.)*.
- Example 1 is described as "a forward-facing shock wave of Mach number 1.1" with post-shock
  state $(\rho,v,p)=(1.51695,0.523346,1.805)$ into $(1+0.1\sin(20x),0,1)$. *(compiler check, not
  in the sources: the Rankine–Hugoniot conditions for $\gamma=1.4$ into $\rho=p=1$ at rest give
  $(1.515695,0.523346,1.805)$ for a Mach 1.3 shock and $(1.16908,0.18824,1.245)$ for Mach 1.1, so
  the printed velocity and pressure are those of a Mach 1.3 shock and the printed density drops a
  digit.)* [Yajaman et al. (2025)](/sources/yajaman-2025.md) (Eq. (70)) print the same
  Mach 1.3 state, density 1.515695, also labelled Mach 1.1, and Chu et al. (2025c) (§3, Ex. 1) print
  the 1.51695 state of Chu et al. (2025a), again as Mach 1.1, on $[-5,5]$ with the jump at $x=-4.5$. See
  [Shu–Osher problem](/benchmarks/shu-osher-problem.md).

# Citations

- [Chu et al. (2025a)](/sources/chu-2025.md) — §1, §2.1 (LDCU flux, anti-diffusion, Eqs. (2.1), (2.4)–(2.6)), §2.2 (Eqs. (2.7)–(2.9), Remark 2.2), §3 (Eq. (3.1), §3.2), §4 (Examples 1–6, Remarks 4.1–4.2), §5, App. A (arXiv v1).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — Eq. (5): the HLL-state anti-diffusion of the CURH flux, for comparison.
- [Yajaman et al. (2025)](/sources/yajaman-2025.md) — Eq. (70): the same shock state of the shock–entropy-wave problem.
- [Chu et al. (2025c)](/sources/chu-2025-c.md) — §1, §2.1–2.3 (Eqs. (2.2)–(2.16), Remarks 2.1–2.2), §3 (Examples 1–5) (arXiv v1): the new LDCU scheme with a moving subcell jump.
