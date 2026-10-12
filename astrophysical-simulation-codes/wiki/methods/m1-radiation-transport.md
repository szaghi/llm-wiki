---
type: Method
title: "M1 two-moment radiation transport"
description: "Radiation transport by the zeroth and first angular moments of the transfer equation closed with the local M1 Eddington tensor, advanced by explicit Godunov schemes with HLL or global Lax–Friedrichs fluxes and operator-split matter coupling, as implemented in RAMSES-RT and Athena's Hyperion module."
status: established
aliases: [M1 closure, two-moment radiation hydrodynamics, moment method, M1 radiative transfer, Levermore closure]
tags: [radiation, riemann-solver, reduced-speed-of-light, conservation]
timestamp: 2026-10-12T00:00:00Z
---

# M1 two-moment radiation transport

The M1 method evolves the radiation energy (or photon number) density and
its flux as a hyperbolic system and closes it with a local, algebraic
Eddington tensor. Two codes in the bundle use it:
[RAMSES-RT](/software/ramses-rt.md), for multigroup ionizing photons on
RAMSES's cell-based AMR ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md)),
and Hyperion, the gray radiation hydrodynamics module of
[Athena](/software/athena.md) on uniform Cartesian grids
([Skinner & Ostriker (2013)](/sources/skinner-2013.md)).

## Moment equations

**Photon-number form** (RAMSES-RT, §2, eqs. 3–7). For each frequency group
the zeroth and first moments are
$$\partial_t N_{\mathrm{ph}} + \nabla\cdot\mathbf F_{\mathrm{ph}} = (\text{absorption}) + (\text{stellar injection}) + (\text{recombination emission}),\qquad \partial_t\mathbf F_{\mathrm{ph}} + c^2\nabla\cdot\left(\mathsf f_{\mathrm E}N_{\mathrm{ph}}\right) = -(\text{absorption}),$$
where the absorption terms are sums over H I, He I and He II of number
density times $c$ times the group cross section. Group cross sections and
energies are averages over an assumed source spectrum, set by hand or
computed on the fly from spectral tables (eqs. 9–11, App. B). Only
ionizing groups are modelled; radiation pressure on dust is an open item
(§7).

**Gray energy form, mixed frame** (Hyperion, §2.1, eq. 8). Material
coefficients are comoving, other quantities lab-frame; scattering is
neglected and the Planck, energy and flux mean opacities are set equal to
one $\kappa$. The radiation subsystem reads
$$\begin{aligned}
\frac{1}{\hat c}\partial_t E_{\mathrm r} + \nabla\cdot\frac{\mathbf F_{\mathrm r}}{c} &= \rho\kappa\,(\text{emission} - E_{\mathrm r}) + \rho\kappa\frac{\mathbf v}{c}\cdot\frac{\mathbf F_{\mathrm r}}{c},\\
\frac{1}{\hat c}\partial_t\frac{\mathbf F_{\mathrm r}}{c} + \nabla\cdot\mathsf P_{\mathrm r} &= -\rho\kappa\frac{\mathbf F_{\mathrm r}}{c} + \rho\kappa\frac{\mathbf v}{c}\cdot\left(E_{\mathrm r}\mathsf I + \mathsf P_{\mathrm r}\right),
\end{aligned}$$
where "emission" is the thermal term $\propto T^4$. The gas energy
equation receives $-c$ times the first right-hand side and the gas
momentum equation $-1$ times the second. The $\hat c$ in the time
derivatives is the
[reduced speed of light](/definitions/reduced-speed-of-light.md). The
velocity-dependent terms are of order $\vert\mathbf v\vert/c$ times the
optical depth, and they must be kept when that product is of order one or
larger (§2.2, eq. 10). The term
$\rho\kappa\frac{\mathbf v}{c}\cdot(E_{\mathrm r}\mathsf I + \mathsf P_{\mathrm r})$
is simplified to $\frac43E_{\mathrm r}\rho\kappa\frac{\mathbf v}{c}$
(eq. 18). The paper names three regimes (§2.2): **streaming** (optical
depth $\ll1$), **static diffusion** ($\vert\mathbf v\vert/c$ times
optical depth $\ll1$) and **dynamic diffusion** (that product $\gg1$);
the product is the ratio of the diffusion time to the flow time.

## The M1 closure

Both sources use the same closure (Levermore 1984)
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §2, eqs. 12–14;
[Skinner & Ostriker (2013)](/sources/skinner-2013.md), §2.3,
eqs. 11–17):
$$\mathsf P_{\mathrm r} = \mathsf f_{\mathrm E}E_{\mathrm r},\qquad \mathsf f_{\mathrm E} = \frac{1-\chi_{\mathrm E}}{2}\mathsf I + \frac{3\chi_{\mathrm E}-1}{2}\hat{\mathbf n}\hat{\mathbf n},\qquad \chi_{\mathrm E} = \frac{3+4f_{\mathrm r}^2}{5+2\sqrt{4-3f_{\mathrm r}^2}},\qquad f_{\mathrm r} = \frac{\vert\mathbf F_{\mathrm r}\vert}{cE_{\mathrm r}},\qquad \hat{\mathbf n} = \frac{\mathbf F_{\mathrm r}}{\vert\mathbf F_{\mathrm r}\vert}.$$
RAMSES-RT applies it per group to $N_{\mathrm{ph}}$ and $\mathbf F_{\mathrm{ph}}$.

**Properties (stated).**
* The reduced flux must satisfy $0\le f_{\mathrm r}\le1$, and
  $\chi_{\mathrm E}$ then lies in $[1/3, 1]$. The closure is exact in the
  diffusion limit ($\mathsf f_{\mathrm E}\to\frac13\mathsf I$) and the
  streaming limit ($\mathsf f_{\mathrm E}\to\hat{\mathbf n}\hat{\mathbf n}$),
  and satisfies Levermore's flux-limiting conditions
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §2.3, eq. 13).
* Being local, it makes the system hyperbolic with wave speeds no larger
  than $c$ (Dubroca & Feugeas 1999;
  [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §1.1.2). The system
  is hyperbolic but not strictly so: the $4\times4$ Jacobian has at most
  three independent eigenvectors
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.3).
* Beams are kept with $f_{\mathrm r} = 1$, $\chi_{\mathrm E} = 1$, which
  allows shadows ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §2).

**Failures (stated).** Opposing beams cannot cross; they merge and create
a spurious source perpendicular to them
([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3.2, Fig. 1). The
closure also has a two-beam instability (Frank et al. 2012) and fails when
distributed sources interact in an optically thin region, "as we have
verified" ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §2.3).
Hyperion can swap M1 for a variable Eddington tensor estimate such as
short characteristics (§§2.3, 5).

## Discretization of the transport

Both codes treat the radiation subsystem $u = (E_{\mathrm r}, \mathbf F_{\mathrm r})$
(or $(N_{\mathrm{ph}}, \mathbf F_{\mathrm{ph}})$) as a conservation law and
use explicit Godunov finite volumes with an
[HLL-type flux](/methods/approximate-riemann-solvers.md).

| | RAMSES-RT | Hyperion |
|---|---|---|
| Order | first order in space and time, no reconstruction (§3.2, §7) | second order: VL (MUSCL–Hancock) predictor–corrector with piecewise-linear reconstruction (§3.3) |
| Flux | HLL with eigenvalues from the table of González et al. (2007), or global Lax–Friedrichs (GLF) | HLL with closed-form eigenvalues (eq. 41) |
| Light speed in transport | $c$ in eq. 24 as printed; the Courant limit uses the reduced value (§§4.1, 6) | $\hat c$ (fluxes $\hat c\mathbf F_{\mathrm r}/c$ and $\hat c c\mathsf P_{\mathrm r}$, eq. 21) |
| Mesh | RAMSES oct-tree AMR | uniform Cartesian, MPI; AMR not discussed |

Sources: [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§3.2, 5, 7;
[Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§3.1, 3.3, 3.4.

**Eigenvalues.** In RAMSES-RT the eigenvalues of the flux Jacobian depend
only on $f_{\mathrm r}$ and the angle between the flux and the interface,
and are read from a table ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md),
§3.2). Hyperion's named contribution is a closed form valid in multiple
dimensions, generalizing Audit et al. (2002)
([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.3, eq. 41):
the eigenvalues are ordered $\lambda^{(1)}\le\lambda^{(2)}\le\lambda^{(3)}$;
as $f_{\mathrm r}\to1$ all three tend to $\hat c$ times the cosine of the
angle between $\hat{\mathbf n}$ and the interface normal, which allows
shadowing; as $f_{\mathrm r}\to0$, $\lambda^{(1)},\lambda^{(3)}\to\mp\hat c/\sqrt3$.
Only $\lambda^{(1)}$ and $\lambda^{(3)}$ enter the HLL flux. HLL is chosen
as robust and "positivity-preserving for one-dimensional problems", at the
cost of extra dissipation (§3.3).

**HLL against GLF.** The GLF flux of RAMSES-RT is HLL with the bounds set
to $\pm c$ (eq. 24):
$$\hat f_{i+1/2} = \frac{\mathbf f(u_i) + \mathbf f(u_{i+1})}{2} - \frac{c}{2}\left(u_{i+1} - u_i\right).$$
In the 2D tests of [Rosdahl et al. (2013)](/sources/rosdahl-2013.md)
(§3.2, Fig. 1) GLF is more diffusive and roughly isotropic around point
sources; HLL keeps axis-aligned beams and shadows but makes isotropic
sources visibly anisotropic; diagonal beams leak with both; the two cost
the same. GLF is the default for cosmological and galactic runs. In the
Iliev et al. dense-clump tests the shadow survives with HLL and erodes
with GLF (§§6.4, 6.8).

## Coupling to matter and time stepping

Both codes split the radiation from the gas, but they place the
light-speed time step differently.

**RAMSES-RT** ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md)).
* Per group and step: injection, then transport, then thermochemistry
  (§3, steps i–iii). The thermochemistry couples photon density and flux,
  thermal energy and three ionization fractions (four plus twice the
  number of groups equations), solved sequentially and quasi-implicitly after Anninos et
  al. (1997). A sub-step is redone at half size when any quantity changes
  by more than 10 %, and the next is doubled when the largest change is
  below 5 %; photons are therefore conserved only "at the 10% level" in
  the thermochemistry, while the transport is photon-conserving (§3.3.1,
  footnote 4).
* "Smoothed RT" starts the thermochemistry from the pre-injection,
  pre-transport state and feeds the transport and injection increments in
  as constant rates; in a cosmological zoom it cut thermochemistry
  subcycles by ×6 and wall time by ×3.5 (§4.4, eqs. 34–37).
* The 3D Courant condition is $\Delta t < h/(3c)$; the tests use
  $\Delta t = 0.8\,h/(3\hat c)$ (eqs. 31, 45). The light-speed step is
  "typically 300 times shorter" than the hydro step at gas speeds of
  about 1000 km/s (§4.1). Implicit transport is rejected because accuracy
  still needs a trial-and-error global step and because it needs iterative
  matrix solves (§4.1).
* Radiation is **not** subcycled inside the hydro step. Each AMR level
  runs injection, hydro, RT transport and thermochemistry over the same
  $\Delta t_l$, the minimum of the hydro and RT steps, which keeps photon
  conservation across levels (§5.2, App. D; see
  [adaptive mesh refinement](/methods/adaptive-mesh-refinement.md)).
  Optional RT subcycling, at the cost of strict photon conservation, is an
  open item (§7).

**Hyperion** ([Skinner & Ostriker (2013)](/sources/skinner-2013.md)).
* The system splits into a non-stiff hyperbolic part with explicit
  sources and a stiff ODE for the gas–radiation energy exchange; transport
  splits further into gas and radiation subsystems. The splitting is
  formally first order in time; Strang splitting was "not found
  particularly advantageous"; splitting gas from radiation breaks strict
  conservation of total energy and momentum (§3.1).
* The gas step uses a radiation-modified effective sound speed in its
  Courant condition; the radiation step is the gas step
  divided by the ratio of $\hat c$ to the maximum gas signal speed, so
  the radiation is subcycled about that many times per gas step; the
  Courant number is "usually 0.4" for VL (eqs. 29–32).
* The energy exchange is integrated locally and implicitly: a weighted implicit–explicit (theta) scheme
  that conserves the gas internal energy plus $(c/\hat c)E_{\mathrm r}$
  reduces to a quartic in the new internal energy, solved by
  Newton–Raphson with bisection fallback and tolerance $10^{-10}$
  (§3.4, eqs. 44–50). The flux absorption term uses the same kind of scheme with
  implicitness weight 0.51 "in most cases" and 1 when stiff (eq. 43).
* The velocity-dependent terms are explicit and assumed never stiff,
  which confines the method to the static diffusion regime (§3.4).
* The gas is advanced with Athena's unsplit VL or CTU integrators (§3.4;
  see [unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md)).

## Accuracy and tests

* RAMSES-RT reports no convergence order or error norm; the tests are
  code-to-code comparisons with the Iliev et al. (2006, 2009) suites and
  analytic ionization-front positions, plus beam transport across AMR
  levels ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§5.3, 6).
* Hyperion converges "nearly second order" on a free-streaming, absorbing
  radiation linear wave in 1D, 2D and 3D, where the source step is exact
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §4.1.2, Fig. 4).
  It keeps a sharp shadow behind a dense cloud, where flux-limited
  diffusion "fails immediately" (§4.1.1). On a sub-critical radiative
  shock the errors are 1.7 % ($\rho$), 6.1 % (gas temperature) and 7.8 %
  (radiation temperature) with the computed M1 eigenvalues, and 0.42 %,
  0.49 % and 0.42 % with eigenvalues fixed at $\mp\hat c/\sqrt3$; the
  authors attribute the difference to the Eddington approximation in the
  reference model (§4.3.5).
* Cost: on a 1D Marshak problem Hyperion's wall time grows linearly with
  the number of cells, while that of Enzo's implicit flux-limited
  diffusion stays about constant (its inexact-Newton iteration count does
  not depend on resolution); the authors expect Enzo to win only above most practical
  resolutions ([Skinner & Ostriker (2013)](/sources/skinner-2013.md),
  §4.2). RAMSES-RT storage for the conserved state grows by a factor
  1.5 × (1 + 4/9 × number of groups), about 3.5 for three groups
  ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §5.2).

# Citations

1. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §§1.1.2, 2, 3–3.3, 4.1, 4.4, 5–5.3, 6, 7, App. D (arXiv v2).
2. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §§2.1–2.3, 3.1–3.4, 4.1–4.3, 5 (arXiv v1).
