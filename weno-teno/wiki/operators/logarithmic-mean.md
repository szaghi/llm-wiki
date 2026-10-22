---
type: Operator
title: "Logarithmic mean"
description: "The logarithmic mean of two positive numbers, the jump of a quantity divided by the jump of its logarithm, is the mean that makes two-point fluxes entropy-conservative for entropies with logarithmic terms; the page gives its identity, its stable and division-reduced evaluation, its cost, and the fluxes that use it."
status: established
symbol: "$\\{\\!\\{a\\}\\!\\}_{\\log}$"
aliases: [log mean, Ismail–Roe mean, inverse logarithmic mean]
tags: [entropy-stable, numerical-flux, dg, kinetic-energy-preserving]
timestamp: 2026-10-22T18:00:00Z
---

# Logarithmic mean

For two positive numbers $a^-$, $a^+$ the logarithmic mean is

$$\{\!\{a\}\!\}_{\log}=\frac{[\![a]\!]}{[\![\ln a]\!]}=\frac{a^+-a^-}{\ln a^+-\ln a^-},\qquad \{\!\{a\}\!\}_{\log}=a\ \text{ if }a^-=a^+=a .$$

[Ranocha et al. (2023)](/sources/ranocha-2023.md) (Eq. (3.3)),
[Renac (2021)](/sources/renac-2021.md) (§3.1) and
[Duan & Tang (2022)](/sources/duan-2022.md) (§3.1) attribute it to Ismail
& Roe.
It is symmetric in its arguments and consistent. It lies between the
geometric and the arithmetic mean,
$\sqrt{a^-a^+}\le\{\!\{a\}\!\}_{\log}\le\{\!\{a\}\!\}$ *(compiler check, not in the
sources: with $a^\pm=c\,e^{\pm t/2}$, $t\ge0$ by symmetry, the three means are $c$,
$c\,2\sinh(t/2)/t$ and $c\cosh(t/2)$, and the inequalities reduce to
$t/2\le\sinh(t/2)$ and $\tanh(t/2)\le t/2$)*.

## Why entropy-conservative fluxes need it

The entropy variables of the Euler equations, and of their multicomponent
and stiffened-gas relatives, contain $\ln\rho$ and $\ln T$ (or $\ln p$).
Tadmor's condition $[\![w]\!]\cdot f^{\mathrm{ec}}=[\![\psi]\!]$ is linear in
jumps, so each logarithmic jump has to be written as a mean times a plain
jump. The defining identity does exactly this,

$$[\![\ln a]\!]=\frac{[\![a]\!]}{\{\!\{a\}\!\}_{\log}},$$

next to the product rule $[\![ab]\!]=\{\!\{a\}\!\}[\![b]\!]+\{\!\{b\}\!\}[\![a]\!]$.
[Li, Duan & Tang (2022)](/sources/li-2022-c.md) derive their
entropy-conservative stiffened-gas fluxes this way. They express the jumps
of the entropy variables in the parameter vector $(\rho,v,1/T)$ with these
two identities and solve the resulting linear system for the flux
(§3.3.1, Eq. (3.15)). Ranocha et al. (2023) cite the literature for the
remark that the logarithmic mean is "even necessary" if some further
properties are wanted (§3.1).

## Fluxes that use it

- **Ranocha flux** (Euler; entropy-conservative, kinetic-energy- and
  pressure-equilibrium-preserving): mass flux $\{\!\{\rho\}\!\}_{\log}\{\!\{v\cdot n\}\!\}$,
  and the internal-energy term carries $1/\{\!\{\rho/p\}\!\}_{\log}$
  (Ranocha et al. (2023), Eq. (3.10)).
- **Chandrashekar-type fluxes.** Li, Duan & Tang (2022) use
  $\{\!\{\rho\}\!\}_{\log}$ and $\{\!\{1/T\}\!\}_{\log}$ for one stiffened gas, and the
  logarithmic means of both partial densities for two components (§3.3).
  For GLM-MHD, the Derigs et al. flux used by
  [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) carries the
  logarithmic means of $\rho$ and of $\rho/(2p)$ (App. A, Eqs. (102)–(103)).
- **Multicomponent Euler.** Renac's flux needs three logarithmic means, of
  the density of the last component, of the mixture density and of
  $1/T$, whatever the number $n_c$ (page-local) of components. The
  Gouasmi-type flux he re-derives needs $n_c+1$ (Remark 3.1, Eq. (24),
  App. B). Renac counts this as a cost saving for $n_c>2$, and as a
  robustness gain because the logarithmic mean "requires positive
  arguments to avoid floating point exceptions": fewer means, fewer
  chances of such an exception.
- **Relativistic MHD.** The entropy-conservative state that Duan & Tang
  (2022) add to the Cartesian flux on moving meshes contains the
  logarithmic means of the rest-mass density $\rho$ and of $\rho/p$, its
  mass component being $\{\!\{\rho\}\!\}_{\log}\{\!\{W\}\!\}$ with $W$ the Lorentz
  factor (§3.1); the entropy variables of relativistic flows contain
  $\ln(p\rho^{-\gamma})$ as in the classical case (§2).
- **Interface states.** Li, Duan & Tang (2022) also average with
  logarithmic means when they evaluate the scaled eigenvectors at an
  interface, e.g. $\bar\rho=\{\!\{\rho\}\!\}_{\log}$ and
  $\bar T=1/\{\!\{1/T\}\!\}_{\log}$ (§3.4).

The flux formulas are on
[entropy-conservative two-point fluxes](/methods/entropy-conservative-flux.md).

**Other density averages.** Kinetic-energy-preserving split forms that do
not aim at entropy conservation average the density arithmetically
(Feiereisen, Coppola, Kennedy–Gruber) or geometrically: the splittings of
Rozema et al. and the Div-rot and Div-str splittings of
[Edoh (2022)](/sources/edoh-2022.md) work in square-root-density
variables, so their two-point mass fluxes carry $\sqrt{\rho^-\rho^+}$-type
averages (§3.2, Table 3;
[split convective forms](/methods/split-convective-forms.md)). Since the
logarithmic mean lies between the geometric and the arithmetic mean, it
sits between these two families *(compiler check, not in the sources)*.

## Evaluation

The formula is a $0/0$ form as $a^-\to a^+$ and loses accuracy nearby.
As recalled by Ranocha et al. (2023), §3.1, Algorithm 1 of Ismail & Roe
sets $\xi_{\mathrm r}=a^-/a^+$, $f_{\mathrm r}=(\xi_{\mathrm r}-1)/(\xi_{\mathrm r}+1)$
and $\varsigma=f_{\mathrm r}^2$ (all page-local), and returns
$(a^-+a^+)/(2F)$ with

$$F=\begin{cases}1+\varsigma/3+\varsigma^2/5+\varsigma^3/7,&\varsigma<10^{-4},\\ \dfrac{\ln\xi_{\mathrm r}}{2f_{\mathrm r}},&\text{otherwise},\end{cases}$$

the threshold being for 64-bit arithmetic. The series is that of
$\ln\xi_{\mathrm r}=2\operatorname{artanh}f_{\mathrm r}$ *(compiler check, not in the
sources)*.

Ranocha et al.'s Algorithm 2 computes $\varsigma$ with one division,
$\varsigma=\big(a^-(a^--2a^+)+(a^+)^2\big)/\big(a^-(a^-+2a^+)+(a^+)^2\big)$. It
returns $(a^-+a^+)/\big(2+\varsigma(2/3+\varsigma(2/5+\varsigma\,2/7))\big)$
below the threshold and $(a^+-a^-)/\ln(a^+/a^-)$ above it. Algorithm 3
returns the *inverse* logarithmic mean $1/\{\!\{a\}\!\}_{\log}$ in the same way,
which the Ranocha flux needs. A variant multiplies by a Taylor polynomial
instead of dividing; it gives no significant difference on the authors'
hardware.

**Cost.** Logarithms dominate. On the authors' 2019 laptop $\ln x+\ln y$
took $11.5\pm3.8$ ns against $1.7\pm0.4$ ns for $2x+3y$. Precomputing
$\ln\rho$ and $\ln p$ once per node cuts the number of logarithms of a
flux-differencing DG element from $O(d(N+1)^{d+1})$ to $O((N+1)^d)$, for a
speed-up of about 10 % to 75 % depending on the data (Ranocha et al.
(2023), §7.2, Fig. 6). The isentropic-vortex benchmark of the paper uses a strong vortex so that
"all possible paths in the logarithmic mean are followed".

## Qualifications

- The argument must be positive. A scheme whose states can lose positivity
  of density or temperature cannot evaluate these fluxes; Renac pairs his
  flux with a positivity-preserving scheme and limiter for that reason
  ([bound preservation](/properties/bound-preservation.md)).
- The series branch of Algorithms 1–3 is given without an error bound in
  Ranocha et al. (2023).

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §3.1 Eq. (3.3), Algorithms 1–3, §3.2 Eqs. (3.10)–(3.11), §7.2 Fig. 6.
- [Renac (2021)](/sources/renac-2021.md) — §3.1 Eq. (24), Remark 3.1, App. B (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §3.3 Eq. (3.15), §3.4 (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — App. A Eqs. (102)–(103) (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2, §3.1 (arXiv v1).
- [Edoh (2022)](/sources/edoh-2022.md) — §3.2, Table 3.
