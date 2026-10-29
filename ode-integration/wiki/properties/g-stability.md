---
type: Property
title: "G-stability"
description: "G-stability of a multistep (one-leg) method: a positive definite matrix G makes the G-norm of the history vector non-increasing on dissipative problems; Dahlquist's theorem makes it equivalent to A-stability, its identity is the energy-method tool behind BDF2, multiplier and IMEX-BDF proofs, and variable steps perturb it."
status: established
aliases: [G-norm, G-stable, Dahlquist's equivalence theorem, one-leg method, G-stability identity]
tags: [linear-multistep, stability, stiff, structure-preserving]
timestamp: 2026-10-29T18:13:00Z
---

# G-stability

For a $k$-step method the state is the history vector $Y_n=(y_n,\dots,y_{n+k-1})$. With a
symmetric positive definite $G=(g_{ij})\in\mathbb R^{k\times k}$ its **G-norm** is
$\lVert Y_n\rVert_G^2=\sum_{i,j}g_{ij}\langle y_{n+i-1},y_{n+j-1}\rangle$. A method is
**G-stable** if, for some such $G$ and every problem with
$\operatorname{Re}\langle f(t,y)-f(t,\hat y),y-\hat y\rangle\le0$, two numerical solutions
satisfy $\lVert Y_{n+1}-\hat Y_{n+1}\rVert_G\le\lVert Y_n-\hat Y_n\rVert_G$ for every $h>0$
*(standard definition supplied by the compiler; the sources use the notion through the identity
below)*. Dahlquist defined it for one-leg methods,
$\sum_j\alpha_jy_{n+j}=hf\big(\sum_j\beta_jt_{n+j},\sum_j\beta_jy_{n+j}\big)$, the "one-leg twins"
of linear multistep methods. It is the multistep analogue of
[B- and algebraic stability](/properties/a-stability.md) of Runge–Kutta methods *(compiler
remark, not in the sources)*.

## Dahlquist's equivalence and the G-identity

[Akrivis et al. (2021)](/sources/akrivis-2021.md) (arXiv v1, Lemma 2.1) recall the theorem from Dahlquist
(1978), Baiocchi–Crouzeix and Hairer–Wanner §V.6. Let $\varrho$ and a second real polynomial
$\mu(\zeta)=\sum_{j=0}^km_j\zeta^j$ (page-local $\mu$, $m_j$; the source writes its
coefficients $\mu_j$, which here denote the multipliers) of degree at most $k$ have no common divisor, one of them of degree
$k$, and let

$$\operatorname{Re}\frac{\varrho(\zeta)}{\mu(\zeta)}>0\quad\text{for }\lvert\zeta\rvert>1.\tag{A}$$

Then there are a symmetric positive definite $G\in\mathbb R^{k\times k}$ and reals
$\delta_0,\dots,\delta_k$ (page-local) such that, for all $v_0,\dots,v_k$ in a real inner-product
space,

$$\Big\langle\sum_{i=0}^k\alpha_iv_i,\sum_{j=0}^km_jv_j\Big\rangle=\sum_{i,j=1}^kg_{ij}\langle v_i,v_j\rangle-\sum_{i,j=1}^kg_{ij}\langle v_{i-1},v_{j-1}\rangle+\Big\lVert\sum_{i=0}^k\delta_iv_i\Big\rVert^2.\tag{G}$$

Condition (A) states that the multistep
method $(\varrho,\mu)$ is A-stable, and (G) states that its one-leg twin is G-stable; Lemma 2.1
gives the direction A $\Rightarrow$ G. With $\mu=\sigma$ this is Dahlquist's theorem: a linear
multistep method is A-stable iff its one-leg twin is G-stable.
[Ma et al. (2026)](/sources/ma-2026.md) (§2.2, citing Dahlquist) use the same equivalence.

The identity is an energy tool. Take the inner product of the scheme with $\sum_jm_jv_j$. The
left side of (G) becomes the discrete time derivative, which telescopes in the G-norm, plus a
non-negative remainder. In the proofs the $\mu(\zeta)$ of (A) is not the method's $\sigma$ but an
auxiliary polynomial. It defines low-order auxiliary methods that are never computed with
(Akrivis et al. 2021, remark after Lemma 2.1); this is the
[multiplier energy technique](/methods/multiplier-energy-technique.md).

## BDF2

BDF2 is A-stable and coincides with its one-leg twin ($\sigma(\zeta)=\zeta^2$), so it is G-stable
with $\mu(\zeta)=\zeta^2$. Ma et al. (2026, Lemma 2.1, case $k=2$)
print the data of the identity with the normalization $\alpha_2=1$: for
$\alpha=(\tfrac13,-\tfrac43,1)$,

$$\Big(v_2-\tfrac43v_1+\tfrac13v_0\Big)v_2=G(v_1,v_2)-G(v_0,v_1)+\tfrac16\big(v_2-2v_1+v_0\big)^2,\qquad G(v_1,v_2)=\tfrac16v_1^2-\tfrac23v_1v_2+\tfrac56v_2^2$$

(their IMEX form, with the extrapolation $2v_1-v_0$ written out). The form $G$ is positive
definite with determinant $1/36$, and $6G(v_1,v_2)=v_2^2+(2v_2-v_1)^2$ *(compiler check by
expansion, not in the source)*. The remainder is the squared
difference between the new value and its linear extrapolation. That is why the same identity
serves IMEX-BDF2, whose explicit part is evaluated at that extrapolation; see
[IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md).

## Variable steps

On a nonuniform grid the identity holds only up to a perturbation.
[García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) (Lemma 7) prove a variable-step BDF2 inequality with the functional

$$G_n=\frac{r_{n-1}}{2(1+r_{n-1})}\lVert e_n\rVert^2+\frac14\lVert 2e_n-e_{n-1}\rVert^2$$

($e_n$ the discrete error, $G_n$ page-local, $r_n=h_n/h_{n-1}$). The perturbation is bounded by
$\frac{K_0}{r_{\min}}(1+r_{\max})^2(\lvert r_{n-1}-1\rvert+\lvert r_n-1\rvert)\,G_n$, with
$K_0\le75/14$ and $r_{\min}$, $r_{\max}$ (page-local) the lower and upper ratio bounds
(Eqs. (69)–(82)). The coercivity bound $G_n\ge\frac{0.07}{1+r_{\max}}r_{n-1}(\lVert e_{n-1}\rVert^2+\lVert e_n\rVert^2)$
comes from an eigenvalue bound checked graphically (Eq. (81), Fig. 1). The error therefore grows
with the total variation of the step ratios, and their theorems assume this variation is bounded
(Eq. (85)). The authors do not call $G_n$ a G-norm; at $r_n=1$ it is $\tfrac32$ times the
constant-step BDF2 form $G(e_{n-1},e_n)$ above *(compiler check, not in the sources)*.

## Lyapunov norms for the trapezoidal rule (Dahlquist 1963)

[Dahlquist (1963)](/sources/dahlquist-1963.md) (§3) does not define G-stability, but proves
nonlinear error bounds for the trapezoidal rule by a quadratic form in a time-dependent norm.
With page-local symbols (the same as on [B-convergence](/definitions/b-convergence.md)): $e_n$
the difference of two numerical solutions, $g_n=f(t_n,\hat y_n)-f(t_n,y_n)$ the corresponding
difference of right-hand sides, and $\lVert v\rVert_n^2=v^\top\Sigma(t_n)v$ for a symmetric positive
definite $d\times d$ matrix $\Sigma(t)$ obtained from a Lyapunov function of the error equation
(Eq. (3.15)). The trapezoidal recursion reads $e_{n+1}-\tfrac12hg_{n+1}=e_n+\tfrac12hg_n+q_n$
($q_n$ the perturbations, Eq. (3.14)), and the identity

$$\big\lVert e+\tfrac12hg\big\rVert_n^2-\big\lVert e-\tfrac12hg\big\rVert_{n-1}^2=h\,W\qquad(3.17)$$

defines a discrete analogue $W$ of the derivative of the Lyapunov function, which tends to it as
$h\to0$ (Eq. (3.18)). Under the one-sided condition $W\le2\mu_\Sigma(\lvert e\rvert^2+\lvert\tfrac12hg\rvert^2)$
and $h\mu'_\Sigma<1$,

$$\big\lVert e+\tfrac12hg\big\rVert_n^2\le\frac{1+h\mu'_\Sigma}{1-h\mu'_\Sigma}\,\big\lVert e-\tfrac12hg\big\rVert_{n-1}^2\qquad(3.23),$$

so the quantity $\lVert e_n-\tfrac12hg_n\rVert_{n-1}$ is propagated with the factor
$e^{\rho h}$, $\rho=\frac1{2h}\log\frac{1+h\mu'_\Sigma}{1-h\mu'_\Sigma}$ (Eqs. (3.25)–(3.27)). This
yields the bound of Theorem 3.1, bounded for all times when $\mu_\Sigma<0$, which Dahlquist calls
"a generalization of the A-stability property" (pp. 37–41). The matrix acts on the state
($d\times d$) of a one-step recursion, not on a $k$-step history vector as the G-norm above does.

## Where the sources use it

- **BDF1–BDF2 on parabolic problems:** directly (Akrivis et al. 2021, §1;
  [Akrivis et al. (2024)](/sources/akrivis-2024.md), §1.3).
- **BDF3–BDF6:** through multipliers (Akrivis et al. 2021, §2–3), giving
  [BDF6 energy stability](/results/bdf6-energy-stability.md).
- **IMEX-BDF1–4 on relaxation systems:** two identities, one in the G-norm weighted by the
  symmetrizer and one for the relaxation term (Ma et al. 2026, Lemmas 2.1–2.2, Thm. 3.1).
- **Variable-step BDF2 for Navier–Stokes:** the perturbed functional above (García-Archilla &
  Novo 2023, §3.2).

## Qualifications

- **Dahlquist (1963) does not define G-stability.** He works with a $d\times d$ Lyapunov matrix
  for the trapezoidal rule only; the $k\times k$ G-norm and the one-leg formulation on this page
  are those recalled by Akrivis et al. (2021).
- **Dahlquist's own definition is not restated.** The sources state the equivalence through
  identity (G) and the remark that (A) and (G) express A-stability of a multistep method and
  G-stability of its one-leg twin. The definition at the top of this page is supplied by the
  compiler.
- **Version read.** Akrivis et al. (2021), García-Archilla & Novo (2023) and Ma et al. (2026)
  were read as arXiv v1 preprints.

# Citations

- [Dahlquist (1963)](/sources/dahlquist-1963.md) — §3 (Eqs. (3.14)–(3.18), (3.23)–(3.27), Thm. 3.1, pp. 37–41).

- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: §1, Lemma 2.1 and the remark after it, §2–3.
- [Ma et al. (2026)](/sources/ma-2026.md) — §2.2 (Lemmas 2.1–2.2), Thm. 3.1.
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §3.2 (Lemma 7, Eqs. (69)–(85), Fig. 1).
- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1.3.
