---
type: Source
title: "Dedner et al. (2002) — Hyperbolic Divergence Cleaning for the MHD Equations"
description: "Origin of GLM divergence cleaning: a scalar ψ couples the divergence constraint to the induction equation through elliptic, parabolic, hyperbolic or mixed operators; the mixed choice transports errors at c_h, set each step to the largest speed the time step admits, and damps them by an exactly integrated source, with c_p fixed by c_p²/c_h = 0.18; the conservative mixed GLM is recommended over the nonconservative EGLM and Powell source terms on four 2D tests on triangles."
resource: "doi:10.1006/jcph.2001.6961"
source_kind: paper
authors: [Dedner A., Kemm F., Kröner D., Munz C.-D., Schnitzer T., Wesenberg M.]
year: 2002
venue: "J. Comput. Phys. 175:645–673"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2002-JCP-Dedner-101006jcph20016961.pdf"
tags: [mhd, divergence-cleaning, verification, benchmark]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper couples the constraint $\nabla\cdot\mathbf B = 0$ to the
induction equation through a scalar $\psi$, a generalized Lagrange
multiplier (GLM) carried over from GLM–Maxwell solvers, and studies
elliptic, parabolic, hyperbolic and mixed hyperbolic/parabolic choices of
the linear operator that links $\psi$ to $\nabla\cdot\mathbf B$ (§2). The
mixed choice gives a telegraph equation for $\nabla\cdot\mathbf B$ and
$\psi$: errors travel at a finite speed $c_h$ and are damped by a source in
the $\psi$ equation alone, so mass, momentum, field and energy stay in
conservation form. A variant derived from GLM–Maxwell (EGLM) adds
nonconservative sources to momentum and energy (eq. 24). §3 proves
hyperbolicity; §4 implements the correction as an add-on to any MHD flux on
unstructured triangular grids; §5 compares mixed GLM, mixed EGLM,
hyperbolic GLM, Powell's source terms and no correction on four 2D tests;
mixed GLM is recommended (§6). See
[GLM divergence cleaning](/methods/glm-divergence-cleaning.md).

# Key claims

In the [registry](/notation.md) notation, with the paper's operator
$\mathcal D(\psi)$ written in words.

1. **GLM system** (§2, eqs. 4–5). The induction equation becomes
   $\partial_t\mathbf B + \nabla\cdot(\mathbf v\mathbf B - \mathbf B\mathbf v) + \nabla\psi = 0$
   and the constraint a linear differential equation in $\psi$ forced by
   $\nabla\cdot\mathbf B$. For smooth solutions $\nabla\cdot\mathbf B$ and
   $\psi$ obey the same equation whatever the operator (eqs. 10–11).
2. **Elliptic correction** (eq. 12, p. 649). A Poisson equation for $\psi$
   with source $\nabla\cdot\mathbf B/\Delta t$ and the projection of
   Brackbill & Barnes; rejected as nonlocal.
3. **Parabolic correction** (eqs. 13–14). $\psi = -c_p^2\nabla\cdot\mathbf B$;
   equivalent to adding $c_p^2\nabla(\nabla\cdot\mathbf B)$ to the induction
   equation (Marder-type). An explicit version is limited by its stability
   condition on $c_p$; not used.
4. **Hyperbolic correction** (eqs. 15–16). A wave equation for $\psi$:
   errors are carried to the boundary at speed $c_h$; the whole system is
   hyperbolic.
5. **Mixed correction** (eqs. 17–19). A telegraph equation; the constraint
   becomes
   $$\partial_t\psi + c_h^2\nabla\cdot\mathbf B = -\frac{c_h^2}{c_p^2}\psi ,$$
   the registry's GLM equation. The damping is a source, so it puts no
   stability restriction on $c_p$; $c_p \to \infty$ recovers the hyperbolic
   case. With the hyperbolic or mixed correction the system is hyperbolic
   and conserves $\rho$, $\rho\mathbf v$, $\mathbf B$ and $E$ (p. 650).
6. **EGLM** (§2, eqs. 20–24). From GLM–Maxwell with
   $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$ and (eq. 22)
   $$\mathbf J\times\mathbf B = \nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - (\nabla\cdot\mathbf B)\,\mathbf B .$$
   The EGLM system (eq. 24) adds the source $-(\nabla\cdot\mathbf B)\mathbf B$
   to the momentum equation (24b), writes the induction equation as
   $\partial_t\mathbf B + \nabla\cdot(\mathbf v\mathbf B - \mathbf B\mathbf v + \psi\mathsf I) = 0$
   (24c), adds $-\mathbf B\cdot\nabla\psi$ to the energy equation (24d) and
   keeps the mixed $\psi$ equation (24e). Eq. 22 and the sign of eq. 24b
   were checked by the compiler on the page image (p. 651). Since
   $\mathbf J\times\mathbf B$ is orthogonal to $\mathbf B$, the component
   of the divergence-form force along $\mathbf B$ is
   $+(\nabla\cdot\mathbf B)\vert\mathbf B\vert$ (projection by the compiler;
   the paper does not state it). Disadvantage: nonconservative terms, so
   errors can violate conservation even for divergence-free initial data
   (§3, p. 654).
7. **Eigensystem** (§3, eqs. 25–37). In 1D the pair $(B_x, \psi)$
   decouples; the eigenvalues are the seven MHD speeds plus $\pm c_h$, and
   only the $\pm c_h$ waves carry changes of $B_x$ or $\psi$; they are
   distinct from the MHD eigenvalues "if $c_h$ is sufficiently large"
   (p. 653), and "extend the idea of a divergence wave" of Powell. EGLM has
   the same eigenvalues. Powell's form (eq. 36: momentum
   $-(\nabla\cdot\mathbf B)\mathbf B$, induction $-(\nabla\cdot\mathbf B)\mathbf v$,
   energy $-(\nabla\cdot\mathbf B)\,\mathbf v\cdot\mathbf B$) instead adds an
   eigenvalue $v_x$: errors are advected with the flow.
8. **Galilean-invariant variant** (eq. 38). Adding
   $-(\nabla\cdot\mathbf B)\mathbf v$, $-(\nabla\cdot\mathbf B)\,\mathbf v\cdot\mathbf B$
   and $-\mathbf v\cdot\nabla\psi$ shifts the cleaning speeds to
   $v_x \mp c_h$, but the system "is no longer conservative".
9. **Scheme** (§4, eqs. 39–43). First-order finite volumes on unstructured
   triangles with rotated 1D fluxes; second order "formally" by linear
   reconstruction and Runge–Kutta. The time step (eq. 40) uses the Courant
   number $\nu \in (0,1)$, the triangle heights and the largest
   $\vert v_n\vert + c_f$; **$c_h$ does not enter it**.
10. **Choice of $c_h$** (p. 656). $c_h$ equals $\nu$ times the smallest
    triangle height divided by $\Delta t$, "the maximal value which is
    compatible with (40)", recomputed every step and uniform in space.
11. **Riemann problem for $(B_x, \psi)$** (eq. 42). The interface values are
    $B_{x,m} = \tfrac12(B_{x,l} + B_{x,r}) - \tfrac{1}{2c_h}(\psi_r - \psi_l)$
    and $\psi_m = \tfrac12(\psi_l + \psi_r) - \tfrac{c_h}{2}(B_{x,r} - B_{x,l})$,
    with flux $(\psi_m,\ c_h^2B_{x,m})$; any 1D MHD flux is then evaluated
    with $B_{x,m}$ as its normal field (eq. 43). The fluxes used are the
    Dai–Woodward "simple" flux and MHD–HLLEM.
12. **Damping step and $c_p$** (eqs. 44–46, p. 657). Operator-split and
    exact, $\psi \leftarrow e^{-\Delta t\,c_h^2/c_p^2}\psi$, "unconditionally
    stable". A constant $c_p$ proved grid- and scheme-dependent; of two
    alternatives (a fixed decay factor per step, or a fixed ratio
    $c_p^2/c_h$) only the ratio is reported, with results "quite independent
    of the grid resolution and the scheme". **$c_p^2/c_h \approx 0.18$** is
    optimal on the peak-in-$B_x$ test, "independent of the order and the grid
    resolution" (Fig. 2), and is used throughout (§5, p. 661). The ratio has
    the dimension of a length (reader's remark; not discussed in the paper).
13. **Boundary conditions for $\psi$** (p. 658). Same as $\rho$, homogeneous
    Dirichlet, or non-reflecting (eq. 49); only the first is shown, and mixed
    GLM shows "no significant dependency" on the choice.
14. **Analysis** (Appendix, Theorems A.1–A.2, 1D, proofs omitted). The
    parabolic correction decays a perturbation like $t^{-1/2}$; the
    hyperbolic correction removes a perturbation supported in $[0,1]$
    exactly for $t \ge 1/c_h$.
15. **Recommendation** (§6). Mixed GLM: robust, smallest divergence errors,
    no loss of conservation; cost one linear $2\times2$ Riemann problem plus
    a scalar source; applicable "on arbitrary grids in 2D and 3D".
16. **Case against constrained transport** (§1, p. 646). CT schemes are
    "restricted to structured grids and require large stencils", and "the
    underlying base scheme is only partially used" (the authors' position).

# Tests

All 2D on triangles, $\nu = 0.3$ (p. 660), second-order Dai–Woodward and
MHD–HLLEM fluxes unless stated, set-ups in Table I (field values carry
$1/\sqrt{4\pi}$, the equations unit permeability). Divergence measured by
the jump of the averaged normal field over each triangle (eqs. 50–54).

1. **Peak in $B_x$** ($\gamma = 5/3$, periodic; domain printed
   "[−0.5, −0.5] × [1.5, 1.5]"). $\rho = 1$, $v_x = v_y = 1$, a quartic
   bump in $B_x$, $B_z = 1/\sqrt{4\pi}$, $p = 6$. Fixes the optimal
   $c_p^2/c_h \approx 0.18$. Powell's terms simply advect the peak; no
   correction creates new extrema; hyperbolic GLM shows wave interactions
   that the damping removes; maximum divergence smallest and nearly equal for
   mixed GLM and EGLM, hyperbolic GLM an order of magnitude below Powell,
   uncorrected worst. With conservation counted (Fig. 9), "mixed GLM ansatz
   is by far the best choice".
2. **1D Riemann problem of Dai & Woodward in 2D** ($\gamma = 5/3$,
   $[-0.5,0.5]\times[-0.25,0.25]$). Left $\rho = 1$, $v_x = 10$, $p = 20$;
   right $\rho = 1$, $v_x = -10$, $p = 1$; $B_x = B_y = 5/\sqrt{4\pi}$.
   First-order runs, cuts against a 1D reference with $h = 0.0002$. Table II
   ($L^1$ error and experimental order, Dai–Woodward flux, 1,024 to
   1,048,576 elements): mixed EGLM 6.44165126 → 0.23998602 (orders 1.064,
   0.873, 0.792, 1.041, 0.976); mixed GLM 6.45517676 → 0.22792806 (1.061,
   0.875, 0.804, 1.069, 1.014); Powell 7.03537990 → 1.84060872 at 65,536
   elements (0.880, 0.622, 0.432), then "No solution" (negative pressures).
   Powell gives wrong intermediate states; uncorrected Dai–Woodward fails on
   all grids; hyperbolic GLM is close to mixed GLM.
3. **MHD shock reflection** (after Aslan & Kammash; $\gamma = 1.4$,
   $[-1,1]\times[-0.5,0.5]$, adaptive grid, $t = 2$). Uncorrected
   Dai–Woodward crashes; Powell's maximum divergence about twice that of
   (E)GLM.
4. **2D MHD Riemann problem** ($\gamma = 5/3$, $[-1,1]^2$, adaptive, to
   $t = 0.25$). Uncorrected and Powell fail to keep $B_y$ constant across a
   shock; (E)GLM divergence errors "at least 50% smaller"; the uncorrected
   and Powell runs need "at least 50% more computational time" (larger
   adaptive grids).
5. **MHD Kelvin–Helmholtz** ($\gamma = 1.4$, $[0,1]\times[-1,1]$,
   periodic, $\rho = 1$, $B_x = 1$, $p = 50$, two shear layers at
   $y = \pm0.5$, $t = 0.5$). Mixed GLM keeps the symmetry; uncorrected is
   distorted and costs 53 % more time. Without nonconservative sources all
   variables are conserved to machine accuracy (except $\rho v_x$ at about
   $10^{-9}$).

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\mathbf u$ | $\mathbf v$ | **collision**: registry $u$ is the state |
| $\mathbf U$ | $u$ | |
| $e$ (total energy density) | $E$ | **collision**: registry $e$ is specific internal energy |
| $\rho$, $p$, $\gamma$, $\mathbf B$ | same | unit permeability |
| $\psi$, $c_h$, $c_p$ | $\psi$, $c_h$, $c_p$ | eq. 19 / 24e is the registry equation |
| $c_a$, $c_f$ | $c_A$, $c_f$ | |
| $c_s$ (slow speed); $a$ | in words; $c_s$ | **collision** |
| $\mathcal D$ | in words | **collision risk** with the Valencia $D$ |
| $c_r = c_p^2/c_h$, $c_d$ | $c_p^2/c_h$; in words | |
| $W$ (primitive vector) | in words | **collision**: $W$ is the Lorentz factor |
| $A(W)$, $B(W)$, $S(U)$ | $A$; in words | **collision**: matrix $B$ vs field $\mathbf B$ |
| $c_{cfl}$ | $\nu$ | |
| $h_{jl}$ | in words | triangle height |
| $\mathbf E$, $\mathbf j$, $\mathbf F_L$ | $\boldsymbol{\mathcal E}$, $\mathbf J$, $\mathbf J\times\mathbf B$ | |
| $\Delta$; $\mathcal I$; $\mathbf B\mathbf B^T$ | $\nabla^2$; $\mathsf I$; $\mathbf B\mathbf B$ | |

# Pages created or updated

* Created this Source page.
* Updated [GLM divergence cleaning](/methods/glm-divergence-cleaning.md):
  the primary source (operators, $c_h$ and $c_p$ choices, EGLM and Powell,
  convergence orders, recommendation).
* Updated
  [constrained transport](/methods/constrained-transport.md) and
  [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md).

# Citations

1. Dedner A., Kemm F., Kröner D., Munz C.-D., Schnitzer T., Wesenberg M.
   (2002), "Hyperbolic divergence cleaning for the MHD equations",
   J. Comput. Phys. 175(2):645–673, doi:10.1006/jcph.2001.6961. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2002-JCP-Dedner-101006jcph20016961.pdf`.
   * **Version read.** The published journal version (received April 3,
     2001; revised October 15, 2001), 29 pp. Not a preprint.
   * **Identity.** Checked on Crossref: title, the six authors, vol. 175,
     issue 2, pp. 645–673, issued 2002-01.
   * **How it was read.** Text layer for prose; eqs. 22, 24, 39, 42 and
     Table I from rendered pages (pp. 651, 655–656, 660); the matrices of
     eqs. 27, 35 and 37 are garbled and not reproduced. Figures 2–9 are
     plots; only the quantitative statements of the text and Table II are
     used.
   * **Recorded as printed.** (a) Eq. 39 prints the edge-sum index as
     "$j = 1$" to 3 ($l$ meant). (b) The peak-in-$B_x$ domain is printed
     "[−0.5, −0.5] × [1.5, 1.5]" and the support of the bump function is not
     printed. (c) The Kelvin–Helmholtz shear profile, a difference of two
     $\tanh$ layers, is printed with an unusual bracketing (not reproduced
     here). (d) Page 1 and refs. 33–35 spell
     the fourth author C.-D. Munz; the bibliography entry carried "C.-T."
     (fixed by the compiler).
   * **Reference list:** 48 printed entries, merged complete. Same first
     author and year follow printed order: `munz-2000` (proceedings, "to
     appear") and `munz-2000-b` (J. Comput. Phys. 161:484); `balsara-1998`
     and `balsara-1998-b` (linearized Riemann problem, ApJS 116:119);
     `toth-1996-b` is Tóth & Odstrčil. Ref. 39 is Ryu, Miniati, Jones &
     Frank (1998), `ryu-1998`. Bibliography: 2407 entries.
