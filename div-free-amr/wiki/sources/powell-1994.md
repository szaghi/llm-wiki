---
type: Source
title: "Powell (1994) — An approximate Riemann solver for magnetohydrodynamics (that works in more than one dimension)"
description: "The ICASE report that introduced the eight-wave scheme: a non-singular modification of the primitive MHD Jacobian found from four eigenstructure criteria, the divergence wave, the source term proportional to ∇·B, and a first-order Roe-type test on a rotated shock tube."
resource: "https://ntrs.nasa.gov/citations/19940028527"
source_kind: report
authors: [Powell K.G.]
year: 1994
venue: "ICASE Report 94-24 (NASA CR-194902)"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1994-ICASE-Powell-19940028527.pdf"
tags: [eight-wave, source-terms, riemann-solver, divergence-wave, mhd]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

Powell observes that the multi-dimensional quasilinear MHD system in
primitive variables has a singular $x$-Jacobian: the row of the normal
field is zero, giving a non-physical zero eigenvalue (§2, eq. 8). Earlier
upwind MHD schemes avoid it by working on the 7×7 system with the normal
field constant ([Brio & Wu (1988)](/sources/brio-wu-1988.md), Zachary–Colella,
Dai–Woodward). In multi-D that is not possible, because the discrete
constraint (eq. 5) allows jumps of the normal field across a face.

He replaces the Jacobian by a non-singular one (eq. 9), found "with Maple"
from four design criteria. The seven classical waves are kept, and an
eighth, "divergence" wave with speed $u$ carries only the jump in the
normal field (eq. 13). In conservative variables the modification is a
source term proportional to $\nabla\cdot\mathbf B$ (eq. 14), which makes
$\nabla\cdot\mathbf B/\rho$ a passive scalar (eq. 17). A first-order
Roe-type code is tested on a 45°-rotated Brio–Wu shock tube (§3): the
results match the unrotated run except for small errors in the normal
velocity and few-percent errors in the normal field that decrease from 600
to 1200 cells.

This report is the chronological origin of the
[eight-wave formulation](/methods/eight-wave.md). It contains no
symmetrizability argument, no Galilean invariance and no entropy law;
those are in [Powell et al. (1999)](/sources/powell-1999.md).

# Key claims

1. **The singular Jacobian** (§2, eqs. 6–8). With primitive variables
   $(\rho,u,v,w,B_x,B_y,B_z,p)$, the fifth row of the $x$-Jacobian
   (eq. 8) is identically zero, so one eigenvalue is 0. Powell calls this
   "clearly non-physical": eigenvalues should be $u$ singly or come in
   pairs symmetric about $u$. It "does not bode well numerically".
2. **Four design criteria** (§2, p. 4): (i) the seven 1D eigenpairs are
   unchanged; (ii) the eighth eigenvalue is $u$, "the only physical choice
   for a single eigenvalue"; (iii) the eighth eigenvectors "make sense";
   (iv) with $B_x$ constant the scheme reduces to the seven-wave problem.
   The derivation is a symbolic search (Maple), not a symmetrization.
3. **Modified Jacobian** (eq. 9): eq. 8 with column 5 zeroed except the
   diagonal entry, which becomes $u$.
4. **Eight-wave eigensystem** (eqs. 10–13): entropy wave ($u$), Alfvén
   waves ($u\pm B_x/\sqrt\rho$), fast and slow waves ($u\pm c_{f,s}$), and
   the divergence wave, $\lambda_d = u$ with left and right eigenvectors
   both the fifth unit vector (eq. 13). The first seven waves carry no
   $B_x$ jump; the eighth carries only $\Delta B_x$, and its strength is
   zero when $B_x$ is constant (p. 6). Eigenvectors are normalized as in
   Roe & Balsara.
5. **The source term** (eq. 14): the term "that must be added to
   Equation 2 is proportional to $\nabla\cdot\mathbf B$",
   $$\partial_t(\rho,\rho\mathbf u,\mathbf B,E)^T+\nabla\cdot(\dots)=-(0,\ \mathbf B,\ \mathbf u,\ \mathbf u\cdot\mathbf B)^T\,\nabla\cdot\mathbf B .$$
   "Technically the equations are no longer in conservative form, [but]
   the deviations from conservation will be very small." It is "only by
   writing the equations in this slightly non-conservative form that the
   singularity related to $\nabla\cdot\mathbf B$ can be removed".
6. **Second justification** (eq. 15). Expanding the conservative system
   exposes terms $-\mathbf B\,\nabla\cdot\mathbf B$ (momentum),
   $-\mathbf u\,\nabla\cdot\mathbf B$ (induction) and $-(\mathbf u\cdot
   \mathbf B)\,\nabla\cdot\mathbf B$ (energy); the source "simply acts to
   remove" them.
7. **Divergence evolution** (eqs. 16–17). The conservative form gives
   $\partial_t(\nabla\cdot\mathbf B) = 0$; the modified form gives
   $\partial_t(\nabla\cdot\mathbf B)+\nabla\cdot(\mathbf u\,\nabla\cdot
   \mathbf B)=0$, so "$\nabla\cdot\mathbf B/\rho$ is treated as a passive
   scalar", "clearly the more numerically stable of the two … any local
   $\nabla\cdot\mathbf B$ that is created is convected away". No stability
   proof is given.
8. **Lineage** (pp. 6–7): "It has been previously noted that solving the
   momentum equation in non-conservative form can remove instabilities
   related to non-zero $\nabla\cdot\mathbf B$"
   ([Brackbill & Barnes (1980)](/sources/brackbill-barnes-1980.md)).
9. **Discrete constraint and taxonomy** (§1, eq. 5). In 2D the constraint
   is $\sum_{\text{faces}} B_n\,ds = 0$, so a face jump in $B_n$ is allowed
   if the other faces balance it. Three standard approaches are listed:
   projection with a Poisson solve, staggered variables, a vector
   potential. Powell's is a fourth, collocated, with all field components
   updated by the Riemann solver.
10. **Implementation** (§2, p. 8). Roe-type solver; the interface state is
    the arithmetic average of left and right states (a Roe average "does
    exist", per Roe, private communication). The source term "is
    calculated in each cell, and added to the residual"; no discrete
    formula for its $\nabla\cdot\mathbf B$ is printed. First order in
    space and time.
11. **Conclusion** (§4). The eighth wave "arises only in multi-dimensional
    problems" and "plays the very important role of stabilizing the
    numerical method with respect to the small amounts of
    $\nabla\cdot\mathbf B$ generated in solving the discrete MHD
    equations".

# Tests

**Rotated Brio–Wu shock tube** (§3, Figs. 2–8), the only test
([rotated shock tube](/benchmarks/rotated-shock-tube.md)).
* **Data** (Fig. 2). Left: $\rho = 1$, $p = 1$, $B_x = 3/4$, $B_y = 1$.
  Right: $\rho = 1/8$, $p = 1/10$, $B_x = 3/4$, $B_y = -1$. Rotated by 45°:
  left $B_x = -1/(4\sqrt2)$, $B_y = 7/(4\sqrt2)$; right $B_x =
  7/(4\sqrt2)$, $B_y = -1/(4\sqrt2)$. Periodic along $y$ = const
  (unrotated) or $x+y$ = const (rotated). $\gamma = 2$.
* **Grids.** 600 cells in $x$ for 100 steps and 1200 cells for 200 steps,
  $\Delta t/\Delta x = 0.2$, "a CFL number of approximately 0.8 on the
  non-rotated problem". The $y$ extent and the output time are not printed.
* **Findings.** Rotated and unrotated results are "nearly
  indistinguishable for all but the normal component of velocity"
  (Figs. 3–7); Fig. 5 shows a visible $u_n$ difference in the post-shock
  plateau, and "the errors in $u_n$ are balanced by errors in … $B_n$".
  Fig. 8 ($B_n$, exact value 0.75): errors "on the order of a few percent
  … on the coarse grid, but the errors are reduced as the grid is
  refined". Coarse-grid spikes reach about 0.71 and 0.79 (read from the
  figure).
* No divergence norm, time history or convergence rate is reported; the
  $B_n$ deviation is the only proxy.

# Notation map

| Powell (1994) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$, cell-centred | $B_h$, cell-collocated | as in [Powell et al. (1999)](/sources/powell-1999.md) |
| $\mathbf u = (u,v,w)$ | $\mathbf u$, $u_h$ | |
| $B_n$ | words: normal field | as on the rotated-shock-tube page |
| $\sum_{\text{faces}} B_n\,ds = 0$ (eq. 5) | $D_h^{\mathrm f} B_h = 0$ | stated as the constraint only, not as the divergence used in the source |
| $(0,\mathbf B,\mathbf u,\mathbf u\cdot\mathbf B)^T$ | $S(U)$ as on [positivity–divergence coupling](/results/positivity-divergence-coupling.md) | |
| $E$ (total energy) | words | **collision:** $E_h$ is the EMF |
| $A_p, B_p, C_p$, $A'_p$ (Jacobians) | words | **collision:** $A_h$, $B_h$, $C_h$ |
| $\tilde\ell_k$, $\tilde r_k$ | words | **collision:** $l$ (level), $r$ (ratio) |
| $\lambda_d$ | words: divergence-wave speed | |
| $c_a$, $c_f$, $c_s$, $a$ | words | $c_h$, $c_p$ are GLM quantities; $a$ undefined in the paper |

# Pages created or updated

* Updated [Eight-wave formulation](/methods/eight-wave.md): the primary report (eqs. 8–17, first-order solver, rotated shock tube), the Brackbill–Barnes lineage, and what the 1994 report does not contain.

# Citations

1. `~/papers/mosaic/div-free-amr/1994-ICASE-Powell-19940028527.pdf`.
   * **Version read.** The NTRS image scan of ICASE Report No. 94-24 /
     NASA CR-194902, April 1994: 18 PDF pages (cover, title and abstract,
     pp. 1–13, report documentation page). The documentation page says
     "Submitted to the Journal of Computational Physics".
   * **Identity.** No DOI exists for the report. Checked against the NTRS
     record 19940028527 (https://ntrs.nasa.gov/citations/19940028527):
     title, single author, date 1994-04-01, report numbers
     NASA-CR-194902 and ICASE-94-24, contract NAS1-19480; the NTRS abstract
     matches the PDF word for word. The 1997 Springer reprint
     (doi:10.1007/978-3-642-60543-7_23, *Upwind and High-Resolution
     Schemes*) is a later printing and was not read.
   * **How it was read.** The OCR layer is poor. All equations were read
     from page renders at 110 and 300 dpi. The fast and slow eigenvectors
     (eq. 12) are not transcribed: their sign pattern needs a
     higher-resolution check. Figure values are read by eye.
   * **Recorded as printed.**
     * Eq. 14 prints the momentum flux as "$\rho\mathbf{uu}+\mathbf
       I(p+\tfrac{\mathbf B\cdot\mathbf B}{2})-\mathbf B n\mathbf B$"; eq. 2
       has $\mathbf{BB}$.
     * Eq. 10 uses $a$ without defining it.
     * Two in-text citations print as "[?]" (Zachary & Colella, §1; a
       second Roe item, p. 2) and have no list entry.
   * **Reference list.** 7 entries, all merged. The two "[?]" citations
     cannot be identified from this source and are not merged. Roe &
     Balsara, printed "J. Comput. Phys., to appear" (1994), was merged into
     `roe-1996` (SIAM J. Appl. Math. 56:57). The bibliography holds 3654
     entries after this batch.
