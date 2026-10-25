---
type: Method
title: "High-order gas-kinetic schemes for turbulence simulation"
description: "A high-order gas-kinetic scheme is a finite-volume Navier–Stokes solver whose interface flux comes from the time-dependent solution of the BGK kinetic equation; this page gives its flux, collision time, reconstruction and two-stage fourth-order time stepping, and its use and cost as a DNS tool from low-Mach to supersonic turbulence."
status: established
aliases: [HGKS, high-order GKS, gas-kinetic scheme, GKS, BGK finite-volume scheme]
tags: [gas-kinetic, dns, compressible, numerical-dissipation]
timestamp: 2026-10-25T19:47:00Z
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

Page-local symbols: $f$ the gas distribution function, $g$ the local
Maxwellian, $\boldsymbol c=(c_1,c_2,c_3)$ the particle (microscopic)
velocity, $\vartheta$ the internal variables with $K_{\mathrm{int}}$ internal
degrees of freedom, $\tau_{\mathrm{col}}$ the collision time, $Q$ the vector of
conservative variables, $\Omega_{ijk}$ a cell and $|\Omega_{ijk}|$ its volume ($\Omega$ and $|\Omega|$ the whole domain). They replace Cao et al.'s $\boldsymbol u$ (particle
velocity), $\xi$, $N$ and $\tau$, which collide with the registry's velocity,
reference coordinate, polynomial degree and subgrid stress.

## Kinetic model and interface flux

The BGK equation, as recalled by Cao et al. (2022, §2.1, Eqs. 1–2), is
$$\partial_tf+\boldsymbol c\cdot\nabla f=\frac{g-f}{\tau_{\mathrm{col}}},$$
with the compatibility condition $\int(g-f)\psi\,d\Xi=0$ for the collision
invariants $\psi=(1,c_1,c_2,c_3,\tfrac12(|\boldsymbol c|^2+|\vartheta|^2))^{\mathsf T}$,
which makes mass, momentum and energy the conserved moments. The number of
internal degrees of freedom is $K_{\mathrm{int}}=(5-3\gamma)/(\gamma-1)$, i.e.
$K_{\mathrm{int}}=2$ for $\gamma=1.4$.

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

**Collision time.** In smooth flow $\tau_{\mathrm{col}}=\mu/p$. Where the
reconstruction is discontinuous, an artificial term enlarges it (§3),
$$\tau_{\mathrm{col}}=\frac{\mu}{p}+C\,\Big|\frac{p_l-p_r}{p_l+p_r}\Big|\,\Delta t,\qquad C=1,$$
with $p_l$, $p_r$ the pressures on the two sides of the face, to "enlarge the
kinetic scale physics in the discontinuous region": the shock-capturing
dissipation of the scheme lives in the collision time.

**Inherent bulk viscosity.** The BGK model carries a bulk viscosity
$\mu_b=\frac{2K_{\mathrm{int}}}{3(K_{\mathrm{int}}+3)}\mu$ (Cao et al. 2022,
§3.1, citing Xu), which is $\mu_b=\tfrac{4}{15}\mu$ for a diatomic gas
*(compiler check, not in the sources)*. It enters the dissipation budget
below.

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

## Qualifications

- The version read is the arXiv v1 preprint (May 2020); the journal version
  may differ in text and numbers.
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

# Citations

- [Cao et al. (2022)](/sources/cao-2022.md) — §1 (motivation, finite-volume DNS, competing methods); §2.1, Eqs. (1)–(7) (BGK model, gas-kinetic flux, WENO, S2O4), Remark 1; §2.2 (MPI decomposition); §3 (collision time); §3.1 (Taylor–Green vortex, bulk viscosity, numerical-dissipation decomposition); §3.2, Tables 1–4 (scaling, cost); §3.3, Tables 5–7, Figs. 10–12 (channel); §3.4, Table 8, Figs. 13–15 (compressible isotropic turbulence).
