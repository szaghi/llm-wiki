---
type: Source
title: "Carrel et al. (2023) — Low-rank Parareal: a low-rank parallel-in-time integrator"
description: "Builds a Parareal iteration for matrix ODEs whose coarse and fine propagators are dynamical low-rank flows of low and high rank, proves linear and superlinear convergence bounds for affine dissipative vector fields up to a truncation-driven stagnation level, and shows rank-independent convergence on Lyapunov, parametric heat and Riccati problems."
resource: "doi:10.1007/s10543-023-00953-3"
source_kind: paper
authors: [Carrel B., Gander M.J., Vandereycken B.]
year: 2023
venue: "BIT Numer. Math. 63:13"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_BIT_Numerical_Mathematics_Carrel_Low-rank_Parareal_a_low-rank_parallel-in-time_integrator.pdf"
tags: [parallel, parareal, low-rank, parabolic, stiff]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper combines [Parareal](/methods/parareal.md) with dynamical
low-rank approximation (DLRA, Koch & Lubich 2007) for matrix ODEs
$y'=f(y)$, $y\in\mathbb R^{m\times m}$. The coarse and fine propagators
differ in **rank**, not in step size or order: the coarse propagator
$\mathcal G$ truncates to rank $q$ and follows the DLRA flow at
that rank, the fine propagator $\mathcal F$ does the same at a larger rank
$r$ (possibly full rank, i.e. the exact flow). DLRA integrators cost at
least $O(mr^2+r^3)$ per step, so the coarse solve is much cheaper. The
iterates keep rank at most $r+2q$. Small random
perturbations in the first coarse sweep make the rank exactly that, so the
iteration runs on the right manifold. The paper places this among the
families of [parallel-in-time integration](/methods/parallel-in-time-integration.md)
and claims it is the first parallel-in-time integrator for DLRA.

For affine autonomous fields $f(y)=\mathcal A(y)+B$ with one-sided Lipschitz
constant $\ell<0$, an energy and Grönwall argument gives the error
recursion $E^{(k+1)}_{j+1}\le\alpha E^{(k)}_j+\beta E^{(k+1)}_j+\chi$. Here $\alpha$ and $\beta$
carry $e^{\ell\Delta T}$ times the Lipschitz constants of the SVD truncations. The
recursion is solved exactly by generating functions, extending Gander &
Hairer (2008) with a constant $\chi$. Three bounds follow, two linear
and one superlinear, valid for $\alpha+\beta<1$ down to a stagnation level
$\chi/(1-\alpha-\beta)$. For dissipative problems a large slice length
$\Delta T$ makes $\alpha$ and $\beta$ small, so convergence is faster with big slices. A
side result proves low-rank approximability of the differential Lyapunov
solution. The DLRA solver in every test is the projector-splitting
integrator of Lubich & Oseledets (2014), a splitting of the tangent-space
projector ([operator splitting](/methods/operator-splitting.md)). Tests on the differential Lyapunov
equation (2D heat), a parametric heat problem and a nonlinear
differential Riccati equation show linear-then-superlinear convergence
that does not depend on the ranks or the problem size. A
tolerance-based, rank-adaptive variant works as intended. No parallel run
or timing is reported.

# Version read

arXiv:2203.08455v2 [math.NA], stamped 13 September 2022 (title page dated
September 5, 2022), 20 pages, all read. This is not the BIT version of
record, although the archive filename says "Crossref_BIT". Title and
authors match the published version, and the file prints no DOI. Equation,
theorem and figure numbers are those of arXiv v2.

# Key claims

Registry notation: Parareal slices $T_j$ of length $\Delta T$ (source $h$,
with slice index $n$), iterate $U^{(k)}_j$ (source $Y^k_n$), propagators
$\mathcal F$, $\mathcal G$, vector field $f$ (source $F$). Page-local:
matrix size $m$, fine and coarse ranks $r$, $q$
(as in the source; **$q$ is not the stage order here**), DLRA flow $\psi_r$ at rank $r$, SVD truncation
$\mathcal T_r$, error $E^{(k)}_j=\lVert y(T_j)-U^{(k)}_j\rVert$ in the
Frobenius norm, one-sided Lipschitz constant $\ell$, DLRA modelling error
$\epsilon_r$, and the recursion constants $\alpha,\beta,\gamma,\chi$ (source $\kappa$), as on [Parareal](/methods/parareal.md). The
Notation map lists the collisions.

1. Low-rank Parareal is, as far as the authors know, the first
   parallel-in-time integrator for low-rank approximations and DLRA (§2.3,
   §5). **Stated**
2. Classical Parareal terminates after $k=j$ iterations at $T_j$. It works
   well on parabolic problems and worse on hyperbolic ones (§2.1, citing
   Gander & Vandewalle 2007). **Stated**
3. The iterates have rank at most $r+2q$ for every $j,k$. The
   perturbations $\mathcal E_j$ keep the rank between $r$ and
   $r+2q$ and affect only the initial error, not
   convergence (§3, after Def. 3.1). **Derived**
4. Most DLRA integrators cost at least $O(mr^2+r^3)$ flops per step, which
   is why a low-rank coarse solver pays off (§3, footnote 1). **Stated**
5. Lemma 3.2: for affine $f$ (Assumptions 1–2),
   $E^{(k+1)}_{j+1}\le e^{\ell\Delta T}C_{r,q}E^{(k)}_j+e^{\ell\Delta T}C_qE^{(k+1)}_j+e^{\ell\Delta T}\max_j\lVert y(T_j)-\mathcal T_r(y(T_j))\rVert+(2\varepsilon_{q}+\varepsilon_{r})\int_0^{\Delta T}e^{\ell(\Delta T-s)}ds$
   (Eq. (11)), with $C_q$, $C_{r,q}$ the Lipschitz constants of
   $\mathcal T_q$ and $\mathcal T_r-\mathcal T_q$. **Proved**
6. Affinity of $f$ is used in one step only, so the analysis may extend to
   some nonlinear fields (§5). **Stated**
7. Theorem 3.3 (linear convergence): if $\alpha+\beta<1$, then
   $\max_jE^{(k)}_j\le\bigl(\alpha/(1-\beta)\bigr)^k\max_jE^{(0)}_j+\chi/(1-\alpha-\beta)$ (Eq. (17)),
   with $\alpha=e^{\ell\Delta T}C_{r,q}$, $\beta=e^{\ell\Delta T}C_q$ and
   $\chi$ the last two terms of claim 5. **Proved**
8. Lemma 3.4: the equality version of the double recursion has a closed
   form by generating functions (Eq. (19)). It generalizes Gander &
   Hairer (2008, Thm 1) by the $\chi$ term and by giving equality instead of
   a bound. **Proved**
9. Theorem 3.5 (superlinear convergence):
   $E^{(k)}_j\le\frac{\alpha^k}{(k-1)!}\frac{\prod_{i=2}^k(j-i)}{1-\beta}\max_jE^{(0)}_j+\frac{\chi}{1-\alpha-\beta}$ (Eq. (21)). **Proved**
10. Theorem 3.6:
    $E^{(k)}_j\le\alpha^k(1+\beta)^{j-1}\max_jE^{(0)}_j+\chi/(1-\alpha-\beta)$ (Eq. (22)).
    Remark 3.7 recovers Theorem 3.3 from it. **Proved**
11. No one of the three bounds is uniformly best. They describe different
    phases of the iteration (Fig. 1, a plot of the bounds for four
    $(\alpha,\beta)$ pairs) (§3.2). **Shown**
12. For $\ell<0$, a large enough $\Delta T$ makes $\alpha$ and $\beta$ as
    small as wanted: convergence is faster for big slices on diffusive
    problems (§2.3, §3.2). **Derived**
13. Theorem 3.8: to first order,
    $\lVert\mathcal T_r(Z)-\mathcal T_r(\tilde Z)\rVert\le\frac{\sigma_r}{\sigma_r-\sigma_{r+1}}\lVert Z-\tilde Z\rVert$, and
    $\mathcal T_r-\mathcal T_q$ has the sum of the two gap ratios as constant
    (Eqs. (24)–(25)). The first part is cited from Breiding &
    Vannieuwenhoven (2021) and Feppon & Lermusiaux (2018b). **Proved**
    (second part by the triangle inequality)
14. For singular values $\sigma_i\approx e^{-ci}$ the gap ratio is about
    $1/(1-e^{-c})$, below 1.6 for $c=1$ (Eq. (26)). **Derived**
15. Remark 3.9: experiments need a singular-value gap at the coarse rank but
    not at the fine rank, so bound (25) can probably be improved. **Shown**
16. For the differential Lyapunov operator with symmetric $A_{\mathrm L}$,
    $\ell=2\max_i\lambda_i(A_{\mathrm L})$; for affine $f$ in general
    $\ell=\tfrac12\lambda_{\max}(\mathcal A+\mathcal A^\top)$ (§2.2, §4.1). **Stated**
17. Lemma 4.1: the differential Lyapunov solution has an approximation of
    rank at most $r_0+2r_1\rho$ whose 2-norm error is bounded by
    $e^{\ell t}\sigma_{r_0+1}(y_0)+\frac{e^{\ell t}-1}{\ell}\bigl(4e^{-\pi^2\rho/\log(4\kappa_A)}\lVert CC^\top\rVert_2+\sigma_{r_1+1}(CC^\top)\bigr)$.
    Here the equation is $y'=A_{\mathrm L}y+yA_{\mathrm L}+CC^\top$ with a tall
    $C$, $\kappa_A$ is the condition number of $A_{\mathrm L}$, and $r_0$, $r_1$,
    $\rho$ are free rank parameters of the lemma, not the Parareal ranks
    (page-local). The authors found no proof in the literature for the
    differential case. **Proved**
18. The Corollary 4.2 bound beats the Krylov-based bound of Koskela &
    Mena (2020, Thm 4.2), which does not vanish at $t=0$; theirs bounds a
    discrete method (Remark 4.3). **Derived**
19. Lyapunov test ($100\times100$ Laplacian, $T=2$): convergence is linear from
    the coarse-rank to the fine-rank solution. The coarse rank
    $q\in\{2,4,6\}$ changes only the initial error. The fine rank
    $r\in\{12,16,20\}$ does not change the rate but limits the final
    error (§4.1, Fig. 3). **Shown**
20. Lyapunov test: convergence does not depend on the problem size
    ($50$, $100$, $200$) despite stiffness. It is faster for larger
    $\Delta T\in\{0.02,0.04,0.08\}$, as predicted (§4.1, Fig. 4). **Shown**
21. Parametric heat ("cookie") problem, 101 parameters,
    $1580\times1580$ matrices, $T=0.1$: the rate does not depend on the
    ranks; convergence is linear in early iterations and superlinear in late
    ones, as predicted (§4.2, Fig. 6). **Shown**
22. Differential Riccati equation (nonlinear, outside the theory): linear
    convergence for $q=6,8$; for $q=4$ it is "slower (but still
    superlinear)", which the authors attribute to non-constant singular
    gaps (§4.3, Fig. 8). **Shown**
23. Rank-adaptive low-rank Parareal (Def. 4.4) with truncation tolerances
    $10^{-7},10^{-9},10^{-11}$ behaves like fixed fine ranks. After two
    iterations the rank is close to the numerical rank of the exact
    solution and changes little (§4.4, Fig. 9). **Shown**
24. Good speedup is "reasonable to expect" from the large cost gap between
    fine and coarse solvers, but no parallel implementation or timing is
    given (§5). **Stated**
25. Every DLRA solve in the experiments uses the second-order
    projector-splitting integrator (Lubich & Oseledets 2014) with enough
    substeps that coarse and fine solvers count as exact (§4). **Stated**

# Printed slips

- Eq. (34): "$e_i(x)=\sqrt2\cos(2\pi kx)$ and $f_i(x)=\sqrt2\sin(2\pi kx)$,
  $i=1,\ldots,(q-1)/2$". The frequency should be $i$, not $k$, and the
  range $(k-1)/2$ (as in the text above it), not $(q-1)/2$, since $q$ is the
  coarse rank.
- §4.4: "Algorithm 3.1 can be easily reformulated". No Algorithm 3.1
  exists; the method is Definition 3.1.
- Def. 4.4: "$\mathcal T_\tau(Y)$ is the best rank $q$ approximation of $Y$ so
  that the $(q+1)$th singular value of $Y$ equals the tolerance $\tau$". The
  letter $q$ is reused for the adaptive rank, against the fixed coarse rank
  $q$, and "equals" should read "is below".
- Theorem 3.8 takes $A,\tilde A\in\mathbb R^{m\times n}$, reusing the slice index
  $n$ as a column count. Its proof writes $\lVert\cdot\rVert_F$ once where
  the paper elsewhere writes $\lVert\cdot\rVert$.
- Proof of Lemma 3.2: "the solution of (1) at time $h$ with initial value
  $Y_0=Z$"; the initial value of (1) is $X_0$. The same proof writes
  $\dot E=F(X-Z-W+V)+\dots$ for affine $F=\mathcal A+B$. The identity holds
  with $\mathcal A$ in place of $F$, because the four copies of $B$ cancel.
  The argument survives.
- Proof of Lemma 3.4: the generating function is defined as
  $\sum_{n=1}^\infty$ and later written $\sum_{n=0}^\infty$ (harmless, since
  $e^k_0=0$).
- Theorem 3.5 is stated "for all $n,k\in\mathbb N$", but
  $\prod_{j=2}^k(n-j)$ is zero or of indefinite sign for $n\le k$. The
  derivation covers $n\ge k+1$; for $n\le k$ the initial-error term vanishes
  by Lemma 3.4.
- Theorem 2.3 puts $h$ on the flows and $t$ in the bound.
- Kieri, Lubich & Walach (2016) in the references prints "SIAM J. Numer.
  Anal.,," (double comma).

*(Compiler observation, not in the sources.)* Fig. 8a shows the $q=4$ Riccati error stalling
near $10^{-2}$ and dropping only near the final iteration, which
"slower (but still superlinear)" describes generously.

# Notation map

| Carrel et al. (2023) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| **$h$**, $t_n=nh$, $T=Nh$ | $\Delta T$, $T_j$, $N$ | **$h$ is the registry step**; here it is the Parareal slice length |
| $n$ (slice index) | $j$ | **$n$ is also the grid size in §4.1** |
| $k$ (superscript) | $k$, written $U^{(k)}_j$ | Parareal iteration index; **$k$ is also the column count of $C$ in (27), (33)–(34)** |
| $X(t)\in\mathbb R^{m\times m}$, $X_n$ | $y(t)$, $y(T_j)$ | matrix-valued solution |
| **$F(t,X)$** | $f(t,y)$ | **collision with the elementary differential $F(\tau)$** |
| $X^k_n$, $Y^k_n$ | $U^{(k)}_j$ | Parareal and low-rank Parareal iterates |
| $\mathcal F^h$, $\mathcal G^h$ | $\mathcal F$, $\mathcal G$ | fine and coarse propagators over one slice |
| $\phi^h$ | $\varphi_{\Delta T}$ | exact flow |
| **$\psi^h_r$** | $\psi_r$ (page-local) | DLRA flow at rank $r$; **the registry $\psi_h$ is a numerical one-step map** |
| $r$, **$q$** | $r$, $q$ (page-local) | fine and coarse ranks, kept as on [Parareal](/methods/parareal.md); **$q$ is the registry stage order** |
| $\mathcal M_r$, $P_Y$ | — | manifold of rank-$r$ matrices, tangent-space projector |
| $\mathcal T_r$, $\mathcal T_q$, $\mathcal T_{r,q}=\mathcal T_r-\mathcal T_q$, $\mathcal T_\tau$ | $\mathcal T_r$, $\mathcal T_q$, $\mathcal T_r-\mathcal T_q$, $\mathcal T_\tau$ | truncated SVD; tolerance-based truncation |
| $\mathcal E_n$ | $\mathcal E_j$ | rank-completing random perturbation |
| $E^k_n=X_n-Y^k_n$ | $E^{(k)}_j$ (page-local, its norm) | Frobenius norm unless subscript 2 |
| $L$, **$\ell$** | — , $\ell$ (page-local) | Lipschitz and one-sided Lipschitz constants (logarithmic norm); **$\ell$ is the registry micro-step index (multirate pages)** |
| **$\varepsilon_r$** | $\epsilon_r$ (page-local) | DLRA modelling error; **collision with the stiffness parameter $\varepsilon$** |
| $C_q$, $C_{r,q}$ | $C_q$, $C_{r,q}$ | Lipschitz constants of the truncations |
| **$\alpha$**, **$\beta$**, **$\gamma$**, $\kappa$ | $\alpha$, $\beta$, $\gamma$, $\chi$ (page-local) | recursion constants (16); **collisions with the Shu–Osher $\alpha_{ij},\beta_{ij}$ and the tree density $\gamma$**; $\alpha$ is also a diffusion coefficient in §4.3 |
| $\sigma_i$ | $\sigma_i$ | singular values; **collision with the tree symmetry $\sigma(\tau)$** |
| $\mathcal A$, $B$ | $\mathcal A$, $B$ | linear part and constant of affine $f$ |
| **$A$** (Lyapunov) | $A_{\mathrm L}$ | **collision with the Butcher matrix**; $\kappa_A$ its condition number |
| $\tau$ | $\tau$ (page-local) | truncation tolerance; **collision with the tree $\tau$** |
| $\rho_k(\xi)$ | — | generating function of Lemma 3.4 |

# Reference list

The paper prints 37 references in author–year style, alphabetical. All
are merged complete into the [bibliography](/bibliography.md) with
`citedby` carrel-2023. Same-author same-year pairs take printed-order
suffixes: Ceruti & Lubich and Ceruti, Kusch & Lubich (2022), Feppon &
Lermusiaux 2018a and 2018b, and Gander's "Time Parallel Time Integration"
(University of Geneva, 2018, printed oddly and entered as a misc item)
beside the Gander & Kwok book (2018). Five preprints are entered as their
own items. Ceruti et al. (2022) prints no volume or pages. No DOIs are
printed.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [Heat equation](/benchmarks/heat-equation.md)
* [Operator splitting: Lie–Trotter, Strang and dimensional splitting](/methods/operator-splitting.md)
* [Parallel-in-time integration](/methods/parallel-in-time-integration.md)
* [Parareal](/methods/parareal.md)
