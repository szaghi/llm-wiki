---
type: Benchmark
title: "Flow past a cylinder (Schäfer–Turek)"
description: "The Schäfer–Turek two-dimensional time-dependent flow past a cylinder at Reynolds number 100, with John's reference maxima of drag 2.95 and lift 0.48: setup, the time integrators run on it (Radau IIA, Lobatto IIIC, Gauss, adaptive BDF2 with explicit or linearized convection) and what each run showed."
status: established
aliases: [Schäfer–Turek benchmark, DFG cylinder benchmark, flow around a cylinder, 2D-3 benchmark, cylinder benchmark]
tags: [verification, implicit, stiff, dae]
timestamp: 2026-10-19T23:00:00Z
---

# Flow past a cylinder (Schäfer–Turek)

The **Schäfer–Turek flow past a cylinder** is a two-dimensional incompressible Navier–Stokes
benchmark with an unsteady inflow and periodic vortex shedding. Its quantities of interest are
the maximal drag and lift coefficients on the cylinder and the times at which they occur. The
three sources use it to check that a time integrator reproduces published reference values on a
realistic semi-discretized flow, an index-2 DAE in velocity and pressure (see
[differential-algebraic equations](/definitions/differential-algebraic-equation.md)). All three
take their reference values from John (2004).

## Setup

The common setup ([Farrell et al. (2021)](/sources/farrell-2021.md), §4.4.1;
[Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md), §5.2;
[García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md), §4.2):

- **Domain.** $\Omega=(0,2.2)\times(0,0.41)$ minus the disc of radius $0.05$ centred at
  $(0.2,0.2)$.
- **Fluid.** Unit density, kinematic viscosity $10^{-3}$, Reynolds number 100 as the sources
  state it.
- **Inflow.** At $x=0$,
  $u=\big(4U(t)\,y(0.41-y)/0.41^2,\,0\big)$ with $U(t)=1.5\sin(\pi t/8)$. García-Archilla & Novo
  write the same profile as $\frac6{0.41^2}\sin(\pi t/8)\,y(0.41-y)$.
- **Walls.** No-slip on the channel walls and on the cylinder.
- **Time.** $t\in[0,8]$, starting from rest.
- **Reference values** (John 2004, as quoted by García-Archilla & Novo):
  $c_{d,\max}=2.950921575$ at $t=3.93625$, $c_{l,\max}=0.47795$ at $t=5.693125$, and the
  pressure difference between the front and back of the cylinder $\Delta p(8)=-0.1116$. The other
  two sources quote the maxima as 2.95 and 0.48.

**Outflow convention.** Farrell et al. and Abu-Labdeh et al. impose a no-stress condition at
$x=2.2$. García-Archilla & Novo impose the inflow profile at the outflow too ("inflow = outflow",
§4.2). This is a different boundary condition. The reported maxima agree to the accuracy the
authors claim, but the setups are not identical.

## Runs reported

| Source | Space | Time integrator | Step | Result |
|---|---|---|---|---|
| Farrell et al. (2021), §4.4.1, Fig. 5 | Scott–Vogelius $P^4$/$P^3_{\mathrm{disc}}$, 14,640 curved cells, about 382k dofs | Radau IIA, 2 stages | $h=0.00125$ | "excellent agreement" with a Crank–Nicolson reference computation ($Q_2/P_1^{\mathrm{disc}}$, about 667k dofs, $h=1/1600$), with half the dofs and twice the step |
| Abu-Labdeh et al. (2023), §5.2, Tables 5–6, Fig. 3 | Taylor–Hood $P_2$–$P_1$, levels 3–6 (245k to 15.5M dofs per stage) | Radau IIA and Lobatto IIIC, 2 and 3 stages | $h=1/400$ | maximal drag 2.95 and lift 0.48 at every level; 1.35–2.70 Newton and 1.61–8.19 linear iterations per step; up to 46.6M dofs on 640 cores, 0.03–0.19 min per step |
| Abu-Labdeh et al. (2023), §5.2, Fig. 4 | as above | Gauss, 3 stages | $h=1/400$ | drag and lift "highly oscillatory" in time, even with a stricter nonlinear tolerance |
| García-Archilla & Novo (2023), §4.2, Figs. 6–9 | $P_2/P_1$ with grad-div parameter 0.01, 6624 cells, 27,168 velocity and 3480 pressure dofs | adaptive BDF1/BDF2 with explicit (IMEX) or linearized (semi-implicit) convection | adaptive, $\mathrm{TOL}_r=10^{-4},10^{-6},10^{-8}$ | IMEX at $10^{-4}$: relative errors 0.012 in maximal drag, 0.043 in maximal lift, below 0.0006 in their times, below 0.002 in $\Delta p(8)$ |

**What the runs show.**

- **Fully implicit Runge–Kutta at large steps.** Stiffly accurate, L-stable collocation methods
  ([fully implicit Runge–Kutta](/methods/fully-implicit-runge-kutta.md)) reproduce the reference
  maxima with steps 2 to 4 times larger than the Crank–Nicolson reference. Newton and linear
  iteration counts stay small across mesh levels, using monolithic multigrid with all stages in
  each patch (Abu-Labdeh et al. 2023; see [implicit stage solvers](/methods/implicit-stage-solvers.md)
  and [Irksome](/software/irksome.md)).
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

## Qualifications

- **Versions read.** Farrell et al. (2021), Abu-Labdeh et al. (2023) and García-Archilla & Novo
  (2023) were read as arXiv preprints.
- **Abu-Labdeh et al.'s second reference.** They compare with "reference data" from two
  sources, one of which is the Irksome paper of Farrell et al. (2021).
- **Figure number.** The text of Abu-Labdeh et al. says the Gauss figure is at level 3, while
  its caption says level 4 (recorded on the Source page).

# Citations

- [Farrell et al. (2021)](/sources/farrell-2021.md) — §4.4.1 (Figs. 4–5).
- [Abu-Labdeh et al. (2023)](/sources/abulabdeh-2023.md) — §5.2 (Tables 5–6, Figs. 3–4).
- [García-Archilla & Novo (2023)](/sources/garciaarchilla-2023.md) — §4.2 (Figs. 6–9).
- [Taddei et al. (2026)](/sources/taddei-2026.md) — §5.2, §5.2.1 (Turek–Hron FSI3, as a related benchmark).
- [Kemm (2024)](/sources/kemm-2024.md) — §4.2 (compressible cylinder, as a distinct problem).
