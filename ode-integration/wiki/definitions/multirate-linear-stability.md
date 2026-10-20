---
type: Definition
title: "Linear stability of multirate methods and joint stability regions"
description: "Defines the scalar and 2D (Gear) test problems for multirate and GARK methods, scalar, real-2D and complex-2D A-, L-, A(α)- and L(α)-stability and their hierarchy, the joint stability regions of IMEX multirate methods, the partitioned Dahlquist test of nonlinearly partitioned methods, and the real scalar test of averaged-force mRKC methods."
status: established
aliases: [scalar A-stability, 2D A-stability, Gear test problem, joint stability region, multirate stability function, partitioned Dahlquist equation, L-stability in the stiff limit]
tags: [multirate, stability, imex, stiff]
timestamp: 2026-10-20T16:00:00Z
---

# Linear stability of multirate methods and joint stability regions

For a single-rate Runge–Kutta method the Dahlquist equation $y'=\lambda y$ and
its [stability function](/definitions/stability-function.md) $R(z)$ decide linear
stability, because the method commutes with diagonalization. A multirate or
[GARK](/methods/generalized-additive-runge-kutta.md) method treats the partitions
of $f=f^{\{\mathrm f\}}+f^{\{\mathrm s\}}$ differently, so its linear stability
depends on the basis, and one scalar test is not enough (Roberts et al. 2021, §3,
after Gear). The sources therefore use a **scalar** test problem with one
eigenvalue per partition, which models partitions whose Jacobians triangularize
simultaneously, and a **2D** test problem with coupling. Every argument $z$ is
scaled by the **macro step** $H$, so the fast base method sees $z^{\{\mathrm f\}}/m$.

## Scalar test problem

$$y'=\lambda^{\{\mathrm f\}}y+\lambda^{\{\mathrm s\}}y,\qquad \lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\in\mathbb C^-=\{\operatorname{Re}z\le0\},\qquad z^{\{\mathrm f\}}=H\lambda^{\{\mathrm f\}},\ z^{\{\mathrm s\}}=H\lambda^{\{\mathrm s\}}.$$

The step multiplies $y_n$ by the two-variable function
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\{\mathrm s\}})$ (page-local symbol; formula on
[GARK](/methods/generalized-additive-runge-kutta.md)), which for a multirate method
also depends on $m$. [Roberts et al. (2021)](/sources/roberts-2021.md) define
(Defs. 3.1–3.2), with
$\mathcal S_{\mathrm{mr}}=\{(z^{\{\mathrm f\}},z^{\{\mathrm s\}})\in\mathbb C^2:\lvert R_{\mathrm{mr}}\rvert\le1\}$
and the wedge $W(\alpha)=\{z\ne0:\lvert\arg(-z)\rvert<\alpha\}$:

- **scalar A-stable** if $\mathcal S_{\mathrm{mr}}\supseteq\mathbb C^-\times\mathbb C^-$;
- **scalar L-stable** if scalar A-stable and $R_{\mathrm{mr}}\to0$ as
  $z^{\{\mathrm f\}}\to\infty$ **and** as $z^{\{\mathrm s\}}\to\infty$, each variable
  separately (eq. 3.5);
- **scalar A($\alpha$)-stable** if $\mathcal S_{\mathrm{mr}}\supseteq W(\alpha)\times W(\alpha)$,
  and **scalar L($\alpha$)-stable** if in addition (3.5) holds.

These reduce to the single-rate notions of
[A-, L- and A($\alpha$)-stability](/properties/a-stability.md) when one partition
is empty.

**Theorem (imaginary-axes criterion; Roberts et al. 2021, Thm. 3.1).** A GARK
method is scalar A-stable if and only if
$\lvert R_{\mathrm{mr}}(i\rho^{\{\mathrm f\}},i\rho^{\{\mathrm s\}})\rvert\le1$ for all real
$\rho^{\{\mathrm f\}},\rho^{\{\mathrm s\}}$ (page-local) and $R_{\mathrm{mr}}$ is analytic on
$\mathbb C^-\times\mathbb C^-$. The proof uses the multivariate maximum principle;
the check drops from four real dimensions to two. The A($\alpha$) angle is found
by checking only $\partial W(\alpha)\times\partial W(\alpha)$ (Remark 3.1).

**Theorem (E-polynomial; Roberts et al. 2021, Thm. 3.2).** Write
$R_{\mathrm{mr}}=P_{\mathrm{mr}}/Q_{\mathrm{mr}}$ and

$$E\big(\rho^{\{\mathrm f\}},\rho^{\{\mathrm s\}}\big)=Q_{\mathrm{mr}}(i\rho^{\{\mathrm f\}},i\rho^{\{\mathrm s\}})\,Q_{\mathrm{mr}}(-i\rho^{\{\mathrm f\}},-i\rho^{\{\mathrm s\}})-P_{\mathrm{mr}}(i\rho^{\{\mathrm f\}},i\rho^{\{\mathrm s\}})\,P_{\mathrm{mr}}(-i\rho^{\{\mathrm f\}},-i\rho^{\{\mathrm s\}}).$$

The scalar stability region contains the imaginary axes if and only if
$E\ge0$ on $\mathbb R^2$; this generalizes the single-rate E-polynomial of
Hairer–Wanner as recalled by Roberts et al.

## 2D (Gear) test problem

$$\begin{bmatrix}y^{\{\mathrm f\}}\\ y^{\{\mathrm s\}}\end{bmatrix}'=\begin{bmatrix}\lambda^{\{\mathrm f\}}&\eta^{\{\mathrm s\}}\\ \eta^{\{\mathrm f\}}&\lambda^{\{\mathrm s\}}\end{bmatrix}\begin{bmatrix}y^{\{\mathrm f\}}\\ y^{\{\mathrm s\}}\end{bmatrix}$$

(Roberts et al. 2021, eq. 3.7; $\eta^{\{\cdot\}}$ the coupling entries,
page-local). The admissible set $\mathbb M$ (page-local) holds the matrices with
bounded exact solutions (eigenvalues with non-positive real part, regular on the
imaginary axis) and $\lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\in\mathbb C^-$. The
**real** variant takes real $\lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\le0$ with
$\eta^{\{\mathrm f\}}\eta^{\{\mathrm s\}}\le\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}$.
One step multiplies the state by a $2\times2$ stability matrix $\mathbf R_2(Z)$,
$Z=H\cdot(\text{test matrix})$, built from the four GARK blocks (eq. 3.8).

- **Complex 2D A-stable** (Def. 3.3): $\mathbf R_2(Z)$ is **power bounded** for every
  $Z\in\mathbb M$ (a spectral radius at most one is not enough).
- **Real 2D A-stable** (Def. 3.4): the same for real $Z\in\mathbb M\cap\mathbb R^{2\times2}$.

On the skew test matrix $\begin{bmatrix}0&\eta\\-\eta&0\end{bmatrix}$ the matrix
$\mathbf R_2$ depends only on the coupling blocks $A^{\{\mathrm f,\mathrm s\}}$,
$A^{\{\mathrm s,\mathrm f\}}$ and the weights, not on the base methods (eq. 3.10).
This is the lever of the decoupled-method barrier on
[multirate A-stability barriers](/results/multirate-a-stability-barriers.md).

The two tests are linked by the identity
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\{\mathrm s\}})=[1\ 1]\,\mathbf R_2\!\begin{pmatrix}z^{\{\mathrm f\}}&z^{\{\mathrm f\}}\\ z^{\{\mathrm s\}}&z^{\{\mathrm s\}}\end{pmatrix}\begin{bmatrix}\alpha\\1-\alpha\end{bmatrix}$
for any $\alpha\in\mathbb C$ (eq. 3.13; $\alpha$ page-local), so $R_{\mathrm{mr}}$ is an
eigenvalue of that $\mathbf R_2$.

## Hierarchy

Roberts et al. (2021, Thm. 3.3, Fig. 3.1) prove or state:

- complex 2D A-stable ⇒ scalar A-stable (Thm. 3.3) and ⇒ real 2D A-stable;
- algebraically stable ⇒ scalar A-stable;
- scalar L ⇒ scalar A ⇒ scalar A($\alpha$); scalar L ⇒ scalar L($\alpha$) ⇒ scalar A($\alpha$).

"In general, no implication arrows are reversible." Two counterexamples show that
the scalar and the real 2D notions are independent:

- the GARK tableau with rows $(1\,|\,0)$, $(1\,|\,1)$ and weights $(1\,|\,1)$ is
  scalar L-stable and algebraically stable, but on the matrix
  $\begin{bmatrix}-1&1\\-10&-1\end{bmatrix}$ its $\mathbf R_2$ has spectral radius
  $(\sqrt5+3)/4>1$, so it is only conditionally stable in 2D (§3.3);
- a GARK method whose base is only A(45°)-stable has
  $\lvert R_{\mathrm{mr}}(-4+8i,0)\rvert=\sqrt{17}/4>1$ yet is stated to be real-2D
  A-stable (eq. 3.12): the real 2D test cannot see base-method instabilities off
  the real axis, which is why the complex variant is needed.

## Joint stability region (IMEX multirate)

For a three-way split $y'=f^{\mathrm I}+f^{\mathrm E}+f^{\{\mathrm f\}}$ (slow stiff,
slow nonstiff, fast) [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md)
(§3, eq. 3.3) use $y'=(\lambda^{\{\mathrm f\}}+\lambda^{\mathrm E}+\lambda^{\mathrm I})y$
with all $z=H\lambda$, solve the fast problem exactly by variation of constants,
and obtain a three-variable stability function
$R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})$ built from
$\phi$-functions of $\Delta c_iz^{\{\mathrm f\}}$ (formula on
[IMEX-MRI-GARK](/methods/imex-mri-gark.md)). Extending Zharovsky et al., as
recalled there, they define the **joint stability region**

$$\mathcal J_{\alpha,\beta}=\Big\{z^{\mathrm E}\in\mathbb C^-:\ \lvert R_{\mathrm{mr}}(z^{\{\mathrm f\}},z^{\mathrm E},z^{\mathrm I})\rvert\le1\ \ \forall z^{\{\mathrm f\}}\in S_\alpha,\ \forall z^{\mathrm I}\in S_\beta\Big\},\qquad S_\alpha=\{z\in\mathbb C^-:\lvert\arg z-\pi\rvert\le\alpha\}.$$

It is the region of admissible explicit arguments that stays valid for every fast
eigenvalue in a sector of half-angle $\alpha$ and every slow stiff eigenvalue in a
sector of half-angle $\beta$ ($\alpha$, $\beta$ page-local). The authors call it
"artificially restrictive", because the stiff partitions will not in practice be
infinitely stiffer than $f^{\mathrm E}$. They use it to optimize IMEX-MRI-GARK3b
and to reject IMEX-MRI-GARK4, whose joint region is empty.

**Truncated and reduced regions.** [Fish et al. (2024)](/sources/fish-2024.md) (§3, eqs.
3.5–3.7) apply the same construction to the stage-restart
[IMEX-MRI-SR](/methods/imex-mri-sr.md) methods, with sectors truncated at radii $\rho$ (fast)
and $\xi$ (implicit), $\mathcal J_{\alpha,\rho,\beta,\xi}$ (page-local $\rho$, $\xi$), and add two
reduced regions: the **implicit-only** region of $z^{\mathrm I}$ with $z^{\mathrm E}=0$ for all
fast $z^{\{\mathrm f\}}$ in $S_{\alpha,\rho}$, and the **explicit-only** region of $z^{\mathrm E}$ with
$z^{\mathrm I}=0$. Like Chinomona & Reynolds, who call it "artificially restrictive", they find that the full region
"may be overly-restrictive", for a different stated reason: it demands stability of the implicit
part over a sector and of the fast part over another sector at once (§3). They go further: the explicit-only regions of the
MERK4 and MERK5 methods are empty, which they take as "a deficiency in these definitions of
joint stability" rather than in those methods, which converge at design order (§5.3–5.4). For
IMEX-MRI-SR4(3) the full region was empty for every choice of the free parameters, so they
optimized the explicit-only region instead (§4.3).

## Partitioned Dahlquist test (nonlinear partitions)

For a nonlinearly partitioned problem $y'=F(y,y)$
([NPRK](/methods/nonlinearly-partitioned-runge-kutta.md)) the test is
$F(u,v)=\lambda_1u+\lambda_2v$ with $z_r=h\lambda_r$; the method then reduces to its underlying
ARK method, whose two-variable stability function $R(z_1,z_2)$ is the ratio of
$\det(I-z_1A^{\{1\}}-z_2A^{\{2\}}+\mathbf 1(z_1b^{\{1\}}+z_2b^{\{2\}})^\top)$ and
$\det(I-z_1A^{\{1\}}-z_2A^{\{2\}})$ ([Buvoli et al. 2026](/sources/buvoli-2026.md), §2.3, eqs.
2.5–2.7). Unlike the scalar multirate test above, both arguments are scaled by the same step $h$,
and the number of stages per argument, not a ratio $m$, carries the multirate structure.
Conjugate symmetry of real spectra makes the region
$\{\max(|R(z_1,z_2)|,|R(\bar z_1,z_2)|)\le1\}$ the relevant one, plotted in slices for fixed $z_1$.

- No IMEX method of this kind is A-stable, because $R(0,z_2)$ is an explicit stability
  polynomial (§3.1); the scalar notions above are therefore replaced by limits.
- **L-stable in the stiff $z_1$ limit** (Def. 3.1): $\lim_{|z_1|\to\infty}R(z_1,z_2)=0$ for every
  $z_2$. Buvoli et al. prove sufficient conditions for multirate NPRK methods (Thm. 3.2:
  decoupled or $1\to2$ coupling, stiff accuracy, DIRK reduced implicit method). They also show
  that its practical value shrinks as the explicit stage count $s^{\{2\}}$ grows: damping
  happens only for $|z_1|\gg|z_2|^{s^{\{2\}}/s^{\{1\}}}$, while the step must stay in an explicit
  region that grows only linearly in $s^{\{2\}}$ (§3.1.1, Fig. 2).
- Buvoli & Southworth's single-rate notions (IMEX A-/L-stability in a stiff limit, stability in
  the coupled stiff $z_2$ limit) are stated on the NPRK page. These are not the scalar
  L-stability of Roberts et al., which requires the limit in each variable together with
  A-stability, and not a joint region.

## Real scalar test of averaged-force methods (mRKC)

[Abdulle, Grote & Rosilho de Souza (2022)](/sources/abdulle-2022.md) (§2.3, §4) analyse the
[multirate Runge–Kutta–Chebyshev method](/methods/multirate-runge-kutta-chebyshev.md) on
the scalar test problem above restricted to **real** eigenvalues,
$\lambda^{\{\mathrm f\}},\lambda^{\{\mathrm s\}}\le0$ (Eq. (2.10)), because its stabilized
Chebyshev polynomials target the negative real axis. Both arguments are scaled by the one
step $h$; the fast part is reached through an inner run of length $\eta$ (page-local, not
the registry entropy and distinct from the Gear coupling entries $\eta^{\{\cdot\}}$), so the
stability function depends on $(h\lambda^{\{\mathrm s\}},\eta\lambda^{\{\mathrm f\}},\eta/h)$
rather than on a step ratio $m$:

$$R_{s,m}=P_s\bigl(h\,\Phi_m(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})\bigr),\qquad \Phi_m(z)=\frac{P_m(z)-1}z$$

(Def. 4.2; $P_s$, $P_m$ the outer and inner RKC polynomials, $\Phi_m$ page-local). The
stability theorem (Thm. 4.5) is the condition $\lvert R_{s,m}\rvert\le1$ for **all**
$\lambda^{\{\mathrm f\}}$ in the inner stability interval once $\eta$ is large enough
relative to $h$; it is the discrete analogue of the exact statement that
$\phi_1(\eta\lambda^{\{\mathrm f\}})(\lambda^{\{\mathrm f\}}+\lambda^{\{\mathrm s\}})\in[\lambda^{\{\mathrm s\}},0]$
for every $\lambda^{\{\mathrm f\}}\le0$ iff $\eta\ge2/\lvert\lambda^{\{\mathrm s\}}\rvert$ (Thm. 2.7).
For coupling they use a real symmetric instance of the 2D test,
$\begin{bmatrix}\lambda^{\{\mathrm s\}}&\sigma\\ \sigma&\lambda^{\{\mathrm f\}}\end{bmatrix}$ with
$\sigma^2\le\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}$ ($\sigma$ page-local; the real 2D
admissibility condition above with both coupling entries equal to $\sigma$), split by a 0/1
selector of the fast row so that the two parts are not simultaneously triangularizable
unless $\sigma=0$ or $\sigma^2=\lambda^{\{\mathrm f\}}\lambda^{\{\mathrm s\}}$ (Eqs. (4.6)–(4.8)).
Spectral-radius plots, not a power-boundedness proof, show that the scalar condition stays
necessary under weak coupling (§4.1, Fig. 9). The test is single-step and real; no complex
or A-stability notion of the kind defined above is claimed for mRKC.

## Qualifications

- The scalar test assumes simultaneously diagonalizable partitions and the 2D test a
  $2\times2$ model coupling; Roberts et al. mention a block generalization (eq. 3.11) and Skelboe's
  more general one without pursuing them.
- Roberts et al. use the macro step for both scaled eigenvalues; Chinomona &
  Reynolds do the same for all three. Single-rate pages scale by the step $h$.
- The sector notation differs: Roberts et al. use the open wedge
  $\lvert\arg(-z)\rvert<\alpha$, Chinomona & Reynolds the closed sector
  $\lvert\arg z-\pi\rvert\le\alpha$. Chinomona & Reynolds' prose (p. 16 of the
  version read) swaps $\alpha$ and $\beta$ relative to their own definition and to
  their §4.1 usage ($\alpha$ fast, $\beta$ implicit); the definition is the one
  given here.
- Chinomona & Reynolds print the $\phi$-functions without the $1/(k-1)!$ factor;
  their $\varphi_{k+1}$ equals $k!\,\phi_{k+1}$ in the registry convention; Fish et al. (2024)
  use the same unnormalized convention.
- Fish et al. (2024) print several figure captions with $\alpha$ in the $\beta$ slot and a radius
  1 where the subcaptions show $10^2$ (§4.1, §4.3); the definitions above are those of eqs.
  3.5–3.7.
- Buvoli et al. (2026, §2.3.3) write that real spectra are symmetric "about the imaginary axis";
  the region they use, with $\bar z_1$, encodes symmetry about the real axis.
- Abdulle et al. (2022) call the real scalar equation the "multirate test equation" and write
  $\lambda$, $\zeta$ for the fast and slow eigenvalues; their stability statements are for
  real nonpositive spectra only.
- The partitioned Dahlquist test assumes simultaneously diagonalizable partial Jacobians (Buvoli
  et al. 2026, §2.3.1), the same caveat as the scalar multirate test.

# Citations

- [Roberts et al. (2021)](/sources/roberts-2021.md) — §3 (eqs. 3.3–3.13, Defs. 3.1–3.4, Thms. 3.1–3.3, Remarks 3.1–3.2, Fig. 3.1).
- [Chinomona & Reynolds (2021)](/sources/chinomona-2021.md) — §3 (eqs. 3.1–3.3, joint stability region), §4.1, Fig. 1.
- [Fish et al. (2024)](/sources/fish-2024.md) — §3 (eqs. 3.4–3.7), §4.3, §5.3–5.4.
- [Abdulle, Grote & Rosilho de Souza (2022)](/sources/abdulle-2022.md) — §2.3 (Eqs. 2.10–2.12, Lemma 2.6, Thm. 2.7), §4 (Lemma 4.1, Def. 4.2, Thm. 4.5), §4.1 (Eqs. 4.6–4.8, Fig. 9).
- [Buvoli et al. (2026)](/sources/buvoli-2026.md) — §2.3 (eqs. 2.5–2.10), §3.1 (Def. 3.1, Thm. 3.2, Fig. 2), App. A.
