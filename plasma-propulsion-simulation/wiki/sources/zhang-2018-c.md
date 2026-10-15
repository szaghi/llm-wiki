---
type: Source
title: "Zhang et al. (2018) — Design and analysis of flexure revolute joint based on four-bar mechanism"
description: "Designs a monolithic flexure revolute joint for deployable space structures that reaches about 90° by inserting four crank-rocker four-bar angle amplifiers between an outer and inner ring, maps torque, stress-limited rotation and stiffness against beam thicknesses with a nonlinear Ansys beam model, and tests a double-thickness prototype whose anticlockwise stiffness is about twice the clockwise one."
resource: "doi:10.1016/j.actaastro.2018.06.046"
source_kind: paper
authors: [Zhang J., Guo H., Wu J., Gao G., Kou Z., Eriksson A.]
year: 2018
venue: "Acta Astronaut. 151:420–431"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhang_Design_and_analysis_of_flexure_revolute_joint_based_on_four-.pdf"
tags: [context, space-mechanisms, compliant-joint, deployable-structure, finite-element]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper designs a monolithic flexure revolute (FR) joint for
deployable space structures with a large rotation range (90°). Between
an outer and an inner ring it places four crank-rocker four-bar
mechanisms that act as angle amplifiers, with rotation ratio
$r_{13}=\theta_1/\theta_3=10$. The rocker is a large curved flexible
beam that stores the energy (the "large deformation element", LDE), and
the linkage joints are short flexible beams (LJ1, LJ2), so motion
transmission is separated from energy storage. The bar lengths come
from the four-bar loop-closure equations under compactness constraints
(§2.2). A nonlinear static finite-element model in Ansys (beam188 and
mass21 elements, titanium alloy) maps torque, maximum von Mises stress,
maximum stress-limited rotation $\theta_{\max}$ and secant rotational
stiffness against the three beam thicknesses $t_3$, $t_4$, $t_5$ (§3).
Five candidate joints (Table 1) span $\theta_{\max}=90.8°$ at
0.013 N·m/rad to 11.1° at 3.465 N·m/rad, with translational stiffnesses
in Table 2. A double-thickness (10 mm) version of Joint 1 is made and
tested in both rotation directions; measured and simulated stiffness
are compared (§4, Fig. 20), and in both the anticlockwise stiffness is
about twice the clockwise one. The paper has no plasma or propulsion
content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Angle amplification** (§2.1, shown by design): replacing the
   flexure part of an FR joint by a crank-rocker intermediate block lets
   a small rocker rotation drive a large crank rotation, decoupling
   energy storage (rocker) from motion transmission. The paper states,
   unreferenced, that most FR joints with small centre shift reach only
   about 10°.
2. **Loop closure** (§2.2.2, Eq. 1), four-bar ABCD with $b/a=l$,
   $c/a=m$, $d/a=n$:
   $$\begin{aligned}l\cos(\theta_2(t)+\beta_0)&=n+m\cos(\theta_3(t)+\varphi_0)-\cos(\theta_1(t)+\alpha_0),\\ l\sin(\theta_2(t)+\beta_0)&=m\sin(\theta_3(t)+\varphi_0)-\sin(\theta_1(t)+\alpha_0).\end{aligned}$$
   Eliminating $\theta_2$ gives Eq. 2:
   $$\cos(\theta_1+\alpha_0)=m\cos(\theta_3+\varphi_0)-\frac mn\cos(\theta_3+\varphi_0-\theta_1-\alpha_0)+\frac{m^2+n^2+1-l^2}{2n}.$$
   The reader re-derived Eq. 2 from Eq. 1: consistent.
3. **Design example** (§2.2.4): $0<\alpha_0<90°$, $a=10$ mm,
   $r_{13}=10$ so $\theta_1(t_e)=90°$ and $\theta_3(t_e)=9°$;
   $\beta_0=\alpha_0$; $a+b=d$, which "leads to"
   $\varphi_0=(\pi+\alpha_0)/2$. Chosen $\beta_0=\alpha_0=84°$,
   $a=10$ mm, $d=63$ mm, $b=50$ mm. Fig. 5: $\theta_1=0°$, 90°, 180° give
   $\theta_3=0°$, 9°, 18°.
4. **Torque and stress maps** (§3.2.1, Figs. 8–9, FE): the driving
   torque at 30° rotation increases with $t_3$, $t_4$, $t_5$; the
   maximum stress increases with $t_4$ and $t_3$, $t_5$ having limited
   influence. Stated: the maximum stress sits in LJ1 when $t_4$ is small
   or close to $t_5$, in LJ2 when $t_5$ is small and $t_4>t_5$.
5. **Rotation and stiffness maps** (§3.2.2, Figs. 11–12, FE): with
   $t_4=0.1$ mm, $\theta_{\max}$ reaches 90° ($t_3=0.1$ mm) and 46°
   ($t_3=1$ mm), with secant stiffness 0.0133 and 0.0175 N·m/rad; the
   effect of $t_5$ on $\theta_{\max}$ is negligible at $t_3=0.1$ mm;
   $\theta_{\max}$ falls nonlinearly as $t_4$ grows (see Recorded as
   printed).
6. **Five joints** (Table 1; thicknesses in mm, out-of-plane thickness
   5 mm):

   | joint | $t_3$ | $t_4$ | $t_5$ | $\theta_{\max}$ | stiffness (N·m/rad) | torque (N·m) |
   |---|---|---|---|---|---|---|
   | J1 | 0.1 | 0.1 | 0.1 | 90.8° | 0.013 | 0.02 |
   | J2 | 0.1 | 0.2 | 0.1 | 45.7° | 0.117 | 0.09 |
   | J3 | 0.1 | 0.3 | 1.0 | 26.7° | 0.460 | 0.21 |
   | J4 | 1.0 | 0.3 | 0.1 | 20.7° | 0.650 | 0.23 |
   | J5 | 1.0 | 0.5 | 1.0 | 11.1° | 3.465 | 0.67 |

7. **Clockwise stiffness against angle** (§3.2.3.1, Fig. 14): J1 −41%
   over +80°; J2 +18% over +40°; J3 +96% over +25°; J4 −5% over +19°; J5
   −2% over +10°. The influence of $t_5$ on stiffness grows as $t_3$
   decreases; the nonlinearity falls as the deformation-element
   thickness rises.
8. **Anticlockwise stiffness** (§3.2.3.2, Fig. 15): with contact against
   the outer ring included, the anticlockwise secant stiffness of
   Joints 4 and 5 is about twice the clockwise one.
9. **Translational stiffness** (§3.2.3.3, Table 2; secant at 1 mm /
   10 mm centre displacement, N/m): J1 5.38/5.42 (+0.74%); J2
   16.25/17.54 (+7.94%); J3 34.14/46.22 (+35.38%); J4 643.43/632.46
   (−1.7%); J5 2199.24/2218.22 (+0.86%); nearly direction-independent.
   Joints 1–3 are below 50 N/m and Joints 4–5 above 600 N/m, so the
   low-stiffness joints need the high-stiffness support with a needle
   bearing (Fig. 6b). Attributed to [13]: the PP-1 joint's centre
   displacement near 20 mm at 90° and the Ti-1 off-axis stiffness of
   3100 N/m.
10. **Experiment** (§4, Figs. 16–20, shown experimentally): a 10 mm
    out-of-plane, bolted (not welded) version of Joint 1, tested with
    torque and angle transducers, three repetitions per direction. The
    clockwise stiffness falls with angle in both simulation and
    experiment; the discrepancy grows as the angle decreases (attributed
    to bolted versus welded modelling and to initial deformation and
    angle setting of the beams); the measured anticlockwise stiffness is
    about twice the clockwise one, as simulated.

# Methods

* Kinematic synthesis: four-bar crank-rocker loop closure (Eqs. 1–2)
  with the five constraints of §2.2.2, nonlinear equations solved for
  the bar lengths against $\alpha_0$ (Fig. 3: $b$ and $d$ first decrease
  then increase with $\alpha_0$; $c$ increases monotonically). Four
  mechanisms are evenly distributed between the rings (Fig. 1).
* FE model (§3.1, Fig. 7): Ansys, beam188 elements for the structure
  and mass21 for the loading point at the joint centre; 1277 elements,
  1271 nodes; points O1–O4 restrained in the plane; loading-point
  translations restrained and in-plane rotation prescribed; outer ring
  fully restrained. Titanium alloy: Young's modulus 95 GPa, Poisson
  ratio 0.41, allowable stress 650 MPa; out-of-plane thickness 5 mm;
  LJ1 and LJ2 10 mm long. Static nonlinear equilibrium at a sequence of
  prescribed rotations, torque as the reaction; secant and tangent
  stiffness; APDL scripts. Thicknesses $t_4,t_5\in[0.1,1]$ mm,
  $t_3\in\{0.1,1\}$ mm. The anticlockwise case includes beam–outer-ring
  contact.
* $\theta_{\max}$ is the rotation at which the maximum von Mises stress
  reaches 650 MPa; the stiffness is the torque at $\theta_{\max}$
  divided by $\theta_{\max}$.
* Translational stiffness: prescribed in-plane centre displacement of
  1 mm and 10 mm, reaction force.
* Experiment (§4): bolted titanium-alloy joint, 10 mm out-of-plane
  thickness; rig with torque and angle transducers (Fig. 17); rotations
  30°, 50°, 70°, 90° in both directions (Figs. 18–19); three repetitions
  per direction. A simulation of the manufactured joint confirmed the
  linear scaling with out-of-plane thickness (stiffness doubled).

# Tests and results

* Design example (§2.2.4, Figs. 3–5): rotation ratio 10 verified at 0°,
  90° and 180°.
* Torque and stress maps at 30° (§3.2.1, Figs. 8–10); the Fig. 10 stress
  plots give maximum stresses 304, 313, 411 and 3010 MPa for panels a–d
  (the panels' parameter sets are not stated in the text).
* Rotation and stiffness maps (§3.2.2, Figs. 11–12): Key claim 5.
* Fig. 13 (§3.2.3): $t_3=1$ mm, $t_4=t_5=0.1$ mm gives
  $\theta_{\max}=46°$ and stiffness below 0.4 N·m/rad; $t_5=0.5$ or
  1 mm gives stiffness above 0.4 N·m/rad and $\theta_{\max}<20°$; the
  stated design choice is $t_3=0.1$ mm, $t_5=1$ mm.
* Table 1, Fig. 14, Fig. 15, Table 2: Key claims 6–9.
* Experiment against simulation (§4, Fig. 20): qualitative agreement in
  trend and in the anticlockwise-to-clockwise ratio of about 2; largest
  discrepancy at small angles. Contact analyses of Joints 1–3 did not
  converge (not shown).

# Notation map

The paper is structural mechanics; none of its quantities has a
registry counterpart, except time.

| Zhang et al. (2018) | Registry | Note |
|---|---|---|
| $a$, $b$, $c$, $d$ | words (bar lengths AB, BC, CD, AD) | **collision:** registry $c$ is the speed of light |
| $l$, $m$, $n$ | words (length ratios $b/a$, $c/a$, $d/a$) | **collisions** with the mass $m_s$ and density $n_s$ |
| $r_{13}$ | words (rotation ratio $\theta_1/\theta_3$) | |
| $\theta_1$, $\theta_2$, $\theta_3$ | words (bar rotation angles) | **collision:** registry $\theta$ is the azimuthal coordinate |
| $\alpha_0$, $\beta_0$, $\varphi_0$ | words (initial bar angles) | not $\alpha_{\mathrm B}$ |
| $\theta_{\max}$ | words (maximum stress-limited rotation) | |
| $t$ | $t$ | time |
| $t_3$, $t_4$, $t_5$ | words (thicknesses of LDE, LJ1, LJ2) | **collision** with the time $t$ |
| $T$ | words (torque) | **collision** with the temperature $T_s$ |
| $K$ | words (rotational secant stiffness) | |
| $E$ | words (Young's modulus) | **collision** with the electric field $\mathbf E$ |
| $\mu$ | words (Poisson ratio) | **collision** with $\mu_0$, $\mu_\perp$ |
| $\sigma$, $\sigma_{\max}$ | words (allowable stress; maximum von Mises stress) | **collision** with the cross section $\sigma_{sk}$ |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Zhang_Design_and_analysis_of_flexure_revolute_joint_based_on_four-.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 12 pages
     (420–431).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.046, printed on page 1
     and checked on Crossref: title, all six authors, Acta Astronaut.
     151:420–431 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 20 Jan 2018, revised 21 May 2018,
     accepted 20 Jun 2018, online 22 Jun 2018. Page 1 matches the
     filename title.
   * **How it was read.** Text layer; Eqs. 1–2 and the formula for
     $\varphi_0$ were checked on rendered page 3, legible. Figs. 1, 4 and
     6–20 are plots and diagrams; numbers come only from the text and
     tables. The Fig. 4 initial values beyond $a$, $b$, $d$ and
     $\alpha_0=\beta_0=84°$, the rocker length $c$ and $\varphi_0$ of the
     chosen design, the Fig. 10 panel parameters and the Fig. 20
     measured stiffnesses are not printed.
   * **Recorded as printed.**
     * §2.2.4: "the measures are chosen according to $a+b=d+3$ mm" with
       $a=10$ mm, $b=50$ mm, $d=63$ mm, which satisfy $a+b=d-3$ mm; the
       sign or a length is misprinted (the clearance intent suggests
       $d=a+b+3$ mm).
     * §3.2.1: "The torque of a flat beam is proportional to the
       thickness of the beam", then "the driving torque is proportional
       to the third power of $t_4$"; the first statement conflicts with
       the second.
     * §3.2.2: "$\theta_{\max}$ increases nonlinearly with $t_4$", while
       the same paragraph explains it by stress rising with $t_4$ and
       Table 1 and Fig. 13 show $\theta_{\max}$ falling as $t_4$ grows (J1
       at 0.1 mm, 90.8°; J2 at 0.2 mm, 45.7°); "decreases" is evidently
       meant.
     * The Fig. 10 caption gives 3010 MPa for panel d, far above the
       650 MPa allowable and the other panels (304–411 MPa): an
       overstressed case or a misprint, not resolvable from the text.
     * §4 compares the measured anticlockwise-to-clockwise ratio of
       (double-thickness) Joint 1 with simulated ratios of Joints 4–5,
       since contact analyses of Joints 1–3 did not converge: the
       agreement claim is cross-joint.
     * §3.2.2 gives 0.0175 N·m/rad for $t_3=1$ mm, $t_4=0.1$ mm, while
       §3.2.3 bounds the same case only as "less than 0.4 N·m/rad"; not
       a contradiction.
     * Reader's check: torque ≈ stiffness × $\theta_{\max}$ (in rad)
       holds for all five rows of Table 1 to two significant figures.
   * **Reference list.** 30 printed entries ([1]–[30]), matching the
     Crossref reference count.
