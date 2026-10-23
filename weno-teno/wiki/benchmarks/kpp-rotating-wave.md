---
type: Benchmark
title: "KPP rotating wave"
description: "Two-dimensional scalar conservation law with the nonconvex flux (sin u, cos u) and piecewise-constant data, whose entropy solution is a rotating spiral; high-order schemes that are non-oscillatory but not entropy stable converge to a wrong, nonentropic solution."
status: established
aliases: [KPP problem, Kurganov–Petrova–Popov problem, rotating wave problem]
tags: [benchmark, entropy-stable, dg, limiting]
timestamp: 2026-10-23T11:06:00Z
---

# KPP rotating wave

The KPP problem ("first introduced by Kurganov, Petrova, and Popov",
Rueda-Ramírez et al.; Kuzmin & Vedral cite the same paper) is the
scalar conservation law

$$
\partial_tu+\partial_x\sin u+\partial_y\cos u=0,
\qquad
u(x,y,0)=\begin{cases}7\pi/2, & x^2+y^2\le1,\\ \pi/4, & \text{otherwise},\end{cases}
$$

i.e. $f^{(1)}(u)=\sin u$, $f^{(2)}(u)=\cos u$, run to $t=1$. Kuzmin &
Vedral and Rueda-Ramírez et al. call the flux nonconvex, and the
entropy solution is a rotating spiral wave (a "composite wave
structure", Dzanic et al.). Its diagnostic value is that
oscillation control and entropy stability come apart: a scheme can be
free of overshoots and still converge to a nonentropic weak solution.
The four sources use it as a test of whether a shock-capturing device
selects the entropy solution of high-order schemes; see
[entropy stability](/properties/entropy-stability.md).

## Setups

| Source | Domain | Discretization | Grids |
|---|---|---|---|
| [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) §7.4, Eqs. (26)–(27) | $(-2,2)\times(-2.5,1.5)$ | continuous $\mathbb Q^p$ finite elements, $p\in\{1,2,4\}$, with [dissipation-based WENO stabilization](/methods/weno-stabilized-continuous-galerkin.md) | $N_h=129^2$ degrees of freedom |
| [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) §5.1, Eqs. (37)–(38) | $[-2,2]^2$ (boundary conditions not stated) | [DGSEM](/methods/dgsem.md), $N=3$, element-wise [subcell FV blending](/methods/subcell-finite-volume-limiting.md) with $\alpha_{\max}=0.5$ | $32^2$ to $256^2$ elements |
| [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) §5.1.2 | $[-2,2]^2$, periodic | flux reconstruction, $\mathbb P_9$, residual-based [artificial viscosity](/methods/artificial-viscosity.md), $c_\mu=6$ | $16^2$ to $64^2$ elements |
| [Lin & Chan (2024)](/sources/lin-2024.md) §4.1.2 | $[0,2]^2$ as printed; initial condition as in Rueda-Ramírez et al.; final time not printed | DGSEM, $N=3$, blended with the Hennemann et al. shock-capturing function, with and without their cell-entropy subcell limiter | $K_{1D}=64$ and $128$ elements per direction |

The domains differ: Kuzmin & Vedral shift the box downwards to
$y\in(-2.5,1.5)$, Rueda-Ramírez et al. and Dzanic et al. use the square
$[-2,2]^2$, the latter with periodic boundaries; Dzanic et al. write
the data as $3.5\pi$ and $\pi/4$.
Kuzmin & Vedral set the linear weights of all five candidates to 0.2
and the low-order viscosity factor $\lambda_e$ (page-local) to $2$ (instead of the bound
1) for this test, and run the plain Galerkin comparison with a lumped
mass matrix. Rueda-Ramírez et al. run it in [Trixi.jl](/software/trixi-jl.md).

## Agreement: absence of oscillations does not select the entropy solution

Kuzmin & Vedral and Rueda-Ramírez et al. show, with different methods,
that a high-order scheme can be non-oscillatory and still converge to
the wrong weak solution.

- **Kuzmin & Vedral.** Lumped-mass continuous Galerkin oscillates and
  produces an entropy-violating shock. A high-order stabilization alone
  reduces the oscillations but does not cure the lack of entropy
  stability. The low-order method and the WENO-stabilized scheme are
  non-oscillatory and reproduce the spiral entropy solution. The
  WENO-stabilized solution ranges are $[0.785,10.990]$ ($p=1$),
  $[0.785,10.983]$ ($p=2$) and $[0.778,10.980]$ ($p=4$), inside the
  initial range $[\pi/4,7\pi/2]=[0.785,10.996]$ except for a small
  undershoot at $p=4$, which the authors attribute to a cell-based
  indicator on a coarse mesh and state to vanish under refinement
  (Figs. 6–8).
- **Rueda-Ramírez et al.** DGSEM with its non-split volume term and
  shock capturing gives
  clean, essentially non-oscillatory but **nonentropic** solutions on
  every grid; its nonentropic wave structures even trigger the shock
  sensor. The entropy-stable split-form DGSEM, with the
  [entropy-conservative two-point flux](/methods/entropy-conservative-flux.md)
  for the square entropy $\eta=\tfrac12u^2$ in the volume
  ([flux differencing](/methods/flux-differencing.md)) and LLF at the
  surfaces, converges to the entropy solution with sharp interfaces
  (Figs. 2–3). They note that the DG cell entropy inequality for the
  square entropy would need exact integration, impossible for the
  non-polynomial KPP flux, which is why the split form is used.

The sources differ in what cures the defect. In Rueda-Ramírez et al.
blending with a first-order finite-volume method (element-wise, capped
at $\alpha_{\max}=0.5$) is not enough, and the cure is the entropy-stable
volume term, which carries a semi-discrete entropy argument. In Kuzmin &
Vedral the WENO-based nonlinear dissipation reproduces the entropy
spiral without an entropy proof; the authors add that entropy
inequalities can be enforced on top of it with algebraic flux
correction if necessary (§7.4). The two findings concern different
schemes and do not conflict; together they show that the benchmark
discriminates between stabilization mechanisms that all remove
oscillations.

A third mechanism passes the test. Dzanic, Trojak & Witherden's
artificial viscosity, computed from the defect of a forward–backward
time step (time reversibility fails at entropy-producing shocks), gives
the expected wave structure at $\mathbb P_9$ on $32^2$ elements with
sub-element resolution and no oscillations; the viscosity is localized
and "roughly proportional to the magnitude of the discontinuity", and
the solution converges qualitatively from $16^2$ to $64^2$ elements
(§5.1.2, Figs. 2–3). Like Kuzmin & Vedral's dissipation, the device
needs no entropy–flux pair and carries no entropy proof.

The fourth source isolates the same defect inside one scheme. Lin &
Chan (2024) show that DGSEM with Hennemann et al.'s blending converges
from $64^2$ to $128^2$ elements to a non-entropic solution, as
Rueda-Ramírez et al. found, and that adding their limiter, which
enforces a semi-discrete cell entropy inequality on the subcell fluxes
by a linear program for the limiting factors
([subcell limiting](/methods/subcell-finite-volume-limiting.md)),
makes the solution entropic (§4.1.2, Fig. 3).

## Qualifications

- Rueda-Ramírez et al. assert that the entropy-stable split form
  "ensures convergence to the unique entropic solution"; the paper
  proves a semi-discrete entropy inequality, not a convergence theorem,
  and shows the convergence numerically only *(compiler check, not in
  the sources)*.
- No source prints an error norm against a reference solution;
  the evidence is contour plots and solution ranges.
- Lin & Chan print the domain $[0,2]^2$ while taking the initial
  condition from Rueda-Ramírez et al., whose domain is $[-2,2]^2$; they
  print no final time, and their colour range $[-0.5,12]$ is wider than
  the initial range $[\pi/4,7\pi/2]$ *(compiler check, not in the
  sources)*.
- Dzanic et al. tune $c_\mu$ per problem (6 here, 1 to 8 elsewhere in
  the paper) and keep it fixed under refinement; they print no CFL
  number.

# Citations

- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §7.4, Eqs. (26)–(27), Figs. 6–8 (arXiv v1).
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.1, Eqs. (37)–(39), Figs. 2–3 (arXiv v2).
- [Dzanic, Trojak & Witherden (2022)](/sources/dzanic-2022.md) — §5.1.2, Figs. 2–3 (arXiv v2).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §3, §4.1.2, Fig. 3.
