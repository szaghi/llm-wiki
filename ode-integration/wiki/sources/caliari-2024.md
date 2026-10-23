---
type: Source
title: "Caliari et al. (2024) — Accelerating exponential integrators to efficiently solve semilinear advection-diffusion-reaction equations"
description: "Puts only a constant-coefficient fraction of the diffusion and a mean advection into the linear part of exponential and Lawson integrators, proves per-scheme lower bounds on that fraction for unconditional stability, adds two stabilized Lawson schemes, and shows speedups up to about 15 with FFT and μ-mode matrix functions."
resource: "doi:10.1137/23m1562056"
source_kind: paper
authors: [Caliari M., Cassini F., Einkemmer L., Ostermann A.]
year: 2024
venue: "SIAM J. Sci. Comput. 46:A906-A928"
local_file: "/home/stefano/papers/mosaic/ode-integration/2024_Crossref_SIAM_Journal_on_Scientific_Computing_Caliari_Accelerating_Exponential_Integrators_to_Efficiently_Solve_Se.pdf"
tags: [exponential, lawson, stability, explicit-implicit-null, advection-diffusion-reaction]
timestamp: 2026-10-20T06:18:00Z
---

# Summary

The paper carries the idea behind preconditioning, solving a simpler
related problem, over to [exponential integrators](/methods/exponential-integrators.md).
For a semilinear advection–diffusion–reaction (ADR) equation with variable
diffusion tensor and velocity, the full linear operator has matrix
functions that need general Krylov or Leja algorithms
([evaluating φ-functions](/methods/phi-function-evaluation.md)). Instead
the linear part $L$ holds only a constant-coefficient operator: a fraction
$\delta\in[0,1]$ of the pointwise maximum of the diagonal diffusion, plus a
mean effective velocity. The rest of the diffusion and advection moves
into the explicitly treated remainder $N$. The matrix functions of $L$
are then cheap: pointwise in Fourier space for periodic problems, or by
$\mu$-mode (Tucker) products when $L$ is a Kronecker sum. This is the
exponential analogue of the IMEX
[explicit–implicit–null](/methods/explicit-implicit-null-method.md) approach
of Wang, Zhang, Wang & Shu (2020).

A Fourier [stability](/definitions/stability-function.md) analysis of the
heat equation, split as $\delta\Delta+(1-\delta)\Delta$, gives for each scheme the
smallest $\delta$ for stability on the whole negative real axis (Thms 2.1–2.7,
Table 1). The bounds are: exponential Euler $1/2$; second-order exponential
Runge–Kutta $1/(1+c_2)$ with $\phi_2$ and $1/(1+2c_2)$ with $\phi_1$ only;
Lawson–Euler $0.218$; Lawson2a/2b $0.301$; and $1/2$ for the IMEX
backward–forward Euler and imex2 schemes. Two new
[Lawson schemes](/methods/lawson-methods.md) lower the bound further:
stabilized Lawson–Euler ($1/(2e)\approx0.184$) and stabilized Lawson2
($0.183$). They are not exact for linear problems and not A-stable, but
their stability regions contain the negative real axis.

1D tests confirm that the bounds are sharp. The smallest stable $\delta$ is not
always the most accurate, so the authors choose $\delta$ by a cheap scan on a
coarse grid. In MATLAB runs on 2D (FFT) and 3D ($\mu$-mode) ADR problems, the
reformulated schemes beat the same integrators on the full operator (kiops
for exponential schemes, bicgstab for IMEX) by up to about a factor 15 in
3D. They often beat the IMEX counterparts as well.

# Version read

arXiv:2303.15861v2 [math.NA], stamped 19 October 2023 (title page dated
October 20, 2023), 23 pages: main text pp. 1–20, appendix pp. 20–21,
references pp. 21–23. This is not the SIAM version of record
(pp. A906–A928). Title and authors match the published version. Theorem,
equation, table and figure numbers are those of arXiv v2.

# Key claims

Registry notation: $y$ the solution (source $u$), $h$ the step (source
$\tau$), $L$ the linear part treated exponentially or implicitly (source
$A$), $N$ the page-local explicit remainder (source $g$), $f=Ly+N$ (source
$F$), $Y_2$ the stage (source $U$), $\phi_k$ (source $\varphi_k$), $c_2$ the
node of every two-stage scheme (source $c_2$, and $\alpha$ for sl2). Page-local:
$\delta$ the fraction of diffusion in $L$ (source $\lambda$; page-local, as
on [Lawson methods](/methods/lawson-methods.md) and
[exponential integrators](/methods/exponential-integrators.md); the EIN
stabilization ratio of the IMEX literature), $R(z;\delta)$ the per-mode amplification factor (source
$\Phi(z,\lambda)$), $z=-h\lvert\xi\rvert^2$ with wavenumber $\xi\in\mathbb Z^d$
(source $k$). Unconditional stability means $\lvert R(z;\delta)\rvert\le1$ for all
$z\le0$. Scheme labels: ee, le, sle, erk2p2, erk2p1, l2a, l2b, sl2, bfe,
imex2, erbe.

1. Exponential Euler (ee) on the split heat equation is unconditionally
   stable iff $\delta\ge1/2$; $R=1-1/\delta+e^{\delta z}/\delta$ (Thm 2.1). **Proved**
2. Lawson–Euler (le), $R=e^{\delta z}(1+(1-\delta)z)$, is unconditionally stable for
   $\delta\ge0.218$; the bound is the zero of $1-1/\delta+e^{1/(1-\delta)}$ (Thm 2.2).
   **Proved** (bound computed numerically)
3. The new stabilized Lawson–Euler (sle), $y_{n+1}=y_n+he^{hL}f(t_n,y_n)$,
   with $R=1+ze^{\delta z}$, is unconditionally stable for
   $\delta\ge1/(2e)\approx0.184$ (Thm 2.3). **Proved**
4. ExpRK2 with $\phi_2$ (erk2p2) is unconditionally stable for
   $\delta\ge1/(1+c_2)$; the minimal bound $1/2$ is at $c_2=1$ (Thm 2.4).
   **Proved**
5. ExpRK2 with only $\phi_1$ (erk2p1) is unconditionally stable for
   $\delta\ge1/(1+2c_2)$; $1/3$ at $c_2=1$ (Thm 2.5). **Proved**
6. Lawson2a (l2a) and Lawson2b (l2b) are unconditionally stable for
   $\delta\ge0.301$ (Thm 2.6, "a numerical calculation"). **Proved** (numerical
   bound). Both have
   $R=e^{\delta z}(1+w+w^2/2)$ with $w=(1-\delta)z$, so the equal bounds are
   automatic *(compiler check, not in the sources)*.
7. The new stabilized Lawson2 (sl2) with $c_2=0.327$, chosen to minimize the
   bound, is unconditionally stable for $\delta\ge0.183$ (Thm 2.7). **Proved**
   (numerical bound; a compiler check, not in the sources, gives about 0.1823)
8. IMEX backward–forward Euler (bfe) and the second-order imex2 of Wang et
   al. (2020) need $\delta\ge1/2$ (Remark 2.1, quoted). **Stated**
9. Ranking (Table 1): stabilized Lawson < Lawson < ExpRK and exponential
   Euler ≤ IMEX in the required $\delta$. "Exponential integrators of
   Runge–Kutta type and Lawson schemes can have better stability properties
   than similarly constructed implicit-explicit schemes" (abstract, §2).
   **Proved** (for the model problem, against two IMEX schemes)
10. sle and sl2 are not exact for linear problems and not A-stable, but
    their stability regions contain the whole negative real axis
    (Remark 2.2, Fig. 1). **Shown**
11. A linear Fourier stability analysis of an exponential integrator with a
    partial linear operator "appears to be novel in the literature" (§2;
    earlier only for exponential Euler). **Stated**
12. Reformulation (11):
    $Ly=\delta\sum_\mu\mathcal D^{\max}_{\mu\mu}\partial_{x_\mu x_\mu}y+\bar v\cdot\nabla y$,
    with $\mathcal D^{\max}_{\mu\mu}=\max_x\mathcal D_{\mu\mu}(x)$ and
    $\bar v_\mu=\lvert\Omega\rvert^{-1}\int_\Omega(v_\mu+\partial_{x_\mu}\mathcal D_{\mu\mu})\,dx$.
    The advection hidden in the variable diffusion must be included in
    $\bar v$ (§3). **Derived**
13. Taking $\delta$ as small as stability permits, as Wang et al. do for IMEX,
    is "not necessarily always the best choice". The proposal is a parameter
    scan on a coarse grid that still resolves the dynamics, at negligible
    cost (§3, Fig. 5). **Shown**
14. 1D linear diffusion $\partial_ty=\mathcal D(x)\partial_{xx}y$,
    $\mathcal D=1+10\sin^2x$: all exponential schemes show their order and the
    Table 1 bounds are sharp. At $\delta=1/3$ ee and erk2p2 blow up; at
    $\delta=0.17<0.183$ every scheme loses unconditional stability (§4.1,
    Figs. 2–3). **Shown**
15. 1D nonlinear diffusion–reaction (Fisher-type reaction $y(1-y)$): the
    linear bounds predict the admissible $\delta$ "very sharply". Every method
    gets more accurate as $\delta$ decreases, the second-order ones more so; sle
    and sl2 are the most accurate first- and second-order methods (§4.2,
    Fig. 4). **Shown**
16. 2D ADR: coarse-grid ($2^6$) and fine-grid ($2^8$) scans of $\delta$ are "very
    similar". The selected values (Table 2) are bfe 0.50, ee 0.50, le 0.22,
    sle 0.23, erk2p1 0.33, imex2 0.57, l2a 0.53, sl2 0.57, not always the
    stability bound (§5.1). **Shown**
17. 2D: the reformulated (FFT) schemes are cheaper than the same integrators
    on the original equation (kiops, bicgstab), with slightly better errors
    except Lawson2a. With FFT the wall-clock time barely depends on the
    integrator, since transforms dominate: 7 per step for first-order
    schemes, 13 for second-order ones (§5.1, Fig. 6). **Shown**
18. 2D: imex2 is slightly the best second-order method. erbe (exponential
    Rosenbrock–Euler, original formulation) is cheaper than l2a and erk2p1 in
    the original formulation, but the reformulated approach is still
    superior overall (§5.1, Fig. 6). **Shown**
19. 3D ADR with advection $-0.01$: $\mu$-mode le and sle beat their
    original-formulation counterparts in error and wall-clock time, le
    slightly ahead; $\mu$-mode l2a is the best second-order method "with a
    considerable advantage" (§5.2, Fig. 8). **Shown**
20. 3D with advection $-1$: the reformulated stabilized schemes have
    comparable (sle) or lower (sl2) errors than in the original formulation,
    while le and l2a errors increase; the time gain still makes $\mu$-mode le
    and l2a the best (§5.2, Fig. 9). **Shown**
21. The reformulation outperforms straightforward implementations "up to a
    factor of roughly 15 in the three dimensional case" and often beats
    popular IMEX schemes (§6). **Shown** (summary of Figs. 6, 8, 9)
22. Kronecker-sum structure is easier to exploit for the matrix exponential
    ($\mu$-mode products, $d$ level-3 BLAS calls) than for linear solves;
    conversely, a good preconditioner gives an efficient linear solver but
    not necessarily efficient matrix functions (§1). **Stated**
23. Krylov- or Leja-based exponential integrators "can be superior to
    implicit schemes for realistic problems"; preconditioning does not apply
    to exponential integrators (§1). **Stated**

# Printed slips

- Fig. 4 (right panel), p. 13: the legend reads "ERK1P1" for the
  second-order erk2p1.
- Thm 2.7: the bound 0.183 at $c_2=0.327$ is rounded up; a compiler
  computation, not in the sources, gives about 0.1823.

# Notation map

| Caliari et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $u^n$ | $y$, $y_n$ | |
| **$\tau$** | $h$ | **collision with the tree $\tau$** |
| **$A$** | $L$ | **collision with the Butcher matrix**; constant-coefficient linear part |
| $g$, $F$ | $N$, $f$ | $N$ page-local remainder, including the variable-coefficient terms; **collides** with the registry slice count $N$, always written with arguments |
| $U$ | $Y_2$ | stage value |
| $\varphi_1=(e^z-1)/z$, $\varphi_2=(\varphi_1-1)/z$ | $\phi_1$, $\phi_2$ | same normalisation |
| **$\lambda\in[0,1]$** | $\delta$ | **collision with the eigenvalue**; fraction of maximal diffusion in $L$, the EIN coefficient |
| **$\Phi(z,\lambda)$** | $R(z;\delta)$ | **collision with the elementary weight $\Phi(\tau)$**; per-mode amplification factor |
| $z=-\tau k^2$, **$k$** | $z=-h\lvert\xi\rvert^2$, $\xi$ | **$k$ collides with the step number of multistep methods**; $z$ uses the full Laplacian, not only the part in $L$ |
| $c_2$; **$\alpha$ (sl2)** | $c_2$ | node; **$\alpha$ collides with Shu–Osher / Rosenbrock coefficients** |
| **$a(x)$**, $a^{\max}$ | $\mathcal D(x)$, $\mathcal D^{\max}$ | **collision with the B-series coefficient map $a$**; diffusion tensor |
| **$b(x)$**, **$\beta$** | $v(x)$, $\bar v$ | **collisions with the weights $b$ and PID/multistep $\beta$**; velocity, mean effective velocity |
| $r(t,x,u)$ | — | reaction term |
| $\times_\mu$, $\oplus$ | — | $\mu$-mode product, Kronecker sum |
| **$N$**, **$m$** | $N_x$, $n_{\mathrm{steps}}$ | **collisions with the remainder $N$ and the multirate ratio $m$**; grid points per direction, number of steps |
| "A-stability regions" (Fig. 1) | $\mathcal S$ | stability regions; not A-stability |
| "unconditionally stable" | — | stable on $(-\infty,0]$ only, weaker than [A-stability](/properties/a-stability.md) |

# Reference list

The paper prints 36 references in numbered style, alphabetical. All are
merged complete into the [bibliography](/bibliography.md) with `citedby`
caliari-2024. Refs. [6] and [7] (Caliari, Cassini & Zivcovich 2023) take
the keys `caliari-2023` and `caliari-2023-b` in printed order. Ref. [30]
prints the author as "Papanicolau" (usually Papanicolaou), and the key
follows the printed spelling, `papanicolau-1991`. No DOIs or arXiv numbers
are printed.

# Pages created or updated

Chunk 4 (2026-10-20). This source is cited on:

* [Evaluating φ-functions: Leja interpolation, Krylov and related methods](/methods/phi-function-evaluation.md)
* [Explicit–implicit–null (EIN) time marching](/methods/explicit-implicit-null-method.md)
* [Exponential integrators and φ-functions](/methods/exponential-integrators.md)
* [Heat equation](/benchmarks/heat-equation.md)
* [Lawson (integrating-factor) methods](/methods/lawson-methods.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
