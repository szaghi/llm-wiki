---
type: Software
title: "STARWALL"
description: "Green's-function thin-wall code that supplies JOREK's free-boundary and resistive-wall response: the vacuum is not meshed, 3D thin walls with holes are linear triangles, and the response matrices enter JOREK implicitly as a natural boundary condition with the wall currents eliminated; validated against CEDRES++, DINA, CASTOR3D, M3D-C1, NIMROD and JOREK–CARIDDI."
status: established
aliases: [JOREK-STARWALL]
tags: [code, wall, free-boundary, vde, disruption, benchmark]
timestamp: 2026-10-16T12:00:00Z
---

# STARWALL

STARWALL computes the electromagnetic response of the vacuum and of thin
resistive conductors to the plasma boundary and is coupled to
[JOREK](/software/jorek.md) as JOREK–STARWALL
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §2.9). See
[free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md).

## Model and numerics

* The vacuum is treated by a Green's-function method and is not discretized;
  thin walls are meshed with linear triangles, and the formalism allows 3D
  walls with holes ([Artola et al. (2021)](/sources/artola-2021.md), §2,
  Table 1; Hoelzl et al. 2021, §2.9). Thin walls are characterized by
  $\eta_w/d_w$ (Artola et al. 2021, §3); the ITER wall uses
  $\eta_w/d_w=1.33\times10^{-5}\,\Omega$ (Hoelzl et al. 2021).
* **Coupling.** The tangential field at the JOREK boundary is expressed
  through response matrices acting on the normal field and on the wall and
  coil currents, which follow RL circuit equations. This relation replaces
  the Dirichlet conditions on $\psi$ and $j$ by a natural boundary condition
  in the boundary integral of the current definition equation. The coupling is
  fully implicit; the implicit wall currents are eliminated analytically, so
  the matrix size is unchanged, though boundary rows become denser (Hoelzl et
  al. 2021, §2.9). [Isernia et al. (2023)](/sources/isernia-2023.md) (§II D)
  describe the same structure with a generalized eigenproblem of the wall
  inductance and resistance matrices, which diagonalizes the wall equation
  when $\Delta t$ changes.
* Response matrices are computed once per grid and wall, reused, and
  exchanged by MPI-IO; STARWALL is MPI-parallel with distributed response
  matrices and reaches a speed-up of 63.3 on 128 MPI tasks (Hoelzl et al.
  2021, §2.9, §3.6, Fig. 10). Wall-coupling matrix compression is a 2021–2024
  development ([Hoelzl et al. (2024)](/sources/hoelzl-2024.md), §5).
* Free or fixed boundary can be chosen per toroidal harmonic; self-consistent
  PF coils, 3D coils, passive coils and sensors are supported (Hoelzl et al.
  2021, §2.9). RMP fields can come self-consistently from 3D coils (§2.4).
* A free-boundary Grad–Shafranov solve is available through STARWALL with
  Newton iterations (Hoelzl et al. 2021, §2.2).

## Verification and benchmarks

* Earlier tests: equilibrium and tearing modes with a wall, resistive-wall-mode
  growth rate against analytic theory, VDE growth rates within 10–20 % of
  CEDRES++ over many wall resistivities, coil fields against Biot–Savart
  (Hoelzl et al. 2021, §4.8).
* ITER: an axisymmetric 15 MA VDE whose last-closed-surface position agrees
  with DINA within a few cm, and a 7.5 MA vertical oscillation driven by the
  VS3 coils with two 6 cm stainless-steel shells (Hoelzl et al. 2021, §4.8,
  Figs. 26–27).
* ASDEX Upgrade passive stabilizing loop: VDE growth rate within about 20 % of
  CASTOR3D over orders of magnitude of loop conductivity, which needs a high SOL
  resistivity because CASTOR3D treats the SOL as vacuum (§4.8, Fig. 30).
* [NSTX VDE benchmarks](/benchmarks/nstx-vde-benchmarks.md) with M3D-C1 and
  NIMROD: 22 000 Bézier plasma elements and 48 000 wall triangles, $n\in[0,10]$;
  vertical force about 28 kN at peak, sideways force about 3.4 kN, thermal
  quench 0.14 ms (Artola et al. 2021, §3, §4.1, Fig. 8). With
  $\mathbf J\cdot\mathbf n=0$ at the wall, the wall force splits cleanly into
  halo and eddy parts; the peak forces come from halo currents (§4.3.1,
  Fig. 12). See [wall forces](/definitions/wall-forces.md) and
  [halo current](/definitions/halo-current.md).
* JOREK–CARIDDI: VDE growth rates within 2 % and $n=1$ tearing growth rates
  within 1 % over a wall-resistivity scan from ideal wall to no wall (Isernia
  et al. 2023, §IV–V, Figs. 5, 7).
* ITER runaway beam with a cold VDE against DINA, with the vessel shells,
  PF1–6 and CS1–6 coils and a vessel-resistivity scan; at nominal resistivity
  the motion has not converged to the ideal-wall limit
  ([Bandaru et al. (2024)](/sources/bandaru-2024.md), §IV, Fig. 9b). See the
  [ITER runaway-electron benchmarks](/benchmarks/iter-runaway-electron-benchmarks.md).

## Applications in the cited sources

ITER mitigated current quenches in 3D at realistic Lundquist number: a 3D
inner vessel of 75 000 triangles, a filament outer vessel and the OTS/DIR
structures, coupled implicitly to JOREK reduced MHD with $n=0$–10,
continued to ≈1.5 s, about 5 million core-hours per run; the vertical force
peaks on the vessel L/R time (≈500 ms) after $I_p$ has vanished
([Artola et al. (2022)](/sources/artola-2022.md), §2, §4.3, §5; see
[wall forces](/definitions/wall-forces.md)). The passive-structure model
had been benchmarked axisymmetrically against DINA (same source, §2).

Free-boundary RMP plasma response, which "was shown to recover experimental
flux surface corrugation accurately", and VDEs including ASDEX Upgrade hot VDEs
(Hoelzl et al. 2024, §2.2, §3.1); 3D NSTX VDEs (Artola et al. 2021); ITER
halo-current fractions as a function of current-quench to wall time (Hoelzl et
al. 2021, §6.3); runaway beams with cold VDEs (Bandaru et al. 2024). See
[vertical displacement event](/definitions/vertical-displacement-event.md).

## Limitations

* Thin walls only; the skin depth can be comparable to wall widths, so the
  thin-wall assumption "is not always robust" (Isernia et al. 2023, §I), which
  motivated [CARIDDI](/software/cariddi.md).
* In 2021 the implicit wall-potential coupling was not implemented: the wall
  potential is set to zero, halo currents enter only through a post-processor
  for wall forces, and ferromagnetic walls are not integrated (Hoelzl et al.
  2021, §2.9).
* At the time of the 3D VDE benchmark JOREK's full-MHD model had no
  resistive-wall extension, so JOREK–STARWALL ran reduced MHD; the toroidal
  $I_p$ asymmetry suppressed by the reduced-MHD boundary condition motivated
  that extension (Artola et al. 2021, §2, §5).

# Citations

1. [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §2.2, §2.4, §2.9, §3.6, §4.8, §6.3.
2. [Artola et al. (2021)](/sources/artola-2021.md) — §2, Table 1, §§3–5.
3. [Isernia et al. (2023)](/sources/isernia-2023.md) — §I, §II D, §§IV–V.
4. [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §2.2, §3.1, §5.
5. [Bandaru et al. (2024)](/sources/bandaru-2024.md) — §IV.
6. [Artola et al. (2022)](/sources/artola-2022.md) — §2, §4.3, §5.
