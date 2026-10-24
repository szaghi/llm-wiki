---
type: Method
title: "SSP Runge–Kutta time stepping"
description: "Strong-stability-preserving Runge–Kutta methods are convex combinations of forward-Euler steps, so bound-preserving, invariant-domain and limiter proofs need only forward Euler; the three-stage third-order Shu–Osher scheme, mostly at CFL numbers 0.3 to 0.6, is the default stepper of the bundle, and the page records how sources size time steps and state the positivity CFL."
status: established
aliases: [SSP-RK, SSP-RK3, TVD Runge–Kutta, TVD-RK3, Shu–Osher Runge–Kutta, strong-stability-preserving time integration]
tags: [bound-preserving, limiting, weno, dg]
timestamp: 2026-10-24T06:00:00Z
---

# SSP Runge–Kutta time stepping

Strong-stability-preserving (SSP) Runge–Kutta methods integrate the semi-discrete system
$\frac{d}{dt}u=\mathcal L(u)$ by stages that are convex combinations of forward-Euler steps.
In this bundle time integration is only the stepper of the spatial scheme; the SSP property
matters because it transfers any property proved for one forward-Euler step — bound
preservation, a convex-limiting bound, a TVD bound — to the full high-order step, under a
possibly reduced time step.

## The three-stage third-order scheme

The default of almost every source here is the scheme of Shu & Osher, as printed by
[Fu (2021)](/sources/fu-2021.md) (§5, Eq. (30)), with page-local stage values $u^{(1)}$, $u^{(2)}$:

$$\begin{aligned}
u^{(1)}&=u^n+\Delta t\,\mathcal L(u^n),\\
u^{(2)}&=\tfrac34u^n+\tfrac14u^{(1)}+\tfrac14\Delta t\,\mathcal L(u^{(1)}),\\
u^{n+1}&=\tfrac13u^n+\tfrac23u^{(2)}+\tfrac23\Delta t\,\mathcal L(u^{(2)}).
\end{aligned}$$

Several sources call it "third-order TVD Runge–Kutta"
([Li et al. (2022b)](/sources/li-2022-b.md), [Luo & Wu (2021)](/sources/luo-2021-b.md),
[Wang & Don (2022)](/sources/wang-2022-b.md), citing Gottlieb & Shu 1998). CFL numbers used
with it:

| Source | Scheme | CFL $\nu$ |
|---|---|---|
| [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) | DGSEM with subcell limiting | 0.5 (blending recomputed every stage, §5) |
| [Li et al. (2022b)](/sources/li-2022-b.md) | FD WENO-ZN, 1D | 0.5 (Eq. (38)) |
| [Wang et al. (2023b)](/sources/wang-2023-b.md) | A-WENO with CURH flux | 0.45; $\Delta x^{2/3}$ in the accuracy test (Remark 1) |
| [Wang & Don (2022)](/sources/wang-2022-b.md) | FD affine-invariant WENO | 0.45 (§3) |
| [Fu (2021)](/sources/fu-2021.md), [Takagi et al. (2022)](/sources/takagi-2022.md) | FD TENO, TENO-THINC | 0.4 (0.35 for the blast waves in Takagi et al.) |
| [Chertock et al. (2023)](/sources/chertock-2023.md) | central-upwind FV | 0.4 |
| [Balsara et al. (2024)](/sources/balsara-2024.md) | fluctuation-form FD-WENO | 0.3 (2D accuracy), 0.4 (2D problems), 0.8 (1D problems) |
| [Wu & Shu (2023)](/sources/wu-2023-b.md) | BP locally divergence-free DG, MHD | 0.15 |
| [Peng et al. (2024)](/sources/peng-2024.md) | OEDG, discontinuous tests | $1/(2N+1)$ |
| [Cao et al. (2026)](/sources/cao-2026.md) | COS(DG), discontinuous tests | 0.3, 0.16, 0.1 for $N=1,2,3$; $\Delta t=\nu/(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$ in 2D (§6) |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) | moment-based multi-resolution HWENO | 0.6 (1D and 2D) |
| [Wang et al. (2021)](/sources/wang-2021.md) | FD multi-resolution WENO | 0.6; 0.3 for the viscous shock tube |
| [Wong et al. (2021)](/sources/wong-2021.md) | positivity-preserving WCNS, gas–liquid | 0.5 |
| [Zheng et al. (2021)](/sources/zheng-2021.md) | conservative two-medium A-WENO | 0.5; $\Delta t=O(\Delta x^{5/3})$ in the accuracy tests |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) | ninth-order central scheme with adaptive dissipation | 0.5 (Taylor–Green), 0.02 (reacting shock tube) |
| [Pazner (2021)](/sources/pazner-2021.md) | sparse IDP DG with subcell convex limiting | half the IDP bound $\min_im_i/(2\lvert\hat d_{ii}\rvert)$, printed with $\hat d_{ii}$ (§3.2, §5; see below) |
| [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) | entropy-stable moving-mesh FD | 0.4 (2D), 0.3 (3D); $\Delta t=\nu(\min\Delta\xi)^{5/3}$ in the accuracy tests ($\Delta\xi$ the computational spacing) |
| [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) | weakly compressible two-phase solver | 0.4 on the acoustic speed, with viscous, surface-tension and phase-field limits (Eq. (38)) |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) | unstructured CWENO, multicomponent | 0.1 in the convergence test, others not printed |
| [Fan et al. (2021)](/sources/fan-2021.md) | positivity-preserving FV hybrid HWENO, Navier–Stokes | $\Delta t=\min\{\Delta x/(12a),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$, halved on failure (below) |
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) | MFC, FV WENO with HLLC | not stated; RK orders 1 to 5 available |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) | FV learned three-point WENO (WENO3-NN) | 0.6; 0.05 in the $\sin^3$ convergence run |
| [Chen & Wu (2022)](/sources/chen-2022-b.md) | physical-constraint-preserving FV WENO on triangles, relativistic | 0.5 (default) |
| [Chu et al. (2022)](/sources/chu-2022.md) | fifth-order A-WENO path-conservative CU | 0.5; $\frac1{10}\Delta x^{2/3}$ in the accuracy test |
| [Du, Shu & Zhong (2022)](/sources/du-2022.md) | RKDG with simple WENO limiter, triangles | 0.3 ($\mathbb P^1$), 0.18 ($\mathbb P^2$, $\mathbb P^3$); $\Delta t\sim\Delta x^{4/3}$ for $\mathbb P^3$ accuracy ($\Delta x$ the mesh size) |
| [Duan & Tang (2022)](/sources/duan-2022.md) | entropy-stable moving-mesh FD, relativistic (M)HD | 0.4 (2D), 0.3 (3D); $\Delta t=\nu\Delta\xi^2$ (sixth-order EC) and $\nu\Delta\xi^{5/3}$ (fifth-order ES) in the accuracy tests |
| [Nguyen et al. (2022)](/sources/nguyen-2022.md) | FV MUSCL, $N$-phase model, update of primitive variables | 0.5 (water–air), 0.9 (gas–gas) |
| [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) | FR with entropy filtering after every stage | not stated |
| [Fan et al. (2022)](/sources/fan-2022.md) | positivity-preserving FD WENO, Navier–Stokes | $\Delta t=\min\{0.6\,\Delta x/a,\ 0.001\,\mathrm{Re}\,\Delta x^2\}$, halved on failure (Alg. 2, below) |
| [Fan et al. (2023)](/sources/fan-2023.md) | FD Hermite WENO (HWENO-R) | 0.6; $\Delta t\propto\Delta x^{5/3}$ in the smooth tests (§3) |
| [Hong et al. (2022)](/sources/hong-2022.md) | FD TENO-M | 0.5 |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) | FD adaptive TENO | 0.4; 0.35 for the blast waves (§4, Eq. (17)) |
| [Liang et al. (2022)](/sources/liang-2022.md) | FD TENO with THINC switch | 0.4; 0.35 for the high-Mach jets; double Mach reflection "not very sensitive" to 0.2, 0.4, 0.6 (§4.5, Fig. 15) |
| [Ji et al. (2022)](/sources/ji-2022.md) | unstructured FV TENO (UCNS3D) | 0.4 (§5) |
| [Lin & Chan (2024)](/sources/lin-2024.md) | DGSEM with entropy-LP subcell limiting | $\Delta t=\tfrac12\min_im_i/(2\lambda_i)$, computed at the first stage and kept for all three (Eq. (52); $m_i$ the lumped mass, $\lambda_i$ not defined in the paper, taken from Lin et al. (2023)) |
| [Jeong et al. (2022)](/sources/jeong-2022.md) | FD RBF-based WENO | 0.4 |
| [Li et al. (2023a)](/sources/li-2023.md) | FD scale-invariant MR A-WENO | 0.45 |
| [Wan & Xia (2022)](/sources/wan-2022.md) | FD WENO, steady problems by pseudo-time marching | 0.2; 0.6 in 3D (Eq. (4.1)) |
| [Ji, Liang & Fu (2023)](/sources/ji-2023.md) | unstructured FV TENO-D, orders 4–7 (UCNS3D) | 0.4 (§4) |
| [Liang & Fu (2024b)](/sources/liang-2024-b.md) | FD hybrid TENO-S | 0.4; Sod and a 2D Riemann problem "not very sensitive" to 0.4–0.6 (§4.2, §4.5.1, Figs. 4, 9) |
| [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) | FV Hermite WENO, relativistic | 0.6, definition not printed; PCP proved for $\Delta t\le\tfrac1{12}\Delta x/a$ (§3, §5) |
| [Yu, Liu & Feng (2023)](/sources/yu-2023.md) | third-order RKDG, Euler with a singular source | $\sup\lvert\lambda_l\rvert\Delta t/\Delta x\le\tfrac12$ (§5) |
| [Chu et al. (2025a)](/sources/chu-2025.md) | adaptive low-dissipation central-upwind FV | 0.4 (§4) |
| [Chu et al. (2025b)](/sources/chu-2025-b.md) | LCD path-conservative central-upwind FV | 0.45 (§5) |
| [Ding & Wu (2024a)](/sources/ding-2024.md) | divergence-free positivity-preserving FV WENO, MHD | 0.3; positivity proved for forward Euler and lifted to SSP-RK3 by convexity (Remark 2.2) |
| [Fan et al. (2025a)](/sources/fan-2025.md) | moment-based FV Hermite WENO with unified stencils (HWENO-U) | 0.6, with a modified scheme whose linear bound is about 0.824 (below) |
| [Huang et al. (2025b)](/sources/huang-2025-b.md) | wave-propagation FV with learned BVD selection, HLLC | SSP-RK2 for the tests (0.4 on Sod); SSP-RK3 at 0.1 to generate the training data (§2.1, §3.3.2, §4.2.1) |
| [Liu & Wu (2025)](/sources/liu-2025.md) | locally divergence-free OEDG, ideal MHD, $N=2$ | 0.12; positivity proved for forward Euler and carried to SSP-RK3 by convexity (§3.2, §3.6, §4) |
| [Liu et al. (2025b)](/sources/liu-2025-b.md) | entropy-stable oscillation-free nodal DG, ideal MHD, $N=2$ | $0.6/(2N+1)=0.12$, each stage split into an explicit step and a closed-form implicit damping step (below) |
| [Liu et al. (2025c)](/sources/liu-2025-c.md) | globally divergence-free entropy-stable nodal DG, ideal MHD | 0.45 with Ketcheson's ten-stage fourth-order SSP-RK, $\Delta t=\nu/(a^{(1)}/\Delta x+a^{(2)}/\Delta y)$ (below) |
| [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) | bound-preserving generalized Active Flux | $\Delta t=\nu/\max_i(\varrho(\bar u_i)/\Delta x_i)$ with $\varrho$ the spectral radius (page-local), $\nu$ 0.1 to 0.4 by splitting and test; step halved and restarted when a stage fails the bound-preserving conditions (Eq. (15), Remark 4.2) |
| [Barsukow et al. (2026)](/sources/barsukow-2026.md) | arbitrary-order 2D Active Flux, linear advection | maximal 0.27, 0.20, 0.17, 0.12, 0.088 for orders 3–7 (Table 3; below) |
| [Chu et al. (2025c)](/sources/chu-2025-c.md) | new low-dissipation central-upwind FV | 0.475 (§3) |

[Fu (2023)](/sources/fu-2023.md), [Cui et al. (2024)](/sources/cui-2024.md) (Exs. 2–5) and
the variants A and C of [Active Flux](/methods/active-flux.md)
([Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), §§3.2, 5.3) use the same scheme; for
Active Flux the SSP-RK3 stability limits of the point-value formulas range from $\nu=0.45$ to
$1$ (variant A) and are $0.13$ (MD5) and $0.066$ (MD7) for variant C, with RK5 giving only a
slightly larger limit for FD5b. [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md)
(§3.3) state that SSP-RK3 "is stable for $CFL\le1$", a statement about the time integrator
that does not give the admissible CFL of their spatial scheme (their convergence test uses
0.1).

[Zheng et al. (2021)](/sources/zheng-2021.md) (§2.2.6, Eq. (27)) write the same scheme in
increment form, $u^{(2)}=u^n+\tfrac14\Delta t\big(\mathcal L(u^n)+\mathcal L(u^{(1)})\big)$,
$u^{n+1}=u^n+\tfrac16\Delta t\big(\mathcal L(u^n)+\mathcal L(u^{(1)})+4\mathcal L(u^{(2)})\big)$,
and accumulate the stage fluxes so that every stage, and the final step, is a single
conservative flux difference from $u^n$; this is what lets their cell merging and
redistribution near a material interface stay conservative. *(compiler check, not in the
sources: expanding the Shu–Osher form above gives exactly these two lines.)*

**Modified stages for moment-based Hermite WENO.** [Fan et al. (2025a)](/sources/fan-2025.md)
(§2.1, Eq. (2.13); §2.3, Thms. 2.1–2.2) evolve the cell average $\bar u_i$ and the first moment
$\bar u^{(1)}_i$ (registry §10) by the $\mathbb P^1$ DG weak form, but reconstruct on cell $i$ from
$\{\bar u_{i-1},\bar u_i,\bar u_{i+1},\bar u^{(1)}_{i-1},\bar u^{(1)}_{i+1}\}$, without the central
first moment ([Hermite WENO](/methods/hermite-weno.md)). For $\partial_tu+\partial_xu=0$ the linear
version of that scheme is unconditionally unstable with forward Euler and with the Shu–Osher
scheme: the spectral radius of the amplification matrix exceeds one for every $\Delta t>0$ tested,
e.g. $1+3.158\times10^{-12}$ for forward Euler at $\Delta t/\Delta x=10^{-12}$ (Thm. 2.1, Eqs. (2.27)–(2.31)). Inspired by the
Lax–Friedrichs scheme, they replace the first moment by its high-order HWENO modification
$\hat u^{(1)}_i$, the first moment of the reconstructed polynomial (page-local), as the "old value"
in every convex combination of the three stages, the cell average being advanced by the unmodified stages
(Eq. (2.13)):

$$\begin{aligned}
\bar u^{(1),[1]}_i&=\hat u^{(1),n}_i+\Delta t\,\mathcal L^{(1)}_i(u^n),\\
\bar u^{(1),[2]}_i&=\tfrac34\hat u^{(1),n}_i+\tfrac14\big(\hat u^{(1),[1]}_i+\Delta t\,\mathcal L^{(1)}_i(u^{[1]})\big),\\
\bar u^{(1),n+1}_i&=\tfrac13\hat u^{(1),n}_i+\tfrac23\big(\hat u^{(1),[2]}_i+\Delta t\,\mathcal L^{(1)}_i(u^{[2]})\big),
\end{aligned}$$

with stage superscripts in brackets, so that the first moment $\bar u^{(1)}$ is not read as the
stage value $u^{(1)}$ of the Shu–Osher form above, and $\mathcal L^{(1)}$ the first-moment operator
(page-local).
For the linear scheme the necessary von Neumann condition becomes $0<\Delta t/\Delta x\lesssim0.824$,
found by sampling $10^4$ wavenumbers (Thm. 2.2, Eq. (2.33)); the tests run at CFL $0.6$ (§3). The
result is a necessary condition for the linear scheme only. The same replacement had been used in
finite-difference HWENO, as the authors cite (§2.1).

## Why SSP: forward Euler suffices

- [Cui et al. (2024)](/sources/cui-2024.md) prove their bound-preserving DG theorems for one
  forward-Euler step and state that they hold for SSP time stepping (Thm. 7.1, footnote 2,
  Remark 7.9).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) state that bound preservation is retained with SSP
  Runge–Kutta "because SSP methods are convex combinations of forward Euler" (§6.2).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) write their a posteriori
  limiter in forward-Euler FCT form on the same ground (§2, Eqs. (26)–(27)); see
  [convex limiting](/methods/convex-limiting.md).
- [Pazner (2021)](/sources/pazner-2021.md) proves invariant-domain preservation of the
  low-order DG update for one forward-Euler step under $\Delta t\le\min_im_i/(2\lvert\hat d_{ii}\rvert)$
  and extends it to high order in time by SSP-RK (Prop. 7). The paper prints the bound as
  $\min_im_i/(2\hat d_{ii})$ with $\hat d_{ii}=-\sum_{j\ne i}\hat d_{ij}\le0$, which is negative;
  the convex combination it rests on, Eq. (39), needs $\lvert\hat d_{ii}\rvert$.
- [Renac (2021)](/sources/renac-2021.md) proves positivity of the cell averages of the
  entropy-stable DGSEM for forward Euler (Thm. 6.1) and applies the scaling limiter at the
  end of each stage of SSP-RK(4,3).
- [Wong et al. (2021)](/sources/wong-2021.md) (§5.3) call the extension of their
  positivity- and boundedness-preserving limiters to SSP-RK "trivial", the stages being
  convex combinations of forward-Euler steps, and state that the CFL upper limit is still
  0.5.
- [Fan et al. (2021)](/sources/fan-2021.md) (§3.3) prove their positivity theorems for
  forward Euler (Thms. 1–2) and state that they "still hold for (2.6) if the CFL is one
  third of (3.12) and (3.30)", (2.6) being SSP-RK3 in the Shu–Osher form; see
  Qualifications.
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) (Remark 3.1) quote free-stream
  preservation of the fully discrete moving-mesh scheme with SSP-RK3 as proved in the
  companion paper of Duan & Tang, not in the paper itself. For the high-order
  finite-difference case the proof is in [Duan & Tang (2022)](/sources/duan-2022.md)
  (Prop. 3.2): forward Euler with the discrete volume and surface conservation laws keeps a
  constant state, and SSP-RK, a convex combination of forward-Euler steps, inherits it
  ([free-stream preservation](/properties/free-stream-preservation.md)).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) (Thm. 3.1, Eq. (26)) prove the
  physical-constraint-preserving property of the relativistic finite-volume WENO scheme for
  forward Euler and obtain it for SSP-RK3 "by convexity" of the admissible set.
- [Fan et al. (2022)](/sources/fan-2022.md) (§3.5) state that any SSP Runge–Kutta method keeps
  positivity, being a convex combination of forward-Euler steps and $G$ convex, and apply their
  scaling limiter at every stage of SSP-RK3 (Eq. (3.24)). [Fan et al. (2023)](/sources/fan-2023.md)
  (§2.2, Eq. (2.6)) replace, at every stage, the derivative component that enters the convex
  combination by its limited version, and apply their positivity-preserving flux limiter at the
  final stage to the Runge–Kutta-combined flux (App. A;
  [positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) (§3.2, Alg. 3) filter after every
  stage and compute the local minimum-entropy bound from the previous stage, which keeps the
  forward-Euler argument stage by stage ([entropy filtering](/methods/entropy-filtering.md)).

- [Lin & Chan (2024)](/sources/lin-2024.md) (footnote 7) need SSPRK(3,3) and the CFL
  condition only for positivity; the cell entropy inequality their subcell limiter enforces is
  semi-discrete and does not depend on the time integrator, and no fully discrete entropy
  inequality is claimed.

## Sizing the time step

- **For accuracy tests.** A third-order integrator caps the observed order of a higher-order
  spatial scheme unless $\Delta t$ shrinks faster than $\Delta x$.
  [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§4.1, Eqs. (39)–(40), Fig. 2)
  model the error as $C_\tau\Delta t^{3}+C_h\Delta x^{9}$ and explain why the observed order
  of their ninth-order scheme on the [isentropic vortex](/benchmarks/isentropic-vortex.md)
  varies between 3 and 9: keeping the ratio of the two errors fixed needs
  $\Delta t\propto\Delta x^{3}$, while a constant CFL gives $\Delta t\propto\Delta x$; ninth
  order appears over $100^2$–$500^2$ only for CFL $1.25\times10^{-2}$ and $6.25\times10^{-3}$.
  [Zheng et al. (2021)](/sources/zheng-2021.md) and [Li, Duan & Tang (2022c)](/sources/li-2022-c.md)
  take $\Delta t\propto\Delta x^{5/3}$ for fifth order; Zheng et al.'s accuracy budget at the
  interface moreover needs $\Delta t=O(\Delta x^{r_t})$ with $r_t\le2$ (page-local $r_t$), because a low-order
  interface flux there is recovered by dividing by $\Delta t/\Delta x$ (Prop. 2.2, App. A).
  [Wang et al. (2021)](/sources/wang-2021.md) report fifth order at CFL 0.6 without a
  reduction.
- **Adaptively, for positivity.** [Fan et al. (2021)](/sources/fan-2021.md) (§3.3, Eq. (3.33))
  start from $\Delta t=\min\{\Delta x/(12a),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$ ($a$ the
  maximum of $\lvert v\rvert+c$; $1/12$ equals the boundary Gauss–Lobatto weight
  $1/(N_{\mathrm{GL}}(N_{\mathrm{GL}}-1))$ of their decomposition for the four-point rule
  *(compiler check, not in the sources)*) and, if any stage cell average leaves the admissible set, halve $\Delta t$
  and restart the step from the first stage; their theorems guarantee termination. The
  viscous bound $O(\mathrm{Re}\,\Delta x^2)$ is needed in addition, since the positivity
  bound is only $O(\Delta x)$.
  [Fan et al. (2022)](/sources/fan-2022.md) (§3.5, Alg. 2, Remark 3.4) use the same strategy
  in their finite-difference counterpart: $\Delta t=\min\{0.6\,\Delta x/a,\ 0.001\,\mathrm{Re}\,\Delta x^2\}$,
  $a=\max_i(\lvert v_i\rvert+c_i)$, halved and restarted when a stage leaves $G$, termination
  guaranteed by their Theorem 1; for smooth solutions the positivity bound gives $\Delta t=O(\Delta x)$,
  so the viscous bound must always be obeyed and the positivity bound is enforced only when
  positivity is lost (Remark 3.3). Their accuracy tests take $\Delta t=\min\{0.6\Delta x^{5/3},0.001\,\mathrm{Re}\,\Delta x^2\}$
  for fifth-order and $\Delta x^{7/3}$ for seventh-order WENO *(compiler check, not in the sources:
  $(\Delta x^{5/3})^3=\Delta x^5$ and $(\Delta x^{7/3})^3=\Delta x^7$, so the third-order time error
  matches the spatial order)*.
- **For accuracy tests with classical RK4.** [Jeong et al. (2022)](/sources/jeong-2022.md) (§5)
  run their order tests with the fourth-order "non-TVD" Runge–Kutta and $\Delta t\sim(\Delta x)^{6/4}$,
  so that, in their words, the time error is effectively sixth order.
- **DG step formulas.** [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
  (§5, Eq. (89)) take $\Delta t=\min\big(\mathrm{CFL}\,\beta^a(N)\Delta x/(\lambda^a_{\max}(2N+1)),\ \mathrm{CFL}_\nu\beta^\nu(N)\Delta x^2/(\lambda^\nu_{\max}(2N+1)^2)\big)$
  with empirical factors $\beta^a,\beta^\nu$ (page-local) and CFL $=$ CFL$_\nu=0.5$.

## Other SSP methods and refinement rules

- **Ten-stage fourth order.** [Liu et al. (2025c)](/sources/liu-2025-c.md) (§4.2, §5)
  advance their globally divergence-free entropy-stable DG scheme for MHD with Ketcheson's
  ten-stage fourth-order SSP Runge–Kutta method, applying the forward-Euler template of DG step,
  face update of the normal field, limiter and least-squares reconstruction of the field with an
  energy correction at every stage (tableau not reprinted). Entropy stability is semi-discrete per
  cell; the full method with reconstruction, limiter and time stepping is not proved fully
  discrete entropy stable.
- **A split stage with implicit damping.** [Liu et al. (2025b)](/sources/liu-2025-b.md) (§3.3,
  Eqs. (3.20)–(3.21)) write each forward-Euler stage of third-order TVD Runge–Kutta as an
  explicit DG step $\tilde u$ followed by the implicit damping
  $u=\tilde u-c_{\mathrm s}\frac{2\Delta t}{\Delta x}\sigma(\tilde u)(u-\bar u)$ with the stage weights $c_{\mathrm s}=1,\tfrac14,\tfrac23$
  (page-local $\sigma$; $\Delta x$ the element size, the sources' $\tau$ and $h$), which is solved in closed form
  and keeps the cell mean ([operator splitting](/methods/operator-splitting.md)).
- **Post-processing once per step.** [Cao et al. (2026)](/sources/cao-2026.md) (§2.1,
  Eq. (26)) run the stages of SSP-RK3 on the unmodified DG operator and apply their
  oscillation-suppressing convex blend with the cell average only to the final stage, as the
  start of the next step ([COS(DG)](/methods/cos-dg.md)), whereas OEDG and most DG limiters act
  after every stage. Since the blend is not applied at intermediate stages, the
  positivity-preserving scaling limiter that their discontinuous Euler runs need is applied at the
  stages separately (§6; [Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md)). Smooth
  tests use an $(N+1)$-stage Runge–Kutta method of order $N+1$ instead.
- **Direction-dependent stability regions.** For their arbitrary-order 2D Active Flux on linear
  advection, [Barsukow et al. (2026)](/sources/barsukow-2026.md) (§4.2, Eqs. (40)–(46), Table 3,
  Figs. 7–8; arXiv v2) diagonalize the semi-discrete operator and apply the SSP-RK3 stability
  polynomial $\mathcal G(z)=1+z+\tfrac12z^2+\tfrac16z^3$ (registry §10) eigenvalue by eigenvalue. The maximal CFL number,
  defined as $\lvert a\rvert\Delta t_{\max}/\Delta x$ for equal velocity components (Eq. (42); $a$ the advection velocity), is 0.27, 0.20,
  0.17, 0.12 and 0.088 for orders 3 to 7. The stable region in the plane of the two directional CFL
  numbers is about a disc for orders 3 and 4 and about a square for order 5, so the stable step
  depends on the direction as well as the magnitude of the velocity; moments added at orders 6 and 7
  round the corners again. Their convergence runs scale $\nu$ with $\Delta x^{(N-2)/3}$ so that
  $\Delta t^3=O(\Delta x^{N+1})$ for order $N+1$ (§5.1).

- **Five-stage fourth order, printed.** [Berta et al. (2024)](/sources/berta-2024.md) (§3.3,
  Eqs. (31)–(32)) advance their fourth-order finite-volume MHD scheme with eSSPRK(5,4), with
  page-local stages $u^{(1)},\dots,u^{(4)}$:
  $$\begin{aligned}
  u^{(1)}&=u^n+0.391752226571890\,\Delta t\,\mathcal L(u^n),\\
  u^{(2)}&=0.444370493651235\,u^n+0.555629506348765\,u^{(1)}+0.368410593050371\,\Delta t\,\mathcal L(u^{(1)}),\\
  u^{(3)}&=0.620101851488403\,u^n+0.379898148511597\,u^{(2)}+0.251891774271694\,\Delta t\,\mathcal L(u^{(2)}),\\
  u^{(4)}&=0.178079954393132\,u^n+0.821920045606868\,u^{(3)}+0.544974750228521\,\Delta t\,\mathcal L(u^{(3)}),\\
  u^{n+1}&=0.517231671970585\,u^{(2)}+0.096059710526147\,u^{(3)}+0.063692468666290\,\Delta t\,\mathcal L(u^{(3)})\\
  &\quad+0.386708617503268\,u^{(4)}+0.226007483236906\,\Delta t\,\mathcal L(u^{(4)}),
  \end{aligned}$$
  "strongly stable" under the forward-Euler restriction, with
  $\Delta t=\nu\min_{ijk}\min_d\big(\Delta x^{(d)}/\lvert\lambda^{(d)}_{\max}\rvert\big)$, $\lambda^{(d)}_{\max}$
  the outermost fast magnetosonic speed (page-local $\Delta x^{(d)}$, $\lambda^{(d)}_{\max}$); CFL
  0.4 in 2D and 0.3 in 3D for the Alfvén-wave convergence runs, 0.4 for the field loop and the
  current sheet, 0.5 for Orszag–Tang (§5). RK2 and RK3 serve their second- and third-order
  reference schemes. They note that the fifth-order finite-difference scheme they compare
  against needs $\Delta t\sim\Delta x^{5/3}$ with RK3 to keep fifth order (§5.2). *(compiler check,
  not in the sources: the convex coefficients of every stage sum to one, and on $u'=\lambda u$ the
  printed scheme gives $u^{n+1}=\big(1+z+\tfrac{z^2}2+\tfrac{z^3}6+\tfrac{z^4}{24}+0.00448\,z^5\big)u^n$,
  $z=\lambda\Delta t$, i.e. fourth order.)*
- Higher order in time: the fourth-order SSP-RK of Spiteri & Ruuth
  ([Balsara et al. (2024)](/sources/balsara-2024.md), §VII); a five-stage fourth-order SSP-RK
  for the $t=2000$ advection run of [Takagi et al. (2022)](/sources/takagi-2022.md) (§4.2);
  SSP **multistep** methods of order $N+1$ for $\mathbb P^N$-DG, with SSP coefficients $1/3$
  (four-step third order), $\approx0.282$ (ten-step fifth), $\approx0.217$ (eighteen-step
  seventh) and $0.1$ (22-step ninth) in [Cui et al. (2024)](/sources/cui-2024.md) (§7, Ex. 1).
- **Orders above four: multistep–multistage SSP.** [Teissier et al. (2024)](/sources/teissier-2024.md)
  (arXiv v2, read under an earlier title with two of the three authors; §3.6, Table 1, Eqs.
  (60)–(65)) match the time order to the spatial order of finite-volume MHD solvers of orders 2
  to 10. They recall that no explicit single-step SSP Runge–Kutta method exists above order four
  and that two-step SSP methods reach at most order eight, so tenth order needs at least three
  steps. Their integrators, SSP$(p,s,n)$ for order $p$, $s$ stages and $n$ steps (page-local
  notation), are Ketcheson's ten-stage SSP(2,10,1) and SSP(4,10,1) and the multistep–multistage
  SSP(6,10,2), SSP(8,10,3) and SSP(10,20,3) from the sspsite collection, with Courant numbers
  $C_{\mathrm{CFL}}=1.9,1.9,1.5,1.2,2.1$ in $\Delta t\le C_{\mathrm{CFL}}\min(\Delta x/a^{(1)},\Delta y/a^{(2)},\Delta z/a^{(3)})$
  ($a^{(d)}$ the Lax–Friedrichs speeds, page-local) and separate viscous and resistive constants;
  the eighth-order two-step methods were rejected because they need a smaller step than the
  three-step ten-stage one. Multistep start-up doubles a step $\Delta t_{\mathrm{CFL}}/2^{\alpha_{\mathrm s}}$
  (page-local $\alpha_{\mathrm s}$) taken with the fourth-order starter until the full step is reached,
  with the first step small enough that the starter's error stays below the target order (Eq. (60)).
  On a 3D MHD vortex the solvers reach their design orders (EOC 4.46, 6.12, 7.87, 9.74 for orders
  4 to 10 at $192^3$), while the eighth-order solver with a second-order integrator at CFL 0.5
  falls to order 2.12 (Table 2). Cost per step relative to the second-order solver is 1.3, 1.6,
  2.2 and 5.9 for orders 4 to 10, and the cost to a fixed time, i.e. divided by the Courant
  number, 1.3, 2.0, 3.5 and 5.3 (Table 3; hardware not specified). See
  [magnetized vortex](/benchmarks/magnetized-vortex.md).
- For smooth problems, [Peng et al. (2024)](/sources/peng-2024.md) match an explicit RK of
  order $N+1$ to $\mathbb P^N$ (§5); Balsara et al. refine the time step as
  $\Delta t_{\mathrm{fine}}/\Delta t_{\mathrm{coarse}}=(\Delta x_{\mathrm{fine}}/\Delta x_{\mathrm{coarse}})^{r_{\mathrm s}/3}$
  (third-order RK) or $^{r_{\mathrm s}/4}$ (fourth-order RK) for spatial order $r_{\mathrm s}$
  (page-local, §VII).
- **IMEX.** With stiff relaxation sources, Balsara et al. use the IMEX-SSP3(4,3,3) scheme of
  Pareschi & Russo (coefficients printed in §X, Eqs. (10.1)–(10.7)), which reduces to the
  Shu–Osher SSP-RK3 when the stiff source vanishes.
- **More stages.** The four-stage third-order and five-stage fourth-order SSP-RK of Spiteri
  & Ruuth in [Renac (2021)](/sources/renac-2021.md) (§7; practical step bound 0.4, less
  restrictive than the proven one) and the five-stage fourth-order one in
  [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) (§5), whose blending
  coefficient is recomputed before every stage; their entropy-conservative runs lose
  entropy at fourth order in the time step, i.e. through the time integrator (§6.1,
  Fig. 5). An eighth-order RK serves the convergence test of
  [Pazner (2021)](/sources/pazner-2021.md) (§5.1).
- **Lower order matched to the space order.** SSP-RK2 for the second-order and SSP-RK3 for
  the third-order LDF WLS-ENO scheme of [Liu et al. (2021)](/sources/liu-2021.md) (§3.3).
- **Ketcheson's low-storage SSP methods.** [Abgrall et al. (2022)](/sources/abgrall-2022.md)
  (§4) use SSPRK(3,3), SSPRK(5,4) and SSPRK(10,4) with their entropy-correction terms, applied
  at every stage, which give semi-discrete entropy conservation only; for a fully discrete
  entropy-conservative scheme they instead apply the correction to the whole space–time
  residual of a deferred-correction residual-distribution scheme (Remark 2.2, Eq. (19);
  [entropy correction terms](/methods/entropy-correction-term.md)).
- **Stiff sources.** [Du & Yang (2022)](/sources/du-2022-b.md) (§1) state that the SSP time
  stepping of earlier positivity-preserving schemes for reacting flows "limits the time step
  for stiff sources", and replace it by a third-order conservative modified exponential RK
  whose stages are convex combinations of a convective forward-Euler state and a source state;
  with $c=10^6$ in the artificial stiff source of their 1D accuracy test, SSP-RK3 at the same step returns NaN on 10
  and 20 cells and runs with $\tfrac25$ of it (Table 6.2;
  [asymptotic preservation](/properties/asymptotic-preservation.md)). Their convective CFL
  factor is $\min\alpha_{jl}/\beta_{jl}$ over the Shu–Osher-form coefficients (Thm. 4.3); *(compiler
  check, not in the sources: from the printed coefficients this is
  $\alpha_{21}/\beta_{21}=\alpha_{32}/\beta_{32}\approx0.793$)*.
- **Classical, non-SSP RK.** RK4 and, after a temporal convergence study, a second-order RK
  with a factor-two speed-up for the disturbance equations of
  [Browne et al. (2022)](/sources/browne-2022.md) (§4.1, §5, Table 6; the two statements of the
  integrator are inconsistent in the paper); the Jameson–Schmidt–Turkel four-step scheme at
  CFL 0.8 in the high-order WCNS of [Hiejima (2022)](/sources/hiejima-2022.md) (§2.2); the
  five-stage fourth-order low-storage RK of Carpenter and Kennedy in the DG of
  [Yu & Hesthaven (2022)](/sources/yu-2022.md) (§2.3); and "three-stage or four-stage
  Runge–Kutta", SSP not stated, at CFL 0.2 (two-phase Shu–Osher: 0.3 for $\mathbb P^0$, $\mathbb P^1$
  and 0.1 for $\mathbb P^3$) in the sharp-interface DG of
  [Bai & Li (2022)](/sources/bai-2022.md) (§2.2, Eq. (30)), whose CFL carries no
  degree-dependent factor.
- **More classical RK4.** In the two-phase kinetic-energy- and entropy-preserving scheme of
  [Jain & Moin (2022)](/sources/jain-2022.md) (§4), $\Delta t=\nu\min(\Delta x/c_1,\Delta x/c_2)$
  with $\nu\approx0.65$ ($c_1,c_2$ the phase sound speeds, page-local); a low-storage
  fourth-order RK at CFL 0.6 in the hybrid MDAD scheme of [Li et al. (2022a)](/sources/li-2022.md)
  (§4), cited to Shu's ENO/WENO lecture notes and not specified further.
- **Code-level integrators.** IDEFIX ([Lesur et al. (2023)](/sources/lesur-2023.md), §2.7–2.8,
  Table 1, Eq. (10)) offers forward Euler and the TVD RK2 and RK3 of Gottlieb and Shu, written
  as $u_{\mathrm s}=w_{\mathrm s}u^*+w^0_{\mathrm s}u^0$ with tabulated weights; the step
  $\Delta t=\nu\big(\max\big[\sum_d c_{\max,d}/\Delta x_d+2\eta_{\max}/\Delta x_d^2\big]\big)^{-1}$
  combines hyperbolic and parabolic limits pointwise ($c_{\max,d}$ the maximum signal speed,
  $\eta_{\max}$ the largest diffusion coefficient; page-local), stable for $\nu<1$; parabolic terms
  can instead use second-order Runge–Kutta–Legendre super time stepping, whose stage count grows
  like $2\sqrt{\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}}$ against $2\Delta t_{\mathrm{hyp}}/\Delta t_{\mathrm{par}}$
  for explicit RK2 (Eq. (13)).
- **Strang splitting around SSP-RK3.** The volume-penalization immersed boundary of
  [Kou et al. (2022)](/sources/kou-2022.md) (§4.1, Eqs. (20)–(22), (27)–(29)) advances the
  convective step with three-stage TVD-RK3 between two half-steps of the penalization source,
  which they solve by linearized backward Euler; explicit treatment of the source would need
  $\Delta t$ below the penalization time, Strang splitting relaxes this and the implicit forcing
  relaxes it further, by "about one or two orders of magnitude" in the penalization parameter
  for a given CFL, stated without a table (§4.6;
  [immersed boundaries](/methods/immersed-boundary-method.md)).
- **Second-order TVD RK.** [Hu et al. (2022)](/sources/hu-2022.md) (§5) pair it with
  second-order MUSCL at CFL 0.9 in 1D and 0.5 in the 2D interface-only problem; their linear
  carbuncle analysis is of one forward-Euler step ([carbuncle](/definitions/carbuncle-phenomenon.md)).
- **Not Runge–Kutta at all.** The [unstaggered central scheme](/methods/unstaggered-central-scheme.md)
  of [Kanbar et al. (2022)](/sources/kanbar-2022.md) is a single-step predictor–corrector in
  time (§3). The implicit [Quinpi](/methods/quinpi.md) scheme of
  [Puppo et al. (2023)](/sources/puppo-2023.md) uses a three-stage DIRK and takes explicit
  SSP-RK3 as its cost reference: one Quinpi step costs 2.5–3.1 SSP-RK3 steps on linear
  transport and 3.5–6.0 on Burgers (§4.5, Table 2). The Quinpi authors also build on
  the reading of a Runge–Kutta step as a combination of Euler steps, so that space
  limiting is needed only per Euler stage (§2).

## Qualifications

- **CFL bounds from TVD analysis.** [Deng (2023)](/sources/deng-2023.md) (§4.1, citing
  Giuliani & Krivodonova) states that the CFL $<0.5$ restriction from the TVD bound is "overly
  stringent when the high-order SSP-RK time scheme is adopted", and that four-stage
  second-order SSP-RK allows a larger CFL than three-stage third-order SSP-RK; the CFL and
  the RK variant of Deng's own tests are not stated.
- **Stage-wise hypotheses.** Transfer from forward Euler requires every stage to satisfy the
  forward-Euler hypotheses; in Wu & Shu's MHD scheme the limiter and the discrete
  divergence-free condition must hold at each stage, which is stated without a stage-wise
  argument (§6.2).
- [Huang et al. (2026)](/sources/huang-2026.md) report "3rd-order Runge–Kutta" at CFL 0.4
  without saying whether it is SSP.
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) print their SSP-RK3 stepper (Alg. 3,
  and the split version Alg. 4) without the factors $\tfrac14$ and $\tfrac23$ on the $\Delta t$
  terms of the second and third stages. *(compiler check, not in the sources: as printed, the
  linear test $u'=\lambda u$ gives $u^{n+1}=\big(1+\tfrac{11}6z+\dots\big)u^n$, $z=\lambda\Delta t$, so the
  printed scheme is not even first-order consistent; with the factors it is the Shu–Osher
  scheme above.)*
- **Two statements of the positivity CFL of SSP-RK3.** [Fan et al. (2021)](/sources/fan-2021.md)
  (§3.3) state that their forward-Euler positivity bound carries over to SSP-RK3 "if the
  CFL is one third" of it; [Wong et al. (2021)](/sources/wong-2021.md) (§5.3) state for
  the same integrator that the CFL upper limit is unchanged, and
  [Wu & Shu (2023)](/sources/wu-2023-b.md), [Cui et al. (2024)](/sources/cui-2024.md),
  [Pazner (2021)](/sources/pazner-2021.md) and [Fan et al. (2022)](/sources/fan-2022.md) (§3.5)
  transfer their forward-Euler results to SSP time stepping without stating any reduction. Both kinds of statement are sufficient
  conditions, so they do not contradict each other formally, but they disagree on what the
  convex-combination argument costs for the three-stage scheme; neither side prints the SSP
  coefficient it relies on. Fan et al.'s working step, $\Delta x/(12a)$ with $a$ the maximum
  of $\lvert v\rvert+c$, carries no factor one third and relies on halving and restarting.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5, Eq. (30) (arXiv v1).
- [Cui et al. (2024)](/sources/cui-2024.md) — Thm. 7.1, Remarks 7.7, 7.9, §7 (arXiv v1).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — §6.2 (arXiv v1).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) — §2 (Eqs. (26)–(27)), §5 (arXiv v2).
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §VII, §VIII, §IX, §X (Eqs. (10.1)–(10.7)).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4, §4.2, §4.5.
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §2, §5 (arXiv v2).
- [Wang et al. (2023b)](/sources/wang-2023-b.md) — Remark 1, §4.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.
- [Li et al. (2022b)](/sources/li-2022-b.md) — Eq. (38).
- [Luo & Wu (2021)](/sources/luo-2021-b.md) — numerical set-up.
- [Peng et al. (2024)](/sources/peng-2024.md) — §5 (arXiv v1).
- [Fu (2023)](/sources/fu-2023.md) — §3.4, Algorithms 1–2.
- [Abgrall & Barsukow (2023)](/sources/abgrall-2023.md) — §3.2, §5.3.
- [Deng (2023)](/sources/deng-2023.md) — §4.1.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.
- [Fan et al. (2021)](/sources/fan-2021.md) — §2 (Eq. (2.6)), §3.3 (Eq. (3.33)), §4.
- [Wong et al. (2021)](/sources/wong-2021.md) — §5.3, §6 (arXiv v1).
- [Pazner (2021)](/sources/pazner-2021.md) — Prop. 7, §5, §5.1 (arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — Thm. 6.1, §6.3, §7 (arXiv v3).
- [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md) — §5 (Eq. (89)), §6.1 (Fig. 5) (arXiv v1).
- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, §4.1 (Eqs. (39)–(40), Fig. 2), §4.4, §5.2 (arXiv v1).
- [Zheng et al. (2021)](/sources/zheng-2021.md) — §2.2.6 (Eq. (27)), Prop. 2.2, App. A, §4.
- [Li, Duan & Tang (2022c)](/sources/li-2022-c.md) — Remark 3.1, §5 (Eq. (5.1)) (arXiv v1).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §2 (Eq. (2.28)), §3 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.2 (Eq. (3.32)), §5.
- [Liu et al. (2021)](/sources/liu-2021.md) — §3.3.
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.3 (Eqs. (37)–(38)).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §3.3, §4.1.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.5 (Eq. (39)) (arXiv v1).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §2, §4.5 (Table 2) (arXiv v2).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3 (arXiv v1).
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4, App. A.5.
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — §3.1 (Eq. (26)), Thm. 3.1, §4 (arXiv v1).
- [Chu et al. (2022)](/sources/chu-2022.md) — §7.
- [Du, Shu & Zhong (2022)](/sources/du-2022.md) — §2.1 (Eq. (2.1)), §4.
- [Duan & Tang (2022)](/sources/duan-2022.md) — Prop. 3.2, §6 (Eq. (6.1)) (arXiv v1).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §2.3 (Eqs. (29)–(31)).
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §3.2, Apps. A (Algs. 3–4) (arXiv v3).
- [Abgrall et al. (2022)](/sources/abgrall-2022.md) — Remark 2.2, Eq. (19), §4 (arXiv v4).
- [Du & Yang (2022)](/sources/du-2022-b.md) — §1, §3.2, Thm. 4.3, §6.1 (Table 6.2).
- [Browne et al. (2022)](/sources/browne-2022.md) — §4.1, §5 (Table 6).
- [Hiejima (2022)](/sources/hiejima-2022.md) — §2.2.
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §2.3.
- [Bai & Li (2022)](/sources/bai-2022.md) — §2.2 (Eq. (30)).
- [Fan et al. (2022)](/sources/fan-2022.md) — §3.5 (Eq. (3.24), Alg. 2, Remarks 3.3–3.4), §5.
- [Fan et al. (2023)](/sources/fan-2023.md) — §2.2 (Eq. (2.6)), §3, App. A.
- [Hong et al. (2022)](/sources/hong-2022.md) — §5.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4 (Eq. (17)), §4.4.
- [Liang et al. (2022)](/sources/liang-2022.md) — §3, §4.5 (Fig. 15), §4.11.
- [Ji et al. (2022)](/sources/ji-2022.md) — Eq. (3), §5.
- [Jeong et al. (2022)](/sources/jeong-2022.md) — §5.
- [Li et al. (2023a)](/sources/li-2023.md) — numerical set-up.
- [Wan & Xia (2022)](/sources/wan-2022.md) — §4 (Eq. (4.1)).
- [Jain & Moin (2022)](/sources/jain-2022.md) — §4.
- [Li et al. (2022a)](/sources/li-2022.md) — §4.
- [Lesur et al. (2023)](/sources/lesur-2023.md) — §2.7–2.8 (Table 1, Eqs. (9)–(13)).
- [Kou et al. (2022)](/sources/kou-2022.md) — §4.1 (Eqs. (20)–(22), (27)–(29)), §4.6.
- [Hu et al. (2022)](/sources/hu-2022.md) — §3.1, §5.
- [Berta et al. (2024)](/sources/berta-2024.md) — §3.3 (Eqs. (31)–(32)), §5 (arXiv v4).
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §4 (Figs. 4, 9).
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — §3 (Eq. (3.10), Thm. 3.1), §5 (arXiv v1).
- [Yu, Liu & Feng (2023)](/sources/yu-2023.md) — §5 (arXiv v1).
- [Lin & Chan (2024)](/sources/lin-2024.md) — Eq. (52), footnote 7.
- [Teissier et al. (2024)](/sources/teissier-2024.md) — §3.6 (Eqs. (60)–(65), Table 1), §4.1 (Tables 2–3) (arXiv v2).
- [Fan et al. (2025a)](/sources/fan-2025.md) — §2.1 (Eq. (2.13)), §2.3 (Thms. 2.1–2.2, Eqs. (2.25)–(2.33)), §3.
- [Chu et al. (2025a)](/sources/chu-2025.md) — §4 (arXiv v1).
- [Chu et al. (2025b)](/sources/chu-2025-b.md) — §5.
- [Ding & Wu (2024a)](/sources/ding-2024.md) — Remark 2.2, §4 (arXiv v1).
- [Huang et al. (2025b)](/sources/huang-2025-b.md) — §2.1 (Eqs. (16)–(17)), §3.3.2, §4.2.1.
- [Liu & Wu (2025)](/sources/liu-2025.md) — §2.3, §3.2, §3.6, §4 (arXiv v2).
- [Liu et al. (2025b)](/sources/liu-2025-b.md) — §3.3 (Eqs. (3.20)–(3.21)), §4.
- [Liu et al. (2025c)](/sources/liu-2025-c.md) — §4.2 (fully discrete algorithm), §5 (time step).
- [Duan, Barsukow & Klingenberg (2025)](/sources/duan-2025.md) — §2.3 (Eqs. (14)–(15)), Remark 4.2, §5 (arXiv v3).
- [Barsukow et al. (2026)](/sources/barsukow-2026.md) — §4.2 (Eqs. (40)–(46), Table 3, Figs. 7–8), §5.1 (arXiv v2).
- [Chu et al. (2025c)](/sources/chu-2025-c.md) — §3 (arXiv v1).
- [Cao et al. (2026)](/sources/cao-2026.md) — §2.1, Eq. (26); §6.
