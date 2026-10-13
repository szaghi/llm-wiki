---
type: Source
title: "Woodward & Colella (1984) — The numerical simulation of two-dimensional fluid flow with strong shocks"
description: "Review comparing seven shock-capturing schemes (MacCormack with Lapidus viscosity, BBC, ETBFCT, Godunov, MUSCL, and PPM in Lagrange-plus-remap and single-step Eulerian forms) on the interacting blast waves, a Mach 3 wind tunnel with a step and the double Mach reflection, with exact set-ups, an L1 density error and CRAY-1 times; PPM is the most accurate per zone and per CPU second, and only PPM converges at first order on the blast waves."
resource: "doi:10.1016/0021-9991(84)90142-6"
source_kind: paper
authors: [Woodward P.R., Colella P.]
year: 1984
venue: "J. Comput. Phys. 54:115–173"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/1984-JCP-Woodward-1010160021-99918490142-6.pdf"
tags: [review, euler, strong-shocks, ppm, godunov, 2d, shock-instability]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

A systematic comparison, labelled "Review Article", of difference schemes
for gas dynamics with strong shocks ("strong" meaning substantial entropy
production, Mach 3 or more in air). All schemes run on uniform Cartesian
grids with square zones, $\gamma = 1.4$, and reach 2D by symmetrized
products of 1D operators. They represent three approaches to
discontinuities:
* artificial viscosity: MacCormack with Lapidus viscosity, and BBC, a von
  Neumann–Richtmyer staggered Lagrangian step plus a MUSCL-type remap
  (specified in the Appendix);
* linear hybridization: Boris's flux-corrected transport code ETBFCT;
* Godunov-type schemes: first-order Godunov, single-step Eulerian MUSCL,
  and [PPM](/methods/ppm.md) as a Lagrangian step plus remap (PPMLR) and
  as a single-step Eulerian scheme (PPMDE).

The tests are the 1D [interacting blast waves](/benchmarks/interacting-blast-waves.md),
the [Mach 3 wind tunnel with a step](/benchmarks/forward-facing-step.md)
and the [double Mach reflection](/benchmarks/double-mach-reflection.md),
with exact set-ups, a corner fix for the step, and a quantitative error
with CPU times for the 1D problem. The accuracy ordering is PPM, MUSCL,
ETBFCT, BBC, MacCormack, Godunov; formal order says little for these
flows. The companion paper is [Colella & Woodward (1984)](/sources/colella-1984.md).

# Key claims

1. **Three approaches** (§§II–III). Artificial viscosity smears shocks
   over three or more zones. Linear hybridization blends low- and
   high-order fluxes under a monotonicity constraint (Boris–Book,
   Zalesak). Godunov's approach builds the Riemann solution into the
   flux, whose fluxes agree with smooth-flow ones "up to and including
   terms of second order in the size of the jumps" (§IIIc). For 1D
   advection, MUSCL "is a linear hybridization technique" (§IIIb).
2. **Cost of Riemann solvers** (§IIIc). First-order Godunov costs about
   twice as much per zone-step as MacCormack with artificial viscosity.
   Hybridizing PPM with simpler equations in smooth zones gains at most a
   factor 2 on a CRAY-1, about 3 on a "more favorably organized computer".
3. **FCT pathologies** (§§IIIb, VIb–c). For systems the monotonicity
   constraint "is not implied by the differential equations". Applied to
   the conserved variables it turns steep smooth gradients into
   staircases. Monotone conserved variables do not imply monotone
   pressure: ETBFCT produces substantial negative pre-shock pressures,
   reset to floor values (§VIb), and inside shocks a specific internal
   energy up to twice its post-shock value (§VIc). MUSCL and PPM, which
   constrain $\rho$, $p$ and the velocity, do not.
4. **PPM ingredients** (§Vc, Fig. 5): a Riemann solver, high-order
   interpolation over the domain of dependence of each interface, and
   monotonicity constraints with discontinuity detectors. In Fig. 5 a
   strong shock that moves 3/4 of a zone per step stays one zone wide.
5. **Slowly moving strong shocks** (§Vc). When strong shocks move slowly
   relative to the grid (all wind-tunnel shocks after $t = 2$), PPM must
   broaden them to about 2 zones "in the worst cases" to prevent
   post-shock oscillations of about 1–2 % amplitude, whose wavelengths of
   many zones cannot be damped afterwards. Two cures: flattening plus
   "jiggling" the remap grid, a diffusive error that is fifth-order small;
   or flattening plus Lapidus viscosity with coefficient 0.1, an error
   third-order small in smooth flow.
6. **Riemann solver** (§Vc). Colella's approximate solver replaces
   rarefactions by rarefaction shocks; with Newton iteration it needs at
   most two iterations, one for all but very strong shocks. The authors
   expect Harten–Lax and Roe solvers to matter for MHD.
7. **Error measure** (§VIa, p. 142): the mean absolute difference of
   cell-average density from the reference over the coarse-grid zones.
   Because the errors sit at discontinuities spread over $O(h)$, it "can
   converge to zero no faster than $\Delta x$" (p. 146).
8. **Convergence against formal order** (§VIa, p. 146). Godunov's error
   converges like $h^{0.15}$ at first and $h^{0.4}$ on the finest grids;
   "only the error of the PPM scheme converges to zero as fast as
   $\Delta x$".
9. **Efficiency on the blast waves** (§VIa). Matching 200-zone PPMLR costs
   more CPU time by factors PPMDE 1.6, MUSCL 6.2, BBC 7.4, MacCormack 8.0,
   ETBFCT 13.5, with 256, 563, 1093, 1431 and 845 zones respectively;
   Godunov cannot match it even with 12 times the zones.
10. **PPMDE ≈ PPMLR** (§§VIb–VII). The two forms give nearly identical
    accuracy and cost, unlike MUSCL or Godunov; attributed to the
    third-order PPM remap and to the slight broadening of stationary
    shocks. The advice: remap "with one extra order of accuracy over the
    Lagrangian step".
11. **Single-step Eulerian sensitivity** (§VIc, Fig. 10). Single-step
    MUSCL generates noise along the nearly steady reflected shock of the
    double Mach reflection; MUSCL as Lagrange plus remap does not, but is
    less accurate there. This "demonstrates the extra sensitivity of
    single-step Eulerian schemes to vanishing characteristic speeds".
12. **Sonic rarefaction shock** (§VIb, p. 157). Godunov's scheme produces
    a small "unphysical rarefaction shock" in the centred fan where the
    $x$-sweep Mach number is 1, because the flux error at a sonic
    interface is one order smaller than elsewhere.
13. **2D shock instability** (§VIb, Figs. 7a, 7e, 8). Godunov and MUSCL
    show a "numerical instability of 2-D, strong, stationary shocks"
    nearly aligned with the mesh, near the bottom wall and behind the Mach
    stem. Noise is emitted where the shock jumps from one zone column to
    the next. In MUSCL the entropy perturbations from a kink running
    along the Mach shock are amplified by the physical Kelvin–Helmholtz
    instability of the slip line. The cure is more dissipation at such
    shocks.
14. **"Conservation of difficulty"** (§VII), a suspected principle.
    Artificial-viscosity schemes need about twice the zones per dimension
    and twice the steps, 8 times the zone updates in 2D; MacCormack being
    about 6 times faster than PPM per zone, it would need only "35% more
    computer time". The 1D blast-wave spread argues against the
    principle.
15. **Ordering** (§VII): 1. PPM (both forms), 2. MUSCL, 3. ETBFCT, 4. BBC,
    5. MacCormack, 6. Godunov, by accuracy on a given grid. By CPU time in
    1D, BBC and MacCormack move ahead of ETBFCT, mainly because ETBFCT
    needs a smaller time step; roughly the same ordering holds in 2D.
16. **BBC** (Appendix, eqs. A1–A33): a two-step staggered Lagrangian step
    with an artificial viscous pressure that includes a "linear" term
    (Noh), followed by a MUSCL-type remap with a monotone slope; a full 2D
    step is $x, y, y, x$ sweeps. More accurate van Leer remaps produce
    "impossibly high densities ranging from 8 to 10" early in the
    blast-wave problem.

# Tests

**Two interacting blast waves** (§IVa, §VIa; Figs. 1, 2, 6; Table I).
Set-up, attributed to Woodward (1982, *Parallel Computation*): gas at
rest between reflecting walls 1 apart, $\rho = 1$, $p = 1000$ in the
leftmost tenth, 100 in the rightmost tenth, 0.01 between; display time
$t = 0.038$. The reference is a special PPMLR run that tracks the two
contacts as three fluids and refines by 8 in space and time near each
discontinuity and the walls: 3096 zones, widths $1/2400$ to $1/9600$.
The blast waves collide at $t \approx 0.028$; the peak density does not
reach the limiting 36 and has fallen to about 24 by $t = 0.030$. The
left and middle contacts carry most of the error. Selected entries of
Table I (CRAY-1, 1D):

| Scheme | $\nu$ | error, 200 zones | error, 1200 zones | CPU s, 1200 | last rate |
|---|---|---|---|---|---|
| MacCormack | 0.8 | 0.261 | 0.0862 | 9.19 | 0.72 |
| BBC | 0.8 | 0.196 | 0.0717 | 14.5 | 0.64 |
| ETBFCT | 0.4 | 0.227 | 0.0606 | 44.0 | 0.76 |
| Godunov | 0.8 | 0.330 | 0.182 | 20.1 | 0.40 |
| MUSCL | 0.8 | 0.162 | 0.0401 | 44.9 | 0.85 |
| PPMDE | 0.8 | 0.0990 | 0.0144 | 53.7 | 1.07 |
| PPMLR | 0.8 | 0.0760 | 0.0133 | 50.8 | 0.98 |

At 200 and 1200 zones (Fig. 6): Godunov smears the three contacts
"unacceptably"; MacCormack and BBC give 3-zone shocks and soft contacts;
ETBFCT gives 1-zone shocks but a spurious contact at a density-slope
discontinuity; MUSCL resolves the contacts adequately at 1200; both PPM
forms keep the outer contacts 1 zone wide at 200 and are "essentially
converged" at 1200. MacCormack's Lapidus coefficient was augmented by a
sound-speed-difference term to damp oscillations at moving contacts.

**Mach 3 wind tunnel with a step** (§IVb, §VIb; Figs. 3, 7, 8). The
problem "was introduced more than a decade ago" by Emery (1968). Tunnel
1 wide and 3 long, step 0.2 high at 0.6 from the left end; initial and
inflow state $\rho = 1.4$, $p = 1$, velocity 3; zero gradients at the
supersonic exit; reflecting walls. **Corner fix** (pp. 131–132): in the
first four zones right of the corner in the first row above the step,
and the first two in the next row, the density is reset to match the
entropy, and the speed (not the direction) to match the total enthalpy,
of the zone just left of and below the corner; it assumes nearly steady
flow. Grids $h = 1/20$, $1/40$, $1/80$ to $t = 4$, mostly at $\nu = 0.8$.
The flow is still unsteady at $t = 4$ (steady by $t = 12$); the Mach stem
forms at about $t = 1.5$ and is the slowest feature to converge.
PPMDE is about 3.6 times more efficient than BBC and 4.4 times more than
MacCormack; PPMLR equals it at 18 % more CPU time.

**Double Mach reflection** (§IVc, §VIc; Figs. 4, 9, 10). A Mach 10 shock
in air "initially makes a 60° angle with a reflecting wall"; undisturbed
$\rho = 1.4$, $p = 1$; the wall runs along $y = 0$ from $x = 1/6$; exact
post-shock values on $[0, 1/6]$ at the bottom and on the left; zero
gradients at $x = 4$; the top follows the exact shock motion; $t = 0.2$,
only $0 \le x \le 3$ shown. Grids $h = 1/30$, $1/60$, $1/120$. The
one-zone initial jump creates an overheated strip about 2 zones wide,
visible in the vertical velocity, which "mars all the computed results".
A dense jet shoots along the wall. PPMDE (with Lapidus 0.1) matches BBC
and MacCormack with less than half the zones per direction, "more
efficient by factors of more than 4.9 and 1.3"; PPMLR by more than 4.4
and 1.2.

# Notation map

| Woodward & Colella (1984) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$, $v$ (Appendix); $v_x$, $v_y$ (figures) | $\mathbf v = (v_x, v_y)$ | the registry $u$ is the conserved state |
| $E$ (specific total energy) | $E/\rho$ | the registry $E$ is an energy density |
| $\varepsilon$ (Appendix: specific internal energy) | words | $\varepsilon$ is the weight regularization |
| $\varepsilon$ (§VIa: fractional L1 density error) | words | same clash |
| $V = 1/\rho$ | words | $\tau$ is the WENO-Z indicator |
| $q$ (artificial viscous pressure) | words | $q$ is the weight power |
| $A = p/\rho^\gamma$ | words ("entropy function") | $A(u)$ is the flux Jacobian |
| $c$ | $c$ | |
| $\Delta x$, $\Delta y$ | $h_x$, $h_y$ ($h$ for square zones) | |
| Courant number | $\nu$ | |
| $\langle\rho\rangle_i$ | $\bar\rho_i$ | cell average |
| incident shock Mach number | $M_s$ | |

# Pages created or updated

* Updated [Woodward–Colella interacting blast waves](/benchmarks/interacting-blast-waves.md) (original set-up, reference solution, error table, attribution to Woodward 1982).
* Updated [Double Mach reflection](/benchmarks/double-mach-reflection.md) (what the original prints; the seven-scheme comparison).
* Updated [Mach 3 wind tunnel with a forward-facing step](/benchmarks/forward-facing-step.md) (origin with Emery 1968; corner fix; the comparison).
* Updated [PPM](/methods/ppm.md) (the comparison; the two dissipation options and their error orders).
* Updated [Slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md) (§Vc and §VIb).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/1984-JCP-Woodward-1010160021-99918490142-6.pdf`.
   * **Version.** The published journal article, a scanned Academic Press
     print of 59 pages with an OCR text layer.
   * **Identity.** doi:10.1016/0021-9991(84)90142-6, checked on Crossref:
     J. Comput. Phys. 54(1):115–173, April 1984, authors P. Woodward and
     P. Colella. Received 15 July 1982, revised 25 August 1983.
   * **How it was read.** The text layer for prose. Its digits are
     unreliable: Table I, the error formula, the Godunov convergence
     exponents, the captions of Figs. 7c, 7f, 9f, 9g and the reference
     list were checked on page images, which corrected three OCR digits
     in Table I (BBC 600 zones: 970 steps; Godunov 400: error 0.274;
     MUSCL 600: rate 0.77) and one CPU time (PPMDE 1200: 53.7). The BBC
     equations A2–A33 are garbled in the text layer and are not
     reproduced; contour figures were not read quantitatively.
   * **Recorded as printed.**
     - §VIa prints "Each result at time 0.38", a typo for the 0.038 of
       §IVa.
     - The text announces nine grids (100 to 2400 zones); Table I lists
       only 200 to 1200.
     - §Vc says Fig. 4 used the jiggled grid and Fig. 9f the Lapidus 0.1
       run, both PPMDE; §VIb (p. 156) instead assigns grid jiggling to
       PPMLR and Lapidus 0.1 to PPMDE.
     - The double Mach reflection prints neither the post-shock state nor
       a wedge angle; the shock foot at $x = 1/6$ follows from the
       attachment condition.
   * **Reference list:** 56 entries, 56 keys. The two Colella
     1984 papers printed in this list were resolved by identity, not by
     printed-order suffix: PPM is `colella-1984`, direct Eulerian MUSCL
     `colella-1984-b` (folded into its published form `colella-1985`,
     SIAM J. Sci. Stat. Comput. 6:104, at batch 12). "Colella, Woodward & Zalesak, in preparation" is
     `colella-1984-d`; Colella's LBL-14442 report is `colella-1984-e`; the
     LBL-15776 report is `colella-1983`, kept distinct from
     `colella-1984-c` (rekeyed `colella-1985-b` at batch 12, when its
     published form, J. Comput. Phys. 59:264, was cited) (a first merge had collapsed `-d` and the LBL-14442
     report into one key; separated at the deep lint). The Russian original of Godunov, Zabrodin &
     Prokopov is merged into `godunov-1961`. Boris's NRL memorandum is
     `boris-1976-b` (also cited by Brio & Wu). Berger & Oliger,
     "submitted", is `berger-1984`. Ref. 7 prints the co-author as
     "Collela" (`woodward-1981`). Undated entries take the citing year,
     1984, with a note.
