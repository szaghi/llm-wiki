---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-14T00:00:00Z
---

# Notation registry

Every concept page of this bundle writes mathematics in the symbols below.
A source's own symbols are translated on its Source page (`# Notation map`).
The registry was seeded on 2026-10-14 from the conventions that dominate the
numerical literature on spectral, discontinuous Galerkin and quadrature
methods (Legendre $P_n$ on $[-1,1]$ with $P_n(1)=1$, Jacobi
$P_n^{(\alpha,\beta)}$, Ferrers functions with the Condon–Shortley phase,
DLMF-style $h_n$ for norms and $k_n$ for leading coefficients). Where a
founding textbook departs from them, the departure is recorded on its Source
page. Extend this registry, and log the extension, before writing a symbol it
lacks.

## 1. Variables, intervals, indices

| Symbol | Meaning | Note |
|---|---|---|
| $x$ | real variable of a polynomial family | on $[-1,1]$ for the Jacobi class, $[0,\infty)$ for Laguerre, $(-\infty,\infty)$ for Hermite |
| $z$ | complex variable; also the mapped variable of an interval change | |
| $[a,b]$ | interval of orthogonality or of integration | $a=-\infty$ or $b=\infty$ allowed |
| $\theta$, $\phi$ | polar and azimuthal angles; $x=\cos\theta$ for Legendre and Chebyshev arguments | $0\le\theta\le\pi$, $0\le\phi<2\pi$ |
| $\Omega$, $d\Omega$ | direction $(\theta,\phi)$ on the unit sphere; $d\Omega=\sin\theta\,d\theta\,d\phi$ | |
| $\gamma$ | angle between two directions $\Omega$ and $\Omega'$ | $\cos\gamma=\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi')$ |
| $n$, $m$ | polynomial degree indices; $m$ is also the order of associated functions | |
| $\ell$ | degree of an associated Legendre function or spherical harmonic | scalar index, written without argument |
| $\nu$ | order of a Bessel function (real) | |
| $t$ | auxiliary variable of a generating function | |
| $r$, $r'$, $r_<$, $r_>$ | radial distances; $r_<=\min(r,r')$, $r_>=\max(r,r')$ | |

## 2. Orthogonality and expansions

| Symbol | Meaning | Note |
|---|---|---|
| $\omega(x)$ | weight function, $\omega>0$ on $(a,b)$ | never $w(x)$: $w_j$ are quadrature weights |
| $\langle f,g\rangle_\omega$ | $\int_a^b f(x)\,g(x)\,\omega(x)\,dx$ | complex conjugate on $f$ when complex |
| $p_n(x)$ | generic member of degree $n$ of an orthogonal polynomial sequence | |
| $h_n$ | norm constant, $h_n=\langle p_n,p_n\rangle_\omega$ | |
| $k_n$ | leading coefficient of $p_n$ ($p_n=k_nx^n+\dots$) | |
| $\delta_{nm}$ | Kronecker delta | |
| $c_n$ | coefficient of an orthogonal expansion $f=\sum_n c_np_n$ | $c_n=\langle f,p_n\rangle_\omega/h_n$ |
| $p(x)$, $q(x)$ | coefficient polynomials of the differential equation $p\,y''+q\,y'+\lambda y=0$ (degrees $\le2$ and $\le1$) | §12.1 setting of Arfken |
| $\lambda_n$ | eigenvalue of that equation for the degree-$n$ polynomial solution | |
| $g(x,t)$ | generating function | |

## 3. Classical orthogonal polynomials

| Symbol | Meaning | Standardization |
|---|---|---|
| $P_n(x)$ | Legendre polynomial | $P_n(1)=1$; $\omega=1$ on $[-1,1]$ |
| $Q_n(x)$ | Legendre function of the second kind | scale fixed so that $Q_n$ obeys the $P_n$ recurrences; $Q_0=\tfrac12\ln\frac{1+x}{1-x}$ |
| $P_n^{(\alpha,\beta)}(x)$ | Jacobi polynomial, $\omega=(1-x)^\alpha(1+x)^\beta$ | reserved: neither founding source treats it |
| $C_n^{(\lambda)}(x)$ | Gegenbauer (ultraspherical) polynomial, $(1-2xt+t^2)^{-\lambda}=\sum_n C_n^{(\lambda)}t^n$ | $\lambda=\tfrac12$ gives $P_n$ |
| $T_n(x)$ | Chebyshev polynomial of the first kind, $T_n(\cos\theta)=\cos n\theta$ | $\omega=(1-x^2)^{-1/2}$ |
| $U_n(x)$ | Chebyshev polynomial of the second kind, $U_n(\cos\theta)=\sin(n+1)\theta/\sin\theta$ | $\omega=(1-x^2)^{1/2}$ |
| $V_n(x)$, $W_n(x)$ | non-polynomial Chebyshev solutions $\sin n\theta$ and $\cos(n+1)\theta/\sin\theta$ | as in both founding sources |
| $H_n(x)$ | Hermite polynomial ("physicists'"), $\omega=e^{-x^2}$, leading coefficient $2^n$ | |
| $\mathit{He}_n(x)$ | Hermite polynomial ("probabilists'"), $\omega=e^{-x^2/2}$ | reserved: neither founding source uses it |
| $L_n(x)$ | Laguerre polynomial, $\omega=e^{-x}$ on $[0,\infty)$ | $L_n(0)=1$ |
| $L_n^{(\alpha)}(x)$ | associated (generalized) Laguerre polynomial, $\omega=x^\alpha e^{-x}$ | $L_n^{(m)}=(-1)^m\frac{d^m}{dx^m}L_{n+m}$ for integer $m$ |

## 4. Functions on the sphere

| Symbol | Meaning | Convention |
|---|---|---|
| $P_\ell^m(x)$ | associated Legendre function of the first kind (Ferrers function), integer $0\le m\le\ell$ | **with** the Condon–Shortley phase: $P_\ell^m=(-1)^m(1-x^2)^{m/2}\frac{d^m}{dx^m}P_\ell$; for $-\ell\le m<0$, $P_\ell^{-m}=(-1)^m\frac{(\ell-m)!}{(\ell+m)!}P_\ell^m$ |
| $Q_\ell^m(x)$ | associated Legendre function of the second kind | |
| $Y_\ell^m(\theta,\phi)$ | spherical harmonic, $Y_\ell^m=\sqrt{\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}}\,P_\ell^m(\cos\theta)\,e^{im\phi}$ | orthonormal on the sphere; $Y_\ell^{-m}=(-1)^m\big(Y_\ell^m\big)^*$ |

## 5. Bessel functions

| Symbol | Meaning | Note |
|---|---|---|
| $J_\nu(x)$ | Bessel function of the first kind | |
| $Y_\nu(x)$ | Bessel function of the second kind (Weber/Neumann) | never $N_\nu$ |
| $H_\nu^{(1)}(x)$, $H_\nu^{(2)}(x)$ | Hankel functions $J_\nu\pm iY_\nu$ | |
| $I_\nu(x)$, $K_\nu(x)$ | modified Bessel functions | $K_\nu=\frac{\pi}{2}i^{\nu+1}H_\nu^{(1)}(ix)$ |
| $j_\ell(x)$, $y_\ell(x)$ | spherical Bessel functions $\sqrt{\pi/2x}\,J_{\ell+1/2}$, $\sqrt{\pi/2x}\,Y_{\ell+1/2}$ | never $n_\ell$ |
| $h_\ell^{(1)}(x)$, $h_\ell^{(2)}(x)$ | spherical Hankel functions $j_\ell\pm iy_\ell$ | |
| $i_\ell(x)$, $k_\ell(x)$ | modified spherical Bessel functions $\sqrt{\pi/2x}\,I_{\ell+1/2}$, $\sqrt{2/\pi x}\,K_{\ell+1/2}$ | note the different prefactor of $k_\ell$ |
| $\alpha_{\nu,k}$ | $k$-th positive zero of $J_\nu$ | not $j_{\nu,k}$: $j$ is taken by $j_\ell$ |
| $\beta_{\nu,k}$ | $k$-th positive zero of $J_\nu'$ | |
| $A_\nu(z)$, $B_\nu(z)$ | the two asymptotic series of Hankel's expansion, $J_\nu\sim\sqrt{2/\pi z}\,[A_\nu\cos(\cdot)-B_\nu\sin(\cdot)]$ | Arfken writes $P_\nu$, $Q_\nu$ |
| $\Gamma(z)$ | gamma function | $\Gamma(n+1)=n!$ |
| $F(a,b,c;x)$, $M(a,c;x)$ | hypergeometric and confluent hypergeometric (Kummer) functions | used only to identify families; $a,b,c$ local parameters |
| $n!!$ | double factorial | $(2n-1)!!=1\cdot3\cdots(2n-1)$, $(-1)!!=1$ |

## 6. Quadrature, interpolation and bases

| Symbol | Meaning | Note |
|---|---|---|
| $I[f]$ | exact integral $\int_a^b f(x)\,\omega(x)\,dx$ | $\omega=1$ when no weight is written |
| $\mathcal Q_n[f]$ | $n$-point quadrature rule $\sum_{j=1}^n w_jf(x_j)$ | calligraphic: $Q_n$ is the Legendre function of the second kind |
| $x_j$ | quadrature or interpolation nodes, $j=1,\dots,n$ | the rule is named in words (Gauss–Legendre, Gauss–Lobatto, …), never by a superscript |
| $w_j$ | quadrature weights (Christoffel numbers for Gauss rules) | |
| $E_n[f]$ | quadrature error $\mathcal Q_n[f]-I[f]$ | sign: rule minus exact, as in Riley |
| $h$ | uniform spacing of an equally spaced rule, $h=(b-a)/N$ | unsubscripted; $h_n$ is a norm constant |
| $N$ | number of equal strips of an equally spaced rule | |
| $f_i$ | $f(x_i)$ at equally spaced points $x_i=a+ih$, $i=0,\dots,N$ | |
| $\langle f^{(k)}\rangle$ | an average of $f^{(k)}$ over $[a,b]$ | in the leading error terms |
| $\ell_j(x)$ | Lagrange cardinal polynomial of node $x_j$, $\ell_j(x_k)=\delta_{jk}$ | always written with subscript and argument; distinct from the scalar $\ell$ |
| $\mathcal V$ | (generalized) Vandermonde matrix $\mathcal V_{jk}=p_k(x_j)$ | reserved |
| $\Lambda_n$ | Lebesgue constant of an interpolation node set | reserved |

## 7. Derived functions and physical symbols

| Symbol | Meaning | Note |
|---|---|---|
| $\varphi_n(x)$ | weighted function $\sqrt{\omega}\,p_n$ of a family (Hermite function $e^{-x^2/2}H_n$, Laguerre function $e^{-x/2}L_n$) | the page names the family |
| $\mu_\ell$ | axial multipole moment $\sum_iq_ia_i^\ell$ | |
| $q_i$, $a_i$ | point charges and their positions on the polar axis | examples only |
| $\psi$, $\varepsilon_0$ | electrostatic potential, vacuum permittivity | examples only |

## Log of extensions

* 2026-10-14 — registry seeded at bundle scaffolding (sections 1–6).
