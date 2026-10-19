---
type: Benchmark
title: "Robertson problem"
description: "Robertson's three-species chemical kinetics system, with rate constants spanning nine orders of magnitude and solutions integrated to t = 1e5 or 1e11; a stiff test with real negative Jacobian eigenvalues on which explicit methods fail and implicit deferred-correction and ADER variants are compared."
status: established
aliases: [Robertson chemical kinetics, ROBER, Robertson (1966) problem]
tags: [stiff, verification, implicit, deferred-correction]
timestamp: 2026-10-19T20:00:00Z
---

# Robertson problem

The **Robertson problem** models three reacting species:

$$\begin{aligned}
y_1'&=-0.04\,y_1+10^4\,y_2y_3,\\
y_2'&=\phantom{-}0.04\,y_1-10^4\,y_2y_3-3\cdot10^7\,y_2^2,\\
y_3'&=3\cdot10^7\,y_2^2,
\end{aligned}\qquad y(0)=(1,0,0)^\top .$$

Both sources print this system
([Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md), Eq. (6.5);
[Han Veiga et al. (2021)](/sources/hanveiga-2021.md), Eq. (75)). The rate constants
span nine orders of magnitude, $y_2$ stays tiny (below $3.6\times10^{-5}$ in
Table 6.5 of Koyaguerebo-Imé & Bourgault), and the sources integrate over very
long intervals ($10^5$ and $10^{11}$). The right-hand sides sum to zero, so
$y_1+y_2+y_3=1$ for all $t$; every Runge–Kutta or linear multistep method keeps this
linear invariant *(compiler check, not in the sources)*.

## Setups and results

**Koyaguerebo-Imé & Bourgault (2022), §6.5, Table 6.5.** Final time $T=10^5$;
reference solution DC10 with $h=1/6000$. Along the solution
$y\in[1.78\times10^{-2},1]\times[0,3.58\times10^{-5}]\times[0,0.983]$ and the Jacobian
eigenvalues lie in $[-9825.744,0]$, real and non-positive. The authors call it "one of
the three problems considered as stiffest" by Hairer–Wanner and the test that
"addresses B-convergence" ([B-convergence](/definitions/b-convergence.md)).
Fixed steps $h=0.5$, $1/300$, $1/600$, $1/6000$:

- their [deferred-correction](/methods/deferred-correction.md) schemes are accurate
  already at $h=0.5$ (DC6: $2.08\times10^{-6}$ in $y_1$, $1.02\times10^{-7}$ in $y_3$), so
  levels above DC6 are unnecessary;
- convergence is slow for $h>1/300$ (observed orders between 0.5 and 1.9) and fast for
  $h<1/300$;
- at $h=0.5$ fixed-step BDF2, BDF4 and BDF6 reach $5.3\times10^{-4}$, $3.6\times10^{-5}$
  and $4.1\times10^{-6}$; at $h=1/600$ the comparison suggests DC error constants "3 to 5
  orders of magnitude smaller" than those of BDF;
- Scilab's adaptive RKF45 fails ("it is likely that rkf45 is inefficient for solving
  this problem"), the table has no entry for explicit RK4, and Scilab's adaptive BDF solver reaches
  about $7.8\times10^{-13}$ with tight tolerances.

**Han Veiga et al. (2021), §5.3, Fig. 10.** Interval $t\in[0,10^{11}]$ covered in 30
steps with geometric growth $h_n=2h_{n-1}$ (following Abgrall & Torlo); the whole
right-hand side is treated as stiff; third-order methods; $y_2$ plotted
multiplied by $10^4$. Only the implicit variants follow the reference: implicit
[ADER](/methods/ader-time-integration.md) is visibly more accurate than the
linearly implicit IMDeC, and the explicit ADER and DeC fail early with wide
oscillations. No error table is given.

## Qualifications

- The two studies share the system but not the protocol: Koyaguerebo-Imé & Bourgault
  measure fixed-step errors to $T=10^5$ against a high-order reference; Han Veiga et al.
  compare trajectories to $10^{11}$ with 30 geometrically growing steps.
- The orders printed in Table 6.5 at $h=1/600$ (up to 27.7) are computed from errors at
  round-off level ($10^{-16}$) and are not convergence orders *(compiler check, not in the sources)*.

# Citations

- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §6.5 (Eq. (6.5), Table 6.5).
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.3 (Eq. (75), Fig. 10).
