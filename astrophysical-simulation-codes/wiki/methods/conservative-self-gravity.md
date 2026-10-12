---
type: Method
title: "Conservative self-gravity coupling"
description: "Discretizing the self-gravity momentum and energy sources as exact discrete divergences of a gravitational stress tensor and energy flux, so that total momentum and energy are conserved to round-off: face gravity from potential differences, momentum source from face-averaged gravity, energy source from Riemann mass fluxes times time-averaged face gravity, and the curl-free stress tensor that fixes Athena's anomalous accelerations."
status: established
aliases: [fully conservative self-gravity, gravitational stress tensor, gravity flux, energy-conserving gravity source, curl-free gravity]
tags: [self-gravity, conservation, hydro, time-integration]
timestamp: 2026-10-12T00:00:00Z
---

# Conservative self-gravity coupling

In the usual source-term form,
$$\partial_t(\rho\mathbf v) + \nabla\cdot(\rho\mathbf v\mathbf v + p\mathsf I) = \rho\mathbf g,\qquad \partial_t E + \nabla\cdot[(E+p)\mathbf v] = \rho\mathbf v\cdot\mathbf g,$$
with $\nabla^2\Phi = 4\pi G\rho$ and $\mathbf g = -\nabla\Phi$, a
discretization conserves neither total momentum nor total (fluid plus
gravitational) energy unless the sources are built to
([Mullen et al. (2021)](/sources/mullen-2021.md), §2.1, eqs. 1–7).
Castro, for instance, keeps gravity as the non-conservative sources
$\rho\mathbf g$ and $\rho\mathbf v\cdot\mathbf g$, not as a flux
([Almgren et al. (2010)](/sources/almgren-2010.md), §2, eqs. 2–3).

## Conservative forms

The same equations can be written as conservation laws (Jiang et al.
2013; [Mullen et al. (2021)](/sources/mullen-2021.md), §2.1, eqs. 8–12):
$$\partial_t(\rho\mathbf v) + \nabla\cdot\left(\rho\mathbf v\mathbf v + p\mathsf I + \mathsf T_{\mathbf g}\right) = 0,\qquad \mathsf T_{\mathbf g} = \frac{1}{4\pi G}\left(\nabla\Phi\nabla\Phi - \tfrac12\vert\nabla\Phi\vert^2\mathsf I\right),$$
$$\partial_t\left(E + E_{\mathrm g}\right) + \nabla\cdot\left[(E+p)\mathbf v + \frac{1}{8\pi G}\left(\Phi\nabla\partial_t\Phi - \partial_t\Phi\,\nabla\Phi\right) + \rho\mathbf v\Phi\right] = 0,\qquad E_{\mathrm g} = \tfrac12\rho\Phi .$$
Hanawa (2019) uses instead $E_{\mathrm g} = -\vert\mathbf g\vert^2/(8\pi G)$
with flux $-\frac{\Phi}{4\pi G}\partial_t\mathbf g + \rho\mathbf v\Phi$
(eqs. 13–14, 19). The two volume integrals differ by a surface term that
vanishes for periodic boundaries or mass far from the boundary (eq. 20).

A source-term scheme is fully conservative if and only if, cell by cell,
$\rho\mathbf g$ equals the discrete $-\nabla\cdot\mathsf T_{\mathbf g}$
and $\rho\mathbf v\cdot\mathbf g$ equals the discrete divergence of the
(Hanawa) gravitational energy flux plus
$\partial_t(\vert\mathbf g\vert^2/8\pi G)$ (§2.2, eqs. 23–24).

## The discretization of Mullen et al. (2021)

[Mullen et al. (2021)](/sources/mullen-2021.md) build both identities into
Athena++ on static, uniform Cartesian meshes (§§2.3, 3.1, App. A),
following Mikami et al. (2008), Springel (2010), Katz et al. (2016) and
Hanawa (2019).
* **Face gravity.** With the 7-point Poisson discretization, the
  face-normal gravity is the potential difference,
  $g_{x,i+1/2} = -(\Phi_{i+1} - \Phi_i)/h$ (eqs. 26–30), so the discrete
  Poisson equation says that the sum over directions of the face
  differences of normal gravity, divided by $h$, equals $-4\pi G\rho_i$
  (eq. 30).
* **Momentum.** The source is the cell density times the average of the
  two face values, $(\rho g_x)_i = \rho_i\,\tfrac12(g_{x,i+1/2} + g_{x,i-1/2})$
  (eqs. 43–48). Using the discrete Poisson equation and a discrete
  circulation identity around loops of four cell centres, this is proved
  equal to the discrete divergence of a new stress tensor $\mathsf T_{\mathbf g}$
  whose diagonal entries use products of neighbouring tangential face
  components (eqs. 39–42, App. A). The cell-centred gravity it implies is
  curl-free under central differences (eqs. 49–51).
* **Energy.** Writing $\rho\mathbf v\cdot\mathbf g = -\nabla\cdot(\rho\mathbf v\Phi) - \Phi\,\partial_t\rho$
  and using discrete mass conservation gives (eqs. 52–57)
  $$(\rho\mathbf v\cdot\mathbf g)_i = \tfrac12\left[\hat f^{\rho}_{i+1/2}\,\bar g_{x,i+1/2} + \hat f^{\rho}_{i-1/2}\,\bar g_{x,i-1/2}\right] + (y) + (z),$$
  where $\hat f^{\rho}$ is the mass component of the numerical flux. Two
  conditions are required: the mass flux must be **the same Riemann mass
  flux** used in the continuity equation (Mikami et al. 2008), and the
  face gravity must be the **time average**
  $\bar{\mathbf g} = \tfrac12[\mathbf g(t^n) + \mathbf g(t^{n+1})]$, the only
  choice for which the change of $\vert\mathbf g\vert^2/(8\pi G)$ over the
  step factors exactly (eqs. 58–59).
* **Time integration.** With VL2: half-step hydro, Poisson solve, half-step
  source with the time-averaged face gravity, full-step hydro, second
  Poisson solve, full-step source (eqs. 60–68). This needs **two Poisson
  solves per step**, as before, and requires storing the old potential and
  solving the Poisson equation after the continuity update but before the
  energy source, which §5 calls the largest porting hurdle. RK2 and RK3
  use "effective mass fluxes" of the stage combination and require storing
  previous stages' mass fluxes (App. B, eqs. B19, B33). The paper does not
  state the RK3 solve count.
* **Order.** The source evaluation limits the scheme to second order
  whatever the integrator and reconstruction; RK3 and PPM lower the error
  constant (§§4.2.1, 6).

**Round-off conservation needs a round-off Poisson solution** (§3.2).
FFT solvers deliver it; multigrid residuals break it. Only the gravity at
the initial and final stages enters the final energy source, so
intermediate-stage potentials may carry residuals without breaking energy
conservation. For momentum, a residual leaves a net self-force; a uniform
corrective acceleration, the residual density weighted by $\mathbf g$
over the total mass, restores zero net force without adding stress or
tides (eqs. 69–71).

## The non-curl-free stress tensor of Athena

[Mullen et al. (2021)](/sources/mullen-2021.md) (§§2.3.1, 3.3, 5) show
that the stress-tensor discretization of Athena and Athena++ v19.0, which
squares a four-point average of the tangential face gravity in its
diagonal entries, is second-order accurate but does not give a curl-free
gravity. Near a massive body with a light atmosphere it produces
anomalous accelerations that grow as the atmosphere mass falls: errors
reach the true gravity when the atmosphere-to-body mass ratio drops to
$\tfrac34$ times the inverse square of the body radius in cells, about
$10^{-2}$ at 10 cells per radius (eqs. 72–79). The new tensor has the
error of the source-term scheme instead.

Athena's own paper states that its fixed-potential gravity source terms
conserve total energy exactly and that its self-gravity conserves total
momentum exactly, with details deferred to Gardiner & Stone (in
preparation) ([Stone et al. (2008)](/sources/stone-2008.md), §§8.3, 9).
This does not conflict with [Mullen et al. (2021)](/sources/mullen-2021.md),
who also find momentum and energy conserved to round-off with the old
tensor; the defect they identify is the curl of $\mathbf g$, not
conservation (§4.3.1).

**Analogy** (§5): $\nabla\times\mathbf g = 0$ is the gravitational
counterpart of $\nabla\cdot\mathbf B = 0$. Constrained transport keeps
$\nabla\cdot\mathbf B$ zero while $\nabla\times\mathbf B$ survives; here
$\nabla\times\mathbf g$ vanishes and $\nabla\cdot\mathbf g = -4\pi G\rho$
survives (see [constrained transport](/methods/constrained-transport.md)).

## Tests

All from [Mullen et al. (2021)](/sources/mullen-2021.md), §4: FFT Poisson
solver, HLLC, VL2 with PLM unless stated, static uniform meshes.
* **Spitzer sheet** advected for one crossing on 16 to 2048 cells: second
  order for both the source-term scheme and the new stress-tensor flux;
  total momentum conserved to about $10^{-15}$ relative (§4.1, Fig. 2).
* **[Jeans wave](/benchmarks/jeans-wave.md), stable** (wavelength half
  the Jeans length, oblique in 3D): strict second order
  for all six combinations of VL2, RK2, RK3 with PLM, PPM (§4.2.1,
  Fig. 3).
* **Jeans instability, unstable** (wavelength 1.5 Jeans lengths):
  kinetic, thermal and gravitational energies change by factors of 20 or
  more of the initial thermal energy, while the total stays within
  $\pm1\times10^{-13}$ relative (§4.2.2, Fig. 4).
* **Polytrope with a light atmosphere** ($\gamma = 2$, atmosphere mass
  $10^{-2}$ of the body, about 10 cells per radius): the old stress tensor
  destroys the atmosphere with a fourfold azimuthal pattern, and its initial
  $(\nabla\times\mathbf g)_z$ reaches about $\pm0.1$; the source-term scheme
  and the new tensor keep the equilibrium and are curl-free to round-off
  (§4.3.1, Figs. 5–6). With white noise added to $\Phi$, only the
  source-term scheme shows no spurious velocities (§4.3.2, Fig. 7).
  Against a non-conservative cell-centred energy source, the conservative
  scheme avoids a steady spurious heating that expands the polytrope and
  lowers its central density by about 30 % after 100 time units of
  body radius over escape speed (§4.3.3, Fig. 8).

## Use with adaptive meshes

The scheme is not implemented with AMR in Athena++; Hanawa (2019) shows
that it extends, and the authors defer it to the multigrid AMR work
([Mullen et al. (2021)](/sources/mullen-2021.md), §6). The
[Athena++ multigrid solver](/methods/multigrid-self-gravity.md) then
adopts the cell-centred momentum source and builds the energy source from
Riemann mass fluxes times face accelerations, which is curl-free; but it
does **not** use the conservative energy scheme, so energy is not
conserved exactly, and neither momentum nor energy is conserved to
round-off because the potential carries a nonzero residual
([Tomida & Stone (2023)](/sources/tomida-2023.md), §3.2.3, eq. 22).
Castro, with subcycled AMR, keeps non-conservative sources, time-centred
by a predictor–corrector with a Poisson re-solve, and adds momentum and
energy "sync sources" from a correction solve after refluxing
([Almgren et al. (2010)](/sources/almgren-2010.md), §§5.1, 6.2.3).

# Citations

1. [Mullen et al. (2021)](/sources/mullen-2021.md), §§2–6, Apps. A–B (arXiv v1).
2. [Tomida & Stone (2023)](/sources/tomida-2023.md), §3.2.3 (arXiv v1).
3. [Almgren et al. (2010)](/sources/almgren-2010.md), §§2, 5.1, 6.2.3 (arXiv v1 numbering).
4. [Stone et al. (2008)](/sources/stone-2008.md), §§8.3, 9.
