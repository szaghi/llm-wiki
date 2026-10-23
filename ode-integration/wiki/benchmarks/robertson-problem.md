---
type: Benchmark
title: "Robertson problem"
description: "Robertson's three-species chemical kinetics system, with rate constants spanning nine orders of magnitude and solutions integrated to t = 1e5 or 1e11; a stiff test with real negative Jacobian eigenvalues on which explicit methods fail, implicit deferred-correction and ADER variants are compared, multirate Runge–Kutta–Chebyshev is run from shifted initial data, and positivity-preserving schemes are tested with near-zero initial data."
status: established
aliases: [Robertson chemical kinetics, ROBER, Robertson (1966) problem]
tags: [stiff, verification, implicit, deferred-correction, positivity]
timestamp: 2026-10-20T06:18:00Z
---

# Robertson problem

The **Robertson problem** models three reacting species:

$$\begin{aligned}
y_1'&=-0.04\,y_1+10^4\,y_2y_3,\\
y_2'&=\phantom{-}0.04\,y_1-10^4\,y_2y_3-3\cdot10^7\,y_2^2,\\
y_3'&=3\cdot10^7\,y_2^2,
\end{aligned}\qquad y(0)=(1,0,0)^\top .$$

Two sources print exactly this system
([Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md), Eq. (6.5);
[Han Veiga et al. (2021)](/sources/hanveiga-2021.md), Eq. (75));
[Abdulle et al. (2022)](/sources/abdulle-2022.md) (Eq. (5.1)) print the same right-hand
side with different initial data. The rate constants
span nine orders of magnitude, $y_2$ stays tiny (below $3.6\times10^{-5}$ in
Table 6.5 of Koyaguerebo-Imé & Bourgault), and the sources integrate over very
long intervals ($10^5$ and $10^{11}$). The right-hand sides sum to zero, so
$y_1+y_2+y_3=1$ for all $t$; every Runge–Kutta or linear multistep method keeps this
linear invariant *(compiler check, not in the sources)*.

As a conservative [production–destruction system](/definitions/production-destruction-system.md)
the nonzero rates are $p_{12}=d_{21}=10^4y_2y_3$, $p_{21}=d_{12}=0.04y_1$ and
$p_{32}=d_{23}=3\cdot10^7y_2^2$ ([Torlo et al. 2022](/sources/torlo-2022.md), Eq. (69);
see Qualifications). [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) (Eq. (36))
write it in graph Laplacian form $y'=\mathbb G(y)y$ (page-local $\mathbb G$) with

$$\mathbb G(y)=\begin{pmatrix}-0.04&10^4y_3&0\\0.04&-3\cdot10^7y_2-10^4y_3&0\\0&3\cdot10^7y_2&0\end{pmatrix},$$

which has the required sign structure for $y\ge0$ only and $\mathbf 1$ as left null
vector.

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

**Torlo et al. (2022), §7.1, Fig. 7.** [Patankar-type schemes](/methods/modified-patankar-methods.md)
need positive data, so the zero initial components are replaced by $10^{-180}$; 20
exponentially growing steps cover $t\in[10^{-10},10^{10}]$. The schemes that fall to first
order for vanishing initial data, MPRK(2,2,α) with $\alpha>1$, MPRK(4,3,10,0.5),
MPRKSO(2,2,0.001,10) and equispaced mPDeC11, miss the evolution of $y_2$ and sometimes of
$y_3$; the non-conservative SI-RK2 and SI-RK3 "go to infinity". The steady state $(0,0,1)$
cannot be overshot by positive conservative schemes, so oscillations are not the issue here.

**Nurkhametova et al. (2026), §5.** Uncorrected SDIRK21 produces negative $y_2$, at
magnitudes $10^{-10}$–$10^{-15}$, on runs to $t\approx10^{12}$; the Patankar
predictor–corrector removes them (Figs. 2–4). Invariant error on $[0,10^4]$:
$2.44\times10^{-15}$ (baseline), $2.22\times10^{-15}$ (final-stage correction),
$3.99\times10^{-15}$ (all stages) (§5.2.1). Observed orders on $[0,5000]$ with tolerances
$10^{-5}$–$10^{-8}$: 1.51, 3.47, 5.47 for SDIRK21, 32, 43 with the final-stage correction and
1.95, 2.84, 3.76 with all stages corrected (Tables 4–5). With SDIRK43 at tolerance $10^{-7}$
the correction cuts the run time on $[0,10^4]$ from 0.485 s to 0.090 s ($-81.4\%$), which the
authors attribute to avoiding stiff dynamics in non-physical negative states (Table 6,
Remark 3.22).

**Abdulle et al. (2022), §5.1, Figs. 10–11.** The
[multirate Runge–Kutta–Chebyshev method](/methods/multirate-runge-kutta-chebyshev.md) (mRKC)
splits the right-hand side into a severely stiff but cheap part, the single term
$-10^4y_2y_3$ of the second equation, and the rest, on $t\in[0,100]$ with the
non-standard initial data $y(0)=(1,\ 2\cdot10^{-5},\ 10^{-1})^\top$ (see Qualifications);
with these data, the authors state, that term is the only source of severe stiffness.
Steps $h=2^{-k}$, $k=0,\dots,7$, against an RK4 reference with $h=10^{-4}$, $\ell^\infty$
error: the standard [Runge–Kutta–Chebyshev method](/methods/stabilized-explicit-runge-kutta.md)
(RKC) and mRKC both converge at first order, with hardly distinguishable errors, and
mRKC's mean inner averaging interval stays much smaller than $h$ (Fig. 10). At $h=1$ the
spectral radius of the slow part decreases in time, so mRKC's outer stage number
decreases, while RKC's stage number grows with the full spectral radius, which the stiff
term drives (Fig. 11).

**Izzo et al. (2025), §5.** The multistep Patankar methods of their Table 1 "exhibit reduced
efficiency" on Robertson; no data are shown ([Izzo et al. 2025](/sources/izzo-2025.md)).

## Qualifications

- **Printed slip in Torlo et al. (2022).** Eq. (69) prints $p_{32}=d_{23}=k_2y_2$ with
  $k_2=3\cdot10^7$; the Robertson rate is $k_2y_2^2$, as in the ODE above and in the
  graph Laplacian form of Nurkhametova et al. *(compiler check of p. 28 of the arXiv v5, not
  in the sources)*. Nurkhametova et al. print the reaction scheme as
  "$A\to B$, $B+B\to B+C\to A+C$", conflating $B+B\to B+C$ and $B+C\to A+C$ *(compiler check of
  the printed scheme, §5.1)*.

- **Initial data of Abdulle et al. (2022).** Their Eq. (5.1) starts from
  $y(0)=(1,\ 2\cdot10^{-5},\ 10^{-1})^\top$, not from the standard $(1,0,0)^\top$, and the
  paper does not say why. The components then sum to $1.10002$, the invariant value of
  $y_1+y_2+y_3$ for that run *(compiler check, not in the source)*. Their results are not
  comparable with runs from $(1,0,0)^\top$.
- Koyaguerebo-Imé & Bourgault and Han Veiga et al. share the system but not the protocol: the former
  measure fixed-step errors to $T=10^5$ against a high-order reference, the latter
  compare trajectories to $10^{11}$ with 30 geometrically growing steps.
- The orders printed in Table 6.5 at $h=1/600$ (up to 27.7) are computed from errors at
  round-off level ($10^{-16}$) and are not convergence orders *(compiler check, not in the sources)*.

# Citations

- [Koyaguerebo-Imé & Bourgault (2022)](/sources/koyaguerebo-2022.md) — §6.5 (Eq. (6.5), Table 6.5).
- [Han Veiga et al. (2021)](/sources/hanveiga-2021.md) — §5.3 (Eq. (75), Fig. 10).
- [Torlo et al. (2022)](/sources/torlo-2022.md) — §7.1 (Eq. (69), Fig. 7); arXiv v5.
- [Nurkhametova et al. (2026)](/sources/nurkhametova-2026.md) — §4.1.1 (Eqs. (35)–(37)), §5.1.1, §5.2.1, §5.3 (Tables 4–5), §5.4 (Table 6), Figs. 2–4, 11–13.
- [Izzo et al. (2025)](/sources/izzo-2025.md) — §5; arXiv v1.
- [Abdulle et al. (2022)](/sources/abdulle-2022.md) — §5.1 (Eq. (5.1), Figs. 10–11); arXiv v6.
