---
type: Benchmark
title: "Eppler 387 airfoil"
description: "Low-Reynolds-number airfoil with a laminar separation bubble on the suction side, measured by McGhee et al. at Re_c from 60,000 to 300,000: it tests the bubble terms of RANS transition models and the transition and turbulent boundary layer that an implicit LES resolves on high-order meshes."
status: established
aliases: [E387, Eppler 387, Eppler-387 airfoil, NASA TM 4062 airfoil]
tags: [benchmark, transition, implicit-les, separated-flow, boundary-layer]
timestamp: 2026-10-27T15:50:00Z
---

# Eppler 387 airfoil

The Eppler 387 (E387) is a cambered low-Reynolds-number airfoil whose
suction-side boundary layer stays laminar, separates, transitions in the
separated shear layer and reattaches turbulent: a
[laminar separation bubble](/definitions/laminar-separation-bubble.md)
whose position and size move with the chord Reynolds number $Re_c$ and the
angle of attack, written $\alpha_a$ on this page (page-local, since
$\alpha$ is the registry's blending factor). The reference measurements
used by all three sources are those of McGhee, Walker and Millard (NASA TM
4062, 1988) in the Langley Low-Turbulence Pressure Tunnel. Quantities
compared are $C_L$, $C_D$, the pressure and skin-friction distributions,
the separation and reattachment points $x_{\mathrm{sep}}/c$ and
$x_{\mathrm{re}}/c$ (page-local, $c$ the chord), and boundary-layer
profiles and integral thicknesses. The case tests what a model or a
discretization does to the laminar instability that sets transition and to
the turbulent layer after reattachment.

## Configurations in the sources

| Item | [Menter et al. (2022)](/sources/menter-2022.md) | [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) | [Lederer et al. (2026)](/sources/lederer-2026.md) |
|---|---|---|---|
| $Re_c$ | $10^5$, $2\times10^5$, $3\times10^5$ | 60,000 | $10^5$ at $\alpha_a=10^\circ$; $3\times10^5$ at $\alpha_a=4^\circ$ |
| Approach | RANS with transition models (algebraic γ, γ-$Re_\theta$-SST, one-equation γ-SST), Ansys Fluent | 2D RANS/URANS with γ-$Re_\theta$ in STAR-CCM+ | wall-resolved [implicit LES](/definitions/implicit-les.md) with an upwind mass-conserving mixed stress method, $N=3$ |
| Inflow | $Tu$ about 0.06% at the leading edge (inlet 0.0631 to 0.0711%, $\mu_t/\mu$ about 0.1) | $Tu=0.03\%$, $\mu_t/\mu=1$ (their setting for all airfoils) | no free-stream turbulence, no inlet-angle correction |
| Other references | — | 2D and 3D simulations of Sahin et al., as cited | — |

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

**What the sources share.** All three use the bubble as the discriminating
feature: its size is what separates the transition models of Menter et al.,
what two-dimensional RANS misses at $Re_c=60{,}000$ in Carreño Ruiz &
D'Ambrosio, and what grows with resolution in the implicit LES of Lederer
et al. Two of them (Menter et al., Lederer et al.) run $Re_c=10^5$ and
$3\times10^5$, but at different angles, and print different quantities
(bubble-size trends against tabulated loads and bubble ends), so their
results cannot be compared number by number.

## Qualifications

- Against the experiment, the implicit LES over-predicts $C_L$ at R1/α10
  by 4.9% (ILES m3) to 6.2% (ILES m1) and under-predicts it at R3/α4 by
  3.2% (m1) to 4.2% (m3) *(compiler check, not in the sources)*; the authors state that "all
  values of $c_l$ and $c_d$ closely match the experimental data" (§4.1).
- [Lederer et al. (2026)](/sources/lederer-2026.md) print the start of the
  averaging as "5 characteristic time lengths ($U_\infty/c$)"; by dimension
  the time unit is $c/U_\infty$ *(compiler check, not in the sources)*. Their Table 2 labels the meshes M1–M3, the text m1–m3.
- The configurations differ in modelling level (2D and 3D RANS against
  wall-resolved implicit LES) and in inflow turbulence (0.03% to about
  0.06% against none), so agreement or disagreement with the experiment is not
  comparable across them.

# Citations

- [Menter et al. (2022)](/sources/menter-2022.md) — §2.4, Figs. 4–5; Eppler 387 test settings and Figs. 16–19.
- [Carreño Ruiz & D'Ambrosio (2022)](/sources/carrenoruiz-2022.md) — §6.3, §7, Fig. 19.
- [Lederer et al. (2026)](/sources/lederer-2026.md) — arXiv v1: §4, Tables 1–2, Figs. 3–4; §4.1–4.2, Figs. 7–10; §5.
