---
type: Benchmark
title: "Taylor–Green vortex"
description: "Periodic vortex flow used to test time integrators on compressible-flow semidiscretizations: inviscid 3D at low Mach number as a stability-limited test for explicit pairs and step-size controllers, viscous 3D for optimized many-stage, semi-implicit and implicit two-derivative methods at large steps, and 2D steady at Mach numbers down to 10^-4 for the Mach scaling of IMEX schemes."
status: established
aliases: [TGV, Taylor-Green vortex, inviscid Taylor–Green vortex, Taylor–Green vortex at Re 1600, two-dimensional Taylor–Green vortex]
tags: [explicit, step-size-control, runge-kutta, stability, imex]
timestamp: 2026-10-20T10:00:00Z
---

# Taylor–Green vortex

The **Taylor–Green vortex (TGV)** is a three-dimensional periodic flow whose smooth initial
vortices stretch and break down into turbulence. In the sources it serves as a method-of-lines
test for explicit time integrators: the semi-discrete spectrum of a high-order DG-type
discretization makes the time step **stability-limited** for most of the run, so the benchmark
measures how far a method's stability region and its step-size controller let the step grow
([Ranocha et al. 2022](/sources/ranocha-2022.md), §5.1;
[Hedayati Nasab et al. 2021](/sources/hedayatinasab-2021.md), §7.2).

## Set-up

Page-local symbols: velocity $(v_1,v_2,v_3)$, pressure $\mathcal P$, density $\rho$, temperature
$\Theta$, Mach number $\mathrm{Ma}$, Reynolds number $\mathrm{Re}$.

**Inviscid, nondimensional** (Ranocha et al. 2022, §5.1, Eq. (5.3)). 3D compressible Euler on
the periodic cube $[-\pi,\pi]^3$:

$$\begin{aligned}
v_1&=\sin x_1\cos x_2\cos x_3,\qquad v_2=-\cos x_1\sin x_2\cos x_3,\qquad v_3=0,\\
\mathcal P&=1+\tfrac1{16}\bigl(\cos2x_1+\cos2x_2\bigr)\bigl(\cos2x_3+2\bigr),\qquad \Theta=1,
\end{aligned}$$

- $\mathrm{Ma}=0.1$;
- entropy-dissipative nodal DG spectral-element collocation with 8 elements per direction;
- final time 20, or 8 in the controller optimization.

**Viscous, dimensional** (Hedayati Nasab et al. 2021, §7.2, Eq. (29)). 3D compressible
Navier–Stokes on $[-\pi L,\pi L]^3$:

$$\begin{aligned}
v_1&=U_0\sin\tfrac xL\cos\tfrac yL\cos\tfrac zL,\qquad v_2=-U_0\cos\tfrac xL\sin\tfrac yL\cos\tfrac zL,\qquad v_3=0,\\
\mathcal P&=\mathcal P_0+\frac{\rho_0U_0^2}{16}\Bigl(\cos\tfrac{2x}L+\cos\tfrac{2y}L\Bigr)\Bigl(\cos\tfrac{2z}L+2\Bigr),\qquad \rho=\mathcal P/(R_{\mathrm g}\Theta_0),
\end{aligned}$$

- $\mathrm{Ma}=0.1$, $\mathrm{Re}=1600$ ($R_{\mathrm g}$ the gas constant, page-local);
- final time $20t_c$ with $t_c=L/U_0$;
- flux-reconstruction DG of degree 5 on hexahedra, prisms or tetrahedra, about $256^3$ solution
  points;
- checked against a reference spectral DNS (van Rees et al.).

**Inviscid, Cartesian and curved meshes** ([Ranocha et al. 2025](/sources/ranocha-2025.md),
§3, Eqs. (3.1)–(3.4)). The velocity field of Ranocha et al. (2022), $\rho=1$ and
$\mathcal P=1/(\kappa\mathrm{Ma}^2)+\tfrac1{16}(\cos2x_1\cos2x_3+2\cos2x_2+2\cos2x_1+\cos2x_2\cos2x_3)$
($\kappa=1.4$ the ratio of specific heats, page-local), $\mathrm{Ma}=0.1$, $8^3$ elements of
degree 3 with an entropy-conservative volume flux, $t\in[0,10]$, on a Cartesian mesh and on a
heavily curved one. The fluctuation is the same as in Ranocha et al. (2022); only the mean
pressure is normalized differently *(compiler check)*.

**Viscous, low Mach, semi-implicit** ([Boscheri & Pareschi 2021](/sources/boscheri-2021.md),
§4.5). The velocity of Ranocha et al. (2022) on $[-\pi,\pi]^3$, $\rho_0=1$,
$\mathcal P=\mathcal P_0+\frac{\rho_0}{16}(\cos2x_1+\cos2x_2)(\cos2x_3+2)$ with
$\mathcal P_0=10^3$ (a low Mach number), $\mathrm{Re}=100$ and $200$, $120^3$ cells, Courant
number 0.5 on the flow speed, final time 10.

**Two-dimensional, steady** ([Orlando et al. 2025b](/sources/orlando-2025-b.md), §4.1,
Eq. (75)). $\rho=1$, $v=(\sin x\cos y,-\cos x\sin y)$,
$\mathcal P=1+\frac{\mathrm{Ma}^2}4(\cos2x+\cos2y)$ on $(0,2\pi)^2$, periodic: a steady
incompressible Euler solution whose pressure fluctuation is scaled with the Mach number,
$\mathrm{Ma}=10^{-1},\dots,10^{-4}$, DG of degree 2 on $60^2$ elements, advective Courant
number about 0.095 (acoustic about $0.11/\mathrm{Ma}$); the final time is not printed.

The set-ups share the velocity and pressure fields up to scaling; they differ in viscosity,
normalization, dimension and element types.

**Three-dimensional, viscous, with AMR** ([Doehring et al. 2024b](/sources/doehring-2024-b.md),
§7.1.3). Compressible Navier–Stokes at $M=0.1$, $\mathrm{Re}=1600$, $\mathrm{Pr}=0.72$ on
$[0,2\pi]^3$, periodic, final time 20; DGSEM of degree 2 with HLLE and an entropy-conservative
volume flux, $16^3$ base cells and two refinement levels driven by an enstrophy indicator.

**Three-dimensional, viscous, implicit two-derivative** ([Zeifang & Schütz 2022](/sources/zeifang-2022.md),
§5.3.3). Compressible Navier–Stokes on the periodic cube $[0,2\pi]^3$, $\rho=1$,
$\mathcal P=\frac\rho{\kappa}+\frac{\rho\varepsilon^2}{16}(\cos2x+\cos2y)(\cos2z+2)$ ($\kappa$ the
ratio of specific heats, $\varepsilon$ their reference Mach number, whose value for this run is
not stated), $\mathrm{Re}=800$ (viscosity $1.25\times10^{-3}$), DG spectral elements of degree 3
on $32^3$ elements; the velocity is printed with a nonstandard first component (see
Qualifications).

## What it tests and results

**Stability-limited explicit pairs and controllers** (Ranocha et al. 2022). The step is mostly
stability-limited and the flow becomes turbulent. At $\mathrm{Ma}=0.1$ the negative real axis
of the stability region matters more than the rest of the advection spectrum; methods covering
more of it do better (§5.5.4). Right-hand-side evaluations at tolerance $10^{-5}$:

- **general-purpose pairs** (§5.5.1, Table 3): BS3(2)3F 5256, BS5(4)7F 7722, DP5(4)6F 8014,
  i.e. the third-order pair is about 50% more efficient when stability-limited;
- **SSP pair** (§5.5.2, Table 4): SSP3(2)4[3S\*$_+$] with controller $(0.55,-0.27,0.05)$ needs
  3438 against 5256/5261 for BS3(2)3F and SSP3(2)3 at loose and medium tolerances, but its cost
  grows sharply at tight tolerances;
- **new low-storage pairs** (§6.2): the third-order pairs are up to 5% better than
  KCL4(3)5[3R$_+$]C with optimized PID, and the fifth-order pairs up to 18% better than
  KCL5(4)9[2R$_+$]S with its prescribed controller;
- **controller tuning**: the TGV is one of the three problems in the brute-force PID search
  (§5.4; see [step-size control](/methods/step-size-control.md)).

**Error-based versus CFL control under a mesh change** (Ranocha et al. 2025, §3, Fig. 2). For
BS3(2)3F, RDPK3(2)5F[3S\*$_+$] and SSP3(2)4[3S\*$_+$], a range of tolerances spanning up to five
orders of magnitude gives the evaluation count of the best hand-tuned CFL factor; looser
tolerances can crash in the first steps (positivity), stricter ones enter the accuracy-limited
regime, earliest for the SSP pair. The optimal CFL factor is 55–74% larger on the curved mesh
(curved against Cartesian: 1.35 against 0.87 for BS3(2)3F, 2.67 against 1.71 for RDPK3(2)5F,
2.77 against 1.59 for the SSP pair), while the good tolerance range barely moves: the cost depends linearly on the CFL factor
and only roughly logarithmically on the tolerance.

**Optimized many-stage methods at Re 1600** (Hedayati Nasab et al. 2021, §7.2). A fourth-order,
16-stage method with an [optimal stability polynomial](/methods/optimal-stability-polynomial.md)
for the multidimensional element spectrum runs at 80% of its bisected maximal stable step.
Against the classical four-stage RK4 at the same fraction, the per-stage step ratios are:

| Elements | hexahedra | prisms | tetrahedra |
|---|---|---|---|
| speedup | 1.68 | 1.64 | 1.57 |

The kinetic-energy dissipation rate and enstrophy histories are visually indistinguishable,
and so are the Q-criterion isosurfaces at $t=15t_c$ (Figs. 8–10). The speedup is a ratio of
stage-normalized step sizes; no wall-clock time or hardware is reported.

**Dynamically partitioned P-ERK** (Doehring et al. 2024b, §7.1.3, Table 9). The three-member
third-order family P-ERK$_{3;\{3,4,6\}}$ is the fastest scheme, but the standalone P-ERK$_{3;6}$
is only 1.068 times slower, because most cells are refined during the run; the family is within
1.034 of a hypothetical optimal family. Partitioning costs 0.3 % of runtime and 7 % of memory
(§7). See [paired explicit Runge–Kutta](/methods/paired-explicit-runge-kutta.md).

[Southworth et al. (2022)](/sources/southworth-2022.md) mention that the Taylor–Green vortex
gave results similar to their double shear layer for implicit Runge–Kutta solvers, without
showing them (§7.2).

**Implicit steps 200 times the explicit limit** (Zeifang & Schütz 2022, §5.3.3, Fig. 12). The
fully implicit two-derivative Hermite–Birkhoff predictor–corrector HBPC(4,0) (fourth order,
no corrections; see [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)),
solved by Newton–GMRES with their extended block-Jacobi preconditioner, runs at $h=0.25$
against $h\approx1.25\times10^{-3}$ for an explicit fourth-order low-storage method, about 200
times larger. The kinetic-energy dissipation rate matches the explicit run and the DNS of Brachet
et al.; the peak near $t\approx9$ is slightly underestimated, which the authors attribute to
the coarse spatial resolution. No timings are reported for this run. See
[implicit stage solvers](/methods/implicit-stage-solvers.md).

**Semi-implicit all-Mach scheme** (Boscheri & Pareschi 2021, §4.5, Fig. 13). With the
[semi-implicit IMEX](/methods/semi-implicit-imex-runge-kutta.md) third-order finite-volume
scheme, the kinetic-energy dissipation rate $-\mathrm dK/\mathrm dt$ fits the Brachet et al.
DNS at $\mathrm{Re}=100$ and $200$ on a mesh the authors call coarser than second-order
solvers need; no error figures are given.

**Mach scaling of IMEX schemes** (Orlando et al. 2025b, §4.1, Tables 1–4, Fig. 2). The steady
2D vortex should keep density and pressure fluctuations of size $O(\mathrm{Ma}^2)$:

- Picard-iterated IMEX with the type-II third-order Kennedy–Carpenter pair: $\delta\mathcal P$
  scales as $O(\mathrm{Ma}^2)$ down to $10^{-4}$ ($L^2$ errors $1.57\times10^{-2}$,
  $1.57\times10^{-4}$, $1.57\times10^{-6}$, $1.62\times10^{-8}$), $\delta\rho$ down to $10^{-3}$
  with rate 1.1 at $10^{-4}$; $\nabla\cdot v$ stagnates at $1.82\times10^{-3}$, the
  interpolation error of the initial datum in the nodal DG space;
- semi-implicit IMEX with the same type-II pair is stable only down to $\mathrm{Ma}=10^{-3}$
  (density rate 0.6 there); with the type-I third-order pair it is stable at $10^{-4}$, but
  $\delta\rho$ stagnates at $1.68\times10^{-6}$, while IMEX with the type-I pair reaches
  $4.66\times10^{-9}$ (rate 1.5).

They conclude that low-Mach accuracy depends on the time-discretization strategy and on the
pair, with type-I pairs more stable; see
[IMEX Runge–Kutta methods](/methods/imex-runge-kutta.md).

## Qualifications

- The explicit-method uses measure cost at the linear stability limit on dissipative
  DG-type discretizations. The IMEX and semi-implicit uses run far beyond the acoustic limit
  and measure the Mach scaling of the fluctuations (Orlando et al. 2025b) or agreement with a
  DNS (Boscheri & Pareschi 2021); neither is an accuracy-limited step-size study.
- Zeifang & Schütz (2022, §5.3.3; *compiler check of the PDF*) print the initial velocity
  as $(\cos x\cos y\cos z,\,-\cos x\sin y\cos z,\,0)$, which is not divergence-free; the
  standard first component, used by the other sources, is $\sin x\cos y\cos z$. They print the
  dissipation rate as $\partial E_{\mathrm{kin}}/\partial t=\frac{2\mu}{\rho\lvert\Omega\rvert}\int\nabla v:\nabla v$
  without the minus sign that their positive plotted $-\partial E_{\mathrm{kin}}/\partial t$
  requires (page-local $E_{\mathrm{kin}}$, viscosity $\mu$, domain $\Omega$). Both are printed slips.
- Hedayati Nasab et al. write the snapshot time as "$t_c=15$"; $t=15t_c$ is meant (§7.2).

# Citations

- [Ranocha et al. (2022)](/sources/ranocha-2022.md) — §5.1 (Eq. (5.3)), §5.4, §5.5.1–5.5.4 (Tables 3–4), §6.2.
- [Hedayati Nasab et al. (2021)](/sources/hedayatinasab-2021.md) — §7.2 (Eq. (29), Figs. 8–10).
- [Southworth et al. (2022)](/sources/southworth-2022.md) — §7.2 (results mentioned, not shown).
- [Ranocha et al. (2025)](/sources/ranocha-2025.md) — §3 (Eqs. (3.1)–(3.4), Fig. 2).
- [Boscheri & Pareschi (2021)](/sources/boscheri-2021.md) — §4.5 (Fig. 13); arXiv v1.
- [Orlando et al. (2025b)](/sources/orlando-2025-b.md) — §4.1 (Eq. (75), Tables 1–4, Fig. 2); arXiv v5.
- [Doehring et al. (2024b)](/sources/doehring-2024-b.md) — §7, §7.1.3 (Table 9).
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) — §5.3.3 (Fig. 12); arXiv v1.
