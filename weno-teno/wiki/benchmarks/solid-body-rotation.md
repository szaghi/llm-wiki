---
type: Benchmark
title: "Solid-body rotation"
description: "LeVeque's two-dimensional linear-advection test in which a smooth hump, a cone and a slotted cylinder rotate rigidly for one revolution; the exact solution is the initial data, so L1 errors and the solution range measure dissipation and bound violations of limited high-order schemes; smooth rotations test order on adaptive grids, and LeVeque's swirling deformation tests positivity limiting."
status: established
aliases: [LeVeque solid body rotation, slotted cylinder test, hump–cone–slotted-cylinder rotation]
tags: [benchmark, limiting, bound-preserving, dg]
timestamp: 2026-10-23T20:30:00Z
---

# Solid-body rotation

The scalar linear advection equation $\partial_tu+\nabla\cdot(vu)=0$ on
$[0,1]^2$ with the rigid rotation $v=2\pi\,(\tfrac12-y,\ x-\tfrac12)$
carries three bodies of radius $0.15$ once around the centre of the
domain in $t=1$; the speed $2\pi$ times the distance from the centre
gives a period of one *(compiler check, not in the sources)*. After one
revolution the exact solution equals the initial data, so the test
measures how a scheme handles a smooth profile, a kink and a
discontinuity at once: the $L^1$ error measures dissipation, and the
range of the computed solution against $[0,1]$ measures over- and
undershoots, a [bound-preservation](/properties/bound-preservation.md)
test for the scalar maximum principle. Pazner, Kuzmin & Vedral and
Ji, Liang & Fu attribute it to LeVeque, and so do Maltsev et al. and
Vilar & Abgrall; one source rotates a Jiang–Shu-type set of four
profiles, and two more rotate a single smooth profile for different
purposes.

## Setup

[Pazner (2021)](/sources/pazner-2021.md) §5.4 and
[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) §7.3 print the same
data. With $r$ the distance to a body's centre divided by $0.15$, and
$u=0$ outside the three disks:

- smooth hump centred at $(0.25,0.5)$: $u=\tfrac14\big(1+\cos(\pi r)\big)$;
- cone centred at $(0.5,0.25)$: $u=1-r$;
- slotted cylinder centred at $(0.5,0.75)$: $u=1$ if $|x-0.5|\ge0.025$ or
  $y\ge0.85$, and $u=0$ in the slot.

[Ji, Liang & Fu (2022)](/sources/ji-2022.md) §5.3 print the same three
bodies (their SB01–SB03, radius $r_0=0.15$) with the unscaled rotation
$v=(\tfrac12-y,\ x-\tfrac12)$, so one revolution takes $t=2\pi$, and with
periodic boundaries; the two velocity scalings give the same solution
at the end of one revolution *(compiler check, not in the sources)*.
[Maltsev et al. (2023)](/sources/maltsev-2023.md) §3.2 print the same
bodies, centres and radius with the unscaled rotation
$v=(0.5-y,\ x-0.5)$ to $t_f=2\pi$, but state the domain as "again a
$[0,10]\times[0,10]$ square"; the rotation centre $(0.5,0.5)$, the body
centres and $r_0=0.15$ place the bodies in the unit square, as in the
other sources *(compiler check, not in the sources)*.
[Vilar & Abgrall (2024)](/sources/vilar-2024.md) §4.1.2 (HAL preprint)
run the same three bodies with $v=(\tfrac12-y,\ x-\tfrac12)$ to $t=2\pi$.

## Runs and results

| Source | Scheme | Mesh | Degrees of freedom | $L^1$ error | Range |
|---|---|---|---|---|---|
| Pazner (2021) §5.4 | unlimited DG, $N=3$ | $64\times64$ | $256^2$ | $1.0\times10^{-2}$ | $[-0.21,\ 1.16]$ |
| Pazner (2021) | low-order invariant-domain-preserving DG | $64\times64$ | $256^2$ | $8.5\times10^{-2}$ | $[0,\ 0.66]$ |
| Pazner (2021) | subcell flux-corrected (convex-limited) DG, $N=3$ | $64\times64$ | $256^2$ | $1.1\times10^{-2}$ | $[0,\ 1]$ |
| Kuzmin & Vedral (2023) §7.3 | standard CG, $\mathbb Q^1$ | uniform | $129^2$ | $3.70\times10^{-2}$ | globally oscillatory |
| Kuzmin & Vedral (2023) | CG with high-order (HO) stabilization only, $\mathbb Q^1$ | uniform | $129^2$ | $1.47\times10^{-2}$ | large over/undershoots at the slotted cylinder |
| Kuzmin & Vedral (2023) | CG with low-order (LO) artificial viscosity, $\mathbb Q^1$ | uniform | $129^2$ | $1.10\times10^{-1}$ | non-oscillatory, very diffusive |
| Kuzmin & Vedral (2023) | [WENO-stabilized CG](/methods/weno-stabilized-continuous-galerkin.md), $\mathbb Q^1$ | uniform | $129^2$ | $2.68\times10^{-2}$ | $[-0.001,\ 0.993]$ |
| Kuzmin & Vedral (2023) | WENO-stabilized CG, $\mathbb Q^4$ | uniform | $129^2$ | $2.76\times10^{-2}$ | $[0.000,\ 0.998]$ |
| Vilar & Abgrall (2024) §4.1.2 | $\mathbb P^5$ DG with a posteriori local subcell correction | 576 triangles | $576\times21=12{,}096$ | not printed | $[6.7\times10^{-10},\ 0.97]$ |

Pazner's runs use $N=3$ on $64^2$ elements of 16 Gauss–Lobatto nodes,
i.e. $256^2=65{,}536$ degrees of freedom, about four times Kuzmin &
Vedral's $129^2=16{,}641$, so the $L^1$ errors of the two papers are not
comparable at equal cost *(compiler check, not in the sources)*.
Kuzmin & Vedral also run $\mathbb Q^2$; their HO-only $\mathbb Q^4$ error is
$1.25\times10^{-2}$.

Ji, Liang & Fu run finite-volume [TENO](/methods/targeted-eno.md) of
orders 3 to 6 on uniform triangles with $h=1/80$ (14,860 elements),
against unstructured WENO5 and [CWENO](/methods/cweno.md)5; they report
no error norms (Figs. 3–4). Their sequel,
[Ji, Liang & Fu (2023)](/sources/ji-2023.md) §4.2, Table 5, reruns the
same bodies, rotation, time $t=2\pi$ and mesh ($h\approx1/80$, 14,860
triangles) with the dual-stencil-selection TENO4-D to TENO7-D, again
without error norms (Fig. 2).

Maltsev et al. run hybrid DG–FV schemes of orders 3 to 5
(DG($P_r$) whose troubled cells receive CWENOZ coefficients of the same
order) in [UCNS3D](/software/ucns3d.md) on a hybrid
quadrilateral–triangle mesh with 64 edges per side, CFL 0.5, with
MOOD-type switches of strict ($10^{-3}$) or relaxed ($10^{-1}$)
discrete-maximum-principle margin and bounds from direct neighbours
("limited") or from the whole reconstruction stencil ("extended")
(Figs. 5–7); no error norm or range is printed.

Vilar & Abgrall's sixth-order DG corrects only the subcells flagged by
a positivity and relaxed discrete-maximum-principle check, replacing
their reconstructed fluxes by first-order finite-volume fluxes
([MOOD-type correction](/methods/mood-a-posteriori-limiting.md);
[DG–subcell equivalence](/results/dg-subcell-finite-volume-equivalence.md)),
with a uniform structured subdivision of each triangle into 21 subcells
(Figs. 22–23); they also run fourth order for five rotations with four
subdivisions (Figs. 24–26). The degrees of freedom are $576$ cells
times the dimension $21$ of $\mathbb P^5$ *(compiler check, not in the
sources)*.

## Findings across sources

**Bounds versus $L^1$ error.** In both papers the scheme with the
smallest $L^1$ error is not the best one. Pazner's unlimited DG has the
smallest error, $1.0\times10^{-2}$, but leaves $[0,1]$ by $-0.21$ and
$+0.16$; Pazner's subcell limited scheme keeps the range exactly $[0,1]$ at
almost the same error, $1.1\times10^{-2}$, against $8.5\times10^{-2}$ for the
low-order scheme on which the limiting is built (Fig. 10). Kuzmin &
Vedral call WENO-stabilized CG "superior" for all degrees although its
$L^1$ error is about twice that of HO stabilization; the superiority is
in boundedness and freedom from oscillations (Figs. 3–5).

**Order and candidate-stencil selection on unstructured meshes.**
Ji, Liang & Fu find TENO4/5/6 much less dissipative than TENO3 on the
slotted cylinder, and TENO5 with fewer overshoots than WENO5 and less
dissipation than CWENO5 (Figs. 3–4); the evidence is visual, with no
$L^1$ error or range printed, so their runs cannot be entered in the
table. In the sequel all TENO-D orders preserve the shapes well, and
"no significant improvement can be noticed by increasing the
reconstruction accuracy order" from four to seven (Ji, Liang & Fu 2023,
§4.2, Fig. 2).

**Subcell correction keeps the global bounds.** Vilar & Abgrall's
corrected solution keeps the global maximum principle, with minimum
$6.7\times10^{-10}$ and maximum $0.97$ after one rotation (Fig. 22). On
their linear-advection tests with correction, uniform subdivisions
resolve the profiles much better than non-uniform ones, which they
attribute mainly to the dependence of their numerical admissibility
detector on the subcell aspect ratio (§4.1.1, Figs. 19–21).

**Troubled-cell switches.** Maltsev et al. find that extended bounds
flag fewer troubled cells than limited ones, especially in smooth
regions, while limited bounds over-diffuse the profiles; that the
troubled-cell percentage falls with increasing order, which they
attribute to the subcell resolution of DG; and that re-checking the
troubled cells at every Runge–Kutta stage or freezing them for the step
makes a negligible difference (§3.2, Figs. 6–7). See
[troubled-cell indicators](/definitions/troubled-cell-indicator.md) and
[MOOD](/methods/mood-a-posteriori-limiting.md).

**Subcell versus element-wise limiting.** On a coarse $25\times25$
mesh with $N=3$, Pazner's subcell limiting is less diffusive than
element-wise limiting (Fig. 4), and Pazner's modal smoothness indicator,
which relaxes local bounds to global ones in smooth cells, lowers the
$L^1$ error by "about 25%", from $2.6\times10^{-2}$ to $1.9\times10^{-2}$, and
widens the computed range from $[0,0.95]$ to $[0,1]$, i.e. it reduces
peak clipping (§4.4, Fig. 6). See
[convex limiting](/methods/convex-limiting.md) and
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

## Rotating complex waves

[Deng, Jiang & Yan (2025)](/sources/deng-2025.md) §4.1, Eq. (4.1)
rotate four profiles of the Jiang–Shu type on $[0,4]^2$ with
$v=(0.5y-1,\ 1-0.5x)$: a cone $1-5r_1$ for $r_1\le0.2$, a square of
height 1 on $\lvert x-2\rvert\le0.4$, $2.8\le y\le3.6$, a Gaussian
composite and an elliptic composite (their $G$ and $F$ with
$\delta=0.01$, $\alpha=5$), with $r_1=0.5\sqrt{(x-3.2)^2+(y-2)^2}$,
$r_2=0.5\sqrt{(x-2)^2+(y-0.8)^2}$, $r_3=\sqrt{(x-0.8)^2+(y-2)^2}$
(page-local), to $t=2$, "after one period", with a pure finite-volume
scheme on $200\times200$ uniform cells or on non-uniform cells equal
to the Gauss-weight subcells of $50\times50$ fourth-order DG elements.
Their non-uniform-grid [ROUND](/methods/round-scheme.md)
reconstruction is far less dissipative than TVD limiters, the van Leer
limiter distorting the shapes even on the uniform grid, keeps the
shapes on the strongly non-uniform grid, and along $y=3.25$ is less
dissipative than WENO5-JS on the uniform grid, which overshoots
(Figs. 5–7); the same holds on grids matching fifth-order DG on
$40\times40$ and sixth-order on $34\times34$ elements (Fig. 8). No error
norm is printed.

## Rotating smooth bump

[Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) §4.1,
Eq. (43) (arXiv v4) rotate a single Gaussian,
$u_0=\exp(-40(x^2+(y-0.5)^2))$, once on the unit disk to $t=1$ with
outflow boundaries, fourth-order continuous Galerkin residual
distribution on Bernstein polynomials, SSPRK(5,4), CFL 0.4, 3582
triangles, applying their
[entropy correction term](/methods/entropy-correction-term.md) at each
Runge–Kutta stage. The test compares the two weightings of the
correction on smooth data, not limiters: the energy changes are
$2.2904450548\times10^{-19}$ against $2.2904450546\times10^{-19}$ at
$t=0.5$ and $1.20908075699\times10^{-17}$ against
$1.20908075829\times10^{-17}$ at $t=1$, and the $L^\infty$ errors
$1.5323772081\times10^{-4}$ against $1.5323772103\times10^{-4}$
(Table 1), so the weightings differ only in the tenth significant
digit, relative differences of about $10^{-10}$ to $10^{-9}$
*(compiler check, not in the sources)*. They
call it a "linear rotation" of a bump "moving around in a circle", but
print the fluxes $\partial_x(2\pi yu)+\partial_y(2\pi xu)$, i.e. the
velocity $(2\pi y,2\pi x)$, whose streamlines $x^2-y^2=\mathrm{const}$
are hyperbolas through a saddle at the origin; a rotation of period one
needs opposite signs, e.g. $(-2\pi y,2\pi x)$ *(compiler check, not in
the sources)*. A sign is lost in print; which field was run cannot be
read from the paper.

## Smooth rotation on adaptive grids

[Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) §4.2
(arXiv v2) rotate a smoothed disc,
$q_0=H(r+r_0)-H(r-r_0)$ with $H(r)=(\tanh(r/0.02)+1)/2$ and $r_0=0.15$
(page-local; their Eq. (16)), on $[-1,1]^2$ with the stream function
$\Psi=\tfrac\pi2(x^2+y^2)$, i.e. $v=(-\pi y,\ \pi x)$, of period 2,
with their Cartesian [Active Flux](/methods/active-flux.md) method in
ForestClaw ([adaptive mesh refinement](/methods/adaptive-mesh-refinement.md));
the centre of the disc is not restated for this domain. With point
values evolved along the exact characteristics, $L^1$ errors at $t=2$
are $4.60\times10^{-6}$ and $5.83\times10^{-7}$ on uniform levels 6 and 7
(EOC 2.9807) and $4.67\times10^{-6}$, $5.92\times10^{-7}$ on AMR levels
3–6 and 3–7 (2.9801); with their general constant-state-preserving
flux, in which the velocity is frozen at the edge midpoint, the errors
are slightly larger, $5.79\times10^{-6}$ and $7.35\times10^{-7}$ on both
grids (2.9786, 2.9781) (Table 2, Fig. 8). The exact-characteristics
variant preserves constant states on regular Cartesian grids, since
its $x$-fluxes depend only on $y$ and its $y$-fluxes only on $x$
(Remark 4.1); see [free-stream preservation](/properties/free-stream-preservation.md).
Their text speaks of the error "after a half rotation", the Table 2
caption of $t=2$, a full rotation of the period-2 flow.

## Swirling deformation (LeVeque)

[Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md) §3.1.1 take
LeVeque's deformation test, as they cite it, as a check of
positivity limiting for the colour equation $\partial_tu+v\cdot\nabla u=0$
with the divergence-free field
$v=\big(\sin^2(\pi x)\sin(2\pi y),\ -\sin^2(\pi y)\sin(2\pi x)\big)$,
time-independent as printed, on $[0,1]^2$, with $u_0=1$ inside the circle
$(x-1)^2+(y-1)^2<0.8^2$ and $0$ outside, on $100^2$ and $200^2$ cells,
snapshots at $t=0,1,2.5$ and slices along $x=0.5$ at $t=2.5$ (Figs. 1–5);
the CFL number is not stated. Their two-dimensional
[Active Flux](/methods/active-flux.md) scheme, whose cell averages are
updated by Simpson's rule in space and time over point values on cell
corners and edge midpoints, shows "quite mild" oscillations unlimited.
Their own earlier bound-preserving reconstruction reduces them but is not
exactly bound preserving, because Simpson's rule is not exact for
piecewise quadratics (Fig. 3). The new limiter blends the Active Flux
fluxes with first-order Lax–Friedrichs fluxes to keep the cell averages
non-negative (lower bound only), with positivity guaranteed for CFL
$\le1/4$, against the CFL limit $1/2$ of Lax–Friedrichs; the
[PAMPA](/methods/pampa-scheme.md) flux limiter of Abgrall et al., which
enforces both bounds, is related but "not equivalent", and on this test
a global Lax–Friedrichs speed gave more accurate results than the local
one (Remark 3.2, Fig. 5). See
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md)
and [bound preservation](/properties/bound-preservation.md). With a
time-independent field the profile is not returned to its initial shape,
so the test compares limiters against each other, not against an exact
solution *(compiler check, not in the sources)*.

## Qualifications

- Kuzmin & Vedral write "the exact solution of the linear advection
  equation (22)" in §7.3, where (22) is their Burgers equation; the
  rotation equation is (24).
- Kuzmin & Vedral's Fig. 4(d) caption gives the $\mathbb Q^2$ WENO-stabilized
  error as $2.67\times10^{-1}$, ten times their $\mathbb Q^1$ and $\mathbb Q^4$
  values and above the LO error $1.10\times10^{-1}$ of a visibly more
  diffused solution; it reads as a slip for $2.67\times10^{-2}$, and no
  $\mathbb Q^2$ value is entered in the table.
- None of the papers reports errors for the three bodies separately.
- Deng, Jiang & Yan's field $v=(0.5y-1,\ 1-0.5x)$ rotates about $(2,2)$
  with angular speed $0.5$, a period of $4\pi\approx12.6$, not the
  printed $t=2$ "after one period"; and they print the Gaussian
  parameter as $\beta=\log_2(36\delta^2)$, negative for $\delta=0.01$
  ($-8.1$), which makes $\exp(-\beta r^2)$ grow away from its centre
  *(compiler check, not in the sources)*.
- Kiechle, Chudzik & Helzel's initial circle, centred at $(1,1)$ with radius
  0.8, covers only the corner of the unit square near $(1,1)$ *(compiler
  check, not in the sources)*; the text layer reads the radius as "0.82",
  the printed form is $0.8^2$.
- Maltsev et al. run their other unit-scale scalar tests (square-wave
  advection) on a domain also printed as $[0,10]^2$.

# Citations

- [Pazner (2021)](/sources/pazner-2021.md) — §4.1.4, Fig. 4; §4.4, Fig. 6; §5.4, Fig. 10 (arXiv v1).
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §7.3, Eqs. (24)–(25), Figs. 3–5 (arXiv v1).
- [Ji, Liang & Fu (2022)](/sources/ji-2022.md) — §5.3, Figs. 3–4 (preprint).
- [Ji, Liang & Fu (2023)](/sources/ji-2023.md) — §4.2, Table 5, Fig. 2.
- [Abgrall, Öffner & Ranocha (2022)](/sources/abgrall-2022.md) — §4.1, Eq. (43), Table 1 (arXiv v4).
- [Maltsev et al. (2023)](/sources/maltsev-2023.md) — §3.2, Figs. 5–7.
- [Calhoun, Chudzik & Helzel (2023)](/sources/calhoun-2023.md) — §4.2, Eqs. (16)–(21), Remark 4.1, Table 2, Fig. 8 (arXiv v2).
- [Vilar & Abgrall (2024)](/sources/vilar-2024.md) — §4.1, §4.1.2, Figs. 19–26 (HAL preprint).
- [Deng, Jiang & Yan (2025)](/sources/deng-2025.md) — §4.1, Eqs. (4.1)–(4.2), Figs. 3–8.
- [Kiechle, Chudzik & Helzel (2025)](/sources/kiechle-2025.md) — §3.1–3.2, Remark 3.2, Figs. 1–5.
