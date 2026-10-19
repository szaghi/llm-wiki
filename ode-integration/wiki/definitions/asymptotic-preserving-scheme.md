---
type: Definition
title: "Asymptotic-preserving scheme"
description: "A discretization of a problem with small scale parameter ε is asymptotic-preserving when its ε→0 limit at fixed step and mesh is a consistent, stable scheme for the limit model; the page covers the definition, the uniform-accuracy argument, the time-integration mechanisms and the step-size restrictions they remove."
status: established
aliases: [AP scheme, AP property, asymptotic preserving, AP in time, stochastic asymptotic-preserving, sAP]
tags: [asymptotic-preserving, stiff, imex, kinetic, splitting]
timestamp: 2026-10-19T12:00:00Z
---

# Asymptotic-preserving scheme

A multiscale problem carries a small parameter $\varepsilon$ (a relaxation time,
Knudsen, Mach or scaled Debye number, a semiclassical $\hbar$) such that, as
$\varepsilon\to0$, its solutions converge to those of a reduced *limit model*
(hydrodynamic, diffusive, classical). A discretization with numerical parameters
held fixed (step size $h$, mesh width $\Delta x$, or other) is
**asymptotic-preserving (AP)** if its own limit as $\varepsilon\to0$, at those fixed
parameters, exists and is a consistent and stable discretization of the limit model
([Jin (2022)](/sources/jin-2022.md), §1, Fig. 1.2(a)). An AP scheme therefore needs no
resolution of the $\varepsilon$-scale to stay stable, and it changes from a solver of
the micro model into a solver of the macro model "automatically" when the small
scales are not resolved. In the ODE setting of
[Gottlieb et al. (2022)](/sources/gottlieb-2022.md) (§3.4) the property reads: for fixed
$h$, as $\varepsilon\to0$, the scheme reduces to a high-order discretization of the
limiting system. Jin (2022) says the term was coined in Jin (1999). The idea came from
capturing steady neutron transport in the diffusive regime (Larsen, Morel & Miller 1987),
as he recalls it (§1, p. 417).

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
goals, not part of the definition.

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
BGK, Broadwell and the Jin–Xin-type hyperbolic relaxation system satisfy property 5
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
| Diffusive limit of linear transport | — | limit is an explicit diffusion scheme, $h=O(\Delta x^2)$ uniformly in $\varepsilon$ (§5.4) |
| Diffusive limit, Boscarino–Pareschi–Russo (2013) reformulation | — | limit is an implicit diffusion scheme, $h=O(\Delta x)$ (p. 457) |
| Stochastic-Galerkin micro–macro scheme | — | $h\le\frac{\sigma_{\min}}3\Delta x^2+\frac{2\varepsilon}3\Delta x$ (Thm. 5.6) |

For the last row, $\sigma_{\min}$ is the lower bound of the scattering cross-section
(page-local). The Boscarino–Pareschi–Russo reformulation adds and subtracts a
diffusion term $\mu(\varepsilon)v^2\partial_{xx}r/\sigma$ ($\mu(\varepsilon)\in[0,1]$,
$\mu(0)=1$; page-local). It treats the added copy implicitly within an IMEX Runge–Kutta
scheme, and $\mu=1$ gives the largest stability region (Jin 2022, eqs. (5.37)–(5.38)).

## Not every AP scheme is AP for every use

- **Initial layers and well-prepared data.** The first-order BGK-penalization IMEX scheme
  is AP only after an initial transient: the numerical distribution comes within
  $O(\varepsilon)$ of the local Maxwellian only after some steps when the data are not near
  equilibrium. A two-step successive
  penalization reaches the limit in one step (Jin 2022, §5.1, Remark 5.1; see
  [BGK penalization](/methods/bgk-penalization.md)). Gottlieb et al. (2022, Remark 2), in
  contrast, claim AP for arbitrary initial data.
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
  where $\le$ is meant.
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
  classification that means an invertible implicit matrix, but their implicit matrix $A$ is
  singular ($d_{ii}=0$ on some stages). The extension rests on the joint condition
  $d_{ii}+\lvert\dot d_{ii}\rvert>0$.

# Citations

- [Jin (2022)](/sources/jin-2022.md) — §1 (definition, Fig. 1.2, eqs. (1.1)–(1.6)); §3.1–3.3 (time-splitting spectral, Thm. 3.1, Example 3.3, Remark 3.2); §4.1 (AP in $N$); §5.1–5.2 (penalization, exponential reformulation, Remark 5.1); §5.4 (parity, micro–macro, Boscarino–Pareschi–Russo); §5.5 (sAP, Thm. 5.6); §5.7 (APNN, Remark 5.10); §6.1, §6.2, §6.5.
- [Gottlieb et al. (2022)](/sources/gottlieb-2022.md) — §3.4.1 (Properties 1–5, eqs. (19)–(28)); §3.4.2 (Prop. 1, eqs. (49)–(51)); Remarks 2 and 4; §3.5 (numerical regimes).
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §4.4 (IMDeC, IMADER), §5.3 (stiff tests).
