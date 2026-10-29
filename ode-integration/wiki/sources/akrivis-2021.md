---
type: Source
title: "Akrivis et al. (2021) — The Energy Technique for the Six-Step BDF Method"
description: "Extends the Nevanlinna–Odeh multiplier energy technique to six-step BDF, for which no classical multiplier exists, by relaxing the multiplier condition to trigonometric positivity and bounding the summed dissipation with the Grenander–Szegő theorem; proves BDF6 energy stability for self-adjoint parabolic problems."
resource: "doi:10.1137/21m1392656"
source_kind: paper
authors: [Akrivis G., Chen M., Yu F., Zhou Z.]
year: 2021
venue: "SIAM J. Numer. Anal. 59:2449-2472"
local_file: "/home/stefano/papers/mosaic/ode-integration/2021_Crossref_SIAM_Journal_on_Numerical_Analysis_Akrivis_The_Energy_Technique_for_the_Six-Step_BDF_Method.pdf"
tags: [linear-multistep, bdf, energy-method, stability, parabolic]
timestamp: 2026-10-19T13:16:00Z
---

# Summary

The paper proves stability of the six-step
[backward differentiation formula](/methods/backward-differentiation-formula.md)
(BDF6) for the abstract linear parabolic problem $y'=Ly$, with $-L$ positive
definite and self-adjoint on a Hilbert space, by the energy technique. BDF1
and BDF2 are [A-stable](/properties/a-stability.md) and yield to the plain
energy method. BDF3–BDF5 yield to the
[multiplier technique](/methods/multiplier-energy-technique.md) of Nevanlinna
and Odeh: the scheme is tested with $y_{n+k}-\sum_j\mu_jy_{n+k-j}$, where the
pair $(\varrho,\mu)$ is A-stable, hence
[G-stable](/properties/g-stability.md) by Dahlquist's equivalence, and the
multiplier satisfies $1-\sum_j\lvert\mu_j\rvert>0$. The paper shows that no
such multiplier exists for $k=6$.

The contribution relaxes the multiplier condition to trigonometric
positivity, $1-\sum_j\mu_j\cos(jx)>0$ for all real $x$. This suffices if the
energy identity is summed over $n$ before the dissipation term is estimated:
the summed term is a quadratic form with a banded lower-triangular Toeplitz
matrix, and the Grenander–Szegő theorem makes its symmetric part positive
definite. The explicit multiplier $(\mu_1,\mu_2,\mu_3)=(13/9,-25/36,1/9)$,
$\mu_4=\mu_5=\mu_6=0$, works for BDF6. The paper also characterizes the
positivity region in a coordinate plane (a triangle joined to an ellipse),
proves that no two-component multiplier works for BDF6, and gives necessary
conditions for three-component ones.

The main theorem is the [energy stability of BDF6](/results/bdf6-energy-stability.md),
uniform in $h$ and $n$, extended to forcing terms (optimal-order error
estimates via the consistency error) and to time-dependent self-adjoint
operators of bounded variation. The result itself was known from spectral
proofs; the novelty is the simplicity of the energy proof. There are no
numerical experiments.

# Version read

The file is the arXiv preprint arXiv:2007.08924v1 [math.NA], 17 July 2020
(header dated 20 July 2020), 15 pages, all read; it is not the version of
record, despite the "Crossref" in the archive filename. The SIAM article
spans 24 journal pages (2449–2472), so the published version was extended
after v1 and its content was not seen. Title and authors match Crossref.
Section, equation and proposition numbers cited here are those of arXiv v1.

# Key claims

1. BDF$k$ has order $k$ and is A($\alpha$)-stable with $\alpha=90^\circ$ ($k=1,2$), $\approx86.03^\circ$ ($k=3$), $\approx73.35^\circ$ ($k=4$), $\approx51.84^\circ$ ($k=5$), $\approx17.84^\circ$ ($k=6$) (§1). **Stated**
2. The A-stable BDF1 and BDF2 are stable by the plain energy method; the Nevanlinna–Odeh multiplier technique extends this to BDF3–BDF5 (§§1–2). **Stated**
3. Dahlquist's equivalence: if $\varrho$ and $\mu$ are coprime real polynomials of degree $\le k$ with $\operatorname{Re}\,\varrho(\zeta)/\mu(\zeta)>0$ for $\lvert\zeta\rvert>1$, there exist a symmetric positive definite $G\in\mathbb R^{k\times k}$ and reals $\delta_0,\dots,\delta_k$ such that the inner product of $\sum_i\alpha_iv_i$ with $\sum_j\mu_jv_j$ equals a G-norm difference plus $\lVert\sum_i\delta_iv_i\rVert^2$ (Lemma 2.1, identity (G)). **Stated**
4. Any multiplier of BDF$k$ satisfies $\sum_j\lvert\mu_j\rvert\ge\cos\alpha$, with $\alpha$ the A($\alpha$) angle of BDF$k$; for BDF6 the paper prints $\sum_j\lvert\mu_j\rvert\ge0.9516169$ (Eq. 2.2). **Stated** (see Printed slips)
5. Estimating the dissipation term per time level needs $1-\sum_j\lvert\mu_j\rvert>0$ (P1); summing over $n$ first needs only $1-\sum_j\mu_j\cos(jx)>0$ for all real $x$ (P2) (§2, after Def. 2.1). **Derived**
6. $(\mu_1,\dots,\mu_6)=(13/9,-25/36,1/9,0,0,0)$ is a multiplier (A-stability of the pair and (P2)) for BDF6, with $\mu(\zeta)=\zeta^3(\zeta-\tfrac12)^2(\zeta-\tfrac49)$ (Prop. 2.1, Eqs. 2.3–2.4). **Proved**
7. For this multiplier the A-stability condition reduces to $4(1-x)P(x)\ge0$ on $[-1,1]$, $x=\cos\varphi$, with $P(x)=2(71+611x+1334x^2-5150x^3+4784x^4-1440x^5)>0$ there (Eqs. 2.9–2.10). **Proved**
8. For this multiplier $\tfrac{31}{32}-\tfrac{13}{9}\cos x+\tfrac{25}{36}\cos2x-\tfrac19\cos3x>0$: as a cubic in $\cos x$ its minimum on $[-1,1]$ is at $(25-\sqrt{145})/24$, with value $0.009321552602567$ (Eqs. 2.11–2.12, Fig. 2.1). **Proved**
9. (P1) implies (P2); they coincide for single-component multipliers, so the (P2) region meets each coordinate axis in $(-1,1)$ (§2.1). **Proved**
10. The (P2) region in the $(\mu_1,\mu_2)$ plane is the union of the triangle $-\tfrac13\le\mu_2<1-\lvert\mu_1\rvert$ and the ellipse $4(\mu_2+\tfrac12)^2+\tfrac12\mu_1^2<1$, so $\lvert\mu_1\rvert<\sqrt2$ and $\lvert\mu_2\rvert<1$; the same shape holds in the $(\mu_2,\mu_4)$ plane ($k\ge4$) and the $(\mu_3,\mu_6)$ plane ($k=6$) (§2.1, Eqs. 2.16–2.17, Fig. 2.2). **Proved**
11. No BDF6 multiplier with $\mu_3=\dots=\mu_6=0$ exists: A-stability at $x=-4/25$ forces $\mu_2<-0.672343782385853$, and at $x=0.99$ forces $\mu_2\ge-0.671118740185537$ (Prop. 2.2, Fig. 2.3). **Proved**
12. A multiplier $(\mu_1,\mu_2,\mu_3,0,0,0)$ of BDF6 must satisfy $0.41990729<\mu_1<\sqrt3$, $-1<\mu_2<-0.58852878$, $0<\mu_3<1$ and $\lvert\mu_1\rvert+\lvert\mu_2\rvert+\lvert\mu_3\rvert>1$ (Prop. 2.3). **Proved** (one printed step does not follow; see Printed slips)
13. No Nevanlinna–Odeh multiplier exists for BDF6: at $x=3/40$ the general A-stability polynomial satisfies $P(3/40)<-15.1563+13.7341\sum_i\lvert\mu_i\rvert$, which is negative when $\sum_i\lvert\mu_i\rvert\le1$ (Remark 2.1). **Proved**
14. The BDF6 multiplier is not unique: Table 2.1 lists seven further multipliers with up to six nonzero components (Remark 2.1). **Stated** (no proofs for the table entries)
15. Grenander–Szegő: the eigenvalues of a symmetric Toeplitz matrix lie between the minimum and maximum of its generating function, so a positive minimum makes it positive definite for every size (Lemma 3.1). **Stated**
16. BDF6 satisfies $\lVert y_n\rVert^2+h\sum_{\ell=6}^n\lVert y_\ell\rVert_L^2\le C\sum_{j=0}^5\big(\lVert y_j\rVert^2+h\lVert y_j\rVert_L^2\big)$ for $n=6,\dots,N$, with $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ and $C$ independent of $h$ and $n$ (Thm. 3.1, Eq. 3.1). **Proved**
17. The BDF6 stability result is "well known"; the novelty is the simplicity of the energy proof, while the spectral and spectral-plus-Fourier proofs are "significantly more involved" (§3). **Stated**
18. Because $\mu_4=\mu_5=\mu_6=0$, the terms in $y_0$, $y_1$, $y_2$ are not needed in the energy-norm part of the right-hand side (end of proof of Thm. 3.1). **Derived**
19. The perturbed scheme $\sum_{i=0}^6\alpha_iy_{n+i}-hLy_{n+6}=hv_{n+6}$ is stable with the extra term $Ch\sum_{\ell=6}^n\lVert v_\ell\rVert_{L,\star}^2$; taking $v$ as the consistency error gives optimal-order error estimates (Eqs. 3.13–3.15). **Derived** (sketch)
20. The stability estimate extends to time-dependent self-adjoint $L(t)$ with common domain, uniformly equivalent energy norms and bounded variation, by freezing the operator, summation by parts and a discrete Gronwall argument (§3.1, Eqs. 3.12–3.23). **Proved**
21. Optimal Nevanlinna–Odeh multipliers (minimal $\sum_j\lvert\mu_j\rvert$) for BDF3–BDF5 were given by Akrivis and Katsoprinakis (2016) (§2). **Stated**
22. The multiplier technique became widely known after its first application to parabolic equations by Lubich, Mansour and Venkataraman (2013) (§2). **Stated**

# Printed slips

- Eq. 3.11 (p. 12, checked visually): the left-hand side prints $\frac1{32}\sum_{n=6}^m\lVert u^n\rVert^2$ without the factor $\tau$ that (3.6) and (3.8) give; it also writes the G-norm vector as $\mathcal U$ where (3.4)–(3.6) use $U$.
- Eq. 2.2: "for the six-step BDF method this means that $|\mu_1|+\dots+|\mu_6|\geqslant0.9516169$", but $\cos(17.84^\circ)=0.95192$; the printed constant corresponds to $17.896^\circ$. The printed bound is weaker, so the inequality still holds.
- Fig. 2.3 caption prints $\mu_2\geqslant-0.671118740185535$; the text and (2.21) print $-0.671118740185537$.
- Prop. 2.2 proof: "This together with (2.2) leads to a contradiction"; the contradiction is with (2.20), not (2.2).
- Prop. 2.3 proof: from $\mu_2<-0.65263636\cdot10^{-2}$ it asserts "$274/625+1154\mu_2/25<0$", which needs $\mu_2<-0.009497$; the step does not follow as printed (the conclusion $\mu_1>0$ may still hold).
- Prop. 2.3 proof: "$0<|\mu_3|<1$" where only $|\mu_3|<1$ has been shown.
- Typos: "It $|\mu_2|\leqslant|\mu_1|/4$" (for "If", §2.1); "from bellow" (§3); "summation be parts" (§3.1); "nonegativity" (Prop. 2.3); "the relaxed positive condition".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$ | $y$, $y_n$ | superscript step index |
| $\tau$ | $h$ | uniform step, $\tau=T/N$ |
| $A$, $u'+Au=0$ | $-L$, $y'=Ly$ | positive definite self-adjoint; **collision** with the Butcher matrix |
| $H$, $(\cdot,\cdot)$, $\lvert\cdot\rvert$ | $\langle\cdot,\cdot\rangle$, $\lVert\cdot\rVert$ | Hilbert space inner product and norm |
| $\lVert v\rVert=\lvert A^{1/2}v\rvert$, $\langle\cdot,\cdot\rangle$ | $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ (page-local, as on the result pages), — | energy norm and inner product; **collision**: the source's $\langle\cdot,\cdot\rangle$ and $\lVert\cdot\rVert$ are the energy ones |
| $\lVert\cdot\rVert_\star$ | $\lVert\cdot\rVert_{L,\star}$ | dual norm |
| $q$ | $k$ | number of steps; **collision**: registry $q$ is the stage order |
| $\alpha(\zeta)$, $\alpha_j$ | $\varrho(\zeta)$, $\alpha_j$ | normalized by $\beta(\zeta)=\zeta^q$, so $\alpha_6=147/60$; **collision** with the A($\alpha$) angle |
| $\beta(\zeta)=\zeta^q$ | $\sigma(\zeta)=\zeta^k$ | |
| $\vartheta_q$ | A($\alpha$) angle $\alpha$ of BDF$k$ | |
| $\mu_j$, $(\mu_1,\dots,\mu_q)$ | $\mu_j$ | agree; in Lemma 2.1 the source's $\mu_j$ are instead the coefficients of $\mu(\zeta)$ |
| $\mu(\zeta)=\zeta^q-\mu_1\zeta^{q-1}-\dots-\mu_q$ | $\mu(\zeta)$ | multiplier polynomial, defined locally |
| $\mu_0:=-31/32$ | — | auxiliary diagonal coefficient in §3 |
| $G=(g_{ij})$, $\lvert U^n\rvert_G$ | $G$, $\lVert\cdot\rVert_G$ | agree; $U^n=(u^{n-5},\dots,u^n)^\top$ |
| $\delta_i$ | $\delta_i$ | remainder-square coefficients of (G) |
| (A), (P1), (P2) | — | A-stability of the pair $(\varrho,\mu)$; Nevanlinna–Odeh condition; relaxed positivity |
| $P(x)$, $x=\cos\varphi$ | — | A-stability polynomial, redefined in (2.10), (2.19), (2.22), Remark 2.1 |
| $f$, $p$ | — | trigonometric positivity function and its cubic in $\cos x$; **collision**: $f$ is also the forcing (§3.1) and the Toeplitz generating function (Def. 3.1), registry $f$ is the right-hand side |
| $L$, $L_s$ | — | lower-triangular Toeplitz matrix and its symmetric part; **collision** with the registry linear operator $L$ |
| $T_n$, $t_k$ | — | Toeplitz matrix and its diagonals |
| $K$ | — | unit circle; **collision** with the iteration count $K$ |
| $v^n$ | $v_n$ | perturbation or consistency error |
| $\sigma$ | — | bounded-variation modulus of $A(t)$; **collision** with $\sigma(\zeta)$ |
| $M^m$, $E^\ell$, $a_\ell$ | — | Gronwall quantities of §3.1; **collision**: $M$ is the mass matrix |

# Reference list

The paper prints 13 references in numbered style ([1]–[13]). The list is
merged complete into the [bibliography](/bibliography.md), with `citedby`
this slug. No DOIs or arXiv identifiers are printed. Two works share first
author and year: [1] (Akrivis 2015) is keyed `akrivis-2015` and [5] (Akrivis
& Lubich 2015) `akrivis-2015-b`, in printed order. No printed duplicates;
all items parsed.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [A-, L-, A(α)- and algebraic stability](/properties/a-stability.md)
* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [Dahlquist's order barrier for A-stable multistep methods](/results/dahlquist-second-barrier.md)
* [Energy stability of the six-step BDF method](/results/bdf6-energy-stability.md)
* [G-stability](/properties/g-stability.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Multiplier energy technique for multistep methods (Nevanlinna–Odeh multipliers)](/methods/multiplier-energy-technique.md)
