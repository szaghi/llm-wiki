---
type: Benchmark
title: "Allen–Cahn equation"
description: "The Allen–Cahn reaction–diffusion equation, a stiff semilinear phase-field model with interface width epsilon; the sources use a 1D travelling front, a 2D forced shrinking circle and a 1D double-well problem to test diagonal SDC, adaptive SDC and Parareal with optimized coarse propagators."
status: established
aliases: [Allen-Cahn equation, phase-field equation, forced Allen–Cahn equation]
tags: [stiff, parallel, imex, verification]
timestamp: 2026-10-20T06:18:00Z
---

# Allen–Cahn equation

The **Allen–Cahn equation** is the reaction–diffusion equation of a phase field with
two stable states separated by a diffuse interface of width proportional to
$\varepsilon$:

$$\partial_tu=\Delta u-\frac{2}{\varepsilon^2}\,u(1-u)(1-2u)\qquad\text{or}\qquad\partial_tw=\Delta w+\frac1{\varepsilon^2}\,(w-w^3).$$

The first form has stable states $u\in\{0,1\}$
([Čaklović et al. (2025)](/sources/caklovic-2025.md), Eq. (4.4);
[Saupe et al. (2025)](/sources/saupe-2025.md), Eq. (29)), the second $w\in\{-1,1\}$
([Jin et al. (2025)](/sources/jin-2025.md), Example 4.2). They are the same equation:
$w=2u-1$ maps one onto the other *(compiler check, not in the sources)*. The reaction
term is stiff for small $\varepsilon$ and nonlinear, the diffusion term is stiff for
fine meshes, so the problem tests implicit and IMEX time stepping on a semilinear
problem beyond linear theory. The sources add a driving force that moves or holds the
interface.

## Set-ups

| source | dimension, form | parameters | discretization | use |
|---|---|---|---|---|
| Čaklović et al. (2025), §4.4, Eqs. (4.4)–(4.5) | 1D, $u$-form plus driving term $-6d_wu(1-u)$ (page-local $d_w$) | $x\in[-0.5,0.5]$, $T=50$, $\varepsilon=d_w=0.04$; exact travelling front $u=\frac12\big(1+\tanh\frac{x-vt}{\sqrt2\varepsilon}\big)$, $v=3\sqrt2\varepsilon d_w$, Dirichlet data from it | second-order finite differences, 2047 points; Newton per node with a sparse direct solver | [diagonal SDC](/methods/parallel-sdc.md) efficiency and MPI timing |
| Saupe et al. (2025), §3.4, Eqs. (29)–(34) | 2D, $u$-form plus a global forcing $-6u(1-u)\,\varsigma(u,t)$ that keeps the phase volume oscillating (page-local $\varsigma$) | periodic $[-0.5,0.5)^2$, $\varepsilon=0.04$, circle of radius $R_0=0.25$, $t\in[0,0.025]$ | Fourier spectral; IMEX: Laplacian implicit, reaction explicit | adaptive SDC, parallel SDC, comparison with ARK5(4) |
| Jin et al. (2025), Example 4.2 | 1D, $w$-form | $(0,\pi)$, homogeneous Neumann, $T=1$ (10 for Table 4.3), $w_0=1-2\chi_{(\pi/2,\pi)}$, $\varepsilon^2\in\{1,0.02\}$ | finite differences, $\Delta x=\pi/1000$; fine: Lobatto IIIC or Radau IIA with Newton; coarse: semi-implicit, reaction explicit | [Parareal](/methods/parareal.md) with optimized coarse propagators |

In Saupe et al.'s forcing, the interface radius oscillates between about $0.24$ and $0.27$
(Fig. 5).

## Results

**Diagonal SDC.** All methods saturate at an $L^2$ error of about $2\times10^{-4}$, the spatial
error. Per step, LU-SDC converges fastest, then ESDIRK4(3)6L[2]SA, then MIN-SR-FLEX; per
modelled cost and per measured wall-clock time MIN-SR-FLEX is the most efficient, MIN-SR-S
being faster only for errors above $10^{-1}$. LU-SDC would catch up only if the parallel
efficiency fell below 40 %; the measured efficiency was 74–93 % (Čaklović et al. 2025,
§4.4, Figs. 16–17). This is the only problem of that paper with wall-clock timings.

**Adaptive SDC.** The IMEX scheme becomes unstable at large steps: SDC adapting both the step and
the number of sweeps needed "around 100 restarts" at loose tolerances; limiting the step size helped (not shown),
and the solutions stayed physical at every tolerance (Saupe et al. 2025, §4.1). In measured wall time, four-process
pipelined GSSDC sped the run up, diagonal SDC with three processes was among the most
efficient variants, and combining both gave very large errors or crashes (§4.1, Fig. 9). At
least one adaptive parallel SDC variant beat the additive pair ARK5(4) in wall time (§4.2,
Fig. 10). See
[step-size control](/methods/step-size-control.md).

**Parareal.** With $\varepsilon^2=1$, $N_f=20$ and $100$ fine steps per slice ($N_f$ page-local), $h=1/2000$, the
observed contraction is about $0.04$ with optimized coarse propagators against $0.3$ with
backward Euler (Jin et al. 2025, §4.2, Fig. 4.4). For $T=10$, $N_f=20$ and target accuracy
$10^{-6}$, iterations fall from 6–11 to 3–5 and simulated efficiency rises from 7.3–8.6 % to
12.5–29.1 % (Table 4.3). With $\varepsilon^2=0.02$, $h=10^{-4}$, the rate is about $0.04$ for
$N_f=10,20$, but for larger $N_f$ the difference from backward Euler is small, and the authors
call for nonlinear modifications (Fig. 4.5).

## Qualifications

- **Initial datum of Saupe et al.** Eq. (31) prints $u_0=\tanh\big(\frac{R_0\lVert x\rVert}{\sqrt2\varepsilon}\big)$;
  a circle of radius $R_0$ needs $R_0-\lVert x\rVert$ in the numerator. The typeset page
  (p. 15) has no minus sign, and the colour bar of their Fig. 5 spans about $-0.9$ to $0.9$,
  the range of a $\tanh$, not the states $\{0,1\}$ of their Eq. (29) *(compiler check, not in
  the source)*. The printed datum is a slip; what was run is not recoverable from the paper.
- **Notation in the sources.** Saupe et al. use $\epsilon$ both for the interface width and for
  the local error estimate; Čaklović et al. use $\varepsilon$ for the interface width and for
  the Prothero–Robinson stiffness. On this page $\varepsilon$ is the interface width only.
- **Different equations under one name.** The three set-ups differ in dimension, forcing,
  boundary conditions and splitting; results are not comparable across sources.
- All three sources were read as arXiv preprints.

# Citations

- [Čaklović et al. (2025)](/sources/caklovic-2025.md) — arXiv v2: §4.4 (Eqs. (4.4)–(4.5), Figs. 16–17).
- [Saupe et al. (2025)](/sources/saupe-2025.md) — arXiv v2: §3.4 (Eqs. (29)–(34), Fig. 5); §4.1 (Fig. 9); §4.2 (Fig. 10).
- [Jin et al. (2025)](/sources/jin-2025.md) — arXiv v2: Example 4.2, §4.2 (Figs. 4.4–4.5, Table 4.3).
