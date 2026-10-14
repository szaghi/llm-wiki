---
type: Source
title: "Riley, Hobson & Bence (2006) — Mathematical Methods for Physics and Engineering, 3rd ed. (Ch. 18 and §27.4)"
description: "Undergraduate textbook read for its special-functions chapter (Legendre, associated Legendre, spherical harmonics with the addition theorem, Chebyshev, Bessel, spherical Bessel, Laguerre, Hermite) and its numerical-integration section (trapezium, Simpson, Gauss–Legendre, Gauss–Chebyshev, Gauss–Laguerre and Gauss–Hermite rules with tables)."
resource: "doi:10.1017/CBO9780511810763"
source_kind: book
authors: [Riley K.F., Hobson M.P., Bence S.J.]
year: 2006
venue: "Cambridge University Press (3rd ed.)"
local_file: "/home/stefano/papers/mosaic/orthogonal-polynomials-and-quadrature/2006-CUP-Riley-101017CBO9780511810763.pdf"
tags: [textbook, special-functions, orthogonal-polynomials, quadrature, scoped-read]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

*Mathematical Methods for Physics and Engineering* (3rd ed., Cambridge
University Press, 2006) is a comprehensive undergraduate text. Its Chapter 18
("Special functions", pp. 577–647) treats the solutions of the second-order
equations listed in its chapters 16–17: for each family it derives the series
solution, the standardization, the Rodrigues formula, mutual orthogonality and
normalization (usually twice, from the Sturm–Liouville form and directly),
the generating function and the recurrence relations, mostly in worked
examples. §27.4 ("Numerical integration", pp. 1000–1018) gives the trapezium
and Simpson rules with Taylor-series error estimates, Gaussian integration
(new in this edition, per the preface: "Gaussian quadrature based on
Legendre, Laguerre, Hermite and Chebyshev polynomials is discussed, and
appropriate tables of points and weights are provided", p. xx), and Monte
Carlo methods.

**Scoped read (bundle law).** Read in full: the preface and contents,
Chapter 18 (§§18.1–18.14, including the exercises and hints) and §27.4
(§§27.4.1–27.4.4). Not read: every other chapter, including the
Sturm–Liouville theory of chapter 17 and the series-solution methods of
chapter 16 to which Chapter 18 refers, and §27.5 onward. §§18.10–18.12
(hypergeometric, confluent hypergeometric, gamma and related functions) and
§27.4.4 (Monte Carlo) were read but are outside the bundle's scope; they enter
only where a page needs them. Text extraction was used throughout; the text
layer renders $\ell$ as "+" and loses many fraction bars, so the equations
used on concept pages were checked against the printed form, and pp. 592,
599, 625, 627, 1006 and 1009 were checked on rendered page images.

Merged into [Legendre polynomials](/definitions/legendre-polynomials.md),
[associated Legendre functions](/definitions/associated-legendre-functions.md),
[spherical harmonics](/definitions/spherical-harmonics.md), the
[addition theorem](/results/spherical-harmonic-addition-theorem.md),
[Chebyshev](/definitions/chebyshev-polynomials.md),
[Hermite](/definitions/hermite-polynomials.md) and
[Laguerre](/definitions/laguerre-polynomials.md) polynomials,
[Bessel](/definitions/bessel-functions.md) and
[spherical Bessel](/definitions/spherical-bessel-functions.md) functions, and
the quadrature methods.

# Key claims

1. **Legendre** (§18.1, pp. 577–586). For integer $\ell$ one series solution
   terminates; with $P_\ell(1)=1$ it is $P_\ell$ (p. 578). Rodrigues formula
   proved (eq. 18.9, p. 581); norm $2/(2\ell+1)$ via
   $K_\ell=\int(1-x^2)^\ell dx$ (eq. 18.11, p. 582); orthogonality proved
   directly from the equation (eq. 18.12, p. 583); Legendre series
   (eqs. 18.13–18.14). Generating function shown to produce Legendre's
   equation and the scale (eqs. 18.15–18.21, pp. 584–585); inverse-distance
   expansion (eq. 18.22); recurrences (eqs. 18.23–18.27), with (18.27)
   recommended for evaluating $P_n(x)$ (p. 586). $Q_\ell$ normalized so that
   it obeys the same recurrences (eqs. 18.5–18.8, pp. 579–580).
2. **Associated Legendre** (§18.2, pp. 587–593). Defined **without** the
   Condon–Shortley phase (eq. 18.32); $P_\ell^{-m}$ relation proved
   (eq. 18.33); orthogonality at fixed $m$ with norm
   $\frac{2}{2\ell+1}\frac{(\ell+m)!}{(\ell-m)!}$ proved (eq. 18.37);
   second orthogonality with weight $(1-x^2)^{-1}$ stated "not of any
   practical use" (eq. 18.39); generating function (eq. 18.40) and four
   recurrences "equally valid for negative and non-negative values of $m$"
   (eqs. 18.41–18.44, p. 592).
3. **Spherical harmonics** (§18.3, pp. 593–595). Defined with an explicit
   $(-1)^m$ (eq. 18.45), orthonormal (eq. 18.46), complete for "any
   reasonable function" (eqs. 18.47–18.48). **Addition theorem** stated and
   proved via closure, a Legendre expansion of $\delta(\Omega-\Omega')$ and
   rotation closure (eqs. 18.49–18.53).
4. **Chebyshev** (§18.4, pp. 595–602). $T_n=\cos(n\arccos x)$,
   $U_n=V_{n+1}/\sqrt{1-x^2}$ (eqs. 18.55–18.58); Rodrigues formulae stated,
   "may be proved in an analogous manner" (p. 599); orthogonality and norms
   (eqs. 18.61–18.62); generating functions (eqs. 18.63–18.64) called "of
   less practical use"; recurrences (eqs. 18.69–18.72) "extremely useful in
   the practical computation" (p. 602); derivative relations.
5. **Bessel** (§18.5, pp. 602–614). Frobenius derivation of $J_\nu$
   (eq. 18.79); $Y_\nu$ (eqs. 18.81–18.82); Hankel functions; orthogonality on
   $[a,b]$ with weight $x$ under boundary conditions (eqs. 18.84–18.88);
   normalization integral (eq. 18.89); Bessel series with
   $J_\nu(\alpha_nb)=0$ (eqs. 18.90–18.91); recurrences (eqs. 18.92–18.97);
   integer-order generating function and integral representation
   (eqs. 18.98–18.99). No asymptotic forms and no modified Bessel functions.
6. **Spherical Bessel** (§18.6, pp. 614–616). $j_\ell$, $n_\ell$
   (eqs. 18.102–18.103), $j_0$, $n_0$ closed forms, the Rayleigh-type
   formula (eq. 18.106); orthogonality "follow[s] directly" from (18.88).
7. **Laguerre and associated Laguerre** (§§18.7–18.8, pp. 616–624).
   $L_n(0)=1$; Rodrigues (eq. 18.112), orthonormality (eq. 18.113),
   generating function and recurrences (eqs. 18.114–18.117);
   $L_n^m=(-1)^m\frac{d^m}{dx^m}L_{n+m}$ (eq. 18.119, other convention
   footnoted), explicit sum, Rodrigues, norm $(n+m)!/n!$, generating
   function, $L_n^m(0)$, recurrences (eqs. 18.120–18.125).
8. **Hermite** (§18.9, pp. 624–628). Physicists' $H_n$ (eqs.
   18.128–18.129), Rodrigues (eq. 18.130), norm $2^nn!\sqrt\pi$
   (eq. 18.132), generating function (eq. 18.133), recurrences
   (eqs. 18.134–18.135); special values.
9. **Hypergeometric identifications** (§§18.10–18.11): $P_m$ and $T_m$ as
   $F(\cdot)$, Laguerre, Hermite and Bessel functions as $M(\cdot)$
   (pp. 630–631, 634). Read, not compiled beyond these identifications.
10. **Equally spaced rules** (§§27.4.1–27.4.2, pp. 1001–1004). Midpoint
    Taylor expansion (eq. 27.35); trapezium rule and error
    $\frac1{12}(b-a)h^2\langle f''\rangle$ (eqs. 27.37–27.38); Simpson's rule
    and error $\frac{b-a}{180}h^4\langle f^{(4)}\rangle$ (eq. 27.40, error
    asserted). Maps for infinite ranges (pp. 1001–1002).
11. **Gaussian integration** (§27.4.3, pp. 1005–1010). Orthogonality
    definition; Gauss–Legendre via the Lagrange interpolant
    (eqs. 27.41–27.43), weight formula and $2n-1$ exactness asserted "can be
    shown"; Table 27.8; worked comparison; Gauss–Chebyshev I and II with
    closed-form nodes and weights (eqs. 27.44–27.47); Table 27.9
    (Laguerre, Hermite).

# Notation map

| Riley et al. (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $h$ (generating functions) | $t$ | **collision:** registry $h$ is the strip width (Riley uses $h$ for that too, in §27.4) |
| $G(x,h)$ | $g(x,t)$ | |
| $P_\ell^m(x)=(1-x^2)^{m/2}\frac{d^mP_\ell}{dx^m}$ | $(-1)^mP_\ell^m$ | **convention:** Riley omits the Condon–Shortley phase in $P_\ell^m$ and puts $(-1)^m$ in $Y_\ell^m$; the $Y_\ell^m$ coincide |
| $Y_\ell^m$ | $Y_\ell^m$ | identical functions |
| $\rho(x)$ (Sturm–Liouville weight), $w(x)$ (§27.4.3) | $\omega(x)$ | |
| $F_n(x)$ | $p_n(x)$ | generic orthogonal polynomial (§27.4.3) |
| $k_n$ | $h_n$ | **collision:** registry $k_n$ is the leading coefficient |
| $a_\ell$, $a_n$ (expansion coefficients) | $c_\ell$, $c_n$ | |
| $n_\ell(x)$ | $y_\ell(x)$ | name only; same function |
| $L_n^m(x)$ | $L_n^{(m)}(x)$ | same function, parenthesized index |
| $\alpha_n$ with $J_\nu(\alpha_nb)=0$; interval $[0,b]$ | $\alpha_{\nu,n}/a$; $[0,a]$ | Riley indexes the series from $n=0$ |
| $\phi_n(x)$ (Laguerre, Hermite functions) | $\varphi_n(x)$ | |
| $(n-\frac12)!$ | $\Gamma(n+\frac12)$ | factorial of non-integer argument |
| $x_i$, $w_i$, $i=1,\dots,n$ | $x_j$, $w_j$ | |
| $w(x_i)$ (weight as integral) | $w_j$ | |
| $G(x)$ (interpolant) | $\sum_j\ell_j(x)\,g(x_j)$ | |
| $\Delta I(\text{estim.})$, $\Delta A_i$ | $E[f]$ and the strip error | sign: estimate minus exact (kept) |
| $\langle f''\rangle$ | $\langle f''\rangle$ | |
| $D^\ell_{mm'}$, $C_{\ell0m'}$ | none (words) | rotation coefficients |
| $\Omega$, $d\Omega$, $\gamma$ | same | |

# Pages created

* Created [Orthogonal polynomials with respect to a weight function](/definitions/orthogonal-polynomials.md).
* Created [Legendre polynomials](/definitions/legendre-polynomials.md).
* Created [Associated Legendre functions](/definitions/associated-legendre-functions.md).
* Created [Spherical harmonics](/definitions/spherical-harmonics.md).
* Created [Chebyshev polynomials](/definitions/chebyshev-polynomials.md).
* Created [Hermite polynomials](/definitions/hermite-polynomials.md).
* Created [Laguerre and associated Laguerre polynomials](/definitions/laguerre-polynomials.md).
* Created [Bessel functions](/definitions/bessel-functions.md).
* Created [Spherical Bessel functions](/definitions/spherical-bessel-functions.md).
* Created [Rodrigues formula](/results/rodrigues-formula.md).
* Created [Generating functions of the classical polynomials and Bessel functions](/results/generating-functions.md).
* Created [Three-term recurrences of the classical polynomials](/results/three-term-recurrences.md).
* Created [Spherical harmonic addition theorem](/results/spherical-harmonic-addition-theorem.md).
* Created [Legendre expansion of the inverse distance (axial multipole expansion)](/results/legendre-expansion-of-inverse-distance.md).
* Created [Fourier–Bessel series](/results/fourier-bessel-series.md).
* Created [Gaussian quadrature](/methods/gaussian-quadrature.md).
* Created [Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md).
* Created [Gauss–Chebyshev quadrature](/methods/gauss-chebyshev-quadrature.md).
* Created [Trapezium and Simpson rules](/methods/trapezium-and-simpson-rules.md).
* Seeded the [notation registry](/notation.md).

# Citations

1. `~/papers/mosaic/orthogonal-polynomials-and-quadrature/2006-CUP-Riley-101017CBO9780511810763.pdf`.
   * **Identity.** doi:10.1017/CBO9780511810763 (Crossref: monograph,
     edition 3); title page and copyright page: K. F. Riley, M. P. Hobson
     and S. J. Bence, third edition, © 2006; hardback ISBN
     978-0-521-86153-3, paperback 978-0-521-67971-8. PDF page = printed
     page + 30.
   * **How it was read.** See the scoped-read statement above. Printed page
     numbers are cited throughout.
   * **Recorded as printed.**
     * p. 625: $H_3(x)=8x^2-12x$ (page image checked); the book's own
       eq. 18.129 gives $8x^3-12x$, as does Arfken et al. Recorded on
       [Hermite polynomials](/definitions/hermite-polynomials.md).
     * p. 624: "Substituting this series into (18.107)" in the Hermite
       section refers to Laguerre's equation; Hermite's is (18.126).
     * p. 634: "$L_n^m(x)$ is an associated Legendre polynomial" for the
       associated Laguerre polynomial.
     * p. 627: the Hermite norm calculation (eq. 18.132) writes the first
       integral from $0$ and the following ones from $-\infty$ (page image
       checked).
   * **Reference list.** The book prints no reference list; the works cited
     in the text of the sections read are its list (bundle law). Three:
     Mathews & Walker (2nd edn, 1971), footnote p. 628; Abramowitz & Stegun
     (Dover, 1965), footnote p. 1009, the source of Tables 27.8–27.9; Press
     et al., *Numerical Recipes in C* (2nd edn, 1992), footnote p. 1014.
     All merged into the [bibliography](/bibliography.md).
