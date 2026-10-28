---
type: Method
title: "Detached-eddy simulation and its delayed and zonal forms"
description: "The single-model hybrid RANS/LES in which a RANS model's length scale is capped by a grid length so that the model acts as a subgrid model away from walls; the DES switch and ambiguous grids, DDES shielding, IDDES, ZDES modes including mode 2 (2020), grid lengths, calibration with the numerical scheme, transitional DDES, and applications."
status: established
aliases: [DES, DDES, delayed detached-eddy simulation, IDDES, improved delayed DES, ZDES, zonal detached-eddy simulation, DDES-SST, SST-IDDES, SA-DDES, ZDES mode 2, ZDES mode 0+1, shear-layer-adapted length scale, grey area, DDES-γ, transitional DDES, RSM-IDDES, RSM-DynIDDES, dynamic IDDES, modelled-stress depletion, grid-induced separation]
tags: [des, hybrid-rans-les, rans, les, turbomachinery, mesh-adaptation]
timestamp: 2026-10-28T07:07:00Z
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
the cell volume); $r_d$ and $f_d$ are the DDES shielding parameter and function (registry §11).

## The DES switch and its failure on ambiguous grids

Basile et al. (2023, §1) describe the original DES as non-zonal: a
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

**The industrial view.** Mani & Dorgan (2023) describe modelled-stress
depletion as the RANS-to-LES transition happening "very near the wall" on a
grid not refined enough for the small-scale features there, so that the
simulation "contains too little viscous stress", which "generally
manifests as grid-induced premature flow separation"; the original DES was
particularly sensitive to it, DDES "significantly improved" it, and DDES is
therefore used "in almost all circumstances" for unsteady simulation at
Boeing ([Mani & Dorgan (2023)](/sources/mani-2023.md), §4.5.2). They report
that certain grid topologies still trigger depletion under DDES,
particularly on unstructured meshes with little control of point
placement, and expect the problem to grow as unsteady mesh adaptation
matures unless the adaptation "is somehow aware of the requirements for
DDES". In a Boeing serpentine-inlet study with smooth-body separation
(Lakebrink & Mani 2018, reproduced in their Fig. 11), the eddy viscosity of
DDES had substantially decayed inside the attached boundary layer upstream
of separation compared with RANS on the same grid; raising the constant
multiplying $r_d$ in $f_d$ from 8 to 16 restored the boundary layer but
"dampened all detached eddies and substantially delayed the separation"
(a value of 4 was also tested). Citing Mani & Winkler and Ashton, they state
that DDES selects the LES branch in the boundary layer when the surface mesh
is nearly isotropic, and that the same holds for IDDES. Menter's robust
shielding function for two-equation hybrids (stress-blended eddy
simulation) has proprietary blending details, and they call for "a
completely robust shielding function within the public domain" (§4.5.2).

Wu et al. (2023), citing Menter, list grid-induced separation and "a slow
'transition' from RANS to LES" among the limitations of DES, DDES and IDDES
([Wu et al. (2023)](/sources/wu-2023-b.md), §1), and attribute the early flap
separation of their SST-IDDES of the 30P30N airfoil to grid-induced
separation, "although the turbulent boundary layer was partially protected
to avoid modeled stress depletion" (§3.4; Applications below). Li et al.
(2022, App. 1–2, Figs. 23–24) check their dynamic RSM-IDDES for both
defects: on the periodic hill the $f_d$ field keeps an intact thin RANS
layer containing the boundary layer upstream of separation, so no
depletion occurs, and on the NASA flat plate (finest grid $545\times385$)
the skin friction follows Kármán–Schoenherr and the profile at
$Re_\theta=10\,000$ follows Coles's in all sublayers, without
[log-layer mismatch](/definitions/log-layer-mismatch.md).

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

Pan & Zhang (2023) print the two original SA-based forms as implemented in
ANSYS Fluent: DES with $d_{\mathrm{DES}}=\min(d,C_{\mathrm{DES}}\Delta_{\max})$,
$C_{\mathrm{DES}}=0.65$, and DDES with
$d_{\mathrm{DDES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta_{\max})$,
$f_d=1-\tanh\big[(8r_d)^3\big]$ and
$$r_d=\frac{\tilde\nu}{\sqrt{\partial_ju_i\,\partial_ju_i}\;\kappa^2d^2},$$
the working variable alone in the numerator, where François et al. write
$\nu+\tilde\nu$ and Möller et al. $\nu_t+\nu$
([Pan & Zhang (2023)](/sources/pan-2023.md), §II.B–C, Eqs. 7–11). They
state the motivation of DDES as the "nonphysical separation phenomenon
induced by Reynolds stress loss" of DES on grids that do not meet LES
requirements, i.e. grid-induced separation (§II.C). Zhang et al. (2024)
print the same SA-based DDES length,
$\tilde d=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta)$ with $\Delta=\Delta_{\max}$,
$C_{\mathrm{DES}}=0.65$ "calibrated by the decay of isotropic turbulence" and
$f_d=1-\tanh[(8r_d)^3]$, with $\nu+\tilde\nu$ in the numerator of $r_d$ as
François et al., and write the velocity-gradient norm first as the strain
norm $S$ of their SA equation (Eq. 3) and then as $\sqrt{\partial_ju_i\,\partial_iu_j}$,
which they call its "traditional" representation (Eq. 4), the index order
of François et al. ([Zhang et al. (2024)](/sources/zhang-2024.md), §2.3,
Eqs. 3–8). The limits $f_d=0\Rightarrow\tilde d=d$ (RANS) and
$f_d=1\Rightarrow\tilde d=\min(d,C_{\mathrm{DES}}\Delta)$ (DES97) are as they
state; they credit the delay with removing "nonphysical artifacts" in the
shear layer during the RANS-to-LES transition. Husson et al. (2024)
print the zonal-DES form of the same function, with $\nu(1+\chi)=\nu+\tilde\nu$
in the numerator and $\kappa=0.41$ (§2.2, Eq. 26; below). Lodares et al.
(2022) and Tomboulides et al. (2025) name a DES built on their RANS models
(an entropy-stable RANS near walls coupled to entropy-stable LES; an SST
form of the [$k$-$\tau$ model](/methods/k-tau-model.md)) as future work
([Lodares et al. (2022)](/sources/lodares-2022.md), §8;
[Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §4).

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

Li et al. (2024b) print the same blending on SA: the wall distance in the
destruction term is replaced by
$l_{\mathrm{IDDES}}=\hat f_d(1+f_e)\,l_{\mathrm{RANS}}+(1-\hat f_d)\,l_{\mathrm{LES}}$
with $l_{\mathrm{RANS}}=d$, $l_{\mathrm{LES}}=C_{\mathrm{DES}}\Delta$ and
$\Delta=\min[\max(C_wd,C_w\Delta_{\max},\Delta_{wn}),\Delta_{\max}]$, $C_w=0.15$
"recommended" by Shur et al.; $\hat f_d$, $f_e$ and the value of
$C_{\mathrm{DES}}$ are not printed ([Li et al. (2024b)](/sources/li-2024-f.md),
§II.B.2, Eq. 4). They adopt IDDES because it "can avoid grid-induced
separation (GIS) and logarithmic layers mismatched (LLM) issues of the
original DES method" (see [log-layer mismatch](/definitions/log-layer-mismatch.md)),
and judge zonal hybrids "intractable to use" for the geometric complexity of
high-lift transport configurations (§I).

**SST-IDDES as a wall-modelled LES of supersonic flows.** Zangeneh (2021)
prints the same blending, $l_{\mathrm{IDDES}}=f_B(1+f_e)\,l_{\mathrm{RANS}}+(1-f_B)\,l_{\mathrm{LES}}$
with $f_B$ (the source's symbol where Carlsson et al. print $\hat f_d$) an empirical
function rising from 0 to 1 that switches rapidly from RANS mode with wall
distance and $f_e$ a function that "corrects the RANS behavior", and uses
it in the $k$ destruction $\rho\sqrt{k^3}/l_{\mathrm{IDDES}}$ of SST (after
Gritskevich et al.; no coefficient printed), the RANS inner layer being
solved on an auxiliary wall grid embedded in the coarse LES mesh
([Zangeneh (2021)](/sources/zangeneh-2021.md), §II.A–B, Eqs. 1, 5–7). The
author cites evidence that IDDES does not remove the
[log-layer mismatch](/definitions/log-layer-mismatch.md): hybrid wall
modelling gives skin friction "on the order of 15% too low" (Nikitin et
al. 2000), IDDES under-predicted it by about 25% in supersonic boundary
layers (Gieseking et al.), Peterson & Candler attributed the mismatch to the
calibration of IDDES on low-speed channels, while Mockett et al. found it
even in low-speed channel IDDES and suggested numerical sensitivity, so
that "a concrete explanation for the problem of the IDDES model has
remained elusive" (§I). The paper's remedy, a random-forest correction of
the wall shear stress and heat flux fed back through $\mu_t$ and $Pr_t$, is
on the [machine-learning wall-model page](/methods/machine-learning-wall-model.md).

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
[continuous eddy simulation](/methods/continuous-eddy-simulation.md)). In their runs the
RANS–LES transition is thin with IDDES and smooth with continuous eddy
simulation (§3.2, Fig. 11).

**SST-DES with $F_2$ shielding in ANSYS CFX.** Yang & Ma (2022) print the
SST-DES of Strelets as a multiplier of the $k$-destruction,
$\beta^*k\omega\to\beta^*k\omega\max\big(L_t/(C_{\mathrm{DES}}\Delta),1\big)$ with
$L_t=\sqrt k/(\beta^*\omega)$ (page-local), $\Delta$ the largest cell edge and
$C_{\mathrm{DES}}=0.61$, and its CFX form
$\max\big(L_t(1-F_2)/(C_{\mathrm{DES}}\Delta),1\big)$, in which the SST
function $F_2$ shields the attached boundary layer against grid-induced
separation and modelled-stress depletion and "can offer essentially
asymptotic shielding" ([Yang & Ma (2022)](/sources/yang-2022-b.md), §2.1,
Eqs. 1–5). The paper calls the method DES, DES-type, hybrid DES and DDES interchangeably.

**SST-DDES in ANSYS Fluent.** Thawait et al. (2023) print the Fluent form
as a multiplier of the $k$-destruction, $\rho\beta^*k\omega\to\rho\beta^*k\omega F_{\mathrm{DES}}$,

$$F_{\mathrm{DES}}=\max\Big(\frac{L_t}{C_{\mathrm{DES}}\Delta_{\max}}(1-F_{\mathrm{DDES}}),1\Big),\qquad L_t=\frac{\sqrt k}{\beta^*\omega},\qquad F_{\mathrm{DDES}}=\tanh\big[(C_{d1}r_d)^{C_{d2}}\big],$$

with $C_{\mathrm{DES}}=0.61$, $C_{d1}=20$, $C_{d2}=3$, $\kappa=0.41$ and the $r_d$ of
Mozaffari et al. (2024) above ($F_{\mathrm{DES}}$, $F_{\mathrm{DDES}}$ registry §11;
[Thawait et al. (2023)](/sources/thawait-2023.md), §II B, Eqs. 9–13). Where
Yang & Ma's CFX form carries $1-F_2$, this form carries $1-F_{\mathrm{DDES}}$,
which has the printed form of the $f_d$ of Delassaux et al.; with
$F_{\mathrm{DDES}}\to1$ the factor is $F_{\mathrm{DES}}=1$ and the
$k$-destruction is that of SST *(compiler check, not in the sources)*. The
paper also prints the length
$d_{\mathrm{DDES}}=d-f_d\max(0,d-C_{\mathrm{DES}}\Delta_{\max})$ (the source's
$\tilde d$) with $f_d=1-F_{\mathrm{DDES}}$ as "the length scale for the DDES
model" (Eq. 14), the SA-based DDES length that Pan & Zhang print for ANSYS
Fluent (above), without saying where it enters the SST equations. The authors motivate DDES, citing Spalart (1997) and Strelets
(2001), by the modelled-stress depletion of DES when LES activates in cells
smaller than the boundary-layer thickness; DDES "preserves RANS in the
boundary layer" (§II B). See [ANSYS Fluent](/software/ansys-fluent.md).

**A thinner shield in a temporal-filtering hybrid.** Mays et al. (2023)
compare DDES with the scale-resolving hybrid (SRH) model of Duffal et al.,
which also modifies only the dissipation of the modelled $k$ equation,
multiplying it by a factor $\psi_H\ge1$ derived from a formal temporal
filter, "like DDES alters the destruction term"; the major difference is
how the factor is set: it depends on the time-mean resolved kinetic
energy, so the model responds to the resolved content, which the authors,
after Heinz, call a "major difference from DES formulations"
([Mays et al. (2023)](/sources/mays-2023.md), §1, §2.1.2, Eqs. 9–13). Its
shielding has the same form as that of DDES, written with page-local
$f_s$ (zero at the wall),
$$f_s=1-\tanh\Big[\Big(45\,\frac{\nu^{3/4}}{\varepsilon^{1/4}d}\Big)^8\Big],$$
the ratio of the wall distance to a Kolmogorov length, calibrated to fall
away at $y^+=100$ in channel flow; on the drag-crisis cylinder its shield
front ($f_s=0.01$) lies inside the boundary layer and is nearly
grid-invariant, whereas the DDES shielded zone "is generally much broader,
producing a RANS-like solution", as the authors found in their earlier
study (§3.1.1, §3.2.2, Figs. 5, 10a). They judge the thin shield necessary
for the breakdown of the separated shear layers, note that it leaves the
model with log-layer mismatch in channel flow, and conclude that "it is
likely that there is no ideal universal shielding function" (§3.2.2; see
[hybrid RANS/LES](/definitions/hybrid-rans-les.md) and
[log-layer mismatch](/definitions/log-layer-mismatch.md)).

**DDES-p for Cartesian grids.** Sugaya & Imamura (2021) run DDES-p, an
SA-based DDES variant of Tamaki, Imamura & Kawai that "introduces a simple
modified shielding function to protect the RANS regions when the
stream-wise grid size is small, meaning the model is suitable for unsteady
flow simulations using Cartesian grids"; the function is not printed
([Sugaya & Imamura (2021)](/sources/sugaya-2021.md), §2.1).

### A general construction through the dissipation term

Wang et al. (2021) derive DES-type models for any RANS model with a
length-scale variable $\phi$ ($\varepsilon$, $\omega$, …) by modifying only the
dissipation of the modelled kinetic energy
([Wang et al. (2021)](/sources/wang-2021-l.md), §2.3, Eqs. 11–16). Writing
the length-scale equation of homogeneous turbulence with production and
destruction coefficients $C_{\phi1}$, $C_{\phi2}$ (page-local; for a
"standard" $\phi$-equation $C_{\phi1}=m+nC_{\varepsilon1}$, $C_{\phi2}=m+nC_{\varepsilon2}$
with $\phi\propto k^m\varepsilon^n$), assuming local equilibrium of
production and dissipation and requiring the LES branch to reduce to the
[Smagorinsky model](/methods/smagorinsky-model.md) $\nu_t=(C_s\Delta)^2\lvert\bar S\rvert$
gives a model length proportional to $\Delta$ and

$$\varepsilon=\begin{cases}k^{3/2}/(C_{\mathrm{DES}}\Delta) & \text{LES region},\\ k^{3/2}/l_{\mathrm{RANS}} & \text{RANS region},\end{cases}\qquad
C_{\mathrm{DES}}=C_s\Big(\frac{C_{\phi1}}{C_{\ell\varepsilon}C_{\phi2}}\Big)^{3/4},$$

with $C_{\ell\varepsilon}=0.09$ (page-local). With $C_s=0.18$ and the
$\omega$-equation coefficients of SST, $(C_{\phi1},C_{\phi2})=(0.55,0.83)$ and
$(0.44,0.92)$, the theoretical constants are $C_{\mathrm{DES},k\text{-}\omega}=0.805$
and $C_{\mathrm{DES},k\text{-}\varepsilon}=0.630$, "with calibration values of
0.78 and 0.61, respectively", blended by $F_1$, with
$l_{\mathrm{RANS}}=\sqrt k/(C_\mu\omega)$ (§2.3, Eqs. 17–18). Substituting the
printed values reproduces 0.805 and 0.630 *(compiler check, not in the
sources)*. Because $C_{\mathrm{DES}}$ sets the effective Smagorinsky
coefficient of the LES branch, a dynamic $C_{\mathrm{DES}}$ yields a dynamic
Smagorinsky model there (§2.3). The authors call the argument "a rigorous
proof"; it rests on the equilibrium and homogeneous-turbulence
assumptions stated above.

**Reynolds-stress IDDES.** Applied to the SSG/LRR-$\omega$
[Reynolds-stress model](/methods/reynolds-stress-model.md), whose length
scale comes from the same BSL $\omega$-equation, the construction replaces
the isotropic dissipation tensor by $\tfrac23(k^{3/2}/l_{\mathrm{IDDES}})\delta_{ij}$
with $k=\tfrac12R_{ii}$ and the IDDES length of Shur et al. (as in the
blending above, with $C_w=0.15$); the theoretical constants are the same as
for SST, $C_{\mathrm{DES,SSG}}=0.630$ and $C_{\mathrm{DES,LRR}}=0.805$, blended
by $F_1$ (§2.3–§2.4, Eqs. 19–20). In the LES region the transported stress
acts as the subgrid stress (§3.3, Fig. 10). The authors implement it as
RSM-IDDES in the unstructured finite-volume solver HUNS3D and calibrate it
with the scheme (below).

**Dynamic RSM-IDDES.** Li et al. (2022) take the same construction one step
further: since $C_{\mathrm{DES}}=C_kC_s$ with
$C_k=\big(C_{\phi1}/(C_{\ell\varepsilon}C_{\phi2})\big)^{3/4}$ (registry §11 $C_k$;
$C_{\ell\varepsilon}=0.09$), a dynamic Smagorinsky coefficient makes the DES
constant dynamic, and the LES branch of RSM-IDDES becomes a dynamic
Smagorinsky model; they call the result RSM-DynIDDES
([Li et al. (2022)](/sources/li-2022-k.md), Abstract, §II C, Eqs. 6–9). The
coefficient comes from the compressible
[dynamic procedure](/methods/dynamic-procedure.md) of Moin et al. with
Lilly's least squares, $C_s^2=\mathcal A(L^\rho_{ij}M_{ij})/\mathcal A(M_{ij}M_{ij})$,
where $L^\rho_{ij}$ is the density-weighted resolved stress of their Eq. 11
(ordering opposite to the registry's $L_{ij}$, see Qualifications),
$M_{ij}$ the model tensor of the procedure and $\mathcal A$ the
volume-weighted average over the direct face neighbours of a cell
($\mathcal A$ registry §11, $L^\rho_{ij}$ and $M_{ij}$ page-local); the test filter is the same neighbour average, of
width $\hat\Delta=2\Delta$ "in general", which works on hybrid unstructured
meshes, and negative $C_s^2$ (backscatter) is clipped to zero for stability
(§II C, Eqs. 10–15, Fig. 1; see
[energy backscatter](/definitions/energy-backscatter.md)). The grid filter is
the implicit finite-volume cell average, and $\Delta$ is the IDDES length
$\min[\max(C_wd,C_w\Delta_{\max},\Delta_{wn}),\Delta_{\max}]$ with $C_w=0.15$
(§II B–C, Eq. 5; $\Delta$ here is that grid length, not a filter width). The authors give two reasons for leaving the constant
coefficient: the decaying-turbulence calibration of $C_{\mathrm{DES}}$ depends on
grid resolution and scheme dissipation (citing Mockett), and a constant
Smagorinsky dissipation calibrated on isotropic turbulence is too large in
mean shear and damps the large-scale fluctuations, while an underestimated
constant can make the computation diverge (§I, citing Germano et al.). They
cite earlier dynamic hybrids built on eddy-viscosity hosts (Bhushan &
Walters on SA; He, Liu et al. on SST-DDES; Yin, Reddy et al. on a
$k$-$\omega$ DDES) and call theirs the first on a Reynolds-stress host (§I).
In their equilibrium argument the LES branch is "Smagorinsky-like", an exact
Smagorinsky model only in equilibrium turbulence (§II C).

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
registry §11, $M=0.1$,
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
  the upwind fraction of the Roe flux, registry §11) in both boundary layers and
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
part of the domain either URANS or one of several ZDES *modes*. The two
sources that use it describe them:

- **mode 0** is RANS; **mode 1** is meant for separation fixed by the
  geometry; modes 1 and 3 need user-defined zones, mode 2 detects the
  regions automatically with the shielding function (Basile et al. 2023, §1,
  §2.2);
- **mode 2** solves the boundary layer in URANS and the rest in LES, with the
  DDES $f_d$ computed from $\tilde\nu$; it differs from DDES mainly in the
  length scale, which switches with $f_d$ (François et al. 2022, §3.1, p. 6);
  Deck's comparisons on a mixing layer, a backward-facing step and an
  airfoil, which François et al. cite, show that it keeps the
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

### ZDES mode 2 (2020)

Husson et al. (2024) print in full the 2020 version of mode 2 of Deck &
Renard, the "automatic" mode, on the SA model in its normalized form
$\chi=\tilde\nu/\nu$, and transpose it to a lattice Boltzmann solver
([Husson et al. (2024)](/sources/husson-2024.md), §2.2, Eqs. 24–35). The
hybrid length is the DDES one with a new shielding function $f_P$
(registry §11),

$$\ell=d-f_P\max\big(0,\,d-C_{\mathrm{DES}}\Delta\big),\qquad f_P=f_d\big[1-(1-f_{P2})f_R\big],\qquad C_{\mathrm{DES}}=0.65,$$

$f_P=0$ giving RANS ($\ell=d$) and $f_P=1$ the LES length. Three functions
(registry §11 names $f_{P2}$, $f_R$, $\mathcal G_{\tilde\nu}$, $\mathcal G_\Omega$;
page-local $\alpha_R$; $\lvert u_{i,j}\rvert=\sqrt{\partial_ju_i\,\partial_ju_i}$, $n$ the wall-normal
direction, $\lvert\boldsymbol\omega\rvert$ the vorticity magnitude):

1. $f_d$, the DDES function with $r_d=\nu(1+\chi)/(\lvert u_{i,j}\rvert\kappa^2d^2)$,
   protects from the viscous sublayer to the log layer (Eq. 26).
2. A second shielding function extends the protection to the wake layer,
   $$f_{P2}=\frac{f_d(2.5\,r_d)}{f_d(r_d)}\,f_d(\mathcal G_{\tilde\nu}),\qquad \mathcal G_{\tilde\nu}=\frac{25}{\lvert u_{i,j}\rvert\,\kappa d}\max\Big(0,-\nu\frac{\partial\chi}{\partial n}\Big)$$
   (Eq. 27); with $f_d$, it gives in the authors' words "a proper RANS
   treatment of attached boundary layers without any restriction on the
   grid spacing".
3. An inhibition function switches the extra shielding off in separated
   regions, where the wake-layer sensor could mistake an early free shear
   layer for a wake layer and delay instabilities:
   $f_R=1$ for $\mathcal G_\Omega\le0.03$, $f_R=0$ for $\mathcal G_\Omega\ge0.04$
   and $f_R=\big[1+\exp\big(6\alpha_R/(\alpha_R^2-1)\big)\big]^{-1}$ in between,
   with $\alpha_R=7-200\,\mathcal G_\Omega$ and the detached-flow sensor
   $\mathcal G_\Omega=\partial_n\lvert\boldsymbol\omega\rvert\,\sqrt{\nu\chi/\lvert u_{i,j}\rvert^3}$
   (Eq. 28). Because vorticity gradients are noisy, $f_R=1$ wherever
   $\lvert\boldsymbol\omega\rvert<0.8\lvert u_{i,j}\rvert$. As $\alpha_R$ runs
   from 1 to $-1$ across the ramp, $f_R$ goes continuously from 1 to 0
   *(compiler check, not in the sources)*.

In LES zones the SA functions take the mode-1 values $f_{v1}=1$, $f_{v2}=0$,
$f_w=1$ (Eqs. 29–30), and two Boolean switches control the transition
(Eqs. 31–35): $\mathrm{test}_\Delta=0$ if $f_d\le0.8$ or
$1-(1-f_{P2})f_R\le0.8$ (else 1), $\mathrm{test}_w=0$ if either is $\le0.2$
(else 1), and

$$\begin{aligned}
f_{v1}&=(1-\mathrm{test}_\Delta)f_{v1}^{\mathrm{RANS}}+\mathrm{test}_\Delta f_{v1}^{\mathrm{mode\,1}},\qquad f_{v2}\ \text{likewise},\\
f_w&=(1-\mathrm{test}_w)f_w^{\mathrm{RANS}}+\mathrm{test}_w\big[100(1-\mathrm{test}_\Delta)+\mathrm{test}_\Delta f_w^{\mathrm{mode\,1}}\big],
\end{aligned}$$

the factor 100 being an enhanced destruction of the RANS eddy viscosity in
grey areas ($\mathrm{test}_w=1$, $\mathrm{test}_\Delta=0$). The authors call
mode 2 (2020) "the only fully-detailed «automatic» formulation in the open
literature" shielding the whole attached boundary layer, the shielding of
ANSYS's SBES/SDES and the switch of the PowerFLOW lattice-Boltzmann VLES
being undisclosed (§1). They state, citing earlier studies, that the DDES
function alone protects only the layer below the log region and fails on
fine meshes or in adverse pressure gradient, typical DES-type methods
protecting insufficiently once $\Delta x\le0.3\delta$ (§2.2, §4.1.2).

**Why lattice Boltzmann grids are a hard test.** Isotropic Cartesian lattice
grids at high Reynolds number are very fine in the wall-parallel directions
relative to $\delta$ ($\Delta<0.01\delta$ is common), so DES-type models
"almost systematically" trigger modelled-stress depletion and a delay in
the formation of instabilities there (§1, §5). The authors list three
reasons why the gradient-based sensors, calibrated in finite-volume
Navier–Stokes solvers, need not carry over: the eddy viscosity enters only
through the relaxation time, a slower destruction of eddy viscosity could
delay instabilities, and the weak numerical noise at the factor-two grid
transitions of octree grids could spuriously activate $f_{P2}$ in shear
layers or $f_R$ inside boundary layers (§2.2 end). The SA equation is
solved by finite differences on the lattice, with the SA analytical wall
law linearized below the interpolation distance as wall model (§2.2, §3.2;
see [lattice Boltzmann methods](/methods/lattice-boltzmann-method.md),
[ProLB](/software/prolb.md) and
[RANS wall functions](/methods/rans-wall-function.md)). Their evidence is
under Applications.

### Grid lengths

The variants differ in the length $\Delta$ that caps the RANS length:

| Variant | $\Delta$ | Source |
|---|---|---|
| DES, DDES | $\Delta_{\max}$ | cited by François et al. (2022, §3.1) and Basile et al. (2023, §2.2) |
| ZDES mode 2 | $\Delta_{\max}$ where $f_d<0.8$, $\Delta_{\mathrm{vol}}$ where $f_d>0.8$ | François et al. (2022), §3.1 |
| ZDES mode 0+1 on high-order DG | $\Delta_{\mathrm{vol}}/(N+1)$, $\Delta_{\mathrm{vol}}$ the cube root of the element volume, $N$ the local polynomial degree; $C_{\mathrm{DES}}=0.65$ | Basile et al. (2023), §2.2 |
| DDES in an edge-based finite-volume code | $\Delta_{\max}$ = longest edge of the dual control volume | Carlsson et al. (2023), §3 |
| SST-DES and SST-DDES in a cell-centred finite-volume code | $\Delta_{\max}$, $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$ | Delassaux et al. (2023), §4.1.3, Eq. 9 |
| IDDES | $\Delta_{dw}$ (Eq. 19 above) | Carlsson et al. (2023), §3 |
| SA-DDES with grey-area mitigation | $\Delta_{\mathrm{SLA}}$ (below), $C_{\mathrm{DES}}=0.65$ | Carlsson et al. (2023), §3.1, §4.4 |
| SST-DDES and transitional DDES in a cell-centred finite-volume code | $\Delta_{\mathrm{SLA}}$, $C_{\mathrm{DES}}=0.65$ | Möller et al. (2024), §II.B.1, Eq. 21 |
| ZDES of the supersonic base flow (Simon et al.) | $\Delta_{\mathrm{vol}}$, $C_{\mathrm{DES}}=0.55$ | cited by Carlsson et al. (2023), §4.4 |
| SST-DES with $F_2$ shielding (ANSYS CFX) | $\Delta_{\max}$, $C_{\mathrm{DES}}=0.61$ | Yang & Ma (2022), §2.1, Eqs. 3–5 |
| SA-DES and SA-DDES in ANSYS Fluent | $\Delta_{\max}$, $C_{\mathrm{DES}}=0.65$ | Pan & Zhang (2023), §II.B–C, Eqs. 7–9 |
| SA-DDES in OpenFOAM | $\Delta_{\max}$, $C_{\mathrm{DES}}=0.65$ | Zhang et al. (2024), §2.3, Eqs. 5–6 |
| SA-IDDES in an unstructured cell-centred finite-volume code (HUNS3D) | IDDES $\Delta=\min[\max(C_wd,C_w\Delta_{\max},\Delta_{wn}),\Delta_{\max}]$, $C_w=0.15$; $\Delta_{\max}=\max(\Delta x,\Delta y,\Delta z)$, not defined for tetrahedra and prisms; $C_{\mathrm{DES}}$ not printed | Li et al. (2024b), §II.B.2, Eq. 4 |
| ZDES mode 2 (2020) on isotropic lattice Boltzmann grids | $\Delta_{\max}$, $\Delta_{\mathrm{vol}}$ or $\Delta_\omega$, "not significant" since $\Delta x=\Delta y=\Delta z$; $C_{\mathrm{DES}}=0.65$ | Husson et al. (2024), §2.2, Eq. 24 |
| RSM-IDDES (SSG/LRR-$\omega$) in a cell-centred finite-volume code | IDDES $\Delta=\min[\max(C_wd,C_w\Delta_{\max},\Delta_{wn}),\Delta_{\max}]$, $C_w=0.15$; $C_{\mathrm{DES}}=0.5F_1+0.3(1-F_1)$ calibrated | Wang et al. (2021), §2.4, §3.1 |
| Dynamic RSM-IDDES (RSM-DynIDDES) in the same code | the same IDDES $\Delta$; $C_{\mathrm{DES}}=C_kC_s$ with dynamic $C_s$, $C_k=2.78$ (LRR) and 1.67 (SSG) | Li et al. (2022), §II B–C, §III A |

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

Wang et al. (2021, §3.1, Fig. 1) calibrate RSM-IDDES on the
Comte-Bellot–Corrsin decay ($64^3$ cells, spectra at $t^*=2.0$) with the
adaptive-dissipation Roe scheme of their applications, which blends low
dissipation in LES regions with stability in RANS regions and itself
contains $C_{\mathrm{DES}}$ (App. A): $C_{\mathrm{DES,SSG}}=0.3$ and
$C_{\mathrm{DES,LRR}}=0.5$ match the spectra, while 0.4, 0.5 and 0.61 (SSG)
and 0.65 and 0.78 (LRR) "yield too much dissipation in the small turbulent
scales". The calibrated values are about half of the theoretical ones; the
authors attribute the difference to numerical dissipation and say the
theoretical value "only provides a reference" (§2.3). With a plain Roe
scheme whose dissipation is reduced to 5%, the same values perform better at
high wavenumbers (App. B, Fig. B1). The direction of a correction follows,
in their reading, from $C_s\approx C_\Delta^{-1}(1.5C_K)^{-3/4}$ (which they
cite; page-local $C_\Delta$, $C_K$ the Kolmogorov constant): reduce
$C_{\mathrm{DES}}$ when the inertial-range level is below experiment (§3.1).
This agrees with Carlsson et al. that the constant is calibrated together
with the scheme, though with lower values.

Li et al. (2022, §III A, Figs. 2–3) repeat the Comte-Bellot–Corrsin test
($64^3$, $Re_M=34\,000$ on the mesh size of the grid, spectra from
$t^*=42$ to the reference $t^*=171$) with the dynamic RSM-IDDES above: the
spectra agree with the experiment up to the high-wavenumber range for both
the SSG and the LRR branch, and descend only "slightly" as $C_k$ grows, so
that the dynamic model is insensitive to $C_k$. They choose
$C_{k,\mathrm{SSG}}=1.67$ and $C_{k,\mathrm{LRR}}=2.78$, which give back the
calibrated $C_{\mathrm{DES}}=0.3$ and 0.5 at $C_s=0.18$
($1.67\times0.18=0.3006$, $2.78\times0.18=0.5004$ *(compiler check, not in
the sources)*). Li et al. do not print $C_{\phi1}$ and $C_{\phi2}$; with the
coefficients printed by Wang et al. (2021, §2.3: $C_{\phi1}=0.44$,
$C_{\phi2}=0.92$ for the $\varepsilon$ branch, $0.55$ and $0.83$ for the
$\omega$ branch, $C_{\ell\varepsilon}=0.09$) the $C_k$ formula of Eq. 9 gives
$3.50$ (SSG) and $4.47$ (LRR), equal to Wang et al.'s theoretical
$C_{\mathrm{DES}}=0.630$ and 0.805 divided by $C_s=0.18$ *(compiler check,
not in the sources)*. The insensitivity is shown on decaying turbulence
only; the hill and buffet cases run with the chosen values.

**An estimate from continuous eddy simulation.** Heinz (2020) writes DES in
$k$-equation form, $Dk/Dt=P_k-\psi_{\mathrm{DES}}\varepsilon+D_k$ with
$\psi_{\mathrm{DES}}=\max\big(1,k^{3/2}/(C_{\mathrm{DES}}\Delta\varepsilon)\big)$,
$C_{\mathrm{DES}}=0.65$ and $D_k$ the diffusion (page-local $\psi_{\mathrm{DES}}$,
$D_k$), and equates its dissipation with that of
[continuous eddy simulation](/methods/continuous-eddy-simulation.md)
([Heinz (2020)](/sources/heinz-2020.md), §3.3, §4.4, Eqs. 22, 53–55):

$$\alpha_\varepsilon-L_+^2(\alpha_\varepsilon-1)=\max\Big(1,\frac{L_+}{C_{\mathrm{DES}}\Delta_+}\Big),$$

with $\alpha_\varepsilon=C_{\varepsilon2}/C_{\varepsilon1}=1.33$ ($k$-$\varepsilon$;
for $k$-$\omega$ the ratio $\alpha_\omega=1.63$, the source's $\beta$),
$\Delta_+=\Delta/L_{\mathrm{tot}}$ and $L_+$ the modelled-to-total length
ratio (page-local $\alpha_\varepsilon$, $\Delta_+$, $L_{\mathrm{tot}}$; $\alpha_\omega$ and $L_+$
registry §11). The solution is
$L_+=\min\big\{[\sqrt{1+4\alpha_\varepsilon(\alpha_\varepsilon-1)C_{\mathrm{DES}}^2\Delta_+^2}-1]/[2(\alpha_\varepsilon-1)C_{\mathrm{DES}}\Delta_+],\,1\big\}$,
which tends to $\alpha_\varepsilon C_{\mathrm{DES}}\Delta_+$ for small $\Delta_+$.
Matching it with the LES length $L=C_+\Delta$ at $C_+=1$ gives
$C_{\mathrm{DES}}=1/\alpha_\varepsilon$, 0.75 for $k$-$\varepsilon$, and
$1/\alpha_\omega$, 0.61 for $k$-$\omega$, which Heinz finds "not far from the
standard value" 0.65 (§4.4, Fig. 5;
$1/1.33=0.752$ and $1/1.63=0.613$ *(compiler check, not in the sources)*).
Heinz draws two
conclusions: the CES forms "generalize DES", and adjusting $\Delta_+$ to
$L_+$ is "absurd", so that DES is unstable under grid variation (§4.4).

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

Fidkowski (2022) removes the grid dependence altogether for an
output-based adaptation study: the SA wall distance is replaced by the
fixed attenuation $d_{\max}\tanh(d/d_{\max})$ with $d_{\max}$ 2% of the chord,
independent of the mesh, "to eliminate modelling variability due to
changing meshes across adaptations"; the author calls the extension to
realistic, mesh-dependent DES models natural but leaves it open
([Fidkowski (2022)](/sources/fidkowski-2022.md), §2.1, Eq. 3, §7). With
this model on a high-lift airfoil ($M=0.2$, $\alpha=17^\circ$, $Re=10^6$),
anisotropic output-based adaptation driven by a field-inversion-corrected
steady surrogate converges the mean lift, where uncorrected RANS
under-predicts it with a larger separation; at the finest meshes the
error estimates exceed the actual error by about a factor of two (§6.3,
Table 3, Fig. 18; see [mesh adaptation](/methods/mesh-adaptation.md)).

## Applications in the sources

- **Cylinder at $Re=1.4\times10^5$ as a reference** (Ghidoni et al. 2022).
  The SA-DES of Travin et al., in laminar-separation and
  turbulent-separation variants, is one of the reference results for the
  two-dimensional URANS of the cylinder, beside experiments, RANS–ILES and
  LES ([Ghidoni et al. (2022)](/sources/ghidoni-2022.md), §6.2, Table 12;
  see Qualifications on the citation). The authors name hybrid RANS/LES
  among the motivations and future targets of their adaptive time
  integration.
- **Shielding function rejected as a feature** (He et al. 2022). For a
  learned eddy-viscosity correction of SA-QCR, He et al. consider the DDES
  shielding function $f_d$ as a wall-proximity input and reject it as
  "mostly binary", using the SA function $f_w$ instead
  ([He et al. (2022)](/sources/he-2022-b.md), §2.6; see the
  [Spalart–Allmaras page](/methods/spalart-allmaras-model.md)).
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
  radius $R$. The authors cite earlier runs: DESider SA-DES with $\Delta_{\max}$ and
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
- **Ahmed body**, as reported by Delassaux et al. (2023, §5, Table 2) from
  their own calibration on four 25° bodies (sharp and rounded edges): RANS
  gives no separation (realizable $k$-$\varepsilon$) or massive separation
  (SST) on the slant; scale-adaptive simulation overestimates and
  stress-blended eddy simulation underestimates the recirculation length;
  SST-DDES is closest, with maximum errors of 3.3% in drag and 7.1% in lift
  on a 20-prism-layer grid. Time steps of $1.5\times10^{-5}$ and
  $5\times10^{-5}$ s give globally the same results, while a CFL number
  above 10 gives no or massive separation on the slant (see
  [Ahmed body](/benchmarks/ahmed-body.md)).
- **Ahmed body**, as cited by Cai et al. (2022, §I). Menter & Kuntz
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
- **Transonic buffet**, as cited by Petrocchi & Barakos (2024, §1) for
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
- **Dynamic stall**, as cited by Baldan & Guardone (2025, Introduction):
  the DES best practice of Shur et al. requires a span of at least one
  chord to reproduce the dynamic-stall vortex, a requirement the authors
  confirm for wall-resolved LES of a pitching NACA 0012 in the downstroke
  ([Baldan & Guardone (2025)](/sources/baldan-2025.md), §2.1; arXiv v2; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Wind-turbine noise**, as cited by Rismondo et al. (2025, §1): Nelson
  et al. used delayed DES with Farassat's linear acoustic formulation for a
  full wind turbine ([Rismondo et al. (2025)](/sources/rismondo-2025.md),
  §1; see [Ffowcs Williams–Hawkings acoustic analogy](/methods/ffowcs-williams-hawkings-acoustic-analogy.md)).
- **Tandem cylinders and a launch-vehicle buffet** (Wang et al. 2021,
  §3.2–§3.3). On the ATAAC tandem cylinders ($L=3.7D$, $M=0.1285$,
  $Re_D=1.6\times10^5$, 11.1 million cells) RSM-IDDES and SST-IDDES give
  "almost identical" mean $C_p$; RSM-IDDES gives better $C_p$ RMS peaks on
  the downstream cylinder, an earlier shear-layer instability closer to the
  PIV, and a primary shedding frequency of 176 Hz against 172 Hz for
  SST-IDDES and 179 Hz (upstream sensor) and 180 Hz (downstream sensor)
  measured, with sound pressure levels 114.3 and 136.8 dB against 115.6 and
  137.6 dB (SST-IDDES) and 116.5 and 138.6 dB measured (Table 1, Figs. 4–6;
  see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)). On
  the NASA Model 11 hammerhead at $M=0.81$, $Re=4.2\times10^6$ (18.5 million
  cells), RSM-IDDES has smaller subgrid stresses in all components, an
  earlier Kelvin–Helmholtz instability, a shorter shear layer and a smaller
  separation bubble, and places the $C_p$ RMS peak at $x=0.58$, the position
  estimated from experiment, against 0.62 for SST-IDDES; both overpredict
  its magnitude, RSM-IDDES less. Both resolve more than 80% of the kinetic
  energy along the extraction line (Figs. 9–14).
- **Periodic hill and launch-vehicle buffet with a dynamic constant** (Li
  et al. 2022, §III B–C). On the [periodic hill](/benchmarks/periodic-hill.md)
  ($Re=10\,595$ on the hill height and crest velocity, $M=0.1$,
  $160\times115\times60$ cells, about 1.1 million, first-cell $\Delta y^+<1$,
  $\Delta x^+$ and $\Delta z^+$ mostly below 35), RSM-IDDES and the dynamic
  RSM-IDDES both match the mean streamwise velocity of the Breuer et al.
  experiment and of the DNS and wall-resolved LES of Balakumar et al.,
  except near the lower wall at $x=4$, where both follow the wall-modelled
  LES instead; the resolved Reynolds stresses of the dynamic model are closer
  to the references, near the lower wall within their spread and close to
  the wall-modelled LES, while RSM-IDDES underpredicts the streamwise normal
  stress at $x=8$; $Q$-criterion fields show more small-scale structures
  (Table I, Figs. 7–12). On the
  [hammerhead launch vehicle](/benchmarks/hammerhead-launch-vehicle-buffet.md)
  ($M=0.81$, $Re=4.0\times10^6$ on the 12-in first-stage diameter, against
  $4.2\times10^6$ printed by Wang et al., see the contradiction on that
  page; the grid of Wang et al.), the dynamic model keeps the shear-layer break point and
  the reattachment line of RSM-IDDES, both upstream of SST-IDDES, has smaller
  modelled subgrid stress in the vortex region, more high-frequency PSD
  along the shear layer and the largest high-wavenumber share of the
  energy spectrum; the mean $C_p$ is "essentially" that of RSM-IDDES, and at
  the location of the experimental $C_p$-RMS maximum the RMS is 0.0554
  against 0.0719 (RSM-IDDES), 0.0897 (SST-IDDES) and 0.0454 measured (Coe &
  Nute) (Figs. 15–22). The authors attribute the later break-up of
  SST-IDDES to its larger modelled stress in the shear-layer extension,
  after Spalart's viewpoint, and conclude that the dynamic model "only
  improves the prediction of the high-frequency part" (§III C, §IV).
- **30P30N high-lift airfoil, IDDES against LES and SATES** (Wu et al. 2023,
  §3.4). On the [30P30N airfoil](/benchmarks/30p30n-high-lift-airfoil.md)
  ($Re=1.71\times10^6$, $M=0.17$, $\alpha=5.5^\circ$, 27 million cells,
  fourth-order linear-weight [WCNS](/methods/weighted-compact-nonlinear-scheme.md)),
  SST-IDDES (Gritskevich et al.'s length, Eq. 9) gives $C_L=2.27$, 19.8%
  below the experimental mean 2.83, against $-6.7\%$ for Smagorinsky LES and
  $-0.4\%$ for the self-adaptive turbulence eddy simulation (Table 2). It
  separates early on the flap suction side (attributed to grid-induced
  separation), misses the small separation bubble on the main element,
  carries larger $\mu_t/\mu$ in the attached boundary layers and
  considerable eddy viscosity in the slat cove, which delays the transition
  of the slat shear layer, and resolves the least kinetic energy of the
  three; the authors conclude that a hybrid RANS/LES "could be worse than the
  LES" on this case (Figs. 17–25; see
  [hybrid RANS/LES](/definitions/hybrid-rans-les.md)).
- **Industrial practice** (Mani & Dorgan 2023, §4.5.2). DES and then DDES
  have carried unsteady simulation at Boeing, on SA and SST hosts; hybrid
  RANS/LES remains "a workhorse for most unsteady simulations in industry"
  but is too expensive for the many flight conditions of a database, and
  "has also struggled at times" to predict separation and reattachment in
  smooth-body separation, where the authors see
  [wall-modelled LES](/methods/wall-modelled-les.md) as the promising route.
- **Turbine tip-leakage vortex** (Yang & Ma 2022). SST-DES of one passage
  of a transonic high-pressure turbine rotor cascade (exit isentropic Mach
  0.95, tip gap $0.07c$, $y^+\approx1$, $\Delta t=10^{-6}$ s) resolves the
  wandering of the tip-leakage vortex, with a single characteristic
  frequency of about 2200 Hz upstream of breakdown, and a "spiral-type"
  breakdown near the trailing edge promoted by the shock-enhanced adverse
  pressure gradient (§4.1, Figs. 10–11). Mesh adequacy is argued on one grid
  from the central/upwind blending factor, near zero in the vortex and
  wake, and from $-5/3$ ranges in velocity spectra (§3.1, Figs. 4–5); only
  the midspan isentropic Mach number is compared with experiment (Fig. 6).
  See [turbine cascades](/benchmarks/turbine-cascade.md).
- **Capsule wakes**, as cited by Placco et al. (2023, §1). DES of
  planetary-entry capsule wakes was restricted to the near-body wake and
  disagreed with experiment in the backshell area, which the cited work
  attributed to the model's prediction of transition after shoulder
  separation ([Placco et al. (2023)](/sources/placco-2023.md), §1).
- **ZDES mode 2 (2020) in a lattice Boltzmann solver** (Husson et al.
  2024, §4). *Flat plate* (NASA TMR, $Re_L=5\times10^6$, $M=0.2$,
  $\Delta y^+\approx30$ at $x/L=1$, $\Delta x\approx0.01\delta$ at
  mid-plate): skin friction, velocity and eddy-viscosity profiles are
  identical to lattice-Boltzmann RANS, also with $C_{\mathrm{DES}}=0$ and on an
  inclined, staircased plate, while DDES (2006) on the same grid suffers
  severe modelled-stress depletion, the layer tending to laminar while the
  wall law imposes a turbulent profile, with an "unexploitable" oscillating
  $C_f$ (§4.1.2, Figs. 4–5). *Backward-facing step* of the A3C combustor
  ($Re_h=40{,}000$ on the step height $h$, $\delta=0.37h$ at separation): with
  44.7 million wall-modelled lattice nodes against 3.9 million wall-resolved
  cells of Deck & Renard's finite-volume ZDES, the a priori shielding field,
  the vorticity thickness, the destruction of eddy viscosity and the mean
  profiles agree, and the authors conclude that the lattice Boltzmann
  transposition adds no further delay in the formation of instabilities;
  the near-wall differences at the first station are attributed to the
  equilibrium wall model in the recirculation (§4.2, Table 1, Figs. 7–11;
  see [backward-facing step](/benchmarks/backward-facing-step.md)).
  *LEISA2 three-element high-lift airfoil* ($Re_c\approx1.23\times10^6$,
  $M=0.178$, $\alpha=6.15^\circ$, 77 million nodes against $2.6\times10^9$ for
  a wall-resolved LES): attached layers on slat and flap stay in RANS
  without grid-induced separation, the mean $C_p$ agrees with experiment,
  and a slight delay of instabilities in the slat shear layer is
  attributed to grid and wall model rather than to the model, because a
  lattice-Boltzmann wall-modelled LES shows "the exact same phenomenon"
  (§4.3, Figs. 13–19).
- **Centrifugal impeller in rotating stall** (Pan & Zhang 2023). SA-based
  DES and DDES with Fluent defaults on a six-blade low-specific-speed
  impeller at 25% of design flow (12.33 million cells, maximum $y^+\approx1.2$,
  one degree of rotation per step, three revolutions averaged), against a
  dynamic-Smagorinsky LES on the same grid. Both capture the alternate
  stall of neighbouring passages. DDES vortex patterns (streamlines) are
  closer to the LES, while the DES $Q$ field agrees better and DDES
  overpredicts it and lacks small scales; DES better reproduces the
  leading-edge low-pressure region; in the mean radial velocity DES tends to
  overpredict and DDES to underpredict the reversed flow, with peak-to-valley
  differences about 10% off the LES; DES is closer for the RMS fluctuations,
  which DDES underpredicts. The authors conclude that no universal ranking
  exists (§IV, §V, Figs. 9–15). The reference LES itself shows "remarkable
  discrepancy" with the PIV data, attributed to a different rig (§III.C;
  see Qualifications and [large-eddy simulation](/definitions/large-eddy-simulation.md)).
- **Dynamic-stall onset with transition models** (Batther & Lee 2022).
  DDES in NASA's OVERFLOW 2.3 (fifth-order central differences with scalar
  dissipation, 30 sub-iterations, $\Delta t^*=2.56\times10^{-4}$ on the
  convective time) of a NACA 0012 pitching up at a constant rate,
  $Re=2\times10^5$, $M=0.1$, span $0.1c$, compared with the wall-resolved LES
  of Visbal & Garmann on its setup; the DDES formulation is not printed.
  On a 16.2-million-point grid (about 22% of the LES points, upper-surface
  averages $\Delta x^+=17.6$, $\Delta y^+=0.375$, $\Delta z^+=7.22$), with the
  SST Langtry–Menter, SA Medida–Baeder, SA amplification-factor-transport
  and fully turbulent SA closures, DDES reproduces the sequence of the LES
  (upstream motion of transition, leading-edge laminar separation bubble,
  its bursting, roll-up and shedding of the dynamic-stall vortex) but
  stalls slightly earlier with a slightly lower peak lift, with a larger
  bubble of weaker reverse flow, earlier suction collapse and faster vortex
  convection. The authors report about 1500 CPU hours against "several
  million" for the LES ([Batther & Lee (2022)](/sources/batther-2022.md),
  §2–§4, Tables 1–3, Figs. 4, 14, 17; see
  [dynamic stall](/definitions/dynamic-stall.md),
  [laminar separation bubble](/definitions/laminar-separation-bubble.md) and
  [transition models](/methods/local-correlation-based-transition-model.md)).
- **Hovering rotor on moving Cartesian grids** (Sugaya & Imamura 2021).
  DDES-p of the two-bladed
  [Caradonna–Tung rotor](/benchmarks/caradonna-tung-rotor.md) (tip Mach
  0.439, collective $8^\circ$, $Re=4.44\times10^6$, fully turbulent) on 75
  and 149 million cells of a hierarchical Cartesian grid moving rigidly with
  the blades, with immersed-boundary wall functions ($y^+$ at the image
  point up to about 500 on the coarser grid), 3600 steps per revolution and
  averages over the last four of 22 revolutions: thrust coefficient
  0.00514–0.00521 and figure of merit 0.594–0.618 over the two grids and two
  schemes, $C_p$ at five stations and tip-vortex trajectories in agreement
  with experiment, and finer wake vortices with secondary braids with the
  high-order scheme than with MUSCL, the authors concluding that "the
  numerical scheme greatly affects the prediction of the wake structure"
  (§4, Tables 6–7, Figs. 17–19; see
  [immersed boundary methods](/methods/immersed-boundary-method.md)). The
  high-order runs took 99 h against 63 h with MUSCL for the last
  revolutions, on 896 and 1792 cores (Table 6).
- **Separated benchmarks, compiled** (Heinz 2020, §5). On the NASA
  wall-mounted hump the compiled DES reattachment lengths lie at
  1.114–1.152 chords against 1.10 measured, and DES, like wall-modelled
  LES, misses the double peak of $C_f$; on the NACA 4412 airfoil a DES
  under-predicts drag by more than 34% (§5.2, §5.4, Table 3; see
  [NASA wall-mounted hump](/benchmarks/nasa-wall-mounted-hump.md),
  [NACA 4412 airfoil](/benchmarks/naca-4412-airfoil.md) and the
  compilation on the [hybrid RANS/LES page](/definitions/hybrid-rans-les.md)).
- **High-speed fin with joint freeplay** (Thawait et al. 2023). The Fluent
  SST-DDES above, with AUSM+ fluxes, second-order upwind convection and dual
  time stepping, carries the flow side of a strongly coupled
  fluid–thermal–structure analysis of a deployable cropped-delta fin at
  Mach 3–6 (15 km altitude), on a 2.7-million-cell tetrahedral grid chosen
  by a three-grid convergence index on wall pressure and temperature (§II,
  §VI A, Table II). The authors adopt DES because RANS models are "not
  suitable" for shock and separation unsteadiness and shock/boundary-layer
  interaction, citing Sartor & Timme (§I). The paper shows no shielding
  field, resolution argument for the LES branch or RANS comparison; its
  validations test the structural response (§V), and the turbulent kinetic
  energy it discusses is the modelled $k$ (§VI B, Fig. 10).
- **Drag crisis of a cylinder** (Mays et al. 2023). The SRH model above,
  not a DES, on the Lag elliptic-blending $k$-$\varepsilon$ host, gives drag
  close to a wall-resolved LES at $Re_D=2.5$–$7.2\times10^5$ on meshes about
  five times coarser, and on the coarsest grid at $Re_D=2.5\times10^5$
  $C_D=0.743$ where WALE LES on the same grid gives 1.247 (reference 0.833),
  at about 39% of the CPU cost of WALE on the finest grid (§3.1, Tables 2–4;
  see [circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)).
- **NASA CRM high-lift configuration and its vortex system** (Li et al.
  2024b). SA-IDDES and steady SA-RANS of the HLPW-4 landing configuration
  (inboard and outboard flaps $40^\circ$/$37^\circ$, $M=0.2$, $Re=5.49\times10^6$
  on the mean aerodynamic chord, $\alpha=7.05^\circ$) on the 276-million-cell
  level-C workshop mesh (first $y^+\le1$, 6000 MPI partitions), with a
  second-order low-Mach-preconditioned Roe scheme and dual time stepping
  (§III.A–C; time step and averaging window not printed). Sectional $C_p$ of
  both agrees with the corrected wind-tunnel data except at the inboard flap
  bracket ($\eta=0.33$), where SA-RANS underestimates the flap leading-edge
  $C_p$ by overpredicting the separation behind the bracket; the drag is
  0.1843 (IDDES), 0.1867 (RANS) and 0.1868 measured, IDDES having the lower
  friction drag (0.0151 against 0.0165); a DES drag below the RANS one also
  appears in the DDES of Probst et al. (as cited, $C_D=0.1793$)
  (§III.D.1–2, Figs. 5–6). IDDES resolves hairpin-like
  vortex "forests" over the inboard wing and in slat-bracket wakes, the
  nacelle-strake vortex over almost the whole upper surface, tip vortices, a
  horseshoe vortex at the lower wing–fuselage junction and Kelvin–Helmholtz
  wake vortices, where RANS captures only the strong tip vortices; the
  authors tie the larger RANS flap separation to the undisturbed flap-bracket
  tip vortex (§III.D.3, Figs. 8–14). One grid and one incidence, no grid or
  time-step study. See the [NASA CRM high-lift configuration](/benchmarks/nasa-crm-high-lift.md).
- **Compressor tandem cascade tip flow** (Zhang et al. 2024). SA-DDES in
  [OpenFOAM](/software/openfoam.md) of a NACA 65-K48-based tandem cascade with
  1% tip clearance ($M=0.67$, $Re=5.6\times10^5$; 6.65 million cells,
  $\Delta x^+<80$, $\Delta y^+<0.5$, $\Delta z^+<130$ near the tip, $\Delta t=10^{-6}$ s,
  about 180 steps per characteristic period, mean Courant number 0.65),
  validated only on the clearance-free K48 cascade against oil flow and loss
  measurements, where the corner-separation extent is captured and the
  loss in the corner "slightly" under-predicted (§2.2–§2.4, Figs. 5–7). The
  DDES is a tool for the tip-leakage vortex system (a second, counter-rotating
  leakage vortex in the rear-blade passage; a 20.05% lower loss); no RANS or
  LES comparison is run (§3). See [compressor cascades](/benchmarks/compressor-cascade.md).
- **Three-dimensional shock interactions**, as cited by Sabnis & Babinsky
  (2023, §3.2–§3.3): DES of a Mach 4 double fin found significant
  low-frequency unsteadiness related to closed separation regions (Adler &
  Gaitonde), and DES of a Mach 3 blunt fin attributed low-frequency
  separation-shock motion to the separation region and high-frequency
  motion to the incoming boundary layer (Ngoh & Poggie); their §4.4 calls
  Garnier's computation of a duct interaction "large-eddy simulations"
  while the cited title is "Stimulated detached eddy simulation"
  ([Sabnis & Babinsky (2023)](/sources/sabnis-2023.md); see
  [shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)).
- **Stall of a high-lift airfoil and a supercritical cylinder, IDDES against
  SATES-σ** (Wu et al. 2024). SST-IDDES is the comparator of the
  σ-weighted [SATES](/methods/self-adaptive-turbulence-eddy-simulation.md):
  on the cylinder at $Re_D=3\times10^6$ it gives $C_D=0.62$, $St=0.29$,
  $L_r/D=0.63$ (SATES-σ 0.55, 0.24, 0.79), and on the MD-30P30N at $21^\circ$ a
  $C_p$ farther from experiment than SATES-σ (§3.2–§3.3, Table 3, Fig. 22).
  The authors cite transitional and turbulent DDES that "did not show an
  appropriate drop in lift after stall", the thick RANS layer giving too much
  eddy viscosity (§1, §3.3), and concede that DDES, closer to URANS, is less
  grid-sensitive for transition than their near-LES model (§4)
  ([Wu et al. (2024)](/sources/wu-2024.md)).
- **One-dimensional-turbulence review.** Chen et al. (2024b) cite DES, DDES
  and IDDES among near-wall approaches and show a DES region in a
  comparison diagram, without results
  ([Chen et al. (2024b)](/sources/chen-2024-c.md), §3.3, Fig. 13, §4.1; see
  [one-dimensional turbulence](/methods/one-dimensional-turbulence.md)).
- **Near-wall model taxonomy** (Maeyama & Kawai 2023). Maeyama & Kawai
  class DES (Spalart 1997, 2009) among the LES/RANS hybrids that blend RANS
  and subgrid eddy viscosities, with the switching location set explicitly
  or implicitly, and restrict "wall-modelled LES" to wall-stress models
  ([Maeyama & Kawai (2023)](/sources/maeyama-2023.md), §1; see
  [wall-modelled LES](/methods/wall-modelled-les.md)).

## Qualifications

- Li et al. (2024b) validate on one grid level and one incidence, with
  neither time step nor averaging window printed; their conclusion that IDDES
  "basically satisfies the engineering simulation requirements" (§IV) rests
  on that case. Their judgement that zonal hybrids are intractable for
  high-lift configurations (§I) is a statement, not a test. They call the
  wake vortices "a prominent source of airframe noise in the cruising stage"
  of a landing configuration (§III.D.3).
- Zhang et al. (2024) take the accuracy of DDES for tip-leakage flow from a
  cited rotor study, not from their own validation, which has no clearance
  (§2.4).
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
- François et al. (2022), Basile et al. (2023) and Mozaffari et al. (2022)
  do not print the DES equations in full; Mozaffari et al. (2022) print
  none. Carlsson et al. (2023) print the DDES
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
  base-flow studies cited by Carlsson et al. use 0.55 with
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
- Wang et al. (2021) print the subscript of the $k$-$\omega$ constant of
  their Eq. 18 as "$C_{DES,k-\varpi}$"; they say the pressure-fluctuation
  magnitude is captured "by both DDES within 1.8% error margin" for two
  IDDES runs, while their Table 1 gives 114.3 dB against 116.5 dB for
  RSM-IDDES at the upstream sensor, a difference of 1.89% *(compiler check,
  not in the sources)*; and the text compares with "experimental data
  (180 Hz)" where Table 1 lists 179 Hz and 180 Hz for the two sensors
  (§3.2). The SST-IDDES values of $C_{\mathrm{DES}}$ used in their
  comparisons are not printed.
- Yang & Ma (2022) print a grid of $169\times155\times404$ points and "about
  13 million" cells; the product is $1.06\times10^7$ *(compiler check, not
  in the sources)*; the 69-layer tip-gap block is not counted separately in
  the text.
- Pan & Zhang (2023) state in the abstract that DDES is "superior in
  resolving ... the fluctuation quantities", while their §IV.C and
  conclusion find DES closer to the LES for the RMS fluctuations and DDES
  underpredicting them; the page follows the body. Their ranking measures
  closeness to an LES on the same grid with the same rotor treatment and
  statistics from three revolutions (one for RMS), and their conclusion
  calls DES and DDES "well validated against available experimental data"
  although only the LES is compared with experiment (§III.C, §V).
- Batther & Lee (2022) state in §2.1 that their time step is "one order of
  magnitude larger" than the LES one and in §4.5 that it is "roughly 8%" of
  it; they also give "roughly 20 s per time step using 192 cores" for
  35,000 steps and "about 1500 total CPU hours", although the first two
  figures multiply to about 37,000 core-hours on the 192 cores
  *(compiler check, not in the sources)*.
- Husson et al. (2024) give the wall-resolved LES of the LEISA2 airfoil as
  $2.6\times10^9$ nodes (p. 15) and "$2700\cdot10^6$" (p. 18).
- Zangeneh (2021) attributes two statements to "Peterson and Candler" with
  the reference number 7, which in its list is Mockett, Fuchs & Thiele
  (2012); Peterson & Candler are its ref. 9 (§I).
- Heinz's verdicts on DES (unstable under grid variation, an "absurd"
  grid adjustment, a framework "too narrow") are stated after the CES–DES
  equivalence above (§4.4); the review runs no simulations, and its DES
  results on the hump and the NACA 4412 are compiled from other authors'
  runs (§5).
- Sugaya & Imamura (2021) do not print the DDES-p shielding function, whose
  origin is a Japanese-language conference paper and an AIAA paper they
  cite (§2.1).

- Ghidoni et al. (2022) attribute the Travin et al. SA-DES cylinder results
  of their Table 12 to their reference 44, which is printed as a DES of an
  airfoil at high angle of attack by Shur, Spalart, Strelets and Travin.
- The "DES" of Fidkowski (2022) has no grid length: it is a RANS model
  with a capped wall distance, and conclusions on mesh adaptation drawn
  with it do not transfer directly to grid-dependent DES, as the author
  states (§2.1, §7).
- Li et al. (2022) print the hammerhead Reynolds number as $4.0\times10^6$
  on the 12-in diameter (§III C), Wang et al. (2021, §3.3) $4.2\times10^6$
  for the same configuration and grid; the conflict is recorded, open, under
  Contradictions on the
  [hammerhead launch-vehicle buffet](/benchmarks/hammerhead-launch-vehicle-buffet.md)
  page. Li et al. use $M_{ij}$ both for the
  fluctuating mass-flux term of the Reynolds-stress equation (Eq. 2) and for
  the model tensor of the dynamic procedure (Eqs. 10, 12), and write after
  Eq. 9 that $C_{\mathrm{DES}}$ affects "the quantity of coefficient $C_k$ of
  the Smagorinsky model", where their Eq. 9 makes $C_s$ the Smagorinsky
  coefficient. Their resolved stress (Eq. 11) is printed with the test
  filter of the product subtracted, the opposite ordering of the registry's
  $L_{ij}$, with the model tensor of Eq. 12 signed to match. The authors
  credit the improvement of the fluctuations to the dynamic subgrid
  dissipation; the runs use a second-order Roe scheme (§II A, §IV).
- Mani & Dorgan (2023) call the modified quantity "the $f_d$ coefficient"
  (§4.5.2) while their Fig. 11 labels the variants $(4r_d)^3$, $(8r_d)^3$ and
  $(16r_d)^3$: the constant changed is the factor multiplying $r_d$ inside
  $f_d$. Their review prints no equations, and the serpentine-inlet flow
  conditions are not given.
- On the 30P30N airfoil at $M=0.17$, $Re\approx1.7\times10^6$,
  $\alpha=5.5^\circ$, Wang et al. (2024) report their SA-DDES with a
  sixth-order upwind scheme in agreement with the measured $C_p$ and
  slat-cove profiles, and Wu et al. (2023) report their SST-IDDES with a
  fourth-order linear-weight WCNS on a span of $C/9$ and 27 million cells
  19.8% low in lift with early flap separation (Table 2). Wu et al. cite a
  successful IDDES of the airfoil by Ashton et al. without discussing the
  difference (see the [30P30N](/benchmarks/30p30n-high-lift-airfoil.md)
  page for the two set-ups).
- Thawait et al. (2023) give no value or formula for $\beta^*$ ("calculated
  using $\rho$, $k$, $\mu$, and $\omega$"), $\alpha^*$, $a_1$ or $F_2$ and
  define $\Delta_{\max}$ only as "the grid spacing"; their wall distance is
  $y$ in $r_d$ (Eq. 13) and $d$ in $d_{\mathrm{DDES}}$ (Eq. 14).
- Mays et al. (2023) attribute the SRH model to Manceau (2018) in the
  abstract and to Duffal et al. (2019) in the introduction and §2.1.2.

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
- [Wang et al. (2021)](/sources/wang-2021-l.md) — §2.3 Eqs. 11–18, §2.4 Eqs. 19–20, §3.1 Fig. 1, §3.2 Table 1 Figs. 4–6, §3.3 Figs. 9–14, App. A–B Fig. B1.
- [Yang & Ma (2022)](/sources/yang-2022-b.md) — §2.1 Eqs. 1–5, §3.1 Figs. 4–6, §4.1 Figs. 10–11.
- [Husson et al. (2024)](/sources/husson-2024.md) — §1, §2.2 Eqs. 24–35, §3.2, §4.1–4.3 Table 1 Figs. 4–19, §5.
- [Pan & Zhang (2023)](/sources/pan-2023.md) — §II.B–C Eqs. 7–11, §III.C, §IV Figs. 9–15, §V.
- [Batther & Lee (2022)](/sources/batther-2022.md) — §2–§4, Tables 1–3, Figs. 4, 14, 17.
- [Lodares et al. (2022)](/sources/lodares-2022.md) — §8.
- [Tomboulides et al. (2025)](/sources/tomboulides-2025.md) — §4.
- [Zangeneh (2021)](/sources/zangeneh-2021.md) — §I, §II.A–B Eqs. 1, 5–7.
- [Sugaya & Imamura (2021)](/sources/sugaya-2021.md) — §2.1, §4, Tables 6–7, Figs. 17–19.
- [Heinz (2020)](/sources/heinz-2020.md) — §3.3 Eq. 22, §4.4 Eqs. 53–55 Fig. 5, §5.2, §5.4 Table 3.
- [Fidkowski (2022)](/sources/fidkowski-2022.md) — §2.1 Eq. 3, §6.3 Table 3 Fig. 18, §7.
- [Ghidoni et al. (2022)](/sources/ghidoni-2022.md) — §6.2 Table 12.
- [He et al. (2022)](/sources/he-2022-b.md) — §2.6.
- [Li et al. (2022)](/sources/li-2022-k.md) — Abstract, §I, §II B–C Eqs. 5–15 Fig. 1, §III A Figs. 2–3, §III B Table I Figs. 7–12, §III C Figs. 15–22, §IV, App. 1–2 Figs. 23–24.
- [Mani & Dorgan (2023)](/sources/mani-2023.md) — §4.5.2, Fig. 11.
- [Wu et al. (2023)](/sources/wu-2023-b.md) — §1, §2.1.3 Eq. 9, §3.4 Table 2 Figs. 17–25.
- [Thawait et al. (2023)](/sources/thawait-2023.md) — §I, §II B Eqs. 9–14, §V, §VI A–B Table II Fig. 10.
- [Mays et al. (2023)](/sources/mays-2023.md) — Abstract, §1, §2.1.2 Eqs. 9–13, §3.1–§3.2.2 Tables 2–4 Figs. 5, 10a.
- [Maeyama & Kawai (2023)](/sources/maeyama-2023.md) — §1.
- [Li et al. (2024b)](/sources/li-2024-f.md) — §I (seamless against zonal hybrids); §II.B.2, Eq. (4) (SA-IDDES, $C_w=0.15$); §III.A–D, Figs. 5–14 (CRM-HL loads, drag, vortex system); §IV.
- [Zhang et al. (2024)](/sources/zhang-2024.md) — §2.2–§2.4, Eqs. (3)–(8), Figs. 5–7 (SA-DDES formulation, grid and time step, K48 validation); §3.
- [Sabnis & Babinsky (2023)](/sources/sabnis-2023.md) — §3.2–§3.3 (DES of double and blunt fins, as cited); §4.4 (stimulated DES cited as LES).
- [Wu et al. (2024)](/sources/wu-2024.md) — §1, §3.2–§3.3, Table 3, Fig. 22, §4 (SST-IDDES against SATES-σ; DDES after stall, as cited).
- [Chen et al. (2024b)](/sources/chen-2024-c.md) — §3.3, Fig. 13; §4.1 (DES family cited).
