---
type: Benchmark
title: "Flow past a cylinder (Schäfer–Turek)"
description: "The Schäfer–Turek two-dimensional time-dependent flow past a cylinder at Reynolds number 100, with John's reference maxima of drag 2.95 and lift 0.48: setup, the time integrators run on it (Radau IIA, Lobatto IIIC, Gauss, DIRK, adaptive BDF2 with explicit or linearized convection) and what each run showed."
status: established
aliases: [Schäfer–Turek benchmark, DFG cylinder benchmark, flow around a cylinder, 2D-3 benchmark, cylinder benchmark]
tags: [verification, implicit, stiff, dae]
timestamp: 2026-10-20T16:00:00Z
---

# Flow past a cylinder (Schäfer–Turek)

The **Schäfer–Turek flow past a cylinder** is a two-dimensional incompressible Navier–Stokes
benchmark with an unsteady inflow and periodic vortex shedding. Its quantities of interest are
the maximal drag and lift coefficients on the cylinder and the times at which they occur. The
four sources use it to check that a time integrator reproduces reference values, or converges
to them, on a realistic semi-discretized flow, an index-2 DAE in velocity and pressure (see
[differential-algebraic equations](/definitions/differential-algebraic-equation.md)). Three of
the four sources take their reference values from John (2004); the fourth computes its own on
its fixed mesh.

## Setup

The common setup ([Farrell et al. (2021)](/sources/farrell-2021.md), §4.4.1;
[Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md), §5.2;
[García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md), §4.2;
[Kirby & MacLachlan (2025)](/sources/kirby-2025.md), §4.2):

- **Domain.** $\Omega=(0,2.2)\times(0,0.41)$ minus the disc of radius $0.05$ centred at
  $(0.2,0.2)$.
- **Fluid.** Unit density, kinematic viscosity $10^{-3}$; Reynolds number 100 as Farrell et al.
  and Abu-Labdeh et al. state it (Kirby & MacLachlan's §4.2 does not state it).
- **Inflow.** At $x=0$,
  $u=\big(4U(t)\,y(0.41-y)/0.41^2,\,0\big)$ with $U(t)=1.5\sin(\pi t/8)$. García-Archilla & Novo
  and Kirby & MacLachlan write the same profile as $\frac6{0.41^2}\sin(\pi t/8)\,y(0.41-y)$.
- **Walls.** No-slip on the channel walls and on the cylinder.
- **Time.** $t\in[0,8]$, starting from rest.
- **Reference values** (John 2004, as quoted by García-Archilla & Novo):
  $c_{d,\max}=2.950921575$ at $t=3.93625$, $c_{l,\max}=0.47795$ at $t=5.693125$, and the
  pressure difference between the front and back of the cylinder $\Delta p(8)=-0.1116$.
  Abu-Labdeh et al. quote the maxima as 2.95 and 0.48; Farrell et al. compare their drag and lift
  with John's computation without printing the values.

**Outflow convention.** Farrell et al., Abu-Labdeh et al. and Kirby & MacLachlan impose a
no-stress condition at $x=2.2$. García-Archilla & Novo impose the inflow profile at the outflow too ("inflow = outflow",
§4.2). This is a different boundary condition. The reported maxima agree to the accuracy the
authors claim, but the setups are not identical.

## Runs reported

| Source | Space | Time integrator | Step | Result |
|---|---|---|---|---|
| Farrell et al. (2021), §4.4.1, Fig. 5 | Scott–Vogelius $P^4$/$P^3_{\mathrm{disc}}$, 14,640 curved cells, about 382k dofs | Radau IIA, 2 stages | $h=0.00125$ | "excellent agreement" with a Crank–Nicolson reference computation ($Q_2/P_1^{\mathrm{disc}}$, about 667k dofs, $h=1/1600$), with half the dofs and twice the step |
| Abu-Labdeh et al. (2023), §5.2, Tables 5–6, Fig. 3 | Taylor–Hood $P_2$–$P_1$, levels 3–6 (245k to 15.5M dofs per stage) | Radau IIA and Lobatto IIIC, 2 and 3 stages | $h=1/400$ | maximal drag 2.95 and lift 0.48 at every level; 1.35–2.70 Newton and 1.61–8.19 linear iterations per step; up to 46.6M dofs on 640 cores, 0.03–0.19 min per step |
| Abu-Labdeh et al. (2023), §5.2, Fig. 4 | as above | Gauss, 3 stages | $h=1/400$ | drag and lift "highly oscillatory" in time, even with a stricter nonlinear tolerance |
| Kirby & MacLachlan (2025), §4.2, Figs. 8–11 | Mardal–Tai–Winther velocity with piecewise-constant pressure, three-level mesh hierarchy, finest 12,800 curved cells | Radau IIA with 1–4 stages, Alexander's three-stage DIRK, WSODIRK433, WSODIRK744; stage-value formulation | $h=0.16$ down to $0.0025$ | own reference by Radau IIA(5) at the finest step on the same mesh: maximal drag about 2.89 at $t=3.93625$, maximal lift about 0.47 at $t=5.68875$ |
| García-Archilla & Novo (2023), §4.2, Figs. 6–9 | $P_2/P_1$ with grad-div parameter 0.01, 6624 cells, 27,168 velocity and 3480 pressure dofs | adaptive BDF1/BDF2 with explicit (IMEX) or linearized (semi-implicit) convection | adaptive, $\mathrm{TOL}_r=10^{-4},10^{-6},10^{-8}$ | IMEX at $10^{-4}$: relative errors 0.012 in maximal drag, 0.043 in maximal lift, below 0.0006 in their times, below 0.002 in $\Delta p(8)$ |

**What the runs show.**

- **Fully implicit Runge–Kutta at large steps.** Stiffly accurate, L-stable collocation methods
  ([fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md)) reproduce the reference
  maxima with steps 2 to 4 times larger than the Crank–Nicolson reference. Newton and linear
  iteration counts stay small across mesh levels, using monolithic multigrid with all stages in
  each patch (Abu-Labdeh et al. 2023; see [implicit stage solvers](/methods/implicit-stage-solvers.md)
  and [Irksome](/software/irksome.md)).
- **Fully implicit against diagonally implicit at equal cost.** With Newton–Krylov and monolithic
  geometric multigrid whose Vanka patches hold all stages, Newton and Krylov counts are stable in
  the number of stages; Radau IIA(3) costs slightly more than three times Radau IIA(1), Radau
  IIA(4) slightly less than four times, and a DIRK with $s$ stages runs almost as long as Radau
  IIA($s$). The Rana-type $LD$ stage preconditioner needs fewer iterations and is faster for
  Radau IIA(2) and (3), monolithic multigrid for Radau IIA(4). In accuracy per run time for the
  final drag and lift, Radau IIA(3) and (4) are best and WSODIRK744 is accurate but far more
  expensive (Kirby & MacLachlan 2025, §4.2, Figs. 8–9, 11; see
  [diagonally implicit Runge–Kutta](/methods/diagonally-implicit-runge-kutta.md) and
  [DIRK methods with high weak stage order](/methods/dirk-high-weak-stage-order.md)).
- **Stage order and the observed order.** Among the order-3 methods, Radau IIA(2) is slightly
  more accurate than Alexander's DIRK, which is slightly more accurate than WSODIRK433; the
  methods generally exceed the bound set by their stage order and reach their formal order in
  final drag and lift, except Alexander's DIRK on the maximal drag, and Radau IIA(1) (backward
  Euler) barely converges (Kirby & MacLachlan 2025, §4.2, Fig. 10). The authors had motivated
  the test by stage order governing accuracy for index-2 DAEs, so their own results qualify that
  premise (see [stage order](/definitions/stage-order.md) and
  [order reduction](/definitions/order-reduction.md)).
- **Lack of damping at infinity shows.** The Gauss oscillations are attributed by Abu-Labdeh et
  al. to the lack of L-stability: stiff modes with stability function near $-1$ decay slowly and
  alternate in sign (§5.2). This is a hypothesis of the authors, not a demonstration. See
  [A-stability](/properties/a-stability.md).
- **Step counts depend on how convection is treated.** For García-Archilla & Novo the step
  counts were 11,221, 21,187 and 93,671 for IMEX and 4,384, 19,885 and 92,086 for semi-implicit
  convection at the three tolerances. Only 53–92 matrix factorizations were needed in all runs,
  by iterative refinement with reused factorizations (§4.2). The IMEX steps coincide for
  tolerances $10^{-4}$ and $10^{-6}$ on $t\in[1.7,3.7]$ and are smaller than the semi-implicit
  ones. The authors read this as the step being limited by the CFL-type condition of explicit
  convection, not by accuracy (Fig. 8). See
  [IMEX linear multistep methods](/methods/imex-linear-multistep-methods.md) and
  [step-size control](/methods/step-size-control.md).

## Related problems that are not this benchmark

- **Turek–Hron FSI3.** [Taddei et al. (2026)](/sources/taddei-2026.md) (§5.2) use this
  fluid–structure benchmark: the same family of channel-and-cylinder geometries, with an elastic
  beam attached to the cylinder. On it, Radau IIA stays stable over long times, while
  [BDF2](/methods/backward-differentiation-formula.md) with an undamped
  [Newmark](/methods/newmark-method.md) structure is unstable (§5.2.1). Its quantities and
  reference values differ.
- **Compressible flow around a cylinder.** [Kemm (2024)](/sources/kemm-2024.md) (§4.2) tests
  explicit integrators for low-Mach Euler solvers on an annulus around a cylinder. It is a steady
  inviscid problem, unrelated to the Schäfer–Turek benchmark.

- **Compressible vortex shedding at $\mathrm{Re}_D=200$.** [Zeifang & Schütz (2022)](/sources/zeifang-2022.md)
  (§5.3.2, Fig. 11) run compressible Navier–Stokes past a cylinder of diameter 1 at
  $\mathrm{Re}_D=200$ (viscosity $5\times10^{-3}$, reference Mach number 0.1, free stream
  $\rho=1$, $v=(1,0)$, $\mathcal P=1/\kappa$ with $\kappa$ the ratio of specific heats;
  page-local) on 1000 DG elements of degree 5, with the implicit two-derivative
  predictor–corrector HBPC(6,2) at $h=0.1$ and $h=0.25$, about 200 and 500 times the step of
  an explicit fourth-order low-storage method. Strouhal numbers 0.1971 and 0.1968 against
  reference values 0.1957 and 0.196, and a lift history matching the explicit run, show that
  the large implicit steps keep the shedding (see
  [multiderivative Runge–Kutta](/methods/multiderivative-runge-kutta.md)). It is a different
  problem from the Schäfer–Turek benchmark: compressible, a free stream instead of a channel,
  and a periodic regime measured by the Strouhal number instead of drag and lift maxima.
- **Supersonic flow over a cylinder.** [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md)
  (§6.2.4, Table 1) run inviscid Mach 3 flow over a cylinder to $t=10$ with a single-stage
  Lax–Wendroff scheme of degree 4 on an adaptive mesh (561 to a peak of about 85,000
  elements). Error-based step-size control needs 1.51 times fewer steps than the best
  hand-tuned constant CFL number at tolerance $10^{-6}$ and 2.08 times fewer at
  $5\times10^{-6}$ (see [step-size control](/methods/step-size-control.md)). This is a shock
  problem with no relation to the Schäfer–Turek quantities.

- **Turbulent flow past a cylinder at $\mathrm{Re}=3900$.** [Pan et al. (2022)](/sources/pan-2022.md)
  (§3.4, Figs. 14–16, Table 2) run three-dimensional compressible implicit LES of the flow past
  a circular cylinder at $\mathrm{Re}=3900$ on 123,360 curved hexahedra with DG of degree 2,
  about 19 shedding periods, validated against experimental mean velocity profiles. Their
  error-balancing step-size controller (see [step-size control](/methods/step-size-control.md))
  with stiffly accurate ESDIRK2, 3 and 4 takes average steps 0.027, 0.043 and 0.127 against a
  fixed DIRK2 step of 0.010 (about CFL 40), at CPU times $7.9\times10^2$, $9.8\times10^2$ and
  $1.1\times10^3$ against $7.2\times10^2$ (ratios 1.09, 1.36, 1.53): the higher-order methods
  take larger steps but cost more overall. The element-wise step is smaller than the global one
  in fewer than 1 % of the elements. It is a different problem from the Schäfer–Turek
  benchmark: three-dimensional, turbulent, compressible, in a free stream, measured by mean
  profiles instead of drag and lift maxima.

## Qualifications

- **Versions read.** Farrell et al. (2021), Abu-Labdeh et al. (2023) and García-Archilla & Novo
  (2023) were read as arXiv preprints.
- **Abu-Labdeh et al.'s second reference.** They compare with "reference data" from two
  sources, one of which is the Irksome paper of Farrell et al. (2021).
- **Kirby & MacLachlan's reference values are mesh-specific.** Their maxima (drag about 2.89,
  lift about 0.47, lift maximum at $t=5.68875$) differ from John's (2.95, 0.48, $t=5.693125$)
  because they are computed with the spatial error frozen on their fixed mesh; they measure
  temporal error only and are not competing reference values. Their §4.2 does not state the
  Reynolds number. They avoid Taylor–Hood elements because these lose inf-sup stability when
  the step is decreased on a fixed mesh, as they state.
- **Figure number.** The text of Abu-Labdeh et al. says the Gauss figure is at level 3, while
  its caption says level 4 (recorded on the Source page).

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §4.4.1 (Figs. 4–5).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §5.2 (Tables 5–6, Figs. 3–4).
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §4.2 (Figs. 6–9).
- [Kirby & MacLachlan (2025)](/sources/kirby-2025.md) — §2 (Eqs. (2.11)–(2.14)), §4.2 (Figs. 6–11).
- [Pan et al. (2022)](/sources/pan-2022.md) — §3.4 (Figs. 14–16, Table 2; turbulent cylinder at Re 3900, as a related problem).
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §5.2, §5.2.1 (Turek–Hron FSI3, as a related benchmark).
- [Kemm (2024)](/sources/kemm-2024.md) — §4.2 (compressible cylinder, as a distinct problem).
- [Zeifang & Schütz (2022)](/sources/zeifang-2022.md) — §5.3.2 (Fig. 11; compressible cylinder at Re 200, as a related problem); arXiv v1.
- [Babbar & Chandrashekar (2025)](/sources/babbar-2025.md) — §6.2.4, Table 1 (Mach 3 cylinder, as a related problem); arXiv v4.
