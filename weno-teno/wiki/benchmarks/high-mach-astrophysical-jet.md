---
type: Benchmark
title: "High-Mach astrophysical jets"
description: "Mach 80 and Mach 2000 gas jets injected into a light ambient medium, and their relativistic, MHD and gas–liquid relatives; near-vacuum, extreme-Mach-number robustness tests that most high-order schemes pass only with a positivity- or invariant-domain-preserving limiter."
status: established
aliases: [Mach 2000 jet, Mach 80 jet, astrophysical jet, high Mach number jet]
tags: [benchmark, positivity, bound-preserving, relativistic, mhd]
timestamp: 2026-10-23T23:55:00Z
---

# High-Mach astrophysical jets

A dense, fast gas jet is injected through a narrow slot into a lighter
ambient gas at the same pressure. With injection speed 800 the jet Mach
number is about 2000, with speed 30 it is about 80; the bow shock, the
contact surface and the cocoon then sit next to regions of nearly zero
density and pressure, and in the Mach 2000 jet the kinetic energy per unit volume of the
injected gas exceeds its internal energy by a factor of about
$2.6\times10^6$ *(compiler check, not in the sources)*. Pressure, a small difference of large
energies, can then leave $G=\{\rho>0,\ p>0\}$, and the sources use the
test as a demonstration of
[bound preservation](/properties/bound-preservation.md); the amount of
small-scale structure in the shear layer is a secondary, visual
measure of resolution.

## The Euler jets

Common data ($\gamma=5/3$), printed by [Fu (2021)](/sources/fu-2021.md)
§5.7.3 and [Takagi et al. (2022)](/sources/takagi-2022.md) §4.9, both
citing Zhang & Shu's positivity-preserving DG paper for it (their refs.
[76] and [74]; Rueda-Ramírez et al. attribute the Mach 2000 jet to Ha et
al., Wang & Don take the setup from Gao et al.), in $(\rho,v_1,v_2,p)$:

- **Mach 80:** domain $[0,2]\times[-0.5,0.5]$, ambient $(0.5,0,0,0.4127)$,
  jet inflow $(5,30,0,0.4127)$ through $|y|\le0.05$ on the left boundary
  (Takagi et al.: $(5,0,0,0.4127)$ on the rest of that boundary).
- **Mach 2000:** domain $[0,1]\times[-0.25,0.25]$, the same ambient state,
  jet inflow $(5,800,0,0.4127)$; outflow on the other boundaries.

The jet sound speed is $c=\sqrt{\gamma p/\rho}=\sqrt{(5/3)(0.4127)/5}=0.371$,
so the jet Mach numbers are $30/0.371=80.9$ and $800/0.371=2156.9$
*(compiler check, not in the sources)*.
[Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md)
§5.2.3 print the same value: Mach 2156.91 with respect to the jet sound
speed and 682.08 with respect to the ambient one.

| Source | Scheme | Grid | Final time | Positivity treatment |
|---|---|---|---|---|
| [Fu (2021)](/sources/fu-2021.md) §5.7.3 | [TENO-AA](/methods/adaptive-teno.md), LLF | Mach 80: $448\times224$; Mach 2000: $800\times400$ | not printed | positivity-preserving flux limiter |
| [Takagi et al. (2022)](/sources/takagi-2022.md) §4.9 | [TENO-THINC](/methods/teno-thinc.md), TENO5, WENO5-Z | $800\times400$, CFL 0.35 | not stated | positivity-preserving flux limiter |
| [Fu (2023)](/sources/fu-2023.md) Fig. 5 | TENO10 (review, reproduced) | $448\times224$, $800\times400$ | — | positivity-preserving limiter |
| [Wang & Don (2022)](/sources/wang-2022-b.md) §3.2.4 | [affine-invariant WENO-Z/D](/methods/affine-invariant-weno.md) | setup from Gao et al. (not reproduced) | — | PP limiter needed |
| [Rueda-Ramírez et al. (2022)](/sources/ruedaramirez-2022.md) §5.2.3 | [DGSEM](/methods/dgsem.md), $N=3$, [subcell IDP limiting](/methods/subcell-finite-volume-limiting.md) | $[-0.5,0.5]^2$, $256^2$ elements | $10^{-3}$ | bar-state bounds |
| [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) §3.5 | LGL-DGSEM, $N=3$, Ranocha volume flux; monolithic convex limiting (MCL) against FCT/IDP subcell limiting, CFL 0.9, 0.45, 0.225, 0.09 | $[-0.5,0.5]^2$, $256^2$ elements, periodic top and bottom | $10^{-3}$ | limited bar states (MCL), local bounds (FCT/IDP) |
| [Liang, Xiao, Shyy & Fu (2022)](/sources/liang-2022.md) §4.11 | fifth-order TENO with THINC-type discontinuity reconstruction, TENO5, TENO5-THINC, WENO5-Z | both jets $800\times400$, CFL 0.35 | not printed | positivity-preserving flux limiter |
| [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) Example 5.7 | finite-difference WENO-JS5, WENO-JS7, WENO-ZQ5, Euler and Navier–Stokes ($\mathrm{Re}=1000$) | $\Delta x=\Delta y=1/640$ | $0.001$ | [positivity-preserving Navier–Stokes flux](/methods/positivity-preserving-navier-stokes-flux.md) and scaling limiter |
| [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) Ex. 3.11 | finite-difference [HWENO](/methods/hermite-weno.md) (HWENO-R, HWENO-L), WENO-ZQ | $640\times320$ | $0.001$ | parametrized PP flux limiter |
| [Li, Li, Don & Wang (2023)](/sources/li-2023.md) §3.6 | scale-invariant multi-resolution [A-WENO](/methods/alternative-weno.md) (MR-AWENO-Si), MR-AWENO | $800\times400$ | $0.001$ | [PP flux limiter](/methods/positivity-preserving-flux-limiter.md) |
| [Lin & Chan (2024)](/sources/lin-2024.md) §4.4 | LGL-[DGSEM](/methods/dgsem.md), $N=3$, [subcell limiting](/methods/subcell-finite-volume-limiting.md) towards a low-order entropy-stable scheme, with factors from a linear program enforcing the cell entropy inequality; SSPRK(3,3) | $[-0.5,0.5]^2$, $150^2$ elements, inflow at $x=-0.5$ | $0.001$ | relaxed positivity of $\rho$ and $\rho e$ ($\ge\tfrac12$ of the low-order value) and TVD-like density bounds, as [convex limiting](/methods/convex-limiting.md) constraints |
| [Peng, Sun & Wu (2024)](/sources/peng-2024.md) Ex. 5.18 | [OEDG](/methods/oedg.md), third order | $320\times160$ | $0.001$ | none mentioned |
| [Yu & Hesthaven (2022)](/sources/yu-2022.md) §5.4.6 | nodal DG on triangles, $P^2$–$P^4$, ANN-predicted [artificial viscosity](/methods/artificial-viscosity.md) (decay-rate threshold $\mathfrak a_0=2.5$, page-local; min-rule) | $h=1/320$, mesh symmetric about $y=0$ | $0.001$ | none; first layer of elements next to the inlet initialized with the jet state |

Yu & Hesthaven print the Mach 2000 data and domain above but not
$\gamma$. Liang et al. print both jets with the common data (Mach 80
with $(5,0,0,0.4127)$ on the rest of the left boundary) and no final
times. Fan, Zhao, Xiong & Qiu and Li et al. print the Mach 2000 data
above. Fan, Zhang & Qiu (2022) print the jet inflow as
$(\rho,v_1,v_2,p)=(0.5,800,0,0.4127)$, the ambient density, not 5
(checked on the PDF page); with that density the jet sound speed is
$1.173$ and the jet Mach number $800/1.173=682$, the value
Rueda-Ramírez et al. give with respect to the ambient sound speed
*(compiler check, not in the sources)*. Fan, Zhang & Qiu still call it
the Mach 2000 jet.
Rueda-Ramírez et al. run the Mach 2000 jet on the square
$[-0.5,0.5]^2$ with inflow at $x=-0.5$, periodic top and bottom and
characteristic inflow/outflow left and right, a different box from the
$[0,1]\times[-0.25,0.25]$ of the other sources.

## Findings across sources

**A positivity limiter is needed by most schemes.** Fu (2021) computes
both jets with LLF and the positivity-preserving flux limiter; Takagi
et al. use the same kind of limiter for all three schemes they compare;
Fu (2023) presents the TENO10 jet as an example of near-vacuum robustness
"with the PP limiter". Wang & Don state that their affine-invariant
schemes are not positivity preserving in general and need a PP limiter
on the Mach 2000 jet; at the final time it is active only around the jet
front and the two inlet corners (§3.2.4, Fig. 8). Rueda-Ramírez et al.
make DGSEM robust by blending with a low-order finite-volume scheme up
to invariant-domain-preserving bar-state bounds, element-wise or
subcell-wise (Figs. 8–9).

Liang et al. report all four of their schemes stable with the
positivity-preserving flux limiter. Fan, Zhang & Qiu (2022) find that
negative density and pressure never appear; their limiter acts on
0.178 %, 0.230 % and 0.416 % of the cells per step for WENO-JS5, JS7 and
ZQ5 at $\mathrm{Re}=\infty$ (0.103 %, 0.070 %, 0.225 % at
$\mathrm{Re}=1000$), and "WENO schemes without any positivity treatment
will simply blow up for this test", which is stated, not shown
(Example 5.7, Fig. 5.6). Fan, Zhao, Xiong & Qiu need the limiter for
HWENO-R and WENO-ZQ, although HWENO-R runs their one-dimensional
extreme problems without it; it acts on 0.0146 % of the cells
(Remark 3.2). Li et al. find that only the pressure part of the limiter
is active, at the jet front, and the density stays positive (§3.6).

**Time-step dependence of the limited scheme.** [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md)
(§3.5, Table 5, Figs. 8–9; arXiv v1) use the Mach 2000 jet, which
they attribute to Ha et al. and run with the inflow through
$y\in[-0.05,0.05]$ at $x=-0.5$, to compare two ways of limiting DGSEM
towards its subcell finite-volume scheme
([convex limiting](/methods/convex-limiting.md),
[subcell finite-volume limiting](/methods/subcell-finite-volume-limiting.md)).
Their MCL limits the anti-diffusive fluxes at the semi-discrete level,
so the limited spatial operator does not depend on $\Delta t$; FCT/IDP
limiting corrects each stage and does. The number of steps to
$t=10^{-3}$ is 10284, 20568, 41138 and 102844 for MCL at CFL 0.9, 0.45,
0.225 and 0.09, exactly inverse to the CFL number (the product is 9256
throughout *(compiler check, not in the sources)*), against 10758,
25608, 71577 and 241974 for FCT/IDP. In FCT/IDP a smaller CFL number
reduces the dissipation: $\rho_{\min}$ falls from $4.43\times10^{-3}$ to
$7.11\times10^{-4}$ and $p_{\max}$ rises from 172640 to 228165, which raises
the sound speed and cuts the step further, a "feedback effect"; its
vortical structures change markedly with the CFL number, those of MCL
only weakly. They conclude that "time convergence can be expected for
MCL but not for FCT schemes in problems that need stabilization". Of
their two pressure-positivity fixes, the "cautious" one suppresses the
vortical structures of the shear layer, while the "sharp" one "allows
the development of turbulence" (Fig. 9).

**Entropy bounds, dissipation and carbuncles.** Lin & Chan run the
Mach 2000 jet, attributed to Ha et al., on the square of Rueda-Ramírez
et al., ambient $(0.5,0,0,0.4127)$ and inflow $(5,800,0,0.4127)$ through
$y\in[-0.05,0.05]$ at $x=-0.5$ (§4.4). With TVD-like density bounds,
relaxed internal-energy positivity and the cell entropy inequality the
run is robust (Fig. 6). In a shock-capturing variant that blends a
fraction $\beta_{\mathrm e}\epsilon_K$ of the low-order entropy dissipation into the
entropy bound ($\epsilon_K$ a modal smoothness factor, $\beta_{\mathrm e}\in[0,1]$
user-chosen; both page-local here), finer features appear as $\beta_{\mathrm e}$
decreases through $1$, $0.1$, $0.01$, $0$, but carbuncles appear at
$\beta_{\mathrm e}=0.01$ and $0$, and also with the local minimum entropy principle
in place of the cell entropy inequality (Fig. 7, Fig. A.8c). The authors
conclude that "the carbuncle effect is not due only to a loss of entropy
stability, but rather a lack of sufficient dissipation near shocks",
and that the solution is highly sensitive to $\beta_{\mathrm e}$. The element-wise
Zhang–Shu-limited entropy-stable DG shows no carbuncle, which they
partly explain by its larger dissipation (Fig. A.8b); see
[carbuncle phenomenon](/definitions/carbuncle-phenomenon.md) and
[entropy stability](/properties/entropy-stability.md).

**An exception without a stated limiter.** Peng, Sun & Wu compute the
Mach 2000 jet with OEDG on $320\times160$ to $t=0.001$ and report no
nonphysical oscillations; the paper neither claims bound preservation
nor mentions a positivity limiter, and says only that the results agree
with earlier ones (Ex. 5.18, Fig. 14). Whether OEDG alone keeps $\rho$
and $p$ positive here is not established by the source.

**Cost.** Fan, Zhao, Xiong & Qiu's HWENO-R takes 2292.73 s on the jet,
1.577 times WENO-ZQ, in Fortran 95 on an Intel Xeon Gold 6130 (Ex. 3.11).

**Artificial viscosity alone, and its order dependence.** Yu &
Hesthaven run the jet with artificial viscosity and no positivity
limiter: $P^3$ and $P^4$ are stable, $P^2$ goes unstable from
insufficient dissipation, which they attribute to the scarce smoothness
information carried by low-degree polynomials (§5.4.6, Figs. 24–25;
§6). The run needs the tuned settings $\mathfrak a_0=2.5$ (default 2) and the min-rule
and a start-up layer of jet-state elements.

**Resolution.** Liang et al. claim richer small-scale structures for
their scheme than for the three comparators on both jets (Figs. 24–25).
Li et al. find MR-AWENO noisier than MR-AWENO-Si along the rear and
above the jet tail (Fig. 8). Takagi et al. rank TENO-THINC, then TENO5, then WENO5-Z
by small-scale structure and claim TENO-THINC beats earlier WENO5-JS and
DG results (Fig. 20). Fu (2021) claims "much richer small-scale
structures" than fifth- and seventh-order WENO and a DG scheme (Figs.
11–14). Rueda-Ramírez et al. find that the low-order partner matters:
going from first-order FV with LLF, to first-order FV with HLLE, to
second-order FV with HLLE sharpens shocks and develops finer scales,
and subcell-wise blending beats element-wise blending. The second-order
and HLLE partners are not guaranteed to satisfy the bar-state bounds;
the authors keep the bounds and the blending returns the solution
closest to them (§5.2.3).

## Relativistic, MHD and gas–liquid variants

- **Mach 800 dense jet without field.** [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md)
  §5.1.6 (arXiv v3) take the setup of the Mach 800 MHD jet below,
  "without magnetic field": half domain $[0,0.5]\times[0,1.5]$ with a
  slip symmetry line on the $y$-axis, ambient $\rho=0.1\gamma$, $v=0$,
  $p=1$, inlet $x\le0.05$ on $y=0$ with $(\rho,v_1,v_2,p)=(\gamma,0,800,1)$,
  free boundaries elsewhere, $t=0.002$, flux reconstruction $\mathbb P_3$
  on $200\times600$ and $800\times2400$ elements with
  [entropy filtering](/methods/entropy-filtering.md). The run is robust;
  the filter acts mainly at the leading shock, and on the fine mesh less
  at the cocoon–jet interface. They claim "significantly better
  resolution" than Wu & Shu's earlier DG with the linear
  [Zhang–Shu limiter](/methods/zhang-shu-scaling-limiter.md), conceding
  that the magnetic field of that run can stabilize the flow (Fig. 6);
  the comparison is with a different problem.
- **Axisymmetric relativistic jet.** [Cui, Ding & Wu (2024)](/sources/cui-2024.md)
  Example 5: special-relativistic hydrodynamics in cylindrical $(r,z)$
  coordinates with a geometric source, $\gamma=5/3$, domain
  $[0,15]\times[0,45]$, $240\times720$ cells; ambient
  $(\rho,v_1,v_2,p)=(0.01,0,0,0.000170304823218172071)$, jet
  $(0.01,0,0.99,\text{same }p)$ through $r\le1$ at $z=0$; reflective
  symmetry axis, outflow elsewhere; classical Mach 6, relativistic Mach
  about 41.95; $t=100$. The DG code breaks down without the
  bound-preserving limiter; with the
  [optimal cell-average decomposition](/methods/optimal-cell-average-decomposition.md)
  the $\mathbb P^4$ run takes 297.26 h against 414.19 h for the classic
  decomposition (Table 10). [Chen & Wu (2022)](/sources/chen-2022-b.md)
  Ex. 4.12 (arXiv v1) run the same jet with their third-order
  finite-volume WENO on triangles ($h=1/25$): beam $\rho_{\mathrm b}=0.01$,
  $v_z=0.99$ through $r\le1$, ambient $(\rho,v_z,v_r,p)=(1,0,0,1.70305\times10^{-4})$,
  pressure matched; classical Mach 6 and relativistic Mach about 41.95,
  output at $t=60$, 80 and 100. The physical-constraint-preserving
  limiter is needed (the run fails within a few steps without it) and
  no carbuncle appears (Fig. 18). With $\gamma=5/3$ the beam sound
  speed is $0.165=0.99/6$ and the relativistic Mach number
  $Wv/(W_sc_s)=41.95$, $W_s$ the Lorentz factor of the sound speed
  *(compiler check, not in the sources)*. The two papers print
  different ambient densities, $1$ (Chen & Wu) against $0.01$ (Cui et
  al.); the Mach numbers depend only on the beam state.
  [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) Example 5.9 (arXiv v1)
  run the jet with Chen & Wu's ambient density, ambient
  $\rho=1$, $v=0$, $p=1.70303\times10^{-4}$, and beam $v_{\mathrm b}=0.99$,
  $\rho_{\mathrm b}=0.01$, $p_{\mathrm b}=1.70303\times10^{-4}$ through
  $r\le1$ on the low-$z$ boundary, on $[0,15]\times[0,45]$ with
  $375\times1125$ cells, reflective at $r=0$ and outflow elsewhere,
  output at $t=60$, 80, 100, $\gamma=5/3$. Their physical-constraint-preserving
  finite-volume [Hermite WENO](/methods/hermite-weno.md) scheme with
  provably convergent Newton–Raphson recovery of the pressure (see
  [relativistic hydrodynamics](/definitions/relativistic-hydrodynamics.md))
  captures the bow shock and Kelvin–Helmholtz instabilities of the beam,
  and the limiter is necessary. Their tests run at "CFL number 0.6",
  whose definition is not printed, while their positivity theorem requires
  $\Delta t\le\Delta x/(12a)$.
- **Relativistic MHD jets at Mach 50.** [Ding & Wu (2024)](/sources/ding-2024-b.md)
  Example 5.9 run the relativistic MHD jet that Wu & Shu proposed with
  the ideal equation of state (Numer. Math. 148, their ref. [12]), with the ideal and the RC equations of
  state: domain $[-12,12]\times[0,25]$, half domain $[0,12]\times[0,25]$
  on $240\times500$ cells with a reflective axis $x=0$; ambient $\rho=1$,
  $v=0$, $B=(0,\sqrt{2000p_{\mathrm a}},0)$, $p=p_{\mathrm a}=2.35362407217\times10^{-5}$;
  inflow $(\rho,v,B,p)=(0.1,\ (0,0.99,0),\ (0,\sqrt{2000p_{\mathrm a}},0),\ p_{\mathrm a})$
  through $x\in[0,0.5]$ at $y=0$ (page-local $p_{\mathrm a}$); jet Mach
  number 50, Lorentz factor about $7.09$, relativistic Mach number about
  $354.37$, plasma beta $0.001$; output at $t=10$, 20, 30 (Figs. 12–14).
  Their $\mathbb P^2$ bound-preserving, locally divergence-free central
  DG code "would quickly break down" without any one of the
  bound-preserving limiter, the discretized symmetrization source, or the
  locally divergence-free spaces (stated, not shown), the same three
  ingredients that Wu & Shu (2023) found necessary for the two-component
  jet below; see
  [divergence-free magnetic field](/properties/divergence-free-magnetic-field.md),
  [bound preservation](/properties/bound-preservation.md). The ideal-EOS
  results are comparable to Wu & Shu's earlier computation. With the
  printed data $2p/\lvert B\rvert^2=2p_{\mathrm a}/(2000p_{\mathrm a})=10^{-3}$
  *(compiler check, not in the sources)*.
- **Two-component MHD jet.** [Wu & Shu (2023)](/sources/wu-2023-b.md)
  Ex. 7.2: two-component ideal MHD, domain $[-0.5,0.5]\times[0,1.5]$,
  ambient $(\rho,p)=(0.14,1)$, inflow $(\rho,p)=(1.4,1)$ with
  $v=(0,800,0)$ through $|x|<0.05$ at $y=0$, magnetic field
  $B=(0,\sqrt{4000},0)$; $200\times600$ cells on the half domain; output
  at $t=0.001$, $0.0015$, $0.002$. The run fails without any one of the
  [scaling limiter](/methods/zhang-shu-scaling-limiter.md), the locally
  [divergence-free](/properties/divergence-free-magnetic-field.md) basis
  or the discretized Godunov-symmetrization source term, which the
  paper's [geometric quasilinearization](/methods/geometric-quasilinearization.md)
  analysis shows is needed for provable bound preservation, even with a
  WENO limiter; this failure is stated in text, without a
  figure.
- **Mach 800 dense MHD jet.** [Liu et al. (2021)](/sources/liu-2021.md)
  §4.5, after Wu & Shu's earlier papers: ideal MHD, $\gamma=1.4$, ambient
  $(\rho,v,B,p)=(0.1\gamma,\ 0,\ (0,\sqrt{20000},0),\ 1)$, jet
  $(\rho,v,p)=(\gamma,\ (0,800,0),\ 1)$ through $-0.05<x<0.05$ at $y=0$,
  outflow elsewhere, $200\times300$ cells, snapshots at $t=0.001$,
  $0.0015$, $0.002$; the plasma beta, page-local
  $\beta_{\mathrm p}=2p/|B|^2$, is $10^{-4}$. The jet sound speed is
  $\sqrt{1.4\cdot1/1.4}=1$, so the jet Mach number is 800 *(compiler
  check, not in the sources)*. Densities and pressures of their
  locally divergence-free [WLS-ENO](/methods/wls-eno.md) scheme stay
  positive at second and third order, but the third-order run produces
  a negative pressure at $t=4.45\times10^{-4}$ when the truncated SVD of
  its least-squares fits keeps singular values down to
  $10^{-10}\sigma_1$, and succeeds with the threshold $10^{-6}\sigma_1$
  ($\sigma_1$ the largest singular value, page-local); the authors
  attribute the failure to ill-conditioning (Figs. 14–17). The
  densities $0.14$ and $1.4$ and the injection speed equal those of the
  two-component jet of Wu & Shu (2023) above, whose field
  $\sqrt{4000}$ gives $|B|^2$ five times smaller, i.e.
  $\beta_{\mathrm p}=5\times10^{-4}$ *(compiler check, not in the
  sources)*.
- **Mach 100 water jet.** [Wong et al. (2021)](/sources/wong-2021.md)
  §6.7, a multiphase version of the Mach 2000 jet in the
  [five-equation model](/definitions/five-equation-model.md) with
  [stiffened-gas](/definitions/stiffened-gas-equation-of-state.md) water
  ($\gamma=6.12$, stiffening pressure $3.43\times10^8$ Pa) and air:
  domain $[0,L]\times[-0.25L,0.25L]$, $L=1$ m; ambient air with partial
  density 1 kg m$^{-3}$, $p=10^5$ Pa and water volume fraction
  $10^{-8}$; water injected through $|y|\le0.05L$ with partial density
  1000 kg m$^{-3}$, $v_1=1.5\times10^5$ m/s, $p=10^5$ Pa;
  $1024\times512$ mesh, output at 1, 2, 4 and 6 µs. The water sound
  speed $\sqrt{6.12\,(10^5+3.43\times10^8)/1000}\approx1449$ m/s makes
  the injection Mach number about 104 with respect to the water
  *(compiler check, not in the sources)*. Neither their
  positivity-preserving [WCNS](/methods/weighted-compact-nonlinear-scheme.md)
  nor first-order HLLC fails; HLLC smears the interface at the jet
  front and shows artifacts at the bow shock (Figs. 17–19).

## Qualifications

- Fu (2021), Takagi et al. and Liang et al. do not print the final
  times of the jets; the sources that do (Rueda-Ramírez et al., Peng et
  al., Fan et al. 2022 and 2023, Li et al. 2023) use $t=10^{-3}$ for
  Mach 2000.
- Fan, Zhang & Qiu (2022)'s printed jet density 0.5 makes their jet a
  Mach 682 jet as defined on this page; whether the printed value or
  the name is the slip cannot be told from the paper.
- The ambient pressure of the axisymmetric relativistic jet is printed
  as $1.70303\times10^{-4}$ (Cai et al.), $1.70305\times10^{-4}$ (Chen &
  Wu) and $1.70304823218172071\times10^{-4}$ (Cui et al.); the
  differences lie in the sixth significant digit.
- Rueda-Ramírez et al. (2024) write that the number of time steps
  "depends linearly on the CFL number" for MCL; their Table 5 shows it
  inversely proportional, as their next paragraph's "not inversely
  proportional" for FCT/IDP implies. Their evidence for the time
  dependence of FCT/IDP limiting is this one test.
- Resolution claims are visual comparisons, partly against figures
  from other papers.
- Dzanic & Witherden compute a half domain $[0,0.5]\times[0,1.5]$
  with a stated symmetry boundary, the configuration Liu et al.'s
  printed domain also suggests.
- Liu et al. print the domain of the MHD jet as $[0,0.5]\times[0,1.5]$,
  while the nozzle $-0.05<x<0.05$ lies at its edge; either the domain
  is misprinted or a half domain with an unstated symmetry boundary is
  used. Wu & Shu (2023) use $[-0.5,0.5]\times[0,1.5]$ with
  $200\times600$ cells on the half domain. Liu et al. give no CFL
  number.

# Citations

- [Fu (2021)](/sources/fu-2021.md) — §5.7.3, Figs. 11–14 (arXiv v1).
- [Takagi et al. (2022)](/sources/takagi-2022.md) — §4.9, Fig. 20.
- [Fu (2023)](/sources/fu-2023.md) — §3.1, Fig. 5 (reproduced).
- [Wang & Don (2022)](/sources/wang-2022-b.md) — §3.2.4, Fig. 8.
- [Rueda-Ramírez, Pazner & Gassner (2022)](/sources/ruedaramirez-2022.md) — §5.2.3, Figs. 8–9 (arXiv v2).
- [Peng, Sun & Wu (2024)](/sources/peng-2024.md) — Ex. 5.18, Fig. 14 (arXiv v1).
- [Liang, Xiao, Shyy & Fu (2022)](/sources/liang-2022.md) — §4.11, Figs. 24–25.
- [Fan, Zhang & Qiu (2022)](/sources/fan-2022.md) — §5, Example 5.7, Fig. 5.6.
- [Fan, Zhao, Xiong & Qiu (2023)](/sources/fan-2023.md) — Ex. 3.11, Remark 3.2.
- [Li, Li, Don & Wang (2023)](/sources/li-2023.md) — §3.6, Fig. 8.
- [Cui, Ding & Wu (2024)](/sources/cui-2024.md) — Example 5, Table 10 (arXiv v1).
- [Wu & Shu (2023)](/sources/wu-2023-b.md) — Ex. 7.2, Fig. 6 (arXiv v1).
- [Liu et al. (2021)](/sources/liu-2021.md) — §4.5, Figs. 14–17.
- [Wong et al. (2021)](/sources/wong-2021.md) — §6.7, Tables 10–11, Figs. 17–19 (arXiv v1).
- [Yu & Hesthaven (2022)](/sources/yu-2022.md) — §5.4.6, Figs. 24–25; §6.
- [Dzanic & Witherden (2022)](/sources/dzanic-2022-b.md) — §5.1.6, Fig. 6 (arXiv v3).
- [Chen & Wu (2022)](/sources/chen-2022-b.md) — Ex. 4.12, Fig. 18 (arXiv v1).
- [Rueda-Ramírez et al. (2024)](/sources/ruedaramirez-2024.md) — §2.2.4, §3.5, Table 5, Figs. 8–9; §4 (arXiv v1).
- [Cai, Qiu & Wu (2024)](/sources/cai-2024.md) — Example 5.9; Theorems 3.1, 4.1 (arXiv v1).
- [Lin & Chan (2024)](/sources/lin-2024.md) — §3.3, §4.4, Eqs. (49), (62), (67), Figs. 6–7, A.8.
- [Ding & Wu (2024)](/sources/ding-2024-b.md) — Example 5.9, Figs. 12–14.
