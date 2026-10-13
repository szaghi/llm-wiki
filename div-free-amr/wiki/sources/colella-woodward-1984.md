---
type: Source
title: "Colella & Woodward (1984) — The Piecewise Parabolic Method (PPM) for Gas-Dynamical Simulations"
description: "The full algorithmic description of PPM: conservative zone parabolae with fourth-order interface values and a monotonicity constraint, contact steepening, Lagrangian, remap and characteristic-tracing Eulerian gas dynamics, and the extra dissipation (flattening, artificial viscosity) it needs; pure hydrodynamics."
resource: "doi:10.1016/0021-9991(84)90143-8"
source_kind: paper
authors: [Colella P., Woodward P.R.]
year: 1984
venue: "J. Comput. Phys. 54:174-201"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1984-JCP-Colella-1010160021-99918490143-8.pdf"
tags: [ppm, reconstruction, godunov, high-order, shock-capturing]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper gives the complete algorithm of the piecewise parabolic method,
a higher-order extension of Godunov's method in the MUSCL family whose
benchmarks are in the companion paper (Woodward & Colella 1984, J. Comput.
Phys. 54:115). It is compiled in [PPM](/methods/ppm.md).
* §1, scalar advection on a general non-uniform mesh: a conservative
  parabola per zone, built from interface values that come from a quartic
  fit of the indefinite integral; a monotonicity constraint; an optional
  contact-steepening ("discontinuity detection") switch.
* §2, Lagrangian gas dynamics: time-averaged edge pressure and velocity
  from a two-shock Riemann problem whose states are averages of the
  parabolae over the sound-wave domains of dependence; Eulerian dynamics by
  Lagrange plus remap (not detailed).
* §3, a single-step Eulerian scheme with characteristic tracing of
  interface states, geometric and gravity sources included.
* §4 and the Appendix: any higher-order Godunov method of this type needs
  dissipation beyond monotonicity limiting, supplied by shock flattening, a
  small artificial-viscosity flux or an alternating grid motion.

It is a **pure hydrodynamics paper**: no magnetic field, no MHD, no
divergence constraint on $\mathbf B$. The only divergence in it is the
undivided velocity divergence that drives the multidimensional
dissipation switch (eqs. 4.5, A.11). Multi-D is done by operator
splitting, so the paper's PPM is dimensionally split.

# Key claims

1. **Conservative parabola** (§1, eqs. 1.4–1.5). In zone $j$, with
   $x = (\xi - \xi_{j-1/2})/\Delta\xi_j$,
   $$a(\xi) = a_{L,j} + x\,(\Delta a_j + a_{6,j}(1-x)),\quad \Delta a_j = a_{R,j} - a_{L,j},\quad a_{6,j} = 6\left(a_j^n - \tfrac12(a_{L,j}+a_{R,j})\right),$$
   which reproduces the zone average $a_j^n$ exactly.
2. **Interface value from a quartic fit of the integral** (eq. 1.6). The
   value $a_{j+1/2}$ is the derivative at $\xi_{j+1/2}$ of the quartic
   through $(\xi_{j+k+1/2}, A_{j+k+1/2})$, $k = 0, \pm1, \pm2$, with $A$
   the indefinite integral of $a$. It is "third-order accurate for
   variable mesh spacing, even where the mesh spacing changes
   discontinuously". On a uniform mesh (eq. 1.9)
   $$a_{j+1/2} = \tfrac{7}{12}(a_j^n + a_{j+1}^n) - \tfrac{1}{12}(a_{j+2}^n + a_{j-1}^n).$$
3. **Limited slope** (eq. 1.8). The slope $\delta a_j$ of eq. 1.6 is
   replaced by $\delta_m a_j$, a minimum of $|\delta a_j|$ and two
   one-sided differences doubled, when $a_j^n$ is not an extremum, and by 0
   otherwise. This keeps $a_{j+1/2}$ between $a_j^n$ and $a_{j+1}^n$ and
   steepens discontinuities. The printed formula duplicates one term (see
   Citations).
4. **Monotonicity constraint** (eq. 1.10). If $a_j^n$ is a local extremum,
   $a_{L,j} = a_{R,j} = a_j^n$ (constant profile). If the parabola
   overshoots near one edge, that edge value is reset ($a_{L,j} \to
   3a_j^n - 2a_{R,j}$, or symmetrically), which makes the derivative zero
   at the opposite edge. The no-overshoot condition is
   $|\Delta a_j| \ge |a_{6,j}|$. *Compiler reading:* smooth extrema are
   therefore clipped to a constant profile.
5. **Accuracy statements.** The advection scheme is "third-order accurate
   in general; in the limit of very small time steps, for equally spaced
   zones, it is fourth-order accurate" (Fig. 2 caption; also after
   eq. 1.9). The gas-dynamics schemes "sacrifice third-order accuracy in
   time to the extent that the nonlinear interaction between the two
   hydrodynamic waves is calculated only to second order" (§2). Edge
   pressure and velocity averages are "second-order accurate" (§§2–3). No
   convergence table is given.
6. **Upwind-integrated flux** (eqs. 1.11–1.13). Domain-of-dependence
   averages of the parabola,
   $f^a_{j+1/2,L}(y) = a_{R,j} - \tfrac{x}{2}(\Delta a_j - (1-\tfrac23 x)a_{6,j})$,
   $x = y/\Delta\xi_j$, give the conservative update
   $a_j^{n+1} = a_j^n + u\frac{\Delta t}{\Delta\xi_j}(\bar a_{j-1/2} - \bar a_{j+1/2})$
   with $\bar a_{j+1/2} = f^a_{j+1/2,L}(u\Delta t)$ for $u \ge 0$. Stability
   needs $u\Delta t \le \min_j \Delta\xi_j$.
7. **Contact steepening** (eqs. 1.14–1.17, Fig. 3). Inside a detected
   discontinuity the edge values are blended with the limited-linear
   extrapolations of the neighbouring zones, with a weight $\eta_j$ driven
   by a large third derivative, a sign change of the second derivative,
   opposite signs of first and third derivatives and a jump that is not
   small. Constants: $\eta^{(1)} = 20$, $\eta^{(2)} = 0.05$,
   $\epsilon = 0.01$. Applied only to density, only at contacts (Eulerian
   criterion eq. 3.2, $K_0 = 0.1$, "problem dependent"), not in the
   Lagrangian step. If it fires in smooth flow the scheme "remains
   second-order accurate".
8. **Lagrangian PPM** (§2, eqs. 2.1–2.10, Fig. 4). Variables $\tau, u, p$
   in the mass coordinate; pressure rather than total energy is
   interpolated, because limiting $p$ behaves better near shocks.
   Geometry index $\alpha = 0, 1, 2$ and a body force are allowed. The
   Riemann problem is the two-shock form (eq. 2.8), solved with a fixed
   number of Newton iterations; in smooth flow it approximates the
   characteristic equations and gives time-centred edge values. The
   states are corrected for geometry and gravity (eq. 2.9), so that a
   smooth steady solution gives no "false jump into the Riemann problem".
9. **Lagrange plus remap** (§2, end). Noh's two-step technique, not
   detailed. The remap interpolates in the volume coordinate, uses density
   instead of specific volume and builds the remapped total energy from
   edge values of $p$, $\rho$, $u$; these "are necessary in order to
   maintain consistency between the Lagrangian step and the remap".
10. **Single-step Eulerian PPM with characteristic tracing** (§3,
    eqs. 3.1–3.8, Fig. 5). First-guess interface states are averages over
    the domain of the fastest characteristic toward the interface; alone
    they would make advection first-order accurate. For each wave family
    moving toward the interface, its amount is subtracted from the first
    guess using the primitive quasi-linear system (eq. 3.4); waves moving
    away contribute nothing. Source terms for geometry and gravity enter
    the tracing coefficients (eq. 3.7). Without pressure and velocity
    gradients the fluxes reduce exactly to the advection scheme of §1. The
    Riemann solver is the §2 iteration; inside a rarefaction fan the
    solution is linear interpolation between the states on either side.
11. **Extra dissipation is required** (§4, eqs. 4.1–4.5). Low-amplitude
    post-shock noise appears in any such higher-order Godunov method,
    especially for slowly moving strong shocks; it "arises only for
    systems of equations". Remedies:
    * **flattening** (eq. 4.1), a blend of the edge values toward the zone
      average with a coefficient between 0 and 1, nonzero only at steep
      shocks; total flattening recovers first-order Godunov locally;
    * flattening is ineffective for nearly stationary strong shocks and
      where the tangential velocity nearly vanishes;
    * an artificial diffusive flux (eq. 4.2) or an alternating moving grid
      (eq. 4.3), with a Lapidus-type coefficient $K\max(u_j - u_{j+1}, 0)$
      in 1D and, in multi-D, $K$ times the negative part of an undivided
      velocity divergence (eq. 4.5), so that shocks transverse to the sweep
      are seen. $K = 0.1$ for single-step Eulerian PPM.
12. **Tuned dissipation algorithms** (Appendix, eqs. A.1–A.11). A shock
    indicator ($\epsilon = 0.33$); simple flattening with viscosity
    ($\omega^{(1)} = 0.75$, $\omega^{(2)} = 10$, $\nu^{(1)} = 0.1$);
    Lagrangian flattening ($\kappa^{(1)} = 2$, $\kappa^{(2)} = 0.01$); a
    multidimensional Eulerian algorithm with flattening and local grid
    motion ($\nu^{(1)} = 2$, $\nu^{(2)} = 0.1$, $\nu^{(3)} = 0.2333$,
    $\sigma^{(1)} = 0.5$, $\sigma^{(2)} = 1$; in 1D $\nu^{(2)} = 0$,
    $\nu^{(3)} = 0.3333$). "Experimentation with different values of the
    parameters is not recommended".
13. **Minimality** (§5). The algorithms "are the minimal ones": every
    further simplification tried "led to some degradation of the results".
    Multifluid and general equations of state are called
    "straightforward" and not done.

# Tests

No dedicated test section; benchmarks are deferred to the companion paper.
The evidence in this paper:
* **Strong isolated planar shock, Lagrangian PPM** (§4, Fig. 6).
  $\gamma = 5/3$, pressure jump above six orders of magnitude. Unflattened
  PPM leaves post-shock oscillations of about 1.3%, mainly in the two
  Riemann invariants crossing the shock; flattening reduces them
  "dramatically" and broadens the shock slightly.
* **Strong, nearly stationary shock, first-order Eulerian Godunov** (§4,
  Fig. 8). Nearly 8000 steps to cross 160 zones; a 3% post-shock error
  (density in the text, entropy in the caption). With 6 Riemann iterations
  it stays at that level; with 2, "very large errors" appear in the zone
  behind the shock.
* **Steady-shock sweep** for the Appendix (c) constants, $\gamma = 1.4$:
  worst post-shock density oscillation $\tfrac23$% of the jump, typically
  $\tfrac14$%; shock width at most two mesh lengths.
* **Appendix (a)**: errors "a fraction of a percent" in most cases, "less
  than two percent in all the cases we tested".
* The Mach 3 wind tunnel of the companion paper is invoked qualitatively.

No convergence tables, no smooth-flow accuracy test, no magnetic test and
no divergence measurement.

# Notation map

| Colella & Woodward (1984) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $a$, $a_j^n$ | $w$, $\bar w_j$ | generic advected scalar and its zone average |
| $\xi_{j+1/2}$, $\Delta\xi_j$ | $\mathbf x$; $h$ on a uniform mesh | non-uniform zone width has no registry symbol |
| $\Delta t$, $t^n$ | $\Delta t$, superscript $n$ | |
| $a_{L,j}$, $a_{R,j}$ | $w^+_{j-1/2}$, $w^-_{j+1/2}$ | parabola edge values in zone $j$ |
| $\Delta a_j$, $a_{6,j}$ | words | parabola coefficients |
| $\delta a_j$, $\delta_m a_j$, $\delta^2 a_j$ | words | slopes and second difference |
| $\eta_j$ and constants | words | $\eta$ is conventionally resistivity in MHD |
| $f_j$ (flattening) | words | close to the registry's $f^{x,*}$ |
| $f^a_{j+1/2,L/R}(y)$ | words | domain-of-dependence average, not a flux |
| $u$, $v$ | components of $u_h$ | |
| $E$ (total energy) | words | **collision** with $E_h$ |
| $m$ (mass coordinate) | words | **collision** with $m(E)$ |
| $r$ (radial/sweep coordinate) | words | **collision** with the refinement ratio $r$ |
| $\alpha$ (geometry index) | words | mild collision with $\alpha^{\mathrm{LF}}$ |
| $V(r)$, $\Delta V_j$ | words | **collision** with $V_h^k$ |
| $A(r)$ | words | **collision** with $A_h$ |
| $H(U)$ | words | **collision** with $H$ and $\mathsf H$ |
| $G$, $\mathbf G$, $g$ | words; $\mathbf g$ | **collision** of $G$ with $G_h$ |
| $(D\cdot\vec u)_{j+1/2,k}$ | $h\,D_h^{\mathrm{c}} u_h$-type (undivided) | the paper's only divergence, applied to velocity |

# Pages created or updated

* Created [PPM](/methods/ppm.md): the method from its primary source, and its role in the bundle's MHD schemes.
* Updated [Constrained transport](/methods/constrained-transport.md): PPM as an EMF transport approximation.
* Updated [Upwind constrained transport](/methods/upwind-constrained-transport.md): the PPM interface-value stencil behind PPM4.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): the characteristic-tracing slot that receives the MHD source terms.
* Updated [Block-structured AMR](/definitions/block-structured-amr.md): the PPM ghost-cell count is not stated in the PPM paper.
* Updated [CASTRO](/software/castro.md): split original against unsplit CASTRO PPM, and the extremum limiter.

# Citations

1. `~/papers/mosaic/div-free-amr/1984-JCP-Colella-1010160021-99918490143-8.pdf`.
   * **Version read.** The published journal article, a 28-page scan
     (Acrobat Capture 2003, with an OCR text layer). Received August 3,
     1982; revised August 25, 1983.
   * **Identity.** doi:10.1016/0021-9991(84)90143-8, checked on Crossref:
     title, both authors, J. Comput. Phys. 54(1):174–201, April 1984,
     reference count 12; all agree with page 1.
   * **How it was read.** The OCR layer is unreliable for equations. Every
     equation cited here was checked on a page render (110 dpi, zoomed to
     300–400 dpi where needed). Eq. 1.6 (general non-uniform interface
     formula) and eqs. 2.9, 3.7, A.3, A.5, A.9–A.11 were read and
     summarized, not transcribed term by term.
   * **Recorded as printed.**
     * Eq. 1.8 prints both doubled differences as
       $2|a_j^n - a_{j-1}^n|$ (verified at 300 dpi). The intended second
       term is evidently $2|a_{j+1}^n - a_j^n|$, van Leer's MUSCL limiter;
       the correction is inferred, not stated by the paper.
       [Felker & Stone (2018)](/sources/felker-2018.md) record typos in
       the "original PPM limiter formulas"; whether this is the one they
       mean is not verifiable from this paper.
     * §2 cites "the discontinuity detection algorithm (1.16)–(1.18)";
       there is no eq. 1.18 (the detection equations are 1.14–1.17).
     * The 3% post-shock error of Fig. 8 is "in the density" in §4 and "in
       the entropy" in the caption.
   * **Reference list.** 12 entries, all merged; Crossref's reference
     count agrees. The bibliography key `colella-1984` was renamed to the
     slug `colella-woodward-1984`, and its malformed DOI was corrected on
     Crossref. Colella's MUSCL paper ("in press") and Colella & Glaz ("in
     preparation") were merged into their 1985 entries (`colella-1985`,
     `colella-glaz-1985-b`). Godunov, Zabrodin & Prokopov (1961) is
     `godunov-1961-b`; van Leer (1984), a private communication, is
     `vanleer-1984-b`. The bibliography holds 3669 entries after this
     batch.
