---
type: Method
title: "A posteriori subcell finite-volume limiting (MOOD paradigm)"
description: "Run the unlimited high-order scheme, test the candidate solution for positivity and a relaxed discrete maximum principle, and recompute only the failed cells from the previous time level with a robust finite-volume scheme — for DG, a third-order ADER-WENO scheme on 2K+1 subcells per direction, gathered back into the DG polynomial."
status: established
aliases: [MOOD, multi-dimensional optimal order detection, a posteriori limiter, subcell limiter, SCL, DG-PN + WENO3 SCL]
tags: [limiter, a-posteriori, dg, finite-volume, ader, positivity, amr]
timestamp: 2026-10-13T00:00:00Z
---

# A posteriori subcell finite-volume limiting (MOOD paradigm)

**MOOD** (Clain, Diot and Loubère, finite volume; as described by
[Dumbser et al. (2014)](/sources/dumbser-2014.md), §§1, 4.1). Compute a
*candidate* solution with the unlimited high-order scheme, then test it
against admissibility criteria. Failed cells and their neighbours are
recomputed with a lower polynomial degree, and the candidate is
retested. The loop ends because at degree zero the cell is updated by
a first-order Godunov scheme, "supposed" monotone and
positivity-preserving under its CFL condition. Two features set this
apart from a priori limiters. The test uses two time levels, $t^n$ and
$t^{n+1}$, and the solution is *recomputed* with a different scheme
rather than post-processed. Classical DG limiters, by contrast, look
only at the current solution ([WENO limiters for DG](/methods/weno-limited-dg.md)).

## Extension to DG

([Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.) Lowering the DG
degree would destroy DG's subcell resolution. Troubled cells are
therefore recomputed on a subgrid with a robust but still high-order
finite-volume scheme. One step has five acts.

1. **Candidate.** One unlimited [ADER-DG](/methods/ader.md) step gives
   $\mathcal{P}^*_i(x, t^{n+1})$.
2. **Scatter.** Project onto $N_{\mathrm s}^d$ equal subcells,
   $\bar v^*_{i,m} = \Pi\,\mathcal{P}^*_i$.
3. **Detect.** Mark $\mathcal{B}_i = 1$ if either test fails.
   * *Physical* (PAD): the positivity of the quantities that must stay
     positive, such as $\rho$ and $p$ for Euler.
   * *Numerical* (NAD): a relaxed discrete maximum principle "in the
     sense of polynomials", evaluated on subcell averages, with
     $$\min_{V_i}\bar v^n - \delta_{\mathrm{DMP}} \le \bar v^*_{i,m} \le \max_{V_i}\bar v^n + \delta_{\mathrm{DMP}}$$
     componentwise over the cell and its node neighbours $V_i$.
4. **Recompute.** For flagged cells only, return to $t^n$, project
   $\mathcal{P}^n_i$ (and the neighbours, as boundary data) onto the
   subgrid, and advance with a third-order ADER-WENO finite-volume
   scheme. The subgrid data carry over if the cell was already troubled.
5. **Gather.** $\mathcal{P}^{n+1}_i = \mathcal{R}\,\bar v^{n+1}_{i,\cdot}$ by
   constrained least squares, conservative in the cell. For
   $N_{\mathrm s} \ge K + 1$, $\mathcal{R}\circ\Pi = I$, so projecting
   loses no information.

Neighbouring unlimited cells re-flux their shared sub-faces, so the
scheme stays conservative. Only subgrid data of troubled cells and
neighbourhood extrema are stored. The initial $L^2$ projection is
tested in the same way. Only two levels are used, unlimited DG and
subcell WENO, not the full MOOD cascade.

**Relaxation.** The 2014 arXiv version read here sets
$\delta_{\mathrm{DMP}} = \epsilon_{\mathrm{DMP}}\left(\max_{V_i} - \min_{V_i}\right)$
with $\epsilon_{\mathrm{DMP}} = 10^{-3}$ (eq. 24, checked on the page
image). [Zanotti et al. (2015)](/sources/zanotti-2015.md) (eq. 17,
checked on the page image) use
$\delta_{\mathrm{DMP}} = \max\left(\delta_0,\ \epsilon_{\mathrm{DMP}}(\max - \min)\right)$
with $\delta_0 = 10^{-4}$, "as recommended" in the 2014 paper. The
floor $\delta_0$ does not appear in the version of the 2014 paper read
here. Positivity is checked separately, so the relaxation cannot
admit negative states.

**Why $N_{\mathrm s} = 2K + 1$** ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.5;
[Zanotti et al. (2015)](/sources/zanotti-2015.md), §4). The DG step obeys
$\Delta t \le \frac{1}{d(2K+1)}\frac{h}{\max_p\vert\lambda^{(p)}\vert}$, and
finite volume on subcells of size $h/N_{\mathrm s}$ obeys
$\Delta t \le \frac{1}{d}\frac{h/N_{\mathrm s}}{\max_p\vert\lambda^{(p)}\vert}$.
With $N_{\mathrm s} = 2K + 1$ the two limits coincide. The subgrid scheme
then runs at its largest Courant number, where ADER-FV truncation errors,
which carry a factor $(1 - \mathrm{CFL})$, are smallest. With
$N_{\mathrm s} = K + 1$ (Sonntag–Munz) it runs at half that.
A larger $N_{\mathrm s}$ would cut the DG time step.

**Why WENO on the subgrid.** A second-order TVD scheme would clip
physical local extrema, such as sound waves. ADER-WENO keeps them, and
both main and subgrid schemes are one-step, so the limiter acts once per
step, not per Runge–Kutta stage
([Dumbser et al. (2014)](/sources/dumbser-2014.md), §4.3).

## Evidence

* **Shocks in one cell.** DG of degree $K = 9$ on $20 \times 5$
  cells captures the Sod and Lax shocks within one main cell. The
  subcell jump sits at the exact location, and the Sod contact is an
  S-shaped profile inside one unlimited cell
  ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §5.1;
  [Sod](/benchmarks/sod-shock-tube.md), [Lax](/benchmarks/lax-shock-tube.md)).
* **Order kept.** The limiter never fires on the
  [isentropic vortex](/benchmarks/isentropic-vortex.md), and design
  order holds for $K = 2$–$9$. Round-off blurs the rates beyond
  $K = 7$, and $K = 9$ on $8\times8$ cells matches $K = 2$ on
  $100\times100$ (Table 2).
* **Fewer flags at higher order.** In the
  [double Mach reflection](/benchmarks/double-mach-reflection.md) the
  vortex region is almost free of limiting for $K = 5, 9$, while
  $K = 2$ flags more cells, including false positives. Higher-degree DG
  resolves these structures as smooth subscale features (§5.4).
* **Scale.** 3D explosion with $K = 9$ on $100^3$ cells, $10^{10}$
  space–time degrees of freedom per step, on 8000 cores (§5.8).
* **With AMR** ([Zanotti et al. (2015)](/sources/zanotti-2015.md), §5.2).
  Virtual children inherit the mother's limiter status. A mother is
  troubled if any active child is, and troubled cells cannot be
  recoarsened. Subcell data pass to a finer level by a WENO
  reconstruction, because the cells involved contain discontinuities,
  and to a coarser one by averaging. With $K = 2$ and about 15% of
  cells limited, the limiter costs a factor of about 1.5 in CPU time (§6.1.2)
  ([high-order AMR](/methods/high-order-amr.md)).

**Open issues** ([Dumbser et al. (2014)](/sources/dumbser-2014.md), §6).
WENO3 on the subgrid may itself fail positivity for very complex
systems. The suggested remedies are a further MOOD layer, a second-order
TVD or first-order Godunov subgrid scheme, or Balsara's self-adjusting
positivity method ([positivity preservation](/properties/positivity-preserving.md)).

**Later uses (batch 7).**
* A review attributes the floor $\delta_{\mathrm{DMP}} = \max(\delta_0, \epsilon_{\mathrm{DMP}}(\max - \min))$
  with $\delta_0 = 10^{-4}$ and $\epsilon_{\mathrm{DMP}} = 10^{-3}$ to Dumbser et al.
  (2014), as Zanotti et al. (2015) do. That suggests the published 2014
  paper has $\delta_0$, which the version read here lacks; it is not
  verified ([Balsara (2017)](/sources/balsara-2017-d.md), §VI.3, eq. 114).
* The same review presents MOOD for DG with at least $(K+1)^d$ subcells,
  not $2K+1$ per direction, and a TVD or low-order WENO subgrid fallback;
  it calls MOOD-limited DG "recursive and difficult to implement" (§§I.2,
  VI.3). This is a different presentation, not a contradiction of the
  choice argued above.

# Citations

1. [Dumbser et al. (2014)](/sources/dumbser-2014.md), §§1, 3, 4, 5, 6 (eqs. 17, 23–25 and 29 read from the page images).
2. [Zanotti et al. (2015)](/sources/zanotti-2015.md), §§1, 4, 5, 6 (eq. 17 read from the page image).
3. [Balsara (2017)](/sources/balsara-2017-d.md), §§I.2, VI.3.
