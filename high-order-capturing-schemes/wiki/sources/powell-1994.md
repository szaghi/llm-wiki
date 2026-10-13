---
type: Source
title: "Powell (1994) — An Approximate Riemann Solver for Magnetohydrodynamics (That Works in More than One Dimension)"
description: "ICASE report deriving the eight-wave Roe-type MHD solver: the primitive Jacobian of the full eight-equation system with a variable normal field is singular, Powell replaces it by a matrix with an eighth 'divergence' wave moving at the flow speed and carrying only normal-field jumps, which in conservative variables equals source terms proportional to ∇·B in momentum, induction and energy, so ∇·B/ρ is advected; first order, tested on a Brio–Wu tube rotated by 45°."
resource: "https://ntrs.nasa.gov/citations/19940028527"
source_kind: report
authors: [Powell K.G.]
year: 1994
venue: "ICASE Report 94-24 (NASA CR-194902)"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1994-ICASE-Powell-19940028527.pdf"
tags: [mhd, riemann-solver, eight-wave, divergence-free, source-terms, eigenvectors]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The report builds a Roe-type approximate Riemann solver for ideal MHD
from the full $8\times8$ system, with the normal field $B_x$ not held
constant; earlier upwind MHD work used the $7\times7$ system with $B_x$
constant. The primitive-variable Jacobian of the eight-equation system is
singular: its row for $B_x$ is zero, which gives a non-physical zero
eigenvalue. Powell replaces it with a modified matrix that keeps the seven
usual waves and adds an eighth "divergence" wave moving at $v_x$ and
carrying only jumps in $B_x$ (§2, eqs. 8–13). In conservative variables the
modification equals adding a source proportional to $\nabla\cdot\mathbf B$
to the momentum, induction and energy equations (eq. 14). With that source,
$\nabla\cdot\mathbf B/\rho$ is passively advected, whereas the original
system freezes $\nabla\cdot\mathbf B$ in place (eqs. 16–17). Multi-D MHD
then runs on a collocated grid with no staggering and no projection. The
implementation is first order in space and time, with an arithmetic-mean
interface state and Roe–Balsara eigenvector normalization. It is tested
on a Brio–Wu shock tube rotated by 45° to the grid, which agrees with the
unrotated run except in the normal velocity and normal field (§3).

# Key claims

1. **Discrete constraint in multi-D** (§1, eq. 5). The discrete analogue of
   $\nabla\cdot\mathbf B = 0$ is a zero sum of normal field times face
   length over a cell's faces. A jump in the normal field across one face is
   therefore allowed if the other faces balance it, while a 1D solver
   assumes it continuous and needs a separate update for that component
   (p. 3).
2. **The usual remedies** (§1, p. 3): a projection (Poisson solve),
   non-collocated (staggered) variables, a vector potential. The eight-wave
   solver, which updates all of $\mathbf B$, is offered instead.
3. **Seven-wave eigenvalues** (§1, p. 2): entropy $v_x$, Alfvén
   $v_x \pm c_A$ with $c_A = B_x/\sqrt\rho$, fast and slow $v_x \pm c_{f,s}$
   with
   $c_{f,s}^2 = \tfrac12\left(\frac{\gamma p + \vert\mathbf B\vert^2}{\rho} \pm \sqrt{\left(\frac{\gamma p + \vert\mathbf B\vert^2}{\rho}\right)^2 - 4\frac{\gamma pB_x^2}{\rho^2}}\right)$;
   units without $4\pi$ or $\mu_0$, $E = \frac{p}{\gamma-1} + \frac12\rho\vert\mathbf v\vert^2 + \frac12\vert\mathbf B\vert^2$
   (eq. 3).
4. **Singular primitive Jacobian** (§2, eqs. 6–8). With primitive variables
   $(\rho, v_x, v_y, v_z, B_x, B_y, B_z, p)$, the $x$-Jacobian has a zero
   fifth row, so a zero eigenvalue, "clearly non-physical"; the
   corresponding mode "will be undamped". Its $\partial_xB_x$ column is
   $(0, -B_x/\rho, -B_y/\rho, -B_z/\rho, 0, -v_y, -v_z, (\gamma-1)\mathbf v\cdot\mathbf B)^T$
   (eq. 8, read at 250 dpi).
5. **The modified matrix** (§2, p. 4, eq. 9). Four criteria: the seven 1D
   eigenpairs unchanged; the new eigenvalue $v_x$; new eigenvectors that
   "make sense"; reduction to the seven-wave problem when $B_x$ is
   constant. The matrix, found "given some patience and some facility with
   Maple's symbolic manipulation capabilities", is the Jacobian with the
   whole $\partial_xB_x$ column zeroed except $v_x$ on the diagonal.
6. **Eight-wave eigensystem** (eqs. 10–13). Entropy, Alfvén, fast and slow
   eigenvectors with zero $B_x$ entries, unnormalized (the fast/slow ones
   singular where $\rho c_{f,s}^2 = B_x^2$), and the divergence wave
   $\lambda = v_x$ with left and right eigenvectors the unit vector of the
   $B_x$ entry (eq. 13). The first seven carry no $B_x$ jump; the eighth
   only that jump, with zero strength when $B_x$ is constant (p. 6). In
   practice "the eigenvectors are properly normalized to avoid difficulties
   associated with coinciding wave speeds" (Roe–Balsara; p. 8).
7. **The source term** (eq. 14, page image p. 6). Conservative MHD with
   the Maxwell-stress momentum flux
   $\rho\mathbf v\mathbf v + \mathsf I\left(p + \tfrac12\vert\mathbf B\vert^2\right) - \mathbf B\mathbf B$
   and the right-hand side
   $$-\begin{pmatrix}0\\ \mathbf B\\ \mathbf v\\ \mathbf v\cdot\mathbf B\end{pmatrix}\nabla\cdot\mathbf B$$
   for $(\rho, \rho\mathbf v, \mathbf B, E)$: momentum
   $-\mathbf B\,\nabla\cdot\mathbf B$, induction $-\mathbf v\,\nabla\cdot\mathbf B$,
   energy $-(\mathbf v\cdot\mathbf B)\,\nabla\cdot\mathbf B$, none in
   continuity (sign checked on the page image). Italicized: "*the source
   term that must be added to Equation 2 is proportional to ∇·B*"; it adds
   only terms that vanish at the PDE level, so "the deviations from
   conservation will be very small". Brackbill & Barnes are cited **only for
   the momentum equation**: "solving the momentum equation in
   non-conservative form can remove instabilities related to non-zero ∇·B
   [1]" (pp. 6–7). The name "Godunov" does not occur.
8. **The expanded form** (eq. 15, page image p. 7). Expanding the
   conservative equations gives, for momentum,
   $\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v) + \nabla\left(p + \tfrac12\vert\mathbf B\vert^2\right) - (\mathbf B\cdot\nabla)\mathbf B - \underline{\mathbf B\,\nabla\cdot\mathbf B} = 0$,
   and for induction and energy the analogous forms with underlined
   $-\mathbf v\,\nabla\cdot\mathbf B$ and $-(\mathbf v\cdot\mathbf B)\nabla\cdot\mathbf B$.
   The underlined terms "are exactly the same as the source term defined
   above", which "simply acts to remove the terms proportional to ∇·B that
   appear in Equation 2". Powell does not project any term on $\mathbf B$.
9. **Divergence evolution** (eqs. 16–17, pp. 7–8). Original system:
   $\partial_t(\nabla\cdot\mathbf B) = 0$. Modified system:
   $\partial_t(\nabla\cdot\mathbf B) + \nabla\cdot(\mathbf v\,\nabla\cdot\mathbf B) = 0$,
   so "the quantity ∇·B/ρ is treated as a passive scalar", "clearly the
   more numerically stable": "any local ∇·B that is created is convected
   away".
10. **Implementation** (p. 8). Roe-type solver with wave strengths and
    speeds from the eigenvectors and eigenvalues above; Roe–Balsara
    normalization; interface state the **arithmetic mean** of left and
    right states ("although a Roe average does exist for the ideal MHD
    equations [4]", a private communication from Roe); source "calculated
    in each cell, and added to the residual", with the discrete
    $\nabla\cdot\mathbf B$ not stated. "The resulting code is first order in
    space and time."
11. **Conclusions** (§4, p. 12). "Only one-eighth of a Riemann solver": the
    eighth wave "arises only in multi-dimensional problems" and "plays the
    very important role of stabilizing the numerical method with respect to
    the small amounts of ∇·B generated".

# Tests

* **Rotated Brio–Wu shock tube** (§3, Fig. 2, pp. 8–9). Unrotated: left
  $\rho = 1$, $p = 1$, $B_x = 3/4$, $B_y = 1$; right $\rho = 1/8$,
  $p = 1/10$, $B_x = 3/4$, $B_y = -1$; $\gamma = 2$. Rotated by 45°: left
  $B_x = -1/(4\sqrt2)$, $B_y = 7/(4\sqrt2)$; right $B_x = 7/(4\sqrt2)$,
  $B_y = -1/(4\sqrt2)$, so the normal field is $3/4$ and the tangential
  $\pm1$ (reader's check). Periodic along $y$ = const (unrotated) and along
  $x + y$ = const (rotated). 600 and 1200 cells in $x$ ($y$ extent not
  stated); $\Delta t/h = 0.2$, "approximately" CFL 0.8 unrotated; 100 and
  200 steps. Rotated results plotted with $x$ scaled by $\sqrt2$. Final time
  and domain not stated. First order.
* **Findings** (Figs. 3–8). Density, pressure, normal and tangential
  velocity and tangential field, rotated against unrotated on the fine
  grid, are "nearly indistinguishable for all but the normal component of
  velocity"; "the errors in $u_n$ are balanced by errors in the
  magnetic-field component normal to the original discontinuity". The
  normal field, which should be 0.75, is wrong by "a few percent" on the
  coarse grid, "reduced as the grid is refined" (Fig. 8, plot range
  0.735–0.795). No norms, rates or divergence measurements
  ([grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md);
  [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md)).

# Notation map

| Powell (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf u = (u, v, w)$ | $\mathbf v = (v_x, v_y, v_z)$ | **collision**: registry $u$ is the conserved state |
| $\rho$, $p$, $E$, $\gamma$, $\mathbf B$ | same | no $4\pi$ or $\mu_0$ |
| $\mathbf W = (\rho, u, v, w, B_x, B_y, B_z, p)$ | $\mathbf W$ extended by $\mathbf B$ | |
| $A_p$, $B_p$, $C_p$ | words (primitive-variable Jacobians) | **collision**: $A(u)$, field $\mathbf B$ |
| $A'_p$ | words (Powell's modified Jacobian) | |
| $\lambda$, $\tilde\ell$, $\tilde r$ | $\lambda^{(p)}$, $\ell^{(p)}$, $r^{(p)}$ | primitive, unnormalized |
| $c_a$, $c_f$, $c_s$ | $c_A$, $c_f$, $c_s$ | |
| $a$ (eq. 10, undefined) | $c$ | evidently the sound speed |
| $\mathbf I$ | $\mathsf I$ | |
| $B_n$, $B_t$, $u_n$, $u_t$ | $B_n$, words, $v_n$, words | relative to the original discontinuity |
| $\Delta t/\Delta x$ | $\Delta t/h$ | |
| $\mathbf B\cdot\nabla\mathbf B$ | $(\mathbf B\cdot\nabla)\mathbf B$ | |

# Pages created or updated

* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md) (batch-18 block: the source terms as printed, eqs. 13–17, the attribution to Brackbill & Barnes; a bullet on the plus side of the Open parallel-force entry).
* Updated [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md) and [Brio–Wu shock tube](/benchmarks/brio-wu-shock-tube.md) (sent to the compiler; not written here).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1994-ICASE-Powell-19940028527.pdf`.
   * **Version read.** NTRS scan of the printed report (OCR text layer, 18
     PDF pages: cover, 13 numbered pages, SF-298), dated April 1994, marked
     "Final Report" and "Submitted to the Journal of Computational Physics"
     (SF-298 box 11). Not a later journal version: `powell-1997` and
     `powell-1999` in the bibliography are other works.
   * **Identity.** No DOI exists (ICASE/NASA contractor report): resource is
     the NTRS record, checked on the NTRS API (citation 19940028527): title
     "An approximate Riemann solver for magnetohydrodynamics (that works in
     more than one dimension)", author Powell, Kenneth G., publication date
     1994-04-01, report numbers ICASE-94-24, NASA-CR-194902, NAS
     1.26:194902, AD-280296, contract NAS1-19480. The word "Actually" in
     the title as printed by balsara-2009 is not on the cover, the title
     page or the SF-298.
   * **How it was read.** Text layer for prose; page images at 110 dpi for
     every equation, eqs. 8 and 10–12 again at 220–250 dpi. Nothing was
     illegible.
   * **Recorded as printed** (reader's reading).
     - Eq. 14 prints the momentum flux "$-\mathbf B n\mathbf B$", a stray
       $n$ (eq. 2 prints $-\mathbf B\mathbf B$).
     - Eq. 10 uses $a$ without definition (evidently the sound speed).
     - "Zachary and Colella [?]" (p. 1) and "ala Roe [2, ?]" (p. 2) are
       unresolved LaTeX citations with no list entry.
     - SF-298 box 15 prints 15 pages; Dedner et al. print the date "8 April
       1994", the PDF only "April 1994".
     - Not stated: domain length, $y$ extent, final time, the discrete
       $\nabla\cdot\mathbf B$ of the cell source.
   * **Reference list:** 7 entries, all merged. Woodward & Dai, "A Riemann
     solver for ideal magnetohydrodynamics" (J. Comput. Phys., to appear),
     is identified by title with `dai-1994` (Dai & Woodward 1994), not the
     homonymous key `woodward-1994`; Roe & Balsara, "Notes on the
     eigensystem of magnetohydrodynamics" (printed J. Comput. Phys., to
     appear) is `roe-1996` (SIAM J. Appl. Math.); Roe's private
     communication is `roe-1994`; Brackbill & Barnes is printed with the
     title "The effect of nonzero ∇·B …". Bibliography: 3380 entries.
