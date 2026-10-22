---
type: Method
title: "SSP Runge–Kutta time stepping"
description: "Strong-stability-preserving Runge–Kutta methods are convex combinations of forward-Euler steps, so bound-preserving, invariant-domain and limiter proofs need only forward Euler; the three-stage third-order Shu–Osher scheme, mostly at CFL numbers 0.3 to 0.6, is the default stepper of the bundle, and the page records how sources size time steps and state the positivity CFL."
status: established
aliases: [SSP-RK, SSP-RK3, TVD Runge–Kutta, TVD-RK3, Shu–Osher Runge–Kutta, strong-stability-preserving time integration]
tags: [bound-preserving, limiting, weno, dg]
timestamp: 2026-10-22T12:00:00Z
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
([Li et al. (2022)](/sources/li-2022-b.md), [Luo & Wu (2021)](/sources/luo-2021-b.md),
[Wang & Don (2022)](/sources/wang-2022-b.md), citing Gottlieb & Shu 1998). CFL numbers used
with it:

| Source | Scheme | CFL $\nu$ |
|---|---|---|
| [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) | DGSEM with subcell limiting | 0.5 (blending recomputed every stage, §5) |
| [Li et al. (2022)](/sources/li-2022-b.md) | FD WENO-ZN, 1D | 0.5 (Eq. (38)) |
| [Wang et al. (2023)](/sources/wang-2023-b.md) | A-WENO with CURH flux | 0.45; $\Delta x^{2/3}$ in the accuracy test (Remark 1) |
| [Wang & Don (2022)](/sources/wang-2022-b.md) | FD affine-invariant WENO | 0.45 (§3) |
| [Fu (2021)](/sources/fu-2021.md), [Takagi et al. (2022)](/sources/takagi-2022.md) | FD TENO, TENO-THINC | 0.4 (0.35 for the blast waves in Takagi et al.) |
| [Chertock et al. (2023)](/sources/chertock-2023.md) | central-upwind FV | 0.4 |
| [Balsara et al. (2024)](/sources/balsara-2024.md) | fluctuation-form FD-WENO | 0.3 (2D accuracy), 0.4 (2D problems), 0.8 (1D problems) |
| [Wu & Shu (2023)](/sources/wu-2023-b.md) | BP locally divergence-free DG, MHD | 0.15 |
| [Peng et al. (2024)](/sources/peng-2024.md) | OEDG, discontinuous tests | $1/(2N+1)$ |
| [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) | moment-based multi-resolution HWENO | 0.6 (1D and 2D) |
| [Wang et al. (2021)](/sources/wang-2021.md) | FD multi-resolution WENO | 0.6; 0.3 for the viscous shock tube |
| [Wong et al. (2021)](/sources/wong-2021.md) | positivity-preserving WCNS, gas–liquid | 0.5 |
| [Zheng et al. (2021)](/sources/zheng-2021.md) | conservative two-medium A-WENO | 0.5; $\Delta t=O(\Delta x^{5/3})$ in the accuracy tests |
| [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) | ninth-order central scheme with adaptive dissipation | 0.5 (Taylor–Green), 0.02 (reacting shock tube) |
| [Pazner (2021)](/sources/pazner-2021.md) | sparse IDP DG with subcell convex limiting | half the IDP bound $\min_im_i/(2\lvert\hat d_{ii}\rvert)$, printed with $\hat d_{ii}$ (§3.2, §5; see below) |
| [Li, Duan & Tang (2022)](/sources/li-2022-c.md) | entropy-stable moving-mesh FD | 0.4 (2D), 0.3 (3D); $\Delta t=\nu(\min\Delta\xi)^{5/3}$ in the accuracy tests ($\Delta\xi$ the computational spacing) |
| [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) | weakly compressible two-phase solver | 0.4 on the acoustic speed, with viscous, surface-tension and phase-field limits (Eq. (38)) |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) | unstructured CWENO, multicomponent | 0.1 in the convergence test, others not printed |
| [Fan et al. (2021)](/sources/fan-2021.md) | positivity-preserving FV hybrid HWENO, Navier–Stokes | $\Delta t=\min\{\Delta x/(12a),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$, halved on failure (below) |
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) | MFC, FV WENO with HLLC | not stated; RK orders 1 to 5 available |

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
redistribution near a material interface stay conservative. *(Compiler check, not in the
sources: expanding the Shu–Osher form above gives exactly these two lines.)*

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
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) (Remark 3.1) quote free-stream
  preservation of the fully discrete moving-mesh scheme with SSP-RK3 as proved in the
  companion paper of Duan & Tang, not in the paper itself.

## Sizing the time step

- **For accuracy tests.** A third-order integrator caps the observed order of a higher-order
  spatial scheme unless $\Delta t$ shrinks faster than $\Delta x$.
  [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) (§4.1, Eqs. (39)–(40), Fig. 2)
  model the error as $C_\tau\Delta t^{3}+C_h\Delta x^{9}$ and explain why the observed order
  of their ninth-order scheme on the [isentropic vortex](/benchmarks/isentropic-vortex.md)
  varies between 3 and 9: keeping the ratio of the two errors fixed needs
  $\Delta t\propto\Delta x^{3}$, while a constant CFL gives $\Delta t\propto\Delta x$; ninth
  order appears over $100^2$–$500^2$ only for CFL $1.25\times10^{-2}$ and $6.25\times10^{-3}$.
  [Zheng et al. (2021)](/sources/zheng-2021.md) and [Li, Duan & Tang (2022)](/sources/li-2022-c.md)
  take $\Delta t\propto\Delta x^{5/3}$ for fifth order; Zheng et al.'s accuracy budget at the
  interface moreover needs $\Delta t=O(\Delta x^r)$ with $r\le2$, because a low-order
  interface flux there is recovered by dividing by $\Delta t/\Delta x$ (Prop. 2.2, App. A).
  [Wang et al. (2021)](/sources/wang-2021.md) report fifth order at CFL 0.6 without a
  reduction.
- **Adaptively, for positivity.** [Fan et al. (2021)](/sources/fan-2021.md) (§3.3, Eq. (3.33))
  start from $\Delta t=\min\{\Delta x/(12a),\ 0.001\,\mathrm{Re}\,\Delta x^2\}$ ($a$ the
  maximum of $\lvert v\rvert+c$; *compiler check, not in the sources: $1/12$ equals the
  boundary Gauss–Lobatto weight $\hat\omega=1/(N(N-1))$ of their decomposition for the
  four-point rule*) and, if any stage cell average leaves the admissible set, halve $\Delta t$
  and restart the step from the first stage; their theorems guarantee termination. The
  viscous bound $O(\mathrm{Re}\,\Delta x^2)$ is needed in addition, since the positivity
  bound is only $O(\Delta x)$.
- **DG step formulas.** [Rueda-Ramírez et al. (2021)](/sources/ruedaramirez-2021.md)
  (§5, Eq. (89)) take $\Delta t=\min\big(\mathrm{CFL}\,\beta^a(N)\Delta x/(\lambda^a_{\max}(2N+1)),\ \mathrm{CFL}_\nu\beta^\nu(N)\Delta x^2/(\lambda^\nu_{\max}(2N+1)^2)\big)$
  with empirical factors $\beta^a,\beta^\nu$ (page-local) and CFL $=$ CFL$_\nu=0.5$.

## Other SSP methods and refinement rules

- Higher order in time: the fourth-order SSP-RK of Spiteri & Ruuth
  ([Balsara et al. (2024)](/sources/balsara-2024.md), §VII); a five-stage fourth-order SSP-RK
  for the $t=2000$ advection run of [Takagi et al. (2022)](/sources/takagi-2022.md) (§4.2);
  SSP **multistep** methods of order $N+1$ for $\mathbb P^N$-DG, with SSP coefficients $1/3$
  (four-step third order), $\approx0.282$ (ten-step fifth), $\approx0.217$ (eighteen-step
  seventh) and $0.1$ (22-step ninth) in [Cui et al. (2024)](/sources/cui-2024.md) (§7, Ex. 1).
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
- **Two statements of the positivity CFL of SSP-RK3.** [Fan et al. (2021)](/sources/fan-2021.md)
  (§3.3) state that their forward-Euler positivity bound carries over to SSP-RK3 "if the
  CFL is one third" of it; [Wong et al. (2021)](/sources/wong-2021.md) (§5.3) state for
  the same integrator that the CFL upper limit is unchanged, and
  [Wu & Shu (2023)](/sources/wu-2023-b.md), [Cui et al. (2024)](/sources/cui-2024.md) and
  [Pazner (2021)](/sources/pazner-2021.md) transfer their forward-Euler results to SSP time
  stepping without stating any reduction. Both kinds of statement are sufficient
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
- [Wang et al. (2023)](/sources/wang-2023-b.md) — Remark 1, §4.
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.
- [Li et al. (2022)](/sources/li-2022-b.md) — Eq. (38).
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
- [Li, Duan & Tang (2022)](/sources/li-2022-c.md) — Remark 3.1, §5 (Eq. (5.1)) (arXiv v1).
- [Li, Shu & Qiu (2022)](/sources/li-2022-d.md) — §2 (Eq. (2.28)), §3 (arXiv v1).
- [Wang et al. (2021)](/sources/wang-2021.md) — §3.2 (Eq. (3.32)), §5.
- [Liu et al. (2021)](/sources/liu-2021.md) — §3.3.
- [Matsushita & Aoki (2021)](/sources/matsushita-2021.md) — §3.3 (Eqs. (37)–(38)).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §3.3, §4.1.
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §4.5 (Eq. (39)) (arXiv v1).
- [Puppo et al. (2023)](/sources/puppo-2023.md) — §2, §4.5 (Table 2) (arXiv v2).
- [Kanbar et al. (2022)](/sources/kanbar-2022.md) — §3 (arXiv v1).
