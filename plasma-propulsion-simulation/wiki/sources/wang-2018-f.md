---
type: Source
title: "Wang, Xie & Fu (2018) — Vibration analysis of functionally graded porous shear deformable tubes excited by moving distributed loads"
description: "Models free and forced transverse vibration of simply supported functionally graded porous tubes under a uniformly distributed moving load with a refined shear-deformable tube theory and a Ritz/Newmark scheme, validated against elasticity, Timoshenko and exact moving-point-load results, with parametric studies of porosity, geometry, load speed and load length."
resource: "doi:10.1016/j.actaastro.2018.06.003"
source_kind: paper
authors: [Wang Y., Xie K., Fu T.]
year: 2018
venue: "Acta Astronaut. 151:603–613"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Vibration_analysis_of_functionally_graded_porous_shear_defor.pdf"
tags: [context, structural-dynamics, functionally-graded-materials, moving-load, vibration]
timestamp: 2026-10-15T00:00:00Z
---

# Summary

The paper models the free and forced transverse vibration of a simply
supported functionally graded (FG) porous tube traversed by a uniformly
distributed load of length $d$ moving at constant speed $v$. The
Young's and shear moduli and the density vary radially by cosine laws,
with a symmetric (Type I, Eq. 1) or non-symmetric (Type II, Eq. 2)
porosity distribution; the open-cell metal-foam law
$E_0/E_1=(\rho_0/\rho_1)^2$ (Eq. 3) ties density porosity to modulus
porosity (Eq. 4). The kinematics follow the Zhang–Fu refined
(higher-order shear) tube beam theory (Eqs. 5–6); the equations of
motion come from a Lagrange/Ritz procedure with sine/cosine admissible
functions (Eqs. 16–19) and are integrated with the Newmark-β method. The
model is validated against elasticity and Timoshenko frequencies
(Table 2) and an exact moving-point-load solution [43] (Table 3,
Fig. 3). Parametric studies report the effect of the porosity
coefficient $e_0$, porosity type, slenderness, radius ratio, load speed
and load length on the natural frequencies and the maximum mid-span
deflection. The paper has no plasma or propulsion content.

# Key claims

Symbols are the paper's own (see the notation map).

1. **Porosity laws** (§2, Eqs. 1–2): Type I
   $E(r)=E_1\left[1-e_0\cos\left(\frac{\pi}{R_o-R_i}\left(r-\frac{R_o+R_i}{2}\right)\right)\right]$,
   the same form for $G(r)$ and, with $e_m$, for $\rho(r)$; Type II
   replaces the argument by
   $\frac{\pi}{2(R_o-R_i)}\left(r-\frac{R_o+R_i}{2}\right)+\frac{\pi}{4}$.
   $e_0=1-E_0/E_1=1-G_0/G_1$ with $0<e_0<1$, and $e_m=1-\rho_0/\rho_1$.
2. **Foam law** (Eqs. 3–4): $E_0/E_1=(\rho_0/\rho_1)^2$, hence
   $e_m=1-\sqrt{1-e_0}$. Stated as open-cell metal-foam behaviour, not
   derived.
3. **Kinematics** (Eqs. 5–6): $u=f\,\partial w_0/\partial x+g\,\varphi$,
   $w=w_0$, with
   $f=\frac{z}{R_o^2+R_i^2}\left(\frac{R_o^2R_i^2}{r^2}-\frac{r^2}{3}\right)$
   and $g=f+z$, stated to satisfy the stress-free conditions on both
   surfaces (from [46–48]).
4. **Moving-load vector** (Eqs. 19–20, Table 1): generalised load
   $\int_{l_0(t)}^{l_1(t)}q\sin(j\pi x/L)\,dx$ for the deflection
   coordinates, zero for the rotations, in closed form per stage
   (entering, fully on or covering, leaving) for $d\le L$ and $d>L$.
5. **Free-vibration validation** (§4, Table 2): for an aluminium tube the
   first three dimensionless frequencies agree with elasticity and
   Timoshenko values to about three significant figures (worst 0.9642
   against 0.960 from elasticity).
6. **Moving-point-load validation** (Table 3): 40 kN point load,
   $R_o=0.05$ m, $R_o/R_i=2$, $L/R_o=40$; maximum $w(0.5L)/(2R_o)$ of
   0.2291 ($n=4$ and $n=6$) against the exact 0.2284 at 40 m/s and
   0.3348 against 0.3334 at 100 m/s; $n=6$ adopted.
7. **Distributed to point load** (Fig. 3): loads with $d=0.5L$, $0.25L$,
   $0.1L$, $0.01L$ (same 40 kN resultant, 20 m/s) converge to the exact
   point-load response; $d=0.01L$ is visually coincident.
8. **Frequency against porosity** (§5.1.1, Table 4, Fig. 4): the
   fundamental frequency falls with $e_0$ and rises again at high $e_0$,
   with its minimum near $e_0=0.75$ in Table 4; the drop from $e_0=0$ to
   the minimum is 8.24% (Type I) and 3.20% (Type II); Type II
   frequencies are slightly higher. The explanation (rates of stiffness
   and inertia reduction) is stated, not shown.
9. **Geometry** (§5.1.2–5.1.3, Figs. 5–6): the fundamental frequency
   falls sharply with $L/R_o$ below 10, is nearly flat for
   $R_i/R_o<0.4$ and then rises roughly linearly.
10. **Forced response** (§5.2.1, Figs. 7–9): Type I responses are
    slightly larger than Type II; the maximum deflection grows with
    $e_0$, mainly for Type I; against speed it peaks at a critical
    velocity (term attributed to [36]) whose peak rises with $e_0$.
11. **Geometry, forced** (§5.2.2, Figs. 10–11): the maximum deflection
    grows roughly linearly with $L/R_o$, is insensitive to $R_i$ below
    $0.1R_o$ and then decreases linearly with $R_i$.
12. **Load length** (§5.2.3, Figs. 12–14): longer loads give more peaks
    during the passage (one for $d=0.5L$ and $1.0L$, two for $3.0L$,
    three for $5.0L$); the maximum deflection grows with $d$ for $d<L$
    and is bounded and wave-like in $d$ for $d>L$, peaking at even
    multiples of $L$; maxima always occur in the forced phase.

# Methods

* Model: one-dimensional refined shear-deformable beam theory for
  circular tubes (Zhang & Fu [46]); radially graded isotropic linear
  elastic material with the transverse stresses neglected (Eq. 8);
  strains (Eq. 7), potential energy with stiffness integrals
  (Eqs. 9–11), kinetic energy with inertia integrals (Eqs. 12–14), work
  of the moving load (Eq. 15).
* Discretisation: Ritz/Lagrange with sine functions for the deflection
  and cosine functions for the rotation (simply supported, Eq. 17);
  a $2n\times2n$ system $[K]q+[M]\ddot q=F$ (Eq. 19) with $n=6$.
* Time integration: Newmark-β (parameters and time step not given);
  free vibration from the eigenproblem with $F=0$; no damping.
* Materials: validation aluminium ($E=70$ GPa, $\rho=2700$ kg/m³,
  $\nu=0.3$); parametric open-cell steel foam ($E_1=200$ GPa,
  $\nu=0.3$, $\rho_1=7850$ kg/m³).
* Non-dimensionalisation (§5): $\Omega_n=\omega_nR_o\sqrt{\rho_1/E_1}$;
  $w_m=w(0.5L)/D_0$ with $D_0=1000\,qL^3/(48E_1I_0)$;
  $\tau=tv/(L+L_0)$.

# Tests and results

* Free vibration (§4, Table 2), aluminium, first three modes: solid tube
  ($R_i/R_o=0$) 0.0761, 0.2734, 0.5393 against 0.076, 0.273, 0.539
  (elasticity and Timoshenko); $R_i/R_o=1/3$: 0.1682, 0.5346, 0.9642
  against 0.168, 0.535, 0.960 (elasticity) and 0.168, 0.536, 0.964
  (Timoshenko).
* Moving point load (Table 3), 40 / 100 m/s: $n=2$ 0.2276 / 0.3337;
  $n=4$ and $n=6$ 0.2291 / 0.3348; exact [43] 0.2284 / 0.3334.
* Porosity sweep (Table 4, $L/R_o=20$, $R_o/R_i=3$), first-mode
  frequency Type I / Type II: $e_0=0$ 0.1031 / 0.1031; 0.25
  0.0999 / 0.1013; 0.50 0.0968 / 0.0999; 0.75 0.0946 / 0.0998; 0.95
  0.0983 / 0.1046. Second mode from 0.3253 to a minimum of
  0.3029 / 0.3101; third mode from 0.5840 to 0.5500 / 0.5507, both at
  $e_0=0.75$.
* Forced-response cases (§5.2): $R_o=0.05$ m, $R_o/R_i=2$, $L/R_o=40$,
  $v=80$ m/s, $e_0=0.4$, $d=0.6L$ and $1.5L$ (Fig. 7); porosity sweeps
  (Fig. 8); speed sweeps for $d=3L$ and $0.5L$ (Fig. 9); slenderness
  and inner-radius sweeps (Figs. 10–11); load lengths from $0.01L$ to
  $8.0L$ (Figs. 12–14, $e_0=0.25$). Trends only; no curve values were
  read.

# Notation map

The paper is structural dynamics; few of its quantities have a registry
counterpart.

| Wang, Xie & Fu (2018) | Registry | Note |
|---|---|---|
| $x$ | words (tube axial coordinate) | **collision:** the registry's axial coordinate is $z$ |
| $y$, $z$ | words (cross-section coordinates; $z$ transverse, downward) | **collision** with the registry's $y$ and axial $z$ |
| $r$, $\theta$ | $r$, $\theta$ | radial and azimuthal coordinates of the cross-section |
| $t$ | $t$ | time |
| $L$ | $L$ | tube length |
| $R_o$, $R_i$ | words (outer, inner radius) | |
| $E(r)$, $G(r)$ | words (Young's and shear moduli) | **collision** with the electric field $\mathbf E$ |
| $\nu$ | words (Poisson's ratio) | **collision** with $\nu_{sk}$ |
| $\rho(r)$ | words (mass density) | not the charge density $\rho_c$ |
| $e_0$, $e_m$ | words (modulus and density porosity coefficients) | **collision** with the elementary charge $e$ |
| $q$ | words (distributed load, N/m) | **collision** with the species charge $q_s$ |
| $v$ | words (load speed) | **collision** with the particle velocity $\mathbf v$ |
| $d$ | words (load length) | **collision** with the data vector $\mathbf d$ |
| $n$ | words (number of admissible functions) | **collision** with $n_s$ |
| $u$, $w$, $w_0$ | words (axial and transverse displacements) | |
| $\varphi$ | words (generalised rotation) | not the potential $\phi$ |
| $f$, $g$ | words (warping shape functions) | **collision** with $f_s$ and the relative speed $g$ |
| $T$, $U$, $W$ | words (kinetic and potential energy, load work) | **collision** with $T_s$ and the macroparticle weight $W$ |
| $\omega_n$ | $\omega$ | natural angular frequency of mode $n$ |
| $\Omega_n$ | words (dimensionless frequency) | **collision** with the Hall parameter $\Omega_e$ |
| $D_0$ | words | two meanings in the paper (see Recorded as printed) |
| $\tau$ | words (dimensionless time) | |

# Pages created or updated

No concept page cites this source. It is outside the plasma-propulsion domain (bundle law, D23); here it is ingested as a Source-only page with its reference list.

# Citations

1. `/home/stefano/papers/mosaic/plasma-propulsion-simulation/2018_Crossref_Acta_Astronautica_Wang_Vibration_analysis_of_functionally_graded_porous_shear_defor.pdf`.
   * **Version.** Publisher's final typeset PDF (Elsevier), 11 pages
     (603–613), IAA copyright.
   * **Identity.** doi:10.1016/j.actaastro.2018.06.003, printed on page 1
     and checked on Crossref: title, all three authors, Acta Astronaut.
     151:603–613 match; issue October 2018 (no published-online field on
     Crossref); page 1 gives received 8 Mar 2018, revised 25 May 2018,
     accepted 1 Jun 2018, online 2 Jun 2018. Page 1 matches the filename
     title.
   * **How it was read.** Full text layer, equations checked on the
     rendered pages, all legible. Figs. 4–14 are plots; only the trends
     stated in the text were recorded.
   * **Recorded as printed.**
     * Conclusion (2) says the dimensionless mid-span displacement
       decreases as the porosity coefficient increases, while §5.2.1
       (Figs. 8–9) says the maximum displacement increases with it; the
       body text is the result shown.
     * $D_0$ is both the shear stiffness integral (Eq. 11) and the
       displacement scale $1000\,qL^3/(48E_1I_0)$ (§5). Two dimensionless
       deflections ($w(0.5L)/(2R_o)$ in §4, $w(0.5L)/D_0$ in §5) and two
       frequency parameters ($\sqrt{\rho/G}$ in §4, $\sqrt{\rho_1/E_1}$
       in §5) are used.
     * $L_0$ in $\tau=tv/(L+L_0)$ is never defined; the stage division
       points of §5.2.3 imply $L_0=d$.
     * §5.2.2 cites "Fig. 8" for the inner-radius study, which is
       Fig. 11.
     * Table 2: the top-left cell reads "$L/R_o=10$" while the first
       column lists 10 and 20/3, whose meaning is not stated (not
       $L/(R_o-R_i)$, which would be 15 for $R_i/R_o=1/3$).
     * Table 4 caption gives "$R_i=1$" without unit.
     * §5.2.1 calls the Type I/Type II difference "slightly larger" and
       concludes "greatly improved resistance" in the same sentence.
     * Table 3 shows $n=4$ and $n=6$ identical to four digits, so "n=6
       would be the best choice" is conservative, not shown better; the
       +0.3% and +0.4% offsets from the exact solution do not shrink with
       $n$.
     * §1 claims "the first attempt" for FG porous tubes under moving
       distributed loads; not verified.
     * Reader's check: the Table 1 closed forms agree with the
       generalised-load integral, and the 8.24% and 3.20% drops agree
       with Table 4 (0.1031 to 0.0946 and to 0.0998).
     * Reference list: [2] and [41] are the same work (Wang & Wu 2016,
       Acta Astronaut. 127:171), as are [27] and [48] (Zhong et al. 2016,
       Appl. Math. Model. 40:7601); [36] prints a stray "94" in the page
       field; [13] prints the journal as "Aero. Sci. Technol.".
   * **Reference list.** 49 printed entries ([1]–[49]), matching the
     Crossref reference count; two pairs are duplicates (above), so 47
     distinct works.
