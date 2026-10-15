---
type: Source
title: "Wang et al. (2018) — Design methodology of the waverider with a controllable planar shape"
description: "Extends osculating-cone waverider design so that the planform curve becomes a design input, via a geometric relation among flow capture, inlet capture and planform curves, and shows on Mach 6 designs that low-sweep planforms raise Mach 0.4 lift-to-drag ratio from 12.1 to 18.3–20.1 at nearly unchanged design-point lift-to-drag ratio."
resource: "doi:10.1016/j.actaastro.2018.06.048"
source_kind: paper
authors: [Wang J., Liu C., Bai P., Cai J., Tian Y.]
year: 2018
venue: "Acta Astronaut. 151:504–510"
local_file: "/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Wang_Design_methodology_of_the_waverider_with_a_controllable_plan.pdf"
tags: [waverider, osculating-cone, inverse-design, wide-speed-range, cfd]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper extends the osculating-cone / osculating-flowfield waverider design
method so that the planform, the *planar shape curve* (PSC), becomes a
design-driving input. A geometric relation among the *flow capture curve*
(FCC), the *inlet capture curve* (ICC, the shock trace in the base plane) and
the PSC (Eqs. 1–4) lets any two of the three curves determine the third. The
conventional method prescribes only FCC and ICC, so the planform follows
indirectly. The relation is solved as a "hybrid Cauchy-Dirichlet problem" by
a predictor-corrector Euler march from the FCC/PSC intersection K. The parent
flows are mixed: external Taylor–Maccoll cone flow, Internal Conical Flow A
(ICFA, after Mölder) and two-dimensional wedge flow, all sharing one effective
shock angle. Three designs at Mach 6 and 30 km (two specified by PSC and FCC,
one by PSC and ICC) and a constant-sweep reference are simulated in Fluent.
The planforms are reproduced, the design-point lift-to-drag ratio stays at
about 6.2–6.3, and the low-speed (Mach 0.4, sea level) lift-to-drag ratio
rises from 12.1 for the reference to 18.3–20.1.

# Key claims

1. **Osculating-plane condition** (§2.1, Eq. 1). The FCC point and the ICC
   point of one osculating plane lie on the normal to the ICC at the ICC
   point (back view, Fig. 1). Derived.
2. **Planform relation** (§2.1, Eqs. 2–3). Each osculating plane is treated
   as a sub-waverider of constant leading-edge sweep; with a straight
   effective shock, the local shock-to-FCC distance equals the tangent of the
   effective shock angle times the local length. Combining gives Eq. 3, which
   ties the back-view inclinations of ICC and FCC to the local sweep and the
   effective shock angle. Derived.
3. **Closure** (§2.1, Eq. 4). With the spanwise coordinate as independent
   variable, the slopes of PSC, ICC and FCC close the system; Eqs. 1, 3 and 4
   give the third curve from FCC-PSC or ICC-PSC. Derived.
4. **Mixed parent flows** (§2.2). External Taylor–Maccoll cone flow gives only
   convex ICCs; with a prescribed FCC and PSC the derived ICC cannot be kept
   convex, so ICFA (same straight shock) is used for concave parts and 2D
   wedge flow for near-straight segments, all with one effective shock angle.
   Curved internal and external cone flows are stated to be admissible (not
   shown).
5. **Design rules** (§2.3). The PSC should be smooth, C2 preferred; the
   maximum local sweep must not exceed the complement of the freestream Mach
   angle (attributed to the paper's ref. [16]); local sweep must not be 0°
   except at boundary points, where Eq. 3 is undefined; non-analytic PSCs are
   parametrized with NURBS. Stated.
6. **Sharp-nose completion** (§2.3). A PSC with nonzero slope at the nose
   gives a sharp nose; the solved ICC then fails to reach the symmetry plane
   and is completed by a circular arc centred on the FCC point in the symmetry
   plane, since only a constant-radius ICC lets the streamlines converge at
   the nose. Stated.
7. **Cost** (§2.3, Table 1). The procedure differs from the conventional one
   only at step 2; its extra cost is "far less" than streamline tracing.
   Stated, no timing.
8. **Planforms reproduced** (§3.3, Figs. 4a, 5a, 6a). The generated planforms
   follow the prescribed PSCs; the CFD base-plane shocks match the design ICC
   except at the arc/curve joint of i(A) and i(B), where the curvature jump
   forces smoothing; type ii matches "perfectly". Shown.
9. **Lift-to-drag ratios** (§3.3, Table 2). Design point (base drag
   excluded): i(A) 6.21, i(B) 6.25, ii 6.32, reference i(R) 6.33. Mach 0.4,
   sea level: 18.3, 20.1, 19.7 and 12.1, "increased by about fifty percent".
   Shown.
10. **Nonlinear lift** (§3.3, Fig. 7). $C_L$ against angle of attack
    (0–10°, design point) is nonlinear, more so for i(A) and i(B) than for
    ii. The authors attribute this to leading-edge vortex lift, following
    Rodi (their ref. [21]). Stated interpretation: no vortex is visualized.
11. **Integration** (§4). Hybrid external/internal parent flows allow an
    inward-turning inlet to be installed at the concave ICC segment. Stated,
    not shown.

# Methods

* Design: osculating-cone / osculating-flowfield method, streamline tracing in
  each osculating plane; parent flows by Taylor–Maccoll (external cone), ICFA
  (internal cone, Mölder) and 2D wedge; curve ODE system by predictor-corrector
  Euler with variable step; NURBS smoothing of the i(B) ICC. Code not named.
* Design condition: $\mathrm{Ma}_\infty=6$, standard atmosphere at 30 km;
  effective shock angle 14.35°. Design angle of attack not stated (Fig. 7 and
  the grid-study $C_L$ suggest 0°).
* Planforms: i(A), sweep decreasing linearly with span from 70° to 20°
  (Eqs. 5–6), horizontal straight FCC; i(B), fold-line planform (70° then 20°,
  sharp nose), ICC = arc + NURBS transition + straight line; ii, cubic PSC and
  ICC (Eqs. 7–8), blunt "∫"-like planform; i(R), constant 70° sweep.
* CFD: ANSYS Fluent, second-order AUSM, RNG k–ε for viscous runs, calorically
  perfect gas; pressure far field, extrapolated pressure outlet, no-slip wall
  (thermal condition not stated); unstructured tetrahedral mesh refined at
  wall and shock. $y^+$, reference area and length, and geometric units not
  stated.
* Grid study (i(A), design point): about 0.8, 1.2 and 1.6 million cells;
  $C_L$ 0.651 / 0.659, $C_D$ 0.105 / 0.107 for coarse / medium; fine "just
  change" (no numbers). Medium adopted.
* Validation (§3, Fig. 3): Space Shuttle model, wind-tunnel data of Li (ref.
  [18]): $\mathrm{Ma}_\infty=8.04$, $\mathrm{Re}_\infty=1.13\times10^7$ (length
  scale not stated), $p_0=7.8$ MPa, $T_0=892$ K, $\alpha=0$–20°. $C_L$ and
  $C_D$ agree well, best at small $\alpha$; above 15° the CFD over-predicts
  (approximate figure reading at 20°: $C_L$ about 0.67 against 0.6, $C_D$
  about 0.38 against 0.32).
* Low-speed runs ($\mathrm{Ma}_\infty=0.4$, sea level): solver settings and
  angle of attack not stated. No uncertainty quantification.

# Tests and results

| Case | Length | Width | Max thickness | Volume index | Aerodynamic centre | $L/D$ design | $L/D$ Mach 0.4 |
|---|---|---|---|---|---|---|---|
| i(A) | 5.0 | 5.79 | 0.88 | 0.113 | 0.68 length | 6.21 | 18.3 |
| i(B) | 5.0 | 5.79 | 0.87 | 0.119 | 0.69 length | 6.25 | 20.1 |
| ii | 5.0 | 5.79 | 0.71 | 0.134 | 0.67 length | 6.32 | 19.7 |
| i(R) | 5.0 | 1.81 | 0.87 | 0.152 | 0.62 length | 6.33 | 12.1 |

Table 2 as printed; length units not stated. The volume index is not defined
in the paper (cited to its ref. [20]). Fig. 7 (approximate reading): $C_L$
about 0.66 at 0°, about 2.5–2.7 at 10°, above a linear reference beyond about
6°.

# Notation map

| Wang et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| Ma∞, Re∞ | $\mathrm{Ma}_\infty$, $\mathrm{Re}_\infty$ | Re length scale not stated |
| Pt, Tt | $p_0$, $T_0$ | |
| α, AoA | $\alpha$ | |
| CL, CD, CL/CD | $C_L$, $C_D$, $L/D$ | |
| βeff | words (effective shock angle) | a constant $\beta_s$ shared by all osculating planes |
| λ, λ0, λn | words (leading-edge sweep; nose, tail values) | $\tan\lambda$ = local length / local width, sweep measured from the spanwise axis |
| θ1, θ2 | words (back-view inclination of ICC, FCC) | **collision:** registry $\theta_w$ |
| R_local | words (local ICC curvature radius) | **collision:** registry $R$ |
| p, i, f | words (PSC, ICC, FCC curve functions) | **collision:** $p$ is pressure |
| τ | words (volume index) | **collision:** $\tau_w$; not identified with $\eta_V$ |
| D_local, L_local, W_local, L_total, W_total | words | |
| x, y, z | $x$, $y$, $z$ | streamwise, spanwise, vertical |

# Pages created or updated

Chunk 2 (2026-10-14) created or updated these pages, which cite this source:

* [Osculating-cone waverider design](/methods/osculating-cone-waverider-design.md)
* [SST k–ω turbulence model in high-speed flow](/methods/sst-k-omega-model.md)
* [Waverider](/definitions/waverider.md)

# Citations

1. `/home/stefano/papers/mosaic/high-speed-aerothermodynamics/2018_Crossref_Acta_Astronautica_Wang_Design_methodology_of_the_waverider_with_a_controllable_plan.pdf`.
   * **Version.** Publisher's typeset version (Elsevier, 7 pages).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.048, printed on page 1 and
     checked on Crossref: Acta Astronaut. 151, 504–510, five authors as
     above, issue 2018-10. Received 12 Feb 2018, revised 18 May 2018,
     accepted 22 Jun 2018, online 27 Jun 2018 (page 1). Page-1 title matches
     the filename.
   * **How it was read.** Full text layer; equation pages 505, 507, 508 and
     Table 2 / Fig. 7 (p. 509) checked on rendered images; no equation
     illegible. Values from Figs. 3 and 7 are approximate readings.
   * **Recorded as printed.**
     * §3.3 puts the aerodynamic centres "at about 0.68Llocal"; Table 2 gives
       0.67–0.69 of the total length.
     * Eq. 6 with 70°, 20° and width 5.79 gives a total length of about 6.71
       (reader's integration), while Table 2 lists 5.0 for i(A); for i(R),
       5.0/1.81 = 2.76 ≈ tan 70°, consistent. Unresolved.
     * "Increased by about fifty percent": Table 2 gives +51%, +66% and +63%
       over i(R).
     * Grid study medium-mesh $C_L/C_D$ = 0.659/0.107 = 6.16, against 6.21 in
       Table 2; whether the grid-study drag excludes base drag is not stated.
     * The $C_L$ magnitudes of Fig. 7 imply a non-planform reference area,
       which is not declared.
   * **Reference list.** 21 printed entries (Crossref count 21). Ref. [16]
     prints "sculating", ref. [15] "curvee"; ref. [20] names "C. Paul,
     V. Jean, Transatmospheric launcher sizing", most likely Czysz &
     Vandenkerckhove in Curran & Murthy, *Scramjet Propulsion* (2000), kept
     as printed; ref. [7] has an unmatched quotation mark.
