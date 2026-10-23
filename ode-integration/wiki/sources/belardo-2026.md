---
type: Source
title: "Belardo et al. (2026) — On the construction of nested explicit Runge–Kutta methods via null rules"
description: "Short note showing that all embedded weight vectors of order at least p that share the stages of an explicit Runge–Kutta method form an affine family along the null space of the order-condition matrix, and using it to build alternative embeddings for midpoint, RK4, DOPRI5(4), a weak-stage-order scheme and Bogacki–Shampine 3(2)."
resource: "doi:10.1016/j.jcp.2026.115061"
source_kind: paper
authors: [Belardo M.R., Calabrò F., Izzo G., Messina E., Veneroso V.]
year: 2026
venue: "J. Comput. Phys. 563:115061"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_ESAIM_Mathematical_Modelling_and_Numerical_Analysis_Izgin_On_Lyapunov_stability_of_positive_and_conservative_time_inte.pdf"
tags: [runge-kutta, explicit, embedded-pair, step-size-control, order-conditions]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The note starts from one observation: the difference between the weights
of two nested explicit Runge–Kutta methods, the vector used for error
estimation in an [embedded pair](/methods/embedded-runge-kutta-pair.md),
lies in the null space of the order conditions both satisfy. Borrowing the
quadrature term of Lyness (1965), such a vector is a *null rule*. With $A$
and $c$ fixed, the [order conditions](/results/runge-kutta-order-conditions.md)
up to order $p$ are linear in the weights, $G_pb=r_p$, so every vector of
$\ker G_p$ can be added to $b$ without losing order $p$: all embeddings of
order $\ge p$ that reuse the stages form the affine family
$\hat b=b+Z_pk$, with $Z_p$ an orthonormal basis of $\ker G_p$. No such
embedding exists when $G_p$ has full column rank, which is how the note
reads the classical fact that a four-stage fourth-order method has no
third-order embedding.

The free parameter is chosen by the real stability interval $\rho(k)$ of
the embedded formula, computed from its
[stability function](/definitions/stability-function.md), with the caveat
that $\rho$ alone does not decide, since $k$ also changes the quality of
the error estimator. The construction is applied to five schemes: explicit
midpoint (order-1 embedding), classical RK4 (two order-2 directions,
positive-weight tableaux), DOPRI5(4), where $\dim\ker G_4=1$ so the
standard embedding is one member of a one-parameter family and a new
order-4 embedding with a wider interval is printed, the (5,3,3)
weak-stage-order scheme of [Biswas et al. (2025)](/sources/biswas-2025.md),
and Bogacki–Shampine 3(2). In the last case the main method is fixed and
only the estimator changes: on a stiff scalar problem with an
ode23tx-type [step-size controller](/methods/step-size-control.md), an
alternative estimator at the same distance from $b$ as the standard one
cuts accepted steps by 11% and 9% at no loss of final accuracy, while its
$\rho$ is smaller than the standard one's, so $\rho$ does not predict the
step count. Everything is by direct construction and numerical tables;
there are no theorems.

# Version read

Version of record: J. Comput. Phys. 563 (2026) 115061, an Elsevier
"Short note" of 7 pages, received 14 November 2025, revised 8 April 2026,
accepted 22 May 2026, online 26 May 2026; the DOI is printed on page 1.
Pages 2–5 were also read as images, since the tableaux of Figs. 1–3 and 5
and the fractions of Table 1 are garbled in text extraction. **Identity:**
the archive filename is wrong: it names Izgin (2022, ESAIM: M2AN), "On
Lyapunov stability of positive and conservative time integrators", but the
file holds this paper; page 1 (title, five authors, journal, article
number, DOI) decides the identity. An automated Crossref lookup on the
title had matched an SSRN preprint record (10.2139/ssrn.5798402), which is
not the version read and not used here.

# Key claims

Registry notation: $(A,b,c)$ the explicit tableau with $c=A\mathbf 1$,
$\hat b$ embedded weights, $s$ stages, $p$ classical order, $R(z)$ the
stability function with $z=h\lambda$, $\mathrm{err}_n$, $\mathrm{atol}$,
$\mathrm{rtol}$ as in step-size control. Page-local: $G_p\in\mathbb
R^{n_p\times s}$ the order-condition matrix up to order $p$ (the source's
$\boldsymbol\Phi_p$), $r_p$ its right-hand side, $Z_p$ an orthonormal basis
of $\ker G_p$, $k$ the family parameter, $\rho(k)$ the real stability
interval $[-\rho,0]\subset\mathcal S$ of the embedded formula.

1. The difference between the weights of two nested explicit methods lies
   in the null space of the order conditions, a "null rule" in the
   quadrature sense (§1). **Stated** (elementary, explained in §2)
2. If $b$ satisfies the conditions to order $p$ for fixed $(A,c)$ and
   $N\in\ker G_p\setminus\{0\}$, then $(A,b+kN,c)$ satisfies them for every
   $k\in\mathbb R$ (§2–3, Eqs. 1–2). **Derived**
3. The construction is impossible when $G_p$ determines $b$ uniquely (full
   column rank) and is also limited by "the well-known Butcher barriers"
   (§2). **Stated**
4. There are 17 conditions for $p=5$, growing exponentially with $p$;
   Table 1 lists the $n_4=8$ conditions for $p\le4$ (§2). **Stated**
5. Stability regions vary continuously with $k$, $k=0$ being the original
   method; choosing $k$ by $\rho$ alone is insufficient, since error
   estimation, step counts and final accuracy depend on $k$, "especially
   on stiff problems" (§3). **Stated** (backed by claim 15)
6. A four-stage fourth-order method cannot be nested with a third-order
   embedding (citing Hairer–Nørsett–Wanner I); in this framework $G_3$ has
   full rank for every such method (§3). **Stated** (rank asserted, not
   proved)
7. Explicit midpoint: the only embedding has order 1, null rule
   $\tfrac1{\sqrt2}(1,-1)^\top$, nonnegative weights for
   $k\in[0,\sqrt2]$; no order-2 embedding exists (§4, Fig. 1). **Derived**
8. Midpoint: $\rho=2$ for the original method, and "the maximum real
   stability interval is 7", reached at $k=1$ with
   $\hat b=(1/\sqrt2,1-1/\sqrt2)$ (§4, Fig. 1). **Shown** (see slips)
9. Classical RK4: $G_4$ and $G_3$ have full rank, $\dim\ker G_2=2$; two
   positive-weight order-2 embeddings are printed at the $k$ maximizing
   $\rho$ (§4, Fig. 2). **Shown**
10. RK4 has $\rho\approx2.8$; the maxima of $\rho(k)$ along the two
    directions are about 5.2 and 6 (§4, Fig. 2c). **Shown** (read from the
    plot)
11. DOPRI5(4): $\dim\ker G_4=1$, so every order-4 embedding with the fixed
    $(A,c)$ is $b+kZ_4$, the standard Dormand–Prince $\hat b$ being one
    member (§4). **Derived**
12. Along this family $\rho(k)$ peaks beyond the standard member, and the
    peak gives a new order-4 embedding $b^\star$ with a wider interval
    (Fig. 3; Fig. 4b shows about 6.6 against 3.3 near $k=0$). **Shown**
13. DOPRI5(4): order-3 embeddings come from three null-rule directions,
    with $\rho$ peaks around 4.5–5 (§4, Fig. 4a). **Shown**
14. The (5,3,3) scheme of [19]: $\dim\ker G_3=1$ with a printed generator,
    $\dim\ker G_2=3$, and only the third order-2 family admits
    nonnegative weights over a nonempty range; that tableau is printed
    (§4, Fig. 5). **Shown**
15. Bogacki–Shampine 3(2) on $y'=-a(y-\cos t)$, $a=50$, $T=10$,
    $\mathrm{rtol}=10^{-6}$, $\mathrm{atol}=10^{-9}$: the standard estimator
    takes 906 accepted steps with final error $3.3050\times10^{-6}$ and
    $\rho=3.1523$; the selected $\theta^\ast$ takes 804 steps with
    $3.2060\times10^{-6}$ and $\rho=2.4100$ (Table 2). **Shown**
16. Same with $a=200$: 1874 steps and $1.2975\times10^{-6}$ for the
    standard estimator, 1709 steps and $1.2925\times10^{-6}$ with
    $\rho=2.9318$ for $\theta^\ast$ (Table 3). **Shown**
17. Other estimators at the same distance need far more steps (1442–1488
    at $a=50$, 2334–2492 at $a=200$) but give smaller final errors; the
    direction $\theta=\pi/2$ takes 977 and 1302 steps, but at $a=200$ its
    error exceeds the standard one's (Tables 2–3). **Shown**
18. The best estimator depends on the stiffness: $(k_1,k_2)$ differs
    between $a=50$ and $a=200$ (Tables 2–3). **Shown**
19. The largest $\rho$ on the fixed-distance circle (3.1833) does not
    minimize the step count, and the step-minimizing estimator has smaller
    $\rho$ than the standard one (Tables 2–3). **Shown** (compiler inference from the tables, not in the sources; the paper states the general caveat of
    claim 5)
20. Null-rule embeddings can serve stiffness detection, giving a
    lower-order formula with a possibly much larger real stability interval
    at "essentially no additional computational cost" (§1). **Stated** (not
    demonstrated)
21. The framework applies when a built-in embedding exists: lower-order
    embeddings solve the reduced system and varying $k$ explores the family
    (§4, DOPRI). **Stated**

*(Compiler note, not in the source.)* The selection of $\theta^\ast$ is
in-sample (minimum steps on the same problem, using the exact solution),
and DOPRI5(4) propagates the order-5 solution, so the stability of the
embedded order-4 formula does not govern the stability of the integration;
$b^\star$ is a different error estimator, not a more stable integrator.
*(Compiler checks, not in the sources.)* $b^\star$ satisfies order 4 to $10^{-6}$ with
$\rho\approx5.80$, against 4.385 for the standard embedding and 3.307 for
the order-5 weights; the standard Bogacki–Shampine estimator has
$\rho=3.1524$ and lies at distance 0.199343 from $b$, as the tables use.

# Printed slips

- §4, midpoint: "the maximum real stability interval is 7 … at $k=1$,
  where $\rho$ attains its maximum". With
  $\hat b=(k/\sqrt2,1-k/\sqrt2)$, $R(z)=1+z+\tfrac12(1-k/\sqrt2)z^2$, so
  $\rho(1)\approx6.83$ and the supremum $\rho=8$ is at
  $k=3\sqrt2/4\approx1.061$; "7" and "$k=1$" are plot readings.
- Fig. 2b (RK4, second direction): the fourth column of $b$ and $\hat b$
  is hidden behind Fig. 2c, and the visible weights
  $(543/1696,917/2987,223/3387)$ are inconsistent with order 2, which
  forces $\hat b_2+\hat b_3=1-2\hat b_1$ (0.3597, printed sum 0.3728).
- Fig. 5a: the text says the tableau is given "at a value of $k$ where
  $\rho(k)$ is maximal", but the printed $\hat b$ gives $\rho\approx2.28$,
  below the base method's 2.51 and the plotted peaks near 6; it is
  presumably the maximum over the nonnegative-weight range. Fig. 2a
  ($\rho\approx4.59$ against a plotted peak near 5.2) is similar.
- Controller: $h_{n+1}=h_n\min\big(5,0.8(\mathrm{rtol}/\mathrm{err}_n)^{1/3}\big)$
  applies $\mathrm{rtol}/\mathrm{err}_n$ to an $\mathrm{err}_n$ already
  normalized by $\mathrm{atol}+\mathrm{rtol}\max\lvert y\rvert$, which
  targets $\mathrm{err}_n\approx0.8^3\,\mathrm{rtol}$; either a
  transcription slip or an unusually conservative controller. It affects
  the absolute step counts, not the comparison.
- "three independent directions (see Fig. 5b)" and the positive-weights
  tableau "see Fig. 5b": the tableau is Fig. 5a.
- Ref. [21] prints "G. Wanner, E. Hairer, Solving Ordinary Differential
  Equations II, vol. 375" (author order reversed; "vol. 375" spurious);
  ref. [20] prints "E. Hairer, G. Wanner, S.P. Nørsett" (book order:
  Hairer, Nørsett, Wanner).
- Typo: "corrisponding" (§4).

# Notation map

| Belardo et al. (2026) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $(\mathbf A,\mathbf b,\mathbf c)$ | $(A,b,c)$ | bold in the source |
| $\mathbf e$ | $\mathbf 1$ | vector of ones; $\mathbf A\mathbf e=\mathbf c$ assumed |
| $\mathbf D_{\mathbf c}$ | $\mathrm{diag}(c)$ | |
| **$q$** | $p$ of the base method | **collision with the stage order $q$**: the source's $q$ is the classical order of the base method |
| $p$ | $p$ (of the embedding) | the order of the condition set |
| **$\boldsymbol\Phi_p$** | $G_p$ (page-local) | **collision with the elementary weight $\Phi(\tau)$**: order-condition matrix, $n_p\times s$ |
| $\mathbf r_p$, $n_p$ | $r_p$, $n_p$ (page-local) | right-hand sides and their number |
| $\mathbf N$, $\mathbf Z_p$, "Null Rule$_p$ #$j$" | $N$, $Z_p$ (page-local) | null rule and orthonormal kernel basis (column $j$) |
| $\mathbf b^{(k)}$, $\hat{\mathbf b}$, $\mathbf b^\star$ | $\hat b$ | embedded weights; $b^\star$ the new DOPRI embedding |
| $R(z;k)=\det(\mathbf I-z\mathbf A+z\mathbf e\mathbf b^{(k)\top})$ | $R(z)$ | stability function of the embedded formula; $z=h\lambda$ implied |
| $S(k)$ | $\mathcal S$ | stability region |
| $\rho(k)$, $\rho(\theta)$ | — | real stability interval from 0 |
| $\theta$, $\theta_{\rm ref}$, $\theta^\ast$ | — | angle in null-space coordinates at fixed radius 0.19934 |
| $a$ | — | stiffness parameter of $y'=-a(y-\cos t)$; plays the role of $-\lambda$ |
| $h_n$, $y_{n+1}$, $\hat y_{n+1}$, $\mathrm{err}_n$, rtol, atol | $h_n$, $y_{n+1}$, $\hat y_{n+1}$, $\mathrm{err}_n$, $\mathrm{rtol}$, $\mathrm{atol}$ | agrees |

# Reference list

The paper prints 22 references, numbered [1]–[22]. All 22 are merged
complete into the [bibliography](/bibliography.md) with `citedby`
belardo-2026. Refs. [12] and [19] are the ingested sources
[Ranocha et al. (2022)](/sources/ranocha-2022.md) and
[Biswas et al. (2025)](/sources/biswas-2025.md). Ref. [21] (Hairer–Wanner
II) is printed with reversed author order and a spurious "vol. 375"; it
is merged into the Hairer–Wanner II entry `hairer-1996`. Ref. [20] prints the Hairer–Nørsett–Wanner authors out
of order. Ref. [16] prints "S.H. Nasab" (Hedayati Nasab). Refs. [1]–[3]
print the first author as "G.Y. Kulikov" and "G.-Y. Kulikov". No printed
duplicates or unparseable items.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Runge–Kutta order conditions and simplifying assumptions](/results/runge-kutta-order-conditions.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
