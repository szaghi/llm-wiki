---
type: Operator
title: "Logarithmic mean"
description: "The logarithmic mean of two positive numbers, the jump of a quantity divided by the jump of its logarithm, makes two-point fluxes entropy-conservative for entropies with logarithmic terms; the page gives its identity and mean inequalities, its stable, division-reduced and truncated evaluations, its cost, an exponential variant, and the fluxes that use it."
status: established
symbol: "$\\{\\!\\{a\\}\\!\\}_{\\log}$"
aliases: [log mean, Ismail–Roe mean, inverse logarithmic mean]
tags: [entropy-stable, numerical-flux, dg, kinetic-energy-preserving]
timestamp: 2026-10-23T23:00:00Z
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
$\sqrt{a^-a^+}\le\{\!\{a\}\!\}_{\log}\le\{\!\{a\}\!\}$, strictly for $a^-\ne a^+$,
as [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) recall from
Carlson (Eq. (5); arXiv v2) *(compiler check, not in the sources: with
$a^\pm=c\,e^{\pm t/2}$, $t\ge0$ by symmetry, the three means are $c$,
$c\,2\sinh(t/2)/t$ and $c\cosh(t/2)$, and the inequalities reduce to
$t/2\le\sinh(t/2)$ and $\tanh(t/2)\le t/2$)*. Applied to $1/a$, the same
chain gives (Eq. (7))

$$\frac{a^-a^+}{\{\!\{a\}\!\}}\le\Big(\{\!\{1/a\}\!\}_{\log}\Big)^{-1}\le\sqrt{a^-a^+},$$

harmonic mean on the left, geometric on the right. With the page-local
relative jump $\mathsf j_a=[\![a]\!]/(2\{\!\{a\}\!\})$, $\lvert\mathsf j_a\rvert<1$,
the geometric mean is $\{\!\{a\}\!\}(1-\mathsf j_a^2)^{1/2}$ and the harmonic
mean $\{\!\{a\}\!\}(1-\mathsf j_a^2)$ (Eqs. (6), (8)).

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
  Gouasmi-type flux Renac re-derives needs $n_c+1$ (Remark 3.1, Eq. (24),
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

**Exponential means for vibrational energy.** [Peyvan et al. (2023)](/sources/peyvan-2023.md)
need, for the entropy-conservative flux of air with a harmonic-oscillator
vibrational energy, the jump of $\ln(e^{T^{\mathrm v}_ka}-1)$ with
$a=1/T$ and page-local characteristic temperature $T^{\mathrm v}_k$ of
species $k$ (§3, Eqs. (78)–(87); arXiv v1). They define two page-local
means,

$$\{\!\{a\}\!\}_{\exp,k}=\frac{[\![a]\!]}{[\![e^{T^{\mathrm v}_ka}]\!]},\qquad \{\!\{a\}\!\}_{\ln\exp,k}=\{\!\{e^{T^{\mathrm v}_ka}-1\}\!\}_{\log}\,\{\!\{a\}\!\}_{\exp,k},$$

so that $[\![\ln(e^{T^{\mathrm v}_ka}-1)]\!]=[\![a]\!]/\{\!\{a\}\!\}_{\ln\exp,k}$:
the logarithmic-mean identity applied to $e^{T^{\mathrm v}_ka}-1$, whose jump
is that of $e^{T^{\mathrm v}_ka}$. For $a^-\approx a^+$ the exponential mean is
evaluated, after the device of Winters et al. used for the logarithmic
mean, by writing $a^\pm=\{\!\{a\}\!\}(1\pm\mathsf j_a)$:

$$\{\!\{a\}\!\}_{\exp,k}=\frac{1}{T^{\mathrm v}_k\,e^{T^{\mathrm v}_k\{\!\{a\}\!\}}}\,\frac{x}{\sinh x},\qquad x=T^{\mathrm v}_k\{\!\{a\}\!\}\mathsf j_a,$$

with $\sinh x/x$ replaced by its series $1+x^2/3!+x^4/5!+x^6/7!$ (Eq. (87)).
No switching threshold is printed. The flux is on
[entropy-conservative fluxes](/methods/entropy-conservative-flux.md).

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

**Truncation by design.** De Michele & Coppola (2023b) write the same
expansion exactly, $[\![\ln a]\!]=\frac{[\![a]\!]}{\{\!\{a\}\!\}}\sum_{n\ge0}\frac{\mathsf j_a^{2n}}{2n+1}$,
so $\{\!\{a\}\!\}_{\log}=\{\!\{a\}\!\}\big/\sum_{n\ge0}\mathsf j_a^{2n}/(2n+1)$
(Eqs. (11)–(12)), recalling that Ismail & Roe used such an expansion to
remove the singularity. Since $f_{\mathrm r}=-\mathsf j_a$, it is the series
of Algorithm 1 with $\varsigma=\mathsf j_a^2$ *(compiler check, not in the
sources)*. Instead of switching to it near $a^-=a^+$, they truncate it at a
fixed order $N_{\mathrm T}$ (page-local) everywhere, which gives purely algebraic fluxes whose
entropy error decreases as $N_{\mathrm T}$ grows; the zeroth-order truncation of
$\big(\{\!\{1/e\}\!\}_{\log}\big)^{-1}$ is the harmonic mean of $e$ (§4, Eq.
(13); [entropy-conservative fluxes](/methods/entropy-conservative-flux.md)).
They state that this is cheaper than the logarithmic mean and avoids the
local treatment against division by zero, without timings (§1, §6).

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
  of density or temperature cannot evaluate these fluxes; Renac pairs the
  flux with a positivity-preserving scheme and limiter for that reason
  ([bound preservation](/properties/bound-preservation.md)).
- The series branch of Algorithms 1–3 is given without an error bound in
  Ranocha et al. (2023).
- Peyvan et al. print the $\sinh$ argument of their Eq. (86) as
  $T^{\mathrm v}_k\mathsf j_a$ and the remainder of Eq. (87) as $O(x^9)$; the
  argument is $T^{\mathrm v}_k\{\!\{a\}\!\}\mathsf j_a$, as their Eq. (87) uses,
  and the remainder of an even series truncated after $x^6$ is $O(x^8)$
  *(compiler check, not in the sources)*.

# Citations

- [Ranocha et al. (2023)](/sources/ranocha-2023.md) — §3.1 Eq. (3.3), Algorithms 1–3, §3.2 Eqs. (3.10)–(3.11), §7.2 Fig. 6.
- [Renac (2021)](/sources/renac-2021.md) — §3.1 Eq. (24), Remark 3.1, App. B (arXiv v3).
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — §3.3 Eq. (3.15), §3.4 (arXiv v1).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — App. A Eqs. (102)–(103) (arXiv v1).
- [Duan & Tang (2022)](/sources/duan-2022.md) — §2, §3.1 (arXiv v1).
- [Edoh (2022)](/sources/edoh-2022.md) — §3.2, Table 3.
- [De Michele & Coppola (2023b)](/sources/demichele-2023-b.md) — §1, §3 Eqs. (5)–(8), §4 Eqs. (11)–(13), §6 (arXiv v2).
- [Peyvan et al. (2023)](/sources/peyvan-2023.md) — §3 Eqs. (76)–(87) (arXiv v1).
