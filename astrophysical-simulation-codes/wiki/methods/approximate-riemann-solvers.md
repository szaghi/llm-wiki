---
type: Method
title: "Approximate Riemann solvers"
description: "The interface flux functions of the astrophysical Godunov codes — HLLE/HLL, HLLC, HLLD, Roe, Rusanov/Lax–Friedrichs and the two-shock solver — which code offers which, what the sources recommend and measure, and the positivity fallbacks and carbuncle fixes they wrap around them, including HLL and Lax–Friedrichs fluxes for M1 radiation."
status: established
aliases: [Riemann solver, HLLE, HLL, HLLC, HLLD, Roe solver, Rusanov flux, local Lax-Friedrichs, LLF, global Lax-Friedrichs, GLF, two-shock Riemann solver, H-correction]
tags: [riemann-solver, hydro, mhd, radiation]
timestamp: 2026-10-12T00:00:00Z
---

# Approximate Riemann solvers

A Godunov code computes the numerical flux $\hat f_{i+1/2}$ from the
reconstructed states $u^-_{i+1/2}$ and $u^+_{i+1/2}$ with a Riemann
solver. The codes of this bundle offer:

| Code | Solvers | Source |
|---|---|---|
| [Athena](/software/athena.md) | HLLE, HLLC, HLLD, Roe (HLLE fallback); exact solver for isothermal hydro only | [Stone et al. (2008)](/sources/stone-2008.md), §4.3 |
| [Athena++](/software/athena-plus-plus.md) | HLLE, HLLC, HLLD, Roe (no exact solver); relativistic HLLE, HLLC, HLLD | [Stone et al. (2020)](/sources/stone-2020.md), §3.2.2, §4.2.2 |
| [PLUTO](/software/pluto.md) | Rusanov (LLF), HLL, HLLC, HLLD for MHD and relativistic MHD; Roe for hydro and MHD only | [Mignone et al. (2012)](/sources/mignone-2012.md), §3.1 |
| [Castro](/software/castro.md) | two-shock solver only | [Almgren et al. (2010)](/sources/almgren-2010.md), §5.2 |
| [Enzo](/software/enzo.md) | two-shock (PPM only), HLL, HLLC, HLLD (MHD only); no Roe or LLF | [Bryan et al. (2014)](/sources/bryan-2014.md), §4.1.2 |
| [GAMER](/software/gamer.md) | HLLE, HLLD, Roe | [Zhang et al. (2018)](/sources/zhang-2018.md), §3.2 |
| [RAMSES-RT](/software/ramses-rt.md) (radiation) | HLL, GLF | [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3.2 |
| Hyperion, [Athena](/software/athena.md) module (radiation) | HLL | [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.3 |

Athena mentions LLF and FORCE as possible but does not describe them as
implemented options (Stone et al. 2008, §4.3).

## HLLE / HLL

* **Athena.** HLLE (Einfeldt 1991, eq. 61). The right signal-speed bound
  is the largest of the largest Roe-matrix eigenvalue, the right state's
  $v_x$ plus its signal speed, and zero; the left bound mirrors it with
  the smallest eigenvalue (eqs. 62–63). Positive-definite in 1D
  (Stone et al. 2008, §4.3).
* Athena++ extends HLLE, HLLC and HLLD to a general EOS; relativistic
  HLLE serves hydro and MHD and, through local frame transformations,
  general relativity (Stone et al. 2020, §3.2.2, §4.2.2). Its
  [double Mach reflection](/benchmarks/double-mach-reflection.md) uses
  HLLE because of the carbuncle (§3.4.2), and its hydro Sedov runs use
  HLLE (§3.4.4).
* **Radiation (M1).** RAMSES-RT's HLL flux uses bounds from the extreme
  eigenvalues of the two neighbouring cells, with zero included in the
  maximum and the minimum;
  the eigenvalues depend only on the reduced flux $f_{\mathrm r}$ and the
  angle of $\mathbf F_{\mathrm r}$ to the interface and are tabulated
  from González, Audit & Huynh (2007)
  ([Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3.2, eq. 23).
  Hyperion instead gives the eigenvalues of the multidimensional M1
  system in closed form (eq. 41) and uses only the outer pair; HLL is
  chosen as robust and "positivity-preserving for one-dimensional
  problems", at the price of extra dissipation
  ([Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.3,
  eqs. 37–41). See [M1 radiation transport](/methods/m1-radiation-transport.md).

## HLLC

* Athena uses wave speeds after Batten et al. (1997) and calls HLLC
  "highly recommended" for adiabatic hydrodynamics (Stone et al. 2008,
  §4.3).
* On the hydro [linear waves](/benchmarks/linear-wave-convergence.md),
  HLLC and Roe errors are nearly identical and second order; HLLE errors
  are slightly larger, with a slightly lower rate (Stone et al. 2008,
  §8.1, Fig. 7).
* Relativistic HLLC (Mignone & Bodo 2005) is available for special
  relativistic hydro in Athena++ (Stone et al. 2020, §4.2.2).

## HLLD

* HLLD (Miyoshi & Kusano 2005) is as accurate as Roe and "much faster",
  "the best choice for many MHD applications" (Stone et al. 2008, §4.3).
  On MHD linear waves Roe and HLLD are nearly identical and second order
  (§8.2, Fig. 12). On the Ryu–Jones 4d problem HLLD captures the
  switch-on slow rarefaction and slow shock well "even without an
  explicit slow wave" (§8.2, Fig. 15).
* Relativistic HLLD (Mignone et al. 2009) is in Athena++ (Stone et al.
  2020, §4.2.2) and PLUTO (Mignone et al. 2012, §3.1). In Athena++'s
  relativistic magnetized Kelvin–Helmholtz runs the choice between HLLE
  and HLLD shifts the KHI rolls (Stone et al. 2020, §4.3.2, Figs. 38–39).
* Enzo's HLLD serves the MUSCL and MHD-CT solvers (Bryan et al. 2014,
  §4.1.2).

## Roe

* Athena's Roe solver follows Roe (1981), with Cargo & Gallice (1997) for
  MHD and Roe averages in eq. 65 (Stone et al. 2008, §4.3, eqs. 64–68).
* GAMER uses Roe with PLM or PPM for its accuracy tests and for the
  single-GPU benchmark (Zhang et al. 2018, §5.1–5.2).

## Rusanov / Lax–Friedrichs

* PLUTO offers Rusanov (LLF) for MHD and relativistic MHD (Mignone et
  al. 2012, §3.1); its relativistic rotor uses HLL (§6.3).
* RAMSES-RT's global Lax–Friedrichs flux for radiation is HLL with
  bounds $\pm\hat c$ (eq. 24 prints $c$; the transport runs under the
  [reduced speed of light](/definitions/reduced-speed-of-light.md), so the
  bound is $\hat c$). Being first order, it uses cell values as interface
  states:
  $$\hat f_{i+1/2} = \tfrac12\left[\mathbf f(u_i) + \mathbf f(u_{i+1})\right] - \tfrac{\hat c}{2}\left(u_{i+1} - u_i\right)$$
  (Rosdahl et al. 2013, §3.2, eq. 24). GLF is more diffusive and roughly
  isotropic around point sources; HLL keeps axis-aligned beams and
  shadows but makes isotropic sources visibly anisotropic; diagonal beams
  leak about as much with either; both cost the same. GLF is the default
  for cosmological and galactic runs (§3.2, Fig. 1). In the dense-clump
  tests the shadow survives with HLL and erodes with GLF (§6.4; §6.8,
  where GLF loses it after about 40 Myr).

## Two-shock solver

* Castro's only solver is of Colella, Glaz & Ferguson (1997) type, from
  Bell, Colella & Trangenstein (1989). It handles a general convex EOS
  without EOS calls, because it carries the internal energy density
  $\rho e$. The star state is a linearized Rankine–Hugoniot solution with
  Lagrangian sound speeds; sampling uses a shock speed or interpolation
  across a transonic rarefaction. A small quadratic artificial viscosity
  proportional to $\nabla\cdot\mathbf v$ is added, and species fluxes are
  rescaled to sum to the density flux
  ([Almgren et al. (2010)](/sources/almgren-2010.md), §5.2, eqs. 33–35).
* Enzo's two-shock solver is available with PPM only (Bryan et al. 2014,
  §4.1.2).

## Safeguards

* **Positivity fallback.** When Roe gives a negative density or pressure
  in an intermediate state, Athena recomputes that one interface with
  HLLE (or an exact solver); in the Einfeldt 1-2-0-3 rarefaction this was
  needed at one interface in the first step (Stone et al. 2008, §4.3.2,
  §8.1). Enzo's PPM and MUSCL solvers, on a negative density at an
  interface, recompute that cell's fluxes with HLL and redo the update
  (Lemaster & Stone 2009) (Bryan et al. 2014, §4.1.2).
* **Shock-adaptive switch.** PLUTO flags zones where the sum over
  directions of the undivided jumps of thermal or magnetic pressure,
  relative to the smaller neighbour, exceeds a threshold (default 5) and
  where $\nabla\cdot\mathbf v < 0$; flagged zones use HLL and
  their stencil neighbours MinMod reconstruction. It is stated to
  preserve second order and is off in the tests unless stated
  (Mignone et al. 2012, App. B, eq. B1; §3.2).
* **Carbuncle (H-correction).** Athena applies the fix of Sanders et al.
  (1998): in the Roe flux each eigenvalue magnitude is raised to at least
  the maximum, over an "H"-shaped stencil (five points in 2D, nine in
  3D), of half the jump of $v + c_f$ across interfaces (the absolute
  value is assumed: it is not legible in the text layer read); for HLL-type
  solvers the signal-speed bounds are modified instead. It acts only on
  the final multidimensional fluxes (Stone et al. 2008, App. C,
  eqs. C1–C2). Without it the 3D Noh problem shows strong grid-aligned
  perturbations, and below $50^3$ the Roe solver crashes unless the
  Courant number is reduced (§8.5, Fig. 31). Athena++ does not yet
  implement it (Stone et al. 2020, §3.4.2). GAMER tilts its rotated MHD
  blast by 5° to avoid the carbuncle (Quirk 1994) (Zhang et al. 2018,
  §5.1(iv)).
* **M1 eigenvalues in a radiative shock.** In Hyperion's sub-critical
  radiative shock, computed M1 eigenvalues give relative errors of 1.7 %
  ($\rho$), 6.1 % (gas temperature) and 7.8 % (radiation temperature);
  fixing them at $\mp\hat c/\sqrt3$ gives 0.42 %, 0.49 % and 0.42 %. The
  authors attribute the gap to the Eddington approximation in the
  reference model (Skinner & Ostriker 2013, §4.3.5).

## Cost

Athena, C version, 3D, $128^3$, gcc -O3 on a 2.2 GHz Opteron, in $10^3$
cell updates per CPU second (Stone et al. 2008, §7, Table 1):

| Physics | Roe | HLLC | HLLD |
|---|---|---|---|
| Isothermal hydro | 328 | 340 | — |
| Adiabatic hydro | 224 | 242 | — |
| Isothermal MHD | 108 | — | 124 |
| Adiabatic MHD | 85.9 | — | 97.6 |

## Later uses (batch 2)

### Wave speeds for a general equation of state

[Coleman (2020)](/sources/coleman-2020.md) extends the nonrelativistic
solvers of [Athena++](/software/athena-plus-plus.md) to an arbitrary EOS
that supplies only $p(\rho,\rho e)$, $\rho e(\rho,p)$ and $c_s^2(\rho,p)$
(§3.1; see [general equations of state in Godunov codes](/methods/general-equation-of-state.md)).
Replacing every ideal-gas relation by these functions carries the solvers
over, with one exception: the wave-speed estimate (§3.3, App. A).
* **HLLC.** The previous estimate took the extremal speeds from a
  Roe-average state: the left bound is the smaller of the left state's
  $v_x - c_s$ and the Roe state's $v_x - c_s$, the right bound the larger of
  the right state's $v_x + c_s$ and the Roe state's $v_x + c_s$
  (eqs. A6–A7); for a general EOS the Roe-average sound speed needs a
  *fourth* EOS function, the sound speed as a function of density and
  enthalpy (eq. A4). The variant of Hu et al. (2009) also needs four. The
  new default is a generalized primitive-variable Riemann solver (PVRS)
  estimate (Toro 1999; eqs. A8–A17): a linearized star pressure and
  velocity from the arithmetic means of the two densities and sound
  speeds, star densities on each side, and a shock factor on each side
  equal to 1 when the star pressure does not exceed that side's pressure,
  and otherwise built from the pressure ratio and the first adiabatic index
  of the star state; the left bound is the left state's $v_x$ minus its
  $c_s$ times the left factor, the right bound the right state's $v_x$ plus
  its $c_s$ times the right factor. It needs
  only the three EOS functions. Measured, not proved: "significant
  reduction of errors and improved convergence in tests 3 and 4 … without
  negatively affecting the accuracy of solutions using an ideal gas EOS"
  (§3.3); the Hu et al. variant gives errors comparable to the Roe
  extension and worse than PVRS on those tests. Recorded as printed:
  eq. A11 writes the pressures as $p_{x,R}$, $p_{x,L}$.
* **HLLD.** Keeps the Miyoshi & Kusano (2005) estimate (their eq. 12) "as
  originally used in Athena++"; PVRS "is not readily extendable to MHD"
  (§3.3, §5.2). Rerunning the hydro tests as MHD with $\mathbf B = 0$, HLLD
  matches HLLC except on the double-shock tests 3 and 4, where convergence is
  slightly worse and errors up to 3× larger; HLLC with the HLLD estimate
  reproduces this, so the paper attributes it to the estimator (§5.2). On
  the all-discontinuity MHD Riemann problem (Ryu & Jones 2a states with the
  hydrogen EOS) HLLD converges close to linearly in every variable (§4.2).
* **HLLE.** None of the estimators tried changed the results on tests 1, 2,
  5 and 6, where HLLE errors were "a few tens of per cent worse than HLLC";
  on tests 3 and 4 HLLE "did not converge to the correct solution for any of
  the wavespeed estimators we tried" (§5.1.4), although with the Roe
  estimator it converges on the ideal-gas analogues of those tests
  (footnote 10). "We were unable to find a modification to HLLE that
  enabled it to properly converge to the solutions of tests 3 and 4" (§6).
  This qualifies, and does not contradict, Stone et al.'s statement that
  HLLE is extended to a general EOS: HLLE runs with a general EOS, but it
  fails to converge on general-EOS double shocks.
* **Two-shock lineage.** Colella & Glaz (1985) are credited for general-EOS
  Godunov methods, and CASTRO for a general EOS (§1), consistent with the
  two-shock section above.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §4.3, §7, §8.1–8.2, §8.5, App. C.
2. [Stone et al. (2020)](/sources/stone-2020.md), §3.2.2, §3.4.2, §3.4.4, §4.2.2, §4.3.2.
3. [Mignone et al. (2012)](/sources/mignone-2012.md), §3.1–3.2, §6.3, App. B.
4. [Almgren et al. (2010)](/sources/almgren-2010.md), §5.2 (arXiv v1).
5. [Bryan et al. (2014)](/sources/bryan-2014.md), §4.1.2 (arXiv v1).
6. [Zhang et al. (2018)](/sources/zhang-2018.md), §3.2, §5.1–5.2 (arXiv v4).
7. [Rosdahl et al. (2013)](/sources/rosdahl-2013.md), §3.2, §6.4, §6.8 (arXiv v2).
8. [Skinner & Ostriker (2013)](/sources/skinner-2013.md), §3.3, §4.3.5 (arXiv v1).
9. [Coleman (2020)](/sources/coleman-2020.md), §§1, 3.3, 4.2, 5.1.4, 5.2, 6, App. A (arXiv v3).
