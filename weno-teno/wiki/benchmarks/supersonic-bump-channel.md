---
type: Benchmark
title: "Supersonic flow over a circular-arc bump"
description: "Steady inviscid Mach 1.4 flow through a channel of length 3 and height 1 with a 4% circular-arc bump on the lower wall, whose leading- and trailing-edge shocks reflect and interact; used to test multi-block shock-capturing closures and shock-adapted meshes."
status: established
aliases: [supersonic bump, supersonic channel bump, 4% bump, circular-arc bump channel]
tags: [benchmark, finite-difference, dg, shock-tracking]
timestamp: 2026-10-23T11:06:00Z
---

# Supersonic flow over a circular-arc bump

A channel of length 3 and height 1 carries a steady inviscid flow at inlet Mach number
$M=1.4$. On its lower wall sits a circular-arc bump of chord 1 and height 4% of the chord.
The flow turns at the leading edge of the bump through an oblique shock, expands over the
arc and turns back through a second shock at the trailing edge; the shocks reflect from
the walls and interact downstream, so the steady field holds several shocks, their
reflections and their intersections. Both walls are slip
walls; the inlet is supersonic and the outlet supersonic, so all inflow data are prescribed
and nothing is imposed at the outlet. The shallow-water bump of the
[flow over a bump](/benchmarks/flow-over-a-bump.md) page is a different problem.

## Geometry

Let $a_{\mathrm b}=0.5$ be the half-chord and $c_{\mathrm b}=0.04$ the height of the bump
(page-local), centred at $x=0$. [Qin et al. (2023)](/sources/qin-2023.md) (§3.5.3, Eq. (42))
print the arc as part of the circle of radius $R_{\mathrm b}=\sqrt{a_{\mathrm b}^2+b_{\mathrm b}^2}$
centred at $(0,-b_{\mathrm b})$, $b_{\mathrm b}=(a_{\mathrm b}^2-c_{\mathrm b}^2)/(2c_{\mathrm b})$,
with half-angle $\Phi=\arcsin(a_{\mathrm b}/R_{\mathrm b})$, and map the block above the bump
from computational coordinates $(s_1,s_2)\in[0,1]^2$ (page-local) by

$$\begin{aligned}
x&=(1-s_2)R_{\mathrm b}\sin\theta+s_2\,(-0.5+s_1),\\
y&=(1-s_2)\big(-b_{\mathrm b}+R_{\mathrm b}\cos\theta\big)+s_2,\qquad\theta=(2s_1-1)\Phi .
\end{aligned}$$

The circle passes through the bump ends $(\pm a_{\mathrm b},0)$ and its top $(0,c_{\mathrm b})$
because $R_{\mathrm b}=b_{\mathrm b}+c_{\mathrm b}$; with $a_{\mathrm b}=0.5$ and
$c_{\mathrm b}=0.04$ these give $b_{\mathrm b}=3.105$, $R_{\mathrm b}=3.145$, and the map sends $s_2=0$ to the arc and
$s_2=1$ to the upper wall $y=1$ *(compiler check, not in the sources)*.

## Setups

| Source | Grid | Method | Run, output |
|---|---|---|---|
| [Qin et al. (2023)](/sources/qin-2023.md) §3.5.3 | three blocks, interfaces at $x=\pm0.5$ (the bump ends), $160\times160$ points per block | fifth-order WCNS-MR finite differences with shock-capturing block closures | four-order residual drop; 30 pressure contours 0.458–1.478 (Fig. 13); $p$ along $y=0.4$ (Fig. 14) |
| [Nguyen et al. (2024)](/sources/nguyen-2024.md) §3.5 | isoparametric elements of degree $k=4$, moved by optimal transport | HDG with artificial viscosity | illustration of the six steps of their adaptation algorithm (Fig. 1); no quantitative output |

Both sources state the same channel, bump and Mach number and cite earlier work for the
case; neither prints $\gamma$ for it.

## Findings

**Multi-block closures.** A single block body-fitted to the bump has metric singularities at
the leading and trailing edges, and a weak horseshoe vortex can develop behind the bump
because of the metric jumps there, as Qin et al. recall from the literature. Their three-block
grid puts the block interfaces at the bump ends, $x=\pm0.5$, and uses their
[shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md) for the
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md) at the
interfaces. The shocks are sharp and unhindered by the interfaces, no spurious vortex
appears, and the pressure along $y=0.4$ matches the single-domain solution and a cited
reference (§3.5.3, Figs. 12–14).

**Mesh adaptation.** Nguyen et al. use the bump only to show, step by step, how their
optimal-transport map clusters the elements of a fixed-connectivity mesh along the shocks
before the [artificial viscosity](/methods/artificial-viscosity.md) is reduced on the adapted
mesh ([adaptive moving mesh](/methods/adaptive-moving-mesh.md)); the quantitative tests of the
method are the [NACA 0012](/benchmarks/naca0012-airfoil.md) and the hypersonic
[cylinder](/benchmarks/flow-past-circular-cylinder.md) flows.

## Qualifications

- Neither source reports an error norm on this case; Qin et al.'s evidence is a pressure cut
  compared with other solutions, Nguyen et al.'s a sequence of meshes and fields.

# Citations

- [Qin et al. (2023)](/sources/qin-2023.md) — §3.5.3, Eq. (42), Figs. 12–14.
- [Nguyen et al. (2024)](/sources/nguyen-2024.md) — §3.5, Fig. 1 (arXiv v1).
