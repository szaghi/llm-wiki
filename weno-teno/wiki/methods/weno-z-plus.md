---
type: Method
title: "WENO-Z+ and WENO-Z+M"
description: "WENO-Z+ adds to the WENO-Z weight a term proportional to (β_k+ε)/(τ_5+ε) that raises the weight of the less-smooth stencil; Luo & Wu's WENO-Z+M takes its square root and an adaptive coefficient, removing the negative dissipation that WENO-Z+ shows in its approximate dispersion relation."
status: established
aliases: [WENO-Z+, WENO-Z+M, WENO-ZP, WENO-P+, Acker–Borges–Costa WENO]
tags: [weno, reconstruction, low-dissipation, finite-difference]
timestamp: 2026-10-23T05:41:00Z
---

# WENO-Z+ and WENO-Z+M

WENO-Z+ (Acker, Borges and Costa, as recalled by Luo & Wu 2021, §2.3) modifies the fifth-order
[WENO-Z](/methods/weno-z.md) weights so that the stencil with the *largest* smoothness indicator
receives *more* than its linear weight $d_k$ in smooth regions. Let (page-local)
$z_k=(\tau_5+\epsilon)/(\beta_k+\epsilon)$ and let $\mu>0$ be a coefficient. Then

$$\alpha_k=d_k\Big[1+z_k^{\,q}+\mu\,z_k^{-1}\Big],\qquad q=2,$$

with $\tau_5=|\beta_0-\beta_2|$ (Luo & Wu 2021, Eq. (6)). The extra term grows with $\beta_k$, so it
favours the less-smooth stencil; it is proportional to $1/\tau_5$, so it becomes feeble at
discontinuities, where $\tau_5$ is large. Acker et al. chose $\mu=\Delta x^{2/3}$: with
$\Delta x^{1/2}$ the smooth waves of the Titarev–Toro problem were magnified, with $\Delta x$ they
were seriously attenuated (as recalled by Luo & Wu 2021, §2.3). Luo & Wu also recall that Acker et
al. proved the [ENO property](/definitions/eno-property.md) for $\mu=O(1)$.

## Motivation

Fu (2023, §2.3) recalls Acker et al.'s finding that raising the weights of the less-smooth
stencils "is considerably more important than maintaining the accuracy order at critical points",
and calls it consistent with the design of [TENO](/methods/targeted-eno.md). Luo & Wu (2021, §4)
give the mechanism they hold responsible. Let $S_D$ be the stencil with the largest $\beta_k$ and
$\omega_D$, $d_D$ its weights. The nonlinear weighting adds positive dissipation when
$\omega_D<d_D$ (every WENO-JS and WENO-Z weighting) and negative dissipation when $\omega_D>d_D$,
which partly cancels the linear dissipation of the underlying upwind scheme UD5. Weights of the
WENO-Z+ type can therefore have dispersion and dissipation errors *below* those of UD5 in a band of
wavenumbers ([numerical dissipation](/definitions/numerical-dissipation.md)). This is a heuristic
argument supported by plots of $\omega_k/d_k$ on Fourier modes (Figs. 5–7), not an analysis.

## The negative-dissipation defect

Luo & Wu (2021, §3.1, Fig. 1) compute the numerical
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md) of WENO-Z+ for
$\mu\in\{\Delta x^0,\Delta x^{1/2},\Delta x^{2/3},\Delta x\}$. For the larger $\mu$ the imaginary part
of the modified wavenumber is positive (anti-dissipation) in a narrow band around
$\vartheta\approx1.1834$, and there the dissipation recovers much more slowly with decreasing $\mu$
than elsewhere, so reducing $\mu$ "sacrifices the spectral properties in vain". The ADR curves of
WENO-Z+ cross those of UD5 at $\vartheta\approx1.3418$: better below, worse above (§4). On the
Titarev–Toro problem (1001 points) WENO-Z+ falsely amplifies the smooth waves ahead of and behind
the shock (§5.2.3, Fig. 11).

## WENO-Z+M (Luo & Wu 2021)

Two modifications (Eqs. (7)–(9)):

1. the extra term is weakened by a root, $z_k^{-1}\mapsto z_k^{-1/2}$ (the paper's exponent $1/q$
   with $q=2$), which by their ADR removes the negative dissipation once the exponent reaches 1/2;
   larger roots damage resolution;
2. the coefficient becomes adaptive, $\mu^{\mathrm M}=\mu\,\zeta$ with (page-local $\zeta$)
   $$\zeta=\frac{1+z_{\min}^2}{\sum_{k=0}^2d_k(1+z_k^2)},\qquad z_{\min}=\min_kz_k,$$
   i.e. the ratio of the WENO-Z ($q=2$) weight of the less-smooth stencil to its linear weight.
   Luo & Wu state, citing earlier analyses, that $\zeta\le1$, $\zeta=1+O(\Delta x^6)$ in smooth
   regions and $\zeta=O(\Delta x^4)$ plus an $\epsilon^2$ term at a discontinuity.

The final weight is $\alpha_k=d_k\big[1+z_k^2+\mu\,\zeta\,z_k^{-1/2}\big]$ with **constant**
$\mu=579$ and $\epsilon=10^{-40}$. The value 579 is the largest for which the interacting blast waves
problem ($N_x=401$) completes; 580 fails (§3.2, Fig. 13). With the root, increasing $\mu$
(Fig. 2: $\mu=1,25,600$) improves dispersion and dissipation monotonically without negative
dissipation. No theorem on order or ENO property is proved for WENO-Z+M.

**Evidence** (FD, global Lax–Friedrichs splitting, Roe-averaged characteristic decomposition,
TVD-RK3; Luo & Wu 2021, §5):

- 2-D smooth density wave (Table 1): at $641^2$, $L_1$ errors $0.3913\times10^{-13}$ (WENO-Z+M),
  $0.7896\times10^{-13}$ (WENO-Z and UD5), $0.1549\times10^{-12}$ (WENO-Z+); WENO-Z+M observed orders
  5.61, 5.46, 5.31, 5.16, 5.08, decreasing toward 5.
- Broadband advection with six points per shortest wavelength ($N_x=25$, $t=30$): WENO-Z+M resolves
  better than UD5, WENO-IS-I and WENO-Z9, while WENO-Z+ does not visibly improve on UD5 (Fig. 8).
- [Shu–Osher](/benchmarks/shu-osher-problem.md) (201 points): WENO-Z+ improves the high-frequency
  waves but not the shock, WENO-Z+M improves both (Fig. 10). Lax (101 points): markedly sharper
  shock and contact than WENO-Z/WENO-Z+ (Fig. 12).
- [Double Mach reflection](/benchmarks/double-mach-reflection.md) ($961\times241$, CFL 0.1),
  [forward-facing step](/benchmarks/forward-facing-step.md) ($481\times161$), 2-D Riemann
  configuration 3 and a viscous shock/shear-layer interaction: WENO-Z+M gives the best resolution
  of the schemes compared (Figs. 14–18).

Luo & Wu conclude (§6) that a well-designed nonlinear mechanism can improve resolution *beyond*
the underlying linear scheme, against the view, which they attribute to Pirozzoli, that
shock-capturing nonlinearities always degrade spectral properties.

## WENO-Z+ weights in a Lagrangian particle method

Jiang, Liu, Meng, Sun, Wei & Wang (2024, §3.2, Eqs. (11)–(15)) use the WENO-Z+ weights of Luo & Wu's paper, as they
attribute them, to give high-order left and right states to the pairwise Riemann problems of a Lagrangian
weighted-least-squares particle method for compressible multiphase flow. For a particle pair, six collinear points are
placed on the line through the two particles; the four that are not particles get values copied from, or extrapolated to
first order with the least-squares gradient of, the nearest particle. The midpoint states are then built from the
fifth-order candidates $\tfrac13u_{i-2}-\tfrac76u_{i-1}+\tfrac{11}6u_i$, $-\tfrac16u_{i-1}+\tfrac56u_i+\tfrac13u_{i+1}$,
$\tfrac13u_i+\tfrac56u_{i+1}-\tfrac16u_{i+2}$ of cell-average (finite-difference flux) reconstruction, applied to the point
values, with the Jiang–Shu indicators, linear weights $(\tfrac1{10},\tfrac35,\tfrac3{10})$ and

$$\alpha_k=d_k\big[1+z_k^2+\mu\,z_k^{-1}\big],\qquad z_k=\frac{\tau_5+10^{-10}}{\beta_k+10^{-10}},\qquad \mu=\lvert x_n-x_i\rvert^{2/3},$$

i.e. the Acker et al. form with $q=2$ and the pair distance $\lvert x_n-x_i\rvert$ (page-local: positions of the two
particles) in place of $\Delta x$ in $\mu=\Delta x^{2/3}$. Primitive variables $(\rho,v,p)$ are interpolated component by
component, without characteristic projection, and the states enter a Roe-type linearized Lagrangian Riemann solver
([Roe solver](/methods/roe-riemann-solver.md)). On smooth density waves with a "fixed particle distribution" the method converges at
orders 2.22–2.35, against about 2.0 without the reconstruction (Tables 1–2); the authors call it high-order. *(Compiler check, not in the sources:
these candidates and weights are exact for cell averages, $\bar u_j=u_j+\tfrac{\Delta x^2}{24}u''_j+O(\Delta x^4)$, so on point
values their linear combination returns $u(x_{i+1/2})-\tfrac{\Delta x^2}{24}u''(x_{i+1/2})+O(\Delta x^4)$, a second-order
midpoint value (for $u=x^2$, $\Delta x=1$: $\tfrac16$ against $\tfrac14$); the point-value weights would be
$(\tfrac1{16},\tfrac58,\tfrac5{16})$, as in Berta et al. on [WENO-Z](/methods/weno-z.md). The second-order least-squares
derivatives and the first-order extrapolation to the four auxiliary points also limit the rate; the observed 2.22–2.35 is
consistent with a second-order method.)* It is less dissipative than the
Riemann-solver-only variant on Rayleigh–Taylor, an [underwater explosion](/benchmarks/underwater-explosion.md) and the
collapse of a bubble near a wall, where only the reconstructed variant reproduces the micro-jet, at about five times the
cost, and less dissipative than earlier WENO-SPH and Riemann-solver SPH schemes on Sod tubes (figure comparisons) (§4–§5;
[bubble collapse near a wall](/benchmarks/bubble-collapse-near-wall.md)).

## Third-order analogue: WENO-P+

Deng (2023, Eq. (4.27)) recalls WENO-P+ of Xu & Wu, the compact third-order counterpart, with
$\alpha_k=d_k\big(1+\tau_P/(\beta_k+\epsilon)+s\,(\beta_k+\epsilon)/(\tau_P+\epsilon)\big)$ and
$\tau_P=\tfrac12(\beta_0+\beta_1)-\tfrac14(\bar u_{i-1}-\bar u_{i+1})^2$; Xu & Wu recommend
$s=\Delta x^{1/6}$, $s=\Delta x^{2/3}$ behaves like WENO-P and $s=\Delta x^0$ oscillates. On the
[normalised-variable diagram](/definitions/normalised-variable-diagram.md), WENO-P+ with $s=1$
leaves the convection-boundedness region, consistent with the oscillations reported for it, and
Deng calls the scheme "neither scale-invariant nor mesh-size-independent" because $s$ is tied to
$\Delta x$ (§4.4, Fig. 6; [scale invariance](/properties/scale-invariance.md)).

## Qualifications

- Jiang et al. (2024) use equispaced-grid linear weights on points whose values come from the nearest particle; the text
  does not state that the six points are equispaced. On a non-uniform particle distribution the paper calls the errors "the same order of magnitude"
  as on the uniform one. *(Compiler check, not in the sources: Tables 2b–2c give non-uniform to uniform $L_{\mathrm{RMS}}$ ratios of 1.8–3.6
  at $51^2$ and 3.1–6.2 at $101^2$ over the three smoothing lengths, and rates 1.48–1.53 on the non-uniform set.)*

- **Calibration.** $\mu=579$ is fixed on one problem at one resolution with a sharp 579/580
  threshold; robustness across grids and problems is not shown, and the switch from the
  $\Delta x$-scaled coefficient of Acker et al. to a constant is not discussed. Fig. 2 displays
  $\mu=600$, a value that already fails on the blast waves.
- **Coarse grids.** On the coarsest grid of Table 1 ($21^2$) WENO-Z+M has a larger $L_1$ error than
  WENO-Z and UD5 ($0.4060\times10^{-5}$ against $0.2613\times10^{-5}$); its advantage appears from
  $81^2$ on. No test with critical points is reported, although the accuracy statement is
  restricted to the case "when there are no critical points" (§5.3.1).
- **Smooth-region limit.** *(Compiler check, not in the sources.)* Away from critical points
  $\beta_k=O(\Delta x^2)$ and $\tau_5=O(\Delta x^5)$, so $\mu\zeta z_k^{-1/2}=O(\Delta x^{-3/2})$
  dominates $1+z_k^2$ as $\Delta x\to0$ and the weights tend to
  $d_k\sqrt{\beta_k}/\sum_ld_l\sqrt{\beta_l}$. Since the $\beta_k$ agree to relative
  $O(\Delta x^2)$, this gives $\omega_k-d_k=O(\Delta x^2)$, the weight rate required by the necessary condition
  recalled by Li et al. (2022b, Eq. (12)), but slower than WENO-Z. This is consistent with the
  fifth order and the halved error constant of Table 1; Luo & Wu's statement that $\zeta$ "has
  little effects" in smooth regions does not address it.
- Deng (2023, abstract) says "the improved WENO-Z scheme is neither scale-invariant nor
  mesh-size-independent"; the body (§4.4) states this of WENO-P+, the third-order analogue of
  WENO-Z+.
- **Two-dimensional problems.** Liang, Xiao, Shyy & Fu (2022, §1) state that the performance of WENO-Z+
  "degenerates to that of WENO-Z for two-dimensional complex problems containing multiscale structures,
  such as the double Mach reflection problem"; the paper runs no WENO-Z+ test. In Luo & Wu's double Mach
  comparison (Fig. 14) the best resolution is that of the modified WENO-Z+M
  ([double Mach reflection](/benchmarks/double-mach-reflection.md)).

# Citations

- [Luo & Wu (2021)](/sources/luo-2021-b.md) — §2.3, Eq. (6); §3, Eqs. (7)–(9), Figs. 1–3, 13; §4, Figs. 4–7; §5, Table 1, Figs. 8–18; §6.
- [Deng (2023)](/sources/deng-2023.md) — §4.4, Eq. (4.27), Fig. 6.
- [Fu (2023)](/sources/fu-2023.md) — §2.3.
- [Li et al. (2022b)](/sources/li-2022-b.md) — Eq. (12) (optimal-order condition recalled).
- [Liang et al. (2022)](/sources/liang-2022.md) — §1.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §3.2, Eqs. (11)–(15); §4.1, Tables 1–2; §5.
