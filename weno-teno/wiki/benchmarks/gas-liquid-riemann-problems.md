---
type: Benchmark
title: "Gas–liquid Riemann problems"
description: "One-dimensional gas–liquid Riemann problems with exact or reference solutions: compressed air against water, water at a billion pascals and at a terapascal against air, a weak water shock through an air interface, water at two gigapascals moving into air, gas–water rarefactions and liquid–vapour tubes with phase change; they test interface location, contact oscillations and robustness."
status: established
aliases: [gas–water Riemann problem, gas–liquid shock tube, water–air shock tube, Cocchi gas–liquid Riemann problem, two-medium Riemann problems]
tags: [benchmark, multiphase, interface-capturing, riemann-solver]
timestamp: 2026-10-24T06:00:00Z
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
otherwise, $p_\infty$ being the stiffened-gas constant $p_{\infty,k}$ of the
state's material with the phase index dropped; $\phi_k$ is the volume
fraction of phase $k$ (page-local).

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
[Jiang et al. (2024)](/sources/jiang-2024.md) §5.1.3 run the problem,
citing Gu et al., on $[-5,5]$ to $t=1$ with their Lagrangian
weighted-least-squares particle method (pairwise Roe-type Lagrangian
Riemann solver with [WENO-Z+](/methods/weno-z-plus.md)-type
reconstruction on virtual points, LWLS-WENO-Z), each particle carrying
its own phase's stiffened-gas law, but print the water pressure as
$0.000359$ (see Qualifications). They capture it "without the
additional treatment" of the interface that mesh-based WENO schemes
need, and the solution converges under particle refinement (Fig. 8).

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

[Zhang et al. (2024a)](/sources/zhang-2024.md) §4.2 (Table 3, set-up of Saurel et al.)
run the same states on the five-equation model: on $[0,1]$ m, water
($\phi_1\rho_1=1000$, $p=10^9$ Pa) for $x<0.75$ against air ($\phi_2\rho_2=1$,
$p=10^5$ Pa), at rest, with water $(\gamma,p_\infty)=(4.4,\ 6\times10^8\ \mathrm{Pa})$ and
extrapolation boundaries; $N_x=128$ and $512$ to $t=240\,\mu$s against WENO5IS-THINC on
12800 cells.

**Shock on a water–air interface (Shukla).** Zhang et al. (2024a) §§4.3–4.4 (Tables 4–5) run two
cases on $[0,5]$ m with the same water constants. *Static interface:* shocked water
($\phi_1\rho_1=1230$, $v=432.7$ m/s, $p=10^9$ Pa) on $0<x<1.31$, water
$(1000,0,10^5)$ on $1.31<x<2$, air $(1,0,10^5)$ beyond, $t=1000\,\mu$s, $N_x=128$ and
$512$. *Moving interface,* in the shock frame: shocked water $(1230,-1878.1,10^9)$ on
$0<x<3.62$, water $(1000,-2310.9,10^5)$ on $3.62<x<4.31$, air $(1,-2310.9,10^5)$ beyond,
$t=1000\,\mu$s, $N_x=512$ and $2048$ (the domain is not restated). Reference solutions on
12800 cells; $L_1$ errors on $N_x=128,\dots,2048$ (Fig. 8). *(Compiler check, not in the
sources: in the static case mass conservation gives the shock speed
$1230\cdot432.7/230\approx2314$ m/s and momentum the jump
$1000\cdot2314\cdot432.7\approx1.001\times10^9$ Pa, consistent with the printed states.)*

**Cavitation and a mainly-vapour tube (water and vapour, with phase change).**
[Wakimura et al. (2024)](/sources/wakimura-2024.md) §§4.1–4.2 run two liquid–vapour tubes on
the six-equation model with infinite-rate relaxation
([five- and six-equation models](/definitions/five-equation-model.md)), water and vapour with
the stiffened-gas constants of their Table 1, outflow boundaries, CFL 0.5. States are
$(\phi_1,\rho_1,\rho_2,v,p)$ in kg/m³, m/s, Pa:

| Problem | left | right | cells | $t$ |
|---|---|---|---|---|
| cavitation tube, $\lvert v_0\rvert=2$ m/s (Eq. (46)) | $(0.99,1150,0.63,-2,10^5)$ | $(0.99,1150,0.63,2,10^5)$ | 500 | 3.2 ms |
| cavitation tube, $\lvert v_0\rvert=500$ m/s | as above with $\mp500$ | | 5000 | 0.58 ms |
| mainly-vapour shock tube (Eq. (47), after Chiapolino et al.) | $(2.7399\times10^{-4},1034.8,1.1344,0,2\times10^5)$, $T=394.25$ K | $(1.3702\times10^{-4},1094.0,0.59969,0,10^5)$, $T=372.88$ K | 200 | 0.8 ms |

on $[0,1]$ m with the jump at $x=0.5$ m, $T_1=T_2=354.728$ K in the cavitation tube, and a
liquid mass fraction of 0.2 on both sides of the shock tube. Each is run with pressure
relaxation alone and with the thermal and chemical relaxations (phase change). *(Compiler
check, not in the sources: the temperature form gives
$\rho_1=(10^5+10^9)/(1.35\cdot1816\cdot354.728)=1150.0$ and
$\rho_2=10^5/(0.43\cdot1040\cdot354.728)=0.630$ kg/m³ for the cavitation tube.)*

**Air–water tube of Beig & Johnsen.** [Huang & Johnsen (2023)](/sources/huang-2023.md)
§4.2, Eq. (49), states in $(\rho_1,\rho_2,v,p,\phi_1)$ with phase 1 air and
phase 2 water: $(1,881.6,0.184,714,0)$ for $0\le x<0.7$ against
$(1,881.6,0,0.714,1)$ for $0.7\le x\le1$. The air is an ideal gas
($\gamma=1.4$), the water a stiffened gas with $\gamma=2.35$,
$p_\infty=10^9$ Pa and energy constant $-1.167\times10^3$ J/kg. The run uses
1000 cells, CFL 0.4 and $t=0.1$, with the
[phase-field](/methods/phase-field-method.md) thickness parameter equal to
$\Delta x$. *(Compiler check, not in the sources: the pressure ratio is
$714/0.714=1000$.)*

**Water at $10^{12}$ Pa against air.** [Paula et al. (2023)](/sources/paula-2023.md)
§7.4.2 put water of density 1000 kg/m³ at
$10^{12}$ Pa against air at $10^5$ Pa of density 1 or 10 kg/m³, with the
interface at $x=0.6$ m on a 1 m domain. The water is a stiffened gas
($\gamma=4.4$, $p_\infty=6\times10^8$ Pa), the air ideal ($\gamma=1.4$).
They use 1024 cells, zero-gradient boundaries, CFL 0.4 and
$t=8.3\,\mu$s.

**Weak shock in water through an air interface.** Paula et al. §7.4.1:
on a 1 m domain, a shock at $x=0.3$ m in water runs into an air interface
at $x=0.7$ m. The states in $(\rho,v,p)$ are post-shock water
$(1001.8658\ \mathrm{kg/m^3},\ 3.0337923\ \mathrm{m/s},\ 5.0421806\times10^6\ \mathrm{Pa})$,
pre-shock water $(1000,0,10^5)$ and air $(1,0,10^5)$, with the water and air
constants of the previous problem (Table 2). They use 1024 cells,
zero-gradient boundaries, $t=600\,\mu$s and the THINC steepness
$\beta_{\mathrm T}\in\{0.325,1,3\}$.

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

**Liquid–vapour tubes with phase change.** [Long et al. (2023)](/sources/long-2023.md)
§4.1 run four Riemann problems between a liquid and its vapour, with the
exact solutions of Fechter et al.'s phase-change Riemann problem as
reference. States are $(\rho,v,p,T)$, the liquid always on one side:

| Problem | left | right | $t$ |
|---|---|---|---|
| n-dodecane, evaporation (Eq. (28)) | $(584.08,0,1.5\times10^5,500)$ | $(4.38,0,1.0\times10^5,500)$ | 0.7 ms |
| n-dodecane, condensation (Eq. (30)) | $(4.38,0,1.0\times10^5,500)$ | $(584.05,0,1.4\times10^5,500)$ | 0.7 ms |
| water, evaporation (Eq. (31)) | $(1073.57,0,1.5\times10^5,380)$ | $(0.68,0,1.2\times10^5,380)$ | 0.3 ms |
| water, condensation (Eq. (32)) | $(0.68,0,1.2\times10^5,380)$ | $(1073.56,0,1.4\times10^5,380)$ | 0.3 ms |

Units are kg/m³, m/s, Pa and K, the discontinuity at $x=0.5$ m on the
n-dodecane tubes. n-Dodecane uses a Helmholtz-energy equation of state.
Water and vapour are stiffened gases: liquid $\gamma=2.35$,
$p_\infty=10^9$ Pa, vapour $\gamma=1.33$, $p_\infty=0$ (§2.2). The grids
have 200 and 2000 uniform cells, plus a multiresolution grid of effective
resolution 409600 for the n-dodecane condensation. The Hertz–Knudsen
coefficients of the phase-change model differ per problem. The fan has
four waves: two outer waves, the phase interface and a contact
([Riemann solvers with phase change](/methods/phase-change-riemann-solver.md)).

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
Huang & Johnsen (2023) §4.1, Eq. (48), run an air–helium tube on $[0,2]$:
air $(\rho,v,p)=(1,0,1)$, $\gamma=1.4$, for $x<1$ against helium
$(0.125,0,0.1)$, $\gamma=1.6$, with 200 cells, CFL 0.4 and $t=0.4$.
*(Compiler check, not in the sources: these are the states of Chamarthi (2023a)'s
Abgrall–Karni tube below on a domain twice as long, run twice as long.)*
[Chamarthi (2023a)](/sources/chamarthi-2023.md) runs two gas–gas problems on the
[five-equation model](/definitions/five-equation-model.md), with states in
$(\phi_1\rho_1,\phi_2\rho_2,v,p,\phi_1,\gamma)$ and CFL 0.1 (arXiv v2):

- the Abgrall–Karni two-fluid tube, $(1,0,0,1,1,1.4)$ for $x<0$ against
  $(0,0.125,0,0.1,0,1.6)$, on $[-0.5,0.5]$ with 200 cells to $t=0.2$
  (Ex. 4.14) *(compiler check, not in the sources: the states of Nguyen
  et al.'s two-fluid Sod above, with $\gamma=1.6$ instead of $1.667$ on the
  right)*;
- Abgrall's shock–curtain problem, $(1.3765,0,0.3948,1.57,1,1.4)$ on
  $[0,0.25)$, $(1,0,0,1,1,1.4)$ on $[0.25,0.4)\cup[0.6,1)$ and a curtain
  $(0,0.138,0,1,0,1.67)$ on $[0.4,0.6)$, with 200 cells to $t=0.3$
  (Ex. 4.15).

[Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) (§5.2.1, Fig. 13;
arXiv v1) run an air–helium tube ($\gamma=1.4$ against $1.667$) on $[0,1]$
with 200 cells to $t=0.15$. They use the sharp-interface
[level-set method](/methods/level-set-method.md) of
[JAX-Fluids](/software/jax-fluids.md) and HLLC, and do not print the
initial states.

[Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) run two gas–gas
problems in the five-equation (Kapila) model, with states in
$(\rho_1,\rho_2,v,p,\phi_1)$ (phase densities, volume fraction of
fluid 1):

- a shock–interface interaction with pressure ratio 100 (Ex. 4.4, after
  Liu et al. as they cite it): $(0.3884,\ 1,\ 27.1123\sqrt{10^5},\ 10^7,\ 10^{-10})$
  for $x<0.2$, $(0.1,1,0,10^5,10^{-10})$ on $0.2<x<0.3$ and
  $(0.1,1,0,10^5,1-10^{-10})$ for $x>0.3$, $\gamma_1=5/3$,
  $\gamma_2=1.4$, on $[0,1]$ with 200 cells and outflow boundaries, to
  $t=10^{-4}$;
- a two-phase Lax tube (Ex. 4.6): $(0.445,0.5,0.698,3.528)$ for $x<0$
  and $(0.445,0.5,0,0.571)$ for $x>0$, with the volume fraction
  $\phi_1=x+0.5$ varying linearly across $[-0.5,0.5]$, $\gamma_1=1.4$,
  $\gamma_2=1.6$, 1000 cells, outflow, $t=0.17$, against a VFRoe-ncv
  reference on 100,000 cells.

## Findings across sources

**Holding the interface thickness.** Huang & Johnsen's
[phase-field](/methods/phase-field-method.md) term keeps the material
interface of the air–helium tube at 6–7 cells for a thickness parameter of
$1.5\Delta x$, while without it the interface keeps thickening; with the
term the volume fraction is insensitive to the TVD limiter (§4.1,
Figs. 2–3). A parameter of $0.1\Delta x$ gives 1–2 cells and $2\Delta x$
gives 8–9; below $\Delta x$ mass overshoots can appear near the
interface, and they recommend a parameter between $\Delta x$ and
$2\Delta x$ (Fig. 4). On the air–water tube the interface stays at 4–5
cells (§4.2, Fig. 5).

**Extreme ratios with the discrete equations method.** Paula et al.'s
[DEM](/methods/discrete-equations-method.md) scheme with time-averaged
[THINC](/methods/thinc-reconstruction.md) agrees "perfectly" with a
published reference solution and the exact solution on the $10^{12}$ Pa tube at
density ratio 100, and also runs at ratio 1000 (Fig. 15). On the weak-shock
problem the computed interface position matches the theoretical one for
every $\beta_{\mathrm T}$, and "in contrast to" an earlier diffuse-interface
computation the shock-front position is reproduced without oscillations
whatever the interface diffusion. Only $\beta_{\mathrm T}=0.325$ shows
small deviations of the air pressure and velocity on the liquid side. No
relaxation is needed, because the two-phase Riemann problem enforces
mechanical equilibrium (§7.4.1, Figs. 13–14).

**Phase change.** Long et al. find that the mass flux of the phase-change
model must be evaluated from the states adjacent to the phase interface:
taken from the initial left and right states it converges to a wrong
solution (§4.1.1, Fig. 4). The density-ratio closure of their approximate
solver errs by about $11.6\%$ at first, against exact interfacial
solutions recorded in the cut cell, and the error then drops quickly to
zero (Fig. 5). In the condensation tubes the interval between phase
interface and contact, $4.9\times10^{-5}$ m for n-dodecane and
$2.6\times10^{-6}$ m for water, is unresolved on 2000 cells, without
spurious waves or instability (§4.1.2, §4.1.4).

**THINC hybrids against plain WENO and MUSCL.** On the $10^9$ Pa water–air tube,
Zhang et al. (2024a)'s WENO5IS-THINC sharpens the interface and places the shock and rarefaction
more accurately than WENO5IS alone and the MUSCL-THINC of Garrick et al. (§4.2, Fig. 5).
On the shocked static interface WENO5IS alone oscillates at the transmitted shock and the
head of the rarefaction, and both THINC hybrids suppress this; on the moving interface the
oscillations are stronger and a "remarkable discrepancy in the shock position" remains at
$N_x=512$ (§§4.3–4.4, Figs. 6–7). In $L_1$ the THINC hybrids converge at roughly first
order, WENO5IS "basically lower than one", and WENO5IS-THINC has the smallest errors
(Fig. 8). On Wakimura et al.'s mainly-vapour tube the BVD schemes capture the contact at
$x\approx0.6$ m in about 3–4 cells, MUSCL in more, and the pressure–temperature results
agree with the four-equation results of Chiapolino et al.; on the cavitation tube the BVD
and MUSCL solutions are close (mass-fraction differences at most $1.49\times10^{-6}$ and
$6.00\times10^{-5}$ for the two speeds) and agree with Pelanti & Shyue (§§4.1–4.2,
Figs. 1–3; [BVD](/definitions/boundary-variation-diminishing.md)).

**Sharp-interface DG.** Bai & Li's discontinuous Galerkin solver with
ghost-fluid states in cut cells ([level-set methods](/methods/level-set-method.md))
agrees with the exact solution of the 2 GPa water–air problem except for
weak temperature oscillations, which weaken on the four-level grid
(Fig. 9); on the air–helium tube both grids agree "very well" with the
exact solution and keep the density jump sharp (Fig. 8). Nguyen et al.
report "very good agreement" with the reference on their
$10^9$ Pa problem (Fig. 10).

**Gas–gas interfaces, diffuse and sharp.** On two gas–gas problems,
Chamarthi (2023a) finds no oscillations at the material interface. The author's
[gradient-based reconstruction](/methods/gradient-based-reconstruction.md)
MIG4 gives the thinnest interface. The volume-fraction equation is written
in the non-conservative form of Johnsen & Colonius, and its source term uses
an HLLC-consistent interface velocity (Eq. (13); Ex. 4.14–4.15; Appendix A,
Eqs. (93)–(95)). Bezgin et
al.'s sharp-interface run places the interface and the shock correctly and
shows slight density oscillations at the interface. They call these
consistent with the original method of Hu et al., since no isobaric fix is
applied (§5.2.1). Yan et al.'s bound-preserving
[OEDG](/methods/oedg.md) scheme shows no visible oscillations at the
interface on the shock–interface problem (Fig. 6), and on the two-phase
Lax tube both their scheme and its variant with the averaged
discretization of the non-conservative source (AVE) agree with the
reference (Fig. 8); on the shock–interface run the ratio of the
interior-source part to the flux part of their bound-preserving
time-step bound stays far below one, as the authors state (Fig. 9).

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
- For the compressed-air–water problem, Jiang et al. (2024, §5.1.3)
  print the initial water pressure as $0.000359$, while Zheng, Shu &
  Qiu (2021, Ex. 5) and Tsoutsanis et al. (2021, §4.3) print
  $3.059\times10^{-4}$ for what all three present as the same problem
  (Jiang et al. attribute it to Gu et al., Zheng et al. to Cheng et
  al.). The papers do not show which value their runs used; the
  difference, $5.3\times10^{-5}$, is $3.5\times10^{-5}$ of
  $p+p_\infty\approx1.5053$, so it hardly changes the water's sound
  speed *(compiler check, not in the sources)*. It is recorded as
  a difference of printed data, not resolved.
- The stiffened-gas constants of water differ between problems and
  sources ($\gamma=4.4$, $5.5$, $6.12$, $7.15$), so the problems do not share a
  water model.
- The evidence is visual comparison with exact or reference solutions,
  except Zhang et al. (2024a, Fig. 8), whose $L_1$ convergence of the shocked
  water–air interface problems is plotted, not tabulated.
- Wakimura et al.'s text calls $\rho_2=1150$ kg/m³ "the gas density" of the cavitation
  tube; their Eq. (46) and the liquid volume fraction $0.99$ make it the liquid density
  $\rho_1$, as the table above reads it.
- Zhang et al. (2024a)'s water ($\gamma=4.4$, $p_\infty=6\times10^8$ Pa) has the $\gamma$ of Nguyen
  et al.'s version of the same tube, whose $p_\infty$ is not printed, and differs from the
  $\gamma=5.5$, $6.12$, $7.15$ fits listed above.
- Nguyen et al.'s Fig. 10 labels the pressure axis in MPa with a
  maximum of 1, while the text sets the water at $10^9$ Pa; the text
  also labels the water side "$\phi_1=1$", whereas their interface
  advection test of §3.1 makes water phase 2.
- Huang & Johnsen print the air–water states without units or a
  nondimensionalization, while the water constants are in Pa and J/kg
  ($p=714$ beside $p_\infty=10^9$ Pa; §4.2). Their scheme is at most
  second order (MUSCL with minmod).
- Long et al. tune the Hertz–Knudsen coefficients to match the exact
  solution: $(1.0,0.9)$ with the adjacent-state mass flux against
  $(0.756,0.680)$ with the initial states (§4.1.1). The exact solution
  itself depends on the phase-change model.
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
- [Chamarthi (2023a)](/sources/chamarthi-2023.md) — Ex. 4.14–4.15; Appendix A, Eqs. (93)–(95): gas–gas two-fluid tube and shock–curtain on the five-equation model (arXiv v2).
- [Bezgin, Buhendwa & Adams (2023)](/sources/bezgin-2023.md) — §5.2.1, Fig. 13: sharp-interface air–helium tube (arXiv v1; gas–gas only).
- [Huang & Johnsen (2023)](/sources/huang-2023.md) — §4.1–4.2, Eqs. (48)–(49), Figs. 2–5: air–helium and air–water tubes with a phase-field term.
- [Paula et al. (2023)](/sources/paula-2023.md) — §7.4.1–7.4.2, Table 2, Figs. 13–15: weak shock through a water–air interface, $10^{12}$ Pa water–air tube.
- [Jiang et al. (2024)](/sources/jiang-2024.md) — §5.1.3, Fig. 8: air–water problem in a Lagrangian WLS particle method.
- [Long et al. (2023)](/sources/long-2023.md) — §2.2, §4.1, Eqs. (28)–(32), Figs. 4–5: liquid–vapour tubes with evaporation and condensation.
- [Zhang et al. (2024a)](/sources/zhang-2024.md) — §§4.2–4.4, Tables 3–5, Figs. 5–8: water–air tube, shock on static and moving water–air interfaces, $L_1$ convergence.
- [Wakimura et al. (2024)](/sources/wakimura-2024.md) — §§4.1–4.2, Eqs. (46)–(47), Figs. 1–3: cavitation tube and mainly-vapour shock tube with phase change.
- [Yan, Abgrall & Wu (2024)](/sources/yan-2024.md) — Ex. 4.4, 4.6, Figs. 6, 8–9: gas–gas shock–interface problem and two-phase Lax tube in the Kapila model (gas–gas only).
