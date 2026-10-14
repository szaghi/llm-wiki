---
type: Method
title: "Permittivity, ion-mass and geometric scaling in PIC"
description: "Speed-up of fully kinetic PIC by enlarging the vacuum permittivity, reducing the ion mass or shrinking the device, which relaxes the Debye-length and plasma-frequency constraints at the cost of altering sheaths, instabilities and the resolved discharge profiles."
status: established
aliases: [permittivity scaling, artificial permittivity, vacuum permittivity scaling, reduced ion mass, mass-ratio scaling, geometric scaling, self-similarity scaling, accelerated PIC]
tags: [pic, numerics, kinetic, hall-thruster]
timestamp: 2026-10-14T00:00:00Z
---

# Permittivity, ion-mass and geometric scaling in PIC

The [resolution constraints of explicit PIC](/definitions/explicit-pic-resolution-constraints.md)
tie the cell size to $\lambda_D$ and the time step to $\omega_{pe}$. Three
non-physical changes relax them and are "still used in many simulations"
([Taccogna et al. (2023)](/sources/taccogna-2023.md), §III A):

- **Permittivity scaling**, $\varepsilon_0\to f_\varepsilon^2\varepsilon_0$,
  which multiplies $\lambda_D$ by $f_\varepsilon$ and divides $\omega_{pe}$
  by $f_\varepsilon$, allowing coarser cells and longer steps.
- **Ion-mass scaling**, $m_i\to m_i/f_m$ (stated by some sources as an
  increased electron-to-ion mass ratio).
- **Geometric scaling** by a factor $f_g$, which shrinks the device.

[Taccogna & Garrigues (2019)](/sources/taccogna-2019.md) (§3.3) attribute
the combined use to Taccogna et al. (2005) and state that the three
break non-dimensional similarity and affect sheaths and instabilities.
Taccogna et al. (2023, §III A) give no quantitative validity limits; for
electromagnetic thrusters they cite two works that caution that "the
physics might not be entirely equivalent".

## Values in use

| Source | Scaling | Registry value | Note |
|---|---|---|---|
| [Reza et al. (2022)](/sources/reza-2022.md), §§3.1–3.2 | ion mass divided by 100; $\varepsilon_0$ multiplied by 400 | $f_m=100$, $f_\varepsilon=20$ | native form converted on the Source page; used only in a 1D tuning run |
| [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), set-up section | $\varepsilon_0\to f_\varepsilon^2\varepsilon_0$ | $f_\varepsilon=10$ | applied to both their PIC-MCC and their five-moment fluid code |
| [Boyd (2005)](/sources/boyd-2005.md), §3.4 | increased electron-to-ion mass ratio and increased $\varepsilon_0$ | not stated | attributed to Szabo & Martinez-Sanchez, Blateau et al., Irishkov et al. |
| Taccogna & Garrigues (2019), §3.5 | small ion mass, large $\varepsilon_0$ | not stated | first 3D Hall-thruster PIC, an SPT-50 (Hirakawa & Arakawa 1995, 1996) |

Several sources run without scaling and say so: [Charoy et al.
(2020)](/sources/charoy-2020.md) (§II, "no reduced ion mass, no increased
$\varepsilon_0$"), [Miranda et al. (2026)](/sources/miranda-2026.md)
(§2.1, which avoid both because they make results harder to interpret),
[Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md) ("No scaling is
performed in the value of the permittivity of free space"), and the
pseudo-2D runs of Reza et al. (2022), which the authors call "real-scale".

## Evidence on what the scaling changes

**Discharge profiles at fixed transport coefficients** (Reza et al. 2022,
§3.2, Fig. 4). A three-zone Bohm-type collision frequency
($\alpha_{\mathrm B}=0.5/0.053/1.6$) was tuned on the 2D
axial–azimuthal benchmark potential with an accelerated 1D PIC run
($f_m=100$, $f_\varepsilon=20$), which needs about 300,000 time steps for
20 µs against 4,000,000 for the benchmark. The same coefficients in a
real-scale 1D run reproduce the 2D profiles; the accelerated run itself
shows "clear discrepancies" — peak axial field $E_x$ ($x$ axial, as in
the benchmark) about $2.2\times10^4$ V/m against
about $5\times10^4$ V/m, peak $T_e$ about 78 eV against about 54 eV (values
read from the figure). The authors conclude that scaling the physical
constants alters the resolved physics.

**Performance prediction** (Boyd 2005, §3.4). Fully kinetic Hall-thruster
PIC with an increased mass ratio and an increased permittivity
over-predicts thrust by about 10 % and efficiency by about 50 %
(attributed to Blateau et al. and Irishkov et al.).

**Sheath, acceleration region and peak temperature** (Troyetsky et al.
2026). The authors chose $f_\varepsilon=10$ after two earlier works and
note, citing them, that the factor affects the sheath width, the location
of the acceleration region and the peak $T_e$.

**Fixed neutrals instead of neutral dynamics.** Taccogna et al. (2023,
§III A d) add, as a further cost-cutting device, a fixed non-uniform
neutral background or a prescribed neutral density or source profile,
which has "shown limited conclusions" but allows parametric studies.

## Alternatives

The sources pursue other routes to the same speed-up without altering the
physical constants: [semi-implicit, implicit and energy-conserving PIC](/methods/implicit-and-energy-conserving-pic.md),
which relax the $\lambda_D$ and $\omega_{pe}$ constraints (Taccogna et al.
2023, §V C b); [reduced-order PIC](/methods/reduced-order-pic.md), which
Reza et al. (2022, §3.2) say allows full-size thruster PIC "without any
speed-up factor"; sparse-grid PIC (Taccogna et al. 2023, §V C a); and
[GPU acceleration](/methods/gpu-acceleration-of-pic.md).

# Citations

1. [Taccogna et al. (2023)](/sources/taccogna-2023.md), §§III A, III A d, V C a, V C b (accepted manuscript).
2. [Taccogna & Garrigues (2019)](/sources/taccogna-2019.md), §§3.3, 3.5 (accepted manuscript).
3. [Boyd (2005)](/sources/boyd-2005.md), §3.4.
4. [Reza et al. (2022)](/sources/reza-2022.md), §§3.1–3.2, Figs. 2, 4 (preprint).
5. [Troyetsky et al. (2026)](/sources/troyetsky-2026.md), simulation set-up section.
6. [Charoy et al. (2020)](/sources/charoy-2020.md), §II (accepted manuscript).
7. [Miranda et al. (2026)](/sources/miranda-2026.md), §2.1.
8. [Muñoz Tejeda et al. (2025)](/sources/munoz-2025.md), "PlasmaSim 0D" (p. 4).
