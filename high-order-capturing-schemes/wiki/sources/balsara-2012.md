---
type: Source
title: "Balsara (2012) — Self-adjusting, positivity preserving high order schemes for hydrodynamics and magnetohydrodynamics"
description: "A reconstruction-level positivity fix for Euler and MHD: a flattener built from the velocity divergence and the neighbourhood's smallest sound speed widens or narrows neighbour-based density and pressure bounds, density is rescaled two-sidedly by Barth's ratio, and pressure one-sidedly by a per-node quadratic (Euler) or cubic (MHD, scaling only the free modes of the divergence-free field); no theorem, three stringent ADER-WENO tests that fail with floors alone."
resource: "doi:10.1016/j.jcp.2012.01.032"
source_kind: paper
authors: [Balsara D.S.]
year: 2012
venue: "J. Comput. Phys. 231:7504–7517"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2012-JCP-Balsara-101016jjcp201201032.pdf"
tags: [positivity, limiter, flattening, mhd, ader, weno]
timestamp: 2026-10-13T00:00:00Z
---

# Summary

The paper turns positivity of density and pressure into a correction of
the reconstructed profile, applied in every zone before the Riemann
solver (and, with ADER, before the predictor). It merges three earlier
ideas: the Colella–Woodward flattener, which detects strong shocks;
Barth's neighbour-bounded limiter, with bounds from the minimum and
maximum of the $3\times3$ neighbour averages; and Zhang and Shu's linear
scaling of the reconstructed polynomial about its mean at a set of nodes.
The neighbour range is widened by a factor 0.4 in smooth flow, so that
non-oscillatory extrema survive, and the flattener shrinks it smoothly
back to the plain neighbour range at strong shocks ("self-adjusting").
Density is limited from both sides by Barth's ratio; pressure only from
below, by a per-node root of a quadratic (Euler) or a cubic (MHD). In MHD
only the "free" modes of the divergence-free magnetic reconstruction are
scaled. The paper claims this is the first positivity treatment for MHD.
Three tests (a Mach 800 dense jet, a Mach 100 light jet, a 3D MHD blast at
plasma beta $1.005\times10^{-3}$) run with third- or fourth-order
ADER-WENO; with floors only, the runs fail or are corrupted. There is no
theorem: no proof that updated cell averages stay positive and no CFL
bound ([self-adjusting positivity limiter](/methods/self-adjusting-positivity-limiter.md)).

# Key claims

1. **Diagnosis** (§1). Spurious solutions in multi-shock flows come from
   loss of positivity of the *reconstructed profile* inside a zone, while
   the zone average stays positive. Characteristic reconstruction "might
   slightly ameliorate the problem, yet it usually does not solve" it; TVD
   limiting "only ensures that the density does not become negative at
   the centers of zone faces", so multidimensional Riemann solvers
   evaluated at edges and vertices need more.
2. **Prior art as the paper states it** (§1). Titarev & Toro restricted
   the density and pressure variation to a *fixed* fraction of the zone
   mean (not adaptive; the paper's attribution, not checked against the
   bundle's Titarev–Toro page, which records no positivity statement).
   Barth and Barth & Frederickson used neighbour min/max bounds; Balsara
   extended them to second-order MHD. Zhang & Shu (building on Perthame &
   Shu; see also Waagan) limit at favourable nodes, but their method "(a)
   is not self-adjusting and (b) does not extend to other useful systems
   like MHD".
3. **Flattener** (§2.1, eqs. 1–3). The smallest sound speed
   $\sqrt{\gamma p/\rho}$ over the $3\times3$ block (eq. 1) is compared with
   the undivided velocity divergence: the flattener is
   $\min[1, \max[0, -(h_x\nabla\cdot\mathbf v + 0.4\,c_{\min})/(0.4\,c_{\min})]]$
   ($c_{\min}$ that smallest sound speed; eq. 2, constant 0.4). It is 0 in
   rarefactions and weak compressions, rises continuously, and reaches 1
   where $h_x\nabla\cdot\mathbf v \le -0.8\,c_{\min}$ (reader's arithmetic).
   A pre-shock spreading rule (eq. 3, printed for $x$): if a zone's
   flattener is positive, its neighbour's is zero and the zone's pressure
   is higher, the neighbour takes the zone's value; applied per direction
   after eq. 2. In MHD the sound speed is replaced by
   $\sqrt{(\gamma p + \vert\mathbf B\vert^2/4\pi)/\rho}$ in Gaussian units,
   "a maximal magnetosonic speed" (§2.2).
4. **Self-adjusting bounds** (eqs. 4–5). The minimum and maximum of the
   $3\times3$ zone averages are extended to minimum times
   $(1 - 0.4 + 0.4\times\text{flattener})$ and maximum times
   $(1 + 0.4 - 0.4\times\text{flattener})$; the range is 40% wider in
   smooth flow and shrinks to Barth's range at strong shocks. The same is
   done for pressure. Both constants (0.4) come from "numerical
   experimentation"; absolute floors on the lower bounds "might be
   valuable" in practice.
5. **Density** (eqs. 6–8). The profile is scaled about the mean by a
   factor in $[0,1]$ (the paper warns that its symbol, $\tau$, is not time).
   With the nodal maximum and minimum of the reconstructed density, the
   factor is the smallest of 1, (upper bound − mean)/(nodal max − mean) and
   (mean − lower bound)/(mean − nodal min) (eq. 7, "as shown by Barth"; no
   case logic for a nodal extremum equal to the mean). The same factor
   should scale the momentum and energy variation, so that "the physical
   velocity should not change".
6. **Pressure, Euler** (eqs. 9–12). After the density fix, one factor
   scales all conserved variables (eq. 9). At a node with pressure below
   the lower bound, the factor solves $p = $ lower bound, which after
   multiplying by twice the scaled density is a quadratic (eq. 12; reader
   re-derived it and agrees). The zone factor is the minimum over nodes.
   Only the lower pressure bound is enforced (§2.3).
7. **Pressure, MHD** (eqs. 13–15). The divergence-free reconstruction
   splits the nodal field into the part fixed by face consistency (itself
   spatially varying) and a free part; only the free part is scaled
   (eq. 13). The magnetic energy then makes the pressure condition a
   **cubic** in the factor (eq. 15, after $\mathbf B \to \mathbf B/\sqrt{4\pi}$;
   reader re-derived it and agrees). The root is bracketed in $[0,1]$ and
   found by Newton's method safeguarded by bisection; three to four
   significant digits suffice, and "a maximum of four iterations" sufficed
   in every run (§2.2).
8. **Where and on which nodes** (§2.3). At every Runge–Kutta stage after
   reconstruction and before the Riemann solver; with ADER, before the
   predictor. Zhang–Shu tensor-product Gauss–Lobatto points are
   **rejected** as "an excessive number of nodes in multiple dimensions";
   the nodes are the minimal symmetric set of the nodal-to-modal
   transcription of Balsara et al. (2013) plus the zone vertices. In 3D:
   8 vertices at second order; 13 nodes + 8 vertices = 21 at third order;
   21 nodes, vertices included, at fourth order; higher orders not
   documented. The vertices are always included, because "piecewise linear
   variation is always present". The nodes are spatial only.
9. **Riemann solver caveat** (§2.3). Linearized solvers lose pressure
   positivity in strong rarefactions (Einfeldt et al.), so the code
   "retain[s] an entropy formulation" there (Balsara & Spicer), never at
   shocks. Positivity-preserving Riemann solvers are recommended "when
   they are available". Velocity and field are limited only "tacitly",
   through pressure positivity.
10. **Optional velocity and field limiting** (App. A). Velocity bounds are
    the neighbour range widened by 0.4 of its width, *not* modulated by the
    flattener; the field factor is valid while the consistency part lies
    within the bounds, which "can always be ensured at second order", so in
    the worst case the order drops locally. Intended for DG, where the
    flattener identifies troubled zones.
11. **Accuracy** (§3). The smooth suite of Balsara et al. was rerun with
    the method and the accuracy "stays unchanged"; no table or figure is
    shown. Conclusions: "The order of accuracy of the base level scheme is
    never degraded for smooth flow".
12. **CFL** (§3.1). "Zhang and Shu [40] claim that their method restricts
    the CFL number. However, the ADER method couples space and time more
    effectively", so the method "works with sufficiently large CFL numbers":
    0.45 in the jets, 0.3 in the blast. Empirical; no bound is proved.
13. **Characteristic limiting unnecessary** (Abstract, Conclusions). All
    runs reconstruct conserved variables; with the positivity step "we have
    seen no need to resort to characteristic limiting". Positivity should
    rank "alongside with non-linear hybridization" as a design principle.
14. **Floors are not a substitute** (§3). The runs were repeated without
    the method, with $\rho \ge 10^{-12}$ and $p \ge 10^{-8}$ in the Riemann
    solver (the only places, with the time step, where positive inputs are
    needed). One jet "simply cannot be run": the floors are hit and the time
    step "bottoms out". Second-order TVD schemes show the same pathologies.

# Tests

All results are colour plots (Figs. 2–6); no error or convergence tables.

* **Smooth suite** (§3): rerun, "unchanged", no data shown.
* **2D Mach 800 dense jet** (§3.1, Figs. 2–3). $\gamma = 1.4$; jet
  $\rho = \gamma$, $p = 1$ (sound speed 1); ambient $\rho = 0.1\gamma$, equal
  pressure; inlet speed 800 at the centre of the short side, width 0.1;
  $[-0.5, 0.5]\times[0, 1.5]$, $400\times600$, outflow elsewhere;
  $t = 0.002$, CFL 0.45. Fourth-order ADER-WENO with a linearized Riemann
  solver. With the method: $\rho \in [0.0159, 10.8]$,
  $p \in [0.981, 52583.4]$, $\vert\mathbf v\vert \in [0, 800]$, symmetric.
  Unmodified second-order TVD with a linearized solver, and higher order
  with floors and a linearized solver, cannot run it. HLL with floors and
  unmodified fourth-order ADER-WENO runs, with intermediate steps at the
  pressure floor ($\rho \in [0.0089, 16.37]$, $p \in [0.808, 73651.7]$), and a
  "dramatic and unphysical loss of symmetry" near the working surface. Set-up
  "very much like" Ha et al.
* **2D Mach 100 light jet** (§3.2, Fig. 4). As above with ambient
  $\rho = 10\gamma$, inlet speed 100, $t = 0.03$, CFL 0.45; fourth-order
  ADER-WENO with HLL (the linearized solver's carbuncle suppression was not
  good enough). $\rho \in [0.0809, 110.3]$, $p \in [0.998, 14960.0]$,
  symmetric. Not runnable with unmodified second-order TVD or with
  higher order plus floors. Offered "as a more stringent variant of the
  problem discussed in Zhang and Shu"
  ([high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md)).
* **3D MHD blast** (§3.3, Figs. 5–6). $\gamma = 1.4$, $\rho = 1$,
  $p = 0.1$, $p = 1000$ inside radius 0.1 (centre not stated);
  $B_x = B_y = B_z = 50/\sqrt3$ (Gaussian, $\vert\mathbf B\vert = 50$), plasma
  beta $1.005\times10^{-3}$; unit cube, $129^3$, CFL 0.3, $t = 0.012$;
  third-order ADER-WENO with a linearized solver (also run at second and
  fourth order). With the method (mid-plane): $\rho \in [0.115, 2.53]$,
  $p \in [0.0135, 88.3]$, $\vert\mathbf v\vert \le 8.94$,
  $\vert\mathbf B\vert \in [13.7, 64.1]$. With floors only: $p$ reaches
  $10^{-8}$, peak $\vert\mathbf v\vert$ 9.6 and $\vert\mathbf B\vert$ 67.2;
  the pressure is "totally corrupted… scientifically unusable". Described
  as the 3D variant of Balsara & Spicer's 2D blast
  ([MHD blast wave](/benchmarks/mhd-blast-wave.md)).

# Notation map

| Balsara (2012) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $P$, $\mathbf v$, $\mathbf B$, $\gamma$ | $\rho$, $p$, $\mathbf v$, $\mathbf B$, $\gamma$ | Gaussian units ($B^2/8\pi$) |
| $\mathbf m \equiv \rho\mathbf v$ | $\rho\mathbf v$ | |
| $\varepsilon$ (total energy density) | $E$ | **collision**: weight regularization $\varepsilon$ |
| $\bar\rho_{i,j}$ | $\bar u_i$ convention, 2D index | |
| $\rho_{i,j}(x, y)$ | $\mathcal P_i$ | |
| $\tau$, $\tau_{i,j}$, $\tau^q_{i,j}$ | $\theta$; $\theta_\rho$, $\theta_p$; per node in words | **collision**: WENO-Z $\tau$ |
| $q = 1..Q$, $(x^q, y^q)$ | words (positivity nodes) | not Gauss–Lobatto, so not $\hat x^{(a)}_i$ |
| $\eta_{i,j}$ | words (flattener) | **collision**: coercivity $\eta$; do not reuse PPM $\phi_i$ |
| $\kappa_1$, $\kappa_2$ | words (both 0.4) | **collision**: $\kappa$, $\kappa_i$ |
| $c_{s;i,j}$ | $c$ (Euler); words in MHD | **collision**: registry $c_s$ is the slow speed |
| $c^{\min-nbr}_{s;i,j}$ | words (smallest sound speed over the block) | |
| $\rho^{\min-nbr}$, $\rho^{\max-nbr}$; $\rho^{\min-ext}$, $\rho^{\max-ext}$ | words (neighbour and extended bounds) | |
| $\bar{\mathbf B}^q$ (consistency part), $\mathbf B^q$ (free part) | words | the paper's overbar is not a zone average here |
| $\Delta x$, $\Delta y$ | $h_x$, $h_y$ | |
| $(\nabla\cdot\mathbf v)_{i,j}$ | $\nabla\cdot\mathbf v$ | printed without the 1/2 (see Citations) |

# Pages created or updated

* Created [Self-adjusting positivity limiter](/methods/self-adjusting-positivity-limiter.md).
* Updated [Positivity preservation](/properties/positivity-preserving.md) (batch-18 block: quadratic only for Euler, cubic for MHD; no theorem; CFL tension with Zhang–Shu; floors).
* Updated [Zhang–Shu positivity-preserving scaling limiter](/methods/positivity-preserving-scaling-limiter.md) (batch-18 block: the original node set rejects tensor Gauss–Lobatto points).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md) (batch-18 block: no characteristic limiting needed with the positivity step).
* Updated [MHD blast wave](/benchmarks/mhd-blast-wave.md) (batch-18 block: the 2012 3D blast and its floors-only run).
* Updated [High-Mach astrophysical jet](/benchmarks/high-mach-astrophysical-jet.md) (batch-18 block: the two hydrodynamic jets) and [PPM](/methods/ppm.md) (batch-18 block: a flattener on bounds, not on the parabola).
* Cited on [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md) (a not-decisive bullet on the Open CT-or-cleaning entry, 2026-10-13 deep lint).

# Citations

1. `/home/stefano/papers/mosaic/high-order-capturing-schemes/2012-JCP-Balsara-101016jjcp201201032.pdf`.
   * **Version read.** The publisher's version of record (Elsevier, 14
     pages), not a preprint. Received 24 October 2010, revised 18 January
     2012, accepted 20 January 2012, online 1 February 2012. Three "Video"
     stills (lecture photographs) carry no technical content.
   * **Identity.** doi:10.1016/j.jcp.2012.01.032 (printed on page 1),
     checked on Crossref: title and author match, J. Comput. Phys.
     231(22):7504–7517, September 2012, reference count 40.
   * **How it was read.** Every equation from rendered page images (pp.
     3–6, 12–13), not the text layer, which garbles the displays. Eqs. 12
     and 15 and the Appendix A velocity factor were re-derived and agree
     with the printed forms.
   * **Recorded as printed** (reader's reading).
     - The velocity divergence (eq. 2 context) is printed as
       $(v_{x;i+1,j} - v_{x;i-1,j})/\Delta x + \dots$, without the factor
       1/2 of a central difference. The text defines the undivided
       divergence with $\min(h_x, h_y)$, but eq. 2 uses $h_x$.
     - Eq. 3 is printed for $x$ only; the order of the directional
       spreadings is not specified. The 3D neighbour block, the nodal
       coordinates of the cited sets and the blast centre are not printed.
     - That the pressure factor multiplies the density factor is implicit.
     - "Linearized Riemann solver" is not specified; the entropy-formulation
       fallback is non-conservative and not detailed.
     - No accuracy data, no positivity theorem, no CFL bound.
   * **Reference list:** 40 entries ([1]–[40]; Crossref also 40), all
     merged. Refs. [9] and [10], printed "submitted for publication" with no
     year, are identified on Crossref: [9] is J. Comput. Phys. 235:934 (2013;
     published author order Balsara, Meyer, Dumbser, Du, Xu, title slightly
     different), keyed `balsara-2013`, and [10] is J. Comput. Phys. 231:7476
     (2012), keyed `balsara-2012-b`. "Von Karmen" ([12]) and "Arbitary"
     ([17]) are kept as printed. Ha et al. is printed J. Sci. Comput. 24:29
     (Crossref 24:29–44, `ha-2005`); Waagan is printed J. Comput. Phys.
     228:6809. Bibliography: 3380 entries.
