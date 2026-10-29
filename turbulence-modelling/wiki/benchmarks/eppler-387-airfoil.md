---
type: Benchmark
title: "Eppler 387 airfoil"
description: "Low-Reynolds-number airfoil with a laminar separation bubble on the suction side, measured by McGhee et al. at Re_c from 60,000 to 300,000: it tests the bubble terms of RANS transition models, the transition and turbulent boundary layer that an implicit LES resolves on high-order meshes, and transitional hybrid RANS/LES up to stall."
status: established
aliases: [E387, Eppler 387, Eppler-387 airfoil, NASA TM 4062 airfoil]
tags: [benchmark, transition, implicit-les, separated-flow, boundary-layer]
timestamp: 2026-10-29T07:36:00Z
---

# Eppler 387 airfoil

The Eppler 387 (E387) is a cambered low-Reynolds-number airfoil whose
suction-side boundary layer stays laminar, separates, transitions in the
separated shear layer and reattaches turbulent: a
[laminar separation bubble](/definitions/laminar-separation-bubble.md)
whose position and size move with the chord Reynolds number $Re_c$ and the
angle of attack, written $\alpha_a$ on this page (page-local, since
$\alpha$ is the registry's blending factor). The reference measurements
used by all the sources are those of McGhee, Walker and Millard (NASA TM
4062, 1988) in the Langley Low-Turbulence Pressure Tunnel; Alberti et al.
(2026) add the digitized data of Emmerson & Verstraete (2020, as cited). Quantities
compared are $C_L$, $C_D$, the pressure and skin-friction distributions,
the separation and reattachment points $x_{\mathrm{sep}}/c$ and
$x_{\mathrm{re}}/c$ (page-local, $c$ the chord), and boundary-layer
profiles and integral thicknesses. The case tests what a model or a
discretization does to the laminar instability that sets transition and to
the turbulent layer after reattachment.

## Configurations in the sources

| Item | [Menter et al. (2022)](/sources/menter-2022.md) | [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) | [Lederer et al. (2026)](/sources/lederer-2026.md) | [Alberti et al. (2026)](/sources/alberti-2026.md) |
|---|---|---|---|---|
| $Re_c$ | $10^5$, $2\times10^5$, $3\times10^5$ | 60,000 | $10^5$ at $\alpha_a=10^\circ$; $3\times10^5$ at $\alpha_a=4^\circ$ | $3\times10^5$ at $\alpha_a=0^\circ$, $8^\circ$, $14^\circ$, $16^\circ$ |
| Approach | RANS with transition models (algebraic γ, γ-$Re_\theta$-SST, one-equation γ-SST), Ansys Fluent | 2D RANS/URANS with γ-$Re_\theta$ in STAR-CCM+ | wall-resolved [implicit LES](/definitions/implicit-les.md) with an upwind mass-conserving mixed stress method, $N=3$ | Spalart–Allmaras IDDES, fully turbulent or with the algebraic SA-BCM transition model, and steady SA-BCM RANS, in an incompressible modal DG solver, $N=3$–5 |
| Inflow | $Tu$ about 0.06% at the leading edge (inlet 0.0631 to 0.0711%, $\mu_t/\mu$ about 0.1) | $Tu=0.03\%$, $\mu_t/\mu=1$ (their setting for all airfoils) | no free-stream turbulence, no inlet-angle correction | $\tilde\nu_\infty/\nu=3$ (fully turbulent SA); $\tilde\nu_\infty/\nu=0.2$, $Tu_\infty=0.1\%$ (SA-BCM) |
| Other references | — | 2D and 3D simulations of Sahin et al., as cited | — | Emmerson & Verstraete (2020, digitized), as cited |

## What the case tests

**Bubble terms of RANS transition models.**
[Menter et al. (2022)](/sources/menter-2022.md) use the E387 at
$Re_c=10^5$ to motivate the bubble term of their algebraic
[transition model](/methods/local-correlation-based-transition-model.md):
without it the laminar separation bubble is strongly over-estimated and the
lift falls at $\alpha_a=4^\circ$–$8^\circ$ through laminar stall, because the
production of the underlying two-equation model acts too slowly even when
the intermittency is switched at the right place (§2.4, Figs. 4–5). Over
the three Reynolds numbers the algebraic model slightly under-predicts and
γ-$Re_\theta$-SST slightly over-predicts the bubble size, while the
one-equation γ-SST over-predicts it significantly at low $Re_c$ in the
mid-$\alpha_a$ range, which the authors read as a deficiency of that
model's bubble terms (Figs. 16–19; skin friction and pressure at
$Re_c=3\times10^5$, $\alpha_a=6^\circ$).

**Limits of two-dimensional transitional RANS.**
[Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md), §6.3,
run the E387 at $Re_c=60{,}000$ as the most cambered of their three
airfoils (with the SD7003 and the Ishii airfoil). Their 2D results agree
with the 2D Navier–Stokes results of Sahin et al. but not with the
three-dimensional data; the higher camber makes the flow
three-dimensional, which the authors name the main limitation of 2D
simulation (§6.3, §7, Fig. 19).

**Transition and turbulent boundary layer in implicit LES.**
[Lederer et al. (2026)](/sources/lederer-2026.md) (read in arXiv v1, 2024)
take the E387 as the test of the
[high-order projection-based upwind method](/methods/high-order-projection-based-upwind-method.md)
on transitional flow. Two cases: R1/α10 ($Re_c=10^5$, $\alpha_a=10^\circ$,
a small leading-edge bubble and a nearly fully turbulent upper surface) and
R3/α4 ($Re_c=3\times10^5$, $\alpha_a=4^\circ$, separation near mid-chord);
the lower surface stays laminar. The 2D curved mesh is extruded over a
span of $0.1c$ (periodic), with a half-circle inlet of radius $5c$ and a
box of length $7c$. Meshes (Table 1):

| Mesh | hexahedra | wall cell height $/c$ | momentum-step degrees of freedom |
|---|---|---|---|
| m1 | 2352 | $2.6\times10^{-3}$ | $1.98\times10^6$ |
| m2 | 7200 | $1.6\times10^{-3}$ | $6.06\times10^6$ |
| m3 | 14,400 | $1.2\times10^{-3}$ | $12.12\times10^6$ |

At $N=3$, the $L^2$ difference of the mean $C_p$ between consecutive meshes
falls below 0.01 at m3, which serves as the grid-independent run (§4).
Results (Table 2):

| Case | run | $C_L$ | $C_D$ | $x_{\mathrm{sep}}/c$ | $x_{\mathrm{re}}/c$ |
|---|---|---|---|---|---|
| R1/α10 | experiment | 1.200 | 0.0413 | — | — |
| | ILES m1 / HOPU m1 | 1.274 / 1.271 | 0.0432 / 0.0436 | 0.007 / 0.007 | 0.010 / 0.010 |
| | ILES m2 / HOPU m2 | 1.268 / 1.266 | 0.0421 / 0.0425 | 0.008 / 0.008 | 0.016 / 0.016 |
| | ILES m3 | 1.259 | 0.0411 | 0.010 | 0.027 |
| R3/α4 | experiment | 0.792 | 0.0109 | 0.40 | 0.58 |
| | ILES m1 / HOPU m1 | 0.767 / 0.767 | 0.0116 / 0.0116 | 0.498 / 0.499 | 0.517 / 0.517 |
| | ILES m2 / HOPU m2 | 0.763 / 0.763 | 0.0113 / 0.0113 | 0.498 / 0.498 | 0.515 / 0.515 |
| | ILES m3 | 0.759 | 0.0113 | 0.467 | 0.560 |

- The bubble grows with resolution; on the coarse meshes the R1/α10
  bubble is too small or replaced by "an (unphysical) almost natural
  transition" (§4.1, Fig. 4). In R3/α4 the experiment separates earlier
  than the simulation (§4.1). The authors attribute the leading-edge $C_p$
  mismatch to the finite domain (§4.1), and read the transition prediction
  of the finest mesh as a benefit of the low dissipation of the scheme,
  which preserves the small-scale laminar instabilities (§5).
- HOPU leaves $C_p$, $C_L$, $C_D$, the bubble and the integral
  thicknesses $\delta^*$, $\theta$ essentially unchanged (Table 2, Fig. 10), but in the
  turbulent boundary layer it reduces the over-prediction of the mean
  tangential velocity in wall units for $y^+>10$ and of the turbulent
  kinetic energy and Reynolds shear stress; on m1 at R1/α10 its velocity
  profiles are "almost as well as the ILES m3" (§4.2, Figs. 7–9). The
  gain is larger at R1/α10, which the authors relate to the larger extent
  of turbulent flow (§4.2, §5).
- The sharp peak of $\delta^*$ at separation and its subsequent fall are not
  captured by the coarse ILES m1 and m2 (§4.2, Fig. 10, R3/α4).

**Transitional hybrid RANS/LES from attached flow to stall.**
[Alberti et al. (2026)](/sources/alberti-2026.md), §3.1, run the E387 at
$Re_c=3\times10^5$ in an incompressible modal DG solver: a circular domain
of diameter $25c$ centred at the leading edge, extruded $0.2c$ in span,
7644 hexahedra and prisms with second-order edges and 12 inflated wall
layers (growth 1.4), first-cell height in wall units divided by $N+1$ of
2.1, 1.7, 1.4 and 152,880, 267,540, 428,064 degrees of freedom at $N=3$, 4,
5, and a refined $N=4$ mesh of 395,325 degrees of freedom at $16^\circ$;
averages over up to $50c/U_\infty$ at the higher angles. Runs: steady
transitional RANS (SA-BCM), fully turbulent SA-IDDES, and IDDES with
SA-BCM as its RANS branch and a shielding function that keeps RANS mode
wherever the intermittency is below one, with the onset constant at the
original 50 or at their 1000 (models on the
[transition-model page](/methods/local-correlation-based-transition-model.md)
and the [DES page](/methods/detached-eddy-simulation.md)). At $0^\circ$ and
$8^\circ$, $N=3$ (Table 3; $C_L$/$C_D$):

| $\alpha_a$ | SA-BCM steady | IDDES | transitional IDDES, constant 50 | transitional IDDES, constant 1000 | McGhee | Emmerson & Verstraete |
|---|---|---|---|---|---|---|
| $0^\circ$ | 0.375/0.008 | 0.361/0.013 | 0.375/0.009 | 0.38/0.010 | 0.352/0.009 | 0.35/0.008 |
| $8^\circ$ | 1.205/0.019 | 1.159/0.024 | 1.235/0.019 | 1.195/0.020 | 1.180/0.017 | 1.14/0.022 |

At $14^\circ$ and $16^\circ$ (Table 3; transitional IDDES with constant 1000):

| Run | $14^\circ$ $C_L$/$C_D$ | $16^\circ$ $C_L$/$C_D$ |
|---|---|---|
| SA-BCM steady, $N=3$ | 1.334/0.087 | 1.168/0.153 |
| SA-BCM steady, $N=4$ | 1.364/0.082 | 1.190/0.148 |
| IDDES, $N=3$ | 1.404/0.067 | 1.427/0.119 |
| transitional IDDES, $N=3$ | 1.318/0.083 | 1.326/0.261 |
| transitional IDDES, $N=4$ | 1.277/0.087 | 1.303/0.266 |
| transitional IDDES, $N=4$, refined | — | 1.139/0.314 |
| transitional IDDES, $N=5$ | 1.224/0.106 | 1.169/0.300 |
| McGhee | 1.179/— | 0.99/— |
| Emmerson & Verstraete | 1.18/0.12 | 1.09/0.25 |

- At $0^\circ$ fully turbulent IDDES predicts attached flow without the
  [laminar separation bubble](/definitions/laminar-separation-bubble.md);
  the transitional hybrid overlaps transitional RANS, the constant 1000
  slightly suppressing the bubble through early transition (Fig. 2).
- At $8^\circ$ the constant 1000 puts transition at $x/c\approx0.2$, in
  agreement with McGhee, with the solution in RANS mode; with 50 the
  transition resembles a separation-induced process (Figs. 3–5).
- At $14^\circ$ and $16^\circ$ the transitional hybrid moves towards the
  experiment as $N$ rises, with the leading-edge bubble in RANS mode,
  turbulent reattachment and trailing-edge separation; at $16^\circ$, $N=5$
  predicts stall over the whole suction surface, which the steady RANS
  cannot, while fully turbulent IDDES under-estimates the separated region
  (Figs. 6–7).
- With the original shielding the results are "practically identical" (not
  shown), because on this mesh no transition region lies outside the
  original shield (§3.1).

**What the sources share.** The first three use the bubble as the discriminating
feature: its size is what separates the transition models of Menter et al.,
what two-dimensional RANS misses at $Re_c=60{,}000$ in Carreño Ruiz &
D'Ambrosio, and what grows with resolution in the implicit LES of Lederer
et al. Two of them (Menter et al., Lederer et al.) run $Re_c=10^5$ and
$3\times10^5$, but at different angles, and print different quantities
(bubble-size trends against tabulated loads and bubble ends), so their
results cannot be compared number by number. Alberti et al. (2026) use
the bubble the same way, as what fully turbulent hybrid RANS/LES misses at
$Re_c=3\times10^5$ and what their transitional hybrid recovers.

## Qualifications

- Against the experiment, the implicit LES over-predicts $C_L$ at R1/α10
  by 4.9% (ILES m3) to 6.2% (ILES m1) and under-predicts it at R3/α4 by
  3.2% (m1) to 4.2% (m3) *(compiler check, not in the sources)*; the authors state that "all
  values of $c_l$ and $c_d$ closely match the experimental data" (§4.1).
- [Lederer et al. (2026)](/sources/lederer-2026.md) print the start of the
  averaging as "5 characteristic time lengths ($U_\infty/c$)"; by dimension
  the time unit is $c/U_\infty$ *(compiler check, not in the sources)*. Their Table 2 labels the meshes M1–M3, the text m1–m3.
- Alberti et al. (2026) print the complete-polynomial count
  $\prod_{m=1}^{3}(N+m)/m$ of modes per element; with 20, 35 and 56 modes at
  $N=3$, 4, 5 it reproduces their printed totals from 7644 elements
  *(compiler check, not in the sources)*. At $16^\circ$ every lift in their
  Table 3 lies above both measured values (0.99 and 1.09), the closest
  being the refined $N=4$ run at 1.139 *(compiler check, not in the
  sources)*; the authors describe the transitional hybrid as converging
  towards the experiment as $N$ rises.
- The configurations differ in modelling level (2D and 3D RANS,
  transitional hybrid RANS/LES, wall-resolved implicit LES) and in inflow
  turbulence (none to 0.1%), so agreement or disagreement with the experiment is not
  comparable across them.

# Citations

- [Menter et al. (2022)](/sources/menter-2022.md) — §2.4, Figs. 4–5; Eppler 387 test settings and Figs. 16–19.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §6.3, §7, Fig. 19.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv v1: §4, Tables 1–2, Figs. 3–4; §4.1–4.2, Figs. 7–10; §5.
- [Alberti et al. (2026)](/sources/alberti-2026.md) — §3, Table 1 (inflow); §3.1, Table 2 (meshes), Table 3, Figs. 2–7.
