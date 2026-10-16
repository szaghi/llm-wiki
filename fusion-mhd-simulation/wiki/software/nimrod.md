---
type: Software
title: "NIMROD"
description: "Initial-value extended-MHD code with high-order C0 nodal spectral elements in the poloidal plane and a toroidal Fourier series, a mixed implicit/semi-implicit leapfrog time advance, diffusive divergence cleaning and a thin resistive wall with a meshed vacuum; benchmarked on NSTX VDEs and impurity gas injection, and extended with a plasma–neutral model whose atomic sources are coupled by Crank–Nicolson/JFNK or Strang splitting."
status: established
aliases: [NIMROD code]
tags: [code, mhd, full-mhd, extended-mhd, finite-elements, spectral, time-integration, neutrals, wall, vde, benchmark]
timestamp: 2026-10-16T00:00:00Z
---

# NIMROD

NIMROD is an initial-value extended-MHD code
([Taheri et al. (2022)](/sources/taheri-2022.md), §2). Its generalized Ohm's
law includes Hall, neoclassical and electron-pressure terms, which the cited
plasma–neutral study does not use (§2). It is one of the three codes of the
[NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md)
([Artola et al. (2021)](/sources/artola-2021.md)).

## Physics models

* **Full MHD** evolving the components of $\mathbf B$ and $\mathbf v$
  (non-reduced). In the VDE benchmark the equations are equivalent to JOREK's
  base set with three differences: Faraday's law replaces the vector-potential
  equation, particle diffusivity is isotropic, and a temperature equation
  replaces the pressure equation. Resistivity is evaluated from the
  toroidally symmetric part of $T$ (Artola et al. 2021, §2).
* **Plasma–neutral model** (Meier–Shumlak): one hydrogenic ion species and a
  neutral fluid with separate continuity, momentum and temperature equations,
  coupled by electron-impact ionization, radiative recombination and resonant
  charge exchange with DEGAS2 rates; resistive MHD only in that study (Taheri
  et al. 2022, §2, Eqs. 1–18). See
  [fluid neutral models](/methods/fluid-neutral-models.md).
* **Impurities**: charge-state-resolved models with KPRAD-fitted ADPAK data in
  the Lyons et al. (2019) gas-injection benchmark
  ([Hu et al. (2021b)](/sources/hu-2021-b.md), §2.2, §6;
  [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.7).
* **Neoclassical tearing**: a heuristic closure (Gianakon et al. 2002, cited
  by [Saxena et al. (2025)](/sources/saxena-2025.md), §1).
* **Runaway electrons**: an RE fluid–MHD model (Sainterme & Sovinec 2024,
  cited by [Bandaru et al. (2024)](/sources/bandaru-2024.md), §I, without
  comparison).

## Discretization

* 2D high-order $C^0$ nodal spectral elements in the poloidal plane
  (quadrilateral, degree 3 with Legendre-spaced nodes in the VDE benchmark;
  bi-quintic in the neutral study) and a toroidal Fourier series (Artola et
  al. 2021, Table 1; Taheri et al. 2022, §2).
* $\nabla\cdot\mathbf B$ is not identically zero; it is controlled by a
  diffusive correction proportional to $\nabla(\nabla\cdot\mathbf B)$ added to
  Faraday's law (Artola et al. 2021, §2). See
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md).
* A stabilization method suppresses numerical interchange (Artola et al. 2021,
  §2).

## Time integration and solvers

* **Implicit leapfrog** ([semi-implicit leapfrog](/methods/semi-implicit-leapfrog.md)).
  $\mathbf V$ is staggered against $(n,T,\mathbf B)$, which are solved one after
  another in dependency order: velocity, density, temperature, field. A
  semi-implicit operator, the ideal-MHD force operator plus a small isotropic
  Laplacian, stabilizes wave propagation in the velocity advance, and
  advection is centred with $\theta_{\mathrm t}=1/2$ (Taheri et al. 2022, §3,
  App. A, Eqs. 37–45).
* The leapfrog "takes smaller but cheaper steps than fully consistent implicit
  methods"; $\Delta t$ is adapted to the flow CFL because the staggering loses
  accuracy beyond it. In the most dynamic part of the 3D VDE
  $\Delta t>0.015\,\tau_A$, "hundreds of times larger than an explicit
  stability limit" (Artola et al. 2021, §2, §3).
* Linear systems are solved with GMRES; in 1D runs periodic matrix
  refactorization makes GMRES counts a poor cost proxy (Taheri et al. 2022,
  §3.2, §5.1.1).
* **Atomic sources in the leapfrog** (Taheri et al. 2022; see
  [operator splitting of atomic sources](/methods/operator-splitting-of-atomic-sources.md)):
  Crank–Nicolson centring of the linearized sources (CN-linear), plus an
  approximate Jacobian-free Newton–Krylov iteration on the nonlinear
  remainder (CN-JFNK), per-field Strang splitting with an lsode ODE solve
  (SS-field), or Strang splitting interleaved into the leapfrog with a
  Douglas–Rachford-inspired coupling source (SS-leapfrog+DR). The paper gives
  no formal stability analysis; stability is taken from the semi-implicit
  operator literature (§3, §6).

## Walls

A thin resistive wall interfaces with a meshed external vacuum that uses the
same magnetic representation as the plasma (Artola et al. 2021, §2, Table 1).
[Isernia et al. (2023)](/sources/isernia-2023.md) (§I) list NIMROD among the
codes coupled only to axisymmetric thin walls. See
[resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Verification and benchmarks

* **NSTX 3D VDE** (39 000 bicubic quadrilaterals inside the wall,
  $n\in[0,10]$, the most dynamic interval rerun with $n\in[0,21]$): kink onset
  0.85–1.10 ms after limiting as in the other codes, thermal quench 0.20 ms,
  peak vertical force about 29 kN, peak sideways force about 2.5 kN (figure
  reading), no force rotation, and a 3–4 % toroidal asymmetry of $I_p$, the
  largest of the three codes (Artola et al. 2021, §3, §4.1, Figs. 8, 10). To
  avoid overshoot in the $n$ expansion, $\nu_\parallel$ was raised to
  $100\,\nu_\perp$ 1.08 ms into the 3D phase (Table 2). Hoelzl et al. (2021)
  (§4.8) summarize the same benchmark with NIMROD's horizontal force "factor 2
  smaller" (see Contradictions).
* **Axisymmetric NSTX VDE**: "excellent agreement" with JOREK and M3D-C1 on
  growth rate, axis motion, currents and halo structure (Hoelzl et al. 2021,
  §4.8).
* **[DIII-D gas-injection impurity benchmark](/benchmarks/diii-d-mgi-impurity-benchmark.md)**:
  JOREK's collisional-radiative model agrees with NIMROD in integrated
  cooling and Ohmic power; at constant $\eta=10^{-5}\,\Omega$ m the JOREK argon
  peak is 0.15 ms later, and for neon NIMROD plateaus where JOREK drops, which
  Hu et al. (2021b) attribute to atomic data (§6, App. A). JOREK's earlier
  coronal model collapsed about 2× slower than M3D-C1 and NIMROD (Hoelzl et
  al. 2021, §2.7).
* **Linear $n=1$ fishbone**: M3D-C1-K agrees with NIMROD and M3D-K except for
  the real frequency at large energetic-particle fraction
  ([Liu et al. (2022)](/sources/liu-2022.md), §6.1).
* **Plasma–neutral schemes** (Taheri et al. 2022, §4–5): on a 1D
  neutral-penetration case into a fixed pedestal (40×4 bi-quintic elements),
  SS-field shows a $\Delta t$-dependent steady state with errors near
  $10^{-2}$, while CN-JFNK and SS-leapfrog+DR reach $10^{-8}$–$10^{-6}$;
  CN-JFNK costs about 3× SS-field and SS-field about 1.1× SS-leapfrog+DR in
  wall-clock time. On a 1D snowplow case all methods share a large-$\Delta t$
  error, and SS-field degrades at small $\Delta t$ (Figs. 7, 11). CN-linear is
  "not robust for all 1D test cases" (§5).

## Limitations

* NIMROD post-processing for open/closed field-line separation and $q_{95}$
  was "not yet developed for VDEs", so its halo current is absent from the
  VDE comparison (Artola et al. 2021, §4.1).
* The second-order claim for SS-leapfrog+DR is asserted without derivation,
  and the printed coupling-source formula (Eq. 34) is identically zero as
  typeset (Taheri et al. 2022, §3.4; recorded on the Source page).
* Stellarator capability was "still in the process of being extended" in 2022
  ([Nikulsin et al. (2022)](/sources/nikulsin-2022.md), §I); a stellarator
  variant, NIMSTELL, is cited by Saxena et al. (2025) (§1).

## Contradictions

* **Sideways wall force in the 3D NSTX VDE benchmark.** *Open.*
  Artola et al. (2021) (§4.1.4, §5, Fig. 8) report "good agreement in
  magnitude" with predicted peaks of 2.5–3.5 kN (figure readings: JOREK about
  3.4, M3D-C1 about 2.8, NIMROD about 2.5 kN); Hoelzl et al. (2021) (§4.8)
  summarize the same benchmark as the horizontal force being "factor 2
  smaller in NIMROD". The peak values read from Fig. 8 do not show a factor 2,
  so the published version of the benchmark figure, or the quantity Hoelzl et
  al. compared (peak or time-resolved), would settle it. Recorded in full on
  the [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md) and
  [wall forces](/definitions/wall-forces.md).

# Citations

1. [Artola et al. (2021)](/sources/artola-2021.md) — §2, Tables 1–2, §§3–5, Figs. 8, 10.
2. [Taheri et al. (2022)](/sources/taheri-2022.md) — §§2–6, App. A.
3. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.7, §4.8.
4. [Hu et al. (2021b)](/sources/hu-2021-b.md) — §§2.2, 6, App. A.
5. [Liu et al. (2022)](/sources/liu-2022.md) — §6.1.
6. [Isernia et al. (2023)](/sources/isernia-2023.md) — §I.
7. [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) — §I.
8. [Saxena et al. (2025)](/sources/saxena-2025.md) — §1.
9. [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §I.
