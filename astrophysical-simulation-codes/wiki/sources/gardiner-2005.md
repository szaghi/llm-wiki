---
type: Source
title: "Gardiner & Stone (2005) — An unsplit Godunov method for ideal MHD via constrained transport"
description: "Origin of the 2D CTU+CT scheme behind Athena: consistency relations tying the finite-volume fluxes of the cell-centred field to the corner EMFs, proof that arithmetic EMF averaging halves the numerical viscosity of grid-aligned flow, three upwind-gradient corner-EMF constructions of which the contact-upwinded one is selected, multidimensional source terms in the PPM characteristic step and in the CTU transverse correction, and 2D tests with second-order linear-wave convergence in all families."
resource: "doi:10.1016/j.jcp.2004.11.016"
source_kind: paper
authors: [Gardiner T.A., Stone J.M.]
year: 2005
venue: "J. Comput. Phys. 205:509–539"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2005-JCP-Gardiner-101016jjcp200411016.pdf"
tags: [mhd, constrained-transport, unsplit, verification, benchmark]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds a single-step, second-order, fully conservative,
directionally unsplit Godunov scheme for 2D ideal MHD from
[PPM](/methods/ppm.md) interface states, Colella's corner transport upwind
(CTU) integrator and face-centred
[constrained transport](/methods/constrained-transport.md). It derives the
relations that tie the finite-volume fluxes of the cell-centred field to
the corner EMFs of CT, shows that arithmetic averaging of the face EMFs
halves the numerical viscosity of grid-aligned plane-parallel flow and so
does not reduce to the 1D scheme, and builds the corner EMF as an
integration from face centres to corners with three gradient choices, of
which the contact-upwinded one is selected. It shows that the PPM
characteristic step needs multidimensional terms proportional to the
normal derivative of the normal field, and that CTU must be extended for
MHD by a CT half-step of the face fields in the predictor and by further
source terms in the transverse correction. The scheme reduces exactly to
the 1D algorithm for plane-parallel, grid-aligned flow. Tests: field-loop
advection, circularly polarized Alfvén waves, a rotated shock tube, linear
waves, a current sheet and an MHD blast wave. Only 2D is treated; 3D
"will be presented elsewhere" (§6). Merged into
[constrained transport](/methods/constrained-transport.md),
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md) and
[Athena](/software/athena.md).

# Key claims

Section and equation numbers are those of the arXiv v1 preprint read
(see Citations).

1. **Against directional splitting** (§1; §2.1, after eq. 12). The fluxes
   of the volume-averaged field are nonzero only for the transverse
   components, so split updates "will not generally satisfy the divergence
   free constraint between directional sweeps"; hence the unsplit CTU.
2. **CT as the fundamental representation** (§2.2, eqs. 13–18).
   Face-area-averaged in-plane field components, updated by Stokes'
   theorem from time-averaged corner EMFs (eqs. 14–15), with
   $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$. Keeping
   $\nabla\cdot\mathbf B = 0$ "in an integral sense" is "as fundamental as
   ... the conservation of mass in a finite volume method". Cell-centred CT
   (Tóth 2000) keeps a divergence on "a different (larger) stencil".
3. **Cell-centred field** (eqs. 19–20): the mean of the two face values,
   "sufficient for second order accuracy".
4. **Finite-volume–CT consistency** (§2.3, eqs. 21–24). Requiring eqs.
   19–20 at $t^{n+1}$ forces the $B_x$ component of the $y$-flux at face
   $(i, j+1/2)$ to equal $\tfrac12(\mathcal E_{z,i-1/2,j+1/2} + \mathcal E_{z,i+1/2,j+1/2})$
   (eq. 23), and the $B_y$ component of the $x$-flux at face $(i+1/2, j)$
   to equal $-\tfrac12(\mathcal E_{z,i+1/2,j-1/2} + \mathcal E_{z,i+1/2,j+1/2})$
   (eq. 24). The Godunov fluxes of the cell-centred transverse field are
   therefore replaced by these averages, "regardless of the details of the
   CT algorithm".
5. **Arithmetic averaging fails** (§3.2.1, eqs. 34–38). With the corner
   EMF the mean of the four face EMFs (eq. 34), a plane-parallel,
   grid-aligned flow gives eq. 38: "the numerical viscosity is reduced by a
   factor of 2", so the scheme "does not reduce to the underlying
   integration algorithm" and "the stability of this approach is
   questionable"; the cause is "the lack of a directional bias". The paper
   reads Balsara & Spicer (1999) as built on this average, with
   shock-sensor weights to restore a bias. Doubling the viscous
   contribution (eqs. 39–40: twice the four-face mean minus the mean of
   the four surrounding cell-centre EMFs) does reduce to the 1D scheme.
6. **Corner EMF by integration to the corner** (§3.2.2, eq. 42): the mean
   of the four face EMFs plus $h/8$ times differences of EMF derivatives
   at the quarter points on either side of the corner, each derivative a
   one-sided difference between a face EMF and a cell-centre reference EMF
   from the cell-centred state, written face minus centre for the quarter
   point on the $+x$ side of the centre (eqs. 45–46). Three variants:
   * a Lax–Friedrichs flux of the differentiated induction equation, with
     a maximum wave speed (eqs. 43–44, 47–49), the paper's
     $\mathcal E_z^\alpha$;
   * its zero-speed limit $\mathcal E_z^\circ$, identical to eqs. 39–40 and
     to averaging the two neighbouring derivatives (eq. 50), "not an
     upwinded approximation"; for a first-order Godunov scheme identical to
     the CT of Londrillo & Del Zanna (2004);
   * $\mathcal E_z^c$ (eq. 51): the derivative taken from the upwind cell
     by the sign of the face-normal velocity (the mass flux), the mean when
     it is zero, hence usable with "any approximate or exact Riemann
     solver". Selected for all second-order tests.
   All three reduce exactly to the 1D scheme for plane-parallel
   grid-aligned flow and "differ only in their numerical viscosity for
   multidimensional problems". Because the cell-size factors cancel, they
   apply also to corner-reconstruction schemes (Balsara), with the corner
   state EMF in place of the cell-centre one, and to wave-propagation and
   central schemes (§6).
7. **Multidimensional terms in the PPM characteristic step** (§3.1, eqs.
   25–33). In primitive variables the 2D induction equation carries terms
   in the normal derivative of the normal field absent in 1D. The
   $x$-direction characteristic evolution of the seven primitive variables
   without $B_x$ gets a term $v_y\,\partial_x B_x$ in the $B_y$ equation,
   evaluated as $v_{y,i}(B_{x,i+1/2} - B_{x,i-1/2})/h$ (eq. 32); the $y$
   sweep gets $v_x\,\partial_y B_y$ in the $B_x$ equation. The $B_z$
   equation is rewritten with $\nabla\cdot\mathbf B = 0$ (eq. 28) and gets
   no term here. The interface normal field is the face value, not
   reconstructed. Without these terms "the field loop disintegrates in
   oscillations before completing a fraction of an orbital period"
   (§3.3.1).
8. **CTU extended for MHD** (§4, eqs. 57–78). The hydrodynamic transverse
   update (eqs. 57–60) "fail[s] to preserve the $\nabla\cdot\mathbf B = 0$
   condition". Two changes: (a) the face fluxes are integrated to the
   corners with a CT EMF (eqs. 65–68), equivalent to a CT half-step of the
   face normal fields to $t^{n+1/2}$ (eqs. 69–70); (b) source terms
   $\tfrac{\Delta t}{2}$ times (eqs. 61–64, 72–73)
   $$s_{x,i,j} = \left(0,\ B_x,\ B_y,\ B_z,\ 0,\ 0,\ v_z,\ B_zv_z\right)^{\mathsf T}_{i,j}\ \frac{B_{x,i+1/2,j} - B_{x,i-1/2,j}}{h}$$
   in the conserved order $(\rho, \rho\mathbf v, \mathbf B, E)$, and the
   analogue in $y$, needed because primitive interface states are not
   formally advanced by $\Delta t/2$ (eq. 71). The $v_z\,\partial_xB_x$ term
   sits here and not in the characteristic step: otherwise a loop advected
   with uniform $v_z$ grows a spurious coherent $B_z$; with this choice
   $B_z$ stays at round-off "with an incoherent structure" (§4.1.2).
9. **Corrector EMF** (§4.2, eqs. 74–78): the same construction with the
   reference EMF $v_yB_x - v_xB_y$ evaluated at $t^{n+1/2}$ (eq. 75), the
   cell-centred field from the half-step face fields, density and momenta
   from a half-step finite-volume update.
10. **Algorithm** (§4.3, 8 steps): PPM interface states with the
    multidimensional terms; Riemann solve; $\mathcal E_z^c$ corner EMFs;
    transverse update with source terms; second Riemann solve;
    $\mathcal E_z^c$ at $t^{n+1/2}$; CT update of the face fields;
    finite-volume update of the rest. "Second order accurate, unsplit, and
    preserves the $\nabla\cdot\mathbf B = 0$ constraint throughout the time
    step"; "ideally suited for use on a statically or adaptively refined
    mesh" (§1, §6; stated, not shown).
11. **Riemann solver**: the Roe linearization of Cargo & Gallice (1997) in
    all tests (§1, §3.3); the construction is claimed compatible with any
    solver (HLL, HLLC, Dai–Woodward, Einfeldt named, §3.2). No carbuncle
    fix is mentioned.
12. **Time step**: printed only for the first-order tests,
    $\Delta t = 0.4\min\left(h/\max_p\vert\lambda^{(p)}_x\vert,\ h/\max_p\vert\lambda^{(p)}_y\vert\right)$
    (eq. 52), "restrictive CFL stability limit". No Courant number is
    printed for the CTU+CT tests of §5.
13. **Scope** (§6): 2D only; the 3D extension "principally involves
    modifications to the 'source terms'"; gravity and Coriolis sources are
    "readily incorporated", to be "described in a later paper".

# Tests

First-order single-step scheme (§3.3; PPM interface states, Roe,
$\nu = 0.4$):
1. **[Field loop](/benchmarks/field-loop-advection.md)** (§3.3.1, Figs. 1–3,
   eq. 53). Domain $[-1,1]\times[-0.5,0.5]$, $2N\times N$ with $N = 64$,
   periodic; $\rho = 1$, $p = 1$; velocity $\sqrt5\,(2/\sqrt5, 1/\sqrt5, 0)$
   (advection; one orbit along the grid diagonal by $t = 1$) or zero
   (diffusion); in-plane field from a $z$ vector potential
   $10^{-3}(0.3 - r)$ inside radius 0.3, zero outside; plasma beta
   $2\times10^6$ inside. Stationary loop at $t = 2$: the Lax–Friedrichs
   variant shows "unacceptable" diffusion (a central hole by
   reconnection); $\mathcal E_z^\circ$ and $\mathcal E_z^c$ are
   "essentially identical" with very small diffusion. Advected loop:
   $\mathcal E_z^\circ$ oscillates, dominating by $t = 2$; the
   Lax–Friedrichs variant and $\mathcal E_z^c$ are similar. $\mathcal E_z^c$
   is judged preferable.
2. **[Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)**
   (§3.3.2, Figs. 4–5). Modified from Tóth (2000): domain
   $[0,\sqrt5]\times[0,\sqrt5/2]$, $2N\times N$ with $N = 8$, periodic,
   wavevector at $\tan^{-1}2$, wavelength 1; $\rho = 1$, $p = 0.1$; field
   1 along the wavevector and transverse components of amplitude 0.1 in
   quadrature; velocity along the wavevector 0 (travelling) or 1
   (standing); $t = 5$. Standing wave: the Lax–Friedrichs variant's
   dissipation is "approximately twice" the others'. No parametric
   instability for these parameters.

Second-order CTU+CT (§5; $\mathcal E_z^c$, Roe; Courant number not
printed):
3. **Field loop** (§5.1, Figs. 6–8): as above, $128\times64$, $t = 2$.
   Dissipation concentrates at the loop centre and edge, where the initial
   current is singular. The volume-averaged $B^2$ fits
   $3.463\times10^{-8}\left[1 - (t/10{,}614)^{0.2914}\right]$ (Fig. 7; it
   falls to about $3.1\times10^{-8}$ by $t = 2$, read from the plot).
   Field lines keep a circular shape; the innermost is dissipated by
   $t = 2$. One resolution only.
4. **Circularly polarized Alfvén wave** (§5.2, Fig. 9): $N = 4, 8, 16, 32$
   at $t = 5$, standing and travelling. Planar symmetry kept;
   "compare well" with published results; no parametric instability. **No
   error norm or convergence order** is reported.
5. **Rotated shock tube** (§5.3, Fig. 10). Rotations by 45° keep the
   field component along the wavevector constant to round-off. A
   non-trivial case after Tóth: square cells, $256\times128$, rotation
   $\tan^{-1}2$, the Ryu & Jones (1995, Fig. 1a) states with
   $(\rho, v_\parallel, p) = (1, 10, 20)$ left and $(1, -10, 1)$ right,
   both with field components $5/\sqrt{4\pi}$ along and across, $t = 0.08$.
   The cell-centred field along the wavevector oscillates by "roughly 10%",
   most at the fast shocks; the Lax–Friedrichs variant does not reduce it,
   so it is not a CT-dissipation defect. Averaged onto macro-cells of
   $2\times1$ cells, it is constant to round-off (also for $3\times2$ and
   $5\times4$): grid-scale transverse variations of the discrete solution.
6. **[Linear waves](/benchmarks/linear-wave-convergence.md)** (§5.4,
   Fig. 11, App. A). Domain $[0, 2/\sqrt5]\times[0, 1/\sqrt5]$,
   $2N\times N$, periodic, wavevector at $\tan^{-1}2$, wavelength stated as
   2/5; amplitude $10^{-6}$; $\rho = 1$, $p = 3/5$, $\gamma = 5/3$, field
   $(1, \sqrt2, 1/2)$ in the wave frame, background velocity 1 along the
   wavevector for the entropy mode only; slow, Alfvén and fast speeds 1/2,
   1 and 2; one wavelength of travel. Error: per-component L1 norm over
   cells, combined as the square root of the sum of squares (eqs. 80–81).
   Fitted orders (Fig. 11): **fast 2.0, Alfvén 2.26, slow 2.29, entropy
   2.11**; L1 errors between about $10^{-7}$ and $10^{-10}$ for $N$ from
   about 8 to 128 (plot axes). With PLM instead of PPM the error scales as
   $N^{-2}$ in all modes, with a slightly larger amplitude.
7. **Current sheet** (§5.5, Fig. 12, eq. 82). Domain $[0,2]^2$,
   $256\times256$, periodic; $\rho = 1$, $p = 0.1$; $B_y = 1$ for
   $x < 1/2$ and $x > 3/2$, $-1$ between; $v_x = 0.1\sin(\pi y)$. Field
   lines at $t = 0$ to 4: the numerical resistivity depends on the field's
   orientation to the grid; islands form by $t = 1$, migrate and merge
   until two per sheet remain. Qualitative robustness test.
8. **[MHD blast wave](/benchmarks/mhd-blast-wave.md)** (§5.6, Fig. 13).
   Londrillo & Del Zanna (2000) parameters: $[-0.5,0.5]^2$, $200\times200$,
   $\rho = 1$, $\mathbf v = 0$, $B_x = B_y = 10/\sqrt2$; $p = 100$ (plasma
   beta 2) inside radius 0.125, $p = 1$ (beta 0.02) outside; adiabatic,
   $\gamma = 5/3$; $t = 0.2$. Density 0.192–3.31, pressure 1.0–32.1,
   magnetic energy density 23.5–77.7; "stable and accurate for low-β plasma
   problems involving strong MHD shock waves", symmetric, "no indication of
   grid related artifacts".

No Orszag–Tang vortex is run.

# Notation map

| Gardiner & Stone (2005) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $q$ | $u$ | conserved vector $(\rho, \rho\mathbf v, \mathbf B, E)$ |
| $f_x$, $f_y$ | components of $\mathbf f(u)$ | |
| $F_{x,i+1/2,j}$, $F_{y,i,j+1/2}$ | $\hat f_{i+1/2}$ per direction | time- and face-averaged |
| $\delta x$, $\delta y$, $\delta t$ | $h$, $\Delta t$ | the paper allows $\delta x \ne \delta y$ |
| $P$, $P^*$ | $p$, $P^*$ | permeability 1, $P^* = p + B^2/2$ |
| $E$ | $E$ | total energy density |
| $\epsilon$ | $\rho e$ | **collision:** the paper's $\epsilon$ is an internal energy density, the registry $e$ is specific |
| $\mathbf E$, $\mathcal E_z$ | $\boldsymbol{\mathcal E}$, $\mathcal E_z$ | corner-centred in 2D CT |
| $\mathcal E_z^\alpha$, $\mathcal E_z^\circ$, $\mathcal E_z^c$ | words for the first; $\mathcal E_z^\circ$, $\mathcal E_z^c$ kept as variant names | as on the IDEFIX Source page |
| $\alpha$ (eqs. 47–49) | none (words: Lax–Friedrichs speed) | **collision:** registry $\alpha_{\mathrm L}$, $\alpha_{\mathrm c}$; the paper reuses $\alpha$ for the Fig. 7 fit exponent |
| $\lambda^{\max}_{x,y}$ | $\max_p\vert\lambda^{(p)}\vert$ per direction | |
| $V$, $\tilde V$, $A$ (eq. 33) | none (words: primitive state, primitive wave matrix) | **collision:** registry $A(u)$ is the conserved flux Jacobian |
| $\sigma$, $S_{x,i,j}$ | $s$ | numerical multidimensional terms, not physical sources |
| $q^{L*}$, $q^{R*}$; $q^L$, $q^R$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | predictor and corrected states |
| $D$ (eq. 36) | none (words: viscosity matrix) | |
| $A_z$, $A_0$, $R$ | none (words: vector potential, amplitude, radius) | **collision:** with $A(u)$ |
| $\beta = 2P/B^2$ | $\beta_{\mathrm p}$ | |
| $c_s$ (§5.4) | none (words: slow magnetosonic speed) | **collision:** registry $c_s$ is the sound speed |
| $c_a$, $c_f$ | $c_A$, $c_f$ | |
| $\varepsilon$, $\lambda$ (§5.4) | none (words: amplitude, wavelength) | bare $\lambda$ would clash with the eigenvalues |
| $\theta$, $x_1$, $B_1$, … | none (words: rotated frame) | |
| $N$ | $N$ | grid $2N\times N$ |

# Pages created or updated

* Created this Source page.
* Updated [Constrained transport](/methods/constrained-transport.md):
  consistency relations, the arithmetic-averaging argument, the three
  corner-EMF variants and the macro-cell result.
* Updated [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md):
  the 2D CTU+CT construction, its source terms and time-step statements.
* Updated [Athena](/software/athena.md), [Enzo](/software/enzo.md).
* Updated benchmarks: [field-loop advection](/benchmarks/field-loop-advection.md),
  [linear wave convergence](/benchmarks/linear-wave-convergence.md),
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
  [MHD blast wave](/benchmarks/mhd-blast-wave.md).

# Citations

1. Gardiner T.A., Stone J.M. (2005), "An unsplit Godunov method for ideal
   MHD via constrained transport", J. Comput. Phys. 205(2):509–539,
   doi:10.1016/j.jcp.2004.11.016. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2005-JCP-Gardiner-101016jjcp200411016.pdf`.
   * **Version read.** The arXiv preprint astro-ph/0501557v1 (25 January
     2005, 45 pages, Elsevier preprint template; the footer date "22
     October 2018" is the arXiv re-render date), not the typeset journal
     version. Section, equation and figure numbers are those of v1 and were
     not compared with the journal version.
   * **Identity.** Checked on Crossref: title, the two authors, J. Comput.
     Phys. 205(2):509–539, issued May 2005; Crossref's reference count
     (33) matches the printed list.
   * **How it was read.** Text layer for prose and for unambiguous
     equations (eqs. 14–15, 19–24, 34–42, 52, 57–70, 74–78); the matrices
     and multi-line equations (eqs. 32–33, 46–51, 72–73, 79–81) and the
     rotated-shock states were read from rendered pages 12, 17, 18, 27, 33
     and 35. Figures are images; Fig. 7 and Fig. 11 values beyond the
     printed fit and legend are plot readings.
   * **Recorded as printed.** The linear-wave initial condition (eq. 79)
     prints the phase as $\cos(2\pi x_1)$, i.e. wavelength 1, next to the
     stated wavelength 2/5; in this domain and angle only wavelengths
     $2/(5n)$ are periodic (computed at ingestion). The Fig. 9 legend lists
     grids from $128\times64$ to $8\times4$, the text $N = 4$ to 32 plus the
     $N = 64$ initial condition. No Courant number for the CTU+CT tests;
     no boundary conditions for the blast wave. The paper does not name
     the code; its acknowledgements thank P. Teuben for "contributions to
     the implementation".
   * **Reference list:** 33 entries. Evans & Hawley printed ApJ 322:659
     (Crossref 332:659) lands on `evans-1988`; 19 title-less entries gained
     their titles in the merge; references printed without a year (two
     arXiv-only, one in press) are keyed with inferred years, noted in the
     entries. The bibliography holds 2200 entries after the merge.
