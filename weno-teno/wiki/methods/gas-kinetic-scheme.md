---
type: Method
title: "Gas-kinetic schemes"
description: "Gas-kinetic schemes take the interface flux, and its time derivative, from moments of a BGK solution instead of a Riemann solver; the bundle's sources build a compact high-order scheme on it that evolves cell-averaged gradients with a nonlinearly limited two-stage fourth-order step, and a discrete-velocity variant that couples convective and viscous fluxes on unstructured grids."
status: established
aliases: [GKS, BGK scheme, gas-kinetic flux solver, compact gas-kinetic scheme, compact GKS, discrete gas-kinetic flux solver, DGKFS, direct modeling]
tags: [numerical-flux, finite-volume, compact-scheme, weno]
timestamp: 2026-10-23T23:00:00Z
---

# Gas-kinetic schemes

A **gas-kinetic scheme** (GKS) is a finite-volume scheme for the Euler or Navier–Stokes
equations whose interface flux is a moment of a gas distribution function evolved by the BGK
model across the interface, not the solution of a Riemann problem. Because the evolved
distribution depends on time, the scheme delivers a time-dependent interface flux $\hat f(t)$ and its time
derivative, and, for viscous flow, the inviscid and viscous fluxes together
([Zhao et al. (2023)](/sources/zhao-2023.md), §3.1;
[Liu et al. (2023b)](/sources/liu-2023-b.md), §1, §3.1.2). Below $\mathsf f$ is the distribution
function, $\mathsf g$ the Maxwellian, $\tau_{\mathrm c}$ the collision time and $\mathsf v$ the
particle velocity (all page-local, to keep $f$ for the flux and $\tau$ for the WENO-Z
indicator).

## The BGK evolution model

As recalled by Zhao et al. (§3.1, Eqs. (5)–(13), after Bhatnagar–Gross–Krook and Xu), the
distribution obeys

$$\partial_t\mathsf f+\mathsf v\cdot\nabla\mathsf f=\frac{\mathsf g-\mathsf f}{\tau_{\mathrm c}},$$

with $\mathsf g$ the Maxwellian of the local density, velocity and temperature, the internal
degrees of freedom $K_{\mathrm i}=(4-2\gamma)/(\gamma-1)$ in 2D (page-local), and the
compatibility condition that the collision term has zero moments against the collision
invariants $\varphi_{\mathrm c}=\big(1,\mathsf v,\tfrac12(\lvert\mathsf v\rvert^2+\text{internal})\big)$
(page-local). The conserved variables and fluxes are moments,
$u=\int\mathsf f\varphi_{\mathrm c}$, $f=\int\mathsf v\,\mathsf f\varphi_{\mathrm c}$. At an interface the
integral solution

$$\mathsf f(x_0,t,\mathsf v)=\frac1{\tau_{\mathrm c}}\int_0^t\mathsf g\big(x',t',\mathsf v\big)e^{-(t-t')/\tau_{\mathrm c}}dt'+e^{-t/\tau_{\mathrm c}}\mathsf f_0\big(x_0-\mathsf vt,\mathsf v\big)$$

blends a Chapman–Enskog-type equilibrium part, built from the reconstructed data on both
sides, with the upwinded initial non-equilibrium distribution; the second-order GKS
distribution is written out in Eq. (13), and a third-order evolution model exists. In the
tests the collision time is $\tau_{\mathrm c}=0.05\,\Delta t+5\big\lvert\frac{p^--p^+}{p^-+p^+}\big\rvert\Delta t$ for
inviscid and $\tau_{\mathrm c}=\mu/p+5\big\lvert\frac{p^--p^+}{p^-+p^+}\big\rvert\Delta t$ for viscous flow
(§4): the pressure-jump term is the scheme's control of
[numerical dissipation](/definitions/numerical-dissipation.md).

## Compact high-order GKS

[Zhao et al. (2023)](/sources/zhao-2023.md) (arXiv v1 of the 2023 paper) argue, under the name
**direct modeling**, that an explicit scheme is physically consistent only if it is
*compact*: nearest-neighbour stencils under a CFL number of order one, so that numerical and
physical domains of dependence agree (Abstract, §2). A compact scheme of order $\ge3$ must then
evolve subcell data beyond cell averages; theirs are the cell-averaged gradients, updated by
Gauss–Green from interface values at $t^{n+1}$,

$$\lvert I_i\rvert\,(\nabla u)^{n+1}_i=\oint_{\partial I_i}u(t^{n+1})\,n\,dS\qquad(\text{Eq. (2)}),$$

with the interface values taken from the same distribution function that gives the flux
(Eq. (15)). The ingredients added in this paper:

1. **Two interface states** (§3.2, Eq. (17)). Instead of the single equilibrium value
   $u^{\mathrm e}$ of their earlier compact schemes, the left and right values at $t^{n+1}$ are
   $u^\pm=(1-e^{-\Delta t/\tau_{\mathrm c,0}})\,u^{\mathrm e}+e^{-\Delta t/\tau_{\mathrm c,0}}\,u^\pm_0$, with
   $u^\pm_0$ evolved separately from each side and
   $\tau_{\mathrm c,0}=5\big\lvert\frac{p^--p^+}{p^-+p^+}\big\rvert\Delta t$ (page-local). In smooth
   flow $\tau_{\mathrm c,0}\to0$ and the single equilibrium value is recovered; at a shock the two
   one-sided values survive. The authors state that this "greatly improve[s] the reliability
   of the updated slope".
2. **Two-stage fourth-order time stepping (S2O4)** of Li and Du, rederived from a cubic
   interpolant in time of $\mathcal L_i(t)$ matched to $\mathcal L$ and $\mathcal L_t$ at $t^n$ and
   $t^n+\Delta t/2$ (§3.3, Eqs. (18)–(24)):
   $$\begin{aligned}u^{n+1/2}_i&=u^n_i+\tfrac12\Delta t\,\mathcal L_i(u^n)+\tfrac18\Delta t^2\,\mathcal L_{i,t}(u^n),\\
   u^{n+1}_i&=u^n_i+\Delta t\,\mathcal L_i(u^n)+\tfrac16\Delta t^2\big(\mathcal L_{i,t}(u^n)+2\mathcal L_{i,t}(u^{n+1/2})\big),\end{aligned}$$
   with $\mathcal L_t$ the time derivative of the flux divergence supplied by the GKS flux. The
   half step is third order and the full step fourth order.
3. **A nonlinear temporal limiter** (§3.3, Eqs. (25)–(27)). S2O4 assumes a flux continuous in
   time, which fails when a shock crosses an interface within the step. The two
   $\tfrac{\Delta t^2}3\mathcal L_t$ terms (the third- and fourth-order part) are recomputed with
   each side $l$ of the cell weighted by $\omega^{\mathrm t}_l\in[0,1]$ (page-local):
   $$\tilde\alpha^k_{\min}=1+\Big(\frac{\tau^k}{\beta^k_{\min}+\epsilon}\Big)^2,\quad\tilde\alpha^k_{\max}=1+\Big(\frac{\tau^k}{\beta^k_{\max}+\epsilon}\Big)^2,\quad\omega^{\mathrm t}_l=\min_{k=\mathrm L,\mathrm R}\frac{2\tilde\alpha^k_{\max}}{\tilde\alpha^k_{\min}+\tilde\alpha^k_{\max}},$$
   with $\beta^k_{\min}$, $\beta^k_{\max}$ the smallest and largest
   [smoothness indicators](/definitions/smoothness-indicator.md) of the spatial reconstruction
   in the cell on side $k$, $\tau^k$ its global indicator and $\epsilon=10^{-5}$. In smooth flow
   $\omega^{\mathrm t}_l=1+O(h^3)$ ($h$ the cell size, page-local), an $O(h^3\Delta t^2)$ perturbation that keeps fourth order
   (derived); near a shock $\omega^{\mathrm t}_l=O(h^4)$ (stated), which falls back to the
   second-order one-stage update. *(compiler check, not in the sources: since
   $\beta_{\min}\le\beta_{\max}$, $\tilde\alpha_{\min}\ge\tilde\alpha_{\max}$, so each ratio lies in
   $(0,1]$.)* In 2D with characteristic reconstruction the weight is the minimum over the first
   and fourth fields, because "the shock wave can only correspond to" them. The authors claim
   it is the first limiting of the high-order time derivatives of a flux (§5).
4. **Nonlinear compact reconstruction** (§3.4, Eqs. (28)–(32)) of [WENO-AO](/methods/weno-ao.md)
   type: one large-stencil polynomial $P$ combined with lower-order sub-stencil polynomials
   $q_k$ (page-local $P$, $q_k$, $R$, as on the WENO-AO page), $R(x)=\sum_k\omega_kq_k+\omega_0\big(\frac{1+C}{C}P-\sum_k\frac{C_k}{C}q_k\big)$,
   linear weights $d_0=C/(1+C)$, $d_k=C_k/(1+C)$, $C=5$, $C_k=1/n$ (page-local), and
   [WENO-Z](/methods/weno-z.md)-type weights $\alpha_k=d_k\big(1+(\tau/(\beta_k+\epsilon))^2\big)$. To
   save cost the large-stencil indicator is replaced by $\max_k\beta_k$. In 1D the stencil is
   cells $i-1,\dots,i+2$ with averages and averaged slopes (a degree-7 polynomial, eighth
   order) and $\tau=\lvert3(\beta_1-\beta_2)+(\beta_3-\beta_2)\rvert$; on triangles it is the
   cell, its neighbours and their neighbours (a cubic by least squares, fourth order) with
   $\tau$ the mean of three second differences of indicators. See
   [Hermite WENO](/methods/hermite-weno.md) for the other route to compact stencils with
   derivative data.

**Evidence** (Zhao et al., §4; CFL $0.8$ unless stated, no troubled-cell detection). The
eighth-order 1D scheme with $\Delta t=0.5\Delta x^2$ has $L_1$ errors
$2.7627\times10^{-4}$ to $5.9689\times10^{-11}$ on meshes $1/10$ to $1/80$, orders
$6.26$, $8.15$, $7.73$ (Table 1). On the 1D
[Woodward–Colella blast waves](/benchmarks/woodward-colella-blast-wave.md) (400 points) it runs at
CFL $0.8$, where the text says the previous compact GKS "can only use CFL number 0.2" and the
legend of Fig. 5 shows it at $0.1$. The fourth-order triangular scheme runs the 2D blast waves,
the Mach 3 [forward-facing step](/benchmarks/forward-facing-step.md) without a corner fix,
inviscid [cylinder flows](/benchmarks/flow-past-circular-cylinder.md) at Mach 8 and 20 from
$t=0$ "without additional treatment", a viscous Mach-5 cylinder at CFL $0.35$, the
[Daru–Tenaud tube](/benchmarks/viscous-shock-tube.md) at $\mathrm{Re}=200$ (on $h=1/400$ better
wall density than third-order CPR-GKS on $1/500$, which needs troubled-cell detection) and a
lid-driven cavity at $\mathrm{Re}=1000$; the [Shu–Osher problem](/benchmarks/shu-osher-problem.md)
runs on 200 points at CFL $0.4$ and $0.8$.

## Discrete gas-kinetic flux on unstructured grids

[Liu et al. (2023b)](/sources/liu-2023-b.md) (§3.1.2, Eqs. (18)–(25)) use the discrete
gas-kinetic flux solver (DGKFS) with a four-velocity (D2Q4) model as the viscous flux of their
fourth-order [RBF differential-quadrature finite volumes](/methods/rbf-differential-quadrature.md).
In the face-normal frame,

$$\hat f=(1-\tau_{\mathrm D})\,f^{\mathrm I}+\tau_{\mathrm D}\,f^{\mathrm{II}},\qquad \tau_{\mathrm D}=\frac{\mu}{p\,\delta_t},$$

with $f^{\mathrm I}$ the Euler flux of the interface state obtained from the moments of the
four particle distributions, $f^{\mathrm{II}}$ the flux carried by the particles streamed from
$x-\mathsf v_d\delta_t$, $\delta_t$ a streaming step much smaller than $\Delta t$ and
$\tau_{\mathrm D}$ the dimensionless collision time (page-local; the source's $\tau_0$). The particle velocities lie on a
circle of radius $\sqrt{2(\gamma-1)e}$ around the fluid velocity, and the particle states are
upwind evaluations of the cubic cell polynomials (Eqs. (21)–(22)). The authors state that
DGKFS evaluates inviscid and viscous fluxes simultaneously, avoiding the separate viscous
treatment of DG and spectral-volume methods, and is simpler and cheaper than Maxwellian-based
GKS (§1). Inviscid tests use a Roe flux instead
([Roe solver](/methods/roe-riemann-solver.md)).

**Evidence** (Liu et al. (2023b), §5): primary-vortex height $0.166$ on the Daru–Tenaud tube at
$\mathrm{Re}=200$, $h=1/500$, against $0.166$ (compact high-order GKS) and $0.165$ (WENO-GKS)
cited from the literature (Table 2); NACA0012 at $M=0.8$, $\mathrm{Re}=500$, $10°$:
$C_d=0.28926$, $C_l=0.47809$ on 5788 triangles (Table 1); a carbuncle-free Mach-8.03 viscous
cylinder whose wall pressure and heat flux agree with Wieting's experiment (Figs. 17–18).

## Kinetic flux-vector splitting and bound preservation

[Wu & Shu (2023)](/sources/wu-2023-b.md) (§5.1, Ex. 1.2, Remark 5.2) prove with
[geometric quasilinearization](/methods/geometric-quasilinearization.md) that the first-order
gas-kinetic (kinetic flux-vector splitting) scheme for Euler is bound preserving under
$\nu\le1$, with a proof much shorter than the classical one because the free auxiliary
velocity commutes with the velocity integrals; [Fan et al. (2022)](/sources/fan-2022.md)
(§1.1) list gas-kinetic schemes among the first-order positivity-preserving building blocks of
high-order WENO ([bound preservation](/properties/bound-preservation.md)).

## Qualifications

- **A normative claim.** "Only the compact schemes with neighboring interaction are the
  physically consistent numerical algorithms" (Zhao et al., §2) excludes the wide-stencil
  finite-difference WENO and TENO schemes that make up most of this bundle; the paper argues it
  from the domain of dependence, not from a failure of those schemes. Likewise its rejection
  of the Riemann solver as an evolution model "not adequate in its dynamics" for compact
  schemes is argued, not tested against a Riemann-solver compact scheme.
- **CFL comparisons.** The claim that a DG method of the same order needs CFL $0.1$ against
  $0.8$ here (Zhao et al., §2) compares CFL numbers defined with different cell sizes (on
  triangles $h$ is $\lvert I_i\rvert/(2\lvert\partial I_i\rvert)$) and different steppers; it is
  asserted, not measured. The near-shock behaviour $\omega^{\mathrm t}=O(h^4)$ is stated without
  derivation.
- **Printed slips** (Zhao et al., arXiv v1): the stated interpolation conditions (20) are
  sums of the derivatives one order too high, and (21) prints $4/t^2$, $24/t^3$ where
  $4/\Delta t^2$, $24/\Delta t^3$ follow from the conditions; Eq. (22) is consistent with the
  corrected conditions. *(compiler check, not in the sources: matching
  $P^3(\Delta t/2)=\mathcal L^{n+1/2}$ and $P^3_t(\Delta t/2)=\mathcal L^{n+1/2}_t$ with
  $P^3=b_0+b_1t+b_2t^2/2+b_3t^3/6$ gives the printed $b_2$, $b_3$ with powers of $\Delta t$, and
  $\int_0^{\Delta t}P^3=\Delta tb_0+\tfrac16\Delta t^2b_1+\tfrac13\Delta t^2\mathcal L^{n+1/2}_t$, the
  S2O4 update above.)*
- Liu et al. (2023b) state that DGKFS is locally $O(\delta_t^2)$ and that "the overall accuracy
  would not be affected"; their fourth-order convergence test is inviscid and uses Roe, so the
  high-order accuracy of the viscous DGKFS path is not measured (§3.1.2, §5.1).

# Citations

- [Zhao et al. (2023)](/sources/zhao-2023.md) — Abstract, §2 (Eqs. (1)–(4)), §3.1 (Eqs. (5)–(13)), §3.2 (Eqs. (14)–(17)), §3.3 (Eqs. (18)–(27)), §3.4 (Eqs. (28)–(32)), §4 (Table 1, Figs. 5–16), §5 (arXiv v1).
- [Liu et al. (2023b)](/sources/liu-2023-b.md) — §1, §3.1.2 (Eqs. (18)–(25)), §5 (Tables 1–2, Figs. 13, 17–18).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — §5.1 (Ex. 1.2, Remark 5.2) (arXiv v1).
- [Fan et al. (2022)](/sources/fan-2022.md) — §1.1.
