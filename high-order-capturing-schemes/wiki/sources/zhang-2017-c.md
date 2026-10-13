---
type: Source
title: "Zhang, Wang, Hao, Huang, Chen & Shi (2017) — Experimental investigation of shock wave diffraction over a single- or double-sphere model"
description: "Shock-tube measurements of the unsteady drag on one 40 mm sphere and on two spheres side by side behind weak planar shocks (M_s 1.10–1.33) from internal accelerometers: a drag peak near half a diameter of shock travel that falls from 14.48 to 4.52 as M_s rises, a negative phase, and double-sphere peaks always above the single-sphere one, largest when the spheres touch; no simulation."
resource: "doi:10.1007/s00193-016-0641-4"
source_kind: paper
authors: [Zhang L.T., Wang T.H., Hao L.N., Huang B.Q., Chen W.J., Shi H.H.]
year: 2017
venue: "Shock Waves 27:97–107"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2017-ShockWaves-Zhang-101007s00193-016-0641-4.pdf"
tags: [benchmark, 3d, experiment]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

An experimental paper with no numerical scheme and no simulation. It
measures the time-resolved drag on one sphere, and on two spheres side by
side, when a weak planar shock passes over them in a circular shock tube
of 200 mm inner diameter. Each 40 mm hollow aluminium sphere hangs on a
thin wire and carries an internal piezoelectric accelerometer; the drag is
mass times acceleration. For the single sphere the drag coefficient rises
to a peak near half a diameter of shock travel, turns negative, and then
settles to a small positive value. Its value here is the measured drag
history a 3D simulation of a [shock passing a sphere](/benchmarks/shock-sphere-interaction.md)
can be scored against.

# Key claims

1. **Facility** (§2.1, Figs. 1–2). Horizontal shock tube: 1260 mm
   driver, 2000 mm driven section, 1540 mm acrylic test section and a
   1260 mm extension open to the ambient air, all 200 mm inner diameter.
   High-pressure N₂ drives air. Aluminium diaphragms 0.05–0.2 mm thick
   give $M_s = 1.10$–$1.33$. The shock speed comes from two wall
   transducers 800 mm apart, sampled at 1 MHz.
2. **Model** (§2.2, Fig. 4). Spheres of 40 mm diameter made of two
   threaded hollow aluminium-alloy hemispheres, 300 mm from the
   test-section outlet, held by a 0.5 mm wire; sphere plus accelerometer
   weigh 94.55 g. The wire's effect on inertia is estimated below 2 % and
   its tension below 1 % (the largest displacement is about 100 µm up to
   five diameters of shock travel).
3. **States** (Table 1, §2.3). Ambient 305 K and 0.1013 MPa, air with
   $\gamma = 1.4$, sound speed 350.2 m/s. Post-shock states from the
   Rankine–Hugoniot relations at the measured $M_s$; Re from the
   post-shock speed and the diameter:

   | Diaphragm (mm) | $M_s$ | post-shock $\rho$ (kg/m³) | post-shock speed (m/s) | Re |
   |---|---|---|---|---|
   | 0.05 | $1.10 \pm 0.01$ | 1.35 | 55.71 | 147,381 |
   | 0.08 | $1.16 \pm 0.01$ | 1.47 | 86.95 | 230,026 |
   | 0.1 | $1.19 \pm 0.02$ | 1.53 | 102.04 | 269,947 |
   | 0.15 | $1.26 \pm 0.03$ | 1.69 | 140.84 | 372,593 |
   | 0.2 | $1.33 \pm 0.03$ | 1.81 | 168.71 | 446,323 |

   Centre spacing over diameter 1, 1.5, 2, 2.5 and 3; three repeats per
   case, 15 single-sphere and 75 double-sphere tests.
4. **Drag** (§3.1, eqs. 1–2). $C_D$ is the drag over the post-shock
   dynamic pressure times the frontal area (the registry definition).
   Time is normalized by the time the incident shock takes to travel one
   diameter (96 µs at $M_s = 1.19$); zero is the shock's arrival at the
   front stagnation point. Wire tension is neglected.
5. **Signal processing** (§3.2, Figs. 5–8). Calibration finds resonances
   near 15, 40, 75 and 125 kHz. The signal is band-block filtered by FFT
   (cut-offs 10 and 130 kHz) and fitted by a ninth-order polynomial (9th
   and 11th order overlap to 200 µs; 7th differs slightly). The peak is
   the mean of 3 tests.
6. **Single sphere** (§4.1, Fig. 9). $C_D$ peaks near 0.5 diameters of
   shock travel, is negative from about 1.6 to 2.6, then tends to a
   positive value with decaying oscillations. The peak falls from 14.48 at
   $M_s = 1.10$ to 4.52 at $M_s = 1.33$; relative errors ±1.8, ±1.5,
   ±5.0, ±1.6 and ±4.1 % for the five $M_s$. The steady value is below
   0.42 at these Re, and the Jourdan et al. non-stationary correlation
   gives at most 0.46.
7. **Mechanism** (§4.1, Fig. 10, a schematic drawn from the literature,
   not a visualization made here).
   * Regular reflection on the front surface turns into Mach reflection at
     a critical angle, quoted from Tanno et al. (2003) as about 33° at
     $M_s = 1.22$, at about 0.228 diameters of shock travel.
   * The first peak balances the falling interaction pressure against the
     growing projected area.
   * Unlike a cylinder, where the drag maximum coincides with the
     reflection transition (quoted from Tanno et al.), the transition has
     "very little influence" on the sphere's drag.
   * The negative phase comes from the diffracted waves focusing at the
     rear stagnation point.
   * Side-wall reflections are weak for $1.10 \le M_s \le 1.33$.
8. **Energy reading** (§4.1, eq. 3, read on the page image). $C_D$ is
   recast as the ratio of the kinetic energy per unit volume given to the
   solid by the drag work to that of the shocked gas; this ratio "increases
   inversely with the intensity of the shock wave", as a cited simulation
   of a 0.8 mm sphere predicts. The longer unsteady stage at low $M_s$ is
   linked to irregular rupture of the thinnest diaphragm, which makes
   post-shock wavelets and axial asymmetry.
9. **Double sphere** (§4.2, Figs. 11–12). At $M_s = 1.19$ the touching
   pair has the highest curve before 2.0 diameters of travel. For every
   $M_s$ the peak first falls, then rises, then falls with spacing; it is
   largest for touching spheres, and every double-sphere peak exceeds the
   single-sphere peak. The relative excess of the largest and smallest
   double-sphere peaks over the single-sphere peak is (35.8, 19.6 %),
   (35.4, 18.9 %), (23.7, 8.3 %), (43.3, 1.2 %) and (42.9, 0.8 %) for
   $M_s = 1.10$, 1.16, 1.19, 1.26 and 1.33; data uncertainty ±9.2, ±2.4,
   ±7.0, ±6.0 and ±5.7 %. The non-monotone spacing dependence is
   attributed, without visualization, to reflected shocks and Mach stems
   between the spheres.
10. **Shading** (§4.3). Tube-to-sphere area ratio 25 (single) and 12.5
    (double). The authors argue from the schematics that the peak is not
    affected by shading; shading is not quantified.

**Tests.** Experiments only: 5 $M_s$ × 3 repeats for one sphere
(Fig. 9: $C_D$ histories to five diameters of travel, peak against
$M_s$), and 5 $M_s$ × 5 spacings × 3 repeats for two spheres (Fig. 11:
histories at $M_s = 1.19$; Fig. 12: peak against spacing). No shadowgraph,
schlieren or interferometry. The peak height and timing depend on the
filtering and the polynomial fit (§3.2, Fig. 8b), which limits a
comparison with a simulation.

# Notation map

| Zhang et al. (2017) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $M_s$, Re | $M_s$, $\mathrm{Re}$ | same meaning |
| $C_d$ (and $C_D$ for the single-sphere peak) | $C_D$ | drag over post-shock dynamic pressure times frontal area |
| $d$, $r$ | $D$, $D/2$ | $r$ is the registry's stencil count |
| $\rho_2$, $U_2$ | post-shock $\rho$ and $\vert\mathbf v\vert$, in words | $U$ is the registry's entropy function |
| $F$, $m$, $a$ | words | drag, sphere mass, acceleration |
| $t_0$, $t' = t/t_0$ | words | time over the shock transit time across one diameter |
| $H = L/d$; $L$ (eq. 3) | words | centre spacing over diameter; a characteristic length. $L$ is the left-eigenvector matrix |
| $\alpha = A_c/A_P$ | words | area ratio; $\alpha$ is the Lax–Friedrichs speed |
| $RD_{\max}$, $RD_{\min}$, $\delta$ | words | relative peak excesses; diaphragm thickness |

# Pages created or updated

* Created [Shock passing a sphere](/benchmarks/shock-sphere-interaction.md).
* Cited in [Regular and Mach reflection](/definitions/mach-reflection.md)
  (the transition angle quoted from Tanno et al., and the cylinder/sphere
  contrast in drag).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2017-ShockWaves-Zhang-101007s00193-016-0641-4.pdf`.
   * **Version.** The publisher's typeset article (Springer), 11 pages;
     received 25 April 2014, published online 21 March 2016.
   * **Identity.** doi:10.1007/s00193-016-0641-4, printed on page 1 and
     checked on Crossref: Shock Waves 27(1):97–107, January 2017. The
     issue year 2017 gives the slug; `-c` because `zhang-2017` and
     `zhang-2017-b` are other works.
   * **How it was read.** Text extraction, all sections; eq. 3 and the
     Conclusions checked on the page images. Figs. 3, 6, 7, 10 and 13 were
     not digitized; the $C_D$ curves of Figs. 9a and 11 and the peaks of
     Figs. 9b and 12 exist only as plots, so only the extremes (14.48,
     4.52) and the relative excesses are reproduced as numbers.
   * **Recorded as printed.** The smallest relative excess (19.6, 18.9,
     8.3, 1.2, 0.8 %) decreases monotonically with $M_s$ over all five
     values, yet §4.2 hedges "when $M_s$ is relatively large" (the
     Conclusions drop the hedge); the largest excess is not monotone. The
     analyzer's 1 MHz rate is said to exceed the transducer's "maximum
     sampling frequency of around 100 kHz". The accelerometer sensitivity
     unit is printed "pc/ms⁻²".
   * **Reference list:** 16 entries. Zhang L.T. et al. (2011, Shock
     Waves 21:243) is keyed `zhang-2011-e`, because `zhang-2011` to
     `zhang-2011-d` are other works; Shi (2003) is keyed `shi-2003-b`.
