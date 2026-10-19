---
type: Source
title: "Ranocha et al. (2025) — On Error-Based Step Size Control for Discontinuous Galerkin Methods for Compressible Fluid Dynamics"
description: "Compares error-based PID step-size control of embedded explicit Runge–Kutta pairs with hand-tuned CFL control on DG compressible-flow problems in two codes, finding that tolerances are easier to choose, match or beat tuned CFL factors, and handle mesh changes, cold starts and new equations automatically."
resource: "doi:10.1007/s42967-023-00264-y"
source_kind: paper
authors: [Ranocha H., Winters A.R., Castro H.G., Dalcin L., Schlottke-Lakemper M., Gassner G.J., Parsani M.]
year: 2025
venue: "Commun. Appl. Math. Comput. 7:3-39"
local_file: "/home/stefano/papers/mosaic/ode-integration/2023_Crossref_Communications_on_Applied_Mathematics_and_Computation_Ranocha_On_Error-Based_Step_Size_Control_for_Discontinuous_Galerkin.pdf"
tags: [runge-kutta, explicit, step-size-control, embedded-pair, ssp, cfd]
timestamp: 2026-10-19T20:00:00Z
---

# Summary

The paper is a numerical study of [step-size control](/methods/step-size-control.md)
for explicit Runge–Kutta methods applied to method-of-lines discontinuous
Galerkin discretizations of compressible flow (Euler, ideal GLM-MHD,
Navier–Stokes, shallow water with Exner sediment transport). It compares
error-based control against CFL-based control with a hand-tuned factor
$\nu$, maximized by bisection to three significant digits. Error-based
control here means an [embedded pair](/methods/embedded-runge-kutta-pair.md)
in local-extrapolation mode, a weighted RMS error norm and a PID controller
with the arctan limiter, using the pairs and controllers of the authors'
earlier `ranocha-2022` paper. The contribution is evidence, not new
methods.

Four third- and fourth-order pairs, three of them
[low-storage](/methods/low-storage-runge-kutta.md) 3S*$_+$ (BS3(2)3$_F$,
RDPK3(2)5$_F$, RDPK4(3)9$_F$, SSP3(2)4), run in two independent codes:
Trixi.jl with [OrdinaryDiffEq.jl](/software/differentialequations-jl.md),
and SSDC on [PETSc TS](/software/petsc-ts.md). Six scenarios test a mesh
change on the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
shock capturing that alters linear stability (Orszag–Tang), cold-start
transients (double Mach reflection, a Mach 2000 jet, a delta wing, the NASA
CRM with $7.68\times10^8$ DOF), entropy projection (Kelvin–Helmholtz) and a
new equation system without a wave-speed estimate (shallow water–Exner).

In stability-limited runs a tolerance range spanning up to five orders of
magnitude reaches the right-hand-side count of the best tuned CFL factor.
The optimal CFL factor shifts by 55–74 % between meshes, while the good
tolerance range does not. Error-based control matches or beats tuned CFL
control (by 6–13 % on Orszag–Tang, about 5 % on Kelvin–Helmholtz) and
handles cold starts on its own, where CFL control crashes even at
$\nu=0.01$. It also runs where CFL control is impossible. It carries no
hard guarantee such as an invariant-domain CFL bound, and limiters or AMR
applied as callbacks are invisible to the error estimator. The
[SSP](/methods/strong-stability-preserving-runge-kutta.md) pair SSP3(2)4 is
usually most efficient for low-Mach, positivity-critical or strongly
shock-captured problems.

# Version read

The file is the arXiv preprint arXiv:2209.07037v2 [math.NA], 16 February
2023 (title block dated 5 February 2023), 35 pages, all read; it is not the
version of record, despite the "Crossref" in the archive filename, and it
prints no journal pagination or DOI. Title and authors match Crossref. The
paper appeared online in 2023 and in the 2025 issue (vol. 7, pp. 3–39);
the slug and `year` follow the issue year. Page 1 prints the title in
sentence case. Section, equation and table numbers cited here are those of
arXiv v2. Reproducibility repository: Zenodo 10.5281/zenodo.7078946.

# Key claims

1. The explicit pairs are used in local-extrapolation mode with main order $p$ and embedded order $\hat p=p-1$; FSAL pairs include $f(t_{n+1},y_{n+1})$ in the embedded solution through $\hat b_{s+1}\ne0$, at no extra cost when the step is accepted (§2, Eq. 2.2). **Stated**
2. The PID controller uses the exponent denominator $k=\min(p,\hat p)+1$, which equals $p$ for these pairs; the default limiter is $\kappa(a)=1+\arctan(a-1)$; a step is accepted iff the limited factor is at least $0.9^2=0.81$; the error history is initialized to 1 at $n=0$; the initial step follows Hairer–Nørsett–Wanner (§2.3, Eqs. 2.6–2.7, Alg. 2). **Stated**
3. The CFL factor affects efficiency linearly and the tolerance only roughly logarithmically, so a tolerance is easier to choose than an optimal CFL factor (§3). **Stated** (supported by Fig. 2)
4. Inviscid Taylor–Green vortex ($8^3$ elements, degree 3, $t\in[0,10]$): in this stability-limited problem a tolerance range spanning up to five orders of magnitude gives the optimal right-hand-side count attainable with a hand-tuned CFL factor; looser tolerances can crash (positivity, first few steps) and stricter ones enter the accuracy-limited regime (§3, Fig. 2). **Shown**
5. Optimized CFL factors on the curved mesh are 55 % (BS3(2)3$_F$) to 74 % (SSP3(2)4) larger than on the Cartesian mesh: $\nu_{\mathrm{opt}}$ = 0.87 vs 1.35 (BS3(2)3$_F$), 1.71 vs 2.67 (RDPK3(2)5$_F$), 1.59 vs 2.77 (SSP3(2)4); the good tolerance range is essentially unchanged (§3, Fig. 2). **Shown**
6. SSP3(2)4 enters the accuracy-limited regime at looser tolerances than the others because it is optimized only for the SSP coefficient, not for the principal truncation error (§3). **Shown**
7. Linear spectra (2D linear advection, $8^2$ elements, degree 3, blending factor 0.5): DG/FV subcell shock-capturing spectra extend outside the stability regions scaled for pure DGSEM; linear analysis predicts about a quarter larger CFL number for pure DGSEM than for the shock-capturing variant for BS3(2)3$_F$ and RDPK3(2)5$_F$ (more than 20 %), but only about 5 % for SSP3(2)4 (§4.1, Fig. 3). **Shown**
8. Orszag–Tang vortex (ideal GLM-MHD, $64^2$ elements, degree 3, tolerance $10^{-4}$): error-based control takes larger steps before shock capturing activates ($0.1<t<0.2$) and then settles near the tuned-CFL step; its initial step is about a quarter larger than the CFL-based one (§4.2, Fig. 5). **Shown**
9. Orszag–Tang right-hand-side savings of error-based over tuned CFL control: 13 % for BS3(2)3$_F$ (2187 vs 2506), 11 % for RDPK3(2)5$_F$ (1863 vs 2091), 6 % for SSP3(2)4 (1550 vs 1648) (§4.2, Table 1). **Shown**
10. On Orszag–Tang, RDPK3(2)5$_F$ uses 15 % fewer right-hand-side evaluations than BS3(2)3$_F$, and SSP3(2)4 a further 16 % fewer than RDPK3(2)5$_F$ (§4.2). **Shown**
11. The linear analysis is not expected to be quantitatively correct for nonlinear problems; shock capturing reduces the smoothness of the right-hand side, which also affects step-size control (§4.2). **Stated**
12. Double Mach reflection (SSP3(2)4, AMR, Zhang–Shu positivity limiter after every stage): an automatic initial transient of about 100 steps with much smaller $h$ and effective CFL; CFL-based control crashes in the first few steps even with $\nu=0.01$ (§5.1, Fig. 7). **Shown**
13. Mach 2000 jet: the initial step must be set by hand to $h\approx10^{-12}$ (the automatic initial guess is insufficient); the transient lasts about 100 steps; CFL control would need $\nu\approx10^{-9}$ initially, and $\nu=10^{-8}$ blows up (§5.2, Fig. 9). **Shown**
14. Delta wing (SSDC, Navier–Stokes, about $1.435\times10^7$ DOF): the asymptotic step is reached after a few hundred steps; CFL control needs an initial factor 13 % (BS3(2)3$_F$), 21 % (RDPK3(2)5$_F$) and 32 % (SSP3(2)4) below the asymptotic one; at tolerance $10^{-8}$ up to $t=0.015$ the counts are 17 641 / 14 963 / 13 392 right-hand-side evaluations (§5.3, Fig. 12, Table 2). **Shown**
15. NASA CRM (SSDC, $12.8\times10^6$ hexahedra, degree 3, about $7.68\times10^8$ DOF): CFL control needs an initial factor 16 % (RDPK3(2)5$_F$) and 9 % (SSP3(2)4) below the asymptotic one, while for BS3(2)3$_F$ the asymptotic factor works throughout; at tolerance $10^{-8}$, $t\le0.004$: 5874 / 4610 / 5920 evaluations with zero rejected steps (§5.4, Table 3). **Shown**
16. On a second CRM mesh (HiOCFD5 CRM-WB-a2.75-Coarse-P2A), CFL control with the target CFL of about 3.6 from the first mesh fails for all three methods, since the new mesh's asymptotic CFL is about 1.2; error-based control runs all three to the end (§5.4). **Shown**
17. Kelvin–Helmholtz, Atwood number 3/7, entropy-stable Gauss DG with entropy projection: error-based control always needs fewer right-hand-side evaluations and steps than tuned CFL control, "usually around 5 %"; RDPK4(3)9$_F$ needed tolerance $10^{-5}$ (it crashed at $10^{-4}$); SSP3(2)4 was most efficient (5478 evaluations), then RDPK3(2)5$_F$ (6403) (§6.1, Table 4). **Shown**
18. Kelvin–Helmholtz, Atwood number 0.7: the evolved variables lose positivity around $t\approx3$ even with $\nu=0.05$ for SSP3(2)4, so CFL-based control is not possible; error-based control works directly (RDPK4(3)9$_F$ needs tolerance $10^{-6}$), SSP3(2)4 again most efficient (6618 evaluations) (§6.2, Table 5). **Shown**
19. The difficulty of RDPK4(3)9$_F$ is attributed to its larger number of stages, "making it more difficult to adapt quickly to changing conditions" (§6.2). **Stated**
20. Error-based control needs no estimate of the maximal eigenvalues, which helps for new equation systems: for shallow water–Exner with the Grass closure ($m=3$), the $x$-Jacobian eigenvalues are $v_1$ and the roots of a cubic (Eq. 7.5), and a loose bound $v_1\pm\sqrt{gh}$ causes excessive diffusion of the slow bed (§7). **Derived**
21. Sand-dune test (tolerance $10^{-7}$, 100 h of physical time): all three methods work directly; RDPK4(3)9$_F$ is most efficient (6 442 851 evaluations), then RDPK3(2)5$_F$ (6 873 513) and BS3(2)3$_F$ (8 088 687); the numerical spreading angle is $20.4^\circ$ against the theoretical $21.787^\circ$ (§7, Table 6, Eq. 7.9, Fig. 19). **Shown**
22. Error-based control has no hard mathematical guarantee: it cannot in general be proven to satisfy the CFL constraints under which invariant-domain-preserving methods are robust, and AMR and positivity limiters applied as callbacks are "not seen" by the error estimator (§8). **Stated**
23. Recommendation: SSP3(2)4 is usually most efficient for lower-Mach flows or problems with positivity issues or strong shock capturing; otherwise RDPK3(2)5$_F$ (more robust) and RDPK4(3)9$_F$ (more efficient at strict tolerances); BS3(2)3$_F$ remains one of the best general-purpose choices (§8). **Shown** (summary of §§3–7)
24. Cures exist for CFL control (restart with a larger $\nu$ after a cold start, a user ramp, including the shock-capturing indicator in the CFL estimate), but they need extra mechanisms, whereas error-based control "worked right out of the box" (§8). **Stated**

# Printed slips

- Eq. 7.4, row 4, column 2 prints $\frac{\xi A_g}{h}(3v_1^2+v_2)$; by Eq. 7.5 it should be $(3v_1^2+v_2^2)$ (p. 23, checked visually).
- §5.2: "in the domain [−0.5, 0.5]" for a 2D problem, exponent $^2$ missing (p. 14).
- §6.1: "Orzsag-Tang vortex".
- §5.4: "held at Ceneaero, Belgium" against ref. [13] "Cenaero".
- §5.4: "maximum aspect ratio of approximately 105" (p. 18), possibly meaning $10^5$.
- §5.4: about $7.68\times10^8$ DOF for $12.8\times10^6$ elements at degree 3 implies 60 DOF per element, matching neither $4^3=64$ nodes nor $5\times64=320$ conservative-variable DOF; unexplained.
- §5.3: $\bar c=0.653$ m is introduced next to a mean aerodynamic chord $\ell=0.667$ m; two chord values, unexplained.
- §8: "optimize new RK methods … in other ranges than [2]" cites Al Jahdali et al. where [76] may be meant; ambiguous.
- Ref. [82] prints an empty year "1 ()".
- The method name `RDPK3SpFSAL49()` for the fourth-order RDPK4(3)9$_F$ is the actual OrdinaryDiffEq.jl name, not a slip; its "3" does not denote the order.

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $f(t,u)$, $u^n$ | $y$, $f(t,y)$, $y_n$ | non-autonomous form |
| $y_i$ | $Y_i$ | stage values; **collision**: the source's $y$ is a stage, not the solution |
| $\Delta t_n$ | $h_n$ | |
| $s$, $A$, $b$, $c$ | $s$, $A$, $b$, $c$ | agree |
| $\hat b\in\mathbb R^{s+1}$, $\hat u^{n+1}$ | $\hat b$, $\hat y_{n+1}$ | $\hat b_{s+1}$ is the FSAL weight |
| $q$, $\hat q$ | $p$, $\hat p$ | main and embedded order; **collision**: registry $q$ is the stage order |
| $k=\min(q,\hat q)+1$ | $k=\min(p,\hat p)+1$ | agree |
| $\beta_1,\beta_2,\beta_3$ | $\beta_1,\beta_2,\beta_3$ | agree: $\varepsilon^{\beta_i/k}=\mathrm{err}^{-\beta_i/k}$; values (0.60, −0.20, 0.00), (0.70, −0.23, 0.00), (0.38, −0.18, 0.01), (0.55, −0.27, 0.05) for BS3, RDPK3(2)5, RDPK4(3)9, SSP3(2)4 |
| $w_{n+1}$ | $\mathrm{err}_n$ | weighted RMS norm $\lVert\cdot\rVert_{\mathrm{WRMS}}$ of $y_{n+1}-\hat y_{n+1}$ |
| $\varepsilon_{n+1}=1/w_{n+1}$ | $1/\mathrm{err}_n$ | **collision** with the registry stiffness parameter $\varepsilon$ |
| $\tau_a$, $\tau_r$ | $\mathrm{atol}$, $\mathrm{rtol}$ | equal to `tol` by default |
| $\kappa$ | — | step-size limiter $1+\arctan(a-1)$ |
| $\nu$ | $\nu$ | CFL factor (agree) |
| $\lambda_{\max}$, $\Delta x_i$ | — , $\Delta x$ | local wave speed and mesh spacing |
| $p$ | — | DG polynomial degree, written in words on this page; **collision** with the registry order $p$ |
| $m$ | — | number of DOF; also the Grass exponent (§7) |
| $\alpha$ | — | DG/FV blending factor (§4); spreading angle (§7) |
| $A$, $A_g$ | — | Atwood number (§6), Grass constant (§7); **collision** with the Butcher matrix |
| #FE, #A, #R | — | right-hand-side evaluations, accepted and rejected steps |

# Reference list

The paper prints 99 references in numbered style ([1]–[99]), ordered
alphabetically. The list is merged complete into the
[bibliography](/bibliography.md), with `citedby` this slug. No printed
duplicates. Ref. [76] is the ingested
[Ranocha et al. (2022)](/sources/ranocha-2022.md), printed with its 2021
online year; ref. [80] (Trixi.jl, JuliaCon proceedings 2022) is a
different work, keyed `ranocha-2022-b`. Ref. [21] is the ingested
[Fekete et al. (2022)](/sources/fekete-2022.md), printed with the arXiv
author order (Conde first). Pre-publication items ([1] PETSc/TS, [30], [33], [79],
[98], all arXiv) are their own entries; [44] is a workshop presentation;
[9], [18], [19] and [77] print no volume or pages; [82] prints an empty
year; [20] is a NASA technical memorandum. All items parsed.

# Pages created or updated

Chunk 2 (2026-10-19). This source is cited on:

* [DifferentialEquations.jl](/software/differentialequations-jl.md)
* [Embedded Runge–Kutta pairs and the FSAL property](/methods/embedded-runge-kutta-pair.md)
* [Low-storage Runge–Kutta methods](/methods/low-storage-runge-kutta.md)
* [PETSc TS](/software/petsc-ts.md)
* [Step-size control: error-based controllers, PID filters and CFL control](/methods/step-size-control.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
