---
type: Method
title: "High-order gas-kinetic schemes for turbulence simulation"
description: "A high-order gas-kinetic scheme is a finite-volume Navier–Stokes solver whose interface flux comes from the time-dependent BGK solution; this page gives its flux, collision time, reconstructions, two-stage fourth-order time stepping, curvilinear extension, its use as DNS and implicit LES of compressible wall-bounded flows, and its multi-GPU cost."
status: established
aliases: [HGKS, HGKS-cur, high-order GKS, gas-kinetic scheme, GKS, BGK finite-volume scheme]
tags: [gas-kinetic, dns, implicit-les, compressible, numerical-dissipation, gpu]
timestamp: 2026-10-27T21:10:00Z
---

# High-order gas-kinetic schemes for turbulence simulation

A **gas-kinetic scheme (GKS)** is a finite-volume method for the compressible
Navier–Stokes equations in which the numerical flux through a cell face is
not obtained from a Riemann solver but from the time-dependent solution of the
Bhatnagar–Gross–Krook (BGK) kinetic equation at the face: a gas distribution
function evolves from the reconstructed states towards a local Maxwellian, and
the inviscid and viscous fluxes are its moments. The **high-order gas-kinetic
scheme (HGKS)** of [Cao et al. (2022)](/sources/cao-2022.md) combines this
flux with fifth-order WENO-type reconstruction and a two-stage fourth-order
time discretization, parallelized with MPI, and is used without any
turbulence model as a [DNS](/definitions/direct-numerical-simulation.md) tool
for the [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md),
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md) and decaying
compressible [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
up to turbulent Mach number $M_t=1.6$. Cao et al. (2022, §1) motivate it by
the observation that DNS "is reported rarely within the finite volume framework
due to its over-dissipative nature" (citing the CFD Vision 2030 study), while
finite volumes have good conservation and shock-capturing properties.
[Zhao et al. (2023a)](/sources/zhao-2023.md) raise the reconstruction to
seventh order (non-compact) and add a fifth-order compact reconstruction, and
use the scheme as [implicit LES](/definitions/implicit-les.md);
[Wang et al. (2023b)](/sources/wang-2023-b.md) port it to single and
multiple GPUs and test single against double precision.

Page-local symbols: $f$ the gas distribution function, $g$ the local
Maxwellian, $\boldsymbol c=(c_1,c_2,c_3)$ the particle (microscopic)
velocity, $\vartheta$ the internal variables with $K_{\mathrm{int}}$ internal
degrees of freedom, $\tau_{\mathrm{col}}$ the collision time, $Q$ the vector of
conservative variables, $\Omega_{ijk}$ a cell and $|\Omega_{ijk}|$ its volume ($\Omega$ and $|\Omega|$ the whole domain). They replace Cao et al.'s $\boldsymbol u$ (particle
velocity), $\xi$, $N$ and $\tau$, which collide with the registry's velocity,
reference coordinate, polynomial degree and subgrid stress. Zhao et al.
(2023a) and Wang et al. (2023b) print the same symbols as Cao et al. and are
translated the same way; their macroscopic velocity $\boldsymbol U$ is the
registry's $\boldsymbol u$.

## Kinetic model and interface flux

The BGK equation, as stated by Cao et al. (2022, §2.1, Eqs. 1–2), is
$$\partial_tf+\boldsymbol c\cdot\nabla f=\frac{g-f}{\tau_{\mathrm{col}}},$$
with the compatibility condition $\int(g-f)\psi\,d\Xi=0$ for the collision
invariants $\psi=(1,c_1,c_2,c_3,\tfrac12(|\boldsymbol c|^2+|\vartheta|^2))^{\mathsf T}$,
which makes mass, momentum and energy the conserved moments. The number of
internal degrees of freedom is $K_{\mathrm{int}}=(5-3\gamma)/(\gamma-1)$, i.e.
$K_{\mathrm{int}}=2$ for $\gamma=1.4$; Wang et al. (2023b, §2, Eqs. 1–2) and
Zhao et al. (2023a, §2, Eq. 1) restate the same model (for Zhao et al.'s
printed form see the Qualifications).

The cell-averaged update is the finite-volume form
$\mathrm dQ_{ijk}/\mathrm dt=\mathcal L(Q_{ijk})=-|\Omega_{ijk}|^{-1}\sum_{p=1}^{6}\mathbb F_p(t)$
on orthogonal Cartesian cells, each face flux $\mathbb F_p$ evaluated by
$2\times2$ Gauss quadrature as the moment $\int\psi\,c_1f\,d\Xi$ of the
interface distribution (Eqs. 3–4). That distribution is built from the
integral solution of the BGK equation (Eq. 5, background from Xu's
second-order GKS),
$$f(\boldsymbol x,t,\boldsymbol c,\vartheta)=\frac{1}{\tau_{\mathrm{col}}}\int_0^tg(\boldsymbol x',t',\boldsymbol c,\vartheta)\,e^{-(t-t')/\tau_{\mathrm{col}}}\,dt'+e^{-t/\tau_{\mathrm{col}}}f_0(\boldsymbol x-\boldsymbol ct,\vartheta),\qquad \boldsymbol x'=\boldsymbol x-\boldsymbol c(t-t'),$$
with the initial distribution $f_0$ taken from the left and right
reconstructed Maxwellians (split by the sign of the normal particle velocity)
and the equilibrium $g$ from a Maxwellian at the interface whose moments
combine both sides. Expanding to second order in space and time gives the
second-order gas-kinetic flux; space and time derivatives of the Maxwellians
are fixed by the reconstructed slopes and the compatibility condition. As
Cao et al. (2022, §1) put it, the scheme "presents a gas evolution process
from kinetic scale to hydrodynamic scale": near a shock the kinetic particle
transport builds a "crisp and stable" transition, and in resolved smooth flow
it recovers the Navier–Stokes solution.

**Collision time.** In smooth flow $\tau_{\mathrm{col}}=\mu/p$ (also
Wang et al. 2023b, §2, who print only this smooth-flow form because their
tests have no discontinuities; Zhao et al. 2023a do not state the collision
time of their turbulence runs). Where the
reconstruction is discontinuous, an artificial term enlarges it (§3),
$$\tau_{\mathrm{col}}=\frac{\mu}{p}+C\,\Big|\frac{p_l-p_r}{p_l+p_r}\Big|\,\Delta t,\qquad C=1,$$
with $p_l$, $p_r$ the pressures on the two sides of the face, to "enlarge the
kinetic scale physics in the discontinuous region": the shock-capturing
dissipation of the scheme lives in the collision time.

**Inherent bulk viscosity.** The BGK model carries a bulk viscosity
$\mu_b=\frac{2K_{\mathrm{int}}}{3(K_{\mathrm{int}}+3)}\mu$ (Cao et al. 2022,
§3.1, citing Xu), which is $\mu_b=\tfrac{4}{15}\mu$ for a diatomic gas
*(compiler check, not in the sources)*. It enters the dissipation budget
below; see [bulk viscosity](/definitions/bulk-viscosity.md).

## Reconstruction and time stepping

**Spatial reconstruction** is fifth-order WENO, dimension by dimension, with
the tangential variation along each face reconstructed for the Gauss points
(Cao et al. 2022, §2.1, Remark 1). The authors choose it per regime:

- for smooth low-speed flow (Taylor–Green vortex, channel) the simplified
  smooth gas-kinetic flux and WENO with **linear weights**, "to avoid the
  numerical dissipation from artificially created interface discontinuity";
- for compressible isotropic turbulence WENO-Z on characteristic variables,
  with the shock-adaptive collision time above and "no extra special
  treatment" (§3.4).

**Two-stage fourth-order (S2O4) time discretization.** Because the
gas-kinetic flux is an explicit function of time, its time derivative is
available, and a Lax–Wendroff-type two-stage scheme reaches fourth order for
hyperbolic problems (Eq. 6, proofs cited, not given):
$$\begin{aligned}Q^*&=Q^n+\tfrac12\Delta t\,\mathcal L(Q^n)+\tfrac18\Delta t^2\,\partial_t\mathcal L(Q^n),\\Q^{n+1}&=Q^n+\Delta t\,\mathcal L(Q^n)+\tfrac16\Delta t^2\big(\partial_t\mathcal L(Q^n)+2\,\partial_t\mathcal L(Q^*)\big),\end{aligned}$$
with the face flux linearized in time, $\mathbb F_p(t)\approx\mathbb F_p^n+\partial_t\mathbb F_p^n(t-t_n)$,
and $\mathbb F_p^n$, $\partial_t\mathbb F_p^n$ fitted to the time integrals of
the flux over $\Delta t$ and $\Delta t/2$ (Eq. 7).

**Parallelization.** The domain of $N_x\times N_y\times N_z$ cells is split in
the $y$ and $z$ directions only ($x$ not split); each sub-domain exchanges
ghost data with its eight neighbours through MPI (§2.2).

## Higher-order and compact reconstruction

Zhao et al. (2023a, §3) keep the second-order gas-kinetic flux, Gauss-point
quadrature on the faces and S2O4 time stepping, and change only the
reconstruction (linear weights throughout, since the flows are smooth). The
variants are labelled by the normal and tangential orders:

- **N5T5**, the fifth-order non-compact baseline (WENO-Z-type stencil of
  five cell averages, $I_{i-2},\dots,I_{i+2}$);
- **N7T5** and **N7T7**, a **seventh-order non-compact** reconstruction in the
  face-normal direction (seventh-order WENO with linear weights on seven cell
  averages, then a sixth-degree polynomial constrained by six cell averages
  for the equilibrium state and its normal derivative, Eqs. 11–14), with
  fifth- or seventh-order tangential reconstruction done direction by
  direction (face averages to line averages to Gauss-point values);
- **C5T5**, a **fifth-order compact** reconstruction following the compact
  GKS of Ji et al. (as Zhao et al. 2023a, §3.2, cite it): each cell
  carries its average and a cell-averaged derivative, the latter obtained
  from time-evolved interface values by the Newton–Leibniz formula
  $(Q_x)_i=(Q_{i+1/2}-Q_{i-1/2})/h$ (Eq. 15), and a fifth-order Hermite WENO
  (HWENO) reconstruction uses cell averages of $I_{i-1},I_i,I_{i+1}$ and
  derivatives of $I_{i-1},I_{i+1}$ only (§3.3, Fig. 2). The interface values
  are advanced in time inside the two S2O4 stages from the gas-kinetic
  distribution.

The authors argue that the compact stencil "has the consistent physical and
numerical domains of dependence" (abstract, §1, §6); this is a design
argument, not a test in the paper.

**Gauss points decide the order.** Zhao et al. (2023a, §4) cite Ji's
thesis: "to achieve a 2Mth- or (2M-1)th-order spatial accuracy, at
least M×M Gaussian points are required for the cell interface", and the
leading error is $O(h_n^{r_n}+h_t^{r_t}+\Delta t^4)$ for normal and
tangential orders $r_n$, $r_t$ (page-local $h_n$, $h_t$ the normal and
tangential cell sizes). Their three-dimensional density-wave advection test
(Tables 2–5, $\Delta t=0.3h^{r/4}$ to keep the spatial order visible) gives:
N5T5 with $2\times2$ points, L1 orders 5.13, 5.19, 5.06; C5T5 with $2\times2$
points, 4.91, 5.12, 5.02; the seventh-order scheme with $2\times2$ points
6.29, 4.63, 4.07, falling to about four; with $4\times4$ points 7.35, 7.46,
6.91. Sixteen points cost 1.964 against 0.961 s per step (§4); the
turbulence runs therefore use $2\times2$ points, so the seventh-order labels
of those runs refer to the reconstruction, whose asymptotic order with four
Gauss points the same test shows to be about four. [Wang et al. (2023b)](/sources/wang-2023-b.md)
and Cao et al. (2022) use the fifth-order scheme with $2\times2$ points.

## Curvilinear meshes from discrete points (HGKS-cur)

[Cao et al. (2024)](/sources/cao-2024.md) extend the scheme from Cartesian
and analytically mapped meshes to general curvilinear meshes given only by
discrete grid points. The BGK equation is written in computational
coordinates $(\xi,\eta,\zeta)$ (page-local here, as on the
[geometric conservation law](/properties/geometric-conservation-law.md)
page) with the Jacobian $\mathcal J$ and the Jacobian-scaled metric terms
(§2.1, Eqs. 3–5),
$$\partial_t(\mathcal Jf)+\partial_\xi\big[(c_1\hat\xi_x+c_2\hat\xi_y+c_3\hat\xi_z)f\big]+\partial_\eta[\dots]+\partial_\zeta[\dots]=\frac{g-f}{\tau_{\mathrm{col}}}\,\mathcal J,$$
and the finite-volume update on the uniform computational mesh advances the
cell averages of the Jacobian-weighted conservative variables $\mathcal JQ$
(Eq. 6). On each face the gas-kinetic flux is evaluated at $2\times2$ Gauss
points in a local frame whose normal is the normalized metric vector, and
weighted by the face metric magnitude (Eq. 7). The metric terms are built
from fourth-order central differences of the grid points in a symmetric
conservative form that satisfies the geometric conservation law, then
interpolated to the Gauss points with cubic Lagrange formulae (Eqs. 10–11);
fifth-order WENO reconstructs the cell-averaged $\mathcal J$ and
$\mathcal JQ$ dimension by dimension in computational space, point values
follow as $Q=(\mathcal JQ)/\mathcal J$, and the gradients needed by the
gas-kinetic flux follow by the chain rule in the local orthogonal frame
(§2.3). Time stepping is the same S2O4 scheme (Eqs. 12–13), and the code is
parallelized by MPI with a two-dimensional domain decomposition in $y$ and
$z$ (§3).

**Verification** (§3.1–3.2, Tables 1–3, Fig. 3): an advected density wave on
two sinusoidally perturbed meshes converges at $L^1$ orders between 4.03
and 4.65 from $10^3$ to $160^3$ cells; a uniform flow stays uniform to
$O(10^{-14})$; the three-dimensional lid-driven cavity at $Re=1000$ ($33^3$)
and 3200 ($65^3$) agrees with a Chebyshev-collocation solution and an
experiment.

**Compressible channel as implicit LES** (§3.3, Tables 4–5): isothermal
walls, bulk Mach 1.5, bulk $Re=3000$, $\mu\propto T^{0.7}$, domain
$4\pi H\times2H\times4\pi H/3$, against the DNS of Coleman et al. and of
Morinishi et al. and a constrained LES of Jiang et al. The $128^3$ implicit
LES (G1: $\Delta y^+_{\min}=0.50$, $\Delta x^+=21.18$, $\Delta z^+=7.06$)
gives $Re_\tau=211$ and a non-dimensional wall heat flux $-0.047$, a $160^3$
run of the same scheme that the authors call DNS (G4) 213 and $-0.048$,
against 222 and $-0.049$ (Coleman) and 218 and $-0.048$ (Morinishi). Halving
the streamwise box leaves the wall statistics nearly unchanged but visibly
changes the r.m.s. of density and temperature; the native BGK Prandtl number
$Pr=1$ instead of the target 0.70 (corrected, as in Xu 2001, by modifying
the energy flux) changes the mean density, temperature and Mach profiles
"greatly" and raises $Re_\tau$ to 221. The authors conclude that a long
enough streamwise box and the target Prandtl number "are essential" in
compressible wall-bounded turbulence. The peak turbulent Mach number stays
below 0.25, "no strong shock-lets".

**Compressible periodic hill as implicit LES** (§3.4, Table 6, Figs. 12–16):
volume-averaged Mach 0.2, target $Re_b=2800$ (realized about 2730), mesh
built from discrete bottom-wall points, $10^6$ to $1.6\times10^7$ cells. The
separation and reattachment points ($x/H$) are 0.23/5.18 ($100^3$),
0.20/5.15 ($200\times100^2$) and 0.24/5.52 ($400\times200^2$), against
0.21/5.41 for the DNS of Peller & Manhart and 0.21/5.30 for the LES with the
approximate deconvolution model of Ziefle et al.; the implicit LES $C_p$
"agrees well" with the DNS, "better than the explicit LES", and the authors
state that the explicit LES over-predicts the Reynolds stresses and "may
pollute" this low-Reynolds-number separated flow, while noting that its
statistics are density-weighted and theirs are not. They judge that "coarse
grids is enough" for implicit LES of such flows given the cost of the
finest grid. See [periodic hill](/benchmarks/periodic-hill.md),
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md) and
[implicit LES](/definitions/implicit-les.md).

## GPU implementation

Wang et al. (2023b, §3) port the fifth-order WENO HGKS to Nvidia GPUs:

- **single GPU**: one thread per cell, kernels for the time step, WENO
  reconstruction, interface flux and update in each direction, each followed
  by a device synchronization (Alg. 1, Fig. 2); the code is built with the
  Nvidia CUDA and HPC SDK compilers;
- **multiple GPUs**: MPI with CUDA-aware MPI passing device data directly, a
  one-dimensional (slab) decomposition in $x$ chosen because it "reduces the
  frequency of GPU-GPU communications and improves performances" (pencil
  decomposition is kept for the CPU code with thousands of cores), halo
  exchange by an even/odd ordering of blocking sends and receives, and an
  all-reduce for the global time step (§3.2, Alg. 2, Figs. 3–4).

The GPU results of the nearly incompressible Taylor–Green vortex are stated
to be "identical" to those of the CPU code (§4.1, not plotted).

## Use as a DNS tool

**Taylor–Green vortex, $Re=1600$, $M=0.1$** (Cao et al. 2022, §3.1), on
$128^3$ to $1024^3$ uniform cells against the $512^3$ dispersion-relation-preserving
finite-difference reference (BB13) of DeBonis. The kinetic energy agrees
with the reference except on $128^3$; the peak of the kinetic-energy decay
rate differs markedly on $128^3$ and $256^3$ and agrees "excellently" with
refinement. The authors quantify the **numerical dissipation** a posteriori
by subtracting from the measured decay rate $-\mathrm dK/\mathrm dt$ ($K$ the
volume-averaged kinetic energy, page-local) the three physical contributions,
$$\varepsilon_{\mathrm{num}}=-\frac{\mathrm dK}{\mathrm dt}-(\varepsilon_1+\varepsilon_2+\varepsilon_3),\quad \varepsilon_1=\frac{2\mu}{\rho_0|\Omega|}\int_\Omega S^d_{ij}S^d_{ij}\,d\Omega,\quad \varepsilon_2=\frac{\mu_b}{\rho_0|\Omega|}\int_\Omega(\nabla\cdot\boldsymbol u)^2d\Omega,\quad \varepsilon_3=-\frac{1}{\rho_0|\Omega|}\int_\Omega p\,\nabla\cdot\boldsymbol u\,d\Omega,$$
the deviatoric, bulk-viscous and pressure-dilatation terms (§3.1). In this
nearly incompressible flow $\varepsilon_1$ dominates, $\varepsilon_2$ and
$\varepsilon_3$ are negligible, and $\varepsilon_{\mathrm{num}}$ decreases
with refinement; on coarse grids $\varepsilon_1+\varepsilon_2+\varepsilon_3$
is significantly lower than the measured decay rate. From this the authors
conclude that "the filtering due to the coarse mesh correctly mimics the
physical dissipation from the unresolved scale dynamics", which in their
reading "validates the usage of high-order numerical methods for the implicit
large-eddy simulations" (see [implicit LES](/definitions/implicit-les.md),
[numerical dissipation](/properties/numerical-dissipation.md), and the
Qualifications). They call the $1024^3$ case "the finest resolution for the
Taylor–Green vortex problem".

**Turbulent channel flow, $Re_\tau=180$, $M=0.1$** (§3.3), "the first
simulation of turbulent channel flow using HGKS": $96^3$ (G1) and $128^3$
(G2) cells with a $\tanh$ wall-normal stretching, $\Delta x^+=11.77$,
$\Delta z^+=5.89$, $\Delta y^+$ from 0.29 to 7.77 on G1, and $\Delta x^+=8.83$,
$\Delta z^+=4.42$, $\Delta y^+$ from 0.21 to 5.83 on G2; constant mass flux
enforced by a body force recomputed each step. G2 gives $Re_\tau=179.21$ and
$C_f=7.82\times10^{-3}$, against $8.39\times10^{-3}$ from Dean's correlation
(Table 6). Mean velocity agrees with the spectral DNS of Kim, Moin & Moser and
with lattice-Boltzmann and discrete-unified-gas-kinetic (DUGKS) results; the
Reynolds shear stress is "clearly better than DUGKS and LBM", while DUGKS is
better for the near-wall streamwise r.m.s. and LBM or DUGKS for the other
r.m.s. components in parts of the channel; the authors' overall verdict is
that "HGKS outweighs LBM and DUGKS" (§3.3, Figs. 10–12). They add that their
results use a coarse stretched grid, whereas the lattice Boltzmann method
needs equidistant grids with $\Delta x^+\approx0.3$ everywhere.

**Decaying compressible isotropic turbulence** (§3.4), $Re_\lambda=72$,
$M_t=0.8,1.0,1.2,1.6$ ($M_t=\sqrt3u_{\mathrm{rms}}/c$), $512^3$ cells: the
scheme runs into the supersonic regime with WENO-Z and the adaptive collision
time only, and the time histories of density r.m.s., kinetic energy,
skewness, flatness, solenoidal and dilatational dissipation and
pressure–dilatation are offered as benchmark data. The resolution criterion
$k_{\max}\eta_0\ge2.71$, taken from the authors' earlier HGKS study, is met
with $k_{\max}\eta_0=3.613$ (Table 8). Dilatation fields show shocklets as
narrow ribbons with expansion regions as blocks beside them (Fig. 15). The
authors state that compact finite differences are limited to $M_t\le0.8$
and that spectral and lattice-Boltzmann methods "fail to capture shocklets
and suffer from numerical instability" in compressible flow with shocks
(§1, §3.4), which is the regime HGKS is meant for. They also note that the
Kolmogorov length exceeds the mean free path in every run (grid spacing
$0.819\eta_0$ and 1.275 to 2.551 mean free paths), which they offer as
"intuitive evidence" that the smallest eddies remain within the continuum
assumption.

## Use as implicit LES

Zhao et al. (2023a, §5) run the scheme with molecular viscosity only and no
subgrid model, as [implicit LES](/definitions/implicit-les.md) in which the
numerical dissipation of the reconstruction and flux replaces the subgrid
dissipation (§1, citing Boris et al. 1992 as origin and MILES).

- **Taylor–Green vortex**, $Re=1600$, $M=0.1$, $Pr=1$, $256^3$ (§5.1):
  kinetic-energy histories are "basically consistent with DNS" except at
  late times, where N7T7 is best, so "the high-order reconstruction in the
  tangential direction is also important"; higher order and compactness both
  improve the enstrophy-based dissipation. With the same budget
  $\varepsilon_{\mathrm{num}}$ as above (Eqs. 22–23, physical terms by
  sixth-order central differences, $\mu_b$ with $K_{\mathrm{int}}=2$), the
  numerical dissipation falls with higher-order or compact reconstruction,
  and the authors conclude that "the 5th-order scheme for ILES is still
  over-dissipative, and reducing the numerical dissipation can improve the
  results" (Fig. 7).
- **Channel flow**, $M=0.1$, isothermal walls, constant flux, against the
  DNS of Moser et al. (§5.2). At nominal $Re_\tau=180$ on
  $64\times96\times64$ cells ($\Delta x^+=17.66$, $\Delta y^+$ from 0.29
  to 7.76, Table 6) the realized $Re_\tau$ is 171.33 (N5T5), 177.04 (N7T5),
  178.44 (N7T7) and 176.27 (C5T5) against 178.12 for DNS (Table 8); at
  nominal $Re_\tau=395$ on $96^3$ it is 360.35, 378.97, 380.45 and 377.05
  against 392.24 (Table 9). Mean velocity, r.m.s. profiles and Reynolds
  shear stress improve with order and with compactness; "the 5th-order
  compact scheme can almost achieve the accuracy of the 7th-order
  non-compact scheme" (Figs. 8–13). Spectra at $y^+=30$ and 180 match DNS at
  low wavenumbers and keep more energy at high wavenumbers with the
  higher-order schemes, but all runs show "an unnatural leveling-off of the
  energy spectrum near the cutoff wavenumber", which the authors attribute to
  the mesh resolution (Figs. 14–15).

The viscosity of these runs is set from the target $Re_\tau$ through a log
law with $\kappa=0.40$, $B=5.5$ (Eqs. 24–26); each case uses one grid, with
no convergence study of the statistics.

## Explicit subgrid models inside the gas-kinetic flux

[Zhao et al. (2021)](/sources/zhao-2021-c.md) compare the implicit LES of
the fifth-order scheme (linear-weight WENO normal to the face, fourth-order
tangential polynomials, $2\times2$ Gauss points, S2O4) with four explicit
eddy-viscosity models in wall-resolved
[channel flow](/benchmarks/turbulent-channel-flow.md) at $M=0.1$.

**Coupling through the collision time.** An eddy viscosity enters the BGK
model as an enlarged relaxation time (§III, Eqs. 12–13, citing Chen et al.
2003 and 2004): with page-local $\tau_{\mathrm{col},t}$ the turbulent
enlargement, the Chapman–Enskog expansion of
$\partial_tf+\boldsymbol c\cdot\nabla f=(g-f)/(\tau_{\mathrm{col}}+\tau_{\mathrm{col},t})$
gives
$$\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=\frac{\mu+\mu_t}{p},$$
so any model that supplies $\mu_t$ can be used. The models are the
[Vreman model](/methods/vreman-model.md) (constant 0.01 at $Re_\tau=180$,
the best of 0.01–0.1, and 0.07 at $Re_\tau=395$), the
[dynamic Smagorinsky model](/methods/dynamic-procedure.md) with
plane-averaged and clipped coefficient, the [WALE model](/methods/wale-model.md)
($C_w=0.5$) and a dynamic Clark model whose
[gradient](/methods/gradient-model.md) and Smagorinsky stress is converted
to an equivalent eddy viscosity by matching its dissipation,
$\nu_t=\Pi/(2\bar S_{ij}\bar S_{ij})$, with the coefficient taken from the
dynamic Smagorinsky procedure instead of its own (§III.A–D, Eqs. 14–23).
The scalar $\nu_t$ keeps only the contraction of the gradient term with
the resolved strain, not its tensor structure *(compiler check, not in the
sources)*.

**Two interface distributions.** "Flux 1" is the smooth-flow simplification
of the second-order distribution,
$f=g_0\big[1-\tau_{\mathrm{col}}(a^{\mathrm e}_ic_i+A^{\mathrm e})+tA^{\mathrm e}\big]$
($a^{\mathrm e}_i$, $A^{\mathrm e}$ page-local, the spatial and temporal
slopes of the equilibrium state; Eq. 7). For under-resolved higher-Reynolds
runs the authors propose "flux 2", which keeps a kinetic upwind part
(Eq. 8):
$$f=(1-e^{-t/\tau_{\mathrm{col}}})\,g_0+e^{-t/\tau_{\mathrm{col}}}\big[g^lH(c_1)+g^r(1-H(c_1))\big]+g_0\big[-\tau_{\mathrm{col}}(a^{\mathrm e}_ic_i+A^{\mathrm e})+tA^{\mathrm e}\big],$$
with $g^l$, $g^r$ the reconstructed Maxwellians on the two sides and $H$ the
Heaviside function. Flux 1 suffices at $Re_\tau=180$, where interface
discontinuities are minor, and gives better results there; at
$Re_\tau=395$ flux 2, whose dissipation "is a little larger", gives better
turbulence intensities and is used, at about twice the cost (§IV, App. A,
Figs. 22–27).

**Results** (against the DNS of Kim, Moin & Moser and of Moser, Kim &
Mansour; domain $2\pi\times2\times\pi$, statistics over $200\,\delta/U_c$
after about $400\,\delta/U_c$, $U_c$ the centreline velocity):

| Case | grid | resolved $Re_\tau$: DNS / implicit LES / Vreman / dynamic Smagorinsky / WALE / dynamic Clark |
|---|---|---|
| $Re_\tau=180$, flux 1 | $96^3$, $\Delta x^+=11.77$, $\Delta z^+=5.89$ | 178.12 / 177.89 / 174.99 / 175.47 / 172.57 / 172.06 |
| $Re_\tau=395$, flux 2 | $96^3$, $\Delta x^+=25.84$, $\Delta z^+=12.92$ | 392.24 / 360.35 / 351.36 / 359.54 / — / 351.35 |
| $Re_\tau=395$, flux 2 | $128^3$, $\Delta x^+=19.38$, $\Delta z^+=9.69$ | 392.24 / 376.33 / 370.13 / 375.22 / — / 369.57 |

(Tables I, V–VII; no WALE results are shown at $Re_\tau=395$.) Every
explicit model lowers the resolved friction velocity below that of the
implicit LES; the implicit LES is closest to the DNS in mean velocity and,
at $Re_\tau=395$, in the r.m.s. velocities and Reynolds shear stress, while
at $Re_\tau=180$ the dynamic Smagorinsky model matches the Reynolds shear
stress better, followed by the implicit LES; spectra at $y^+=30$ and 395
show no visible differences between methods and the same "unnatural
leveling-off" near the cut-off as above (§V, Figs. 2–19). The authors
explain the ranking by the numerical dissipation of the high-order scheme
already sufficing as subgrid dissipation, so that an explicit model
over-dissipates and lowers the wall velocity gradient (Abstract, §VI); this
is stated, not measured by a dissipation budget. Refining the $Re_\tau=180$
grid from $64^3$ to $96^3$ "significantly" improves all statistics; they
state that "when the grids are refined, the numerical dissipation
decreases" (App. B, Table VIII). They conclude that implicit LES is "more suitable than traditional
LES models" in this finite-volume approach (§VI).

**Taylor–Green vortex: implicit against explicit LES, with a budget.**
[Cao et al. (2022b)](/sources/cao-2022-c.md) repeat the comparison on the
compressible [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
($M=0.1$, $Re=1600$, $\gamma=1.4$, $Pr=1$) with the fourth-order two-stage
scheme on $256^3$ cells (and $128^3$, $384^3$ in App. B), against the
$1024^3$ DNS of Cao et al. (2022). The eddy viscosity enters through the
same enlarged collision time, $\tau_{\mathrm{col}}+\tau_{\mathrm{col},t}=(\mu+\mu_t)/p$
(§III, Eqs. 7–8, citing Zhao et al. 2021), with the cell as the implicit
filter and no explicit filter. The models are the static
[Smagorinsky model](/methods/smagorinsky-model.md) with $C_s=0.1$, the
[Vreman model](/methods/vreman-model.md) with constant $2.5C_s^2=0.025$
and the [dynamic Smagorinsky model](/methods/dynamic-procedure.md) with a
domain-averaged coefficient and a 27-point discrete top-hat test filter of
twice the grid width (§III, Eqs. 9–13, App. A). Findings (§IV, Figs. 1–3,
7–12):

- the kinetic energy and its decay rate $-\mathrm dE_k/\mathrm dt$ are
  insensitive to the model and the grid, while the enstrophy-based
  dissipation and the deviatoric-strain dissipation $\varepsilon_1$ are
  closest to the DNS for the implicit LES; among the explicit models the
  dynamic one is best;
- the total subgrid dissipation, estimated a posteriori as the budget
  residual $\varepsilon_{\mathrm{sgs}}=-\mathrm dE_k/\mathrm dt-\varepsilon_{\mathrm{phy}}$
  (Eq. 22; [bulk-viscous](/definitions/bulk-viscosity.md) and
  [pressure-dilatation](/definitions/pressure-dilatation.md) parts
  included in $\varepsilon_{\mathrm{phy}}$), is smallest for the implicit
  LES on every grid: $1.5\times10^{-5}$, $1.4\times10^{-4}$,
  $6.7\times10^{-4}$, $1.8\times10^{-5}$ at $t=2.5$, 5, 10, 15, against
  $2.8\times10^{-5}$, $3.5\times10^{-4}$, $1.4\times10^{-3}$,
  $2.5\times10^{-4}$ for the static Smagorinsky model, with the dynamic
  model in between (Table II);
- the static explicit LES on $384^3$ is only comparable with the implicit
  LES on $256^3$.

The authors read the scheme's numerical dissipation as a built-in subgrid
dissipation that suffices for this low-Reynolds-number flow, the explicit
eddy viscosity as adding to it and smearing the resolved vorticity; §I
cites the same ranking from their compressible periodic-hill LES (the
arXiv preprint of [Cao et al. 2024](/sources/cao-2024.md)), where explicit
LES over-predicts the Reynolds stresses (§I, §IV C, §V). The modelled and numerical parts of
the explicit-LES residual are not separated. The decomposition is on
[implicit LES](/definitions/implicit-les.md) and
[numerical dissipation](/properties/numerical-dissipation.md).

## Cost

Cao et al. (2022, §3.2) note that the finite-volume scheme "is considered
to be less efficient than the finite difference method" because of the
multidimensional reconstruction and flux quadrature, and that the
gas-kinetic flux is considered more complicated than Riemann solvers. On TianHe-II (2.2 GHz) the $512^3$ Taylor–Green
run took 69.00, 17.29 and 4.66 s per step on 64, 256 and 1024 cores
(Table 1). Whole runs cost 213, 3456, 67,584 and 747,062 core hours from
$128^3$ to $1024^3$ (Table 3), against 2560 and 47,840 core hours for the
BB13 finite-difference code at $256^3$ and $512^3$ on a 2.6 GHz machine
(Table 4): HGKS is "around 1.4 times" more expensive, "around 1.2 times"
after correcting for processor speed, which the authors call "comparable and
affordable" given its robustness. The comparison uses different machines and
time steps.

**Subgrid-model cost** (Zhao et al. 2021, Tables III–IV;
$64\times96\times64$ cells, 16 cores): implicit LES 0.520 s per step,
Vreman 0.534, WALE 0.552, dynamic Smagorinsky 0.613, dynamic Clark 0.624
with flux 1; 1.014 to 1.123 s with flux 2, "almost twice" flux 1. On the
same grid and core count Zhao et al. (2023a, Table 7) print 0.595 s for
N5T5; neither paper names the hardware.

**Reconstruction cost** (Zhao et al. 2023a, Table 7; $64\times96\times64$
cells, 16 CPU cores, $2\times2$ Gauss points): 0.595 (N5T5), 0.649 (N7T5),
0.961 (N7T7) and 0.618 (C5T5) s per step. The authors note that higher
order raises the cost and the compact reconstruction raises it only slightly
(§5.2); the tangential seventh order costs about half again
($0.961/0.649=1.48$, *compiler check, not in the sources*).

**GPU speedups** (Wang et al. 2023b, §4.1, Tables 2–5; Taylor–Green vortex,
double precision, 20 convective times): against an 8-core desktop OpenMP
code, one TITAN RTX is about 7 times and one Tesla V100 about 16 times
faster on $64^3$ to $256^3$. The V100 has about 15 times the double-precision
peak of the TITAN RTX but runs only about 2 times faster, which the authors
attribute to memory bandwidth ("the bottleneck for current memory-intensive
simulations"; not profiled). The $256^3$ run takes 11.697 h on one V100 and
1.987 h on eight; $512^3$ takes 22.252, 19.055 and 13.466 h on 8, 12 and 16
V100s, with the communication share rising and scaling degrading beyond 8
GPUs, where inter-node traffic leaves NVLink for RoCE (Table 5, Figs. 5–6).
Eight V100s run the $512^3$ case about 3 times faster than 1024 cores of
TianHe-II (66 h, the CPU data of Cao et al. 2022), from which the authors
infer an equivalence to about 3000 CPU cores, in agreement with the FluTAS
code they cite; no run on 3000 cores is reported (§4.1, Tables 4–5).

**Single against double precision** (Wang et al. 2023b, §4.2, Table 8;
channel at $Re_\tau=395$, $M=0.1$, and at bulk $Re=3000$, bulk $M=0.8$):
single precision halves memory (ratios 1.928 to 1.968) and runs 2.7 times
(TITAN RTX) or 1.7 times (V100) faster. Mean and r.m.s. profiles averaged over
200 $\delta/U_c$ agree between precisions, and the fine grids agree with the
reference DNS (Moser, Kim & Mansour; Fu et al.), but instantaneous r.m.s.
profiles at $t=20$ and $200\,\delta/U_c$ after a common restart differ
visibly; the authors attribute this to single-precision round-off "approximately
equals to or larger than the errors of numerical scheme" and conclude that
single precision "may not be safe for DNS in turbulence especially for
time-evolutionary turbulent flows", while it "may be used" for LES and RANS
(§4.2, §5). The deviation is shown in instantaneous r.m.s. profiles
(Fig. 14); the profiles averaged over 200 $\delta/U_c$ show "negligible"
differences between precisions (Figs. 10–13).

## Qualifications

- **Version read (Cao et al. 2022).** The arXiv v1 preprint (May 2020); the
  journal version may differ in text and numbers.
- **Implicit-LES reading.** Cao et al. (2022, §3.1) write both that "a large
  discrepancy is observed in the peak dissipation rate" on $128^3$ and
  $256^3$ and that "$\varepsilon(E_k)$ is well predicted at all grid levels";
  the implicit-LES conclusion is drawn from the second statement, i.e. from
  the volume-averaged decay rate of the Taylor–Green vortex alone. The
  authors add that implicit LES "for complex turbulent flows is still under
  debate".
- **Printed slips.** Eq. (11) prints the energy balance of decaying
  turbulence as $\mathrm d\langle K\rangle/\mathrm dt=\varepsilon+\langle p\Theta\rangle$
  ($\Theta$ the dilatation, page-local) with positive dissipations, while the
  text describes a decay; the dissipation enters with a minus sign. The
  resolution formula is printed $\kappa_{max}=\sqrt2\kappa_0N/3$, here
  $k_{\max}=\sqrt2\,k_0N_x/3$ with $N_x=512$ cells per direction and
  $k_0=8$ the spectrum peak; with $h=2\pi/512$ and the tabulated
  $h/\eta_0=0.819$ (the paper's $\Delta$), $\sqrt2\cdot512/3\cdot\eta_0=3.617$ reproduces the
  tabulated 3.613, while the printed factor $k_0$ would give about 29
  *(compiler check, not in the sources)*. The wall shear stress is printed
  $\tau_{\mathrm{wall}}=\partial U/\partial y|_{\mathrm{wall}}$, without the
  viscosity. The speedup is printed $S_n=T_n/T_{n_{\mathrm{ref}}}$, while
  the ideal value is stated as $n/n_{\mathrm{ref}}$, which holds for the
  inverse ratio. §1 announces tests "to the hypersonic one"; the abstract,
  §3.4 and the conclusions say supersonic ($M_t\le1.6$).
- The priority claims ("first successful DNS application of HGKS",
  "finest resolution" of the Taylor–Green vortex) are the authors'.
- **Versions read.** Zhao et al. (2023a): arXiv 2208.07713v1; Wang et al.
  (2023b): arXiv 2207.01173v1. Locators are those of the preprints.
- **Printed slips (Zhao et al. 2023a).** §2 prints the internal degrees of
  freedom as the product $N=(5-3\gamma)(\gamma-1)$, which gives 0.32 for
  $\gamma=1.4$, while §5.1 uses $N=2$, the value of the quotient
  $(5-3\gamma)/(\gamma-1)$ printed by Wang et al. (2023b) *(compiler check,
  not in the sources)*. §5.2 prints $\mu=2.83\times10^{-4}$ for
  $Re_\tau=180$; the paper's own Eqs. (25)–(26) with $U_c=1$ give
  $3.01\times10^{-4}$, and the same procedure reproduces the printed
  $1.24\times10^{-4}$ at $Re_\tau=395$ *(compiler check, not in the
  sources)*. Table 6 prints $\Delta z^+=8.33$ for $\pi\cdot180/64=8.84$
  *(compiler check, not in the sources)*.
- **Printed slips (Wang et al. 2023b).** The scalability is defined as
  $S_n=T_n/T_1$ with the ideal value stated as $n$, which holds for the
  inverse ratio; the single/double-precision memory ratio is defined as
  single over double while the printed values are double over single
  (e.g. $5.355/2.761=1.94$, *compiler check, not in the sources*); the text
  says the coarse channel grids ran on one GPU while Table 8 states two.

- **Version read (Cao et al. 2024).** The file is the arXiv 2107.08609v1
  preprint of July 2021, with five authors (Cao, Pan, Wan, Xu, Chen); the
  version of record (J. Sci. Comput., 2024) lists four. Claims and
  locators are those of the preprint.
- **Cited limits of other schemes.** Cao et al. (2022, §1, §3.4) state
  that compact finite differences are limited to $M_t\le0.8$; Cao et al.
  (2024, §1) cite a limit $M_t\le1.2$ for high-order finite-difference DNS
  of supersonic isotropic turbulence and an HGKS run at $M_t=2.0$ (both
  from cited works), above the $M_t=1.6$ of Cao et al. (2022). The limits
  concern different scheme classes and are cited, not tested.
- **Printed slips (Cao et al. 2024).** Eq. (11) does not reproduce the
  metric terms of Eq. (5) (see the
  [geometric conservation law](/properties/geometric-conservation-law.md));
  the bulk velocity and density are printed as integrals over $[-H,H]$
  without the factor $1/(2H)$; $C_f$ and $C_p$ of the hill are normalized
  by $\rho_bU_b^2$ without the factor $\tfrac12$ (so their values are half
  those of a normalization by $\tfrac12\rho_bU_b^2$, *compiler check, not in
  the sources*); with $\eta\in[-1.5\pi,1.5\pi]$ the printed
  wall-normal mapping does not span $[-H,H]$; and the wall-unit spacings
  of G1 and G4 imply $Re_\tau\approx216$, against the tabulated 211 and 213
  *(compiler check, not in the sources)*.
- The DNS/implicit-LES boundary of Cao et al. (2024) is set by resolution
  only: G4 ($160^3$) is called DNS, G1 ($128^3$) implicit LES, with the same
  scheme. Their hill separation points do not converge monotonically with
  the grid.

- **Kinetic fluxes in multi-material solvers.** The review of
  [Maltsev et al. (2022)](/sources/maltsev-2022.md), §III E, §IV C–E,
  cites gas-kinetic ideas in high-order multiphase codes: the discrete
  unified gas-kinetic scheme as a finite-volume discretization of the
  discrete-velocity BGK equation with double distributions, lattice
  Boltzmann intercell fluxes in finite-volume solvers, and a non-oscillatory
  kinetic flux in DG for Mie–Grüneisen materials; none is a turbulence
  application.
- **Printed slips (Zhao et al. 2021).** The same as in Zhao et al. (2023a):
  the internal degrees of freedom are printed as the product
  $(5-3\gamma)(\gamma-1)$, which gives 0.32 for $\gamma=1.4$ where the
  quotient gives 2; $\mu=2.83\times10^{-4}$ is printed for
  $Re_\tau=180$, while Eqs. (25)–(26) give $3.01\times10^{-4}$ and Table V
  gives $u_\tau/Re_\tau=3.007\times10^{-4}$ for the implicit LES; Table VIII
  prints $\Delta z^+=8.33$ for $N_z=64$, where $\pi\cdot180/64=8.84$ *(all
  compiler checks, not in the sources)*. With the printed $L_{ij}$ and
  $M_{ij}$ (no factor 2) and $\mu_t=\bar\rho C\Delta^2|\bar S|$, the
  least-squares coefficient of the Germano identity carries a factor
  $-\tfrac12$ that Eq. (16) does not print *(compiler check, not in the
  sources)*. The DNS at $Re_\tau=180$ is credited to "Moser et al." where
  ref. [1] is Kim, Moin & Moser.
- **Internal inconsistency (Zhao et al. 2021).** The abstract and
  conclusions give the implicit LES the better Reynolds stress, while §V.B
  finds the dynamic Smagorinsky model better at $Re_\tau=180$; the claim
  holds at $Re_\tau=395$. The Vreman constant changes sevenfold between the
  two Reynolds numbers by tuning.
- **Values shared by Zhao et al. (2021) and Zhao et al. (2023a).** The
  implicit LES at nominal $Re_\tau=395$ on $96^3$ reaches 360.35 in both
  (2021, Table VI, 360.3495; 2023a, Table 9, N5T5); the
  $64\times96\times64$ grid has the same printed spacings in both
  ($\Delta x^+=17.66$, $\Delta y^+$ 0.29 to 7.76, $\Delta z^+=8.33$; 2021,
  Table VIII; 2023a, Table 6), and both print $\mu=2.83\times10^{-4}$ for
  $Re_\tau=180$.

- **Printed ratios (Cao et al. 2022b).** The abstract and §IV B state that
  $\varepsilon_1$ is "approximately 20 times larger" than the a priori
  subgrid production; the Table I values give ratios of about 68, 32, 22
  and 35 at $t=2.5$, 5, 10 and 15 *(compiler check, not in the sources)*.
  §IV C states that static explicit LES has an
  $\varepsilon_{\mathrm{sgs}}$ "approximately two times larger" than
  implicit LES; the Table II values give 1.9, 2.5, 2.1 and about 14
  (Smagorinsky) and 1.7, 2.3, 1.9 and 10 (Vreman) *(compiler check, not in
  the sources)*. The a posteriori $\varepsilon_{\mathrm{sgs}}$ is said to
  exceed the a priori production "except" at $t=15$; at $t=15$ Table II
  prints $2.5\times10^{-4}$ (Smagorinsky) and $1.8\times10^{-4}$ (Vreman)
  against the a priori $1.3\times10^{-4}$ of Table I, and
  $1.8\times10^{-5}$ (implicit) and $9.4\times10^{-5}$ (dynamic) below
  it. The evidence is a single low-Reynolds-number flow
  with one scheme, to which the authors restrict their conclusion.

## Contradictions

- **Is the numerical dissipation of the fifth-order scheme right for
  implicit LES?** *Open.* [Cao et al. (2022)](/sources/cao-2022.md) (§3.1)
  state that, because the kinetic-energy decay rate of the Taylor–Green
  vortex at $Re=1600$ is "well predicted at all grid levels" ($128^3$ to
  $1024^3$), "the filtering due to the coarse mesh correctly mimics the
  physical dissipation from the unresolved scale dynamics".
  [Zhao et al. (2023a)](/sources/zhao-2023.md) (§5.1, Fig. 7) run the same
  fifth-order scheme (N5T5) on the same flow at $256^3$, find that
  higher-order or compact reconstruction lowers the measured
  $\varepsilon_{\mathrm{num}}$ and improves the energy, dissipation and
  enstrophy histories, and conclude that "the 5th-order scheme for ILES is
  still over-dissipative"; their channel results (§5.2, Tables 8–9) point the
  same way. Zhao et al. (§1) cite the authors' earlier fifth-order implicit
  LES as showing that high-order GKS "can provide appropriate numerical
  dissipation" and present their result as an improvement on it; they cite Cao et al. only
  for the dissipation decomposition (§5.1).
  [Zhao et al. (2021)](/sources/zhao-2021-c.md), with the fifth-order
  linear-weight scheme on channel flow, side with the first reading: the
  numerical dissipation is "enough to replace" the subgrid dissipation and
  explicit models only add to it (Abstract, §VI), a statement drawn from
  profile comparisons, not from a dissipation measurement. Their $96^3$
  implicit LES at $Re_\tau=180$ reaches $Re_\tau=177.89$ (Table V), whereas
  Zhao et al. (2023a, Table 8) report 171.33 for N5T5 on
  $64\times96\times64$ cells, and Zhao et al. (2021, App. B, Table VIII)
  find their own $64\times96\times64$ results worse than the $96^3$ ones.
  [Cao et al. (2022b)](/sources/cao-2022-c.md) (§IV C, §V, Table II) add a
  budget measurement to the first reading on the Taylor–Green vortex at
  $256^3$, with the scheme of Cao et al. (2022), which they call
  fourth-order (reconstruction not printed): the implicit LES has the
  smallest total subgrid dissipation and the best enstrophy-based
  dissipation, the explicit models only add dissipation, and the
  numerical dissipation serves as the subgrid dissipation, explicit
  modelled dissipation not being required at this low Reynolds number (§V).

# Citations

- [Cao et al. (2022)](/sources/cao-2022.md) — §1 (motivation, finite-volume DNS, competing methods); §2.1, Eqs. (1)–(7) (BGK model, gas-kinetic flux, WENO, S2O4), Remark 1; §2.2 (MPI decomposition); §3 (collision time); §3.1 (Taylor–Green vortex, bulk viscosity, numerical-dissipation decomposition); §3.2, Tables 1–4 (scaling, cost); §3.3, Tables 5–7, Figs. 10–12 (channel); §3.4, Table 8, Figs. 13–15 (compressible isotropic turbulence).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — arXiv v1: §1 (implicit LES, compact stencils); §2, Eqs. (1)–(10) (BGK flux, Gauss quadrature); §3.1–3.3, Eqs. (11)–(15), Figs. 1–2 (seventh-order non-compact and fifth-order compact reconstruction); §4, Tables 2–5 (accuracy, Gauss-point rule, cost of 16 points); §5.1, Eqs. (19)–(23), Figs. 3–7 (Taylor–Green vortex, numerical dissipation); §5.2, Eqs. (24)–(28), Tables 6–9, Figs. 8–17 (channel flow); Table 7 (cost).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — arXiv v1: §2, Eqs. (1)–(8) (BGK flux, S2O4); §3.1–3.2, Algs. 1–2, Figs. 2–4 (single- and multi-GPU implementation); §4.1, Tables 2–5, Figs. 5–8 (speedups, scaling, compressible Taylor–Green vortex); §4.2, Tables 6–8, Figs. 10–14 (channel flow, single against double precision); §5.
- [Cao et al. (2024)](/sources/cao-2024.md) — arXiv 2107.08609v1: §1 (implicit LES, cited $M_t$ limits); §2.1, Eqs. (3)–(9) (transformed BGK equation, curvilinear flux); §2.3, Eqs. (10)–(11) (metrics, WENO in computational space); §2.4, Eqs. (12)–(13); §3.1–3.2, Tables 1–3, Fig. 3 (accuracy, free-stream preservation, cavity); §3.3, Tables 4–5, Figs. 5–9 (compressible channel); §3.4, Table 6, Figs. 11–16 (compressible periodic hill).
- [Cao et al. (2022b)](/sources/cao-2022-c.md) — §I (periodic-hill ranking, cited); §II, Eqs. (1)–(6) (fourth-order scheme); §III, Eqs. (7)–(13), App. A (eddy viscosity through the collision time, three models, top-hat test filter); §IV A–C, Eqs. (14)–(22), Tables I–II, Figs. 1–8; App. B, Figs. 9–12 (implicit against explicit LES of the Taylor–Green vortex, subgrid-dissipation budget); §V.
- [Zhao et al. (2021)](/sources/zhao-2021-c.md) — §II, Eqs. (1)–(11) (BGK flux, flux 1 and flux 2, reconstruction); §III, Eqs. (12)–(23) (eddy viscosity through the collision time; Vreman, dynamic Smagorinsky, WALE, dynamic Clark); §IV, Table I (setup); §V, Tables III–VII, Figs. 2–21 (results, cost); §VI; App. A–B, Table VIII.
- [Maltsev et al. (2022)](/sources/maltsev-2022.md) — §III E, §IV C–E (kinetic and lattice-Boltzmann fluxes in multi-material solvers, cited).
