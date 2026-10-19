---
type: Source
title: "Bencomo & Chan (2023) — Discrete Adjoint Computations for Relaxation Runge–Kutta Methods"
description: "Derives the discrete tangent-linear and adjoint recurrences of relaxation Runge–Kutta methods (IDT and RRK) by implicit differentiation of the relaxation root, proves exact time-symmetry of the adjoint on skew-symmetric linear problems, and shows that only the full linearization gives consistent, accurate gradients."
resource: "doi:10.1007/s10915-023-02102-y"
source_kind: paper
authors: [Bencomo M.J., Chan J.]
year: 2023
venue: "J. Sci. Comput. 94:59"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Journal_of_Scientific_Computing_Bencomo_Discrete_Adjoint_Computations_for_Relaxation_RungeKutta_Meth.pdf"
tags: [relaxation, adjoint, structure-preserving, runge-kutta, entropy-stability]
timestamp: 2026-10-19T00:00:00Z
---

# Summary

The paper derives the [discrete tangent-linear and adjoint](/methods/discrete-adjoint-runge-kutta.md)
of [relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md), for
discretize-then-optimize gradients in optimal control. Relaxation multiplies
the Runge–Kutta update by $\gamma_n$, the nonzero root closest to one of a
scalar entropy equation, so that a convex entropy $\eta$ is conserved or
dissipated by the fully discrete scheme
([entropy stability](/properties/entropy-stability.md)). Two variants are
treated: the incremental direction technique (IDT), which keeps
$t_n=t_{n-1}+h$, and RRK proper, which advances time by $\gamma_nh$.

The whole time-stepping loop is written as one global block lower-triangular
system (after Rothauge). Its Jacobian, solved forward, gives the tangent
recurrences; its transpose, solved backward, gives the adjoint ones. Because
$\gamma_n$ depends on $y_{n-1}$ and the stages, implicit differentiation of
the root equation adds rank-one terms to both recurrences. For RRK the last
step is an IDT step of length $h^*=T-t_{N-1}$, which depends on every earlier
$\gamma_n$ and adds accumulated corrections (Lemmas 1–4).

For skew-symmetric linear systems $y'=Sy$ with $\eta=\frac12\lVert y\rVert^2$,
IDT and RRK commute with linearization (Theorems 1, 3). With explicit or
diagonally implicit base methods, the adjoint started from $\lambda_N=y_N$
retraces the forward solution exactly, $\lambda_n=y_n$ (Theorems 2, 4). The
authors stress that this "time-symmetry" is not the adjoint method or
symmetric method of geometric integration
([symplecticity](/properties/symplecticity.md)).

The tests use the nonlinear pendulum, 1D compressible Euler with entropy-stable
DG, and a random $10\times10$ skew-symmetric system, with Heun, SSPRK(3,3),
RK4 and Alexander's DIRK3 as base methods. Finite-difference checks converge
only with the full linearization. The properly linearized RRK adjoint is
consistent with optimal order and is the most accurate adjoint tested, more
accurate than the plain Runge–Kutta adjoint. Freezing $h^*$ loses one order.
The paper contrasts this with Eberhard & Bischof and with Alexe & Sandu, who
argue that differentiating through adaptive step selection is non-physical.

# Version read

The file is the arXiv preprint arXiv:2107.11408v1 [math.NA] (23 Jul 2021),
39 pages, with the footer "Preprint submitted to Journal of XXXX, July 27,
2021". It is not the J. Sci. Comput. version of record, and it prints no DOI.
Title and authors match Crossref; page 1 prints the title in sentence case
("Discrete adjoint computations for relaxation Runge-Kutta methods"). Section,
equation, figure and reference numbers on this page are those of arXiv v1;
the published article may differ.

# Key claims

Notation: step index $n=1,\dots,N$; $Y_{n,i}$ the stages of step $n$,
$f_{n,i}=f(Y_{n,i},t_{n-1}+c_ih)$, $J_{n,i}$ the Jacobian at stage $i$;
$\delta_n,\Delta_{n,i}$ the tangent solution and stages; $\lambda_n,\Lambda_{n,i}$
the adjoint solution and stages (page-local); $w_n,W_{n,i}$ source terms;
$r_n(\gamma)$ the relaxation root function.

1. The discrete adjoint of relaxation Runge–Kutta follows from a global matrix form of the time stepping plus implicit differentiation of the root equation. The result is a backward recurrence with the cost structure of the Runge–Kutta adjoint plus rank-one corrections (§2.2, Lemmas 1–2, Appendix). **Derived**
2. $\gamma_n$ depends only on $y_{n-1}$ and $Y_n$; its gradients are $\nabla_y\gamma_n^\top=-(\partial r_n/\partial\gamma)^{-1}\partial r_n/\partial y_{n-1}$ and $\nabla_Y\gamma_{n,i}^\top=-(\partial r_n/\partial\gamma)^{-1}\partial r_n/\partial Y_{n,i}$ (§2.2.1, Eqs. 13–14). **Derived**
3. Treating $\gamma_n$ as a constant in the linearization gives the Runge–Kutta formulas with $b\mapsto\gamma_nb$ and "will have negative consequences" (§2.2.1). **Stated** (shown in §3)
4. Linearized IDT (Lemma 1): $\delta_n=\delta_{n-1}+\gamma_nh\sum_ib_iJ_{n,i}\Delta_{n,i}+\rho_nh\sum_ib_if_{n,i}+w_n$ with $\rho_n=(\nabla_y\gamma_n)^\top\delta_{n-1}+(\nabla_Y\gamma_n)^\top\Delta_n$; the stages are as for Runge–Kutta (Eq. 15). **Derived**
5. Adjoint IDT (Lemma 2): $\lambda_{n-1}=\lambda_n+\sum_i\Lambda_{n,i}+\xi_n\nabla_y\gamma_n+w_{n-1}$, $\xi_n=h\sum_ib_if_{n,i}^\top\lambda_n$, $\Lambda_{n,i}=hJ_{n,i}^\top(\gamma_nb_i\lambda_n+\sum_ja_{ji}\Lambda_{n,j})+\xi_n\nabla_Y\gamma_{n,i}+W_{n,i}$ (Eqs. 16–17). **Derived**
6. The proper linearization needs, per step, $y_{n-1}$, $y_n$, $Y_n$, $f$ and its Jacobian, and the gradient and Hessian of $\eta$ (§2.2.1). **Stated**
7. For $f=Sy$, $S$ skew-symmetric, $\eta=\frac12\lVert y\rVert^2$: IDT and linearized IDT coincide; with $\delta_0=y_0$ and zero sources, $\delta_n=y_n$ for all $n$ because $\rho_n=0$ (Thm. 1). **Proved**
8. In that case the root is explicit: $\gamma_n=-2y_{n-1}^\top d_n/\lVert d_n\rVert^2$ with $d_n=h\sum_ib_iSY_{n,i}$ (Eq. 19). **Derived**
9. For explicit or diagonally implicit base methods, IDT is time-symmetric on $y'=Sy$: the adjoint started from $\lambda_N=y_N$ with zero sources gives $\lambda_n=y_n$ for all $n$, and the adjoint stages vanish (Thm. 2). **Proved**
10. The paper's "adjoint" (transpose of the linearized global system) and "time-symmetry" must not be equated with the adjoint method and time-reversibility of geometric integration (§2.2.2). **Stated**
11. RRK end-of-interval handling: the last step is an IDT step with $h^*=T-t_{N-1}=T-t_0-h\sum_{\ell=1}^{N-1}\gamma_\ell$, so $h^*$ and $\gamma_N$ depend on all earlier steps (§2.2.3, Eq. 24). **Derived**
12. Linearized RRK (Lemma 3): steps $1,\dots,N-1$ as linearized IDT; the last step uses $h^*$ and the stage correction $-\rho_*h\sum_ja_{ij}f_{N,j}$ with $\rho_*=\sum_{n=1}^{N-1}\rho_n$. **Derived**
13. Adjoint RRK (Lemma 4): the first reverse step is adjoint IDT with $h\mapsto h^*$; the others use $\xi_n-\xi_*$ in place of $\xi_n$, with $\xi_*=h\sum_i\sum_ja_{ji}f_{N,i}^\top\Lambda_{N,j}$. **Derived**
14. Theorems 1–2 carry over to RRK (Thms. 3–4): RRK equals linearized RRK on skew-symmetric linear problems, and RRK with an explicit or DIRK base is time-symmetric, since $\rho_*=\xi_*=0$. **Proved**
15. The scalar root is found by bisection (§3). **Stated**
16. Finite-difference check on the pendulum ($h=0.1$, $T=200$): the full linearization converges as $O(\epsilon)$ in the perturbation size for RRK2/3/4; the $\gamma$-constant and $h^*$-constant variants stall, the latter at smaller errors (§3.3.1, Fig. 1). **Shown**
17. Same check on 1D Euler (DG degree 3, element size $1/16$, RK4, CFL 1 and 1.5): the full linearization converges linearly; both improper variants fail, here the $h^*$-constant one with the larger error (§3.3.2, Fig. 2). **Shown**
18. Forward errors of RK and RRK of orders 2–4 converge at the expected rates on the pendulum ($T=2$) (§3.4, Fig. 3). **Shown**
19. The discrete RRK adjoint is consistent, contrary to the argument of Eberhard & Bischof and Alexe & Sandu for adaptive stepping. Full linearization and the $\gamma$-constant variant attain optimal order; the $h^*$-constant variant loses one order (RRK2 $O(h)$, RRK3 $O(h^2)$, RRK4 $O(h^3)$). Reference: RK4 adjoint with $h=10^{-5}$ (§3.4, Fig. 4). **Shown**
20. The properly linearized RRK adjoint is the most accurate adjoint tested, including standard Runge–Kutta (§3.5, Fig. 4). **Shown**
21. Long-time adjoint norm on the pendulum ($T=200$): with $h=0.1$ and RK4 all adjoints agree; with RK2 the standard adjoint deviates early and the $\gamma$-constant one becomes erratic; with $h=0.9$ (RK4) the $\gamma$-constant adjoint grows and the standard RK4 adjoint is highly inaccurate, partly from forward dissipation (§3.5, Figs. 5–6). **Shown**
22. Time-symmetry test (random skew $S$, $d=10$, $T=10\lVert S\rVert_F\approx133.46$): RRK (full and $h^*$-constant) gives $\lVert\lambda_0-y_0\rVert/\lVert y_0\rVert\sim10^{-14}$ for RK2, RK3, RK4 and DIRK3; standard Runge–Kutta and $\gamma$-constant RRK violate it (§3.6, Fig. 7). **Shown**
23. The symmetry error of the non-symmetric variants converges at order 5 for RK4 and 3 for RK2, one above the method order, which the authors cannot explain; at order 3 for RK3 and DIRK3 (§3.6, Fig. 7). **Shown**
24. The $h^*$-constant variant is time-symmetric on the linear problem because $\rho_*$ and $\xi_*$ vanish there (§3.6). **Derived**
25. The discrete adjoint of a Runge–Kutta method is consistent and is itself a Runge–Kutta scheme of the same order (§1, §3.4). **Stated** (prior work)
26. IDT has order $p-1$ for an order-$p$ base method; RRK keeps order $p$ (§2.2). **Stated** (prior work)

# Printed slips

- **Lemma 4 against the Appendix (p. 37):** the Appendix prints $\lambda_{k-1}=\sum_i\Lambda_{k,i}+\lambda_k+\Gamma_{y,k}^\top\lambda_k+\xi_*\nabla_y\gamma_k^\top+w_{k-1}$, with $+\xi_*$, while Lemma 4 (p. 15), the adjacent stage line ($-\xi_*$) and the block matrix on p. 37 all give $-\xi_*$. The Appendix sign is the slip.
- Appendix p. 37: $\xi_*$ is printed with $F_{K,i}$ untransposed; Lemma 4 prints $F_{K,i}^\top$.
- pp. 15–16: "linearized and adjoint IDT formulas define solutions to the following matrix systems" introduces systems with the $\Delta t^*$ terms, i.e. the RRK systems.
- Fig. 4(b) ("Using RK3"): the legend lists "RRK4 ($\gamma$-const)" for RRK3.
- Theorem 3 omits the hypothesis $\eta=\frac12\lVert y\rVert^2$ that Theorem 1 states.
- Root choice: §2.2 "the non-zero root (closest to one)", Appendix p. 31 "the positive root near 1".
- Appendix section numbered "4.1" after the unnumbered Appendix heading; "uncontrained" (p. 3).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y_k$, $k=1,\dots,K$ | $y_n$, $n=1,\dots,N$ | step index and number of steps; **collision**: the registry's $K$ is the number of correction iterations |
| $y\in\mathbb R^N$ | $y\in\mathbb R^d$ | **collision**: the source's $N$ is also the DG polynomial degree ($N=3$) and $\mathsf N$ the nonlinear part of the global system |
| $\Delta t$, $\Delta t^*$ | $h$, $h^*$ | nominal and corrected final step; the source's $h$ is the FD perturbation (written $\epsilon$ in claim 16) and the DG element size |
| $A_s$, $b_s$, $c_s$ | $A$, $b$, $c$ | column vectors (agrees) |
| $Y_{k,i}$ | $Y_{n,i}$ | stage values (agrees) |
| $F_{k,i}$ | $f_{n,i}=f(Y_{n,i},t_{n-1}+c_ih)$ | stage derivatives |
| $J_{k,i}$ | $J_{n,i}$ | Jacobian at stage $i$ (agrees) |
| $\gamma_k$ | $\gamma_n$ | relaxation parameter; **collision** in §3.1 with the ratio of specific heats $\gamma=1.4$ |
| $\eta$, $\nabla\eta$, $\nabla^2\eta$ | $\eta$, $\eta'(y)$, $\eta''(y)$ | convex entropy |
| $r_k(\gamma;\bar y)$ | $r_n(\gamma)$ | root function (page-local) |
| $d_k$, $e_k$ | same (page-local) | search direction, entropy production |
| $\delta_k$, $\Delta_{k,i}$ | $\delta_n$, $\Delta_{n,i}$ | tangent solution and stages (page-local); $\Delta_{n,i}$ is not a mesh width |
| $\lambda_k$, $\Lambda_{k,i}$ | $\lambda_n$, $\Lambda_{n,i}$ | adjoint solution and stages; **collision**: the registry's $\lambda$ is an eigenvalue |
| $\rho_k$, $\xi_k$, $\rho_*$, $\xi_*$ | same (page-local) | scalars of the $\gamma$ and $h^*$ linearization |
| $L$, $\chi_k$ | same (page-local) | **collision**: $L$ is the lower unit-triangular linear part of the global system, not a linear operator $y'=Ly$ |
| $S$ | same | skew-symmetric matrix of $y'=Sy$ |
| $y_{init}$ | $y_0$ | initial value |

# Reference list

The preprint prints 25 references in numbered style ([1]–[25], order of first
citation). The list is merged complete into the [bibliography](/bibliography.md),
with `citedby` this slug. [19] is software (GitHub, dated "05 2019", Zenodo
DOI 10.5281/zenodo.3066518) and [21] an arXiv preprint (arXiv:2006.07504),
kept as its own entry. [23] is an AIAA paper printed with "p. 456" (the paper
number). Two Ranocha 2020 works ([2], [3]) are matched to the bibliography by
title and venue. No printed duplicates.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [Discrete adjoints of Runge–Kutta and relaxation Runge–Kutta methods](/methods/discrete-adjoint-runge-kutta.md)
* [Entropy stability and conservation of the fully discrete scheme](/properties/entropy-stability.md)
* [Relaxation Runge–Kutta methods](/methods/relaxation-runge-kutta.md)
* [Symplecticity and quadratic-invariant preservation](/properties/symplecticity.md)
