---
type: Method
title: "Constrained transport for the induction equation"
description: "Constrained transport stores face averages of the normal magnetic field and updates them with edge averages of the electric field by a discrete Stokes theorem, so the face-based discrete divergence is constant to round-off; the page gives the update, high-order face-to-cell interpolation, multidimensional and upwind edge fields, implicit variants and their limits."
status: established
aliases: [CT, staggered constrained transport, Evans–Hawley constrained transport, upwind constrained transport, UCT, UCT-GFORCE, Gardiner–Stone constrained transport, staggered mesh MHD, MPACT]
tags: [mhd, finite-volume, relativistic, numerical-flux]
timestamp: 2026-10-23T11:06:00Z
---

# Constrained transport for the induction equation

**Constrained transport** (CT) discretizes the induction equation
$\partial_tB+\nabla\times\mathcal E=0$, with the electric field
$\mathcal E=-v\times B$ of ideal MHD plus $\eta_{\mathrm r}\nabla\times B$
in resistive MHD ($\mathcal E$ and the resistivity $\eta_{\mathrm r}$
page-local; $\mathcal E$ is not the vortex strength of registry §10, and
the electric field is written $\mathcal E$ as on the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
page), on a staggered layout: each component of $B$ is stored as an average
over the cell faces normal to it, and $\mathcal E$ as averages along the
cell edges. Integrating the induction equation over a face and applying
Stokes' theorem gives an update of each face average by the circulation of
$\mathcal E$ around the face's edges. Every edge is shared by the faces of
a cell twice with opposite orientation, so the face-based discrete
divergence of every cell keeps its initial value to round-off. The method
goes back to Evans and Hawley, as recalled by
[Teissier et al. (2024)](/sources/teissier-2024.md) (§2.3) and
[Berta et al. (2024)](/sources/berta-2024.md) (§2), and is one of the
divergence controls of the
[divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
page; this page collects its construction. What CT leaves open is how the
edge electric field is computed from cell-centred finite-volume data, and
at which order.

## The staggered update

Let $\hat B_{1,i-1/2,j,k}$ denote the average of $B_1$ over the face
$x=x_{i-1/2}$ of cell $(i,j,k)$, $\hat B_2$, $\hat B_3$ likewise, and
$\bar{\mathcal E}_{3,i-1/2,j+1/2,k}$ the average of $\mathcal E_3$ along the
edge parallel to $x_3$ at $(x_{i-1/2},y_{j+1/2})$ (page-local; the sources
write $\bar b^x_x$ and $\bar E^z_z$ (Teissier et al.), $\hat B_{x_f}$ and
$\bar E_{x_e}$ (Berta et al.), where Berta et al.'s bar is an edge average,
not the registry's cell average). Teissier et al. (Eq. (15)) print
$$\frac{d}{dt}\hat B_{1,i-1/2,j,k}=-\frac{\bar{\mathcal E}_{3,i-1/2,j+1/2,k}-\bar{\mathcal E}_{3,i-1/2,j-1/2,k}}{\Delta y}+\frac{\bar{\mathcal E}_{2,i-1/2,j,k+1/2}-\bar{\mathcal E}_{2,i-1/2,j,k-1/2}}{\Delta z},$$
and the same for $\hat B_2$, $\hat B_3$ by cyclic permutation. The
discrete divergence
$$(\nabla_h\cdot\hat B)_{ijk}=\frac{\hat B_{1,i+1/2}-\hat B_{1,i-1/2}}{\Delta x}+\frac{\hat B_{2,j+1/2}-\hat B_{2,j-1/2}}{\Delta y}+\frac{\hat B_{3,k+1/2}-\hat B_{3,k-1/2}}{\Delta z}$$
(unchanged indices omitted) then satisfies $\frac{d}{dt}(\nabla_h\cdot\hat B)_{ijk}=0$
exactly, because the edge contributions cancel pairwise (Teissier et al.,
Eq. (17), citing Evans–Hawley and Balsara–Kim; Berta et al., Eqs. 14–15).
Both sources therefore keep $\nabla\cdot B$ "to machine precision" without
cleaning. The conserved variables $(\rho,\rho v,E)$ remain cell averages
updated by finite-volume fluxes; the magnetic contribution to their
fluxes needs a cell-centred field, and CT needs edge values of
$\mathcal E$ built from them.

[Dematté et al. (2024)](/sources/dematte-2024.md) (§3.3.1, Eqs.
(39)–(40)) use the same structure in 2D, $\hat B_1$ on $x$-faces and
$\hat B_2$ on $y$-faces updated by differences of the corner value
$\mathcal E_{3,i+1/2,j+1/2}$, inside an implicit iteration (below). The face
values are sampled at face centres initially and never overwritten by
cell values.

## Face-to-cell interpolation

Because the normal component $B_1$ is continuous across $x$-faces, the cell
value along $x$ is obtained by plain polynomial interpolation of the face
data, with no non-oscillatory reconstruction (Teissier et al., §3.1.1,
citing an earlier result; this property is stated, not proved there).
Teissier et al. interpolate the face averages $\hat B_{1,l-1/2}$,
$l=i-q+1,\dots,i+q$, by the polynomial of degree $2q-1$ in $x$ and average
it over the cell, for orders $2q=2,\dots,10$ (Eqs. (18)–(24)). With
$\tilde B^{(s)}=\hat B_{1,i+s}+\hat B_{1,i-s}$ for half-integer $s$
(page-local; the source's $\tilde b^{x(p)}_{x}$), the volume average is
$$\bar B_{1,i}=\tfrac12\tilde B^{(1/2)}+O(\Delta x^2)=\tfrac1{24}\big(13\tilde B^{(1/2)}-\tilde B^{(3/2)}\big)+O(\Delta x^4)=\tfrac1{1440}\big(802\tilde B^{(1/2)}-93\tilde B^{(3/2)}+11\tilde B^{(5/2)}\big)+O(\Delta x^6),$$
with eighth- and tenth-order formulas in Eqs. (23)–(24). Berta et al.
(Eq. 22) take the other target, the point value at the cell centre from
face-centre point values,
$B_{1,i}=\tfrac9{16}(B_{1,i+1/2}+B_{1,i-1/2})-\tfrac1{16}(B_{1,i+3/2}+B_{1,i-3/2})$,
after converting face averages to face point values by subtracting
$\tfrac1{24}$ of the transverse undivided Laplacian (Eq. 21). The two
fourth-order stencils differ because one returns an average over the cell
and the other a point value at its centre: for a quadratic $B_1$ the
first gives $B_1(x_i)+\tfrac{\Delta x^2}{24}B_1''$, the second $B_1(x_i)$
*(compiler check, not in the sources)*. The conversions between
averages and point values are on
[cell-average and point-value conversion](/operators/cell-average-point-value-conversion.md).

## The edge electric field

The edge field must be upwinded: the face Riemann problems deliver
$\mathcal E$ components at face centres (as transverse flux components of
the induction equation, Berta et al., Eq. 38), and an edge touches four
faces.

**Multidimensional Lax–Friedrichs** (Teissier et al., §3.2.3, Eqs.
(50)–(51), after Balsara). At the edge $(i-1/2,j-1/2,k)$,
$$\bar{\mathcal E}_3=\tfrac14\big(\bar{\mathcal E}^{++}_3+\bar{\mathcal E}^{+-}_3+\bar{\mathcal E}^{-+}_3+\bar{\mathcal E}^{--}_3\big)+\tfrac{S}{2}\big(\hat B^{+}_2-\hat B^{-}_2\big)-\tfrac{S}{2}\big(\hat B^{+}_1-\hat B^{-}_1\big),$$
with the four corner states of the edge, the two edge-reconstructed values
of each tangential face field, and
$S=\max\big(a^{(1)}_{i-1/2,j,k},a^{(1)}_{i-1/2,j-1,k},a^{(2)}_{i,j-1/2,k},a^{(2)}_{i-1,j-1/2,k}\big)$
the largest of the four adjacent face speeds of the one-dimensional
[Lax–Friedrichs flux](/methods/lax-friedrichs-flux.md), reused for
efficiency (page-local $S$; the authors write that one should ideally take
the maximum speed among the four reconstructed states). The corner fields are built in
steps: point values of $-v\times B$ from the face point values, conversion
to face averages, the resistive part added when $\eta_{\mathrm r}>0$, WENO
reconstruction from face to edge in each transverse direction, and the
average of the two values obtained by the $x$-then-$y$ and $y$-then-$x$
paths, "assuming discontinuities only at cell boundaries". The resistive
edge field uses a current computed from face averages, e.g.
$j_1=(\hat B_{3,j+1/2}-\hat B_{3,j-1/2})/\Delta y-(\hat B_{2,k+1/2}-\hat B_{2,k-1/2})/\Delta z$
(Eq. (53); $j_1$ page-local).

**Upwind constrained transport** (Berta et al., §4, Eqs. 38–40, App. B,
after Mignone and Del Zanna). With the states reconstructed from face
centres to the edge, labelled N, S (along $y$) and E, W (along $x$), the
point value of the edge field is
$$\mathcal E_3=-\big[(\mathsf a_1v_1B_2)^{\mathrm W}+(\mathsf a_1v_1B_2)^{\mathrm E}\big]+\big[(\mathsf a_2v_2B_1)^{\mathrm N}+(\mathsf a_2v_2B_1)^{\mathrm S}\big]+\big[(\mathsf d_1B_2)^{\mathrm E}-(\mathsf d_1B_2)^{\mathrm W}\big]-\big[(\mathsf d_2B_1)^{\mathrm N}-(\mathsf d_2B_1)^{\mathrm S}\big],$$
with flux weights $\mathsf a$ and diffusion coefficients $\mathsf d$ taken
from the face Riemann solver (page-local; the source's $a$, $d$, which
collide with the registry's wave speed and linear weights). For HLL and
HLLC the weights are $s^+/(s^+-s^-)$ and $-s^-/(s^+-s^-)$ and
$\mathsf d=-s^+s^-/(s^+-s^-)$ with the face wave speeds clipped at zero,
$s^+\ge0\ge s^-$ (Eq. B.4, written in registry speeds *(compiler check, not
in the sources: the source's $\alpha^{\mathrm R}=\max(0,\lambda^{\mathrm R})$,
$\alpha^{\mathrm L}=-\min(0,\lambda^{\mathrm L})$)*); HLLD and GFORCE have
their own coefficients (Eqs. B.3, B.5–B.6), and the relativistic
UCT-GFORCE is new. The edge point value becomes an edge average by
$\bar{\mathcal E}_3=\mathcal E_3+\tfrac1{24}\Delta_3\mathcal E_3$, the undivided
second difference along the edge (Eq. 40). Because the reconstruction acts
on point values, three layers of transverse ghost zones suffice instead of
four (§4). Details of the HLL-family coefficients are on
[HLL-family solvers](/methods/hll-riemann-solvers.md).

**Inside an implicit iteration** (Dematté et al., §3.3.1, Eqs.
(41)–(47), adapting Gardiner and Stone). In a semi-implicit all-Mach
scheme the corner field is the average of the four adjacent face values
plus two gradient corrections,
$\mathcal E_{3,i+1/2,j+1/2}=\bar{\mathcal E}^{\mathrm f}_3+\frac{\Delta x}8\big[(\partial_x\mathcal E_3)_{i+1/4,j+1/2}-(\partial_x\mathcal E_3)_{i+3/4,j+1/2}\big]+\frac{\Delta y}8\big[(\partial_y\mathcal E_3)_{i+1/2,j+1/4}-(\partial_y\mathcal E_3)_{i+1/2,j+3/4}\big]$
($\bar{\mathcal E}^{\mathrm f}_3$ the four-face average, page-local), the
gradients being differences between face values and the cell value
$v_2\tilde B_1-v_1\tilde B_2$ of the predicted field $\tilde B$ (page-local).
The face fields come from the flux duality and include the implicit
pressure-subsystem flux, $\mathcal E_{3,i+1/2,j}=-(F^{\mathrm a}_{[B_2]}+F^{\mathrm p}_{[B_2]})_{i+1/2,j}$
(Eq. (43); $F^{\mathrm a}$, $F^{\mathrm p}$ the advective and pressure parts
of the split flux, page-local), recomputed at every inner Picard iteration
of the [semi-implicit all-Mach scheme](/methods/semi-implicit-all-mach-scheme.md);
the resistive case adds $\eta_{\mathrm r}$ times differences of the four
cell-centred field values around the corner, divided by $2\Delta x$ and $2\Delta y$ (Eq. (61)).
The cell-centred field is then replaced by the mean of its two face values
in each direction, which satisfies the corner-centred divergence
$\big[(B_1)_{i+1,j}+(B_1)_{i+1,j+1}-(B_1)_{i,j}-(B_1)_{i,j+1}\big]/(2\Delta x)+\big[(B_2)_{i,j+1}+(B_2)_{i+1,j+1}-(B_2)_{i,j}-(B_2)_{i+1,j}\big]/(2\Delta y)=0$
(Eqs. (46)–(47)).

**Unstaggered vector-potential variant** (Dematté et al., §3.3.2, Eqs.
(48)–(51), adapting Rossmanith's MPACT). Only the out-of-plane vector
potential $A_3$ (page-local) is kept, at cell centres, advected by
$\partial_tA_3+v_1\partial_xA_3+v_2\partial_yA_3=0$ with Rossmanith's
limited upwind wave-propagation method, and $B_1$, $B_2$ are recomputed
from it by central differences, so that the central (cell-centred)
divergence vanishes (Eq. (50)); motivated by adaptive meshes and
multi-material coupling, which a dual representation complicates.

## Order and accuracy

CT itself is exact in the divergence at any order; the order is set by the
face-to-cell interpolation, the edge field and the conversions between
averages and point values. Teissier et al. reach tenth order with
**one** reconstructed value per face (orders 2–10, schemes S2–S10: WENO of
order 3–11, face-to-cell interpolation and point-value conversions of the
scheme's order, and an SSP integrator of matching order;
[SSP Runge–Kutta](/methods/ssp-runge-kutta.md)). On a 3D
[magnetized vortex](/benchmarks/magnetized-vortex.md) advected for one
period ($t=10$, background pressure $p_0=360$) the $L_2$ orders at $192^3$
are 4.46, 6.12, 7.87 and 9.74 for S4–S10 (Table 2). Dropping the
point-value passage of S8 lowers the order to 2.11, 1.97, 1.99, and a
second-order time integrator to 2.12, while the energy loss of the
point-value-free scheme stays close to that of S8, which the authors read
as a sign of dispersive rather than dissipative error (§4.1, Table 2).
Berta et al. observe $L_1$ orders between 3.91 and 4.84 on MHD and
relativistic vortices (Table 1) and 4.00 on circularly polarized Alfvén
waves (Table 2), with the [field-loop advection](/benchmarks/field-loop-advection.md)
smeared less at fourth than at second order (§5.4). Dematté et al. measure
second order in space on a smooth MHD vortex at fixed $\Delta t$ (Table 2),
and $\lVert\nabla\cdot B\rVert_{L^2}$ near machine precision with both
variants through the MHD rotor (§4.1.4, Fig. 8).

**Divergence-free forcing.** For driven turbulence Teissier et al. make the
electromotive forcing a staggered face average in Fourier space, multiplying
each mode by a phase shift and by the cell average of $e^{\mathrm i k x}$
over the face in each transverse direction, so that the forcing adds no
divergence (§3.5, Eq. (55); initial fields likewise, Eqs. (76)–(77)).

## Qualifications

- **Version and authorship.** The Teissier et al. file read is the arXiv
  v2 preprint, with two of the three authors of the version of record
  (Teissier and Müller) and an earlier title; claims are those of that
  version.
- **Printed slips in Teissier et al.** Every transverse averaging factor of
  Eqs. (55), (76) and (77) is printed
  $(e^{\mathrm ik\Delta/2}-e^{\mathrm ik\Delta/2})$, which vanishes
  identically; the factor that makes a face or cell average of
  $e^{\mathrm ikx}$ is $(e^{\mathrm ik\Delta/2}-e^{-\mathrm ik\Delta/2})/(\mathrm ik\Delta)=\sin(k\Delta/2)/(k\Delta/2)$
  *(compiler check, not in the sources)*.
- **Printed signs in Dematté et al.** With their $\mathcal E=-v\times B$
  and cell value $v_2B_1-v_1B_2$ (Eq. (45)), Faraday's law gives
  $\partial_tB_1=-\partial_y\mathcal E_3$ and
  $\partial_tB_2=+\partial_x\mathcal E_3$; Eq. (39) prints both signs
  reversed, which leaves the divergence preservation intact. Eqs. (49) and
  (51) print $B_2=+(A_{3,i+1,j}-A_{3,i-1,j})/(2\Delta x)$; from
  $B=\nabla\times(A_3e_3)$, $B_2=-\partial_xA_3$, and only with the minus sign
  does the central divergence of Eq. (50) vanish identically (with the
  printed sign it equals $2\,\delta_x\delta_yA_3/(4\Delta x\Delta y)$, $\delta$
  central differences) *(compiler check, not in the sources)*. The text
  also writes "$A=\nabla\times B$" for $B=\nabla\times A$.
- **Scope of the high-order evidence.** Teissier et al. treat only smooth
  subsonic flows and state that shocks need flattening, possibly with
  positivity preservation, which they do not implement (§1, §5); their
  efficiency argument (about a factor 10 for S6 over S4 at equal energy
  loss) rests on the smooth vortex. Berta et al. reach their shock tests
  with an order-reduction fallback
  ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).
- **Speeds and ghost data.** Teissier et al.'s edge speed $S$ reuses the
  one-dimensional face speeds instead of the maximum over the four edge
  states, a choice the authors state is made for efficiency (§3.2.3); their
  Lax–Friedrichs speed estimate is valid only for ideal MHD and is replaced
  by a diffusion speed in their diffusion-only tests (§3.2.1, §4.2).
- Other constrained-transport variants of the bundle (Touma's unstaggered
  CTM in a central scheme, the IDEFIX GPU code, vector potentials in
  finite-difference WENO, divergence-preserving prolongation on adaptive
  meshes) are on the
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
  page.

# Citations

- [Teissier et al. (2024)](/sources/teissier-2024.md) — arXiv v2: §2.3, Eqs. (12)–(17); §3.1.1, Eqs. (18)–(24); §3.2.1, Eqs. (31)–(33); §3.2.3, Eqs. (50)–(51); §3.4.2, Eq. (53); §3.5, Eq. (55); §4.1, Table 2; §4.2, Eqs. (76)–(77); §5.
- [Berta et al. (2024)](/sources/berta-2024.md) — arXiv v4: §2, Eqs. (11)–(15); §3.1, Eqs. (21)–(22); §4, Eqs. (38)–(40); App. B, Eqs. (B.1)–(B.6); §5.2–5.4, Tables 1–2.
- [Dematté et al. (2024)](/sources/dematte-2024.md) — §3.3.1, Eqs. (39)–(47); §3.3.2, Eqs. (48)–(51); §3.4, Eq. (61); §4.1.2, Table 2; §4.1.4, Fig. 8.
