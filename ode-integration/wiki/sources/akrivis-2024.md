---
type: Source
title: "Akrivis et al. (2024) — The variable two-step BDF method for parabolic equations"
description: "Proves energy stability of variable-step BDF2 for self-adjoint parabolic problems whenever adjacent step ratios stay below about 1.9398, improving the earlier bounds 1.8685 and 1.9104, by testing with two multipliers and bounding the summed elliptic terms through a Grenander–Szegő-type lemma for non-Toeplitz matrices."
resource: "doi:10.1007/s10543-024-01007-y"
source_kind: paper
authors: [Akrivis G., Chen M., Han J., Yu F., Zhang Z.]
year: 2024
venue: "BIT Numer. Math. 64:14"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_BIT_Numerical_Mathematics_Akrivis_The_variable_two-step_BDF_method_for_parabolic_equations.pdf"
tags: [linear-multistep, bdf, energy-method, stability, step-size-control, parabolic]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper analyses the variable-step two-step
[backward differentiation formula](/methods/backward-differentiation-formula.md)
(BDF2) for the linear parabolic problem $y'=Ly+g(t)$, with $-L$ positive
definite and self-adjoint on a Hilbert space. On a nonuniform grid,
stability is governed by the adjacent step ratios $r_n$.
[Zero-stability](/definitions/zero-stability.md) holds for $r_n<1+\sqrt2$,
and that bound is sharp. Energy-technique stability estimates for
parabolic problems were known only for smaller ratio bounds: $1.366$
(Grigorieff), $1.8685$ (Becker 1998) and $1.9104$ (Emmrich 2005). All three
test the scheme with one multiplier and bound each elliptic term separately.

The contribution is a [multiplier energy technique](/methods/multiplier-energy-technique.md)
with two multipliers: the scheme is tested with $y_n-\mu_1y_{n-1}-\mu_2y_{n-2}$,
$0<\mu_1<1$, $-1<\mu_2<0$, and the sum of the elliptic terms is bounded from
below in one go. That sum is a quadratic form with a banded
lower-triangular matrix that is neither Toeplitz nor diagonally dominant.
Lemma 2.1, presented as a variant of the Grenander–Szegő theorem for
non-Toeplitz matrices, gives a necessary and sufficient condition for its
uniform positive definiteness: a quadratic polynomial must stay positive
on $[-1,1]$. The difference-quotient terms telescope under a second ratio
condition.

Optimizing the two conditions over $(\mu_1,\mu_2)$ reduces to a quintic
equation and gives $\mu_1^\star\approx0.9672$, $\mu_2^\star\approx-0.1793$ and
the ratio bound $r^\star\approx1.9398$. Theorem 1.1 proves the
[stability of variable-step BDF2](/results/variable-step-bdf2-stability.md)
for $r_n\le r^\star$, with a growth factor $e^{c\Gamma_n}$ in the
variation of the ratios. The bound constrains adaptive BDF2
[step-size sequences](/methods/step-size-control.md); graded meshes
satisfy it except for finitely many steps. Within the same framework,
Emmrich's $1.9104$ is optimal for a single multiplier. Everything is
proved; there are no numerical experiments.

# Version read

The file is the version of record (Springer, open access, CC BY 4.0),
21 pages, all read, with visual checks of the pages whose equations the
text extraction garbled. Received 31 July 2023, published online 1 March
2024; article number 14 of vol. 64. Title, authors, volume and DOI on page
1 match Crossref. No identity problem.

# Key claims

The source indexes steps by their end point, $k_n=t_n-t_{n-1}$, so its
ratio $r_n=k_n/k_{n-1}$ is the registry ratio of the step ending at $t_n$;
the claims below keep that indexing.

1. Variable-step BDF2 for $y'=Ly+g(t)$ is stable in the sense of Eq. 1.4 whenever all adjacent step ratios satisfy $r_n\le r^\star\approx1.9398$; the constants $C$, $c$ are independent of $T$, $L$, $g$ and the partition (Thm. 1.1, Eqs. 1.3–1.5). **Proved**
2. The stability constant carries $e^{c\Gamma_n}$ with $\Gamma_n=\sum_{j=2}^{n-2}[r_j-r_{j+2}]_+$; $\Gamma_n=0$ for nondecreasing ratios, $\Gamma_n=r_2+r_3-r_{n-1}-r_n$ for decreasing ones, and $\Gamma_n$ is bounded when the number of monotonicity changes of $(r_n)$ is bounded uniformly in $N$ (§1.1). **Stated**
3. On graded meshes $t_i=(i/N)^a$, $a>1$, the ratios decrease to 1, so $r_i\le r^\star$ except for finitely many $i$ (§1.1). **Stated**
4. Zero-stability of variable-step BDF2 holds for ratios below $1+\sqrt2\approx2.414$, and this bound is sharp (§1.3, citing Crouzeix–Lisbona, Grigorieff and Hairer–Nørsett–Wanner). **Stated**
5. Earlier parabolic stability bounds: Grigorieff $(1+\sqrt3)/2\approx1.366$, independent of $\Gamma_n$; Becker $(2+\sqrt{13})/3\approx1.8685$; Emmrich $1.9104$ for semilinear problems (§1.3, Abstract). **Stated**
6. Liao and Zhang (2021) and the works cited there prove estimates of a different kind, with $(y_1-y_0)/k_1$ on the right-hand side, for ratio bounds well above $1+\sqrt2$ (§1.3). **Stated**
7. The BDF2 difference quotient can be written $D_2v^n=\frac1{\omega_nk_n}(\Delta_1v^n-\psi_n\Delta_2v^n)$ with $\Delta_jv^n=v^n-v^{n-j}$, $\omega_n=1/(1+r_n)$ and $\psi_n=(r_n/(1+r_n))^2$ (Eq. 1.6). **Derived**
8. Lemma 2.1: for $\mu_2\le0$, $(\mathbb L(r_2,\dots,r_n)x,x)\ge c\lVert x\rVert_2^2$ for all matrices of the form (2.1) with $0<r_i\le r$ and all $n\ge4$ if and only if $\mathfrak p(x)=\frac1{1+r}\big[1+\mu_2r-\mu_1\sqrt r\,x-2\mu_2rx^2\big]\ge c$ for all $x\in[-1,1]$ (Lemma 2.1, Eqs. 2.1–2.3). **Proved**
9. Necessity follows from the Grenander–Szegő theorem at constant ratio: the symmetric part of $\mathbb L(r,\dots,r)$ is a pentadiagonal Toeplitz matrix with symbol $\frac1{1+r}(1-\mu_1\sqrt r\cos x-\mu_2r\cos2x)$, whose minimum equals $\min_{[-1,1]}\mathfrak p$ (§2, Thm. 2.1). **Proved**
10. Lemma 3.2: if $0<\mu_1<1$, $-1<\mu_2<0$, $2-\mu_1+2\mu_2\ge0$, $1+\mu_1+3\mu_2\ge0$ and $r_j\le r\le r^\star(\mu_1,\mu_2):=\frac{\sqrt{1+\mu_1+3\mu_2}}{2\sqrt{1+\mu_2}-\sqrt{1+\mu_1+3\mu_2}}$, the telescoped lower bound (3.2) on the summed difference-quotient terms holds (Lemma 3.2, Eqs. 3.1–3.2). **Proved**
11. $\sup r^\star(\mu_1,\mu_2)=r^\star(1,0)=1+\sqrt2$, the optimal zero-stability bound (footnote 1, p. 9). **Derived**
12. Lemma 3.3: with $\mu_1=0.9672$, $\mu_2=-0.1793$ and $r_j\le r^\star(0.9672,-0.1793)\approx1.9398$, half the summed elliptic terms is at least $c_1\sum_jk_j\lVert y_j\rVert_L^2$ minus three starting-value terms, with $c_1=10^{-6}$ (Lemma 3.3, Eq. 3.9). **Proved**
13. At these multipliers the minimum of $\mathfrak p$ on $[-1,1]$ is attained at $x^\star=-\mu_1/(4\mu_2\sqrt{r^\star})\in(0,1)$, and the paper prints $\mathfrak p(x^\star)\approx7.3592\cdot10^{-6}>c_1$ (proof of Lemma 3.3, p. 12). **Proved** (see Printed slips)
14. Remark 3.1: within this positive-definiteness framework, Emmrich's bound $1.9104$ is optimal for a single multiplier, attained at $\mu_1=0.72349$, $\mu_2=0$. **Derived**
15. On the domain $0<\mu_1<2$, $-1<\mu_2<0$, $1+\mu_1+3\mu_2\ge0$, positivity of $\mathfrak p$ holds iff $r<\bar r(\mu_1,\mu_2)$, with $\bar r=-\frac1{\mu_2}-\frac{\mu_1^2}{8\mu_2^2}$ where $\frac3{16}\mu_1^2\le-\mu_2$ and $\bar r=\big(2/(\mu_1+\sqrt{\mu_1^2+4\mu_2})\big)^2$ otherwise (§4, Eq. 4.3). **Proved**
16. The optimal ratio bound is $\max_{\vartheta\ge1/3}\min\{H(\vartheta),\tilde G(\vartheta)\}$ along the segments $\mu_2=\vartheta(2-\mu_1)-1$, with $H(\vartheta)=\frac{\sqrt{3\vartheta-1}}{2\sqrt\vartheta-\sqrt{3\vartheta-1}}$ increasing and $\tilde G(\vartheta)=\frac1{1-2\vartheta}$ on $[1/3,1/2)$, $\frac12+\frac1{2(2\vartheta-1)^2}$ on $(1/2,\infty)$ (Eqs. 4.7–4.9, 4.16, Fig. 2). **Proved**
17. The crossing $H=\tilde G$ reduces to $23\vartheta^5-55\vartheta^4+55\vartheta^3-29\vartheta^2+8\vartheta-1=0$, whose only real root $\vartheta\approx0.794645365827$ gives $\mu_1^\star\approx0.967237837020572$, $\mu_2^\star\approx-0.179320334471962$ and $r^\star\approx1.9398285699451$ (Eq. 4.17). **Derived** (the compiler reproduced the root and the three values (not in the sources))
18. The optimal multipliers satisfy all hypotheses of the analysis, in particular $2-\mu_1^\star+2\mu_2^\star\ge0$, which the optimization domain does not build in (§4). **Stated**
19. Within the two-multiplier, summed-elliptic-term approach, $\approx1.9398$ is the best obtainable ratio bound (§4). **Derived**
20. Arbitrary starting values $y_0,y_1$ in the energy space are allowed; the estimate needs $\lVert y_0\rVert^2+\lVert y_1\rVert^2+k_2\lVert y_0\rVert_L^2+k_2\lVert y_1\rVert_L^2$ on the right-hand side (Thm. 1.1). **Proved**

The paper does not claim that $1.9398$ is sharp for parabolic stability,
and $1+\sqrt2$ bounds a different property (zero-stability); the Liao–Zhang
bounds concern a different estimate. The three numbers are not competing
values of one quantity.

# Printed slips

- Proof of Lemma 3.3 (p. 12): "$p(y^\star)\approx7.3592\cdot10^{-6}>c_1$" is the value at the rounded $r=1.9398$; at the hypothesis bound $r=r^\star(0.9672,-0.1793)=1.939804\ldots$ it is about $7.107\cdot10^{-6}$ *(compiler check, not in the sources)*. Harmless, since both exceed $c_1=10^{-6}$.
- Lemma 3.2 requires $-1<\eta<0$ strictly, yet Remark 3.1 applies "the proof" with $\eta=0$.
- §4 defines the domain with $0<\delta<2$, while Lemma 3.2 assumes $0<\delta<1$; the a-posteriori admissibility check names only $2-\delta^\star+2\eta^\star\ge0$, although $\delta^\star<1$ is also needed (it holds).
- p. 13: "we are lead to the inequality" (for "led").

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$ | $y$, $y_n$ | superscript step index |
| $A$, $u'+Au=f$ | $-L$, $y'=Ly+g(t)$ | positive definite self-adjoint; **collision** with the Butcher matrix; the forcing $f$ is written $g$ (**collision** with the registry right-hand side $f$) |
| $(\cdot,\cdot)$, $\lvert\cdot\rvert$ | $\langle\cdot,\cdot\rangle$, $\lVert\cdot\rVert$ | Hilbert space inner product and norm |
| $\lVert v\rVert=\lvert A^{1/2}v\rvert$, $\langle\cdot,\cdot\rangle$ | $\lVert v\rVert_L=\lVert(-L)^{1/2}v\rVert$ (page-local, as on the result pages), — | energy norm and inner product; **collision**: the source's $\langle\cdot,\cdot\rangle$ and $\lVert\cdot\rVert$ are the energy ones |
| $\lVert\cdot\rVert_\star$ | $\lVert\cdot\rVert_{L,\star}$ | dual norm |
| $k_n=t_n-t_{n-1}$ | $h_{n-1}$ | step indexed by its end point; **collision** with the registry step count $k$ |
| $r_n=k_n/k_{n-1}$ | $r_{n-1}=h_{n-1}/h_{n-2}$ | same ratio, index shifted by one |
| $r$, $r^\star$ | — | uniform ratio bound; $r^\star$ is both the function $r^\star(\delta,\eta)$ and the number $\approx1.9398$ |
| $\delta$, $\eta$ | $\mu_1$, $\mu_2$ | multipliers of the test function $u^n-\delta u^{n-1}-\eta u^{n-2}$; registry translates $\eta$ |
| $\delta_kv^n=v^n-v^{n-k}$ | $\Delta_kv^n$ | backward difference, renamed to avoid the multiplier $\delta$ |
| $D_2$ | $D_2$ | variable-step BDF2 difference quotient |
| $\omega_n$, $\psi_n$ | $\omega_n$, $\psi_n$ | $1/(1+r_n)$ and $(r_n/(1+r_n))^2$ |
| $\Gamma_n$ | $\Gamma_n$ | ratio-variation quantity; distinct from the MRI coupling matrices $\Gamma^{(k)}$ |
| $\mathscr D_n$, $\mathscr A_n$, $\mathscr F_n$ | — | difference-quotient, elliptic and forcing terms of the tested equation |
| $\mathbb L(r_2,\dots,r_n)$, $L$ | — | scaled and unscaled lower-triangular banded matrices; the source's $L$ is a **collision** with the registry linear operator |
| $p(y)$, $P(y)=(1+r)p(y)$ | $\mathfrak p(x)$, $(1+r)\mathfrak p(x)$ (page-local) | quadratic positivity polynomial; **collision**: $p$ is the order, $y$ the solution; not the registry Patankar weight $\varpi_i$ |
| $g(x)$ | — | Toeplitz symbol |
| $J,G,K,P,Z,Z_s,M$ | — | auxiliary matrices of the proof of Lemma 2.1; $G$ and $M$ **collide** with the G-norm matrix and the mass matrix |
| $c_1$ | $c_1$ | coercivity constant $10^{-6}$, not an abscissa |
| $D$, $D_1$, $D_2$ | — | multiplier domains of §4; $D_2$ is also the difference quotient |
| $h(\delta,\eta)$ | $\bar r(\mu_1,\mu_2)$ | positivity ratio bound; **collision** with the step $h$ |
| $t$, $L_t$, $H(t)$, $G(t)$ | $\vartheta$, —, $H(\vartheta)$, $\tilde G(\vartheta)$ | optimization parameter and functions; **collision**: $t$ is time |
| $\alpha$ (graded mesh exponent) | $a$ | **collision** with the multistep coefficients |

# Reference list

The paper prints 12 references in numbered style ([1]–[12]), ordered
alphabetically. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. Ref. [1] is the
ingested [Akrivis et al. (2021)](/sources/akrivis-2021.md). Ref. [8] is a
NUMDIFF-5 proceedings chapter (Teubner 1991); ref. [9] a TU Berlin preprint
(Preprint 426/1995); refs. [6], [10] and [12] are books. DOIs are printed for
[1]–[5], [7] and [11]. Ref. [3] (Calvo & Grigorieff 2002, variable 3-step
BDF) is `calvo-2002-b`, because the bibliography already held a different
Calvo 2002 work under the plain key. No printed duplicates; all items parsed.

# Pages created or updated

Chunk 3 (2026-10-19). This source is cited on:

* [Backward differentiation formulas (BDF)](/methods/backward-differentiation-formula.md)
* [G-stability](/properties/g-stability.md)
* [Linear multistep methods](/methods/linear-multistep-method.md)
* [Multiplier energy technique for multistep methods (Nevanlinna–Odeh multipliers)](/methods/multiplier-energy-technique.md)
* [Stability of variable-step BDF2 under step-ratio bounds](/results/variable-step-bdf2-stability.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Zero-stability](/definitions/zero-stability.md)
