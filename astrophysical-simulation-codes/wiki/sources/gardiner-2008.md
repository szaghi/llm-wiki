---
type: Source
title: "Gardiner & Stone (2008) — An unsplit Godunov method for ideal MHD via constrained transport in three dimensions"
description: "3D extension of the CTU+CT scheme behind Athena: minmod-limited multidimensional induction terms in the PPM interface states, the contact-upwinded corner EMF of 2005 reused unchanged, a 12-solve CTU (CFL ≤ 1) that is only sketched for MHD and a 6-solve CTU (stable for CFL < 1/2, observed) given in full and preferred, with 3D field-loop, linear-wave, circularly polarized Alfvén, inclined Riemann and low-beta blast-wave tests."
resource: "doi:10.1016/j.jcp.2007.12.017"
source_kind: paper
authors: [Gardiner T.A., Stone J.M.]
year: 2008
venue: "J. Comput. Phys. 227:4123–4141"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2008-JCP-Gardiner-101016jjcp200712017.pdf"
tags: [mhd, constrained-transport, unsplit, time-integration, verification, benchmark]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper extends the 2D CTU+CT scheme of
[Gardiner & Stone (2005)](/sources/gardiner-2005.md) to three dimensions,
changing two of its three parts. (1) The PPM characteristic interface-state
step gains minmod-limited multidimensional terms from the induction
equation, chosen to respect the balance that $\nabla\cdot\mathbf B = 0$
implies (§3.1, eqs. 8–20). (2) The CTU integrator gains source terms next
to the transverse flux gradients (§4). The third part, the corner EMF, is
the contact-upwinded construction of 2005, reused unchanged. Two 3D CTU
variants are compared: Saltzman's 12-solve algorithm, stable for Courant
numbers up to 1, which for MHD needs complicated source-term corrections and
is only sketched; and a new 6-solve variant, stable only below 1/2, given
in full and preferred (§4.2, §6). Tests are field-loop advection oblique to
the grid, linear waves of all four families, circularly polarized Alfvén
waves with a magnetic-helicity diagnostic, a Ryu–Jones Riemann problem
inclined to the grid, and a 3D low-β blast wave (§5). See
[unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md),
[constrained transport](/methods/constrained-transport.md) and
[Athena](/software/athena.md).

# Key claims

Equations are in the [registry](/notation.md) notation (see the Notation
map).

1. **Why the scheme is unsplit** (§1). With directional splitting the
   divergence-free constraint cannot be enforced between partial updates
   unless all three field components are updated together, which would
   break the independence of the split operators.
2. **Field-loop criterion** (§1, §5.1). For a loop in an $x$–$y$ plane
   advected with $v_z \neq 0$, $B_z$ evolves spuriously in any conservative
   scheme that does not satisfy $\nabla\cdot\mathbf B = 0$ on the stencil
   of the $B_z$ fluxes; a conservative scheme that keeps $B_z = 0$ satisfies
   the constraint on that stencil.
3. **3D interface states** (§3.1, eqs. 8–16). Before the characteristic
   step, each component of the induction equation receives a limited
   amount of the transverse terms, through limiter functions constrained in
   pairs (eq. 11). Minimizing the magnitude of the summed terms gives the
   minmod limiter, $\mathrm{minmod}(a, b) = \mathrm{sign}(a)\min(\vert a\vert,\vert b\vert)$
   if $ab > 0$ and 0 otherwise (eqs. 15–16): when $\partial_xB_x$ and
   $\partial_yB_y$ have opposite signs the smaller is added and subtracted,
   so that the reduced term attaches to one flux gradient; with equal signs
   the equation is left unmodified.
4. **The $x$-interface system** (eqs. 17–20), using $\nabla\cdot\mathbf B = 0$:
   $$\begin{aligned}
   &\partial_tB_x = 0,\\
   &\partial_tB_y + \partial_x(v_xB_y) - B_x\partial_xv_y - v_y\,\mathrm{minmod}(\partial_xB_x,\ -\partial_yB_y) = 0,\\
   &\partial_tB_z + \partial_x(v_xB_z) - B_x\partial_xv_z - v_z\,\mathrm{minmod}(\partial_xB_x,\ -\partial_zB_z) = 0,
   \end{aligned}$$
   with the derivatives taken from the face fields (eq. 20). In 2D this
   reduces to the 2005 interface states; with $\partial_x = 0$ the
   $x$-interface state equals the cell-centre state.
5. **Corner EMF** (§4 intro). The contact-upwinded EMF of the 2005 paper
   (its eqs. 41 and 50), "shown to have the best properties", is used in both
   3D variants; it reduces to the Godunov EMF for grid-aligned plane-parallel
   flow. CT is framed as a predictor (Godunov electric fields) and corrector
   (CT electric fields).
6. **12-solve CTU** (§4.1, eqs. 21–34; after Colella 1990, Saltzman 1994,
   Miller & Colella 2002). PPM states and fluxes; each state advanced by
   $\Delta t/3$ of a *single* transverse flux gradient, giving cross fluxes;
   states advanced by $\Delta t/2$ of the transverse gradients built from
   the cross fluxes; final Riemann solves and update. "Optimally stable for
   CFL numbers ≤ 1". As written it is not a useful MHD method: the parallel
   gradients enter in primitive form and the transverse ones in conservative
   form, so the MHD source terms are dropped and the result is formally first
   order, with secular field evolution in the field-loop test. The authors
   implemented the corrections but do not give them.
7. **6-solve CTU for MHD** (§4.2, eqs. 35–50). For Euler it is the 12-solve
   scheme without the $\Delta t/3$ step. For MHD:
   1. PPM states with the §3.1 terms; Riemann fluxes (eq. 35);
   2. CT edge EMFs from these fluxes, with a cell-centre reference EMF from
      $t^n$;
   3. states advanced by $\Delta t/2$ of the transverse flux gradients plus
      $\tfrac{\Delta t}{2}$ times source terms (eqs. 36–37): momentum
      $\mathbf B\,\partial_xB_x$, **not limited** (eq. 38); energy
      $B_yv_y\,\mathrm{minmod}(-\partial_zB_z,\ \partial_xB_x) + B_zv_z\,\mathrm{minmod}(-\partial_yB_y,\ \partial_xB_x)$
      (eq. 39); the interface-normal $B_x$ by a $\Delta t/2$ loop of edge EMFs
      (eq. 40); the transverse $B_y$, $B_z$ by $\Delta t/4$ edge-EMF
      differences on both sides plus $\tfrac{\Delta t}{2}v_y\,\mathrm{minmod}(-\partial_zB_z,\ \partial_xB_x)$
      and $\tfrac{\Delta t}{2}v_z\,\mathrm{minmod}(-\partial_yB_y,\ \partial_xB_x)$
      (eqs. 41–46);
   4. Riemann fluxes at $t^{n+1/2}$ (eq. 47);
   5. CT EMFs at $t^{n+1/2}$, the reference EMF from face-averaged
      $\mathbf B^{n+1/2}$ and from $\rho$, $\rho\mathbf v$ after a conservative
      $\Delta t/2$ update with the step-1 fluxes (eq. 48);
   6. finite-volume update and CT update of the face fields (eqs. 49–50).

   No source terms are needed for the interface-normal field. The scheme
   reduces exactly to 2D CTU and to 1D PPM under the corresponding
   symmetry. It is "stable for CFL < 1/2", observed experimentally, with no
   proof. Two 6-solve steps at a Courant number of 1/2 cost about one
   12-solve step at 1.
8. **Preference** (§6). Both variants are "accurate and robust for
   approximately the same computational cost"; the 6-solve is preferred "as
   a result of its simplicity and smaller memory footprint". The 3D
   interface-state algorithm is called "a new and essential element".
9. **Accuracy and the Courant number** (§5.3, §6). The dominant
   L1-error difference between the two variants on smooth waves comes from
   the Courant-number dependence of the truncation error.
10. **Scope** (§6). Static and adaptive mesh refinement with these
    integrators is left to a future paper; the integrators were already used
    for the MRI and the magnetic Rayleigh–Taylor instability (refs. 2, 18).

# Tests

No test states the Riemann solver or, for the 6-solve runs, the Courant
number; no time-step formula is printed. $\gamma = 5/3$ is implied by
$p = 1/\gamma = 3/5$ (§5.2).

1. **[Field-loop advection](/benchmarks/field-loop-advection.md)** (§5.1,
   eqs. 51–52, Figs. 1–2). Domain $[-0.5,0.5]^2\times[-1,1]$ with
   $N\times N\times2N$ cells, periodic; $\rho = 1$, $p = 1$,
   $\mathbf v = (1, 1, 2)$. The loop axis is along $(-1, 0, 2)/\sqrt5$; the
   vector potential along it is $10^{-3}$ times (0.3 minus the distance from
   the axis) inside radius 0.3, zero outside, with periodic images. The
   volume-averaged $B^2$ fits $C\left[1 - (t/\tau_{\mathrm{fit}})^{\alpha_{\mathrm{fit}}}\right]$
   with time constants $3.22\times10^2$, $3.68\times10^3$, $2.65\times10^4$ and
   exponents 0.365, 0.328, 0.320 for $N = 32$, 64, 128 (2D: $1.061\times10^4$
   and 0.291). The normalized mean absolute axial field converges at about
   first order and concentrates on the loop axis and edge, where the initial
   current is singular (Fig. 2). For a $z$-invariant loop both 3D schemes
   reproduce the 2D algorithm exactly and keep $B_z = 0$. 6-solve throughout.
   The velocity is **not** perpendicular to the loop axis: its component
   along the axis is $3/\sqrt5$ (computed at reading).
2. **[Linear waves](/benchmarks/linear-wave-convergence.md)** (§5.2,
   eqs. 53–56, Fig. 3, App. A). Amplitude $10^{-6}$; background $\rho = 1$,
   $p = 3/5$, $\mathbf B = (1, 3/2, 0)$, velocity 1 along the wave for the
   entropy mode and 0 otherwise, giving slow, Alfvén and fast speeds 1/2, 1
   and 2. Domain $[0,3]\times[0,1.5]^2$ on $2N\times N\times N$ cells,
   periodic; rotation angles with sines $2/3$ and $2/\sqrt5$, wavelength 1,
   field from a vector potential, run to one wave crossing. Error: per
   component L1 with cell-centred $\mathbf B$, combined in quadrature.
   Second order for fast, Alfvén, slow and entropy waves with both schemes;
   the 6-solve errors are lower except for the slow wave. $N$ from 16 to 512
   (6-solve fast and Alfvén) or 256. App. A prints the eigenvectors in the
   conserved order $(\rho, \rho\mathbf v, \mathbf B, E)$.
3. **[Circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md)**
   (§5.3, eqs. 57–58, Figs. 4–6). Along-wave field 1, transverse field and
   velocity amplitudes 0.1, $\rho = 1$, $p = 0.1$ (plasma beta about 0.2),
   along-wave velocity 0 (travelling) or 1 (standing, sign as printed);
   domain and rotation of §5.2; parameters after Tóth (2000); no parametric
   instability seen. Vector-potential initialization leaves magnetic-pressure
   truncation errors that drive compressive waves. Both schemes converge at
   second order; the travelling wave has the larger error. The 12-solve run
   at Courant number 0.4 matches the 6-solve run; at 0.8 it gives a slightly
   lower travelling and a higher standing error. The helicity of the
   fluctuating field shows dissipation plus oscillations of period 1/2 whose
   amplitude scales as $N^{-2}$ (Fig. 6).
4. **Riemann problem inclined to the grid** (§5.4, eqs. 59–63, Fig. 7).
   Ryu & Jones test 2a: left $\rho = 1.08$, $\mathbf v = (1.2, 0.01, 0.5)$,
   $\mathbf B = (2, 3.6, 2)/\sqrt{4\pi}$, $p = 0.95$; right $\rho = 1$,
   $\mathbf v = 0$, $\mathbf B = (2, 4, 2)/\sqrt{4\pi}$, $p = 0.95$; rotation
   integers $(1, 2, 4)$, with translation invariance used to fill ghost
   cells (eq. 63); $768\times8\times8$ cells on
   $[-0.75,0.75]\times[0,1/64]^2$, $h = 1/512$, $t = 0.2$, 6-solve.
   Dissipation "nearly identical" to 1D PPM at the same resolution, with
   oscillations at the slow, Alfvén and fast discontinuities. The cell-centred
   normal field already oscillates at amplitude about $8.26\times10^{-3}$ in
   the initial data; averaging over "macrocells" removes it.
5. **[MHD blast wave](/benchmarks/mhd-blast-wave.md)** (§5.5, Fig. 8).
   Londrillo & Del Zanna (2000) parameters in 3D: unit cube
   $[-0.5,0.5]^3$, $200^3$ cells; $\rho = 1$, $\mathbf v = 0$,
   $B_x = B_z = 10/\sqrt2$, $B_y = 0$; $p = 100$ (plasma beta 2) inside
   radius 0.125, $p = 1$ (beta 0.02) outside; **$t = 0.02$** (text and
   caption); slices at $y = 0$. Ranges: density 0.190–2.98, pressure
   1.0–42.4, magnetic energy density 25.2–64.9, kinetic energy density
   0–33.1. The maximum slow-shock compression, about 3.3, is "the same as was
   found in the 2D calculation". The 6-solve scheme is robust at
   $\beta_{\mathrm p}\sim10^{-2}$ and keeps the symmetry. Boundary
   conditions not stated.

# Notation map

| Paper | Registry | Note |
|---|---|---|
| $\rho$, $\rho\mathbf v$, $\mathbf B$, $E$ | same | units with unit permeability; the Riemann test uses $/\sqrt{4\pi}$ values |
| $P$ | $p$ | gas pressure |
| $P^* = P + \mathbf B\cdot\mathbf B/2$ | $P^*$ | |
| $\epsilon$ | $\rho e$ | internal energy density |
| $q$, $\bar q$ | $u$ | conserved state |
| $F_x$, $\mathcal F_x(q_L, q_R)$ | $\hat f_{i+1/2}$ | $F^*$ predictor, $F^{n+1/2}$ corrector |
| $q^*_{Lx,i+1/2}$, $q^*_{Rx,i+1/2}$ | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | |
| $\mathcal E^*$, $\mathcal E^{n+1/2}$, $\mathcal E^c$ | $\boldsymbol{\mathcal E}$ | edge EMFs; "$\mathcal E^c$" names the contact-upwinded variant |
| $\delta x$, $\delta y$, $\delta z$; $\delta t$ | $h$; $\Delta t$ | the paper allows different spacings per direction |
| CFL number | $\nu$ | |
| $L_{xy}$, … | in words | limiter functions |
| $S_x$ | in words ("source terms") | numerical terms of the directional step, not physical sources $s(u)$ |
| $c_s$ (§5.2) | in words ("slow speed") | **collision**: registry $c_s$ is the sound speed |
| $c_a$, $c_f$ | $c_A$, $c_f$ | |
| $c$ (wave speed, §5.2) | in words | **collision** with the speed of light |
| $\lambda$ (wavelength) | in words | **collision risk** with eigenvalues |
| $x_1, x_2, x_3$ (rotated frame) | in words | **collision**: registry $x_i$ is a cell centre |
| $\alpha$, $\beta$ (rotation angles); $\alpha$, $\tau$ (loop fit) | in words; $\alpha_{\mathrm{fit}}$, $\tau_{\mathrm{fit}}$ on this page only | **collisions** with $\alpha_{\mathrm L}$, $\beta^i$, $\beta_{\mathrm p}$, $\tau$ |
| $\beta = 2P/B^2$ | $\beta_{\mathrm p}$ | |
| $N$ | $N$ | cells per dimension |
| $H$, $\mathbf a$, $\mathbf b$, $\mathbf B_0$ | in words | helicity diagnostic |

# Pages created or updated

* Created this Source page.
* Updated [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md):
  the 3D primary source; the 12↔$\nu\le1$ and 6↔$\nu<1/2$ pairing is
  printed first here; the quoted "as accurate" and "dramatically simpler"
  are Stone et al.'s wording.
* Updated [Athena](/software/athena.md): the same attribution, the reused
  2005 EMF, the 3D blast at $\beta_{\mathrm p} = 0.02$.
* Updated [Field-loop advection](/benchmarks/field-loop-advection.md): the
  original 3D set-up; its velocity is not perpendicular to the loop axis.
* Updated [MHD blast wave](/benchmarks/mhd-blast-wave.md): a third 3D run,
  to $t = 0.02$; flag on the recorded 2005 output time.
* Updated
  [linear wave convergence](/benchmarks/linear-wave-convergence.md),
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md),
  [constrained transport](/methods/constrained-transport.md) and
  [Stone et al. (2008)](/sources/stone-2008.md).

# Citations

1. Gardiner T.A., Stone J.M. (2008), "An unsplit Godunov method for ideal
   MHD via constrained transport in three dimensions", J. Comput. Phys.
   227(8):4123–4141, doi:10.1016/j.jcp.2007.12.017. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2008-JCP-Gardiner-101016jjcp200712017.pdf`.
   * **Version read.** The published journal version (Elsevier typeset,
     19 pp.; received 14 September 2006, revised 10 July 2007, accepted
     15 December 2007). Not a preprint.
   * **Identity.** Checked on Crossref: title, the two authors, vol. 227,
     issue 8, pp. 4123–4141, issued 2008-04.
   * **How it was read.** Text layer for prose; every equation used here
     was checked on rendered pages (pp. 3–11, 16, 18 of the PDF), because the
     text layer drops minus signs, $\nabla$, $\epsilon$ and $\gamma$.
   * **Recorded as printed.** (a) Eqs. 39 and 40 lack the "=" sign; the
     left-hand side of eq. 39 is the energy source term. (b) The Fig. 1
     caption names the mean squared axial field, the text and the panel the
     mean absolute axial field. (c) The standing Alfvén wave has along-wave
     velocity $+1$ with transverse velocity and field perturbations of the
     same sign; that pairing is self-consistent (the wave then moves toward
     negative along-wave coordinate; reader's reading). (d) The $\mathcal E^c$
     formulas, the 12-solve MHD corrections, the Riemann solver, the 6-solve
     Courant number and the blast-wave boundary conditions are not given.
   * **Reference list:** 20 printed entries, merged complete. Evans &
     Hawley, printed ApJ 322:659, lands on `evans-1988` (332:659). No DOIs
     printed. Bibliography: 2407 entries.
