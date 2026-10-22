---
type: Benchmark
title: "Solid-body rotation"
description: "LeVeque's two-dimensional linear-advection test in which a smooth hump, a cone and a slotted cylinder rotate rigidly for one revolution; the exact solution is the initial data, so L1 errors and the solution range measure together the dissipation and the bound violations of limited high-order finite element schemes."
status: established
aliases: [LeVeque solid body rotation, slotted cylinder test, hump–cone–slotted-cylinder rotation]
tags: [benchmark, limiting, bound-preserving, dg]
timestamp: 2026-10-22T12:00:00Z
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
test for the scalar maximum principle. Both sources attribute it to
LeVeque.

## Setup

[Pazner (2021)](/sources/pazner-2021.md) §5.4 and
[Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) §7.3 print the same
data. With $r$ the distance to a body's centre divided by $0.15$, and
$u=0$ outside the three disks:

- smooth hump centred at $(0.25,0.5)$: $u=\tfrac14\big(1+\cos(\pi r)\big)$;
- cone centred at $(0.5,0.25)$: $u=1-r$;
- slotted cylinder centred at $(0.5,0.75)$: $u=1$ if $|x-0.5|\ge0.025$ or
  $y\ge0.85$, and $u=0$ in the slot.

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

Pazner's runs use $N=3$ on $64^2$ elements of 16 Gauss–Lobatto nodes,
i.e. $256^2=65{,}536$ degrees of freedom, about four times Kuzmin &
Vedral's $129^2=16{,}641$, so the $L^1$ errors of the two papers are not
comparable at equal cost *(compiler check, not in the sources)*.
Kuzmin & Vedral also run $\mathbb Q^2$; their HO-only $\mathbb Q^4$ error is
$1.25\times10^{-2}$.

## Findings across sources

**Bounds versus $L^1$ error.** In both papers the scheme with the
smallest $L^1$ error is not the best one. Pazner's unlimited DG has the
smallest error, $1.0\times10^{-2}$, but leaves $[0,1]$ by $-0.21$ and
$+0.16$; his subcell limited scheme keeps the range exactly $[0,1]$ at
almost the same error, $1.1\times10^{-2}$, against $8.5\times10^{-2}$ for the
low-order scheme on which the limiting is built (Fig. 10). Kuzmin &
Vedral call WENO-stabilized CG "superior" for all degrees although its
$L^1$ error is about twice that of HO stabilization; the superiority is
in boundedness and freedom from oscillations (Figs. 3–5).

**Subcell versus element-wise limiting.** On a coarse $25\times25$
mesh with $N=3$, Pazner's subcell limiting is less diffusive than
element-wise limiting (Fig. 4), and his modal smoothness indicator,
which relaxes local bounds to global ones in smooth cells, lowers the
$L^1$ error by "about 25%", from $2.6\times10^{-2}$ to $1.9\times10^{-2}$, and
widens the computed range from $[0,0.95]$ to $[0,1]$, i.e. it reduces
peak clipping (§4.4, Fig. 6). See
[convex limiting](/methods/convex-limiting.md) and
[troubled-cell indicators](/definitions/troubled-cell-indicator.md).

## Qualifications

- Kuzmin & Vedral write "the exact solution of the linear advection
  equation (22)" in §7.3, where (22) is their Burgers equation; the
  rotation equation is (24).
- Kuzmin & Vedral's Fig. 4(d) caption gives the $\mathbb Q^2$ WENO-stabilized
  error as $2.67\times10^{-1}$, ten times their $\mathbb Q^1$ and $\mathbb Q^4$
  values and above the LO error $1.10\times10^{-1}$ of a visibly more
  diffused solution; it reads as a slip for $2.67\times10^{-2}$, and no
  $\mathbb Q^2$ value is entered in the table.
- Neither paper reports errors for the three bodies separately.

# Citations

- [Pazner (2021)](/sources/pazner-2021.md) — §4.1.4, Fig. 4; §4.4, Fig. 6; §5.4, Fig. 10 (arXiv v1).
- [Kuzmin & Vedral (2023)](/sources/kuzmin-2023.md) — §7.3, Eqs. (24)–(25), Figs. 3–5 (arXiv v1).
