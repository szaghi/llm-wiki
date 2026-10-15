---
type: Source
title: "Wang et al. (2018) — Design methodology of the waverider with a controllable planar shape"
description: "Extends osculating-cone waverider design so that the planform curve becomes a design input, through a geometric relation among flow capture, inlet capture and planar shape curves solved by predictor-corrector marching with mixed external, internal-cone and wedge parent flows, and shows by CFD that low-sweep planforms raise Mach 0.4 lift-to-drag ratio from 12.1 to 18.3–20.1 at nearly unchanged Mach 6 performance."
resource: "doi:10.1016/j.actaastro.2018.06.048"
source_kind: paper
authors: [Wang J., Liu C., Bai P., Cai J., Tian Y.]
year: 2018
venue: "Acta Astronaut. 151:504–510"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Design_methodology_of_the_waverider_with_a_controllable_plan.pdf"
tags: [context, hypersonic, waverider, vehicle-design]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

The paper extends the osculating-cone / osculating-flowfield waverider
design method so that the planform, the planar shape curve (PSC), becomes
a design-driving input. A geometric relation among the flow capture curve
(FCC), the inlet capture curve (ICC, the shock trace in the base plane)
and the PSC (Eqs. 1–4) lets any two of the three determine the third;
the conventional method prescribes FCC and ICC and obtains the planform
indirectly. The relation is solved as a "hybrid Cauchy-Dirichlet problem"
by predictor-corrector Euler marching from the FCC/PSC intersection K.
Parent flows are mixed: external Taylor–Maccoll cone flow, Mölder's
internal cone flow A (ICFA) and 2-D wedge flow, sharing one effective
shock angle. Three designs at Mach 6 and 30 km (two PSC-FCC, one PSC-ICC)
and a constant-sweep reference are simulated with Fluent: the planforms
are reproduced, design-point L/D stays at about 6.2–6.3, and the Mach 0.4
sea-level L/D rises from 12.1 to 18.3–20.1.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Osculating-plane condition** (§2.1, Eq. 1): FCC point F and ICC point
   G lie on the normal to the ICC at G,
   $(F_z-G_z)/(F_y-G_y)=-1/\tan\theta_1$, with $\theta_1$, $\theta_2$ the
   back-view inclinations of ICC at G and FCC at F.
2. **Geometry** (§2.1, Eqs. 2–3): $\overline{FH}=D_{local}/\sin(\theta_1-\theta_2)=W_{local}/\cos\theta_2$;
   treating each osculating plane as a sub-waverider of constant sweep
   $\lambda$ ($\tan\lambda=L_{local}/W_{local}$) with a straight effective
   shock ($D_{local}=\tan\beta_{eff}\,L_{local}$) gives
   $\cos\theta_2/\sin(\theta_1-\theta_2)=1/(\tan\lambda\tan\beta_{eff})$.
3. **Closure** (§2.1, Eq. 4): with $y$ independent, $\tan\lambda=p^{(1)}$,
   $\tan\theta_1=i^{(1)}$, $\tan\theta_2=f^{(1)}$ on $(0,W_{total})$, for
   the PSC, ICC and FCC functions $p$, $i$, $f$; Eqs. 1, 3, 4 give the
   third curve from FCC-PSC or ICC-PSC.
4. **Mixed parent flows** (§2.2): external cone flow yields convex ICCs; a
   prescribed FCC-PSC cannot keep the derived ICC convex, so ICFA (same
   straight shock) is used on concave parts and wedge flow on near-straight
   ones, all sharing $\beta_{eff}$. Curved cone flows are stated admissible,
   not shown.
5. **Design rules** (§2.3, stated): smooth (preferably C²) PSC; maximum
   local sweep not above the complement of the freestream Mach angle
   (attributed); local sweep nonzero except at boundary points (else Eq. 3
   is undefined); NURBS for non-analytic PSCs.
6. **Sharp nose** (§2.3): a PSC with nonzero slope at the nose leaves the
   solved ICC short of the symmetry plane; it is completed by a circular
   arc of radius $L_{total}\tan\beta_{eff}$ centred on the FCC point, since
   only a constant-radius ICC lets streamlines converge at the nose.
7. **Cost** (§2.3, Table 1): only step 2 of the conventional procedure
   changes; the extra cost is "far less" than streamline tracing (stated,
   no timing).
8. **Planform families** (§§3.1–3.2, Eqs. 5–8): type i(A) with linearly
   decreasing sweep, $p^{(1)}(y)=\tan[(y/W_{total})(\lambda_n-\lambda_0)+\lambda_0]$,
   integrated to $p(y)=-\frac1a\ln\cos(ay+b)+c$ with
   $a=(\lambda_n-\lambda_0)/W_{total}$, $b=\lambda_0$, $c=\frac1a\ln\cos b$;
   type ii with cubic PSC and ICC (blunt nose, $z_0=-1$, $z_n=0$,
   $\theta_{1,0}=0°$, $\theta_{1,n}=2°$).
9. **Planforms reproduced** (§3.3, Figs. 4a, 5a, 6a): shown; CFD shocks
   match the design ICC except at the arc/curve joint of i(A) and i(B),
   where the curvature jump forces smoothing; type ii matches "perfectly".
10. **Performance** (§3.3, Table 2, base drag excluded): design-point L/D
    i(A) 6.21, i(B) 6.25, ii 6.32, i(R) 6.33; Mach 0.4 sea-level L/D 18.3,
    20.1, 19.7, 12.1, "increased by about fifty percent". Shown.
11. **Nonlinear lift** (§3.3, Fig. 7): $C_L$ against angle of attack
    (0–10°, design point) is nonlinear, attributed to leading-edge vortex
    lift after Rodi [21]; stronger for i(A), i(B) than ii. Interpretation
    stated; no vortex is shown.
12. **Integration** (§4, stated): hybrid parent flows allow an
    inward-turning inlet at the concave ICC segment.

# Methods

* Design: osculating cone/flowfield method with Taylor–Maccoll (external),
  ICFA (internal) and wedge parent flows, streamline tracing per osculating
  plane, predictor-corrector Euler with variable step, NURBS smoothing for
  i(B). Code not named. Design condition Mach 6, standard atmosphere at
  30 km, $\beta_{eff}=14.35°$; design angle of attack not stated.
* CFD: ANSYS Fluent, second-order AUSM, RNG k–ε for viscous runs,
  calorically perfect gas, pressure far field, extrapolated outlet, no-slip
  wall; unstructured tetrahedral mesh refined at wall and shock. $y^+$,
  convergence, reference area and length, and units of geometric
  quantities not stated.
* Grid study (case i(A), design point): about 0.8 M cells $C_L$ 0.651,
  $C_D$ 0.105; 1.2 M cells 0.659, 0.107 (adopted); 1.6 M cells "just
  change" (no numbers).
* Validation (§3, Fig. 3): Space Shuttle model, wind-tunnel data of Li
  [18], Mach 8.04, $Re_\infty=1.13\times10^7$, 7.8 MPa, 892 K, $\alpha$ =
  0–20°; good agreement, slight overprediction above 15° (at 20°, CFD
  $C_L\approx0.67$ vs 0.6, $C_D\approx0.38$ vs 0.32; approximate reading).
* Low-speed runs at Mach 0.4, sea level; solver settings and angle of
  attack not stated. No uncertainty stated.

# Tests and results

| Design | $L_{total}$ | $W_{total}$ | Max. thickness | Volume index τ | Aero. centre | L/D Mach 6 | L/D Mach 0.4 |
|---|---|---|---|---|---|---|---|
| i(A) (sweep 70° → 20°) | 5.0 | 5.79 | 0.88 | 0.113 | 0.68 $L_{total}$ | 6.21 | 18.3 |
| i(B) (fold line 70°/20°) | 5.0 | 5.79 | 0.87 | 0.119 | 0.69 $L_{total}$ | 6.25 | 20.1 |
| ii (cubic PSC-ICC) | 5.0 | 5.79 | 0.71 | 0.134 | 0.67 $L_{total}$ | 6.32 | 19.7 |
| i(R) (constant 70°) | 5.0 | 1.81 | 0.87 | 0.152 | 0.62 $L_{total}$ | 6.33 | 12.1 |

Table 2 as printed (units not stated); τ is defined only by citation [20].
Fig. 7: $C_L\approx0.66$ at 0° to about 2.5–2.7 at 10° (approximate),
above a linear reference beyond about 6°.

# Notation map

| Wang et al. (2018) | Registry | Note |
|---|---|---|
| $Ma_\infty$, $Re_\infty$ | words | |
| $P_t$, $T_t$ | words (stagnation pressure, temperature) | |
| $\alpha$ (AoA), $C_L$, $C_D$, L/D | words | |
| $\beta_{eff}$ | words (effective shock angle) | |
| $\lambda$, $\lambda_0$, $\lambda_n$ | words (sweep angle) | **collision risk:** registry $\lambda_D$, $\lambda_w$ |
| $\theta_1$, $\theta_2$ | words (back-view curve inclinations) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $R_{local}$ | words (ICC curvature radius) | |
| $D_{local}$, $L_{local}$, $W_{local}$, $L_{total}$, $W_{total}$ | words | registry $L$ is a generic length |
| $p$, $i$, $f$ (curve functions) | words | $f$ collides with distribution functions $f_s$ |
| τ | words (volume index) | |
| $x$, $y$, $z$ | $x$, $y$ and words | streamwise, spanwise, vertical; registry $z$ is axial |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Design_methodology_of_the_waverider_with_a_controllable_plan.pdf`.
   * **Version.** Publisher's typeset version, 7 pages.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.048, printed on page 1
     and checked on Crossref: title, five authors, Acta Astronaut.
     151:504–510 match; issue October 2018; page 1 gives received 12 Feb
     2018, revised 18 May 2018, accepted 22 Jun 2018, online 27 Jun 2018.
     Page 1 matches the filename title.
   * **How it was read.** Clean text layer; equation pages 505, 507, 508
     and Table 2/Fig. 7 (p. 509) checked on rendered images; all equations
     legible. Figs. 3 and 7 values are approximate readings.
   * **Recorded as printed.**
     * §3.3 places the aerodynamic centres "at about 0.68Llocal to the
       nose"; Table 2 gives 0.67–0.69 $L_{total}$.
     * Reader's check, unresolved: integrating Eq. 5 with $\lambda_0=70°$,
       $\lambda_n=20°$, $W_{total}=5.79$ gives $L_{total}\approx6.71$, while
       Table 2 lists 5.0 for i(A); for i(R), 5.0/1.81 = 2.76 ≈ tan 70° is
       consistent.
     * "Increased by about fifty percent" understates Table 2: the ratios
       to i(R) are 1.51, 1.66 and 1.63.
     * The medium-grid $C_L/C_D=0.659/0.107=6.16$ differs slightly from the
       Table 2 L/D of 6.21 for the same case (drag bookkeeping of the grid
       study not stated).
     * Fig. 7 coefficients (about 0.66 at zero incidence) imply an
       undeclared, non-planform reference area.
     * The nonlinear-lift attribution to vortex lift at the Mach 6 design
       point is stated without any vortex evidence.
   * **Reference list.** 21 printed entries, matching the Crossref
     reference count. Printed slips: ref. [16] title "sculating" for
     "osculating"; ref. [15] "curvee"; ref. [7] has an unmatched opening
     quotation mark; ref. [20] "C. Paul, V. Jean, Transatmospheric launcher
     sizing" most likely misrenders Paul A. Czysz and Jean Vandenkerckhove
     (chapter in Curran & Murthy, *Scramjet Propulsion*, 2000), identity
     to be checked at merge.
