---
type: Method
title: "Lattice Boltzmann methods for turbulent flow"
description: "Lattice Boltzmann methods advance particle populations on a discrete velocity lattice by local collision and streaming, recovering weakly compressible Navier–Stokes; this page gives the scheme, regularized, central-moment and MRT collisions, eddy viscosities in the relaxation time, temporal LES closed in the collision, immersed boundaries, a Hall-MHD extension, and accuracy."
status: established
aliases: [LBM, lattice Boltzmann, LB, lattice Boltzmann equation, LBE, HRR collision, central-moment collision, MRT collision, lattice Boltzmann MHD, FLAME, ZDES-LBM, temporal LES with lattice Boltzmann, TLES-LBM, OpenLB]
tags: [lattice-boltzmann, les, dns, hybrid-rans-les, gpu, mhd, immersed-boundary]
timestamp: 2026-10-27T15:53:00Z
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
[ProLB](/software/prolb.md) solver, Spalart–Allmaras RANS and zonal
detached-eddy simulation in a development branch of the same solver
([Husson et al. 2024](/sources/husson-2024.md)), and model-free
Hall-MHD turbulence on GPUs in the FLAME code of
[Foldes et al. (2023)](/sources/foldes-2023.md), and temporal LES of the
Taylor–Green vortex with the residual stress advanced inside the
collision in OpenLB ([Simonis et al. 2022](/sources/simonis-2022.md)).

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

**BGK lattice Boltzmann equation.** Cai et al. (2022, §II.A, Eqs. 2, 5)
print
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
Foldes et al. (2023, §5), citing Horstmann et al., state that in plain
MHD the LBM time step is smaller than that of an incompressible
pseudo-spectral solver by roughly the Mach number, so the method has
"little" turnaround advantage there; the advantage appears when another
constraint limits both (see the Hall-MHD section).

## Collision operators for turbulence

Plain BGK collision is unstable at high Reynolds number or large velocity
gradients (Cai et al. 2022, §II.A; Foldes et al. 2023, §1, §3.1.2). The
sources use two remedies.

- **Hybrid recursive regularized (HRR) collision** (Jacob et al., cited
  by Cai et al. 2022, §II.A, Eq. 7, and by
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
  the dissipation of physical ones. Husson et al. (2024, §2.1, Eqs. 7–14)
  also use $\sigma_{\mathrm{HRR}}=0.98$, citing an earlier ProLB study,
  and print the full D3Q19 form: the off-equilibrium second-order Hermite
  coefficient blends the population moments with the finite-difference
  strain rate, the third-order one is rebuilt recursively from it and the
  velocity (the "recursive regularized" part), and only the three pairs of
  third-order Hermite combinations that D3Q19 supports are kept, in the
  non-equilibrium part and in an "improved" equilibrium that adds the
  same third-order terms with $\rho u_\alpha u_\beta u_\gamma$.
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
log-layer wall functions switching at $y^+=11.06$ (Mozaffari et al. cite
Kalitzin et al.; Eqs. 22–25). The same machinery hosts SST-based IDDES and
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

**Spalart–Allmaras RANS and zonal detached-eddy simulation.**
Husson et al. (2024, §2.1–2.2, Eqs. 15, 18–35) couple the
[Spalart–Allmaras model](/methods/spalart-allmaras-model.md), transported
in its incompressible form for $\chi=\tilde\nu/\nu$, and its hybrid
extension ZDES mode 2 (2020) ([detached-eddy simulation](/methods/detached-eddy-simulation.md))
through the relaxation time, written with the physical sound speed $c_0$
as $\tau_{\mathrm{LB}}=(\nu+\nu_t)/c_0^2+\Delta t/2$ (Eq. 15, the
Chapman–Enskog result for the weakly compressible equations). The $\chi$
equation is solved apart from the populations by finite differences:
second-order centred differences on its right-hand side and a hybrid
upwind–centred scheme for advection (§2.2). The authors state that the
gradient-based shielding sensors of ZDES were designed and calibrated for
Navier–Stokes finite-volume solvers and that there is "a priori no
evidence" that they keep their efficiency here, for three reasons: the
eddy viscosity acts only through the relaxation time; a slower
destruction of eddy viscosity could delay the formation of instabilities
in shear layers; and the factor-two level transitions of the isotropic
octree lattice cause weak numerical instabilities that could trigger the
wake-layer sensor in shear layers or the inhibition sensor inside
boundary layers (§2.2).

The isotropy of the lattice is the core of the problem they address. At
high Reynolds number it makes the streamwise and spanwise spacing very
small relative to the boundary-layer thickness ($\Delta x\approx0.01\delta$
at mid-plate on their flat plate), a regime in which, they state, the
shielding of DES-type models fails "almost systematically", with
modelled-stress depletion and possibly grid-induced separation, which makes
those models "prohibitive" for attached layers in lattice Boltzmann
solvers (§1, §4.1.2; definitions on
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)). Their results
(§4):

- **Flat plate** ($Re_L=5\times10^6$, $M=0.2$, $\Delta y^+\approx30$):
  ZDES reproduces the lattice Boltzmann RANS skin friction, velocity and
  eddy-viscosity profiles, also with $C_{DES}=0$ and on a plate inclined
  to the lattice; DDES (2006) on the same grid suffers severe
  modelled-stress depletion and an "unexploitable" oscillating $C_f$
  (Fig. 4–5).
- **Backward-facing step** (A3C, $Re_h=40{,}000$;
  [backward-facing step](/benchmarks/backward-facing-step.md)): with
  $44.7\times10^6$ lattice nodes and a wall law, against
  $3.9\times10^6$ points for the wall-resolved body-fitted Navier–Stokes
  ZDES of Deck & Renard (2020), which Husson et al. cite, the shielding field, the
  eddy-viscosity destruction, the vorticity-thickness growth and the mean
  profiles agree, and the authors conclude that the lattice adds "no
  further delay in the formation of instabilities" (Figs. 7–11, Table 1).
  Isotropy makes the lattice locally much finer than the body-fitted grid
  ($\Delta z$ about ten times finer near the step; 61,000 against 5000
  points in the plane $x=0$, §4.2).
- **LEISA2 three-element high-lift airfoil** ($Re_c\approx1.23\times10^6$,
  $77\times10^6$ nodes against $2.6\times10^9$ for the wall-resolved LES of
  Terracol & Manoha, which Husson et al. cite): attached layers stay in RANS, there is
  no grid-induced separation and the mean $C_p$ agrees with experiment; a
  small delay of the slat shear-layer instability, which the authors
  attribute to grid and wall model because wall-modelled LES in the same
  solver (Soni et al., which the authors cite) shows the same (§4.3).

They present the combination as a "fair alternative" to Navier–Stokes
hybrids and to wall-modelled LES in lattice Boltzmann solvers, especially
for aeroacoustics (§5).

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

**The relaxation time as the place of the turbulence model.** In the
appendix of a review of hybrid RANS/LES,
[Heinz (2020)](/sources/heinz-2020.md), App. A, Eqs. (56)–(57), writes the
continuous BGK equation for the velocity p.d.f. $f(\boldsymbol w,\boldsymbol x,t)$
($\boldsymbol w$ the sample-space velocity, $g$ the equilibrium, $\tau_{\mathrm{BGK}}$ the
relaxation time, all page-local),
$$\partial_tf+\partial_k(w_kf)=-\frac{f-g}{\tau_{\mathrm{BGK}}},$$
with $g$ an isotropic Gaussian around the mean velocity of variance
$2k_{\mathrm{BGK}}/3$. Heinz states that the fluctuations it carries are
molecular and turbulent together. Consistency with the momentum and
stress equations gives
$$\tau_{\mathrm{BGK}}=\frac{3(\nu+\nu_t)}{2(e+k)},\qquad k_{\mathrm{BGK}}=e+k,\qquad \nu=\tfrac23\tau_{\mathrm{BGK}}e,\qquad \nu_t=\tfrac23\tau_{\mathrm{BGK}}k,$$
with $e$ and $k$ the molecular and the modelled turbulent kinetic energy
(page-local $e$). Depending on how $\tau_{\mathrm{BGK}}$ is supplied as a
function of $\nu_t$, lattice Boltzmann methods run as RANS, LES or hybrid
RANS/LES. They are "not seen as modeling alternative" to these, but as a
route to "more accurate and more efficient numerical solutions" of the
same turbulence equations (App. A). With $k_{\mathrm{BGK}}=e+k$ the first
relation reads $\nu+\nu_t=\tfrac23k_{\mathrm{BGK}}\tau_{\mathrm{BGK}}$,
which has the form of the lattice relation
$\nu_{\mathrm{tot}}=c_s^2(\tau_{\mathrm{LB}}-\Delta t/2)$ of the Scheme
section with $c_s^2$ replaced by the per-component variance
$2k_{\mathrm{BGK}}/3$ and without the discrete shift $\Delta t/2$
*(compiler check, not in the sources)*. Heinz (2020, §2.3, Eq. 12) also rewrites the $k$,
$\varepsilon$ and $\omega$ equations as BGK-type relaxations towards
equilibrium values plus sink terms, citing Asinari et al. The finite-volume
[high-order gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md)
couples subgrid models the same way, through an enlarged collision time
$\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$ (page-local: the
gas-kinetic collision time and its turbulent increment, $p$ the pressure;
[Zhao et al. 2021](/sources/zhao-2021-c.md),
§III, Eqs. 12–13, citing Chen et al.).

## Temporal LES closed inside the collision

[Simonis et al. (2022)](/sources/simonis-2022.md) combine, to their
knowledge for the first time, temporal large-eddy simulation (TLES) with
the lattice Boltzmann method (§1). The incompressible equations are
filtered in **time** with a causal exponential kernel of width $\Theta$
(page-local; the overbar in this section is that time filter, not a
spatial one). Its differential form
$\partial_t\bar\phi=(\phi-\bar\phi)/\Theta$ inverts exactly,
$\phi=\bar\phi+\Theta\,\partial_t\bar\phi$ ("direct deconvolution"), and
the temporal residual stress $T^{\mathrm t}_{ij}=\overline{u_iu_j}-\bar u_i\bar u_j$
(page-local, positive trace like the registry's $\tau_{ij}$) obeys the
closed relaxation equation
$$\frac{\partial T^{\mathrm t}_{ij}}{\partial t}=-\frac{T^{\mathrm t}_{ij}}{\Theta}+\Theta\,\frac{\partial\bar u_i}{\partial t}\frac{\partial\bar u_j}{\partial t}$$
(the temporal direct deconvolution model of Oberle, Pruett & Jenny, which
Simonis et al. cite; §2.1, Eqs. 4–6), with no constant besides $\Theta$. In the
filtered BGK equation of Malaspinas & Sagaut, which Simonis et al. cite, the residual of
the filtered equilibrium has, in its Hermite expansion to second order,
only a second-order coefficient equal to the residual stress plus a
subgrid temperature times $\delta_{ij}$; for an isothermal model the
latter is zero (§2.2, Eqs. 7–11). Simonis et al. read that stress as
$T^{\mathrm t}_{ij}$ instead of closing it with an eddy viscosity, and add
the forcing $w_q\mathcal H^{(2)}_q:T^{\mathrm t}/(2c_s^4)$, unrelaxed, to a
D3Q19 multiple-relaxation-time collision in the orthogonal moment basis of
d'Humières with Mach-dependent kinetic relaxation rates fitted to
optimized values (§2.3–2.4, Eqs. 12–17). $T^{\mathrm t}_{ij}$ is advanced
by forward Euler and the fields are deconvolved by backward differences
(Eqs. 18–19; a second-order Adams–Bashforth variant in App. A.2), with
$\Theta=\tilde\Theta\,\Delta t$ (Eq. 28). Both updates are local in space:
a higher order costs stored time levels, not communication, which the
authors contrast with the spatial approximate deconvolution of
Malaspinas & Sagaut (§2.4, §4). The scheme is implemented in OpenLB.

On the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
(§3, with $N_x$ lattice points per direction):

- *Calibration* ($Re=800$, $N_x=64$): $\tilde\Theta=5$ has marginal effect,
  10 and 20 bring the peak of the total dissipation rate towards the DNS,
  40 drives the model dissipation into "complete overdrive"; above 10 the
  oscillations are "clearly unphysical", so $\tilde\Theta=10$ is chosen.
  Lattice Mach numbers from 0.05 to 0.2 were tried: at 0.05 the model
  dissipation turns clearly negative, compensating an increased resolved
  dissipation late in the run, and 0.1 is the lowest value without an
  overly increased dissipation tail (§3.2, Figs. 2–5). The authors trace the
  early dissipation-rate deviation to initialization errors of the LBM
  that the model amplifies (§3.2.3).
- *Against spectral elements* ($Re=3000$, $N_x=64$ and about 128):
  unmodelled under-resolved LBM underpredicts the dissipation peak more
  than the [spectral-element method](/methods/spectral-element-method.md)
  of [Nek5000](/software/nek5000.md) and shows an early onset of the
  dissipation range where the spectral elements pile up energy; with the
  closure, the LBM recovers a distinct dissipation peak near $t\approx9$
  already at $N_x=64$, while the spectral-element TLES shows a "distorted
  crown" there (§3.3, Figs. 7–8).
- *Implicit LES conjecture.* At $N_x=64$ the dissipation not accounted for
  by the enstrophy of the unmodelled MRT run is about half the total; the
  authors conjecture that MRT LBM without a model "already acts as" an
  [implicit LES](/definitions/implicit-les.md) (§3.3.2, Fig. 7a).
- *Error under acoustic scaling* ($Ma=0.1$, $N_x=24$ to 192): the subgrid
  activity (the ratio of model to total dissipation, after Geurts &
  Fröhlich) decreases with refinement and has about the same magnitude
  with and without the closure; the energy-spectrum error falls at second
  order up to $N_x=64$ and then saturates at a plateau that the authors
  attribute mainly to the compressibility defect of the LBM (§3.4,
  Fig. 9). The text states that the work "proves" convergence towards the
  incompressible solution "up to a known combination of errors"; the
  support is this numerical study.
- *Order of convergence* (App. B, Table 3; $Re=800$, $N_x=64$, 128, 256):
  the closure raises the experimental order of the dissipation-rate error
  for single- and multiple-relaxation-time collisions under acoustic and
  diffusive scaling, e.g. 1.70 (unmodelled), 1.78 (first-order closure) and
  2.11 (second-order closure) for single relaxation under acoustic scaling,
  and 1.52, 1.63, 1.81 for MRT; MRT lowers the order but is stable at
  $N_x=32$ and at all tested Mach numbers. The authors call such regressed
  orders "fuzzy".

The method is summarized on the [LES](/definitions/large-eddy-simulation.md)
page as a temporal filter.

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
Reynolds number is "too expensive". Husson et al. (2024, §3) use a
sharp-interface direct-forcing method with forcing nodes on the fluid
side, where all populations are overwritten by equilibrium plus
regularized non-equilibrium parts, and a Spalart–Allmaras analytical wall
law, linearized below the interpolation-point distance $2.5\Delta y$,
inverted at the interpolation point (details on
[immersed boundary methods](/methods/immersed-boundary-method.md) and
[RANS wall functions](/methods/rans-wall-function.md)).

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

[Bose & Park (2018)](/sources/bose-2018.md), §3, cite the lattice
Boltzmann wall model for LES of Malaspinas & Sagaut (2014); the review
lists it among implementation
studies it does not discuss.

## Lattice Boltzmann MHD with the Hall term

Foldes et al. (2023) solve the weakly compressible Hall-MHD equations with
two coupled lattices in the FLAME code (Fast Lattice-Boltzmann Algorithm for
MHD Experiments):

- the **fluid** on D3Q27 with the central-moment collision, the Lorentz
  force entering through a Maxwell-stress term added to the equilibrium, so
  that its second moment is $\rho\boldsymbol u\otimes\boldsymbol u+p\boldsymbol I+\tfrac12|\boldsymbol B|^2\boldsymbol I-\boldsymbol B\otimes\boldsymbol B$
  ($\boldsymbol B$ in Alfvén units; §3.1.1, Eqs. 3.12–3.13);
- the **induction equation** with Dellar's vector-valued BGK scheme on D3Q7
  (which Foldes et al. cite, §3.2, Eqs. 3.18–3.23), $\boldsymbol B$ the zeroth moment of
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

Simonis et al. (2022, §3.4, App. B) state that under diffusive scaling
($\Delta t\propto\Delta x^2$) the method is consistent with the
incompressible equations but first order in time, while under acoustic
scaling (fixed Mach number) it suggests second order in space and time
until a constant compressibility-error plateau; they argue that an
incompressible closure is reasonable for the weakly compressible scheme
at lattice Mach numbers up to 0.1.

Cao et al. (2022, §1, §3.4) state that spectral and lattice Boltzmann
methods "fail to capture shocklets and suffer from numerical instability" in
compressible flow with shocks, which is the regime their
[gas-kinetic scheme](/methods/high-order-gas-kinetic-scheme.md) targets; the
lattice Boltzmann sources here are all weakly compressible.

[Maltsev et al. (2022)](/sources/maltsev-2022.md), §III E, Eqs. (80)–(92),
review the method for compressible multiphase flow and state its limits
there: the classical scheme is restricted to low Mach number by the
expansion of the Maxwellian, and the fixed velocity stencil restricts the
attainable ratio of specific heats and Prandtl number. Compressible
extensions need more discrete velocities, counterterms, double
distributions or multiple relaxation times. Multiphase variants come in
colour-gradient, Shan–Chen and free-energy families. Hybrid lattice
Boltzmann/finite-volume schemes either discretize the discrete-velocity
Boltzmann equation by finite volumes, which frees the velocities from the
lattice, or store finite-volume data and take the intercell fluxes from a
lattice Boltzmann step. In their conclusions (§V) the authors find
hybrid finite-volume/lattice Boltzmann treatments of diffuse-interface
multiphase models still at an early stage.

## Qualifications

- **D3Q27 weights.** Foldes et al. print the edge weight as $1/54$ in
  §3.1.1 and $8/27$ in App. A; only $1/54$ makes the weights sum to one
  *(compiler check, not in the sources)*.
- **Current solve.** Eq. (3.27) of Foldes et al. lacks a factor
  $-\omega_B/C^2$ on its right-hand side that App. B carries,
  and one leading term of $J_y$ in Eq. (B1) has the wrong sign, by
  substitution of their own Eq. (3.26) *(compiler check, not in the
  sources)* ($\omega_B$ the magnetic relaxation frequency and $C$ the
  magnetic lattice speed, page-local).
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
- **Index range (Husson et al.).** Their Eq. (10) sums the D3Q19
  populations over $i=1,\dots,19$, while Eqs. (2)–(3) number them
  $0,\dots,18$; Eq. (13) carries the lattice index on the velocity,
  $\rho u_{i,\alpha}$, where Eq. (4) has $\rho\boldsymbol u$. The
  wall-resolved LES of the LEISA2 airfoil is printed with
  "$2.6\cdot10^9$ nodes" (p. 15) and "$2700\cdot10^6$ nodes" (p. 18). The
  version read is the version of record.

- **Relaxation factor (Simonis et al.).** Simonis et al. print the
  collision with the factor $\Delta t/(\tau_{\mathrm{LB}}+\Delta t/2)$
  (Eq. 14) together with $\nu=c_s^2(\tau_{\mathrm{LB}}-\Delta t/2)$
  (Eq. 15); the BGK form printed by Cai et al. in the Scheme section pairs
  the same viscosity with the factor $\Delta t/\tau_{\mathrm{LB}}$. Their
  Table 1 prints $\Delta t=0.00288$ for $N_x=128$ at Mach 0.1, while
  Table 2 prints 0.00285 for the same configuration and the other
  $N_x=128$ rows of Table 1 equal the lattice velocity times $\Delta x$
  *(compiler check, not in the sources)*. §3.3 and the Fig. 6 caption write
  the calibrated filter width as "$\Theta=10$" for the dimensionless
  $\tilde\Theta=10$ of Eq. (28). The version read is the version of record.

# Citations

- [Cai et al. (2022)](/sources/cai-2022.md) — §II.A, Eqs. (1)–(15) (BGK lattice Boltzmann, HRR collision, Vreman model, equivalent LES equations); §II.B (boundary reconstruction); §III, Eq. (28) (time step, artificial Mach number, infeasible wall resolution).
- [Cheylan et al. (2023)](/sources/cheylan-2023.md) — §2.1, Eqs. (1)–(4) (D3Q19, HRR, Guo forcing); §2.2 (direct forcing); §2.7, Eqs. (37)–(38) (shear-improved Smagorinsky in the relaxation time).
- [Foldes et al. (2023)](/sources/foldes-2023.md) — arXiv v2: §1; §3.1, Eqs. (3.4)–(3.17), App. A (BGK, sixth-order equilibrium, Lorentz force, central-moment collision); §3.2–3.4, Eqs. (3.18)–(3.44), App. B (vector BGK induction, Hall term, current solve, whistler CFL); §4.2–4.4, Figs. 3–12 (accuracy, Orszag–Tang against GHOST); §5 (cost, turnaround); §7.
- [Cao et al. (2022)](/sources/cao-2022.md) — §1, §3.3–3.4 (lattice Boltzmann grids in channel flow; shocks).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — HAL accepted manuscript hal-04921212v1: §1; §2.1, Eqs. (1)–(8) (trapezoidal D3Q19, HRR with $\sigma=0.98$, eddy viscosity in the relaxation time); §2.2 (immersed boundary, wall model); §2.3, Eqs. (16)–(34) (SST by finite differences, wall functions, IDDES, CES); §3.1–3.3, Tables 1–3 (NACA 23012, NACA 0012, Ahmed body).
- [Husson et al. (2024)](/sources/husson-2024.md) — §1 (isotropic lattices and DES-type shielding); §2.1, Eqs. (1)–(17) (D3Q19 HRR with $\sigma=0.98$, improved equilibrium, relaxation time); §2.2, Eqs. (18)–(35) (SA and ZDES mode 2 (2020) by finite differences, lattice-specific concerns); §3 (immersed boundary, wall law); §4.1–4.3, Table 1, Figs. 4–19 (flat plate, step, LEISA2); §5.
- [Heinz (2020)](/sources/heinz-2020.md) — §2.3, Eq. (12) (BGK form of the $k$, $\varepsilon$, $\omega$ equations); App. A, Eqs. (56)–(57) (BGK equation, relaxation time with $\nu_t$, RANS/LES/hybrid use).
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §III, Eqs. (12)–(13) (enlarged collision time of the gas-kinetic scheme).
- [Bose & Park (2018)](/sources/bose-2018.md) — §3 (lattice Boltzmann wall model, cited).
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §III E, Eqs. (80)–(92) (BGK, low-Mach limits, multiphase and compressible variants, hybrid LB–FV); §V (conclusions).
- [Simonis et al. (2022)](/sources/simonis-2022.md) — §1; §2.1–2.4, Eqs. (1)–(19), (28) (time filter, direct deconvolution, filtered BGK, MRT with residual-stress forcing); §3.2–3.4, Table 1, Figs. 2–9 (Taylor–Green calibration, comparison with spectral elements, subgrid activity, error plateau); §4; App. A–B, Tables 2–3, Fig. 10.
- [Ghidoni et al. (2026)](/sources/ghidoni-2026.md) — §1; §3.3, Eqs. (12)–(14); reference [11] (the explicit power-law wall model of Wilhelm et al., devised for lattice Boltzmann RANS, reused in a DG solver).
