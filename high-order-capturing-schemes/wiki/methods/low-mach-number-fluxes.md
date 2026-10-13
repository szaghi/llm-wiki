---
type: Method
title: "Low-Mach-number numerical fluxes"
description: "Why upwind (Godunov-type) fluxes lose accuracy as the Mach number goes to zero — their momentum dissipation scales like 1/Ma against an O(1) physical flux — and the fixes that rescale only the numerical dissipation: Roe flux preconditioning (Miczek et al.) and the Mach-scaled AUSM+-up; both revert to the standard flux for Ma ≥ 1, neither is tested on shocks."
status: established
aliases: [low-Mach preconditioning, flux preconditioning, preconditioned Roe, AUSM+-up, all-speed flux]
tags: [riemann-solver, numerical-flux, low-mach]
timestamp: 2026-10-13T00:00:00Z
---

# Low-Mach-number numerical fluxes

**The accuracy problem.** Nondimensionalized with a reference Mach
number $\mathrm{Ma}_r$, the Euler momentum flux carries the pressure with
a factor $1/\mathrm{Ma}_r^2$. As $\mathrm{Ma}_r \to 0$, the expansion
$p = p_0(t) + \mathrm{Ma}_r^2\,p_2 + \dots$ and $\nabla\cdot\mathbf v = 0$
follow. A correct scheme must therefore meet two requirements: data
prepared with pressure fluctuations of order $\mathrm{Ma}_r^2$ stay
incompressible, and kinetic energy is conserved. Sound waves form a
second class of solutions, with pressure fluctuations linear in
$\mathrm{Ma}_r$ ([Miczek et al. (2015)](/sources/miczek-2015.md), §§2–3).
* Any Godunov-type flux can be written as a central term minus an
  upwinding matrix acting on the jump. Its interface pressure carries
  fluctuations of order $\mathrm{Ma}_r$, driven by the first-order
  velocity jump, so Godunov-type schemes violate the first requirement.
  This holds for the Godunov strategy in general, not just for Roe (§6.2,
  quoting Guillard & Murrone).
* In primitive variables the velocity rows of the Roe upwind matrix
  $\vert A\vert = R\vert\Lambda\vert L$ scale like $1/\mathrm{Ma}_r$, where
  the physical Jacobian is of order 1. The numerical dissipation then
  swamps the flux (§7). On a 40×40 Gresho vortex with unlimited linear
  reconstruction, plain Roe keeps 94.47 %, 74.52 % and 49.24 % of the
  kinetic energy after one revolution at maximum Mach $10^{-1}$,
  $10^{-2}$ and $10^{-3}$ (Table 1). Higher-order reconstruction only
  "slightly" alleviates the problem (§1).

**Fix 1: precondition the dissipation only** ([Miczek et al. (2015)](/sources/miczek-2015.md), §8).
The time derivative and the central flux stay untouched:
$$\hat f_{i+1/2} = \tfrac12\left[f(u^-) + f(u^+) - P_{\mathrm{pc}}^{-1}\,\big\vert P_{\mathrm{pc}}A\big\vert_{\mathrm{Roe}}\,(u^+ - u^-)\right].$$
* The Weiss–Smith preconditioner leaves terms of order $1/\mathrm{Ma}_r^2$
  in the pressure column of the mass and energy rows. These drive
  spurious mass and energy fluxes from pressure differences, which ruins
  hydrostatic equilibrium in stratified flows.
* The new matrix is the identity plus off-diagonal terms. In primitive
  variables $(\rho, \mathbf v, p)$, the density row has
  $n_d\,\rho\,\delta_{\mathrm{pc}}\mathrm{Ma}_r/c$ in the velocity columns.
  The velocity rows have $-n_d\,\delta_{\mathrm{pc}}/(\rho c\,\mathrm{Ma}_r)$
  in the pressure column. The pressure row has
  $n_d\,\rho c\,\delta_{\mathrm{pc}}\mathrm{Ma}_r$ in the velocity columns.
  Here $n_d$ are the components of the face normal (eq. 37). The
  preconditioned dissipation then has the Mach scaling of the physical
  Jacobian.
* $\mu_{\mathrm{pc}} \le 1$, so $\delta_{\mathrm{pc}} = 0$ whenever the
  local $\mathrm{Ma} \ge 1$, and plain Roe is recovered continuously.
* **Results.** With the preconditioned flux the Gresho vortex keeps
  98.70–98.72 % of its kinetic energy independently of the Mach number,
  and tests down to $10^{-10}$ "did not detect any deviation". A
  Kelvin–Helmholtz roll-up at $\mathrm{Ma} = 10^{-2}$ on $128^2$ resembles
  the $1024^2$ runs. An acoustic packet crosses the vortex at the
  unchanged sound speed (§9).
* **Limits.** Stability is not proved, the value of
  $\mathrm{Ma}_{\mathrm{cut}}$ is not given, and there is no shock test.
  The flux change is claimed to combine with any reconstruction and to
  help most at low order. Explicit RK3 needed no step restriction beyond
  the acoustic CFL condition (§§6, 8, 9.1).

**Fix 2: Mach-scaled AUSM+-up** ([Edelmann et al. (2021)](/sources/edelmann-2021.md), §3.2).
The flux splits into a pressure part and an upwinded mass-flux part. Its
pressure-velocity diffusion terms are scaled by
$\mu_{\mathrm{pc}}(2 - \mu_{\mathrm{pc}})$, with the same Mach parameter
$\mu_{\mathrm{pc}} = \min[1, \max(\mathrm{Ma}, \mathrm{Ma}_{\mathrm{cut}})]$.
The SLH code gives the pressure-diffusion term its own cut-off, near
$10^{-1}$ against $\mathrm{Ma}_{\mathrm{cut}} \approx 10^{-13}$, which
avoids instabilities where the inverse factor becomes huge. Setting both
cut-offs to 1 gives the dissipative "basic" variant.

**A caveat from long runs.** Edelmann et al. ran 2D stably stratified
atmospheres for thousands of buoyancy times, with a
[well-balanced](/properties/well-balanced.md) scheme. With the low-Mach
AUSM+-up, perturbations starting at Mach $10^{-13}$ grow exponentially,
and the fluxes of Miczek et al. (2015) and of Li & Gu (2008) grow
similarly at varying rates (no figure is shown for these two). The
dissipative variant stays below $10^{-11}$. The authors attribute the
growth to pressure–velocity decoupling, which is a hypothesis. 1D runs
and runs of a few sound-crossing times do not reveal it
([Edelmann et al. (2021)](/sources/edelmann-2021.md), §5.1, App. A).

**Shocks.** Both fixes switch themselves off for $\mathrm{Ma} \ge 1$ by
construction, so they leave shock capturing to the standard flux; neither
source tests a shock. A shock-instability cure can need the opposite
switch: Simon & Mandal remove the extra dissipation of their HLLC cure
for $\mathrm{Ma} \le 0.3$ to protect boundary layers
([Simon & Mandal (2019)](/sources/simon-2019.md), §9.9;
[cures for numerical shock instability](/methods/shock-instability-cures.md)).
On the [Riemann-solver page](/methods/approximate-riemann-solvers.md), the
same split into central part and dissipation frames the Lax–Friedrichs
flux.

**Later uses (batch 11).** An isolated contact,
$(\rho, v_x, p) = (1.4, 0.1, 1)$ for $x \le 0.5$ and $(1, 0.1, 1)$
otherwise on $[0, 1]$ with 100 cells, is run at $\mathrm{Ma} = 0.1$ to
$t = 2$ and again at $\mathrm{Ma} = 10^{-5}$ (velocity and end time not
printed). At $\mathrm{Ma} = 10^{-5}$ HLL smears the contact completely,
"consistently with previous reports" (the authors cite Guillard &
Viozat, Thornber et al. and Rieper), and HLL-BVD keeps it sharp ([Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md),
§III A, Fig. 2). This is not a fix of the kind on this page. HLL-BVD
shrinks only the density jump in HLL's state-difference dissipation and
leaves the momentum dissipation analysed above untouched. The paper gives
no low-Mach analysis and no vortex test, so it adds one more report of
an upwind flux failing at low Mach, on a density-only (contact) mode.

# Citations

1. [Miczek et al. (2015)](/sources/miczek-2015.md), §§1–3, 6–9, Table 1.
2. [Edelmann et al. (2021)](/sources/edelmann-2021.md), §§3.2, 5.1, App. A.
3. [Simon & Mandal (2019)](/sources/simon-2019.md), §9.9.
4. [Deng, Boivin & Xiao (2019)](/sources/deng-2019-b.md), §III A.
