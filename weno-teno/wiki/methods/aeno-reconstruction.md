---
type: Method
title: "AENO and AENO-C reconstruction"
description: "AENO averages, coefficient by coefficient, the Taylor coefficients of two candidate polynomials of one degree through a joining function of their magnitude ratio; AENO-C pairs the ENO polynomial with the centred one and uses a symmetric exponential joining function, giving design order to 10 in ADER finite volumes at two-stencil cost."
status: established
aliases: [AENO, average ENO, AENO-C, AENO-Centred, joining function, ADER-AENO, ADER-AENO-C]
tags: [reconstruction, finite-volume, limiting, low-dissipation]
timestamp: 2026-10-23T15:16:00Z
---

# AENO and AENO-C reconstruction

**AENO** ("average ENO", Toro et al. 2021, as recalled by
[Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md), §2.3) is a one-dimensional
nonlinear polynomial reconstruction for finite-volume schemes. On cell $I_i$ it builds two
candidate polynomials of the same degree $m$ (page-local; each fitted to the averages of
$m+1$ consecutive cells, $r=m+1$ in registry terms) and averages them **coefficient by
coefficient**: each Taylor coefficient about $x_i$ is a nonlinear convex-type combination of
the two candidates' coefficients, with a weight given by a **joining function** of the ratio
of their magnitudes. The constant coefficient is fixed afterwards by conservation of the
cell average. **AENO-C** ("AENO-Centred", Yajaman et al. 2025, §§3–4) changes the pair of
candidates (the degree-$m$ [ENO](/definitions/eno-property.md) polynomial and the centred
one) and the joining function. Both are designed as the reconstruction step of
[ADER](/methods/ader-scheme.md) finite-volume schemes, where the reconstructed polynomial
is the data of a [generalized Riemann problem](/methods/generalized-riemann-problem.md).

## Stencils

Yajaman et al. (§2.1, Eqs. (21)–(28)) recall the ENO selection: on the extended stencil
$\{I_{i-m},\dots,I_{i+m}\}$ of $2m+1$ cells, the candidate stencils are the $m+1$ runs of
$m+1$ consecutive cells, and the ENO stencil is chosen level by level by comparing the
magnitudes of divided differences of the cell averages. The ENO polynomial is computed
directly from the cell-average conditions on its stencil ("direct ENO", without the
primitive function). The two reconstructions then take two candidates:

- **AENO** (Eqs. (35)–(36)): the two degree-$m$ stencils that contain the degree-$(m-1)$
  ENO stencil. For $m=1$ they are $\{I_{i-1},I_i\}$ and $\{I_i,I_{i+1}\}$; for $m=2$,
  $\{I_{i-2},I_{i-1},I_i\}$ and $\{I_{i-1},I_i,I_{i+1}\}$ if
  $\lvert\bar u_i-\bar u_{i-1}\rvert<\lvert\bar u_{i+1}-\bar u_i\rvert$, else
  $\{I_{i-1},I_i,I_{i+1}\}$ and $\{I_i,I_{i+1},I_{i+2}\}$.
- **AENO-C** (Eqs. (47)–(53)): the degree-$m$ ENO stencil and the **centred** stencil
  $\{I_{i-m/2},\dots,I_{i+m/2}\}$ for even $m$; for odd $m$ there are two almost-centred
  stencils, and the one closer to the ENO stencil is taken. Three special cases keep two
  distinct candidates: for $m=1$ both stencils are averaged as in AENO; for even $m$ with the
  ENO stencil equal to the centred one, the AENO pair is used; for odd $m$ with the ENO
  stencil equal to one almost-centred stencil, the two almost-centred stencils are averaged.
  The first candidate is always the ENO stencil.

For $m=4$ with the ENO stencil $\{I_{i-4},\dots,I_i\}$, AENO averages it with
$\{I_{i-3},\dots,I_{i+1}\}$, AENO-C with the centred $\{I_{i-2},\dots,I_{i+2}\}$, and
[WENO-JS](/methods/weno-js-reconstruction.md) combines all five (Fig. 7). The rationale for the centred partner is that on smooth data the centred
polynomial is "the most faithful" reconstruction within the cell (§4).

## Coefficient-wise averaging

Write the two candidates in Taylor form about $x_i$,
$p_{\mathrm L}(x)=\sum_{k=0}^m\mathsf c^{\mathrm L}_k(x-x_i)^k$ and
$p_{\mathrm R}(x)=\sum_{k=0}^m\mathsf c^{\mathrm R}_k(x-x_i)^k$ (page-local symbols; for AENO-C,
L is the ENO and R the centred polynomial). The reconstruction is
$p(x)=\sum_k\tilde{\mathsf c}_k(x-x_i)^k$ with (Eqs. (39), (53))

$$\tilde{\mathsf c}_k=\tfrac12\big(1+\mathcal J(\mathsf s_k)\big)\mathsf c^{\mathrm L}_k+\tfrac12\big(1-\mathcal J(\mathsf s_k)\big)\mathsf c^{\mathrm R}_k,\qquad
\mathsf s_k=\frac{\lvert\mathsf c^{\mathrm L}_k\rvert}{\lvert\mathsf c^{\mathrm R}_k\rvert},\qquad k\ge1,$$

where $\mathcal J$ is the joining function (page-local; the source writes $\omega(s)$, which is
not a WENO weight). In AENO the ratio carries a guard,
$\mathsf s_k=\lvert\mathsf c^{\mathrm L}_k\rvert/(\lvert\mathsf c^{\mathrm R}_k\rvert+10^{-6})$
(Eq. (41)); AENO-C prints none. The constant term restores the cell average (Eq. (42)),

$$\tilde{\mathsf c}_0=\bar u_i-\frac1{\Delta x}\sum_{k=1}^m\int_{x_{i-1/2}}^{x_{i+1/2}}\tilde{\mathsf c}_k(x-x_i)^k\,dx .$$

When the two magnitudes differ strongly, $\mathcal J\to\pm1$ and the averaged coefficient is
close to the smaller one, a minmod-like ENO choice made coefficient by coefficient (§2.3). The
result is one closed-form polynomial, evaluable anywhere in the cell; Yajaman et al. (§7.1)
name this as an advantage over WENO for the space–time Gauss quadrature of ADER source
terms, because WENO linear weights at generic Gauss points are "non-trivial".

## The joining function

The AENO joining function of Toro et al. is (Eq. (40); $\epsilon_{\mathrm J}$ page-local,
$\epsilon_{\mathrm J}^2=0.5$ in Toro et al.)

$$\mathcal J(\mathsf s)=\frac{1-\mathsf s}{\sqrt{\epsilon_{\mathrm J}^2+(1-\mathsf s)^2}} .$$

Yajaman et al. (§3, Eqs. (43)–(45)) find two defects. First, $\mathcal J(0)<1$ for every
$\epsilon_{\mathrm J}>0$: when $\mathsf c^{\mathrm L}_k=0$ and $\mathsf c^{\mathrm R}_k\ne0$
the right coefficient always keeps some weight, "an unintended bias". Second, the average
should not depend on which candidate is labelled left: swapping the labels replaces
$\mathsf s$ by $1/\mathsf s$, and the average is label-independent iff
$\mathcal J(1/\mathsf s)=-\mathcal J(\mathsf s)$, which the function above does not satisfy.
They replace it by the family (Eq. (46))

$$\mathcal J(\mathsf s)=e^{-\mathsf s^{\mathsf p}}-e^{-1/\mathsf s^{\mathsf p}},\qquad\mathsf p>0,$$

with $\mathcal J(1/\mathsf s)=-\mathcal J(\mathsf s)$, $\mathcal J(0)=1$, $\mathcal J(1)=0$ and
$\mathcal J\to-1$ as $\mathsf s\to\infty$ (page-local exponent $\mathsf p$, not the pressure).
*(Compiler check, not in the sources: substituting $1/\mathsf s$ in Eq. (46) exchanges the two
exponentials; in Eq. (40) it gives $(\mathsf s-1)/\sqrt{\epsilon_{\mathrm J}^2\mathsf s^2+(\mathsf s-1)^2}$,
which equals $-\mathcal J(\mathsf s)$ only for $\epsilon_{\mathrm J}=0$, and
$\mathcal J(0)=1/\sqrt{1+\epsilon_{\mathrm J}^2}$.)* Larger $\mathsf p$ makes $\mathcal J$
step-like; decreasing $\mathsf p$ plays the role of increasing $\epsilon_{\mathrm J}$, and
$\mathsf p=2$ is "a good approximation" of Eq. (40) with $\epsilon_{\mathrm J}^2=0.5$ on
inspection of the curves (§3, §5.1, Fig. 6). $\mathsf p=2$ is used throughout: squaring is
cheaper than a general power, $\mathsf p=1$ produced negative densities or pressures on the
left half of the Woodward–Colella problem, and the authors call $\mathsf p=2$ "an excellent
compromise" on all their experiments while giving no theoretical justification (§5.2). They
warn that $\mathsf s^{\mathsf p}$ can overflow in floating point (§3).

Inside plain AENO, the new function with $\mathsf p=2$ instead of Eq. (40) reduces numerical
diffusion and improves the symmetry of a square wave advected to $t=2000$ on 100 cells at
orders 7–10 (§5.1, Fig. 8).

## Accuracy, robustness and cost

All tests use ADER finite-volume schemes with the Toro–Titarev generalized-Riemann-problem
solver of orders 2 to 10, and compare ENO, Jiang–Shu WENO (exponent 2), AENO
($\epsilon_{\mathrm J}^2=0.5$) and AENO-C ($\mathsf p=2$) (§§5–8). Jiang–Shu WENO is used
instead of the Dumbser–Käser WENO common in ADER codes because, in the authors' experience,
the latter "degrades beyond the sixth-order" (§2.2; stated, not shown).

- **Smooth advection** ($\sin^4(\pi x)$ on $[-1,1]$, CFL 0.9, $t=4$; Tables 1–2, A.6–A.8).
  AENO misses the design order at orders 4 and 5 and loses convergence on the finest mesh at
  order 5 ($L_1$ order $-0.63$ from 200 to 400 cells). AENO-C reaches the design order in
  $L_1$ and $L_2$ at every order from 2 to 10 except order 4, where it is still below
  ($L_1$ order 2.78 at 400 cells). Purely in rates, AENO-C beats ENO and AENO and is beaten
  only by WENO, whose degree-$m$ polynomial has spatial accuracy $2m+1$ (§6); WENO is
  superconvergent on coarse meshes, e.g. $L_1$ order 14.13 from 32 to 64 cells at order 10
  (Table A.7).
- **Efficiency** (CPU time to $L_1=10^{-8}$). On advection at $t=100$ AENO-C is the most
  efficient of the four at all orders except 3 and 4, where WENO is (§6, Fig. 10). On the
  Euler [density wave](/benchmarks/density-wave-advection.md) at $t=10$ AENO-C is better than
  AENO at every order and almost as efficient as WENO up to order 7, less efficient beyond
  (§7.2, Fig. 13). The profile on 200 cells to $t=5$ (serial, one CPU) attributes the loss to
  the Cauchy–Kovalevskaya procedure of the solver, 37 %, 59.6 %, 74.1 % and 85.2 % of the
  AENO-C run time at orders 7–10, against below 7 % for the reconstruction at order 10; the
  order-10 AENO-C reconstruction (4.36 s) is faster than the order-7 WENO one (16.02 s)
  (§8, Table 5).
- **Long-time advection of discontinuities.** On the Jiang–Shu composite profile
  ([Jiang–Shu composite advection](/benchmarks/jiang-shu-composite-advection.md)) advected for
  1000 periods on 200 cells (222,223 steps), AENO-C keeps the four waves without overshoots at
  orders 5–10, while WENO shows spurious oscillations near discontinuities and steep gradients
  (§6, Fig. 11).
- **Euler shocks.** On the left half of the
  [Woodward–Colella problem](/benchmarks/woodward-colella-blast-wave.md) (pressure ratio
  $10^5$, 200 cells, $t=0.012$) WENO oscillates at the contact at orders 5–6 and crashes with
  negative pressures or densities at orders 7–10 for every CFL number tried between 0.2 and
  0.9, while AENO-C shows no visible oscillation; at sixth order AENO-C is nearly twice as
  efficient as WENO to $L_1=0.01$ (§7.2, Figs. 15–16). The full two-blast problem gives
  negative pressures for all high-order schemes tested, AENO-C included, near the shock
  collision. On a modified Sod problem with a sonic rarefaction AENO oscillates near the
  rarefaction tail at orders 7–10 and AENO-C does not; at orders 9 and 10 the tail is
  "slightly disconnected" unless the CFL number is lowered to about 0.75–0.8 (Fig. 14;
  [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)). The Toro–Titarev
  variant of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md) on 1000 cells
  approaches the reference as the order rises (Figs. 17–18).
- **Balance laws.** With source terms (Burgers with $\beta u^2$ and an accelerating-shock
  problem with $e^{-u}$), ADER-AENO-C reaches the expected order essentially at all orders
  2–10 (§7.1, Table 3, Fig. 12; [Burgers tests](/benchmarks/burgers-equation-tests.md)).

The cost per reconstruction is that of two stencils, comparable to ENO and AENO, against
$m+1$ for WENO (abstract, §9).

## Place among reconstructions

AENO and AENO-C sit between ENO, which takes one stencil, and WENO, which blends all $m+1$
candidates through [smoothness indicators](/definitions/smoothness-indicator.md): they blend
two candidates, without indicators, through the coefficient magnitudes. For WENO,
Yajaman et al. give a spatial accuracy of $2m+1$ for the degree-$m$ reconstruction (§6).
Yajaman et al. mention mENO, TENO, CENO
and ENO-ET only as other reconstructions, and [MOOD](/methods/mood-a-posteriori-limiting.md)
in the conclusions (§§2, 9).

## Qualifications

- **One dimension only.** The tests are 1-D; a dimension-by-dimension extension on Cartesian
  meshes is said to be possible, and the extension of the stencil choice to unstructured
  meshes "non-trivial and unclear" (§9).
- **Undershoots.** AENO-C shows occasional undershoots near discontinuities at order 6
  (Figs. 9, 11), absent with AENO, which the authors attribute to retaining too much
  centred-stencil information; they shrink under refinement, and a WENO-type average of the
  two stencils with smoothness indicators is suggested, not tested (§5.2, §9).
- **Order 4.** AENO-C stays sub-optimal at order 4 on the smooth advection and Euler
  tests (Tables 2, 4); the paper gives no explanation.
- **Text against tables.** §6 calls AENO "quite satisfactory" from sixth to tenth order, while
  its Table A.8 shows divergence on the finest mesh at orders 6 and 7 ($L_1$ orders $-3.25$ and
  $-0.25$ from 200 to 400 cells). §6 makes WENO the most efficient at orders 3 and 4, §7.2
  recalls the same advection result as "all orders except the fourth-order". §7.2 places the
  efficiency loss on Euler "beyond the seventh-order", §8 "above the eighth-order".
- **Printed slips.** §2.2 calls the full-stencil polynomial of WENO "of degree $2m+1$"; the
  $2m+1$ cells of the extended stencil determine degree $2m$, consistent with the spatial
  accuracy $2m+1$ that §6 states. Eq. (42) prints the cell average as $\bar q_j$ and the upper
  summation limit as $n$ for cell $i$ and degree $m$.
- **Priority claim.** The authors state that this is, to their knowledge, the first study of
  the Euler equations with nonlinear ADER schemes of order 8 or higher (§9).
- The efficiency figures come from one serial 1-D code on unspecified hardware.

# Citations

- [Yajaman, Toro & Demattè (2025)](/sources/yajaman-2025.md) — §2.1–2.3, Eqs. (21)–(42); §3, Eqs. (43)–(46), Fig. 6; §4, Eqs. (47)–(53), Fig. 7; §5, Figs. 8–9; §6, Tables 1–2, Figs. 10–11; §7, Tables 3–4, Figs. 12–18; §8, Table 5; §9; App. A, Tables A.6–A.8.
