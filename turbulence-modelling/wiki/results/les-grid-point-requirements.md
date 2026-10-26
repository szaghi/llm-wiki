---
type: Result
title: "Grid-point requirements of LES and DNS"
description: "How the grid-point and time-step counts of DNS, wall-resolved and wall-modelled LES scale with Reynolds number, the explicit WMLES cost model, wall-unit and per-thickness resolution criteria and evidence that meeting them is not sufficient, the resolutions used in practice and found by adaptive grids, measured costs, and why WMLES cost exponents differ."
status: established
aliases: [grid-point estimates, resolution requirements, LES cost scaling, Chapman estimate, Choi–Moin estimate, WMLES cost]
tags: [les, wmles, dns, boundary-layer]
timestamp: 2026-10-26T10:26:00Z
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
[Bae & Koumoutsakos (2022)](/sources/bae-2022.md) (Introduction) and
[Gillyns et al. (2022)](/sources/gillyns-2022.md) (§1) quote the grid count
as $Re^{13/7}$ for WRLES and $Re$ for WMLES ("at most" $O(Re)$ for Bae &
Koumoutsakos; Gillyns et al. cite Choi & Moin 2012 and Yang & Griffin 2021),
without stating the Reynolds number used; $13/7\approx1.857$ agrees with the
1.86 of the table *(compiler check, not in the sources)*.
Their exponents for the total WMLES cost differ, because they rest on different time-step assumptions (see Qualifications).
[Morsbach et al. (2024)](/sources/morsbach-2024.md) (§1) quote, after Choi &
Moin (2012), a cost of roughly $Re^{3.5}$ for DNS and $Re^{2.5}$ for
wall-resolved LES. [Delassaux et al. (2023)](/sources/delassaux-2023.md)
(§4.1) recall Spalart's forecast that wall-resolved LES and DNS of a
full-scale high-Reynolds-number geometry would become available in 2050 and
2080 respectively.

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

For a bluff body [Cai et al. (2022)](/sources/cai-2022.md) (§III, Tables
I–II) estimate the scales of the Ahmed body flow at $Re_H=7.68\times10^5$
($H$ the body height, $L$ its length) from correlations they cite:
$\lambda_H/H\approx5.5Re_H^{-1/2}=6.3\times10^{-3}$ (called the Taylor scale),
$\eta_H/H\approx1.2Re_H^{-3/4}=4.6\times10^{-5}$, boundary-layer thickness at
the rear $\delta/L\approx0.37Re_L^{-1/5}$ ($\delta/H=6.9\times10^{-2}$) and
viscous length $\delta_\nu/L\approx5.9Re_L^{-0.9}$ ($\delta_\nu/H=3.4\times10^{-5}$);
"resolving down to the Kolmogorov scale or even the viscous sublayer is not
feasible" on their octree grids, whose finest cells are
$\Delta x_{\min}/H=9.0\times10^{-3}$ (13.6 M cells) and $4.5\times10^{-3}$
(40.3 M cells), 1.4 and 0.7 times $\lambda_H$. The finest cell is thus about
265 and 132 viscous lengths, and about 8 and 15 cells span the rear boundary
layer *(compiler check, not in the sources)*; the authors do not report the
near-wall resolution in wall units.

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

## Wall-unit criteria and their limits

[Lewis et al. (2023)](/sources/lewis-2023.md) (§3.3, Table 5) collect, from
Piomelli (2014) and Wagner et al. (2007) as they cite them, cell sizes in wall
units ($\Delta x^+$ streamwise, $\Delta z^+$ spanwise, $\Delta y^+$ wall-normal; the source's $s^+$, $r^+$, $n^+$):

| | $\Delta x^+$ | $\Delta z^+$ | $\Delta y^+$ | points below $y^+=10$ |
|---|---|---|---|---|
| Wall-resolved LES | 50–150 | 10–40 | 1 | 3–5 |
| Wall-modelled LES | 100–600 | 100–300 | 30–150 | — |

Two WMLES of a fan stage that the authors judge compliant with these ranges
differ qualitatively — a large stator separation on the 95 M-cell mesh
vanishes on the 210 M-cell mesh — so they call the requirements "quite
broad" (§4.2.2; see [wall-modelled LES](/methods/wall-modelled-les.md) and the
qualification there on their mean values). For wall-resolved LES,
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§II D) recall typical
eddy-viscosity resolutions $\Delta x^+<130$, $\Delta z^+<30$ and the stricter
$\Delta x^+<100$, $\Delta z^+<20$ that Cimarelli & De Angelis require for an
eddy-viscosity model to resolve the interscale transfer including the spanwise
inverse cascade. Their own a posteriori dynamic-Smagorinsky LES of channel
flow at $Re_\tau=400$ predicts the DNS mean velocity on grids of
$(\Delta x^+,\Delta z^+)=(26.2,13.1)$ and $(52.4,26.2)$ but over-estimates it
on $(105,52.4)$, with $\Delta y^+=0.7$–20 in all three (App. C, Table I);
a priori, with a sharp filter in $x$ and $z$ matching the medium grid, the
filtered wall-normal fluctuation is below 80 % of the unfiltered one for
$y^+<50$, from which they suggest $\Delta z^+<20$ may be
needed for the near-wall anisotropy (§III B, Fig. 2). With the filter of the coarse grid
the part of the SGS stress that transfers no energy carries a mean shear
stress comparable to the eddy-viscosity part (§III C, Fig. 3); see
[energy backscatter](/definitions/energy-backscatter.md).

For high-order elements the "first cell" is ambiguous:
[Slaughter et al. (2023)](/sources/slaughter-2023.md) (§3.6, Fig. 4) measure
the wall-normal resolution by the position of the first quadrature point
inside the wall element, and the spanwise resolution of their Fourier
direction by the decay of the modal energy rather than by $\Delta z^+$; their
in-plane spacings lie below the limits of Georgiadis et al. (2010) (values
not printed) except two small regions where $y^+$ is "slightly above one".
Morsbach et al. (2024, §3.1, Fig. 2) normalize the element size by the
polynomial degree $N$ and keep the ratio of mean solution-point spacing to the
estimated Kolmogorov length below 6 in the free stream.
[Wang (2024)](/sources/wang-2024-b.md) (§4.2, Eq. 26, after Jia et al. as
cited) make the per-degree-of-freedom convention explicit for DG and flux
reconstruction: the first-cell $y^+$ computed from the cell height $d$ is
divided by $N+1$, $y^+=\rho u_\tau d/\big(\mu(N+1)\big)$, with $u_\tau$ of the
time-averaged flow. [Duan & Wang (2024)](/sources/duan-2024.md) print "equivalent
resolutions" $(\Delta x^+,\Delta y^+_{\min},\Delta z^+)=(5.7,0.68,5.7)$ for
their wall-resolved channel ($Re_\tau=180$, $N=3$, $100\times20\times33$
elements), which are the element sizes divided by $N+1=4$, but for their
wall-modelled channels the undivided element sizes (§5.3–5.4) *(compiler
check, not in the sources)*; Blind et al.
(2023) divide by $N+1=6$ (below). A spacing in wall units for an element
method is therefore comparable across sources only after checking which
convention is used.

For stabilized finite elements of lowest order, [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md)
(§3.2, App. B) place implicit-LES resolution between DNS and wall-resolved
LES: they quote, for the [periodic hill](/benchmarks/periodic-hill.md) DNS of
Krank et al. (as cited), $\Delta y^+_{\max}<0.86$ and
$\Delta x^+_{\max}=\Delta z^+_{\max}=7.2$, and for wall-resolved LES
$\Delta x^+\approx50$–100, $\Delta y^+\approx1$, $\Delta z^+\approx15$–30,
and call a mesh in between "exactly the definition of implicit LES when it
comes to mesh resolution". Apart from $y^+$ criteria they found no a
posteriori mesh-quality criterion in the literature on stabilized methods
(§3.2). Their averages are listed in the next section; on their finer
meshes the averaged wall-parallel spacings ($\Delta x^+\approx1.4$–2.4) lie
below the DNS maxima they quote, a comparison of averages with maxima at
$Q_1$ against high order *(compiler check, not in the sources)*.

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

- **Wall-modelled grids in wall units and per $\delta$.** Gillyns et al.
  (2022, §6–9) run spectral-element WMLES of channel flow at $Re_\tau=1000$
  with $22\times16$ elements of degree 7 on $2\pi\delta\times\pi\delta$
  (average node spacings $0.040\delta$ and $0.028\delta$, i.e. 24.5 and 35.7
  nodes per $\delta$), chosen by refining until element-interface spikes are
  small and found similar to the guidelines of Larsson et al.; in wall units
  this is about $\Delta x^+\approx41$, $\Delta z^+\approx28$ *(compiler check,
  not in the sources)*. Five wall-normal elements per half-height (35 nodes)
  are acceptable and four "not sufficiently resolved" (§8), though §9 calls
  the four-element mesh "a fair compromise"; at $Re_\tau=5200$ ten elements per
  half-height with the same in-plane count keep mean-velocity errors below
  1 %. Bae & Koumoutsakos (2022, Methods) use $\Delta x=\Delta z=0.05\delta$ (20 points
  per $\delta$) and $\Delta y=0.01$–$0.05\delta$ in channel flow up to $Re_\tau=10^6$, and for the boundary
  layer at $Re_\theta=6500$ $\Delta x^+=128$, $\Delta z^+=105$, uniform
  $\Delta y^+=64$, about ten wall-normal points per $\delta$ at the inlet.
  [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) (§3) use
  $\Delta x\approx0.08\delta_0$, $\Delta z=0.05\delta_0$ and four cells below
  $h_{\mathrm{wm}}=0.1\delta_0$ for a Mach 3 shock/boundary-layer interaction,
  about 20 M cells for a span of $5\delta_0$ and 200 M for $50\delta_0$.
- **Wall-resolved LES at coarse resolution.** [Prakash et al. (2022)](/sources/prakash-2022.md)
  (§III.B.3, Table 3) run channel flow at $Re_\tau=590$ on meshes with
  $\Delta x^+=78$ and 58, $\Delta z^+=39$ and 29, first off-wall
  $\Delta y^+=1$, and find their optimally clipped gradient model and the
  dynamic mixed model close to DNS on the medium mesh. They argue, after
  Baggett et al. as recalled, that in anisotropic wall-bounded flows at
  moderate resolution an accurate SGS stress, not only an accurate
  dissipation, is needed for accurate statistics, and hypothesize that
  structurally accurate models therefore lower mesh requirements (§I–II).
- **Hybrid RANS/LES on adapted meshes.** [Mozaffari et al. (2022)](/sources/mozaffari-2022.md)
  stress that every change of cell size in space or time perturbs hybrid
  RANS/LES turbulence: across a fine-to-coarse interface "the loss of
  resolved turbulence is never equal to the gain in modeled turbulence"
  (§1, Fig. 1, from a thesis they cite). Their average-based adaptive
  refinement (see [mesh adaptation](/methods/mesh-adaptation.md)) predicts
  the reattachment length of a backward-facing step at $Re_H=28\,000$ within
  5.1 % on 2.5 M cells and 3.6 % on 9.9 M cells, against 9.6 % for a 9.3 M
  cell hand-designed mesh (Table 2; the text of §4.1 gives 9.2 M), and recommends a minimum cell size of a
  quarter of the Taylor microscale for vortex cores (§5.1, §6).

- **Implicit LES with high-order elements.** Morsbach et al. (2024, §3.1,
  Table 2) run a wall-resolved implicit DG LES of the MTU T161 low-pressure
  turbine cascade (exit $Re=90\,000$, $M=0.6$) at $N=5$: 876 960 elements,
  $189.4\times10^6$ degrees of freedom, mean spacings per solution point
  $(23.1,0.742,15.0)$ in wall units at blade midspan and $(23.2,0.809,18.8)$ on
  the end walls (maxima $(65.2,1.71,60.3)$); a coarser mesh of 312 424
  elements, mainly coarser spanwise, gives the same blade loading but a
  subtly different skin friction downstream of the transition peak,
  "indicating that the resolution on the coarse mesh is not entirely
  sufficient" (§4.1, Fig. 7). [Zhao et al. (2023a)](/sources/zhao-2023.md)
  (§5.2, Table 6) run implicit LES of channel flow with high-order
  gas-kinetic schemes on $64\times96\times64$ cells at $Re_\tau=180$
  ($\Delta x^+=17.66$, $\Delta z^+=8.33$ as printed, $\Delta y^+=0.29$–7.76)
  and $96^3$ at $Re_\tau=395$ ($25.84$, $12.92$, $0.58$–20.83); all schemes
  show "an unnatural leveling-off of the energy spectrum near the cutoff
  wavenumber", attributed to the mesh resolution (§5.2.3).
- **Hybrid RANS/LES of a full-scale car.** Delassaux et al. (2023, §4.4,
  §5) size a DDES grid of 115 M cells with wall-resolved prism layers
  ($y^+\approx1$, 20 layers) and wall-parallel spacings kept coarse on
  purpose against the boundary-layer thickness ($\Delta x^+\approx600$ on the
  roof) to avoid grid-induced separation; from their Ahmed-body calibration
  they recall that $y^+<1$ and "at least 15 or 20 prism layers" are needed.
  The constraint is the reverse of WMLES sizing (see
  [boundary-layer-conforming grid](/methods/boundary-layer-conforming-grid.md)).
- **Implicit LES with stabilized $Q_1$ finite elements.** Prieto Saavedra
  et al. (2024, §3.2, §4.2–4.4, Tables 4–5, B.6) run the
  [periodic hill](/benchmarks/periodic-hill.md) at $Re_h=5600$ with SUPG/PSPG
  stabilization and no SGS model ([implicit LES](/definitions/implicit-les.md))
  on 250 K to 4 M hexahedra (1.1 M to 16 M DoFs), against 12.4 M cells for
  the LESOCC reference LES. Averaged wall spacings are
  $(\Delta x^+,\Delta y^+,\Delta z^+)=(2.96,1.66,4.20)$, $(2.40,1.16,2.26)$
  and $(1.39,0.61,1.51)$ on 250 K, 1 M and 4 M cells ($\Delta y^+_{\max}$
  4.30, 3.15, 1.73). The 1 M and 4 M meshes give reattachment points close
  enough that the authors call the result mesh independent (§5). The time
  step is not independent of the mesh: on the 250 K mesh refining $\Delta t$
  from 0.1 to 0.0125 moves the reattachment point from 4.73 to 5.37 hill
  heights (Rapp's experiment gives 4.83), which the authors read as a loss of
  accuracy caused by the stabilization parameter, and hence the added
  dissipation, shrinking with $\Delta t$; on the 4 M mesh all
  but the largest step agree (§4.2, Table 5). At $Re_h=10\,600$ and 37 000
  they use 120 K–500 K cells, with Reynolds stresses over-predicted (§4.4).
- **Turbine cascades at high order.** Wang (2024, §4.2–4.3, Tables 3, 6)
  runs implicit DG LES with shock-capturing filters: the T106C low-pressure
  cascade (exit $Re=80\,000$) at $N=3$ on 122 904 hexahedra (7.87 M DOFs per
  equation) with $(y^+,x^+,z^+)\approx(0.5,20,6)$, and the LS89 high-pressure
  vane (exit $Re=1.13\times10^6$) on 6.6 M to 31.3 M DOFs with
  $y^+\approx0.75$, $x^+\approx30$ and $z^+\approx90$, 60, 45 for 10, 15 and
  20 spanwise layers. The isentropic Mach number on the LS89 vane is
  insensitive to resolution (an inviscid 2D run already predicts it, as
  cited), so it cannot validate the resolution; the heat-transfer
  coefficient improves from $N=2$ to $N=3$ and with spanwise refinement, and
  15 layers ($z^+\approx60$) are judged cost-effective (§4.3.1, Figs. 13–14).
  See [turbine cascade](/benchmarks/turbine-cascade.md).
- **High-order wall-modelled channels.** Duan & Wang (2024, §5.4) run
  flux-reconstruction WMLES of channel flow on $60\times16\times40$ elements
  of degree $N=2$–5 at $Re_\tau=5200$, element sizes
  $(\Delta x^+,\Delta y^+,\Delta z^+)=(1088,650,544)$, and at $Re_\tau=544$
  on the same mesh, $(114,68,57)$; with the
  [Vreman model](/methods/vreman-model.md) and filter width
  $V^{1/3}/\sqrt{N+1}$ the mean velocity is consistent with DNS at every $N$
  (see [wall-modelled LES](/methods/wall-modelled-les.md)).
- **One fixed grid across ten decades.** Vadrot et al. (2023a) run
  half-channel WMLES on the same uniform $48^3$ grid at every $Re_\tau$ from
  180 to $10^{10}$ and recover the log law with a learned wall model whenever
  the matching height lies in the log layer, while neither near-wall nor
  outer peak of the streamwise velocity variance is resolved (§III.A,
  Figs. 6–7; [Vadrot et al. 2023a](/sources/vadrot-2023.md)).
- **Hybrid RANS/LES of transonic buffet.** [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md)
  (§4.5.3, Table 1, Fig. 8) run [PANS](/methods/partially-averaged-navier-stokes.md)
  of the OAT15A airfoil in half of the wind tunnel on grids of 5.0 M, 10 M
  and 16.7 M cells, all with $\Delta y^+<1$: the coarse grid resolves no
  three-dimensional structure in the separated boundary layer, the medium
  grid mainly spanwise trailing-edge shedding, and only the fine grid, with
  half the time step, the stall cells of the experiment; buffet itself
  appears on all three.
- **Under-resolved no-slip walls in hybrid LBM.** Mozaffari et al. (2024,
  §3.3) impose no slip on the Ahmed body at $y^+\approx100$–150 on the slant
  (45.8 M nodes, finest cell 1.3 mm): the $35^\circ$ wake is reproduced but
  at $25^\circ$ separation is late with no reattachment, which they
  attribute to this resolution ([Mozaffari et al. 2024](/sources/mozaffari-2024.md)).
- **Training grids of a learned wall model.** [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
  (§2.6) train their wall model on WMLES with isotropic grids $\Delta=\delta/n$,
  $n=5$ to 380 ($\delta$ the channel half-height, $n$ page-local), and below
  $\delta/380$ on DNS data so that the model converges to no slip; their NASA
  CRM-HL WMLES uses 30 M points with 0–20 points per boundary-layer
  thickness (§4.7).

## Resolution found by solution-adaptive grids

Instead of prescribing spacings, [Blind et al. (2023)](/sources/blind-2023.md)
let a residual-based estimator choose them (see
[mesh adaptation](/methods/mesh-adaptation.md)) in DG spectral element LES
of degree 5, and report what the converged grids look like (spacings per
degree of freedom, i.e. element size over 6):

| Case | Converged grid | Wall spacing $(\Delta x^+,\Delta y^+,\Delta z^+)$ per DOF | DOF |
|---|---|---|---|
| Wall-resolved channel, $Re_\tau=550$ (§3.1, Table 1) | $l=4$, 16 200 elements | $(18.3,1.3,7.6)$ | 3.5 M |
| Wall-resolved channel, $Re_\tau=2000$, 2-to-1 mortars (§3.2, Table 3) | $l=5$, 142 662 elements | $(26.9,2.0,9.6)$ | 30.8 M |
| Wall-modelled channel, $Re_\tau=2000$, $h_{\mathrm{wm}}=0.1h$ (§3.3, Table 4) | $l=3$ (mean velocity), $l=4$ (stresses) | $(104.2,34.7,43.5)$ at $l=3$; $(53.8,10.0,26.3)$ at $l=4$ | 0.95 M; 6.7 M |

The $Re_\tau=550$ grid, about $(18,1,8)$, is "viewed as an acceptable
(albeit a bit fine) grid by the LES community", and the sequence of spacings
resembles the finite-difference results of Toosi & Larsson. The estimator
asks for larger wall-parallel spacings in the viscous sublayer than in the
buffer layer, which the authors call correct because wall-parallel length
scales grow there (citing Jiménez). Mortar interfaces that coarsen the
wall-parallel spacing away from the wall save "up to approx. 50 %" of the
elements against a structured mesh with the same, mortar-free, spacing
(128 154 elements saved against 142 662 used at $l=5$); the time step is set by the smallest cell and
does not change, so the saving is in processor count (§3.2), while for the
airfoil the authors equate it with compute time (§4). The estimator says
nothing about whether a grid is converged: convergence must be judged on the
quantities of interest (§2.5).

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

For hybrid RANS/LES of a ship hull at 10° drift (DDES-SST), Mozaffari et al.
(2022, §5.1) report about 160 000 CPU-hours on a 154 M cell adapted mesh
against about 250 000 on a 163 M cell hand-designed mesh, and for steady RANS
about 16 000 (47 M cells) against 30 000 (163 M); the runs used different
processor counts and the hand-designed DDES included extra analysis steps, so
"the adaptation probably saves some time, but not a lot". Training the
reinforcement-learning wall model of Bae & Koumoutsakos (2022, p. 8) costs
$O(10^3)$ CPU-hours, against an estimated $O(10^7)$ for the DNS data a
supervised model would need at $Re_\tau=4200$.

Delassaux et al. (2023, §7.6) run steady RANS of a full-scale car on 384
cores in about 2 h and DDES on 1152 cores in about one and a half days, and
call the hybrid simulation "18 times more expensive"; 18 is the wall-clock
ratio, and in core-hours the ratio is $1152\times36/(384\times2)=54$
*(compiler check, not in the sources)*. Morsbach et al. (2024, Table 2)
report 25 852 CPU-hours per convective time unit for their fine turbine LES
(5120 MPI ranks) and 5861 for the coarse one (hardware not stated).
Lozano-Durán & Bae (2023, §2.6) report that their learned wall model makes
WMLES 1.1–1.3 times as expensive as the algebraic equilibrium model.

Prieto Saavedra et al. (2024, App. C, Table C.9; Intel Skylake, 40 cores per
node) report the core-hours for 1000 s of periodic-hill flow at $Re_h=5600$
(about 110 flow-throughs at 9 s each *(compiler check, not in the sources)*)
for time steps 0.1, 0.05, 0.025 and 0.0125: 3647, 5180, 6933 and 9400 on
250 K cells; 16 800, 24 667, 36 667 and 39 933 on 1 M; 116 667, 174 000,
188 000 and 167 333 on 4 M. They conclude that implicit LES "can reduce the
computational effort, in terms of mesh size and degrees of freedom", without
an equal-accuracy comparison with an explicit LES (§5). Petrocchi & Barakos
(2024, §4.6, Table 3) measure PANS at "+3.1%" wall time per inner
iteration against URANS on the same grid and processors (2.00 s against
1.95 s as printed, whose ratio is 2.6 % *(compiler check, not in the
sources)*; "about 3%" in the text), the largest increase being in the
residual Jacobian. [Constant et al. (2024)](/sources/constant-2024.md)
(§6.3, Tables 8–9) run steady RANS of the NASA CRM high-lift configuration
on an immersed-boundary Cartesian mesh of 2.4 billion cells, four times the
550 M cells of the body-fitted reference, on $20\times28$ Broadwell cores,
and report the mesh pre-processing at under seven hours from the surface
mesh alone, against weeks for a comparable curvilinear grid (as they state
it, without breakdown).

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
- **Savings against what.** The abstract of Blind et al. (2023) claims
  solutions "at up to 50% lower cost at comparable accuracy compared to when
  using human-generated grids"; the 50 % measured in §3.2 and §4 is counted
  against a structured mesh of the same spacing without mortars, not against
  an independently designed grid. Their airfoil DOF counts are 512 per
  element (Table 6), i.e. $8^3$, polynomial degree 7, whereas §2.3 states
  degree 5 "throughout this work" and the channel tables give $6^3=216$
  *(compiler check, not in the sources)*. Locators refer to the arXiv v1
  preprint read.
- **Recalled exponents.** The WRLES cost exponents in this page are
  recalled, not derived, by the sources: $Re^{2.7}$ by Griffin et al. (2023)
  after Yang & Griffin (2021), $Re^{2.5}$ by Morsbach et al. (2024) after Choi
  & Moin (2012). The two rest on different underlying works whose
  assumptions the citing sources do not state; no source of this bundle
  derives either.
- Zhao et al. (2023a, Table 6) print $\Delta z^+=8.33$ at $Re_\tau=180$ with
  $L_z=\pi$ and 64 cells, where $\pi\cdot180/64\approx8.84$; their printed
  $\Delta x^+=17.66$ and the $Re_\tau=395$ values are reproduced by the same
  arithmetic *(compiler check, not in the sources)*.
- Cai et al. (2022, §III) call $\lambda_H$ "the Taylor scale describing the
  integral motions in the wake"; the estimate is printed as such.

# Citations

- [Domingo & Vervisch (2023)](/sources/domingo-2023.md) — §2, Eqs. (1)–(6).
- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §7.1–7.4, Figs. 24–28.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I.
- [Griffin et al. (2023)](/sources/griffin-2023.md) — §1.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1; §2.2; §3.2; §4, Tables 1–2.
- [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md) — §III.B, Eqs. (5)–(7), Fig. 6; §V.A–V.E; App. A, Eqs. (13)–(14).
- [Agrawal et al. (2022)](/sources/agrawal-2022.md) — §VIII.B.
- [Haering et al. (2022)](/sources/haering-2022.md) — §V.A.1; §V.B.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Introduction; p. 8; Methods.
- [Gillyns et al. (2022)](/sources/gillyns-2022.md) — §1; §6–9, Tables 1–3.
- [Hoy & Bermejo-Moreno (2022)](/sources/hoy-2022.md) — §3.
- [Prakash et al. (2022)](/sources/prakash-2022.md) — §I–II; §III.B.3, Table 3.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §1, Fig. 1; §4, Table 2; §5.1; §6.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I; §III, Tables I–II.
- [Blind et al. (2023)](/sources/blind-2023.md) — Abstract; §2.3; §2.5; §3.1–3.3, Tables 1, 3, 4; §4, Table 6.
- [Morsbach et al. (2024)](/sources/morsbach-2024.md) — §1; §3.1, Table 2, Fig. 2; §4.1, Fig. 7.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1; §4.4; §5; §7.6 (HAL author manuscript).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §3.3, Table 5; §4.2.2 (HAL accepted manuscript).
- [Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) — §II D; §III B–C, Figs. 2–3; App. C, Table I (arXiv v3).
- [Slaughter et al. (2023)](/sources/slaughter-2023.md) — §3.6, Figs. 4–5 (Research Square preprint v1).
- [Zhao et al. (2023a)](/sources/zhao-2023.md) — §5.2, Table 6; §5.2.3 (arXiv v1).
- [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md) — §2.6; §4.7.
- [Wang (2024)](/sources/wang-2024-b.md) — §4.2, Eq. (26), Table 3; §4.3, Tables 5–6, Figs. 13–14 (arXiv v2).
- [Duan & Wang (2024)](/sources/duan-2024.md) — §5.3–5.4.
- [Prieto Saavedra et al. (2024)](/sources/prietosaavedra-2024.md) — §3.2, Table 4; §4.2–4.4, Table 5; §5; App. B, Table B.6; App. C, Table C.9.
- [Vadrot et al. (2023a)](/sources/vadrot-2023.md) — §III.A, Figs. 6–7 (arXiv v3).
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — §4.5.3, Table 1, Fig. 8; §4.6, Table 3.
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §3.3 (HAL accepted manuscript).
- [Constant et al. (2024)](/sources/constant-2024.md) — §6.3, Tables 8–9 (HAL author manuscript).
