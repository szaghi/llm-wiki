---
type: Method
title: "Detached-eddy simulation and its delayed and zonal forms"
description: "The single-model hybrid RANS/LES in which a RANS model's length scale is capped by a grid length so that the model acts as a subgrid model away from walls; the DES switch and ambiguous grids, the DDES shielding function, IDDES, ZDES modes, grid lengths and the shear-layer-adapted length, calibration with the numerical scheme, transitional DDES, and applications."
status: established
aliases: [DES, DDES, delayed detached-eddy simulation, IDDES, improved delayed DES, ZDES, zonal detached-eddy simulation, DDES-SST, SST-IDDES, SA-DDES, ZDES mode 2, ZDES mode 0+1, shear-layer-adapted length scale, grey area, DDES-γ, transitional DDES]
tags: [des, hybrid-rans-les, rans, les, turbomachinery, mesh-adaptation]
timestamp: 2026-10-26T15:50:00Z
---

# Detached-eddy simulation and its delayed and zonal forms

Detached-eddy simulation (DES) is a [hybrid RANS/LES](/definitions/hybrid-rans-les.md)
method that uses a single transport model in two regimes: near walls the
model runs as a RANS closure, and away from them a length built from the
grid replaces the RANS length scale, so that the same equation acts as a
subgrid-scale model and the large eddies are resolved. In the
[Spalart–Allmaras](/methods/spalart-allmaras-model.md) form the wall distance
$d$ in the destruction term is replaced by a hybrid length (page-local)

$$d_{\mathrm{DES}}=\min\big(d,\;C_{\mathrm{DES}}\Delta\big),$$

with $\Delta$ a grid length whose definition differs between the variants
(see the table below) and $C_{\mathrm{DES}}$ a model constant, as written by
Basile et al. (2023) for the DES zones of their zonal model
([Basile et al. (2023)](/sources/basile-2023.md), §2.2, Eq. 6).
Haering et al. (2022) call DES "the most ubiquitous HRL approach" and class
it with the single-model hybrids that switch internally between RANS-like
and LES-like operation
([Haering et al. (2022)](/sources/haering-2022.md), §I). Page-local
symbols: $d_{\mathrm{DES}}$ the hybrid length, $l_{\mathrm{RANS}}$ and $l_{\mathrm{LES}}$ the RANS and LES length scales, $\Delta_{\max}=\max(\Delta x,\Delta y,\Delta z)$
and $\Delta_{\mathrm{vol}}=(\Delta x\Delta y\Delta z)^{1/3}$ (the cube root of
the cell volume), $r_d$ and $f_d$ the DDES shielding parameter and function.

## The DES switch and its failure on ambiguous grids

As recalled by Basile et al. (2023, §1), the original DES is non-zonal: a
mesh-size sensor switches the model from RANS to LES automatically. On
"ambiguous" meshes, whose wall-parallel spacing is fine enough to activate
the switch but too coarse to resolve boundary-layer turbulence, the switch
occurs inside the attached boundary layer, where the resolved fluctuations
do not make up for the modelled Reynolds stress that is lost. The extreme
case is *grid-induced separation*: a mesh too fine in the longitudinal
direction lets DES lower the RANS viscosity and the boundary layer
separates for numerical reasons. Haering et al. (2022) generalize the
mechanism as modelled-stress depletion of every method that generates
resolved turbulence passively (§II A; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[log-layer mismatch](/definitions/log-layer-mismatch.md)).

Delassaux et al. (2023) recall the same chain with its names: grid-induced
separation (GIS, Menter & Kuntz) was renamed modelled-stress depletion (MSD)
by Spalart et al., because the LES mode entering the upper boundary layer
lowers the eddy viscosity and transfers modelled stress to a resolved
stress the grid cannot sustain; "In reality, GIS is a consequence of MSD".
The *grey area* is the RANS-to-LES transition region with an initial lack
of resolved turbulence ([Delassaux et al. (2023)](/sources/delassaux-2023.md),
§4.1.3; HAL author manuscript). As a grid rule they keep the wall-parallel
spacing $\Delta_{\max}$ above the boundary-layer thickness $\delta$ ("Menter's
criterion"); with Menter's ratio $r=\Delta_{\max}/\delta$, they report, the
grid-refinement impact is delayed to $r<0.2$ in DDES against $r<1$ in DES
(§4.1.3, §4.4). On a full-scale car they deliberately coarsen the flat-area
surface mesh to 10 mm ($\Delta x^+\approx600$ on the roof) for this reason,
and show GIS on a rounded separation line: a 3 mm surface mesh there is
"too fine and leads to GIS", and 6 mm is advised (§4.4, §7.3, Figs. 8, 21).

## Delayed DES: the shielding function

Delayed DES (DDES) detects the boundary layer with a sensor built from the
velocity gradients and the viscosity and keeps it in RANS mode (Basile et al.
2023, §1). François et al. (2022) print the shielding function in the form
used by zonal DES mode 2, translated to registry notation:

$$r_d=\frac{\nu+\tilde\nu}{\sqrt{\partial_ju_i\,\partial_iu_j}\;\kappa^2d^2},\qquad f_d=1-\tanh(8r_d)^3,$$

with $\tilde\nu$ the Spalart–Allmaras working variable and $\kappa$ the von
Kármán constant, whose value they do not print
([François et al. (2022)](/sources/francois-2022.md), §3.1, p. 5). According to
the paper $r_d$ is 1 in the log layer and vanishes at the boundary-layer edge,
so $f_d=0$ in the boundary layer (RANS) and $f_d=1$ outside (LES). The
classic DDES of Spalart et al. evaluates $r_d$ with $\nu_t$ instead of
$\tilde\nu$ (footnote 2). Yan et al. (2022) recall the same function as
$f_d=1-\tanh\big((8r_d)^3\big)$, "initially proposed for detached eddy
simulations", and use a modification $1-\tanh(r_d^{1/2})$ as an input
feature of their learned SA correction, without defining $r_d$
([Yan et al. (2022)](/sources/yan-2022.md), §2.3; see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).

Carlsson et al. (2023) write DDES for any host model through its length
scale,

$$l_{\mathrm{DDES}}=l_{\mathrm{RANS}}-f_d\max\big(0,\,l_{\mathrm{RANS}}-l_{\mathrm{LES}}\big),\qquad l_{\mathrm{LES}}=C_{\mathrm{DES}}\Psi\Delta,$$

with $\Psi$ a low-Reynolds-number correction that avoids an unphysical
damping in LES regions (page-local; $\Psi=1$ for SST) and $C_{\mathrm{DES}}$ "code
dependent"; the RANS model becomes hybrid by replacing $l_{\mathrm{RANS}}$
with $l_{\mathrm{DDES}}$. They use the SA and SST hosts, with $\Delta=\Delta_{\max}$
taken in their edge-based solver as the longest edge of the dual control
volume ([Carlsson et al. (2023)](/sources/carlsson-2023.md), §3, Eqs. 16–17).
For SA, $l_{\mathrm{RANS}}=d$ and with $f_d=1$ the form reduces to the
$d_{\mathrm{DES}}$ above *(compiler check, not in the sources)*.

Delassaux et al. (2023, §4.1.3, Eqs. 6–11) print the SST host in ANSYS
Fluent. The destruction of the $k$-equation becomes

$$\rho\beta^*k\omega\;\to\;\rho\beta^*\frac{k^{3/2}}{l_{\mathrm{DES}}},\qquad l_{\mathrm{DES}}=\min(l_{\mathrm{RANS}},l_{\mathrm{LES}}),\quad l_{\mathrm{RANS}}=\frac{\sqrt k}{\beta^*\omega},\quad l_{\mathrm{LES}}=C_{\mathrm{DES}}\Delta_{\max},$$

with $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$, the inner and outer constants
that Carlsson et al. also quote. The delayed form uses the same
$l_{\mathrm{DDES}}$ as Carlsson et al. and

$$f_d=1-\tanh\big[(C_{d1}r_d)^{C_{d2}}\big],\qquad C_{d1}=20,\quad C_{d2}=3,$$

the SST values of Gritskevich et al. "to ensure a fair protection of
boundary layer"; $r_d$, "the ratio of a model length scale to the wall
distance", is not printed. Raising $C_{d1}$ to 30 increases the shielding,
as their Ahmed-body tests showed, and is "advised for this case" (§4.4).
They state, without derivation, that under local equilibrium the DDES
subgrid model reduces to the Smagorinsky–Lilly model (§4.1.3; see
[Smagorinsky model](/methods/smagorinsky-model.md)).

Möller et al. (2024) print the SST-DDES of the DLR solver
[TRACE](/software/trace.md) with the destruction
$\rho k^{3/2}/l_{\mathrm{DDES}}$, the $l_{\mathrm{DDES}}$ of Carlsson et al.,
$l_{\mathrm{RANS}}=\sqrt k/(\beta^*\omega)$, $l_{\mathrm{LES}}=C_{\mathrm{DES}}\Delta_{\mathrm{SLA}}$
(the shear-layer-adapted length below) with $C_{\mathrm{DES}}=0.65$, and the
shielding function with $C_{d1}=20$, $C_{d2}=3$ and
$$r_d=\frac{\nu_t+\nu}{\sqrt{\partial_ju_i\,\partial_ju_i}\;\kappa^2d^2},$$
in kinematic form; $\kappa$, "the Kármán constant", has no printed value
([Möller et al. (2024)](/sources/moller-2024.md), §II.B.1, Eqs. 17–21;
accepted manuscript). They verified the calibration of $C_{\mathrm{DES}}$ in
their code on decaying isotropic turbulence, without showing it. They read
$f_d$ as an "enabler" of LES mode, not an activator: LES mode needs both
$l_{\mathrm{RANS}}>C_{\mathrm{DES}}\Delta$ and $f_d\neq0$, and they monitor the
mode by the ratio $l_{\mathrm{RANS}}/l_{\mathrm{DDES}}$, one in RANS regions and
above one in LES regions (page-local; §II.B.1, Eq. 22).

Wu et al. (2025) reuse the shielding function outside DES, as a
boundary-layer mask for a field-inversion correction of SST: they print
$f_d=1-\tanh\big[(8r_d)^3\big]$, with $r_d$ the kinematic form above and
$\kappa=0.41$, and state that it is 0 inside the boundary layer and 1
outside ([Wu et al. (2025)](/sources/wu-2025.md), §2.1, Eqs. 5–6, Fig. 2;
authors' manuscript; see
[field inversion and machine learning](/methods/field-inversion-machine-learning.md)).
François et al. instead print $\sqrt{\partial_ju_i\,\partial_iu_j}$ under the
root and $\tilde\nu$ in place of $\nu_t$ (above); the two differ by the index
order under the root and by the eddy-viscosity variable, conventions none
of the sources discusses.

Haering et al. (2022) count the delaying function of DDES among the ad hoc
unified switches "tuned per flow", which make such methods possibly not
predictive in general (§I). In the AIAA Third High-Lift Prediction Workshop
DDES was among the few unsteady techniques submitted next to steady RANS
([Goc et al. (2021)](/sources/goc-2021.md), §1).

**Improved DDES** (IDDES) and an SST-based DDES ("DDES-SST") are the hybrid
models of the ISIS-CFD solver used by Mozaffari et al. (2022), built on the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md); the paper prints no
equation of either ([Mozaffari et al. (2022)](/sources/mozaffari-2022.md),
§2, §4.1, §5).

Carlsson et al. (2023, §3, Eqs. 18–19) print the IDDES blending of Shur et
al.,

$$l_{\mathrm{IDDES}}=\hat f_d(1+f_e)\,l_{\mathrm{RANS}}+(1-\hat f_d)\,l_{\mathrm{LES}},\qquad
\Delta_{dw}=\min\big(\max[C_{dw}d,\;C_{dw}\Delta_{\max},\;\Delta_{wn}],\;\Delta\big),$$

with $\hat f_d$ (page-local; the source's $\tilde f_d$) blending a DDES
branch, meant for inflow without turbulent content, and a wall-modelled-LES
branch, meant for turbulent inflow on grids fine enough to resolve the
boundary-layer eddies; $f_e$ raises the RANS length near the interface to
reduce [log-layer mismatch](/definitions/log-layer-mismatch.md); $\Delta_{dw}$
replaces $\Delta$ in $l_{\mathrm{LES}}$ to give the right log-layer behaviour
"without the need to alter the value of the modeling constant"; $\Delta_{wn}$ is
the wall-normal cell size, $C_{dw}=0.15$ (page-local names). With this
IDDES on SST, channel flow at $M_b=0.15$ ($Re_\tau=395$ to 18 000) and
$M_b=1.5$ ($Re_\tau=500$ to 5000) on wall-modelled-LES grids
($\Delta x^+$ up to about 1800 at $Re_\tau=18\,000$) agrees with DNS and
Reichardt's law once the scheme's dissipation is low enough (§4.3, Table 2,
Figs. 4–6; see [hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[turbulent channel flow](/benchmarks/turbulent-channel-flow.md)).

**SST-DDES and SST-IDDES in a lattice Boltzmann solver.** Mozaffari et al.
(2024) print the SST hybrids they implement in
[ProLB](/software/prolb.md) as multipliers of the $k$-destruction,
$\beta^*\omega k\to\beta^*\omega k\,F$ with $F=l_{\mathrm{RANS}}/l_{\mathrm{DDES}}$ or
$l_{\mathrm{RANS}}/l_{\mathrm{IDDES}}$, the $l_{\mathrm{DDES}}$ of Carlsson et al. and
the IDDES blending above
([Mozaffari et al. (2024)](/sources/mozaffari-2024.md), §2.3, Eqs. 26–32;
HAL accepted manuscript). Their shielding function is

$$f_d=1-\tanh\big[(C_{d1}r_d)^{C_{d2}}\big],\qquad r_d=\frac{\nu_t+\nu}{\kappa^2d^2\sqrt{\tfrac12(S^2+\Omega^2)}},\qquad C_{d1}=20,\ C_{d2}=3,\ \kappa=0.41,$$

with $S$ and $\Omega$ the strain and vorticity magnitudes (normalization
not printed), and $l_{\mathrm{LES}}=C_{\mathrm{DES}}h_{\max}$, $h_{\max}$ the
largest cell edge (equal to the cell size on the cubic lattice cells) and
$C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$, the values Delassaux et al. use.
$l_{\mathrm{RANS}}$, $\hat f_d$, $f_e$ and the IDDES grid length are not
printed ("can be found in" Gritskevich et al.). Beside IDDES they test
Heinz's continuous eddy simulation, whose dissipation multiplier varies
continuously with a resolution ratio instead of switching (see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md)). In their runs the
RANS–LES transition is thin with IDDES and smooth with continuous eddy
simulation (§3.2, Fig. 11).

## Transitional DDES

Möller et al. (2024) couple SST-DDES to the one-equation intermittency
model of Menter et al. (2015) (see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)),
a model they introduced in earlier work and call DDES-$\gamma$
([Möller et al. (2024)](/sources/moller-2024.md), §II.B.3, Eqs. 24–25, 27;
accepted manuscript). With $\gamma$ the intermittency (registry, transition
pages) and $P_k$ the production of the modelled $k$:

$$P_k\to\gamma P_k,\qquad \rho\frac{k^{3/2}}{l_{\mathrm{DDES}}}\to\max(0.1,\gamma)\,\rho\frac{k^{3/2}}{l_{\mathrm{DDES}}},$$

and the extra production that the RANS $\gamma$ model adds in separated
shear layers is removed, which "needs to be eliminated for a coupled
DDES-$\gamma$ model", as their earlier paper showed. Their introduction
lists other couplings of DES with transition models, among them
$\gamma$-$Re_\theta$ and $k$-$k_L$-$\omega$ hosts (§I).

**Mode bookkeeping in transitional flow.** In a laminar region $\gamma=0$
removes the production and leaves 10% of the destruction, so the modelled
$k$ and $l_{\mathrm{RANS}}$ stay near zero and the length-scale test reports
RANS mode where the model behaves as "more a laminar mode", even as an
implicit LES; LES mode there would need extremely fine meshes (§II.D,
Fig. 1, p. 10). The dynamic central/upwind flux blending of Travin et al.,
designed for the fully turbulent RANS/LES distinction, loses its meaning
(§II.D; see [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).

**V103 compressor cascade** ($Re=138\,500$ on the axial chord $c_{ax}$,
page-local, $M=0.1$,
inflow $Tu=3.25\%$, span $0.1c_{ax}$; separation-induced transition on the
suction side, bypass transition on the pressure side; DNS of Zaki et al.,
own WALE LES on 10.9 million cells; §III; see
[compressor cascades](/benchmarks/compressor-cascade.md)):

- *Mesh.* Coarse, medium and fine DDES meshes of 0.68, 1.08 and 4.32
  million cells, 40 spanwise cells, $y^+<1$; the integral total-pressure
  loss converges towards the LES with refinement, and the medium mesh,
  comparable to the 1.47 million cells of Yin & Durbin's DDES, is used
  (§III.A, Tables 2–3, Fig. 3).
- *Baseline.* Fully turbulent DDES misses the suction-side
  [laminar separation bubble](/definitions/laminar-separation-bubble.md)
  and "transitions" the pressure side just behind the leading edge;
  DDES-$\gamma$ captures the bubble, but on the pressure side follows RANS
  with the $\gamma$ model, since the attached layer stays in RANS mode
  without resolved content (§III.B.1, Figs. 5–10, §IV). On the ERCOFTAC
  T3C5 plate it gives results identical to RANS-$\gamma$, not shown
  (§II.F; see [ERCOFTAC T3 flat plates](/benchmarks/ercoftac-t3-flat-plate.md)).
- *Free-stream decay.* Without inflow turbulence both DDES variants lose
  the modelled free-stream turbulence intensity rapidly ahead of the
  leading edge, unlike DNS, LES and RANS: $f_d=1$ in the free stream and
  the very small $\Delta_{\mathrm{SLA}}$ there "spuriously" enable the LES-mode
  destruction (§III.B.1, Figs. 11–12).
- *Synthetic inflow turbulence.* The generator of Shur et al. restores the
  free-stream intensity, slightly improves the bubble, and moves bypass
  transition onto resolved scales ($x=0.3$–$0.55c_{ax}$, against modelled
  $k$ at $0.5$–$0.65c_{ax}$ without it), yet the pressure-side $C_f$ barely
  changes because $f_d=0$ near the wall enforces RANS mode; hence, in the
  authors' words, assessing transition by surface values such as the skin
  friction alone "may lead to wrong conclusions" (§III.B.2, Figs. 13–18).
  The inlet $\omega=\sqrt k/(\beta^*L)$, with $L$ the inlet turbulent length
  scale, uses $L=0.055c_{ax}$ with the generator and $0.003c_{ax}$ without
  (Eq. 28; see
  [inflow turbulence generation](/methods/inflow-turbulence-generation.md)).
  The authors suggest that with resolved inflow scales the near-wall mesh
  is fine enough that shielding "might not be required" (§III.B.2, p. 21).
- *Flux blending.* The dynamic blending is fully upwind ($\sigma_b\approx1$,
  page-local upwind fraction of the Roe flux) in both boundary layers and
  damps the resolved scales; a constant upwind fraction of 0% oscillates and
  suppresses the bubble, 25% (Yin & Durbin's value) damps the synthetic
  turbulence and overpredicts the bubble, and 5% predicts both transitions
  best, agreeing with Yin & Durbin's DDES and closer to the DNS on the
  pressure side (§III.B.3, Figs. 19–22). The authors caution that bypass
  transition then relies on resolved scales, so the model may act "more
  like an LES model", and that 5% is a further adjustable parameter that
  may need re-tuning for other cases or meshes (pp. 25–26; see
  [numerical dissipation](/properties/numerical-dissipation.md)).

## Zonal DES

Zonal detached-eddy simulation (ZDES, Deck) lets the user assign to each
part of the domain either URANS or one of several ZDES *modes*. As recalled
by the two sources that use it:

- **mode 0** is RANS; **mode 1** is meant for separation fixed by the
  geometry; modes 1 and 3 need user-defined zones, mode 2 detects the
  regions automatically with the shielding function (Basile et al. 2023, §1,
  §2.2);
- **mode 2** solves the boundary layer in URANS and the rest in LES, with the
  DDES $f_d$ computed from $\tilde\nu$; it differs from DDES mainly in the
  length scale, which switches with $f_d$ (François et al. 2022, §3.1, p. 6);
  Deck's comparisons on a mixing layer, a backward-facing step and an
  airfoil, as recalled by François et al., show that it keeps the
  attached-boundary-layer treatment of DDES and shortens the delay in the
  formation of instabilities;
- ZDES aims at a faster decay of the eddy viscosity in LES mode than DES and
  DDES (Basile et al. 2023, §2.2), and its user zoning (RANS forced inside a
  nozzle, for instance) prevents grid-induced separation of attached
  boundary layers.

In LES mode Basile et al. set the SA near-wall functions to their far-wall
values, $f_{v1}=1$, $f_{v2}=0$, $f_w=1$, to avoid a drop of subgrid viscosity
in resolved regions of low $\nu_t$ (§2.2, Eq. 7). The modelled viscosity then
scales as $\tilde\nu\sim\lvert\Omega\rvert\,d_{\mathrm{DES}}^2$, with $\lvert\Omega\rvert$ the
vorticity magnitude (the source's $\rho\tilde\nu\sim\tilde\omega\tilde d^2$), so it falls with
the square of the element size, and their adaptation lowers $\mu_t$ in the
jet shear layer from one mesh to the next (§2.2; §4.2.2, Fig. 7).

### Grid lengths

The variants differ in the length $\Delta$ that caps the RANS length:

| Variant | $\Delta$ | Source |
|---|---|---|
| DES, DDES | $\Delta_{\max}$ | as recalled by François et al. (2022, §3.1) and Basile et al. (2023, §2.2) |
| ZDES mode 2 | $\Delta_{\max}$ where $f_d<0.8$, $\Delta_{\mathrm{vol}}$ where $f_d>0.8$ | François et al. (2022), §3.1 |
| ZDES mode 0+1 on high-order DG | $\Delta_{\mathrm{vol}}/(N+1)$, $\Delta_{\mathrm{vol}}$ the cube root of the element volume, $N$ the local polynomial degree; $C_{\mathrm{DES}}=0.65$ | Basile et al. (2023), §2.2 |
| DDES in an edge-based finite-volume code | $\Delta_{\max}$ = longest edge of the dual control volume | Carlsson et al. (2023), §3 |
| SST-DES and SST-DDES in a cell-centred finite-volume code | $\Delta_{\max}$, $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$ | Delassaux et al. (2023), §4.1.3, Eq. 9 |
| IDDES | $\Delta_{dw}$ (Eq. 19 above) | Carlsson et al. (2023), §3 |
| SA-DDES with grey-area mitigation | $\Delta_{\mathrm{SLA}}$ (below), $C_{\mathrm{DES}}=0.65$ | Carlsson et al. (2023), §3.1, §4.4 |
| SST-DDES and transitional DDES in a cell-centred finite-volume code | $\Delta_{\mathrm{SLA}}$, $C_{\mathrm{DES}}=0.65$ | Möller et al. (2024), §II.B.1, Eq. 21 |
| ZDES of the supersonic base flow (Simon et al.) | $\Delta_{\mathrm{vol}}$, $C_{\mathrm{DES}}=0.55$ | as recalled by Carlsson et al. (2023), §4.4 |

Basile et al. divide by $N+1$, the number of one-dimensional degrees of
freedom, following Lorteau et al., and take $C_{\mathrm{DES}}=0.65$ ("usually
set to"), calibrated on decaying homogeneous turbulence. François et al. do
not print the formula through which $\Delta$ enters the model, nor
$C_{\mathrm{DES}}$.

The choice matters on stretched cells. Abe (2021) shows, for LES of the
shear layer behind a backward-facing step on cells with
$\Delta x/\Delta y\sim100$, that subgrid models using $\Delta_{\mathrm{vol}}$ are
"clearly suppressed" there while $\Delta_{\max}$ gives reasonable eddy
viscosities ([Abe (2021)](/sources/abe-2021.md), §IV C–D, Figs. 9–11), and
Haering et al. (2022) note that $\Delta_{\mathrm{vol}}$ tends to the smallest
cell size as the aspect ratio grows (§II C). Neither source tests a DES
model. Basile et al. remesh isotropically outside a frozen prism layer,
justified by the isotropy of the inertial-range scales in free shear flows
(§3.4).

### The shear-layer-adapted length

$\Delta_{\max}$ "often gives an excess SGS viscosity" in free shear layers in
LES mode, delaying resolved turbulence after the RANS–LES switch (the grey
area). Carlsson et al. (2023, §3.1, Eqs. 20–21) recall the remedy of Shur et
al. (2015): a vorticity-oriented length and a Kelvin–Helmholtz reduction,

$$\Delta_\omega=\frac1{\sqrt3}\max_{n,m}\lVert\boldsymbol l_n-\boldsymbol l_m\rVert,\quad
\boldsymbol l_n=\boldsymbol n_\omega\times(\boldsymbol r_n-\boldsymbol r),\quad
\boldsymbol n_\omega=\frac{\boldsymbol\omega}{\lVert\boldsymbol\omega\rVert},\qquad
\Delta_{\mathrm{SLA}}=\Delta_\omega\,F_{KH}(\langle VTM\rangle),$$

with $\boldsymbol r_n$ the cell vertices, $F_{KH}\in[0,1]$ equal to one in
developed turbulence and reduced where the vortex-tilting measure
$\langle VTM\rangle$ (averaged over neighbouring cells, near zero in
quasi-two-dimensional regions) detects Kelvin–Helmholtz structures
(page-local symbols; the source writes $\tilde\Delta_\omega$). The factor
$1/\sqrt3$ recovers $\Delta_{\max}$ for cubic cells. Replacing $\Delta_{\max}$
by $\Delta_\omega$ alone "is not enough to fully unlock the Kelvin–Helmholtz
instability". The authors state that $\Delta_{\mathrm{SLA}}$ gives the same
decaying-turbulence spectra as $\Delta_{\max}$ with the same constant
(§4.4).

### Calibration of $C_{\mathrm{DES}}$ and the numerical scheme

In LES mode on Comte-Bellot–Corrsin decaying turbulence ($32^3$ to $128^3$),
Carlsson et al. (2023, §4.2, Fig. 3) find that the "standard values" of the constant,
$C_{\mathrm{DES}}=0.65$ for SA and $0.61$ for the $k$-$\varepsilon$ branch of
SST ($0.78$ for the $k$-$\omega$ branch giving "nearly identical results", not
shown), predict the measured spectra without recalibration once the
fourth-difference dissipation coefficient of the scheme is lowered to
1/512 or 1/1024, while the RANS-practice value 1/128 is far too
dissipative on all grids; the constant is thus calibrated together with
the scheme (see [numerical dissipation](/properties/numerical-dissipation.md)
and [low-dissipation low-dispersion schemes](/methods/low-dissipation-low-dispersion-scheme.md)).

## Grid dependence and mesh adaptation

Because the cell size sets the switch, any change of cell size perturbs a
DES. In a DES of freely decaying turbulence crossing an interface where the
cell size doubles, Mozaffari et al. (2022, §1, Fig. 1, from the first
author's thesis) find that the resolved kinetic energy drops abruptly while
the modelled energy decays more slowly on the coarser mesh, because the
grid-dependent dissipation of the model's $k$-equation is smaller there;
"the loss of resolved turbulence is never equal to the gain in modeled
turbulence", so a single change in mesh size causes a lasting perturbation.
Their remedy is to drive adaptive refinement with a time-averaged criterion
so that the mesh converges to a quasi-static one; with IDDES on the
backward-facing step and DDES-SST on the DTMB 5512 hull it reaches the
fixed-mesh accuracy with fewer cells (§4–§5; see
[mesh adaptation](/methods/mesh-adaptation.md) and
[backward-facing step](/benchmarks/backward-facing-step.md)). Basile et al.
(2023) adapt a ZDES on high-order DG with an $hp$ strategy started from a
RANS-adapted mesh (§3.3).

## Applications in the sources

- **Fan–outlet-guide-vane stage** (François et al. 2022). ZDES mode 2 with
  SA in [elsA](/software/elsa.md): URANS in the core flow and upstream of
  the fan, mode 2 in the bypass; 380 million cells, free-shear cells of
  0.5 mm (ONERA's mode-2 practice: $\Delta x^+,\Delta y^+,\Delta z^+<200$ in
  free-shear regions, first cell $\Delta y^+\le1$), about 2 million CPU hours.
  The $f_d=0.95$ contour covers the whole boundary layer of fan and vanes
  and switches to LES quickly at trailing edges (§4.2, Fig. 9). Mean
  profiles agree with hot-wire data within 3%, RMS profiles lie within
  the measurement band, the wake-deficit depth is over-predicted by
  10–15% and the RMS peak by 15% on average, while RANS ($k$-$\omega$ SST
  and Smith $k$-$l$) fails in the tip gap (§5.3–5.4, Figs. 12–15). The URANS
  border must be placed so that all streamlines passing near the fan and
  entering the bypass are in mode 2; otherwise part of the wakes stays
  "RANS-like" (§3.2.1). Lewis et al. (2023) compare two wall-modelled LES
  of the same [ACAT1 stage](/benchmarks/acat1-fan-stage.md) with this ZDES
  and its acoustic follow-up by Polacsek et al.: the trends of the
  simulations agree, the ZDES recovers the measured RMS levels better but
  shows a secondary peak of the axial RMS velocity absent in the
  experiment, and the ZDES gives an aft-to-front difference of the vane
  noise sources of about 5 dB (vane split at 50% chord) against about
  10 dB in their LES (split at 40% of the maximum axial chord)
  ([Lewis et al. (2023)](/sources/lewis-2023.md), §4.3, §5.3.1; HAL accepted
  manuscript; see [wall-modelled LES](/methods/wall-modelled-les.md)).
- **Full-scale car** (Delassaux et al. 2023). SST-DDES of a simplified
  Peugeot 308 SW estate car at $Re_L=1.3\times10^7$ in ANSYS Fluent
  (bounded central differencing, $\Delta t=5\times10^{-5}$ s, 115 million
  cells with 20 prism layers at $y^+\approx1$): drag 0.255 against 0.244
  measured and 0.242 for SST and realizable $k$-$\varepsilon$ RANS, but the
  wake topology, the base pressure, the underbody flow and the cross-plane
  velocities agree with the wind-tunnel data where RANS fails; on rounded
  separation lines DDES under-predicts the pressure coefficient (GIS
  above), on the sharp rear lump it is the most accurate (§6–§7, Table 3,
  Figs. 15–28). A RANS run takes about 2 hours on 384 cores, a DDES about
  1.5 days on 1152 cores (§7.6). They advise a maximum CFL number of 5 in
  the LES region (structures vanish above it) and use a time step giving
  "a CFL number below 2 around the car" (§4.2), and a prism-layer growth
  ratio below 1.25 for hybrid methods after Spalart & Streett (§4.4). See
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
  [k-ε models](/methods/k-epsilon-model.md).
- **Subsonic jet** (Basile et al. 2023). ZDES mode 0+1 on the negative SA
  model, RANS forced inside the nozzle, on the isothermal PPRIME jet at
  $M_j=0.9$, $Re_D\simeq10^6$; with 31.7 million degrees of freedom the
  finest $hp$ mesh matches the finest ZDES and implicit-LES references,
  which used more degrees of freedom; refinement lengthens the potential
  core beyond experiment, as in those references (§4.2.3, Table 1, Fig. 9).
- **Separated and vortical flows with adaptation** (Mozaffari et al. 2022).
  IDDES of the Vogel–Eaton backward-facing step ($Re_H=28{,}000$):
  reattachment-length error 25% with instantaneous-criterion adaptation,
  5.1% and 3.6% with averaged criteria on 2.5 and 9.9 million cells, 9.6%
  on a 9.3-million-cell fixed mesh (Table 2). DDES-SST of the DTMB 5512
  hull at 10° drift on an adapted 154-million-cell mesh reproduces the
  163-million-cell fixed-mesh DDES up to $x/L=0.4$, the end of that mesh's
  finest box, and keeps the experimental trends downstream (160 000 against
  about 250 000 CPU hours)
  and a delta wing at $\alpha=24^\circ$ (§5).
- **Supersonic axisymmetric base flow** (Carlsson et al. 2023, §4.4).
  Herrin–Dutton experiment, $M_\infty=2.46$, $Re_R=1.632\times10^6$ on the base
  radius $R$. As the authors recall, DESider SA-DES with $\Delta_{\max}$ and
  $C_{\mathrm{DES}}=0.65$ (0.9–3.6 million cells) gave a good flat base
  pressure but an over-long recirculation and low early shear stresses,
  attributed to excess $\mu_t$ from $\Delta_{\max}$; ZDES of Simon et al. (13.5
  and 20.7 million cells) matched recirculation length and shear stress but
  over-predicted backflow and gave a wavy, too low base pressure; SA-DDES
  with $\Delta_{\mathrm{SLA}}$ of Guseva et al. (2 million cells) accelerated the
  instability without a flat base pressure. Their own SA-DDES with
  $\Delta_{\mathrm{SLA}}$ on 1.82, 2.06 and 8.51 million cells shows that the
  low-dissipation scheme unlocks the Kelvin–Helmholtz instability, its
  coarse grid matching the reference scheme's fine grid in small-scale
  content; reattachment at $x/R\approx2.7$ (G2, G3) against 2.67 measured,
  against about 4.0 (G1) and 3.0 (G2, G3) with the reference scheme; better
  shear stress at $x/R=1.57$; but a wavy, under-predicted base pressure
  (experiment flat near $C_p=-0.102$): "improved numerics in the initial
  shear layer does not produce a better prediction of the base pressure
  profile" (Figs. 9–10).
- **Ahmed body**, as recalled by Delassaux et al. (2023, §5, Table 2) from
  their own calibration on four 25° bodies (sharp and rounded edges): RANS
  gives no separation (realizable $k$-$\varepsilon$) or massive separation
  (SST) on the slant; scale-adaptive simulation overestimates and
  stress-blended eddy simulation underestimates the recirculation length;
  SST-DDES is closest, with maximum errors of 3.3% in drag and 7.1% in lift
  on a 20-prism-layer grid. Time steps of $1.5\times10^{-5}$ and
  $5\times10^{-5}$ s give globally the same results, while a CFL number
  above 10 gives no or massive separation on the slant (see
  [Ahmed body](/benchmarks/ahmed-body.md)).
- **Ahmed body**, as recalled by Cai et al. (2022, §I). Menter & Kuntz
  obtained the partial reattachment of the 25° slant with DES where RANS
  gave fully attached or fully separated flow; Guilmineau et al.'s DES and
  IDDES on body-fitted grids predicted the massive 35° separation with a
  small separation near the slant end, and at 25° only IDDES gave the
  partial reattachment; their 35° drag coefficients are 0.3156 (DES) and
  0.3452 (IDDES) against 0.279 measured by Meile et al. (Table III). Cai et
  al. state that their immersed-boundary wall-modelled LES (0.2347) is
  closer to experiment than that IDDES; their Table III also lists RANS,
  EARSM and DES values closer to 0.279 than 0.2347 *(compiler check, not
  in the sources)*
  ([Cai et al. (2022)](/sources/cai-2022.md), §I, §IV, Table III; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Lattice Boltzmann airfoil and Ahmed body** (Mozaffari et al. 2024).
  On the NACA 0012 at $Re_c=3\times10^6$, SST-IDDES reproduces RANS while
  the flow is attached ($\alpha\le15^\circ$, the fine leading-edge grid
  running the outer boundary layer in LES mode at $15^\circ$); at $45^\circ$
  it gives $C_L=1.231$, $C_D=1.038$ against reference values of 1.097 and
  1.180 and RANS values of 2.238 and 2.053 (§3.2, Table 2, Figs. 10–12). On
  the [Ahmed body](/benchmarks/ahmed-body.md) ($Re_H=7.68\times10^5$, 45.8
  million nodes) with the equilibrium wall model on the body, neither IDDES
  nor continuous eddy simulation separates on the $25^\circ$ or $35^\circ$
  slant, which the authors attribute to the wall model's missing pressure
  gradient and to the missing instability that would switch the hybrid to
  LES; with a zero-velocity condition at $y^+\gg1$ instead, IDDES
  reproduces the $35^\circ$ wake topology and drag (0.2819 against
  0.258–0.32 measured) but at $25^\circ$ separates late and does not
  reattach, attributed to $y^+\approx100$–$150$ on the slant (§3.3,
  Figs. 16–24, Table 3).
- **High-lift airfoil** (Wang et al. 2024). SA-based DDES of the 30P30N
  three-element airfoil ($M_\infty=0.17$, $Re=1.7\times10^6$,
  $\alpha=5.5^\circ$, span $0.74C$, about 27 million cells,
  $\Delta tU_\infty/C=2\times10^{-5}$) with a sixth-order optimized upwind
  scheme agrees with the measured mean $C_p$, slat-cove profiles and the
  slat-trailing-edge pressure spectrum (tone near 21 kHz); the authors use
  it to classify the spatial patterns of the turbulent-kinetic-energy budget
  terms across the shear layers and attribute the budget imbalance to grid
  resolution ([Wang et al. (2024)](/sources/wang-2024.md), §4, Figs. 8–12).
- **Transonic buffet**, as recalled by Petrocchi & Barakos (2024, §1) for
  the OAT15A airfoil: Deck's basic DES failed to predict the shock
  oscillation, ZDES over-predicted the trailing-edge unsteadiness, a DDES of
  Grossi et al. gave higher leading-edge unsteadiness, and an IDDES of Huang
  et al. with a time step more than an order of magnitude larger placed the
  shock too far upstream; Petrocchi & Barakos attribute such problems to
  overly fine grids in separated regions and to the time step, and argue
  that DES-family methods in LES mode reintroduce LES grid and time-step
  requirements that [PANS](/methods/partially-averaged-navier-stokes.md)
  avoids on RANS-like grids
  ([Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md), §1).
- **Turbomachinery design**, as stated by Liu et al. (2024): DES, SAS and
  related hybrids are too expensive for routine turbomachinery design,
  which motivates their transition-coupled
  [Reynolds-stress model](/methods/reynolds-stress-model.md)
  ([Liu et al. (2024)](/sources/liu-2024.md), Introduction).
- **Dynamic stall**, as recalled by Baldan & Guardone (2025, Introduction):
  the DES best practice of Shur et al. requires a span of at least one
  chord to reproduce the dynamic-stall vortex, a requirement the authors
  confirm for wall-resolved LES of a pitching NACA 0012 in the downstroke
  ([Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.1; arXiv v2; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Wind-turbine noise**, as recalled by Rismondo et al. (2025, §1): Nelson
  et al. used delayed DES with Farassat's linear acoustic formulation for a
  full wind turbine ([Rismondo et al. (2025)](/sources/rismondo-2025.md),
  §1; see [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)).
- **Capsule wakes**, as recalled by Placco et al. (2023, §1). DES of
  planetary-entry capsule wakes was restricted to the near-body wake and
  disagreed with experiment in the backshell area, which the cited work
  attributed to the model's prediction of transition after shoulder
  separation ([Placco et al. (2023)](/sources/placco-2023.md), §1).

## Qualifications

- François et al. state that relying on RANS in the boundary layer lets
  them use 0.5 mm free-shear cells and that the same density "would require
  a larger number of cells in the whole mesh with a WMLES approach" (§4.1),
  and that the cost of ZDES is "much less dependent on the Reynolds number"
  than that of wall-resolved or wall-modelled LES (§1); no cost comparison
  is shown.
- François et al. print $f_d=1-\tanh(8r_d)^3$, which can be read as
  $1-[\tanh(8r_d)]^3$, while Yan et al. write $1-\tanh\big((8r_d)^3\big)$.
  Neither source discusses the form further. At $r_d=1$ both readings give
  $f_d\approx0$ ($\tanh8\approx1$), so François et al.'s description does
  not decide between them *(compiler check, not in the sources)*.
- None of the three applications of chunks 1–2 prints the DES equations in
  full; Mozaffari et al. print none. Carlsson et al. (2023) print the DDES
  and IDDES length scales but not $f_d$, $\hat f_d$ or $f_e$.
- Carlsson et al. print $C_{dw}$ in their Eq. 19 and "$C_w=0.15$" below it.
  They credit their conclusion on grey-area mitigation partly to the
  vorticity-weighted shock sensor, but the base-flow comparison changes the
  sensor, the dissipation coefficient and the face extrapolation at once
  (§4.4, §5, Table 1), so the sensor's share is not isolated *(compiler
  check, not in the sources)*.
- Delassaux et al. print $f_d=1-\tanh[(C_{d1}r_d)^{C_{d2}}]$ with the power
  inside the hyperbolic tangent; with $C_{d1}=8$, $C_{d2}=3$ this is Yan et
  al.'s reading of the SA form above *(compiler check, not in the sources)*.
  Delassaux et al. attribute $C_{d1}=20$ to the SST host (Gritskevich et
  al.); François et al.'s 8 goes with the Spalart–Allmaras host.
- Delassaux et al. state the RANS-to-LES switch as occurring "when
  $\Delta_{\max}<\delta$" (§4.1.3), while their Eq. 7 switches where
  $C_{\mathrm{DES}}\Delta_{\max}<l_{\mathrm{RANS}}$; they use the
  $\Delta_{\max}$–$\delta$ comparison to design their surface meshes
  ("Menter's criterion", §4.4). They
  give $C_{d1}=20$ in §4.1.3 and call 30 "advised for this case" in §4.4,
  without stating which value the reported car results use. The cost ratio
  "18 times more expensive" (§7.6) is the wall-clock ratio; in core-hours
  the printed figures give 54 *(compiler check, not in the sources)*.
- $C_{\mathrm{DES}}=0.65$ goes with $\Delta_{\mathrm{vol}}/(N+1)$ in Basile et al.
  and with $\Delta_{\max}$ or $\Delta_{\mathrm{SLA}}$ in Carlsson et al.; the ZDES
  base-flow studies recalled by Carlsson et al. use 0.55 with
  $\Delta_{\mathrm{vol}}$. Carlsson et al. call the constant code dependent, so
  these are different calibrations, not a disagreement.
  Möller et al. (2024) use 0.65, citing Travin et al., with an SST host and
  $\Delta_{\mathrm{SLA}}$, where Carlsson et al. and Delassaux et al. blend
  0.61 and 0.78 for SST; Möller et al. checked their value on decaying
  isotropic turbulence without showing it (§II.B.1).
- Möller et al. use $\kappa$ both for the ratio of specific heats (1.4) and
  for the von Kármán constant of $r_d$ (§II.A, Eq. 20). They write that
  values $l_{\mathrm{RANS}}/l_{\mathrm{DDES}}<0$ are not possible (p. 7); by their
  Eq. 18, $l_{\mathrm{DDES}}\le l_{\mathrm{RANS}}$, so the ratio is at least one
  wherever $l_{\mathrm{DDES}}>0$, the stronger bound their text uses
  *(compiler check, not in the sources)*.

# Citations

- [François et al. (2022)](/sources/francois-2022.md) — §1, §3.1 (pp. 5–6, footnote 2), §3.2.1, §3.4–3.5, §4.1–4.2 Fig. 9, §5.3–5.4 Figs. 12–15.
- [Basile et al. (2023)](/sources/basile-2023.md) — §1, §2.2 Eqs. 5–7, §3.3–3.4, §4.2.2 Fig. 7, §4.2.3 Table 1 Fig. 9.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §1 Fig. 1, §2, §4.1, Table 2, §5.
- [Haering et al. (2022)](/sources/haering-2022.md) — §I, §II A, §II C.
- [Abe (2021)](/sources/abe-2021.md) — §IV C–D, Figs. 9–11.
- [Yan et al. (2022)](/sources/yan-2022.md) — §2.3.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1.
- [Carlsson et al. (2023)](/sources/carlsson-2023.md) — §1, §3 Eqs. 16–19, §3.1 Eqs. 20–21, §4.2 Fig. 3, §4.3 Table 2 Figs. 4–6, §4.4 Figs. 9–10, §5.
- [Cai et al. (2022)](/sources/cai-2022.md) — §I, §IV, Table III (HAL v1).
- [Placco et al. (2023)](/sources/placco-2023.md) — §1.
- [Delassaux et al. (2023)](/sources/delassaux-2023.md) — §4.1.3 Eqs. 6–11, §4.2, §4.4 Fig. 8, §5 Table 2, §6–§7 Table 3 Figs. 15–28, §7.3 Fig. 21, §7.6 (HAL author manuscript).
- [Lewis et al. (2023)](/sources/lewis-2023.md) — §4.3, §5.3.1 (HAL accepted manuscript).
- [Mozaffari et al. (2024)](/sources/mozaffari-2024.md) — §2.3 Eqs. 26–32, §3.2 Table 2 Figs. 10–12, §3.3 Figs. 16–24 Table 3 (HAL accepted manuscript).
- [Wang et al. (2024)](/sources/wang-2024.md) — §4, Figs. 8–12.
- [Petrocchi & Barakos (2024)](/sources/petrocchi-2024.md) — §1.
- [Liu et al. (2024)](/sources/liu-2024.md) — Introduction.
- [Möller et al. (2024)](/sources/moller-2024.md) — §I, §II.B.1 Eqs. 17–22, §II.B.3 Eqs. 24–25, 27, §II.D Fig. 1, §II.F, §III.A–B Figs. 3–22, Tables 2–3, Eq. 28, §IV (accepted manuscript).
- [Wu et al. (2025)](/sources/wu-2025.md) — §2.1, Eqs. 5–6, Fig. 2 (authors' manuscript).
- [Baldan & Guardone (2025)](/sources/baldan-2025.md) — Introduction, §2.1 (arXiv v2).
- [Rismondo et al. (2025)](/sources/rismondo-2025.md) — §1.
