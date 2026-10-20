---
type: Source
title: "Chouchoulis et al. (2022) — Jacobian-Free Explicit Multiderivative Runge–Kutta Methods for Hyperbolic Conservation Laws"
description: "Makes explicit multiderivative Runge–Kutta methods Jacobian-free for 1-D conservation laws through the compact approximate Taylor procedure, proves consistency order min(2p, q), and finds by von Neumann analysis critical CFL numbers that the method-of-lines stability region fails to predict."
resource: "doi:10.1007/s10915-021-01753-z"
source_kind: paper
authors: [Chouchoulis J., Schütz J., Zeifang J.]
year: 2022
venue: "J. Sci. Comput. 90:96"
local_file: "/home/stefano/papers/mosaic/ode-integration/2022_Crossref_Journal_of_Scientific_Computing_Chouchoulis_Jacobian-Free_Explicit_Multiderivative_RungeKutta_Methods_fo.pdf"
tags: [multiderivative, lax-wendroff, explicit, stability, hyperbolic-conservation-laws]
timestamp: 2026-10-20T16:00:00Z
---

# Summary

The paper makes explicit [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)
(MDRK) methods practical for 1-D hyperbolic conservation laws $w_t+f(w)_x=0$
by removing analytic flux Jacobians. An MDRK scheme needs the higher time
derivatives of the right-hand side. For a PDE, the Cauchy–Kowalevskaya
(Lax–Wendroff) procedure turns them into nested space derivatives involving
$f'$, $f''$, and so on, which soon become intractable. The authors adopt the
compact approximate Taylor (CAT) procedure of Carrillo and Parés, built on
the approximate Lax–Wendroff procedure of Zorío, Baeza and Mulet. CAT
approximates $\partial_t^{k-1}f(w)$ at each interface recursively, by local
finite differences in time of the flux at Taylor-predicted states, using
only evaluations of $f$. The same Jacobian-free device underlies
[Lax–Wendroff flux reconstruction](/methods/lax-wendroff-flux-reconstruction.md).
Inserting these approximations into the stage and update fluxes of an
$r$-derivative, $s$-stage, order-$p$ MDRK scheme gives the conservative
MDRKCAT family, written $r$DRKCAT$p$-$s$.

Theorem 1 proves consistency order $\min(2\mathsf p,p)$, where $2\mathsf p$
is the order of the $(2\mathsf p+1)$-point centred stencil, so
$\mathsf p=\lceil p/2\rceil$ is the efficient choice. For linear advection,
MDRKCAT reduces to an MDRK–Lax–Wendroff scheme. A
[von Neumann stability analysis](/definitions/von-neumann-stability-analysis.md)
gives critical CFL numbers between 0.2300 (3DRKCAT7-3) and 1.4718
(2DRKCAT4-2), against 1 for the original CAT method. Even numbers of
derivatives are more stable. The [stability function](/definitions/stability-function.md)
of the ODE scheme predicts these numbers badly: "a method of lines (MOL)
viewpoint is inadequate".

Smooth tests confirm the design orders: [Burgers](/benchmarks/burgers-equation.md)
with two initial data, Buckley–Leverett, and 1-D Euler density advection and
a nonlinear Euler problem. CAT with large $\mathsf p$ diverges before shocks
form; the MDRKCAT schemes do not. Accuracy is comparable to DG with
[SSP Runge–Kutta](/methods/strong-stability-preserving-runge-kutta.md). A
new four-derivative, two-stage, sixth-order method 4DRK6-2 is constructed.
[ADER](/methods/ader-time-integration.md) is cited as the main family of
high-order Lax–Wendroff methods.

# Version read

arXiv:2107.06633v1 [math.NA], 14 July 2021, Springer "Noname manuscript"
template, 26 pages, all read. This is the arXiv preprint, not the version
of record (J. Sci. Comput. 90:96), although the archive filename says
"Crossref_Journal_of_Scientific_Computing". The page-1 title differs from
the published one only in capitalization and the dash. Section, equation
and table numbers on this page are those of arXiv v1.

# Key claims

Registry notation: the ODE is $y'=f(y)$ (source $\Phi$), with
$\dot f=f'(y)f(y)$ and in general $\frac{d^{k-1}}{dt^{k-1}}f(y)$ (source
$\Phi^{(k-1)}$); $Y_l$ are stage values (source $y^{n,l}$); $p$ is the
classical order (source $q$); $h$ is the step (source $\Delta t$); $\nu$ is
the Courant number (source $\sigma$). Page-local: the PDE unknown $w$ and
flux $f(w)$ of the conservation law, the number of derivatives $r$, the
stencil half-width $\mathsf p$ (source $p$), the wave number $\kappa$ and
the amplification factors $g$.

1. The Lax–Wendroff route to second time derivatives already gives
   $w_{tt}=2f'(w)f''(w)w_x^2+f'(w)^2w_{xx}$ for a scalar flux, which shows
   why exact flux derivatives become "very tedious" (§1, Eq. (4)).
   **Derived**
2. Multiderivative schemes have been studied since the early 1940s but
   rarely used, "most likely due to the necessary cumbersome calculation of
   flux derivatives" (§1, citing [30]). **Stated**
3. Explicit MDRK ($r$DRK$p$-$s$) follows Seal, Güçlü and Christlieb [30,
   Def. 2]; Taylor methods are the case $s=1$, $a^{(k)}_{11}=0$,
   $b^{(k)}_1=1/k!$ (§2, Def. 1, Remark 2). **Stated**
4. The fully discrete algorithm "seems to have a multistep flavour" but is
   not multistep, so variable steps are admissible; shown with
   $h_n=\nu\Delta x/\max_i|\lambda^n_{\mathrm{eig},i}|$ (§2, Remark 1; §6).
   **Shown**
5. In MDRKCAT only one time derivative is converted into a space derivative
   (Eq. (6), cf. Eq. (3)); the remaining $\partial_t^{k-1}f$ are approximated
   by CAT (§3). **Derived**
6. MDRKCAT is conservative: $w^{n,l}_i=w^n_i-\frac{h}{\Delta x}(F^{n,l}_{i+1/2}-F^{n,l}_{i-1/2})$,
   with interface fluxes built from the half-way operators $\Lambda^{(0)}$
   (§3.2, Eqs. (17)–(18)). **Derived**
7. Theorem 1: the consistency order of explicit $r$DRKCAT$p$-$s$ is
   $\min(2\mathsf p,p)$ on the stencil $\{i-\mathsf p,\dots,i+\mathsf p\}$,
   assuming $f,w\in C^\infty$ and $h=O(\Delta x)$ (§4, Thm. 1, Lemmas 1–4).
   **Proved**
8. The efficient choice is $\mathsf p=\lceil p/2\rceil$, so the scheme name
   omits $\mathsf p$ (§4, Remark 6). **Stated** (follows from Thm. 1)
9. The original CAT scheme reduces linearly to high-order Lax–Wendroff and
   is stable under CFL 1 for linear equations ([3, Thm. 1], recalled in §5).
   **Stated**
10. Theorem 2: for $f(w)=\alpha w$, MDRKCAT reduces to the "MDRK-LW scheme"
    (Eq. (20)) with centred approximations $P^{(k)}$ of the $k$-th space
    derivative (§5). **Stated** (proof "similar to [3, Theorem 1]", omitted)
11. Proposition 1: the von Neumann amplification factors satisfy the
    recurrence (21), with symbols
    $\mathrm P^{(k)}(\kappa)=\sum_{j=-\mathsf p}^{\mathsf p}\delta^k_{\mathsf p,j}e^{\mathrm ij\kappa\Delta x}$
    (§5, Eqs. (21)–(22)). **Derived**
12. Critical CFL numbers (bisection on $\nu$, $\max|g|$ over 1000 values of
    $\kappa\in[-\pi,\pi]$, $\Delta x=1$): 2DRKCAT3-2 1.2954, 2DRKCAT4-2
    1.4718, 2DRKCAT5-3 1.0619, 3DRKCAT5-2 0.4275, 3DRKCAT7-3 0.2300,
    4DRKCAT6-2 0.8563 (§5, Table 2). **Shown**
13. Two-derivative schemes are more stable than the original CAT (CFL 1);
    three- and four-derivative ones are less stable (§5). **Shown**
14. CAT-type (Taylor) schemes with odd $r$: $r=1$ is forward-time
    central-space and unconditionally unstable; odd $r>1$ gives CFL numbers
    below one (§5). **Stated**
15. "A method of lines (MOL) viewpoint is inadequate": by the ODE stability
    regions (Fig. 1) 3DRK7-3 would look most stable, yet in the fully
    discrete analysis the even-derivative schemes are better. The fully
    discrete factor is not $R(-\nu\mathrm P^{(1)})$ because
    $\mathrm P^{(i)}\mathrm P^{(j)}\ne\mathrm P^{(i+j)}$ (§5). **Shown**
16. Even numbers of derivatives give better stability than odd ones, as
    observed for the original CAT method (§5). **Shown**
17. MDRK has two free parameters (derivatives and stages), Taylor methods
    one; both strongly affect stability (§5). **Stated**
18. Except for 3DRK5-2 and 4DRK6-2, the stability regions of the six MDRK
    schemes contain parts of the imaginary axis (Remark 3, Fig. 1).
    **Shown** (plot)
19. Burgers, $w_0=\frac14\cos(\pi x)$ on $[0,2]$, $T_{\mathrm{end}}=0.8$,
    $\nu=0.5$: all expected orders are reached, $2\mathsf p$ for CAT-$\mathsf p$
    ($\mathsf p=1,\dots,6$) and at least $p$ for MDRKCAT. 2DRKCAT5-3,
    3DRKCAT5-2 and 3DRKCAT7-3 do better than expected because $2\mathsf p>p$
    and spatial errors dominate at large $h$ (§6.1, Fig. 2). **Shown**
20. CAT-$\mathsf p$ with $\mathsf p=4,5,6$ diverges for large $h$ "well
    before shocks are formed", in regions of large $|w_0'|$, despite linear
    CFL-1 stability; "the MDRKCAT methods used in this work do not suffer
    this fate" (§6.1, Fig. 2). **Shown**
21. Burgers with $w_0=\frac14e^{\cos(\pi x)+\sin(\pi x)}$,
    $T_{\mathrm{end}}=0.3$: similar behaviour; 3DRKCAT7-3 is "driven back
    faster to order 7" (§6.1, Fig. 3). **Shown**
22. Buckley–Leverett, $T_{\mathrm{end}}=0.1$, $\nu=0.5$: all schemes
    converge as expected (§6.2, Fig. 4). **Shown**
23. Euler density advection ($\rho_0=1+0.3\sin\pi x$, $u=p=1$, $[0,4]$,
    $T_{\mathrm{end}}=0.8$, $\nu=0.5$): expected orders from the coarsest
    meshes (§6.3, Fig. 5). **Shown**
24. Smooth nonlinear Euler ($T_{\mathrm{end}}=0.2$, $\nu=0.15$, DG
    reference): all expected orders; the error saturates near $2\cdot10^{-11}$,
    the reference accuracy. At $\nu=0.5$, 3DRKCAT7-3 with $\mathsf p=4$
    diverged on 8 to 64 cells (§6.3, Fig. 7). **Shown**
25. MDRKCAT reaches its design order only gradually under refinement,
    whereas DG-P3/P4 with SSP-RK4 ($\nu=0.1$) reach it from 32 to 64 cells.
    The authors attribute this to MDRKCAT approximating $\partial_t^{k-1}f$
    from nodal data, while DG uses the exact $f$ at interfaces and several
    quadrature points per cell (§6.3). **Shown** / **Stated**
26. The $r$DRKCAT$p$-$s$ schemes "compare well with a state-of-the-art DG
    solver in terms of accuracy" (§6.3, §7). **Shown** (accuracy per cell
    only; no timings)
27. A new four-derivative, two-stage, sixth-order MDRK, 4DRK6-2, is
    constructed (App. A, Table 8). Its stability function is
    $\sum_{k=0}^6z^k/k!+z^7/6480+z^8/77760$ (Fig. 1). **Derived** (no order
    verification printed; the stability function recomputed from the tableau
    agrees, *(compiler check, not in the sources)*)
28. Odd-derivative MDRK schemes "seem less adequate in conjunction with the
    CAT algorithm", because the underlying Lax–Wendroff scheme uses centred
    differences only (§7). **Stated** (interpretation of Table 2)

# Printed slips

- Table 7 (3DRK7-3), row 3 of the $a^{(3)}$ block: printed
  "$c_2^3/6-a^{(3)}_{32}$" (checked visually at 300 dpi). In the
  Taylor-plus-last-derivative form of App. A the row sum of $a^{(3)}_{3j}$
  should be $c_3^3/6$, so $c_3^3/6-a^{(3)}_{32}$ is likely meant. Not checked
  against [21].
- Fig. 2 caption: "The 2DRKCAT5-3, 3DRKCAT5-2 and 4DRKCAT6-2 schemes behave
  in a very alike manner"; the text names 2DRKCAT5-3, 3DRKCAT5-2 and
  3DRKCAT7-3 as behaving better than expected.
- Lemma 2 uses $\delta_{s,k}$ (Kronecker), clashing with the
  finite-difference coefficients $\delta^k_{\mathsf p,j}$.
- Lemma 1 asserts $O(\Delta x^{2\mathsf p})$ while its proof ends with
  $O(\Delta x^{2\mathsf p-k+1})$ per term; the claim follows only after
  multiplying by $h^{k-1}$ under the assumption $h=O(\Delta x)$, which the
  proof leaves implicit. Lemma 4 covers $k\le2\mathsf p-1$; the general
  theorem implicitly needs $r\le2\mathsf p$ (satisfied by all schemes used).
- Theorem 1 proof: "the Runge-Kutta update is an integration scheme of
  order $q+1$", meaning a local truncation error $O(h^{p+1})$.
- Typos: "follwing" (p. 11), "it's own local stencil" (p. 21), "conjuction"
  (p. 22).
- Ref. [31] has no pages ("SIAM Journal on Numerical Analysis, 40, 02
  2002").

# Notation map

| Chouchoulis et al. (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $y'=\Phi(y)$ | $y'=f(y)$ | autonomous ODE; the source calls $\Phi$ "flux function" |
| $\Phi'(y)\Phi(y)$; $\frac{d^{k-1}}{dt^{k-1}}\Phi$, $\Phi^{(k-1)}$ | $\dot f$; $\frac{d^{k-1}}{dt^{k-1}}f(y)$ | total time derivatives along the solution |
| $w_t+f(w)_x=0$ | — | PDE unknown and flux, page-local; **$f$ collides with the registry right-hand side** |
| $y^{n,l}$, $w^{n,l}_i$ at $t_n+c_l\Delta t$ | $Y_l$ at $t_n+c_lh$ | stage values |
| $a^{(1)}_{l\nu}$, $a^{(2)}_{l\nu}$, $a^{(k)}_{l\nu}$; $b^{(k)}_l$ | $a_{ij}$, $\dot a_{ij}$, $a^{(k)}_{ij}$; $b^{(k)}_i$ | extended Butcher tableau, one block per derivative; strictly lower triangular |
| $q$ | $p$ | classical order of the MDRK scheme; **$q$ collides with the stage order** |
| **$p$** | $\mathsf p$ (page-local) | stencil half-width, spatial order $2\mathsf p$; **collides with the order $p$** |
| $\mathtt r$ | — | number of derivatives, counting $f$ itself (2DRK uses $f$ and $\dot f$) |
| $s$ | $s$ | stages, agrees |
| $\Delta t$, $t_n$; $\Delta t^n$ | $h$, $t_n$; $h_n$ | |
| $\sigma=\alpha\Delta t/\Delta x$, $\sigma^*$ | $\nu$, critical $\nu$ | **$\sigma$ collides with the tree symmetry $\sigma(\tau)$** |
| $\Delta x$, $x_i$ | $\Delta x$ | uniform 1-D grid |
| **$M$** | — | number of cells; **collides with the mass matrix** |
| $R(z)$, $\mathcal R$ | $R(z)$, $\mathcal S$ | stability function and region of the ODE scheme |
| $L_{p,j}$, $\ell_{p,j}$; $P_i$, $Q_i$; $P^{(k)}$, $Q^{(k)}_m$ | — | $(2\mathsf p+1)$- and $2\mathsf p$-point Lagrange bases, interpolants, derivative operators; **$Q$ is not the SDC collocation matrix** |
| $\delta^k_{p,j}$, $\gamma^{k,m}_{p,j}$, $\lambda^{k-1}_{p,j}$ | — | centred, off-centre and half-way difference coefficients; **$\gamma$ and $\lambda$ collide with registry symbols** |
| $\Lambda^{(k-1)}$ | — | half-way interpolation operator |
| $\tilde f^{(k-1)}_{i,j}$, $\tilde w^{(m)}_{i,j}$ | — | CAT approximations of $\partial_t^{k-1}f(w)$ and $\partial_t^mw$ |
| $F^{n,l}_{i+1/2}$, $F^n_{i+1/2}$ | — | stage and update numerical fluxes; **not the elementary differential $F(\tau)$** |
| $g^{n,l}(\kappa)$, $g(\kappa)$, $\mathrm P^{(k)}(\kappa)$ | — | stage and step amplification factors, Fourier symbol of $P^{(k)}$ |
| $\alpha$ | — | advection speed; **not Shu–Osher $\alpha_{ij}$** |

# Reference list

The paper prints 36 references in numbered, alphabetical style. All are
merged complete into the [bibliography](/bibliography.md) with `citedby`
chouchoulis-2022. Refs. [4], [10] and [31] print no pages. Ref. [11] is the
arXiv version (arXiv:2102.11939) of the later Gottlieb et al. paper and is
kept as a preprint entry. Ref. [28] is a CMAT preprint (UP-21-01) with URL;
ref. [20] is MathWorks software with a corporate author; refs. [1] and [7]
are edited volumes. The two Dumbser 2008 items take suffixes in printed
order ([8], [9]); the first author of [21], Ökten Turacı, gives the key
`oktenturaci-2017`. No DOIs are printed.

# Pages created or updated

Chunk 5 (2026-10-20). This source is cited on:

* [ADER as a time integrator](/methods/ader-time-integration.md)
* [Burgers equation](/benchmarks/burgers-equation.md)
* [Lax–Wendroff flux reconstruction (single-stage Taylor time stepping)](/methods/lax-wendroff-flux-reconstruction.md)
* [Linear advection equation](/benchmarks/linear-advection-equation.md)
* [Multiderivative Runge–Kutta methods and the backward derivative condition](/methods/multiderivative-runge-kutta.md)
* [Stability function, stability polynomial and stability region](/definitions/stability-function.md)
* [Strong-stability-preserving (SSP) Runge–Kutta methods](/methods/strong-stability-preserving-runge-kutta.md)
* [Von Neumann (Fourier) stability analysis of fully discrete schemes](/definitions/von-neumann-stability-analysis.md)
