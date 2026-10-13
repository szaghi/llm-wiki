---
type: Method
title: "Approximate Riemann solvers"
description: "The interface flux functions of the astrophysical Godunov codes — HLLE/HLL, HLLC, HLLD, Roe, Rusanov/Lax–Friedrichs and the two-shock solver — which code offers which, what the sources recommend and measure, and the positivity fallbacks and carbuncle fixes they wrap around them, including HLL and Lax–Friedrichs fluxes for M1 radiation."
status: established
aliases: [Riemann solver, HLLE, HLL, HLLC, HLLD, Roe solver, Rusanov flux, local Lax-Friedrichs, LLF, global Lax-Friedrichs, GLF, two-shock Riemann solver, H-correction, FOFC, first-order flux correction, flux-vector splitting]
tags: [riemann-solver, hydro, mhd, radiation, gpu]
timestamp: 2026-10-13T00:00:00Z
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

## Later uses (batch 3)

| Code | Solvers | Source |
|---|---|---|
| [AthenaK](/software/athenak.md) | LLF, HLLE, HLLC, HLLD, Roe; first-order flux correction (FOFC) with LLF | [Stone et al. (2026)](/sources/stone-2026.md), §3 |
| [IDEFIX](/software/idefix.md) | Rusanov (LF), HLL, HLLC (hydro), HLLD (MHD), Roe; HLL with whistler speed for Hall MHD | [Lesur et al. (2023)](/sources/lesur-2023.md), §2.3, §2.5 |
| [Cholla](/software/cholla.md) (MHD) | HLLD only | [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2.3 |
| [gPLUTO](/software/gpluto.md) | HLLD in all runs | [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2, §4.1 |
| [Quokka](/software/quokka.md) | HLLC (hydro), HLL (radiation) | [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1–2.2.2 |
| [GRaM-X](/software/gram-x.md) | HLLE only (general-relativistic MHD) | [Shankar et al. (2023)](/sources/shankar-2023.md), §II C |
| [ADAM](/software/adam.md) (NASTO), [STREAmS](/software/streams.md) | Lax–Friedrichs (Rusanov) flux-vector splitting with WENO, not an interface Riemann solver | [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1; [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.1 |

### Per code

* **AthenaK** offers LLF, HLLE, HLLC, HLLD and Roe
  ([Stone et al. (2026)](/sources/stone-2026.md), §3). Because "the number
  of registers is extremely limited on many GPUs", templating algorithmic
  options such as the Riemann solver "reduces register spillage and can
  greatly improve performance" (§2). MHD runs about two times slower per
  cell than hydro, attributed to the Riemann solver and CT (§5.1,
  Table 2). Choices in its tests: HLLE for the SRMHD shock tube and the
  GR Bondi flow, HLLC for a multiphase supernova run, HLLD for MHD
  turbulence, LLF for a Kelvin–Helmholtz tracer test (§3.1–3.6, §4.1).
* **IDEFIX** lists its solvers from most to least diffusive: Rusanov
  (LF), HLL (Einfeldt et al. 1991), HLLC (Toro et al. 1994; replaced by
  HLLD of Miyoshi & Kusano 2005 in MHD), Roe (Cargo & Gallice 1997),
  selectable at run time ([Lesur et al. (2023)](/sources/lesur-2023.md),
  §2.3). Pressure sits in the momentum flux handled by the Riemann
  solver, unlike PLUTO, which treats the pressure gradient as a source
  term; in curvilinear geometry this adds pressure source terms, so
  PLUTO and IDEFIX results "are expected to differ, even if the same
  algorithm combination is chosen" (§2.3). On MHD linear waves with PLM
  and RK2, Lax–Friedrichs, HLL, HLLD and Roe all converge at second
  order (§4.2, Fig. 7), as in Athena, where the solvers differ by the
  error constant. For the Hall effect the whistler speed is added to the
  HLL fan for the magnetic-field fluxes only, the ideal speeds being kept
  for the other components (Lesur et al. 2014; Marchand et al. 2019);
  HLL is "our only solver compatible with the Hall effect", stated to be
  diffusive but stable (§2.5, §4.3). IDEFIX also offers 2D Riemann
  solvers at cell edges (HLL and HLLD) to build CT electric fields
  (§2.4).
* **Cholla** implements HLLD "exactly as described in Miyoshi & Kusano
  (2005)" and names no other MHD solver
  ([Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2.3). The
  longitudinal field is the face value, not reconstructed; Table 1 maps
  the HLLD magnetic fluxes of each sweep direction onto face-centred
  electric fields for CT (§2.2.3). On the GPU, fusing piecewise-constant
  reconstruction into the Riemann kernel cut total run time by about
  10 %, while fusing characteristic PLM into it slowed the code by about
  10–15 % through higher register use and lower occupancy, an outcome
  that "depends on compiler optimizations" (§2.3.1). The 3D Einfeldt
  strong rarefaction with HLLD shows "no spurious oscillations or
  unphysical negative values" (§3.1.4).
* **gPLUTO** uses HLLD for all runs and prints the generic upwind flux as
  the average of the two physical fluxes minus half a dissipation matrix
  applied to the jump of the conserved states (eq. 8)
  ([Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2, §4.1).
  Direction-dependent kernels, the Riemann solver among them, are
  templated on the sweep direction so that small local arrays stay in
  registers (§3.3, Fig. 3).
* **Quokka** uses HLLC with "primitive variable Riemann solver" wave
  speeds and intermediate states (Toro 2013)
  ([Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1), the
  same family as the PVRS estimate Coleman made Athena++'s general-EOS
  default (above). A stationary contact keeps exactly zero error, an
  HLLC property (§3.1.2). In the Einfeldt 1-2-3 rarefaction its specific
  internal energy "compares favourably" with approximate-solver results,
  which Toro (2013) shows with factor 2–3 errors (§3.1.7). For radiation
  it uses HLL with wave speeds from Eddington factors frozen at the start
  of the step (Balsara 1999), so any closure can be plugged in without
  changing the solver, in contrast to the closure-specific M1 eigenvalues
  of RAMSES-RT and Hyperion (§2.2.2; see
  [M1 radiation transport](/methods/m1-radiation-transport.md)).
* **GRaM-X** implements only HLLE; Roe and Marquina are planned because
  "methods which are compute intensive but not memory intensive add
  little extra cost on GPUs" — asserted, not measured
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §II C).
* **Flux-vector splitting.** ADAM/NASTO and STREAmS use the Lax–Friedrichs
  (Rusanov) dissipation as a flux-vector splitting: the positive and
  negative parts of the flux are reconstructed by WENO in a
  finite-difference scheme, instead of a Riemann solver acting on
  reconstructed interface states
  ([Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1;
  [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.1). STREAmS
  splits characteristic fluxes and switches to this flux only where a
  modified Ducros sensor flags shocks, using an energy-preserving central
  flux elsewhere (§2.1).

### First-order flux correction (FOFC)

AthenaK's positivity safeguard is the "first-order flux-correction" of
Lemaster & Stone (2009): in each SSP-RK stage, if density or pressure in
any cell would become negative, the fluxes on all faces of that cell are
recomputed with piecewise-constant reconstruction and the LLF solver,
before the flux corrections at AMR level boundaries
([Stone et al. (2026)](/sources/stone-2026.md), §3). It was applied "once
in every ∼$10^{10}$ cell updates" in Lemaster & Stone's turbulence run;
in AthenaK "it significantly reduces the need for floors" in GRMHD
accretion, and it lets the relativistic cylindrical explosions of
Komissarov (1999) run "robustly" without the floors, background changes
or artificial viscosity other codes need (§3, §3.5, Fig. 10; visual
only). The authors attribute loss of positivity to truncation error,
not round-off (§3). The positivity safeguards on this page differ in scope
and fallback flux (Enzo and AthenaK both cite Lemaster & Stone 2009):
* Athena recomputes one interface with HLLE (or an exact solver) when Roe
  gives a negative intermediate state (above);
* Enzo recomputes the fluxes of the offending cell with HLL and redoes the
  update, citing Lemaster & Stone (2009) (above);
* AthenaK recomputes all faces of the offending cell with first-order
  reconstruction and LLF, inside each RK stage.

### Carbuncle

Quokka acknowledges that its HLLC is subject to the carbuncle and has
not fixed it; the planned fix is an adaptive switch to HLL perpendicular
to strong shocks ([Wibking & Krumholz (2022)](/sources/wibking-2022.md),
§2.2.1), the kind of switch PLUTO already has (shock-adaptive switch,
above). It joins Athena++, which "does not yet implement" the
H-correction (above), among the codes that state an open carbuncle
problem.

## Later uses (batch 4)

| Code | Solvers | Source |
|---|---|---|
| [FLASH](/software/flash.md) | HLL5R (5-wave HLL, Waagan et al. 2011) in the 2021 configuration | [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.1 |
| [TIGRESS](/software/tigress.md) (on Athena) | Roe, H-correction above a 20 km s⁻¹ signal-speed difference, first-order flux correction | [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1 |
| [H-AMR](/software/h-amr.md) | HLL | [Porth et al. (2019)](/sources/porth-2019.md), Table 1 |

AREPO, in an application run, uses an HLLC-type solver on its moving mesh
([Ohlmann et al. (2016)](/sources/ohlmann-2016.md), §2).

### Two-wave solvers in production GRMHD

The nine codes of the
[EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md) split
between HLL (Athena++, Cosmos++, ECHO, [H-AMR](/software/h-amr.md),
IllinoisGRMHD) and LLF (BHAC, HARM-Noble, iharm3D, KORAL); HARM-Noble's
solver is "LLF" in Table 1 and "LF" in §4.1.6
([Porth et al. (2019)](/sources/porth-2019.md), Table 1, §4.1, §6). Table 1
lists no other solver.
The paper cites Flock et al. (2010): with PPM, HLL and LLF resolve linear
MRI growth with 10 cells per mode, against 16 with PLM, so that PPM
"compensates for the large dissipation" of these two solvers (App. A).
Its own PLM runs agree: at fixed second order, PLM runs of H-AMR and
Athena++ give accretion rates "a factor of two to almost six" below their
PPM runs (App. A, Table 3).

### TIGRESS on Athena: H-correction threshold and FOFC

The TIGRESS configuration of [Athena](/software/athena.md) uses the VL
predictor–corrector, PLM and the Roe solver
([Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1). Two safeguards:
* **H-correction** (Sanders et al. 1998) applied only "when the
  difference in signal speed is larger than 20 km s⁻¹", to suppress the
  carbuncle from supernova blast waves — a usage threshold the Athena
  description above does not state.
* **First-order flux correction** (Lemaster & Stone 2009) applied "to
  cells with negative pressure and/or density after the second-order
  update", which strong rarefactions in turbulence can produce. The
  fallback flux and reconstruction are not stated, so this use cannot be
  placed against AthenaK's LLF or Enzo's HLL fallback (above). With it,
  Athena has two positivity safeguards in the sources: the per-interface
  HLLE re-solve of Stone et al. (2008) and this per-cell correction.

## Later uses (batch 6)

### PPM's own Riemann solver

The original [PPM](/methods/ppm.md) paper solves one Riemann problem per
interface for the time-averaged interface pressure and velocity
([Colella & Woodward (1984)](/sources/colella-1984.md), eq. 2.8, p. 185).
Each side contributes one equation in which the wave speed is that side's
Lagrangian shock speed, a function of the unknown interface pressure
through the factor $1 + \frac{\gamma+1}{2\gamma}(\text{pressure ratio} - 1)$;
the same shock-type speed serves both sides whatever the wave, the
structure this page calls two-shock (the paper does not use the term). The
pair is solved by van Leer's Newton iteration "with a fixed number of
iterations"; in smooth flow the equations are a finite-difference
approximation of the characteristic equations. The direct-Eulerian scheme
uses the Cartesian form with the same iteration and takes the state inside
a rarefaction fan by linear interpolation between the states on either
side (p. 191). The iteration count matters: in a first-order Godunov run of
a nearly stationary, extremely strong shock (pressure jump over six
orders), 6 iterations are used, and "if only 2 iterations are performed,
very large errors are generated in the single zone just behind the shock"
(§4, Fig. 8). The Castro entry above cites later work (Colella, Glaz &
Ferguson 1997; Bell, Colella & Trangenstein 1989), not this equation; the
Enzo entry names no origin.

## Later uses (batch 8)

* **The two-shock solver in FLASH's first version.** [Fryxell et al. (2000)](/sources/fryxell-2000.md), §§3.1.6–3.1.7, eqs. 68–91: both waves are treated as shocks ("accurate to third order in the size of the entropy jump"). The star pressure comes from Newton–Raphson, "two to three iterations" for "reasonably strong shocks", and simple linear iteration may need 10 or more. A secant iteration with Colella & Glaz's two adiabatic indices handles a general EOS. Inside a rarefaction the state is linearly interpolated between head and foot. Interface mass fractions are clipped and renormalized (§3.1.8).

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
10. [Stone et al. (2026)](/sources/stone-2026.md), §2, §3, §3.1–3.6, §4.1, §5.1 (arXiv v1).
11. [Lesur et al. (2023)](/sources/lesur-2023.md), §2.3–2.5, §4.2–4.3 (arXiv v1).
12. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §2.2.3, §2.3.1, §3.1.4 (arXiv v2).
13. [Rossazza et al. (2026)](/sources/rossazza-2026.md), §2.2, §3.3, §4.1 (arXiv v1).
14. [Wibking & Krumholz (2022)](/sources/wibking-2022.md), §2.2.1–2.2.2, §3.1.2, §3.1.7 (arXiv v2).
15. [Shankar et al. (2023)](/sources/shankar-2023.md), §II C (arXiv v2).
16. [Zaghi et al. (2023)](/sources/zaghi-2023.md), §3.1.
17. [Bernardini et al. (2021)](/sources/bernardini-2021.md), §2.1.
18. [Porth et al. (2019)](/sources/porth-2019.md), §4.1, §4.1.6, §6, Tables 1, 3, App. A (arXiv v2).
19. [Kim & Ostriker (2017)](/sources/kim-2017.md), §2.1 (arXiv v2).
20. [Mathew & Federrath (2021)](/sources/mathew-2021.md), §2.1 (arXiv v2).
21. [Ohlmann et al. (2016)](/sources/ohlmann-2016.md), §2 (arXiv v1).
22. [Colella & Woodward (1984)](/sources/colella-1984.md), eq. 2.8, pp. 185, 191, §4, Fig. 8.
23. [Fryxell et al. (2000)](/sources/fryxell-2000.md), §§3.1.6–3.1.8.
