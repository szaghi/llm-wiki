---
type: Source
title: "Mungiguerra et al. (2018) — Effects of solar panels on Aerodynamics of a small satellite with deployable aero-brake"
description: "DSMC (DS3V 2.6) study of a low-Earth-orbit small satellite with a deployable 45-degree aero-brake at 150 km, showing that deployable solar panels remove intermediate equilibria and stabilize the closed configuration but halve the drag-modulation ratio (8.75 to 4.06); off-domain for this bundle except for its account of DSMC practice and Maxwell gas-surface modelling."
resource: "doi:10.1016/j.actaastro.2018.06.040"
source_kind: paper
authors: [Mungiguerra S., Zuppardi G., Spanò Cuomo L., Savino R.]
year: 2018
venue: "Acta Astronaut. 151:456–466"
local_file: "/home/stefano/papers/mosaic/plasma-propulsion-simulation/2009_Crossref_Physics_of_Fluids_Bird_Accuracy_and_efficiency_of_the_sophisticated_direct_simulati.pdf"
tags: [dsmc, wall-interaction]
timestamp: 2026-10-14T00:00:00Z
---

# Summary

A DSMC study, with Bird's DS3V version 2.6, of the aerodynamics of a small
satellite with an umbrella-like deployable 45° half-cone aero-brake in low
Earth orbit, at 150 km altitude and 7800 m/s, for angles of attack 0–180° in
10° steps. Five configurations are compared: aero-brake at the front or in
the middle without panels, front with eight deployable solar panels,
closed with and without panels. A middle aero-brake is an order of
magnitude more stable than a front one but is rejected on engineering
grounds. Panels remove the intermediate equilibria of the open front
configuration and stabilize the closed one, but more than double the
closed-brake drag, cutting the open-to-closed drag ratio from 8.75 to 4.06.
A sensitivity study varies the specular fraction of the Maxwell
gas–surface model from 0 to 0.3.

**Scope.** The paper is rarefied-gas satellite aerodynamics with no plasma,
thruster or electric propulsion. Under the bundle's scope rule it
contributes only to [DSMC](/methods/dsmc.md) and to
[gas–surface interaction models](/methods/gas-surface-interaction.md); its
aerodynamic results (drag, lift, stability derivatives, power estimates)
seed no concept page.

**File identity.** The archive file is named for Bird, Gallis, Torczynski &
Rader (2009), "Accuracy and efficiency of the sophisticated direct
simulation Monte Carlo algorithm…", Phys. Fluids 21:017103
(doi:10.1063/1.3067865), but page 1, the running headers and the PDF
metadata all identify this paper, which cites Bird et al. (2009) as its
ref. 26. Bird et al. (2009) is not in the archive.

# Key claims

1. **Regime** (§4): $\mathrm{Kn}\approx31$ on the 1.04 m aero-brake diameter
   at 150 km ($\lambda_{\mathrm{mfp}}\approx32$ m). Free-molecular flow
   starts at $\mathrm{Kn}=50$ (stated, citing Moss), so DSMC is preferred to
   Maxwell's free-molecular formulas to capture free-stream/re-emitted
   molecule interactions. Maxwell theory and DSMC are "perfectly
   equivalent" for ISS drag in fully free-molecular flow (stated, citing
   Zuppardi).
2. **Sophisticated DSMC** (§3, stated, attributed to Bird 2006, Bird et al.
   2009 and Gallis et al. 2009): collision and sampling cells with
   adaptation; nearest-neighbour collisions; automatic numbers of cells and
   molecules from memory and free-stream density; radial weighting for
   axisymmetric flows; an "optimal time step"; no repeated collisions of
   the same pair. DS3V displays, per collision cell, the ratio of mean
   collision separation to $\lambda_{\mathrm{mfp}}$, to be below 1, with 0.2
   suggested by Bird for an optimal run.
3. **Run quality** (§4, Tables 2a–2d): that ratio is 0.003–0.062; ratio of
   simulated to fluid-dynamic time 72–309; $3.88\times10^6$–$1.00\times10^7$
   simulated molecules; $2.34\times10^7$–$1.16\times10^8$ collisions.
   107 runs. No experimental validation (stated).
4. **Surface-model sensitivity** (§5.1, Tables 3–4): specular fraction
   0.1–0.3 changes the drag coefficient by 0.000–6.178% against fully
   diffuse; the zero-incidence stability derivative is $-9.51\times10^{-4}$,
   $-1.57\times10^{-3}$, $-9.64\times10^{-3}$, $-2.80\times10^{-3}$ deg$^{-1}$
   for specular fraction 0, 0.1, 0.2, 0.3. The paper concludes the surface
   model "does not influence strongly the coefficients" and uses the fully
   diffuse model thereafter.
5. **Configurations** (§5.2–5.3, Tables 5–6, Figs. 7–11): middle aero-brake
   forward derivative $-0.012$ deg$^{-1}$ against $-0.00092$ for the front
   one; panels on the closed brake give $-0.11$ deg$^{-1}$ forward (from
   $+0.011$, unstable, without); drag area at zero incidence about 1.75 m$^2$
   open, 0.2 m$^2$ closed without panels, slightly above 0.4 m$^2$ closed
   with panels.

# Models and numerics

* Boltzmann equation by DSMC, each simulated molecule standing for
  $10^9$–$10^{10}$ real ones (§3). Air with five neutral species (O$_2$,
  N$_2$, O, N, NO) and the Gupta–Yos–Thompson 23-reaction set. Full 3D,
  surface discretized by triangles; the service module is a cylinder in
  place of the real octagonal prism.
* Gas–surface: Maxwell model per triangle, specular fraction constant and
  independent of incidence angle, diffuse part fully accommodated to the
  wall temperature; fully diffuse baseline (§4, §5.1).
* Steady state judged when the time history of the number of simulated
  molecules becomes "jagged" within a standard-deviation band (§3, §4).
* Language, parallelism and run times not stated. No field, plasma or
  kinetic electron model.

# Tests and results

Key claims 3–5. No experiment; correctness rests on correct use of DS3V
(stated).

# Notation map

| Mungiguerra et al. (2018) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\lambda$, $\lambda_\infty$ | $\lambda_{\mathrm{mfp}}$ | |
| $\mathrm{Kn}_{\infty D}$ | $\mathrm{Kn}$ | based on the aero-brake diameter |
| mcs | words (mean collision separation) | DSMC quality metric |
| $N_m$ | words (number of simulated molecules) | registry has only $N_{\mathrm{ppc}}$ |
| molecules represented per simulated molecule | $W$ | |
| $r$, $f=1-r$ | words (specular and diffuse fractions) | **collision**: $r$ is the radial coordinate |
| $T_r$, $T_w$ | words (wall temperature) | |
| $\alpha$ | words (angle of attack) | outside the registry's scope |
| $C_D$, $C_L$, $C_{M_{cg}}$, $S_{\mathrm{ref}}$, $D$ | — | aerodynamic quantities outside the bundle's scope |

# Pages created or updated

Chunk 1 (2026-10-14) created every page of the bundle. This source is cited on:

* [Direct simulation Monte Carlo (DSMC)](/methods/dsmc.md)
* [Gas–surface interaction models](/methods/gas-surface-interaction.md)

# Citations

1. `~/papers/mosaic/plasma-propulsion-simulation/2009_Crossref_Physics_of_Fluids_Bird_Accuracy_and_efficiency_of_the_sophisticated_direct_simulati.pdf`
   (archive filename names Bird et al. 2009; content is this paper; md5
   94ea5c30ed4f8de964a54d1cea3eb14e, 11 pages).
   * **Version.** Publisher's typeset version of record (Elsevier, © 2018 IAA).
   * **Identity.** doi:10.1016/j.actaastro.2018.06.040, checked on Crossref
     (title, four authors, volume, pages): Acta Astronaut. 151:456–466,
     issue 2018-10; online 2018-06-19 (printed). Received 18 Mar 2018,
     revised 17 May 2018, accepted 17 Jun 2018.
   * **How it was read.** Text extraction, all sections; numbers from text
     and tables only, no figure digitization.
   * **Recorded as printed.**
     - §5.3 calls the zero-incidence stability derivative of the front
       aero-brake with panels "almost the same" as without, but Table 6
       gives $-0.0095$ against $-0.00092$ deg$^{-1}$; with Table 4's
       $-9.51\times10^{-4}$ for the same configuration, Table 6's value is
       probably a misprint of $-0.00095$.
     - §5.1 concludes a weak surface-model influence, but Table 4's
       stability derivative varies by a factor of about 10,
       non-monotonically, with the specular fraction; the conclusion holds
       for drag (Table 3).
     - Table 6: the closed-without-panels backward derivative 0.00089
       equals the front-open backward value; possible copy slip.
     - §4 calls the simulated time "about one order of magnitude higher"
       than the fluid time; Tables 2 give 72–309.
   * **Reference list:** 31 printed entries. Printed slips: ref. 14
     "Anigstem" (probably Anigstein); ref. 21 "ISBS" for ISBN; ref. 26
     "Phys. Fluids 21 (1) (2009) 12 017103", where "12" is the page count.
