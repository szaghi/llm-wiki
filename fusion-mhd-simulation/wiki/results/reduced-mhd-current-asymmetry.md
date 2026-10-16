---
type: Result
title: "Reduced-MHD boundary condition suppresses the toroidal asymmetry of the plasma current"
description: "In ansatz-based reduced MHD the poloidal electric field is a pure potential gradient and the boundary condition on the normal velocity makes the potential constant on the boundary, so the boundary acts as a poloidal ideal conductor, no current crosses it and the plasma current is the same in every poloidal plane; JOREK therefore shows below 0.01% toroidal asymmetry of $I_p$ in a 3D VDE where full-MHD codes find 1-4% and experiments 10-20%."
status: established
aliases: [Ip asymmetry, toroidal plasma current asymmetry, poloidal ideal conductor boundary]
tags: [reduced-mhd, vde, disruption, wall, verification]
timestamp: 2026-10-16T00:00:00Z
---

# Reduced-MHD boundary condition suppresses the toroidal asymmetry of the plasma current

**Statement.** In the ansatz-based [reduced MHD](/methods/reduced-mhd.md)
model of JOREK, with the boundary condition $\mathbf v\cdot\mathbf n=0$ at
the computational boundary, the plasma current is independent of the
toroidal angle, $\partial_\phi I_p=0$, at all times, whatever the 3D MHD
activity ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6;
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8).

## Argument

The chain is given by [Artola et al. (2021)](/sources/artola-2021.md)
(§4.1.6, §4.3.1):

1. With the ansatz $\mathbf B=\nabla\psi\times\nabla\phi+F_0\nabla\phi$ the
   vector potential has only a toroidal component, so the poloidal electric
   field is a pure gradient, $\mathbf E_{\mathrm{pol}}=-\nabla_{\mathrm{pol}}\Phi$.
2. The perpendicular velocity is the $\mathbf E\times\mathbf B$ flow of
   $\Phi$ (the stream function $u$ is $\Phi$ up to the constant factor of the
   page's ansatz), so a vanishing normal velocity at the boundary forces
   $\Phi=$ const along it (JOREK sets $\Phi=0$).
3. The tangential poloidal electric field therefore vanishes on the
   boundary: the boundary behaves as an ideal conductor in the poloidal
   direction. Poloidal surface currents exist there implicitly, and no
   current leaves or enters the plasma domain, $\mathbf J\cdot\mathbf n=0$
   at the wall.
4. With no current crossing the boundary, current continuity between
   poloidal planes gives the same total toroidal current in every plane,
   $\partial_\phi I_p=0$.

In the full-MHD codes M3D-C1 and NIMROD the poloidal electric field at the
boundary is finite, $\mathbf E_{\mathrm{pol}}=\eta\mathbf J_{\mathrm{pol}}$,
so normal current can leave or enter the plasma domain and $I_p$ can vary
toroidally (same section).

## Evidence

In the 3D NSTX hot-VDE benchmark ([NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md)),
$I_p$ evaluated in ten equidistant poloidal planes gives a maximum
asymmetry $\Delta I_p/I_p$ of 3–4% (NIMROD), 1–1.4% (M3D-C1) and below
0.01% (JOREK) ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6,
Fig. 10). [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§4.8) report the
same benchmark as "maximum toroidal asymmetries in the plasma current of
1–4%" in the full-MHD codes, absent in JOREK "due to the employed B.C. for
the electric potential in the reduced MHD model ($\Phi=0$)". Experiments
measure 10–20% with Rogowski coils at different toroidal sectors
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6, citing
Gerasimov et al. 2015).

## Scope and consequences

- The suppression is a property of the boundary condition of the reduced
  model, not of reduced MHD's interior dynamics: the same JOREK run agrees
  with the full-MHD codes on kink onset, TQ duration and wall forces, and
  the asymmetry "does not seem to affect key quantities such as the wall
  forces" ([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6, §5).
- The same property makes the halo/eddy force decomposition exact in JOREK
  (see [wall forces](/definitions/wall-forces.md)), and it means halo
  currents close at the domain boundary rather than through the wall
  ([halo current](/definitions/halo-current.md)).
- The result motivated implementing a resistive wall for JOREK's full-MHD
  model ([Artola et al. (2021)](/sources/artola-2021.md), §5); coupling of
  the full-MHD model and of halo currents to the volumetric wall code was
  still ongoing in 2024 ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3;
  see [resistive-wall coupling](/methods/resistive-wall-coupling.md)).

## Contradictions

**Magnitude of the $I_p$ asymmetry in the full-MHD codes — Open.** Within
the same benchmark, NIMROD gives 3–4% and M3D-C1 1–1.4%, a factor ≈3, and
neither explanation nor resolution study is given for the difference
([Artola et al. (2021)](/sources/artola-2021.md), §4.1.6); both are
well below the 10–20% measured in experiments (same section), a gap the
source does not discuss although its case has no Ohmic heating, no
radiation and a resistivity ten times the Spitzer value (§3, Table 2).
[Hoelzl et al. (2021)](/sources/hoelzl-2021.md) (§4.8) quote the pooled
range 1–4% and attribute only the JOREK value. A full-MHD resolution and
resistivity scan of $\Delta I_p/I_p$ in both codes, and a comparison at
realistic resistivity, would separate numerical from physical causes.

## Citations

- [Artola et al. (2021)](/sources/artola-2021.md), §3, §4.1.6, §4.3.1, §5, Fig. 10.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §4.8.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §3.
