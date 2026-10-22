---
type: Method
title: "Entropy-conservative and kinetic-energy-preserving two-point fluxes"
description: "Two-point fluxes that satisfy Tadmor's jump condition between entropy variables and flux potentials conserve entropy, and entropy-dissipative fluxes satisfy it as an inequality; the page states the condition in Cartesian and directional form, gives the Ranocha, Shima et al. and scalar KPP fluxes, and the logarithmic mean with its division-reduced evaluation."
status: established
aliases: [EC flux, entropy-conservative flux, entropy-dissipative flux, ED flux, Tadmor flux, KEP flux, KEEP flux, Ranocha flux, Shima flux, logarithmic mean]
tags: [entropy-stable, kinetic-energy-preserving, numerical-flux, dg]
timestamp: 2026-10-21T12:00:00Z
---

# Entropy-conservative and kinetic-energy-preserving two-point fluxes

Let $\eta(u)$ be a convex entropy of $\partial_tu+\sum_d\partial_{x_d}f^{(d)}(u)=0$,
with entropy fluxes $F_\eta^{(d)}$, entropy variables $w=\eta'(u)$ and flux
potentials $\psi^{(d)}=w\cdot f^{(d)}-F_\eta^{(d)}$. A consistent two-point
flux $f^{(d)}(u^-,u^+)$ is **entropy-conservative** (EC) when it satisfies
Tadmor's condition

$$[\![w]\!]\cdot f^{\mathrm{ec},(d)}(u^-,u^+)=[\![\psi^{(d)}]\!],$$

and **entropy-dissipative** (ED) when
$[\![w]\!]\cdot f^{(d)}-[\![\psi^{(d)}]\!]\le0$
([Ranocha et al. (2023)](/sources/ranocha-2023.md), Def. 2.5, after Tadmor).
A **directional** flux $f(u^-,u^+,n)$, consistent with $\sum_dn_df^{(d)}(u)$,
is EC when $[\![w]\!]\cdot f(u^-,u^+,n)=\sum_dn_d[\![\psi^{(d)}]\!]$. It must also
satisfy $f(u^-,u^+,n)=-f(u^+,u^-,-n)$ (Def. 2.4).

## Role in DG

Used as the symmetric volume flux of
[flux differencing](/methods/flux-differencing.md) on a diagonal-norm
[SBP](/operators/summation-by-parts-operator.md) element, an EC flux makes
the volume term entropy-conservative. Pairing it with an EC or ED surface
flux gives an EC or ED DG scheme (Ranocha et al. (2023), §2;
[entropy stability](/properties/entropy-stability.md)).
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) use
two such pairings:

- an EC volume flux with a local Lax–Friedrichs (Rusanov) surface flux on
  the KPP problem (§5.1);
- the Chandrashekar flux in the volume with a Rusanov surface flux for Euler
  (§5.2).

## Fluxes for the compressible Euler equations

Let page-local $(\!(a;b)\!)=\tfrac12(a^+b^-+a^-b^+)$ be the product mean,
with $\{\!\{\cdot\}\!\}$ and $\{\!\{\cdot\}\!\}_{\log}$ the arithmetic and logarithmic
means of the registry and $n$ the direction. Ranocha et al. (2023) give the
directional forms of two fluxes (§3.2).

**Shima et al. flux** (kinetic-energy- and pressure-equilibrium-preserving,
*not* EC; the "cheap" flux; Eq. (3.7)):

$$\begin{aligned}
f_\rho&=\{\!\{\rho\}\!\}\{\!\{v\cdot n\}\!\},\qquad f_{\rho v}=f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\}\,n,\\
f_E&=f_\rho\tfrac12(\!(v;v)\!)+\frac{\{\!\{p\}\!\}\{\!\{v\cdot n\}\!\}}{\gamma-1}+(\!(p;v\cdot n)\!).
\end{aligned}$$

**Ranocha flux** (EC, kinetic-energy- and pressure-equilibrium-preserving;
the "expensive" flux; Eq. (3.10)):

$$\begin{aligned}
f_\rho&=\{\!\{\rho\}\!\}_{\log}\{\!\{v\cdot n\}\!\},\qquad f_{\rho v}=f_\rho\{\!\{v\}\!\}+\{\!\{p\}\!\}\,n,\\
f_E&=f_\rho\tfrac12(\!(v;v)\!)+\frac{f_\rho}{(\gamma-1)\{\!\{\rho/p\}\!\}_{\log}}+(\!(p;v\cdot n)\!).
\end{aligned}$$

The properties of both fluxes are cited from the literature, not proved
in the paper (§3.2). A division-saving rewrite of the last term uses
$1/\{\!\{\rho/p\}\!\}_{\log}=p^+p^-/\{\!\{\rho p\}\!\}^{\times}_{\log}$. Here
$\{\!\{\rho p\}\!\}^{\times}_{\log}$ (page-local) is the logarithmic mean of the two
numbers $\rho^+p^-$ and $\rho^-p^+$ (Eq. (3.11)). The same optimizations
apply to the Ismail–Roe and Chandrashekar EC fluxes (§3.2).
Rueda-Ramírez et al. (2022) describe the Chandrashekar flux as EC and
kinetic-energy-preserving, and use its MHD relative, the
Chandrashekar–Klingenberg flux, for GLM-MHD (§4, §5.3).

**Shared structure** *(compiler check, not in the sources)*. Both fluxes
share three features:

- The momentum flux is the mass flux times the arithmetic mean of the
  velocity, plus a central pressure.
- The kinetic part of the energy flux is $\tfrac12f_\rho\,v^-\cdot v^+$,
  since $(\!(v;v)\!)=v^-\cdot v^+$.
- They differ only in the mass flux and in the internal-energy term, the
  one carrying $1/(\gamma-1)$; the pressure-work term $(\!(p;v\cdot n)\!)$ is
  common.

This is the structure that
[Coppola & Veldman (2023)](/sources/coppola-2023.md) prove necessary and
sufficient for kinetic-energy preservation of three-point finite-volume
schemes: momentum flux $m_{i+1/2}\{\!\{v\}\!\}$ with a free mass flux $m_{i+1/2}$,
and kinetic-energy flux $\tfrac12m_{i+1/2}v_iv_{i+1}$ (Observation 7). The
Shima et al. mass flux $\{\!\{\rho\}\!\}\{\!\{v\}\!\}$ equals their Kennedy–Gruber–Pirozzoli
face mass flux $\tfrac14(\rho_i+\rho_{i+1})(v_i+v_{i+1})$ ($\zeta=1/2$ on
[split convective forms](/methods/split-convective-forms.md)) *(compiler check, not in the
sources: neither paper makes the identification)*. Coppola &
Veldman add that no finite-difference equivalent of the logarithmic-mean
fluxes of Chandrashekar or Ranocha is known (§5.4). Their in-passing
remark, after Chandrashekar, is that the free mass-flux choice can be used
to induce entropy conservation. See
[kinetic energy preservation](/properties/kinetic-energy-preservation.md).

## Scalar case: the KPP flux

For a scalar law with $\eta=\tfrac12u^2$, the entropy variable is $w=u$,
and Tadmor's condition fixes the flux whenever $u^-\ne u^+$:
$f^{\mathrm{ec},(d)}=[\![\psi^{(d)}]\!]/[\![u]\!]$, with
$f^{\mathrm{ec},(d)}=f^{(d)}(u^-)$ if $u^-=u^+$. For the KPP flux
$f=(\sin u,\cos u)$, the potentials are $\psi=(-\cos u,\sin u)$
(Rueda-Ramírez et al. (2022), Eqs. (39)–(40)). The authors call it "the unique
two-point entropy conservative flux". Uniqueness holds because, for a scalar,
the EC condition is one linear equation in one unknown *(compiler check, not
in the sources)*. It does not carry over to systems.

## The logarithmic mean and its evaluation

The logarithmic mean
$\{\!\{a\}\!\}_{\log}=[\![a]\!]/[\![\ln a]\!]$ (Ismail–Roe) is ill-conditioned
when $a^-\approx a^+$. Ranocha et al. (2023), §3.1, give division-reduced
algorithms. Let page-local $\varsigma=\big((a^+-a^-)/(a^++a^-)\big)^2$, computed with
one division as $\big(a^-(a^--2a^+)+(a^+)^2\big)/\big(a^-(a^-+2a^+)+(a^+)^2\big)$.

- If $\varsigma<10^{-4}$ (64-bit), Algorithm 2 returns
  $\{\!\{a\}\!\}_{\log}\approx(a^-+a^+)/\big(2+\varsigma(2/3+\varsigma(2/5+\varsigma\,2/7))\big)$.
- Otherwise it returns $(a^+-a^-)/\ln(a^+/a^-)$.
- Algorithm 3 computes the inverse logarithmic mean the same way.

The series follows from $\ln(a^+/a^-)=2\operatorname{artanh}\sqrt\varsigma$
*(compiler check, not in the sources)*. The paper's variant (3.6)
multiplies by $\tfrac12+\varsigma\big(-\tfrac16+\varsigma(-\tfrac2{45}-\varsigma\tfrac{22}{945})\big)$.
These are the Taylor coefficients of
$\tfrac12/(1+\varsigma/3+\varsigma^2/5+\varsigma^3/7)$ to $O(\varsigma^3)$
*(compiler check, not in the sources: expand $1/(1+s)$)*. It gives no
significant performance difference on the authors' hardware (§3.1).

Logarithms are expensive. On a 2019 laptop, $\ln x+\ln y$ took
$11.5\pm3.8$ ns against $1.7\pm0.4$ ns for $2x+3y$. Precomputing $\ln\rho$
and $\ln p$ per node cuts the logarithm count from $O(d(N+1)^{d+1})$ to
$O((N+1)^d)$ per element. The resulting speed-up depends on the data: about
10 % for the isentropic vortex, 25–55 % for sinusoidal data and 60–75 % for
random data (§7.2, Fig. 6). In the flux microbenchmarks, LLF and HLL
surface fluxes cost between the Shima and the Ranocha fluxes (§4.2,
Table 2).

## Qualifications

- Ranocha et al. (2023) do not state the entropy sign convention
  explicitly. With a convex mathematical entropy, ED means entropy
  production $\le0$, the convention used here and in the registry
  ($\eta=-\rho s/(\gamma-1)$ for Euler).
- In Ranocha et al.'s Def. 2.4, directional fluxes take unit normals, but
  the curvilinear volume term evaluates them at unnormalized averaged
  contravariant vectors (Eq. (2.19)). The scaling is linear, as their
  rotation Algorithm 4 makes explicit.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — Defs. 2.4–2.5, §2, §3.1 Algorithms 1–3 Eqs. (3.3)–(3.6), §3.2 Eqs. (3.7)–(3.11), §4.2 Table 2, §7.2 Fig. 6.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §2.1, §4, §5.1 Eqs. (39)–(40), §5.2, §5.3.
- [Coppola & Veldman (2023)](/sources/coppola-2023.md) — §5.2 Observation 7, §5.4, Table 1.
