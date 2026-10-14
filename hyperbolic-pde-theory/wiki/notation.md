---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-14T00:00:00Z
---

# Notation registry

This registry is law for every concept page of the bundle. Source pages
translate their native symbols onto it in a `# Notation map`. It was seeded
on 2026-10-13 from the conventions that dominate the PDE literature (the
founding textbook's where they do not collide, the hyperbolic-systems
conventions where they do), so that later sources map onto it with few
renamings. Extend it, and log the extension, before writing a symbol it
lacks.

Two choices were made with the hyperbolic-systems literature in mind and
depart from the founding textbook: the second-order coefficients are
$a_{ij}$ (not $A, B, C$, which would collide with the flux Jacobian $A$),
and the right-hand side of a linear problem is $\psi$ (not $f$, which is
the flux, nor $\rho$, which is a density).

## Independent variables and domains

| Symbol | Meaning |
|---|---|
| $t$ | time |
| $x$ | space coordinate in one dimension; first independent variable of a two-variable problem |
| $y$ | second independent variable of a two-variable problem; in ODE pages, the unknown $y(x)$ (an ODE for a curve $y(x)$ of the $(x,y)$ plane is both at once) |
| $z$ | third Cartesian coordinate |
| $\mathbf x = (x_1, \dots, x_d)$ | position in $d$ space dimensions; $\mathbf x = (x, y, z)$ in Cartesian components |
| $d$ | number of space dimensions |
| $(r, \phi)$; $(r, \phi, z)$; $(r, \theta, \phi)$ | plane polar; cylindrical polar; spherical polar coordinates ($\theta$ polar angle, $\phi$ azimuth) |
| $\Omega$, $\partial\Omega$ | solution domain and its boundary |
| $\hat{\mathbf n}$ | outward unit normal on $\partial\Omega$ (or unit normal of a curve) |
| $\mathrm dV$, $\mathrm dS$ | volume and surface elements |
| $\Gamma$ | curve (two variables) or surface carrying initial or boundary data |
| $\sigma$ | parameter (arc length unless stated) along $\Gamma$ or along a characteristic |
| $x'$, $\mathbf x'$ | source point of a Green's function; also a dummy integration variable |
| $x_0$ | expansion point of a series solution of an ODE; point carrying one-point (initial) conditions $y(x_0)$, $y'(x_0)$ (added 2026-10-14, arfken-2013) |
| $q$ | dummy integration variable (e.g. in $\operatorname{erf}$ and d'Alembert's formula) |

## Unknowns, data and coefficients

| Symbol | Meaning |
|---|---|
| $u$ | unknown of a PDE: a scalar, or the state vector $u \in \mathbb R^m$ of a system |
| $y(x)$ | unknown of an ODE; $y'$, $y''$, $y^{(k)}$ its derivatives |
| $\psi$ | right-hand side (forcing, source) of a linear problem: $\mathcal L u = \psi$, $\mathcal L y = \psi(x)$; source term of a balance law |
| $g$, $h$ | prescribed value and prescribed normal derivative on $\Gamma$ or $\partial\Omega$: $u = g$, $\partial_n u = h$ |
| $u_0(x)$, $u_1(x)$ | Cauchy (initial) data of a second-order-in-time problem: $u(x,0) = u_0$, $\partial_t u(x,0) = u_1$; for a first-order-in-time problem only $u_0$ |
| $b_1$, $b_2$, $c_0$ | coefficients of the first-order linear operator $b_1\partial_x u + b_2\partial_y u + c_0 u$ (also the lower-order part of a second-order operator) |
| $b_3$; $\mathbf b = (b_1, b_2, b_3)$ | coefficient of $\partial_z u$, and coefficient vector, of a first-order operator in three variables, $\mathbf b\cdot\nabla u$ (added 2026-10-14, arfken-2013) |
| $a_{11}$, $a_{12}$, $a_{22}$ | principal coefficients of the second-order operator $a_{11}\partial_x^2 u + 2a_{12}\partial_x\partial_y u + a_{22}\partial_y^2 u$ |
| $D = a_{12}^2 - a_{11}a_{22}$ | discriminant of the second-order operator |
| $a_k(x)$ | coefficient of $y^{(k)}$ in a linear ODE of order $n$ |
| $n$ | order of an ODE; also a summation / mode index |
| $c$ | wave (propagation) speed |
| $c(u)$ | propagation speed that depends on the solution, in the scalar quasi-linear equation $\partial_t u + c(u)\,\partial_x u = 0$ (added 2026-10-14, arfken-2013; for a conservation law $c(u) = f'(u)$) |
| $\kappa$ | diffusivity (diffusion coefficient), dimensions length$^2$ time$^{-1}$ |
| $\rho$ | mass density (never a coordinate, never a source) |
| $\alpha(\mathbf x)$ | coefficient of a divergence-form operator $\nabla\cdot(\alpha\nabla u)$ |
| $L$; $L_x$, $L_y$; $R_0$ | lengths: interval or bar length; rectangle sides; radius of a disc, cylinder or sphere |
| $L_z$ | third side of a rectangular box (added 2026-10-14, arfken-2013) |
| $c_j$, $C_j$, $B_n$ (also primed) | arbitrary constants and expansion coefficients, local to the page that defines them |
| $u_h$, $u_s$ | homogeneous-problem part and steady-state part of a decomposed solution |

## Derivatives and operators

| Symbol | Meaning |
|---|---|
| $\partial_t$, $\partial_x$, $\partial_{x_j}$ | partial derivatives; $\partial u/\partial x$ is the same object, used in displays. Subscripts on $u$ never denote derivatives |
| $\partial_x^2$, $\partial_x\partial_y$ | second partial derivatives |
| $\mathrm d/\mathrm d\sigma$ | derivative along a curve parametrised by $\sigma$ |
| $\nabla$, $\nabla\cdot$ | gradient, divergence |
| $\nabla^2$ | Laplacian (sources writing $\Delta$ map to it) |
| $\partial_n u = \nabla u\cdot\hat{\mathbf n}$ | normal derivative |
| $\mathcal L$ | linear differential operator (ordinary or partial) |
| $\delta$ | Dirac delta, of the dimension of its argument |
| $H$ | Heaviside step function |
| $\operatorname{erf}(\zeta) = \frac{2}{\sqrt\pi}\int_0^\zeta e^{-q^2}\,\mathrm dq$ | error function |

## Characteristics and special variables

| Symbol | Meaning |
|---|---|
| $\xi$, $\eta$ | characteristic (canonical) coordinates of a second-order operator; $\xi$ alone is the invariant of a first-order operator, constant along its characteristics |
| $\beta_1$, $\beta_2$ | roots of $a_{22}\beta^2 + 2a_{12}\beta + a_{11} = 0$; the characteristic coordinates of a constant-coefficient operator are $x + \beta_j y$ |
| $\hat\xi$, $\hat\eta$ | non-characteristic coordinates that diagonalise a constant-coefficient principal part, $\hat\xi = a_{22}^{1/2}x - a_{22}^{-1/2}a_{12}y$, $\hat\eta = a_{22}^{-1/2}y$ ($a_{22} > 0$) (added 2026-10-14, arfken-2013) |
| $F$, $G$ | arbitrary functions in a general solution, e.g. $u = F(x - ct) + G(x + ct)$ (a context of its own; $G$ with two arguments is a Green's function) |
| $\zeta = x/(2\sqrt{\kappa t})$ | similarity variable of the one-dimensional diffusion equation |
| $\hat{\mathbf n}\cdot\mathbf x \mp ct$ | phase of a plane wave travelling along the unit vector $\hat{\mathbf n}$ |

## ODE theory

| Symbol | Meaning |
|---|---|
| $y_1, \dots, y_n$ | linearly independent solutions of a homogeneous linear ODE |
| $y_c$, $y_p$ | complementary function, particular integral |
| $W(y_1, \dots, y_n)$ | Wronskian |
| $\nu_j$ | roots of the auxiliary (characteristic) polynomial of a constant-coefficient linear ODE |
| $\nu$ | leading exponent of a Frobenius series $y = \sum_j C_j(x - x_0)^{\nu + j}$; the roots of its indicial equation are written $\nu_1, \nu_2$ (added 2026-10-14, arfken-2013) |
| $\mu(x)$ | integrating factor of a first-order ODE |
| $k_j(x)$ | varied parameters in variation of parameters |
| $M(x,y)\,\mathrm dx + N(x,y)\,\mathrm dy = 0$ | first-order ODE written as a differential form |
| $\gamma$ | exponent of Bernoulli's equation |
| $\chi_0$, $\chi_1$, $\chi_2$ | coefficients of Riccati's equation $y' = \chi_2y^2 + \chi_1y + \chi_0$ (added 2026-10-14, arfken-2013) |
| $U(x,y)$ | potential of an exact differential form, $M\,\mathrm dx + N\,\mathrm dy = \mathrm dU$ (ODE pages only) |
| $x_a$, $x_b$ | ends of the interval of a boundary-value problem |
| $y_b(x)$ | polynomial carrying inhomogeneous boundary values, subtracted to make them homogeneous |
| $v$ | auxiliary dependent variable introduced by a substitution |

## Transforms, separation and eigenfunctions

| Symbol | Meaning |
|---|---|
| $\tilde u(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} u(x)\,e^{-ikx}\,\mathrm dx$ | Fourier transform (symmetric convention) |
| $\bar u(p) = \int_0^\infty u(t)\,e^{-pt}\,\mathrm dt$ | Laplace transform; $p$ is the transform variable |
| $k$, $\mathbf k$ | wavenumber, wave vector; separation constant written $\pm k^2$ |
| $k_x$, $k_y$, $k_z$ | Cartesian components of $\mathbf k$ (separation constants of the Cartesian Helmholtz equation) (added 2026-10-14, arfken-2013) |
| $\omega$ | angular frequency |
| $X(x)$, $Y(y)$, $Z(z)$, $\mathcal T(t)$ | separated factors in Cartesian coordinates |
| $U(\mathbf x)$ | spatial factor of a space–time separation $u = U(\mathbf x)\mathcal T(t)$ |
| $R(r)$, $\Theta(\theta)$, $\Phi(\phi)$ | separated factors in polar coordinates; $n$ is the azimuthal order (integer), $\ell$ the polar degree |
| $\ell$ | Legendre degree (bare $\ell$, no superscript) |
| $P_\ell$, $P_\ell^n$, $Q_\ell^n$ | Legendre and associated Legendre functions |
| $J_n$, $Y_n$ | Bessel functions of the first and second kind of order $n$ |
| $j_\ell$, $y_\ell$ | spherical Bessel functions, $j_\ell(kr) = \sqrt{\pi/(2kr)}\,J_{\ell+1/2}(kr)$, and the second solution $y_\ell$ (added 2026-10-14, arfken-2013) |
| $\varphi_n$, $\lambda_n$ | eigenfunctions and eigenvalues of a linear operator, $\mathcal L\varphi_n = \lambda_n\varphi_n$ (subscript $n$; never confuse with $\lambda^{(p)}$) |

## Green's functions

| Symbol | Meaning |
|---|---|
| $G(x, x')$, $G(\mathbf x, \mathbf x')$ | Green's function: $\mathcal L G = \delta(\mathbf x - \mathbf x')$, $\mathcal L$ acting on the first argument |
| $E_d(\mathbf x - \mathbf x')$ | fundamental solution of the Laplacian in $d$ dimensions, $\nabla^2 E_d = \delta$ (sources writing $\Phi$ map to it; $\Phi$ is the azimuthal separated factor) |
| $K(x, t)$ | heat kernel (fundamental solution of the diffusion equation) |
| $\mathbf x_j$, $q_j$ | positions and strengths of image sources |
| $\lvert\partial\Omega\rvert$, $\langle u\rangle_{\partial\Omega}$ | area (length) of the boundary; mean of $u$ over it |

## Hyperbolic systems and conservation laws (reserved)

Reserved for the hyperbolic-systems sources the bundle expects; no page
uses these yet.

| Symbol | Meaning |
|---|---|
| $m$ | number of components of a system |
| $f(u)$ | flux function in one space dimension: $\partial_t u + \partial_x f(u) = 0$ |
| $f_j(u)$ | flux in direction $x_j$: $\partial_t u + \sum_{j=1}^d \partial_{x_j} f_j(u) = 0$ |
| $A(u) = \partial f/\partial u$ | flux Jacobian ($f'(u)$ for a scalar law); $A_j(u)$ for $f_j$ |
| $\lambda^{(p)}(u)$, $p = 1, \dots, m$ | eigenvalues of $A(u)$ = characteristic speeds, ordered $\lambda^{(1)} \le \dots \le \lambda^{(m)}$ |
| $r^{(p)}$, $\ell^{(p)}$ | right and left eigenvectors of $A(u)$ (the parenthesised superscript distinguishes $\ell^{(p)}$ from the Legendre degree $\ell$) |
| $w^{(p)}$ | characteristic variables (Riemann invariants where they exist) |
| $u_L$, $u_R$ | left and right states of Riemann data |

The shock speed is not yet registered; the Laplace variable was given the
symbol $p$, not $s$, to leave $s$ free for it.
