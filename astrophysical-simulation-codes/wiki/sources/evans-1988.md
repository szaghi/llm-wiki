---
type: Source
title: "Evans & Hawley (1988) — Simulation of magnetohydrodynamic flows: a constrained transport method"
description: "Origin of constrained transport: the induction equation in integral form for the magnetic flux through each face of a staggered cell, updated by line-integrated edge EMFs that each enter two faces with opposite signs, written metric-free for general relativity on a moving, stretching grid, with a van Leer upwind EMF in 2D axisymmetry and kinematic tests only."
resource: "doi:10.1086/166684"
source_kind: paper
authors: [Evans C.R., Hawley J.F.]
year: 1988
venue: "Astrophys. J. 332:659–677"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1988-ApJ-Evans-101086166684.pdf"
tags: [mhd, constrained-transport, relativity, conservation, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper introduces [constrained transport (CT)](/methods/constrained-transport.md).
The induction equation is written in integral form for the magnetic flux
through each face of a staggered cell; each face flux changes by the
line-integrated EMFs on its four edges, a finite-difference Stokes
theorem. Every edge EMF is computed once and used, with opposite signs,
by the two faces that share it, so the net flux out of each cell (the
finite-difference divergence) keeps its initial value to round-off. The
derivation is general relativistic (3+1 split): for the magnetic vector
density $\sqrt{\det\gamma_{ij}}\,B^i$ and contravariant velocities, the
induction equation has a "Cartesian" form in any coordinates and on a
moving mesh, with the shift entering only through the net velocity. In
2D axisymmetric spherical-polar coordinates the EMF is a van Leer upwind
interpolation of the field times an equal-weight average of the
velocity. All tests are **kinematic**: the Lorentz force "is left to a
later paper" (§I). They are square-wave advection on a Cartesian grid and
three Schwarzschild accretion problems, comparing CT with
vector-potential codes. The main claims are that CT gives the current
from one derivative of an evolved field, without the sign oscillations of
the vector-potential current, and keeps a normalized divergence
diagnostic at $10^{-15}$–$10^{-10}$. The induction equations are added to
the existing general-relativistic hydrodynamics code of Hawley, Smarr &
Wilson (1984b, "HSWb"), to which every hydrodynamic detail is deferred.

# Key claims

Equations are in the [registry](/notation.md) notation where it has the
symbols, otherwise in words (see the Notation map).

1. **Scope** (abstract, §I, p. 660). CT works in arbitrary coordinate
   systems, places no restriction on the order of accuracy of the
   transport scheme, works in 3D as well as 2D, allows an adaptive mesh
   "in a natural way" and presents no barrier to nonideal MHD. It keeps
   the divergence of the poloidal (constrained) field "to within machine
   round-off error".
2. **Metric-free induction equation** (§IIa–b, eqs. 2.4–2.8; App. A).
   For the vector density $\sqrt{\det\gamma_{ij}}\,B^i$ the induction
   equation contains only partial derivatives of the products of
   velocity and vector density, and the constraint is the vanishing of its
   partial-derivative divergence (eqs. 2.4, 2.6). This needs the
   contravariant velocity and field; "physical" (orthonormal) components
   "reintroduce the metric". In general relativity the velocity is the
   transport velocity (the spatial four-velocity components divided by the time component) minus the shift $\beta^i$, and the
   equation keeps the flat-space form (eq. 2.8). Ideal MHD:
   $\alpha_{\mathrm L}\mathcal E_i = -\epsilon_{ijk}v^jB^k$ (eq. A14).
3. **Integral form on a moving surface** (§IIc, eqs. 2.9–2.12). The rate
   of change of the magnetic flux through a surface moving with the grid
   velocity is minus the EMF around its boundary, the contour integral of
   the net velocity (transport minus grid minus shift) crossed with the
   vector density (eq. 2.12). This "becomes the basis of our
   constraint-preserving adaptive mesh numerical transport algorithm".
   "Adaptive mesh" here means one moving, stretching grid (grid velocity,
   eqs. 2.10–2.12, 4.20), not a hierarchy of refined grids.
4. **Against the vector potential** (§III, eqs. 3.1–3.2). The current in
   $\mathbf J\times\mathbf B$ needs second derivatives of the vector
   potential. To the concern of Norman, Clarke & Burns (1987) that each
   difference loses one order, the authors answer with Choptuik's (1986)
   Richardson argument: a smooth error keeps its order under
   differentiation. They place the real problem at sharp features, where
   monotonic and flux-correcting schemes change their local weights
   abruptly ("violates a tenet of Richardson's hypothesis") and produce
   "anomalous current, or force, reversals". Of Ramshaw's (1983) three
   ways to enforce $\nabla\cdot\mathbf B = 0$ (vector potential; the
   constraint built into the difference equations; cleaning with an
   extra scalar) they choose the second. Brackbill & Barnes (1980): a
   nonconservative ($\mathbf J\times\mathbf B$) momentum equation
   reduced kinetic-energy errors "by a factor of 4000", but this only
   hides an untrustworthy field (§III, p. 661).
5. **Mesh and centring** (§IVa, eqs. 4.1–4.3, Fig. 1). Zone corners are
   the paper's integer points, zone centres its half-integer points
   (eq. 4.2). Zone widths need not be constant; grids may stretch and
   move. Stretch beyond "several percent change from zone to zone"
   degrades the second-order truncation accuracy, but "the ability to
   construct a constrained transport scheme is unaffected by grid
   stretch". Hydrodynamic centring (from HSWb): $\rho$, $\rho e$, $p$,
   $W$, $\alpha_{\mathrm L}$ and $\gamma_{ij}$ at zone centres and integer
   time levels; velocities, grid velocity, momenta $S_i$ and the shift on
   zone faces at half-integer time levels.
6. **Field placement** (§IVb, eq. 4.4, Figs. 1–2). The paper places
   $\mathcal B^x$ at $(i+\tfrac12, j, k)$, $\mathcal B^y$ at
   $(i, j+\tfrac12, k)$ and $\mathcal B^z$ at $(i, j, k+\tfrac12)$ in its
   indices, at integer time levels: "face centered, but in a different
   way from the velocity and momentum terms". The CT control volume is
   "centered on $(i,j,k)$" (Fig. 2), a hydro-zone corner in the paper's
   convention. Per Fig. 1, this places each field component relative to
   the hydro zones as the figure labels show; see the field-layout note
   under Recorded as printed.
7. **Face field = flux / area** (eqs. 4.5–4.6): the face value is "the
   face area averaged flux".
8. **Discrete divergence = finite-difference Gauss theorem**
   (eqs. 4.7–4.9). The net flux through the six faces of the CT cell
   vanishes. On a uniform mesh, with the CT cell's centre at index
   $(i,j,k)$ and its faces at the half indices,
   $$\frac{B^x_{i+1/2,j,k} - B^x_{i-1/2,j,k}}{h} + \frac{B^y_{i,j+1/2,k} - B^y_{i,j-1/2,k}}{h} + \frac{B^z_{i,j,k+1/2} - B^z_{i,j,k-1/2}}{h} = 0 \qquad \text{(eq. 4.9)},$$
   written in the paper for the vector density and non-uniform widths.
   On a moving mesh it must hold with the new fluxes and the new zone
   widths.
9. **Finite-difference Stokes theorem and the update** (§IVc,
   eqs. 4.10–4.13). The time derivative of a face flux is minus the sum
   of the four edge EMFs (eq. 4.10, after Schnack & Killeen 1980). Each
   of the 12 edges carries a **line integral** along the edge of the EMF
   component parallel to it, built with the net velocity (eqs. 4.11–4.12).
   The update of a face flux from $t^n$ to $t^{n+1}$ adds the two edge
   integrals of one transverse direction and subtracts those of the other
   (eq. 4.13a; 4.13b–c analogous); the updates account for the changing
   zone widths.
10. **Why the divergence is preserved** (§IVc, p. 665, Fig. 2). Summing
    the six face updates, the total flux "continues to vanish if it did
    originally, even though the cell position and shape may change",
    because "each EMF edge contribution appears in the full sum exactly
    twice with opposing signs". "The edge EMF contributions are
    calculated *once* even though each contribution is used in two
    separate evolution equations", analogous to mass conservation by face
    fluxes. There is no separate proof: the argument is this
    cancellation.
11. **Vector potential on edges** (eqs. 4.14–4.17). The face flux is the
    circulation of the vector potential around the face, so the potential
    sits on the EMF edges as line averages, and its discrete curl
    (eq. 4.17) satisfies eq. 4.9 exactly. It is used to build
    divergence-free initial and inflow/outflow boundary fields,
    "regardless of the method used to evolve" the potential.
12. **Only changes are divergence-free** (§IVc, p. 666). "The CT scheme
    only guarantees that field evolution *changes* are divergence free.
    If the initial magnetic field fails to satisfy the constraint, it will
    continue to do so." Badly posed inflow/outflow boundaries "can lead to
    subtle inflow of nondivergence-free magnetic field"; a global
    constraint measure (eq. 5.6) should be monitored during runs.
13. **EMF in 2D axisymmetry** (§IVd, eqs. 4.18–4.24). With
    $(x,y,z) \to (r,\theta,\phi)$ and no $\phi$ dependence, $B^\phi$ is
    unconstrained and evolved directly (as in Clarke et al. 1986);
    $B^r$ and $B^\theta$ are constrained. The edge EMF is $-\Delta\phi$
    times the net-velocity–field cross product at the edge, from averaged
    velocities and upwinded fields (eq. 4.18). The updates (eqs. 4.20a–b)
    are written for field times zone width at both time levels: "The
    adaptive mesh remap algorithm is constructed in a very specific way in
    equation (4.20) to maintain divergence-free field"; a straightforward
    differencing of eq. 2.10 "would be disastrous to constraint
    satisfaction".
    * **Consistent upwinding.** In each update one field difference is a
      transport term and the other a shear term; "These terms must be
      differenced in a consistent manner. Hence upwind differencing is
      required for each such term." Each field is upwind-averaged in the
      direction of the velocity component it is paired with; velocities
      are a "direct equal-weight average" of the two neighbours
      (eq. 4.21).
    * **Recipe.** Raw one-sided slopes of the field (eq. 4.22); a van Leer
      limited slope, twice the product of the two adjacent raw slopes
      divided by their sum when they have the same sign, else zero
      (eq. 4.23); then the upwind, time-centred value at the edge, the
      upwind zone value plus half the limited slope times (zone width
      minus $\Delta t$ times the averaged velocity), with the mirror form
      for negative velocity (eq. 4.24; the zero-velocity case is not
      printed). Named alternatives: donor cell ("not recommended"), van
      Leer, PPM (Colella & Woodward 1984); consistent advection (Norman &
      Winkler 1986) can be added.
    * This is an upwind advection "flux" of each transverse field
      component, not a Riemann-solver (Godunov-flux) EMF and not the
      method of characteristics; no Alfvén characteristics enter,
      consistent with the kinematic scope.
14. **Nonideal MHD** (§IVd, p. 667): add the current term (eq. A13b) to
    the electric field; "Since Stoke's theorem still applies, properly
    constrained evolution equations can be written." Asserted, not tested.
15. **Recovering the potential** (eq. 4.25). Because the field is
    divergence-free, the azimuthal potential is recovered up to a
    constant by integrating in angle at fixed radius ($\theta = 0, \pi$
    give the boundary condition). CT "is related to a particular numerical
    approach for advecting the vector potential": in effect it makes the
    derivatives of the potential monotonic rather than the potential.
16. **Host code** (§V, p. 667). The induction equations are added to "an
    existing, calibrated black hole code (HSWb)", the 2D axisymmetric
    general-relativistic finite-difference hydrodynamics code of Hawley,
    Smarr & Wilson (1984b). The CT code uses second-order van Leer
    monotonicity. The vector-potential comparison codes advect the
    azimuthal potential by $-v^r\partial_r - v^\theta\partial_\theta$
    (eq. 5.1) with van Leer, donor cell, or the "Wilson scheme" (a
    weighted average of Lax–Wendroff and donor cell, HSWb). Operator
    splitting, artificial viscosity and the time integrator are not
    described, beyond the staggered time centring of claim 5. Runs on a
    CRAY X-MP/48 at NCSA (acknowledgments, p. 675).
17. **Conclusions** (§VI). CT "manifestly conserves magnetic flux through a
    closed surface, and hence maintains the constraint equation
    $\nabla\cdot\mathbf B = 0$ to machine roundoff"; "Constrained transport
    allows higher order schemes to be employed without sacrificing quality
    in the current." The relativistic Lorentz-force terms (displacement
    current, charge density) are the next challenge.

# Tests

All tests are passive or kinematic: the field does not act on the flow
(§I). CT (van Leer) is compared with vector-potential codes (van Leer,
Wilson, donor cell). Figure values are read off plots and approximate.

1. **Cartesian square-wave advection** (§Va, Figs. 3a–b). A unit square
   wave of $B^x$, 50 zones wide, advected 250 zones (5 widths) in $y$ at
   constant velocity, Courant number $\nu = 1/2$. CT spreads each
   discontinuity "across 16 grid zones". The monotonic-potential field
   has a "slightly smaller zone spread" but new extrema (overshoot to
   about 1.13). Wilson rings and is asymmetric; donor cell is
   diffusion-dominated (peak about 0.98, spread over about 100 zones).
   Current (ideal: two δ-function sheets): CT gives two clean peaks of
   about $\pm0.15$; the monotonic-potential and Wilson codes give
   "decidedly nonmonotonic currents" that change sign between the peaks;
   donor cell gives no new extrema but is "extremely diffusive". "A donor
   cell implementation of CT is identical to the donor cell vector
   potential scheme." A thought example (field linear in $y$, square
   current pulse): CT gives a non-oscillating force, the monotonic
   vector-potential code "spatially narrow oscillations of order unity in
   the current, a potentially disastrous result".
2. **Radial accretion onto a Schwarzschild black hole** (§Vb,
   eqs. 5.2–5.6). Outer boundary $100\,r_{\mathrm g}$; $64\times64$
   axisymmetric spherical-polar mesh, uniform in $\theta \in [0, \pi]$,
   logarithmic in $r$ from the horizon. Cold free-falling gas carries a
   field whose boundary potential is proportional to $\sin^2\theta$; a
   small angular momentum, also proportional to $\sin^2\theta$, generates a
   toroidal field; both amplitudes $10^{-4}$. Run to $1320\,r_{\mathrm g}/c$
   (2.6 free-fall times). During infall the monotonic potential gives the
   sharpest pulse, then CT, Wilson, donor cell. Steady state after two
   free-fall times. $B^r$ matches the steady solution (eq. 5.3) to within
   0.04 % in all codes, an error from the difference of $\sin^2\theta$
   (improvable by "numerical regularization", Evans 1986); $B^\phi$ spans
   three orders of magnitude with errors of about 0.5 % out to
   $50\,r_{\mathrm g}$; the error in the one steady current component is
   0.004 at all radii in all codes. Eq. 5.4 is not reproduced (see
   Recorded as printed).
   * **Divergence diagnostic** (eq. 5.6): the sum over the mesh of the
     absolute discrete divergence, divided by the sum over the mesh of
     $(\vert B^r\vert + r\vert B^\theta\vert)$ over (radial width plus $r$
     times angular width). It starts at about $10^{-15}$. Round-off
     "accumulates, but at a problem specific rate": $10^{-10}$ by the end
     of one calculation, only $10^{-13}$ in another (§Vd). "By
     calculating the evolution of the magnetic vector density components
     (only) in double precision the error remains on the order of
     $10^{-15}$–$10^{-14}$ throughout the simulations." The baseline
     precision is not stated.
3. **Infall of a closed field loop** (§Vc, Fig. 4). Radial inflow carries
   field onto the grid until $132\,r_{\mathrm g}/c$, then the inflow is
   closed and that state becomes the initial one; the vector-potential
   codes start from its potential. Run to $1053\,r_{\mathrm g}/c$ (about two
   free-fall times); 17 radial zones from the outer boundary to
   $35\,r_{\mathrm g}$, so diffusion is rapid. The monotonic schemes are
   least diffusive, the monotonic potential sharpest. The equatorial
   current should have three extrema: CT gives them cleanly (about +10,
   −18, +6), the monotonic potential adds spurious extrema, Wilson and
   donor cell are diffusive. "Accurate CT calculations may therefore
   require slightly greater resolution to maintain the same sharpness in
   the magnetic field", judged worth it to avoid sign oscillations in the
   force. The diagnostic stays near $10^{-15}$.
4. **Accretion-disk formation** (§Vd, Figs. 5–6). As test 2 with a large
   angular momentum (Keplerian orbit at $77\,r_{\mathrm g}$), a
   low-resolution repeat of Hawley (1986): strong shocks, a hot torus and
   an equatorial outflow that bends the field lines outward; no analytic
   solution. The CT current is "much smoother without being diffusive";
   the vector-potential currents have extra extrema "on the scale of
   $2\Delta x$", "almost certainly numerical in origin". The diagnostic
   starts at about $1.8\times10^{-15}$, dips to about $7\times10^{-16}$
   near $t \approx 450$ and stays flat near $10^{-15}$ to $t \approx 1350$
   (Fig. 6).

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\mathbf B$, $B^i$ | $\mathbf B$, $B^i$ | Gaussian units ($\mathbf J\times\mathbf B = (\nabla\times\mathbf B)\times\mathbf B/4\pi$, §III); $G = c = 1$ (App.) |
| $\mathcal B^i = \gamma^{1/2}B^i$ | $\sqrt{\det\gamma_{ij}}\,B^i$, "vector density" in words | **collision**: the paper's bare $\gamma$ is $\det\gamma_{ij}$; the registry $\gamma$ is the adiabatic index. In flat Cartesian coordinates it equals $B^i$ |
| $V^i = U^i/U^t$ | $v^i$ | transport velocity $dx^i/dt$, coordinate components |
| $V_g^i$ | grid velocity, in words | no registry symbol |
| $u^i = V^i - V_g^i - \beta^i$ | net velocity, in words | **collision**: $u$ is the registry state |
| $U^\mu$, $U_\phi$ | four-velocity and specific angular momentum, in words | the registry has no four-velocity symbol; $u$ is the state |
| $\alpha$, $\beta^i$, $\gamma_{ij}$ | $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$ | 3+1 symbols |
| $W$ | $W$ | generalized Lorentz factor, $\alpha_{\mathrm L}$ times the time component of the four-velocity |
| $\Phi_S$ | magnetic flux through a face, in words | **collision**: $\Phi$ is the gravitational potential |
| $\mathcal E$ (contour EMF), $\mathcal F$ (edge EMF) | $\boldsymbol{\mathcal E}$ times the edge length | $\mathcal F$ is line-integrated (eq. 4.11) and includes $\Delta\phi$ in 2D |
| $E^i$ (App.) | $\boldsymbol{\mathcal E}$ | |
| $A_k$, $A_\phi$, $A_z$ | vector potential, in words | **collision**: $A(u)$ is the flux Jacobian; the registry has no vector-potential symbol |
| $\Delta x_i$, $\Delta r_i$, $\Delta\theta_j$ | $h$ on a uniform mesh; zone width in words otherwise | non-uniform in the paper |
| integer $(i,j,k)$ = zone corner, half-integer = zone centre | $x_i$ centre, $x_{i+1/2}$ interface **of the CT cell** | opposite to the registry convention **relative to the hydro zones**; the paper's indices match the registry for the corner-centred CT cell |
| $\rho$, $p$, $\rho\epsilon$ | $\rho$, $p$, $\rho e$ | $\epsilon$ is the specific internal energy |
| $S_i$ | $S_i$ | relativistic momentum density |
| $J^i$ | $\mathbf J$ | |
| $\rho_e$, $\sigma$ | charge density, conductivity, in words | App. only |
| $\xi$ (eq. 5.6) | divergence diagnostic, in words | |
| $M$ | $M_{\mathrm{BH}}$; lengths in $r_{\mathrm g}$ | $G = c = 1$ |
| $k$, $l$ | field and angular-momentum amplitudes, in words | |
| $\Delta_r$, $\delta_r$ | raw and limited slopes, in words | |

# Pages created or updated

* Created this Source page.
* Updated [Constrained transport](/methods/constrained-transport.md): the
  origin of the method (integral form, edge line integrals, the
  twice-used-EMF cancellation, the moving mesh, the van Leer upwind EMF,
  the edge-centred vector potential, the initial-state caveat, the
  measured divergence floor, the kinematic scope); the layout difference
  from later codes per Fig. 1.
* Updated [IDEFIX](/software/idefix.md): its Evans–Hawley attribution and
  the "equivalent to the original CT" vector-potential statement checked
  against the primary source.

# Citations

1. Evans C.R., Hawley J.F. (1988), "Simulation of magnetohydrodynamic
   flows: a constrained transport method", Astrophys. J. 332(2):659–677,
   doi:10.1086/166684. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1988-ApJ-Evans-101086166684.pdf`.
   * **Version read.** The published journal version (1988 September 15),
     as the ADS scan `1988ApJ...332..659E`, 19 pages; received 1987
     November 23, accepted 1988 March 9. Not a preprint.
   * **Identity.** Checked on Crossref: title "Simulation of
     magnetohydrodynamic flows - A constrained transport method", the two
     authors, The Astrophysical Journal vol. 332, first page 659, issued
     1988-09; agrees with page 1. Gardiner & Stone (2005) print the volume
     as 322; 332 is correct, as the bibliography note already records.
   * **How it was read.** The PDF has no text layer (pdftotext returns
     only the ADS bibcode). Every page was read from rendered images at
     110–300 dpi; equations are transcribed only where legible.
   * **Recorded as printed.** (a) Eq. 5.4: the exponent of $\sin\theta$
     in the second term of the steady toroidal field is illegible even at
     300 dpi; the equation is not reproduced. (b) The zero-velocity case
     of eq. 4.24 is not printed. (c) "Double precision" for the field
     evolution (§Vb) is stated without the baseline precision. (d) The
     hydrodynamics (time integration, artificial viscosity, operator
     splitting) is not described; it is deferred to HSWb. (e) **Field
     layout.** Relative to the hydro zones, per Fig. 1 and eq. 4.4, the
     reader places $\mathcal B^x$ at the paper's $(x_{i+1/2}, y_j)$,
     co-located with $V^y$ and $S_y$, and $\mathcal B^y$ at
     $(x_i, y_{j+1/2})$, co-located with $V^x$ and $S_x$, with the 2D edge
     EMF at the hydro-zone centre $(i+\tfrac12, j+\tfrac12)$ (eq. 4.18).
     This rests on the reading of Fig. 1 and is stated only "per Fig. 1".
   * **Reference list:** 32 entries (13 on p. 676, 19 on p. 677), ApJ
     style without titles for journal articles and with no DOIs; titles
     only for books. Hawley, Smarr & Wilson Paper I, printed as
     Ap. J. 277:276, is merged into `hawley-1984-b` (277:296 on Crossref;
     p. 276 lies inside another paper). HSWb (ApJS 55:211) is
     `hawley-1984`. Woodward & Colella (1984, J. Comput. Phys. 54:115)
     and Colella & Woodward (1984, 54:174) are distinct works.
     Bibliography: 2244 entries.
