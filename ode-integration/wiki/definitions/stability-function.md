---
type: Definition
title: "Stability function, stability polynomial and stability region"
description: "The stability function R(z) is the factor by which a one-step method multiplies the solution of y' = λy per step; it is rational for implicit methods and a polynomial P(z) for explicit ones, its order and degree structure constrain the method, and its region of absolute stability decides the linearly stable step sizes for method-of-lines systems."
status: established
aliases: [linear stability function, amplification factor, stability polynomial, region of absolute stability, stability domain, linear stability region, real stability interval, real stability boundary]
tags: [stability, runge-kutta, explicit, implicit]
timestamp: 2026-10-20T16:00:00Z
---

# Stability function, stability polynomial and stability region

Applied to the Dahlquist test equation $y'=\lambda y$, a
[Runge–Kutta method](/definitions/runge-kutta-method.md) gives
$y_{n+1}=R(z)\,y_n$, $z=h\lambda$, with **stability function**

$$R(z)=1+z\,b^\top(I-zA)^{-1}\mathbf 1=\frac{\det(I-zA+z\mathbf 1b^\top)}{\det(I-zA)}$$

([Biswas et al. (2023)](/sources/biswas-2023.md), Eq. (9);
[Biswas et al. (2024)](/sources/biswas-2024.md), Eq. (5);
[Vermeire 2023](/sources/vermeire-2023.md), Eqs. (9)–(10)). For an explicit method the
denominator is 1 and $R(z)=\det(I-zA+z\mathbf 1b^\top)$, the form
[Belardo et al. (2026)](/sources/belardo-2026.md) use to scan families of embedded
weights (§3). For an explicit
method $A$ is nilpotent and $R$ is the **stability polynomial**

$$P(z)=1+\sum_{j=1}^{s}\theta_jz^j,\qquad \theta_j=b^\top A^{j-1}\mathbf 1,$$

of degree at most $s$ ([Biswas et al. (2025)](/sources/biswas-2025.md), §1;
[Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md), Eqs. (1)–(2)).
Order $p$ forces $\theta_j=1/j!$ for $j\le p$, so an explicit method has
$s-p$ free coefficients in $P$ (Hedayati Nasab et al. (2021), Eq. (3)); these
are the tall-tree [order conditions](/results/runge-kutta-order-conditions.md)
$T(p)$. The **region of absolute stability** is
$\mathcal S=\{z\in\mathbb C:\lvert R(z)\rvert\le1\}$.

## Method of lines: the step-size condition

For a semi-discretization $y'=Ly$ with diagonalizable $L$, linear stability
requires $h\lambda\in\mathcal S$ for every eigenvalue $\lambda$ of $L$; for a
given spectrum this fixes a maximal stable step, a function of the free
coefficients of $P$ (Hedayati Nasab et al. (2021), Eqs. (4)–(5)). Choosing
those coefficients to maximize the stable step for a given spectrum is the
subject of [optimal stability polynomials](/methods/optimal-stability-polynomial.md):
for flux-reconstruction DG spectra on six element types, the maximal stable
step grows about linearly with $s$, and the step per stage keeps increasing
beyond $s=16$ for orders 3 and 4 (§6). Eigenvalue analysis is only a necessary
condition when $L$ is not normal
([Sun et al. (2022)](/sources/sun-2022.md), §1); for inner-product norms the
energy approach of [strong stability](/properties/strong-stability.md) replaces
it.

[Fekete et al. (2022)](/sources/fekete-2022.md) (Defs. 1–4) characterize
$\mathcal S$ by four radii: real-axis inclusion (largest interval on the
negative real axis in $\mathcal S$), imaginary-axis inclusion (largest
$[-i\beta,i\beta]\subset\mathcal S$), circle contractivity (largest $r$ with
the disk $\lvert z+r\rvert\le r$ in $\mathcal S$) and the radius of absolute
monotonicity (largest $r$ such that $R$ and all its derivatives are
nonnegative on $(-r,0]$). The last one is the linear counterpart of the SSP
coefficient; see [SSP methods](/methods/strong-stability-preserving-runge-kutta.md).

**Imaginary-axis inclusion decides for nearly central spectra.**
[Kemm (2024)](/sources/kemm-2024.md) (§3.3, Figs. 1–2) studies low-Mach finite-volume
schemes whose acoustic viscosity scales with the flow speed: the eigenvalues of the
discretized advection operator lie on ellipses between the upwind circle and a segment of
the imaginary axis, and the integrator must be stable on the convex hull of these
ellipses, which forward Euler is not. Among explicit Runge–Kutta methods with the minimal
number of stages (2, 3, 4 and 6 stages for orders 2–5) only RK3 and RK4 have regions
covering it; RK2 and the six-stage fifth-order method do not. Among Adams–Bashforth
methods, whose root-locus curves he plots, order at least 3 is needed, at a Courant
number that shrinks with the order (see
[linear multistep methods](/methods/linear-multistep-method.md)). For orders 2–4 the
minimal-stage methods share their stability polynomial, the degree-$s$ Taylor polynomial
of $e^z$, so the choice of tableau does not change linear stability (§4).

**Real stability interval as a design indicator.** The real-axis inclusion (page-local
$\ell$: the largest $\ell$ with $\lvert R\rvert\le1$ on $[-\ell,0]$) is the usual
one-number summary for explicit methods. Its values for the classical $s$-stage
methods of order $s$ are 2, 2, 2.5127 and 2.7853 for $s=1,\dots,4$
([Bassenne et al. 2021](/sources/bassenne-2021.md), Table 1, which prints the rounded
values 2.00, 2.00, 2.50, 2.79; the four-digit values are a *compiler check, not in the
source*). Belardo et al. (2026, §3–4) use it to choose among embedded weight
vectors that share $(A,c)$ with a main method: the order-4 embedding of
Dormand–Prince 5(4) is one member of a one-parameter family, and another member has
$\ell\approx5.8$ against 4.4 for the standard one *(compiler check from the printed
weights, not in the source)*. They warn that $\ell$ alone does not decide the choice: for
Bogacki–Shampine 3(2) on a stiff scalar problem the embedding that minimizes the
number of accepted steps has a *smaller* $\ell$ (2.41) than the standard one (3.15)
(Tables 2–3); see [embedded pairs](/methods/embedded-runge-kutta-pair.md).
[Faleichik & Moisa (2026)](/sources/faleichik-2026.md) (§1, §3) replace the stability
interval by the **monotonicity interval**, the longest $(-\varrho,0]$ on which $P>0$
and $P'\ge0$ (page-local $\varrho$), as for the exponential, and measure accuracy by
the error constant $(1-P'''(0))/6$ of a second-order polynomial.

## Stability polynomials of stabilized methods

For many-stage explicit methods the polynomial is chosen from an orthogonal family
whose real stability interval grows like $s^2$ (see
[stabilized explicit Runge–Kutta methods](/methods/stabilized-explicit-runge-kutta.md)).
Runge–Kutta–Chebyshev methods have

$$P(z)=\mathsf a_s+\mathsf b_sT_s(\omega_0+\omega_1z),\qquad \ell=\frac{2\omega_0}{\omega_1},$$

with $T_s$ the Chebyshev polynomial of the first kind, $\omega_0=1+\varepsilon_{\mathrm d}/s^2$ a
shift with damping parameter $\varepsilon_{\mathrm d}$, and $\mathsf a_s$, $\mathsf b_s$, $\omega_1$
fixed by the order (page-local symbols); $\ell\ge(2-\frac43\varepsilon_{\mathrm d})s^2$ at
first order and $\ell\ge\frac23(1-\frac2{15}\varepsilon_{\mathrm d})(s^2-1)$ at second
([Croci & Rosilho de Souza 2022](/sources/croci-2022.md), §2.2, Eqs. (11)–(12)).
Runge–Kutta–Legendre methods replace $T_s$ by the Legendre polynomial with
$\omega_0=1$ and no damping ([Dawes 2021](/sources/dawes-2021.md), §3, Eq. (7)).
The stage polynomials of the recurrence are the internal stability polynomials
(Croci & Rosilho de Souza 2022, Lemma 3.1), which govern the propagation of stage
perturbations; see [internal stability](/definitions/internal-stability.md). For a
linear system $y'=Ly$ one step is the matrix $P(hL)$, and Dawes (2021, §5–7) reads
monotonicity and positivity off the signs of its entries, which depend on the
boundary closure in $L$ and not only on $P$; see
[positivity preservation](/properties/positivity-preservation.md).

Polynomials of degree above 100 for hyperbolic spectra are parametrized by the roots
$\tilde r_j$ of $(P-1)/z$, $P(z)=1+z\prod_j(1-z/\tilde r_j)$; since $P(\tilde r_j)=1$,
these roots lie on the boundary of $\mathcal S$
([Doehring et al. 2024](/sources/doehring-2024.md), §2.2, Eqs. (2.10)–(2.11));
see [optimal stability polynomials](/methods/optimal-stability-polynomial.md).

## Structure of rational stability functions

Write $R=N/D$ with coprime polynomials (page-local $N$, $D$). Biswas et al.
(2024) use three facts:

* **Order barriers** (as recalled from Hairer–Wanner Thms. IV.3.11, IV.4.18
  and Nørsett–Wolfbrandt): if $N/D=e^z+O(z^{p+1})$ then
  $p\le\deg N+\deg D$; if all poles are real, $p\le\deg N+1$ (Thm. 3.7). The
  first is attained by Padé approximants; DIRKs have real poles $1/a_{ii}$.
* **Degree bound** (Thm. 3.8): $\deg N,\deg D\le\dim\mathcal Y$, where
  $\mathcal Y$ is the smallest $A^\top$-invariant subspace
  containing $b$. With the order barriers this gives
  $\lfloor(p+1+\delta_{\mathrm{SA}})/2\rfloor\le\dim\mathcal Y$, and
  $p\le\dim\mathcal Y+1-\delta_{\mathrm{SA}}$ for DIRKs, with
  $\delta_{\mathrm{SA}}=1$ for [stiffly accurate](/properties/stiff-accuracy.md)
  methods with invertible $A$ and 0 otherwise (page-local; Thm. 3.9).
* **Orthogonal-polynomial form** (Lemma 5.2): if $p\ge\dim\mathcal Y$, $R$ is
  determined by the coefficients of the minimal polynomial of $\mathcal Y$ in
  a family of polynomials orthogonal for the functional with moments
  $1/(n+1)!$.

For explicit methods the same chain reads
$p\le\deg P\le\dim\mathcal Y\le s-\dim\mathcal K_{q_{\mathrm w}}$, with $\mathcal K_{q_{\mathrm w}}$ the Krylov space of
stage-order residuals that [weak stage order](/definitions/weak-stage-order.md)
makes orthogonal to $b$. Hence weak stage order $q_{\mathrm w}$ forces the
highest $q_{\mathrm w}-1$ coefficients of $P$ to vanish, dual to order $p$
fixing the lowest $p+1$, and explicit methods with the minimum number of
stages for given $(p,q_{\mathrm w})$ have $P(z)=\sum_{j=0}^pz^j/j!$ exactly
(Biswas et al. (2025), Lemma 2.1, Thm. 2.6, §7).

## Padé approximations

The $(m,k)$ Padé approximation of $e^z$ (numerator degree $m$, denominator
degree $k$, as Sun et al. (2022) use the labels) has order $m+k$. Sun et al.
(2022, §1) recall: the diagonal $(s,s)$ approximations are A-stable and are
the stability functions of the Gauss collocation methods; the first and second
subdiagonals are A-stable; the others are not. The diagonal coefficients are
$N(z)=\sum_{i=0}^s\frac{s!\,(2s-i)!}{(2s)!\,i!\,(s-i)!}z^i$, $D(z)=N(-z)$ (Eq.
(5.1)). The $(0,3)$ approximation is A($\alpha$)-stable with
$\alpha\approx88.23^\circ$ (Ex. 4.5). Since their energy analysis uses only
$R$, it applies to any linear one-step method with rational $R$, without a
tableau (§3); the unconditional energy law of diagonal Padé schemes is on
[diagonal Padé strong stability](/results/diagonal-pade-strong-stability.md).

A rational approximation of $e^z$ can also be used directly as a time integrator,
without a Runge–Kutta tableau. [Song & Eisenträger (2022)](/sources/song-2022.md)
(§2.2, App. B) replace the matrix exponential of the exact one-step map of linear
structural dynamics by the $(m,m)$ diagonal Padé approximant, written unnormalized
($\hat N_m(z)=\sum_{j=0}^m\frac{(2m-j)!}{j!(m-j)!}z^j$, $\hat D_m(z)=\hat N_m(-z)$,
page-local), and factor $\hat D_m(z)=\prod_i(r_i-z)$ into real roots and
complex-conjugate pairs, each costing one linear solve. They state that Padé-based
integrators are unconditionally stable with spectral radius one; that holds for the
diagonal approximants on the undamped spectrum, where $\lvert R\rvert=1$ on the imaginary
axis and at infinity, so these schemes are A-stable and not L-stable *(compiler check, not
in the source)*. On linear problems their propagator is the stability function of the
$m$-stage Gauss method *(compiler remark, not in the source)*. See
[Padé time integration](/methods/pade-time-integration.md).

## Stability functions of other method families

* **Rosenbrock–Wanner methods.** [Steinebach (2023)](/sources/steinebach-2023.md)
  (Eq. (2.14)) writes $R$ as a polynomial of degree $s$ in $z/(1-\gamma z)$
  whose coefficients are sums of products of the method coefficients (Scholz's
  sums). The embedded method of Rodas5 is not A-stable (Fig. 1), which can
  force step reductions for eigenvalues near the imaginary axis; Rodas5P and
  its embedded method are A-stable (Fig. 2). See [Rodas5P](/methods/rodas5p.md).
* **Deferred correction and ADER.** [Han Veiga et al. (2021)](/sources/hanveiga-2021.md)
  (§5.1, Fig. 2) compute the regions of explicit ADER and explicit DeC
  numerically on a grid of $z$: they coincide for orders 2–5, do not depend on
  the node family (equispaced, Gauss–Legendre, Gauss–Lobatto) and grow with
  order. An analytic treatment "is not feasible" because it leads to
  polynomial inequalities of degree $p(p+1)$. The coincidence has since been proved for
  the DeC side: [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) (Thm. 6.1) show
  that every bDeC method of order $K$, and its variants that add subnodes between
  iterations, has $R(z)=\sum_{j=0}^Kz^j/j!$ for any distribution of subnodes, because the
  Butcher matrix is block-nilpotent with $A^K=0$; the sDeC branch has node-dependent regions
  (Fig. 3). They define the region with the strict inequality $\lvert R\rvert<1$ (Eq.
  (40)). The implicit Gauss–Legendre ADER-DG solver iterated to convergence has
  $R(z)=\det(I-zB+z\mathbf 1w^\top)/\det(I-zB)$, numerator of degree $\mathsf M$ and
  denominator of degree $\mathsf M+1$ by a rank computation for $\mathsf M\le80$
  ([Popov 2024](/sources/popov-2024.md), §1.2, Eq. (15)); a compiler check matches it to
  the $(\mathsf M,\mathsf M+1)$ Padé approximant for $\mathsf M\le12$ (details on
  [ADER](/methods/ader-time-integration.md)). See
  [deferred correction](/methods/deferred-correction.md).
* **Spectral deferred correction with a fixed number of sweeps.** On $y'=\lambda y$ the
  sweep error obeys $\mathbf e^{(k+1)}=\mathcal K(z)\mathbf e^{(k)}$ with
  $\mathcal K(z)=z(I-zQ_\Delta)^{-1}(Q-Q_\Delta)$ (page-local $\mathcal K$), whose limits
  $Q-Q_\Delta$ ($z\to0$) and $I-Q_\Delta^{-1}Q$ ($\lvert z\rvert\to\infty$) govern
  non-stiff and stiff convergence ([Čaklović et al. 2025](/sources/caklovic-2025.md), §2.2,
  Eqs. (2.12)–(2.13)). With $Q_\Delta=0$ (Picard) and $K$ sweeps the stability region is
  that of the $K$-stage explicit method of order $K$, never A-stable (§3.2, Fig. 5); the
  diagonal preconditioners and their plotted regions are on
  [parallel SDC](/methods/parallel-sdc.md).
* **Multiderivative methods.** An explicit method that uses $f$, $\dot f$ and higher
  derivatives has a polynomial $R$ whose degree can exceed the order: e.g.
  $R(z)=\sum_{k\le5}z^k/k!+z^6/600$ for the two-derivative three-stage fifth-order method of
  Chan & Tsai, and degree 9 for a three-derivative seventh-order method
  ([Chouchoulis et al. 2022](/sources/chouchoulis-2022.md), Fig. 1, App. A; table on
  [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)). For
  Lax–Wendroff-type discretizations of PDEs these regions do not predict the fully discrete
  Courant limit, because the discrete space operators that replace the time derivatives do
  not multiply like powers of one symbol; the limit comes from a
  [von Neumann analysis](/definitions/von-neumann-stability-analysis.md) (§5).
* **Parareal.** Applied to a (partitioned) Dahlquist problem, a whole Parareal run with
  coarse and fine propagators $\mathcal G$, $\mathcal F$ is a linear map with a stability
  function built from the error-propagation matrix $\mathbf E=I-\mathbf M_{\mathcal G}^{-1}\mathbf M_{\mathcal F}$
  ($\mathbf M_{\mathcal G}$, $\mathbf M_{\mathcal F}$ page-local all-slice matrices): after
  $k$ iterations $R=\mathbf c_2^\top\big(\sum_{j=0}^k\mathbf E^j\big)\mathbf M_{\mathcal G}^{-1}\mathbf c_1$
  ($\mathbf c_1$, $\mathbf c_2$ page-local selection vectors;
  [Buvoli & Minion 2024](/sources/buvoli-2024.md), Eqs. (30)–(37), after Ruprecht). The
  two-parameter function $R(z_1,z_2)$ of each exponential propagator enters through
  $\mathbf M_{\mathcal G}$, $\mathbf M_{\mathcal F}$ (§5). $\mathbf E$ is nilpotent,
  so its spectrum does not give the convergence rate; $\lVert\mathbf E\rVert_\infty<1$ gives
  monotone convergence (Eqs. (39)–(40)). For parabolic problems
  [Jin et al. (2025)](/sources/jin-2025.md) (§3) go further and **design** the coarse
  propagator's stability function: for $y'=-\mu y$, $\mu>0$ (page-local), with
  $s=\Delta T\mu$ and $J$ fine steps per slice (page-local), the error factor of each mode
  is $\big(R_{\mathcal F}(-s/J)^J-R_{\mathcal G}(-s)\big)/\big(1-\lvert R_{\mathcal G}(-s)\rvert\big)$
  ($R_{\mathcal G}$, $R_{\mathcal F}$ the coarse and fine stability functions, page-local),
  and they minimize its supremum over a rational $R_{\mathcal G}$ of degree $(2,2)$ under
  linear order constraints and $\lvert R_{\mathcal G}\rvert<1$ on the negative real axis,
  enforced at the critical points of $R_{\mathcal G}$ (Eqs. (3.1)–(3.7), Prop. 3.3). The
  optimized factor is about 0.013–0.014 against 0.298 for backward Euler with Lobatto IIIC
  fine propagators (Table 4.1). See [Parareal](/methods/parareal.md).
* **TASE operators.** Preconditioning the right-hand side of an explicit
  Runge–Kutta method by a time-accurate stabilizing operator makes the stability
  function rational, $R(z)=N(z)/D(z)$ with
  $D(z)=\prod_{i=0}^{p_{\mathrm T}-1}(2^i-\alpha z)^s$ for a TASE operator of order
  $p_{\mathrm T}$ with parameter $\alpha>0$ (page-local); the poles $2^i/\alpha$ are
  positive, so $R$ is analytic in the left half-plane, and A-stability reduces to a
  bound on the imaginary axis, checked numerically
  ([Bassenne et al. 2021](/sources/bassenne-2021.md), §3.2, Eqs. (24)–(27), Fig. 4).
  Equivalently $R$ is the explicit method's polynomial composed with the TASE map of
  $z$ *(compiler check, not in the source)*. When the TASE operator is built on a matrix
  $\tilde J\ne J$ (page-local), [Conte et al. (2024)](/sources/conte-2024.md) (§3,
  Eq. (3.4), Lemma 3.4) test on $y'=(\lambda+\lambda_E)y$ with $\lambda$ an eigenvalue of
  $\tilde J$ and $\lambda_E$ one of $J-\tilde J$, and obtain a **two-parameter stability
  function** $P\big(\hat{\mathcal P}_p(h\lambda)(1+\mu)\big)$, $\mu=\lambda_E/\lambda$,
  with $P$ the explicit stability polynomial and $\hat{\mathcal P}_p$ the scalar TASE map
  (page-local). Its stability set in the $\mu$-plane is the explicit region
  $\mathcal S$, rotated by $180^\circ$, scaled and shifted by $-1$; these "stability
  diagrams" shrink monotonically with $h$ to an unconditional diagram. See
  [TASE operators](/methods/tase-operators.md) and
  [A-stability](/properties/a-stability.md).
* **Partitioned methods.** A partitioned Runge–Kutta method has a matrix-valued
  stability function, and absolute stability of each member for its own eigenvalues
  does not imply stability of the coupled method; for paired explicit families it is
  observed to suffice, and checked by the spectral radius of the fully discrete
  matrix ([Doehring et al. 2025](/sources/doehring-2025.md), §2.2, Eq. (2.12), §5.1;
  [paired explicit Runge–Kutta methods](/methods/paired-explicit-runge-kutta.md)).
* **Exponential integrators with a partial linear part.** When only a fraction
  $\vartheta\in[0,1]$ (page-local) of a diffusion operator is put in the linear part
  that an [exponential integrator](/methods/exponential-integrators.md) treats exactly,
  the heat equation written as $\vartheta\Delta+(1-\vartheta)\Delta$ gives, per Fourier
  mode with $z=-hk^2\le0$ the symbol of the whole operator, a **two-parameter stability
  function** $\Phi(z,\vartheta)$ (page-local), and the scheme is called unconditionally
  stable if $\lvert\Phi\rvert\le1$ on the whole negative real axis
  ([Caliari et al. (2024)](/sources/caliari-2024.md), §2, Eq. (1)). The paper proves
  closed forms and thresholds: exponential Euler, $\Phi=1+z\phi_1(\vartheta z)$, needs
  $\vartheta\ge\tfrac12$ (Thm. 2.1); Lawson–Euler, $\Phi=e^{\vartheta z}(1+(1-\vartheta)z)$,
  needs $\vartheta\ge0.218$ (Thm. 2.2); the new stabilized Lawson–Euler,
  $\Phi=1+ze^{\vartheta z}$, needs $\vartheta\ge1/(2e)\approx0.184$ (Thm. 2.3); the
  second-order exponential Runge–Kutta methods need $\vartheta\ge1/(1+c_2)$ with
  $\phi_2$ and $\vartheta\ge1/(1+2c_2)$ with $\phi_1$ only (Thms. 2.4–2.5); the
  Lawson2 schemes $\vartheta\ge0.301$ and the new stabilized Lawson2 $\vartheta\ge0.183$
  (Thms. 2.6–2.7, thresholds computed numerically); and two IMEX schemes, as quoted
  from Wang et al., $\vartheta\ge\tfrac12$ (Remark 2.1, Table 1). The stabilized schemes
  are not A-stable; their regions merely contain the negative real axis (Remark 2.2,
  Fig. 1). The Lawson functions have the form $e^{\vartheta z}P((1-\vartheta)z)$, with
  $P$ the polynomial of the underlying explicit method, so Lawson2a and Lawson2b share
  one function and their common threshold is no coincidence *(compiler check, not in
  the source: on a scalar linear problem the Lawson transform turns the step into the
  explicit method applied to $y'=(1-\vartheta)\lambda y$)*. The same split test on an IMEX pair is the
  stability analysis of the
  [explicit–implicit–null method](/methods/explicit-implicit-null-method.md); see
  also [Lawson methods](/methods/lawson-methods.md).
* **Nonlinearly partitioned and additive methods.** On the partitioned Dahlquist
  problem $y'=F(y,y)$, $F(u,v)=\lambda_1u+\lambda_2v$, an
  [NPRK method](/methods/nonlinearly-partitioned-runge-kutta.md) multiplies the
  solution by the additive Runge–Kutta stability function of its underlying tableaux
  $(A^{\{1\}},b^{\{1\}})$, $(A^{\{2\}},b^{\{2\}})$,

  $$R(z_1,z_2)=\frac{\det\big(I-z_1A^{\{1\}}-z_2A^{\{2\}}+\mathbf 1(z_1b^{\{1\}}+z_2b^{\{2\}})^\top\big)}{\det\big(I-z_1A^{\{1\}}-z_2A^{\{2\}}\big)},\qquad z_j=h\lambda_j$$

  ([Buvoli & Southworth (2025)](/sources/buvoli-2025.md), §4.5, Eq. (4.18);
  [Buvoli et al. (2026)](/sources/buvoli-2026.md), §2.3.2, Eq. (2.7)). For IMEX-NPRK methods the first argument $u$, hence $z_1$, is the implicitly treated one, as on the NPRK page. The test is
  representative of a nonlinear system only if the two partial Jacobians are
  simultaneously diagonalizable (Buvoli & Southworth (2025), SM2). A method implicit in
  one argument only cannot be A-stable, because $R(0,z_2)$ is an explicit stability
  polynomial (§4.5.2). Buvoli & Southworth add **stability in the coupled stiff
  limit**: with $z_2=\kappa z_1$ (page-local ratio $\kappa$, as on the NPRK page), require
  $\lim_{\lvert z_1\rvert\to\infty}\lvert R(z_1,\kappa z_1)\rvert\le1$ for all
  $\lvert\kappa\rvert\le1$, i.e. stability when the explicitly treated argument is as stiff
  as a fraction of the implicit one (Eqs. (4.24)–(4.26)). For a diagonally implicit
  method with nonzero diagonal the limit is a polynomial in $\kappa$, so by the maximum
  modulus principle the condition reduces to a cosine series in the angle
  $\omega$ of $\kappa=e^{\mathrm i\omega}$ staying $\le1$ on $[0,2\pi)$ (Props. SM3.1–SM3.2,
  Remark 2, Eq. (4.27)). The nonlinearly partitioned Euler step
  $y_{n+1}=y_n+hF(y_{n+1},y_n)$ has $R=(1+z_2)/(1-z_1)$ and passes (Eq. (5.2)).
  Buvoli et al. (2026, Thm. 3.2) prove when a different limit, taken at fixed $z_2$,
  $\lim_{\lvert z_1\rvert\to\infty}R(z_1,z_2)=0$ holds for multirate members (L-stability in the stiff $z_1$ limit; it neither implies nor follows from the coupled condition, *compiler remark*).
  Both papers plot conjugate-symmetric slices of the two-variable region in $z_2$
  for fixed $z_1$. These notions are separate from the multirate tests on
  [linear stability of multirate methods](/definitions/multirate-linear-stability.md).
* **Positive, conservative (Patankar) schemes.** Modified Patankar schemes cannot be
  applied to $y'=\lambda y$ and are nonlinear on linear problems.
  [Izgin et al. (2022)](/sources/izgin-2022.md) test them on the positive conservative
  system $y_1'=-ay_1+by_2$, $y_2'=ay_1-by_2$ (page-local $a,b\ge0$), whose steady states
  form a line. The Jacobian of the scheme's map at a steady state has eigenvalues $1$ and
  $R$, and they call $R$, as a function of $z_a=-ha$ and $z_b=-hb$, the **stability
  function** of the scheme: for a Runge–Kutta method it is the ordinary $R(z_a+z_b)$, for
  MPRK22(α) a function of $z_a+z_b$ only, $R_1(z)=\frac{2-2\alpha z-z^2}{2(1-z)(1-\alpha z)}$,
  and for the variant with non-conservative stages a genuinely two-variable function
  (Lemma 3.6, Remark 3.7). $\lvert R\rvert<1$ then gives Lyapunov stability of the steady
  state (Thm. 2.9); see
  [Lyapunov stability of positive, conservative schemes](/results/lyapunov-stability-positive-conservative-schemes.md).
  On the one-directional test $b=0$ both MPRK22 families have an amplification factor in
  $(0,1)$, which is why that test cannot tell them apart (§3.1).
* **Imaginary-axis expansion and L-stability conditions in tableau design.**
  [Ern & Guermond (2022)](/sources/ern-2022.md) design their seven-stage fifth-order
  method with one extra condition
  $\lvert R(\mathrm i\epsilon)\rvert=1+\rho_6\epsilon^6+O(\epsilon^8)$, $\rho_6=-0.009$
  (page-local $\epsilon$, $\rho_6$), negative so that the method is dissipative near the
  origin; $\lvert R(\mathrm iy)\rvert\le1$ for $y\in[-1.562,1.562]$ (§4.1, Fig. 1; printed
  with $\Re$ for $R$). [Ern & Guermond (2023)](/sources/ern-2023.md) (§4.1) give $\rho_6$ in
  terms of $b^\top A^kc$: $-2b^\top A^4c+2b^\top A^3c-b^\top A^2c+\tfrac1{36}$ for a third-order
  method, $-2b^\top A^4c+2b^\top A^3c-\tfrac1{72}$ at fourth order and
  $-2b^\top A^4c+\tfrac1{360}$ when the fifth-order linear conditions hold. For an EDIRK with
  $A^{\mathrm I}=\begin{pmatrix}0&0\\\tilde a&\tilde A\end{pmatrix}$ and weights
  $(b_1,\tilde b^\top)$ (page-local blocks),
  $R(z)=1+zb_1+z\tilde b^\top(I-z\tilde A)^{-1}(\mathbf 1+z\tilde a)$, and, given A-stability
  and invertible $\tilde A$, L-stability holds iff $b_1=\tilde b^\top\tilde A^{-1}\tilde a$
  and $\tilde b^\top\tilde A^{-1}\mathbf 1+\tilde b^\top\tilde A^{-2}\tilde a=1$ (Eqs.
  (73)–(75); they are the vanishing of the $z$ and constant terms of the expansion of $R$
  at infinity, *compiler check, not in the source*). For their three-stage third-order design the second
  condition has no solution, and minimizing $R(-\infty)$ gives an A-stable method with
  $R(-\infty)=1-\sqrt3$ (Eq. (81)). See
  [invariant-domain preserving time stepping](/methods/invariant-domain-preserving-time-stepping.md).
* **Stability polynomial as the design variable of an IMEX family.**
  [Vermeire & Hedayati Nasab (2021)](/sources/vermeire-2021.md) (§3.1, Eqs. (32)–(34),
  App. 1) build accelerated IMEX schemes AIMEX$s$,2 whose implicit part is a fixed
  two-implicit-stage SDIRK and whose explicit part has one free coefficient per added
  stage; the $s-2$ free coefficients $\theta_3,\dots,\theta_s$ of the second-order explicit
  stability polynomial determine these coefficients uniquely and sequentially, so a
  polynomial optimized for the spectrum of the explicitly treated elements fixes the
  tableau. Optimal four-stage polynomials allow 1.79–2.01 times the step of the
  three-stage IMEX3,2 for flux-reconstruction DG of degrees 1–8, and the gain grows
  about linearly with $s$, above 5 at $s=10$ (Table 1, Fig. 1); see
  [optimal stability polynomials](/methods/optimal-stability-polynomial.md).
* **Fully discrete amplification matrices of sequential partitioned updates.**
  [Maurya et al. (2021)](/sources/maurya-2021.md) advance the linearized Euler equations
  $u_t=L_1(p)$, $p_t=L_2(u)$ by forward Euler in $u$ followed by
  $p^{n+1}=p^n+h[(1-\vartheta)L_2(u^n)+\vartheta L_2(u^{n+1})]$ with weight $\vartheta$ (page-local),
  which uses only already updated values and needs no solve. A Fourier mode then has a
  $2\times2$ amplification matrix with eigenvalues
  $G_{1,2}=1-\frac{\vartheta a^2}2\mp\frac a2\sqrt{\vartheta^2a^2-4}$, $a$ the Courant number
  times the modified wavenumber of the spatial scheme (page-local; §2.1, Eq. (8)); the
  scheme is stable in the wave regime only for $\vartheta\ge1$ and neutrally stable,
  $\lvert G\rvert=1$, at $\vartheta=1$, up to a critical Courant number of 2 with second-order
  central differences and 0.91 with a compact scheme (Table 1). In the wave regime the
  eigenvalues are conjugate, so $\lvert G\rvert^2=\det=1+(1-\vartheta)a^2$ *(compiler check,
  not in the source)*. These amplification factors belong to the space–time scheme, not to
  a stability function of an ODE method; see
  [von Neumann analysis](/definitions/von-neumann-stability-analysis.md).
* **Multirate, IMEX and splitting methods** need several scaled eigenvalues or
  a matrix test problem; see
  [linear stability of multirate methods](/definitions/multirate-linear-stability.md).
  The internal stability function $(I-zA)^{-1}\mathbf 1$ of the stages enters
  their formulas ([Roberts et al. (2021)](/sources/roberts-2021.md), §3.4).

Classes of $\mathcal S$ — A-, L-, A($\alpha$)-stability — are on
[A-stability](/properties/a-stability.md).

## Qualifications

* Notation varies: Fekete et al. (2022) write $\psi(z)$, Hedayati Nasab et al.
  (2021) $P_{s,q}(z)$ with coefficients $\gamma_j$ and order $q$, Han Veiga et
  al. (2021) $\phi(z)$, Sun et al. (2022) $Q(Z)^{-1}P(Z)$ with $s$ the
  polynomial degree rather than the stage count; Dawes (2021) $E_s$ ("the
  exponential"), Bassenne et al. (2021) $\sigma(z)$, Croci & Rosilho de Souza (2022)
  $R_s(z)$, Faleichik & Moisa (2026) $R_s(x)$ on the real axis, Belardo et al. (2026)
  $\rho$ for the real stability interval, Conte et al. (2024) $R_{T_p}$ and
  $\tilde R_{T_p}(y,\mu)$, Abu-Labdeh et al. (2023) $r(z)$, Song & Eisenträger (2022)
  $e^x_M=P_M/Q_M$, Caliari et al. (2024) $\Phi(z,\lambda)$ with $\lambda$ the diffusion
  fraction (here $\vartheta$), Buvoli & Southworth (2025) $\epsilon$ for the stiffness
  ratio (here $\kappa$) and $\gamma(\theta)$ for the cosine series; Popov (2024) $E$ for the identity, $B$ and $w$ for the
  Butcher matrix and weights, and "L1-stable" for $R=\mathcal O(\lvert z\rvert^{-1})$;
  Micalizzi & Torlo (2024) $P$ for the order; Jin et al. (2025) $R(\lambda,\theta)$ and
  $r(\lambda)$ as functions of $\lambda=-z>0$ with parameters $\theta$; Chouchoulis et al.
  (2022) $\mathcal R$ for the region, without printing the test equation.
* Buvoli & Southworth (2025) define the coupled stiff limit with a modulus (Eq. (4.25))
  but treat it as a polynomial without one in Remark 2 and the supplement, and print the
  limit of the Euler step as $\epsilon$, while $(1+\kappa z_1)/(1-z_1)\to-\kappa$; only the modulus
  matters for the condition.
* Caliari et al. (2024) call their stability regions "A-stability regions" (Fig. 1)
  and use "unconditionally stable" for stability on the negative real axis only, which
  is weaker than [A-stability](/properties/a-stability.md).
* [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) (§2) define the stability
  domain with the strict inequality $\lvert r(z)\rvert<1$ and L-stability by the limit
  along the negative real axis; most sources use $\le1$. The difference matters only on
  the boundary.
* Popov (2024, Eq. (15)) prints $R(z)=1+w^\top(I-zB)^{-1}\mathbf 1$ without the factor
  $z$; the determinant form he gives beside it is the correct one.
* Jin et al. (2025, Remark 3.4) note that the textbook form of a degree-$(2,2)$ rational
  $R$ loses accuracy to round-off through the squared operator in the numerator and
  rewrite it as a constant plus a proper fraction; no numbers are shown.
* Kemm (2024) reads stability from plotted regions only; his thesis that the first
  explicit-Euler stage spoils explicit Runge–Kutta methods on nonlinear problems is about
  stage values, not about $R$; see [internal stability](/definitions/internal-stability.md).
* Belardo et al. (2026, §4) state that the maximal real stability interval of the
  first-order embedding of the explicit midpoint rule is "7", reached at their
  parameter value 1; with $\hat b=(1/\sqrt2,1-1/\sqrt2)$ the embedding has
  $R(z)=1+z+\alpha z^2$, $\alpha=\tfrac12(1-1/\sqrt2)$, so $\ell=1/\alpha\approx6.83$
  there and the supremum $\ell=8$ is reached at $\alpha=1/8$, a slightly larger parameter;
  the printed values are plot readings *(compiler check, not in the source)*.
* Fekete et al. (2022, Def. 1) print the real-axis inclusion with a symmetric
  segment $[-\beta,\beta]$; for an explicit method this gives zero, and the
  intended segment is $[-\beta,0]$.
* Han Veiga et al. (2021, §5.1) print the region as $\{z:\phi(z)<1\}$
  without modulus and call their computation of the bounded regions of
  explicit methods an "A-stability" study; the explicit ADER and DeC schemes
  are not A-stable.
* Hedayati Nasab et al. (2021, §5) remove eigenvalues with positive real part
  at machine-precision level before optimizing, an ad hoc choice; they also do
  not analyse internal stability of their 16-stage methods.

# Citations

- [Biswas et al. (2023)](/sources/biswas-2023.md) — Eq. (9).
- [Biswas et al. (2024)](/sources/biswas-2024.md) — Eq. (5), Thms. 3.7–3.9, Lemma 5.2.
- [Biswas et al. (2025)](/sources/biswas-2025.md) — §1, Lemma 2.1, Thm. 2.6, §7.
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — Eqs. (1)–(5), §5, §6.
- [Sun et al. (2022)](/sources/sun-2022.md) — §1, §3, Eq. (5.1), Ex. 4.5.
- [Fekete et al. (2022)](/sources/fekete-2022.md) — Defs. 1–4.
- [Steinebach (2023)](/sources/steinebach-2023.md) — Eq. (2.14), Figs. 1–2.
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.1, Fig. 2.
- [Roberts et al. (2021)](/sources/roberts-2021.md) — §3.4 (internal stability function).
- [Belardo et al. (2026)](/sources/belardo-2026.md) — §3–4, Tables 2–3 (determinant form; real stability interval of embedded formulas).
- [Bassenne et al. (2021)](/sources/bassenne-2021.md) — Table 1 (real-axis intercepts), §3.2 (Eqs. 24–27, Fig. 4; rational stability function of TASE).
- [Croci & Rosilho de Souza (2022)](/sources/croci-2022.md) — §2.2 (Eqs. 11–12), Lemma 3.1.
- [Dawes (2021)](/sources/dawes-2021.md) — §3 (Eq. 7), §5–7.
- [Faleichik & Moisa (2026)](/sources/faleichik-2026.md) — §1, §3 (monotonicity interval, error constant).
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §2.2 (Eqs. 2.10–2.11).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §2.2 (Eq. 2.12), §5.1.
- [Vermeire (2023)](/sources/vermeire-2023.md) — Eqs. (9)–(10) (main and embedded polynomials).
- [Conte et al. (2024)](/sources/conte-2024.md) — §3, Eq. (3.4), Lemma 3.4, Thm. 3.6 (two-parameter stability function, stability diagrams).
- [Song & Eisenträger (2022)](/sources/song-2022.md) — §2.2, §3.2.1, App. B Eqs. (B.2)–(B.4) (diagonal Padé as integrator, factored denominator).
- [Kemm (2024)](/sources/kemm-2024.md) — §3.3, §4, Figs. 1–2 (regions of minimal-stage RK and Adams–Bashforth for nearly central spectra).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §2 (strict-inequality stability domain).
- [Caliari et al. (2024)](/sources/caliari-2024.md) — §2 (Eq. (1), Thms. 2.1–2.7, Remarks 2.1–2.2, Table 1, Fig. 1).
- [Buvoli & Southworth (2025)](/sources/buvoli-2025.md) — §4.5 (Eqs. (4.16)–(4.27)), §4.5.2, Eq. (5.2), SM2, SM3.
- [Buvoli et al. (2026)](/sources/buvoli-2026.md) — §2.3 (Eqs. (2.5)–(2.10)), Thm. 3.2.
- [Micalizzi & Torlo (2024)](/sources/micalizzi-2024.md) — Eqs. (40)–(42), Thms. 6.1–6.2, Fig. 3 (stability function of DeC variants).
- [Popov (2024)](/sources/popov-2024.md) — §1.2 (Eqs. (14)–(15), Figs. 1–2).
- [Chouchoulis et al. (2022)](/sources/chouchoulis-2022.md) — §5, Fig. 1, App. A (stability functions of explicit multiderivative methods; MOL remark).
- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — §2.2 (Eqs. (2.12)–(2.13)), §3.2 (Fig. 5).
- [Buvoli & Minion (2024)](/sources/buvoli-2024.md) — §5 (Eqs. (30)–(40)).
- [Jin et al. (2025)](/sources/jin-2025.md) — §3.1–3.2 (Eqs. (3.1)–(3.7), Prop. 3.3, Remark 3.4), Table 4.1.
- [Izgin et al. (2022)](/sources/izgin-2022.md) — Thm. 2.9, Lemma 3.6, Remark 3.7, §3.1 (Eqs. (43a)–(43b), (47)–(48)); arXiv v1.
- [Ern & Guermond (2022)](/sources/ern-2022.md) — §4.1 (Eq. (40), Fig. 1); HAL v2.
- [Ern & Guermond (2023)](/sources/ern-2023.md) — §4.1 (Eqs. (72)–(75)), §4.3 (Eq. (81)); HAL v1.
- [Vermeire & Hedayati Nasab (2021)](/sources/vermeire-2021.md) — §3.1 (Eqs. (32)–(34)), App. 1, Table 1, Fig. 1.
- [Maurya et al. (2021)](/sources/maurya-2021.md) — §2.1 (Eq. (8)), Table 1.
