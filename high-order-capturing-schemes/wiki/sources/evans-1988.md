---
type: Source
title: "Evans & Hawley (1988) — Simulation of magnetohydrodynamic flows: a constrained transport method"
description: "The origin of constrained transport: the induction equation in integral (Stokes) form for the flux through a moving surface, face-averaged field components on a mesh staggered against the hydrodynamic faces, edge electromotive forces computed once and used with opposite signs in the two faces that share them, so the total flux out of every cell keeps its initial value to round-off, in any coordinates, in 3D and on a moving mesh; tested in 2D axisymmetric black-hole accretion against vector-potential codes."
resource: "doi:10.1086/166684"
source_kind: paper
authors: [Evans C.R., Hawley J.F.]
year: 1988
venue: "Astrophys. J. 332:659–677"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1988-ApJ-Evans-101086166684.pdf"
tags: [mhd, divergence-free, constrained-transport, staggered-mesh, vector-potential]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper writes the ideal-MHD induction equation for the contravariant
velocity and the magnetic vector density (the field times the square
root of the 3-metric determinant). In that form it has a Cartesian
flux-difference appearance in any curvilinear coordinates, Newtonian or
general-relativistic in 3+1 form. The integral form, for the magnetic
flux through a moving surface, leads to **constrained transport (CT)**:
face-averaged field components on a staggered mesh, electromotive forces
(EMFs) on cell edges, and each face flux updated by the discrete Stokes
theorem. Each edge EMF is computed once and enters the two faces that
share it with opposite signs, so the total flux out of every cell, the
discrete divergence, keeps its initial value to round-off, in 3D and on a
moving, stretched mesh, with no restriction on the transport order. In 2D
axisymmetry the EMF is built from averaged velocities times upwind
(van Leer) interpolated field densities. Tests compare CT with
vector-potential codes using monotone, Wilson and donor-cell transport:
square-wave advection and three Schwarzschild black-hole accretion
problems. CT avoids the anomalous current oscillations that come from
differentiating a monotonically advected potential twice, and keeps the
normalized divergence near $10^{-15}$.

# Key claims

1. **Induction without the metric** (§IIa, eqs. 2.1–2.6). For the vector
   density $\gamma^{1/2}B^i$ and the contravariant velocity the induction
   equation is a pure flux difference and the constraint a plain
   coordinate divergence, in arbitrary curvilinear coordinates; the
   orthonormal ("physical") components of earlier work bring the metric
   back in (p. 660).
2. **General relativity** (§IIb, eq. 2.8; App. eqs. A1–A17). In the 3+1
   form the shift enters only as a velocity offset; the constraint keeps
   its form.
3. **Integral form on a moving surface** (§IIc, eqs. 2.9–2.12; App. b,
   eqs. A18–A22). The rate of change of the magnetic flux through a
   surface moving with the grid velocity is a contour integral of the
   EMF built from the velocity relative to the grid (eq. 2.12), "the
   basis" of the constraint-preserving adaptive-mesh algorithm.
4. **Staggering** (§IVa–b, eqs. 4.1–4.6, Figs. 1–2). Hydrodynamic
   scalars sit at zone centres, velocities and momenta at face centres.
   The field components are face-centred "in a different way from the
   velocity and momentum terms" (p. 664): in Fig. 1 each field component
   shares a location with the *transverse* velocity component, so the CT
   control volume is the dual cell centred on a hydrodynamic zone corner
   (Fig. 2). Face values are flux averages (eqs. 4.5–4.6).
5. **Discrete divergence** (eqs. 4.7–4.9). The six face fluxes of each
   cell sum to zero: the face-flux (Gauss) divergence. On a moving mesh
   it must hold with the new fluxes and the new zone increments (p. 665).
6. **Edge EMFs and the Stokes update** (§IVc, eqs. 4.10–4.13). The rate
   of change of each face flux is minus the sum of the four edge EMFs
   around it (eq. 4.10); the EMF of an edge is the line integral of the
   electric field built from the velocity relative to the grid and the
   shift (eqs. 4.11–4.12); the face updates (eqs. 4.13a–c) have the signs
   of the Yee update on the [constrained-transport page](/methods/constrained-transport.md)
   (reader's check at 220 dpi).
7. **Proof of preservation** (§IVc, p. 665, Fig. 2). Summing the face
   updates over a cell, the total flux "continues to vanish if it did
   originally, even though the cell position and shape may change",
   because "each EMF edge contribution appears in the full sum exactly
   twice with opposite signs"; the edge EMFs "are calculated *once* even
   though each contribution is used in two separate evolution
   equations". The authors compare this with flux conservation in the
   continuity equation.
8. **Only changes are divergence-free** (p. 666). "The CT scheme only
   guarantees that field evolution *changes* are divergence free. If the
   initial magnetic field fails to satisfy the constraint, it will
   continue to do so." Inflow and outflow boundaries can admit
   non-solenoidal field; a global divergence measure (eq. 5.6) should be
   monitored.
9. **Edge-collocated vector potential** (eqs. 4.14–4.17, 4.25). The
   magnetic flux is the circulation of $\mathbf A$, so $\mathbf A$ sits on
   the EMF edges, and the face fields defined as its discrete curl
   (eq. 4.17) satisfy the discrete divergence exactly: properly posed
   initial data and inflow. In 2D the potential is recovered from the
   evolved field (eq. 4.25). CT is "simply obtaining a monotonic
   distribution of" the derivatives of the potential "rather than of"
   the potential (p. 667).
10. **2D axisymmetric EMF** (§IVd, eqs. 4.18–4.24). The same EMF product
    is a transport term in one face equation and a shear term in the
    other: "These terms must be differenced in a consistent manner.
    Hence upwind differencing is required for each such term" (p. 666).
    Velocities are plain averages to the edge (eq. 4.21); the field is
    upwind-interpolated with van Leer's harmonic-mean slope (eqs.
    4.22–4.24). Donor cell ("not recommended"), van Leer and PPM are the
    named transport options (p. 667).
11. **Adaptive mesh** (p. 666). The remap is built into the update to
    keep the field divergence-free: "A straightforward differencing of
    the adaptive mesh equation (2.10) would be disastrous to constraint
    satisfaction."
12. **Generality** (abstract, §§I, IVd). CT works in arbitrary
    coordinates, places no restriction on the transport order, works in
    3D, admits an adaptive mesh and extends to non-ideal MHD (the current
    term enters the electric field and Stokes' theorem still applies,
    p. 667). The order, 3D and non-ideal claims are asserted, not tested:
    every run is 2D, ideal and second order.
13. **Why not a vector potential** (§III, eqs. 3.1–3.2). The Lorentz force
    needs second derivatives of $\mathbf A$. Against Choptuik's
    Richardson-hypothesis argument that the order is kept, monotone
    schemes violate Richardson's hypothesis near sharp features and give
    anomalous current reversals in second differences. CT is the second
    of Ramshaw's three options (vector potential, constraint built into
    the difference equations, divergence cleaning); the finite-difference
    Stokes analogue is credited to Schnack and Killeen (p. 665).
14. **Parallel force** (§III, p. 661). A nonzero divergence "can produce
    an anomalous force *parallel* to the magnetic field, especially when
    one uses the conservative form of the momentum equation", citing
    Brackbill and Barnes, whose nonconservative $\mathbf J\times\mathbf B$
    differencing reduced kinetic-energy errors "by a factor of 4000";
    $\mathbf J\times\mathbf B$ still "yields inaccurate results when the
    magnetic field cannot be trusted". No sign or formula of the force is
    given.
15. **Scope** (§§I, VI). Induction only; the Lorentz-force differencing is
    deferred to a later paper.

# Tests

The CT code is the authors' black-hole hydrodynamics code plus induction,
in second-order monotone (van Leer) mode. The vector-potential codes
advect the azimuthal potential with monotone, donor-cell or "Wilson"
(a weighted mix of Lax–Wendroff and donor cell) transport (§V, eq. 5.1).
No convergence study, error norms, cost data, field shocks or 3D runs.

1. **Cartesian square wave** (§Va, Figs. 3a–b). A unit square wave of
   $B_x$, 50 zones wide, advected 250 zones in $y$ at Courant number 1/2.
   CT-monotone spreads each discontinuity over about 16 zones with no new
   extrema; the field differenced from a monotonically advected $A_z$ is
   slightly sharper but has new extrema (overshoot to about 1.2); Wilson
   rings, donor cell diffuses. The current (ideally two delta-function
   sheets) is two clean peaks with CT, and oscillates "with a rather
   substantial amplitude", changing sign, with monotone-$A_z$ and Wilson.
   "a donor cell implementation of CT is identical to the donor cell
   vector potential scheme" (p. 668).
2. **Radial accretion onto a Schwarzschild hole** (§Vb, eqs. 5.2–5.6).
   $64\times64$ axisymmetric spherical-polar mesh to $r = 100M$, a
   low-pressure inflow carrying a weak field ($k = l = 10^{-4}$), run to
   $t = 1320M$. The radial field agrees with the analytic steady state
   "to within 0.04% for all calculations"; the azimuthal field's errors
   are "on order 0.5%". The normalized divergence (eq. 5.6) starts at
   about $10^{-15}$ and grows by round-off to $10^{-10}$ by the end of one
   calculation; with the field evolution alone in double precision it
   stays at $10^{-15}$–$10^{-14}$.
3. **Infall of a closed field loop** (§Vc, Fig. 4), only 17 radial zones
   out to $r = 35M$. The CT current is smooth with the expected shape;
   the monotone-$A$ current shows "the usual anomalous oscillations in
   the second finite-difference derivative". CT "may therefore require
   slightly greater resolution", since $\mathbf A$ has a longer length
   scale. This is not the [field-loop advection](/benchmarks/field-loop-advection.md)
   benchmark.
4. **Accretion-disk formation** (§Vd, Figs. 5–6). No analytic solution.
   The CT potential, reconstructed, is "quite similar" to the
   vector-potential code's; currents from two derivatives of $\mathbf A$
   show extra extrema on the $2h$ scale, while the CT current is "much
   smoother without being diffusive". The divergence stays near
   $10^{-15}$.

# Notation map

| Evans & Hawley (1988) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathscr B^i = \gamma^{1/2}B^i$ | $\mathbf B$ (Cartesian, $\gamma = 1$); words otherwise | **collision**: registry $\mathcal B_i$ is the troubled-cell flag, $\gamma$ the ratio of specific heats |
| $V^i$ | $\mathbf v$ | |
| $V_g^i$ | words (grid velocity) | |
| $\alpha$, $\beta^i$, $\gamma_{ij}$ | words (lapse, shift, 3-metric) | **collision**: Lax–Friedrichs $\alpha$, smoothness $\beta_k$ |
| $\mathscr F_{i+1/2,j+1/2,k}$ (line-integrated edge EMF) | $h_z\,\bar{\mathcal E}_{z;i+1/2,j+1/2,k}$ | with $\boldsymbol{\mathcal E} = -\mathbf v\times\mathbf B$; eqs. 4.13 match the registry Yee signs |
| $\mathscr E$ (contour EMF) | $\oint\boldsymbol{\mathcal E}\cdot d\mathbf l$ | **collision risk** with the field $\boldsymbol{\mathcal E}$ |
| $\Phi_S$ (face magnetic flux) | words | **collision**: registry $\Phi$ is the projection potential |
| $(\mathscr B^x)_{i+1/2,j,k}$ | $\bar B_{x;i+1/2,j,k}$ | **index collision**: in the paper $x_i$ is a zone corner and $x_{i+1/2}$ a zone centre; the indices coincide with the registry's because the CT cell is the dual cell |
| $A_k$ | $\mathbf A$ | edge-collocated |
| $\Delta x_i$ (centre separation), $\Delta x_{i+1/2}$ (zone width) | $h$ | integer and half-integer meanings reversed against the usual convention |
| $\Delta_r$, $\delta_r$ | words (raw and van Leer harmonic-mean slope) | |
| $\xi$ (eq. 5.6) | words (normalized divergence) | **collision**: registry $\xi$ is the scaled wavenumber |

# Pages created or updated

* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md)
  (batch-17 block: the origin, staggering, pairwise cancellation, the
  edge vector potential, the moving-mesh form, the motivation against a
  monotone vector potential).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/1988-ApJ-Evans-101086166684.pdf`.
   * **Version read.** The published version as a NASA ADS scan, 19
     pages, image only (`pdftotext` returns only the ADS bibcode).
     Received 1987 November 23; accepted 1988 March 9.
   * **Identity.** doi:10.1086/166684, checked on Crossref: "Simulation of
     magnetohydrodynamic flows - A constrained transport method", Evans
     and Hawley, Astrophys. J. 332:659, issued 1988-09; page 1 prints
     332:659–677, 1988 September 15, with a colon in the title. The year
     is 1988 on page 1 and on Crossref (one citing source prints 1989).
   * **How it was read.** Every page from rendered images at 130 dpi;
     eqs. 4.11–4.13, 4.16–4.24, Fig. 1 and the reference list re-checked
     at 200–250 dpi. Equations are reproduced on the Source page only
     where legible; the appendix is summarized only where used.
   * **Recorded as printed** (reader's reading).
     - There is no method-of-characteristics content: the EMF uses
       averaged velocities and upwind interpolation of the field.
     - Eq. 4.20b was read at 130 dpi only; its sign structure is legible.
     - Eq. 5.4 prints "sin·θ", presumably $\sin\theta$.
     - Fig. 4 shows the current "at time $t = 132M$", the instant the
       inflow is closed (the new $t = 0$), in both caption and text.
   * **Reference list:** 32 printed entries (ApJ style, no article
     titles), all merged. Hawley, Smarr & Wilson 1984a, printed ApJ
     277:276, lands on `hawley-1984` (277:296), and 1984b on
     `hawley-1984-b`. Blandford & Payne, MNRAS 199:883 (Crossref), is the
     new `blandford-1982`; the entry previously under that key, Blandford's
     single-author 1976 paper as printed by Roe & Balsara, was rekeyed
     `blandford-1976` (Crossref). Bibliography: 3270 entries.
