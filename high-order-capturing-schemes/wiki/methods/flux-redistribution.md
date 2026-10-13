---
type: Method
title: "Flux redistribution for small cut cells"
description: "The most common small-cell cure of cut-cell finite volume: a cut cell takes a stable hybrid of its conservative flux divergence and a neighbourhood average, and the conserved amount this withholds is handed to its neighbours with weights whose volume-weighted sum is one, so the step follows the regular cells and the scheme stays conservative; first order at the cut cells, not linearity-preserving and not monotone, with a re-redistribution correction under AMR; contrasted with state redistribution."
status: established
aliases: [FRD, flux redistribution, hybrid divergence, redistribution of excess mass, flux re-redistribution]
tags: [embedded-boundary, boundary-treatment, cut-cell, conservation, amr, cartesian-grid]
timestamp: 2026-10-13T00:00:00Z
---

# Flux redistribution for small cut cells

In [cut-cell finite volume](/methods/cut-cell-finite-volume.md) an explicit
update divides the flux balance of cell $I_i$ by its volume
$\vert I_i\vert = \kappa_i h^d$, so the stable step vanishes with
$\kappa_i$. Flux redistribution (FRD) lets every cell take the step of
the regular cells: a cut cell keeps only a stable part of its update, and
the rest is handed to its neighbours so that the total is conserved
([Natarajan et al. (2022)](/sources/natarajan-2022.md), §§1–2). Berger &
Giuliani call it "the most commonly used stabilization algorithm", already
run in 3D "due to its simplicity"
([Berger & Giuliani (2021)](/sources/berger-2021.md), §1).

**Origin, as cited.** None of the originating papers is in the corpus, and
the citing sources name different ones:
* Chern & Colella (1987) and Colella, Graves, Keen & Modiano (2006)
  ([Berger & Giuliani (2021)](/sources/berger-2021.md), §1;
  [Giuliani et al. (2022)](/sources/giuliani-2022.md), §1);
* Colella et al. (2006) and Pember et al. (1995) ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §§1–2);
* Pember et al. (1995) first among six compressible-flow and two
  incompressible-flow works; the neighbourhood average of Appendix A
  follows Trebotich & Graves, with Pember et al. and Colella et al. as an
  alternative ([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §1, App. A).

## The algorithm

As printed by [Natarajan et al. (2022)](/sources/natarajan-2022.md) (§2)
and [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md)
(App. A, eqs. A.1–A.4), for one cut cell $I_i$ and one step:
1. **Conservative divergence**, the usual flux balance over the cut cell,
   $(\nabla\cdot\mathbf f)^{\mathrm c}_i = \frac{1}{\vert I_i\vert}\oint_{\partial I_i}\mathbf f\cdot\mathbf n\,dA$,
   the embedded-boundary face included.
2. **Non-conservative divergence**, a volume-fraction-weighted average of
   the conservative divergences over the FRD neighbourhood of $I_i$:
   $$(\nabla\cdot\mathbf f)^{\mathrm{nc}}_i = \frac{\sum_j\kappa_j\,(\nabla\cdot\mathbf f)^{\mathrm c}_j}{\sum_j\kappa_j},$$
   both sums over that neighbourhood: the fluid cells of the 3×3×3 block
   around $I_i$ that can be reached from it (Natarajan et al.); Barrio
   Sanchez et al. make "reached" precise as a monotone index path through
   valid cells. It is not the merging neighbourhood $\mathcal N_i$ of
   state redistribution.
3. **Hybrid update** of the cut cell,
   $$u^{n+1}_i = u^n_i - \Delta t\left[\kappa_i(\nabla\cdot\mathbf f)^{\mathrm c}_i + (1 - \kappa_i)(\nabla\cdot\mathbf f)^{\mathrm{nc}}_i\right].$$
   Since $\kappa_i(\nabla\cdot\mathbf f)^{\mathrm c}_i = h^{-d}\oint\mathbf f\cdot\mathbf n\,dA$,
   no $\kappa_i$ remains in a denominator, which is what removes the
   small-cell step restriction; the update "is not strictly conservative"
   (Natarajan et al., §2).
4. **Redistribution.** Against the conservative update, the hybrid update
   leaves the cut cell with an excess
   $-\Delta t(1 - \kappa_i)\left[(\nabla\cdot\mathbf f)^{\mathrm{nc}}_i - (\nabla\cdot\mathbf f)^{\mathrm c}_i\right]$
   per unit volume of the cut cell. Its opposite, in total
   $\kappa_i(1 - \kappa_i)h^d\,\Delta t\left[(\nabla\cdot\mathbf f)^{\mathrm{nc}}_i - (\nabla\cdot\mathbf f)^{\mathrm c}_i\right]$
   (Barrio Sanchez et al., eq. A.2), is added to the neighbours of $I_i$,
   so that the sum over all cells matches the conservative update; each
   cell's final state is its own update plus the shares it receives from
   every neighbouring cut cell.

**The weights.** Conservation requires only that the shares add up to the
withheld amount: if neighbour $I_j$ receives the state increment
(intensive) equal to a weight times that amount, the weights times the
neighbour volumes $\vert I_j\vert$ must sum to one over the neighbourhood
(Natarajan et al., eq. 1). The two printed choices differ:
* Natarajan et al. take the weight $\kappa_j/\sum_k\kappa_k^2$ per unit
  withheld amount per regular-cell volume, described as volume weighting
  "assuming equal volumes for all cells"; the state increment of a
  neighbour is then proportional to its $\kappa_j$, and its extensive
  share to $\kappa_j^2$.
* Barrio Sanchez et al. take the same weight $1/(h^d\sum_k\kappa_k)$ for
  every neighbour (eq. A.4): all neighbours receive the same state
  increment, and the extensive shares are proportional to $\kappa_j$.

Upwind or mass weighting are named as alternatives (Natarajan et al.), and
a density weighting $\rho_j/\sum_k\rho_k\vert I_k\vert$ "is
often used" in gas dynamics (Barrio Sanchez et al., App. A); Giuliani et
al. plan to borrow density weighting from Pember et al. for state
redistribution ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §7).
No source compares the weightings.

**Berger & Giuliani's summary of the idea** (§1). Write the cut-cell
update as a change of its conserved content; the cut cell receives only a
fraction of it. "If the fraction … is proportional to the cell's volume
fraction … the update should be stable", and the rest of the change goes
to the neighbours. The stability is stated, not proved.

## Properties

* **Conservation** holds by construction on a static body, through the
  weight condition above. On a moving body the closed-piston mass loss of
  Natarajan et al. (up to 0.92 % at $32^3$) shows consistency, not
  conservation, and comes from their moving update rather than from the
  redistribution (see the [cut-cell page](/methods/cut-cell-finite-volume.md),
  "Moving bodies").
* **Accuracy.** FRD is "only first order accurate at the cut cells" and is
  not linearity-preserving ([Berger & Giuliani (2021)](/sources/berger-2021.md), §§1–2;
  [Giuliani et al. (2022)](/sources/giuliani-2022.md), §1;
  [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §1).
  Natarajan et al. state that their scheme "has an accuracy of 2 for smooth
  problems" and measure order 1 on a receding piston, attributed to the
  fill of freshly cleared cells
  ([Natarajan et al. (2022)](/sources/natarajan-2022.md), §3.2.2, Fig. 5c).
  The two statements meet in the open entry "What order does flux
  redistribution give, and what limits it on moving bodies?" under
  `Contradictions` on the [cut-cell finite volume](/methods/cut-cell-finite-volume.md)
  page; it is not restated here.
* **Not monotone.** In the 1D analysis of state redistribution the
  neighbour coefficients turn negative for small cells, "also the case
  with flux redistribution", so neither scheme is monotone or TVD
  ([Berger & Giuliani (2021)](/sources/berger-2021.md), §2). In linear
  advection of a Heaviside profile along a 40° and a 50° ramp, FRD
  "generates overshoots and undershoots" after 10 steps while both state
  redistribution variants do not, although none of them guarantees
  monotonicity ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §3.2, Fig. 4).
* **Positivity and boundedness.** No source claims either for FRD
  (Natarajan et al. make no monotonicity or positivity claim). A 3D
  reacting fuel-injection run in a piston bowl "is not possible with the
  standard flux redistribution scheme as it leads to unphysical solution
  values (e.g. concentrations less than 0 or > 1)"; state redistribution
  ran it ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §6.1;
  [positivity preservation](/properties/positivity-preserving.md)).
* **In production.** FRD "was the stabilization technique in AMReX", and
  AMReX-Hydro carries modules for both flux and state redistribution
  ([Giuliani et al. (2022)](/sources/giuliani-2022.md), §§3.2, 4); the
  moving-body solver of Natarajan et al. uses it inside AMReX.

## Under AMR: flux re-redistribution

Redistribution done one level at a time sends conserved quantities across
the coarse–fine boundary into cells outside the composite solution:
covered coarse cells and fine ghost cells. Barrio Sanchez et al.
take the FRD repair from Pember et al.
([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), App. B):
* the register at each uncovered coarse cell next to the interface sums
  four kinds of misdirected shares: from uncovered into covered coarse
  cells and back, and from valid into ghost fine cells and back, each
  formed from the same weights and withheld amounts as the single-level
  step;
* at synchronization the register, together with the refluxing
  correction, is not added in full to a cut coarse cell, which "could
  introduce an instability": the cell keeps the fraction $\kappa_i$ and
  the rest is spread over its FRD neighbourhood in proportion to volume,
  with covered targets passed down to the fine cells by piecewise-constant
  interpolation (§3.4).

The same paper uses this FRD-style spreading for the synchronization of
weighted state redistribution
([state redistribution](/methods/state-redistribution.md), "Re-redistribution
under AMR"). On a 2D channel with Godunov time stepping, flux
re-redistribution keeps the mass to round-off as state re-redistribution
does (§4.1, Fig. 3c; observed, no proof). Codes without it keep the
coarse–fine boundary off the cut cells or refine every cut cell to the
finest level ([cut-cell page](/methods/cut-cell-finite-volume.md), "Cut
cells and AMR").

## Against state redistribution

Both start from the same conservative but unstable provisional update and
both modify cut and regular cells. FRD redistributes the update before it
is applied; [state redistribution](/methods/state-redistribution.md)
applies it and then redistributes the updated states
([Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§1–3,
eqs. 3–4). The difference that matters is the linear reconstruction on
the merging neighbourhoods: state redistribution preserves linear
functions (proved), FRD does not
([Berger & Giuliani (2021)](/sources/berger-2021.md), §§2, 4.3). Measured
consequences are the ramp-advection over- and undershoots and the
reacting-flow bounds violations above; the boundary order of state
redistribution, about 1.4 in the $L^1$ norm on the supersonic vortex, is
not matched by an FRD convergence study in the corpus.

# Citations

1. [Berger & Giuliani (2021)](/sources/berger-2021.md), §§1–2, 4.3 (arXiv v1).
2. [Natarajan et al. (2022)](/sources/natarajan-2022.md), §§1–2, 3.2.2, eq. 1 (arXiv v1).
3. [Giuliani et al. (2022)](/sources/giuliani-2022.md), §§1, 3.2, 4, 6.1, 7, Fig. 4 (arXiv v2).
4. [Barrio Sanchez et al. (2024)](/sources/barriosanchez-2024.md), §§1–4.1, Apps. A–B, Fig. 3c (arXiv v1).
