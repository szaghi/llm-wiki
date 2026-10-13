---
type: Source
title: "Fryxell et al. (2000) — FLASH: An Adaptive Mesh Hydrodynamics Code for Modeling Astrophysical Thermonuclear Flashes"
description: "Code paper of the first version of FLASH: PARAMESH block-structured AMR (8-cell blocks with four guard cells, oct-tree, 2:1 level jumps, Morton-curve load balancing, fine-flux sums at coarse–fine faces, one global time step, Löhner refinement), split direct-Eulerian PPM from PROMETHEUS with a two-shock Riemann solver and a Colella–Glaz general EOS, gamma-law, Nadyozhin and Helmholtz EOS, α-chain networks with a Bader–Deuflhard integrator, a hydrodynamic test suite and scaling on the ASCI machines with an AMR-versus-uniform crossover."
resource: "doi:10.1086/317361"
source_kind: paper
authors: [Fryxell B., Olson K., Ricker P., Timmes F.X., Zingale M., Lamb D.Q., MacNeice P., Rosner R., Truran J.W., Tufo H.]
year: 2000
venue: "Astrophys. J. Suppl. 131:273–334"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2000-ApJS-Fryxell-101086317361.pdf"
tags: [software, hydro, amr, reconstruction, riemann-solver, equation-of-state, verification, performance, scaling]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The code paper of [FLASH](/software/flash.md), in its "first version"
(Abstract, §9): a modular, parallel (MPI, single program multiple data)
Fortran code for compressible reactive hydrodynamics, built for X-ray
bursts, classical novae and Type Ia supernovae (§1). It couples the
PARAMESH block-structured [AMR](/methods/adaptive-mesh-refinement.md)
library (§2) to a directionally split, direct-Eulerian
[PPM](/methods/ppm.md) solver inherited from PROMETHEUS, with contact
steepening, flattening, a two-shock Riemann solver and the Colella–Glaz
extension to a general equation of state (§3). It ships a gamma-law, the
analytic Nadyozhin and the tabulated Helmholtz-free-energy
electron–positron EOS (§4), and hard-wired nuclear networks integrated by
a variable-order Bader–Deuflhard method with a sparse direct solver (§5).
It describes the module architecture and the `setup` build system (§6), a
hydrodynamic test suite (§7) and scaling on the three ASCI machines, with
the refinement depth and refined fraction at which AMR beats a uniform
grid (§8). The Fig. 22 caption names "FLASH 1.5" as "the current
development version"; the paper never prints "FLASH 1.0".

# Key claims

Equations below are in the [registry](/notation.md) notation (see the
Notation map).

1. **AMR family** (§2). PARAMESH (MacNeice et al. 1999, 2000), "a package
   of FORTRAN 90 subroutines", is classed as **block-structured AMR**,
   "similar to" the bisection tree of De Zeeuw & Powell (1993), and
   contrasted with Berger-style overlapping or rotated subgrids ("very
   complex and has proven to be very difficult to parallelize") and with
   Khokhlov's (1997) cell-based tree (irregular memory referencing).
2. **Blocks and guard cells** (§2, Figs. 1, 27). Each block holds the same
   number of cells, $N_{\mathrm b} = 8$ per direction in FLASH, with
   $n_{\mathrm g} = 4$ guard cells because PPM "requires four guard cells
   at each spatial boundary"; both are adjustable PARAMESH parameters. A
   refined block is halved in each direction ($r_{\mathrm{ref}} = 2$) into
   2, 4 or 8 children of the same cell count, nested in the parent. FLASH
   "uses only cell-centered data". The memory overhead of identical blocks
   is "rarely more than about 30%".
3. **Guard-cell filling** (§2). Copies from same-level neighbours; at a
   refinement jump "The FLASH code employs quadratic interpolation for the
   guard cell filling operation". Whether the interpolation is
   conservative or limited is not stated. Each block then advances
   independently.
4. **Tree, nesting and load balance** (§2, Figs. 2–3). A fully linked
   oct- or quad-tree (parent, children, same-level neighbours, each as
   local id and processor); leaves hold the solution; "a jump of no more
   than one refinement level across adjacent blocks". After a change of
   refinement, blocks are redistributed along a work-weighted Morton
   space-filling curve (after Warren & Salmon 1993): keys by
   bit-interleaving the integer block coordinates, a parallel bitonic sort
   of the keys only, then equal-work cuts; data move after the sort.
5. **Flux conservation** (§2, Fig. 4). At a refinement jump the fine-face
   fluxes of mass, momentum, energy and composition are summed and replace
   the coarse-face flux, printed $F = [f_1 + f_2 + f_3 + f_4]$ in 3D. The
   paper says neither whether the sum is area-weighted nor whether fluxes
   or flux times area are summed.
6. **No subcycling** (§2). PARAMESH can advance levels with their own
   steps, but "The FLASH code does not currently take advantage of this
   capability of PARAMESH": one step on all levels. Reasons against
   per-level steps: extra memory for temporary solution copies, and a
   forced ordering of block advances that "can have a damaging effect on
   load balance"; reasons for: accumulated numerical diffusion from many
   fine steps on coarse blocks (with a counter-argument) and saved work.
   No measurement.
7. **Refinement criterion** (§2, eqs. 1–3). Löhner's (1987) normalized
   second derivative; in 1D (eq. 2)
   $$\frac{\vert u_{i+1} - 2u_i + u_{i-1}\vert}{\vert u_{i+1} - u_i\vert + \vert u_i - u_{i-1}\vert + 0.01\left(\vert u_{i+1}\vert + 2\vert u_i\vert + \vert u_{i-1}\vert\right)},$$
   the term with coefficient 0.01 filtering small ripples. A block is
   refined if the maximum over its interior plus a halo two guard cells
   wide exceeds 0.8 and derefined below 0.2, evaluated "defaulting to once
   every four time steps" on density, pressure and temperature. The test
   is local and dimensionless; the module is user-replaceable; a
   Richardson (Berger–Colella) test is only under consideration.
8. **Hydrodynamics lineage** (§3). Based on PROMETHEUS (Fryxell, Müller &
   Arnett 1989), "a modified version of the PPM" of Colella & Woodward
   (1984), in the **direct Eulerian** form (Lagrange-plus-remap "may be
   implemented in future versions"); Euler equations with a gravity
   source and passive species mass fractions (eqs. 4–16).
9. **Stated order** (§3). "PPM is formally accurate to only second order
   in both space and time", with "the most critical steps ... performed to
   third- or fourth-order accuracy". Shocks spread over "one to two grid
   points"; steepened contacts stay within "one to two grid points, no
   matter how far they propagate".
10. **Interface interpolation** (§3.1.1, eqs. 20–26). A cubic with the
    correct zone averages, of "fourth-order accuracy": "The above
    equations retain their fourth-order accuracy even in the presence of
    nonuniform zoning." On a uniform mesh (eq. 25) the interface value is
    $\tfrac{7}{12}(u_i^n + u_{i+1}^n) - \tfrac{1}{12}(u_{i-1}^n + u_{i+2}^n)$.
    The average slope is limited as in MUSCL (eq. 26): the smallest of
    its own modulus and twice the moduli of the one-sided differences,
    with its own sign, and zero unless
    $(u_{i+1}^n - u_i^n)(u_i^n - u_{i-1}^n) > 0$. Reconstructed variables:
    $\rho$, the three velocity components, $p$, the energy index $\gamma$
    and the mass fractions.
11. **Contact steepening** (§3.1.2, eqs. 33–42). Five conditions
    (second-derivative sign change, large third derivative, first and
    third derivatives of opposite sign, large density jump, small pressure
    jump); a relative density jump below 0.01 is noise (eq. 37); a
    relative pressure jump above $0.1\gamma$ times the relative density
    jump marks a shock (eq. 39); the weight is
    $\max\{0, \min[20(\tilde\eta - 0.05), 1]\}$ in the normalized third
    derivative $\tilde\eta$ (eq. 40). Applied to density **and
    composition**. The constants were "determined empirically ... any
    changes should be performed with extreme caution"; under-resolved
    steep smooth gradients can turn into stair-steps. A contact after 320
    zones is 2 zones wide with steepening, 6 without (Figs. 7–8).
12. **Flattening** (§3.1.3, eqs. 43–50). Steepness
    $(p_{i+1} - p_{i-1})/(p_{i+2} - p_{i-2})$ (about 1/2 smooth, 2/3 for a
    two-zone shock, 1 for a one-zone shock); coefficient
    $\max\{0, \min[1, 10(\text{steepness} - 0.75)]\}$ (eq. 45), set to 0
    where the relative pressure jump is below 1/3 (eq. 46) or the flow
    expands, $v_{x,i+1} - v_{x,i-1} > 0$ (eq. 47); the larger of the
    zone's and its lower-pressure neighbour's value is taken ($i+1$ when
    $p_{i+1} - p_{i-1} < 0$, else $i-1$; eq. 48); edge values become the coefficient times $u_i^n$ plus one
    minus the coefficient times the edge value (eqs. 49–50): **0 leaves
    them unchanged, 1 gives first-order Godunov**.
13. **Monotonicity** (§3.1.3, eqs. 51–53). At an extremum both edges take
    the zone mean (eq. 52); on overshoot
    $u^+_{i-1/2} \to 3u_i^n - 2u^-_{i+1/2}$ when
    $(u^-_{i+1/2} - u^+_{i-1/2})\left[u^+_{i-1/2} - (3u_i^n - 2u^-_{i+1/2})\right] < 0$,
    and symmetrically (eq. 53).
14. **Interface states and Riemann solver** (§§3.1.5–3.1.6, eqs. 54–85).
    Characteristic domain-of-dependence averages of the parabolae with
    the Colella–Woodward corrections, zeroed for outgoing
    characteristics. Both waves are approximated as shocks ("accurate to
    third order in the size of the entropy jump", "small error at
    rarefactions"); the star pressure by Newton–Raphson: "Reasonably
    strong shocks can now be handled adequately with two to three
    iterations" (simple linear iteration may need 10 or more); inside a
    rarefaction, linear interpolation between head and foot.
15. **General EOS in the solver** (§3.1, eq. 17; §3.1.7, eqs. 86–91). Two
    adiabatic indices after Colella & Glaz (1985): the energy index
    $\gamma = p/(\rho e) + 1$ (eq. 8) and $\Gamma_1$ (eq. 17); a secant
    iteration replaces Newton because EOS derivatives "may not be readily
    available".
16. **Update** (§3.1.8, eqs. 92–97). Conservative, in area and volume
    form; the gravity source is time-centred as the average of the old-
    and new-time products of density and acceleration (eqs. 93, 96; read
    from the text layer only). Interface mass fractions are clipped to
    $[0, 1]$ and divided by their sum: "Not applying this correction ...
    can have disastrous effects, especially for reactive flows."
17. **Dimensional splitting** (§3.2, eqs. 98–99). Strang-type splitting
    with the sweep order reversed every step (xy then yx; xyz then zyx),
    "second-order accuracy in time"; a nine-point stencil per sweep, hence
    four guard cells. A Lapidus (1967) multidimensional artificial
    viscosity, "Typically a coefficient of 0.1", "not required to
    stabilize shocks", reduces stair-casing of diagonal shocks. Only
    "assuming that the CFL number is less than 1, as required for
    numerical stability" (§3.1.5); the Courant number of the tests is not
    printed.
18. **EOS** (§4). Every EOS takes temperature, density, mean mass number
    and mean charge and returns pressure, energy, entropy and their
    derivatives (eq. 100). Nadyozhin: maximum error about 0.1 %, typical
    0.01 % or less. **Helmholtz** (recommended): biquintic Hermite
    interpolation of the electron–positron Helmholtz free energy,
    thermodynamically consistent "to the limits of IEEE 64 bit
    arithmetic", typical error about $10^{-7}$, maximum about $10^{-5}$
    halfway between table points; table over $10^{-10}$ to $10^{11}$
    g cm$^{-3}$ in density times $Y_{\mathrm e}$ and $10^4$ to $10^{11}$ K,
    10 points per decade (211 × 71), about 1 MB, scaled by $Y_{\mathrm e}$
    (§4.3.2); "about twice as fast as the Nadyozhin EOS" (Fig. 19);
    temperature by Newton–Raphson "in two to four iterations" (§4.3.3).
    Error budget (§4.4): the hydro is accurate to "about two or three
    digits" with strong shocks, "perhaps to five or six digits" in smooth
    flow, and the EOS error should stay below that.
19. **Nuclear burning** (§5). Hard-wired networks: 7-isotope α-chain, the
    13-isotope α-chain plus heavy-ion network, a 19-isotope network and a
    17-isotope hydrogen-burning network; the 13-isotope energy generation
    is within about 30 % of large networks. Integrator: variable-order
    Bader–Deuflhard semi-implicit extrapolation (fifth to fifteenth
    order, accuracy 1 part in $10^6$) with the MA28 sparse direct solver;
    operator split from the hydro, sub-stepping internally (eqs. 182–191).
20. **Architecture** (§6, Figs. 21–23). Modules and submodules with
    inherited sources and stubs; a `setup` script links sources, with
    problem and system directories overriding by filename; runtime
    parameters as `variable = value`; data shared through common blocks,
    Fortran 90 derived types announced. Split FCT and unsplit PPM appear in
    Fig. 22 "for illustrative purposes only; they are not present in the
    current version".
21. **Scaling** (§8). Uniform-grid FLASH (one block per processor) scales
    nearly ideally in strong scaling until guard-cell communication
    competes (Fig. 40); AMR at fixed work scales worse, because the ratio
    of guard-cell communication to computation grows (Fig. 41). Weak
    scaling: ASCI Red "nearly perfect scaling up to 1024 processors when
    one processor per node is used"; on Nirvana the time rises "by more
    than a factor of 2 between 64 and 256 processors" (Figs. 42–44).
22. **AMR against uniform** (§8.4, Figs. 45–48). "Beyond a refinement
    level of six (corresponding to a uniform mesh with 512 cells per
    side), the AMR code is faster than the uniform mesh code"; "at most
    60% of the mesh in two dimensions, or 40% in three dimensions, can be
    maximally refined before the AMR overhead begins to outweigh the speed
    advantage".

# Tests

All §7 tests use the hydro module alone with a dimensionless gamma-law
EOS; reactive and general-EOS tests are deferred to "a subsequent paper".
The paper counts levels from 1 (one 8-cell block per direction), so 2
levels is $h = 1/16$ and 9 levels $h = 1/2048$ on a unit domain (§7.5).

1. **Advection** (§7.1, Fig. 24). 2D square and Gaussian pulses at 0°
   and 45°, $t = 0.4$, 2, 4 and 6 levels. Spreading of about one zone per
   side; at 4 levels the Gaussian loses "about 50%" of its amplitude, at 6
   levels it keeps "93% of its initial value"; no oscillations. Advice:
   refined zones "at least a factor of 5–10 smaller than the narrowest
   features of interest".
2. **[Sod shock tube](/benchmarks/sod-shock-tube.md)** (§7.2, Figs.
   25–27). Standard states, $\gamma = 1.4$, 2D, 6 levels (effective
   $256^2$), $t = 0.2$: discontinuities in 2–3 zones, errors of 1–2 % near
   the contact and in the rarefaction, no oscillation. Along the diagonal,
   "slightly larger oscillations (on the order of a few percent)" at the
   rarefaction tail and contact, attributed to the directional splitting.
   Sod "is not a very discriminating test for modern codes" (§7.3).
3. **Strong shock tube** (§7.3, Fig. 28). Densities 10 and 1, pressures
   100 and 1, $\gamma = 1.4$, 1D, 8 levels, $t = 0.4$: "virtually
   indistinguishable from the analytical solution" (no norm).
4. **[Sedov blast](/benchmarks/sedov-taylor-blast-wave.md)** (§7.4, Figs.
   29–31). Unit energy in 3.5 finest cells, 2D cylindrical at 2–8 levels,
   $t = 0.05$: the shock in about two zones; 90 % of the swept mass in
   4 / 17 / 69 zones at 4 / 6 / 8 levels; the centre refined by a
   temperature criterion. 3D at 5 levels: the analytic peak (about 1.5
   zones wide) is missed and rms deviations reach "up to 40%" in density
   and velocity in the derefined region behind the shock.
5. **Woodward–Colella interacting blast waves** (§7.5, Figs. 32–33).
   Reflecting walls; reference solution at 10 levels; L1 self-convergence
   at $t = 0.038$ for 2–9 levels is "only linear", and "Woodward & Colella
   (1984) found that only PPM achieved even linear convergence"
   ([Woodward & Colella (1984)](/sources/woodward-1984.md)).
6. **Emery Mach 3 step** (§7.6, Figs. 34–37). No corner treatment: an
   entropy error at the corner, an artificial second Mach stem at low
   resolution, and Kelvin–Helmholtz growth behind the Mach stem that "does
   not disappear with increasing resolution". With thresholds 0.8/0.2 the
   slip line near the Mach stem is not refined; 0.6 refines it
   everywhere: "refinement criterion and thresholds need to be carefully
   considered for any particular problem".
7. **Shock through a forced refinement jump** (§7.7, Figs. 38–39). A
   Sedov front crossing a static jump from 7 to 6 levels: a broader front
   and lower peak density on the coarse side, and a **reflected shock** at
   the jump, stronger the smaller the angle between the shock direction
   and the jump; head-on crossing errors "appear small and well behaved".
   Forced jumps "should only be used for regions ... not critical".
8. **Performance** (§8): ASCI Nirvana (SGI Origin 2000), ASCI Red
   (Pentium II Xeon) and Blue Pacific (PowerPC 604e); results in claims
   21–22. No zone-cycles-per-second figure is printed.

**Batch 9.** The interacting-blast-wave run now has a benchmark page, [interacting blast waves](/benchmarks/interacting-blast-waves.md); Woodward & Colella's finest-pair rates are PPMDE 1.07, PPMLR 0.98, all others ≤ 0.85 (Table I), which agrees with "only PPM achieved even linear convergence". On the Emery step, Woodward & Colella (p. 131) give a corner treatment (four plus two zones reset to the corner entropy and enthalpy) whose absence produces the numerical boundary layer and spurious Mach reflections that FLASH reports.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\rho$, $u, v, w$, $P$ | $\rho$, $\mathbf v$, $p$ | |
| $\epsilon$ (specific internal energy) | $e$ | **collision**: the paper's $\epsilon$ is also the Löhner filter constant (0.01), written as a number here |
| $E$ (specific total energy) | $E/\rho$ | the paper's $E$ is per unit mass |
| $\gamma$ (eq. 8) | $\gamma$ | used as the energy index $p/(\rho e) + 1$ also for non-ideal EOS |
| $\Gamma$ (eq. 17) | $\Gamma_1$ | |
| $\Gamma$ (eq. 167, plasma coupling) | in words | **collision** with eq. 17's $\Gamma$, flagged by the paper |
| $c$ (sound speed) | $c_s$ | **collision**: $c$ is the speed of light |
| $C = \rho c$ | $\rho c_s$ | Lagrangian sound speed |
| $X_l$ (mass fractions) | in words | the registry has no mass-fraction symbol; $l$ is the refinement level |
| $\bar A$, $\bar Z$, $Y_i$ | in words | mean mass number, mean charge, molar abundances |
| $Y_e$ | $Y_{\mathrm e}$ | |
| $\mathbf g$ | $\mathbf g$ | external field only in this version |
| $\langle U\rangle_i^n$ | $u_i^n$ | zone average |
| $U_{L,i}$, $U_{R,i}$ | $u^+_{i-1/2}$, $u^-_{i+1/2}$ | edge values of zone $i$ |
| $E_i$ (Löhner error) | in words | **collision** with the registry $E$ |
| CTORE, CTODE | in words (0.8, 0.2) | refine and derefine thresholds |
| $\eta_i$, $F_i$, $S_p$ | in words | steepening weight, flattening coefficient, steepness; **collision**: $\eta_1$, $\eta_2$ are dual-energy thresholds |
| $nxb$ | $N_{\mathrm b}$ | 8 |
| guard cells | $n_{\mathrm g}$ | 4 |
| $N_{\mathrm{ref}}$ (levels, root = 1) | $l_{\max} = N_{\mathrm{ref}} - 1$ | registry $l = 0$ is the root |
| $\Delta x$ | $h$ | |
| $\mathsf J$ (network Jacobian) | in words | **collision** with the current $\mathbf J$ |
| $F$ (Helmholtz free energy) | in words | **collision** with the flux notation |

# Pages created or updated

* Created this Source page.
* Updated [FLASH](/software/flash.md): the first version from its code
  paper (architecture, AMR, hydro, EOS, burning, tests, performance), the
  page's open points answered, and the "has not ingested a FLASH code
  paper" sentence replaced.
* Updated [PPM](/methods/ppm.md): FLASH's PPM as printed, the flattening
  convention checked, and an open contradiction on the order of the
  interface interpolation on non-uniform meshes.
* Updated [Adaptive mesh refinement](/methods/adaptive-mesh-refinement.md):
  the FLASH row, refluxing, prolongation, ghost layers, Löhner thresholds,
  Morton balancing, cost and crossover, and the effects of refinement.
* Updated [Unsplit Godunov integrators](/methods/unsplit-godunov-integrators.md):
  FLASH as a split scheme, with its diagonal Sod finding.
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md) (batch-8 section: FLASH's Sod and strong shock tube runs).
* Updated [Sedov–Taylor blast wave](/benchmarks/sedov-taylor-blast-wave.md) (batch-8 section: FLASH's Sedov runs and the level-jump reflection).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (batch-8 section: the two-shock solver of FLASH's first version).
* Updated [General equations of state in Godunov codes](/methods/general-equation-of-state.md) (batch-8 section: FLASH's three EOS).

# Citations

1. Fryxell B., Olson K., Ricker P., Timmes F.X., Zingale M., Lamb D.Q.,
   MacNeice P., Rosner R., Truran J.W., Tufo H. (2000), Astrophys. J.
   Suppl. 131:273–334, doi:10.1086/317361. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2000-ApJS-Fryxell-101086317361.pdf`.
   * **Version read.** The published journal version (publisher PDF,
     62 pages; received 1999 November 9, accepted 2000 April 13). Not a
     preprint.
   * **Identity.** Checked on Crossref: title, the ten authors, ApJS vol.
     131, issue 1, pp. 273–334, published 2000 November; agrees with
     page 1.
   * **How it was read.** Text layer for the prose (ligatures garbled).
     Every equation is garbled in the text layer; eqs. 1–3, 26 and 33–53
     were read from rendered pages. Eqs. 54–97, 100–170 and 172–191 were
     read from the text layer only and are summarized, not reproduced; the
     gravity time-centring of eqs. 93 and 96 is from the text layer.
     Figures 24–48 (test plots and scaling curves) were not digitized:
     only numbers printed in the text are used.
   * **Recorded as printed.** (a) Eq. 1 prints the second difference as
     $(u_{i+1} + 2u_i + u_{i-1})/h^2$, with $+2u_i$ (reader's reading: a
     sign misprint; eq. 2 has $-2u_i$). (b) Eq. 3, the multidimensional
     Löhner estimator, squares the denominator but not the numerator of a
     square-rooted sum (reader's reading: an apparent misprint; not
     corrected). (c) §7.7 prints the front at "~0.92 cm along the x-axis"
     (the coarse side) and "~0.88 cm along the y-axis", then concludes that
     "the speed of the shock front is slower in the more coarsely refined
     regions"; the numbers as printed put the coarse-side front farther
     out. Not resolved. (d) The Courant number of the tests is not
     printed.
   * **Reference list:** 71 entries, no DOIs. Berger & Colella (1989),
     with the co-author printed "Collela", lands on `berger-1989`. Timmes
     & Arnett (1999), printed "ApJS, 125, 294" (its last page; Crossref
     125:277–294), is `timmes-1999`; Timmes (1999), ApJS 124:241, is
     `timmes-1999-b`; Timmes & Swesty (2000), ApJS 126:501, is
     `timmes-2000`; Timmes et al. (2000), ApJ 543:938, is `timmes-2000-b`;
     Timmes, Hoffman & Woosley (2000), ApJS 129:377, is `timmes-2000-c`.
     Five software packages (DAGH, AMR++, SAMRAI, AMRCLAW, HAMR) are
     printed without venue. Bibliography: 2314 entries.
