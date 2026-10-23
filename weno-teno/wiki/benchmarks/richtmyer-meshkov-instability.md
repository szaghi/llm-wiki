---
type: Benchmark
title: "Richtmyer–Meshkov instability"
description: "A planar shock crossing a sinusoidally perturbed interface: single-mode air–SF6 at Mach 1.2 against front tracking and growth models, heavy-to-light copper–gas with phase reversal, Brouillette–Sturtevant air–acetone/SF6 with re-shock, a single-gas interface ranking Riemann solvers and reconstructions, its viscous version, shocked N2 and He bubbles and a cavitating water–vapour variant; it tests interface sharpness, growth rates and mixing."
status: established
aliases: [RMI, Richtmyer–Meshkov, shock-accelerated interface, reshocked Richtmyer–Meshkov instability, single-mode Richtmyer–Meshkov instability]
tags: [benchmark, multiphase, interface-capturing, dg]
timestamp: 2026-10-23T15:15:00Z
---

# Richtmyer–Meshkov instability

A planar shock crosses an interface between two materials of different
density whose position carries a small single-mode perturbation,
$x=x_{\mathrm I}+a_0\cos(2\pi y/\lambda)$ with amplitude $a_0$ and
wavelength $\lambda$ (page-local symbols). The impulsive acceleration
makes the perturbation grow: the light fluid penetrates the heavy one as
bubbles, the heavy fluid the light one as spikes, and the interface
rolls up. When the shock reflects from an end wall and crosses the
interface again (re-shock), the mixing zone breaks into fine structures.
The benchmark tests whether a scheme keeps the material interface sharp
and resolves its roll-up, and, where the sources measure it, whether
the perturbation amplitude and growth rate agree with front-tracking
computations and with growth models. The density contrast is given by
the Atwood number $A=(\rho_{\mathrm h}-\rho_{\mathrm l})/(\rho_{\mathrm h}+\rho_{\mathrm l})$
(page-local; heavy and light densities).

## Setups in the sources

The planar setups are two-dimensional and single-mode, one of them smoothed for an unlimited DG robustness test; one source runs shocked bubbles under the same name, and another a cavitating two-phase variant.

**Air–SF$_6$, Mach 1.2.** [Bai & Li (2022)](/sources/bai-2022.md)
§3.3.1, Table 2: domain $[-28,32]\times[-1.875,1.875]$ cm, symmetry
conditions in $y$ and outgoing ones in $x$; interface at $x_{\mathrm I}=0$
with $\lambda=3.75$ cm and $a_0=0.24$ cm; air $\rho=0.95$ kg/m³,
$\gamma=1.4$, and SF$_6$ $\rho=4.84$ kg/m³, $\gamma=1.09$, at
$p=0.8$ bar; a Mach 1.2 shock starts at $x=-1.0$ cm in the air. The
pre-shock Atwood number is $A\approx0.67$ *(compiler check, not in the
sources)*. Their sharp-interface discontinuous Galerkin solver (degree
2, level set, ghost fluid in cut cells; see
[level-set methods](/methods/level-set-method.md)) runs on three
adaptive levels with 80 elements per wavelength on the background
mesh; snapshots from $-30.1$ to $1118\,\mu$s.

**Copper–gas, Mach 2.5, heavy to light.** Bai & Li §3.3.2, Table 3:
domain $[-10,10]\times[-2,2]$ cm, $\lambda=4.0$ cm, $a_0=0.16$ cm; a
Mach 2.5 shock starts at $x=-0.28$ cm inside a copper-like
[stiffened gas](/definitions/stiffened-gas-equation-of-state.md)
($\rho=8930$ kg/m³, $\gamma=3.0$, $C_p=2587$, $p_\infty=4.62\times10^{10}$)
and passes into a gas ($\rho=1.22$ kg/m³, $\gamma=1.67$, $C_p=683$) at
$p=1.0$ bar; four levels, 32 elements per wavelength; time zero when
the shock reaches the bottom of the interface, snapshots to
$81.8\,\mu$s. The shock goes from heavy to light, so the perturbation
first reverses its phase.

**Air–acetone/SF$_6$ with re-shock, Mach 1.21.**
[Renac (2021)](/sources/renac-2021.md) §7.4, after Brouillette &
Sturtevant's experiment: a Mach 1.21 shock in a mixture of air and
acetone vapour ($\gamma=1.24815$, $C_v=3.2286$) hits a single-mode
interface with SF$_6$ ($\gamma=1.0984$, $C_v=2.0019$), $A=0.6053$; data
non-dimensional with a length of 1 cm and the pre-shock pressure,
temperature and sound speed of the mixture; domain
$[0,80.1]\times[0,5.9]$, periodic top and bottom, non-reflecting on the
left and reflecting on the right, so that the shock returns and
re-shocks the interface. The
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
are solved by entropy-stable [DGSEM](/methods/dgsem.md) of degree
$N=3$ on $1601\times118$ Cartesian elements, 118 per wavelength, which
Renac calls coarse compared with earlier computations; snapshots
labelled 4, 6 and 6.6 µs before and 7 µs after re-shock (Fig. 7).

**Single gas, density interface, Mach about 1.24.**
[Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) §5.5, Eqs. (5.6)–(5.7),
put one ideal gas ($\gamma=1.4$) on $[0,4]\times[0,1]$ with a density
interface at $x_{\mathrm p}=2.9-0.1\sin(2\pi(y+0.25))$:
$(\rho,v_1,v_2,p)=(5.04,0,0,1)$ for $x\le x_{\mathrm p}$,
$(1,0,0,1)$ for $x_{\mathrm p}<x<3.2$, and the post-shock state
$(1.4112,-665/1556,0,1.628)$ for $x\ge3.2$, so a left-travelling shock
runs from the light into the heavy part. The "heavy fluid" is only
denser gas: there is one $\gamma$, $A=(5.04-1)/(5.04+1)\approx0.67$
*(compiler check, not in the sources)*, the same pre-shock contrast as
air–SF$_6$. Periodic in $y$, non-reflecting left and right,
$640\times160$ cells, CFL 0.5, $t=9$, second-order MUSCL with
second-order TVD Runge–Kutta.
[Chamarthi (2023a)](/sources/chamarthi-2023.md) Ex. 4.8 (arXiv v2) and
[Chamarthi (2023b)](/sources/chamarthi-2023-b.md) Ex. 3.6 (arXiv v1)
print the same states and interface, with $\gamma=1.4$ "for both
fluids", on $320\times80$ points to $t=9$, left and right boundaries
fixed to the initial values, periodic top and bottom, CFL 0.2.

**Two-phase air–SF$_6$ on the same geometry.** [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md)
Ex. 4.10 keep the interface $x=2.9-0.1\sin(2\pi(y+0.25))$ and the shock
at $x=3.2$ but make the heavy region a second material, in the Kapila
[five-equation model](/definitions/five-equation-model.md): with
$(\rho_1,\rho_2,v_1,v_2,p,\phi_1)$ (phase 1 air, $\gamma_1=1.4$; phase 2
SF$_6$, $\gamma_2=1.093$), SF$_6$ $(1,5.04,0,0,1,10^{-6})$, pre-shock air
$(1,5.04,0,0,1,1-10^{-6})$ and post-shock air
$(1.411,5.04,-0.39,0,1.628,1-10^{-6})$, a Mach 1.24 shock moving left;
$[0,4]\times[0,1]$, $1000\times250$ cells, periodic top and bottom,
outflow on the left, post-shock values on the right; snapshots at
$t=2.31$, $4.62$, $6.93$ and $9.24$ with $\mathbb P^3$ (Fig. 13). Their
scheme is the bound-preserving [OEDG](/methods/oedg.md) DG method with
an HLL flux, CFL $1/(2N+1)$ and SSP-RK3.

**Smooth single-gas variant for unlimited DG.** [Alberti et al. (2025)](/sources/alberti-2025.md)
§3.1.2, Eqs. (55)–(56), use a tanh-smoothed setup they cite from the
literature, with $v=0$,
$p=4.9-1.95\,[1+\tanh(2\xi_1)]$,
$\rho=4.22-1.985\,[2+\tanh(2\xi_1)+\tanh(2\xi_2)]$,
$\xi_1=\lvert y-4\rvert-2$, $\xi_2=y-[18+2\cos(6\pi x/40)]$
(page-local), on the half domain $x\in[0,40/6]$, $y\in[0,40]$ of the
original $[0,40/3]\times[0,40]$ with a symmetry condition, to $t=42$, on
$8\times48$ and $16\times96$ quadrilateral and triangular grids, DG
degree $N=4,\dots,7$, CFL $2.5\times10^{-2}$ and no shock capturing. The
high-pressure slab $\lvert y-4\rvert<2$ releases the shock that later
reaches the perturbed density step near $y=18$ *(compiler check, not in
the sources)*. The test measures robustness, as the completion index
(the fraction of the final time reached, averaged over the runs).

**Viscous air–SF$_6$, two materials.** Chamarthi (2023a) Ex. 4.18 solves
the five-equation model with viscosity $\mu=10^{-4}$ on
$[0,16\lambda]\times[0,\lambda]$, $\lambda=1$, interface
$x/\lambda=0.4-0.1\sin(2\pi(y/\lambda+0.25))$, states
$(\rho,v_1,v_2,p,\gamma)$: pre-shock air $(1,1.24,0,1/1.4,1.4)$,
post-shock air $(1.4112,0.8787,0,1.6272/1.4,1.4)$ and SF$_6$
$(5.04,1.24,0,1/1.4,1.093)$; the interface is smoothed with an error
function (parameter 5); $4096\times256$ points, CFL 0.1, snapshots at
$t=5.5$, $8.25$ and $11$. The air states are the single-gas data above
in units of the pre-shock sound speed, $v\to v/\sqrt{1.4}$,
$p\to p/1.4$, and in a frame moving at $1.24$:
$1.24-\tfrac{665}{1556}/\sqrt{1.4}=0.8788$ and $1.628/1.4=1.1629$
against the printed $0.8787$ and $1.6272/1.4=1.1623$
*(compiler check, not in the sources)*, but the heavy gas now has
$\gamma=1.093$.

**Shock-accelerated bubbles, multi-species OpenFOAM.**
[Duronio & Di Mascio (2024)](/sources/duronio-2024.md) §3.1 call two
shock–bubble cases Richtmyer–Meshkov flows: a square N$_2$ bubble of
edge 56.6 mm in SF$_6$, after the experiment of Zhai et al. (2014), and
a circular He bubble of diameter 50 mm in N$_2$, after Haas &
Sturtevant (1987), both at $101325$ Pa and 273 K, ideal gases, on
$[0,45]\times[0,14]$ cm, the shock crossing the domain left to right
(square bubble) or right to left (circle), its post-shock state set by
the normal-shock relations (Eq. (9)); the shock Mach number is not
printed. The square-bubble grids are $450\times140$, $900\times280$
and $1800\times560$ hexahedra; the circular-bubble grids are not
printed. The solver is a finite-volume multi-species extension of a
kinetic-energy-preserving central scheme with AUSM$^+$-up dissipation,
whose convective part is switched by a Ducros-type sensor (see
[split convective forms](/methods/split-convective-forms.md),
[Ducros sensor](/definitions/ducros-shock-sensor.md),
[OpenFOAM](/software/openfoam.md)). The geometry is that of the
[shock–bubble interaction](/benchmarks/shock-bubble-interaction.md),
not a sinusoidal planar interface.

**Cavitating water–vapour interface.** [Wakimura et al. (2024)](/sources/wakimura-2024.md)
§4.3 (Eq. (48), after Saurel et al. and Pelanti & Shyue, phase change
added) solve the six-equation two-phase model with stiffened-gas water
on $[0,3]\times[0,1]$ m, $300\times100$ cells, outflow on the right and
reflective walls elsewhere, to $t=10$ ms, CFL 0.5. The state is
$(\phi_1,\rho_1,\rho_2,v_1,v_2,p)=(1-10^{-6},1000,100,-200,0,10^5)$ for
$x<1.2$ m and $r>0.6$ m, and $(10^{-6},1000,100,-200,0,10^5)$ otherwise,
with $r$ the distance from $(1.2,0.5)$ m. The liquid region left of
$x=1.2$ m thus has a semicircular notch of radius 0.6 m filled with
vapour, and the whole flow moves at 200 m s$^{-1}$ towards the left
wall *(compiler check, not in the sources: the geometry)*. The run is
made with mechanical relaxation only and with full pressure,
temperature and Gibbs-energy relaxation (phase change), and compares
MUSCL with the [BVD](/definitions/boundary-variation-diminishing.md)
schemes MUSCL-THINC-BVD and adaptive THINC-BVD.

## Findings

**Growth against models and other computations.** On air–SF$_6$, Bai &
Li's amplitude and growth-rate histories are consistent with Holmes's
front-tracking results, with Ullah et al.'s and with an earlier
computation of their group, and agree with the Zhang–Sohn nonlinear
model; they also plot linear theory and Richtmyer's impulsive model
(Figs. 16–17). On copper–gas, the transmitted rarefaction decompresses
the metal from 8930 to a release density of 7570 kg/m³, the asymptotic
bubble velocity is almost equal to the velocity of the unperturbed
interface, and the spike velocity falls after its peak (Figs. 18–19).

**Resolution of the re-shocked mixing zone.** Renac reports "a good
resolution of the shock and material interface and the associated
vortical structures" before and after re-shock, with spike roll-up
after the first passage and "complex fine flow field structures and a
low Mach number flow field" after the second (§7.4, Fig. 7). The
evidence is contour plots; no growth rate or mixing width is measured.

**Grid convergence and experiments for shocked bubbles.** Duronio & Di
Mascio's three-grid Roache analysis along the axis gives observed
orders 1.53 ($p$) and 1.46 ($\rho$) with grid-convergence indices 0.92%
and 0.97% for the square bubble, and 1.35 and 1.46 with 1.1% and 0.77%
for the circular one (Table 1). The square-bubble run reproduces the
experimental wave sequence from 82 to 1334 μs (transmitted, precursor,
reflected and diffracted shocks, Mach stem, corner vortices, jet and
vortex pair); its interface width agrees "excellent[ly]" with the
experiment and its height is "slightly higher" after 0.75 ms (Figs.
4–5). For the He bubble the trajectories of the upstream and downstream
interface points agree with Haas & Sturtevant (Figs. 6–7).

**Bound preservation and interface quality in two-phase DG.** Yan,
Abgrall & Wu show the air–SF$_6$ interface rolling up through the four
snapshots with their bound-preserving OEDG scheme, whose source
discretization of the non-conservative volume-fraction equation keeps
uniform high order and whose oscillation-eliminating step and limiter
preserve constant velocity and pressure across the interface (Fig. 13;
see [pressure-equilibrium preservation](/properties/pressure-equilibrium-preservation.md),
[bound preservation](/properties/bound-preservation.md)).

**Robustness of entropy corrections.** Alberti et al. (2025) find on
the smooth variant that, with the element entropy correction clipped
to non-negative values, their Laplacian-type spreading DEEB$_a$
completes every run and the entropy-viscosity form DEEB$_b$ crashes
once (at $N=6$); without the clipping both lose robustness markedly,
while the other spreading terms are insensitive to it, and the
uncorrected entropy-projection scheme is the least stable, especially
on triangles (Fig. 6; see
[entropy correction term](/methods/entropy-correction-term.md),
[entropy projection](/methods/entropy-projection.md)).

**Riemann-solver ranking.** Hu et al. compare
[HLL-type solvers](/methods/hll-riemann-solvers.md) (HLLE, HLLEM, HLLC
and their RHLLEM-LD) in one second-order scheme and find the sharpest
interfaces with RHLLEM-LD; the evidence is contour plots.

**Roll-up as a dissipation gauge.** On the single-gas case Chamarthi
(2023a) finds that TENO5 produces "no roll-up vortices at all", MEG6
some and MIG4 the most ([gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
with an [MP limiter](/methods/monotonicity-preserving-limiter.md);
Fig. 11). Chamarthi (2023b) finds MEG7 with conservative variables
giving a thinner interface than the seventh-order mapped WCNS7M, and
MEG7 with primitive variables lower dissipation still, with small-scale
roll-ups (Fig. 9); the wall-clock times are 224 s (MEG7-prim), 205 s
(MEG7-cons) and 345 s (WCNS7M), hardware not stated (Table 2). In the
viscous two-material run of Chamarthi (2023a) the interface stays free of
oscillations and is thinnest with MIG4 (Ex. 4.18; see
[five-equation model](/definitions/five-equation-model.md)).

**Cavitation and dissipation.** With phase change Wakimura et al. find
more vaporization near the left wall than without; the instability is
more developed with the BVD schemes, which they attribute to their lower
dissipation, and no scheme shows significant pressure oscillations
(§4.3, Figs. 4–5). They state that, to their knowledge, results of this
test with phase change had not been published before. See
[THINC reconstruction](/methods/thinc-reconstruction.md) and
[operator splitting](/methods/operator-splitting.md) for the relaxation
steps.

**Also in the bundle.** [Huang et al. (2026)](/sources/huang-2026.md)
§6.9 run a Richtmyer–Meshkov problem at $\Delta x=1/200$ to $t=2$ and
find [ROUND](/methods/round-scheme.md) comparable to a learned
third-order WENO and its low-dissipation variant finer than WENO5-JS
(Fig. 14), again by visual comparison.

## Qualifications

- The setups share only the geometry: the Atwood numbers
  (about 0.67, 0.61, a metal–gas contrast, and 0.67 for one gas and for
  the viscous air–SF$_6$ case), the
  shock strengths (Mach 1.2, 1.21, 2.5, about 1.24), the direction
  (light to heavy, heavy to light) and the presence of re-shock all
  differ, and only Bai & Li measure a growth rate.
- Chamarthi (2023a)'s finding that TENO5 shows no roll-up comes from
  one grid ($320\times80$) and the author's TENO5 implementation; no
  other source on this page runs TENO on this case.
- Yan, Abgrall & Wu's post-shock air density and pressure, $1.411$ and
  $1.628$, are those of a Mach 1.24 shock into $(\rho,p)=(1,1)$ with
  $\gamma=1.4$, whose post-shock speed is $0.4275$, not the printed
  $0.39$; Hu et al. print $665/1556=0.4274$ for the same state
  *(compiler check, not in the sources)*.
- Hu et al.'s post-shock state is consistent with the Rankine–Hugoniot
  conditions into $(1,0,0,1)$ only to about $10^{-3}$: $p=1.628$ gives
  $M=1.24028$, $\rho=1.41164$, $\lvert v_1\rvert=0.42793$, whereas
  $\rho=1.4112$ corresponds to $M=1.24002$, $p=1.62727$,
  $\lvert v_1\rvert=0.42752$, and $665/1556=0.42738$ matches neither
  exactly *(compiler check, not in the sources)*. The mismatch is at the
  level of rounding of the printed data.
- Bai & Li print the copper stiffening constant with the unit "bar";
  with bar the sound speed of their metal would be about 1250 km/s, with
  pascal about 3.9 km/s, so pascal is meant *(compiler check, not in the
  sources)*. Their Table 3 labels the gas density "$\rho_{\mathrm{air}}$"
  although the gas has $\gamma=1.67$.
- Renac defines the Atwood number with "$\rho_2=\gamma_2$ taken as the
  pre-shock density of the mixture", but component 1 is the mixture:
  with Renac's non-dimensionalization the mixture density is
  $\gamma_1=1.24815$, and $A=0.6053$ then gives an SF$_6$ density of
  about 5.08 *(compiler check, not in the sources)*.
- Renac's figure labels the snapshots in microseconds for a
  non-dimensional computation.
- Duronio & Di Mascio's observed orders of 1.35–1.53 are those of a
  flow with shocks and material interfaces on three grids, not the
  design order of their second-order scheme; they print neither the
  shock Mach number nor the circular-bubble grids, and their §3.1.2 says
  Table 1 reports density only while the table gives pressure and
  density.

# Citations

- [Bai & Li (2022)](/sources/bai-2022.md) — §3.3.1–3.3.2, Tables 2–3, Figs. 16–19.
- [Renac (2021)](/sources/renac-2021.md) — §7.4, Fig. 7 (arXiv v3).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.9, Fig. 14.
- [Hu, Yuan & Zhao (2022)](/sources/hu-2022.md) — §5.5, Eqs. (5.6)–(5.7).
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Exs. 4.8, 4.18, Fig. 11 (arXiv v2).
- [Chamarthi (2023b)](/sources/chamarthi-2023-b.md) — Ex. 3.6, Fig. 9, Table 2 (arXiv v1).
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §2 (Eqs. (6)–(9)), §3.1, Table 1, Figs. 1–7.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §4, §4.3, Eq. (48), Figs. 4–5.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — §4, Ex. 4.10, Fig. 13.
- [Alberti et al. (2025)](/sources/alberti-2025.md) — §3.1.2, Eqs. (53), (55)–(56), Fig. 6.
