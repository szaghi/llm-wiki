---
type: Benchmark
title: "Korteweg–de Vries equation"
description: "The dispersive KdV equation u_t + 6uu_x + u_xxx = 0 and its generalized and linear variants; its third-derivative term makes explicit steps scale like Δx³, so the sources use it to test explicit–implicit–null stabilization and energy-relaxed IMEX methods on soliton and travelling-wave data."
status: established
aliases: [KdV equation, KdV, generalized KdV equation, Korteweg–de Vries]
tags: [verification, imex, structure-preserving, stiff]
timestamp: 2026-10-20T05:00:00Z
---

# Korteweg–de Vries equation

The Korteweg–de Vries (KdV) equation

$$u_t+6uu_x+u_{xxx}=0$$

is the model of weakly nonlinear dispersive waves; on a periodic domain it conserves
the mass $\int u$, the energy $\int\tfrac12u^2$ and the Whitham invariant
$\int(2u^3-u_x^2)$, and it has soliton solutions
([Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md), §6, Eqs. (32)–(33)). For time
integration its point is the third derivative: a semi-discretization has
$\lVert D_3\rVert=O(\Delta x^{-3})$ (page-local third-derivative matrix), so an
explicit method needs $h=O(\Delta x^3)$, and the sources treat the dispersive term
implicitly (§6) or through an implicitly treated linear surrogate
([Tan et al. (2022)](/sources/tan-2022.md), §1).

## Variants and data

* **Soliton data** (Biswas & Ketcheson 2023, §6, App. B): one soliton
  $u=\beta_1\operatorname{sech}^2\big(\sqrt{\beta_1}(x-2\beta_1t)/\sqrt2\big)$ with
  $\beta_1=1$ on $[-20,60]$, $N=512$, $t\in[0,20]$; two solitons ($\beta=0.5,1$) on
  $[-80,80]$, $N=1024$, $t\in[-25,25]$; three solitons ($\beta=0.4,0.7,1$) on
  $[-130,130]$, $N=1536$, $t\in[-50,50]$; steps $0.1$ or $0.01$ (page-local soliton
  amplitudes $\beta_j$). Space: the split-form Fourier semi-discretization of Ranocha,
  Mitsotakis & Ketcheson, which conserves discrete mass and energy for any $\Delta x$
  (Eqs. (34)–(35), as recalled).
* **Linear dispersion** $u_t+u_{xxx}=0$ with $u_0=\sin x$ on $(-\pi,\pi)$, $T=1$
  (Tan et al. 2022, §4.2.1, Eq. (4.8), Tables 4.11–4.12).
* **Generalized KdV** $u_t+(u^3)_x+(u(u^2)_{xx})_x=0$ with the travelling-wave solution
  $u=\sqrt{2\alpha}\cos((x-\alpha t)/2)$, $\alpha=0.1$, on $(-\tfrac32\pi,\tfrac52\pi)$ to
  $T=\pi$ (Tan et al. 2022, §4.2.1, Eq. (4.9), Tables 4.13–4.14), and a 2D version with
  $\alpha=0.5$ to $T=1$ (§4.2.2, Eq. (4.11), Tables 4.17–4.18;
  page-local wave speed $\alpha$). The dispersive term has a solution-dependent
  coefficient, so an implicit treatment of it would be nonlinear.
* **Zakharov–Kuznetsov**, a 2D relative with $u_{xxx}+u_{xyy}$ and a manufactured source
  (Tan et al. 2022, §4.2.2, Eq. (4.10), Tables 4.15–4.16).

Tan et al. use fourth-order central finite differences and $P^2$ local DG, periodic
data and $h=\Delta x$ throughout (§2.2, §4.2).

## What it shows

* **Explicit–implicit–null stabilization of dispersion.** Adding and subtracting
  $\vartheta\,c_{\max}\partial_x^3u$ (page-local: $\vartheta$ the stabilization ratio,
  $c_{\max}$ the largest coefficient of the third derivative, sign chosen by the wind
  direction) and treating only the added copy implicitly with ARS(4,4,3) gives linear
  constant-coefficient stage solves for the nonlinear equations. The numerical Fourier
  threshold $\vartheta\ge0.54$ is sharp on these tests: with $\vartheta=0.53$ the linear
  dispersive run explodes on fine meshes ($L^1$ error $1.01\times10^1$ for finite
  differences and $7.33\times10^2$ for DG at $N=1280$), while $\vartheta=0.54$ is third
  order with errors near $10^{-9}$ (Tan et al. 2022, §4.2.1, Tables 4.11–4.12); generalized
  KdV shows the same split between 0.53 and 0.54, with a mild error penalty for a large
  ratio ($\vartheta=10$), unlike on diffusion problems (Tables 4.13–4.14). See
  [explicit–implicit–null method](/methods/explicit-implicit-null-method.md).
* **Relaxation with IMEX methods and long-time error growth.** With the dispersive term
  implicit and the nonlinear term explicit in the Kennedy–Carpenter pairs ARK3(2)4L[2]SA
  and ARK4(3)6L[2]SA, energy relaxation reduces the maximal energy change on one soliton
  from $5.38\times10^{-2}$ and $1.05\times10^{-2}$ to about $10^{-15}$, and turns quadratic
  error growth into linear growth, as theory predicts for one soliton (Biswas & Ketcheson
  2023, §6.1.1, Table 1, Fig. 11). With two solitons the two relaxed methods grow
  sublinearly or between linearly and quadratically; with three, growth stays quadratic,
  though smaller, because the energy of each soliton drifts linearly, so mass and energy
  conservation do not guarantee linear error growth for multi-soliton data (§6.1.2–6.1.3,
  §7, Figs. 12–13). See [relaxation Runge–Kutta](/methods/relaxation-runge-kutta.md)
  and [IMEX Runge–Kutta](/methods/imex-runge-kutta.md).

## Qualifications

* Biswas & Ketcheson (2023) leave open why the two-soliton case does not show the
  three-soliton effect (§6.1.3).
* Tan et al. (2022) need the wind direction of the dispersive term to be fixed; a sign
  change inside a cell would need a spatially varying stabilization coefficient and a
  central flux, which they do not analyse (§2.2).

# Citations

- [Biswas & Ketcheson (2023)](/sources/biswas-2023-b.md) — §6 (Eqs. (32)–(39)), App. B, §6.1.1–6.1.3 (Table 1, Figs. 11–13), §7.
- [Tan et al. (2022)](/sources/tan-2022.md) — §1, §2.2, §4.2.1 (Eqs. (4.8)–(4.9), Tables 4.11–4.14), §4.2.2 (Eqs. (4.10)–(4.11), Tables 4.15–4.18).
