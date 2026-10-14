---
type: Result
title: "Three-term recurrences of the classical polynomials"
description: "The recurrences p_{n+1}=(A_n x+B_n)p_n-C_n p_{n-1} of the Legendre, Chebyshev, Hermite, Laguerre and associated Laguerre polynomials (and the Legendre functions of the second kind and Bessel functions in their order), as stated family by family in both founding sources; their use to evaluate p_n(x) from p_0 and p_1, and what the sources leave out."
status: established
aliases: [recurrence relations, three-term recurrence relation, recurrence formula]
tags: [recurrence, evaluation, classical-family]
timestamp: 2026-10-14T00:00:00Z
---

# Three-term recurrences of the classical polynomials

## Statements

Each classical family obeys a recurrence linking three consecutive degrees.
Both founding sources state them family by family:

| Family | Recurrence | Locators |
|---|---|---|
| Legendre | $(n+1)P_{n+1}=(2n+1)\,x\,P_n-n\,P_{n-1}$ | Riley eq. 18.27, p. 586; Arfken eq. 15.18, p. 718 |
| Legendre, 2nd kind | $(n+1)Q_{n+1}=(2n+1)\,x\,Q_n-n\,Q_{n-1}$ | Riley pp. 579–580 (scale chosen for this, eqs. 18.5–18.6); Arfken eq. 15.158, p. 767 |
| associated Legendre ($m$ fixed) | $(\ell-m+1)P_{\ell+1}^m=(2\ell+1)\,x\,P_\ell^m-(\ell+m)P_{\ell-1}^m$ | Riley eq. 18.42, p. 592; Arfken eq. 15.84, p. 744 |
| Chebyshev I | $T_{n+1}=2x\,T_n-T_{n-1}$ | Riley eq. 18.69, p. 601; Arfken eq. 18.92, p. 901 |
| Chebyshev II | $U_{n+1}=2x\,U_n-U_{n-1}$ | Riley eq. 18.70, p. 601; Arfken eq. 18.93, p. 901 |
| Hermite | $H_{n+1}=2x\,H_n-2n\,H_{n-1}$ | Riley eq. 18.134, p. 628; Arfken eqs. 12.23, 18.3 |
| Laguerre | $(n+1)L_{n+1}=(2n+1-x)L_n-n\,L_{n-1}$ | Riley eq. 18.115, p. 620; Arfken eq. 18.51, p. 890 |
| associated Laguerre | $(n+1)L_{n+1}^{(m)}=(2n+m+1-x)L_n^{(m)}-(n+m)L_{n-1}^{(m)}$ | Riley eq. 18.124, p. 624; Arfken eq. 18.66, p. 894 |
| Bessel (in the order) | $J_{\nu+1}=\frac{2\nu}{x}J_\nu-J_{\nu-1}$ | Riley eq. 18.97, p. 612; Arfken eq. 14.7, p. 646 |
| spherical Bessel | $f_{\ell+1}=\frac{2\ell+1}{x}f_\ell-f_{\ell-1}$ | Arfken eq. 14.169, p. 702 |

The associated Legendre recurrence at fixed $m$ is unchanged by the
Condon–Shortley phase; the recurrences that change $m$ are on
[associated Legendre functions](/definitions/associated-legendre-functions.md).
$V_n$ obeys the $T_n$ recurrence (Arfken et al., Exercise 18.4.9).

**Derivations.** Riley et al. derive the Legendre, Hermite and Laguerre
relations from the generating functions and the Chebyshev ones from
$\cos(n\pm1)\theta=\cos n\theta\cos\theta\mp\sin n\theta\sin\theta$ and the
sine analogue (pp. 586, 601–602, 620); Arfken et al. derive them all from
the generating functions (pp. 556, 718, 890, 901). See
[generating functions](/results/generating-functions.md).

## Use for evaluation

Both books recommend the recurrence as the way to compute values: start from
$p_0(x)$ and $p_1(x)$ at the point $x$ and iterate. Riley et al. say this of
the Legendre (p. 586), Chebyshev ("extremely useful in the practical
computation", p. 602) and Hermite (p. 628) recurrences; Arfken et al. of the
Legendre (eq. 15.19, p. 718), Hermite (p. 556) and Bessel (p. 646) ones. For
the associated Legendre functions Arfken et al. start the recursion in $\ell$
from the closed forms $P_m^m$ and $P_{m+1}^m$ (Example 15.4.1, p. 745).

**What the sources do not say.** Neither book discusses the rounding-error
behaviour of these recursions: there is no statement about forward or
backward stability for any of them, including the Bessel recursion in the
order. Neither book states the general theorem that every orthogonal
polynomial sequence obeys a three-term recurrence, nor its converse, nor the
link between the recurrence coefficients and the Gauss nodes. These are left
for sources that treat them.

## Derivative relations

Companion relations used with the recurrences (both books unless marked):
$P_{n+1}'-P_{n-1}'=(2n+1)P_n$ and $(1-x^2)P_n'=n(P_{n-1}-xP_n)$ (Riley
eqs. 18.25–18.26, p. 586; Arfken eqs. 15.22, 15.25, p. 719);
$T_n'=nU_{n-1}$ (Riley p. 602); $H_n'=2nH_{n-1}$; $xL_n'=n(L_n-L_{n-1})$;
$J_{\nu-1}-J_{\nu+1}=2J_\nu'$. Arfken et al. show that any functions obeying
the Legendre recurrences (Exercise 15.1.1) or the two Bessel recurrences
(eqs. 14.13–14.14, pp. 646–647) satisfy the corresponding differential
equation.

# Citations

1. [Riley et al. (2006)](/sources/riley-2006.md), eqs. 18.18–18.27, pp. 585–586; eqs. 18.41–18.44, p. 592; eqs. 18.69–18.72, pp. 601–602; eqs. 18.92–18.97, pp. 611–612; eqs. 18.115–18.117, p. 620; eqs. 18.124–18.125, p. 624; eqs. 18.134–18.135, p. 628.
2. [Arfken et al. (2013)](/sources/arfken-2013.md), eqs. 12.23–12.24, p. 556; eqs. 14.7–14.14, pp. 646–647; eq. 14.169, p. 702; eqs. 15.18–15.26, pp. 718–719; eqs. 15.84, 15.158; eqs. 18.3–18.4, 18.51–18.52, 18.66, 18.92–18.96.
