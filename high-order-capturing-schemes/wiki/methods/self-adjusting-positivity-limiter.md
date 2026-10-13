---
type: Method
title: "Self-adjusting positivity limiter (Balsara)"
description: "A reconstruction-level positivity fix for Euler and MHD: a flattener built from the velocity divergence and the smallest neighbouring sound speed widens neighbour-based density and pressure bounds in smooth flow and narrows them at strong shocks; density is scaled about the mean by Barth's two-sided ratio, pressure from below by a per-node root of a quadratic (Euler) or a cubic (MHD, free field modes only); robust in stringent tests but with no positivity theorem or CFL bound."
status: established
aliases: [Balsara's self-adjusting method, self-adjusting positivity preserving scheme, self-adjusting positivity method]
tags: [positivity, limiter, flattening, mhd, ader, weno]
timestamp: 2026-10-13T00:00:00Z
---

# Self-adjusting positivity limiter (Balsara)

**What it is** ([Balsara (2012)](/sources/balsara-2012.md), §§1–2). A
correction of the reconstructed polynomial $\mathcal P_i$ of every zone,
applied after reconstruction and before the Riemann solver (with ADER,
before the predictor; with Runge–Kutta, at every stage). It targets the
failure the paper diagnoses: the zone average stays in $\mathcal G$ while
the reconstructed profile leaves it inside the zone, which TVD limiting,
controlling only face-centre values, does not prevent at the edges and
vertices where multidimensional Riemann solvers evaluate it. It combines
three ingredients: the Colella–Woodward flattener (shock detection),
Barth's neighbour-bounded limiter (bounds from the neighbour averages), and
Zhang and Shu's scaling of $\mathcal P_i$ about $\bar u_i$ at a set of
nodes ([scaling limiter](/methods/positivity-preserving-scaling-limiter.md)).
"Self-adjusting" refers to the bounds: wide in smooth flow, so that smooth
extrema survive, and narrow at strong shocks.

## Algorithm

All numbers are those of the paper; the 2D formulas use a $3\times3$
neighbour block.

1. **Flattener** (eqs. 1–3). Take the smallest sound speed $c$ over the
   block (in MHD, the "maximal magnetosonic speed"
   $\sqrt{(\gamma p + \vert\mathbf B\vert^2)/\rho}$ in Heaviside–Lorentz
   units). Compare it with the undivided velocity divergence
   $h_x\nabla\cdot\mathbf v$: the flattener is 0 in rarefactions and in
   compressions weaker than 0.4 times that sound speed, rises linearly, and
   is 1 for $h_x\nabla\cdot\mathbf v$ below $-0.8$ times it (eq. 2, constant
   0.4; the threshold is a reader's arithmetic). A pre-shock rule spreads a
   nonzero value to a neighbour with zero flattener and lower pressure, per
   direction (eq. 3). The flattener acts on bounds, not on the profile,
   unlike the [PPM](/methods/ppm.md) flattening $\phi_i$.
2. **Bounds** (eqs. 4–5). The minimum and maximum of $\bar\rho$ over the
   block are scaled by $1 - 0.4(1 - \text{flattener})$ and
   $1 + 0.4(1 - \text{flattener})$: the admissible range is up to 40%
   wider than the neighbour range in smooth flow and equals it (Barth's
   range) at strong shocks. The same is done for $p$. Both 0.4 constants
   come from "numerical experimentation".
3. **Density, two-sided** (eqs. 6–8). With the largest and smallest values
   of the reconstructed density at the nodes,
   $$\theta_\rho = \min\left(1,\ \frac{\text{upper bound} - \bar\rho_i}{\text{nodal maximum} - \bar\rho_i},\ \frac{\bar\rho_i - \text{lower bound}}{\bar\rho_i - \text{nodal minimum}}\right)$$
   (eq. 7, "as shown by Barth"); the density variation is scaled by
   $\theta_\rho$, and the momentum and energy variations should be scaled
   alike, so that the velocity does not change.
4. **Pressure, one-sided** (eqs. 9–15). After the density step, one factor
   $\theta_p$ scales the variation of every conserved variable (eq. 9). At
   each node where the pressure is below the lower bound, the factor
   solves $p\left((1-\theta)\bar u_i + \theta\,\mathcal P_i(\text{node})\right) = \text{lower bound}$,
   and $\theta_p$ is the minimum over the nodes. Multiplying by twice the
   scaled density turns this into
   * a **quadratic** for Euler (eq. 12), since $\rho$ is linear and
     $\vert\rho\mathbf v\vert^2$ quadratic in $\theta$;
   * a **cubic** for MHD (eq. 15). The divergence-free reconstruction splits
     the nodal field into a part fixed by face consistency, itself spatially
     varying, and a free part; only the free part is scaled (eq. 13), so the
     magnetic energy is quadratic in $\theta$ and, times the linear density,
     cubic. The root is bracketed in $[0, 1]$ and found by Newton's method
     safeguarded by bisection, three to four digits, at most four
     iterations in the paper's runs.

   Only the lower pressure bound is enforced; density is bounded on both
   sides (§2.3).
5. **Nodes** (§2.3). Not Gauss–Lobatto: tensor-product Gauss–Lobatto points
   are rejected as "an excessive number of nodes in multiple dimensions".
   The nodes are the minimal symmetric set of a nodal-to-modal
   transcription (Balsara et al. 2013) plus the zone vertices, always
   included because "piecewise linear variation is always present". In 3D:
   8 at second order, $13 + 8 = 21$ at third, 21 (vertices included) at
   fourth; higher orders are not documented.
6. **Optional** (App. A). Velocity bounds are the neighbour range widened by
   0.4 of its width, without the flattener; a field bound is possible while
   the consistency part stays within it, otherwise the order drops locally.
   Meant for DG, where the flattener flags troubled zones.

## What is and is not claimed

* **No theorem.** Nothing proves that the updated cell averages stay in
  $\mathcal G$, and no CFL bound is given. The nodes are not the
  Gauss–Lobatto points of the Zhang–Shu decomposition, so its sufficient
  condition does not transfer ([positivity preservation](/properties/positivity-preserving.md)).
  The method is robust in practice, not provably positive.
* **CFL.** The paper answers Zhang and Shu's CFL restriction empirically:
  with ADER, which "couples space and time more effectively", the method
  "works with sufficiently large CFL numbers", 0.45 and 0.3 in its tests
  (§3.1).
* **Accuracy.** The order is "never degraded for smooth flow"; the smooth
  test suite was rerun, but no table or figure is shown (§3).
* **Riemann solver.** Linearized solvers can still lose positivity in strong
  rarefactions (Einfeldt et al.); the code falls back to an entropy
  formulation there, and positivity-preserving solvers are recommended
  where available (§2.3; [approximate Riemann solvers](/methods/approximate-riemann-solvers.md)).
* **Characteristic limiting.** With the positivity step, the runs
  reconstruct conserved variables and "we have seen no need to resort to
  characteristic limiting" ([characteristic decomposition](/methods/characteristic-decomposition.md)).

## Evidence

Three tests with third- or fourth-order ADER-WENO
([Balsara (2012)](/sources/balsara-2012.md), §3), each repeated with floors
$\rho \ge 10^{-12}$, $p \ge 10^{-8}$ in the Riemann solver instead of the
method:
* a Mach 800 jet 10 times denser than its surroundings, $400\times600$,
  linearized solver: runs symmetric with the method; with floors it cannot
  run with the linearized solver, and with HLL it runs at the pressure floor
  with a "dramatic and unphysical loss of symmetry";
* a Mach 100 jet 10 times lighter, HLL: runs with the method, not with
  higher order plus floors
  ([high-Mach jet](/benchmarks/high-mach-astrophysical-jet.md));
* a 3D MHD blast at plasma beta $1.005\times10^{-3}$, $129^3$: with floors
  the pressure hits $10^{-8}$ and is "totally corrupted"
  ([MHD blast wave](/benchmarks/mhd-blast-wave.md)).

Second-order TVD schemes show the same pathologies without the method.

## Later descriptions

* *The review form* ([Balsara (2017)](/sources/balsara-2017-d.md), §VII,
  eqs. 115–126) gives the 2D third-order version at the $3\times3$
  Gauss–Lobatto tensor nodes with the vertices, and describes the pressure
  factor as a per-node quadratic. Both differ from the 2012 original, which
  rejects Gauss–Lobatto tensor nodes and has a cubic for MHD; the review's
  scope is a pedagogical 2D third-order presentation, and a $3\times3$
  Gauss–Lobatto grid contains the vertices, so this is a variant, not a
  contradiction. The review calls it "designed to save a code from a rare
  code crash"; the original says the correction is "invoked in an extremely
  small fraction of zones" (§2.1). It is used there on a 3D MHD blast at
  plasma beta $1.117\times10^{-4}$ (§IX.4).
* *A proposed remedy* for positivity failures of subcell WENO in a
  posteriori limited DG ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §6;
  [a posteriori subcell limiting](/methods/a-posteriori-subcell-limiting.md)),
  in line with the original's suggestion of DG use (§2.3, App. A).

# Citations

1. [Balsara (2012)](/sources/balsara-2012.md), §§1–3, App. A (eqs. 1–15 read from the page images; eqs. 12 and 15 re-derived by the reader).
2. [Balsara (2017)](/sources/balsara-2017-d.md), §§VII, IX.4.
3. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §6.
