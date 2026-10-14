---
type: Source
title: "Riley, Hobson & Bence (2006) — Mathematical Methods for Physics and Engineering, 3rd ed."
description: "Undergraduate-to-graduate textbook of mathematical methods; this bundle reads only its ODE chapters (first- and higher-order linear equations, Wronskian, variation of parameters, ODE Green's functions) and its two PDE chapters (model equations, classification, characteristics, general solutions, d'Alembert, Table 20.1 of boundary data, uniqueness for Poisson, separation of variables, transform methods, PDE Green's functions and images)."
resource: "doi:10.1017/CBO9780511810763"
source_kind: book
authors: [Riley K.F., Hobson M.P., Bence S.J.]
year: 2006
venue: "Cambridge University Press (3rd ed.)"
local_file: "/home/stefano/papers/mosaic/hyperbolic-pde-theory/2006-CUP-Riley-101017CBO9780511810763.pdf"
tags: [textbook, classification, characteristics, ode, separation-of-variables, greens-function, transform-methods]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A methods textbook in a uniform style: definitions, worked examples and
"solution method" recipes, with exercises (hints for the odd-numbered
ones) at the end of each chapter. It is the founding source of the bundle.
It supplies the continuum vocabulary (equation types, characteristics,
Dirichlet/Neumann/Cauchy data) and the standard solution methods for the
linear model equations. It is a weak source for the hyperbolic theory the
bundle is ultimately about: it treats only **linear** equations, mostly in
**two independent variables**, and has no hyperbolic systems, conservation
laws, weak or entropy solutions, Riemann problems, or existence theorems.
The pages created here restrict themselves to what the book says; the
rest of the scope waits for its sources.

**Scoped read.** Read: front matter (contents, prefaces); Ch. 14
*First-order ordinary differential equations* (pp. 468–489); Ch. 15
*Higher-order ordinary differential equations* (pp. 490–530); Ch. 20
*Partial differential equations: general and particular solutions*
(pp. 675–712); Ch. 21 *Partial differential equations: separation of
variables and other methods* (pp. 713–774). The text was read in full and
the exercises skimmed for stated results and citations. All other chapters
were not read. In particular, Ch. 11 (Green's theorems), Ch. 12 (Fourier
series), Ch. 13 (Fourier and Laplace transforms), Chs. 16–18 (series
solutions, Sturm–Liouville and eigenfunction methods, special functions)
and Ch. 24 (contour inversion), which the chapters read invoke, are not
part of this ingestion. Results imported from them are marked as such on
the concept pages. PDF page = printed page + 30. All locators below are
printed pages.

**Legibility.** The PDF is a scan with a text layer. The text layer was
checked against a rendered image of p. 703 (the characteristic determinant
and eqs. 20.44–20.45) and matched. No equation used here was illegible.

**Metadata.** Title, authors, edition and publisher from the title and
copyright pages; DOI verified on Crossref (type monograph, edition 3).
ISBNs: hardback 978-0-521-86153-3, paperback 978-0-521-67971-8.

# Key claims

1. **Classification** (§20.3.3, eq. 20.19, p. 687). $A u_{xx} + Bu_{xy} + Cu_{yy} + \dots$
   is hyperbolic, parabolic or elliptic as $B^2 - 4AC$ is $>, =, < 0$; the
   type can vary over the plane. Type invariance under a change of variables
   is set as Exercise 20.24 (p. 710).
2. **First-order linear PDEs** (§20.3.1, eqs. 20.9–20.12, pp. 681–685).
   The general solution is $u = F(\xi)$ with $\xi$ constant on
   $\mathrm dx/b_1 = \mathrm dy/b_2$, a solution factor when a zeroth-order
   term is present, and a particular integral for forcing (§20.3.2).
3. **Homogeneous equation vs. homogeneous problem**, and general solution
   = particular + homogeneous (§20.3.2, pp. 685–687).
4. **Constant-coefficient second-order equations** (§20.3.3,
   pp. 687–692). $u = F(x + \beta_1y) + G(x + \beta_2y)$, or $F + xG$ when
   parabolic; reduction to $\partial_\xi\partial_\eta u = 0$. The p. 690
   remark on the form of elliptic arguments is accurate only without a
   mixed term (compiler's check).
5. **Wave equation** (§20.1.1, §20.4, pp. 676–677, 693–695): string
   derivation, travelling and standing waves, d'Alembert's formula
   (eq. 20.31), plane waves in 3D (eq. 20.33).
6. **Diffusion equation** (§20.1.2, §20.5, pp. 678–679, 695–698):
   derivation through a flux law and the divergence theorem, no
   travelling-wave solution, error-function similarity solution
   (eq. 20.36).
7. **Characteristics** (§20.6, pp. 699–705): defined as curves on which
   data cannot fix the derivatives (eqs. 20.41, 20.44–20.45). Data on a
   characteristic leave the solution undetermined; data on a curve met
   twice by a characteristic overdetermine it; the solution is fixed only
   where both characteristics meet the data curve (Fig. 20.5).
8. **Boundary-condition types and Table 20.1** (§20.6.2, pp. 702–705):
   Dirichlet/Neumann/Cauchy; hyperbolic–open–Cauchy,
   parabolic–open–Dirichlet or Neumann, elliptic–closed–Dirichlet or
   Neumann. Stated without proof (reference to Morse & Feshbach).
9. **Uniqueness for Poisson's equation** (§20.7, pp. 705–707), proved by
   Green's first theorem; up to a constant for Neumann data.
10. **Separation of variables** (§21.1–21.3, pp. 713–746): separation
    constants, superposition with complete sets, Fourier sine series for
    plate problems, removal of inhomogeneous boundary values,
    Laplace/Helmholtz in polar coordinates with Bessel and Legendre
    functions, solution by expansion with uniqueness, Legendre expansion
    for Poisson's equation.
11. **Integral transforms** (§21.4, pp. 747–751): Laplace in $t$, Fourier
    in $x$, heat-kernel solution (eq. 21.74), equivalence with continuum
    separation.
12. **PDE Green's functions** (§21.5, pp. 751–767): definition (eq. 21.77),
    eigenfunction form (eq. 21.79), representation formula (eq. 21.84),
    Dirichlet and Neumann Green's functions, Neumann compatibility
    (eq. 21.105), fundamental solutions (eqs. 21.90, 21.93), method of
    images (half-space, sphere, disc; Poisson integral eq. 21.104).
13. **Linear ODEs** (Ch. 15, pp. 490–517): $y = y_c + y_p$, Wronskian
    (eq. 15.6; non-vanishing is sufficient, not necessary, for
    independence), auxiliary equation, undetermined coefficients, Laplace
    method, Euler/Legendre equations, exact equations, reduction of order,
    variation of parameters (eq. 15.55), Green's functions with jump
    conditions (eqs. 15.62–15.65), canonical form (eq. 15.73). Linear
    recurrence relations (§15.1.4) are noted but not compiled (discrete).
14. **First-order ODEs** (Ch. 14, pp. 468–484): separable, exact,
    integrating factors, linear, homogeneous, isobaric, Bernoulli,
    Clairaut and singular solutions. The $n$ arbitrary constants of an
    $n$th-order ODE are assumed ("a totally general proof is difficult",
    p. 470); there is no existence/uniqueness theorem.

# Notation map

| Riley et al. (2006) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $A, B, C$ (second-order coefficients) | $a_{11}$, $2a_{12}$, $a_{22}$ | **factor 2:** $B^2 - 4AC = 4D$ |
| $D, E, F$ (lower-order coefficients, eq. 20.19) | $b_1$, $b_2$, $c_0$ | |
| $A, B, C$ (first-order eq. 20.9) | $b_1$, $b_2$, $c_0$ | |
| $R(x,y)$, $F(x,y,u)$, $\rho(\mathbf r)$, $f(x)$ (right-hand sides) | $\psi$ | $\rho$ is a density in the registry, $f$ a flux |
| $\mathbf r$, $\mathbf r_0$ | $\mathbf x$, $\mathbf x'$ | Green's functions: $G(\mathbf r,\mathbf r_0) \to G(\mathbf x,\mathbf x')$ |
| $G(x,z)$ (ODE Green's function), $\xi$ (Ex. 15.27) | $G(x,x')$ | |
| $V$, $S$ | $\Omega$, $\partial\Omega$ | |
| $C$ (boundary curve), $s$ (arc length) | $\Gamma$, $\sigma$ | |
| $\varphi(s)$, $\psi(s)$ (Cauchy data on $C$) | $g$, $h$ | |
| $\phi(x)$, $\psi(x)$ (d'Alembert initial data) | $u_0$, $u_1$ | |
| $f$, $u_0$ (Dirichlet values in examples) | $g$ | |
| $p$ (combination variable), $\zeta, \eta$ (new variables) | $\xi$; $\xi, \eta$ | |
| $\lambda_1$, $\lambda_2$ (ratios $b/a$) | $\beta_1$, $\beta_2$ | $\lambda$ is reserved for eigenvalues |
| $f$, $g$ (arbitrary functions) | $F$, $G$ | |
| $h(x,y)$ (solution factor) | $v$ | |
| $\lambda$, $l, m, n, \mu$ (separation constants) | $k$, $\mathbf k$ | |
| $T(t)$ (time factor), $F(\mathbf r)$ (spatial factor) | $\mathcal T(t)$, $U(\mathbf x)$ | |
| $\rho$ (cylindrical / plane-polar radius) | $r$ | **collision:** $\rho$ is density in the registry |
| $P(\rho)$ (radial factor), $M(\mu)$ | $R(r)$, $\Theta$ | |
| $n$ (plane polar), $m$ (cylindrical and spherical azimuthal order) | $n$ | $m$ is reserved for the number of system components |
| $\ell$, $P_\ell^m$, $Q_\ell^m$, $J_m$, $Y_m$ | $\ell$, $P_\ell^n$, $Q_\ell^n$, $J_n$, $Y_n$ | |
| $a$, $b$ (radius, plate sides), $L$ | $R_0$, $L_x$, $L_y$, $L$ | |
| $\lambda_m$ (auxiliary roots) | $\nu_j$ | |
| $P(x)$, $Q(x)$ (first-order linear ODE) | $a_0(x)$, $\psi(x)$ | |
| $A(x,y)\,\mathrm dx + B(x,y)\,\mathrm dy$ | $M\,\mathrm dx + N\,\mathrm dy$ | |
| $n$ (Bernoulli exponent) | $\gamma$ | |
| $h(x)$ (boundary-value polynomial) | $y_b(x)$ | $h$ is Neumann data in the registry |
| $\lambda_n$, $u_n$ (operator eigenpairs) | $\lambda_n$, $\varphi_n$ | |
| $F(\mathbf r,\mathbf r_0)$ (fundamental solution) | $E_d(\mathbf x - \mathbf x')$ | |
| $G(x,t)$ (heat-equation Green's function) | $K(x,t)$ | |
| $q$, $\mathbf r_n$ (images) | $q_j$, $\mathbf x_j$ | |
| $A$ (area of $S$), $\langle u\rangle_S$ | $\lvert\partial\Omega\rvert$, $\langle u\rangle_{\partial\Omega}$ | |
| $\bar f(s)$ (Laplace variable $s$) | $\bar u(p)$ | $s$ kept free for a shock speed |
| $\nabla^2$, $\tilde f(k)$ | $\nabla^2$, $\tilde u(k)$ | same |
| $p(\mathbf r)$, $q(\mathbf r)$ (Ex. 21.28 operator) | $\alpha(\mathbf x)$, $c_0$ | |
| $m^2$ (Klein–Gordon, Ex. 20.25) | $k^2$ | |

# Pages created

* Created [Notation registry](/notation.md) (seeded).
* Created [Classification of second-order linear PDEs](/definitions/second-order-pde-classification.md), [Characteristic curves](/definitions/characteristic-curve.md), [Dirichlet, Neumann and Cauchy boundary conditions](/definitions/boundary-condition-types.md), [Homogeneous equations and homogeneous problems](/definitions/homogeneous-linear-problem.md), [Wronskian](/definitions/wronskian.md), [Fundamental solution](/definitions/fundamental-solution.md), [Wave equation](/definitions/wave-equation.md), [Diffusion equation](/definitions/diffusion-equation.md), [Laplace and Poisson equations](/definitions/laplace-and-poisson-equations.md).
* Created [First-order linear PDEs: general solution along characteristics](/methods/first-order-linear-pde-characteristics.md), [General solution of constant-coefficient second-order PDEs](/methods/constant-coefficient-second-order-general-solution.md), [Separation of variables](/methods/separation-of-variables.md), [Integral transform methods](/methods/integral-transform-methods.md), [Green's functions for linear PDEs](/methods/greens-functions-for-pdes.md), [Green's functions for linear ODEs](/methods/greens-functions-for-linear-odes.md), [Variation of parameters](/methods/variation-of-parameters.md), [Solution methods for first-order ODEs](/methods/first-order-ode-solution-methods.md).
* Created [d'Alembert's formula](/results/dalembert-formula.md), [Boundary data by equation type](/results/boundary-data-by-equation-type.md), [Uniqueness theorem for Poisson's equation](/results/uniqueness-theorem-poisson.md), [Structure of linear ODE solutions](/results/linear-ode-solution-structure.md).
* Cited on [Helmholtz equation](/definitions/helmholtz-equation.md) (added with arfken-2013).
* Cited on [Series solutions of linear ODEs (Frobenius' method)](/methods/frobenius-series-solutions.md) (added with arfken-2013).

# Citations

1. `~/papers/mosaic/hyperbolic-pde-theory/2006-CUP-Riley-101017CBO9780511810763.pdf`
   (1363 PDF pages; the full third edition).
2. Reference list: the book prints none. The works cited in the footnotes
   of the chapters read (Piaggio 1954, p. 686; Morse & Feshbach 1953,
   p. 705; Schiff 1955, p. 741) are recorded in the
   [bibliography](/bibliography.md). Chs. 14–15 cite nothing.
