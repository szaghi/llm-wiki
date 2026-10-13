---
type: Source
title: "van Leer (1979) — Towards the ultimate conservative difference scheme. V. A second-order sequel to Godunov's method"
description: "MUSCL: a second-order extension of Godunov's method for ideal compressible flow, as a Lagrangean step on piecewise-linear slabs with independently stored slopes, an iterated interface Riemann problem with one-step characteristic time-centring, and a least-squares remap, with slope-limiting monotonicity algorithms; tested on Sod's shock tube and a Mach 3 wind tunnel with a step."
resource: "doi:10.1016/0021-9991(79)90145-1"
source_kind: paper
authors: [van Leer B.]
year: 1979
venue: "J. Comput. Phys. 32:101–136"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1979-JCP-VanLeer-1010160021-99917990145-1.pdf"
tags: [godunov, reconstruction, limiter, finite-volume, euler, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper builds the second-order extension of Godunov's method for ideal
compressible flow. Its core is a 1D **Lagrangean** scheme in the mass
coordinate. Each gas slab carries a **linear** distribution of specific
volume, velocity and energy (pressure in the step itself): a slab average
plus a slope that is **stored independently**, where Godunov uses a
uniform distribution (§§1, 2.2). Slabs interact through the interface
discontinuity, resolved as Godunov's Riemann problem with a faster
iteration. The characteristic equations then give first time derivatives
at the interface, and a half-step time-centring gives second order in time
in **one step** (§§2.3–2.4). The Lagrangean results are **remapped** to the
Eulerian grid by least-squares (moment) fitting in a separate step (§3.2).
Slope-limiting "monotonicity algorithms" keep the slabs from creating new
extrema (§3.3). Multi-D uses Strang splitting (§3.4). The code, written by
P. R. Woodward, is named **MUSCL**, "Monotonic Upstream-centered Scheme for
Conservation Laws" (§1). Tests: Sod's shock tube and a Mach 3 wind tunnel
with a step, with a comparison against Godunov's method (§4). Merged into
the new [MUSCL](/methods/muscl.md) page and into
[finite-volume reconstruction](/methods/finite-volume-reconstruction.md),
[PPM](/methods/ppm.md) and the [Sod shock tube](/benchmarks/sod-shock-tube.md).

# Key claims

1. **Name and origin** (§1, p. 102). "An all-purpose computer code for
   compressible gas dynamics, by the name of MUSCL (Monotonic
   Upstream-centered Scheme for Conservation Laws), was written along the
   above lines by P. R. Woodward at Leiden Observatory." The separate remap
   step was Woodward's idea (Acknowledgments); the remap technique as such
   "originated with the group of W.F. Noh at Livermore" (§3.2).
2. **Piecewise-linear slabs with stored slopes** (§2.2, eqs. 39–41, p. 107).
   Each slab carries its average and its slab-averaged gradient,
   $\mathcal P_i = \bar u_i + \hat u^{(1)}_i\zeta$ in registry form. The
   slopes are "independent of the slab averages; they can not be derived
   from the latter and must be stored separately". Six data per slab are
   kept (averages and slopes of specific volume, velocity and specific total
   energy). Setting all slopes to zero gives Godunov's scheme: "This accounts
   for the first-order accuracy of Godunov's scheme".
3. **Pressure in place of energy** (eqs. 47–48, p. 107). The Lagrangean step
   distributes specific volume, velocity and pressure, with the slab
   pressure from the averages to $O(h^2)$. The more accurate eqs. 43–46γ are
   not used because they would make the monotonicity algorithm implicit in
   $p$.
4. **Conservative update** (eqs. 49–51). Exact for slab averages
   "regardless of the presence of discontinuities in the slab"; the
   time-averaged interface velocity, pressure and position are needed to
   $O(\Delta t^2)$. Slopes are updated by interface differencing (the
   difference of the two new interface values, eq. 51.5), called a
   "temporary substitute" for least-squares fitting.
5. **Interface Riemann problem** (§2.3, eqs. 54–61; App. A). The interface
   states are the slab profiles evaluated at the interface. The Lagrangean
   jump conditions give $p_*$ and $v_{n*}$ in terms of the Lagrangean wave
   speeds (mass fluxes through the waves; eqs. 31γ for a shock, 34γ for a
   rarefaction). The iteration starts from the acoustic guess (eq. 60)
   $$p_* \approx \frac{(\rho c)^+ p^- + (\rho c)^- p^+ - (\rho c)^-(\rho c)^+(v_n^+ - v_n^-)}{(\rho c)^- + (\rho c)^+}.$$
   Godunov's chord iteration gains a factor of the order of the data jumps
   per cycle; the tangent (Newton-type) iteration adopted, suggested by
   P. J. Bedijn, gains their square (pp. 109–110; eqs. A1–A3). Pressure is
   floored for cavitation (Fig. A4).
6. **Iterate only near shocks** (p. 110). In smooth flow the interface jumps
   are $O(h^3)$, against $O(h)$ for Godunov, so the acoustic guess "is more
   than adequate". MUSCL iterates only if the guess differs from the
   neighbouring pressures by more than 1 %, until successive iterates agree
   within 1.5 %; this cost 2–3 % of the Lagrangean step on the shock tube. A
   poor star state inside a shock structure enhances post-shock
   oscillations, "an effect also known for Godunov's method".
7. **Second order in time in one step** (§§2.3–2.4, eqs. 64–90). Time
   derivatives of the resolved interface state come from the characteristic
   equations written at a discontinuity (eqs. 64–66, derived in his ref.
   [17]), with the slab slopes as space derivatives on each side. A half
   step, e.g. $v_{n*} + \tfrac12\Delta t\,\partial_t v_{n*}$ (eq. 70), gives
   time-centred interface values, and the full step is accurate to
   $O(\Delta t^3)$ per step. No multi-stage integrator is used.
8. **Upwind character** (p. 111; App. B, p. 134). The Riemann invariants are
   updated by "a second-order upstream-centered (upwind) difference formula
   resembling Fromm's scheme". With slab-average slopes the scheme "boils
   down to the upstream-centered second-order scheme of Fromm", as
   Godunov's reduces to Courant–Isaacson–Rees.
9. **Monotonicity algorithm, Lagrangean step** (§3.3, eq. 101, Fig. 3). In
   registry form, with $\hat u^{(1)}_i$ the stored undivided slope,
   $$\hat u^{(1)}_i \leftarrow \operatorname{minmod}\left(2\Delta^1\bar u_{i-1},\ \hat u^{(1)}_i,\ 2\Delta^1\bar u_i\right),$$
   applied to specific volume, velocity and pressure at the start of each
   Lagrangean step. The stated rules (p. 117): the linear distribution must
   not take values beyond the neighbouring averages; the slope is zero at an
   extremum of the averages; the slope is zero if its sign disagrees with
   the trend of the averages. They "also guarantee the preservation of
   positivity". The paper does **not** claim monotonicity for the system:
   "the nonlinearity of slab interactions makes it impossible to fully
   guarantee monotonicity, especially for the largest allowed time steps"
   (p. 118). The factors 2 may be lowered for stronger limiting, "not beyond
   $1 + O(\Delta Q)$, lest the scheme lose its second-order accuracy", or
   made to decrease with the Lagrangean Courant number; with factors 0 the
   scheme is Godunov's.
10. **Monotonicity algorithm, remap** (eqs. 102–103, Fig. 4). The factors 2
    are divided by the fraction of the slab's mass that crosses the
    Eulerian boundary and by the fraction that stays. The rule: the averages
    over the crossing part and over the remaining part must each stay within
    the neighbouring averages; values inside the slab may exceed them, and
    "positivity is guaranteed only for the zone averages" (p. 119). The
    density slope is limited with the volume fraction instead.
11. **Peak clipping** (pp. 119–120, eq. 104, Fig. 5). Algorithms (101) and
    (102) "will clip real peaks to the same degree as a first-order method
    would do", notably at reflecting boundaries. For purely Lagrangean runs
    the paper tries a narrow-base variant built on the saved interface
    values: the same limiting as (101) near a plateau, weaker near a peak.
12. **Remap by moment fitting** (§3.2, eqs. 92–100). Zeroth and first
    moments are conserved; density is remapped over the volume coordinate,
    which avoids a quadratic solve. The step condition
    $\Delta t \le \min(h/\vert v_x\vert,\ h/c)$ to leading order (eq. 99) is
    "less stringent than the usual condition for a fully Eulerian scheme",
    $\Delta t \le h/(\vert v_x\vert + c)$ (eq. 100), plus a zone-tangling
    condition (eq. 100.5). The remap costs 0.55 of the Lagrangean step in 1D
    and 0.75 in 2D (p. 117).
13. **Slope options** (App. B, eqs. B1–B5). Slab-average central
    differencing, $\hat u^{(1)}_i = \tfrac12(\bar u_{i+1} - \bar u_{i-1})$
    (eq. B1, "scheme I"); interface differencing ("scheme II"); moment
    fitting ("scheme III"). Per the linear analysis of his ref. [2], moment
    fitting is "vastly superior", with a convective error smaller "by two
    orders of $\Delta\xi$"; I and II have equal convective errors, and II's
    largest dissipative error is 3 times smaller than I's and 3 times larger
    than III's. The **harmonic-mean slope** (eq. B2),
    $$\hat u^{(1)}_i = \frac{2\,\Delta^1\bar u_{i-1}\,\Delta^1\bar u_i}{\Delta^1\bar u_{i-1} + \Delta^1\bar u_i}$$
    if the two differences have one sign, else 0, "automatically" meets the
    crudest monotonicity condition. A continuous piecewise-quadratic option
    (eq. B5) matches scheme III's errors but was not implemented for gas
    dynamics.
14. **Efficiency** (§§1, 4). In 2D, even on coarse grids, the method is "at
    least an order of magnitude more efficient than Godunov's method".
    Carrying two data per quantity per dimension "potentially has the effect
    of a mesh refinement of a factor two" (p. 102). MUSCL is 15–20 % slower
    than the SHASTA-based code ALFVEN in absolute advancement (pp. 102, 129).

# Tests

1. **Sod shock tube** (§4, Fig. 6, pp. 121–123). Velocity 0;
   $\rho = p = 1$ for $x < 0.5$; $\rho = 0.125$, $p = 0.1$ for $x > 0.5$;
   $\gamma = 1.4$; $\nu = 0.9$; $h = 0.01$ (100 cells on $[0, 1]$). Output
   after **34 steps at $t = 0.14154$**, when the right-moving shock "has
   approximately reached $x = 0.75$". Cell averages of $\rho$, velocity,
   $p$ and specific internal energy against the exact solution; no error
   norms. Claimed "superior to all methods tested by Sod, including
   Phoenical SHASTA", which Sod ran at too high a Courant number for
   monotonicity. 0.47 s per step on an IBM 370/158, 0.17 s on a CDC 6600.
2. **Mach 3 wind tunnel with a step** (§4, Figs. 7–11, pp. 123–129; runs by
   P. R. Woodward). Impulsive start, inflow velocity 3 with sound speed 1,
   free outflow, step height one fifth of the entrance height, square
   zones, $\Delta t$ at 90 % of the limit (99), $\gamma = 1.4$; pressure
   contours.
   * $60\times20$ (step 4 zones), 452 steps, $t = 4.01$ entrance heights over
     inflow sound speed (Fig. 7); $30\times10$, 194 steps, $t = 4.03$
     (Fig. 8); $15\times5$, 86 steps, $t = 4.06$ (Fig. 9), where the
     visible Mach stem "is an artifact due to the monotonicity algorithms
     (101) and (102) which force pressure contours to be perpendicular to a
     reflecting wall".
   * Steady state at $t = 16.02$ on $45\times15$, 1244 steps (Fig. 10).
   * Godunov's method, run in the MUSCL code with all slopes zeroed:
     $80\times30$, 429 steps, $t = 4.02$ (Fig. 11). Godunov at 30 zones of
     entrance height is mimicked by MUSCL at 10, and Godunov "will not run
     more than twice as fast as MUSCL" (p. 123).
   * The flows at $t \approx 4$ "are far from stationary". 8.78 s per step on
     the IBM 370/158 for the 1008 cells of Fig. 7. Provisional runs by
     Woodward with least-squares slopes and the limiter (104) in the
     Lagrangean step show "a dramatic increase in accuracy for coarse grids"
     (p. 129).

# Notation map

| van Leer (1979) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\xi$ (mass coordinate) | words ("mass coordinate") | **Collision:** registry $\xi$ is the scaled wavenumber |
| $x$; $X = x^{\alpha+1}/(\alpha+1)$ | $x$; words ("volume coordinate") | **Collision:** $\mathbf X$ is the mapped-grid coordinate |
| $\alpha = 0, 1, 2$ (geometry) | words | **Collision:** $\alpha$ is the Lax–Friedrichs speed |
| $V$ (specific volume) | $1/\rho$ | **Collision:** $V_i$ is the Voronoi neighbourhood |
| $u$ (velocity) | $v_x$; $v_n$ at an interface | **Collision:** registry $u$ is the conserved state |
| $E$, $e$ (specific total, internal energy) | $E/\rho$; words | registry $E$ is an energy density |
| $p$, $\gamma$, $c$ | $p$, $\gamma$, $c$ | same |
| $C = c/V$ (Lagrangean sound speed) | $\rho c$ | acoustic impedance |
| $W$ (Lagrangean wave speed) | words | mass flux through a wave; no registry symbol |
| $u^*$, $p^*$; $V^*_{i\pm}$ | $v_{n*}$, $p_*$; $1/\rho_{*L}$, $1/\rho_{*R}$ | star region |
| interfaces $i$, slabs $i+1/2$ | interfaces $i+1/2$, cells $i$ | **Index shift:** the paper's convention is the reverse of the registry's |
| $i_-$, $i_+$ (sides of interface $i$) | $u^-_{i+1/2}$, $u^+_{i+1/2}$ | with the index shift |
| $\bar Q_{i+1/2}$ | $\bar u_i$ | slab average |
| $\bar\Delta_{i+1/2}Q$ (undivided slab slope) | $\hat u^{(1)}_i$ | first Legendre moment, $P_1 = \zeta$ |
| $\Delta_i\bar Q = \bar Q_{i+1/2} - \bar Q_{i-1/2}$ | $\Delta^1\bar u_{i-1}$ | **Collision:** an unsuperscripted $\Delta$ is the PPM jump |
| $\langle Q\rangle_i$ (time average over a step) | written out | **Collision:** registry $\langle w\rangle_i$ is a space average |
| eq. 101 with the B1 slope | $\delta^{\mathrm{MC}}\bar u_i$ | algebraic identity; the paper does not use the name |
| eq. B2 | words ("harmonic-mean slope") | no registry symbol |
| $\varphi_{i+1}$, $f_{i+1}$ (crossing mass and volume fractions) | words | **Collision:** $\varphi_{\mathrm p}$, $\varphi_{\mathrm g}$ |
| $\sigma = c\,\Delta t/\Delta x$ | $\nu$ | **Collision:** $\sigma$ is the flux-limiter constant |
| $J^\pm$, $S$ | words ("Riemann invariants", "entropy") | **Collision:** $S$ is the Rusanov speed |
| $Z_\pm$ (tangent slopes, App. A) | words | |

# Pages created or updated

* Created [MUSCL](/methods/muscl.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md) (origin of the stored-slope linear reconstruction, the limiters as printed).
* Updated [Piecewise parabolic method (PPM)](/methods/ppm.md) (what PPM inherits from MUSCL).
* Updated [Sod shock tube](/benchmarks/sod-shock-tube.md) (printed diaphragm position and end time).
* Updated [Total variation diminishing](/properties/total-variation-diminishing.md) (batch-14 block: no TVD claim; monotonicity not guaranteed for the system; clipping of extrema).
* Updated [Exact Riemann solver for the Euler equations](/methods/exact-riemann-solver.md) (batch-14 block: the acoustic guess and the tangent iteration of App. A).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md) (batch-14 block: the Mach 3 step runs of §4, Figs. 7–11).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1979-JCP-VanLeer-1010160021-99917990145-1.pdf`.
   * **Version read.** The published journal article, a 36-page Academic
     Press scan (Acrobat Capture 2003) with a text layer; not a preprint.
   * **Identity.** doi:10.1016/0021-9991(79)90145-1, from the PDF's PII and
     checked on Crossref: J. Comput. Phys. 32(1):101–136, July 1979, sole
     author Bram van Leer (University Observatory, Leiden), reference count
     20; all fields agree with page 1. Received 18 October 1977, revised 17
     October 1978.
   * **How it was read.** `pdftotext -layout` for prose; every equation
     quoted here read from page images at 110 dpi (journal pp. 105–112,
     117, 119–120, 133, 134, 136 and the figure captions on pp. 125–128).
     Not reproduced: eqs. 65–66 (characteristic equations at a
     discontinuity, described in words only), eqs. 43–46γ (unused by the
     paper), eqs. 94–98 (remap moments; garbled text layer, not rendered),
     and eq. A2γ in full. Figures were not read quantitatively.
   * **Recorded as printed.**
     - Appendix B (p. 134) cites Fromm as [12] and Courant–Isaacson–Rees as
       [15]; the reference list has Fromm (1968) as [11] and CIR as [14],
       so the Appendix B numbers are off by one.
     - Fig. 11 prints an $80\times30$ grid for Godunov's run, shorter than
       the $90\times30$ a tunnel three entrance heights long would need; the
       plotted axis ends near 64 zones. Not reconciled.
     - The "1008-cell grid of Fig. 7" is consistent: $60\times20$ minus the
       $48\times4$ cells of the step block.
     - Citing sources print the title with "Conservation"; page 1 and
       Crossref read "Conservative".
   * **Reference list:** 20 entries, all merged. The bibliography title was
     corrected from page 1 ("Conservative", not "Conservation") and the
     Crossref DOI added. The Russian original of Godunov, Zabrodin &
     Prokopov (Ž. Vyčisl. Mat. i Mat. Fiz. 1:1020) is merged into
     `godunov-1961`, which carries the translation's pagination. Boris's NRL
     Memorandum Report 3237 (1976) is `boris-1976-b`, not Boris & Book's
     FCT III (`boris-1976`). Bibliography after the batch: 3104 entries.
