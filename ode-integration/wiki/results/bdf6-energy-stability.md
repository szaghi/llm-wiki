---
type: Result
title: "Energy stability of the six-step BDF method"
description: "Akrivis, Chen, Yu and Zhou prove by the energy technique that six-step BDF is unconditionally stable for linear parabolic problems: no Nevanlinna–Odeh multiplier exists for BDF6, but the relaxed multiplier (13/9, -25/36, 1/9) with Toeplitz positivity suffices, and the estimate extends to forcing and time-dependent operators."
status: established
aliases: [BDF6 stability, six-step BDF energy estimate, BDF6 multiplier]
tags: [linear-multistep, stability, stiff, implicit]
timestamp: 2026-10-20T06:18:00Z
---

# Energy stability of the six-step BDF method

**Statement** ([Akrivis et al. (2021)](/sources/akrivis-2021.md), arXiv v1, Thm. 3.1). Let $-L$ be
self-adjoint and positive definite on a Hilbert space, with energy norm
$\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ (page-local). Apply the six-step
[BDF method](/methods/backward-differentiation-formula.md)

$$\sum_{j=0}^6\alpha_jy_{n+j}=hLy_{n+6},\qquad60\,\varrho(\zeta)=147\zeta^6-360\zeta^5+450\zeta^4-400\zeta^3+225\zeta^2-72\zeta+10,$$

with a uniform step $h$ and arbitrary starting values $y_0,\dots,y_5$. Then

$$\lVert y_n\rVert^2+h\sum_{\ell=6}^n\lVert y_\ell\rVert_L^2\le C\sum_{j=0}^5\big(\lVert y_j\rVert^2+h\lVert y_j\rVert_L^2\big),\qquad n=6,\dots,N,$$

with $C$ independent of $h$ and $n$. There is no step-size restriction.

The authors call the result itself "well known": spectral proofs exist for the self-adjoint case
(after Thomée), and spectral plus Fourier proofs exist for non-self-adjoint and nonlinear
problems (after Akrivis, 2018). What is new is an energy proof, which they describe as much
simpler (§3). Energy proofs were previously available for BDF1–BDF5; see
[multiplier energy technique](/methods/multiplier-energy-technique.md).

## Ingredients

**No Nevanlinna–Odeh multiplier exists** (Remark 2.1). Write the (A) condition of the multiplier
technique as non-negativity of a polynomial in $x=\cos\phi$ on $[-1,1]$ ($\phi$ page-local).
Evaluated at $x=3/40$, this polynomial is below $-15.1563+13.7341\sum_{i=1}^6\lvert\mu_i\rvert$.
The Nevanlinna–Odeh condition $\sum\lvert\mu_i\rvert<1$ therefore forces it negative, about
$-1.42$. No multiplier with only $\mu_1$ and $\mu_2$ nonzero exists either, even under the
relaxed condition (Prop. 2.2). Three-component multipliers must satisfy
$0.41990729<\mu_1<\sqrt3$, $-1<\mu_2<-0.58852878$, $0<\mu_3<1$ and $\sum\lvert\mu_i\rvert>1$
(Prop. 2.3).

**A relaxed multiplier** (Prop. 2.1). The tuple

$$(\mu_1,\dots,\mu_6)=\big(\tfrac{13}9,-\tfrac{25}{36},\tfrac19,0,0,0\big),\qquad\mu(\zeta)=\zeta^3\big(\zeta-\tfrac12\big)^2\big(\zeta-\tfrac49\big),$$

with $\mu(\zeta)$ the multiplier polynomial (page-local), satisfies both conditions:

- **(A)**, i.e. $\operatorname{Re}\varrho(\zeta)/\mu(\zeta)>0$ for $\lvert\zeta\rvert>1$. This
  reduces to $4(1-x)P(x)\ge0$ on $[-1,1]$, with
  $P(x)=2(71+611x+1334x^2-5150x^3+4784x^4-1440x^5)>0$ there (Eqs. (2.9)–(2.10); $P$ page-local).
- **The trigonometric positivity condition (P2)**, with a margin:
  $$\tfrac{31}{32}-\tfrac{13}9\cos x+\tfrac{25}{36}\cos2x-\tfrac19\cos3x\ge0.0093>0$$
  (Eqs. (2.11)–(2.12)). The minimum of the cubic in $\cos x$ is at
  $\cos x=(25-\sqrt{145})/24$.

The polynomials $\varrho$ and $\mu$ are coprime, since $\varrho(1/2)=-37/3840$ and
$\varrho(4/9)\ne0$; the multiplier polynomial factors as
$\tfrac1{36}(2\zeta-1)^2(9\zeta-4)$, and the printed values $\varrho(\tfrac12)$ and the margin
0.0093 (minimum $0.00932$) reproduce *(compiler check, symbolic)*. Table 2.1 lists seven further multipliers, with up to six nonzero components, without
proofs (Remark 2.1).

**Proof structure** (§3). The steps:

1. Test the scheme with $y_{n+6}-\tfrac{13}9y_{n+5}+\tfrac{25}{36}y_{n+4}-\tfrac19y_{n+3}$.
2. The difference term is bounded below through Dahlquist's G-identity, because (A) holds, and
   telescopes in a G-norm of $(y_{n+1},\dots,y_{n+6})$; see [G-stability](/properties/g-stability.md).
3. The dissipative terms are summed over $n$ first. They form a quadratic form with a
   lower-triangular banded Toeplitz matrix whose symmetric part has the positive generating
   function above. By the Grenander–Szegő theorem it is positive definite, leaving only boundary
   terms in $y_3,\dots,y_8$ (Eqs. (3.7)–(3.10)).
4. Young's inequality with a parameter below $1/32$ and the equivalence of the G-norm with
   $\lVert y_n\rVert^2$ give the estimate.

Because $\mu_4=\mu_5=\mu_6=0$, the starting values $y_0,y_1,y_2$ in fact do not need their
energy norms on the right-hand side (end of the proof).

## Extensions

- **Forcing and perturbations** (Eqs. (3.13)–(3.15)). If the scheme carries an extra term
  $hv_{n+6}$, the estimate gains $Ch\sum_\ell\lVert v_\ell\rVert_{L,\star}^2$, where
  $\lVert v\rVert_{L,\star}=\lVert(-L)^{-1/2}v\rVert$ is the dual norm (page-local). Taking $v$
  as the consistency error gives optimal-order error estimates. This step is sketched, not
  detailed.
- **Time-dependent operators** (§3.1, Eqs. (3.12)–(3.23)). The estimate extends to self-adjoint
  $L(t)$ with a common domain, uniformly equivalent energy norms and bounded variation. The proof
  freezes the operator, sums by parts and applies a discrete Gronwall argument.

## Qualifications

- **Scope.** The result covers linear problems with self-adjoint $-L$, uniform steps and the
  energy norm. There are no numerical experiments.
- **Version read.** The ingested version is arXiv v1 (15 pages). The SIAM version of record
  (24 pages) was extended after it and was not read, so all locators refer to v1.
- **Printed slips** (recorded on the Source page). Eq. (3.11) omits the factor $h$ in front of
  the summed energy norms. Prop. 2.2 cites (2.2) where (2.20) gives the contradiction. Fig. 2.3
  and the text differ in the last digit of $-0.671118740185537$.

# Citations

- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: §1; §2 (Def. 2.1, Prop. 2.1, Eqs. (2.3)–(2.12), Props. 2.2–2.3, Remark 2.1, Table 2.1); §3 (Thm. 3.1, Lemma 3.1, Eqs. (3.1)–(3.15)); §3.1 (Eqs. (3.12)–(3.23)).
