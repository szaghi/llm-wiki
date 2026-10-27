---
type: Method
title: "Lattice Boltzmann methods for turbulent flow"
description: "Lattice Boltzmann methods advance particle populations on a discrete velocity lattice by local collision and streaming, recovering weakly compressible Navier–Stokes; this page gives the scheme, regularized and central-moment collisions, LES and RANS/hybrid eddy viscosities in the relaxation time, immersed boundaries, a Hall-MHD extension, and cost and accuracy."
status: established
aliases: [LBM, lattice Boltzmann, LB, lattice Boltzmann equation, LBE, HRR collision, central-moment collision, lattice Boltzmann MHD, FLAME]
tags: [lattice-boltzmann, les, dns, hybrid-rans-les, gpu, mhd, immersed-boundary]
timestamp: 2026-10-26T20:48:00Z
---

# Lattice Boltzmann methods for turbulent flow

A **lattice Boltzmann method (LBM)** evolves, on a Cartesian lattice, a set
of particle populations $f_q$ attached to a small set of discrete
velocities $\boldsymbol c_q$ (D3Q19 or D3Q27 in three dimensions); each time
step relaxes the populations locally towards an equilibrium (collision) and
shifts them to the neighbouring nodes (streaming). The density and momentum
are the moments $\rho=\sum_qf_q$, $\rho\boldsymbol u=\sum_q\boldsymbol c_qf_q$,
and a Chapman–Enskog expansion recovers the weakly compressible athermal
Navier–Stokes equations for Mach numbers below about 0.3
([Cai et al. 2022](/sources/cai-2022.md), §II.A, Eqs. 1–6). Cai et al. list
its advantages as an explicit collision–streaming algorithm with local
collision and streaming that is a memory shift. In the bundle it carries
wall-modelled LES of a car body, LES of turbulent fluid–structure
interaction, and $k$-$\omega$ SST RANS and SST-based hybrid RANS/LES
([Mozaffari et al. 2024](/sources/mozaffari-2024.md)) in the
[ProLB](/software/prolb.md) solver, and model-free
Hall-MHD turbulence on GPUs in the FLAME code of
[Foldes et al. (2023)](/sources/foldes-2023.md).

Page-local notation: $f_q$, $f^{\mathrm{eq}}_q$ the populations of lattice
direction $q$ and their equilibrium (not the registry's body force $f_i$,
which this page writes in words); $\boldsymbol c_q$, $w_q$ the lattice
velocities and weights; $c_s$ the lattice sound speed; $\tau_{\mathrm{LB}}$
the relaxation time and $\omega_{\mathrm{LB}}=\Delta t/\tau_{\mathrm{LB}}$ the
relaxation frequency (the sources' $\tau$ and $\omega$, renamed because they
are the registry's SGS stress and specific dissipation rate);
$\mathcal H^{(n)}_q$ the Hermite tensors of order $n$; $\Omega_q$ the
collision operator (not the rotation-rate tensor).

## Scheme

**BGK lattice Boltzmann equation.** As recalled by Cai et al. (2022, §II.A,
Eqs. 2, 5),
$$f_q(\boldsymbol x+\boldsymbol c_q\Delta t,t+\Delta t)-f_q(\boldsymbol x,t)=-\frac{\Delta t}{\tau_{\mathrm{LB}}}\big(f_q-f^{\mathrm{eq}}_q\big),\qquad \nu_{\mathrm{tot}}=c_s^2\Big(\tau_{\mathrm{LB}}-\frac{\Delta t}{2}\Big),$$
with $c_s=1/\sqrt3$ in lattice units on D3Q19 and $p=\rho c_s^2$, the
equilibrium a truncated Maxwell–Boltzmann expansion. Foldes et al. (2023,
§3.1.1, Eqs. 3.4–3.11) derive the same update from the discrete-velocity BGK
equation by the trapezoidal change of variables, with
$1/\omega_{\mathrm{LB}}=\nu/(c_s^2\Delta t)+1/2$, and expand the equilibrium
to **sixth order** in the velocity on D3Q27, following groups that report
gains in accuracy and stability (App. A). The D3Q27 weights are $8/27$
(centre), $2/27$ (faces), $1/54$ (edges) and $1/216$ (corners) (§3.1.1; see
Qualifications). Mozaffari et al. (2024, §2.1, Eqs. 1–4, 7–8) write the
same trapezoidal form with shifted populations
$\bar f_q=f_q-\tfrac12\Delta t\,\Omega_q$ on D3Q19 and a second-order
Hermite equilibrium
$f^{\mathrm{eq}}_q=w_q\rho\big(1+\boldsymbol u\cdot\boldsymbol c_q/c_s^2+\mathcal H^{(2)}_q:\boldsymbol u\boldsymbol u/(2c_s^4)\big)$,
$\mathcal H^{(2)}_q=\boldsymbol c_q\boldsymbol c_q-c_s^2\boldsymbol I$.

**Time step and Mach number.** The time step is tied to the lattice:
$\Delta t=(c_s/c_0)\Delta x_{\min}$ with $c_0$ the physical sound speed
(Cai et al. 2022, Eq. 28). To enlarge it, Cai et al. raise the Mach number
from 0.12 to 0.24 by lowering the physical sound speed, on the argument that
it barely affects nearly incompressible results (§III, citing Fares).
Foldes et al. (2023, §5), recalling Horstmann et al., state that in plain
MHD the LBM time step is smaller than that of an incompressible
pseudo-spectral solver by roughly the Mach number, so the method has
"little" turnaround advantage there; the advantage appears when another
constraint limits both (see the Hall-MHD section).

## Collision operators for turbulence

Plain BGK collision is unstable at high Reynolds number or large velocity
gradients (Cai et al. 2022, §II.A; Foldes et al. 2023, §1, §3.1.2). The
sources use two remedies.

- **Hybrid recursive regularized (HRR) collision** (Jacob et al., as
  recalled by Cai et al. 2022, §II.A, Eq. 7, and by
  [Cheylan et al. 2023](/sources/cheylan-2023.md), §2.1): the
  non-equilibrium part is rebuilt from its Hermite expansion and blended
  with a finite-difference strain rate,
  $$\Omega_q=-\frac{1}{\tau_{\mathrm{LB}}}\Big(\sigma_{\mathrm{HRR}}f^{(1)}_q-(1-\sigma_{\mathrm{HRR}})\frac{\rho\tau_{\mathrm{LB}}}{c_s^2}\mathcal H^{(2)}_q:\boldsymbol S^{\mathrm{FD}}\Big),$$
  ($f^{(1)}_q$ the non-equilibrium part, $\boldsymbol S^{\mathrm{FD}}$ the
  finite-difference strain-rate tensor, page-local), which adds a
  hyper-viscosity; the weight $\sigma_{\mathrm{HRR}}$ is "chosen as close to
  unity as possible" (no value printed). The equivalent macroscopic equations
  are the Favre-filtered LES equations plus a negligible high-order low-Mach
  term and a hyper-viscous term in the fourth velocity derivative (Eq. 9).
  Cheylan et al. describe the regularization as removing the trace of the
  non-equilibrium tensor for stability, on D3Q19. Mozaffari et al. (2024,
  §2.1, Eq. 5) print the same operator with $\sigma_{\mathrm{HRR}}=0.98$
  and state, citing Astoul et al., that because $\boldsymbol S^{\mathrm{FD}}$
  comes from second-order centred differences the blend introduces a
  bi-Laplacian hyper-viscosity that damps non-physical modes while limiting
  the dissipation of physical ones.
- **Central-moment multi-relaxation-time collision** (De Rosis et al., as
  used by Foldes et al. 2023, §3.1.2, Eqs. 3.14–3.17, App. A): the
  populations are transformed into central moments in the frame moving with
  the fluid ($\boldsymbol c_q-\boldsymbol u$), only the five deviatoric
  second-order moments relax with $\omega_{\mathrm{LB}}$ (the shear viscosity)
  and all others, including the trace, are set to equilibrium; BGK is the
  special case of a single rate. The authors state that central moments
  reduce dissipation artefacts in turbulence; in their own code comparison,
  however, this operator over-damps the kinetic-energy spectrum at high
  wavenumbers, which they attribute to the enhanced numerical dissipation of
  moment-based collisions (§4.4, citing Coreixas et al.).

## Eddy viscosity in the relaxation time

LES closures enter through the relaxation time: the total viscosity
$\nu+\nu_t$ sets $\tau_{\mathrm{LB}}$. Cai et al. (2022, §II.A) use the
[Vreman model](/methods/vreman-model.md) with $C_s\approx0.1$ and the
grid size as filter width; Cheylan et al. (2023, §2.7, Eqs. 37–38) use the
shear-improved [Smagorinsky model](/methods/smagorinsky-model.md) of
Lévêque et al., whose eddy viscosity is built from the strain-rate norm
minus that of its low-pass time-filtered value, with
$\tau_{\mathrm{LB}}=(\nu+\nu_t)/c_s^2+\Delta t/2$, the same relation as
above. Near walls Cai et al. add a constrained-LES hybrid viscosity and an
explicit equilibrium wall model on the immersed boundary (see
[immersed boundary methods](/methods/immersed-boundary-method.md) and
[wall-modelled LES](/methods/wall-modelled-les.md)).

**RANS and hybrid RANS/LES eddy viscosity.** Mozaffari et al. (2024,
§2.1, Eq. 6) couple a RANS or hybrid closure through the same relation,
$\tau_{\mathrm{LB}}=\Delta t/2+(\nu+\nu_t)/c_s^2$, so the turbulence model
enters the lattice only through the relaxation time. The
[$k$-$\omega$ SST](/methods/k-omega-sst-model.md) transport equations are
solved by finite differences on the lattice inside the collision step:
fourth-order centred derivatives, one-sided differences at walls,
second-order centred differences at grid-level transitions, and a hybrid
TVD centred/upwind advection with a modified van Albada limiter calibrated
on an inclined flat plate to avoid large $\omega$ fluxes near the wall
(§2.3). Near-wall $k$ and $\omega$ are imposed by viscous-sublayer and
log-layer wall functions switching at $y^+=11.06$ (Kalitzin et al., as
recalled; Eqs. 22–25). The same machinery hosts SST-based IDDES and
continuous eddy simulation, the hybrid modifying only the dissipation term
$\beta^*\omega k$ (Eqs. 26–34; see
[detached-eddy simulation](/methods/detached-eddy-simulation.md) and
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)). The authors state that
SST "has never been used in the standard LBM framework" (§1), having
cited Wang et al.'s use of it in a finite-volume lattice Boltzmann
formulation on unstructured grids. Forces are obtained by far-field
momentum integration over a control volume because the boundary-node
pressure and stress do not lie on the surface (§3.1, after Wilhelm et
al.); at $45^\circ$ incidence on a NACA 0012 this needed 234 flow-through
times (§3.2).

**Results** (Mozaffari et al. 2024, §3): on the two-dimensional NACA 23012
at $Re_c=1.88\times10^6$, $M=0.18$, SST and the Spalart–Allmaras model
already validated in ProLB give close lift and drag (e.g. $C_L$ 1.12 and
1.175 against 1.07 measured at $9.3^\circ$, Table 1) and both
under-predict $C_p$ near the leading edge; one more refinement level
reduces the $C_p$ error at $9.3^\circ$ by "almost 50%" (Fig. 8). On the
[NACA 0012](/benchmarks/naca-0012-airfoil.md) at $Re_c=3\times10^6$ the
hybrids equal RANS for attached flow and at $45^\circ$ correct its force
over-prediction ($C_L/C_D$: RANS 2.238/2.053, IDDES 1.231/1.038, continuous
eddy simulation 1.192/0.993, reference 1.097/1.180, Table 2). On the
[Ahmed body](/benchmarks/ahmed-body.md) the equilibrium wall model
suppresses slant separation (see
[immersed boundary methods](/methods/immersed-boundary-method.md)). The
authors conclude that SST-based hybrids are a cheaper alternative to
wall-modelled LES in a lattice Boltzmann code, but give no run time or
hardware.

## Walls on Cartesian lattices

Both ProLB sources impose walls by
[immersed boundaries](/methods/immersed-boundary-method.md) on octree or
uniform Cartesian lattices: Cai et al. (2022, §II.B) by reconstructing the
populations at boundary points as equilibrium plus a non-equilibrium part
from the finite-difference strain rate (bounce-back being noted as limited
to no-slip walls); Cheylan et al. (2023, §2.2) by direct forcing from
Lagrangian markers, the body force entering the collision through Guo's
forcing term and the velocity update. Cao et al. (2022, §3.3), comparing a
gas-kinetic scheme with lattice Boltzmann results for channel flow, state
that the lattice Boltzmann run needs equidistant grids with
$\Delta x^+\approx0.3$ everywhere to resolve the viscous layer. Cai et al.
(2022, §III) call resolving the near-wall layer of a car body on a
hierarchical lattice "not feasible", which motivates their wall model;
Mozaffari et al. (2024, §2.2) state likewise that, with the isotropic
mesh of ProLB, refining enough to resolve the boundary layer at high
Reynolds number is "too expensive".

**An explicit wall law from lattice Boltzmann RANS reused elsewhere.**
[Ghidoni et al. (2026)](/sources/ghidoni-2026.md), §1 and §3.3, adopt in a
high-order discontinuous Galerkin $k$-$\omega$ RANS solver the power-law wall
model of Wilhelm, Jacob & Sagaut (2018), which their reference list ([11])
titles "An explicit power-law-based wall model for lattice Boltzmann
method–Reynolds-averaged numerical simulations of the flow around
airfoils": $u^+=y^+$ for $y^+\le11.81$ and $u^+=8.3\,(y^+)^{1/7}$ above
(Eq. 13), inverted in closed form for $u_\tau$ (Eq. 14), chosen because
implicit laws (log law, Reichardt, Spalding) need Newton iterations at
every wall quadrature point. The DG implementation and its accuracy are on
[RANS wall functions](/methods/rans-wall-function.md); Ghidoni et al. run
no lattice Boltzmann computation.

## Lattice Boltzmann MHD with the Hall term

Foldes et al. (2023) solve the weakly compressible Hall-MHD equations with
two coupled lattices in the FLAME code (Fast Lattice-Boltzmann Algorithm for
MHD Experiments):

- the **fluid** on D3Q27 with the central-moment collision, the Lorentz
  force entering through a Maxwell-stress term added to the equilibrium, so
  that its second moment is $\rho\boldsymbol u\otimes\boldsymbol u+p\boldsymbol I+\tfrac12|\boldsymbol B|^2\boldsymbol I-\boldsymbol B\otimes\boldsymbol B$
  ($\boldsymbol B$ in Alfvén units; §3.1.1, Eqs. 3.12–3.13);
- the **induction equation** with Dellar's vector-valued BGK scheme on D3Q7
  (as recalled, §3.2, Eqs. 3.18–3.23), $\boldsymbol B$ the zeroth moment of
  vector populations, with a relaxation frequency set by $\eta_m$; the
  magnetic equilibrium is kept to second order only, and upgrading the
  magnetic lattice to D3Q15 or D3Q27 brought "no significant improvement",
  confirming Dellar (§4.3).

**The Hall term** (the authors' contribution, §3.2, Eqs. 3.24–3.28, App. B)
enters by replacing $\boldsymbol u$ with $\boldsymbol u-\alpha_H\boldsymbol J$
in the antisymmetric first moment of the magnetic equilibrium ($\alpha_H$
the Hall parameter, $\boldsymbol J=\nabla\times\boldsymbol B$, page-local).
The current is not differentiated: it is read locally from the
non-equilibrium first moment of the magnetic populations, which, since the
equilibrium now depends on $\boldsymbol J$, becomes a $3\times3$ linear
system per node with a closed-form, unique solution. The divergence of
$\boldsymbol B$ is the trace of that moment and was kept "to machine
round-off error" (Eq. 3.29). Whistler waves, whose phase speed grows with
the wavenumber, impose $\Delta t\propto\Delta x^2$; in lattice units the
condition reads $M\le(\sqrt3/\pi)/(\epsilon_HN_x^2)$ for $U_0$ equal to the
Alfvén speed ($\epsilon_H$ the dimensionless Hall number, page-local, and
$N_x$ the lattice points per reference length; Eqs. 3.40–3.44).

**Accuracy** (Foldes et al. 2023, §4.2–4.4): on an exact damped-wave
solution of dissipative Hall-MHD ($N_x=32$ to 128 lattice points per direction) all runs were stable,
density fluctuations stayed at $10^{-7}$–$10^{-6}$, and the dispersion,
dissipation and numerical-viscosity errors all decay as $N_x^{-2}$, the
numerical viscosity being "only a small percentage" of the physical one and
independent of viscosity and Mach number. On the decaying
[Orszag–Tang problem](/results/decaying-mhd-turbulence.md) at $512^3$
against the pseudo-spectral code [GHOST](/software/ghost.md), energies,
mean current and energy fluxes agree, the magnetic spectra "perfectly
match", and the kinetic spectrum is over-damped at high wavenumbers; at
$768^3$ it "gets very close" to the $512^3$ pseudo-spectral one, which the
authors call "qualitatively consistent" with the statement of Shen et al.
that the LBM needs about twice the resolution of a pseudo-spectral method.
They add that the LBM resolves up to the Nyquist wavenumber $N_x/2$, against
$N_x/3$ for the de-aliased pseudo-spectral code.

**Cost.** On three NVIDIA A100 GPUs (OpenCL with MPI, one-dimensional slab
decomposition, double precision) FLAME runs $512^3$ at about 20 iterations
per second, 2.7 billion lattice updates per second, including transfers and
on-the-fly diagnostics (§5). In Hall-MHD, where both methods are limited by
whistlers, the authors state that the GPU lattice code gives "significantly
smaller" turnaround times than pseudo-spectral codes; no side-by-side timing
is given.

## Limits stated by other sources

Cao et al. (2022, §1, §3.4) state that spectral and lattice Boltzmann
methods "fail to capture shocklets and suffer from numerical instability" in
compressible flow with shocks, which is the regime their
[gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) targets; the
lattice Boltzmann sources here are all weakly compressible.

## Qualifications

- **D3Q27 weights.** Foldes et al. print the edge weight as $1/54$ in
  §3.1.1 and $8/27$ in App. A; only $1/54$ makes the weights sum to one
  *(compiler check, not in the sources)*.
- **Current solve.** Eq. (3.27) of Foldes et al. lacks a factor
  $-\omega_{\mathrm{LB}}/C^2$ on its right-hand side that App. B carries,
  and one leading term of $J_y$ in Eq. (B1) has the wrong sign, by
  substitution of their own Eq. (3.26) *(compiler check, not in the
  sources)* ($C$ the magnetic lattice speed, page-local).
- Foldes et al. state (§7) that stability issues "are now mostly solved"
  by improved collision operators that "do not compromise the accuracy",
  while their own spectra show the central-moment collision over-damping
  high wavenumbers at $512^3$ (§4.4).
- The version of Foldes et al. read is the arXiv v2 author manuscript;
  Cai et al. a HAL deposit of the published article; Mozaffari et al. the
  HAL accepted manuscript hal-04921212v1.
- **Relaxation time in lattice units.** Mozaffari et al. write
  $\tau_{\mathrm{LB}}=\nu/c_s^2+0.5$ in §2.1 and
  $\Delta t/2+(\nu+\nu_t)/c_s^2$ in Eq. 6; the two agree for $\Delta t=1$
  and $\nu_t=0$ *(compiler check, not in the sources)*. Their SST
  production terms (Eqs. 16–17) are printed as
  $\tau_{ij}\,\partial u_j/\partial x_j$, which leaves a free index $i$ in a
  scalar equation *(compiler check, not in the sources)*. No SST
  coefficient value except $a_1=0.31$ is printed.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (1)–(15) (BGK lattice Boltzmann, HRR collision, Vreman model, equivalent LES equations); §II.B (boundary reconstruction); §III, Eq. (28) (time step, artificial Mach number, infeasible wall resolution).
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §2.1, Eqs. (1)–(4) (D3Q19, HRR, Guo forcing); §2.2 (direct forcing); §2.7, Eqs. (37)–(38) (shear-improved Smagorinsky in the relaxation time).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — arXiv v2: §1; §3.1, Eqs. (3.4)–(3.17), App. A (BGK, sixth-order equilibrium, Lorentz force, central-moment collision); §3.2–3.4, Eqs. (3.18)–(3.44), App. B (vector BGK induction, Hall term, current solve, whistler CFL); §4.2–4.4, Figs. 3–12 (accuracy, Orszag–Tang against GHOST); §5 (cost, turnaround); §7.
- [Cao et al. (2022)](/sources/cao-2022.md) — §1, §3.3–3.4 (lattice Boltzmann grids in channel flow; shocks).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — HAL accepted manuscript hal-04921212v1: §1; §2.1, Eqs. (1)–(8) (trapezoidal D3Q19, HRR with $\sigma=0.98$, eddy viscosity in the relaxation time); §2.2 (immersed boundary, wall model); §2.3, Eqs. (16)–(34) (SST by finite differences, wall functions, IDDES, CES); §3.1–3.3, Tables 1–3 (NACA 23012, NACA 0012, Ahmed body).
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1; §3.3, Eqs. (12)–(14); reference [11] (the explicit power-law wall model of Wilhelm et al., devised for lattice Boltzmann RANS, reused in a DG solver).
