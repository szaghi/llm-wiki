---
type: Benchmark
title: "Isentropic vortex"
description: "Exact smooth solution of the compressible Euler equations, a vortex advected by a uniform stream, used to measure temporal convergence order and accuracy-limited cost of time integrators: explicit embedded pairs with PID control and fully implicit Runge–Kutta methods with block preconditioning."
status: established
aliases: [isentropic Euler vortex, convecting vortex, Shu vortex]
tags: [verification, runge-kutta, step-size-control, implicit]
timestamp: 2026-10-19T00:00:00Z
---

# Isentropic vortex

The **isentropic vortex** is an exact solution of the compressible Euler equations: an
isentropic vortex, steady in its own frame, translated by a uniform free stream. Because the
exact solution is known at all times, it measures temporal accuracy and observed order without
a reference run. It is the accuracy-relevant counterpart of the stability-limited
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
([Ranocha et al. 2022](/sources/ranocha-2022.md), §5.2;
[Southworth et al. 2022](/sources/southworth-2022.md), §7.1.1).

## Set-up

Page-local symbols: ratio of specific heats $\kappa=1.4$ (the registry reserves $\gamma$),
vortex strength $\Gamma$, core radius $r_c$, free-stream Mach number $\mathrm{Ma}_\infty$,
temperature $\Theta$, density $\rho$, pressure $\mathcal P$, tangential velocity $v_\theta$,
distance $r$ from the vortex centre.

**Ranocha et al. (2022), §5.2, Eq. (5.4)** (citing Shu 1997). 3D, on the periodic cube
$[-5,5]^3$, with the vortex axis $(1,1,0)$ not aligned with the grid:

$$\Theta=1-\frac{(\kappa-1)\mathrm{Ma}_\infty^2\Gamma^2}{8\kappa\pi^2}e^{1-r^2},\qquad
v_\theta=\frac{r\Gamma}{2\pi}e^{(1-r^2)/2},\qquad \rho=\Theta^{1/(\kappa-1)},$$

- $\mathrm{Ma}_\infty=0.5$, $\Gamma=5$, free-stream temperature 1;
- 8 elements per direction to $t=4$ in the controller optimization, 20 elements to $t=20$
  otherwise.

**Southworth et al. (2022), §7.1.1** (2D). Domain $[0,20]\times[-7.5,7.5]$, vortex centre
$(x_0,y_0)$ advected at angle $\varphi=\arctan\tfrac12$ (page-local) with speed $U_\infty=1$,
$(\bar u,\bar v)=U_\infty(\cos\varphi,\sin\varphi)$. With
$\phi_{\mathrm v}=\bigl(1-(x-x_0-\bar ut)^2-(y-y_0-\bar vt)^2\bigr)/r_c^2$ (page-local),

$$\rho=\rho_\infty\Bigl(1-\frac{\Gamma^2(\kappa-1)\mathrm{Ma}_\infty^2}{8\pi^2}e^{\phi_{\mathrm v}}\Bigr)^{\frac1{\kappa-1}},\qquad
\mathcal P=\mathcal P_\infty\Bigl(1-\frac{\Gamma^2(\kappa-1)\mathrm{Ma}_\infty^2}{8\pi^2}e^{\phi_{\mathrm v}}\Bigr)^{\frac{\kappa}{\kappa-1}},$$

and Cartesian velocity perturbations of size $\frac{\Gamma}{2\pi r_c}e^{\phi_{\mathrm v}/2}$
times the rotated distance from the moving centre.

- $\Gamma=15$, $r_c=1.5$, $\mathrm{Ma}_\infty=0.5$, $\rho_\infty=1$;
- degree-4 DG with Roe flux on 532 structured triangles.

The two sources normalize the vortex differently (temperature versus free-stream pressure
scaling, unit versus explicit core radius), so their strengths are not comparable as numbers.
Both are the same benchmark family.

## What it tests and results

**Accuracy-limited explicit control** (Ranocha et al. 2022). Unlike the Taylor–Green vortex,
accuracy can limit the step at tight tolerances (§5.2).

- **Controller tuning.** It is one of the three problems in the brute-force PID search. In this
  accuracy-relevant regime, larger $\beta_1$ and $\beta_2$ closer to zero, i.e. controllers
  close to the deadbeat I controller, perform best. The controller chosen for RK3(2)5F[3S\*$_+$]
  is within 3.1% of the minimal cost (§6.1, Fig. 6; see
  [step-size control](/methods/step-size-control.md)).
- **New pairs.** RK3(2)5[3S\*$_+$] is up to 13% cheaper than KCL4(3)5[3R$_+$]C with optimized
  PID, and the new fifth-order pairs up to 35% cheaper than KCL5(4)9[2R$_+$]S with its
  prescribed controller (§6.2; see [low-storage methods](/methods/low-storage-runge-kutta.md)).

**Order verification of fully implicit methods** (Southworth et al. 2022, §7.1.1, Table 2).
Reference: explicit RK4 with $h=5\times10^{-5}$; steps $h=2.5,1.25,0.625\times10^{-2}$. Observed
orders at the finest refinement:

| Method (order) | observed |
|---|---|
| Gauss 2 / 4 / 6 | 2.07 / 4.07 / 5.99 |
| Radau IIA 3 / 5 / 7 | 2.90 / 4.91 / 6.28 |
| Lobatto IIIC 2 / 4 / 6 | 1.88 / 3.67 / 5.83 |

**Solver cost** (Southworth et al. 2022, $h=2\times10^{-2}$, Table 3; preconditioner applications
per step):

| Family | orders | cost |
|---|---|---|
| SDIRK | 1 / 2 / 3 / 4 | 20 / 26 / 45 / 59 |
| Gauss | 2 / 4 / 6 / 8 / 10 | 15 / 36 / 103 / 162 / 169 |
| Radau IIA | 3 / 5 / 7 / 9 | 44 / 121 / 168 / 205 |

Gauss 2 and 4 beat SDIRK of equal order. The optimal Schur-complement shift roughly halves, or better,
the Krylov iterations of the high-order methods (Table 4; see
[implicit stage solvers](/methods/implicit-stage-solvers.md)).

## Qualifications

- Southworth et al. call the rates of Table 2 "the expected rates", but Lobatto IIIC of orders 2
  and 4 fall visibly short at coarse steps (first rate 1.13 for order 2; 3.53 and 3.67 for order
  4), and Radau IIA 7 ends at 6.28.
- Southworth et al. print the $v$ perturbation with $-(x-x_0-\bar ut)$; for a rotating vortex
  whose $u$ perturbation carries $-(y-y_0-\bar vt)$, the $v$ perturbation needs
  $+(x-x_0-\bar ut)$ (reader's check; likely a printed sign slip, p. 17). The final time of their
  convergence runs is not printed.

# Citations

- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5.2 (Eq. (5.4)), §5.4, §6.1 (Fig. 6), §6.2.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §7.1.1 (Tables 2–4).
