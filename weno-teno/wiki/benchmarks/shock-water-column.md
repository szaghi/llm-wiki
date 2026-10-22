---
type: Benchmark
title: "Shock–water-column interaction"
description: "A planar shock in air hitting a cylindrical water column (or a spherical droplet), the liquid counterpart of the shock–bubble problem: validation against the interferograms of Igra and Takayama and the schlieren images of Sembian et al. at Mach 1.47 and 2.4, a column with an air cavity, and a Mach 10 case that tests positivity of high-order schemes."
status: established
aliases: [shock–water column, shock–water cylinder, shock–droplet interaction, water column in air, shocked water cylinder]
tags: [benchmark, multiphase, interface-capturing, positivity]
timestamp: 2026-10-22T12:00:00Z
---

# Shock–water-column interaction

A planar shock travelling through air hits a cylinder of water, about
a thousand times denser than the air in every setup below. The shock
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
at high Mach number, a robustness test for high-order schemes.

Page-local symbols: $\phi_1$ the water volume fraction, $D$ the column
diameter, $(\gamma,p_\infty)$ the stiffened-gas constants. Water is
$(\gamma,p_\infty)=(6.12,\ 3.43\times10^8\ \mathrm{Pa})$ and air
$(1.4,0)$ in every setup below that prints them.

## Setups

| Source | Shock Mach | Setup as printed | Grid | Compared with |
|---|---|---|---|---|
| [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) §5.2 | 1.47 | 4.8 mm water cylinder in air, 2D; parameters deferred to Meng & Colonius | not printed | holographic interferograms of Igra & Takayama at $t=16$ and $32\,\mu$s |
| [Wong et al. (2021)](/sources/wong-2021.md) §6.5 | 2.4 | domain 11.1 cm × 7.4 cm, $D=2.2$ cm at $(4\ \mathrm{cm},0)$; pre-shock air $\phi_2\rho_2=1.17$, $p=1.01\times10^5$ Pa; post-shock air $\phi_2\rho_2=3.7579$, $v_1=574.57$ m/s, $p=6.6189\times10^5$ Pa; water $1000$, $p=1.01\times10^5$ Pa; constant extrapolation | $3072\times2048$ | shadowgraph/schlieren images of Sembian et al. at $t=4$, 17, 40, 67 µs |
| [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.5 | 2.4 | $(\rho,v_1,v_2,p,\gamma,p_\infty,\phi_1)$: post-shock air $(3.85,567.3,0,0.664\times10^6,1.4,0,0)$, pre-shock $(1.2,0,0,0.101\times10^6,1.4,0,0)$, water $(1000,0,0,10^5,6.12,0.343\times10^9,1)$; $x\in[0,0.2208]$, $y\in[0,0.1152]$ m, column centred at $(0.0576,0.0576)$ m, shock at $x=0.05$ m; with or without a coaxial air cavity of radius 3.6 mm; non-reflecting left and right, slip walls top and bottom; run to $tv_{\mathrm s}/D=10$ ($v_{\mathrm s}$ the post-shock velocity) | about 0.89 million quadrilaterals, edge $\approx D/192$, CWENO5 | Xiang & Wang's computations; schlieren of Sembian et al. |
| Wong et al. §6.6 | 10 | $[0,30L]\times[-10L,10L]$, $L=1$ mm, $D=8L$ at $(13L,0)$; pre-shock air $\phi_2\rho_2=1.2$, $p=10^5$ Pa; post-shock air $\phi_2\rho_2=6.8571$, $v_1=2.8179\times10^3$ m/s, $p=1.165\times10^7$ Pa; water $1000$, $p=10^5$ Pa | $1152\times768$ | first-order HLLC; the unlimited scheme |

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
three comparisons are visual; no source reports a quantitative error.

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
- Bryngelson et al.'s Mach 1.47 run prints no grid or state, so it
  cannot be placed against the others quantitatively.

# Citations

- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §5.2, Figs. 2–3 (arXiv v1).
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.5, Table 8, Figs. 11–12; §6.6, Table 9, Figs. 13–16 (arXiv v1).
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.5, Eq. (44), Figs. 9–13.
