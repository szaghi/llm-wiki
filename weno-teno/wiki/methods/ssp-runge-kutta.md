---
type: Method
title: "SSP Runge–Kutta time stepping"
description: "Strong-stability-preserving Runge–Kutta methods are convex combinations of forward-Euler steps; this is why the bundle's bound-preserving, invariant-domain and limiter proofs need only forward Euler, and the three-stage third-order Shu–Osher scheme, at CFL numbers from 0.15 to 0.8, is the default stepper of its semi-discrete schemes."
status: established
aliases: [SSP-RK, SSP-RK3, TVD Runge–Kutta, TVD-RK3, Shu–Osher Runge–Kutta, strong-stability-preserving time integration]
tags: [bound-preserving, limiting, weno, dg]
timestamp: 2026-10-21T12:00:00Z
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

[Fu (2023)](/sources/fu-2023.md), [Cui et al. (2024)](/sources/cui-2024.md) (Exs. 2–5) and
the variants A and C of [Active Flux](/methods/active-flux.md)
([Abgrall & Barsukow (2023)](/sources/abgrall-2023.md), §§3.2, 5.3) use the same scheme; for
Active Flux the SSP-RK3 stability limits of the point-value formulas range from $\nu=0.45$ to
$1$ (variant A) and are $0.13$ (MD5) and $0.066$ (MD7) for variant C, with RK5 giving only a
slightly larger limit for FD5b.

## Why SSP: forward Euler suffices

- [Cui et al. (2024)](/sources/cui-2024.md) prove their bound-preserving DG theorems for one
  forward-Euler step and state that they hold for SSP time stepping (Thm. 7.1, footnote 2,
  Remark 7.9).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) state that bound preservation is retained with SSP
  Runge–Kutta "because SSP methods are convex combinations of forward Euler" (§6.2).
- [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) write their a posteriori
  limiter in forward-Euler FCT form on the same ground (§2, Eqs. (26)–(27)); see
  [convex limiting](/methods/convex-limiting.md).

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
