---
type: Source
title: "Woodward & Colella (1984) — The Numerical Simulation of Two-Dimensional Fluid Flow with Strong Shocks"
description: "Review comparing seven difference schemes (MacCormack with Lapidus viscosity, BBC, ETBFCT, first-order Godunov, MUSCL, and PPM in Lagrange-plus-remap and direct-Eulerian forms) on three strong-shock problems it fixes as benchmarks — the interacting blast waves with a measured L1 error, the Emery Mach 3 step with a corner treatment, and the double Mach reflection of a Mach 10 shock — finding PPM first in accuracy per zone and per CPU second."
resource: "doi:10.1016/0021-9991(84)90142-6"
source_kind: paper
authors: [Woodward P., Colella P.]
year: 1984
venue: "J. Comput. Phys. 54:115–173"
local_file: "/home/stefano/papers/mosaic/astrophysical-simulation-codes/1984-JCP-Woodward-1010160021-99918490142-6.pdf"
tags: [hydro, benchmark, verification, reconstruction, riemann-solver]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper compares seven difference schemes on three problems with
strong shocks (Mach ≥ 3) in a $\gamma = 1.4$ gas on uniform square
Cartesian grids; every 2D scheme is a symmetrized product of 1D
operators, and adaptive meshes are excluded on purpose. The schemes stand
for three ways of treating discontinuities: artificial viscosity
(MacCormack with a Lapidus viscosity; BBC, a von Neumann–Richtmyer
Lagrangian step with a MUSCL-type remap), linear hybridization (Boris's
ETBFCT flux-corrected transport) and Godunov's approach (first-order
Godunov, a single-step Eulerian MUSCL, and [PPM](/methods/ppm.md) as
Lagrange-plus-remap PPMLR and direct-Eulerian PPMDE). It introduces the
[interacting blast waves](/benchmarks/interacting-blast-waves.md) with a
measured L1 error and convergence rates, and fixes two 2D tests: the
Emery Mach 3 step, with a corner treatment, and the
[double Mach reflection](/benchmarks/double-mach-reflection.md). PPM ranks
first in accuracy per zone and per CPU second. A Lagrange-plus-remap
scheme matches the direct-Eulerian one only when the remap is one order
more accurate than the Lagrangian step.

# Key claims

1. **Taxonomy** (§II–III). Artificial viscosity, linear hybridization
   (blending low- and high-order fluxes under a monotonicity constraint)
   and Godunov's approach (piecing together Riemann solutions). The random
   choice method is excluded: its 1D advantages "do not persist in its
   multidimensional formulations" (p. 118).
2. **Godunov-type structure** (§IIIc, pp. 122–123). Interpolation
   polynomials from zone averages; Riemann input states that represent the
   domains of dependence swept by the characteristics during the step;
   fluxes averaged over the step. "The order of these polynomials
   determines the spatial order of accuracy."
3. **Cost** (p. 123). First-order Godunov costs "about twice as much
   computer time per zone per time step" as MacCormack with artificial
   viscosity. Hybridizing PPM with simple difference equations in smooth
   zones gains "a factor of two" on a CRAY-1 and "about three" on a more
   favourable computer.
4. **Linear hybridization on systems** (pp. 120–121, 156, 166). The
   monotonicity constraint has no basis in the differential equations; it
   turns smooth strong gradients into staircases. ETBFCT keeps density,
   momenta and total energy monotone but not the pressure, so negative
   pre-shock pressures are reset to floors; inside shocks the specific
   internal energy reaches "twice its post-shock value".
5. **Interacting blast waves converge slowly** (§VIa, Table I, p. 146).
   "Only the error of the PPM scheme converges to zero as fast as
   $\Delta x$. All the other schemes show less than linear convergence."
   Because the error concentrates at discontinuities, it can converge "no
   faster than $\Delta x$".
6. **Efficiency** (p. 146). Matching the 200-zone PPMLR accuracy costs
   1.6 (PPMDE), 6.2 (MUSCL), 7.4 (BBC), 8.0 (MacCormack) and 13.5 (ETBFCT)
   times the CPU time, with 256, 563, 845, 1093 and 1431 zones (PPMDE,
   MUSCL, ETBFCT, BBC, MacCormack); Godunov cannot match it "even if it is
   given twelve times as many zones".
7. **Ranking** (§VII, p. 166). By accuracy on a given grid: PPM (both
   forms), MUSCL, ETBFCT, BBC, MacCormack, Godunov. By accuracy per CRAY-1
   CPU time, BBC and MacCormack move ahead of ETBFCT in 1D; "roughly the
   same ordering" is judged to hold in 2D.
8. **Strong, slowly moving grid-aligned shocks are unstable** (Figs. 7a,
   7e, 8, pp. 155–156). In Godunov and single-step MUSCL, noise is emitted
   where the shock moves from one zone column to the next; behind the Mach
   stem the Kelvin–Helmholtz instability of the slip line amplifies it. The
   cure is extra dissipation that broadens such shocks slightly: PPMLR uses
   flattening plus "jiggling" of the remap grid, PPMDE flattening plus a
   Lapidus viscosity of coefficient 0.1 (pp. 141, 156).
9. **Shock broadening in PPM** (§Vc, p. 141). Slowly moving strong shocks
   are broadened to "about 2 zone widths in the worst cases" to prevent
   post-shock oscillations of "about 1 to 2%". Flattening plus Lapidus
   viscosity 0.1 (a tenth of the coefficient used with MacCormack in 2D)
   gives a smooth-flow diffusive error that is "third-order small"; grid
   jiggling, "fifth-order small".
10. **Remap order** (§VII, pp. 165, 167–168, 157). PPMDE and PPMLR are equivalent
    in accuracy and cost; MUSCL and Godunov show no such equivalence. A remap
    should "be performed with one extra order of accuracy over the Lagrangian
    step"; the PPM remap is formally third order. Lagrange-plus-remap suits
    multifluid problems, single-step Eulerian "complicated spatially
    dependent source terms".
11. **Vanishing characteristic speeds** (p. 165, Fig. 10). Lagrange-plus-remap
    MUSCL does not oscillate at the steady shock, single-step MUSCL generates
    noise along the curved reflected shock; single-step MUSCL is more
    accurate overall.
12. **Riemann solver** (§Vc, pp. 141–142). Colella's approximate solver,
    which approximates rarefactions by rarefaction shocks, iterated by
    Newton's method: "more than two iterations are never required"; one
    suffices except for very strong shocks; two are used in the blast-wave
    problem. Single-step Eulerian codes need a special provision for
    spreading rarefaction fans. Approximate solvers such as Harten–Lax and
    Roe "will be in much greater demand when ... the equations of
    magnetohydrodynamics, are attacked".
13. **Sonic rarefaction shock in Godunov** (p. 157). An unphysical
    rarefaction shock forms in the centred fan where the flow is sonic,
    because the flux error at a sonic interface "is one order smaller than
    everywhere else".
14. **Time step of split Lagrange-plus-remap** (p. 147). For PPMLR and BBC
    the step is limited by "the maximum of the fluid velocity and the sound
    speed rather than by the maximum of their sum or difference".
15. **"Conservation of difficulty"** (§VII, p. 167). MacCormack is "about 6
    times faster than PPM" per zone; a doubly refined 2D grid needs at least
    8 times the zone updates, so MacCormack there needs "only 35% more
    computer time" than PPM on the original grid. In 2D the spread in
    accuracy per CPU second is much smaller than in accuracy per zone.
16. **Local mesh refinement** (§IIIa, p. 119). The Oliger, Gropp, Bolstad
    and Berger–Oliger approach saves memory "at the cost of introducing
    substantial program complexity"; time savings are "not as great as one
    might expect", refined regions "must be wider than one would suspect",
    and vector organization costs time. No assessment is attempted.
17. **BBC Lagrangian step** (Appendix, eqs. A1–A33). DeBar's KRAKEN step in
    1D sweeps on a staggered grid, sweep order x, y, y, x, all four with the
    same step for second order; an artificial viscosity with Noh's "linear
    q" term, which broadens the weak second Mach shock (p. 164); the remap
    uses a monotone MUSCL-type slope, because more accurate remaps give
    "impossibly high densities ranging from 8 to 10" in the blast-wave
    problem (p. 171).

# Tests

All in a $\gamma = 1.4$ gas; Courant number 0.8 for all schemes except
ETBFCT (0.4) in the blast waves, 0.8 for most runs elsewhere.

1. **[Two interacting blast waves](/benchmarks/interacting-blast-waves.md)**
   (§IVa, §VIa, Figs. 1–2, 6, Table I). Gas at rest between reflecting
   walls a unit apart; density 1; pressure 1000 for $x < 0.1$, 0.01 in the
   middle, 100 for $x > 0.9$. Reference: a special PPMLR run with three
   tracked fluids, the early phase computed exactly, local refinement by 8
   near the discontinuities and walls, 3096 zones of width 1/2400 with finer
   zones in $0.64 < x < 0.81$. Comparison time $t = 0.038$. Error: mean over
   the coarse zones of the absolute deviation of the zone-averaged density
   from the reference. Grids 100 to 2400 zones; Table I lists 200–1200:
   MacCormack 0.261 → 0.0862 (finest-pair rate 0.72), BBC 0.196 → 0.0717
   (0.64), ETBFCT 0.227 → 0.0606 (0.76), Godunov 0.330 → 0.182 (0.40),
   MUSCL 0.162 → 0.0401 (0.85), PPMDE 0.0990 → 0.0144 (1.07), PPMLR
   0.0760 → 0.0133 (0.98).
2. **Mach 3 wind tunnel with a step** (§IVb, §VIb, Figs. 3, 7–8; Emery
   1968). Tunnel 1 high and 3 long; step 0.2 high starting 0.6 from the
   inflow; inflow and initial state $\rho = 1.4$, $p = 1$, velocity 3;
   reflecting walls, zero-gradient outflow. **Corner treatment** (p. 131):
   in the first zone row above the step the first four zones right of the
   corner, and in the next row the first two, have density reset to the
   entropy of the zone just left of and below the corner and the velocity
   magnitude reset to match that zone's enthalpy plus kinetic energy per
   unit mass; it assumes nearly steady flow and is "clearly inappropriate
   at the very outset". Without it a one-zone numerical boundary layer forms
   above the step. Output every 0.5 to $t = 3$ and at $t = 4$; reference
   PPMLR at $h = 1/80$. Comparisons at $t = 4$ on $h = 1/20$, 1/40, 1/80:
   PPMDE matches BBC at twice and MacCormack at $2\sqrt2$ times the zones per
   direction (about 3.6 and 4.4 times more efficient); PPMLR takes 18 % more
   time (3.0 and 3.7).
3. **[Double Mach reflection](/benchmarks/double-mach-reflection.md)**
   (§IVc, §VIc, Figs. 4, 9–10). A Mach 10 shock that "initially makes a 60°
   angle with" the reflecting wall; undisturbed $\rho = 1.4$, $p = 1$; domain
   $[0,4]\times[0,1]$, the wall from $x = 1/6$; post-shock values on the
   bottom for $x < 1/6$ and on the left, exact shock motion on the top,
   zero gradients on the right; $t = 0.2$; grids $h = 1/30$, 1/60, 1/120.
   Fig. 4 is PPMDE at $h = 1/120$ with grid jiggling. A starting error from
   the one-zone initial and top-boundary shock mars all results. Even at
   $h = 1/120$ the wall jet is "less than five zones wide".

# Notation map

| Paper | Canonical | Note |
|---|---|---|
| $u$ ($u_x$), $v$ ($u_y$) | $\mathbf v = (v_x, v_y)$ | **collision**: registry $u$ is the state |
| $E$ | $E/\rho$ | the paper's $E$ is per unit mass |
| $\varepsilon$ | $e$ | specific internal energy |
| $V = 1/\rho$ | $1/\rho$ | specific volume |
| $c$, $c_i$ | $c_s$ | **collision**: $c$ is the speed of light |
| $A = p/\rho^\gamma$ | in words ("entropy function") | **collision** with the flux Jacobian $A(u)$ |
| $\Delta x$, $\Delta y$ | $h$ | uniform square zones |
| $N$ | $N$ | zones of a coarse grid |
| Courant number | $\nu$ | |
| $\epsilon$ (L1 density error) | in words | |
| $q$ (artificial viscous pressure) | in words | |
| $m$, $\Delta m_i$ | in words | Lagrangian mass coordinate |

# Pages created or updated

* Created this Source page.
* Created [Interacting blast waves](/benchmarks/interacting-blast-waves.md).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md):
  the printed set-up, boundary conditions and angle (60° to the wall);
  Berger & Colella's "4 times finer" checked (consistent in $h/t$; see the double Mach reflection page).
* Updated [PPM](/methods/ppm.md): the verification paper; the
  detector constants are not printed in it; Lapidus 0.1, shock broadening,
  remap order, Riemann iterations.
* Updated
  [approximate Riemann solvers](/methods/approximate-riemann-solvers.md),
  [Berger & Colella (1989)](/sources/berger-1989.md),
  [Colella & Woodward (1984)](/sources/colella-1984.md),
  [Fryxell et al. (2000)](/sources/fryxell-2000.md) and
  [FLASH](/software/flash.md).

# Citations

1. Woodward P., Colella P. (1984), "The numerical simulation of
   two-dimensional fluid flow with strong shocks", J. Comput. Phys.
   54(1):115–173, doi:10.1016/0021-9991(84)90142-6. Local file:
   `/home/stefano/papers/mosaic/astrophysical-simulation-codes/1984-JCP-Woodward-1010160021-99918490142-6.pdf`.
   * **Version read.** The published journal version ("Review Article";
     received 15 July 1982, revised 25 August 1983), a 59-page scan with an
     OCR text layer. Not a preprint.
   * **Identity.** Checked on Crossref: title, Woodward and Colella,
     vol. 54, issue 1, pp. 115–173, issued 1984-04.
   * **How it was read.** Text layer for the prose (clean); the error
     formula (p. 142), the Appendix eqs. A8–A18 (p. 169) and the reference
     list (pp. 172–173) from rendered pages. Figures were not reproduced;
     the Fig. 4 legend ($\Delta t = 3.14\times10^{-4}$, Courant number 0.800,
     $t = 0.200260$) was read from the OCR only. The Godunov convergence
     exponents on p. 146 are garbled; the values 0.15 and 0.40 are taken
     from the first and last Table I rates.
   * **Recorded as printed.** (a) p. 142 prints the comparison time as
     "0.38", a misprint for 0.038 (pp. 129, 141). (b) Godunov's Table I error
     at 600 zones (0.241) exceeds that at 400 (0.214). (c) Eq. A13 prints
     $16q_i$ inside the square root. (d) The paper credits the first
     appearance of the blast-wave problem to Woodward (1982), its ref. 21.
   * **Reference list:** 56 printed entries, merged complete. Colella's
     direct-Eulerian MUSCL "in press" is `colella-1985-c`; the PPM paper
     (printed without a page) is `colella-1984`; Gropp, printed 1:191, is
     `gropp-1980` (Crossref 10.1137/0901012; the existing entry carried
     4:191); Godunov et al. cited in the Russian original is `godunov-1961`;
     Bolstad "in preparation" is `bolstad-1982` (Stanford thesis, June 1982).
     Printed slips kept in the entries: ref. 7 spells the second author
     "Collela", ref. 23 prints the report number "LA-66640", ref. 35 the
     title with "Articial". Bibliography: 2407 entries.
