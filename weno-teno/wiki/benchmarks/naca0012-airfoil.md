---
type: Benchmark
title: "NACA 0012 airfoil"
description: "Inviscid flow past the symmetric NACA 0012 airfoil, above all the transonic case at Mach 0.8 with a strong upper-surface and a weak lower-surface shock, plus subsonic and supersonic cases, used to test unstructured WENO, shock-adapted artificial-viscosity DG and multi-block shock-capturing closures by surface pressure."
status: established
aliases: [NACA0012, NACA 0012, transonic NACA 0012, NACA0012 airfoil]
tags: [benchmark, weno, dg, finite-difference]
timestamp: 2026-10-23T11:06:00Z
---

# NACA 0012 airfoil

The NACA 0012 is a symmetric airfoil of 12% thickness. Its inviscid flow at a small angle of
attack $\alpha$ is a steady test of shock-capturing schemes on body-fitted or
unstructured grids. In the transonic case, free-stream Mach number $M_\infty=0.8$ at
$\alpha\approx1.25^\circ$–$1.5^\circ$, a supersonic pocket on the upper surface ends in a
strong normal shock, and a weaker shock stands on the lower surface. Schemes are compared by
the surface pressure coefficient $C_p$ (page-local), its sharpness and freedom from overshoot
at the two shocks, and by Mach or pressure contours. Subsonic cases test smooth accuracy
around the body, and supersonic cases add a detached bow shock ahead of the leading edge. The
steady state is reached by time marching to a residual drop or by an implicit steady solver.

## Setups

| Source | Case | Grid, domain | Method | Output |
|---|---|---|---|---|
| [Lin & Zhu (2024)](/sources/lin-2024-b.md) Case 3.10 | $M_\infty=0.8$, $\alpha=1.25^\circ$ | 9340 triangles, circumcircle diameters 0.0031–1.4188, domain $[-15,15]^2$ | finite-volume ALW-MR-WENO, orders 3–5, characteristic-wise, CFL 0.6 | pressure distributions (Fig. 3.19), 30 Mach contours 0.172–1.325 (Fig. 3.20) |
| Lin & Zhu Case 3.11 (conditions "specified in" Zhu & Shu's steady-state work) | (1) $M_\infty=0.5$, $\alpha=1.25^\circ$; (2) $M_\infty=2.0$, $\alpha=1^\circ$; (3) $M_\infty=3.0$, $\alpha=5^\circ$ | as Case 3.10 | as above | pressure contours: 30 levels 0.88–1.16; 30 levels 0.76–5.35; 60 levels 0.76–11.35 (Figs. 3.21–3.26) |
| [Nguyen et al. (2024)](/sources/nguyen-2024.md) §4.1 | $M_\infty=0.8$, $\alpha=1.5^\circ$ | slip wall on the airfoil, far field elsewhere; element count not stated | HDG, degree $k=4$, artificial viscosity, three optimal-transport adapted meshes | $C_p$ on the three meshes (Figs. 2–4) |
| [Qin et al. (2023)](/sources/qin-2023.md) §3.5.4 | $M_\infty=0.8$, $\alpha=1.25^\circ$ | $240\times100$ nodes in three blocks, far field at 50 chords; interfaces at the upper-surface point nearest $x=0.1$, the lower-surface point nearest $x=-0.14$ and along $y=0$ | fifth-order WCNS-MR with shock-capturing block closures, run to a four-order residual drop | 30 pressure contours 0.37–1.05 (Fig. 16), $C_p$ (Fig. 17) |

None of the three sources prints $\gamma$ for this case. Nguyen et al. take the case from
their own earlier work, Qin et al. compare with a cited reference solution, and Lin & Zhu
compare their adaptive-linear-weight schemes with the multi-resolution WENO schemes of the
same group on the same mesh. Nguyen et al.'s angle $1.5^\circ$ differs from the $1.25^\circ$
of the other two: the runs are of the same family, not of the same flow.

## Findings

**Unstructured WENO with two stencils.** Lin & Zhu's ALW-MR-WENO schemes reconstruct on
triangles from a one-cell stencil and one large stencil, with linear weights adapted by a
troubled-cell rule ([multi-resolution WENO](/methods/multi-resolution-weno.md),
[CWENO](/methods/cweno.md)). On all four airfoil cases they "can provide good resolution" and
give results similar to MR-WENO of the same order (Figs. 3.19–3.26), at lower cost: on Case
3.11(2) the fifth-order run takes 100764.83 s against 167994.37 s for MR-WENO, a ratio of 0.60
(Table 3.1; no hardware stated). The comparison is visual; no error or force coefficient is
printed.

**Shock-adapted meshes for artificial viscosity.** Nguyen et al. move the nodes of a fixed
mesh by an optimal-transport (Monge–Ampère) map so that elements cluster at the shocks, and
add [artificial viscosity](/methods/artificial-viscosity.md) whose amplitude and width are
reduced by a homotopy on the final mesh
([adaptive moving mesh](/methods/adaptive-moving-mesh.md)). The $C_p$ profiles converge
rapidly: the second and third adaptive meshes give very similar profiles, and the third is
"very sharp at the shocks, yet there is no oscillation and overshoot" (§4.1, Figs. 2–4).

**Block interfaces through the shocks.** Qin et al. place the block interfaces of their
multi-block grid so that they cut both the upper and the lower shock, a partition that "is
surely to be avoided" with traditional closures. With their
[shock-capturing boundary closures](/methods/shock-capturing-boundary-closure.md) for the
[weighted compact nonlinear scheme](/methods/weighted-compact-nonlinear-scheme.md), the
discontinuities are captured accurately and $C_p$ coincides with the single-domain result and
is "comparable to" the cited reference (§3.5.4, Figs. 15–17). The airfoil here is a test of
interface treatment, not of the interior scheme.

**Viscous variants elsewhere.** Viscous NACA 0012 flows, at low Reynolds numbers and other
angles, are recorded with [hp-adaptation](/methods/hp-adaptation.md), the
[immersed boundary method](/methods/immersed-boundary-method.md), the
[gas-kinetic scheme](/methods/gas-kinetic-scheme.md),
[RBF differential quadrature](/methods/rbf-differential-quadrature.md) and
[WENO limiters for DG](/methods/weno-limiter-dg.md).

## Qualifications

- All three sources judge the transonic case by plots of $C_p$ or contours; none prints lift,
  drag or an error against a reference.
- Lin & Zhu's Case 3.11 text says that "the single NACA0012 airfoil configuration is shown in
  Case 3.11", i.e. in itself; the configuration and the mesh are those of Case 3.10.

# Citations

- [Lin & Zhu (2024)](/sources/lin-2024-b.md) — §3 (CFL, characteristic reconstruction), Cases 3.10–3.11, Table 3.1, Table 3.4, Figs. 3.19–3.26.
- [Nguyen et al. (2024)](/sources/nguyen-2024.md) — §2.2–§2.4, §3, §4.1, Figs. 2–4 (arXiv v1).
- [Qin et al. (2023)](/sources/qin-2023.md) — §3.5.4, Figs. 15–17.
