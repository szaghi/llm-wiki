---
type: Benchmark
title: "MHD blast wave"
description: "An over-pressured region expanding into a uniformly magnetized medium, whose anisotropic fast and slow shocks test the robustness of MHD schemes at low plasma beta, symmetry preservation, and AMR against uniform grids; run in non-relativistic and relativistic versions."
status: established
aliases: [magnetized blast wave, MHD blast]
tags: [benchmark, mhd, verification, amr]
timestamp: 2026-10-13T00:00:00Z
---

# MHD blast wave

**Set-up.** A circular (2D) or spherical (3D) region of high pressure in a
uniform medium threaded by a uniform oblique magnetic field. The blast is
elongated along the field and bounded by fast and slow shocks. Strong
fields (low plasma beta) make it a robustness test; there is no exact
solution. The non-magnetized point explosion is the
[Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md).

## Non-relativistic

* *2D, adiabatic and isothermal* ([Stone et al. (2008)](/sources/stone-2008.md),
  §8.4, Figs. 28–30). Initial conditions of Londrillo & Del Zanna (2000);
  the initial pressure and radius are deferred to that paper. Adiabatic
  case: domain $(1, 3/2)$, $200\times300$, PPM, HLLC (hydro) or HLLD
  (MHD), $\mathbf B = (1/\sqrt2, 1/\sqrt2)$, periodic, shown at $t = 0.2$
  and 1. CTU keeps perfect symmetry, and the field suppresses
  Richtmyer–Meshkov fingers. Isothermal case: field amplitude 1 (plasma
  beta 2) and 10 (beta 0.02), HLLD; the paper calls CTU with
  [constrained transport](/methods/constrained-transport.md) "robust for
  low-β flows".
* *3D, uniform grid* ([Stone et al. (2008)](/sources/stone-2008.md), §8.6,
  Fig. 36). Domain $(1, 1.5, 1)$, $200\times300\times200$, HLLD, PPM,
  $t = 0.2$. Symmetric; the bubble grows more slowly than in 2D.
* *3D, AMR against uniform* ([Zhang et al. (2018)](/sources/zhang-2018.md),
  §5.1(iv), Figs. 11–14). Londrillo & Del Zanna generalized to 3D: a
  sphere at the ambient density and 100 times the ambient pressure;
  ambient plasma beta 0.2; maximum fast Mach number 2.54; periodic cube of
  20 sphere radii on a side; $\mathbf B$ along $(1, 1, 0)/\sqrt2$;
  $\gamma = 5/3$, CTU, Courant factor 1/2. Uniform $512^3$ against AMR on
  a $256^3$ root with 3 levels, refined on the normalized pressure
  gradient, about $8.3\times10^7$ cells with filling fractions 27.3%, 0.7%
  and 0.3% at 6 Alfvén crossing times of the sphere radius. In sphere
  radii, the equatorial fast shocks lie at $\pm9.4$ (captured in 1–2
  cells) and the contacts at $\pm1.3$ (4–5 cells); on the axis, the
  contact at $\pm5.4$ (4–5 cells) and the slow shock at $\pm7.2$ (1–2
  cells). A "finger" structure at the slow-shock nose, absent in the
  uniform run, is confirmed physical by runs with the field rotated (with
  a 5° tilt to avoid the carbuncle), seeded density noise of amplitude
  $2\times10^{-2}$, and static refinement resolving the shortest noise
  wavelength by 16 cells (Fig. 14). The paper reads it as a
  Rayleigh–Taylor-like instability.

## Relativistic

[Mignone et al. (2012)](/sources/mignone-2012.md) use a variant of
Komissarov (1999) with the parameters of Beckwith & Stone (2011): domain
$[-6, 6]^2$, a cylinder of radius 0.8 with $\rho = 10^{-2}$ and $p = 1$ in
an ambient medium with $\rho = 10^{-4}$ and $p = 5\times10^{-3}$,
adiabatic index $4/3$, $t = 4$.
[Stone et al. (2020)](/sources/stone-2020.md) print the same domain,
densities, pressures and adiabatic index, with a transition between
radii 0.8 and 1.

* *2D, PLUTO-CHOMBO* ([Mignone et al. (2012)](/sources/mignone-2012.md),
  §6.4, Fig. 28). Field amplitude 1; base $48^2$ with 5 levels (effective
  $1536^2$), HLLC, tagging on total energy. Maximum Lorentz factor about
  1.76, symmetry kept, 2258 blocks; AMR about 4.5 times faster than a
  uniform grid on 4 processors.
* *3D sphere, PLUTO-CHOMBO* ([Mignone et al. (2012)](/sources/mignone-2012.md),
  §6.5, Fig. 30). $[-6, 6]^3$, sphere of radius 0.8 with a linear decay to
  the ambient state at radius 1, oblique field 0.1; base $40^3$ with 4
  levels (effective $640^3$), HLLD. Maximum Lorentz factor about 6.3;
  frozen-flux scaling from 32 to 2048 processors with efficiency above
  0.75 for a maximum box size of 20 (27,661 blocks), worse for 40.
* *2D and 3D, [Athena++](/software/athena-plus-plus.md)* ([Stone et al. (2020)](/sources/stone-2020.md),
  §4.3.3, Figs. 40–41). Density $10^{-2}$ inside radius 0.8 falling to
  $10^{-4}$ outside radius 1 (pressure 1 to $5\times10^{-3}$); field
  components $B^x = B^y = 1/\sqrt{20}$ in 2D and $1/\sqrt{200}$ in 3D;
  CFL 0.25, PLM, HLLD. 2D: uniform $1536^2$ against AMR on a $48^2$ root
  with 5 levels and $16^2$ blocks; 3D: uniform $768^3$ against AMR on a
  $48^3$ root with 4 levels and $16^3$ blocks. Agreement better than 1% in
  most of the volume; cost 24.7 against 6.18 core-hours in 2D (a factor
  4.0) and 2720 against 316 core-hours in 3D (8.6).

The relativistic runs are not one set-up. In 3D they agree, $|\mathbf B| = 0.1$
in both (components $1/\sqrt{200}$ in Stone et al.). In 2D they differ:
$|\mathbf B| = 1$ in Mignone et al. against $|\mathbf B| = 1/\sqrt{10}\approx 0.32$
(components $1/\sqrt{20}$) in Stone et al.

**What it shows.** Unsplit CTU with constrained transport stays
symmetric and robust down to plasma beta 0.02
([Stone et al. (2008)](/sources/stone-2008.md), §8.4).
[AMR](/methods/adaptive-mesh-refinement.md) reproduces uniform-grid
solutions at a fraction of the cost
([Stone et al. (2020)](/sources/stone-2020.md), §4.3.3;
[Mignone et al. (2012)](/sources/mignone-2012.md), §6.4), and can resolve
physical structure the uniform grid misses
([Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(iv)).

## Later uses (batch 3)

### Non-relativistic

* *3D, Cholla* ([Caddy & Schneider (2024)](/sources/caddy-2024.md),
  §3.1.5, Fig. 11; [Cholla](/software/cholla.md)). The domain and grid of
  the Stone et al. (2008) 3D run, $1\times1.5\times1$ with
  $200\times300\times200$ cells, $t = 0.2$, now with printed parameters:
  ambient $\rho = 1$, $p = 0.1$, $\mathbf B = (1/\sqrt2, 1/\sqrt2, 0)$
  (plasma beta 0.2), and $p = 10$ inside a sphere of radius 0.1. VL+CT
  with HLLD. Smooth, symmetric contours; qualitative. "Like Stone &
  Gardiner (2009), we find instabilities if β is decreased by a factor of
  10", i.e. at plasma beta 0.02.
* *2D, AMR against uniform on one GPU, AthenaK*
  ([Stone et al. (2026)](/sources/stone-2026.md), §5.1, Fig. 20;
  [AthenaK](/software/athenak.md)). Pressure 100 times the background
  inside a circle; uniform $4096^2$ with $64^2$ MeshBlocks against AMR on
  a $1024^2$ root with $64^2$ blocks and two levels, refining where the
  density exceeds 1.1 times the background; $t = 0.4$; one NVIDIA A100,
  precision not stated. The densities are "essentially identical"
  (visual). Throughput falls from 181 to 141 million cell updates per
  second with AMR ("roughly 20% overhead"; 22% from the printed numbers),
  and the AMR run takes 18% of the uniform wall time (the caption says
  "5.4× faster"; $1/0.18 = 5.6$). The authors say the overhead is "likely
  amplified" in 2D; the 3D problem does not fit on one device.

Cholla's instability at plasma beta 0.02 qualifies, and does not
contradict, the Stone et al. (2008) statement above that CTU with
constrained transport is "robust for low-β flows" down to beta 0.02:
that statement comes from the isothermal 2D case integrated with CTU,
while Cholla's run is adiabatic, 3D and integrated with VL+CT.

### Relativistic

* *Komissarov cylindrical explosions, AthenaK*
  ([Stone et al. (2026)](/sources/stone-2026.md), §3.5, Fig. 10). Inner
  $\rho = 10^{-2}$, $p = 1.0$ within radius 1; ambient $\rho = 10^{-4}$,
  $p = 3\times10^{-5}$; an exponential ramp between them; field
  $B_x = 0.1$ and $B_x = 1$; pressure-based AMR with $20\times20$
  MeshBlocks. With the first-order flux
  correction (FOFC) fallback the problem runs "robustly" without the
  floors, background changes or artificial viscosity other codes need.
  Visual; robustness only.
* *Komissarov weak-field case, GRaM-X*
  ([Shankar et al. (2023)](/sources/shankar-2023.md), §IV B, eqs. 14–15,
  Fig. 4; [GRaM-X](/software/gram-x.md)). The GRHydro set-up after
  Komissarov: radii 0.8 and 1.0, $\rho = 10^{-2}$ inside and $10^{-4}$
  outside, $p = 1.0$ inside and $3\times10^{-5}$ outside, exponential
  transition (eq. 14), $\mathbf B = (0.1, 0, 0)$, adiabatic index 4/3;
  $200\times200\times8$ cells on $[-6, 6]^2$ ($h = 0.06$), constrained
  transport, TVD-minmod, HLLE, RK4, CFL 0.25, $t = 4$, no AMR; static
  Minkowski spacetime, on a GPU. Visual comparison with the GRHydro and
  Komissarov figures; small deviations in 1D cuts are attributed to cell-
  against vertex-centred initial data and "go away" (not shown) with the
  same discretization.

These two are a **further relativistic variant**, not the set-up of
Mignone et al. (2012) and Stone et al. (2020) above: the ambient pressure
is $3\times10^{-5}$ instead of $5\times10^{-3}$. The inner radius is
printed differently in the two (radius 1 with a ramp in AthenaK, radii
0.8 to 1.0 in GRaM-X). AthenaK's §3.5 also shows a test that its text
calls the relativistic MHD blast wave of Stone et al. (2020), §4.3.1,
"as proposed by Mignone et al. (2012)", while the Fig. 9 caption calls it
an "SRMHD shock tube test"; it is not counted here.

The batch-3 runs add a GPU instance of the AMR-against-uniform comparison
(identical density, about a fifth of the wall time; Stone et al. 2026),
the low-beta limit of VL+CT (Caddy & Schneider 2024), and the
low-ambient-pressure relativistic variant as a robustness test (Stone et
al. 2026; Shankar et al. 2023). All comparisons remain visual.

## Later uses (batch 6)

* *2D, adiabatic, CTU+CT, parameters printed* ([Gardiner & Stone (2005)](/sources/gardiner-2005.md),
  §5.6, Fig. 13; arXiv v1). The Londrillo & Del Zanna (2000) parameters that
  Stone et al. (2008) above defer: domain $[-0.5,0.5]^2$, $200\times200$;
  $\rho = 1$, $\mathbf v = 0$, $B_x = B_y = 10/\sqrt2$ (field magnitude 10),
  $B_z = 0$; $p = 100$ (plasma beta 2) inside radius 0.125, $p = 1$ (beta
  0.02) outside; adiabatic, $\gamma = 5/3$; $t = 0.2$; boundary conditions
  not stated. Ranges at $t = 0.2$: density 0.192–3.31, pressure 1.0–32.1,
  magnetic energy density 23.5–77.7. The scheme is called "stable and
  accurate for low-β plasma problems involving strong MHD shock waves",
  with symmetry preserved and "no indication of grid related artifacts".
  Stone et al.'s adiabatic run above uses a field of magnitude 1, so the two
  are not the same case.

This is an adiabatic low-beta data point for 2D CTU+CT at the ambient
beta, 0.02, at which Cholla's 3D VL+CT run turns unstable (batch 3), and
complements the isothermal one of Stone et al. (2008). The qualification
recorded in batch 3 stands: the integrator (CTU against VL) and the
dimension (2D against 3D) differ. Cholla's printed base run has the same
pressure ratio, 100 ($p = 10$ in a background of 0.1), but how its
beta-0.02 variant was set up is not printed, so the cases are not
otherwise compared.

# Citations

1. [Stone et al. (2008)](/sources/stone-2008.md), §8.4, §8.6.
2. [Zhang et al. (2018)](/sources/zhang-2018.md), §5.1(iv) (arXiv v4).
3. [Mignone et al. (2012)](/sources/mignone-2012.md), §6.4, §6.5.
4. [Stone et al. (2020)](/sources/stone-2020.md), §4.3.3.
5. [Caddy & Schneider (2024)](/sources/caddy-2024.md), §3.1.5 (arXiv v2).
6. [Stone et al. (2026)](/sources/stone-2026.md), §3.5, §5.1 (arXiv v1).
7. [Shankar et al. (2023)](/sources/shankar-2023.md), §IV B (arXiv v2).
8. [Gardiner & Stone (2005)](/sources/gardiner-2005.md), §5.6 (arXiv v1).
