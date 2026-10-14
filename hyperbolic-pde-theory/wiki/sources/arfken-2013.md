---
type: Source
title: "Arfken, Weber & Harris (2013) — Mathematical Methods for Physicists, 7th ed."
description: "Graduate textbook of mathematical methods for physics; this bundle reads only its ODE chapter (first-order methods, singular points, Frobenius series and Fuchs' theorem, Wronskian and the number of solutions, variation of parameters) and its PDE chapter (first-order characteristics, classification by factorisation, Table 9.1 of boundary data, separation of variables in three coordinate systems, uniqueness for Laplace, d'Alembert, heat-flow solutions)."
resource: "doi:10.1016/C2009-0-30629-7"
source_kind: book
authors: [Arfken G.B., Weber H.J., Harris F.E.]
year: 2013
venue: "Academic Press (7th ed.)"
local_file: "/home/stefano/papers/mosaic/hyperbolic-pde-theory/2013-AcademicPress-Arfken-101016C20090306297.pdf"
tags: [textbook, classification, characteristics, ode, separation-of-variables, series-solution, boundary-conditions]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A methods textbook for physicists, in the style the preface describes:
"Proofs are sketched for almost all the mathematical relations", and they
are "not what a mathematician would consider rigorous", with the reader
"warned of limitations that are likely to be relevant" (Preface, p. xi).
It is the bundle's second source and, like the founding
[Riley et al. (2006)](/sources/riley-2006.md), a weak source for hyperbolic
theory proper: Ch. 9 is "mainly devoted to general properties of
homogeneous PDEs" (p. 403), treats only linear equations in its methods,
and names one nonlinear wave equation without analysing it. Its
contribution here is a second, independent statement of the linear theory.
Every shared claim now carries two citations. It adds a table of all
boundary-data pairings, with stability; characteristics in three variables;
Frobenius' method and Fuchs' theorem; Abel's formula and the bound on the
number of independent solutions; and a solution route for the heat equation
that needs no transform.

**Scoped read.** Read: the preface (pp. xi–xiii); Ch. 7 *Ordinary
Differential Equations* (pp. 329–380) and Ch. 9 *Partial Differential
Equations* (pp. 401–446), text in full, exercises skimmed for stated
results, and both chapters' Additional Readings. Not read: every other
chapter. In particular Ch. 8 (Sturm–Liouville theory), Ch. 10 (Green's
functions), Chs. 14–16 (Bessel and Legendre functions, angular momentum)
and Chs. 19–20 (Fourier series, integral transforms), to which Chs. 7 and 9
defer, are not part of this ingestion; results imported from them are
marked on the concept pages.

**Page numbers.** The PDF is a calibre ebook conversion (1206 PDF pages)
with a good text layer. PDF page minus printed page is $+9$ in Ch. 7 and
$+8$ in Ch. 9. All locators below and on the concept pages are printed
pages, read from the running heads.

**Legibility.** The text layer was used throughout. Printed p. 443 was
rendered and read as an image to confirm eqs. 9.123–9.126 (see claim 14);
the text layer matched it. No equation used here was illegible.

**Metadata.** Title, subtitle (*A Comprehensive Guide*), authors, edition
and publisher from the title page; © 2013 Elsevier Inc. and ISBN
978-0-12-384654-9 from the copyright page. DOI as verified on Crossref
for the bundle law (D21).

# Key claims

1. **First-order PDEs, constant coefficients** (§9.2, eqs. 9.1–9.10,
   pp. 403–408). The rotated coordinates along and across the
   characteristics turn $b_1\partial_x u + b_2\partial_y u = 0$ into
   $\partial_\sigma u = 0$, general solution $F(b_2x - b_1y)$; with lower-order
   terms, an ODE along each characteristic. Also in three variables.
2. **Data and characteristics** (§9.2, pp. 405–408). Taylor-expansion
   determinant argument; four conclusions on data along, across and twice
   across characteristics; the three-variable version for data surfaces.
3. **Classification** (§9.3, eqs. 9.11–9.22, pp. 409–411) by factorising
   the principal part; discriminant $b^2 - ac$ ($= D$); slopes of the
   characteristics; diagonal canonical form; local classification for
   variable coefficients; informal extension to more variables.
4. **Boundary conditions and Table 9.1** (§9.3, pp. 411–413): Dirichlet,
   Neumann, Cauchy; all pairings of data and equation type with "unique,
   stable", "insufficient", "too restrictive", "not unique", "unphysical
   (instability)"; initial conditions as Cauchy data at one end; the table
   "oversimplifies" (Helmholtz). Reference to Morse and Feshbach, Ch. 6.
5. **Nonlinear PDEs** (§9.3, eqs. 9.23–9.28, pp. 413–414): the "simplest
   nonlinear wave equation" $\partial_tu + c(u)\partial_xu = 0$, named only;
   the KdV soliton (dispersive, outside the bundle's compiled scope).
6. **Separation of variables** (§9.4, pp. 414–432): $n - 1$ independent
   constants; additive operators and separable boundary conditions as the
   condition for success; unique-solution versus eigenvalue problems;
   Cartesian, cylindrical and spherical Helmholtz equations; $\ell(\ell+1)$
   from regularity; radial functions $r^\ell$, $r^{-\ell-1}$, $j_\ell$,
   $y_\ell$; Tables 9.2–9.3; Examples 9.4.1–9.4.4.
7. **Laplace and Poisson** (§9.5, pp. 433–434): no interior extremum
   (curvature argument); uniqueness for Dirichlet (by the extremum
   argument) and Neumann data (by Green's theorem, up to a constant);
   method of images justified by uniqueness.
8. **Wave equation** (§9.6, pp. 435–437): general solution along the
   characteristics, standing waves, equivalence of separated and travelling
   solution sets, d'Alembert's formula (eq. 9.95), also credited to Euler.
9. **Diffusion equation** (§9.7, pp. 437–444): anisotropy removed by
   rescaling; separated modes including the zero-constant one; error
   function similarity solution; new solutions by differentiation and by
   translation-superposition, giving the heat-kernel integral (eq. 9.114);
   spherical symmetry by $u = v/r$; point release in three dimensions with
   $t_{\max} = r^2/(6\kappa)$.
10. **First-order ODEs** (§7.2, pp. 331–342): separable, exact, homogeneous,
    isobaric, linear (integrating factor), variation of the constant;
    uniqueness up to a homogeneous solution; one independent homogeneous
    solution. Bernoulli and Riccati equations, movable singularities
    (§7.8, pp. 377–380).
11. **Constant coefficients and linear structure** (§7.1, §7.3, §7.5,
    pp. 329–330, 342–343, 346): linear operators, two senses of
    "homogeneous", $e^{\nu x}$ and the repeated-root rule,
    $y = c_1y_1 + c_2y_2 + y_p$.
12. **Singular points, Frobenius, Fuchs** (§7.4–7.5, pp. 343–358):
    ordinary, regular and irregular points; indicial equation and
    recurrence; Fuchs' theorem (stated); cases by indicial roots;
    convergence cautions.
13. **Wronskian and second solutions** (§7.6, pp. 358–374): linear
    independence, the Wronskian test with its conditions (footnote, Lass);
    $W' = -a_1W$ and the zero-or-never dichotomy; at most two independent
    solutions; second solution by the Wronskian integral (eq. 7.67) and its
    logarithmic series form; $Y_0$, $Y_1$. Variation of parameters (§7.7,
    pp. 375–377).
14. **A misprint** (§9.7, eq. 9.126, p. 443): the "solution" for planar
    radial diffusion is the integrated $v'$, not $v$, and does not satisfy
    the PDE (compiler's check; see the [diffusion
    equation](/definitions/diffusion-equation.md)).

# Notation map

| Arfken et al. (2013) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\varphi(x,y)$, $\psi$ (unknown of a PDE) | $u$ | $\psi$ is the right-hand side in the registry |
| $F(x,y)$, $F(x)$ (source term) | $\psi$ | |
| $L$ (differential operator) | $\mathcal L$ | |
| $a$, $b$ (first-order coefficients, eq. 9.1); $c$ (third, eq. 9.10) | $b_1$, $b_2$; $b_3$ | |
| $q(x,y)$ (zeroth-order coefficient, eq. 9.8) | $c_0$ | |
| $s$, $t$ (coordinates along and across the characteristics) | $\sigma$, $\xi$ | $t$ is time in the registry; $\sigma$ here is not arc length |
| $l$, $l'$ (curve parameters) | $\sigma$ | |
| $D$ (determinant of the data system, p. 405) | no symbol | **collision:** $D$ is the discriminant in the registry |
| $a$, $2b$, $c$ (second-order coefficients, eq. 9.17) | $a_{11}$, $2a_{12}$, $a_{22}$ | **no factor:** $b^2 - ac = D$ exactly |
| $a$, $c$ (eq. 9.11 prototype) | $\sqrt{a_{11}}$, $\sqrt{-a_{22}}$ | |
| $\xi$, $\eta$ (eq. 9.20, diagonalising) | $\hat\xi$, $\hat\eta$ | registry $\xi$, $\eta$ are characteristic coordinates |
| $f$, $g$ (arbitrary functions) | $F$, $G$ | |
| $c(\psi)$ (eq. 9.23) | $c(u)$ | |
| $\psi_0(x)$, $\partial\psi(x,0)/\partial t$ | $u_0$, $u_1$ | |
| $V$, $V_0$ (boundary values) | $g$ | |
| $d\psi/dn$ | $\partial_nu$ | |
| $l$, $m$, $n$ (Cartesian separation constants, eq. 9.39) | $k_x$, $k_y$, $k_z$ | |
| $\lambda$, $\mu$, $\nu$ (mode integers, Examples 9.4.1–9.4.2) | $n$; $n_1$, $n_2$, $n_3$ | |
| $\rho$ (cylindrical radius), $P(\rho)$ | $r$, $R(r)$ | **collision:** $\rho$ is density in the registry |
| $\varphi$ (azimuth), $\Phi(\varphi)$, $\Theta(\theta)$ | $\phi$, $\Phi(\phi)$, $\Theta(\theta)$ | |
| $m$ (azimuthal order), $l$ (degree) | $n$, $\ell$ | $m$ is reserved for the number of system components |
| $\lambda$ (Legendre separation constant) | $\ell(\ell+1)$ | |
| $P_l^m$, $Q_l^m$, $J_m$, $Y_m$, $j_l$, $y_l$ | $P_\ell^n$, $Q_\ell^n$, $J_n$, $Y_n$, $j_\ell$, $y_\ell$ | |
| $R$, $a$ (cylinder, sphere radius); $a$, $b$, $c$ (box sides); $L$ | $R_0$; $L_x$, $L_y$, $L_z$; $L$ | |
| $E$, $\lambda$ (eigenvalues of $-\tfrac12\nabla^2$, $-\nabla^2$) | $\lambda_n$ | $k^2 = 2E$ for the box |
| $\alpha \approx 2.4048$ (first zero of $J_0$) | the number | $\alpha$ is a coefficient in the registry |
| $a^2$ (diffusivity) | $\kappa$ | |
| $\xi = x/\sqrt t$ (similarity variable) | $\zeta = x/(2\sqrt{\kappa t})$ | rescaled |
| $\xi$ (integration variable, eqs. 9.112–9.114) | $q$ | |
| $\sigma$, $\rho$, $Q$ (specific heat, density, heat released) | words; $\int u\,\mathrm dV$ | $\sigma$, $q$ are taken |
| $\mu^2$ (Klein–Gordon) | $k^2$ | Arfken's Klein–Gordon is four-dimensional; see [Helmholtz](/definitions/helmholtz-equation.md) |
| $P(x)$, $Q(x)$ (in $y'' + Py' + Qy = 0$) | $a_1(x)$, $a_0(x)$ | |
| $p(x)$, $q(x)$ (in $y' + py = q$) | $a_0(x)$, $\psi(x)$ | |
| $P(x,y)\,\mathrm dx + Q(x,y)\,\mathrm dy$; $\varphi(x,y)$ | $M\,\mathrm dx + N\,\mathrm dy$; $U(x,y)$ | |
| $\alpha(x)$ (integrating factor) | $\mu(x)$ | |
| $n$ (Bernoulli exponent) | $\gamma$ | |
| $p$, $q$, $r$ (Riccati coefficients) | $\chi_2$, $\chi_1$, $\chi_0$ | |
| $m$, $m_j$ (auxiliary roots) | $\nu_j$ | |
| $s$ (indicial exponent); $\alpha$, $\alpha - n$ (its roots) | $\nu$; $\nu_1$, $\nu_2$ | $s$ is kept free for a shock speed |
| $a_j$ (series coefficients); $d_j$ | $C_j$; $C_j'$ | $a_k$ are ODE coefficients in the registry |
| $x_0$ (expansion point) | $x_0$ | |
| $u_1$, $u_2$ (varied parameters) | $k_1$, $k_2$ | |
| $W$ | $W$ | same |
| $\nabla^2$, erf, $\delta$ | $\nabla^2$, $\operatorname{erf}$, $\delta$ | same |

# Pages touched

* Created [Helmholtz equation](/definitions/helmholtz-equation.md) (≥2 sources; carries the open `Contradictions` entry on the minus sign).
* Created [Series solutions of linear ODEs (Frobenius' method)](/methods/frobenius-series-solutions.md) (a substantive named method and theorem of this source; also cites Riley et al.).
* Updated [Notation registry](/notation.md): $x_0$, $b_3$ and $\mathbf b$, $c(u)$, $\hat\xi$ and $\hat\eta$, $\nu$ (Frobenius exponent), $k_x$, $k_y$, $k_z$, $j_\ell$ and $y_\ell$, $L_z$, $\chi_0$, $\chi_1$, $\chi_2$ (Riccati coefficients).
* Updated [Classification of second-order linear PDEs](/definitions/second-order-pde-classification.md) (agreement; factorisation; canonical forms; qualifications on invariance and on more variables).
* Updated [Characteristic curves](/definitions/characteristic-curve.md) (agreement; qualification on data along a characteristic; three variables; the compiler's ODE-along-characteristics remark now partly supported).
* Updated [Dirichlet, Neumann and Cauchy boundary conditions](/definitions/boundary-condition-types.md).
* Updated [Homogeneous equations and homogeneous problems](/definitions/homogeneous-linear-problem.md) (qualification: two definitions of a homogeneous ODE).
* Updated [Wronskian](/definitions/wronskian.md) (qualification on the converse; Abel's formula; the gap narrowed, not closed).
* Updated [Wave equation](/definitions/wave-equation.md), [Diffusion equation](/definitions/diffusion-equation.md) (compiler's check of eq. 9.126), [Laplace and Poisson equations](/definitions/laplace-and-poisson-equations.md), [Fundamental solution](/definitions/fundamental-solution.md).
* Updated [First-order linear PDEs: general solution along characteristics](/methods/first-order-linear-pde-characteristics.md), [General solution of constant-coefficient second-order PDEs](/methods/constant-coefficient-second-order-general-solution.md), [Separation of variables](/methods/separation-of-variables.md), [Integral transform methods](/methods/integral-transform-methods.md), [Green's functions for linear PDEs](/methods/greens-functions-for-pdes.md), [Variation of parameters](/methods/variation-of-parameters.md), [Solution methods for first-order ODEs](/methods/first-order-ode-solution-methods.md).
* Updated [d'Alembert's formula](/results/dalembert-formula.md), [Boundary data by equation type](/results/boundary-data-by-equation-type.md) (Table 9.1; qualifications), [Uniqueness theorem for Poisson's equation](/results/uniqueness-theorem-poisson.md), [Structure of linear ODE solutions](/results/linear-ode-solution-structure.md).
* Updated [Riley et al. (2006)](/sources/riley-2006.md) (audit lines only).

Not touched: [Green's functions for linear ODEs](/methods/greens-functions-for-linear-odes.md)
(Arfken's ODE Green's functions are in Ch. 10, not read).

# Citations

1. `~/papers/mosaic/hyperbolic-pde-theory/2013-AcademicPress-Arfken-101016C20090306297.pdf`
   (1206 PDF pages; the full seventh edition).
2. Reference list: the Additional Readings of Ch. 7 (p. 380) and Ch. 9
   (p. 445), merged complete into the [bibliography](/bibliography.md),
   together with the works cited in footnotes of the chapters read (Lass
   1957, p. 360; Wolfram 1991 and Heck 1993, p. 355; Jahnke and Emde 1945
   and Jahnke, Emde and Lösch 1960, p. 422) and the second edition of the
   book itself, cited in the text (p. 415). Cohen (1992) and Margenau and
   Murphy (1956) appear in both lists; Morse and Feshbach (1953) was
   already in the bibliography from Riley et al.
