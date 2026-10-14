---
type: Definition
title: "Notation registry"
description: "Normative symbol registry — every concept page writes mathematics in this notation, never in paper-native symbols."
status: established
tags: [notation, meta]
timestamp: 2026-10-14T00:00:00Z
---

# Notation registry

This page is **normative** for the bundle. Concept pages must use these symbols
exclusively; each Source page maps its source's native notation to this registry
in a `# Notation map` section. Extend this registry (and record the extension in
[the log](/log.md)) before writing math that needs a symbol it lacks.

The registry was seeded once, at scaffolding (2026-10-13), from the conventions
dominant in numerical linear algebra and elliptic PDE theory, with Riley, Hobson
& Bence as the base for the continuum part. It is wiki-native law from then on.
Where a choice departs from a common alternative, the alternative is named so
that later sources map onto it in one line.

## Vector spaces and inner products

| Symbol | Meaning |
|---|---|
| $V$, $W$ | (linear) vector spaces over $\mathbb C$ (or $\mathbb R$) |
| $N$, $M$ | dimensions: $N=\dim V$, $M=\dim W$; $N$ is also the number of unknowns of a linear system |
| $\mathbf x$, $\mathbf y$, $\mathbf a$, $\mathbf b$ | vectors (bold lower case); also their column matrices in a fixed basis — the registry does not distinguish a vector from its column of components |
| $\mathbf z$, $\hat{\mathbf z}$ | further generic vectors; a hat marks a unit vector |
| $\lambda$, $\mu$ | generic scalars in linearity statements (distinct from eigenvalues $\lambda_k$, which carry an index) |
| $\mathbf x'$, $\mathbf e'_j$, $A'$ | primes mark components, basis vectors and matrices in a transformed basis |
| $x_i$ | $i$-th component of $\mathbf x$ in the chosen basis |
| $\mathbf e_i$ | basis vectors, $i=1,\dots,N$; orthonormal when $\langle\mathbf e_i,\mathbf e_j\rangle=\delta_{ij}$ |
| $\delta_{ij}$ | Kronecker delta |
| $\langle\mathbf a,\mathbf b\rangle$ | inner product, **conjugate-linear in the first argument**, linear in the second; $\langle\mathbf a,\mathbf b\rangle=\mathbf a^{\mathsf H}\mathbf b$ in an orthonormal basis (sources linear in the first argument map by swapping arguments) |
| $\lVert\mathbf a\rVert$ | norm induced by the inner product, $\langle\mathbf a,\mathbf a\rangle^{1/2}$ |
| $\Gamma$, $\Gamma_{ij}$ | Gram matrix of a basis, $\Gamma_{ij}=\langle\mathbf e_i,\mathbf e_j\rangle$ |
| $\bar z$ | complex conjugate of a scalar, a function, or (elementwise) a matrix |

## Matrices and linear operators

| Symbol | Meaning |
|---|---|
| $\mathcal A$ | abstract linear operator $V\to W$ (basis-free) |
| $A$, $a_{ij}$ | matrix of $\mathcal A$ in chosen bases, and its entries (row $i$, column $j$) |
| $I$, $I_N$ | identity matrix (of order $N$); $0$ the null matrix |
| $A^{\mathsf T}$ | transpose |
| $A^{\mathsf H}$ | Hermitian conjugate (conjugate transpose), $A^{\mathsf H}=\bar A^{\mathsf T}$; also written $A^\dagger$ or $A^*$ in sources |
| $A^{-1}$ | inverse |
| $\operatorname{tr}A$ | trace |
| $\det A$ | determinant |
| $C_{ij}$ | cofactor of $a_{ij}$: $(-1)^{i+j}$ times the determinant of $A$ with row $i$ and column $j$ deleted |
| $\operatorname{adj}A$ | adjugate, $\operatorname{adj}A=C^{\mathsf T}$ |
| $A_i$ | (Cramer's rule only) $A$ with column $i$ replaced by $\mathbf b$ |
| $\operatorname{rank}A$ | rank |
| $\mathcal R(A)$, $\mathcal N(A)$ | range and null space; $\dim\mathcal N(A)$ is the nullity |
| $\operatorname{diag}(d_1,\dots,d_N)$ | diagonal matrix |
| $\exp A$ | matrix exponential, $\sum_{n\ge0}A^n/n!$ |
| $[\mathbf c_1\ \cdots\ \mathbf c_N]$ | matrix with columns $\mathbf c_j$ |
| $[A,B]$ | commutator $AB-BA$ of square matrices or of operators (added 2026-10-14, arfken-2013) |
| $A\otimes B$ | direct (Kronecker) product: for $A$ of size $M\times N$, the $MM'\times NN'$ block matrix $(a_{ij}B)$ (added 2026-10-14, arfken-2013) |
| $\varepsilon_{i_1i_2\cdots i_N}$ | Levi-Civita symbol: $+1$ ($-1$) for an even (odd) permutation of $1,\dots,N$, $0$ otherwise (added 2026-10-14, arfken-2013) |
| $\mathcal A^{\mathsf H}$ | Hilbert-space adjoint of an abstract operator, $\langle f,\mathcal Ag\rangle=\langle\mathcal A^{\mathsf H}f,g\rangle$ for all $f$, $g$ of the space (boundary conditions enter through the space); its matrix in an orthonormal basis is $A^{\mathsf H}$. Distinct from the formal adjoint $\mathcal L^{*}$ of a differential operator (added 2026-10-14, arfken-2013) |

## Eigenproblems, forms and decompositions

| Symbol | Meaning |
|---|---|
| $\lambda_k$, $\mathbf q_k$ | eigenpair of a square matrix, $A\mathbf q_k=\lambda_k\mathbf q_k$, $\mathbf q_k\neq\mathbf 0$ |
| $\Lambda$ | $\operatorname{diag}(\lambda_1,\dots,\lambda_N)$ |
| $Q$ | matrix whose columns are eigenvectors, $Q=[\mathbf q_1\ \cdots\ \mathbf q_N]$; unitary when they are orthonormal |
| $S$ | non-singular change-of-basis (similarity) matrix, $A'=S^{-1}AS$; $A'$ the transformed matrix |
| $\rho(A)$ | spectral radius $\max_k\lvert\lambda_k\rvert$ (reserved for iteration theory; not used by the founding source) |
| $R_A(\mathbf x)$ | Rayleigh quotient $\mathbf x^{\mathsf H}A\mathbf x/\mathbf x^{\mathsf H}\mathbf x$ |
| $R_{\mathcal L}(u)$ | Rayleigh quotient of an operator, $\langle u,\mathcal Lu\rangle/\langle u,u\rangle$ (the "expectation value" of physics texts when $\lVert u\rVert=1$) (added 2026-10-14, arfken-2013) |
| $\lambda_{\min}$, $\lambda_{\max}$ | algebraically smallest and largest eigenvalue (added 2026-10-14, arfken-2013) |
| $\tilde u$ | trial function of the variation method (added 2026-10-14, arfken-2013) |
| $\vartheta$ | rotation angle of one step of the Jacobi eigenvalue method (added 2026-10-14, arfken-2013) |
| $\Theta$ | upper-triangular coefficient matrix of Gram–Schmidt, $\hat{\mathbf z}_m=\sum_{l\le m}\Theta_{lm}\mathbf y_l$ (added 2026-10-14, arfken-2013) |
| $U$, $\Sigma$, $V$ | singular value decomposition $A=U\Sigma V^{\mathsf H}$ ($U$ is $M\times M$ unitary, $\Sigma$ is $M\times N$ diagonal, $V$ is $N\times N$ unitary) — on SVD pages only |
| $\sigma_k$; $\mathbf u_k$, $\mathbf v_k$ | singular values ($\sigma_1\ge\sigma_2\ge\dots\ge0$); left and right singular vectors |
| $p$, $r$ | (SVD pages) $p=\min(M,N)$; $r$ the number of non-zero singular values |
| $\Sigma^{+}$, $A^{+}$ | $\Sigma^{+}$: $N\times M$, transpose of $\Sigma$ with each non-zero $\sigma_k$ replaced by $1/\sigma_k$; $A^{+}=V\Sigma^{+}U^{\mathsf H}$ |
| $L$, $U$ | (LU pages only) unit lower and upper triangular factors, $A=LU$; Cholesky $A=LL^{\mathsf H}$ with $L$ lower triangular, not unit. $U$ never denotes both the LU factor and the SVD factor on one page |

## Linear systems and iterations

| Symbol | Meaning |
|---|---|
| $A\mathbf x=\mathbf b$ | the linear system; $A$ is $M\times N$ in general, $N\times N$ when square |
| $\mathbf x^\star$ | exact solution |
| $\mathbf x^{(k)}$ | $k$-th iterate, $k=0,1,\dots$ (iteration index always a parenthesised superscript) |
| $\mathbf e^{(k)}$ | error $\mathbf x^{(k)}-\mathbf x^\star$ (distinct from the basis vectors $\mathbf e_i$, which carry a subscript) |
| $\mathbf r^{(k)}$ | residual $\mathbf b-A\mathbf x^{(k)}$ (always with superscript; the bare $\mathbf r$ is a position vector) |
| $D$, $E$, $F$ | splitting $A=D-E-F$: $D$ the diagonal of $A$, $-E$ its strictly lower part, $-F$ its strictly upper part |
| $T$, $\mathbf c$ | iteration matrix and constant vector of a stationary iteration $\mathbf x^{(k+1)}=T\mathbf x^{(k)}+\mathbf c$ |
| $T_{\mathrm J}$, $T_{\mathrm{GS}}$ | Jacobi iteration matrix $D^{-1}(E+F)$; Gauss–Seidel iteration matrix $(D-E)^{-1}F$ |
| $\theta_i$, $\eta_i$ | coefficients of the tridiagonal elimination sweep, $x_{i-1}=\theta_{i-1}x_i+\eta_{i-1}$ |

A tridiagonal matrix is written with the general entries: subdiagonal
$a_{i,i-1}$, diagonal $a_{ii}$, superdiagonal $a_{i,i+1}$.

## Scalar nonlinear equations

| Symbol | Meaning |
|---|---|
| $g(x)=0$ | scalar equation to be solved |
| $\xi$ | a real root, $g(\xi)=0$ |
| $x_k$ | $k$-th approximation |
| $\Phi$ | iteration function, $x_{k+1}=\Phi(x_k)$, $\xi=\Phi(\xi)$ |
| $\epsilon_k$ | error $x_k-\xi$ |
| $p$ | order of convergence (scalar-iteration pages only; distinct from the Sturm–Liouville coefficient $p(x)$) |
| $A_k$, $B_k$ | endpoints of a bracketing interval, $A_k<\xi<B_k$, $g(A_k)g(B_k)<0$ |
| $X$ | radicand in the square-root iteration $x_{k+1}=\tfrac12(x_k+X/x_k)$ |

## Function spaces and differential operators (one dimension)

| Symbol | Meaning |
|---|---|
| $[a,b]$ | interval |
| $w(x)$ | weight function, real and non-negative on $[a,b]$ |
| $f$, $g$ | generic functions in function-space identities (as well as source term and scalar equation on their own pages) |
| $\langle f,g\rangle_w$ | $\int_a^b\bar f(x)g(x)w(x)\,\mathrm dx$; subscript dropped when $w\equiv1$; $\lVert f\rVert_w=\langle f,f\rangle_w^{1/2}$ |
| $\mathcal L$ | linear differential operator |
| $\mathcal L^{*}$ | formal adjoint of $\mathcal L$ (by integration by parts) |
| $\lambda_n$, $\phi_n(x)$ | eigenvalues and eigenfunctions, $\mathcal L\phi_n=\lambda_n w\phi_n$; $\phi_n$ normalised, $\langle\phi_m,\phi_n\rangle_w=\delta_{mn}$, unless stated |
| $c_n$ | expansion coefficients, $u=\sum_n c_n\phi_n$ |
| $p(x)$, $q(x)$ | Sturm–Liouville coefficients: $\mathcal Lu=-(pu')'+qu$ (sign of $q$ fixed so; sources writing $-(pu')'-qu$ map $q\to-q$) |
| $p_1(x)$ | first-order coefficient of a general second-order equation $pu''+p_1u'-qu+\lambda wu=0$ before reduction to Sturm–Liouville form |
| $\mu$ | fixed constant in the shifted problem $\mathcal Lu-\mu wu=f$ |
| $\Psi(x)$ | integrating factor that brings a second-order equation to Sturm–Liouville form |
| $u_a(x)$, $u_b(x)$ | solutions of the homogeneous equation $\mathcal Lu=0$ that satisfy the boundary condition at $x=a$, respectively at $x=b$ (one-dimensional Green's-function construction) (added 2026-10-14, arfken-2013) |
| $\mathcal W(x)$ | Wronskian $u_a u_b'-u_a'u_b$ (added 2026-10-14, arfken-2013) |
| $\delta(x-x')$, $\delta(\mathbf r-\mathbf r')$ | Dirac delta |

## Elliptic boundary-value problems

| Symbol | Meaning |
|---|---|
| $\Omega\subset\mathbb R^d$ | domain; $d$ the space dimension |
| $\partial\Omega$ | its boundary (possibly several disconnected parts, possibly a surface at infinity); $\lvert\partial\Omega\rvert$ its area |
| $\hat{\mathbf n}$ | outward unit normal on $\partial\Omega$ |
| $\partial_n u$ | normal derivative $\nabla u\cdot\hat{\mathbf n}$ |
| $\mathrm dV$, $\mathrm dS$ | volume and surface elements |
| $\mathbf r$, $\mathbf r'$ | position vectors: field point and source point; $r=\lvert\mathbf r\rvert$ |
| $(x,y,z)$, $(x',y',z')$ | Cartesian coordinates of $\mathbf r$ and $\mathbf r'$ |
| $(r,\varphi)$, $(r',\varphi')$ | plane polar coordinates of $\mathbf r$ and $\mathbf r'$ |
| $\phi$, $\psi$ | generic scalar functions in integral identities (Green's theorems); an eigenfunction always carries a subscript, $\phi_n$ |
| $\nabla^2$ | Laplacian |
| $u$, $f$ | unknown and source term; **Poisson's equation is $\nabla^2u=f$** (sign convention: sources writing $-\nabla^2u=f$ map $f\to-f$, and their Green's function changes sign) |
| $\kappa$ | wavenumber in Helmholtz's equation $\nabla^2u+\kappa^2u=f$; the modified Helmholtz equation is $\nabla^2u-\kappa^2u=f$ with $\kappa>0$ (modified form added 2026-10-14, arfken-2013) |
| $H_0^{(1)}$, $K_0$ | Hankel function of the first kind and modified Bessel function of the second kind, both of order 0 (two-dimensional fundamental solutions) (added 2026-10-14, arfken-2013) |
| $P_l$, $\chi$, $r_<$, $r_>$ | Legendre polynomial of degree $l$; angle between $\mathbf r$ and $\mathbf r'$; smaller and larger of $\lvert\mathbf r\rvert$, $\lvert\mathbf r'\rvert$ (multipole expansion of $G_0$) (added 2026-10-14, arfken-2013) |
| $g_{\mathrm D}$, $g_{\mathrm N}$ | Dirichlet data ($u=g_{\mathrm D}$ on $\partial\Omega$) and Neumann data ($\partial_nu=g_{\mathrm N}$ on $\partial\Omega$) |
| $G(\mathbf r,\mathbf r')$ | Green's function, $\mathcal L_{\mathbf r}G=\delta(\mathbf r-\mathbf r')$ (for the Laplacian, $\nabla^2_{\mathbf r}G=\delta(\mathbf r-\mathbf r')$); $G(x,x')$ in one dimension |
| $G_0(\mathbf r,\mathbf r')$ | fundamental (free-space) solution, $G_0=-1/(4\pi\lvert\mathbf r-\mathbf r'\rvert)$ in $d=3$ |
| $H(\mathbf r,\mathbf r')$ | regular part, $G=G_0+H$, $\nabla^2H=0$ in $\Omega$ |
| $\langle u\rangle_{\partial\Omega}$ | mean of $u$ over $\partial\Omega$ |
| $\mathbf r_m$, $\alpha_m$ | image points (outside $\Omega$) and image strengths |
| $R$ | radius of a sphere or disc |

## Discretization

| Symbol | Meaning |
|---|---|
| $h$ | uniform mesh spacing |
| $\Delta x$, $\Delta y$ | directional spacings |
| $x_i$, $y_j$ | grid coordinates $x_0+i\Delta x$, $y_0+j\Delta y$ (the subscript-$i$ scalar $x_i$ is a vector component only on linear-algebra pages) |
| $u_{i,j}$ | grid value approximating $u(x_i,y_j)$; on a rectangle $0\le i\le N$, $0\le j\le M$ (grid index ranges, reusing $N$, $M$) |
| $\beta$ | squared aspect ratio $(\Delta x/\Delta y)^2$ |
| $\nabla_h^2$ | five-point discrete Laplacian |
