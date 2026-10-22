---
type: Benchmark
title: "Shock–bubble interaction"
description: "A planar shock hitting a circular region of different density or material, from the one-dimensional Euler analogue to the Mach 6 air–helium interaction and Baer–Nunziato and shallow-water variants; tests interface sharpness, robustness at material contrasts and the resolution of the vortical roll-up behind the shock."
status: established
aliases: [shock–bubble, shock-bubble interaction, shocked bubble]
tags: [benchmark, multiphase, interface-capturing, central-scheme]
timestamp: 2026-10-21T00:00:00Z
---

# Shock–bubble interaction

A planar shock travels through a uniform medium and hits a circular
(in one dimension, an interval) region whose density, and in multiphase
versions whose material, differs from its surroundings. The waves
refracted and reflected at the interface deform the bubble and roll it
up; the benchmark tests how sharply a scheme
keeps the interface, whether it survives the material contrast, and how
much of the roll-up it resolves. The sources use it in three quite
different settings.

## Euler and two-material Euler versions

**One-dimensional analogue.** [Chertock et al. (2023)](/sources/chertock-2023.md)
Ex. 1 run, on $[-1,1]$ with $\gamma=1.4$, a left-moving shock at
$x=0.75$ hitting a heavy "bubble" of radius $0.25$ at the origin:

$$
(\rho,v,p)(x,0)=\begin{cases}
(13.1538,\ 0,\ 1), & \lvert x\rvert<0.25,\\
(1.3333,\ -0.3535,\ 1.5), & x>0.75,\\
(1,\ 0,\ 1), & \text{otherwise},
\end{cases}
$$

solid wall on the left, free boundary on the right, $t=3$,
$\Delta x=1/100$, reference on $\Delta x=1/2000$, after a work they
list as in preparation. Their [LCD central-upwind scheme](/methods/lcd-central-upwind-scheme.md)
is "sharper and less oscillatory" than the earlier
[central-upwind scheme](/methods/central-upwind-scheme.md), which has
lower shock resolution and an oscillation at the contact (Fig. 5.1).

**Mach 6 air–helium interaction.** [Huang et al. (2026)](/sources/huang-2026.md)
§6.12, Eqs. (6.11)–(6.12), after a cited multiphase work: in
$(\rho,v_1,v_2,p,\gamma)$, pre-shock air $(1,0,0,1,1.4)$, post-shock air
$(5.268,5.752,0,41.83,1.4)$, helium $(0.138,0,0,1,1.667)$; the helium
bubble is given by the level set
$-0.025+\sqrt{(x-0.15)^2+(y-0.0445)^2}$, a circle of radius $0.025$
about $(0.15,0.0445)$; the shock starts at $x=0.1$;
domain $[0,0.356]\times[0,0.089]$, walls top and bottom, inflow left
and outflow right; multi-resolution grid with $L_{\max}=3$ levels and
finest $1024\times256$; snapshots at $t=0.006$, $0.012$, $0.018$,
$0.024$. [ROUND and LD-ROUND](/methods/round-scheme.md) are comparable to
WENO5-JS; ROUND is slightly more dissipative at the two later times and
LD-ROUND develops more complex vortical structures than WENO5-JS
(Fig. 17). The test is presented as evidence of robustness in
multiphase flow.

## Non-conservative multiphase and shallow-water versions

[Balsara et al. (2024)](/sources/balsara-2024.md) §IX use the geometry
for systems with non-conservative products, computed with their
[FD-WENO in fluctuation form](/methods/fluctuation-form-fd-weno.md):

- **Baer–Nunziato shock–bubble** (§IX.a, Table IX, Fig. 11; after
  Dumbser and co-workers): domain $[-0.5,3]\times[-0.75,0.75]$,
  $700\times300$ zones, CFL 0.4, $t=0.025$; phases with stiffened-gas
  parameters $(\gamma_1,\pi_1)=(3,100)$ and $(\gamma_2,\pi_2)=(1.4,0)$;
  bubble of radius $0.25$ at $(0.5,0)$ with solid volume fraction 0.25
  against 0.75 outside; shock at $x=0$, left state
  $(\rho_1,v_1,p_1,\rho_2,v_2,p_2,\phi_1)=(1999.939402,\ 49.998485,\ 4999849.5,\ 1,\ 0,\ 1,\ 0.75)$,
  right and bubble states $(1000,0,1,1,0,1,\phi_1)$; Dirichlet left and
  right, periodic top and bottom ($\phi_1$ is the solid volume fraction,
  page-local; $\pi_k$ the stiffened-gas constants, page-local).
- **Two-layer shallow-water shock–"bubble"** (§IX.c, Fig. 13) and
  **debris-flow shock–"bubble"** (§IX.e, Fig. 15), both new: the
  "bubble" is a smooth depression of the bottom,
  $b(r)=-0.25+0.25\tanh\big((r-0.25)/(2\Delta x)\big)$ (debris flow:
  amplitude 0.5) centred at $(0.5,0)$, hit by a bore at $x=0$;
  $700\times300$ (debris flow $700\times500$) zones, CFL 0.4, $t=0.30$.

Fifth and seventh order resolve the structures "much more crisply" than
third order, and the authors present the shallow-water and debris-flow
cases as genuinely new multidimensional tests (§IX).

## Qualifications

- The three settings share only the geometry; neither the equations
  nor the measures of success (interface sharpness in one dimension,
  roll-up in two-material Euler, order comparisons for non-conservative
  systems) carry over between them.
- Balsara et al. print the post-shock two-layer state with labels
  "$h_{1L},u_{1L},v_{1L},h_{1R},u_{1R},v_{1R}$" for what are the left
  states of both layers.
- All evidence is from contour plots; no source reports an error norm.

# Citations

- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.1, Ex. 1, Fig. 5.1 (arXiv v2).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.12, Eqs. (6.11)–(6.12), Fig. 17.
- [Balsara et al. (2024)](/sources/balsara-2024.md) — §IX.a, §IX.c, §IX.e, Table IX, Figs. 11, 13, 15.
