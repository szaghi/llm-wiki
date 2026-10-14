---
type: Source
title: "Gallo et al. (2021) — Numerical Aspects of Particle-in-Cell Simulations for Plasma-Motion Modeling of Electric Thrusters"
description: "An in-house MATLAB/CUDA particle code for heavy species only (prescribed or Boltzmann electrons) that replaces leapfrog by a fourth-order Runge–Kutta push, bilinear field interpolation by cubic bi-splines of the potential, and adds ray-traced diffuse wall reflection, mass-conserving ionization and GPU list compaction; applied to an SPT-100-like channel and a quasi-1D helicon double-layer thruster."
resource: "doi:10.3390/aerospace8050138"
source_kind: paper
authors: [Gallo G., Isoldi A., Del Gatto D., Savino R., Capozzoli A., Curcio C., Liseno A.]
year: 2021
venue: "Aerospace 8:138"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2021_Crossref_Aerospace_Gallo_Numerical_Aspects_of_Particle-in-Cell_Simulations_for_Plasma.pdf"
tags: [pic, hybrid, numerics, gpu, hall-thruster, helicon, magnetic-nozzle, wall-interaction]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper describes an unnamed in-house 2D particle code for ions and
neutrals, written in MATLAB with GPUArrays and one hand-written CUDA kernel
for field interpolation. Electrons are not solved: in a Hall-thruster
channel $\phi$ and $T_e$ are prescribed, fixed in time and axial only; in a
helicon double-layer thruster the electrons follow an isothermal Boltzmann
relation with a quasi-1D area correction and a nonlinear 1D Poisson solve.
The authors state that the contributions improve tools and add no physics
(§1): a fourth-order Runge–Kutta push instead of leapfrog; cubic bi-spline
interpolation of $\phi$ differentiated analytically instead of bilinear
interpolation of $\mathbf E$; ray-traced wall reflection with diffuse
Maxwellian re-emission; a cell-based ionization step that conserves mass;
and GPU list compaction of active particles. Tests: single-particle
accuracy of RK4 against leapfrog and of spline against bilinear
interpolation; an SPT-100-like channel compared with the hybrid results of
Hofer et al. (2007); a CPU–GPU timing; helicon performance trends with
$T_e$, ionization rate and propellant. Merged into
[PIC-MCC](/methods/pic-mcc.md), [particle pushers](/methods/particle-pushers.md)
and [Monte Carlo collisions](/methods/monte-carlo-collisions.md), among
others listed below.

# Key claims

1. **Scope** (§1, p. 3). "the advancements shown in this paper do not
   concern a better knowledge of the plasma physics, but rather an
   improvement of tools already available in the literature".
2. **Baseline** (§1, attributed to the review of Taccogna et al.). Common
   hybrid codes use finite-difference $\mathbf E$ at nodes, leapfrog and
   bilinear interpolation; most ignore mass conservation in ionization and
   appropriate wall reflection, and all run sequentially.
3. **Stated orders** (§2.1). Leapfrog second order, linear interpolation
   first order, RK4 fourth order, cubic bi-spline "third order"; the spline
   gives a $C^1$ potential and a continuous $\mathbf E$. Not proved.
4. **RK4 is more accurate than leapfrog** (§4.2, Fig. 8a, Table 1; shown).
   Single particle, fixed Hall-case potential, cubic bi-spline field,
   $\Delta x=4.16\times10^{-4}$ m, $\Delta t\in\{2.5,5,10\}\times10^{-8}$ s,
   final-velocity error against a Richardson-extrapolated reference: RK4
   from $2.45\times10^{-2}$ to $1.9\times10^{-3}$, leapfrog from
   $1.64\times10^{-1}$ to $6.31\times10^{-2}$ (text).
5. **Spline interpolation** (§4.2, Figs. 8b, 9; shown). Equal accuracy on a
   smooth field; on a discontinuous concentric-capacitor field (100 V and
   0 V plates, radii 3.5 and 1.5 m, 2 × 1 m box, 100 × 50 nodes, 5 ions)
   bilinear interpolation accelerates particles outside the capacitor, the
   spline does not.
6. **Mass-conserving ionization** (§2.4, Fig. 7b; shown). Neutral plus ion
   mass flow stays at about $5\times10^{-6}$ kg/s along the channel,
   unlike Parra et al. (ref. 26), which the paper says does not conserve mass.
7. **GPU timing** (§4.3, Table 2; shown). Hall case: 55.75 min on the GPU
   against 101.2 min on a multicore CPU, a 44.91 % saving; a fully
   sequential loop version "required 1.5 h to perform a single timestep".
8. **Priority** (§2.6, citing the review of Kahnfeld et al. 2019): "the
   approach presented here is the very first one to exploit GPU computing
   for a PIC application in plasma thrusters". Stated, not established by
   the paper beyond the citation.
9. **Helicon double-layer trends** (§4.4, §5, Figs. 10–12, Table 3; shown
   with the reduced model, no experiment). $T_e$ from 5 to 20 eV at
   $10^{18}$ s$^{-1}$ ionization rate: potential drop 6 to 23 V, $I_{sp}$
   460 to 977 s; ionization rate $10^{17}$–$10^{19}$ s$^{-1}$ leaves the
   potential unchanged and thrust grows linearly; at equal ion mass flow
   ($6.5\times10^{-8}$ kg/s) iodine gives $I_{sp}$ 352 s and 0.22 mN against
   argon's 698 s and 0.45 mN.

# Models and numerics

* **Species.** Ions and neutrals as macroparticles; ions pushed by
  $\mathbf E$ only (no magnetic force on ions); neutrals ballistic (§2).
* **Electrons.** Hall case: prescribed axial $\phi(x)$ (about 305 V at the
  anode to about 75 V at 0.025 m) and $T_e(x)$ (peak about 25 eV near
  0.024 m), read from Fig. 5, provenance not stated. Helicon case:
  Boltzmann electrons, $n_e=n_0e^{e\phi/T_e}$ with the duct-area factor
  $r_{ch}^2/r^2(x)$ (Chen), nonlinear Poisson (Eq. 15) with $\phi=0$ at both
  ends (Eq. 16), solved by a scheme citing Newton–Kantorovich papers;
  $n_0$ from a global electron balance (Eqs. 17–18).
* **Geometry.** Hall case: 2D Cartesian axial–radial box
  0.025 × 0.015 m, 34 × 22 nodes, channel only. Helicon case: quasi-1D
  along the outermost field line, 0–0.6 m, 2000 nodes.
* **Ionization** (§2.4). Electron impact only, single charge, Drawin rate
  coefficient $\zeta(T_e)$; ionized mass per cell per step capped at the
  cell's neutral mass, removed equally from its neutral macroparticles;
  40 new ion macroparticles per step (per cell or per domain not stated).
  No elastic or charge-exchange collisions; DSMC and standard MCC judged not
  applicable.
* **Moments.** Mass per cell over cell volume; "weighting functions have
  been dismissed" (nearest-cell deposition).
* **Boundaries** (§2.2–2.3). Inlet: 20 neutral macroparticles per step,
  weight from the mass flow, Maxwellian velocities (Eq. 5). Walls:
  ray-traced reflection checked at each RK4 sub-step, diffuse re-emission
  at $T_w$; an ion hitting a wall becomes a neutral. Outlet: deletion. No
  sheath, SEE or cathode model.
* **Numerical parameters.** Hall: $\Delta t=5\times10^{-8}$ s to
  $5\times10^{-4}$ s, inlet $5\times10^{-6}$ kg/s, $T_w=850$ K, inlet
  750 K; about 100,000 particles. Helicon: $\Delta t=10^{-7}$ s, steady
  state at about $10^{-3}$ s, about 150,000 macroparticles. Mesh and time
  step copied from the reference work; no $\lambda_D$ or $\omega_{pe}$
  constraint applies (no electron particles); no scaling, no subcycling.
* **Code.** MATLAB GPUArrays; the interpolation routine is a CUDA
  `__global__` kernel; ion and neutral lists sorted each step to cluster
  active particles and avoid thread divergence (§2.6, Fig. 3). One GPU, no
  MPI; hardware not stated.

# Tests and results

| Test | Set-up | Result |
|---|---|---|
| Hall channel (§4.1, Figs. 5–7) | SPT-100-like, against Hofer et al. (2007), propellant not stated | neutral density about $8.9\times10^{19}$ m$^{-3}$ at the anode, ion peak about $10^{18}$ m$^{-3}$ near 0.015 m (colour scales); radially averaged profiles in "good agreement", ion peak slightly narrower; no thrust or $I_{sp}$ |
| RK4 vs leapfrog (§4.2, Fig. 8a) | see Key claim 4 | plotted errors about 0.03 / 0.09 / 0.22 (leapfrog) and 0.001 / 0.003 / 0.025 (RK4) at the three $\Delta t$ (read from the figure) |
| Spline vs bilinear (§4.2, Figs. 8b, 9) | $\Delta x\in\{8.3,4.16,2.08\}\times10^{-4}$ m, $\Delta t=5\times10^{-8}$ s; capacitor test | errors nearly coincide (about 7 → 0.45 → 0.03, units not stated); spline removes spurious acceleration |
| CPU vs GPU (§4.3, Table 2) | Hall case | total 101.2 / 55.75 min (44.91 %); RK4 43.65 / 23.18 (46.89 %); spline 40.22 / 19.80 (50.77 %); neutral motion 7.31 / 3.45 (52.80 %) |
| Helicon base case (§4.4, Fig. 10) | Ar, 10 eV, $3\times10^{16}$ ions/s | potential drop 12 V near the chamber exit, $n_e$ about 3–8 × 10¹⁴ m⁻³, exit Mach number about −1.2, $I_{sp}=662$ s, thrust 0.0126 mN, about 10 min run |

# Notation map

| Gallo et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $x$ (axial), $y$ (radial) | $x$, $y$ with $x\to z$, $y\to r$ | Cartesian, no axisymmetric metric |
| $\mathbf u_{i,n}$, $u$, $v$ | $\mathbf v_p$ and its components | **collision:** registry $\mathbf u_s$ is a mean velocity |
| $\mathbf a_i$ | $(q_i/m_i)\mathbf E$ | |
| $\phi$, $\Phi$ | $\phi$ | |
| $q$ (Eqs. 9–15) | $e$ | the text calls it "the electron charge"; Eq. 13 needs $q=+e$ |
| $\dot n_i$ | words (volumetric ionization rate) | a source, not a time derivative |
| $\zeta(T_e)$ | $k_{\mathrm{ion}}(T_e)$ | units printed "m³/s⁻¹" |
| $k_bT_e$, $T_e$ in eV | $T_e$ | unit slip |
| $T_w$ | words (wall temperature) | |
| $v_{mp}=\sqrt{2k_bT/m}$ | $v_{th,s}$ with the $\sqrt2$ convention | |
| $v_e$ | words (electron thermal speed) | printed definition suspect, see below |
| $\theta$ (emission angle) | words | **collision:** azimuthal $\theta$ |
| $SR$ | words (total ionization rate, s⁻¹) | |
| $g$ | $g_0$ | |
| $\Delta\Phi$ | words (potential drop) | |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Boltzmann-relation electrons](/methods/boltzmann-electron-model.md)
* [Breathing mode](/definitions/breathing-mode.md)
* [Current-free double layer](/definitions/current-free-double-layer.md)
* [Direct simulation Monte Carlo (DSMC)](/methods/dsmc.md)
* [Gas–surface interaction models](/methods/gas-surface-interaction.md)
* [GPU acceleration of particle codes](/methods/gpu-acceleration-of-pic.md)
* [Hall-effect thruster](/definitions/hall-effect-thruster.md)
* [Helicon plasma thruster](/definitions/helicon-plasma-thruster.md)
* [Hybrid PIC–fluid models](/methods/hybrid-pic-fluid-model.md)
* [Magnetic nozzle](/definitions/magnetic-nozzle.md)
* [Monte Carlo collisions and the null-collision method](/methods/monte-carlo-collisions.md)
* [Particle pushers: leapfrog, Boris and Runge–Kutta](/methods/particle-pushers.md)
* [Particle-in-cell with Monte Carlo collisions (PIC-MCC)](/methods/pic-mcc.md)
* [SPT-100 as a validation case](/benchmarks/spt-100.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2021_Crossref_Aerospace_Gallo_Numerical_Aspects_of_Particle-in-Cell_Simulations_for_Plasma.pdf`.
   * **Version.** Final published MDPI version (headers "Aerospace 2021, 8,
     138", pp. 1–22), open access CC BY 4.0.
   * **Identity.** doi:10.3390/aerospace8050138, printed on page 1 and
     checked on Crossref (title, journal, all seven authors): Aerospace 8(5),
     article 138; published online and in print 2021-05-15.
   * **How it was read.** In full; equations read from rendered pages 5, 7,
     10 and 11, none unreadable. Figure values are approximate visual
     readings.
   * **Recorded as printed.**
     - Eqs. 3–4 are not classical RK4: each velocity increment adds the
       start-of-step acceleration to the stage acceleration, and stages
       are evaluated at full rather than half increments; as printed the
       velocity update is not first-order consistent. Read as a typesetting
       slip. The text below Eq. 2 says "particle position and position".
     - Slopes read from Fig. 8a give observed orders of about 2.3 (RK4) and
       1.4 (leapfrog), below the stated 4 and 2; Fig. 8b gives about 3.9
       for both interpolations, against the stated first and third order.
       Reader's readings; the paper comments on neither.
     - The §4.2 error values do not match Fig. 8a at the leapfrog end
       points, and "for the linear interpolation" should read "for the
       leapfrog".
     - $\Delta x=4.16\times10^{-4}$ m is called the reference mesh, but
       0.025 m over 33 intervals is $7.6\times10^{-4}$ m.
     - The Fig. 7a legend reads "Ref.[28]" (Carlsson et al.); caption and
       text compare with [37] (Hofer et al. 2007).
     - "Fully conserved" mass flow: Fig. 7b fluctuates between about 4.8 and
       5.2 × 10⁻⁶ kg/s.
     - Boltzmann derivation signs: Eq. 9 needs $q>0$, the text calls $q$ the
       electron charge, Eqs. 10–12 are sign-inconsistent; Eq. 13 is the
       correct relation for $q=+e$.
     - $k_bT_e$ with $T_e$ in eV; units of $\zeta$ printed "m³/s⁻¹".
     - $v_e=\sqrt{eT_e/(8\pi m_e)}$ (p. 11) is a factor 8 below the mean
       speed $\sqrt{8eT_e/(\pi m_e)}$.
     - Cross-references: "Equation (16)" for Eq. 15 (p. 11), "Equation (7)"
       for Eq. 6 (§3); Eq. 8 printed $\frac{d\phi}{dx}^2$; "$q_i/m_i$ is the
       mass to charge ratio".
     - Table 2 caption names three versions, the table has two; §4.3 calls
       the speed-up "around 2" against sequential runs, the table gives
       1.82 overall against the multicore CPU; §5 claims the gain against
       "sequential or multi-core" options.
     - Argon at 10 eV: $I_{sp}$ 662 s (Fig. 10) against 698 s (Table 3),
       unexplained; computed $I_{sp}$ about 10–15 % below the
       $\sqrt{2e\Delta\phi/m_i}/g_0$ value it is said to "well approximate".
     - Iodine called four times heavier than argon; 126.90/39.95 = 3.18
       (atomic I).
     - §1 calls electromagnetic PIC suitable for Hall thrusters, citing
       electrostatic/quasi-neutral hybrid works.
     - The GPU priority claim (Key claim 8) rests on one review;
       [Taccogna et al. (2023)](/sources/taccogna-2023.md) (§V B) report
       that the CUDA code ECCOPIC2S-M ran the 2019 axial–azimuthal
       Hall-thruster benchmark, and
       [Marks & Gorodetsky (2025)](/sources/marks-2025.md) (Results) that
       one GPU code took part in it.
   * **Reference list:** 48 printed entries (Crossref 48). Ref. 4 (NASA web
     feature) keyed `nasa-2021`; ref. 11 printed as "Nat. Cell Biol.
     562:185", kept as printed; ref. 34 prints duplicated author names.
