---
type: Source
title: "Roe & Balsara (1996) — Notes on the eigensystem of magnetohydrodynamics"
description: "Orthonormal scaling of the 1D seven-wave MHD eigenvectors that keeps them bounded at every degeneracy except vacuum, their direction-dependent form at the triple umbilic, and a proof that the Roe flux there is insensitive to the linearization state."
resource: "doi:10.1137/S003613999427084X"
source_kind: paper
authors: [Roe P.L., Balsara D.S.]
year: 1996
venue: "SIAM J. Appl. Math. 56:57-67"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1996-SIAMJAM-Roe-101137S003613999427084X.pdf"
tags: [mhd, eigenvectors, riemann-solver, godunov]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An analytical paper on the eigensystem of 1D ideal MHD in primitive
variables, a $7\times7$ system with the normal field constant. It scales
the fast and slow eigenvectors so that each right–left pair has unit
product, through two parameters whose squares sum to one (eqs. 7–9), a
refinement of Brio & Wu's renormalization. Because the squares sum to one,
the eigenvectors stay bounded and linearly independent in all degenerate
cases except the vacuum limit. At the **triple umbilic**, where the fast,
slow and Alfvén speeds coincide, the parameters are indeterminate; the
paper gives their direction-dependent limit (eq. 15). It integrates the
wave paths near that point (§3) and shows that the Roe-type flux changes
only by $O(\epsilon)$ when the linearization state moves within $\epsilon$
of it, although the individual wave strengths change by $O(1)$ (§4). The
divergence constraint appears only in a closing remark on Powell's eighth
wave (§6). There are no numerical tests.

# Key claims

1. **System and speeds** (§2, eqs. 2–4). Primitive variables density,
   three velocities, two transverse field components, pressure; "Because of
   the one-dimensional assumption, $B_x$ is a constant" (p. 58), so there
   is no normal-field row. Seven waves; the fast and slow speeds are the
   roots of a quadratic in the squared speed (eq. 3), with the identities
   of eq. 4.
2. **Geometry of degeneracy** (p. 59, Fig. 1). In the plane of normal and
   transverse Alfvén speed scaled by the sound speed, constant fast and
   slow speeds are confocal ellipses and hyperbolae with foci at the
   triple points; fast and slow speeds coincide only when the normal
   Alfvén speed equals the sound speed and the transverse field vanishes.
3. **Why normalization is needed** (eqs. 5–6). The left–right product of
   the unnormalized magnetoacoustic eigenvectors is "singular or
   indeterminate in a variety of cases".
4. **The normalization** (eqs. 7–9, 17–18, p. 60). Two parameters for fast
   and slow, with squares summing to one, scale the right eigenvectors; the
   left ones carry an extra inverse squared sound speed so that the right
   ones have the dimensions of the state. The slow parameter "is identical"
   to Brio & Wu's; "our $\alpha_f$ has an additional factor $a/c_f$". The
   transverse directions are the unit transverse-field components,
   following Brio & Wu; when the transverse field vanishes "the values they
   then assume may be given arbitrarily; for example,
   $\beta_y=\beta_z=1/\sqrt2$. This preserves the orthonormality". Alfvén
   and entropy eigenvectors: eqs. 17–18.
5. **Brio & Wu's eigenvectors, as Roe & Balsara state them** (p. 57).
   Brio & Wu's expressions "are well formed except close to the 'triple
   umbilic,' where the fast, slow, and Alfvén speeds coincide", and
   credit them with demonstrating "that the MHD equations are always
   diagonalisable although not everywhere convex". This qualifies the
   scope of Brio & Wu's own "well defined everywhere", which at the triple
   umbilic rests on an assignment (Brio & Wu eq. 46); the abstract calls the
   indeterminacy there "unavoidable"
   ([eight-wave formulation](/methods/eight-wave.md), regularity
   paragraph).
6. **Six degenerate cases** (Fig. 2, eqs. 10–16).
   * Normal field near zero; both fields near zero (the hydrodynamic
     limit, slow and Alfvén merge into shear waves); transverse field near
     zero with the normal Alfvén speed below or above the sound speed. In
     these four the eigenvectors "remain well formed and linearly
     independent" (p. 60).
   * **Triple umbilic.** The parameters "become indeterminate. However,
     since $\alpha_f^2+\alpha_s^2=1$, the eigenvectors cannot be singular."
     Close to it they equal the sine and cosine of half the angle of
     approach in the speed plane, plus corrections bounded by a quarter of
     the scaled transverse Alfvén speed (eq. 15). "The forms taken by
     $\alpha_{f,s}$ close to the singularity have not been given
     previously" (p. 61). The limit depends on the direction of approach.
   * **Vacuum** (eq. 16): both slow eigenvectors collapse onto the entropy
     eigenvector; the system "is no longer complete" and the equations are
     "ill posed in a way that cannot be removed by any renormalization"
     (p. 62).
7. **Wave paths near the triple umbilic** (§3, eqs. 19–20, Fig. 3).
   Closed form for $\gamma = 5/3$; the topology is Schaeffer–Shearer type
   IV, and the Riemann problem is then well posed without dissipation "if
   compressive shocks are the only ones admitted" (p. 63; stated with
   references, not proved here).
8. **Flux insensitivity** (§4, eq. 21, Fig. 4). For the Roe-type flux, the
   central average minus half the sum of wave strength times absolute
   speed times eigenvector, only the case of a normal velocity between the
   slow and fast speeds matters. The fast and slow wave strengths may
   change by $O(1)$ as the linearization state moves within a circle of
   radius $\epsilon$ about the triple umbilic, but they multiply speed
   differences bounded by $\epsilon$ times the sound speed, so "the
   arbitrariness in choosing $V_0$ has only an $\mathcal O(\epsilon)$
   effect on the value of the computed flux" (p. 65). The same argument
   "provides a justification for assigning arbitrary values" to the
   transverse directions when the transverse field vanishes. Left open:
   whether internal structures near the triple umbilic (intermediate
   shocks) are captured correctly.
9. **Structure coefficients** (§5, eqs. 22–24). Closed forms through the
   normalized eigenvectors; they vanish where the transverse field does,
   the loss of convexity "first observed in" Brio & Wu (p. 66). Whether
   extra dissipation is needed beyond stationary sonic points is left to
   "extensive testing".
10. **Divergence** (§6, p. 66, the only multidimensional content). In 1D
    the constraint is a constant normal field; in several dimensions "the
    constraint $B_x = 0$ gets replaced by the more complicated constraint
    $\mathrm{div}\,\mathbf B = 0$" (as printed). The multidimensional
    eigenvectors are "not simple extensions" of the 1D ones. The paper
    reports Powell's partially conservative form, which "retains the
    one-dimensional eigenstructure, with the addition of an eighth wave
    that convects div B as a passive scalar"
    ([eight-wave formulation](/methods/eight-wave.md);
    [Powell (1994)](/sources/powell-1994.md)). No eighth eigenvector, no
    discrete divergence and no divergence measurement appear.
11. **A correction to Zachary & Colella** (footnote 1, p. 60): in their
    slow left eigenvector "the last component should be $\tau\alpha_s$",
    and their normalizing factors "can be simplified considerably".

**Relation to the bundle.** [Powell (1994)](/sources/powell-1994.md)
normalizes his eight-wave eigenvectors "as in Roe & Balsara", and
[Powell et al. (1999)](/sources/powell-1999.md) use the same normalization;
the eighth eigenvector is Powell's, not this paper's. The two papers cite
each other: this one was received in July 1994, after Powell's April 1994
report.

# Tests

None. The paper is analytical; Figs. 1–4 are diagrams.

# Notation map

| Roe & Balsara | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf B$; $B_x$; $B_y, B_z$ | words: normal and transverse field | Gaussian units; $B_x$ constant in 1D |
| $\mathrm{div}\,\mathbf B$ | $\nabla\cdot\mathbf B$ | continuous only |
| $V$, $U$, $U_V$ | words | primitive state, conserved state, Jacobian |
| $A$ (primitive Jacobian) | words | **collision:** $A_h$ vector potential |
| $a$; $b_x, b_y, b_z, b_\perp$; $c_f, c_s$ | words | sound, Alfvén, fast and slow speeds; do not reuse $c_h$, $c_p$ |
| $\alpha_f, \alpha_s$ | words (normalization parameters) | **collision:** $\alpha^{\mathrm{LF}}$, $\mathcal E^{\alpha}$ |
| $\beta_y, \beta_z$ | words | |
| $r_k$, $l_k$ | words | **collision:** $r$ refinement ratio, $l$ level index |
| $R_k = U_V r_k$ | words | **collision:** $R$ restriction |
| $\lambda_k$ | $\lambda_k$ | eigenvalues |
| $F^*(U_L,U_R)$ | words: base-scheme numerical flux of the full system | $f^{x,*}$ is registered for field components only |
| $T$, $\phi$, $\kappa$, $s_k$, $\epsilon$, $\delta_{f,s}$ | words | **collision risk:** $\phi_h$, $\phi_{\mathrm g}$ |

# Pages created or updated

* Updated [Eight-wave formulation](/methods/eight-wave.md): the normalization and the regularity paragraph.

# Citations

1. `~/papers/mosaic/div-free-amr/1996-SIAMJAM-Roe-101137S003613999427084X.pdf`.
   * **Version read.** The publisher's typeset PDF (SIAM, 11 pp.; a 2012
     download stamp in the margin). Received 8 July 1994, accepted
     (revised) 28 December 1994.
   * **Identity.** doi:10.1137/S003613999427084X, checked on Crossref:
     title and authors match; vol. 56, issue 1, pp. 57–67, issued February
     1996; reference count 26.
   * **How it was read.** The OCR text layer garbles every equation; all
     equations (2–24) were read from page renders, footnote 1 and refs.
     [14]–[19] at 300 dpi. Nothing left unreproduced.
   * **Recorded as printed.**
     * Footnote 1 prints $\tau\alpha_s$; $\tau$ is not defined in this
       paper.
     * §6 prints "the constraint $B_x = 0$", where a constant normal field
       is meant.
     * The degenerate-case asymptotics and the bounds of eq. 15 are
       stated ("It can be shown"), not derived; the topology and
       well-posedness statements rest on references and a private
       communication.
     * Ref. [8] first author printed "Shaeffer" in the list and
       "Schaeffer" in the text; ref. [1] prints "Tanuiti"; ref. [12]
       prints "collination".
   * **Reference list.** 26 entries, all merged. Ref. [9], printed
     "Blandford & Payne 1982, MNRAS 176:465", carries the title and venue
     of Blandford's single-author 1976 paper (Crossref): new entry
     `blandford-1976`. "Woodward & Dai, JCP 115:485" is
     `dai-woodward-1994-b`. Brio & Wu is the ingested `brio-wu-1988`.
     Bibliography key renamed `roe-1996` → `roe-balsara-1996`. The
     bibliography holds 3711 entries after this batch.
