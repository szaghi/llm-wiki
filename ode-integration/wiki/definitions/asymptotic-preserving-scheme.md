---
type: Definition
title: "Asymptotic-preserving scheme"
description: "A discretization of a problem with small scale parameter ε is asymptotic-preserving when its ε→0 limit at fixed step and mesh is a consistent, stable scheme for the limit model; the page covers the definition and its strong, weak and asymptotically accurate variants, uniform accuracy, the time-integration mechanisms and the step-size restrictions they remove."
status: established
aliases: [AP scheme, AP property, asymptotic preserving, AP in time, stochastic asymptotic-preserving, sAP, asymptotically accurate, AA scheme, strongly AP, weakly AP]
tags: [asymptotic-preserving, stiff, imex, kinetic, splitting]
timestamp: 2026-10-20T06:18:00Z
---

# Asymptotic-preserving scheme

A multiscale problem carries a small parameter $\varepsilon$ (a relaxation time,
Knudsen, Mach or scaled Debye number, a semiclassical $\hbar$) such that, as
$\varepsilon\to0$, its solutions converge to those of a reduced *limit model*
(hydrodynamic, diffusive, classical, incompressible). A discretization with numerical
parameters held fixed (step size $h$, mesh width $\Delta x$, or other) is
**asymptotic-preserving (AP)** if its own limit as $\varepsilon\to0$, at those fixed
parameters, exists and is a consistent and stable discretization of the limit model
([Jin (2022)](/sources/jin-2022.md), §1, Fig. 1.2(a)). An AP scheme therefore needs no
resolution of the $\varepsilon$-scale to stay stable, and it changes from a solver of
the micro model into a solver of the macro model "automatically" when the small
scales are not resolved. In the ODE setting of
[Gottlieb et al. (2022)](/sources/gottlieb-2022.md) (§3.4) the property reads: for fixed
$h$, as $\varepsilon\to0$, the scheme reduces to a high-order discretization of the
limiting system. The low-Mach literature states it as a stability condition independent
of the Mach number plus a consistent discretization of the incompressible limit
([Orlando & Bonaventura (2025)](/sources/orlando-2025.md), §1;
[Orlando et al. (2025b)](/sources/orlando-2025-b.md), §1), and
[Toh et al. (2026)](/sources/toh-2026.md) (§3.1) quote Jin's two requirements, limit
consistency and uniform stability through an implicit step that is cheap to solve. Jin
(2022) says the term was coined in Jin (1999). The idea came from capturing steady
neutron transport in the diffusive regime (Larsen, Morel & Miller 1987), as he recalls it
(§1, p. 417).

## The definition as a commuting diagram

Let $\mathcal F^\varepsilon$ denote the micro model, $\mathcal F^0$ its limit,
$\mathcal F^\varepsilon_\delta$ a discretization with numerical parameter $\delta$
(time step and/or mesh), and $\mathcal F^0_\delta=\lim_{\varepsilon\to0}\mathcal F^\varepsilon_\delta$
at fixed $\delta$ (page-local symbols). The scheme is AP when the square

$$\begin{aligned}
\mathcal F^\varepsilon_\delta &\xrightarrow{\ \varepsilon\to0\ }\mathcal F^0_\delta\\
\downarrow{\scriptstyle\delta\to0}\ &\qquad\ \downarrow{\scriptstyle\delta\to0}\\
\mathcal F^\varepsilon\ &\xrightarrow{\ \varepsilon\to0\ }\ \mathcal F^0
\end{aligned}$$

commutes, i.e. when the right-hand arrow holds: $\mathcal F^0_\delta$ is a good
approximation of $\mathcal F^0$ (Jin 2022, Fig. 1.2(a)). The fixed parameter
names the variant. Jin speaks of a scheme being "AP in time" (the step $h$ may stay
$O(1)$), "AP in space" ($\Delta x$ or phase-space meshes), "AP in $N$" (the particle number of
the random batch method, §4.1), and **stochastic AP (sAP)**: a stochastic-Galerkin
scheme for a random kinetic equation is sAP if, with the polynomial-chaos order, mesh
and step fixed, its limit is a stochastic-Galerkin scheme for the random limit equation
(§5.5).

Jin (2022, p. 449) lists the design features expected of AP schemes for kinetic
equations: an implicit time discretization that can still be carried out explicitly or
cheaply (at least without a Newton iteration on a nonlinear algebraic system), and
automatic reduction to a good hydrodynamic scheme as $\varepsilon\to0$. These are design
goals, not part of the definition. Toh et al. (2026, §3, Eqs. (41)–(42)) cite the absence
of Newton iterations in their linear relaxation step as "an important feature of AP
schemes".

## Strong, weak and asymptotically accurate variants

The sources refine the definition in two directions.

- **Initial data.** Orlando & Bonaventura (2025, §3.1) call a scheme **strongly AP** if it
  is AP for general initial data and **weakly AP** if it needs well-prepared data; for the
  low-Mach Euler equations, IMEX Runge–Kutta pairs of type I and type ARS are strongly AP
  and type II non-ARS pairs only weakly AP, because they need an initial pressure without
  $O(1)$ and $O(\mathrm{Ma})$ gradients (Thm. 3.4, Assumption 3.3; types on
  [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md)). They note that, unlike earlier
  schemes they cite, theirs does not need a divergence-free initial velocity.
- **Order in the limit.** A scheme is **asymptotically accurate (AA)** if it keeps its
  order as $\varepsilon\to0$, i.e. the limit scheme $\mathcal F^0_\delta$ has the order of
  $\mathcal F^\varepsilon_\delta$ (Orlando & Bonaventura 2025, §3.1; Orlando et al. 2025b,
  §1; [Boscheri & Thomann (2024)](/sources/boscheri-2024.md), §1).
  [Hu & Shu (2025)](/sources/hu-2025.md) (Def. 7.3) build AA into their definition of AP and
  note that it is "stronger than the classical" one of Jin. Orlando & Bonaventura state
  that AP does not imply AA and that "it is quite established that L-stability is necessary
  to guarantee asymptotic accuracy" (§3.1).

## From AP to uniform accuracy

Jin (2022, §1, eqs. (1.1)–(1.6)) reproduces the argument of Golse, Jin & Levermore (1999)
that turns the AP property into an error bound **uniform in $\varepsilon$**. Let $r$ be the
order of the scheme in $\delta$ for fixed $\varepsilon$ and let $\kappa$, $1\le\kappa\le r$,
be the power of $\varepsilon$ that the classical error constant carries (page-local
symbols; Jin's $s$). In a suitable problem-dependent norm, assume

$$\begin{aligned}
&\lVert\mathcal F^\varepsilon-\mathcal F^0\rVert=O(\varepsilon), &&\text{(limit model)}\\
&\mathcal E_1:=\lVert\mathcal F^\varepsilon_\delta-\mathcal F^\varepsilon\rVert=O(\delta^r/\varepsilon^\kappa), &&\text{(classical estimate)}\\
&\lVert\mathcal F^\varepsilon_\delta-\mathcal F^0_\delta\rVert=O(\varepsilon)\ \text{uniformly in }\delta, &&\text{(AP, first half)}\\
&\lVert\mathcal F^0_\delta-\mathcal F^0\rVert=O(\delta^r). &&\text{(AP, second half)}
\end{aligned}$$

The triangle inequality gives $\mathcal E_2=O(\varepsilon+\delta^r)$, so

$$\lVert\mathcal F^\varepsilon_\delta-\mathcal F^\varepsilon\rVert\le\min(\mathcal E_1,\mathcal E_2)=O\big(\delta^{r/(\kappa+1)}\big)\quad\text{uniformly in }\varepsilon,$$

with the worst case at $\varepsilon=O(\delta^{r/(\kappa+1)})$ (Fig. 1.2(b)). When
$\delta=o(\varepsilon^{\kappa/r})$ the scheme resolves and approximates $\mathcal F^\varepsilon$;
otherwise it approximates $\mathcal F^0$. The uniform rate $r/(\kappa+1)$ is lower than the
fixed-$\varepsilon$ order $r$: AP buys uniform convergence, not uniform order. Jin cites
Hu & Shu (2021) as "a rigorous uniform accuracy proof of AP schemes for linear problems"
(IMEX-BDF, §6.1).

Uniform accuracy at the full order has since been proved for linear hyperbolic relaxation
systems: by Hu & Shu (2025, Thms. 4.3, 5.1) for type-CK, implicitly stiffly accurate IMEX
Runge–Kutta pairs of orders 2 and 3 under extra stage-order and coefficient conditions, and
by [Ma et al. (2026)](/sources/ma-2026.md) (Thm. 3.3, Cor. 3.1) for IMEX-BDF of orders 1–4
on every system satisfying Yong's structural stability condition. Both need data without an
initial layer: Hu & Shu start after the layer, Ma et al. admit either a start after the layer
or data prepared to the order of the scheme. Both also need a step restriction
$h\le c/N^2$ coming from the proof ($N$ the Fourier cutoff of the space discretization,
$c$ a constant; page-local). Hu & Shu stress that AP, which concerns the two ends
$\varepsilon=O(1)$ and $\varepsilon\to0$, "does not settle" the accuracy in the
intermediate regime (§1, App. 7.3). See
[uniform accuracy of IMEX schemes](/results/uniform-accuracy-relaxation-systems.md).

## Time-integration mechanisms

Explicit time stepping of the stiff term ties $h$ to $\varepsilon$. The AP literature
removes that restriction with a small set of devices. The sources organize them as follows.

- **IMEX splitting of the stiff relaxation.** Write $y'=\mathcal T(y)+\frac1\varepsilon Q(y)$
  with a non-stiff transport part $\mathcal T$ and a stiff collision or relaxation part
  $Q$ (page-local symbols). Treat $\mathcal T$ explicitly and $Q/\varepsilon$ implicitly,
  i.e. $f^{\mathrm E}=\mathcal T$, $f^{\mathrm I}=Q/\varepsilon$ in the notation of
  [IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md). Conservation of the
  collision invariants lets the implicit step be "inverted explicitly" for BGK-type
  operators (Jin 2022, §5.1). Jin cites high-order IMEX schemes for hyperbolic relaxation
  (Pareschi & Russo 2005; Dumbser, Enaux & Toro 2008) and the combination of AP with
  positivity in Hu & Shu (2019), an exponential Runge–Kutta method by its title (§6.1).
  For type-CK pairs Hu & Shu (2025, Thm. 7.4) give formal AA conditions: global stiff
  accuracy, or their condition (A) (the last stage is projected onto equilibrium) plus
  order-dependent conditions on the explicit weights. IMEX-BDF methods are AP and uniformly
  accurate under the hypotheses of Ma et al. (2026); see
  [IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md).
- **Implicit pressure for low Mach numbers.** For the compressible Euler and Navier–Stokes
  equations at Mach number $\mathrm{Ma}$ (here $\varepsilon\propto\mathrm{Ma}^2$), the
  pressure gradient and the enthalpy flux are implicit and the convective terms explicit,
  so that the step depends on the flow speed only. Orlando & Bonaventura (2025, Thms. 3.4,
  3.7) prove formally that the resulting IMEX Runge–Kutta stage system is a consistent
  discretization of the single-scale and two-scale low-Mach limits for a general equation
  of state, with local stage errors $O(h^2)$. [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md)
  (§3.1, Eqs. (37)–(47)) show formally for a first-order semi-implicit version that the
  discrete velocity satisfies $\nabla\cdot u^{n+1}_{(0)}=O(h)$ at leading order. Boscheri &
  Thomann (2024, §3.2) and [Birke et al. (2024)](/sources/birke-2024.md) extend the approach
  to ideal MHD, the former transferring an AP proof from a related scheme, the latter
  asserting AP without analysis. These schemes are on
  [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md). For a
  general equation of state the limit is incompressible only if the background pressure is
  constant in time; a time-dependent boundary pressure gives
  $\nabla\cdot u=-\frac{1}{\rho c^2}\frac{\mathrm d\bar p}{\mathrm dt}$, an EOS-dependent
  compression (Orlando & Bonaventura 2025, §2.2; Orlando et al. 2025b, §2.2, Eqs. (23)–(24);
  page-local $\rho$, $u$, $c$, $\bar p$).
- **Split relaxation inside Runge–Kutta stages.** Toh et al. (2026, §3, §3.1) apply, at
  every sub-stage of an explicit SSP-RK2 step, a first-order implicit relaxation step for
  the stiff electric-field and current equations of extended MHD, linear because the
  nonstiff variables are frozen. As the relaxation parameters tend to zero at fixed $h$ and
  $\Delta x$ the update reduces to ideal-MHD Ohm's and Ampère's laws (Eqs. (43)–(50)); the
  limit is consistent only if the electric-field flux update uses the already updated
  magnetic field, otherwise a nonzero residual source survives into the next sub-stage. The
  scheme is first order in time in the stiff regime (§3.5). See
  [operator splitting](/methods/operator-splitting.md).
- **Penalization.** Subtract a simple stiff operator that can be inverted (BGK, Fokker–Planck),
  treat it implicitly, and treat the remainder explicitly. See
  [BGK penalization](/methods/bgk-penalization.md).
- **Exponential reformulation.** Integrate the relaxation factor
  $e^{\beta t/\varepsilon}$ exactly. Jin (2022, §5.2) says any explicit Runge–Kutta method
  applied to the reformulated equation is high order and "satisfies the AP property
  automatically". See [exponential integrators](/methods/exponential-integrators.md) and
  [BGK penalization](/methods/bgk-penalization.md).
- **Micro–macro decomposition.** Split $f$ into equilibrium plus a correction scaled by
  $\varepsilon$, and treat only a linear stiff operator implicitly. See
  [micro–macro decomposition](/methods/micro-macro-decomposition.md).
- **Splitting with exactly integrated sub-flows.** The Lie and Strang time-splitting spectral
  methods for the semiclassical Schrödinger equation solve each sub-step exactly in time.
  In the Wigner picture each sub-step has a limit as $\varepsilon\to0$ at fixed $h$, and the
  limits are the splitting of the classical Liouville equation. Hence the scheme is AP in
  time for physical observables: $h=O(1)$ with $\Delta x=o(\varepsilon)$ (Jin 2022, §3.3,
  eqs. (3.7)–(3.10)). Crank–Nicolson does not share the property: in Example 3.3
  ($\varepsilon=10^{-3}$) it misses the weak limit even with $h=10^{-4}$. Rigorous
  uniform-in-$\varepsilon$ estimates are in Golse, Jin & Paul (2021) and Lasser & Lubich (2020)
  (Remark 3.2). See [operator splitting](/methods/operator-splitting.md).
- **Parity reformulation for diffusive limits.** For linear transport in the diffusive
  scaling, Jin, Pareschi & Toscani (2000) rewrite the even/odd parities so that the
  characteristic speeds of the transport part no longer depend on $\varepsilon$. They then
  split into an implicit stiff relaxation step and an explicit non-stiff transport step
  (Jin 2022, §5.4.1, eqs. (5.20)–(5.28)).
- **Multiderivative implicit stages.** Gottlieb et al. (2022, §3.4) put both $Q$ and
  $\dot Q=Q'(y)Q(y)$ into the implicit stages of an IMEX
  [multiderivative Runge–Kutta method](/methods/multiderivative-runge-kutta.md); see the
  next section.

## A sufficient condition for IMEX multiderivative schemes

Gottlieb et al. (2022, §3.4.1) consider $y'=\mathcal T(y)+\frac1\varepsilon Q(y)$ with five
structural properties:
(1) forward Euler on $\mathcal T$ preserves positivity for $h\le h_{\mathrm{FE}}$;
(2) backward Euler on $Q$ preserves positivity for every step;
(3) a linear conservation map $\mathcal R$ annihilates $Q$;
(4) $Q(y)=0$ iff $y=E(\mathcal Ry)$ for a local-equilibrium map $E$;
(5) $\dot Q(y)=-C_{\mathcal Ry}\,Q(y)$ with a scalar $C_{\mathcal Ry}>0$ that depends only on
$\mathcal Ry$ (page-local symbols $\mathcal R$, $E$, $C$).
The limiting system is $\omega'=\mathcal R\mathcal T(E(\omega))$ for $\omega=\mathcal Ry$.
BGK, [Broadwell](/benchmarks/broadwell-model.md) and the Jin–Xin-type
[hyperbolic relaxation system](/benchmarks/hyperbolic-relaxation-system.md) satisfy property 5
($C=1$, $C=\rho$, $C=1$ respectively, eqs. (35), (40), (48)).

Write the method in Shu–Osher form with explicit forward-Euler substeps $h/r$ on
$\mathcal T$ and, on stage $i$, implicit terms $h\,d_{ii}\frac1\varepsilon Q(Y_i)$ and
$h^2\dot d_{ii}\frac1{\varepsilon^2}\dot Q(Y_i)$ (page-local diagonal coefficients
$d_{ii}$, $\dot d_{ii}$). **Proposition 1** states: if every Shu–Osher coefficient is
non-negative and $\dot d_{ii}\le0$, the scheme preserves positivity for
$h\le r\,h_{\mathrm{FE}}$ independently of $\varepsilon$. If moreover

$$d_{ii}+\lvert\dot d_{ii}\rvert>0\quad\text{for every stage }i,$$

the scheme is AP. As $\varepsilon\to0$ at fixed $h$ it reduces to the explicit part applied
to the limiting system, "with the same order as the original scheme". The mechanism
(eq. (51)): by property 5 the implicit part of stage $i$ is
$\big(\frac{h}{\varepsilon}d_{ii}-\frac{h^2}{\varepsilon^2}\dot d_{ii}C_{\mathcal RY_i}\big)Q(Y_i)$,
a backward-Euler step with a non-negative effective step. Property 2 therefore gives
positivity, and the coefficient blows up as $\varepsilon\to0$, which forces $Q(Y_i)\to0$ at every
stage. The authors present their third-order scheme (6 stages, $r\approx0.9044$) as the
first positivity-preserving AP IMEX scheme of order three. Earlier derivative-correction
schemes (Hu, Shu & Zhang) stopped at order two (§3.4). Remark 2 places the schemes in the
type-A, globally-stiffly-accurate class of Boscarino, Pareschi & Russo, which admits
arbitrary (not well-prepared) initial data. See
[positivity preservation](/properties/positivity-preservation.md) and
[SSP Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md).

## Step-size restrictions that AP schemes remove or keep

The sources quote these restrictions (Jin 2022 unless stated):

| Setting | Explicit or non-AP restriction | AP outcome |
|---|---|---|
| Boltzmann collision term, explicit | $h=O(\varepsilon)$ | $h$ independent of $\varepsilon$ (§5.1) |
| Fokker–Planck–Landau collisions, explicit | $h=O(\varepsilon(\Delta v)^2)$, $\Delta v$ the velocity mesh | penalization by a Fokker–Planck operator (§5.1) |
| Semiclassical Schrödinger, wave function | $h=o(\varepsilon)$, $\Delta x=o(\varepsilon)$ (Thm. 3.1) | observables with $h=O(1)$, still $\Delta x=o(\varepsilon)$ (§3.3) |
| Euler–Poisson, quasi-neutral limit | $h\le\varepsilon$ | reformulated Poisson equation uniformly elliptic in $\varepsilon$ (§6.2) |
| Low Mach, explicit shock capturing | $\Delta x=O(\varepsilon)$, then $h=O(\varepsilon\Delta x)$ | implicit linear pressure term, projection method in the limit (§6.5) |
| Low Mach, compressible Navier–Stokes (Boscheri & Pareschi 2021, Eqs. (20), (27)) | acoustic speeds $\lvert u\pm c/\sqrt\varepsilon\rvert$, $h=O(\sqrt\varepsilon)$ | $h\le\nu\,\Delta x/\max\lvert u\rvert$, material speed only |
| Low Mach, Euler with DG (Orlando & Bonaventura 2025, §5.4) | acoustic Courant number about 1 | acoustic Courant numbers up to about 19,300 at advective Courant number 0.015 |
| Low Mach and low Alfvén number, ideal MHD (Boscheri & Thomann 2024, §4.7) | explicit magnetosonic step | steps up to about $10^4$ times larger at $\mathrm{Ma}=10^{-4}$ |
| Extended MHD relaxation (Toh et al. 2026, §2, §3) | $h=O(\varepsilon_i)$ for each relaxation parameter | CFL step on the fluid and electron sound speeds, independent of the speed of light (Eqs. (66), (94)); first order in time |
| Diffusive limit of linear transport | — | limit is an explicit diffusion scheme, $h=O(\Delta x^2)$ uniformly in $\varepsilon$ (§5.4) |
| Diffusive limit, Boscarino–Pareschi–Russo (2013) reformulation | — | limit is an implicit diffusion scheme, $h=O(\Delta x)$ (p. 457) |
| Stochastic-Galerkin micro–macro scheme | — | $h\le\frac{\sigma_{\min}}3\Delta x^2+\frac{2\varepsilon}3\Delta x$ (Thm. 5.6) |

For the last row, $\sigma_{\min}$ is the lower bound of the scattering cross-section
(page-local). The Boscarino–Pareschi–Russo reformulation adds and subtracts a
diffusion term $\mu(\varepsilon)v^2\partial_{xx}r/\sigma$ ($\mu(\varepsilon)\in[0,1]$,
$\mu(0)=1$; page-local). It treats the added copy implicitly within an IMEX Runge–Kutta
scheme, and $\mu=1$ gives the largest stability region (Jin 2022, eqs. (5.37)–(5.38)).
The low-Mach rows use $u$ for the flow velocity and $c$ for the sound speed (page-local).

## Not every AP scheme is AP for every use

- **Initial layers and well-prepared data.** The first-order BGK-penalization IMEX scheme
  is AP only after an initial transient: the numerical distribution comes within
  $O(\varepsilon)$ of the local Maxwellian only after some steps when the data are not near
  equilibrium. A two-step successive
  penalization reaches the limit in one step (Jin 2022, §5.1, Remark 5.1; see
  [BGK penalization](/methods/bgk-penalization.md)). Gottlieb et al. (2022, Remark 2), in
  contrast, claim AP for arbitrary initial data. Type-II IMEX pairs are only weakly AP in
  the low-Mach limit (Orlando & Bonaventura 2025, §3.1), and the uniform-accuracy theorems
  of Hu & Shu (2025) and Ma et al. (2026) assume prepared data.
- **AP without uniform order.** ARS(4,4,3) is third order for $\varepsilon=O(1)$ and as
  $\varepsilon\to0$, but only second order uniformly, with an error peak near
  $\varepsilon\approx10^{-4}$–$10^{-3}$ on a linear relaxation system (Hu & Shu 2025, §6,
  Fig. 1).
- **AP limited by space.** Orlando et al. (2025b, §4.2, §5) find their IMEX and
  semi-implicit DG schemes AP and AA only "in the range of low Mach accuracy established by
  the spatial discretization": errors saturate at $\mathrm{Ma}=10^{-4}$, attributed mainly
  to DG on quadrilaterals.
- **Learned solvers.** A physics-informed neural network trained on the residual of the
  kinetic equation is not AP: its loss tends to that of the collisional equilibrium condition alone,
  not to the diffusion equation. A loss built on the micro–macro system is AP. Not every AP formulation yields
  one: the parity formulation does not (Jin 2022, §5.7, Remark 5.10).
- **Implicit deferred correction and ADER.** [Han Veiga et al. (2021)](/sources/hanveiga-2021.md)
  (§4.4, §5.3) use the linearly implicit deferred-correction variant of Abgrall & Torlo,
  which originated in AP schemes for kinetic models, and an implicit ADER. They show only that
  these integrate stiff ODEs (a stiff linear system with $h=1$, Robertson) where the explicit
  variants fail. They do not test the AP property. See
  [deferred correction](/methods/deferred-correction.md) and
  [ADER](/methods/ader-time-integration.md).

## Qualifications

- **AP is weaker than uniform accuracy.** The uniform estimate above needs the first AP
  half "uniformly in $\delta$". The bare definition does not supply that: a scheme with an
  initial layer, or an IMEX scheme with [order reduction](/definitions/order-reduction.md)
  at intermediate $\varepsilon$, can be AP without it. Jin's sentence "this argument shows
  that an AP scheme is convergent uniformly in $\varepsilon$" (p. 419) holds under
  hypotheses (1.1)–(1.4), not under the definition alone. Jin also prints
  $\lVert\mathcal F^\varepsilon_\delta-\mathcal F^\varepsilon\rVert=\min(\mathcal E_1,\mathcal E_2)$
  where $\le$ is meant. Hu & Shu (2025, §1, App. 7.3) make the same distinction.
- **Order at intermediate $\varepsilon$.** Gottlieb et al. (2022, Remark 4, §3.5) observe
  design order in both the kinetic ($\varepsilon=O(1)$) and the fluid ($\varepsilon\ll1$)
  regimes, and order reduction in between. On the stiff ODE model they also see error
  plateaus of size $O(\varepsilon)$, which they distinguish from the usual AP order reduction.
  These plateaus have the shape of the $\mathcal E_2=O(\varepsilon+\delta^r)$ branch of
  Jin's argument: the error is flat at $O(\varepsilon)$ until $h$ is small enough for the
  $\mathcal E_1$ branch to take over *(compiler check, not in the sources)*.
- **"Automatically AP" exponential Runge–Kutta.** Jin's claim (§5.2) concerns high order at
  fixed $\varepsilon$ plus the AP limit. It does not claim high order uniformly in
  $\varepsilon$.
- **Type A, extended.** Gottlieb et al. call their schemes "type A". In Boscarino–Pareschi–Russo's
  classification that means an invertible implicit matrix, but their implicit matrix $A^{\mathrm I}$ is
  singular ($d_{ii}=0$ on some stages). The extension rests on the joint condition
  $d_{ii}+\lvert\dot d_{ii}\rvert>0$.
- **Formal proofs.** The low-Mach AP theorems of Orlando & Bonaventura (2025) rest on
  stage-wise Hilbert expansions that they say "can be justified only for smooth functions";
  the extended-MHD derivation of Toh et al. (2026) is a formal limit of one sub-stage, with no
  uniform stability or accuracy estimate.
- **Garbled quotation.** Toh et al. (2026, §3.1) render Jin's design goal as an implicit
  discretization that "can either be implemented explicitly or at least very efficiently";
  "explicitly solvable" is meant.

## Contradictions

**Can an AP IMEX Runge–Kutta pair have an explicit stage in its implicit tableau?**
*Open.* [Southworth et al. (2024)](/sources/southworth-2024.md) (§5.1) state that "in [27]
[Pareschi & Russo 2005] it is proven that for IMEX schemes to be asymptotic preserving for
hyperbolic equations with stiff relaxation terms, they must have equal implicit and explicit
number of stages/not have explicit stages in the implicit method", and select only such pairs
for radiation hydrodynamics. On the same problem class, Hu & Shu (2025, App. 7.3, Thm. 7.4)
derive formally, for the nonlinear hyperbolic relaxation system and initial data with
$v_{\mathrm{in}}-f(u_{\mathrm{in}})=O(\varepsilon)$ (page-local), that a type-CK, implicitly
stiffly accurate pair (explicit first implicit stage) is AP with full order in the limit if it
is globally stiffly accurate, and keeps order 1, 2 or 3 in the limit under their condition
(A) plus one or two conditions on the explicit weights. They state that "the ARS(2,2,2) and
ARS(4,4,3) schemes are GSA, hence they are AP", and they prove uniform second order for both
and uniform third order for BHR(5,5,3)\* (Thms. 4.3, 5.1). ARS pairs have an explicit first stage
in the implicit method, so they fall under Southworth et al.'s "must not". The conflict is with the sentence as printed, not a
convention difference: both sides speak of AP for hyperbolic relaxation, and Hu & Shu's AP
(order kept in the limit) is stronger than the classical AP property. The data hypothesis does
not reconcile them for ARS pairs: write the type-CK implicit tableau as
$A^{\mathrm I}=\begin{pmatrix}0&0\\ \hat a&\hat A\end{pmatrix}$ (page-local $\hat a$, $\hat A$, as on
[uniform accuracy](/results/uniform-accuracy-relaxation-systems.md)); in Hu & Shu's limit
identity (7.3) the stiff residual of stages $2,\dots,s$ is $-\hat A^{-1}\hat a$ times that of
the initial value, and $\hat a=0$ for type ARS, so these stages, and with GSA the step result, reach equilibrium for any data after
one step *(compiler check on Eq. (7.3), not in the source)*. It may reconcile them for
type-CK non-ARS pairs, which Orlando & Bonaventura (2025, Thm. 3.4, §3.1) find only weakly AP (well-prepared data) in the low-Mach limit, a different
limit in which they find type-ARS pairs strongly AP. What would decide it: the Pareschi–Russo
proof itself (not ingested), in particular whether it assumes non-equilibrium initial data or
a specific pair class.

# Citations

- [Jin (2022)](/sources/jin-2022.md) — §1 (definition, Fig. 1.2, eqs. (1.1)–(1.6)); §3.1–3.3 (time-splitting spectral, Thm. 3.1, Example 3.3, Remark 3.2); §4.1 (AP in $N$); §5.1–5.2 (penalization, exponential reformulation, Remark 5.1); §5.4 (parity, micro–macro, Boscarino–Pareschi–Russo); §5.5 (sAP, Thm. 5.6); §5.7 (APNN, Remark 5.10); §6.1, §6.2, §6.5.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §3.4.1 (Properties 1–5, eqs. (19)–(28)); §3.4.2 (Prop. 1, eqs. (49)–(51)); Remarks 2 and 4; §3.5 (numerical regimes).
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §4.4 (IMDeC, IMADER), §5.3 (stiff tests).
- [Hu & Shu (2025)](/sources/hu-2025.md) — §1; Thms. 4.3, 5.1; §6 (Fig. 1); App. 7.3 (Def. 7.3, Thm. 7.4, Eq. (7.3)); arXiv v1.
- [Ma et al. (2026)](/sources/ma-2026.md) — §1, Thm. 3.3, Cor. 3.1; arXiv v1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §1; §2.2; §3.1 (strong and weak AP, AA, L-stability); Thms. 3.4, 3.7 (Assumptions 3.2–3.6); §5.4; HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §1 (AP and AA definitions), §2.2 (Eqs. (23)–(24)), §4.2, §5; arXiv v5.
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §3.1 (Eqs. (20), (27), (37)–(47)); arXiv v1.
- [Boscheri & Thomann (2024)](/sources/boscheri-2024.md) — §1, §3.2, §4.7; arXiv v1.
- [Birke et al. (2024)](/sources/birke-2024.md) — Abstract (AP claim); arXiv v1.
- [Toh et al. (2026)](/sources/toh-2026.md) — §2, §3 (Eqs. (41)–(42)), §3.1 (Eqs. (43)–(50)), §3.5.
- [Southworth et al. (2024)](/sources/southworth-2024.md) — §5.1 (AP requirement attributed to Pareschi–Russo, their ref. [27]).
