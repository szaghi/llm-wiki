---
type: Method
title: "Multiplier energy technique for multistep methods (Nevanlinna–Odeh multipliers)"
description: "Energy proofs for BDF and IMEX-BDF on parabolic and relaxation problems: test the scheme with y_{n+k} minus a multiplier combination of past values, telescope a G-norm, and bound the dissipative term per step (Nevanlinna–Odeh) or summed through Toeplitz positivity (Grenander–Szegő); known multipliers, the BDF6 gap and the variable-step BDF2 extension."
status: established
aliases: [multiplier technique, Nevanlinna–Odeh multiplier, energy technique for BDF, multiplier method, two-multiplier technique, Grenander–Szegő argument]
tags: [linear-multistep, stability, stiff, implicit, structure-preserving]
timestamp: 2026-10-20T16:00:00Z
---

# Multiplier energy technique for multistep methods

The energy method proves stability of a time discretization of $y'=Ly$, with $-L$ self-adjoint
and positive definite on a Hilbert space. It takes the inner product of the scheme with a
suitable combination of unknowns and sums over the steps. For the
[BDF method](/methods/backward-differentiation-formula.md)
$\sum_{j=0}^k\alpha_jy_{n+j}=hLy_{n+k}$, testing with $y_{n+k}$ works only when BDF$k$ is
A-stable, i.e. $k\le2$. The **multiplier technique** of Nevanlinna and Odeh tests instead with

$$y_{n+k}-\sum_{j=1}^k\mu_jy_{n+k-j},$$

with multipliers $\mu_1,\dots,\mu_k$ chosen so that both terms of the tested equation can be
controlled ([Akrivis et al. (2021)](/sources/akrivis-2021.md), arXiv v1, §2, Eq. (2.1)). Akrivis et al.
recall that the technique became widely known after Lubich, Mansour and Venkataraman applied it
to parabolic equations (§2).

Notation on this page: $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ is the energy norm and
$\langle v,w\rangle_L=\langle(-L)^{1/2}v,(-L)^{1/2}w\rangle$ its inner product; both are
page-local. $\mu(\zeta)=\zeta^k-\mu_1\zeta^{k-1}-\dots-\mu_k$ is the multiplier polynomial,
also page-local.

## The two conditions

Testing splits the equation into two terms (Akrivis et al. 2021, §2, Def. 2.1).

1. **The difference term** $\big\langle\sum_j\alpha_jy_{n+j},\,y_{n+k}-\sum_j\mu_jy_{n+k-j}\big\rangle$
   telescopes in a G-norm if the pair $(\varrho,\mu)$ satisfies
   $$\operatorname{Re}\frac{\varrho(\zeta)}{\mu(\zeta)}>0\quad\text{for }\lvert\zeta\rvert>1\tag{A}$$
   and $\varrho$, $\mu$ are coprime. This is Dahlquist's G-identity; see
   [G-stability](/properties/g-stability.md). By the maximum principle, (A) is checked on the
   unit circle as $\operatorname{Re}\big(\varrho(e^{i\phi})\mu(e^{-i\phi})\big)\ge0$ (Eq. (2.5);
   $\phi$ page-local).
2. **The dissipative term** $h\big\langle y_{n+k},\,y_{n+k}-\sum_j\mu_jy_{n+k-j}\big\rangle_L$
   must be bounded below by a multiple of $h\lVert y_{n+k}\rVert_L^2$, up to terms that can be
   absorbed. There are two versions:
   - **(P1)**, per step: $1-\sum_j\lvert\mu_j\rvert>0$ (Nevanlinna–Odeh);
   - **(P2)**, after summation over $n$: $1-\sum_j\mu_j\cos(jx)>0$ for all real $x$.

A $k$-tuple satisfying (A) and (P1) is a **Nevanlinna–Odeh multiplier**. Akrivis et al. (2021)
call a tuple satisfying (A) and only (P2) a **multiplier**. (P1) implies (P2), and the two
coincide for multipliers with a single nonzero component (§2.1).

**Why (P2) suffices.** Summed over $n=k,\dots,m$, the dissipative terms form a quadratic form
whose matrix is lower-triangular, banded and Toeplitz: 1 on the main diagonal and $-\mu_j$ on
the $j$-th subdiagonal. Its symmetric part has generating function
$f(x)=1-\sum_j\mu_j\cos(jx)$ (page-local). Akrivis et al. split off a margin $\tfrac1{32}$ of
the diagonal, so their $f$ starts with $\tfrac{31}{32}$ (Eqs. (2.11), (3.7)–(3.9)). By the **Grenander–Szegő theorem**, the
eigenvalues of a symmetric Toeplitz matrix lie between the minimum and the maximum of its
generating function. Hence $\min f>0$ makes the summed form positive definite for every number
of steps (Lemma 3.1, citing Chan–Jin). [Akrivis et al. (2024)](/sources/akrivis-2024.md)
(Thm. 2.1, citing Garoni and Serra-Capizzano) state the theorem in its sharper form: the
eigenvalues lie in the open interval, and the extreme ones tend to the extrema of $f$ as the
size grows.

## Which multipliers exist

| $k$ | Status | Source |
|---|---|---|
| 1, 2 | $\mu=0$: BDF1 and BDF2 are A-stable, so the energy method applies directly | Akrivis et al. (2021), §1 |
| 3, 4, 5 | Nevanlinna–Odeh multipliers exist; optimal ones (minimal $\sum\lvert\mu_j\rvert$) were given by Akrivis–Katsoprinakis (2016) | Akrivis et al. (2021), §1–2, as recalled |
| 6 | no Nevanlinna–Odeh multiplier; the (P2) multiplier $(\mu_1,\mu_2,\mu_3)=(\tfrac{13}9,-\tfrac{25}{36},\tfrac19)$ exists | Akrivis et al. (2021), Remark 2.1, Prop. 2.1 |

A necessary condition, recalled from Nevanlinna–Odeh, is $\sum_j\lvert\mu_j\rvert\ge\cos\vartheta_k$,
with $\vartheta_k$ (page-local) the angle of A($\alpha$)-stability of BDF$k$ (Eq. (2.2)). For
BDF6 ($\vartheta_6\approx17.84^\circ$) this forces $\sum\lvert\mu_j\rvert$ close to 1. Evaluating
the (A) polynomial at a single point then shows that no tuple with $\sum\lvert\mu_j\rvert\le1$
works. The BDF6 results are on [BDF6 energy stability](/results/bdf6-energy-stability.md).

**Shape of the (P2) region.** In the $(\mu_1,\mu_2)$ plane, with the other multipliers zero,
(P2) holds on the union of a triangle and an ellipse,
$\{-\tfrac13\le\mu_2<1-\lvert\mu_1\rvert\}\cup\{4(\mu_2+\tfrac12)^2+\tfrac12\mu_1^2<1\}$. It
implies $\lvert\mu_1\rvert<\sqrt2$ and $\lvert\mu_2\rvert<1$, while the (P1) region is the
diamond $\lvert\mu_1\rvert+\lvert\mu_2\rvert<1$. The same shape appears in the $(\mu_2,\mu_4)$
and $(\mu_3,\mu_6)$ planes (Akrivis et al. 2021, §2.1, Eqs. (2.16)–(2.17), Fig. 2.2).

## Variable steps: two multipliers for BDF2

On a nonuniform grid the summed matrix is no longer Toeplitz. Akrivis et al. (2024) test
variable-step BDF2 with

$$y_n-\mu_1y_{n-1}-\mu_2y_{n-2},\qquad0<\mu_1<1,\ -1<\mu_2<0,$$

($\mu_1$, $\mu_2$ are their $\delta$, $\eta$) and bound the sum of the elliptic terms in one go (§1.3, Eqs. (1.7)–(1.8)). Earlier proofs used
one multiplier ($\mu_2=0$) and bounded each term separately. With step ratios
$r_n=h_n/h_{n-1}\le r$ for all $n$, their results are:

- **Lemma 2.1, a Grenander–Szegő variant for non-Toeplitz matrices.** The summed matrix is
  lower-triangular and banded, with entries depending on all the ratios $r_i\in(0,r]$. The whole
  family is uniformly positive definite iff
  $$p(x)=\frac1{1+r}\big[1+\mu_2r-\mu_1\sqrt r\,x-2\mu_2r\,x^2\big]\ge c>0\quad\text{for all }x\in[-1,1]$$
  (Eqs. (2.1)–(2.3); $p$ page-local). Necessity follows from the constant-ratio case, which is
  Toeplitz.
- **Lemma 3.2, the difference terms.** They telescope under
  $$r\le r^\star(\mu_1,\mu_2)=\frac{\sqrt{1+\mu_1+3\mu_2}}{2\sqrt{1+\mu_2}-\sqrt{1+\mu_1+3\mu_2}},$$
  together with $2-\mu_1+2\mu_2\ge0$ and $1+\mu_1+3\mu_2\ge0$ (Eq. (3.1)).
- **§4, the optimum.** Combining both conditions and maximizing over $(\mu_1,\mu_2)$ reduces to
  the real root of a quintic. It gives $\mu_1^\star\approx0.967237837020572$,
  $\mu_2^\star\approx-0.179320334471962$ and the ratio bound $r^\star\approx1.9398285699451$
  (Eq. (4.17)).
- **Remark 3.1, one multiplier.** Within the same framework, the best single multiplier is
  $\mu_1=0.72349$, giving Emmrich's bound 1.9104.
- **Footnote 1 (p. 9).** $\sup r^\star(\mu_1,\mu_2)=r^\star(1,0)=1+\sqrt2$, the zero-stability
  bound.

The theorem built on these lemmas is on
[variable-step BDF2 stability](/results/variable-step-bdf2-stability.md).

## IMEX-BDF and relaxation systems

[Ma et al. (2026)](/sources/ma-2026.md) (Lemma 2.1, from Akrivis–Katsoprinakis and Hu–Shu) use
two identities for the IMEX-BDF pair $(\alpha,\beta^{\mathrm E})$ of order $k\le4$, where
$\beta^{\mathrm E}$ are the explicit extrapolation weights (page-local; see
[IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md)). Both identities
hold with a multiplier $v_k-\sum_{j=1}^{k-1}\mu_jv_{k-j}$ (their $\eta_j$; no $v_0$ term):

- the difference identity telescopes a positive definite form $G$. Its remainder is the square of
  the multiplier term minus a multiple of the explicit extrapolation;
- the identity for the stiff term telescopes a positive semidefinite form plus a square.

A vector version holds for any symmetric positive definite weight (Lemma 2.2). With the
symmetrizer of the relaxation system as weight, the stiff relaxation term becomes dissipative and
drops out uniformly in the relaxation time $\varepsilon$ (Thm. 3.1). The explicit convection term
is absorbed under $h\le c/N^2$, with $N$ (page-local) the number of Fourier modes. Ma et al.
attribute the restriction $k\le4$ to the availability of these identities (§1). The resulting
uniform-accuracy theorem is on
[uniform accuracy for relaxation systems](/results/uniform-accuracy-relaxation-systems.md).

[García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) need no multiplier for BDF2.
They test with the error itself and control the step-ratio perturbation of the G-form directly
(Lemma 7; see [G-stability](/properties/g-stability.md)).

## Qualifications

- **Terminology.** Akrivis et al. (2021) use "multiplier" for (A) plus (P2) and reserve
  "Nevanlinna–Odeh multiplier" for (A) plus (P1). Earlier literature, as they note, uses
  "multiplier" for the (P1) notion. Read each source's definition before comparing statements.
- **Optimality is relative to the technique.** The bound 1.9398 is optimal within the
  two-multiplier technique, and 1.9104 within the single-multiplier one. Neither is claimed
  sharp for parabolic stability (Akrivis et al. 2024, §4, Remark 3.1).
- **Printed slips.**
  - Akrivis et al. (2021, Eq. (2.2)) print $\sum\lvert\mu_j\rvert\ge0.9516169$ for BDF6. That
    value is $\cos(17.90^\circ)$, while $\cos(17.84^\circ)\approx0.9519$; the printed bound is
    weaker, so it remains true.
  - One step of the proof of their Prop. 2.3 does not follow as printed, as recorded on the
    Source page.
  - Akrivis et al. (2024, p. 12) evaluate $\min p\approx7.3592\cdot10^{-6}$ at the rounded
    $r=1.9398$; at the exact bound the value is about $7.107\cdot10^{-6}$. Both exceed the
    constant $10^{-6}$ that is used, so the result is unaffected *(compiler check,
    recorded on the Source page)*.
- **Version read.** Akrivis et al. (2021) and Ma et al. (2026) were read as arXiv v1 preprints;
  the published Akrivis et al. (2021) is substantially longer.

# Citations

- [Akrivis et al. (2021)](/sources/akrivis-2021.md) — arXiv v1: §1, §2 (Eqs. (2.1)–(2.5), Def. 2.1, Prop. 2.1, Remark 2.1), §2.1 (Eqs. (2.16)–(2.17), Fig. 2.2), §3 (Lemma 3.1, Eqs. (3.7)–(3.9)).
- [Akrivis et al. (2024)](/sources/akrivis-2024.md) — §1.3 (Eqs. (1.7)–(1.8)), §2 (Lemma 2.1, Thm. 2.1, Remark 2.1), §3 (Lemma 3.2, Eq. (3.1), Remark 3.1), §4 (Eq. (4.17)), footnote 1.
- [Ma et al. (2026)](/sources/ma-2026.md) — §1, §2.2 (Lemmas 2.1–2.2), Thm. 3.1.
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §3.2 (Lemma 7).
