---
type: Method
title: "Free-boundary and resistive-wall coupling"
description: "Methods that close a nonlinear MHD model with the vacuum field and the eddy currents of resistive conductors: a meshed vacuum and wall inside the computational domain (M3D-C1, NIMROD), or an un-meshed exterior handled by Green's functions and a natural boundary condition on the tangential field, with thin walls (JOREK-STARWALL) or 3D volumetric conductors through a virtual-casing equivalent current (JOREK-CARIDDI)."
status: established
aliases: [free-boundary MHD, resistive wall, JOREK-STARWALL, JOREK-CARIDDI, vacuum response, virtual casing]
tags: [free-boundary, wall, vde, numerics, code]
timestamp: 2026-10-16T12:00:00Z
---

# Free-boundary and resistive-wall coupling

A free-boundary MHD simulation lets the plasma boundary move and the
magnetic field outside the plasma domain respond to the plasma, to coils and
to the eddy currents induced in passive conductors. It is required for
[VDEs](/definitions/vertical-displacement-event.md), resistive-wall modes,
mode locking and RMP response, and it is what produces
[halo currents](/definitions/halo-current.md) and
[wall forces](/definitions/wall-forces.md) in a simulation
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9, §6.3). Two families
exist in the codes of this bundle.

## 1. Meshed vacuum and wall

The computational domain extends past the wall to an outer boundary, and
the vacuum and the conductor are discretized with the plasma
([Artola et al. (2021)](/sources/artola-2021.md), §2, Table 1).

- **[M3D-C1](/software/m3d-c1.md):** an axisymmetric thick wall; in
  conductor regions only $\mathbf A$ is advanced, with
  $\mathbf E=\eta_w\mathbf J$; in vacuum $\nabla\times\nabla\times\mathbf A=0$.
  Temperature and density boundary conditions are imposed at the plasma
  boundary, magnetic ones at the outermost boundary.
- **[NIMROD](/software/nimrod.md):** an axisymmetric thin resistive wall
  interfaced with a meshed external vacuum that uses the same magnetic
  representation as the plasma.

Because current can flow from plasma to wall through a resistive interface,
these codes carry toroidally asymmetric plasma currents
([reduced-MHD current asymmetry](/results/reduced-mhd-current-asymmetry.md)).
[Isernia et al. (2023)](/sources/isernia-2023.md) (§I) classify
[M3D](/software/m3d.md) and NIMROD as coupled to axisymmetric thin walls
only, and M3D-C1 as placing its conductors inside the computational domain.
M3D-C1 with a resistive wall gives linear (2,1) growth rates over wall
Lundquist numbers $\tau_w/\tau_A$ from ≈50 to $5\times10^4$ on a DIII-D
reconstruction that is stable with an ideal wall, and M3D with a thin
resistive wall follows the resulting
[resistive-wall tearing mode](/definitions/resistive-wall-tearing-mode.md)
nonlinearly to a thermal quench ([Strauss et al. (2022)](/sources/strauss-2022.md),
§II–III).

**Analytic thin-wall condition.** The cylindrical limit of a thin wall at
$r_w$, with a vacuum solution $\propto r^{-m}$ outside, is
$(1+\gamma\tau_w/m)\,\delta\psi=-(r_w/m)\,\partial_r\delta\psi$ with
$\tau_w=\mu_0r_wd_w/\eta_w$ ([Strauss et al. (2022)](/sources/strauss-2022.md),
§II, Eq. 1); it interpolates between the ideal-wall
($\delta\psi(r_w)=0$) and vacuum boundary conditions and is the basis of
the dispersion relations used to check these codes.

## 2. Un-meshed exterior: Green's functions and a natural boundary condition

The plasma domain ends at a boundary inside the wall; the vacuum is not
discretized. A separate code computes, once, linear response matrices that
express the tangential field on the boundary through the normal field and
the conductor currents; the MHD code imposes this relation as a natural
boundary condition.

**JOREK–STARWALL** ([STARWALL](/software/starwall.md), coupled to
[JOREK](/software/jorek.md); [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9):

- STARWALL represents thin walls by triangles and solves the vacuum by a
  Green's-function method; 3D walls with holes are allowed
  ([Artola et al. (2021)](/sources/artola-2021.md), §2).
- The boundary condition enters through the boundary integral of the
  current-definition equation: $\mathbf B\times\mathbf n$ on the boundary is
  a linear function of $\mathbf B\cdot\mathbf n$ and of the wall and coil
  currents, which obey RL circuit equations.
- The coupling is fully implicit; the implicit wall currents are eliminated
  analytically, so the matrix size is unchanged and only the boundary rows
  become denser. The response matrices are computed once per grid and wall,
  reused, and exchanged by MPI-IO; STARWALL itself is MPI-parallel with
  distributed response matrices.
- Free or fixed boundary can be chosen per toroidal harmonic; self-consistent
  PF coils, 3D (RMP) coils, passive coils and sensors are supported, and a
  free-boundary Grad–Shafranov solve uses the same coupling.
- The wall potential is not coupled implicitly; the plasma-domain boundary
  has $\Phi=0$, and halo source/sink currents are treated by the
  Zakharov–Atanasiu formalism as a post-processor for wall forces.

The thin-wall approximation uses the sheet resistance $\eta_w/d_w$
([Artola et al. (2021)](/sources/artola-2021.md), §2), and "is not always
robust" because the skin depth can be comparable to the wall thickness
([Isernia et al. (2023)](/sources/isernia-2023.md), §I).

**JOREK–CARIDDI** ([CARIDDI](/software/cariddi.md);
[Isernia et al. (2023)](/sources/isernia-2023.md), §II):

- CARIDDI solves the magneto-quasi-static eddy-current problem by an
  integral formulation over the conductors only: the current density is the
  curl of an electric vector potential expanded in edge elements, gauged by a
  tree–cotree decomposition, and a Galerkin projection gives a circuit
  equation with resistance and inductance matrices of the volumetric
  conductor (Eqs. 4–11).
- The coupling is indirect and rests on the virtual-casing principle: an
  equivalent surface current on the JOREK boundary reproduces the plasma's
  field outside. It is discretized as a thin CARIDDI shell (0.1 mm) and
  obtained by inverting the shell inductance matrix against the tangential
  vector potential supplied by JOREK (Eqs. 13–22).
- Eliminating the equivalent current gives (i) a circuit equation for the
  wall currents with a modified inductance, the conductor inductance in the
  presence of a superconducting shell that holds the boundary flux fixed, and
  (ii) a vacuum-response relation for the tangential poloidal field on the
  boundary, the boundary condition of the reduced-MHD $\psi$ equation
  (Eqs. 24–27).
- As for STARWALL, a generalized eigenproblem of the modified inductance
  against the resistance matrix is solved once; in its eigenbasis the
  circuit equation is diagonal, so changes of the implicit time step are
  cheap (Eq. 28).
- Limits: reduced MHD only (the full-MHD extension needs both tangential
  components of $\mathbf A$), no halo currents (a solenoidal equivalent
  current cannot represent current crossing the boundary, and
  plasma-facing electrodes are excluded), tokamak control surfaces only
  (§II, §VII).

## Verification

- **Vacuum response (JOREK–CARIDDI):** against the analytic field of a tilted
  toroidal wire, the RMS error is ≈0.1% for $n=0$, 0.25–0.4% for $n=1$ and
  0.45–2% for $n=2$, depending on the shell subdivision and toroidal
  quadrature; the source's summary claim of 0.2% holds only for $n=0$
  ([Isernia et al. (2023)](/sources/isernia-2023.md), §III, §VII, Figs. 2–3).
- **Axisymmetric VDE, AUG-like:** JOREK–CARIDDI and JOREK–STARWALL growth
  rates differ by less than 2% (39.87 against 39.59 s$^{-1}$); the
  mass-less CarMa0NL gives 44.38 s$^{-1}$, ≈11% higher, attributed to its
  fixed profiles and fixed $I_p$ ([Isernia et al. (2023)](/sources/isernia-2023.md),
  §IV, Figs. 4–5).
- **Tearing mode with a resistive wall:** over eight decades of wall
  resistivity, from ideal wall (≈630 s$^{-1}$) to no wall (≈960 s$^{-1}$),
  the $n=1$ growth rates of the two couplings agree within 1%
  ([Isernia et al. (2023)](/sources/isernia-2023.md), §V, Fig. 7).
- **JOREK–STARWALL:** resistive-wall-mode growth rate against analytic
  theory; VDE growth rates against CEDRES++ within 10–20%; ITER VDE against
  DINA within a few cm of the boundary; coil fields against Biot–Savart;
  ASDEX Upgrade PSL growth rates against CASTOR3D within ≈20%
  ([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8).
- **Three-code 3D VDE** with the two families against each other:
  [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md). Hoelzl et al.
  (2021, §4.8) conclude that "the very different numerical descriptions of
  the resistive wall structures used in the codes lead to comparable results"
  for this case.

## Physics enabled by 3D conductors

Ports in a volumetric wall couple toroidal harmonics through the wall. With
equally spaced holes the $n=1$ tearing growth rate rises monotonically with
the number of holes (509.5 to 573.0 rad/s for 0 to 8 holes). With an even
number of holes $n=1$ and $n=2$ do not couple through the wall, and $n=2$
is driven nonlinearly at twice the $n=1$ rate; with 1 or 3 holes they couple
directly ([Isernia et al. (2023)](/sources/isernia-2023.md), §VI, Table I).
The authors restrict the claim to their two-harmonic runs and conclude that
the number of toroidal harmonics may need to match the toroidal periodicity
of the conductors (§VI–VII). A single port advances the thermal quench of a
3D hot VDE (§VI, Fig. 10).

## Use in benchmarks and applications

The ITER runaway-electron VDE benchmark against DINA uses JOREK–STARWALL with
the vacuum-vessel shells (6 cm, $\eta_w=0.8\times10^{-6}$ Ω m), the PF and
central-solenoid coils and passive structures; a vessel-resistivity scan
shows that the nominal-resistivity case is not ideal-wall converged
([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV, Fig. 9b; see
[ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md)).
The ITER current-quench study of [Artola et al. (2022)](/sources/artola-2022.md)
(§2, Fig. 1) uses JOREK–STARWALL with a 3D inner vacuum-vessel layer of
75 000 linear triangles, an outer layer of toroidal filaments carrying
axisymmetric currents only (justified because the CQ is much shorter than
the inner-layer penetration time), the OTS and DIR passive structures as
filaments for vertical stability, $\eta_w=0.8\times10^{-6}$ Ω m (printed
without the metre) and $d_w=6$ cm, giving a vessel L/R time of ≈500 ms.
Blanket modules and ports are omitted. The runs are continued past the CQ
to ≈1.5 s to capture wall-current diffusion, which sets the maximum vertical
force ([wall forces](/definitions/wall-forces.md)).
JOREK has no free-boundary capability for stellarators yet, which blocks
benchmarks of external modes in stellarator geometry
([Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.2, §4.5).
The 2024 JOREK review lists, as ongoing, halo-current and full-MHD coupling
to CARIDDI, needed to predict horizontal forces linked to 1/1 kinks, and a
compression of the wall-coupling matrices
([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3, §5).

## Citations

- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9, §4.8, §6.3.
- [Isernia et al. (2023)](/sources/isernia-2023.md), §I–VII, Eqs. 4–28, Table I.
- [Artola et al. (2021)](/sources/artola-2021.md), §2, Table 1.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3, §5.
- [Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV.
- [Strauss et al. (2022)](/sources/strauss-2022.md), §II–III, Eq. 1.
- [Artola et al. (2022)](/sources/artola-2022.md), §2, Fig. 1.
- [Ramasamy et al. (2024)](/sources/ramasamy-2024.md), §3.2, §4.5.
