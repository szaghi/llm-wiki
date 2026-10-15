---
type: Method
title: "Semi-implicit, implicit and energy-conserving PIC"
description: "PIC time-integration schemes (direct-implicit, implicit-moment, energy-conserving, and the semi-implicit electrostatic scheme of Barnes) that relax the explicit Debye-length and plasma-frequency constraints at the price of numerical heating or cooling, with particle resampling and numerical heating as measured in a GPU Hall-thruster benchmark."
status: established
aliases: [implicit PIC, direct-implicit method, DIM, implicit-moment method, IMM, ECPIC, ECSIM, energy-conserving PIC, semi-implicit PIC]
tags: [pic, kinetic, numerics, hall-thruster, performance, verification]
timestamp: 2026-10-15T00:00:00Z
---

# Semi-implicit, implicit and energy-conserving PIC

Explicit electrostatic PIC must resolve the Debye length and the electron
plasma period (see [explicit-PIC resolution constraints](/definitions/explicit-pic-resolution-constraints.md)).
Implicit and semi-implicit schemes relax these constraints so that coarser
grids and longer steps can be used; their failure mode is numerical heating
or cooling, tied to the finite-grid instability.

## Direct-implicit and implicit-moment methods

* [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V C b, review:
  the direct-implicit method (DIM) and the implicit-moment method (IMM,
  Crank–Nicolson) relax the $\lambda_D$, $\omega_{pe}$ and light-crossing
  constraints. Both are mostly used semi-implicitly and suffer heating or
  cooling from the finite-grid instability; in the explicit case that
  instability triggers when $\Delta x$ exceeds $\lambda_D$, and DIM and IMM
  keep the heating when $\Delta x\gg\lambda_D$.
* DIM codes named: EDIPIC, LSP, Warp. IMM was used for an SPT-type Hall
  thruster ([Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V C b).
* In Hall-thruster wall studies, the 1D radial PIC-MCC model of Sydorenko
  et al. (2006–2009) is implicit (direct-implicit) and Cartesian, against
  the explicit cylindrical model of Taccogna et al.
  ([Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), Sect. 3.2,
  Sect. 3).

## Energy-conserving implicit PIC

* [Taccogna et al. (2023)](/sources/taccogna-2023.md), Sec. V C b, report
  that IMM implemented with identical current-assignment and
  field-interpolation functions and time-centring parameter 0.5 conserves
  energy exactly (ECPIC). It requires an Ampère-law field update even in the
  electrostatic case. In ECPIC the finite-grid instability occurs only if
  the electron drift exceeds the thermal velocity; that analysis was "never
  conducted for magnetized plasmas".
* Fully implicit solutions use particle enslavement with Jacobian-free
  Newton–Krylov iteration; ECSIM is the semi-implicit alternative.
  Subcycling of the orbit integration improves conservation and is needed for
  charge conservation (Sec. V C b).
* The RUB code ECCOPIC2S-M (implicit, energy-conserving, CUDA) was verified in
  the [axial–azimuthal Hall-thruster benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md)
  and validated against experiment ([Taccogna et al. (2023)](/sources/taccogna-2023.md),
  Sec. V C b). Because the benchmark fixed $\Delta t$ and $\Delta x$ at the
  explicit codes' values, the benefit of its GPU parallelization did not
  show there; it "became visible only in a different benchmark" (Sec. V B; see [GPU acceleration](/methods/gpu-acceleration-of-pic.md)).

## Semi-implicit electrostatic scheme of Barnes (WarpX)

[Marks & Gorodetsky (2025)](/sources/marks-2025.md) use the semi-implicit
electrostatic scheme of Barnes, as implemented in [WarpX](/software/warpx.md)
by Groenewald et al.
* **Field equation** (Eq. 9). In the Poisson equation for $\phi$ with
  electron charge density $-en_e$, the permittivity $\varepsilon_0$ is
  multiplied, inside the divergence, by one plus a quarter of an adjustable
  constant (greater than 1) times $(\omega_{pe}\Delta t)^2$.
  The added term stabilizes the electron plasma mode by raising its
  effective frequency. The authors note the resemblance to the
  direct-implicit method, which suffers numerical heating at large
  $\Delta t$ (Methods).
* **Coarsening tested** on the [axial–azimuthal benchmark](/benchmarks/axial-azimuthal-pic-benchmark.md)
  (Table 5, Figs. 8–14), starting from $\Delta t=5\times10^{-12}$ s on
  512×256 cells ($x$ axial, $y$ azimuthal, as in the benchmark):

  | Case | $\Delta t$ [s] | cells | constant | wall time (1 H100) | deviation from benchmark |
  |---|---|---|---|---|---|
  | 2× | $1\times10^{-11}$ | 256×128 | 8 | 11.5 h | ≤10% ($n$, $E_x$, $T_e$) |
  | 4× | $2\times10^{-11}$ | 128×64 | 16 | 4 h | <25% |
  | 8× | $4\times10^{-11}$ | 64×32 | 8 | 2 h | <25% |

  The deviation is the $L^2$ norm of the difference from the benchmark
  profile divided by the $L^2$ norm of the benchmark profile, ignoring
  $x>2.4$ cm (Eq. 10). The constant was chosen by minimum deviation of the
  time-averaged $T_e$ from the baseline. Runs used 75 initial particles per
  cell, multigrid tolerance $10^{-3}$, no resampling.
* **Peaks** drop from baseline to 8×: $E_x$ 50 → 43 (printed "kV"; a field
  unit is implied), density $3.6\times10^{17}$ → $3\times10^{17}$ m⁻³,
  $T_e$ 52 → 44 eV. At 8× the anode sheath widens, since $\Delta x$ exceeds
  the baseline sheath width (Fig. 10).
* **Instabilities** (Figs. 11–13). The 1× and 2× runs reproduce the two
  azimuthal modes of the benchmark (short wavelength near the anode, long
  wavelength downstream) with matching dominant wavelengths and frequencies;
  the distinction fades at 4× and disappears at 8×, and the maximum
  azimuthal field falls by 40% (4×) and 70% (8×). The time-averaged axial
  field stays consistent, which the authors read as transport magnitude
  being "relatively insensitive" to some spectral characteristics of the
  [electron drift instability](/definitions/electron-drift-instability.md)
  (a hypothesis).
* **Cathode current** (Fig. 14a), as a fraction of the extracted ion current,
  agrees with the benchmark at 1×, 2×, 4× and falls by a factor of 3 at 8×.
* **Speed-up.** The 2× case does 8× less work (¼ of the cells, ½ of the
  steps) but runs only about 3.5× faster than the explicit baseline; the
  authors attribute this to fixed GPU overhead on small problems and expect
  larger gains for larger and 3D problems (a hypothesis).
* **Trust.** The authors call the 4× and 8× runs "difficult to trust for
  predictive simulations" in the semi-implicit section, while the
  Conclusion speaks of "good agreement" up to 4× (see the Source page).
* Groenewald et al. are reported to have accelerated an electrostatic
  Penning discharge by two orders of magnitude with the same scheme
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods).

## Numerical heating

* In the semi-implicit runs the domain-averaged $T_e$ exceeds the benchmark
  by 2, 2.5 and 1 eV at 2×, 4× and 8×. Raising the constant improves $T_e$
  agreement at the cost of $n$ and $E_x$ (Fig. 9d–f); more particles reduce
  heating in the 2× case (Fig. 9g–i)
  ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Convergence and
  numerical heating", Fig. 14).
* The explicit baseline uses the energy-conserving gather of Lewis (1970) on
  a staggered grid with linear shape functions; the paper attributes to Sun
  et al. (2023) that this gather stabilizes runs with an under-resolved Debye
  length ([Marks & Gorodetsky (2025)](/sources/marks-2025.md), Methods).

## Particle resampling

[Marks & Gorodetsky (2025)](/sources/marks-2025.md), "Effect of
resampling", Table 5, Figs. 5–7, test the leveling-thinning resampling of
Muraviev et al. (2021) (target ratio 1.5, minimum 75 particles per cell)
in the explicit baseline:

| Trigger threshold (avg. particles per cell) | wall time [days] |
|---|---|
| none | 1.81 |
| 300 | 1.76 |
| 275 | 1.66 |
| 250 | 1.54 |
| 200 | 1.39 |

* The baseline reaches about 290 particles per cell per species at steady
  state, so a 300 threshold acts only during start-up.
* At a 200 threshold, $T_e$ at the right boundary rises by 7 eV over the
  baseline; the electron VDF widens in the axial and azimuthal directions
  (non-Maxwellian there) while the radial VDF stays Maxwellian. The authors'
  hypothesis is that resampling widens the VDF where particle resolution is
  insufficient, in high-density regions of the long-wavelength mode
  downstream of the magnetic-field peak (Fig. 6).
* Recommendation: set the threshold near the expected steady-state count.

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md) — Sec. V B, Sec. V C b.
2. [Marks & Gorodetsky (2025)](/sources/marks-2025.md) — Methods (Eq. 9), Results (Table 5, Figs. 5–14, Eq. 10), Conclusion.
3. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md) — §§3, 3.2 (accepted manuscript).
