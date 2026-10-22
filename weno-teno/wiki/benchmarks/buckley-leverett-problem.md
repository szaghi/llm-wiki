---
type: Benchmark
title: "Buckley–Leverett problem"
description: "Scalar conservation law with the non-convex S-shaped flux used to model porous-media flow, run as Riemann or step data against a fine first-order reference; used to show that explicit DG with subcell convex limiting and implicit CWENO at Courant numbers near ten stay free of overshoots."
status: established
aliases: [Buckley–Leverett equation, Buckley–Leverett test]
tags: [benchmark, limiting, cweno, dg]
timestamp: 2026-10-22T12:00:00Z
---

# Buckley–Leverett problem

The Buckley–Leverett equation $\partial_tu+\partial_xf(u)=0$ is used to
model porous-media flow (Pazner 2021, §5.3); the sources plot its
solution in $[0,1]$. Its flux

$$
f(u)=\frac{u^2}{u^2+M_{\mathrm{BL}}(1-u)^2},
$$

with a positive constant $M_{\mathrm{BL}}$ (page-local symbol), is
non-convex. Both sources describe it so; the S shape follows from
$f(0)=0$, $f(1)=1$ and $f'(0)=f'(1)=0$, which force $f'$ to have an
interior maximum and $f''$ to change sign on $(0,1)$. The entropy
solution of a Riemann problem can then contain a shock attached to a
rarefaction in one compound wave, by the convex-hull construction
*(compiler check and remark, not in the sources)*. A scheme that
converges to a non-entropic or overshooting solution is exposed against
a fine first-order reference.

## Setups

| Source | $M_{\mathrm{BL}}$ | Initial data | Domain | Grid | Final time |
|---|---|---|---|---|---|
| [Pazner (2021)](/sources/pazner-2021.md) §5.3, Eq. (75) | $1/4$ (printed as $4u^2/(4u^2+(1-u)^2)$) | Riemann data, printed $u_0=-3$ for $x<0$, $3$ for $x\ge0$ | not stated (plots on $[-1,1]$) | 256 DOFs, $N=0,1,3,7$; reference $N=0$ on 10,000 elements | 0.25 |
| [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) §4.4, Eqs. (38)–(39) | $1/3$ | $u_0=0.5$ on $-0.25\le x\le0.25$, $0$ otherwise | "periodic domain $\Omega=[0,1]$" | 100 cells, $\Delta t=1.1h$ and $4.4h$ | 0.085 |

Puppo et al. take the setup from Arbogast et al. ("the same setup as
in [3]"); $h$ is their cell width. With $M_{\mathrm{BL}}=1/3$ the largest
characteristic speed is $\max f'\approx2.21$ (at $u\approx0.33$), so the
two time steps correspond to Courant numbers of about 2.4 and 9.7
*(compiler check, not in the sources)*.

## Findings

**Explicit DG with subcell convex limiting.** Pazner's sparse
invariant-domain-preserving DG with subcell
[convex limiting](/methods/convex-limiting.md) at fixed 256 degrees of
freedom "compare[s] well" with the fine first-order reference for every
degree $N=0,1,3,7$ (Fig. 9).

**Implicit CWENO at large time steps.** Puppo et al. compare implicit
Euler, the unlimited third-order DIRK–CWENO scheme D3P1 and the
time-limited [Quinpi](/methods/quinpi.md) scheme Q3P1, with the
time-limiter regularization set to $\Delta t^3$ for this test. At the
smaller time step the schemes are similar; at $\Delta t=4.4h$ Q3P1 avoids
the overshoots of D3P1 (Fig. 10).

## Qualifications

- Pazner's printed Riemann data, $\mp3$, lie outside the range $[0,1]$
  shown on the vertical axis of his Fig. 9; the data run cannot be
  recovered from the paper.
- Puppo et al.'s step occupies $[-0.25,0.25]$, outside their stated
  domain $[0,1]$; on a periodic $[0,1]$ it is the step on
  $[0,0.25]\cup[0.75,1]$, and their Fig. 10 is plotted on $[0,1]$.
- Evidence in both papers is visual.

# Citations

- [Pazner (2021)](/sources/pazner-2021.md) — §5.3, Eq. (75), Fig. 9 (arXiv v1).
- [Puppo, Semplice & Visconti (2023)](/sources/puppo-2023.md) — §4.4, Eqs. (38)–(39), Fig. 10 (arXiv v2).
