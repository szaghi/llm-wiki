---
type: Source
title: "Dai & Woodward (1998) — A Simple Finite Difference Scheme for Multidimensional Magnetohydrodynamical Equations"
description: "Second-order split Godunov MHD scheme whose field is held as face averages and updated by the exact integral induction law with corner EMFs interpolated from cell states: the primary source of field-interpolated CT."
resource: "doi:10.1006/jcph.1998.5944"
source_kind: paper
authors: [Dai W., Woodward P.R.]
year: 1998
venue: "J. Comput. Phys. 142:331-369"
local_file: "/home/stefano/papers/mosaic/div-free-amr/1998-JCP-Dai-101006jcph19985944.pdf"
tags: [constrained-transport, godunov, staggered, mhd, shock-capturing, astrophysics]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A second-order, dimensionally split Godunov scheme for multidimensional
ideal MHD, with an approximate Riemann solver built on characteristic
invariants. Density, momentum and energy are cell averages; the magnetic
field is held as **face averages**, each component on its own set of
faces (eqs. 11–13). The face averages are advanced by the exact integral
form of the induction equation, with line- and time-averaged values of
$\mathbf u\times\mathbf B$ on cell edges (eqs. 18–23), so the net flux
through every cell surface never changes (eq. 24). No Poisson solve and no
source term are used.

The edge value is not built from upwind fluxes. The split Godunov sweep
also advances a cell-averaged field that is not divergence-free; the edge
value is $\mathbf u\times\mathbf B$ evaluated from velocity and field
averaged to the cell corner over four cells, at the old and new time
levels (§3.6, eqs. 50–51). This is the field-interpolated CT of later
classifications ([flux-CT](/methods/flux-ct.md)).

The authors claim that all eight conservation laws and the divergence-free
condition hold exactly at once. In their account projection breaks exact
conservation of $\mathbf B$, and Evans–Hawley CT does not conserve
exactly (§1). A Mach-15 shock–cloud run with and without the staggered
update gives "very close" solutions (§5).

# Key claims

1. **Conservation versus the constraint** (§1, p. 332). In all earlier
   multidimensional Godunov MHD schemes "either the conservation laws or
   the divergence-free condition of the magnetic field is satisfied only to
   the accuracy of schemes"; in supersonic flow the truncation errors "may
   be O(1)". On the "cleaning-up" by a Poisson projection after each step
   (stated, not tested):
   * it needs global information, which parallel machines do not favour;
   * "derivatives have to be directly evaluated for divergence";
   * it "may destroy the conservative property": after it, the $\mathbf B$
     conservation law "is satisfied only to the accuracy of the schemes,
     although the cleaning-up conserves the magnetic field analytically".

   Evans & Hawley's CT, as used by Stone & Norman, satisfies the constraint
   exactly "although the conservation laws are satisfied to the accuracy of
   the algorithms".
2. **Structural observation** (§2, p. 334; §5, pp. 364–365). The
   conservation law for $B_x$ has no $x$-derivative. This is what lets
   eight conservation laws and the divergence-free condition hold exactly
   in eight difference equations. Face averages and staggered grids are
   "generally… not favored in hyperbolic systems of conservation laws", but
   pay off here.
3. **Mixed representation** (eqs. 7, 11–14). Fluid variables are cell
   averages; the field components are face averages, the independent
   variables. The cell-averaged field is "only… intermediate", initialized
   from the faces. A face average is well defined even when a
   discontinuity coincides with the face.
4. **Discrete divergence** (eqs. 15–17). The net face flux of a cell,
   area-weighted differences of the three face components (eq. 15), is
   zero in every cell "if and only if" the field is discretely
   divergence-free (eq. 16); 2D form eq. 17.
5. **Field update, exact in integral form** (§3.1, eqs. 18–26). Each face
   average changes by the edge-length-weighted differences of space–time
   edge averages of $\mathbf u\times\mathbf B$ (eq. 23); "Eqs. (18)–(20)
   are exact" and the net flux "does not change with time" (eq. 24). In 2D
   (eqs. 25–26) the edge values sit at cell corners, and $B_z$ is the cell
   average updated by the conservative eq. 6. The fluid may be split or
   unsplit, but "the magnetic field … should be updated in an unsplit
   manner in order to exactly maintain the divergence-free condition"
   (p. 336).
6. **The provisional cell field** (§3.2, eqs. 27–28). The Strang-type
   sequence of eq. 27 updates the fluid **and** a cell-averaged field that
   "does not exactly satisfy the divergence-free condition" and serves
   "only for an approximate calculation of the time-averaged flux". The
   initial cell field is the two-face average (eq. 28, "simplest choice").
7. **The edge value** (§3.6, eqs. 47–51). In 2D, the corner value is
   $\mathbf u\times\mathbf B$ of the time-averaged corner velocity and
   field; the new-level corner values are plain four-cell averages of the
   split-updated cell values (eqs. 50–51). In 3D the edge line averages
   "are approximately calculated through" the updated cell values; the
   stencil is not printed. No upwind dissipation enters the edge value
   except through the split Godunov update that produced the cell values.
8. **Operator form** (§5, eq. 52). Two field updates per pair of split
   sweeps: field update, $x$–$y$–$z$ sweeps, field update, $z$–$y$–$x$
   sweeps. The field update is claimed to fit any 1D operator and unsplit
   Godunov schemes as well.
9. **Riemann solver** (§§3.3–3.5, eqs. 29–46). Characteristic invariants,
   time-averaged interface states from a $6\times6$ linear system whose
   coefficients use upwind-signed absolute values (eqs. 43–45). The normal
   field is constant in the solver and takes the face value. Vanishing
   field components are set to a machine-level small value, which "will
   not influence the exact satisfaction of the conservation laws and the
   divergence-free condition" (§3.5).
10. **Reconstruction** (§3.4). Linear profiles with van Leer's
    monotonicity constraint; effective left/right states per wave family.
    Using one state for all families drops the scheme to first order.
11. **The cell-centred divergence is not controlled** (§5, p. 365). The
    cell-averaged fields "do not exactly maintain the divergence-free
    constraint"; its value "is interpolation-dependent", and "for the
    problems presented in this paper, the divergence is O(1) if strong
    shocks are involved, no matter what kind of interpolation is used".
12. **Open question, stated** (§5, p. 365): "it remains unknown whether or
    not truncation errors in the divergence-free condition in the existing
    Godunov schemes have serious influences on the dynamics for supersonic
    MHD flows if conservation laws are exactly satisfied"; the authors "are
    unable to and do not intend to fully answer the question".
13. **Exact vector potential** (§4.2, p. 349). In 2D the $z$ component of
    the potential follows from the face fluxes "without involving any
    approximation"; field lines are its contours.
14. **Parallel scaling** (§4, p. 363, Fig. 22). No global solver. Cray
    T3E, $64^3$ cells per processor: 0.10187, 0.81767, 6.52350 and 12.75963
    GFLOP/s on 1, 8, 64 and 125 processors; a linear speed-up "may be
    expected" at 512.
15. **Future direction** (§5). A Riemann solver for multidimensional
    problems "arising from grid points, instead of interfaces" for the edge
    fluxes.

**Divergence treatment, in sum.** Staggered face averages updated by the
integral induction law with one edge value per edge: a CT-type update,
though the paper does not use the name. No projection, no source term, no
cleaning. The face invariant is stated to stay "exactly the same as its
initial value all the time in all these simulations" (§4, p. 343); no
value is printed.

# Tests

Uniform grids, $\gamma = 5/3$, Courant number "around 0.6" (§4). No error
norms or convergence rates are printed anywhere.

1. **1D fast and slow waves** (§4.1, Figs. 1–2): ten wavelengths, grids of
   256 down to 8 cells; "no difference may be observed" between 256 and 128
   cells. Plots only.
2. **1D fast shock** (Figs. 3–4), $B_x = 5$, 256 cells: "starting errors"
   from discontinuous initial data, which "almost disappear" with a small
   initial shock structure.
3. **1D shock tubes** (Figs. 5–7, Tables 1–2), $B_x = 5$, 512 cells,
   $t = 0.06$: two fast shocks; two fast and two slow shocks; two fast
   shocks and two rotational discontinuities, with exact intermediate
   states tabulated.
4. **2D smooth waves at 30°** (§4.2, Figs. 8–10): linear and nonlinear
   fast waves, an Alfvén wave; qualitative.
5. **Rotated shock tubes at 45°** (§4.2, Figs. 11–13), $256^2$,
   $t = 0.06$, the data of Figs. 3, 5, 6 rotated
   ([rotated shock tube](/benchmarks/rotated-shock-tube.md)). 45° was
   chosen "only because it is easy to set initial conditions which exactly
   satisfy the divergence-free condition". The jump conditions are
   satisfied; "there were O(1) truncation errors in the jump conditions if
   the scheme is not conservative for any one of eight conserved
   quantities". The scheme "does not have mechanisms to maintain the
   constant" normal field. Read off the plot axes: flat at 5 in Figs.
   11–12; a dip to about 4.99997 in Fig. 13.
6. **Orszag–Tang** (Figs. 14–15): $\beta_0 = 10/3$, $M_0 = 1$, $128^2$
   to $512^2$, $t = 0.5$; qualitative.
7. **2D MHD Riemann problem** (Figs. 16–17), four quadrants, uniform field
   $(2, 0, 1)$, $512^2$.
8. **Shock–cloud runs** (Figs. 18–20): Mach-10 shock on a 10× cloud;
   Mach-12 shock on "MHD"-letter clouds 50× denser (robustness).
9. **3D magneto-convection** (Fig. 21), $128^3$ on 64 T3E processors.
10. **With versus without the field update** (§5, Figs. 23–26): Mach-15
    shock on a 10× cloud, $384\times256$. Without it the split cell-centred
    field is used ("constraint satisfied to second-order accuracy").
    Density: "very hard to find differences"; $B_x$ very close, the
    exact-constraint run "cleaner in the tail behind the cloud"; $B_y$
    close "except near the front of the cloud".

# Notation map

| Dai & Woodward | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $b_x, b_y, b_z$ (face averages, eqs. 11–13) | $B_h \in V_h^2$ | the evolved field |
| $\mathbf B_{i,j,k}$ (cell average) | $B_h^{*}$ | provisional field of the split base scheme |
| $\Omega \equiv \mathbf u\times\mathbf B$; edge averages $\bar\Omega$ (eqs. 21–23) | $-E_h \in V_h^1$, at $n+1/2$ | **sign:** $\Omega = -E$ |
| eqs. 15–16 | $D_h^{\mathrm f} B_h$ times cell volume | the held invariant |
| eqs. 18–20, 25–26; operator $D_{\Delta t}$ (eq. 52) | $B_h^{n+1} = B_h^n - \Delta t\, C_h E_h^{n+1/2}$ | **collision:** $D_{\Delta t}$ is the field update, not a divergence |
| $L^x$ (1D split operator) | words | |
| $A_z$ (§4.2) | $A_h$ | in 2D the edge is the cell corner |
| $\Delta x_i$, $\Delta t$ | $h$, $\Delta t$ | uniform grids in all tests |
| $\alpha$ (rotation angle; also polytropic index in §4) | words | **collision:** $\alpha^{\mathrm{LF}}$, $\mathcal E^{\alpha}$ |
| $c_f, c_s, c_a$, $R_0$, $dR_{f\pm}$, $\delta$ | words | Riemann-solver internals |

# Pages created or updated

* Updated [Flux-CT and the Godunov CT variants](/methods/flux-ct.md): field-interpolated CT from its primary sources; "not yet ingested" replaced.
* Updated [Constrained transport](/methods/constrained-transport.md): the integral derivation of the Godunov-CT update and the unsplit-field rule.
* Updated [CT–finite-volume equivalence](/results/ct-finite-volume-equivalence.md): which cell-centred field the field-CT primary source carries.
* Updated [Exact discrete divergence](/properties/exact-discrete-divergence.md): face invariant asserted, cell-centred divergence O(1) at strong shocks.
* Updated [Staggered grid](/definitions/staggered-grid.md): only the field is staggered.
* Updated [Tóth (2000)](/sources/toth-2000.md): "DW not yet ingested" replaced.
* Updated [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) (the set-up and runs as printed, §4.2).
* Updated [Rotated shock tube](/benchmarks/rotated-shock-tube.md) (the 45° runs, Figs. 11–13).
* Updated [Projection method (divergence cleaning by Poisson solve)](/methods/projection-method.md) (the objection to projection, §1, and the Open `Contradictions` entry on conservation at discontinuities).

# Citations

1. `~/papers/mosaic/div-free-amr/1998-JCP-Dai-101006jcph19985944.pdf`.
   * **Version read.** The publisher's typeset version of record (Academic
     Press, 39 pp.; article no. CP985944). Received 14 October 1996,
     revised 19 February 1998.
   * **Identity.** doi:10.1006/jcph.1998.5944 (not printed in the PDF; from
     the archive filename), checked on Crossref: title and authors match;
     vol. 142, issue 2, pp. 331–369, issued May 1998; reference count 40.
   * **How it was read.** Text extraction, all sections; pp. 336, 337, 342,
     355–357 and 364 rendered and checked visually (eqs. 18–28, 47–49, 52;
     Figs. 11–13, 22).
   * **Recorded as printed.**
     * Eq. 49 prints $\Omega_y$ for the $z$-edge value; by symmetry with
       eqs. 47–48 $\Omega_z$ is meant (reader's reading).
     * p. 337 twice says "Eq. (28)" where eq. 27 is meant.
     * The Fig. 2 text says "five different grids" and lists six.
     * The Fig. 5 caption tuple lacks one zero; Table 2 prints
       $u_y^L = -3.12543\mathrm{E}{-01}$ against $-0.312542$ in the text.
     * The Fig. 12–13 captions refer one figure off from the text and the
       plots; the text is taken as correct.
     * The Mach-10 cloud postshock $B_z$ is printed $-7.73718$ against a
       preshock $+2$; likely a sign misprint, not resolved.
     * The 3D edge interpolation and the coefficients of eqs. 33–35,
       43–45 are not fully specified.
   * **Reference list.** 40 entries, all merged. Balsara's "Total variation
     diminishing scheme for magnetohydrodynamics", printed as submitted to
     J. Comput. Phys. without a year, was merged into `balsara-1998-b`
     (ApJS 116:133). LeVeque's 1988 journal version and 1992 second edition
     are noted on `leveque-1987` and `leveque-1990`. The bibliography holds
     3711 entries after this batch.
