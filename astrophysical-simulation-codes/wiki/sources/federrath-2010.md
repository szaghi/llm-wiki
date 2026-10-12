---
type: Source
title: "Federrath et al. (2010) — Modeling collapse and accretion in turbulent gas clouds: implementation and comparison of sink particles in AMR and SPH"
description: "Accreting sink particles in the block-AMR code FLASH: creation gated by a resolution density threshold plus refinement, converging-flow, potential-minimum, Jeans-instability, boundedness and proximity checks; bound-and-infalling accretion of the mass above threshold; a four-way gravity split with cubic-spline softening; subcycled leapfrog particle steps; and a 100 solar-mass turbulent cluster compared against SPH."
resource: "doi:10.1088/0004-637X/713/1/269"
source_kind: paper
authors: [Federrath C., Banerjee R., Clark P.C., Klessen R.S.]
year: 2010
venue: "Astrophys. J. 713:269–290"
local_file: "~/papers/mosaic/astrophysical-simulation-codes/2010-ApJ-Federrath-1010880004-637x7131269.pdf"
tags: [amr, self-gravity, multigrid, hydro, benchmark, verification, performance]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The paper adds accreting sink particles to the block-AMR code FLASH
(Fryxell et al. 2000; Dubey et al. 2008) as a subgrid model that cuts off
local runaway collapse once the Jeans length can no longer be resolved at the
finest level. Its central claim concerns creation: a density threshold alone
($\rho_{\rm res}$, set from the Truelove Jeans condition) creates spurious sinks
in supersonic turbulence whenever that threshold lies below the opacity limit
(about $10^{-14}$ g cm$^{-3}$), because shocks can exceed it without the gas being
bound. A control volume of radius $r_{\rm acc}$ must therefore pass further
checks (finest level, converging flow, central potential minimum, Jeans
instability, boundedness, no existing sink within $r_{\rm acc}$). Accretion takes
only the mass above threshold, and only if it is bound and infalling. Gravity
is split four ways; sinks advance by a variable-step leapfrog with a
close-encounter limit and N-body subcycling. Tests: two-body orbits, gas–sink
gravity on AMR, Bonnor–Ebert and singular-isothermal-sphere collapse, the
Boss–Bodenheimer rotating core, and a 100 $M_\odot$ turbulent cluster compared
with the Bate et al. (1995) SPH code. Merged into
[sink particles](/methods/sink-particles.md), the
[Jeans resolution criterion](/definitions/jeans-resolution-criterion.md) and
[adaptive mesh refinement](/methods/adaptive-mesh-refinement.md).

# Key claims

1. **Subgrid options** (§1, eqs. 1–2). $t_{\rm ff} = (3\pi/(32G\rho))^{1/2}$,
   $\lambda_J = (\pi c_s^2/(G\rho))^{1/2}$. "Jeans heating" (stiffening the EOS
   above $\rho_{\rm res}$) is rejected: it heats gas that should stay isothermal,
   heats non-collapsing shocked gas, and shrinks the Courant step. Sink
   particles are the alternative, first used in Eulerian AMR by Krumholz,
   McKee & Klein (2004). Asserted.
2. **Truelove criterion** (§2.2.1, §2.2.2, §2.2.8, §4.2.1, eq. 32). Stated as
   $\lambda_J/\Delta x \ge 4$; Heitsch et al. (2001) find that MHD needs "more than
   four cells". The criteria "are only meaningful in regions that are undergoing
   self-gravitational collapse"; pure AMR satisfies them only for the first
   collapsing object, because the Courant step then stalls the run. Threshold:
   $\rho_{\rm res} = \pi c_s^2/(G\lambda_J^2) = \pi c_s^2/(4Gr_{\rm acc}^2)$, i.e.
   $\lambda_J = 2r_{\rm acc}$ (eq. 32). With $r_{\rm acc} \simeq 2.5\,\Delta x$, $\lambda_J$
   is resolved by 5 cells at the finest level; coarser levels refine to keep at
   least 12 cells per $\lambda_J$ (§4.2.1). An extra criterion keeps every cell
   within any sink's $r_{\rm acc}$ at the finest level (§2.2.2). Letting shocks
   exceed $\rho_{\rm res}$ does not violate Truelove, since it "only applies to
   gravitationally bound gas in freefall collapse" (§2.2.8, asserted).
3. **Creation checks** (§2.2, eqs. 3–12). Control volume: cells within
   $r_{\rm acc}$ of a cell above $\rho_{\rm res}$ (eq. 3). Checks: finest level;
   converging flow along each principal axis, not only $\nabla\cdot\mathbf v < 0$
   ("unlike Krumholz et al. 2004", §2.2.3); central potential minimum (eq. 4);
   Jeans instability $\vert E_{\rm grav}\vert > 2E_{\rm th}$ (eq. 8), with
   $E_{\rm mag}$ added to the right side when fields are present (eq. 9);
   boundedness $E_{\rm grav} + E_{\rm th} + E_{\rm kin} + E_{\rm mag} < 0$ with
   $E_{\rm kin}$ relative to the centre of mass (eqs. 10–12); no existing sink
   within $r_{\rm acc}$ (§2.2.7). The order "does not matter"; the cheapest
   run first. The potential-minimum check alone "prevents almost all spurious
   sink particles"; the Jeans and bound checks remain necessary in
   shock-dominated, high-dispersion flows and for magnetic effects (§2.2.8,
   qualitative, no numbers). A new sink takes the control-volume gas and sits
   at its centre of mass.
4. **Other grid sink codes** (§2.2.8). Krumholz et al. (2004), Wang et al.
   (2010) and Padoan & Nordlund (2009) use a density threshold and the total
   divergence only; "Thus, a significantly larger number of sink particles is
   typically created", which the AMR codes handle by subsequent merging, acting
   as an effective accretion on top of their Bondi–Hoyle accretion. The extra
   checks matter only when sinks form below the opacity limit.
5. **Accretion** (§2.3, eq. 13). A cell above $\rho_{\rm res}$ inside $r_{\rm acc}$
   offers $\Delta M = [\rho - \rho_{\rm res}]\Delta V$, accreted only if bound to the
   sink plus remaining gas and radially infalling; with overlapping radii it
   goes to the sink it is most strongly bound to. Inside an inner radius
   covering the single central cell, gas is accreted without checks. Mass and
   linear momentum are conserved; the sink is moved to the centre of mass of
   the particle–gas configuration.
6. **Gravity split** (§2.4, eqs. 14–19). Gas–gas by multigrid Poisson (tree
   solver an alternative); gas→sink by first-order CIC interpolation (TSC or
   tricubic made no significant difference); sink→gas by a direct sum over
   cells × sinks, negligible next to the multigrid solve up to $10^3$ sinks;
   sink–sink by direct sum. Sink potentials are not in the Poisson source.
7. **Softening** (§2.4.5, App. A, eq. A1). Cubic-spline softening (Monaghan &
   Lattanzio 1985; Price & Monaghan 2007), exactly Newtonian for
   $r \ge r_{\rm soft}$ and smoothly zero as $r \to 0$; $r_{\rm soft} = r_{\rm acc}$ in
   the cluster comparison.
8. **Particle time step** (§2.5, eqs. 20–23). Variable-step leapfrog with four
   limits (Courant, gas acceleration, sink crossing at most half a cell, and a
   sink–sink close-encounter limit), each with a factor $< 1$ (values not
   printed). The hydro step is the minimum of eqs. 20–22; the close-encounter
   step was measured up to three orders of magnitude smaller, so sinks are
   subcycled at eq. 23 with the gas held fixed ("similar to Krumholz et al.
   2004"); subcycling is called "absolutely necessary".
9. **Conservation** (App. B, eqs. B1–B6). Mass and linear momentum are
   conserved by construction; angular momentum is in general not, because the
   condition $\mathbf R\times\mathbf v_{\rm cm} = \mathbf L/M$ (B5) fails when
   $\mathbf L$ is not orthogonal to $\mathbf v_{\rm cm}$ — "the case for any
   implementation of accreting sink particles"; the fix is an intrinsic sink
   spin (proved, elementary). §2.3 nevertheless says accretion conserves
   angular momentum (see Recorded as printed).
10. **Merging** (§3.5). Optional: sinks within each other's $r_{\rm acc}$,
    bound and converging, merge at the centre of mass, inheriting linear and
    angular momenta.
11. **Threshold alone overcounts** (§4.3, §5, Fig. 14). A threshold-only cluster
    run overestimates the number of fragments "by more than one order of
    magnitude" and the accreted sink mass by 133%, 51%, 19% and 14% at
    $t/t_{\rm ff}$ = 0.8, 0.9, 1.0, 1.1 (measured).
12. **Cost** (§4.3.4). On HLRB-II (SGI Altix 4700): FLASH ~10,300 CPU h on 128
    CPUs, SPH ~2,400 CPU h on 16 CPUs (SPH "4-5 times faster"); FLASH had ~32 M
    cells at $t = 0$ and 56 M at $1.1\,t_{\rm ff}$, ~30× the SPH element count, so
    FLASH was 6–8× cheaper per resolution element (measured).

**Tests** (§3–4; measured). Two 1 $M_\odot$ sinks, circular orbit: circular
for 1000 orbits (Fig. 2); elliptical: ~1° perihelion shift after ~100 orbits
with subcycling, ~21° after ten orbits without eq. 23 (Fig. 3); head-on passes:
energy conserved over 1000 oscillations with subcycling, particles leave the
domain after ~68 oscillations without (Fig. 4). Static singular isothermal
sphere, hydro off, three test sinks, $32^3$ base plus 2 levels, refine at 6 and
derefine above 12 cells per $\lambda_J$: circular velocities 1–2% below
analytic; multigrid loses spherical symmetry near Cartesian boundaries after
10–100 orbits (Figs. 5–6). Bonnor–Ebert sphere ($\xi_{\max} = 7.0$), thresholds
$10^2$ and $10^4\rho_0$: qualitative agreement with Foster & Chevalier (1993)
(Figs. 7–8). Singular isothermal sphere collapse, $A = 29.3$: accretion rate
about $1.5\times10^{-4}\,M_\odot$ yr$^{-1}$ against $1.45\times10^{-4}$ from a
re-integration of Shu (1977), "excellent agreement", about 3% (Figs. 10–11).
Boss–Bodenheimer core, $r_{\rm acc} = 39$ AU (2.5 cells), merging on: angular
momentum conserved "to within 2%" up to 23% of the mass accreted (Fig. 12).
Cluster run ($100\,M_\odot$, rms Mach ~4.5, $128^3$ base plus 2 levels, effective
$512^3$; SPH 2 M particles; same $\rho_{\rm res}$ and $r_{\rm acc} = 490$ AU): FLASH
5, 15, 32, 49 sinks vs SPH 5, 17, 48, 61 at $t/t_{\rm ff}$ = 0.8–1.1; at equal
formation efficiency (~26%) 49 vs 50 sinks, KS probability 55% (Fig. 17).

# Notation map

| Federrath et al. (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf v$, $P$ | $\rho$, $\mathbf v$, $p$ | |
| $c_s$ | $c_s$ | **note:** isothermal sound speed in most of the paper; registry $c_s$ is adiabatic |
| $\Gamma$ (eqs. 30–31) | none (words) | barotropic polytropic exponent, not a ratio of specific heats |
| $\Delta x$ | $h$ (finest level) | "smallest linear cell size" |
| $\phi$ (eqs. 4, 6), $\Phi_{\rm gas}$ (eq. 14) | $\Phi$ | in eq. 6 $\phi$ is the potential of the control-volume gas only |
| $\mathbf g_{g-g}$, $\mathbf g_{s-g}$, $\mathbf g_{\rm gas}$, $\mathbf g_{{\rm sinks},n}$ | $\mathbf g$ with words | |
| $C_{\rm cfl}$ | $\nu$ | |
| $C_{gg}$, $C_{vs}$, $C_{gs}$ | none (words) | safety factors of the particle step limits |
| $\rho_{\rm res}$, $r_{\rm acc}$, $r_{\rm soft}$ | none (words) | sink density threshold, accretion radius, softening radius |
| $\lambda_J$, $M_J$, $t_{\rm ff}$ | none (words) | Jeans length, Jeans mass, free-fall time |
| cells per $\lambda_J$ | none (words) | |
| $E_{\rm th}$, $E_{\rm grav}$, $E_{\rm kin}$, $E_{\rm mag}$ | none (words) | **collision:** volume-integrated energies; registry $E$ and $E_{\mathrm g}$ are densities |
| $\mathbf B$ (eq. 9, $1/8\pi$) | $\mathbf B$ | Gaussian units; Heaviside–Lorentz $\mathbf B = \mathbf B_{\rm G}/\sqrt{4\pi}$ |
| $M_n$, $\mathbf r_n$, $\mathbf v_n$, $\mathbf r_{nm}$ | none (words) | sink mass, position, velocity; $n$, $m$ sink indices |
| $\tau$ (eq. 26), $m$, $\xi$ | none (local) | **collision:** $\tau$ is the dimensionless Bonnor–Ebert time (registry $\tau$ is the Valencia energy or optical depth); $m$ is also an azimuthal mode number |
| $\alpha$, $\beta$ | none (local) | **collision:** energy ratios (§3.5) and SPH viscosity coefficients (§4.1) |
| $A$ | none (local) | Shu instability parameter; **collision** with flux Jacobian $A(u)$ |

# Pages created or updated

* Created [Sink particles](/methods/sink-particles.md),
  [Jeans resolution criterion](/definitions/jeans-resolution-criterion.md).
* Updated [Adaptive mesh refinement in astrophysical codes](/methods/adaptive-mesh-refinement.md).
* Also cited on [Singular isothermal sphere collapse](/benchmarks/singular-isothermal-sphere-collapse.md).

# Citations

1. `~/papers/mosaic/astrophysical-simulation-codes/2010-ApJ-Federrath-1010880004-637x7131269.pdf`.
   * **Version.** arXiv:1001.4456v2 (28 Feb 2010), emulateapj preprint, 30
     pages (17 text, 13 figure pages); the header "draft October 23, 2018" is
     an arXiv rebuild artefact. Not the typeset article; "in press" and
     "submitted" items in the reference list suggest a post-acceptance
     revision. The FLASH version of the runs is not stated (the multigrid is
     "implemented in flash v2.5, recently refined for v3 by Ricker 2008").
   * **Identity.** doi:10.1088/0004-637X/713/1/269, checked on Crossref:
     title as on page 1, Astrophys. J. 713(1):269–290, issued 2010-03-19;
     authors Federrath, Banerjee, Clark, Klessen.
   * **How it was read.** Text extraction, all sections; eqs. 16–23 and
     32–33 checked on page images (pp. 6, 11); eq. A1, garbled in the text
     layer, read from the page image (p. 15) and checked for continuity.
     Figures read for captions only.
   * **Recorded as printed.** Eq. 18 prints
     $\mathbf g_{s-s,n} = -\sum_{m\ne n}GM_m\mathbf r_{nm}/\vert\mathbf r_{nm}\vert^3$ with
     $\mathbf r_{nm} = \mathbf r_m - \mathbf r_n$, which read literally is
     repulsive (eq. 16 has the same form); treated as a sign-convention slip.
     §2.3 says accretion conserves "mass, linear momentum, and angular
     momentum (see Appendix § B)", while App. B shows angular momentum cannot
     be conserved without sink spin; whether FLASH sinks carry spin is not
     stated. "Bondy-Hoyle" (sic) in §2.2.8. No values for the time-step
     factors $C$; no resolution sweep or error norms.
   * **Reference list:** 97 printed entries, no titles, no DOIs. Same-key
     suffixes in printed order: federrath-2009 (2009a, ApJ 692:364) /
     federrath-2009-b (Roman-Duval, A&A in press); krumholz-2007 (Krumholz &
     Bonnell, arXiv:0712.0828) / krumholz-2007-b (Krumholz, Klein & McKee, ApJ
     656:959); price-2010 / price-2010-b (Price & Federrath, submitted);
     benz-1990 / benz-1990-b (Benz et al., ApJ 348:647). truelove-1997 (ApJ
     489:L179) is distinct from truelove-1998 (ApJ 495:821); fryxell-2000
     matches the existing key; the krumholz-2007 keys need a vol:page check
     against the bundle's existing krumholz-2007 entries. Padoan & Nordlund
     2009 printed "ApJ, submitted (arXiv:0907.0248)".
