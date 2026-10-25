---
type: Result
title: "Grid-point requirements of LES and DNS"
description: "How the number of grid points and time steps of DNS, wall-resolved LES and wall-modelled LES scales with Reynolds number, the explicit WMLES cost model with boundary-layer and leading-edge resolution parameters, the practical sizing rules the sources use, and why their WMLES cost exponents differ."
status: established
aliases: [grid-point estimates, resolution requirements, LES cost scaling, Chapman estimate, Choi–Moin estimate, WMLES cost]
tags: [les, wmles, dns, boundary-layer]
timestamp: 2026-10-25T13:44:00Z
---

# Grid-point requirements of LES and DNS

The cost of a scale-resolving simulation is the number of grid points times
the number of time steps, and both grow with Reynolds number at a rate set by
what must be resolved: the Kolmogorov scale for
[direct numerical simulation](/definitions/direct-numerical-simulation.md), the
near-wall streaks for wall-resolved LES (WRLES), only the eddies of the
boundary-layer thickness for [wall-modelled LES](/methods/wall-modelled-les.md).
The sources of this bundle recall the classical estimates, derive an explicit
WMLES cost model, and report what resolution sufficed in practice.

## Reynolds-number scaling

| Simulation | Grid points | Cost (points × steps) | Source |
|---|---|---|---|
| DNS, volume of side $L_d$ resolved at $2\eta$ | $(L_d/2\eta)^3=(L_d/2L)^3Re_T^{9/4}$ | — | [Domingo & Vervisch (2023)](/sources/domingo-2023.md), §2, Eqs. (1)–(2) |
| WRLES, flat plate | $Re_{L_x}^{1.86}$ | $Re^{2.7}$ | points: [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §I; cost: [Griffin et al. (2023)](/sources/griffin-2023.md), §1 — both after Yang & Griffin (2021) |
| WMLES, flat plate | $Re_{L_x}^{1.0}$ | $Re^{1.1}$ | same |
| WMLES | $\propto Re_c$ | $\propto Re_c^{4/3}$, "which accounts for the reduction in time step" | [Goc et al. (2021)](/sources/goc-2021.md), §2.2, §4, after Choi & Moin (2012) |
| WMLES on a [BL-conforming grid](/methods/boundary-layer-conforming-grid.md) | $n_\delta^{13/6}\,Re\,(Re_\Delta^{\min})^{-5/6}$ | steps $\sim\tilde t\,Re\,(Re_\Delta^{\min})^{-1}$ | [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §III.B, Eqs. (5)–(7) |

Page-local symbols: $L_d$ the domain size, $L$ the integral length,
$Re_T=k^{1/2}L/\nu$ the turbulent Reynolds number, $Re_{L_x}=L_xU_\infty/\nu$ the
plate-length Reynolds number, $n_\delta$ the points per boundary-layer
thickness, $Re_\Delta^{\min}=\Delta_{\min}U_\infty/\nu$ the minimum grid
Reynolds number, $\tilde t$ the run length in flow-through times. The
sources agree that the grid of WMLES grows linearly with Reynolds number and
that of WRLES almost quadratically, so that wall modelling is "a necessity for
flows at practically relevant Reynolds numbers" (Vadrot et al. 2023b, §I).
Their exponents for the total WMLES cost differ, because they rest on different time-step assumptions (see Qualifications).

## DNS

Domingo & Vervisch (2023, §2) take $h=2\eta$ as sufficient for the dissipative
range (after Moin & Mahesh, as they recall it) and derive the point count of
the table. For reacting flows they add the Damköhler and Karlovitz numbers
(page-local $Da$, $Ka$), with $Da\,Ka\approx Re_T^{1/2}$ (Eq. 5), so

$$N_{\mathrm{pts}}=\left(\frac{L_d}{2L}\right)^3Da\,Ka\,Re_T^{7/4}\qquad\text{(Eq. 6)}:$$

a DNS cannot have large $Re_T$, $Da$ and $Ka$ at once, and a DNS domain holds
few integral scales. Their example: a gas-turbine swirl burner with
$Re_T\sim1500$ and $L\sim5$ mm needs "more than 10 billon mesh points" to
resolve $10^3$ cm³ of shear layer; Eq. (2) with $L_d=10$ cm gives about
$1.4\times10^{10}$ *(compiler check, not in the sources)*. Near walls,
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§7.1) obtain
pipe DNS at $Re_\tau=1000$ in excellent agreement with reference data on a
uniform mesh with $\Delta x^+=\Delta y^+\approx3$ (no near-wall refinement,
immersed boundary), and suggest the recommended one-wall-unit wall-normal spacing
"may be somewhat over-demanding"; a factor 3 coarser in each direction
($\Delta x^+\approx9$, a cost reduction of $3^4=81$) still gives $u_\tau$
within 1.8 % with implicit LES (§7.2–7.4).

## Explicit WMLES cost model

Lozano-Durán et al. (2022, §III.B) count only points inside the boundary layer,
$N_{\mathrm{pts}}=\iint_Sn_\delta\Delta^{-2}\,dA$ for a grid with
$\Delta\approx\delta/n_\delta$ floored at $\Delta_{\min}$ (Eq. 5). For a flat
plate with $\delta/x=0.16\,Re_x^{-1/7}$ the count is exact (App. A, Eq. 13):
a leading-edge part (constant $\Delta_{\min}$) plus the rest, both
proportional to $n_\delta^{13/6}Re\,(Re_\Delta^{\min})^{-5/6}$, with the
leading-edge extent $L_0/L_x=(Re_\Delta^{\min}n_\delta/0.16)^{7/6}Re^{-1}$.
Fixing $Re_{L_0}=U_\infty L_0/\nu$ instead gives $n_\delta^3Re\,Re_{L_0}^{-5/7}$
(Eq. 14). Substituting $Re_\Delta^{\min}=0.16\,Re_{L_0}^{6/7}/n_\delta$ into
Eq. (13) reproduces the prefactors of Eq. (14) *(compiler check, not in the
sources)*. The authors present Eq. (6) as "the generalization of the WMLES cost
scaling from previous works", that is of Chapman, Spalart et al., Choi & Moin
and Yang & Griffin, as they recall them. With time steps limited by
$\Delta_{\min}/U_\infty$ (Eq. 7) the total cost is the product times a
machine- and code-dependent constant.

Numerically on the [NASA Juncture Flow](/benchmarks/nasa-juncture-flow.md)
geometry at $Re=5\times10^6$ (§III.B, Fig. 6): $n_\delta\approx5$ with
$Re_\Delta^{\min}\approx10^4$ needs $O(10)$ million points (hours on $O(1000)$
cores), whereas $n_\delta\approx20$ with $Re_\Delta^{\min}\approx10^3$ needs
$O(1000)$ million, "which renders WMLES unfeasible as a routine tool in
industry"; flight Reynolds numbers ($\approx5\times10^7$) multiply the count by
about ten.

## What resolution sufficed in practice

- **Integrated forces at about ten points per boundary layer.** Goc et al.
  (2021) size the [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
  grids for $\delta_{99}/\Delta\approx10$ at the main-element trailing edge
  ($Re_c=1.96\times10^6$, $Re_\tau\approx5000$) and predict $C_{L,\max}$ within
  five lift counts with 32 M cells; they argue that the estimates of Spalart
  (1997), Choi & Moin (2012) and Slotnick et al. (2014) were too pessimistic for
  integrated forces because they were not tied to particular quantities of
  interest, while Reynolds stresses and wall-pressure fluctuations need more
  resolution (§1, recalling Park & Moin 2016). Part of the requirement is
  inviscid: the leading-edge acceleration at high angle of attack (§1, §3.2).
- **Wall pressure at fewer.** Lozano-Durán et al. (2022, §V.E) find $C_p$
  errors below 5 % with 0–1 points per $\delta$.
- **Mean velocity and separation need more.** The mean-velocity error
  decreases linearly with $\Delta/\delta$ in developed layers and more slowly in
  corners and separation (Lozano-Durán et al. 2022, §V.B); in the Gaussian bump
  separation appears only on the finest of three grids, with the first cell at
  $y^+\sim30$ ([Agrawal et al. 2022](/sources/agrawal-2022.md), §VIII.B).
- **Hybrid methods.** [Haering et al. (2022)](/sources/haering-2022.md)
  (§V.A.1) recall that typical LES needs an unresolved fraction of turbulent
  kinetic energy of at most about 0.1 (after Jiménez & Moser); their
  [active model split](/methods/active-model-split.md) runs channel flow at
  $Re_\tau\approx5200$ with fractions up to 0.4 at the centre and the
  [periodic hill](/benchmarks/periodic-hill.md) on 0.2–0.9 M cells, 14–62
  times fewer than the 13 M-cell wall-resolved LES reference (§V.B).

## Measured costs

Goc et al. (2021, §4, Tables 1–2) report, for 30 flow passes of the JAXA model
at $\alpha=18.58^\circ$ in [CharLES](/software/charles.md): 32 M cells, 1.4
thousand core-hours per pass, 21 h on 2000 CPU cores or 48 min on 96 V100
GPUs; 157 M cells, 12.3 thousand core-hours per pass, 7.5 days on CPUs or 7 h
on GPUs. A medium-grid LES (about $40\times10^3$ core-hours) costs about the
same as a steady RANS run of the workshop (about $60\times10^3$); the fine grid
(about $360\times10^3$) six times the RANS cost. Lozano-Durán et al. (2022, §V.A) report 13–398 thousand
core-hours for 6–174 M cells on the Juncture Flow. Uniform refinement by two
halves the explicit time step (Goc et al. 2021, §4).

## Qualifications

- **WMLES cost exponent: $Re_c^{4/3}$ or $Re^{1.1}$** (reclassified from
  Contradictions in the chunk-1 deep lint, 2026-10-25). The two exponents are
  not incompatible statements about one quantity under one set of
  assumptions. Goc et al. (2021, §4) extrapolate their own JAXA runs to
  flight Reynolds numbers: assuming, after Choi & Moin (2012), a grid-point
  count $\propto Re_c$, "the overall cost would then scale by $Re_c^{4/3}$,
  which accounts for the reduction in time step". Their grids are isotropic
  and uniformly refined, and refinement by two halves the time step (§4); with
  $N\propto Re_c$ isotropic cells on a fixed geometry the cell size falls as
  $Re_c^{-1/3}$ and the number of steps grows as $Re_c^{1/3}$, which gives the
  4/3 *(compiler check, not in the sources)*. Griffin et al. (2023, §1) quote
  $Re^{1.1}$ for the cost (points times time steps) of WMLES of a turbulent
  boundary layer, and Vadrot et al. (2023b, §I) $Re_{L_x}^{1.0}$ for the
  points of a flat-plate WMLES, both from Yang & Griffin (2021) and without
  its time-step assumptions; together they imply a step count growing about as
  $Re^{0.1}$ *(compiler check, not in the sources)*. Goc et al. themselves
  cite Yang & Griffin (2021) (§2.2) for a "significant reduction in the time
  step size" beyond their practice, "in particular for compressible flow
  solvers deploying explicit time-marching schemes that are limited by the
  acoustic CFL condition". Lozano-Durán et al. (2022, Eq. 7) show that the
  step count depends on the grid strategy: under a convective limit on the
  smallest cell it is $\tilde t\,Re\,(Re_\Delta^{\min})^{-1}$, set by how the
  leading-edge resolution is scaled with Reynolds number. The exponents also
  refer to different configurations (a high-lift aircraft at chord Reynolds
  number; a flat-plate boundary layer at plate-length Reynolds number).
  Ingesting Yang & Griffin (2021) would show which time-step constraint yields
  $Re^{1.1}$.
- Goc et al. (2021, §4) state that, at the solver's strong-scaling limit
  (about 2000 cells per core), the 157 M-cell case would run on about
  $80\times10^3$ cores and 160 GPUs, with a wall-clock time under 4 h. From
  their Table 1, perfect scaling of $12.3\times10^3$ core-hours per pass over 30
  passes on $78.5\times10^3$ cores ($157\times10^6/2000$) gives about 4.7 h, and
  of 7 h on 96 GPUs to 157 GPUs about 4.3 h: both exceed 4 h even at perfect
  scaling, whereas the stated parallel efficiency is ">80 %"
  *(compiler check, not in the sources)*. The same table gives 7.5 days where 12.3 thousand core-hours
  times 30 on 2000 cores gives 7.7 days *(compiler check, not in the sources)*.
- Lozano-Durán et al. (2022, arXiv v1) print the growth law as
  $\delta\sim x\,Re_x^{-m}$ with "$m\approx-1/7$" (§III.B), which with the minus
  sign gives growth as $Re_x^{+1/7}$, against their own $\delta/x=0.16\,Re_x^{-1/7}$
  (App. A); App. A also writes $(Re_\Delta^{\min})^{5/6}$ in words where Eqs.
  (6) and (13) have the exponent $-5/6$.
- Goc et al. cite "Choi and Moin (1994)" for the $N\propto Re_c$ scaling in one
  sentence of §4 and Choi & Moin (2012) in another; their reference list
  gives the 1994 work as "Effects of the computational time step on numerical
  solutions of turbulent flow".

# Citations

- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §2, Eqs. (1)–(6).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.1–7.4, Figs. 24–28.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1; §2.2; §3.2; §4, Tables 1–2.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §III.B, Eqs. (5)–(7), Fig. 6; §V.A–V.E; App. A, Eqs. (13)–(14).
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VIII.B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V.A.1; §V.B.
