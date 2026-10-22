---
type: Benchmark
title: "Rayleigh–Taylor instability"
description: "Two-dimensional Euler benchmark with gravity, in the Xu–Shu setting: a heavy and a light gas, γ=5/3, a single-mode interface perturbation on [0,1/4]×[0,1] run to t=1.95; used to compare the small-scale structure and the left–right symmetry of low-dissipation schemes; a three-dimensional magnetized variant tests positivity-preserving DG for ideal MHD."
status: established
aliases: [RTI, Rayleigh–Taylor, single-mode Rayleigh–Taylor instability]
tags: [benchmark, low-dissipation, teno, weno, central-scheme]
timestamp: 2026-10-23T16:00:00Z
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
[symmetry preservation](/properties/symmetry-preservation.md). Sixteen
sources of the bundle discuss it (one of them only in a
three-dimensional magnetized variant); Fu (2021), Takagi et al., Ye et al.,
Huang et al. (2026), Huang, Liang & Fu (2023) and Li, Chen & Ren (2022)
cite Xu & Shu for it, Li et al. (2022, WENO-ZN) cite Shi, Zhang & Shu
and Young et al.

## Setup

The common data, printed by [Fu (2021)](/sources/fu-2021.md) §5.5.2,
[Takagi et al. (2022)](/sources/takagi-2022.md) §4.7,
[Ye et al. (2022)](/sources/ye-2022.md) §4.7, Eq. (47),
[Li et al. (2022)](/sources/li-2022-b.md) §4.4.1, Eq. (45),
[Chertock et al. (2023)](/sources/chertock-2023.md) Ex. 9,
[Wang et al. (2023)](/sources/wang-2023-b.md) Example 9,
[Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.7, Eq. (38),
[Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.5,
[Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.7,
[Li, Chen & Ren (2022)](/sources/li-2022.md) §4.3.2,
[Liang et al. (2022)](/sources/liang-2022.md) §4.10,
[Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.13 and
[Zhou et al. (2023)](/sources/zhou-2023.md) §5.7, Eq. (42), with
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
... placed on top of a layer of lighter fluid". [Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.13 and
[Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.5 likewise add $\rho$
and $\rho v_2$ to the $y$-momentum and energy equations as source
terms (Hong et al.: "added to the third and fourth Euler equations"),
and so do Zhou et al. ("added to the right-hand sides").
[Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) Eq. (48) print the
source $(0,0,\rho g,\rho v_2g)$ with $g=1$ on the right-hand side, the
same convention. [Li, Chen & Ren (2022)](/sources/li-2022.md) mention
"gravity source terms" without writing them, and
[Liang et al. (2022)](/sources/liang-2022.md) do not write the gravity
term. Ye et al. say "the direction of gravity is the
same as the $y$ axis" without giving the sign of the source; Li et al.
write that $\rho$ and $\rho v_2$ are added "to the flux" of the
$y$-momentum and energy equations, without writing the term; Takagi et al., Fu (2021),
[Huang et al. (2026)](/sources/huang-2026.md) and Bezgin et al. do not
describe the gravity term. For Bezgin et al. this is a gap in the
printed model: they state the homogeneous Euler system (their Eq. (26)),
for which the initial pressures $2y+1$ and $y+3/2$ are not in
equilibrium.

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
| [Hong, Ye & Ye (2022)](/sources/hong-2022.md) §5.5 | [TENO-M](/methods/targeted-eno.md)6/8 vs TENO6/8, [WENO-CU6](/methods/weno-cu6.md), WENO-JS, WENO7, WENO9; $\epsilon=10^{-4}$ | $64\times256$ | 1.95 |
| [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) §4.7 | five-point [adaptive TENO](/methods/adaptive-teno.md) with a new scale sensor vs WENO5-Z, TENO5, TENO5-A; Roe | $96\times384$ | 1.95; 43 contours 0.9–2.2 |
| [Li, Chen & Ren (2022)](/sources/li-2022.md) §4.3.2 | hybrid MDAD-HY vs MDCD-HY, TENO-HY ([MDCD family](/methods/mdcd-scheme.md)) | $128\times512$ | 1.95 |
| [Liang et al. (2022)](/sources/liang-2022.md) §4.10 | TENO5 with THINC jump reconstruction ([TENO-THINC](/methods/teno-thinc.md)) vs WENO5-Z, TENO5, TENO5-THINC, TENO6; Rusanov | $64\times256$, $128\times512$ | 1.95 |
| [Fan et al. (2023)](/sources/fan-2023.md) Ex. 3.13 | finite-difference [Hermite WENO](/methods/hermite-weno.md) HWENO-R vs WENO-ZQ | $120\times480$, $240\times960$ | 1.95 |
| [Zhou et al. (2023)](/sources/zhou-2023.md) §5.7 | six-point [WCNS](/methods/weighted-compact-nonlinear-scheme.md) WCNS-SA vs WCNS-LD and ONL6; HLLC, TVD-RK3, CFL 0.5 | $60\times240$, $120\times480$ | 1.95 |
| [Bezgin et al. (2022)](/sources/bezgin-2022.md) §4.7 | [WENO3-NN](/methods/learned-weno-weights.md) vs WENO3-JS, WENO3-Z, WENO5-JS; LLF, characteristic | $128\times512$, $256\times1024$ | 1.95; 20 contours 0.85–2.25 |

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
at $C_T=10^{-8}$ (Fig. 8). Bezgin et al. find the three-point
WENO3-NN resolving finer structures than WENO3-JS and WENO3-Z, and
report that at $256\times1024$ WENO5-JS shows no vortical structures at
all (§4.7, Figs. 15–16). Hong et al. find TENO and TENO-M resolving far
more small-scale structure than WENO-JS, WENO7 and WENO9, TENO
"slightly better" than TENO-M, and WENO-CU6 comparable to TENO-M6
(Fig. 13); their Table 4 also uses the case for timing (CPU s per 1000
steps on $64\times256$: TENO-M6 100.84, TENO6 125.75, WENO-JS 88.64,
WENO-CU6 105.80). Huang, Liang & Fu find much richer vortical
structures with their scheme (Fig. 11); Li, Chen & Ren find the finest
shear-layer structures with MDAD-HY, whose shock detector flags only
vortex edges, not vortex interiors (Figs. 21–22); Liang et al. find more
interfacial and small-scale structure with their TENO-THINC variant
(Figs. 22–23). Fan et al. give a second cross-grid calibration:
HWENO-R on $120\times480$ is comparable to WENO-ZQ on $240\times960$,
which they attribute to the lower dissipation of compact Hermite
stencils (Fig. 3.17).
Zhou et al. find bubble, spike and the small vortices on the spike
neck reproduced by all three of their six-point WCNS, and more
small-scale structure with the adaptive-dissipation WCNS-SA on both
grids (Figs. 17–18).

**Symmetry.** The data are symmetric about $x=1/8$ ($\cos 8\pi x$ is
invariant under $x\mapsto\tfrac14-x$) *(compiler check, not in the
sources)*, and the sources
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
- Huang, Liang & Fu (2023) observe a loss of symmetry with TENO5,
  TENO5-A and their new scheme and attribute it, like Fu (2021), to low
  dissipation failing to suppress machine round-off (§4.7).
- Liang et al. (2022) state that very-low-dissipation TENO schemes "may
  cause the so-called symmetry breaking issue ... due to machine
  round-off errors", apply a symmetry-preserving implementation
  technique from the literature, and report "rigorous flow symmetry"
  (§4, §4.10).
- Hong et al. raise the weight regularization to $\epsilon=10^{-4}$ on
  this case "to alleviate" round-off symmetry breaking, following
  Fu et al. (§5.5).

Both Fu papers name round-off as the seed of the asymmetry. They
weigh the role of dissipation differently: Fu (2021) writes that the
round-off "cannot be hidden by the low numerical dissipation of the
present schemes", Fu (2023), reporting Fleischmann et al., that there
is no causal link between symmetry breaking and low dissipation. Fu (2023) frames its account as countering the earlier TENO5
observation, not Fu (2021).

## Three-dimensional magnetized variant

[Dzanic & Witherden (2023)](/sources/dzanic-2023.md) §5.6, Eqs.
(47)–(52) (arXiv v2) scale the ideal-MHD setup of Stone & Gardiner to
$[-L/2,L/2]^2\times[-L,L]$, $L=1$: light fluid $\rho=1$ for $z\le0$,
heavy fluid $\rho=3$ above (Atwood number $1/2$), $\gamma=5/3$,
hydrostatic pressure $p(z)=p_0-\rho gz$ with $p_0=10/\gamma$ and $g=1$,
gravity as a source term added to the Powell term, uniform field
$B=(B_0,0,0)$, and a single deterministic mode
$v_3=A\cos(\pi z/(2L))\sin(4\pi x/L)\sin(4\pi y/L)$, $A=0.05$, in place
of random noise; periodic in $x$ and $y$, reflecting top and bottom.
With the critical field $B_{\mathrm c}=\sqrt{(\rho_{\mathrm h}-\rho_{\mathrm l})gL}=\sqrt2$
they run $B_0=0$, $0.1B_{\mathrm c}$ and $0.5B_{\mathrm c}$ ($A$,
$B_{\mathrm c}$, $\rho_{\mathrm h}$, $\rho_{\mathrm l}$ page-local), at
$\mathbb P_3$ on $64\times64\times128$ hexahedra, $\Delta t=2\times10^{-5}$,
snapshots at $t=2,3,4,5$.

With positivity-preserving [entropy filtering](/methods/entropy-filtering.md)
the runs are well behaved in the hydrodynamic, weakly and strongly
magnetized regimes; the field makes the mixing anisotropic and slows the
growth (Figs. 14–16). The case is also their cost test: to $t=1$ at
$B_0=0.1B_{\mathrm c}$ on 16 V100 GPUs, the new node-wise filter
optimization takes 25.3 GPU hours against 61.4 with the earlier
matrix–vector approach at $\mathbb P_3$ (a factor 2.43), and 39.8
against 257 at $\mathbb P_4$ on $51\times51\times102$ elements (6.46),
at about the same number of degrees of freedom (Fig. 17). The speedup
factors are recomputed from the printed hours *(compiler check, not in
the sources)*.

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
- Hong et al. print the domain as "$[0,0.25]\times[0,1][0,1]$", a
  duplicated interval.
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
- [Bezgin et al. (2022)](/sources/bezgin-2022.md) — §4.7, Eqs. (26), (38), Figs. 15–16.
- [Hong, Ye & Ye (2022)](/sources/hong-2022.md) — §5.5, Fig. 13; §6, Table 4.
- [Huang, Liang & Fu (2023)](/sources/huang-2023-b.md) — §4.7, Eq. (48), Fig. 11 (arXiv v1).
- [Li, Chen & Ren (2022)](/sources/li-2022.md) — §4.3.2, Figs. 21–22.
- [Liang et al. (2022)](/sources/liang-2022.md) — §4, §4.10, Figs. 22–23.
- [Fan et al. (2023)](/sources/fan-2023.md) — Ex. 3.13, Fig. 3.17.
- [Dzanic & Witherden (2023)](/sources/dzanic-2023.md) — §5.6, Eqs. (47)–(52), Figs. 14–17 (arXiv v2).
- [Zhou et al. (2023)](/sources/zhou-2023.md) — §5.7, Eq. (42), Figs. 17–18.
