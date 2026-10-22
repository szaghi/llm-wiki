---
type: Method
title: "WENO limiters for discontinuous Galerkin"
description: "A WENO limiter replaces the DG polynomial of a troubled cell by a nonlinear, cell-average-preserving combination of polynomials from the cell and its neighbours; the page gives the compact simple WENO limiter, Du, Shu and Zhong's direction-wise characteristic variant with two polynomials per direction on triangles and point-cloud meshes, and the uses and critiques in the sources."
status: established
aliases: [simple WENO limiter, compact WENO limiter, improved simple WENO limiter, WENO limiter for RKDG, Qiu–Shu WENO limiter, HWENO limiter]
tags: [dg, weno, limiting, characteristic]
timestamp: 2026-10-22T18:00:00Z
---

# WENO limiters for discontinuous Galerkin

A **WENO limiter** for Runge–Kutta [discontinuous Galerkin](/methods/discontinuous-galerkin.md)
methods acts only in cells flagged by a
[troubled-cell indicator](/definitions/troubled-cell-indicator.md): there it
replaces the DG polynomial by a WENO-type convex combination of candidate
polynomials, built from the cell's own polynomial and those of its
neighbours, with nonlinear weights from
[smoothness indicators](/definitions/smoothness-indicator.md). The cell
average is kept, so the method stays conservative, and in smooth cells that
are wrongly flagged the reconstruction keeps the order of the DG solution.
The family, as recalled by [Du, Shu & Zhong (2022)](/sources/du-2022.md)
(§1), comprises the WENO and Hermite WENO limiters of Qiu and Shu, which
reconstruct on wider stencils, the compact **simple WENO limiter** of Zhong
& Shu (2013) and its triangle extension by Zhu, Zhong, Shu & Qiu (2013),
compact Hermite WENO limiters ([Hermite WENO](/methods/hermite-weno.md)),
and the multi-resolution WENO limiters of Zhu, Qiu & Shu, which "appear to be
quite robust" ([multi-resolution WENO](/methods/multi-resolution-weno.md)).

## The simple WENO limiter

The simple limiter uses only the DG polynomials of the target cell and of
its immediate neighbours, which matches the communication pattern of DG,
with simple linear weights (Du, Shu & Zhong, §1, §3, recalling Zhong & Shu
and Zhu et al.). On a triangle $K_0$ with neighbours $K_1,K_2,K_3$ and DG
polynomial vectors $p_0,\dots,p_3$ of degree $N$ (page-local $p_l$), each
neighbour polynomial is first shifted to the cell average of the target,
$$\tilde p_l(x)=p_l(x)-\frac{1}{\lvert K_0\rvert}\int_{K_0}p_l\,dx+\frac1{\lvert K_0\rvert}\int_{K_0}p_0\,dx,\qquad l=1,2,3$$
(Eq. (3.1); the neighbour polynomial is evaluated on $K_0$). Every convex
combination of $p_0$ and the $\tilde p_l$ then has the cell average of
$p_0$. For systems the combination is done in characteristic variables,
direction by direction: for each edge normal $n_l$ the original limiter
projects **all four** polynomial vectors onto the characteristic fields of
the normal Jacobian (§3.1); on polygonal meshes it projects $N_j+1$ vectors,
$N_j$ the number of neighbours (§3.2).

## Du, Shu and Zhong's direction-wise variant

[Du, Shu & Zhong (2022)](/sources/du-2022.md) (§3.1, Eqs. (3.1)–(3.8))
transform and combine only **two** polynomial vectors per direction, the
target and the neighbour across the edge:

1. Average correction (3.1) as above.
2. For each edge $l$, the Jacobian
   $A_l=n_{l,1}A^{(1)}(\bar p_0)+n_{l,2}A^{(2)}(\bar p_0)$ at the cell average
   $\bar p_0$, with left and right eigenvector matrices $L_l=R_l^{-1}$
   (Eq. (3.2); registry §1).
3. Project the two vectors, $\check p_0=L_lp_0$ and $\check p_1=L_l\tilde p_l$
   (Eq. (3.3); page-local $\check p$; the source writes double tildes).
4. Combine each characteristic component with two-polynomial WENO weights
   (Eqs. (3.4)–(3.5)):
   $$\check p^{\mathrm{new}}_l=\omega_0\check p_0+\omega_1\check p_1,\qquad \omega_k=\frac{\alpha_k}{\alpha_0+\alpha_1},\qquad \alpha_k=\frac{d_k}{(\epsilon+\beta_k)^2},\quad k=0,1,$$
   with $\epsilon=10^{-6}$ and the multi-dimensional Jiang–Shu-type indicator
   $$\beta_k=\sum_{1\le\lvert\ell\rvert\le N}\lvert K_0\rvert^{\lvert\ell\rvert-1}\int_{K_0}\Big(\frac{1}{\lvert\ell\rvert!}\,\partial^{\ell}\check p_k\Big)^2dx$$
   (Eq. (3.6); $\ell$ a multi-index, page-local).
5. Back-transform, $p^{\mathrm{new}}_l=R_l\check p^{\mathrm{new}}_l$ (Eq. (3.7)),
   and average the three directional results with the neighbour areas,
   $$p^{\mathrm{new}}_0(x)=\frac{\sum_{l=1}^3\lvert K_l\rvert\,p^{\mathrm{new}}_l(x)}{\sum_{l=1}^3\lvert K_l\rvert}$$
   (Eq. (3.8)).

The authors call the reduction from four (or $N_j+1$) to two transformed
polynomials per direction "the main difference and improvement" over the
original limiter (§3.1). Since both candidates are $(N+1)$th-order
approximations in smooth regions, any positive linear weights with
$d_0+d_1=1$ keep the accuracy (argued, not proved); a large $d_0$ gives a
non-oscillatory transition at shocks: $d_0=0.999$, $d_1=0.001$ on triangles,
$d_0=0.9995$, $d_1=0.0005$ on point clouds (§3.1, §4). The cell average is
kept because the shift (3.1), the linear maps $L_l$, $R_l$ and the convex
weights preserve it *(compiler check, not in the sources: each step is
linear or convex in the polynomials, and every candidate has the target
average)*.

**Polygonal meshes from point clouds** (§3.2, Eq. (3.9)). On the DG method
of Du & Shu for arbitrarily distributed points (as recalled: Voronoi
regions grouped into polygonal cells with at least $(N+1)(N+2)/2$ points
each), the direction $n_l$ is the unit vector between the centres of the
cell and of neighbour $l$, the centre being the mean of the generator points;
the directional results are averaged with the neighbour areas. The original
limiter transforms $N_j+1$ polynomials per direction, the new one still two.

The idea "may be generalized to other limiters with a characteristic-wise
limiting procedure" and to higher dimensions (§5); characteristic
projection is on [characteristic decomposition](/methods/characteristic-decomposition.md).

## Evidence

Du, Shu & Zhong test the 2D Euler equations ($\gamma=1.4$) with SSP-RK3,
CFL 0.3 ($N=1$) and 0.18 ($N=2$, 3; $\Delta t\sim h^{4/3}$ in $N=3$ accuracy
tests), the KXRCF indicator with threshold $C_k$ (page-local) tuned per
test, and a positivity-preserving limiter for $N=2$ on point clouds (§4).
The numerical flux is not stated. The claims are numerical; no theorem is
given.

- **Accuracy under over-flagging.** With $C_k$ lowered so that up to 78.94%
  ($N=1$), 90.85% ($N=2$) and 81.73% ($N=3$) of cells are flagged on the
  coarsest mesh of a sine density wave, both limiters keep order $N+1$ and
  the error level of the unlimited DG; the improved one perturbs it less,
  e.g. $N=1$, $h=2\pi/10$: $L^2$ error $2.46\times10^{-2}$ (improved),
  $3.87\times10^{-2}$ (original), $5.63\times10^{-3}$ (unlimited) (Ex. 4.1,
  Tables 4.1–4.3). The same holds on the
  [isentropic vortex](/benchmarks/isentropic-vortex.md) (Ex. 4.2) and on
  point clouds (Exs. 4.7–4.8), where all variants show reduced orders that
  the authors attribute to the random point sets.
- **Cost.** CPU time saved over the original limiter: 6.6–36.25% on triangle
  shock tests ([double Mach reflection](/benchmarks/double-mach-reflection.md)
  12.34% and 17.88%, [shock diffraction](/benchmarks/shock-diffraction.md)
  6.6% and 11.73%, Mach 3 [forward-facing step](/benchmarks/forward-facing-step.md)
  9.35% and 33.96%, NACA0012 20.19–36.25%), up to 54.92% on the point-cloud
  double Mach reflection ($N=2$, 800000 points) (Tables 4.7–4.10, 4.17–4.18).
  Even with no cell flagged, limited runs cost more than unlimited DG
  because of the troubled-cell detection (§4.1).
- **Resolution.** Less smearing of the Mach stem on the $N=2$ double Mach
  reflection; a spurious Mach stem at the bottom wall of the $N=2$ forward
  step "decreases" with the improved limiter; results almost identical on
  shock diffraction and NACA0012 (Exs. 4.3–4.6). On point clouds the authors
  state that the original limiter needed 1664000 points for the resolution
  that the improved one reaches with 800000 (Ex. 4.9).

## Use in other sources

- [Bai & Li (2022)](/sources/bai-2022.md) run their sharp-interface DG
  two-phase solver with a TVB minmod limiter, and with the simple WENO
  limiter of Zhong & Shu or the compact Hermite WENO limiter of Zhu et al.
  only for the two-phase Shu–Osher problem (§2, §2.6, §3.1.5).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) apply a locally divergence-free
  WENO limiter in KXRCF-flagged cells before the
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md) (§7), and
  [Cui, Ding & Wu (2024)](/sources/cui-2024.md) the Qiu–Shu WENO limiter
  (Exs. 3–5): the WENO limiter controls oscillations, the scaling limiter
  bounds.

## Positions on WENO limiters

- [Yu & Hesthaven (2022)](/sources/yu-2022.md) state that WENO and HWENO
  limiters that reconstruct the whole polynomial are "difficult to extend …
  to higher order cases (typically higher than 3rd order) due to the
  stability issue of extrapolation", and use an
  [artificial viscosity](/methods/artificial-viscosity.md) instead (§1).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) call troubled-cell limiters
  problem-dependent and replace them by a damping applied in every cell
  ([OEDG](/methods/oedg.md)).
- Du, Shu & Zhong argue the opposite need: since no troubled-cell indicator
  is "bullet-proof", the limiter itself must be harmless in wrongly flagged
  smooth cells (§3), which they test by deliberate over-flagging (§4).
- Du, Shu & Zhong list the a posteriori subcell finite-volume limiters of
  Dumbser and coworkers as another class (§1;
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

## Qualifications

- The attribution of the sharper Mach stem to "less information being used
  for reconstruction in each direction" (Abstract, §3.2) is not isolated by
  an experiment: the same runs also change the flagged fraction (e.g. 12.63%
  against 9.48% on the $N=2$ shock diffraction, Table 4.8).
- The unlimited DG itself is below design order on some tests ($N=2$
  isentropic vortex, $L^2$ orders 2.64–2.70, Table 4.5; $N=1$ point clouds,
  $L^\infty$ about 1.6, Table 4.11); "maintains the designed order" means
  that the limited runs match the unlimited ones.
- **Printed slips** (version of record). Table 4.6 prints for unlimited
  $N=3$ the CPU times of Table 4.5 ($N=2$), which would make the $N=3$
  limited runs about four times dearer than unlimited ones with no cell
  flagged, unlike Ex. 4.1; the text after Eq. (3.5) writes $\beta_l$ for
  $\beta_1$; ref. [37] duplicates ref. [34]. The statement that the time
  saved decreases with refinement (§4.1) is not monotone in Table 4.2
  (40.61, 44.29, 40.63, 27.91, 1.77%).

# Citations

- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1; §3 (Eqs. (3.1)–(3.9)); §4 (Exs. 4.1–4.10, Tables 4.1–4.18, Figs. 4.2–4.16); §5.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2, §2.6 (TVB minmod limiter), §3.1.5 (simple or Hermite WENO limiter for the two-phase Shu–Osher problem).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §7 (locally divergence-free WENO limiter).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §8, Exs. 3–5 (Qiu–Shu WENO limiter).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §1 (critique of WENO/HWENO limiters).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1 (troubled-cell limiters problem-dependent).
