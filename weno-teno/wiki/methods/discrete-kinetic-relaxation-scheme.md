---
type: Method
title: "Discrete kinetic relaxation schemes"
description: "A discrete kinetic (Jin–Xin, BGK-type) scheme replaces a system of conservation laws by a linear transport system with diagonal velocities relaxing to a Maxwellian; combined with deferred correction it is arbitrarily high order, asymptotic preserving and computationally explicit, because the projection on the conserved variables annihilates the stiff source, and it runs at CFL numbers near one."
status: established
aliases: [discrete BGK scheme, kinetic scheme, Jin–Xin relaxation scheme, discrete kinetic approximation, four-wave model]
tags: [asymptotic-preserving, finite-difference, limiting]
timestamp: 2026-10-23T10:00:00Z
---

# Discrete kinetic relaxation schemes

A **discrete kinetic approximation** of the conservation law
$\partial_tu+\sum_d\partial_{x_d}f^{(d)}(u)=0$, $u\in\mathbb R^m$, is the relaxation system

$$\partial_t\mathsf f+\sum_d\Lambda^{(d)}\partial_{x_d}\mathsf f=\frac1\varepsilon\big(\mathbb M(\mathbb P\mathsf f)-\mathsf f\big),$$

with page-local symbols: kinetic unknown $\mathsf f\in\mathbb R^{L}$; constant diagonal velocity
matrices $\Lambda^{(d)}$; a constant $m\times L$ projection $\mathbb P$ that returns the conserved
variables, $u^\varepsilon=\mathbb P\mathsf f$; a Lipschitz Maxwellian $\mathbb M:\mathbb R^m\to\mathbb R^L$;
and the relaxation time $\varepsilon$, which plays the role of a Knudsen number (not the WENO
regularization $\epsilon$). The Maxwellian satisfies the consistency relations

$$\mathbb P\,\mathbb M(u)=u,\qquad \mathbb P\,\Lambda^{(d)}\mathbb M(u)=f^{(d)}(u),$$

so that, formally, $\mathsf f=\mathbb M(u^\varepsilon)+O(\varepsilon)$ and
$\partial_tu^\varepsilon+\sum_d\partial_{x_d}f^{(d)}(u^\varepsilon)=O(\varepsilon)$ (Chapman–Enskog
limit). This is the setting of Jin–Xin, Natalini and Aregba-Driollet–Natalini, as recalled by
[Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) (§2, Eqs. (1)–(3)); the
nonlinearity sits in the local source, the transport is linear with constant speeds.

## Velocity models

Aregba-Driollet and Natalini's orthogonal-velocity construction, as recalled by Abgrall &
Nassajian Mojarrad (§2.1): $N_{\mathrm b}$ blocks of size $m$ (page-local), $\mathbb P=(\mathrm{Id}_m,\dots,\mathrm{Id}_m)$,
$\Lambda^{(d)}=\mathrm{diag}(\lambda_{jd}\mathrm{Id}_m)_j$ with $\sum_j\lambda_{jd}=0$ and
$\sum_j\lambda_{jd}\lambda_{jd'}=0$ for $d\ne d'$ (so $N_{\mathrm b}\ge\dim+1$), and

$$\mathbb M_j(u)=\frac u{N_{\mathrm b}}+\sum_d\frac{f^{(d)}(u)}{a_d^2}\lambda_{jd},\qquad a_d^2=\sum_j\lambda_{jd}^2 .$$

The paper uses a family with angular and speed levels; its simplest member, the **four-wave
model** in 2D, has velocities $(0,\lambda_{\mathrm k})$, $(-\lambda_{\mathrm k},0)$,
$(0,-\lambda_{\mathrm k})$, $(\lambda_{\mathrm k},0)$ (page-local speed $\lambda_{\mathrm k}>0$) and

$$\mathbb M_j(u)=\frac14\Big(u+\frac2{\lambda_{\mathrm k}}\big(f^{(1)}(u)\cos\tfrac{j\pi}2+f^{(2)}(u)\sin\tfrac{j\pi}2\big)\Big),\qquad j=1,\dots,4 .$$

*(compiler check, not in the sources: $\sum_j\mathbb M_j=u$ and
$\sum_j\lambda_{\mathrm k}\cos\tfrac{j\pi}2\,\mathbb M_j=f^{(1)}$, so the consistency relations hold.)*
With the four-wave model the 2D linear stability reduces to the 1D results of Abgrall and
Torlo (§4). The paper does not state the values of $\lambda_{\mathrm k}$ and $\varepsilon$
used in its tests.

## High order and explicit: the projection trick

Time is discretized by [deferred correction](/methods/deferred-correction.md) in which the
low-order operator is forward Euler on the transport and both operators keep the relaxation
source in the same implicit form (Eqs. (9)–(10)). Applying $\mathbb P$ to an iteration, the
source disappears because $\mathbb P\mathbb M(\mathbb P\mathsf f)=\mathbb P\mathsf f$, and the
conserved part of the new iterate is explicit (Eq. (12)):

$$\mathbb P\mathsf f^{n,m,(\ell+1)}=\mathbb P\mathsf f^{n,0}-\Delta t\sum_k\Omega_{mk}\sum_d\frac{1}{\Delta x_d}\mathbb P\Lambda^{(d)}\delta^{(d)}\mathsf f^{n,k,(\ell)}$$

(page-local DeC weights $\Omega_{mk}$, undivided flux differences $\delta^{(d)}$, direction
spacing $\Delta x_d$). The Maxwellian $\mathbb M(\mathbb P\mathsf f^{(\ell+1)})$ is then known, and
the full kinetic update (Eq. (14a)) needs only the inverse of the small matrix
$\mathrm{Id}+\frac{\Delta t}\varepsilon\Omega$ of the sub-step weights, independent of space. The
cost is stated to be "of the same order of a fully explicit scheme" (Abstract). For orders 1,
2 and 4 the matrices $(\mathrm{Id}+\frac{\Delta t}\varepsilon\Omega)^{-1}$ and
$\frac{\Delta t}\varepsilon(\mathrm{Id}+\frac{\Delta t}\varepsilon\Omega)^{-1}\Omega$ are bounded
uniformly in $\varepsilon$ (first order: $\varepsilon/(\varepsilon+\Delta t)$ and
$\Delta t/(\varepsilon+\Delta t)$), which gives the $\varepsilon$-independent contraction of the
DeC iteration (§2.3, Prop. 1).

**Asymptotic preservation** (Prop. 2). With $u^{\varepsilon,(\ell)}=\mathbb P\mathsf f^{(\ell)}$, the
update gives $\mathsf f^{(\ell+1)}=\mathbb M(u^{\varepsilon,(\ell+1)})+O(\varepsilon)$, and by the
consistency relations the conserved update is a DeC discretization of the limit conservation
law itself, up to $O(\varepsilon)$; AP is meant in Jin's sense, stability and accuracy uniform
in $\varepsilon$ (§1, §2.2; [asymptotic preservation](/properties/asymptotic-preservation.md)).
The AP property is shown only as this formal consistency: the tests do not report $\varepsilon$.

## Space discretization

Point values on grid nodes and Iserles' interpolatory upwind-biased finite differences of
orders 1–4, written in [conservative flux form](/definitions/conservative-finite-difference-scheme.md)
$\delta\mathsf f_i=\hat{\mathsf f}_{i+1/2}-\hat{\mathsf f}_{i-1/2}$ (§3.1); the fourth-order
scheme uses the stencil $i-3,\dots,i+1$ for a positive speed, with face flux
$\hat{\mathsf f}_{i+1/2}=\tfrac1{12}\mathsf f_{i-2}-\tfrac5{12}\mathsf f_{i-1}+\tfrac{13}{12}\mathsf f_i+\tfrac14\mathsf f_{i+1}$.
Each kinetic component is a scalar linear transport, so no Riemann solver or characteristic
decomposition is needed. In 2D the update of a node is the sum of four vertex residuals of
the quads around it, whose sum over a quad approximates the flux through its boundary; this
guarantees [local conservation](/results/local-conservation-flux-form.md) and lets a quad be
recomputed on its own (§2.1, Eqs. (15)–(16)). The first-order version "amounts to global
[Lax–Friedrichs](/methods/lax-friedrichs-flux.md)" (§3.2.2).

**Nonlinear stabilization** (§3.2). (i) A flux-limiter blend of first- and higher-order
differences with a smoothness ratio and a TVD-type limiter function
([TVD](/definitions/total-variation-diminishing.md)); the authors note that it ignores the
projection on the conserved variables, so weaknesses are expected. (ii) A
[MOOD](/methods/mood-a-posteriori-limiting.md)-type fallback: after the high-order step, nodes
whose $(\rho,v,p)$ is non-positive or NaN are flagged, quads with a flagged corner are flagged,
and their four residuals are recomputed with the first-order scheme for each sub-step; no
extremum detection is used. Applied at every DeC iteration it would make the scheme
invariant-domain preserving, which the tests do not do.

## Evidence

All 2D, CFL 1 unless stated (§5):

- linear advection $u_t+u_x+u_y=0$ on $[-2,2]^2$, $t=10$: observed orders 2.08/2.07/2.07
  ($L^1/L^2/L^\infty$) for the second-order scheme and 4.01/4.01/4.00 for the fourth-order one,
  finest $L^\infty$ error $6.9070\times10^{-6}$ at $h=0.003125$ (Tables 2–3);
- [isentropic vortex](/benchmarks/isentropic-vortex.md) with the four-wave model, fourth
  order in space and time: design order at $t=5$ (Fig. 6); at $t=200$ on $200\times200$ the
  pressure error stays in $[-4.2\times10^{-3},1.6\times10^{-3}]$ (Fig. 7); CFL 1.2 to $t=200$
  with five iterations (Remark 1);
- radial Sod problem, $200\times200$, $t=0.16$: limiter and MOOD give almost identical
  results, MOOD never switches to first order and leaves over- and undershoots, the limiter
  removes the overshoot (Figs. 8–9);
- radial shock with pressure ratio 1000: MOOD is required, the flagged quads are few and
  localized at discontinuities (Fig. 10).

## Qualifications

- The CFL-above-one claim comes from a linear analysis that excludes the source
  ([deferred correction](/methods/deferred-correction.md), Table 1); the paper states both that
  the schemes "are always stable for CFL $=1+\delta$" with the BGK source (§4) and that the
  source is not included in the analysis and observed limits are more severe (Remark 1).
- CFL here is measured with the kinetic speeds: $\mu=a\Delta t/\Delta x$ with $a$ an entry of
  $\Lambda^{(1)}$ (§4), not with the physical wave speeds.
- The isentropic-vortex data print $v_2=\frac{\sqrt2}2+\dots$ while the free stream and the
  vortex centre use $\frac{\sqrt3}2$ (§5.2.1); the radial Sod problem uses periodic boundaries.
- *(compiler check, not in the sources: the printed fourth-order face flux
  $\tfrac1{12}\mathsf f_{i-2}-\tfrac5{12}\mathsf f_{i-1}+\tfrac{13}{12}\mathsf f_i+\tfrac14\mathsf f_{i+1}$
  reproduces the printed fourth-order difference
  $-\tfrac1{12}\mathsf f_{i-3}+\tfrac12\mathsf f_{i-2}-\tfrac32\mathsf f_{i-1}+\tfrac56\mathsf f_i+\tfrac14\mathsf f_{i+1}$,
  so the scheme used in the tests is consistent in flux form.)*

# Citations

- [Abgrall & Nassajian Mojarrad (2024)](/sources/abgrall-2024.md) — Abstract, §1, §2.1 (Eqs. (1)–(16)), §2.2 (Prop. 2), §2.3, §3.1, §3.2, §4 (Remark 1), §5 (Tables 2–3, Figs. 6–10).
