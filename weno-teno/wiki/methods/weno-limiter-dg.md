---
type: Method
title: "WENO limiters for discontinuous Galerkin"
description: "A WENO limiter replaces the DG polynomial of a troubled cell by a nonlinear, cell-average-preserving combination of polynomials from the cell and its neighbours; the page gives the simple WENO limiter, a direction-wise variant, a same-order CWENOZ replacement on mixed meshes, a TENO-weighted compact limiter, a TENO-THINC limiter with a compact BVD switch, and critiques."
status: established
aliases: [simple WENO limiter, compact WENO limiter, improved simple WENO limiter, WENO limiter for RKDG, Qiu–Shu WENO limiter, HWENO limiter, TENO limiter for RKDG]
tags: [dg, weno, teno, limiting, characteristic]
timestamp: 2026-10-24T06:00:00Z
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

## Same-order CWENOZ replacement on mixed unstructured meshes

[Maltsev et al. (2023)](/sources/maltsev-2023.md) (§2.1–2.4, Eq. 33)
build hybrid DG–finite-volume schemes up to fifth order ($N=2$ to $4$) on
mixed-element meshes in 2D and 3D, in [UCNS3D](/software/ucns3d.md). The
modal DG uses a cell-centred Taylor basis normalized by $h_i$ (page-local), the square
root of the cell volume, whose modes $k=1,\dots,\mathcal K$ (page-local $\mathcal K$) have zero cell mean; without
the normalization they "could not achieve higher than 4th of accuracy"
(§2.1, stated without data). The finite-volume reconstruction is
[CWENOZ](/methods/cweno.md) on the same Taylor basis: a least-squares
central polynomial on $2\mathcal K$ neighbours combined with lower-order
directional polynomials, weights
$\alpha_s=d_s\big(1+\tau/(\epsilon+\beta_s)\big)$, $\omega_s=\alpha_s/\sum_l\alpha_l$, with
$\tau$ the mean absolute difference of the directional indicators from
the central one raised to the power 4, $\epsilon=10^{-14}$, and a
non-normalized central linear weight $10^7$ (Eqs. 18–28; stencils
numbered from $s=1$, the central one). At every Runge–Kutta stage the unlimited
DG solution is checked by a [troubled-cell indicator](/definitions/troubled-cell-indicator.md),
a priori; in troubled cells the DG coefficients of modes $1,\dots,\mathcal K$ are
overwritten by the CWENOZ coefficients reconstructed from the cell
averages, and mode 0 is kept, so the replacement is a copy of
coefficients and conservative. The reconstruction has the same order as
the DG polynomial (DG degree $N$ with CWENOZ of order $N+1$), so no order is
lost in a wrongly flagged cell.

Their evidence (§3, Appendix B):

- with every cell flagged, the hybrid keeps the design order on smooth
  advection on quadrilaterals ($L^2$ orders 3.01, 4.04, 4.99 for
  $N=2,3,4$), as accurate as pure CWENOZ (Table B.4);
- pure DG reaches close to design order on the
  [isentropic vortex](/benchmarks/isentropic-vortex.md), CWENOZ of the
  same order only on finer meshes ($N=4$ on quadrilaterals:
  DG $2.97\times10^{-4}\to1.14\times10^{-9}$, CWENOZ
  $7.64\times10^{-2}\to7.20\times10^{-4}$ over 8 to 64 edges per side,
  Table 1), and the hybrid approaches DG as the mesh is refined;
- the hybrid costs 1.4–1.5 times pure DG on coarse meshes and about 1.05
  times on fine ones (Table 1);
- on Schardin's shock–wedge problem the hybrids resolve more structure
  and acoustic waves than pure fifth-order CWENOZ, with below 0.4 % of
  cells troubled (§3.5; [shock diffraction](/benchmarks/shock-diffraction.md));
- on the inviscid [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
  at $64^3$ the hybrid is closer to the DNS than pure FV but its modal DG
  part shows aliasing, though it runs without over-integration, filtering
  or split-form fluxes (§3.6); on the LM1021 sonic-boom case it matches
  the measured pressure signature better than third-order CWENOZ (§3.8).

## TENO-weighted compact limiter

[Huang & Fu (2024)](/sources/huang-2024.md) (§4.4, §5.2) keep the
candidate polynomials of the compact Hermite WENO limiters and replace
the WENO weighting by the stencil selection of
[TENO](/methods/targeted-eno.md), for third-order RKDG ($N=2$). In 1D the
DG solution of $I_i$ is $\sum_{l=0}^2u^{(l)}_iv_l$ in the scaled Legendre
basis $v_0=1$, $v_1=(x-x_i)/\Delta x$, $v_2=v_1^2-\tfrac1{12}$, with
$\int_{I_i}v_l^2\,dx=c_l$ (page-local $u^{(l)}_i$, $v_l$, $c_l$; Eq. 16).
The cell average $u^{(0)}_i$ is kept, and the two higher modes are
rebuilt one after the other from candidates on the cell and its two
neighbours (numbered as in the source, $k=2$ the central one):

| mode | candidates $p_0$, $p_1$, $p_2$ | target (page-local $P_{\mathrm{tar}}$) | linear weights $d_0,d_1,d_2$ |
|---|---|---|---|
| $u^{(1)}_i$ | quadratics: averages of $I_{i-1},I_i$ and first moment of $I_{i-1}$; averages of $I_i,I_{i+1}$ and first moment of $I_{i+1}$; the three averages | quartic: three averages and the first moments of $I_{i\pm1}$ | $\tfrac{11}{38},\tfrac{11}{38},\tfrac8{19}$ |
| $u^{(2)}_i$ | cubics: averages and first moments of $I_{i-1},I_i$; of $I_i,I_{i+1}$; three averages and the first moment of $I_i$ | quintic: three averages and three first moments | $\tfrac{45}{154},\tfrac{45}{154},\tfrac{32}{77}$ |

The linear weights make the combination of the candidates' moments equal
the target's moment, $\int_{I_i}P_{\mathrm{tar}}v_l=\sum_kd_k\int_{I_i}p_kv_l$
(Eqs. 37–40, 47–49). The nonlinear step is (Eqs. 41–46, 50)
$$\beta_k=\sum_{l=1}^{2}\int_{I_i}\Delta x^{2l-1}\big(\partial_x^lp_k\big)^2dx,\qquad
\gamma_k=\frac{t_k}{(\beta_k+\epsilon)^q},\qquad
\omega_k=\frac{d_k\delta_k}{\sum_ld_l\delta_l},\qquad
u^{(l),\mathrm{new}}_i=\frac1{c_l}\sum_k\omega_k\int_{I_i}p_kv_l\,dx,$$
with $\chi_k=\gamma_k/\sum_l\gamma_l$, $\delta_k=0$ if $\chi_k<C_T$, the
cut-off $C_T=10^{-4}$, $q=6$, $\epsilon=10^{-10}$, and a bias $t_0=t_1=1$,
$t_2=10$ (page-local) "to enlarge the chance to choose the central
stencil". This $\gamma_k$ has neither the constant $C$ nor the global
indicator $\tau$ of the registry's TENO measure. When all three
candidates survive, the new mode is the target's moment; otherwise it is
the renormalized convex combination of the surviving candidates. There is
no option that keeps the target when some candidate is cut.

In 2D (§5.2, Eqs. 51–64) the limiter rebuilds the five higher modes of a
$\mathbb P^2$ solution on rectangles from eight quadratic candidates on
the $3\times3$ block: four match the averages of a $2\times2$ sub-block
plus one $x$- and one $y$-moment, as in the Hermite WENO limiter, and four
match six cell averages. Exactness conditions plus a minimum-norm
condition $\min\sum_k(d_k^{(l)})^2$ give linear weights $\tfrac{11}{76}$
(first four) and $\tfrac2{19}$ (last four) for the two first-order modes,
and $\tfrac18$ for every candidate for the three second-order modes
(Eqs. 56–58). The bias is $t=10$ on the six-average candidates. The
indicators of the second-order modes add first-derivative terms to those
of the Hermite WENO limiter "for better robustness" (Eq. 59; no ablation
shown). The limiter acts only in cells flagged by the authors' TENO-type
[troubled-cell indicator](/definitions/troubled-cell-indicator.md), and
standard RKDG runs elsewhere.

**Evidence** (§6; Euler, $\gamma=1.4$, SSP-RK3, CFL 0.15, Rusanov flux).
On the [density wave](/benchmarks/density-wave-advection.md) the
indicator flags no cell, so limited and unlimited runs give identical
errors ($L^1$ $3.53\times10^{-7}\to6.94\times10^{-10}$ for
$N_x=100\to800$, orders 2.99–3.00, Table 1). Forcing limiting with the
TVB indicator at $M=1$ keeps third order ($L^1$ $3.02\times10^{-6}\to
5.58\times10^{-9}$, $N_x=50\to400$, orders 3.05, 3.02, 3.01, Table 2; in
2D $L^1$ orders 2.79, 2.90, 2.99, Table 4). On the
[Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md), the
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md),
the [Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
[double Mach reflection](/benchmarks/double-mach-reflection.md) and
configuration 3 of the
[two-dimensional Riemann problems](/benchmarks/two-dimensional-riemann-problems.md),
the TENO limiter is oscillation-free and resolves more small-scale
structure than the compact WENO limiter of Zhu, Qiu and Zhu (2020) driven
by the same indicator. The comparison is visual; no error norm or
spectral measure is given for the discontinuous tests.

## TENO-THINC limiter with a compact BVD switch

[Huang et al. (2025a)](/sources/huang-2025.md) replace, in third-order
modal RKDG ($N=2$, the scaled Legendre basis above), the Hermite-type
candidates by two simpler candidate polynomials. A compact
[boundary-variation-diminishing](/definitions/boundary-variation-diminishing.md)
rule chooses between them (§3.2–3.3). The limiter acts only in cells
flagged by the TENO indicator of Huang & Fu (2024), with $\epsilon=10^{-3}$,
$q=6$, $C_T=10^{-4}$ (§3.1).

- **TENO candidate** (Eqs. (15)–(19)). The smoothness indicators
  $\beta_l$ of the three DG polynomials $p_{i-1},p_i,p_{i+1}$ give
  $\gamma_l=1/(\beta_l+\epsilon_1)^6$, normalized and cut off at
  $C_T=10^{-5}$, with $\epsilon_1=10^{-10}$. If all three survive, $p_i$ is
  kept. Otherwise $p^{\mathrm{TENO}}_i=\sum_l\delta_lp_l/\sum_m\delta_m$:
  surviving stencils get equal weights, with no linear weights. The
  authors say $\epsilon_1$ "also acts as a cutoff of the smoothness
  measurements", after Castro et al.
- **THINC candidate** (Eqs. (20)–(21)). Interface values come from the
  three cell averages by the THINC formula
  $\hat u_{i+1/2}=f_{\mathrm m}+f_{\mathrm j}\frac{\mathcal A+\mathcal T}{1+\mathcal A\mathcal T}$,
  with page-local $f_{\mathrm m}=\tfrac12(\bar u_{i+1}+\bar u_{i-1})$ and
  $f_{\mathrm j}=\tfrac12(\bar u_{i+1}-\bar u_{i-1})$ (the source's
  $\bar u_\pm$), $\mathcal T=\tanh(\beta_{\mathrm T}/2)$,
  $\mathcal A=\frac{\operatorname{sgn}(\varsigma)}{\mathcal T}\frac{e^{\lvert\varsigma\rvert\beta_{\mathrm T}}-1}{e^{\lvert\varsigma\rvert\beta_{\mathrm T}}+1}$
  and $\varsigma=(\bar u_i-f_{\mathrm m})/f_{\mathrm j}$ (the source's
  $\alpha$), steepness $\beta_{\mathrm T}=1.6$, as on
  [THINC reconstruction](/methods/thinc-reconstruction.md). The value falls back to $\bar u_i$ when
  $(\bar u_{i-1}-\bar u_i)(\bar u_i-\bar u_{i+1})<10^{-15}$. The THINC
  polynomial is the unique quadratic with the cell integral of $p_i$ and
  these two interface values
  ([THINC reconstruction](/methods/thinc-reconstruction.md)).
- **Compact BVD** (Eqs. (22)–(24)). For each candidate, the total
  boundary variation is the sum of its jumps against the *unlimited*
  traces $p_{i\pm1}(x_{i\pm1/2})$ of the neighbours. THINC is chosen when
  $\mathrm{TBV}^{\mathrm{TENO}}-\mathrm{TBV}^{\mathrm{THINC}}>\max\big(10^{-10},10^{-3}(\mathrm{TBV}^{\mathrm{TENO}}+\mathrm{TBV}^{\mathrm{THINC}})\big)$.
  Because the neighbours' unlimited traces are used, the limiter stays on
  the three-cell stencil. The authors set this against Jiang et al.'s
  BVD, which "requires the reconstructed values of neighboring cells"
  (§1, §3.2.3).
- **Systems and 2D** (§3.3, §4.2). Indicator and limiter act on local
  characteristic variables, and the limiter is skipped when every
  component is smooth. In 2D the weights computed on the traces at
  $y=y_j$ rebuild only the $x$-only modes, and those at $x=x_i$ the
  $y$-only modes. The mixed mode is always the average of the $x$- and
  $y$-TENO combinations and never uses THINC, "to enhance robustness"
  (Eqs. (27)–(36)). The THINC weights in 2D solve a $3\times3$ system and
  are not constrained to be non-negative.

**Evidence** (§5; Euler, SSP-RK3, CFL 0.15, local Lax–Friedrichs flux;
the comparison is the Zhong–Shu simple WENO limiter driven by the same
indicator).

- **Smooth flows.** On the 1D and 2D density waves no cell is flagged, so
  the errors equal the unlimited ones (Tables 1, 3). They also equal them
  with the limiter forced on in every cell, because the BVD rule picks
  TENO and TENO keeps $p_i$ (Table 2).
- **Cost.** On Lax's problem the run takes 172.08 s against 163.07 s
  with the WENO limiter (Table 4). The hardware is not stated.
- **Flagged fraction.** On the $1200\times300$ double Mach reflection,
  34681 cells (9.63 %) are flagged, and THINC is selected in 6476 of them
  (1.8 % of the domain) (§5.5, Fig. 6).
- **Shocked flows.** On Sod, Lax, the blast waves, Shu–Osher, the double
  Mach reflection, 2D Riemann configuration 7 and Rayleigh–Taylor, the
  authors report sharper discontinuities and more small-scale structure
  than with the WENO limiter. On Shu–Osher the gain is "not as obvious".
  On Rayleigh–Taylor the symmetry breaks under round-off, which they
  attribute to the low dissipation (§5.4, §5.7). The evidence is visual.

## Nodal Hermite TENO limiter for spectral difference

[Chen & Fu (2024)](/sources/chen-2024.md) (§5–§7, Algorithm 1) build a
limiter for the nodal [spectral difference method](/methods/spectral-difference-method.md)
at third and fourth order (SD3, SD4: $N_{\mathrm s}=3,4$ solution points per
direction, polynomials of degree $N_{\mathrm s}-1$; page-local $N_{\mathrm s}$),
which they state applies to other nodal discontinuous methods as well. It
works **dimension by dimension** along each line of solution points and
uses only the target cell and its two face neighbours in that direction.
From the nodal values it computes, by quadrature, each cell's average and
the averages of the first and second derivatives of its polynomial
(Eqs. (28)–(35)), and builds Hermite candidates from them:

- **3-DoF reconstruction** (both orders): quadratics $p_0$ (averages of
  $I_{i-1},I_i$ and the derivative average of $I_{i-1}$), $p_1$ (three
  averages) and $p_2$ (averages of $I_i,I_{i+1}$ and the derivative average
  of $I_{i+1}$) (Eq. (36));
- **4-DoF reconstruction** (SD4): cubics $p_3,\dots,p_6$ that add first, or
  first and second, derivative averages of a neighbour (Eq. (51)).

Instead of limiting low-order moments one after another, as compact
Hermite WENO limiters do, the limiter takes a direct convex combination of
these high-order candidates (§1). The linear weights make the average of
the first derivative over $I_i$ third-order and that of the second
derivative second-order accurate (Eqs. (38)–(48)), and depend on the
solution-point set: $d=(8/31,15/31,8/31)$ for SD3,
$(1/4,1/2,1/4)$ for SD4, and $(5/14,5/14,1/7,1/7)$ for the four cubics
(Eqs. (49)–(50), (54)). The nonlinear weights are of
[WENO-JS](/methods/weno-js-reconstruction.md) form ($q=2$,
$\epsilon=10^{-12}$) or of [TENO](/methods/targeted-eno.md) form with $C=1$,
$q=6$, $\tau=\tfrac12(\lvert\beta_0-\beta_1\rvert+\lvert\beta_1-\beta_2\rvert)$
for three candidates and $\tfrac12\lvert\beta_3+\beta_5-\beta_4-\beta_6\rvert$
for four, and an adaptive cut-off $C_T$ from Ren's discontinuity measure
mapped by $(1-m)^4(1+4m)$ ([adaptive TENO](/methods/adaptive-teno.md);
$C_T\in[10^{-8},10^{-4}]$ for 3-DoF and $[10^{-7},10^{-3}]$ for 4-DoF
*(compiler check, not in the sources: the bounds of their Eq. (65) with
the stated $\alpha_1$, $\alpha_2$)*). At fourth order the cubics are used
whenever any of them survives the cut-off, and the quadratics otherwise
(§5.7). For the Euler equations the limiting is characteristic-wise, with
the Jacobian at the cell average of the sweep direction; the $x$- and
$y$-limited nodal values are averaged (Eqs. (70)–(75)), and every step
keeps the cell average. In cells where a five-point scale sensor exceeds
$0.6$ a linear compression toward the average follows
([Zhang–Shu scaling limiter](/methods/zhang-shu-scaling-limiter.md)). The
limiter acts in the directions flagged by their TENO-type
[troubled-cell indicator](/definitions/troubled-cell-indicator.md).

**Evidence** (§9; SSPRK(5,3), CFL 0.3). With every cell forced troubled
on a 2D [density wave](/benchmarks/density-wave-advection.md) all limiters
keep the design order, e.g. $L_1$ orders 3.03, 3.08 for SD3 with TENO3-A
and 4.13, 4.09 for SD4 with TENO4-A, the TENO-A errors being "about half"
of the WENO ones (Table 1); at $80^2$ the limited SD3 error,
$1.99\times10^{-6}$, is below the unlimited one, $2.60\times10^{-6}$. On the
[Sod and Lax tubes](/benchmarks/sod-and-lax-shock-tubes.md), the
[Shu–Osher problem](/benchmarks/shu-osher-problem.md), the
[double Mach reflection](/benchmarks/double-mach-reflection.md), the
[triple point](/benchmarks/triple-point-problem.md), a
[two-dimensional Riemann problem](/benchmarks/two-dimensional-riemann-problems.md),
the [Rayleigh–Taylor instability](/benchmarks/rayleigh-taylor-instability.md)
and a [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md)
the TENO-A limiter resolves more small-scale structure than the WENO
limiter; lowering $C_T$ lowers the dissipation (Fig. 13). On the
shock–bubble case TENO4-A brings no significant gain over TENO3-A, and
TENO3-A combined with SD4 degrades the results against SD3, which the
authors take as the reason a fourth-order limiter is needed (§9.4, §9.8;
the second point stated without figure). Comparisons are visual.

## Evidence

Du, Shu & Zhong test the 2D Euler equations ($\gamma=1.4$) with SSP-RK3,
CFL 0.3 ($N=1$) and 0.18 ($N=2$, 3; $\Delta t\sim\Delta x^{4/3}$, $\Delta x$ the mesh size, in $N=3$ accuracy
tests), the KXRCF indicator with threshold $C_k$ (page-local) tuned per
test, and a positivity-preserving limiter for $N=2$ on point clouds (§4).
The numerical flux is not stated. The claims are numerical; no theorem is
given.

- **Accuracy under over-flagging.** With $C_k$ lowered so that up to 78.94%
  ($N=1$), 90.85% ($N=2$) and 81.73% ($N=3$) of cells are flagged on the
  coarsest mesh of a sine density wave, both limiters keep order $N+1$ and
  the error level of the unlimited DG; the improved one perturbs it less,
  e.g. $N=1$, mesh size $2\pi/10$: $L^2$ error $2.46\times10^{-2}$ (improved),
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
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) (§3.1.3, arXiv v1) apply
  the Hermite WENO limiter of Zhao and Qiu to the first moments of
  KXRCF-flagged cells of a finite-volume Hermite WENO scheme for
  relativistic hydrodynamics (moments, not a DG polynomial), with weights
  $d_k\big(1+\tau^2\Delta x/(\beta_k^2+\epsilon)\big)$ that they call
  scale-invariant; the values of the linear weights, of $\epsilon$ and of
  the KXRCF threshold are not printed
  ([Hermite WENO](/methods/hermite-weno.md),
  [scale invariance](/properties/scale-invariance.md)).

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
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) list the
  Hermite WENO limiter of Qiu and Shu and the WENO limiter of Zhu et al.
  (as cited) among DG shock-capturing options, with artificial viscosity
  and subcell finite volumes, and choose the last; their argument, after
  Li and Jameson, is that $h$-refinement is better at discontinuities and
  $p$-refinement more efficient in smooth regions, which finite-volume
  subcells inside a $p$-adaptive DG realize (§1;
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md),
  [h- and hp-adaptation](/methods/hp-adaptation.md)).
- Huang & Fu call the compact WENO limiter of Zhu, Qiu and Zhu "highly
  dissipative" and motivate the TENO limiter by its smearing of small
  scales (§1, §6); the evidence is the visual comparisons above.
- Du, Shu & Zhong list the a posteriori subcell finite-volume limiters of
  Dumbser and coworkers as another class (§1;
  [subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).

- [Cao et al. (2026)](/sources/cao-2026.md) group WENO and simple WENO
  limiters with the TVB, moment and MP limiters that modify KXRCF-flagged
  cells after every Runge–Kutta stage, and fault WENO and MP limiters for
  their wide stencils, against which their [COS(DG)](/methods/cos-dg.md)
  post-processing uses only the two face neighbours (§1, Property 2.1). In
  their comparisons the Qiu–Shu WENO limiter and the simple WENO limiter of
  Zhong & Shu, flagged by KXRCF, are among seven limiters whose results are
  taken from Zhu, Cheng & Qiu's 2013 comparison; third-order COS(DG) gives
  sharper non-oscillatory profiles on a strong single shock, the Lax,
  Woodward–Colella and Shu–Osher problems and 2D Burgers (Figs. 1, 6, 8,
  10, 11, 13). The comparison is visual.

- **Compact stencils.** Chen & Fu contrast their face-neighbour stencil
  with the RKDG WENO and TENO limiters of Qiu & Shu and Huang & Fu, whose
  eight candidate stencils each include at least one cell that does not
  share a face with the target (§7, Fig. 3), and state that the direct
  combination of high-order candidates is more efficient at high order
  than moment-by-moment Hermite WENO limiting (§1, §10; no timing given).
- **Against subcell limiting on unstructured meshes.** Maltsev et al.
  prefer replacing the modes to subcell finite-volume limiting, which
  keeps more of the DG subcell information but is "not as
  straightforward" on meshes with arbitrary elements, transition layers
  and poor cells and may restrict the time step (§2.4;
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

- **Printed slips in Huang & Fu.** The fourth line of their Eq. (38)
  prints the target's first moment as
  $c_1\big(\tfrac{15}{19}(u^{(0)}_{i-1}-u^{(0)}_{i+1})-\tfrac{11}{38}(u^{(1)}_{i-1}+u^{(1)}_{i+1})\big)$;
  for the linear function $u=(x-x_i)/\Delta x$ ($u^{(0)}_{i\pm1}=\pm1$,
  all $u^{(1)}=1$, exact moment $c_1$) this gives $-\tfrac{41}{19}c_1$,
  while the average term with $u^{(0)}_{i+1}-u^{(0)}_{i-1}$ gives $c_1$;
  the other three lines and the weights of Eqs. (40) and (49) are
  consistent *(compiler check, not in the sources)*. In Table 2 the $L^\infty$
  error of the new limiter at $N_x=50$ is printed $5.38\times10^{-7}$,
  below the $N_x=100$ value $5.56\times10^{-7}$; the printed order 3.27
  is $\log_2$ of $5.38\times10^{-6}/5.56\times10^{-7}$ *(compiler check,
  not in the sources)*. Eq. (56) enforces exactness for basis functions
  $v_6,\dots,v_9$ that the paper never defines, so the 2D weights cannot
  be re-derived from the text.
- **Huang et al. (2025a) against Huang & Fu (2024).** The 2025 paper
  states that it reuses the TENO indicator of Huang & Fu (2024)
  unchanged (§3.1). Yet its Eq. (11) integrates the indicators of all
  three polynomials over the central cell $I_i$, while Huang & Fu (2024)
  integrate each polynomial over its own cell (their Eqs. (32)–(35)). For
  quadratics the first-derivative term differs between the two domains,
  so the two printed indicators are not the same *(compiler check, not in
  the sources)*. Which one the 2025 code uses is not stated. The 1D TENO
  candidate of Eq. (19) combines the full neighbour polynomials. Its
  integral over $I_i$ equals that of $p_i$ only if the neighbours'
  extrapolated averages equal $\bar u_i$, so the printed 1D formula is not
  conservative unless a mean shift is understood *(compiler check, not in
  the sources)*. The 2D Eqs. (27)–(29) recombine only the non-constant
  modes and keep the average. Neither the 2025 limiter nor the 2024 one
  is compared with the other.
- Huang & Fu weight the 2D indicators by powers of the cell area,
  $|I_{ij}|^{2k-1}$, where the 1D ones use $\Delta x^{2l-1}$ (Eqs. 41,
  59), and do not say whether the limiter acts on conserved or
  characteristic variables, nor whether the just-limited $u^{(1)}_i$
  enters the second-mode candidates.
- Maltsev et al.'s Eq. (5) gives the number of degrees of freedom as
  $\frac1{d!}\prod_{l=1}^d(N+l)$ and names it with the highest mode index
  $\mathcal K$, while it counts the $\mathcal K+1$ functions $k=0,\dots,\mathcal K$;
  the text calls the growth exponential, while the formula is a
  polynomial of degree $d$ in $N$ *(compiler check, not in the sources:
  $N=1$, $d=2$ gives 3, the functions $1,x,y$)*. Their
  printed Runge–Kutta stages add $+\Delta tM^{-1}R$ for a residual defined
  by $M\,dU/dt+R=0$.

- **Chen & Fu: gaps.** The Taylor formula of the averaged second
  derivatives used by the cubics $p_5$, $p_6$ and their characteristic
  projection are not printed (Eqs. (51), (71)); how the WENO4 weights
  combine three quadratics and four cubics is not stated, the selection
  rule of §5.7 relying on the TENO flags; the solution points of Eq. (3),
  called Gauss points, are Chebyshev–Gauss points ($0,\pm\sqrt3/4$ for
  $N_{\mathrm s}=3$, against $0,\pm\sqrt{15}/10$ for Gauss–Legendre on
  $[-\tfrac12,\tfrac12]$), and the printed linear weights belong to the
  printed points *(compiler check, not in the sources)*. The 4-DoF
  reconstruction needs a higher upper bound of $C_T$ than the 3-DoF one,
  which the authors set against "traditional scenarios" in which higher
  orders lead to reduced bounds; the reason given is the lower robustness
  of the 4-DoF reconstruction, from experiments not shown (§5.5).

# Citations

- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §1; §3 (Eqs. (3.1)–(3.9)); §4 (Exs. 4.1–4.10, Tables 4.1–4.18, Figs. 4.2–4.16); §5.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2, §2.6 (TVB minmod limiter), §3.1.5 (simple or Hermite WENO limiter for the two-phase Shu–Osher problem).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — arXiv v1: §7 (locally divergence-free WENO limiter).
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — arXiv v1: §8, Exs. 3–5 (Qiu–Shu WENO limiter).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §1 (critique of WENO/HWENO limiters).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — arXiv v1: §1 (troubled-cell limiters problem-dependent).
- [Mossier, Beck & Munz (2022)](/sources/mossier-2022.md) — §1 (WENO limiters named among alternatives).
- [Huang & Fu (2024)](/sources/huang-2024.md) — §4.4, Eqs. (36)–(50); §5.2, Eqs. (51)–(64); §6, Tables 1–4, Figs. 4–15.
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — arXiv v1: §3.1.3 (Hermite WENO limiter on first moments).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §2.1–2.4, Eqs. (2)–(34); §3.1, Table 1; §3.5–3.8; §4; Appendix B, Tables B.3–B.4.
- [Chen & Fu (2024)](/sources/chen-2024.md) — §1; §2, Eq. (3); §5.1–5.7, Eqs. (21)–(69); §6–7, Eqs. (70)–(75), Algorithm 1, Figs. 2–3; §9, Table 1, Figs. 5–25; §10.
- [Cao et al. (2026)](/sources/cao-2026.md) — §1; §2.1 (Property 2.1); §6, Figs. 1, 6, 8, 10, 11, 13.
- [Huang et al. (2025a)](/sources/huang-2025.md) — §1; §3.1 Eq. (11); §3.2–3.3 Eqs. (15)–(25); §4 Eqs. (26)–(36); §5 Tables 1–4, Figs. 1–8.
