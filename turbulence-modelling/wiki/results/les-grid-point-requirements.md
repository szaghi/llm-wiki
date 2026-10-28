---
type: Result
title: "Grid-point requirements of LES and DNS"
description: "How the grid-point and time-step counts of DNS, wall-resolved and wall-modelled LES scale with Reynolds number, the explicit WMLES cost model, wall-unit and per-thickness resolution criteria and evidence that meeting them is not sufficient, the resolutions used in practice and found by adaptive grids, measured costs, and why WMLES cost exponents differ."
status: established
aliases: [grid-point estimates, resolution requirements, LES cost scaling, Chapman estimate, Choi–Moin estimate, WMLES cost]
tags: [les, wmles, dns, boundary-layer]
timestamp: 2026-10-28T07:06:00Z
---

# Grid-point requirements of LES and DNS

The cost of a scale-resolving simulation is the number of grid points times
the number of time steps, and both grow with Reynolds number at a rate set by
what must be resolved: the Kolmogorov scale for
[direct numerical simulation](/definitions/direct-numerical-simulation.md), the
near-wall streaks for wall-resolved LES (WRLES), only the eddies of the
boundary-layer thickness for [wall-modelled LES](/methods/wall-modelled-les.md).
The sources of this bundle cite the classical estimates, derive an explicit
WMLES cost model, and report what resolution sufficed in practice.

## Reynolds-number scaling

| Simulation | Grid points | Cost (points × steps) | Source |
|---|---|---|---|
| DNS, volume of side $L_d$ resolved at $2\eta$ | $(L_d/2\eta)^3=(L_d/2L)^3Re_T^{9/4}$ | — | [Domingo & Vervisch (2023)](/sources/domingo-2023.md), §2, Eqs. (1)–(2) |
| WRLES, flat plate | $Re_{L_x}^{1.86}$ | $Re^{2.7}$ | points: [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md), §I; cost: [Griffin et al. (2023)](/sources/griffin-2023.md), §1 — both after Yang & Griffin (2021) |
| WMLES, flat plate | $Re_{L_x}^{1.0}$ | $Re^{1.1}$ | same |
| WMLES | $\propto Re_c$ | $\propto Re_c^{4/3}$, "which accounts for the reduction in time step" | [Goc et al. (2021)](/sources/goc-2021.md), §2.2, §4, after Choi & Moin (2012) |
| WMLES, order of magnitude | $\Delta/\delta_\nu\sim O(Re_\tau/10)$ for $\delta/\Delta\sim O(10)$ | — | [Hu et al. (2024)](/sources/hu-2024.md), §2, Eqs. (1)–(4) |
| WMLES on a [BL-conforming grid](/methods/boundary-layer-conforming-grid.md) | $n_\delta^{13/6}\,Re\,(Re_\Delta^{\min})^{-5/6}$ | steps $\sim t_{\mathrm{run}}\,Re\,(Re_\Delta^{\min})^{-1}$ | [Lozano-Durán et al. (2022)](/sources/lozanoduran-2022.md), §III.B, Eqs. (5)–(7) |

Page-local symbols: $L_d$ the domain size, $L$ the integral length,
$Re_T=k^{1/2}L/\nu$ the turbulent Reynolds number, $Re_{L_x}=L_xU_\infty/\nu$ the
plate-length Reynolds number, $n_\delta$ the points per boundary-layer
thickness, $Re_\Delta^{\min}=\Delta_{\min}U_\infty/\nu$ the minimum grid
Reynolds number, $t_{\mathrm{run}}$ the run length in flow-through times. The
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
wall-resolved LES; [Wu et al. (2024)](/sources/wu-2024.md) (§1) cite Choi &
Moin (2012) for an LES near-wall grid "similar to that of Direct Numerical
Simulation", after quoting 2.6 billion cells and 6 million CPU hours for
the LES of a three-element airfoil at $Re_c=1.23\times10^6$ by Terracol &
Manoha (as cited), as the reason
high-lift airfoils at flight Reynolds numbers motivate their hybrid
[self-adaptive turbulence eddy simulation](/methods/self-adaptive-turbulence-eddy-simulation.md).
[Delassaux et al. (2023)](/sources/delassaux-2023.md)
(§4.1) cite Spalart's forecast that wall-resolved LES and DNS of a
full-scale high-Reynolds-number geometry would become available in 2050 and
2080 respectively. [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md)
(§1, Fig. 1) cite Spalart's view that accurate "pure"
WMLES of a full-size airliner wing will not be possible before 2045, because
$\delta$ grows from about 1 mm at the leading edge to tens of centimetres at
the trailing edge and LES needs near-isotropic cells where RANS accepts high
aspect ratios (their Fig. 1 maps $1/\delta^2$ over the wing); they add that
wall-resolved LES requirements are "almost identical to those of DNS".
[Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) (§1) cite from
Choi & Moin (2012) grid counts growing as $Re^{37/14}$ for DNS,
$Re^{13/7}$ for wall-resolved and $Re$ for wall-modelled LES
($37/14\approx2.64$ *(compiler check, not in the sources)*), and from
Piomelli (2014) that above $Re=O(10^5)$ more than 90 % of the points of a
wall-resolved LES resolve less than 10 % of the domain.
[Maeyama & Kawai (2023)](/sources/maeyama-2023.md) (§1) quote the same three
Choi–Moin exponents ($Re^{37/14}$, $Re^{13/7}$, $Re$; after Chapman 1979 and
with Yang & Griffin 2021, as cited).
[De Vanna et al. (2022)](/sources/devanna-2022.md) (§1) quote the same
$Re_L^{13/7}$ for wall-resolved LES after Choi & Moin (2012), calling the
growth "mostly quadratic", and [van Noordt et al. (2022)](/sources/vannoordt-2022.md)
(§1) cite the Choi–Moin scaling as the motivation of WMLES.
[Brenner et al. (2022)](/sources/brenner-2022.md) (§1) cite Xiao & Jenny
for a near-wall resolution cost growing as $Re^3$ for DNS and $Re^{1.8}$
for LES of wall-bounded flows; the source states neither the Reynolds
number nor whether time steps are counted (see Qualifications).

The differential forms behind these exponents are written out by
[Bose & Park (2018)](/sources/bose-2018.md) (§1, Eqs. 1–2), after Chapman
(1979) and Choi & Moin (2012) as cited: per wall area $dx\,dz$,

$$dN_{\mathrm{wr}}=\frac{n_y}{\Delta x_w^+\Delta z_w^+}\frac{\tau_w\,dx\,dz}{\rho\nu^2},\qquad dN_{\mathrm{wm}}=\frac{n_xn_yn_z\,dx\,dz}{\delta^2},$$

with $n_i$ the points per $\delta$ in direction $i$ and $\Delta x_w^+$,
$\Delta z_w^+$ the wall-unit spacings that resolve the near-wall eddies
(page-local); integrated over a plate they give $Re_L^{37/14}$ for DNS,
$Re_L^{13/7}$ for WRLES and $Re_L$ for WMLES. The WMLES count depends on the
wall only through $\delta$, $N\propto\int\delta^{-2}dA$, the form of
Lozano-Durán et al.'s Eq. (5) above with $n_\delta^3$ points per $\delta^3$
*(compiler check, not in the sources)*. [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md)
(§2.1) apply the DNS estimate to turbomachinery: for evolving boundary
layers on bladed components the cost scales as $Re_{L_x}^{37/14}$, and the
domain must also hold the blade passages and the gaps between rows.
[Heinz (2020)](/sources/heinz-2020.md) (§1) states, citing the literature, that LES of wall-bounded
flows "can become computationally extremely expensive (almost as expensive
as DNS)", the motivation of hybrid methods.

## DNS

**The historical estimates.** In the account of [Kim & Leonard (2024)](/sources/kim-2024-b.md)
(§2.1–2.2, §5), von Neumann (1949) judged even an $8^3$ simulation beyond the
computers of that time, and Corrsin (1961) argued that a simulation would need
$Re=10^4$ to show universality and, from Kolmogorov scaling, at least
$10^{12}$ grid points, an estimate later substantiated by Case et al. (1973)
(all as cited). The first DNS of decaying isotropic turbulence (Orszag &
Patterson 1971–1972) ran on $16^3$ and $32^3$ meshes at initial $Re_\lambda=35$
on a 3-megaflop CDC 6600, 30 s per time step at $32^3$. Orszag (1971, as
cited) estimated that an $N^3$ spectral simulation (here $N$ the points per
direction, not the polynomial degree) is as accurate as a $(4N)^3$
finite-difference one at the cost of a $(2N)^3$ one, and the review prints
the pseudospectral transform count as "$O((N\log N)^3)$" against the $O(N^6)$
of the convolution sums. Peak speed grew by about $10^{12}$ from the CDC 6600
to the 2-exaflop Frontier (2022); isotropic DNS reached $4096^3$ (Kaneda et
al. 2003) and $8192^3$ (Yeung et al. 2015) at $Re_\lambda=1200$–1300, with
well-constructed codes reaching 20–50 % of peak (Bose, personal
communication, as cited) (§5).

Domingo & Vervisch (2023, §2) take $h=2\eta$ as sufficient for the dissipative
range (after Moin & Mahesh, as they cite it) and derive the point count of
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

For isotropic turbulence the record is set by
[Yeung et al. (2025)](/sources/yeung-2025.md): forced homogeneous isotropic
turbulence at $Re_\lambda\approx2500$ on $32\,768^3$ points with a GPU
Fourier pseudo-spectral code on the Frontier exascale machine, in single
precision (§1–2, Table 1). The largest pseudo-spectral grid that fits in
Frontier's memory is $40\,960^3$ (§1). Their resolution parameter is
$k_{\max}\eta=(\sqrt2N_x/3)\eta$: 1.4 suffices for scales larger than $\eta$,
and the statistics reported use 2.8, reached only for a few Kolmogorov
times by the [multi-resolution independent simulations](/methods/multi-resolution-independent-simulations.md)
protocol (§2.2). At fixed forcing and fixed $k_{\max}\eta$,
$\nu\propto N_x^{-4/3}$ and $Re_\lambda\propto N_x^{2/3}$, a 58 % increase for
each doubling of $N_x$ (§2.2), so going from $Re_\lambda=1000$ to 2500 needs
four times the points per direction, at least 64 times the wall time per
step and 256 times for a given physical time, on a machine with at least 64
times the memory (§5). The $N_x^3\propto Re_\lambda^{9/2}$ that follows is the
$Re_T^{9/4}$ of the table with $Re_\lambda\propto Re_T^{1/2}$ *(compiler check,
not in the sources)*. They add, after Yakhot & Sreenivasan as cited, that
scales finer than $\eta$ become more frequent as the Reynolds number grows,
so better small-scale resolution than often practised is needed (§1).

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
and Yang & Griffin, as they cite them. With time steps limited by
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
[Inagaki & Kobayashi (2023)](/sources/inagaki-2023.md) (§II D) cite typical
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

[Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) (§III B 2), citing
the literature, give a typical fine wall-resolved LES mesh as
$\Delta x^+\approx50$–130 and $\Delta z^+\approx15$–30, with 10–30 points
across the boundary layer and the first point at $y^+\lesssim1$. Their own
implicit LES of a Mach 1.94 oblique shock interaction on a compliant panel
(production grid "medium 2", $384\times128\times192$ cells, full 152 mm span)
runs at $\Delta x^+=717$, $\Delta z^+=634$, $y^+=4.8$ with 37 points across
the incoming layer. The other grids of their study range from
$\Delta x^+=1076$, $\Delta z^+=551$ (coarse) to $268$, $100$, $y^+=2.7$
(fine, 33 mm span) (Table III). They judge the medium 2 grid "adequately
accurate, at least concerning the flow properties of interest" (mean and
rms wall pressure, against their fine grid; §IV A, Fig. 4). They estimate a
wall-resolved implicit LES at about 175 times its cost (see
Qualifications).

Other sources cite stricter wall-resolved targets:
[Baldan & Guardone (2025)](/sources/baldan-2025.md) (§1.1, §2.1, Fig. 7),
after Piomelli & Balaras (2002) and Georgiadis et al. (2010) as they cite
them, require $\Delta x^+<40$, $\Delta y^+<5$, $\Delta z^+<20$ (the source's
$\xi^+$, $\eta^+$, $z^+$), a streamwise bound below the 50–150 range above,
and check them span-averaged at the most demanding instant of a pitching
airfoil, where the near-wall velocity exceeds twice the free stream; the
first-cell $\Delta y^+$ is close to 1. [Maejima & Kawai (2025)](/sources/maejima-2025.md)
(§4.1, App. B) state the requirement through the near-wall streaks of
spanwise wavelength $\lambda_z^+\approx100$ (page-local, after Smith &
Metzler as cited): their channel LES at $(\Delta x^+,\Delta z^+)\approx(36,18)$
puts five to six points per wavelength, "close to" the requirements of
Kawai & Fujii (2008) as cited, and reproduces the DNS mean velocity and
Reynolds stresses with the selective mixed-scale model, while at
$(72,36)$, two to three points per wavelength, the mean velocity is
over-predicted and the stresses deviate (Fig. 5).

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

## Points per thickness in published airfoil WMLES

Bose & Park (2018, §3, Fig. 5) set the estimates against what published
airfoil WMLES used: cell counts of NACA 0012, NACA 4412, Aérospatiale-A,
cruise NASA CRM and MD 30P/30N simulations, scaled to a span-to-chord ratio
of 4, compared with Chapman's estimate at
$n_xn_yn_z=10^3$ and $20^3$. "Strong conclusions cannot be drawn" from the
few points, but "the majority of calculations performed seem to require
outer-layer resolution of $n_xn_yn_z\gtrsim20^3$ for accuracy", which raises
the cost prefactor assumed by Choi & Moin by a factor of three to five; the
scatter is partly the difficulty of keeping $\delta^3/(\Delta x\Delta y\Delta z)$
fixed when $\delta$ varies, since practical grids follow a nominal thickness
(see [boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)).
Three further statements of the same section bear on cost:

- the wall model itself is often cheap relative to the flow solution, the
  full non-equilibrium boundary-layer equations costing about twice the
  baseline LES, and load imbalance at large processor counts can matter more
  (see [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md));
- the claim that laminar regions dominate the cost, because $N\propto\int\delta^{-2}dA$
  and the laminar layer is thin, is "overly pessimistic": it presumes
  isotropic cells, which outer-layer turbulence ($y/\delta>0.1$) justifies but
  a laminar layer may not need, and aspect ratios $AR=O(10)$ would cut the
  prefactor "by orders of magnitude";
- the conclusion of Slotnick et al. (2014), as cited, that petascale
  resources are needed for airfoils with span equal to chord at $Re_c\sim10^6$
  is "inconsistent with the cost incurred by the recent wall-modeled
  simulations" in that range, although, as Slotnick et al. pointed out,
  relaxing the laminar resolution presupposes that the LES captures
  transition.

Goc et al. (2021, §1) also call the estimates of Spalart, Choi & Moin and
Slotnick et al. too pessimistic, for integrated forces, and obtain
$C_{L,\max}$ with about ten points per $\delta_{99}$ at the trailing edge
(next section). Bose & Park (§3, above) read the published airfoil WMLES as
needing more than the Choi & Moin prefactor, and expect (§4.1) the outer
peak of the streamwise fluctuations to be likely unresolved with the
Choi & Moin resolution, $\delta/\Delta x_i\sim10$.

## What resolution sufficed in practice

- **Grid convergence of WMLES against the matching height.**
  [Hu et al. (2024)](/sources/hu-2024.md) (§2, Eqs. 1–4) argue that a
  quantity with length scale $O(\delta)$, resolved by $O(10)$ cells, can
  converge on WMLES grids with $\delta/\Delta\sim O(10)$, that is
  $\Delta/\delta_\nu=(\Delta/\delta)Re_\tau\sim O(Re_\tau/10)$, and that ideally
  convergence should be shown on grids with $\Delta^+>O(100)$ and
  $\Delta/\delta=O(0.1)$ at $Re_\tau=O(10^4)$; they cite Choi & Moin for 10
  to 30 cells per $\delta$, Goc et al. for $O(1)$ cells per $\delta$ in
  aircraft convergence checks, and aircraft WMLES at cruise at about a
  billion cells. From integral length scales (Sillero et al. 2014, as cited)
  they expect the mean velocity to converge first, the Reynolds stresses
  more slowly and wall-pressure fluctuations to need about $0.02\delta$. On
  isotropic CharLES grids at $Re_\tau=1000$ and in two three-dimensional
  boundary layers the mean wall stress, mean velocity and flow direction
  converge once $\Delta/h_{\mathrm{wm}}\lesssim0.3$–0.4, a criterion set by
  the matching height rather than by $\delta$ (§6.1–6.2); the streamwise
  r.m.s. velocity needs about $\Delta^+\approx50$ at $Re_\tau=1000$ (80 % of the
  small-scale-eddy energy, four cells per scale), where "WMLES starts to
  approach WRLES" (§6.2, §7; see [wall-modelled LES](/methods/wall-modelled-les.md)).
- **Near-WRLES resolution in a separated WMLES.** On the
  [Gaussian bump](/benchmarks/gaussian-bump.md) ($Re_L=2\times10^6$, $L$ the
  bump width), [Zhou & Bae (2024)](/sources/zhou-2024-b.md) (§2.2.3, §3.1,
  Table 1) refine isotropic grids from $\Delta_c/L=1.90\times10^{-3}$
  (1.94 M cells) to $2.38\times10^{-4}$ (993 M cells; $\Delta_c$ the cube root
  of the cell volume, page-local), with the incoming boundary layer covered
  by about 5, 9, 18 and 36 cells. The finest grid has 10–30 wall units in
  the attached regions, "comparable to that of the standard WRLES mesh in
  the streamwise and spanwise directions" but an order of magnitude coarser
  wall-normally, and there even WMLES without an SGS model improves
  markedly, with over 150 cells across the separated boundary layer. The
  reference simulation they call DNS (Uzun & Malik, as cited) has a
  characteristic cell size of about $1.10\times10^{-4}L$ at the thickest
  bubble.
- **Resolved fraction in a wall-resolved supersonic LES.** [Wei et al. (2023)](/sources/wei-2023.md)
  (§II E, §III B, Eq. 34, Fig. 6) run a wall-resolved LES of supersonic
  hydrogen film cooling (Mach 2.44) on about $7.4\times10^6$ cells with
  $\Delta x^+=120$, $\Delta z^+=40$, $\Delta y^+<60$ and a first cell at
  $y^+\approx0.6$, and check it by the 80 % resolved-energy criterion of
  Pope, as cited: 99.5 % of the cells resolve more than 80 % of the
  turbulent kinetic energy, the rest lying in the viscous sublayer; the
  velocity spectrum at $y/\delta=0.5$ shows a $-5/3$ range. Mesh
  independence is not shown.

- **Integrated forces at about ten points per boundary layer.** Goc et al.
  (2021) size the [JAXA Standard Model](/benchmarks/jaxa-standard-model.md)
  grids for $\delta_{99}/\Delta\approx10$ at the main-element trailing edge
  ($Re_c=1.96\times10^6$, $Re_\tau\approx5000$) and predict $C_{L,\max}$ within
  five lift counts with 32 M cells; they argue that the estimates of Spalart
  (1997), Choi & Moin (2012) and Slotnick et al. (2014) were too pessimistic for
  integrated forces because they were not tied to particular quantities of
  interest, while Reynolds stresses and wall-pressure fluctuations need more
  resolution (§1, citing Park & Moin 2016). Part of the requirement is
  inviscid: the leading-edge acceleration at high angle of attack (§1, §3.2).
- **Wall pressure at fewer.** Lozano-Durán et al. (2022, §V.E) find $C_p$
  errors below 5 % with 0–1 points per $\delta$.
- **More than 250 M degrees of freedom for the pitching moment of a
  high-lift aircraft.** In the HLPW-4 wall-modelled LES focus group on the
  [NASA CRM high-lift](/benchmarks/nasa-crm-high-lift.md) configuration
  ($Re=5.5\times10^6$ on the mean aerodynamic chord, Mach 0.2),
  [Kiris et al. (2023)](/sources/kiris-2023.md) find that every submission
  that resolves the outboard slat and main-element suction peaks at
  $\alpha=19.57^\circ$ has more than 250 M spatial degrees of freedom, and
  that this resolution is needed to predict pitching moments at high angle
  of attack (Abstract, §IV, Fig. 12). The submitted grids ranged from 3 M
  to 11.2 B (Table 2). They attribute the requirement to inviscid
  curvature-induced acceleration, not to wall-layer resolution (§III, §VI.1a;
  see [boundary-layer-conforming grids](/methods/boundary-layer-conforming-grid.md)).
  This "appears to be somewhat contradictory" to the coarse JAXA-model
  result of Goc et al. (2021) above, which the authors reconcile by the same
  inviscid argument (§VI.1a). Below $10^9$ degrees of freedom they still
  call full-airframe WMLES "coarse-grid simulations", since their spacing
  per unit span is much coarser than that of academic WMLES of
  non-equilibrium boundary layers (§I.1). They add that grid convergence of
  wall-bounded LES in mean-velocity profiles is likely non-monotonic, and
  assess convergence on static pressure only (§I.1a). The high-order
  flux-reconstruction submission (W-047, [hpMusic](/software/hpmusic.md),
  $N=2$, 13 M degrees of freedom) obtained reasonably accurate loads at
  $C_{L,\max}$ but missed the outboard slat-bracket-wake separation (§VI.1a).
- **WMLES at a fixed number of points per $\delta$ across a decade of
  $Re_\tau$.** [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) (§3,
  Table 1) run a Mach 2.28 zero-pressure-gradient boundary layer with about
  12 M points at $Re_\tau\approx700$ to 14 000, with
  $\delta/\Delta x=\delta/\Delta z=25.6$–29.4 (the Kawai–Larsson criterion
  $\delta/\Delta x\gtrsim25$, as cited). In wall units this is
  $\Delta x^+=\Delta z^+$ from 23 to 546, with 56–61 points across $\delta$
  and the 10th point as matching height. The DNS references at
  $Re_\tau\approx715$, 1280 and 2407 need 0.2, 1.4 and 5.6 billion points
  ($\Delta x^+\lesssim10$, $\Delta z^+\lesssim5$, $\Delta y_w^+\lesssim1$).
  The mean velocity, Reynolds shear stress and turbulent-kinetic-energy
  budget match the DNS above the matching height (§4). Two things are
  missed: the Reynolds-number growth of the log-region streamwise stress
  and that of the outer spectral peak. A spanwise cut-off places the
  deficit in scales larger than $0.7\delta$, which the grid nominally
  resolves (§6). A wall-parallel grid $\sqrt2$ finer ($\delta/\Delta x=37.8$)
  begins to show the outer peak, and the authors expect it to "appear more
  clearly as increasing the grid resolution towards that used in the WRLES"
  (App. C). They cite Bose & Park (2018) for the view that the WMLES
  predictability of the outer peak is "highly questionable" (§1, §6.1; see
  [wall-modelled LES](/methods/wall-modelled-les.md)).
- **Mean velocity and separation need more.** The mean-velocity error
  decreases linearly with $\Delta/\delta$ in developed layers and more slowly in
  corners and separation (Lozano-Durán et al. 2022, §V.B); in the Gaussian bump
  separation appears only on the finest of three grids, with the first cell at
  $y^+\sim30$ ([Agrawal et al. 2022](/sources/agrawal-2022.md), §VIII.B).
- **Hybrid methods.** [Haering et al. (2022)](/sources/haering-2022.md)
  (§V.A.1) cite the statement that typical LES needs an unresolved fraction of turbulent
  kinetic energy of at most about 0.1 (after Jiménez & Moser); their
  [active model split](/methods/active-model-split.md) runs channel flow at
  $Re_\tau\approx5200$ with fractions up to 0.4 at the centre and the
  [periodic hill](/benchmarks/periodic-hill.md) on 0.2–0.9 M cells, 14–62
  times fewer than the 13 M-cell wall-resolved LES reference (§V.B).
- **Resolved fraction as a stability condition.** [Jakhar et al. (2026)](/sources/jakhar-2026.md)
  (p. 4) find that LES of forced two-dimensional turbulence with their
  fourth- and sixth-order [gradient models](/methods/gradient-model.md)
  stays stable over long times only when the grid captures more than 80 %
  of the DNS enstrophy, and compare it with the requirement, cited from
  Pope, that three-dimensional LES resolve at least 80 % of the kinetic
  energy; the stability runs are in the Supplemental Material, not in the
  file read. Haering et al.'s cited bound above, an unresolved fraction of
  at most about 0.1, is the stricter of the two cited criteria
  *(compiler check, not in the sources)*.
- **Resolved fraction as a grid check in reacting LES.** [Fureby & Nilsson (2023)](/sources/fureby-2023.md)
  (§6.2) judge three grids of a scramjet combustor, 7.3 M, 24.6 M and 57.8 M
  hexahedra, by the resolved fraction of turbulent kinetic energy, 90 %,
  94 % and 96 %, "rendering all grids appropriate for LES according to"
  Pope "as well as with the more stringent requirements of" Matheou & Chung,
  as cited, without printing either threshold; mean and rms velocity,
  temperature and pressure are similar on the three grids (statistics not
  shown). All three fractions exceed the 80 % attributed to Pope above, and
  the coarsest sits at the 0.1 unresolved fraction cited by Haering et al.
  *(compiler check, not in the sources)*.
- **Hybrid and "very large" eddy simulation of a high-lift airfoil.**
  [Wu et al. (2023)](/sources/wu-2023-b.md) (§1) motivate their hybrid by
  the cost of wall-resolved LES of a three-element airfoil at
  $Re_c=1.23\times10^6$, "2.6 billion grid cells and 6 million CPU hours"
  (Terracol et al., as cited), and by the Choi & Moin estimates. On the
  [30P30N airfoil](/benchmarks/30p30n-high-lift-airfoil.md) at
  $Re=1.71\times10^6$ (basis not stated) their self-adaptive turbulence eddy simulation with
  a linear weighted compact scheme gives $C_L$ within 3 % of the
  experimental mean on 7.2 M, 19 M and 27 M cells (60 or 80 spanwise cells;
  wall units not reported), with mean $C_p$ insensitive to the grid and
  rms values moderately sensitive (§3.2, Table 2). They rename the method
  from "very-large eddy simulation" because it resolves more than 90 % of
  the turbulent kinetic energy, while Pope defines VLES as too coarse to
  resolve 80 % (§2.1.1); the 90 % is asserted from earlier papers and shown
  here only as resolved-against-modelled scatter plots (see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **High order against more elements in wall-modelled implicit LES.**
  [Huang et al. (2022c)](/sources/huang-2022-c.md) (§III A, §III E,
  Table I, Fig. 9) take the spacings $\Delta x\simeq0.087\delta$,
  $\Delta y_1\simeq0.037\delta$, $\Delta z\simeq0.052\delta$ from the WMLES
  review of Larsson et al. (2016), as cited, which on one $12\times6\times10$
  spectral/hp mesh is $\Delta x^+\times\Delta y_1^+\times\Delta z^+=48\times20\times29$
  at $Re_\tau=550$ and $175\times75\times105$ at 2000; the mean velocity
  stays within 5.4 % of DNS. At similar resolution the mesh with fewer
  elements at higher order ("polynomial order" 7 against 6, as printed)
  resolves the fluctuations and shear stress better, and the wall-modelled
  run is "as high as seven times" cheaper than the wall-resolved one at 550
  (§III A; no timings). They cite Choi & Moin for the cost growth of
  wall-resolved LES as motivation (§I).

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
  $\Delta x\approx0.08\delta_0$, $\Delta z=0.05\delta_0$ ($\delta_0=4$ mm their
  reference boundary-layer thickness, page-local) and four cells below
  $h_{\mathrm{wm}}=0.1\delta_0$ for a Mach 3 shock/boundary-layer interaction,
  about 20 M cells for a span of $5\delta_0$ and 200 M for $50\delta_0$.
- **Wall-resolved LES at coarse resolution.** [Prakash et al. (2022)](/sources/prakash-2022.md)
  (§III.B.3, Table 3) run channel flow at $Re_\tau=590$ on meshes with
  $\Delta x^+=78$ and 58, $\Delta z^+=39$ and 29, first off-wall
  $\Delta y^+=1$, and find their optimally clipped gradient model and the
  dynamic mixed model close to DNS on the medium mesh. They argue, after
  Baggett et al. as they cite it, that in anisotropic wall-bounded flows at
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
  they state that $y^+<1$ and "at least 15 or 20 prism layers" are needed.
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
- **Uniform grids without near-wall refinement and an integrated wall
  model.** [Lv et al. (2021)](/sources/lv-2021.md) (§IV A–B 1, Table I) run
  channel WMLES on grids uniform in all three directions: $Re_\tau=2000$ on
  $32^3$, $64^3$ and $128^3$ cells (first-cell heights $y_1^+=125$, 63 and 31),
  $Re_\tau=50\,000$ on $64^3$ ($y_1^+=1.6\times10^3$) and $Re_\tau=180$ on
  $64\times128\times64$ ($y_1^+=2.81$, wall resolved; $y_1$ page-local). The
  mean velocity follows DNS on every grid at $Re_\tau=2000$, and second-order
  statistics approach DNS under refinement. With $y_1=2\delta/n_y$ the printed
  heights are $2Re_\tau/n_y$, i.e. 125, 62.5, 31.25, 1562.5 and 2.8125
  *(compiler check, not in the sources)*. Their wall model adds, by their
  statement, no cost to the LES (see
  [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).
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
- **Very coarse wall-resolved LES rescued by a learned SGS model.**
  Maejima & Kawai (2025, §4.1, §6.1, §7, Tables 1–2) take the
  $(\Delta x^+,\Delta z^+)\approx(72,36)$ channel grid at $Re_\tau\approx1000$
  ($\Delta y^+=0.8$–16, $270\times180\times285$ points, eight times coarser
  than their DNS in $x$ and $z$) as "very coarse-grid LES", where even the
  energetic near-wall eddies are under-resolved and the resolved field
  differs from filtered DNS. With the selective mixed-scale model the mass
  flow rate is over-predicted by 23 %; their
  [super-resolution SGS model](/methods/super-resolution-sgs-model.md) lowers
  this to 10 % and gives mean velocity and total shear stress in good
  agreement with DNS, also at the untrained $Re_\tau\approx2000$ on the same
  wall-unit grid. They motivate coarse grids by the cost of resolved LES,
  citing an airfoil LES at $Re_c=10^7$ on Fugaku that needed about
  $38\times10^9$ points (Tamaki & Kawai 2023, as cited; §1).
- **Spectral-element WMLES: elements per thickness.** Mukha et al. (2025,
  §III.A–III.B, §IV.A, Tables I, V, Fig. 12) run channel flow at
  $Re_\tau\approx8000$ at $N=7$ on $16\times4\times12$, $32\times8\times24$ and
  $64\times16\times48$ elements over $8\delta\times2\delta\times6\delta$ (2, 4
  and 8 elements per $\delta$; $0.39$, $3.14$ and $25.17$ million nodes): the
  mean velocity is within 1 % above $0.1\delta$ on all three, while
  second-order statistics need "at least 4 elements across the boundary
  layer in all three spatial directions". For a developing flat-plate
  boundary layer, whose $\delta_{99}$ grows about eight times over their
  domain, a structured mesh cannot keep the spanwise size proportional to
  $\delta_{99}$, and four elements per inlet $\delta_{99}$ are already about
  $10\delta_\nu$, "essentially WRLES" in inner units, so WMLES must coarsen
  with $x$ and $y$; their meshes of $519\times15\times28$, 56 and 112
  elements (1, 2 and 4 spanwise elements per inlet $\delta_{99}$; 75, 149 and
  299 million nodes) give $C_f$ within 2 % of wall-resolved LES on the
  finest. See [wall-modelled LES](/methods/wall-modelled-les.md).
- **Span of a nominally two-dimensional geometry.** Baldan & Guardone (2025,
  §1.1, §2.1, Tables 1–2, Figs. 3–6) run wall-resolved LES of a NACA 0012
  in deep dynamic stall ($Re_c=1.35\times10^5$, pitching about
  $10^\circ\pm15^\circ$) on spans of $0.2c$, $0.4c$, $0.8c$ and $1.2c$ with the
  same spanwise spacing $10^{-3}c$, from 62.7 M to 374.7 M nodes, the number
  of points "respecting the LES requirements" of Choi & Moin (2012) as they
  cite it. The upstroke with attached flow is insensitive to the span
  (lift within 0.05 up to about $22^\circ$), but after the dynamic-stall
  vortex forms the two short spans force a quasi-two-dimensional vortex and
  spurious lift peaks; they conclude that a span of at least one chord is
  required for the downstroke, against the 5–20 % of chord common in the
  literature; the $1.2c$ grid has six times the nodes of the $0.2c$ one
  (Table 2). At $10^\circ$ in the downstroke the $1.2c$ span is completely
  stalled while the $0.8c$ span still shows oscillatory wake patterns
  (§2.1, Fig. 4); no span beyond $1.2c$ is run. See [NACA 0012](/benchmarks/naca-0012-airfoil.md).
- **Coarse DG "DNS" of a compressible channel.** [Ranjbar et al. (2026)](/sources/ranjbar-2026.md)
  (§III.C, Table III) run channel flow at $Re_\tau=395$ ($M=0.3$) in
  [HORSES3D](/software/horses3d.md) on $14\times12\times16$ elements of
  degree $N=6$, 921 984 solution points with six inside $y^+=10$, elements
  clustered at the walls and uniform in $x$ and $z$, a resolution they place
  "within the suitable range for LES without wall modeling, as recommended
  by Choi and Moin (2012)"; they call it a coarse DNS and use it to test
  [explicit modal filtering](/methods/explicit-modal-filtering.md).
  $14\cdot12\cdot16\cdot7^3=921\,984$ confirms $(N+1)^3$ points per element
  *(compiler check, not in the sources)*.
- **Training grids of a learned wall model.** [Lozano-Durán & Bae (2023)](/sources/lozanoduran-2023.md)
  (§2.6) train their wall model on WMLES with isotropic grids $\Delta=\delta/n$,
  $n=5$ to 380 ($\delta$ the channel half-height, $n$ page-local), and below
  $\delta/380$ on DNS data so that the model converges to no slip; their NASA
  CRM-HL WMLES uses 30 M points with 0–20 points per boundary-layer
  thickness (§4.7).
- **Wall-modelled against wall-resolved LES of a shock interaction.**
  De Vanna et al. (2022, §4.1, Table 1) run the Mach 2.28 oblique
  [shock/boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
  ($Re_\tau=700$ at the inflow, domain $90\delta_r\times10\delta_r\times6\delta_r$, $\delta_r$ the inflow 99 % thickness)
  on uniform WMLES grids of $480\times96\times80$, $720\times128\times120$ and
  $960\times128\times160$ points ($\Delta x^+=140$, 104, 82; first point at
  $\Delta y^+_w=39$, 32, 34; $\Delta z^+=56$, 42, 33 at $x/\delta_r=40$) and a
  wall-resolved LES of $2800\times200\times440$ points ($\Delta x^+=28$,
  $\Delta y^+_w=0.5$, $\Delta z^+=12$). The WMLES grids hold 3.7 M, 11.1 M and
  19.7 M points against 246 M, so the finest WMLES uses about 8 % of the
  wall-resolved count *(compiler check, not in the sources)*. Both kinds
  reproduce the incoming boundary layer, but no WMLES grid reaches the
  wall-resolved interaction length (5.0–7.0 against 3.3 $\delta_r$; see
  [wall-modelled LES](/methods/wall-modelled-les.md)). Their wall-model
  switch is itself a resolution criterion: the model is turned off where
  $\Delta x^+_w<40$, $\Delta y^+_w<3$ and $\Delta z^+_w<15$ hold with the
  resolved wall stress (§3.2, Eq. 9), within the wall-resolved ranges of
  the table above.
- **Hypersonic WMLES on an immersed boundary.** Van Noordt et al. (2022,
  §3) run channel flow at $Re_\tau=5200$ on 1.9 M and 8.9 M cells
  ($\Delta x^+\times\Delta y^+\times\Delta z^+=270\times68\times270$ and
  $173.3\times40.6\times156$, as printed, Table 5; see
  [log-layer mismatch](/definitions/log-layer-mismatch.md)), a Mach 6
  transitional interaction on 2.1 M, 4.6 M and 16 M cells
  ($295\times65\times171$ to $43\times35\times90$, Table 10), and a Mach 7.2
  compression ramp on 11 M, 50 M and 89 M cells
  ($160\times80\times190$ to $116\times32\times171$, Table 15). The coarsest
  ramp grid needs less than 5 % of the cells of the reference DNS (96 M in
  the ramp domain plus 138 M upstream) "considering only the spatial
  requirement" (§3.4); $11/234=4.7$ % *(compiler check, not in the
  sources)*.

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

Kiris et al. (2023, §VI.4), from cost numbers reported by participants,
put most best-practice WMLES of the CRM high-lift configuration at about
5–10 times the cost of a representative steady RANS at $Re=5.5\times10^6$.
This assumes runs long enough for statistically stationary loads, which is
ambiguous at the angles with large-scale separation, where steady RANS
fails to converge or is "dramatically inaccurate". Two participants (W-021,
W-047) report substantial wall-time reductions on GPUs. The authors withhold
the detailed costs and state that no WMLES cost scaling with Reynolds
number exists for such a configuration. They also argue for explicit time
stepping (§II.3): eddy decorrelation times in the inertial range scale as
$k^{-2/3}$ and acoustic CFL limits as $k^{-1}$, with $k$ the grid Nyquist
wavenumber. Explicit schemes thus suit near-unity-aspect-ratio grids for
compressible solvers at Mach $\ge0.2$, and the implicit codes used time
steps only "about 10×" larger (§VI.1c; see Qualifications). The thin
geometric features (trailing edges about 2.5 mm thick on a 7 m chord at
full scale) dominate the cost of the explicit codes (§VI.1c).

For hybrid RANS/LES of a ship hull at 10° drift (DDES-SST), Mozaffari et al.
(2022, §5.1) report about 160 000 CPU-hours on a 154 M cell adapted mesh
against about 250 000 on a 163 M cell hand-designed mesh, and for steady RANS
about 16 000 (47 M cells) against 30 000 (163 M); the runs used different
processor counts and the hand-designed DDES included extra analysis steps, so
"the adaptation probably saves some time, but not a lot". Training the
reinforcement-learning wall model of Bae & Koumoutsakos (2022, p. 8) costs
$O(10^3)$ CPU-hours, against an estimated $O(10^7)$ for the DNS data a
supervised model would need at $Re_\tau=4200$.

Yeung et al. (2025, §1) report 13 s per time step for the $32\,768^3$ DNS
on 44 % of Frontier at best, about 1000 steps per Kolmogorov time and about
300 Kolmogorov times per large-eddy time at $Re_\lambda\approx2500$, so a run
of ten large-eddy times "would require two years or more of virtually
non-stop computing"; this is why the record grid is run only for a few
Kolmogorov times (see Qualifications).

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

- **WMLES cost exponent: $Re_c^{4/3}$ or $Re^{1.1}$.** The two exponents
  rest on different assumptions, stated by each source. Goc et al. (2021, §4) extrapolate their own JAXA runs to
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
  smallest cell it is $t_{\mathrm{run}}\,Re\,(Re_\Delta^{\min})^{-1}$, set by how the
  leading-edge resolution is scaled with Reynolds number. The exponents also
  refer to different configurations (a high-lift aircraft at chord Reynolds
  number; a flat-plate boundary layer at plate-length Reynolds number).
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
- **Cited exponents.** The WRLES cost exponents in this page are
  cited, not derived, by the sources: $Re^{2.7}$ by Griffin et al. (2023)
  after Yang & Griffin (2021), $Re^{2.5}$ by Morsbach et al. (2024) after Choi
  & Moin (2012). The two rest on different underlying works whose
  assumptions the citing sources do not state; no source of this bundle
  derives either. The near-wall resolution costs $Re^3$ (DNS) and
  $Re^{1.8}$ (LES) quoted by Brenner et al. (2022, §1) after Xiao & Jenny
  are a third cited pair; whether they count grid points or points
  times steps is not stated, so they are not compared with the exponents
  above.
- Zhao et al. (2023a, Table 6) print $\Delta z^+=8.33$ at $Re_\tau=180$ with
  $L_z=\pi$ and 64 cells, where $\pi\cdot180/64\approx8.84$; their printed
  $\Delta x^+=17.66$ and the $Re_\tau=395$ values are reproduced by the same
  arithmetic *(compiler check, not in the sources)*.
- **Node counts of Mukha et al. (2025).** Both node tables are captioned
  "total number of nodes", but the channel values equal $(N+1)^3=512$ nodes
  per element times the element count ($16\cdot4\cdot12\cdot512=393\,216$),
  i.e. element-local nodes with duplicates, while the boundary-layer values
  equal $N^3=343$ per element ($519\cdot15\cdot28\cdot343\approx74.8\times10^6$),
  about the unique nodes *(compiler check, not in the sources)*; the two
  tables are not on the same count. Locators refer to the arXiv v1 read.
- **Cost of Yeung et al. (2025).** Their printed figures, 3000 Kolmogorov
  times of 1000 steps at 13 s, give about $3.9\times10^7$ s, 1.2 years,
  against the "two years or more" printed; the 13 s is a best timing on part
  of the machine, and overheads are not stated *(compiler check, not in the
  sources)*.
- **Grid of Baldan & Guardone (2025).** Their Table 1 lists 311 622
  quadrilaterals in the two-dimensional grid of $934\times334$ nodes, whereas
  $933\times333=310\,689$ cells reproduce the hexahedron counts of their
  Table 2 (62.1 M for 200 layers) *(compiler check, not in the sources)*.
  They quote the spans of the literature as 5–20 % of chord in the
  introduction and as 0.1–0.2 in the conclusions. Locators refer to the
  arXiv v2 preprint read.
- Cai et al. (2022, §III) call $\lambda_H$ "the Taylor scale describing the
  integral motions in the wake"; the estimate is printed as such.
- **Colours of Bose & Park's Fig. 5.** The caption assigns green to
  Chapman's estimate with $n_xn_yn_z=10^3$ and blue to $20^3$; the labels
  inside the figure assign blue to $10^3$ and green to $20^3$. The text
  ("require $n_xn_yn_z\gtrsim20^3$ … increase the cost prefactor") does not
  depend on which assignment is meant.
- Heinz (2020, §3.1) writes, citing the literature, that an adequate
  resolution of the boundary-layer thickness makes WM-LES "orders of
  magnitude more expensive than original DES"; no estimate is printed.
- **Cost factor of Kokkinakis et al. (2023, §III B 2).** They state that
  refining the $x$ and $z$ cells to a third costs "almost an order of
  magnitude" and that the full 152 mm width instead of 33 mm adds "$\sim4.6$
  times", and conclude "$\sim175$ times greater compared to the medium 2
  mesh". A third of the cell size in $x$ and $z$ is $3\times3=9$ times the
  cells, $152/33=4.61$, and $9\times4.6\approx41$ *(compiler check, not in
  the sources)*. Their Table III lists the medium 2 mesh with the full
  152 mm span and the coarse, medium 1 and fine meshes with 33 mm.
- **Time steps of Kiris et al. (2023).** §VI.1c states that the implicit
  codes used time steps "only about 10× larger" than the explicit ones. In
  Table 2 the explicit steps are $2.9\times10^{-5}$–$5.7\times10^{-5}$ and
  the implicit ones $5.8\times10^{-4}$ (W-031), $5\times10^{-4}$ (W-050) and
  $9.7\times10^{-5}$ (W-047), besides $2.1\times10^{-2}$ for the inviscid
  W-030, ratios of about 9–20 for the first two and
  1.7–3.3 for W-047 *(compiler check, not in the sources)*. The same paper
  counts six explicit and three implicit participants in §II.3, while its
  Table 1 lists five explicit (one with implicit viscous terms) and four
  implicit time integrations. It writes the 250 M threshold as degrees of
  freedom (Abstract), grid cells (§VI.1a) and points (§IV), which differ
  for the $N=2$ flux-reconstruction and nodal finite-element submissions.

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
- [Yeung et al. (2025)](/sources/yeung-2025.md) — §1; §2.2, Table 1; §5.
- [Maejima & Kawai (2025)](/sources/maejima-2025.md) — §1; §4.1, Tables 1–2, Fig. 5; §6.1; §7; App. B.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §III.A–III.B, Table I; §IV.A–IV.B, Table V, Fig. 12 (arXiv v1).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — §1.1, Tables 1–2; §2.1, Figs. 3–7; §3 (arXiv v2).
- [Elzaabalawy et al. (2023)](/sources/elzaabalawy-2023.md) — §1, Fig. 1.
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §1.
- [Jakhar et al. (2026)](/sources/jakhar-2026.md) — p. 4 (arXiv v3).
- [Ranjbar et al. (2026)](/sources/ranjbar-2026.md) — §III.C, Table III (arXiv v1).
- [Bose & Park (2018)](/sources/bose-2018.md) — §1, Eqs. (1)–(2), Fig. 1; §3, Fig. 5; §4.1.
- [Sandberg & Michelassi (2022)](/sources/sandberg-2022.md) — §2.1.
- [Heinz (2020)](/sources/heinz-2020.md) — §1; §3.1.
- [Lv et al. (2021)](/sources/lv-2021.md) — §IV A–B 1, Table I; §II B 4.
- [Brenner et al. (2022)](/sources/brenner-2022.md) — §1.
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §1; §3.2, Eq. (9); §4.1, Table 1.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §1; §3.1, Table 5; §3.3, Table 10; §3.4, Table 15.
- [Fureby & Nilsson (2023)](/sources/fureby-2023.md) — §6.2 (resolved-energy grid check).
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1; §2.1.1; §3.2, Table 2.
- [Huang et al. (2022c)](/sources/huang-2022-c.md) — §I; §III A, Table I; §III E, Fig. 9.
- [Kiris et al. (2023)](/sources/kiris-2023.md) — Abstract; §I.1; §II.3; Tables 1–2; §III, Fig. 6; §IV, Fig. 12; §VI.1a, §VI.1c, §VI.4.
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §1; §3, Table 1; §4; §6; App. C, Table 2.
- [Kokkinakis et al. (2023)](/sources/kokkinakis-2023.md) — §III B 2, Table III; §IV A, Fig. 4.
- [Hu et al. (2024)](/sources/hu-2024.md) — §2, Eqs. (1)–(4), Fig. 1; §6.1–6.2, Fig. 14; §7.
- [Kim & Leonard (2024)](/sources/kim-2024-b.md) — §2.1–2.2; §5 (historical estimates and computing growth).
- [Zhou & Bae (2024)](/sources/zhou-2024-b.md) — §2.2.3, Table 1; §3.1.
- [Wei et al. (2023)](/sources/wei-2023.md) — §II E; §III B, Eq. (34), Figs. 5–6.
- [Wu et al. (2024)](/sources/wu-2024.md) — §1 (Choi & Moin cited; passing).
