---
type: Result
title: "Legendre expansion of the inverse distance (axial multipole expansion)"
description: "1/|r-r'| = sum_l r_<^l / r_>^{l+1} P_l(cos gamma), the Legendre generating function read geometrically; converges except at r=r'; gives the axial multipole expansion, whose lowest non-vanishing moment alone is independent of the expansion centre."
status: established
aliases: [multipole expansion, expansion of 1/|r1-r2|, Legendre generating function, axial multipole moments]
tags: [legendre, multipole, generating-function, potential-theory]
timestamp: 2026-10-14T00:00:00Z
---

# Legendre expansion of the inverse distance (axial multipole expansion)

## Statement

For points $\mathbf r$, $\mathbf r'$ at distances $r$, $r'$ from the origin,
with $\gamma$ the angle between them, $r_<=\min(r,r')$ and $r_>=\max(r,r')$,
$$\frac{1}{|\mathbf r-\mathbf r'|}=\frac{1}{(r^2+r'^2-2rr'\cos\gamma)^{1/2}}=\frac1{r_>}\sum_{\ell=0}^\infty\Big(\frac{r_<}{r_>}\Big)^\ell P_\ell(\cos\gamma).$$
It is the Legendre generating function
$(1-2xt+t^2)^{-1/2}=\sum_\ell P_\ell(x)t^\ell$ with $x=\cos\gamma$ and
$t=r_</r_>$ ([Riley et al. (2006)](/sources/riley-2006.md), eq. 18.22,
p. 585; [Arfken et al. (2013)](/sources/arfken-2013.md), §15.3,
eqs. 15.58–15.63, pp. 736–737). Riley et al. write it for $r'<r$ and say
that $r$ and $r'$ "must be exchanged … or the series would not converge"
(pp. 585–586); Arfken et al. state the combined form and that it "will
converge everywhere except when $r_1=r_2$", with convergence improving as
$r_>/r_<$ grows (pp. 736–737). Neither book gives a truncation error bound.
Since $|P_\ell|\le1$ on $[-1,1]$ (see
[Legendre polynomials](/definitions/legendre-polynomials.md)), the remainder
after $L$ terms is bounded by $\frac1{r_>}\frac{(r_</r_>)^{L+1}}{1-r_</r_>}$
(compiler's derivation, geometric-series bound; hypothesis-grade as a
citation).

## Multipole expansion

For charges $q_i$ at $z=a_i$ on the polar axis, summing the expansions gives,
for $r>\max_i|a_i|$,
$$\psi=\frac{1}{4\pi\varepsilon_0r}\Big[\mu_0+\frac{\mu_1}{r}P_1(\cos\theta)+\frac{\mu_2}{r^2}P_2(\cos\theta)+\cdots\Big],\qquad \mu_\ell=\sum_iq_ia_i^\ell,$$
the **multipole moments** (monopole $\mu_0$, dipole $\mu_1$, quadrupole
$\mu_2$, …), each term the potential of a point $2^\ell$-pole
([Arfken et al. (2013)](/sources/arfken-2013.md), eq. 15.67, p. 739, after the
dipole and quadrupole constructions, eqs. 15.64–15.66, Figs. 15.6–15.7). The expansion
converges at points farther from the origin than every charge (p. 739).

**Dependence on the centre.** Shifting the expansion centre leaves only the
lowest non-vanishing moment unchanged: the total charge always, the dipole
moment only when the net charge vanishes, the quadrupole only when charge
and dipole both vanish (Arfken et al., p. 739). They add that the expansion
holds for any inverse-square interaction (mass multipoles, gravitational
radiation) and that continuous distributions replace sums by integrals.

**Scope.** Both books present the axial case. The extension to arbitrary
directions needs the spherical harmonics: Arfken et al. defer it to their
chapter 16, outside this bundle's reading (pp. 738–739), and Riley et al.
give only the potential of a point charge (p. 586). The off-axis form
follows from the
[spherical harmonic addition theorem](/results/spherical-harmonic-addition-theorem.md).
Arfken et al. use axial expansions of this kind, with coefficients fixed on
the symmetry axis, for a charged ring (Example 15.2.3, pp. 729–730) and a
current loop (Example 15.4.2, pp. 748–753), and fit Earth's gravitational
potential with Legendre series (Example 15.2.1, p. 727).

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), §18.1.2, eq. 18.22, pp. 585–586.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), §15.3, eqs. 15.58–15.67, pp. 736–739; Examples 15.2.1, 15.2.3, 15.4.2.
