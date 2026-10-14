---
type: Source
title: "Arfken, Weber & Harris (2013) — Mathematical Methods for Physicists, 7th ed. (§12.1, Chs. 14–15, §§18.1, 18.3, 18.4)"
description: "Graduate-level textbook read for its general treatment of orthogonal polynomials (Rodrigues formula from the Sturm–Liouville equation, Schlaefli integral, generating functions), its Bessel-function chapter (J, Y, Hankel, modified, asymptotic and spherical Bessel functions), its Legendre-function chapter (Legendre, associated Legendre with the Condon–Shortley phase, spherical harmonics, second-kind functions) and its Hermite, Laguerre and Chebyshev sections."
resource: "doi:10.1016/C2009-0-30629-7"
source_kind: book
authors: [Arfken G.B., Weber H.J., Harris F.E.]
year: 2013
venue: "Academic Press (7th ed.)"
local_file: "/home/stefano/papers/mosaic/orthogonal-polynomials-and-quadrature/2013-AcademicPress-Arfken-101016C20090306297.pdf"
tags: [textbook, special-functions, orthogonal-polynomials, bessel, legendre, scoped-read]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

*Mathematical Methods for Physicists: A Comprehensive Guide* (7th ed.,
Academic Press/Elsevier, 2013) states in its preface that its proofs "are not
what a mathematician would consider rigorous" but convey the ideas and warn
of the limitations relevant to physics (p. xi). §12.1 (pp. 551–560) develops
orthogonal polynomials in general: the Rodrigues formula of any
Sturm–Liouville equation with quadratic $p$ and linear $q$, the Schlaefli
integral, and the construction of generating functions, ending with a
summary table for Legendre, Hermite, Laguerre and both Chebyshev kinds.
Chapter 14 (pp. 643–713) treats Bessel functions of all kinds, their
orthogonality, asymptotic expansions and the spherical Bessel functions;
Chapter 15 (pp. 715–772) the Legendre polynomials, their physical
interpretation as multipole expansions, associated Legendre functions,
spherical harmonics and second-kind functions; §§18.1, 18.3 and 18.4 the
Hermite, Laguerre (with associated) and Chebyshev polynomials.

**Scoped read (bundle law).** Read: the title, copyright and preface pages,
§12.1 with its exercises and Table 12.1, Chapter 14 and Chapter 15 in full,
and §§18.1, 18.3 and 18.4, plus the chapter-end Additional Readings of
Chapters 12, 14, 15 and 18. The worked text and examples were read closely;
the exercises were read for their statements, not worked. Not read: every
other section, in particular §18.2 (applications of Hermite functions),
§§18.5–18.8 (hypergeometric functions, elliptic integrals), §§12.2 onward,
and Chapter 16, to which §15.5 defers the addition theorem and rotation
matrices. The PDF is an ebook conversion with a clean text layer; all
locators are printed pages from the running heads (the PDF offset drifts
from about +13 to +2), and the extraction renders $\Gamma$ as "0", $\Phi$ and
$\Theta$ as "8" and "2", which were read as such.

**Gaussian quadrature is not treated** in the sections read; it appears only
as the motivation of Exercise 15.1.18 (p. 724). All quadrature pages rest on
[Riley et al. (2006)](/sources/riley-2006.md).

# Key claims

1. **General Rodrigues formula** (§12.1, eqs. 12.1–12.16, pp. 551–554):
   for $p\,y''+q\,y'+\lambda y=0$ with $p$ quadratic, $q$ linear and weight
   $\omega=p^{-1}\exp\int q/p$, $y_n=\omega^{-1}(d/dx)^n(\omega p^n)$ is a
   degree-$n$ solution with $\lambda_n=-n(n-1)p''/2-nq'$; proof given.
   Schlaefli integral (eq. 12.18) and generating-function construction
   (eqs. 12.19–12.27), worked for Legendre (Example 12.1.3).
2. **Bessel $J_\nu$** (§14.1, pp. 643–654): generating function as the
   starting point (eq. 14.2), series (eqs. 14.4–14.6), recurrences
   (eqs. 14.7–14.12) and the converse that the recurrences imply Bessel's
   equation (eqs. 14.13–14.14), integral representations (eqs. 14.16–14.20),
   Table 14.1 of zeros of $J_n$, $J_n'$ ($n\le5$), Schlaefli contour for
   non-integer order (eqs. 14.37–14.40).
3. **Orthogonality of $J_\nu$** (§14.2, pp. 661–665): weight $\rho$,
   Dirichlet and Neumann scalings, norm $\frac{a^2}2J_{\nu+1}^2(\alpha_{\nu,i})$,
   Bessel series "if we assume that the set … is complete" (eqs. 14.43–14.48).
4. **$Y_\nu$, Hankel, modified Bessel** (§§14.3–14.5, pp. 667–685):
   definitions following AMS-55; log term of $Y_n$ (eqs. 14.61–14.62);
   Wronskians (eqs. 14.65–14.71); $K_\nu$ obeys different recurrences from
   $I_\nu$ (eqs. 14.104–14.109).
5. **Asymptotics** (§14.6, pp. 688–695): steepest-descent leading terms of
   $H_\nu^{(1,2)}$, the full asymptotic series for $K_\nu$, $J_\nu$, $Y_\nu$,
   $I_\nu$ with their sectors of validity (eqs. 14.125–14.143); accuracy
   condition $8x\gg4n^2-1$ for the leading term (eq. 14.145).
6. **Spherical Bessel** (§14.7, pp. 698–709): definitions (eq. 14.151),
   series, closed forms, recurrences, Rayleigh formulae (eqs. 14.173–14.176),
   limits, orthogonality with weight $r^2$ (eq. 14.183), Table 14.2 of zeros,
   index orthogonality on $(-\infty,\infty)$ (eqs. 14.190–14.191), modified
   spherical functions.
7. **Legendre** (§§15.1–15.3, pp. 716–739): scale and parity from the
   generating function, explicit form (eq. 15.14), recurrences
   (eqs. 15.18–15.26), bound $|P_n|\le1$ (eqs. 15.27–15.28), Rodrigues
   (eq. 15.30), norm by squaring the generating function (eqs.
   15.33–15.38), Legendre series, inverse-distance and axial multipole
   expansions (eqs. 15.58–15.67).
8. **Associated Legendre** (§15.4, pp. 741–753): defined **with** the
   factor $(-1)^m$ "to maintain agreement with AMS-55" (eq. 15.78);
   $P_\ell^{-m}$ relation (eq. 15.81), polynomial generating function
   (eq. 15.82), recurrences (eqs. 15.84–15.92), Table 15.3, stable start
   $P_m^m$ (Example 15.4.1), parity and $P_\ell^m(0)$ (eqs. 15.95–15.96),
   orthogonality with proof (eqs. 15.97–15.105), second orthogonality
   (eq. 15.107).
9. **Spherical harmonics** (§15.5, pp. 756–765): definition (eq. 15.137),
   orthonormality, Condon–Shortley phase named (p. 758), Table 15.4 with
   Cartesian forms, Laplace series with uniform convergence cited to Hobson
   (eqs. 15.144–15.145), rotation closure (eq. 15.147), special values and
   recurrences (eqs. 15.148–15.152). No addition theorem (deferred to Ch. 16).
10. **$Q_\ell$** (§15.6, pp. 766–770): second-solution integral, closed
    forms, recurrences, extension beyond $|x|>1$, series about $x=0$.
11. **Hermite** (§18.1, pp. 871–876): generating function as definition,
    recurrences, Table 18.1, special values, Rodrigues, explicit series,
    norm by generating functions, Hermite functions.
12. **Laguerre** (§18.3, pp. 889–897): Rodrigues from the general formula,
    generating function by residues, recurrences, Table 18.2, orthonormality
    (proof as exercise), associated polynomials with a generating function
    in the lower index due to Weber (2007) (eq. 18.60), norm
    $(n+m)!/n!$ (eq. 18.71), hydrogen atom.
13. **Chebyshev** (§18.4, pp. 899–907): via Gegenbauer generating function
    (eqs. 18.85–18.91), recurrences, ODEs, special values, Rodrigues,
    trigonometric forms, $V_n$, $W_n$, power series, the heuristic minimax
    argument and Example 18.4.1, orthogonality of $T,U,V,W$
    (eqs. 18.116–18.119).

# Notation map

| Arfken et al. (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $P_l^m$ (with $(-1)^m$) | $P_\ell^m$ | same convention |
| $\mathcal P_l^m$ (polynomial factor) | $(1-x^2)^{-m/2}P_\ell^m$ | words on pages |
| $w(x)$ | $\omega(x)$ | weight function |
| $\alpha,\beta,\gamma,\mu,\nu$ (coefficients of $p$, $q$ in §12.1) | none (words) | **collision:** registry $\nu$ is a Bessel order, $\alpha$ a Jacobi parameter |
| $\lambda$, $\lambda_n$ | $\lambda_n$ | |
| $c_n$ (generating-function scale, eq. 12.19) | none (words) | **collision:** registry $c_n$ is an expansion coefficient |
| $a_n$, $c_{lm}$ (expansion coefficients) | $c_n$, $c_{\ell m}$ | |
| $C_n^{(\alpha)}$ | $C_n^{(\lambda)}$ | Gegenbauer parameter |
| $L_n^k$ | $L_n^{(k)}$ | same function |
| $y_n$, $h_n^{(1,2)}$, $i_n$, $k_n$ (spherical) | $y_\ell$, $h_\ell^{(1,2)}$, $i_\ell$, $k_\ell$ | index renamed; **collision:** registry $h_n$, $k_n$ are norm and leading coefficient, so the spherical functions always carry $\ell$ and a superscript or argument |
| $\alpha_{\nu i}$, $\beta_{\nu m}$; $\alpha_{np}$ (zeros of $j_n$) | $\alpha_{\nu,i}$, $\beta_{\nu,m}$; $\alpha_{\ell+1/2,p}$ | |
| $P_\nu(z)$, $Q_\nu(z)$ (asymptotic series, §14.6) | $A_\nu(z)$, $B_\nu(z)$ | **collision** with Legendre $P$, $Q$ |
| $N_\nu$ (earlier editions) | $Y_\nu$ | |
| $\Theta_{lm}$, $\Phi_m$ | words | normalized polar and azimuthal factors |
| $Y^e_{ml}$, $Y^o_{ml}$ (after Morse–Feshbach) | words | real unnormalized harmonics |
| $\varphi_n$ (Hermite, Laguerre functions); $\psi_n^k$, $\Phi_n^k$ | $\varphi_n$; words | |
| $\chi$; $r_1$, $r_2$ (inverse distance) | $\gamma$; $r$, $r'$ | |
| $\mu_i$ (multipole moments) | $\mu_\ell$ | |
| $t$, $g(x,t)$ | same | |
| $T_n$ generating function $\frac{1-t^2}{1-2xt+t^2}=T_0+2\sum T_nt^n$ | same $T_n$ | **convention:** Riley's generating function differs; both correct |

# Pages created or updated

* Created (merging with Riley et al.) [Orthogonal polynomials with respect to a weight function](/definitions/orthogonal-polynomials.md), [Legendre polynomials](/definitions/legendre-polynomials.md), [Associated Legendre functions](/definitions/associated-legendre-functions.md), [Spherical harmonics](/definitions/spherical-harmonics.md), [Chebyshev polynomials](/definitions/chebyshev-polynomials.md), [Hermite polynomials](/definitions/hermite-polynomials.md), [Laguerre and associated Laguerre polynomials](/definitions/laguerre-polynomials.md), [Bessel functions](/definitions/bessel-functions.md), [Spherical Bessel functions](/definitions/spherical-bessel-functions.md).
* Created (merging with Riley et al.) [Rodrigues formula](/results/rodrigues-formula.md), [Generating functions of the classical polynomials and Bessel functions](/results/generating-functions.md), [Three-term recurrences of the classical polynomials](/results/three-term-recurrences.md), [Legendre expansion of the inverse distance (axial multipole expansion)](/results/legendre-expansion-of-inverse-distance.md), [Fourier–Bessel series](/results/fourier-bessel-series.md).
* Updated (scope note only) [Spherical harmonic addition theorem](/results/spherical-harmonic-addition-theorem.md), [Gaussian quadrature](/methods/gaussian-quadrature.md), [Gauss–Legendre quadrature](/methods/gauss-legendre-quadrature.md), [Gauss–Chebyshev quadrature](/methods/gauss-chebyshev-quadrature.md), [Trapezium and Simpson rules](/methods/trapezium-and-simpson-rules.md).

# Citations

1. `~/papers/mosaic/orthogonal-polynomials-and-quadrature/2013-AcademicPress-Arfken-101016C20090306297.pdf`.
   * **Identity.** doi:10.1016/C2009-0-30629-7 (verified on Crossref per
     bundle law); title page: George B. Arfken, Hans J. Weber, Frank E.
     Harris, *Mathematical Methods for Physicists: A Comprehensive Guide*,
     seventh edition; copyright page ISBN 978-0-12-384654-9, © 2013
     Elsevier Inc.
   * **How it was read.** See the scoped-read statement above.
   * **Recorded as printed.**
     * p. 890: "Equating coefficients of $z^n$" where the series is in $t$;
       and "differentiating the generating function in Eq. (18.45)" where
       the generating function is eq. 18.49.
     * p. 743: "if we insert the Rodrigues formula for $P_l$ into
       Eq. (15.73)" where the substitution is into eq. 15.79.
     * p. 767: eq. 15.159 prints $Q'_{n-1}$ among $Q_l$ terms (index slip).
     * Example 15.5.2 cites its Table 15.5 as "Eq. (15.145)".
   * **Reference list.** The chapter-end Additional Readings of Chs. 12,
     14, 15 and 18 (36 entries, 29 distinct works after merging the
     repeated Abramowitz–Stegun (4×), Whittaker–Watson (3×), Jackson (2×)
     and Morse–Feshbach (2×) entries), merged complete into the
     [bibliography](/bibliography.md). Also merged: two works cited in
     footnotes of the sections read with full bibliographic data, Beattie
     (1958), Bell Syst. Tech. J. 37:689 (p. 648), and H. J. Weber (2007),
     Cent. Eur. J. Math. 5:415 (p. 892), both DOI-verified on Crossref. Not
     merged: the anonymous "Math. Tables Aids Comput. 1: 207–308 (1944)"
     (footnote 5, p. 682), "Smythe … (1969), p. 270" (footnote 12, p. 932,
     belonging to the unread §18.8), and the unreferenced mentions of
     Rainville, Weisner, Truesdell (p. 556) and Condon and Shortley
     (p. 758).
