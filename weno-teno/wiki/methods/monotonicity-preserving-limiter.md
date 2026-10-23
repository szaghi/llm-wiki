---
type: Method
title: "Monotonicity-preserving (MP) limiter"
description: "The Suresh–Huynh monotonicity-preserving limiter keeps a high-order interface value unless it leaves a monotonicity bound and otherwise clips it into an interval built from median, upper-limit and large-curvature values; the page records its form in the gradient-based MEG/MIG schemes, the gradient-based curvature that replaces the three-point one, and MP3/MP5 convergence in a relativistic code."
status: established
aliases: [MP limiter, MP5, MP3, MP reconstruction, Suresh–Huynh limiter, monotonicity-preserving scheme, monotonicity-preserving reconstruction, improved MP5 limiter, pointwise MP5]
tags: [limiting, reconstruction, finite-difference, finite-volume, relativistic, mhd]
timestamp: 2026-10-23T23:30:00Z
---

# Monotonicity-preserving (MP) limiter

The **monotonicity-preserving limiter** of Suresh & Huynh (1997), as recalled and used by Chamarthi
(2023a, §3.3, Eqs. (53)–(61)), Chamarthi (2023b, §2.3, Eqs. (25)–(27)) and Chandravamsi et al. (2023,
App. E, Eqs. (E.1)–(E.4)), post-processes a high-order interface value $u^{\mathrm{lin}}_{i+1/2}$
(page-local: the unlimited left state from cell $i$, e.g. a
[gradient-based reconstruction](/methods/gradient-based-reconstruction.md)) in two stages: a cheap test
that accepts the value whenever it lies within a monotonicity bound, and otherwise a clipping into an
interval $[u^{\min},u^{\max}]$ wide enough to keep smooth extrema. López-Miralles, Martí & Perucho (2023,
§3.2) use the same family, MP3 and MP5, as a reconstruction of a finite-volume relativistic MHD code.
The right state $u^+_{i+1/2}$ follows by mirror symmetry.

## The limiter

With $\mathrm{minmod}(a,b)=\tfrac12(\mathrm{sgn}\,a+\mathrm{sgn}\,b)\min(|a|,|b|)$ (page-local $a$, $b$),
with the multi-argument form zero unless all arguments share one sign and otherwise the argument of least modulus (the sources print only the two-argument form), and a page-local constant $\xi_{\mathrm{MP}}>1$:

1. **Test.** Keep $u^{\mathrm{lin}}_{i+1/2}$ if
   $$\big(u^{\mathrm{lin}}_{i+1/2}-u_i\big)\big(u^{\mathrm{lin}}_{i+1/2}-u^{\mathrm{MP}}\big)\le\varepsilon_{\mathrm{MP}},\qquad
   u^{\mathrm{MP}}=u_i+\mathrm{minmod}\big(u_{i+1}-u_i,\ \xi_{\mathrm{MP}}(u_i-u_{i-1})\big),$$
   with the round-off threshold $\varepsilon_{\mathrm{MP}}$ (page-local) $10^{-20}$ (Chamarthi 2023a, Eq. (54);
   Chandravamsi et al. 2023, Eq. (E.1)) or $10^{-40}$ (Chamarthi 2023b, Eq. (25)).
2. **Curvatures.** A curvature $d_i$ at each node and a limited curvature at the interfaces,
   $d^{\mathrm M}_{i+1/2}=\mathrm{minmod}(4d_i-d_{i+1},4d_{i+1}-d_i,d_i,d_{i+1})$ in the base form
   (Chamarthi 2023a, Eq. (57)) or $\mathrm{minmod}(d_i,d_{i+1})$ (Eq. (61), "one of the two options in
   Suresh–Huynh").
3. **Bounds.** The median, upper-limit and large-curvature values
   $$u^{\mathrm{MD}}=\tfrac12(u_i+u_{i+1})-\tfrac12d^{\mathrm M}_{i+1/2},\qquad
   u^{\mathrm{UL}}=u_i+\xi_{\mathrm{MP}}(u_i-u_{i-1}),\qquad
   u^{\mathrm{LC}}=\tfrac12(3u_i-u_{i-1})+\tfrac43d^{\mathrm M}_{i-1/2},$$
   $$u^{\min}=\max\big[\min(u_i,u_{i+1},u^{\mathrm{MD}}),\min(u_i,u^{\mathrm{UL}},u^{\mathrm{LC}})\big],\quad
   u^{\max}=\min\big[\max(u_i,u_{i+1},u^{\mathrm{MD}}),\max(u_i,u^{\mathrm{UL}},u^{\mathrm{LC}})\big].$$
4. **Clip.** $u^-_{i+1/2}=u^{\mathrm{lin}}_{i+1/2}+\mathrm{minmod}\big(u^{\min}-u^{\mathrm{lin}}_{i+1/2},\ u^{\max}-u^{\mathrm{lin}}_{i+1/2}\big)$,
   which moves the value to the nearer end of $[u^{\min},u^{\max}]$ when it lies outside.

All three Chamarthi-group sources apply it in local characteristic variables
([characteristic decomposition](/methods/characteristic-decomposition.md)), the cell values and the
gradients projected with the same matrix (Chamarthi 2023a, §3.3; Chamarthi 2023b, §2.3; Chandravamsi et
al. 2023, §5.1, Step 4).

## Curvature from the shared gradients

The base limiter uses the three-point curvature $d_i=u_{i-1}-2u_i+u_{i+1}$ (Chamarthi 2023a, Eq. (56)).
In the gradient-based schemes the high-order second derivative is already available, and Chamarthi
(2023a, Eq. (60)) replaces it:

$$d_i=2(u_{i+1}-2u_i+u_{i-1})-\tfrac{\Delta x}{2}\big(u'_{i+1}-u'_{i-1}\big)=\Delta x^2u''_i ,$$

($u'$, $u''$ the cell-centre derivatives of the gradient-based page), together with the two-argument
$d^{\mathrm M}$. Chamarthi (2023b, Eq. (27)) and Chandravamsi et al. (2023, Eq. (E.3)) keep this form for
MEG7 and for the "improved MP5 limiter" of MEG6 and MIG4. *(Compiler check, not in the sources: for
smooth data both curvatures equal $\Delta x^2\partial_x^2u+O(\Delta x^4)$; the gradient-based one is
exact on polynomials up to degree 5 when $u'$ is exact, the three-point one up to degree 3.)* The effect, measured by
comparing MIG4 with "MIG4-base" (Eqs. (56)–(57)): better dispersion in the
[approximate dispersion relation](/definitions/approximate-dispersion-relation.md), "marginal" for MEG6
(Fig. 3), better density peaks in the 2-D shock–entropy wave and more vortical structure in a
[2-D Riemann problem](/benchmarks/two-dimensional-riemann-problems.md) (Chamarthi 2023a, Exs. 4.6–4.7,
Figs. 9–10).

**Value of $\xi_{\mathrm{MP}}$.** Chamarthi (2023b, Eqs. (26)–(27)) uses one constant, $\xi=7$ "as in
[28]", in both $u^{\mathrm{MP}}$ and $u^{\mathrm{UL}}$. Chamarthi (2023a) writes $\beta=7$ in
$u^{\mathrm{MP}}$ (Eq. (55)) and an $\alpha$ in $u^{\mathrm{UL}}$ whose value is not stated (Eq. (58));
Chandravamsi et al. (2023, App. E) give neither value.

## Uses and evidence

- **Gradient-based finite differences.** MP limiting of the fourth-order GBR state gives MEG6 and MIG4,
  and of the seventh-order state MEG7 ([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)).
  Against TENO5 the MP-limited MIG4 is less oscillatory on double Mach reflection, the 2-D
  shock–entropy wave and Leblanc, and resolves more roll-ups (Chamarthi 2023a, §4). Chandravamsi et
  al. (2023, §5.1, Step 4) state, citing earlier work, that MP5 captures shocks and acoustic waves
  together better than WENO strategies, and run implicit LES of a screeching jet with the MP-limited
  schemes as the only dissipation (§8.3). Chamarthi (2023a, §1) recalls that MP is less dissipative than
  WENO with better convergence (Li & Jaberi) and that MP5 is the most efficient fifth-order scheme
  (Zhao et al.).
- **Reference solutions.** MP5 provides the fine-grid references of the 2-D shock–entropy wave
  ($1600\times320$; Chamarthi 2023a, Ex. 4.6) and of the [Shu–Osher problem](/benchmarks/shu-osher-problem.md)
  (2000 points; Chamarthi 2023b, Ex. 3.5).
- **Relativistic MHD.** López-Miralles et al. (2023, §3.2, §4.1.1, Tables 1–4) add MP3 and MP5 to a
  finite-volume RMHD code, on primitive variables, with a fallback to first order when the
  reconstruction gives $|v|^2>1$. On the
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md) ($L_1$ error of
  $v_3$ after one period):
  - MP3 with SSP-RK3 is third order, HLLD 2.998231 and the polynomial-viscosity-matrix solver PVM-int-8
    2.998835 at the finest pair ([PVM solver](/methods/polynomial-viscosity-matrix-solver.md));
  - MP5 with RK3 stays third order (HLLD 3.005290), limited by the time integrator, with errors about two
    orders of magnitude lower ($4.284\times10^{-9}$ against $3.224\times10^{-7}$ for MP3 at $N=512$);
  - MP5 with a five-step fourth-order SSP-RK reaches 4.827224–5.046792 and $9.006\times10^{-12}$ at
    $N=512$ (Table 3) ([SSP Runge–Kutta](/methods/ssp-runge-kutta.md)).

  The authors state that the earlier code was tested only to second order. MP reconstruction is
  restricted there to non-radiative problems; radiative runs use piecewise-linear reconstruction (§3.2).
- **Pointwise MP5 in a fourth-order finite-volume scheme.** Berta, Mignone, Bugli & Mattia (2024, §3.2, Eq. (23); arXiv
  v4 read) apply MP5 to **point values** inside a finite-volume scheme for classical and relativistic MHD: the cell
  averages are first converted to fourth-order point values at cell centres by a Laplacian correction, then to primitive
  variables, and the unlimited interface value is the five-point point-value interpolation
  $$u^{\mathrm{lin}}_{i+1/2}=\tfrac1{128}\big(3u_{i-2}-20u_{i-1}+90u_i+60u_{i+1}-5u_{i+2}\big),$$
  the finite-difference form, instead of the reconstruction from cell averages. The limiting step is unchanged, "as
  monotonicity-preserving bounds are equally well expressed in terms of point values", and the authors claim the
  first use of pointwise MP5 and WENO-Z in a finite-volume scheme (§1, §3.2; [WENO-Z](/methods/weno-z.md)). With
  SSPRK(5,4) the scheme is fourth order: on the 2-D and 3-D
  [circularly polarized Alfvén wave](/benchmarks/circularly-polarized-alfven-wave.md) the MP5 and WENO-Z errors are
  "almost identical" and the $L_1$ orders reach 4.00 at $N_x=512$ (Table 2), and on the
  [magnetized vortex](/benchmarks/magnetized-vortex.md) the finest $L_1$ errors of $B_x$ are $5.76\times10^{-9}$ for both
  reconstructions (Table 1). In [field-loop advection](/benchmarks/field-loop-advection.md) MP5 shows small overshoots
  at the tail and undershoots at the head of the loop, while WENO-Z "performs the best" (§5.4, Figs. 6–7); MP5 with
  HLLD resolves a central magnetic island in the [Orszag–Tang vortex](/benchmarks/orszag-tang-vortex.md) at $64^2$
  (§5.6), and MP5 in primitive variables is the reconstruction of their relativistic rotated shock tube (§5.1).
  Robustness rests on an a priori order reduction that switches flagged cells to WENO3 or piecewise-linear
  reconstruction ([troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Qualifications

- López-Miralles et al. do not discuss why MP5 with a fourth-order Runge–Kutta method shows fifth-order
  rates at CFL 0.3; the rates are those of the grids shown.
- Chamarthi (2023a) uses $\alpha$ for the damping coefficient, the $u^{\mathrm{UL}}$ constant and the
  volume fraction, and $\beta$ for the compact coefficient, the MP constant and the vortex strength;
  Chamarthi (2023b) reuses $\xi$ for the MP constant and the detector constant $10^{-3}$, and prints a
  hat on $\hat\Phi_{j-1}$ in $\Phi^{\mathrm{LC}}$ that is defined nowhere, as is the hat on $\hat W$ in
  Chandravamsi et al. (App. E).
- None of the sources proves a monotonicity or bound property of the limited GBR schemes; the
  evidence is numerical.

# Citations

- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — §1; §3.3, Eqs. (53)–(64), Fig. 3; §4, Exs. 4.6–4.7, Figs. 9–10.
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — §2.3, Eqs. (25)–(27); Ex. 3.5.
- [Chandravamsi et al. (2023)](/sources/chandravamsi-2023.md) — §5.1, Step 4; §8.3; App. E, Eqs. (E.1)–(E.4).
- [López-Miralles, Martí & Perucho (2023)](/sources/lopezmiralles-2023.md) — §3.2; §4.1.1, Tables 1–4; §5.
- [Berta et al. (2024)](/sources/berta-2024.md) — §1; §3.1–3.2, Eq. (23); §5.1–5.4, §5.6, Tables 1–2, Figs. 6–7 (arXiv v4).
