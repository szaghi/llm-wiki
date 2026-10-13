---
type: Source
title: "Truelove et al. (1997) — The Jeans Condition: A New Constraint on Spatial Resolution in Simulations of Isothermal Self-gravitational Hydrodynamics"
description: "Origin of the Jeans condition: in multiple-grid simulations of isothermal self-gravitating collapse, discretization errors on scales above the Jeans length grow into artificial fragments; with a Jeans number (cell size over Jeans length) kept at or below 0.25 they did not in the authors' Gaussian-cloud tests, and resolving the Jeans length is stated as necessary but not in general sufficient for convergence."
resource: "doi:10.1086/310975"
source_kind: paper
authors: [Truelove J.K., Klein R.I., McKee C.F., Holliman II J.H., Howell L.H., Greenough J.A.]
year: 1997
venue: "Astrophys. J. Lett. 489:L179–L183"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1997-ApJL-Truelove-101086310975.pdf"
tags: [self-gravity, amr, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A Letter introducing the **Jeans condition**. With a new 3D AMR code for
isothermal self-gravitational hydrodynamics, built on Berger–Colella AMR
and not named here (its methods are deferred to the companion paper,
cited as "submitted", ApJ 495:821, 1998), the authors show that
discretization errors can grow into fragments in multiple-grid
simulations of isothermal collapse. They call this **artificial
fragmentation**. They define the Jeans number as the cell size over the
Jeans length. In four runs of the unperturbed Boss (1991) Gaussian cloud
they keep it below 0.5, 0.375, 0.25 and 0.125, and they find that 0.25 or
less avoids the growth of numerical perturbations into fragments.
Resolving the Jeans length is stated as "a necessary (but not, in general,
sufficient) condition for convergence". They also show that the
Burkert & Bodenheimer (1996) fixed-grid runs, which arrested collapse with
artificial viscosity, violated the condition and fragment even without
their seed perturbation.

# Key claims

1. **Jeans length** (§1, eq. 1): $\lambda_{\mathrm J} = (\pi c_s^2/G\rho)^{1/2}$,
   with $c_s$ the sound speed. Perturbations on larger scales are
   unstable (Jeans 1902, 1928).
2. **Mechanism** (§1, §2). Discretization errors are "most strongly
   correlated at the scale of the spatial resolution". Errors correlated
   on scales larger than $\lambda_{\mathrm J}$ grow by the physical Jeans
   instability, so the seed is numerical but the growth is physical. The
   authors set this apart from a purely numerical instability such as a
   Courant violation. Resolving $\lambda_{\mathrm J}$ puts cell-scale noise
   in the thermally damped range of wavelengths.
3. **Jeans number** (§2, eq. 2): the cell size over the Jeans length, "a
   dimensionless measure of the resolution"; it is $1/N_{\mathrm J}$.
4. **Threshold** (§2, Figs. 2–3): "use of $J_{\max} \le 0.25$ avoids the
   growth of numerical perturbations into fragments", i.e.
   $N_{\mathrm J} \ge 4$. The paper never states it as a cell count. The
   abstract and Conclusion 2 say "below 0.25"; the body says "≤ 0.25".
5. **Necessary, not sufficient** (abstract, §2, §4): "resolution of
   $\lambda_J$ is a necessary (but not, in general, sufficient) condition
   for convergence"; "particularly as the cloud becomes nonisothermal, the
   additional physics may demand resolution of yet smaller scales".
6. **Scope as stated** (§2): "a valid constraint for any calculation made
   with a code employing multiple grids or rezoning", evaluated with "the
   actual values of the density and temperature at each spatial point and
   at all times during the calculation". The paper's restriction is to
   isothermal gas; it does not restrict the condition to gas that is
   bound or collapsing. It rejects estimates from a fixed minimum
   temperature and the box-averaged density (Owen & Villumsen 1997) as "a
   gross underestimate of the required resolution".
7. **Enforcement by AMR** (§2, Fig. 1): the Jeans number is computed in
   every cell at every step, and grids 4 times finer are inserted wherever
   it reaches the threshold, "immediately reducing $J$ there by a factor
   of 4". Runs start at 32 cells per cloud radius (Jeans number 0.05).
   Perturbations also grow as they are advected into finer grids, and
   coarse-to-fine interpolation at rezoning seeds errors (§2).
8. **Cost** (§2): collapse over 9 orders of magnitude in density with 10
   cells across the final cloud radius would need more than $10^{12}$
   cells on one uniform grid.
9. **Artificial viscosity** (§4): used to arrest collapse at a fixed finest
   resolution, it leaves $\lambda_{\mathrm J}$ unresolved; in Burkert &
   Bodenheimer (1996) the maximum Jeans number reached 2.39 (512 cells per
   radius) and 3.65 (2048), and the results "cannot be confirmed with a
   convergence study". Burkert & Bodenheimer (1993) had speculated that
   fragmentation might be numerical where the Jeans length falls below
   one cell; this paper tightens that to 0.25.
10. **No fragmentation of the filament** (§3): the perturbed, isothermal,
    inviscid cloud collapses to a filamentary singularity without
    fragmenting, as Inutsuka & Miyama (1992, 1997) predict.

# Tests

All runs use one code, isothermal, with refinement ratio 4. The hydro
scheme and gravity solver are not described in the Letter.

1. **Burkert–Bodenheimer reproduction** (§2). With AMR held to their
   static grids, their fragmentation is reproduced, and it recurs without
   the seed perturbation. Bodenheimer reproduced the artificial
   fragmentation with their own code (private communication).
2. **Unseeded Gaussian cloud** (§2, Figs. 2–3). The Boss (1991) cloud:
   $1\,M_\odot$, radius $5\times10^{16}$ cm, solid-body rotation
   $10^{-12}$ rad s⁻¹, Gaussian density with central value
   $10^{-16.8}$ g cm⁻³ and scale radius 0.58 of the cloud radius, sound
   speed 0.19 km s⁻¹; the usual 10% $m = 2$ seed is omitted. Thresholds
   0.5, 0.375, 0.25, 0.125. At a maximum density of about
   $10^{-9.5}$ g cm⁻³, artificial fragmentation is "striking" at 0.5 and
   0.375 and "much more subtle" at 0.25 and 0.125. A perturbation measure
   (Fig. 3) grows by orders of magnitude at 0.5 and 0.375 and stays small
   at 0.25 and below (values only plotted). Maximum density, not time,
   serves as the clock, because finer runs reach the singularity sooner.
3. **Seeded cloud** (§3, Fig. 4). Threshold 0.5 gives a binary, 0.25 a
   single bar; a run with doubled initial resolution (threshold 0.125)
   gives the single bar only, so the binary is "a resolution-dependent
   numerical artifact".
4. **Burkert–Bodenheimer run repeated** (§4, Fig. 5). Threshold 0.25 is
   enforced up to 512 cells per radius and then refinement stops. Seeded
   and unseeded runs fragment alike, so the seeded result is "a
   convolution of physical effects with significant numerical ones".

The evidence is morphological plus one perturbation measure: one problem
family, one code, no error norms.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\lambda_J$ | $\lambda_{\mathrm J}$ | Jeans length, same formula |
| $c_s$, $\rho$, $G$ | $c_s$, $\rho$, $G$ | isothermal sound speed |
| $\Delta x$ | $h$ | cell size |
| $J \equiv \Delta x/\lambda_J$ | $1/N_{\mathrm J}$, "Jeans number" in words | $\mathbf J$ is the current density in the registry |
| $J_{\max}$ | the threshold on $1/N_{\mathrm J}$, in words | $J_{\max} \le 0.25$ is $N_{\mathrm J} \ge 4$ |
| $R_N$ ($\Delta x = R/N$) | "N cells per cloud radius", in words | registry $N$ counts cells per dimension of a test grid |
| $R$, $R_1$, $\rho_c$, $\Omega$, $m$ | in words | Gaussian-cloud parameters |

# Pages created or updated

* Updated [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md):
  the origin section, the necessary-not-sufficient wording, and an open
  contradiction on the criterion's scope.
* Updated [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
  Jeans refinement as stated in the original.

# Citations

1. Truelove J.K., Klein R.I., McKee C.F., Holliman II J.H., Howell L.H.,
   Greenough J.A. (1997), Astrophys. J. 489:L179–L183,
   doi:10.1086/310975. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1997-ApJL-Truelove-101086310975.pdf`.
   * **Version read.** The published Letter (5 text pages and 3 colour
     plates with Figs. 2, 4, 5).
   * **Identity.** Checked on Crossref: title, the six authors (the fifth
     is L. H. Howell, which a citing source prints as "J. H."), vol. 489,
     issue 2, pp. L179–L183, issued 1997-11-10.
   * **How it was read.** Text extraction; equations 1–2 and all numbers
     checked on rendered pages, because the text layer substitutes
     symbols. The colour plates were read from their captions and the
     text; Fig. 3 values are only plotted.
   * **Recorded as printed.** "Below 0.25" (abstract, Conclusion 2) against
     "≤ 0.25" (body). §3 places the single bar "on the left", while the
     Fig. 4 caption puts it in the right panel.
   * **Reference list:** 16 entries; no article titles printed (ApJ
     style). The self-citation "Truelove et al. 1997, ApJ, submitted"
     (seven authors, with Woods) is the companion paper `truelove-1998`
     (ApJ 495:821), not this Letter. Berger & Colella (1989), Burkert &
     Bodenheimer (1993), Jeans (1902) and Richtmyer & Morton (1967) land
     on existing entries by venue. The bibliography's title and author
     list for this paper were corrected from page 1.
