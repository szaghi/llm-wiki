---
type: Benchmark
title: "Gas–liquid Riemann problems"
description: "One-dimensional Riemann problems between an ideal gas and a stiffened-gas liquid, with exact solutions: compressed air against water (Cocchi et al.), water at a billion pascals against air, water at two gigapascals moving into air, a gas–water double rarefaction and a rarefaction reflected into water; they test interface location, contact oscillations and robustness."
status: established
aliases: [gas–water Riemann problem, gas–liquid shock tube, water–air shock tube, Cocchi gas–liquid Riemann problem, two-medium Riemann problems]
tags: [benchmark, multiphase, interface-capturing, riemann-solver]
timestamp: 2026-10-22T20:00:00Z
---

# Gas–liquid Riemann problems

A gas–liquid Riemann problem is a shock tube whose two initial states
are different materials: an ideal gas on one side and a liquid, closed
by the [stiffened-gas equation of state](/definitions/stiffened-gas-equation-of-state.md),
on the other. The exact solution is a three-wave fan with a
material contact in the middle, across which $p$ and the velocity are
continuous while the density and the equation-of-state constants jump.
The tests measure whether a scheme places the contact correctly, keeps
pressure and velocity free of oscillations there, and survives pressure
ratios of about $10^4$. They are the one-dimensional companions of
the [shock–water-column](/benchmarks/shock-water-column.md) and
gas-bubble-in-water [shock–bubble](/benchmarks/shock-bubble-interaction.md)
problems.

States are listed as $(\rho,v,p,\gamma,p_\infty)$ unless a row says
otherwise; $\phi_k$ is the volume fraction of phase $k$ (page-local).

## Problems in the sources

**Highly compressed air against water (Cocchi et al.).** Non-dimensional
air $(1.241,0,2.753,1.4,0)$ for $x<0$ against water
$(0.991,0,3.059\times10^{-4},5.5,1.505)$ for $x\ge0$.
[Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) Ex. 5 run it on
$[-5,5]$ with $N_x=300$ to $t=1$ (attributed to Cheng et al.);
[Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) §4.3 run "the
2D equivalent" on $[-1,1]^2$ with a mixed triangle–quadrilateral mesh
of 100 edges per side to $t=0.2$, against the exact solution. Tsoutsanis
et al.'s printed tuple is garbled (see Qualifications); their
description (compressed air on the left, water at atmospheric pressure
on the right), their constants (air 1.4, water 5.5 with
$p_\infty=1.505$) and the readable numbers coincide with Zheng et al.'s
Ex. 5 *(compiler check, not in the sources)*.

**Water at $10^9$ Pa against air.** [Wong et al. (2021)](/sources/wong-2021.md)
§6.3 (after Chen & Liang and Wang et al.): on $[0,1.5]$ m, water
($\phi_1\rho_1=1000$, $p=10^9$ Pa, $\phi_1=1-10^{-8}$) for $x<0.8$ and
air ($\phi_2\rho_2=20$, $p=10^5$ Pa, $\phi_1=10^{-8}$) for $x\ge0.8$,
at rest; water $(6.12,\ 3.43\times10^8\ \mathrm{Pa})$, air $(1.4,0)$;
200 points, $\Delta t=1.25\times10^{-6}$ s, $t=3\times10^{-4}$ s;
reference on 4000 points; a water–air version of the
[Sod problem](/benchmarks/sod-and-lax-shock-tubes.md) with a pressure
ratio of $10^4$.
[Nguyen et al. (2022)](/sources/nguyen-2022.md) §3.2 run a version
with pure phases: water $(\rho,v,p,\gamma)=(1000,0,10^9\ \mathrm{Pa},4.4)$
for $0\le x\le0.75$ m against air $(1,0,10^5\ \mathrm{Pa},1.4)$, on
100 and 1000 cells to $t=240\,\mu$s, compared with an earlier
computation; the water's $p_\infty$ is not printed for this test (their
underwater-explosion water has $p_\infty=6\times10^8$ Pa). They solve
the [multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)
in pressure–temperature equilibrium with MUSCL and HLLC.

**Water at 2 GPa moving into air (Saurel & Abgrall).**
[Bai & Li (2022)](/sources/bai-2022.md) §3.1.2, Eq. (32), with the
temperature form of the stiffened gas: water
$(\gamma,C_p,p_\infty)=(2.788103,\ 4190,\ 7.862511\times10^8\ \mathrm{Pa})$
at $\rho=1499.77$ kg/m³, $v=818.52$ m/s, $p=2.0$ GPa, $T=691.35$ K,
against air $(1.4,\ 1004.85,\ 0)$ at $\rho=1.224$ kg/m³, $v=0$,
$p=1.03$ bar, $T=293.15$ K, interface at $x=0$, domain $[-5,5]$ m (run
as a strip $[-5,5]\times[0,1]$ m), $t=1.807$ ms; two-level adaptive
grids with 50 and four-level grids with 200 elements/m on the top level,
degree $N=2$. Unlike the other problems, the liquid moves into the gas
at about $800$ m/s, so the wave fan is not that of a tube at rest.

**Gas–water double rarefaction.** Zheng et al. Ex. 6 (after Liu, Khoo
& Yeo): $(0.01,-100,100,1.4,0)$ for $x<0$ against
$(1.002,0,50,7.15,3309)$, $[-5,5]$, $N_x=200$, $t=0.01$.

**Strong rarefaction reflected into water.** Zheng et al. Ex. 7:
water $(1000,0,25000,7.15,3309)$ for $x<2$ against gas
$(1,-10,1,1.4,0)$, $[-5,5]$, $N_x=200$, $t=0.25$.

**Recalled, not rerun.** [Bryngelson et al. (2021)](/sources/bryngelson-2021.md)
§5.5 state that [MFC](/software/mfc.md) matches the exact solutions of
the Cocchi et al. gas–liquid shock tube and of a Mach 8.96 helium shock
on an air interface without spurious oscillations, results shown in an
earlier MFC paper.

**Gas–gas relatives.** Zheng et al. Ex. 4 (after Liu, Khoo & Wang)
drives a strong shock into a gas–gas interface,
$(0.3856,27.0784,100,5/3,0)$ against $(1,0,1,1.4,0)$ on $[-500,500]$,
$N_x=200$, $t=20$; [Renac (2021)](/sources/renac-2021.md) §7.2 runs six
two-component ideal-gas Riemann problems (see
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md)).
Nguyen et al. §3.2 run a two-fluid Sod tube, $(1,0,1,1.4)$ against
$(0.125,0,0.1,1.667)$ in $(\rho,v,p,\gamma)$, on 100 to 800 cells to
$t=0.2$, without spurious oscillations. Bai & Li §3.1.1 run an
air–helium tube with a hot driver, air
$(\rho,p,T)=(1.2036\ \mathrm{kg/m^3},\ 10.1\ \mathrm{bar},\ 2931.5\ \mathrm K)$
against helium $(0.167\ \mathrm{kg/m^3},\ 1.01\ \mathrm{bar},\ 293.15\ \mathrm K)$,
$\gamma=1.4$ and $1.63$, both at rest, on $[-5,5]$ m to $t=1.7817$ ms.

## Findings across sources

**Sharp-interface DG.** Bai & Li's discontinuous Galerkin solver with
ghost-fluid states in cut cells ([level-set methods](/methods/level-set-method.md))
agrees with the exact solution of the 2 GPa water–air problem except for
weak temperature oscillations, which weaken on the four-level grid
(Fig. 9); on the air–helium tube both grids agree "very well" with the
exact solution and keep the density jump sharp (Fig. 8). Nguyen et al.
report "very good agreement" with the reference on their
$10^9$ Pa problem (Fig. 10).

**Interface location.** Zheng et al.'s conservative sharp-interface
scheme ([level-set methods](/methods/level-set-method.md)) gets the
interface location right on Ex. 5–7. On Ex. 5 it shows "a small trough
along the interface in the density plot" that the DG scheme of Cheng
et al. does not show, but is otherwise "a good approximation to the
exact solution" (Fig. 9). On Ex. 7 a conservative-variable WENO-JS
scheme "produces a jump at the interface" (Fig. 11). On the gas–gas
Ex. 4 a finite-difference WENO ghost-fluid method misplaces both the
shock and the interface (Fig. 8).

**Oscillations and order.** Tsoutsanis et al. find CWENO5 (a fifth-order
central polynomial with second-order directional polynomials) less
oscillatory than WENO3 on the Cocchi problem, and from then on use only
[CWENO](/methods/cweno.md) (Fig. 5). Wong et al. find that
PP-WCNS-IS ([WCNS](/methods/weighted-compact-nonlinear-scheme.md) with
positivity limiters) resolves the interface and the shock with a few
points where first-order HLLC merges them, at the price of a slightly
larger undershoot and overshoot at the expansion fan (Figs. 7–8).

The three finite-difference and finite-volume high-order sources (Zheng et al., Tsoutsanis et al., Wong et al.) reconstruct or interpolate
primitive-type variables at the interface (Zheng et al. primitive
variables in characteristic fields, Tsoutsanis et al. primitive
variables, Wong et al. characteristic variables of the primitive
system); the comparisons with conservative-variable schemes (Zheng et
al.'s WENO-JS) are where the interface jumps appear. See
[five- and six-equation models](/definitions/five-equation-model.md)
for the interface-equilibrium argument. Nguyen et al. also reconstruct
primitive variables $(p,v,T,\phi_k)$ and advance them directly; the
cost in conservation is discussed under
[multicomponent Euler equations](/definitions/multicomponent-euler-equations.md).

## Qualifications

- Tsoutsanis et al. print the state vector as
  $(\rho_1,\rho_2,v_1,v_2,p,\phi_1)$ with the left state
  "(1.241, 0, 0, 2.753, 1.4, 1)" and the right state
  "(0, 0.991, 0, 3.059x10$^{-4}$, 0)": the left tuple has $\gamma$ in
  the pressure slot and the right one has five entries. The reading
  $\rho_1=1.241$, $p=2.753$ (air) and $\rho_2=0.991$,
  $p=3.059\times10^{-4}$ (water) rests on Zheng et al.'s Ex. 5, which
  prints the same numbers in full *(compiler check, not in the
  sources)*.
- The stiffened-gas constants of water differ between problems and
  sources ($\gamma=5.5$, $6.12$, $7.15$), so the problems do not share a
  water model.
- The evidence is visual comparison with exact or reference solutions;
  no source reports an error norm for these problems.
- Nguyen et al.'s Fig. 10 labels the pressure axis in MPa with a
  maximum of 1, while the text sets the water at $10^9$ Pa; the text
  also labels the water side "$\phi_1=1$", whereas their interface
  advection test of §3.1 makes water phase 2.
- Bai & Li's air temperature of 2931.5 K is consistent with their
  temperature form: $\frac{\gamma-1}{\gamma}C_p\rho T\approx1.013\times10^6$
  Pa, the printed 10.1 bar *(compiler check, not in the sources)*.

# Citations

- [Zheng, Shu & Qiu (2021)](/sources/zheng-2021.md) — §4, Ex. 4–7, Figs. 8–11.
- [Tsoutsanis et al. (2021)](/sources/tsoutsanis-2021.md) — §4.3, Eq. (42), Fig. 5.
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.3, Table 6, Figs. 7–8 (arXiv v1).
- [Bryngelson et al. (2021)](/sources/bryngelson-2021.md) — §5.5 (recalled results only; arXiv v1).
- [Renac (2021)](/sources/renac-2021.md) — §7.2 (gas–gas problems only; arXiv v3).
- [Nguyen et al. (2022)](/sources/nguyen-2022.md) — §3.2, Figs. 6–10.
- [Bai & Li (2022)](/sources/bai-2022.md) — §3.1.1–3.1.2, Eqs. (31)–(32), Figs. 8–9.
