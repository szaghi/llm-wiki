---
type: Benchmark
title: "Shock–water-column interaction"
description: "A planar air shock hitting a water column or droplet: comparisons with Igra and Takayama's interferograms and Sembian et al.'s schlieren at Mach 1.47 and 2.4, a column with an air cavity, two columns at Mach 6, Mach 10 positivity and symmetry tests, and Mach 1.5 shocks on water and n-dodecane droplets in their vapour, with and without phase change."
status: established
aliases: [shock–water column, shock–water cylinder, shock–droplet interaction, water column in air, shocked water cylinder]
tags: [benchmark, multiphase, interface-capturing, positivity]
timestamp: 2026-10-23T23:55:00Z
---

# Shock–water-column interaction

A planar shock travelling through air hits a cylinder of water, about
a thousand times denser than the air in the air–water setups below; one
source replaces the air by the liquid's own vapour. The shock
is reflected and a shock is transmitted into the water; the incident
shock wraps round the column, its Mach stems converge at the rear
stagnation point, expansion waves follow, and a pair of
counter-rotating vortices forms behind the column (the features the
sources compare with experiments, listed below). It is the
"inverse" of the [shock–bubble interaction](/benchmarks/shock-bubble-interaction.md):
the heavy, stiff medium is inside. The sources run it with
[five-equation diffuse-interface models](/definitions/five-equation-model.md)
closed by the [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md)
and use it in two roles: validation against shock-tube experiments and,
at high Mach number, a robustness test for high-order schemes. A
sharp-interface [level-set](/methods/level-set-method.md) source uses it
for evaporating and condensing droplets.

Page-local symbols: $\phi_1$ the water volume fraction, $D$ the column
diameter, $(\gamma,p_\infty)$ the stiffened-gas constants. Water is
$(\gamma,p_\infty)=(6.12,\ 3.43\times10^8\ \mathrm{Pa})$ and air
$(1.4,0)$ in every air–water setup below that prints them, except
Zhang et al.'s, whose water is $(4.4,\ 6\times10^8\ \mathrm{Pa})$.

## Setups

| Source | Shock Mach | Setup as printed | Grid | Compared with |
|---|---|---|---|---|
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.2 | 1.47 | 4.8 mm water cylinder in air, 2D; parameters deferred to Meng & Colonius | not printed | holographic interferograms of Igra & Takayama at $t=16$ and $32\,\mu$s |
| [Wong et al. (2021)](/sources/wong-2021.md) §6.5 | 2.4 | domain 11.1 cm × 7.4 cm, $D=2.2$ cm at $(4\ \mathrm{cm},0)$; pre-shock air $\phi_2\rho_2=1.17$, $p=1.01\times10^5$ Pa; post-shock air $\phi_2\rho_2=3.7579$, $v_1=574.57$ m/s, $p=6.6189\times10^5$ Pa; water $1000$, $p=1.01\times10^5$ Pa; constant extrapolation | $3072\times2048$ | shadowgraph/schlieren images of Sembian et al. at $t=4$, 17, 40, 67 µs |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.5 | 2.4 | $(\rho,v_1,v_2,p,\gamma,p_\infty,\phi_1)$: post-shock air $(3.85,567.3,0,0.664\times10^6,1.4,0,0)$, pre-shock $(1.2,0,0,0.101\times10^6,1.4,0,0)$, water $(1000,0,0,10^5,6.12,0.343\times10^9,1)$; $x\in[0,0.2208]$, $y\in[0,0.1152]$ m, column centred at $(0.0576,0.0576)$ m, shock at $x=0.05$ m; with or without a coaxial air cavity of radius 3.6 mm; non-reflecting left and right, slip walls top and bottom; run to $tv_{\mathrm s}/D=10$ ($v_{\mathrm s}$ the post-shock velocity) | about 0.89 million quadrilaterals, edge $\approx D/192$, CWENO5 | Xiang & Wang's computations; schlieren of Sembian et al. |
| [Zhang et al. (2024a)](/sources/zhang-2024.md) §4.5, Table 6 | 2.4 | $[0,0.111]\times[0,0.074]$ m, $D=0.022$ m at $(0.04,0.037)$, shock at $x=0.029$ m; post-shock air $\phi_2\rho_2=3.76$, $v_1=574.57$ m/s, $p=6.62\times10^5$ Pa; pre-shock air $1.17$, $10^5$ Pa; water 1000; extrapolation left and right, walls top and bottom; water $(4.4,\ 6\times10^8\ \mathrm{Pa})$ | $3072\times2048$ | schlieren of Sembian et al. at 4, 17, 40, 67 µs |
| Zhang et al. §4.6, Table 7 | 6 | two water columns in $[0,0.03]\times[0,0.025]$ m, diameters printed 0.064 and 0.005 m, at $(0.01,0.015)$ and $(0.017,0.011)$ m; shock at $x=0.002$ m; post-shock air $\phi_2\rho_2=6.32$, $v_1=1660.39$ m/s, $p=4.05\times10^6$ Pa; pre-shock air 1.20; extrapolation on all sides | $1920\times1600$ | MUSCL-THINC of Garrick et al. |
| Zhang et al. §4.7, Table 8 | 10 | $[0,0.03]\times[0,0.02]$ m, $D=0.008$ m at $(0.013,0.01)$, shock at $x=0.009$ m; post-shock air $6.86$, $v_1=2817.9$ m/s, $p=1.16\times10^7$ Pa; pre-shock air 1.20; extrapolation | $1920\times1280$; $480\times320$ to $1920\times1280$ at $t=25\,\mu$s | MUSCL-THINC |
| Wong et al. §6.6 | 10 | $[0,30L]\times[-10L,10L]$, $L=1$ mm, $D=8L$ at $(13L,0)$; pre-shock air $\phi_2\rho_2=1.2$, $p=10^5$ Pa; post-shock air $\phi_2\rho_2=6.8571$, $v_1=2.8179\times10^3$ m/s, $p=1.165\times10^7$ Pa; water $1000$, $p=10^5$ Pa | $1152\times768$ | first-order HLLC; the unlimited scheme |

**Droplets in their own vapour, with phase change.**
[Long, Cai & Pan (2023)](/sources/long-2023.md) §4.4 run a Mach 1.5 shock
on a liquid droplet surrounded by its vapour, with their conservative
cut-cell level-set scheme and a Riemann solver with phase change
([Riemann solvers with phase change](/methods/phase-change-riemann-solver.md)).
States are $(\rho,v_1,v_2,p,T)$ in kg/m³, m/s, Pa and K:

| Case | pre-shock vapour | post-shock vapour | droplet |
|---|---|---|---|
| n-dodecane, 2D (Eq. (38)) | $(4.38,0,0,10^5,500)$ | $(10.63,130.29,0,226613,511.19)$ | $(593.47,0,0,10^5,490)$ |
| water, 2D (Eq. (39)) | $(0.57,0,0,10^5,380.0)$ | $(1.09,345.47,0,242704,482.47)$ | $(1093.67,0,0,10^5,373)$ |

The 2D domain is $10\times10$ mm (top half computed), with the shock at
$x=2$ mm, inflow and outflow left and right and symmetry top and bottom,
on a multiresolution grid of effective resolution $2048\times1024$. The
droplet is the zero level of $-1.0+\sqrt{(x-0.35)^2+y^2}$ in mm, a radius
of 1 mm. A 3D water droplet is run on one eighth of a $10\times5\times5$ mm
domain at effective $1024\times512\times512$ (Eq. (40)). The water is a
stiffened gas with $\gamma=2.35$ and $p_\infty=10^9$ Pa, its vapour an
ideal gas, and n-dodecane has a Helmholtz-energy equation of state (§2.2).

A three-dimensional relative, the aerobreakup of a spherical water
droplet behind a helium shock (post-shock flow Mach 0.59, conditions of
Theofanous et al.), is shown by Bryngelson et al. §5.2 (Fig. 3) with
qualitative agreement for shear-induced entrainment.

## Findings across sources

**Wave systems match the experiments.** Bryngelson et al. find that
[MFC](/software/mfc.md) reproduces the primary waves (incident and
reflected shocks) and the secondary ones (Mach stems converging at the
rear stagnation point) of the Igra–Takayama interferograms (§5.2,
Fig. 2). Wong et al. find that their positivity-preserving
[WCNS](/methods/weighted-compact-nonlinear-scheme.md) (PP-WCNS-IS)
reproduces the incident, reflected and transmitted shocks, the
expansion waves and the two counter-rotating vortices of Sembian et
al.'s images (Fig. 12). Tsoutsanis et al. find all key features
(reflected expansion, transmitted wave, Mach stem, recirculation zone)
in agreement with Xiang & Wang and with Sembian et al.'s schlieren, for
both the plain column and the column with a cavity (Figs. 10–13). All
three comparisons are visual, as is Zhang et al.'s below; no source reports a quantitative error.

[Zhang et al. (2024a)](/sources/zhang-2024.md) (§4.5, Fig. 9) find that the numerical
schlieren of their [WENO5IS-THINC](/methods/thinc-reconstruction.md) scheme agrees
qualitatively with Sembian et al.'s images: incident, reflected and transmitted shocks,
Mach reflection, rarefaction focusing and the vortex pair. The water "mist" shed from the
column is, in their reading, a pseudo-capillary effect of interface sharpening, not
physics. On the two Mach 6 columns WENO5IS-THINC captures the vortices more clearly and
develops Rayleigh–Taylor and Kelvin–Helmholtz instabilities more intensely than
MUSCL-THINC, and both show a [carbuncle](/definitions/carbuncle-phenomenon.md) (§4.6,
Figs. 10–11).

**Symmetry and negative pressure at Mach 10.** In Zhang et al.'s Mach 10 column negative
pressure appears in the water behind strong rarefactions. On the resolution study
MUSCL-THINC loses mirror symmetry as the grid is refined, which they attribute to
floating-point asymmetry, while WENO5IS-THINC keeps it at every resolution (§4.7,
Figs. 12–13; [symmetry preservation](/properties/symmetry-preservation.md)).

**Phase change.** With phase change Long et al. see an additional wave
from the initial evaporation, condensation after the shock has passed,
and a larger deformation of the interface than without phase change
(§4.4.1, Figs. 14–15). They state that their finer resolution shows more
structures than earlier phase-change computations. The 3D water droplet
is compared qualitatively with Das & Udaykumar (§4.4.3).

**Negative pressure and the cavity.** In Tsoutsanis et al.'s plain
column the pressure dip below zero inside the water at $t v_{\mathrm s}/D=0.8$
is present but less pronounced than in Xiang & Wang, who used a finer
mesh ($D/333$). With the cavity, the maximum-pressure history has the
right peak timing and a slightly lower peak (§4.5). The stiffened-gas
law admits such negative pressures as long as $p+p_\infty>0$.

**Positivity at Mach 10.** Wong et al.'s Mach 10 case is the test that
the high-order scheme without its limiters fails: WCNS-IS breaks down
with an imaginary sound speed at the incident shock, in low-pressure
regions inside the column and in the vortices, while PP-WCNS-IS runs,
keeps the volume fraction within its thresholds, and resolves the
baroclinic roll-up that first-order HLLC smears (§6.6, Figs. 14–16).
See [bound preservation](/properties/bound-preservation.md) and the
[positivity-preserving flux limiter](/methods/positivity-preserving-flux-limiter.md).

## Qualifications

- Tsoutsanis et al. print the column diameter as $D=96$ mm. With the
  printed centre at $x=57.6$ mm and the shock at $x=50$ mm, a 96 mm
  column would contain the initial shock; a 9.6 mm column (radius
  4.8 mm, around the 3.6 mm cavity) lies entirely downstream of it and
  fits the 0.2208 m × 0.1152 m domain: the printed 96 mm is
  inconsistent with the printed geometry, which 9.6 mm fits *(compiler
  check, not in the sources)*. Their text also calls
  the column a "water droplet" and a "water bubble".
- Wong et al.'s Sembian setup uses $D=2.2$ cm, while Tsoutsanis et al.
  follow Xiang & Wang's geometry and compare with the same experiment;
  the post-shock states differ slightly ($v_1=574.57$ against
  $567.3$ m/s, $p=6.6189\times10^5$ against $6.64\times10^5$ Pa).
- Wong et al.'s figure caption calls the experimental images
  shadowgraphs and the text calls them grey schlieren images.
- As printed, Long et al.'s droplet centre is $x=0.35$ mm, with the
  shock at $x=2$ mm and the post-shock vapour moving in $+x$ *(compiler
  check, not in the sources: a shock that moves in $+x$ leaves the shocked
  vapour at $x<2$ mm, and a 1 mm droplet about $x=0.35$ mm spans
  $x\in[-0.65,1.35]$ mm, so it would start inside the shocked region and
  never be hit by the shock)*. The printed geometry and the described
  test therefore disagree; the text does not state the n-dodecane droplet
  radius either. *(Compiler check, not in the sources: the liquid–vapour
  density ratio is $593.47/4.38\approx135$ for n-dodecane and
  $1093.67/0.57\approx1900$ for water, not the air–water 1000 of the other
  setups.)*
- Zhang et al.'s Mach 6 post-shock pressure, $4.05\times10^6$ Pa, does not match their
  density and velocity. *(Compiler check, not in the sources: the ideal-gas
  Rankine–Hugoniot state of a Mach 6 shock into air at $\rho=1.2$ kg/m³, $p=10^5$ Pa,
  $\gamma=1.4$ is $\rho=6.322$, $v_1=1660.4$ m/s, $p=4.183\times10^6$ Pa, the printed
  $\rho$ and $v_1$; $4.05\times10^6$ Pa belongs to Mach 5.9, whose velocity is
  $1631$ m/s.)* Their Mach 10 state matches the same relations ($6.857$, $2817.9$ m/s,
  $1.165\times10^7$ Pa, the values Wong et al. print in full) *(compiler check, not in the
  sources)*. The Mach 6 cylinder diameter printed as $0.064$ m cannot fit the
  $0.03\times0.025$ m domain about the printed centre; $0.0064$ m would *(compiler check,
  not in the sources: radius $0.032$ m against a centre $0.01$ m from the left boundary)*.
- Zhang et al.'s Mach 2.4 states are Wong et al.'s rounded ($3.76$ against $3.7579$,
  $6.62\times10^5$ against $6.6189\times10^5$ Pa, the same $v_1=574.57$ m/s), but with the
  pre-shock pressure printed as $10^5$ instead of Wong et al.'s $1.01\times10^5$ Pa.
  *(Compiler check, not in the sources: Mach 2.4 into $\rho=1.17$ kg/m³ gives
  $v_1=574.57$ m/s and $p=6.619\times10^5$ Pa from $1.01\times10^5$ Pa, but $571.7$ m/s and
  $6.553\times10^5$ Pa from $10^5$ Pa, so the printed post-shock state belongs to Wong et
  al.'s pre-shock pressure.)*
- Bryngelson et al.'s Mach 1.47 run prints no grid or state, so it
  cannot be placed against the others quantitatively.

# Citations

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §5.2, Figs. 2–3 (arXiv v1).
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.5, Table 8, Figs. 11–12; §6.6, Table 9, Figs. 13–16 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.5, Eq. (44), Figs. 9–13.
- [Long, Cai & Pan (2023)](/sources/long-2023.md) — §2.2; §4.4, Eqs. (38)–(40), Figs. 14–15: shock on droplets in their vapour, with and without phase change.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §§4.5–4.7, Tables 6–8, Figs. 9–13: Mach 2.4 column against Sembian et al., Mach 6 two columns, Mach 10 column and its symmetry.
