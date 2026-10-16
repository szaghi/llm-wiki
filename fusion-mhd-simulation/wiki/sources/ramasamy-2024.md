---
type: Source
title: "Ramasamy et al. (2024) — Nonlinear MHD modeling of soft β limits in W7-AS"
description: "Extends JOREK3D stellarator reduced MHD with parallel flow and a finite-element vacuum field, benchmarks it against CASTOR3D on a W7-AS (2,1) tearing mode (about 3%) and on low-shear interchange modes (within 10% only with parallel flow), and applies it to W7-AS β scans that reproduce resistive, mild, non-disruptive MHD activity and a dominant (2,1) mode."
resource: "doi:10.1088/1741-4326/ad56a1"
source_kind: paper
authors: [Ramasamy R., Aleynikova K., Nikulsin N., Hindenlang F., Holod I., Strumberger E., Hoelzl M., JOREK Team]
year: 2024
venue: "Nucl. Fusion 64:086030"
local_file: "/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Ramasamy_Nonlinear_MHD_modeling_of_soft_β_limits_in_W7-AS.pdf"
tags: [mhd, reduced-mhd, stellarator, tearing, ballooning, equilibrium, finite-elements, spectral, time-integration, linear-solver, benchmark, verification, code]
timestamp: 2026-10-16T00:00:00Z
---

# Summary

The paper extends the [stellarator reduced MHD](/methods/stellarator-reduced-mhd.md)
model of [JOREK3D](/software/jorek3d.md)
([Nikulsin et al. (2022)](/sources/nikulsin-2022.md)) with a parallel-velocity
field and a parallel momentum equation, so that fluid compression and acoustic
dynamics are retained, and replaces the analytic
[Dommaschk](/methods/dommaschk-potentials.md) vacuum field by a finite-element
vacuum potential $\chi$ from a Poisson problem, which reduces the ideal-wall
condition to $\psi_\chi=\text{const}$ on the boundary. Two linear benchmarks
against the full-MHD code CASTOR3D follow: a current-driven (2,1)
[tearing mode](/definitions/tearing-mode.md) in an approximate W7-AS
equilibrium (vacuum $\iota\approx0.34$ plus an ohmic current), with growth
rates within about 3%; and low- and high-$n$ interchange modes in a five-period
$l=2$ classical stellarator with low shear crossing $\iota=2/3$. Without
parallel flow the compressible ($\Gamma=5/3$) growth rates are artificially
stabilized, the error growing as $n$ falls; with it all modes agree within
10%, from which the authors infer that the eliminated fast-magnetosonic (field
compression) terms, the concern of Graves et al. (2019), do not matter in this
case. A validation study then uses fixed-boundary imports of free-boundary
VMEC reconstructions of W7-AS shot #51751 (1–10 kPa central pressure) heated
with 3.2 MW. The MHD activity is resistive: a tenfold resistivity increase
destroys confinement, lower resistivity confines the activity to the edge.
With approximately experimental coefficients β keeps rising through the MHD
saturation, because field lines remain ergodically confined within radially
separated sub-volumes; results converge in toroidal resolution only at a
maximum toroidal mode number of about 50. In full-torus runs at artificially
high resistivity a nonlinearly dominant (2,1) mode appears, as in the
experiment. No β flat top is reached; fixed boundary, the missing island
divertor and radial electric field, and approximate transport coefficients are
listed as limitations.

# Key claims

Locations are sections of arXiv v1.

1. **Parallel flow** (§2.1, Eqs. 1–2, 5). The velocity becomes
   $\mathbf v=\nabla u\times\nabla\chi/|\nabla\chi|^2+\hat v_\parallel\mathbf B$
   with a new parallel momentum equation; $\hat v_\parallel=0$ recovers the
   Nikulsin et al. (2022) model. Stated (model definition).
2. **Finite-element vacuum field** (§2.2). $\chi$ solves a Poisson problem with
   $\nabla\cdot\nabla\chi=0$ and $\mathbf n\cdot\nabla\chi=0$ on the plasma
   boundary; the ideal-wall correction is then inside $\nabla\chi$ and
   $\mathbf n\cdot\mathbf B=0$ reduces to $\psi_\chi=\text{const}$, which
   "circumvents" the boundary procedure of §IV of [9]. Dommaschk potentials
   met "numerical difficulties … when representing the vacuum field of highly
   shaped devices", so the finite-element representation "is therefore used
   in all simulations" as "a more robust approach". Stated, no evidence. In
   tension with Nikulsin et al. (2022), who argued that a finite-element
   $\chi$ on $G^1$ elements makes advective terms discontinuous; the
   discontinuity is not addressed.
3. **Conservative form** (§2.3). The momentum equations are written in
   conservative form "unlike in [9]", though [9]'s code already implemented
   it. Stated.
4. **Artificial parallel diffusivity** (§2.3). $D_\parallel$ is used only when
   parallel flow is neglected, to mimic redistribution along field lines.
   Stated.
5. **Validity of the reduction** (§2.3). Tokamak reduced MHD misses the
   finite-β (1,1) internal kink but captures most other instabilities (Pamela
   et al. 2020); Graves et al. (2019) argue that reduced models artificially
   stabilize compressible modes in low-shear regions, worse for low-order
   rational surfaces with broad modes. Attributed.
6. **Mode-group preconditioner** (§2.4). The preconditioner of Holod et al.
   (2021), which couples adjacent harmonics of one mode family, "has been
   important for making simulations computationally manageable"; coupling
   stays strong "even in the second and third toroidal sidebands" for more
   optimized configurations. Stated.
7. **W7-AS (2,1) tearing benchmark** (§3.1, Fig. 2, Table 1). JOREK and
   CASTOR3D linear growth rates differ by at most "approximately 3 %" over the
   resistivity scan; Boozer-coordinate eigenfunctions are in "very good
   agreement" (CASTOR3D sidebands marginally larger, below 6%). Shown.
8. **Re-attribution of the earlier JOREK3D–CASTOR3D mismatch** (§3.1). "The
   helical mode coupling was not correctly resolved in the initial study, due
   to the use of insufficient poloidal resolution in CASTOR3D. At higher
   poloidal resolution, the level of agreement for this simpler case is
   similar to the results shown herein." Stated, no figure or number for the
   re-run W7-A case. This contradicts the attribution of the 13.2%/26.2%
   tearing gap to the neglect of $v_\parallel$ by
   [Nikulsin et al. (2022)](/sources/nikulsin-2022.md) (§VI), recorded on the
   [JOREK3D](/software/jorek3d.md) page; two authors are shared.
9. **Nonlinear W7-AS tearing** (§3.1, Fig. 3). The $N_f=1$ family leads, then
   $n=4,6$, then $n=9,11$; the $N_f=2$ family is driven nonlinearly as $N_f=1$
   saturates; the (2,1) island is visible at $t=4.18$ ms. A single-period run
   first relaxes the force imbalance of the GVEC import. Shown.
10. **Incompressible interchange** (§3.2, Fig. 5a). At $\Gamma=0$ the model
    without parallel flow "agrees very well with full MHD", marginal point
    included. Shown.
11. **Compressional stabilization without parallel flow** (§3.2, Fig. 5b). At
    $\Gamma=5/3$ JOREK without $\hat v_\parallel$ stabilizes the $n=10,15$
    modes more than CASTOR3D; with it agreement is recovered. Shown.
12. **Error grows as $n$ falls** (§3.2, Fig. 7). Full torus at β = 0.86%: with
    parallel flow all identified modes ($n=2$–15) agree with CASTOR3D within
    10%; without it the error grows as $n$ decreases and the low-$n$ modes,
    notably (3,2), are "not observed". Broader, more global modes suffer more
    artificial compression, "similar to the axial compression of a tube of
    fluid". Shown; explanation Stated.
13. **Fast wave unimportant here** (§3.2). With parallel flow the error does
    not grow with decreasing $n$ and the JOREK (3,2) growth rate is slightly
    above full MHD; "the eliminated flux compression terms are not playing an
    important role in the given test case". Shown for this case, inferential.
14. **External (7,5) mode** (§3.2, Figs. 5b, 6). A boundary (7,5) structure is
    a physical external instability (CASTOR3D's $n=5$ free-boundary mode); it
    lowers JOREK's internal growth rates at higher β, capping the benchmark at
    β = 0.86%. With the VMEC equilibrium extended into a vacuum region it grows
    in tens of µs, flattens $\iota$ at 7/5 and later destroys confinement over
    most of the volume. A rigorous benchmark needs a free-boundary JOREK
    stellarator implementation. Shown (qualitative).
15. **Import limit** (§4.1–4.2). The 14 kPa equilibrium, with strong
    Shafranov shift, could not be represented accurately in the JOREK ansatz;
    only ≤10 kPa cases are used. Stated.
16. **Resistive activity** (§4.2, Fig. 9). Resistivity ×10 makes the initial
    activity destroy confinement and β fall; lower resistivity makes it milder
    and edge-confined, and at $\eta=1.93\times10^{-7}$ Ω m "the experimental
    β limit can be exceeded"; the 10 kPa baseline rises, then a mild crash caps
    β at ≈2.35%. Shown.
17. **Fixed-boundary artefact** (§4.2, §4.5). Without the free-boundary
    Shafranov shift and tokamak-like shear growth the $\iota=0.5$ surface is
    not removed with β, which enhances MHD activity: the 1 and 4 kPa runs
    flatten at β > 1.3%, below the experiment. Stated (interpretation).
18. **Toroidal convergence** (§4.3.1, Fig. 10). The rate of rise of β falls as
    the maximum toroidal mode number grows up to ≈50 and does not change
    significantly beyond; under-resolved runs give artificially better
    confinement; doubling the poloidal resolution changes little. Shown.
19. **Transport sensitivity** (§4.3.2, Fig. 11). Tripling $\kappa_\perp$
    (0.231 → 0.693 m²/s) makes β fall below its initial value; a large
    constant $\kappa_\parallel$ ($2.31\times10^6$ m²/s) delays the
    ergodization but slows the later rise; "the soft β limit result … is
    sensitive to the thermal transport parameters". Shown.
20. **Ergodic confinement in sub-volumes** (§4.3.3, Fig. 12). Poincaré plots at
    0.188, 0.421 and 1.189 ms show ergodic field lines separated into radially
    localized sub-volumes; islands do not overlap enough to flatten $T$, so β
    keeps rising; confinement is worst when the ergodic region crosses
    $\iota=0.5$ (a (10,5) chain); most ergodization lies outside $\iota=0.5$,
    as in earlier PIES studies (Reiman et al. 2007). Shown (qualitative).
21. **Full-torus low-$n$ activity** (§4.4, Fig. 13). At
    $\eta=1.93\times10^{-5}$ Ω m the $N_f=1$ family saturates first and
    dominates, a (2,1) island appears at $t\approx0.46$ ms, "in line with past
    experimental observations"; at Spitzer resistivity $N_f=2$ dominates, core
    surfaces survive and a (4,2) deformation sits at $\iota=0.5$. Shown.
22. **Conclusion** (§4.5, §5). "The MHD activity is viscoresistive. At
    viscoresistive parameters which approach the experimental values, a soft β
    limit can be observed, because the induced MHD activity is mild enough for
    field lines to remain ergodically confined within nested plasma
    sub-volumes." Shown in part: "soft β limit" here means mild,
    non-disruptive saturation, not a β plateau (claim 23).
23. **No flat top** (§4.5). A flat top near the experimental limit, 3.4%, is not
    reached; reasons given: fixed boundary (no island divertor, poor parallel
    edge losses), no removal of $\iota=0.5$, approximate turbulent transport,
    no impurities or radiation. Stated.
24. **Flows neglected** (§4.5). The ambipolar radial electric field is absent;
    it could stabilize high-$n$ and destabilize low-$n$ modes, and the
    experimental (2,1) mode rotated poloidally. Stated.

# Models and numerics

**Model.** Single-temperature visco-resistive stellarator reduced MHD with
parallel flow; a two-temperature variant exists but is not used. In the
notation of the [stellarator reduced-MHD page](/methods/stellarator-reduced-mhd.md):

$$\mathbf B=\nabla\chi+\nabla\psi_\chi\times\nabla\chi,\qquad \mathbf v=\frac{\nabla u\times\nabla\chi}{|\nabla\chi|^2}+\hat v_\parallel\mathbf B,$$

with $\hat v_\parallel$ a velocity per unit field (page-local, $\hat v_\parallel B\approx v_\parallel$).
Derivatives with superscripts are relative to $\nabla\chi$
($\partial^\parallel=|\nabla\chi|^{-1}\nabla\chi\cdot\nabla$,
$\nabla^\perp=\nabla-|\nabla\chi|^{-1}\nabla\chi\,\partial^\parallel$,
$\Delta^\perp=\nabla\cdot\nabla^\perp$,
$\Delta^*f=|\nabla\chi|^{-2}\nabla\cdot(|\nabla\chi|^2\nabla^\perp f)$,
$[f,g]=|\nabla\chi|^{-1}\nabla\chi\cdot(\nabla f\times\nabla g)$), with
subscripts relative to $\mathbf B$. The evolved fields are $\rho$, $u$ (via
the vorticity $\varpi=\Delta^\perp u$), $\rho\hat v_\parallel$, $\rho T$ and
$\psi_\chi$, with $\mu_0j=\Delta^*\psi_\chi$ (the paper writes $j=\Delta^*\Psi$
in unstated JOREK normalized units). The flux equation (Eq. 7) reads

$$\partial_t\psi_\chi=\frac{\partial^\parallel u-[\psi_\chi,u]}{|\nabla\chi|}+\eta(j-j_{\mathrm{src}})-\nabla\cdot(\eta_h\nabla^\perp j),$$

where $j_{\mathrm{src}}$ is the current source. Both dissipative terms have the
diffusive sign with $j=+\Delta^*\psi_\chi$, opposite to Nikulsin et al.
(2022), Eq. 3d (compiler's check; evidence for the printed-slip reading of the
open resistive-sign entry on the [reduced MHD page](/methods/reduced-mhd.md)).
The continuity, vorticity, parallel momentum and energy equations (Eqs. 3–6)
carry the parallel-flow terms
$-|\nabla\chi|\partial^\parallel(\rho\hat v_\parallel)-|\nabla\chi|[\rho\hat v_\parallel,\psi_\chi]$
(density), the parallel pressure gradient and $\nabla\cdot(\rho\mathbf v)$
(parallel momentum), and the compression $-\Gamma p|\nabla\chi|(\partial^\parallel\hat v_\parallel+[\hat v_\parallel,\psi_\chi])$
(energy); the vorticity equation is in conservative form with
$-\nabla\cdot[\nabla^\perp u\,\nabla\cdot(\rho\mathbf v)/|\nabla\chi|^2]$
replacing the mass-source term of [9]. Dissipation: resistivity $\eta$,
hyper-resistivity $\eta_h$, perpendicular viscosity $\nu_\perp$ and
hyperviscosity $\nu_h$ (vorticity), viscosities $\nu_{\parallel\perp}$,
$\nu_{\parallel\parallel}$ (parallel momentum), particle diffusivities
$D_\perp$, $D_\parallel$, heat diffusivities $\kappa_\perp$, $\kappa_\parallel$
(m²/s), Ohmic heating with a separate resistivity, sources $S_\rho$, $S_p$.
$\Gamma=5/3$, or 0 in the incompressible test. Coefficients are constant in
the verification and simplified scans; the "experimental approximation" uses
Spitzer $\eta$ and Spitzer–Härm $\kappa_\parallel$ with their $T$ dependence,
a Braginskii-range perpendicular viscosity with Spitzer-like $T$ dependence and
a constant parallel viscosity "several orders of magnitude higher".

**Equilibria.** GVEC (W7-AS tearing case) or free-boundary VMEC (interchange
case, W7-AS #51751), imported into the JOREK ansatz; force balance is "not
guaranteed" to survive the import (§2.2, §4.1).

**Discretization.** Bézier finite elements in the poloidal plane (typically
$G^1$) with toroidal Fourier representation of grid and variables
([Bézier–Hermite elements](/methods/bezier-finite-elements.md)); single field
period (no symmetry-breaking modes) or full torus; mode families $N_f=0,1,2$
for $N_{\mathrm{fp}}=5$. Weak form, [implicit time stepping](/methods/implicit-time-integration.md)
with the mode-group preconditioner; $\Delta t$ not given. Fixed boundary with
an ideal wall; no stellarator free boundary.

**Resolution** (Tables 1–3; "$n_{\rm tor}$" is the highest toroidal mode
number kept, single-period runs keeping multiples of 5):

| Case | $n_{\rm rad}\times n_{\rm pol}$ | toroidal modes |
|---|---|---|
| W7-AS tearing | 64 × 64 | $n\le40$ (linear), $n\le20$ (nonlinear) |
| interchange | 71 × 96 | $n=0,5,\dots,30$ |
| β scan, simplified | 65 × 91 | $n=0,5,\dots,40$ |
| β scan, experimental approximation | 46 × 64 | $n=0,5,\dots,50$ (scans to 60 and to 65 × 91) |
| full torus low-$n$ | | $n\le20$ |

**Diagnostics.** Per-harmonic magnetic and kinetic energies (cross terms from
the toroidal variation of the Jacobian neglected; family totals include them),
Poincaré plots, $\iota$ from field-line tracing, Boozer eigenfunctions. Runs on
COBRA, RAVEN, JFRS-1 and Marconi-Fusion; no core counts, wall times or GPU
use.

# Tests and results

**T1. W7-AS (2,1) tearing** (§3.1, Figs. 1–3). GVEC equilibrium with the
toroidal current of Fig. 28 of Weller et al. added to vacuum
$\iota\approx0.34$, giving $\iota=0.5$ ($\iota$ peaks ≈0.57 near
$s\approx0.45$). $\hat v_\parallel=0$, no viscosity (linear),
$n_i=10^{20}$ m⁻³, $\eta=k\times1.93\times10^{-6}$ Ω m with all
coefficients scaled by $k$ (constant magnetic Prandtl number), $D=0.154$,
$\kappa=0.231$ m²/s isotropic. JOREK $\eta$ ≈$6\times10^{-7}$–$2\times10^{-5}$
Ω m; $\gamma\sim10^4$ s⁻¹, following an $\eta^{0.6}$ reference at low $\eta$
and bending below it at high $\eta$; maximum deviation ≈3%. Nonlinear run:
saturation ≈3.5 ms (figure reading), island at 4.18 ms.

**T2. Interchange, $l=2$ low-shear stellarator** (§3.2, Figs. 4–7). Five
periods, ellipticity 1.6, $\iota$ 0.64–0.71 crossing 2/3,
$\eta=1.93\times10^{-8}$ Ω m, no viscosity (near-ideal).

| Run | Result |
|---|---|
| $\Gamma=0$, (15,10) mode | $\gamma$ to ≈$1.0\times10^5$ s⁻¹ at β ≈ 0.86%, agrees with CASTOR3D |
| $\Gamma=5/3$, no $\hat v_\parallel$ | $n=15$ ≈0.7 vs 1.0 × 10⁵ s⁻¹ near β ≈ 1% (figure reading) |
| $\Gamma=5/3$, with $\hat v_\parallel$ | agrees; larger error at 0.86% from the (7,5) structure |
| full torus, β = 0.86%, with $\hat v_\parallel$ | $n=2$–15 within 10%, ≈0.4–1.0 × 10⁵ s⁻¹; $n=2$ structure matches CASTOR3D's (3,2) |
| full torus, no $\hat v_\parallel$ | $n<7$ missing; $n=7$ ≈0.42 vs 0.58 × 10⁵ s⁻¹ |
| CASTOR3D $n=5$ free-boundary mode | faster than internal modes above β ≈ 0.6% (≈1.5 × 10⁵ s⁻¹ at 1.3%) |

**T3. W7-AS soft β limit** (§4, Figs. 8–13). Experiment: $B\approx0.9$ T,
$n\approx2\times10^{20}$ m⁻³, $T\sim100$ eV, 3.2 MW from two counter-directed
NBI sources (no momentum source); MHD activity suppressed above β ≈ 2.5%;
experimental β limit 3.4%; low-$n$ activity at 1.5% < β < 2.5%.

* Simplified scan (single period, no $\hat v_\parallel$,
  $\eta=1.93\times10^{-6}$ Ω m, $D_\parallel=1540$,
  $\kappa_\parallel=2.31\times10^6$ m²/s): 1 and 4 kPa flatten at β ≈ 1.55% and
  1.8% (figure; text "> 1.3 %"); 8 kPa ≈2.1%; 10 kPa capped at ≈2.35%. At
  10 kPa: $\eta\times10$ → β falls; $7.384\times10^{-7}$ → ≈2.8%;
  $1.9382\times10^{-7}$ → ≈3.4% by 3.5 ms.
* Experimental approximation, 10 kPa (axis $T=0.31$ keV, $n=2\times10^{20}$,
  $\eta=3.49\times10^{-7}$ Ω m, $\nu_\perp=6.46\times10^{-9}$,
  $\nu_\parallel=5.15\times10^{-7}$ kg m⁻¹ s⁻¹,
  $\kappa_\parallel=4.52\times10^7$ m²/s, with $\hat v_\parallel$): converged
  for maximum $n\ge50$; transient stochastization at ≈0.4 and 0.83 ms; β from
  2.25% to ≈2.6–2.7% in ≈1.1 ms, no flat top.
* Full torus, maximum $n=20$: (2,1) island at 0.46 ms for
  $\eta=1.93\times10^{-5}$ with falling $N_f=0$ energy; at Spitzer $\eta$
  $N_f=2$ dominates after ≈0.6 ms, good core surfaces at 0.80 ms.

# Notation map

| Ramasamy et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\chi$, $B_v=\lvert\nabla\chi\rvert$ | $\chi$, $\lvert\nabla\chi\rvert$ | finite-element Poisson solution here |
| $\Psi$ | $\psi_\chi$ | a length; not a poloidal flux |
| $\Phi$ | $u$ | **collision:** registry $\Phi$ is the electrostatic potential |
| $v_\parallel$ (in $\mathbf v=\dots+v_\parallel\mathbf B$) | $\hat v_\parallel$ (page-local) | **collision:** not $\mathbf v\cdot\mathbf b$; velocity per unit field |
| $\omega=\Delta^\perp\Phi$ | $\varpi=\Delta^\perp u$ | **collision:** registry $\omega$ is a frequency |
| $j=\Delta^*\Psi$, $j_{\rm source}$ | $\mu_0j=\Delta^*\psi_\chi$, $j_{\mathrm{src}}$ | JOREK units, $\mu_0=1$; stellarator $\Delta^*$ relative to $\nabla\chi$ |
| "$\nabla^*$" (operator list) | $\Delta^*$ | printed label slip |
| $\rho$; table "$n$" | $\rho$; $n_i$ | **collision:** registry $n$ is the toroidal mode number |
| $T$ | $T$ (total, $T_e+T_i$) | $p=\rho T$ in normalized units |
| $\eta$, $\eta_{\rm num}$, $\eta_{\rm Ohm}$ | $\eta$, $\eta_h$, words | |
| $\mu_\perp$, $\mu_{\rm num}$ | $\nu_\perp$, $\nu_h$ | dynamic (kg m⁻¹ s⁻¹); **collision:** registry $\mu$ is the magnetic moment |
| $\mu_{\parallel,\perp}$, $\mu_{\parallel,\parallel}$ | $\nu_{\parallel\perp}$, $\nu_{\parallel\parallel}$ | |
| $P$ (density source term) | $\nabla\cdot(\mathsf D\nabla\rho)+S_\rho$ | |
| $S_e$ | $S_p$ | 3.2 MW |
| $\kappa_\perp$, $\kappa_\parallel$ | $\kappa_\perp$, $\kappa_\parallel$ | diffusivities (m²/s) |
| $\iota_{\rm ext}$ | words (vacuum rotational transform) | |
| $\hat\psi_t$, $\psi_{t,0}$ | $\psi_{t,N}$, initial toroidal flux | radius $\sqrt{\psi_{t,N}}$ |
| $s$, $t$, $\phi$, $J$ (Eqs. 10–11) | words (element coordinates, Jacobian) | **collision:** registry $s$ is a radial label |
| $\hat E_{{\rm mag},n}$, $\hat E_{{\rm kin},n}$ | $W_{\mathrm{mag}}^{(n)}$, $W_{\mathrm{kin}}^{(n)}$ | normalized |
| $N_f$ | words (toroidal mode family, $n \bmod N_{\mathrm{fp}}$) | not in the registry |
| $n_{\rm tor}$ | words (highest toroidal mode number) | **collision:** registry $N_{\mathrm{tor}}$ counts harmonics |
| $\xi_\perp=\mathbf v\cdot\nabla s$ | words (eigenfunction) | |
| $l$, $k$ | words (coil multipolarity, coefficient scale factor) | |

# Pages created or updated

Chunk 2 (2026-10-16) created or updated the pages below. This source is cited on:

* [Ballooning mode](/definitions/ballooning-mode.md)
* [Bézier–Hermite finite elements with toroidal Fourier harmonics](/methods/bezier-finite-elements.md)
* [CASTOR3D](/software/castor3d.md)
* [Divergence-free magnetic field](/properties/divergence-free-magnetic-field.md)
* [Dommaschk potentials for the vacuum field](/methods/dommaschk-potentials.md)
* [Free-boundary and resistive-wall coupling](/methods/resistive-wall-coupling.md)
* [Implicit time integration and preconditioned Krylov solvers for nonlinear MHD](/methods/implicit-time-integration.md)
* [Interchange modes and the Mercier criterion](/definitions/interchange-mode.md)
* [JOREK](/software/jorek.md)
* [JOREK3D](/software/jorek3d.md)
* [Linear MHD eigenvalue codes](/methods/linear-mhd-eigenvalue-codes.md)
* [MIPS](/software/mips.md)
* [Reduced MHD for stellarators](/methods/stellarator-reduced-mhd.md)
* [Reduced MHD for tokamaks](/methods/reduced-mhd.md)
* [Resistive internal kink (m/n = 1/1)](/definitions/resistive-internal-kink.md)
* [Resistive tearing mode](/definitions/tearing-mode.md)
* [Soft β limit of stellarators](/definitions/soft-beta-limit.md)
* [Three-dimensional inverse equilibrium solvers](/methods/inverse-equilibrium-solvers.md)
* [Toroidal mode families in stellarators](/definitions/toroidal-mode-family.md)
* [VMEC](/software/vmec.md)

# Citations

1. `/home/stefano/papers/mosaic/fusion-mhd-simulation/2024_Crossref_Nuclear_Fusion_Ramasamy_Nonlinear_MHD_modeling_of_soft_β_limits_in_W7-AS.pdf`
   * **Version.** arXiv:2402.02881v1 [physics.plasm-ph], 5 February 2024,
     "Submitted to: Nucl. Fusion", 18 pages: the pre-refereeing submission
     (the only arXiv version), although the file name says "Crossref". The
     published text, figures and numbers may differ.
   * **Identity.** doi:10.1088/1741-4326/ad56a1, checked on Crossref: title,
     the seven authors in printed order plus a collective-author slot, Nucl.
     Fusion 64(8), article 086030, issue 1 August 2024 (online 26 June 2024).
     The JOREK team is listed by reference to [1] (`hoelzl-2021`). The
     bibliography already held `ramasamy-2024` as cited by `hoelzl-2024`.
   * **How read.** Full text; Eqs. 1–11 checked on the rendered page 4 at
     220 dpi; all tables and figures inspected. Figure values are
     approximate readings.
   * **Recorded as printed.**
     * Table 1 gives the nonlinear tearing run $\eta=1.93\times10^{-6}$ Ω m
       (and hyper-resistivity $1.93\times10^{-12}$); the text and Fig. 3
       caption say $1.93\times10^{-5}$. The nonlinear $\mu_\perp$ is 100× the
       linear $k=1$ value, so "keeping the magnetic Prandtl number constant"
       applies to the linear scan only.
     * Operator list (§2.3): unclosed parentheses in
       "$\nabla_\parallel=B^{-2}\mathbf B(\mathbf B\cdot\nabla,$" and
       "$\nabla^*=B_v^{-2}\nabla\cdot(B_v^2\nabla^\perp$"; the second is
       labelled $\nabla^*$ but Eq. 8 uses $\Delta^*$.
     * Eq. 5: the leading $\rho$ in "$\rho B^2\partial(\rho v_\parallel)/\partial t$"
       makes the term dimensionally inconsistent with the rest; presumably
       $B^2\partial_t(\rho v_\parallel)$ (compiler's check).
     * Eq. 7: resistive and hyper-resistive signs are opposite to Nikulsin et
       al. (2022), Eq. 3d; here both are diffusive with $j=\Delta^*\Psi$
       (compiler's check). The normalization of the equations is not stated;
       parameter tables are SI.
     * §4.3 figure cross-references: "temperature profiles in Figure 9 (b)"
       should be Fig. 10(b); the conductivity scans "in Figure 9" and "the
       green line in Figure 10" should be Fig. 11.
     * §3.2 calls β = 0.86% "the largest β value simulated in JOREK", yet
       Fig. 5b has JOREK points without parallel flow at β ≈ 1.03%.
     * Fig. 7c legend $\eta=10^{-8}$ against Table 2 $1.93\times10^{-8}$ Ω m.
     * Fig. 9 legend $1.9382\times10^{-7}$, $7.384\times10^{-7}$,
       $1.9382\times10^{-5}$ Ω m against the text's $1.93\times10^{-7}$; the
       $7.384\times10^{-7}$ case is not mentioned in the text; "the
       experimental β limit can be exceeded" is marginal (the curve reaches
       3.4% at the end of the plotted time).
     * "Baseline" means the central column of Table 3 in §4.2 but the
       right-hand (experimental approximation) column in the Fig. 12 caption.
     * The intermediate-β range is printed "1.5% < β < 2.5%" (§4) and
       "1.5 ≤ β ≤ 2.5" (§4.4). The activity-suppression value (≈2.5%) and the
       β limit (3.4%) are distinct quantities.
     * "Soft β limit is observed" (abstract, §4.5, §5) while β keeps rising
       with no flat top in the experimental-parameter runs.
     * Table 2 prints $\kappa_\parallel$ "2310000".
     * The re-attribution of the earlier mismatch to CASTOR3D poloidal
       resolution (claim 8) is given without data.
     * Typos: "Afvénic", "stochasation", "indiates", "the initial the rate";
       ref. [11] spells "Huysmans".
   * **Reference list.** 35 printed entries (titles only for [8], [12], [16],
     [22], [26], [28], [29]), merged into the bibliography under
     `ramasamy-2024`. The Nikulsin 2021 PhD thesis [12] is `nikulsin-2021-b`
     (`nikulsin-2021` is a different work); [20] Pamela et al. JCP 464:111101
     and [21] Holod et al. PPCF 63:114002 are the existing `pamela-2022` and
     `holod-2021`; [11] "Huysmans" is `huysmans-2009`; [26] is
     `ramasamy-2023-b`; [25] is a private communication (`nuehrenberg-2023`);
     [22] a presentation (`hindenlang-2019`). Collective or garbled authors
     ("Team J", "Contributors J", "mod Team R", "Team N, Team E, Team W A",
     "W VII-A Team") are recorded as printed.
