---
type: Method
title: "Micro–macro decomposition"
description: "Asymptotic-preserving reformulation of kinetic equations as an equilibrium part plus an ε-scaled microscopic correction, discretized with only a linear stiff operator implicit; its limit is a scheme for Euler or diffusion equations, with an explicit diffusive limit that keeps a parabolic step restriction uniform in ε."
status: established
aliases: [micro-macro method, micro–macro scheme, Bennoune–Lemou–Mieussens scheme, Lemou–Mieussens scheme]
tags: [asymptotic-preserving, kinetic, stiff, imex]
timestamp: 2026-10-19T00:00:00Z
---

# Micro–macro decomposition

The micro–macro decomposition writes a kinetic distribution as its local equilibrium
plus $\varepsilon$ times a microscopic correction. It then evolves a coupled system: a
macroscopic conservation law for the moments, and a microscopic equation for the
correction. A time discretization that treats only the linear stiff operator of the
microscopic equation implicitly is
[asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md). Its
$\varepsilon\to0$ limit at fixed $h$ and $\Delta x$ is a scheme for the hydrodynamic or
diffusive limit equation ([Jin 2022](/sources/jin-2022.md), §5.3, §5.4.2, reviewing
Bennoune, Lemou & Mieussens 2008 and Lemou & Mieussens 2008). Jin traces the
decomposition to Klar & Schmeiser (2001) for radiative heat transfer and its analysis
to Liu & Yu (2004).

**Page-local notation.** $F(t,x,v)$ is the distribution (sources' $f$). $\mathcal M$ is
the local Maxwellian. $\mathbf m(v)=(1,v,\lvert v\rvert^2/2)^\top$ are the collision
invariants. $g$ is the microscopic part. $\rho$ is the density. $\mathcal M_0(v)$ is the
normalized global Maxwellian of linear transport (sources' $M$, renamed because $M$ is
the mass matrix). $\langle\cdot\rangle_v$ is the velocity average. $\mathcal L$ is the
linear collision (scattering) operator. $\mathbb D$ is the diffusion matrix. Time levels
are subscripts.

## Nonlinear Boltzmann: limit to Euler and Navier–Stokes

With $F=\mathcal M+\varepsilon g$ and $\int\mathbf m(v)(F-\mathcal M)\,dv=0$, let
$\mathcal L_{\mathcal M}g=Q[\mathcal M,g]+Q[g,\mathcal M]$ be the collision operator
linearized at $\mathcal M$. Let $\Pi_{\mathcal M}$ be the projection onto its null space
$\operatorname{span}\{\mathcal M,v\mathcal M,\lvert v\rvert^2\mathcal M\}$. The Boltzmann
equation is equivalent to (Jin 2022, eq. (5.12))

$$\begin{aligned}
&\partial_tg+(I-\Pi_{\mathcal M})(v\cdot\nabla_xg)-Q[g,g]=\frac1\varepsilon\Big[\mathcal L_{\mathcal M}g-(I-\Pi_{\mathcal M})(v\cdot\nabla_x\mathcal M)\Big],\\
&\partial_t\int\mathbf m\,\mathcal M\,dv+\int\mathbf m\,v\cdot\nabla_x\mathcal M\,dv+\varepsilon\,\nabla_x\cdot\int v\,\mathbf m\,g\,dv=0.
\end{aligned}$$

The scheme of Bennoune, Lemou & Mieussens (2008), eq. (5.15), takes the linear stiff
term $\mathcal L_{\mathcal M_n}g_{n+1}$ implicitly and the quadratic term $Q[g_n,g_n]$
and the transport terms explicitly. The macroscopic update then uses the new
$g_{n+1}$:

$$\begin{aligned}
&\frac{g_{n+1}-g_n}{h}+(I-\Pi_{\mathcal M_n})(v\cdot\nabla_xg_n)-Q[g_n,g_n]=\frac1\varepsilon\Big[\mathcal L_{\mathcal M_n}g_{n+1}-(I-\Pi_{\mathcal M_n})(v\cdot\nabla_x\mathcal M_n)\Big],\\
&\int\mathbf m\,\mathcal M_{n+1}\,dv+h\,\varepsilon\int\mathbf m\,v\cdot\nabla_xg_{n+1}\,dv=\int\mathbf m\,\mathcal M_n\,dv-h\int\mathbf m\,v\cdot\nabla_x\mathcal M_n\,dv.
\end{aligned}$$

Each step needs only the inversion of $I-\frac{h}{\varepsilon}\mathcal L_{\mathcal M_n}$,
a linear operator with non-positive spectrum. **Theorem 5.2** (Bennoune et al. 2008, as
recalled by Jin 2022, §5.3) states two limits. (i) As $\varepsilon\to0$ the scheme becomes
a scheme consistent with the compressible Euler equations. (ii) For small $\varepsilon$ it
is asymptotically equivalent, up to $O(\varepsilon^2)$, to an explicit time discretization
of the compressible Navier–Stokes equations. Gamba, Jin & Liu (2019) replace
$\mathcal L_{\mathcal M}$ by a [BGK penalty](/methods/bgk-penalization.md) to avoid
inverting it.

## Linear transport: the diffusion limit

For $\varepsilon\partial_tF+v\cdot\nabla_xF=\frac1\varepsilon\mathcal LF$, write
$F=\rho\,\mathcal M_0+\varepsilon g$ with $\langle g\rangle_v=0$, and let
$\Pi(\cdot)=\mathcal M_0\langle\cdot\rangle_v$. The micro–macro system is (Jin 2022,
eqs. (5.31)–(5.32), Lemou & Mieussens 2008)

$$\partial_t\rho+\nabla_x\cdot\langle vg\rangle_v=0,\qquad
\varepsilon^2\partial_tg+\varepsilon(I-\Pi)(v\cdot\nabla_xg)+v\,\mathcal M_0\cdot\nabla_x\rho=\mathcal Lg .$$

The time discretization (5.33)–(5.34) takes $\mathcal Lg_{n+1}$ implicitly and the
transport terms explicitly. In the continuity equation the flux of $g$ is taken at
$t_{n+1}$ "to recover the correct diffusion limit":

$$\begin{aligned}
&\frac{g_{n+1}-g_n}{h}+\frac1\varepsilon(I-\Pi)(v\cdot\nabla_xg_n)=\frac1{\varepsilon^2}\mathcal Lg_{n+1}-\frac1{\varepsilon^2}v\,\mathcal M_0\cdot\nabla_x\rho_n,\\
&\frac{\rho_{n+1}-\rho_n}{h}+\nabla_x\cdot\langle vg_{n+1}\rangle_v=0 .
\end{aligned}$$

As $\varepsilon\to0$, $\mathcal Lg_{n+1}=v\,\mathcal M_0\cdot\nabla_x\rho_n$. Hence
$g_{n+1}=\mathcal L^{-1}(v\mathcal M_0)\cdot\nabla_x\rho_n$, and the density update becomes
the **forward-Euler** discretization of the diffusion equation
$\partial_t\rho=\nabla_x\cdot(\mathbb D\nabla_x\rho)$. On a staggered grid with upwinded
$v^\pm=(v\pm\lvert v\rvert)/2$ (eqs. (5.35)–(5.36)) the limit is the classical
three-point explicit diffusion scheme. Liu & Mieussens (2010), as recalled by Jin (p. 457),
proved stability under $h\le C\Delta x^2$ **uniformly in $\varepsilon$**.

## The parabolic restriction and how to remove it

The limit time discretization is explicit for the diffusion equation, so the AP scheme
inherits the parabolic restriction $h=O(\Delta x^2)$ in the diffusive regime. Jin (2022,
p. 457) notes that every scheme in this family has this property, including the even/odd
parity scheme of Jin, Pareschi & Toscani (2000). The Boscarino–Pareschi–Russo (2013)
reformulation removes it. It adds and subtracts a diffusion term, treats one copy
implicitly within an [IMEX Runge–Kutta](/methods/imex-runge-kutta.md) scheme, and so
makes the limit an implicit diffusion scheme with $h=O(\Delta x)$ (see
[asymptotic-preserving scheme](/definitions/asymptotic-preserving-scheme.md)).

## Uses beyond deterministic kinetic schemes

- **Stochastic Galerkin (sAP).** With random scattering $\sigma(x,z)\ge\sigma_{\min}>0$, the
  stochastic-Galerkin micro–macro scheme (Jin, Liu & Ma 2017, as recalled by Jin 2022,
  §5.5, eqs. (5.56)–(5.61)) tends to the stochastic-Galerkin scheme of the random diffusion
  limit. It is therefore stochastically AP. Theorem 5.6 gives stability and a discrete energy
  estimate under
  $$h\le\frac{\sigma_{\min}}{3}\Delta x^2+\frac{2\varepsilon}{3}\Delta x,$$
  a step bound that interpolates between a hyperbolic CFL condition for $\varepsilon=O(1)$
  and a parabolic one as $\varepsilon\to0$ ($\sigma$, $\sigma_{\min}$, $z$ page-local).
  The test with $\sigma=2+z$, $\varepsilon=10^{-8}$ shows the difference from the limit
  solution decaying like $\varepsilon^2$ until the discretization error dominates (Fig. 5.2).
- **Asymptotic-preserving neural networks.** Using the micro–macro system, with
  $\langle g\rangle_v=0$ enforced exactly, as the residual loss gives a learned solver whose
  loss tends to that of the diffusion equation. A residual loss on the original kinetic
  equation does not. In Example 5.9 ($\varepsilon=10^{-8}$) the relative $\ell^2$ errors are
  $9.40\times10^{-1}$ for the plain physics-informed network and $2.76\times10^{-3}$ for the
  micro–macro network (Jin 2022, §5.7, Jin, Ma & Wu 2021).

## Qualifications

- The schemes displayed by Jin (2022) are first order in time (forward and backward Euler).
  Their AP statements are formal limits or theorems recalled from the cited papers. None is
  proved in the survey.
- Theorem 5.2 (ii) concerns asymptotic equivalence to an *explicit* Navier–Stokes
  discretization. The Navier–Stokes regime therefore inherits the explicit viscous step
  restriction *(compiler inference, not stated in the source)*.
- Jin's §5.4.2 says the derivation uses "the rotational invariance of $\sigma$" where the
  scattering kernel is meant (printed slip).

# Citations

- [Jin (2022)](/sources/jin-2022.md) — §5.3 (eqs. (5.11)–(5.15), Thm. 5.2); §5.4.2 (eqs. (5.29)–(5.36)); p. 457 (parabolic restriction, Boscarino–Pareschi–Russo); §5.5.3 (Thm. 5.6, eq. (5.62), Figs. 5.1–5.2); §5.7 (APNN, Example 5.9).
