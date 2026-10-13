---
type: Source
title: "Dedner et al. (2002) — Hyperbolic Divergence Cleaning for the MHD Equations"
description: "The origin of GLM divergence cleaning for ideal MHD: a scalar coupled to the induction equation through a linear operator gives elliptic, parabolic, hyperbolic or mixed cleaning; the mixed form stays conservative except for the damping source, has the cleaning waves ±c_h, a time-step-tied c_h, an exact 2×2 face Riemann solve and an exact damping step with c_p²/c_h = 0.18; the non-conservative EGLM and Galilean-invariant variants lose conservation, and mixed GLM is recommended."
resource: "doi:10.1006/jcph.2001.6961"
source_kind: paper
authors: [Dedner A., Kemm F., Kröner D., Munz C.-D., Schnitzer T., Wesenberg M.]
year: 2002
venue: "J. Comput. Phys. 175:645–673"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2002-JCP-Dedner-101006jcph20016961.pdf"
tags: [mhd, divergence-cleaning, glm, source-terms, unstructured-grid]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper carries the generalized Lagrange multiplier (GLM) correction
of Munz et al. for Maxwell's equations over to ideal MHD. A scalar
$\psi_{\mathrm{GLM}}$ enters the induction equation through its gradient
and is tied to Gauss's law by a linear operator; the choice of that
operator gives elliptic (projection), parabolic, hyperbolic or mixed
hyperbolic/parabolic cleaning. In the mixed choice divergence errors
travel at the cleaning speed $c_h$ and are damped at rate
$c_h^2/c_p^2$; density, momentum, field and energy stay conserved, and
the system is hyperbolic with nine waves, of which only $\pm c_h$ carry
jumps in $B_x$ and $\psi_{\mathrm{GLM}}$. A non-conservative extended
form (EGLM), derived from the GLM–Maxwell equations, and
Galilean-invariant forms of both are also given. The scheme is a
cell-centred finite-volume add-on on unstructured triangles: an exact
$2\times2$ Riemann solve for $(B_x, \psi_{\mathrm{GLM}})$ at each edge, a
$c_h$ tied to the time step, and an exact operator-split damping step.
On adaptive triangular grids mixed GLM and mixed EGLM give the smallest
divergence errors, and mixed GLM is recommended because EGLM and Powell's
source terms lose conservation.

# Key claims

1. **General constrained form** (§2, eqs. 4–5, 10–11). The induction
   flux gains $\psi_{\mathrm{GLM}}\mathsf I$, and Gauss's law becomes
   "a linear operator of $\psi_{\mathrm{GLM}}$ plus $\nabla\cdot\mathbf B$
   equals zero". For smooth solutions $\nabla\cdot\mathbf B$ and
   $\psi_{\mathrm{GLM}}$ satisfy the same equation, whatever the operator.
2. **Four choices** (§2, eqs. 12–19).
   * *Elliptic* (operator zero, eq. 12): the projection of Brackbill and
     Barnes, a Poisson solve per step ("elliptic correction", p. 649).
   * *Parabolic* ($\psi_{\mathrm{GLM}}/c_p^2$, eqs. 13–14):
     $\psi_{\mathrm{GLM}}$ obeys a heat equation, and eliminating it adds
     $c_p^2\nabla(\nabla\cdot\mathbf B)$ to the induction equation.
     Rejected because an explicit discretization limits $c_p$ through
     stability (p. 650).
   * *Hyperbolic* ($c_h^{-2}\partial_t\psi_{\mathrm{GLM}}$, eqs. 15–16):
     a wave equation; errors leave the domain at the finite speed $c_h$.
   * *Mixed* (eq. 17): the telegraph equation (eq. 18) and
     $$\partial_t\psi_{\mathrm{GLM}} + c_h^2\,\nabla\cdot\mathbf B = -\frac{c_h^2}{c_p^2}\psi_{\mathrm{GLM}}\qquad(19).$$
     Since the damping is a source and not a dissipation term, there is
     "no longer a restriction on $c_p$ imposed by a stability condition";
     "the variables ρ, ρu, B, and e are still conserved" (p. 650).
3. **EGLM** (§2, eqs. 20–24, p. 651, signs checked on the page image).
   The Lorentz force is written
   $$(\nabla\times\mathbf B)\times\mathbf B = \nabla\cdot\left(\mathbf B\mathbf B - \tfrac12\vert\mathbf B\vert^2\mathsf I\right) - (\nabla\cdot\mathbf B)\mathbf B\qquad(22),$$
   "the part in divergence form is added to the flux, while the second
   term is considered to be a 'source term.' Usually this second term is
   dropped". EGLM keeps it: the momentum equation carries the source
   $-(\nabla\cdot\mathbf B)\mathbf B$ (eq. 24b), the energy equation
   $-\mathbf B\cdot\nabla\psi_{\mathrm{GLM}}$ (eq. 24d), and the induction
   equation none (eq. 24c). The non-conservative terms can violate
   conservation "even if the initial values are divergence-free" (p. 654).
   The paper does not write the component of either force along
   $\mathbf B$.
4. **Eigenstructure** (§3, eqs. 25–35, p. 653). In 1D the
   $(B_x, \psi_{\mathrm{GLM}})$ equations decouple; the eigenvalues are
   $-c_h$, the seven MHD speeds $v_x - c_f, \dots, v_x + c_f$, and $+c_h$,
   distinct from the MHD ones "if $c_h$ is sufficiently large"; "only the
   waves traveling with speeds $\lambda_1$ and $\lambda_9$ can carry a
   change in $B_x$ or ψ". EGLM has the same eigenvalues.
5. **Powell source terms** (eqs. 36–37): momentum
   $-(\nabla\cdot\mathbf B)\mathbf B$, induction
   $-(\nabla\cdot\mathbf B)\mathbf v$, energy
   $-(\nabla\cdot\mathbf B)\,\mathbf v\cdot\mathbf B$; the extra
   eigenvalue $v_x$ transports divergence errors with the flow; the
   system is Galilean invariant.
6. **Galilean-invariant (E)GLM** (eq. 38, p. 655, page image): momentum
   $-(\nabla\cdot\mathbf B)\mathbf B$, induction
   $-(\nabla\cdot\mathbf B)\mathbf v$, energy
   $-(\nabla\cdot\mathbf B)\,\mathbf v\cdot\mathbf B - \mathbf B\cdot\nabla\psi_{\mathrm{GLM}}$,
   and $-\mathbf v\cdot\nabla\psi_{\mathrm{GLM}}$ added to the right of
   eq. 19. The cleaning speeds become $v_x \mp c_h$; "with this
   modification the GLM–MHD system is no longer conservative".
7. **Time step and cleaning speed** (§4, eq. 40, p. 656). The step is
   $\nu$ times the smallest triangle height over the largest normal
   $\vert v_n\vert + c_f$; $c_h$ is $\nu$ times the smallest triangle
   height over $\Delta t$, set "uniformly for all" cells, so that "$c_h$
   is the maximal value which is compatible with (40)". It is therefore
   recomputed every step with $\Delta t$.
8. **Face solve** (eqs. 41–43). The linear $(B_x, \psi_{\mathrm{GLM}})$
   subsystem, eigenvalues $\pm c_h$, is solved exactly at each edge:
   $$B_x^* = B_{x,L} + \tfrac12(B_{x,R} - B_{x,L}) - \tfrac{1}{2c_h}(\psi_{\mathrm{GLM},R} - \psi_{\mathrm{GLM},L}),\qquad \psi^*_{\mathrm{GLM}} = \psi_{\mathrm{GLM},L} + \tfrac12(\psi_{\mathrm{GLM},R} - \psi_{\mathrm{GLM},L}) - \tfrac{c_h}{2}(B_{x,R} - B_{x,L}),$$
   with flux $(\psi^*_{\mathrm{GLM}}, c_h^2B_x^*)$ added to any 1D MHD
   flux that takes $B_x^*$ as its normal field. Base fluxes: the simple
   Dai–Woodward flux, and MHD–HLLEM.
9. **Damping** (eqs. 44–46, p. 657). An exact operator-split step,
   $\psi_{\mathrm{GLM}} \leftarrow \psi_{\mathrm{GLM}}\,e^{-\Delta t\,c_h^2/c_p^2}$,
   "unconditionally stable". Three ways to set $c_p$: constant (but its
   optimum "significantly depends on the grid size and the scheme used");
   a fixed per-step factor $e^{-\Delta t\,c_h^2/c_p^2} \in (0, 1)$
   (eq. 46); or a fixed $c_p^2/c_h$, the "ratio between hyperbolic and
   parabolic effects", with which "the numerical results are quite
   independent of the grid resolution and the scheme used". Only the last
   is used. No dimension is stated; $c_p^2/c_h$ is a length.
10. **The value 0.18** (§5, p. 661, Fig. 2): "the optimal value of
    [$c_p^2/c_h$] is about 0.18 independent of the grid resolution and the
    order of the scheme", found on the peak-in-$B_x$ test with the DW
    scheme; it is used throughout.
11. **EGLM sources discretized** (eqs. 47–48) with the face normal field
    $B_x^*$ and the gradient of the linear function through the three
    edge values of $\psi_{\mathrm{GLM}}$. Boundary data for
    $\psi_{\mathrm{GLM}}$: like $\rho$ (used), homogeneous Dirichlet, or
    non-reflecting (eq. 49); "no significant dependency" on the choice.
12. **1D analysis** (Appendix, Theorems A.1–A.2). Parabolic cleaning
    decays like $t^{-1/2}$ (an erf bound, A.16); hyperbolic cleaning
    restores the initial field on $[0, 1]$ for $t \ge 1/c_h$ (A.17–A.19).
    Proofs omitted as standard.
13. **Conclusions** (§6). Mixed GLM gives "both propagation and damping
    of divergence errors even in stagnation points"; its MHD part stays
    in conservation form; the extra cost is a $2\times2$ linear Riemann
    problem and a scalar source. "We have observed a significant loss of
    conservation caused by hyperbolic source terms, which are not present
    in the mixed GLM formulation. Thus we recommend using the mixed GLM
    scheme." Direct applicability on arbitrary 2D and 3D grids is
    claimed, and an extension to resistive MHD expected; the paper tests
    neither. Constrained transport and staggered grids are
    explicitly not considered (pp. 647–648).

# Tests

2D, unstructured triangles; second-order DW and MHD–HLLEM except the 1D
Riemann problem (first order); $\nu = 0.3$ and $c_p^2/c_h = 0.18$
throughout. Five variants: mixed GLM, mixed EGLM, hyperbolic GLM, no
correction, Powell source terms. Divergence is measured by the face-jump
divergence (sum of edge-length times averaged normal field, over cell
area), its maximum and its $L^1$ norm (eqs. 50–55). Initial data: Table I.

* **Peak in $B_x$** ($\gamma = 5/3$; Figs. 2, 3, 9): $\rho = 1$,
  $\mathbf v = (1, 1, 0)$, a polynomial bump in $B_x$, $p = 6$, periodic;
  the domain is printed "[−0.5, −0.5] × [1.5, 1.5]" (read as
  $[-0.5, 1.5]^2$). Powell advects the peak, no correction creates new
  extrema, hyperbolic GLM shows complex wave interactions, mixed GLM
  damps it. Maximum divergence: mixed GLM ≈ mixed EGLM smallest. EGLM and
  source terms lose conservation (Fig. 9): "the mixed GLM ansatz is by
  far the best choice".
* **1D Riemann problem** (Dai–Woodward, also used by Tóth; $\gamma = 5/3$;
  Table II, Fig. 4). Domain $[-0.5, 0.5]\times[-0.25, 0.25]$;
  $\rho = 1$, $v_x = \pm10$, $\mathbf B = (5, 5, 0)/\sqrt{4\pi}$, $p = 20$
  left and 1 right. $L^1$ errors against a 1D reference on a cut at
  $y = 0.0424$ (first-order DW):

  | Elements | Mixed EGLM | EOC | Mixed GLM | EOC | Source terms | EOC |
  |---|---|---|---|---|---|---|
  | 1,024 | 6.44165126 | | 6.45517676 | | 7.03537990 | |
  | 4,096 | 3.08112407 | 1.064 | 3.09306537 | 1.061 | 3.82213248 | 0.880 |
  | 16,384 | 1.68278946 | 0.873 | 1.68627598 | 0.875 | 2.48360779 | 0.622 |
  | 65,536 | 0.97173595 | 0.792 | 0.96600380 | 0.804 | 1.84060872 | 0.432 |
  | 262,144 | 0.47211608 | 1.041 | 0.46045425 | 1.069 | no solution | |
  | 1,048,576 | 0.23998602 | 0.976 | 0.22792806 | 1.014 | no solution | |

  Source terms give wrong intermediate states, falling rates, divergence
  errors 2–3 times larger, and negative pressure on fine grids; the
  uncorrected DW run fails on all grids; hyperbolic ≈ mixed GLM. "A close
  study of the EGLM results also reveals some problems with the
  intermediate states, which are not present in the GLM case" (p. 664).
* **Shock reflection** (Aslan & Kammash; $\gamma = 1.4$; Fig. 5), shock at
  29°. Uncorrected DW crashes; Powell's maximum divergence is about twice
  that of GLM and EGLM, and its $L^1$ divergence stays constant while the
  GLM variants' decreases; with HLLEM the source-term run also breaks
  down.
* **2D Riemann problem** (MHD four-quadrant, $[-1, 1]^2$, $\gamma = 5/3$;
  Figs. 6–7; quadrant data in Table I). The three GLM variants have
  almost identical divergence errors, "at least 50% smaller" than without
  correction or with source terms; at $t = 0.25$ about 166,000 adapted
  triangles against 375,606 (uncorrected) and 315,662 (source terms),
  which take at least 50% more time.
* **MHD Kelvin–Helmholtz** ($[0, 1]\times[-1, 1]$, $\rho = 1$,
  $\mathbf B = (1, 0, 0)$, $p = 50$, $\gamma = 1.4$; Figs. 8–9). Mixed GLM
  keeps the symmetry; the uncorrected run distorts it and needs 53% more
  computing time; uncorrected MHD–HLLEM crashes; source terms deviate in
  conservation much more than mixed EGLM.

# Notation map

| Dedner et al. (2002) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$ | $\psi_{\mathrm{GLM}}$ | **collision**: the registry's bare $\psi$ is the vector-potential gauge scalar |
| $c_h$, $c_p$ | $c_h$, $c_p$ | same |
| $c_r := c_p^2/c_h$ | $C_r L_{\mathrm{GLM}}$ | **collision**: the paper's $c_r$ is a length, the registry's $C_r$ is dimensionless; $\alpha_p = \min_d h_d/c_r$ |
| $c_d := e^{-\Delta t_n c_h^2/c_p^2}$ | words (per-step damping factor) | |
| $\mathcal D$ | words (linear operator of the constraint) | not registered |
| $\mathbf u$, $e$ | $\mathbf v$, $E$ | |
| $\mathcal I$ | $\mathsf I$ | identity |
| $\mathbf j$, $\mathbf F_L$ | $\nabla\times\mathbf B$; $(\nabla\times\mathbf B)\times\mathbf B$ | **collision**: the registry's $\mathbf J$ is a curl-constrained edge field |
| $c_f$, $c_a$, $c_s$ | $c_f$, $c_A$, $c_s$ | |
| $W$, $U$, $\mathcal A$, $\mathcal B$ | words; $u$; words | $\mathcal B$ (source matrix) avoided: visual clash with $\mathbf B$ |
| $\Delta t_n$, $c_{cfl}$ | $\Delta t$, $\nu$ | |
| $h_{jl} = 2\vert T_j\vert/\vert S_{jl}\vert$ | words (triangle height) | |
| $B_{x,m}$, $\psi_m$ | $B_x^*$, $\psi^*_{\mathrm{GLM}}$ | as on the cleaning page |
| $\mathrm{divB}_{jmp}$, $max_{jmp}$, $L1_{jmp}$ | words (face-jump divergence) | |
| eoc | EOC | |

# Pages created or updated

* Updated [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)
  (batch-17 block: the origin of the system, the operator family, the
  time-step-tied $c_h$, the three choices of $c_p$ and the value 0.18,
  EGLM and its Galilean-invariant form, the recommendation of mixed GLM,
  Table II; a bullet in the Open entry on the sign of the parallel force,
  for the plus side; a bullet in the Open entry on the time-step-tied
  $c_h$).
* Updated [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md)
  (batch-17 block: the colliding-flow tube on unstructured triangles,
  Table II).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2002-JCP-Dedner-101006jcph20016961.pdf`.
   * **Version read.** The publisher's typeset PDF (Elsevier Science (USA)
     2002), 29 pages; received April 3, 2001, revised October 15, 2001.
   * **Identity.** doi:10.1006/jcph.2001.6961, printed on page 1 and
     checked on Crossref: "Hyperbolic Divergence Cleaning for the MHD
     Equations", J. Comput. Phys. 175(2):645–673, issued 2002-01, authors
     Dedner, Kemm, Kröner, Munz, Schnitzer, Wesenberg, reference count 48;
     agrees with page 1.
   * **How it was read.** Text layer, with the sign-bearing equations
     (17–19, 22, 24a–e, 36, 38, 40–49, A.16–A.19) and Table I checked on
     page images (pp. 650, 651, 654–658, 660, 670). Figures 2–9 are plots;
     only the statements of the text are reported. Matrix (27) is
     described, not reproduced.
   * **Recorded as printed** (reader's reading).
     - The peak-in-$B_x$ domain is printed "[−0.5, −0.5] × [1.5, 1.5]",
       read as $[-0.5, 1.5]^2$; the support of the bump polynomial is not
       stated.
     - The Kelvin–Helmholtz $v_x$ is copied with its printed
       parenthesization, "$5(\tanh(20(y+0.5)) - (\tanh(20(y-0.5)) + 1))$".
     - In A.18 the upper limit of the time integral is printed $T$,
       presumably $t$.
   * **Reference list:** 48 entries, all merged. Powell's ICASE report
     94-24 lands on `powell-1994`; Powell et al. in Numerical Methods for
     Fluid Dynamics V is `powell-1995-b`, distinct from the AIAA paper
     `powell-1995`; B.-N. Jiang's works are `jiang-1996-b` and
     `jiang-1998-c` (the bare keys are Jiang & Shu and Jiang & Tadmor);
     Dai & Woodward's J. Comput. Phys. 142:331 is `dai-1998-b`; the Munz
     2000 pair (proceedings and J. Comput. Phys. 161:484), printed in the
     opposite suffix order to the bundle, was resolved by venue.
     Bibliography: 3270 entries.
