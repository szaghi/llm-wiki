---
type: Source
title: "Ohlmann et al. (2016) — Hydrodynamic moving-mesh simulations of the common envelope phase in binary stellar systems"
description: "First AREPO moving-mesh simulation of the common-envelope dynamical spiral-in, with an HLLC-type solver on a Voronoi mesh, tree gravity, individual time steps and mass-targeted refinement, conserving energy to 3 % and angular momentum to 1 %, and attributing the Kelvin–Helmholtz instabilities it finds to the code's Galilean invariance."
resource: "doi:10.3847/2041-8205/816/1/L9"
source_kind: paper
authors: [Ohlmann S.T., Röpke F.K., Pakmor R., Springel V.]
year: 2016
venue: "Astrophys. J. Lett. 816:L9"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2016-ApJL-Ohlmann-1038472041-82058161l9.pdf"
tags: [software, hydro, self-gravity, conservation]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

An application Letter: the moving-mesh code AREPO
(Springel 2010) computes the dynamical spiral-in of a common-envelope
event, a 0.99 $M_\odot$ point-mass companion placed at the surface of a
2 $M_\odot$ red giant whose 0.4 $M_\odot$ core is replaced by a softened
gravitation-only particle. Numerical configuration (§2): HLLC-type Riemann
solver on a moving unstructured Voronoi mesh, the gradient estimate and
time integration of Pakmor et al. (2016) (second order for general mesh
motion), tree-based self-gravity, individual adaptive time steps,
mass-targeted refinement with a cell-radius cap near the core particle,
and an ideal gas with adiabatic index 5/3. With 1.8–2.7 million cells the
run conserves total energy to better than 3 % and angular momentum to
better than 1 % over about 120 d. The orbit shrinks to 4.3 $R_\odot$, about
8 % of the envelope is unbound, and large-scale Kelvin–Helmholtz
instabilities appear between spiral shocks; the authors attribute their
absence from earlier SPH and static-grid runs to SPH diffusion and to the
violation of Galilean invariance on static grids. No verification test
and no performance data are given.

# Key claims

1. **Scheme** (§2, ¶1). AREPO "solves the Euler equations on a moving,
   unstructured Voronoi mesh using an HLLC-type approximate Riemann
   solver. Self-gravity is included with a tree-based algorithm." The
   Pakmor et al. (2016) gradient estimate and time integration give
   "second order convergence also for general mesh motions" (stated; no
   data here).
2. **Individual time steps** (§2, ¶1). Only the cells requiring the
   smallest time steps are evolved on it; this "boosts the computational
   efficiency" (not quantified).
3. **Boundaries** (§2). Periodic, box side $3.3\times10^{14}$ cm; the run
   stops (about 120 d) when the first low-density tidal arm reaches the
   boundary; "no mass is lost during the simulation".
4. **Initial model** (§2, ¶2). MESA red giant (zero-age main-sequence mass
   2 $M_\odot$), mapped to mass-adaptive radial shells with a HEALPix
   distribution; core softened at $7.3\times10^{10}$ cm (about 1.0
   $R_\odot$) with the Springel (2010) spline. The procedure is deferred to
   "Ohlmann et al. (2015, in prep.)".
5. **Equation of state** (§2). Ideal gas, adiabatic index 5/3, "different
   from the MESA equation of state"; density, pressure and sound speed
   within 5 % in the envelope; internal energy deviates more because
   ionization is neglected.
6. **Relaxation** (§2). A damping term for several dynamical times; final
   core 0.38 $M_\odot$, envelope 1.60 $M_\odot$; envelope Mach numbers up to
   0.1; profiles stable for several dynamical times without damping.
   Envelope convection is not properly resolved.
7. **Resolution and refinement** (§2). About $1.8\times10^6$ cells at the
   start (mean cell mass $8.7\times10^{-7}\,M_\odot$) and $2.7\times10^6$ at
   the end ($5.8\times10^{-7}\,M_\odot$); target cell mass
   $8.4\times10^{-7}\,M_\odot$; within five softening lengths of the
   core particle the maximum cell radius is one tenth of the softening
   length. Smallest cells about $4.6\times10^9$ cm at the start and
   $8\times10^8$ cm at the end. The flow is resolved only outside one
   softening length.
8. **Energy-conservation requirement** (§2, footnote 6). "A resolution of
   about 10 cells per softening length is required to ensure energy
   conservation during the in-spiral"; because gravity and hydrodynamics
   are discretized differently, large potential-to-kinetic or internal
   conversions "can lead to substantial errors in the total energy, when
   the resolution is too low" (Evrard collapse, Springel 2010). Stated, not
   shown.
9. **Softening constraint** (§2). Softening lengths at most one fifth of
   the core–companion distance.
10. **Background** (§2, footnote 5). Background density
    $10^{-16}$ g cm$^{-3}$; the giant is resolved down to 0.002 g cm$^{-3}$.
11. **Resolution against earlier work** (§2). Ricker & Taam (2008, 2012):
    AMR cells of 0.3 $R_\odot$ for a 32 $R_\odot$ giant; Passy et al.
    (2012): SPH smoothing lengths 0.1 $R_\odot$, grid cells 1.7 and 3.4
    $R_\odot$ for an 83 $R_\odot$ giant.
12. **Conservation** (§2, §3, Fig. 2). Angular momentum error "below 1%";
    total energy "conserved to better than 3% during the whole run",
    although up to $1.5\times10^{47}$ erg (65 % of the total energy) is
    exchanged between potential and kinetic energy in one orbit.
13. **Galilean invariance** (§3, last ¶; §4). "The violation of Galilean
    invariance in conventional grid-based hydrodynamics codes (when
    altering the background velocity at the same resolution) suppresses
    Kelvin-Helmholtz instabilities on a static mesh" (Springel 2010,
    Fig. 33); AREPO is Galilean invariant. The absence of the instability
    in Passy et al. (2012) is attributed to SPH numerical diffusion and to
    the background velocity of the grid runs — "We suspect"; untested.
14. **Astrophysical result** (§3, Figs. 1–4). Separation 49 → about 4.3
    $R_\odot$; eccentricity 0.18 (0.08 in Ricker & Taam 2012); 0.1
    $M_\odot$ (about 8 %) unbound; mass-loss rate about 0.015 $M_\odot$
    yr$^{-1}$; a Solberg–Høiland analysis (eq. 1) finds unstable regions
    throughout the envelope.

**Tests.** None. The numerical evidence is internal to the production
run: the relaxed single star (within 5 % of MESA, Mach ≤ 0.1), the
conservation diagnostics (energy 3 %, angular momentum 1 %, no boundary
mass loss) and a stated, unshown resolution requirement. No second
resolution, no resolution study of the Kelvin–Helmholtz instability, no
hardware, run time, code version, throughput or scaling.

# Notation map

| Ohlmann et al. (2016) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$ | $\rho$ | |
| $\mathbf u$ (velocity), $v_r$, $v_\phi$ | $\mathbf v$; components in words | **collision:** registry $u$ is the conserved state |
| adiabatic index 5/3 (words) | $\gamma = 5/3$ | |
| $\mathbf g$ | $\mathbf g$ | gravitational acceleration |
| $h$ (softening length) | $r_{\mathrm{soft}}$ | **collision:** registry $h$ is the cell size |
| $s$ (specific entropy) | none (words) | **collision:** registry $s(u)$ is the source term |
| $c_p$ (specific heat at constant pressure) | none (words) | **collision:** registry $c_p$ is the GLM damping parameter |
| $j$ (specific angular momentum) | none (words) | close to the registry current density $\mathbf J$ |
| $\varpi$ (distance from the rotation axis) | none (words) | used only in eq. 1 |
| $a$ (semi-major axis) | none (words) | **collision:** registry $a$ is the scale factor |
| $e$ (eccentricity) | none (words) | **collision:** registry $e$ is the specific internal energy |

# Pages created or updated

* AREPO has no Software page: no AREPO method paper is ingested, and this
  application paper describes its numerics in one paragraph (batch-4 audit).
* Updated [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)
  (Galilean-invariance attribution, recorded as a qualification of the
  Katz et al. bulk-flow runs, not a contradiction).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2016-ApJL-Ohlmann-1038472041-82058161l9.pdf`.
   * **Version.** arXiv:1512.04529v1 [astro-ph.SR], 14 Dec 2015, 6 pages,
     4 figures, 1 equation (the "Draft version November 6, 2018" stamp is
     arXiv's regeneration date): the pre-acceptance preprint, not the
     typeset Letter; refereeing changes after v1 are not seen. No code
     version is printed.
   * **Identity.** doi:10.3847/2041-8205/816/1/L9, checked on Crossref
     (returned lower-case `.../l9`): title and four authors match page 1;
     Astrophys. J. Lett. 816(1):L9, online 2015-12-30, issue 2016-01-01.
   * **How it was read.** Text extraction of all sections; eq. 1 (garbled
     in the text layer) read from the rendered page 3. Figures 1–4 read only
     for the numbers in text and captions.
   * **Recorded as printed.** The abstract places the Kelvin–Helmholtz
     instabilities "after about 20 orbits"; §3 places their onset at about 7
     orbits (40 d) and the large-scale overlap at 90 d. "Ohlmann et al.
     (2015, in prep.)" is cited twice for the initial-condition and
     relaxation procedure but has no reference-list entry.
   * **Reference list:** 20 entries, only Kippenhahn et al. (2012) with a
     title and DOI. Same-key collisions resolved as different works:
     Pakmor, Springel, Bauer et al. (MNRAS 455:1134) is `pakmor-2016-b`
     (`pakmor-2016` is Pakmor, Pfrommer, Simpson & Springel, ApJ 824:L30);
     Ricker & Taam (ApJ 672:L41) is `ricker-2008-b` (`ricker-2008` is
     Ricker, ApJS 176:293). `springel-2010`, `gorski-2005`, `hunter-2007`
     and `passy-2012` match existing entries by volume and page.
