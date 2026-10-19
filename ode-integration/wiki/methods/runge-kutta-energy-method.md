---
type: Method
title: "Energy method for Runge–Kutta stability"
description: "The energy method writes $\\lVert y_{n+1}\\rVert^2-\\lVert y_n\\rVert^2$ for a Runge–Kutta method on a linear seminegative problem as a diagonal sum plus a quadratic form in a dissipation semi-inner product, by discrete integration by parts, and reads strong, weak or unconditional stability from the signs; it works for non-normal operators, and a multiplier-matrix version gives stiffness-independent stability of IMEX pairs."
status: established
aliases: [energy analysis of Runge–Kutta methods, discrete energy law, discrete energy identity, discrete integration by parts]
tags: [stability, runge-kutta, structure-preserving, implicit, explicit, imex]
timestamp: 2026-10-19T23:00:00Z
---

# Energy method for Runge–Kutta stability

The energy method analyses a time discretization of $y'=Ly$, $L$ bounded and
seminegative ($\langle Lv,v\rangle\le0$) on a real Hilbert space, by deriving an exact
identity for the one-step change of $\lVert y\rVert^2$ instead of bounding
$\lVert R(hL)\rVert$ through the spectrum. The identity mimics the continuous law
$\frac{d}{dt}\lVert y\rVert^2=-\lvert y\rvert_L^2$, with the semi-inner product
$[v,w]_L=-\langle Lv,w\rangle-\langle v,Lw\rangle$ and semi-norm $\lvert
v\rvert_L=\sqrt{[v,v]_L}$ (page-local, as on
[strong stability](/properties/strong-stability.md)). It was developed for explicit
methods by Sun & Shu (recalled in [Sun & Shu 2021](/sources/sun-2021.md), §2) and
extended to every rational stability function by
[Sun, Wei & Wu (2022)](/sources/sun-2022.md). Its purpose is to decide
[strong stability](/properties/strong-stability.md) for **non-normal** $L$, where
eigenvalue analysis is only a necessary condition.

## Setting

Only the [stability function](/definitions/stability-function.md) enters. Write it
as $R(z)=D(z)^{-1}N(z)$ with $N(z)=\sum_{i=0}^m\theta_iz^i$,
$D(z)=\sum_{i=0}^m\vartheta_iz^i$, $\theta_0=\vartheta_0=1$, $m$ the larger degree
(page-local symbols; $D\equiv1$ and $N=P$ for explicit methods). With
$w_n:=D(hL)^{-1}y_n$ (so $y_{n+1}=N(hL)w_n$, $y_n=D(hL)w_n$),

$$\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=\sum_{i,j=0}^m\omega_{ij}h^{i+j}\langle L^iw_n,L^jw_n\rangle,\qquad \omega_{ij}:=\theta_i\theta_j-\vartheta_i\vartheta_j$$

(Sun et al. 2022, §3, Lemma 3.2, Eq. (3.4)). The analysis applies to any one-step
linear method with rational $R$, Padé approximations included, without a Butcher
tableau (Sun et al. 2022, §3).

## Discrete integration by parts

The identity $\langle w,Lv\rangle=-\langle Lw,v\rangle-[w,v]_L$, the discrete analogue
of moving a derivative across an inner product, gives the reduction rules

$$\langle L^iw,L^jw\rangle=\begin{cases}\lVert L^iw\rVert^2, & j=i,\\ -\tfrac12\lvert L^iw\rvert_L^2, & j=i+1,\\ -\langle L^{i+1}w,L^{j-1}w\rangle-[L^iw,L^{j-1}w]_L, & \text{otherwise}\end{cases}$$

(Sun et al. 2022, Eqs. (3.6)–(3.7), from Sun & Shu's Prop. 2.1). Applied repeatedly
to the double sum, it yields

$$\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=\sum_{k=0}^m\eta_kh^{2k}\lVert L^kw_n\rVert^2+\sum_{i,j=0}^{m-1}\upsilon_{ij}h^{i+j+1}[L^iw_n,L^jw_n]_L,$$

$$\eta_k=\sum_{r=\max\{0,2k-m\}}^{\min\{2k,m\}}(-1)^{k-r}\omega_{r,2k-r},\qquad \upsilon_{ij}=\sum_{r=\max\{0,i+j+1-m\}}^{\min\{i,j\}}(-1)^{\min\{i,j\}+1-r}\omega_{r,i+j+1-r}$$

(Sun et al. 2022, Lemma 3.3, Eqs. (3.9)–(3.10)), with $\Upsilon=(\upsilon_{ij})$
symmetric. The closed forms come from the conversion algorithm of Sun & Shu; their
combinatorial proof is "omitted here" and deferred to a work in preparation. For
explicit methods Sun & Shu (2021, Eq. (2.6)) write the same expansion with the step
absorbed into $Z=hL$, i.e. with $[\cdot,\cdot]_{hL}=h[\cdot,\cdot]_L$; the conversion
was done by a computer program.

## From quadratic form to energy law

If $\Upsilon$ is negative semidefinite with a Cholesky-type factorization
$\Upsilon=-U^\top\mathrm{diag}(d_k)U$, $U=(u_{kj})$ upper triangular and
$d_k\ge0$, then

$$\sum_{i,j}\upsilon_{ij}h^{i+j+1}[L^iv,L^jv]_L=-\sum_kd_kh^{2k+1}\lvert L^kv^{(k)}\rvert_L^2\le0,\qquad v^{(k)}=\sum_{j\ge k}u_{kj}(hL)^{j-k}v$$

(Sun et al. 2022, Lemma 2.2). When $\Upsilon$ is not negative semidefinite, a
nonnegative diagonal shift $\Delta=\mathrm{diag}(\delta_k)$ making $\Upsilon-\Delta$
negative semidefinite gives the **discrete energy law**

$$\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=\sum_k\eta_kh^{2k}\lVert L^kw_n\rVert^2-\sum_k\tilde d_kh^{2k+1}\lvert L^ky^{(k)}\rvert_L^2+\sum_k\delta_kh^{2k+1}\lvert L^kw_n\rvert_L^2$$

with $y^{(k)}$ built from the factors of $\Upsilon-\Delta$ (Sun et al. 2022, Thm. 3.4).
Each term has a sign or a size in powers of $h\lVert L\rVert$, which is what the
stability criteria read off; using $\lvert v\rvert_L^2\le2\lVert L\rVert\lVert
v\rVert^2$ and Cauchy–Schwarz bounds the shift terms (Lemma 3.6). The criteria
(unconditional if $\mathrm{diag}(\eta_k)\le0$ and $\Upsilon\le0$; conditional strong
stability if the first nonzero $\eta_\zeta<0$ and $\zeta\le\rho$; failure if
$\eta_\zeta>0$; weak($\kappa$) stability with $\kappa=\min\{2\zeta,2\rho+1\}$) are on
[strong stability](/properties/strong-stability.md) (Sun et al. 2022, Thms. 3.5, 3.7).
For explicit methods Sun & Shu (2021, Prop. 2.1) state the small-step version: if the
leading block of $\Upsilon$ minus a diagonal shift is negative definite, the sign of
the change is that of $\eta_\zeta$ up to $O(h\lVert L\rVert)$.

## The continuous law, expanded

The exact flow obeys an expansion of the same shape:

$$\lVert y(t_n+h)\rVert^2-\lVert y(t_n)\rVert^2=-\sum_{k=0}^\infty d_kh^{2k+1}\lvert L^k\hat y^{(k)}\rvert_L^2,\qquad d_k=\frac{(k!)^2}{(2k)!\,(2k+1)!},$$

$$\hat y^{(k)}=\sum_{j\ge k}\hat u_{kj}(hL)^{j-k}y(t_n),\qquad \hat u_{kj}=\frac{(2k+1)!\,j!}{k!\,(j-k)!\,(k+j+1)!}$$

(Sun et al. 2022, Thm. 2.1, Eqs. (2.1)–(2.3)). It follows from the Cholesky
factorization of the scaled Hilbert matrix $-\bigl(1/(i!j!(i+j+1))\bigr)_{ij}$
(Lemma 2.3). A discrete law is *energy-accurate* to the extent that it truncates this
series; the diagonal Padé approximations do so exactly
([diagonal Padé strong stability](/results/diagonal-pade-strong-stability.md)).

## Worked identities

Sun et al. (2022, §4) give the laws explicitly:

- backward Euler: $\lVert y_{n+1}\rVert^2-\lVert y_n\rVert^2=-h^2\lVert Ly_{n+1}\rVert^2-h\lvert y_{n+1}\rvert_L^2$ (Ex. 4.1);
- Crank–Nicolson and implicit midpoint: $-h\lvert w_n\rvert_L^2$, $w_n=(I-\frac h2L)^{-1}y_n$ (Ex. 4.2);
- Qin–Zhang two-stage symplectic DIRK ($c=(\frac14,\frac34)$, $A$ with rows $(\frac14)$, $(\frac12,\frac14)$, $b=(\frac12,\frac12)$; $R=(1-\frac z2+\frac{z^2}{16})^{-1}(1+\frac z2+\frac{z^2}{16})$, not the (2,2) Padé): $-h\lvert w_n\rvert_L^2-\frac1{16}h^3\lvert Lw_n\rvert_L^2$ (Ex. 4.3);
- Kraaijevanger–Spijker two-stage DIRK ($c=(\frac12,\frac32)$, rows $(\frac12)$, $(-\frac12,2)$, $b=(-\frac12,\frac32)$): $-3h^2\lVert Lw_n\rVert^2-\frac34h^4\lVert L^2w_n\rVert^2-h\lvert(I-\frac h2L)w_n\rvert_L^2-\frac32h^3\lvert Lw_n\rvert_L^2$ (Ex. 4.4);
- (0,3) Padé: $\eta_2=\frac1{12}>0$ appears as $+\frac{h^4}{12}\lVert L^2w_n\rVert^2$, so the method is weakly(4) stable and not strongly stable (Ex. 4.5);
- (4,1) Padé: leading term $-\frac{h^6}{1800}\lVert L^3w_n\rVert^2$ plus a positive $\frac{h^8}{14400}\lVert L^4w_n\rVert^2$, so strongly stable for small $h\lVert L\rVert$ (Ex. 4.6).

For skew $L$ ($[\cdot,\cdot]_L=0$) the semi-norm terms vanish: Crank–Nicolson and the
Qin–Zhang DIRK then conserve the norm exactly, while backward Euler and the
Kraaijevanger–Spijker DIRK keep negative $\lVert L^kw_n\rVert^2$ terms and damp
*(compiler check, not in the sources)*. Irksome's energy test on a mixed wave equation, whose
semi-discretization conserves energy, shows exactly this: Gauss–Legendre and the
Qin–Zhang DIRK give $E(10)/E(0)=1$, while Radau IIA and Lobatto IIIC damp
([Farrell et al. 2021](/sources/farrell-2021.md), §4.3, Table 1).

## Uses

- deciding strong stability of explicit methods, including the mod-4 pattern for
  Taylor-type stability polynomials (Sun & Shu 2021, §2, Prop. 2.2);
- designing [superviscosity](/methods/superviscosity-stabilized-runge-kutta.md)
  corrections whose critical coefficients are read off $\eta_\zeta$ and the leading
  block of $\Upsilon$ (Sun & Shu 2021, Thms. 3.1–3.2);
- proving unconditional strong stability *with* an energy law for implicit methods,
  culminating in the [diagonal Padé](/results/diagonal-pade-strong-stability.md)
  result (Sun et al. 2022, §5);
- step-size conditions for hyperbolic semi-discretizations: strong stability under
  $h\le C\Delta x$, weak($\kappa$) under $h\le C\Delta x^{1+1/(\kappa-1)}$ (Sun et al.
  2022, Remark 3.8).

## Multiplier matrices for IMEX stages

[Hu & Shu (2025)](/sources/hu-2025.md) (§3) carry the energy method to an
[IMEX Runge–Kutta](/methods/imex-runge-kutta.md) pair applied to a linear hyperbolic
relaxation system, where the relaxation term $-\frac1\varepsilon w$ is implicit and the
convection explicit, and where the constants must not depend on $\varepsilon$. The stage
equations for the relaxing variable are multiplied by $W^\top\Pi$, with $W$ the vector of
stage values and $\Pi$ an $s\times s$ **multiplier matrix** with zero first column
(page-local symbols). This turns the step into the identity

$$\lVert W_s\rVert^2=\lVert W_0\rVert^2-W^\top\Pi_*W-\frac h\varepsilon W^\top\Pi A^{\mathrm I}W-h\,W^\top\Pi A^{\mathrm E}(\text{convection terms}),$$

($W_0$ the step's initial value, $\Pi_*$ a fixed shift of $\Pi$, Eq. (3.3); notation
condensed from Eq. (3.2)). Two algebraic conditions make the stiff and the stage-difference
terms good:

- **(M1)** $\Pi A^{\mathrm I}+(\Pi A^{\mathrm I})^\top$ is positive semidefinite of rank $s-1$;
- **(M2)** $\Pi_*+\Pi_*^\top$ is positive semidefinite of rank $s-1$.

A positive semidefinite matrix of rank $s-1$ that vanishes on a vector $u$ is positive
definite on $u^\perp$ (Lemma 3.1), so (M2) bounds
$W^\top\Pi_*W\ge c\sum_{i<j}\lvert W_i-W_j\rvert^2$ (Lemma 3.2), and (M1) with their condition
(A) bounds $W^\top\Pi A^{\mathrm I}W\ge c\lvert W_s\rvert^2$ (Lemma 4.1). The cross terms from
the explicit convection are absorbed with Young's inequality and an inverse inequality,
which needs $h\le c_{\mathrm{CFL}}/N^2$ for $N$ Fourier modes, and Gronwall gives uniform
stability (Thm. 3.4). Neither matrix can be strictly positive definite; each condition forces
one zero eigenvalue and fixes one row combination of $\Pi$, so a candidate can be built with
those constraints and checked by computing eigenvalues (Prop. 7.1). Exact multipliers exist
for ARS(2,2,2) and ARS(4,4,3); for BHR(5,5,3)\* a numerical $\Pi$ has second-smallest
eigenvalues above 0.01, and for the original BHR(5,5,3) none was found (App. 7.2, Remark
7.2). The construction is inspired by Fu & Shu and recovers their energy estimates for
ARS-type pairs (Remark 3.3). The same energy argument, applied to the error equation, gives
the uniform-accuracy theorems on
[uniform accuracy of IMEX schemes](/results/uniform-accuracy-relaxation-systems.md). The
multistep analogue, testing with Nevanlinna–Odeh multipliers, is on
[multiplier energy technique](/methods/multiplier-energy-technique.md).

## Qualifications

- The method covers autonomous linear problems with bounded $L$; nonlinear problems
  are reached only through devices such as the adaptive filter of Sun & Shu (2021, §5).
- Sun et al. (2022) present the closed forms of Lemma 3.3 without proof. The
  semi-inner product is normalized with $L$ in Sun et al. (2022) and with $hL$ in Sun
  & Shu (2021, footnote 3); results are equivalent up to the factor $h$.
- Printed slips in the version read of Sun et al. (2022, arXiv v1): Ex. 4.3 prints
  $\mathrm{diag}\{1,\frac14\}$ for the factor whose correct value, by the printed
  energy identity, is $\mathrm{diag}\{1,\frac1{16}\}$; Eq. (3.17) prints $y_n$ where
  $w_n$ is meant.

# Citations

- [Sun et al. (2022)](/sources/sun-2022.md) — §1, Thm. 2.1, Lemmas 2.2–2.3, §3 (Lemmas 3.2–3.3, Thm. 3.4, Lemma 3.6, Thms. 3.5, 3.7, Remark 3.8), §4 Exs. 4.1–4.6.
- [Sun & Shu (2021)](/sources/sun-2021.md) — §2 (Eqs. 2.3–2.6, Def. 2.1, Props. 2.1–2.2), Thms. 3.1–3.2, §5.
- [Farrell et al. (2021)](/sources/farrell-2021.md) — §4.3, Table 1 (energy behaviour of Gauss–Legendre, Radau IIA, Lobatto IIIC and the Qin–Zhang DIRK).
- [Hu & Shu (2025)](/sources/hu-2025.md) — §3 (Eqs. (3.2)–(3.3), Lemmas 3.1–3.2, Thm. 3.4, Remark 3.3), Lemma 4.1, §7.1–7.2 (Prop. 7.1, Remark 7.2); arXiv v1.
