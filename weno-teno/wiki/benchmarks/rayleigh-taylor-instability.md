---
type: Benchmark
title: "Rayleigh–Taylor instability"
description: "Two-dimensional Euler benchmark with gravity, in the Xu–Shu setting: a heavy and a light gas, γ=5/3, a single-mode interface perturbation on [0,1/4]×[0,1] run to t=1.95; used to compare the small-scale structure and the left–right symmetry of low-dissipation schemes."
status: established
aliases: [RTI, Rayleigh–Taylor, single-mode Rayleigh–Taylor instability]
tags: [benchmark, low-dissipation, teno, weno, central-scheme]
timestamp: 2026-10-21T12:00:00Z
---

# Rayleigh–Taylor instability

Two ideal gases ($\gamma=5/3$) of density 2 and 1 are separated by the
line $y=1/2$ in a tall channel $[0,1/4]\times[0,1]$, in hydrostatic
equilibrium under a unit gravity, with the heavy gas on the side
towards which gravity does not point. A single-mode velocity
perturbation of the interface grows into a rising bubble and falling
spike whose flanks are Kelvin–Helmholtz unstable. The test serves two
purposes: the amount of secondary roll-up is a visual gauge of
[numerical dissipation](/definitions/numerical-dissipation.md), and the
exact left–right mirror symmetry of the data probes
[symmetry preservation](/properties/symmetry-preservation.md). Eight
sources of the bundle discuss it; Fu (2021), Takagi et al., Ye et al. and
Huang et al. cite Xu & Shu for it, Li et al. cite Shi, Zhang & Shu and
Young et al.

## Setup

The common data, printed by [Fu (2021)](/sources/fu-2021.md) §5.5.2,
[Takagi et al. (2022)](/sources/takagi-2022.md) §4.7,
[Ye et al. (2022)](/sources/ye-2022.md) §4.7, Eq. (47),
[Li et al. (2022)](/sources/li-2022-b.md) §4.4.1, Eq. (45),
[Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 9 and
[Wang et al. (2023)](/sources/wang-2023-b.md) Example 9, with
$c=\sqrt{\gamma p/\rho}$:

$$
(\rho,v_1,v_2,p)(x,y,0)=\begin{cases}
\big(2,\ 0,\ -0.025\,c\cos(8\pi x),\ 2y+1\big), & y<\tfrac12,\\
\big(1,\ 0,\ -0.025\,c\cos(8\pi x),\ y+\tfrac32\big), & y\ge\tfrac12,
\end{cases}
$$

reflecting walls at $x=0$ and $x=1/4$, fixed states
$(\rho,v_1,v_2,p)=(2,0,0,1)$ at $y=0$ and $(1,0,0,2.5)$ at $y=1$, final
time $t=1.95$.

**Gravity convention.** Chertock et al. and Wang et al. state the
gravity term explicitly: $+\rho$ in the $y$-momentum equation and
$+\rho v_2$ in the energy equation, i.e. gravity of unit magnitude
along $+y$, which is consistent with the hydrostatic profiles
$\partial_yp=+\rho$ ($p=2y+1$ below, $y+3/2$ above, continuous at
$y=1/2$ and matching the fixed states at $y=0$ and $y=1$) and puts the
heavy gas physically "on top" *(compiler check, not in the sources)*;
Chertock et al. describe the instability as "a layer of heavier fluid
... placed on top of a layer of lighter fluid". Ye et al. say "the direction of gravity is the
same as the $y$ axis" without giving the sign of the source; Li et al.
write that $\rho$ and $\rho v_2$ are added "to the flux" of the
$y$-momentum and energy equations, without writing the term; Takagi et al., Fu (2021) and
[Huang et al. (2026)](/sources/huang-2026.md) do not describe the
gravity term.

## Runs in the sources

| Source | Scheme | Grid | Times |
|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.5.2 | very-high-order [TENO](/methods/adaptive-teno.md) vs [WENO-CU6](/methods/weno-cu6.md); Rusanov and Roe | $64\times256$ | 1.95 |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.7 | [TENO-THINC](/methods/teno-thinc.md) vs WENO5-Z, TENO5; Rusanov and Roe | $64\times256$, $128\times512$ | 1.95 |
| [Li et al. (2022)](/sources/li-2022-b.md) §4.4.1 | seventh-order [WENO-ZN](/methods/weno-zn.md) vs WENO-JS, WENO-Z | $120\times480$ | 1.95 |
| [Ye et al. (2022)](/sources/ye-2022.md) §4.7 | [AFTENO](/methods/afteno.md) vs TENO5, AFWENO; HLLC | $120\times480$ ($h=1/480$) | 1.95 |
| [Huang et al. (2026)](/sources/huang-2026.md) §6.8 | [ROUND, LD-ROUND](/methods/round-scheme.md) vs WENO5-JS, WENO5-Z | $128\times512$ | 1.95 |
| [Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 9 | [LCD central-upwind](/methods/lcd-central-upwind-scheme.md) vs earlier CU | $\Delta x=\Delta y=1/1024$ | 1.95, 2.95 |
| [Wang et al. (2023)](/sources/wang-2023-b.md) Example 9 | A-WENO with [adaptive-diffusion CURH flux](/methods/adaptive-diffusion-central-upwind-flux.md) | $\Delta x=\Delta y=1/800$ | 1.95, 2.95 |
| [Fu (2023)](/sources/fu-2023.md) §3.8 | TENO review: symmetry discussion | — | — |

## Findings across sources

**Small-scale structure.** Every comparison favours the new scheme by
the richness of the roll-up on the spike flanks: TENO-THINC over
WENO5-Z and TENO5 with both Rusanov and Roe fluxes (Takagi et al.,
Figs. 14–17); WENO-ZN over WENO-JS and WENO-Z (Li et al., Fig. 7);
AFTENO5 with HLLC richest among the TENO and AFWENO variants (Ye et
al., Fig. 7); the new central-upwind fluxes over their predecessors,
with earlier secondary mushrooms and a "jellyfish-like" structure at
$t=2.95$ (Wang et al., Fig. 9; Chertock et al.). Ye et al. give the
only cross-grid calibration: AFTENO5 at $h=1/480$ is comparable to
fifth-order WENO-JS at $h=1/1920$ and ninth-order WENO-JS at $h=1/960$
from earlier literature, and lowering the TENO cut-off $C_T$ from
$10^{-6}$ to $10^{-8}$ resolves more scales, matching those references
at $C_T=10^{-8}$ (Fig. 8).

**Symmetry.** The data are symmetric about $x=1/8$ ($\cos 8\pi x$ is
invariant under $x\mapsto\tfrac14-x$; *compiler check, not in the
sources*), and the sources
report different outcomes for low-dissipation schemes:

- Fu (2021) observes a **loss of symmetry** with very-high-order TENO on
  $64\times256$ and attributes it to machine round-off that the low
  dissipation no longer hides, citing similar asymmetries of other
  low-dissipation schemes and Fleischmann et al. as a cure by careful
  floating-point implementation (§5.5.2, Fig. 9).
- Fu (2023) reports the observation that TENO5 breaks the symmetry on
  a coarse grid where WENO5-JS keeps it, and sides with Fleischmann et
  al.: symmetry breaking is caused by floating-point inconsistencies
  that grow exponentially, not by low dissipation, and with a
  consistent implementation TENO5 keeps symmetry to machine precision
  (§3.8).
- Takagi et al. report that TENO-THINC preserves symmetry on both grids
  (§4.7).

Both Fu papers name round-off as the seed of the asymmetry. They
weigh the role of dissipation differently: Fu (2021) writes that the
round-off "cannot be hidden by the low numerical dissipation of the
present schemes", Fu (2023), reporting Fleischmann et al., that there
is no causal link between symmetry breaking and low dissipation. The
two statements are compatible if dissipation only masks an asymmetry
whose source is the implementation, which is what Fleischmann et al.'s
symmetric TENO5 results show; Fu (2023) frames its account as
countering the earlier TENO5 observation, not Fu (2021). Whether a
given run is symmetric is therefore a property of the implementation as
much as of the scheme.

## Qualifications

- Huang et al. (Eq. (6.10) and the text after it) print the heavy gas
  ($\rho=2$, $p=2y+1$) for $y\ge0.5$ and the light gas ($p=y+1.5$)
  below, and the fixed states $(1,0,0,2.5)$ at the bottom and
  $(2,0,0,1)$ at the top. Each of the two is the common setup with the
  roles of bottom and top exchanged, and the two do not fit each other:
  the printed initial data give $(\rho,p)=(1,1.5)$ at $y=0$ and $(2,3)$
  at $y=1$ *(compiler check, not in the sources)*; the common setup is
  the one printed by Fu (2021), Takagi et al., Ye et al., Li et al.,
  Chertock et al. and Wang et al. The gravity term is not given, so the run actually computed
  cannot be reconstructed from the paper.
- Li et al. print the domain as "$[0,0.25]\times[0.1]$"; Eq. (45) and
  the $120\times480$ grid fix it as $[0,0.25]\times[0,1]$. They also use
  $\alpha$ for the sound speed in the data.
- More small-scale structure is not evidence of accuracy: the
  inviscid problem has no grid-converged solution (see
  [Kelvin–Helmholtz instability](/benchmarks/kelvin-helmholtz-instability.md)).

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.5.2, Fig. 9 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.7, Figs. 14–17.
- [Li et al. (2022)](/sources/li-2022-b.md) — §4.4.1, Eq. (45), Fig. 7.
- [Ye et al. (2022)](/sources/ye-2022.md) — §4.7, Eq. (47), Figs. 7–8.
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.8, Eq. (6.10).
- [Chertock et al. (2023)](/sources/chertock-2023.md) — §5.2, Ex. 9 (arXiv v2).
- [Wang et al. (2023)](/sources/wang-2023-b.md) — §4, Example 9, Fig. 9.
- [Fu (2023)](/sources/fu-2023.md) — §3.8.
