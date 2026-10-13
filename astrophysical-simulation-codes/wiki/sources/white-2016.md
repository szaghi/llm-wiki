---
type: Source
title: "White et al. (2016) — An extension of the Athena++ code framework for GRMHD based on advanced Riemann solvers and staggered-mesh constrained transport"
description: "Method paper of the general-relativistic MHD module of Athena++ on arbitrary stationary spacetimes: HLLC and HLLD used in GR through a transformation to a locally Minkowski frame at each interface, Gardiner–Stone upwind constrained transport with metric-weighted lengths, Noble 1D_W inversion, PLM and van Leer predictor–corrector, verified on SR/GR linear waves, Komissarov shock tubes, coordinate-invariance blasts, Bondi and Gammie inflows and Fishbone–Moncrief tori, with single-core throughput and weak scaling to 6144 cores."
resource: "doi:10.3847/0067-0049/225/2/22"
source_kind: paper
authors: [White C.J., Stone J.M., Gammie C.F.]
year: 2016
venue: "Astrophys. J. Suppl. 225:22"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/2016-ApJS-White-1038470067-004922522.pdf"
tags: [software, mhd, hydro, relativity, riemann-solver, constrained-transport, primitive-recovery, time-integration, performance, scaling, verification]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper documents the general-relativistic MHD module of
[Athena++](/software/athena-plus-plus.md), a rewrite of Athena in which
Newtonian, special- and general-relativistic dynamics share one code, for
arbitrary stationary spacetimes in 1, 2 or 3 dimensions (§1, §2). It
states two contributions. (i) The HLL-family solvers (HLLC for hydro,
HLLD for MHD) are used in general relativity without being rewritten:
left and right states are transformed to a locally Minkowski orthonormal
frame attached to each interface, a special-relativistic solver is
applied there, and the result is mapped back; the interface generally
moves in that frame (§3.3–§3.4, Appendix). (ii) Staggered-mesh
[constrained transport](/methods/constrained-transport.md) after Evans &
Hawley (1988), with the Gardiner & Stone (2005) upwind EMF construction
extended to arbitrary stationary coordinates (§3.5). The scheme is second
order: PLM with Mignone's (2014) limiter, the van Leer predictor–corrector,
and an inversion based on Noble et al. (2006) 1D_W. It is verified on
special- and general-relativistic linear waves, Komissarov shock tubes,
blast waves in "snake" coordinates, Bondi accretion, the Gammie (1999)
magnetized inflow and hydro and MRI-turbulent Fishbone–Moncrief tori, and
timed on one core and in weak scaling to 6144 cores (§4–§6).

# Key claims

Equations are written in words where the registry has no symbol (the
4-metric, its determinant, the connection, the fluid-frame field); see the
Notation map.

1. **Riemann solvers in GRMHD codes** (§1). Of the 10 GRMHD codes listed
   (Harm, Komissarov 2004, the Valencia code, ECHO, Shibata & Sekiguchi,
   Anderson et al., WhiskyMHD, GRHydro, SpEC, IllinoisGRMHD), only
   Komissarov (2004) and Antón et al. (2006) describe Roe-type solvers,
   and only Shibata & Sekiguchi and Antón et al. central schemes; "All
   others restrict themselves to HLLE and LLF".
2. **Divergence control in GRMHD codes** (§1). Four families: divergence
   cleaning (elliptic, parabolic, hyperbolic; "only the last naturally
   able to respect causality in relativistic settings"),
   vector-potential evolution (gauge care needed with mesh refinement),
   staggered CT (Evans & Hawley 1988) and Flux-CT (Tóth 2000). Among the
   10 codes, Anderson et al. use hyperbolic cleaning, IllinoisGRMHD a
   staggered vector potential, Harm and GRHydro Flux-CT, "and the
   remaining six use a staggered CT scheme".
3. **Priority** (§1; asserted). To the authors' knowledge the code is "the
   only 3D finite-volume Godunov GRMHD code" combining advanced Riemann
   solvers and staggered-mesh CT.
4. **Equations** (§2, eqs. 1–6). Units with the gravitational constant and
   the speed of light equal to 1 and $\sqrt{4\pi}$ absorbed into the
   field; signature $(-,+,+,+)$. Mass, energy–momentum and induction are
   written in flux-conservative form for densities weighted by the square
   root of minus the 4-metric determinant, which equals
   $\alpha_{\mathrm L}\sqrt{\det\gamma_{ij}}$; the energy–momentum source
   is the connection contracted with the stress–energy tensor (eq. 6).
5. **Metric-weighted finite volume** (§2, eqs. 7–15). Cell volumes, face
   areas and edge lengths are integrals of that weight over the cell,
   face or edge (eqs. 7, 8, 14); conserved quantities are weighted volume
   averages (eq. 9) and fluxes area averages (eq. 10); the geometric source
   is evaluated from the inverted primitives at cell centres (eq. 11); the
   face field is updated by the circulation of edge EMFs times the edge
   lengths over the face area (eq. 15).
6. **Inversion** (§3.1). Based on the 1D_W scheme of Noble et al. (2006).
   In GR the primitives are $\rho$, $p$ and the normal-observer spatial
   velocity, which "describe subluminal motion no matter what values they
   have"; Newton–Raphson solves for $\rho h_{\mathrm{rel}}W^2$, with
   $\mathbf B = 0$ for hydro. In SR, MHD uses Newton–Raphson in the same
   variable as Mignone & McKinney (2007), but on the residual of the
   conserved energy as a function of it; SR hydro solves the quartic in
   $\vert\mathbf v\vert$ in closed form (Schneider et al. 1993; eqs. 17–19).
   Limits: density and pressure floors and a Lorentz-factor ceiling
   "often chosen to be 100"; out-of-range primitives move to the nearest
   admissible values; a non-converged iteration sets the floors and the
   cell's conserved variables are recomputed. The face field is
   interpolated to the volume centroid with a linear weight (eq. 16).
7. **Reconstruction** (§3.2, eqs. 20–22). PLM on primitives with the
   modified van Leer limiter of Mignone (2014), accounting for nonuniform
   spacing and for centroids that differ from geometric centres; "proved
   to be TVD for all orthogonal coordinate systems", not for
   non-orthogonal ones. Transverse $\mathbf B$ is reconstructed from
   cell-centred values; the normal component is the face value.
8. **Frame transformation** (§3.3, eqs. 23–28; Appendix, eqs. 54–72). An
   orthonormal tetrad is built per interface direction from four
   requirements: mutual orthogonality; normalization to $\pm1$; the time
   vector is the normal observer (orthogonal to the constant-time slices);
   the spatial projection of the interface-normal vector is orthogonal to
   the interface within the slice. This gives lower-triangular matrices
   (eqs. 23, 25). The interface moves in that frame with speed
   $\beta^1/(\alpha_{\mathrm L}\sqrt{\gamma^{11}})$ (eq. 28, written there
   with the inverse 4-metric; $\gamma^{11}$ is the component of the inverse
   of $\gamma_{ij}$), "in agreement with Pons et al. (1998)". Because the
   frame is the normal observer's, it works inside the ergosphere and,
   in horizon-penetrating coordinates, inside the horizon, where a frame
   of stationary observers fails. The transformation can be singular at
   coordinate singularities such as the polar axis. Rejected alternatives
   (Appendix): an interface-normal vector along the coordinate basis
   vector mixes transverse fluxes into the normal flux; one orthogonal to
   the constant-coordinate 3-surface exists only when the time–space
   component of the inverse metric vanishes.
9. **Riemann solvers** (§3.4, Fig. 1). LLF with the largest Roe-matrix
   eigenvalue on both sides; HLLE with Einfeldt (1988) bounds; HLLC of
   Mignone & Bodo (2005), hydro only (the relativistic MHD HLLC of Mignone
   & Bodo 2006 is not implemented, "in favor of HLLD"); HLLD of Mignone,
   Ugliano & Bodo (2009), with the total pressure across the contact found
   by the secant method, started from a Newton–Raphson inversion of the
   HLLE state when the normal field is strong. Signal speeds are sound
   speeds (hydro) or fast speeds (MHD). With a moving interface the wave
   fan is sampled along the ray moving with the interface, not at the
   fixed position, and the selected region's conserved state, not just its
   flux, is needed. All HLL solvers "guarantee positivity" (asserted).
10. **Constrained transport** (§3.5, eqs. 29–32, Fig. 2). The Gardiner &
    Stone (2005) algorithm "extended to relativity", differing from Evans
    & Hawley (1988) in cell-centred rather than face-centred velocities.
    Steps: face EMFs from the Riemann fluxes of the field; cell-centre
    EMFs from the four-velocity and fluid-frame field; eight
    centre-to-face gradients divided by metric-weighted half-widths (the
    integral of the square root of the diagonal metric component along the
    half-cell, eqs. 29–30); upwinding by the sign of the face mass flux,
    citing "(50) of Gardiner & Stone" (eq. 31); the corner EMF following
    "(41) of Gardiner & Stone" (eq. 32). For a smoothly varying metric and
    spacing the length factors "approximately cancel" between eqs. 30
    and 32. "The fundamentals of CT were in fact developed within the
    context of general relativity".
11. **Source terms** (§3.6). With the free index lowered, the source
    vanishes for coordinates the metric does not depend on; the metric
    being stationary, there is never a geometric energy source. Momentum
    sources use cell-centred metric values.
12. **Time integrator** (§3.7, eq. 33). The second-order van Leer
    predictor–corrector, "TVD, so it will not introduce spurious extrema"
    (asserted). The first half step "can" use first-order reconstruction
    and still converge at second order. RK2 (Heun) is "no better than the
    vanLeer method" and needs second-order reconstruction in both stages;
    RK3 needs extra storage; CTU is not used because it "require[s]
    time-advanced variable estimates that are difficult to generalize to
    arbitrary coordinate systems".
13. **Storage** (§3.8, eq. 34). 20 numbers per cell for hydro, 50 for MHD.
    The metric is stationary and interfaces are constant-coordinate
    surfaces, so metric quantities are precomputed in separable 1D and 2D
    arrays, never 3D. In Kerr–Schild coordinates: 22 values per radial
    cell, 32 per polar cell, 9 per azimuthal cell and 20 per radial–polar
    pair, against 20–50 per cell for the evolved variables; the cell volume
    is in closed form (eq. 34).
14. **Performance** (§6, Table 1, Fig. 17). One core of a Xeon E5-2670
    (Sandy Bridge, 2.6 GHz), in $10^5$ cell updates per second, for SR /
    GR Minkowski / GR Kerr–Schild: hydro LLF-NT 12.8 / 10.4 / 3.82, HLLC
    8.57 / 7.36 / 3.28; MHD LLF-NT 3.24 / 4.70 / 2.94, LLF-T — / 2.60 /
    1.97, HLLD 1.23 / 1.13 / 1.22. HLLE runs at 93 ± 6 % of the LLF speed.
    Weak scaling on the NAOJ Cray XC30 (24 cores per node), one $64^3$
    block per core, up to 6144 cores: one core to a full node costs 20 %
    per core (attributed to memory-bus saturation); at 6144 cores the
    efficiency relative to 24 cores is ">97%" (hydro) and
    "indistinguishable from 100%" (MHD). Optimizations: precomputed metric
    functions; unit-stride innermost loops, with the second- and
    third-direction fluxes also swept in first-direction order; vectorized
    innermost loops with manual inlining (e.g. the HLLD residual); fixed
    iteration counts in place of convergence loops so they vectorize.
15. **State of the code** (§7). Static mesh refinement is available; AMR,
    PPM, RK3 and GR radiative transfer are "being developed".

# Tests

All in §4–§5; second order is measured as $L_1$ error against resolution.

1. **SR hydro linear waves** (§4.1, Fig. 3). Background $\rho = 4$,
   $p = 1$, $\mathbf v = (0.1, 0.3, -0.05)$, $\gamma = 4/3$; one period;
   error the rms over primitives of the $L_1$ error (eq. 36). Second
   order; HLLE's entropy-wave error is 1.7× HLLC's; equal sound-wave
   errors.
2. **SR MHD linear waves** (§4.1, Fig. 4). Same background with
   $\mathbf B = (2.5, 1.8, -1.2)$; the four rightmost waves. Second order;
   HLLD better than HLLE by 3.1×, 1.7×, 1.4× (entropy, slow, Alfvén), not
   on the fast wave. LLF is "indistinguishable from HLLE".
3. **GR linear waves in "tilted" coordinates** (§4.1, eq. 37, Figs. 5–6),
   with a nonzero interface velocity: second order, with margins 2.8×
   (hydro entropy) and 4.8×, 1.8×, 1.4× (MHD), larger than in SR.
4. **Komissarov (1999) SR MHD shock tubes**, seven (§4.2, Fig. 7). HLLD,
   220 cells on $[-1.1, 1.1]$, reference at 2200; $\nu = 0.8$, except 0.2
   (fast shock) and 0.5 (collision). Some of Komissarov's artefacts recur
   (ringing upstream of the slow shock, a bump in the switch-off case, an
   overshoot in shock tube 2); shock tube 1 shows none of his density
   overshoot and much less velocity overshoot.
5. **Hydro blast in Minkowski and "snake" coordinates** (§4.3, eqs. 38–40,
   Fig. 8). Pressure 2.5 inside radius 0.5, 0.1 outside; periodic
   $4\times6$ box, $200\times300$, $\nu = 0.4$, $t = 15$. Differences above
   1 % only at the shocks and in the Richtmyer–Meshkov fingers; HLLC
   fingers sharper than HLLE's.
6. **Magnetized blast** (§4.3, Fig. 9). $\mathbf B = (1, 1, 0)$, HLLD,
   $t = 5$: the field guides the blast and suppresses Richtmyer–Meshkov,
   the same in both coordinate systems. See
   [MHD blast wave](/benchmarks/mhd-blast-wave.md).
7. **Bondi accretion in Schwarzschild** (§4.4, eqs. 41–48, Figs. 10–11),
   hydro (HLLC) and with a radial monopole (HLLD): second order in the
   pressure over the inner three quarters of the grid at $t = 10$.
8. **Gammie (1999) magnetized equatorial inflow** (§4.5, eq. 49, Fig. 12),
   Kerr–Schild, spin 0.5: second order in density, toroidal field and
   radial and azimuthal four-velocity, with the frame-transforming HLLE
   under a large shift.
9. **2D hydro Fishbone–Moncrief torus** (§5, eq. 50, Fig. 13). Spin 0.95,
   $\gamma = 13/9$, HLLC, $\nu = 0.2$: second order; over three orbits at
   $64\times32$, error 0.030 with HLLE and 0.021 with HLLC.
10. **3D MRI torus** (§5, Figs. 14–16). Spin 0.9375, $\gamma = 13/9$,
    inner edge 6 and pressure maximum 12 (gravitational radii), outer
    radius 40; effective $144\times128\times96$ and $288\times256\times192$
    with static refinement derefining the poles by 4; loop field
    normalized by maximum gas over maximum magnetic pressure 100; LLF
    "just as is used in Harm"; $t = 12{,}000$. Compared with Shiokawa et
    al. (2012), not with other codes: electron temperature roughly
    matches; the outer plasma beta reaches about 200 against below 60 and
    approaches 1 in the innermost region (theirs never below 4); larger
    azimuthal correlation lengths, which decrease with resolution. See
    [magnetized torus accretion](/benchmarks/magnetized-torus-accretion.md).
11. **Performance** (§6): claim 14.

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $\rho$, $p_{\rm gas}$ | $\rho$, $p$ | rest-mass density, gas pressure |
| $h$ | $h_{\mathrm{rel}}$ | **collision**: the bare $h$ is the cell size |
| $\Gamma$ | $\gamma$ | adiabatic index; **collision**: the paper's $\gamma$ is the Lorentz factor |
| $\gamma$ (normal-frame Lorentz factor) | $W$ | **collision** with $\gamma$ |
| $W = \gamma^2\rho h$ | $\rho h_{\mathrm{rel}}W^2$ | **collision**: registry $W$ is the Lorentz factor; no new symbol |
| $\alpha$, $\beta^i$, $\gamma_{ij}$, $\gamma^{ij}$ | $\alpha_{\mathrm L}$, $\beta^i$, $\gamma_{ij}$, inverse of $\gamma_{ij}$ | lapse, shift, 3-metric |
| $g_{\mu\nu}$, $g$, $\Gamma^\sigma{}_{\mu\nu}$ | in words | 4-metric, determinant ($\sqrt{-g} = \alpha_{\mathrm L}\sqrt{\det\gamma_{ij}}$), connection; not in the registry |
| $u^\mu$, $\tilde u^i$ | in words | four-velocity; normal-frame spatial velocity; **collision** with $u$ |
| $B^i$ | $\mathbf B$ | $\sqrt{4\pi}$ absorbed |
| $b^\mu$, ${}^*F^{\mu\nu}$, $T^{\mu\nu}$ | in words | fluid-frame field, dual field tensor, stress–energy tensor |
| $E^i$ | $\boldsymbol{\mathcal E}$ | edge EMF |
| $D$, $M^i$, $E$ (SR) | $D$, $S_i$, $\tau + D$ | SR $E$ includes $D$; **collision** with the Newtonian $E$ |
| $F$, $G$, $H$ | $\hat f_{i+1/2}$ per direction | **collision**: $G$ is the gravitational constant |
| $\Delta V$, $\Delta A$, $\Delta L$ | in words | metric-weighted volume, area, length |
| $\lambda$ | $\lambda^{(p)}$ | also a centroid weight (eq. 16) and a correlation length (§5): **collision** |
| $v^{\hat x}$ | in words | interface speed in the orthonormal frame |
| $\beta$ (torus) | $\beta_{\mathrm p}$ | gas over magnetic pressure |
| $M$, $a$ | $M_{\mathrm{BH}}$, spin in words | **collision**: $a$ is the scale factor |
| $T = p_{\rm gas}/\rho$ (Bondi) | in words | dimensionless, not a temperature |
| $\epsilon$ | $L_1$ | error measure |
| CFL number | $\nu$ | |

# Pages created or updated

* Created this Source page.
* Updated [Athena++](/software/athena-plus-plus.md) (batch-10 section: the
  GRMHD module, frame transformation, dated inversion and integrator
  statements, 2016 performance and tests).
* Updated [Constrained transport](/methods/constrained-transport.md)
  (batch-10 section: the metric-weighted upwind CT, the 2016 census of
  GRMHD induction schemes).
* Updated [Primitive-variable recovery](/methods/primitive-variable-recovery.md)
  (batch-10 section: Noble 1D_W in the 2016 Athena++, the SR quartic,
  dating).
* Updated[Approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Magnetized torus accretion](/benchmarks/magnetized-torus-accretion.md),
  [Linear wave convergence](/benchmarks/linear-wave-convergence.md),
  [MHD blast wave](/benchmarks/mhd-blast-wave.md),
  [Density and pressure floors](/methods/numerical-floors.md),
  [Cell-update throughput](/definitions/cell-updates-per-second.md).

# Citations

1. White C.J., Stone J.M., Gammie C.F. (2016), "An extension of the
   Athena++ code framework for GRMHD based on advanced Riemann solvers and
   staggered-mesh constrained transport", Astrophys. J. Suppl. 225(2):22,
   doi:10.3847/0067-0049/225/2/22. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/2016-ApJS-White-1038470067-004922522.pdf`.
   * **Version read.** The typeset publisher PDF (22 pages, © AAS);
     received 2015 October 30, revised 2016 June 18, accepted 2016 June
     20, published 2016 August 11. Not a preprint.
   * **Identity.** Checked on Crossref: title, the three authors, vol. 225,
     issue 2, article 22, print 2016-08, online 2016-08-11.
   * **How it was read.** Text extraction of all sections; eqs. 22, 31–32
     and Table 1 checked on rendered pages (eq. 32 at 250 dpi). Figs. 3–7
     and 10–17 read for orders and printed ratios only; Fig. 17 values
     only qualitatively. Eqs. 52–53 (correlation function) are garbled in
     the text layer and not reproduced.
   * **Recorded as printed.** (a) Eq. 32: the two correction terms print
     the EMF itself at quarter points, where the upwinded EMF gradients of
     eqs. 29–31 are meant (reader's reading, from steps 3–4 and
     dimensions); not checked against Gardiner & Stone's printed formula.
     (b) White et al. cite Gardiner & Stone's eqs. (41) and (50) for the
     corner formula and the upwinding; the bundle's
     [Gardiner & Stone (2005)](/sources/gardiner-2005.md) page, from the
     arXiv v1, places them at eq. 42 and eqs. 50–51, probably a
     journal-versus-preprint numbering offset (not verified). (c) Eq. 31
     gives only the positive and negative mass-flux cases; no rule for
     zero mass flux. (d) §6 says MHD runs "at 1/4 to 3/4 the speed of pure
     hydrodynamics" for fixed geometry and solver; Table 1 gives
     HLLD/HLLC = 0.14 (SR) and 0.15 (GR Minkowski), and LLF-NT in
     Kerr–Schild 0.77. MHD LLF-NT is faster in GR Minkowski (4.70) than in
     SR (3.24), and MHD HLLD faster in Kerr–Schild (1.22) than in GR
     Minkowski (1.13); neither is explained.
   * **Reference list:** 50 printed entries (AAS style, no titles except
     Misner, Thorne & Wheeler). Evans & Hawley is printed ApJ 322:659
     (Crossref 332:659), merged into `evans-1988`; Hawley, Smarr & Wilson,
     ApJ 277:296, is `hawley-1984-b`, not `hawley-1984` (ApJS 55:211);
     Misner, Thorne & Wheeler, printed "New York: W. H. Freeman and
     Company", is `misner-1973`; Stone & Gardiner, ApJS 178:137, is
     `stone-2008`. The ingested [Evans & Hawley (1988)](/sources/evans-1988.md),
     [Gardiner & Stone (2005)](/sources/gardiner-2005.md) and
     [Stone et al. (2008)](/sources/stone-2008.md) are cited.
     Bibliography: 2522 entries.
