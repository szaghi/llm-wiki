---
type: Benchmark
title: "Isentropic vortex"
description: "Exact smooth solution of the compressible Euler equations, a vortex advected by a uniform stream or at rest, used to measure temporal convergence order, conservation and cost of time integrators: explicit pairs with PID control, fully implicit Runge–Kutta methods, paired and many-stage stabilized explicit methods, relaxation ADER-DG, and low-Mach IMEX and semi-implicit schemes."
status: established
aliases: [isentropic Euler vortex, convecting vortex, Shu vortex, travelling vortex, low-Mach isentropic vortex]
tags: [verification, runge-kutta, step-size-control, implicit, structure-preserving, imex]
timestamp: 2026-10-20T03:00:00Z
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

**Hedayati Nasab & Vermeire (2022), §5.1, Eq. (55)** (2D). With
$\phi=(1-x^2-y^2)/(2r_c^2)$ (page-local),

$$\rho=\Bigl(1-\frac{\Gamma^2\mathrm{Ma}_\infty^2(\kappa-1)e^{2\phi}}{8\pi^2}\Bigr)^{\frac1{\kappa-1}},\qquad
v_x=\frac{\Gamma y\,e^{\phi}}{2\pi r_c},\qquad v_y=1-\frac{\Gamma x\,e^{\phi}}{2\pi r_c},\qquad
\mathcal P=\frac{\rho^\kappa}{\kappa\mathrm{Ma}_\infty^2},$$

- $\Gamma=13.5$, $r_c=1.5$, $\mathrm{Ma}_\infty=0.4$, free stream along $y$;
- domain $[0,20]^2$, $20\times20$ quadrilaterals, flux reconstruction of degree 6, periodic top
  and bottom, Riemann-invariant sides, 40 passes of the vortex through the domain.

The same parameters ($\Gamma=13.5$, $r_c=1.5$, $\mathrm{Ma}_\infty=0.4$) are used by
[Doehring et al. (2024)](/sources/doehring-2024.md) (§10.2.2, Eqs. (10.12)–(10.16): free stream
$(1,1)$, domain $[-10,10]^2$, $64^2$ elements, DGSEM of degree 6 with HLLC flux, final time 20,
one traversal) and, "as in Vermeire", by [Doehring et al. (2025)](/sources/doehring-2025.md)
(§5.2: domain $[0,10]^2$, base $64^2$ elements with two or three levels of adaptive refinement,
DGSEM of degree 3 or 6, final time 20). [Gaburro et al. (2023)](/sources/gaburro-2023.md) use
Shu's vortex centred at $(5,5)$, periodic, final time 1, on unstructured triangles, without
restating the parameters (§5.3.1). [Doehring et al. (2024b)](/sources/doehring-2024-b.md) (§5)
take the parameters of the P-ERK papers on $[0,10]^2$ with $64^2$ base elements and two extra
AMR levels (finest cell $10/256$), DGSEM with HLLC flux, final time 20.

**Convected vortex for local time stepping.** [Sreejith et al. (2022)](/sources/sreejith-2022.md)
(§6.1) use a 2D convected vortex (called "isentropic, Rankine vortex"; strength 0.01556, radius
0.1 m, free stream 100 m/s, domain about $1.4\times0.6224$ m, periodic top and bottom,
characteristic inlet and outlet) on quadrilateral or triangular, uniform or stretched meshes, and
measure the pressure deviation of their LTS run from the single-rate run, not from an exact
solution.

**Low-Mach variants.** For [asymptotic-preserving](/definitions/asymptotic-preserving-scheme.md)
schemes the perturbations are scaled with the reference Mach number $\mathrm{Ma}$ so that
the pressure fluctuation is $O(\mathrm{Ma}^2)$ against an $O(1)$ background:

- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) (§5.1, Eqs. (96)–(97)): steady
  vortex, no free stream, tangential velocity of size $\mathrm{Ma}\frac{\Gamma}{2\pi}e^{(1-r^2)/2}$
  (printed as a scalar; Orlando et al. (2025b) multiply the same factor by the rotated
  position vector),
  $\Theta=1-\mathrm{Ma}^2\frac{\kappa-1}{\kappa}\frac{\Gamma^2}{8\pi^2}e^{1-r^2}$,
  $\rho=\Theta^{1/(\kappa-1)}$, $\mathcal P=\mathrm{Ma}^2\rho^\kappa$; $\Gamma=5$, domain
  $(-10,10)^2$ periodic, final time 10, DG of degree 2 or 3;
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) (§4.2, Eqs. (76)–(78)): "travelling
  vortex" with free stream $(1,1)$, $\Gamma=10$, $\mathcal P=1+\mathrm{Ma}^2\Theta^{\kappa/(\kappa-1)}$,
  domain $(-10,10)^2$ periodic, final time 3, $\mathrm{Ma}\in[10^{-4},10^{-1}]$, DG of degree
  1–3;
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) (§4.1, Eqs. (107)–(108)): a
  stationary "modified isentropic vortex" on $[0,10]^2\times[0,1]$, periodic, final time 1,
  meshes $16^2$–$128^2$, Courant number 0.9 on the material speed, with the stiffness
  parameter $\varepsilon\propto\mathrm{Ma}^2$ swept from 1 to $10^{-6}$; the vortex strength
  is not printed.

The sources normalize the vortex differently (temperature versus free-stream pressure
scaling, unit versus explicit core radius), so the strengths of Ranocha et al. (2022) and
Southworth et al. (2022) are not comparable as numbers with each other or with the
$\Gamma=13.5$ group. All are the same benchmark family; the exponent $e^{2\phi}$ of Hedayati
Nasab & Vermeire equals Southworth et al.'s $e^{\phi_{\mathrm v}}$ *(compiler check)*.

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

**Order verification of paired explicit methods.** Each member of the third-order
[P-ERK](/methods/paired-explicit-runge-kutta.md) family with 16 stages and $e=3,\dots,16$
active stages (page-local $e$: the number of active stages of a member; a family is listed
by the set of its members' $e$) converges at observed order 2.98–3.00 in the $L_2$ density error, and so does a
random spatial mix of all members; members with more active stages are more accurate at equal
step (e.g. $6.75\times10^{-8}$ for $e=3$ against $5.03\times10^{-10}$ for $e=10$ at
$h=2.5\times10^{-3}$) (Hedayati Nasab & Vermeire 2022, §5.1, Table 2). For the fourth-order
family, Doehring et al. (2025) use the vortex four ways (§4.3–5.3, §6.3):

- its spectrum ($8\times8$ elements, degree 3) is the target of the
  [stability-polynomial optimization](/methods/optimal-stability-polynomial.md), and the
  constrained polynomials reach about 85% ($e=6$) to 96.5% ($e=16$) of the unconstrained
  optimal step;
- on a three-level adaptive mesh with $e=\{6,10,16\}$ the mixed scheme has the errors of the
  standalone members to 4–5 digits ($L^1$ about $3.632\times10^{-7}$), and conservation errors
  of $10^{-13}$–$10^{-12}$, round-off only (Tables 2–3);
- at degree 6 the $L^1$ order is 3.99 before the spatial error takes over (1.71 at the next
  refinement; Table 4);
- on a four-level adaptive mesh with $e=\{5,7,11,19\}$, competing optimized fourth-order
  methods need 1.20–1.79 times the runtime and 1.38–2.08 times the evaluations (Table 6).

**Dynamically partitioned P-ERK.** On the AMR mesh Doehring et al. (2024b, §5, Tables 5–6,
Fig. 6) run the families P-ERK$_{2;\{3,6,12\}}$ (degree 2) and P-ERK$_{3;\{4,8,16\}}$ (degree 3),
with the partition reassigned at every mesh change. The families' density errors are those of
their standalone members ($L^1/|\Omega|$: $2.09\times10^{-5}$ against
$1.74$–$1.77\times10^{-5}$ at second order; $3.73\times10^{-7}$ against $4.05\times10^{-7}$ at
third order), orders 2 and 3 appear at degree 6 until the spatial error dominates, so no
interface order reduction is seen, and conservation errors are on par with SSPRK(3,3) (mass
$3.94\times10^{-13}$ against $7.82\times10^{-13}$). The same authors explain the absence of
interface oscillations in the random-mix test of Hedayati Nasab & Vermeire by the step
reduction the smallest member imposes, the third-order member with 3 active stages having a
stable step about 8 times smaller than the one with 16 (§3.2.6).

**Local time stepping** (Sreejith et al. 2022, §6.1, Fig. 18, Table 4). With the Lax–Wendroff
or TTGC scheme and step ratios 2, 5 and 10, the deviation from the single-rate solution is
similar on uniform and stretched meshes, lower on quadrilaterals than triangles and for TTGC than
Lax–Wendroff, and grows with the ratio; at ratio 10 the measured speedups are 1.92–2.21, 90–98 %
of the theoretical ones ([local time stepping](/methods/local-time-stepping.md)).

**Many-stage stabilized methods.** Doehring et al. (2024, §10.2.2, Table 6) run second-order
methods with 30, 60 and 120 stages and need Courant fractions 0.79, 0.65 and 0.40 of the
linearly predicted step, a reduction they attribute to the missing SSP property; the density
converges at second order in $L^\infty$ until the spatial error dominates. As a nonconvex
spectrum (degree 2, $8^2$ cells, Rusanov flux) the vortex lets the 28-stage polynomial reach
97.9% of the linearly scaled optimal step and the 56- and 112-stage ones all of it (§8).

**Entropy conservation with relaxation.** For ADER-DG of degrees 1–3 with entropy correction
and [relaxation](/methods/relaxation-runge-kutta.md), Gaburro et al. (2023, §5.3.1, Table 4,
Figs. 9–10) observe orders 2.01–2.03 (degree 1), 2.68–2.74 (degree 2) and 4.06–4.35 (degree 3),
errors "very close" to plain ADER-DG, total entropy conserved to machine precision against a
loss proportional to the accuracy without relaxation, and relaxation parameters $\gamma_n$ at
most about 1.02. See [ADER](/methods/ader-time-integration.md) and
[entropy stability](/properties/entropy-stability.md).

**Low-Mach IMEX and semi-implicit schemes.** The low-Mach variants test whether the order
survives as $\mathrm{Ma}\to0$ (asymptotic accuracy) with a step set by the flow speed:

- **Semi-implicit finite volumes.** Boscheri & Pareschi (2021, Tables 1–2) obtain
  $L^1$ orders 2.72, 2.95, 3.11 for density at $\varepsilon=1$ with the third-order scheme
  and the SA DIRK(3,4,3) pair (errors $7.68\times10^{-5}$ to $1.74\times10^{-7}$), and
  finest-level momentum orders 2.87–2.99 for $\varepsilon=10^{-1},\dots,10^{-6}$ with errors
  independent of $\varepsilon$ below $10^{-4}$; the second-order scheme gives 2.01–2.22. See
  [semi-implicit IMEX Runge–Kutta](/methods/semi-implicit-imex-runge-kutta.md).
- **IMEX-DG.** At $\mathrm{Ma}=10^{-3}$ and acoustic Courant number about 3.5, the
  third-order Kennedy–Carpenter pair with degree 2 gives $L^2$ rates 3.2, 3.0, 3.0 and the
  fourth-order Calvo–de Frutos–Novo pair with degree 3 gives 3.9, 3.9, 3.5 (Orlando &
  Bonaventura 2025, §5.1, Table 3). With the third-order pair, $\lVert\nabla\rho\rVert$ scales
  as $O(\mathrm{Ma}^2)$ down to $\mathrm{Ma}=10^{-5}$ and degrades at $10^{-6}$, and
  $\lVert\nabla\cdot u\rVert$ as $O(\mathrm{Ma})$; with the fourth-order pair the density
  scaling drops to $O(\mathrm{Ma})$ from $10^{-4}$, which the authors attribute partly to
  [order reduction](/definitions/order-reduction.md) (Tables 4–5).
- **IMEX against semi-implicit IMEX.** On the travelling vortex Orlando et al. (2025b, §4.2,
  Tables 5–15, Fig. 6) find the Picard-iterated IMEX and the semi-implicit methods equally
  accurate at second order (rate 1.2 at $\mathrm{Ma}=10^{-2}$ with degree 1, restored to 2.4
  with degree 2 for velocity), third order up to $\mathrm{Ma}=10^{-3}$ for all combinations
  except the semi-implicit method with the type-II pair, and saturation at
  $\mathrm{Ma}=10^{-4}$ for all; at fourth order the semi-implicit method with the type-II
  Kennedy–Carpenter pair has "severe issues" from $\mathrm{Ma}=10^{-3}$. The semi-implicit
  method is generally cheaper in wall-clock time, by about 5% at $\mathrm{Ma}=10^{-3}$.

## Qualifications

- Boscheri & Pareschi (2021, Eq. (107)) print the initial state with velocity $(1,1,0)$ and
  no vortex velocity perturbation, while calling the flow stationary with the initial state as
  exact solution; the standard vortex with zero background velocity is presumably meant.
  Their text promises $L^1$, $L^2$ and $L^\infty$ errors, but Table 1 reports $L^1$ only.
- Orlando et al. (2025b, Fig. 3 caption) plot $\mathcal P-(1-\mathrm{Ma}^2)$ where the
  background of Eq. (77) is $1+\mathrm{Ma}^2$ (Fig. 4 has the right sign).
- Southworth et al. call the rates of Table 2 "the expected rates", but Lobatto IIIC of orders 2
  and 4 fall visibly short at coarse steps (first rate 1.13 for order 2; 3.53 and 3.67 for order
  4), and Radau IIA 7 ends at 6.28.
- Southworth et al. print the $v$ perturbation with $-(x-x_0-\bar ut)$; for a rotating vortex
  whose $u$ perturbation carries $-(y-y_0-\bar vt)$, the $v$ perturbation needs
  $+(x-x_0-\bar ut)$ (reader's check; likely a printed sign slip, p. 17). The final time of their
  convergence runs is not printed.
- Hedayati Nasab & Vermeire (2022) centre the vortex at the origin in Eq. (55) while the
  domain is $[0,20]^2$, and their Table 2 prints some step sizes as $5.000\times10^{-2}$ where
  the halving sequence and the observed orders require $5.000\times10^{-3}$.
- Sreejith et al. (2022) call their vortex an "isentropic, Rankine vortex"; a Rankine vortex
  is not the smooth isentropic vortex of the other sources, and their reference is the
  single-rate solver, so their figures measure the LTS coupling error only. Their Table 4 case 4
  prints node counts identical to case 1 with a different theoretical speedup (reader's check).
- The degree-2 ADER orders of Gaburro et al. (2023) stay near 2.7 rather than 3, and their
  order claim for relaxed ADER is inherited from a theory proved for Runge–Kutta and multistep
  methods (see the relaxation page).

# Citations

- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5.2 (Eq. (5.4)), §5.4, §6.1 (Fig. 6), §6.2.
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §7.1.1 (Tables 2–4).
- [Hedayati Nasab & Vermeire (2022)](/sources/hedayatinasab-2022.md) — §5.1 (Eq. (55), Table 2).
- [Doehring et al. (2024)](/sources/doehring-2024.md) — §8, §10.2.2 (Eqs. (10.12)–(10.16), Table 6).
- [Doehring et al. (2025)](/sources/doehring-2025.md) — §4.3, §5.2–5.4 (Tables 2–4), §6.3 (Table 6).
- [Gaburro et al. (2023)](/sources/gaburro-2023.md) — §5.3.1 (Table 4, Figs. 9–10); arXiv v1.
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §4.1 (Eqs. (107)–(108), Tables 1–2); arXiv v1.
- [Orlando & Bonaventura (2025)](/sources/orlando-2025.md) — §5.1 (Eqs. (96)–(97), Tables 3–5); HAL v2.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §4.2 (Eqs. (76)–(78), Tables 5–15, Fig. 6); arXiv v5.
- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §3.2.6, §5 (Tables 5–6, Fig. 6).
- [Sreejith et al. (2022)](/sources/sreejith-2022.md) — §6.1 (Tables 3–4, Fig. 18).
